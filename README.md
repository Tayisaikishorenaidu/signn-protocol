[![Release](https://img.shields.io/badge/release-v0.1--draft-blue)](https://github.com/Tayisaikishorenaidu/signn-protocol/releases/tag/v0.1-draft)

# SIGNN Protocol

**Version:** v0.1 (Draft)  
**Status:** Open Specification Proposal  
**License:** Apache 2.0  

---

## Overview

The SIGNN Protocol defines a cryptographic framework for binding AI-generated decisions to verifiable metadata, including:

- Model identity and version
- Governance policy binding
- Human oversight metadata
- Timestamp and expiry enforcement
- Revocation capability

While TLS/HTTPS secures transport channels, it does not provide cryptographic accountability for AI decision artifacts.  
The SIGNN Protocol introduces a signed decision envelope format enabling post-execution verification and auditability.

The protocol is designed for high-risk AI systems operating in regulated environments.

---

## Problem Statement

High-risk AI systems currently lack a standardized mechanism to prove:

- Which model version produced a decision  
- Whether governance policies were applied  
- Whether required human oversight occurred  
- Whether a decision has expired or been revoked  
- Whether the output has been altered after issuance  

This creates regulatory ambiguity, audit friction, and liability exposure.

---

## Core Design Principles

1. Cryptographic Integrity  
2. Non-Repudiation  
3. Policy Binding  
4. Human-in-the-Loop Accountability  
5. Expiry & Revocation  
6. Open and Vendor-Neutral Standard  

---

## Decision Envelope (Simplified Example)

```json
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

The envelope MUST be canonicalized, hashed, and signed using an approved cryptographic algorithm (Ed25519 recommended).

## Reference Implementation

A minimal Python reference implementation is provided:

- Canonicalizes the decision envelope
- Signs with Ed25519
- Verifies signature over the canonicalized envelope

See: `reference/python/signn_ed25519_demo.py`

```markdown
## minimal Python reference Implementation

A minimal Python reference implementation is available:

→ See `reference/python/QUICK_START.md`

## Regulatory Alignment

An informative mapping to EU AI Act high-risk system requirements is provided:

→ See: EU AI Act Mapping Appendix

## This mapping demonstrates structural alignment for:

      - Traceability
    
      - Logging & Record-Keeping
    
      - Human Oversight
    
      - Post-Market Monitoring

## Repository Structure

      - signn-protocol-v0.1.md — Full Specification
      
      - eu-ai-act-mapping.md — Regulatory Alignment Appendix
      
      - LICENSE — Apache 2.0

## Governance

The SIGNN Protocol is proposed as an open specification.
Future governance may be transitioned to a neutral working group.

SIGNN (company) acts as the initial reference implementer.

## Status

This is an early draft (v0.1).
Feedback, critique, and formal review are welcome.

