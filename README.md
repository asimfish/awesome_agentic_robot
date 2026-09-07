# Awesome Agentic Robot：Agent × Robot 论文地图、解读报告与幻灯片

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![papers](https://img.shields.io/badge/%E8%AE%BA%E6%96%87-209-blue) ![topics](https://img.shields.io/badge/%E4%B8%BB%E7%BA%BF-25-green) ![updated](https://img.shields.io/badge/%E6%9B%B4%E6%96%B0-2026-09-08-lightgrey) ![license](https://img.shields.io/badge/license-MIT%20%2B%20CC--BY--4.0-orange)

一份面向 **Agentic Robotics（Agent × Robot）** 的中文检索地图与解读仓库。主题覆盖：Coding Agent 写机器人策略、围绕冻结 VLA 的 Harness 与 Runtime、机器人记忆、反思与自进化、VLA + RL、数字孪生、群体学习、安全与治理、硬件标准接口，以及把这些串起来的 Robot RSI（递归自我改进）。

*A Chinese-first reading map of Agentic Robotics with bilingual reports and slides. English report: [docs/reports/report_en.pdf](docs/reports/report_en.pdf).*

**仓库地址** <https://github.com/asimfish/awesome_agentic_robot> · 维护 [asimfish](https://github.com/asimfish) · 首次构建 2026-09-06 · 最近更新 2026-09-08

## 目录

1. [产物入口](#产物入口)（含[我们的方案](docs/proposal/PROPOSAL_agent_data_engine_zh.md)）
2. [总览图](#总览图)
3. [仓库简介](#仓库简介)
4. [六条核心结论](#六条核心结论)
5. [源材料](#源材料)
6. [深度解读索引](#深度解读索引)（45 篇）
7. [论文清单](#论文清单)（25 条主线，209 篇）
8. [统计](#统计)
9. [复现与贡献](#复现与贡献)
10. [许可与引用](#许可与引用)

## 产物入口

| 想要 | 打开 | 说明 |
|---|---|---|
| **我们的方案** | [`docs/proposal/PROPOSAL_agent_data_engine_zh.md`](docs/proposal/PROPOSAL_agent_data_engine_zh.md) | HARVEST：以前沿多模态 Agent 为遥操作员、规则记忆为脚手架、独立验证器为准入、三级补齐接触段、训好的动作头交回 Agent 自举的机器人数据引擎——架构、数据格式、12 周计划、五条可证伪假设、基线与指标 |
| **15 分钟拿到全部结论** | [`docs/slides/index.html`](docs/slides/index.html) · [PDF](docs/slides/index.pdf) | 19 页 HTML 幻灯片，浏览器打开 ← → 翻页、F 全屏、P 打印；另有 [Beamer 版 PDF](docs/slides/agentic_robot_slides.pdf)（25 页，含参考文献与备份页） |
| **系统研读** | [`report/survey_full_report.pdf`](report/survey_full_report.pdf) · [HTML](report/survey_full_report.html) | 148 页全文合订本：封面 + 两级目录 + 两张总览图 + Part 0 执行摘要 + Part 1 五份材料解读与 25 条主线综述 + Part A-G 共 45 份深度解读 |
| **两份解读报告** | [中文 PDF](docs/reports/report_zh.pdf) · [英文 PDF](docs/reports/report_en.pdf) | 独立成篇的中英文报告（19 / 21 页）：五份材料逐一解读、主线综述、十条洞见、八个开放问题；Markdown 源在 [`docs/reports/`](docs/reports/) |
| **趋势与洞察** | [`insights/10_trends_insights_zh.md`](insights/10_trends_insights_zh.md) | 一页结论 · 领域时间线 · 六大趋势 · 十条洞察 · 八条可证伪预测（12-24 个月，到期回来核对） |
| **研究机会清单** | [`insights/11_open_problems_zh.md`](insights/11_open_problems_zh.md) | 19 个待验证问题，按 Part A-G 排列，每条配「缺口 + 为什么重要 + 最小可行实验 + 相关解读」；只做一件事就做第 1 条（分层验证器） |
| **数字口径账本** | [`insights/12_numbers_ledger_zh.md`](insights/12_numbers_ledger_zh.md) | 30 余个头条数字逐条标注任务集 / 指标类型 / 对照 / 干预与更新 / 证据形式——并排任何两个数字前先查此表 |
| **总览图** | [图 1 时间线](assets/fig1_timeline.svg) · [图 2 分类树](assets/fig2_taxonomy.svg) | 矢量 SVG，`scripts/make_figures.py` 生成；深色版见 `assets/*_dark.svg` |
| **逐篇深度解读** | [`notes/`](notes/) | 45 份中文解读（编号 01-43），每份含一句话定位 / 问题 / 方法 / 结果与口径 / 局限 / 关系定位 / 延伸批判；索引见[下文](#深度解读索引) |
| **论文原文与中译** | [`papers/pdf/`](papers/pdf/) · [`papers/pdf_zh/`](papers/pdf_zh/) | 六篇核心论文原文与 [SuperTranslate](https://github.com/asimfish/super_translate) 保版式中译（Code as Policies 正文全译，其余首页或首两页）；方法见 [`papers/README.md`](papers/README.md) |
| **源材料转写** | [`sources/`](sources/) | 小红书长文 39 卡转写、讲稿文字与备注、检索地图转写、Lil'Log 两篇存档、具身纪元文章与其小红书版转写 |
| **机器可读数据** | [`data/papers.csv`](data/papers.csv) · [`data/topics.csv`](data/topics.csv) · [`data/paper_meta.json`](data/paper_meta.json) | 209 条论文条目、25 条主线、arXiv 元数据；README 由此生成 |

> 所有成功率数字都依赖各自的任务集与判定口径，**不同工作的数字禁止直接比大小**；详见各篇解读的「结果与口径」节与[数字口径账本](insights/12_numbers_ledger_zh.md)。

## 总览图

![图 1 · 时间线](assets/fig1_timeline.svg)

*图 1 · 209 篇中约 100 项代表工作的时间线：按七个 Part 分泳道、按发表年月定位，★ 为源材料点名的核心工作，橙色竖带为 2026 年 6-8 月——Harness、记忆、自进化论文密度最高的季度。*

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

| Part | 编号 · 解读 | 一句话 |
|---|---|---|
| **A** · 主线：Coding Agent 与自进化 | [01 · Code as Policies 深度解读](notes/01_code_as_policies_zh.md) | 让 LLM 写的程序成为机器人策略 |
| A | [02 · CaP-X 深度解读](notes/02_capx_zh.md) | 把 Code-as-Policy 做成可以被系统研究的平台 |
| A | [03 · RHO 深度解读](notes/03_rho_zh.md) | 训练时搜索策略仓库，部署时单轮执行 |
| A | [04 · ASPIRE 深度解读](notes/04_aspire_zh.md) | 失败修复沉淀成技能，技能库越大适应越快 |
| A | [05 · SkillOpt 深度解读](notes/05_skillopt_zh.md) | 把技能文档当作冻结 Agent 的可训练外部状态 |
| A | [06 · ENPIRE 深度解读](notes/06_enpire_zh.md) | 把真机学习变成 coding agent 可以管理的优化过程 |
| A | [07 · 自进化续作合评](notes/07_self_evolution_successors_zh.md) | Zetta、SHAPER、PRACTICE、SkillGLoW、HiSME、MEMENTO |
| A | [08 · 自动研究谱系](notes/08_autoresearch_lineage_zh.md) | Eureka → DrEureka → HARBOR / Nautilus / AgenticRobotics / Push-T 重访 |
| A | [09 · 技能库谱系](notes/09_skill_library_lineage_zh.md) | 从 LLM 提任务到形式化可验证的技能契约 |
| **B** · 记忆、反思与验证 | [10 · RoboMME 与 RoboMME-Interference 深度解读](notes/10_robomme_zh.md) | 机器人记忆的评测基准与它的两个结论 |
| B | [11 · PonderPounce 深度解读](notes/11_ponderpounce_zh.md) | 用 MLLM 的原生因果上下文当机器人记忆 |
| B | [12 · AGM 深度解读](notes/12_agm_zh.md) | 只有物理证据才能推进进度指针 |
| B | [13 · HyMeS 深度解读](notes/13_hymes_zh.md) | "技能在权重里，记忆在代码里" |
| B | [14 · BATON 深度解读](notes/14_baton_zh.md) | 长程问题是技能交接问题 |
| B | [15 · 权重内记忆与记忆选择合评](notes/15_in_weight_memory_zh.md) | NativeMEM、LaMem-VLA、Remember Smarter、OnEvoMemory、Memory Anchors、概念中心记忆 |
| B | [16 · 反思与纠错合评](notes/16_reflection_correction_zh.md) | REMAC、PhysReflect-VLA、Agentic RAG-VLM、PhysiAgent |
| B | [17 · PRIMO R1 深度解读](notes/17_primo_r1_zh.md) | 从"观察者"到"批评者"的过程级视频验证 |
| B | [18 · VERITAS 深度解读](notes/18_veritas_zh.md) | 推理时视觉验证，验证过的 rollout 直接成为训练数据 |
| B | [19 · 验证器谱系](notes/19_verifier_lineage_zh.md) | LLM-as-a-Verifier、立场论文、Consilience、Agentic Harnesses |
| **C** · Harness、Runtime、双系统与端侧 | [20 · Harness VLA 深度解读](notes/20_harness_vla_zh.md) | 不改权重、不扩技能库，学冻结 VLA 的"使用说明书" |
| C | [45 · Harness VLA × Agent 数据引擎](notes/45_harness_vla_rules_for_data_engine_zh.md) | 把"规则记忆"加进采集 agent |
| C | [21 · PhyAgentOS 深度解读](notes/21_phyagentos_zh.md) | 把 Harness 做成操作系统 |
| C | [22 · Thea 深度解读](notes/22_thea_zh.md) | 物理世界不白送的两样东西——读状态、判结果 |
| C | [23 · Harness Engineering for Physical AI 深度解读](notes/23_harness_engineering_physical_ai_zh.md) | 机器人中间件就是 harness 层 |
| C | [24 · Harness 框架合评](notes/24_harness_frameworks_zh.md) | RoboHarness、Guava、Cortex 与 Agentic Harnesses |
| C | [25 · 治理与运行时合评](notes/25_runtime_governance_zh.md) | Runtime Governance、EmbodiedGovBench、ICAN-Deploy、FSAR |
| C | [26 · 快慢双系统合评](notes/26_dual_systems_zh.md) | Fast-in-Slow、OneTwoVLA、StreamVLA、LaST0、RationalVLA 与 2026 年的频率分层 |
| C | [27 · 端侧部署合评](notes/27_edge_deployment_zh.md) | PhyAI、EcoVLA、CloudEdgeVLA、ARLI、ST-Merge、Habilis-β |
| **D** · 学习闭环：RL、数据回流、数字孪生与世界模型 | [28 · LWD 深度解读](notes/28_lwd_zh.md) | 16 台机器人的 fleet-scale 离线到在线 RL |
| D | [29 · Q-Planning 深度解读](notes/29_q_planning_zh.md) | 只微调一个小 Q 函数，就能从部署失败里学 |
| D | [30 · TwinRL 与数字孪生谱系](notes/30_twinrl_digital_twin_zh.md) | Sim 是 sandbox，不是训练场 |
| D | [31 · RoboClaw 深度解读](notes/31_roboclaw_zh.md) | 让机器人同时学会"做任务"与"恢复现场" |
| D | [32 · VLA + RL 合评](notes/32_vla_rl_credit_zh.md) | 信用分配、免外部奖励与测试时 RL |
| D | [33 · 世界模型的角色合评](notes/33_world_model_roles_zh.md) | H-WM、Motus2、ContactGuard、SafeDojo、Online Continual RL、RoboGene |
| D | [44 · RoboCurve 的 GPT-6 Astra 演示与"Agent 当遥操作员"的数据引擎](notes/44_gpt6_astra_data_engine_zh.md) | 解读与方案 |
| **E** · 总览、接口、多机器人与跨本体 | [34 · AgenticLab / PLanAR 深度解读](notes/34_agenticlab_zh.md) | 用规划语言定义 VLM 的推理空间 |
| E | [35 · Agent + Robot 总览合评](notes/35_agent_robot_overview_zh.md) | Agentic Robot、ManiAgent、VoLo、HoloAgent-0 与"灵活但仍脆弱" |
| E | [36 · 接口层合评](notes/36_rosclaw_mhs_interfaces_zh.md) | 两篇 ROSClaw、MHS、OpenClaw 生态与 MCP |
| E | [37 · 多机器人协作合评](notes/37_multi_robot_zh.md) | RoCo、MALMM、REMAC、RoboOS 系列、DynaHMRC、Scale-Plan、MeCo、Tool-RoCo、对话对齐与通信攻击 |
| E | [38 · 生命周期、跨本体与主动感知合评](notes/38_lifecycle_active_perception_zh.md) | Arcadia、PhysCaP、ActiveVLA 与相关工作 |
| **F** · 安全与治理 | [39 · 安全合评](notes/39_safety_zh.md) | EMBGuard、SENTINEL、VASO、Same Weights Different Robot、RationalVLA、通信攻击与 AgentRob |
| **G** · 基础：LLM Agent、Harness 工程与 RSI | [40 · Lil'Log 两篇深度解读](notes/40_lilianweng_posts_zh.md) | 《LLM Powered Autonomous Agents》与《Harness Engineering for Self-Improvement》 |
| G | [41 · RSI 谱系](notes/41_rsi_lineage_zh.md) | 从 Good 1965 到 BigBang-V1——软件侧递归自我改进的四个环节 |
| G | [42 · Harness 演化方法合评](notes/42_harness_evolution_methods_zh.md) | ACE、MCE、Meta-Harness、Self-Harness、AHE、Harness Updating ≠ Harness Benefit、DGM、Hyperagents、AlphaEvolve、ShinkaEvolve、ThetaEvolve、GEPA、Promptbreeder、STOP、ADAS、AFlow 与相关工作 |
| G | [43 · AI 研发基准与失败模式合评](notes/43_ai_research_benchmarks_zh.md) | PaperBench、RE-Bench、MLE-bench、ScienceAgentBench、CORE-Bench、KernelBench、Early Science Acceleration 与《Why LLMs Aren't Scientists Yet》 |


## 论文清单

共 25 条主线、209 篇论文，按主线分组、组内按时间排序。每条主线先给检索关键词与代表工作，再列条目；⭐ 为源材料点名的核心工作。点击主线标题可回到本目录。

<table>
<tr>
	<td>&emsp;<a href="#基础llm-agent-与-harness-工程--foundations-llm-agents--harness-engineering">0. 基础：LLM Agent 与 Harness 工程（Foundations: LLM Agents &amp; Harness Engineering）</a></td>
	<td>&emsp;<a href="#agent--robot-总览--agent--robot-overview">1. Agent + Robot 总览（Agent + Robot Overview）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#coding-agent-控机器人--coding-agents-control-robots">2. Coding Agent 控机器人（Coding Agents Control Robots）</a></td>
	<td>&emsp;<a href="#openclaw--ros-生态--openclaw--ros">3. OpenClaw / ROS 生态（OpenClaw / ROS）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#长程任务--long-horizon-tasks">4. 长程任务（Long-Horizon Tasks）</a></td>
	<td>&emsp;<a href="#机器人记忆--robot-memory">5. 机器人记忆（Robot Memory）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#反思与纠错--reflection--failure-correction">6. 反思与纠错（Reflection / Failure Correction）</a></td>
	<td>&emsp;<a href="#自进化--self-evolution">7. 自进化（Self-Evolution）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#技能库--skill-library">8. 技能库（Skill Library）</a></td>
	<td>&emsp;<a href="#vla--rl">9. VLA + RL</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#部署数据回流--deployment-data-flywheel">10. 部署数据回流（Deployment Data Flywheel）</a></td>
	<td>&emsp;<a href="#数字孪生--sim2real--digital-twin--sim2real">11. 数字孪生 / Sim2Real（Digital Twin / Sim2Real）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#世界模型--world-model">12. 世界模型（World Model）</a></td>
	<td>&emsp;<a href="#快慢双系统--fast-slow-dual-systems">13. 快慢双系统（Fast-Slow Dual Systems）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#端侧部署--edge-agent--edge-agent--on-device-deployment">14. 端侧部署 / Edge Agent（Edge Agent / On-Device Deployment）</a></td>
	<td>&emsp;<a href="#harness">15. Harness</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#runtime-运行时--runtime">16. Runtime 运行时（Runtime）</a></td>
	<td>&emsp;<a href="#安全--safety">17. 安全（Safety）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#标准接口--hardware-api--standard-interfaces--hardware-api">18. 标准接口 / Hardware API（Standard Interfaces / Hardware API）</a></td>
	<td>&emsp;<a href="#多机器人协作--multi-robot-collaboration">19. 多机器人协作（Multi-Robot Collaboration）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#跨本体--cross-embodiment">20. 跨本体（Cross-Embodiment）</a></td>
	<td>&emsp;<a href="#群体学习--fleet-learning--fleet-learning">21. 群体学习 / Fleet Learning（Fleet Learning）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#主动感知--active-perception">22. 主动感知（Active Perception）</a></td>
	<td>&emsp;<a href="#验证器--成功验证--verifier--success-verification">23. 验证器 / 成功验证（Verifier / Success Verification）</a></td>
</tr>
<tr>
	<td>&emsp;<a href="#robot-rsi递归自我改进--robot-rsi-recursive-self-improvement">24. Robot RSI：递归自我改进（Robot RSI: Recursive Self-Improvement）</a></td>
</tr>
</table>

### [基础：LLM Agent 与 Harness 工程 | Foundations: LLM Agents & Harness Engineering](#论文清单)

检索关键词：`LLM agent / harness engineering / recursive self-improvement / context engineering / agentic workflow search`　代表工作：Lil'Log (LLM Powered Autonomous Agents; Harness Engineering for Self-Improvement) and the full reference lists of both posts: ReAct, Reflexion, Toolformer, Generative Agents, ACE, Meta-Harness, Self-Harness, DGM, AlphaEvolve, STOP, AI-R&D benchmarks　（71 篇）

1. **Speculations Concerning the First Ultraintelligent Machine.** Advances in Computers 6:31-88, 1965. [paper](https://doi.org/10.1016/S0065-2458(08)60418-0)

    *Irving John Good*

    > 1965 年的“智能爆炸”设想：能设计出更强机器的机器会让新机器继续参与下一代设计；RSI 概念的源头。

2. **Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements.** arXiv, 2003. [paper](https://arxiv.org/abs/cs/0309048)

    *Jürgen Schmidhuber*

    > 自我改写的形式化起点：只有能证明某项修改会提高既定效用时才执行修改。

3. **Recursive Self-Improvement.** LessWrong, 2008. [paper](https://www.lesswrong.com/posts/JBadX7rwdcRFzGuju/recursive-self-improvement)

    *Eliezer Yudkowsky*

    > 2008 年对递归自我改进的系统论述，Lil'Log 与具身纪元文章均以其为概念参照。

4. **WebGPT: Browser-assisted question-answering with human feedback.** arXiv, 2021. [paper](https://arxiv.org/abs/2112.09332)

    *Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou, Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, John Schulman*

    > 浏览器辅助问答与人类反馈，工具使用的早期实证。

5. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.** NeurIPS 2022, 2022. [paper](https://arxiv.org/abs/2201.11903)

    *Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou*

    > Lil'Log 2023 文中 Planning 组件的起点：让模型逐步推理。

6. **STaR: Bootstrapping Reasoning With Reasoning.** NeurIPS 2022, 2022. [paper](https://arxiv.org/abs/2203.14465)

    *Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman*

    > 训练时自迭代：生成推理 → 答对保留、答错看答案重推 → 筛出的过程微调下一版模型。

7. **MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning.** arXiv, 2022. [paper](https://arxiv.org/abs/2205.00445)

    *Ehud Karpas, Omri Abend, Yonatan Belinkov, Barak Lenz, Opher Lieber, Nir Ratner, Yoav Shoham, Hofit Bata, Yoav Levine, Kevin Leyton-Brown, Dor Muhlgay, Noam Rozen, Erez Schwartz, Gal Shachaf, Shai Shalev-Shwartz, Amnon Shashua, Moshe Tenenholtz*

    > 模块化神经符号架构：LLM 路由到专家模块（计算器、API、知识库）。

8. **TALM: Tool Augmented Language Models.** arXiv, 2022. [paper](https://arxiv.org/abs/2205.12255)

    *Aaron Parisi, Yao Zhao, Noah Fiedel*

    > 用自博弈式迭代扩展工具调用数据。

9. **ReAct: Synergizing Reasoning and Acting in Language Models.** ICLR 2023, 2022. [paper](https://arxiv.org/abs/2210.03629)

    *Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao*

    > 推理与行动交织的 Thought / Action / Observation 循环，Agent 循环的标准形态。

10. **In-context Reinforcement Learning with Algorithm Distillation.** ICLR 2023, 2022. [paper](https://arxiv.org/abs/2210.14215)

    *Michael Laskin, Luyu Wang, Junhyuk Oh, Emilio Parisotto, Stephen Spencer, Richie Steigerwald, DJ Strouse, Steven Hansen, Angelos Filos, Ethan Brooks, Maxime Gazeau, Himanshu Sahni, Satinder Singh, Volodymyr Mnih*

    > 用上下文内强化学习蒸馏学习算法本身，Lil'Log 2023 文中“上下文即记忆”的例证。

11. **Chain of Hindsight Aligns Language Models with Feedback.** arXiv, 2023. [paper](https://arxiv.org/abs/2302.02676)

    *Hao Liu, Carmelo Sferrazza, Pieter Abbeel*

    > 用带反馈标注的历史输出序列微调模型，自反思的训练时版本。

12. **Toolformer: Language Models Can Teach Themselves to Use Tools.** NeurIPS 2023, 2023. [paper](https://arxiv.org/abs/2302.04761)

    *Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom*

    > 模型自监督学会何时调用哪个 API。

13. **Reflexion: Language Agents with Verbal Reinforcement Learning.** NeurIPS 2023, 2023. [paper](https://arxiv.org/abs/2303.11366) [code](https://github.com/noahshinn/reflexion)

    *Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao*

    > 部署时的记忆自改进：把测试 / 环境反馈写成反思存进记忆再重试，不更新权重；HumanEval 91%。

14. **Self-Refine: Iterative Refinement with Self-Feedback.** NeurIPS 2023, 2023. [paper](https://arxiv.org/abs/2303.17651)

    *Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, Peter Clark*

    > 同一模型生成 → 自我反馈 → 精炼的迭代，不训练；反思类方法的基线。

15. **HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face.** NeurIPS 2023, 2023. [paper](https://arxiv.org/abs/2303.17580)

    *Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, Yueting Zhuang*

    > ChatGPT 做任务规划与模型选择，调用 HuggingFace 上的专家模型执行。

16. **Generative Agents: Interactive Simulacra of Human Behavior.** UIST 2023, 2023. [paper](https://arxiv.org/abs/2304.03442)

    *Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein*

    > 记忆流 + 检索（新近性 / 重要性 / 相关性）+ 反思 + 规划的沙盒 agent，是 Robot Memory 主线常引的记忆架构。

17. **ChemCrow: Augmenting large-language models with chemistry tools.** arXiv, 2023. [paper](https://arxiv.org/abs/2304.05376)

    *Andres M Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D White, Philippe Schwaller*

    > 用 13 个化学工具增强 LLM 完成有机合成与材料设计。

18. **Emergent autonomous scientific research capabilities of large language models.** arXiv, 2023. [paper](https://arxiv.org/abs/2304.05332)

    *Daniil A. Boiko, Robert MacKnight, Gabe Gomes*

    > LLM 驾驭实验室自动化（含云实验室）做科学实验的早期案例。

19. **API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs.** arXiv, 2023. [paper](https://arxiv.org/abs/2304.08244)

    *Minghao Li, Yingxiu Zhao, Bowen Yu, Feifan Song, Hangyu Li, Haiyang Yu, Zhoujun Li, Fei Huang, Yongbin Li*

    > 工具增强 LLM 的评测基准。

20. **LLM+P: Empowering Large Language Models with Optimal Planning Proficiency.** arXiv, 2023. [paper](https://arxiv.org/abs/2304.11477)

    *Bo Liu, Yuqian Jiang, Xiaohan Zhang, Qiang Liu, Shiqi Zhang, Joydeep Biswas, Peter Stone*

    > LLM 把问题翻译成 PDDL，交给经典规划器求解；AgenticLab 等规划语言接口的先驱。

21. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models.** NeurIPS 2023, 2023. [paper](https://arxiv.org/abs/2305.10601)

    *Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan*

    > 把推理组织为树搜索，每步多候选并评估。

22. **Let's Verify Step by Step.** ICLR 2024, 2023. [paper](https://arxiv.org/abs/2305.20050)

    *Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe*

    > 过程奖励模型：逐步标出推理出错位置而非只看最终答案，为 RSI 提供细粒度评价信号。

23. **LLM Powered Autonomous Agents.** Lil'Log, 2023. [paper](https://lilianweng.github.io/posts/2023-06-23-agent/) [code](https://lilianweng.github.io/posts/2023-06-23-agent/)

    *Lilian Weng*

    > Agent = LLM + Planning + Memory + Tool use 的经典分解，是后续所有 Agent+Robot 架构图的原型。

24. **Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution.** arXiv, 2023. [paper](https://arxiv.org/abs/2309.16797)

    *Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero, Tim Rocktäschel*

    > 自指式 prompt 演化，突变 prompt 本身也被演化。

25. **Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation.** arXiv, 2023. [paper](https://arxiv.org/abs/2310.02304)

    *Eric Zelikman, Eliana Lorch, Lester Mackey, Adam Tauman Kalai*

    > 自学优化器：优化 improver 而非解本身；弱模型下会退化。

26. **Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models.** ICML 2024, 2024. [paper](https://arxiv.org/abs/2401.01335)

    *Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, Quanquan Gu*

    > 弱模型通过与自己历史版本博弈变强，无需额外人类数据。

27. **Self-Rewarding Language Models.** arXiv, 2024. [paper](https://arxiv.org/abs/2401.10020)

    *Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, Jason Weston*

    > 模型用 LLM-as-a-Judge 给自己的回答打分并做 DPO，回答与评价能力同时迭代。

28. **Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge.** arXiv, 2024. [paper](https://arxiv.org/abs/2407.19594)

    *Tianhao Wu, Weizhe Yuan, Olga Golovneva, Jing Xu, Yuandong Tian, Jiantao Jiao, Jason Weston, Sainbayar Sukhbaatar*

    > 同一模型既当回答者、评审者和“评审的评审”，评价能力本身自改进；四轮后 AlpacaEval 2 LC 胜率 22.9%→39.4%。

29. **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery.** arXiv, 2024. [paper](https://arxiv.org/abs/2408.06292) [code](https://github.com/SakanaAI/AI-Scientist)

    *Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha*

    > 自动研究：从代码模板出发提想法、查新颖性、改代码、跑实验、写论文并接受自动评审。

30. **Automated Design of Agentic Systems.** ICLR 2025, 2024. [paper](https://arxiv.org/abs/2408.08435)

    *Shengran Hu, Cong Lu, Jeff Clune*

    > 用 meta agent 在代码空间里搜索新的 agent 设计（ICLR 2025）。

31. **CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark.** TMLR 2024, 2024. [paper](https://arxiv.org/abs/2409.11363)

    *Zachary S. Siegel, Sayash Kapoor, Nitya Nadgir, Benedikt Stroebl, Arvind Narayanan*

    > 计算可复现性 agent 基准（TMLR 2024）。

32. **ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery.** ICLR 2025, 2024. [paper](https://arxiv.org/abs/2410.05080)

    *Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns, Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, Huan Sun*

    > 数据驱动科学发现任务上的语言 agent 严格评测（ICLR 2025）。

33. **MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering.** arXiv, 2024. [paper](https://arxiv.org/abs/2410.07095)

    *Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mądry*

    > 在 Kaggle 式机器学习工程任务上评测 agent。

34. **AFlow: Automating Agentic Workflow Generation.** ICLR 2025, 2024. [paper](https://arxiv.org/abs/2410.10762)

    *Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xionghui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng, Bang Liu, Yuyu Luo, Chenglin Wu*

    > 用 MCTS 在代码表示的工作流空间中自动生成 agentic workflow（ICLR 2025）。

35. **RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts.** ICML 2025, 2024. [paper](https://arxiv.org/abs/2411.15114)

    *Hjalmar Wijk, Tao Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael Chen, Josh Clymer, Jai Dhyani, Elena Ericheva, Katharyn Garcia, Brian Goodrich, Nikola Jurkovic, Holden Karnofsky, Megan Kinniment, Aron Lajko, Seraphina Nix, Lucas Sato, William Saunders, Maksym Taran, Ben West, Elizabeth Barnes*

    > 对比前沿 agent 与人类专家的 AI R&D 能力（ICML 2025）。

36. **KernelBench: Can LLMs Write Efficient GPU Kernels?.** arXiv, 2025. [paper](https://arxiv.org/abs/2502.10517)

    *Anne Ouyang, Simon Guo, Simran Arora, Alex L. Zhang, William Hu, Christopher Ré, Azalia Mirhoseini*

    > LLM 能否写出高效 GPU kernel 的基准，harness 演化常用的可验证任务。

37. **PaperBench: Evaluating AI's Ability to Replicate AI Research.** ICML 2025, 2025. [paper](https://arxiv.org/abs/2504.01848)

    *Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, Tejal Patwardhan*

    > 评测 AI 复现 AI 研究论文的能力（ICML 2025）。

38. **Absolute Zero: Reinforced Self-play Reasoning with Zero Data.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.03335)

    *Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Yang Yue, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, Gao Huang*

    > 零数据自博弈推理：模型自己提出可验证任务并求解，训练时自迭代的极端形式。

39. **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents.** arXiv 2025, 2025. [paper](https://arxiv.org/abs/2505.22954)

    *Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune*

    > 允许 coding agent 修改自身 harness 代码库并开放式演化，SWE-bench 20%→50%。

40. **AlphaEvolve: A coding agent for scientific and algorithmic discovery.** arXiv, 2025. [paper](https://arxiv.org/abs/2506.13131)

    *Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, Matej Balog*

    > 冻结 LLM 生成程序 diff 的演化搜索，EVOLVE-BLOCK 标记可改区域。

41. **GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning.** arXiv, 2025. [paper](https://arxiv.org/abs/2507.19457)

    *Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab*

    > 反思式 prompt 演化优于 RL 的实证。

42. **ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.19349)

    *Robert Tjarko Lange, Yuki Imajuku, Edoardo Cetin*

    > 开放式、样本高效的程序演化：新颖性拒绝采样与多模型集成；本报告建议用其去重机制缓解机器人集群的假设重复。

43. **Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models.** ICLR 2026, 2025. [paper](https://arxiv.org/abs/2510.04618)

    *Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, Kunle Olukotun*

    > 把上下文当作可演化的 playbook：Generator/Reflector/Curator 三角色，增量条目式更新避免上下文塌缩。

44. **Early science acceleration experiments with GPT-5.** arXiv, 2025. [paper](https://arxiv.org/abs/2511.16072)

    *Sébastien Bubeck, Christian Coester, Ronen Eldan, Timothy Gowers, Yin Tat Lee, Alexandru Lupsasca, Mehtaab Sawhney, Robert Scherrer, Mark Sellke, Brian K. Spears, Derya Unutmaz, Kevin Weil, Steven Yin, Nikita Zhivotovskiy*

    > 前沿模型加速科研的早期实证案例集。

45. **ThetaEvolve: Test-time Learning on Open Problems.** arXiv, 2025. [paper](https://arxiv.org/abs/2511.23473)

    *Yiping Wang, Shao-Rong Su, Zhiyuan Zeng, Eva Xu, Liliang Ren, Xinyu Yang, Zeyi Huang, Xuehai He, Luyao Ma, Baolin Peng, Hao Cheng, Pengcheng He, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, Yelong Shen*

    > 面向开放问题的测试时学习：在演化搜索中同时更新模型。

46. **BigBang: Pursuing Open-Ended Intelligence through Self-Evolving Synthesis of Verifiable Frontier Tasks.** Technical report, 2026. [paper](https://endlessfrontier.tech/assets/paper.pdf) [code](https://huggingface.co/endless-frontier/BigBang-v1)

    *The BigBang Team (Endless Frontier)*

    > 出题者 / 批评者 / 元批评者三角合成可验证难题，约一万条样本更新权重；训练时自迭代 + 评价器校准，证据来自团队技术报告。

47. **Towards end-to-end automation of AI research.** Nature 651:914-919, 2026. [paper](https://www.nature.com/articles/s41586-026-10265-5)

    *Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha*

    > The AI Scientist 路线在 Nature 上的正式发表：从想法到论文与评审的端到端自动化。

48. **Why LLMs Aren't Scientists Yet: Lessons from Four Autonomous Research Attempts.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.03315)

    *Dhruv Trehan, Paras Chopra*

    > 四次自主研究尝试总结出的 6 类失败模式（训练数据默认偏置、实现漂移、记忆退化、过度乐观等）。

49. **Learning to Discover at Test Time.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.16175)

    *Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, Yu Sun*

    > 测试时发现：让模型在推理时对开放问题持续搜索与学习。

50. **Meta Context Engineering via Agentic Skill Evolution.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.21557)

    *Haoran Ye, Xuning He, Vincent Arak, Haonan Dong, Guojie Song*

    > 双层优化：外层演化技能（上下文管理机制），内层优化任务上下文。

51. **Hyperagents.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.19461)

    *Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, Tatiana Shavrina*

    > 引入元代理控制如何修改任务代理。

52. **Meta-Harness: End-to-End Optimization of Model Harnesses.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.28052)

    *Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn*

    > 用 coding agent 优化 harness 代码本身，输出 Pareto 前沿上的 harness 候选。

53. **Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.25850)

    *Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Zhiheng Xi, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui, Yu-Gang Jiang*

    > 以可观测性为核心：组件 / 经验 / 决策三层可观测，每次编辑都是可证伪的文件级声明。

54. **Continual Harness: Online Adaptation for Self-Improving Foundation Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.09998)

    *Seth Karten, Joel Zhang, Tersoo Upaa, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, Kiran Vodrahalli*

    > 长程游戏中同时更新 harness 与蒸馏策略模型。

55. **Epistemic Uncertainty for Test-Time Discovery.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.11328)

    *Kainat Riaz, Muhammad Ahmed Mohsin, Ahsan Bilal, Muhammad Umer, Ayesha Mohsin, Aqib Riaz, Ali Subhan, John M. Cioffi*

    > 用认知不确定性引导测试时发现的搜索方向。

56. **⭐SkillOpt: Executive Strategy for Self-Evolving Agent Skills.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.23904) [code](https://aka.ms/skillopt)

    *Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo*

    > 把 skill.md 当冻结 agent 的外部可训练状态：有界编辑 + held-out 验证门 + 拒绝编辑缓冲 + epoch 慢更新；52/52 cells 最优或并列。

57. **DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.24539)

    *Lirong Che, Yuzhe yang, Peiwen lin, Chuang wang, Xueqian wang, Jian su*

    > 用人类示范补充稀疏反馈下的 harness 演化。

58. **ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.26340)

    *Rui Meng, Bhavana Dalvi Mishra, Jiefeng Chen, Chun-Liang Li, Palash Goyal, Mihir Parmar, Yiwen Song, Yale Song, Rajarishi Sinha, Parthasarathy Ranganathan, Burak Gokturk, Jinsung Yoon, Tomas Pfister*

    > 以证据链（chain-of-evidence）组织自主研究，面向人类水平的科研自动化。

59. **SIA: Self Improving AI with Harness & Weight Updates.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.27276)

    *Prannay Hebbar, Yogendra Manawat, Samuel Verboomen, Alesia Ivanova, Selvam Palanimalai, Kunal Bhatia, Vignesh Baskaran*

    > Feedback-Agent 决定本轮更新 harness 还是模型权重的早期尝试。

60. **You Live More Than Once: Towards Hierarchical Skill Meta-Evolving.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.28390)

    *Xujun Li, Kehan Zheng, Mingyuan Zhao, Yize Geng, Jinfeng Zhou, Qi Zhu, Fei Mi, Lifeng Shang, Minlie Huang, Hongning Wang*

    > 分层技能元进化：从执行轨迹学出“怎样生成与修改技能”的元技能并反过来整理技能库，MineDojo 0.700→0.856，底层权重不变。

61. **Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.30621)

    *Minhua Lin, Juncheng Wu, Zijun Wang, Zhan Shi, Yisi Sang, Bing He, Zewen Liu, Tianxin Wei, Zongyu Wu, Zhiwei Zhang, Dakuo Wang, Xiang Zhang, Benoit Dumoulin, Cihang Xie, Yuyin Zhou, Suhang Wang, Hanqing Lu*

    > 9B 到 Opus 的模型写 harness 的能力相近，但利用 harness 的能力非单调；模型智能仍是核心。

62. **When AI builds itself: our progress toward recursive self-improvement, and its implications.** Anthropic Institute, 2026. [paper](https://www.anthropic.com/institute/recursive-self-improvement)

    *Anthropic*

    > Anthropic 对递归自我改进的路线判断：代码建议 → 编程智能体自改代码 → AI 参与设计与训练后继系统；具身智能可能紧随，但物理制造、实验周期与部署是新的速度瓶颈。

63. **Self-Harness: Harnesses That Improve Themselves.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.09498)

    *Hangfan Zhang, Shao Zhang, Kangcong Li, Chen Zhang, Yang Chen, Yiqun Zhang, Lei Bai, Shuyue Hu*

    > weakness mining → bounded harness proposal → held-in/held-out 双重回归验证的自改进循环。

64. **Autodata: An agentic data scientist to create high quality synthetic data.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.25996)

    *Ilia Kulikov, Chenxi Whitehouse, Tianhao Wu, Yixin Nie, Swarnadeep Saha, Eryk Helenowski, Weizhe Yuan, Olga Golovneva, Jack Lanchantin, Yoram Bachrach, Jakob Foerster, Xian Li, Han Fang, Sainbayar Sukhbaatar, Jason Weston*

    > 作为“数据科学家”的 agent，自动生成高质量合成数据。

65. **SkillOpt-Lite: Better and Faster Agent Self-evolution via One Line of Vibe.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.03451) [code](https://github.com/EvolvingLMMs-Lab/SkillOpt-Lite)

    *Yifei Shen, Bo Li, Xinjie Zhang*

    > 零阶优化视角的最小技能优化流水线，推广到 HarnessOpt。

66. **Anchored Self-Play for Code Repair.** ICML 2026, 2026. [paper](https://arxiv.org/abs/2607.03523)

    *Caroline Choi, Zeyneb Kaya, Shirley Wu, Tengyu Ma, Tatsunori Hashimoto, Ludwig Schmidt*

    > 带锚点的自博弈代码修复：出题者与修复者共同演化，锚定避免漂移（ICML 2026）。

67. **Harness Engineering for Self-Improvement.** Lil'Log, 2026. [paper](https://lilianweng.github.io/posts/2026-07-04-harness/) [code](https://lilianweng.github.io/posts/2026-07-04-harness/)

    *Lilian Weng*

    > 定义 Harness 三大模式（工作流自动化 / 文件系统即记忆 / 子代理），提出优化对象阶梯 prompt→context→workflow→harness code→optimizer code，列出 RSI 的 7 个未解挑战。

68. **Recursive Harness Self-Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.15524)

    *Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Matei Zaharia, Yujin Tang*

    > harness 作为 prompt 级 agent loop 规范，用配对反馈迭代精炼。

69. **GPT-6 未必能当好机器人的大脑，却可能帮王兴兴加速 RobotRSI.** WeChat 公众号 具身纪元, 2026. [paper](https://mp.weixin.qq.com/s/DTj1be0CGhwcvaFh2WI0HA)

    *Marilyn Liu (具身纪元)*

    > 提出 Robot RSI 两条轴线：改进环节（部署时自演化 / 训练时自迭代 / 自我评估 / 自动研究）× 人的参与程度（in-the-loop / on-the-loop / closed loop）；判断前沿 LLM 更可能先成为 Robot RSI 的认知中枢而非末端控制器。

70. **A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference.** Machine Intelligence Research, 2026. [paper](https://arxiv.org/abs/2609.01679)

    *Shuaicheng Niu, Guohao Chen, Yaofo Chen, Zhiquan Wen, Jinwu Hu, Zeshuai Deng, Deyu Chen, Shuhai Zhang, Renjie Chen, Zihao Lian, Shoukai Xu, Gang Dai, Yunbei Zhang, Wei Luo, Yifan Zhang, Mingkui Tan, Cheng Deng*

    > 统一测试时适应/学习/扩展的反馈驱动 TTI 视角，覆盖机器人。

71. **SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams.** arXiv, 2026. [paper](https://arxiv.org/abs/2609.02217)

    *Ao Yan, Xin Zhang, Jiawei Du, Joey Tianyi Zhou*

    > 把复用单元定义为'过程族'，局部技能聚合为去实例化的全局先验，提交门保证不退化。

### [Agent + Robot 总览 | Agent + Robot Overview](#论文清单)

检索关键词：`Agentic Robotics / Embodied Agent / LLM Robot Agent / Physical AI Agent`　代表工作：AgenticLab, Agentic Robot, ManiAgent　（10 篇）

1. **LLM+P: Empowering Large Language Models with Optimal Planning Proficiency.** arXiv, 2023. [paper](https://arxiv.org/abs/2304.11477)

    *Bo Liu, Yuqian Jiang, Xiaohan Zhang, Qiang Liu, Shiqi Zhang, Joydeep Biswas, Peter Stone*

    > LLM 把问题翻译成 PDDL，交给经典规划器求解；AgenticLab 等规划语言接口的先驱。

2. **RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.** CoRL 2023, 2023. [paper](https://arxiv.org/abs/2307.15818) [code](https://robotics-transformer2.github.io)

    *Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan, Kehang Han, Karol Hausman, Alexander Herzog, Jasmine Hsu, Brian Ichter, Alex Irpan, Nikhil Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal, Lisa Lee, Tsang-Wei Edward Lee, Sergey Levine, Yao Lu, Henryk Michalewski, Igor Mordatch, Karl Pertsch, Kanishka Rao, Krista Reymann, Michael Ryoo, Grecia Salazar, Pannag Sanketi, Pierre Sermanet, Jaspiar Singh, Anikait Singh, Radu Soricut, Huong Tran, Vincent Vanhoucke, Quan Vuong, Ayzaan Wahid, Stefan Welker, Paul Wohlhart, Jialin Wu, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Tianhe Yu, Brianna Zitkovich*

    > VLA 的起点：把 VLM 的网络知识迁移到机器人动作；文章将其作为 2023-2024 年机器人吃到 VLM 红利的代表。

3. **⭐Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.23450) [code](https://agentic-robot.github.io)

    *Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue Yan, Dingjie Song, Yinuo Liu, Yuting Li, Yu Zhang, Pan Zhou, Hechang Chen, Lichao Sun*

    > 脑启发框架：Standardized Action Procedure 协调推理模型 / VLA 执行器 / 时序验证器，LIBERO 79.6%。

4. **PhysiAgent: An Embodied Agent Framework in Physical World.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.24524)

    *Zhihao Wang, Jianxiong Li, Jinliang Zheng, Wencong Zhang, Dongxiu Liu, Yinan Zheng, Haoyi Niu, Junzhi Yu, Xianyuan Zhan*

    > VLM 根据 VLA 实时熟练度反馈组织 monitor / memory / reflection 组件。

5. **⭐ManiAgent: An Agentic Framework for General Robotic Manipulation.** arXiv, 2025. [paper](https://arxiv.org/abs/2510.11660) [code](https://yi-yang929.github.io/ManiAgent/)

    *Yi Yang, Kefan Gu, Yuqing Wen, Hebei Li, Yucheng Zhao, Tiancai Wang, Xudong Liu*

    > 多 agent 感知-分解-动作生成，SimplerEnv 86.8%，可为 VLA 生成训练数据。

6. **⭐PLanAR: Planning-Language-Grounded Agentic Reasoning for Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.01662) [code](https://agentic1ab.github.io/)

    *Pengyuan Guo, Zhonghao Mai, Zhengtong Xu, Kaidi Zhang, Quan Khanh Luu, Heng Zhang, Zichen Miao, Arash Ajoudani, Zachary Kingston, Qiang Qiu, Yu She*

    > Purdue 真机 agent 平台：以规划语言（谓词/动作 schema）定义 VLM 推理空间，逐步验证符号效果并重规划。

7. **Agentic AI for Robot Control: Flexible but still Fragile.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.13081)

    *Oscar Lima, Marc Vinci, Martin Günther, Marian Renz, Alexander Sung, Sebastian Stock, Johannes Brust, Lennart Niecksch, Zongyao Yi, Felix Igelbrink, Benjamin Kisliuk, Martin Atzmueller, Joachim Hertzberg*

    > 两台真机上的规划-执行循环：迁移只需改系统 prompt，但非确定性与 prompt 敏感性显著。

8. **VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.07723) [code](https://chicychen.github.io/VoLo/)

    *Siyi Chen, Hugo Hadfield, Alex Zook, Mikaela Angelina Uy, Chan Hee Song, Erwin Coumans, Xuning Yang, Faisal Ladhak, Qing Qu, Stan Birchfield, Jonathan Tremblay, Valts Blukis*

    > NVIDIA Physical Orchestration：VLM 把 VLA/WAM 当作可中断工具中途干预。

9. **Guava: An Effective and Universal Harness for Embodied Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.18363)

    *Haowen Liu, Xirui Li, Shaoxiong Yao, Peng Shi, Tianyi Zhou, Jia-Bin Huang, Furong Huang, Jiayuan Mao*

    > 系统探索 harness 设计空间：迭代感知-推理-动作循环、语义动作抽象、多模态观测三要素；蒸馏进 4B 模型。

10. **HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.23565)

    *Xiaolin Zhou, Liu Liu, Tingyang Xiao, Wei Feng, Fa Fu, Xinrui Meng, Xinjie Wang, Jialiang Han, Boyang Yu, Yun Du, Wei Sui, Zhizhong Su*

    > Embodied AgentOS + 3D 空间记忆 + 具身技能三层真机框架。

### [Coding Agent 控机器人 | Coding Agents Control Robots](#论文清单)

检索关键词：`Code-as-Policy robotics / robot coding agent / coding agents robot manipulation`　代表工作：Code as Policies, CaP-X, RHO, ASPIRE　（20 篇）

1. **⭐Code as Policies: Language Model Programs for Embodied Control.** arXiv, 2022. [paper](https://arxiv.org/abs/2209.07753) [code](https://code-as-policies.github.io)

    *Jacky Liang, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, Brian Ichter, Pete Florence, Andy Zeng*

    > 首次系统提出 Code-as-Policy：LLM 生成处理感知、调用控制原语、可表达反应式与航点式策略的程序。

2. **⭐MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation.** arXiv, 2024. [paper](https://arxiv.org/abs/2411.17636)

    *Harsh Singh, Rocktim Jyoti Das, Mingfei Han, Preslav Nakov, Ivan Laptev*

    > Planner / Coder / Supervisor 多 LLM agent 零样本操作，每步环境观测驱动重规划。

3. **⭐Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.18597)

    *Yuan Meng, Zhenguo Sun, Max Fest, Xukun Li, Zhenshan Bing, Alois Knoll*

    > 人在环的终身代码生成：把纠正编码为可复用技能 + 外部记忆 RAG，解决 20+ 原语的超长程任务。

4. **Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning.** NeurIPS 2025 Spotlight, 2025. [paper](https://arxiv.org/abs/2510.21302)

    *Sanghyun Ahn, Wonje Choi, Junyong Lee, Jinwoo Park, Honguk Woo*

    > NeurIPS 2025 Spotlight：符号验证 + 交互式验证代码，成功率比 CaP +46.2%。

5. **AtomBridge: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.09430)

    *Yiwen Pang, Bo Zhou, Changjin Li, Xuanhao Wang, Shengxiang Xu, Deng-Bao Wang, Peng Cheng, Shimin Di, Jingkuan Song, Min-Ling Zhang*

    > 在原子技能边界由 LLM 生成过渡动作代码，8 步任务成功率 +10-25%。

6. **⭐CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.22435)

    *Letian Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Dantong Niu, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi "Jim" Fan*

    > CaP-Gym / CaP-Bench / CaP-Agent0 / CaP-RL 四件套；抽象降低时性能下降，可用 agentic test-time compute 弥补；RL with verifiable reward 可 sim2real。

7. **Nautilus: From One Prompt to Plug-and-Play Robot Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.11665)

    *Yufeng Jin, Jianfei Guo, Xiaogang Jia, Yu Deng, Zechu Li, Han Liu, Weiran Liao, Vignesh Prasad, Mathias Franzius, Gerhard Neumann, Georgia Chalvatzaki*

    > 从一句 prompt 生成复现/评估/微调/部署工作流的开源研究 harness。

8. **HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.08610)

    *Zechu Li, Yufeng Jin, Xiaoyang Liu, Puze Liu, Vignesh Prasad, Carlo D'Eramo, Georgia Chalvatzaki*

    > 把机器人 RL 自动化视为 harness 工程问题：从环境搭建到训练的分阶段 agent 流水线。

9. **⭐RHO: Your Coding Agent is Secretly a Roboticist.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.16458) [code](https://rho-robotics.github.io)

    *Karim Elmaaroufi, Justin Svegliato, Sarunas Kalade, Graham Schelle, Sanjit A. Seshia, Matei Zaharia*

    > Robotics Harness Optimization：coding agent 在训练时搜索多文件策略仓库（Repositories-as-Policies），部署时单轮执行，LIBERO-PRO 45% vs π0.5 12.8%。

10. **Playful Agentic Robot Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19419) [code](https://playful-rats.github.io/)

    *Junyi Zhang, Jiaxin Ge, Hanjun Yoo, Letian Fu, Zihan Yang, Yaowei Liu, Raj Saravanan, Shaofeng Yin, Justin Yu, Dantong Niu, Zirui Wang, Roei Herzig, Ken Goldberg, Yutong Bai, David M. Chan, Ion Stoica, Angjoo Kanazawa, Jiahui Lei, Haiwen Feng, Trevor Darrell*

    > 自主'玩耍'阶段发现技能并蒸馏进代码技能库，LIBERO-PRO 比 CaP-Agent0 +20.6pp。

11. **⭐ENPIRE: Agentic Robot Policy Self-Improvement in the Real World.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19980)

    *Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi*

    > coding agent 的真机 harness：EN（自动 reset+验证）/ PI / R（多机并行 rollout）/ E（读日志改算法与基础设施），自主训练策略至 99% 成功。

12. **⭐ASPIRE: Agentic /Skills Discovery for Robotics.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.00272) [code](https://research.nvidia.com/labs/gear/aspire/)

    *Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi "Jim" Fan, Guanzhi Wang*

    > NVIDIA GEAR：执行引擎 + 技能库 + 演化搜索的持续学习系统，技能跨任务/仿真/真机/本体持久化，LIBERO-Pro Long 零样本 31% vs 4%。

13. **Contract-Grounded Behavior Tree Synthesis via Coding Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.12220)

    *Jonathan Salfity, Robert Blake Anderson, Mitch Pryor*

    > coding agent 先向机器人侧 MCP server 拉取技能契约再合成行为树。

14. **MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.22832) [code](https://github.com/sygkounas/MEMENTO)

    *Alkis Sygkounas, Victor Aregbede, Amy Loutfi, Andreas Persson*

    > 记忆引导的单精英模因式 code-as-policy 演化，先演化 rollout 评估器。

15. **A Few Words Go a Long Way: Language Guided Robot Policy Synthesis.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.23784) [code](https://robo-architect.github.io/)

    *Daphne Chen, Archit Ritesh Jain, Eric Goossen, Emma Romig, Michael Murray, Nick Walker, Maya Cakmak*

    > 把策略获取视为交互式程序合成，人类语言纠正蒸馏进持久技能库。

16. **You Don't Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.07555)

    *Hang Yu*

    > 策略改进的控制平面：证据分级技能库、commit 键控崩溃恢复、签名验证器。

17. **Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.09410)

    *Yunhao Zhao, Zhenyang Ni, Haoyang Chen, Ruohan Zhang, Qi Zhu*

    > 权重学技能、代码管记忆：coding agent 用启发式学习迭代记忆管理系统，RoboMemArena 任务成功 41.3%→60.1%。

18. **Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.18227)

    *Shuangyu Xie, Kaiyuan Chen, Ken Goldberg*

    > Goldberg 组：Claude Code 无示范写出 Push-T 算法解，100% 成功且比扩散策略少 46% 步数。

19. **PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.21031) [code](https://physcap.github.io)

    *Chen-Yu Lin, Jing-Wen Chen, Hsueh-En Chang, Hung-An Chen, Sheng-Hsun Chang, Chi-Pin Huang, Fu-En Yang, Min-Hung Chen, Yi-Ting Chen, Yu-Chiang Frank Wang, Shao-Hua Sun*

    > 物理信息驱动的主动探索层：从本体感知估计质量/刚度，Planner+Prioritizer 决定何时探索。

20. **RoboCurve：GPT-6 Astra 直接控制机器人.** 知乎专栏, 2026. [paper](https://zhuanlan.zhihu.com/p/208031326825455257)

    *罗清雨 (知乎)*

    > RoboCurve 第三方测试：GPT-6 Astra 以 EEF waypoint 工具调用控制 YAM 双臂，block→bowl 19/20（2.5 min，2.1K tokens）而精密插入 10%；文章提出“接一个 flow head”的双系统设想。本仓库 notes/44 据此给出 Agent-as-Teleoperator 数据引擎方案。

### [OpenClaw / ROS 生态 | OpenClaw / ROS](#论文清单)

检索关键词：`OpenClaw robotics / ROS2 agentic robot / MCP robotics`　代表工作：ROSClaw, OpenClawPi, AgentRob　（10 篇）

1. **ROSBag MCP Server: Analyzing Robot Data with LLMs for Agentic Embodied AI Applications.** arXiv, 2025. [paper](https://arxiv.org/abs/2511.03497) [code](https://github.com/binabik-ai/mcp-rosbags)

    *Lei Fu, Sahar Salimpour, Leonardo Militano, Harry Edelman, Jorge Peña Queralta, Giovanni Toffetti*

    > 用 MCP 让 LLM 分析 ROS/ROS 2 bag 数据。

2. **⭐AgentRob: From Virtual Forum Agents to Hijacked Physical Robots.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.13591)

    *Wenrui Liu, Yaxuan Wang, Xun Zhang, Yanshu Wang, Jiashen Wei, Yifan Xiang, Yuhang Wang, Mingshen Ye, Elsie Dai, Zhiqi Liu, Yingjie Xu, Xinyang Chen, Hengzhe Sun, Jiyu Shen, Jingjing He, Tong Yang*

    > 通过 MCP 把论坛 agent 与 Unitree Go2/G1 相连，展示论坛介导的多 agent 机器人编排（及被劫持风险）。

3. **⭐ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.26997)

    *Irvin Steve Cardenas, Marcus Anthony Arnett, Natalie Catherine Yeo, Lucky Sah, Jong-Hoon Kim*

    > OpenClaw runtime + ROS 2 的模型无关执行层：能力发现、观测归一、安全包络内的预执行验证、审计日志；发现不同前沿模型越权动作率差 3.4-4.8 倍。

4. **⭐OpenClawPi: AgileX Robotics Skill Set Library for OpenClaw.** Open Robotics Discourse / Hackster, 2026. [paper](https://discourse.openrobotics.org/t/rapid-deployment-of-openclaw-and-graspgen-crawling-system/53764) [code](https://discourse.openrobotics.org/t/rapid-deployment-of-openclaw-and-graspgen-crawling-system/53764)

    *AgileX Robotics*

    > 松灵机器人（AgileX）面向 OpenClaw 的模块化机器人技能库，覆盖机械臂控制、抓取等场景。

5. **OpenGo: An OpenClaw-Based Robotic Dog with Real-Time Skill Switching.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.01708)

    *Hanbing Li, Xuewei Cao, Zhiwen Zeng, Yuhan Wu, Yanyong Zhang, Yan Xia*

    > OpenClaw 驱动的 Go2 机器狗：技能库 + 调度器 + 基于反馈的自学习，飞书自然语言交互。

6. **⭐ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.04664) [code](https://www.rosclaw.io/)

    *Rongfeng Zhao, Xuanhao Zhang, Zhaochen Guo, Xiang Shao, Zhongpan Zhu, Bin He, Jie Chen*

    > 同名工作：e-URDF 物理约束 + sim-real 拓扑映射，统一 VLM 控制器串起采集、训练与执行。

7. **SpaceMind: A Modular and Self-Evolving Embodied Vision-Language Agent Framework for Autonomous On-orbit Servicing.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.14399) [code](https://github.com/wuaodi/SpaceMind)

    *Aodi Wu, Haodong Han, Xubo Luo, Ruisuo Wang, Shan He, Xue Wan*

    > MCP 工具 + 技能自演化的在轨服务 VLM agent，单次失败即恢复。

8. **Long-Term Memory for VLA-based Agents in Open-World Task Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.15671)

    *Xu Huang, Weixin Mao, Yinhao Li, Hua Chen, Jiabao Zhao*

    > 化学实验室双层记忆 + MCP 子 agent 编排 + 异步推理。

9. **Contract-Grounded Behavior Tree Synthesis via Coding Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.12220)

    *Jonathan Salfity, Robert Blake Anderson, Mitch Pryor*

    > coding agent 先向机器人侧 MCP server 拉取技能契约再合成行为树。

10. **⭐Previewing the Model Hardware Standard (MHS).** Anthropic Research Preview, 2026. [paper](https://www.anthropic.com/news/model-hardware-standard-research-preview) [code](https://www.anthropic.com/news/model-hardware-standard-research-preview)

    *Anthropic*

    > Anthropic 2026-08-27 研究预览：让 agent 通过统一规范发现、操作、排障真实设备（显微镜、液体处理器、机械臂），被称为硬件版 MCP。

### [长程任务 | Long-Horizon Tasks](#论文清单)

检索关键词：`long-horizon robotic manipulation agent / hierarchical robot agent`　代表工作：RoboClaw, H-WM, Agentic Robot, REMAC　（11 篇）

1. **⭐REMAC: Self-Reflective and Self-Evolving Multi-Agent Collaboration for Long-Horizon Robot Manipulation.** arXiv, 2025. [paper](https://arxiv.org/abs/2503.22122)

    *Puzhen Yuan, Angyuan Ma, Yunchao Yao, Huaxiu Yao, Masayoshi Tomizuka, Mingyu Ding*

    > 多机器人长程规划：前置/后置条件检查的自反思 + 场景推理的自进化，成功率 +40%，效率 +52.7%。

2. **⭐Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.23450) [code](https://agentic-robot.github.io)

    *Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue Yan, Dingjie Song, Yinuo Liu, Yuting Li, Yu Zhang, Pan Zhou, Hechang Chen, Lichao Sun*

    > 脑启发框架：Standardized Action Procedure 协调推理模型 / VLA 执行器 / 时序验证器，LIBERO 79.6%。

3. **AtomBridge: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.09430)

    *Yiwen Pang, Bo Zhou, Changjin Li, Xuanhao Wang, Shengxiang Xu, Deng-Bao Wang, Peng Cheng, Shimin Di, Jingkuan Song, Min-Ling Zhang*

    > 在原子技能边界由 LLM 生成过渡动作代码，8 步任务成功率 +10-25%。

4. **⭐H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.11291)

    *Jinbang Huang, Wenyuan Chen, Zhiyuan Li, Oscar Pang, Xiao Hu, Lingfeng Zhang, Yuanzhao Hu, Zhanguang Zhang, Mark Coates, Tongtong Cao, Xingyue Quan, Yingxue Zhang*

    > 分层世界模型：高层逻辑世界模型 + 低层视觉世界模型联合预测，为 VLA 提供稳定中间引导。

5. **Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.09513)

    *Honghui Wang, Zhi Jing, Jicong Ao, Shiji Song, Xuelong Li, Gao Huang, Chenjia Bai*

    > 非马尔可夫保险箱基准 + VQ 离散本体历史记忆。

6. **⭐RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.11558) [code](https://github.com/RoboClaw-Robotics/RoboClaw)

    *Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang, Sukai Wang, Kongtao Hu, Minhui Yu, Bowen Jiang, Zhan Su, Jiayao Ma, Xin He, Yongjian Shen, Yang Yang, Guanghui Ren, Maoqing Yao, Wenhao Wang, Yao Mu*

    > 统一采集-学习-部署的 VLM 控制器；Entangled Action Pairs 把正向技能与逆向恢复绑定实现自复位采数据，成功率 +25%，人工时间 -53.7%。

7. **VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.07723) [code](https://chicychen.github.io/VoLo/)

    *Siyi Chen, Hugo Hadfield, Alex Zook, Mikaela Angelina Uy, Chan Hee Song, Erwin Coumans, Xuning Yang, Faisal Ladhak, Qing Qu, Stan Birchfield, Jonathan Tremblay, Valts Blukis*

    > NVIDIA Physical Orchestration：VLM 把 VLA/WAM 当作可中断工具中途干预。

8. **Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.05377)

    *Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai, Jing Xiong, Ganlin Yang, Jinliang Zheng, Jiafei Cao, Xueyuan Wei, Jiangmiao Pang, Yuan Shen, Tai Wang*

    > 32 个规范技能原语的双向对齐规划接口，附推理期 harness engineering。

9. **Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models.** IROS 2026, 2026. [paper](https://arxiv.org/abs/2607.16506)

    *Yuhan Liu, Xinyu Zhang, Litao Liu, Abdeslam Boularias*

    > 用下游成功概率（foresight value）塑形子任务交接状态。

10. **RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.18060)

    *Jinbang Huang, Yuanzhao Hu, Zhiyuan Li, Ran Qi, Yixin Xiao, Zhanguang Zhang, Mark Coates, Tongtong Cao, Yingxue Zhang*

    > 多模态执行记忆刻画异构策略能力边界，Memory Bridge 把机器人引导到下一策略的分布内区域。

11. **Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.16889)

    *Bingxin Xu, Yuzhang Shang, Emilio Ferrara*

    > 以子任务为探索单元（成本 T·K 而非 T^K），转移感知记忆治理 VLA 的进入条件。

### [机器人记忆 | Robot Memory](#论文清单)

检索关键词：`robot memory / memory-augmented VLA / episodic memory robotics / history-dependent manipulation`　代表工作：RoboMME, PonderPounce, ViReSkill　（21 篇）

1. **Generative Agents: Interactive Simulacra of Human Behavior.** UIST 2023, 2023. [paper](https://arxiv.org/abs/2304.03442)

    *Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein*

    > 记忆流 + 检索（新近性 / 重要性 / 相关性）+ 反思 + 规划的沙盒 agent，是 Robot Memory 主线常引的记忆架构。

2. **⭐ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.24219)

    *Tomoyuki Kagaya, Subramanian Lakshmi, Anbang Ye, Thong Jing Yuan, Jayashree Karlekar, Sugiri Pranata, Natsuki Murakami, Akira Kinose, Yang You*

    > 失败时视觉接地重规划，成功后把计划存入技能记忆下次直接复用，无需再调 LLM。

3. **⭐RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration.** arXiv, 2025. [paper](https://arxiv.org/abs/2510.26536) [code](https://flagopen.github.io/RoboOS/)

    *Huajie Tan, Cheng Chi, Xiansheng Chen, Yuheng Ji, Zhongxia Zhao, Xiaoshuai Hao, Yaoxu Lyu, Mingyu Cao, Junkai Zhao, Huaihai Lyu, Enshen Zhou, Ning Chen, Yankai Fu, Cheng Peng, Wei Guo, Dong Liang, Zhuo Chen, Mengsi Lyu, Chenrui He, Yulong Ao, Yonghua Lin, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang*

    > Spatio-Temporal-Embodiment Memory 统一多机器人终身协作的共享记忆。

4. **MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.20577)

    *Baiqing Wang, Helei Cui, Bo Zhang, Xiaolong Zheng, Bin Guo, Zhiwen Yu*

    > 相似任务记忆化复用多机器人计划。

5. **⭐RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies.** ICML 2026, 2026. [paper](https://arxiv.org/abs/2603.04639) [code](https://robomme.github.io)

    *Yinpei Dai, Hongze Fu, Jayjun Lee, Yuejiang Liu, Haoran Zhang, Jianing Yang, Chelsea Finn, Nima Fazeli, Joyce Chai*

    > ICML 2026。16 个任务覆盖时间/空间/物体/程序四类记忆，14 个 π0.5 记忆变体；记忆表示的有效性高度任务依赖。

6. **Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.09513)

    *Honghui Wang, Zhi Jing, Jicong Ao, Shiji Song, Xuelong Li, Gao Huang, Chenjia Bai*

    > 非马尔可夫保险箱基准 + VQ 离散本体历史记忆。

7. **Long-Term Memory for VLA-based Agents in Open-World Task Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.15671)

    *Xu Huang, Weixin Mao, Yinhao Li, Hua Chen, Jiabao Zhao*

    > 化学实验室双层记忆 + MCP 子 agent 编排 + 异步推理。

8. **⭐RoboMME-Interference: Benchmarking Robot Memory Under Interference.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.22338) [code](https://robotmemorybench.com)

    *Soumil Rathi*

    > 跨会话干扰基准：感知型记忆随无关会话累积而衰减，检索步骤可恢复。

9. **HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.23565)

    *Xiaolin Zhou, Liu Liu, Tingyang Xiao, Wei Feng, Fa Fu, Xinrui Meng, Xinjie Wang, Jialiang Han, Boyang Yu, Yun Du, Wei Sui, Zhizhong Su*

    > Embodied AgentOS + 3D 空间记忆 + 具身技能三层真机框架。

10. **Analytic Concept-Centric Memory for Agentic Embodied Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.29774)

    *Mingyang Sun, Xiujian Liang, Jiude Wei, Qichen He, Donglin Wang, Cewu Lu, Jianhua Sun*

    > 以部件/模板/位姿/affordance 组织的结构化概念记忆，连接转移记忆与技能记忆。

11. **NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.06678)

    *Ziye Wang, Modi Shi, Chaojun Ni, Jiazhi Yang, Mengdi Li, Zhizhong Su, Tianwei Lin, Hongyang Li*

    > 复用 VLA 自身视觉编码器把每帧压成一个记忆 token，成功率 32.4%→84.0%。

12. **Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.07608) [code](https://github.com/quhongyu/LaMem-VLA)

    *Hongyu Qu, Jianzhe Gao, Xiaobin Hu, Shaohuan Yang, Xinlei Yu, Rui Yan, Wenguan Wang, Xiangbo Shu, Shuicheng Yan*

    > 短/长期记忆库在 VLA 原生潜空间中交织。

13. **RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.18060)

    *Jinbang Huang, Yuanzhao Hu, Zhiyuan Li, Ran Qi, Yixin Xiao, Zhanguang Zhang, Mark Coates, Tongtong Cao, Yingxue Zhang*

    > 多模态执行记忆刻画异构策略能力边界，Memory Bridge 把机器人引导到下一策略的分布内区域。

14. **SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.05970)

    *Changyuan Wang, Chubin Zhang, Zhenyu Wu, Runhao Li, Angyuan Ma, Ke Chao, Yinan Liang, Xiuwei Xu, Ziwei Wang, Yansong Tang, Jiwen Lu*

    > MoE 门控隐式切分技能原语并存入情景记忆库。

15. **OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies.** ECCV 2026 Workshop, 2026. [paper](https://arxiv.org/abs/2608.08749)

    *Zhongxi Chen, Shenqi Zong*

    > 价值引导的记忆模块，用在线 rollout 结果学习该保留哪些经验。

16. **Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.09410)

    *Yunhao Zhao, Zhenyang Ni, Haoyang Chen, Ruohan Zhang, Qi Zhu*

    > 权重学技能、代码管记忆：coding agent 用启发式学习迭代记忆管理系统，RoboMemArena 任务成功 41.3%→60.1%。

17. **Remember Smarter: Visual History Compressor and Hyperbolic Experience Space for Robotic Memory.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.15269)

    *Dai Zhou, Jiexi Yan, Tong Li, Yuxuan Wang, Cheng Deng*

    > Mamba 视觉历史压缩 + 双曲经验空间，LIBERO-Plus 53.6%→70.6%。

18. **Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.16889)

    *Bingxin Xu, Yuzhang Shang, Emilio Ferrara*

    > 以子任务为探索单元（成本 T·K 而非 T^K），转移感知记忆治理 VLA 的进入条件。

19. **⭐PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.24115) [code](https://worv-ai.github.io/ponderpounce/)

    *Suhwan Choi, Jaeyoon Jung, Sungkyung Kim, Yunsung Lee, Youngjae Yu*

    > 复用 MLLM 原生因果上下文作为 episode 记忆：Ponder(System2) 异步向 Pounce(System1 VLA) 发送最新认知 token；RoboMME 60.83% vs π0.5 17.93%。

20. **Memory Anchors for Continual Robot Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.26545) [code](https://robot-adaptation.github.io/MemoryAnchors)

    *Maximilian Du, Zhanyi Sun, Chen Xu, Paarth Shah, Masha Itkina, Shuran Song*

    > 持续学习中 10% 的关键锚点经验决定是否灾难性遗忘。

21. **AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.29537)

    *Hongbo Gao, Zeyu Ni, Xin Wen, Siyu Xu, Ruifeng Li*

    > 成就接地记忆：只有物理证据验证子目标后才推进进度指针；可靠记忆取决于状态更新纪律而非容量。

### [反思与纠错 | Reflection / Failure Correction](#论文清单)

检索关键词：`robot self-reflection / closed-loop replanning robot / failure reflection robotics`　代表工作：REMAC, AgenticLab, ASPIRE　（15 篇）

1. **Reflexion: Language Agents with Verbal Reinforcement Learning.** NeurIPS 2023, 2023. [paper](https://arxiv.org/abs/2303.11366) [code](https://github.com/noahshinn/reflexion)

    *Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao*

    > 部署时的记忆自改进：把测试 / 环境反馈写成反思存进记忆再重试，不更新权重；HumanEval 91%。

2. **Self-Refine: Iterative Refinement with Self-Feedback.** NeurIPS 2023, 2023. [paper](https://arxiv.org/abs/2303.17651)

    *Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, Peter Clark*

    > 同一模型生成 → 自我反馈 → 精炼的迭代，不训练；反思类方法的基线。

3. **⭐REMAC: Self-Reflective and Self-Evolving Multi-Agent Collaboration for Long-Horizon Robot Manipulation.** arXiv, 2025. [paper](https://arxiv.org/abs/2503.22122)

    *Puzhen Yuan, Angyuan Ma, Yunchao Yao, Huaxiu Yao, Masayoshi Tomizuka, Mingyu Ding*

    > 多机器人长程规划：前置/后置条件检查的自反思 + 场景推理的自进化，成功率 +40%，效率 +52.7%。

4. **⭐ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.24219)

    *Tomoyuki Kagaya, Subramanian Lakshmi, Anbang Ye, Thong Jing Yuan, Jayashree Karlekar, Sugiri Pranata, Natsuki Murakami, Akira Kinose, Yang You*

    > 失败时视觉接地重规划，成功后把计划存入技能记忆下次直接复用，无需再调 LLM。

5. **PhysiAgent: An Embodied Agent Framework in Physical World.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.24524)

    *Zhihao Wang, Jianxiong Li, Jinliang Zheng, Wencong Zhang, Dongxiu Liu, Yinan Zheng, Haoyi Niu, Junzhi Yu, Xianyuan Zhan*

    > VLM 根据 VLA 实时熟练度反馈组织 monitor / memory / reflection 组件。

6. **⭐PLanAR: Planning-Language-Grounded Agentic Reasoning for Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.01662) [code](https://agentic1ab.github.io/)

    *Pengyuan Guo, Zhonghao Mai, Zhengtong Xu, Kaidi Zhang, Quan Khanh Luu, Heng Zhang, Zichen Miao, Arash Ajoudani, Zachary Kingston, Qiang Qiu, Yu She*

    > Purdue 真机 agent 平台：以规划语言（谓词/动作 schema）定义 VLM 推理空间，逐步验证符号效果并重规划。

7. **Agentic AI for Robot Control: Flexible but still Fragile.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.13081)

    *Oscar Lima, Marc Vinci, Martin Günther, Marian Renz, Alexander Sung, Sebastian Stock, Johannes Brust, Lennart Niecksch, Zongyao Yi, Felix Igelbrink, Benjamin Kisliuk, Martin Atzmueller, Joachim Hertzberg*

    > 两台真机上的规划-执行循环：迁移只需改系统 prompt，但非确定性与 prompt 敏感性显著。

8. **RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.16444)

    *Yixue Zhang, Kun Wu, Zhi Gao, Zhen Zhao, Pei Ren, Zhiyuan Xu, Fei Liao, Xinhua Wang, Shichao Fan, Di Wu, Qiuxuan Feng, Meng Li, Zhengping Che, Chang Liu, Jian Tang*

    > 多样性驱动 + 自反思物理约束的真实任务生成 agent，18k 轨迹。

9. **Self-adapting Robotic Agents through Online Continual Reinforcement Learning with World Model Feedback.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.04029)

    *Fabian Domberg, Georg Schildbach*

    > DreamerV3 预测残差检测 OOD 并自动触发微调。

10. **⭐From Passive Observer to Active Critic: Reinforcement Learning Elicits Process Reasoning for Robotic Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.15600)

    *Yibin Liu, Yaxing Lyu, Daqi Gao, Zhixuan Liang, Weiliang Tang, Shilong Mu, Xiaokang Yang, Yao Mu*

    > 7B 视频 MLLM 从“观察者”变“批评者”：以初始 / 当前画面锚定过程视频，RL 激励显式 CoT 估计进度与失败位置；RoboFail 失败检测 67%。

11. **PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.27146)

    *Jiayu Yang, Tao Yang, Weijun Li, Xiang Chang, Fei Chao, Changjing Shang, Qiang Shen*

    > 可行性算子 + 动作解释算子 + LLM 反思模块的执行期可靠性框架。

12. **⭐ASPIRE: Agentic /Skills Discovery for Robotics.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.00272) [code](https://research.nvidia.com/labs/gear/aspire/)

    *Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi "Jim" Fan, Guanzhi Wang*

    > NVIDIA GEAR：执行引擎 + 技能库 + 演化搜索的持续学习系统，技能跨任务/仿真/真机/本体持久化，LIBERO-Pro Long 零样本 31% vs 4%。

13. **Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.31200)

    *Tao Chen, Lizheng Liu, Jiaxu Wang, Ziyue Jiang, Ruiqi Tian, JiGuang Huo, Zhongxue Gan*

    > affordance 感知检索 + 场景图约束 + 14 类失败分类的自反思抓取。

14. **⭐Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.08448) [code](https://github.com/RLinf/RPent)

    *Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, Zhengru Fang, Yi Nie, Changxu Wei, Yu Wang, Wenbo Ding, Chao Yu*

    > 把冻结 VLA 暴露为可重试的接触原语，与少量解析原语组合；从执行轨迹学习原语的适用范围而非扩张技能库；LIBERO-Pro +38.6pp。

15. **Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.16590)

    *Xin Ding, Liang Mi, Mingzhe Huang, Zixuan Wang, Chao Zhang, Zixu Hao, Fu Chen, Xiangyu Li, Yikai Zheng, Yaoyu Guo, Weijun Wang, Kun Li, Hao Wu, Yunxin Liu, Ting Cao*

    > 三时间尺度闭环 harness：动作频率治理 / rollout 级 critic-recovery 提议 / 验证门控技能更新；LIBERO-Pro 90.8%，推理加速 11.1x。

### [自进化 | Self-Evolution](#论文清单)

检索关键词：`self-evolving robot agent / lifelong embodied learning / continual robot learning`　代表工作：Arcadia, ASPIRE, PhyAgentOS, Growing with Your Embodied Agent　（21 篇）

1. **⭐Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.18597)

    *Yuan Meng, Zhenguo Sun, Max Fest, Xukun Li, Zhenshan Bing, Alois Knoll*

    > 人在环的终身代码生成：把纠正编码为可复用技能 + 外部记忆 RAG，解决 20+ 原语的超长程任务。

2. **⭐Arcadia: Toward a Full-Lifecycle Framework for Embodied Lifelong Learning.** arXiv, 2025. [paper](https://arxiv.org/abs/2512.00076)

    *Minghe Gao, Juncheng Li, Yuze Lin, Xuqi Liu, Jiaming Ji, Xiaoran Pan, Zihan Xu, Xian Li, Mingjie Li, Wei Ji, Rong Wei, Rui Tang, Qizhou Wang, Kai Shen, Jun Xiao, Qi Wu, Siliang Tang, Yueting Zhuang*

    > 全生命周期闭环：自进化探索 → 生成式场景重建 → 共享具身表征 → sim-from-real 评估与演化。

3. **Self-adapting Robotic Agents through Online Continual Reinforcement Learning with World Model Feedback.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.04029)

    *Fabian Domberg, Georg Schildbach*

    > DreamerV3 预测残差检测 OOD 并自动触发微调。

4. **⭐RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.11558) [code](https://github.com/RoboClaw-Robotics/RoboClaw)

    *Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang, Sukai Wang, Kongtao Hu, Minhui Yu, Bowen Jiang, Zhan Su, Jiayao Ma, Xin He, Yongjian Shen, Yang Yang, Guanghui Ren, Maoqing Yao, Wenhao Wang, Yao Mu*

    > 统一采集-学习-部署的 VLM 控制器；Entangled Action Pairs 把正向技能与逆向恢复绑定实现自复位采数据，成功率 +25%，人工时间 -53.7%。

5. **SpaceMind: A Modular and Self-Evolving Embodied Vision-Language Agent Framework for Autonomous On-orbit Servicing.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.14399) [code](https://github.com/wuaodi/SpaceMind)

    *Aodi Wu, Haodong Han, Xubo Luo, Ruisuo Wang, Shan He, Xue Wan*

    > MCP 工具 + 技能自演化的在轨服务 VLM agent，单次失败即恢复。

6. **⭐SkillOpt: Executive Strategy for Self-Evolving Agent Skills.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.23904) [code](https://aka.ms/skillopt)

    *Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo*

    > 把 skill.md 当冻结 agent 的外部可训练状态：有界编辑 + held-out 验证门 + 拒绝编辑缓冲 + epoch 慢更新；52/52 cells 最优或并列。

7. **VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.05395)

    *Yunhao Yang, Neel P. Bhatt, Kevin Wang, Samuel Tetteh, Zhangyang Wang, Ufuk Topcu*

    > 形式化可验证的自进化技能契约：模型检查反例变成文本梯度，97.2% 规范符合。

8. **Playful Agentic Robot Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19419) [code](https://playful-rats.github.io/)

    *Junyi Zhang, Jiaxin Ge, Hanjun Yoo, Letian Fu, Zihan Yang, Yaowei Liu, Raj Saravanan, Shaofeng Yin, Justin Yu, Dantong Niu, Zirui Wang, Roei Herzig, Ken Goldberg, Yutong Bai, David M. Chan, Ion Stoica, Angjoo Kanazawa, Jiahui Lei, Haiwen Feng, Trevor Darrell*

    > 自主'玩耍'阶段发现技能并蒸馏进代码技能库，LIBERO-PRO 比 CaP-Agent0 +20.6pp。

9. **⭐ENPIRE: Agentic Robot Policy Self-Improvement in the Real World.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19980)

    *Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi*

    > coding agent 的真机 harness：EN（自动 reset+验证）/ PI / R（多机并行 rollout）/ E（读日志改算法与基础设施），自主训练策略至 99% 成功。

10. **⭐ASPIRE: Agentic /Skills Discovery for Robotics.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.00272) [code](https://research.nvidia.com/labs/gear/aspire/)

    *Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi "Jim" Fan, Guanzhi Wang*

    > NVIDIA GEAR：执行引擎 + 技能库 + 演化搜索的持续学习系统，技能跨任务/仿真/真机/本体持久化，LIBERO-Pro Long 零样本 31% vs 4%。

11. **SkillOpt-Lite: Better and Faster Agent Self-evolution via One Line of Vibe.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.03451) [code](https://github.com/EvolvingLMMs-Lab/SkillOpt-Lite)

    *Yifei Shen, Bo Li, Xinjie Zhang*

    > 零阶优化视角的最小技能优化流水线，推广到 HarnessOpt。

12. **⭐PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.16636)

    *Yang Liu, Weixing Chen, Xinshuai Song, Tao Pu, Siwen Mo, Yongjie Bai, Zihao Chen, Qianran Sun, Liruo Zhong, Ying Shen, Liang Lin*

    > 会话为最小调度单元的运行时：State-as-a-File、SessionVerifier 区分执行终止与语义完成、epistemic memory、分层安全；19+ 本体验证。

13. **MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.22832) [code](https://github.com/sygkounas/MEMENTO)

    *Alkis Sygkounas, Victor Aregbede, Amy Loutfi, Andreas Persson*

    > 记忆引导的单精英模因式 code-as-policy 演化，先演化 rollout 评估器。

14. **Self-Evolving Embodied Agents via Skill-Harness Evolution.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.11350)

    *Peidong Wang, Zhiming Ma, Ying Chang, Xufang Luo, Xiaocui Yang, Shi Feng, Yuqing Yang, Dongsheng Li*

    > 冻结模型同时充当规划器和优化器，演化技能与 context-code harness。

15. **Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.16590)

    *Xin Ding, Liang Mi, Mingzhe Huang, Zixuan Wang, Chao Zhang, Zixu Hao, Fu Chen, Xiangyu Li, Yikai Zheng, Yaoyu Guo, Weijun Wang, Kun Li, Hao Wu, Yunxin Liu, Ting Cao*

    > 三时间尺度闭环 harness：动作频率治理 / rollout 级 critic-recovery 提议 / 验证门控技能更新；LIBERO-Pro 90.8%，推理加速 11.1x。

16. **Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.21204) [code](https://varungiridhar.github.io/qplanning/)

    *Varun Giridhar, Anant Khandelwal, Jeremy A. Collins, Ignat Georgiev, Animesh Garg*

    > 大 BC 策略 + 小 off-policy Q 函数，只微调 Q 即可从部署失败中自我改进。

17. **Memory Anchors for Continual Robot Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.26545) [code](https://robot-adaptation.github.io/MemoryAnchors)

    *Maximilian Du, Zhanyi Sun, Chen Xu, Paarth Shah, Masha Itkina, Shuran Song*

    > 持续学习中 10% 的关键锚点经验决定是否灾难性遗忘。

18. **PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.30760) [code](https://baai-agents.github.io/PRACTICE)

    *Ziyi Bai, Siqi Li, Tinglei Huang, Börje F. Karlsson*

    > 训练一个技能学习器对持久技能库做结构化批量编辑（增/改/合/删），执行器冻结。

19. **Motus2: A Self-Evolving General World Model for Dexterous Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.30237)

    *Hongzhe Bi, Zihao Zhou, Yihang Tang, Jingrui Pang, Shuhe Huang, Haitian Liu, Runqing Wang, Shuai Huang, Yichen Wang, Yiming Cheng, Ruowen Zhao, Zhenghua Li, Hengkai Tan, Xiaolong Liu, Jinhui Wan, Jiabao Liu, Min Zhao, Fan Bao, Jun Zhu*

    > 单模型三接口（策略/模拟器/评估器）的自进化世界模型。

20. **A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference.** Machine Intelligence Research, 2026. [paper](https://arxiv.org/abs/2609.01679)

    *Shuaicheng Niu, Guohao Chen, Yaofo Chen, Zhiquan Wen, Jinwu Hu, Zeshuai Deng, Deyu Chen, Shuhai Zhang, Renjie Chen, Zihao Lian, Shoukai Xu, Gang Dai, Yunbei Zhang, Wei Luo, Yifan Zhang, Mingkui Tan, Cheng Deng*

    > 统一测试时适应/学习/扩展的反馈驱动 TTI 视角，覆盖机器人。

21. **SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams.** arXiv, 2026. [paper](https://arxiv.org/abs/2609.02217)

    *Ao Yan, Xin Zhang, Jiawei Du, Joey Tianyi Zhou*

    > 把复用单元定义为'过程族'，局部技能聚合为去实例化的全局先验，提交门保证不退化。

### [技能库 | Skill Library](#论文清单)

检索关键词：`robot skill memory / atomic skill library / autonomous skill discovery`　代表工作：Agentic Skill Discovery, Atomic Skill Library, ViReSkill　（16 篇）

1. **⭐Agentic Skill Discovery.** arXiv, 2024. [paper](https://arxiv.org/abs/2405.15019) [code](https://agentic-skill-discovery.github.io/)

    *Xufeng Zhao, Cornelius Weber, Stefan Wermter*

    > 完全由 LLM 驱动的技能发现：LLM 提任务、采样奖励与成功判定函数、RL 学策略、VLM 独立验证，技能库从零生长。

2. **⭐An Atomic Skill Library Construction Method for Data-Efficient Embodied Manipulation.** arXiv, 2025. [paper](https://arxiv.org/abs/2501.15068)

    *Dongjiang Li, Bo Peng, Chang Li, Ning Qiao, Qi Zheng, Lei Sun, Yusen Qin, Bangguo Li, Yifeng Luan, Bo Wu, Yibing Zhan, Mingang Sun, Tong Xu, Lusong Li, Hui Shen, Xiaodong He*

    > 三轮数据驱动构建原子技能库：VLP 拆子任务 → 抽象技能定义 → VLA 微调。

3. **⭐Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.18597)

    *Yuan Meng, Zhenguo Sun, Max Fest, Xukun Li, Zhenshan Bing, Alois Knoll*

    > 人在环的终身代码生成：把纠正编码为可复用技能 + 外部记忆 RAG，解决 20+ 原语的超长程任务。

4. **⭐ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.24219)

    *Tomoyuki Kagaya, Subramanian Lakshmi, Anbang Ye, Thong Jing Yuan, Jayashree Karlekar, Sugiri Pranata, Natsuki Murakami, Akira Kinose, Yang You*

    > 失败时视觉接地重规划，成功后把计划存入技能记忆下次直接复用，无需再调 LLM。

5. **⭐OpenClawPi: AgileX Robotics Skill Set Library for OpenClaw.** Open Robotics Discourse / Hackster, 2026. [paper](https://discourse.openrobotics.org/t/rapid-deployment-of-openclaw-and-graspgen-crawling-system/53764) [code](https://discourse.openrobotics.org/t/rapid-deployment-of-openclaw-and-graspgen-crawling-system/53764)

    *AgileX Robotics*

    > 松灵机器人（AgileX）面向 OpenClaw 的模块化机器人技能库，覆盖机械臂控制、抓取等场景。

6. **OpenGo: An OpenClaw-Based Robotic Dog with Real-Time Skill Switching.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.01708)

    *Hanbing Li, Xuewei Cao, Zhiwen Zeng, Yuhan Wu, Yanyong Zhang, Yan Xia*

    > OpenClaw 驱动的 Go2 机器狗：技能库 + 调度器 + 基于反馈的自学习，飞书自然语言交互。

7. **⭐SkillOpt: Executive Strategy for Self-Evolving Agent Skills.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.23904) [code](https://aka.ms/skillopt)

    *Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo*

    > 把 skill.md 当冻结 agent 的外部可训练状态：有界编辑 + held-out 验证门 + 拒绝编辑缓冲 + epoch 慢更新；52/52 cells 最优或并列。

8. **You Live More Than Once: Towards Hierarchical Skill Meta-Evolving.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.28390)

    *Xujun Li, Kehan Zheng, Mingyuan Zhao, Yize Geng, Jinfeng Zhou, Qi Zhu, Fei Mi, Lifeng Shang, Minlie Huang, Hongning Wang*

    > 分层技能元进化：从执行轨迹学出“怎样生成与修改技能”的元技能并反过来整理技能库，MineDojo 0.700→0.856，底层权重不变。

9. **VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.05395)

    *Yunhao Yang, Neel P. Bhatt, Kevin Wang, Samuel Tetteh, Zhangyang Wang, Ufuk Topcu*

    > 形式化可验证的自进化技能契约：模型检查反例变成文本梯度，97.2% 规范符合。

10. **Playful Agentic Robot Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19419) [code](https://playful-rats.github.io/)

    *Junyi Zhang, Jiaxin Ge, Hanjun Yoo, Letian Fu, Zihan Yang, Yaowei Liu, Raj Saravanan, Shaofeng Yin, Justin Yu, Dantong Niu, Zirui Wang, Roei Herzig, Ken Goldberg, Yutong Bai, David M. Chan, Ion Stoica, Angjoo Kanazawa, Jiahui Lei, Haiwen Feng, Trevor Darrell*

    > 自主'玩耍'阶段发现技能并蒸馏进代码技能库，LIBERO-PRO 比 CaP-Agent0 +20.6pp。

11. **Analytic Concept-Centric Memory for Agentic Embodied Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.29774)

    *Mingyang Sun, Xiujian Liang, Jiude Wei, Qichen He, Donglin Wang, Cewu Lu, Jianhua Sun*

    > 以部件/模板/位姿/affordance 组织的结构化概念记忆，连接转移记忆与技能记忆。

12. **⭐ASPIRE: Agentic /Skills Discovery for Robotics.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.00272) [code](https://research.nvidia.com/labs/gear/aspire/)

    *Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi "Jim" Fan, Guanzhi Wang*

    > NVIDIA GEAR：执行引擎 + 技能库 + 演化搜索的持续学习系统，技能跨任务/仿真/真机/本体持久化，LIBERO-Pro Long 零样本 31% vs 4%。

13. **A Few Words Go a Long Way: Language Guided Robot Policy Synthesis.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.23784) [code](https://robo-architect.github.io/)

    *Daphne Chen, Archit Ritesh Jain, Eric Goossen, Emma Romig, Michael Murray, Nick Walker, Maya Cakmak*

    > 把策略获取视为交互式程序合成，人类语言纠正蒸馏进持久技能库。

14. **SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.05970)

    *Changyuan Wang, Chubin Zhang, Zhenyu Wu, Runhao Li, Angyuan Ma, Ke Chao, Yinan Liang, Xiuwei Xu, Ziwei Wang, Yansong Tang, Jiwen Lu*

    > MoE 门控隐式切分技能原语并存入情景记忆库。

15. **PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.30760) [code](https://baai-agents.github.io/PRACTICE)

    *Ziyi Bai, Siqi Li, Tinglei Huang, Börje F. Karlsson*

    > 训练一个技能学习器对持久技能库做结构化批量编辑（增/改/合/删），执行器冻结。

16. **SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams.** arXiv, 2026. [paper](https://arxiv.org/abs/2609.02217)

    *Ao Yan, Xin Zhang, Jiawei Du, Joey Tianyi Zhou*

    > 把复用单元定义为'过程族'，局部技能聚合为去实例化的全局先验，提交门保证不退化。

### [VLA + RL](#论文清单)

检索关键词：`VLA reinforcement learning / online RL VLA / offline-to-online robot policy`　代表工作：TwinRL, LWD, SAC Flow, CaP-RL, TT-VLA　（20 篇）

1. **⭐Eureka: Human-Level Reward Design via Coding Large Language Models.** ICLR 2024, 2023. [paper](https://arxiv.org/abs/2310.12931) [code](https://eureka-research.github.io)

    *Yecheng Jason Ma, William Liang, Guanzhi Wang, De-An Huang, Osbert Bastani, Dinesh Jayaraman, Yuke Zhu, Linxi Fan, Anima Anandkumar*

    > LLM 编写奖励函数、RL 学策略、结果反馈回 LLM 改奖励；83% 任务超过人工奖励；训练方法的自动搜索。

2. **⭐SAC Flow: Sample-Efficient Reinforcement Learning of Flow-Based Policies via Velocity-Reparameterized Sequential Modeling.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.25756)

    *Yixian Zhang, Shu'ang Yu, Tonghe Zhang, Mo Guang, Haojia Hui, Kaiwen Long, Yu Wang, Chao Yu, Wenbo Ding*

    > 把 flow rollout 视为残差 RNN，用门控/解码速度网络稳定 off-policy RL 训练 flow 策略。

3. **⭐On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.06748)

    *Changyu Liu, Yiyang Liu, Taowen Wang, Qiao Zhuang, James Chenhao Liang, Wenhao Yang, Renjing Xu, Qifan Wang, Dongfang Liu, Cheng Han*

    > 测试时 RL：用逐步任务进度密集奖励在推理时在线适配 VLA。

4. **⭐TwinRL: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.09023)

    *Qinwen Xu, Jiaming Liu, Rui Zhou, Shaojun Shi, Nuowei Han, Zhuoyang Liu, Chenyang Gu, Shuo Gu, Yang Yue, Gao Huang, Wenzhao Zheng, Sirui Han, Peng Jia, Shanghang Zhang*

    > 手机拍摄重建数字孪生，twin 内并行 RL 预热真机 RL 并定位易失败配置；20 分钟真机交互接近 100% 成功。

5. **⭐CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.22435)

    *Letian Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Dantong Niu, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi "Jim" Fan*

    > CaP-Gym / CaP-Bench / CaP-Agent0 / CaP-RL 四件套；抽象降低时性能下降，可用 agentic test-time compute 弥补；RL with verifiable reward 可 sim2real。

6. **⭐Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.00416)

    *Yi Wang, Xinchen Li, Pengwei Xie, Pu Yang, Buqing Nie, Yunuo Cai, Qinglin Zhang, Chendi Qu, Jeffrey Wu, Jianheng Song, Xinlin Ren, Jingshun Huang, Mingjie Pan, Siyuan Feng, Zhi Chen, Jianlan Luo*

    > 16 台双臂机器人 fleet-scale 离线到在线 RL 持续后训练通用 VLA（DIVL + QAM），8 个真实任务平均 95%。

7. **HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.08610)

    *Zechu Li, Yufeng Jin, Xiaoyang Liu, Puze Liu, Vignesh Prasad, Carlo D'Eramo, Georgia Chalvatzaki*

    > 把机器人 RL 自动化视为 harness 工程问题：从环境搭建到训练的分阶段 agent 流水线。

8. **SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.20698)

    *Kai Tang, Peidong Jia, Zhong Chu, Jixian Wu, Rui Ma, Jiajun Cao, Fangyuan Zhao, Sixiang Chen, Yichen Guo, Xiaowei Chi, Chun-Kai Fan, Kevin Zhang, Jinchang Xu, Fubing Yang, Weishi Mi, Xiaozhu Ju, Jian Tang, Shanghang Zhang*

    > 交互式视频世界模型上的安全 RL，Lagrangian 约束 GRPO。

9. **⭐Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.18247) [code](https://veritas-improvement.github.io/)

    *Mingtong Zhang, Dhruv Shah*

    > 生成器-验证器框架：冻结通用策略 + 无梯度视觉验证器做推理时引导，验证过的自生成轨迹再微调策略；50 条自主轨迹 70% vs 同量人工示范 65%。

10. **⭐ENPIRE: Agentic Robot Policy Self-Improvement in the Real World.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19980)

    *Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi*

    > coding agent 的真机 harness：EN（自动 reset+验证）/ PI / R（多机并行 rollout）/ E（读日志改算法与基础设施），自主训练策略至 99% 成功。

11. **Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.29892)

    *Siyao Chen, Jiakang Yuan, Jiaxin Wang, Tao Chen*

    > 利用生成置信度作为内在奖励的测试时 RL。

12. **Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.31846)

    *Lang Cao, Renhong Chen, Luyi Li, Peng Wang, Mofan Peng, Yitong Li*

    > π0.5 上的任务级 GRPO 后训练，RoboCasa 24 任务 80.6%。

13. **Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models.** IROS 2026, 2026. [paper](https://arxiv.org/abs/2607.16506)

    *Yuhan Liu, Xinyu Zhang, Litao Liu, Abdeslam Boularias*

    > 用下游成功概率（foresight value）塑形子任务交接状态。

14. **RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.26991) [code](https://rl2-vla.github.io)

    *Derek Ming Siang Tan, Shailesh Shailesh, Srikrishna Iyer, William Wei Jie Teo, Yuanliang Ju, Qiao Gu, Guillaume Sartoretti*

    > 仅在预测失败时激活的 latent 组合式推理期引导。

15. **WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.29613)

    *Senyu Fei, Xiaopeng Yu, Siyin Wang, Xianzhong Zhao, Jingjing Gong, Xipeng Qiu*

    > 世界批评家模型：critic 同时预测未来 latent 与价值，149 任务 SOTA。

16. **TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.07314)

    *Ziheng Liu, Quantao Yang*

    > 语义-动作解耦的双时间尺度 RL 后训练。

17. **OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies.** ECCV 2026 Workshop, 2026. [paper](https://arxiv.org/abs/2608.08749)

    *Zhongxi Chen, Shenqi Zong*

    > 价值引导的记忆模块，用在线 rollout 结果学习该保留哪些经验。

18. **Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.13026)

    *Yao Zhou, Hang Gao, Fengge Wu, Changwen Zheng, Wenwen Qiang*

    > 按可检测任务阶段分配优势，解决轨迹级信用混叠。

19. **Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.21204) [code](https://varungiridhar.github.io/qplanning/)

    *Varun Giridhar, Anant Khandelwal, Jeremy A. Collins, Ignat Georgiev, Animesh Garg*

    > 大 BC 策略 + 小 off-policy Q 函数，只微调 Q 即可从部署失败中自我改进。

20. **Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.23831)

    *Brian Zhu, Momen Khalil, E Harrison, Emanuele Poggi, Philipp Schmitt, Bernd Kast, Philine Meister, Pranav Atreya, Qiyang Li, Finn Ferchau, Cesar Colmenero, Yash Shahapurkar, Gokul Narayanan, Melih Erdogan, Kai Wurm, Georg von Wichert, Oier Mees, Eugen Solowjow, Andrew Wagenmaker, Sergey Levine*

    > 推理延迟下的异步 RL：状态增广恢复近马尔可夫性。

### [部署数据回流 | Deployment Data Flywheel](#论文清单)

检索关键词：`learning while deploying robot / fleet robot learning / deployment feedback robot policy`　代表工作：Learning While Deploying, RoboClaw, Arcadia　（9 篇）

1. **⭐Arcadia: Toward a Full-Lifecycle Framework for Embodied Lifelong Learning.** arXiv, 2025. [paper](https://arxiv.org/abs/2512.00076)

    *Minghe Gao, Juncheng Li, Yuze Lin, Xuqi Liu, Jiaming Ji, Xiaoran Pan, Zihan Xu, Xian Li, Mingjie Li, Wei Ji, Rong Wei, Rui Tang, Qizhou Wang, Kai Shen, Jun Xiao, Qi Wu, Siliang Tang, Yueting Zhuang*

    > 全生命周期闭环：自进化探索 → 生成式场景重建 → 共享具身表征 → sim-from-real 评估与演化。

2. **RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.16444)

    *Yixue Zhang, Kun Wu, Zhi Gao, Zhen Zhao, Pei Ren, Zhiyuan Xu, Fei Liao, Xinhua Wang, Shichao Fan, Di Wu, Qiuxuan Feng, Meng Li, Zhengping Che, Chang Liu, Jian Tang*

    > 多样性驱动 + 自反思物理约束的真实任务生成 agent，18k 轨迹。

3. **⭐RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.11558) [code](https://github.com/RoboClaw-Robotics/RoboClaw)

    *Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang, Sukai Wang, Kongtao Hu, Minhui Yu, Bowen Jiang, Zhan Su, Jiayao Ma, Xin He, Yongjian Shen, Yang Yang, Guanghui Ren, Maoqing Yao, Wenhao Wang, Yao Mu*

    > 统一采集-学习-部署的 VLM 控制器；Entangled Action Pairs 把正向技能与逆向恢复绑定实现自复位采数据，成功率 +25%，人工时间 -53.7%。

4. **⭐Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.00416)

    *Yi Wang, Xinchen Li, Pengwei Xie, Pu Yang, Buqing Nie, Yunuo Cai, Qinglin Zhang, Chendi Qu, Jeffrey Wu, Jianheng Song, Xinlin Ren, Jingshun Huang, Mingjie Pan, Siyuan Feng, Zhi Chen, Jianlan Luo*

    > 16 台双臂机器人 fleet-scale 离线到在线 RL 持续后训练通用 VLA（DIVL + QAM），8 个真实任务平均 95%。

5. **⭐Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.18247) [code](https://veritas-improvement.github.io/)

    *Mingtong Zhang, Dhruv Shah*

    > 生成器-验证器框架：冻结通用策略 + 无梯度视觉验证器做推理时引导，验证过的自生成轨迹再微调策略；50 条自主轨迹 70% vs 同量人工示范 65%。

6. **⭐ENPIRE: Agentic Robot Policy Self-Improvement in the Real World.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19980)

    *Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi*

    > coding agent 的真机 harness：EN（自动 reset+验证）/ PI / R（多机并行 rollout）/ E（读日志改算法与基础设施），自主训练策略至 99% 成功。

7. **You Don't Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.07555)

    *Hang Yu*

    > 策略改进的控制平面：证据分级技能库、commit 键控崩溃恢复、签名验证器。

8. **Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.21204) [code](https://varungiridhar.github.io/qplanning/)

    *Varun Giridhar, Anant Khandelwal, Jeremy A. Collins, Ignat Georgiev, Animesh Garg*

    > 大 BC 策略 + 小 off-policy Q 函数，只微调 Q 即可从部署失败中自我改进。

9. **RoboCurve：GPT-6 Astra 直接控制机器人.** 知乎专栏, 2026. [paper](https://zhuanlan.zhihu.com/p/208031326825455257)

    *罗清雨 (知乎)*

    > RoboCurve 第三方测试：GPT-6 Astra 以 EEF waypoint 工具调用控制 YAM 双臂，block→bowl 19/20（2.5 min，2.1K tokens）而精密插入 10%；文章提出“接一个 flow head”的双系统设想。本仓库 notes/44 据此给出 Agent-as-Teleoperator 数据引擎方案。

### [数字孪生 / Sim2Real | Digital Twin / Sim2Real](#论文清单)

检索关键词：`digital twin robot RL / sim-from-real robotics / simulation guided robot learning`　代表工作：TwinRL, Arcadia　（9 篇）

1. **⭐DrEureka: Language Model Guided Sim-To-Real Transfer.** RSS 2024, 2024. [paper](https://arxiv.org/abs/2406.01967) [code](https://eureka-research.github.io/dr-eureka/)

    *Yecheng Jason Ma, William Liang, Hung-Ju Wang, Sam Wang, Yuke Zhu, Linxi Fan, Osbert Bastani, Dinesh Jayaraman*

    > LLM 同时写奖励与域随机化参数范围（摩擦、质量、外力），四足机器人仿真学会站瑜伽球并迁移真机；自动研究推进到 sim-to-real。

2. **⭐Arcadia: Toward a Full-Lifecycle Framework for Embodied Lifelong Learning.** arXiv, 2025. [paper](https://arxiv.org/abs/2512.00076)

    *Minghe Gao, Juncheng Li, Yuze Lin, Xuqi Liu, Jiaming Ji, Xiaoran Pan, Zihan Xu, Xian Li, Mingjie Li, Wei Ji, Rong Wei, Rui Tang, Qizhou Wang, Kai Shen, Jun Xiao, Qi Wu, Siliang Tang, Yueting Zhuang*

    > 全生命周期闭环：自进化探索 → 生成式场景重建 → 共享具身表征 → sim-from-real 评估与演化。

3. **Real2Sim via Active Perception with Behavior Trees Automatically Generated by VLMs.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.08454)

    *Alessandro Adami, Sebastian Zudaire, Ruggero Carli, Pietro Falco*

    > VLM 生成行为树主动获取缺失物理参数。

4. **⭐TwinRL: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.09023)

    *Qinwen Xu, Jiaming Liu, Rui Zhou, Shaojun Shi, Nuowei Han, Zhuoyang Liu, Chenyang Gu, Shuo Gu, Yang Yue, Gao Huang, Wenzhao Zheng, Sirui Han, Peng Jia, Shanghang Zhang*

    > 手机拍摄重建数字孪生，twin 内并行 RL 预热真机 RL 并定位易失败配置；20 分钟真机交互接近 100% 成功。

5. **PerceptTwin: Semantic Scene Reconstruction for Iterative LLM Planning and Verification.** ICRA 2026, 2026. [paper](https://arxiv.org/abs/2606.04226)

    *Charlie Gauthier, Sacha Morin, Liam Paull*

    > ICRA 2026：从感知栈自动构建交互仿真以验证与精炼计划，成功率 +39%。

6. **A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks.** CCF TPCI, 2026. [paper](https://arxiv.org/abs/2606.18646)

    *Kui Yang, Xianlei Long, Haoxuan Li, Yan Ding, Chao Chen*

    > 自动场景生成 + 硬件无关中间件的 real-to-sim-to-real 平台。

7. **ConCent: Contact-Centric Real-to-Sim-to-Real Learning from One Demonstration.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.30268)

    *Heecheol Kim, Namiko Saito, Katsushi Ikeuchi, Yasuyuki Matsushita*

    > 以接触事件序列为学习目标的 real-to-sim-to-real RL。

8. **RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.06699) [code](https://robosnap.github.io)

    *Shujie Zhang, Jingkun Yi, Weipeng Zhong, Zirui Zhou, Yangkun Zhu, Hanqing Wang, Xudong Xu, Weinan Zhang, Chunhua Shen*

    > 单张 RGB 图生成可交互仿真场景，DROID-Sim 564 场景。

9. **Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.19190) [code](https://agentic-real2sim.github.io/)

    *Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Siyuan Luo, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen*

    > VLM agent 把真实交互录像转为可仿真的 episodic twin。

### [世界模型 | World Model](#论文清单)

检索关键词：`robot world model planning / hierarchical world model robotics`　代表工作：H-WM　（9 篇）

1. **⭐H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.11291)

    *Jinbang Huang, Wenyuan Chen, Zhiyuan Li, Oscar Pang, Xiao Hu, Lingfeng Zhang, Yuanzhao Hu, Zhanguang Zhang, Mark Coates, Tongtong Cao, Xingyue Quan, Yingxue Zhang*

    > 分层世界模型：高层逻辑世界模型 + 低层视觉世界模型联合预测，为 VLA 提供稳定中间引导。

2. **Self-adapting Robotic Agents through Online Continual Reinforcement Learning with World Model Feedback.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.04029)

    *Fabian Domberg, Georg Schildbach*

    > DreamerV3 预测残差检测 OOD 并自动触发微调。

3. **Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.12920)

    *Vardhan Dongre, Dilek Hakkani-Tür*

    > 对话减少 40-83pp 动作冲突但降低任务成功；提出世界模型对齐度量。

4. **SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.20698)

    *Kai Tang, Peidong Jia, Zhong Chu, Jixian Wu, Rui Ma, Jiajun Cao, Fangyuan Zhao, Sixiang Chen, Yichen Guo, Xiaowei Chi, Chun-Kai Fan, Kevin Zhang, Jinchang Xu, Fubing Yang, Weishi Mi, Xiaozhu Ju, Jian Tang, Shanghang Zhang*

    > 交互式视频世界模型上的安全 RL，Lagrangian 约束 GRPO。

5. **DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.04927)

    *Jian Zhu, Jianjun Zhang, Taiyi Su, Tianbin Liu, Zhangyuan Wang, Kai Xie, Zitai Huang, Chong Ma, Youzhang He, Tianjian Wang, Hanyang Wang, Weihao Ding, Yi Xu*

    > System 1 WAM 执行器 + 可选 System 2 子任务规划器。

6. **Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.19190) [code](https://agentic-real2sim.github.io/)

    *Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Siyuan Luo, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen*

    > VLM agent 把真实交互录像转为可仿真的 episodic twin。

7. **WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.29613)

    *Senyu Fei, Xiaopeng Yu, Siyin Wang, Xianzhong Zhao, Jingjing Gong, Xipeng Qiu*

    > 世界批评家模型：critic 同时预测未来 latent 与价值，149 任务 SOTA。

8. **ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.13438)

    *Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi*

    > 潜空间世界模型的接触前执行监控。

9. **Motus2: A Self-Evolving General World Model for Dexterous Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.30237)

    *Hongzhe Bi, Zihao Zhou, Yihang Tang, Jingrui Pang, Shuhe Huang, Haitian Liu, Runqing Wang, Shuai Huang, Yichen Wang, Yiming Cheng, Ruowen Zhao, Zhenghua Li, Hengkai Tan, Xiaolong Liu, Jinhui Wan, Jiabao Liu, Min Zhao, Fan Bao, Jun Zhu*

    > 单模型三接口（策略/模拟器/评估器）的自进化世界模型。

### [快慢双系统 | Fast-Slow Dual Systems](#论文清单)

检索关键词：`dual-system VLA / fast slow robot reasoning / System 1 System 2 robotics`　代表工作：Fast-in-Slow, OneTwoVLA, StreamVLA, LaST0, RationalVLA　（15 篇）

1. **Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation.** arXiv, 2024. [paper](https://arxiv.org/abs/2410.08001) [code](https://opendrivelab.com/RoboDual/)

    *Qingwen Bu, Hongyang Li, Li Chen, Jisong Cai, Jia Zeng, Heming Cui, Maoqing Yao, Yu Qiao*

    > 通用-专家双系统，3.8x 控制频率。

2. **OpenHelix: A Short Survey, Empirical Analysis, and Open-Source Dual-System VLA Model for Robotic Manipulation.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.03912) [code](https://openhelix-robot.github.io/)

    *Can Cui, Pengxiang Ding, Wenxuan Song, Shuanghao Bai, Xinyang Tong, Zirui Ge, Runze Suo, Wanqi Zhou, Yang Liu, Bofang Jia, Han Zhao, Siteng Huang, Donglin Wang*

    > 双系统 VLA 短综述 + 开源模型。

3. **⭐OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.11917)

    *Fanqi Lin, Ruiqian Nai, Yingdong Hu, Jiacheng You, Junming Zhao, Yang Gao*

    > 单一模型自适应切换推理与执行模式，关键时刻显式推理。

4. **⭐Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning.** arXiv, 2025. [paper](https://arxiv.org/abs/2506.01953) [code](https://fast-in-slow.github.io)

    *Hao Chen, Jiaming Liu, Chenyang Gu, Zhuoyang Liu, Renrui Zhang, Xiaoqi Li, Xiao He, Yandong Guo, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng*

    > System 1 嵌入 System 2 共享参数的统一双系统 VLA，action chunk=8 时 117.7 Hz。

5. **⭐RationalVLA: A Rational Vision-Language-Action Model with Dual System.** arXiv, 2025. [paper](https://arxiv.org/abs/2506.10826) [code](https://irpn-eai.github.io/RationalVLA)

    *Wenxuan Song, Jiayi Chen, Wenxue Li, Xu He, Han Zhao, Can Cui, Pengxiang Ding Shiyan Su, Feilong Tang, Xuelian Cheng, Donglin Wang, Zongyuan Ge, Xinhu Zheng, Zhe Liu, Hesheng Wang, Haoang Li*

    > RAMA 基准含 6 维缺陷指令；双系统通过可学习 latent 嵌入拒绝不可行指令。

6. **⭐LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.05248) [code](https://vla-last0.github.io/)

    *Zhuoyang Liu, Jiaming Liu, Hao Chen, Jiale Yu, Ziyu Guo, Chengkai Hou, Chenyang Gu, Xiangju Mi, Renrui Zhang, Kun Wu, Zhengping Che, Jian Tang, Pheng-Ann Heng, Shanghang Zhang*

    > 潜空间时空 CoT：未来视觉、3D 结构、本体状态进入 latent 推理，MoT 双专家异频运行。

7. **⭐StreamVLA: Breaking the Reason-Act Cycle via Completion-State Gating.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.01100)

    *Tongqing Chen, Hang Wu, Jiasen Wang, Xiaotao Li, Lu Fang*

    > Lock-and-Gated：仅在子任务切换时触发慢思考并想象完成态，72% 时间步跳过自回归解码，延迟 -48%。

8. **Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System.** ACL 2026, 2026. [paper](https://arxiv.org/abs/2604.24921) [code](https://libra-vla.github.io/)

    *Yifei Wei, Linqing Zhong, Yi Liu, Yuxiang Lu, Xindong He, Maoqing Yao, Guanghui Ren*

    > ACL 2026：异步粗到细双系统。

9. **Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.02739)

    *Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin, Qinsi Wang, Yi Li, Shuangjun Liu, Shuai Zhang, Taotao Jing, Dashan Gao, Ning Bi, Jingwei Sun, Yiran Chen, Hai Li*

    > 预测 VLM 输出 delta，减少 50-75% VLM 调用。

10. **VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.30011)

    *Mingjian Gao, Wenqiao Zhang, Yuqian Yuan, Yang Dai, Binhe Yu, Zheqi Lv, Haoyu Zheng, Jiaqi Zhu, Zhiqi Ge, Zixuan Wan, Siliang Tang, Yueting Zhuang*

    > 视觉中间推理替代文本 CoT，延迟 8.4s→0.37s。

11. **UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.22794) [code](https://github.com/linsun449/UniFS)

    *Lin Sun, Zhiwei Guan, Conglin Wang, Zihong Chen, Jianhai Yu, Zongsheng Li, Boyong He, Tao Sun, Jiale Cao, Lige Liu*

    > VLM 层按更新频率分层，延迟 36.5ms→17.8ms。

12. **Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.05377)

    *Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai, Jing Xiong, Ganlin Yang, Jinliang Zheng, Jiafei Cao, Xueyuan Wei, Jiangmiao Pang, Yuan Shen, Tai Wang*

    > 32 个规范技能原语的双向对齐规划接口，附推理期 harness engineering。

13. **DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.04927)

    *Jian Zhu, Jianjun Zhang, Taiyi Su, Tianbin Liu, Zhangyuan Wang, Kai Xie, Zitai Huang, Chong Ma, Youzhang He, Tianjian Wang, Hanyang Wang, Weihao Ding, Yi Xu*

    > System 1 WAM 执行器 + 可选 System 2 子任务规划器。

14. **⭐PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.24115) [code](https://worv-ai.github.io/ponderpounce/)

    *Suhwan Choi, Jaeyoon Jung, Sungkyung Kim, Yunsung Lee, Youngjae Yu*

    > 复用 MLLM 原生因果上下文作为 episode 记忆：Ponder(System2) 异步向 Pounce(System1 VLA) 发送最新认知 token；RoboMME 60.83% vs π0.5 17.93%。

15. **RoboCurve：GPT-6 Astra 直接控制机器人.** 知乎专栏, 2026. [paper](https://zhuanlan.zhihu.com/p/208031326825455257)

    *罗清雨 (知乎)*

    > RoboCurve 第三方测试：GPT-6 Astra 以 EEF waypoint 工具调用控制 YAM 双臂，block→bowl 19/20（2.5 min，2.1K tokens）而精密插入 10%；文章提出“接一个 flow head”的双系统设想。本仓库 notes/44 据此给出 Agent-as-Teleoperator 数据引擎方案。

### [端侧部署 / Edge Agent | Edge Agent / On-Device Deployment](#论文清单)

检索关键词：`edge embodied AI / on-device VLA / robot inference latency`　代表工作：Fast-in-Slow, Harness Engineering　（11 篇）

1. **⭐Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning.** arXiv, 2025. [paper](https://arxiv.org/abs/2506.01953) [code](https://fast-in-slow.github.io)

    *Hao Chen, Jiaming Liu, Chenyang Gu, Zhuoyang Liu, Renrui Zhang, Xiaoqi Li, Xiao He, Yandong Guo, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng*

    > System 1 嵌入 System 2 共享参数的统一双系统 VLA，action chunk=8 时 117.7 Hz。

2. **Habilis-$β$: A Fast-Motion and Long-Lasting On-Device Vision-Language-Action Model.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.18813)

    *Tommoro Robotics,  :, Jesoon Kang, Taegeon Park, Jisu An, Soo Min Kimm, Jaejoon Kim, Jinu Pahk, Byungju Kim, Junseok Lee, Namheon Baek, Sungwan Ha, Hojun Baek, Eduardo Ayerve Cruz, Wontae Kim, Junghyeon Choi, Yousuk Lee, Joonmo Han, Sunghyun Cho, Sunghyun Kwon, Soyoung Lee, Jun Ki Lee, Seung-Joon Yi, Byoung-Tak Zhang, Theo Taeyeong Kim*

    > 端侧 VLA；提出 Tasks per Hour × Mean Time Between Intervention 的生产力-可靠性平面。

3. **LSAI: A Large Small AI Model Codesign Framework for Agentic Robot Scenarios.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.21726)

    *Longyu Zhou, Supeng Leng, Tianhao Liang, Jianping Yao*

    > 大小模型协同设计的 agentic 机器人协作。

4. **Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.02739)

    *Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin, Qinsi Wang, Yi Li, Shuangjun Liu, Shuai Zhang, Taotao Jing, Dashan Gao, Ning Bi, Jingwei Sun, Yiran Chen, Hai Li*

    > 预测 VLM 输出 delta，减少 50-75% VLM 调用。

5. **VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.30011)

    *Mingjian Gao, Wenqiao Zhang, Yuqian Yuan, Yang Dai, Binhe Yu, Zheqi Lv, Haoyu Zheng, Jiaqi Zhu, Zhiqi Ge, Zixuan Wan, Siliang Tang, Yueting Zhuang*

    > 视觉中间推理替代文本 CoT，延迟 8.4s→0.37s。

6. **⭐Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer.** ACM/IFIP Middleware 2026 (Big Ideas), 2026. [paper](https://arxiv.org/abs/2606.09416)

    *Sanghoon Lee, Jiyeong Chae, Kyung-Joon Park*

    > 机器人中间件即 Harness 层：必须同时在控制、计算、通信三处介入；提出 Projection / Isolation / Transfer 三个缺失的强制功能与 ROS 2 Harness Profile。

7. **Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.29350)

    *Junzhou Chen, Jindong Wang, Gang Zhou*

    > 训练无关时空视觉 token 合并，π0.5 8.3x 加速。

8. **Latency-Tolerant Cloud-Edge Collaborative Vision-Language-Action Models via Emergent Representational Specialization.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.00569)

    *Daojie Peng, Fulong Ma, Bingtao Wang, Sheng Wang, Jun Ma*

    > 把时间错位当表示学习问题的云-边 VLA，40 步延迟仍保持 63.8-78%。

9. **PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.03682) [code](https://github.com/mingti-org/phyai)

    *Chenghua Wang, Daliang Xu, Dongqi Cai, Duojin Sun, Hao Zhang, Haoze Qian, Huaiyuan Zhang, Jinshuo Cui, Junbo Cui, Kezhao Zhao, Longxi Gao, Mengwei Xu, Rongjie Yi, Ruixin Liu, Shangguang Wang, Tam Sikyuen, Tianyue Zhang, Weikai Xie, Xuanzhe Liu, Yingying Qin, Yiwen Lu, Yuan Yao, Yuezhi Zu, Yunhan Guo, Yuxin Zheng, Ziqi Guo*

    > 统一 VLA/WAM 推理运行时，提出 control-time Roofline。

10. **EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints.** APPT 2026, 2026. [paper](https://arxiv.org/abs/2608.15502)

    *Ao Zhou, Bo Dai, Le Yu, Xingyu Liu, Zeyu Hao, Lingkun Long, Chunming Hu, Jianlei Yang*

    > 端-边协同推理，20Hz 约束下能效 +236%。

11. **Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.23831)

    *Brian Zhu, Momen Khalil, E Harrison, Emanuele Poggi, Philipp Schmitt, Bernd Kast, Philine Meister, Pranav Atreya, Qiyang Li, Finn Ferchau, Cesar Colmenero, Yash Shahapurkar, Gokul Narayanan, Melih Erdogan, Kai Wurm, Georg von Wichert, Oier Mees, Eugen Solowjow, Andrew Wagenmaker, Sergey Levine*

    > 推理延迟下的异步 RL：状态增广恢复近马尔可夫性。

### [Harness](#论文清单)

检索关键词：`robot harness / Physical AI harness / VLA harness`　代表工作：RHO, Harness VLA, Harness Engineering, PhyAgentOS　（15 篇）

1. **Nautilus: From One Prompt to Plug-and-Play Robot Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.11665)

    *Yufeng Jin, Jianfei Guo, Xiaogang Jia, Yu Deng, Zechu Li, Han Liu, Weiran Liao, Vignesh Prasad, Mathias Franzius, Gerhard Neumann, Georgia Chalvatzaki*

    > 从一句 prompt 生成复现/评估/微调/部署工作流的开源研究 harness。

2. **HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.08610)

    *Zechu Li, Yufeng Jin, Xiaoyang Liu, Puze Liu, Vignesh Prasad, Carlo D'Eramo, Georgia Chalvatzaki*

    > 把机器人 RL 自动化视为 harness 工程问题：从环境搭建到训练的分阶段 agent 流水线。

3. **⭐Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer.** ACM/IFIP Middleware 2026 (Big Ideas), 2026. [paper](https://arxiv.org/abs/2606.09416)

    *Sanghoon Lee, Jiyeong Chae, Kyung-Joon Park*

    > 机器人中间件即 Harness 层：必须同时在控制、计算、通信三处介入；提出 Projection / Isolation / Transfer 三个缺失的强制功能与 ROS 2 Harness Profile。

4. **⭐RHO: Your Coding Agent is Secretly a Roboticist.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.16458) [code](https://rho-robotics.github.io)

    *Karim Elmaaroufi, Justin Svegliato, Sarunas Kalade, Graham Schelle, Sanjit A. Seshia, Matei Zaharia*

    > Robotics Harness Optimization：coding agent 在训练时搜索多文件策略仓库（Repositories-as-Policies），部署时单轮执行，LIBERO-PRO 45% vs π0.5 12.8%。

5. **Guava: An Effective and Universal Harness for Embodied Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.18363)

    *Haowen Liu, Xirui Li, Shaoxiong Yao, Peng Shi, Tianyi Zhou, Jia-Bin Huang, Furong Huang, Jiayuan Mao*

    > 系统探索 harness 设计空间：迭代感知-推理-动作循环、语义动作抽象、多模态观测三要素；蒸馏进 4B 模型。

6. **Harness Engineering for Self-Improvement.** Lil'Log, 2026. [paper](https://lilianweng.github.io/posts/2026-07-04-harness/) [code](https://lilianweng.github.io/posts/2026-07-04-harness/)

    *Lilian Weng*

    > 定义 Harness 三大模式（工作流自动化 / 文件系统即记忆 / 子代理），提出优化对象阶梯 prompt→context→workflow→harness code→optimizer code，列出 RSI 的 7 个未解挑战。

7. **Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.05377)

    *Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai, Jing Xiong, Ganlin Yang, Jinliang Zheng, Jiafei Cao, Xueyuan Wei, Jiangmiao Pang, Yuan Shen, Tai Wang*

    > 32 个规范技能原语的双向对齐规划接口，附推理期 harness engineering。

8. **⭐Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.08448) [code](https://github.com/RLinf/RPent)

    *Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, Zhengru Fang, Yi Nie, Changxu Wei, Yu Wang, Wenbo Ding, Chao Yu*

    > 把冻结 VLA 暴露为可重试的接触原语，与少量解析原语组合；从执行轨迹学习原语的适用范围而非扩张技能库；LIBERO-Pro +38.6pp。

9. **Recursive Harness Self-Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.15524)

    *Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Matei Zaharia, Yujin Tang*

    > harness 作为 prompt 级 agent loop 规范，用配对反馈迭代精炼。

10. **⭐PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.16636)

    *Yang Liu, Weixing Chen, Xinshuai Song, Tao Pu, Siwen Mo, Yongjie Bai, Zihao Chen, Qianran Sun, Liruo Zhong, Ying Shen, Liang Lin*

    > 会话为最小调度单元的运行时：State-as-a-File、SessionVerifier 区分执行终止与语义完成、epistemic memory、分层安全；19+ 本体验证。

11. **RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.18060)

    *Jinbang Huang, Yuanzhao Hu, Zhiyuan Li, Ran Qi, Yixin Xiao, Zhanguang Zhang, Mark Coates, Tongtong Cao, Yingxue Zhang*

    > 多模态执行记忆刻画异构策略能力边界，Memory Bridge 把机器人引导到下一策略的分布内区域。

12. **Towards the Harness of Embodied Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.11246) [code](https://eit-hai.github.io/thea)

    *Qi Wang, Tianyi Wang, Chengyang Li, Shikun Ban, Yurun Chen, Yizhong Ge, Jason Qin, Chengtai Li, Wentao Zhu*

    > 继承 coding agent 组件，补上物理世界缺的两件事：Scene Graph as Context 与 Evaluation as Exit Codes。

13. **Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.09857)

    *Rohan Bhagra, Mahantesh Halapannavar, Uddhav Bhattarai*

    > 规划与执行之间的 LLM-as-a-Judge 集成验证层，接受/拒绝/升级人工，对抗攻击 97% 拦截。

14. **Self-Evolving Embodied Agents via Skill-Harness Evolution.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.11350)

    *Peidong Wang, Zhiming Ma, Ying Chang, Xufang Luo, Xiaocui Yang, Shi Feng, Yuqing Yang, Dongsheng Li*

    > 冻结模型同时充当规划器和优化器，演化技能与 context-code harness。

15. **Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.16590)

    *Xin Ding, Liang Mi, Mingzhe Huang, Zixuan Wang, Chao Zhang, Zixu Hao, Fu Chen, Xiangyu Li, Yikai Zheng, Yaoyu Guo, Weijun Wang, Kun Li, Hao Wu, Yunxin Liu, Ting Cao*

    > 三时间尺度闭环 harness：动作频率治理 / rollout 级 critic-recovery 提议 / 验证门控技能更新；LIBERO-Pro 90.8%，推理加速 11.1x。

### [Runtime 运行时 | Runtime](#论文清单)

检索关键词：`embodied agent runtime / robot runtime governance`　代表工作：PhyAgentOS, Runtime Governance　（9 篇）

1. **⭐Harnessing Embodied Agents: Runtime Governance for Policy-Constrained Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.07833)

    *Xue Qin, Simin Luan, John See, Zeyd Boukhers, Cong Yang, Zhijun Li*

    > 把治理外置为运行时层：策略检查、能力准入、执行监控、回滚、人工接管；96.2% 越权拦截。

2. **EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.11174) [code](https://github.com/s20sc/embodied-gov-bench)

    *Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li*

    > 七维治理评测：越权调用、运行时漂移、恢复、策略可移植、升级安全、人工接管、审计。

3. **Federated Single-Agent Robotics: Multi-Robot Coordination Without Intra-Robot Multi-Agent Fragmentation.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.11028) [code](https://github.com/s20sc/fsar-fleet-coordination)

    *Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li*

    > 多机器人协调不需要机器人内部多 agent 碎片化，联邦式 fleet runtime。

4. **ICAN-Deploy: Identity-Stable Canary Deployment for Safety-Critical Embodied Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.28097)

    *Xue Qin, Simin Luan, John See, Zeyd Boukhers, Cong Yang, Zhijun Li*

    > 身份稳定的金丝雀部署，TLA+ 验证。

5. **⭐Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer.** ACM/IFIP Middleware 2026 (Big Ideas), 2026. [paper](https://arxiv.org/abs/2606.09416)

    *Sanghoon Lee, Jiyeong Chae, Kyung-Joon Park*

    > 机器人中间件即 Harness 层：必须同时在控制、计算、通信三处介入；提出 Projection / Isolation / Transfer 三个缺失的强制功能与 ROS 2 Harness Profile。

6. **HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.23565)

    *Xiaolin Zhou, Liu Liu, Tingyang Xiao, Wei Feng, Fa Fu, Xinrui Meng, Xinjie Wang, Jialiang Han, Boyang Yu, Yun Du, Wei Sui, Zhizhong Su*

    > Embodied AgentOS + 3D 空间记忆 + 具身技能三层真机框架。

7. **⭐PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.16636)

    *Yang Liu, Weixing Chen, Xinshuai Song, Tao Pu, Siwen Mo, Yongjie Bai, Zihao Chen, Qianran Sun, Liruo Zhong, Ying Shen, Liang Lin*

    > 会话为最小调度单元的运行时：State-as-a-File、SessionVerifier 区分执行终止与语义完成、epistemic memory、分层安全；19+ 本体验证。

8. **You Don't Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.07555)

    *Hang Yu*

    > 策略改进的控制平面：证据分级技能库、commit 键控崩溃恢复、签名验证器。

9. **PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.03682) [code](https://github.com/mingti-org/phyai)

    *Chenghua Wang, Daliang Xu, Dongqi Cai, Duojin Sun, Hao Zhang, Haoze Qian, Huaiyuan Zhang, Jinshuo Cui, Junbo Cui, Kezhao Zhao, Longxi Gao, Mengwei Xu, Rongjie Yi, Ruixin Liu, Shangguang Wang, Tam Sikyuen, Tianyue Zhang, Weikai Xie, Xuanzhe Liu, Yingying Qin, Yiwen Lu, Yuan Yao, Yuezhi Zu, Yunhan Guo, Yuxin Zheng, Ziqi Guo*

    > 统一 VLA/WAM 推理运行时，提出 control-time Roofline。

### [安全 | Safety](#论文清单)

检索关键词：`embodied agent safety / robot agent safety envelope / policy constrained execution`　代表工作：ROSClaw, Runtime Governance, RationalVLA　（15 篇）

1. **⭐RationalVLA: A Rational Vision-Language-Action Model with Dual System.** arXiv, 2025. [paper](https://arxiv.org/abs/2506.10826) [code](https://irpn-eai.github.io/RationalVLA)

    *Wenxuan Song, Jiayi Chen, Wenxue Li, Xu He, Han Zhao, Can Cui, Pengxiang Ding Shiyan Su, Feilong Tang, Xuelian Cheng, Donglin Wang, Zongyuan Ge, Xinhu Zheng, Zhe Liu, Hesheng Wang, Haoang Li*

    > RAMA 基准含 6 维缺陷指令；双系统通过可学习 latent 嵌入拒绝不可行指令。

2. **SENTINEL: A Multi-Level Formal Framework for Safety Evaluation of Foundation Model-based Embodied Agents.** arXiv, 2025. [paper](https://arxiv.org/abs/2510.12985)

    *Simon Sinong Zhan, Philip Wang, Yao Liu, Yiyan Peng, Zinan Wang, Qineng Wang, Zhian Ruan, Xiangyu Shi, Xinyu Cao, Frank Yang, Zhenyang Ni, Kangrui Wang, Ruohan Zhang, Huajie Shao, Manling Li, Qi Zhu*

    > 语义/计划/轨迹三层时序逻辑形式化安全评估。

3. **⭐AgentRob: From Virtual Forum Agents to Hijacked Physical Robots.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.13591)

    *Wenrui Liu, Yaxuan Wang, Xun Zhang, Yanshu Wang, Jiashen Wei, Yifan Xiang, Yuhang Wang, Mingshen Ye, Elsie Dai, Zhiqi Liu, Yingjie Xu, Xinyang Chen, Hengzhe Sun, Jiyu Shen, Jingjing He, Tong Yang*

    > 通过 MCP 把论坛 agent 与 Unitree Go2/G1 相连，展示论坛介导的多 agent 机器人编排（及被劫持风险）。

4. **⭐ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.26997)

    *Irvin Steve Cardenas, Marcus Anthony Arnett, Natalie Catherine Yeo, Lucky Sah, Jong-Hoon Kim*

    > OpenClaw runtime + ROS 2 的模型无关执行层：能力发现、观测归一、安全包络内的预执行验证、审计日志；发现不同前沿模型越权动作率差 3.4-4.8 倍。

5. **⭐Harnessing Embodied Agents: Runtime Governance for Policy-Constrained Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.07833)

    *Xue Qin, Simin Luan, John See, Zeyd Boukhers, Cong Yang, Zhijun Li*

    > 把治理外置为运行时层：策略检查、能力准入、执行监控、回滚、人工接管；96.2% 越权拦截。

6. **EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.11174) [code](https://github.com/s20sc/embodied-gov-bench)

    *Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li*

    > 七维治理评测：越权调用、运行时漂移、恢复、策略可移植、升级安全、人工接管、审计。

7. **ICAN-Deploy: Identity-Stable Canary Deployment for Safety-Critical Embodied Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.28097)

    *Xue Qin, Simin Luan, John See, Zeyd Boukhers, Cong Yang, Zhijun Li*

    > 身份稳定的金丝雀部署，TLA+ 验证。

8. **EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents.** ICML 2026, 2026. [paper](https://arxiv.org/abs/2605.30924) [code](https://github.com/dongwxxkchoi/EMBGuard)

    *Dongwook Choi, Taeyoon Kwon, Bogyung Jeong, Minju Kim, Yeonjun Hwang, Hyojun Kim, Byungchul Kim, Young Kyun Jang, Jinyoung Yeo*

    > ICML 2026：与策略解耦的 MLLM 物理风险护栏，2B/4B 媲美闭源大模型。

9. **Same Weights, Different Robot: A Deployment Safety View of VLA Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.03724)

    *Jianwei Tai*

    > 动作反归一化元数据是可执行策略的一部分；替换元数据键使成功 28/28→2/28。

10. **VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.05395)

    *Yunhao Yang, Neel P. Bhatt, Kevin Wang, Samuel Tetteh, Zhangyang Wang, Ufuk Topcu*

    > 形式化可验证的自进化技能契约：模型检查反例变成文本梯度，97.2% 规范符合。

11. **SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.20698)

    *Kai Tang, Peidong Jia, Zhong Chu, Jixian Wu, Rui Ma, Jiajun Cao, Fangyuan Zhao, Sixiang Chen, Yichen Guo, Xiaowei Chi, Chun-Kai Fan, Kevin Zhang, Jinchang Xu, Fubing Yang, Weishi Mi, Xiaozhu Ju, Jian Tang, Shanghang Zhang*

    > 交互式视频世界模型上的安全 RL，Lagrangian 约束 GRPO。

12. **⭐PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.16636)

    *Yang Liu, Weixing Chen, Xinshuai Song, Tao Pu, Siwen Mo, Yongjie Bai, Zihao Chen, Qianran Sun, Liruo Zhong, Ying Shen, Liang Lin*

    > 会话为最小调度单元的运行时：State-as-a-File、SessionVerifier 区分执行终止与语义完成、epistemic memory、分层安全；19+ 本体验证。

13. **When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.06830)

    *Zhen Huang, Zhihuang Liu, Weijia Shi, Yifan Yang, Weishang Wu, Zhiping Cai*

    > 多机器人通信攻击可达 97.8% 不安全动作成功率，CPV Gate 缓解。

14. **Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.09857)

    *Rohan Bhagra, Mahantesh Halapannavar, Uddhav Bhattarai*

    > 规划与执行之间的 LLM-as-a-Judge 集成验证层，接受/拒绝/升级人工，对抗攻击 97% 拦截。

15. **ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.13438)

    *Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi*

    > 潜空间世界模型的接触前执行监控。

### [标准接口 / Hardware API | Standard Interfaces / Hardware API](#论文清单)

检索关键词：`agent hardware interface / AI hardware standard / MCP physical devices`　代表工作：MHS, ROSClaw　（5 篇）

1. **ROSBag MCP Server: Analyzing Robot Data with LLMs for Agentic Embodied AI Applications.** arXiv, 2025. [paper](https://arxiv.org/abs/2511.03497) [code](https://github.com/binabik-ai/mcp-rosbags)

    *Lei Fu, Sahar Salimpour, Leonardo Militano, Harry Edelman, Jorge Peña Queralta, Giovanni Toffetti*

    > 用 MCP 让 LLM 分析 ROS/ROS 2 bag 数据。

2. **⭐AgentRob: From Virtual Forum Agents to Hijacked Physical Robots.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.13591)

    *Wenrui Liu, Yaxuan Wang, Xun Zhang, Yanshu Wang, Jiashen Wei, Yifan Xiang, Yuhang Wang, Mingshen Ye, Elsie Dai, Zhiqi Liu, Yingjie Xu, Xinyang Chen, Hengzhe Sun, Jiyu Shen, Jingjing He, Tong Yang*

    > 通过 MCP 把论坛 agent 与 Unitree Go2/G1 相连，展示论坛介导的多 agent 机器人编排（及被劫持风险）。

3. **⭐ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.26997)

    *Irvin Steve Cardenas, Marcus Anthony Arnett, Natalie Catherine Yeo, Lucky Sah, Jong-Hoon Kim*

    > OpenClaw runtime + ROS 2 的模型无关执行层：能力发现、观测归一、安全包络内的预执行验证、审计日志；发现不同前沿模型越权动作率差 3.4-4.8 倍。

4. **Contract-Grounded Behavior Tree Synthesis via Coding Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.12220)

    *Jonathan Salfity, Robert Blake Anderson, Mitch Pryor*

    > coding agent 先向机器人侧 MCP server 拉取技能契约再合成行为树。

5. **⭐Previewing the Model Hardware Standard (MHS).** Anthropic Research Preview, 2026. [paper](https://www.anthropic.com/news/model-hardware-standard-research-preview) [code](https://www.anthropic.com/news/model-hardware-standard-research-preview)

    *Anthropic*

    > Anthropic 2026-08-27 研究预览：让 agent 通过统一规范发现、操作、排障真实设备（显微镜、液体处理器、机械臂），被称为硬件版 MCP。

### [多机器人协作 | Multi-Robot Collaboration](#论文清单)

检索关键词：`multi-robot LLM / multi-agent robot collaboration`　代表工作：RoCo, REMAC, RoboOS　（13 篇）

1. **⭐RoCo: Dialectic Multi-Robot Collaboration with Large Language Models.** arXiv, 2023. [paper](https://arxiv.org/abs/2307.04738) [code](https://project-roco.github.io)

    *Zhao Mandi, Shreeya Jain, Shuran Song*

    > 多机器人用 LLM 对话协商分工与航点，交给多臂运动规划器；RoCoBench。

2. **⭐MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation.** arXiv, 2024. [paper](https://arxiv.org/abs/2411.17636)

    *Harsh Singh, Rocktim Jyoti Das, Mingfei Han, Preslav Nakov, Ivan Laptev*

    > Planner / Coder / Supervisor 多 LLM agent 零样本操作，每步环境观测驱动重规划。

3. **⭐REMAC: Self-Reflective and Self-Evolving Multi-Agent Collaboration for Long-Horizon Robot Manipulation.** arXiv, 2025. [paper](https://arxiv.org/abs/2503.22122)

    *Puzhen Yuan, Angyuan Ma, Yunchao Yao, Huaxiu Yao, Masayoshi Tomizuka, Mingyu Ding*

    > 多机器人长程规划：前置/后置条件检查的自反思 + 场景推理的自进化，成功率 +40%，效率 +52.7%。

4. **⭐RoboOS: A Hierarchical Embodied Framework for Cross-Embodiment and Multi-Agent Collaboration.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.03673) [code](https://github.com/FlagOpen/RoboOS)

    *Huajie Tan, Xiaoshuai Hao, Cheng Chi, Minglan Lin, Yaoxu Lyu, Mingyu Cao, Dong Liang, Zhuo Chen, Mengsi Lyu, Cheng Peng, Chenrui He, Yulong Ao, Yonghua Lin, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang*

    > Brain-Cerebellum 架构：Embodied Brain + Cerebellum Skill Library + Real-Time Shared Memory，边云通信。

5. **⭐RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration.** arXiv, 2025. [paper](https://arxiv.org/abs/2510.26536) [code](https://flagopen.github.io/RoboOS/)

    *Huajie Tan, Cheng Chi, Xiansheng Chen, Yuheng Ji, Zhongxia Zhao, Xiaoshuai Hao, Yaoxu Lyu, Mingyu Cao, Junkai Zhao, Huaihai Lyu, Enshen Zhou, Ning Chen, Yankai Fu, Cheng Peng, Wei Guo, Dong Liang, Zhuo Chen, Mengsi Lyu, Chenrui He, Yulong Ao, Yonghua Lin, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang*

    > Spatio-Temporal-Embodiment Memory 统一多机器人终身协作的共享记忆。

6. **Tool-RoCo: An Agent-as-Tool Self-organization Large Language Model Benchmark in Multi-robot Cooperation.** arXiv, 2025. [paper](https://arxiv.org/abs/2511.21510) [code](https://github.com/ColaZhang22/Tool-Roco)

    *Ke Zhang, Xiaoning Zhao, Ce Zheng, Jiahong Ning, Dandan Zhu, Wenqi Zhang, Chen Sun, Toshiharu Sugawara*

    > 把其他 agent 当工具的自组织多机器人基准。

7. **MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.20577)

    *Baiqing Wang, Helei Cui, Bo Zhang, Xiaolong Zheng, Bin Guo, Zhiwen Yu*

    > 相似任务记忆化复用多机器人计划。

8. **Scale-Plan: Scalable Language-Enabled Task Planning for Heterogeneous Multi-Robot Teams.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.08814) [code](https://github.com/honda-research-institute/Scale_Plan)

    *Piyush Gupta, Sangjae Bae, Jiachen Li, David Isele*

    > LLM 引导的动作图搜索裁剪 PDDL 问题规模。

9. **LSAI: A Large Small AI Model Codesign Framework for Agentic Robot Scenarios.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.21726)

    *Longyu Zhou, Supeng Leng, Tianhao Liang, Jianping Yao*

    > 大小模型协同设计的 agentic 机器人协作。

10. **Federated Single-Agent Robotics: Multi-Robot Coordination Without Intra-Robot Multi-Agent Fragmentation.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.11028) [code](https://github.com/s20sc/fsar-fleet-coordination)

    *Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li*

    > 多机器人协调不需要机器人内部多 agent 碎片化，联邦式 fleet runtime。

11. **Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.12920)

    *Vardhan Dongre, Dilek Hakkani-Tür*

    > 对话减少 40-83pp 动作冲突但降低任务成功；提出世界模型对齐度量。

12. **DynaHMRC: Decentralized Heterogeneous Multi-Robot Collaboration for Dynamic Tasks with Large Language Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.14882)

    *Wenhao Yu, Yu'ang Xie, Yifan Duan, Jie Peng, Guanting Ye, Ka-Veng Yuen, Yanyong Zhang, Jianmin Ji*

    > 去中心化角色感知 LLM agent 的异构多机器人协作。

13. **When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.06830)

    *Zhen Huang, Zhihuang Liu, Weijia Shi, Yifan Yang, Weishang Wu, Zhiping Cai*

    > 多机器人通信攻击可达 97.8% 不安全动作成功率，CPV Gate 缓解。

### [跨本体 | Cross-Embodiment](#论文清单)

检索关键词：`cross-embodiment robot agent / heterogeneous robot collaboration`　代表工作：RoboOS, ASPIRE, Harness VLA　（5 篇）

1. **⭐RoboOS: A Hierarchical Embodied Framework for Cross-Embodiment and Multi-Agent Collaboration.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.03673) [code](https://github.com/FlagOpen/RoboOS)

    *Huajie Tan, Xiaoshuai Hao, Cheng Chi, Minglan Lin, Yaoxu Lyu, Mingyu Cao, Dong Liang, Zhuo Chen, Mengsi Lyu, Cheng Peng, Chenrui He, Yulong Ao, Yonghua Lin, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang*

    > Brain-Cerebellum 架构：Embodied Brain + Cerebellum Skill Library + Real-Time Shared Memory，边云通信。

2. **⭐ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.04664) [code](https://www.rosclaw.io/)

    *Rongfeng Zhao, Xuanhao Zhang, Zhaochen Guo, Xiang Shao, Zhongpan Zhu, Bin He, Jie Chen*

    > 同名工作：e-URDF 物理约束 + sim-real 拓扑映射，统一 VLM 控制器串起采集、训练与执行。

3. **A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks.** CCF TPCI, 2026. [paper](https://arxiv.org/abs/2606.18646)

    *Kui Yang, Xianlei Long, Haoxuan Li, Yan Ding, Chao Chen*

    > 自动场景生成 + 硬件无关中间件的 real-to-sim-to-real 平台。

4. **⭐ASPIRE: Agentic /Skills Discovery for Robotics.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.00272) [code](https://research.nvidia.com/labs/gear/aspire/)

    *Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi "Jim" Fan, Guanzhi Wang*

    > NVIDIA GEAR：执行引擎 + 技能库 + 演化搜索的持续学习系统，技能跨任务/仿真/真机/本体持久化，LIBERO-Pro Long 零样本 31% vs 4%。

5. **⭐Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.08448) [code](https://github.com/RLinf/RPent)

    *Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, Zhengru Fang, Yi Nie, Changxu Wei, Yu Wang, Wenbo Ding, Chao Yu*

    > 把冻结 VLA 暴露为可重试的接触原语，与少量解析原语组合；从执行轨迹学习原语的适用范围而非扩张技能库；LIBERO-Pro +38.6pp。

### [群体学习 / Fleet Learning | Fleet Learning](#论文清单)

检索关键词：`fleet learning robotics / shared robot experience / collective robot learning`　代表工作：LWD, RoboOS　（6 篇）

1. **⭐RoboOS: A Hierarchical Embodied Framework for Cross-Embodiment and Multi-Agent Collaboration.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.03673) [code](https://github.com/FlagOpen/RoboOS)

    *Huajie Tan, Xiaoshuai Hao, Cheng Chi, Minglan Lin, Yaoxu Lyu, Mingyu Cao, Dong Liang, Zhuo Chen, Mengsi Lyu, Cheng Peng, Chenrui He, Yulong Ao, Yonghua Lin, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang*

    > Brain-Cerebellum 架构：Embodied Brain + Cerebellum Skill Library + Real-Time Shared Memory，边云通信。

2. **ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.19349)

    *Robert Tjarko Lange, Yuki Imajuku, Edoardo Cetin*

    > 开放式、样本高效的程序演化：新颖性拒绝采样与多模型集成；本报告建议用其去重机制缓解机器人集群的假设重复。

3. **⭐RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration.** arXiv, 2025. [paper](https://arxiv.org/abs/2510.26536) [code](https://flagopen.github.io/RoboOS/)

    *Huajie Tan, Cheng Chi, Xiansheng Chen, Yuheng Ji, Zhongxia Zhao, Xiaoshuai Hao, Yaoxu Lyu, Mingyu Cao, Junkai Zhao, Huaihai Lyu, Enshen Zhou, Ning Chen, Yankai Fu, Cheng Peng, Wei Guo, Dong Liang, Zhuo Chen, Mengsi Lyu, Chenrui He, Yulong Ao, Yonghua Lin, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang*

    > Spatio-Temporal-Embodiment Memory 统一多机器人终身协作的共享记忆。

4. **Federated Single-Agent Robotics: Multi-Robot Coordination Without Intra-Robot Multi-Agent Fragmentation.** arXiv, 2026. [paper](https://arxiv.org/abs/2604.11028) [code](https://github.com/s20sc/fsar-fleet-coordination)

    *Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li*

    > 多机器人协调不需要机器人内部多 agent 碎片化，联邦式 fleet runtime。

5. **⭐Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.00416)

    *Yi Wang, Xinchen Li, Pengwei Xie, Pu Yang, Buqing Nie, Yunuo Cai, Qinglin Zhang, Chendi Qu, Jeffrey Wu, Jianheng Song, Xinlin Ren, Jingshun Huang, Mingjie Pan, Siyuan Feng, Zhi Chen, Jianlan Luo*

    > 16 台双臂机器人 fleet-scale 离线到在线 RL 持续后训练通用 VLA（DIVL + QAM），8 个真实任务平均 95%。

6. **⭐ENPIRE: Agentic Robot Policy Self-Improvement in the Real World.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19980)

    *Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi*

    > coding agent 的真机 harness：EN（自动 reset+验证）/ PI / R（多机并行 rollout）/ E（读日志改算法与基础设施），自主训练策略至 99% 成功。

### [主动感知 | Active Perception](#论文清单)

检索关键词：`active perception robot agent / VLM active perception manipulation`　代表工作：AgenticLab, PhysCaP, ActiveVLA　（6 篇）

1. **Real2Sim via Active Perception with Behavior Trees Automatically Generated by VLMs.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.08454)

    *Alessandro Adami, Sebastian Zudaire, Ruggero Carli, Pietro Falco*

    > VLM 生成行为树主动获取缺失物理参数。

2. **ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.08325)

    *Zhenyang Liu, Yongchong Gu, Yikai Wang, Xiangyang Xue, Yanwei Fu*

    > 关键区域定位 + 主动视点选择与 3D 放大。

3. **⭐PLanAR: Planning-Language-Grounded Agentic Reasoning for Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.01662) [code](https://agentic1ab.github.io/)

    *Pengyuan Guo, Zhonghao Mai, Zhengtong Xu, Kaidi Zhang, Quan Khanh Luu, Heng Zhang, Zichen Miao, Arash Ajoudani, Zachary Kingston, Qiang Qiu, Yu She*

    > Purdue 真机 agent 平台：以规划语言（谓词/动作 schema）定义 VLM 推理空间，逐步验证符号效果并重规划。

4. **⭐CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.22435)

    *Letian Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Dantong Niu, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi "Jim" Fan*

    > CaP-Gym / CaP-Bench / CaP-Agent0 / CaP-RL 四件套；抽象降低时性能下降，可用 agentic test-time compute 弥补；RL with verifiable reward 可 sim2real。

5. **Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.31200)

    *Tao Chen, Lizheng Liu, Jiaxu Wang, Ziyue Jiang, Ruiqi Tian, JiGuang Huo, Zhongxue Gan*

    > affordance 感知检索 + 场景图约束 + 14 类失败分类的自反思抓取。

6. **PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.21031) [code](https://physcap.github.io)

    *Chen-Yu Lin, Jing-Wen Chen, Hsueh-En Chang, Hung-An Chen, Sheng-Hsun Chang, Chi-Pin Huang, Fu-En Yang, Min-Hung Chen, Yi-Ting Chen, Yu-Chiang Frank Wang, Shao-Hua Sun*

    > 物理信息驱动的主动探索层：从本体感知估计质量/刚度，Planner+Prioritizer 决定何时探索。

### [验证器 / 成功验证 | Verifier / Success Verification](#论文清单)

检索关键词：`robot verifier agent / semantic verification robotics / precondition postcondition VLM`　代表工作：Harness VLA, PhyAgentOS, REMAC　（23 篇）

1. **Let's Verify Step by Step.** ICLR 2024, 2023. [paper](https://arxiv.org/abs/2305.20050)

    *Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe*

    > 过程奖励模型：逐步标出推理出错位置而非只看最终答案，为 RSI 提供细粒度评价信号。

2. **Self-Rewarding Language Models.** arXiv, 2024. [paper](https://arxiv.org/abs/2401.10020)

    *Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, Jason Weston*

    > 模型用 LLM-as-a-Judge 给自己的回答打分并做 DPO，回答与评价能力同时迭代。

3. **Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge.** arXiv, 2024. [paper](https://arxiv.org/abs/2407.19594)

    *Tianhao Wu, Weizhe Yuan, Olga Golovneva, Jing Xu, Yuandong Tian, Jiantao Jiao, Jason Weston, Sainbayar Sukhbaatar*

    > 同一模型既当回答者、评审者和“评审的评审”，评价能力本身自改进；四轮后 AlpacaEval 2 LC 胜率 22.9%→39.4%。

4. **⭐REMAC: Self-Reflective and Self-Evolving Multi-Agent Collaboration for Long-Horizon Robot Manipulation.** arXiv, 2025. [paper](https://arxiv.org/abs/2503.22122)

    *Puzhen Yuan, Angyuan Ma, Yunchao Yao, Huaxiu Yao, Masayoshi Tomizuka, Mingyu Ding*

    > 多机器人长程规划：前置/后置条件检查的自反思 + 场景推理的自进化，成功率 +40%，效率 +52.7%。

5. **⭐Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.23450) [code](https://agentic-robot.github.io)

    *Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue Yan, Dingjie Song, Yinuo Liu, Yuting Li, Yu Zhang, Pan Zhou, Hechang Chen, Lichao Sun*

    > 脑启发框架：Standardized Action Procedure 协调推理模型 / VLA 执行器 / 时序验证器，LIBERO 79.6%。

6. **SENTINEL: A Multi-Level Formal Framework for Safety Evaluation of Foundation Model-based Embodied Agents.** arXiv, 2025. [paper](https://arxiv.org/abs/2510.12985)

    *Simon Sinong Zhan, Philip Wang, Yao Liu, Yiyan Peng, Zinan Wang, Qineng Wang, Zhian Ruan, Xiangyu Shi, Xinyu Cao, Frank Yang, Zhenyang Ni, Kangrui Wang, Ruohan Zhang, Huajie Shao, Manling Li, Qi Zhu*

    > 语义/计划/轨迹三层时序逻辑形式化安全评估。

7. **Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning.** NeurIPS 2025 Spotlight, 2025. [paper](https://arxiv.org/abs/2510.21302)

    *Sanghyun Ahn, Wonje Choi, Junyong Lee, Jinwoo Park, Honguk Woo*

    > NeurIPS 2025 Spotlight：符号验证 + 交互式验证代码，成功率比 CaP +46.2%。

8. **⭐PLanAR: Planning-Language-Grounded Agentic Reasoning for Robot Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2602.01662) [code](https://agentic1ab.github.io/)

    *Pengyuan Guo, Zhonghao Mai, Zhengtong Xu, Kaidi Zhang, Quan Khanh Luu, Heng Zhang, Zichen Miao, Arash Ajoudani, Zachary Kingston, Qiang Qiu, Yu She*

    > Purdue 真机 agent 平台：以规划语言（谓词/动作 schema）定义 VLM 推理空间，逐步验证符号效果并重规划。

9. **⭐From Passive Observer to Active Critic: Reinforcement Learning Elicits Process Reasoning for Robotic Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.15600)

    *Yibin Liu, Yaxing Lyu, Daqi Gao, Zhixuan Liang, Weiliang Tang, Shilong Mu, Xiaokang Yang, Yao Mu*

    > 7B 视频 MLLM 从“观察者”变“批评者”：以初始 / 当前画面锚定过程视频，RL 激励显式 CoT 估计进度与失败位置；RoboFail 失败检测 67%。

10. **PerceptTwin: Semantic Scene Reconstruction for Iterative LLM Planning and Verification.** ICRA 2026, 2026. [paper](https://arxiv.org/abs/2606.04226)

    *Charlie Gauthier, Sacha Morin, Liam Paull*

    > ICRA 2026：从感知栈自动构建交互仿真以验证与精炼计划，成功率 +39%。

11. **VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.05395)

    *Yunhao Yang, Neel P. Bhatt, Kevin Wang, Samuel Tetteh, Zhangyang Wang, Ufuk Topcu*

    > 形式化可验证的自进化技能契约：模型检查反例变成文本梯度，97.2% 规范符合。

12. **⭐Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.18247) [code](https://veritas-improvement.github.io/)

    *Mingtong Zhang, Dhruv Shah*

    > 生成器-验证器框架：冻结通用策略 + 无梯度视觉验证器做推理时引导，验证过的自生成轨迹再微调策略；50 条自主轨迹 70% vs 同量人工示范 65%。

13. **PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.27146)

    *Jiayu Yang, Tao Yang, Weijun Li, Xiang Chang, Fei Chao, Changjing Shang, Qiang Shen*

    > 可行性算子 + 动作解释算子 + LLM 反思模块的执行期可靠性框架。

14. **Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.30686)

    *Taozhao Chen, Ian Manchester, Huaming Chen*

    > 成功率无法区分语义匹配与物理泛化，需受控变量评测设计。

15. **LLM-as-a-Verifier: A General-Purpose Verification Framework.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.05391) [code](https://llm-as-a-verifier.com)

    *Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini*

    > 对评分 token logits 取期望得到连续分数，RoboRewardBench 87.4%，可作 RL 密集奖励。

16. **⭐Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.08448) [code](https://github.com/RLinf/RPent)

    *Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, Zhengru Fang, Yi Nie, Changxu Wei, Yu Wang, Wenbo Ding, Chao Yu*

    > 把冻结 VLA 暴露为可重试的接触原语，与少量解析原语组合；从执行轨迹学习原语的适用范围而非扩张技能库；LIBERO-Pro +38.6pp。

17. **⭐PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.16636)

    *Yang Liu, Weixing Chen, Xinshuai Song, Tao Pu, Siwen Mo, Yongjie Bai, Zihao Chen, Qianran Sun, Liruo Zhong, Ying Shen, Liang Lin*

    > 会话为最小调度单元的运行时：State-as-a-File、SessionVerifier 区分执行终止与语义完成、epistemic memory、分层安全；19+ 本体验证。

18. **Towards the Harness of Embodied Agents.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.11246) [code](https://eit-hai.github.io/thea)

    *Qi Wang, Tianyi Wang, Chengyang Li, Shikun Ban, Yurun Chen, Yizhong Ge, Jason Qin, Chengtai Li, Wentao Zhu*

    > 继承 coding agent 组件，补上物理世界缺的两件事：Scene Graph as Context 与 Evaluation as Exit Codes。

19. **Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.09857)

    *Rohan Bhagra, Mahantesh Halapannavar, Uddhav Bhattarai*

    > 规划与执行之间的 LLM-as-a-Judge 集成验证层，接受/拒绝/升级人工，对抗攻击 97% 拦截。

20. **Consilience for Verifier-Free Test-Time Scaling.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.09898)

    *Lecheng Kong, Like Hui, Haitao Mao, Jun Huan*

    > 无验证器测试时扩展：置信度轨迹的时间不对称性。

21. **ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.13438)

    *Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi*

    > 潜空间世界模型的接触前执行监控。

22. **Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.16889)

    *Bingxin Xu, Yuzhang Shang, Emilio Ferrara*

    > 以子任务为探索单元（成本 T·K 而非 T^K），转移感知记忆治理 VLA 的进入条件。

23. **AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.29537)

    *Hongbo Gao, Zeyu Ni, Xin Wen, Siyu Xu, Ruifeng Li*

    > 成就接地记忆：只有物理证据验证子目标后才推进进度指针；可靠记忆取决于状态更新纪律而非容量。

### [Robot RSI：递归自我改进 | Robot RSI: Recursive Self-Improvement](#论文清单)

检索关键词：`recursive self-improvement robot / deployment-time self-evolution / training-time self-iteration / self-evaluation verifier / auto research robotics / human-on-the-loop`　代表工作：ENPIRE, ASPIRE, RoboHarness, RoboClaw, PRIMO R1, VERITAS, Eureka, DrEureka, Reflexion, STaR, Let's Verify Step by Step, Meta-Rewarding LMs, The AI Scientist　（47 篇）

1. **Speculations Concerning the First Ultraintelligent Machine.** Advances in Computers 6:31-88, 1965. [paper](https://doi.org/10.1016/S0065-2458(08)60418-0)

    *Irving John Good*

    > 1965 年的“智能爆炸”设想：能设计出更强机器的机器会让新机器继续参与下一代设计；RSI 概念的源头。

2. **Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements.** arXiv, 2003. [paper](https://arxiv.org/abs/cs/0309048)

    *Jürgen Schmidhuber*

    > 自我改写的形式化起点：只有能证明某项修改会提高既定效用时才执行修改。

3. **Recursive Self-Improvement.** LessWrong, 2008. [paper](https://www.lesswrong.com/posts/JBadX7rwdcRFzGuju/recursive-self-improvement)

    *Eliezer Yudkowsky*

    > 2008 年对递归自我改进的系统论述，Lil'Log 与具身纪元文章均以其为概念参照。

4. **STaR: Bootstrapping Reasoning With Reasoning.** NeurIPS 2022, 2022. [paper](https://arxiv.org/abs/2203.14465)

    *Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman*

    > 训练时自迭代：生成推理 → 答对保留、答错看答案重推 → 筛出的过程微调下一版模型。

5. **Reflexion: Language Agents with Verbal Reinforcement Learning.** NeurIPS 2023, 2023. [paper](https://arxiv.org/abs/2303.11366) [code](https://github.com/noahshinn/reflexion)

    *Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao*

    > 部署时的记忆自改进：把测试 / 环境反馈写成反思存进记忆再重试，不更新权重；HumanEval 91%。

6. **Emergent autonomous scientific research capabilities of large language models.** arXiv, 2023. [paper](https://arxiv.org/abs/2304.05332)

    *Daniil A. Boiko, Robert MacKnight, Gabe Gomes*

    > LLM 驾驭实验室自动化（含云实验室）做科学实验的早期案例。

7. **Let's Verify Step by Step.** ICLR 2024, 2023. [paper](https://arxiv.org/abs/2305.20050)

    *Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe*

    > 过程奖励模型：逐步标出推理出错位置而非只看最终答案，为 RSI 提供细粒度评价信号。

8. **Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation.** arXiv, 2023. [paper](https://arxiv.org/abs/2310.02304)

    *Eric Zelikman, Eliana Lorch, Lester Mackey, Adam Tauman Kalai*

    > 自学优化器：优化 improver 而非解本身；弱模型下会退化。

9. **⭐Eureka: Human-Level Reward Design via Coding Large Language Models.** ICLR 2024, 2023. [paper](https://arxiv.org/abs/2310.12931) [code](https://eureka-research.github.io)

    *Yecheng Jason Ma, William Liang, Guanzhi Wang, De-An Huang, Osbert Bastani, Dinesh Jayaraman, Yuke Zhu, Linxi Fan, Anima Anandkumar*

    > LLM 编写奖励函数、RL 学策略、结果反馈回 LLM 改奖励；83% 任务超过人工奖励；训练方法的自动搜索。

10. **Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models.** ICML 2024, 2024. [paper](https://arxiv.org/abs/2401.01335)

    *Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, Quanquan Gu*

    > 弱模型通过与自己历史版本博弈变强，无需额外人类数据。

11. **Self-Rewarding Language Models.** arXiv, 2024. [paper](https://arxiv.org/abs/2401.10020)

    *Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, Jason Weston*

    > 模型用 LLM-as-a-Judge 给自己的回答打分并做 DPO，回答与评价能力同时迭代。

12. **⭐DrEureka: Language Model Guided Sim-To-Real Transfer.** RSS 2024, 2024. [paper](https://arxiv.org/abs/2406.01967) [code](https://eureka-research.github.io/dr-eureka/)

    *Yecheng Jason Ma, William Liang, Hung-Ju Wang, Sam Wang, Yuke Zhu, Linxi Fan, Osbert Bastani, Dinesh Jayaraman*

    > LLM 同时写奖励与域随机化参数范围（摩擦、质量、外力），四足机器人仿真学会站瑜伽球并迁移真机；自动研究推进到 sim-to-real。

13. **Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge.** arXiv, 2024. [paper](https://arxiv.org/abs/2407.19594)

    *Tianhao Wu, Weizhe Yuan, Olga Golovneva, Jing Xu, Yuandong Tian, Jiantao Jiao, Jason Weston, Sainbayar Sukhbaatar*

    > 同一模型既当回答者、评审者和“评审的评审”，评价能力本身自改进；四轮后 AlpacaEval 2 LC 胜率 22.9%→39.4%。

14. **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery.** arXiv, 2024. [paper](https://arxiv.org/abs/2408.06292) [code](https://github.com/SakanaAI/AI-Scientist)

    *Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha*

    > 自动研究：从代码模板出发提想法、查新颖性、改代码、跑实验、写论文并接受自动评审。

15. **CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark.** TMLR 2024, 2024. [paper](https://arxiv.org/abs/2409.11363)

    *Zachary S. Siegel, Sayash Kapoor, Nitya Nadgir, Benedikt Stroebl, Arvind Narayanan*

    > 计算可复现性 agent 基准（TMLR 2024）。

16. **ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery.** ICLR 2025, 2024. [paper](https://arxiv.org/abs/2410.05080)

    *Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns, Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, Huan Sun*

    > 数据驱动科学发现任务上的语言 agent 严格评测（ICLR 2025）。

17. **MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering.** arXiv, 2024. [paper](https://arxiv.org/abs/2410.07095)

    *Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mądry*

    > 在 Kaggle 式机器学习工程任务上评测 agent。

18. **RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts.** ICML 2025, 2024. [paper](https://arxiv.org/abs/2411.15114)

    *Hjalmar Wijk, Tao Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael Chen, Josh Clymer, Jai Dhyani, Elena Ericheva, Katharyn Garcia, Brian Goodrich, Nikola Jurkovic, Holden Karnofsky, Megan Kinniment, Aron Lajko, Seraphina Nix, Lucas Sato, William Saunders, Maksym Taran, Ben West, Elizabeth Barnes*

    > 对比前沿 agent 与人类专家的 AI R&D 能力（ICML 2025）。

19. **KernelBench: Can LLMs Write Efficient GPU Kernels?.** arXiv, 2025. [paper](https://arxiv.org/abs/2502.10517)

    *Anne Ouyang, Simon Guo, Simran Arora, Alex L. Zhang, William Hu, Christopher Ré, Azalia Mirhoseini*

    > LLM 能否写出高效 GPU kernel 的基准，harness 演化常用的可验证任务。

20. **PaperBench: Evaluating AI's Ability to Replicate AI Research.** ICML 2025, 2025. [paper](https://arxiv.org/abs/2504.01848)

    *Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, Tejal Patwardhan*

    > 评测 AI 复现 AI 研究论文的能力（ICML 2025）。

21. **Absolute Zero: Reinforced Self-play Reasoning with Zero Data.** arXiv, 2025. [paper](https://arxiv.org/abs/2505.03335)

    *Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Yang Yue, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, Gao Huang*

    > 零数据自博弈推理：模型自己提出可验证任务并求解，训练时自迭代的极端形式。

22. **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents.** arXiv 2025, 2025. [paper](https://arxiv.org/abs/2505.22954)

    *Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune*

    > 允许 coding agent 修改自身 harness 代码库并开放式演化，SWE-bench 20%→50%。

23. **ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution.** arXiv, 2025. [paper](https://arxiv.org/abs/2509.19349)

    *Robert Tjarko Lange, Yuki Imajuku, Edoardo Cetin*

    > 开放式、样本高效的程序演化：新颖性拒绝采样与多模型集成；本报告建议用其去重机制缓解机器人集群的假设重复。

24. **Early science acceleration experiments with GPT-5.** arXiv, 2025. [paper](https://arxiv.org/abs/2511.16072)

    *Sébastien Bubeck, Christian Coester, Ronen Eldan, Timothy Gowers, Yin Tat Lee, Alexandru Lupsasca, Mehtaab Sawhney, Robert Scherrer, Mark Sellke, Brian K. Spears, Derya Unutmaz, Kevin Weil, Steven Yin, Nikita Zhivotovskiy*

    > 前沿模型加速科研的早期实证案例集。

25. **ThetaEvolve: Test-time Learning on Open Problems.** arXiv, 2025. [paper](https://arxiv.org/abs/2511.23473)

    *Yiping Wang, Shao-Rong Su, Zhiyuan Zeng, Eva Xu, Liliang Ren, Xinyu Yang, Zeyi Huang, Xuehai He, Luyao Ma, Baolin Peng, Hao Cheng, Pengcheng He, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, Yelong Shen*

    > 面向开放问题的测试时学习：在演化搜索中同时更新模型。

26. **BigBang: Pursuing Open-Ended Intelligence through Self-Evolving Synthesis of Verifiable Frontier Tasks.** Technical report, 2026. [paper](https://endlessfrontier.tech/assets/paper.pdf) [code](https://huggingface.co/endless-frontier/BigBang-v1)

    *The BigBang Team (Endless Frontier)*

    > 出题者 / 批评者 / 元批评者三角合成可验证难题，约一万条样本更新权重；训练时自迭代 + 评价器校准，证据来自团队技术报告。

27. **Towards end-to-end automation of AI research.** Nature 651:914-919, 2026. [paper](https://www.nature.com/articles/s41586-026-10265-5)

    *Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha*

    > The AI Scientist 路线在 Nature 上的正式发表：从想法到论文与评审的端到端自动化。

28. **Why LLMs Aren't Scientists Yet: Lessons from Four Autonomous Research Attempts.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.03315)

    *Dhruv Trehan, Paras Chopra*

    > 四次自主研究尝试总结出的 6 类失败模式（训练数据默认偏置、实现漂移、记忆退化、过度乐观等）。

29. **Learning to Discover at Test Time.** arXiv, 2026. [paper](https://arxiv.org/abs/2601.16175)

    *Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, Yu Sun*

    > 测试时发现：让模型在推理时对开放问题持续搜索与学习。

30. **⭐RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.11558) [code](https://github.com/RoboClaw-Robotics/RoboClaw)

    *Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang, Sukai Wang, Kongtao Hu, Minhui Yu, Bowen Jiang, Zhan Su, Jiayao Ma, Xin He, Yongjian Shen, Yang Yang, Guanghui Ren, Maoqing Yao, Wenhao Wang, Yao Mu*

    > 统一采集-学习-部署的 VLM 控制器；Entangled Action Pairs 把正向技能与逆向恢复绑定实现自复位采数据，成功率 +25%，人工时间 -53.7%。

31. **⭐From Passive Observer to Active Critic: Reinforcement Learning Elicits Process Reasoning for Robotic Manipulation.** arXiv, 2026. [paper](https://arxiv.org/abs/2603.15600)

    *Yibin Liu, Yaxing Lyu, Daqi Gao, Zhixuan Liang, Weiliang Tang, Shilong Mu, Xiaokang Yang, Yao Mu*

    > 7B 视频 MLLM 从“观察者”变“批评者”：以初始 / 当前画面锚定过程视频，RL 激励显式 CoT 估计进度与失败位置；RoboFail 失败检测 67%。

32. **Epistemic Uncertainty for Test-Time Discovery.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.11328)

    *Kainat Riaz, Muhammad Ahmed Mohsin, Ahsan Bilal, Muhammad Umer, Ayesha Mohsin, Aqib Riaz, Ali Subhan, John M. Cioffi*

    > 用认知不确定性引导测试时发现的搜索方向。

33. **ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.26340)

    *Rui Meng, Bhavana Dalvi Mishra, Jiefeng Chen, Chun-Liang Li, Palash Goyal, Mihir Parmar, Yiwen Song, Yale Song, Rajarishi Sinha, Parthasarathy Ranganathan, Burak Gokturk, Jinsung Yoon, Tomas Pfister*

    > 以证据链（chain-of-evidence）组织自主研究，面向人类水平的科研自动化。

34. **You Live More Than Once: Towards Hierarchical Skill Meta-Evolving.** arXiv, 2026. [paper](https://arxiv.org/abs/2605.28390)

    *Xujun Li, Kehan Zheng, Mingyuan Zhao, Yize Geng, Jinfeng Zhou, Qi Zhu, Fei Mi, Lifeng Shang, Minlie Huang, Hongning Wang*

    > 分层技能元进化：从执行轨迹学出“怎样生成与修改技能”的元技能并反过来整理技能库，MineDojo 0.700→0.856，底层权重不变。

35. **When AI builds itself: our progress toward recursive self-improvement, and its implications.** Anthropic Institute, 2026. [paper](https://www.anthropic.com/institute/recursive-self-improvement)

    *Anthropic*

    > Anthropic 对递归自我改进的路线判断：代码建议 → 编程智能体自改代码 → AI 参与设计与训练后继系统；具身智能可能紧随，但物理制造、实验周期与部署是新的速度瓶颈。

36. **⭐Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.18247) [code](https://veritas-improvement.github.io/)

    *Mingtong Zhang, Dhruv Shah*

    > 生成器-验证器框架：冻结通用策略 + 无梯度视觉验证器做推理时引导，验证过的自生成轨迹再微调策略；50 条自主轨迹 70% vs 同量人工示范 65%。

37. **⭐ENPIRE: Agentic Robot Policy Self-Improvement in the Real World.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.19980)

    *Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi*

    > coding agent 的真机 harness：EN（自动 reset+验证）/ PI / R（多机并行 rollout）/ E（读日志改算法与基础设施），自主训练策略至 99% 成功。

38. **Autodata: An agentic data scientist to create high quality synthetic data.** arXiv, 2026. [paper](https://arxiv.org/abs/2606.25996)

    *Ilia Kulikov, Chenxi Whitehouse, Tianhao Wu, Yixin Nie, Swarnadeep Saha, Eryk Helenowski, Weizhe Yuan, Olga Golovneva, Jack Lanchantin, Yoram Bachrach, Jakob Foerster, Xian Li, Han Fang, Sainbayar Sukhbaatar, Jason Weston*

    > 作为“数据科学家”的 agent，自动生成高质量合成数据。

39. **⭐ASPIRE: Agentic /Skills Discovery for Robotics.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.00272) [code](https://research.nvidia.com/labs/gear/aspire/)

    *Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi "Jim" Fan, Guanzhi Wang*

    > NVIDIA GEAR：执行引擎 + 技能库 + 演化搜索的持续学习系统，技能跨任务/仿真/真机/本体持久化，LIBERO-Pro Long 零样本 31% vs 4%。

40. **Anchored Self-Play for Code Repair.** ICML 2026, 2026. [paper](https://arxiv.org/abs/2607.03523)

    *Caroline Choi, Zeyneb Kaya, Shirley Wu, Tengyu Ma, Tatsunori Hashimoto, Ludwig Schmidt*

    > 带锚点的自博弈代码修复：出题者与修复者共同演化，锚定避免漂移（ICML 2026）。

41. **Harness Engineering for Self-Improvement.** Lil'Log, 2026. [paper](https://lilianweng.github.io/posts/2026-07-04-harness/) [code](https://lilianweng.github.io/posts/2026-07-04-harness/)

    *Lilian Weng*

    > 定义 Harness 三大模式（工作流自动化 / 文件系统即记忆 / 子代理），提出优化对象阶梯 prompt→context→workflow→harness code→optimizer code，列出 RSI 的 7 个未解挑战。

42. **RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning.** arXiv, 2026. [paper](https://arxiv.org/abs/2607.18060)

    *Jinbang Huang, Yuanzhao Hu, Zhiyuan Li, Ran Qi, Yixin Xiao, Zhanguang Zhang, Mark Coates, Tongtong Cao, Yingxue Zhang*

    > 多模态执行记忆刻画异构策略能力边界，Memory Bridge 把机器人引导到下一策略的分布内区域。

43. **Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence.** arXiv, 2026. [paper](https://arxiv.org/abs/2608.16590)

    *Xin Ding, Liang Mi, Mingzhe Huang, Zixuan Wang, Chao Zhang, Zixu Hao, Fu Chen, Xiangyu Li, Yikai Zheng, Yaoyu Guo, Weijun Wang, Kun Li, Hao Wu, Yunxin Liu, Ting Cao*

    > 三时间尺度闭环 harness：动作频率治理 / rollout 级 critic-recovery 提议 / 验证门控技能更新；LIBERO-Pro 90.8%，推理加速 11.1x。

44. **GPT-6 未必能当好机器人的大脑，却可能帮王兴兴加速 RobotRSI.** WeChat 公众号 具身纪元, 2026. [paper](https://mp.weixin.qq.com/s/DTj1be0CGhwcvaFh2WI0HA)

    *Marilyn Liu (具身纪元)*

    > 提出 Robot RSI 两条轴线：改进环节（部署时自演化 / 训练时自迭代 / 自我评估 / 自动研究）× 人的参与程度（in-the-loop / on-the-loop / closed loop）；判断前沿 LLM 更可能先成为 Robot RSI 的认知中枢而非末端控制器。

45. **A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference.** Machine Intelligence Research, 2026. [paper](https://arxiv.org/abs/2609.01679)

    *Shuaicheng Niu, Guohao Chen, Yaofo Chen, Zhiquan Wen, Jinwu Hu, Zeshuai Deng, Deyu Chen, Shuhai Zhang, Renjie Chen, Zihao Lian, Shoukai Xu, Gang Dai, Yunbei Zhang, Wei Luo, Yifan Zhang, Mingkui Tan, Cheng Deng*

    > 统一测试时适应/学习/扩展的反馈驱动 TTI 视角，覆盖机器人。

46. **GPT-6 Astra 开启 Robot RSI 时代! howto 实现.** 小红书, 2026. [paper](https://www.xiaohongshu.com/explore/6a9e3498000000002802d485)

    *♥VLA和RL的具身未来 (小红书)*

    > 具身纪元 Robot RSI 文章的小红书精简版：把 Robot RSI 压成一段话——执行 → 判断错在哪 → 智能体改代码与策略 → 仿真与真机验证 → 有效经验进入下一轮；结论是 GPT-6 更可能先成为制造下一代机器人能力的引擎。

47. **RoboCurve：GPT-6 Astra 直接控制机器人.** 知乎专栏, 2026. [paper](https://zhuanlan.zhihu.com/p/208031326825455257)

    *罗清雨 (知乎)*

    > RoboCurve 第三方测试：GPT-6 Astra 以 EEF waypoint 工具调用控制 YAM 双臂，block→bowl 19/20（2.5 min，2.1K tokens）而精密插入 10%；文章提出“接一个 flow head”的双系统设想。本仓库 notes/44 据此给出 Agent-as-Teleoperator 数据引擎方案。

## 统计

- 共 209 条：核心 ⭐ 46、扩展 94、基础 69。
- 按年份：1965 年 1 篇、2003 年 1 篇、2008 年 1 篇、2021 年 1 篇、2022 年 7 篇、2023 年 18 篇、2024 年 14 篇、2025 年 29 篇、2026 年 137 篇。
- 按主线：基础：LLM Agent 与 Harness 工程 71、Agent + Robot 总览 10、Coding Agent 控机器人 20、OpenClaw / ROS 生态 10、长程任务 11、机器人记忆 21、反思与纠错 15、自进化 21、技能库 16、VLA + RL 20、部署数据回流 9、数字孪生 / Sim2Real 9、世界模型 9、快慢双系统 15、端侧部署 / Edge Agent 11、Harness 15、Runtime 运行时 9、安全 15、标准接口 / Hardware API 5、多机器人协作 13、跨本体 5、群体学习 / Fleet Learning 6、主动感知 6、验证器 / 成功验证 23、Robot RSI：递归自我改进 47。

## 复现与贡献

仓库结构：

```
README.md              由 data/*.csv + data/header.md + data/footer.md 生成（src/generator.py），请勿手改
data/                  topics.csv（主线）· papers.csv（论文条目）· paper_meta.json（arXiv 元数据）· header.md / footer.md
docs/reports/          中英文报告 Markdown 与 PDF，LaTeX 头文件、pandoc Lua 过滤器与构建脚本
docs/slides/           HTML 幻灯片（index.html / index.pdf）与 Beamer 幻灯片（.tex / .pdf）
docs/proposal/         PROPOSAL_agent_data_engine_zh.md：HARVEST 数据引擎方案（合订本 Part H）
report/                survey_full_report.html / .pdf：全文合订本（scripts/build_full_report.py 生成）
insights/              10 趋势与洞察 · 11 研究机会清单 · 12 数字口径账本
notes/                 43 份深度解读（01-43），按 Part A-G 合订进全文报告
assets/                fig1_timeline.svg · fig2_taxonomy.svg（scripts/make_figures.py 生成）及幻灯片预览图
papers/pdf/            六篇核心论文原文；papers/pdf_zh/ 为 SuperTranslate 中文版（*.inspect.json 为 QA 报告）
papers/translations/   人工译文表，供 scripts/manual_translate.py 使用
sources/               五份源材料的转写与存档
scripts/               download_papers.sh · translate_papers.sh · manual_translate.py · export_slides_pdf.py · make_figures.py · build_full_report.py · build_docs.sh
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

# 重建总览图、两份报告、两套幻灯片与全文合订本（pandoc + XeLaTeX + Playwright/Chromium）
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
