// The F2.3 envelope and RFC 7748 §6.1 wrap inputs of squad-sealed-vectors.json, for squad-sealed.test.ts.
import { openEpochWrap, openSquadEntry } from "../../src/index.js";
import type { SquadEpochWrap, SquadEpochWrapInput, SquadSealedInput } from "../../src/index.js";
import {
  sealSquadEntryWithRandomness,
  wrapEpochKeyWithRandomness,
} from "../../src/squad-sealed.js";
import { bytes, file, utf8 } from "./squad-sealed.js";

// RESEARCH F2.3 anchors: the parent fill must reproduce them (15-01's bytes win if they differ).
export const ANCHORS = {
  envelope_length: 304,
  envelope_sha256: "672c6da84576576efd468049feeb616da5537b54d86f2730be0f8975020e0a63",
  envelope_tag: "b8541ff31a622ae7d632a5d61d275a81",
  wrap_hkdf_key: "d51914e663f68f0e60c8a9239cb8ddcd1ebb7c047b092baf2a2dbacd2369c82e",
  wrap_kid: "f35e5616160a30bf3c6e79fa73c576d40205e8fc3ba4e1c6dcf93e6b98e857b4",
  wrap_length: 364,
  wrap_sha256: "c7dab3bbe75e0703a2b171c6846bcc4b86dc0784d4b4b243cfabe8626f520f1c",
} as const;
export const MARKER = "SQUAD-PLAINTEXT-7f3a";
export const EPOCH_KEY_TYPE = "application/vnd.agentland.squad-epoch-key";
export const OTHER_SQUAD = "01900000-0000-7000-8000-000000000002";
export const ROTATED = "2026-10-10T00:00:00.000Z";
export const NAMES: readonly string[] = [
  "SS1-sealed",
  "SS-no-epoch",
  "SS-stale-after-leave",
  "SS-wrong-header-epoch",
  "SS-bad-length",
  "SS-content-type",
];

export const E = file.envelope;
export const entryInput = (overrides: Partial<SquadSealedInput> = {}): SquadSealedInput => ({
  epochKey: bytes(E.epoch_key_hex),
  epoch: E.epoch,
  squadId: E.squad_id,
  key: E.key,
  meta: E.meta,
  body: utf8(E.body_utf8),
  ...overrides,
});
export const anchor = (): Uint8Array =>
  sealSquadEntryWithRandomness(entryInput(), { nonce: bytes(E.nonce_hex) });
export const openAnchor = (
  envelope: Uint8Array,
  overrides: Partial<{ epochKey: Uint8Array; squadId: string; key: string }> = {},
) =>
  openSquadEntry({
    epochKey: bytes(E.epoch_key_hex),
    squadId: E.squad_id,
    key: E.key,
    envelope,
    ...overrides,
  });
/** A zero-filled envelope of `length` bytes behind a valid magic and the given header epoch. */
export const shaped = (length: number, epoch = 1): Uint8Array => {
  const out = new Uint8Array(length);
  out.set([0x41, 0x4c, 0x51, 0x01]);
  new DataView(out.buffer).setUint32(4, epoch);
  return out;
};
// RFC 8785 equals JSON.stringify here: ASCII strings and members already in code-point order.
export const metaBytes = (size: number): Uint8Array =>
  utf8(JSON.stringify({ content_type: E.meta.content_type, name: E.meta.name, size, tags: [] }));

export const W = file.wrap;
export const WRAP_KEY = `sealed/.squad/${W.squad_id}/epoch/1`;
export const wrapInput = (overrides: Partial<SquadEpochWrapInput> = {}): SquadEpochWrapInput => ({
  recipient: bytes(W.recipient_public_hex),
  did: W.did,
  squadId: W.squad_id,
  epoch: W.epoch,
  epochKey: bytes(W.epoch_key_hex),
  ...overrides,
});
export const wrapAnchor = (): SquadEpochWrap =>
  wrapEpochKeyWithRandomness(wrapInput(), {
    ephemeralSecretKey: bytes(W.ephemeral_secret_hex),
    nonce: bytes(W.nonce_hex),
  });
export const openWrap = (
  envelope: string,
  overrides: Partial<{ did: string; squadId: string; epoch: string; keyring: Uint8Array[] }> = {},
): Uint8Array =>
  openEpochWrap({
    envelope,
    did: W.did,
    squadId: W.squad_id,
    epoch: W.epoch,
    keyring: [bytes(W.recipient_secret_hex)],
    ...overrides,
  });
