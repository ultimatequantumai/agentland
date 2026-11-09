import { secp256k1 } from "@noble/curves/secp256k1.js";
import { keccak_256 } from "@noble/hashes/sha3.js";
import { assertBytes, utf8Bytes } from "./json.js";

/**
 * agentland-anchor/1 (D-45…D-48, C-19…C-25): the daily second anchor. A notary, nothing else:
 * one zero-value self-send per published root whose input is the root's payload text. This
 * module never holds a private key (Cloud KMS signs, 15-13); it builds the EIP-1559 signing
 * hash, turns KMS DER into a low-s signature with its recovery bit, serializes, strictly decodes
 * and runs the signing guard. No wallet library (non-negotiable 5, T15): RLP and the strict
 * decoder are the few lines below. No `node:`, no `Buffer`: the verifier runs anywhere.
 */
export const ANCHOR_FORMAT = "agentland-anchor/1";
export const ANCHOR_PAYLOAD_PREFIX = "agentland-audit-root/1";
export const ANCHOR_MIN_GAS = 21_000;
export const ANCHOR_MAX_GAS = 100_000;

export interface AnchorTransactionFields {
  readonly chainId: bigint;
  readonly nonce: bigint;
  readonly maxPriorityFeePerGas: bigint;
  readonly maxFeePerGas: bigint;
  readonly gasLimit: bigint;
  readonly to: string;
  readonly value: bigint;
  readonly data: Uint8Array;
}
export interface AnchorExpectation {
  readonly chainId: bigint;
  readonly address: string;
  readonly payload: Uint8Array;
  readonly maxFeePerGasCap: bigint;
}
type Reason =
  "value" | "destination" | "payload" | "chain" | "fee_cap" | "gas" | "signature" | "encoding";
type Signature = { readonly r: bigint; readonly s: bigint; readonly yParity: 0 | 1 };

export class AnchorGuardError extends Error {
  override readonly name = "AnchorGuardError";
  constructor(readonly reason: Reason) {
    super(`${ANCHOR_FORMAT}: ${reason}`);
  }
}

const N = secp256k1.Point.CURVE().n;
const HEX = Array.from({ length: 256 }, (_, i) => i.toString(16).padStart(2, "0"));
const SPKI_PREFIX = "3056301006072a8648ce3d020106052b8104000a034200";
const ADDRESS = /^0x[0-9a-f]{40}$/u;

const hex = (bytes: Uint8Array) => Array.from(bytes, (b) => HEX[b]).join("");
function unhex(text: string): Uint8Array {
  const out = new Uint8Array(text.length / 2);
  for (let i = 0; i < out.length; i++) out[i] = Number.parseInt(text.slice(2 * i, 2 * i + 2), 16);
  return out;
}
function concat(...parts: readonly Uint8Array[]): Uint8Array {
  const out = new Uint8Array(parts.reduce((n, p) => n + p.length, 0));
  let at = 0;
  for (const p of parts) {
    out.set(p, at);
    at += p.length;
  }
  return out;
}
function intBytes(n: bigint): Uint8Array {
  if (n === 0n) return new Uint8Array(0);
  const text = n.toString(16);
  return unhex(text.length % 2 ? "0" + text : text);
}
// Byte inputs are snapshotted through intrinsics that read the TypedArray internal slots:
// subclasses, proxies and foreign typed arrays cannot show one byte sequence to the check and
// another to serialization. Not `slice`: it dispatches to a subclass's species constructor.
const TYPED_ARRAY = Object.getPrototypeOf(Uint8Array.prototype) as object;
const TYPED_TAG = Object.getOwnPropertyDescriptor(TYPED_ARRAY, Symbol.toStringTag)!.get!;
const TYPED_LENGTH = Object.getOwnPropertyDescriptor(TYPED_ARRAY, "length")!.get!;
const TYPED_SET = Uint8Array.prototype.set;
function snapshotBytes(value: unknown): Uint8Array {
  // The tag getter returns undefined (never throws) for anything without the internal slot.
  if (TYPED_TAG.call(value) !== "Uint8Array") return encoding();
  const copy = new Uint8Array(TYPED_LENGTH.call(value) as number);
  TYPED_SET.call(copy, value as Uint8Array);
  return copy;
}
function bytesEqual(left: Uint8Array, right: Uint8Array): boolean {
  const a = snapshotBytes(left);
  const b = snapshotBytes(right);
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
  return true;
}

// RLP, Ethereum Yellow Paper Appendix B, for byte strings and lists only.
type Rlp = Uint8Array | readonly Rlp[];
function rlpLength(length: number, offset: number): Uint8Array {
  if (length < 56) return Uint8Array.of(offset + length);
  const bytes = intBytes(BigInt(length));
  return concat(Uint8Array.of(offset + 55 + bytes.length), bytes);
}
function rlp(item: Rlp): Uint8Array {
  if (item instanceof Uint8Array)
    return item.length === 1 && item[0]! < 0x80 ? item : concat(rlpLength(item.length, 0x80), item);
  const body = concat(...item.map(rlp));
  return concat(rlpLength(body.length, 0xc0), body);
}

const encoding = (): never => {
  throw new AnchorGuardError("encoding");
};
// Strict decoder: canonical length prefixes only, every byte accounted for. Lists nest at most
// two deep (the transaction and its empty access list), so deeper input is refused, not recursed.
function decodeItem(bytes: Uint8Array, at: number, depth: number): { item: Rlp; end: number } {
  const first = bytes[at] ?? encoding();
  if (first < 0x80) return { item: bytes.subarray(at, at + 1), end: at + 1 };
  const isList = first >= 0xc0;
  const short = first - (isList ? 0xc0 : 0x80);
  let start = at + 1;
  let length = short;
  if (short > 55) {
    const lengthOfLength = short - 55;
    const prefix = bytes.subarray(start, start + lengthOfLength);
    if (prefix.length !== lengthOfLength || prefix[0] === 0) encoding();
    length = prefix.reduce((n, b) => n * 256 + b, 0);
    if (length < 56) encoding();
    start += lengthOfLength;
  }
  const end = start + length;
  if (end > bytes.length) encoding();
  if (!isList) {
    if (length === 1 && bytes[start]! < 0x80) encoding();
    return { item: bytes.subarray(start, end), end };
  }
  if (depth > 2) encoding();
  const items: Rlp[] = [];
  for (let cursor = start; cursor < end;) {
    const next = decodeItem(bytes, cursor, depth + 1);
    if (next.end > end) encoding();
    items.push(next.item);
    cursor = next.end;
  }
  return { item: items, end };
}
const asBytes = (item: Rlp | undefined): Uint8Array =>
  item instanceof Uint8Array ? item : encoding();
function asInt(item: Rlp | undefined): bigint {
  const bytes = asBytes(item);
  if (bytes[0] === 0) encoding();
  return bytes.length === 0 ? 0n : BigInt("0x" + hex(bytes));
}

export function anchorPayload(date: string, rootHex: string): Uint8Array {
  const match = /^([0-9]{4})-([0-9]{2})-([0-9]{2})$/u.exec(date);
  const [year, month, day] = match ? match.slice(1).map(Number) : [0, 0, 0];
  const leap = year! % 4 === 0 && (year! % 100 !== 0 || year! % 400 === 0);
  const days = [31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month! - 1] ?? 0;
  if (day! < 1 || day! > days)
    throw new TypeError("Anchor date must be a UTC calendar day YYYY-MM-DD");
  if (!/^[0-9a-f]{64}$/u.test(rootHex))
    throw new TypeError("Anchor root must be 64 lowercase hex characters");
  return utf8Bytes(`${ANCHOR_PAYLOAD_PREFIX} ${date} ${rootHex}`);
}

const natural = (n: unknown): n is bigint => typeof n === "bigint" && n >= 0n;
const isAddress = (x: unknown): x is string => typeof x === "string" && ADDRESS.test(x);
const naturalOrFail = (n: unknown): bigint => (natural(n) ? n : encoding());
const addressOrFail = (x: unknown): string => (isAddress(x) ? x : encoding());

// Every input is read once and reduced to primitives (bigints, primitive strings, copied bytes)
// before any use, so an object cannot show the guard one value and the signing hash another.
function snapshotFields(f: AnchorTransactionFields): AnchorTransactionFields {
  return {
    chainId: naturalOrFail(f.chainId),
    nonce: naturalOrFail(f.nonce),
    maxPriorityFeePerGas: naturalOrFail(f.maxPriorityFeePerGas),
    maxFeePerGas: naturalOrFail(f.maxFeePerGas),
    gasLimit: naturalOrFail(f.gasLimit),
    to: addressOrFail(f.to),
    value: naturalOrFail(f.value),
    data: snapshotBytes(f.data),
  };
}

/** A transaction that passed the guard: the only input the signing hash and serializer accept. */
export type GuardedAnchorTransaction = AnchorTransactionFields & { readonly guarded: true };
// Guarded object → the module's private snapshot. Signing reads only the private snapshot, so
// neither getters on the caller's input nor writes to the returned object's bytes reach the hash.
const guardedSnapshots = new WeakMap<object, AnchorTransactionFields>();

/**
 * The signing guard. It takes no signature: 15-13 runs it before any KMS call, then hashes and
 * serializes the returned snapshot, and runs it again on the decoded transaction.
 */
export function assertAnchorTransaction(
  input: AnchorTransactionFields,
  expectedInput: AnchorExpectation,
): GuardedAnchorTransaction {
  const fields = snapshotFields(input);
  const expected: AnchorExpectation = {
    chainId: naturalOrFail(expectedInput.chainId),
    address: addressOrFail(expectedInput.address),
    payload: snapshotBytes(expectedInput.payload),
    maxFeePerGasCap: naturalOrFail(expectedInput.maxFeePerGasCap),
  };
  if (fields.chainId !== expected.chainId) throw new AnchorGuardError("chain");
  if (fields.value !== 0n) throw new AnchorGuardError("value");
  if (fields.to !== expected.address) throw new AnchorGuardError("destination");
  if (!bytesEqual(fields.data, expected.payload)) throw new AnchorGuardError("payload");
  // With both fee bounds and the gas window, gasLimit × maxFeePerGas ≤ cap × 100,000 holds by construction.
  if (
    fields.maxFeePerGas > expected.maxFeePerGasCap ||
    fields.maxPriorityFeePerGas > fields.maxFeePerGas
  )
    throw new AnchorGuardError("fee_cap");
  if (fields.gasLimit < BigInt(ANCHOR_MIN_GAS) || fields.gasLimit > BigInt(ANCHOR_MAX_GAS))
    throw new AnchorGuardError("gas");
  const guarded: GuardedAnchorTransaction = Object.freeze({
    ...fields,
    data: fields.data.slice(),
    guarded: true as const,
  });
  guardedSnapshots.set(guarded, Object.freeze(fields));
  return guarded;
}

function guardedSnapshot(guarded: GuardedAnchorTransaction): AnchorTransactionFields {
  const fields =
    typeof guarded === "object" && guarded !== null ? guardedSnapshots.get(guarded) : undefined;
  if (!fields) throw new TypeError("Anchor transaction must come from assertAnchorTransaction");
  return fields;
}

const unsignedList = (f: AnchorTransactionFields): Rlp[] => [
  intBytes(f.chainId),
  intBytes(f.nonce),
  intBytes(f.maxPriorityFeePerGas),
  intBytes(f.maxFeePerGas),
  intBytes(f.gasLimit),
  unhex(f.to.slice(2)),
  intBytes(f.value),
  f.data,
  [],
];
const signingHashOf = (f: AnchorTransactionFields) =>
  keccak_256(concat(Uint8Array.of(0x02), rlp(unsignedList(f))));

export function anchorSigningHash(guarded: GuardedAnchorTransaction): Uint8Array {
  return signingHashOf(guardedSnapshot(guarded));
}

/** The 65-byte uncompressed point of an 88-byte secp256k1 SPKI, checked on the curve. */
function spkiPoint(spkiDer: Uint8Array): Uint8Array {
  assertBytes(spkiDer);
  if (spkiDer.length !== 88 || hex(spkiDer.subarray(0, 23)) !== SPKI_PREFIX)
    throw new TypeError("secp256k1 SPKI required");
  const point = spkiDer.subarray(23);
  try {
    secp256k1.Point.fromBytes(point);
  } catch {
    throw new TypeError("secp256k1 SPKI required");
  }
  return point;
}
const addressOf = (point: Uint8Array) => "0x" + hex(keccak_256(point.subarray(1)).subarray(12));

export function evmAddressFromSpki(spkiDer: Uint8Array): string {
  return addressOf(spkiPoint(spkiDer));
}

function recover(r: bigint, s: bigint, yParity: number, hash: Uint8Array): Uint8Array | undefined {
  try {
    return new secp256k1.Signature(r, s)
      .addRecoveryBit(yParity)
      .recoverPublicKey(hash)
      .toBytes(false);
  } catch {
    return undefined;
  }
}

export function anchorSignatureFromDer(
  der: Uint8Array,
  signingHash: Uint8Array,
  publicKeySpki: Uint8Array,
): Signature {
  assertBytes(der);
  assertBytes(signingHash);
  if (signingHash.length !== 32) throw new TypeError("32-byte signing hash required");
  const point = spkiPoint(publicKeySpki);
  let parsed: { r: bigint; s: bigint };
  try {
    parsed = secp256k1.Signature.fromBytes(der, "der");
  } catch {
    throw new AnchorGuardError("signature");
  }
  // EIP-2: only the low half of s is valid; KMS may return either.
  const s = parsed.s > N / 2n ? N - parsed.s : parsed.s;
  for (const yParity of [0, 1] as const) {
    const key = recover(parsed.r, s, yParity, signingHash);
    if (key && bytesEqual(key, point)) return { r: parsed.r, s, yParity };
  }
  throw new AnchorGuardError("signature");
}

const validSignature = ({ r, s, yParity }: Signature) =>
  r >= 1n && r < N && s >= 1n && s <= N / 2n && (yParity === 0 || yParity === 1);

/**
 * Accepts a guarded snapshot or plain fields (15-16 rebuilds third-party transactions; no fee cap).
 * Plain fields are read once into primitives. Serializing other fields than were signed is harmless:
 * the sender recovers to another address, which verifyAnchorTransaction and 15-13 refuse.
 */
export function serializeAnchorTransaction(
  input: AnchorTransactionFields | GuardedAnchorTransaction,
  signature: { r: bigint; s: bigint; yParity: 0 | 1 },
): Uint8Array {
  if (typeof input !== "object" || input === null) encoding();
  const fields = guardedSnapshots.get(input) ?? snapshotFields(input);
  // Read each signature member once; validSignature and the encoder see the same values.
  const sig: Signature = { r: signature.r, s: signature.s, yParity: signature.yParity };
  if (typeof sig.r !== "bigint" || typeof sig.s !== "bigint" || !validSignature(sig))
    throw new AnchorGuardError("signature");
  return concat(
    Uint8Array.of(0x02),
    rlp([...unsignedList(fields), intBytes(BigInt(sig.yParity)), intBytes(sig.r), intBytes(sig.s)]),
  );
}

export function decodeAnchorTransaction(raw: Uint8Array): AnchorTransactionFields & {
  readonly signature: { r: bigint; s: bigint; yParity: 0 | 1 };
  readonly from: string;
  readonly hash: string;
} {
  assertBytes(raw);
  if (raw[0] !== 0x02) encoding();
  const { item, end } = decodeItem(raw, 1, 1);
  if (end !== raw.length || item instanceof Uint8Array || item.length !== 12) encoding();
  const list = item as readonly Rlp[];
  const to = asBytes(list[5]);
  const accessList = list[8];
  if (to.length !== 20 || !Array.isArray(accessList) || accessList.length !== 0) encoding();
  const parity = asInt(list[9]);
  if (parity > 1n) encoding();
  const fields: AnchorTransactionFields = {
    chainId: asInt(list[0]),
    nonce: asInt(list[1]),
    maxPriorityFeePerGas: asInt(list[2]),
    maxFeePerGas: asInt(list[3]),
    gasLimit: asInt(list[4]),
    to: "0x" + hex(to),
    value: asInt(list[6]),
    data: asBytes(list[7]).slice(),
  };
  const signature = { r: asInt(list[10]), s: asInt(list[11]), yParity: Number(parity) as 0 | 1 };
  if (!validSignature(signature)) throw new AnchorGuardError("signature");
  const key = recover(signature.r, signature.s, signature.yParity, signingHashOf(fields));
  if (!key) throw new AnchorGuardError("signature");
  return { ...fields, signature, from: addressOf(key), hash: "0x" + hex(keccak_256(raw)) };
}

/** The offline verifier core: decides whether a fetched transaction anchors the published payload. */
export function verifyAnchorTransaction(
  raw: Uint8Array,
  expected: Omit<AnchorExpectation, "maxFeePerGasCap">,
): { readonly hash: string; readonly from: string } {
  if (typeof expected.address !== "string" || !ADDRESS.test(expected.address))
    throw new TypeError("EVM address required");
  const tx = decodeAnchorTransaction(raw);
  if (tx.chainId !== expected.chainId) throw new AnchorGuardError("chain");
  if (tx.value !== 0n) throw new AnchorGuardError("value");
  if (tx.to !== expected.address) throw new AnchorGuardError("destination");
  if (!bytesEqual(tx.data, expected.payload)) throw new AnchorGuardError("payload");
  if (tx.from !== expected.address) throw new AnchorGuardError("signature");
  return { hash: tx.hash, from: tx.from };
}

/** Tests only (C-21): EIP-7623's calldata floor over EIP-2028; production uses eth_estimateGas within the guard. */
export function currentRuleGas(dataLength: number, nonZeroBytes: number): number {
  if (
    !Number.isInteger(dataLength) ||
    !Number.isInteger(nonZeroBytes) ||
    nonZeroBytes < 0 ||
    nonZeroBytes > dataLength
  )
    throw new RangeError("nonZeroBytes must be an integer from 0 to dataLength");
  const zero = dataLength - nonZeroBytes;
  return Math.max(21_000 + 16 * nonZeroBytes + 4 * zero, 21_000 + 10 * (zero + 4 * nonZeroBytes));
}
