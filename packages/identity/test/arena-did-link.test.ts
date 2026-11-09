import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import {
  ARENA_FORECAST_DOMAIN,
  DID_LINK_FORMAT,
  MAX_ACTIVE_DID_LINKS,
  activeDidLinks,
  arenaForecastSigningMessage,
  buildDidDocument,
  buildDidHistory,
  createVerifyNonce,
  didLinkSigningBytes,
  popPreimage,
  requestSigningMessage,
  signEd25519,
  validateDidLinkStatement,
  verifyEd25519,
} from "../src/index.js";
import type { DidLinkStatement, Ed25519PublicJwk, PublicKeyRecord } from "../src/index.js";
import file from "./arena-did-link-vectors.json" with { type: "json" };
import requestFile from "./request-signing-vectors.json" with { type: "json" };
import standards from "./standards-vectors.json" with { type: "json" };

// RESEARCH F12 anchors (RFC 8032 §7.1 test-1 key): the parent fill must reproduce them.
const ARENA_SIG =
  "o5++WnXtH9SlR6StgSF9uCpR7W1l1n6O6Q37yoh4IbZZpcwBMbBDqllNn71jg7Ch75IIP5E+kE49ZKS7psPQBQ==";
const LINK_SIG =
  "dQUF5IyM2R5o7lThd6Aslaza9pFGrmcWVTMzwoT5rho0Nqef4q2RXcMQPQUVYWqgayn113ZkUIgf67-WO0LxCA";
const UNLINK_SIG =
  "byyXfGxWKa-ypAFWVE_4Q0HaK7vZQZrdGDMjbVsjmpXux_ttfJUYWNfmNfPWxsUMmC7sb1awd87kxedoQ4gcDw";
const PKCS8_PREFIX = "302e020100300506032b657004220420";
const PREFIX = "agentland-arena-forecast/1\n";

interface ArenaVector {
  name: string;
  method: string;
  request_target: string;
  timestamp: string;
  raw_body_b64: string;
  body_sha256_hex: string;
  message_utf8: string;
  signature_b64: string | null;
}
interface TamperEntry {
  name: string;
  base?: string;
  base_public?: string;
  message_utf8: string;
  signature_b64: string | null;
}
interface LinkVector {
  name: string;
  statement: DidLinkStatement;
  canonical_utf8: string;
  signature: string | null;
}
interface ValidationEntry {
  name: string;
  statement: DidLinkStatement;
  now: string;
  active_links: string[];
  error: "TypeError" | "RangeError" | null;
}
interface ActiveEntry {
  name: string;
  history: DidLinkStatement[];
  expected: string[];
}
interface AlsoKnownAsEntry {
  name: string;
  handle: string;
  links: string[];
  expected: string[];
}
interface VectorFile {
  private_pkcs8_b64: string;
  public_jwk: Ed25519PublicJwk;
  arena_forecast: { prefix_utf8: string; vectors: ArenaVector[]; tamper: TamperEntry[] };
  did_link: {
    agent_did: string;
    now: string;
    vectors: LinkVector[];
    validation: ValidationEntry[];
    active: ActiveEntry[];
    also_known_as: AlsoKnownAsEntry[];
  };
}
interface RequestVector {
  name: string;
  method: string;
  request_target: string;
  timestamp: string;
  raw_body_b64: string;
  message_utf8: string;
  signature_b64: string;
}

const data = file as unknown as VectorFile;
const requestVectors = (requestFile as unknown as { vectors: RequestVector[] }).vectors;
const forecastSubmit = requestVectors.find((vector) => vector.name === "forecast-submit")!;
const arena = data.arena_forecast.vectors[0]!;
const [unprefixedTamper, prefixedTamper] = data.arena_forecast.tamper;
const linkVector = data.did_link.vectors.find((vector) => vector.name === "link")!;
const unlinkVector = data.did_link.vectors.find((vector) => vector.name === "unlink")!;
const agent = data.did_link.agent_did;
const pkcs8 = new Uint8Array(Buffer.from(data.private_pkcs8_b64, "base64"));
const jwk = data.public_jwk;
const record: PublicKeyRecord = {
  id: "did:web:agentland.us:agents:weatherwise#key-1",
  publicKeyJwk: jwk,
  purpose: "signing",
  activated_at: "2026-10-01T00:00:00.000Z",
};
const PROFILE = "https://agentland.us/agents/weatherwise/did.json";

const inputOf = (vector: {
  method: string;
  request_target: string;
  timestamp: string;
  raw_body_b64: string;
}) => ({
  method: vector.method,
  requestTarget: vector.request_target,
  timestamp: vector.timestamp,
  rawBody: new Uint8Array(Buffer.from(vector.raw_body_b64, "base64")),
});
const utf8 = (text: string) => new Uint8Array(Buffer.from(text, "utf8"));
const toUrl = (padded: string) => Buffer.from(padded, "base64").toString("base64url");
const flipFirst = (bytes: Uint8Array) => {
  const copy = new Uint8Array(bytes);
  copy[0] = copy[0]! ^ 0x01;
  return copy;
};
// Class and message both, so a missing export ("is not a function") cannot pass.
const throws = (run: () => unknown, cls: typeof TypeError | typeof RangeError, message: RegExp) => {
  expect(run).toThrow(cls);
  expect(run).toThrow(message);
};
const OTHER_AGENT = /^DID link statement is for another agent$/;
const NOT_AGENTLAND = /^Linked DID must not be an AgentLand DID$/;
const ABNF = /^Linked DID must match DID Core syntax$/;
const VALIDATION_MESSAGES: Record<string, RegExp> = {
  "N1-own-did": /^Linked DID must not be the agent DID$/,
  "N2-agentland-agent": NOT_AGENTLAND,
  "N2-agentland-platform": NOT_AGENTLAND,
  "N2-agentland-host-case": NOT_AGENTLAND,
  "N3-abnf-method-case": ABNF,
  "N3-abnf-empty-id": ABNF,
  "N3-abnf-space": ABNF,
  "N4-ninth-active": /^At most 8 active DID links$/,
  "N5-unlink-inactive": /^DID is not linked$/,
  "N6-non-ascii": ABNF,
  "X-stale-future": /^DID link statement is not within 5 minutes$/,
  "X-stale-past": /^DID link statement is not within 5 minutes$/,
  "X-relink": /^DID is already linked$/,
  "X-did-url": ABNF,
  "X-wrong-did": OTHER_AGENT,
  "X-format": /^agentland-did-link\/1 format required$/,
  "X-action": /^DID link action must be link or unlink$/,
  "X-timestamp": /^UTC millisecond timestamp required$/,
};
const sortedJson = (statement: DidLinkStatement) =>
  JSON.stringify(
    Object.fromEntries(
      Object.keys(statement)
        .sort()
        .map((key) => [key, statement[key as keyof DidLinkStatement]]),
    ),
  );

describe("vectors file", () => {
  it("shape and key", () => {
    expect(Object.keys(data).sort()).toEqual(
      ["arena_forecast", "attribution", "did_link", "private_pkcs8_b64", "public_jwk"].sort(),
    );
    expect(Buffer.from(pkcs8).toString("hex")).toBe(PKCS8_PREFIX + standards.ed25519[0]!.seed);
    expect(jwk.x).toBe(Buffer.from(standards.ed25519[0]!.public, "hex").toString("base64url"));
    expect(data.arena_forecast.prefix_utf8).toBe(PREFIX);
    for (const entry of data.did_link.validation)
      expect([null, "TypeError", "RangeError"]).toContain(entry.error);
    const names = data.did_link.validation.map((entry) => entry.name);
    for (const prefix of ["N1-", "N2-", "N3-", "N4-", "N5-", "N6-"])
      expect(names.some((name) => name.startsWith(prefix))).toBe(true);
  });

  it("signatures are filled and equal the F12 anchors", () => {
    expect(arena.signature_b64).toBe(ARENA_SIG);
    expect(unprefixedTamper!.signature_b64).toBe(ARENA_SIG);
    expect(prefixedTamper!.signature_b64).toBe(forecastSubmit.signature_b64);
    expect(linkVector.signature).toBe(LINK_SIG);
    expect(unlinkVector.signature).toBe(UNLINK_SIG);
  });
});

describe("arena forecast domain", () => {
  it("prefix bytes", () => {
    expect(ARENA_FORECAST_DOMAIN).toBe("agentland-arena-forecast/1");
    for (const vector of [arena, ...requestVectors]) {
      const input = inputOf(vector);
      expect(Buffer.from(arenaForecastSigningMessage(input))).toEqual(
        Buffer.concat([Buffer.from(PREFIX), Buffer.from(requestSigningMessage(input))]),
      );
    }
    expect(Buffer.from(arenaForecastSigningMessage(inputOf(arena))).toString("utf8")).toBe(
      arena.message_utf8,
    );
  });

  it("signature reproduces", () => {
    const message = arenaForecastSigningMessage(inputOf(arena));
    const signature = signEd25519(message, pkcs8);
    expect(Buffer.from(signature, "base64url").toString("base64")).toBe(ARENA_SIG);
    expect(verifyEd25519(message, toUrl(ARENA_SIG), jwk)).toBe(true);
  });

  it("domains are disjoint", () => {
    const message = arenaForecastSigningMessage(inputOf(arena));
    expect(verifyEd25519(utf8(unprefixedTamper!.message_utf8), toUrl(ARENA_SIG), jwk)).toBe(false);
    expect(verifyEd25519(flipFirst(message), toUrl(ARENA_SIG), jwk)).toBe(false);
    expect(prefixedTamper!.message_utf8).toBe(PREFIX + forecastSubmit.message_utf8);
    const publicSig = toUrl(forecastSubmit.signature_b64);
    expect(verifyEd25519(utf8(prefixedTamper!.message_utf8), publicSig, jwk)).toBe(false);
    expect(verifyEd25519(requestSigningMessage(inputOf(forecastSubmit)), publicSig, jwk)).toBe(
      true,
    );
    expect(String.fromCharCode(message[0]!)).toBe("a");
    expect(message[0]).not.toBe("{".charCodeAt(0));
    const nonce = createVerifyNonce(new Uint8Array(32));
    const pop = Buffer.from(popPreimage({ did: agent, nonce })).toString("utf8");
    expect(pop.startsWith(PREFIX)).toBe(false);
    expect(nonce.startsWith(PREFIX)).toBe(false);
    expect(PREFIX.startsWith("agentland-pop/1\n")).toBe(false);
    expect(PREFIX.startsWith("agentland-verify/1:")).toBe(false);
  });

  it("no normalization", () => {
    const text = Buffer.from(
      arenaForecastSigningMessage({ ...inputOf(arena), method: "post" }),
    ).toString("utf8");
    expect(text.startsWith(`${PREFIX}post\n`)).toBe(true);
  });
});

describe("did link statement", () => {
  it("format constants", () => {
    expect(DID_LINK_FORMAT).toBe("agentland-did-link/1");
    expect(MAX_ACTIVE_DID_LINKS).toBe(8);
  });

  it("canonical bytes and signatures", () => {
    for (const [vector, anchor] of [
      [linkVector, LINK_SIG],
      [unlinkVector, UNLINK_SIG],
    ] as const) {
      const bytes = didLinkSigningBytes(vector.statement);
      expect(Buffer.from(bytes).toString("utf8")).toBe(vector.canonical_utf8);
      expect(Buffer.from(bytes).toString("utf8")).toBe(sortedJson(vector.statement));
      expect(signEd25519(bytes, pkcs8)).toBe(anchor);
      expect(verifyEd25519(bytes, anchor, jwk)).toBe(true);
      expect(verifyEd25519(flipFirst(bytes), anchor, jwk)).toBe(false);
    }
  });

  it("refuses malformed statements", () => {
    const missingFormat: Partial<DidLinkStatement> = { ...linkVector.statement };
    delete missingFormat.format;
    const bad: [unknown, RegExp][] = [
      [{ ...linkVector.statement, extra: 1 }, /^Unexpected or missing members$/],
      [missingFormat, /^Unexpected or missing members$/],
      [
        { ...linkVector.statement, format: "agentland-did-link/2" },
        /^agentland-did-link\/1 format required$/,
      ],
      [{ ...linkVector.statement, action: "relink" }, /^DID link action must be link or unlink$/],
    ];
    for (const [statement, message] of bad)
      throws(() => didLinkSigningBytes(statement as DidLinkStatement), TypeError, message);
  });
});

describe("did link validation", () => {
  for (const entry of data.did_link.validation) {
    it(entry.name, () => {
      const run = () =>
        validateDidLinkStatement(entry.statement, {
          agentDid: agent,
          now: new Date(entry.now),
          activeLinks: entry.active_links,
        });
      if (entry.error === null) expect(run()).toBeUndefined();
      else
        throws(
          run,
          entry.error === "TypeError" ? TypeError : RangeError,
          VALIDATION_MESSAGES[entry.name]!,
        );
      expect(VALIDATION_MESSAGES[entry.name] === undefined).toBe(entry.error === null);
    });
  }

  it("512 bytes is the limit", () => {
    const ctx = { agentDid: agent, now: new Date(data.did_link.now), activeLinks: [] };
    const at = (linked_did: string) => ({ ...linkVector.statement, linked_did });
    expect(validateDidLinkStatement(at(`did:web:${"a".repeat(504)}`), ctx)).toBeUndefined();
    throws(
      () => validateDidLinkStatement(at(`did:web:${"a".repeat(505)}`), ctx),
      TypeError,
      /^Linked DID exceeds 512 bytes$/,
    );
  });

  it("invalid now", () => {
    throws(
      () =>
        validateDidLinkStatement(linkVector.statement, {
          agentDid: agent,
          now: new Date(Number.NaN),
          activeLinks: [],
        }),
      TypeError,
      /^Valid now required$/,
    );
  });
});

describe("active links", () => {
  for (const entry of data.did_link.active) {
    it(entry.name, () => {
      expect(activeDidLinks(entry.history.map((statement) => ({ statement })))).toEqual(
        entry.expected,
      );
    });
  }

  it("inconsistent histories throw", () => {
    const at = (action: "link" | "unlink", timestamp: string): DidLinkStatement => ({
      ...linkVector.statement,
      action,
      linked_did: "did:example:alpha",
      timestamp,
    });
    const histories: [DidLinkStatement[], RegExp][] = [
      [[at("unlink", "2026-11-01T12:00:00.000Z")], /^Inconsistent DID link history$/],
      [
        [at("link", "2026-11-01T12:00:00.000Z"), at("link", "2026-11-01T12:01:00.000Z")],
        /^Inconsistent DID link history$/,
      ],
      [
        [{ ...at("link", "2026-11-01T12:00:00.000Z"), format: "x" as "agentland-did-link/1" }],
        /^agentland-did-link\/1 format required$/,
      ],
    ];
    for (const [history, message] of histories)
      throws(() => activeDidLinks(history.map((statement) => ({ statement }))), TypeError, message);
  });
});

describe("alsoKnownAs", () => {
  for (const entry of data.did_link.also_known_as) {
    it(entry.name, () => {
      expect(
        buildDidDocument({ handle: entry.handle, keys: [record], links: entry.links }).alsoKnownAs,
      ).toEqual(entry.expected);
    });
  }

  it("unchanged without links", () => {
    const plain = buildDidDocument({ handle: "weatherwise", keys: [record] });
    expect(JSON.stringify(plain)).toBe(
      JSON.stringify(buildDidDocument({ handle: "weatherwise", keys: [record], links: [] })),
    );
    expect(plain.alsoKnownAs).toEqual([PROFILE]);
  });

  it("refused links", () => {
    const nine = Array.from({ length: 9 }, (_, index) => `did:example:link${index + 1}`);
    const refused: [string[], RegExp][] = [
      [[agent], /^Linked DID must not be the agent DID$/],
      [["did:web:agentland.us:agents:other"], /^Linked DID must not be an AgentLand DID$/],
      [["did:Web:x"], /^Linked DID must match DID Core syntax$/],
      [
        ["did:example:alpha", "did:example:alpha"],
        /^Links must be an array of at most 8 unique DIDs$/,
      ],
      [nine, /^Links must be an array of at most 8 unique DIDs$/],
    ];
    for (const [links, message] of refused)
      throws(
        () => buildDidDocument({ handle: "weatherwise", keys: [record], links }),
        TypeError,
        message,
      );
  });
});

describe("did history links", () => {
  const linkRecord = { statement: linkVector.statement, signature: LINK_SIG };
  const unlinkRecord = { statement: unlinkVector.statement, signature: UNLINK_SIG };
  const history = (
    links: readonly { statement: DidLinkStatement; signature: string }[],
    keys: PublicKeyRecord[] = [record],
  ) => buildDidHistory({ handle: "weatherwise", keys, rotations: [], links });

  it("orders and verifies link entries", () => {
    expect(history([unlinkRecord, linkRecord]).links).toEqual([linkRecord, unlinkRecord]);
  });

  it("refuses inactive keys, bad signatures, other agents and inconsistent histories", () => {
    const late: PublicKeyRecord = { ...record, activated_at: "2026-11-01T12:00:00.001Z" };
    const badSignature = /^Invalid or inactive DID link signature$/;
    throws(() => history([linkRecord], [late]), TypeError, badSignature);
    const flipped = Buffer.from(LINK_SIG, "base64url");
    flipped[0] = flipped[0]! ^ 0x01;
    throws(
      () => history([{ ...linkRecord, signature: flipped.toString("base64url") }]),
      TypeError,
      badSignature,
    );
    const other = { ...linkVector.statement, did: "did:web:agentland.us:agents:other" };
    throws(
      () =>
        history([{ statement: other, signature: signEd25519(didLinkSigningBytes(other), pkcs8) }]),
      TypeError,
      OTHER_AGENT,
    );
    throws(() => history([unlinkRecord]), TypeError, /^Inconsistent DID link history$/);
  });

  it("no links member without a links input", () => {
    const plain = buildDidHistory({ handle: "weatherwise", keys: [record], rotations: [] });
    expect(Object.hasOwn(plain, "links")).toBe(false);
  });
});

describe("spec", () => {
  it("documents DID links", () => {
    const spec = readFileSync(new URL("../spec/agentland-did-1.md", import.meta.url), "utf8");
    expect(spec).toContain("agentland-did-link/1");
    expect(spec).toContain("**DID link:**");
    expect(spec).toContain("- `links`:");
    expect(spec).not.toContain(
      '- `alsoKnownAs`: `["https://agentland.us/agents/<handle>/did.json"]`.',
    );
  });
});
