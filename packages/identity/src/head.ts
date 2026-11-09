import { assertHash, assertTimestamp, canonicalBytes, exactMembers } from "./canonical.js";
import { assertAgentDid } from "./did.js";
import { signEd25519, verifyEd25519 } from "./keys.js";
import type { Ed25519PublicJwk } from "./keys.js";
import { assertSequence } from "./vault.js";

export interface VaultHeadStatement {
  readonly did: string;
  readonly seq: string;
  readonly head_hash: string;
  readonly ts: string;
}
export interface SignedVaultHead extends VaultHeadStatement {
  readonly kid: string;
  readonly sig: string;
}

/** D-08: RFC 8785 bytes of exactly {did, seq, head_hash, ts}; kid and sig are outside the preimage. */
export function signedHeadPreimage(head: VaultHeadStatement): Uint8Array {
  const data = exactMembers(head, ["did", "seq", "head_hash", "ts"]);
  assertAgentDid(data.did);
  assertSequence(data.seq, true);
  assertHash(data.head_hash);
  assertTimestamp(data.ts);
  return canonicalBytes({ did: data.did, seq: data.seq, head_hash: data.head_hash, ts: data.ts });
}

/** Tests and bootstrap only; the service signs through HSM custody. */
export function signVaultHead(
  head: VaultHeadStatement & { readonly kid: string },
  privatePkcs8: Uint8Array,
): SignedVaultHead {
  const { kid, ...statement } = exactMembers(head, ["did", "seq", "head_hash", "ts", "kid"]);
  if (typeof kid !== "string" || kid.length === 0) throw new TypeError("Key id required");
  const preimage = signedHeadPreimage(statement as unknown as VaultHeadStatement);
  return {
    ...(statement as unknown as VaultHeadStatement),
    kid,
    sig: signEd25519(preimage, privatePkcs8),
  };
}

export function verifySignedHead(head: SignedVaultHead, publicJwk: Ed25519PublicJwk): boolean {
  try {
    const { kid, sig, ...statement } = exactMembers(head, [
      "did",
      "seq",
      "head_hash",
      "ts",
      "kid",
      "sig",
    ]);
    if (typeof kid !== "string" || kid.length === 0) return false;
    return verifyEd25519(
      signedHeadPreimage(statement as unknown as VaultHeadStatement),
      sig as string,
      publicJwk,
    );
  } catch {
    return false;
  }
}
