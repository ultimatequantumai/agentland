/**
 * agentland-squad/1 (C-1, D-29, D-30). A squad is a shared memory, not an identity: no squad key
 * exists; every entry is signed by the writing member's own key; the only AgentLand signature is
 * the disclosed `attest_leave` (D-34). Members sign `agentland-squad/1\n` ‖ RFC 8785(intent), so
 * the domain is disjoint by its first bytes from vault intents (`{`), request preimages (an
 * uppercase method), proof of possession (`agentland-pop/1\n`), verify nonces
 * (`agentland-verify/1:`) and arena forecasts (`agentland-arena-forecast/1\n`).
 * Any byte change is a breaking chain change: second review, tamper test and a `/transparency`
 * changelog entry (OPS-19). Pure: no I/O, no clock.
 */
import {
  assertBytes,
  assertHash,
  assertTimestamp,
  canonicalBytes,
  decodeBase64url,
  exactMembers,
  parseIJson,
  sha256Hex,
} from "./canonical.js";
import type { PublicKeyRecord } from "./did.js";
import { assertAgentDid } from "./json.js";
import { signEd25519, verifyEd25519 } from "./keys.js";
import type { Ed25519PublicJwk } from "./keys.js";
import { merkleRoot } from "./merkle.js";
import {
  INTENT_FIELDS,
  assertSequence,
  createDeleteIntent,
  createPutIntent,
  validateIntent,
} from "./vault.js";
import type { VaultIntent } from "./vault.js";

export const SQUAD_FORMAT = "agentland-squad/1";
export const SQUAD_HEAD_FORMAT = "agentland-squad-head/1";
export const SQUAD_PLATFORM_DID = "did:web:agentland.us";
export const SQUAD_STATEMENT_PREFIX = "public/.squad/";
export const SQUAD_STATEMENT_CONTENT_TYPE = "application/json";
export const SQUAD_MAX_MEMBERS = 10;
export const SQUAD_INVITE_TTL_MS = 604_800_000;
export const SQUAD_REASON_MAX = 500; // code points
export const SQUAD_STATEMENT_KINDS = [
  "found",
  "invite",
  "accept",
  "leave",
  "remove",
  "role",
  "epoch",
  "attest_leave",
] as const;
export const SQUAD_ATTEST_REASONS = [
  "agent_retired",
  "operator_closed",
  "operator_removed",
] as const;
export type SquadStatementKind = (typeof SQUAD_STATEMENT_KINDS)[number];
export type SquadAttestReason = (typeof SQUAD_ATTEST_REASONS)[number];
export type SquadRole = "admin" | "member";
export interface SquadIntent extends VaultIntent {
  readonly squad_id: string;
  readonly signer: string;
  readonly signing_key_id: string;
}
export interface SquadEntry extends SquadIntent {
  readonly ts_server: string;
  readonly sig: string;
}
export interface SquadEpochWrap {
  readonly kid: string;
  readonly envelope: string;
}
export interface SquadStatement {
  readonly squad_id: string;
  readonly kind: SquadStatementKind;
  readonly subject_did: string;
  readonly actor_did: string;
  readonly ts: string;
  readonly role?: SquadRole;
  readonly reason?: string;
  readonly epoch?: string;
  readonly invite_seq?: string;
  readonly wraps?: readonly SquadEpochWrap[];
}
export interface SquadSignerKeys {
  readonly did: string;
  readonly keys: readonly PublicKeyRecord[];
}
export interface SquadPlatformKey {
  readonly kid: string;
  readonly publicKeyJwk: Ed25519PublicJwk;
}
export interface SquadStatementPayload {
  readonly seq: string;
  readonly content: Uint8Array;
}
export interface SquadHeadStatement {
  readonly squad_id: string;
  readonly seq: string;
  readonly head_hash: string;
  readonly ts: string;
}
export interface SignedSquadHead extends SquadHeadStatement {
  readonly kid: string;
  readonly sig: string;
}

const SQUAD_ID = /^[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;
const PREFIX = new TextEncoder().encode(`${SQUAD_FORMAT}\n`);
const SQUAD_FIELDS = [...INTENT_FIELDS, "squad_id", "signer", "signing_key_id"] as const;
const STATEMENT_FIELDS = ["squad_id", "kind", "subject_did", "actor_did", "ts"] as const;
// Per kind: members that must be present and members that may be present (outline O-3).
const KIND_MEMBERS: Record<SquadStatementKind, { required: string[]; optional: string[] }> = {
  found: { required: ["role"], optional: [] },
  invite: { required: [], optional: ["reason"] },
  accept: { required: ["invite_seq"], optional: [] },
  leave: { required: [], optional: [] },
  remove: { required: [], optional: ["reason"] },
  role: { required: ["role"], optional: [] },
  epoch: { required: ["epoch", "wraps"], optional: [] },
  attest_leave: { required: ["reason"], optional: [] },
};

export function assertSquadId(value: unknown): asserts value is string {
  if (typeof value !== "string" || !SQUAD_ID.test(value))
    throw new TypeError("Lowercase UUIDv7 squad id required");
}

export function validateSquadIntent(value: unknown): asserts value is SquadIntent {
  const intent = exactMembers(value, SQUAD_FIELDS);
  validateIntent(Object.fromEntries(INTENT_FIELDS.map((name) => [name, intent[name]])));
  assertSquadId(intent.squad_id);
  const signer = intent.signer;
  const keyId = intent.signing_key_id;
  if (signer === SQUAD_PLATFORM_DID) {
    if (typeof keyId !== "string" || keyId.length === 0 || keyId.length > 200)
      throw new TypeError("Squad signing key id required");
    return;
  }
  try {
    assertAgentDid(signer);
  } catch {
    throw new TypeError("Squad signer DID required");
  }
  if (
    typeof keyId !== "string" ||
    !keyId.startsWith(`${signer}#`) ||
    !/^[A-Za-z0-9._~-]+$/.test(keyId.slice(signer.length + 1))
  )
    throw new TypeError("Squad signing key id required");
}

export function squadGenesis(squadId: string): string {
  assertSquadId(squadId);
  return sha256Hex(new TextEncoder().encode(`${SQUAD_FORMAT}\n${squadId}`));
}

export function squadSigningMessage(intent: SquadIntent): Uint8Array {
  validateSquadIntent(intent);
  const body = canonicalBytes(intent);
  const message = new Uint8Array(PREFIX.length + body.length);
  message.set(PREFIX);
  message.set(body, PREFIX.length);
  return message;
}

function withSquad(
  intent: VaultIntent,
  input: { readonly squad_id: string; readonly signer: string; readonly signing_key_id: string },
): SquadIntent {
  const squad: SquadIntent = {
    ...intent,
    squad_id: input.squad_id,
    signer: input.signer,
    signing_key_id: input.signing_key_id,
  };
  validateSquadIntent(squad);
  return squad;
}

export function createSquadPutIntent(input: {
  seq: string;
  key: string;
  content: Uint8Array;
  prev_hash: string;
  squad_id: string;
  signer: string;
  signing_key_id: string;
  content_type?: string;
  tags?: readonly string[];
}): SquadIntent {
  exactMembers(
    input,
    ["seq", "key", "content", "prev_hash", "squad_id", "signer", "signing_key_id"],
    ["content_type", "tags"],
  );
  const { squad_id, signer, signing_key_id, ...vault } = input;
  return withSquad(createPutIntent(vault), { squad_id, signer, signing_key_id });
}

export function createSquadDeleteIntent(input: {
  seq: string;
  key: string;
  prev_hash: string;
  squad_id: string;
  signer: string;
  signing_key_id: string;
}): SquadIntent {
  exactMembers(input, ["seq", "key", "prev_hash", "squad_id", "signer", "signing_key_id"]);
  const { squad_id, signer, signing_key_id, ...vault } = input;
  return withSquad(createDeleteIntent(vault), { squad_id, signer, signing_key_id });
}

/** Tests and bootstrap; members sign with their own keys. */
export function signSquadIntent(intent: SquadIntent, privatePkcs8: Uint8Array): string {
  return signEd25519(squadSigningMessage(intent), privatePkcs8);
}

function assertWraps(value: unknown): void {
  if (!Array.isArray(value) || value.length < 1 || value.length > SQUAD_MAX_MEMBERS)
    throw new TypeError("Wrap list required");
  let previous = "";
  for (const item of value) {
    const wrap = exactMembers(item, ["kid", "envelope"]);
    if (typeof wrap.kid !== "string" || !/^[0-9a-f]{64}$/.test(wrap.kid) || wrap.kid <= previous)
      throw new TypeError("Sorted distinct wrap kids required");
    previous = wrap.kid;
    if (decodeBase64url(wrap.envelope).length < 1) throw new TypeError("Wrap envelope required");
  }
}

function assertStatementFields(s: Record<string, unknown>): void {
  assertSquadId(s.squad_id);
  assertAgentDid(s.subject_did);
  if (s.actor_did !== SQUAD_PLATFORM_DID) assertAgentDid(s.actor_did);
  assertTimestamp(s.ts);
  if (s.kind === "found" && s.role !== "admin") throw new TypeError("Founder is an admin");
  if (s.kind === "role" && s.role !== "admin" && s.role !== "member")
    throw new TypeError("Squad role required");
  if (s.invite_seq !== undefined) assertSequence(s.invite_seq);
  if (s.epoch !== undefined) assertSequence(s.epoch);
  if (s.wraps !== undefined) assertWraps(s.wraps);
  if (s.reason !== undefined) {
    if (typeof s.reason !== "string" || s.reason.length === 0) throw new TypeError("Reason");
    if ([...s.reason].length > SQUAD_REASON_MAX) throw new TypeError("Reason too long");
    const reasons: readonly string[] = SQUAD_ATTEST_REASONS;
    if (s.kind === "attest_leave" && !reasons.includes(s.reason))
      throw new TypeError("Attestation reason");
  }
}

function validateStatement(value: unknown): SquadStatement {
  try {
    const optional = [...STATEMENT_FIELDS, "role", "reason", "epoch", "invite_seq", "wraps"];
    const kind = exactMembers(value, ["kind"], optional).kind;
    if (!(SQUAD_STATEMENT_KINDS as readonly unknown[]).includes(kind))
      throw new TypeError("Unknown kind");
    const members = KIND_MEMBERS[kind as SquadStatementKind];
    const s = exactMembers(value, [...STATEMENT_FIELDS, ...members.required], members.optional);
    assertStatementFields(s);
    return { ...(s as unknown as SquadStatement) };
  } catch {
    throw new TypeError("Exact squad statement required");
  }
}

export function squadStatementBytes(statement: SquadStatement): Uint8Array {
  return canonicalBytes(validateStatement(statement));
}

export function parseSquadStatement(content: Uint8Array): SquadStatement {
  assertBytes(content);
  let parsed: unknown;
  try {
    parsed = parseIJson(new TextDecoder("utf-8", { fatal: true }).decode(content));
  } catch {
    throw new TypeError("Exact squad statement required");
  }
  const statement = validateStatement(parsed);
  if (!Buffer.from(canonicalBytes(statement)).equals(Buffer.from(content)))
    throw new TypeError("Canonical squad statement bytes required");
  return statement;
}

export function validateSquadEntry(value: unknown): asserts value is SquadEntry {
  const entry = exactMembers(value, [...SQUAD_FIELDS, "ts_server", "sig"]);
  const { ts_server, sig, ...intent } = entry;
  validateSquadIntent(intent);
  assertTimestamp(ts_server);
  decodeBase64url(sig, 64);
}

/** Never its own preimage; `sig` is a member (outline O-2). */
export function hashSquadEntry(entry: SquadEntry): string {
  validateSquadEntry(entry);
  return sha256Hex(canonicalBytes(entry));
}

/** RFC 6962 root over the canonical entries stamped on `date` (UTC), in input (seq) order. */
export function squadDayRoot(entries: readonly SquadEntry[], date: string): string {
  try {
    if (typeof date !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(date)) throw new TypeError();
    assertTimestamp(`${date}T00:00:00.000Z`);
  } catch {
    throw new TypeError("UTC date required");
  }
  return merkleRoot(
    entries
      .filter((entry) => entry.ts_server.startsWith(date))
      .map((entry) => canonicalBytes(entry)),
  );
}

/** C-7: RFC 8785 bytes of {format, squad_id, seq, head_hash, ts}; kid and sig are outside. */
export function squadHeadPreimage(head: SquadHeadStatement): Uint8Array {
  const data = exactMembers(head, ["squad_id", "seq", "head_hash", "ts"]);
  assertSquadId(data.squad_id);
  assertSequence(data.seq, true);
  assertHash(data.head_hash);
  assertTimestamp(data.ts);
  return canonicalBytes({ format: SQUAD_HEAD_FORMAT, ...data });
}

/** Tests and bootstrap only; the service signs through HSM custody (16-10). */
export function signSquadHead(
  head: SquadHeadStatement & { readonly kid: string },
  privatePkcs8: Uint8Array,
): SignedSquadHead {
  const { kid, ...statement } = exactMembers(head, ["squad_id", "seq", "head_hash", "ts", "kid"]);
  if (typeof kid !== "string" || kid.length === 0) throw new TypeError("Key id required");
  const value = statement as unknown as SquadHeadStatement;
  return { ...value, kid, sig: signEd25519(squadHeadPreimage(value), privatePkcs8) };
}

export function verifySquadHead(head: SignedSquadHead, publicJwk: Ed25519PublicJwk): boolean {
  try {
    const { kid, sig, ...statement } = exactMembers(head, [
      "squad_id",
      "seq",
      "head_hash",
      "ts",
      "kid",
      "sig",
    ]);
    if (typeof kid !== "string" || kid.length === 0) return false;
    return verifyEd25519(
      squadHeadPreimage(statement as unknown as SquadHeadStatement),
      sig as string,
      publicJwk,
    );
  } catch {
    return false;
  }
}
