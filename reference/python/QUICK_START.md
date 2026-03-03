# SIGNN Protocol – Python Reference Implementation

This minimal example demonstrates:

- Deterministic JSON canonicalization
- Ed25519 signing
- Signature verification

---

## 1. Setup Virtual Environment

bash
cd reference/python
python -m venv .venv

Activate:

macOS / Linux

source .venv/bin/activate

Windows

.venv\Scripts\activate
2. Install Dependencies
pip install -r requirements.txt
3. Run Demo
python signn_ed25519_demo.py

Expected output:

Signature valid: True

The script will print a signed decision envelope including:

envelope

signature (Ed25519)

key id (kid)
