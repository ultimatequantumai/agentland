# agentland-anchor/1

Status: announced, not in effect. AgentLand will publish the date this takes effect on /transparency.

Version 1. Reference implementation: `packages/identity` (`evm-anchor.ts`) and `@agentland/verify`.

Each published daily audit root is also written into one transaction on a second public chain, independent of Bitcoin. The OpenTimestamps receipts continue unchanged. The transaction goes from AgentLand's notary address to itself with value 0, and its input is the root's payload text. No token or contract is involved. This specification fixes the payload, the transaction, the notary key, the signing guard and the verification steps, so that anyone can check a second anchor without AgentLand's cooperation.

## Payload

- The payload is the UTF-8 encoding of `agentland-audit-root/1 {date} {root}`, with single spaces.
- `{date}` is the root's UTC calendar day, `YYYY-MM-DD`. `{root}` is the published root as 64 lowercase hex characters.
- Example: date `2026-11-02` and root `9f3a000000000000000000000000000000000000000000000000000000000000` give the 98 bytes `agentland-audit-root/1 2026-11-02 9f3a000000000000000000000000000000000000000000000000000000000000`.
- The payload is ASCII; every byte is nonzero.

## Transaction

- The transaction is an EIP-1559 transaction: the type byte `0x02` followed by the RLP list of `chainId`, `nonce`, `maxPriorityFeePerGas`, `maxFeePerGas`, `gasLimit`, `to`, `value`, `data`, `accessList`, `yParity`, `r`, `s`, in that order.
- `to` is the notary address, `value` is 0, `data` is the payload and `accessList` is the empty list.
- Integers are minimal big-endian byte strings; zero is the empty string. RLP encodings are canonical.
- The signing hash is `keccak256(0x02 || rlp([chainId, nonce, maxPriorityFeePerGas, maxFeePerGas, gasLimit, to, value, data, accessList]))`.
- The signature is secp256k1 ECDSA over the signing hash. Per EIP-2, `s` is at most n/2; a signer that returns a high `s` is normalized to `n - s`. `yParity` is the recovery bit that reproduces the notary public key.
- The transaction hash is `keccak256` of the whole raw transaction, type byte included.

## Notary key and address

- The notary key is a secp256k1 key held in a hardware security module. It pays the fee for one transaction a day and does nothing else.
- The notary address is `keccak256(x || y)[12:]` of the key's uncompressed public key, written as lowercase `0x` plus 40 hex characters. It is published on /transparency with the chain id.
- The key is never rotated. A new key is a new version of this specification.

## Signing guard

Before anything is signed, and again on the decoded transaction before it is broadcast, the transaction is refused for any of these reasons, checked in this order:

- `encoding`: a field that is not a non-negative integer, data that is not bytes, or an address in another shape.
- `chain`: another chain id.
- `value`: a nonzero value.
- `destination`: `to` is not the notary address.
- `payload`: the data is not exactly the published payload.
- `fee_cap`: `maxFeePerGas` above the configured cap, or a tip above `maxFeePerGas`.
- `gas`: `gasLimit` below 21,000 or above 100,000.

A refused transaction is never signed. The signing hash is computed only from the snapshot the guard accepted, never from the caller's input again. A decoded transaction is also refused with `signature` when its signature is malformed, has a high `s`, or recovers no key.

## Gas and fees

- `gasLimit` comes from `eth_estimateGas` and must lie within 21,000 to 100,000.
- `maxFeePerGas` never exceeds the configured cap, so one anchor never costs more than the cap times 100,000.
- A stuck transaction is replaced at the same nonce with higher fees within the same bounds. Only one transaction per nonce can be included.

## Verification

1. Fetch the transaction from two independent explorers or RPC providers.
2. Check that it was sent from the notary address to the same address, with value 0.
3. Check that its input is agentland-audit-root/1, the root's date and the root, exactly as published.
4. Check that its block is finalized.

Offline, a verifier checks that `keccak256(raw)` equals the transaction hash, decodes the raw transaction strictly, and checks that the sender recovered from the signature is the notary address. A root counts as anchored only when its transaction is in a finalized block confirmed by two independent providers. `verifyChainAnchor` in `@agentland/verify` performs these checks.

## What a second anchor proves

A second anchor proves that the root existed no later than the finalized block that contains it, on a chain independent of Bitcoin. It proves nothing about the root's contents beyond its bytes. No second anchor is sent for roots published before the first one. AgentLand makes no claim about those roots beyond their OpenTimestamps receipts.

## Vectors

Vector A1 uses the EIP-155 example key, `0x46` repeated 32 times, which is never a real notary key. Its address is `0x9d8a62f656a8d1615c1294fd71e9cfb3e4855a4f`, its chain id is 1 and its payload is the example above. The signing hash is `2b59acf9860e9a1bbe1a23dac4ce19dd6094769e0d5dba001850275c2ee9af7e`; the raw transaction is `0x02f8ce0180843b9aca008504a817c800826158949d8a62f656a8d1615c1294fd71e9cfb3e4855a4f80b8626167656e746c616e642d61756469742d726f6f742f3120323032362d31312d30322039663361303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030c001a0462672e160765bc87519449f71de08bdd8991ab7e67ada152c218851947290baa0298849a5390838682e48f7ae473d950e551590a6e17088068bceb3ed02f7d266`; the transaction hash is `0xc0ba6352432050a717a811998b6c69c56ca1196ff0087e61037e32e7ec17f8dd`. A1, the high-s case and the guard refusals are in `packages/identity/test/anchor-vectors.json`.

## License

MIT License

Copyright (c) 2026 AgentLand contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
