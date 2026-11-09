import { createHash } from "node:crypto";
import { describe, expect, it } from "vitest";
import {
  canonicalBytes,
  canonicalize,
  createDeleteIntent,
  createInclusionProof,
  createPutIntent,
  hashVaultEntry,
  merkleRoot,
  sha256Hex,
  signVaultIntent,
  stampVaultEntry,
  validateVaultChain,
  verifyEd25519,
  verifyInclusionProof,
  verifyVaultBundle,
} from "../src/index.js";
import type { VaultEntry, VaultIntent, VaultProofBundle, VaultSigningKey } from "../src/index.js";
import vectors from "./standards-vectors.json" with { type: "json" };
import fixture from "./fixtures/vault-three.json" with { type: "json" };
import {
  fixtureDailyRoot,
  fixtureEntryHashes,
  fixtureGenesis,
  fixtureHead,
  fixtureRoot,
} from "./fixtures/oracle.js";
import { did, testKey, timestamp } from "./helpers.js";
const key = testKey();
const keys: VaultSigningKey[] = [{ from_seq: "1", publicKeyJwk: key.publicKeyJwk }];
const entries = fixture.entries as unknown as VaultEntry[];
const expectedHead = { seq: "3", head_hash: fixtureHead };
const chain = { did, entries, keys, expectedHead };
const bundle = fixture as unknown as VaultProofBundle;
const pins = { keys, expectedHead, publishedRoot: fixtureDailyRoot };
const fixtureMerkleProof = {
  leaf_index: 1,
  tree_size: 3,
  siblings: [
    "f728fdc9448d353df8ac210f82ca04f2627c833719f7442bd58444867a7db160",
    "da55cd3e1f10da77fc63b252801d2451c80d891c43a20e668877719f555ceec3",
  ],
};
const bytes = Buffer.from("First memory");
const zero = "0".repeat(64);

function unsignedFixture(entry: VaultEntry): VaultIntent {
  return Object.fromEntries(
    Object.entries(entry).filter(([name]) => name !== "ts_server" && name !== "sig_agent"),
  ) as unknown as VaultIntent;
}

function nativeRoot(leaves: readonly Uint8Array[]): string {
  const hash = (parts: readonly Uint8Array[]) => {
    const state = createHash("sha256");
    for (const part of parts) state.update(part);
    return state.digest();
  };
  let nodes: Buffer[] = leaves.map((leaf) => hash([Buffer.of(0), leaf]));
  if (!nodes.length) return hash([]).toString("hex");
  // Independent bottom-up stack: promote odd subtrees unchanged, never duplicate.
  while (nodes.length > 1) {
    const next: Buffer[] = [];
    for (let index = 0; index < nodes.length; index += 2)
      next.push(
        index + 1 < nodes.length
          ? hash([Buffer.of(1), nodes[index]!, nodes[index + 1]!])
          : nodes[index]!,
      );
    nodes = next;
  }
  return nodes[0]!.toString("hex");
}

describe("exact intent and stamped receipt", () => {
  it("matches independent fixture bytes, signatures and hashes", () => {
    const intent = createPutIntent({
      seq: "1",
      key: "vault/lesson",
      content: bytes,
      prev_hash: fixtureGenesis,
      tags: ["weather", "lesson"],
    });
    const { ts_server, sig_agent, ...receivedIntent } = entries[0]!;
    expect(intent).toEqual(receivedIntent);
    expect(canonicalize(intent)).toBe(
      '{"content_hash":"b596e7d10b707fad2b71018e812b0fbc4a16a8539aadb0c6f8d4bad8f29284e2","content_ref":"sha256:b596e7d10b707fad2b71018e812b0fbc4a16a8539aadb0c6f8d4bad8f29284e2","content_type":"text/plain; charset=utf-8","key":"vault/lesson","op":"put","prev_hash":"f2746c9a731399cc623c322ea699a8e24ad29fc96dc373ef2d2d83a5eb478584","seq":"1","tags":["weather","lesson"]}',
    );
    expect(signVaultIntent(intent, key.privatePkcs8)).toBe(sig_agent);
    expect(stampVaultEntry({ intent, sig_agent, ts_server }, key.publicKeyJwk)).toEqual(entries[0]);
    expect(entries.map(hashVaultEntry)).toEqual(fixtureEntryHashes);
    const stamped = { ...entries[0]!, ts_server: "2026-01-01T00:00:00.001Z" };
    expect(verifyEd25519(canonicalBytes(intent), sig_agent, key.publicKeyJwk)).toBe(true);
    expect(hashVaultEntry(stamped)).not.toBe(fixtureEntryHashes[0]);
    expect(() =>
      stampVaultEntry({ intent, sig_agent, ts_server }, testKey(1).publicKeyJwk),
    ).toThrow(TypeError);
  });
  it("normalizes constructors only, preserving ciphertext and tag order", () => {
    const defaults = createPutIntent({
      seq: "9007199254740993",
      key: "sealed/opaque",
      content: Buffer.of(0, 255, 128),
      prev_hash: zero,
    });
    expect(defaults.seq).toBe("9007199254740993");
    expect(defaults.content_hash).toBe(
      createHash("sha256")
        .update(Buffer.of(0, 255, 128))
        .digest("hex"),
    );
    expect(defaults.content_type).toBe("text/plain; charset=utf-8");
    expect(defaults.tags).toEqual([]);
    const custom = createPutIntent({
      seq: "2",
      key: "public/x",
      content: Buffer.of(1),
      prev_hash: zero,
      content_type: "application/json",
      tags: ["z", "a", "z"],
    });
    expect(custom.tags).toEqual(["z", "a", "z"]);
    expect(custom.content_type).toBe("application/json");
    expect(
      createDeleteIntent({ seq: "2", key: "vault/lesson", prev_hash: fixtureEntryHashes[0] }),
    ).toEqual(unsignedFixture(entries[1]!));
    const exactSignature = signVaultIntent(defaults, key.privatePkcs8);
    expect(verifyEd25519(canonicalBytes(defaults), exactSignature, key.publicKeyJwk)).toBe(true);
    expect(
      verifyEd25519(
        canonicalBytes({ ...defaults, seq: "9007199254740992" }),
        exactSignature,
        key.publicKeyJwk,
      ),
    ).toBe(false);
  });
  it("rejects noncanonical received fields instead of normalizing signed bytes", () => {
    const intent = unsignedFixture(entries[0]!);
    const missing: Record<string, unknown> = { ...intent };
    delete missing.tags;
    const mutations: unknown[] = [
      missing,
      { ...intent, extra: 1 },
      { ...intent, seq: "01" },
      { ...intent, seq: "0" },
      { ...intent, seq: 1 },
      { ...intent, seq: "-1" },
      { ...intent, seq: "1e1" },
      { ...intent, key: "vault/" },
      { ...intent, key: "other/x" },
      { ...intent, content_hash: zero.toUpperCase().replace("0", "A") },
      { ...intent, prev_hash: "0" },
      { ...intent, content_ref: `sha256:${zero}` },
      { ...intent, content_type: "" },
      { ...intent, tags: [1] },
      { ...intent, tags: "a" },
      { ...intent, op: "append" },
    ];
    for (const bad of mutations)
      expect(() => signVaultIntent(bad as VaultIntent, key.privatePkcs8)).toThrow(TypeError);
    const tombstone = createDeleteIntent({ seq: "1", key: "vault/x", prev_hash: zero });
    for (const bad of [
      { ...tombstone, content_hash: zero },
      { ...tombstone, content_ref: `sha256:${tombstone.content_hash}` },
      { ...tombstone, tags: ["a"] },
      { ...tombstone, content_type: "text/plain" },
    ])
      expect(() => signVaultIntent(bad, key.privatePkcs8)).toThrow(TypeError);
    for (const ts_server of [
      "2026-02-30T00:00:00.000Z",
      "2026-01-01T00:00:60.000Z",
      "2026-01-01T00:00:00Z",
      "2026-01-01T00:00:00.000+00:00",
      "2026-13-01T00:00:00.000Z",
    ])
      expect(() => hashVaultEntry({ ...entries[0]!, ts_server })).toThrow(TypeError);
    for (const bad of [
      { ...entries[0]!, sig_agent: `${entries[0]!.sig_agent}=` },
      { ...entries[0]!, hash: zero },
      { ...entries[0]!, ts_server: undefined },
    ])
      expect(() => hashVaultEntry(bad as VaultEntry)).toThrow(TypeError);
    expect(() =>
      createPutIntent({
        seq: "1",
        key: "vault/x",
        content: "not bytes" as unknown as Uint8Array,
        prev_hash: zero,
      }),
    ).toThrow(TypeError);
    for (const metadata of [{ tags: "tags" }, { tags: null }, { content_type: null }])
      expect(() =>
        createPutIntent({
          seq: "1",
          key: "vault/x",
          content: Buffer.of(1),
          prev_hash: zero,
          ...metadata,
        } as unknown as Parameters<typeof createPutIntent>[0]),
      ).toThrow(TypeError);
  });
});

describe("complete externally pinned chains", () => {
  it("accepts literal put/delete/put and empty genesis only with exact pins", () => {
    expect(validateVaultChain(chain)).toEqual({
      valid: true,
      did,
      entries: 3,
      head_seq: "3",
      head_hash: fixtureHead,
    });
    expect(
      validateVaultChain({
        did,
        entries: [],
        keys: [],
        expectedHead: { seq: "0", head_hash: fixtureGenesis },
      }),
    ).toEqual({ valid: true, did, entries: 0, head_seq: "0", head_hash: fixtureGenesis });
    expect(
      validateVaultChain({ ...chain, entries: [], expectedHead: { seq: "0", head_hash: zero } })
        .valid,
    ).toBe(false);
    for (const altered of [
      { ...chain, did: "did:web:agentland.us:agents:another" },
      { ...chain, expectedHead: { seq: "2", head_hash: fixtureHead } },
      { ...chain, expectedHead: { seq: "3", head_hash: zero } },
      { ...chain, expectedHead: { seq: "03", head_hash: fixtureHead } },
      { ...chain, expectedHead: { seq: "9007199254740993", head_hash: fixtureHead } },
      { ...chain, entries: entries.slice(0, 2) },
      { ...chain, entries: [...entries].reverse() },
      { ...chain, entries: [entries[0]!, entries[0]!, entries[2]!] },
    ])
      expect(validateVaultChain(altered).valid).toBe(false);
  });
  it("detects each entry mutation and reports its index without content", () => {
    for (let index = 0; index < entries.length; index++) {
      for (const mutation of [
        { content_hash: zero },
        { prev_hash: zero },
        { sig_agent: testKey(1).vector.signature },
        { key: "vault/attacker" },
        { tags: ["altered"] },
        { ts_server: "2026-02-01T00:00:00.000Z" },
        { seq: "9" },
        { extra: "private-content-sentinel" },
      ]) {
        const altered = structuredClone(entries);
        Object.assign(altered[index]!, mutation);
        const result = validateVaultChain({ ...chain, entries: altered });
        expect(result.valid).toBe(false);
        if (!result.valid) {
          const expectedIndex =
            "ts_server" in mutation ? (index + 1 < entries.length ? index + 1 : undefined) : index;
          expect(result.error.index).toBe(expectedIndex);
          expect(JSON.stringify(result)).not.toContain("private-content-sentinel");
        }
      }
    }
  });
  it("requires unambiguous external key ranges, preserving exact BigInt bounds", () => {
    const other = testKey(1);
    const rotationKeys: VaultSigningKey[] = [
      { from_seq: "1", through_seq: "1", publicKeyJwk: key.publicKeyJwk },
      { from_seq: "2", through_seq: "9007199254740993", publicKeyJwk: other.publicKeyJwk },
    ];
    let previous = fixtureGenesis;
    const rotated = entries.map((entry, index) => {
      const ts_server = entry.ts_server;
      const intent = { ...unsignedFixture(entry), prev_hash: previous };
      const signer = index === 0 ? key : other;
      const result = stampVaultEntry(
        { intent, sig_agent: signVaultIntent(intent, signer.privatePkcs8), ts_server },
        signer.publicKeyJwk,
      );
      previous = hashVaultEntry(result);
      return result;
    });
    expect(
      validateVaultChain({
        did,
        entries: rotated,
        keys: rotationKeys,
        expectedHead: { seq: "3", head_hash: previous },
      }).valid,
    ).toBe(true);
    for (const ranges of [
      [],
      [keys[0]!, keys[0]!],
      [{ ...keys[0]!, from_seq: "2" }],
      [{ ...keys[0]!, from_seq: "01" }],
      [{ ...keys[0]!, through_seq: "0" }],
      [{ ...keys[0]!, through_seq: "1" }],
      [
        { ...keys[0]!, through_seq: "2" },
        { ...keys[0]!, from_seq: "2" },
      ],
      [
        { ...keys[0]!, through_seq: "1" },
        { ...keys[0]!, from_seq: "3" },
      ],
      [{ ...keys[0]!, publicKeyJwk: other.publicKeyJwk }],
      [{ ...keys[0]!, publicKeyJwk: { ...key.publicKeyJwk, d: "secret" } }],
    ])
      expect(validateVaultChain({ ...chain, keys: ranges }).valid).toBe(false);
  });
  it("covers deterministic chain lengths and every position mutation", () => {
    for (let length = 1; length <= 12; length++) {
      let previous = fixtureGenesis;
      const generated: VaultEntry[] = [];
      for (let index = 0; index < length; index++) {
        const intent =
          index % 3 === 1
            ? createDeleteIntent({ seq: String(index + 1), key: "vault/grid", prev_hash: previous })
            : createPutIntent({
                seq: String(index + 1),
                key: "vault/grid",
                content: Buffer.from(`memory-${index}`),
                prev_hash: previous,
              });
        const entry = stampVaultEntry(
          { intent, sig_agent: signVaultIntent(intent, key.privatePkcs8), ts_server: timestamp },
          key.publicKeyJwk,
        );
        generated.push(entry);
        previous = hashVaultEntry(entry);
      }
      const head = { seq: String(length), head_hash: previous };
      expect(validateVaultChain({ did, entries: generated, keys, expectedHead: head }).valid).toBe(
        true,
      );
      for (let index = 0; index < length; index++) {
        const altered = generated.map((entry, position) =>
          position === index ? { ...entry, key: "vault/tampered" } : entry,
        );
        expect(validateVaultChain({ did, entries: altered, keys, expectedHead: head }).valid).toBe(
          false,
        );
      }
    }
  });
});

describe("RFC6962 strict inclusion proofs", () => {
  it("matches independent published leaf and inclusion literals", () => {
    expect(merkleRoot([])).toBe(vectors.merkle.empty);
    expect(merkleRoot([new Uint8Array()])).toBe(vectors.merkle.emptyLeaf);
    expect(merkleRoot([Buffer.from("L123456")])).toBe(vectors.merkle.leafL123456);
    const published = vectors.merkle.inclusion;
    const proof = {
      leaf_index: published.leafIdx,
      tree_size: published.treeSize,
      siblings: published.proof.map((part) => Buffer.from(part, "base64").toString("hex")),
    };
    const root = Buffer.from(published.root, "base64").toString("hex");
    expect(verifyInclusionProof(new Uint8Array(), proof, root)).toBe(true);
    expect(verifyInclusionProof(Buffer.of(1), proof, root)).toBe(false);
    expect(merkleRoot(entries.map(canonicalBytes))).toBe(fixtureRoot);
    expect(createInclusionProof(entries.map(canonicalBytes), 1)).toEqual(fixtureMerkleProof);
  });
  it("checks all indices in sizes1..33 against independent native tree shape", () => {
    for (let size = 1; size <= 33; size++) {
      const leaves = Array.from({ length: size }, (_, index) => Buffer.from(`leaf-${index}`));
      const root = nativeRoot(leaves);
      expect(merkleRoot(leaves)).toBe(root);
      for (let index = 0; index < size; index++) {
        const proof = createInclusionProof(leaves, index);
        expect(verifyInclusionProof(leaves[index]!, proof, root)).toBe(true);
        expect(verifyInclusionProof(Buffer.from("tampered"), proof, root)).toBe(false);
        expect(
          verifyInclusionProof(
            leaves[index]!,
            { ...proof, siblings: [...proof.siblings, zero] },
            root,
          ),
        ).toBe(false);
        if (proof.siblings.length)
          expect(
            verifyInclusionProof(
              leaves[index]!,
              { ...proof, siblings: proof.siblings.slice(1) },
              root,
            ),
          ).toBe(false);
      }
    }
  });
  it("rejects malformed coordinates, root encodings and path lengths", () => {
    const leaf = canonicalBytes(entries[1]!);
    const proof = fixtureMerkleProof;
    for (const altered of [
      { ...proof, tree_size: 0 },
      { ...proof, leaf_index: -1 },
      { ...proof, leaf_index: 3 },
      { ...proof, leaf_index: 0.5 },
      { ...proof, tree_size: 3.5 },
      { ...proof, tree_size: Number.MAX_SAFE_INTEGER + 1 },
      { ...proof, leaf_index: Number.MAX_SAFE_INTEGER + 1 },
      { ...proof, siblings: [] },
      { ...proof, siblings: [...proof.siblings, zero] },
      { ...proof, siblings: [zero, "bad"] },
      { ...proof, siblings: "bad" },
      { ...proof, extra: true },
      null,
    ])
      expect(verifyInclusionProof(leaf, altered as typeof proof, fixtureRoot)).toBe(false);
    expect(verifyInclusionProof(leaf, proof, zero)).toBe(false);
    expect(verifyInclusionProof(leaf, proof, fixtureRoot.toUpperCase())).toBe(false);
    for (const index of [-1, 0.5, 3, NaN])
      expect(() => createInclusionProof(entries.map(canonicalBytes), index)).toThrow(RangeError);
    expect(() => createInclusionProof([], 0)).toThrow(RangeError);
    expect(() => merkleRoot(["bad" as unknown as Uint8Array])).toThrow(TypeError);
    expect(
      verifyInclusionProof(
        leaf,
        { leaf_index: 0, tree_size: Number.MAX_SAFE_INTEGER, siblings: [] },
        fixtureRoot,
      ),
    ).toBe(false);
    const largeIndex = 2 ** 40;
    const leafHash = createHash("sha256").update(Buffer.of(0)).update(leaf).digest();
    const trustedLargeRoot = createHash("sha256")
      .update(Buffer.of(1))
      .update(Buffer.from(zero, "hex"))
      .update(leafHash)
      .digest("hex");
    expect(
      verifyInclusionProof(
        leaf,
        { leaf_index: largeIndex, tree_size: largeIndex + 1, siblings: [zero] },
        trustedLargeRoot,
      ),
    ).toBe(true);
    expect(
      verifyInclusionProof(
        leaf,
        { leaf_index: 0, tree_size: largeIndex + 1, siblings: [zero] },
        trustedLargeRoot,
      ),
    ).toBe(false);
    expect(
      verifyInclusionProof(
        leaf,
        { ...proof, siblings: Array(54).fill(zero) as string[] },
        fixtureRoot,
      ),
    ).toBe(false);
  });
});

describe("bundle composition with external authority", () => {
  it("accepts exact second-entry proof and binds optional raw-root audit leaf", () => {
    expect(nativeRoot([canonicalBytes(entries[1]!)])).toBe(fixtureDailyRoot);
    const result = verifyVaultBundle(bundle, pins);
    expect(result).toEqual({
      valid: true,
      did,
      entries: 3,
      head_seq: "3",
      head_hash: fixtureHead,
      proved_seq: "2",
      root: fixtureDailyRoot,
    });
    const leaves = [
      Buffer.from("other leaf"),
      Buffer.from(fixtureDailyRoot, "hex"),
      Buffer.from("last leaf"),
    ];
    const audit = {
      vault_root_leaf_bytes: Buffer.from(fixtureDailyRoot, "hex").toString("base64url"),
      proof: createInclusionProof(leaves, 1),
    };
    const publishedRoot = merkleRoot(leaves);
    expect(verifyVaultBundle({ ...bundle, audit }, { ...pins, publishedRoot })).toEqual({
      ...result,
      root: publishedRoot,
    });
    expect(
      verifyVaultBundle(
        {
          ...bundle,
          audit: {
            ...audit,
            vault_root_leaf_bytes: Buffer.from(zero, "hex").toString("base64url"),
          },
        },
        { ...pins, publishedRoot },
      ).valid,
    ).toBe(false);
    expect(verifyVaultBundle({ ...bundle, audit }, pins).valid).toBe(false);
    expect(
      verifyVaultBundle(
        { ...bundle, proof: { seq: "2", ...fixtureMerkleProof } },
        { ...pins, publishedRoot: fixtureRoot },
      ).valid,
    ).toBe(false);
  });
  it("uses UTC-day leaves and coordinates without weakening the complete chain", () => {
    let previous = fixtureGenesis;
    const generated = [
      "2026-01-01T23:59:59.998Z",
      "2026-01-01T23:59:59.999Z",
      "2026-01-02T00:00:00.000Z",
      "2026-01-02T00:00:00.001Z",
      "2026-01-02T00:00:00.002Z",
    ].map((ts_server, index) => {
      const intent = createPutIntent({
        seq: String(index + 1),
        key: "vault/daily",
        content: Buffer.from(`memory-${index}`),
        prev_hash: previous,
      });
      const entry = stampVaultEntry(
        { intent, sig_agent: signVaultIntent(intent, key.privatePkcs8), ts_server },
        key.publicKeyJwk,
      );
      previous = hashVaultEntry(entry);
      return entry;
    });
    const head = { seq: "5", head_hash: previous };
    const firstDay = generated.slice(0, 2).map(canonicalBytes);
    const secondDay = generated.slice(2).map(canonicalBytes);
    const root = nativeRoot(secondDay);
    const dailyBundle: VaultProofBundle = {
      format: "agentland-vault/1",
      did,
      entries: generated,
      proof: { seq: "3", ...createInclusionProof(secondDay, 0) },
    };
    const dailyPins = { keys, expectedHead: head, publishedRoot: root };
    expect(dailyBundle.proof).toEqual({
      seq: "3",
      leaf_index: 0,
      tree_size: 3,
      siblings: createInclusionProof(secondDay, 0).siblings,
    });
    expect(verifyVaultBundle(dailyBundle, dailyPins)).toEqual({
      valid: true,
      did,
      entries: 5,
      head_seq: "5",
      head_hash: previous,
      proved_seq: "3",
      root,
    });
    for (const siblings of [
      dailyBundle.proof.siblings.slice(1),
      [...dailyBundle.proof.siblings, zero],
    ])
      expect(
        verifyVaultBundle({ ...dailyBundle, proof: { ...dailyBundle.proof, siblings } }, dailyPins),
      ).toEqual({ valid: false, error: { stage: "proof", reason: "invalid-entry-path" } });
    for (const [offset, leaves] of [
      [0, firstDay],
      [2, secondDay],
    ] as const)
      for (let index = 0; index < leaves.length; index++)
        expect(
          verifyVaultBundle(
            {
              ...dailyBundle,
              proof: { seq: String(offset + index + 1), ...createInclusionProof(leaves, index) },
            },
            { ...dailyPins, publishedRoot: nativeRoot(leaves) },
          ).valid,
        ).toBe(true);
    for (const leaves of [generated.slice(0, 3).map(canonicalBytes), generated.map(canonicalBytes)])
      expect(
        verifyVaultBundle(
          { ...dailyBundle, proof: { seq: "3", ...createInclusionProof(leaves, 2) } },
          { ...dailyPins, publishedRoot: nativeRoot(leaves) },
        ).valid,
      ).toBe(false);
    expect(
      verifyVaultBundle(dailyBundle, { ...dailyPins, publishedRoot: nativeRoot(firstDay) }).valid,
    ).toBe(false);
    const partialDay = secondDay.slice(0, 1);
    expect(
      verifyVaultBundle(
        { ...dailyBundle, proof: { seq: "3", ...createInclusionProof(partialDay, 0) } },
        { ...dailyPins, publishedRoot: nativeRoot(partialDay) },
      ).valid,
    ).toBe(false);
    const altered = [...generated];
    altered[0] = { ...altered[0]!, ts_server: "2026-01-01T23:59:59.997Z" };
    expect(altered.slice(2).map(canonicalBytes)).toEqual(secondDay);
    expect(verifyVaultBundle({ ...dailyBundle, entries: altered }, dailyPins)).toEqual({
      valid: false,
      error: { stage: "chain", reason: "broken-hash-link", index: 1 },
    });
    const outerLeaves = [Buffer.from(root, "hex"), Buffer.from("other daily root")];
    const audit = {
      vault_root_leaf_bytes: outerLeaves[0]!.toString("base64url"),
      proof: createInclusionProof(outerLeaves, 0),
    };
    const outerPins = { ...dailyPins, publishedRoot: nativeRoot(outerLeaves) };
    expect(verifyVaultBundle({ ...dailyBundle, audit }, outerPins).valid).toBe(true);
    expect(
      verifyVaultBundle(
        {
          ...dailyBundle,
          audit: {
            ...audit,
            vault_root_leaf_bytes: Buffer.from(nativeRoot(firstDay), "hex").toString("base64url"),
          },
        },
        outerPins,
      ).valid,
    ).toBe(false);
  });
  it("rejects malformed bundle schema, missing authority and mismatched selection", () => {
    for (const bad of [
      { ...bundle, format: "other" },
      { ...bundle, keys },
      { ...bundle, proof: { ...bundle.proof, seq: "1" } },
      { ...bundle, proof: { ...bundle.proof, seq: "4" } },
      { ...bundle, proof: { ...bundle.proof, tree_size: 2 } },
      { ...bundle, proof: { ...bundle.proof, siblings: [zero] } },
      { ...bundle, audit: {} },
      null,
    ])
      expect(verifyVaultBundle(bad as VaultProofBundle, pins).valid).toBe(false);
    expect(verifyVaultBundle(bundle, { ...pins, publishedRoot: zero }).valid).toBe(false);
    expect(
      verifyVaultBundle(bundle, {
        ...pins,
        expectedHead: { seq: "2", head_hash: fixtureEntryHashes[1] },
      }).valid,
    ).toBe(false);
    expect(verifyVaultBundle(bundle, {} as typeof pins).valid).toBe(false);
    expect(sha256Hex(Buffer.from(did))).toBe(fixtureGenesis);
  });
});
