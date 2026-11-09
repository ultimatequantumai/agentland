// agentland-squad-sealed/1 (D-37, RESEARCH F2.1, C-5, C-6): squad `sealed/` entries encrypted under
// a per-epoch key that members wrap to each other's own encryption keys as unchanged
// agentland-sealed/1 envelopes.
// Client code: the server may import only SQUAD_SEALED_FORMAT, SQUAD_SEALED_MAGIC,
// SQUAD_SEALED_CONTENT_TYPE, parseSquadSealedHeader and squadSealedAad (16-12 gate); it never
// decrypts (non-negotiable 10).
// XChaCha20-Poly1305 is not key-committing: the header names one epoch and a reader opens with that
// epoch's key only, never by trial decryption; a wrap is opened by kid only.
// Not browser-portable: assertSquadId and verifyEncKeyRecipient reach canonical.ts (Node crypto).
import { xchacha20poly1305 } from "@noble/ciphers/chacha.js";
import { randomBytes } from "@noble/ciphers/utils.js";
import { sha256 } from "@noble/hashes/sha2.js";
import { bytesToHex } from "@noble/hashes/utils.js";
import { verifyEncKeyRecipient } from "./enc-key.js";
import type { EncKeyHistory } from "./enc-key.js";
import { assertBytes, base64urlEncode, canonicalize, decodeBase64url, utf8Bytes } from "./json.js";
import {
  SealedEnvelopeError,
  openSealedEntry,
  parseSealedInner,
  recipientKeyId,
  sealEntry,
  sealEntryWithRandomness,
  sealedInner,
} from "./sealed.js";
import type { SealedMeta, SealRandomness, SealInput } from "./sealed.js";
import { assertSquadId, hashSquadEntry, squadGenesis } from "./squad.js";
import type { SquadEntry, SquadEpochWrap, SquadStatementPayload } from "./squad.js";
import type { SquadReplaySuccess } from "./squad-replay.js";
import { assertSequence } from "./vault.js";
import type { VerificationFailure } from "./vault.js";

export const SQUAD_SEALED_FORMAT = "agentland-squad-sealed/1";
export const SQUAD_SEALED_MAGIC = "414c5101"; // "ALQ" + 0x01
export const SQUAD_SEALED_CONTENT_TYPE = "application/vnd.agentland.squad-sealed";

const MAGIC = Uint8Array.of(0x41, 0x4c, 0x51, 0x01);
const OVERHEAD = 48; // 4 magic + 4 epoch + 24 nonce + 16 tag
const MIN_ENVELOPE = 304;
const MAX_ENVELOPE = 63_792; // OVERHEAD + SEALED_MAX_INNER
const PAD_UNIT = 256;
const NONCE_LENGTH = 24;
const HEADER_END = 8 + NONCE_LENGTH;
const MAX_EPOCH = 4_294_967_295n;
const EPOCH_KEY_CONTENT_TYPE = "application/vnd.agentland.squad-epoch-key";

export type SquadSealedFailure =
  | "magic"
  | "length"
  | "epoch"
  | "epoch_key"
  | "authentication"
  | "meta_length"
  | "meta"
  | "size"
  | "padding"
  | "members";

export class SquadSealedError extends Error {
  readonly reason: SquadSealedFailure;
  constructor(reason: SquadSealedFailure) {
    super(`agentland-squad-sealed/1: ${reason}`);
    this.name = "SquadSealedError";
    this.reason = reason;
  }
}

export interface SquadSealedInput {
  readonly epochKey: Uint8Array;
  readonly epoch: string;
  readonly squadId: string;
  readonly key: string;
  readonly meta: SealedMeta;
  readonly body: Uint8Array;
}
export interface OpenedSquadEntry {
  readonly epoch: string;
  readonly meta: SealedMeta & { readonly size: number };
  readonly body: Uint8Array;
}
export interface SquadEpochWrapInput {
  readonly recipient: Uint8Array;
  readonly did: string;
  readonly squadId: string;
  readonly epoch: string;
  readonly epochKey: Uint8Array;
}
export interface SquadRecipientHistory {
  readonly did: string;
  readonly history: EncKeyHistory;
  readonly publicKey: Uint8Array;
  readonly pinnedSigningKey?: string;
}
export interface VerifiedSquadRecipient {
  readonly did: string;
  readonly publicKey: Uint8Array;
  readonly kid: string;
  readonly signingKey: string;
}
export type SquadSealedCheckResult = { readonly valid: true } | VerificationFailure;

function fail(reason: SquadSealedFailure): never {
  throw new SquadSealedError(reason);
}

/** Inner-layout errors from sealed.ts keep their reason under this format's error class. */
function inner<T>(run: () => T): T {
  try {
    return run();
  } catch (error) {
    if (error instanceof SealedEnvelopeError) fail(error.reason as SquadSealedFailure);
    throw error;
  }
}

function assertEpoch(epoch: unknown): asserts epoch is string {
  assertSequence(epoch);
  if (BigInt(epoch) > MAX_EPOCH) throw new RangeError("Squad epoch exceeds u32");
}

function assertSquadKey(key: unknown): asserts key is string {
  if (typeof key !== "string" || !/^sealed\/.+$/u.test(key))
    throw new TypeError("Sealed vault key required");
}

function assertEpochKey(epochKey: unknown): asserts epochKey is Uint8Array {
  if (!(epochKey instanceof Uint8Array) || epochKey.length !== 32) fail("epoch_key");
}

// Hostile-input rule (2R review): every public entry point snapshots the caller's input exactly
// once with structuredClone and uses only the snapshot. Getters run once; proxies and
// function-valued members throw (DataCloneError); subclass prototypes and overridden methods are
// dropped; typed arrays clone from their internal slots. Valid inputs produce identical bytes.
function snapshot<T>(value: T, refuse: () => never): T {
  let copy: T;
  try {
    copy = structuredClone(value);
  } catch {
    return refuse();
  }
  return copy;
}
const badInput = (): never => {
  throw new TypeError("Squad sealed input required");
};
const badBytes = (): never => {
  throw new TypeError("Uint8Array required");
};
// structuredClone keeps a Uint8Array over a SharedArrayBuffer pointing at the same shared block,
// so every byte field is copied into a fresh, non-shared ArrayBuffer right after the clone and
// before any validation; only that copy is validated and used.
const own = <T>(value: T): T =>
  value instanceof Uint8Array ? (new Uint8Array(value) as T) : value;

function aadOf(squadId: unknown, key: unknown, epoch: unknown): Uint8Array {
  assertSquadId(squadId);
  assertSquadKey(key);
  assertEpoch(epoch);
  return utf8Bytes(canonicalize({ epoch, format: SQUAD_SEALED_FORMAT, key, squad_id: squadId }));
}

/** RFC 8785 bytes of {epoch, format, key, squad_id}; epoch is a canonical decimal string. */
export function squadSealedAad(input: {
  readonly squadId: string;
  readonly key: string;
  readonly epoch: string;
}): Uint8Array {
  const { squadId, key, epoch } = snapshot(input, badInput);
  return aadOf(squadId, key, epoch);
}

function headerOf(envelope: unknown): { epoch: string } {
  assertBytes(envelope);
  if (envelope.length < 4 || MAGIC.some((byte, i) => envelope[i] !== byte)) fail("magic");
  if (
    envelope.length < MIN_ENVELOPE ||
    envelope.length > MAX_ENVELOPE ||
    (envelope.length - OVERHEAD) % PAD_UNIT !== 0
  )
    fail("length");
  const epoch = new DataView(envelope.buffer, envelope.byteOffset, 8).getUint32(4);
  if (epoch < 1) fail("epoch");
  return { epoch: String(epoch) };
}

/** Shape only (magic, length, epoch); never decrypts, so a bad tag still parses. */
export function parseSquadSealedHeader(envelope: Uint8Array): { epoch: string } {
  return headerOf(own(snapshot(envelope, badBytes)));
}

/** Vectors and tests only. Reusing a nonce under one epoch key breaks confidentiality; it is not
 * in the package barrel. */
export function sealSquadEntryWithRandomness(
  input: SquadSealedInput,
  randomness: { readonly nonce: Uint8Array },
): Uint8Array {
  const s = snapshot(input, badInput);
  const epochKey = own(s.epochKey);
  const body = own(s.body);
  const nonce = own(snapshot(randomness, badInput).nonce);
  assertEpochKey(epochKey);
  if (!(nonce instanceof Uint8Array) || nonce.length !== NONCE_LENGTH)
    throw new TypeError("24-byte nonce required");
  const aad = aadOf(s.squadId, s.key, s.epoch);
  const plain = inner(() => sealedInner(s.meta, body));
  const sealed = xchacha20poly1305(epochKey, nonce, aad).encrypt(plain);
  const out = new Uint8Array(HEADER_END + sealed.length);
  out.set(MAGIC);
  new DataView(out.buffer).setUint32(4, Number(s.epoch));
  out.set(nonce, 8);
  out.set(sealed, HEADER_END);
  return out;
}

/** Fresh 24-byte nonce per entry. */
export function sealSquadEntry(input: SquadSealedInput): Uint8Array {
  return sealSquadEntryWithRandomness(snapshot(input, badInput), {
    nonce: randomBytes(NONCE_LENGTH),
  });
}

export function openSquadEntry(input: {
  readonly epochKey: Uint8Array;
  readonly squadId: string;
  readonly key: string;
  readonly envelope: Uint8Array;
}): OpenedSquadEntry {
  const s = snapshot(input, badInput);
  const { squadId, key } = s;
  const epochKey = own(s.epochKey);
  const envelope = own(s.envelope);
  assertEpochKey(epochKey);
  const { epoch } = headerOf(envelope);
  const aad = aadOf(squadId, key, epoch);
  let plain: Uint8Array;
  try {
    plain = xchacha20poly1305(epochKey, envelope.subarray(8, HEADER_END), aad).decrypt(
      envelope.subarray(HEADER_END),
    );
  } catch {
    return fail("authentication");
  }
  const { meta, body } = inner(() => parseSealedInner(plain));
  return { epoch, meta, body };
}

const wrapKey = (squadId: string, epoch: string) => `sealed/.squad/${squadId}/epoch/${epoch}`;

/** Takes a snapshot already; never re-reads caller input. */
function wrapArgs(input: SquadEpochWrapInput): SealInput {
  const { did, squadId, epoch } = input;
  const recipient = own(input.recipient);
  const epochKey = own(input.epochKey);
  assertSquadId(squadId);
  assertEpoch(epoch);
  assertEpochKey(epochKey);
  return {
    recipient,
    did,
    key: wrapKey(squadId, epoch),
    meta: { content_type: EPOCH_KEY_CONTENT_TYPE, name: `${squadId}/epoch/${epoch}`, tags: [] },
    body: epochKey.slice(),
  };
}

/** One unchanged agentland-sealed/1 envelope to a recipient already passed through
 * verifySquadEpochRecipients (C-5). Sealed errors propagate unchanged. */
export function wrapEpochKey(input: SquadEpochWrapInput): SquadEpochWrap {
  const args = wrapArgs(snapshot(input, badInput));
  return { kid: recipientKeyId(args.recipient), envelope: base64urlEncode(sealEntry(args)) };
}

/** Vectors and tests only; not in the package barrel. */
export function wrapEpochKeyWithRandomness(
  input: SquadEpochWrapInput,
  randomness: SealRandomness,
): SquadEpochWrap {
  const args = wrapArgs(snapshot(input, badInput));
  return {
    kid: recipientKeyId(args.recipient),
    envelope: base64urlEncode(sealEntryWithRandomness(args, ownRandomness(randomness))),
  };
}

function ownRandomness(randomness: SealRandomness): SealRandomness {
  const r = snapshot(randomness, badInput);
  return { ephemeralSecretKey: own(r.ephemeralSecretKey), nonce: own(r.nonce) };
}

/** Opens only the wrap addressed to the keyring's kid (openSealedEntry), and only an epoch key. */
export function openEpochWrap(input: {
  readonly envelope: string;
  readonly did: string;
  readonly squadId: string;
  readonly epoch: string;
  readonly keyring: readonly Uint8Array[];
}): Uint8Array {
  const s = snapshot(input, badInput);
  const { envelope, did, squadId, epoch } = s;
  const keyring = Array.isArray(s.keyring) ? s.keyring.map(own) : s.keyring;
  assertSquadId(squadId);
  assertEpoch(epoch);
  const opened = openSealedEntry(decodeBase64url(envelope), {
    did,
    key: wrapKey(squadId, epoch),
    keyring,
  });
  if (opened.meta.content_type !== EPOCH_KEY_CONTENT_TYPE || opened.meta.size !== 32)
    fail("epoch_key");
  return opened.body;
}

const big = (seq: string) => BigInt(seq);

/** A member-set change (accept, leave, remove, attest_leave) strictly after `afterSeq` and, when
 * given, strictly before `beforeSeq`. `role` and `invite` never open or close an interval. */
function changedBetween(replay: SquadReplaySuccess, afterSeq: string, beforeSeq?: string): boolean {
  const inside = (seq: string | undefined) =>
    seq !== undefined &&
    big(seq) > big(afterSeq) &&
    (beforeSeq === undefined || big(seq) < big(beforeSeq));
  return replay.members.some((m) => inside(m.from_seq) || inside(m.until_seq));
}

// 16-09/16-12's DB sealed arm must accept and refuse exactly what these do (trigger = verifier);
// the enc-key half of C-6 needs DID histories and is verifySquadEpochRecipients's `fresh`.

/** C-5/C-27: every current member's served key is verified (self custody, signature, pin) before
 * any wrap; EncKeyRecipientError propagates. Callers wrap only the returned recipients. */
export function verifySquadEpochRecipients(input: {
  readonly replay: SquadReplaySuccess;
  readonly histories: readonly SquadRecipientHistory[];
}): { recipients: readonly VerifiedSquadRecipient[]; fresh: boolean } {
  const { replay, histories } = snapshot(input, () => fail("members"));
  if (replay?.valid !== true || !Array.isArray(replay.members) || !Array.isArray(histories))
    fail("members");
  const members = replay.members.filter((m) => m.until_seq === undefined).map((m) => m.did);
  const dids = histories.map((h) => h.did);
  if (
    members.length === 0 ||
    dids.length !== members.length ||
    new Set(dids).size !== dids.length ||
    dids.some((did) => !members.includes(did))
  )
    fail("members");
  const recipients = members
    .map((did) => {
      const h = histories.find((entry) => entry.did === did)!;
      const pin = h.pinnedSigningKey;
      const v = verifyEncKeyRecipient(
        h.history,
        did,
        own(h.publicKey),
        pin === undefined ? {} : { pinnedSigningKey: pin },
      );
      return { did, publicKey: v.publicKey, kid: v.recipientKeyId, signingKey: v.signingKey };
    })
    .sort((a, b) => (a.kid < b.kid ? -1 : a.kid > b.kid ? 1 : 0));
  const latest = replay.epochs[replay.epochs.length - 1];
  const fresh =
    latest !== undefined &&
    !changedBetween(replay, latest.seq) &&
    latest.recipients.length === recipients.length &&
    !latest.recipients.some((kid, i) => kid !== recipients[i]!.kid);
  return { recipients, fresh };
}

const SCHEMA: VerificationFailure = {
  valid: false,
  error: { stage: "schema", reason: "invalid-schema-or-trust-pins" },
};

/** The entries must be exactly the replayed chain: same squad, linked from genesis by
 * prev_hash, ending at the replay's head. Returns the payloads by seq, or null. */
function payloadMap(
  replay: SquadReplaySuccess,
  entries: readonly SquadEntry[],
  payloads: readonly SquadStatementPayload[],
): Map<string, Uint8Array> | null {
  if (
    replay?.valid !== true ||
    !Array.isArray(entries) ||
    entries.length !== replay.entries ||
    !Array.isArray(payloads)
  )
    return null;
  let prev = squadGenesis(replay.squad_id);
  for (let i = 0; i < entries.length; i += 1) {
    const entry = entries[i]!;
    if (entry.squad_id !== replay.squad_id || entry.prev_hash !== prev) return null;
    prev = hashSquadEntry(entry);
  }
  if (prev !== replay.head_hash || entries[entries.length - 1]?.seq !== replay.head_seq)
    return null;
  const map = new Map<string, Uint8Array>();
  for (let i = 0; i < payloads.length; i += 1) {
    const p = payloads[i]!;
    assertSequence(p.seq);
    if (!(p.content instanceof Uint8Array) || map.has(p.seq)) return null;
    map.set(p.seq, own(p.content));
  }
  return map;
}

function sealedReason(
  replay: SquadReplaySuccess,
  entry: SquadEntry,
  content: Uint8Array | undefined,
): string | undefined {
  if (content === undefined) return "payload-missing";
  if (bytesToHex(sha256(content)) !== entry.content_hash) return "payload-mismatch";
  let epoch: string;
  try {
    if (entry.content_type !== SQUAD_SEALED_CONTENT_TYPE || entry.tags.length !== 0)
      return "sealed-envelope";
    epoch = headerOf(content).epoch;
  } catch {
    return "sealed-envelope";
  }
  let current: SquadReplaySuccess["epochs"][number] | undefined;
  for (let i = 0; i < replay.epochs.length; i += 1)
    if (big(replay.epochs[i]!.seq) < big(entry.seq)) current = replay.epochs[i];
  if (
    current === undefined ||
    current.epoch !== epoch ||
    changedBetween(replay, current.seq, entry.seq)
  )
    return "epoch-stale";
  return undefined;
}

/** Shape and freshness of every `sealed/` put, in chain order; never decrypts. Operates only on
 * one structuredClone snapshot of the input, iterated by index. */
export function checkSquadSealedEntries(input: {
  readonly replay: SquadReplaySuccess;
  readonly entries: readonly SquadEntry[];
  readonly payloads: readonly SquadStatementPayload[];
}): SquadSealedCheckResult {
  let s: typeof input;
  let map: Map<string, Uint8Array> | null;
  try {
    s = structuredClone(input);
    map = payloadMap(s.replay, s.entries, s.payloads);
  } catch {
    return SCHEMA;
  }
  if (map === null) return SCHEMA;
  for (let index = 0; index < s.entries.length; index += 1) {
    const entry = s.entries[index]!;
    if (entry.op !== "put" || !entry.key.startsWith("sealed/")) continue;
    const reason = sealedReason(s.replay, entry, map.get(entry.seq));
    if (reason !== undefined) return { valid: false, error: { stage: "sealed", reason, index } };
  }
  return { valid: true };
}
