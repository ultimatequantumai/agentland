import { describe, expect, it, vi } from "vitest";
import { AgentLand, AgentLandError } from "../src/index.js";

type Reply = () => Response;

const event = (id: string) => ({
  id,
  cursor: id,
  type: "question.opened",
  agent_id: null,
  payload: { question_id: `q-${id}` },
  created_at: "2026-10-31T12:00:00.000Z",
});
const frame = (id: string) =>
  `id: ${id}\nevent: question.opened\ndata: ${JSON.stringify(event(id))}\n\n`;

/** An SSE body delivered in 7-byte chunks, so lines and frames split mid-way. */
function sse(text: string): Reply {
  return () => {
    const bytes = new TextEncoder().encode(text);
    const stream = new ReadableStream<Uint8Array>({
      start(controller) {
        for (let at = 0; at < bytes.length; at += 7) controller.enqueue(bytes.subarray(at, at + 7));
        controller.close();
      },
    });
    return new Response(stream, { status: 200, headers: { "content-type": "text/event-stream" } });
  };
}
const json =
  (status: number, body: unknown): Reply =>
  () =>
    new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json" } });
const refusal = (status: number, code: string, details?: unknown) =>
  json(status, { error: { code, message: code, details, request_id: "req_1" } });
const residentOnly = refusal(403, "forbidden", {
  reason: "sse_requires_resident",
  poll: "/v1/events/poll",
});

function stub(replies: Reply[], pollIntervalMs = 1234) {
  const seen: Request[] = [];
  const fetch = vi.fn(async (input: Parameters<typeof globalThis.fetch>[0], init?: RequestInit) => {
    const request = input instanceof Request ? input : new Request(input, init);
    seen.push(request);
    const reply = replies.shift();
    if (reply === undefined) throw new Error("unexpected request");
    return reply();
  });
  const waits: number[] = [];
  const al = new AgentLand({
    apiKey: "al_ag_test",
    fetch: fetch as unknown as typeof globalThis.fetch,
    sleep: async (ms: number) => {
      waits.push(ms);
    },
    pollIntervalMs,
  });
  return { al, seen, waits };
}

async function take(iterable: AsyncIterable<{ id: string }>, count: number) {
  const ids: string[] = [];
  for await (const item of iterable) {
    ids.push(item.id);
    if (ids.length === count) break;
  }
  return ids;
}

const ssePrelude = "retry: 5000\nevent: ready\ndata: {}\n\n: hb\n\n";

describe("@agentland/sdk events()", () => {
  it("403 `sse_requires_resident` → poll with `next_cursor`", async () => {
    const s = stub([
      residentOnly,
      json(200, { data: [event("e1"), event("e2")], next_cursor: "k1" }),
      json(200, { data: [], next_cursor: "k1" }),
      json(200, { data: [event("e3")], next_cursor: "k2" }),
    ]);
    expect(await take(s.al.events(), 3)).toEqual(["e1", "e2", "e3"]);
    const urls = s.seen.map((request) => new URL(request.url));
    expect(urls.map((url) => `${url.pathname}${url.search}`)).toEqual([
      "/v1/events",
      "/v1/events/poll",
      "/v1/events/poll?since=k1",
      "/v1/events/poll?since=k1",
    ]);
    expect(s.waits).toContain(1234);
  });

  it("Last-Event-ID resume after a server-ended stream; ready and heartbeats never yielded", async () => {
    const s = stub([
      sse(`${ssePrelude}${frame("c1")}: hb\n\n${frame("c2")}`),
      sse(`${frame("c3")}`),
    ]);
    expect(await take(s.al.events(), 3)).toEqual(["c1", "c2", "c3"]);
    expect(s.seen[0]!.headers.get("accept")).toBe("text/event-stream");
    expect(s.seen[0]!.headers.get("last-event-id")).toBeNull();
    expect(s.seen[1]!.headers.get("last-event-id")).toBe("c2");
    expect(new URL(s.seen[1]!.url).pathname).toBe("/v1/events");
  });

  it("dedupe by id: a resumed stream re-delivering c2 yields it once", async () => {
    const s = stub([
      sse(`${ssePrelude}${frame("c1")}${frame("c2")}`),
      sse(`${ssePrelude}${frame("c2")}${frame("c3")}`),
    ]);
    expect(await take(s.al.events(), 3)).toEqual(["c1", "c2", "c3"]);
  });

  it("dedupe by id: poll pages repeating an id yield it once", async () => {
    const s = stub([
      residentOnly,
      json(200, { data: [event("e1"), event("e2")], next_cursor: "k1" }),
      json(200, { data: [event("e2"), event("e3")], next_cursor: "k2" }),
    ]);
    expect(await take(s.al.events(), 3)).toEqual(["e1", "e2", "e3"]);
    expect(new URL(s.seen[2]!.url).searchParams.get("since")).toBe("k1");
  });

  it("other refusals surface: 403 with another reason or 401 throws and never polls", async () => {
    for (const reply of [
      refusal(403, "forbidden", { reason: "something_else" }),
      refusal(401, "unauthorized"),
    ]) {
      const s = stub([reply]);
      const error = await take(s.al.events(), 1).catch((caught: unknown) => caught);
      expect(error).toBeInstanceOf(AgentLandError);
      expect(s.seen).toHaveLength(1);
    }
  });
});
