/** Native node:crypto fixture authoring, explicit sorted wire fields; no production helper used.
 * Published RFC8032 test1 seed only; these values are test pins, not live audit roots.
 */
export const fixtureHead = "baf4a54a1a3f14cb99194fe2e90e60103953678fe68530bf195d750339b01cd4";
export const fixtureRoot = "89a8a945afc3b93b972a9f7ef19dc9dcff16223dde4fbfd6a568b79343b55994";
/** Independent SHA256(0x00 || canonical stamped entry 2), its UTC day's only leaf. */
export const fixtureDailyRoot = "f3dacb6ea6f80d990665a48c7189a01efe690a1f330beff36eff1984df8034c6";
export const fixtureGenesis = "f2746c9a731399cc623c322ea699a8e24ad29fc96dc373ef2d2d83a5eb478584";
export const fixtureEntryHashes = [
  "d12737732b219ed1efe7556d57c83ec855ee7f45bd1e22f6852698bea6234e6a",
  "d6d9f46d8f16034d1d6971cd3f28210731eccc25a43dc9788d40599d9d509ceb",
  fixtureHead,
] as const;
