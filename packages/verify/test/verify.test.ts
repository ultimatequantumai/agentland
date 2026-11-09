import { describe, expect, it, vi } from "vitest";
import * as identity from "@agentland/identity";
import * as verify from "../src/index.js";
import { resolveDid } from "../src/index.js";
import { testKey, timestamp } from "../../identity/test/helpers.js";
import { fixtureRoot } from "../../identity/test/fixtures/oracle.js";
import { readFileSync } from "node:fs";
import {
  EXPORT_LAYOUT,
  SEALED_CONTENT_TYPE,
  buildExportManifest,
  canonicalBytes,
  createDeleteIntent,
  createInclusionProof,
  createPutIntent,
  hashVaultEntry,
  merkleRoot,
  sha256Hex,
  signVaultHead,
  signVaultIntent,
  stampVaultEntry,
  validateVaultChain,
  writeUstar,
} from "@agentland/identity";
import type { ArchiveFile, VaultEntry, VaultIntent } from "@agentland/identity";
import { verifyChainAnchor, verifyVaultExport } from "../src/index.js";

// D-38 / CITIZEN-20: what a third party needs with only `fetch`. The source entry is
// imported because the root test run builds identity, not this package; the re-exports
// still resolve to identity's published entry, so `===` pins them to the same functions.
const key = testKey();
const aliceDid = "did:web:agentland.us:agents:alice";
const aliceDocument = identity.buildDidDocument({
  handle: "alice",
  keys: [
    {
      id: `${aliceDid}#key-1`,
      publicKeyJwk: key.publicKeyJwk,
      purpose: "signing",
      activated_at: timestamp,
    },
  ],
});
/** Labelled fixture: the platform DID document shape, issuer key `#vc-1` (test key). */
const platformDocument = {
  "@context": ["https://www.w3.org/ns/did/v1", "https://w3id.org/security/suites/jws-2020/v1"],
  id: "did:web:agentland.us",
  verificationMethod: [
    {
      id: "did:web:agentland.us#vc-1",
      controller: "did:web:agentland.us",
      type: "JsonWebKey2020",
      publicKeyJwk: key.publicKeyJwk,
    },
  ],
  assertionMethod: ["did:web:agentland.us#vc-1"],
};

function fakeFetch(body: string, status = 200) {
  return vi.fn<typeof fetch>(
    async () => new Response(body, { status, headers: { "content-type": "application/json" } }),
  );
}

describe("@agentland/verify re-exports", () => {
  it("re-exports the six offline verifiers of @agentland/identity unchanged", () => {
    for (const name of [
      "verifyNonceSignature",
      "buildDidHistory",
      "verifyCredential",
      "verifyVaultBundle",
      "verifySignedHead",
      "verifyInclusionProof",
    ] as const) {
      expect(typeof verify[name], name).toBe("function");
      expect(verify[name], name).toBe(identity[name]);
    }
  });

  it("verifies an AgentLand credential through the re-export", () => {
    const kid = "did:web:agentland.us#vc-1";
    const compact = identity.issueCredential({
      id: "urn:uuid:0f223836-2222-4444-8888-777777777777",
      subjectDid: aliceDid,
      type: "Calibrated",
      evidence: { season: "alltime", n: 200, shrunk_edge: 0.025, audit_root: fixtureRoot },
      validFrom: timestamp,
      issuerKeyId: kid,
      privatePkcs8: key.privatePkcs8,
    });
    const options = {
      trustedIssuer: { issuer: "did:web:agentland.us", kid, publicKeyJwk: key.publicKeyJwk },
      expectedSubjectDid: aliceDid,
      now: timestamp,
    };
    expect(verify.verifyCredential(compact, options).valid).toBe(true);
    expect(verify.verifyCredential(compact, { ...options, expectedSubjectDid: "x" }).valid).toBe(
      false,
    );
  });
});

describe("resolveDid", () => {
  it("maps an agent DID to its did.json and returns the parsed document", async () => {
    const fetchFn = fakeFetch(JSON.stringify(aliceDocument));
    await expect(resolveDid(aliceDid, fetchFn)).resolves.toEqual(aliceDocument);
    expect(fetchFn).toHaveBeenCalledTimes(1);
    expect(String(fetchFn.mock.calls[0]![0])).toBe("https://agentland.us/agents/alice/did.json");
  });

  it("maps the platform DID to /.well-known/did.json", async () => {
    const fetchFn = fakeFetch(JSON.stringify(platformDocument));
    await expect(resolveDid("did:web:agentland.us", fetchFn)).resolves.toEqual(platformDocument);
    expect(fetchFn).toHaveBeenCalledTimes(1);
    expect(String(fetchFn.mock.calls[0]![0])).toBe("https://agentland.us/.well-known/did.json");
  });

  it("refuses non-agentland DIDs without fetching", async () => {
    for (const did of [
      "did:web:example.com",
      "did:web:agentland.us.evil.test",
      "did:web:agentland.us%3A8080",
      "did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnEGta2doK",
      "did:web:agentland.us:agents:../admin",
      "did:web:agentland.us:agents:alice:extra",
      "did:web:agentland.us:agents:Alice",
      "did:web:agentland.us:other:alice",
      "",
    ]) {
      const fetchFn = fakeFetch(JSON.stringify(aliceDocument));
      await expect(resolveDid(did, fetchFn), did).rejects.toThrow(TypeError);
      expect(fetchFn, did).not.toHaveBeenCalled();
    }
  });

  it("requires HTTP 200", async () => {
    for (const status of [404, 203, 500])
      await expect(
        resolveDid(aliceDid, fakeFetch(JSON.stringify(aliceDocument), status)),
        String(status),
      ).rejects.toThrow(TypeError);
  });

  it("requires strict JSON", async () => {
    for (const body of [
      "<html>not json</html>",
      "",
      `{"id":"${aliceDid}","id":"${aliceDid}"}`,
      JSON.stringify(aliceDocument).slice(0, -1),
    ])
      await expect(resolveDid(aliceDid, fakeFetch(body)), body).rejects.toThrow(TypeError);
  });

  it("rejects a document whose id is not the requested DID", async () => {
    for (const document of [
      { ...aliceDocument, id: "did:web:agentland.us:agents:mallory" },
      { ...aliceDocument, id: undefined },
      [aliceDocument],
      null,
    ])
      await expect(resolveDid(aliceDid, fakeFetch(JSON.stringify(document)))).rejects.toThrow(
        TypeError,
      );
    await expect(
      resolveDid("did:web:agentland.us", fakeFetch(JSON.stringify(aliceDocument))),
    ).rejects.toThrow(TypeError);
  });

  it("uses only the caller's fetch, never globalThis.fetch", async () => {
    const ambient = vi
      .spyOn(globalThis, "fetch")
      .mockRejectedValue(new Error("ambient fetch used"));
    await expect(resolveDid(aliceDid, fakeFetch(JSON.stringify(aliceDocument)))).resolves.toEqual(
      aliceDocument,
    );
    await expect(resolveDid(aliceDid, fakeFetch("", 404))).rejects.toThrow(TypeError);
    expect(ambient).not.toHaveBeenCalled();
  });
});

// 15-16 (D-20, PRIVATE-05): the offline export fixture. One plain put, one sealed put
// carrying the frozen V1 envelope, one delete; proofs for the 2026-11-01 daily root.
interface SealedVector {
  readonly did: string;
  readonly key: string;
  readonly envelope_hex: string;
  readonly envelope_sha256: string;
  readonly recipient_key_id: string;
}
function sealedVector(): SealedVector {
  const raw = readFileSync(
    new URL("../../identity/test/sealed-vectors.json", import.meta.url),
    "utf8",
  );
  return (JSON.parse(raw) as unknown as { readonly v1: SealedVector }).v1;
}
const HEAD_KID = "did:web:agentland.us#head-key-1";
const utf8 = (text: string): Uint8Array => Buffer.from(text, "utf8");

interface ExportOptions {
  /** Overrides for entry 2's sealed put; the entry is re-signed so only the overridden value differs. */
  readonly sealed?: {
    readonly content?: Uint8Array;
    readonly content_type?: string;
    readonly tags?: readonly string[];
  };
  /** Applied to the stamped entries before they are written (the chain is not re-linked). */
  readonly entries?: (entries: VaultEntry[]) => VaultEntry[];
  /** Applied to the members before the manifest is computed. */
  readonly members?: (files: ArchiveFile[]) => ArchiveFile[];
  /** Applied to the members after the manifest is computed (the manifest goes stale). */
  readonly stale?: (files: ArchiveFile[]) => ArchiveFile[];
}
interface BuiltExport {
  readonly did: string;
  readonly tar: Uint8Array;
  readonly headHash: string;
  readonly envelope: Uint8Array;
  readonly entries: readonly VaultEntry[];
  readonly pins: {
    readonly keys: readonly {
      readonly from_seq: string;
      readonly publicKeyJwk: ReturnType<typeof testKey>["publicKeyJwk"];
    }[];
    readonly headKeys: readonly {
      readonly kid: string;
      readonly publicKeyJwk: ReturnType<typeof testKey>["publicKeyJwk"];
    }[];
    readonly auditRoots: Readonly<Record<string, string>>;
  };
}

function buildExport(options: ExportOptions = {}): BuiltExport {
  const vector = sealedVector();
  const did = vector.did;
  const agent = testKey(0);
  const head = testKey(1);
  const envelope = new Uint8Array(Buffer.from(vector.envelope_hex, "hex"));
  const sealedContent = options.sealed?.content ?? envelope;
  const stamp = (intent: VaultIntent, ts_server: string): VaultEntry =>
    stampVaultEntry(
      { intent, sig_agent: signVaultIntent(intent, agent.privatePkcs8), ts_server },
      agent.publicKeyJwk,
    );
  let prev = sha256Hex(utf8(did));
  const stamped: VaultEntry[] = [];
  const intents: readonly ((prev_hash: string) => VaultIntent)[] = [
    (prev_hash) =>
      createPutIntent({
        seq: "1",
        key: "vault/notes",
        content: utf8("lesson: check the radar"),
        prev_hash,
      }),
    (prev_hash) =>
      createPutIntent({
        seq: "2",
        key: vector.key,
        content: sealedContent,
        prev_hash,
        content_type: options.sealed?.content_type ?? SEALED_CONTENT_TYPE,
        tags: options.sealed?.tags ?? [],
      }),
    (prev_hash) => createDeleteIntent({ seq: "3", key: "vault/notes", prev_hash }),
  ];
  const stamps: readonly string[] = [
    "2026-11-01T10:00:00.000Z",
    "2026-11-01T11:00:00.000Z",
    "2026-11-02T09:00:00.000Z",
  ];
  for (const [index, build] of intents.entries()) {
    stamped.push(stamp(build(prev), stamps[index]!));
    prev = hashVaultEntry(stamped.at(-1)!);
  }
  const entries = options.entries ? options.entries(stamped) : stamped;
  const signedHead = signVaultHead(
    { did, seq: "3", head_hash: prev, ts: "2026-11-02T09:00:01.000Z", kid: HEAD_KID },
    head.privatePkcs8,
  );
  const leaves: Uint8Array[] = entries.slice(0, 2).map((entry) => canonicalBytes(entry));
  const vaultRoot = merkleRoot(leaves);
  const vaultRootBytes = new Uint8Array(Buffer.from(vaultRoot, "hex"));
  const auditLeaves: Uint8Array[] = [vaultRootBytes, new Uint8Array(32).fill(7)];
  const auditRoot = merkleRoot(auditLeaves);
  const proofs: ArchiveFile[] = ["1", "2"].map((seq, index) => ({
    name: EXPORT_LAYOUT.proof(seq),
    bytes: canonicalBytes({
      seq,
      date: "2026-11-01",
      root: vaultRoot,
      proof: createInclusionProof(leaves, index),
      audit_root: auditRoot,
      audit: {
        vault_root_leaf_bytes: Buffer.from(vaultRootBytes).toString("base64url"),
        proof: createInclusionProof(auditLeaves, 0),
      },
    }),
  }));
  let members: ArchiveFile[] = [
    { name: EXPORT_LAYOUT.didHistory, bytes: canonicalBytes({ did, keys: [] }) },
    { name: EXPORT_LAYOUT.head, bytes: canonicalBytes(signedHead) },
    { name: EXPORT_LAYOUT.record, bytes: canonicalBytes({ did }) },
    ...entries.map((entry) => ({
      name: EXPORT_LAYOUT.entry(entry.seq),
      bytes: canonicalBytes(entry),
    })),
    { name: EXPORT_LAYOUT.payload("1"), bytes: utf8("lesson: check the radar") },
    { name: EXPORT_LAYOUT.payload("2"), bytes: sealedContent },
    ...proofs,
  ];
  if (options.members) members = options.members(members);
  const manifest = buildExportManifest({ did, files: members });
  if (options.stale) members = options.stale(members);
  const tar = new Uint8Array(
    Buffer.concat([
      ...writeUstar([
        { name: EXPORT_LAYOUT.manifest, bytes: canonicalBytes(manifest) },
        ...members,
      ]),
    ]),
  );
  return {
    did,
    tar,
    headHash: prev,
    envelope,
    entries,
    pins: {
      keys: [{ from_seq: "1", publicKeyJwk: agent.publicKeyJwk }],
      headKeys: [{ kid: HEAD_KID, publicKeyJwk: head.publicKeyJwk }],
      auditRoots: { "2026-11-01": auditRoot },
    },
  };
}

function flipByte(files: ArchiveFile[], name: string, at: number): ArchiveFile[] {
  return files.map((file) => {
    if (file.name !== name) return file;
    const bytes = new Uint8Array(file.bytes);
    bytes[at] = bytes[at]! ^ 1;
    return { name, bytes };
  });
}

function throwsWith(fn: () => unknown, Class: new (message: string) => Error, message: string) {
  expect(fn).toThrow(Class);
  expect(fn).toThrow(message);
}

describe("15-16 sealed export", () => {
  it("verifies an export with a sealed payload and returns it unopened", () => {
    const built = buildExport();
    const vector = sealedVector();
    const result = verifyVaultExport(built.tar, built.pins);
    expect(result).toEqual({
      valid: true,
      did: built.did,
      head_seq: "3",
      head_hash: built.headHash,
      entries: 3,
      proved: ["1", "2"],
      sealed: [
        {
          seq: "2",
          key: vector.key,
          recipient_key_id: "f35e5616160a30bf3c6e79fa73c576d40205e8fc3ba4e1c6dcf93e6b98e857b4",
          envelope: built.envelope,
        },
      ],
    });
    if (!result.valid) throw new Error("expected a valid export");
    expect(sha256Hex(result.sealed[0]!.envelope)).toBe(
      "142141121a3f4f341083806ec715c64d2cb1cdedffc9ef35d560269955c32838",
    );
  });

  it("a flipped ciphertext byte fails before any open", () => {
    const built = buildExport({ members: (files) => flipByte(files, "payloads/2.bin", 200) });
    const result = verifyVaultExport(built.tar, built.pins);
    expect(result).toEqual({
      valid: false,
      error: { stage: "payload", reason: "digest-mismatch", index: 2 },
    });
    expect(Object.hasOwn(result, "sealed")).toBe(false);
  });

  it("a flipped byte without a recomputed manifest fails at the manifest", () => {
    const built = buildExport({ stale: (files) => flipByte(files, "payloads/2.bin", 200) });
    expect(verifyVaultExport(built.tar, built.pins)).toEqual({
      valid: false,
      error: { stage: "archive", reason: "manifest-mismatch" },
    });
  });

  it("a sealed entry needs the fixed outer type, empty tags and a valid envelope", () => {
    const envelope = new Uint8Array(Buffer.from(sealedVector().envelope_hex, "hex"));
    const variants: readonly ExportOptions["sealed"][] = [
      { content_type: "text/plain; charset=utf-8" },
      { tags: ["macro"] },
      { content: envelope.slice(0, 363) },
    ];
    for (const [index, sealed] of variants.entries()) {
      const built = buildExport({ sealed });
      expect(verifyVaultExport(built.tar, built.pins), `variant ${index}`).toEqual({
        valid: false,
        error: { stage: "payload", reason: "sealed-envelope", index: 2 },
      });
    }
  });

  it("a purged sealed payload is absent and the export still verifies", () => {
    const built = buildExport({
      members: (files) => files.filter((file) => file.name !== "payloads/2.bin"),
    });
    const result = verifyVaultExport(built.tar, built.pins);
    expect(result).toMatchObject({ valid: true, sealed: [], proved: ["1", "2"] });
  });

  it("a payload for a delete or unknown seq is an orphan", () => {
    const built = buildExport({
      members: (files) => [...files, { name: "payloads/3.bin", bytes: utf8("resurrected") }],
    });
    expect(verifyVaultExport(built.tar, built.pins)).toEqual({
      valid: false,
      error: { stage: "payload", reason: "orphan", index: 3 },
    });
  });

  it("an unknown member is refused", () => {
    const built = buildExport({
      members: (files) => [...files, { name: "notes.txt", bytes: utf8("hello") }],
    });
    expect(verifyVaultExport(built.tar, built.pins)).toEqual({
      valid: false,
      error: { stage: "archive", reason: "unknown-member" },
    });
    expect(verifyVaultExport(new Uint8Array(utf8("not a tar archive")), built.pins)).toEqual({
      valid: false,
      error: { stage: "archive", reason: "unreadable" },
    });
  });

  it("the head must verify under a pinned vault-head key", () => {
    const built = buildExport();
    const other = testKey(2).publicKeyJwk;
    expect(
      verifyVaultExport(built.tar, {
        ...built.pins,
        headKeys: [
          {
            kid: "did:web:agentland.us#head-key-2",
            publicKeyJwk: built.pins.headKeys[0]!.publicKeyJwk,
          },
        ],
      }),
    ).toEqual({ valid: false, error: { stage: "head", reason: "untrusted-kid" } });
    expect(
      verifyVaultExport(built.tar, {
        ...built.pins,
        headKeys: [{ kid: HEAD_KID, publicKeyJwk: other }],
      }),
    ).toEqual({ valid: false, error: { stage: "head", reason: "invalid-signature" } });
  });

  it("a broken chain fails with the chain validator's own error", () => {
    const tamper = (entries: VaultEntry[]): VaultEntry[] =>
      entries.map((entry, index) =>
        index === 0 ? { ...entry, sig_agent: entries[1]!.sig_agent } : entry,
      );
    const built = buildExport({ entries: tamper });
    const result = verifyVaultExport(built.tar, built.pins);
    expect(result.valid).toBe(false);
    expect(result).toEqual(
      validateVaultChain({
        did: built.did,
        entries: built.entries,
        keys: built.pins.keys,
        expectedHead: { seq: "3", head_hash: built.headHash },
      }),
    );
    if (result.valid) throw new Error("expected a chain failure");
    expect(result.error.stage).not.toBe("payload");
  });

  it("proofs verify only against pinned audit roots", () => {
    const built = buildExport();
    expect(verifyVaultExport(built.tar, { ...built.pins, auditRoots: {} })).toEqual({
      valid: false,
      error: { stage: "proof", reason: "unpinned-audit-root", index: 1 },
    });
    expect(
      verifyVaultExport(built.tar, {
        ...built.pins,
        auditRoots: { "2026-11-01": "ab".repeat(32) },
      }),
    ).toEqual({ valid: false, error: { stage: "proof", reason: "audit-root-mismatch", index: 1 } });
  });

  it("never decrypts", () => {
    const source = readFileSync(new URL("../src/index.ts", import.meta.url), "utf8");
    for (const name of ["openSealedEntry", "sealEntry", "generateEncryptionKey"])
      expect(source.includes(name), name).toBe(false);
    expect(verifyVaultExport.length).toBe(2);
  });

  it("rejects invalid pins with a TypeError", () => {
    const built = buildExport();
    const message = "Vault export pins required: keys, headKeys, auditRoots";
    const bad: readonly unknown[] = [
      { keys: [] },
      { ...built.pins, extra: 1 },
      { ...built.pins, auditRoots: { "2026-11-1": "00".repeat(32) } },
    ];
    for (const pins of bad)
      throwsWith(
        () => verifyVaultExport(built.tar, pins as unknown as BuiltExport["pins"]),
        TypeError,
        message,
      );
  });
});

// 15-16 (D-51, C-25, C-26, PRIVATE-12): vector A1 (RESEARCH F9) as two providers return it.
const A1_ADDRESS = "0x9d8a62f656a8d1615c1294fd71e9cfb3e4855a4f";
const A1_HASH = "0xc0ba6352432050a717a811998b6c69c56ca1196ff0087e61037e32e7ec17f8dd";
const A1_R = "0x462672e160765bc87519449f71de08bdd8991ab7e67ada152c218851947290ba";
const A1_S = "0x298849a5390838682e48f7ae473d950e551590a6e17088068bceb3ed02f7d266";
const A1_HIGH_S = "0xd677b65ac6f7c797d1b70851b8c26af065994c3fcdd818353403aa9fcd3e6edb";
const A1_INPUT =
  "0x6167656e746c616e642d61756469742d726f6f742f3120323032362d31312d30322039663361" +
  "30".repeat(60);
const NOTARY = { chain_id: 1, address: A1_ADDRESS } as const;
type Json = Record<string, unknown>;
const ROOT: Json = {
  date: "2026-11-02",
  root: "9f3a" + "0".repeat(60),
  prev_root: "0".repeat(64),
  published_at: "2026-11-03T00:05:00.000Z",
  anchor_status: "confirmed",
  block_height: 871204,
  chain_anchor_status: "confirmed",
  chain_anchor: { chain_id: 1, tx_hash: A1_HASH, block_number: 21904117 },
};
const TX: Json = {
  type: "0x2",
  chainId: "0x1",
  nonce: "0x0",
  maxPriorityFeePerGas: "0x3b9aca00",
  maxFeePerGas: "0x4a817c800",
  gas: "0x6158",
  to: A1_ADDRESS,
  value: "0x0",
  input: A1_INPUT,
  accessList: [],
  yParity: "0x1",
  v: "0x1",
  r: A1_R,
  s: A1_S,
  hash: A1_HASH,
  from: A1_ADDRESS,
  blockNumber: "0x14e3af5",
  blockHash: "0x" + "ab".repeat(32),
  transactionIndex: "0x0",
};
// A second provider's shape: no yParity/from/transactionIndex, upper-case hex in r.
const ETHERSCAN: Json = {
  ...Object.fromEntries(
    Object.entries(TX).filter(([name]) => !["yParity", "from", "transactionIndex"].includes(name)),
  ),
  r: "0x" + A1_R.slice(2).toUpperCase(),
};
const anchorOf = (overrides: Json): Json => ({
  ...ROOT,
  chain_anchor: { ...(ROOT.chain_anchor as Json), ...overrides },
});
const failure = (stage: string, reason: string) => ({ valid: false, error: { stage, reason } });

describe("15-16 verifyChainAnchor", () => {
  it("vector A1 verifies from two providers' JSON", () => {
    const expected = {
      valid: true,
      chain_id: 1,
      tx_hash: A1_HASH,
      block_number: 21904117,
      from: A1_ADDRESS,
    };
    expect(verifyChainAnchor(ROOT, TX, NOTARY)).toEqual(expected);
    expect(verifyChainAnchor(ROOT, ETHERSCAN, NOTARY)).toEqual(expected);
  });

  it("a payload transaction to the notary from another address fails", () => {
    const s = "0x" + (BigInt(A1_S) - 1n).toString(16);
    expect(s).not.toBe(A1_S);
    expect(verifyChainAnchor(ROOT, { ...TX, s, from: A1_ADDRESS }, NOTARY)).toEqual(
      failure("transaction", "signature"),
    );
  });

  it("a high-s copy fails", () => {
    expect(
      verifyChainAnchor(ROOT, { ...TX, s: A1_HIGH_S, yParity: "0x0", v: "0x0" }, NOTARY),
    ).toEqual(failure("transaction", "signature"));
  });

  it("chain, value, destination and payload use the anchor guard's reasons", () => {
    expect(verifyChainAnchor(ROOT, { ...TX, chainId: "0xaa36a7" }, NOTARY)).toEqual(
      failure("transaction", "chain"),
    );
    expect(verifyChainAnchor(ROOT, { ...TX, value: "0x1" }, NOTARY)).toEqual(
      failure("transaction", "value"),
    );
    expect(verifyChainAnchor(ROOT, TX, { chain_id: 1, address: "0x" + "11".repeat(20) })).toEqual(
      failure("transaction", "destination"),
    );
    expect(verifyChainAnchor({ ...ROOT, root: "9f3b" + "0".repeat(60) }, TX, NOTARY)).toEqual(
      failure("transaction", "payload"),
    );
    expect(verifyChainAnchor({ ...ROOT, date: "2026-11-03" }, TX, NOTARY)).toEqual(
      failure("transaction", "payload"),
    );
  });

  it("hashes, sender claims and blocks must agree", () => {
    expect(verifyChainAnchor(ROOT, { ...TX, hash: "0x" + "00".repeat(32) }, NOTARY)).toEqual(
      failure("transaction", "hash-mismatch"),
    );
    expect(verifyChainAnchor(ROOT, { ...TX, from: "0x" + "22".repeat(20) }, NOTARY)).toEqual(
      failure("transaction", "from-mismatch"),
    );
    expect(verifyChainAnchor(anchorOf({ tx_hash: "0x" + "00".repeat(32) }), TX, NOTARY)).toEqual(
      failure("root", "tx-hash-mismatch"),
    );
    expect(verifyChainAnchor(ROOT, { ...TX, blockNumber: "0x14e3af6" }, NOTARY)).toEqual(
      failure("root", "block-mismatch"),
    );
    expect(verifyChainAnchor(ROOT, { ...TX, blockNumber: null }, NOTARY)).toEqual(
      failure("transaction", "pending"),
    );
  });

  it("only a confirmed anchor on the pinned chain is checked", () => {
    expect(verifyChainAnchor({ ...ROOT, chain_anchor_status: "pending" }, TX, NOTARY)).toEqual(
      failure("root", "not-confirmed"),
    );
    expect(verifyChainAnchor({ ...ROOT, chain_anchor: null }, TX, NOTARY)).toEqual(
      failure("root", "not-confirmed"),
    );
    expect(verifyChainAnchor(anchorOf({ chain_id: 11155111 }), TX, NOTARY)).toEqual(
      failure("root", "chain-mismatch"),
    );
    const rootless = Object.fromEntries(Object.entries(ROOT).filter(([name]) => name !== "root"));
    expect(verifyChainAnchor(rootless, TX, NOTARY)).toEqual(
      failure("root", "invalid-root-document"),
    );
  });

  it("an impossible calendar date is an invalid root document, not a throw", () => {
    const impossible = { ...ROOT, date: "2026-02-29" };
    expect(() => verifyChainAnchor(impossible, TX, NOTARY)).not.toThrow();
    expect(verifyChainAnchor(impossible, TX, NOTARY)).toEqual(
      failure("root", "invalid-root-document"),
    );
  });

  it("malformed transaction JSON is refused", () => {
    const bad: readonly unknown[] = [
      { ...TX, type: "0x0" },
      { ...TX, accessList: [{ address: A1_ADDRESS, storageKeys: [] }] },
      { ...TX, nonce: "0x00" },
      { ...TX, input: "0x6" },
      { ...TX, yParity: "0x1", v: "0x0" },
      "not a transaction",
    ];
    for (const [index, transaction] of bad.entries())
      expect(verifyChainAnchor(ROOT, transaction, NOTARY), `case ${index}`).toEqual(
        failure("transaction", "invalid-transaction-json"),
      );
  });

  it("rejects an invalid notary pin with a TypeError", () => {
    const message = "Chain anchor notary pin required: chain_id, address";
    const bad: readonly unknown[] = [
      { chain_id: 0, address: A1_ADDRESS },
      { chain_id: 1, address: "0x" + A1_ADDRESS.slice(2).toUpperCase() },
      { chain_id: 1 },
    ];
    for (const notary of bad)
      throwsWith(
        () => verifyChainAnchor(ROOT, TX, notary as unknown as typeof NOTARY),
        TypeError,
        message,
      );
  });

  it("uses no network", () => {
    const ambient = vi
      .spyOn(globalThis, "fetch")
      .mockRejectedValue(new Error("ambient fetch used"));
    try {
      const built = buildExport();
      expect(verifyVaultExport(built.tar, built.pins).valid).toBe(true);
      expect(verifyChainAnchor(ROOT, TX, NOTARY).valid).toBe(true);
      expect(verifyChainAnchor(ROOT, ETHERSCAN, NOTARY).valid).toBe(true);
      expect(ambient).not.toHaveBeenCalled();
    } finally {
      ambient.mockRestore();
    }
  });
});
