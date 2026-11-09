"""Self-custody request signing (docs/04-api.md :62). The SDK never holds a key: callers pass a
`signer(message) -> raw 64-byte Ed25519 signature`."""

import base64
import hashlib
from typing import Callable

Signer = Callable[[bytes], bytes]


def request_preimage(method: str, request_target: str, timestamp: str, raw_body: bytes) -> bytes:
    """`METHOD\\nrequestTarget\\nX-AL-Timestamp\\nsha256hex(rawBody)`, checked against identity's vectors."""
    digest = hashlib.sha256(raw_body).hexdigest()
    return f"{method}\n{request_target}\n{timestamp}\n{digest}".encode()


def signature_headers(signer: Signer, method: str, request_target: str, raw_body: bytes, timestamp: str) -> dict[str, str]:
    signature = signer(request_preimage(method, request_target, timestamp, raw_body))
    if len(signature) != 64:
        raise ValueError(f"signer must return a raw 64-byte Ed25519 signature, got {len(signature)} bytes")
    # Padded standard base64 (88 chars), never base64url (P-18).
    return {"X-AL-Timestamp": timestamp, "X-AL-Signature": base64.b64encode(signature).decode("ascii")}
