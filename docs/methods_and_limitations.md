# Methods and Limitations — drop-in draft (control-plane mapping review)
Numbers from the 2026-11-17/19 multi-source re-run. Mapping-sample framing.
Proposals only; adapt to the manuscript's voice.

## 2.1 Review type and protocol
We conducted a systematic **mapping review** reported per PRISMA-ScR (Tricco et al. 2018).
The review began as an IEEE-Xplore pilot; after the pilot reproduced only 31 of 69 previously
cited systematic references, the protocol was amended (dated) to a multi-source design. All
amendments are logged in the protocol file released with the review. [If registered: "The
protocol was deposited on OSF (DOI …) during the conduct of the review."]

## 2.2 Information sources
Primary identification used **OpenAlex** (Priem et al. 2022), an open cross-publisher index
spanning IEEE, ACM, Springer/LNCS, Elsevier, AAAI, the ACL Anthology, and arXiv. To guard
against single-index dependence, the **ACM Digital Library** was run as an independent second
primary database using the same thirteen title-scoped cluster queries (authenticated
institutional session, searched 19 November 2026). Three further indices were queried as
authenticated coverage probes (IEEE Xplore, ScienceDirect, Scopus) and two as recall-gap
probes (Crossref, Semantic Scholar Graph API).
Web of Science was not searchable (no institutional access) and is logged as unresolved. The
last search was executed on 19 November 2026; a living tier refreshes 2026 records.

## 2.3 Search strategy
Thirteen cluster queries (one per control-plane theme; Appendix B) were executed as title-scoped
exact-phrase streams against OpenAlex, 2019–2026, unioned and de-duplicated by work identifier.
Identification is title-scoped; studies whose titles omit the cluster vocabulary are recovered via
backward snowballing (2.5). Exact strings and harvest code are released for reproduction.

## 2.4 Selection process
Records were ordered by citation count to prioritise the screening queue (citation count was NOT
an inclusion criterion). Title+abstract were screened against the inclusion criteria by two
reviewers independently; disagreements were reconciled. Inclusion required: addresses ≥1
control-plane cluster AND offers an empirical evaluation, a reproducible system, or a normative
architectural contribution. A pre-agreed sub-rule governed method-in-domain cases: a benchmark,
dataset, or method evaluated across ≥2 domains or framed as domain-general was included; a
single-domain deployment with no transferable artifact was excluded (E6). Exclusion codes E1–E8
(Appendix C). Both tiers were double-screened; Cohen's κ = 0.45 (primary tier, fully reconciled)
and 0.63 (snowball tier).

## 2.5 Backward snowballing
Reference lists of all included primary studies were harvested via OpenAlex citation links; new,
title-relevant records (2023–2026) were screened under the identical criteria.

## 2.6 Data and counts
Identification yielded **17,682** unique records (OpenAlex 12,021; ACM second-database net-new 28;
snowball-relevant 5,633). The ACM search returned 278 unique records, of which 250 (90.0%) were
already present in the OpenAlex set; the 28 net-new records (all also absent from the snowball
set) were carried to screening under the identical criteria. The screened mapping sample comprises
**898 studies** (primary tier 657; snowball tier 238; ACM second-database tier 3, dual-rated κ = 1.00). At the identification level the multi-source + snowball search recovered **75
of 119** previously cited references (67% of the 112 in-window references; the 7 pre-2019 anchors
are outside the search window by design), versus 31/69 for the IEEE-only pilot.

**Single-source robustness.** Adding ACM as a second primary database changed the identified pool
by 28 of 12,021 records (0.23%). The 20 in-scope net-new records were dual-rated (κ = 1.00) and
yielded **3 new included studies** (0.34% of the corpus); the remainder were one edited volume
excluded as a book plus two out-of-scope applications. Because OpenAlex already indexed 90% of
ACM's title-matched records, the corpus is not an artifact of a single index.

## 3. Limitations
1. **Title-scoped identification.** Studies whose titles omit the cluster vocabulary are reached
   only through backward snowballing; some may remain unretrieved.
2. **Mapping sample, not a census.** The screened corpus is bounded by a citation-ordered queue;
   it is a reproducible mapping sample. Lower-cited and very recent studies are identified and
   tracked in a living tier rather than exhaustively screened.
3. **Database scope.** OpenAlex and the ACM Digital Library were searched as primary databases,
   with further subscription indices as coverage probes; Web of Science was not searched.
4. **Inter-rater agreement.** Primary-tier agreement was moderate (κ = 0.45) before full
   reconciliation, driven by the method-in-domain boundary; the sub-rule was then applied
   uniformly and the snowball tier reached κ = 0.63.
5. **Currency.** As a living review, currency is refreshed rather than fixed to a single date.
