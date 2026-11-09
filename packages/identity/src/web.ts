// Browser-safe entry `@agentland/identity/web` (D-36, UI-SPEC OQ-5): the visitor's browser is the
// verifier. Imports only node-free modules; the parity test walks this import graph.
import {
  checkClaims,
  checkHeader,
  credentialFailure,
  credentialPins,
  decodeJsonSegment,
  parseCompact,
} from "./credential-claims.js";
import type { CredentialVerification, TrustedIssuer } from "./credential-claims.js";
import { asciiBytes, decodeBase64url } from "./json.js";
import type { Ed25519PublicJwk } from "./keys.js";

export type {
  AgentLandCredential,
  CredentialType,
  CredentialVerification,
  SeasonEvidence,
  TrustedIssuer,
} from "./credential-claims.js";

/** The runtime has no WebCrypto Ed25519, so it cannot verify; never reported as a failed check. */
export class Ed25519UnsupportedError extends Error {
  constructor() {
    super("This browser can't verify Ed25519 signatures");
    this.name = "Ed25519UnsupportedError";
  }
}

async function verifySignature(
  signingInput: string,
  signature: string,
  publicKeyJwk: Ed25519PublicJwk,
): Promise<boolean> {
  // Typed as always present, but absent in insecure contexts and old runtimes.
  const subtle = (globalThis.crypto as Partial<typeof globalThis.crypto> | undefined)?.subtle;
  if (subtle === undefined) throw new Ed25519UnsupportedError();
  try {
    const bytes = decodeBase64url(signature, 64);
    const key = await subtle.importKey("jwk", { ...publicKeyJwk }, { name: "Ed25519" }, false, [
      "verify",
    ]);
    return await subtle.verify("Ed25519", key, bytes, asciiBytes(signingInput));
  } catch (error) {
    if ((error as { name?: unknown } | null)?.name === "NotSupportedError")
      throw new Ed25519UnsupportedError();
    // Mirrors keys.ts verifyEd25519: any other signature or key failure is "not verified".
    return false;
  }
}

/** Same pins, steps and result objects as `verifyCredential`, with WebCrypto doing the signature.
 * Throws only `Ed25519UnsupportedError`; every other failure is a result object.
 */
export async function verifyCredentialWeb(
  compact: string,
  options: {
    readonly trustedIssuer: TrustedIssuer;
    readonly expectedSubjectDid: string;
    readonly now: string;
  },
): Promise<CredentialVerification> {
  try {
    const pins = credentialPins(options);
    const { first, second, signature, header } = parseCompact(compact);
    const untrusted = checkHeader(header, pins.trustedIssuer.kid);
    if (untrusted) return untrusted;
    const payload = decodeJsonSegment(second);
    if (!(await verifySignature(`${first}.${second}`, signature, pins.trustedIssuer.publicKeyJwk)))
      return credentialFailure("invalid-signature");
    return checkClaims(payload, pins.expectedSubjectDid, pins.now);
  } catch (error) {
    if (error instanceof Ed25519UnsupportedError) throw error;
    return credentialFailure("invalid-schema-or-trust-pins");
  }
}
