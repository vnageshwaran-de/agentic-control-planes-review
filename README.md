# agentic-control-planes-review

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24403910.svg)](https://doi.org/10.5281/zenodo.24403910)

**Independent coverage-verification and reproducibility package** for the survey
*Agentic AI Control Planes: A Systematic Survey of Protocols, Security, Cloud-Native LLMOps,
and Governance* (Nageshwaran & Ezekiel, IEEE Open Journal of the Computer Society, 2026).

The survey's reported search is an IEEE-Xplore-primary structured review with supplementary ACM
Digital Library searches and snowballing (Appendix A / Figure 2 of the paper). **This repository
is a separate, independent verification of that search:** it re-harvests the same thirteen
clusters through OpenAlex (an open, cross-publisher index) with ACM run as a second record-level
database, then dual-screens the result, to test whether the paper's cited corpus is recoverable
from an independent path. It is reported per PRISMA-ScR (Tricco et al., 2018) as a reproducible
coverage check, not as a claim of exhaustive completeness and not as a replacement for the
paper's primary search. The separate static security-posture audit tool (§VIII-E) lives in
[`agentic-control-planes-audit`](https://github.com/vnageshwaran-de/agentic-control-planes-audit)
(DOI [10.5281/zenodo.20102926](https://doi.org/10.5281/zenodo.20102926)).

**Headline verification result:** an independent OpenAlex + ACM + snowball re-harvest
re-identified **75 of the 119 cited research references** (67% of those in the 2019–2026 window)
and produced a dual-screened mapping sample of 898 studies; the ACM second-database check found
90% of its title-matched records already in the open index (28 net-new, 3 included), indicating
limited single-source dependence.

## Headline numbers
| | |
|---|---|
| Unique identified | **17,682** (OpenAlex 12,021 + ACM second-database net-new 28 + snowball 5,633) |
| Primary databases | OpenAlex + ACM Digital Library (ACM: 278 unique, 90% already in OpenAlex) |
| Included mapping sample | **898** (primary 657 + snowball 238 + ACM 3) |
| Inter-rater agreement (Cohen's κ) | primary 0.45 · snowball 0.63 · ACM net-new 1.00 |
| Prior-corpus reproduction (identification) | 75/119 (67% in-window) vs 31/69 IEEE-only pilot |
| Last search | 2026-11-19 (living 2026 tier) |

## Layout
```
protocol/   frozen 13 cluster queries, screening method, adjudication guide
code/       OpenAlex harvest, ACM records + dedup, fetch/screen/snowball scripts
data/       identified corpus, citation-ordered queue, ACM harvest, snowball candidates,
            frozen primary tier, final included corpus (898)
screening/  dual-rater workbooks + reconciliations (incl. ACM net-new, κ = 1.00)
docs/       PRISMA-ScR methods, flow (md + svg), checklist, limitations, ACM second-database
            write-up, multi-source findings, registration draft, full reproducibility README
```

## Reproduce the identification
```bash
pip install -r code/requirements.txt
export OPENALEX_KEY=...            # free key from https://openalex.org (supply your own)
python code/openalex_harvest.py    # -> data/openalex_harvest.csv (12,021)
python code/dedup_acm.py           # ACM records -> data/acm_harvest.csv + acm_netnew.csv
```
The ACM second-database records are in `code/acm_records.py` (per-cluster counts self-verify
on run); re-running the live ACM search needs institutional access (see
`docs/acm_second_database.md`). Full run order: `docs/README_reproducibility.md`.

## Screening
Final selection is human dual-screening (retrieval was phrase-based, so a keyword classifier
cannot discriminate the corpus). Workbooks, reconciliations, and live Cohen's κ are in
`screening/`; the decision rule and exclusion codes (E1–E8) are in `protocol/screening_method.md`.

## Cite
See `CITATION.cff`. Archived on Zenodo via GitHub Releases. DOI: [10.5281/zenodo.24403910](https://doi.org/10.5281/zenodo.24403910).

## License
Code: MIT (`LICENSE`). Data and documentation may be reused under CC-BY-4.0 with attribution.
