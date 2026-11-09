import { readFileSync } from "node:fs";
import { xchacha20poly1305 } from "@noble/ciphers/chacha.js";
import type * as Chacha from "@noble/ciphers/chacha.js";
import { describe, expect, it, vi } from "vitest";

// Pass-through spy: records the AEAD key of every decrypt so "opens" can prove that
// openSealedEntry decrypts exactly once, with the RID-selected key. Behavior is unchanged.
const decryptKeys: string[] = vi.hoisted(() => []);
vi.mock("@noble/ciphers/chacha.js", async (importOriginal) => {
  const actual = await importOriginal<typeof Chacha>();
  return {
    ...actual,
    xchacha20poly1305: (key: Uint8Array, nonce: Uint8Array, aad?: Uint8Array) => {
      const cipher = actual.xchacha20poly1305(key, nonce, aad);
      return {
        ...cipher,
        encrypt: (plaintext: Uint8Array) => cipher.encrypt(plaintext),
        decrypt: (ciphertext: Uint8Array) => {
          decryptKeys.push(Buffer.from(key).toString("hex"));
          return cipher.decrypt(ciphertext);
        },
      };
    },
  };
});
import {
  SEALED_CONTENT_TYPE,
  SEALED_FORMAT,
  SEALED_MAGIC_HEX,
  SEALED_MAX_ENVELOPE,
  SEALED_MAX_INNER,
  SEALED_MIN_ENVELOPE,
  SEALED_OVERHEAD,
  SEALED_PAD_UNIT,
  SealedEnvelopeError,
  assertEncryptionPublicKey,
  encryptionPublicKey,
  generateEncryptionKey,
  openSealedEntry,
  recipientKeyId,
  sealEntry,
  sealedEnvelopeRecipient,
  sha256Hex,
} from "../src/index.js";
import type { SealInput, SealedMeta } from "../src/index.js";
import { sealEntryWithRandomness, sealedInnerLength } from "../src/sealed.js";
import vectors from "./sealed-vectors.json" with { type: "json" };

// RESEARCH F2 / draft-irtf-cfrg-xchacha-03 §A.3.1 anchors: the generated file must reproduce them.
const ANCHORS = {
  shared: "4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742",
  aeadKey: "d51914e663f68f0e60c8a9239cb8ddcd1ebb7c047b092baf2a2dbacd2369c82e",
  nonce: "404142434445464748494a4b4c4d4e4f5051525354555657",
  contentHash: "142141121a3f4f341083806ec715c64d2cb1cdedffc9ef35d560269955c32838",
  rid: "f35e5616160a30bf3c6e79fa73c576d40205e8fc3ba4e1c6dcf93e6b98e857b4",
  katPrefix: "bd6d179d3e83d43b9576579493c0e939",
  katTag: "c0875924c1c7987947deafd8780acf49",
} as const;
const OTHER_DID = "did:web:agentland.us:agents:otheragent";
const NEGATIVE_NAMES = [
  "wrong-magic",
  "length-363",
  "length-365",
  "length-64108",
  "recipient-unknown",
  "aad-did",
  "aad-key",
  "tag-flip",
  "meta-length-past-end",
  "meta-not-canonical",
  "meta-extra-member",
  "meta-missing-member",
  "meta-size-not-integer",
  "size-past-end",
  "nonzero-padding",
  "surplus-padding",
] as const;

interface SealedVector {
  recipient_secret_hex: string;
  recipient_public_hex: string;
  recipient_key_id: string;
  ephemeral_secret_hex: string;
  ephemeral_public_hex: string;
  shared_hex: string;
  aead_key_hex: string;
  nonce_hex: string;
  did: string;
  key: string;
  aad_utf8: string;
  meta: SealedMeta;
  meta_utf8: string;
  body_utf8: string;
  inner_hex: string;
  envelope_hex: string;
  envelope_sha256: string;
}
interface NegativeVector {
  name: string;
  did: string;
  key: string;
  keyring_secret_hex: string;
  reason: string;
  envelope_hex?: string;
  prefix_hex?: string;
  total_length?: number;
}
interface MaxVector {
  meta: SealedMeta;
  body_rule: string;
  body_length: number;
  envelope_length: number;
  envelope_sha256: string;
}
interface VectorFile {
  format: string;
  xchacha_kat: {
    key_hex: string;
    nonce_hex: string;
    aad_hex: string;
    plaintext_utf8: string;
    ciphertext_hex: string;
  };
  v1: SealedVector;
  v2: SealedVector;
  low_order: { encodings: string[] };
  padding: { inner_length: [number, number][]; max: MaxVector };
  negatives: NegativeVector[];
}
const file = vectors as unknown as VectorFile;

const fail = (reason: string) => `agentland-sealed/1: ${reason}`;
const hex = (value: string) => new Uint8Array(Buffer.from(value, "hex"));
const toHex = (bytes: Uint8Array) => Buffer.from(bytes).toString("hex");
const utf8 = (text: string) => new TextEncoder().encode(text);
const input = (
  vector: SealedVector,
  recipient: Uint8Array = hex(vector.recipient_public_hex),
): SealInput => ({
  recipient,
  did: vector.did,
  key: vector.key,
  meta: vector.meta,
  body: utf8(vector.body_utf8),
});
const randomness = (vector: SealedVector) => ({
  ephemeralSecretKey: hex(vector.ephemeral_secret_hex),
  nonce: hex(vector.nonce_hex),
});
const opened = (vector: SealedVector) => ({
  meta: { ...vector.meta, size: utf8(vector.body_utf8).length },
  body: utf8(vector.body_utf8),
  recipientKeyId: vector.recipient_key_id,
});
const v1Envelope = () => hex(file.v1.envelope_hex);
const v1Open = (envelope: Uint8Array, did = file.v1.did, key = file.v1.key) =>
  openSealedEntry(envelope, { did, key, keyring: [hex(file.v1.recipient_secret_hex)] });
const zeroFilled = (prefix: Uint8Array, length: number) => {
  const bytes = new Uint8Array(length);
  bytes.set(prefix.subarray(0, Math.min(prefix.length, length)));
  return bytes;
};
const maxBody = (length: number) => Uint8Array.from({ length }, (_, i) => i % 251);
const lowOrderInputs = () =>
  file.low_order.encodings.flatMap((encoding) =>
    [0, 0x80].map((bit) => {
      const bytes = hex(encoding);
      bytes[31] = bytes[31]! | bit;
      return bytes;
    }),
  );
const caught = (run: () => unknown) => {
  try {
    run();
  } catch (error) {
    return error;
  }
  throw new Error("expected a throw");
};

describe("constants", () => {
  it("are exactly outline b.1.1", () => {
    expect(SEALED_FORMAT).toBe("agentland-sealed/1");
    expect(SEALED_CONTENT_TYPE).toBe("application/vnd.agentland.sealed");
    expect(SEALED_MAGIC_HEX).toBe("414c5301");
    expect(SEALED_OVERHEAD).toBe(108);
    expect(SEALED_PAD_UNIT).toBe(256);
    expect(SEALED_MIN_ENVELOPE).toBe(364);
    expect(SEALED_MAX_ENVELOPE).toBe(63_852);
    expect(SEALED_MAX_INNER).toBe(63_744);
  });

  it("derive from the layout and the 64,000-byte payload bound", () => {
    expect(SEALED_OVERHEAD).toBe(4 + 32 + 32 + 24 + 16);
    expect(SEALED_MIN_ENVELOPE).toBe(SEALED_OVERHEAD + SEALED_PAD_UNIT);
    expect(SEALED_MAX_ENVELOPE).toBe(
      SEALED_OVERHEAD + SEALED_PAD_UNIT * Math.floor((64_000 - SEALED_OVERHEAD) / SEALED_PAD_UNIT),
    );
    expect(SEALED_MAX_INNER).toBe(SEALED_MAX_ENVELOPE - SEALED_OVERHEAD);
  });

  it("the vector file is for SEALED_FORMAT", () => {
    expect(file.format).toBe(SEALED_FORMAT);
  });
});

describe("xchacha kat", () => {
  it("noble reproduces draft-irtf-cfrg-xchacha-03 §A.3.1", () => {
    const kat = file.xchacha_kat;
    const cipher = () => xchacha20poly1305(hex(kat.key_hex), hex(kat.nonce_hex), hex(kat.aad_hex));
    const sealed = cipher().encrypt(utf8(kat.plaintext_utf8));
    expect(toHex(sealed)).toBe(kat.ciphertext_hex);
    expect(kat.ciphertext_hex.startsWith(ANCHORS.katPrefix)).toBe(true);
    expect(kat.ciphertext_hex.endsWith(ANCHORS.katTag)).toBe(true);
    expect(new TextDecoder().decode(cipher().decrypt(sealed))).toBe(kat.plaintext_utf8);
  });
});

describe("vector V1", () => {
  it("seals to the published envelope", () => {
    expect(file.v1.shared_hex).toBe(ANCHORS.shared);
    expect(file.v1.aead_key_hex).toBe(ANCHORS.aeadKey);
    expect(file.v1.nonce_hex).toBe(ANCHORS.nonce);
    const envelope = sealEntryWithRandomness(input(file.v1), randomness(file.v1));
    expect(toHex(envelope)).toBe(file.v1.envelope_hex);
    expect(envelope.length).toBe(364);
    expect(sha256Hex(envelope)).toBe(ANCHORS.contentHash);
    expect(file.v1.envelope_sha256).toBe(ANCHORS.contentHash);
    expect(toHex(envelope.subarray(4, 36))).toBe(ANCHORS.rid);
  });

  it("recipient key id", () => {
    const rid = recipientKeyId(hex(file.v1.recipient_public_hex));
    expect(rid).toBe(ANCHORS.rid);
    expect(file.v1.recipient_key_id).toBe(ANCHORS.rid);
    expect(sealedEnvelopeRecipient(v1Envelope())).toBe(ANCHORS.rid);
  });

  it("public key", () => {
    expect(toHex(encryptionPublicKey(hex(file.v1.recipient_secret_hex)))).toBe(
      file.v1.recipient_public_hex,
    );
    expect(toHex(encryptionPublicKey(hex(file.v1.ephemeral_secret_hex)))).toBe(
      file.v1.ephemeral_public_hex,
    );
  });

  it("opens", () => {
    // A non-matching first keyring entry plus exactly one AEAD decrypt, under the V1 key,
    // proves selection by recipient key id with no trial decryption (RESEARCH A5).
    decryptKeys.length = 0;
    const result = openSealedEntry(v1Envelope(), {
      did: file.v1.did,
      key: file.v1.key,
      keyring: [hex(file.v1.ephemeral_secret_hex), hex(file.v1.recipient_secret_hex)],
    });
    expect(result).toStrictEqual({
      meta: {
        content_type: "text/plain; charset=utf-8",
        name: "notes/cpi.md",
        size: 59,
        tags: ["macro"],
      },
      body: utf8(file.v1.body_utf8),
      recipientKeyId: ANCHORS.rid,
    });
    expect(decryptKeys).toStrictEqual([file.v1.aead_key_hex]);
  });

  it("V2 (two blocks)", () => {
    const envelope = sealEntryWithRandomness(input(file.v2), randomness(file.v2));
    expect(toHex(envelope)).toBe(file.v2.envelope_hex);
    expect(envelope.length).toBe(620);
    expect(sha256Hex(envelope)).toBe(file.v2.envelope_sha256);
    expect(
      openSealedEntry(envelope, {
        did: file.v2.did,
        key: file.v2.key,
        keyring: [hex(file.v2.recipient_secret_hex)],
      }),
    ).toStrictEqual(opened(file.v2));
  });

  it("fresh randomness", () => {
    const first = sealEntry(input(file.v1));
    const second = sealEntry(input(file.v1));
    expect(toHex(first.subarray(36, 92))).not.toBe(toHex(second.subarray(36, 92)));
    for (const envelope of [first, second]) expect(v1Open(envelope)).toStrictEqual(opened(file.v1));
  });

  it("generated keys", () => {
    const pair = generateEncryptionKey();
    expect(pair.secretKey.length).toBe(32);
    expect(pair.publicKey.length).toBe(32);
    expect(toHex(encryptionPublicKey(pair.secretKey))).toBe(toHex(pair.publicKey));
    const envelope = sealEntry(input(file.v1, pair.publicKey));
    expect(
      openSealedEntry(envelope, { did: file.v1.did, key: file.v1.key, keyring: [pair.secretKey] }),
    ).toStrictEqual({ ...opened(file.v1), recipientKeyId: recipientKeyId(pair.publicKey) });
  });
});

describe("negative", () => {
  it("the file carries exactly the published negatives", () => {
    expect(file.negatives.map((entry) => entry.name)).toStrictEqual([...NEGATIVE_NAMES]);
  });

  it.each(NEGATIVE_NAMES.map((name) => [name]))("%s", (name) => {
    const entry = file.negatives.find((negative) => negative.name === name)!;
    const envelope =
      entry.envelope_hex === undefined
        ? zeroFilled(hex(entry.prefix_hex!), entry.total_length!)
        : hex(entry.envelope_hex);
    const run = () =>
      openSealedEntry(envelope, {
        did: entry.did,
        key: entry.key,
        keyring: [hex(entry.keyring_secret_hex)],
      });
    expect(run).toThrow(SealedEnvelopeError);
    expect(run).toThrow(fail(entry.reason));
    const error = caught(run);
    expect(error instanceof SealedEnvelopeError && error.reason).toBe(entry.reason);
  });

  it("seal refuses a recipient of 31 or 33 bytes", () => {
    for (const length of [31, 33]) {
      const run = () => sealEntry(input(file.v1, new Uint8Array(length).fill(9)));
      expect(run).toThrow(SealedEnvelopeError);
      expect(run).toThrow(fail("public_key"));
    }
  });

  it("seal refuses a non-agent DID", () => {
    const run = () => sealEntry({ ...input(file.v1), did: "did:web:example.com" });
    expect(run).toThrow(TypeError);
    expect(run).toThrow("AgentLand agent DID required");
  });

  it("seal refuses a key outside sealed/", () => {
    for (const key of ["vault/x", "sealed/"]) {
      const run = () => sealEntry({ ...input(file.v1), key });
      expect(run).toThrow(TypeError);
      expect(run).toThrow("Sealed vault key required");
    }
  });

  it("seal refuses meta without exactly content_type, name and tags", () => {
    const metas: unknown[] = [
      { ...file.v1.meta, size: 59 },
      { ...file.v1.meta, name: 7 },
      { ...file.v1.meta, tags: "macro" },
      { ...file.v1.meta, tags: ["macro", 1] },
    ];
    for (const meta of metas) {
      const run = () => sealEntry({ ...input(file.v1), meta: meta as SealedMeta });
      expect(run).toThrow(TypeError);
      expect(run).toThrow("Sealed meta requires content_type, name and tags");
    }
  });

  it("seal refuses an inner of 63,745 bytes", () => {
    const max = file.padding.max;
    const metaLength = utf8(JSON.stringify({ ...max.meta, size: max.body_length + 1 })).length;
    const body = maxBody(SEALED_MAX_INNER + 1 - 4 - metaLength);
    expect(4 + metaLength + body.length).toBe(63_745);
    const run = () =>
      sealEntryWithRandomness({ ...input(file.v1), meta: max.meta, body }, randomness(file.v1));
    expect(run).toThrow(SealedEnvelopeError);
    expect(run).toThrow(fail("length"));
  });

  it("open refuses a keyring entry of 31 bytes", () => {
    const run = () =>
      openSealedEntry(v1Envelope(), {
        did: file.v1.did,
        key: file.v1.key,
        keyring: [new Uint8Array(31).fill(1)],
      });
    expect(run).toThrow(SealedEnvelopeError);
    expect(run).toThrow(fail("public_key"));
  });
});

describe("low-order", () => {
  it("assertEncryptionPublicKey refuses all 14 encodings", () => {
    const inputs = lowOrderInputs();
    expect(new Set(inputs.map(toHex)).size).toBe(14);
    for (const u of inputs) {
      const run = () => assertEncryptionPublicKey(u);
      expect(run, toHex(u)).toThrow(SealedEnvelopeError);
      expect(run, toHex(u)).toThrow(fail("low_order"));
    }
  });

  it("sealEntry refuses each as recipient", () => {
    for (const u of lowOrderInputs()) {
      const run = () => sealEntry(input(file.v1, u));
      expect(run, toHex(u)).toThrow(SealedEnvelopeError);
      expect(run, toHex(u)).toThrow(fail("low_order"));
    }
  });

  it("openSealedEntry refuses each as E_pub", () => {
    for (const u of lowOrderInputs()) {
      const envelope = v1Envelope();
      envelope.set(u, 36);
      // The key id still matches, so the low-order check is reached.
      expect(sealedEnvelopeRecipient(envelope)).toBe(ANCHORS.rid);
      const run = () => v1Open(envelope);
      expect(run, toHex(u)).toThrow(SealedEnvelopeError);
      expect(run, toHex(u)).toThrow(fail("low_order"));
    }
  });

  it("positive control: V1's recipient key passes", () => {
    expect(() => assertEncryptionPublicKey(hex(file.v1.recipient_public_hex))).not.toThrow();
  });
});

describe("aad", () => {
  it("V1 opens under its own DID and key", () => {
    expect(v1Open(v1Envelope())).toStrictEqual(opened(file.v1));
  });

  it("another DID, the key suffixed x and a flipped byte 200 fail authentication", () => {
    const flipped = v1Envelope();
    flipped[200] = flipped[200]! ^ 1;
    const runs = [
      () => v1Open(v1Envelope(), OTHER_DID),
      () => v1Open(v1Envelope(), file.v1.did, `${file.v1.key}x`),
      () => v1Open(flipped),
    ];
    for (const run of runs) {
      expect(run).toThrow(SealedEnvelopeError);
      expect(run).toThrow(fail("authentication"));
    }
  });
});

describe("padding", () => {
  it("sealedInnerLength rounds 4 + n up to 256-byte blocks", () => {
    const cases: [number, number][] = [
      [0, 256],
      [252, 256],
      [253, 512],
      [256, 512],
      [63_740, 63_744],
    ];
    expect(file.padding.inner_length).toStrictEqual(cases);
    for (const [n, length] of cases) expect(sealedInnerLength(n), String(n)).toBe(length);
  });

  it("sealedEnvelopeRecipient enforces the length rule", () => {
    const head = v1Envelope().subarray(0, 36);
    for (const length of [363, 365, 64_108]) {
      const run = () => sealedEnvelopeRecipient(zeroFilled(head, length));
      expect(run, String(length)).toThrow(SealedEnvelopeError);
      expect(run, String(length)).toThrow(fail("length"));
    }
    for (const length of [364, 620, 63_852])
      expect(sealedEnvelopeRecipient(zeroFilled(head, length)), String(length)).toBe(ANCHORS.rid);
    const wrong = zeroFilled(head, 364);
    wrong[3] = 0x02;
    const run = () => sealedEnvelopeRecipient(wrong);
    expect(run).toThrow(SealedEnvelopeError);
    expect(run).toThrow(fail("magic"));
  });

  it("largest envelope", () => {
    const max = file.padding.max;
    expect(max.envelope_length).toBe(63_852);
    const seal = (length: number) =>
      sealEntryWithRandomness(
        { ...input(file.v1), meta: max.meta, body: maxBody(length) },
        randomness(file.v1),
      );
    const envelope = seal(max.body_length);
    expect(envelope.length).toBe(63_852);
    expect(sha256Hex(envelope)).toBe(max.envelope_sha256);
    expect(v1Open(envelope).body).toStrictEqual(maxBody(max.body_length));
    const run = () => seal(max.body_length + 1);
    expect(run).toThrow(SealedEnvelopeError);
    expect(run).toThrow(fail("length"));
  });
});

describe("portable", () => {
  it("sealed.ts reaches only json.ts and @noble, with no node:, Buffer, Math.random or Date", () => {
    const visited = new Set<string>();
    const pending = [new URL("../src/sealed.ts", import.meta.url)];
    while (pending.length > 0) {
      const source = pending.pop()!;
      if (visited.has(source.pathname)) continue;
      visited.add(source.pathname);
      const text = readFileSync(source, "utf8");
      expect(text, source.pathname).not.toMatch(/\bfrom\s*["']node:|\bimport\s*\(\s*["']node:/);
      expect(text, source.pathname).not.toMatch(/\bBuffer\b/);
      expect(text, source.pathname).not.toMatch(/\bMath\.random\b/);
      // No clock in the new module; json.ts's assertTimestamp parse is shared and not a clock read.
      if (source.pathname.endsWith("/sealed.ts"))
        expect(text, source.pathname).not.toMatch(/\bDate\b/);
      // Static, side-effect and dynamic imports; type-only ones are erased at build.
      const specifiers = [
        ...text.matchAll(
          /^\s*(?:import|export)(\s+type\b)?[\w$*{},\s]*?\bfrom\s*["']([^"']+)["']|^\s*import\s*["']([^"']+)["']|\bimport\s*\(\s*["']([^"']+)["']/gm,
        ),
      ].flatMap((match) => (match[1] === undefined ? [match[2] ?? match[3] ?? match[4]!] : []));
      for (const specifier of specifiers) {
        expect(specifier, `${source.pathname} imports ${specifier}`).toMatch(
          /^(?:\.\.?\/|@noble\/)/,
        );
        if (specifier.startsWith("."))
          pending.push(new URL(specifier.replace(/\.js$/, ".ts"), source));
      }
    }
    const names = [...visited].map((path) => path.slice(path.lastIndexOf("/") + 1));
    expect([...names].sort()).toStrictEqual(["json.ts", "sealed.ts"]);
  });
});

describe("spec", () => {
  const specFile = new URL("../spec/agentland-sealed-1.md", import.meta.url);
  const STATUS =
    "Status: announced, not in effect. AgentLand will publish the date this takes effect on /transparency.";
  const HEADINGS = [
    "Envelope",
    "Key derivation",
    "Associated data",
    "Inner plaintext and padding",
    "Opening",
    "Encryption-key statements (agentland-enc-key/1)",
    "Choosing a recipient",
    "Rotation",
    "Lost keys",
    "What AgentLand can still see",
    "Vectors",
    "License",
  ] as const;

  it("title first, then the status paragraph", () => {
    const lines = readFileSync(specFile, "utf8").split("\n");
    expect(lines[0]).toBe("# agentland-sealed/1");
    expect(lines.slice(1).find((line) => line.trim() !== "")).toBe(STATUS);
  });

  it("has the ## headings in order", () => {
    const lines = readFileSync(specFile, "utf8").split("\n");
    const positions = HEADINGS.map((heading) => lines.indexOf(`## ${heading}`));
    for (const [i, position] of positions.entries())
      expect(position, HEADINGS[i]).toBeGreaterThan(0);
    expect(positions).toStrictEqual([...positions].sort((a, b) => a - b));
  });

  it("states every constant, the lost-key sentence, V1 and the vector file", () => {
    const text = readFileSync(specFile, "utf8");
    for (const needle of [
      "41 4c 53 01",
      "108",
      "256",
      "364",
      "63,852",
      "63,744",
      "application/vnd.agentland.sealed",
      "agentland-enc-key/1",
      "AgentLand cannot read this. If the key is lost, these entries are gone.",
      ANCHORS.contentHash,
      "packages/identity/test/sealed-vectors.json",
    ])
      expect(text, needle).toContain(needle);
  });

  it("ends with an MIT ## License section", () => {
    const text = readFileSync(specFile, "utf8");
    const license = text.indexOf("\n## License\n");
    expect(license).toBeGreaterThan(0);
    const tail = text.slice(license + "\n## License\n".length);
    expect(tail).toContain("MIT License");
    expect(tail).toContain("Permission is hereby granted, free of charge");
    expect(tail).not.toMatch(/^#{1,2} /m);
  });

  it("never mentions escrow and uses no tables", () => {
    const text = readFileSync(specFile, "utf8");
    expect(text.toLowerCase()).not.toContain("escrow");
    expect(text).not.toMatch(/^\| /m);
  });
});
