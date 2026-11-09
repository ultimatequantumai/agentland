import { readFileSync } from "node:fs";
import { secp256k1 } from "@noble/curves/secp256k1.js";
import { keccak_256 } from "@noble/hashes/sha3.js";
import { describe, expect, it } from "vitest";
import {
  ANCHOR_FORMAT,
  ANCHOR_MAX_GAS,
  ANCHOR_MIN_GAS,
  ANCHOR_PAYLOAD_PREFIX,
  AnchorGuardError,
  anchorPayload,
  anchorSignatureFromDer,
  anchorSigningHash,
  assertAnchorTransaction,
  currentRuleGas,
  decodeAnchorTransaction,
  evmAddressFromSpki,
  serializeAnchorTransaction,
  verifyAnchorTransaction,
} from "../src/index.js";
import type { AnchorExpectation, AnchorTransactionFields } from "../src/index.js";
import vectors from "./anchor-vectors.json" with { type: "json" };

type A1 = typeof vectors.a1;
type Change = Readonly<Record<string, string>>;
interface GuardCase {
  readonly name: string;
  readonly change: Change;
  readonly reason: string;
}
interface PassCase {
  readonly name: string;
  readonly change: Change;
}

const hex = (bytes: Uint8Array) =>
  Array.from(bytes, (b) => b.toString(16).padStart(2, "0")).join("");
const unhex = (text: string) => {
  const s = text.startsWith("0x") ? text.slice(2) : text;
  const out = new Uint8Array(s.length / 2);
  for (let i = 0; i < out.length; i++) out[i] = Number.parseInt(s.slice(2 * i, 2 * i + 2), 16);
  return out;
};
const concat = (...parts: readonly Uint8Array[]) => {
  const out = new Uint8Array(parts.reduce((n, p) => n + p.length, 0));
  let at = 0;
  for (const p of parts) {
    out.set(p, at);
    at += p.length;
  }
  return out;
};
const fail = (reason: string) => `agentland-anchor/1: ${reason}`;
const utf8 = (text: string) => new TextEncoder().encode(text);

const fieldsOf = (a1: A1, change: Change): AnchorTransactionFields => {
  const v = { ...a1, ...change } as unknown as Record<string, string>;
  return {
    chainId: BigInt(v.chain_id!),
    nonce: BigInt(v.nonce!),
    maxPriorityFeePerGas: BigInt(v.max_priority_fee_per_gas!),
    maxFeePerGas: BigInt(v.max_fee_per_gas!),
    gasLimit: BigInt(v.gas_limit!),
    to: v.to ?? a1.address,
    value: BigInt(v.value!),
    data: utf8(v.data_utf8!),
  };
};
const expectation = (): AnchorExpectation => ({
  chainId: BigInt(vectors.guard.expected.chain_id),
  address: vectors.guard.expected.address,
  payload: utf8(vectors.a1.data_utf8),
  maxFeePerGasCap: BigInt(vectors.guard.expected.max_fee_per_gas_cap),
});
const guardedA1 = () => assertAnchorTransaction(fieldsOf(vectors.a1, {}), expectation());
const a1Signature = () => ({
  r: BigInt("0x" + vectors.a1.r),
  s: BigInt("0x" + vectors.a1.s),
  yParity: 1 as const,
});

// Test-local RLP (Yellow Paper App. B), independent of the module under test.
type Rlp = Uint8Array | readonly Rlp[];
const rlpLength = (n: number, offset: number) => {
  if (n < 56) return Uint8Array.of(offset + n);
  const bytes = unhex(
    n.toString(16).padStart(n.toString(16).length + (n.toString(16).length % 2), "0"),
  );
  return concat(Uint8Array.of(offset + 55 + bytes.length), bytes);
};
const rlp = (item: Rlp): Uint8Array => {
  if (item instanceof Uint8Array)
    return item.length === 1 && item[0]! < 0x80 ? item : concat(rlpLength(item.length, 0x80), item);
  const body = concat(...item.map(rlp));
  return concat(rlpLength(body.length, 0xc0), body);
};
const int = (n: bigint) =>
  n === 0n
    ? new Uint8Array(0)
    : unhex(n.toString(16).padStart(n.toString(16).length + (n.toString(16).length % 2), "0"));

// Signs a type-2 transaction test-side with noble (low-s by default) and finds the recovery bit.
const signTx = (
  fields: AnchorTransactionFields,
  privByte: number,
  accessList: readonly Rlp[] = [],
) => {
  const priv = new Uint8Array(32).fill(privByte);
  const unsigned: Rlp[] = [
    int(fields.chainId),
    int(fields.nonce),
    int(fields.maxPriorityFeePerGas),
    int(fields.maxFeePerGas),
    int(fields.gasLimit),
    unhex(fields.to),
    int(fields.value),
    fields.data,
    accessList,
  ];
  const hash = keccak_256(concat(Uint8Array.of(2), rlp(unsigned)));
  const sig = secp256k1.Signature.fromBytes(
    secp256k1.sign(hash, priv, { prehash: false }),
    "compact",
  );
  const pub = hex(secp256k1.getPublicKey(priv, false));
  const yParity = [0, 1].find(
    (v) => hex(sig.addRecoveryBit(v).recoverPublicKey(hash).toBytes(false)) === pub,
  )!;
  return concat(Uint8Array.of(2), rlp([...unsigned, int(BigInt(yParity)), int(sig.r), int(sig.s)]));
};
const spkiOf = (privByte: number) =>
  concat(
    unhex("3056301006072a8648ce3d020106052b8104000a034200"),
    secp256k1.getPublicKey(new Uint8Array(32).fill(privByte), false),
  );
const verifyExpected = () => ({
  chainId: 1n,
  address: vectors.a1.address,
  payload: utf8(vectors.a1.data_utf8),
});

describe("vector A1", () => {
  it("payload bytes", () => {
    const payload = anchorPayload(vectors.a1.date, vectors.a1.root_hex);
    expect(new TextDecoder().decode(payload)).toBe(vectors.a1.data_utf8);
    expect(payload.length).toBe(98);
  });

  it("signing hash", () => {
    expect(hex(anchorSigningHash(guardedA1()))).toBe(vectors.a1.signing_hash);
  });

  it("address", () => {
    expect(evmAddressFromSpki(unhex(vectors.a1.public_key_spki_der_hex))).toBe(vectors.a1.address);
  });

  it("signature from DER", () => {
    expect(
      anchorSignatureFromDer(
        unhex(vectors.a1.kms_der_signature),
        unhex(vectors.a1.signing_hash),
        unhex(vectors.a1.public_key_spki_der_hex),
      ),
    ).toEqual(a1Signature());
  });

  it("raw transaction", () => {
    expect("0x" + hex(serializeAnchorTransaction(guardedA1(), a1Signature()))).toBe(
      vectors.a1.raw_tx,
    );
  });

  it("decode", () => {
    const raw = unhex(vectors.a1.raw_tx);
    const decoded = decodeAnchorTransaction(raw);
    const fields = fieldsOf(vectors.a1, {});
    expect(decoded.chainId).toBe(fields.chainId);
    expect(decoded.nonce).toBe(fields.nonce);
    expect(decoded.maxPriorityFeePerGas).toBe(fields.maxPriorityFeePerGas);
    expect(decoded.maxFeePerGas).toBe(fields.maxFeePerGas);
    expect(decoded.gasLimit).toBe(fields.gasLimit);
    expect(decoded.to).toBe(fields.to);
    expect(decoded.value).toBe(fields.value);
    expect(hex(decoded.data)).toBe(hex(fields.data));
    expect(decoded.signature).toEqual(a1Signature());
    expect(decoded.from).toBe(vectors.a1.address);
    expect(decoded.hash).toBe(vectors.a1.tx_hash);
    expect(decoded.hash).toBe("0x" + hex(keccak_256(raw)));
  });
});

describe("high-s", () => {
  const N_HALF = BigInt("0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a0");

  it("normalizes a high s from DER to n - s with the recovered parity", () => {
    const h = vectors.high_s;
    expect(
      anchorSignatureFromDer(
        unhex(h.der),
        unhex(h.digest),
        unhex(vectors.a1.public_key_spki_der_hex),
      ),
    ).toEqual({ r: BigInt("0x" + h.r), s: BigInt("0x" + h.s_low), yParity: 1 });
  });

  it("s_high is above n/2 and s_low = n - s_high", () => {
    const h = vectors.high_s;
    expect(BigInt("0x" + h.s_high) > N_HALF).toBe(true);
    expect(BigInt("0x" + h.s_low)).toBe(secp256k1.Point.CURVE().n - BigInt("0x" + h.s_high));
  });

  it("noble's default lowS verify rejects s_high and accepts s_low", () => {
    const h = vectors.high_s;
    const pub = secp256k1.getPublicKey(unhex(vectors.a1.test_private_key_hex), false);
    const compact = (r: string, s: string) => unhex(r + s);
    expect(secp256k1.verify(compact(h.r, h.s_high), unhex(h.digest), pub, { prehash: false })).toBe(
      false,
    );
    expect(secp256k1.verify(compact(h.r, h.s_low), unhex(h.digest), pub, { prehash: false })).toBe(
      true,
    );
  });

  it("serializeAnchorTransaction refuses a high s", () => {
    const h = vectors.high_s;
    const call = () =>
      serializeAnchorTransaction(guardedA1(), {
        r: BigInt("0x" + h.r),
        s: BigInt("0x" + h.s_high),
        yParity: 1,
      });
    expect(call).toThrow(AnchorGuardError);
    expect(call).toThrow(fail("signature"));
  });

  it("decodeAnchorTransaction refuses a raw transaction carrying a high s", () => {
    const raw = unhex(vectors.a1.raw_tx);
    const tampered = concat(raw.slice(0, raw.length - 32), unhex(vectors.high_s.s_high));
    const call = () => decodeAnchorTransaction(tampered);
    expect(call).toThrow(AnchorGuardError);
    expect(call).toThrow(fail("signature"));
  });

  it("refuses unparsable DER and a key no recovery bit reproduces", () => {
    const spki = unhex(vectors.a1.public_key_spki_der_hex);
    const hash = unhex(vectors.a1.signing_hash);
    const der = unhex(vectors.a1.kms_der_signature);
    for (const call of [
      () => anchorSignatureFromDer(unhex("3000"), hash, spki),
      () => anchorSignatureFromDer(der, hash, spkiOf(0x47)),
    ]) {
      expect(call).toThrow(AnchorGuardError);
      expect(call).toThrow(fail("signature"));
    }
  });

  it("requires a 32-byte signing hash", () => {
    const call = () =>
      anchorSignatureFromDer(
        unhex(vectors.a1.kms_der_signature),
        new Uint8Array(31),
        unhex(vectors.a1.public_key_spki_der_hex),
      );
    expect(call).toThrow(TypeError);
    expect(call).toThrow("32-byte signing hash required");
  });
});

describe("guard", () => {
  const cases = vectors.guard.cases as unknown as readonly GuardCase[];
  const passes = vectors.guard.passes as unknown as readonly PassCase[];

  for (const entry of cases)
    it(entry.name, () => {
      let caught: unknown;
      try {
        assertAnchorTransaction(fieldsOf(vectors.a1, entry.change), expectation());
      } catch (error) {
        caught = error;
      }
      expect(caught).toBeInstanceOf(AnchorGuardError);
      expect((caught as AnchorGuardError).message).toBe(fail(entry.reason));
      expect((caught as AnchorGuardError).reason).toBe(entry.reason);
    });

  for (const entry of passes)
    it(entry.name, () => {
      const guarded = assertAnchorTransaction(fieldsOf(vectors.a1, entry.change), expectation());
      expect(guarded.gasLimit).toBe(fieldsOf(vectors.a1, entry.change).gasLimit);
      expect(Object.isFrozen(guarded)).toBe(true);
    });

  it("the cap bound holds by construction", () => {
    const cap = expectation().maxFeePerGasCap;
    for (const entry of passes) {
      const f = fieldsOf(vectors.a1, entry.change);
      expect(f.gasLimit * f.maxFeePerGas <= cap * 100_000n).toBe(true);
    }
  });

  it("constants", () => {
    expect(ANCHOR_FORMAT).toBe("agentland-anchor/1");
    expect(ANCHOR_PAYLOAD_PREFIX).toBe("agentland-audit-root/1");
    expect(ANCHOR_MIN_GAS).toBe(21_000);
    expect(ANCHOR_MAX_GAS).toBe(100_000);
  });

  it("no signature input", () => {
    expect(assertAnchorTransaction.length).toBe(2);
  });

  it("a Uint8Array subclass with lying methods cannot pass a wrong payload", () => {
    class Lying extends Uint8Array {
      override some(): boolean {
        return false;
      }
      override every(): boolean {
        return true;
      }
    }
    const wrong = new Lying(utf8("agentland-audit-root/1 2026-11-02 9f3b" + "00".repeat(30)));
    let caught: unknown;
    try {
      assertAnchorTransaction({ ...fieldsOf(vectors.a1, {}), data: wrong }, expectation());
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(AnchorGuardError);
    expect((caught as AnchorGuardError).message).toBe(fail("payload"));
    expect((caught as AnchorGuardError).reason).toBe("payload");
  });

  it("an address-like object that lies through toString and slice is refused as encoding", () => {
    const liar = {
      toString: () => vectors.a1.address,
      slice: () => "0000000000000000000000000000000000000001",
    } as unknown as string;
    let caught: unknown;
    try {
      assertAnchorTransaction(
        { ...fieldsOf(vectors.a1, {}), to: liar },
        { ...expectation(), address: liar },
      );
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(AnchorGuardError);
    expect((caught as AnchorGuardError).message).toBe(fail("encoding"));
    expect((caught as AnchorGuardError).reason).toBe("encoding");
    const signing = () =>
      anchorSigningHash({ ...fieldsOf(vectors.a1, {}), to: liar, guarded: true });
    expect(signing).toThrow(TypeError);
    expect(signing).toThrow("Anchor transaction must come from assertAnchorTransaction");
  });

  it("a Proxy over a Uint8Array with a lying iterator and indexes is refused as encoding", () => {
    const expected = utf8(vectors.a1.data_utf8);
    const other = utf8("agentland-audit-root/1 2026-11-02 9f3b" + "00".repeat(30));
    const proxy = new Proxy(other, {
      get: (target, key) =>
        key === Symbol.iterator
          ? () => expected[Symbol.iterator]()
          : (Reflect.get(target, key) as unknown),
    });
    let caught: unknown;
    try {
      assertAnchorTransaction({ ...fieldsOf(vectors.a1, {}), data: proxy }, expectation());
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(AnchorGuardError);
    expect((caught as AnchorGuardError).message).toBe(fail("encoding"));
    expect((caught as AnchorGuardError).reason).toBe("encoding");
  });

  it("a data getter is read once: guarding then hashing gives the D-47 hash", () => {
    const payload = utf8(vectors.a1.data_utf8);
    const other = utf8("agentland-audit-root/1 2026-11-02 9f3b" + "00".repeat(30));
    let reads = 0;
    const fields = Object.defineProperty({ ...fieldsOf(vectors.a1, {}) }, "data", {
      get: () => (reads++ === 0 ? payload : other),
    });
    const guarded = assertAnchorTransaction(fields, expectation());
    expect(hex(anchorSigningHash(guarded))).toBe(vectors.a1.signing_hash);
    expect("0x" + hex(serializeAnchorTransaction(guarded, a1Signature()))).toBe(vectors.a1.raw_tx);
    expect(reads).toBe(1);
  });

  it("signing refuses anything that did not come from assertAnchorTransaction", () => {
    const plain = { ...fieldsOf(vectors.a1, {}), guarded: true as const };
    const copied = { ...guardedA1() };
    for (const input of [plain, copied]) {
      const call = () => anchorSigningHash(input);
      expect(call).toThrow(TypeError);
      expect(call).toThrow("Anchor transaction must come from assertAnchorTransaction");
    }
  });

  it("serialization accepts plain fields but refuses coercing or proxied inputs", () => {
    expect("0x" + hex(serializeAnchorTransaction(fieldsOf(vectors.a1, {}), a1Signature()))).toBe(
      vectors.a1.raw_tx,
    );
    const liar = {
      toString: () => vectors.a1.address,
      slice: () => "0000000000000000000000000000000000000001",
    } as unknown as string;
    const proxy = new Proxy(utf8(vectors.a1.data_utf8), {});
    for (const fields of [
      { ...fieldsOf(vectors.a1, {}), to: liar },
      { ...fieldsOf(vectors.a1, {}), data: proxy },
    ]) {
      const call = () => serializeAnchorTransaction(fields, a1Signature());
      expect(call).toThrow(AnchorGuardError);
      expect(call).toThrow(fail("encoding"));
    }
  });

  it("the guarded snapshot is frozen and its bytes are not the signing input", () => {
    const guarded = guardedA1();
    expect(Object.isFrozen(guarded)).toBe(true);
    expect(Reflect.set(guarded, "gasLimit", 1n)).toBe(false);
    expect(guarded.gasLimit).toBe(24_920n);
    guarded.data[0] = 0x41;
    expect(hex(anchorSigningHash(guarded))).toBe(vectors.a1.signing_hash);
  });
});

describe("gas", () => {
  it("current-rule gas values", () => {
    expect(currentRuleGas(98, 98)).toBe(24_920);
    expect(currentRuleGas(0, 0)).toBe(21_000);
    expect(currentRuleGas(98, 0)).toBe(21_980);
    expect(currentRuleGas(10, 10)).toBe(21_400);
  });

  it("the A1 gas limit is the current-rule gas of its payload", () => {
    const payload = anchorPayload(vectors.a1.date, vectors.a1.root_hex);
    expect(BigInt(vectors.a1.gas_limit)).toBe(
      BigInt(currentRuleGas(payload.length, payload.filter((b) => b !== 0).length)),
    );
  });

  it("refuses non-integer or out-of-range byte counts", () => {
    for (const [len, nz] of [
      [98, 99],
      [98, -1],
      [1.5, 0],
    ] as const) {
      const call = () => currentRuleGas(len, nz);
      expect(call).toThrow(RangeError);
      expect(call).toThrow("nonZeroBytes must be an integer from 0 to dataLength");
    }
  });
});

describe("payload", () => {
  const root = vectors.a1.root_hex;

  it("round-trips the prefix, date and root", () => {
    expect(new TextDecoder().decode(anchorPayload("2026-11-02", root))).toBe(
      ANCHOR_PAYLOAD_PREFIX + " 2026-11-02 " + root,
    );
  });

  it("refuses a date that is not a UTC calendar day", () => {
    for (const date of ["2026-02-29", "2026-13-01", "2026-1-02", "2026-11-02 "]) {
      const call = () => anchorPayload(date, root);
      expect(call).toThrow(TypeError);
      expect(call).toThrow("Anchor date must be a UTC calendar day YYYY-MM-DD");
    }
  });

  it("accepts a leap day", () => {
    expect(anchorPayload("2028-02-29", root).length).toBe(98);
  });

  it("refuses a root that is not 64 lowercase hex characters", () => {
    for (const bad of [root.toUpperCase(), root.slice(1), "g" + root.slice(1)]) {
      const call = () => anchorPayload("2026-11-02", bad);
      expect(call).toThrow(TypeError);
      expect(call).toThrow("Anchor root must be 64 lowercase hex characters");
    }
  });

  it("evmAddressFromSpki refuses an off-curve point and a short SPKI", () => {
    const spki = unhex(vectors.a1.public_key_spki_der_hex);
    const offCurve = spki.slice();
    offCurve[offCurve.length - 1] = offCurve[offCurve.length - 1]! ^ 0x01;
    for (const bad of [offCurve, spki.slice(0, 87)]) {
      const call = () => evmAddressFromSpki(bad);
      expect(call).toThrow(TypeError);
      expect(call).toThrow("secp256k1 SPKI required");
    }
  });
});

describe("verify", () => {
  const refuse = (call: () => unknown, reason: string) => {
    expect(call).toThrow(AnchorGuardError);
    expect(call).toThrow(fail(reason));
  };

  it("A1 verifies", () => {
    expect(verifyAnchorTransaction(unhex(vectors.a1.raw_tx), verifyExpected())).toEqual({
      hash: vectors.a1.tx_hash,
      from: vectors.a1.address,
    });
  });

  it("refuses another chain, destination or payload", () => {
    const raw = unhex(vectors.a1.raw_tx);
    refuse(
      () => verifyAnchorTransaction(raw, { ...verifyExpected(), chainId: 11155111n }),
      "chain",
    );
    refuse(
      () =>
        verifyAnchorTransaction(raw, {
          ...verifyExpected(),
          address: "0x0000000000000000000000000000000000000001",
        }),
      "destination",
    );
    refuse(
      () =>
        verifyAnchorTransaction(raw, {
          ...verifyExpected(),
          payload: anchorPayload("2026-11-02", "9f3b" + "00".repeat(30)),
        }),
      "payload",
    );
  });

  it("refuses malformed or non-canonical encodings", () => {
    const raw = unhex(vectors.a1.raw_tx);
    const typeOne = raw.slice();
    typeOne[0] = 0x01;
    const padded = raw.slice();
    expect(padded[4]).toBe(0x80);
    padded[4] = 0x00;
    for (const bad of [
      typeOne,
      concat(raw, Uint8Array.of(0)),
      raw.slice(0, raw.length - 1),
      padded,
    ])
      refuse(() => verifyAnchorTransaction(bad, verifyExpected()), "encoding");
  });

  it("refuses a transaction with value", () => {
    const raw = signTx({ ...fieldsOf(vectors.a1, {}), value: 1n }, 0x46);
    refuse(() => verifyAnchorTransaction(raw, verifyExpected()), "value");
  });

  it("refuses a non-empty access list", () => {
    const entry: Rlp = [unhex(vectors.a1.address), [new Uint8Array(32)]];
    const raw = signTx(fieldsOf(vectors.a1, {}), 0x46, [entry]);
    refuse(() => verifyAnchorTransaction(raw, verifyExpected()), "encoding");
  });

  it("refuses a payload transaction sent to the notary from another key", () => {
    const raw = signTx(fieldsOf(vectors.a1, {}), 0x47);
    refuse(() => verifyAnchorTransaction(raw, verifyExpected()), "signature");
  });

  it("refuses a canonical list nested 100,000 deep as encoding, not a stack overflow", () => {
    // Prefixes are computed inside out, then joined once, to keep construction linear.
    const prefixes: Uint8Array[] = [];
    let length = 1;
    for (let i = 0; i < 100_000; i++) {
      const prefix = rlpLength(length, 0xc0);
      prefixes.push(prefix);
      length += prefix.length;
    }
    // No spread over 100,000 arguments: write the prefixes into one buffer.
    const raw = new Uint8Array(1 + length);
    raw[0] = 0x02;
    let at = 1;
    for (let i = prefixes.length - 1; i >= 0; i--) {
      raw.set(prefixes[i]!, at);
      at += prefixes[i]!.length;
    }
    raw[at] = 0xc0;
    refuse(() => verifyAnchorTransaction(raw, verifyExpected()), "encoding");
    refuse(() => decodeAnchorTransaction(raw), "encoding");
  });

  it("refuses a malformed expected address as a caller bug", () => {
    const call = () =>
      verifyAnchorTransaction(unhex(vectors.a1.raw_tx), { ...verifyExpected(), address: "0xABC" });
    expect(call).toThrow(TypeError);
    expect(call).toThrow("EVM address required");
  });
});

describe("spec", () => {
  const text = () =>
    readFileSync(new URL("../spec/agentland-anchor-1.md", import.meta.url), "utf8");

  it("opens with the title and the announced status", () => {
    const lines = text().split("\n");
    expect(lines[0]).toBe("# agentland-anchor/1");
    expect(lines.slice(1).find((line) => line.trim() !== "")).toBe(
      "Status: announced, not in effect. AgentLand will publish the date this takes effect on /transparency.",
    );
  });

  it("has the sections in order", () => {
    const headings = text()
      .split("\n")
      .filter((line) => line.startsWith("## "));
    expect(headings).toEqual([
      "## Payload",
      "## Transaction",
      "## Notary key and address",
      "## Signing guard",
      "## Gas and fees",
      "## Verification",
      "## What a second anchor proves",
      "## Vectors",
      "## License",
    ]);
  });

  it("carries the frozen terms, the A1 vector and the no-earlier-roots rule", () => {
    const body = text();
    for (const term of [
      "agentland-audit-root/1",
      "EIP-1559",
      "EIP-2",
      "0x02",
      "21,000",
      "100,000",
      "finalized",
      "keccak256",
      vectors.a1.tx_hash,
      vectors.a1.address,
      "packages/identity/test/anchor-vectors.json",
      "No second anchor is sent for roots published before the first one.",
    ])
      expect(body).toContain(term);
  });

  it("ends with an MIT ## License section, never mentions escrow and uses no tables", () => {
    const body = text();
    const license = body.indexOf("\n## License\n");
    expect(license).toBeGreaterThan(0);
    const tail = body.slice(license + "\n## License\n".length);
    expect(tail).toContain("MIT License");
    expect(tail).toContain("Permission is hereby granted, free of charge");
    expect(tail).not.toMatch(/^#{1,2} /m);
    expect(body.toLowerCase()).not.toContain("escrow");
    expect(body).not.toMatch(/^\| /m);
  });
});
