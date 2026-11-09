import base64
import hashlib
import json
import re
from pathlib import Path

import pytest
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import load_der_private_key

from agentland.signing import request_preimage, signature_headers

ROOT = Path(__file__).resolve().parents[3]
DATA = json.loads((ROOT / "packages/identity/test/request-signing-vectors.json").read_text())
VECTORS = DATA["vectors"]
TAMPER = DATA["tamper"]
BY_NAME = {v["name"]: v for v in VECTORS}
SIG_RE = re.compile(r"^[A-Za-z0-9+/]{86}==$")


def b64(value: str) -> bytes:
    return base64.b64decode(value, validate=True)


def public_key(jwk: dict) -> Ed25519PublicKey:
    x = jwk["x"]
    raw = base64.urlsafe_b64decode(x + "=" * (-len(x) % 4))
    assert len(raw) == 32
    return Ed25519PublicKey.from_public_bytes(raw)


def preimage(entry: dict) -> bytes:
    return request_preimage(entry["method"], entry["request_target"], entry["timestamp"], b64(entry["raw_body_b64"]))


def verifies(entry: dict, message: bytes) -> bool:
    try:
        public_key(entry["public_jwk"]).verify(b64(entry["signature_b64"]), message)
        return True
    except InvalidSignature:
        return False


@pytest.mark.parametrize("entry", VECTORS + TAMPER, ids=lambda e: e["name"])
def test_signature_encoding(entry):
    assert SIG_RE.match(entry["signature_b64"])
    assert len(b64(entry["signature_b64"])) == 64


@pytest.mark.parametrize("vector", VECTORS, ids=lambda v: v["name"])
def test_every_vector_preimage_and_signature_match(vector):
    assert vector["valid"] is True
    raw_body = b64(vector["raw_body_b64"])
    message = preimage(vector)
    assert message == vector["message_utf8"].encode()
    assert hashlib.sha256(raw_body).hexdigest() == vector["body_sha256_hex"]
    assert verifies(vector, message) is True

    key = load_der_private_key(b64(vector["private_pkcs8_b64"]), password=None)
    raw_sig = key.sign(message)
    assert raw_sig == b64(vector["signature_b64"])
    assert base64.b64encode(raw_sig).decode() == vector["signature_b64"]

    headers = signature_headers(
        lambda m: key.sign(m), vector["method"], vector["request_target"], raw_body, vector["timestamp"]
    )
    assert headers["X-AL-Signature"] == vector["signature_b64"]
    assert SIG_RE.match(headers["X-AL-Signature"])
    assert headers["X-AL-Timestamp"] == vector["timestamp"]


def test_tamper_covers_every_field():
    assert {t["field"] for t in TAMPER} == {"method", "request_target", "timestamp", "raw_body", "signature"}


@pytest.mark.parametrize("entry", TAMPER, ids=lambda t: t["name"])
def test_one_flipped_byte_fails(entry):
    base = BY_NAME[entry["base"]]
    message = preimage(entry)
    assert message == entry["message_utf8"].encode()
    assert hashlib.sha256(b64(entry["raw_body_b64"])).hexdigest() == entry["body_sha256_hex"]
    if entry["field"] == "signature":
        assert entry["message_utf8"] == base["message_utf8"]
        assert entry["signature_b64"] != base["signature_b64"]
    else:
        assert entry["message_utf8"] != base["message_utf8"]
    with pytest.raises(InvalidSignature):
        public_key(entry["public_jwk"]).verify(b64(entry["signature_b64"]), entry["message_utf8"].encode())
    assert verifies(entry, message) is entry["valid"] is False


def test_short_signature_rejected():
    v = VECTORS[0]
    with pytest.raises(ValueError):
        signature_headers(lambda m: b"\x00" * 63, v["method"], v["request_target"], b64(v["raw_body_b64"]), v["timestamp"])


def test_sdk_sources_never_import_cryptography():
    src = Path(__file__).resolve().parents[1] / "src" / "agentland"
    files = list(src.rglob("*.py"))
    assert files
    assert not [f for f in files if "cryptography" in f.read_text()]
