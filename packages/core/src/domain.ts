import {
  DEFAULT_MIN_RESOLVED_FOR_RANK,
  DEFAULT_SHRINK_K,
  count,
  finite,
  identifier,
  probability,
  shrunkMean,
  timestamp,
} from "./scoring.js";

export const HORIZONS = ["hour", "day", "week", "month", "long"] as const;
export type Horizon = (typeof HORIZONS)[number];
export const TOPICS = [
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
] as const;
export type Topic = (typeof TOPICS)[number];
export interface QuestionClassification {
  topic: Topic;
  tags?: string[];
}
export function isTopic(value: unknown): value is Topic {
  return typeof value === "string" && TOPICS.some((topic) => topic === value);
}
export function horizonFor(openAt: Date, expectedResolveAt: Date): Horizon {
  const duration = timestamp(expectedResolveAt) - timestamp(openAt);
  if (duration < 0) throw new RangeError("resolution precedes open");
  if (duration <= 2 * 3_600_000) return "hour";
  if (duration <= 36 * 3_600_000) return "day";
  if (duration <= 10 * 86_400_000) return "week";
  if (duration <= 45 * 86_400_000) return "month";
  return "long";
}
// D-01: contiguous 28-day windows anchored on Monday 00:00 UTC.
const SEASON_MS = 28 * 86_400_000;
export function isSeasonAnchor(at: Date): boolean {
  const ms = timestamp(at);
  return ms % 86_400_000 === 0 && new Date(ms).getUTCDay() === 1;
}
export function nextSeasonWindow(prevEndsAt: Date): { startsAt: Date; endsAt: Date } {
  const ms = timestamp(prevEndsAt);
  return { startsAt: new Date(ms), endsAt: new Date(ms + SEASON_MS) };
}
export interface SeasonParameters {
  shrinkK?: number;
  minResolvedForRank?: number;
}
export interface SeasonAggregate {
  nResolved: number;
  meanEdge: number | null;
  shrunkEdge: number;
  ranked: boolean;
  shrinkK: number;
  minResolvedForRank: number;
}
/** Overall and explicitly first-season rookie membership use this same metric. */
export function aggregateSeason(
  edges: readonly number[],
  parameters: SeasonParameters = {},
): SeasonAggregate {
  const shrinkK = parameters.shrinkK ?? DEFAULT_SHRINK_K;
  const minResolvedForRank = parameters.minResolvedForRank ?? DEFAULT_MIN_RESOLVED_FOR_RANK;
  count(minResolvedForRank, "rank threshold");
  if (minResolvedForRank === 0) throw new RangeError("rank threshold must be positive");
  const shrunkEdge = shrunkMean(edges, shrinkK);
  return {
    nResolved: edges.length,
    meanEdge: edges.length === 0 ? null : shrunkMean(edges, 0),
    shrunkEdge,
    ranked: edges.length >= minResolvedForRank,
    shrinkK,
    minResolvedForRank,
  };
}
export interface DivisionRow {
  readonly horizon: Horizon;
  readonly topic: Topic;
  readonly edge: number;
}
export type DivisionSelector =
  | { readonly horizon: Horizon; readonly topic?: never }
  | { readonly topic: Topic; readonly horizon?: never };
/** Share refers to ALL season questions. Nonnegative Math.round gives explicit half-up scaling. */
export function aggregateDivision(
  rows: readonly DivisionRow[],
  selector: DivisionSelector,
  share: number,
  parameters: SeasonParameters = {},
): SeasonAggregate {
  probability(share, "division share");
  const season = aggregateSeason([], parameters);
  if (selector.horizon !== undefined) {
    if (!HORIZONS.some((horizon) => horizon === selector.horizon) || selector.topic !== undefined)
      throw new TypeError("invalid horizon selector");
  } else if (!isTopic(selector.topic)) throw new TypeError("invalid topic selector");
  const edges: number[] = [];
  for (const row of rows) {
    finite(row.edge, "edge");
    if (!HORIZONS.some((horizon) => horizon === row.horizon) || !isTopic(row.topic))
      throw new TypeError("invalid division row");
    if (
      selector.horizon !== undefined
        ? row.horizon === selector.horizon
        : row.topic === selector.topic
    )
      edges.push(row.edge);
  }
  const result = aggregateSeason(edges, {
    shrinkK: Math.max(5, Math.round(season.shrinkK * share)),
    minResolvedForRank: Math.max(1, Math.round(season.minResolvedForRank * share)),
  });
  if (share === 0) result.ranked = false;
  return result;
}
export function formatProbability(p: number): string {
  probability(p);
  return `${(p * 100).toFixed(1)}%`;
}
/** Pass shrunkEdge for season/division totals, never a cumulative sum. */
export function formatEdgePoints(value: number): string {
  finite(value, "edge");
  const points = value * 100;
  finite(points, "edge points");
  const rounded = points.toFixed(1);
  return `${Number(rounded) === 0 ? "+0.0" : points > 0 ? `+${rounded}` : rounded} pts`;
}
export interface ResolvedEdge {
  readonly forecastId: string;
  readonly resolvedAt: Date;
  readonly edge: number;
}
export function edgeStreak(rows: readonly ResolvedEdge[]): { current: number; longest: number } {
  const seen = new Set<string>();
  for (const row of rows) {
    identifier(row.forecastId);
    if (seen.has(row.forecastId)) throw new TypeError("duplicate forecast ID");
    seen.add(row.forecastId);
    timestamp(row.resolvedAt);
    finite(row.edge, "edge");
  }
  const ordered = [...rows].sort(
    (a, b) =>
      a.resolvedAt.getTime() - b.resolvedAt.getTime() ||
      (a.forecastId < b.forecastId ? -1 : a.forecastId > b.forecastId ? 1 : 0),
  );
  let current = 0;
  let longest = 0;
  for (const row of ordered) {
    current = row.edge > 0 ? current + 1 : 0;
    longest = Math.max(longest, current);
  }
  return { current, longest };
}
export type Badge = "Calibrated" | "Market Beater" | "Teacher" | "Ironclad";
export interface LiftStanding {
  readonly agentId: string;
  readonly lift: number;
}
export interface BadgeInput {
  readonly calibrationCount: number;
  readonly calibrationEce: number | null;
  readonly seasonShrunkEdge: number;
  readonly seasonResolved: number;
  readonly allTimeResolved: number;
  readonly agentId: string;
  readonly liftStandings: readonly LiftStanding[];
}
/** Display only. Teacher uses raw Lift, ordinal ties by agent ID, ceil(10% of population). */
export function badges(input: BadgeInput): Badge[] {
  count(input.calibrationCount, "calibration count");
  count(input.seasonResolved, "season resolved");
  count(input.allTimeResolved, "all-time resolved");
  if (
    input.seasonResolved > input.allTimeResolved ||
    input.calibrationCount > input.allTimeResolved
  )
    throw new RangeError("component count exceeds all-time count");
  if (input.calibrationEce !== null) probability(input.calibrationEce, "ECE");
  finite(input.seasonShrunkEdge, "season Edge");
  identifier(input.agentId);
  const seen = new Set<string>();
  for (const standing of input.liftStandings) {
    identifier(standing.agentId);
    if (seen.has(standing.agentId)) throw new TypeError("duplicate Lift standing");
    seen.add(standing.agentId);
    finite(standing.lift, "Lift");
    if (standing.lift < 0) throw new RangeError("Lift must be nonnegative");
  }
  const standings = [...input.liftStandings].sort(
    (a, b) => b.lift - a.lift || (a.agentId < b.agentId ? -1 : a.agentId > b.agentId ? 1 : 0),
  );
  const rank = standings.findIndex((standing) => standing.agentId === input.agentId);
  const result: Badge[] = [];
  if (input.calibrationCount >= 100 && input.calibrationEce !== null && input.calibrationEce < 0.05)
    result.push("Calibrated");
  if (input.seasonResolved >= 200 && input.seasonShrunkEdge > 0.01) result.push("Market Beater");
  if (rank >= 0 && rank < Math.ceil(standings.length * 0.1)) result.push("Teacher");
  if (input.allTimeResolved >= 1000) result.push("Ironclad");
  return result;
}
