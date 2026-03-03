# SIGNN Protocol

**Version:** 0.1 (Draft)  
**Status:** Informational Draft  
**Intended Audience:** Operators of High-Risk AI Systems  
**Date:** March 2026  
**License:** Apache 2.0  

---
---

## About the Author

Tayi Saikishore is the CEO of DeployH AI and Founder of SIGNN.

His work focuses on building operational AI systems for regulated environments, with an emphasis on readiness, human oversight, and execution accountability.

The SIGNN Protocol emerges from practical deployment experience in high-risk domains, where AI decisions require traceability, governance binding, and verifiable execution context.

The concept of “Authority as Readiness Execution” reflects a design philosophy: authority in AI systems should derive not from model capability alone, but from measurable oversight, policy enforcement, and cryptographic accountability.

https://www.linkedin.com/in/saikishorenaidu/

---

## 1. Introduction

The SIGNN Protocol defines a cryptographic framework for binding AI-generated decisions to verifiable metadata.

While TLS/HTTPS secures communication channels, it does not provide integrity, traceability, or non-repudiation for AI decision artifacts. The SIGNN Protocol introduces a structured and signed decision envelope enabling post-execution verification and accountability.

The protocol is domain-neutral and intended for regulated environments requiring high-assurance AI governance.

---

## 2. Problem Definition

High-risk AI systems lack a standardized method to prove:

- Which model version generated a decision
- Whether governance policy was applied
- Whether required human oversight occurred
- Whether a decision has expired or been revoked
- Whether the output has been modified after issuance

This creates audit ambiguity, regulatory friction, and liability exposure.

---

## 3. Design Principles

The SIGNN Protocol adheres to:

1. Cryptographic Integrity  
2. Non-Repudiation  
3. Governance Binding  
4. Human Oversight Traceability  
5. Expiry & Revocation Enforcement  
6. Open and Vendor-Neutral Specification  

---

## 4. Decision Envelope Schema

All AI decisions MUST be encapsulated in a canonical JSON envelope prior to signing.

### Required Fields

{
  "decision_id": "string",
  "issuer": "string",
  "subject": "string",
  "model": {
    "name": "string",
    "version": "string",
    "hash": "sha256 string"
  },
  "policy": {
    "id": "string",
    "hash": "sha256 string"
  },
  "human_validation": {
    "required": true,
    "performed": true
  },
  "risk_score": 0.0,
  "issued_at": "ISO-8601 timestamp",
  "expires_at": "ISO-8601 timestamp"
}

The envelope MUST be:

Deterministically serialized
Hashed using SHA-256
Signed using an approved digital signature algorithm

## 5. Cryptographic Requirements

Recommended:

Ed25519 for digital signatures
SHA-256 for hashing
Deterministic JSON canonicalization
Regular key rotation

The signature object MUST include:

{
  "alg": "Ed25519",
  "kid": "key-id",
  "sig": "base64-signature"
}

Private keys SHOULD be protected via HSM, TPM, or secure KMS.

## 6. Authority Hierarchy

The SIGNN trust model is hierarchical:

SIGNN Root Authority
→ Domain Authority
→ Issuer Authority
→ Signed Decision

Public key discovery MUST be supported via:

https://issuer-domain/.well-known/signn-keys.json

## 7. Verification Procedure

A compliant verifier MUST:

Validate envelope structure
Confirm expires_at has not passed
Retrieve public key using kid
Verify signature
Check revocation status
Confirm policy hash integrity
Only after successful verification SHALL the decision be treated as valid.

## 8. Revocation Model

Two revocation layers are defined:
Decision Revocation List (DRL)
Authority Revocation List (ARL)
Revoked decisions MUST be treated as invalid even if signature verification succeeds.

## 9. Security Considerations

The SIGNN Protocol:

Does not guarantee correctness of AI outputs
Does not replace regulatory certification
Does not define model training standards
It provides cryptographic accountability infrastructure only.

## 10. Future Work

Future versions MAY include:
Transparency log integration
Formal JSON Canonicalization Scheme adoption
Domain-specific compliance profiles
Standardized audit APIs

End of Specification.
