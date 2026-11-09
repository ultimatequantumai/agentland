import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { afterAll, describe, expect, it } from "vitest";
import {
  canonicalBytes,
  createInclusionProof,
  createPutIntent,
  hashVaultEntry,
  merkleRoot,
  sha256Hex,
  signVaultIntent,
  stampVaultEntry,
} from "../src/index.js";
import type { VaultProofBundle } from "../src/index.js";
import fixture from "./fixtures/vault-three.json" with { type: "json" };
import publicKeys from "./fixtures/public-keys.json" with { type: "json" };
import { fixtureDailyRoot, fixtureHead, fixtureRoot } from "./fixtures/oracle.js";
import { testKey } from "./helpers.js";

const root = fileURLToPath(new URL("../../../", import.meta.url));
// Each case spawns the real verifier CLI once per mutation; under the full parallel suite a
// matrix has taken 53 s. The assertions are on outcomes, so the bound is suite scale.
const CLI_TIMEOUT = 180_000;
const directory = mkdtempSync(join(tmpdir(), "agentland-identity-"));
const denyNetwork = join(directory, "deny-network.cjs");
writeFileSync(
  denyNetwork,
  `const deny = () => { throw new Error('network denied in offline verifier test'); };
const net = require('node:net'); net.connect = deny; net.createConnection = deny; net.Socket.prototype.connect = deny;
require('node:tls').connect = deny;
for (const name of ['node:http', 'node:https']) { const mod = require(name); mod.request = deny; mod.get = deny; }
globalThis.fetch = deny; globalThis.WebSocket = class { constructor() { deny(); } };
`,
);
afterAll(() => rmSync(directory, { recursive: true, force: true }));
const cli = join(root, "scripts/verify-vault.ts");
const keysPath = join(directory, "public-keys.json");
writeFileSync(keysPath, JSON.stringify(publicKeys));
let fileCounter = 0;
function runBundle(
  bundle: unknown,
  extra: {
    root?: string;
    headHash?: string;
    headSeq?: string;
    keys?: unknown;
    stdin?: boolean;
    raw?: string;
  } = {},
) {
  const path = join(directory, `bundle-${fileCounter++}.json`);
  const contents = extra.raw ?? JSON.stringify(bundle);
  if (!extra.stdin) writeFileSync(path, contents);
  const keyFile =
    extra.keys === undefined ? keysPath : join(directory, `keys-${fileCounter++}.json`);
  if (extra.keys !== undefined) writeFileSync(keyFile, JSON.stringify(extra.keys));
  const args = [
    "--bundle",
    extra.stdin ? "-" : path,
    "--keys",
    keyFile,
    "--root",
    extra.root ?? fixtureDailyRoot,
    "--head-seq",
    extra.headSeq ?? "3",
    "--head-hash",
    extra.headHash ?? fixtureHead,
  ];
  return spawnSync(process.execPath, ["--require", denyNetwork, "--import", "tsx", cli, ...args], {
    cwd: root,
    encoding: "utf8",
    input: extra.stdin ? contents : undefined,
    timeout: 15_000,
  });
}

describe("actual no-server file/stdin verifier CLI", () => {
  it("returns exact externally pinned three-entry/second-proof success for file and stdin", () => {
    for (const stdin of [false, true]) {
      const result = runBundle(fixture, { stdin });
      expect(result.error).toBeUndefined();
      expect(result.status).toBe(0);
      expect(result.stderr).toBe("");
      expect(JSON.parse(result.stdout)).toEqual({
        valid: true,
        did: fixture.did,
        entries: 3,
        head_seq: "3",
        head_hash: fixtureHead,
        proved_seq: "2",
        root: fixtureDailyRoot,
      });
    }
  });
  it(
    "verifies a later UTC day's first entry and rejects cumulative or partial authority",
    () => {
      const signer = testKey();
      let previous = sha256Hex(Buffer.from(fixture.did));
      const entries = [
        "2026-01-01T23:59:59.998Z",
        "2026-01-01T23:59:59.999Z",
        "2026-01-02T00:00:00.000Z",
        "2026-01-02T00:00:00.001Z",
      ].map((ts_server, index) => {
        const intent = createPutIntent({
          seq: String(index + 1),
          key: "vault/daily",
          content: Buffer.from(`daily-memory-${index}`),
          prev_hash: previous,
        });
        const entry = stampVaultEntry(
          { intent, sig_agent: signVaultIntent(intent, signer.privatePkcs8), ts_server },
          signer.publicKeyJwk,
        );
        previous = hashVaultEntry(entry);
        return entry;
      });
      const leaves = entries.slice(2).map(canonicalBytes);
      const publishedRoot = merkleRoot(leaves);
      const bundle: VaultProofBundle = {
        format: "agentland-vault/1",
        did: fixture.did,
        entries,
        proof: { seq: "3", ...createInclusionProof(leaves, 0) },
      };
      const pins = { root: publishedRoot, headSeq: "4", headHash: previous };
      expect(bundle.proof.leaf_index).toBe(0);
      expect(bundle.proof.tree_size).toBe(2);
      for (const stdin of [false, true]) {
        const result = runBundle(bundle, { ...pins, stdin });
        expect(result.error).toBeUndefined();
        expect(result.status).toBe(0);
        expect(result.stderr).toBe("");
        expect(JSON.parse(result.stdout)).toEqual({
          valid: true,
          did: fixture.did,
          entries: 4,
          head_seq: "4",
          head_hash: previous,
          proved_seq: "3",
          root: publishedRoot,
        });
      }
      for (const siblings of [
        bundle.proof.siblings.slice(1),
        [...bundle.proof.siblings, "0".repeat(64)],
      ]) {
        const result = runBundle({ ...bundle, proof: { ...bundle.proof, siblings } }, pins);
        expect(result.status).toBe(1);
        expect(JSON.parse(result.stdout)).toEqual({
          valid: false,
          error: { stage: "proof", reason: "invalid-entry-path" },
        });
      }
      for (const cumulative of [
        entries.slice(0, 3).map(canonicalBytes),
        entries.map(canonicalBytes),
      ]) {
        const result = runBundle(
          { ...bundle, proof: { seq: "3", ...createInclusionProof(cumulative, 2) } },
          { ...pins, root: merkleRoot(cumulative) },
        );
        expect(result.status).toBe(1);
        expect(JSON.parse(result.stdout).valid).toBe(false);
      }
      const wrongDay = runBundle(bundle, {
        ...pins,
        root: merkleRoot(entries.slice(0, 2).map(canonicalBytes)),
      });
      expect(wrongDay.status).toBe(1);
      expect(JSON.parse(wrongDay.stdout).valid).toBe(false);
      const partialDay = leaves.slice(0, 1);
      const incomplete = runBundle(
        { ...bundle, proof: { seq: "3", ...createInclusionProof(partialDay, 0) } },
        { ...pins, root: merkleRoot(partialDay) },
      );
      expect(incomplete.status).toBe(1);
      expect(JSON.parse(incomplete.stdout).valid).toBe(false);
      const altered = [...entries];
      altered[0] = { ...altered[0]!, ts_server: "2026-01-01T23:59:59.997Z" };
      expect(altered.slice(2).map(canonicalBytes)).toEqual(leaves);
      const earlierChain = runBundle({ ...bundle, entries: altered }, pins);
      expect(earlierChain.status).toBe(1);
      expect(JSON.parse(earlierChain.stdout)).toEqual({
        valid: false,
        error: { stage: "chain", reason: "broken-hash-link", index: 1 },
      });
    },
    CLI_TIMEOUT,
  );
  it(
    "rejects byte/stamp/key/root/head/order/truncation and every path attack",
    () => {
      const mutations: unknown[] = [];
      const changedContent = structuredClone(fixture);
      changedContent.entries[0]!.content_hash = "0".repeat(64);
      mutations.push(changedContent);
      const changedStamp = structuredClone(fixture);
      changedStamp.entries[2]!.ts_server = "2026-01-03T00:00:00.001Z";
      mutations.push(changedStamp);
      mutations.push(
        { ...fixture, entries: fixture.entries.slice(0, 2) },
        { ...fixture, entries: [...fixture.entries].reverse() },
      );
      for (const patch of [
        { leaf_index: 1 },
        { leaf_index: 3 },
        { leaf_index: -1 },
        { leaf_index: 0.5 },
        { tree_size: 0 },
        { tree_size: 2 },
        { tree_size: Number.MAX_SAFE_INTEGER + 1 },
        { seq: "1" },
        { siblings: ["0".repeat(64)] },
        { siblings: ["0"] },
        { siblings: ["0".repeat(64), "0".repeat(64)] },
        { siblings: ["malformed"] },
      ])
        mutations.push({ ...fixture, proof: { ...fixture.proof, ...patch } });
      for (const bundle of mutations) {
        const result = runBundle(bundle);
        expect(result.status).toBe(1);
        expect(JSON.parse(result.stdout).valid).toBe(false);
        expect(result.stdout).not.toContain("First memory");
      }
      for (const options of [
        { keys: [{ from_seq: "1", publicKeyJwk: testKey(1).publicKeyJwk }] },
        {
          keys: [
            {
              ...publicKeys[0]!,
              publicKeyJwk: { ...publicKeys[0]!.publicKeyJwk, d: "secret-sentinel" },
            },
          ],
        },
        { root: "0".repeat(64) },
        { headHash: "0".repeat(64) },
        { headSeq: "2" },
      ]) {
        const result = runBundle(fixture, options);
        expect(result.status).toBe(1);
        expect(JSON.parse(result.stdout).valid).toBe(false);
        expect(result.stdout + result.stderr).not.toContain("secret-sentinel");
      }
    },
    CLI_TIMEOUT,
  );
  it("verifies optional outer root composition and rejects changed root bytes", () => {
    const leaves = [Buffer.from(fixtureDailyRoot, "hex"), Buffer.from("other")];
    const audit = {
      vault_root_leaf_bytes: leaves[0]!.toString("base64url"),
      proof: createInclusionProof(leaves, 0),
    };
    const publishedRoot = merkleRoot(leaves);
    const success = runBundle({ ...fixture, audit }, { root: publishedRoot });
    expect(success.status).toBe(0);
    expect(JSON.parse(success.stdout).root).toBe(publishedRoot);
    const altered = { ...audit, vault_root_leaf_bytes: Buffer.alloc(32).toString("base64url") };
    expect(runBundle({ ...fixture, audit: altered }, { root: publishedRoot }).status).toBe(1);
  });
  it(
    "distinguishes invalid JSON/schema from usage and I/O failures",
    () => {
      for (const raw of ['{"format":"a","format":"b"}', '{"entries":[}', "null"])
        expect(runBundle(null, { raw }).status).toBe(1);
      for (const args of [
        [],
        ["--bundle", "x"],
        ["--private-key", "secret-sentinel"],
        ["--bundle", "x", "--bundle", "y"],
        ["--bundle"],
      ]) {
        const result = spawnSync(
          process.execPath,
          ["--require", denyNetwork, "--import", "tsx", cli, ...args],
          { cwd: root, encoding: "utf8", timeout: 15_000 },
        );
        expect(result.status).toBe(2);
        expect(result.stderr).toContain("Usage:");
        expect(result.stderr).not.toContain("secret-sentinel");
      }
      const absent = spawnSync(
        process.execPath,
        [
          "--require",
          denyNetwork,
          "--import",
          "tsx",
          cli,
          "--bundle",
          join(directory, "absent"),
          "--keys",
          keysPath,
          "--root",
          fixtureDailyRoot,
          "--head-seq",
          "3",
          "--head-hash",
          fixtureHead,
        ],
        { cwd: root, encoding: "utf8", timeout: 15_000 },
      );
      expect(absent.status).toBe(2);
      expect(absent.stderr).toContain("Unable to read");
      expect(runBundle(fixture, { root: "bad" }).status).toBe(2);
      expect(runBundle(fixture, { headSeq: "03" }).status).toBe(2);
    },
    CLI_TIMEOUT,
  );
});

describe("plain Node emitted-package consumer", () => {
  it("imports actual exports and performs independent signature/chain/proof operations without tsx", () => {
    const program = `import assert from 'node:assert/strict';
import { createPrivateKey } from 'node:crypto';
import { canonicalBytes, signEd25519, verifyEd25519, validateVaultChain, verifyVaultBundle, merkleRoot } from '@agentland/identity';
const bundle = ${JSON.stringify(fixture)};
const keys = ${JSON.stringify(publicKeys)};
const head = {seq:'3',head_hash:'${fixtureHead}'};
const key = keys[0].publicKeyJwk;
const secret = createPrivateKey({format:'jwk',key:{...key,d:Buffer.from('${testKey().vector.seed}','hex').toString('base64url')}}).export({format:'der',type:'pkcs8'});
const sig = signEd25519(Buffer.alloc(0),secret);
assert.equal(sig,Buffer.from('${testKey().vector.signature}','hex').toString('base64url'));
assert.equal(verifyEd25519(Buffer.alloc(0),sig,key),true);
assert.equal(validateVaultChain({did:bundle.did,entries:bundle.entries,keys,expectedHead:head}).head_hash,'${fixtureHead}');
assert.equal(merkleRoot(bundle.entries.map(canonicalBytes)),'${fixtureRoot}');
assert.equal(verifyVaultBundle(bundle,{keys,expectedHead:head,publishedRoot:'${fixtureDailyRoot}'}).proved_seq,'2');
console.log(JSON.stringify({valid:true,entries:3,proved_seq:'2'}));`;
    const result = spawnSync(
      process.execPath,
      ["--require", denyNetwork, "--input-type=module", "--eval", program],
      { cwd: join(root, "packages/identity"), encoding: "utf8", timeout: 15_000 },
    );
    expect(result.error).toBeUndefined();
    expect(result.status).toBe(0);
    expect(result.stderr).toBe("");
    expect(JSON.parse(result.stdout)).toEqual({ valid: true, entries: 3, proved_seq: "2" });
  });
});
