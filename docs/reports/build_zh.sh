#!/bin/bash
cd "$(dirname "$0")"
pandoc report_zh.md -o report_zh.pdf --pdf-engine=xelatex -H header_zh.tex --lua-filter tabular.lua --toc --toc-depth=2 -V documentclass=article -V papersize=a4 -V colorlinks=true -V linkcolor=NavyBlue -V urlcolor=NavyBlue -V toccolor=black 2>&1 | rg -v "MiKTeX" | rg -v "^$"
