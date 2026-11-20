# Reconciliation — re-run corpus vs. the 119 cited references (2026-11-17)

Method: each of the 119 references in `reconciliation_scaffold.csv` was matched by
normalized-title containment (fraction of the cited title's content words present in a
retrieved title; threshold 0.7, ≥4 content words) against this run's retrieved corpus.
After re-scraping C3/C6/C7 to recover their titles, the corpus has titles for 2,731 of
the 2,762 unique records (near-complete). Per-reference results are in `reconciliation.csv`.

## Recovery by source tier (FINAL — after second-rater reconciliation)
| Source tier (current_route) | retrieved this run | retrieved **and** included (final) |
|---|--:|--:|
| systematic_ieee_acm | **36 / 69** | **31** |
| snowball_supplementary | 7 / 39 | 7 |
| author_survey | 0 / 2 | 0 |
| anchor_pre2019 | 0 / 7 | 0 |
| anchor_usenix_elsevier | 0 / 2 | 0 |
| **Total** | **43 / 119** | **38** |

Of the 36 systematic-tier references recovered, **31 survive to the final included set**;
5 were retrieved but screened out (judged out-of-scope on the abstract). So of the 69
originally-cited systematic references, 31 are reproduced by this IEEE-Xplore-only,
tightened-query pipeline — 33 are not retrieved at all, and 5 are retrieved but excluded.

## Why the re-run does not fully reproduce the cited systematic set (33/69)
This is a genuine finding, reported as-is:

1. **IEEE-Xplore-only scope.** The source tier is `systematic_ieee_acm`, i.e. it mixes
   IEEE Xplore *and* ACM Digital Library. This re-run queried **only IEEE Xplore**, so
   ACM-indexed systematic papers cannot be retrieved here. This accounts for a large part
   of the 36-paper gap.
2. **Tightened queries.** The frozen v3 strings were deliberately narrowed to cut the
   ~13,784-hit noisy corpus down to a screenable one. Papers the original search caught
   with broader terms fall outside — visible in the governance/identity cluster
   (e.g. "EU AI Act" compliance, "Zero-Trust maturity", "SPIFFE verifiable identity",
   responsible-GenAI-governance), whose titles do not contain the C12 anchors
   ("AI governance" / "policy-as-code" / "runtime policy enforcement").
3. **(Resolved.)** C3, C6, C7 were re-scraped on 2026-11-17 to recover their titles, so
   the corpus now covers 2,731 of 2,762 records; this raised systematic recovery from
   33/69 to 36/69. The remaining gap is therefore not a missing-title artifact.
4. **Phrasing / subtitle drift.** A handful of still-"absent" systematic titles sit at
   containment 0.5–0.69 (different subtitle or word order) and may in fact be present.

## Implication for the manuscript
The re-run **confirms the reproducibility limitation it was meant to close is real**: an
IEEE-Xplore-only, tightened-query re-run reproduces only **31/69** of the originally cited
systematic references in the final included set (36 retrieved, 5 then screened out; the
470 unsure records have now been fully adjudicated by two co-authors, so this is a final
figure, not a title-level estimate). To make the pipeline fully reproducible the paper should
either (a) state the search as IEEE Xplore **and** ACM with the exact (broader) strings
used originally, or (b) adopt the tightened IEEE-only protocol here and accept a
re-derived, smaller cited set — not retro-fit the old numbers. The 470 unsure records and
a full-text pass remain to be adjudicated by a human second rater before the included set
is final.
