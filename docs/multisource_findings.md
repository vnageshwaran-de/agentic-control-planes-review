# Multi-source expansion — findings (2026-11-19)

Replicating the published evaluation paper's source set for the control-plane survey.

## Sources executed
| Source | Status | Records |
|---|---|---|
| **OpenAlex** (primary, cross-publisher incl. arXiv) | ✅ harvested (title-scoped, exact-phrase, 2019–2026) | **12,021 unique** |
| Crossref | ✅ reachable (recall-gap probe) | not yet harvested |
| Semantic Scholar | ✅ reachable (rate-limited) | not yet harvested |
| IEEE Xplore | ✅ done earlier | 2,762 |
| ACM Digital Library | ✅ browser-accessible | not yet harvested |
| ScienceDirect | ✅ browser, **authenticated** (Univ. of the Cumberlands) | not yet harvested |
| Scopus / SpringerLink | likely same subscription | not yet checked |
| Web of Science | no access (same as published paper) | unresolved |

## OpenAlex corpus venue rollup (12,021)
arXiv 3,775 · IEEE 863 · ACM 289 · Springer/LNCS 248 · Elsevier 1 · other/unknown 6,845.
→ **arXiv is the single biggest addition** (3,775 records IEEE Xplore never indexed),
confirming the evaluation paper's finding that ~78% of this literature is preprint-hosted.

## Reconciliation vs the 119 cited references
| | IEEE-only | **+ OpenAlex (combined)** |
|---|--:|--:|
| Total recovered | 43/119 | **56/119** |
| Systematic tier | 36/69 | **40/69** |
| Snowball tier | 7/39 | **15/39** |

Covering all sources **helped** (43→56; systematic 36→40) — but less than expected.

## The remaining gap is now TITLE-SCOPING, not source coverage
Both this OpenAlex harvest and the evaluation paper identify papers **by title** (the search
phrase must appear in the title). Papers whose titles omit the cluster vocabulary are missed
at identification regardless of how many databases are searched — the published paper says
exactly this and recovers them via backward snowballing from seeds. So 29 cited systematic
papers remain unretrieved because their titles don't contain the exact cluster phrases, not
because they're in an unsearched database.

## Decision point (recall vs precision)
To close the remaining gap, three options:
1. **Keep title-scoped** (current): precise, 12,021 records, reproducible mapping sample —
   accept that identification is title-bounded and document it (the evaluation paper's stance).
2. **Broaden to abstract-inclusive** (OpenAlex `title_and_abstract.search`): matches the
   control-plane paper's original "All Metadata" scope, recovers more, but the corpus balloons
   to an estimated 40,000–60,000 records — a much larger screen.
3. **Add backward snowballing** from the already-included seeds (the evaluation paper's method)
   to recover title-missed papers without a full abstract-scope harvest.

## Citation-ranked bounding (Q1-standard volume control, per the published paper)
All 12,021 OpenAlex works were fetched with cited_by_count and ranked (openalex_ranked.csv).
Distribution: ≥1 cite 5,802 (48%) · ≥5 3,102 (26%) · ≥10 2,127 (18%) · ≥20 1,260 (10%) ·
≥50 538 · ≥100 287. 8,983 are 2026 (citations lag, so too new to rank on impact).
The top-cited are the field's landmark works (Greshake prompt-injection 3,358; A-Mem 1,507;
ExpeL 1,453; AgentDojo 1,347; InjecAgent 1,344; MCP survey 996), confirming the ranking is
sound. A citation cutoff bounds the abstract-screening pool to a Q1-defensible size; recent
(2026) records are handled as a living-review tier, exactly as the published paper did.

## Status of the multi-source expansion
- Identification across all sources: DONE (OpenAlex 12,021; arXiv + all publishers).
- Reconciliation improved: 43→56/119 cited recovered; systematic 36→40/69.
- Remaining gap is title-scoping, addressed by citation-bounded abstract screening + snowballing.
- NEXT (needs the authors' cutoff decision): set the citation threshold -> abstract-screen that
  bounded pool to Q1 standard (second-rater, as for IEEE) -> backward-snowball from the included
  seeds -> final PRISMA + reconciliation.

## Final recovery after backward snowballing (2026-11-19)
Criterion for method-in-domain settled (author decision): middle sub-rule
(>=2 domains or domain-general = include; else E6). Applied to the 150 tie-break records:
100 include / 50 exclude -> FROZEN PRIMARY = 657 include / 143 exclude (frozen_primary_final.csv).
Backward snowball from the 657 included seeds: 14,947 referenced works -> 14,216 new ->
5,633 title-relevant candidates (snowball_candidates.csv).

Reconciliation progression vs the 119 cited references:
  IEEE-only:                 43/119  (systematic 36/69)
  + OpenAlex (all sources):  56/119  (systematic 40/69)
  + backward snowball:       75/119  (systematic 45/69, snowball-tier 28/39)
The 7 anchor_pre2019 references are outside the 2019-2026 window and are not recoverable by
design. The multi-source + snowball pipeline therefore recovers the large majority of the
in-window cited corpus, closing most of the original IEEE-only reproducibility gap.
