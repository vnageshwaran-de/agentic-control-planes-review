# Depositing this repo on Zenodo via the GitHub integration

Zenodo watches a GitHub repo and, **when you publish a GitHub Release**, archives a snapshot of
the whole repo and mints a DOI automatically. Do the steps in this order.

## 0. One-time: connect Zenodo to GitHub
1. Go to **https://zenodo.org/account/settings/github/** (the page you opened).
2. Click **Connect** / authorize if you haven't. Zenodo lists your GitHub repos.
3. You won't see `agentic-control-planes-review` in the list until it exists on GitHub (step 2
   below) — Zenodo refreshes the list, or hit the sync button after you push.

## 1. Create the repo locally and push it
These are **your** commands (run in your own terminal — the files are already staged on disk at
`~/vnageshwaran/code/agentic-control-planes-review/`):

```bash
cd ~/vnageshwaran/code/agentic-control-planes-review
git init -b main
git add -A
git commit -m "Systematic search + screening reproducibility package (PRISMA-ScR), v1.0.0"

# create the GitHub repo and push (GitHub CLI):
gh repo create vnageshwaran-de/agentic-control-planes-review --public --source=. --remote=origin --push
# ...or create it on github.com first, then:
# git remote add origin git@github.com:vnageshwaran-de/agentic-control-planes-review.git
# git push -u origin main
```

## 2. Toggle the repo ON in Zenodo
1. Back on **https://zenodo.org/account/settings/github/**, click the sync icon if needed.
2. Find `vnageshwaran-de/agentic-control-planes-review` and flip its switch **ON**.
   (This must be ON **before** you create the release, or Zenodo won't catch it.)

## 3. Publish a GitHub Release — this triggers the DOI
```bash
gh release create v1.0.0 --title "v1.0.0 — PRISMA-ScR search & screening package" \
  --notes "Systematic mapping search for the Agentic AI Control Planes survey. 17,682 identified; 898 included (657 primary + 238 snowball + 3 ACM); OpenAlex + ACM Digital Library primary; dual-rater screening (κ 0.45 / 0.63 / 1.00)."
```
Or on github.com: **Releases → Draft a new release → tag `v1.0.0` → Publish**.

Within a minute or two Zenodo archives the release and mints:
- a **concept DOI** (always points to the latest version), and
- a **version DOI** (this specific v1.0.0).

## 4. Backfill the DOI
Once Zenodo shows the DOI:
1. Uncomment and fill the `doi:` line in `CITATION.cff` with the **concept** DOI.
2. Add the DOI badge to `README.md`:
   `[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXXX)`
3. Commit, and (optional) cut `v1.0.1` so the archive carries the self-citation — or just leave
   it; the concept DOI is stable.
4. Cite the concept DOI in the paper's **Search Methods / Data Availability** section, distinct
   from the audit tool's DOI (10.5281/zenodo.20102926).

## Notes
- `.zenodo.json` (repo root) supplies Zenodo's metadata — title, authors+ORCID, license,
  keywords, and an `isSupplementTo` link to the audit archive. Edit it before releasing if you
  want different wording; Zenodo reads it at release time.
- `.gitignore` already excludes the OpenAlex key and the large regenerable caches
  (`abstracts.json`, `citations.json`). Confirm no secret is staged: `git status` before commit.
- The full working bundle (`systematic_rerun_20261117.zip`) is **not** committed (it duplicates
  these files). If you want it as a release asset: `gh release upload v1.0.0 systematic_rerun_20261117.zip`.
