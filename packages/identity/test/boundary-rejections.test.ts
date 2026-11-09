import { describe, expect, it } from "vitest";
import {
  buildDidDocument,
  buildDidHistory,
  canonicalBytes,
  canonicalize,
  createInclusionProof,
  createPutIntent,
  issueCredential,
  merkleRoot,
  parseIJson,
  signEd25519,
  validateVaultChain,
  verifyCredential,
  verifyEd25519,
  verifyInclusionProof,
  verifyVaultBundle,
} from "../src/index.js";
import type {
  PublicKeyRecord,
  RotationRecord,
  VaultProofBundle,
  VaultSigningKey,
} from "../src/index.js";
import fixture from "./fixtures/vault-three.json" with { type: "json" };
import { fixtureDailyRoot, fixtureHead, fixtureRoot } from "./fixtures/oracle.js";
import { did, testKey, timestamp } from "./helpers.js";
const key = testKey();
const next = testKey(1);
const record: PublicKeyRecord = {
  id: `${did}#key-1`,
  publicKeyJwk: key.publicKeyJwk,
  purpose: "signing",
  activated_at: timestamp,
};
const keys: VaultSigningKey[] = [{ from_seq: "1", publicKeyJwk: key.publicKeyJwk }];
const bundle = fixture as unknown as VaultProofBundle;
const pins = {
  keys,
  expectedHead: { seq: "3", head_hash: fixtureHead },
  publishedRoot: fixtureDailyRoot,
};

describe("strict security boundaries", () => {
  it("never executes object/array accessors or normalizes invalid JSON", () => {
    let read = false;
    const accessor = Object.defineProperty([1], "0", {
      get() {
        read = true;
        return 1;
      },
      enumerable: true,
    });
    const sparse = Object.assign(Array(1) as unknown[], { other: 1 });
    const extra = Object.assign([1], { other: 1 });
    for (const value of [accessor, sparse, extra, { toJSON: () => "different signed value" }])
      expect(() => canonicalize(value)).toThrow(TypeError);
    expect(read).toBe(false);
    for (const raw of [
      '{"a" 1}',
      '{"a":1;"b":2}',
      "[1;2]",
      "[1",
      "{",
      '"\u0001"',
      '"\\uZZZZ"',
      "nullx",
      "+1",
      ".1",
      "1.",
      "--1",
      '"\\ud800x"',
    ])
      expect(() => parseIJson(raw)).toThrow(TypeError);
    expect(() => parseIJson(1 as unknown as string)).toThrow(TypeError);
    expect(parseIJson(' ["𝄞", "a/b", "\\b\\t\\n\\f\\r", -0, 1E30] ')).toEqual([
      "𝄞",
      "a/b",
      "\b\t\n\f\r",
      -0,
      1e30,
    ]);
    expect(canonicalize({ first: { shared: 1 }, second: { shared: 1 } })).toBe(
      '{"first":{"shared":1},"second":{"shared":1}}',
    );
  });
  it("rejects invalid DID records and rotations without leaking public-input secrets", () => {
    for (const invalid of [
      null,
      {},
      [{ ...record, purpose: "unknown" }],
      [{ ...record, id: `${did}#bad fragment` }],
      [{ ...record, revoked_at: undefined }],
      [
        {
          ...record,
          publicKeyJwk: { ...key.publicKeyJwk, x: Buffer.alloc(31).toString("base64url") },
        },
      ],
    ])
      expect(() =>
        buildDidDocument({ handle: "weatherwise", keys: invalid as unknown as PublicKeyRecord[] }),
      ).toThrow(TypeError);
    expect(
      buildDidDocument({ handle: "weatherwise", keys: [{ ...record, revoked_at: timestamp }] })
        .authentication,
    ).toEqual([]);
    const statement = {
      old_pub: key.publicKeyJwk,
      new_pub: next.publicKeyJwk,
      reason: "scheduled",
      timestamp,
    };
    const rotation: RotationRecord = {
      statement,
      sig_old: signEd25519(canonicalBytes(statement), key.privatePkcs8),
      sig_new: signEd25519(canonicalBytes(statement), next.privatePkcs8),
    };
    const newRecord: PublicKeyRecord = {
      ...record,
      id: `${did}#key-2`,
      publicKeyJwk: next.publicKeyJwk,
    };
    const variants = [
      { ...rotation, statement: { ...statement, reason: "" } },
      { ...rotation, statement: { ...statement, new_pub: key.publicKeyJwk } },
      { ...rotation, statement: { ...statement, timestamp: "bad" } },
      { ...rotation, statement: { ...statement, old_pub: { ...key.publicKeyJwk, d: "secret" } } },
      { ...rotation, sig_new: undefined },
    ];
    for (const invalid of variants)
      expect(() =>
        buildDidHistory({
          handle: "weatherwise",
          keys: [record, newRecord],
          rotations: [invalid as RotationRecord],
        }),
      ).toThrow(TypeError);
    expect(() =>
      buildDidHistory({ handle: "weatherwise", keys: [record], rotations: [rotation] }),
    ).toThrow(TypeError);
    expect(() =>
      buildDidHistory({
        handle: "weatherwise",
        keys: [record, { ...newRecord, activated_at: "2026-01-02T00:00:00.000Z" }],
        rotations: [rotation],
      }),
    ).toThrow(TypeError);
    expect(() =>
      buildDidHistory({
        handle: "weatherwise",
        keys: [record, newRecord],
        rotations: null as unknown as RotationRecord[],
      }),
    ).toThrow(TypeError);
    const earlier = { ...statement, timestamp: "2025-12-31T00:00:00.000Z" };
    expect(() =>
      buildDidHistory({
        handle: "weatherwise",
        keys: [record, newRecord],
        rotations: [
          { statement: earlier, sig_old: signEd25519(canonicalBytes(earlier), key.privatePkcs8) },
        ],
      }),
    ).toThrow(TypeError);
    const later = { ...statement, timestamp: "2026-01-02T00:00:00.000Z" };
    const laterRotation = {
      statement: later,
      sig_old: signEd25519(canonicalBytes(later), key.privatePkcs8),
    };
    expect(
      buildDidHistory({
        handle: "weatherwise",
        keys: [record, newRecord],
        rotations: [laterRotation, rotation],
      }).rotations.map((item) => item.statement.timestamp),
    ).toEqual([timestamp, later.timestamp]);
  });
  it("returns false for malformed cryptographic inputs rather than deriving private trust", () => {
    const signature = signEd25519(Buffer.of(1), key.privatePkcs8);
    expect(verifyEd25519("message" as unknown as Uint8Array, signature, key.publicKeyJwk)).toBe(
      false,
    );
    expect(() => merkleRoot(null as unknown as Uint8Array[])).toThrow(TypeError);
    expect(() => createInclusionProof(null as unknown as Uint8Array[], 0)).toThrow(TypeError);
    expect(() => createInclusionProof(["bad" as unknown as Uint8Array], 0)).toThrow(TypeError);
    const path = { leaf_index: 0, tree_size: 1, siblings: [] };
    for (const proof of [
      { ...path, leaf_index: "0" },
      { ...path, tree_size: "1" },
      { ...path, siblings: null },
    ])
      expect(verifyInclusionProof(Buffer.of(1), proof as unknown as typeof path, fixtureRoot)).toBe(
        false,
      );
    expect(verifyInclusionProof("leaf" as unknown as Uint8Array, path, fixtureRoot)).toBe(false);
    for (const patch of [
      { did: "not-a-did" },
      { entries: null },
      { keys: null },
      { expectedHead: null },
      { expectedHead: { seq: 3, head_hash: fixtureHead } },
    ])
      expect(
        validateVaultChain({
          did,
          entries: bundle.entries,
          keys,
          expectedHead: pins.expectedHead,
          ...patch,
        } as unknown as Parameters<typeof validateVaultChain>[0]).valid,
      ).toBe(false);
    for (const audit of [
      { vault_root_leaf_bytes: "A", proof: path },
      { vault_root_leaf_bytes: Buffer.alloc(31).toString("base64url"), proof: path },
      {
        vault_root_leaf_bytes: Buffer.from(fixtureDailyRoot, "hex").toString("base64url"),
        proof: { ...path, siblings: [fixtureDailyRoot] },
      },
    ])
      expect(verifyVaultBundle({ ...bundle, audit }, pins).valid).toBe(false);
    for (const proof of [
      { ...bundle.proof, leaf_index: "1" },
      { ...bundle.proof, seq: "02" },
      { ...bundle.proof, leaf_index: Number.MAX_SAFE_INTEGER + 1 },
      { ...bundle.proof, siblings: null },
    ])
      expect(
        verifyVaultBundle({ ...bundle, proof } as unknown as VaultProofBundle, pins).valid,
      ).toBe(false);
    expect(() =>
      createPutIntent({
        seq: "1",
        key: "vault/x",
        content: Buffer.of(1),
        prev_hash: fixtureHead,
        tags: ["\ud800"],
      }),
    ).toThrow(TypeError);
  });
  it("validates absolute credential IDs, required issuer/time pins and evidence", () => {
    const evidence = { season: "s1", n: 0, shrunk_edge: 0, audit_root: fixtureRoot };
    const issuance = {
      id: "https://agentland.us/credentials/1",
      subjectDid: did,
      type: "SeasonResult" as const,
      evidence,
      validFrom: timestamp,
      issuerKeyId: "did:web:agentland.us#issuer",
      privatePkcs8: key.privatePkcs8,
    };
    for (const patch of [
      { id: "https://[" },
      { id: "urn:has space" },
      { evidence: { ...evidence, season: "" } },
      { validUntil: "2026-02-30T00:00:00.000Z" },
    ])
      expect(() => issueCredential({ ...issuance, ...patch })).toThrow(TypeError);
    const token = issueCredential(issuance);
    const options = {
      trustedIssuer: {
        issuer: "did:web:agentland.us",
        kid: issuance.issuerKeyId,
        publicKeyJwk: key.publicKeyJwk,
      },
      expectedSubjectDid: did,
      now: timestamp,
    };
    expect(verifyCredential(null as unknown as string, options).valid).toBe(false);
    expect(
      verifyCredential(token, {
        ...options,
        trustedIssuer: { ...options.trustedIssuer, kid: "relative" },
      }).valid,
    ).toBe(false);
    expect(verifyCredential(token, { ...options, expectedSubjectDid: "relative" }).valid).toBe(
      false,
    );
  });
});
