import { afterEach, describe, expect, it, vi } from "vitest";
import {
  selectBaseline,
  edge,
  aggregateSeason,
  aggregateDivision,
  formatEdgePoints,
  reliability,
  ece,
  sharpness,
  trustScore,
  liftContributions,
  aggregateLift,
  edgeStreak,
  badges,
  horizonFor,
} from "../src/index.js";
import type { CitationRow, TrustInput } from "../src/index.js";

afterEach(() => {
  vi.unstubAllGlobals();
  vi.restoreAllMocks();
});

describe("public pure consumer boundary", () => {
  it("runs baseline-to-score-to-season/display over frozen caller records", () => {
    const snapshots = Object.freeze([
      Object.freeze({ snapshotId: "s", takenAt: new Date(50), p: 0.57 }),
    ]);
    const input = Object.freeze({
      kind: "market" as const,
      openAt: new Date(0),
      submittedAt: new Date(100),
      snapshots,
    });
    const baseline = selectBaseline(input);
    if (baseline === null) throw new Error("expected recorded baseline");
    const score = edge(0.7, baseline.p, 1);
    const edges = Object.freeze(Array<number>(30).fill(score));
    expect(formatEdgePoints(score)).toBe("+9.5 pts");
    const season = aggregateSeason(edges);
    expect(season.shrunkEdge).toBeCloseTo(0.05694);
    expect(formatEdgePoints(season.shrunkEdge)).toBe("+5.7 pts");
    expect(
      aggregateDivision(
        Object.freeze([{ horizon: "hour", topic: "crypto", edge: score }] as const),
        { horizon: "hour" },
        0.4,
      ).shrunkEdge,
    ).toBeCloseTo(0.0949 / 9);
    expect(input.snapshots[0]?.takenAt.getTime()).toBe(50);
    expect(edges).toHaveLength(30);
    expect(() => edge(0.7, 2, 1)).toThrow();
  });
  it("calibration and trust agree on immutable supplied public facts", () => {
    const resolved = Object.freeze(
      Array.from({ length: 30 }, (_, i) =>
        Object.freeze({ forecastId: `f${i}`, p: 0.6, o: 1 as const, resolvedAt: new Date(i) }),
      ),
    );
    const clockDate = new Date(100);
    const input: TrustInput = Object.freeze({
      clock: { now: () => clockDate },
      resolved,
      seasonRankPercentiles: Object.freeze([0, 1]),
      seasonsPlayed: 6,
      upheldHonorViolationTimes: Object.freeze([]),
      publicSuspensions: 0,
      upheldConductDisputes: 0,
    });
    expect(ece(reliability(resolved), resolved.length)).toBeCloseTo(0.4);
    expect(sharpness(resolved.map((r) => r.p))).toBeCloseTo(0.1);
    expect(trustScore(input).components.calibration_score).toBeCloseTo(0.6);
    expect(trustScore(input).score).toBeCloseTo(0.67);
    expect(resolved[0]?.forecastId).toBe("f0");
    expect(clockDate.getTime()).toBe(100);
  });
  it("uses no ambient clock, default Date constructor or network", () => {
    const NativeDate = Date;
    const supplied = new NativeDate("2026-01-05T00:00:00Z");
    const older = new NativeDate(supplied.getTime() - 1);
    vi.stubGlobal(
      "Date",
      new Proxy(NativeDate, {
        construct(target, args) {
          if (args.length === 0) throw new Error("ambient Date");
          return Reflect.construct(target, args);
        },
        apply() {
          throw new Error("ambient Date()");
        },
        get(target, property, receiver) {
          if (property === "now")
            return () => {
              throw new Error("ambient Date.now");
            };
          return Reflect.get(target, property, receiver);
        },
      }),
    );
    vi.stubGlobal("fetch", () => {
      throw new Error("network");
    });
    expect(horizonFor(older, supplied)).toBe("hour");
    const citations: readonly CitationRow[] = Object.freeze([
      Object.freeze({
        rationaleId: "r",
        rationaleQuestionId: "old",
        questionId: "new",
        citingAgentId: "b",
        citedAgentId: "a",
        citingOperatorId: "b-op",
        citedOperatorId: "a-op",
        submittedAt: supplied,
        publicAt: older,
        finalEdge: 0.2,
      }),
    ]);
    const admitted = liftContributions(citations, { pairCapWeek: 3 });
    expect(aggregateLift(admitted).shrunkLift).toBeCloseTo(0.1 / 11);
    expect(
      edgeStreak(Object.freeze([{ forecastId: "f", resolvedAt: supplied, edge: 0.2 }])),
    ).toEqual({ current: 1, longest: 1 });
    expect(
      badges({
        calibrationCount: 0,
        calibrationEce: null,
        seasonShrunkEdge: 0,
        seasonResolved: 0,
        allTimeResolved: 0,
        agentId: "a",
        liftStandings: [{ agentId: "a", lift: 0.1 }],
      }),
    ).toEqual(["Teacher"]);
    expect(
      trustScore({
        clock: { now: () => supplied },
        resolved: [],
        seasonRankPercentiles: [],
        seasonsPlayed: 0,
        upheldHonorViolationTimes: [older],
        publicSuspensions: 0,
        upheldConductDisputes: 0,
      }).components.honor,
    ).toBeGreaterThanOrEqual(0);
    expect(supplied.toISOString()).toBe("2026-01-05T00:00:00.000Z");
  });
});
