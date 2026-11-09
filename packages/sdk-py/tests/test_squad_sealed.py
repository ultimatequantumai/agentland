"""agentland-squad-sealed/1 cross-checks with libsodium (PyNaCl).

Independent of packages/identity/src and of the agentland package: re-derives the F2.3 squad
envelope, the epoch-key wrap (an unchanged agentland-sealed/1 envelope) and every SS1-sealed
payload with a stdlib RFC 5869 HKDF and RFC 8785 bytes written here (T-PLAIN, format half).
"""

import base64
import hashlib
import hmac
import json
import struct
from pathlib import Path

import pytest
from nacl import bindings as b
from nacl.exceptions import CryptoError

ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = ROOT / "packages/identity/test/squad-sealed-vectors.json"
# RESEARCH F2.3 anchors (15-01's frozen agentland-sealed/1 bytes win if they differ).
ANCHORS = {
    "envelope_length": 304,
    "envelope_sha256": "672c6da84576576efd468049feeb616da5537b54d86f2730be0f8975020e0a63",
    "envelope_tag": "b8541ff31a622ae7d632a5d61d275a81",
    "wrap_hkdf_key": "d51914e663f68f0e60c8a9239cb8ddcd1ebb7c047b092baf2a2dbacd2369c82e",
    "wrap_kid": "f35e5616160a30bf3c6e79fa73c576d40205e8fc3ba4e1c6dcf93e6b98e857b4",
    "wrap_length": 364,
    "wrap_sha256": "c7dab3bbe75e0703a2b171c6846bcc4b86dc0784d4b4b243cfabe8626f520f1c",
}
SQUAD_FORMAT = "agentland-squad-sealed/1"
SEALED_FORMAT = "agentland-sealed/1"
EPOCH_KEY_TYPE = "application/vnd.agentland.squad-epoch-key"
MARKER = b"SQUAD-PLAINTEXT-7f3a"


def data() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def b64url(value: str) -> bytes:
    return base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))


def jcs(o: object) -> bytes:
    # RFC 8785 for these inputs: ASCII strings, small integers, sorted members.
    return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def inner(meta: dict, body: bytes) -> bytes:
    meta_bytes = jcs({**meta, "size": len(body)})
    n = len(meta_bytes) + len(body)
    length = max(256, -(-(4 + n) // 256) * 256)
    raw = struct.pack(">I", len(meta_bytes)) + meta_bytes + body
    return raw + bytes(length - len(raw))


def parse_inner(plain: bytes) -> tuple[dict, bytes]:
    (meta_len,) = struct.unpack(">I", plain[:4])
    meta = json.loads(plain[4 : 4 + meta_len])
    return meta, plain[4 + meta_len : 4 + meta_len + meta["size"]]


def hkdf_sha256(ikm: bytes, salt: bytes, info: bytes, n: int) -> bytes:
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()
    out, block, counter = b"", b"", 1
    while len(out) < n:
        block = hmac.new(prk, block + info + bytes([counter]), hashlib.sha256).digest()
        out += block
        counter += 1
    return out[:n]


def squad_aad(squad_id: str, key: str, epoch: str) -> bytes:
    return jcs({"epoch": epoch, "format": SQUAD_FORMAT, "key": key, "squad_id": squad_id})


def epoch_key(name: str, n: str) -> bytes:
    return hashlib.sha256(f"{name}/epoch/{n}".encode()).digest()


def build_envelope(e: dict) -> bytes:
    key, nonce = bytes.fromhex(e["epoch_key_hex"]), bytes.fromhex(e["nonce_hex"])
    plain = inner(e["meta"], e["body_utf8"].encode())
    aad = squad_aad(e["squad_id"], e["key"], e["epoch"])
    sealed = b.crypto_aead_xchacha20poly1305_ietf_encrypt(plain, aad, nonce, key)
    return b"ALQ\x01" + struct.pack(">I", int(e["epoch"])) + nonce + sealed


def open_wrap(envelope: bytes, secret: bytes, did: str, squad_id: str, epoch: str) -> bytes:
    """agentland-sealed/1 open: X25519 + HKDF + XChaCha20-Poly1305, then the inner layout."""
    assert envelope[:4] == b"ALS\x01"
    r_pub = b.crypto_scalarmult_base(secret)
    assert envelope[4:36] == hashlib.sha256(r_pub).digest()
    e_pub, nonce = envelope[36:68], envelope[68:92]
    key = hkdf_sha256(b.crypto_scalarmult(secret, e_pub), e_pub + r_pub, SEALED_FORMAT.encode(), 32)
    aad = jcs({"did": did, "format": SEALED_FORMAT, "key": f"sealed/.squad/{squad_id}/epoch/{epoch}"})
    meta, body = parse_inner(
        b.crypto_aead_xchacha20poly1305_ietf_decrypt(envelope[92:], aad, nonce, key)
    )
    assert meta["content_type"] == EPOCH_KEY_TYPE and meta["size"] == 32
    return body


def ss1() -> dict:
    return next(s for s in data()["scenarios"] if s["name"] == "SS1-sealed")


def test_envelope_anchor() -> None:
    e = data()["envelope"]
    envelope = build_envelope(e)
    assert len(envelope) == ANCHORS["envelope_length"]
    assert hashlib.sha256(envelope).hexdigest() == ANCHORS["envelope_sha256"]
    assert envelope[-16:].hex() == ANCHORS["envelope_tag"]
    assert envelope.hex() == e["envelope_hex"]
    assert squad_aad(e["squad_id"], e["key"], e["epoch"]).decode() == e["aad_utf8"]


def test_aad_epoch_2_refused() -> None:
    e = data()["envelope"]
    envelope = build_envelope(e)
    key, nonce = bytes.fromhex(e["epoch_key_hex"]), envelope[8:32]
    with pytest.raises(CryptoError):
        b.crypto_aead_xchacha20poly1305_ietf_decrypt(
            envelope[32:], squad_aad(e["squad_id"], e["key"], "2"), nonce, key
        )
    plain = b.crypto_aead_xchacha20poly1305_ietf_decrypt(
        envelope[32:], squad_aad(e["squad_id"], e["key"], "1"), nonce, key
    )
    assert plain == inner(e["meta"], e["body_utf8"].encode())


def test_wrap_rederived() -> None:
    w = data()["wrap"]
    e_sec, r_pub = bytes.fromhex(w["ephemeral_secret_hex"]), bytes.fromhex(w["recipient_public_hex"])
    e_pub, nonce = b.crypto_scalarmult_base(e_sec), bytes.fromhex(w["nonce_hex"])
    assert e_pub.hex() == w["ephemeral_public_hex"]
    key = hkdf_sha256(b.crypto_scalarmult(e_sec, r_pub), e_pub + r_pub, SEALED_FORMAT.encode(), 32)
    assert key.hex() == ANCHORS["wrap_hkdf_key"]
    sq, n = w["squad_id"], w["epoch"]
    plain = inner(
        {"content_type": EPOCH_KEY_TYPE, "name": f"{sq}/epoch/{n}", "tags": []},
        bytes.fromhex(w["epoch_key_hex"]),
    )
    aad = jcs({"did": w["did"], "format": SEALED_FORMAT, "key": f"sealed/.squad/{sq}/epoch/{n}"})
    sealed = b.crypto_aead_xchacha20poly1305_ietf_encrypt(plain, aad, nonce, key)
    envelope = b"ALS\x01" + hashlib.sha256(r_pub).digest() + e_pub + nonce + sealed
    assert len(envelope) == ANCHORS["wrap_length"]
    assert hashlib.sha256(envelope).hexdigest() == ANCHORS["wrap_sha256"]
    assert hashlib.sha256(r_pub).hexdigest() == ANCHORS["wrap_kid"] == w["kid"]
    assert envelope == b64url(w["envelope_b64url"])
    assert w["envelope_sha256"] == ANCHORS["wrap_sha256"]


def test_payloads_are_ciphertext() -> None:
    s = ss1()
    entries = {entry["seq"]: entry for entry in s["entries"]}
    assert [row["seq"] for row in s["payloads"]] == ["5", "9", "12"]
    for row in s["payloads"]:
        payload = b64url(row["content_b64url"])
        assert payload[:4] == b"ALQ\x01"
        assert len(payload) >= 304 and (len(payload) - 48) % 256 == 0
        assert MARKER not in payload
        (n,) = struct.unpack(">I", payload[4:8])
        plain = b.crypto_aead_xchacha20poly1305_ietf_decrypt(
            payload[32:],
            squad_aad(s["squad_id"], entries[row["seq"]]["key"], str(n)),
            payload[8:32],
            epoch_key("SS1-sealed", str(n)),
        )
        assert MARKER in parse_inner(plain)[1]


def test_wraps_open() -> None:
    doc = data()
    s = ss1()
    secrets = {k["kid"]: (k["label"], bytes.fromhex(k["secret_hex"])) for k in doc["enc_keys"]}
    dids = {h["label"]: h["did"] for h in doc["histories"]}
    opened = 0
    for row in s["statements"]:
        statement = json.loads(b64url(row["content_b64url"]))
        if statement["kind"] != "epoch":
            continue
        n = statement["epoch"]
        for wrap in statement["wraps"]:
            label, secret = secrets[wrap["kid"]]
            body = open_wrap(b64url(wrap["envelope"]), secret, dids[label], s["squad_id"], n)
            assert body == epoch_key("SS1-sealed", n)
            opened += 1
    assert opened == 7
