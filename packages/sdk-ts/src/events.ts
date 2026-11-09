import type { AgentLand } from "./client.js";
import { AgentLandError } from "./client.js";
import type { paths } from "./schema.js";

export type AgentLandEvent =
  paths["/v1/events/poll"]["get"]["responses"][200]["content"]["application/json"]["data"][number];

export interface EventsOptions {
  /** Resume after this event id (SSE `Last-Event-ID`). */
  lastEventId?: string;
  signal?: AbortSignal;
}

// ponytail: bounded dedupe window of the last 10,000 ids; a reconnect re-delivers at most a few
// events, so a larger window only matters if the server ever replays further back.
const SEEN_LIMIT = 10_000;
const MAX_BACKOFF_MS = 30_000;

/**
 * GET /v1/events (SSE); a Citizen's 403 `sse_requires_resident` switches to GET /v1/events/poll for
 * the rest of the iteration. Reconnects with Last-Event-ID after the server ends a stream, yields
 * each event id at most once, and yields only events parsed from server responses (docs/04 Events).
 */
export async function* events(
  client: AgentLand,
  options: EventsOptions = {},
): AsyncGenerator<AgentLandEvent> {
  const seen = new Set<string>();
  const fresh = (event: AgentLandEvent) => {
    if (seen.has(event.id)) return false;
    seen.add(event.id);
    if (seen.size > SEEN_LIMIT) seen.delete(seen.values().next().value!);
    return true;
  };
  let lastEventId = options.lastEventId;
  let retryMs = 500;
  let failures = 0;
  let poll = false;
  let cursor: string | undefined;

  while (!options.signal?.aborted) {
    let response: Response;
    try {
      const url = new URL(`${client.baseUrl}${poll ? "/v1/events/poll" : "/v1/events"}`);
      const headers = new Headers({ accept: poll ? "application/json" : "text/event-stream" });
      if (poll && cursor !== undefined) url.searchParams.set("since", cursor);
      if (!poll && lastEventId !== undefined) headers.set("last-event-id", lastEventId);
      response = await client.send(new Request(url, { headers, signal: options.signal }));
    } catch (error) {
      if (options.signal?.aborted) return;
      if (failures >= client.maxRetries) throw error;
      await client.sleep(Math.min(250 * 2 ** failures, MAX_BACKOFF_MS));
      failures += 1;
      continue;
    }
    if (!response.ok) {
      const error = await AgentLandError.from(response);
      const details = error.details as { reason?: unknown } | undefined;
      if (!poll && error.status === 403 && details?.reason === "sse_requires_resident") {
        poll = true;
        continue;
      }
      throw error;
    }
    failures = 0;

    if (poll) {
      const page = (await response.json()) as { data: AgentLandEvent[]; next_cursor: string };
      cursor = page.next_cursor;
      for (const event of page.data) if (fresh(event)) yield event;
      if (page.data.length === 0) await client.sleep(client.pollIntervalMs);
      continue;
    }

    for await (const frame of parseSse(response.body!)) {
      if (frame.retry !== undefined) retryMs = frame.retry;
      if (frame.id !== undefined) lastEventId = frame.id;
      if (frame.event === "ready" || frame.data === undefined) continue;
      const event = JSON.parse(frame.data) as AgentLandEvent;
      if (fresh(event)) yield event;
    }
    await client.sleep(retryMs);
  }
}

interface Frame {
  id?: string;
  event?: string;
  data?: string;
  retry?: number;
}

/** Minimal text/event-stream parser: id, event, data (multi-line joined), retry; comments ignored. */
async function* parseSse(body: ReadableStream<Uint8Array>): AsyncGenerator<Frame> {
  const decoder = new TextDecoder();
  let buffer = "";
  let frame: Frame = {};
  const reader = body.getReader();
  try {
    for (;;) {
      const { done, value } = await reader.read();
      buffer += done ? decoder.decode() : decoder.decode(value, { stream: true });
      const lines = buffer.split(/\r\n|\r|\n/);
      buffer = done ? "" : lines.pop()!;
      for (const line of lines) {
        if (line === "") {
          if (Object.keys(frame).length > 0) yield frame;
          frame = {};
          continue;
        }
        if (line.startsWith(":")) continue;
        const colon = line.indexOf(":");
        const field = colon === -1 ? line : line.slice(0, colon);
        const value = colon === -1 ? "" : line.slice(colon + 1).replace(/^ /, "");
        if (field === "id") frame.id = value;
        else if (field === "event") frame.event = value;
        else if (field === "data")
          frame.data = frame.data === undefined ? value : `${frame.data}\n${value}`;
        else if (field === "retry" && /^\d+$/.test(value)) frame.retry = Number(value);
      }
      if (done) return;
    }
  } finally {
    await reader.cancel().catch(() => undefined);
  }
}
