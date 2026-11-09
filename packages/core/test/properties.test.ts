import { describe, expect, it } from "vitest";
import {
  brier,
  edge,
  shrunkMean,
  shrunkTrack,
  selectBaseline,
  reliability,
  ece,
  liftContributions,
  liftLedger,
  LIFT_STATUSES,
} from "../src/index.js";
import type {
  CitationGraphInput,
  CitationRow,
  Horizon,
  LiftCaps,
  LiftResult,
  MarketSnapshot,
  Outcome,
} from "../src/index.js";

// frozen pre-Phase-8 oracle (C-05: byte-identical, no SCORING_VERSION bump).
// Verbatim copy of liftContributions and the validators it called (lift.ts:31-100,
// scoring.ts:24-48) as of SCORING_VERSION 1.1.0. Never edit it to match new code.
function finite(value: number, name: string): void {
  if (typeof value !== "number") throw new TypeError(`${name} must be a number`);
  if (!Number.isFinite(value)) throw new RangeError(`${name} must be finite`);
}
function count(value: number, name: string): void {
  if (!Number.isSafeInteger(value) || value < 0)
    throw new RangeError(`${name} must be a nonnegative safe integer`);
}
function identifier(value: string): void {
  if (typeof value !== "string" || value.trim().length === 0)
    throw new TypeError("identifier must be nonempty text");
}
function timestamp(value: Date): number {
  if (!(value instanceof Date)) throw new TypeError("timestamp must be a Date");
  const ms = value.getTime();
  if (!Number.isFinite(ms)) throw new RangeError("invalid timestamp");
  return ms;
}
function referenceLiftContributions(input: CitationGraphInput, caps: LiftCaps): LiftResult[] {
  count(caps.pairCapWeek, "pair cap per week");
  const finals = new Map<string, CitationRow>();
  const eligible: CitationRow[] = [];
  for (const row of input) {
    for (const id of [
      row.rationaleId,
      row.rationaleQuestionId,
      row.questionId,
      row.citingAgentId,
      row.citedAgentId,
      row.citingOperatorId,
      row.citedOperatorId,
    ])
      identifier(id);
    const submitted = timestamp(row.submittedAt);
    const published = timestamp(row.publicAt);
    finite(row.finalEdge, "final Edge");
    const key = JSON.stringify([row.citingAgentId, row.citedAgentId, row.questionId]);
    const previous = finals.get(key);
    if (
      previous !== undefined &&
      (previous.finalEdge !== row.finalEdge ||
        previous.submittedAt.getTime() !== submitted ||
        previous.citingOperatorId !== row.citingOperatorId ||
        previous.citedOperatorId !== row.citedOperatorId)
    )
      throw new TypeError("conflicting final citation facts");
    finals.set(key, row);
    if (
      published <= submitted &&
      row.rationaleQuestionId !== row.questionId &&
      row.citingAgentId !== row.citedAgentId &&
      row.citingOperatorId !== row.citedOperatorId
    )
      eligible.push(row);
  }
  eligible.sort(
    (a, b) =>
      a.submittedAt.getTime() - b.submittedAt.getTime() ||
      (a.questionId < b.questionId ? -1 : a.questionId > b.questionId ? 1 : 0) ||
      (a.rationaleId < b.rationaleId ? -1 : a.rationaleId > b.rationaleId ? 1 : 0) ||
      (a.citingAgentId < b.citingAgentId ? -1 : a.citingAgentId > b.citingAgentId ? 1 : 0) ||
      (a.citedAgentId < b.citedAgentId ? -1 : a.citedAgentId > b.citedAgentId ? 1 : 0),
  );
  const seen = new Set<string>();
  const pairWeeks = new Map<string, number>();
  const result: LiftResult[] = [];
  for (const row of eligible) {
    const finalKey = JSON.stringify([row.citingAgentId, row.citedAgentId, row.questionId]);
    if (seen.has(finalKey)) continue;
    seen.add(finalKey);
    const monday = new Date(row.submittedAt.getTime());
    monday.setUTCHours(0, 0, 0, 0);
    monday.setUTCDate(monday.getUTCDate() - ((monday.getUTCDay() + 6) % 7));
    const week = monday.toISOString().split("T")[0]!;
    const pairWeek = JSON.stringify([row.citingAgentId, row.citedAgentId, week]);
    const admitted = pairWeeks.get(pairWeek) ?? 0;
    if (admitted >= caps.pairCapWeek) continue;
    pairWeeks.set(pairWeek, admitted + 1);
    result.push({
      citingAgentId: row.citingAgentId,
      citedAgentId: row.citedAgentId,
      questionId: row.questionId,
      week,
      contribution: row.finalEdge > 0 ? 0.5 * row.finalEdge : 0,
    });
  }
  return result;
}

// Errors compare by class and message, so refusals must stay identical too.
function outcomeOf(run: () => LiftResult[]): LiftResult[] | string {
  try {
    return run();
  } catch (error) {
    return `${(error as Error).constructor.name}: ${(error as Error).message}`;
  }
}
function expectFrozen(rows: readonly CitationRow[], caps: LiftCaps): void {
  for (const input of [rows, [...rows].reverse()])
    expect(outcomeOf(() => liftContributions(input, caps))).toEqual(
      outcomeOf(() => referenceLiftContributions(input, caps)),
    );
}

// Deterministic generator (mulberry32) so a failing seed reproduces exactly.
function generator(seed: number): () => number {
  let state = seed >>> 0;
  return () => {
    state = (state + 0x6d2b79f5) >>> 0;
    let t = state;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// frozen pre-1.2.0 oracle (D-18): the SCORING_VERSION 1.1.0 market pin (scoring.ts:112-158),
// `latest ?? fallback`, returning the chosen snapshot. Never edit it to match new code.
function referenceMarketPin(
  openAt: Date,
  submittedAt: Date,
  snapshots: readonly MarketSnapshot[],
): MarketSnapshot | undefined {
  const opened = timestamp(openAt);
  const submitted = timestamp(submittedAt);
  if (submitted < opened) throw new RangeError("submission precedes open");
  const seen = new Set<string>();
  let latest: MarketSnapshot | undefined;
  for (const snapshot of snapshots) {
    identifier(snapshot.snapshotId);
    if (seen.has(snapshot.snapshotId)) throw new TypeError("duplicate snapshot ID");
    seen.add(snapshot.snapshotId);
    const taken = timestamp(snapshot.takenAt);
    finite(snapshot.p, "probability");
    if (snapshot.p < 0 || snapshot.p > 1) throw new RangeError("probability must be in [0,1]");
    if (
      taken <= submitted &&
      (latest === undefined ||
        taken > latest.takenAt.getTime() ||
        (taken === latest.takenAt.getTime() && snapshot.snapshotId < latest.snapshotId))
    )
      latest = snapshot;
  }
  let fallback: MarketSnapshot | undefined;
  for (const snapshot of snapshots) {
    const taken = snapshot.takenAt.getTime();
    if (
      taken > opened &&
      (fallback === undefined ||
        taken < fallback.takenAt.getTime() ||
        (taken === fallback.takenAt.getTime() && snapshot.snapshotId < fallback.snapshotId))
    )
      fallback = snapshot;
  }
  return latest ?? fallback;
}

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
  it("liftContributions equals the frozen pre-change output on generated graphs", () => {
    const hour = 3_600_000;
    const week = 7 * 24 * hour;
    const start = Date.parse("2026-01-05T00:00:00Z"); // a Monday
    // Sunday 23:59:59.999 and Monday 00:00:00.000 on both inner week boundaries.
    const boundaries = [start + week - 1, start + week, start + 2 * week - 1, start + 2 * week];
    const cited = [
      { agent: "t0", operator: "op-t0" },
      { agent: "t1", operator: "op-t1" },
    ];
    // c2 shares t0's operator; t1 cites as itself.
    const citing = [
      { agent: "c0", operator: "op-c0" },
      { agent: "c1", operator: "op-c1" },
      { agent: "c2", operator: "op-t0" },
      { agent: "t1", operator: "op-t1" },
    ];
    const statuses = new Set<string>();
    for (let seed = 0; seed < 40; seed++) {
      const random = generator(seed + 1);
      const pick = <T>(values: readonly T[]): T => values[Math.floor(random() * values.length)]!;
      const rows: CitationRow[] = [];
      while (rows.length < 60) {
        const from = pick(citing);
        const to = pick(cited);
        const questionId = `q${rows.length}`;
        const hours = Math.floor(random() * 21 * 24);
        const submitted = random() < 0.25 ? pick(boundaries) : start + hours * hour;
        const late = random();
        const published = late < 0.15 ? submitted + 1 : late < 0.3 ? submitted : submitted - hour;
        const base: CitationRow = {
          rationaleId: `r${rows.length}`,
          rationaleQuestionId: random() < 0.1 ? questionId : "old",
          questionId,
          citingAgentId: from.agent,
          citedAgentId: to.agent,
          citingOperatorId: from.operator,
          citedOperatorId: to.operator,
          submittedAt: new Date(submitted),
          publicAt: new Date(published),
          finalEdge: (Math.floor(random() * 11) - 5) / 10,
        };
        rows.push(base);
        // Duplicate key with another rationale, sometimes still unpublished.
        if (random() < 0.2 && rows.length < 60)
          rows.push({
            ...base,
            rationaleId: `${base.rationaleId}-again`,
            publicAt: new Date(random() < 0.3 ? submitted + 1 : submitted - 2 * hour),
          });
      }
      for (const pairCapWeek of [0, 1, 3]) {
        const caps = { pairCapWeek };
        expectFrozen(rows, caps);
        const ledger = liftLedger(rows, caps);
        const byStatus = LIFT_STATUSES.map((s) => ledger.filter((e) => e.status === s).length);
        expect(byStatus.reduce((a, b) => a + b, 0)).toBe(rows.length);
        for (const entry of ledger) statuses.add(entry.status);
      }
    }
    // The generator is not vacuous: every core status occurs somewhere.
    expect([...statuses].sort()).toEqual([...LIFT_STATUSES].sort());
  });
  it("liftContributions equals the frozen pre-change output on the lift.test.ts fixtures", () => {
    // Copied inputs from lift.test.ts (never imported from a test file).
    const monday = Date.parse("2025-12-29T00:00:00Z");
    const week = 7 * 86_400_000;
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
    const original = row("q");
    const sets: CitationRow[][] = [
      [row("q1", 1, -0.1), row("q2", 2, 0), row("q3", 3, 0.4), row("q4", 4, 0.8)],
      [{ ...original, citedAgentId: "B" }],
      [{ ...original, citedOperatorId: "op-B" }],
      [{ ...original, publicAt: new Date(monday + 1) }],
      [{ ...original, rationaleQuestionId: "q" }],
      [{ ...original, publicAt: original.submittedAt }],
      [original, { ...original, rationaleId: "second" }],
      [original, { ...original, finalEdge: 0.3 }],
      [original, { ...original, submittedAt: new Date(monday + 1) }],
      [original, { ...original, citingOperatorId: "different" }],
      [original, { ...original, citedOperatorId: "different" }],
      [{ ...original, publicAt: new Date(monday + 1) }, original],
      [
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
      ],
      [row("sun", -1)],
      [row("z"), row("a"), row("b"), row("c")],
      ...[
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
      ].map((change) => [{ ...row("q"), ...change }]),
    ];
    for (const rows of sets) for (const pairCapWeek of [0, 3]) expectFrozen(rows, { pairCapWeek });
    for (const pairCapWeek of [-1, 0.5, Infinity]) expectFrozen([], { pairCapWeek });
  });
  it("shrunkTrack ends at shrunkMean bit-for-bit and is a prefix shrunk mean", () => {
    let arrays = 0;
    for (let seed = 0; seed < 200; seed++) {
      const length = (seed * 53) % 121;
      // Thirds and sevenths of 21 keep the sums inexact in binary floating point.
      const values = Array.from({ length }, (_, i) => (((i * 37 + seed * 11) % 43) - 21) / 21);
      for (const k of [0, 2, 5, 10, 20]) {
        const track = shrunkTrack(values, k);
        expect(track.length).toBe(values.length);
        expect(Object.is(track.at(-1) ?? 0, shrunkMean(values, k))).toBe(true);
        for (let i = 0; i < track.length; i++)
          expect(Object.is(track[i], shrunkMean(values.slice(0, i + 1), k))).toBe(true);
      }
      arrays++;
    }
    expect(arrays).toBeGreaterThanOrEqual(200);
    expect(shrunkTrack([], 20)).toEqual([]);
    expect(() => shrunkTrack([0.1], -1)).toThrow(RangeError);
    expect(() => shrunkTrack([0.1, Infinity], 2)).toThrow(RangeError);
    expect(() => shrunkTrack([0.1, NaN], 2)).toThrow(RangeError);
  });
  it("D-18: the 1.2.0 market pin is the 1.1.0 pin when fresh, else null", () => {
    // Independent copy of the D-18 bounds (seconds), never imported from the code under test.
    const bounds: Record<Horizon, number> = {
      hour: 120,
      day: 600,
      week: 1800,
      month: 7200,
      long: 7200,
    };
    const horizons = Object.keys(bounds) as Horizon[];
    const outcomes = { fresh: 0, stale: 0, none: 0 };
    for (let seed = 0; seed < 300; seed++) {
      const random = generator(seed + 1000);
      const horizon = horizons[seed % horizons.length]!;
      const b = bounds[horizon] * 1000;
      const submitted = 10_000_000_000;
      const opened = submitted - Math.floor(random() * 4 * b);
      const snapshots: MarketSnapshot[] = [];
      const n = Math.floor(random() * 7);
      for (let i = 0; i < n; i++) {
        const shape = random();
        // Exact edges (±b, ±(b + 1)) often, else anywhere within ±3 bounds; sometimes a tie.
        const offset =
          shape < 0.1
            ? -b
            : shape < 0.2
              ? -b - 1
              : shape < 0.3
                ? b
                : shape < 0.4
                  ? b + 1
                  : shape < 0.5 && snapshots.length > 0
                    ? snapshots[snapshots.length - 1]!.takenAt.getTime() - submitted
                    : Math.floor(random() * 6 * b) - 3 * b;
        snapshots.push({
          snapshotId: `${Math.floor(random() * 1e6).toString(36)}-${i}`,
          takenAt: new Date(submitted + offset),
          p: Math.floor(random() * 1001) / 1000,
        });
      }
      const openAt = new Date(opened);
      const submittedAt = new Date(submitted);
      const oracle = referenceMarketPin(openAt, submittedAt, snapshots);
      const actual = selectBaseline({ kind: "market", horizon, openAt, submittedAt, snapshots });
      if (oracle === undefined) {
        outcomes.none++;
        expect(actual).toBeNull();
      } else if (Math.abs(submitted - oracle.takenAt.getTime()) <= b) {
        outcomes.fresh++;
        expect(actual).toEqual({ kind: "market", p: oracle.p, snapshotId: oracle.snapshotId });
      } else {
        outcomes.stale++;
        expect(actual).toBeNull();
      }
    }
    // The generator is not vacuous: fresh, stale and absent pins all occur.
    expect(outcomes.fresh).toBeGreaterThan(0);
    expect(outcomes.stale).toBeGreaterThan(0);
    expect(outcomes.none).toBeGreaterThan(0);
  });
});
