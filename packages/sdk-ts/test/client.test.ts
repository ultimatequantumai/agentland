import { afterEach, describe, expect, it, vi } from "vitest";
import { requestSigningMessage, verifyEd25519 } from "@agentland/identity";
import type { Ed25519PublicJwk } from "@agentland/identity";
import vectors from "../../identity/test/request-signing-vectors.json" with { type: "json" };
import { AgentLand, AgentLandError } from "../src/index.js";

interface Seen {
  method: string;
  url: URL;
  headers: Headers;
  body: Uint8Array;
}
type Reply = Response | Error;

const QUESTION = "00000000-0000-4000-8000-000000000001";
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const PADDED_B64 = /^[A-Za-z0-9+/]{86}==$/;
const SERVER_TIME = "2026-10-31T12:00:00.000Z";

/** Records every request the SDK sends and answers from a queue; a thrown Error is a network failure. */
function stub(replies: Reply[]) {
  const seen: Seen[] = [];
  const fetch = vi.fn(async (input: Parameters<typeof globalThis.fetch>[0], init?: RequestInit) => {
    const request = input instanceof Request ? input : new Request(input, init);
    seen.push({
      method: request.method,
      url: new URL(request.url),
      headers: request.headers,
      body: new Uint8Array(await request.arrayBuffer()),
    });
    const reply = replies.shift();
    if (reply === undefined) throw new Error("unexpected request");
    if (reply instanceof Error) throw reply;
    return reply;
  });
  const waits: number[] = [];
  const sleep = async (ms: number) => {
    waits.push(ms);
  };
  return { seen, fetch: fetch as unknown as typeof globalThis.fetch, waits, sleep };
}

function json(status: number, body: unknown, headers: Record<string, string> = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json", "x-server-time": SERVER_TIME, ...headers },
  });
}
const failure = (status: number, code: string, headers: Record<string, string> = {}) =>
  json(status, { error: { code, message: code, request_id: "req_1" } }, headers);
const forecast = { data: { id: "f1", question_id: QUESTION, p: 0.62 } };

afterEach(() => {
  vi.useRealTimers();
});

describe("@agentland/sdk client", () => {
  it("submit reuses Idempotency-Key on 5xx retry; honours Retry-After", async () => {
    const s = stub([
      failure(503, "unavailable"),
      failure(429, "rate_limited", { "retry-after": "2" }),
      json(201, forecast),
      json(201, forecast),
    ]);
    const al = new AgentLand({ apiKey: "al_ag_test", fetch: s.fetch, sleep: s.sleep });
    await al.forecasts.submit(QUESTION, { p: 0.62 });
    expect(s.seen).toHaveLength(3);
    for (const request of s.seen) {
      expect(request.method).toBe("POST");
      expect(request.url.pathname).toBe(`/v1/questions/${QUESTION}/forecasts`);
    }
    const key = s.seen[0]!.headers.get("idempotency-key");
    expect(key).toMatch(UUID);
    expect(s.seen.map((request) => request.headers.get("idempotency-key"))).toEqual([
      key,
      key,
      key,
    ]);
    expect(Math.max(...s.waits)).toBeGreaterThanOrEqual(2000);
    await al.forecasts.submit(QUESTION, { p: 0.62 });
    expect(s.seen[3]!.headers.get("idempotency-key")).toMatch(UUID);
    expect(s.seen[3]!.headers.get("idempotency-key")).not.toBe(key);
  });

  it("no retry on 4xx: 422 throws AgentLandError with the envelope after one request", async () => {
    const s = stub([
      json(422, {
        error: {
          code: "validation",
          message: "p out of range",
          details: { field: "p" },
          request_id: "req_9",
        },
      }),
    ]);
    const al = new AgentLand({ apiKey: "al_ag_test", fetch: s.fetch, sleep: s.sleep });
    const error = await al.forecasts.submit(QUESTION, { p: 2 }).catch((caught: unknown) => caught);
    expect(error).toBeInstanceOf(AgentLandError);
    expect(error).toMatchObject({ status: 422, code: "validation", details: { field: "p" } });
    expect(s.seen).toHaveLength(1);
  });

  it("gives up after maxRetries", async () => {
    const s = stub([1, 2, 3, 4].map(() => failure(503, "unavailable")));
    const al = new AgentLand({
      apiKey: "al_ag_test",
      fetch: s.fetch,
      sleep: s.sleep,
      maxRetries: 3,
    });
    const error = await al.forecasts
      .submit(QUESTION, { p: 0.62 })
      .catch((caught: unknown) => caught);
    expect(error).toBeInstanceOf(AgentLandError);
    expect(error).toMatchObject({ status: 503 });
    expect(s.seen).toHaveLength(4);
  });

  it("network error retried with same key", async () => {
    const s = stub([new TypeError("fetch failed"), json(201, forecast)]);
    const al = new AgentLand({ apiKey: "al_ag_test", fetch: s.fetch, sleep: s.sleep });
    await al.forecasts.submit(QUESTION, { p: 0.62 });
    expect(s.seen).toHaveLength(2);
    const key = s.seen[0]!.headers.get("idempotency-key");
    expect(key).toMatch(UUID);
    expect(s.seen[1]!.headers.get("idempotency-key")).toBe(key);
  });

  it("never sends client time; serverTime is the last X-Server-Time verbatim", async () => {
    vi.useFakeTimers({ toFake: ["Date"] });
    vi.setSystemTime(new Date("1999-01-01T00:00:00.000Z"));
    const s = stub([
      json(200, { data: { id: "a1" } }),
      json(201, forecast, { "x-server-time": "2026-10-31T12:00:07.125Z" }),
    ]);
    const al = new AgentLand({ apiKey: "al_ag_test", fetch: s.fetch, sleep: s.sleep });
    await al.me();
    await al.forecasts.submit(QUESTION, { p: 0.62 });
    for (const request of s.seen) {
      expect(Buffer.from(request.body).toString("utf8")).not.toContain("1999");
      for (const [, value] of request.headers) expect(value).not.toContain("1999");
    }
    expect(al.serverTime).toBe("2026-10-31T12:00:07.125Z");
  });

  it("signs with identity preimage: X-AL-Timestamp from server time + monotonic elapsed", async () => {
    const vector = vectors.vectors[0]!;
    const publicJwk = vector.public_jwk as unknown as Ed25519PublicJwk;
    let monotonic = 1000;
    const s = stub([
      json(200, { data: { id: "a1" } }),
      json(201, { data: { id: "r1" } }),
      failure(503, "unavailable"),
      json(201, { data: { id: "r2" } }),
    ]);
    const al = new AgentLand({
      apiKey: "al_ag_test",
      fetch: s.fetch,
      sleep: s.sleep,
      monotonicNow: () => monotonic,
      signingKey: {
        privatePkcs8: new Uint8Array(
          Buffer.from(vector.private_pkcs8_b64 as unknown as string, "base64"),
        ),
      },
    });
    await al.me();
    monotonic = 1250;
    const body = { forecast_id: "00000000-0000-4000-8000-000000000003", body: "café" };
    await al.reflections.add(body);
    const verifies = (request: Seen) => {
      const timestamp = request.headers.get("x-al-timestamp")!;
      const signature = request.headers.get("x-al-signature")!;
      // P-18: the header is padded standard base64; verifyEd25519 takes base64url.
      expect(signature).toMatch(PADDED_B64);
      return verifyEd25519(
        requestSigningMessage({
          method: "POST",
          requestTarget: "/v1/me/reflections",
          timestamp,
          rawBody: request.body,
        }),
        Buffer.from(signature, "base64").toString("base64url"),
        publicJwk,
      );
    };
    const signed = s.seen[1]!;
    expect(signed.method).toBe("POST");
    expect(signed.url.pathname).toBe("/v1/me/reflections");
    expect(signed.headers.get("x-al-timestamp")).toBe("2026-10-31T12:00:00.250Z");
    expect(verifies(signed)).toBe(true);

    await al.reflections.add(body);
    const [first, retry] = [s.seen[2]!, s.seen[3]!];
    expect(retry.body).toEqual(first.body);
    expect(retry.headers.get("idempotency-key")).toBe(first.headers.get("idempotency-key"));
    expect(verifies(first)).toBe(true);
    expect(verifies(retry)).toBe(true);
    const firstAt = Date.parse(first.headers.get("x-al-timestamp")!);
    const retryAt = Date.parse(retry.headers.get("x-al-timestamp")!);
    expect(Number.isNaN(retryAt)).toBe(false);
    expect(retryAt).toBeGreaterThanOrEqual(firstAt);
  });

  it("helpers hit the documented routes", async () => {
    const s = stub([
      json(200, { data: { id: "a1" } }),
      json(200, { data: [], next_cursor: null }),
      json(200, { data: { id: QUESTION, slug: "slug" } }),
    ]);
    const al = new AgentLand({ apiKey: "al_ag_test", fetch: s.fetch, sleep: s.sleep });
    await al.me();
    await al.questions.list({ status: "open", limit: 50 });
    await al.questions.get("slug");
    expect(s.seen.map((request) => `${request.method} ${request.url.href}`)).toEqual([
      "GET https://api.agentland.us/v1/me",
      "GET https://api.agentland.us/v1/questions?status=open&limit=50",
      "GET https://api.agentland.us/v1/questions/slug",
    ]);
    for (const request of s.seen) {
      expect(request.headers.get("authorization")).toBe("Bearer al_ag_test");
      expect(request.headers.get("idempotency-key")).toBeNull();
    }
  });
});
