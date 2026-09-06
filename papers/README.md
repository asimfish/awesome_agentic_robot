# Core papers / 核心论文

| arXiv | Paper | Original | Chinese (SuperTranslate) | Translated scope |
|---|---|---|---|---|
| 2209.07753 | Code as Policies: Language Model Programs for Embodied Control | [pdf](pdf/2209.07753.pdf) | [pdf_zh](pdf_zh/2209.07753_zh.pdf) | Full main body (16 pages); appendix prompts/code kept in English by design. `inspect` QA: 3 untranslated appendix paragraphs, 0 issues in the main body ([report](pdf_zh/2209.07753_zh.inspect.json)) |
| 2605.23904 | SkillOpt: Executive Strategy for Self-Evolving Agent Skills | [pdf](pdf/2605.23904.pdf) | [pdf_zh](pdf_zh/2605.23904_zh.pdf) | Page 1: title, abstract, introduction opening |
| 2603.22435 | CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation | [pdf](pdf/2603.22435.pdf) | [pdf_zh](pdf_zh/2603.22435_zh.pdf) | Page 1: title, abstract, introduction opening |
| 2606.19980 | ENPIRE: Agentic Robot Policy Self-Improvement in the Real World | [pdf](pdf/2606.19980.pdf) | [pdf_zh](pdf_zh/2606.19980_zh.pdf) | Page 1: title, figure caption, abstract |
| 2607.00272 | ASPIRE: Agentic Skills Discovery for Robotics | [pdf](pdf/2607.00272.pdf) | [pdf_zh](pdf_zh/2607.00272_zh.pdf) | Page 1: title, abstract, introduction opening |

## How the Chinese versions were produced

The translations use the engine of [asimfish/super_translate](https://github.com/asimfish/super_translate) (`pdf_zh_translator`), which re-typesets translated text in place while keeping figures, formulas, code blocks and layout. The engine normally calls an LLM API; no working key was available on the build machine, so the deterministic manual path was used:

1. `pdf_zh_translator export <pdf> --out blocks.jsonl` — export every text block with a stable key.
2. Write translations into a Python table keyed by block index (`papers/translations/*.py`; `T[i]` = translation of block `i`, `E[text]` = translation of an exact segment).
3. `scripts/manual_translate.py <pdf> <out_zh.pdf> --blocks blocks.jsonl --dict table.py` — runs the engine in `cache-only` mode with a lookup translator (dictionary hit → Chinese, miss → original English, placeholder sets `⟦N⟧` verified), so the result is fully reproducible.
4. `pdf_zh_translator inspect <pdf> <out_zh.pdf>` — QA for untranslated or overflowing blocks.

`2603.22435` and `2606.19980` embed CID fonts that MuPDF cannot parse; the copies in `pdf/` were re-distilled with Ghostscript (`-dPDFSETTINGS=/prepress`, text unchanged, images recompressed) before translation. `scripts/download_papers.sh` fetches the untouched originals from arXiv.

To translate the remaining pages, or all 150 arXiv papers in `data/papers.csv`, set an API key and run `bash scripts/translate_papers.sh` (see the script header).
