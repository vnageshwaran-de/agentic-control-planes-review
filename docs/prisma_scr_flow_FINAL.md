# Final PRISMA-ScR flow — multi-source mapping review (2026-11-19)

## Identification
- OpenAlex primary (13 title-scoped cluster queries, 2019–2026): 12,021 unique
- ACM Digital Library, second primary database (same 13 title-scoped clusters, 2026-11-19):
  278 unique; 250 (90.0%) already in OpenAlex; **28 net-new** (all also absent from snowball).
- Backward snowball from included seeds (title-relevant, new): 5,633
- Unique identified (OpenAlex + ACM-new + snowball): **17,682**
- Additional coverage probes (IEEE/ScienceDirect/Scopus/Crossref/Semantic Scholar); WoS unresolved.

### ACM second-database detail (see acm_second_database.md)
- Per-cluster hits: C1 127·C2 5·C3 0·C4 6·C5 10·C6 7·C7 5·C8 11·C9 90·C10 0·C11 21·C12 0·C13 8 (290 raw → 278 unique).
- Of the 28 net-new: 7 obvious non-contributions (E7: front/back matter, podcast), 1 out-of-window
  (E8, 2010), 15 chapters of one edited volume (10.1145/3749421.*) + 5 recent papers → 20 screened (κ = 1.00) → **3 included**, 17 excluded (see acm_netnew_reconciliation.md).

## Reproducibility check vs the 119 prior cited references (identification level)
- IEEE-only 43 → + OpenAlex 56 → + snowball **75/119** recovered
- Excluding 7 pre-2019 anchors (outside window): 75/112 in-window ≈ 67%.

## Screening (dual independent rating, both tiers)
- Primary tier (top-800 citation-ordered): 657 include / 143 exclude; Cohen's κ = 0.45
  (154 disagreements reconciled via the agreed method-in-domain sub-rule).
- Snowball tier (top-800, 2023–2026): 238 include / 562 exclude; Cohen's κ = 0.63
  (143 disagreements jointly reconciled).

## Included (screened mapping sample)
- **898 studies** (primary 657 + snowball 238 + ACM 3) — the citation-bounded, dual-rated core corpus.

## Single-source robustness (answers the "only OpenAlex" objection)
Running ACM DL as an independent second primary database changed the identified pool by
**28 of 12,021 (0.23%)**. The 20 in-scope net-new records were dual-rated (κ = 1.00) and gave
**3 new included studies**; the rest were one edited volume excluded as a book plus two
out-of-scope applications. OpenAlex already held 90% of ACM's title-matched records. This is
the evidence that the corpus is not an artifact of a single index.

## Two distinct numbers — do not conflate (state both in the paper)
1. **Identification coverage** = 75/119 (67% in-window). This is the reproducibility evidence —
   it shows the multi-source + snowball search *reaches* the prior corpus.
2. **Included mapping sample** = 898 high-impact, dual-screened studies. This is the curated
   output. It recovers only ~20/119 cited because the included set is citation-bounded and most
   prior citations are recent/lower-cited papers that sit below the top-800 tiers — they are
   *identified* but outside the *screened* tiers by the declared bounding.

## If the goal is to also INCLUDE the prior cited references
The 75 recovered cited papers are in the identified corpus but mostly below the citation cutoffs.
To bring them into the included set, screen the living tier / lower-citation tail that contains
them (relevance screen), OR carry them as a named seed set. This is a scoping choice to declare,
not a defect.

## Limitations to state
Title-scoped identification; citation-ordered screening bound (mapping sample, not census);
living 2026 tier; WoS not searched; dual-rated throughout (κ 0.45 / 0.63).
