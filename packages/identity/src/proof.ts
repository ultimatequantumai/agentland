import { assertHash, canonicalBytes, decodeBase64url, exactMembers } from "./canonical.js";
import { merkleRoot, verifyInclusionProof } from "./merkle.js";
import type { MerkleProof } from "./merkle.js";
import { assertSequence, validateVaultChain } from "./vault.js";
import type {
  VaultChainSuccess,
  VaultEntry,
  VaultHead,
  VaultSigningKey,
  VerificationFailure,
} from "./vault.js";

export interface VaultProofBundle {
  readonly format: "agentland-vault/1";
  readonly did: string;
  readonly entries: readonly VaultEntry[];
  readonly proof: MerkleProof & { readonly seq: string };
  /** Generic composition only: raw32 verified vault-root bytes, not an invented daily inventory. */
  readonly audit?: { readonly vault_root_leaf_bytes: string; readonly proof: MerkleProof };
}
export type VaultBundleResult =
  | (VaultChainSuccess & { readonly proved_seq: string; readonly root: string })
  | VerificationFailure;

/** Bundle data never supplies authority: keys, complete head and published root are external pins. */
export function verifyVaultBundle(
  bundle: VaultProofBundle,
  options: {
    readonly keys: readonly VaultSigningKey[];
    readonly expectedHead: VaultHead;
    readonly publishedRoot: string;
  },
): VaultBundleResult {
  try {
    const pins = exactMembers(options, ["keys", "expectedHead", "publishedRoot"]);
    assertHash(pins.publishedRoot);
    const data = exactMembers(bundle, ["format", "did", "entries", "proof"], ["audit"]);
    if (data.format !== "agentland-vault/1") throw new TypeError("Unsupported export format");
    const chain = validateVaultChain({
      did: data.did as string,
      entries: data.entries as readonly VaultEntry[],
      keys: pins.keys as readonly VaultSigningKey[],
      expectedHead: pins.expectedHead as VaultHead,
    });
    if (!chain.valid) return chain;
    const entries = data.entries as readonly VaultEntry[];
    const raw = exactMembers(data.proof, ["seq", "leaf_index", "tree_size", "siblings"]);
    assertSequence(raw.seq);
    const selected = entries[Number(raw.seq) - 1];
    if (selected?.seq !== raw.seq)
      return { valid: false, error: { stage: "proof", reason: "entry-coordinate-mismatch" } };
    // Chain validation already established exact UTC timestamps and global sequence order.
    const day = selected.ts_server.slice(0, 10);
    const leaves: Uint8Array[] = [];
    let leafIndex = -1;
    for (const entry of entries) {
      if (!entry.ts_server.startsWith(day)) continue;
      if (entry.seq === raw.seq) leafIndex = leaves.length;
      leaves.push(canonicalBytes(entry));
    }
    if (
      typeof raw.leaf_index !== "number" ||
      !Number.isSafeInteger(raw.leaf_index) ||
      raw.leaf_index < 0 ||
      raw.leaf_index !== leafIndex ||
      raw.tree_size !== leaves.length
    )
      return { valid: false, error: { stage: "proof", reason: "entry-coordinate-mismatch" } };
    const proof: MerkleProof = {
      leaf_index: raw.leaf_index,
      tree_size: raw.tree_size as number,
      siblings: raw.siblings as readonly string[],
    };
    const vaultRoot = merkleRoot(leaves);
    if (!verifyInclusionProof(leaves[raw.leaf_index]!, proof, vaultRoot))
      return { valid: false, error: { stage: "proof", reason: "invalid-entry-path" } };
    if (Object.hasOwn(data, "audit")) {
      const audit = exactMembers(data.audit, ["vault_root_leaf_bytes", "proof"]);
      const leaf = decodeBase64url(audit.vault_root_leaf_bytes, 32);
      if (
        leaf.toString("hex") !== vaultRoot ||
        !verifyInclusionProof(leaf, audit.proof as MerkleProof, pins.publishedRoot)
      )
        return { valid: false, error: { stage: "audit", reason: "root-leaf-or-path-mismatch" } };
    } else if (vaultRoot !== pins.publishedRoot)
      return { valid: false, error: { stage: "proof", reason: "published-root-mismatch" } };
    return { ...chain, proved_seq: raw.seq, root: pins.publishedRoot };
  } catch {
    return { valid: false, error: { stage: "bundle", reason: "invalid-schema-or-trust-pins" } };
  }
}
