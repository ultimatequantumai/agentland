import { generateKeyPairSync } from "node:crypto";
import { describe, expect, it } from "vitest";
import { signEd25519, verifyEd25519 } from "../src/keys.js";
import type { Ed25519PublicJwk } from "../src/keys.js";
import { signedHeadPreimage, signVaultHead, verifySignedHead } from "../src/head.js";

function key() {
  const pair = generateKeyPairSync("ed25519");
  const { kty, crv, x } = pair.publicKey.export({ format: "jwk" });
  return {
    publicKeyJwk: { kty, crv, x } as Ed25519PublicJwk,
    privatePkcs8: pair.privateKey.export({ format: "der", type: "pkcs8" }),
  };
}
const platform = key();
const did = "did:web:agentland.us:agents:weatherwise";
const head = {
  did,
  seq: "3",
  head_hash: "a".repeat(64),
  ts: "2026-10-22T12:00:00.000Z",
};
const kid = "did:web:agentland.us#head-key-1";

describe("signed vault head", () => {
  it("preimage is RFC 8785 bytes of exactly {did, seq, head_hash, ts}", () => {
    expect(Buffer.from(signedHeadPreimage(head)).toString("utf8")).toBe(
      `{"did":"${did}","head_hash":"${"a".repeat(64)}","seq":"3","ts":"2026-10-22T12:00:00.000Z"}`,
    );
    // Member order in the input never changes the bytes.
    const reordered = { ts: head.ts, head_hash: head.head_hash, seq: head.seq, did: head.did };
    expect(Buffer.from(signedHeadPreimage(reordered))).toEqual(
      Buffer.from(signedHeadPreimage(head)),
    );
    // An empty vault head (seq 0) is a valid head.
    expect(() => signedHeadPreimage({ ...head, seq: "0" })).not.toThrow();
  });

  it("preimage rejects extra/missing members and malformed fields", () => {
    expect(() => signedHeadPreimage({ ...head, kid } as typeof head)).toThrow();
    const missing: Partial<typeof head> = { ...head };
    delete missing.ts;
    expect(() => signedHeadPreimage(missing as typeof head)).toThrow();
    for (const head_hash of ["A".repeat(64), "a".repeat(63), "g".repeat(64)])
      expect(() => signedHeadPreimage({ ...head, head_hash })).toThrow();
    for (const seq of ["03", "-1", "1.0", ""])
      expect(() => signedHeadPreimage({ ...head, seq })).toThrow();
    expect(() => signedHeadPreimage({ ...head, seq: 3 as unknown as string })).toThrow();
    for (const ts of [
      "2026-10-22T12:00:00Z",
      "2026-10-22T12:00:00.000+00:00",
      "2026-02-30T00:00:00.000Z",
    ])
      expect(() => signedHeadPreimage({ ...head, ts })).toThrow();
    expect(() => signedHeadPreimage({ ...head, did: "did:web:example.com" })).toThrow();
  });

  it("signVaultHead signs the preimage and carries the explicit key id", () => {
    const signed = signVaultHead({ ...head, kid }, platform.privatePkcs8);
    expect(signed).toEqual({
      ...head,
      kid,
      sig: signEd25519(signedHeadPreimage(head), platform.privatePkcs8),
    });
    expect(verifyEd25519(signedHeadPreimage(head), signed.sig, platform.publicKeyJwk)).toBe(true);
    expect(() => signVaultHead({ ...head, kid: "" }, platform.privatePkcs8)).toThrow();
    expect(() =>
      signVaultHead(head as typeof head & { kid: string }, platform.privatePkcs8),
    ).toThrow();
  });

  it("verifySignedHead accepts only the exact preimage under the published key", () => {
    const signed = signVaultHead({ ...head, kid }, platform.privatePkcs8);
    expect(verifySignedHead(signed, platform.publicKeyJwk)).toBe(true);
    expect(verifySignedHead(signed, key().publicKeyJwk)).toBe(false);
    expect(
      verifySignedHead(
        { ...signed, did: "did:web:agentland.us:agents:other" },
        platform.publicKeyJwk,
      ),
    ).toBe(false);
    expect(verifySignedHead({ ...signed, seq: "4" }, platform.publicKeyJwk)).toBe(false);
    expect(verifySignedHead({ ...signed, head_hash: "b".repeat(64) }, platform.publicKeyJwk)).toBe(
      false,
    );
    expect(
      verifySignedHead({ ...signed, ts: "2026-10-22T12:00:00.001Z" }, platform.publicKeyJwk),
    ).toBe(false);
    // A signature over any other byte string (e.g. the non-canonical JSON) never verifies.
    const loose = signEd25519(Buffer.from(JSON.stringify(head)), platform.privatePkcs8);
    expect(verifySignedHead({ ...signed, sig: loose }, platform.publicKeyJwk)).toBe(false);
  });

  it("verifySignedHead returns false, never throws, on malformed heads", () => {
    const signed = signVaultHead({ ...head, kid }, platform.privatePkcs8);
    expect(verifySignedHead({ ...signed, sig: "not-a-signature" }, platform.publicKeyJwk)).toBe(
      false,
    );
    expect(verifySignedHead({ ...signed, extra: 1 } as typeof signed, platform.publicKeyJwk)).toBe(
      false,
    );
    const noKid: Record<string, unknown> = { ...signed };
    delete noKid.kid;
    expect(verifySignedHead(noKid as unknown as typeof signed, platform.publicKeyJwk)).toBe(false);
    expect(verifySignedHead({ ...signed, kid: "" }, platform.publicKeyJwk)).toBe(false);
    expect(verifySignedHead(null as unknown as typeof signed, platform.publicKeyJwk)).toBe(false);
  });
});
