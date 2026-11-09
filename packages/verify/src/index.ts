import { parseIJson } from "@agentland/identity";
import type { DidDocument } from "@agentland/identity";
import {
  AnchorGuardError,
  EXPORT_LAYOUT,
  SEALED_CONTENT_TYPE,
  anchorPayload,
  canonicalBytes,
  readUstar,
  sealedEnvelopeRecipient,
  serializeAnchorTransaction,
  sha256Hex,
  validateVaultChain,
  verifyAnchorTransaction,
  verifySignedHead as checkHead,
  verifyVaultBundle as checkBundle,
} from "@agentland/identity";
import type {
  AnchorTransactionFields,
  Ed25519PublicJwk as HeadJwk,
  MerkleProof,
  SignedVaultHead,
  VaultEntry,
  VaultProofBundle,
  VaultSigningKey as SigningKey,
  VerificationFailure,
} from "@agentland/identity";

export {
  buildDidHistory,
  verifyCredential,
  verifyInclusionProof,
  verifyNonceSignature,
  verifySignedHead,
  verifyVaultBundle,
} from "@agentland/identity";
export type {
  AgentLandCredential,
  CredentialType,
  CredentialVerification,
  DidDocument,
  DidHistory,
  Ed25519PublicJwk,
  MerkleProof,
  PublicJwk,
  PublicKeyRecord,
  RotationRecord,
  RotationStatement,
  SeasonEvidence,
  SignedVaultHead,
  TrustedIssuer,
  VaultBundleResult,
  VaultHead,
  VaultHeadStatement,
  VaultProofBundle,
  VaultSigningKey,
} from "@agentland/identity";

const PLATFORM_DID = "did:web:agentland.us";
const AGENT_DID = /^did:web:agentland\.us:agents:([a-z0-9-]{3,24})$/;

/**
 * agentland-did/1 resolution with the caller's fetch only. The exact URL mapping and the `id`
 * check stop a response from standing in for another DID; anything else is refused unfetched.
 */
export async function resolveDid(did: string, fetchFn: typeof fetch): Promise<DidDocument> {
  const handle = typeof did === "string" ? AGENT_DID.exec(did)?.[1] : undefined;
  const url =
    did === PLATFORM_DID
      ? "https://agentland.us/.well-known/did.json"
      : handle === undefined
        ? undefined
        : `https://agentland.us/agents/${handle}/did.json`;
  if (url === undefined) throw new TypeError("AgentLand DID required");
  const response = await fetchFn(url);
  if (response.status !== 200) throw new TypeError("DID document unavailable");
  let document: unknown;
  try {
    document = parseIJson(await response.text());
  } catch {
    throw new TypeError("DID document is not strict JSON");
  }
  if (
    typeof document !== "object" ||
    document === null ||
    Array.isArray(document) ||
    !("id" in document) ||
    document.id !== did
  )
    throw new TypeError("DID document id does not match the DID");
  // Only the id is checked: key and service semantics are the caller's to verify.
  return document as DidDocument;
}

export type VaultExportPins = Readonly<{
  keys: readonly SigningKey[];
  headKeys: readonly Readonly<{ kid: string; publicKeyJwk: HeadJwk }>[];
  auditRoots: Readonly<Record<string, string>>;
}>;
type Sealed = { seq: string; key: string; recipient_key_id: string; envelope: Uint8Array };
export type SealedExportPayload = Readonly<Sealed>;
type ExportOk = { did: string; head_seq: string; head_hash: string; entries: number };
export type VaultExportResult =
  | Readonly<ExportOk & { valid: true; proved: readonly string[]; sealed: readonly Sealed[] }>
  | VerificationFailure;
export type ChainAnchorNotary = Readonly<{ chain_id: number; address: string }>;
type AnchorOk = { chain_id: number; tx_hash: string; block_number: number; from: string };
export type ChainAnchorResult = Readonly<AnchorOk & { valid: true }> | VerificationFailure;
/** A stage verdict thrown out of nested checks; any other error inside a stage is `invalid-schema`. */
class Failed extends Error {
  constructor(readonly result: VerificationFailure) {
    super(result.error.reason);
  }
}
function fail(stage: string, reason: string, index?: number): never {
  const error = index === undefined ? { stage, reason } : { stage, reason, index };
  throw new Failed({ valid: false, error });
}
function inStage<T>(stage: string, run: () => T, reason = "invalid-schema", index?: number): T {
  try {
    return run();
  } catch (error) {
    if (error instanceof Failed) throw error;
    return fail(stage, reason, index);
  }
}
/** A plain object with exactly these own keys. */
function hasExactly(value: unknown, names: readonly string[]): value is Record<string, unknown> {
  if (typeof value !== "object" || value === null || Array.isArray(value)) return false;
  const keys = Object.keys(value);
  return keys.length === names.length && names.every((name) => Object.hasOwn(value, name));
}
const isCount = (value: unknown, min: number): value is number =>
  typeof value === "number" && Number.isSafeInteger(value) && value >= min;
const json = (bytes: Uint8Array): unknown => parseIJson(Buffer.from(bytes).toString("utf8"));
const seqOf = (name: string) => name.slice(name.indexOf("/") + 1, name.lastIndexOf("."));
const bySeqNumber = (a: string, b: string) => Number(seqOf(a)) - Number(seqOf(b));
const DAY = /^\d{4}-\d{2}-\d{2}$/;
const HASH64 = /^[0-9a-f]{64}$/;
const MEMBER =
  /^(?:did-history|head|record)\.json$|^(?:entries|proofs)\/[1-9][0-9]*\.json$|^payloads\/[1-9][0-9]*\.bin$/;
/**
 * Offline check of an uncompressed agentland-vault/1 export. Pins come from outside the archive.
 * It never opens a sealed payload: callers open `sealed` only after `valid: true` (D-20).
 */
export function verifyVaultExport(tar: Uint8Array, pins: VaultExportPins): VaultExportResult {
  const roots: unknown = hasExactly(pins, ["keys", "headKeys", "auditRoots"]) && pins.auditRoots;
  const valid =
    hasExactly(pins, ["keys", "headKeys", "auditRoots"]) &&
    Array.isArray(pins.keys) &&
    Array.isArray(pins.headKeys) &&
    pins.headKeys.every(
      (item: unknown) =>
        hasExactly(item, ["kid", "publicKeyJwk"]) &&
        typeof item.kid === "string" &&
        item.kid !== "",
    ) &&
    hasExactly(roots, Object.keys(roots ?? {})) &&
    Object.getPrototypeOf(roots) === Object.prototype &&
    Object.entries(roots).every(([day, root]) => DAY.test(day) && HASH64.test(String(root)));
  if (!valid) throw new TypeError("Vault export pins required: keys, headKeys, auditRoots");
  try {
    return checkExport(tar, pins);
  } catch (error) {
    if (error instanceof Failed) return error.result;
    throw error;
  }
}
function checkExport(tar: Uint8Array, pins: VaultExportPins): VaultExportResult {
  // 1. archive: manifest first, strict canonical JSON, exactly the other members.
  const files = inStage("archive", () => readUstar(tar), "unreadable");
  const members = new Map(files.slice(1).map((file) => [file.name, file.bytes]));
  const names = [...members.keys()].sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
  const { did } = inStage(
    "archive",
    () => {
      const bytes = files[0]?.name === EXPORT_LAYOUT.manifest ? files[0].bytes : undefined;
      const value = json(bytes!);
      if (Buffer.compare(canonicalBytes(value as never), bytes!) !== 0) throw new TypeError("form");
      if (
        !hasExactly(value, ["format", "did", "files"]) ||
        value.format !== "agentland-vault/1" ||
        !AGENT_DID.test(String(value.did)) ||
        members.size !== files.length - 1 ||
        members.has(EXPORT_LAYOUT.manifest) ||
        !Array.isArray(value.files) ||
        value.files.length !== names.length ||
        value.files.some((item: unknown, index) => {
          const bytes = members.get(names[index]!)!;
          return !(
            hasExactly(item, ["name", "sha256", "size"]) &&
            item.name === names[index] &&
            item.sha256 === sha256Hex(bytes) &&
            item.size === bytes.length
          );
        })
      )
        throw new TypeError("manifest");
      return value as { readonly did: string };
    },
    "manifest-mismatch",
  );
  if (names.some((name) => !MEMBER.test(name))) fail("archive", "unknown-member");
  const head = inStage("head", () => {
    const value = json(members.get(EXPORT_LAYOUT.head)!) as SignedVaultHead;
    const pinned = pins.headKeys.find((item) => item.kid === value.kid);
    if (!pinned) fail("head", "untrusted-kid");
    if (!checkHead(value, pinned.publicKeyJwk)) fail("head", "invalid-signature");
    if (value.did !== did) fail("head", "did-mismatch");
    return value;
  });
  const expectedHead = { seq: head.seq, head_hash: head.head_hash };
  const entries = inStage("chain", () => {
    const parsed = names
      .filter((name) => name.startsWith("entries/"))
      .sort(bySeqNumber)
      .map((name) => {
        const entry = json(members.get(name)!) as VaultEntry;
        if (entry.seq !== seqOf(name)) fail("chain", "invalid-schema");
        return entry;
      });
    const chain = validateVaultChain({ did, entries: parsed, keys: pins.keys, expectedHead });
    if (!chain.valid) throw new Failed(chain);
    return parsed;
  });
  const bySeq = new Map(entries.map((entry) => [entry.seq, entry]));
  // 4. payloads: every digest before any sealed check; sealed envelopes stay unopened.
  const payloads = names.filter((name) => name.startsWith("payloads/")).sort(bySeqNumber);
  for (const name of payloads) {
    const entry = bySeq.get(seqOf(name));
    if (entry?.op !== "put") fail("payload", "orphan", Number(seqOf(name)));
    if (sha256Hex(members.get(name)!) !== entry.content_hash)
      fail("payload", "digest-mismatch", Number(entry.seq));
  }
  const sealed: SealedExportPayload[] = [];
  for (const name of payloads) {
    const { seq, key, content_type, tags } = bySeq.get(seqOf(name))!;
    if (!key.startsWith("sealed/")) continue;
    const envelope = members.get(name)!;
    try {
      if (content_type !== SEALED_CONTENT_TYPE || tags.length !== 0) throw new TypeError("outer");
      sealed.push({ seq, key, recipient_key_id: sealedEnvelopeRecipient(envelope), envelope });
    } catch {
      fail("payload", "sealed-envelope", Number(seq));
    }
  }
  // 5. proofs against pinned audit roots only
  const proved: string[] = [];
  for (const name of names.filter((item) => item.startsWith("proofs/")).sort(bySeqNumber)) {
    const seq = seqOf(name);
    const index = Number(seq);
    const proof = inStage("proof", () => json(members.get(name)!));
    const entry = bySeq.get(seq);
    if (
      !hasExactly(proof, ["seq", "date", "root", "proof", "audit_root", "audit"]) ||
      proof.seq !== seq ||
      !entry ||
      !hasExactly(proof.audit, ["vault_root_leaf_bytes", "proof"])
    )
      return fail("proof", "invalid-schema", index);
    const date = String(proof.date);
    if (date !== entry.ts_server.slice(0, 10)) fail("proof", "date-mismatch", index);
    const pinned = pins.auditRoots[date];
    if (pinned === undefined) fail("proof", "unpinned-audit-root", index);
    if (proof.audit_root !== pinned) fail("proof", "audit-root-mismatch", index);
    const leaf = String(proof.audit.vault_root_leaf_bytes);
    if (Buffer.from(leaf, "base64url").toString("hex") !== proof.root)
      fail("proof", "root-mismatch", index);
    const bundle = checkBundle(
      {
        format: "agentland-vault/1",
        did,
        entries,
        proof: { ...(proof.proof as MerkleProof), seq },
        audit: proof.audit as unknown as NonNullable<VaultProofBundle["audit"]>,
      },
      { keys: pins.keys, expectedHead, publishedRoot: pinned },
    );
    if (!bundle.valid) return bundle;
    proved.push(seq);
  }
  const { seq: head_seq, head_hash } = head;
  return { valid: true, did, head_seq, head_hash, entries: entries.length, proved, sealed };
}

const QUANTITY = /^0x(?:0|[1-9a-f][0-9a-f]*)$/;
const ADDRESS = /^0x[0-9a-f]{40}$/;
const TX_HASH = /^0x[0-9a-f]{64}$/;
const PARITY = /^0x[01]$/;
/** eth_getTransactionByHash members read; others are ignored (`from` is only compared). */
const TX_MEMBERS =
  "chainId nonce maxPriorityFeePerGas maxFeePerGas gas value r s to input hash blockNumber blockHash";
const TX_PATTERNS: Readonly<Record<string, RegExp>> = {
  to: ADDRESS,
  input: /^0x(?:[0-9a-f]{2})*$/,
  hash: TX_HASH,
  blockHash: TX_HASH,
};

/**
 * Offline check of one second-anchor transaction (D-51, C-25). Fetch the transaction from two
 * independent providers and run this on each; finality is the provider's `finalized` block and is
 * not checked here. TypeScript only (C-26). The JSON `from` is compared, never believed.
 */
export function verifyChainAnchor(
  rootDocument: unknown,
  transactionJson: unknown,
  notary: ChainAnchorNotary,
): ChainAnchorResult {
  if (
    !hasExactly(notary, ["chain_id", "address"]) ||
    !isCount(notary.chain_id, 1) ||
    !ADDRESS.test(String(notary.address))
  )
    throw new TypeError("Chain anchor notary pin required: chain_id, address");
  const failure = (stage: string, reason: string): VerificationFailure => ({
    valid: false,
    error: { stage, reason },
  });
  const doc = rootDocument as Record<string, unknown> | null;
  const anchor = doc?.chain_anchor;
  if (
    !doc ||
    !DAY.test(String(doc.date)) ||
    !HASH64.test(String(doc.root)) ||
    !Object.hasOwn(doc, "chain_anchor_status") ||
    !(
      anchor === null ||
      (hasExactly(anchor, ["chain_id", "tx_hash", "block_number"]) &&
        isCount(anchor.chain_id, 1) &&
        TX_HASH.test(String(anchor.tx_hash)) &&
        isCount(anchor.block_number, 0))
    )
  )
    return failure("root", "invalid-root-document");
  let payload: Uint8Array;
  try {
    payload = anchorPayload(String(doc.date), String(doc.root));
  } catch {
    return failure("root", "invalid-root-document");
  }
  if (doc.chain_anchor_status !== "confirmed" || anchor === null)
    return failure("root", "not-confirmed");
  if (anchor.chain_id !== notary.chain_id) return failure("root", "chain-mismatch");
  const invalid = failure("transaction", "invalid-transaction-json");
  if (typeof transactionJson !== "object" || transactionJson === null) return invalid;
  const tx = transactionJson as Record<string, unknown>;
  const lower = (name: string, raw = tx[name]) =>
    typeof raw === "string" ? raw.toLowerCase() : null;
  const value: Record<string, string | null> = {};
  for (const name of TX_MEMBERS.split(" ")) {
    const text = lower(name);
    const nullable = name.startsWith("block") && tx[name] === null;
    if (text === null ? !nullable : !(TX_PATTERNS[name] ?? QUANTITY).test(text)) return invalid;
    value[name] = text;
  }
  const parity = [lower("yParity"), lower("v")].filter((item) => item !== null);
  if (
    tx.type !== "0x2" ||
    !Array.isArray(tx.accessList) ||
    tx.accessList.length !== 0 ||
    parity.length === 0 ||
    parity.some((item) => !PARITY.test(item) || item !== parity[0]) ||
    ["yParity", "v"].some((name) => tx[name] !== undefined && lower(name) === null)
  )
    return invalid;
  if (value.blockNumber === null || value.blockHash === null)
    return failure("transaction", "pending");
  const big = (name: string) => BigInt(value[name]!);
  const fields: AnchorTransactionFields = {
    chainId: big("chainId"),
    nonce: big("nonce"),
    maxPriorityFeePerGas: big("maxPriorityFeePerGas"),
    maxFeePerGas: big("maxFeePerGas"),
    gasLimit: big("gas"),
    to: value.to!,
    value: big("value"),
    data: new Uint8Array(Buffer.from(value.input!.slice(2), "hex")),
  };
  let verified: { readonly hash: string; readonly from: string };
  try {
    const signature = { r: big("r"), s: big("s"), yParity: parity[0] === "0x1" ? 1 : 0 } as const;
    verified = verifyAnchorTransaction(serializeAnchorTransaction(fields, signature), {
      chainId: BigInt(notary.chain_id),
      address: notary.address,
      payload,
    });
  } catch (error) {
    if (error instanceof AnchorGuardError) return failure("transaction", error.reason);
    throw error;
  }
  if (verified.hash !== value.hash) return failure("transaction", "hash-mismatch");
  if (tx.from !== undefined && lower("from") !== verified.from)
    return failure("transaction", "from-mismatch");
  if (verified.hash !== anchor.tx_hash) return failure("root", "tx-hash-mismatch");
  const block_number = Number(value.blockNumber);
  if (block_number !== anchor.block_number) return failure("root", "block-mismatch");
  const { chain_id } = notary;
  return { valid: true, chain_id, tx_hash: verified.hash, block_number, from: verified.from };
}
