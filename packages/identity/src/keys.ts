import { createPrivateKey, createPublicKey, sign, verify } from "node:crypto";
import { assertBytes, decodeBase64url, exactMembers } from "./canonical.js";

export type Ed25519PublicJwk = { readonly kty: "OKP"; readonly crv: "Ed25519"; readonly x: string };
export type X25519PublicJwk = { readonly kty: "OKP"; readonly crv: "X25519"; readonly x: string };
export type PublicJwk = Ed25519PublicJwk | X25519PublicJwk;

export function validatePublicJwk(value: unknown, curve?: PublicJwk["crv"]): PublicJwk {
  const key = exactMembers(value, ["kty", "crv", "x"]);
  if (
    key.kty !== "OKP" ||
    (key.crv !== "Ed25519" && key.crv !== "X25519") ||
    (curve !== undefined && key.crv !== curve)
  )
    throw new TypeError("Wrong public key type or purpose");
  decodeBase64url(key.x, 32);
  return { kty: "OKP", crv: key.crv, x: key.x as string };
}

/** Caller-owned PKCS8 DER only; never generates, stores or returns a private key. */
export function signEd25519(message: Uint8Array, privatePkcs8: Uint8Array): string {
  assertBytes(message);
  assertBytes(privatePkcs8);
  try {
    const key = createPrivateKey({ key: Buffer.from(privatePkcs8), type: "pkcs8", format: "der" });
    if (key.asymmetricKeyType !== "ed25519") throw new TypeError("Ed25519 private key required");
    return sign(null, message, key).toString("base64url");
  } catch {
    throw new TypeError("Invalid Ed25519 PKCS8 signing input");
  }
}

/** Signature possession is not replay protection, custody or service authorization. */
export function verifyEd25519(
  message: Uint8Array,
  signature: string,
  publicJwk: Ed25519PublicJwk,
): boolean {
  try {
    assertBytes(message);
    const key = validatePublicJwk(publicJwk, "Ed25519");
    const bytes = decodeBase64url(signature, 64);
    return verify(null, message, createPublicKey({ key: { ...key }, format: "jwk" }), bytes);
  } catch {
    return false;
  }
}
