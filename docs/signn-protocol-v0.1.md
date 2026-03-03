# SIGNN Protocol

**Version:** 0.1 (Draft)  
**Status:** Informational Draft  
**Intended Audience:** Operators of High-Risk AI Systems  
**Date:** March 2026  
**License:** Apache 2.0  

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

json
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
