import { assertBytes, assertHash, exactMembers, sha256Hex } from "./canonical.js";

export interface MerkleProof {
  readonly leaf_index: number;
  readonly tree_size: number;
  /** Bottom-up; orientation derives exclusively from index and size. */
  readonly siblings: readonly string[];
}

function split(size: number): number {
  let power = 1;
  while (power * 2 < size) power *= 2;
  return power;
}

function leafHash(bytes: Uint8Array): string {
  assertBytes(bytes);
  return sha256Hex(Buffer.concat([Buffer.of(0), bytes]));
}

function nodeHash(left: string, right: string): string {
  return sha256Hex(
    Buffer.concat([Buffer.of(1), Buffer.from(left, "hex"), Buffer.from(right, "hex")]),
  );
}

function subtree(leaves: readonly Uint8Array[], start: number, size: number): string {
  if (size === 0) return sha256Hex(new Uint8Array());
  if (size === 1) return leafHash(leaves[start]!);
  const boundary = split(size);
  return nodeHash(
    subtree(leaves, start, boundary),
    subtree(leaves, start + boundary, size - boundary),
  );
}

/** RFC6962 empty/leaf/node domains; no duplicated odd leaves. */
export function merkleRoot(leaves: readonly Uint8Array[]): string {
  if (!Array.isArray(leaves)) throw new TypeError("Byte leaves required");
  return subtree(leaves, 0, leaves.length);
}

export function createInclusionProof(leaves: readonly Uint8Array[], index: number): MerkleProof {
  if (!Array.isArray(leaves)) throw new TypeError("Byte leaves required");
  if (!Number.isSafeInteger(index) || index < 0 || index >= leaves.length)
    throw new RangeError("Leaf index outside tree");
  // Validate every leaf, including a singleton whose path contains no siblings.
  for (const leaf of leaves) assertBytes(leaf);
  const siblings: string[] = [];
  function path(start: number, size: number, selected: number): void {
    if (size === 1) return;
    const boundary = split(size);
    if (selected < boundary) {
      path(start, boundary, selected);
      siblings.push(subtree(leaves, start + boundary, size - boundary));
    } else {
      path(start + boundary, size - boundary, selected - boundary);
      siblings.push(subtree(leaves, start, boundary));
    }
  }
  path(0, leaves.length, index);
  return { leaf_index: index, tree_size: leaves.length, siblings };
}

/** Exact path consumption, including coordinates above32 bits; mismatches return false. */
export function verifyInclusionProof(
  leafBytes: Uint8Array,
  proof: MerkleProof,
  trustedRoot: string,
): boolean {
  try {
    assertBytes(leafBytes);
    assertHash(trustedRoot);
    const raw = exactMembers(proof, ["leaf_index", "tree_size", "siblings"]);
    const index = raw.leaf_index,
      size = raw.tree_size;
    if (
      typeof index !== "number" ||
      typeof size !== "number" ||
      !Number.isSafeInteger(index) ||
      !Number.isSafeInteger(size) ||
      size < 1 ||
      index < 0 ||
      index >= size ||
      !Array.isArray(raw.siblings)
    )
      return false;
    const siblings: unknown[] = raw.siblings;
    // A safe-integer tree has at most53 branch levels. Bound attacker-controlled paths first.
    if (siblings.length > 53) return false;
    for (const sibling of siblings) assertHash(sibling);
    let consumed = 0;
    function climb(selected: number, count: number): string {
      if (count === 1) return leafHash(leafBytes);
      const boundary = split(count);
      const left = selected < boundary;
      const child = climb(
        left ? selected : selected - boundary,
        left ? boundary : count - boundary,
      );
      const sibling = siblings[consumed++];
      assertHash(sibling);
      return left ? nodeHash(child, sibling) : nodeHash(sibling, child);
    }
    const root = climb(index, size);
    return consumed === siblings.length && root === trustedRoot;
  } catch {
    return false;
  }
}
