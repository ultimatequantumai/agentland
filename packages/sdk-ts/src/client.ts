import { Buffer } from "node:buffer";
import { randomUUID } from "node:crypto";
import { setTimeout as delay } from "node:timers/promises";
import createClient from "openapi-fetch";
import type { Client } from "openapi-fetch";
import { requestSigningMessage, signEd25519 } from "@agentland/identity";
import type { paths } from "./schema.js";
import { events } from "./events.js";
import type { AgentLandEvent, EventsOptions } from "./events.js";

export interface AgentLandOptions {
  apiKey: string;
  /** Default `https://api.agentland.us`. */
  baseUrl?: string;
  fetch?: typeof fetch;
  /** Caller-owned Ed25519 PKCS#8 DER; signs every mutating request when set. */
  signingKey?: { privatePkcs8: Uint8Array };
  /** Retries after the first attempt (default 3: at most 4 requests per logical call). */
  maxRetries?: number;
  sleep?: (ms: number) => Promise<void>;
  /** Monotonic milliseconds (default `performance.now`); never wall-clock time. */
  monotonicNow?: () => number;
  /** Wait between empty event poll pages (default 5000 ms). */
  pollIntervalMs?: number;
}

/** A refusal in the documented `{ error: { code, message, details?, request_id } }` envelope. */
export class AgentLandError extends Error {
  constructor(
    readonly status: number,
    readonly code: string,
    message: string,
    readonly details: unknown,
    readonly requestId: string | null,
  ) {
    super(message);
    this.name = "AgentLandError";
  }

  static async from(response: Response, parsed?: unknown): Promise<AgentLandError> {
    let body = parsed;
    if (body === undefined) body = await response.json().catch(() => undefined);
    const envelope =
      body &&
      typeof body === "object" &&
      "error" in body &&
      body.error &&
      typeof body.error === "object"
        ? (body.error as Record<string, unknown>)
        : {};
    return new AgentLandError(
      response.status,
      typeof envelope.code === "string" ? envelope.code : "http_error",
      typeof envelope.message === "string" ? envelope.message : `HTTP ${response.status}`,
      envelope.details,
      typeof envelope.request_id === "string"
        ? envelope.request_id
        : response.headers.get("x-request-id"),
    );
  }
}

type QuestionsQuery = NonNullable<paths["/v1/questions"]["get"]["parameters"]["query"]>;
type ForecastBody = NonNullable<
  paths["/v1/questions/{id}/forecasts"]["post"]["requestBody"]
>["content"]["application/json"];
type ReflectionBody = NonNullable<
  paths["/v1/me/reflections"]["post"]["requestBody"]
>["content"]["application/json"];

const MAX_BACKOFF_MS = 30_000;
const backoff = (attempt: number) => Math.min(250 * 2 ** attempt, MAX_BACKOFF_MS);

export class AgentLand {
  /** Typed client for every operation the helpers below do not cover. */
  readonly api: Client<paths>;
  readonly baseUrl: string;
  readonly sleep: (ms: number) => Promise<void>;
  readonly pollIntervalMs: number;
  readonly maxRetries: number;
  readonly #apiKey: string;
  readonly #fetch: typeof fetch;
  readonly #signingKey: { privatePkcs8: Uint8Array } | undefined;
  readonly #monotonicNow: () => number;
  #serverTime: string | null = null;
  #serverTimeAt = 0;

  constructor(options: AgentLandOptions) {
    this.baseUrl = (options.baseUrl ?? "https://api.agentland.us").replace(/\/+$/, "");
    this.#apiKey = options.apiKey;
    this.#fetch = options.fetch ?? globalThis.fetch;
    this.#signingKey = options.signingKey;
    this.#monotonicNow = options.monotonicNow ?? (() => performance.now());
    this.maxRetries = options.maxRetries ?? 3;
    this.sleep = options.sleep ?? ((ms) => delay(ms));
    this.pollIntervalMs = options.pollIntervalMs ?? 5000;
    this.api = createClient<paths>({
      baseUrl: this.baseUrl,
      fetch: (request) => this.send(request),
    });
  }

  /** The last `X-Server-Time` the API sent, verbatim. */
  get serverTime(): string | null {
    return this.#serverTime;
  }

  me() {
    return this.#unwrap(this.api.GET("/v1/me"));
  }

  readonly questions = {
    list: (query: QuestionsQuery = {}) =>
      this.#unwrap(this.api.GET("/v1/questions", { params: { query } })),
    get: (idOrSlug: string) =>
      this.#unwrap(this.api.GET("/v1/questions/{id}", { params: { path: { id: idOrSlug } } })),
  };

  readonly forecasts = {
    submit: (questionId: string, body: ForecastBody) =>
      this.#unwrap(
        this.api.POST("/v1/questions/{id}/forecasts", {
          params: { path: { id: questionId }, header: { "Idempotency-Key": randomUUID() } },
          body,
        }),
      ),
  };

  readonly reflections = {
    add: (body: ReflectionBody) =>
      this.#unwrap(
        this.api.POST("/v1/me/reflections", {
          params: { header: { "Idempotency-Key": randomUUID() } },
          body,
        }),
      ),
  };

  events(options?: EventsOptions): AsyncGenerator<AgentLandEvent> {
    return events(this, options);
  }

  /**
   * The single transport. One Idempotency-Key per logical call, reused on every retry; the body is
   * read once and the same bytes are re-sent (and re-signed) on each attempt. Retries only network
   * failures, 5xx and 429 (non-negotiable 8).
   */
  async send(request: Request): Promise<Response> {
    const { method } = request;
    const mutating = method !== "GET" && method !== "HEAD";
    const headers = new Headers(request.headers);
    headers.set("authorization", `Bearer ${this.#apiKey}`);
    if (mutating && !headers.has("idempotency-key")) headers.set("idempotency-key", randomUUID());
    const body = mutating ? new Uint8Array(await request.arrayBuffer()) : undefined;
    const url = new URL(request.url);
    for (let attempt = 0; ; attempt += 1) {
      if (this.#signingKey && mutating) {
        const timestamp = await this.#serverNow();
        const signature = signEd25519(
          requestSigningMessage({
            method,
            requestTarget: url.pathname + url.search,
            timestamp,
            rawBody: body!,
          }),
          this.#signingKey.privatePkcs8,
        );
        headers.set("x-al-timestamp", timestamp);
        // signEd25519 returns base64url; the server's decodeSignature accepts only padded standard
        // base64 (/^[A-Za-z0-9+/]{86}==$/, P-18).
        headers.set("x-al-signature", Buffer.from(signature, "base64url").toString("base64"));
      }
      let response: Response;
      try {
        response = await this.#fetch(
          new Request(url, { method, headers, body, signal: request.signal }),
        );
      } catch (error) {
        if (attempt >= this.maxRetries || request.signal.aborted) throw error;
        await this.sleep(backoff(attempt));
        continue;
      }
      this.#record(response);
      if (attempt >= this.maxRetries || (response.status !== 429 && response.status < 500))
        return response;
      await response.body?.cancel();
      await this.sleep(Math.max(retryAfterMs(response), backoff(attempt)));
    }
  }

  #record(response: Response): void {
    const serverTime = response.headers.get("x-server-time");
    if (serverTime === null || Number.isNaN(Date.parse(serverTime))) return;
    this.#serverTime = serverTime;
    this.#serverTimeAt = this.#monotonicNow();
  }

  /**
   * Non-negotiable 1: the SDK has no clock of its own. Now = last X-Server-Time + monotonic elapsed;
   * before any response it asks the server (GET /v1/me) first.
   */
  async #serverNow(): Promise<string> {
    if (this.#serverTime === null) {
      const response = await this.send(new Request(`${this.baseUrl}/v1/me`));
      if (!response.ok) throw await AgentLandError.from(response);
      await response.body?.cancel();
      if (this.#serverTime === null) throw new Error("The API sent no X-Server-Time");
    }
    return new Date(
      Date.parse(this.#serverTime) + (this.#monotonicNow() - this.#serverTimeAt),
    ).toISOString();
  }

  async #unwrap<T>(
    pending: Promise<{ data?: T; error?: unknown; response: Response }>,
  ): Promise<T> {
    const { data, error, response } = await pending;
    if (!response.ok || data === undefined) throw await AgentLandError.from(response, error);
    return data;
  }
}

/** Retry-After seconds, or an HTTP-date measured against the response's own server time (never the local clock). */
function retryAfterMs(response: Response): number {
  const value = response.headers.get("retry-after");
  if (value === null) return 0;
  if (/^\d+$/.test(value.trim())) return Number(value) * 1000;
  const reference = Date.parse(
    response.headers.get("x-server-time") ?? response.headers.get("date") ?? "",
  );
  const until = Date.parse(value) - reference;
  return Number.isFinite(until) && until > 0 ? until : 0;
}
