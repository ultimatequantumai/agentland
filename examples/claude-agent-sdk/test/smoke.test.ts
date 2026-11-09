import { describe, expect, it } from "vitest";
// Static imports: a missing starter fails even when the stack env is absent.
import { idempotencyHook, run } from "../src/bot.js";
import { startStub } from "./stub-server.js";

const REQUIRED = [
  "AGENTLAND_API_KEY",
  "AGENTLAND_MCP_URL",
  "AGENTLAND_QUESTION_ID",
  "AGENTLAND_EXAMPLES_CONTROL_URL",
] as const;
const missing = REQUIRED.filter((name) => !process.env[name]);
if (missing.length > 0 && process.env.AGENTLAND_EXAMPLES_REQUIRED === "1") {
  throw new Error(`AGENTLAND_EXAMPLES_REQUIRED=1 but missing: ${missing.join(", ")}`);
}

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

type Control = {
  count: number;
  latest: {
    question_id: string;
    rationale_publish_at: string;
    idempotency_key_present: boolean;
  } | null;
};

async function controlForecasts(): Promise<Control> {
  const response = await fetch(
    `${process.env.AGENTLAND_EXAMPLES_CONTROL_URL}/__examples/forecasts`,
  );
  expect(response.status).toBe(200);
  return (await response.json()) as Control;
}

function hookInput(toolName: string, toolInput: Record<string, unknown>) {
  return {
    hook_event_name: "PreToolUse",
    session_id: "smoke",
    transcript_path: "",
    cwd: process.cwd(),
    tool_name: toolName,
    tool_input: toolInput,
  } as unknown as Parameters<typeof idempotencyHook>[0];
}

async function callHook(toolName: string, toolInput: Record<string, unknown>) {
  return (await idempotencyHook(hookInput(toolName, toolInput), "toolu_smoke", {
    signal: new AbortController().signal,
  })) as { hookSpecificOutput?: { updatedInput?: Record<string, unknown> } };
}

function parse(body: unknown): unknown {
  if (typeof body !== "string") return body;
  try {
    return JSON.parse(body);
  } catch {
    return body;
  }
}

/** Every tool_use input the stub wrote, as seen in the conversation history the SDK sent back. */
function stubToolUseInputs(requests: readonly { body?: unknown }[]): unknown[] {
  const inputs: unknown[] = [];
  for (const request of requests) {
    const body = parse(request.body) as { messages?: { role: string; content: unknown }[] };
    for (const message of body?.messages ?? []) {
      if (message.role !== "assistant" || !Array.isArray(message.content)) continue;
      for (const block of message.content as { type?: string; input?: unknown }[]) {
        if (block.type === "tool_use") inputs.push(block.input);
      }
    }
  }
  return inputs;
}

describe("idempotencyHook", () => {
  it("gives every submit_forecast a fresh UUID and leaves other tools untouched", async () => {
    const input = { question_id: "q", p: 0.5, idempotency_key: "model-said-this" };
    const first = await callHook("mcp__agentland__submit_forecast", input);
    const second = await callHook("mcp__agentland__submit_forecast", input);
    const firstKey = first.hookSpecificOutput?.updatedInput?.idempotency_key;
    const secondKey = second.hookSpecificOutput?.updatedInput?.idempotency_key;
    expect(firstKey).toMatch(UUID);
    expect(secondKey).toMatch(UUID);
    expect(firstKey).not.toBe(secondKey);
    expect(first.hookSpecificOutput?.updatedInput).toMatchObject({ question_id: "q", p: 0.5 });
    expect(input.idempotency_key).toBe("model-said-this");

    const other = await callHook("mcp__agentland__list_questions", { limit: 5 });
    expect(other.hookSpecificOutput?.updatedInput).toBeUndefined();
  });
});

describe.skipIf(missing.length > 0)("claude agent sdk starter", () => {
  it("stub model submits one forecast with publish: close", async () => {
    process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC = "1";
    const stub = await startStub();
    const previousBase = process.env.ANTHROPIC_BASE_URL;
    const previousKey = process.env.ANTHROPIC_API_KEY;
    process.env.ANTHROPIC_BASE_URL = stub.url;
    process.env.ANTHROPIC_API_KEY = "stub-not-a-key";
    try {
      const before = await controlForecasts();
      const trace = (await run()) as { tool: string; input: Record<string, unknown> }[];

      expect(stub.requests.some((r) => r.method === "POST" && r.path === "/v1/messages")).toBe(
        true,
      );
      expect(stub.requests.filter((r) => r.path !== "/v1/messages")).toEqual([]);

      const submits = trace.filter((step) => step.tool === "mcp__agentland__submit_forecast");
      expect(submits).toHaveLength(1);
      const key = submits[0]!.input.idempotency_key;
      expect(key).toMatch(UUID);
      expect(submits[0]!.input.publish).toBe("close");
      // The key came from idempotencyHook: no tool_use the stub wrote ever carried it.
      expect(JSON.stringify(stubToolUseInputs(stub.requests))).not.toContain(String(key));

      const after = await controlForecasts();
      const questionIds = [process.env.AGENTLAND_QUESTION_ID, process.env.AGENTLAND_QUESTION_ID_2];
      expect(after.count).toBe(before.count + 1);
      expect(questionIds).toContain(after.latest?.question_id);
      expect(after.latest?.idempotency_key_present).toBe(true);
      expect(after.latest?.rationale_publish_at).toBe("close");
    } finally {
      process.env.ANTHROPIC_BASE_URL = previousBase;
      process.env.ANTHROPIC_API_KEY = previousKey;
      if (previousBase === undefined) delete process.env.ANTHROPIC_BASE_URL;
      if (previousKey === undefined) delete process.env.ANTHROPIC_API_KEY;
      await stub.close();
    }
  }, 120_000);

  it("capped run submits once and denies the second", async () => {
    process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC = "1";
    const stub = await startStub({ submits: 2 });
    const previousBase = process.env.ANTHROPIC_BASE_URL;
    const previousKey = process.env.ANTHROPIC_API_KEY;
    const previousCap = process.env.HOUSE_MAX_QUESTIONS_PER_RUN;
    const previousExit = process.exitCode;
    process.env.ANTHROPIC_BASE_URL = stub.url;
    process.env.ANTHROPIC_API_KEY = "stub-not-a-key";
    process.env.HOUSE_MAX_QUESTIONS_PER_RUN = "1";
    process.exitCode = undefined;
    try {
      const before = await controlForecasts();
      // A cap stop is a normal end of the run: it resolves and exits 0.
      const trace = (await run()) as {
        tool: string;
        input: Record<string, unknown>;
        denied?: boolean;
      }[];
      expect([undefined, 0]).toContain(process.exitCode);

      const after = await controlForecasts();
      expect(after.count).toBe(before.count + 1);
      expect(after.latest?.rationale_publish_at).toBe("close");
      const questionIds = [process.env.AGENTLAND_QUESTION_ID, process.env.AGENTLAND_QUESTION_ID_2];
      expect(questionIds).toContain(after.latest?.question_id);
      const other = questionIds.find((id) => id !== after.latest?.question_id);
      expect(other).toBeDefined();

      const submits = trace.filter((step) => step.tool === "mcp__agentland__submit_forecast");
      const denied = submits.filter((step) => step.denied === true);
      expect(denied).toHaveLength(1);
      expect(denied[0]!.input.question_id).toBe(other);
      const allowed = submits.filter((step) => step.denied !== true);
      expect(allowed).toHaveLength(1);
      expect(allowed[0]!.input.question_id).toBe(after.latest?.question_id);
    } finally {
      process.env.ANTHROPIC_BASE_URL = previousBase;
      process.env.ANTHROPIC_API_KEY = previousKey;
      process.env.HOUSE_MAX_QUESTIONS_PER_RUN = previousCap;
      if (previousBase === undefined) delete process.env.ANTHROPIC_BASE_URL;
      if (previousKey === undefined) delete process.env.ANTHROPIC_API_KEY;
      if (previousCap === undefined) delete process.env.HOUSE_MAX_QUESTIONS_PER_RUN;
      process.exitCode = previousExit;
      await stub.close();
    }
  }, 120_000);
});
