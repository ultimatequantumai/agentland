import { generateKeyPairSync } from "node:crypto";
import { describe, expect, it } from "vitest";
import { signEd25519 } from "../src/keys.js";
import type { Ed25519PublicJwk } from "../src/keys.js";
import {
  createVerifyNonce,
  popPreimage,
  verifyNonceSignature,
  verifyProofOfPossession,
} from "../src/challenge.js";

function key() {
  const pair = generateKeyPairSync("ed25519");
  const { kty, crv, x } = pair.publicKey.export({ format: "jwk" });
  return {
    publicKeyJwk: { kty, crv, x } as Ed25519PublicJwk,
    privatePkcs8: pair.privateKey.export({ format: "der", type: "pkcs8" }),
  };
}
const agent = key();
const did = "did:web:agentland.us:agents:weatherwise";
const random = Uint8Array.from({ length: 32 }, (_, i) => i);
const nonce = createVerifyNonce(random);
const utf8 = (text: string) => Buffer.from(text, "utf8");

describe("verify nonce", () => {
  it("is the domain-separated base64url of exactly 32 caller-supplied bytes", () => {
    expect(nonce).toBe(`agentland-verify/1:${Buffer.from(random).toString("base64url")}`);
    expect(nonce).toBe("agentland-verify/1:AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8");
    expect(createVerifyNonce(new Uint8Array(32))).toBe(`agentland-verify/1:${"A".repeat(43)}`);
  });

  it("rejects any length other than 32 bytes", () => {
    for (const length of [0, 16, 31, 33, 64])
      expect(() => createVerifyNonce(new Uint8Array(length))).toThrow();
    expect(() => createVerifyNonce(Array(32).fill(0) as unknown as Uint8Array)).toThrow();
  });

  it("verifies Ed25519 over the UTF-8 nonce string only", () => {
    const signature = signEd25519(utf8(nonce), agent.privatePkcs8);
    expect(verifyNonceSignature({ nonce, signature, publicJwk: agent.publicKeyJwk })).toBe(true);
    expect(verifyNonceSignature({ nonce, signature, publicJwk: key().publicKeyJwk })).toBe(false);
    const other = createVerifyNonce(new Uint8Array(32));
    expect(verifyNonceSignature({ nonce: other, signature, publicJwk: agent.publicKeyJwk })).toBe(
      false,
    );
    // A signature over the PoP preimage is not a verify signature.
    const pop = signEd25519(popPreimage({ did, nonce }), agent.privatePkcs8);
    expect(verifyNonceSignature({ nonce, signature: pop, publicJwk: agent.publicKeyJwk })).toBe(
      false,
    );
  });

  it("refuses non-domain-separated nonces even with a valid signature", () => {
    const bare = Buffer.from(random).toString("base64url");
    const signature = signEd25519(utf8(bare), agent.privatePkcs8);
    expect(verifyNonceSignature({ nonce: bare, signature, publicJwk: agent.publicKeyJwk })).toBe(
      false,
    );
    expect(
      verifyNonceSignature({ nonce, signature: "garbage", publicJwk: agent.publicKeyJwk }),
    ).toBe(false);
  });
});

describe("proof of possession", () => {
  it("preimage is UTF-8 `agentland-pop/1\\n{did}\\n{nonce}`", () => {
    expect(Buffer.from(popPreimage({ did, nonce })).toString("utf8")).toBe(
      `agentland-pop/1\n${did}\n${nonce}`,
    );
    expect(Buffer.from(popPreimage({ did, nonce }))).toEqual(
      utf8(`agentland-pop/1\ndid:web:agentland.us:agents:weatherwise\n${nonce}`),
    );
  });

  it("preimage rejects malformed did, nonce or members", () => {
    expect(() => popPreimage({ did: "did:web:example.com", nonce })).toThrow();
    expect(() => popPreimage({ did: `${did}\nx`, nonce })).toThrow();
    expect(() => popPreimage({ did, nonce: "agentland-verify/1:short" })).toThrow();
    expect(() => popPreimage({ did, nonce: Buffer.from(random).toString("base64url") })).toThrow();
    expect(() => popPreimage({ did, nonce, extra: 1 } as { did: string; nonce: string })).toThrow();
  });

  it("verifies the candidate key's signature over the PoP preimage only", () => {
    const signature = signEd25519(popPreimage({ did, nonce }), agent.privatePkcs8);
    const input = { did, nonce, signature, publicJwk: agent.publicKeyJwk };
    expect(verifyProofOfPossession(input)).toBe(true);
    expect(verifyProofOfPossession({ ...input, publicJwk: key().publicKeyJwk })).toBe(false);
    expect(verifyProofOfPossession({ ...input, did: "did:web:agentland.us:agents:other" })).toBe(
      false,
    );
    expect(
      verifyProofOfPossession({ ...input, nonce: createVerifyNonce(new Uint8Array(32)) }),
    ).toBe(false);
  });

  it("rejects a signature over the bare nonce (domain separation)", () => {
    const signature = signEd25519(utf8(nonce), agent.privatePkcs8);
    expect(verifyProofOfPossession({ did, nonce, signature, publicJwk: agent.publicKeyJwk })).toBe(
      false,
    );
  });

  it("returns false, never throws, on malformed input", () => {
    const signature = signEd25519(popPreimage({ did, nonce }), agent.privatePkcs8);
    expect(
      verifyProofOfPossession({ did: "bad", nonce, signature, publicJwk: agent.publicKeyJwk }),
    ).toBe(false);
    expect(
      verifyProofOfPossession({ did, nonce, signature: "bad", publicJwk: agent.publicKeyJwk }),
    ).toBe(false);
  });
});
