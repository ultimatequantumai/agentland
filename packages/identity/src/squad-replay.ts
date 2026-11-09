/**
 * The reference verifier of agentland-squad/1. The 0029 insert trigger (16-09) must accept and
 * refuse exactly what this accepts and refuses (trigger = verifier). Pure: the caller supplies
 * every trust pin (signer DID histories, platform keys, the expected head); nothing inside the
 * input is trusted. Invite expiry compares server stamps only, never statement `ts` (DB time).
 */
import { assertBytes, assertHash, exactMembers, sha256Hex } from "./canonical.js";
import { activeSigningAt, publicRecords } from "./did.js";
import type { PublicKeyRecord } from "./did.js";
import { assertAgentDid } from "./json.js";
import { validatePublicJwk, verifyEd25519 } from "./keys.js";
import type { Ed25519PublicJwk } from "./keys.js";
import {
  SQUAD_INVITE_TTL_MS,
  SQUAD_MAX_MEMBERS,
  SQUAD_PLATFORM_DID,
  SQUAD_STATEMENT_CONTENT_TYPE,
  SQUAD_STATEMENT_PREFIX,
  assertSquadId,
  hashSquadEntry,
  parseSquadStatement,
  squadGenesis,
  squadSigningMessage,
  validateSquadEntry,
} from "./squad.js";
import type {
  SquadEntry,
  SquadIntent,
  SquadPlatformKey,
  SquadRole,
  SquadSignerKeys,
  SquadStatement,
  SquadStatementPayload,
} from "./squad.js";
import { assertSequence } from "./vault.js";
import type { VaultHead, VerificationFailure } from "./vault.js";

export interface SquadMembership {
  readonly did: string;
  readonly role: SquadRole;
  readonly from_seq: string;
  readonly until_seq?: string;
  readonly exit?: "leave" | "remove" | "attest_leave";
}
export interface SquadEpoch {
  readonly epoch: string;
  readonly seq: string;
  readonly recipients: readonly string[];
}
export interface SquadReplaySuccess {
  readonly valid: true;
  readonly squad_id: string;
  readonly entries: number;
  readonly head_seq: string;
  readonly head_hash: string;
  readonly members: readonly SquadMembership[];
  readonly epochs: readonly SquadEpoch[];
  readonly closed: boolean;
}
export type SquadReplayResult = SquadReplaySuccess | VerificationFailure;

type Interval = { -readonly [K in keyof SquadMembership]: SquadMembership[K] };
interface Pins {
  readonly squadId: string;
  readonly entries: readonly unknown[];
  readonly payloads: Map<string, Uint8Array>;
  readonly signers: Map<string, PublicKeyRecord[]>;
  readonly platform: Map<string, Ed25519PublicJwk>;
  readonly head: VaultHead;
}
interface State {
  readonly members: Map<string, Interval>;
  readonly intervals: Interval[];
  readonly invites: Map<string, { seq: string; issuer: string; ts: string }>;
  epoch: bigint;
  readonly epochs: SquadEpoch[];
}

const AGENT_PREFIX = "did:web:agentland.us:agents:";
// O-3: these kinds are about the actor itself.
const SELF_KINDS: Record<string, true> = { found: true, accept: true, leave: true, epoch: true };
const SCHEMA: VerificationFailure = {
  valid: false,
  error: { stage: "schema", reason: "invalid-schema-or-trust-pins" },
};

function failure(stage: string, reason: string, index: number): VerificationFailure {
  return { valid: false, error: { stage, reason, index } };
}

function uniqueMap<T>(rows: unknown, read: (row: unknown) => [string, T]): Map<string, T> {
  if (!Array.isArray(rows)) throw new TypeError("Pin array required");
  const map = new Map<string, T>();
  for (const row of rows) {
    const [key, value] = read(row);
    if (map.has(key)) throw new TypeError("Duplicate pin");
    map.set(key, value);
  }
  return map;
}

function readPins(input: unknown): Pins {
  const data = exactMembers(input, [
    "squadId",
    "entries",
    "statements",
    "signerKeys",
    "platformKeys",
    "expectedHead",
  ]);
  assertSquadId(data.squadId);
  if (!Array.isArray(data.entries)) throw new TypeError("Entry array required");
  const head = exactMembers(data.expectedHead, ["seq", "head_hash"]);
  assertSequence(head.seq, true);
  assertHash(head.head_hash);
  const signers = uniqueMap(data.signerKeys, (row) => {
    const signer = exactMembers(row, ["did", "keys"]);
    assertAgentDid(signer.did);
    const handle = signer.did.slice(AGENT_PREFIX.length);
    return [signer.did, publicRecords(handle, signer.keys as readonly PublicKeyRecord[])];
  });
  const platform = uniqueMap(data.platformKeys, (row) => {
    const key = exactMembers(row, ["kid", "publicKeyJwk"]);
    if (typeof key.kid !== "string" || key.kid.length === 0 || key.kid.length > 200)
      throw new TypeError("Platform key id required");
    return [key.kid, validatePublicJwk(key.publicKeyJwk, "Ed25519") as Ed25519PublicJwk];
  });
  const payloads = uniqueMap(data.statements, (row) => {
    const payload = exactMembers(row, ["seq", "content"]);
    assertSequence(payload.seq);
    assertBytes(payload.content);
    return [payload.seq, payload.content];
  });
  return {
    squadId: data.squadId,
    entries: data.entries,
    payloads,
    signers,
    platform,
    head: { seq: head.seq, head_hash: head.head_hash },
  };
}

function checkChain(
  entry: unknown,
  index: number,
  pins: Pins,
  previous: string,
): VerificationFailure | undefined {
  try {
    validateSquadEntry(entry);
  } catch {
    return failure("chain", "invalid-entry", index);
  }
  if (entry.squad_id !== pins.squadId) return failure("chain", "foreign-squad", index);
  if (entry.seq !== String(index + 1)) return failure("chain", "noncontiguous-sequence", index);
  if (entry.prev_hash !== previous) return failure("chain", "broken-hash-link", index);
  return undefined;
}

function checkSignature(entry: SquadEntry, pins: Pins): string | undefined {
  let jwk: Ed25519PublicJwk | undefined;
  if (entry.signer === SQUAD_PLATFORM_DID) jwk = pins.platform.get(entry.signing_key_id);
  else {
    const records = pins.signers.get(entry.signer) ?? [];
    const record = records.find((r) => r.id === entry.signing_key_id && r.purpose === "signing");
    if (record && !activeSigningAt(records, entry.ts_server).includes(record))
      return "key-not-active";
    jwk = record?.publicKeyJwk as Ed25519PublicJwk | undefined;
  }
  if (!jwk) return "unknown-signer-key";
  const intent: Record<string, unknown> = { ...entry };
  delete intent.ts_server;
  delete intent.sig;
  return verifyEd25519(squadSigningMessage(intent as unknown as SquadIntent), entry.sig, jwk)
    ? undefined
    : "untrusted-signature";
}

/** Returns the parsed statement, null for a data entry, or the refusal reason. */
function checkStatement(entry: SquadEntry, pins: Pins): SquadStatement | null | string {
  if (!entry.key.startsWith(SQUAD_STATEMENT_PREFIX)) return null;
  if (entry.op === "delete") return "statement-delete";
  const payload = pins.payloads.get(entry.seq);
  if (!payload) return "payload-missing";
  if (sha256Hex(payload) !== entry.content_hash) return "payload-mismatch";
  let statement: SquadStatement;
  try {
    statement = parseSquadStatement(payload);
  } catch {
    return "invalid-statement";
  }
  if (
    statement.squad_id !== entry.squad_id ||
    entry.key !== SQUAD_STATEMENT_PREFIX + statement.kind ||
    entry.content_type !== SQUAD_STATEMENT_CONTENT_TYPE ||
    entry.tags.length !== 0 ||
    statement.actor_did !== entry.signer
  )
    return "statement-mismatch";
  return statement;
}

const admins = (state: State) =>
  [...state.members.values()].filter((member) => member.role === "admin").length;

function authorizeAccept(entry: SquadEntry, s: SquadStatement, state: State): string | undefined {
  const invite = state.invites.get(s.subject_did);
  if (!invite || invite.seq !== s.invite_seq) return "invite-not-live";
  if (Date.parse(entry.ts_server) - Date.parse(invite.ts) >= SQUAD_INVITE_TTL_MS)
    return "invite-expired";
  if (state.members.get(invite.issuer)?.role !== "admin") return "issuer-not-admin";
  if (state.members.size >= SQUAD_MAX_MEMBERS) return "squad-full";
  return undefined;
}

function authorizeMember(entry: SquadEntry, s: SquadStatement, state: State): string | undefined {
  const admin = state.members.get(entry.signer)!.role === "admin";
  const subject = state.members.get(s.subject_did);
  if ((s.kind === "invite" || s.kind === "remove" || s.kind === "role") && !admin)
    return "admin-required";
  switch (s.kind) {
    case "invite":
      return subject || s.subject_did === entry.signer ? "already-member" : undefined;
    case "remove":
      return !subject || s.subject_did === entry.signer ? "not-a-member" : undefined;
    case "role":
      if (!subject) return "not-a-member";
      return subject.role === "admin" && s.role === "member" && admins(state) === 1
        ? "last-admin"
        : undefined;
    case "leave":
      return admin && admins(state) === 1 && state.members.size > 1 ? "last-admin" : undefined;
    case "epoch":
      if (BigInt(s.epoch!) !== state.epoch + 1n) return "epoch-sequence";
      return s.wraps!.length === state.members.size ? undefined : "epoch-recipients";
    default:
      return undefined;
  }
}

function authorizeStatement(
  entry: SquadEntry,
  s: SquadStatement | null,
  state: State,
): string | undefined {
  if ((entry.signer === SQUAD_PLATFORM_DID) !== (s?.kind === "attest_leave"))
    return "platform-signer";
  if ((entry.seq === "1") !== (s?.kind === "found")) return "found-not-first";
  if (s === null) return state.members.has(entry.signer) ? undefined : "not-a-member";
  if (SELF_KINDS[s.kind] && s.subject_did !== s.actor_did) return "subject-mismatch";
  if (s.kind === "found") return undefined;
  if (s.kind === "attest_leave")
    return state.members.has(s.subject_did) ? undefined : "not-a-member";
  if (s.kind === "accept") return authorizeAccept(entry, s, state);
  if (!state.members.has(entry.signer)) return "not-a-member";
  return authorizeMember(entry, s, state);
}

function close(state: State, did: string, seq: string, exit: Interval["exit"]): void {
  const member = state.members.get(did)!;
  member.until_seq = seq;
  member.exit = exit;
  state.members.delete(did);
}

/** O-4: an attest_leave that leaves members but no admin promotes the earliest member. */
function succeed(state: State): void {
  if (state.members.size === 0 || admins(state) > 0) return;
  let earliest: Interval | undefined;
  for (const member of state.members.values())
    if (!earliest || BigInt(member.from_seq) < BigInt(earliest.from_seq)) earliest = member;
  earliest!.role = "admin";
}

function applyStatement(entry: SquadEntry, s: SquadStatement, state: State): void {
  switch (s.kind) {
    case "found":
    case "accept": {
      state.invites.delete(s.subject_did);
      const role: SquadRole = s.kind === "found" ? "admin" : "member";
      const member: Interval = { did: s.subject_did, role, from_seq: entry.seq };
      state.members.set(s.subject_did, member);
      state.intervals.push(member);
      return;
    }
    case "invite":
      state.invites.set(s.subject_did, {
        seq: entry.seq,
        issuer: entry.signer,
        ts: entry.ts_server,
      });
      return;
    case "role":
      state.members.get(s.subject_did)!.role = s.role!;
      return;
    case "epoch":
      state.epoch = BigInt(s.epoch!);
      state.epochs.push({
        epoch: s.epoch!,
        seq: entry.seq,
        recipients: s.wraps!.map((w) => w.kid),
      });
      return;
    case "attest_leave":
      close(state, s.subject_did, entry.seq, "attest_leave");
      succeed(state);
      return;
    default:
      close(state, s.subject_did, entry.seq, s.kind);
  }
}

function replayEntry(
  raw: unknown,
  index: number,
  pins: Pins,
  previous: string,
  state: State,
): VerificationFailure | undefined {
  const chain = checkChain(raw, index, pins, previous);
  if (chain) return chain;
  const entry = raw as SquadEntry;
  const signature = checkSignature(entry, pins);
  if (signature) return failure("signature", signature, index);
  const statement = checkStatement(entry, pins);
  if (typeof statement === "string") return failure("statement", statement, index);
  const refusal = authorizeStatement(entry, statement, state);
  if (refusal) return failure("authorization", refusal, index);
  if (statement) applyStatement(entry, statement, state);
  return undefined;
}

export function replaySquad(input: {
  squadId: string;
  entries: readonly SquadEntry[];
  statements: readonly SquadStatementPayload[];
  signerKeys: readonly SquadSignerKeys[];
  platformKeys: readonly SquadPlatformKey[];
  expectedHead: VaultHead;
}): SquadReplayResult {
  try {
    const pins = readPins(input);
    const state: State = {
      members: new Map(),
      intervals: [],
      invites: new Map(),
      epoch: 0n,
      epochs: [],
    };
    let previous = squadGenesis(pins.squadId);
    for (let index = 0; index < pins.entries.length; index++) {
      const refused = replayEntry(pins.entries[index], index, pins, previous, state);
      if (refused) return refused;
      previous = hashSquadEntry(pins.entries[index] as SquadEntry);
    }
    const headSeq = String(pins.entries.length);
    if (pins.head.seq !== headSeq || pins.head.head_hash !== previous)
      return { valid: false, error: { stage: "chain", reason: "expected-head-mismatch" } };
    return {
      valid: true,
      squad_id: pins.squadId,
      entries: pins.entries.length,
      head_seq: headSeq,
      head_hash: previous,
      members: state.intervals.map((m) => ({ ...m })),
      epochs: state.epochs,
      closed: state.members.size === 0,
    };
  } catch {
    return SCHEMA;
  }
}
