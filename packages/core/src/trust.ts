import { count, ece, identifier, outcome, probability, reliability, timestamp } from "./scoring.js";
import type { Forecast } from "./scoring.js";

/** Diagnostic-only formula; version independently of Edge and expose every raw component. */
export const TRUST_VERSION = "1.0.0";
export interface TrustComponents {
  calibration_score: number;
  consistency: number;
  tenure: number;
  honor: number;
  incidents: number;
}
export const TRUST_WEIGHTS: Readonly<TrustComponents> = Object.freeze({
  calibration_score: 0.2,
  consistency: 0.2,
  tenure: 0.2,
  honor: 0.2,
  incidents: 0.2,
});
export interface Clock {
  now(): Date;
}
export interface ResolvedForecast extends Forecast {
  readonly forecastId: string;
  readonly resolvedAt: Date;
}
export interface TrustInput {
  readonly clock: Clock;
  readonly resolved: readonly ResolvedForecast[];
  readonly seasonRankPercentiles: readonly number[];
  readonly seasonsPlayed: number;
  readonly upheldHonorViolationTimes: readonly Date[];
  readonly publicSuspensions: number;
  readonly upheldConductDisputes: number;
}
export function trustScore(input: TrustInput): { score: number; components: TrustComponents } {
  const now = timestamp(input.clock.now());
  count(input.seasonsPlayed, "seasons played");
  count(input.publicSuspensions, "public suspensions");
  count(input.upheldConductDisputes, "upheld conduct disputes");
  const incidents = input.publicSuspensions + input.upheldConductDisputes;
  count(incidents, "incidents");
  const seen = new Set<string>();
  for (const forecast of input.resolved) {
    identifier(forecast.forecastId);
    if (seen.has(forecast.forecastId)) throw new TypeError("duplicate resolved forecast");
    seen.add(forecast.forecastId);
    probability(forecast.p);
    outcome(forecast.o);
    if (timestamp(forecast.resolvedAt) > now) throw new RangeError("future resolution");
  }
  const latest = [...input.resolved]
    .sort(
      (a, b) =>
        b.resolvedAt.getTime() - a.resolvedAt.getTime() ||
        (a.forecastId < b.forecastId ? -1 : a.forecastId > b.forecastId ? 1 : 0),
    )
    .slice(0, 500);
  const calibration_score = latest.length < 30 ? 0 : 1 - ece(reliability(latest), latest.length);
  let rankSum = 0;
  for (const percentile of input.seasonRankPercentiles) {
    probability(percentile, "rank percentile");
    rankSum += percentile;
  }
  const n = input.seasonRankPercentiles.length;
  let consistency = 0;
  if (n > 0) {
    const mean = rankSum / n;
    let squaredDeviation = 0;
    for (const percentile of input.seasonRankPercentiles)
      squaredDeviation += (percentile - mean) ** 2;
    consistency = 1 - squaredDeviation / n;
  }
  let honorPenalty = 0;
  for (const violation of input.upheldHonorViolationTimes) {
    const occurred = timestamp(violation);
    if (occurred > now) throw new RangeError("future honor violation");
    const ageDays = (now - occurred) / 86_400_000;
    honorPenalty += 2 ** (-ageDays / 90);
  }
  const components: TrustComponents = {
    calibration_score,
    consistency,
    tenure: Math.min(1, input.seasonsPlayed / 6),
    honor: Math.max(0, 1 - honorPenalty),
    incidents,
  };
  const score =
    TRUST_WEIGHTS.calibration_score * components.calibration_score +
    TRUST_WEIGHTS.consistency * components.consistency +
    TRUST_WEIGHTS.tenure * components.tenure +
    TRUST_WEIGHTS.honor * components.honor -
    TRUST_WEIGHTS.incidents * components.incidents;
  return { score, components };
}
