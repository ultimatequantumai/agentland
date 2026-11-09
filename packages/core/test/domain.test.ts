import { describe, expect, it } from "vitest";
import {
  aggregateSeason,
  aggregateDivision,
  horizonFor,
  isTopic,
  formatProbability,
  formatEdgePoints,
  edgeStreak,
  badges,
} from "../src/index.js";
import type { BadgeInput, QuestionClassification } from "../src/index.js";

describe("season and division aggregation", () => {
  it("distinguishes empty, provisional and ranked, preserving signed means", () => {
    expect(aggregateSeason([])).toEqual({
      nResolved: 0,
      meanEdge: null,
      shrunkEdge: 0,
      ranked: false,
      shrinkK: 20,
      minResolvedForRank: 30,
    });
    for (const n of [29, 30, 31]) {
      const result = aggregateSeason(Array<number>(n).fill(-0.1));
      expect(result.ranked).toBe(n >= 30);
      expect(result.meanEdge).toBeCloseTo(-0.1);
      expect(result.shrunkEdge).toBeCloseTo((-0.1 * n) / (n + 20));
    }
    expect(aggregateSeason([0.5], { shrinkK: 0, minResolvedForRank: 1 }).shrunkEdge).toBe(0.5);
  });
  it("filters first and scales by all-question share with half-up rounding", () => {
    const rows = [
      { horizon: "hour", topic: "crypto", edge: 0.1 },
      { horizon: "day", topic: "crypto", edge: 0.3 },
      { horizon: "hour", topic: "weather", edge: -0.2 },
    ] as const;
    expect(aggregateDivision(rows, { horizon: "hour" }, 0.25)).toEqual({
      nResolved: 2,
      meanEdge: -0.05,
      shrunkEdge: -0.1 / 7,
      ranked: false,
      shrinkK: 5,
      minResolvedForRank: 8,
    });
    expect(
      aggregateDivision(rows, { topic: "crypto" }, 0.5, { shrinkK: 11, minResolvedForRank: 3 }),
    ).toEqual({
      nResolved: 2,
      meanEdge: 0.2,
      shrunkEdge: 0.05,
      ranked: true,
      shrinkK: 6,
      minResolvedForRank: 2,
    });
    expect(aggregateDivision(rows, { topic: "crypto" }, 0).ranked).toBe(false);
    expect(aggregateDivision(rows, { topic: "other" }, 0.1).meanEdge).toBeNull();
  });
  it("rejects malformed parameters and division rows", () => {
    for (const shrinkK of [-1, Infinity]) expect(() => aggregateSeason([], { shrinkK })).toThrow();
    for (const minResolvedForRank of [0, 1.5, Infinity])
      expect(() => aggregateSeason([], { minResolvedForRank })).toThrow();
    expect(() => aggregateSeason([NaN])).toThrow();
    for (const share of [-0.1, 1.1, NaN])
      expect(() => aggregateDivision([], { horizon: "hour" }, share)).toThrow();
    expect(() => aggregateDivision([], { horizon: "unknown" as "hour" }, 0.5)).toThrow();
    expect(() => aggregateDivision([], { topic: "unknown" as "other" }, 0.5)).toThrow();
    expect(() =>
      aggregateDivision(
        [{ horizon: "hour", topic: "other", edge: Infinity }],
        { horizon: "day" },
        0.5,
      ),
    ).toThrow();
    expect(() =>
      aggregateDivision(
        [{ horizon: "bad" as "hour", topic: "other", edge: 0 }],
        { horizon: "hour" },
        0.5,
      ),
    ).toThrow();
    expect(() =>
      aggregateDivision(
        [{ horizon: "hour", topic: "bad" as "other", edge: 0 }],
        { horizon: "hour" },
        0.5,
      ),
    ).toThrow();
  });
});

describe("classification and presentation", () => {
  it("uses all inclusive cutoffs and rejects reversed or invalid dates", () => {
    const hour = 3_600_000;
    const cases = [
      [0, "hour"],
      [2 * hour, "hour"],
      [2 * hour + 1, "day"],
      [36 * hour, "day"],
      [36 * hour + 1, "week"],
      [240 * hour, "week"],
      [240 * hour + 1, "month"],
      [1080 * hour, "month"],
      [1080 * hour + 1, "long"],
    ] as const;
    for (const [ms, expected] of cases)
      expect(horizonFor(new Date(0), new Date(ms))).toBe(expected);
    expect(() => horizonFor(new Date(1), new Date(0))).toThrow();
    expect(() => horizonFor(new Date(NaN), new Date(0))).toThrow();
    expect(() => horizonFor(new Date(0), new Date(NaN))).toThrow();
    expect(() => horizonFor(0 as unknown as Date, new Date(0))).toThrow(TypeError);
  });
  it("accepts exactly the named topics with singular topic and optional tags", () => {
    for (const topic of [
      "finance",
      "crypto",
      "weather",
      "sports",
      "politics",
      "economics",
      "science_tech",
      "culture",
      "world",
      "other",
    ])
      expect(isTopic(topic)).toBe(true);
    for (const topic of ["SCIENCE", "", null, ["crypto"], 1]) expect(isTopic(topic)).toBe(false);
    const classified: QuestionClassification = { topic: "science_tech", tags: ["space"] };
    expect(isTopic(classified.topic)).toBe(true);
  });
  it("formats raw probabilities and signed Edge, including rounded negative zero", () => {
    expect(formatProbability(0.7)).toBe("70.0%");
    expect(formatProbability(0)).toBe("0.0%");
    expect(formatProbability(1)).toBe("100.0%");
    expect(formatEdgePoints(0.0949)).toBe("+9.5 pts");
    expect(formatEdgePoints(-0.1651)).toBe("-16.5 pts");
    expect(formatEdgePoints(-0.00001)).toBe("+0.0 pts");
    expect(formatEdgePoints(-0)).toBe("+0.0 pts");
    expect(() => formatProbability(2)).toThrow();
    expect(() => formatEdgePoints(NaN)).toThrow();
    expect(formatEdgePoints(aggregateSeason([0.1]).shrunkEdge)).toBe("+0.5 pts");
  });
});

describe("display-only streaks and badges", () => {
  const base: BadgeInput = {
    calibrationCount: 0,
    calibrationEce: null,
    seasonShrunkEdge: 0,
    seasonResolved: 0,
    allTimeResolved: 0,
    agentId: "a",
    liftStandings: [],
  };
  it("orders resolutions then IDs and resets on zero and negative", () => {
    const row = (forecastId: string, ms: number, edge: number) => ({
      forecastId,
      resolvedAt: new Date(ms),
      edge,
    });
    expect(edgeStreak([])).toEqual({ current: 0, longest: 0 });
    expect(
      edgeStreak([
        row("f", 3, 0.1),
        row("b", 0, 0.1),
        row("a", 0, 0.1),
        row("e", 2, -0.1),
        row("c", 1, 0),
        row("g", 4, 0.1),
      ]),
    ).toEqual({ current: 2, longest: 2 });
    expect(edgeStreak([row("z", 0, 0.1), row("a", 0, 0)])).toEqual({ current: 1, longest: 1 });
    expect(() => edgeStreak([row("a", 0, 0.1), row("a", 1, 0.2)])).toThrow();
    expect(() => edgeStreak([row("", 0, 0.1)])).toThrow();
    expect(() => edgeStreak([row("a", NaN, 0.1)])).toThrow();
    expect(() => edgeStreak([row("a", 0, NaN)])).toThrow();
  });
  it("honors strict quality thresholds and inclusive count boundaries", () => {
    expect(badges(base)).toEqual([]);
    for (const calibrationCount of [99, 100, 101])
      expect(
        badges({
          ...base,
          calibrationCount,
          allTimeResolved: calibrationCount,
          calibrationEce: 0.049,
        }),
      ).toEqual(calibrationCount >= 100 ? ["Calibrated"] : []);
    for (const calibrationEce of [0.049, 0.05, 0.051])
      expect(
        badges({ ...base, calibrationCount: 100, allTimeResolved: 100, calibrationEce }),
      ).toEqual(calibrationEce < 0.05 ? ["Calibrated"] : []);
    expect(
      badges({ ...base, calibrationCount: 100, allTimeResolved: 100, calibrationEce: null }),
    ).toEqual([]);
    for (const seasonResolved of [199, 200, 201])
      expect(
        badges({
          ...base,
          seasonResolved,
          allTimeResolved: seasonResolved,
          seasonShrunkEdge: 0.011,
        }),
      ).toEqual(seasonResolved >= 200 ? ["Market Beater"] : []);
    for (const seasonShrunkEdge of [0.009, 0.01, 0.011])
      expect(
        badges({ ...base, seasonResolved: 200, allTimeResolved: 200, seasonShrunkEdge }),
      ).toEqual(seasonShrunkEdge > 0.01 ? ["Market Beater"] : []);
    for (const allTimeResolved of [999, 1000, 1001])
      expect(badges({ ...base, allTimeResolved })).toEqual(
        allTimeResolved >= 1000 ? ["Ironclad"] : [],
      );
  });
  it("ranks Teacher by raw Lift with stable tied-zero ordinal places", () => {
    expect(badges({ ...base, liftStandings: [{ agentId: "a", lift: 0 }] })).toEqual(["Teacher"]);
    const liftStandings = Array.from({ length: 11 }, (_, i) => ({
      agentId: String(i).padStart(2, "0"),
      lift: 0,
    }));
    expect(badges({ ...base, agentId: "01", liftStandings: [...liftStandings].reverse() })).toEqual(
      ["Teacher"],
    );
    expect(badges({ ...base, agentId: "02", liftStandings })).toEqual([]);
    expect(badges({ ...base, agentId: "absent", liftStandings })).toEqual([]);
    expect(
      badges({
        ...base,
        calibrationCount: 100,
        calibrationEce: 0,
        seasonResolved: 200,
        seasonShrunkEdge: 0.02,
        allTimeResolved: 1000,
        liftStandings: [
          { agentId: "b", lift: 0.2 },
          { agentId: "a", lift: 0.3 },
        ],
      }),
    ).toEqual(["Calibrated", "Market Beater", "Teacher", "Ironclad"]);
  });
  it("rejects incoherent badge facts and duplicate standings", () => {
    for (const change of [
      { calibrationCount: -1 },
      { calibrationCount: 1.5 },
      { calibrationCount: 1, allTimeResolved: 0 },
      { calibrationEce: 2 },
      { seasonShrunkEdge: Infinity },
      { seasonResolved: 1, allTimeResolved: 0 },
      { allTimeResolved: -1 },
      { agentId: "" },
    ])
      expect(() => badges({ ...base, ...change })).toThrow();
    expect(() =>
      badges({
        ...base,
        liftStandings: [
          { agentId: "a", lift: 0 },
          { agentId: "a", lift: 1 },
        ],
      }),
    ).toThrow();
    expect(() => badges({ ...base, liftStandings: [{ agentId: "a", lift: -0.1 }] })).toThrow();
    expect(() => badges({ ...base, liftStandings: [{ agentId: "", lift: 0 }] })).toThrow();
  });
});
