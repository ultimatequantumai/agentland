import { randomBytes } from "node:crypto";
import { describe, expect, it } from "vitest";
import {
  buildVaultProofBundle,
  createInclusionProof,
  merkleRoot,
  verifyVaultBundle,
} from "../src/index.js";
import type { VaultEntry, VaultProofBundle, VaultSigningKey } from "../src/index.js";
import fixture from "./fixtures/vault-three.json" with { type: "json" };
import { fixtureDailyRoot, fixtureHead } from "./fixtures/oracle.js";
import { did, testKey } from "./helpers.js";

const key = testKey();
const keys: VaultSigningKey[] = [{ from_seq: "1", publicKeyJwk: key.publicKeyJwk }];
const chain = fixture.entries as unknown as VaultEntry[];
const expectedHead = { seq: "3", head_hash: fixtureHead };
const head32 = randomBytes(32);
const other32 = randomBytes(32);
const auditLeaves = [head32, Buffer.from(fixtureDailyRoot, "hex"), other32];
const publishedRoot = merkleRoot(auditLeaves);
const build = (overrides: Partial<Parameters<typeof buildVaultProofBundle>[0]> = {}) =>
  buildVaultProofBundle({ did, chain, seq: "2", auditLeaves, vaultLeafIndex: 1, ...overrides });

describe("buildVaultProofBundle", () => {
  it("composes the entry path and the outer path to the published audit root", () => {
    const bundle = build();
    const expected = fixture as unknown as VaultProofBundle;
    expect(bundle).toEqual({
      format: "agentland-vault/1",
      did,
      entries: chain,
      proof: expected.proof,
      audit: {
        vault_root_leaf_bytes: Buffer.from(fixtureDailyRoot, "hex").toString("base64url"),
        proof: createInclusionProof(auditLeaves, 1),
      },
    });
    expect(verifyVaultBundle(bundle, { keys, expectedHead, publishedRoot })).toMatchObject({
      valid: true,
      proved_seq: "2",
      root: publishedRoot,
    });
    for (const wrong of [fixtureDailyRoot, randomBytes(32).toString("hex")])
      expect(verifyVaultBundle(bundle, { keys, expectedHead, publishedRoot: wrong })).toEqual({
        valid: false,
        error: { stage: "audit", reason: "root-leaf-or-path-mismatch" },
      });
  });

  it("refuses the audit head index, out-of-range indexes, absent seqs and non-32-byte leaves", () => {
    for (const vaultLeafIndex of [0, 3, -1, 1.5])
      expect(() => build({ vaultLeafIndex })).toThrow(RangeError);
    expect(() => build({ seq: "9" })).toThrow(RangeError);
    expect(() => build({ auditLeaves: [head32, Buffer.alloc(31), other32] })).toThrow(TypeError);
  });

  it("does not compare the chain with the leaves: the verifier is the authority", () => {
    const leaves = [head32, randomBytes(32), other32];
    const bundle = build({ auditLeaves: leaves });
    expect(
      verifyVaultBundle(bundle, { keys, expectedHead, publishedRoot: merkleRoot(leaves) }),
    ).toEqual({ valid: false, error: { stage: "audit", reason: "root-leaf-or-path-mismatch" } });
  });
});
