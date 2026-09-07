# 05 · SkillOpt 深度解读：把技能文档当作冻结 Agent 的可训练外部状态

> **SkillOpt: Executive Strategy for Self-Evolving Agent Skills**
> arXiv 2605.23904（2026-05）· Microsoft · 上海交通大学 · 同济大学 · 复旦大学 · Yifan Yang, Ziyang Gong, Weiquan Huang et al.（共 15 位作者） · aka.ms/SkillOpt
> 续作：**SkillOpt-Lite: Better and Faster Agent Self-evolution via One Line of Vibe**，arXiv 2607.03451（2026-07）
> 所属主线：T7、T8、T0 · 材料来源：讲稿第 14-15、23 页；本仓库有首页中译

## 1. 一句话定位

SkillOpt 主张技能（skill.md）应当被当作冻结 Agent 的外部状态来训练，并采用使权重空间优化可复现的同一套纪律：独立的优化器模型把打分后的 rollout 转成对单一技能文档的有界增/删/改编辑，只有严格提升 held-out 验证分数的编辑才被接受；文本学习率预算、拒绝编辑缓冲区与按 epoch 的慢速/元更新使训练稳定，部署时零额外推理调用。它不是机器人论文，却是讲稿把"自进化"抽象成 $z_{t+1} = A(z_t, \tau_t, r_t, \log_t)$ 的算法原型。

## 2. 要解决的问题

现有 Agent 技能要么人工编写、要么一次性生成、要么通过松散控制的自我修订演化——没有一种像深度学习优化器那样对待技能，也没有一种能在反馈之下可靠地超越起点。对闭源前沿模型，权重适配不可用；技能文档是唯一可训练的对象，却缺少"训练"的纪律。

## 3. 方法

类比表（讲稿第 15 页）：参数 ↔ 技能文档；梯度方向 ↔ 从轨迹中抽出的编辑方向；学习率 ↔ 编辑预算 $L_t$；验证 ↔ held-out 选择门；负样本 ↔ 拒绝编辑缓冲区；epoch ↔ 慢速/元更新。流程：目标模型带当前技能跑任务 → 评分 → 优化器模型读轨迹并提出有界编辑 → 在 held-out 集上验证，严格提升才接受，否则进拒绝缓冲区供后续参考 → 每个 epoch 做一次慢速元更新整理文档结构。SkillOpt-Lite 把这套流程用零阶优化（中心差分、信任域）重新形式化，提出三条原则——基于文件系统的轨迹探索、共识属性挖掘、独立验证门控——并去掉冗余组件。

## 4. 实验结果与口径

- 6 个基准 × 7 个目标模型 × 3 种执行 harness（直接对话、Codex、Claude Code）共 52 个单元，全部最优或并列最优，击败人工、一次性 LLM、Trace2Skill、TextGrad、GEPA、EvoSkill 技能。
- GPT-5.5：无技能基线上直接对话 +23.5、Codex 循环内 +24.8、Claude Code 内 +19.1 个百分点。
- 消融（讲稿第 15 页转述）：任意适度预算（$L_t$=2-8）优于无界重写，去掉预算 Spreadsheet 77.5→75.7、LiveMath 61.3→57.3；选择门每 epoch 只放行几十个候选里的 1-4 个，OfficeQA 的 +39pp 来自单个被接受的编辑；去掉拒绝缓冲 Spreadsheet 77.5→72.9；去掉 epoch 慢/元更新 Spreadsheet 77.5→55.0（最大退化）。
- 迁移：优化后的技能跨模型规模、跨 Codex/Claude Code 执行环境、迁移到邻近数学基准时无需再优化即保持价值。
- SkillOpt-Lite：LiveMath 在 GPT-5.5 上 +8.8、GPT-5.4-nano 上 +25.4，nano 超过用 SkillOpt 优化的标准 GPT-5.4；并把方法推广到整套 harness（HarnessOpt），GPT-5.4-nano 在 SpreadsheetBench 上超过跑标准流水线的 GPT-5.5。
- 口径：全部是软件/推理基准的准确率；"+23.5 个点"是对无技能基线的绝对百分点提升。

## 5. 局限

1. 任务是数字世界的可验证任务（表格、数学、办公问答），held-out 验证廉价；搬到机器人上，"held-out 集"意味着真机 rollout，验证成本是 SkillOpt 纪律能否成立的第一道门槛。
2. 优化器模型与目标模型的关系摘要未展开：优化器更强时收益如何归因，是"更强模型代写技能"还是"目标模型学会了"？Lil'Log 引用的 Lin 等（Harness Updating ≠ Harness Benefit）正是对这一点的追问。
3. 52/52 是"最优或并列"，并列的比例摘要未说明。

## 6. 关系定位

SkillOpt 在 Lil'Log 优化阶梯的 structured context 一级；在讲稿公式里 $z$ = skill.md、$r$ = held-out 分数、$A$ = 优化器模型。机器人侧的对应物是 ASPIRE（$z$ = 技能库）、Harness VLA（$z$ = VLA 使用规则）、Zetta（$z$ = 运行时 critic 与恢复技能）。它对机器人侧最有价值的输出不是数字，而是"选择门 + 有界编辑 + 拒绝缓冲 + 慢更新"这四条纪律——具身纪元文章的 RSI 定义（无法验证的变化只能叫变化）与这里的严格提升门是同一原则。

## 7. 延伸批判

SkillOpt 的成功很大程度上来自任务有便宜且客观的验证器。机器人任务缺的正是这个（notes/17-19、报告 I3）。因此把 SkillOpt 搬到机器人的最小可行实验，不是换任务，而是先换验证器：用 PRIMO R1 式的过程级判断或 VERITAS 式的视觉验证器充当 held-out 分数，看选择门在噪声验证下是否仍能保证"严格提升"。另一个未走之路：SkillOpt 只训练一份文档；机器人技能库是多份文档 + 代码，PRACTICE 的批量编辑与 SkillGLoW 的过程族（notes/07）是向这个方向的两步。
