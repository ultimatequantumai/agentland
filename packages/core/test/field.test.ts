import { describe, expect, it } from "vitest";
import {
  applyDelta,
  buildState,
  diffState,
  frameKind,
  keyframe,
  MIN_CROWD_OTHER_AGENTS,
  reliability,
  stateFromFrames,
  type FieldQuestion,
  type FieldRead,
  type FieldResolved,
  type FieldState,
} from "../src/index.js";

const T = "2026-10-23T12:00:00.000Z";
const at = (ms: number) => new Date(Date.parse(T) + ms).toISOString();
const uuid = (n: number) => `00000000-0000-4000-8000-${n.toString(16).padStart(12, "0")}`;

function openRow(n: number, overrides: Partial<FieldRead["open"][number]> = {}) {
  return {
    id: uuid(n),
    title: `Question ${n}`,
    horizon: "hour",
    topic: "other",
    close_at: at(60_000),
    p_yes: null,
    forecast_count: "0",
    ...overrides,
  };
}
function read(overrides: Partial<FieldRead> = {}): FieldRead {
  return { t: T, open: [], bins: [], resolved: [], ...overrides };
}

describe("buildState (D-32, non-negotiable 13)", () => {
  it(`publishes bins only from ${MIN_CROWD_OTHER_AGENTS} distinct final forecasters`, () => {
    const four = buildState(
      read({
        open: [openRow(1, { forecast_count: "4" })],
        bins: [{ question_id: uuid(1), bin: 4, n: 4 }],
      }),
    );
    expect(four.q.get(uuid(1))).toEqual([
      uuid(1),
      "Question 1",
      "hour",
      "other",
      at(60_000),
      null,
      4,
      null,
    ]);
    const five = buildState(
      read({
        open: [openRow(1, { forecast_count: "5" })],
        bins: [
          { question_id: uuid(1), bin: 4, n: 3 },
          { question_id: uuid(1), bin: 9, n: 2 },
        ],
      }),
    );
    const bins = five.q.get(uuid(1))![7]!;
    expect(bins).toEqual([0, 0, 0, 0, 3, 0, 0, 0, 0, 2]);
    expect(bins.reduce((a, b) => a + b, 0)).toBe(5);
  });

  it("drops a question whose close_at <= T even if the view returned it (Pitfall F2)", () => {
    const state = buildState(
      read({ open: [openRow(1, { close_at: T }), openRow(2, { close_at: at(-1) }), openRow(3)] }),
    );
    expect([...state.q.keys()]).toEqual([uuid(3)]);
  });

  it("quantizes market p to 3 dp and keeps the exact 8-field tuple", () => {
    const state = buildState(read({ open: [openRow(1, { p_yes: "0.41237" })] }));
    const q = state.q.get(uuid(1))!;
    expect(q).toHaveLength(8);
    expect(q[5]).toBe(0.412);
  });

  it("builds resolved entries with the non-Sandbox best rule and id-free sorted edges", () => {
    const state = buildState(
      read({
        resolved: [
          {
            id: uuid(100),
            question_id: uuid(1),
            title: "Resolved one",
            revision: 2,
            outcome: "yes",
            resolved_at: at(-60_000),
            scores: [
              // Sandbox best edge never names a handle.
              {
                p_clipped: "0.99",
                edge: "0.24",
                is_sandbox: true,
                agent_id: uuid(1),
                handle: "sandboxed",
              },
              {
                p_clipped: "0.71234",
                edge: "0.12345",
                is_sandbox: false,
                agent_id: uuid(3),
                handle: "later",
              },
              {
                p_clipped: "0.7",
                edge: "0.12345",
                is_sandbox: false,
                agent_id: uuid(2),
                handle: "earlier",
              },
              {
                p_clipped: "0.2",
                edge: "-0.3",
                is_sandbox: false,
                agent_id: uuid(4),
                handle: "worst",
              },
            ],
          },
          {
            id: uuid(101),
            question_id: uuid(2),
            title: "Sandbox only",
            revision: 1,
            outcome: "no",
            resolved_at: at(-1_000),
            scores: [
              {
                p_clipped: "0.1",
                edge: "0.2",
                is_sandbox: true,
                agent_id: uuid(5),
                handle: "citizen",
              },
            ],
          },
          {
            id: uuid(102),
            question_id: uuid(3),
            title: "Too old",
            revision: 1,
            outcome: "no",
            resolved_at: at(-30 * 60_000),
            scores: [],
          },
        ],
      }),
    );
    const entry = state.r.get(uuid(100))!;
    expect(Object.keys(entry).sort()).toEqual(
      [
        "best",
        "edges",
        "n_scored",
        "outcome",
        "question_id",
        "resolved_at",
        "revision",
        "title",
      ].sort(),
    );
    expect(Object.keys(entry.best!).sort()).toEqual(["edge", "handle"]);
    expect(entry.best).toEqual({ edge: 0.123, handle: "earlier" });
    expect(entry.n_scored).toBe(4);
    expect(entry.edges).toEqual([
      [0.2, -0.3],
      [0.7, 0.123],
      [0.712, 0.123],
      [0.99, 0.24],
    ]);
    expect(JSON.stringify(entry)).not.toContain(uuid(2));
    const sandbox = state.r.get(uuid(101))!;
    expect(sandbox.best).toBeNull();
    expect(sandbox.n_scored).toBe(1);
    expect(sandbox.edges).toEqual([[0.1, 0.2]]);
    expect(state.r.has(uuid(102))).toBe(false);
  });
});

describe("bin rule equals core reliability()", () => {
  it("least(floor(p*10),9) matches reliability() over the 10001-point 4-dp grid", () => {
    const mismatches: number[] = [];
    for (let k = 0; k <= 10_000; k++) {
      const p = k / 10_000;
      const sqlBin = Math.min(Math.floor(k / 1000), 9);
      const coreBin = reliability([{ p, o: 0 }]).findIndex((bin) => bin.count === 1);
      if (sqlBin !== coreBin) mismatches.push(k);
    }
    expect(mismatches).toEqual([]);
  });
});

// Deterministic PRNG (mulberry32): failures reproduce exactly.
function prng(seed: number) {
  return () => {
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function randomQuestion(random: () => number, id: string): FieldQuestion {
  const n = Math.floor(random() * 9);
  const bins =
    n >= MIN_CROWD_OTHER_AGENTS ? Array.from({ length: 10 }, () => Math.floor(random() * 3)) : null;
  return [
    id,
    `Title ${Math.floor(random() * 5)}`,
    (["hour", "day", "week", "month", "long"] as const)[Math.floor(random() * 5)]!,
    "other",
    at(Math.floor(random() * 4) * 60_000 + 60_000),
    random() < 0.3 ? null : Math.round(random() * 1000) / 1000,
    n,
    bins,
  ];
}
function randomResolved(random: () => number, t: string): FieldResolved {
  return {
    question_id: uuid(Math.floor(random() * 50)),
    title: "Resolved",
    revision: 1 + Math.floor(random() * 2),
    outcome: random() < 0.5 ? "yes" : "no",
    resolved_at: new Date(Date.parse(t) - Math.floor(random() * 29 * 60_000)).toISOString(),
    n_scored: Math.floor(random() * 6),
    best: random() < 0.5 ? null : { edge: 0.1, handle: "h" },
    edges: [[0.5, Math.round(random() * 100) / 1000]],
  };
}

describe("diffState / applyDelta round trip", () => {
  it("applyDelta(prev, diffState(prev, next)) equals next over 200 seeded pairs", () => {
    const random = prng(20261023);
    for (let pair = 0; pair < 200; pair++) {
      const prevT = at(pair * 10_000);
      const nextT = at(pair * 10_000 + 10_000);
      const prev: FieldState = { t: prevT, q: new Map(), r: new Map() };
      for (let i = 0; i < 20; i++) {
        if (random() < 0.7) prev.q.set(uuid(i), randomQuestion(random, uuid(i)));
      }
      for (let i = 0; i < 4; i++) prev.r.set(uuid(1000 + i), randomResolved(random, prevT));
      // Some previous resolved entries age out of the 30-minute window by next.t.
      prev.r.set(uuid(1999), {
        ...randomResolved(random, prevT),
        resolved_at: new Date(Date.parse(nextT) - 30 * 60_000).toISOString(),
      });
      const next: FieldState = { t: nextT, q: new Map(), r: new Map() };
      for (let i = 0; i < 20; i++) {
        const before = prev.q.get(uuid(i));
        const roll = random();
        if (before && roll < 0.15) continue; // removed
        if (before && roll < 0.6) {
          next.q.set(uuid(i), before);
          continue;
        }
        if (before) {
          const changed = [...before] as FieldQuestion;
          changed[5] = random() < 0.5 ? before[5] : Math.round(random() * 1000) / 1000;
          changed[6] = before[6] + (random() < 0.5 ? 1 : 0);
          changed[7] =
            changed[6] >= MIN_CROWD_OTHER_AGENTS
              ? Array.from({ length: 10 }, () => Math.floor(random() * 3))
              : null;
          next.q.set(uuid(i), changed);
        } else if (roll < 0.4) next.q.set(uuid(i), randomQuestion(random, uuid(i)));
      }
      for (const [id, entry] of prev.r) {
        if (Date.parse(entry.resolved_at) <= Date.parse(nextT) - 30 * 60_000) continue;
        next.r.set(id, random() < 0.5 ? entry : { ...entry, n_scored: entry.n_scored + 1 });
      }
      if (random() < 0.5) next.r.set(uuid(2000 + pair), randomResolved(random, nextT));
      const delta = diffState(prev, next);
      expect(applyDelta(prev, delta)).toEqual(next);
    }
  });

  it("diffState(s, s) is an empty delta", () => {
    const state: FieldState = {
      t: T,
      q: new Map([[uuid(1), randomQuestion(prng(1), uuid(1))]]),
      r: new Map(),
    };
    expect(diffState(state, state)).toEqual({ v: 1, k: "delta", t: T, c: [], a: [], x: [], r: [] });
  });

  it("applyDelta drops resolved entries older than 30 minutes", () => {
    const old = randomResolved(prng(2), T);
    const state: FieldState = {
      t: T,
      q: new Map(),
      r: new Map([[uuid(5), { ...old, resolved_at: at(-60_000) }]]),
    };
    const later = at(30 * 60_000); // resolved_at is now 31 minutes before t
    const next = applyDelta(state, { v: 1, k: "delta", t: later, c: [], a: [], x: [], r: [] });
    expect(next.r.size).toBe(0);
    expect(next.t).toBe(later);
  });
});

describe("frameKind (D-33)", () => {
  const slot = 177_000_001; // slot % 60 != 0
  it("keyframes at slot % 60 == 0, without a key within 10 min, or after a >30 s gap", () => {
    expect(
      frameKind({ slot: 177_000_000, t: T, lastKeyAt: at(-20_000), lastFrameAt: at(-10_000) }),
    ).toBe("key");
    expect(frameKind({ slot, t: T, lastKeyAt: null, lastFrameAt: null })).toBe("key");
    expect(frameKind({ slot, t: T, lastKeyAt: at(-601_000), lastFrameAt: at(-10_000) })).toBe(
      "key",
    );
    expect(frameKind({ slot, t: T, lastKeyAt: at(-300_000), lastFrameAt: at(-31_000) })).toBe(
      "key",
    );
    expect(frameKind({ slot, t: T, lastKeyAt: at(-300_000), lastFrameAt: at(-10_000) })).toBe(
      "delta",
    );
  });
});

describe("stateFromFrames", () => {
  const question: FieldQuestion = [uuid(2), "Q", "day", "finance", at(1000), 0.5, 1, null];
  const state: FieldState = { t: T, q: new Map([[uuid(2), question]]), r: new Map() };
  const next: FieldState = {
    t: at(10_000),
    q: new Map([[uuid(2), [uuid(2), "Q", "day", "finance", at(1000), 0.6, 2, null]]]),
    r: new Map(),
  };
  const delta = diffState(state, next);

  it("throws a plain Error without a keyframe", () => {
    for (const frames of [[], [delta]]) {
      let thrown: unknown;
      try {
        stateFromFrames(frames);
      } catch (error) {
        thrown = error;
      }
      expect(thrown).toBeInstanceOf(Error);
      expect((thrown as Error).constructor).toBe(Error);
      expect((thrown as Error).message).toBe("no keyframe");
    }
  });

  it("replays a delta onto its keyframe", () => {
    const key = keyframe(state);
    expect(stateFromFrames([key, delta])).toEqual(applyDelta(stateFromFrames([key]), delta));
    expect(stateFromFrames([key, delta])).toEqual(next);
  });

  it("keyframes sort lights and resolved entries by id and replay to the same state", () => {
    const resolved = randomResolved(prng(3), T);
    const unsorted: FieldState = {
      t: T,
      q: new Map([
        [uuid(3), randomQuestion(prng(4), uuid(3))],
        [uuid(1), randomQuestion(prng(5), uuid(1))],
      ]),
      r: new Map([
        [uuid(9), resolved],
        [uuid(7), resolved],
      ]),
    };
    const key = keyframe(unsorted);
    expect(key.q.map((light) => light[0])).toEqual([uuid(1), uuid(3)]);
    expect(key.r.map(([id]) => id)).toEqual([uuid(7), uuid(9)]);
    expect(stateFromFrames([key])).toEqual(unsorted);
  });
});

describe("buildState edge rules", () => {
  it("publishes zero bins at the floor without bin rows and breaks edge ties by agent id", () => {
    const state = buildState(
      read({
        open: [openRow(1, { forecast_count: String(MIN_CROWD_OTHER_AGENTS) })],
        resolved: [
          {
            id: uuid(100),
            question_id: uuid(2),
            title: "Tie",
            revision: 1,
            outcome: "yes",
            resolved_at: at(-1_000),
            scores: [
              { p_clipped: "0.6", edge: 0.1, is_sandbox: false, agent_id: uuid(2), handle: "a" },
              { p_clipped: "0.6", edge: 0.1, is_sandbox: false, agent_id: uuid(3), handle: "b" },
            ],
          },
        ],
      }),
    );
    expect(state.q.get(uuid(1))![7]).toEqual(Array<number>(10).fill(0));
    expect(state.r.get(uuid(100))!.best).toEqual({ edge: 0.1, handle: "a" });
  });
});
