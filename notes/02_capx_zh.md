# 02 · CaP-X 深度解读：把 Code-as-Policy 做成可以被系统研究的平台

> **CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation**
> arXiv 2603.22435（2026-03）· NVIDIA · UC Berkeley · Stanford · CMU · Letian Fu, Justin Yu, Karim El-Refai et al.（共 16 位作者） · 项目页 capgym.github.io
> 所属主线：T2、T9、T22 · 材料来源：讲稿第 10-12 页、小红书长文 04 节；本仓库有首页中译

## 1. 一句话定位

CaP-X 是 Code-as-Policy 的"研究平台四件套"：CaP-Gym（交互环境）、CaP-Bench（分层评测）、CaP-Agent0（无需训练的 agentic 框架）、CaP-RL（对 coding agent 做可验证奖励的强化学习）。它第一次把"Agent 的能力"与"设计者给的脚手架"拆开衡量，结论是成功率随人工抽象而升、随抽象撤除而降，但测试时计算（多轮交互、执行反馈、视觉差分、技能合成、集成推理）能把低层原语上的鲁棒性补回来。

## 2. 要解决的问题

先前的 CaP 系统依赖高层的人工原语，因此无法回答两个问题：LLM 到底会不会控制机器人，还是只会调用别人写好的宏？不同模型、不同交互方式、不同感知接地方式之间的差异有多大？没有统一的交互环境与分层评测，这些问题无法被系统研究。

## 3. 方法

- **CaP-Gym**：建立在 Gymnasium 接口上的分层控制框架，把低层环境循环（物理仿真或真机）与有状态的代码执行器循环绑在一起，agent 通过合成并执行组合感知/控制原语的程序来控制机器人。
- **CaP-Bench**：三条轴——抽象层级（人工宏 → 原子原语）、时序交互（单轮 S1-S4 / 多轮 M1-M4）、感知接地（不同视觉反馈模态）；7 个核心任务（Cube Lift、Cube Stack、Spill Wipe、Peg Insertion、Cube Re-stack、Two-Arm Lift、Two-Arm Handover），每个 tier 100 次试验，12 个开源与闭源模型。
- **CaP-Agent0**：多轮交互 + 视觉差分模块（把场景变化转成文本）+ 自动合成的任务无关技能库 + 并行多模型代码生成（集成推理），不做任何训练。
- **CaP-RL**：用 GRPO 在 CaP-Gym 里对 Qwen2.5-Coder-7B-Instruct 做可验证奖励的后训练；跨 sim-to-real 迁移的是"代码即动作空间"接口，而不是像素到电机的映射。

## 4. 实验结果与口径

- 12 个模型上，成功率随人工抽象单调上升、随抽象撤除下降（Takeaway 2）；多轮 + 视觉差分 + 低层 API（M4）显著优于单轮低层 API（S3）和单轮高层 API（S2）。
- CaP-Agent0 在 7 个任务中的 4 个上达到与人类专家程序相当的成功率（论文图 8）；在仿真与真机（Franka Panda、AgiBot）上有零样本展示。
- CaP-Bench++ 把 coding agent 与 VLA 直接对比：LIBERO-PRO 位置/指令扰动下 CaP-Agent0 对比 OpenVLA、π0.5（表 2）。
- 口径：每 tier 100 次试验、脚本判定成功；真机数字为零样本展示，试验规模摘要未说明。讲稿与小红书长文引用的"抽象降低则成功率下降"是趋势结论，不是单一数字。

## 5. 局限

1. 论文自己指出程序化控制在接触丰富、需要紧密视觉伺服的任务（插入、倒水）上仍脆弱；给出的方向是 CaP-VLA 混合策略。
2. 多轮交互的代价是时间：CaP-Bench 的多轮 tier 不测实时性，RHO（notes/03）正是针对这一点。
3. 12 个模型的差异同时来自模型能力与 prompt/接口设计，CaP-Bench 控制了接口但不能控制各模型的训练数据。

## 6. 关系定位

CaP-X 是讲稿五篇论文里的"研究平台"一格（$z$ = agent/benchmark，$r$ 来自执行反馈与视觉差分）。它对本仓库的三条主线都有贡献：T2（Code-as-Policy 的系统化）、T9（CaP-RL 是最早对 coding agent 本身做 RL 的机器人工作之一）、T22（视觉差分是一种"为获取信息而观察"的弱形式主动感知）。ENPIRE 的 RoboCasa365 对照（GR00T ≈53%、ENPIRE 混合 ≈77%、CaP-X ≈27%）说明纯代码在 RoboCasa 这类家居长程任务上落后于混合方案。

## 7. 延伸批判

CaP-X 最重要的贡献是方法论：先把脚手架拆掉再谈能力。这个思路应当被反向应用到 VLA 侧——VLA 的成功率里有多少来自基准设计的"脚手架"（固定初始位姿、有限指令模板）？LIBERO-Pro 的扰动评测（RHO、Harness VLA 都在用）是同一思路的另一面。另一个未走之路：CaP-Agent0 的技能库跨试验持久化，但论文没有报告库规模与成功率的关系曲线，这条曲线由 ASPIRE（notes/04）补上。
