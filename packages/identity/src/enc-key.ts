import { canonicalBytes, canonicalize, exactMembers } from "./canonical.js";
import {
  assertAgentDid,
  assertTimestamp,
  base64urlEncode,
  decodeBase64url,
  objectRecord,
} from "./json.js";
import { verifyEd25519 } from "./keys.js";
import type { Ed25519PublicJwk } from "./keys.js";
import { activeSigningAt, buildDidHistory } from "./did.js";
import type { PublicKeyRecord, RotationRecord } from "./did.js";
import { assertEncryptionPublicKey, recipientKeyId } from "./sealed.js";

// agentland-enc-key/1 (D-14, D-15, C-27). Statements are the RFC 8785 bytes of the object with no
// prefix (docs/14 §2.3); `kind` separates the domain from every other statement type. Identity
// has no clock: callers pass DB time as `now`. First contact trusts AgentLand's DID resolution
// (TOFU, RESEARCH F2.1); a pinned signing key closes that gap for every later verification.
export const ENC_KEY_FORMAT = "agentland-enc-key/1";
export const ENC_KEY_STATEMENT_WINDOW_MS = 300_000;
export const ENC_KEY_REVOKE_REASON_MAX = 200;

export interface EncKeyStatement {
  readonly did: string;
  readonly kind: "enc_key";
  readonly previous: string | null;
  readonly public_key: string;
  readonly ts: string;
}
export interface EncKeyRevokeStatement {
  readonly did: string;
  readonly key_id: string;
  readonly kind: "enc_key_revoke";
  readonly reason: string;
  readonly ts: string;
}
export type EncKeyStatementAny = EncKeyStatement | EncKeyRevokeStatement;
export interface EncKeyRecord {
  readonly statement: EncKeyStatementAny;
  readonly signature: string;
  readonly signing_key_id: string;
  readonly custody: "self" | "platform";
}
export interface EncKeyHistory {
  readonly did: string;
  readonly keys: readonly PublicKeyRecord[];
  readonly rotations: readonly RotationRecord[];
  readonly enc_keys: readonly EncKeyRecord[];
  readonly recovery_notice: {
    readonly id: string;
    readonly started_at: string;
    readonly completes_at: string;
  } | null;
}
export type EncKeyRecipientFailure =
  "recipient_unverified" | "recipient_platform_custody" | "recipient_pin_broken";
export interface VerifiedEncKeyRecipient {
  readonly keyId: string;
  readonly publicKey: Uint8Array;
  readonly recipientKeyId: string;
  readonly signingKey: string;
}

export class EncKeyRecipientError extends Error {
  readonly reason: EncKeyRecipientFailure;
  constructor(reason: EncKeyRecipientFailure) {
    super(reason);
    this.name = "EncKeyRecipientError";
    this.reason = reason;
  }
}

const SHAPE = "Encryption key statement shape required";

function refuse(reason: EncKeyRecipientFailure): never {
  throw new EncKeyRecipientError(reason);
}

// `<did>#key-<seq>` with no DID-derived regex.
const isKeyId = (value: unknown, did: string): value is string =>
  typeof value === "string" &&
  value.startsWith(`${did}#key-`) &&
  /^[1-9][0-9]*$/.test(value.slice(did.length + 5));

/** Shape errors (including helper errors) are one TypeError; a low-order key keeps its own error. */
function assertStatement(input: unknown): EncKeyStatementAny {
  let statement: EncKeyStatementAny;
  let publicKey: Uint8Array | undefined;
  try {
    const kind = objectRecord(input).kind;
    const record =
      kind === "enc_key"
        ? exactMembers(input, ["did", "kind", "previous", "public_key", "ts"])
        : kind === "enc_key_revoke"
          ? exactMembers(input, ["did", "key_id", "kind", "reason", "ts"])
          : undefined;
    if (record === undefined) throw new TypeError(SHAPE);
    const did = record.did;
    assertAgentDid(did);
    assertTimestamp(record.ts);
    if (kind === "enc_key") {
      if (record.previous !== null && !isKeyId(record.previous, did)) throw new TypeError(SHAPE);
      publicKey = decodeBase64url(record.public_key, 32);
      statement = {
        did,
        kind,
        previous: record.previous as string | null,
        public_key: record.public_key as string,
        ts: record.ts,
      };
    } else {
      const reason = record.reason;
      if (
        !isKeyId(record.key_id, did) ||
        typeof reason !== "string" ||
        reason.length === 0 ||
        [...reason].length > ENC_KEY_REVOKE_REASON_MAX
      )
        throw new TypeError(SHAPE);
      statement = { did, key_id: record.key_id, kind: "enc_key_revoke", reason, ts: record.ts };
    }
    // RFC 8785 / I-JSON: e.g. a lone surrogate in `reason` is a shape error, not a helper error.
    canonicalize(statement);
  } catch {
    throw new TypeError(SHAPE);
  }
  // Low order is a key error, not a shape error: SealedEnvelopeError propagates unchanged.
  if (publicKey !== undefined) assertEncryptionPublicKey(publicKey);
  return statement;
}

export function encKeyStatementBytes(statement: EncKeyStatementAny): Uint8Array {
  return canonicalBytes(assertStatement(statement));
}

/** Shape, agent, ±5 minutes and active-key rules. Signatures are verified by the caller with the
 * signing key active at `ts` (15-06) or by `verifyEncKeyRecipient`. */
export function validateEncKeyStatement(
  statement: unknown,
  context: { readonly agentDid: string; readonly now: Date; readonly activeKeyId: string | null },
): asserts statement is EncKeyStatementAny {
  const { agentDid, now, activeKeyId } = context;
  if (!(now instanceof Date) || !Number.isFinite(now.getTime()))
    throw new TypeError("Valid now required");
  const parsed = assertStatement(statement);
  if (parsed.did !== agentDid) throw new TypeError("Encryption key statement is for another agent");
  if (Math.abs(Date.parse(parsed.ts) - now.getTime()) > ENC_KEY_STATEMENT_WINDOW_MS)
    throw new RangeError("Encryption key statement is not within 5 minutes");
  if (parsed.kind === "enc_key" && parsed.previous !== activeKeyId)
    throw new RangeError("previous must name the active encryption key");
  if (parsed.kind === "enc_key_revoke" && (activeKeyId === null || parsed.key_id !== activeKeyId))
    throw new RangeError("Only the active encryption key can be revoked");
}

const compare = (a: string, b: string) => (a < b ? -1 : a > b ? 1 : 0);

interface Checked {
  readonly statement: EncKeyStatementAny;
  readonly custody: "self" | "platform";
  readonly signer: string;
}

function checkRecord(input: unknown, did: string, keys: readonly PublicKeyRecord[]): Checked {
  const record = exactMembers(input, ["statement", "signature", "signing_key_id", "custody"]);
  const statement = assertStatement(record.statement);
  const { signature, signing_key_id, custody } = record;
  if (statement.did !== did) refuse("recipient_unverified");
  if (custody !== "self" && custody !== "platform") return refuse("recipient_unverified");
  const signer = activeSigningAt(keys, statement.ts).find((key) => key.id === signing_key_id);
  if (
    signer === undefined ||
    typeof signature !== "string" ||
    !verifyEd25519(
      encKeyStatementBytes(statement),
      signature,
      signer.publicKeyJwk as Ed25519PublicJwk,
    )
  )
    refuse("recipient_unverified");
  return { statement, custody, signer: signer.publicKeyJwk.x };
}

/** O-8: forward through any verified rotation, backward only through dual-signed ones (an
 * old-only rotation declares the old key compromised). */
function pinChain(
  pin: string,
  rotations: readonly (RotationRecord & { readonly signatures: "dual" | "old-only" })[],
): Set<string> {
  const chain = new Set([pin]);
  for (let size = 0; size !== chain.size;) {
    size = chain.size;
    for (const { statement, signatures } of rotations) {
      if (chain.has(statement.old_pub.x)) chain.add(statement.new_pub.x);
      if (signatures === "dual" && chain.has(statement.new_pub.x)) chain.add(statement.old_pub.x);
    }
  }
  return chain;
}

interface VerifiedState {
  readonly rotations: readonly (RotationRecord & { readonly signatures: "dual" | "old-only" })[];
  readonly keys: readonly PublicKeyRecord[];
  readonly records: readonly Checked[];
}

/** Any failure here, including helper TypeErrors, is `recipient_unverified`. */
function verifiedState(history: EncKeyHistory, did: string): VerifiedState {
  try {
    const dto = objectRecord(history);
    if (dto.did !== did || dto.recovery_notice !== null) refuse("recipient_unverified");
    if (!Array.isArray(dto.rotations) || !Array.isArray(dto.enc_keys))
      refuse("recipient_unverified");
    // The DTO's `signatures` member is stripped: buildDidHistory recomputes it.
    const rotations = (dto.rotations as readonly unknown[]).map((input) => {
      const { statement, sig_old, sig_new } = objectRecord(input);
      return {
        statement,
        sig_old,
        ...(sig_new === undefined ? {} : { sig_new }),
      } as RotationRecord;
    });
    const verified = buildDidHistory({
      handle: did.slice(did.lastIndexOf(":") + 1),
      keys: dto.keys as readonly PublicKeyRecord[],
      rotations,
    });
    const records = (dto.enc_keys as readonly unknown[]).map((input) =>
      checkRecord(input, did, verified.keys),
    );
    return { rotations: verified.rotations, keys: verified.keys, records };
  } catch (error) {
    if (error instanceof EncKeyRecipientError) throw error;
    return refuse("recipient_unverified");
  }
}

interface ActiveKey {
  readonly id: string;
  readonly publicKey: string;
  readonly custody: "self" | "platform";
  readonly signer: string;
}

export function verifyEncKeyRecipient(
  history: EncKeyHistory,
  did: string,
  publicKey: Uint8Array,
  options: { readonly pinnedSigningKey?: string } = {},
): VerifiedEncKeyRecipient {
  assertAgentDid(did);
  assertEncryptionPublicKey(publicKey);
  const { rotations, keys, records } = verifiedState(history, did);
  const encryption = keys.filter((key) => key.purpose === "encryption");
  const replay = [...records].sort(
    (a, b) =>
      compare(a.statement.ts, b.statement.ts) ||
      compare(canonicalize(a.statement), canonicalize(b.statement)),
  );
  let active: ActiveKey | null = null;
  const seen = new Set<string>();
  for (const { statement, custody, signer } of replay) {
    if (statement.kind === "enc_key") {
      const matches = encryption.filter((key) => key.publicKeyJwk.x === statement.public_key);
      if (matches.length !== 1 || statement.previous !== (active === null ? null : active.id))
        refuse("recipient_unverified");
      const id = matches[0]!.id;
      if (seen.has(id)) refuse("recipient_unverified");
      seen.add(id);
      active = { id, publicKey: statement.public_key, custody, signer };
    } else {
      if (active === null || statement.key_id !== active.id) refuse("recipient_unverified");
      active = null;
    }
  }
  const current: ActiveKey | null = active;
  if (
    current === null ||
    current.publicKey !== base64urlEncode(publicKey) ||
    encryption.some((key) => key.id === current.id && key.revoked_at !== undefined)
  )
    return refuse("recipient_unverified");
  if (current.custody === "platform") refuse("recipient_platform_custody");
  if (
    options.pinnedSigningKey !== undefined &&
    !pinChain(options.pinnedSigningKey, rotations).has(current.signer)
  )
    refuse("recipient_pin_broken");
  // publicRecords guarantees a signing key; the latest-activated unrevoked one is current.
  const signing = keys.filter((key) => key.purpose === "signing" && key.revoked_at === undefined);
  const latest = signing.reduce((a, b) => (b.activated_at > a.activated_at ? b : a));
  return {
    keyId: current.id,
    publicKey: publicKey.slice(),
    recipientKeyId: recipientKeyId(publicKey),
    signingKey: latest.publicKeyJwk.x,
  };
}
