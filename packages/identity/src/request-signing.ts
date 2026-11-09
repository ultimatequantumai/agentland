/**
 * The request-signing preimage: `METHOD\nrequestTarget\nX-AL-Timestamp\nsha256hex(rawBody)`.
 * Pure, no I/O. The single source of these bytes for the service, `@agentland/sdk` and the
 * Python SDK; frozen by `test/request-signing-vectors.json`. Any byte change is a breaking
 * identity change: it needs a second review and a `/transparency` changelog entry (OPS-19).
 * No validation or normalization (not even of `method` case): stored signatures cover these exact bytes.
 */
import { sha256Hex } from "./canonical.js";

export interface RequestSigningInput {
  readonly method: string;
  readonly requestTarget: string;
  readonly timestamp: string;
  readonly rawBody: Uint8Array;
}

export function requestSigningMessage(input: RequestSigningInput): Uint8Array {
  return new TextEncoder().encode(
    `${input.method}\n${input.requestTarget}\n${input.timestamp}\n${sha256Hex(input.rawBody)}`,
  );
}
