import { createPrivateKey, createPublicKey, sign, verify } from "node:crypto";
import { describe, expect, it } from "vitest";
import {
  assembleCredential,
  credentialClaims,
  credentialSigningInput,
  issueCredential,
  signEd25519,
  verifyCredential,
} from "../src/index.js";
import type { CredentialType, SeasonEvidence } from "../src/index.js";
import { did, testKey, timestamp } from "./helpers.js";
import { fixtureRoot } from "./fixtures/oracle.js";
const key = testKey();
const issuer = "did:web:agentland.us";
const kid = `${issuer}#issuer-1`;
const validUntil = "2026-02-01T00:00:00.000Z";
const evidence: SeasonEvidence = {
  season: "season-2026-01",
  n: 200,
  shrunk_edge: 0.025,
  audit_root: fixtureRoot,
};
const input = {
  id: "urn:uuid:0f223836-2222-4444-8888-777777777777",
  subjectDid: did,
  type: "MarketBeater" as const,
  evidence,
  validFrom: timestamp,
  validUntil,
  issuerKeyId: kid,
  privatePkcs8: key.privatePkcs8,
};
const options = {
  trustedIssuer: { issuer, kid, publicKeyJwk: key.publicKeyJwk },
  expectedSubjectDid: did,
  now: timestamp,
};
function decoded(compact: string) {
  const [header, payload] = compact.split(".");
  return {
    header: JSON.parse(Buffer.from(header!, "base64url").toString()) as Record<string, unknown>,
    payload: JSON.parse(Buffer.from(payload!, "base64url").toString()) as Record<string, unknown>,
  };
}
function nativeCompact(
  payload: unknown,
  header: unknown = { alg: "Ed25519", kid, typ: "vc+jwt", cty: "vc" },
): string {
  const first = Buffer.from(
    typeof header === "string" ? header : JSON.stringify(header, null, 2),
  ).toString("base64url");
  const second = Buffer.from(
    typeof payload === "string" ? payload : JSON.stringify(payload, null, 2),
  ).toString("base64url");
  const wire = `${first}.${second}`;
  return `${wire}.${sign(null, Buffer.from(wire, "ascii"), createPrivateKey({ key: key.privatePkcs8, format: "der", type: "pkcs8" })).toString("base64url")}`;
}

describe("VC2 compact Ed25519 JWS", () => {
  it("issues a native-verifiable actual VC payload and fully specified envelope", () => {
    const compact = issueCredential(input);
    const [headerPart, payloadPart, signature] = compact.split(".");
    expect(
      verify(
        null,
        Buffer.from(`${headerPart}.${payloadPart}`, "ascii"),
        createPublicKey({ format: "jwk", key: { ...key.publicKeyJwk } }),
        Buffer.from(signature!, "base64url"),
      ),
    ).toBe(true);
    const { header, payload } = decoded(compact);
    expect(header).toEqual({ alg: "Ed25519", kid, typ: "vc+jwt", cty: "vc" });
    expect(payload).toEqual({
      "@context": [
        "https://www.w3.org/ns/credentials/v2",
        {
          Calibrated: "https://agentland.us/spec/agentland-vc/1#Calibrated",
          MarketBeater: "https://agentland.us/spec/agentland-vc/1#MarketBeater",
          Teacher: "https://agentland.us/spec/agentland-vc/1#Teacher",
          Ironclad: "https://agentland.us/spec/agentland-vc/1#Ironclad",
          EarlyBird: "https://agentland.us/spec/agentland-vc/1#EarlyBird",
          SeasonResult: "https://agentland.us/spec/agentland-vc/1#SeasonResult",
          SeasonEvidence: "https://agentland.us/spec/agentland-vc/1#SeasonEvidence",
          season: "https://agentland.us/spec/agentland-vc/1#season",
          n: "https://agentland.us/spec/agentland-vc/1#n",
          shrunk_edge: "https://agentland.us/spec/agentland-vc/1#shrunk_edge",
          audit_root: "https://agentland.us/spec/agentland-vc/1#audit_root",
        },
      ],
      id: input.id,
      type: ["VerifiableCredential", "MarketBeater"],
      issuer,
      credentialSubject: { id: did },
      evidence: { type: "SeasonEvidence", ...evidence },
      validFrom: timestamp,
      validUntil,
    });
    expect(verifyCredential(compact, options)).toEqual({ valid: true, credential: payload });
    expect("vc" in payload).toBe(false);
  });
  it("verifies independently native-signed original whitespace, not reserialized bytes", () => {
    const { payload } = decoded(issueCredential(input));
    const compact = nativeCompact(payload);
    expect(verifyCredential(compact, options)).toEqual({ valid: true, credential: payload });
    const parts = compact.split(".");
    const compactedPayload = Buffer.from(JSON.stringify(payload)).toString("base64url");
    expect(verifyCredential(`${parts[0]}.${compactedPayload}.${parts[2]}`, options).valid).toBe(
      false,
    );
  });
  it("binds explicit time and subject with inclusive start/exclusive end", () => {
    const token = issueCredential(input);
    for (const [now, valid] of [
      ["2025-12-31T23:59:59.999Z", false],
      [timestamp, true],
      ["2026-01-31T23:59:59.999Z", true],
      [validUntil, false],
      ["2026-02-01T00:00:00.001Z", false],
    ] as const)
      expect(verifyCredential(token, { ...options, now }).valid).toBe(valid);
    expect(verifyCredential(token, { ...options, now: "2026-02-30T00:00:00.000Z" }).valid).toBe(
      false,
    );
    expect(
      verifyCredential(token, { ...options, now: undefined } as unknown as typeof options).valid,
    ).toBe(false);
    expect(
      verifyCredential(token, {
        ...options,
        expectedSubjectDid: "did:web:agentland.us:agents:another",
      }).valid,
    ).toBe(false);
    const permanent = { ...input, validUntil: undefined };
    expect(
      verifyCredential(issueCredential(permanent), { ...options, now: "2099-01-01T00:00:00.000Z" })
        .valid,
    ).toBe(true);
    expect(
      verifyCredential(issueCredential({ ...input, validUntil: timestamp }), options).valid,
    ).toBe(false);
  });
  it("rejects algorithm confusion, substituted trust, unprotected extensions and embedded keys", () => {
    const { header, payload } = decoded(issueCredential(input));
    for (const altered of [
      { ...header, alg: "none" },
      { ...header, alg: "HS256" },
      { ...header, alg: "EdDSA" },
      { ...header, alg: "Ed448" },
      { ...header, alg: "X25519" },
      { ...header, kid: `${issuer}#wrong` },
      { ...header, typ: "JWT" },
      { ...header, cty: "json" },
      { ...header, crit: ["unknown"], unknown: true },
      { ...header, b64: false },
      { ...header, jwk: key.publicKeyJwk },
      { ...header, jku: "https://evil.test/keys" },
      { ...header, x5u: "https://evil.test/cert" },
      { alg: "Ed25519", typ: "vc+jwt", cty: "vc" },
    ])
      expect(verifyCredential(nativeCompact(payload, altered), options).valid).toBe(false);
    for (const trustedIssuer of [
      { ...options.trustedIssuer, issuer: "did:web:evil.test" },
      { ...options.trustedIssuer, kid: `${issuer}#other` },
      { ...options.trustedIssuer, publicKeyJwk: testKey(1).publicKeyJwk },
      { ...options.trustedIssuer, publicKeyJwk: { ...key.publicKeyJwk, d: "secret" } },
      { ...options.trustedIssuer, publicKeyJwk: { ...key.publicKeyJwk, crv: "X25519" } },
    ])
      expect(
        verifyCredential(issueCredential(input), {
          ...options,
          trustedIssuer: trustedIssuer as typeof options.trustedIssuer,
        }).valid,
      ).toBe(false);
  });
  it("rejects signed malformed evidence, context replacement and claims", () => {
    const { payload } = decoded(issueCredential(input));
    const badPayloads = [
      { ...payload, issuer: "did:web:evil.test" },
      { ...payload, credentialSubject: { id: "did:web:agentland.us:agents:another" } },
      { ...payload, "@context": ["https://evil.test/context"] },
      {
        ...payload,
        "@context": [
          "https://www.w3.org/ns/credentials/v2",
          { MarketBeater: "https://evil.test/meaning" },
        ],
      },
      { ...payload, type: ["VerifiableCredential", "Unknown"] },
      { ...payload, type: ["MarketBeater"] },
      { ...payload, validFrom: "2026-02-30T00:00:00.000Z" },
      { ...payload, validUntil: "2025-01-01T00:00:00.000Z" },
      { ...payload, id: "relative" },
      { ...payload, evidence: { ...evidence, type: "Other" } },
      { ...payload, evidence: { ...evidence, type: "SeasonEvidence", n: -1 } },
      { ...payload, evidence: { ...evidence, type: "SeasonEvidence", n: 1.1 } },
      {
        ...payload,
        evidence: { ...evidence, type: "SeasonEvidence", n: Number.MAX_SAFE_INTEGER + 1 },
      },
      { ...payload, evidence: { ...evidence, type: "SeasonEvidence", shrunk_edge: "0.2" } },
      {
        ...payload,
        evidence: { ...evidence, type: "SeasonEvidence", audit_root: fixtureRoot.toUpperCase() },
      },
      { ...payload, evidence: { ...evidence, type: "SeasonEvidence", season: "" } },
    ];
    for (const altered of badPayloads)
      expect(verifyCredential(nativeCompact(altered), options).valid).toBe(false);
    for (const type of [
      "Calibrated",
      "MarketBeater",
      "Teacher",
      "Ironclad",
      "EarlyBird",
      "SeasonResult",
    ] as const) {
      for (const n of [0, 30, 200])
        for (const shrunk_edge of [-1, 0, 0.5])
          expect(
            verifyCredential(
              issueCredential({ ...input, type, evidence: { ...evidence, n, shrunk_edge } }),
              options,
            ).valid,
          ).toBe(true);
    }
  });
  it("rejects malformed encodings/JSON and changed protected/payload bytes", () => {
    const token = issueCredential(input);
    const parts = token.split(".");
    for (const bad of [
      "",
      "a.b",
      `${token}.extra`,
      `${parts[0]}=.${parts[1]}.${parts[2]}`,
      `${parts[0]}.${parts[1]}.A`,
      `${parts[0]}.${parts[1]}.${parts[2]}=`,
      `_${parts[0]}.${parts[1]}.${parts[2]}`,
      `${parts[0]}.wK8.${parts[2]}`,
    ])
      expect(verifyCredential(bad, options).valid).toBe(false);
    expect(verifyCredential(nativeCompact('{"issuer":"a","issuer":"b"}'), options).valid).toBe(
      false,
    );
    const { header, payload } = decoded(token);
    expect(
      verifyCredential(nativeCompact(payload, '{"alg":"Ed25519","alg":"Ed25519"}'), options).valid,
    ).toBe(false);
    expect(
      verifyCredential(
        `${Buffer.from(JSON.stringify({ ...header, kid: `${issuer}#other` })).toString("base64url")}.${parts[1]}.${parts[2]}`,
        options,
      ).valid,
    ).toBe(false);
    expect(
      verifyCredential(
        `${parts[0]}.${Buffer.from(JSON.stringify({ ...payload, id: "urn:altered" })).toString("base64url")}.${parts[2]}`,
        options,
      ).valid,
    ).toBe(false);
  });
  it("validates issuance domains without asserting factual badge eligibility", () => {
    for (const altered of [
      { ...input, type: "Other" as CredentialType },
      { ...input, issuerKeyId: "issuer-1" },
      { ...input, subjectDid: "did:web:evil.test" },
      { ...input, validFrom: "2026-02-30T00:00:00.000Z" },
      { ...input, evidence: { ...evidence, n: -1 } },
      { ...input, evidence: { ...evidence, shrunk_edge: Infinity } },
      { ...input, evidence: { ...evidence, audit_root: "0" } },
      { ...input, id: "relative" },
      { ...input, validUntil: "2025-01-01T00:00:00.000Z" },
    ])
      expect(() => issueCredential(altered)).toThrow(TypeError);
  });
});

// D-32: the vc_issuer key lives in the HSM, so the bytes to sign are built without any key and
// the detached Ed25519 signature is assembled afterwards. The split must not change one byte.
const unsignedInput = {
  id: input.id,
  subjectDid: did,
  type: input.type,
  evidence,
  validFrom: timestamp,
  validUntil,
  issuerKeyId: kid,
};
function thrown(action: () => unknown): Error {
  try {
    action();
  } catch (error) {
    return error as Error;
  }
  throw new Error("expected a throw");
}
function detachedSignature(signingInput: string): Uint8Array {
  return Buffer.from(
    signEd25519(Buffer.from(signingInput, "ascii"), key.privatePkcs8),
    "base64url",
  );
}

describe("key-free signing input and detached assembly (HSM issuer)", () => {
  it("credentialSigningInput + assembleCredential equals issueCredential byte for byte", () => {
    for (const [unsigned, signed] of [
      [unsignedInput, input],
      [
        { ...unsignedInput, validUntil: undefined },
        { ...input, validUntil: undefined },
      ],
    ] as const) {
      const prepared = credentialSigningInput(unsigned);
      expect(Object.keys(prepared)).toEqual(["signingInput"]);
      const compact = issueCredential(signed);
      expect(prepared.signingInput).toBe(compact.split(".").slice(0, 2).join("."));
      const signature = detachedSignature(prepared.signingInput);
      expect(assembleCredential(prepared.signingInput, signature)).toBe(compact);
    }
    const { signingInput } = credentialSigningInput(unsignedInput);
    expect(assembleCredential(signingInput, new Uint8Array(64))).toBe(
      `${signingInput}.${"A".repeat(86)}`,
    );
    expect(decoded(`${signingInput}.x`).header).toEqual({
      alg: "Ed25519",
      kid,
      typ: "vc+jwt",
      cty: "vc",
    });
  });
  it("credentialSigningInput rejects the same domains with the same errors as issueCredential", () => {
    for (const altered of [
      { ...unsignedInput, id: "relative" },
      { ...unsignedInput, id: "not a uri" },
      { ...unsignedInput, type: "Other" as CredentialType },
      { ...unsignedInput, evidence: { ...evidence, extra: 1 } as SeasonEvidence },
      { ...unsignedInput, evidence: { ...evidence, audit_root: fixtureRoot.toUpperCase() } },
      { ...unsignedInput, issuerKeyId: "did:web:evil.test#vc-1" },
      { ...unsignedInput, issuerKeyId: "vc-1" },
      { ...unsignedInput, subjectDid: "did:web:evil.test" },
      { ...unsignedInput, validUntil: "2025-01-01T00:00:00.000Z" },
    ]) {
      const split = thrown(() => credentialSigningInput(altered));
      const whole = thrown(() => issueCredential({ ...altered, privatePkcs8: key.privatePkcs8 }));
      expect(split).toBeInstanceOf(TypeError);
      expect(split.message).toBe(whole.message);
    }
  });
  it("assembleCredential rejects a non-64-byte signature and a malformed signing input", () => {
    const { signingInput } = credentialSigningInput(unsignedInput);
    const [first, second] = signingInput.split(".");
    for (const signature of [
      new Uint8Array(0),
      new Uint8Array(63),
      new Uint8Array(65),
      "A".repeat(86) as unknown as Uint8Array,
    ])
      expect(() => assembleCredential(signingInput, signature)).toThrow(TypeError);
    for (const bad of [
      "",
      "abc",
      `${signingInput}.extra`,
      `${signingInput}.`,
      `.${second}`,
      `${first}.`,
      `${first}=.${second}`,
      `${first}.${second}+`,
      `${first}.${second}/`,
    ])
      expect(() => assembleCredential(bad, new Uint8Array(64))).toThrow(TypeError);
  });
});

// D-33: a badge scope is a season row (uuid) or the all-time row, encoded as the literal `alltime`.
describe("season scopes and urn:uuid credential IDs", () => {
  it("issues and verifies evidence for the alltime scope and a season uuid", () => {
    for (const season of ["alltime", "0f223836-1111-4444-8888-777777777777"]) {
      const compact = issueCredential({
        ...input,
        id: "urn:uuid:01a1e5f0-7c3d-7e2a-8b4c-5d6e7f8091a2",
        evidence: { ...evidence, season },
      });
      const { payload } = decoded(compact);
      expect(payload.id).toBe("urn:uuid:01a1e5f0-7c3d-7e2a-8b4c-5d6e7f8091a2");
      expect(payload.evidence).toEqual({ type: "SeasonEvidence", ...evidence, season });
      expect(verifyCredential(compact, options)).toEqual({ valid: true, credential: payload });
      const { signingInput } = credentialSigningInput({
        ...unsignedInput,
        id: "urn:uuid:01a1e5f0-7c3d-7e2a-8b4c-5d6e7f8091a2",
        evidence: { ...evidence, season },
      });
      expect(assembleCredential(signingInput, detachedSignature(signingInput))).toBe(compact);
    }
  });
});

describe("credentialClaims (decode without verifying)", () => {
  it("returns the issued header and credential and never checks a signature", () => {
    const compact = issueCredential(input);
    const { header, payload } = decoded(compact);
    expect(credentialClaims(compact)).toEqual({ header, credential: payload });
    const parts = compact.split(".");
    expect(credentialClaims(`${parts[0]}.${parts[1]}.${"A".repeat(86)}`)).toEqual({
      header,
      credential: payload,
    });
    expect(
      credentialClaims(issueCredential({ ...input, privatePkcs8: testKey(1).privatePkcs8 })),
    ).toEqual({ header, credential: payload });
    const otherKid = issueCredential({ ...input, issuerKeyId: `${issuer}#vc-2` });
    expect(credentialClaims(otherKid)).toEqual({
      header: { ...header, kid: `${issuer}#vc-2` },
      credential: payload,
    });
  });
  it("throws on a malformed credential with the existing parser's TypeError", () => {
    const compact = issueCredential(input);
    const parts = compact.split(".");
    const { payload } = decoded(compact);
    const notJson = Buffer.from("not json").toString("base64url");
    // Messages are the ones the shared helpers already throw inside verifyCredential, so a
    // missing export ("… is not a function") cannot satisfy this test.
    for (const [bad, message] of [
      ["", "Three JWS segments required"],
      [`${parts[0]}.${parts[1]}`, "Three JWS segments required"],
      [`${compact}.extra`, "Three JWS segments required"],
      [`${parts[0]}.${notJson}.${parts[2]}`, "Invalid I-JSON"],
      [`${notJson}.${parts[1]}.${parts[2]}`, "Invalid I-JSON"],
      [`${parts[0]}=.${parts[1]}.${parts[2]}`, "Canonical base64url required"],
      [nativeCompact({ ...payload, extra: true }), "Unexpected or missing members"],
      [nativeCompact('{"issuer":"a","issuer":"b"}'), "Invalid I-JSON"],
      [
        nativeCompact(payload, { alg: "Ed25519", kid, typ: "vc+jwt", cty: "vc", jwk: {} }),
        "Unexpected or missing members",
      ],
    ] as const) {
      const error = thrown(() => credentialClaims(bad));
      expect(error).toBeInstanceOf(TypeError);
      expect(error.message).toBe(message);
    }
  });
});
