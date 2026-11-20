# Screening method (frozen 2026-11-17)

## Pipeline per cluster
1. **Identification** — IEEE Xplore command search, All Metadata, year≥2019, English,
   using the frozen tightened Boolean string for the cluster. Each results page
   (rowsPerPage=100) is scraped in-browser to `{docid, year, title}` and saved to
   `raw/<Cx>_p<N>.tsv`. The live "Showing X of N results" header is recorded.
2. **De-duplication** — pages concatenated (`awk 1`, newline-safe) → dedupe by IEEE
   docid (first occurrence kept). Count after dedupe = records entering screening.
3. **Title screening** — two-stage, fully logged:
   a. *Keyword pre-sort* (`screen_classifier.py`, documented rule): proposes
      include / exclude(E-code) / unsure for every record.
      - BOOK phrases → exclude E7 (trade books, not peer-reviewed contributions)
      - WORKSHOP/front-matter phrases → exclude E7
      - generalizable control-plane signal (tool/function calling, benchmark, eval,
        protocol/MCP/A2A, caching, planning, verification, guardrail, reliability,
        taxonomy, reference architecture, prompt-injection, observability,
        governance, serving) and NO domain-application signal → include
      - domain-application signal (medical, power grid, water, telecom/6G, optical,
        robotics, UAV, vehicle, aircraft, space, agriculture, finance vertical,
        pentest/red-team/IDS "agents-FOR-security", game, fake news, etc.) and no
        general signal → exclude E6
      - both signals, or neither → unsure
   b. *Human adjudication*: every proposed decision is reviewed against the title.
      Overrides are recorded (`decided_by = manual`). Key rules applied:
      - security OF agents (threat models, prompt-injection defenses, access control,
        auth, MCP security) = include; agents FOR security (pentest, red-team, IDS,
        threat-hunting, vuln-patching tools) = exclude E6.
      - a generalizable method/benchmark/dataset demonstrated in a vertical = include;
        a vertical application that merely uses agents/tool-calling = exclude E6.
      - trade books / keynotes / workshop front-matter = exclude E7.
      - general LLM training/alignment/post-training (not control-plane) = exclude E6.
4. **Unsure handling** — every `unsure` row carries `review_flag = human-review` and is
   NOT resolved. These are surfaced for a human second rater; they are not counted as
   include or exclude in the PRISMA screened-in total.

## Exclusion codes
E1 vendor whitepaper · E2 short workshop abstract · E3 duplicate · E4 retracted ·
E5 unresolved DOI · E6 out-of-scope (domain application / not a control-plane concern) ·
E7 not-a-contribution (book, keynote, front-matter) · E8 wrong language/year

## Log columns
`cluster, docid, year, decision, reason_code, review_flag, decided_by, title`

## Reproducibility note
Raw per-page scrapes are retained in `raw/`. Proposed decisions are retained in
`<Cx>_proposed.tsv`. This closes the gap in the 2026-05-06 run (screening log not kept):
every decision here traces to a saved record and a documented rule, and the keyword
pre-sort is deterministic and re-runnable.
