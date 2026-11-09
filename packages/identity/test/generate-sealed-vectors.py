#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) AgentLand
#
# Reproduction script for packages/identity/test/sealed-vectors.json (agentland-sealed/1,
# agentland-enc-key/1). Implements the formats independently of
# packages/identity/src/{sealed,enc-key}.ts with libsodium (PyNaCl 1.6.2) and a stdlib RFC 5869
# HKDF. Never edit vectors by hand; change this script and regenerate.
#
# Deterministic: every secret, nonce and body is a fixed constant or
# hashlib.sha256(<ASCII label>).digest(); no clock. Output is RFC 8785 (ASCII strings and
# integers only, so sorted-key compact json.dumps is exact), with no trailing newline.
#
#   (cd packages/sdk-py && uv run --python 3.12 python ../identity/test/generate-sealed-vectors.py)
#   (cd packages/sdk-py && uv run --python 3.12 python ../identity/test/generate-sealed-vectors.py --stdout)

import base64
import hashlib
import hmac
import json
import sys
from pathlib import Path

from nacl import bindings as b
from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey, VerifyKey

OUT = Path(__file__).with_name("sealed-vectors.json")
FORMAT = "agentland-sealed/1"
MAGIC = bytes.fromhex("414c5301")
OVERHEAD = 108
PAD_UNIT = 256
MIN_ENVELOPE = 364
MAX_ENVELOPE = 63_852
MAX_INNER = 63_744
DID = "did:web:agentland.us:agents:weatherwise"
OTHER_DID = "did:web:agentland.us:agents:otheragent"

# RESEARCH F2 / F2.1 / draft-irtf-cfrg-xchacha-03 section A.3.1 anchors.
ANCHOR_SHARED = "4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742"
ANCHOR_KEY = "d51914e663f68f0e60c8a9239cb8ddcd1ebb7c047b092baf2a2dbacd2369c82e"
ANCHOR_CONTENT_HASH = "142141121a3f4f341083806ec715c64d2cb1cdedffc9ef35d560269955c32838"
ANCHOR_RID = "f35e5616160a30bf3c6e79fa73c576d40205e8fc3ba4e1c6dcf93e6b98e857b4"
ANCHOR_KAT_PREFIX = "bd6d179d3e83d43b9576579493c0e939"
ANCHOR_KAT_TAG = "c0875924c1c7987947deafd8780acf49"
ANCHOR_REGISTER = "iP4HoBxwA9Np0gfQGs4q3uO0iT6UxsdjRs_NKgGHt2mo7oAx9fwBuEdiG-IzS1vqA2xBF1dVM7EuBUXATuTiBw"
ANCHOR_REVOKE = "8EVua95crxhFxwWE5HmThUOdj2N7OwUsxPeELBa9gekGsGa631-TNRzIrg57hFfwTRoOyN-SKIFN9zs3McLhAQ"

# RFC 7748 section 6.1: recipient = Bob, ephemeral = Alice.
R_PRIV = bytes.fromhex("5dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb")
E_PRIV = bytes.fromhex("77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a")
V1_NONCE = bytes.fromhex("404142434445464748494a4b4c4d4e4f5051525354555657")
SIGNING_SEED = bytes.fromhex("9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60")

# RESEARCH F3: the libsodium low-order blacklist.
LOW_ORDER = [
    "0000000000000000000000000000000000000000000000000000000000000000",
    "0100000000000000000000000000000000000000000000000000000000000000",
    "e0eb7a7c3b41b8ae1656e3faf19fc46ada098deb9c32b1fd866205165f49b800",
    "5f9c95bca3508c24b1d0b1559c83ef5b04445cc4581c8e86d8224eddd09f1157",
    "ecffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f",
    "edffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f",
    "eeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f",
]


# ---- primitives -----------------------------------------------------------------------------

def jcs(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def b64url(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def hkdf_sha256(ikm, salt, info, n):
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()
    okm, block, counter = b"", b"", 1
    while len(okm) < n:
        block = hmac.new(prk, block + info + bytes([counter]), hashlib.sha256).digest()
        okm += block
        counter += 1
    return okm[:n]


def label(text):
    return hashlib.sha256(text.encode("ascii")).digest()


def inner_length(n):
    return max(PAD_UNIT, -(-(4 + n) // PAD_UNIT) * PAD_UNIT)


def aad(did, key):
    return jcs({"did": did, "format": FORMAT, "key": key})


def derive(e_priv, r_pub):
    e_pub = b.crypto_scalarmult_base(e_priv)
    shared = b.crypto_scalarmult(e_priv, r_pub)
    return e_pub, shared, hkdf_sha256(shared, e_pub + r_pub, FORMAT.encode(), 32)


def meta_bytes(meta, size):
    return jcs({**meta, "size": size})


def build_inner(meta, body):
    m = meta_bytes(meta, len(body))
    raw = len(m).to_bytes(4, "big") + m + body
    return raw + bytes(inner_length(len(m) + len(body)) - len(raw))


def seal_inner(inner, r_pub, e_priv, nonce, did, key):
    """Seals arbitrary inner bytes (negatives use malformed inners)."""
    e_pub, _, k = derive(e_priv, r_pub)
    ct = b.crypto_aead_xchacha20poly1305_ietf_encrypt(inner, aad(did, key), nonce, k)
    return MAGIC + hashlib.sha256(r_pub).digest() + e_pub + nonce + ct


# ---- reference opener (agentland-sealed-1.md open order) ------------------------------------

class Refused(Exception):
    pass


def check_meta(raw):
    try:
        obj = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise Refused("meta")
    if (
        not isinstance(obj, dict)
        or sorted(obj) != ["content_type", "name", "size", "tags"]
        or jcs(obj) != raw
        or not isinstance(obj["content_type"], str)
        or not isinstance(obj["name"], str)
        or not isinstance(obj["tags"], list)
        or any(not isinstance(t, str) for t in obj["tags"])
        or isinstance(obj["size"], bool)
        or not isinstance(obj["size"], int)
        or obj["size"] < 0
    ):
        raise Refused("meta")
    return obj


def open_envelope(env, did, key, keyring):
    if env[:4] != MAGIC:
        raise Refused("magic")
    if len(env) < MIN_ENVELOPE or len(env) > MAX_ENVELOPE or (len(env) - OVERHEAD) % PAD_UNIT:
        raise Refused("length")
    secret = None
    for sk in keyring:
        if len(sk) != 32:
            raise Refused("public_key")
        if hashlib.sha256(b.crypto_scalarmult_base(sk)).digest() == env[4:36]:
            secret = sk
            break
    if secret is None:
        raise Refused("recipient_unknown")
    r_pub, e_pub, nonce = b.crypto_scalarmult_base(secret), env[36:68], env[68:92]
    try:
        shared = b.crypto_scalarmult(secret, e_pub)
    except Exception:
        raise Refused("low_order")
    k = hkdf_sha256(shared, e_pub + r_pub, FORMAT.encode(), 32)
    try:
        inner = b.crypto_aead_xchacha20poly1305_ietf_decrypt(env[92:], aad(did, key), nonce, k)
    except Exception:
        raise Refused("authentication")
    ml = int.from_bytes(inner[:4], "big")
    if 4 + ml > len(inner):
        raise Refused("meta_length")
    meta = check_meta(inner[4 : 4 + ml])
    size = meta["size"]
    if 4 + ml + size > len(inner):
        raise Refused("size")
    if any(inner[4 + ml + size :]) or len(inner) != inner_length(ml + size):
        raise Refused("padding")
    return meta, inner[4 + ml : 4 + ml + size]


def refusal(env, did, key, keyring):
    try:
        open_envelope(env, did, key, keyring)
    except Refused as e:
        return str(e)
    raise AssertionError("expected a refusal")


# ---- vectors --------------------------------------------------------------------------------

def sealed_vector(r_priv, e_priv, nonce, key, meta, body_text):
    r_pub = b.crypto_scalarmult_base(r_priv)
    e_pub, shared, k = derive(e_priv, r_pub)
    body = body_text.encode("ascii")
    inner = build_inner(meta, body)
    env = seal_inner(inner, r_pub, e_priv, nonce, DID, key)
    opened_meta, opened_body = open_envelope(env, DID, key, [r_priv])
    assert opened_meta == {**meta, "size": len(body)} and opened_body == body
    return {
        "aad_utf8": aad(DID, key).decode(),
        "aead_key_hex": k.hex(),
        "body_utf8": body_text,
        "did": DID,
        "envelope_hex": env.hex(),
        "envelope_sha256": hashlib.sha256(env).hexdigest(),
        "ephemeral_public_hex": e_pub.hex(),
        "ephemeral_secret_hex": e_priv.hex(),
        "inner_hex": inner.hex(),
        "key": key,
        "meta": meta,
        "meta_utf8": meta_bytes(meta, len(body)).decode(),
        "nonce_hex": nonce.hex(),
        "recipient_key_id": hashlib.sha256(r_pub).hexdigest(),
        "recipient_public_hex": r_pub.hex(),
        "recipient_secret_hex": r_priv.hex(),
        "shared_hex": shared.hex(),
    }


def xchacha_kat():
    key, nonce = bytes(range(0x80, 0xA0)), bytes(range(0x40, 0x58))
    ad = bytes.fromhex("50515253c0c1c2c3c4c5c6c7")
    text = (
        "Ladies and Gentlemen of the class of '99: If I could offer you only one tip for the "
        "future, sunscreen would be it."
    )
    ct = b.crypto_aead_xchacha20poly1305_ietf_encrypt(text.encode(), ad, nonce, key)
    assert ct.hex().startswith(ANCHOR_KAT_PREFIX) and ct[-16:].hex() == ANCHOR_KAT_TAG
    return {
        "aad_hex": ad.hex(),
        "ciphertext_hex": ct.hex(),
        "key_hex": key.hex(),
        "nonce_hex": nonce.hex(),
        "plaintext_utf8": text,
    }


def low_order():
    for u in LOW_ORDER:
        for bit in (0, 0x80):
            raw = bytes.fromhex(u)
            point = raw[:31] + bytes([raw[31] | bit])
            try:
                b.crypto_scalarmult(E_PRIV, point)
            except Exception:
                continue
            raise AssertionError(f"libsodium accepted low-order {point.hex()}")
    return {"encodings": LOW_ORDER}


def padding(v1):
    meta = {"content_type": "application/octet-stream", "name": "max.bin", "tags": []}
    size = MAX_INNER
    for _ in range(4):  # fixed point: the size digits are part of the meta bytes
        size = MAX_INNER - 4 - len(meta_bytes(meta, size))
    assert 4 + len(meta_bytes(meta, size)) + size == MAX_INNER
    body = bytes(i % 251 for i in range(size))
    r_pub = bytes.fromhex(v1["recipient_public_hex"])
    env = seal_inner(build_inner(meta, body), r_pub, E_PRIV, V1_NONCE, DID, v1["key"])
    assert len(env) == MAX_ENVELOPE
    assert open_envelope(env, DID, v1["key"], [R_PRIV])[1] == body
    cases = [[0, 256], [252, 256], [253, 512], [256, 512], [63740, 63744]]
    assert all(inner_length(n) == length for n, length in cases)
    return {
        "inner_length": cases,
        "max": {
            "body_length": size,
            "body_rule": "byte i = i mod 251",
            "envelope_length": len(env),
            "envelope_sha256": hashlib.sha256(env).hexdigest(),
            "meta": meta,
        },
    }


def negatives(v1):
    env = bytes.fromhex(v1["envelope_hex"])
    key, r_pub = v1["key"], bytes.fromhex(v1["recipient_public_hex"])
    meta, body = v1["meta"], v1["body_utf8"].encode("ascii")
    good = build_inner(meta, body)
    m = meta_bytes(meta, len(body))

    def pad(raw, length=256):
        return raw + bytes(length - len(raw))

    def framed(meta_raw, rest=body):
        return pad(len(meta_raw).to_bytes(4, "big") + meta_raw + rest)

    reordered = (
        '{"name":"notes/cpi.md","content_type":"text/plain; charset=utf-8",'
        '"size":59,"tags":["macro"]}'
    ).encode()
    inners = [
        ("meta-length-past-end", (0xFFF0).to_bytes(4, "big") + good[4:], "meta_length"),
        ("meta-not-canonical", framed(reordered), "meta"),
        ("meta-extra-member", framed(jcs({**meta, "size": len(body), "x": 1})), "meta"),
        ("meta-missing-member", framed(jcs({"content_type": meta["content_type"], "name": meta["name"], "size": len(body)})), "meta"),
        ("meta-size-not-integer", framed(jcs({**meta, "size": str(len(body))})), "meta"),
        ("size-past-end", framed(meta_bytes(meta, 400)), "size"),
        ("nonzero-padding", good[:-1] + b"\x01", "padding"),
        ("surplus-padding", pad(len(m).to_bytes(4, "big") + m + body, 512), "padding"),
    ]
    flipped = bytearray(env)
    flipped[200] ^= 1
    wrong_magic = bytearray(env)
    wrong_magic[3] = 0x02
    entries = [
        ("wrong-magic", bytes(wrong_magic), DID, key, R_PRIV, "magic"),
        ("length-363", env[:363], DID, key, R_PRIV, "length"),
        ("length-365", env + b"\x00", DID, key, R_PRIV, "length"),
        ("length-64108", None, DID, key, R_PRIV, "length"),
        ("recipient-unknown", env, DID, key, E_PRIV, "recipient_unknown"),
        ("aad-did", env, OTHER_DID, key, R_PRIV, "authentication"),
        ("aad-key", env, DID, key + "x", R_PRIV, "authentication"),
        ("tag-flip", bytes(flipped), DID, key, R_PRIV, "authentication"),
    ] + [
        (name, seal_inner(inner, r_pub, E_PRIV, V1_NONCE, DID, key), DID, key, R_PRIV, reason)
        for name, inner, reason in inners
    ]
    out = []
    for name, envelope, did, k, secret, reason in entries:
        entry = {"did": did, "key": k, "keyring_secret_hex": secret.hex(), "name": name, "reason": reason}
        if envelope is None:
            prefix, total = env[:92], 64_108
            entry.update({"prefix_hex": prefix.hex(), "total_length": total})
            envelope = prefix + bytes(total - len(prefix))
        else:
            entry["envelope_hex"] = envelope.hex()
        assert refusal(envelope, did, k, [secret]) == reason, name
        out.append(entry)
    return out


def enc_key(r_pub):
    signer = SigningKey(SIGNING_SEED)
    verify_key = VerifyKey(bytes(signer.verify_key))
    register = {"did": DID, "kind": "enc_key", "previous": None, "public_key": b64url(r_pub), "ts": "2026-11-01T12:00:00.000Z"}
    revoke = {"did": DID, "key_id": f"{DID}#key-2", "kind": "enc_key_revoke", "reason": "rotated", "ts": "2026-11-01T12:05:00.000Z"}

    def signed(statement, anchor):
        raw = jcs(statement)
        sig = b64url(signer.sign(raw).signature)
        assert sig == anchor
        return {"canonical_utf8": raw.decode(), "signature": sig, "statement": statement}

    active2 = {"active_key_id": f"{DID}#key-2"}
    revoke_ctx = {"active_key_id": f"{DID}#key-2", "now": "2026-11-01T12:05:00.000Z"}
    no_ts = {k: v for k, v in register.items() if k != "ts"}
    entries = [
        ("kind-wrong", {**register, "kind": "enc_key_rotate"}, None, "TypeError"),
        ("member-extra", {**register, "extra": 1}, None, "TypeError"),
        ("member-missing", no_ts, None, "TypeError"),
        ("public-key-31", {**register, "public_key": b64url(r_pub[:31])}, None, "TypeError"),
        ("public-key-33", {**register, "public_key": b64url(r_pub + b"\x00")}, None, "TypeError"),
        ("previous-malformed", {**register, "previous": f"{DID}#enc-2"}, active2, "TypeError"),
        ("reason-empty", {**revoke, "reason": ""}, revoke_ctx, "TypeError"),
        ("reason-201", {**revoke, "reason": "r" * 201}, revoke_ctx, "TypeError"),
        ("ts-not-utc-ms", {**register, "ts": "2026-11-01T12:00:00Z"}, None, "TypeError"),
        ("did-other-agent", {**register, "did": OTHER_DID}, None, "TypeError"),
        ("ts-early", {**register, "ts": "2026-11-01T11:54:59.999Z"}, None, "RangeError"),
        ("ts-late", {**register, "ts": "2026-11-01T12:05:00.001Z"}, None, "RangeError"),
        ("previous-null-while-active", register, active2, "RangeError"),
        ("revoke-not-active", revoke, {"active_key_id": f"{DID}#key-3", "now": "2026-11-01T12:05:00.000Z"}, "RangeError"),
        ("now-invalid", register, {"now": "not-a-date"}, "TypeError"),
    ] + [
        (f"public-key-low-order-{i}", {**register, "public_key": b64url(bytes.fromhex(u))}, None, "SealedEnvelopeError")
        for i, u in enumerate(LOW_ORDER)
    ]
    out = []
    for name, statement, context, error in entries:
        entry = {"error": error, "name": name, "statement": statement}
        if context is not None:
            entry["context"] = context
        out.append(entry)
    # A signature over non-canonical bytes must not verify the canonical statement.
    raw = json.dumps(dict(reversed(list(register.items()))), separators=(",", ":")).encode()
    assert raw != jcs(register) and json.loads(raw) == register
    try:
        verify_key.verify(jcs(register), signer.sign(raw).signature)
        raise AssertionError("non-canonical signature verified")
    except BadSignatureError:
        pass
    out.append({"canonical_utf8": raw.decode(), "error": "verify_false", "name": "non-canonical-signature"})
    return {
        "did": DID,
        "negatives": out,
        "register": signed(register, ANCHOR_REGISTER),
        "revoke": signed(revoke, ANCHOR_REVOKE),
        "signing_public_x": b64url(bytes(signer.verify_key)),
        "signing_seed_hex": SIGNING_SEED.hex(),
    }


def build():
    v1 = sealed_vector(
        R_PRIV, E_PRIV, V1_NONCE, "sealed/mfrggzdfmztwq2lknnwg23tpoa",
        {"content_type": "text/plain; charset=utf-8", "name": "notes/cpi.md", "tags": ["macro"]},
        "Remember: the July CPI print moved my priors on rate cuts.\n",
    )
    assert v1["shared_hex"] == ANCHOR_SHARED and v1["aead_key_hex"] == ANCHOR_KEY
    assert v1["envelope_sha256"] == ANCHOR_CONTENT_HASH and v1["recipient_key_id"] == ANCHOR_RID
    assert len(v1["envelope_hex"]) == 2 * 364 and len(v1["meta_utf8"]) == 93
    v2 = sealed_vector(
        R_PRIV, label("agentland-sealed/1 v2 ephemeral"), label("agentland-sealed/1 v2 nonce")[:24],
        "sealed/notes-2026", {"content_type": "application/json", "name": "", "tags": []},
        '{"note":"' + "x" * 280 + '"}',
    )
    assert len(v2["inner_hex"]) == 2 * 512 and len(v2["envelope_hex"]) == 2 * 620
    return {
        "conventions": {
            "aad": "RFC 8785 {did, format: agentland-sealed/1, key}",
            "envelope": "41 4c 53 01 || SHA-256(R_pub) || E_pub || nonce(24) || XChaCha20-Poly1305 ciphertext || tag(16)",
            "hex": "hex lowercase",
            "inner": "u32be(len(meta)) || meta || body || zero padding; meta = RFC 8785 {content_type, name, size, tags}",
            "kdf": "HKDF-SHA256(IKM = X25519(e, R_pub), salt = E_pub || R_pub, info = agentland-sealed/1, L = 32)",
            "negatives": "negatives give the first failing check in the open order of agentland-sealed-1.md",
            "padding": "inner length = max(256, ceil((4 + len(meta) + len(body)) / 256) * 256)",
        },
        "enc_key": enc_key(bytes.fromhex(v1["recipient_public_hex"])),
        "format": FORMAT,
        "generator": "packages/identity/test/generate-sealed-vectors.py (PyNaCl 1.6.2, libsodium; stdlib HKDF)",
        "low_order": low_order(),
        "negatives": negatives(v1),
        "padding": padding(v1),
        "v1": v1,
        "v2": v2,
        "xchacha_kat": xchacha_kat(),
    }


def check_ascii(value):
    if isinstance(value, str):
        assert value.isascii(), value
    elif isinstance(value, dict):
        for k, v in value.items():
            check_ascii(k)
            check_ascii(v)
    elif isinstance(value, list):
        for v in value:
            check_ascii(v)
    else:
        assert value is None or isinstance(value, int), value  # no floats


def main():
    data = build()
    check_ascii(data)
    out = jcs(data)
    if sys.argv[1:] == ["--stdout"]:
        sys.stdout.buffer.write(out)
    elif sys.argv[1:] == []:
        OUT.write_bytes(out)
    else:
        sys.exit("usage: generate-sealed-vectors.py [--stdout]")


if __name__ == "__main__":
    main()
