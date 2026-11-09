import base64
import hashlib
import json
import re
from pathlib import Path

import pytest
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import load_der_private_key

from agentland.signing import request_preimage

ROOT = Path(__file__).resolve().parents[3]
DATA = json.loads((ROOT / "packages/identity/test/arena-did-link-vectors.json").read_text())
REQUEST = json.loads((ROOT / "packages/identity/test/request-signing-vectors.json").read_text())
PUBLIC_BY_NAME = {v["name"]: v for v in REQUEST["vectors"]}
ARENA = DATA["arena_forecast"]
LINK = DATA["did_link"]
PREFIX = b"agentland-arena-forecast/1\n"
# RESEARCH F12 anchors (RFC 8032 section 7.1 test-1 key).
ANCHORS = {
    "arena-forecast-submit": "o5++WnXtH9SlR6StgSF9uCpR7W1l1n6O6Q37yoh4IbZZpcwBMbBDqllNn71jg7Ch75IIP5E+kE49ZKS7psPQBQ==",
    "link": "dQUF5IyM2R5o7lThd6Aslaza9pFGrmcWVTMzwoT5rho0Nqef4q2RXcMQPQUVYWqgayn113ZkUIgf67-WO0LxCA",
    "unlink": "byyXfGxWKa-ypAFWVE_4Q0HaK7vZQZrdGDMjbVsjmpXux_ttfJUYWNfmNfPWxsUMmC7sb1awd87kxedoQ4gcDw",
}
PADDED_RE = re.compile(r"^[A-Za-z0-9+/]{86}==$")
URL_RE = re.compile(r"^[A-Za-z0-9_-]{86}$")


def b64(value: str) -> bytes:
    return base64.b64decode(value, validate=True)


def b64url(value: str) -> bytes:
    return base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))


def public_key(jwk: dict) -> Ed25519PublicKey:
    raw = b64url(jwk["x"])
    assert len(raw) == 32
    return Ed25519PublicKey.from_public_bytes(raw)


def preimage(entry: dict) -> bytes:
    return request_preimage(entry["method"], entry["request_target"], entry["timestamp"], b64(entry["raw_body_b64"]))


def jcs(obj) -> bytes:
    # Valid RFC 8785 for these string-only objects.
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


PRIVATE = load_der_private_key(b64(DATA["private_pkcs8_b64"]), password=None)
PUBLIC = public_key(DATA["public_jwk"])


def test_signatures_filled_and_anchored():
    arena = ARENA["vectors"][0]
    assert isinstance(arena["signature_b64"], str)
    assert PADDED_RE.match(arena["signature_b64"])
    assert arena["signature_b64"] == ANCHORS["arena-forecast-submit"]
    assert ARENA["tamper"][0]["signature_b64"] == ANCHORS["arena-forecast-submit"]
    for vector in LINK["vectors"]:
        assert isinstance(vector["signature"], str)
        assert URL_RE.match(vector["signature"])
        assert vector["signature"] == ANCHORS[vector["name"]]


def test_arena_vector():
    vector = ARENA["vectors"][0]
    message = PREFIX + preimage(vector)
    assert message == vector["message_utf8"].encode()
    assert hashlib.sha256(b64(vector["raw_body_b64"])).hexdigest() == vector["body_sha256_hex"]
    assert PRIVATE.sign(message) == b64(vector["signature_b64"])
    PUBLIC.verify(b64(vector["signature_b64"]), message)


@pytest.mark.parametrize("entry", ARENA["tamper"], ids=lambda t: t["name"])
def test_arena_tamper(entry):
    if "base_public" in entry:
        public = PUBLIC_BY_NAME[entry["base_public"]]
        assert entry["message_utf8"].encode() == PREFIX + preimage(public)
        assert entry["signature_b64"] == public["signature_b64"]
    else:
        base = next(v for v in ARENA["vectors"] if v["name"] == entry["base"])
        assert entry["message_utf8"].encode() == preimage(base)
    with pytest.raises(InvalidSignature):
        PUBLIC.verify(b64(entry["signature_b64"]), entry["message_utf8"].encode())


@pytest.mark.parametrize("vector", LINK["vectors"], ids=lambda v: v["name"])
def test_did_link_vectors(vector):
    message = jcs(vector["statement"])
    assert message == vector["canonical_utf8"].encode()
    signature = b64url(vector["signature"])
    assert PRIVATE.sign(message) == signature
    PUBLIC.verify(signature, message)
    flipped = bytes([message[0] ^ 0x01]) + message[1:]
    with pytest.raises(InvalidSignature):
        PUBLIC.verify(signature, flipped)


@pytest.mark.parametrize("entry", LINK["active"], ids=lambda e: e["name"])
def test_active_order(entry):
    active: dict[str, str] = {}
    for statement in sorted(entry["history"], key=lambda s: (s["timestamp"], jcs(s))):
        linked = statement["linked_did"]
        if statement["action"] == "link":
            assert linked not in active
            active[linked] = statement["timestamp"]
        else:
            assert linked in active
            del active[linked]
    assert sorted(active, key=lambda d: (active[d], d)) == entry["expected"]


@pytest.mark.parametrize("entry", LINK["also_known_as"], ids=lambda e: e["name"])
def test_also_known_as(entry):
    assert [f"https://agentland.us/agents/{entry['handle']}/did.json", *entry["links"]] == entry["expected"]
