// Fills every derived field of squad-vectors.json from the built @agentland/identity.
// Never edit the vectors by hand; change the inputs and re-run.
// Usage: node packages/identity/test/fill-squad-vectors.mjs [--check]
import { createPrivateKey, createPublicKey } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { TextEncoder } from "node:util";
import * as identity from "../dist/index.js";

const args = process.argv.slice(2);
if (args.length > 1 || (args.length === 1 && args[0] !== "--check")) process.exit(2);
const check = args[0] === "--check";
const path = new URL("./squad-vectors.json", import.meta.url);
const original = readFileSync(path, "utf8");
const doc = JSON.parse(original);

const PKCS8_PREFIX = "302e020100300506032b657004220420";
const utf8 = (text) => new TextEncoder().encode(text);
const seeds = new Map(doc.keys.map((k) => [k.label, k.seed_hex]));
const pkcs8 = (label) => new Uint8Array(Buffer.from(PKCS8_PREFIX + seeds.get(label), "hex"));
const publicX = (label) =>
  createPublicKey(
    createPrivateKey({ key: Buffer.from(pkcs8(label)), format: "der", type: "pkcs8" }),
  ).export({ format: "jwk" }).x;
const didOf = (label) =>
  label === "platform"
    ? identity.SQUAD_PLATFORM_DID
    : doc.agents.find((a) => a.label === label).did;

for (const key of doc.keys) key.public_x = publicX(key.label);
doc.platform.public_x = publicX(doc.platform.key);

function buildIntent(scenario, step, seq, prevHash, content) {
  const tamper = step.tamper ?? {};
  const common = {
    seq,
    key: step.key,
    prev_hash: prevHash,
    squad_id: tamper.squad_id ?? scenario.squad_id,
    signer: didOf(step.signer),
    signing_key_id: step.key_id,
  };
  if (step.op === "delete") return identity.createSquadDeleteIntent(common);
  const contentType = step.content_type ?? (step.statement ? "application/json" : undefined);
  return identity.createSquadPutIntent({
    ...common,
    content:
      tamper.content_hash_of_utf8 === undefined ? content : utf8(tamper.content_hash_of_utf8),
    ...(contentType === undefined ? {} : { content_type: contentType }),
  });
}

function message(intent, sign) {
  if (sign === "unprefixed") return identity.canonicalBytes(intent);
  if (sign === "vault-intent") {
    const vault = { ...intent };
    delete vault.squad_id;
    delete vault.signer;
    delete vault.signing_key_id;
    return identity.canonicalBytes(vault);
  }
  return identity.squadSigningMessage(intent);
}

function fillScenario(scenario) {
  const genesis = identity.squadGenesis(scenario.squad_id);
  const entries = [];
  const hashes = [];
  const statements = [];
  scenario.steps.forEach((step, index) => {
    const tamper = step.tamper ?? {};
    const content = step.statement
      ? identity.squadStatementBytes({
          squad_id: scenario.squad_id,
          ts: step.ts_server,
          ...step.statement,
        })
      : utf8(step.content_utf8 ?? "");
    const seq = tamper.seq ?? String(index + 1);
    const prevHash =
      tamper.prev_hash ??
      (tamper.prev_seq === undefined
        ? (hashes[index - 1] ?? genesis)
        : tamper.prev_seq === "0"
          ? genesis
          : hashes[Number(tamper.prev_seq) - 1]);
    const intent = buildIntent(scenario, step, seq, prevHash, content);
    const sig = identity.signEd25519(message(intent, tamper.sign), pkcs8(step.sign_with));
    const entry = { ...intent, ts_server: step.ts_server, sig, ...(tamper.after ?? {}) };
    entries.push(entry);
    hashes.push(identity.sha256Hex(identity.canonicalBytes(entry)));
    if (
      step.op === "put" &&
      step.key.startsWith(identity.SQUAD_STATEMENT_PREFIX) &&
      !tamper.omit_payload
    )
      // Payload pins carry the step's position, not a tampered seq: a stale seq is a chain
      // fault of the entry (b.1.4 stage 1), never a duplicate pin.
      statements.push({
        seq: String(index + 1),
        content_b64url: Buffer.from(content).toString("base64url"),
      });
  });
  scenario.entries = entries;
  scenario.statements = statements;
  scenario.head = { seq: entries.at(-1).seq, head_hash: hashes.at(-1) };
}

doc.scenarios.forEach(fillScenario);

const headScenario = doc.scenarios.find((s) => s.name === doc.head.scenario);
doc.head.value = identity.signSquadHead(
  { squad_id: headScenario.squad_id, ...headScenario.head, ts: doc.head.ts, kid: doc.platform.kid },
  pkcs8(doc.platform.key),
);

const bundleScenario = doc.scenarios.find((s) => s.name === doc.bundle.scenario);
const proved = bundleScenario.entries.find((e) => e.seq === doc.bundle.seq);
const squadRoot = identity.squadDayRoot(bundleScenario.entries, proved.ts_server.slice(0, 10));
const auditLeaves = doc.bundle.audit_leaves_hex.map(
  (hex) => new Uint8Array(Buffer.from(hex, "hex")),
);
auditLeaves.splice(doc.bundle.squad_leaf_index, 0, new Uint8Array(Buffer.from(squadRoot, "hex")));
doc.bundle.published_root = identity.merkleRoot(auditLeaves);
doc.bundle.value = identity.buildSquadProofBundle({
  squadId: bundleScenario.squad_id,
  entries: bundleScenario.entries,
  statements: bundleScenario.statements.map((s) => ({
    seq: s.seq,
    content: new Uint8Array(Buffer.from(s.content_b64url, "base64url")),
  })),
  seq: doc.bundle.seq,
  auditLeaves,
  squadLeafIndex: doc.bundle.squad_leaf_index,
});

const output = identity.canonicalize(doc);
if (check) {
  if (output !== original) {
    console.error("squad-vectors.json differs from the fill; re-run without --check");
    process.exit(1);
  }
} else writeFileSync(path, output);
