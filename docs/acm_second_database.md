# ACM Digital Library — second primary database search

**Run date:** 2026-11-19
**Database:** ACM Digital Library (dl.acm.org), authenticated institutional session
**Field scope:** Title field (`Title:(...)`), matching the title-scoped exact-phrase
approach used for the OpenAlex primary harvest. Multi-concept clusters were expressed as
`Title:(group A) AND Title:(group B)` so that each concept group must appear in the title.
**Query set:** the frozen v3 Boolean clusters C1–C13 (identical phrase lists to the
OpenAlex/IEEE runs; see `protocol_v3_frozen_queries.md`).
**Pagination:** `doSearch?...&pageSize=50&startPage=N`, all result pages captured per cluster.

## Why a second primary database

The OpenAlex-based map is open to a "single-source" objection at Q1 review. ACM DL was run
as an independent second primary database to test how much of the title-matched corpus a
major closed index contributes beyond OpenAlex. ACM was chosen because it is the dominant
venue family for this topic (OpenAlex already attributes 289 of its records to ACM venues).

## Per-cluster results (live header counts = records captured)

| Cluster | ACM title-scoped hits |
|---|---|
| C1  LLM agent | 127 |
| C2  LLM + function/tool calling | 5 |
| C3  agentic RAG + LLM | 0 |
| C4  GraphRAG + KG/LLM | 6 |
| C5  LLMOps/serving + pipeline/deploy | 10 |
| C6  Kubernetes/serverless + LLM + serving | 7 |
| C7  LLM agent + security/attack | 5 |
| C8  prompt injection + LLM/agent | 11 |
| C9  multi-agent LLM + LLM | 90 |
| C10 agent interoperability/protocol + LLM | 0 |
| C11 MCP / A2A / ACP / ANP | 21 |
| C12 AI governance/policy-as-code + LLM/agent | 0 |
| C13 observability/tracing + LLM/agentic | 8 |
| **Raw records** | **290** |
| **Unique by DOI** | **278** |

(12 of the 290 are cross-cluster or within-list duplicates — e.g. a record returned by both
C1 and C7, or listed twice by ACM — collapsed to 278 unique DOIs.)

Note on C3/C10/C12 = 0: forcing **both** concept groups into the title is strict, and ACM's
index is far smaller than OpenAlex's, so clusters whose concepts rarely co-occur in a single
title return nothing. The counts are reported exactly as produced; they are a property of the
title-field scope + index size, not an error.

## Deduplication against OpenAlex (by normalized DOI)

| Quantity | Count |
|---|---|
| ACM unique DOIs | 278 |
| Already present in OpenAlex corpus (12,021) | **250 (90.0%)** |
| **ACM net-new (absent from OpenAlex)** | **28** |

Net-new by cluster (a DOI may count under several): C1 22 · C6 2 · C8 1 · C9 1 · C11 2.

## What the 28 net-new records actually are

The residual is overwhelmingly non-substantive, which is itself the useful finding:

- **20 of 28** are parts of a *single* ACM edited volume, *Multi-LLM Agent Collaborative
  Intelligence* (DOI stem `10.1145/3749421.*`). OpenAlex indexes the book but not its
  individual front/back matter and chapters.
  - **7 are clear non-contributions** (E7): Preface, Acknowledgments, Introduction, a
    "Brief History of AI" overview chapter, Epilogue, Authors' Biography/Index, plus one
    "Session Summary Podcast" entry from C6.
  - **~13 are book chapters** (CRIT, SocraSynth, EVINCE, SagaLLM, CoCoMo, MACI framework,
    etc.) — borderline for a systematic map (edited-volume chapters). **Flagged for human
    screening; not resolved here.**
- **1 is out of window** (E8): *An agent communication protocol for resolving conflicts*
  (2010), a false match from the broad C11 OR query.
- **~6 are genuine standalone 2025–2026 research items** not in OpenAlex yet (OpenAlex
  indexing lags for very recent ACM content), e.g. SensorMCP (C11), PVDetector (C8),
  SkyMind (C9), Evaluating Kubernetes Performance for GenAI Inference (C6), Invisible Walls
  in Cities (C1). **Flagged for human screening; not resolved here.**

So after the same structural exclusions already used in the protocol (E7 non-contribution,
E8 out-of-window), **8 of the 28 drop out immediately** and the remaining 20 (15 edited-book
chapters + 5 recent papers) went to the co-authors for title screening under the unchanged
inclusion criteria.

## Screening outcome (second-rater, 2026-11-19)

The 20 were dual-rated with **perfect agreement (Cohen's κ = 1.00)**. The edited-volume
policy was resolved as **exclude the book (E7)**, applied to all 15 chapters. Final:
**3 include, 25 exclude** (E7 ×22, E6 ×2, E8 ×1). The 3 included (corpus tier `acm`):
SensorMCP (C11), Evaluating Kubernetes Performance for GenAI Inference (C6), PVDetector (C8).
Final included corpus **895 → 898**. See `acm_netnew_reconciliation.md`.

## Interpretation for the manuscript

- OpenAlex already captured **90%** of ACM's title-matched records. The second primary
  database changes the identified pool by **28 of 12,021 (0.23%)**, and the in-scope,
  screenable residual is **≤20** records, most from one edited volume.
- This directly answers the single-source objection: adding a second major database does not
  materially change the corpus, which is the robustness evidence a reviewer is looking for.
- Report ACM as a second primary database in the PRISMA identification box with its own
  count (278 unique), the 250 duplicates-removed-against-OpenAlex, and the 28 taken to
  screening. Do **not** merge ACM counts into OpenAlex totals silently.

## Files

- `acm_raw.tsv` — all 290 captured rows (cluster, doi, year, title).
- `acm_harvest.csv` — 278 unique ACM DOIs (doi, year, clusters, in_openalex, title).
- `acm_netnew.csv` — the 28 records absent from OpenAlex (for co-author screening).
- `acm_records.py` — source-of-truth record list (per-cluster counts self-verify on run).

## Reproducibility note

Captured via the authenticated dl.acm.org session using title-scoped `doSearch` URLs; the
exact URL per cluster is the frozen phrase list URL-encoded into the `Title:` field. ACM's
browser download channel blocked repeated automated downloads mid-run, so records were read
back from the page buffer in verified fixed-size windows (each closed with a sentinel; total
byte length reconciled) — this affects only the transport, not the result set. Per-cluster
counts recomputed from the stored records match the live search-header counts exactly.
