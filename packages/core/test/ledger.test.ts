import { describe, expect, it } from "vitest";
import { bucketStats } from "../src/ledger.js";
import type { LedgerRow } from "../src/ledger.js";

const emptyBins = Array.from({ length: 10 }, (_, i) => ({
  lower: i / 10,
  upper: (i + 1) / 10,
  count: 0,
  meanProbability: null,
  observedFrequency: null,
}));
const at = (day: number) => new Date(Date.UTC(2026, 0, day));
const params = {
  shrinkK: 20,
  shares: { horizon: { day: 0.6, week: 0.4 }, topic: { weather: 0.25, finance: 0.75 } },
};

// Stored per-forecast scores (D-01); brier/log equal brier(p,o)/logScore(p,o) for these p.
// Input order is deliberately not resolution order: streaks order by resolvedAt, then forecastId.
const rows: LedgerRow[] = [
  {
    forecastId: "f4",
    p: 0.9,
    outcome: 1,
    brier: 0.01,
    log: Math.log(0.9),
    edge: 0.03,
    horizon: "week",
    topic: "finance",
    resolvedAt: at(5),
  },
  {
    forecastId: "f1",
    p: 0.8,
    outcome: 1,
    brier: 0.04,
    log: Math.log(0.8),
    edge: 0.05,
    horizon: "day",
    topic: "weather",
    resolvedAt: at(1),
  },
  {
    forecastId: "f3",
    p: 0.6,
    outcome: 0,
    brier: 0.36,
    log: Math.log(0.4),
    edge: -0.04,
    horizon: "week",
    topic: "finance",
    resolvedAt: at(3),
  },
  {
    forecastId: "f5",
    p: 0.15,
    outcome: 1,
    brier: 0.7225,
    log: Math.log(0.15),
    edge: -0.01,
    horizon: "day",
    topic: "finance",
    resolvedAt: at(4),
  },
  {
    forecastId: "f2",
    p: 0.3,
    outcome: 0,
    brier: 0.09,
    log: Math.log(0.7),
    edge: 0.02,
    horizon: "day",
    topic: "weather",
    resolvedAt: at(2),
  },
];

describe("bucketStats", () => {
  it("returns the exact docs/05 empty convention", () => {
    expect(bucketStats([], params)).toEqual({
      n_resolved: 0,
      mean_brier: null,
      mean_log: null,
      mean_edge: null,
      shrunk_edge: 0,
      ece: 0,
      reliability_bins: emptyBins,
      by_horizon: {},
      by_topic: {},
      streaks: { edge_streak: { current: 0, longest: 0 } },
    });
  });

  it("aggregates overall stats with k = 20 shrinkage, raw-p reliability bins and ECE", () => {
    const stats = bucketStats(rows, params);
    expect(stats.n_resolved).toBe(5);
    expect(stats.mean_brier).toBeCloseTo(1.2225 / 5, 12);
    expect(stats.mean_log).toBeCloseTo(
      (Math.log(0.8) + Math.log(0.7) + Math.log(0.4) + Math.log(0.9) + Math.log(0.15)) / 5,
      12,
    );
    expect(stats.mean_edge).toBeCloseTo(0.01, 12);
    expect(stats.shrunk_edge).toBeCloseTo(0.05 / 25, 12);
    // ECE = (|0.8-1| + |0.3-0| + |0.6-0| + |0.9-1| + |0.15-1|) / 5
    expect(stats.ece).toBeCloseTo(2.05 / 5, 12);
    expect(stats.reliability_bins).toHaveLength(10);
    expect(stats.reliability_bins.map((bin) => bin.count)).toEqual([0, 1, 0, 1, 0, 0, 1, 0, 1, 1]);
    expect(stats.reliability_bins[8]).toEqual({
      lower: 0.8,
      upper: 0.9,
      count: 1,
      meanProbability: 0.8,
      observedFrequency: 1,
    });
    expect(stats.reliability_bins[0]).toEqual(emptyBins[0]);
    // Resolution order f1+ f2+ f3- f5- f4+.
    expect(stats.streaks).toEqual({ edge_streak: { current: 1, longest: 2 } });
  });

  it("scales division shrinkage as k_div = max(5, round(k × share))", () => {
    const stats = bucketStats(rows, params);
    expect(Object.keys(stats.by_horizon).sort()).toEqual(["day", "week"]);
    expect(Object.keys(stats.by_topic).sort()).toEqual(["finance", "weather"]);

    const day = stats.by_horizon.day!; // f1, f2, f5; k_div = round(12) = 12
    expect(day.n_resolved).toBe(3);
    expect(day.mean_brier).toBeCloseTo(0.8525 / 3, 12);
    expect(day.mean_log).toBeCloseTo((Math.log(0.8) + Math.log(0.7) + Math.log(0.15)) / 3, 12);
    expect(day.mean_edge).toBeCloseTo(0.02, 12);
    expect(day.shrunk_edge).toBeCloseTo(0.06 / 15, 12);
    expect(day.ece).toBeCloseTo(1.35 / 3, 12);

    const week = stats.by_horizon.week!; // f3, f4; k_div = round(8) = 8
    expect(week.n_resolved).toBe(2);
    expect(week.mean_brier).toBeCloseTo(0.185, 12);
    expect(week.mean_log).toBeCloseTo((Math.log(0.4) + Math.log(0.9)) / 2, 12);
    expect(week.mean_edge).toBeCloseTo(-0.005, 12);
    expect(week.shrunk_edge).toBeCloseTo(-0.01 / 10, 12);
    expect(week.ece).toBeCloseTo(0.35, 12);

    const weather = stats.by_topic.weather!; // f1, f2; k_div = max(5, round(5)) = 5
    expect(weather.n_resolved).toBe(2);
    expect(weather.mean_brier).toBeCloseTo(0.065, 12);
    expect(weather.mean_edge).toBeCloseTo(0.035, 12);
    expect(weather.shrunk_edge).toBeCloseTo(0.07 / 7, 12);
    expect(weather.ece).toBeCloseTo(0.25, 12);

    const finance = stats.by_topic.finance!; // f3, f4, f5; k_div = round(15) = 15
    expect(finance.n_resolved).toBe(3);
    expect(finance.mean_brier).toBeCloseTo(1.0925 / 3, 12);
    expect(finance.mean_edge).toBeCloseTo(-0.02 / 3, 12);
    expect(finance.shrunk_edge).toBeCloseTo(-0.02 / 18, 12);
    expect(finance.ece).toBeCloseTo(1.55 / 3, 12);
  });

  it("floors division k at 5 and follows the supplied shrinkK", () => {
    const small = bucketStats(rows, {
      ...params,
      shares: { ...params.shares, topic: { weather: 0.1, finance: 0.75 } },
    });
    expect(small.by_topic.weather!.shrunk_edge).toBeCloseTo(0.07 / 7, 12); // round(2) → 5
    const k10 = bucketStats(rows, { ...params, shrinkK: 10 });
    expect(k10.shrunk_edge).toBeCloseTo(0.05 / 15, 12);
    expect(k10.by_horizon.day!.shrunk_edge).toBeCloseTo(0.06 / 9, 12); // max(5, round(6)) = 6
  });

  it("rejects invalid inputs instead of inventing values", () => {
    const one = rows[0]!;
    expect(() => bucketStats([{ ...one, p: Number.NaN }], params)).toThrow();
    expect(() => bucketStats([{ ...one, p: Number.POSITIVE_INFINITY }], params)).toThrow();
    expect(() => bucketStats([{ ...one, outcome: 2 as 0 }], params)).toThrow();
    expect(() => bucketStats([{ ...one, edge: Number.NaN }], params)).toThrow();
    expect(() => bucketStats(rows, { ...params, shrinkK: 0 })).toThrow();
    expect(() => bucketStats(rows, { ...params, shrinkK: -1 })).toThrow();
    expect(() => bucketStats([one, { ...one }], params)).toThrow(); // duplicate forecastId
    expect(() => bucketStats([{ ...one, horizon: "year" as "day" }], params)).toThrow();
    expect(() => bucketStats([{ ...one, topic: "gossip" as "weather" }], params)).toThrow();
    expect(() => bucketStats([{ ...one, brier: Number.NaN }], params)).toThrow();
    // A populated bucket without its share has no defined k_div.
    expect(() =>
      bucketStats(rows, { ...params, shares: { ...params.shares, horizon: { day: 0.6 } } }),
    ).toThrow();
  });
});
