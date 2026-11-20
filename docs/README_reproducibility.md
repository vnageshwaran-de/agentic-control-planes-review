# Reproducibility package — control-plane systematic mapping review

Deposit this directory on OSF or Zenodo for a citable DOI. It lets a reader re-run the
identification and reproduce the screening decisions and counts.

## Pipeline (run order)
1. protocol_v3_frozen_queries.md — the 13 frozen cluster queries (IEEE + OpenAlex + ACM).
2. openalex_harvest.py — OpenAlex title-scoped identification -> openalex_harvest.csv (needs a free OpenAlex key).
3. ACM Digital Library second primary database — same 13 clusters, title-scoped
   (Title:(A) AND Title:(B)) via authenticated dl.acm.org; records in acm_records.py ->
   dedup_acm.py -> acm_harvest.csv (278) + acm_netnew.csv (28). See acm_second_database.md.
4. fetch_citations.py / fetch_abstracts.py — enrich with citations + abstracts.
5. abstract_screen.py / screen_classifier2.py — documented pre-sort (transparency; not the final screen).
6. snowball.py — backward snowball from included seeds -> snowball_candidates.csv.
7. Human dual screening (workbooks in second_rater*/); ACM net-new (<=20 in-scope) added to the queue.

## Key data files
- openalex_harvest.csv (12,021), openalex_ranked.csv (citation-ordered)
- acm_records.py (ACM source of truth), acm_raw.tsv (290), acm_harvest.csv (278 unique),
  acm_netnew.csv (28 net-new vs OpenAlex), dedup_acm.py
- snowball_candidates.csv (5,633), snowball_screen_set.csv (screened tier)
- frozen_primary_final.csv (657 incl / 143 excl), final_included_corpus.csv (898: +3 ACM)
- screening_log_*.csv (IEEE per-cluster decisions), second_rater*/ (all rating rounds + reconciliations)
- reconciliation.csv / .md (vs the 119 prior cited references)

## Documentation
- methods_and_limitations.md, prisma_scr_methods.md, prisma_scr_flow_FINAL.md
- acm_second_database.md (ACM 2nd-database search, dedup, net-new triage)
- prisma_scr_checklist.md, prisma_scr_flow.svg (figure)
- screening_method.md (two-stage screen), multisource_findings.md

## Headline numbers
Identified 17,682 unique (OpenAlex 12,021 + ACM 2nd-database net-new 28 + snowball 5,633);
screened 1,620 (dual-rated, κ 0.45 / 0.63 / ACM 1.00); included 898.
Two primary databases: OpenAlex + ACM DL — ACM shifts the identified pool by 0.23% (278 unique,
90% already in OpenAlex), answering the single-source objection.
Prior-corpus reproduction at identification: 75/119 (67% in-window) vs 31/69 IEEE-only pilot.

## Not included (by design / access)
Web of Science (no institutional access); abstracts.json/citations.json (large caches, regenerable);
the OpenAlex API key (secret — supply your own). ACM records were captured from the authenticated
dl.acm.org session (title-scoped doSearch URLs in acm_second_database.md); re-running needs ACM access.
