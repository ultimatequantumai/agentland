import { spawnSync } from "node:child_process";
import { generateKeyPairSync } from "node:crypto";
import { gunzipSync, gzipSync } from "node:zlib";
import { describe, expect, it } from "vitest";
import { canonicalBytes, sha256Hex } from "../src/canonical.js";
import type { Ed25519PublicJwk } from "../src/keys.js";
import {
  createDeleteIntent,
  createPutIntent,
  hashVaultEntry,
  signVaultIntent,
  stampVaultEntry,
  validateVaultChain,
} from "../src/vault.js";
import type { VaultEntry, VaultIntent } from "../src/vault.js";
import { signVaultHead, verifySignedHead } from "../src/head.js";
import type { SignedVaultHead } from "../src/head.js";
import {
  EXPORT_LAYOUT,
  buildExportManifest,
  buildExportManifestFromDigests,
  readUstar,
  writeUstar,
  writeUstarStream,
} from "../src/export.js";
import type { ArchiveFile, ExportManifest, StreamedArchiveFile } from "../src/export.js";

function key() {
  const pair = generateKeyPairSync("ed25519");
  const { kty, crv, x } = pair.publicKey.export({ format: "jwk" });
  return {
    publicKeyJwk: { kty, crv, x } as Ed25519PublicJwk,
    privatePkcs8: pair.privateKey.export({ format: "der", type: "pkcs8" }),
  };
}
const did = "did:web:agentland.us:agents:weatherwise";
const utf8 = (text: string) => new Uint8Array(Buffer.from(text, "utf8"));
const archive = (files: Iterable<{ name: string; bytes: Uint8Array }>) =>
  Buffer.concat([...writeUstar(files)]);
const ascii = (block: Buffer, start: number, length: number) =>
  block
    .subarray(start, start + length)
    .toString("latin1")
    .replace(/\0.*$/s, "");
const octal = (block: Buffer, start: number, length: number) =>
  Number.parseInt(ascii(block, start, length).trim(), 8);
const hasBsdtar = spawnSync("bsdtar", ["--version"]).status === 0;

async function* chunksOf(bytes: Uint8Array, split?: number): AsyncGenerator<Uint8Array> {
  const step = split ?? Math.max(bytes.length, 1);
  for (let offset = 0; offset < bytes.length; offset += step)
    yield bytes.subarray(offset, offset + step);
}
/** Each ArchiveFile as a streamed member whose chunks cut its bytes every `split` bytes (whole when omitted). */
async function* streamed(
  files: Iterable<ArchiveFile>,
  split?: number,
): AsyncGenerator<StreamedArchiveFile> {
  for (const file of files)
    yield { name: file.name, size: file.bytes.length, chunks: chunksOf(file.bytes, split) };
}
async function* members(...files: StreamedArchiveFile[]): AsyncGenerator<StreamedArchiveFile> {
  yield* files;
}
async function collect(generator: AsyncIterable<Uint8Array>): Promise<Buffer> {
  const chunks: Uint8Array[] = [];
  for await (const chunk of generator) chunks.push(chunk);
  return Buffer.concat(chunks);
}
/** Drains until the writer throws; reports the error and how many bytes it yielded first. */
async function refusal(
  generator: AsyncIterable<Uint8Array>,
): Promise<{ error: unknown; yielded: number }> {
  let yielded = 0;
  try {
    for await (const chunk of generator) yielded += chunk.length;
  } catch (error) {
    return { error, yielded };
  }
  throw new Error("writeUstarStream accepted an invalid member");
}
/** A chunk source that records whether the writer ever read from it. */
function probe(): { pulled: boolean; chunks: AsyncIterable<Uint8Array> } {
  const state = { pulled: false };
  async function* chunks() {
    state.pulled = true;
    yield utf8("x");
  }
  return Object.assign(state, { chunks: chunks() });
}

const small = [
  { name: "a.txt", bytes: utf8("hello") },
  { name: "empty.bin", bytes: new Uint8Array() },
  { name: "dir/block.bin", bytes: new Uint8Array(512).fill(7) },
];

describe("writeUstar", () => {
  it("emits 512-byte headers, zero-padded bodies and two zero end blocks", () => {
    const tar = archive(small);
    // a.txt: header + 1 body block; empty.bin: header only; block.bin: header + 1 body; end: 2.
    expect(tar.length).toBe(512 * 7);
    expect(tar.subarray(512 * 5).equals(Buffer.alloc(1024))).toBe(true);
    expect(tar.subarray(512 + 5, 1024).equals(Buffer.alloc(512 - 5))).toBe(true);

    const header = tar.subarray(0, 512);
    expect(ascii(header, 0, 100)).toBe("a.txt");
    expect(octal(header, 124, 12)).toBe(5);
    expect(octal(header, 136, 12)).toBe(0); // fixed mtime keeps bytes deterministic
    expect(String.fromCharCode(header[156]!)).toBe("0");
    expect(header.subarray(257, 263).toString("latin1")).toBe("ustar\0");
    expect(header.subarray(263, 265).toString("latin1")).toBe("00");
    const unsigned = Buffer.from(header);
    unsigned.fill(0x20, 148, 156);
    expect(octal(header, 148, 8)).toBe(unsigned.reduce((sum, byte) => sum + byte, 0));
    expect(tar.subarray(512, 517).toString("utf8")).toBe("hello");
  });

  it("is deterministic and round-trips through readUstar", () => {
    expect(archive(small).equals(archive(small))).toBe(true);
    const read = readUstar(archive(small));
    expect(read.map((file) => file.name)).toEqual(small.map((file) => file.name));
    read.forEach((file, i) =>
      expect(Buffer.from(file.bytes).equals(Buffer.from(small[i]!.bytes))).toBe(true),
    );
  });

  it("accepts a 100-character ASCII name and rejects unsafe or ambiguous names", () => {
    const name100 = "x".repeat(100);
    expect(readUstar(archive([{ name: name100, bytes: utf8("ok") }]))[0]!.name).toBe(name100);
    for (const name of [
      "x".repeat(101),
      "café.json",
      "",
      "/etc/passwd",
      "entries/../x",
      "../x",
      "a\0b",
    ])
      expect(() => archive([{ name, bytes: utf8("x") }]), name).toThrow();
    expect(() =>
      archive([
        { name: "same.json", bytes: utf8("1") },
        { name: "same.json", bytes: utf8("2") },
      ]),
    ).toThrow();
  });

  it("readUstar rejects corrupted, unsupported, truncated or unterminated archives", () => {
    const corrupt = archive(small);
    corrupt[0] = "b".charCodeAt(0);
    expect(() => readUstar(corrupt)).toThrow();
    const directory = archive(small);
    directory[156] = "5".charCodeAt(0);
    const header = Buffer.from(directory.subarray(0, 512));
    header.fill(0x20, 148, 156);
    const sum = header.reduce((total, byte) => total + byte, 0);
    directory.write(`${sum.toString(8).padStart(6, "0")}\0 `, 148, "latin1");
    expect(() => readUstar(directory)).toThrow();
    expect(() => readUstar(archive(small).subarray(0, 512 * 4 + 100))).toThrow();
    expect(() => readUstar(archive(small).subarray(0, 512 * 5))).toThrow();
    expect(() => readUstar(new Uint8Array(1024).fill(0x41))).toThrow();
  });

  it.skipIf(!hasBsdtar)("produces archives a stock tar lists and extracts", () => {
    const gz = gzipSync(archive(small));
    const list = spawnSync("bsdtar", ["-tzf", "-"], { input: gz });
    expect(list.status).toBe(0);
    expect(list.stdout.toString("utf8").trim().split("\n")).toEqual(small.map((file) => file.name));
    const extract = spawnSync("bsdtar", ["-xOzf", "-", "a.txt"], { input: gz });
    expect(extract.stdout.toString("utf8")).toBe("hello");
  });
});

describe("buildExportManifest", () => {
  it("lists every file's SHA-256 and size sorted by name under agentland-vault/1", () => {
    const files = [
      { name: "entries/2.json", bytes: utf8("two") },
      { name: "entries/10.json", bytes: utf8("ten") },
      { name: "did-history.json", bytes: utf8("{}") },
    ];
    expect(buildExportManifest({ did, files })).toEqual({
      format: "agentland-vault/1",
      did,
      files: [
        { name: "did-history.json", sha256: sha256Hex(utf8("{}")), size: 2 },
        { name: "entries/10.json", sha256: sha256Hex(utf8("ten")), size: 3 },
        { name: "entries/2.json", sha256: sha256Hex(utf8("two")), size: 3 },
      ],
    });
  });

  it("rejects a non-agent DID and duplicate names", () => {
    expect(() => buildExportManifest({ did: "did:web:example.com", files: [] })).toThrow();
    expect(() =>
      buildExportManifest({
        did,
        files: [
          { name: "a", bytes: utf8("1") },
          { name: "a", bytes: utf8("2") },
        ],
      }),
    ).toThrow();
  });

  it("names the archive layout", () => {
    expect(EXPORT_LAYOUT.manifest).toBe("manifest.json");
    expect(EXPORT_LAYOUT.didHistory).toBe("did-history.json");
    expect(EXPORT_LAYOUT.head).toBe("head.json");
    expect(EXPORT_LAYOUT.record).toBe("record.json");
    expect(EXPORT_LAYOUT.entry("12")).toBe("entries/12.json");
    expect(EXPORT_LAYOUT.payload("12")).toBe("payloads/12.bin");
    expect(EXPORT_LAYOUT.proof("12")).toBe("proofs/12.json");
  });
});

describe("writeUstarStream", () => {
  it("is byte-identical to writeUstar", async () => {
    const files = [
      ...small,
      ...[1, 511, 512, 513, 1_025].map((length) => ({
        name: `sized/${length}.bin`,
        bytes: Uint8Array.from({ length }, (_, i) => (i * 31 + 7) % 251),
      })),
    ];
    for (const split of [1, 7, 512, undefined])
      expect(
        (await collect(writeUstarStream(streamed(files, split)))).equals(archive(files)),
        `split ${split ?? "whole"}`,
      ).toBe(true);
    expect((await collect(writeUstarStream(streamed([])))).equals(Buffer.alloc(1_024))).toBe(true);
  });

  it("refuses a member whose bytes differ from its declared size", async () => {
    const short = await refusal(
      writeUstarStream(members({ name: "short.bin", size: 5, chunks: chunksOf(utf8("abcd")) })),
    );
    expect(short.error).toBeInstanceOf(RangeError);
    expect((short.error as Error).message).toMatch(/size/);

    const long = await refusal(
      writeUstarStream(members({ name: "long.bin", size: 4, chunks: chunksOf(utf8("abcde")) })),
    );
    expect(long.error).toBeInstanceOf(RangeError);
    expect((long.error as Error).message).toMatch(/size/);
    // The over-long chunk never leaves the writer: at most the header and the declared bytes.
    expect(long.yielded).toBeLessThanOrEqual(512 + 4);

    const first = { name: "first.txt", bytes: utf8("ok") };
    const firstMember = archive([first]).length - 1_024; // header + one padded body block
    for (const size of [-1, 1.5, 8 ** 11]) {
      const source = probe();
      const bad = await refusal(
        writeUstarStream(
          members(
            { name: first.name, size: first.bytes.length, chunks: chunksOf(first.bytes) },
            { name: "bad.bin", size, chunks: source.chunks },
          ),
        ),
      );
      expect(bad.error, String(size)).toBeInstanceOf(RangeError);
      expect(bad.yielded, String(size)).toBe(firstMember);
      expect(source.pulled, String(size)).toBe(false);
    }
  });

  it("refuses unsafe and duplicate names like writeUstar", async () => {
    for (const name of ["../x", "/abs", "x".repeat(101)]) {
      const { error } = await refusal(writeUstarStream(streamed([{ name, bytes: utf8("x") }])));
      expect(error, name).toBeInstanceOf(TypeError);
      expect((error as Error).message, name).toBe(
        "Archive name must be relative printable ASCII of at most 100 bytes",
      );
    }
    const duplicate = await refusal(
      writeUstarStream(
        streamed([
          { name: "a.txt", bytes: utf8("1") },
          { name: "a.txt", bytes: utf8("2") },
        ]),
      ),
    );
    expect(duplicate.error).toBeInstanceOf(TypeError);
    expect((duplicate.error as Error).message).toBe("Duplicate archive name");
  });

  it("passes body chunks through without copying or buffering", async () => {
    const source = new Uint8Array(65_536).fill(0xab);
    async function* body(): AsyncGenerator<Uint8Array> {
      for (let i = 0; i < 4_096; i++) yield source;
    }
    const start = process.memoryUsage().arrayBuffers;
    let peak = start;
    let total = 0;
    let index = 0;
    let firstBody: Uint8Array | undefined;
    // The consumer counts bytes and keeps no reference beyond the first body chunk (the source itself).
    for await (const chunk of writeUstarStream(
      members({ name: "big.bin", size: 268_435_456, chunks: body() }),
    )) {
      if (index === 1) firstBody = chunk;
      total += chunk.length;
      index += 1;
      if (index % 256 === 0) peak = Math.max(peak, process.memoryUsage().arrayBuffers);
    }
    peak = Math.max(peak, process.memoryUsage().arrayBuffers);
    expect(firstBody).toBe(source);
    expect(total).toBe(512 + 268_435_456 + 1_024);
    expect(peak).toBeLessThanOrEqual(start + 33_554_432);
  }, 60_000);
});

describe("buildExportManifestFromDigests", () => {
  const digests = small.map((file) => ({
    name: file.name,
    sha256: sha256Hex(file.bytes),
    size: file.bytes.length,
  }));

  it("produces the same manifest bytes as buildExportManifest", () => {
    expect(
      Buffer.from(canonicalBytes(buildExportManifestFromDigests({ did, files: digests }))).equals(
        Buffer.from(canonicalBytes(buildExportManifest({ did, files: small }))),
      ),
    ).toBe(true);
  });

  it("rejects malformed digests and sizes, duplicate names and a non-agent DID", () => {
    // Calling a missing export would throw a TypeError and pass the loop below by accident.
    expect(buildExportManifestFromDigests).toBeTypeOf("function");
    const first = digests[0]!;
    const cases = [
      { did, files: [{ ...first, sha256: "x" }] },
      { did, files: [{ ...first, sha256: "a".repeat(63) }] },
      { did, files: [{ ...first, size: -1 }] },
      { did, files: [{ ...first, size: 1.5 }] },
      { did, files: [first, first] },
      { did: "did:web:example.com", files: digests },
    ];
    for (const [index, input] of cases.entries()) {
      let error: unknown;
      try {
        buildExportManifestFromDigests(input);
      } catch (caught) {
        error = caught;
      }
      expect([TypeError, RangeError], `case ${index}`).toContain(
        (error as Error | undefined)?.constructor,
      );
    }
  });
});

describe("agentland-vault/1 export round trip", () => {
  it("re-verifies every manifest hash, the vault chain and the signed head offline", () => {
    const agent = key();
    const platform = key();
    const stamp = (intent: VaultIntent, ts_server: string) =>
      stampVaultEntry(
        { intent, sig_agent: signVaultIntent(intent, agent.privatePkcs8), ts_server },
        agent.publicKeyJwk,
      );
    const payloads = new Map([
      ["1", utf8("lesson: check the radar")],
      ["3", utf8("lesson: restored")],
    ]);
    const entries: VaultEntry[] = [];
    let prev = sha256Hex(utf8(did));
    for (const [seq, ts] of [
      ["1", "2026-10-20T00:00:00.000Z"],
      ["2", "2026-10-21T00:00:00.000Z"],
      ["3", "2026-10-22T00:00:00.000Z"],
    ] as const) {
      const content = payloads.get(seq);
      const intent = content
        ? createPutIntent({ seq, key: "vault/lesson", content, prev_hash: prev })
        : createDeleteIntent({ seq, key: "vault/lesson", prev_hash: prev });
      entries.push(stamp(intent, ts));
      prev = hashVaultEntry(entries.at(-1)!);
    }
    const head = signVaultHead(
      {
        did,
        seq: "3",
        head_hash: prev,
        ts: "2026-10-22T00:00:01.000Z",
        kid: "did:web:agentland.us#head-key-1",
      },
      platform.privatePkcs8,
    );
    const files = [
      { name: EXPORT_LAYOUT.didHistory, bytes: canonicalBytes({ did, keys: [] }) },
      { name: EXPORT_LAYOUT.head, bytes: canonicalBytes(head) },
      { name: EXPORT_LAYOUT.record, bytes: canonicalBytes({ did }) },
      ...entries.map((entry) => ({
        name: EXPORT_LAYOUT.entry(entry.seq),
        bytes: canonicalBytes(entry),
      })),
      ...[...payloads].map(([seq, bytes]) => ({ name: EXPORT_LAYOUT.payload(seq), bytes })),
    ];
    const manifest = buildExportManifest({ did, files });
    const gz = gzipSync(
      archive([{ name: EXPORT_LAYOUT.manifest, bytes: canonicalBytes(manifest) }, ...files]),
    );

    // Offline consumer: only the archive bytes and the published keys.
    const read = new Map(
      readUstar(gunzipSync(gz)).map((file) => [file.name, Buffer.from(file.bytes)]),
    );
    const parsed = JSON.parse(read.get("manifest.json")!.toString("utf8")) as ExportManifest;
    expect(parsed.format).toBe("agentland-vault/1");
    expect(parsed.did).toBe(did);
    expect(parsed.files.map((file) => file.name).sort()).toEqual(
      [...read.keys()].filter((name) => name !== "manifest.json").sort(),
    );
    for (const file of parsed.files) {
      expect(sha256Hex(read.get(file.name)!), file.name).toBe(file.sha256);
      expect(read.get(file.name)!.length).toBe(file.size);
    }

    const extracted = ["1", "2", "3"].map(
      (seq) => JSON.parse(read.get(`entries/${seq}.json`)!.toString("utf8")) as VaultEntry,
    );
    for (const entry of extracted)
      if (entry.op === "put")
        expect(sha256Hex(read.get(`payloads/${entry.seq}.bin`)!)).toBe(entry.content_hash);
    const signedHead = JSON.parse(read.get("head.json")!.toString("utf8")) as SignedVaultHead;
    expect(verifySignedHead(signedHead, platform.publicKeyJwk)).toBe(true);
    expect(
      validateVaultChain({
        did,
        entries: extracted,
        keys: [{ from_seq: "1", publicKeyJwk: agent.publicKeyJwk }],
        expectedHead: { seq: signedHead.seq, head_hash: signedHead.head_hash },
      }),
    ).toEqual({ valid: true, did, entries: 3, head_seq: "3", head_hash: prev });
  });
});
