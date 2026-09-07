#!/usr/bin/env bash
# Rebuild README, the two PDF reports, the HTML deck PDF export and the Beamer deck.
# Requirements: python3 (playwright, pymupdf), pandoc >= 3, XeLaTeX with xeCJK, macOS fonts (Songti SC / PingFang SC).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/make_figures.py
(cd docs/reports && ./build_zh.sh && ./build_en.sh)
python3 scripts/export_slides_pdf.py
(cd docs/slides && xelatex -interaction=nonstopmode agentic_robot_slides.tex >/dev/null && xelatex -interaction=nonstopmode agentic_robot_slides.tex >/dev/null && rm -f agentic_robot_slides.{aux,log,nav,out,snm,toc,vrb})
python3 scripts/build_full_report.py
python3 src/generator.py
echo done
