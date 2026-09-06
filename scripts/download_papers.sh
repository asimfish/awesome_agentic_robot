#!/usr/bin/env bash
# Download the original PDFs of the five core papers (and optionally every arXiv paper in data/papers.csv).
# usage: bash scripts/download_papers.sh [--all]
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p papers/pdf
CORE="2209.07753 2605.23904 2603.22435 2606.19980 2607.00272"
if [[ "${1:-}" == "--all" ]]; then
  IDS=$(python3 -c "import csv;print(' '.join(r['id'] for r in csv.DictReader(open('data/papers.csv',encoding='utf-8')) if r['id'][0].isdigit()))")
else
  IDS=$CORE
fi
for id in $IDS; do
  out="papers/pdf/$id.pdf"
  if [[ -s "$out" && "${FORCE:-0}" != "1" ]]; then echo "skip $id (exists)"; continue; fi
  echo "downloading $id"; curl -sL --retry 3 -o "$out" "https://arxiv.org/pdf/$id" && sleep 3
done
echo done
