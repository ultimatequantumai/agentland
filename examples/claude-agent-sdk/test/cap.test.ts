// Pure: no stack, no model. The @house per-run cap (11-31, D-42) enforced in code.
import { describe, expect, it, vi } from "vitest";
import { buildHooks, createCapHook, idempotencyHook, parseHouseCap } from "../src/bot.js";

const SUBMIT = "mcp__agentland__submit_forecast";

function submitInput(questionId: string) {
  return {
    hook_event_name: "PreToolUse",
    session_id: "cap",
    transcript_path: "",
    cwd: process.cwd(),
    tool_name: SUBMIT,
    tool_input: { question_id: questionId, p: 0.5, rationale: "cap", publish: "close" },
  } as unknown as Parameters<typeof idempotencyHook>[0];
}

describe("parseHouseCap", () => {
  it("unset keeps the uncapped starter; whole numbers 1 to 20 are the cap", () => {
    expect(parseHouseCap(undefined)).toBeNull();
    expect(parseHouseCap("5")).toBe(5);
    expect(parseHouseCap("1")).toBe(1);
    expect(parseHouseCap("20")).toBe(20);
  });

  it("anything else is house_cap_invalid", () => {
    for (const raw of ["0", "-1", "1.5", "abc", "21"]) {
      let error: unknown;
      try {
        parseHouseCap(raw);
      } catch (e) {
        error = e;
      }
      expect(Object.getPrototypeOf(error)).toBe(Error.prototype);
      expect((error as Error).message).toBe("house_cap_invalid");
    }
  });
});

describe("createCapHook", () => {
  it("allows the first N submissions, then denies, reports and records the next", async () => {
    const onDeny = vi.fn();
    const cap = createCapHook(2, onDeny);
    const options = { signal: new AbortController().signal };
    expect(cap.reached()).toBe(false);
    expect(await cap.hook(submitInput("q1"), "toolu_1", options)).toEqual({});
    expect(cap.reached()).toBe(false);
    expect(await cap.hook(submitInput("q2"), "toolu_2", options)).toEqual({});
    expect(cap.reached()).toBe(true);
    expect(onDeny).not.toHaveBeenCalled();
    expect(cap.denied()).toEqual([]);

    expect(await cap.hook(submitInput("q3"), "toolu_3", options)).toEqual({
      hookSpecificOutput: {
        hookEventName: "PreToolUse",
        permissionDecision: "deny",
        permissionDecisionReason: expect.stringContaining("HOUSE_MAX_QUESTIONS_PER_RUN"),
      },
    });
    expect(onDeny).toHaveBeenCalledTimes(1);
    expect(cap.denied()).toEqual(["toolu_3"]);
  });
});

describe("buildHooks", () => {
  it("uncapped: the submit matcher carries only idempotencyHook", () => {
    expect(buildHooks()).toEqual({ PreToolUse: [{ matcher: SUBMIT, hooks: [idempotencyHook] }] });
  });

  it("capped: the same matcher carries the cap hook and idempotencyHook, in any order", () => {
    const cap = createCapHook(1);
    const hooks = buildHooks(cap.hook);
    expect(Object.keys(hooks)).toEqual(["PreToolUse"]);
    expect(hooks.PreToolUse).toHaveLength(1);
    expect(hooks.PreToolUse?.[0]?.matcher).toBe(SUBMIT);
    expect(hooks.PreToolUse?.[0]?.hooks).toHaveLength(2);
    expect(new Set(hooks.PreToolUse?.[0]?.hooks)).toEqual(new Set([cap.hook, idempotencyHook]));
  });
});
