#!/usr/bin/env bash
# Backfill the Zenodo DOI into CITATION.cff and README.md after the first release.
# Usage:  ./backfill_doi.sh 10.5281/zenodo.12345678
#   (pass the CONCEPT DOI — the one that always points to the latest version)
set -euo pipefail

DOI="${1:-}"
if [[ -z "$DOI" ]]; then
  echo "usage: $0 <concept-doi>   e.g. $0 10.5281/zenodo.12345678" >&2
  exit 1
fi
# normalize: strip a leading https://doi.org/ if pasted that way
DOI="${DOI#https://doi.org/}"
DOI="${DOI#http://doi.org/}"
if [[ ! "$DOI" =~ ^10\.5281/zenodo\.[0-9]+$ ]]; then
  echo "error: '$DOI' does not look like a Zenodo concept DOI (10.5281/zenodo.NNNN)" >&2
  exit 1
fi
SUFFIX="${DOI##*.}"   # the numeric id

cd "$(dirname "$0")"

python3 - "$DOI" "$SUFFIX" <<'PY'
import sys, re, pathlib
doi, suffix = sys.argv[1], sys.argv[2]

# --- CITATION.cff: replace the commented placeholder (or an old doi line) ---
cff = pathlib.Path("CITATION.cff"); t = cff.read_text()
if re.search(r'(?m)^\s*#\s*doi:.*$', t):
    t = re.sub(r'(?m)^\s*#\s*doi:.*$', f'doi: "{doi}"', t, count=1)
elif re.search(r'(?m)^\s*doi:.*$', t):
    t = re.sub(r'(?m)^\s*doi:.*$', f'doi: "{doi}"', t, count=1)
else:  # insert after repository-code line
    t = re.sub(r'(?m)^(repository-code:.*)$', r'\1\ndoi: "%s"' % doi, t, count=1)
cff.write_text(t); print("CITATION.cff -> doi:", doi)

# --- README.md: insert/replace a DOI badge under the H1 ---
rd = pathlib.Path("README.md"); r = rd.read_text()
badge = f"[![DOI](https://zenodo.org/badge/DOI/{doi}.svg)](https://doi.org/{doi})"
if "zenodo.org/badge/DOI/" in r:
    r = re.sub(r'\[!\[DOI\]\(https://zenodo\.org/badge/DOI/[^)]+\)\]\([^)]+\)', badge, r, count=1)
else:
    # place the badge on its own line right after the first H1
    r = re.sub(r'(?m)^(#\s.*\n)', r'\1\n' + badge + '\n', r, count=1)
# also swap the "badge will appear here after the first release" sentence if present
r = r.replace(
    "Archived on Zenodo via GitHub Releases — the DOI badge will appear here\nafter the first release (see `ZENODO_RELEASE_GUIDE.md`).",
    f"Archived on Zenodo via GitHub Releases. DOI: [{doi}](https://doi.org/{doi}).")
rd.write_text(r); print("README.md -> badge added for", doi)
PY

echo
echo "Done. Review the diff, then commit:"
echo "  git add CITATION.cff README.md && git commit -m 'Add Zenodo DOI ${DOI}'"
echo "  git push"
echo "(Optional) cut v1.0.1 so the archived copy carries its own DOI:"
echo "  gh release create v1.0.1 --title 'v1.0.1 - add DOI' --notes 'Backfill Zenodo DOI ${DOI}.'"
