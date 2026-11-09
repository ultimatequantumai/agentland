import { createPrivateKey } from "node:crypto";
import vectors from "./standards-vectors.json" with { type: "json" };
import type { Ed25519PublicJwk } from "../src/index.js";

/** RFC8032 published test-only material. Never a production credential. */
export function testKey(index = 0) {
  const vector = vectors.ed25519[index]!;
  const publicKeyJwk: Ed25519PublicJwk = {
    kty: "OKP",
    crv: "Ed25519",
    x: Buffer.from(vector.public, "hex").toString("base64url"),
  };
  const privatePkcs8 = createPrivateKey({
    key: { ...publicKeyJwk, d: Buffer.from(vector.seed, "hex").toString("base64url") },
    format: "jwk",
  }).export({ format: "der", type: "pkcs8" });
  return { publicKeyJwk, privatePkcs8, vector };
}
export const did = "did:web:agentland.us:agents:weatherwise";
export const timestamp = "2026-01-01T00:00:00.000Z";
