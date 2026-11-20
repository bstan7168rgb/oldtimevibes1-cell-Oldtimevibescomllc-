# Old-Time Vibes LLC — Master Ecosystem README (`README.md`)

**Governing Entity:** Old-Time Vibes LLC (Ponca City & McCord, Oklahoma | D-U-N-S: `14-219-7315`)  
**Founder, Principal Systems Architect & CEO:** Stanley Joseph Brown ("Kodak")  
**Primary Domains:** `https://oldtimevibes.com` | `https://genxnext.online` | `https://genx.online` | `https://online.genxnext.app`  
**Contact:** `oldtimevibes1@gmail.com`  
**Patent Priority Anchor:** November 28, 2025 (`USPTO-EXP-OTV-R2IO-2026-01` — 20-Claim Utility Patent Portfolio; Nonprovisional Conversion Deadline: **November 28, 2026**)  

---

## 1. Executive Overview

Old-Time Vibes LLC engineers sovereign, local-first edge computing hardware, humanoid robotics, privacy-hardened AI companions, and decentralized agentic commerce infrastructure. By decoupling on-device neural processing and hardware safety interlocks from continuous third-party cloud telemetry, every platform operates with deterministic low latency, strict zero-PII child and patient privacy compliance (COPPA, HIPAA, CIPA, ASTM F963-23), and automated cryptographic auditability.

---

## 2. Modular Department & Repository Architecture

All repositories, cloud environments, and hardware/software deliverables follow Old-Time Vibes LLC's four-department organizational hierarchy:

```text
old-time-vibes-ecosystem/
├── 01_hardware/
│   ├── cad_models/          # OpenSCAD, FreeCAD TechDraw & Onshape assemblies (R2IO, Barnaby capsule)
│   ├── bom/                 # Verified bills of materials & manufacturer RFQ specs (platform_parts_manifest.csv)
│   └── firmware/            # ESP32-S3 bare-metal RTOS (ESP-IDF/ADF), RK3588 C++20 enclaves, eFuse & QA jigs
├── 02_software/
│   ├── edge_ai/             # Quantized SLMs (GGUF/INT4), <300 KB LiteRT KWS/VAD, Software LOTO, PTT listener
│   ├── orchestration/       # FastMCP servers (:8000/:8080), Express MCP Gateway, Cloudflare Workers, UCP/A2A
│   └── interfaces/          # Web storefronts (oldtimevibes.com, genxnext.online), Android 16 app, MV3 extension
├── 03_operations/
│   ├── corporate_legal/     # Form C Reg CF disclosures, Mutual NDAs, LICENSE.md, NOTICE.md, TERMS.md, PRIVACY.md
│   ├── treasury/            # Stripe Connect UCP settlement hooks, Addendum V3 waterfall, Base L2 contracts
│   └── patents/             # USPTO 20-claim DOCX specs, formal vector drawings, DTSA trade-secret walls
└── 04_creative/
    ├── publishing/          # White papers (OTV-WP-2026-004-REV2), The Gemini Tales, Human-AI Collaboration series
    ├── audio_production/    # Workshop playlists, Suno stems, ISRC/ISWC audio POD middleware
    └── media_assets/        # Barnaby's Animals & Agents episodes, XR 3D apparel assets, Merchant Center feeds
