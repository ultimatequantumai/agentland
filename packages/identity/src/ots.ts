import { createHash } from "node:crypto";

/**
 * OpenTimestamps wire format (python-opentimestamps core/{serialize,timestamp,op,notary}.py),
 * pure and dependency-free (D-24). Bitcoin attestations are read, never verified here: the
 * official `ots` client and block explorers do that (D-26).
 */
export class OtsFormatError extends Error {
  override readonly name = "OtsFormatError";
}

export type OtsOp = { readonly tag: 0x03 | 0x08 | 0xf0 | 0xf1; readonly arg?: Uint8Array };
export type OtsAttestation =
  | { readonly kind: "pending"; readonly uri: string }
  | { readonly kind: "bitcoin"; readonly height: number }
  | { readonly kind: "unknown"; readonly tag: Uint8Array; readonly payload: Uint8Array };
export interface OtsNode {
  readonly msg: Uint8Array;
  attestations: OtsAttestation[];
  ops: Array<[OtsOp, OtsNode]>;
}

/** The official client's default aggregator pool; same strings as `audit_root_anchors.calendar`. */
export const OTS_AGGREGATORS = [
  "https://a.pool.opentimestamps.org",
  "https://b.pool.opentimestamps.org",
  "https://a.pool.eternitywall.com",
  "https://ots.btc.catallaxy.com",
] as const;

const HEADER_MAGIC = Buffer.from(
  "004f70656e54696d657374616d7073000050726f6f6600bf89e2e884e89294",
  "hex",
);
const PENDING_TAG = Buffer.from("83dfe30d2ef90c8e", "hex");
const BITCOIN_TAG = Buffer.from("0588960d73d71901", "hex");
const EMPTY = new Uint8Array();
const MAX_MSG = 4096; // message and op result
const MAX_ARG = 4096;
const MAX_PAYLOAD = 8192;
const MAX_DEPTH = 256;
const URI_RULE = /^[A-Za-z0-9._/:-]{1,1000}$/;
const CALENDAR_HOST =
  /^([a-z0-9-]+\.)+calendar\.(opentimestamps\.org|eternitywall\.com|catallaxy\.com)$/;

class Reader {
  private offset = 0;
  private readonly input: Uint8Array;
  constructor(input: Uint8Array) {
    this.input = input;
  }
  bytes(length: number): Uint8Array {
    if (this.offset + length > this.input.length) throw new OtsFormatError("truncated input");
    return this.input.slice(this.offset, (this.offset += length));
  }
  byte(): number {
    return this.bytes(1)[0]!;
  }
  /** Unsigned LEB128, at most 8 bytes, and only values that stay exact as JS numbers. */
  varuint(): number {
    let value = 0;
    let scale = 1;
    let byte: number;
    do {
      byte = this.byte();
      value += (byte & 0x7f) * scale;
      scale *= 128;
    } while (byte >= 0x80 && scale <= 2 ** 49);
    if (byte >= 0x80 || value > Number.MAX_SAFE_INTEGER) {
      throw new OtsFormatError("varuint exceeds 2^53");
    }
    return value;
  }
  varbytes(min: number, max: number, what: string): Uint8Array {
    const length = this.varuint();
    if (length < min || length > max) throw new OtsFormatError(`${what} out of range`);
    return this.bytes(length);
  }
  end(): void {
    if (this.offset !== this.input.length) throw new OtsFormatError("trailing bytes");
  }
}

function varuint(value: number): number[] {
  const out: number[] = [];
  do {
    const low = value % 128;
    value = Math.floor(value / 128);
    out.push(value > 0 ? low | 0x80 : low);
  } while (value > 0);
  return out;
}
const varbytes = (value: Uint8Array) =>
  Buffer.concat([Uint8Array.from(varuint(value.length)), value]);

function sized(msg: Uint8Array): Uint8Array {
  if (msg.length > MAX_MSG) throw new OtsFormatError("message length exceeds 4096");
  return msg;
}

function applyOp(op: OtsOp, msg: Uint8Array): Uint8Array {
  if (op.tag === 0xf0) return sized(Buffer.concat([msg, op.arg!]));
  if (op.tag === 0xf1) return sized(Buffer.concat([op.arg!, msg]));
  return createHash(op.tag === 0x08 ? "sha256" : "ripemd160")
    .update(msg)
    .digest();
}

/** Fail closed: sha1, keccak256, reverse, hexlify and unknown tags are refused (Pitfall R6). */
function parseOp(reader: Reader, tag: number): OtsOp {
  const known = tag as OtsOp["tag"];
  if (tag === 0x08 || tag === 0x03) return { tag: known };
  if (tag === 0xf0 || tag === 0xf1) {
    return { tag: known, arg: reader.varbytes(1, MAX_ARG, "argument length") };
  }
  throw new OtsFormatError(`unsupported op 0x${tag.toString(16).padStart(2, "0")}`);
}

/** Unknown attestation tags are preserved byte-exact (Pitfall R6). */
function parseAttestation(reader: Reader): OtsAttestation {
  const tag = reader.bytes(8);
  const payload = reader.varbytes(0, MAX_PAYLOAD, "attestation payload length");
  if (Buffer.compare(tag, PENDING_TAG) === 0) {
    const inner = new Reader(payload);
    const uri = Buffer.from(inner.varbytes(0, 1000, "pending uri length")).toString("latin1");
    if (!URI_RULE.test(uri)) throw new OtsFormatError("pending uri has invalid characters");
    inner.end();
    return { kind: "pending", uri };
  }
  if (Buffer.compare(tag, BITCOIN_TAG) === 0) {
    const inner = new Reader(payload);
    const height = inner.varuint();
    inner.end();
    return { kind: "bitcoin", height };
  }
  return { kind: "unknown", tag, payload };
}

function parseNode(reader: Reader, msg: Uint8Array, depth: number): OtsNode {
  if (depth > MAX_DEPTH) throw new OtsFormatError("nesting depth exceeds 256");
  const node: OtsNode = { msg, attestations: [], ops: [] };
  const item = (tag: number) => {
    if (tag === 0x00) {
      addAttestation(node, parseAttestation(reader));
      return;
    }
    const op = parseOp(reader, tag);
    addOp(node, op, parseNode(reader, applyOp(op, msg), depth + 1));
  };
  let tag = reader.byte();
  while (tag === 0xff) {
    item(reader.byte());
    tag = reader.byte();
  }
  item(tag);
  return node;
}

const attestationTag = (item: OtsAttestation) =>
  item.kind === "pending" ? PENDING_TAG : item.kind === "bitcoin" ? BITCOIN_TAG : item.tag;

function attestationPayload(item: OtsAttestation): Uint8Array {
  if (item.kind === "pending") return varbytes(Buffer.from(item.uri));
  if (item.kind === "bitcoin") return Uint8Array.from(varuint(item.height));
  return item.payload;
}

/** python TimeAttestation.__lt__: tag bytes, then URI string, integer height or raw payload. */
function compareAttestations(left: OtsAttestation, right: OtsAttestation): number {
  const byTag = Buffer.compare(attestationTag(left), attestationTag(right));
  if (byTag !== 0) return byTag;
  if (left.kind === "bitcoin" && right.kind === "bitcoin") return left.height - right.height;
  // UTF-8 byte order equals python's code point order for str.
  const key = (item: OtsAttestation) =>
    item.kind === "pending" ? Buffer.from(item.uri) : attestationPayload(item);
  return Buffer.compare(key(left), key(right));
}

const compareOps = (left: OtsOp, right: OtsOp) =>
  left.tag - right.tag || Buffer.compare(left.arg ?? EMPTY, right.arg ?? EMPTY);

function addAttestation(node: OtsNode, item: OtsAttestation): void {
  if (!node.attestations.some((existing) => compareAttestations(existing, item) === 0)) {
    node.attestations.push(item);
  }
}

/** Equal ops on equal messages yield equal children, so their subtrees merge. */
function addOp(node: OtsNode, op: OtsOp, child: OtsNode): void {
  const existing = node.ops.find(([other]) => compareOps(other, op) === 0);
  if (existing) mergeNode(existing[1], child);
  else node.ops.push([op, child]);
}

function mergeNode(target: OtsNode, source: OtsNode): void {
  for (const item of source.attestations) addAttestation(target, item);
  for (const [op, child] of source.ops) addOp(target, op, clone(child));
}

function clone(node: OtsNode): OtsNode {
  return {
    msg: node.msg,
    attestations: [...node.attestations],
    ops: node.ops.map(([op, child]) => [op, clone(child)]),
  };
}

const allNodes = (node: OtsNode): OtsNode[] => [
  node,
  ...node.ops.flatMap(([, child]) => allNodes(child)),
];

/** Exact-length parse of a timestamp rooted at `msg`; any violation throws OtsFormatError. */
export function parseTimestamp(bytes: Uint8Array, msg: Uint8Array): OtsNode {
  const reader = new Reader(bytes);
  const node = parseNode(reader, sized(Uint8Array.from(msg)), 1);
  reader.end();
  return node;
}

function writeNode(node: OtsNode, out: Uint8Array[]): void {
  const attestations = [...node.attestations].sort(compareAttestations);
  const ops = [...node.ops].sort(([left], [right]) => compareOps(left, right));
  if (attestations.length + ops.length === 0) {
    throw new OtsFormatError("cannot serialize an empty timestamp node");
  }
  attestations.forEach((item, index) => {
    const last = ops.length === 0 && index === attestations.length - 1;
    out.push(Uint8Array.of(...(last ? [] : [0xff]), 0x00), attestationTag(item));
    out.push(varbytes(attestationPayload(item)));
  });
  ops.forEach(([op, child], index) => {
    if (index < ops.length - 1) out.push(Uint8Array.of(0xff));
    out.push(Uint8Array.of(op.tag));
    if (op.arg) out.push(varbytes(op.arg));
    writeNode(child, out);
  });
}

/** python Timestamp.serialize order, so calendar responses round-trip byte for byte. */
export function serializeTimestamp(node: OtsNode): Uint8Array {
  const out: Uint8Array[] = [];
  writeNode(node, out);
  return Buffer.concat(out);
}

/** New tree where every node whose message is `commitment` gains the upgrade (python merge). */
export function mergeAt(root: OtsNode, commitment: Uint8Array, upgrade: OtsNode): OtsNode {
  if (Buffer.compare(upgrade.msg, commitment) !== 0) {
    throw new OtsFormatError("upgrade does not start at the commitment");
  }
  const out = clone(root);
  const targets = allNodes(out).filter((node) => Buffer.compare(node.msg, commitment) === 0);
  if (targets.length === 0) throw new OtsFormatError("commitment not in tree");
  for (const target of targets) mergeNode(target, upgrade);
  return out;
}

export function pendingCommitments(root: OtsNode): Array<{ uri: string; commitment: Uint8Array }> {
  return allNodes(root).flatMap((node) =>
    node.attestations.flatMap((item) =>
      item.kind === "pending" ? [{ uri: item.uri, commitment: node.msg }] : [],
    ),
  );
}

export function bitcoinHeights(root: OtsNode): number[] {
  return allNodes(root).flatMap((node) =>
    node.attestations.flatMap((item) => (item.kind === "bitcoin" ? [item.height] : [])),
  );
}

/** Detached file: HEADER_MAGIC ‖ major 1 ‖ sha256 file-hash op ‖ digest ‖ timestamp. */
export function detachedOts(digest: Uint8Array, node: OtsNode): Uint8Array {
  if (digest.length !== 32 || Buffer.compare(digest, node.msg) !== 0) {
    throw new OtsFormatError("digest must be the 32-byte message of the timestamp");
  }
  return Buffer.concat([HEADER_MAGIC, Uint8Array.of(0x01, 0x08), digest, serializeTimestamp(node)]);
}

export function parseDetachedOts(bytes: Uint8Array): { digest: Uint8Array; node: OtsNode } {
  const reader = new Reader(bytes);
  if (Buffer.compare(reader.bytes(HEADER_MAGIC.length), HEADER_MAGIC) !== 0) {
    throw new OtsFormatError("bad header magic");
  }
  if (reader.byte() !== 0x01) throw new OtsFormatError("unsupported major version");
  if (reader.byte() !== 0x08) throw new OtsFormatError("unsupported file hash op");
  const digest = reader.bytes(32);
  const node = parseNode(reader, digest, 1);
  reader.end();
  return { digest, node };
}

/**
 * SSRF guard for pending URIs (Pitfall R5): an exact https origin (no userinfo, port, path,
 * query or fragment) on the official client's three default calendar domains.
 */
export function matchesCalendarWhitelist(uri: string): boolean {
  if (!URI_RULE.test(uri)) return false;
  let url: URL;
  try {
    url = new URL(uri);
  } catch {
    return false;
  }
  return (
    url.protocol === "https:" &&
    url.origin === uri &&
    url.port === "" &&
    CALENDAR_HOST.test(url.hostname)
  );
}

/**
 * C11: per calendar the upgraded receipt if stored, else the submitted one; failed rows and
 * rows without bytes never contribute. Merged at the root into one detached file, or null.
 */
export function mergedReceipt(
  rows: readonly {
    readonly calendar: string;
    readonly status: "submitted" | "upgraded" | "failed";
    readonly ots: Uint8Array | null;
  }[],
): Uint8Array | null {
  const upgraded = new Set(
    rows.filter((row) => row.status === "upgraded" && row.ots).map((row) => row.calendar),
  );
  const receipts = rows
    .filter(
      (row) =>
        row.ots &&
        (row.status === "upgraded" || (row.status === "submitted" && !upgraded.has(row.calendar))),
    )
    .map((row) => parseDetachedOts(row.ots!));
  if (receipts.length === 0) return null;
  const { digest, node } = receipts[0]!;
  const merged = clone(node);
  for (const next of receipts.slice(1)) {
    if (Buffer.compare(next.digest, digest) !== 0) {
      throw new OtsFormatError("receipts commit to different digests");
    }
    mergeNode(merged, next.node);
  }
  return detachedOts(digest, merged);
}
