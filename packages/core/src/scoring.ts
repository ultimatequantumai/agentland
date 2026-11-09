import type { Horizon } from "./domain.js";

/**
 * Formula changes bump the minor version, are announced one season ahead, and never rescore frozen seasons.
 * 1.1.0 adds the D-03 Metaculus community baseline and excludes house finals from the crowd (D-09).
 * 1.2.0 (D-18) requires the market and community pin to be fresh at submission: within twice the horizon's snapshot cadence, else unavailable.
 */
export const SCORING_VERSION = "1.2.0";
export const DEFAULT_SHRINK_K = 20;
export const DEFAULT_MIN_RESOLVED_FOR_RANK = 30;
export const DEFAULT_RELIABILITY_BINS = 10;
export const MIN_CROWD_OTHER_AGENTS = 5;
export type Outcome = 0 | 1;
export interface Forecast {
  readonly p: number;
  readonly o: Outcome;
}
export interface ReliabilityBin {
  lower: number;
  upper: number;
  count: number;
  meanProbability: number | null;
  observedFrequency: number | null;
}

// Shared internal input checks; index.ts exposes only domain APIs.
export function finite(value: number, name: string): void {
  if (typeof value !== "number") throw new TypeError(`${name} must be a number`);
  if (!Number.isFinite(value)) throw new RangeError(`${name} must be finite`);
}
export function probability(value: number, name = "probability"): void {
  finite(value, name);
  if (value < 0 || value > 1) throw new RangeError(`${name} must be in [0,1]`);
}
export function outcome(value: Outcome): void {
  if (value !== 0 && value !== 1) throw new RangeError("outcome must be 0 or 1");
}
export function count(value: number, name: string): void {
  if (!Number.isSafeInteger(value) || value < 0)
    throw new RangeError(`${name} must be a nonnegative safe integer`);
}
export function identifier(value: string): void {
  if (typeof value !== "string" || value.trim().length === 0)
    throw new TypeError("identifier must be nonempty text");
}
export function timestamp(value: Date): number {
  if (!(value instanceof Date)) throw new TypeError("timestamp must be a Date");
  const ms = value.getTime();
  if (!Number.isFinite(ms)) throw new RangeError("invalid timestamp");
  return ms;
}

/** Clipping preserves the founding formula; reports in either clipped tail are equivalent. */
export function clip(p: number): number {
  probability(p);
  return Math.max(0.001, Math.min(0.999, p));
}
export function brier(p: number, o: Outcome): number {
  outcome(o);
  return (clip(p) - o) ** 2;
}
export function logScore(p: number, o: Outcome): number {
  outcome(o);
  const clipped = clip(p);
  return Math.log(o === 1 ? clipped : 1 - clipped);
}
export function edge(p: number, baseline: number, o: Outcome): number {
  return brier(baseline, o) - brier(p, o);
}
export function shrunkMean(values: readonly number[], k: number): number {
  finite(k, "shrink k");
  if (k < 0) throw new RangeError("shrink k must be nonnegative");
  let sum = 0;
  for (const value of values) {
    finite(value, "value");
    sum += value;
    finite(sum, "sum");
  }
  return values.length === 0 ? 0 : sum / (values.length + k);
}
/**
 * The race track (Seasons P7, E-18): entry i is the shrunk mean of the first i + 1 values. Its last
 * point equals shrunkMean bit-for-bit only when the caller passes values in the rank job's
 * (resolved_at, forecast_id) order.
 */
export function shrunkTrack(values: readonly number[], k: number): number[] {
  finite(k, "shrink k");
  if (k < 0) throw new RangeError("shrink k must be nonnegative");
  const track: number[] = [];
  let sum = 0;
  for (const [i, value] of values.entries()) {
    finite(value, "value");
    sum += value;
    finite(sum, "sum");
    track.push(sum / (i + 1 + k));
  }
  return track;
}

export interface MarketSnapshot {
  readonly snapshotId: string;
  readonly takenAt: Date;
  readonly p: number;
}
export interface FinalProbability {
  readonly agentId: string;
  readonly p: number;
  readonly isHouse: boolean;
}
/** Twice the snapshot cadence; equal to job-metrics snapshot_stale_open_questions and 0019 agentland_baseline_pin. */
export const SNAPSHOT_FRESHNESS_SECONDS: Readonly<Record<Horizon, number>> = Object.freeze({
  hour: 120,
  day: 600,
  week: 1800,
  month: 7200,
  long: 7200,
});
function freshnessMs(horizon: Horizon): number {
  if (typeof horizon !== "string" || !Object.hasOwn(SNAPSHOT_FRESHNESS_SECONDS, horizon))
    throw new TypeError("unknown horizon");
  return SNAPSHOT_FRESHNESS_SECONDS[horizon] * 1000;
}
export type BaselineInput =
  | {
      readonly kind: "market";
      readonly horizon: Horizon;
      readonly openAt: Date;
      readonly submittedAt: Date;
      readonly snapshots: readonly MarketSnapshot[];
    }
  | {
      readonly kind: "non-market";
      readonly agentId: string;
      readonly finals: readonly FinalProbability[];
    }
  | {
      readonly kind: "community";
      readonly horizon: Horizon;
      readonly submittedAt: Date;
      readonly snapshots: readonly MarketSnapshot[];
      readonly agentId: string;
      readonly finals: readonly FinalProbability[];
    };
export type Baseline =
  | { kind: "market" | "community"; p: number; snapshotId: string }
  | { kind: "crowd" | "uniform"; p: number };

/** Validates every snapshot; the one owner of the at-or-before pin and its ascending-ID tie (the DB guard mirrors it). */
function latestAtOrBefore(
  snapshots: readonly MarketSnapshot[],
  submitted: number,
): MarketSnapshot | undefined {
  const seen = new Set<string>();
  let latest: MarketSnapshot | undefined;
  for (const snapshot of snapshots) {
    identifier(snapshot.snapshotId);
    if (seen.has(snapshot.snapshotId)) throw new TypeError("duplicate snapshot ID");
    seen.add(snapshot.snapshotId);
    const taken = timestamp(snapshot.takenAt);
    probability(snapshot.p);
    if (
      taken <= submitted &&
      (latest === undefined ||
        taken > latest.takenAt.getTime() ||
        (taken === latest.takenAt.getTime() && snapshot.snapshotId < latest.snapshotId))
    )
      latest = snapshot;
  }
  return latest;
}

/** Caller supplies already-eligible finals. Missing or stale market data stays missing, never a synthetic baseline. */
export function selectBaseline(input: BaselineInput): Baseline | null {
  if (input.kind === "market") {
    const bound = freshnessMs(input.horizon);
    const opened = timestamp(input.openAt);
    const submitted = timestamp(input.submittedAt);
    if (submitted < opened) throw new RangeError("submission precedes open");
    const latest = latestAtOrBefore(input.snapshots, submitted);
    // D-18: a stale latest never falls through to a later snapshot.
    if (latest !== undefined)
      return submitted - latest.takenAt.getTime() <= bound
        ? { kind: "market", p: latest.p, snapshotId: latest.snapshotId }
        : null;
    let fallback: MarketSnapshot | undefined;
    for (const snapshot of input.snapshots) {
      const taken = snapshot.takenAt.getTime();
      if (
        taken > opened &&
        (fallback === undefined ||
          taken < fallback.takenAt.getTime() ||
          (taken === fallback.takenAt.getTime() && snapshot.snapshotId < fallback.snapshotId))
      )
        fallback = snapshot;
    }
    return fallback !== undefined && fallback.takenAt.getTime() - submitted <= bound
      ? { kind: "market", p: fallback.p, snapshotId: fallback.snapshotId }
      : null;
  }
  if (input.kind === "community") {
    const bound = freshnessMs(input.horizon);
    const submitted = timestamp(input.submittedAt);
    identifier(input.agentId);
    const latest = latestAtOrBefore(input.snapshots, submitted);
    // D-03: community → crowd → uniform; a snapshot taken after submission is hindsight, never
    // used, and a stale one (D-18) counts as absent.
    return latest === undefined || submitted - latest.takenAt.getTime() > bound
      ? selectBaseline({ kind: "non-market", agentId: input.agentId, finals: input.finals })
      : { kind: "community", p: latest.p, snapshotId: latest.snapshotId };
  }
  if (input.kind !== "non-market") throw new TypeError("unknown baseline kind");
  identifier(input.agentId);
  const seen = new Set<string>();
  let sum = 0;
  let n = 0;
  for (const final of input.finals) {
    identifier(final.agentId);
    probability(final.p);
    if (typeof final.isHouse !== "boolean") throw new TypeError("isHouse must be a boolean");
    if (seen.has(final.agentId)) throw new TypeError("duplicate final agent");
    seen.add(final.agentId);
    // D-09: house baselines are scored but never form the crowd (mean or quorum).
    if (final.agentId !== input.agentId && !final.isHouse) {
      sum += final.p;
      n++;
    }
  }
  return n >= MIN_CROWD_OTHER_AGENTS ? { kind: "crowd", p: sum / n } : { kind: "uniform", p: 0.5 };
}

/** Raw, not clipped, submitted probabilities define the reliability diagram. */
export function reliability(
  forecasts: readonly Forecast[],
  bins = DEFAULT_RELIABILITY_BINS,
): ReliabilityBin[] {
  count(bins, "bins");
  if (bins === 0) throw new RangeError("bins must be positive");
  const result: ReliabilityBin[] = Array.from({ length: bins }, (_, i) => ({
    lower: i / bins,
    upper: (i + 1) / bins,
    count: 0,
    meanProbability: null,
    observedFrequency: null,
  }));
  for (const forecast of forecasts) {
    probability(forecast.p);
    outcome(forecast.o);
    const bin = result[Math.min(bins - 1, Math.floor(forecast.p * bins))]!;
    bin.count++;
    bin.meanProbability = (bin.meanProbability ?? 0) + forecast.p;
    bin.observedFrequency = (bin.observedFrequency ?? 0) + forecast.o;
  }
  for (const bin of result) {
    if (bin.count > 0) {
      bin.meanProbability = bin.meanProbability! / bin.count;
      bin.observedFrequency = bin.observedFrequency! / bin.count;
    }
  }
  return result;
}
export function ece(bins: readonly ReliabilityBin[], n: number): number {
  count(n, "sample count");
  let total = 0;
  let weightedError = 0;
  for (const bin of bins) {
    count(bin.count, "bin count");
    probability(bin.lower, "bin lower");
    probability(bin.upper, "bin upper");
    if (bin.lower >= bin.upper) throw new RangeError("invalid bin bounds");
    total += bin.count;
    count(total, "total count");
    if (bin.count === 0) {
      if (bin.meanProbability !== null || bin.observedFrequency !== null)
        throw new TypeError("empty bins require null statistics");
    } else {
      if (bin.meanProbability === null || bin.observedFrequency === null)
        throw new TypeError("nonempty bins require statistics");
      probability(bin.meanProbability, "bin mean");
      probability(bin.observedFrequency, "bin frequency");
      weightedError += bin.count * Math.abs(bin.meanProbability - bin.observedFrequency);
    }
  }
  if (total !== n) throw new RangeError("ECE denominator must equal bin counts");
  return n === 0 ? 0 : weightedError / n;
}
/**
 * C-10: the count-weighted merge of reliability diagrams used for the whole-record mark. Counts
 * add; mean and frequency are count-weighted; empty bins stay null. Inputs are never mutated.
 */
export function mergeReliability(
  binSets: readonly (readonly ReliabilityBin[])[],
): ReliabilityBin[] {
  const first = binSets[0];
  if (first === undefined) return [];
  const merged = first.map((bin) => ({ lower: bin.lower, upper: bin.upper, count: 0, p: 0, o: 0 }));
  for (const bins of binSets) {
    if (bins.length !== merged.length) throw new RangeError("bin sets differ in length");
    for (const [i, bin] of bins.entries()) {
      const target = merged[i]!;
      if (bin.lower !== target.lower || bin.upper !== target.upper)
        throw new RangeError("bin sets differ in bounds");
      count(bin.count, "bin count");
      if (bin.count === 0) continue;
      if (bin.meanProbability === null || bin.observedFrequency === null)
        throw new TypeError("nonempty bins require statistics");
      target.count += bin.count;
      count(target.count, "total count");
      target.p += bin.count * bin.meanProbability;
      target.o += bin.count * bin.observedFrequency;
    }
  }
  return merged.map(({ lower, upper, count: n, p, o }) => ({
    lower,
    upper,
    count: n,
    meanProbability: n === 0 ? null : p / n,
    observedFrequency: n === 0 ? null : o / n,
  }));
}
export function sharpness(probabilities: readonly number[]): number {
  let sum = 0;
  for (const p of probabilities) {
    probability(p);
    sum += Math.abs(p - 0.5);
  }
  return probabilities.length === 0 ? 0 : sum / probabilities.length;
}
