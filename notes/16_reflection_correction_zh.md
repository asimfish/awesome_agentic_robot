# 16 · 反思与纠错合评：REMAC、PhysReflect-VLA、Agentic RAG-VLM、PhysiAgent

> 覆盖：REMAC（arXiv 2503.22122，2025-03）· PhysReflect-VLA（2606.27146，2026-06）· Agentic RAG-VLM（2606.31200，2026-06）· PhysiAgent（2509.24524，2025-09）
> 所属主线：T6、T4、T19、T23 · 材料来源：检索地图 T6 代表工作；小红书长文 02 节的 L1-L7 分层

## 1. 一句话定位

小红书长文给了一个判断标准："Retry ≠ Learning"——反思的价值取决于它能否被写进持久对象。这一组工作展示了反思在 L2-L3 的四种形态：REMAC 用前置/后置条件检查与场景推理做多机器人长程重规划（成功率 +40%）；PhysReflect-VLA 在执行时给 VLA 加物理可行性评估与结构化自反思（接触密集真机任务平均 +5.4%）；Agentic RAG-VLM 用 14 类失败分类与三级自适应重试把杂乱场景抓取从 25% 提到 78.3%；PhysiAgent 让 VLM 根据 VLA 的实时熟练度反馈组织 monitor、memory、reflection 组件。

## 2. 各篇要点

**REMAC**：面向多机器人长程操作的自适应规划：前置条件与后置条件检查让每一步执行前后都被验证，场景特定的自进化让规划随环境反馈改进；报告数字为成功率 +40%（相对基线）。它同时属于 T4（长程）、T19（多机器人）、T23（验证器）——前/后置条件是验证器最古典的形式。

**PhysReflect-VLA**：即插即用的执行时可靠性框架。可行性算子评估候选动作是否产生动力学一致的状态转移；动作解释算子核查转移一致性；LLM 反思模块分析状态差异、生成纠正指令回灌控制回路。数字：接触密集真机任务平均 +5.4%。它把"反思"细化到了单步动作层面，比 episode 级反思更接近控制。

**Agentic RAG-VLM**：面向杂乱环境抓取。诊断：VLM 抓取方法靠视觉相似度匹配物体，忽略把手可抓性、材料脆性等物理 affordance，且开环、无空间推理与失败恢复。方法：分层 affordance 感知的 RAG + VLM 语义理解 + agentic 自反思规划，14 类失败分类与三级自适应重试。数字：杂乱场景抓取 25% → 78.3%。

**PhysiAgent**：诊断 VLM + VLA 的"僵硬串联"（VLM 只做高层理解与规划、VLA 只当执行器）导致协作低效与接地差。方法：monitor、memory、self-reflection 机制 + 轻量现成工具箱构成自主脚手架，VLM 根据 VLA 的实时熟练度反馈组织这些组件。它是 2025 年"Agent 围绕 VLA"配方的一个早期完整实例。

## 3. 口径与局限

- 四篇的数字分别是相对提升（REMAC +40%、PhysReflect +5.4pp）与绝对成功率（Agentic RAG-VLM 25→78.3%），任务集与判定方式各不相同，不能并排。
- PhysReflect-VLA 的可行性算子需要某种动力学一致性模型，其来源与泛化性摘要未说明。
- Agentic RAG-VLM 的 14 类失败分类是人工定义的，覆盖面限于抓取。
- 四篇的反思结果是否跨 episode 持久化（写进记忆或技能）：REMAC 的自进化与 PhysiAgent 的 memory 有此意图，PhysReflect 与 Agentic RAG-VLM 主要是 episode 内纠正。

## 4. 关系定位与延伸批判

按 L1-L7 分层，PhysReflect-VLA 与 Agentic RAG-VLM 落在 L3（反思产生纠正指令），REMAC 与 PhysiAgent 触及 L4（记忆演化）。真正把反思写进持久对象的是 Harness VLA（学 VLA 的适用范围，notes/20）、ASPIRE（修复即技能，notes/04）与 AGM（进度指针，notes/12）。这组工作最值得追问的是**反思的成本-收益**：PhysReflect 的 +5.4pp 来自每步都跑三个算子，控制频率受多大影响未报告；Agentic RAG-VLM 的 78.3% 用了三级重试，重试次数计入成本后与单次成功率如何比较（同一问题见 Zeva 的 CSR@K 讨论）。反思类方法应当同时报告"每次成功的平均尝试数"，否则与更贵的 retry 无法区分——这一点应成为 T6 主线的口径规范。
