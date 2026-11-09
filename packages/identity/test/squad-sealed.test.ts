import { xchacha20poly1305 } from "@noble/ciphers/chacha.js";
import type * as Chacha from "@noble/ciphers/chacha.js";
import { describe, expect, it, vi } from "vitest";

// Pass-through spy: records the AEAD key of every decrypt and counts encrypts, so opening is
// proved to be one attempt with the selected key (never trial decryption) and a refused
// recipient is proved to be refused before any wrap is encrypted. Behavior is unchanged.
const decryptKeys: string[] = vi.hoisted(() => []);
const encrypts: { n: number } = vi.hoisted(() => ({ n: 0 }));
vi.mock("@noble/ciphers/chacha.js", async (importOriginal) => {
  const actual = await importOriginal<typeof Chacha>();
  return {
    ...actual,
    xchacha20poly1305: (key: Uint8Array, nonce: Uint8Array, aad?: Uint8Array) => {
      const cipher = actual.xchacha20poly1305(key, nonce, aad);
      return {
        ...cipher,
        encrypt: (plaintext: Uint8Array) => {
          encrypts.n += 1;
          return cipher.encrypt(plaintext);
        },
        decrypt: (ciphertext: Uint8Array) => {
          decryptKeys.push(Buffer.from(key).toString("hex"));
          return cipher.decrypt(ciphertext);
        },
      };
    },
  };
});
import {
  EncKeyRecipientError,
  SEALED_MAX_INNER,
  SQUAD_SEALED_CONTENT_TYPE,
  SQUAD_SEALED_FORMAT,
  SQUAD_SEALED_MAGIC,
  SealedEnvelopeError,
  SquadSealedError,
  canonicalBytes,
  checkSquadSealedEntries,
  encKeyStatementBytes,
  encryptionPublicKey,
  openEpochWrap,
  openSealedEntry,
  openSquadEntry,
  parseSquadSealedHeader,
  recipientKeyId,
  sealSquadEntry,
  sealedEnvelopeRecipient,
  signEd25519,
  squadSealedAad,
  verifySquadEpochRecipients,
  wrapEpochKey,
} from "../src/index.js";
import type {
  EncKeyHistory,
  EncKeyStatement,
  RotationRecord,
  RotationStatement,
  SquadEpochWrap,
  SquadSealedInput,
  SquadStatementPayload,
} from "../src/index.js";
import { sealEntryWithRandomness } from "../src/sealed.js";
import { sealSquadEntryWithRandomness } from "../src/squad-sealed.js";
import {
  base,
  bytes,
  decode,
  encOf,
  epochKeyOf,
  fail,
  file,
  filled,
  fromB64url,
  hexOf,
  hist,
  pkcs8,
  platformKeys,
  recipient,
  replayOf,
  scenario,
  sealedFail,
  sealedVectors,
  sha256,
  statementsOf,
  throwsWith,
  toB64url,
  utf8,
  xOf,
} from "./fixtures/squad-sealed.js";
import {
  ANCHORS,
  E,
  EPOCH_KEY_TYPE,
  MARKER,
  NAMES,
  OTHER_SQUAD,
  ROTATED,
  W,
  WRAP_KEY,
  anchor,
  entryInput,
  metaBytes,
  openAnchor,
  openWrap,
  shaped,
  wrapAnchor,
  wrapInput,
} from "./fixtures/squad-sealed-inputs.js";
const refuses = (run: () => unknown, reason: string): void =>
  throwsWith(run, SquadSealedError, fail(reason));

describe("envelope", () => {
  it("anchor", () => {
    expect(SQUAD_SEALED_FORMAT).toBe("agentland-squad-sealed/1");
    expect(SQUAD_SEALED_MAGIC).toBe("414c5101");
    expect(SQUAD_SEALED_CONTENT_TYPE).toBe("application/vnd.agentland.squad-sealed");
    const envelope = anchor();
    expect(envelope.length).toBe(ANCHORS.envelope_length);
    expect(sha256(envelope)).toBe(ANCHORS.envelope_sha256);
    expect(hexOf(envelope.subarray(-16))).toBe(ANCHORS.envelope_tag);
    expect(hexOf(envelope.subarray(0, 8))).toBe("414c510100000001");
    expect(hexOf(envelope.subarray(8, 32))).toBe(E.nonce_hex);
  });

  it("opens", () => {
    decryptKeys.length = 0;
    expect(openAnchor(anchor())).toStrictEqual({
      epoch: "1",
      meta: { content_type: E.meta.content_type, name: "notes", size: 5, tags: [] },
      body: utf8("hello"),
    });
    // One AEAD attempt, under the epoch key named by the header.
    expect(decryptKeys).toStrictEqual([E.epoch_key_hex]);
  });

  it("fresh nonce", () => {
    const a = sealSquadEntry(entryInput());
    const b = sealSquadEntry(entryInput());
    expect(hexOf(a.subarray(8, 32))).not.toBe(hexOf(b.subarray(8, 32)));
    for (const envelope of [a, b]) expect(openAnchor(envelope).body).toStrictEqual(utf8("hello"));
  });

  it("header", () => {
    const envelope = anchor();
    expect(parseSquadSealedHeader(envelope)).toStrictEqual({ epoch: "1" });
    const flipped = envelope.slice();
    flipped[flipped.length - 1] = flipped[flipped.length - 1]! ^ 1;
    decryptKeys.length = 0;
    // Shape only: a bad tag still parses, and nothing is decrypted.
    expect(parseSquadSealedHeader(flipped)).toStrictEqual({ epoch: "1" });
    expect(decryptKeys).toStrictEqual([]);
  });

  it("hostile input: a Proxy header is refused, getters are read once", () => {
    // The buffer's magic is invalid; the Proxy shows 0x41 at index 0 through indexed reads.
    const target = shaped(304);
    target[0] = 0x00;
    const proxy = new Proxy(target, {
      get: (t, p) => (p === "0" ? 0x41 : (Reflect.get(t, p) as unknown)),
    });
    throwsWith(() => parseSquadSealedHeader(proxy), TypeError, "Uint8Array required");
    throwsWith(() => openAnchor(proxy), TypeError, "Squad sealed input required");
    // epochKey and epoch change after their first read: the envelope uses the first values.
    const reads = { key: 0, epoch: 0 };
    const changing = { ...entryInput() } as Record<string, unknown>;
    Object.defineProperty(changing, "epochKey", {
      enumerable: true,
      get: () => (reads.key++ === 0 ? bytes(E.epoch_key_hex) : new Uint8Array(32).fill(7)),
    });
    Object.defineProperty(changing, "epoch", {
      enumerable: true,
      get: () => (reads.epoch++ === 0 ? "1" : "2"),
    });
    const sealed = sealSquadEntryWithRandomness(changing as unknown as SquadSealedInput, {
      nonce: bytes(E.nonce_hex),
    });
    expect(hexOf(sealed)).toBe(hexOf(anchor()));
    expect([reads.key, reads.epoch]).toStrictEqual([1, 1]);
  });

  it("hostile input: shared memory is copied once and used consistently", () => {
    if (typeof SharedArrayBuffer === "undefined") return;
    const shared = new Uint8Array(new SharedArrayBuffer(5));
    shared.set(utf8("hello"));
    const input = { ...entryInput({ body: shared }) } as Record<string, unknown>;
    // A later member's getter rewrites the shared body during the clone.
    Object.defineProperty(input, "zz", {
      enumerable: true,
      get: () => {
        shared.set(utf8("HELLO"));
        return 0;
      },
    });
    const sealed = sealSquadEntryWithRandomness(input as unknown as SquadSealedInput, {
      nonce: bytes(E.nonce_hex),
    });
    shared.set(utf8("xxxxx"));
    const opened = openAnchor(sealed);
    expect(opened.body).toStrictEqual(utf8("HELLO"));
    expect(opened.meta.size).toBe(5);
  });

  it("length rule", () => {
    for (const length of [303, 305, 559, 64_048])
      throwsWith(() => parseSquadSealedHeader(shaped(length)), SquadSealedError, fail("length"));
    for (const length of [304, 560, 63_792])
      expect(parseSquadSealedHeader(shaped(length))).toStrictEqual({ epoch: "1" });
    const version = shaped(304);
    version[3] = 0x02;
    throwsWith(() => parseSquadSealedHeader(version), SquadSealedError, fail("magic"));
    const magic = shaped(304);
    magic[0] = 0x00;
    throwsWith(() => parseSquadSealedHeader(magic), SquadSealedError, fail("magic"));
    throwsWith(() => parseSquadSealedHeader(shaped(304, 0)), SquadSealedError, fail("epoch"));
    throwsWith(
      () => parseSquadSealedHeader([0x41] as unknown as Uint8Array),
      TypeError,
      "Uint8Array required",
    );
  });

  it("largest", () => {
    const length = SEALED_MAX_INNER - 4 - metaBytes(10_000).length;
    const largest = sealSquadEntry(entryInput({ body: new Uint8Array(length) }));
    expect(largest.length).toBe(63_792);
    expect(parseSquadSealedHeader(largest)).toStrictEqual({ epoch: "1" });
    throwsWith(
      () => sealSquadEntry(entryInput({ body: new Uint8Array(length + 1) })),
      SquadSealedError,
      fail("length"),
    );
  });

  it("refusals", () => {
    const short = new Uint8Array(31).fill(0x42);
    refuses(() => sealSquadEntry(entryInput({ epochKey: short })), "epoch_key");
    refuses(() => openAnchor(anchor(), { epochKey: short }), "epoch_key");
    throwsWith(
      () => sealSquadEntryWithRandomness(entryInput(), { nonce: new Uint8Array(23) }),
      TypeError,
      "24-byte nonce required",
    );
    const flipped = anchor();
    flipped[flipped.length - 1] = flipped[flipped.length - 1]! ^ 1;
    throwsWith(() => openAnchor(flipped), SquadSealedError, fail("authentication"));
    // A well-formed inner except one nonzero padding byte, under the anchor's key, nonce and AAD.
    const meta = metaBytes(5);
    const inner = new Uint8Array(256);
    new DataView(inner.buffer).setUint32(0, meta.length);
    inner.set(meta, 4);
    inner.set(utf8("hello"), 4 + meta.length);
    inner[255] = 1;
    const aad = squadSealedAad({ squadId: E.squad_id, key: E.key, epoch: "1" });
    const aead = xchacha20poly1305(bytes(E.epoch_key_hex), bytes(E.nonce_hex), aad);
    const ciphertext = aead.encrypt(inner);
    const padded = new Uint8Array(32 + ciphertext.length);
    padded.set(anchor().subarray(0, 32));
    padded.set(ciphertext, 32);
    throwsWith(() => openAnchor(padded), SquadSealedError, fail("padding"));
    // Distinct magics: neither format opens as the other.
    throwsWith(
      () => openSealedEntry(anchor(), { did: W.did, key: E.key, keyring: [] }),
      SealedEnvelopeError,
      sealedFail("magic"),
    );
    throwsWith(
      () => parseSquadSealedHeader(bytes(sealedVectors.v1.envelope_hex)),
      SquadSealedError,
      fail("magic"),
    );
  });
});

describe("aad", () => {
  it("bytes", () => {
    const aad = squadSealedAad({ squadId: E.squad_id, key: "sealed/notes", epoch: "1" });
    expect(new TextDecoder().decode(aad)).toBe(
      '{"epoch":"1","format":"agentland-squad-sealed/1","key":"sealed/notes","squad_id":"01900000-0000-7000-8000-000000000001"}',
    );
  });

  it("epoch 2 refused", () => {
    const moved = anchor();
    new DataView(moved.buffer, moved.byteOffset).setUint32(4, 2);
    expect(hexOf(moved.subarray(4, 8))).toBe("00000002");
    throwsWith(() => openAnchor(moved), SquadSealedError, fail("authentication"));
  });

  it("squad and key bound", () => {
    refuses(() => openAnchor(anchor(), { squadId: OTHER_SQUAD }), "authentication");
    refuses(() => openAnchor(anchor(), { key: "sealed/notesx" }), "authentication");
  });

  it("inputs", () => {
    const aad = (overrides: Partial<{ squadId: string; key: string; epoch: string }>) => () =>
      squadSealedAad({ squadId: E.squad_id, key: E.key, epoch: "1", ...overrides });
    const squadId = "01900000-0000-7000-8000-00000000000a".toUpperCase();
    expect(squadId).not.toBe(squadId.toLowerCase());
    throwsWith(aad({ squadId }), TypeError, "Lowercase UUIDv7 squad id required");
    for (const key of ["vault/notes", "sealed/"])
      throwsWith(aad({ key }), TypeError, "Sealed vault key required");
    for (const epoch of ["0", "01"])
      throwsWith(aad({ epoch }), TypeError, "Canonical decimal sequence required");
    throwsWith(aad({ epoch: "4294967296" }), RangeError, "Squad epoch exceeds u32");
  });
});

describe("wrap", () => {
  it("W1 anchor", () => {
    const wrap = wrapAnchor();
    expect(wrap.kid).toBe(ANCHORS.wrap_kid);
    const envelope = fromB64url(wrap.envelope);
    expect(envelope.length).toBe(ANCHORS.wrap_length);
    expect(sha256(envelope)).toBe(ANCHORS.wrap_sha256);
    expect(sealedEnvelopeRecipient(envelope)).toBe(wrap.kid);
    decryptKeys.length = 0;
    // The first keyring entry does not match: selection by kid, one attempt, the HKDF key.
    const keyring = [bytes(W.ephemeral_secret_hex), bytes(W.recipient_secret_hex)];
    expect(openWrap(wrap.envelope, { keyring })).toStrictEqual(bytes(W.epoch_key_hex));
    expect(decryptKeys).toStrictEqual([ANCHORS.wrap_hkdf_key]);
  });

  it("W2 fresh randomness", () => {
    const a = wrapEpochKey(wrapInput());
    const b = wrapEpochKey(wrapInput());
    expect(a.kid).toBe(b.kid);
    expect(a.envelope).not.toBe(b.envelope);
    for (const wrap of [a, b])
      expect(openWrap(wrap.envelope)).toStrictEqual(bytes(W.epoch_key_hex));
  });

  it("W3 bound", () => {
    const { envelope } = wrapAnchor();
    for (const overrides of [
      { did: "did:web:agentland.us:agents:member-three" },
      { epoch: "2" },
      { squadId: OTHER_SQUAD },
    ])
      throwsWith(
        () => openWrap(envelope, overrides),
        SealedEnvelopeError,
        sealedFail("authentication"),
      );
    throwsWith(
      () => openWrap(envelope, { keyring: [bytes(W.ephemeral_secret_hex)] }),
      SealedEnvelopeError,
      sealedFail("recipient_unknown"),
    );
    throwsWith(
      () => wrapEpochKey(wrapInput({ recipient: bytes(sealedVectors.low_order.encodings[0]!) })),
      SealedEnvelopeError,
      sealedFail("low_order"),
    );
  });

  it("W4 only epoch keys open", () => {
    const seal = (contentType: string, body: Uint8Array): string =>
      toB64url(
        sealEntryWithRandomness(
          {
            recipient: bytes(W.recipient_public_hex),
            did: W.did,
            key: WRAP_KEY,
            meta: { content_type: contentType, name: `${W.squad_id}/epoch/1`, tags: [] },
            body,
          },
          { ephemeralSecretKey: bytes(W.ephemeral_secret_hex), nonce: bytes(W.nonce_hex) },
        ),
      );
    refuses(() => openWrap(seal("text/plain", bytes(W.epoch_key_hex))), "epoch_key");
    refuses(() => openWrap(seal(EPOCH_KEY_TYPE, new Uint8Array(31))), "epoch_key");
    throwsWith(
      () => wrapEpochKey(wrapInput({ epochKey: new Uint8Array(31) })),
      SquadSealedError,
      fail("epoch_key"),
    );
  });

  it("W5 verified recipients", () => {
    const replay = replayOf(filled(scenario("SS1-sealed")));
    const result = verifySquadEpochRecipients({
      replay,
      histories: [recipient("founder"), recipient("three")],
    });
    // verifyEncKeyRecipient's signingKey is the latest unrevoked signing key: founder's #key-1 is
    // revoked in squad-vectors.json, so founder's is #key-2 (founder-2).
    const expected = [
      { label: "founder", signingKey: xOf("founder-2") },
      { label: "three", signingKey: xOf("three") },
    ]
      .map(({ label, signingKey }) => ({
        did: hist(label).did,
        publicKey: bytes(encOf(label).public_hex!),
        kid: encOf(label).kid!,
        signingKey,
      }))
      .sort((a, b) => (a.kid < b.kid ? -1 : a.kid > b.kid ? 1 : 0));
    expect(result).toStrictEqual({ recipients: expected, fresh: true });
    expect(result.recipients.map((r) => r.kid)).toStrictEqual(replay.epochs.at(-1)!.recipients);
  });

  it("W6 platform custody refused before any wrap", () => {
    const replay = replayOf(filled(scenario("SS1-sealed")));
    const three = hist("three").value!;
    const history: EncKeyHistory = {
      ...three,
      enc_keys: [{ ...three.enc_keys[0]!, custody: "platform" }],
    };
    const wraps: SquadEpochWrap[] = [];
    encrypts.n = 0;
    throwsWith(
      () => {
        const { recipients } = verifySquadEpochRecipients({
          replay,
          histories: [recipient("founder"), recipient("three", { history })],
        });
        for (const r of recipients)
          wraps.push(
            wrapEpochKey({
              recipient: r.publicKey,
              did: r.did,
              squadId: replay.squad_id,
              epoch: "4",
              epochKey: new Uint8Array(32).fill(7),
            }),
          );
      },
      EncKeyRecipientError,
      "recipient_platform_custody",
    );
    expect(wraps).toStrictEqual([]);
    expect(encrypts.n).toBe(0);
  });

  it("W7 unverified", () => {
    const replay = replayOf(filled(scenario("SS1-sealed")));
    const three = hist("three").value!;
    const signature = three.enc_keys[0]!.signature;
    const history: EncKeyHistory = {
      ...three,
      enc_keys: [
        {
          ...three.enc_keys[0]!,
          signature: (signature[0] === "A" ? "B" : "A") + signature.slice(1),
        },
      ],
    };
    throwsWith(
      () =>
        verifySquadEpochRecipients({
          replay,
          histories: [recipient("founder"), recipient("three", { history })],
        }),
      EncKeyRecipientError,
      "recipient_unverified",
    );
  });

  it("W8 substituted key", () => {
    const replay = replayOf(filled(scenario("SS1-sealed")));
    const substituted = recipient("three", { publicKey: bytes(encOf("two").public_hex!) });
    throwsWith(
      () => verifySquadEpochRecipients({ replay, histories: [recipient("founder"), substituted] }),
      EncKeyRecipientError,
      "recipient_unverified",
    );
  });

  it("W9 pin changed", () => {
    const replay = replayOf(filled(scenario("SS1-sealed")));
    const pinned = recipient("three", { pinnedSigningKey: xOf("two") });
    throwsWith(
      () => verifySquadEpochRecipients({ replay, histories: [recipient("founder"), pinned] }),
      EncKeyRecipientError,
      "recipient_pin_broken",
    );
  });

  it("W9b a pin getter cannot show the genuine pin after a broken one", () => {
    const replay = replayOf(filled(scenario("SS1-sealed")));
    const counts: number[] = [];
    // throwsWith invokes `run` more than once: each call builds a fresh "broken first" getter.
    const run = () => {
      let reads = 0;
      counts.push(0);
      const three = { ...recipient("three") };
      Object.defineProperty(three, "pinnedSigningKey", {
        enumerable: true,
        get: () => {
          counts[counts.length - 1] = ++reads;
          return reads === 1 ? xOf("two") : xOf("three");
        },
      });
      return verifySquadEpochRecipients({ replay, histories: [recipient("founder"), three] });
    };
    throwsWith(run, EncKeyRecipientError, "recipient_pin_broken");
    expect(counts.length).toBeGreaterThan(0);
    expect(counts.some((n) => n !== 1)).toBe(false);
  });

  it("W10 genuine rotation accepted", () => {
    const replay = replayOf(filled(scenario("SS1-sealed")));
    const three = hist("three").value!;
    const did = three.did;
    const statement: RotationStatement = {
      old_pub: { kty: "OKP", crv: "Ed25519", x: xOf("three") },
      new_pub: { kty: "OKP", crv: "Ed25519", x: xOf("m04") },
      reason: "scheduled",
      timestamp: ROTATED,
    };
    const signed = canonicalBytes(statement);
    const rotation: RotationRecord = {
      statement,
      sig_old: signEd25519(signed, pkcs8("three")),
      sig_new: signEd25519(signed, pkcs8("m04")),
    };
    const register = three.enc_keys[0]!.statement;
    const history: EncKeyHistory = {
      ...three,
      keys: [
        { ...three.keys.find((k) => k.id === `${did}#key-1`)!, revoked_at: ROTATED },
        three.keys.find((k) => k.purpose === "encryption")!,
        {
          id: `${did}#key-3`,
          publicKeyJwk: { kty: "OKP", crv: "Ed25519", x: xOf("m04") },
          purpose: "signing",
          activated_at: ROTATED,
        },
      ],
      rotations: [rotation],
      enc_keys: [
        {
          statement: register,
          signature: signEd25519(encKeyStatementBytes(register), pkcs8("m04")),
          signing_key_id: `${did}#key-3`,
          custody: "self",
        },
      ],
    };
    const { recipients, fresh } = verifySquadEpochRecipients({
      replay,
      histories: [
        recipient("founder"),
        recipient("three", { history, pinnedSigningKey: xOf("three") }),
      ],
    });
    expect(fresh).toBe(true);
    expect(recipients.find((r) => r.did === did)!.signingKey).toBe(xOf("m04"));
  });

  it("W11 members", () => {
    const replay = replayOf(filled(scenario("SS1-sealed")));
    for (const histories of [
      [recipient("founder")],
      [recipient("founder"), recipient("three"), recipient("two")],
      [recipient("founder"), recipient("founder"), recipient("three")],
    ])
      refuses(() => verifySquadEpochRecipients({ replay, histories }), "members");
    const closed = replayOf(
      base.scenarios.find((s) => s.name === "S1-lifecycle")!,
      platformKeys,
    );
    expect(closed.closed).toBe(true);
    throwsWith(
      () => verifySquadEpochRecipients({ replay: closed, histories: [] }),
      SquadSealedError,
      fail("members"),
    );
  });

  it("W12 fresh is false", () => {
    const stale = replayOf(filled(scenario("SS-stale-after-leave")));
    expect(
      verifySquadEpochRecipients({ replay: stale, histories: [recipient("founder")] }).fresh,
    ).toBe(false);
    // C-6 key half: founder registers a new active encryption key after epoch 3.
    const replay = replayOf(filled(scenario("SS1-sealed")));
    const founder = hist("founder").value!;
    const did = founder.did;
    const next = encryptionPublicKey(bytes("a4".repeat(32)));
    const statement: EncKeyStatement = {
      did,
      kind: "enc_key",
      previous: `${did}#key-3`,
      public_key: toB64url(next),
      ts: "2026-10-20T00:00:00.000Z",
    };
    const history: EncKeyHistory = {
      ...founder,
      keys: [
        ...founder.keys,
        {
          id: `${did}#key-4`,
          publicKeyJwk: { kty: "OKP", crv: "X25519", x: toB64url(next) },
          purpose: "encryption",
          activated_at: statement.ts,
        },
      ],
      enc_keys: [
        ...founder.enc_keys,
        {
          statement,
          signature: signEd25519(encKeyStatementBytes(statement), pkcs8("founder")),
          signing_key_id: `${did}#key-1`,
          custody: "self",
        },
      ],
    };
    const result = verifySquadEpochRecipients({
      replay,
      histories: [recipient("founder", { history, publicKey: next }), recipient("three")],
    });
    expect(result.recipients.map((r) => r.kid)).toContain(recipientKeyId(next));
    expect(result.fresh).toBe(false);
  });
});

describe("sealed entries", () => {
  it("vector file", () => {
    expect(Object.keys(file).sort()).toStrictEqual([
      "anchors",
      "attribution",
      "enc_keys",
      "envelope",
      "histories",
      "scenarios",
      "wrap",
    ]);
    expect(file.anchors).toStrictEqual(ANCHORS);
    expect(file.scenarios.map((s) => s.name)).toStrictEqual(NAMES);
    const derived: unknown[] = [
      E.aad_utf8,
      E.envelope_hex,
      W.kid,
      W.envelope_b64url,
      W.envelope_sha256,
      ...file.enc_keys.flatMap((k) => [k.public_hex, k.kid]),
      ...file.histories.map((h) => h.value),
      ...file.scenarios.flatMap((s) => [s.entries, s.statements, s.payloads, s.head]),
    ];
    expect(derived.some((value) => value === null)).toBe(false);
    expect(E.envelope_hex).toBe(hexOf(anchor()));
    expect(E.aad_utf8).toBe(
      new TextDecoder().decode(squadSealedAad({ squadId: E.squad_id, key: E.key, epoch: E.epoch })),
    );
    const wrap = wrapAnchor();
    expect([W.kid, W.envelope_b64url, W.envelope_sha256]).toStrictEqual([
      wrap.kid,
      wrap.envelope,
      sha256(fromB64url(wrap.envelope)),
    ]);
    for (const key of file.enc_keys) {
      const publicKey = encryptionPublicKey(bytes(key.secret_hex));
      expect([key.public_hex, key.kid]).toStrictEqual([
        hexOf(publicKey),
        recipientKeyId(publicKey),
      ]);
    }
    let opened = 0;
    for (const s of file.scenarios)
      for (const { statement } of statementsOf(s)) {
        if (statement.kind !== "epoch") continue;
        for (const wrap of statement.wraps!) {
          const key = file.enc_keys.find((k) => k.kid === wrap.kid)!;
          const epochKey = openEpochWrap({
            envelope: wrap.envelope,
            did: hist(key.label).did,
            squadId: s.squad_id,
            epoch: statement.epoch!,
            keyring: [bytes(key.secret_hex)],
          });
          expect(hexOf(epochKey)).toBe(epochKeyOf(s.name, statement.epoch!));
          opened += 1;
        }
      }
    // SS1: 2 + 3 + 2; four scenarios with one two-member epoch each.
    expect(opened).toBe(15);
  });

  it.each(NAMES.map((name) => [name]))("%s", (name) => {
    const s = scenario(name);
    const replay = replayOf(filled(s));
    expect(
      checkSquadSealedEntries({ replay, entries: s.entries!, payloads: decode(s.payloads!) }),
    ).toStrictEqual(s.expected);
  });

  it("end to end", () => {
    const s = scenario("SS1-sealed");
    const statements = statementsOf(s);
    const payloads = decode(s.payloads!);
    expect(payloads.map((p) => p.seq)).toStrictEqual(["5", "9", "12"]);
    for (const { seq, content } of payloads) {
      expect(hexOf(content.subarray(0, 4))).toBe("414c5101");
      expect(Buffer.from(content).includes(MARKER)).toBe(false);
      const entry = s.entries!.find((e) => e.seq === seq)!;
      const { epoch } = parseSquadSealedHeader(content);
      const label = file.histories.find((h) => h.did === entry.signer)!.label;
      const epochStatement = statements.find(
        (st) =>
          st.statement.kind === "epoch" &&
          st.statement.epoch === epoch &&
          BigInt(st.seq) < BigInt(seq),
      )!.statement;
      const own = epochStatement.wraps!.find((w) => w.kid === encOf(label).kid)!;
      const epochKey = openEpochWrap({
        envelope: own.envelope,
        did: entry.signer,
        squadId: s.squad_id,
        epoch,
        keyring: [bytes(encOf(label).secret_hex)],
      });
      expect(hexOf(epochKey)).toBe(epochKeyOf(s.name, epoch));
      const opened = openSquadEntry({
        epochKey,
        squadId: s.squad_id,
        key: entry.key,
        envelope: content,
      });
      expect(new TextDecoder().decode(opened.body)).toContain(MARKER);
    }
  });

  it("missing and changed payloads", () => {
    const s = scenario("SS1-sealed");
    const replay = replayOf(filled(s));
    const payloads = decode(s.payloads!);
    expect(
      checkSquadSealedEntries({
        replay,
        entries: s.entries!,
        payloads: payloads.filter((p) => p.seq !== "5"),
      }),
    ).toStrictEqual({
      valid: false,
      error: { stage: "sealed", reason: "payload-missing", index: 4 },
    });
    const changed = payloads.map((p) => {
      if (p.seq !== "5") return p;
      const content = p.content.slice();
      content[40] = content[40]! ^ 1;
      return { seq: p.seq, content };
    });
    expect(
      checkSquadSealedEntries({ replay, entries: s.entries!, payloads: changed }),
    ).toStrictEqual({
      valid: false,
      error: { stage: "sealed", reason: "payload-mismatch", index: 4 },
    });
  });

  it("overridden array methods cannot hide a missing payload", () => {
    const s = scenario("SS1-sealed");
    const replay = replayOf(filled(s));
    const entries = [...s.entries!];
    const payloads = decode(s.payloads!).filter((p) => p.seq !== "5");
    for (const array of [entries, payloads] as unknown[][])
      for (const name of ["entries", "some", "filter", "map", "find", "forEach"])
        Object.defineProperty(array, name, { enumerable: false, value: () => [] });
    expect(checkSquadSealedEntries({ replay, entries, payloads })).toStrictEqual({
      valid: false,
      error: { stage: "sealed", reason: "payload-missing", index: 4 },
    });
  });

  it("schema", () => {
    const s = scenario("SS1-sealed");
    const replay = replayOf(filled(s));
    const payloads = decode(s.payloads!);
    const schema = {
      valid: false,
      error: { stage: "schema", reason: "invalid-schema-or-trust-pins" },
    };
    for (const input of [
      { replay, entries: scenario("SS-no-epoch").entries!, payloads },
      { replay, entries: s.entries!, payloads: [...payloads, payloads[0]!] },
      { replay, entries: s.entries!, payloads: "payloads" as unknown as SquadStatementPayload[] },
      // Non-canonical payload seq, and payload content that is not a Uint8Array.
      {
        replay,
        entries: s.entries!,
        payloads: [{ ...payloads[0]!, seq: "05" }, ...payloads.slice(1)],
      },
      {
        replay,
        entries: s.entries!,
        payloads: [
          { seq: payloads[0]!.seq, content: [1, 2] as unknown as Uint8Array },
          ...payloads.slice(1),
        ],
      },
    ])
      expect(checkSquadSealedEntries(input)).toStrictEqual(schema);
  });
});
