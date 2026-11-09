import { assertTimestamp, canonicalBytes, canonicalize, exactMembers } from "./canonical.js";
import { assertAgentDid } from "./json.js";

// C-13 / D-45: an agent links another DID it controls with a signed `agentland-did-link/1`
// statement. The `format` member puts the domain in the signed bytes (the agentland-vault/1
// manifest precedent). AgentLand never fetches a linked DID: reciprocity (the linked document
// listing the agent DID) is the relying party's check, so no SSRF surface exists. Identity has
// no clock: callers pass DB time as `now`.
export const DID_LINK_FORMAT = "agentland-did-link/1";
export const MAX_ACTIVE_DID_LINKS = 8;
const MAX_DID_BYTES = 512;
const FRESHNESS_MS = 5 * 60 * 1000;

export interface DidLinkStatement {
  action: "link" | "unlink";
  did: string;
  format: "agentland-did-link/1";
  linked_did: string;
  timestamp: string;
}

// W3C DID Core §3.1: lowercase method name; idchar = ALPHA / DIGIT / "." / "-" / "_" /
// pct-encoded; no path, query or fragment. ASCII only, so homographs need percent-encoding.
const DID_ABNF =
  /^did:[a-z0-9]+:(?:(?:[A-Za-z0-9._-]|%[0-9A-Fa-f]{2})*:)*(?:[A-Za-z0-9._-]|%[0-9A-Fa-f]{2})+$/;
// Applied to the lowercased DID: any case, any port, the bare platform DID.
const AGENTLAND_DID = /^did:web:agentland\.us(?:%3a[0-9]+)?(?::|$)/;

/** Package-internal (did.ts uses it); deliberately not in the public barrel. */
export function assertLinkedDid(linked: unknown, agentDid: string): asserts linked is string {
  if (typeof linked !== "string") throw new TypeError("Linked DID must be a string");
  if (new TextEncoder().encode(linked).length > MAX_DID_BYTES)
    throw new TypeError("Linked DID exceeds 512 bytes");
  if (!DID_ABNF.test(linked)) throw new TypeError("Linked DID must match DID Core syntax");
  if (linked === agentDid) throw new TypeError("Linked DID must not be the agent DID");
  if (AGENTLAND_DID.test(linked.toLowerCase()))
    throw new TypeError("Linked DID must not be an AgentLand DID");
}

function assertStatementShape(input: unknown): DidLinkStatement {
  const raw = exactMembers(input, ["action", "did", "format", "linked_did", "timestamp"]);
  if (raw.action !== "link" && raw.action !== "unlink")
    throw new TypeError("DID link action must be link or unlink");
  if (raw.format !== DID_LINK_FORMAT) throw new TypeError("agentland-did-link/1 format required");
  assertAgentDid(raw.did);
  assertTimestamp(raw.timestamp);
  assertLinkedDid(raw.linked_did, raw.did);
  return {
    action: raw.action,
    did: raw.did,
    format: DID_LINK_FORMAT,
    linked_did: raw.linked_did,
    timestamp: raw.timestamp,
  };
}

export function didLinkSigningBytes(s: DidLinkStatement): Uint8Array {
  return canonicalBytes(assertStatementShape(s));
}

/** Checks shape, agent, freshness and the active set; the caller verifies the signature. */
export function validateDidLinkStatement(
  s: unknown,
  ctx: { readonly agentDid: string; readonly now: Date; readonly activeLinks: readonly string[] },
): asserts s is DidLinkStatement {
  const statement = assertStatementShape(s);
  if (!(ctx.now instanceof Date) || Number.isNaN(ctx.now.getTime()))
    throw new TypeError("Valid now required");
  if (statement.did !== ctx.agentDid)
    throw new TypeError("DID link statement is for another agent");
  if (Math.abs(Date.parse(statement.timestamp) - ctx.now.getTime()) > FRESHNESS_MS)
    throw new RangeError("DID link statement is not within 5 minutes");
  const active = ctx.activeLinks.includes(statement.linked_did);
  if (statement.action === "link") {
    if (active) throw new RangeError("DID is already linked");
    if (ctx.activeLinks.length >= MAX_ACTIVE_DID_LINKS)
      throw new RangeError("At most 8 active DID links");
  } else if (!active) throw new RangeError("DID is not linked");
}

const compare = (a: string, b: string) => (a < b ? -1 : a > b ? 1 : 0);

/** Replays in (timestamp, canonical bytes) order; returns DIDs by link time, then code units. */
export function activeDidLinks(
  history: readonly { readonly statement: DidLinkStatement }[],
): string[] {
  const ordered = history
    .map((entry) => assertStatementShape(entry.statement))
    .sort((a, b) => compare(a.timestamp, b.timestamp) || compare(canonicalize(a), canonicalize(b)));
  const active = new Map<string, string>();
  for (const statement of ordered) {
    if ((statement.action === "link") === active.has(statement.linked_did))
      throw new TypeError("Inconsistent DID link history");
    if (statement.action === "link") active.set(statement.linked_did, statement.timestamp);
    else active.delete(statement.linked_did);
  }
  return [...active].sort((a, b) => compare(a[1], b[1]) || compare(a[0], b[0])).map(([did]) => did);
}
