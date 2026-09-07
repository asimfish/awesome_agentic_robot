# 43 · AI 研发基准与失败模式合评：PaperBench、RE-Bench、MLE-bench、ScienceAgentBench、CORE-Bench、KernelBench、Early Science Acceleration 与《Why LLMs Aren't Scientists Yet》

> 覆盖：PaperBench（arXiv 2504.01848，ICML 2025）· RE-Bench（2411.15114，ICML 2025）· MLE-bench（2410.07095）· ScienceAgentBench（2410.05080，ICLR 2025）· CORE-Bench（2409.11363，TMLR 2024）· KernelBench（2502.10517）· Early science acceleration experiments with GPT-5（2511.16072）· Why LLMs Aren't Scientists Yet（2601.03315）· Emergent autonomous scientific research capabilities of LLMs（2304.05332）
> 所属主线：T0、T24 · 材料来源：Lil'Log 2026 文的参考文献 [28]-[35]

## 1. 一句话定位

自动研究需要度量。这组基准从六个角度衡量 AI 做研发的能力：复现论文（PaperBench 评测 AI 复现 AI 研究论文；CORE-Bench 评测计算可复现性）、对比人类专家做 AI R&D（RE-Bench）、机器学习工程（MLE-bench 的 Kaggle 式任务）、数据驱动的科学发现（ScienceAgentBench）、写高效 GPU kernel（KernelBench，harness 演化常用的可验证任务）。两篇经验报告给出两端：《Early science acceleration experiments with GPT-5》是前沿模型加速科研的早期正面案例集；Trehan & Chopra 的《Why LLMs Aren't Scientists Yet》从四次自主研究尝试里总结出六类失败模式——训练数据默认偏置、实现漂移、记忆退化、过度乐观、领域知识不足、科学品味弱。Boiko 等 2023 年的工作是 LLM 驾驭实验室自动化（含云实验室）的早期案例。

## 2. 对 Robot RSI 的意义

机器人侧的自动研究（ENPIRE、HARBOR、Nautilus、AgenticRobotics，notes/06、08）目前没有对应的基准。这组软件侧基准提示了三个可以直接移植的维度：

- **复现**（PaperBench/CORE-Bench）：给 coding agent 一篇机器人论文与开源代码，能否在仿真里复现报告的成功率——Nautilus 的"一句 prompt 到复现工作流"正是这个任务，但没有基准化。
- **与人类专家对比**（RE-Bench）：ENPIRE 的"pin insertion 收敛到 100% 快于一个前沿 human-in-the-loop 方法"是一个孤立的数据点，缺少标准化的人类专家基线。
- **工程任务**（MLE-bench/KernelBench）：HARBOR 的 6 基准 16 任务是机器人 RL 工程的雏形基准。

Trehan & Chopra 的六类失败模式在机器人侧的形态（报告 I9）："仿真 100% 真机 60%"（过度乐观 + 实现漂移）、多个 agent 试同一想法（多样性塌缩，Lil'Log 的表述）、把噪声当信号宣布成功（过度乐观 + 弱评估器）。

## 3. 口径与局限

- 这些基准评的是软件 agent；机器人 R&D 的额外成本（真机时间、复位、硬件损耗）在任何一个基准里都没有建模。
- 《Early science acceleration》是案例集而非受控评测。
- 六类失败模式来自四次尝试的定性总结，不是统计结论。

## 4. 延伸批判

本仓库最缺的一份东西，是一个"Robot Autoresearch Bench"：固定仿真环境与真机接口、固定人类基线、固定验证器，让 ENPIRE 式系统的收敛速度、MRU/MTU、假设多样性、真机迁移差距可以跨论文比较。它的设计可以直接借 RE-Bench 的人类对照协议、CORE-Bench 的复现判定与 KernelBench 的可验证任务形式，再加上 EmbodiedGovBench（notes/25）的治理维度。在这份基准出现之前，本仓库数字口径账本（insights/12）里所有"自动研究"的数字都只能定性定位，不能定量比较。
