# Awesome Agentic Robot: Agent + Robot Papers, Reports and Slides

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![papers](https://img.shields.io/badge/papers-{N_PAPERS}-blue) ![topics](https://img.shields.io/badge/topic%20lines-{N_TOPICS}-green) ![updated](https://img.shields.io/badge/updated-{DATE}-lightgrey)

A curated reading map of **Agentic Robotics** (Agent × Robot): coding agents that write robot policies, harnesses and runtimes around frozen VLAs, robot memory, reflection and self-evolution, VLA + RL, digital twins, fleet learning, safety and hardware standards. The list follows the 23 topic lines of the "Agent + Robot 论文检索地图" and adds two lines: a foundation line (LLM agents and harness engineering) and a Robot RSI line (recursive self-improvement, from the 具身纪元 essay), so that the software-side theory and the robotics-side practice can be read together.

一份 **Agentic Robotics（Agent × Robot）** 的检索地图与解读仓库：Coding Agent 写机器人策略、围绕冻结 VLA 的 Harness 与 Runtime、机器人记忆、反思与自进化、VLA + RL、数字孪生、群体学习、安全与硬件标准。按"Agent + Robot 论文检索地图"的 23 条主线组织，并增加两条主线：基础主线（LLM Agent 与 Harness 工程）和 Robot RSI 主线（递归自我改进，来自具身纪元的文章），把软件侧理论和机器人侧实践放在一起读。

We mark robotics works that are explicitly named in the source materials (the retrieval map, the Xiaohongshu essay, the Code-as-Policy deck and the 具身纪元 Robot RSI essay) with ⭐; the remaining entries were found by an arXiv sweep of 2025-2026 work along each line. Every entry links to the paper and, when available, to code.

*Maintained by [asimfish](https://github.com/asimfish). Built on 2026-09-06 from five inputs: the Xiaohongshu essay "Harness 之后，Agent+Robot 下一站是什么？" by 具身RL日记, the 25-slide deck `code_policy_self_evolving_agents.pptx`, the two-page "Agent + Robot 论文检索地图", Lilian Weng's Lil'Log posts on LLM agents and harness engineering, and the 具身纪元 WeChat essay "GPT-6 未必能当好机器人的大脑，却可能帮王兴兴加速 RobotRSI" by Marilyn Liu. Contributions welcome via pull request; see [CONTRIBUTING.md](CONTRIBUTING.md).*

## Deliverables

| Item | 中文 | English |
|---|---|---|
| Detailed report (Markdown) | [docs/reports/report_zh.md](docs/reports/report_zh.md) | [docs/reports/report_en.md](docs/reports/report_en.md) |
| Detailed report (PDF) | [docs/reports/report_zh.pdf](docs/reports/report_zh.pdf) | [docs/reports/report_en.pdf](docs/reports/report_en.pdf) |
| Summary slides, HTML deck (19 slides, bilingual) | [docs/slides/index.html](docs/slides/index.html) — open in a browser, arrow keys to navigate, `P` prints to PDF; a pre-rendered export is [docs/slides/index.pdf](docs/slides/index.pdf) | same file |
| Summary slides, Beamer PDF (25 pages incl. backup) | [docs/slides/agentic_robot_slides.pdf](docs/slides/agentic_robot_slides.pdf) ([source](docs/slides/agentic_robot_slides.tex)) | same file |
| Source-material transcripts | [sources/](sources/) — Xiaohongshu essay transcript, deck text and notes, retrieval-map transcript, Lil'Log archives, 具身纪元 Robot RSI essay transcript | |
| Core papers, original + Chinese (SuperTranslate, layout-preserving) | [papers/pdf_zh/](papers/pdf_zh/) — see [papers/README.md](papers/README.md) for what is translated | originals in [papers/pdf/](papers/pdf/) |
| Machine-readable data | [data/papers.csv](data/papers.csv), [data/topics.csv](data/topics.csv), [data/paper_meta.json](data/paper_meta.json) | regenerate README with `python3 src/build_papers_csv.py && python3 src/generator.py` |

<p align="center">
  <a href="docs/slides/index.html"><img src="docs/assets/slides_preview/pdf_01.png" width="49%" alt="HTML deck, title slide"></a>
  <a href="docs/slides/index.html"><img src="docs/assets/slides_preview/pdf_13.png" width="49%" alt="HTML deck, architecture slide"></a>
</p>

### Six conclusions of the report (TL;DR)

1. **The optimised object is moving up the stack.** Code as Policies (2022) had an LLM write one policy program; SkillOpt, ASPIRE, RHO and ENPIRE (2026) have a coding agent optimise a skill document, a policy repository, a training recipe or a whole harness: $z_{t+1} = A(z_t, \tau_t, r_t, \log_t)$.
2. **"Frozen VLA + learning around it" is the 2026 default, with a ceiling.** Harness VLA, BATON, AGM, HyMeS and Zetta never touch VLA weights; LWD and Q-Planning show real-world feedback still has to be written back into weights.
3. **The verifier is the bottleneck and a new scaling axis.** SessionVerifier, Evaluation as Exit Codes, evidence-gated progress pointers, LLM-as-a-Verifier.
4. **Harness became a real-time-systems problem.** A robot harness intervenes in control, compute and communication at once and must know latency, deadlines and fallbacks.
5. **Fleets are the route to experience at scale, with sublinear returns.** 16 robots take one VLA to 95% (LWD); 8 stations give 2-3× speed, not 8× (ENPIRE).
6. **Robot RSI is the frame that ties it together.** The 具身纪元 essay's two axes (what is improved: deployment-time / training-time / evaluator / research process × how much a human is in the loop) place ENPIRE, ASPIRE, RoboHarness, RoboClaw, PRIMO R1, VERITAS, Eureka and DrEureka next to Reflexion, STaR, Let's Verify, Meta-Rewarding and The AI Scientist; the frontier LLM is more likely to become the cognitive hub of the robot research loop than the robot's end-effector controller.

## Repository layout

```
README.md                  this file (generated from data/*.csv by src/generator.py)
data/                      topics.csv (25 lines), papers.csv (169 entries), paper_meta.json (arXiv metadata), header.md
docs/reports/              report_zh.md/.pdf, report_en.md/.pdf, LaTeX header + pandoc Lua filter + build scripts
docs/slides/               index.html (HTML deck) + index.pdf, agentic_robot_slides.tex/.pdf (Beamer)
papers/pdf/                original PDFs of the five core papers
papers/pdf_zh/             Chinese versions rendered by SuperTranslate; *.inspect.json = QA report
papers/translations/       human translation tables used by scripts/manual_translate.py
sources/                   transcripts and archives of the four input materials
scripts/                   download_papers.sh, translate_papers.sh, manual_translate.py, export_slides_pdf.py, build_docs.sh
src/                       fetch_arxiv_meta.py, build_papers_csv.py, generator.py
```

## How the list is organised

Each topic line below lists the works in chronological order. The first line of an entry is `**Title.** Venue, Year. [paper] [code]`, the second line is the author list, and core entries carry a one-sentence Chinese note on what the work contributes to the line. A paper that belongs to several lines appears under each of them.
