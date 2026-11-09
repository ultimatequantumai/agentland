import { createHash } from "node:crypto";
import { assertBytes, canonicalize, decodeBase64url as decodeBase64urlBytes } from "./json.js";

// The node-free primitives live in json.ts (the browser verifier imports them); every existing
// `./canonical.js` import keeps working through these re-exports.
export {
  assertBytes,
  assertHash,
  assertTimestamp,
  canonicalize,
  exactMembers,
  objectRecord,
  parseIJson,
} from "./json.js";
export type { JsonValue } from "./json.js";

export function canonicalBytes(value: unknown): Uint8Array {
  return Buffer.from(canonicalize(value), "utf8");
}

export function sha256Hex(bytes: Uint8Array): string {
  assertBytes(bytes);
  return createHash("sha256").update(bytes).digest("hex");
}

/** Buffer view for Node-side callers (proof.ts compares it as hex); the rules live in json.ts. */
export function decodeBase64url(value: unknown, length?: number): Buffer {
  const bytes = decodeBase64urlBytes(value, length);
  return Buffer.from(bytes.buffer, bytes.byteOffset, bytes.byteLength);
}
