/**
 * Squad proof bundles: the vault-bundle.ts / proof.ts shapes over agentland-squad/1. The squad
 * day root enters the daily audit tree as a raw 32-byte notary leaf (D-38), so the audit tree
 * shape is unchanged. Pins are external; the bundle never authorizes itself.
 */
import { assertHash, canonicalBytes, decodeBase64url, exactMembers } from "./canonical.js";
import { createInclusionProof, merkleRoot, verifyInclusionProof } from "./merkle.js";
import type { MerkleProof } from "./merkle.js";
import { replaySquad } from "./squad-replay.js";
import type { SquadReplaySuccess } from "./squad-replay.js";
import type {
  SquadEntry,
  SquadPlatformKey,
  SquadSignerKeys,
  SquadStatementPayload,
} from "./squad.js";
import { assertSequence } from "./vault.js";
import type { VaultHead, VerificationFailure } from "./vault.js";

export interface SquadProofBundle {
  readonly format: "agentland-squad/1";
  readonly squad_id: string;
  readonly entries: readonly SquadEntry[];
  readonly statements: readonly { readonly seq: string; readonly content_b64url: string }[];
  readonly proof: MerkleProof & { readonly seq: string };
  readonly audit?: { readonly squad_root_leaf_bytes: string; readonly proof: MerkleProof };
}
export type SquadBundleResult =
  | (SquadReplaySuccess & { readonly proved_seq: string; readonly root: string })
  | VerificationFailure;

/** Pure rows → bundle. Never compares the chain with `auditLeaves`: the verifier is the authority. */
export function buildSquadProofBundle(input: {
  squadId: string;
  entries: readonly SquadEntry[];
  statements: readonly SquadStatementPayload[];
  seq: string;
  auditLeaves: readonly Uint8Array[];
  squadLeafIndex: number;
}): SquadProofBundle & { audit: NonNullable<SquadProofBundle["audit"]> } {
  const { squadId, entries, statements, seq, auditLeaves, squadLeafIndex } = input;
  const entry = entries.find((candidate) => candidate.seq === seq);
  if (!entry) throw new RangeError("Entry is not in the chain");
  // Leaf 0 is always the audit-log head; squad roots start at 1.
  if (
    !Number.isSafeInteger(squadLeafIndex) ||
    squadLeafIndex < 1 ||
    squadLeafIndex >= auditLeaves.length
  )
    throw new RangeError("Squad-root leaf index out of range");
  if (auditLeaves.some((leaf) => !(leaf instanceof Uint8Array) || leaf.length !== 32))
    throw new TypeError("Audit leaves must be 32-byte roots or hashes");
  const day = entry.ts_server.slice(0, 10);
  const daily = entries.filter((candidate) => candidate.ts_server.startsWith(day));
  return {
    format: "agentland-squad/1",
    squad_id: squadId,
    entries,
    statements: statements.map((s) => ({
      seq: s.seq,
      content_b64url: Buffer.from(s.content).toString("base64url"),
    })),
    proof: {
      seq,
      ...createInclusionProof(
        daily.map((candidate) => canonicalBytes(candidate)),
        daily.indexOf(entry),
      ),
    },
    audit: {
      squad_root_leaf_bytes: Buffer.from(auditLeaves[squadLeafIndex]!).toString("base64url"),
      proof: createInclusionProof(auditLeaves, squadLeafIndex),
    },
  };
}

function verifyProofs(
  data: Record<string, unknown>,
  entries: readonly SquadEntry[],
  publishedRoot: string,
): VerificationFailure | string {
  const raw = exactMembers(data.proof, ["seq", "leaf_index", "tree_size", "siblings"]);
  assertSequence(raw.seq);
  const selected = entries[Number(raw.seq) - 1];
  const mismatch: VerificationFailure = {
    valid: false,
    error: { stage: "proof", reason: "entry-coordinate-mismatch" },
  };
  if (selected?.seq !== raw.seq) return mismatch;
  const day = selected.ts_server.slice(0, 10);
  const daily = entries.filter((entry) => entry.ts_server.startsWith(day));
  const leaves = daily.map((entry) => canonicalBytes(entry));
  const leafIndex = daily.indexOf(selected);
  if (raw.leaf_index !== leafIndex || raw.tree_size !== leaves.length) return mismatch;
  const proof: MerkleProof = {
    leaf_index: leafIndex,
    tree_size: leaves.length,
    siblings: raw.siblings as readonly string[],
  };
  const squadRoot = merkleRoot(leaves);
  if (!verifyInclusionProof(leaves[leafIndex]!, proof, squadRoot))
    return { valid: false, error: { stage: "proof", reason: "invalid-entry-path" } };
  if (Object.hasOwn(data, "audit")) {
    const audit = exactMembers(data.audit, ["squad_root_leaf_bytes", "proof"]);
    const leaf = decodeBase64url(audit.squad_root_leaf_bytes, 32);
    if (
      leaf.toString("hex") !== squadRoot ||
      !verifyInclusionProof(leaf, audit.proof as MerkleProof, publishedRoot)
    )
      return { valid: false, error: { stage: "audit", reason: "root-leaf-or-path-mismatch" } };
  } else if (squadRoot !== publishedRoot)
    return { valid: false, error: { stage: "proof", reason: "published-root-mismatch" } };
  return raw.seq;
}

export function verifySquadBundle(
  bundle: SquadProofBundle,
  pins: {
    signerKeys: readonly SquadSignerKeys[];
    platformKeys: readonly SquadPlatformKey[];
    expectedHead: VaultHead;
    publishedRoot: string;
  },
): SquadBundleResult {
  try {
    const trusted = exactMembers(pins, [
      "signerKeys",
      "platformKeys",
      "expectedHead",
      "publishedRoot",
    ]);
    assertHash(trusted.publishedRoot);
    const data = exactMembers(
      bundle,
      ["format", "squad_id", "entries", "statements", "proof"],
      ["audit"],
    );
    if (data.format !== "agentland-squad/1") throw new TypeError("Unsupported squad format");
    if (!Array.isArray(data.statements)) throw new TypeError("Statement array required");
    const statements = data.statements.map((row: unknown) => {
      const s = exactMembers(row, ["seq", "content_b64url"]);
      return { seq: s.seq as string, content: new Uint8Array(decodeBase64url(s.content_b64url)) };
    });
    const chain = replaySquad({
      squadId: data.squad_id as string,
      entries: data.entries as readonly SquadEntry[],
      statements,
      signerKeys: trusted.signerKeys as readonly SquadSignerKeys[],
      platformKeys: trusted.platformKeys as readonly SquadPlatformKey[],
      expectedHead: trusted.expectedHead as VaultHead,
    });
    if (!chain.valid) return chain;
    const proved = verifyProofs(data, data.entries as readonly SquadEntry[], trusted.publishedRoot);
    if (typeof proved !== "string") return proved;
    return { ...chain, proved_seq: proved, root: trusted.publishedRoot };
  } catch {
    return { valid: false, error: { stage: "bundle", reason: "invalid-schema-or-trust-pins" } };
  }
}
