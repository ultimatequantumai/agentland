import { requestSigningMessage, type RequestSigningInput } from "./request-signing.js";

// C-12 / D-39: arena forecasts sign `agentland-arena-forecast/1\n` ‖ the request preimage, so a
// public forecast signature can never be replayed into a private arena, nor the reverse. The
// domains are disjoint by their first bytes: request preimages start with an uppercase method,
// vault intents with `{`, proof of possession with `agentland-pop/1`, verify nonces with
// `agentland-verify/1:` and squad entries with `agentland-squad/1\n` (squad.ts). No validation
// or normalization, exactly like requestSigningMessage.
// Any byte change is a breaking identity change: it needs a second review and a
// `/transparency` changelog entry. The HSM attestation signs the same bytes.
export const ARENA_FORECAST_DOMAIN = "agentland-arena-forecast/1";
const PREFIX = new TextEncoder().encode(`${ARENA_FORECAST_DOMAIN}\n`);

export function arenaForecastSigningMessage(input: RequestSigningInput): Uint8Array {
  const body = requestSigningMessage(input);
  const message = new Uint8Array(PREFIX.length + body.length);
  message.set(PREFIX);
  message.set(body, PREFIX.length);
  return message;
}
