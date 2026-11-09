import { count, finite, identifier, timestamp } from "./scoring.js";

export const DEFAULT_LIFT_PAIR_CAP_WEEK = 3;
export const LIFT_SHRINK_K = 10;
export interface CitationRow {
  readonly rationaleId: string;
  readonly rationaleQuestionId: string;
  readonly questionId: string;
  readonly citingAgentId: string;
  readonly citedAgentId: string;
  readonly citingOperatorId: string;
  readonly citedOperatorId: string;
  readonly submittedAt: Date;
  readonly publicAt: Date;
  readonly finalEdge: number;
}
export type CitationGraphInput = readonly CitationRow[];
export interface LiftCaps {
  readonly pairCapWeek: number;
}
export interface LiftResult {
  citingAgentId: string;
  citedAgentId: string;
  questionId: string;
  /** ISO Monday date in UTC, not a locale- or wall-clock-dependent week. */
  week: string;
  contribution: number;
}

/** Caps count admitted questions including zero/negative Edge, never cherry-pick winners. */
export function liftContributions(input: CitationGraphInput, caps: LiftCaps): LiftResult[] {
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

/** nCitations counts admitted rows, including zero contributions, not citation attempts. */
export function aggregateLift(contributions: readonly LiftResult[]): {
  lift: number;
  nCitations: number;
  shrunkLift: number;
} {
  let lift = 0;
  const seen = new Set<string>();
  for (const row of contributions) {
    identifier(row.citingAgentId);
    identifier(row.citedAgentId);
    identifier(row.questionId);
    finite(row.contribution, "contribution");
    if (row.contribution < 0) throw new RangeError("contribution must be nonnegative");
    if (typeof row.week !== "string" || !/^(?:\d{4}|[+-]\d{6})-\d{2}-\d{2}$/.test(row.week))
      throw new TypeError("invalid UTC week");
    const week = new Date(`${row.week}T00:00:00.000Z`);
    timestamp(week);
    if (week.getUTCDay() !== 1 || week.toISOString().split("T")[0] !== row.week)
      throw new RangeError("week must be a Monday UTC date");
    const key = JSON.stringify([row.citingAgentId, row.citedAgentId, row.questionId]);
    if (seen.has(key)) throw new TypeError("duplicate admitted citation");
    seen.add(key);
    lift += row.contribution;
    finite(lift, "Lift sum");
  }
  return {
    lift,
    nCitations: contributions.length,
    shrunkLift: lift / (contributions.length + LIFT_SHRINK_K),
  };
}
