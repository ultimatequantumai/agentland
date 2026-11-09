/** Independent agentland-squad/1 oracle: sorted-key JSON and node:crypto only, never ../../src.
 * Recomputes every derived field of an untampered scenario so a drifting fill cannot pass.
 */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { Buffer } from "node:buffer";
import { createHash, createPrivateKey, createPublicKey, sign } from "node:crypto";

type Json = any;
const PKCS8_PREFIX = "302e020100300506032b657004220420";
const PREFIX = "agentland-squad/1\n";

/** RFC 8785 for the vector domain: strings, integers, arrays, objects and null. */
export function jcs(value: Json): string {
  if (value === null || typeof value !== "object") return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(jcs).join(",")}]`;
  const names = Object.keys(value).filter((name) => value[name] !== undefined);
  names.sort();
  return `{${names.map((name) => `${JSON.stringify(name)}:${jcs(value[name])}`).join(",")}}`;
}

const sha256 = (bytes: Uint8Array | string) => createHash("sha256").update(bytes).digest("hex");

export function oracleKey(seedHex: string) {
  const privateKey = createPrivateKey({
    key: Buffer.from(PKCS8_PREFIX + seedHex, "hex"),
    format: "der",
    type: "pkcs8",
  });
  const x = createPublicKey(privateKey).export({ format: "jwk" }).x as string;
  return { privateKey, x };
}

export function oracleScenario(file: Json, scenario: Json) {
  const seeds = new Map<string, string>(file.keys.map((k: Json) => [k.label, k.seed_hex]));
  let previous = sha256(PREFIX + scenario.squad_id);
  const entries: Json[] = [];
  const statements: Json[] = [];
  scenario.steps.forEach((step: Json, index: number) => {
    const seq = String(index + 1);
    const isStatement = step.statement !== undefined;
    const content = isStatement
      ? Buffer.from(
          jcs({ squad_id: scenario.squad_id, ts: step.ts_server, ...step.statement }),
          "utf8",
        )
      : Buffer.from(step.content_utf8 ?? "", "utf8");
    const del = step.op === "delete";
    const contentHash = del ? sha256(new Uint8Array()) : sha256(content);
    const intent = {
      seq,
      key: step.key,
      op: step.op,
      content_hash: contentHash,
      content_ref: del ? null : `sha256:${contentHash}`,
      content_type: del
        ? "application/octet-stream"
        : (step.content_type ?? (isStatement ? "application/json" : "text/plain; charset=utf-8")),
      tags: [] as string[],
      prev_hash: previous,
      squad_id: scenario.squad_id,
      signer:
        step.signer === "platform"
          ? "did:web:agentland.us"
          : file.agents.find((agent: Json) => agent.label === step.signer).did,
      signing_key_id: step.key_id,
    };
    const { privateKey } = oracleKey(seeds.get(step.sign_with)!);
    const sig = sign(null, Buffer.from(PREFIX + jcs(intent), "utf8"), privateKey).toString(
      "base64url",
    );
    const entry = { ...intent, ts_server: step.ts_server, sig };
    previous = sha256(jcs(entry));
    entries.push(entry);
    if (!del && step.key.startsWith("public/.squad/"))
      statements.push({ seq, content_b64url: content.toString("base64url") });
  });
  return { entries, statements, head: { seq: String(entries.length), head_hash: previous } };
}
