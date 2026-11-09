import { createHash } from "node:crypto";
import { describe, expect, it } from "vitest";
import {
  ENC_KEY_FORMAT,
  ENC_KEY_REVOKE_REASON_MAX,
  ENC_KEY_STATEMENT_WINDOW_MS,
  EncKeyRecipientError,
  SealedEnvelopeError,
  canonicalBytes,
  encKeyStatementBytes,
  signEd25519,
  validateEncKeyStatement,
  verifyEd25519,
  verifyEncKeyRecipient,
} from "../src/index.js";
import type {
  EncKeyHistory,
  EncKeyRecord,
  EncKeyRevokeStatement,
  EncKeyStatement,
  EncKeyStatementAny,
  PublicKeyRecord,
  RotationRecord,
  RotationStatement,
} from "../src/index.js";
import vectors from "./sealed-vectors.json" with { type: "json" };

// RESEARCH F2.1 E1 anchors (RFC 8032 §7.1 test-1 key): the generated file must reproduce them.
const REGISTER_SIG =
  "iP4HoBxwA9Np0gfQGs4q3uO0iT6UxsdjRs_NKgGHt2mo7oAx9fwBuEdiG-IzS1vqA2xBF1dVM7EuBUXATuTiBw";
const REVOKE_SIG =
  "8EVua95crxhFxwWE5HmThUOdj2N7OwUsxPeELBa9gekGsGa631-TNRzIrg57hFfwTRoOyN-SKIFN9zs3McLhAQ";
const PKCS8_PREFIX = "302e020100300506032b657004220420";
const TEST1_SEED = "9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60";
const TEST1_X = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo";
const TEST2_SEED = "4ccd089b28ff96da9db6c346ec114e0f5b8a319f35aba624da8cf6ed4fb8a6fb";
const TEST2_PUBLIC_HEX = "3d4017c3e843895a92b70aa74d1b7ebc9c982ccf2ec4968cc0cd55f12af4660c";
const DID = "did:web:agentland.us:agents:weatherwise";
const OTHER_DID = "did:web:agentland.us:agents:otheragent";
const NOW = new Date("2026-11-01T12:00:00.000Z");
const R_PUB_X = "3p7bfXt9wbTTW2HC7OQ1Nz-DQ8hbeGdNrfx-FG-IK08";
const V1_RID = "f35e5616160a30bf3c6e79fa73c576d40205e8fc3ba4e1c6dcf93e6b98e857b4";
// V1's ephemeral public key: a valid, distinct X25519 key for the key-3 cases.
const KEY3_HEX = "8520f0098930a754748b7ddcb43ef75a0dbf3a0d26381af4eba4a98eaa9b4e6a";
const SHAPE = "Encryption key statement shape required";
const LOW_ORDER = "agentland-sealed/1: low_order";
// Class + message per non-low-order negative; the file's `error` names the class.
const MESSAGES: Readonly<Record<string, string>> = {
  "kind-wrong": SHAPE,
  "member-extra": SHAPE,
  "member-missing": SHAPE,
  "public-key-31": SHAPE,
  "public-key-33": SHAPE,
  "previous-malformed": SHAPE,
  "reason-empty": SHAPE,
  "reason-201": SHAPE,
  "ts-not-utc-ms": SHAPE,
  "did-other-agent": "Encryption key statement is for another agent",
  "ts-early": "Encryption key statement is not within 5 minutes",
  "ts-late": "Encryption key statement is not within 5 minutes",
  "previous-null-while-active": "previous must name the active encryption key",
  "revoke-not-active": "Only the active encryption key can be revoked",
  "now-invalid": "Valid now required",
};
const LOW_ORDER_NAMES = [0, 1, 2, 3, 4, 5, 6].map((i) => `public-key-low-order-${i}`);
const VERIFY_FALSE_NAME = "non-canonical-signature";
const NEGATIVE_NAMES = [...Object.keys(MESSAGES), ...LOW_ORDER_NAMES, VERIFY_FALSE_NAME];

interface StatementVector {
  statement: EncKeyStatementAny;
  canonical_utf8: string;
  signature: string;
}
interface NegativeEntry {
  name: string;
  statement?: unknown;
  canonical_utf8?: string;
  context?: { agent_did?: string; now?: string; active_key_id?: string | null };
  error: "TypeError" | "RangeError" | "SealedEnvelopeError" | "verify_false";
}
interface EncKeyFile {
  signing_seed_hex: string;
  signing_public_x: string;
  did: string;
  register: StatementVector;
  revoke: StatementVector;
  negatives: NegativeEntry[];
}
// The generated vector file is the frozen contract; its shape is EncKeyFile by construction.
const vectorFile = vectors as unknown as { enc_key: EncKeyFile };
const encKey = vectorFile.enc_key;

const pkcs8 = (seed: string) => new Uint8Array(Buffer.from(PKCS8_PREFIX + seed, "hex"));
const TEST1 = pkcs8(TEST1_SEED);
const TEST2 = pkcs8(TEST2_SEED);
const TEST2_X = Buffer.from(TEST2_PUBLIC_HEX, "hex").toString("base64url");
const KEY3_X = Buffer.from(KEY3_HEX, "hex").toString("base64url");
const R_PUB = new Uint8Array(Buffer.from(R_PUB_X, "base64url"));
const flip = (signature: string) => (signature[0] === "A" ? "B" : "A") + signature.slice(1);

const signing = (seq: number, x: string, activated: string, revoked?: string): PublicKeyRecord => ({
  id: `${DID}#key-${seq}`,
  publicKeyJwk: { kty: "OKP", crv: "Ed25519", x },
  purpose: "signing",
  activated_at: activated,
  ...(revoked === undefined ? {} : { revoked_at: revoked }),
});
const encryption = (seq: number, x: string, activated: string): PublicKeyRecord => ({
  id: `${DID}#key-${seq}`,
  publicKeyJwk: { kty: "OKP", crv: "X25519", x },
  purpose: "encryption",
  activated_at: activated,
});
const KEY1 = signing(1, TEST1_X, "2026-10-01T00:00:00.000Z");
const KEY2 = encryption(2, R_PUB_X, "2026-11-01T12:00:00.000Z");
const KEY3 = encryption(3, KEY3_X, "2026-11-01T13:00:00.000Z");
const REGISTER: EncKeyStatement = {
  did: DID,
  kind: "enc_key",
  previous: null,
  public_key: R_PUB_X,
  ts: "2026-11-01T12:00:00.000Z",
};
const REVOKE: EncKeyRevokeStatement = {
  did: DID,
  key_id: `${DID}#key-2`,
  kind: "enc_key_revoke",
  reason: "rotated",
  ts: "2026-11-01T12:05:00.000Z",
};
const REGISTER_RECORD: EncKeyRecord = {
  statement: REGISTER,
  signature: REGISTER_SIG,
  signing_key_id: `${DID}#key-1`,
  custody: "self",
};
// Calls the new export, so only ever invoked inside `it` bodies.
const record = (
  statement: EncKeyStatementAny,
  key: Uint8Array,
  signingKeyId: string,
  custody: EncKeyRecord["custody"] = "self",
): EncKeyRecord => ({
  statement,
  signature: signEd25519(encKeyStatementBytes(statement), key),
  signing_key_id: signingKeyId,
  custody,
});
const rotation = (timestamp: string, dual: boolean): RotationRecord => {
  const statement: RotationStatement = {
    old_pub: { kty: "OKP", crv: "Ed25519", x: TEST1_X },
    new_pub: { kty: "OKP", crv: "Ed25519", x: TEST2_X },
    reason: "scheduled",
    timestamp,
  };
  const bytes = canonicalBytes(statement);
  return {
    statement,
    sig_old: signEd25519(bytes, TEST1),
    ...(dual ? { sig_new: signEd25519(bytes, TEST2) } : {}),
  };
};
const history = (overrides: Partial<EncKeyHistory> = {}): EncKeyHistory => ({
  did: DID,
  keys: [KEY1, KEY2],
  rotations: [],
  enc_keys: [REGISTER_RECORD],
  recovery_notice: null,
  ...overrides,
});
const refuses = (run: () => unknown, reason: string) => {
  expect(run).toThrow(EncKeyRecipientError);
  expect(run).toThrow(reason);
};
const verified = (keyId: string, publicKey: Uint8Array, rid: string, signingKey: string) => ({
  keyId: `${DID}#${keyId}`,
  publicKey,
  recipientKeyId: rid,
  signingKey,
});

describe("vector E1", () => {
  it("constants", () => {
    expect(ENC_KEY_FORMAT).toBe("agentland-enc-key/1");
    expect(ENC_KEY_STATEMENT_WINDOW_MS).toBe(300_000);
    expect(ENC_KEY_REVOKE_REASON_MAX).toBe(200);
  });

  it("the file pins the RFC 8032 test-1 key and the agent DID", () => {
    expect(encKey.signing_seed_hex).toBe(TEST1_SEED);
    expect(encKey.signing_public_x).toBe(TEST1_X);
    expect(encKey.did).toBe(DID);
    expect(encKey.register.statement).toStrictEqual(REGISTER);
    expect(encKey.revoke.statement).toStrictEqual(REVOKE);
  });

  it.each([
    ["register", REGISTER_SIG],
    ["revoke", REVOKE_SIG],
  ] as const)("%s bytes and signature", (name, anchor) => {
    const vector = encKey[name];
    const bytes = encKeyStatementBytes(vector.statement);
    expect(new TextDecoder().decode(bytes)).toBe(vector.canonical_utf8);
    expect(signEd25519(bytes, TEST1)).toBe(anchor);
    expect(vector.signature).toBe(anchor);
    const jwk = { kty: "OKP", crv: "Ed25519", x: TEST1_X } as const;
    expect(verifyEd25519(bytes, anchor, jwk)).toBe(true);
    const tampered = bytes.slice();
    tampered[10] = tampered[10]! ^ 1;
    expect(verifyEd25519(tampered, anchor, jwk)).toBe(false);
  });

  it("register validates with no active key; revoke validates against key-2", () => {
    expect(() =>
      validateEncKeyStatement(encKey.register.statement, {
        agentDid: DID,
        now: NOW,
        activeKeyId: null,
      }),
    ).not.toThrow();
    expect(() =>
      validateEncKeyStatement(encKey.revoke.statement, {
        agentDid: DID,
        now: new Date("2026-11-01T12:05:00.000Z"),
        activeKeyId: `${DID}#key-2`,
      }),
    ).not.toThrow();
  });
});

describe("negative", () => {
  it("the file carries exactly the published negatives", () => {
    expect([...encKey.negatives.map((entry) => entry.name)].sort()).toStrictEqual(
      [...NEGATIVE_NAMES].sort(),
    );
  });

  it.each(NEGATIVE_NAMES.map((name) => [name]))("%s", (name) => {
    const entry = encKey.negatives.find((negative) => negative.name === name)!;
    if (entry.error === "verify_false") {
      // A signature over non-canonical bytes does not verify the canonical statement.
      const raw = new TextEncoder().encode(entry.canonical_utf8!);
      expect(JSON.parse(entry.canonical_utf8!)).toStrictEqual(REGISTER);
      const canonical = encKeyStatementBytes(REGISTER);
      expect(Buffer.from(raw).equals(Buffer.from(canonical))).toBe(false);
      const signature = signEd25519(raw, TEST1);
      expect(verifyEd25519(canonical, signature, { kty: "OKP", crv: "Ed25519", x: TEST1_X })).toBe(
        false,
      );
      return;
    }
    const run = () =>
      validateEncKeyStatement(entry.statement, {
        agentDid: entry.context?.agent_did ?? DID,
        now: new Date(entry.context?.now ?? NOW.toISOString()),
        activeKeyId: entry.context?.active_key_id ?? null,
      });
    const errorClass =
      entry.error === "TypeError"
        ? TypeError
        : entry.error === "RangeError"
          ? RangeError
          : SealedEnvelopeError;
    expect(run).toThrow(errorClass);
    expect(run).toThrow(entry.error === "SealedEnvelopeError" ? LOW_ORDER : MESSAGES[name]!);
  });

  it("exactly ±5 minutes passes", () => {
    for (const ts of ["2026-11-01T11:55:00.000Z", "2026-11-01T12:05:00.000Z"])
      expect(() =>
        validateEncKeyStatement(
          { ...REGISTER, ts },
          { agentDid: DID, now: NOW, activeKeyId: null },
        ),
      ).not.toThrow();
  });

  it("encKeyStatementBytes refuses a malformed statement", () => {
    const run = () =>
      encKeyStatementBytes({ ...REGISTER, extra: 1 } as unknown as EncKeyStatementAny);
    expect(run).toThrow(TypeError);
    expect(run).toThrow(SHAPE);
  });

  it("a lone surrogate in reason is a shape error", () => {
    const statement = { ...REVOKE, reason: "\ud800" };
    for (const run of [
      () => encKeyStatementBytes(statement),
      () =>
        validateEncKeyStatement(statement, {
          agentDid: DID,
          now: new Date("2026-11-01T12:05:00.000Z"),
          activeKeyId: `${DID}#key-2`,
        }),
    ]) {
      expect(run).toThrow(TypeError);
      expect(run).toThrow(SHAPE);
    }
  });
});

describe("recipient", () => {
  it("R1 a self-custody register by the active signing key verifies", () => {
    expect(verifyEncKeyRecipient(history(), DID, R_PUB)).toStrictEqual(
      verified("key-2", R_PUB, V1_RID, TEST1_X),
    );
  });

  it("R2 platform custody is refused", () => {
    const enc_keys = [{ ...REGISTER_RECORD, custody: "platform" as const }];
    refuses(
      () => verifyEncKeyRecipient(history({ enc_keys }), DID, R_PUB),
      "recipient_platform_custody",
    );
  });

  it("R3 a flipped signature is refused", () => {
    const enc_keys = [{ ...REGISTER_RECORD, signature: flip(REGISTER_SIG) }];
    refuses(() => verifyEncKeyRecipient(history({ enc_keys }), DID, R_PUB), "recipient_unverified");
  });

  it("R4 a signer activated after ts is refused", () => {
    const keys = [KEY1, KEY2, signing(5, TEST2_X, "2026-11-01T13:00:00.000Z")];
    const enc_keys = [record(REGISTER, TEST2, `${DID}#key-5`)];
    refuses(
      () => verifyEncKeyRecipient(history({ keys, enc_keys }), DID, R_PUB),
      "recipient_unverified",
    );
  });

  it("R5 a later register supersedes key-2", () => {
    const next: EncKeyStatement = {
      did: DID,
      kind: "enc_key",
      previous: `${DID}#key-2`,
      public_key: KEY3_X,
      ts: "2026-11-01T13:00:00.000Z",
    };
    const state = history({
      keys: [KEY1, KEY2, KEY3],
      enc_keys: [REGISTER_RECORD, record(next, TEST1, `${DID}#key-1`)],
    });
    refuses(() => verifyEncKeyRecipient(state, DID, R_PUB), "recipient_unverified");
    const key3 = new Uint8Array(Buffer.from(KEY3_HEX, "hex"));
    // sha256(KEY3) via node:crypto, independent of the module under test.
    const rid = createHash("sha256").update(key3).digest("hex");
    expect(verifyEncKeyRecipient(state, DID, key3)).toStrictEqual(
      verified("key-3", key3, rid, TEST1_X),
    );
  });

  it("R6 the E1 revoke retires key-2", () => {
    const revoke: EncKeyRecord = {
      statement: REVOKE,
      signature: REVOKE_SIG,
      signing_key_id: `${DID}#key-1`,
      custody: "self",
    };
    refuses(
      () => verifyEncKeyRecipient(history({ enc_keys: [REGISTER_RECORD, revoke] }), DID, R_PUB),
      "recipient_unverified",
    );
  });

  it("R7 a pending recovery notice is refused", () => {
    const recovery_notice = {
      id: "recovery-1",
      started_at: "2026-11-01T11:00:00.000Z",
      completes_at: "2026-11-04T11:00:00.000Z",
    };
    refuses(
      () => verifyEncKeyRecipient(history({ recovery_notice }), DID, R_PUB),
      "recipient_unverified",
    );
  });

  it("R8 another agent's DID is refused", () => {
    refuses(() => verifyEncKeyRecipient(history(), OTHER_DID, R_PUB), "recipient_unverified");
  });

  it("R9 a signer reached forward through any verified rotation from the pin verifies", () => {
    // O-8: forward traversal accepts old-only and dual rotations alike.
    for (const dual of [false, true]) {
      const state = history({
        keys: [
          signing(1, TEST1_X, "2026-10-01T00:00:00.000Z", "2026-10-15T00:00:00.000Z"),
          KEY2,
          signing(4, TEST2_X, "2026-10-15T00:00:00.000Z"),
        ],
        rotations: [rotation("2026-10-15T00:00:00.000Z", dual)],
        enc_keys: [record(REGISTER, TEST2, `${DID}#key-4`)],
      });
      expect(
        verifyEncKeyRecipient(state, DID, R_PUB, { pinnedSigningKey: TEST1_X }),
        `dual=${dual}`,
      ).toStrictEqual(verified("key-2", R_PUB, V1_RID, TEST2_X));
    }
  });

  it("R10 a pin absent from the history is refused", () => {
    refuses(
      () => verifyEncKeyRecipient(history(), DID, R_PUB, { pinnedSigningKey: TEST2_X }),
      "recipient_pin_broken",
    );
  });

  it("R11 backward only through dual rotations", () => {
    const state = (dual: boolean) =>
      history({
        keys: [
          signing(1, TEST1_X, "2026-10-01T00:00:00.000Z", "2026-11-01T13:00:00.000Z"),
          KEY2,
          signing(4, TEST2_X, "2026-11-01T13:00:00.000Z"),
        ],
        rotations: [rotation("2026-11-01T13:00:00.000Z", dual)],
      });
    expect(
      verifyEncKeyRecipient(state(true), DID, R_PUB, { pinnedSigningKey: TEST2_X }),
    ).toStrictEqual(verified("key-2", R_PUB, V1_RID, TEST2_X));
    refuses(
      () => verifyEncKeyRecipient(state(false), DID, R_PUB, { pinnedSigningKey: TEST2_X }),
      "recipient_pin_broken",
    );
  });

  it("R12 two registers with previous null are refused", () => {
    const second: EncKeyStatement = {
      did: DID,
      kind: "enc_key",
      previous: null,
      public_key: KEY3_X,
      ts: "2026-11-01T13:00:00.000Z",
    };
    const state = history({
      keys: [KEY1, KEY2, KEY3],
      enc_keys: [REGISTER_RECORD, record(second, TEST1, `${DID}#key-1`)],
    });
    refuses(() => verifyEncKeyRecipient(state, DID, R_PUB), "recipient_unverified");
  });

  it("R13 rotations carrying the DTO's signatures member verify", () => {
    const dto: (RotationRecord & { readonly signatures: "dual" })[] = [
      { ...rotation("2026-10-15T00:00:00.000Z", true), signatures: "dual" },
    ];
    const state = history({
      keys: [
        signing(1, TEST1_X, "2026-10-01T00:00:00.000Z", "2026-10-15T00:00:00.000Z"),
        KEY2,
        signing(4, TEST2_X, "2026-10-15T00:00:00.000Z"),
      ],
      rotations: dto,
      enc_keys: [record(REGISTER, TEST2, `${DID}#key-4`)],
    });
    expect(verifyEncKeyRecipient(state, DID, R_PUB, { pinnedSigningKey: TEST1_X })).toStrictEqual(
      verified("key-2", R_PUB, V1_RID, TEST2_X),
    );
  });

  it("R14 a low-order publicKey is refused by the sealed check", () => {
    const run = () => verifyEncKeyRecipient(history(), DID, new Uint8Array(32));
    expect(run).toThrow(SealedEnvelopeError);
    expect(run).toThrow(LOW_ORDER);
  });

  it("R15 a register matching no encryption key record is refused", () => {
    refuses(
      () => verifyEncKeyRecipient(history({ keys: [KEY1] }), DID, R_PUB),
      "recipient_unverified",
    );
  });
});
