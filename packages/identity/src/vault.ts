import {
  assertBytes,
  assertHash,
  assertTimestamp,
  canonicalBytes,
  canonicalize,
  decodeBase64url,
  exactMembers,
  sha256Hex,
} from "./canonical.js";
import { assertAgentDid } from "./did.js";
import { signEd25519, validatePublicJwk, verifyEd25519 } from "./keys.js";
import type { Ed25519PublicJwk } from "./keys.js";

export interface VaultIntent {
  readonly seq: string;
  readonly key: string;
  readonly op: "put" | "delete";
  readonly content_hash: string;
  readonly content_ref: string | null;
  readonly content_type: string;
  readonly tags: readonly string[];
  readonly prev_hash: string;
}
export interface VaultEntry extends VaultIntent {
  readonly ts_server: string;
  readonly sig_agent: string;
}
export interface VaultHead {
  readonly seq: string;
  readonly head_hash: string;
}
export interface VaultSigningKey {
  readonly from_seq: string;
  readonly through_seq?: string;
  readonly publicKeyJwk: Ed25519PublicJwk;
}
export interface VerificationFailure {
  readonly valid: false;
  readonly error: { readonly stage: string; readonly reason: string; readonly index?: number };
}
export interface VaultChainSuccess {
  readonly valid: true;
  readonly did: string;
  readonly entries: number;
  readonly head_seq: string;
  readonly head_hash: string;
}
export type VaultChainResult = VaultChainSuccess | VerificationFailure;

export const INTENT_FIELDS = [
  "seq",
  "key",
  "op",
  "content_hash",
  "content_ref",
  "content_type",
  "tags",
  "prev_hash",
] as const;
const EMPTY_HASH = sha256Hex(new Uint8Array());

export function assertSequence(value: unknown, allowEmpty = false): asserts value is string {
  if (
    typeof value !== "string" ||
    !(allowEmpty ? /^(?:0|[1-9][0-9]*)$/ : /^[1-9][0-9]*$/).test(value)
  )
    throw new TypeError("Canonical decimal sequence required");
}

export function validateIntent(value: unknown): asserts value is VaultIntent {
  const intent = exactMembers(value, INTENT_FIELDS);
  canonicalize(intent);
  assertSequence(intent.seq);
  assertHash(intent.content_hash);
  assertHash(intent.prev_hash);
  if (typeof intent.key !== "string" || !/^(?:public|vault|sealed)\/.+$/u.test(intent.key))
    throw new TypeError("Vault namespace and nonempty key required");
  if (
    typeof intent.content_type !== "string" ||
    intent.content_type.length === 0 ||
    !Array.isArray(intent.tags) ||
    !intent.tags.every((tag: unknown) => typeof tag === "string")
  )
    throw new TypeError("Exact vault metadata required");
  if (intent.op === "put") {
    if (intent.content_ref !== `sha256:${intent.content_hash}`)
      throw new TypeError("Content reference mismatch");
  } else if (intent.op === "delete") {
    if (
      intent.content_hash !== EMPTY_HASH ||
      intent.content_ref !== null ||
      intent.content_type !== "application/octet-stream" ||
      intent.tags.length !== 0
    )
      throw new TypeError("Invalid tombstone commitment");
  } else throw new TypeError("Unknown vault operation");
}

/** Only unsigned constructor inputs receive defaults. Content bytes include opaque sealed ciphertext. */
export function createPutIntent(input: {
  readonly seq: string;
  readonly key: string;
  readonly content: Uint8Array;
  readonly prev_hash: string;
  readonly content_type?: string;
  readonly tags?: readonly string[];
}): VaultIntent {
  exactMembers(input, ["seq", "key", "content", "prev_hash"], ["content_type", "tags"]);
  if (input.tags !== undefined && !Array.isArray(input.tags))
    throw new TypeError("Tag array required");
  assertBytes(input.content);
  const content_hash = sha256Hex(input.content);
  const intent: VaultIntent = {
    seq: input.seq,
    key: input.key,
    op: "put",
    content_hash,
    content_ref: `sha256:${content_hash}`,
    content_type:
      input.content_type === undefined ? "text/plain; charset=utf-8" : input.content_type,
    tags: input.tags === undefined ? [] : [...input.tags],
    prev_hash: input.prev_hash,
  };
  validateIntent(intent);
  return intent;
}

export function createDeleteIntent(input: {
  readonly seq: string;
  readonly key: string;
  readonly prev_hash: string;
}): VaultIntent {
  exactMembers(input, ["seq", "key", "prev_hash"]);
  const intent: VaultIntent = {
    seq: input.seq,
    key: input.key,
    op: "delete",
    content_hash: EMPTY_HASH,
    content_ref: null,
    content_type: "application/octet-stream",
    tags: [],
    prev_hash: input.prev_hash,
  };
  validateIntent(intent);
  return intent;
}

export function signVaultIntent(intent: VaultIntent, privatePkcs8: Uint8Array): string {
  validateIntent(intent);
  return signEd25519(canonicalBytes(intent), privatePkcs8);
}

/** The agent signs intent, NOT server time. The completed receipt hash binds both. */
export function stampVaultEntry(
  input: { readonly intent: VaultIntent; readonly sig_agent: string; readonly ts_server: string },
  publicJwk: Ed25519PublicJwk,
): VaultEntry {
  exactMembers(input, ["intent", "sig_agent", "ts_server"]);
  validateIntent(input.intent);
  assertTimestamp(input.ts_server);
  if (!verifyEd25519(canonicalBytes(input.intent), input.sig_agent, publicJwk))
    throw new TypeError("Invalid vault intent signature");
  return {
    ...input.intent,
    tags: [...input.intent.tags],
    ts_server: input.ts_server,
    sig_agent: input.sig_agent,
  };
}

function entryIntent(entry: VaultEntry): VaultIntent {
  return {
    seq: entry.seq,
    key: entry.key,
    op: entry.op,
    content_hash: entry.content_hash,
    content_ref: entry.content_ref,
    content_type: entry.content_type,
    tags: entry.tags,
    prev_hash: entry.prev_hash,
  };
}

export function validateEntry(value: unknown): asserts value is VaultEntry {
  exactMembers(value, [...INTENT_FIELDS, "ts_server", "sig_agent"]);
  const entry = value as VaultEntry;
  validateIntent(entryIntent(entry));
  assertTimestamp(entry.ts_server);
  decodeBase64url(entry.sig_agent, 64);
}

/** Hash is separate; it is never included in its own preimage. */
export function hashVaultEntry(entry: VaultEntry): string {
  validateEntry(entry);
  return sha256Hex(canonicalBytes(entry));
}

/** Complete export verification requires independent head AND sequence-ranged public key pins. */
export function validateVaultChain(input: {
  readonly did: string;
  readonly entries: readonly VaultEntry[];
  readonly keys: readonly VaultSigningKey[];
  readonly expectedHead: VaultHead;
}): VaultChainResult {
  try {
    const data = exactMembers(input, ["did", "entries", "keys", "expectedHead"]);
    assertAgentDid(data.did);
    const head = exactMembers(data.expectedHead, ["seq", "head_hash"]);
    assertSequence(head.seq, true);
    assertHash(head.head_hash);
    if (!Array.isArray(data.entries) || !Array.isArray(data.keys))
      throw new TypeError("Entry and key arrays required");
    const ranges = data.keys
      .map((value: unknown) => {
        const range = exactMembers(value, ["from_seq", "publicKeyJwk"], ["through_seq"]);
        assertSequence(range.from_seq);
        if (Object.hasOwn(range, "through_seq")) {
          assertSequence(range.through_seq);
          if (BigInt(range.through_seq) < BigInt(range.from_seq))
            throw new TypeError("Reversed signing key range");
        }
        const publicKeyJwk = validatePublicJwk(range.publicKeyJwk, "Ed25519") as Ed25519PublicJwk;
        return {
          from: BigInt(range.from_seq),
          through:
            range.through_seq === undefined ? undefined : BigInt(range.through_seq as string),
          publicKeyJwk,
        };
      })
      .sort((left, right) => (left.from < right.from ? -1 : left.from > right.from ? 1 : 0));
    for (let index = 0; index < ranges.length; index++) {
      const current = ranges[index]!;
      const previous = ranges[index - 1];
      if (
        index === 0
          ? current.from !== 1n
          : previous!.through === undefined || previous!.through! + 1n !== current.from
      )
        throw new TypeError("Ambiguous or gapped signing ranges");
    }
    let previous = sha256Hex(Buffer.from(data.did, "utf8"));
    let sequence = 0n;
    let rangeIndex = 0;
    for (let index = 0; index < data.entries.length; index++) {
      try {
        const entry: unknown = data.entries[index];
        validateEntry(entry);
        sequence++;
        if (BigInt(entry.seq) !== sequence)
          return {
            valid: false,
            error: { stage: "chain", reason: "noncontiguous-sequence", index },
          };
        if (entry.prev_hash !== previous)
          return { valid: false, error: { stage: "chain", reason: "broken-hash-link", index } };
        while (ranges[rangeIndex]?.through !== undefined && ranges[rangeIndex]!.through! < sequence)
          rangeIndex++;
        const range = ranges[rangeIndex];
        if (
          !range ||
          range.from > sequence ||
          !verifyEd25519(canonicalBytes(entryIntent(entry)), entry.sig_agent, range.publicKeyJwk)
        )
          return { valid: false, error: { stage: "chain", reason: "untrusted-signature", index } };
        previous = hashVaultEntry(entry);
      } catch {
        return { valid: false, error: { stage: "chain", reason: "invalid-entry", index } };
      }
    }
    if (head.seq !== sequence.toString() || head.head_hash !== previous)
      return { valid: false, error: { stage: "chain", reason: "expected-head-mismatch" } };
    return {
      valid: true,
      did: data.did,
      entries: data.entries.length,
      head_seq: sequence.toString(),
      head_hash: previous,
    };
  } catch {
    return { valid: false, error: { stage: "chain", reason: "invalid-schema-or-trust-pins" } };
  }
}
