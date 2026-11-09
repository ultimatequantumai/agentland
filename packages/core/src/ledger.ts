import {
  aggregateDivision,
  aggregateSeason,
  edgeStreak,
  HORIZONS,
  isTopic,
  TOPICS,
} from "./domain.js";
import type { Horizon, Topic } from "./domain.js";
import { ece, finite, reliability, shrunkMean } from "./scoring.js";
import type { Outcome, ReliabilityBin } from "./scoring.js";

/** Stored per-forecast scores under the current scoring version; core only aggregates (D-01). */
export interface LedgerRow {
  readonly forecastId: string;
  readonly p: number;
  readonly outcome: Outcome;
  readonly brier: number;
  readonly log: number;
  readonly edge: number;
  readonly horizon: Horizon;
  readonly topic: Topic;
  readonly resolvedAt: Date;
}
export interface LedgerBucketStats {
  n_resolved: number;
  mean_brier: number | null;
  mean_log: number | null;
  mean_edge: number | null;
  shrunk_edge: number;
  ece: number;
}
export interface LedgerSummaryStats extends LedgerBucketStats {
  reliability_bins: ReliabilityBin[];
  by_horizon: Partial<Record<Horizon, LedgerBucketStats>>;
  by_topic: Partial<Record<Topic, LedgerBucketStats>>;
  streaks: { edge_streak: { current: number; longest: number } };
}
export interface LedgerParameters {
  readonly shrinkK: number;
  /** Division share of all questions in scope; required for every populated division. */
  readonly shares: {
    readonly horizon: Partial<Record<string, number>>;
    readonly topic: Partial<Record<string, number>>;
  };
}

function calibration(rows: readonly LedgerRow[]) {
  const bins = reliability(rows.map((row) => ({ p: row.p, o: row.outcome })));
  return { bins, ece: ece(bins, rows.length) };
}

function means(rows: readonly LedgerRow[]) {
  for (const row of rows) {
    finite(row.brier, "brier");
    finite(row.log, "log score");
  }
  return rows.length === 0
    ? { mean_brier: null, mean_log: null }
    : {
        mean_brier: shrunkMean(
          rows.map((row) => row.brier),
          0,
        ),
        mean_log: shrunkMean(
          rows.map((row) => row.log),
          0,
        ),
      };
}

/** docs/05 §3, §4, §7 composed from existing formulas; empty input follows docs/05:145-146. */
export function bucketStats(
  rows: readonly LedgerRow[],
  params: LedgerParameters,
): LedgerSummaryStats {
  finite(params.shrinkK, "shrink k");
  for (const row of rows)
    if (!HORIZONS.includes(row.horizon) || !isTopic(row.topic))
      throw new TypeError("invalid ledger row division");
  if (params.shrinkK <= 0) throw new RangeError("shrink k must be positive");
  const overall = aggregateSeason(
    rows.map((row) => row.edge),
    { shrinkK: params.shrinkK },
  );
  const { bins, ece: overallEce } = calibration(rows);
  const bucket = (
    subset: readonly LedgerRow[],
    selector: { horizon: Horizon } | { topic: Topic },
    share: number | undefined,
  ): LedgerBucketStats => {
    const division = aggregateDivision(subset, selector, share as number, {
      shrinkK: params.shrinkK,
    });
    return {
      n_resolved: division.nResolved,
      ...means(subset),
      mean_edge: division.meanEdge,
      shrunk_edge: division.shrunkEdge,
      ece: calibration(subset).ece,
    };
  };
  const by_horizon: Partial<Record<Horizon, LedgerBucketStats>> = {};
  for (const horizon of HORIZONS) {
    const subset = rows.filter((row) => row.horizon === horizon);
    if (subset.length > 0)
      by_horizon[horizon] = bucket(subset, { horizon }, params.shares.horizon[horizon]);
  }
  const by_topic: Partial<Record<Topic, LedgerBucketStats>> = {};
  for (const topic of TOPICS) {
    const subset = rows.filter((row) => row.topic === topic);
    if (subset.length > 0) by_topic[topic] = bucket(subset, { topic }, params.shares.topic[topic]);
  }
  return {
    n_resolved: overall.nResolved,
    ...means(rows),
    mean_edge: overall.meanEdge,
    shrunk_edge: overall.shrunkEdge,
    ece: overallEce,
    reliability_bins: bins,
    by_horizon,
    by_topic,
    streaks: { edge_streak: edgeStreak(rows) },
  };
}
