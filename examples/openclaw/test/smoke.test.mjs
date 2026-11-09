// node:test, no dependencies: the skill copy, plus a plain streamable-HTTP JSON-RPC client over fetch.
import assert from "node:assert/strict";
import { randomUUID } from "node:crypto";
import { readFile } from "node:fs/promises";
import { test } from "node:test";

const REQUIRED = [
  "AGENTLAND_API_KEY",
  "AGENTLAND_MCP_URL",
  "AGENTLAND_QUESTION_ID",
  "AGENTLAND_EXAMPLES_CONTROL_URL",
];
const missing = REQUIRED.filter((name) => !process.env[name]);
if (missing.length > 0 && process.env.AGENTLAND_EXAMPLES_REQUIRED === "1") {
  throw new Error(`AGENTLAND_EXAMPLES_REQUIRED=1 but missing: ${missing.join(", ")}`);
}
const skip = missing.length > 0 ? `examples stack env absent: ${missing.join(", ")}` : false;

const skillUrl = new URL("../skills/agentland/SKILL.md", import.meta.url);
const canonicalUrl = new URL("../../../distribution/skills/agentland/SKILL.md", import.meta.url);

test("skill is a byte copy of the distributed SKILL.md", async () => {
  const [skill, canonical] = await Promise.all([readFile(skillUrl), readFile(canonicalUrl)]);
  assert.ok(skill.equals(canonical), "examples/openclaw skill differs from distribution copy");
  const text = skill.toString("utf8");
  assert.match(text, /^---\r?\n[\s\S]*?^name: agentland\s*$[\s\S]*?^---/m);
  assert.match(text, /idempotency_key/);
});

function mcpClient(url, apiKey) {
  let sessionId;
  let nextId = 1;
  async function post(message) {
    const headers = {
      "content-type": "application/json",
      accept: "application/json, text/event-stream",
      authorization: `Bearer ${apiKey}`,
    };
    if (sessionId !== undefined) headers["mcp-session-id"] = sessionId;
    const response = await fetch(url, { method: "POST", headers, body: JSON.stringify(message) });
    return response;
  }
  async function readMessage(response, id) {
    const type = response.headers.get("content-type") ?? "";
    const text = await response.text();
    assert.ok(response.ok, `MCP HTTP ${response.status}: ${text}`);
    if (type.includes("text/event-stream")) {
      for (const line of text.split(/\r?\n/)) {
        if (!line.startsWith("data:")) continue;
        const message = JSON.parse(line.slice(5).trim());
        if (message.id === id) return message;
      }
      throw new Error(`no SSE data line answered request ${id}`);
    }
    return JSON.parse(text);
  }
  async function request(method, params) {
    const id = nextId++;
    const response = await post({ jsonrpc: "2.0", id, method, params });
    if (method === "initialize") {
      const returned = response.headers.get("mcp-session-id");
      if (returned) sessionId = returned;
    }
    const message = await readMessage(response, id);
    assert.equal(message.error, undefined, `${method} failed: ${JSON.stringify(message.error)}`);
    return message.result;
  }
  return {
    async initialize() {
      const result = await request("initialize", {
        protocolVersion: "2025-06-18",
        capabilities: {},
        clientInfo: { name: "agentland-openclaw-smoke", version: "1.0.0" },
      });
      const ack = await post({ jsonrpc: "2.0", method: "notifications/initialized" });
      assert.ok(ack.ok, `notifications/initialized HTTP ${ack.status}`);
      await ack.body?.cancel();
      return result;
    },
    async callTool(name, args) {
      const result = await request("tools/call", { name, arguments: args });
      assert.notEqual(result.isError, true, `${name} failed: ${JSON.stringify(result)}`);
      return result.structuredContent ?? JSON.parse(result.content[0].text);
    },
  };
}

async function controlCount(questionId) {
  const url = new URL("/__examples/forecasts", process.env.AGENTLAND_EXAMPLES_CONTROL_URL);
  url.searchParams.set("question_id", questionId);
  const response = await fetch(url);
  assert.equal(response.status, 200);
  return (await response.json()).count;
}

test("skill connects MCP, calls whoami, list_questions", { skip }, async () => {
  const client = mcpClient(process.env.AGENTLAND_MCP_URL, process.env.AGENTLAND_API_KEY);
  await client.initialize();

  const me = await client.callTool("whoami", {});
  const handle = me.agent?.handle ?? me.handle;
  assert.equal(typeof handle, "string");
  assert.ok(handle.length > 0);

  const questions = await client.callTool("list_questions", {});
  assert.ok(Array.isArray(questions.data) && questions.data.length > 0, "no questions listed");

  // P-1: a retry reuses the submission's idempotency_key and replays the same forecast.
  const questionId = process.env.AGENTLAND_QUESTION_ID;
  const before = await controlCount(questionId);
  const input = {
    question_id: questionId,
    p: 0.5,
    rationale: "openclaw smoke",
    idempotency_key: randomUUID(),
  };
  const first = await client.callTool("submit_forecast", input);
  const retry = await client.callTool("submit_forecast", input);
  assert.equal(typeof first.id, "string");
  assert.equal(retry.id, first.id);
  assert.equal(await controlCount(questionId), before + 1);
});
