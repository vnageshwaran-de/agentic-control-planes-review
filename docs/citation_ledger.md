# Source-Level Citation Inclusion Ledger

Generated from `references.bib` (the live submission bibliography). Each of the 149 entries is assigned one category and one source tier. This ledger reconciles the bibliography against the included-study corpus, addressing the review request to document how the 148-entry bibliography relates to the systematic corpus.

## Reconciliation summary

| Source tier | Count | Meaning |
|---|---:|---|
| Systematic (IEEE Xplore + ACM DL search) | 76 | Cluster-keyed `cN-*` results of the 13-cluster Boolean search |
| Snowball / supplementary | 48 | Additional peer-reviewed papers reached by backward/forward snowballing (incl. 2 first-author domain self-citations) |
| Specifications & standards | 12 | MCP, A2A, ACP, ANP, NIST AI RMF, NIST GenAI Profile, OWASP LLM Top 10, OWASP Agentic, OAuth 2.0 BCP, OAuth 2.1 draft, OpenTelemetry GenAI, Kubernetes arch |
| Pre-2019 foundational anchors | 6 | SDN / service-mesh lineage (OpenFlow, SDN survey, control-plane surveys, service-mesh studies) |
| USENIX / Elsevier venue anchors | 4 | Security-venue items captured by snowballing outside IEEE/ACM |
| Adjacent-survey self-citations | 2 | The authors' two closest prior surveys |
| Data artifact | 1 | The audit kit's own Zenodo/GitHub release |
| **Total** | **149** | |

## Key finding for §II accounting

- Peer-reviewed research papers total **124** (76 systematic + 48 snowball/supplementary), **not 91** as stated in §II-A / Figure 2.
- The manuscript's "91 research papers" matches neither the systematic subset (76) nor the full research set (124). The count must be reconciled to one explicit definition.
- Specifications total **12** (the text says 11; the extra one is the newly added OAuth 2.1 draft — update "11" to "12" or drop the draft).
- The 13 anchor/venue/survey additions from this revision are correctly outside the systematic corpus and should be reported as separately counted anchors.

## Full ledger

See `citation_ledger.csv` for the per-entry table (key, type, year, category, source_tier, first_author, venue, title).
