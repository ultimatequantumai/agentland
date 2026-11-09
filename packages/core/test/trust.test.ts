import { describe, expect, it } from "vitest";
import { trustScore } from "../src/index.js";
import type { TrustInput, ResolvedForecast } from "../src/index.js";

const now = Date.parse("2026-07-01T00:00:00Z");
const day = 86_400_000;
const base: TrustInput = {
  clock: { now: () => new Date(now) },
  resolved: [],
  seasonRankPercentiles: [],
  seasonsPlayed: 0,
  upheldHonorViolationTimes: [],
  publicSuspensions: 0,
  upheldConductDisputes: 0,
};
const forecasts = (n: number): ResolvedForecast[] =>
  Array.from({ length: n }, (_, i) => ({
    forecastId: `f${String(i).padStart(4, "0")}`,
    p: 1,
    o: 1,
    resolvedAt: new Date(now - i),
  }));

describe("transparent trust", () => {
  it("returns raw components and reads only the supplied clock once", () => {
    let reads = 0;
    const result = trustScore({
      ...base,
      clock: {
        now: () => {
          reads++;
          return new Date(now);
        },
      },
    });
    expect(reads).toBe(1);
    expect(result).toEqual({
      score: 0.2,
      components: { calibration_score: 0, consistency: 0, tenure: 0, honor: 1, incidents: 0 },
    });
  });
  it("calibration requires 30 raw-probability resolved forecasts", () => {
    expect(trustScore({ ...base, resolved: forecasts(29) }).components.calibration_score).toBe(0);
    expect(trustScore({ ...base, resolved: forecasts(30) }).components.calibration_score).toBe(1);
    expect(
      trustScore({ ...base, resolved: forecasts(30).map((r) => ({ ...r, p: 0.7, o: 0 })) })
        .components.calibration_score,
    ).toBeCloseTo(0.3);
  });
  it("uses only newest 500 and stable ID ordering for timestamp ties", () => {
    const rows = forecasts(501);
    rows[500] = { ...rows[500]!, p: 0 };
    expect(trustScore({ ...base, resolved: rows }).components.calibration_score).toBe(1);
    rows[0] = { ...rows[0]!, p: 0 };
    expect(
      trustScore({ ...base, resolved: [...rows].reverse() }).components.calibration_score,
    ).toBeCloseTo(0.998);
    const tied = forecasts(501).map((r) => ({
      ...r,
      resolvedAt: new Date(now),
      p: r.forecastId === "f0500" ? 0 : 1,
    }));
    expect(trustScore({ ...base, resolved: tied.reverse() }).components.calibration_score).toBe(1);
    expect(trustScore({ ...base, resolved: forecasts(500) }).components.calibration_score).toBe(1);
  });
  it("uses population variance, bounded tenure and no percentile rescaling", () => {
    expect(trustScore(base).components.consistency).toBe(0);
    expect(trustScore({ ...base, seasonRankPercentiles: [0.2] }).components.consistency).toBe(1);
    expect(trustScore({ ...base, seasonRankPercentiles: [0, 1] }).components.consistency).toBe(
      0.75,
    );
    expect(
      trustScore({ ...base, seasonRankPercentiles: [0.25, 0.75] }).components.consistency,
    ).toBe(0.9375);
    for (const seasonsPlayed of [0, 1, 5, 6, 7])
      expect(trustScore({ ...base, seasonsPlayed }).components.tenure).toBe(
        Math.min(1, seasonsPlayed / 6),
      );
  });
  it("decays honor penalties at 0/90/180 days and sums before clamping honor", () => {
    for (const [age, honor] of [
      [0, 0],
      [90, 0.5],
      [180, 0.75],
    ] as const) {
      expect(
        trustScore({ ...base, upheldHonorViolationTimes: [new Date(now - age * day)] }).components
          .honor,
      ).toBe(honor);
    }
    expect(
      trustScore({
        ...base,
        upheldHonorViolationTimes: [new Date(now - 90 * day), new Date(now - 180 * day)],
      }).components.honor,
    ).toBe(0.25);
    expect(
      trustScore({ ...base, upheldHonorViolationTimes: [new Date(now), new Date(now)] }).components
        .honor,
    ).toBe(0);
    const facts = { ...base, upheldHonorViolationTimes: [new Date(now)] };
    expect(
      trustScore({ ...facts, clock: { now: () => new Date(now + 90 * day) } }).components.honor,
    ).toBe(0.5);
  });
  it("exposes raw incident count and negative totals without hidden normalization", () => {
    const result = trustScore({
      ...base,
      resolved: forecasts(30),
      seasonRankPercentiles: [0, 1],
      seasonsPlayed: 3,
      upheldHonorViolationTimes: [new Date(now - 90 * day)],
      publicSuspensions: 3,
      upheldConductDisputes: 4,
    });
    expect(result.components).toEqual({
      calibration_score: 1,
      consistency: 0.75,
      tenure: 0.5,
      honor: 0.5,
      incidents: 7,
    });
    expect(result.score).toBeCloseTo(-0.85);
  });
  it("rejects bad dates, future facts, duplicate forecasts and invalid domains", () => {
    for (const change of [
      { seasonsPlayed: -1 },
      { seasonsPlayed: 1.5 },
      { publicSuspensions: -0.1 },
      { upheldConductDisputes: Infinity },
      { seasonRankPercentiles: [-0.1] },
      { seasonRankPercentiles: [1.1] },
      { seasonRankPercentiles: [NaN] },
      { clock: { now: () => new Date(NaN) } },
      { upheldHonorViolationTimes: [new Date(now + 1)] },
      { upheldHonorViolationTimes: [new Date(NaN)] },
    ])
      expect(() => trustScore({ ...base, ...change })).toThrow();
    const one = forecasts(1)[0]!;
    for (const change of [
      { forecastId: "" },
      { resolvedAt: new Date(now + 1) },
      { resolvedAt: new Date(NaN) },
      { p: NaN },
      { o: 2 as 1 },
    ])
      expect(() => trustScore({ ...base, resolved: [{ ...one, ...change }] })).toThrow();
    expect(() => trustScore({ ...base, resolved: [one, one] })).toThrow();
    expect(() =>
      trustScore({ ...base, publicSuspensions: Number.MAX_SAFE_INTEGER, upheldConductDisputes: 1 }),
    ).toThrow();
  });
});
