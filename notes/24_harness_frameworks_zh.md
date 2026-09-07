# 24 · Harness 框架合评：RoboHarness、Guava、Cortex 与 Agentic Harnesses

> 覆盖：RoboHarness（arXiv 2607.18060，2026-07，华为诺亚 · UBC · 多伦多）· Guava（2606.18363，2026-06）· Cortex（2607.05377，2026-07）· Agentic Harnesses（2608.09857，2026-08，另见 notes/19）
> 所属主线：T15、T1、T4、T20 · 材料来源：具身纪元文章点名 RoboHarness；报告第 4 章 T1/T15

## 1. 一句话定位

2026 年 6-8 月出现了一批"围绕冻结模型的机器人 harness 框架"，各自回答一个不同的问题：RoboHarness 问异构策略（VLA、RL、TAMP）怎么被当作可复用的 agentic 技能来调度——用执行记忆刻画能力边界，用 Memory Bridge 在切换前把机器人带到下一策略熟悉的状态（135 次真机实验，使用 GPT-5.5 改策略编排代码）；Guava 问什么构成有效且通用的具身 harness——系统探索设计空间得到三要素（迭代感知-推理-动作循环、语义动作抽象、多模态观测）并蒸馏进 4B 模型；Cortex 问高层规划语义与低层执行运动学之间的缝怎么补——32 个规范技能原语的双向对齐规划接口；Agentic Harnesses 问规划出的动作该不该执行——LLM 验证层。

## 2. 各篇要点

**RoboHarness**：长程任务需要没有单一策略能全部提供的多样能力；异构策略互补，但编排它们要推理不确定的能力边界与跨策略的分布不匹配——现有规划方法建立在同质、预定义、适用性固定的技能上，忽略了这一点。方法：把独立开发的机器人控制系统（VLA、RL 策略、TAMP）封装为可复用 agentic 技能，用多模态执行记忆刻画每个策略的能力边界，用 Memory Bridge 引导机器人进入下一策略的分布内区域。具身纪元文章的例子：先让 VLA 打开柜门取出积木，再交给 TAMP 精确搭桥；135 次真机实验。

**Guava**：通过系统探索 harness 设计空间得到有效具身 harness 的三个要素——迭代的感知-推理-动作循环、语义动作抽象、多模态观测；并把 harness 释放的能力蒸馏进一个 4B 模型，说明 harness 既是运行时也是训练数据的来源。

**Cortex**：VLA 的马尔可夫性质使其在长程上失效；分层双系统方法有规划语义与执行运动学之间的缝。方法：把操作子任务标准化为 32 个规范技能原语，构建双向对齐的规划接口，让高层 VLM 输出可执行、可处理的子任务计划给低层 VLA。它是"用有限原语集合约束规划输出"的代表。

**Agentic Harnesses**：见 notes/19；此处强调它把 harness 的职责从"完成任务"扩展到"判断允许"。

## 3. 口径与局限

- RoboHarness 的 135 次真机实验是本组唯一的真机规模数字；成功率与任务集见正文。
- Guava 的三要素来自设计空间探索，探索的基准范围决定结论的普适性；4B 蒸馏模型的性能与前沿模型 harness 的差距摘要未说明。
- Cortex 的 32 个原语是人工标准化的——这正是 CaP-X 警告的"设计者脚手架"。

## 4. 关系定位与延伸批判

这四篇与 Harness VLA（notes/20）、Thea（notes/22）、PhyAgentOS（notes/21）一起构成 T15 的密集带。把它们按"harness 治理什么"排列：Cortex 治理规划输出的形式、Harness VLA 治理 VLA 的调用时机、RoboHarness 治理异构策略间的交接、Agentic Harnesses 治理动作的许可、PhyAgentOS 治理整个会话、Thea 治理状态读取与结果判断、Guava 则回答"以上哪些是必需的"。RoboHarness 的 Memory Bridge 是 BATON"进入条件"问题（notes/14）在异构策略上的解法，与 Harness VLA 的 MOVE_TO 预定位同源。未走之路：这些 harness 各自定义了自己的技能接口（RoboHarness 的 agentic skill、Cortex 的 32 原语、Guava 的语义动作抽象），没有一个与 MHS / ROS 2 Harness Profile（notes/23、36）这类标准接口对接——harness 层的碎片化正在重演策略层的碎片化。
