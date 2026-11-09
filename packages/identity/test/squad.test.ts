/* eslint-disable @typescript-eslint/no-explicit-any */
import { createHash } from "node:crypto";
import { describe, expect, it } from "vitest";
import {
  buildSquadProofBundle,
  canonicalBytes,
  createSquadDeleteIntent,
  createSquadPutIntent,
  hashSquadEntry,
  merkleRoot,
  parseSquadStatement,
  replaySquad,
  requestSigningMessage,
  sha256Hex,
  signSquadHead,
  signVaultHead,
  squadDayRoot,
  squadGenesis,
  squadHeadPreimage,
  squadSigningMessage,
  squadStatementBytes,
  verifyEd25519,
  verifySquadBundle,
  verifySquadHead,
} from "../src/index.js";
import type { SquadStatement } from "../src/index.js";
import { oracleKey, oracleScenario } from "./fixtures/squad-oracle.js";
import file from "./squad-vectors.json" with { type: "json" };

type Json = any;
const vectors: Json = file;

// RESEARCH F1.7 with the O-2 `sig` entry hash: the parent fill must reproduce them.
const GENESIS = "e0a4268ef8453ba0e11557b9c8c83bc88630a8e7774ac9177c0e29fa3c902960";
const FOUND_CONTENT_HASH = "b8cc77584a98da225ea018b715be199bbff74bc1f20c1140ae45d1afe53774b9";
const FOUND_MESSAGE_SHA256 = "8a853ea8159af39aa16a9df63b99709c8df68bfc213481a183c2cb346bea14e1";
const FOUND_SIG =
  "MbkoWL-ALJlZthteAIQayBrbycTa2SmjFzqH_-jRjssmSF0S2o499VhZSp_-3R-SBZQitOtAhh7YgoXvYFSTCQ";
const FOUND_ENTRY_HASH = "ac2fc20a409eeba7ad0116038689537ef0d9e64a4747035adb3126a78932d05f";
const PKCS8_PREFIX = "302e020100300506032b657004220420";
const S1_ID = "01900000-0000-7000-8000-000000000001";
const FOUNDER = "did:web:agentland.us:agents:founder-one";
const NAMES: string[] = [
  "S1-lifecycle",
  "S2-succession",
  "N-prefix",
  "N-vault-intent",
  "N-stale-seq",
  "N-broken-link",
  "N-foreign-squad",
  "N-unknown-key",
  "N-key-window",
  "N-tamper",
  "N-payload-missing",
  "N-payload-hash",
  "N-noncanonical",
  "N-actor-mismatch",
  "N-statement-delete",
  "N-found-twice",
  "N-platform-found",
  "N-attest-by-member",
  "N-non-member",
  "N-invite-by-member",
  "N-accept-expired",
  "N-accept-demoted",
  "N-accept-twice",
  "N-superseded",
  "N-last-admin-leave",
  "N-demote-last-admin",
  "N-squad-full",
  "N-epoch-skip",
  "N-epoch-wraps",
  "N-closed",
  "N-head-mismatch",
];

const seeds = new Map<string, string>(vectors.keys.map((k: Json) => [k.label, k.seed_hex]));
const pkcs8 = (label: string) => Buffer.from(PKCS8_PREFIX + seeds.get(label)!, "hex");
const jwk = (label: string) =>
  ({ kty: "OKP", crv: "Ed25519", x: oracleKey(seeds.get(label)!).x }) as const;
const signerKeys: Json[] = vectors.agents.map((agent: Json) => ({
  did: agent.did,
  keys: agent.keys.map((key: Json) => ({
    id: key.id,
    publicKeyJwk: jwk(key.key),
    purpose: "signing",
    activated_at: key.activated_at,
    ...(key.revoked_at === undefined ? {} : { revoked_at: key.revoked_at }),
  })),
}));
const platformKeys: Json[] = [
  { kid: vectors.platform.kid, publicKeyJwk: jwk(vectors.platform.key) },
];
const scenario = (name: string): Json => vectors.scenarios.find((s: Json) => s.name === name);
const S1 = scenario("S1-lifecycle");
const copy = (value: Json): Json => JSON.parse(JSON.stringify(value));
const decode = (statements: Json[]): Json[] =>
  statements.map((s) => ({
    seq: s.seq,
    content: new Uint8Array(Buffer.from(s.content_b64url, "base64url")),
  }));
const replayInput = (s: Json): Json => ({
  squadId: s.squad_id,
  entries: s.entries,
  statements: decode(s.statements),
  signerKeys,
  platformKeys,
  expectedHead: s.expected_head ?? s.head,
});
const vaultProjection = (entry: Json) => ({
  seq: entry.seq,
  key: entry.key,
  op: entry.op,
  content_hash: entry.content_hash,
  content_ref: entry.content_ref,
  content_type: entry.content_type,
  tags: entry.tags,
  prev_hash: entry.prev_hash,
});
const intentOf = (entry: Json) => {
  const intent = copy(entry);
  delete intent.ts_server;
  delete intent.sig;
  return intent;
};
const utf8 = (text: string) => new TextEncoder().encode(text);
const schemaFailure = {
  valid: false,
  error: { stage: "schema", reason: "invalid-schema-or-trust-pins" },
};
// Class and exact message both, so a missing export ("is not a function") cannot pass.
const throwsWith = (
  run: () => unknown,
  kind: typeof TypeError | typeof RangeError,
  message: string,
) => {
  expect(run).toThrow(kind);
  expect(run).toThrow(new RegExp(`^${message.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}$`));
};

describe("vectors", () => {
  it("file shape", () => {
    expect(Object.keys(vectors).sort()).toEqual([
      "agents",
      "anchors",
      "attribution",
      "bundle",
      "head",
      "keys",
      "platform",
      "scenarios",
    ]);
    expect(vectors.scenarios.map((s: Json) => s.name)).toEqual(NAMES);
    expect(vectors.scenarios.filter((s: Json) => s.name.startsWith("N-"))).toHaveLength(29);
    const missing: string[] = [];
    for (const k of vectors.keys) if (k.public_x === null) missing.push(`keys.${k.label}`);
    if (vectors.platform.public_x === null) missing.push("platform.public_x");
    for (const s of vectors.scenarios)
      for (const field of ["entries", "statements", "head"])
        if (s[field] === null) missing.push(`${s.name}.${field}`);
    if (vectors.head.value === null) missing.push("head.value");
    if (vectors.bundle.published_root === null) missing.push("bundle.published_root");
    if (vectors.bundle.value === null) missing.push("bundle.value");
    expect(missing).toEqual([]);
    for (const k of vectors.keys) expect(k.public_x).toBe(oracleKey(k.seed_hex).x);
  });

  it("anchors", () => {
    expect(vectors.anchors).toEqual({
      genesis: GENESIS,
      found_content_hash: FOUND_CONTENT_HASH,
      found_signing_message_sha256: FOUND_MESSAGE_SHA256,
      found_sig: FOUND_SIG,
      found_entry_hash: FOUND_ENTRY_HASH,
    });
    // Independent of sha256Hex: node:crypto over the D-30 preimage.
    const genesis = createHash("sha256").update(`agentland-squad/1\n${S1_ID}`).digest("hex");
    expect(genesis).toBe(GENESIS);
    expect(squadGenesis(S1_ID)).toBe(GENESIS);
    const entry = S1.entries[0];
    expect(entry.prev_hash).toBe(GENESIS);
    expect(entry.content_hash).toBe(FOUND_CONTENT_HASH);
    expect(sha256Hex(squadSigningMessage(intentOf(entry)))).toBe(FOUND_MESSAGE_SHA256);
    expect(entry.sig).toBe(FOUND_SIG);
    expect(hashSquadEntry(entry)).toBe(FOUND_ENTRY_HASH);
    expect(S1.entries[1].prev_hash).toBe(FOUND_ENTRY_HASH);
  });

  it("oracle", () => {
    expect(oracleScenario(vectors, S1)).toEqual({
      entries: S1.entries,
      statements: S1.statements,
      head: S1.head,
    });
  });

  it("domains", () => {
    const entry = S1.entries[0];
    const message = squadSigningMessage(intentOf(entry));
    const prefix = utf8("agentland-squad/1\n");
    expect(Buffer.from(message.subarray(0, prefix.length))).toEqual(Buffer.from(prefix));
    expect(message[0]).toBe("a".charCodeAt(0));
    const vault = canonicalBytes(vaultProjection(entry));
    expect(Buffer.from(message).equals(Buffer.from(vault))).toBe(false);
    for (const other of [
      "agentland-pop/1\n",
      "agentland-verify/1:",
      "agentland-arena-forecast/1\n",
    ])
      expect("agentland-squad/1\n".startsWith(other)).toBe(false);
    const founder = jwk("founder");
    expect(verifyEd25519(message, entry.sig, founder)).toBe(true);
    expect(verifyEd25519(vault, entry.sig, founder)).toBe(false);
    const content = decode(S1.statements)[0].content;
    const request = requestSigningMessage({
      method: "POST",
      requestTarget: "/v1/squads",
      timestamp: entry.ts_server,
      rawBody: content,
    });
    expect(verifyEd25519(request, entry.sig, founder)).toBe(false);
  });

  it("intents", () => {
    const base = {
      seq: "1",
      key: "vault/a",
      prev_hash: GENESIS,
      squad_id: S1_ID,
      signer: FOUNDER,
      signing_key_id: `${FOUNDER}#key-1`,
    };
    const hash = sha256Hex(utf8("x"));
    expect(createSquadPutIntent({ ...base, content: utf8("x") })).toEqual({
      ...base,
      op: "put",
      content_hash: hash,
      content_ref: `sha256:${hash}`,
      content_type: "text/plain; charset=utf-8",
      tags: [],
    });
    expect(createSquadDeleteIntent(base)).toEqual({
      ...base,
      op: "delete",
      content_hash: sha256Hex(new Uint8Array()),
      content_ref: null,
      content_type: "application/octet-stream",
      tags: [],
    });
    const put = (overrides: Json) => () =>
      createSquadPutIntent({ ...base, content: utf8("x"), ...overrides });
    // Hex letters, so the uppercase form actually differs from a valid lowercase id.
    const UPPER_ID = "0190000A-0000-7000-8000-00000000000A";
    for (const squad_id of [UPPER_ID, "01900000-0000-4000-8000-000000000001"])
      throwsWith(put({ squad_id }), TypeError, "Lowercase UUIDv7 squad id required");
    throwsWith(() => squadGenesis(UPPER_ID), TypeError, "Lowercase UUIDv7 squad id required");
    throwsWith(put({ signer: "did:web:example.com" }), TypeError, "Squad signer DID required");
    for (const signing_key_id of ["did:web:agentland.us:agents:other#key-1", ""])
      throwsWith(put({ signing_key_id }), TypeError, "Squad signing key id required");
    throwsWith(put({ key: "private/a" }), TypeError, "Vault namespace and nonempty key required");
  });

  it("statements", () => {
    const decoded = decode(S1.statements);
    expect(decoded).toHaveLength(10);
    for (const { content } of decoded) {
      const statement = parseSquadStatement(content);
      expect(Buffer.from(squadStatementBytes(statement))).toEqual(Buffer.from(content));
    }
    const parsed = decoded.map(({ content }) => parseSquadStatement(content));
    const found = parsed[0];
    const epoch = parsed.find((s: Json) => s.kind === "epoch");
    if (epoch?.wraps === undefined) throw new Error("epoch wraps missing");
    const common = { squad_id: S1_ID, ts: "2026-11-01T00:00:00.000Z", actor_did: FOUNDER };
    const two = "did:web:agentland.us:agents:member-two";
    const bad: Json[] = [
      { ...found, kind: "merge" },
      { ...common, kind: "invite", subject_did: two, role: "member" },
      { ...common, kind: "accept", subject_did: two, actor_did: two },
      { ...epoch, epoch: "01" },
      { ...epoch, wraps: [...epoch.wraps].reverse() },
      { ...epoch, wraps: [epoch.wraps[0], epoch.wraps[0]] },
      { ...common, kind: "invite", subject_did: two, reason: "🙂".repeat(501) },
      {
        ...common,
        kind: "attest_leave",
        subject_did: two,
        actor_did: "did:web:agentland.us",
        reason: "suspended",
      },
      { ...found, subject_did: "did:web:example.com" },
    ];
    for (const statement of bad)
      throwsWith(() => squadStatementBytes(statement), TypeError, "Exact squad statement required");
    const longest: SquadStatement = {
      ...common,
      kind: "invite",
      subject_did: two,
      reason: "🙂".repeat(500),
    };
    expect(parseSquadStatement(squadStatementBytes(longest))).toEqual(longest);
    const noncanonical = scenario("N-noncanonical").steps[0].content_utf8;
    throwsWith(
      () => parseSquadStatement(utf8(noncanonical)),
      TypeError,
      "Canonical squad statement bytes required",
    );
  });

  it("hash and day root", () => {
    S1.entries.forEach((entry: Json, index: number) => {
      expect(hashSquadEntry(entry)).toBe(sha256Hex(canonicalBytes(entry)));
      const next = S1.entries[index + 1];
      expect(next?.prev_hash ?? S1.head.head_hash).toBe(hashSquadEntry(entry));
    });
    expect(squadDayRoot(S1.entries, "2026-11-01")).toBe(
      merkleRoot(S1.entries.slice(0, 5).map((entry: Json) => canonicalBytes(entry))),
    );
    expect(squadDayRoot(S1.entries, "2026-11-02")).toBe(sha256Hex(new Uint8Array()));
    throwsWith(() => squadDayRoot(S1.entries, "2026-11-1"), TypeError, "UTC date required");
  });
});

describe("negative", () => {
  for (const s of vectors.scenarios.filter((x: Json) => x.name.startsWith("N-")))
    it(`${s.name} fails at its stage`, () => {
      expect(replaySquad(replayInput(s))).toEqual(s.expected);
    });
});

describe("replay", () => {
  for (const name of ["S1-lifecycle", "S2-succession"])
    it(name, () => {
      const s = scenario(name);
      expect(replaySquad(replayInput(s))).toEqual({
        ...s.expected,
        squad_id: s.squad_id,
        head_hash: s.head.head_hash,
      });
    });

  it("membership intervals are half-open", () => {
    const result: Json = replaySquad(replayInput(S1));
    const two = result.members.find((m: Json) => m.did.endsWith(":member-two"));
    const remove = S1.entries.find((e: Json) => e.key === "public/.squad/remove");
    expect(two.until_seq).toBe("10");
    expect(two.until_seq).toBe(remove.seq);
  });

  it("every entry is tamper-evident", () => {
    for (let index = 0; index < S1.entries.length; index += 1) {
      const entries = copy(S1.entries);
      entries[index].sig = S1.entries[(index + 1) % S1.entries.length].sig;
      expect(replaySquad({ ...replayInput(S1), entries })).toEqual({
        valid: false,
        error: { stage: "signature", reason: "untrusted-signature", index },
      });
    }
  });

  it("pins are external", () => {
    const input = replayInput(S1);
    expect(replaySquad({ ...input, signerKeys: [...signerKeys, signerKeys[0]] })).toEqual(
      schemaFailure,
    );
    expect(
      replaySquad({
        ...input,
        platformKeys: [{ kid: "k".repeat(201), publicKeyJwk: platformKeys[0].publicKeyJwk }],
      }),
    ).toEqual(schemaFailure);
    expect(replaySquad(null as never)).toEqual(schemaFailure);
    expect(replaySquad({ ...input, extra: 1 })).toEqual(schemaFailure);
  });

  it("the platform key is a pin", () => {
    expect(replaySquad({ ...replayInput(S1), platformKeys: [] })).toEqual({
      valid: false,
      error: { stage: "signature", reason: "unknown-signer-key", index: 12 },
    });
  });
});

describe("head", () => {
  const statement = () => ({
    squad_id: S1_ID,
    seq: S1.head.seq,
    head_hash: S1.head.head_hash,
    ts: vectors.head.ts,
  });
  const platform = () => jwk(vectors.platform.key);

  it("signs and verifies", () => {
    const signed = signSquadHead({ ...statement(), kid: vectors.platform.kid }, pkcs8("platform"));
    expect(signed).toEqual(vectors.head.value);
    expect(verifySquadHead(vectors.head.value, platform())).toBe(true);
  });

  it("a changed member fails", () => {
    const head = vectors.head.value;
    const flipped = head.sig[0] === "A" ? `B${head.sig.slice(1)}` : `A${head.sig.slice(1)}`;
    const changes: Json[] = [
      { seq: "12" },
      { head_hash: "00".repeat(32) },
      { ts: "2026-11-08T10:00:00.501Z" },
      { squad_id: "01900000-0000-7000-8000-000000000002" },
      { sig: flipped },
    ];
    for (const change of changes)
      expect(verifySquadHead({ ...head, ...change }, platform())).toBe(false);
  });

  it("domains", () => {
    const vault = signVaultHead(
      {
        did: FOUNDER,
        seq: S1.head.seq,
        head_hash: S1.head.head_hash,
        ts: vectors.head.ts,
        kid: vectors.platform.kid,
      },
      pkcs8("platform"),
    );
    expect(verifySquadHead({ ...vectors.head.value, sig: vault.sig }, platform())).toBe(false);
  });

  it("never throws", () => {
    expect(verifySquadHead(null as never, platform())).toBe(false);
    expect(verifySquadHead({ ...vectors.head.value, extra: 1 } as never, platform())).toBe(false);
    const preimage = squadHeadPreimage(statement());
    const object = JSON.parse(new TextDecoder().decode(preimage));
    expect(Object.keys(object)).toEqual(["format", "head_hash", "seq", "squad_id", "ts"]);
    expect(object).toEqual({ format: "agentland-squad-head/1", ...statement() });
    expect(Buffer.from(preimage)).toEqual(Buffer.from(canonicalBytes(object)));
  });
});

describe("bundle", () => {
  const auditLeaves = (): Uint8Array[] => [
    ...vectors.bundle.audit_leaves_hex.map(
      (hex: string) => new Uint8Array(Buffer.from(hex, "hex")),
    ),
    new Uint8Array(Buffer.from(squadDayRoot(S1.entries, "2026-11-01"), "hex")),
  ];
  const pins = (publishedRoot: string): Json => ({
    signerKeys,
    platformKeys,
    expectedHead: S1.head,
    publishedRoot,
  });
  const build = (squadLeafIndex: number) =>
    buildSquadProofBundle({
      squadId: S1_ID,
      entries: S1.entries,
      statements: decode(S1.statements),
      seq: vectors.bundle.seq,
      auditLeaves: auditLeaves(),
      squadLeafIndex,
    });

  it("builds the filled bundle", () => {
    expect(build(vectors.bundle.squad_leaf_index)).toEqual(vectors.bundle.value);
    expect(merkleRoot(auditLeaves())).toBe(vectors.bundle.published_root);
  });

  it("verifies", () => {
    expect(
      verifySquadBundle(vectors.bundle.value, pins(vectors.bundle.published_root)),
    ).toMatchObject({
      valid: true,
      proved_seq: "4",
      root: vectors.bundle.published_root,
    });
  });

  it("fails on a changed path, root, payload or member", () => {
    const root = vectors.bundle.published_root;
    const other = (hex: string) => (hex === "00".repeat(32) ? "11".repeat(32) : "00".repeat(32));
    const entryPath = copy(vectors.bundle.value);
    entryPath.proof.siblings[0] = other(entryPath.proof.siblings[0]);
    expect(verifySquadBundle(entryPath, pins(root))).toEqual({
      valid: false,
      error: { stage: "proof", reason: "invalid-entry-path" },
    });
    const auditPath = copy(vectors.bundle.value);
    auditPath.audit.proof.siblings[0] = other(auditPath.audit.proof.siblings[0]);
    const auditFailure = {
      valid: false,
      error: { stage: "audit", reason: "root-leaf-or-path-mismatch" },
    };
    expect(verifySquadBundle(auditPath, pins(root))).toEqual(auditFailure);
    expect(verifySquadBundle(vectors.bundle.value, pins(other(root)))).toEqual(auditFailure);
    const payload = copy(vectors.bundle.value);
    const k = payload.entries.findIndex((e: Json) => e.seq === payload.statements[0].seq);
    payload.statements[0].content_b64url = Buffer.from("{}").toString("base64url");
    expect(verifySquadBundle(payload, pins(root))).toEqual({
      valid: false,
      error: { stage: "statement", reason: "payload-mismatch", index: k },
    });
    expect(verifySquadBundle({ ...vectors.bundle.value, keys: signerKeys }, pins(root))).toEqual({
      valid: false,
      error: { stage: "bundle", reason: "invalid-schema-or-trust-pins" },
    });
    throwsWith(() => build(0), RangeError, "Squad-root leaf index out of range");
  });
});
