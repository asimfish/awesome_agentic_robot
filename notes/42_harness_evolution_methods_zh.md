# 42 · Harness 演化方法合评：ACE、MCE、Meta-Harness、Self-Harness、AHE、Harness Updating ≠ Harness Benefit、DGM、Hyperagents、AlphaEvolve、ShinkaEvolve、ThetaEvolve、GEPA、Promptbreeder、STOP、ADAS、AFlow 与相关工作

> 覆盖：ACE（arXiv 2510.04618，ICLR 2026）· Meta Context Engineering（2601.21557）· Meta-Harness（2603.28052）· Self-Harness（2606.09498）· Agentic Harness Engineering / AHE（2604.25850）· Harness Updating Is Not Harness Benefit（2605.30621）· Continual Harness（2605.09998）· DemoEvolve（2605.24539）· SIA（2605.27276）· Darwin Gödel Machine（2505.22954）· Hyperagents（2603.19461）· AlphaEvolve（2506.13131）· ShinkaEvolve（2509.19349）· ThetaEvolve（2511.23473）· GEPA（2507.19457）· Promptbreeder（2309.16797）· STOP（2310.02304，COLM 2024）· ADAS（2408.08435，ICLR 2025）· AFlow（2410.10762，ICLR 2025）· Learning to Discover at Test Time（2601.16175）· Epistemic Uncertainty for Test-Time Discovery（2605.11328）
> 所属主线：T0、T15、T24 · 材料来源：Lil'Log 2026 文；报告第 5.2 节

## 1. 一句话定位

这是 Lil'Log 优化阶梯的完整实例集。**context 一级**：ACE 把上下文当作可演化的 playbook（Generator/Reflector/Curator 三角色，增量条目式更新避免上下文塌缩）；MCE 做双层优化（外层演化技能即上下文管理机制，内层优化任务上下文）；GEPA 的反思式 prompt 演化优于 RL；Promptbreeder 的自指式 prompt 演化连突变 prompt 本身也被演化。**workflow 一级**：ADAS 用 meta agent 在代码空间搜索 agent 设计；AFlow 用 MCTS 在代码表示的工作流空间生成 agentic workflow。**harness code 一级**：Meta-Harness 用 coding agent 优化 harness 代码并输出 Pareto 前沿；Self-Harness 做 weakness mining → bounded proposal → held-in/held-out 双重回归验证；AHE 以可观测性为核心（组件/经验/决策三层可观测，每次编辑是可证伪的文件级声明）；Continual Harness 在长程游戏中同时更新 harness 与蒸馏策略；DemoEvolve 用人类示范补稀疏反馈；SIA 让 Feedback-Agent 决定本轮更新 harness 还是权重。**optimizer code 一级**：STOP 优化 improver 而非解本身（弱模型下退化）；DGM 让 coding agent 修改自身 harness 代码库并开放式演化（SWE-bench 20% → 50%）；Hyperagents 引入元代理控制如何修改任务代理。**程序演化搜索**：AlphaEvolve 用冻结 LLM 生成程序 diff 的演化搜索（EVOLVE-BLOCK 标记可改区域）；ShinkaEvolve 的开放式样本高效演化（新颖性拒绝采样、多模型集成）；ThetaEvolve 的测试时学习；Learning to Discover / Epistemic Uncertainty 的测试时发现。**警示**：Harness Updating Is Not Harness Benefit——写 harness 的能力从 9B 到 Opus 几乎持平，利用 harness 的能力非单调。

## 2. 对机器人侧的意义（逐级）

- context 一级 → SkillOpt（notes/05）、Harness VLA 的规则记忆（notes/20）、HyMeS 的代码记忆（notes/13）。ACE 的"增量条目式更新避免塌缩"与 SkillGLoW 的"文档塌缩 vs 条目膨胀"诊断（notes/07）是同一问题。
- workflow 一级 → ASPIRE 的执行引擎 → 诊断 → 修复 → 验证（notes/04）、HARBOR 的分阶段 agent（notes/08）。
- harness code 一级 → RHO 的策略仓库（notes/03）、SHAPER 的 context-code harness（notes/07）、Zetta 的运行时 critic（notes/07）。Self-Harness 的 held-in/held-out 双重回归验证是机器人侧最缺的纪律——目前只有 SkillOpt 类工作有 held-out 门。
- optimizer code 一级 → HiSME 的元技能（notes/41）、SkillOpt-Lite 的 HarnessOpt；机器人侧还没有"演化演化器"的工作。
- 程序演化搜索 → MEMENTO 的模因演化（notes/07）、ENPIRE 的多 agent 假设搜索（notes/06）；ShinkaEvolve 的新颖性拒绝采样是缓解 ENPIRE 假设重复（8 倍机器人 2-3 倍加速）的现成工具（报告开放问题第 5 条）。

## 3. 口径与局限

- SWE-bench 20% → 50%（DGM）等数字全部是软件基准；它们证明的是搜索方法有效，不是方法在物理反馈下有效。
- 这些方法的验证器（测试用例、基准分数）廉价且客观；搬到机器人时，验证成本会把"每个 epoch 几十个候选编辑"（SkillOpt）这类预算压到个位数。
- Harness Updating ≠ Harness Benefit 提示：任何机器人 harness 论文报告的收益都应当附带"换基座模型后收益如何变化"。

## 4. 延伸批判

这组工作的共同结构——提议编辑、验证、接受/拒绝、保留历史——与遗传算法、贝叶斯优化并无本质区别，新的是提议者（LLM）能读懂失败日志并给出有语义的编辑。机器人侧真正需要从这里借的不是搜索算法，而是三条纪律：held-out 验证（Self-Harness）、可观测性与可证伪声明（AHE）、只读评估器（AHE）。目前机器人侧的自进化工作里，只有 SkillOpt 类满足第一条，几乎没有工作明确满足第三条——Zetta 与 MEMENTO 都在演化评估器。这是本仓库对 Robot RSI 现状最重要的批评。
