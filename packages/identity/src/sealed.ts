// agentland-sealed/1 (D-09…D-13, C-4…C-6): X25519 → HKDF-SHA256 → XChaCha20-Poly1305.
// Client code: the server only calls `sealedEnvelopeRecipient` and `recipientKeyId` and never sees
// a key or plaintext (non-negotiable 10). Entries are opened by recipient key id, never by trial
// decryption (RESEARCH F3 note: XChaCha20-Poly1305 is not key-committing).
// No `node:`, no Node globals: runs on Node, Bun and browsers. Randomness comes only from
// noble's WebCrypto-backed `randomBytes` / `randomSecretKey`.
// The inner layout is shared with agentland-squad-sealed/1 (squad-sealed.ts).
import { xchacha20poly1305 } from "@noble/ciphers/chacha.js";
import { randomBytes } from "@noble/ciphers/utils.js";
import { x25519 } from "@noble/curves/ed25519.js";
import { hkdf } from "@noble/hashes/hkdf.js";
import { sha256 } from "@noble/hashes/sha2.js";
import {
  assertAgentDid,
  assertBytes,
  canonicalize,
  exactMembers,
  parseIJson,
  utf8Bytes,
} from "./json.js";

export const SEALED_FORMAT = "agentland-sealed/1";
export const SEALED_CONTENT_TYPE = "application/vnd.agentland.sealed";
export const SEALED_MAGIC_HEX = "414c5301"; // "ALS" + 0x01
export const SEALED_OVERHEAD = 108; // 4 + 32 + 32 + 24 + 16
export const SEALED_PAD_UNIT = 256;
export const SEALED_MIN_ENVELOPE = 364;
// Largest valid envelope under the unchanged 64,000-byte payload bound (C-6).
export const SEALED_MAX_ENVELOPE = 63_852;
export const SEALED_MAX_INNER = 63_744;

const MAGIC = Uint8Array.of(0x41, 0x4c, 0x53, 0x01);
const KEY_LENGTH = 32;
const NONCE_LENGTH = 24;
const NONCE_END = 4 + 32 + 32 + NONCE_LENGTH;
// Any clamped scalar is a multiple of 8, so X25519(PROBE, u) is all-zero exactly for the
// small-order u (the libsodium blacklist, with or without the top bit).
const PROBE = new Uint8Array(32).fill(1);
const HEX = Array.from({ length: 256 }, (_, byte) => byte.toString(16).padStart(2, "0"));

export type SealedFailure =
  | "magic"
  | "length"
  | "public_key"
  | "low_order"
  | "recipient_unknown"
  | "authentication"
  | "meta_length"
  | "size"
  | "padding"
  | "meta";

export class SealedEnvelopeError extends Error {
  readonly reason: SealedFailure;
  constructor(reason: SealedFailure) {
    super(`agentland-sealed/1: ${reason}`);
    this.name = "SealedEnvelopeError";
    this.reason = reason;
  }
}

export interface SealedMeta {
  readonly content_type: string;
  readonly name: string;
  readonly tags: readonly string[];
}
export interface SealInput {
  readonly recipient: Uint8Array;
  readonly did: string;
  readonly key: string;
  readonly meta: SealedMeta;
  readonly body: Uint8Array;
}
export interface OpenedSealedEntry {
  readonly meta: SealedMeta & { readonly size: number };
  readonly body: Uint8Array;
  readonly recipientKeyId: string;
}
export interface EncryptionKeyPair {
  readonly secretKey: Uint8Array;
  readonly publicKey: Uint8Array;
}
export interface SealRandomness {
  readonly ephemeralSecretKey: Uint8Array;
  readonly nonce: Uint8Array;
}

function fail(reason: SealedFailure): never {
  throw new SealedEnvelopeError(reason);
}

function hex(bytes: Uint8Array): string {
  let text = "";
  for (const byte of bytes) text += HEX[byte];
  return text;
}

function concat(...parts: readonly Uint8Array[]): Uint8Array {
  const out = new Uint8Array(parts.reduce((total, part) => total + part.length, 0));
  let offset = 0;
  for (const part of parts) {
    out.set(part, offset);
    offset += part.length;
  }
  return out;
}

function u32be(n: number): Uint8Array {
  const out = new Uint8Array(4);
  new DataView(out.buffer).setUint32(0, n);
  return out;
}

const is32 = (value: unknown): value is Uint8Array =>
  value instanceof Uint8Array && value.length === KEY_LENGTH;

function x25519Shared(secret: Uint8Array, publicKey: Uint8Array): Uint8Array {
  if (!is32(secret) || !is32(publicKey)) fail("public_key");
  try {
    return x25519.getSharedSecret(secret, publicKey);
  } catch {
    // With both inputs 32 bytes, noble only throws on the all-zero (small-order) result.
    return fail("low_order");
  }
}

export function assertEncryptionPublicKey(publicKey: unknown): asserts publicKey is Uint8Array {
  if (!is32(publicKey)) fail("public_key");
  x25519Shared(PROBE, publicKey);
}

/** Lowercase hex SHA-256 of the 32-byte X25519 public key. */
export function recipientKeyId(publicKey: Uint8Array): string {
  if (!is32(publicKey)) fail("public_key");
  return hex(sha256(publicKey));
}

export function encryptionPublicKey(secretKey: Uint8Array): Uint8Array {
  if (!is32(secretKey)) fail("public_key");
  return x25519.getPublicKey(secretKey);
}

export function generateEncryptionKey(): EncryptionKeyPair {
  const secretKey = x25519.utils.randomSecretKey();
  return { secretKey, publicKey: x25519.getPublicKey(secretKey) };
}

/** max(256, ⌈(4 + n)/256⌉·256): n = len(meta) + len(body). */
export function sealedInnerLength(metaAndBodyLength: number): number {
  if (!Number.isSafeInteger(metaAndBodyLength) || metaAndBodyLength < 0)
    throw new RangeError("Inner length must be a nonnegative integer");
  return Math.max(
    SEALED_PAD_UNIT,
    Math.ceil((4 + metaAndBodyLength) / SEALED_PAD_UNIT) * SEALED_PAD_UNIT,
  );
}

/** Structural check only ("magic" | "length"); returns the recipient key id. */
export function sealedEnvelopeRecipient(envelope: Uint8Array): string {
  assertBytes(envelope);
  if (envelope.length < 4 || MAGIC.some((byte, i) => envelope[i] !== byte)) fail("magic");
  if (
    envelope.length < SEALED_MIN_ENVELOPE ||
    envelope.length > SEALED_MAX_ENVELOPE ||
    (envelope.length - SEALED_OVERHEAD) % SEALED_PAD_UNIT !== 0
  )
    fail("length");
  return hex(envelope.subarray(4, 36));
}

function assertSealedKey(key: unknown): asserts key is string {
  if (typeof key !== "string" || !/^sealed\/.+$/u.test(key))
    throw new TypeError("Sealed vault key required");
}

function assertMeta(meta: unknown): asserts meta is SealedMeta {
  const message = "Sealed meta requires content_type, name and tags";
  let record: Record<string, unknown>;
  try {
    record = exactMembers(meta, ["content_type", "name", "tags"]);
  } catch {
    throw new TypeError(message);
  }
  const { content_type, name, tags } = record;
  if (
    typeof content_type !== "string" ||
    typeof name !== "string" ||
    !Array.isArray(tags) ||
    tags.some((tag) => typeof tag !== "string")
  )
    throw new TypeError(message);
}

const aad = (did: string, key: string) =>
  utf8Bytes(canonicalize({ did, format: SEALED_FORMAT, key }));

const aeadKey = (shared: Uint8Array, ephemeral: Uint8Array, recipient: Uint8Array) =>
  hkdf(sha256, shared, concat(ephemeral, recipient), utf8Bytes(SEALED_FORMAT), 32);

/** Vectors and tests only. Reusing randomness for different content breaks confidentiality; it is
 * not in the package barrel. */
export function sealEntryWithRandomness(input: SealInput, randomness: SealRandomness): Uint8Array {
  const { recipient, did, key, meta, body } = input;
  assertAgentDid(did);
  assertSealedKey(key);
  assertMeta(meta);
  assertBytes(body);
  assertEncryptionPublicKey(recipient);
  const { ephemeralSecretKey, nonce } = randomness;
  if (!(nonce instanceof Uint8Array) || nonce.length !== NONCE_LENGTH)
    throw new TypeError("24-byte nonce required");
  const shared = x25519Shared(ephemeralSecretKey, recipient);
  const ephemeral = x25519.getPublicKey(ephemeralSecretKey);
  const inner = sealedInner(meta, body);
  const sealed = xchacha20poly1305(
    aeadKey(shared, ephemeral, recipient),
    nonce,
    aad(did, key),
  ).encrypt(inner);
  return concat(MAGIC, sha256(recipient), ephemeral, nonce, sealed);
}

/** Fresh ephemeral key and nonce per call; no default recipient (C-27). */
export function sealEntry(input: SealInput): Uint8Array {
  return sealEntryWithRandomness(input, {
    ephemeralSecretKey: x25519.utils.randomSecretKey(),
    nonce: randomBytes(NONCE_LENGTH),
  });
}

function parseMeta(bytes: Uint8Array): SealedMeta & { readonly size: number } {
  let text: string;
  let record: Record<string, unknown>;
  try {
    text = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
    record = exactMembers(parseIJson(text), ["content_type", "name", "size", "tags"]);
  } catch {
    return fail("meta");
  }
  const { content_type, name, size, tags } = record;
  if (
    typeof content_type !== "string" ||
    typeof name !== "string" ||
    typeof size !== "number" ||
    !Number.isSafeInteger(size) ||
    size < 0 ||
    !Array.isArray(tags) ||
    tags.some((tag) => typeof tag !== "string") ||
    canonicalize(record) !== text
  )
    fail("meta");
  return { content_type, name, size, tags: [...(tags as string[])] };
}

export function openSealedEntry(
  envelope: Uint8Array,
  context: { readonly did: string; readonly key: string; readonly keyring: readonly Uint8Array[] },
): OpenedSealedEntry {
  const { did, key, keyring } = context;
  assertAgentDid(did);
  assertSealedKey(key);
  if (!Array.isArray(keyring)) throw new TypeError("Keyring required");
  for (const secret of keyring) if (!is32(secret)) fail("public_key");
  const rid = sealedEnvelopeRecipient(envelope);
  // Selection by key id: exactly one AEAD attempt, never trial decryption.
  const secret = keyring.find((entry) => recipientKeyId(x25519.getPublicKey(entry)) === rid);
  if (secret === undefined) return fail("recipient_unknown");
  const recipient = x25519.getPublicKey(secret);
  const ephemeral = envelope.subarray(36, 68);
  const shared = x25519Shared(secret, ephemeral);
  let inner: Uint8Array;
  try {
    inner = xchacha20poly1305(
      aeadKey(shared, ephemeral, recipient),
      envelope.subarray(68, NONCE_END),
      aad(did, key),
    ).decrypt(envelope.subarray(NONCE_END));
  } catch {
    return fail("authentication");
  }
  return { ...parseSealedInner(inner), recipientKeyId: rid };
}

/** The inner layout, shared with agentland-squad-sealed/1 (squad-sealed.ts): u32be(len(meta)) ‖
 * meta ‖ body ‖ zero padding. Module export, not in the barrel. */
export function sealedInner(meta: SealedMeta, body: Uint8Array): Uint8Array {
  assertMeta(meta);
  assertBytes(body);
  const metaBytes = utf8Bytes(
    canonicalize({
      content_type: meta.content_type,
      name: meta.name,
      size: body.length,
      tags: [...meta.tags],
    }),
  );
  const raw = concat(u32be(metaBytes.length), metaBytes, body);
  if (raw.length > SEALED_MAX_INNER) fail("length");
  const inner = new Uint8Array(sealedInnerLength(metaBytes.length + body.length));
  inner.set(raw);
  return inner;
}

/** Post-decrypt checks in order: meta_length → meta → size → padding. Module export only. */
export function parseSealedInner(inner: Uint8Array): {
  meta: SealedMeta & { readonly size: number };
  body: Uint8Array;
} {
  const metaLength = new DataView(inner.buffer, inner.byteOffset, 4).getUint32(0);
  if (4 + metaLength > inner.length) fail("meta_length");
  const meta = parseMeta(inner.subarray(4, 4 + metaLength));
  const end = 4 + metaLength + meta.size;
  if (end > inner.length) fail("size");
  if (
    inner.length !== sealedInnerLength(metaLength + meta.size) ||
    inner.subarray(end).some((byte) => byte !== 0)
  )
    fail("padding");
  return { meta, body: inner.slice(4 + metaLength, end) };
}
