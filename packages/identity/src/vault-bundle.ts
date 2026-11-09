import { canonicalBytes } from "./canonical.js";
import { createInclusionProof, merkleRoot, verifyInclusionProof } from "./merkle.js";
import type { VaultProofBundle } from "./proof.js";
import type { VaultEntry } from "./vault.js";

/**
 * Pure rows → composed bundle (D-23). `chain` is the complete genesis→current-head chain, so the
 * bundle verifies against the current signed head; only the proved entry's UTC day forms the
 * daily tree. It never compares the chain with `auditLeaves`: the verifier is the authority, so
 * altered rows still yield a bundle that verifyVaultBundle rejects.
 */
export function buildVaultProofBundle(input: {
  did: string;
  chain: readonly VaultEntry[];
  seq: string;
  auditLeaves: readonly Uint8Array[];
  vaultLeafIndex: number;
}): VaultProofBundle & { audit: NonNullable<VaultProofBundle["audit"]> } {
  const { did, chain, seq, auditLeaves, vaultLeafIndex } = input;
  const entry = chain.find((candidate) => candidate.seq === seq);
  if (!entry) throw new RangeError("Entry is not in the chain");
  // D-18: leaf 0 is always the audit-log head; vault roots start at 1.
  if (
    !Number.isSafeInteger(vaultLeafIndex) ||
    vaultLeafIndex < 1 ||
    vaultLeafIndex >= auditLeaves.length
  )
    throw new RangeError("Vault-root leaf index out of range");
  if (auditLeaves.some((leaf) => !(leaf instanceof Uint8Array) || leaf.length !== 32))
    throw new TypeError("Audit leaves must be 32-byte roots or hashes");
  const day = entry.ts_server.slice(0, 10);
  const daily = chain.filter((candidate) => candidate.ts_server.startsWith(day));
  const leaf = auditLeaves[vaultLeafIndex]!;
  const audit = {
    vault_root_leaf_bytes: Buffer.from(leaf).toString("base64url"),
    proof: createInclusionProof(auditLeaves, vaultLeafIndex),
  };
  if (!verifyInclusionProof(leaf, audit.proof, merkleRoot(auditLeaves)))
    throw new Error("Audit path does not reproduce the audit root");
  return {
    format: "agentland-vault/1",
    did,
    entries: chain,
    proof: {
      seq,
      ...createInclusionProof(
        daily.map((candidate) => canonicalBytes(candidate)),
        daily.indexOf(entry),
      ),
    },
    audit,
  };
}
