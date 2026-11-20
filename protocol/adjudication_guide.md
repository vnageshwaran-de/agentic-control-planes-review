# Second-rater adjudication guide — the 470 unsure records

Companion to `unsure_for_review.csv` (470 unique records whose best status across all
clusters is *unsure*). These were **flagged, not resolved**, during the re-run. This guide
gives the rules to resolve each one to **include** or **exclude (with an E-code)**.

## How to use
1. Open `unsure_for_review.csv`. Each row is one record, with its `docid`, `year`, `title`,
   and `unsure_in_clusters` (the cluster(s) that flagged it).
2. Pull the record on IEEE Xplore: `https://ieeexplore.ieee.org/document/<docid>`.
   (12 C6 rows are keyed by DOI tail and have no title/docid — look them up by DOI.)
3. Read the abstract, then fill `reviewer_decision_include_or_exclude`, and
   `reviewer_exclusion_code` if excluding. Add a short `reviewer_notes` for any non-obvious call.
4. Two raters should score independently; compute inter-rater agreement (Cohen's κ) and
   reconcile disagreements, consistent with the second-rater (R2) method already in the paper.

## Why these were flagged
The deterministic pre-sort (screen_classifier2.py) marked a record *unsure* when its title
contained **both** a general control-plane signal (method/benchmark/framework/protocol/
survey/security term) **and** a domain-application signal (medical, power, telecom,
vehicle, education, finance, etc.) — "method-in-domain" — or **neither** signal
("no-signal"). The title alone could not decide scope, so the abstract is needed.

## The decision rule (apply uniformly)
Include if, on reading the abstract, the paper's **primary contribution** is a
generalizable control-plane artifact — a method, system, benchmark, dataset, protocol,
reference architecture, evaluation, taxonomy, or security analysis — that transfers beyond
one vertical, and it addresses ≥1 cluster (tool-calling, RAG/retrieval, serving/LLMOps,
orchestration/multi-agent, protocols/interoperability, security, governance, observability).

Exclude with:
- **E6 (out-of-scope / domain application)** — the contribution is a vertical system and the
  agent/LLM/graph/tooling is applied machinery, not the advance. This is the most common
  call for these records. Includes "agents FOR security" (pentest, red-team, IDS,
  threat-hunting, vuln-patching) — exclude; "security OF agents" stays include.
- **E7 (not a contribution)** — trade book, keynote, tutorial abstract, workshop
  front-matter, editorial, panel.
- **E3 (duplicate)** — same work as an already-included record (note the twin's docid).
- **E8 (wrong language/year)** — non-English or outside 2019–2026 (rare; the search filtered).

Keep *unsure* only if the abstract genuinely cannot settle it; escalate those to a third rater.

## Cluster-specific notes (where the borderline sits)
- **C1 LLM agents (133)** — the broadest pile. Many are "LLM agent for <vertical>"
  deployments → E6. Include agent *frameworks, surveys, reasoning/planning/memory methods,
  evaluations*. A single-domain case study with no transferable method → E6.
- **C9 Multi-agent / orchestration (103)** — include coordination/orchestration/role/
  communication *methods, frameworks, benchmarks*; exclude multi-agent systems built for one
  domain (a multi-agent pipeline for radiology, grid dispatch, etc.) → E6.
- **C11 MCP / A2A (99)** — include MCP/A2A *protocol work, servers, security, registries,
  interoperability, benchmarks*; exclude an MCP integration that is really a vertical app → E6.
- **C12 Governance / policy (41)** — include *technical* runtime policy enforcement,
  policy-as-code, guardrails, access control, audit/attestation for agents; exclude
  high-level AI-ethics/EU-AI-Act *commentary* without an enforceable mechanism → E6 (or
  E7 if a position/opinion piece).
- **C5 LLMOps / serving (40)** — the "no-signal" rows here are often **classical ML/DNN
  serving** with no LLM/agent content (recommendation, federated, CNN serving). For a
  control-plane survey of *LLM/agentic* systems, exclude non-LLM serving → E6, unless it is
  a foundational serving system the survey deliberately cites as an anchor.
- **C13 Observability (31)** — include observability/tracing/telemetry *for LLM/agent
  systems*; exclude general microservices observability that only name-drops LLMs → E6.
- **C4 GraphRAG (27)** — include general GraphRAG/graph-retrieval *methods, surveys,
  benchmarks*; exclude domain knowledge-graph QA systems → E6.
- **C8 (23) / C7 (13) / C2 (18)** — mostly genuine security/tool-calling contributions in a
  domain wrapper; include if the attack/defense/benchmark/tool-calling method is general.
- **C3 (4) / C6 (12) / C10 (3)** — small; decide case-by-case on the same rule.

## After adjudication
Move resolved rows into the master screening set (include → the included corpus with its
cluster tag; exclude → with its E-code). Recompute the PRISMA "included" figure in
`prisma_counts.md` and re-run the reconciliation so the final included set reflects the
human decisions, not the title-level pre-sort.

## Calibration sub-rule for the 129 disagreements (added after R1/R2 round, kappa=0.47)
R1 and R2 diverged systematically: 119 of 129 disputes are R1-exclude / R2-include, i.e.
whether a general method/benchmark *demonstrated in* a vertical counts as in-scope. Agree
on this one line first, then most of the 129 resolve in a batch:

> **A benchmark, dataset, or method evaluated across >=2 domains, or framed as
> domain-general, = INCLUDE. A single-domain deployment with no transferable artifact = E6.**

The Reconcile tab carries a non-binding title-level "Suggested" column applying this rule;
confirm each against the abstract before entering FINAL.
