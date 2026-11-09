import { createPrivateKey } from "node:crypto";
import { describe, expect, it } from "vitest";
import {
  agentDid,
  buildDidDocument,
  buildDidHistory,
  canonicalBytes,
  canonicalize,
  parseIJson,
  sha256Hex,
  signEd25519,
  verifyEd25519,
} from "../src/index.js";
import type { JsonValue, PublicKeyRecord, RotationRecord } from "../src/index.js";
import vectors from "./standards-vectors.json" with { type: "json" };
import { did, testKey, timestamp } from "./helpers.js";

const { publicKeyJwk, privatePkcs8 } = testKey();
const newer = testKey(1);
const record: PublicKeyRecord = {
  id: `${did}#sign-1`,
  publicKeyJwk,
  purpose: "signing",
  activated_at: timestamp,
};

describe("strict RFC8785 / I-JSON", () => {
  it("matches published IEEE754 literals and UTF16 order", () => {
    for (const [hex, expected] of vectors.jcsNumbers) {
      expect(canonicalize(Buffer.from(hex!, "hex").readDoubleBE())).toBe(expected);
    }
    expect(
      canonicalize({
        "€": "Euro",
        "\r": "Return",
        דּ: "Dalet",
        "1": "One",
        "😀": "Emoji",
        "\u0080": "Control",
        ö: "O",
      }),
    ).toBe(
      '{"\\r":"Return","1":"One","\u0080":"Control","ö":"O","€":"Euro","😀":"Emoji","דּ":"Dalet"}',
    );
    expect(canonicalize({ "2": 2, "10": 10, a: [{ z: true, a: null }, false] })).toBe(
      '{"10":10,"2":2,"a":[{"a":null,"z":true},false]}',
    );
    expect(
      canonicalize({
        string: '€$\u000f\nA\'B"\\\\"/',
        numbers: [Number("333333333.33333329"), 1e30, 4.5, 0.002, 1e-27],
        literals: [null, true, false],
      }),
    ).toBe(
      String.raw`{"literals":[null,true,false],"numbers":[333333333.3333333,1e+30,4.5,0.002,1e-27],"string":"€$\u000f\nA'B\"\\\\\"/"}`,
    );
    expect(Buffer.from(canonicalBytes("é")).toString("hex")).toBe("22c3a922");
    expect(canonicalize("e\u0301")).not.toBe(canonicalize("é"));
    expect(sha256Hex(new Uint8Array())).toBe(vectors.merkle.empty);
  });
  it("rejects I-JSON noncharacters in literal and escaped names and values", () => {
    const invalid = [
      "\ufdd0",
      "\ufdef",
      "\ufffe",
      "\uffff",
      ...Array.from({ length: 16 }, (_, index) => [
        String.fromCodePoint((index + 2) * 0x10000 - 2),
        String.fromCodePoint((index + 2) * 0x10000 - 1),
      ]).flat(),
    ];
    for (const character of invalid) {
      expect(() => canonicalize(character)).toThrow(TypeError);
      expect(() => canonicalize({ [character]: "value" })).toThrow(TypeError);
      expect(() => parseIJson(JSON.stringify({ key: character }))).toThrow(TypeError);
      expect(() => parseIJson(JSON.stringify({ [character]: "value" }))).toThrow(TypeError);
    }
    for (const text of [
      String.raw`{"key":"\ufdd0"}`,
      String.raw`{"\uffff":"value"}`,
      String.raw`{"key":"\ud83f\udffe"}`,
      String.raw`{"\udbff\udfff":"value"}`,
    ])
      expect(() => parseIJson(text)).toThrow(TypeError);
    for (const character of ["\ufdcf", "\ufdf0", "\u{1fffd}", "\u{10fffd}"]) {
      expect(parseIJson(JSON.stringify({ key: character }))).toEqual({ key: character });
      expect(canonicalize(character)).toBe(JSON.stringify(character));
    }
  });
  it("rejects non-JSON values, accessors, cycles and lone surrogates", () => {
    const cyclic: Record<string, unknown> = {};
    cyclic.self = cyclic;
    const sparse = Array(1);
    const hidden = Object.defineProperty({}, "x", { value: 1 });
    for (const value of [
      undefined,
      NaN,
      Infinity,
      -Infinity,
      1n,
      () => 1,
      Symbol(),
      new Date(timestamp),
      /x/,
      new Uint8Array(),
      cyclic,
      sparse,
      { a: undefined },
      "\ud800",
      "\udfff",
      { "\ud800": 1 },
      {
        get x() {
          throw new Error("must not execute");
        },
      },
      hidden,
      { [Symbol()]: 1 },
    ]) {
      expect(() => canonicalize(value as JsonValue)).toThrow(TypeError);
    }
    expect(canonicalize(Object.assign(Object.create(null) as object, { z: 1 }))).toBe('{"z":1}');
  });
  it("rejects duplicate raw members before parsing loses them", () => {
    for (const text of [
      '{"a":1,"a":2}',
      '{"a":1,"\\u0061":2}',
      '{"a":[{"b":1,"b":2}]}',
      '{"a":}',
      "[1,]",
      "{a:1}",
      "01",
      "true false",
      '"\\ud800"',
      "1e400",
      '{"a":1,}',
      '"unterminated',
      '"bad\\x"',
      "",
    ]) {
      expect(() => parseIJson(text)).toThrow(TypeError);
    }
    expect(
      parseIJson(String.raw` {"a":[true,false,null,-1.5e+2,{},[]],"s":"\u0061\"\\"} `),
    ).toEqual({
      a: [true, false, null, -150, {}, []],
      s: 'a"\\',
    });
    expect(Object.hasOwn(parseIJson('{"__proto__":1}') as object, "__proto__")).toBe(true);
  });
});

describe("native Ed25519", () => {
  it("matches RFC8032 tests1–3 and RFC8037 signing input", () => {
    for (let index = 0; index < 3; index++) {
      const key = testKey(index);
      const message = Buffer.from(key.vector.message, "hex");
      const expected = Buffer.from(key.vector.signature, "hex").toString("base64url");
      expect(signEd25519(message, key.privatePkcs8)).toBe(expected);
      expect(verifyEd25519(message, expected, key.publicKeyJwk)).toBe(true);
      expect(
        verifyEd25519(Buffer.concat([message, Buffer.of(1)]), expected, key.publicKeyJwk),
      ).toBe(false);
    }
    expect(signEd25519(Buffer.from(vectors.jws.input), privatePkcs8)).toBe(vectors.jws.signature);
    expect(verifyEd25519(Buffer.from(vectors.jws.input), vectors.jws.signature, publicKeyJwk)).toBe(
      true,
    );
    expect(
      verifyEd25519(Buffer.from(vectors.jws.input), vectors.jws.signature, newer.publicKeyJwk),
    ).toBe(false);
    expect(sha256Hex(canonicalBytes(publicKeyJwk))).toBe(
      "90facafea9b1556698540f70c0117a22ea37bd5cf3ed3c47093c1707282b4b89",
    );
  });
  it("rejects wrong key types, private public inputs and malformed bytes", () => {
    const message = Buffer.from("challenge");
    const signature = signEd25519(message, privatePkcs8);
    for (const key of [
      { ...publicKeyJwk, d: "secret" },
      { ...publicKeyJwk, kty: "EC" },
      { ...publicKeyJwk, crv: "X25519" },
      { ...publicKeyJwk, x: `${publicKeyJwk.x}=` },
      { ...publicKeyJwk, x: "A" },
      { ...publicKeyJwk, x: "_".repeat(43) },
      null,
    ]) {
      expect(verifyEd25519(message, signature, key as typeof publicKeyJwk)).toBe(false);
    }
    for (const sig of ["", `${signature}=`, "A", "_".repeat(86), signature.slice(1)])
      expect(verifyEd25519(message, sig, publicKeyJwk)).toBe(false);
    expect(() => signEd25519(message, Buffer.of(0))).toThrow(TypeError);
    const xPrivate = createPrivateKey({
      format: "jwk",
      key: {
        kty: "OKP",
        crv: "X25519",
        x: "3p7bfXt9wbTTW2HC7OQ1Nz-DQ8hbeGdNrfx-FG-IK08",
        d: Buffer.from(vectors.ed25519[0]!.seed, "hex").toString("base64url"),
      },
    }).export({ format: "der", type: "pkcs8" });
    expect(() => signEd25519(message, xPrivate)).toThrow(TypeError);
    expect(() => signEd25519("not bytes" as unknown as Uint8Array, privatePkcs8)).toThrow(
      TypeError,
    );
  });
});

describe("public DID profile and retained history", () => {
  it("separates signing and encryption and emits exact URLs", () => {
    const encryption: PublicKeyRecord = {
      ...record,
      id: `${did}#enc-1`,
      purpose: "encryption",
      publicKeyJwk: { kty: "OKP", crv: "X25519", x: "3p7bfXt9wbTTW2HC7OQ1Nz-DQ8hbeGdNrfx-FG-IK08" },
    };
    const revoked: PublicKeyRecord = {
      ...record,
      id: `${did}#old`,
      revoked_at: "2026-01-02T00:00:00.000Z",
    };
    const doc = buildDidDocument({ handle: "weatherwise", keys: [record, revoked, encryption] });
    expect(agentDid("weatherwise")).toBe(did);
    expect(doc.id).toBe(did);
    expect(doc.alsoKnownAs).toEqual(["https://agentland.us/agents/weatherwise/did.json"]);
    expect(doc.authentication).toEqual([record.id]);
    expect(doc.assertionMethod).toEqual([record.id]);
    expect(doc.keyAgreement).toEqual([encryption.id]);
    expect(doc.verificationMethod.map((key) => key.id)).toEqual([encryption.id, record.id]);
    expect(doc.service).toEqual([
      {
        id: `${did}#trust`,
        type: "AgentLandTrust",
        serviceEndpoint: "https://agentland.us/v1/agents/weatherwise/trust",
      },
    ]);
    const history = buildDidHistory({
      handle: "weatherwise",
      keys: [record, revoked],
      rotations: [],
    });
    expect(history.keys.map((key) => key.id)).toEqual([revoked.id, record.id]);
    expect(history.keys[0]!.revoked_at).toBe(revoked.revoked_at);
  });
  it("retains verifiable dual and old-only signed rotation statements", () => {
    const statement = {
      old_pub: publicKeyJwk,
      new_pub: newer.publicKeyJwk,
      reason: "scheduled",
      timestamp: "2026-01-02T00:00:00.000Z",
    };
    const oldSignature = signEd25519(canonicalBytes(statement), privatePkcs8);
    const newSignature = signEd25519(canonicalBytes(statement), newer.privatePkcs8);
    const nextRecord: PublicKeyRecord = {
      ...record,
      id: `${did}#sign-2`,
      activated_at: statement.timestamp,
      publicKeyJwk: newer.publicKeyJwk,
    };
    const rotations: RotationRecord[] = [
      { statement, sig_old: oldSignature, sig_new: newSignature },
      {
        statement: { ...statement, reason: "compromised" },
        sig_old: signEd25519(canonicalBytes({ ...statement, reason: "compromised" }), privatePkcs8),
      },
    ];
    const history = buildDidHistory({
      handle: "weatherwise",
      keys: [nextRecord, { ...record, revoked_at: statement.timestamp }],
      rotations,
    });
    expect(history.rotations.map((rotation) => rotation.signatures)).toEqual(["old-only", "dual"]);
    expect(history.rotations[1]!.statement).toEqual(statement);
    for (const rotation of [
      { ...rotations[0]!, sig_old: newSignature },
      { ...rotations[0]!, sig_new: oldSignature },
      { ...rotations[0]!, statement: { ...statement, reason: "altered" } },
    ]) {
      expect(() =>
        buildDidHistory({
          handle: "weatherwise",
          keys: [record, nextRecord],
          rotations: [rotation],
        }),
      ).toThrow(TypeError);
    }
  });
  it("rejects noncanonical handles, private records and invalid ordering", () => {
    for (const handle of ["ab", "Aaa", "@aaa", "a_aa", "a".repeat(25)])
      expect(() => agentDid(handle)).toThrow(TypeError);
    const invalid = [
      [],
      [record, record],
      [{ ...record, id: "#relative" }],
      [{ ...record, id: "did:web:evil.test#key" }],
      [{ ...record, publicKeyJwk: { ...publicKeyJwk, d: "secret" } }],
      [{ ...record, purpose: "encryption" }],
      [{ ...record, activated_at: "2026-02-30T00:00:00.000Z" }],
      [{ ...record, revoked_at: "2025-01-01T00:00:00.000Z" }],
      [{ ...record, privateKey: "secret" }],
    ];
    for (const keys of invalid)
      expect(() =>
        buildDidDocument({ handle: "weatherwise", keys: keys as PublicKeyRecord[] }),
      ).toThrow(TypeError);
  });
});
