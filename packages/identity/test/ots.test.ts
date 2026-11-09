import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import * as identity from "../src/index.js";
import {
  OTS_AGGREGATORS,
  OtsFormatError,
  bitcoinHeights,
  detachedOts,
  matchesCalendarWhitelist,
  mergeAt,
  mergedReceipt,
  parseDetachedOts,
  parseTimestamp,
  pendingCommitments,
  serializeTimestamp,
} from "../src/ots.js";
import type { OtsNode } from "../src/ots.js";

interface Recorded {
  readonly sha256: string;
  readonly hex: string;
}
const recorded = JSON.parse(
  readFileSync(new URL("./fixtures/ots/recorded.json", import.meta.url), "utf8"),
) as {
  readonly aggregators: {
    readonly digest: string;
    readonly recorded_at: string;
    readonly responses: Record<string, Recorded>;
  };
  readonly hello_world_ots: Recorded;
  readonly incomplete_ots: Recorded;
  readonly incomplete_alice_upgrade: Recorded;
};

const bytes = (value: string) => new Uint8Array(Buffer.from(value, "hex"));
const hex = (value: Uint8Array) => Buffer.from(value).toString("hex");
const cat = (...parts: Array<Uint8Array | number[]>) =>
  new Uint8Array(Buffer.concat(parts.map((part) => Uint8Array.from(part))));
function varuint(value: number): number[] {
  const out: number[] = [];
  do {
    const low = value % 128;
    value = Math.floor(value / 128);
    out.push(value > 0 ? low | 0x80 : low);
  } while (value > 0);
  return out;
}
const varbytes = (value: Uint8Array) => cat(varuint(value.length), value);
const ascii = (value: string) => new TextEncoder().encode(value);

// Format rules (python-opentimestamps): an attestation item is 00 ‖ 8-byte tag ‖ varbytes payload.
const HEADER = bytes("004f70656e54696d657374616d7073000050726f6f6600bf89e2e884e89294");
const PENDING_TAG = [0x83, 0xdf, 0xe3, 0x0d, 0x2e, 0xf9, 0x0c, 0x8e];
const BITCOIN_TAG = [0x05, 0x88, 0x96, 0x0d, 0x73, 0xd7, 0x19, 0x01];
// Litecoin is not decoded: it is preserved as an unknown attestation.
const LITECOIN_TAG = [0x06, 0x86, 0x9a, 0x0d, 0x73, 0xd7, 0x1b, 0x45];
const attestation = (tag: number[], payload: Uint8Array) => cat([0x00], tag, varbytes(payload));
const pending = (uri: string) => attestation(PENDING_TAG, varbytes(ascii(uri)));
const bitcoin = (height: number) => attestation(BITCOIN_TAG, Uint8Array.from(varuint(height)));
const ALICE = "https://alice.btc.calendar.opentimestamps.org";
const BOB = "https://bob.btc.calendar.opentimestamps.org";
const leaf = pending(ALICE);

const CALENDARS: Record<string, { calendar: string; size: number }> = {
  "https://a.pool.opentimestamps.org": { calendar: ALICE, size: 207 },
  "https://b.pool.opentimestamps.org": { calendar: BOB, size: 275 },
  "https://a.pool.eternitywall.com": {
    calendar: "https://finney.calendar.eternitywall.com",
    size: 191,
  },
  "https://ots.btc.catallaxy.com": { calendar: "https://btc.calendar.catallaxy.com", size: 185 },
};
const digest = bytes(recorded.aggregators.digest);
const responses = Object.entries(recorded.aggregators.responses);
const aPool = bytes(recorded.aggregators.responses["https://a.pool.opentimestamps.org"]!.hex);
const A_POOL_COMMITMENT =
  "6adb2043525d01e35aee46666bb9cb53de3897d0a46696ce37e8ea2579b6e34196b9e0efa97b679145abfbe1";
const hello = bytes(recorded.hello_world_ots.hex);
const incompleteFile = bytes(recorded.incomplete_ots.hex);
const upgradeBytes = bytes(recorded.incomplete_alice_upgrade.hex);
const INCOMPLETE_DIGEST = "05c4f616a8e5310d19d938cfd769864d7f4ccdc2ca8b479b10af83564b097af9";
const INCOMPLETE_COMMITMENT =
  "57cfa5c46716df9bd9e83595bce439c58108d8fcc1678f30d4c6731c3f1fa6c79ed712c66fb1ac8d4e4eb0e7";

function rejects(run: () => unknown, reason: RegExp) {
  let caught: unknown;
  try {
    run();
  } catch (error) {
    caught = error;
  }
  expect(caught).toBeInstanceOf(OtsFormatError);
  expect((caught as Error).message).toMatch(reason);
}

/** Order-insensitive tree view: two trees are equal when their dumps are equal. */
interface Dump {
  readonly msg: string;
  readonly attestations: string[];
  readonly ops: Array<{ readonly op: string; readonly node: Dump }>;
}
function dump(node: OtsNode): Dump {
  return {
    msg: hex(node.msg),
    attestations: node.attestations
      .map((item) =>
        JSON.stringify(
          item.kind === "unknown" ? { tag: hex(item.tag), payload: hex(item.payload) } : item,
        ),
      )
      .sort(),
    ops: node.ops
      .map(([op, child]) => ({ op: `${op.tag}:${op.arg ? hex(op.arg) : ""}`, node: dump(child) }))
      .sort((left, right) => (left.op < right.op ? -1 : 1)),
  };
}
function bitcoinNodes(node: OtsNode): OtsNode[] {
  return [
    ...(node.attestations.some((item) => item.kind === "bitcoin") ? [node] : []),
    ...node.ops.flatMap(([, child]) => bitcoinNodes(child)),
  ];
}
const pendingNode = (uri: string): OtsNode => ({
  msg: new Uint8Array(32),
  attestations: [{ kind: "pending", uri }],
  ops: [],
});

describe("recorded OpenTimestamps fixtures", () => {
  it("are the real recorded bytes pinned by sha256 and size", () => {
    const pinned: Array<[Recorded, number]> = [
      ...responses.map(([url, item]): [Recorded, number] => [item, CALENDARS[url]!.size]),
      [recorded.hello_world_ots, 688],
      [recorded.incomplete_ots, 175],
      [recorded.incomplete_alice_upgrade, 699],
    ];
    expect(Object.keys(recorded.aggregators.responses).sort()).toEqual(
      Object.keys(CALENDARS).sort(),
    );
    for (const [item, size] of pinned) {
      const raw = bytes(item.hex);
      expect(raw.length).toBe(size);
      expect(createHash("sha256").update(raw).digest("hex")).toBe(item.sha256);
    }
    expect(recorded.hello_world_ots.sha256).toBe(
      "be61ecb940db2e4a6f89fbed59c8d4f7f74fa756cbc1fad1ad7aabcb2bf59c30",
    );
    expect(recorded.incomplete_ots.sha256).toBe(
      "95673f2878cbcfdddded530bd2ad5f3fb04e13d2e659760d7c1386346fdd036c",
    );
    expect(recorded.incomplete_alice_upgrade.sha256).toBe(
      "4acea6404115ad0fe73589dc1e2ebdd39752decac1120b7a35873ec518619e24",
    );
  });
});

describe("OTS codec", () => {
  it("round-trips each recorded aggregator response byte for byte", () => {
    for (const [url, item] of responses) {
      const response = bytes(item.hex);
      const node = parseTimestamp(response, digest);
      expect(hex(node.msg)).toBe(recorded.aggregators.digest);
      expect(hex(serializeTimestamp(node))).toBe(item.hex);
      const commitments = pendingCommitments(node);
      expect(commitments).toHaveLength(1);
      expect(commitments[0]!.uri).toBe(CALENDARS[url]!.calendar);
      expect(commitments[0]!.commitment).toHaveLength(44);
      expect(matchesCalendarWhitelist(commitments[0]!.uri)).toBe(true);
      expect(bitcoinHeights(node)).toEqual([]);
    }
    expect(hex(pendingCommitments(parseTimestamp(aPool, digest))[0]!.commitment)).toBe(
      A_POOL_COMMITMENT,
    );
  });

  it("builds and parses the detached receipt HEADER ‖ 01 ‖ 08 ‖ digest ‖ response", () => {
    for (const [, item] of responses) {
      const node = parseTimestamp(bytes(item.hex), digest);
      const file = detachedOts(digest, node);
      expect(hex(file)).toBe(hex(cat(HEADER, [0x01, 0x08], digest, bytes(item.hex))));
      const parsed = parseDetachedOts(file);
      expect(hex(parsed.digest)).toBe(recorded.aggregators.digest);
      expect(dump(parsed.node)).toEqual(dump(node));
    }
  });

  it("reads the upstream complete receipt: ripemd160 path, Bitcoin height 358391", () => {
    const { digest: fileDigest, node } = parseDetachedOts(hello);
    expect(hex(fileDigest)).toBe(
      "03ba204e50d126e4674c005e04d82e84c21366780af1f43bd54a37816b6ab340",
    );
    expect(hex(detachedOts(fileDigest, node))).toBe(recorded.hello_world_ots.hex);
    expect(bitcoinHeights(node)).toEqual([358391]);
    expect(pendingCommitments(node)).toEqual([]);
    const attested = bitcoinNodes(node);
    expect(attested).toHaveLength(1);
    // `ots` prints the merkle root in Bitcoin display order (b2lx: reversed bytes).
    expect(hex(Uint8Array.from(attested[0]!.msg).reverse())).toBe(
      "8a1b66ecb7cbd07d8139a7e7d7f2c41aab1f5009b8364aaf61d03ad245e47e00",
    );
  });

  it("merges the real alice upgrade into upstream incomplete.txt.ots → height 428648", () => {
    const incomplete = parseDetachedOts(incompleteFile);
    expect(hex(incomplete.digest)).toBe(INCOMPLETE_DIGEST);
    const commitments = pendingCommitments(incomplete.node);
    expect(commitments).toHaveLength(1);
    expect(commitments[0]!.uri).toBe(ALICE);
    const commitment = commitments[0]!.commitment;
    expect(hex(commitment)).toBe(INCOMPLETE_COMMITMENT);

    const upgrade = parseTimestamp(upgradeBytes, commitment);
    expect(hex(serializeTimestamp(upgrade))).toBe(recorded.incomplete_alice_upgrade.hex);
    expect(bitcoinHeights(upgrade)).toEqual([428648]);

    const merged = mergeAt(incomplete.node, commitment, upgrade);
    expect(bitcoinHeights(merged)).toEqual([428648]);
    expect(bitcoinHeights(incomplete.node)).toEqual([]); // a new tree; the input is untouched
    const file = detachedOts(incomplete.digest, merged);
    // The final `00 pending` item becomes `ff 00 pending` followed by the upgrade's ops.
    const cut = incompleteFile.length - leaf.length;
    expect(hex(file)).toBe(
      hex(cat(incompleteFile.subarray(0, cut), [0xff], incompleteFile.subarray(cut), upgradeBytes)),
    );
    const reparsed = parseDetachedOts(file);
    expect(hex(reparsed.digest)).toBe(INCOMPLETE_DIGEST);
    expect(dump(reparsed.node)).toEqual(dump(merged));
    expect(hex(detachedOts(incomplete.digest, mergeAt(merged, commitment, upgrade)))).toBe(
      hex(file),
    );
  });

  it("refuses to merge at a commitment absent from the tree or a mismatched upgrade", () => {
    const incomplete = parseDetachedOts(incompleteFile).node;
    const upgrade = parseTimestamp(upgradeBytes, bytes(INCOMPLETE_COMMITMENT));
    rejects(() => mergeAt(incomplete, bytes(A_POOL_COMMITMENT), upgrade), /commitment/);
    rejects(
      () => mergeAt(incomplete, bytes(INCOMPLETE_COMMITMENT), parseTimestamp(aPool, digest)),
      /commitment/,
    );
  });

  it("preserves unknown attestation tags byte-exact", () => {
    const raw = attestation([1, 2, 3, 4, 5, 6, 7, 8], ascii("opaque payload"));
    const node = parseTimestamp(raw, digest);
    expect(node.attestations).toHaveLength(1);
    expect(node.attestations[0]!.kind).toBe("unknown");
    expect(hex(serializeTimestamp(node))).toBe(hex(raw));
  });

  it("orders attestations as python TimeAttestation.__lt__ and ops by (tag, arg)", () => {
    const heights = cat([0xff], bitcoin(255), bitcoin(256));
    const byHeight: OtsNode = {
      msg: digest,
      attestations: [
        { kind: "bitcoin", height: 256 },
        { kind: "bitcoin", height: 255 },
      ],
      ops: [],
    };
    expect(hex(serializeTimestamp(byHeight))).toBe(hex(heights)); // integer, not varuint bytes
    expect(bitcoinHeights(parseTimestamp(heights, digest))).toEqual([255, 256]);
    expect(hex(serializeTimestamp(parseTimestamp(heights, digest)))).toBe(hex(heights));

    const uris = cat([0xff], pending(ALICE), pending(BOB));
    const byUri: OtsNode = {
      msg: digest,
      attestations: [
        { kind: "pending", uri: BOB },
        { kind: "pending", uri: ALICE },
      ],
      ops: [],
    };
    expect(hex(serializeTimestamp(byUri))).toBe(hex(uris));
    expect(hex(serializeTimestamp(parseTimestamp(uris, digest)))).toBe(hex(uris));

    const mixed: OtsNode = {
      msg: digest,
      attestations: [
        { kind: "pending", uri: ALICE },
        { kind: "unknown", tag: Uint8Array.from(LITECOIN_TAG), payload: Uint8Array.of(2) },
        { kind: "bitcoin", height: 1 },
        { kind: "unknown", tag: Uint8Array.from(LITECOIN_TAG), payload: Uint8Array.of(1) },
      ],
      ops: [
        [{ tag: 0xf0, arg: Uint8Array.of(1) }, pendingNode(ALICE)],
        [{ tag: 0x08 }, pendingNode(ALICE)],
        [{ tag: 0xf0, arg: Uint8Array.of(0) }, pendingNode(ALICE)],
      ],
    };
    const expected = cat(
      [0xff],
      bitcoin(1),
      [0xff],
      attestation(LITECOIN_TAG, Uint8Array.of(1)),
      [0xff],
      attestation(LITECOIN_TAG, Uint8Array.of(2)),
      [0xff],
      pending(ALICE),
      [0xff, 0x08],
      leaf,
      [0xff, 0xf0],
      varbytes(Uint8Array.of(0)),
      leaf,
      [0xf0],
      varbytes(Uint8Array.of(1)),
      leaf,
    );
    expect(hex(serializeTimestamp(mixed))).toBe(hex(expected));
    expect(hex(serializeTimestamp(parseTimestamp(expected, digest)))).toBe(hex(expected));
  });

  it("accepts nesting depth 256 and refuses an empty node", () => {
    const tower = cat(new Array<number>(255).fill(0x08), leaf);
    expect(hex(serializeTimestamp(parseTimestamp(tower, digest)))).toBe(hex(tower));
    rejects(() => serializeTimestamp({ msg: digest, attestations: [], ops: [] }), /empty/);
  });

  it("fails closed on unsupported, oversized, deep, trailing or truncated input", () => {
    const fill = (length: number) => new Uint8Array(length).fill(0x61);
    const cases: Array<[Uint8Array, RegExp]> = [
      [cat([0x02], leaf), /unsupported op/], // sha1
      [cat([0x67], leaf), /unsupported op/], // keccak256
      [cat([0xf2], leaf), /unsupported op/], // reverse
      [cat([0xf3], leaf), /unsupported op/], // hexlify
      [cat([0x55], leaf), /unsupported op/],
      [cat([0xf0], varuint(0), leaf), /argument length/],
      [cat([0xf0], varbytes(fill(4097)), leaf), /argument length/],
      [cat([0xf1], varbytes(fill(4097)), leaf), /argument length/],
      [cat([0xf0], varbytes(fill(4096)), leaf), /message length/],
      [attestation([1, 2, 3, 4, 5, 6, 7, 8], fill(8193)), /payload length/],
      [pending(`https://${"a".repeat(993)}`), /pending uri/], // 1001 bytes
      [pending(`${ALICE}?x=1`), /pending uri/],
      [pending(`${ALICE} x`), /pending uri/],
      [attestation(PENDING_TAG, cat(varbytes(ascii(ALICE)), [0x00])), /trailing/],
      [attestation(BITCOIN_TAG, Uint8Array.of(0x01, 0x00)), /trailing/],
      [attestation(BITCOIN_TAG, Uint8Array.of(...new Array<number>(7).fill(255), 127)), /varuint/],
      [cat(new Array<number>(256).fill(0x08), leaf), /depth/], // 257 nested nodes
      [cat(aPool, [0x00]), /trailing/],
      [aPool.subarray(0, aPool.length - 1), /truncated/],
      [new Uint8Array(), /truncated/],
      [Uint8Array.of(0xf0, 0x80), /truncated/],
    ];
    for (const [input, reason] of cases) rejects(() => parseTimestamp(input, digest), reason);
    rejects(() => parseTimestamp(leaf, new Uint8Array(4097)), /message length/);
  });

  it("fails closed on detached header, version, file-hash op and digest errors", () => {
    rejects(() => parseDetachedOts(cat([0x01], hello.subarray(1))), /header/);
    rejects(() => parseDetachedOts(cat(HEADER, [0x02], hello.subarray(32))), /version/);
    rejects(() => parseDetachedOts(cat(HEADER, [0x01, 0x03], hello.subarray(33))), /file hash op/);
    rejects(() => parseDetachedOts(HEADER), /truncated/);
    rejects(() => parseDetachedOts(cat(hello, [0x00])), /trailing/);
    const node = parseTimestamp(aPool, digest);
    rejects(() => detachedOts(digest.subarray(1), node), /digest/);
    rejects(() => detachedOts(bytes(INCOMPLETE_DIGEST), node), /digest/);
  });
});

describe("calendar whitelist and aggregators", () => {
  it("allows only https origins on the three official calendar domains", () => {
    for (const uri of [
      ALICE,
      "https://finney.calendar.eternitywall.com",
      "https://btc.calendar.catallaxy.com",
    ]) {
      expect(matchesCalendarWhitelist(uri)).toBe(true);
    }
    for (const uri of [
      "http://alice.btc.calendar.opentimestamps.org",
      "https://calendar.opentimestamps.org.evil.com",
      "https://evil.com/x.calendar.opentimestamps.org",
      "https://a.calendar.opentimestamps.org:8443",
      "https://u@alice.btc.calendar.opentimestamps.org",
      "https://alice.btc.calendar.opentimestamps.org/x",
      "https://alice.btc.calendar.opentimestamps.org/",
      "https://alice.btc.calendar.opentimestamps.org?x",
      "https://a.pool.opentimestamps.org",
      "https://",
      "",
    ]) {
      expect(matchesCalendarWhitelist(uri)).toBe(false);
    }
  });

  it("pins the four default aggregators", () => {
    expect(OTS_AGGREGATORS).toEqual([
      "https://a.pool.opentimestamps.org",
      "https://b.pool.opentimestamps.org",
      "https://a.pool.eternitywall.com",
      "https://ots.btc.catallaxy.com",
    ]);
  });
});

describe("mergedReceipt (C11)", () => {
  const submitted = responses.map(([calendar, item]) => ({
    calendar,
    status: "submitted" as const,
    ots: detachedOts(digest, parseTimestamp(bytes(item.hex), digest)),
  }));

  it("merges one submitted receipt per calendar at the root node", () => {
    const out = mergedReceipt(submitted);
    expect(out).not.toBeNull();
    const merged = parseDetachedOts(out!);
    expect(hex(merged.digest)).toBe(recorded.aggregators.digest);
    expect(merged.node.ops).toHaveLength(4);
    expect(merged.node.attestations).toEqual([]);
    expect(
      pendingCommitments(merged.node)
        .map((item) => item.uri)
        .sort(),
    ).toEqual(
      Object.values(CALENDARS)
        .map((item) => item.calendar)
        .sort(),
    );
    expect(hex(mergedReceipt([...submitted].reverse())!)).toBe(hex(out!));
  });

  it("prefers the upgraded row, ignores failed rows and rows without receipts", () => {
    const incomplete = parseDetachedOts(incompleteFile);
    const commitment = bytes(INCOMPLETE_COMMITMENT);
    const upgraded = detachedOts(
      incomplete.digest,
      mergeAt(incomplete.node, commitment, parseTimestamp(upgradeBytes, commitment)),
    );
    const calendar = "https://a.pool.opentimestamps.org";
    expect(
      hex(
        mergedReceipt([
          { calendar, status: "submitted", ots: incompleteFile },
          { calendar, status: "upgraded", ots: upgraded },
        ])!,
      ),
    ).toBe(hex(upgraded));
    // Unparseable bytes prove the submitted and failed rows are never read.
    expect(
      hex(
        mergedReceipt([
          { calendar, status: "submitted", ots: Uint8Array.of(1, 2, 3) },
          { calendar, status: "upgraded", ots: upgraded },
          {
            calendar: "https://b.pool.opentimestamps.org",
            status: "failed",
            ots: Uint8Array.of(9),
          },
          { calendar: "https://a.pool.eternitywall.com", status: "submitted", ots: null },
        ])!,
      ),
    ).toBe(hex(upgraded));
    expect(mergedReceipt([])).toBeNull();
    expect(
      mergedReceipt([
        { calendar, status: "failed", ots: null },
        { calendar: "https://ots.btc.catallaxy.com", status: "failed", ots: incompleteFile },
      ]),
    ).toBeNull();
  });

  it("throws when rows commit to different digests", () => {
    rejects(
      () =>
        mergedReceipt([
          submitted[0]!,
          {
            calendar: "https://b.pool.opentimestamps.org",
            status: "submitted",
            ots: incompleteFile,
          },
        ]),
      /digest/,
    );
  });
});

describe("package entry", () => {
  it("re-exports the codec", () => {
    const codec = {
      OTS_AGGREGATORS,
      OtsFormatError,
      bitcoinHeights,
      detachedOts,
      matchesCalendarWhitelist,
      mergeAt,
      mergedReceipt,
      parseDetachedOts,
      parseTimestamp,
      pendingCommitments,
      serializeTimestamp,
    };
    for (const [name, value] of Object.entries(codec)) {
      expect(identity[name as keyof typeof identity]).toBe(value);
    }
  });
});
