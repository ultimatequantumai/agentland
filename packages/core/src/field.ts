import { MIN_CROWD_OTHER_AGENTS } from "./scoring.js";

/**
 * C1 — the pure Field frame codec shared by the service (ring writer and readers), packages/ui
 * (types only) and apps/web (client buffer). Frame v1 was frozen by 05-07. Every byte becomes
 * public, so a frame carries only whitelisted, agent-free fields before close (non-negotiable 13);
 * the service's schema whitelist enforces that before any frame is stored. No I/O, no clock: every
 * time is the caller's DB time (D-03).
 */
const KEY_EVERY_SLOTS = 60; // a keyframe every 10 minutes
const KEY_MAX_AGE_MS = 10 * 60_000;
const MAX_GAP_MS = 30_000; // worker was down: restart from a keyframe
const RESOLVED_WINDOW_MS = 30 * 60_000;
const BINS = 10;

export type FieldQuestion = [
  id: string,
  title: string,
  horizon: string,
  topic: string,
  close_at: string,
  p: number | null,
  n: number,
  bins: number[] | null,
];
export interface FieldResolved {
  question_id: string;
  title: string;
  revision: number;
  outcome: string;
  resolved_at: string;
  n_scored: number;
  best: { edge: number; handle: string } | null;
  edges: [number, number][];
}
export interface FieldState {
  t: string;
  q: Map<string, FieldQuestion>;
  r: Map<string, FieldResolved>;
}
const CHANGE_FIELDS = ["title", "horizon", "topic", "close_at", "p", "n", "bins"] as const;
export type FieldChange = Partial<{
  title: string;
  horizon: string;
  topic: string;
  close_at: string;
  p: number | null;
  n: number;
  bins: number[] | null;
}>;
export interface FieldKeyframe {
  v: 1;
  k: "key";
  t: string;
  /** Sorted by question id. */
  q: FieldQuestion[];
  r: [resolutionId: string, entry: FieldResolved][];
}
export interface FieldDelta {
  v: 1;
  k: "delta";
  t: string;
  /**
   * Changed fields of existing lights, referenced by position in the previous state's ids sorted
   * ascending: a uuid per change would push the 24 h ring past D-33's 100 MB under lz4.
   */
  c: [index: number, change: FieldChange][];
  a: FieldQuestion[];
  x: string[];
  r: [resolutionId: string, entry: FieldResolved][];
}
export type FieldFrame = FieldKeyframe | FieldDelta;
export interface FieldRead {
  t: string;
  open: {
    id: string;
    title: string;
    horizon: string;
    topic: string;
    close_at: string;
    p_yes: string | null;
    forecast_count: string | number;
  }[];
  bins: { question_id: string; bin: number; n: number }[];
  resolved: {
    id: string;
    question_id: string;
    title: string;
    revision: number;
    outcome: string;
    resolved_at: string;
    scores: {
      p_clipped: string | number;
      edge: string | number;
      is_sandbox: boolean;
      agent_id: string;
      handle: string;
    }[];
  }[];
}

/** 3 dp; `+ 0` folds -0 into 0 so equal frames serialize equally. */
const round3 = (value: number) => Math.round(value * 1000) / 1000 + 0;
const sortedIds = (state: FieldState) => [...state.q.keys()].sort();

export function buildState(read: FieldRead): FieldState {
  const t = Date.parse(read.t);
  const counts = new Map<string, number[]>();
  for (const row of read.bins) {
    const bins = counts.get(row.question_id) ?? Array<number>(BINS).fill(0);
    bins[row.bin]! += Number(row.n);
    counts.set(row.question_id, bins);
  }
  const q = new Map<string, FieldQuestion>();
  for (const row of read.open) {
    // Pitfall F2: the view's clock moved on after T; the frame's own T decides.
    if (Date.parse(row.close_at) <= t) continue;
    const n = Number(row.forecast_count);
    q.set(row.id, [
      row.id,
      row.title,
      row.horizon,
      row.topic,
      row.close_at,
      row.p_yes === null ? null : round3(Number(row.p_yes)),
      n,
      n >= MIN_CROWD_OTHER_AGENTS ? (counts.get(row.id) ?? Array<number>(BINS).fill(0)) : null,
    ]);
  }
  const r = new Map<string, FieldResolved>();
  for (const row of read.resolved) {
    if (Date.parse(row.resolved_at) <= t - RESOLVED_WINDOW_MS) continue;
    let best: (typeof row.scores)[number] | undefined;
    for (const score of row.scores) {
      // docs/09 §1: Sandbox citizens never rank, so a Sandbox score never names a handle.
      if (score.is_sandbox) continue;
      const edge = Number(score.edge);
      if (
        !best ||
        edge > Number(best.edge) ||
        (edge === Number(best.edge) && score.agent_id < best.agent_id)
      )
        best = score;
    }
    r.set(row.id, {
      question_id: row.question_id,
      title: row.title,
      revision: row.revision,
      outcome: row.outcome,
      resolved_at: row.resolved_at,
      n_scored: row.scores.length,
      best: best ? { edge: round3(Number(best.edge)), handle: best.handle } : null,
      edges: row.scores
        .map((score): [number, number] => [
          round3(Number(score.p_clipped)),
          round3(Number(score.edge)),
        ])
        .sort((a, b) => a[0] - b[0] || a[1] - b[1]),
    });
  }
  return { t: read.t, q, r };
}

export function keyframe(state: FieldState): FieldKeyframe {
  return {
    v: 1,
    k: "key",
    t: state.t,
    q: sortedIds(state).map((id) => state.q.get(id)!),
    r: [...state.r].sort(([a], [b]) => (a < b ? -1 : 1)),
  };
}

export function diffState(prev: FieldState, next: FieldState): FieldDelta {
  const index = new Map(sortedIds(prev).map((id, i) => [id, i]));
  const delta: FieldDelta = { v: 1, k: "delta", t: next.t, c: [], a: [], x: [], r: [] };
  for (const [id, light] of next.q) {
    const before = prev.q.get(id);
    if (!before) {
      delta.a.push(light);
      continue;
    }
    const change: Record<string, unknown> = {};
    CHANGE_FIELDS.forEach((field, i) => {
      if (JSON.stringify(before[i + 1]) !== JSON.stringify(light[i + 1]))
        change[field] = light[i + 1];
    });
    if (Object.keys(change).length > 0) delta.c.push([index.get(id)!, change as FieldChange]);
  }
  for (const id of prev.q.keys()) if (!next.q.has(id)) delta.x.push(id);
  for (const [id, entry] of next.r)
    if (JSON.stringify(prev.r.get(id)) !== JSON.stringify(entry)) delta.r.push([id, entry]);
  return delta;
}

export function applyDelta(state: FieldState, delta: FieldDelta): FieldState {
  const ids = sortedIds(state);
  const q = new Map(state.q);
  for (const [i, change] of delta.c) {
    const light = [...q.get(ids[i]!)!] as FieldQuestion;
    CHANGE_FIELDS.forEach((field, f) => {
      const value = change[field];
      if (value !== undefined) light[f + 1] = value;
    });
    q.set(light[0], light);
  }
  for (const id of delta.x) q.delete(id);
  for (const light of delta.a) q.set(light[0], light);
  const r = new Map(state.r);
  for (const [id, entry] of delta.r) r.set(id, entry);
  const horizon = Date.parse(delta.t) - RESOLVED_WINDOW_MS;
  for (const [id, entry] of r) if (Date.parse(entry.resolved_at) <= horizon) r.delete(id);
  return { t: delta.t, q, r };
}

/** Replays a ring segment; it must start at (or contain) a keyframe. */
export function stateFromFrames(frames: readonly FieldFrame[]): FieldState {
  let state: FieldState | undefined;
  for (const frame of frames) {
    if (frame.k === "key")
      state = {
        t: frame.t,
        q: new Map(frame.q.map((light) => [light[0], light])),
        r: new Map(frame.r),
      };
    else if (state) state = applyDelta(state, frame);
  }
  if (!state) throw new Error("no keyframe");
  return state;
}

export function frameKind(input: {
  slot: number;
  t: string;
  lastKeyAt: string | null;
  lastFrameAt: string | null;
}): "key" | "delta" {
  const t = Date.parse(input.t);
  if (input.slot % KEY_EVERY_SLOTS === 0 || !input.lastKeyAt || !input.lastFrameAt) return "key";
  if (t - Date.parse(input.lastKeyAt) >= KEY_MAX_AGE_MS) return "key";
  return t - Date.parse(input.lastFrameAt) > MAX_GAP_MS ? "key" : "delta";
}
