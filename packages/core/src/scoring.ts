/** Formula changes bump the minor version, are announced one season ahead, and never rescore frozen seasons. */
export const SCORING_VERSION = "1.0.0";
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

export interface MarketSnapshot {
  readonly snapshotId: string;
  readonly takenAt: Date;
  readonly p: number;
}
export interface FinalProbability {
  readonly agentId: string;
  readonly p: number;
}
export type BaselineInput =
  | {
      readonly kind: "market";
      readonly openAt: Date;
      readonly submittedAt: Date;
      readonly snapshots: readonly MarketSnapshot[];
    }
  | {
      readonly kind: "non-market";
      readonly agentId: string;
      readonly finals: readonly FinalProbability[];
    };
export type Baseline =
  { kind: "market"; p: number; snapshotId: string } | { kind: "crowd" | "uniform"; p: number };

/** Caller supplies already-eligible finals. Missing market data stays missing, never a synthetic baseline. */
export function selectBaseline(input: BaselineInput): Baseline | null {
  if (input.kind === "market") {
    const opened = timestamp(input.openAt);
    const submitted = timestamp(input.submittedAt);
    if (submitted < opened) throw new RangeError("submission precedes open");
    const seen = new Set<string>();
    let latest: MarketSnapshot | undefined;
    let fallback: MarketSnapshot | undefined;
    for (const snapshot of input.snapshots) {
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
      if (
        taken > opened &&
        (fallback === undefined ||
          taken < fallback.takenAt.getTime() ||
          (taken === fallback.takenAt.getTime() && snapshot.snapshotId < fallback.snapshotId))
      )
        fallback = snapshot;
    }
    const selected = latest ?? fallback;
    return selected === undefined
      ? null
      : { kind: "market", p: selected.p, snapshotId: selected.snapshotId };
  }
  if (input.kind !== "non-market") throw new TypeError("unknown baseline kind");
  identifier(input.agentId);
  const seen = new Set<string>();
  let sum = 0;
  let n = 0;
  for (const final of input.finals) {
    identifier(final.agentId);
    probability(final.p);
    if (seen.has(final.agentId)) throw new TypeError("duplicate final agent");
    seen.add(final.agentId);
    if (final.agentId !== input.agentId) {
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
export function sharpness(probabilities: readonly number[]): number {
  let sum = 0;
  for (const p of probabilities) {
    probability(p);
    sum += Math.abs(p - 0.5);
  }
  return probabilities.length === 0 ? 0 : sum / probabilities.length;
}
