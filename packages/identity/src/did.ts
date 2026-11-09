import { assertTimestamp, canonicalBytes, canonicalize, exactMembers } from "./canonical.js";
import { assertAgentDid } from "./json.js";
import { validatePublicJwk, verifyEd25519 } from "./keys.js";
import type { Ed25519PublicJwk, PublicJwk } from "./keys.js";
import {
  MAX_ACTIVE_DID_LINKS,
  activeDidLinks,
  assertLinkedDid,
  didLinkSigningBytes,
  type DidLinkStatement,
} from "./did-link.js";

export interface DidLinkRecord {
  readonly statement: DidLinkStatement;
  readonly signature: string;
}

export interface PublicKeyRecord {
  readonly id: string;
  readonly publicKeyJwk: PublicJwk;
  readonly purpose: "signing" | "encryption";
  readonly activated_at: string;
  readonly revoked_at?: string;
}
export interface RotationStatement {
  readonly old_pub: Ed25519PublicJwk;
  readonly new_pub: Ed25519PublicJwk;
  readonly reason: string;
  readonly timestamp: string;
}
export interface RotationRecord {
  readonly statement: RotationStatement;
  readonly sig_old: string;
  readonly sig_new?: string;
}
export interface DidDocument {
  readonly "@context": readonly (string | Readonly<Record<string, string>>)[];
  readonly id: string;
  readonly alsoKnownAs: readonly string[];
  readonly verificationMethod: readonly {
    readonly id: string;
    readonly controller: string;
    readonly type: "JsonWebKey2020";
    readonly publicKeyJwk: PublicJwk;
  }[];
  readonly authentication: readonly string[];
  readonly assertionMethod: readonly string[];
  readonly keyAgreement: readonly string[];
  readonly service: readonly {
    readonly id: string;
    readonly type: "AgentLandTrust";
    readonly serviceEndpoint: string;
  }[];
}
export interface DidHistory {
  readonly did: string;
  readonly keys: readonly PublicKeyRecord[];
  readonly rotations: readonly (RotationRecord & { readonly signatures: "dual" | "old-only" })[];
  readonly links?: readonly DidLinkRecord[];
}

export function agentDid(handle: string): string {
  if (typeof handle !== "string" || !/^[a-z0-9-]{3,24}$/.test(handle))
    throw new TypeError("Canonical lowercase agent handle required");
  return `did:web:agentland.us:agents:${handle}`;
}

export { assertAgentDid };

export function publicRecords(handle: string, keys: readonly PublicKeyRecord[]): PublicKeyRecord[] {
  const did = agentDid(handle);
  if (!Array.isArray(keys)) throw new TypeError("Public key records required");
  const ids = new Set<string>();
  const records = keys.map((input): PublicKeyRecord => {
    const key = exactMembers(
      input,
      ["id", "publicKeyJwk", "purpose", "activated_at"],
      ["revoked_at"],
    );
    if (
      typeof key.id !== "string" ||
      !key.id.startsWith(`${did}#`) ||
      !/^[A-Za-z0-9._~-]+$/.test(key.id.slice(did.length + 1)) ||
      ids.has(key.id)
    )
      throw new TypeError("Unique absolute agent key ID required");
    ids.add(key.id);
    if (key.purpose !== "signing" && key.purpose !== "encryption")
      throw new TypeError("Unknown key purpose");
    const publicKeyJwk = validatePublicJwk(
      key.publicKeyJwk,
      key.purpose === "signing" ? "Ed25519" : "X25519",
    );
    assertTimestamp(key.activated_at);
    if (Object.hasOwn(key, "revoked_at")) {
      assertTimestamp(key.revoked_at);
      if (key.revoked_at < key.activated_at)
        throw new TypeError("Key revocation precedes activation");
    }
    return {
      id: key.id,
      publicKeyJwk,
      purpose: key.purpose,
      activated_at: key.activated_at,
      ...(key.revoked_at === undefined ? {} : { revoked_at: key.revoked_at as string }),
    };
  });
  if (!records.some((key) => key.purpose === "signing"))
    throw new TypeError("Ed25519 signing key required");
  return records.sort((a, b) =>
    a.activated_at < b.activated_at
      ? -1
      : a.activated_at > b.activated_at
        ? 1
        : a.id < b.id
          ? -1
          : a.id > b.id
            ? 1
            : 0,
  );
}

function assertLinkList(handle: string, links: readonly string[]): string[] {
  if (
    !Array.isArray(links) ||
    links.length > MAX_ACTIVE_DID_LINKS ||
    new Set(links).size !== links.length
  )
    throw new TypeError("Links must be an array of at most 8 unique DIDs");
  const did = agentDid(handle);
  for (const link of links) assertLinkedDid(link, did);
  return [...links];
}

export const activeSigningAt = (records: readonly PublicKeyRecord[], timestamp: string) =>
  records.filter(
    (key) =>
      key.purpose === "signing" &&
      key.activated_at <= timestamp &&
      (key.revoked_at === undefined || key.revoked_at >= timestamp),
  );

export function buildDidDocument({
  handle,
  keys,
  links,
}: {
  readonly handle: string;
  readonly keys: readonly PublicKeyRecord[];
  /** Active linked DIDs in published order: pass `activeDidLinks(history)`. */
  readonly links?: readonly string[];
}): DidDocument {
  const id = agentDid(handle);
  const active = publicRecords(handle, keys).filter((key) => key.revoked_at === undefined);
  const signing = active.filter((key) => key.purpose === "signing").map((key) => key.id);
  return {
    "@context": [
      "https://www.w3.org/ns/did/v1",
      "https://w3id.org/security/suites/jws-2020/v1",
      { AgentLandTrust: "https://agentland.us/spec/agentland-did/1#AgentLandTrust" },
    ],
    id,
    // The profile URL stays first (DID permanence); linked DIDs follow.
    alsoKnownAs: [
      `https://agentland.us/agents/${handle}/did.json`,
      ...assertLinkList(handle, links ?? []),
    ],
    verificationMethod: active.map((key) => ({
      id: key.id,
      controller: id,
      type: "JsonWebKey2020",
      publicKeyJwk: key.publicKeyJwk,
    })),
    authentication: signing,
    assertionMethod: [...signing],
    keyAgreement: active.filter((key) => key.purpose === "encryption").map((key) => key.id),
    service: [
      {
        id: `${id}#trust`,
        type: "AgentLandTrust",
        serviceEndpoint: `https://agentland.us/v1/agents/${handle}/trust`,
      },
    ],
  };
}

/** Verifies statements, not challenge windows, recovery delays or authorization policy. */
export function buildDidHistory({
  handle,
  keys,
  rotations,
  links,
}: {
  readonly handle: string;
  readonly keys: readonly PublicKeyRecord[];
  readonly rotations: readonly RotationRecord[];
  readonly links?: readonly DidLinkRecord[];
}): DidHistory {
  const records = publicRecords(handle, keys);
  if (!Array.isArray(rotations)) throw new TypeError("Rotation statements required");
  const history = rotations.map((input) => {
    const rotation = exactMembers(input, ["statement", "sig_old"], ["sig_new"]);
    const raw = exactMembers(rotation.statement, ["old_pub", "new_pub", "reason", "timestamp"]);
    const oldKey = validatePublicJwk(raw.old_pub, "Ed25519") as Ed25519PublicJwk;
    const newKey = validatePublicJwk(raw.new_pub, "Ed25519") as Ed25519PublicJwk;
    assertTimestamp(raw.timestamp);
    if (typeof raw.reason !== "string" || raw.reason.length === 0 || oldKey.x === newKey.x)
      throw new TypeError("Distinct rotation keys and reason required");
    const statement: RotationStatement = {
      old_pub: oldKey,
      new_pub: newKey,
      reason: raw.reason,
      timestamp: raw.timestamp,
    };
    canonicalize(statement);
    for (const publicKey of [oldKey, newKey]) {
      if (
        !activeSigningAt(records, statement.timestamp).some(
          (key) => key.publicKeyJwk.x === publicKey.x,
        )
      )
        throw new TypeError("Rotation key absent or inactive at statement time");
    }
    const bytes = canonicalBytes(statement);
    if (
      !verifyEd25519(bytes, rotation.sig_old as string, oldKey) ||
      (Object.hasOwn(rotation, "sig_new") &&
        !verifyEd25519(bytes, rotation.sig_new as string, newKey))
    )
      throw new TypeError("Invalid rotation signature");
    return {
      statement,
      sig_old: rotation.sig_old as string,
      ...(rotation.sig_new === undefined ? {} : { sig_new: rotation.sig_new as string }),
      signatures: rotation.sig_new === undefined ? ("old-only" as const) : ("dual" as const),
    };
  });
  history.sort((a, b) => {
    const left = canonicalize(a.statement),
      right = canonicalize(b.statement);
    return a.statement.timestamp < b.statement.timestamp
      ? -1
      : a.statement.timestamp > b.statement.timestamp
        ? 1
        : left < right
          ? -1
          : left > right
            ? 1
            : 0;
  });
  const did = agentDid(handle);
  if (links === undefined) return { did, keys: records, rotations: history };
  if (!Array.isArray(links)) throw new TypeError("DID link records required");
  const linkHistory = links.map((input): DidLinkRecord => {
    const entry = exactMembers(input, ["statement", "signature"]);
    const bytes = didLinkSigningBytes(entry.statement as DidLinkStatement);
    const statement = entry.statement as DidLinkStatement;
    if (statement.did !== did) throw new TypeError("DID link statement is for another agent");
    if (
      typeof entry.signature !== "string" ||
      !activeSigningAt(records, statement.timestamp).some((key) =>
        verifyEd25519(bytes, entry.signature as string, key.publicKeyJwk as Ed25519PublicJwk),
      )
    )
      throw new TypeError("Invalid or inactive DID link signature");
    return { statement, signature: entry.signature };
  });
  activeDidLinks(linkHistory);
  linkHistory.sort((a, b) => {
    const left = canonicalize(a.statement),
      right = canonicalize(b.statement);
    return a.statement.timestamp < b.statement.timestamp
      ? -1
      : a.statement.timestamp > b.statement.timestamp
        ? 1
        : left < right
          ? -1
          : left > right
            ? 1
            : 0;
  });
  return { did, keys: records, rotations: history, links: linkHistory };
}
