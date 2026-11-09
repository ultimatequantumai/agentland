import { createPrivateKey, sign } from "node:crypto";
import { readFileSync } from "node:fs";
import { describe, expect, it, vi } from "vitest";
import { issueCredential, verifyCredential } from "../src/index.js";
import { Ed25519UnsupportedError, verifyCredentialWeb } from "../src/web.js";
import { did, testKey, timestamp } from "./helpers.js";
import { fixtureRoot } from "./fixtures/oracle.js";

// D-36 / UI-SPEC OQ-5: the visitor's browser is the verifier, so the WebCrypto path must return
// exactly what the Node verifier returns for every fixture, failure reasons included.
const key = testKey();
const issuer = "did:web:agentland.us";
const kid = `${issuer}#vc-1`;
const other = "did:web:agentland.us:agents:another";
const validUntil = "2026-02-01T00:00:00.000Z";
const schema = "invalid-schema-or-trust-pins";
const input = {
  id: "urn:uuid:01a1e5f0-7c3d-7e2a-8b4c-5d6e7f8091a2",
  subjectDid: did,
  type: "Calibrated" as const,
  evidence: { season: "alltime", n: 200, shrunk_edge: 0.025, audit_root: fixtureRoot },
  validFrom: timestamp,
  validUntil,
  issuerKeyId: kid,
  privatePkcs8: key.privatePkcs8,
};
type Options = Parameters<typeof verifyCredential>[1];
const options: Options = {
  trustedIssuer: { issuer, kid, publicKeyJwk: key.publicKeyJwk },
  expectedSubjectDid: did,
  now: timestamp,
};
const valid = issueCredential(input);
const [first, second, signature] = valid.split(".") as [string, string, string];
const header = { alg: "Ed25519", kid, typ: "vc+jwt", cty: "vc" };
const payload = JSON.parse(Buffer.from(second, "base64url").toString()) as Record<string, unknown>;

/** Independently signed with node:crypto over arbitrary (non-canonical) header/payload bytes. */
function signedRaw(protectedHeader: unknown, body: unknown): string {
  const encode = (value: unknown) =>
    Buffer.from(typeof value === "string" ? value : JSON.stringify(value)).toString("base64url");
  const wire = `${encode(protectedHeader)}.${encode(body)}`;
  const privateKey = createPrivateKey({ key: key.privatePkcs8, format: "der", type: "pkcs8" });
  return `${wire}.${sign(null, Buffer.from(wire, "ascii"), privateKey).toString("base64url")}`;
}
function flippedSignature(): string {
  const bytes = Buffer.from(signature, "base64url");
  bytes[0] = bytes[0]! ^ 0x01;
  return `${first}.${second}.${bytes.toString("base64url")}`;
}

const rows: readonly {
  readonly name: string;
  readonly compact: string;
  readonly options: Options;
  readonly reason: string | null;
}[] = [
  { name: "valid", compact: valid, options, reason: null },
  {
    name: "valid without validUntil, far-future now",
    compact: issueCredential({ ...input, validUntil: undefined }),
    options: { ...options, now: "2099-01-01T00:00:00.000Z" },
    reason: null,
  },
  {
    name: "valid on the last millisecond before validUntil",
    compact: valid,
    options: { ...options, now: "2026-01-31T23:59:59.999Z" },
    reason: null,
  },
  {
    name: "signature byte flipped",
    compact: flippedSignature(),
    options,
    reason: "invalid-signature",
  },
  {
    name: "signed by another key",
    compact: issueCredential({ ...input, privatePkcs8: testKey(1).privatePkcs8 }),
    options,
    reason: "invalid-signature",
  },
  {
    // Undecodable signature segment: both verifiers treat it as "not verified", not schema.
    name: "signature segment is not 64 base64url bytes",
    compact: `${first}.${second}.A`,
    options,
    reason: "invalid-signature",
  },
  {
    name: "header kid #vc-2 with trusted kid #vc-1",
    compact: issueCredential({ ...input, issuerKeyId: `${issuer}#vc-2` }),
    options,
    reason: "untrusted-protected-header",
  },
  {
    name: "header alg EdDSA",
    compact: signedRaw({ ...header, alg: "EdDSA" }, payload),
    options,
    reason: "untrusted-protected-header",
  },
  {
    name: "credential for another subject",
    compact: issueCredential({ ...input, subjectDid: other }),
    options,
    reason: "subject-mismatch",
  },
  {
    name: "expected subject is another DID",
    compact: valid,
    options: { ...options, expectedSubjectDid: other },
    reason: "subject-mismatch",
  },
  {
    name: "now before validFrom",
    compact: valid,
    options: { ...options, now: "2025-12-31T23:59:59.999Z" },
    reason: "outside-validity-period",
  },
  {
    name: "now at validUntil",
    compact: valid,
    options: { ...options, now: validUntil },
    reason: "outside-validity-period",
  },
  {
    name: "signed payload with an extra member",
    compact: signedRaw(header, { ...payload, extra: true }),
    options,
    reason: schema,
  },
  {
    name: "signed payload with a duplicate member",
    compact: signedRaw(header, '{"issuer":"a","issuer":"b"}'),
    options,
    reason: schema,
  },
  { name: "three dots", compact: "...", options, reason: schema },
  { name: "three-segment garbage", compact: "abc.def.ghi", options, reason: schema },
  { name: "two segments", compact: `${first}.${second}`, options, reason: schema },
  { name: "non-string compact", compact: 42 as unknown as string, options, reason: schema },
  {
    name: "trusted key carries a private member",
    compact: valid,
    options: {
      ...options,
      trustedIssuer: {
        ...options.trustedIssuer,
        publicKeyJwk: {
          ...key.publicKeyJwk,
          d: "secret",
        } as Options["trustedIssuer"]["publicKeyJwk"],
      },
    },
    reason: schema,
  },
  {
    name: "trusted issuer is not AgentLand",
    compact: valid,
    options: {
      ...options,
      trustedIssuer: { ...options.trustedIssuer, issuer: "did:web:evil.test" },
    },
    reason: schema,
  },
  {
    name: "now is not a valid instant",
    compact: valid,
    options: { ...options, now: "2026-02-30T00:00:00.000Z" },
    reason: schema,
  },
];

describe("verifyCredentialWeb parity with verifyCredential", () => {
  it.each(rows)("$name", async ({ compact, options: pins, reason }) => {
    const node = verifyCredential(compact, pins);
    expect(node).toStrictEqual(
      reason === null
        ? {
            valid: true,
            credential: JSON.parse(Buffer.from(compact.split(".")[1]!, "base64url").toString()),
          }
        : { valid: false, error: { stage: "credential", reason } },
    );
    expect(await verifyCredentialWeb(compact, pins)).toStrictEqual(node);
  });

  it("throws Ed25519UnsupportedError when WebCrypto lacks Ed25519", async () => {
    try {
      vi.stubGlobal("crypto", {});
      await expect(verifyCredentialWeb(valid, options)).rejects.toBeInstanceOf(
        Ed25519UnsupportedError,
      );
      vi.stubGlobal("crypto", {
        subtle: {
          importKey: () =>
            Promise.reject(new DOMException("Unrecognized algorithm name", "NotSupportedError")),
          verify: () =>
            Promise.reject(new DOMException("Unrecognized algorithm name", "NotSupportedError")),
        },
      });
      await expect(verifyCredentialWeb(valid, options)).rejects.toBeInstanceOf(
        Ed25519UnsupportedError,
      );
    } finally {
      vi.unstubAllGlobals();
    }
    expect(await verifyCredentialWeb(valid, options)).toStrictEqual(
      verifyCredential(valid, options),
    );
  });
});

describe("@agentland/identity/web import graph", () => {
  it("web.ts and every module it reaches are free of node: imports and Buffer", () => {
    const visited = new Set<string>();
    const pending = [new URL("../src/web.ts", import.meta.url)];
    while (pending.length > 0) {
      const file = pending.pop()!;
      if (visited.has(file.pathname)) continue;
      visited.add(file.pathname);
      const text = readFileSync(file, "utf8");
      expect(text, file.pathname).not.toMatch(/\bfrom\s*["']node:|\bimport\s*\(\s*["']node:/);
      expect(text, file.pathname).not.toMatch(/\bBuffer\b/);
      // Static, side-effect and dynamic imports; type-only ones are erased at build, so they
      // never reach the browser bundle (group 1 marks them).
      const specifiers = [
        ...text.matchAll(
          /^\s*(?:import|export)(\s+type\b)?[\w$*{},\s]*?\bfrom\s*["']([^"']+)["']|^\s*import\s*["']([^"']+)["']|\bimport\s*\(\s*["']([^"']+)["']/gm,
        ),
      ].flatMap((match) => (match[1] === undefined ? [match[2] ?? match[3] ?? match[4]!] : []));
      for (const specifier of specifiers) {
        // Identity is zero-dependency: anything the browser entry reaches is a relative module.
        expect(specifier, `${file.pathname} imports ${specifier}`).toMatch(/^\.\.?\//);
        pending.push(new URL(specifier.replace(/\.js$/, ".ts"), file));
      }
    }
    const names = [...visited].map((path) => path.slice(path.lastIndexOf("/") + 1));
    expect(names).toContain("web.ts");
    expect(names).toContain("credential-claims.ts");
    expect(names).toContain("json.ts");
  });
});
