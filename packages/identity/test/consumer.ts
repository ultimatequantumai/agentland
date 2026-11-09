import {
  agentDid,
  buildDidDocument,
  buildDidHistory,
  canonicalBytes,
  canonicalize,
  createDeleteIntent,
  createInclusionProof,
  createPutIntent,
  hashVaultEntry,
  issueCredential,
  merkleRoot,
  parseIJson,
  sha256Hex,
  signEd25519,
  signVaultIntent,
  stampVaultEntry,
  validateVaultChain,
  verifyCredential,
  verifyEd25519,
  verifyInclusionProof,
  verifyVaultBundle,
} from "@agentland/identity";
import type {
  AgentLandCredential,
  CredentialType,
  CredentialVerification,
  DidDocument,
  DidHistory,
  Ed25519PublicJwk,
  JsonValue,
  MerkleProof,
  PublicKeyRecord,
  RotationRecord,
  SeasonEvidence,
  TrustedIssuer,
  VaultBundleResult,
  VaultChainResult,
  VaultEntry,
  VaultHead,
  VaultIntent,
  VaultProofBundle,
  VaultSigningKey,
  X25519PublicJwk,
} from "@agentland/identity";

export function portableConsumer(
  privatePkcs8: Uint8Array,
  signing: Ed25519PublicJwk,
  encryption: X25519PublicJwk,
) {
  const did = agentDid("weatherwise");
  const instant = "2026-01-01T00:00:00.000Z";
  const value: JsonValue = parseIJson('{"meaning":"portable"}');
  const wire: string = canonicalize(value);
  const genesis: string = sha256Hex(Buffer.from(did));
  const intent: VaultIntent = createPutIntent({
    seq: "1",
    key: "vault/x",
    content: canonicalBytes(value),
    prev_hash: genesis,
  });
  const tombstone: VaultIntent = createDeleteIntent({
    seq: "2",
    key: "vault/x",
    prev_hash: genesis,
  });
  const signature: string = signVaultIntent(intent, privatePkcs8);
  const entry: VaultEntry = stampVaultEntry(
    { intent, sig_agent: signature, ts_server: instant },
    signing,
  );
  const head: VaultHead = { seq: "1", head_hash: hashVaultEntry(entry) };
  const keys: readonly VaultSigningKey[] = [{ from_seq: "1", publicKeyJwk: signing }];
  const chain: VaultChainResult = validateVaultChain({
    did,
    entries: [entry],
    keys,
    expectedHead: head,
  });
  const root: string = merkleRoot([canonicalBytes(entry)]);
  const proof: MerkleProof = createInclusionProof([canonicalBytes(entry)], 0);
  const bundle: VaultProofBundle = {
    format: "agentland-vault/1",
    did,
    entries: [entry],
    proof: { ...proof, seq: "1" },
  };
  const verified: VaultBundleResult = verifyVaultBundle(bundle, {
    keys,
    expectedHead: head,
    publishedRoot: root,
  });
  const records: PublicKeyRecord[] = [
    { id: `${did}#sign`, publicKeyJwk: signing, purpose: "signing", activated_at: instant },
    { id: `${did}#enc`, publicKeyJwk: encryption, purpose: "encryption", activated_at: instant },
  ];
  const rotations: readonly RotationRecord[] = [];
  const document: DidDocument = buildDidDocument({ handle: "weatherwise", keys: records });
  const history: DidHistory = buildDidHistory({ handle: "weatherwise", keys: records, rotations });
  const type: CredentialType = "SeasonResult";
  const evidence: SeasonEvidence = {
    season: "season-1",
    n: 30,
    shrunk_edge: 0.1,
    audit_root: root,
  };
  const trustedIssuer: TrustedIssuer = {
    issuer: "did:web:agentland.us",
    kid: "did:web:agentland.us#issuer",
    publicKeyJwk: signing,
  };
  const credential = issueCredential({
    id: "urn:agentland:test-result",
    subjectDid: did,
    type,
    evidence,
    validFrom: instant,
    issuerKeyId: trustedIssuer.kid,
    privatePkcs8,
  });
  const credentialResult: CredentialVerification = verifyCredential(credential, {
    trustedIssuer,
    expectedSubjectDid: did,
    now: instant,
  });
  const claims: AgentLandCredential | undefined = credentialResult.valid
    ? credentialResult.credential
    : undefined;
  const actionSignature = signEd25519(Buffer.from(wire), privatePkcs8);
  return {
    chain,
    verified,
    document,
    history,
    claims,
    tombstone,
    action: verifyEd25519(Buffer.from(wire), actionSignature, signing),
    proof: verifyInclusionProof(canonicalBytes(entry), proof, root),
  };
}
