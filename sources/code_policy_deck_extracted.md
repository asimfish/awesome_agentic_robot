# Code-as-Policy 讲稿（code_policy_self_evolving_agents.pptx）文字与讲稿备注提取

来源：用户提供的 25 页 PPTX；用 python-pptx 提取全部文本框、表格与演讲者备注。图片页仅记录图片尺寸。


## Slide 1

- SELF-EVOLVING ROBOT AGENTS
- 01 / 16
- Code-as-Policy
- 代码即策略
  到自进化机器人 Agent
- SkillOpt · Code as Policies · CaP-X · ASPIRE · ENPIRE
- skill.md
- 外部可训练状态
- policy.py
- 程序化机器人策略
- CaP-Gym
- 可复现评测环境
- skill library
- 跨任务经验复用
- real robot
- 真实物理闭环
- 核心问题：LLM 不只回答机器人指令，而是写、运行、诊断、改进可执行机器人代码。

> 备注：Sources: arXiv:2209.07753, 2605.23904, 2603.22435, 2606.19980, 2607.00272.

## Slide 2

- SELF-EVOLVING AGENT
- 自进化 Agent 以及Heuristic Learning
- （图片）图片 30 5299710x4995545
- （图片）图片 31 4931410x2740025

## Slide 3

- SKILLOPT
- SkillOpt：在可控的文本空间训练 skill.md
- Source: SkillOpt, arXiv:2605.23904.
- （图片）Picture 1 12191365x5405120

> 备注：SkillOpt treats skill as trainable external state; optimizer performs bounded edits and validation-gated updates; reports best or tied-best on all 52 evaluated cells.

## Slide 4

- （图片）Picture 1 12191695x6858000

> 备注：⏱  Slide 15/23 — Why bounded updates? Skill training is gradient descent in text space
      Allotted 1:15   |   Cumulative 19:15 / 30:00
  ──────────────────────────────────────────────────────────
  [中文 · 主讲稿]
  我想先给大家一个直觉图，再去拆具体的 pipeline。你把它当成一个 loss landscape 来看 —— 只不过纵轴不是 training loss，而是 validation error；横轴不是参数空间，而是 skill 文本的空间。我们从一个初始 skill 出发，目标是走到谷底那个更好的 skill。蓝色这条路就是 SkillOpt：每一步都是有边界的小编辑，每一步都过 held-out 的 selection gate，走不动了就把失败的编辑记进 buffer。它很稳，一步一步往下走。灰色这条虚线，是没有约束的 ad hoc rewrite，也就是现在很多 skill 自我改写的做法。它一次跳很大，语义乱跳，最后卡在一个次优的 skill 上下不来。右边这张对照表，其实就是整篇 SkillOpt 的灵魂：参数对应 skill 文档，梯度方向对应从轨迹里抽出来的编辑方向，learning rate 对应 edit budget，验证对应 held-out gate。所以这真的就是一次文本空间里的梯度下降。下一页，我把这条蓝色的路径拆开，看一个 step 到底怎么走。
  ──────────────────────────────────────────────────────────
  [English · backup]
  Let me give you the intuition before the mechanics. Think of it as a loss landscape — except the vertical axis is validation error, not training loss, and the horizontal axis is the space of skill text, not parameters. We start at an initial skill and want to reach the better skill at the bottom. The blue path is SkillOpt: every step is a small bounded edit, every step passes a held-out selection gate, and when an edit fails it goes into the buffer. It's stable; it walks down step by step. The grey dashed path is unconstrained ad hoc rewriting — how most skill self-editing works today. It jumps far, lands semantically all over the place, and stalls at a sub-optimal skill. The table on the right is the soul of the paper: parameter maps to skill document, gradient direction to trajectory-derived edit direction, learning rate to edit budget, validation to the held-out gate. It really is gradient descent in text space. Next slide, I unfold that blue path into a single step.

## Slide 5

- （图片）Picture 1 12191695x6858000

## Slide 6

- （图片）Picture 1 12191695x6858000

## Slide 7

- （图片）图片 1 8879840x6456680

## Slide 8

- CODE AS POLICIES · FIRST PAPER
- Code as Policies：第一篇与定义
- 第一篇以“Code as Policies”命名并系统提出该范式的是 2022 年的 Google Robotics 论文。
- 2022.09.16
- Code as Policies: Language Model Programs for Embodied Control
- 定义：Code-as-Policy 是一种机器人中心的 Language Model Program 形式。
  LLM 生成可执行 policy code，该代码处理感知输出、调用控制 primitive/API，并可表达 reactive policy 或 waypoint-based policy。
- Source: Liang et al., arXiv:2209.07753.
- （图片）图片 23 5076825x4124325

> 备注：arXiv:2209.07753 submitted on 16 Sep 2022. Abstract states policy code can express functions or feedback loops that process perception outputs and parameterize control primitive APIs; presents robot-centric formulation of LMPs.

## Slide 9

- CODE-AS-POLICY ABSTRACTION
- CaP 的本质：把机器人行为压进“可执行中间表示”
- 这让 LLM 获得组合性和空间几何推理，但也把能力强依赖于 API、环境反馈和程序安全边界。
- 自然语言任务
- “把红色积木放到蓝碗左边”
- LLM / VLM Agent
- 将任务转成程序结构与变量绑定
- Policy Code
- 函数、循环、条件、几何运算
- Robot APIs
- 感知 / 规划 / 控制 primitive
- 优势
- 可读、可执行、可调试；能调用第三方库；能组合 perception 和 control。
- 瓶颈
- 没有执行反馈时容易幻觉；API 越低级越难；失败经验若不沉淀，下一次仍会犯。
- 演化方向
- 从 one-shot codegen 走向 rollout-grounded repair、skill library、benchmark 和真实机器人闭环。
- 讲 PPT 时，这页要把 CaP 和 VLA 分清楚：CaP 优化的是程序接口层，不是直接学习连续控制器。

## Slide 10

- CAP-X
- CaP-X：Vibe Coding 时代的第一个Code As Policy工作
- 核心价值不是“又一个 agent”，而是把不同 abstraction、perception、interaction 条件系统化。
- CaP-Gym
- interactive environment：agent 写程序控制机器人
- CaP-Bench
- 跨模型、跨任务、跨抽象层评测
- CaP-Agent0
- 训练-free：多轮反馈、视觉差分、skill synthesis
- CaP-RL
- 可验证 reward + RL，提升 success 并 sim2real
- CaP-X 证明了一个重要现象：当人为抽象减少、API 更低级、perception 更不完美时，CaP agent 的性能会明显下降；但 test-time compute 和结构化执行反馈可以缓解这个 gap。
- （图片）图片 25 7740015x2607310

> 备注：CaP-X introduces CaP-Gym and CaP-Bench; evaluates 12 models and studies abstraction/interaction/perceptual grounding; derives CaP-Agent0 and CaP-RL.

## Slide 11

- ASPIRE
- ASPIRE：在控制程序空间里发现可复用机器人技能
- 它把 CaP 从一次性生成，推进到持续探索、失败诊断、修复蒸馏、技能库复用。
- （图片）图片 21 6076315x3679190
- （图片）图片 23 5405755x3364230

> 备注：ASPIRE: Agentic Skill Programming through Iterative Robot Exploration; components include execution engine, skill library, evolutionary search; reports improvements on LIBERO-Pro, Robosuite, BEHAVIOR-1K.

## Slide 12

- （图片）图片 22 8782050x4705350

## Slide 13

- （图片）图片 1 9124950x5391150

## Slide 14

- ENPIRE
- ENPIRE：把真实机器人学习变成 coding-agent 可管理的优化循环
- （图片）图片 27 7931785x5432425

> 备注：ENPIRE modules: EN, PI, R, E; abstract reports coding agents autonomously train policies up to 99% success on dexterous manipulation tasks.

## Slide 15

- （图片）图片 1 11049000x4114800

## Slide 16

- （图片）图片 1 7610475x5781675

## Slide 17

- （图片）图片 1 11077575x4152900

## Slide 18

- （图片）图片 1 5268595x6392545

## Slide 19

- （图片）图片 1 6184900x6507480

## Slide 20

- （图片）图片 1 6848475x5181600

## Slide 21

- （图片）图片 2 7515225x5572125

## Slide 22

- COMPARISON
- 横向比较：每篇文章到底在进化什么？
- 这一页建议放在读完每篇之后，给听众一个收束视角。
- Paper
- 外部状态 z
- 反馈
- 验证/选择
- 定位
- Code as Policies
- policy code
- 语言指令 + few-shot examples
- 程序可执行性 / 机器人任务完成
- 提出范式
- SkillOpt
- skill.md
- scored rollouts
- held-out validation score
- 自进化算法抽象
- CaP-X
- CaP agent / benchmark
- execution feedback / visual diff
- CaP-Bench / sim2real
- 研究平台
- ASPIRE
- control program + skill library
- multimodal traces
- validated fixes / task success
- 经验复用
- ENPIRE
- training code / recipe / infra
- real robot rollouts + logs
- physical task success
- 真实机器人自动算法工程
- 可直接作为 PPT 的“总览表”：不要每篇都堆原图，先让听众知道优化对象。

## Slide 23

- THESIS
- 未来CAP主线不仅仅是“会写代码”
  更是“代码成为可进化状态”
- 把这些论文放到一条线上，会清楚很多：从一次性生成 policy，到闭环搜索，再到经验积累与真实机器人自改进。
- 1 · 代码化策略
- LLM 输出 Python：处理感知、调用控制 API、组成反馈循环。
- 2 · 闭环评测
- 执行代码 → 观测轨迹/错误/奖励 → 给 agent 可验证反馈。
- 3 · 外部状态进化
- skill 文档、程序库、训练 recipe、git 分支都变成可搜索对象。
- PPT 叙事建议：先定义范式，再逐篇说明“优化对象”如何变化。

## Slide 24

- UNIFIED VIEW
- 统一抽象：自进化就是优化外部 artifact z
- 把这几篇 paper 统一起来，可以用一个很简单的闭环公式讲。
- zₜ₊₁ = A(zₜ, τₜ, rₜ, logₜ)
- 其中 z 可以是 skill 文档、policy.py、skill library、training recipe 或 git 分支；τ 是 rollout 轨迹；r 是验证信号；log 是错误、视觉差分、robot trace、训练曲线等可诊断证据。
- Agent A
- LLM / VLM coding agent
- Artifact z
- skill / code / recipe / library
- Environment
- simulator / benchmark / real robot
- Verifier
- reward / unit test / success detector
- Generate
- Execute
- Score
- Edit
- 这页可作为你自己后续工作的 method-story 起点。

## Slide 25

- SOURCES
- 16 / 16
- 参考论文与材料
- Code as Policies: Language Model Programs for Embodied Control
- Liang et al., arXiv:2209.07753, submitted 2022-09-16
- SkillOpt: Executive Strategy for Self-Evolving Agent Skills
- Yang, Gong et al., arXiv:2605.23904, submitted 2026-05-22
- CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation
- Fu et al., arXiv:2603.22435, submitted 2026-03-23
- ENPIRE: Agentic Robot Policy Self-Improvement in the Real World
- Xiao et al., arXiv:2606.19980, submitted 2026-06-18
- ASPIRE: Agentic /Skills Discovery for Robotics
- Lu et al., arXiv:2607.00272, submitted 2026-06-30
- Uploaded current HTML deck
- index.html: existing 22-slide deck with SkillOpt, ASPIRE and ENPIRE sections
- Use as appendix; citations in speaker notes/handout can be expanded if needed.