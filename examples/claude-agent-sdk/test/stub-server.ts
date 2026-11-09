// A local Messages-API SSE stub: the only model endpoint the Claude starter's tests reach.
// Its next move comes from the request body, never from shared state.
import { once } from "node:events";
import { createServer, type IncomingMessage, type ServerResponse } from "node:http";
import type { AddressInfo } from "node:net";

export type StubRequest = { method: string; path: string; body: string };

type Block = { type?: string; id?: string; name?: string; tool_use_id?: string; content?: unknown };
type Message = { role?: string; content?: unknown };
type Body = { tools?: { name?: string }[]; messages?: Message[]; stream?: boolean; model?: string };

const blocks = (message: Message | undefined): Block[] =>
  Array.isArray(message?.content) ? (message.content as Block[]) : [];

function text(content: unknown): string {
  if (typeof content === "string") return content;
  if (Array.isArray(content))
    return content.map((block: { text?: string }) => block.text ?? "").join("");
  return "";
}

/**
 * The model's next content block, chosen from the conversation the SDK sent. With `submits: 2`
 * a second submit (second listed question) follows the first submit's tool_result.
 */
function nextBlock(body: Body, submits: number): Record<string, unknown> {
  const done = { type: "text", text: "done" };
  // Auxiliary calls (titles, summaries) carry no agentland tools.
  if (!body.tools?.some((tool) => tool.name?.startsWith("mcp__agentland__")))
    return { type: "text", text: "ok" };
  const messages = body.messages ?? [];
  const results = messages.flatMap((message) =>
    blocks(message).filter((block) => block.type === "tool_result"),
  );
  if (!results.length)
    return {
      type: "tool_use",
      id: "toolu_stub_list",
      name: "mcp__agentland__list_questions",
      input: {},
    };
  const last = results.at(-1)!;
  const called = messages
    .flatMap((message) => blocks(message))
    .find((block) => block.type === "tool_use" && block.id === last.tool_use_id);
  if (submits >= 2 && called?.id === "toolu_stub_submit") {
    const list = results.find((result) => result.tool_use_id === "toolu_stub_list")!;
    const listed = JSON.parse(text(list.content)) as { data: { id: string }[] };
    return {
      type: "tool_use",
      id: "toolu_stub_submit_2",
      name: "mcp__agentland__submit_forecast",
      input: {
        question_id: listed.data[1]!.id,
        p: 0.5,
        rationale: "starter stub",
        publish: "close",
      },
    };
  }
  if (called?.name !== "mcp__agentland__list_questions") return done;
  const listed = JSON.parse(text(last.content)) as { data: { id: string }[] };
  return {
    type: "tool_use",
    id: "toolu_stub_submit",
    name: "mcp__agentland__submit_forecast",
    // No idempotency key: the starter's PreToolUse hook adds it.
    input: { question_id: listed.data[0]!.id, p: 0.5, rationale: "starter stub", publish: "close" },
  };
}

function respond(response: ServerResponse, body: Body, submits: number) {
  const block = nextBlock(body, submits);
  const message = {
    id: `msg_stub_${Math.random().toString(36).slice(2)}`,
    type: "message",
    role: "assistant",
    model: body.model ?? "stub",
    stop_sequence: null,
    usage: { input_tokens: 1, output_tokens: 1 },
  };
  const stopReason = block.type === "tool_use" ? "tool_use" : "end_turn";
  if (!body.stream) {
    response.writeHead(200, { "content-type": "application/json" });
    response.end(JSON.stringify({ ...message, content: [block], stop_reason: stopReason }));
    return;
  }
  response.writeHead(200, { "content-type": "text/event-stream", "cache-control": "no-cache" });
  const send = (event: string, data: Record<string, unknown>) =>
    response.write(`event: ${event}\ndata: ${JSON.stringify({ type: event, ...data })}\n\n`);
  send("message_start", { message: { ...message, content: [], stop_reason: null } });
  if (block.type === "tool_use") {
    send("content_block_start", { index: 0, content_block: { ...block, input: {} } });
    send("content_block_delta", {
      index: 0,
      delta: { type: "input_json_delta", partial_json: JSON.stringify(block.input) },
    });
  } else {
    send("content_block_start", { index: 0, content_block: { type: "text", text: "" } });
    send("content_block_delta", { index: 0, delta: { type: "text_delta", text: block.text } });
  }
  send("content_block_stop", { index: 0 });
  send("message_delta", {
    delta: { stop_reason: stopReason, stop_sequence: null },
    usage: { output_tokens: 1 },
  });
  send("message_stop", {});
  response.end();
}

async function readText(request: IncomingMessage): Promise<string> {
  const chunks: Buffer[] = [];
  for await (const chunk of request) chunks.push(chunk as Buffer);
  return Buffer.concat(chunks).toString("utf8");
}

/** `submits` (default 1, 11-07's behaviour): how many submit_forecast calls the stub asks for. */
export async function startStub({ submits = 1 }: { submits?: number } = {}) {
  const requests: StubRequest[] = [];
  const server = createServer((request, response) => {
    void readText(request).then((body) => {
      const path = new URL(request.url ?? "/", "http://stub").pathname;
      requests.push({ method: request.method ?? "", path, body });
      if (request.method !== "POST" || path !== "/v1/messages") {
        response.writeHead(404, { "content-type": "application/json" });
        response.end(JSON.stringify({ type: "error", error: { type: "not_found_error" } }));
        return;
      }
      respond(response, JSON.parse(body) as Body, submits);
    });
  });
  server.listen(0, "127.0.0.1");
  await once(server, "listening");
  const { port } = server.address() as AddressInfo;
  return {
    url: `http://127.0.0.1:${port}`,
    requests,
    close: async () => {
      server.closeAllConnections();
      server.close();
      await once(server, "close");
    },
  };
}
