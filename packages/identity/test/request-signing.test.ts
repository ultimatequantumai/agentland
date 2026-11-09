import { describe, expect, it } from "vitest";
import { requestSigningMessage, sha256Hex, signEd25519, verifyEd25519 } from "../src/index.js";
import type { Ed25519PublicJwk } from "../src/index.js";
import standards from "./standards-vectors.json" with { type: "json" };
import file from "./request-signing-vectors.json" with { type: "json" };

interface Entry {
  name: string;
  method: string;
  request_target: string;
  timestamp: string;
  raw_body_b64: string;
  body_sha256_hex: string;
  message_utf8: string;
  private_pkcs8_b64: string;
  public_jwk: Ed25519PublicJwk;
  signature_b64: string;
  valid: boolean;
  base?: string;
  field?: string;
}
// The fixture is the frozen cross-language contract (11-04 consumes it unchanged).
const { vectors, tamper } = file as unknown as { vectors: Entry[]; tamper: Entry[] };

const PADDED_B64 = /^[A-Za-z0-9+/]{86}==$/;
const VECTOR_KEYS = [
  "body_sha256_hex",
  "message_utf8",
  "method",
  "name",
  "private_pkcs8_b64",
  "public_jwk",
  "raw_body_b64",
  "request_target",
  "signature_b64",
  "timestamp",
  "valid",
];
const TAMPER_KEYS = [...VECTOR_KEYS, "base", "field"].sort();
const PKCS8_PREFIX = "302e020100300506032b657004220420";
const seed = standards.ed25519[0]!;

const rawBody = (entry: Entry) => new Uint8Array(Buffer.from(entry.raw_body_b64, "base64"));
const message = (entry: Entry) =>
  requestSigningMessage({
    method: entry.method,
    requestTarget: entry.request_target,
    timestamp: entry.timestamp,
    rawBody: rawBody(entry),
  });
// P-18: the header is padded standard base64; verifyEd25519 takes base64url.
const verify = (bytes: Uint8Array, entry: Entry) =>
  verifyEd25519(
    bytes,
    Buffer.from(entry.signature_b64, "base64").toString("base64url"),
    entry.public_jwk,
  );
const baseOf = (entry: Entry) => vectors.find((vector) => vector.name === entry.base)!;

describe("request-signing preimage", () => {
  it("vectors file shape: frozen keys, encodings and no null left", () => {
    expect(vectors.length).toBeGreaterThanOrEqual(3);
    expect(tamper.length).toBeGreaterThanOrEqual(5);
    expect(new Set(tamper.map((entry) => entry.field))).toEqual(
      new Set(["method", "request_target", "timestamp", "raw_body", "signature"]),
    );
    for (const [entries, keys] of [
      [vectors, VECTOR_KEYS],
      [tamper, TAMPER_KEYS],
    ] as const) {
      for (const entry of entries) {
        expect(Object.keys(entry).sort()).toEqual(keys);
        expect(JSON.stringify(entry)).not.toContain("null");
        expect(Object.keys(entry.public_jwk).sort()).toEqual(["crv", "kty", "x"]);
        expect(entry.public_jwk).toMatchObject({ kty: "OKP", crv: "Ed25519" });
        expect(entry.public_jwk.x).toMatch(/^[A-Za-z0-9_-]{43}$/);
        expect(entry.timestamp).toMatch(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/);
        expect(Buffer.from(entry.raw_body_b64, "base64").toString("base64")).toBe(
          entry.raw_body_b64,
        );
        expect(entry.body_sha256_hex).toMatch(/^[0-9a-f]{64}$/);
        expect(entry.signature_b64).toMatch(PADDED_B64);
        expect(typeof entry.message_utf8).toBe("string");
        expect(typeof entry.valid).toBe("boolean");
      }
    }
    expect(vectors.every((vector) => vector.valid)).toBe(true);
    expect(tamper.every((entry) => !entry.valid && baseOf(entry) !== undefined)).toBe(true);
  });

  it("vectors match: preimage, body hash, deterministic signature and RFC8032 key", () => {
    for (const vector of vectors) {
      const bytes = message(vector);
      expect(Buffer.from(bytes).toString("utf8")).toBe(vector.message_utf8);
      expect(sha256Hex(rawBody(vector))).toBe(vector.body_sha256_hex);
      expect(vector.signature_b64).toMatch(PADDED_B64);
      const pkcs8 = Buffer.from(vector.private_pkcs8_b64, "base64");
      expect(pkcs8.toString("hex")).toBe(PKCS8_PREFIX + seed.seed);
      expect(vector.public_jwk.x).toBe(Buffer.from(seed.public, "hex").toString("base64url"));
      expect(
        Buffer.from(signEd25519(bytes, new Uint8Array(pkcs8)), "base64url").toString("base64"),
      ).toBe(vector.signature_b64);
      expect(verify(bytes, vector)).toBe(true);
    }
  });

  it("one flipped byte fails: every tamper entry and a flipped body byte are rejected", () => {
    for (const entry of tamper) {
      const base = baseOf(entry);
      expect(entry.signature_b64).toMatch(PADDED_B64);
      if (entry.field === "signature") {
        expect(message(entry)).toEqual(message(base));
        expect(entry.message_utf8).toBe(base.message_utf8);
        const flipped = Buffer.from(entry.signature_b64, "base64");
        const original = Buffer.from(base.signature_b64, "base64");
        expect(flipped.length).toBe(64);
        expect(flipped[0]).toBe(original[0]! ^ 0x01);
        expect(flipped.subarray(1)).toEqual(original.subarray(1));
      } else {
        expect(Buffer.from(message(entry)).toString("utf8")).toBe(entry.message_utf8);
        expect(entry.message_utf8).not.toBe(base.message_utf8);
        expect(entry.signature_b64).toBe(base.signature_b64);
      }
      expect(verify(new Uint8Array(Buffer.from(entry.message_utf8, "utf8")), entry)).toBe(false);
    }
    for (const vector of vectors) {
      // An empty body has no byte to flip; one 0x01 byte is the smallest change there.
      const body = vector.raw_body_b64 === "" ? Buffer.from([1]) : Buffer.from(rawBody(vector));
      if (vector.raw_body_b64 !== "") body[0] = body[0]! ^ 0x01;
      const mutated = requestSigningMessage({
        method: vector.method,
        requestTarget: vector.request_target,
        timestamp: vector.timestamp,
        rawBody: new Uint8Array(body),
      });
      expect(verify(mutated, vector)).toBe(false);
    }
  });

  it("service parity: the frozen literal preimage bytes", () => {
    for (const vector of vectors) {
      const expected = Buffer.from(
        `${vector.method}\n${vector.request_target}\n${vector.timestamp}\n${sha256Hex(rawBody(vector))}`,
      );
      expect(Buffer.from(message(vector))).toEqual(expected);
    }
  });
});
