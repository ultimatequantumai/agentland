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

/** Every status, in a fixed public order; `other_league` is service-assigned (08-15), not core. */
export const LIFT_STATUSES = [
  "credited",
  "zero_edge",
  "pair_cap",
  "duplicate",
  "same_question",
  "self",
  "same_operator",
  "not_public",
] as const;
export type LiftStatus = (typeof LIFT_STATUSES)[number];
export interface LiftLedgerRow<R extends CitationRow = CitationRow> {
  row: R;
  status: LiftStatus;
  /** ISO Monday date in UTC of the citing submission. */
  week: string;
  contribution: number;
}

/**
 * C-05: every input row exactly once, in the order caps are applied, with the reason it was or
 * was not credited. Ineligible rows take the first failing rule: not_public, same_question, self,
 * same_operator (D-17, R-04). Operators are those the caller resolved at citing time
 * (`agentland_operator_at`, E-09). Ineligible rows never enter the duplicate set, so an
 * unpublished twin cannot hide the eligible rationale. Caps count admitted questions including
 * zero/negative Edge, never cherry-pick winners.
 */
export function liftLedger<R extends CitationRow>(
  input: readonly R[],
  caps: LiftCaps,
): LiftLedgerRow<R>[] {
  count(caps.pairCapWeek, "pair cap per week");
  const finals = new Map<string, CitationRow>();
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
    timestamp(row.publicAt);
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
  }
  const ordered = [...input].sort(
    (a, b) =>
      a.submittedAt.getTime() - b.submittedAt.getTime() ||
      (a.questionId < b.questionId ? -1 : a.questionId > b.questionId ? 1 : 0) ||
      (a.rationaleId < b.rationaleId ? -1 : a.rationaleId > b.rationaleId ? 1 : 0) ||
      (a.citingAgentId < b.citingAgentId ? -1 : a.citingAgentId > b.citingAgentId ? 1 : 0) ||
      (a.citedAgentId < b.citedAgentId ? -1 : a.citedAgentId > b.citedAgentId ? 1 : 0),
  );
  const seen = new Set<string>();
  const pairWeeks = new Map<string, number>();
  const ledger: LiftLedgerRow<R>[] = [];
  for (const row of ordered) {
    const monday = new Date(row.submittedAt.getTime());
    monday.setUTCHours(0, 0, 0, 0);
    monday.setUTCDate(monday.getUTCDate() - ((monday.getUTCDay() + 6) % 7));
    const week = monday.toISOString().split("T")[0]!;
    const status = ((): LiftStatus => {
      if (row.publicAt.getTime() > row.submittedAt.getTime()) return "not_public";
      if (row.rationaleQuestionId === row.questionId) return "same_question";
      if (row.citingAgentId === row.citedAgentId) return "self";
      if (row.citingOperatorId === row.citedOperatorId) return "same_operator";
      // The key is recorded before the cap check: a capped key still blocks a later twin.
      const finalKey = JSON.stringify([row.citingAgentId, row.citedAgentId, row.questionId]);
      if (seen.has(finalKey)) return "duplicate";
      seen.add(finalKey);
      const pairWeek = JSON.stringify([row.citingAgentId, row.citedAgentId, week]);
      const admitted = pairWeeks.get(pairWeek) ?? 0;
      if (admitted >= caps.pairCapWeek) return "pair_cap";
      pairWeeks.set(pairWeek, admitted + 1);
      return row.finalEdge > 0 ? "credited" : "zero_edge";
    })();
    ledger.push({
      row,
      status,
      week,
      contribution: status === "credited" ? 0.5 * row.finalEdge : 0,
    });
  }
  return ledger;
}

/**
 * The admitted rows of `liftLedger`. Output is byte-identical to the pre-Phase-8 function (frozen
 * oracle in properties.test.ts), so no SCORING_VERSION bump.
 */
export function liftContributions(input: CitationGraphInput, caps: LiftCaps): LiftResult[] {
  return liftLedger(input, caps)
    .filter((entry) => entry.status === "credited" || entry.status === "zero_edge")
    .map(({ row, week, contribution }) => ({
      citingAgentId: row.citingAgentId,
      citedAgentId: row.citedAgentId,
      questionId: row.questionId,
      week,
      contribution,
    }));
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
