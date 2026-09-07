# Awesome Agentic Robot：Agent × Robot 论文地图、解读报告与幻灯片

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![papers](https://img.shields.io/badge/%E8%AE%BA%E6%96%87-{N_PAPERS}-blue) ![topics](https://img.shields.io/badge/%E4%B8%BB%E7%BA%BF-{N_TOPICS}-green) ![updated](https://img.shields.io/badge/%E6%9B%B4%E6%96%B0-{DATE}-lightgrey) ![license](https://img.shields.io/badge/license-MIT%20%2B%20CC--BY--4.0-orange)

一份面向 **Agentic Robotics（Agent × Robot）** 的中文检索地图与解读仓库。主题覆盖：Coding Agent 写机器人策略、围绕冻结 VLA 的 Harness 与 Runtime、机器人记忆、反思与自进化、VLA + RL、数字孪生、群体学习、安全与治理、硬件标准接口，以及把这些串起来的 Robot RSI（递归自我改进）。

*A Chinese-first reading map of Agentic Robotics with bilingual reports and slides. English report: [docs/reports/report_en.pdf](docs/reports/report_en.pdf).*

**仓库地址** <https://github.com/asimfish/awesome_agentic_robot> · 维护 [asimfish](https://github.com/asimfish) · 首次构建 2026-09-06 · 最近更新 {DATE}

## 目录

1. [产物入口](#产物入口)（含[我们的方案](docs/proposal/PROPOSAL_agent_data_engine_zh.md)）
2. [总览图](#总览图)
3. [仓库简介](#仓库简介)
4. [六条核心结论](#六条核心结论)
5. [源材料](#源材料)
6. [深度解读索引](#深度解读索引)（{N_NOTES} 篇）
7. [论文清单](#论文清单)（{N_TOPICS} 条主线，{N_PAPERS} 篇）
8. [统计](#统计)
9. [复现与贡献](#复现与贡献)
10. [许可与引用](#许可与引用)

## 产物入口

| 想要 | 打开 | 说明 |
|---|---|---|
| **我们的方案** | [`docs/proposal/PROPOSAL_agent_data_engine_zh.md`](docs/proposal/PROPOSAL_agent_data_engine_zh.md) | HARVEST：以前沿多模态 Agent 为遥操作员、规则记忆为脚手架、独立验证器为准入、三级补齐接触段、训好的动作头交回 Agent 自举的机器人数据引擎——架构、数据格式、12 周计划、五条可证伪假设、基线与指标 |
| **15 分钟拿到全部结论** | [`docs/slides/index.html`](docs/slides/index.html) · [PDF](docs/slides/index.pdf) | 19 页 HTML 幻灯片，浏览器打开 ← → 翻页、F 全屏、P 打印；另有 [Beamer 版 PDF](docs/slides/agentic_robot_slides.pdf)（25 页，含参考文献与备份页） |
| **系统研读** | [`report/survey_full_report.pdf`](report/survey_full_report.pdf) · [HTML](report/survey_full_report.html) | {N_FULL_PAGES} 页全文合订本：封面 + 两级目录 + 两张总览图 + Part 0 执行摘要 + Part 1 五份材料解读与 25 条主线综述 + Part A-G 共 {N_NOTES} 份深度解读 |
| **两份解读报告** | [中文 PDF](docs/reports/report_zh.pdf) · [英文 PDF](docs/reports/report_en.pdf) | 独立成篇的中英文报告（19 / 21 页）：五份材料逐一解读、主线综述、十条洞见、八个开放问题；Markdown 源在 [`docs/reports/`](docs/reports/) |
| **趋势与洞察** | [`insights/10_trends_insights_zh.md`](insights/10_trends_insights_zh.md) | 一页结论 · 领域时间线 · 六大趋势 · 十条洞察 · 八条可证伪预测（12-24 个月，到期回来核对） |
| **研究机会清单** | [`insights/11_open_problems_zh.md`](insights/11_open_problems_zh.md) | 19 个待验证问题，按 Part A-G 排列，每条配「缺口 + 为什么重要 + 最小可行实验 + 相关解读」；只做一件事就做第 1 条（分层验证器） |
| **数字口径账本** | [`insights/12_numbers_ledger_zh.md`](insights/12_numbers_ledger_zh.md) | 30 余个头条数字逐条标注任务集 / 指标类型 / 对照 / 干预与更新 / 证据形式——并排任何两个数字前先查此表 |
| **总览图** | [图 1 时间线](assets/fig1_timeline.svg) · [图 2 分类树](assets/fig2_taxonomy.svg) | 矢量 SVG，`scripts/make_figures.py` 生成；深色版见 `assets/*_dark.svg` |
| **逐篇深度解读** | [`notes/`](notes/) | {N_NOTES} 份中文解读（编号 01-43），每份含一句话定位 / 问题 / 方法 / 结果与口径 / 局限 / 关系定位 / 延伸批判；索引见[下文](#深度解读索引) |
| **论文原文与中译** | [`papers/pdf/`](papers/pdf/) · [`papers/pdf_zh/`](papers/pdf_zh/) | 六篇核心论文原文与 [SuperTranslate](https://github.com/asimfish/super_translate) 保版式中译（Code as Policies 正文全译，其余首页或首两页）；方法见 [`papers/README.md`](papers/README.md) |
| **源材料转写** | [`sources/`](sources/) | 小红书长文 39 卡转写、讲稿文字与备注、检索地图转写、Lil'Log 两篇存档、具身纪元文章与其小红书版转写 |
| **机器可读数据** | [`data/papers.csv`](data/papers.csv) · [`data/topics.csv`](data/topics.csv) · [`data/paper_meta.json`](data/paper_meta.json) | {N_PAPERS} 条论文条目、{N_TOPICS} 条主线、arXiv 元数据；README 由此生成 |

> 所有成功率数字都依赖各自的任务集与判定口径，**不同工作的数字禁止直接比大小**；详见各篇解读的「结果与口径」节与[数字口径账本](insights/12_numbers_ledger_zh.md)。

## 总览图

![图 1 · 时间线](assets/fig1_timeline.svg)

*图 1 · {N_PAPERS} 篇中约 100 项代表工作的时间线：按七个 Part 分泳道、按发表年月定位，★ 为源材料点名的核心工作，橙色竖带为 2026 年 6-8 月——Harness、记忆、自进化论文密度最高的季度。*

![图 2 · 分类树](assets/fig2_taxonomy.svg)

*图 2 · 分类体系：七个 Part、25 条主线（括号内为条目数）——与下文论文清单和全文报告的 Part A-G 一一对应。*

## 仓库简介

- **组织方式**：按《Agent + Robot 论文检索地图》的 23 条主线组织，另加两条：T0「基础：LLM Agent 与 Harness 工程」收软件侧理论（含 Lil'Log 两篇文章的全部参考文献），T24「Robot RSI」收递归自我改进这条把各主线串起来的线。一篇论文属于多条主线时会在每条下重复出现。
- **标注规则**：⭐ 表示被源材料点名的机器人侧核心工作；未标星的条目来自沿每条主线对 2025-2026 年 arXiv 的扩展检索（扩展），或软件侧 Agent / Harness / RSI 的基础工作（基础）。
- **条目格式**：`**标题.** 发表信息, 年份. [paper] [code]`，下一行为作者，再下一行为一句中文说明（这项工作对该主线的贡献）。
- **数据口径**：全部条目经 arXiv API 核实标题、作者与日期；非 arXiv 条目（博客、技术报告、标准预览）单独标注来源。报告中严格区分「论文报告的数字」与「我们的判断」。

## 六条核心结论

1. **优化对象在上移。** 2022 年的 Code as Policies 让 LLM 写一段策略代码；2026 年的 SkillOpt、ASPIRE、RHO、ENPIRE 让 coding agent 优化的对象变成技能文档、策略仓库、训练配方和整套 harness。讲稿的统一公式 $z_{t+1} = A(z_t, \tau_t, r_t, \log_t)$ 抓住了这个变化：被学习的 $z$ 从动作变成了外部可训练产物。
2. **「冻结 VLA + 外围学习」是 2026 年的默认范式，但有天花板。** Harness VLA、BATON、AGM、HyMeS、Zetta 都不改 VLA 权重；LWD（16 台机器人推到 95%）和 Q-Planning（真机 40%→90%）说明真实反馈最终还要写回权重。
3. **验证器是新的瓶颈，也是新的 scaling 轴。** PhyAgentOS 的 SessionVerifier、Thea 的 Evaluation as Exit Codes、AGM「物理证据才推进进度指针」、LLM-as-a-Verifier：能不能自进化，取决于能不能可靠判断「这一步成没成」。
4. **Harness 从软件术语变成了机器人中间件问题。** 机器人的 harness 要同时在控制、计算、通信三处介入，必须知道模型最大延迟、技能 deadline 和断网后的 fallback——这是操作系统与实时系统设计，不是 prompt 工程。
5. **群体是经验规模化的出路，收益亚线性。** ENPIRE 用 8 个工位把收敛时间压到 1/3-1/2：8 倍机器人换来 2-3 倍加速，多出来的是假设吞吐量，不是 rollout 数量。
6. **Robot RSI 是把这些串起来的框架。** 具身纪元文章的两条轴线（改进环节：部署时自演化 / 训练时自迭代 / 自我评估 / 自动研究 × 人的参与程度）把 ENPIRE、ASPIRE、RoboHarness、PRIMO R1、VERITAS、Eureka 与软件侧的 Reflexion、STaR、AI Scientist 放进同一张表；前沿 LLM 更可能先成为机器人研发循环的认知中枢，而不是机器人的末端控制器。

一句话：下一阶段不是 Model Scaling，也不只是 Harness Scaling，而是 **System Scaling + Experience Scaling**——先训练出足够好的机器人让它开始工作，再让工作本身继续训练机器人。

## 源材料

| # | 材料 | 作者 / 平台 | 原文 | 仓库内转写 | 解读位置 |
|---|---|---|---|---|---|
| 1 | 《Harness 之后，Agent+Robot 下一站是什么？》（39 张图文卡片） | 具身RL日记 · 小红书 | [原帖](https://www.xiaohongshu.com/explore/6a9d2fb10000000026033df2) | [转写](sources/xiaohongshu_harness_next_transcript.md) | 报告第 2 章 |
| 2 | Code-as-Policy → 自进化机器人 Agent 讲稿（25 页 PPTX） | 用户提供 | [PPTX](sources/code_policy_self_evolving_agents.pptx) | [文字与备注提取](sources/code_policy_deck_extracted.md) | 报告第 3 章 |
| 3 | 《Agent + Robot 论文检索地图》（23 条主线） | 用户提供的两页表格 | — | [转写](sources/retrieval_map_transcript.md)、[data/topics.csv](data/topics.csv) | 报告第 4 章（逐线） |
| 4 | 《LLM Powered Autonomous Agents》(2023)、《Harness Engineering for Self-Improvement》(2026) | Lilian Weng · Lil'Log | [2023](https://lilianweng.github.io/posts/2023-06-23-agent/)、[2026](https://lilianweng.github.io/posts/2026-07-04-harness/) | [2023 存档](sources/lilianweng_2023-06-23_llm_agents.txt)、[2026 存档](sources/lilianweng_2026-07-04_harness_engineering.txt)；两文 60 条参考文献全部收入 T0 | 报告第 5 章 |
| 5 | 《GPT-6 未必能当好机器人的大脑，却可能帮王兴兴加速 RobotRSI》及其小红书图文版《GPT-6 Astra 开启 Robot RSI 时代》 | Marilyn Liu · 具身纪元（公众号）；♥VLA和RL的具身未来（小红书） | [公众号](https://mp.weixin.qq.com/s/DTj1be0CGhwcvaFh2WI0HA)、[小红书](https://www.xiaohongshu.com/explore/6a9e3498000000002802d485) | [公众号转写](sources/wechat_embodied_era_robot_rsi_transcript.md)、[小红书转写](sources/xiaohongshu_robot_rsi_howto_transcript.md) | 报告第 6 章、主线 T24 |
| 6 | 《RoboCurve：GPT-6 Astra 直接控制机器人》（RoboCurve 第三方测试解读） | 罗清雨 · 知乎 | [知乎](https://zhuanlan.zhihu.com/p/208031326825455257) | [转写](sources/zhihu_robocurve_gpt6_astra_transcript.md) | [解读 44](notes/44_gpt6_astra_data_engine_zh.md)：演示定位 + Agent-as-Teleoperator 数据引擎方案 |

## 深度解读索引

{NOTES_INDEX}
