# Methods — reproducible multi-source mapping review (PRISMA-ScR)
Draft methods text + PRISMA flow for the control-plane survey, Q1-acceptable framing.
Proposals only; adapt to the manuscript. All counts are from the 2026-11-17/19 re-run.

## Framing (important)
Report this as a **systematic mapping / scoping review under PRISMA-ScR**, not an exhaustive
census. This is the framing that makes a bounded, reproducible corpus acceptable at a Q1
venue (and is the framing the authors' related AI Review survey used successfully). Do not
claim completeness; claim a reproducible, auditable mapping sample.

## 2.x Information sources
Primary retrieval used **OpenAlex** (Priem et al. 2022), an open, cross-publisher index that
covers IEEE, ACM, Springer/LNCS, Elsevier, AAAI, the ACL Anthology, and preprint servers
(arXiv) in a single catalogue. To test dependence on a single index, the **ACM Digital
Library was searched as an independent second primary database** with the same thirteen
title-scoped cluster queries, through an authenticated institutional session (University of
the Cumberlands). Three further subscription indices were registered as coverage probes
(IEEE Xplore, ScienceDirect (Elsevier), and Scopus); Crossref and the Semantic Scholar Graph
API were queried as additional recall-gap probes. Web of Science could not be searched for
lack of institutional credentials and is logged as unresolved rather than silently dropped.
The ACM search returned 278 unique records; 250 (90.0%) were already in the OpenAlex set and
28 were net-new, confirming that OpenAlex's coverage of the subscription publishers is
near-complete for this topic and that the remaining probes function as coverage checks rather
than primary record sources.

## 2.x Search strategy
Thirteen cluster queries (one per control-plane theme; Table 13) were executed title-scoped
against OpenAlex as exact-phrase streams, unioned and de-duplicated by work id, restricted to
2019–2026. Identification is title-scoped: a benchmark or method whose title omits the cluster
vocabulary can be missed at identification and is recovered only through backward snowballing
(below). The exact executed queries and the harvest code are released with the repository so
the identification set can be reconstructed.

## 2.x Study selection
- **Identification:** 12,021 unique works (OpenAlex primary). Venue mix: arXiv 3,775; IEEE 863;
  ACM 289; Springer/LNCS 248; Elsevier 1; other/unindexed-venue 6,845.
- **Screening queue:** records were ordered by citation count to prioritise canonical works
  first; citation count was used only to ORDER the human screening queue and to select
  snowball seeds — it was NOT an inclusion criterion (that would introduce recency and
  popularity bias; 75% of the corpus is 2026 work with citation lag).
- **Eligibility:** title+abstract screened against the inclusion criteria (addresses ≥1
  control-plane cluster; offers an empirical evaluation, reproducible system, or normative
  architectural contribution) by two independent raters; disagreements reconciled; Cohen's κ
  reported. Exclusion codes E1–E8.
- **Two-tier corpus:** a frozen primary tier (screened in full) plus a living-review tier for
  2026 records (relevance-screened, refreshed), so recent work is retained rather than excluded
  by citation lag.
- **Backward snowballing:** reference lists of the included seeds were harvested via OpenAlex
  citation links and screened under the same criteria, to recover title-missed studies.

## PRISMA-ScR flow (identification complete; screening is the authors' next stage)
> Identification
>   OpenAlex primary (13 title-scoped cluster queries, 2019–2026): n = 12,021 unique
>   ACM Digital Library, second primary database (same 13 clusters): n = 278 unique
>     → 250 duplicates of OpenAlex removed; 28 net-new carried forward
>   Backward snowball from included seeds (title-relevant, new): n = 5,633
>   Unique identified (OpenAlex + ACM-new + snowball): n = 17,682
>   Coverage probes (IEEE / ScienceDirect / Scopus / Crossref / S2): counts only
>   Web of Science: unresolved (no credentials)
> Screening (dual independent rating, both tiers)
>   Primary tier (top-800 citation-ordered): 657 include / 143 exclude; κ = 0.45
>   Snowball tier (top-800, 2023–2026): 238 include / 562 exclude; κ = 0.63
>   ACM net-new: 20 screened (κ = 1.00) → 3 include / 17 exclude; +8 pre-struck E7/E8
> Eligibility / Included
>   Screened mapping sample: n = 898 (primary 657 + snowball 238 + ACM 3)

## Limitations to state explicitly (reviewers will expect these)
1. Title-scoped identification — studies whose titles omit the cluster vocabulary are reached
   only by snowballing.
2. OpenAlex-primary with subscription databases as probes; Web of Science not searched.
3. Volume bounded for feasibility via a citation-ordered queue + living tier — a reproducible
   mapping sample, not a field census.
4. The living-review tier means currency is refreshed, not fixed at one date.

## What is reproducible / released
openalex_harvest.py (identification), openalex_ranked.csv (citation-ordered queue),
abstracts.json + abstract_screen.py (screening inputs), multisource_findings.md, and the
reconciliation against the prior cited set.
