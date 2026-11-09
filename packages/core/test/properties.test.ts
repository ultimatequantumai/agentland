import { describe, expect, it } from "vitest";
import { brier, edge, shrunkMean, reliability, ece, liftContributions } from "../src/index.js";
import type { CitationRow, Outcome } from "../src/index.js";

describe("independent deterministic properties", () => {
  it("has exact copy-zero throughout domain including clipping equivalence tails", () => {
    for (let i = 0; i <= 1000; i++)
      for (const outcome of [0, 1] as const) expect(edge(i / 1000, i / 1000, outcome)).toBe(0);
    expect(brier(0, 1)).toBe(brier(0.001, 1));
    expect(brier(1, 0)).toBe(brier(0.999, 0));
  });
  it("minimizes independent probability-weighted Brier at truth on clipped interior", () => {
    const grid = [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99, 0.999];
    for (const truth of grid) {
      const optimum = truth * (1 - truth);
      for (const report of grid) {
        const loss = truth * brier(report, 1) + (1 - truth) * brier(report, 0);
        expect(loss).toBeCloseTo(optimum + (report - truth) ** 2, 13);
        if (report !== truth) expect(loss).toBeGreaterThan(optimum);
        else expect(loss).toBeCloseTo(optimum, 14);
      }
    }
  });
  it("approaches fixed positive AND negative means with n, preserving k=0 and zero", () => {
    for (const mean of [-0.8, -0.1, 0, 0.1, 0.8]) {
      let previousDistance = Infinity;
      for (const n of [1, 2, 10, 30, 100, 1000]) {
        const result = shrunkMean(Array<number>(n).fill(mean), 20);
        expect(result).toBeCloseTo((mean * n) / (n + 20), 12);
        expect(Math.abs(result - mean)).toBeLessThanOrEqual(previousDistance + 1e-14);
        expect(shrunkMean(Array<number>(n).fill(mean), 0)).toBeCloseTo(mean, 12);
        previousDistance = Math.abs(result - mean);
      }
    }
  });
  it("keeps ECE bounded across independently generated raw probabilities and outcomes", () => {
    for (let seed = 0; seed < 30; seed++) {
      const rows = Array.from({ length: seed * 7 }, (_, i) => ({
        p: ((i * 37 + seed) % 101) / 100,
        o: ((i + seed) % 2) as Outcome,
      }));
      const result = ece(reliability(rows), rows.length);
      expect(result).toBeGreaterThanOrEqual(0);
      expect(result).toBeLessThanOrEqual(1);
    }
    expect(
      ece(
        reliability([
          { p: 0, o: 1 },
          { p: 1, o: 0 },
        ]),
        2,
      ),
    ).toBe(1);
  });
  it("preserves nonnegative capped Lift and permutation invariance on generated graphs", () => {
    const start = Date.parse("2026-01-05T00:00:00Z");
    for (let seed = 0; seed < 12; seed++) {
      const rows: CitationRow[] = Array.from({ length: 45 }, (_, i) => ({
        rationaleId: `r${i}`,
        rationaleQuestionId: "old",
        questionId: `q${i}`,
        citingAgentId: `c${i % 3}`,
        citedAgentId: "teacher",
        citingOperatorId: `operator${i % 3}`,
        citedOperatorId: "teacher-op",
        publicAt: new Date(start - 1),
        submittedAt: new Date(start + i * 86_400_000),
        finalEdge: (((i * 7 + seed) % 11) - 5) / 10,
      }));
      const result = liftContributions(rows, { pairCapWeek: 3 });
      expect(liftContributions([...rows].reverse(), { pairCapWeek: 3 })).toEqual(result);
      expect(
        liftContributions([...rows.slice(17), ...rows.slice(0, 17)], { pairCapWeek: 3 }),
      ).toEqual(result);
      const counts = new Map<string, number>();
      for (const admitted of result) {
        expect(admitted.contribution).toBeGreaterThanOrEqual(0);
        const original = rows.find((r) => r.questionId === admitted.questionId)!;
        expect(admitted.contribution).toBe(original.finalEdge > 0 ? original.finalEdge / 2 : 0);
        const key = `${admitted.citingAgentId}/${admitted.citedAgentId}/${admitted.week}`;
        counts.set(key, (counts.get(key) ?? 0) + 1);
      }
      for (const count of counts.values()) expect(count).toBeLessThanOrEqual(3);
    }
  });
});
