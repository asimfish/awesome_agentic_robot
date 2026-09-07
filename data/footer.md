## 复现与贡献

仓库结构：

```
README.md              由 data/*.csv + data/header.md + data/footer.md 生成（src/generator.py），请勿手改
data/                  topics.csv（主线）· papers.csv（论文条目）· paper_meta.json（arXiv 元数据）· header.md / footer.md
docs/reports/          中英文报告 Markdown 与 PDF，LaTeX 头文件、pandoc Lua 过滤器与构建脚本
docs/slides/           HTML 幻灯片（index.html / index.pdf）与 Beamer 幻灯片（.tex / .pdf）
papers/pdf/            五篇核心论文原文；papers/pdf_zh/ 为 SuperTranslate 中文版（*.inspect.json 为 QA 报告）
papers/translations/   人工译文表，供 scripts/manual_translate.py 使用
sources/               五份源材料的转写与存档
scripts/               download_papers.sh · translate_papers.sh · manual_translate.py · export_slides_pdf.py · build_docs.sh
src/                   fetch_arxiv_meta.py · build_papers_csv.py · generator.py
```

常用命令：

```bash
# 增补论文后重新生成 README（条目定义在 src/build_papers_csv.py，主线定义在 data/topics.csv）
python3 src/fetch_arxiv_meta.py && python3 src/build_papers_csv.py && python3 src/generator.py

# 下载核心论文原文（加 --all 下载 data/papers.csv 中全部 arXiv 论文）
bash scripts/download_papers.sh

# 用 SuperTranslate 翻译（需要 LLM API key，如 DEEPSEEK_API_KEY）；无 key 时用 scripts/manual_translate.py 的人工译文表通路
bash scripts/translate_papers.sh

# 重建全部报告与幻灯片 PDF（pandoc + XeLaTeX + Playwright/Chromium）
bash scripts/build_docs.sh
```

欢迎通过 Pull Request 增补论文或修正说明，流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可与引用

代码（`src/`、`scripts/`、幻灯片源码）采用 MIT 许可；报告、清单、译文表等内容采用 CC BY 4.0；论文 PDF 与源材料转写的版权归原作者，详见 [LICENSE](LICENSE)。

```bibtex
@misc{awesome_agentic_robot_2026,
  title  = {Awesome Agentic Robot: Agent + Robot Papers, Reports and Slides},
  author = {asimfish},
  year   = {2026},
  url    = {https://github.com/asimfish/awesome_agentic_robot}
}
```
