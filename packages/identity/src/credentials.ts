import {
  CONTEXT,
  ISSUER,
  assertIssuerKeyId,
  checkClaims,
  checkHeader,
  credentialFailure,
  credentialPins,
  decodeJsonSegment,
  parseCompact,
  validateCredential,
} from "./credential-claims.js";
import type {
  AgentLandCredential,
  CredentialType,
  CredentialVerification,
  SeasonEvidence,
  TrustedIssuer,
} from "./credential-claims.js";
import {
  asciiBytes,
  base64urlEncode,
  canonicalize,
  decodeBase64url,
  exactMembers,
  utf8Bytes,
} from "./json.js";
import { signEd25519, verifyEd25519 } from "./keys.js";

export type {
  AgentLandCredential,
  CredentialType,
  CredentialVerification,
  SeasonEvidence,
  TrustedIssuer,
} from "./credential-claims.js";

/** Builds and validates the exact JWS signing input without any key (D-32): the vc_issuer key is
 * HSM-held and never exposes key bytes, so the platform signer signs `signingInput` (ASCII) and
 * `assembleCredential` attaches the detached signature.
 * VC2 application/vc+jwt, RFC7515 compact JWS, RFC9864 alg=Ed25519.
 * Profile times are explicit UTC millisecond instants. Does not infer badge eligibility.
 */
export function credentialSigningInput(input: {
  readonly id: string;
  readonly subjectDid: string;
  readonly type: CredentialType;
  readonly evidence: SeasonEvidence;
  readonly validFrom: string;
  readonly validUntil?: string;
  readonly issuerKeyId: string;
}): { readonly signingInput: string } {
  assertIssuerKeyId(input.issuerKeyId);
  exactMembers(input.evidence, ["season", "n", "shrunk_edge", "audit_root"]);
  const credential: AgentLandCredential = {
    "@context": ["https://www.w3.org/ns/credentials/v2", { ...CONTEXT }],
    id: input.id,
    type: ["VerifiableCredential", input.type],
    issuer: ISSUER,
    credentialSubject: { id: input.subjectDid },
    evidence: { type: "SeasonEvidence", ...input.evidence },
    validFrom: input.validFrom,
    ...(input.validUntil === undefined ? {} : { validUntil: input.validUntil }),
  };
  validateCredential(credential);
  const header = { alg: "Ed25519", kid: input.issuerKeyId, typ: "vc+jwt", cty: "vc" };
  const first = base64urlEncode(utf8Bytes(canonicalize(header)));
  return { signingInput: `${first}.${base64urlEncode(utf8Bytes(canonicalize(credential)))}` };
}

/** Attaches a detached 64-byte Ed25519 signature over the ASCII bytes of `signingInput`. */
export function assembleCredential(signingInput: string, signature: Uint8Array): string {
  if (!(signature instanceof Uint8Array) || signature.length !== 64)
    throw new TypeError("64-byte Ed25519 signature required");
  if (typeof signingInput !== "string" || !/^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$/.test(signingInput))
    throw new TypeError("Two base64url JWS segments required");
  return `${signingInput}.${base64urlEncode(signature)}`;
}

/** Software-key issuance (tests, offline tools); production issues through the HSM split. */
export function issueCredential(input: {
  readonly id: string;
  readonly subjectDid: string;
  readonly type: CredentialType;
  readonly evidence: SeasonEvidence;
  readonly validFrom: string;
  readonly validUntil?: string;
  readonly issuerKeyId: string;
  readonly privatePkcs8: Uint8Array;
}): string {
  const { signingInput } = credentialSigningInput(input);
  const signature = signEd25519(asciiBytes(signingInput), input.privatePkcs8);
  return assembleCredential(signingInput, decodeBase64url(signature, 64));
}

/** Verifies ORIGINAL received compact bytes under external authority and time.
 * No embedded-key trust, resolver, online status/revocation or factual-evidence assertion.
 * Parsing and claim checks are shared with the browser verifier (web.ts) via credential-claims.
 */
export function verifyCredential(
  compact: string,
  options: {
    readonly trustedIssuer: TrustedIssuer;
    readonly expectedSubjectDid: string;
    readonly now: string;
  },
): CredentialVerification {
  try {
    const pins = credentialPins(options);
    const { first, second, signature, header } = parseCompact(compact);
    const untrusted = checkHeader(header, pins.trustedIssuer.kid);
    if (untrusted) return untrusted;
    const payload = decodeJsonSegment(second);
    const signed = asciiBytes(`${first}.${second}`);
    if (!verifyEd25519(signed, signature, pins.trustedIssuer.publicKeyJwk))
      return credentialFailure("invalid-signature");
    return checkClaims(payload, pins.expectedSubjectDid, pins.now);
  } catch {
    return credentialFailure("invalid-schema-or-trust-pins");
  }
}
