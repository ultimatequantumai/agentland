import { describe, expect, it } from "vitest";
import { aggregateLift, liftContributions } from "../src/index.js";
import type { CitationRow } from "../src/index.js";

const monday = Date.parse("2025-12-29T00:00:00Z");
const row = (questionId: string, offset = 0, finalEdge = 0.2): CitationRow => ({
  questionId,
  rationaleId: `r-${questionId}`,
  rationaleQuestionId: "earlier",
  citingAgentId: "B",
  citedAgentId: "A",
  citingOperatorId: "op-B",
  citedOperatorId: "op-A",
  submittedAt: new Date(monday + offset),
  publicAt: new Date(monday - 1),
  finalEdge,
});
const caps = { pairCapWeek: 3 };

describe("Lift", () => {
  it("admits first three eligible distinct questions before considering outcomes", () => {
    const inputs = [row("q1", 1, -0.1), row("q2", 2, 0), row("q3", 3, 0.4), row("q4", 4, 0.8)];
    const result = liftContributions(inputs.reverse(), caps);
    expect(result.map((r) => [r.questionId, r.week, r.contribution])).toEqual([
      ["q1", "2025-12-29", 0],
      ["q2", "2025-12-29", 0],
      ["q3", "2025-12-29", 0.2],
    ]);
    expect(aggregateLift(result)).toEqual({ lift: 0.2, nCitations: 3, shrunkLift: 0.2 / 13 });
    expect(aggregateLift([])).toEqual({ lift: 0, nCitations: 0, shrunkLift: 0 });
    expect(liftContributions(inputs, { pairCapWeek: 0 })).toEqual([]);
  });
  it("excludes self, same operator, unpublished and same-question rationales", () => {
    const original = row("q");
    const excluded = [
      { ...original, citedAgentId: "B" },
      { ...original, citedOperatorId: "op-B" },
      { ...original, publicAt: new Date(monday + 1) },
      { ...original, rationaleQuestionId: "q" },
    ];
    for (const value of excluded) expect(liftContributions([value], caps)).toEqual([]);
    expect(liftContributions([{ ...original, publicAt: original.submittedAt }], caps)).toHaveLength(
      1,
    );
  });
  it("deduplicates author citations and rejects conflicting final facts", () => {
    const original = row("q");
    expect(
      liftContributions([original, { ...original, rationaleId: "second" }], caps),
    ).toHaveLength(1);
    for (const change of [
      { finalEdge: 0.3 },
      { submittedAt: new Date(monday + 1) },
      { citingOperatorId: "different" },
      { citedOperatorId: "different" },
    ]) {
      expect(() => liftContributions([original, { ...original, ...change }], caps)).toThrow();
    }
    // An ineligible duplicate does not hide the eligible public rationale.
    expect(
      liftContributions([{ ...original, publicAt: new Date(monday + 1) }, original], caps),
    ).toHaveLength(1);
  });
  it("has independent ordered-pair/week caps and ISO Monday UTC rollover", () => {
    const week = 7 * 86_400_000;
    const inputs = [
      row("a", 0),
      row("b", 1),
      row("c", 2),
      row("d", 3),
      row("sunday", week - 1),
      row("next", week),
      {
        ...row("reverse", 4),
        citingAgentId: "A",
        citedAgentId: "B",
        citingOperatorId: "op-A",
        citedOperatorId: "op-B",
      },
      { ...row("other", 5), citingAgentId: "C", citingOperatorId: "op-C" },
    ];
    const result = liftContributions(inputs, caps);
    expect(result.map((r) => r.questionId)).toEqual(["a", "b", "c", "reverse", "other", "next"]);
    expect(result.at(-1)?.week).toBe("2026-01-05");
    expect(liftContributions([row("sun", -1)], caps)[0]?.week).toBe("2025-12-22");
    const tied = [row("z"), row("a"), row("b"), row("c")];
    expect(liftContributions(tied, caps).map((r) => r.questionId)).toEqual(["a", "b", "c"]);
    expect(liftContributions([...tied].reverse(), caps)).toEqual(liftContributions(tied, caps));
  });
  it("rejects invalid local facts, cap and aggregation corruption", () => {
    for (const change of [
      { rationaleId: "" },
      { rationaleQuestionId: "" },
      { questionId: "" },
      { citingAgentId: "" },
      { citedAgentId: "" },
      { citingOperatorId: "" },
      { citedOperatorId: "" },
      { submittedAt: new Date(NaN) },
      { publicAt: new Date(NaN) },
      { finalEdge: Infinity },
    ])
      expect(() => liftContributions([{ ...row("q"), ...change }], caps)).toThrow();
    for (const pairCapWeek of [-1, 0.5, Infinity])
      expect(() => liftContributions([], { pairCapWeek })).toThrow();
    const result = liftContributions([row("q")], caps)[0]!;
    expect(() => aggregateLift([{ ...result, contribution: -1 }])).toThrow();
    expect(() => aggregateLift([result, result])).toThrow();
    expect(() => aggregateLift([{ ...result, contribution: Infinity }])).toThrow();
    expect(() => aggregateLift([{ ...result, week: "bad" }])).toThrow();
  });
});
