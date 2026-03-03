import base64
import json
from dataclasses import dataclass
from typing import Any, Dict, Tuple

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, NoEncryption


def canonical_json_bytes(obj: Any) -> bytes:
    """
    Deterministic canonicalization for signing.
    NOTE: This is a practical canonicalization (sorted keys + compact separators).
    If you later want strict JSON Canonicalization Scheme (RFC 8785), you can upgrade.
    """
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def generate_keypair() -> Tuple[bytes, bytes]:
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(
        encoding=Encoding.Raw,
        format=PrivateFormat.Raw,
        encryption_algorithm=NoEncryption(),
    )
    public_bytes = public_key.public_bytes(
        encoding=Encoding.Raw,
        format=PublicFormat.Raw,
    )
    return private_bytes, public_bytes


def sign_envelope(envelope: Dict[str, Any], private_key_raw: bytes) -> Dict[str, Any]:
    """
    Returns a SIGNN-style signed decision object:
      { "envelope": {...}, "signature": { "alg", "kid", "sig" } }
    """
    # Important: signature must NOT include itself in the signed bytes.
    signing_bytes = canonical_json_bytes(envelope)

    private_key = Ed25519PrivateKey.from_private_bytes(private_key_raw)
    sig = private_key.sign(signing_bytes)

    signed = {
        "envelope": envelope,
        "signature": {
            "alg": "Ed25519",
            "kid": envelope.get("issuer_key_id", "signn-root-2026-01"),
            "sig": base64.b64encode(sig).decode("ascii"),
        },
    }
    return signed


def verify_signed_decision(signed: Dict[str, Any], public_key_raw: bytes) -> bool:
    """
    Verifies signature over canonicalized envelope.
    """
    envelope = signed.get("envelope")
    sig_obj = signed.get("signature") or {}

    if not isinstance(envelope, dict):
        return False
    if sig_obj.get("alg") != "Ed25519":
        return False
    if "sig" not in sig_obj:
        return False

    sig = base64.b64decode(sig_obj["sig"])
    verify_bytes = canonical_json_bytes(envelope)

    public_key = Ed25519PublicKey.from_public_bytes(public_key_raw)
    try:
        public_key.verify(sig, verify_bytes)
        return True
    except Exception:
        return False


def main() -> None:
    # Example SIGNN envelope (minimal v0.1)
    envelope = {
        "decision_id": "SAI-2026-0001",
        "issuer": "SIGNN",
        "issuer_key_id": "signn-root-2026-01",
        "subject": "clinic:lakshmi",
        "model": {"name": "signn-readiness", "version": "1.4.2", "hash": "sha256:abc123"},
        "policy": {"id": "SIGNN-HG-1.2", "hash": "sha256:def456"},
        "human_validation": {"required": True, "performed": True},
        "risk_score": 0.18,
        "issued_at": "2026-03-03T16:30:00Z",
        "expires_at": "2026-03-03T16:45:00Z",
        "output": {"status": "GREEN", "recommendations": ["hydrate", "break 5 min"]},
    }

    private_raw, public_raw = generate_keypair()

    signed = sign_envelope(envelope, private_raw)
    ok = verify_signed_decision(signed, public_raw)

    print("Signature valid:", ok)
    print("\nSIGNED OBJECT:\n")
    print(json.dumps(signed, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
