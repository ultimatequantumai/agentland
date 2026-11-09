import { existsSync, readFileSync, readdirSync } from "node:fs";
import { describe, expect, it } from "vitest";

// D-37: the six MIT open specs served at /spec. Every JSON-LD term IRI the code emits
// must land on a `### <Term>` heading in its spec, so published credentials and DID
// documents never dereference to nothing.
const specDir = new URL("../spec/", import.meta.url);
const srcDir = new URL("../src/", import.meta.url);
const names = ["did", "vault", "vc", "verify", "sealed", "anchor"] as const;
const read = (file: string) => readFileSync(new URL(file, specDir), "utf8");

describe("agentland open specs", () => {
  it.each(names)("spec/agentland-%s-1.md exists with its title first", (name) => {
    const file = `agentland-${name}-1.md`;
    expect(existsSync(new URL(file, specDir))).toBe(true);
    expect(read(file).split("\n")[0]).toBe(`# agentland-${name}/1`);
  });

  it.each(names)("agentland-%s/1 ends with an MIT ## License section", (name) => {
    const text = read(`agentland-${name}-1.md`);
    const license = text.indexOf("\n## License\n");
    expect(license).toBeGreaterThan(0);
    const tail = text.slice(license + "\n## License\n".length);
    expect(tail).toContain("MIT License");
    expect(tail).toContain("Permission is hereby granted, free of charge");
    expect(tail).not.toMatch(/^#{1,2} /m);
  });

  it.each(names)("agentland-%s/1 never mentions escrow and uses no tables", (name) => {
    const text = read(`agentland-${name}-1.md`);
    expect(text.toLowerCase()).not.toContain("escrow");
    expect(text).not.toMatch(/^\| /m);
  });

  it("every context term IRI in packages/identity/src has a ### heading in its spec", () => {
    const iri = /https:\/\/agentland\.us\/spec\/(agentland-[a-z]+)\/1#([A-Za-z_]+)/g;
    const found = new Set<string>();
    for (const file of readdirSync(srcDir).filter((f) => f.endsWith(".ts")))
      for (const [, spec, term] of readFileSync(new URL(file, srcDir), "utf8").matchAll(iri))
        found.add(`${spec}#${term}`);
    // The scan must see the known terms, or a regex drift would pass vacuously.
    expect(found).toContain("agentland-did#AgentLandTrust");
    expect(found).toContain("agentland-vc#SeasonEvidence");
    expect(found).toContain("agentland-vc#audit_root");
    for (const entry of found) {
      const [spec, term] = entry.split("#") as [string, string];
      const lines = read(`${spec}-1.md`).split("\n");
      expect(lines, `${spec}-1.md lacks ### ${term}`).toContain(`### ${term}`);
    }
  });

  it("agentland-vault/1 names RFC 8785 canonicalization and the RFC 6962 Merkle profile", () => {
    const text = read("agentland-vault-1.md");
    expect(text).toContain("RFC 8785");
    expect(text).toContain("RFC 6962");
  });

  it("agentland-vc/1 pins the issuer key, the alltime season and upheld-fraud revocation", () => {
    const text = read("agentland-vc-1.md");
    expect(text).toContain("did:web:agentland.us#vc-1");
    expect(text).toContain("alltime");
    expect(text).toContain("upheld fraud");
    for (const heading of [
      "### Calibrated",
      "### MarketBeater",
      "### Teacher",
      "### Ironclad",
      "### EarlyBird",
      "### SeasonResult",
      "### SeasonEvidence",
    ])
      expect(text.split("\n")).toContain(heading);
  });
});

describe("16-01 squad spec", () => {
  const file = "agentland-squad-1.md";

  it("spec/agentland-squad-1.md exists with its title first", () => {
    expect(existsSync(new URL(file, specDir))).toBe(true);
    expect(read(file).split("\n")[0]).toBe("# agentland-squad/1");
  });

  it("ends with an MIT ## License section, never mentions escrow and uses no tables", () => {
    const text = read(file);
    const license = text.indexOf("\n## License\n");
    expect(license).toBeGreaterThan(0);
    const tail = text.slice(license + "\n## License\n".length);
    expect(tail).toContain("MIT License");
    expect(tail).toContain("Permission is hereby granted, free of charge");
    expect(tail).not.toMatch(/^#{1,2} /m);
    expect(text.toLowerCase()).not.toContain("escrow");
    expect(text).not.toMatch(/^\| /m);
  });

  it("carries the SCALE-04 sections and the frozen terms", () => {
    const text = read(file);
    const lines = text.split("\n");
    for (const heading of [
      "## Membership",
      "## Authorization",
      "## Key custody",
      "## Append concurrency",
      "## Proofs",
      "## Exit and export",
      "## What the chain proves",
    ])
      expect(lines).toContain(heading);
    for (const term of [
      "agentland-squad-head/1",
      "public/.squad/",
      "attest_leave",
      "RFC 8785",
      "RFC 6962",
      "604800000",
      "self-custod",
      "e0a4268ef8453ba0e11557b9c8c83bc88630a8e7774ac9177c0e29fa3c902960",
    ])
      expect(text).toContain(term);
  });

  it("docs/14 has §12 with the six subsections and the §10 list line", () => {
    const lines = readFileSync(
      new URL("../../../docs/14-identity-and-memory.md", import.meta.url),
      "utf8",
    ).split("\n");
    for (const heading of [
      "## 12. Squads (agentland-squad/1)",
      "### 12.1 Membership",
      "### 12.2 Authorization",
      "### 12.3 Key custody",
      "### 12.4 Append concurrency",
      "### 12.5 Proofs",
      "### 12.6 Exit and export",
    ])
      expect(lines).toContain(heading);
    expect(lines.some((line) => line.startsWith("- `agentland-squad/1`"))).toBe(true);
  });
});

// 15-04 (D-20, PRIVATE-02, 14): the vault spec describes sealed entries (non-normative) and the DID
// spec documents encryption keys, without claiming either is live.
describe("15-04 spec sections", () => {
  it("vault has a non-normative sealed section", () => {
    const text = read("agentland-vault-1.md");
    const lines = text.split("\n");
    const at = lines.indexOf("## Sealed entries");
    expect(at).toBeGreaterThan(0);
    const first = lines.slice(at + 1).find((line) => line.trim() !== "");
    expect(first).toBe("This section is non-normative.");
    for (const term of ["agentland-sealed/1", "application/vnd.agentland.sealed", "content_hash"])
      expect(text).toContain(term);
  });

  it("did documents encryption keys", () => {
    const text = read("agentland-did-1.md");
    for (const term of ["agentland-enc-key/1", "`enc_keys`", "keyAgreement"])
      expect(text).toContain(term);
    expect(text).not.toContain("this list is empty today");
  });
});

// 16-02 (D-29, SCALE-04): agentland-squad-sealed/1 is published before any sealed squad code runs.
describe("16-02 squad sealed spec", () => {
  const file = "agentland-squad-sealed-1.md";

  it("spec/agentland-squad-sealed-1.md exists with its title first", () => {
    expect(existsSync(new URL(file, specDir))).toBe(true);
    expect(read(file).split("\n")[0]).toBe("# agentland-squad-sealed/1");
  });

  it("ends with an MIT ## License section, never mentions escrow and uses no tables", () => {
    const text = read(file);
    const license = text.indexOf("\n## License\n");
    expect(license).toBeGreaterThan(0);
    const tail = text.slice(license + "\n## License\n".length);
    expect(tail).toContain("MIT License");
    expect(tail).toContain("Permission is hereby granted, free of charge");
    expect(tail).not.toMatch(/^#{1,2} /m);
    expect(text.toLowerCase()).not.toContain("escrow");
    expect(text).not.toMatch(/^\| /m);
  });

  it("carries the sections in order and the frozen terms", () => {
    const text = read(file);
    const lines = text.split("\n");
    const at = [
      "## Envelope",
      "## Associated data",
      "## Inner plaintext",
      "## Epoch keys and wraps",
      "## Choosing recipients",
      "## Freshness",
      "## Forward and backward secrecy",
      "## Lost keys",
      "## What the server checks",
      "## Vectors",
      "## License",
    ].map((heading) => lines.indexOf(heading));
    expect(at.some((index) => index < 0)).toBe(false);
    expect([...at].sort((a, b) => a - b)).toStrictEqual(at);
    for (const term of [
      "41 4c 51 01",
      "304",
      "(len − 48) mod 256 = 0",
      "application/vnd.agentland.squad-sealed",
      "application/vnd.agentland.squad-epoch-key",
      "sealed/.squad/",
      "agentland-sealed/1",
      "agentland-enc-key/1",
      "not key-committing",
      "never by trial decryption",
      "AgentLand never holds an epoch key",
      "that sealed content is gone",
      "672c6da84576576efd468049feeb616da5537b54d86f2730be0f8975020e0a63",
      "packages/identity/test/squad-sealed-vectors.json",
    ])
      expect(text).toContain(term);
  });

  it("agentland-squad/1 points to it and docs/14 has §12.7 and the §10 line", () => {
    expect(read("agentland-squad-1.md")).toContain("/spec/agentland-squad-sealed/1");
    const lines = readFileSync(
      new URL("../../../docs/14-identity-and-memory.md", import.meta.url),
      "utf8",
    ).split("\n");
    expect(lines).toContain("### 12.7 Sealed squads (agentland-squad-sealed/1)");
    expect(lines.some((line) => line.startsWith("- `agentland-squad-sealed/1`"))).toBe(true);
  });
});
