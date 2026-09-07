# Contributing

The README (Chinese-first) is generated from `data/header.md`, `data/topics.csv`, `data/papers.csv` and `data/footer.md`. Please do not edit it by hand; edit the data files and regenerate. Topic headings are rendered as `中文名 | English name`, and the generator computes GitHub-compatible anchors for them (CJK kept, punctuation dropped, spaces to hyphens).

## Add or fix a paper

1. Add a row to `data/papers.csv` (or edit the entry in `src/build_papers_csv.py` if you also want it regenerated from arXiv metadata). Columns:
   `id` (arXiv id or a short slug for non-arXiv items), `short_name`, `title`, `authors`, `year`, `date`, `venue`, `url`, `code_url`, `topics` (semicolon-separated topic ids from `data/topics.csv`, e.g. `T15;T23`), `tier` (`core` = named by the source materials, `extended`, `foundation`), `note_zh` (one sentence, optional).
2. If the paper is on arXiv, run `python3 src/fetch_arxiv_meta.py` to refresh `data/paper_meta.json`, then `python3 src/build_papers_csv.py`.
3. Run `python3 src/generator.py` and check the diff of `README.md`.

## Add a topic line

Add a row to `data/topics.csv` (`topic_id,order,name_en,name_zh,keywords,representative`) and regenerate.

## Reports and slides

- Reports live in `docs/reports/report_zh.md` and `report_en.md`; build PDFs with `./build_zh.sh` / `./build_en.sh` in that directory (pandoc 3 + XeLaTeX with xeCJK; macOS fonts Songti SC / PingFang SC, change them in `header_*.tex` on other systems).
- Tables are rendered as non-breaking `tabular` through `docs/reports/tabular.lua`; keep individual tables shorter than a page.
- The HTML deck is `docs/slides/index.html` (self-contained, no dependencies). Export to PDF with `python3 scripts/export_slides_pdf.py` (Playwright + Chromium).
- The Beamer deck follows the rules of `beamer-skill`: 16:9, 10pt, no overlays, at most two coloured boxes per slide, references slide, backup slides after the closing slide, compiled with XeLaTeX. Fix any `Overfull \hbox` larger than 10pt before committing.

## Style

Chinese and English prose follow two rules: state the claim first, then the evidence; do not hedge or pad. Numbers quoted from papers must come from the paper's abstract or text, and the report distinguishes "what the paper reports" from "our judgement".

## Non-ASCII text on macOS

Files containing Chinese must be written as UTF-8 (shell heredocs or Python `open(..., encoding="utf-8")`). Verify with a quick CJK count and a check for U+FFFD before committing.
