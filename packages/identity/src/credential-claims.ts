// Node-free: shared by the Node verifier (credentials.ts) and the browser verifier (web.ts), so
// parsing, trust pins and claim checks cannot drift between the two (D-36, T-10-02-02).
import {
  assertAgentDid,
  assertHash,
  assertTimestamp,
  canonicalize,
  decodeBase64url,
  exactMembers,
  parseIJson,
} from "./json.js";
import type { Ed25519PublicJwk } from "./keys.js";
import type { VerificationFailure } from "./vault.js";

export type CredentialType =
  "Calibrated" | "MarketBeater" | "Teacher" | "Ironclad" | "EarlyBird" | "SeasonResult";
export interface SeasonEvidence {
  /** A season row id, or the literal `alltime` for the all-time scope (D-33). */
  readonly season: string;
  readonly n: number;
  readonly shrunk_edge: number;
  readonly audit_root: string;
}
export interface AgentLandCredential {
  readonly "@context": readonly (string | Readonly<Record<string, string>>)[];
  readonly id: string;
  readonly type: readonly ["VerifiableCredential", CredentialType];
  readonly issuer: "did:web:agentland.us";
  readonly credentialSubject: { readonly id: string };
  readonly evidence: SeasonEvidence & { readonly type: "SeasonEvidence" };
  readonly validFrom: string;
  readonly validUntil?: string;
}
export interface TrustedIssuer {
  readonly issuer: string;
  readonly kid: string;
  readonly publicKeyJwk: Ed25519PublicJwk;
}
export type CredentialVerification =
  { readonly valid: true; readonly credential: AgentLandCredential } | VerificationFailure;

export const ISSUER = "did:web:agentland.us";
export const CONTEXT = {
  Calibrated: "https://agentland.us/spec/agentland-vc/1#Calibrated",
  MarketBeater: "https://agentland.us/spec/agentland-vc/1#MarketBeater",
  Teacher: "https://agentland.us/spec/agentland-vc/1#Teacher",
  Ironclad: "https://agentland.us/spec/agentland-vc/1#Ironclad",
  EarlyBird: "https://agentland.us/spec/agentland-vc/1#EarlyBird",
  SeasonResult: "https://agentland.us/spec/agentland-vc/1#SeasonResult",
  SeasonEvidence: "https://agentland.us/spec/agentland-vc/1#SeasonEvidence",
  season: "https://agentland.us/spec/agentland-vc/1#season",
  n: "https://agentland.us/spec/agentland-vc/1#n",
  shrunk_edge: "https://agentland.us/spec/agentland-vc/1#shrunk_edge",
  audit_root: "https://agentland.us/spec/agentland-vc/1#audit_root",
} as const;
export const CREDENTIAL_TYPES: Readonly<Record<CredentialType, true>> = {
  Calibrated: true,
  MarketBeater: true,
  Teacher: true,
  Ironclad: true,
  EarlyBird: true,
  SeasonResult: true,
};
const CONTEXT_BYTES = canonicalize(["https://www.w3.org/ns/credentials/v2", CONTEXT]);

export function credentialFailure(reason: string): VerificationFailure {
  return { valid: false, error: { stage: "credential", reason } };
}

export function assertIssuerKeyId(value: unknown): asserts value is string {
  if (typeof value !== "string" || !/^did:web:agentland\.us#[A-Za-z0-9._~-]+$/.test(value))
    throw new TypeError("Absolute AgentLand issuer key ID required");
}

export function validateCredential(value: unknown): asserts value is AgentLandCredential {
  const credential = exactMembers(
    value,
    ["@context", "id", "type", "issuer", "credentialSubject", "evidence", "validFrom"],
    ["validUntil"],
  );
  canonicalize(credential);
  if (canonicalize(credential["@context"]) !== CONTEXT_BYTES || credential.issuer !== ISSUER)
    throw new TypeError("Unsupported credential context or issuer");
  if (
    typeof credential.id !== "string" ||
    /\s/.test(credential.id) ||
    !/^[A-Za-z][A-Za-z0-9+.-]*:/.test(credential.id)
  )
    throw new TypeError("Absolute credential ID required");
  try {
    new URL(credential.id);
  } catch {
    throw new TypeError("Invalid credential ID");
  }
  const types: unknown = credential.type;
  if (
    !Array.isArray(types) ||
    types.length !== 2 ||
    types[0] !== "VerifiableCredential" ||
    typeof types[1] !== "string" ||
    !Object.hasOwn(CREDENTIAL_TYPES, types[1])
  )
    throw new TypeError("Unsupported AgentLand credential type");
  const subject = exactMembers(credential.credentialSubject, ["id"]);
  assertAgentDid(subject.id);
  const evidence = exactMembers(credential.evidence, [
    "type",
    "season",
    "n",
    "shrunk_edge",
    "audit_root",
  ]);
  if (
    evidence.type !== "SeasonEvidence" ||
    typeof evidence.season !== "string" ||
    evidence.season.length === 0 ||
    typeof evidence.n !== "number" ||
    !Number.isSafeInteger(evidence.n) ||
    evidence.n < 0 ||
    typeof evidence.shrunk_edge !== "number" ||
    !Number.isFinite(evidence.shrunk_edge)
  )
    throw new TypeError("Invalid season evidence");
  assertHash(evidence.audit_root);
  assertTimestamp(credential.validFrom);
  if (Object.hasOwn(credential, "validUntil")) {
    assertTimestamp(credential.validUntil);
    if (credential.validUntil < credential.validFrom)
      throw new TypeError("Reversed credential validity");
  }
}

/** External authority and time only; the VC's own kid or key is never trusted (T-10-02-01). */
export function credentialPins(options: unknown): {
  readonly trustedIssuer: TrustedIssuer;
  readonly expectedSubjectDid: string;
  readonly now: string;
} {
  const pins = exactMembers(options, ["trustedIssuer", "expectedSubjectDid", "now"]);
  const trust = exactMembers(pins.trustedIssuer, ["issuer", "kid", "publicKeyJwk"]);
  if (trust.issuer !== ISSUER) throw new TypeError("Wrong trusted issuer");
  assertIssuerKeyId(trust.kid);
  // Same rule as keys.ts validatePublicJwk(…, "Ed25519"); this node-free path cannot import it.
  const jwk = exactMembers(trust.publicKeyJwk, ["kty", "crv", "x"]);
  if (jwk.kty !== "OKP" || jwk.crv !== "Ed25519")
    throw new TypeError("Wrong public key type or purpose");
  decodeBase64url(jwk.x, 32);
  assertAgentDid(pins.expectedSubjectDid);
  assertTimestamp(pins.now);
  return {
    trustedIssuer: {
      issuer: ISSUER,
      kid: trust.kid,
      publicKeyJwk: { kty: "OKP", crv: "Ed25519", x: jwk.x as string },
    },
    expectedSubjectDid: pins.expectedSubjectDid,
    now: pins.now,
  };
}

export function decodeJsonSegment(segment: string): unknown {
  const decoder = new TextDecoder("utf-8", { fatal: true, ignoreBOM: true });
  return parseIJson(decoder.decode(decodeBase64url(segment)));
}

/** Splits the ORIGINAL compact bytes; the payload is decoded separately (decodeJsonSegment) so a
 * bad protected header is reported before payload errors, as verifyCredential always has. */
export function parseCompact(compact: unknown): {
  readonly first: string;
  readonly second: string;
  readonly signature: string;
  readonly header: Readonly<Record<string, unknown>>;
} {
  if (typeof compact !== "string") throw new TypeError("Compact JWS required");
  const parts = compact.split(".");
  if (parts.length !== 3) throw new TypeError("Three JWS segments required");
  const first = parts[0]!;
  const header = exactMembers(decodeJsonSegment(first), ["alg", "kid", "typ", "cty"]);
  return { first, second: parts[1]!, signature: parts[2]!, header };
}

export function checkHeader(
  header: Readonly<Record<string, unknown>>,
  trustedKid: string,
): VerificationFailure | undefined {
  if (
    header.alg !== "Ed25519" ||
    header.typ !== "vc+jwt" ||
    header.cty !== "vc" ||
    header.kid !== trustedKid
  )
    return credentialFailure("untrusted-protected-header");
  return undefined;
}

/** Runs after the signature check; schema failures throw for the caller's catch-all. */
export function checkClaims(
  payload: unknown,
  expectedSubjectDid: string,
  now: string,
): CredentialVerification {
  validateCredential(payload);
  if (payload.credentialSubject.id !== expectedSubjectDid)
    return credentialFailure("subject-mismatch");
  if (now < payload.validFrom || (payload.validUntil !== undefined && now >= payload.validUntil))
    return credentialFailure("outside-validity-period");
  return { valid: true, credential: payload };
}

/** Decodes without verifying (server-side evidence projection); throws on a malformed credential.
 * Never treat the result as verified: no signature, trust pin or time is checked. */
export function credentialClaims(compact: string): {
  readonly header: Readonly<Record<string, unknown>>;
  readonly credential: AgentLandCredential;
} {
  const { header, second } = parseCompact(compact);
  const credential = decodeJsonSegment(second);
  validateCredential(credential);
  return { header, credential };
}
