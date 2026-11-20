# OSF Registration — draft (copy-paste into an OSF Registration form)

**Where to register:** OSF Registries (https://osf.io/registries) — use the *PRISMA-based*
or *Open-Ended Registration* template. PROSPERO is **not** applicable: it accepts only
reviews with a health-related outcome, and this is a computing/software-architecture mapping
review. Registering on OSF gives a citable, time-stamped DOI and satisfies the Q1
"pre-registered protocol" expectation.

**Registration type:** Prospective-amended (the review began, then the protocol was amended
to the multi-source design before the final screening — disclose this honestly in §Amendments;
OSF allows registering a protocol mid-review as long as the amendment history is transparent).

> Fields below map to the OSF form. [BRACKETS] = author must fill. Everything else is drawn
> from the frozen protocol and the completed re-run; proposals only, adapt to the manuscript.

---

## Title
A Systematic Mapping Review of Control-Plane Architectures for Agentic AI / LLM Systems
[adjust to the manuscript's exact title]

## Authors / Contributors
[Author 1, ORCID, affiliation — University of the Cumberlands] · [Author 2 …] · [Author 3 …]
Corresponding: [name, email]

## Description / Abstract
We map the literature on control-plane architectures for LLM-based and agentic AI systems —
tool/function calling, retrieval (RAG/GraphRAG), serving and LLMOps, multi-agent
orchestration, agent interoperability protocols (MCP/A2A/ACP/ANP), agent security, governance,
and observability. The review is reported per PRISMA-ScR (Tricco et al., 2018) as a
reproducible mapping sample, not an exhaustive census. We identify records via OpenAlex (open,
cross-publisher) with the ACM Digital Library as a second primary database, screen a
citation-ordered tier plus a living 2026 tier by two independent raters, and recover
title-missed studies by backward snowballing.

## Review type
Systematic mapping / scoping review (PRISMA-ScR).

## Research questions
- RQ1. What architectural patterns, systems, and protocols constitute the "control plane" for
  agentic/LLM systems, and how do they map onto the 13 thematic clusters?
- RQ2. What evaluation methods, benchmarks, and datasets are used for these components?
- RQ3. What security, governance, and observability concerns are reported, and how are they
  addressed?
- RQ4. Where are the open gaps and under-studied clusters?
[trim/extend to match the manuscript]

## Hypotheses
None — this is a descriptive mapping review, not a hypothesis test. (OSF requires a response;
state "Not applicable — descriptive mapping review.")

## Information sources
- **Primary databases (2):** OpenAlex (Priem et al., 2022; indexes IEEE, ACM, Springer/LNCS,
  Elsevier, AAAI, ACL Anthology, arXiv) and the **ACM Digital Library** (same 13 title-scoped
  clusters, authenticated institutional session).
- **Coverage probes (counts only):** IEEE Xplore, ScienceDirect (Elsevier), Scopus, Crossref,
  Semantic Scholar Graph API.
- **Not searched:** Web of Science (no institutional access) — logged as unresolved.
- **Supplementary:** backward snowballing from included seeds via OpenAlex reference links.
- **Last search executed:** 19 November 2026. A living tier refreshes 2026 records.

## Search strategy (full, reproducible)
Thirteen cluster queries, one per control-plane theme, executed title-scoped as exact-phrase
streams, 2019–2026, unioned and de-duplicated by work identifier. ACM used the same phrase
lists with `Title:(group A) AND Title:(group B)`. Exact strings:

| # | Cluster | Query (phrase groups) |
|---|---|---|
| C1 | LLM agents | ("LLM agent" OR "large language model agent" OR "LLM-based agent") |
| C2 | Function/tool calling | ("LLM" OR "large language model") AND ("function calling" OR "tool calling" OR "tool invocation") |
| C3 | Agentic RAG | ("agentic RAG" OR "agentic retrieval-augmented" OR "self-RAG" OR "iterative retrieval") AND ("LLM" OR "large language model") |
| C4 | GraphRAG | ("GraphRAG" OR "graph retrieval-augmented") AND ("knowledge graph" OR "LLM" OR "large language model") |
| C5 | LLMOps / serving | ("LLMOps" OR "LLM serving" OR "large language model operations" OR "model serving") AND ("pipeline" OR "deployment" OR "lifecycle" OR "inference") |
| C6 | Kubernetes / serverless | ("Kubernetes" OR "serverless" OR "cloud-native") AND ("LLM" OR "large language model") AND ("serving" OR "inference" OR "deployment") |
| C7 | Agent security | ("LLM agent" OR "LLM-based agent" OR "agentic AI system") AND ("security" OR "attack" OR "threat" OR "vulnerability") |
| C8 | Prompt injection | ("prompt injection" OR "indirect prompt injection" OR "tool poisoning") AND ("LLM" OR "large language model" OR "agent") |
| C9 | Multi-agent / orchestration | ("LLM-based multi-agent" OR "multi-agent LLM" OR "LLM multi-agent" OR "agent orchestration") AND ("LLM" OR "large language model") |
| C10 | Interoperability | ("agent interoperability" OR "agent protocol" OR "agent communication protocol") AND ("LLM" OR "large language model" OR "agentic") |
| C11 | MCP / A2A / ACP / ANP | ("Model Context Protocol" OR "Agent2Agent" OR "Agent Communication Protocol" OR "Agent Network Protocol") |
| C12 | Governance / policy | ("AI governance" OR "policy-as-code" OR "runtime policy enforcement") AND ("LLM" OR "agent" OR "agentic") |
| C13 | Observability / tracing | ("observability" OR "distributed tracing" OR "OpenTelemetry") AND ("LLM" OR "large language model" OR "agentic") |

Harvest code (`openalex_harvest.py`) and the ACM record list are released so identification is
reconstructable.

## Eligibility criteria
- **Include** if the primary contribution is a generalizable control-plane artifact — a method,
  system, benchmark, dataset, protocol, reference architecture, evaluation, taxonomy, or
  security analysis — for LLM/agentic systems, addressing ≥1 cluster.
- **Method-in-domain sub-rule (pre-agreed):** a benchmark/dataset/method evaluated across ≥2
  domains or framed as domain-general is included; a single-domain deployment with no
  transferable artifact is excluded (E6).
- **Exclude codes:** E1–E8, with E3 duplicate, E6 out-of-scope/single-domain application,
  E7 not-a-contribution (book, keynote, editorial, tutorial, front/back matter), E8 wrong
  language/year.
- **Window:** 2019–2026. **Language:** English.

## Study selection process
Records ordered by citation count to prioritise the screening queue (citation count was **not**
an inclusion criterion — ordering only). Title+abstract screened by two independent raters;
disagreements reconciled; Cohen's κ reported per tier. Two-tier corpus: a frozen primary tier
(screened in full) plus a living 2026 tier (relevance-screened, refreshed). Backward snowball
screened under identical criteria.

## Data extraction / items
Per included study: identifier (DOI/OpenAlex id), year, venue, cluster membership(s),
contribution type (method/system/benchmark/dataset/protocol/architecture/evaluation/taxonomy/
security), evaluation present (y/n), and mapped RQ. Extraction performed by [one / two]
reviewer(s) [with/without independent check].

## Synthesis
Narrative + tabular mapping by cluster and contribution type; no meta-analysis (heterogeneous,
non-comparable outcomes).

## Results recorded at registration (for a prospective-amended registration, disclose current state)
- Identified: **17,682** unique (OpenAlex 12,021; ACM second-database net-new 28; snowball 5,633).
- ACM second database: 278 unique, 250 (90%) already in OpenAlex, 28 net-new → 3 included
  (κ = 1.00 on that tier).
- Screened: 1,620 (dual-rated; primary κ = 0.45, snowball κ = 0.63, ACM κ = 1.00).
- **Included: 898** (primary 657 + snowball 238 + ACM 3).
- Prior-corpus reproduction at identification: 75/119 (67% in-window) vs 31/69 IEEE-only pilot.

## Protocol amendments (disclose honestly)
1. Pilot was IEEE-Xplore-only; it reproduced 31/69 previously cited systematic references.
2. Amended (dated) to a multi-source design with OpenAlex primary — reproduction rose to 56/119,
   then 75/119 with snowballing.
3. C1 and C7 phrase lists re-tightened from v2 to v3 before screening (off-topic LLM dominance);
   frozen in `protocol_v3_frozen_queries.md`.
4. ACM Digital Library added as a second primary database (2026-11-19) to test single-source
   dependence.
All amendments and dates are in the released protocol files.

## Timeline
Search start [date] · protocol amended [date] · last search 2026-11-19 · screening complete
2026-11-19 · manuscript in preparation.

## Funding / Conflicts of interest
[Funding sources or "None."] · [COI statement or "The authors declare no competing interests."]

## Data, code, and materials availability
Reproducibility package (this repository) to be deposited on OSF/Zenodo: frozen queries,
`openalex_harvest.py`, `acm_records.py` + `dedup_acm.py`, ranked queue, screening workbooks and
reconciliations, PRISMA-ScR flow and checklist, methods and limitations. See
`README_reproducibility.md`.

## License
[CC-BY-4.0 recommended for the protocol/data]
