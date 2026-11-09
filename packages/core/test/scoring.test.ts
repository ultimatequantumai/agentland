import { describe, expect, it } from "vitest";
import {
  brier,
  clip,
  edge,
  logScore,
  shrunkMean,
  selectBaseline,
  reliability,
  ece,
  mergeReliability,
  sharpness,
  SCORING_VERSION,
  SNAPSHOT_FRESHNESS_SECONDS,
  type Horizon,
  type MarketSnapshot,
} from "../src/index.js";

const date = (ms: number) => new Date(ms);

describe("binary scores", () => {
  it("reproduces both published outcomes without rounding intermediates", () => {
    expect(brier(0.7, 1)).toBeCloseTo(0.09, 14);
    expect(brier(0.57, 1)).toBeCloseTo(0.1849, 14);
    expect(edge(0.7, 0.57, 1)).toBeCloseTo(0.0949, 14);
    expect(edge(0.7, 0.57, 0)).toBeCloseTo(-0.1651, 14);
    expect(logScore(0.7, 1)).toBe(Math.log(0.7));
    expect(logScore(0.7, 0)).toBe(Math.log(1 - 0.7));
  });
  it("clips only for scores, preserving exact copy-zero including tails", () => {
    expect(clip(0)).toBe(0.001);
    expect(clip(1)).toBe(0.999);
    expect(clip(0.4)).toBe(0.4);
    expect(brier(0, 0)).toBe(0.000001);
    expect(brier(1, 0)).toBe(0.998001);
    expect(logScore(0, 1)).toBe(Math.log(0.001));
    for (const p of [0, 0.0005, 0.001, 0.3, 0.999, 0.9995, 1]) {
      for (const o of [0, 1] as const) expect(edge(p, p, o)).toBe(0);
    }
  });
  it.each([NaN, Infinity, -Infinity, -0.01, 1.01])("rejects invalid p %s", (p) => {
    for (const call of [
      () => clip(p),
      () => brier(p, 1),
      () => logScore(p, 0),
      () => edge(0.5, p, 1),
    ]) {
      expect(call).toThrow(RangeError);
    }
  });
  it("rejects nonbinary outcomes and numeric type impostors", () => {
    expect(() => brier(0.5, 2 as 1)).toThrow(RangeError);
    expect(() => logScore(0.5, NaN as 0)).toThrow(RangeError);
    expect(() => clip("0.5" as unknown as number)).toThrow(TypeError);
  });
  it("shrinks positive and negative totals toward zero, including empty k=0", () => {
    expect(shrunkMean([], 0)).toBe(0);
    expect(shrunkMean([0.1, 0.2], 0)).toBeCloseTo(0.15);
    expect(shrunkMean([-0.1, -0.2], 1)).toBeCloseTo(-0.1);
    expect(shrunkMean([0.1, 0.2], 1)).toBeCloseTo(0.1);
    for (const k of [-1, NaN, Infinity]) expect(() => shrunkMean([1], k)).toThrow();
    expect(() => shrunkMean([NaN], 1)).toThrow();
    expect(() => shrunkMean([Number.MAX_VALUE, Number.MAX_VALUE], 1)).toThrow();
  });
});

describe("baseline provenance", () => {
  const snapshot = (snapshotId: string, ms: number, p = 0.6) => ({
    snapshotId,
    takenAt: date(ms),
    p,
  });
  it("selects latest at submission, with ascending ID tie-break and no sorting mutation", () => {
    const snapshots = Object.freeze([
      snapshot("z", 50),
      snapshot("later", 101),
      snapshot("a", 50, 0.4),
      snapshot("old", -1),
    ]);
    expect(
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(100),
        snapshots,
      }),
    ).toEqual({ kind: "market", snapshotId: "a", p: 0.4 });
    expect(snapshots.map((s) => s.snapshotId)).toEqual(["z", "later", "a", "old"]);
    expect(
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(50),
        snapshots,
      }),
    ).toEqual({ kind: "market", snapshotId: "a", p: 0.4 });
    expect(
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(100),
        snapshots: [snapshot("old", 1), snapshot("new", 99, 0.8)],
      }),
    ).toEqual({ kind: "market", snapshotId: "new", p: 0.8 });
    expect(
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(100),
        snapshots: [snapshot("a", 50, 0.4), snapshot("z", 50), snapshot("future", 101)],
      }),
    ).toEqual({ kind: "market", snapshotId: "a", p: 0.4 });
  });
  it("uses earliest strictly after open only as fallback, never invents market data", () => {
    expect(
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("z", 3), snapshot("b", 2), snapshot("a", 2, 0.7)],
      }),
    ).toEqual({ kind: "market", snapshotId: "a", p: 0.7 });
    expect(
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [],
      }),
    ).toBeNull();
    expect(
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(0),
        snapshots: [snapshot("at-open", 0)],
      }),
    ).toEqual({ kind: "market", snapshotId: "at-open", p: 0.6 });
  });
  it("requires five OTHER unique finals for crowd", () => {
    const finals = Array.from({ length: 5 }, (_, i) => ({
      agentId: `a${i}`,
      p: 0.1 * (i + 1),
      isHouse: false,
    }));
    expect(selectBaseline({ kind: "non-market", agentId: "a0", finals })).toEqual({
      kind: "uniform",
      p: 0.5,
    });
    expect(selectBaseline({ kind: "non-market", agentId: "target", finals })).toEqual({
      kind: "crowd",
      p: 0.3,
    });
    expect(() =>
      selectBaseline({ kind: "non-market", agentId: "target", finals: [...finals, finals[0]!] }),
    ).toThrow();
    expect(
      selectBaseline({
        kind: "non-market",
        agentId: "target",
        finals: [{ agentId: "target", p: 1, isHouse: false }, ...finals],
      }),
    ).toEqual({ kind: "crowd", p: 0.3 });
    expect(selectBaseline({ kind: "non-market", agentId: "target", finals: [] })).toEqual({
      kind: "uniform",
      p: 0.5,
    });
  });
  it("rejects invalid facts rather than repairing them", () => {
    expect(() =>
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(2),
        submittedAt: date(1),
        snapshots: [],
      }),
    ).toThrow();
    expect(() =>
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(NaN),
        submittedAt: date(1),
        snapshots: [],
      }),
    ).toThrow();
    expect(() =>
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("a", NaN)],
      }),
    ).toThrow();
    expect(() =>
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("a", 0), snapshot("a", 1)],
      }),
    ).toThrow();
    expect(() =>
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("", 0)],
      }),
    ).toThrow();
    expect(() => selectBaseline({ kind: "non-market", agentId: "", finals: [] })).toThrow();
    expect(() =>
      selectBaseline({
        kind: "non-market",
        agentId: "a",
        finals: [{ agentId: "b", p: 2, isHouse: false }],
      }),
    ).toThrow();
    expect(() =>
      selectBaseline({
        kind: "non-market",
        agentId: "a",
        finals: [{ agentId: "", p: 0.5, isHouse: false }],
      }),
    ).toThrow();
    expect(() => selectBaseline({ kind: "unknown" } as never)).toThrow(TypeError);
    expect(() =>
      selectBaseline({
        kind: "market",
        horizon: "hour",
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("a", 0, -1)],
      }),
    ).toThrow();
  });

  it("is version 1.2.0", () => {
    expect(SCORING_VERSION).toBe("1.2.0");
  });

  describe("D-03 community baseline", () => {
    const finals5 = Array.from({ length: 5 }, (_, i) => ({
      agentId: `o${i}`,
      p: 0.1 * (i + 1),
      isHouse: false,
    }));
    const community = (snapshots: readonly MarketSnapshot[], finals = finals5) =>
      selectBaseline({
        kind: "community",
        horizon: "hour",
        submittedAt: date(100),
        snapshots,
        agentId: "target",
        finals,
      });

    it("pins the latest snapshot at or before submission with ascending ID ties", () => {
      const snapshots = Object.freeze([
        snapshot("x", 50, 0.3),
        snapshot("b", 100, 0.4),
        snapshot("a", 100, 0.45),
        snapshot("later", 101, 0.9),
      ]);
      expect(community(snapshots)).toEqual({ kind: "community", snapshotId: "a", p: 0.45 });
      expect(snapshots.map((s) => s.snapshotId)).toEqual(["x", "b", "a", "later"]);
    });
    it("never falls back to a later snapshot", () => {
      const crowd = community([snapshot("later", 101, 0.9)]);
      expect(crowd).toEqual({ kind: "crowd", p: 0.3 });
      expect(crowd!.p).not.toBe(0.9);
      expect(community([snapshot("later", 101, 0.9)], [])).toEqual({ kind: "uniform", p: 0.5 });
      expect(community([], [])).toEqual({ kind: "uniform", p: 0.5 });
      expect(community([])).toEqual({ kind: "crowd", p: 0.3 });
    });
    it("rejects invalid facts", () => {
      expect(() => community([snapshot("a", 0), snapshot("a", 1)])).toThrow(TypeError);
      expect(() => community([snapshot("a", 0, 2)])).toThrow();
      expect(() =>
        selectBaseline({
          kind: "community",
          horizon: "hour",
          submittedAt: date(NaN),
          snapshots: [],
          agentId: "t",
          finals: [],
        }),
      ).toThrow();
      expect(() =>
        selectBaseline({
          kind: "community",
          horizon: "hour",
          submittedAt: date(1),
          snapshots: [],
          agentId: "",
          finals: [],
        }),
      ).toThrow();
    });
  });

  describe("D-09 non-house crowd", () => {
    const house = Array.from({ length: 4 }, (_, i) => ({
      agentId: `h${i}`,
      p: 0.9,
      isHouse: true,
    }));
    const real = (n: number) =>
      Array.from({ length: n }, (_, i) => ({ agentId: `r${i}`, p: 0.1 * (i + 1), isHouse: false }));
    const crowd = (agentId: string, finals: { agentId: string; p: number; isHouse: boolean }[]) =>
      selectBaseline({ kind: "non-market", agentId, finals });

    it("excludes house finals from the mean and the quorum", () => {
      const target = { agentId: "t", p: 1, isHouse: false };
      expect(crowd("t", [target, ...house, ...real(4)])).toEqual({ kind: "uniform", p: 0.5 });
      expect(crowd("t", [target, ...house, ...real(5)])).toEqual({ kind: "crowd", p: 0.3 });
      expect(crowd("t", [target, ...real(5)])).toEqual({ kind: "crowd", p: 0.3 });
    });
    it("scores a house target against real others and never counts itself", () => {
      expect(crowd("h0", [...house, ...real(5)])).toEqual({ kind: "crowd", p: 0.3 });
      expect(crowd("r0", [...house, ...real(5)])).toEqual({ kind: "uniform", p: 0.5 });
      expect(crowd("t", [{ agentId: "t", p: 1, isHouse: true }, ...real(5)])).toEqual({
        kind: "crowd",
        p: 0.3,
      });
    });
    it("requires a boolean isHouse and unique agents", () => {
      expect(() => crowd("t", [{ agentId: "a", p: 0.5 } as never])).toThrow(TypeError);
      expect(() => crowd("t", [{ agentId: "a", p: 0.5, isHouse: "false" } as never])).toThrow(
        TypeError,
      );
      expect(() =>
        crowd("t", [
          { agentId: "a", p: 0.5, isHouse: true },
          { agentId: "a", p: 0.5, isHouse: false },
        ]),
      ).toThrow(TypeError);
    });
  });
});

describe("D-18 fresh-pin baseline (1.2.0)", () => {
  const snapshot = (snapshotId: string, ms: number, p = 0.6) =>
    Object.freeze({ snapshotId, takenAt: date(ms), p });
  const openAt = date(0);
  const submitted = 10_000_000;
  const submittedAt = date(submitted);
  const market = (horizon: Horizon, snapshots: readonly MarketSnapshot[]) =>
    selectBaseline({ kind: "market", horizon, openAt, submittedAt, snapshots });
  const others = Object.freeze(
    Array.from({ length: 5 }, (_, i) =>
      Object.freeze({ agentId: `o${i}`, p: 0.1 * (i + 1), isHouse: false }),
    ),
  );
  const community = (
    horizon: Horizon,
    snapshots: readonly MarketSnapshot[],
    finals: typeof others = others,
  ) =>
    selectBaseline({
      kind: "community",
      horizon,
      submittedAt,
      snapshots,
      agentId: "target",
      finals,
    });

  it("freezes twice the snapshot cadence per horizon", () => {
    expect(SNAPSHOT_FRESHNESS_SECONDS).toEqual({
      hour: 120,
      day: 600,
      week: 1800,
      month: 7200,
      long: 7200,
    });
    expect(Object.isFrozen(SNAPSHOT_FRESHNESS_SECONDS)).toBe(true);
  });

  it.each([
    ["hour", 120],
    ["day", 600],
    ["week", 1800],
    ["month", 7200],
    ["long", 7200],
  ] as const)("pins exactly within the %s bound of %i s", (horizon, seconds) => {
    const b = seconds * 1000;
    expect(market(horizon, Object.freeze([snapshot("edge", submitted - b, 0.4)]))).toEqual({
      kind: "market",
      snapshotId: "edge",
      p: 0.4,
    });
    // A stale latest never falls through to the later snapshot.
    const stale = Object.freeze([
      snapshot("stale", submitted - b - 1),
      snapshot("after", submitted + 1, 0.9),
    ]);
    expect(market(horizon, stale)).toBeNull();
    expect(stale.map((s) => s.snapshotId)).toEqual(["stale", "after"]);
    expect(market(horizon, Object.freeze([snapshot("late", submitted + b, 0.7)]))).toEqual({
      kind: "market",
      snapshotId: "late",
      p: 0.7,
    });
    expect(market(horizon, Object.freeze([snapshot("too-late", submitted + b + 1)]))).toBeNull();
    const tie = Object.freeze([
      snapshot("b", submitted - b, 0.2),
      snapshot("a", submitted - b, 0.3),
    ]);
    expect(market(horizon, tie)).toEqual({ kind: "market", snapshotId: "a", p: 0.3 });
    expect(tie.map((s) => s.snapshotId)).toEqual(["b", "a"]);

    expect(community(horizon, Object.freeze([snapshot("c", submitted - b, 0.45)]))).toEqual({
      kind: "community",
      snapshotId: "c",
      p: 0.45,
    });
    // A stale community prediction counts as absent: crowd of the five others, then uniform.
    const staleCommunity = Object.freeze([snapshot("c", submitted - b - 1, 0.45)]);
    expect(community(horizon, staleCommunity)).toEqual({ kind: "crowd", p: 0.3 });
    expect(community(horizon, staleCommunity, Object.freeze([]))).toEqual({
      kind: "uniform",
      p: 0.5,
    });
    expect(staleCommunity.map((s) => s.snapshotId)).toEqual(["c"]);
    expect(others.map((f) => f.agentId)).toEqual(["o0", "o1", "o2", "o3", "o4"]);
  });

  it("refuses an unknown or missing horizon", () => {
    const snapshots = [snapshot("s", submitted - 1)];
    expect(() => market("minute" as Horizon, snapshots)).toThrow(TypeError);
    expect(() => community("minute" as Horizon, snapshots)).toThrow(TypeError);
    expect(() =>
      selectBaseline({ kind: "market", openAt, submittedAt, snapshots } as never),
    ).toThrow(TypeError);
    expect(() =>
      selectBaseline({
        kind: "community",
        submittedAt,
        snapshots,
        agentId: "target",
        finals: others,
      } as never),
    ).toThrow(TypeError);
  });
});

describe("raw calibration diagnostics", () => {
  it("places every decile on its lower bound, and 1 in the final bin", () => {
    const bins = reliability(
      Array.from({ length: 11 }, (_, i) => ({ p: i / 10, o: (i % 2) as 0 | 1 })),
    );
    expect(bins.map((b) => b.count)).toEqual([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]);
    expect(bins[0]).toEqual({
      lower: 0,
      upper: 0.1,
      count: 1,
      meanProbability: 0,
      observedFrequency: 0,
    });
    expect(bins[9]).toEqual({
      lower: 0.9,
      upper: 1,
      count: 2,
      meanProbability: 0.95,
      observedFrequency: 0.5,
    });
    expect(ece(bins, 11)).toBeCloseTo(5.3 / 11, 14);
  });
  it("computes weighted ECE and raw sharpness on independent examples", () => {
    const bins = reliability(
      [
        { p: 0, o: 0 },
        { p: 1, o: 1 },
        { p: 0.6, o: 0 },
      ],
      2,
    );
    expect(ece(bins, 3)).toBeCloseTo(0.2);
    expect(sharpness([0, 1, 0.6])).toBeCloseTo(1.1 / 3);
    expect(sharpness([])).toBe(0);
    expect(ece(reliability([]), 0)).toBe(0);
    expect(
      reliability([]).every(
        (b) => b.count === 0 && b.meanProbability === null && b.observedFrequency === null,
      ),
    ).toBe(true);
  });
  it("rejects incoherent counts, statistics and invalid bin configuration", () => {
    for (const bins of [0, -1, 1.5, NaN, Infinity]) expect(() => reliability([], bins)).toThrow();
    const full = reliability([{ p: 0.5, o: 1 }], 1);
    for (const n of [0, -1, 1.5, NaN]) expect(() => ece(full, n)).toThrow();
    for (const change of [
      { count: -1 },
      { count: 0.5 },
      { meanProbability: null },
      { observedFrequency: null },
      { meanProbability: 2 },
      { observedFrequency: NaN },
      { lower: -1 },
      { upper: 0 },
    ]) {
      expect(() => ece([{ ...full[0]!, ...change }], 1)).toThrow();
    }
    expect(() => ece([{ ...reliability([], 1)[0]!, meanProbability: 0.5 }], 0)).toThrow();
    expect(() => ece([{ ...reliability([], 1)[0]!, observedFrequency: 0 }], 0)).toThrow();
    expect(() =>
      ece([{ ...full[0]!, count: Number.MAX_SAFE_INTEGER }, full[0]!], Number.MAX_SAFE_INTEGER),
    ).toThrow();
    expect(() => reliability([{ p: 2, o: 1 }])).toThrow();
    expect(() => sharpness([Infinity])).toThrow();
  });
});

describe("mergeReliability (C-10)", () => {
  it("adds counts and weights means and frequencies by count, keeping empty bins null", () => {
    const hit = reliability([
      { p: 0.85, o: 1 },
      { p: 0.85, o: 1 },
    ]);
    const split = reliability([
      { p: 0.85, o: 1 },
      { p: 0.85, o: 0 },
    ]);
    const merged = mergeReliability([hit, split]);
    expect(merged).toHaveLength(10);
    expect(merged[8]!.lower).toBe(0.8);
    expect(merged[8]!.upper).toBe(0.9);
    expect(merged[8]!.count).toBe(4);
    expect(merged[8]!.meanProbability).toBeCloseTo(0.85, 12);
    expect(merged[8]!.observedFrequency).toBeCloseTo(0.75, 12);
    for (const [i, bin] of merged.entries())
      if (i !== 8)
        expect(bin).toEqual({
          lower: hit[i]!.lower,
          upper: hit[i]!.upper,
          count: 0,
          meanProbability: null,
          observedFrequency: null,
        });
    expect(ece(merged, 4)).toBeCloseTo(0.1, 12);
  });
  it("merges nothing to nothing and one set to a fresh equal copy", () => {
    expect(mergeReliability([])).toEqual([]);
    expect(ece([], 0)).toBe(0);
    const input = reliability([
      { p: 0.85, o: 1 },
      { p: 0.31, o: 0 },
    ]);
    const snapshot = structuredClone(input);
    const merged = mergeReliability([input]);
    expect(merged).toEqual(input);
    expect(merged).not.toBe(input);
    merged[8]!.count = 99;
    merged.pop();
    expect(input).toEqual(snapshot);
  });
  it("equals the ECE of all forecasts pooled, on generated chunked data", () => {
    for (let seed = 0; seed < 20; seed++) {
      const all = Array.from({ length: 5 + seed * 7 }, (_, i) => ({
        p: ((i * 37 + seed * 11) % 101) / 100,
        o: ((i * 3 + seed) % 5 < 2 ? 1 : 0) as 0 | 1,
      }));
      const parts = 1 + (seed % 4);
      const size = Math.ceil(all.length / parts);
      const chunks = Array.from({ length: parts }, (_, k) => all.slice(k * size, (k + 1) * size));
      const merged = mergeReliability(chunks.map((chunk) => reliability(chunk)));
      const pooled = reliability(all);
      expect(merged.map((b) => b.count)).toEqual(pooled.map((b) => b.count));
      expect(ece(merged, all.length)).toBeCloseTo(ece(pooled, all.length), 12);
    }
  });
  it("refuses mismatched bins and invalid counts", () => {
    const ten = reliability([{ p: 0.5, o: 1 }]);
    expect(() => mergeReliability([ten, reliability([], 5)])).toThrow(RangeError);
    expect(() => mergeReliability([reliability([], 5), ten])).toThrow(RangeError);
    for (const change of [{ lower: 0.31 }, { upper: 0.39 }]) {
      const moved = ten.map((bin, i) => (i === 3 ? { ...bin, ...change } : bin));
      expect(() => mergeReliability([ten, moved])).toThrow(RangeError);
    }
    for (const count of [-1, 0.5]) {
      const corrupt = ten.map((bin, i) => (i === 5 ? { ...bin, count } : bin));
      expect(() => mergeReliability([ten, corrupt])).toThrow();
      expect(() => mergeReliability([corrupt])).toThrow();
    }
  });
});
