"""agentland-sealed/1 and agentland-enc-key/1 cross-checks with libsodium (PyNaCl 1.6.2).

Independent of packages/identity/src: re-runs the committed generator byte for byte and
re-derives V1 with a stdlib RFC 5869 HKDF written here.
"""

import base64
import hashlib
import hmac
import json
import subprocess
import sys
from pathlib import Path

import pytest
from nacl import bindings as b
from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey, VerifyKey

ROOT = Path(__file__).resolve().parents[3]
GENERATOR = ROOT / "packages/identity/test/generate-sealed-vectors.py"
DATA_PATH = ROOT / "packages/identity/test/sealed-vectors.json"
# RESEARCH F2 / F2.1 / draft-irtf-cfrg-xchacha-03 section A.3.1 anchors.
ANCHORS = {
    "shared": "4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742",
    "key": "d51914e663f68f0e60c8a9239cb8ddcd1ebb7c047b092baf2a2dbacd2369c82e",
    "content_hash": "142141121a3f4f341083806ec715c64d2cb1cdedffc9ef35d560269955c32838",
    "rid": "f35e5616160a30bf3c6e79fa73c576d40205e8fc3ba4e1c6dcf93e6b98e857b4",
    "kat_tag": "c0875924c1c7987947deafd8780acf49",
    "register": "iP4HoBxwA9Np0gfQGs4q3uO0iT6UxsdjRs_NKgGHt2mo7oAx9fwBuEdiG-IzS1vqA2xBF1dVM7EuBUXATuTiBw",
    "revoke": "8EVua95crxhFxwWE5HmThUOdj2N7OwUsxPeELBa9gekGsGa631-TNRzIrg57hFfwTRoOyN-SKIFN9zs3McLhAQ",
}
# RESEARCH F3: the libsodium low-order blacklist (hard-coded so parametrization never reads the file).
LOW_ORDER = [
    "0000000000000000000000000000000000000000000000000000000000000000",
    "0100000000000000000000000000000000000000000000000000000000000000",
    "e0eb7a7c3b41b8ae1656e3faf19fc46ada098deb9c32b1fd866205165f49b800",
    "5f9c95bca3508c24b1d0b1559c83ef5b04445cc4581c8e86d8224eddd09f1157",
    "ecffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f",
    "edffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f",
    "eeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f",
]
LOW_ORDER_INPUTS = [
    bytes.fromhex(u)[:31] + bytes([bytes.fromhex(u)[31] | bit]) for u in LOW_ORDER for bit in (0, 0x80)
]


def data() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def b64url(value: str) -> bytes:
    return base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))


def b64url_encode(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def hkdf_sha256(ikm: bytes, salt: bytes, info: bytes, n: int) -> bytes:
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()
    okm, block, counter = b"", b"", 1
    while len(okm) < n:
        block = hmac.new(prk, block + info + bytes([counter]), hashlib.sha256).digest()
        okm += block
        counter += 1
    return okm[:n]


def aad(vector: dict) -> bytes:
    body = {"did": vector["did"], "format": "agentland-sealed/1", "key": vector["key"]}
    return json.dumps(body, sort_keys=True, separators=(",", ":")).encode()


def open_envelope(vector: dict) -> bytes:
    envelope = bytes.fromhex(vector["envelope_hex"])
    r_priv = bytes.fromhex(vector["recipient_secret_hex"])
    r_pub = b.crypto_scalarmult_base(r_priv)
    assert envelope[:4] == b"ALS\x01" and envelope[4:36] == hashlib.sha256(r_pub).digest()
    e_pub, nonce = envelope[36:68], envelope[68:92]
    key = hkdf_sha256(b.crypto_scalarmult(r_priv, e_pub), e_pub + r_pub, b"agentland-sealed/1", 32)
    return b.crypto_aead_xchacha20poly1305_ietf_decrypt(envelope[92:], aad(vector), nonce, key)


def test_hkdf_rfc5869_case_1():
    # The test's own HKDF must itself be right: RFC 5869 appendix A.1.
    okm = hkdf_sha256(
        bytes.fromhex("0b" * 22), bytes.fromhex("000102030405060708090a0b0c"), bytes.fromhex("f0f1f2f3f4f5f6f7f8f9"), 42
    )
    assert okm.hex() == (
        "3cb25f25faacd57a90434f64d0362f2a2d2d0a90cf1a5a4c5db02d56ecc4c5bf34007208d5b887185865"
    )


def test_generator_reproduces_file():
    out = subprocess.run([sys.executable, str(GENERATOR), "--stdout"], capture_output=True, check=True)
    assert out.stdout == DATA_PATH.read_bytes()


def test_v1_rederived():
    v1 = data()["v1"]
    e_priv, r_pub = bytes.fromhex(v1["ephemeral_secret_hex"]), bytes.fromhex(v1["recipient_public_hex"])
    e_pub, nonce = b.crypto_scalarmult_base(e_priv), bytes.fromhex(v1["nonce_hex"])
    assert e_pub.hex() == v1["ephemeral_public_hex"]
    assert hashlib.sha256(r_pub).hexdigest() == ANCHORS["rid"] == v1["recipient_key_id"]
    shared = b.crypto_scalarmult(e_priv, r_pub)
    assert shared.hex() == ANCHORS["shared"]
    key = hkdf_sha256(shared, e_pub + r_pub, b"agentland-sealed/1", 32)
    assert key.hex() == ANCHORS["key"]
    assert aad(v1) == v1["aad_utf8"].encode()
    inner = bytes.fromhex(v1["inner_hex"])
    envelope = (
        b"ALS\x01" + hashlib.sha256(r_pub).digest() + e_pub + nonce
        + b.crypto_aead_xchacha20poly1305_ietf_encrypt(inner, aad(v1), nonce, key)
    )
    assert envelope.hex() == v1["envelope_hex"]
    assert len(envelope) == 364
    assert hashlib.sha256(envelope).hexdigest() == ANCHORS["content_hash"]
    assert open_envelope(v1) == inner


def test_v2_opens():
    v2 = data()["v2"]
    inner = open_envelope(v2)
    assert inner.hex() == v2["inner_hex"]
    assert len(inner) == 512 and len(bytes.fromhex(v2["envelope_hex"])) == 620
    meta_len = int.from_bytes(inner[:4], "big")
    meta = json.loads(inner[4 : 4 + meta_len])
    body = inner[4 + meta_len : 4 + meta_len + meta["size"]]
    assert inner[4 : 4 + meta_len].decode() == v2["meta_utf8"]
    assert {k: v for k, v in meta.items() if k != "size"} == v2["meta"]
    assert body.decode() == v2["body_utf8"]
    assert not any(inner[4 + meta_len + meta["size"] :])


@pytest.mark.parametrize("u", LOW_ORDER_INPUTS, ids=[u.hex() for u in LOW_ORDER_INPUTS])
def test_low_order_refused(u):
    e_priv = hashlib.sha256(b"agentland-sealed/1 low-order probe").digest()
    with pytest.raises(Exception):
        b.crypto_scalarmult(e_priv, u)


def test_low_order_matches_file():
    assert data()["low_order"]["encodings"] == LOW_ORDER
    assert len(set(LOW_ORDER_INPUTS)) == 14


@pytest.mark.parametrize("name", ["register", "revoke"])
def test_e1_signatures(name):
    enc = data()["enc_key"]
    vector = enc[name]
    statement_bytes = json.dumps(vector["statement"], sort_keys=True, separators=(",", ":")).encode()
    assert statement_bytes == vector["canonical_utf8"].encode()
    signing_key = SigningKey(bytes.fromhex(enc["signing_seed_hex"]))
    signature = signing_key.sign(statement_bytes).signature
    assert b64url_encode(signature) == ANCHORS[name] == vector["signature"]
    verify_key = VerifyKey(b64url(enc["signing_public_x"]))
    assert bytes(signing_key.verify_key) == bytes(verify_key)
    verify_key.verify(statement_bytes, signature)
    tampered = bytearray(statement_bytes)
    tampered[10] ^= 1
    with pytest.raises(BadSignatureError):
        verify_key.verify(bytes(tampered), signature)


def test_xchacha_kat():
    kat = data()["xchacha_kat"]
    sealed = b.crypto_aead_xchacha20poly1305_ietf_encrypt(
        kat["plaintext_utf8"].encode(),
        bytes.fromhex(kat["aad_hex"]),
        bytes.fromhex(kat["nonce_hex"]),
        bytes.fromhex(kat["key_hex"]),
    )
    assert sealed.hex() == kat["ciphertext_hex"]
    assert sealed[-16:].hex() == ANCHORS["kat_tag"]


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from _strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)


def test_strings_ascii():
    # json.dumps(sort_keys=True, separators=(",", ":")) is exact RFC 8785 only for ASCII strings (F4).
    assert all(s.isascii() for s in _strings(data()))
