export { canonicalize, canonicalBytes, parseIJson, sha256Hex } from "./canonical.js";
export type { JsonValue } from "./canonical.js";
export { signEd25519, verifyEd25519 } from "./keys.js";
export type { Ed25519PublicJwk, X25519PublicJwk, PublicJwk } from "./keys.js";
export { requestSigningMessage } from "./request-signing.js";
export type { RequestSigningInput } from "./request-signing.js";
export { ARENA_FORECAST_DOMAIN, arenaForecastSigningMessage } from "./arena-forecast.js";
export {
  DID_LINK_FORMAT,
  MAX_ACTIVE_DID_LINKS,
  didLinkSigningBytes,
  validateDidLinkStatement,
  activeDidLinks,
} from "./did-link.js";
export type { DidLinkStatement } from "./did-link.js";
export { agentDid, buildDidDocument, buildDidHistory } from "./did.js";
export type {
  DidDocument,
  DidHistory,
  PublicKeyRecord,
  RotationRecord,
  RotationStatement,
} from "./did.js";
export {
  createPutIntent,
  createDeleteIntent,
  signVaultIntent,
  stampVaultEntry,
  hashVaultEntry,
  validateVaultChain,
} from "./vault.js";
export type {
  VaultIntent,
  VaultEntry,
  VaultHead,
  VaultSigningKey,
  VaultChainResult,
  VaultChainSuccess,
  VerificationFailure,
} from "./vault.js";
export {
  SQUAD_FORMAT,
  SQUAD_HEAD_FORMAT,
  SQUAD_PLATFORM_DID,
  SQUAD_STATEMENT_PREFIX,
  SQUAD_STATEMENT_CONTENT_TYPE,
  SQUAD_MAX_MEMBERS,
  SQUAD_INVITE_TTL_MS,
  SQUAD_REASON_MAX,
  SQUAD_STATEMENT_KINDS,
  SQUAD_ATTEST_REASONS,
  squadGenesis,
  squadSigningMessage,
  createSquadPutIntent,
  createSquadDeleteIntent,
  signSquadIntent,
  squadStatementBytes,
  parseSquadStatement,
  hashSquadEntry,
  squadDayRoot,
  squadHeadPreimage,
  signSquadHead,
  verifySquadHead,
} from "./squad.js";
export type {
  SquadStatementKind,
  SquadAttestReason,
  SquadRole,
  SquadIntent,
  SquadEntry,
  SquadEpochWrap,
  SquadStatement,
  SquadSignerKeys,
  SquadPlatformKey,
  SquadStatementPayload,
  SquadHeadStatement,
  SignedSquadHead,
} from "./squad.js";
export { replaySquad } from "./squad-replay.js";
export type {
  SquadMembership,
  SquadEpoch,
  SquadReplaySuccess,
  SquadReplayResult,
} from "./squad-replay.js";
export { buildSquadProofBundle, verifySquadBundle } from "./squad-bundle.js";
export type { SquadProofBundle, SquadBundleResult } from "./squad-bundle.js";
export {
  SQUAD_SEALED_FORMAT,
  SQUAD_SEALED_MAGIC,
  SQUAD_SEALED_CONTENT_TYPE,
  SquadSealedError,
  squadSealedAad,
  sealSquadEntry,
  openSquadEntry,
  parseSquadSealedHeader,
} from "./squad-sealed.js";
export type { SquadSealedFailure, SquadSealedInput, OpenedSquadEntry } from "./squad-sealed.js";
export {
  wrapEpochKey,
  openEpochWrap,
  verifySquadEpochRecipients,
  checkSquadSealedEntries,
} from "./squad-sealed.js";
export type {
  SquadEpochWrapInput,
  SquadRecipientHistory,
  VerifiedSquadRecipient,
  SquadSealedCheckResult,
} from "./squad-sealed.js";
export { merkleRoot, createInclusionProof, verifyInclusionProof } from "./merkle.js";
export type { MerkleProof } from "./merkle.js";
export {
  assembleCredential,
  credentialSigningInput,
  issueCredential,
  verifyCredential,
} from "./credentials.js";
export { credentialClaims } from "./credential-claims.js";
export type {
  AgentLandCredential,
  CredentialType,
  CredentialVerification,
  SeasonEvidence,
  TrustedIssuer,
} from "./credentials.js";
export { verifyVaultBundle } from "./proof.js";
export type { VaultProofBundle, VaultBundleResult } from "./proof.js";
export { buildVaultProofBundle } from "./vault-bundle.js";
export { signedHeadPreimage, signVaultHead, verifySignedHead } from "./head.js";
export type { SignedVaultHead, VaultHeadStatement } from "./head.js";
export {
  createVerifyNonce,
  popPreimage,
  verifyNonceSignature,
  verifyProofOfPossession,
} from "./challenge.js";
export {
  EXPORT_LAYOUT,
  buildExportManifest,
  buildExportManifestFromDigests,
  readUstar,
  writeUstar,
  writeUstarStream,
} from "./export.js";
export type { ArchiveFile, ExportManifest, StreamedArchiveFile } from "./export.js";
export {
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
} from "./ots.js";
export type { OtsAttestation, OtsNode, OtsOp } from "./ots.js";
export {
  ANCHOR_FORMAT,
  ANCHOR_PAYLOAD_PREFIX,
  ANCHOR_MIN_GAS,
  ANCHOR_MAX_GAS,
  AnchorGuardError,
  anchorPayload,
  assertAnchorTransaction,
  anchorSigningHash,
  evmAddressFromSpki,
  anchorSignatureFromDer,
  serializeAnchorTransaction,
  decodeAnchorTransaction,
  verifyAnchorTransaction,
  currentRuleGas,
} from "./evm-anchor.js";
export type {
  AnchorTransactionFields,
  AnchorExpectation,
  GuardedAnchorTransaction,
} from "./evm-anchor.js";
export {
  SEALED_FORMAT,
  SEALED_CONTENT_TYPE,
  SEALED_MAGIC_HEX,
  SEALED_OVERHEAD,
  SEALED_PAD_UNIT,
  SEALED_MIN_ENVELOPE,
  SEALED_MAX_ENVELOPE,
  SEALED_MAX_INNER,
  SealedEnvelopeError,
  generateEncryptionKey,
  encryptionPublicKey,
  recipientKeyId,
  assertEncryptionPublicKey,
  sealedEnvelopeRecipient,
  sealEntry,
  openSealedEntry,
} from "./sealed.js";
export type {
  SealedFailure,
  SealedMeta,
  SealInput,
  OpenedSealedEntry,
  EncryptionKeyPair,
} from "./sealed.js";
export {
  ENC_KEY_FORMAT,
  ENC_KEY_STATEMENT_WINDOW_MS,
  ENC_KEY_REVOKE_REASON_MAX,
  encKeyStatementBytes,
  validateEncKeyStatement,
  EncKeyRecipientError,
  verifyEncKeyRecipient,
} from "./enc-key.js";
export type {
  EncKeyStatement,
  EncKeyRevokeStatement,
  EncKeyStatementAny,
  EncKeyRecord,
  EncKeyHistory,
  EncKeyRecipientFailure,
  VerifiedEncKeyRecipient,
} from "./enc-key.js";
