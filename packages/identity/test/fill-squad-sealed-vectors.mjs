// Fills every derived field of squad-sealed-vectors.json from the built @agentland/identity.
// Never edit the vectors by hand; change the inputs and re-run.
// Usage: node packages/identity/test/fill-squad-sealed-vectors.mjs [--check]
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { TextDecoder, TextEncoder } from "node:util";
import * as identity from "../dist/index.js";
// Deterministic-randomness seams: module-only, never in the barrel (vectors and tests only).
import { sealSquadEntryWithRandomness, wrapEpochKeyWithRandomness } from "../dist/squad-sealed.js";

const args = process.argv.slice(2);
if (args.length > 1 || (args.length === 1 && args[0] !== "--check")) process.exit(2);
const check = args[0] === "--check";
const path = new URL("./squad-sealed-vectors.json", import.meta.url);
const original = readFileSync(path, "utf8");
const doc = JSON.parse(original);
// Read-only: seeds, DIDs and signing records of the agentland-squad/1 vectors.
const squad = JSON.parse(readFileSync(new URL("./squad-vectors.json", import.meta.url), "utf8"));

const PKCS8_PREFIX = "302e020100300506032b657004220420";
const bytes = (hex) => new Uint8Array(Buffer.from(hex, "hex"));
const hexOf = (raw) => Buffer.from(raw).toString("hex");
const b64url = (raw) => Buffer.from(raw).toString("base64url");
const utf8 = (text) => new TextEncoder().encode(text);
const sha256 = (data) => new Uint8Array(createHash("sha256").update(data).digest());
const seeds = new Map(squad.keys.map((k) => [k.label, k]));
const pkcs8 = (label) => bytes(PKCS8_PREFIX + seeds.get(label).seed_hex);
const agent = (label) => squad.agents.find((a) => a.label === label);
const encKey = (label) => doc.enc_keys.find((k) => k.label === label);
const encPublic = (label) => identity.encryptionPublicKey(bytes(encKey(label).secret_hex));

// enc_keys
for (const key of doc.enc_keys) {
  const publicKey = identity.encryptionPublicKey(bytes(key.secret_hex));
  key.public_hex = hexOf(publicKey);
  key.kid = identity.recipientKeyId(publicKey);
}

// envelope (RESEARCH F2.3)
const e = doc.envelope;
e.aad_utf8 = new TextDecoder().decode(
  identity.squadSealedAad({ squadId: e.squad_id, key: e.key, epoch: e.epoch }),
);
e.envelope_hex = hexOf(
  sealSquadEntryWithRandomness(
    {
      epochKey: bytes(e.epoch_key_hex),
      epoch: e.epoch,
      squadId: e.squad_id,
      key: e.key,
      meta: e.meta,
      body: utf8(e.body_utf8),
    },
    { nonce: bytes(e.nonce_hex) },
  ),
);

// wrap (RFC 7748 §6.1 Bob as recipient, Alice as ephemeral)
const w = doc.wrap;
const wrapped = wrapEpochKeyWithRandomness(
  {
    recipient: bytes(w.recipient_public_hex),
    did: w.did,
    squadId: w.squad_id,
    epoch: w.epoch,
    epochKey: bytes(w.epoch_key_hex),
  },
  { ephemeralSecretKey: bytes(w.ephemeral_secret_hex), nonce: bytes(w.nonce_hex) },
);
w.kid = wrapped.kid;
w.envelope_b64url = wrapped.envelope;
w.envelope_sha256 = hexOf(sha256(Buffer.from(wrapped.envelope, "base64url")));

// histories: the /did/history DTO with one self-custody agentland-enc-key/1 register
for (const h of doc.histories) {
  const signing = agent(h.label).keys.map((k) => ({
    id: k.id,
    publicKeyJwk: { kty: "OKP", crv: "Ed25519", x: seeds.get(k.key).public_x },
    purpose: "signing",
    activated_at: k.activated_at,
    ...(k.revoked_at === undefined ? {} : { revoked_at: k.revoked_at }),
  }));
  const x = b64url(encPublic(h.label));
  const statement = {
    did: h.did,
    kind: "enc_key",
    previous: null,
    public_key: x,
    ts: h.register_ts,
  };
  h.value = {
    did: h.did,
    keys: [
      ...signing,
      {
        id: h.enc_key_id,
        publicKeyJwk: { kty: "OKP", crv: "X25519", x },
        purpose: "encryption",
        activated_at: h.register_ts,
      },
    ],
    rotations: [],
    enc_keys: [
      {
        statement,
        signature: identity.signEd25519(
          identity.encKeyStatementBytes(statement),
          pkcs8(h.sign_with),
        ),
        signing_key_id: h.signing_key_id,
        custody: "self",
      },
    ],
    recovery_notice: null,
  };
}

const didOf = (label) => doc.histories.find((h) => h.label === label).did;
const epochKey = (name, n) => sha256(utf8(`${name}/epoch/${n}`));
const compare = (a, b) => (a.kid < b.kid ? -1 : a.kid > b.kid ? 1 : 0);

function content(scenario, step, i) {
  const name = scenario.name;
  if (step.statement) {
    const statement = { squad_id: scenario.squad_id, ts: step.ts_server, ...step.statement };
    if (statement.kind === "epoch")
      statement.wraps = step.wrap_to
        .map((label) =>
          wrapEpochKeyWithRandomness(
            {
              recipient: encPublic(label),
              did: didOf(label),
              squadId: scenario.squad_id,
              epoch: statement.epoch,
              epochKey: epochKey(name, statement.epoch),
            },
            {
              ephemeralSecretKey: sha256(utf8(`${name}/${i}/${label}/ephemeral`)),
              nonce: sha256(utf8(`${name}/${i}/${label}/nonce`)).slice(0, 24),
            },
          ),
        )
        .sort(compare);
    return identity.squadStatementBytes(statement);
  }
  const sealed = sealSquadEntryWithRandomness(
    {
      epochKey: epochKey(name, step.sealed.epoch),
      epoch: step.sealed.epoch,
      squadId: scenario.squad_id,
      key: step.key,
      meta: step.sealed.meta,
      body: utf8(step.sealed.body_utf8),
    },
    { nonce: sha256(utf8(`${name}/${i}/nonce`)).slice(0, 24) },
  );
  const append = bytes(step.tamper?.payload_append_hex ?? "");
  const out = new Uint8Array(sealed.length + append.length);
  out.set(sealed);
  out.set(append, sealed.length);
  return out;
}

function fillScenario(scenario) {
  const entries = [];
  const statements = [];
  const payloads = [];
  let prevHash = identity.squadGenesis(scenario.squad_id);
  scenario.steps.forEach((step, index) => {
    const i = index + 1;
    const raw = content(scenario, step, i);
    const signer = agent(step.signer).did;
    const intent = identity.createSquadPutIntent({
      seq: String(i),
      key: step.key,
      content: raw,
      prev_hash: prevHash,
      squad_id: scenario.squad_id,
      signer,
      signing_key_id: step.key_id ?? `${signer}#key-1`,
      content_type:
        step.content_type ??
        (step.statement
          ? identity.SQUAD_STATEMENT_CONTENT_TYPE
          : identity.SQUAD_SEALED_CONTENT_TYPE),
      tags: [],
    });
    const sig = identity.signSquadIntent(intent, pkcs8(step.sign_with));
    const entry = { ...intent, ts_server: step.ts_server, sig };
    entries.push(entry);
    prevHash = identity.hashSquadEntry(entry);
    const row = { seq: String(i), content_b64url: b64url(raw) };
    if (step.key.startsWith(identity.SQUAD_STATEMENT_PREFIX)) statements.push(row);
    else if (step.key.startsWith("sealed/")) payloads.push(row);
  });
  scenario.entries = entries;
  scenario.statements = statements;
  scenario.payloads = payloads;
  scenario.head = { seq: entries.at(-1).seq, head_hash: prevHash };
}

doc.scenarios.forEach(fillScenario);

const output = identity.canonicalize(doc);
if (check) {
  if (output !== original) {
    console.error("squad-sealed-vectors.json differs from the fill; re-run without --check");
    process.exit(1);
  }
} else writeFileSync(path, output);
