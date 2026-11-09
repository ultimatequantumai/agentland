import { assertBytes, sha256Hex } from "./canonical.js";
import { assertAgentDid } from "./did.js";
import { assertSequence } from "./vault.js";

export interface ArchiveFile {
  readonly name: string;
  readonly bytes: Uint8Array;
}
export interface ExportManifest {
  readonly format: "agentland-vault/1";
  readonly did: string;
  readonly files: readonly {
    readonly name: string;
    readonly sha256: string;
    readonly size: number;
  }[];
}

/** D-10 archive layout. proofs/ holds only real Merkle proofs; none exist before Phase 5 roots. */
export const EXPORT_LAYOUT = {
  manifest: "manifest.json",
  didHistory: "did-history.json",
  head: "head.json",
  record: "record.json",
  entry: (seq: string) => {
    assertSequence(seq);
    return `entries/${seq}.json`;
  },
  payload: (seq: string) => {
    assertSequence(seq);
    return `payloads/${seq}.bin`;
  },
  proof: (seq: string) => {
    assertSequence(seq);
    return `proofs/${seq}.json`;
  },
} as const;

const BLOCK = 512;
const MAX_SIZE = 8 ** 11; // 11 octal digits in the ustar size field

// Archive names are ours: printable ASCII, ≤100 bytes (no ustar prefix), relative, no dot segments.
function assertName(name: unknown): asserts name is string {
  if (
    typeof name !== "string" ||
    !/^[\x21-\x7e]{1,100}$/.test(name) ||
    name.startsWith("/") ||
    name.split("/").some((part) => part === "" || part === "." || part === "..")
  )
    throw new TypeError("Archive name must be relative printable ASCII of at most 100 bytes");
}

function octal(header: Uint8Array, offset: number, length: number, value: number): void {
  header.set(Buffer.from(`${value.toString(8).padStart(length - 1, "0")}\0`, "latin1"), offset);
}

function checksum(header: Uint8Array): number {
  let sum = 0;
  for (let i = 0; i < BLOCK; i++) sum += i >= 148 && i < 156 ? 0x20 : header[i]!;
  return sum;
}

/** One 512-byte ustar header: fixed mode 0644, uid/gid 0, mtime 0, regular file. */
function ustarHeader(name: string, size: number): Uint8Array {
  const header = new Uint8Array(BLOCK);
  header.set(Buffer.from(name, "latin1"), 0);
  octal(header, 100, 8, 0o644);
  octal(header, 108, 8, 0);
  octal(header, 116, 8, 0);
  octal(header, 124, 12, size);
  octal(header, 136, 12, 0);
  header[156] = 0x30; // regular file
  header.set(Buffer.from("ustar\x0000", "latin1"), 257);
  octal(header, 148, 7, checksum(header));
  header[155] = 0x20;
  return header;
}

/** Deterministic POSIX ustar stream: fixed mode/owner/mtime, regular files only; gzip belongs to the caller. */
export function* writeUstar(files: Iterable<ArchiveFile>): Generator<Uint8Array> {
  const seen = new Set<string>();
  for (const file of files) {
    assertName(file.name);
    assertBytes(file.bytes);
    if (seen.has(file.name)) throw new TypeError("Duplicate archive name");
    seen.add(file.name);
    if (file.bytes.length >= MAX_SIZE) throw new RangeError("Archive file too large");
    yield ustarHeader(file.name, file.bytes.length);
    if (file.bytes.length > 0) {
      yield file.bytes;
      const pad = (BLOCK - (file.bytes.length % BLOCK)) % BLOCK;
      if (pad > 0) yield new Uint8Array(pad);
    }
  }
  yield new Uint8Array(BLOCK * 2);
}

export interface StreamedArchiveFile {
  readonly name: string;
  readonly size: number;
  readonly chunks: AsyncIterable<Uint8Array>;
}

/**
 * Streaming twin of writeUstar: same deterministic ustar bytes; body chunks pass through uncopied,
 * so memory is bounded by the caller's chunk size; a member whose bytes differ from its declared
 * size throws.
 */
export async function* writeUstarStream(
  files: AsyncIterable<StreamedArchiveFile>,
): AsyncGenerator<Uint8Array> {
  const seen = new Set<string>();
  for await (const file of files) {
    assertName(file.name);
    if (seen.has(file.name)) throw new TypeError("Duplicate archive name");
    seen.add(file.name);
    const { size } = file;
    if (!Number.isSafeInteger(size) || size < 0)
      throw new RangeError("Archive member size must be a non-negative integer");
    if (size >= MAX_SIZE) throw new RangeError("Archive file too large");
    yield ustarHeader(file.name, size);
    let written = 0;
    for await (const chunk of file.chunks) {
      assertBytes(chunk);
      // Refuse before yielding: an over-long chunk must never reach the archive.
      if (written + chunk.length > size)
        throw new RangeError("Archive member bytes exceed its declared size");
      written += chunk.length;
      if (chunk.length > 0) yield chunk;
    }
    if (written < size) throw new RangeError("Archive member bytes are short of its declared size");
    const pad = (BLOCK - (size % BLOCK)) % BLOCK;
    if (pad > 0) yield new Uint8Array(pad);
  }
  yield new Uint8Array(BLOCK * 2);
}

function field(header: Buffer, offset: number, length: number): string {
  const raw = header.subarray(offset, offset + length);
  const end = raw.indexOf(0);
  return raw.subarray(0, end === -1 ? length : end).toString("latin1");
}

function parseOctal(header: Buffer, offset: number, length: number): number {
  const text = field(header, offset, length).trim();
  if (!/^[0-7]+$/.test(text)) throw new TypeError("Invalid ustar numeric field");
  return Number.parseInt(text, 8);
}

/** Reads the regular-file ustar subset writeUstar emits. */
export function readUstar(archive: Uint8Array): ArchiveFile[] {
  assertBytes(archive);
  const bytes = Buffer.from(archive.buffer, archive.byteOffset, archive.byteLength);
  const files: ArchiveFile[] = [];
  let offset = 0;
  while (offset + BLOCK <= bytes.length) {
    const header = bytes.subarray(offset, offset + BLOCK);
    if (header.every((byte) => byte === 0)) return files;
    if (parseOctal(header, 148, 8) !== checksum(header)) throw new TypeError("Bad ustar checksum");
    if (field(header, 257, 6) !== "ustar" || (header[156] !== 0x30 && header[156] !== 0))
      throw new TypeError("Unsupported ustar entry");
    const name = field(header, 0, 100);
    const size = parseOctal(header, 124, 12);
    const start = offset + BLOCK;
    if (start + size > bytes.length) throw new TypeError("Truncated ustar archive");
    files.push({ name, bytes: new Uint8Array(bytes.subarray(start, start + size)) });
    offset = start + Math.ceil(size / BLOCK) * BLOCK;
  }
  throw new TypeError("Missing ustar end blocks");
}

/** agentland-vault/1 manifest from precomputed digests: one validation and code-unit sort path. */
export function buildExportManifestFromDigests(input: {
  readonly did: string;
  readonly files: readonly {
    readonly name: string;
    readonly sha256: string;
    readonly size: number;
  }[];
}): ExportManifest {
  assertAgentDid(input.did);
  const seen = new Set<string>();
  const files = input.files.map(({ name, sha256, size }) => {
    assertName(name);
    if (seen.has(name)) throw new TypeError("Duplicate archive name");
    seen.add(name);
    if (typeof sha256 !== "string" || !/^[0-9a-f]{64}$/.test(sha256))
      throw new TypeError("Invalid manifest digest");
    if (!Number.isSafeInteger(size) || size < 0)
      throw new RangeError("Archive member size must be a non-negative integer");
    return { name, sha256, size };
  });
  files.sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0));
  return { format: "agentland-vault/1", did: input.did, files };
}

/** agentland-vault/1 manifest: per-file SHA-256 and size, sorted by code-unit name. */
export function buildExportManifest(input: {
  readonly did: string;
  readonly files: readonly ArchiveFile[];
}): ExportManifest {
  return buildExportManifestFromDigests({
    did: input.did,
    files: input.files.map((file) => ({
      name: file.name,
      sha256: sha256Hex(file.bytes),
      size: file.bytes.length,
    })),
  });
}
