---
title: "Agent × Robot：从 Harness 到自进化物理智能体"
subtitle: "四份材料的解读、23 条主线的 2026 综述与十条洞见"
author: "awesome_agentic_robot · asimfish"
date: "2026-09-06"
lang: zh-CN
---

# 导读

这份报告回答三个问题：2026 年 Agent × Robot 这条线上到底发生了什么；手头五份材料（一篇小红书长文、一份 Code-as-Policy 讲稿、一张 23 条主线的检索地图、Lilian Weng 的两篇博文、具身纪元关于 Robot RSI 的公众号文章）各自说对了什么、漏了什么；沿着这些主线往前看，哪些判断有论文证据支撑，哪些还只是预测。

结论先放在前面。

1. **优化对象在上移。** 2022 年的 Code as Policies 让 LLM 写一段策略代码；2026 年的 SkillOpt、ASPIRE、RHO、ENPIRE 让 coding agent 优化的对象变成技能文档、多文件策略仓库、训练配方和整套 harness。讲稿里的统一公式 $z_{t+1} = A(z_t, \tau_t, r_t, \log_t)$ 抓住了这个变化：被学习的东西 $z$ 从动作变成了“外部可训练产物”。
2. **“冻结 VLA + 外围学习”成了 2026 年的默认范式。** Harness VLA、BATON、AGM、HyMeS、Zetta、SHAPER 全都不改 VLA 权重，而是在外面学 VLA 的适用范围、记忆管理规则、恢复技能和运行时 critic。原因很实际：权重更新贵、慢、难验证。但这条路有天花板，LWD、Q-Planning、TEMPO、Temporal GRPO 说明真实反馈最终还要写回策略权重。
3. **验证器是新的瓶颈，也是新的 scaling 轴。** PhyAgentOS 的 SessionVerifier、Thea 的 Evaluation as Exit Codes、AGM 的“物理证据才能推进进度指针”、LLM-as-a-Verifier 把验证当作可扩展维度，以及那篇立场论文“成功率无法证明 VLA 在做物理推理”，都指向同一件事：能不能自进化，取决于能不能可靠地判断“这一步到底成没成”。
4. **Harness 从软件术语变成了机器人中间件问题。** 软件 Agent 的 harness 在工具调用边界介入；机器人的 harness 必须同时在控制、计算、通信三处介入（Harness Engineering for Physical AI），必须知道模型最大延迟、技能 deadline 和断网后的 fallback（小红书长文的 Real-time-aware Harness）。这不再是 prompt 工程，而是 OS 与实时系统设计。
5. **群体是经验规模化的唯一出路，但收益不是线性的。** LWD 用 16 台双臂机器人把单一 VLA 推到 95%；ENPIRE 用 8 个工位把收敛时间从 5 小时压到 2 小时——8 倍机器人换来 2-3 倍加速，多出来的是假设吞吐量，不是 rollout 数量。
6. **Robot RSI 是把这些串起来的框架。** 具身纪元文章的两条轴线（改进的环节：部署时自演化 / 训练时自迭代 / 自我评估 / 自动研究 × 人的参与程度）把 ENPIRE、ASPIRE、RoboHarness、RoboClaw、PRIMO R1、VERITAS、Eureka、DrEureka 与软件侧的 Reflexion、STaR、Let's Verify、Meta-Rewarding、The AI Scientist 放进同一张表；前沿 LLM 更可能先成为机器人研发循环的认知中枢，而不是机器人的末端控制器。

阅读路径：只想知道结论看第 7、8 章；想核对每条主线的论文看第 4 章和附录；想看五份材料各自的解读看第 2、3、5、6 章。仓库根目录的 `README.md` 是按主线组织的 169 篇论文清单，`data/papers.csv` 是机器可读版本。

# 1. 材料、方法与边界

## 1.1 四份输入

| 材料 | 形态 | 核心主张 |
|---|---|---|
| 《Harness 只是开始：Agent+Robot 真正值得关注的 6 个下一站》，具身RL日记，小红书，39 张图文卡片 | 观点长文 | Harness 解决“Agent 怎样稳定使用已有能力”；下一步是 Memory、Reflection & Evolution、双时间尺度、Agent+VLA+RL、Real→Sim→Learn→Real、Multi-Robot；终局是 System Scaling + Experience Scaling |
| Code-as-Policy 讲稿（25 页 PPTX） | 论文精读讲稿 | 从 Code as Policies 到 SkillOpt、CaP-X、ASPIRE、ENPIRE，自进化 = 优化外部产物 $z$ |
| 《Agent + Robot 论文检索地图》，两页表格 | 检索框架 | 23 条主线，每条给检索词与代表工作 |
| Lil'Log：《LLM Powered Autonomous Agents》(2023.06)、《Harness Engineering for Self-Improvement》(2026.07) | 软件侧综述 | Agent = Planning + Memory + Tool use；Harness 三模式、优化阶梯、RSI 七个挑战 |
| 《GPT-6 未必能当好机器人的大脑，却可能帮王兴兴加速 RobotRSI》，Marilyn Liu，公众号具身纪元 | 观点长文 | RSI 两条轴线（改进环节 × 人的参与程度）；LLM 更可能先成为 Robot RSI 的认知中枢；Robot RSI 缺一个可重复、可扩展的虚拟世界 |

## 1.2 方法

我们把地图上 23 条主线的代表工作和长文、讲稿点名的全部工作逐一在 arXiv 上核实（标题、作者、日期、摘要），再沿每条主线按提交时间倒序检索 2025-2026 的新工作，最终保留 169 条：46 条是材料点名的机器人侧核心工作，94 条是扩展检索到的 2025-2026 新工作，29 条是软件侧 Agent / Harness / RSI 的基础工作（其中具身纪元文章点名的 Reflexion、STaR、Let's Verify Step by Step、Meta-Rewarding、The AI Scientist、HiSME、BigBang-V1、Gödel Machine、Anthropic《When AI builds itself》归入此类）。地图与文章上的非 arXiv 条目也做了溯源：BigBang-V1 是 Endless Frontier 的技术报告；PRIMO R1 对应 arXiv 2603.15600《From Passive Observer to Active Critic》；VERITAS 对应 arXiv 2606.18247《Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement》；HiSME 对应 arXiv 2605.28390《You Live More Than Once》；AgenticLab 对应 arXiv 2602.01662（v1 题为 PLanAR，Purdue）；MHS 是 Anthropic 2026 年 8 月 27 日发布的 Model Hardware Standard 研究预览；OpenClawPi 是松灵机器人（AgileX）面向 OpenClaw 的技能库，不是论文。

所有对论文的陈述都以摘要和材料原文为依据；报告区分“论文报告的数字”与“我们的判断”。

## 1.3 边界

机器翻译环节受本机条件限制：SuperTranslate 引擎需要 LLM API，本机所有 key 均不可用，因此五篇核心论文的中文版走的是引擎的手工翻译通路（`export` 导出文本块，译文由人工填入，`cache-only` 模式原位回填并跑 `inspect` QA）。Code as Policies 完成了正文全文翻译，其余四篇翻译了首页（标题、摘要、引言开头）。`scripts/translate_papers.sh` 可在配置 API key 后一键补全。

# 2. 解读一：《Harness 之后，Agent+Robot 下一站是什么？》

这篇长文的价值在于它给出了一个可检验的框架，而不只是一组新名词。作者的起点是一个反常识判断：VLA、WAM、Agent、Harness 不是相互替代的概念，而是在拼装同一台机器人系统。下面按六个“下一站”逐条对照论文。

## 2.1 Memory：机器人没有“过去”

长文的诊断准确：传统 VLA 的输入是当前图像 + 当前指令 + 当前本体状态，长程任务的核心变量因此从 State 变成 History。它点名的两篇论文数据都对得上。

- RoboMME（ICML 2026）用 16 个操作任务、时间/空间/物体/程序四类记忆的分类，在 π0.5 上系统比较了 14 种记忆变体，结论是记忆表示的有效性高度依赖任务，没有一种设计全面占优。后续的 RoboMME-Interference 进一步发现：感知型记忆在没有干扰时最好，但随着无关会话累积而稳定衰减；子目标型记忆提升较小但更抗干扰；加一个按视觉相似度检索历史片段的步骤能在每个干扰级别上恢复无干扰时的成功率。
- PonderPounce（2026.08）不设计专门的记忆模块，而是让一个 System 2 的 MLLM（Ponder）在原生因果上下文里累积整段 episode 的观测、示范和先前认知，再异步地只把最新的一个认知 token 及其“年龄”发给 System 1 的 VLA（Pounce）。RoboMME 上 9B 版本 60.83%，0.8B 版本 50.04%，对比当前观测 π0.5 的 17.93%；认知刷新 p50 延迟 78 ms，动作模型 25 ms，支持 20 Hz 播放。

长文预测机器人记忆会分化为 Working / Episodic / Semantic / Skill 四类。2026 年 6-8 月的论文恰好在这四条线上各有实例：AGM 用带进度指针的子目标序列做 working memory，且只有物理证据验证子目标完成后才推进指针（它的结论很硬——可靠的具身记忆靠的是状态更新纪律，不是记忆容量）；Analytic Concept-Centric Memory 用部件、参数模板、位姿、affordance 组织物体与场景记忆，并连接转移记忆和技能记忆；HyMeS 提出“技能在权重里、记忆在代码里”，让 coding agent 用启发式学习迭代一个可执行的记忆管理系统，RoboMemArena 任务成功率从 41.3% 提到 60.1%；ViReSkill 把验证过的计划存进技能记忆下次直接重放。

长文没有展开、但论文已经给出的一点：记忆可以放在 VLA 权重内部。NativeMEM 复用 VLA 自身的视觉编码器把每帧压成一个 token 追加到输入序列，成功率从 32.4% 提到 84.0%；LaMem-VLA 把短期/长期记忆库在 VLA 原生潜空间里交织；Remember Smarter 用 Mamba 压缩视觉历史加双曲经验空间，LIBERO-Plus 从 53.6% 到 70.6%。权重内记忆与权重外记忆现在是两条并行路线，第 7 章会讨论它们的分工。

## 2.2 Reflection：Retry 不等于 Learning

长文把“自进化”拆成 L1 Retry、L2 Replan、L3 Reflection、L4 Memory Evolution、L5 Skill Evolution、L6 Policy Evolution、L7 Fleet Evolution 七层，并判断 2026 年正从 L2/L3 快速向 L4-L7 延伸。这个分层是这篇长文最有用的贡献，因为它能直接给论文归位：

| 层级 | 代表工作 | 被更新的对象 |
|---|---|---|
| L1-L2 Retry / Replan | AgenticLab、Agentic Robot、MALMM、REMAC 的前置/后置条件检查 | 当前计划 |
| L3 Reflection | PhysReflect-VLA、Agentic RAG-VLM 的 14 类失败分类 | 下一步动作的纠正指令 |
| L4 Memory Evolution | Harness VLA 学冻结 VLA 的“使用说明书”、AGM、OnEvoMemory | 记忆与适用范围规则 |
| L5 Skill Evolution | ASPIRE、ViReSkill、PRACTICE、SkillGLoW、RATs 的玩耍式技能发现 | 技能库 |
| L6 Policy Evolution | LWD、Q-Planning、Z-1、TEMPO、Temporal GRPO | 策略权重 |
| L7 Fleet Evolution | LWD 的 16 台机器人、ENPIRE 的 8 工位、RoboOS-NeXT 的共享记忆 | 群体共享的数据与策略 |

长文对 Harness VLA 的概括值得强调：它不修改 VLA 权重，也不扩张技能库，而是从任务专属执行轨迹、全局成功规则和失败模型里学“这个 VLA 什么时候靠谱、什么时候先 MOVE_TO、什么时候重新 grounding、什么时候交给解析原语”。论文数字是 LIBERO-Pro +38.6 个百分点、RoboCasa365 +25.4 个百分点、RoboTwin C2R 58.4%。ASPIRE 的“经验复利”也有数字：LIBERO-90 上积累的技能库让 LIBERO-Pro Long 的零样本成功率随库规模单调上升，N=90 时达到 31%，对比先前方法 4%。

## 2.3 两个时间尺度：Agent 负责秒，Controller 负责毫秒

长文提出 Slow Loop（几百毫秒到数秒）和 Fast Loop（几十到几百 Hz）的划分，并引出 Fast-in-Slow（117.7 Hz）、StreamVLA（72% 时间步跳过自回归解码，延迟降 48%）、LaST0（潜空间时空 CoT，低频推理专家给高频动作专家提供物理表征）。这些数字与论文一致。

更重要的是它把这个划分接到了 Harness 上：Harness Engineering for Physical AI 那篇短文说，软件 harness 在工具调用边界介入，机器人 harness 必须同时在控制、计算、通信三处介入，因为学习策略的输出同时改变轨迹、日程和带宽；它提出三个缺失的强制功能——Projection（在输出处约束动作）、Isolation（限定推理的执行与传输时隙）、Transfer（检查失败时回退到经过验证的基线），并建议把它们做成 ROS 2 Harness Profile。长文由此提出的原则“Cloud can think. Edge must survive.”有 2026 年的系统论文支撑：CloudEdgeVLA 在 40 步统一延迟窗口下仍保持 63.8-78.0% 成功率，而对比方法最高 6.4%；EcoVLA 在 20 Hz 约束下把端-边协同的能效提高 236%；ARLI 说明推理延迟会破坏 RL 依赖的马尔可夫假设，需要状态增广才能在延迟下微调。

## 2.4 Agent + VLA + RL：最终还是要写回权重

长文举的例子是插 USB：第一次偏 3 mm，Agent 可以记一条“下次向左修正一点”放进技能，但视觉特征、接触状态、力反馈、微动作之间的连续关系最终属于策略权重。这个判断有实证：LWD 用 16 台双臂机器人、8 个真实任务，从预训练 VLA 出发做 fleet-scale 离线到在线 RL，单一通用策略随群体经验积累提升到平均 95%，长程任务提升最大；Q-Planning 给大 BC 策略配一个小的 off-policy Q 函数，只微调 Q 就能从部署失败里学，真机 stack-cups 从 40% 到 90%、insert-wallet 从 25% 到 80%，而只用成功 rollout 做 SFT 分别停在 55% 和 30%。

长文对 CaP-X 的评价——重点不是“代码打败 VLA”，而是 agentic test-time compute + 环境反馈 + RL 开始结合——与论文自述一致。对 RoboClaw 的 EAP（把正向技能与逆向恢复技能绑定实现自复位采数据，成功率 +25%、人工时间 -53.7%）的评价也成立，而且它点出了一个常被忽略的成本结构：机器人 RL 最贵的是人，不是 GPU。ENPIRE 的 EN 模块（自动重置 + 验证）解决的是同一个问题。

## 2.5 Real → Sim → Learn → Verify → Real

长文说 Sim 的角色是安全测试环境，是 Physical Agent 的 sandbox，而不是回到“全部在仿真里训练”。TwinRL 的流程与此吻合：手机拍摄重建数字孪生，SFT 阶段扩展轨迹分布支撑，twin 内并行 RL 预热真机 RL 并定位易失败配置，四个任务上接近 100% 成功且只用 20 分钟真机交互。2026 年这条线上新增了一批“把真实场景变成可交互仿真”的工具：RoboSnap 从单张 RGB 图生成可交互场景并发布 DROID-Sim（564 个场景）；Agentic Real2Sim 让 VLM agent 把真实交互录像转成可仿真的 episodic twin；PerceptTwin 从机器人感知栈自动构建交互仿真来验证与精炼计划，把 GPT-5 系列规划器的计划成功率平均提高约 39%；SafeDojo 在交互式视频世界模型上做带安全约束的 RL。世界模型在这里的角色确实如长文所说——是“脑内预演”的地方，而不只是动作预测器。

## 2.6 Multi-Robot：大规模进化不该发生在一台机器人身上

长文的 Shared Skill / Shared Experience / Shared World Knowledge / Shared Policy Improvement 四层共享，目前论文覆盖的是两端：RoboOS-NeXT 的 Spatio-Temporal-Embodiment Memory 做共享的时空-本体记忆；LWD 做共享的策略改进。中间两层（共享经验、共享世界知识）还没有系统性的论文，MeCo 的相似任务记忆化和 FSAR 的联邦式能力注册表算是雏形。长文估算的“100 万台机器人 × 每天 100 次任务 = 1 亿次物理交互/天”是推演，不是数据。

值得补充的是安全侧：多机器人 LLM 系统的通信攻击在 DMAS/HMAS 三种架构下都能把不安全信息变成不安全动作（最高 97.8% 不安全动作成功率），Claim Provenance and Verification Gate 能把违规率从 70.0% 降到 36.6%。群体共享经验意味着一个被污染的经验会被整个群体继承，这是长文没有讨论的风险。

## 2.7 评价

这篇长文的六个判断里，Memory、Reflection 分层、双时间尺度、Sim-as-sandbox 四条已有 2026 年论文实证；Agent+VLA+RL 的分工有 LWD 和 Q-Planning 两个强证据；Fleet 的中间层仍是预测。它最有价值的产出是 L1-L7 分层和三个闭环（Execution Loop / Learning Loop / Fleet Loop），这两个框架足以给绝大多数 2026 年论文定位。它的盲区是安全与治理：整篇没有出现 Runtime Governance、EmbodiedGovBench 这一类工作，而它们正是“让机器人长期工作”的前提。

# 3. 解读二：Code-as-Policy → 自进化机器人 Agent（讲稿）

这份 25 页讲稿的叙事线是：Code as Policies（2022）提出范式 → CaP-X（2026.03）把它做成研究平台 → ASPIRE（2026.06）加上技能库 → SkillOpt（2026.05）给出自进化的算法抽象 → ENPIRE（2026.06）把 coding agent 放进真机学习循环。讲稿最后给出一个统一抽象：自进化就是优化外部产物 $z$。

## 3.1 五篇论文各在进化什么

讲稿第 22 页的对比表是全份材料里最有用的一张表，我们补上论文数字后重列如下。

| 论文 | 外部状态 $z$ | 反馈 → 验证/选择 | 定位 |
|---|---|---|---|
| Code as Policies (2022.09) | policy code | 语言指令 + few-shot 示例 → 程序可执行性 / 任务完成 | 提出范式 |
| SkillOpt (2026.05) | skill.md | 打分后的 rollout → held-out 验证分数严格提升才接受 | 自进化算法抽象 |
| CaP-X (2026.03) | CaP agent / benchmark | 执行反馈 / 视觉差分 → CaP-Bench / sim2real | 研究平台 |
| ASPIRE (2026.06) | 控制程序 + 技能库 | 多模态轨迹 → 验证过的修复 / 任务成功 | 经验复用 |
| ENPIRE (2026.06) | 训练代码 / 配方 / 基础设施 | 真机 rollout + 日志 → 物理任务成功 | 真机自动算法工程 |

各篇的关键数字：

- Code as Policies：分层代码生成把 HumanEval P@1 提到 39.8%；仿真桌面任务上，属性与指令均未见时 CaP 保持 62-80% 成功率而 CLIPort 降到接近 0。
- SkillOpt：6 基准 × 7 模型 × 3 harness 共 52 格全部最优或并列；GPT-5.5 上直接对话 +23.5、Codex +24.8、Claude Code +19.1 个百分点。
- CaP-X：12 个模型；抽象降低则成功率下降；CaP-Agent0 无需训练恢复到接近人类水平；CaP-RL 以可验证奖励做 RL 并以很小差距 sim2real。
- ASPIRE：LIBERO-Pro 最多 +77%、Robosuite 双臂交接 +72%、BEHAVIOR-1K 最多 +32%；LIBERO-Pro Long 零样本 31% 对比先前方法 4%。
- ENPIRE：前沿 coding agent 自主训练到 99% 成功；8 工位集群把 pin insertion 收敛时间从 1.5 小时以上压到约 40 分钟。

## 3.2 Heuristic Learning 与统一公式

讲稿第 2 页把 coding agent 迭代修改软件结构的过程定义为 Heuristic Learning（HL）：它和 Deep RL 共享“状态-动作-反馈-更新”的闭环，但更新对象从神经网络参数换成了软件结构；反馈由 coding agent 消化，可以来自环境奖励、测试、日志、视频、回放和人类反馈；更新不走反向传播，coding agent 直接修改策略、状态检测器、测试、配置或记忆；被长期维护的对象叫 Heuristic System（HS），它至少包含程序策略、状态表示、反馈入口、实验记录、回放/测试、记忆和更新机制。

第 24 页把它压成一个公式：$z_{t+1} = A(z_t, \tau_t, r_t, \log_t)$。$A$ 是 LLM/VLM coding agent，$z$ 可以是技能文档、`policy.py`、技能库、训练配方或 git 分支，$\tau$ 是 rollout 轨迹，$r$ 是验证信号，$\log$ 是错误、视觉差分、机器人 trace、训练曲线等可诊断证据。这个公式的意义在于它把五篇看起来不同的论文放到了同一个坐标系：区别只在 $z$ 是什么、$r$ 从哪来、$A$ 被允许改什么。

SkillOpt 把这个类比推到最严格：参数 ↔ 技能文档，梯度方向 ↔ 从轨迹里抽出的编辑方向，学习率 ↔ 编辑预算 $L_t$，验证 ↔ held-out 选择门。它的四个设计选择都有消融数字：任意适度的编辑预算（$L_t$=2-8）都优于无界重写，去掉预算后 Spreadsheet 77.5→75.7、LiveMath 61.3→57.3；选择门每个 epoch 只放行几十个候选编辑里的 1-4 个，OfficeQA 的 +39 个百分点来自单个被接受的编辑；去掉拒绝编辑缓冲区 Spreadsheet 77.5→72.9；去掉 epoch 级慢/元更新 Spreadsheet 77.5→55.0，是所有消融里最大的退化。SkillOpt-Lite 随后用零阶优化的视角把流水线压到最小，并把同样的方法推广到整套 harness（HarnessOpt），让 GPT-5.4-nano 在 SpreadsheetBench 上超过跑标准流水线的 GPT-5.5。

## 3.3 ENPIRE 的四个实验教训

讲稿第 16-21 页对 ENPIRE 的四组实验做了很好的提炼，我们逐条核对并补充。

1. **仿真成功不等于真机鲁棒。** Gym-PushT 里 Codex 和 Claude Code 约 2 小时达到 95%，Kimi 约两倍时间；迁移到真实 Push-T 后 Codex 接近 95%，Claude 和 Kimi 停在约 75% 和 60%。原因是接触摩擦随时间变化、物体位姿有误差、控制器与真实动力学有偏差、启发式对边界情况敏感。讲稿的结论是“Simulation success ≠ Real-world robustness”，后续实验因此允许 Agent 混用启发式、BC 和 RL。Goldberg 组同月的《Revisiting Push-T with Agentic Robotics》给了另一侧证据：Claude Code 在没有任何示范的情况下写出的算法解在仿真里 100% 成功，且比用 200 条人类示范训练的最佳扩散策略少 46% 步数——仿真里 coding agent 已经赢了，真机上还没有。
2. **纯 BC 不够。** pin insertion 要求策略连续 50 次真机成功。BC 只学示范分布，一旦偏离就进入无覆盖状态；iterative BC 让当前策略上真机采集偏移状态、失败接触、恢复动作和新成功轨迹，逐步覆盖策略诱导分布。Agent 自行尝试了 BC、iterative BC、在线 rollout 聚合、offline RL、online RL、offline-to-online RL、RL + BC 正则，以及 batch size、更新频率和 BC 权重的调优；hillclimb 时间线上最大的一步是 BC regularization（+10.8 个百分点）。
3. **群体提升的是假设吞吐量。** 1/4/8 个 Agent 对应 1/4/8 台机器人，Push-T 归一化得分 1.0 的时间从约 5 小时降到约 2 小时，pin insertion 从 1.5 小时以上降到约 40 分钟。8 倍机器人只有 2-3 倍加速，因为 Agent 会重复探索相似想法、等待训练或大模型输出、阅读其他分支、整理合并实验、花时间分析日志。讲稿的判断正确：多机器人提升的是 hypothesis throughput，不是同一策略的 rollout batch。
4. **持续学习发生在文本记忆里。** 作者让多个 Agent 在 pin insertion 上积累经验后把研究过程整理成 Markdown 总结（哪些 RL 方法稳定、BC 正则是否重要、哪些 batch size 有效、接触任务的控制器需要什么补偿、哪些失败模式优先检查），启动 GPU insertion 时把这份总结放进新 Agent 的初始上下文，并刻意删除原始轨迹、checkpoint、隐藏日志和旧任务工作区。迁移路径是 research experience → textual memory → new autoresearch，不是模型权重的持续学习。这与 Lilian Weng 说的“文件系统即持久记忆”是同一个机制。

第五组实验（讲稿第 21 页）说明 code policy 与 VLA 的分工：RoboCasa365 里纯 GR00T VLA 抓取前常缺少稳定的预定位动作，Agent 于是调用目标检测、分割、三维位置估计和运动规划先把末端移到物体上方的 hover pose，再把控制交给 VLA 完成接触密集的抓取。平均结果 GR00T N1.5 约 53%，ENPIRE 产生的混合方案约 77%，CaP-X 约 27%。这就是 Harness VLA、BATON 采用的同一分工：代码负责几何确定、可规划的阶段，VLA 负责接触丰富的阶段。

## 3.4 对讲稿的补充

讲稿的时间线止于 2026 年 6 月底。7-9 月出现了三类直接续写这条线的工作。第一类把 ASPIRE 的“技能库”推向更抽象的复用单元：PRACTICE 训练一个技能学习器对持久技能库做增/改/合/删的结构化批量编辑，执行器冻结；SkillGLoW 主张复用单元应是“一族相关任务共享的求解过程”，而不是单个全局文档或按任务堆积的条目池，未修改的先验库把未见 ALFWorld 任务成功率从 73.9% 提到 83.9%。第二类把“优化外部产物”从 $z$ 推到运行时：Zetta 在冻结基座策略的前提下在线演化代码形式的 runtime critic 和恢复技能，三个时间尺度分别负责动作频率治理、rollout 级 critic-recovery 提议和验证门控的技能更新，LIBERO-Pro 90.8%、RoboCasa 93.6%、推理加速 11.1 倍；SHAPER 让同一个冻结模型既当规划器又当优化器，演化技能与 context-code harness。第三类是 RHO：coding agent 在训练时搜索多文件策略仓库（Repositories-as-Policies），部署时单轮执行、不再有纠错性代码编辑，在 LIBERO-PRO 上 45.0% 对比 π0.5 的 12.83%，Robosuite 70.0% 刷新最好成绩。RHO 直接回应了 CaP 一直以来的批评——多轮代码生成循环不适合实时控制。

讲稿第 9 页的提醒仍然成立：CaP 优化的是程序接口层，不是直接学习连续控制器。ENPIRE 的混合方案和 RHO 的“同样的底层原语”都说明，2026 年的 Code-as-Policy 不再和 VLA 竞争，而是在给 VLA 写外围。

# 4. 解读三：检索地图的 23 条主线（2026 年 9 月状态）

地图给每条主线列了检索词和代表工作。下面每条主线回答四个问题：这条线在解决什么问题；地图点名的代表工作说了什么；2025-2026 年新增了什么；我们怎么判断它的状态。论文全名、链接与作者见 `README.md` 对应小节。

## T1 Agent + Robot 总览

问题：把 LLM/VLM 的推理接到真实机械臂上，能不能形成“感知 → 分解 → 执行 → 验证 → 重规划”的闭环。地图点名的 AgenticLab（arXiv 2602.01662，Purdue）用规划语言接口定义 VLM 的推理空间：物体谓词表示场景状态，动作 schema 带前置条件与效果，符号计划作为可执行的中间表示，每步执行后用板载观测检查符号效果是否达成。Agentic Robot 用 Standardized Action Procedure 协调推理模型、VLA 执行器和时序验证器，LIBERO 长程任务 79.6%。ManiAgent 用多 agent 协作在 SimplerEnv 达到 86.8%，并用它给 VLA 生成训练数据。2026 年新增的 Cortex（32 个规范技能原语的双向对齐规划接口）、HoloAgent-0（Embodied AgentOS + 3D 空间记忆）、VoLo（VLM 把 VLA/WAM 当作可中断工具中途干预，提出“物理编排”的时序问题）、Guava（系统探索 harness 设计空间，得到三要素：迭代感知-推理-动作循环、语义动作抽象、多模态观测，并蒸馏进 4B 模型）都在同一条线上。《Agentic AI for Robot Control: Flexible but still Fragile》给了清醒的对照：两台真机上迁移只需改系统 prompt，但非确定性行为、指令遵循错误和对 prompt 措辞的高敏感性普遍存在。判断：闭环骨架已经标准化，可靠性瓶颈在验证与 grounding，不在规划。

## T2 Coding Agent 控机器人

问题：让会写代码的模型直接生成机器人策略。这条线从 Code as Policies（2022）到 2026 年出现了三个分叉。测试时生成：CaP-X 的 CaP-Agent0 用多轮交互、执行反馈、视觉差分、技能合成、集成推理在低层原语上恢复人类水平可靠性；MALMM 用 Planner/Coder/Supervisor 三个 LLM agent 零样本完成 RLBench 任务；Neuro-Symbolic Code-as-Policies（NeurIPS 2025 Spotlight）加入符号验证与交互式验证代码，比 CaP 基线成功率 +46.2%。训练时搜索：RHO 让 coding agent 搜索多文件策略仓库，部署时单轮执行；MEMENTO 用记忆引导的单精英模因演化搜索代码策略，并先演化 rollout 评估器；PhysCaP 加一层物理信息驱动的主动探索，从本体感知估计质量和刚度。研究自动化：ENPIRE、HARBOR（把机器人 RL 自动化当作 harness 工程问题）、Nautilus（一句 prompt 生成复现/评估/微调/部署工作流）、AgenticRobotics（策略改进的控制平面，证据分级技能库与签名验证器）。判断：Coding agent 在这条线上的角色已经从“写策略的人”变成“做实验的研究员”，Lil'Log 里的 autoresearch 进入了物理世界。

## T3 OpenClaw / ROS

问题：让任何基础模型接到任何 ROS 机器人，而不是为每对模型-平台写胶水。两篇同名的 ROSClaw 目标不同。Cardenas 等的 ROSClaw 把 OpenClaw agent runtime 接到 ROS 2，提供能力发现与 affordance 注入、观测归一化、安全包络内的预执行动作验证和审计日志，换模型或换平台只是改配置；它同时是测量仪器——在同一基底上，不同前沿模型的越权动作提议率相差 3.4-4.8 倍，且执行层设计比 prompt 措辞更影响任务完成与安全行为。Zhao 等的 ROSClaw 面向异构机器人，用 e-URDF 物理约束构建 sim-real 拓扑映射，把采集、训练与执行放进统一的 VLM 控制器。AgentRob 通过 MCP 把论坛 agent 与 Unitree Go2/G1 相连，也顺带展示了论坛介导的机器人被劫持风险。OpenGo 是 OpenClaw 驱动的 Go2 机器狗，技能库 + 调度器 + 基于反馈的自学习。OpenClawPi 是松灵机器人的技能库，不是论文。MCP 正在成为机器人侧的通用接口：ROSBag MCP Server、ChemBot 的 MCP 子 agent 编排、Contract-Grounded BT Synthesis 让 coding agent 先向机器人侧 MCP server 拉取技能契约再合成行为树。判断：模型无关的执行层是 2026 年基础设施层最实用的进展，它把“安全包络”和“审计”做成了配置项而不是每个项目重写的代码。

## T4 长程任务

问题：多阶段任务的误差累积与阶段间的隐性约束。RoboClaw 用 Entangled Action Pairs 把正向技能与逆向恢复绑定，实现自复位的持续采数据，长程成功率 +25%、人工时间 -53.7%。H-WM 让高层逻辑世界模型与低层视觉世界模型联合预测，为 VLA 提供稳定的中间引导。REMAC 用前置/后置条件检查和场景推理自进化做多机器人长程规划，成功率 +40%。2026 年最重要的新增是 BATON：它指出“冻结 VLA + LLM agent”配方在长程上会坏两次——整任务探索的代价是阶段数的指数（$T^K$）且失败无法归因到阶段，以及 VLA 原语只有退出条件没有进入条件。BATON 以子任务为探索单元（代价变成 $T \cdot K$）并用转移感知记忆治理调用、交接和前瞻三种转移，RoboMemArena 任务成功 +11.6%。AtomBridge 在原子技能边界用 LLM 生成过渡动作代码，8 步任务成功率 +10-25%；Foresight Residual RL 用下游成功概率塑形子任务交接状态，三阶段装配 85.6% 对比 54.5%。判断：长程问题正在被重新表述为“技能交接问题”，进入条件、退出条件和交接状态质量成为核心变量。

## T5 Robot Memory

见 2.1 节。补充一条主线内的分类：权重内记忆（NativeMEM、LaMem-VLA、Remember Smarter、Dual Latent Memory、VQ-Memory、SkillMemo）与权重外记忆（AGM、HyMeS、BATON、Analytic Concept-Centric Memory、OnEvoMemory、ChemBot 的双层记忆、RoboHarness 的多模态执行记忆）。RoboMME 的结论——记忆表示的有效性高度任务依赖——是这条线目前最可靠的经验事实；AGM 的结论——可靠记忆靠状态更新纪律而非容量——是最有设计指导意义的判断。Memory Anchors 从持续学习角度补了一刀：回放缓冲里 10% 的关键锚点经验决定是否灾难性遗忘，去掉它们遗忘增加 4.5 倍。

## T6 Reflection / 反思纠错

问题：失败之后系统改变的是什么。地图点名的 REMAC、AgenticLab、ASPIRE 分别对应 L2、L2-L3 和 L5。2026 年的新增让“反思”有了更细的形态：PhysReflect-VLA 用可行性算子评估候选动作是否产生动力学一致的状态转移、用动作解释算子核查转移一致性、用 LLM 反思模块分析状态差异生成纠正指令，接触密集真机任务平均 +5.4%；Agentic RAG-VLM 用 14 类失败分类和三级自适应重试，杂乱场景抓取从 25% 提到 78.3%；PhysiAgent 让 VLM 根据 VLA 的实时熟练度反馈组织 monitor、memory、reflection 组件；Online Continual RL with World Model Feedback 用 DreamerV3 的预测残差检测 OOD 事件并自动触发微调。判断：反思的价值取决于它能否被写进持久对象（记忆、技能、权重），否则只是更贵的 retry。

## T7 Self-Evolution / 自进化

问题：系统能不能在没有人的情况下持续变好。Arcadia 主张具身学习是生命周期问题，四阶段（自进化探索与接地、生成式场景重建与增强、共享具身表征、sim-from-real 评估与演化）不可分解，去掉任一阶段就退回一次性训练。PhyAgentOS 把调度、验证、记忆、评测、安全做成系统级服务，以会话为最小调度单元，用 State-as-a-File 解耦认知与物理执行，SessionVerifier 区分执行终止与语义完成，验证过的结果经 epistemic memory 沉淀为可复用知识与纠正性教训，在 19+ 个仿真与真实本体上验证。Growing with Your Embodied Agent 走人在环路线，把纠正编码为可复用技能配合外部记忆与 RAG，解决需要 20 个以上原语的“盖房子”任务。2026 年 8 月的一批工作把自进化的对象继续细分：PRACTICE 训练技能学习器维护技能库；SkillGLoW 以过程族为复用单元；Zetta 演化运行时 critic 与恢复技能；SHAPER 演化技能与 context-code harness；Motus2 用单模型三接口（策略/模拟器/评估器）形成决策-学习闭环；Q-Planning 只微调 Q 函数。与软件侧的 Self-Harness、AHE、Meta-Harness 对照，机器人侧的自进化在“可编辑面”上更保守（几乎都冻结基座策略），在“验证”上更依赖物理证据。判断：自进化的真正门槛是验证门与可编辑面的划定，而非搜索算法。

## T8 Skill Library / 技能库

问题：技能从哪来、怎么存、怎么复用。Agentic Skill Discovery（2024）完全由 LLM 驱动：LLM 提任务、采样奖励与成功判定函数、RL 学策略、VLM 独立验证，技能库从零生长。Atomic Skill Library 用三轮数据驱动流程（VLP 拆子任务 → 抽象技能定义 → VLA 微调）构建可动态扩展的原子技能库。ViReSkill 把验证过的计划存进技能记忆下次直接重放，不再调用 LLM。2026 年三个值得记住的变化：ASPIRE 的技能库跨任务、跨仿真/真机、跨本体持久化，并给出了库规模与零样本成功率的单调曲线；RATs 提出“玩耍”阶段——在下游任务到来前用自主提出的探索任务发现技能，LIBERO-PRO 比 CaP-Agent0 +20.6 个百分点，且技能可直接检索进其他 Code-as-Policy agent 的上下文；VASO 把技能表示为带形式接口的语义契约，模型检查的反例变成文本梯度更新技能契约，97.2% 规范符合率——这是“信任技能”的成本第一次被正面处理。ARCHITECT 把人类语言纠正蒸馏进持久技能库，SkillMemo 用 MoE 门控隐式切分技能原语。判断：技能库正在从“代码片段集合”变成“带验证证据与适用范围的知识库”，VASO 和 AgenticRobotics 的证据分级是方向。

## T9 VLA + RL

问题：怎样把真实反馈写回策略权重而不破坏预训练先验。地图点名的 TwinRL（数字孪生预热真机 RL，20 分钟真机交互接近 100%）、LWD（fleet-scale 离线到在线 RL，16 台机器人 95%）、SAC Flow（把 flow rollout 视为残差 RNN，用门控/解码速度网络稳定 off-policy RL）、CaP-RL（对 coding agent 做可验证奖励 RL）、TT-VLA（测试时 RL，逐步任务进度密集奖励）覆盖了从训练时到测试时的全谱。2026 年的新增集中在两个技术点。信用分配：Temporal GRPO 按可检测任务阶段分配优势，解决轨迹级信用混叠；TEMPO 冻结 VLM 主干，语义投影层低频、动作专家高频的双时间尺度更新；WCM 让 critic 同时预测未来 latent 与价值，149 个任务上 SOTA。免外部奖励：T²VLA 用生成置信度作内在奖励；RL²-VLA 只在预测失败时激活 latent 组合式引导，OOD 最多 +17.3%；Z-1 在 π0.5 上用任务级 GRPO 把 RoboCasa 24 任务推到 80.6%。ARLI 解决的是部署侧问题：推理延迟破坏马尔可夫假设，标准 RL 在延迟下完全失效，需要状态增广。判断：VLA + RL 在 2026 年从“能不能”变成了“怎么分配信用、怎么在没有奖励和有延迟时做”，这是一条已经成熟的工程线。

## T10 部署数据回流

问题：部署产生的数据怎么回到训练。LWD 的 Deploy → Experience → RL → Updated Policy → Redeploy 是目前最完整的实证；RoboClaw 的 EAP 解决自复位；Arcadia 用 sim-from-real 评估闭环。2026 年的新增：RoboGene 用多样性驱动 + 自反思物理约束的 agent 自动生成真实操作任务，采集 18k 轨迹，用它预训练的 VLA 泛化更好；AgenticRobotics 把“人可以离开”定义为一个操作性声明——因为晋升是证据门控的、状态可恢复、能力质量由记录导出——并给出了假阳性晋升率 0.001 的硬化数字；Q-Planning 给出了“只用自己的部署 rollout、BC 冻结、无人干预”的真机自改进曲线。判断：数据回流的瓶颈从“采不到”变成了“怎么判断哪些经验值得回流”，这又回到验证器。

## T11 数字孪生 / Sim2Real

问题：把真实场景变成低成本试错环境。TwinRL 和 Arcadia 见上。2026 年这条线的进展是“建 twin 的成本”在快速下降：RoboSnap 单张 RGB 图生成可交互场景并给出 sim-real 相关性；Agentic Real2Sim 让开源 VLM 驱动的 agent 把真实交互录像转成 episodic twin，成本远低于前沿模型；ConCent 以接触事件序列为学习目标做 real-to-sim-to-real RL，避免策略利用不真实的仿真接触；BestMan 提供自动场景生成加硬件无关中间件的 real-to-sim-to-real 平台；Real2Sim via Active Perception 让 VLM 生成行为树主动获取缺失的物理参数；PerceptTwin 直接从机器人感知栈构建交互仿真来验证计划。判断：twin 从“训练场”变成了“验证器的一部分”，它的价值是让 Agent 生成的新技能先在物理仿真里跑一遍。

## T12 World Model

问题：世界模型在 Agent 系统里扮演什么角色。H-WM 用逻辑 + 视觉分层世界模型给 VLA 提供中间引导。2026 年的新增让角色更清楚：Motus2 用一个共享权重的模型同时暴露策略、模拟器和评估器三个接口，形成闭环；WCM 把世界建模目标加进 critic；ContactGuard 用潜空间世界模型做接触前执行监控，在机器人真正接触前预测并中止可能的失败；SafeDojo 在交互式视频世界模型上做安全 RL；Online Continual RL 用世界模型预测残差做 OOD 检测。判断：世界模型在 Agentic Robot 里最有用的角色是“预演器 + 监控器”，而不是动作生成器；这与小红书长文的“脑内预演”判断一致。

## T13 快慢双系统

问题：推理要慢、控制要快，两者怎么共存。Fast-in-Slow 把 System 1 嵌入 System 2 共享参数，异构模态输入、异步频率，action chunk 为 8 时 117.7 Hz；OneTwoVLA 用单一模型自适应切换推理与执行模式；StreamVLA 只在子任务切换时触发慢思考并想象“完成态”作为时间不变的目标锚点，72% 时间步跳过自回归解码，LIBERO 98.5%；LaST0 把推理搬进潜空间，MoT 双专家异频运行，10 个真机任务平均 +13-14%；RationalVLA 用双系统拒绝 RAMA 基准里六维缺陷指令。2026 年新增的 UniFS 把 VLM 各层按更新频率分层（浅层快、深层慢），延迟 36.5 ms → 17.8 ms；Latent Bridge 预测 VLM 输出的帧间 delta，减少 50-75% VLM 调用；Libra-VLA 做异步粗到细；VisualThink-VLA 用视觉中间推理替代文本 CoT，步延迟 8.377 s → 0.367 s；DSWAM 把 System 1 换成世界动作模型。判断：双系统的设计空间已经被系统探索（OpenHelix 有综述与开源实现），剩下的问题是“何时切换”——StreamVLA 的完成态门控和 RL²-VLA 的失败预测门控是两种答案。

## T14 Edge Agent / 端侧部署

问题：大模型上云、控制在端，延迟与断网怎么办。Harness Engineering for Physical AI 给了理论框架（Projection / Isolation / Transfer）。2026 年的系统工作：PhyAI 用一个运行时统一 VLA/WAM 在板载、边缘、云端的推理，对 π0、π0.5、GR00T N1.7、MiniCPM-Robot 提速 1.40-4.65 倍，并提出 control-time Roofline 区分推理受限与环境受限的控制；EcoVLA 做端-边协同推理的能效优化；CloudEdgeVLA 把时间错位当作表示学习问题，云端编码慢变任务特征、边缘头结合最新本地视觉，40 步延迟下仍保持 63.8-78.0%；ST-Merge 训练无关地合并时空视觉 token，π0.5 在 1024×1024 分辩率下提速 8.3 倍；Habilis-β 提出用 Tasks per Hour 与 Mean Time Between Intervention 构成的生产力-可靠性平面，在 1 小时连续运行下评测端侧 VLA。判断：端侧部署的评价指标正在从单次成功率转向连续运行的吞吐与介入间隔，这是“让机器人长期工作”的必要度量。

## T15 Harness

问题：围绕冻结模型的外围系统怎么设计、怎么优化。这是 2026 年 6-8 月密度最高的主线。RHO 优化多文件策略仓库；Harness VLA 学冻结 VLA 的适用范围；Harness Engineering for Physical AI 把中间件定义为 harness 层；PhyAgentOS 把 harness 做成 OS；Thea 补上 Scene Graph as Context 与 Evaluation as Exit Codes；Guava 系统探索 harness 设计空间；HARBOR 把机器人 RL 工程 harness 化；Zetta 让 harness 自己闭环演化；SHAPER 演化技能与 context-code harness；RoboHarness 用执行记忆刻画异构策略的能力边界并用 Memory Bridge 把机器人引导到下一策略的分布内区域；Agentic Harnesses 在规划与执行之间放 LLM-as-a-Judge 集成验证层，对抗攻击 97% 拦截；Cortex 在推理期做从任务上下文到技能约束的 harness engineering。软件侧的 Recursive Harness Self-Improvement、Meta-Harness、Self-Harness、AHE 提供方法论。判断：harness 是 2026 年 Agent × Robot 的中心词，但“harness updating ≠ harness benefit”的警告同样适用——写出 harness 编辑的能力与利用 harness 的能力是两回事。

## T16 Runtime

问题：执行权交给 Agent 之后，谁来保证它可治理。PhyAgentOS 提供会话级调度、预检、监督执行、证据收集与验收。Harnessing Embodied Agents（Runtime Governance）把治理外置为独立运行时层——策略检查、能力准入、执行监控、回滚、人工接管——1000 次随机试验中 96.2% 越权拦截，运行时漂移下不安全继续从 100% 降到 22.2%，恢复成功 90.7%；与 AutoRT 式宪法过滤和 RoboGuard 式两阶段护栏比较，预执行过滤各方法相当，只有它提供持续的运行时检测（RVDR 61.3% 对 0%）与结构化恢复。同一团队的 EmbodiedGovBench 把治理做成七维评测（越权调用、运行时漂移、恢复、策略可移植、升级安全、人工接管、审计完整性）；ICAN-Deploy 用 TLA+ 验证身份稳定的金丝雀部署；FSAR 主张多机器人协调不需要机器人内部的多 agent 碎片化，而是在 fleet 层联邦。HoloAgent-0 的 Embodied AgentOS、PhyAI 的统一推理运行时、AgenticRobotics 的控制平面也属于这条线。判断：Runtime 是把“可治理”从论文变成工程的地方，七维治理评测比任务成功率更接近部署方的关切。

## T17 安全

问题：Agent 驱动的机器人如何不伤人。ROSClaw 的安全包络与审计、Runtime Governance 的拦截与回滚、RationalVLA 的缺陷指令拒绝是地图点名的三条路。2026 年的新增分四类。护栏模型：EMBGuard（ICML 2026）用 2B/4B 模型对（观测，动作）对做物理风险判断，性能接近 GPT-5.1/Gemini-2.5-Pro 且假阳性更低。形式化：SENTINEL 用时序逻辑在语义、计划、轨迹三层评估；VASO 把形式验证接进技能自进化。世界模型：SafeDojo 在想象中学安全动作；ContactGuard 接触前中止。部署视角：Same Weights, Different Robot 指出动作反归一化元数据是可执行策略的一部分，替换一个看似合理的元数据键就能让 LIBERO-Goal 从 28/28 降到 2/28——安全审查只看 checkpoint 会漏掉到达控制器的真实策略。多机器人通信攻击（见 2.6 节）与 AgentRob 的劫持风险也在这条线。判断：安全正在从“过滤不安全计划”扩展到“运行时持续检测 + 恢复 + 可审计 + 升级安全”，并开始触及动作空间语义这类以前没人看的层面。

## T18 标准接口 / Hardware API

问题：Agent 怎样标准化地接入真实硬件。Anthropic 2026 年 8 月 27 日发布的 Model Hardware Standard（MHS）研究预览是这条线的标志性事件：一套让 agent 发现、操作、排障任意物理设备（显微镜、液体处理器、相机、机械臂、激光系统）的共享规范，被媒体称为“硬件版 MCP”，可通过 MCP、CLI 或代码调用。ROSClaw 的能力发现与 affordance 注入、Contract-Grounded BT Synthesis 的机器人侧 MCP 契约、ROSBag MCP Server、AgentRob 的 MCP 桥接、Harness Engineering for Physical AI 的 ROS 2 Harness Profile 都是同一方向的具体实例。判断：接口标准化会决定 harness 层的可移植性，MHS 与 ROS 2 Harness Profile 是否融合值得跟踪。

## T19 多机器人协作

问题：多台机器人怎么用语言协商与协作。RoCo（2023）让机器人用 LLM 对话协商分工与航点，交给多臂运动规划器；REMAC 加入前置/后置条件检查与自进化；RoboOS 用 Brain-Cerebellum 架构与实时共享记忆协调多本体；RoboOS-NeXT 用 STEM 记忆做终身多机器人协作。2026 年新增：DynaHMRC 的去中心化角色感知 agent 与领导者竞选；Scale-Plan 用 LLM 引导的动作图搜索裁剪 PDDL 问题；MeCo 用相似任务记忆化避免重复规划；Tool-RoCo 发现 LLM agent 很少把其他 agent 当作助手调用（协作工具只占 7.09%）；World-Model Alignment Through Dialogue 发现对话把动作冲突减少 40-83 个百分点却降低任务成功，并给出世界模型对齐的度量；FSAR 主张联邦式而非碎片化。判断：多机器人协作的语言层已经不缺方法，缺的是共享记忆的一致性与通信的可信性。

## T20 跨本体

问题：技能与系统能否跨机器人形态迁移。RoboOS 支持异构本体；ASPIRE 的技能跨本体与机器人 API 迁移并有初步 sim-to-real 证据；Harness VLA 在 RoboTwin C2R 达到 58.4%。ROSClaw（异构）用 e-URDF 做物理约束；BestMan 用硬件无关中间件；PhyAgentOS 在 19+ 本体上验证。判断：跨本体在 Agent 层比在策略层容易——代码、技能契约和 harness 配置天然可迁移，而策略权重不能。

## T21 群体学习 / Fleet Learning

问题：一台机器人学到的东西怎么变成群体的能力。LWD 是策略层的实证，RoboOS/RoboOS-NeXT 是记忆层的实证，ENPIRE 的 8 工位集群是研究层的实证（并给出 MRU/MTU 两个效率指标）。FSAR 讨论 fleet 层的治理与恢复边界。判断：群体学习目前有两端（共享策略、共享状态记忆），中间的共享经验与共享世界知识还缺系统性工作；Fleet 的加速比不是线性的（ENPIRE：8 倍机器人 2-3 倍加速），因为瓶颈在假设生成与分析而非 rollout。

## T22 主动感知

问题：Agent 能不能为了获取信息而行动。AgenticLab 的在线验证需要主动观测；PhysCaP 让 Code-as-Policy agent 通过交互推断质量与刚度（找隐藏物体、检测空罐、挑成熟的鳄梨），Planner 决定何时探索与停止，Prioritizer 过滤不合理交互；ActiveVLA 做关键区域定位加主动视点选择与 3D 放大；Real2Sim via Active Perception 用 VLM 生成的行为树主动获取仿真缺失的物理参数。判断：主动感知在 Agent 系统里的形态是“把探索当作可调用的工具”，成本控制（何时停）是关键。

## T23 Verifier / 成功验证

问题：“这一步到底成没成”由谁判断。Harness VLA 的成功规则与失败模型、PhyAgentOS 的 SessionVerifier、REMAC 的前置/后置条件是地图点名的三种形态。2026 年这条线上的新工作最能说明它已成为瓶颈：Thea 的 Evaluation as Exit Codes（检测动作何时应终止、判断是否成功、失败时诊断原因）；AGM 用本体感知线索决定何时验证、用点跟踪与跨视角语言比较决定达成了什么，一个 2.43M 参数的验证头；Agentic Harnesses 的 LLM-as-a-Judge 集成；LLM-as-a-Verifier 把验证当作新的 scaling 轴，对评分 token logits 取期望得到连续分数，RoboRewardBench 87.4%，还能作为 RL 的密集奖励；VASO 用模型检查替代轨迹级证据；PerceptTwin 用仿真验证计划；Consilience 讨论无验证器时如何利用置信度轨迹。那篇立场论文《VLA Cannot Be Verified to Perform Physical Reasoning》指出成功率无法区分语义匹配与物理泛化，需要受控变量的评测设计。判断：验证器决定了自进化循环的上限——奖励作弊、过度乐观、“仿真 100% 真机 60%”都在这里发生。

## T24 Robot RSI：递归自我改进（新增主线）

问题：机器人系统能否参与改进“怎样让自己变得更好”，并把成果带进下一轮。这条主线来自具身纪元的文章（见第 6 章），把软件侧的 RSI 谱系（Gödel Machine 的“可证明有益才修改”、STaR、Reflexion、Let's Verify Step by Step、Meta-Rewarding、The AI Scientist、HiSME、BigBang-V1、Anthropic《When AI builds itself》）与机器人侧的四个环节并列：部署时自演化（ASPIRE、RoboHarness、Zetta）、训练时自迭代（RoboClaw、LWD、Q-Planning）、自我评估（PRIMO R1 的过程级视频批评者、VERITAS 的推理时视觉验证器）、自动研究（Eureka → DrEureka → ENPIRE 的“奖励 → 仿真参数 → 整个研究循环”演进）。判断：Robot RSI 是把 T2、T7、T9、T10、T23 串起来的框架而不是新方法；它的两个独有难题是可重复、可扩展的物理验证环境，以及当评价器本身也在演化时如何保持“评估器在循环之外”。

# 5. 解读四：Lilian Weng 的两篇文章


## 5.1 《LLM Powered Autonomous Agents》（2023.06）

这篇文章给出的分解——Agent = LLM 大脑 + Planning（子目标分解、反思与精炼）+ Memory（短期 = 上下文、长期 = 外部向量库与快速检索）+ Tool use（调用外部 API）——是小红书长文那张完整架构图的直系祖先。长文把 Planning 放进 Agent/System 2 层，把 Memory 拆成 Memory/Skill/Dataset，把 Tool use 具体化为 Harness/Runtime 的 Tool Routing 和 Skill Layer 的四类原语（Code Skill、Analytic Primitive、VLA Primitive、RL Policy）。2023 年文章列出的三个挑战——有限上下文长度、长程规划与任务分解的困难、自然语言接口的不可靠——在机器人侧对应的正是 Memory 主线、长程任务主线和 Verifier 主线。

## 5.2 《Harness Engineering for Self-Improvement》（2026.07）

这篇文章把 harness 定义为“围绕基座模型的系统，它编排执行，决定模型如何思考与规划、如何调用工具与行动、如何感知与管理上下文、如何存储产物、如何评估结果”。它的三个设计模式在机器人论文里都有对应物。

| Lil'Log 的 harness 模式 | 机器人侧对应 |
|---|---|
| 工作流自动化：plan → execute → observe/test → improve 的目标导向循环 | ENPIRE 的 reset → execute → verify → refine；ASPIRE 的执行引擎 → 诊断 → 修复 → 验证；RoboClaw 的 Collection ↔ Learning ↔ Deployment 单一 Agent 循环 |
| 文件系统即持久记忆：状态与产物存文件而不是塞进上下文 | PhyAgentOS 的 State-as-a-File（跨层状态物化为 Markdown + YAML）；ENPIRE 的 Markdown 研究总结迁移；AgenticRobotics 的 commit 键控崩溃恢复与证据分级技能库 |
| 子代理与后台任务：并行搜索假设、监控作业、合并结果 | ENPIRE 的 Agent 团队 × 机器人集群；HARBOR 的分阶段专门 agent；RATs 的 Robotics Agent Teams |

文章提出的优化对象阶梯——instruction prompts → structured context → workflow → harness code → optimizer code——与讲稿的 $z$ 完全对应：SkillOpt 在 structured context 一级（skill.md），ASPIRE 在 workflow 与技能库一级，RHO 与 SHAPER 在 harness code 一级，Meta-Harness 与 SkillOpt-Lite 的 HarnessOpt 在 optimizer code 一级。

文章里有两个结论对机器人尤其重要。第一，STOP 的自学优化器在 GPT-4 上有效、在 GPT-3.5 和 Mixtral 上退化，Lin 等人 2026 年进一步拆出两个轴：写 harness 的能力（从 Qwen3.5-9B 到 Claude Opus 4.6 几乎持平）和利用 harness 的能力（非单调，中等模型受益最大）。这意味着 ENPIRE 里 Codex、Claude、Kimi 在真机上的差距，更可能来自利用 harness 的能力而非提出改进的能力。第二，评估器和权限控制必须放在演化循环之外：AHE 把 runs 目录、tracer、verifier 和 LLM 配置设为只读，才能把每一次收益归因到 harness 编辑而不是奖励作弊。机器人侧的 Runtime Governance、ICAN-Deploy 和 AgenticRobotics 的签名验证器做的是同一件事。

文章列出的 RSI 七个挑战——弱而模糊的评估器、上下文与记忆的生命周期、负面结果、多样性塌缩、奖励作弊、长期成功、人的角色——在机器人侧有更具体的形态：评估器弱对应 Verifier 主线（“这一步成没成”要靠物理证据）；记忆生命周期对应 RoboMME-Interference 的干扰衰减；负面结果对应 ASPIRE 与 Zetta 强调的失败轨迹是最有价值的数据；多样性塌缩对应 ENPIRE 里多个 Agent 重复探索相似想法；奖励作弊对应仿真里 100% 成功、真机上 60% 的 Push-T；人的角色对应 LWD 与 TwinRL 里的人工干预与 human-in-the-loop rollout。

## 5.3 两篇文章没有覆盖的部分

Lil'Log 讨论的 harness 生活在数字世界：状态可读、结果可判、失败可重试一千次。Thea 那篇论文说得最清楚——物理世界拒绝提供软件白送的两样东西：读取世界状态和判断动作结果。它用 Scene Graph as Context 和 Evaluation as Exit Codes 补这两个缺口。Harness Engineering for Physical AI 补的是第三个缺口：时间。软件 harness 不关心一次推理花 2 秒，机器人 harness 必须关心，因为这 2 秒会改变控制日程和轨迹。这三点是机器人 harness 与软件 harness 的本质差异，也是第 7 章几条洞见的出发点。

# 6. 解读五：具身纪元《GPT-6 未必能当好机器人的大脑，却可能帮王兴兴加速 RobotRSI》

这篇文章（Marilyn Liu，公众号具身纪元，2026 年 8-9 月）从一个反差出发：GPT-6 Astra 在 Robocurve 第三方测试的“方块放入碗中”拿到 19/20（Claude Fable 5.1 为 8/20），却在精细拼图插入上与对手同为 2/20，拧洗衣机按钮用了 4 分钟。作者的判断是，模型升级增强了视觉理解、空间规划、纠错和工具调用，但涉及接触、摩擦、精确对齐和毫米级误差时，LLM 的提升没有转化成控制能力；因此与其关注 LLM 对 policy generator 的贡献，不如关注它对具身领域 RSI（Recursive Self-Improvement，递归自我改进）的贡献。这与本报告 I2 的判断（冻结 VLA + 外围学习有天花板，接触相关的连续关系要写回权重）是同一件事的两面。

## 6.1 RSI 的定义与两条轴线

文章把 RSI 拆成三个词：Self（被改的可以是回答方式、记忆、工具、代码、训练数据、评价器或权重，不必是重写全部源代码）、Improvement（新版本必须在某个可检查目标上更好，无法验证的变化只能叫变化）、Recursive（上一轮成果进入下一轮并让系统更有效地制造下一版，“改进能力本身也被再次用于改进”）。它随后给出两条轴线，这是全文最有用的工具：

| 轴线一：改进的环节 | LLM 侧代表 | 机器人侧代表（文章点名） |
|---|---|---|
| 部署时自演化：权重不变，改推理、记忆、工具、代码、harness | Reflexion（反思存记忆再重试，HumanEval 91%）；HiSME（从执行轨迹学“怎样生成与修改技能”的元技能，MineDojo 0.700→0.856）；Lil'Log 的 harness 判断 | ASPIRE（失败修复存成技能）；RoboHarness（执行记忆调度异构策略，切换前先把机器人带到下一策略熟悉的状态，135 次真机实验） |
| 训练时自迭代：上一轮数据、推理、偏好、奖励回到训练，更新权重 | STaR（答对保留、答错看答案重推、微调下一版）；BigBang-V1（出题者 / 批评者 / 元批评者合成约一万条可验证难题更新权重） | RoboClaw（同时学“完成任务”与“恢复现场”两套策略，正反交替回收成功数据，人工时间 -53.7%） |
| 自我评估：改进 judge、reward model、process reward model、verifier | Let's Verify Step by Step（过程奖励模型逐步定位错误）；Meta-Rewarding LMs（同一模型当回答者、评审者和“评审的评审”，AlpacaEval 2 LC 22.9%→39.4%） | PRIMO R1（以初始 / 当前画面锚定过程视频，判断进度与失败位置，RoboFail 67%）；VERITAS（冻结策略 + 无梯度视觉验证器，50 条验证过的自主轨迹 70% vs 同量人工示范 65%） |
| 自动研究：提出假设、改算法、跑实验、分析结果、安排下一轮 | The AI Scientist（从代码模板到自动评审的全流程） | ENPIRE（自动复位、成功验证、策略更新、真机试验封装成工具）；Eureka（LLM 写奖励，83% 任务超过人工奖励）；DrEureka（LLM 同时写奖励与域随机化范围，四足机器人站瑜伽球迁移真机） |

轴线二是人的参与程度：Human-in-the-loop（AI 提议、人逐次确认）、Human-on-the-loop（数据、奖励、评价、执行大体自动，人监督结果、设置权限、控制发布）、Closed loop（在预先授权范围内自行提出、验证并采用改进）。文章没有把论文逐一放进这条轴，但本报告第 4 章 T16 的 Runtime Governance、ICAN-Deploy 和 AgenticRobotics 的“人可以离开”的操作性定义，正是从 on-the-loop 走向 closed loop 时需要的基础设施。

## 6.2 与本报告框架的对照

两条轴线与前面几章的框架可以直接叠放。轴线一的四个环节对应讲稿公式里 $A$ 被允许改的对象：部署时自演化改 $z$ 中的 harness / 记忆 / 技能，训练时自迭代改策略权重，自我评估改 $r$ 的来源，自动研究改整个实验流程。它也对应小红书长文的 L1-L7：部署时自演化覆盖 L3-L5，训练时自迭代是 L6，自动研究把 L7 的群体经验变成研究流程本身。文章对 ENPIRE 的概括——“把自动复位、成功验证、策略更新和真机试验封装成工具，让编程智能体连续执行—检查—改代码—再执行”——与讲稿第 3 章的四个教训一致。

文章新增的价值有三点。第一，它把 PRIMO R1 与 VERITAS 放进“自我评估”环节，补上了本报告 T23 里两类此前缺席的验证器：过程级的视频批评者（不只判断最终画面像不像成功，而是判断进展到哪一步、从哪里开始失败）和推理时的动作验证器（生成器-验证器框架，验证过的 rollout 直接成为微调数据，且效率与专家示范相当）。第二，它把 Eureka / DrEureka 这条 2023-2024 年的“LLM 写奖励与仿真参数”线接回自动研究，说明 ENPIRE 式的 physical autoresearch 有更早的源头：先自动化训练方法（奖励、域随机化），再自动化整个研究循环。第三，它给出了机器人 RSI 与大模型 RSI 的核心差异：评估包含两个问题——评价器能否判断成功、进度与失败位置，以及系统能否提供可重复、可扩展的验证环境；后者是 LLM 从未遇到、机器人必须解决的。这与本报告 I6（Sim 是 sandbox）和 I3（验证器是瓶颈）的结论重合，作者把它表述为“Robot RSI 还缺一个虚拟世界”，并认为世界模型是比传统仿真更可扩展的解法。

## 6.3 评价

文章的核心判断——前沿 LLM 更可能先成为 Robot RSI 的认知中枢而不是机器人的末端控制器——有本报告核实过的证据支持：ASPIRE 用 Claude Opus 4.6 读多模态执行记录并修复程序，RoboHarness 用 GPT-5.5 改策略编排代码，ENPIRE 让 coding agent 查文献、提假设并在真机比较，Zetta 在冻结 VLA 下持续更新 critic、恢复技能和工具。它对产业动向的记录（Anthropic《When AI builds itself》、OpenAI 的 RSI 团队、Recursive Superintelligence / Trajectory / Discovery Loop 的融资与创立、王兴兴在 2026 世界机器人大会上的“直接让物理 AI 机器人模型实现自进化”）是观察，不是证据；Robocurve 测试与方舟无限视频也属第三方报道。文章没有触及的部分与小红书长文相同：治理与安全——closed loop 这一格在文章里只有定义，而 Runtime Governance 的 96.2% 越权拦截、EmbodiedGovBench 的七维评测正是让 closed loop 可被授权的前提；另一个空缺是 Lil'Log 强调的“评估器必须在演化循环之外”，当自我评估环节本身也在被系统改进（Meta-Rewarding 的“评审的评审”）时，这条原则如何在机器人上落实，是 Robot RSI 真正的难题。

# 7. 趋势与洞见

下面十条是把四份材料和 154 篇论文放在一起之后得到的判断。每条给出证据、边界和它对研究选题的含义。

## I1 优化对象在上移：从动作到产物

2022 年 LLM 输出一段策略代码；2026 年 coding agent 优化的是 skill.md（SkillOpt）、多文件策略仓库（RHO）、技能库（ASPIRE、PRACTICE）、训练配方与基础设施（ENPIRE、HARBOR）、运行时 critic 与恢复技能（Zetta）、整套 harness（SHAPER、HarnessOpt）。Lil'Log 的阶梯 prompt → context → workflow → harness code → optimizer code 在机器人侧被完整走了一遍。含义：一个新方法的贡献，越来越取决于它把哪个层级的产物变成了可搜索、可验证、可复用的对象，而不是它在某个基准上多了几个点。

## I2 “冻结 VLA + 外围学习”是默认范式，但有天花板

Harness VLA、BATON、AGM、HyMeS、Zetta、SHAPER、RoboHarness、AtomBridge、RL²-VLA 都不改 VLA 权重。理由是权重更新贵、慢、验证难，而且闭源前沿模型根本不开放权重。这条路的成绩是真实的：LIBERO-Pro 上 Harness VLA +38.6 个百分点、Zetta 90.8%。但天花板也清楚：小红书长文的 USB 例子——视觉、接触、力反馈到微动作的连续关系——和 BATON 分析的“VLA 原语没有进入条件”，都是外围学习填不平的洞。LWD（16 台机器人 95%）、Q-Planning（真机 40%→90%）、TEMPO、Temporal GRPO 说明真实反馈最终要写回权重。HyMeS 的“技能在权重里、记忆在代码里”是一个可操作的分工假设：低层运动技能用梯度学，高层记忆与流程管理用 coding agent 学。

## I3 验证器是新的瓶颈，也是新的 scaling 轴

自进化循环的每一步都要回答“成没成”。PhyAgentOS 把“执行终止”与“语义完成”分开；Thea 把评估做成 exit code；AGM 只在物理证据确认后推进进度指针，并得出“可靠记忆靠状态更新纪律”的结论；LLM-as-a-Verifier 证明验证精度可以沿评分粒度、重复评估和标准分解三个维度扩展，并能作为 RL 密集奖励；VASO 用形式验证替代轨迹级证据；那篇立场论文说成功率本身无法证明物理推理。Lil'Log 列的 RSI 第一个挑战正是弱评估器。具身纪元文章点名的 PRIMO R1（过程级视频批评者，判断进度与失败位置）和 VERITAS（推理时视觉验证器，验证过的 rollout 直接成为微调数据）说明验证器正在分化为“过程监督”和“动作选择”两种形态。含义：在 Agent × Robot 里，一个更好的验证器比一个更好的规划器更稀缺，也更容易成为独立贡献。

## I4 记忆分成权重内与权重外两条路，各有适用区

权重内：NativeMEM（32.4%→84.0%）、LaMem-VLA、Remember Smarter、VQ-Memory、SkillMemo、PonderPounce 的原生因果上下文。权重外：AGM、HyMeS、BATON、概念中心记忆、OnEvoMemory、RoboHarness 的执行记忆。RoboMME 的结论（记忆表示高度任务依赖）和 RoboMME-Interference 的发现（感知型记忆随干扰衰减、检索可恢复）给出了选择依据：需要精确时序与计数的用权重内记忆；需要跨会话、抗干扰、可解释与可编辑的用权重外结构化记忆。小红书长文的四类记忆（Working/Episodic/Semantic/Skill）在这两条路上都能落位。

## I5 Harness 从软件名词变成实时系统问题

软件 harness 在工具调用边界介入；机器人 harness 必须同时在控制、计算、通信三处介入（Harness Engineering for Physical AI），必须知道最大延迟、deadline 和 fallback（小红书长文的 Real-time-aware Harness）。PhyAI 的 control-time Roofline、EcoVLA 的 20 Hz 约束、CloudEdgeVLA 的 40 步延迟、ARLI 的延迟破坏马尔可夫假设、UniFS/Latent Bridge 的频率分层，都是这个问题的具体形态。含义：机器人 harness 的研究会越来越像操作系统与实时调度，而不是 prompt 工程；Lil'Log 提到的“harness 与 OS 的类比”在机器人侧是字面意义的。

## I6 真机试错成本决定了 Sim 的角色是 sandbox

软件 Agent 可以 retry 一千次，机器人碰一次可能坏一个零件。TwinRL、RoboSnap、Agentic Real2Sim、PerceptTwin、SafeDojo、ContactGuard 的共同点是把仿真/世界模型用作新技能与新计划的预演与验证环境，而不是主训练场。小红书长文的流程（生成技能 → 静态检查 → 数字孪生 rollout → 域随机化 → 失败挖掘 → 安全验证 → 硬件在环 → 小规模真机 → 真实反馈 → 更新仿真）在 2026 年论文里每一步都有对应工具。含义：“Real → Sim → Learn → Verify → Real”是可以工程化的流水线，缺的是把这些工具串起来的 harness。

## I7 治理与安全成为一等公民

Runtime Governance（96.2% 越权拦截、持续运行时检测）、EmbodiedGovBench（七维治理评测）、ICAN-Deploy（身份稳定的升级）、FSAR（fleet 层治理）、EMBGuard（小模型护栏）、SENTINEL/VASO（形式化）、Same Weights Different Robot（动作空间元数据）、多机器人通信攻击、AgentRob 的劫持风险。这些工作说明“让机器人长期工作”的前提是可治理，而四份材料里只有 ROSClaw 和 PhyAgentOS 涉及这一点。含义：安全与治理是 Agent × Robot 里被材料低估、被论文高估的方向——低估是因为观点文章不写它，高估是因为它目前主要在仿真里验证。

## I8 群体是经验规模化的出路，但收益是亚线性的

LWD 用 16 台机器人把单一 VLA 推到 95%；ENPIRE 用 8 工位把收敛时间压到 1/3-1/2。ENPIRE 的分析很诚实：8 倍机器人只有 2-3 倍加速，因为 Agent 会重复探索相似想法、等待训练、阅读其他分支、分析日志。群体提升的是假设吞吐量。含义：Fleet 的价值在多样性（不同假设、不同场景），不在同一策略的 rollout 数量；Lil'Log 的“多样性塌缩”挑战在机器人集群里会以“多个 Agent 试同一个想法”的形式出现。

## I9 Coding agent 成为 roboticist：autoresearch 进入物理世界

RHO 的标题《Your Coding Agent is Secretly a Roboticist》、ENPIRE 的“physical autoresearch”、HARBOR 的 RL 工程自动化、Nautilus 的一句话工作流、Goldberg 组的 Push-T 实验（Claude Code 无示范 100% 成功、少 46% 步数）、AgenticRobotics 的“人可以离开”。这条线与 Lil'Log 讨论的 AI Scientist、AlphaEvolve、DGM 是同一件事在物理世界的版本，具身纪元文章把它命名为 Robot RSI 并追溯到 Eureka / DrEureka 的“LLM 写奖励与仿真参数”；物理世界给它加了三个约束：读状态难、判结果难、有时间。含义：Trehan & Chopra 总结的六类自主研究失败模式（训练数据默认偏置、实现漂移、记忆退化、过度乐观、领域知识不足、科学品味弱）在机器人侧会以“仿真 100% 真机 60%”、“重复假设”、“把噪声当信号宣布成功”的形式出现，需要专门的检测。

## I10 风险与反例

三条警告应该和上面九条一起读。第一，“harness updating ≠ harness benefit”：写 harness 编辑的能力在 9B 到 Opus 之间几乎持平，利用 harness 的能力非单调，所以 harness 收益不能脱离基座模型讨论。第二，奖励作弊与 Goodhart：Lil'Log 强调评估器与权限控制必须在演化循环之外，AHE 用只读的 verifier 与配置做到这一点，机器人侧对应的是 Runtime Governance 的外置治理与 AgenticRobotics 的签名验证器；任何把验证器放进可编辑面的自进化系统都应被怀疑。第三，多智能体系统的对话可能降低任务成功（World-Model Alignment Through Dialogue），协作工具很少被调用（Tool-RoCo 7.09%），共享经验会共享污染（通信攻击）。这些反例提醒：Agent × Robot 的系统复杂度本身就是风险来源。

# 8. 开放问题与研究建议

1. **验证器的可扩展性。** 能否把 LLM-as-a-Verifier 的连续评分、AGM 的物理证据验证头和 VASO 的形式检查组合成分层验证器，并用 EmbodiedGovBench 式的指标评测它？这是自进化循环的上限所在。
2. **进入条件。** BATON 指出 VLA 原语只有退出条件；RoboHarness 用执行记忆估计分布内区域并引导机器人进入。能否为每个原语学习显式的进入条件与交接状态质量（Foresight Residual RL 的 foresight value），使长程任务的代价从 $T^K$ 变成 $T \cdot K$？
3. **权重内外记忆的分工。** HyMeS 的“技能在权重里、记忆在代码里”是一个假设。哪些信息应当进入权重（连续接触关系），哪些应当留在外部结构（跨会话、可编辑）？RoboMME 的任务分类是评测这个分工的现成工具。
4. **实时感知的 harness。** 把 Projection / Isolation / Transfer 做成 ROS 2 Harness Profile 并与 MHS 对接，让延迟预算、deadline 和 fallback 成为声明式配置。PhyAI 的 control-time Roofline 可以作为度量。
5. **群体的多样性。** ENPIRE 的亚线性加速来自假设重复。能否用 Lil'Log 提到的 ShinkaEvolve 式新颖性拒绝采样或 SkillGLoW 式的过程族去重，让 N 台机器人探索 N 个不同假设？
6. **Real → Sim → Verify → Real 的流水线化。** RoboSnap、Agentic Real2Sim、PerceptTwin、SafeDojo 各管一段。谁来做把它们串起来、以技能为单位运行的 harness？
7. **治理进入真机。** Runtime Governance 与 EmbodiedGovBench 目前主要在仿真验证；把七维治理指标搬到真机集群（LWD、ENPIRE 规模）是下一步。
8. **从 System Scaling 到 Experience Scaling 的度量。** 小红书长文提出的口号需要指标。Habilis-β 的 Tasks per Hour × Mean Time Between Intervention、ENPIRE 的 MRU/MTU、AgenticRobotics 的假阳性晋升率是候选。

给自己的 method-story 起点（沿讲稿第 24 页的建议）：选一个 $z$（例如“技能的进入条件与验证头”），选一个 $r$ 的来源（物理证据 + 形式检查），把 $A$ 的可编辑面画清楚并把验证器放在外面，然后在 LIBERO-Pro Long 或 RoboMemArena 这类长程基准上报告库规模 vs 零样本成功率的曲线。

# 9. 附录

## 9.1 论文索引

按 25 条主线组织的 169 条论文清单见仓库 `README.md`；机器可读版本见 `data/papers.csv`（字段：id、short_name、title、authors、year、date、venue、url、code_url、topics、tier、note_zh）。`tier` 为 core 的 46 条是五份材料点名的机器人侧工作，extended 的 94 条是扩展检索到的 2025-2026 工作，foundation 的 29 条是软件侧 Agent / Harness / RSI 基础。

## 9.2 术语表

| 术语 | 本报告中的含义 |
|---|---|
| Harness | 围绕冻结模型的外围系统：编排执行、调用工具、管理上下文与状态、存储产物、评估结果（Lil'Log 定义） |
| Code-as-Policy (CaP) | LLM 生成处理感知输出、调用控制原语、可含反馈循环的可执行程序作为策略 |
| Heuristic Learning / System | 讲稿定义：coding agent 依据反馈直接修改软件结构（策略、检测器、测试、配置、记忆）的学习过程 / 被长期维护的对象 |
| 外部产物 $z$ | 讲稿统一公式中被优化的对象：skill.md、policy.py、技能库、训练配方、git 分支、harness 代码 |
| L1-L7 | 小红书长文的自进化分层：Retry、Replan、Reflection、Memory Evolution、Skill Evolution、Policy Evolution、Fleet Evolution |
| Execution / Learning / Fleet Loop | 小红书长文的三个闭环：这次能不能做完 / 下次能不能更好 / 一台学到的能不能变成群体的 |
| Real-time-aware Harness | 知道模型最大延迟、技能 deadline、断网 fallback、哪些动作必须本地完成的 harness |
| Projection / Isolation / Transfer | Harness Engineering for Physical AI 提出的三个强制功能：输出处约束动作、限定执行与传输时隙、失败时回退到验证过的基线 |
| Experience Scaling | 小红书长文的判断：机器人的 scaling 来自群体持续产生的物理交互经验，而非仅来自模型规模 |
| RSI 两条轴线 | 具身纪元文章的框架：改进的环节（部署时自演化 / 训练时自迭代 / 自我评估 / 自动研究）× 人的参与程度（in-the-loop / on-the-loop / closed loop） |

## 9.3 复现说明

- 重新生成 README：`python3 src/build_papers_csv.py && python3 src/generator.py`（前者需要 `data/paper_meta.json`，由 `src/fetch_arxiv_meta.py` 从 arXiv API 抓取）。
- 下载全部论文 PDF：`bash scripts/download_papers.sh`。
- 用 SuperTranslate 翻译：配置 `DEEPSEEK_API_KEY`（或任意 OpenAI 兼容端点）后运行 `bash scripts/translate_papers.sh`；无 API key 时可用 `scripts/manual_translate.py` 走"导出文本块 → 人工译文表 → 原位回填 → inspect QA"的确定性通路，本仓库五篇核心论文的中文版即由此产生。
- 生成 PDF 报告与幻灯片：`bash scripts/build_docs.sh`（pandoc + XeLaTeX；HTML 幻灯片用 Playwright/Chromium 导出 PDF；Beamer 幻灯片用 XeLaTeX 编译）。

## 9.4 材料来源

- 具身RL日记，《Harness 之后，Agent+Robot 下一站是什么？》，小红书，2026。转写见 `sources/xiaohongshu_harness_next_transcript.md`。
- `code_policy_self_evolving_agents.pptx`，25 页，文字与讲稿摘录见 `sources/code_policy_deck_extracted.md`。
- 《Agent + Robot 论文检索地图》，两页表格，转写见 `data/topics.csv`。
- Lilian Weng, "LLM Powered Autonomous Agents", Lil'Log, 2023-06-23; "Harness Engineering for Self-Improvement", Lil'Log, 2026-07-04。文本存档见 `sources/`。
- Marilyn Liu（具身纪元），《GPT-6 未必能当好机器人的大脑，却可能帮王兴兴加速 RobotRSI》，微信公众号，2026 年 8-9 月（访问日期 2026-09-06）。转写与论文对照表见 `sources/wechat_embodied_era_robot_rsi_transcript.md`。
