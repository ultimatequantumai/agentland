// Typed views of the vector files and byte helpers for squad-sealed.test.ts (16-02).
import { createHash } from "node:crypto";
import { expect } from "vitest";
import { replaySquad } from "../../src/index.js";
import type {
  EncKeyHistory,
  PublicKeyRecord,
  SquadEntry,
  SquadEpochWrap,
  SquadPlatformKey,
  SquadRecipientHistory,
  SquadReplaySuccess,
  SquadSignerKeys,
  SquadStatementPayload,
} from "../../src/index.js";
import sealedFile from "../sealed-vectors.json" with { type: "json" };
import squadFile from "../squad-sealed-vectors.json" with { type: "json" };
import baseFile from "../squad-vectors.json" with { type: "json" };

const PKCS8_PREFIX = "302e020100300506032b657004220420";

export interface Meta {
  content_type: string;
  name: string;
  tags: string[];
}
export interface Row {
  seq: string;
  content_b64url: string;
}
export interface Head {
  seq: string;
  head_hash: string;
}
export interface Scenario {
  name: string;
  squad_id: string;
  expected: unknown;
  entries: SquadEntry[] | null;
  statements: Row[] | null;
  payloads: Row[] | null;
  head: Head | null;
}
export interface SquadSealedFile {
  anchors: Record<string, string | number>;
  attribution: Record<string, string>;
  enc_keys: { label: string; secret_hex: string; public_hex: string | null; kid: string | null }[];
  envelope: Record<
    "epoch_key_hex" | "nonce_hex" | "squad_id" | "epoch" | "key" | "body_utf8",
    string
  > & { meta: Meta; aad_utf8: string | null; envelope_hex: string | null };
  histories: { label: string; did: string; value: EncKeyHistory | null }[];
  scenarios: Scenario[];
  wrap: Record<
    | "recipient_secret_hex"
    | "recipient_public_hex"
    | "ephemeral_secret_hex"
    | "nonce_hex"
    | "did"
    | "squad_id"
    | "epoch"
    | "epoch_key_hex",
    string
  > &
    Record<"kid" | "envelope_b64url" | "envelope_sha256", string | null>;
}
interface BaseFile {
  keys: { label: string; public_x: string; seed_hex: string }[];
  agents: {
    label: string;
    did: string;
    keys: { id: string; key: string; activated_at: string; revoked_at?: string }[];
  }[];
  platform: { kid: string; key: string };
  scenarios: {
    name: string;
    squad_id: string;
    entries: SquadEntry[];
    statements: Row[];
    head: Head;
  }[];
}

export const file = squadFile as unknown as SquadSealedFile;
export const base = baseFile as unknown as BaseFile;
export const sealedVectors = sealedFile as unknown as {
  v1: { envelope_hex: string };
  low_order: { encodings: string[] };
};

export const bytes = (hex: string): Uint8Array => new Uint8Array(Buffer.from(hex, "hex"));
export const hexOf = (raw: Uint8Array): string => Buffer.from(raw).toString("hex");
export const fromB64url = (text: string): Uint8Array =>
  new Uint8Array(Buffer.from(text, "base64url"));
export const toB64url = (raw: Uint8Array): string => Buffer.from(raw).toString("base64url");
export const sha256 = (data: Uint8Array | string): string =>
  createHash("sha256").update(data).digest("hex");
export const utf8 = (text: string): Uint8Array => new TextEncoder().encode(text);
export const fail = (reason: string): string => `agentland-squad-sealed/1: ${reason}`;
export const sealedFail = (reason: string): string => `agentland-sealed/1: ${reason}`;

/** Class and exact message both, so a missing export ("is not a function") cannot pass. */
export function throwsWith(
  run: () => unknown,
  kind: new (...args: never[]) => Error,
  message: string,
): void {
  expect(run).toThrow(kind);
  expect(run).toThrow(new RegExp(`^${message.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}$`));
}

const seeds = new Map(base.keys.map((key) => [key.label, key]));
export const xOf = (label: string): string => seeds.get(label)!.public_x;
export const pkcs8 = (label: string): Uint8Array =>
  bytes(PKCS8_PREFIX + seeds.get(label)!.seed_hex);
export const signerKeys: SquadSignerKeys[] = base.agents.map((agent) => ({
  did: agent.did,
  keys: agent.keys.map((key): PublicKeyRecord => ({
    id: key.id,
    publicKeyJwk: { kty: "OKP", crv: "Ed25519", x: xOf(key.key) },
    purpose: "signing",
    activated_at: key.activated_at,
    ...(key.revoked_at === undefined ? {} : { revoked_at: key.revoked_at }),
  })),
}));
export const platformKeys: SquadPlatformKey[] = [
  {
    kid: base.platform.kid,
    publicKeyJwk: { kty: "OKP", crv: "Ed25519", x: xOf(base.platform.key) },
  },
];

export const hist = (label: string) => file.histories.find((h) => h.label === label)!;
export const encOf = (label: string) => file.enc_keys.find((k) => k.label === label)!;
/** A member's served DID history and encryption key, as a wrapping client receives them. */
export const recipient = (
  label: string,
  overrides: Partial<SquadRecipientHistory> = {},
): SquadRecipientHistory => ({
  did: hist(label).did,
  history: hist(label).value!,
  publicKey: bytes(encOf(label).public_hex!),
  ...overrides,
});
export const scenario = (name: string): Scenario => file.scenarios.find((s) => s.name === name)!;
export const decode = (rows: readonly Row[]): SquadStatementPayload[] =>
  rows.map((row) => ({ seq: row.seq, content: fromB64url(row.content_b64url) }));
export function replayOf(
  s: { squad_id: string; entries: SquadEntry[]; statements: Row[]; head: Head },
  platform: SquadPlatformKey[] = [],
): SquadReplaySuccess {
  const result = replaySquad({
    squadId: s.squad_id,
    entries: s.entries,
    statements: decode(s.statements),
    signerKeys,
    platformKeys: platform,
    expectedHead: s.head,
  });
  expect(result.valid).toBe(true);
  return result as SquadReplaySuccess;
}
export const filled = (s: Scenario) => ({
  squad_id: s.squad_id,
  entries: s.entries!,
  statements: s.statements!,
  head: s.head!,
});
export interface EpochStatement {
  kind: string;
  epoch?: string;
  wraps?: SquadEpochWrap[];
}
export const statementsOf = (s: Scenario): { seq: string; statement: EpochStatement }[] =>
  decode(s.statements!).map((p) => ({
    seq: p.seq,
    statement: JSON.parse(new TextDecoder().decode(p.content)) as EpochStatement,
  }));
/** The attribution rule: epoch key n of scenario X = sha256(utf8(X + "/epoch/" + n)). */
export const epochKeyOf = (name: string, n: string): string => sha256(utf8(`${name}/epoch/${n}`));
