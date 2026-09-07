# 35 · Agent + Robot 总览合评：Agentic Robot、ManiAgent、VoLo、HoloAgent-0 与"灵活但仍脆弱"

> 覆盖：Agentic Robot（arXiv 2505.23450，2025-05）· ManiAgent（2510.11660，2025-10）· VoLo（2606.07723，2026-06）· HoloAgent-0（2606.23565，2026-06）· Agentic AI for Robot Control: Flexible but still Fragile（2602.13081，2026-02）· Cortex（见 notes/24）· Guava（见 notes/24）
> 所属主线：T1、T4、T23 · 材料来源：检索地图 T1 代表工作；报告第 4 章 T1

## 1. 一句话定位

T1 主线回答"把 LLM/VLM 的推理接到真实机械臂上能否形成闭环"。Agentic Robot 用 Standardized Action Procedure 协调推理模型、VLA 执行器与时序验证器（LIBERO 长程 79.6%）；ManiAgent 用多 agent 协作做环境感知、任务分解与动作生成（SimplerEnv 86.8%），并用 agent 给 VLA 生成训练数据；VoLo 让 VLM 把 VLA/WAM 当作**可中断的工具**在执行中途干预，并把"决策、动作与工具调用的时序在不会暂停的物理世界里很重要"命名为物理编排（Physical Orchestration）；HoloAgent-0 用 Embodied AgentOS + 3D 空间记忆把操作、空间理解、导航、人形控制统一进一个执行循环；"Flexible but still Fragile"则是这条线最清醒的真机报告：两台真机平台之间迁移只需改系统 prompt，但非确定性行为、指令遵循错误与对 prompt 措辞的高敏感性普遍存在。

## 2. 各篇要点

**Agentic Robot**：长程操作的误差累积与执行中缺少验证机制；脑启发的三角色——推理模型规划、VLA 执行、时序验证器核对——由 Standardized Action Procedure 协调。LIBERO 长程 79.6%。

**ManiAgent**：VLA 在复杂推理与长程规划上受数据与容量限制；多 agent 通过 agent 间通信完成环境感知、子任务分解与动作生成，从任务描述到动作端到端输出；SimplerEnv 86.8%；还能为 VLA 生成训练数据——agent 系统作为数据引擎的早期例子。

**VoLo**：闭环 agent 循环中 VLM 编排异构机器人能力为可中断工具；与虚拟 agent 不同，物理世界不为推理暂停，因此何时决策、何时中断、何时调用工具的时序是一等问题。它把 T13 双系统的"何时切换"（notes/26）提升为 agent 层的编排问题。

**HoloAgent-0**：LLM agent 在数字环境的循环（结构化状态 → 调用工具 → 检查反馈 → 修订）难以直接延伸到连续、依赖本体、不确定且受安全约束的物理执行；用 Embodied AgentOS 与 3D 空间记忆统一多种具身能力。

**Flexible but still Fragile**：推理型语言模型在迭代的规划器-执行器循环里选择并调用机器人技能，部署在两个平台（室内移动操作 Mobipick 的桌面抓放与箱体插入；农业自主导航）。发现：跨平台迁移只改系统 prompt；但非确定性、指令遵循错误、prompt 敏感普遍存在。

## 3. 口径与局限

- 79.6%（LIBERO 长程）与 86.8%（SimplerEnv）是仿真基准上的成功率，基座与任务集不同，不可并排；"Fragile"论文是真机定性 + 少量统计。
- 多 agent 架构（ManiAgent）的 agent 间通信开销与非确定性未量化——Tool-RoCo（notes/37）后来发现 agent 很少把彼此当工具用。
- VoLo 的"可中断"依赖 VLA/WAM 支持中途中断与安全停止，这是硬件与策略层的前提。

## 4. 关系定位与延伸批判

把这组工作与 AgenticLab（notes/34）、Cortex 与 Guava（notes/24）放在一起，T1 的骨架已经标准化：感知 → 分解 → 执行 → 验证 → 重规划，差别只在验证器（时序验证器 / 谓词效果检查 / exit codes）与执行器（VLA / 代码 / 混合）。"Flexible but still Fragile"给出的三条脆弱性——非确定性、指令遵循错误、prompt 敏感——恰好对应 ROSClaw 的发现（不同前沿模型越权动作率差 3.4-4.8 倍，执行层设计比 prompt 措辞更影响安全，notes/36）：可靠性来自执行层与验证层，不来自更好的 prompt。这也是本仓库把 T15/T16/T23 视为 2026 年重心的原因。未走之路：VoLo 的"物理编排"时序问题与 Harness Engineering for Physical AI 的 Isolation（notes/23）是同一问题的 agent 层与中间件层表述，尚无工作把两层的时序预算统一起来。
