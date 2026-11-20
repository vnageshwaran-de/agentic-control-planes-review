# ACM net-new — second-rater screening outcome (2026-11-19)

Workbook returned: `reconciled_review_acm_netnew.xlsx` (co-authors R1, R2).

## Agreement
- 20 screenable rows, both reviewers scored all 20.
- Agreements: 20/20. Observed Po = 1.000; expected Pe = 0.745.
- **Cohen's κ = 1.00** (perfect) on the ACM net-new tier.

## Decision on the edited-volume policy
The one policy call — whether to include chapters of the ACM edited volume *Multi-LLM Agent
Collaborative Intelligence* (`10.1145/3749421.*`) — was resolved as **exclude the volume as a
book (E7)**, applied uniformly to all 15 chapters.

## Final decisions (28 net-new)
| Outcome | Count | Codes |
|---|--:|---|
| **Include** | **3** | — |
| Exclude | 25 | E7 ×22 (15 book chapters + 7 pre-struck front/back/podcast), E6 ×2, E8 ×1 |

**3 included (added to corpus, tier = `acm`):**
- `10.1145/3711875.3736687` (2025, C11) — SensorMCP: A Model Context Protocol Server for Custom Sensor Tool Creation
- `10.1145/3777884.3796983` (2026, C6) — Evaluating Kubernetes Performance for GenAI Inference
- `10.1145/3767308.3836398` (2026, C8) — PVDetector: Detecting Prompt Injection Attacks on Purpose-Specific LLM Agents

Two standalone papers were excluded as E6 (out-of-scope / single-domain application):
*Invisible Walls in Cities* (C1) and *SkyMind* (C9).

## Effect on the corpus
- **Final included corpus: 895 → 898** (primary 657 + snowball 238 + ACM 3).
- Identification total unchanged at 17,682 (the 28 were already counted at identification).
- Inter-rater agreement across tiers: primary κ = 0.45, snowball κ = 0.63, **ACM κ = 1.00**.
- Single-source robustness confirmed: a second primary database added 3 included studies
  (0.34% of the 895-study corpus); the dominant residual was one edited volume excluded by
  the agreed book policy.
