import { describe, expect, it } from "vitest";
import { aggregateLift, liftContributions, liftLedger, LIFT_STATUSES } from "../src/index.js";
import type { CitationRow, LiftLedgerRow, LiftStatus } from "../src/index.js";

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

describe("liftLedger (C-05)", () => {
  const week = 7 * 86_400_000;
  const one = (value: CitationRow): LiftLedgerRow => {
    const ledger = liftLedger([value], caps);
    expect(ledger).toHaveLength(1);
    return ledger[0]!;
  };
  const statuses = (ledger: readonly LiftLedgerRow[]): [string, LiftStatus, number][] =>
    ledger.map((e) => [e.row.rationaleId, e.status, e.contribution]);

  it("lists the eight statuses in their fixed order", () => {
    expect(LIFT_STATUSES).toEqual([
      "credited",
      "zero_edge",
      "pair_cap",
      "duplicate",
      "same_question",
      "self",
      "same_operator",
      "not_public",
    ]);
  });

  it("names every exclusion with precedence not_public, same_question, self, same_operator", () => {
    const original = row("q");
    const late = new Date(monday + 1);
    const cases: [CitationRow, LiftStatus][] = [
      // self wins over same_operator: one agent always shares its own operator.
      [{ ...original, citedAgentId: "B", citedOperatorId: "op-B" }, "self"],
      [{ ...original, citedOperatorId: "op-B" }, "same_operator"],
      [{ ...original, publicAt: late }, "not_public"],
      [{ ...original, rationaleQuestionId: "q" }, "same_question"],
      // not_public before same_question.
      [{ ...original, publicAt: late, rationaleQuestionId: "q" }, "not_public"],
      // same_question before self.
      [
        { ...original, rationaleQuestionId: "q", citedAgentId: "B", citedOperatorId: "op-B" },
        "same_question",
      ],
      // not_public even when it is also self.
      [{ ...original, publicAt: late, citedAgentId: "B", citedOperatorId: "op-B" }, "not_public"],
      // A rationale public at the very instant of citing is eligible.
      [{ ...original, publicAt: original.submittedAt }, "credited"],
    ];
    for (const [value, status] of cases) {
      const entry = one(value);
      expect(entry.status, status).toBe(status);
      expect(entry.contribution).toBe(status === "credited" ? 0.1 : 0);
      expect(entry.week).toBe("2025-12-29");
    }
  });

  it("marks a repeated key duplicate, but an ineligible twin never hides the eligible one", () => {
    const original = row("q");
    const second = { ...original, rationaleId: "second" };
    for (const input of [
      [original, second],
      [second, original],
    ])
      expect(statuses(liftLedger(input, caps))).toEqual([
        ["r-q", "credited", 0.1],
        ["second", "duplicate", 0],
      ]);
    const twin = { ...original, rationaleId: "a-early", publicAt: new Date(monday + 1) };
    expect(statuses(liftLedger([original, twin], caps))).toEqual([
      ["a-early", "not_public", 0],
      ["r-q", "credited", 0.1],
    ]);
  });

  it("caps each ordered pair per UTC Monday week and a capped key still blocks a later twin", () => {
    const input = [
      row("a", 0),
      row("b", 1),
      row("c", 2),
      row("d", 3),
      { ...row("d", 3), rationaleId: "r-z" },
      row("sunday", week - 1),
      row("next", week),
    ];
    const ledger = liftLedger([...input].reverse(), caps);
    expect(statuses(ledger)).toEqual([
      ["r-a", "credited", 0.1],
      ["r-b", "credited", 0.1],
      ["r-c", "credited", 0.1],
      ["r-d", "pair_cap", 0],
      ["r-z", "duplicate", 0],
      ["r-sunday", "pair_cap", 0],
      ["r-next", "credited", 0.1],
    ]);
    expect(ledger.map((e) => e.week)).toEqual([
      ...Array<string>(6).fill("2025-12-29"),
      "2026-01-05",
    ]);
  });

  it("credits positive Edge only, and zero or negative Edge still consumes a cap slot", () => {
    const ledger = liftLedger(
      [row("q1", 1, 0.4), row("q2", 2, 0), row("q3", 3, -0.1), row("q4", 4, 0.8)],
      caps,
    );
    expect(statuses(ledger)).toEqual([
      ["r-q1", "credited", 0.2],
      ["r-q2", "zero_edge", 0],
      ["r-q3", "zero_edge", 0],
      ["r-q4", "pair_cap", 0],
    ]);
  });

  it("returns every input row once, in cap order, keeping caller fields, and agrees with aggregateLift", () => {
    type Extended = CitationRow & { readonly citingForecastId: string };
    const extend = (value: CitationRow, citingForecastId: string): Extended => ({
      ...value,
      citingForecastId,
    });
    const input: Extended[] = [
      extend(row("next", week, 0.3), "f-next"),
      extend(row("early", -1, 0.5), "f-earlier"),
      extend({ ...row("self", 2), citedAgentId: "B", citedOperatorId: "op-B" }, "f-self"),
      extend(row("b", 1, 0.25), "f-b"),
      extend({ ...row("b", 1, 0.25), rationaleId: "r-b2" }, "f-b2"),
      extend(row("c", 3, 0), "f-c"),
      extend(row("d", 4, 0.7), "f-d"),
      extend(row("e", 5, 0.9), "f-e"),
      extend({ ...row("late", 6), publicAt: new Date(monday + week) }, "f-late"),
      extend({ ...row("other", 0, 0.6), citingAgentId: "C", citingOperatorId: "op-C" }, "f-other"),
    ];
    const ledger = liftLedger(input, caps);
    expect(ledger).toHaveLength(input.length);
    for (const value of input) expect(ledger.filter((e) => e.row === value)).toHaveLength(1);
    expect(ledger.map((e) => [e.row.citingForecastId, e.status, e.week])).toEqual([
      ["f-earlier", "credited", "2025-12-22"],
      ["f-other", "credited", "2025-12-29"],
      ["f-b", "credited", "2025-12-29"],
      ["f-b2", "duplicate", "2025-12-29"],
      ["f-self", "self", "2025-12-29"],
      ["f-c", "zero_edge", "2025-12-29"],
      ["f-d", "credited", "2025-12-29"],
      ["f-e", "pair_cap", "2025-12-29"],
      ["f-late", "not_public", "2025-12-29"],
      ["f-next", "credited", "2026-01-05"],
    ]);
    let credited = 0;
    for (const entry of ledger) if (entry.status === "credited") credited += entry.contribution;
    expect(Object.is(credited, aggregateLift(liftContributions(input, caps)).lift)).toBe(true);
    const original = row("q");
    expect(() => liftLedger([original, { ...original, finalEdge: 0.3 }], caps)).toThrow(TypeError);
  });
});
