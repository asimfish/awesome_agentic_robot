#!/usr/bin/env bash
# One-click layout-preserving Chinese translation of the core papers with SuperTranslate
# (https://github.com/asimfish/super_translate). Needs an LLM API key, e.g. DEEPSEEK_API_KEY.
#
#   export DEEPSEEK_API_KEY=sk-...          # or any OpenAI-compatible endpoint supported by super_translate
#   bash scripts/translate_papers.sh        # translates every PDF in papers/pdf -> papers/pdf_zh/<id>_zh.pdf
#
# Without a key, use scripts/manual_translate.py (deterministic lookup-table path used for this repository).
set -euo pipefail
cd "$(dirname "$0")/.."
ST="${SUPER_TRANSLATE_HOME:-../super_translate}"
if [[ ! -d "$ST" ]]; then
  git clone https://github.com/asimfish/super_translate "$ST"
  (cd "$ST" && python3 -m venv .venv && .venv/bin/pip install -e .)
fi
PY="$ST/.venv/bin/python"; [[ -x "$PY" ]] || PY=python3
mkdir -p papers/pdf_zh
for pdf in papers/pdf/*.pdf; do
  id=$(basename "$pdf" .pdf); out="papers/pdf_zh/${id}_zh.pdf"
  echo "== $id"
  # Large PDFs with exotic CID fonts (e.g. 2603.22435, 2606.19980) render more reliably after a Ghostscript re-distill.
  src="$pdf"
  if command -v gs >/dev/null && [[ $(stat -f%z "$pdf" 2>/dev/null || stat -c%s "$pdf") -gt 20000000 ]]; then
    mkdir -p /tmp/st_gs; gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile=/tmp/st_gs/$id.pdf "$pdf"; src=/tmp/st_gs/$id.pdf
  fi
  "$PY" -m pdf_zh_translator translate "$src" "$out" --preserve-graphics-text "$@"
  "$PY" -m pdf_zh_translator inspect "$src" "$out" --json-out "papers/pdf_zh/${id}_zh.inspect.json" || true
done
echo done
