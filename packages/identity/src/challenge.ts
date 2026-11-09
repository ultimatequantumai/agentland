import { assertBytes, decodeBase64url, exactMembers } from "./canonical.js";
import { assertAgentDid } from "./did.js";
import { verifyEd25519 } from "./keys.js";
import type { Ed25519PublicJwk } from "./keys.js";

// Domain-separated (Assumption A4) so a verifier cannot use an agent as a signing oracle
// for vault intents or request preimages.
const VERIFY_PREFIX = "agentland-verify/1:";
const POP_PREFIX = "agentland-pop/1";

function assertVerifyNonce(value: unknown): asserts value is string {
  if (typeof value !== "string" || !value.startsWith(VERIFY_PREFIX))
    throw new TypeError("agentland-verify/1 nonce required");
  decodeBase64url(value.slice(VERIFY_PREFIX.length), 32);
}

/** Randomness is caller-supplied; this package performs no I/O. */
export function createVerifyNonce(random32: Uint8Array): string {
  assertBytes(random32);
  if (random32.length !== 32) throw new RangeError("32 random bytes required");
  return `${VERIFY_PREFIX}${Buffer.from(random32).toString("base64url")}`;
}

export function verifyNonceSignature(input: {
  readonly nonce: string;
  readonly signature: string;
  readonly publicJwk: Ed25519PublicJwk;
}): boolean {
  try {
    assertVerifyNonce(input.nonce);
    return verifyEd25519(Buffer.from(input.nonce, "utf8"), input.signature, input.publicJwk);
  } catch {
    return false;
  }
}

/** D-15 proof of possession: UTF-8 `agentland-pop/1\n{did}\n{nonce}`. */
export function popPreimage(input: { readonly did: string; readonly nonce: string }): Uint8Array {
  const data = exactMembers(input, ["did", "nonce"]);
  assertAgentDid(data.did);
  assertVerifyNonce(data.nonce);
  return Buffer.from(`${POP_PREFIX}\n${data.did}\n${data.nonce}`, "utf8");
}

export function verifyProofOfPossession(input: {
  readonly did: string;
  readonly nonce: string;
  readonly signature: string;
  readonly publicJwk: Ed25519PublicJwk;
}): boolean {
  try {
    return verifyEd25519(
      popPreimage({ did: input.did, nonce: input.nonce }),
      input.signature,
      input.publicJwk,
    );
  } catch {
    return false;
  }
}
