# 08 · 自动研究谱系：Eureka → DrEureka → HARBOR / Nautilus / AgenticRobotics / Push-T 重访

> 覆盖：Eureka（arXiv 2310.12931，ICLR 2024，NVIDIA · UPenn · Caltech · UT Austin）· DrEureka（2406.01967，RSS 2024）· HARBOR（2606.08610，2026-06）· Nautilus（2605.11665，2026-05）· AgenticRobotics（2608.07555，2026-08）· Revisiting Push-T with Agentic Robotics（2608.18227，2026-08，Goldberg 组）
> 所属主线：T2、T9、T11、T24 · 材料来源：具身纪元文章"自动研究"节；报告第 3.3、6.2 节

## 1. 一句话定位

"让 AI 改进制造机器人能力的方法"这条线比 ENPIRE 早三年就开始了：Eureka（2023）让 LLM 写奖励函数、RL 学策略、结果反馈回 LLM 改奖励；DrEureka（2024）让 LLM 同时写域随机化的参数范围，把自动研究推进到 sim-to-real；2026 年 HARBOR 把仿真 RL 的整条工程流水线 harness 化，Nautilus 把"复现/评测/微调/部署"做成一句 prompt，AgenticRobotics 把策略改进做成可以让人离开的控制平面，Goldberg 组的 Push-T 重访则展示了 coding agent 在仿真里"不要示范也能赢"。具身纪元文章把这条线归入 Robot RSI 矩阵的"自动研究"环节。

## 2. 各篇要点

**Eureka**：大模型编写奖励函数代码，RL 在仿真中训练策略，实验结果反馈给大模型修改奖励。在 83% 的测试任务上超过人工设计的奖励；标志性演示是五指机械手转笔。它的分工——LLM 决定"什么动作值得奖励"，连续控制仍由 RL 学出——正是后来 ENPIRE 混合方案（代码决定阶段、VLA/RL 做接触）的雏形。

**DrEureka**：在自动写奖励之外，让 LLM 设置摩擦、质量、外力等仿真参数的变化范围，训练能适应多种物理条件的策略；四足机器人在仿真里学会站上瑜伽球并带球移动，随后迁移真机。它回答的是"自动研究出来的能力如何在现实中成立"。

**HARBOR**：把机器人 RL 自动化定义为 harness 工程问题——给定仿真代码库与任务规格，自动化从环境搭建到策略训练的全流程；高层目标被分解为有界阶段，由专门 agent 通过标准化命令、持久产物、可执行门与可复用知识执行，并用去中心化并行试验与跨运行的经验学习扩展迭代。6 个基准 16 个任务（操作、行走、双臂灵巧）。它是 Lil'Log 三模式（工作流自动化、文件系统即记忆、子代理）在机器人 RL 工程上的完整实例。

**Nautilus**：诊断是机器人学习研究在策略族、基准套件与真机之间碎片化，通用 coding agent 缺少机器人研究的过程先验与验证习惯；提供带蒸馏先验的 agent 技能集、策略/仿真/真机之间的类型化契约、统一接口与执行环境、每个里程碑自动验证的可信 agentic 工作流。

**AgenticRobotics**（You Don't Need To Stay in The Loop）：把 Claude Code / Codex 式的"主 agent 管循环、子 agent 分析执行、工具干活"架构移植到策略改进，核心差异是机器人工具（训练好的策略、训练流水线、数据采集）会经常失败，因此每次调用都要测量、记录工具质量，产物变化时过期。设计：不可变目标、控制器拥有的测量、commit 键控的崩溃恢复、证据分级技能库、带标准化记录调用面的工具注册表。"人可以离开"是操作性声明：晋升是证据门控的、状态可恢复、能力质量由记录导出。

**Push-T 重访**：Claude Code（Fable 5）在没有任何示范的情况下，自己找到 2D gym 仿真、用仿真实验学习推的力学、迭代优化，达到 100% 成功且比用 200 条人类示范训练的最佳扩散策略少 46% 步数；还用自生成课程解决 Push-A 到 Push-Z，并生成 Franka 与 UR5 的 3D 跨本体仿真代码。与 ENPIRE 真机 Push-T 的 60-95% 对照，这是"仿真里 coding agent 已经赢了，真机上还没有"的最清楚证据。

## 3. 口径与局限

- Eureka 的 83% 是"超过人工奖励的任务比例"，不是成功率；DrEureka 的真机结果是演示级。
- HARBOR、Nautilus 都在仿真/工程层验证，摘要没有真机策略成功率。
- AgenticRobotics 的关键数字是运行层的（硬化后假阳性晋升率 0.001），不是任务成功率。
- Push-T 重访是短文，100% 为仿真、脚本判定。

## 4. 关系定位与延伸批判

把这六篇与 ENPIRE（notes/06）放在一条线上，可以看到自动化的对象逐级上移：奖励函数（Eureka）→ 仿真参数（DrEureka）→ 整条训练流水线（HARBOR）→ 研究工作流（Nautilus）→ 真机改进循环（ENPIRE）→ 让人离开的控制平面（AgenticRobotics）。这正是 Lil'Log 优化阶梯从 context 到 optimizer code 的机器人版本。两个未走之路：其一，Eureka 式"LLM 写奖励"与 2026 年"LLM-as-a-Verifier 当密集奖励"（notes/19）尚无直接对照——前者写的是奖励的代码，后者用模型当奖励，谁更抗奖励作弊值得一测；其二，AgenticRobotics 的"证据分级技能库"与 ASPIRE 的"验证过的修复"是同一概念的两种实现，把证据等级作为技能检索的排序信号还没有人做。
