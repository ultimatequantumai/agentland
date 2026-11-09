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
  sharpness,
  SCORING_VERSION,
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
      selectBaseline({ kind: "market", openAt: date(0), submittedAt: date(100), snapshots }),
    ).toEqual({ kind: "market", snapshotId: "a", p: 0.4 });
    expect(snapshots.map((s) => s.snapshotId)).toEqual(["z", "later", "a", "old"]);
    expect(
      selectBaseline({ kind: "market", openAt: date(0), submittedAt: date(50), snapshots }),
    ).toEqual({ kind: "market", snapshotId: "a", p: 0.4 });
    expect(
      selectBaseline({
        kind: "market",
        openAt: date(0),
        submittedAt: date(100),
        snapshots: [snapshot("old", 1), snapshot("new", 99, 0.8)],
      }),
    ).toEqual({ kind: "market", snapshotId: "new", p: 0.8 });
    expect(
      selectBaseline({
        kind: "market",
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
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("z", 3), snapshot("b", 2), snapshot("a", 2, 0.7)],
      }),
    ).toEqual({ kind: "market", snapshotId: "a", p: 0.7 });
    expect(
      selectBaseline({ kind: "market", openAt: date(0), submittedAt: date(1), snapshots: [] }),
    ).toBeNull();
    expect(
      selectBaseline({
        kind: "market",
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
      selectBaseline({ kind: "market", openAt: date(2), submittedAt: date(1), snapshots: [] }),
    ).toThrow();
    expect(() =>
      selectBaseline({ kind: "market", openAt: date(NaN), submittedAt: date(1), snapshots: [] }),
    ).toThrow();
    expect(() =>
      selectBaseline({
        kind: "market",
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("a", NaN)],
      }),
    ).toThrow();
    expect(() =>
      selectBaseline({
        kind: "market",
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("a", 0), snapshot("a", 1)],
      }),
    ).toThrow();
    expect(() =>
      selectBaseline({
        kind: "market",
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
        openAt: date(0),
        submittedAt: date(1),
        snapshots: [snapshot("a", 0, -1)],
      }),
    ).toThrow();
  });

  it("is version 1.1.0", () => {
    expect(SCORING_VERSION).toBe("1.1.0");
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
          submittedAt: date(NaN),
          snapshots: [],
          agentId: "t",
          finals: [],
        }),
      ).toThrow();
      expect(() =>
        selectBaseline({
          kind: "community",
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
