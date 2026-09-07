# 06 · ENPIRE 深度解读：把真机学习变成 coding agent 可以管理的优化过程

> **ENPIRE: Agentic Robot Policy Self-Improvement in the Real World**
> arXiv 2606.19980（2026-06-19）· NVIDIA GEAR · CMU · UC Berkeley · Wenli Xiao, Jia Xie, Tonghe Zhang et al.（共 17 位作者） · 项目页 research.nvidia.com/labs/gear/enpire
> 所属主线：T2、T7、T9、T10、T21、T24 · 材料来源：讲稿第 16-21 页（最详细的一份材料）、小红书长文 02/04 节、具身纪元文章；本仓库有首页中译

## 1. 一句话定位

ENPIRE 是面向 coding agent 的真机 harness，用四个模块把"重置场景、执行策略、验证结果、改进下一轮"这条物理反馈回路实例化：环境模块 EN（自动重置与验证）、策略改进模块 PI、Rollout 模块 R（单台或多台真机并行评估）、演化模块 E（coding agent 读日志、查文献、改训练基础设施与算法代码）。借助它，前沿 coding agent 自主开发出在 PushT、插针入盒、剪扎带等灵巧任务上 99% 成功率的策略；8 工位集群把收敛时间压到 1/3-1/2；并提出 MRU / MTU 两个效率指标。它是本仓库"physical autoresearch"的代表，也是具身纪元文章 Robot RSI 矩阵里"自动研究"一格的机器人侧例子。

## 2. 要解决的问题

真机灵巧操作严重依赖人类监督与算法工程：重置场景、判断成败、调参、换算法都是人。coding agent 已经能在数字环境里自动化算法搜索，但缺一个"可重复的真机策略改进反馈回路"作为抽象。ENPIRE 的假设是：把重置、验证、更新、真机试验都做成 agent 可调用的工具，机器人研究就变成 agent 可以管理的可控优化过程，同时还能对训练配方与 agent 变体做公平消融。

## 3. 方法

EN 模块负责自动重置（接触密集任务用 CaP-X 式的程序化工具调用，把环境直接复位到最近一次完整尝试的起点）与成功验证（例如扎带插入后由两个相机共同判断是否穿过锁头）；PI 模块启动策略精炼，支持启发式学习、工具调用、行为克隆、离线/在线 RL 等多种机制；R 模块用一台或多台并行真机评估；E 模块里 coding agent 分析日志、查阅文献、改训练基础设施与算法代码。研究经验以 Markdown 总结的形式在任务之间迁移。

## 4. 实验结果与口径

讲稿第 16-21 页的四组实验（数字为讲稿转述）：

1. **Gym-PushT → 真实 Push-T**：仿真里 Codex 与 Claude Code 约 2 小时达 95%、Kimi 约两倍时间；真机上 Codex 接近 95%，Claude 约 75%，Kimi 约 60%。结论：仿真成功 ≠ 真机鲁棒（摩擦漂移、位姿误差、控制器偏差、启发式对边界敏感）。
2. **Pin insertion**（要求连续 50 次真机成功）：Agent 自行尝试 BC、iterative BC、在线 rollout 聚合、offline RL、online RL、offline-to-online、RL + BC 正则及超参调优；hillclimb 最大一步是 BC regularization +10.8pp。结论：纯 BC 不够，需要策略诱导分布上的迭代数据。
3. **集群规模**：1/4/8 个 Agent 对应 1/4/8 台机器人，Push-T 归一化 1.0 的时间约 5h → 2h，pin insertion 1.5h+ → 40min；8 倍机器人 2-3 倍加速，瓶颈是 Agent 重复探索、等待训练、阅读分支、分析日志。
4. **文本记忆迁移**：多个 Agent 的 pin insertion 研究总结写成 Markdown 放进 GPU insertion 新 Agent 的初始上下文，并刻意删除轨迹、checkpoint、隐藏日志、旧工作区。路径：research experience → textual memory → new autoresearch。

第五组（RoboCasa365 仿真）：GR00T N1.5 约 53%，ENPIRE 产生的混合方案（代码做 hover pose，VLA 做接触阶段）约 77%，CaP-X 约 27%。摘要另给：固定八次重试设置下部分任务 99%；pin insertion 收敛到 100% 快于一个前沿的 human-in-the-loop 方法。口径：真机数字为特定任务、特定重试预算下的成功率；MRU（机器人主动执行时间占比）与 MTU（token 利用率）是效率指标而非成功率。

## 5. 局限

1. 任务集小且都有清晰的自动验证器（PushT 位姿、插针、剪扎带）；验证器难做的任务（叠衣、倒水）不在其中——验证器是 ENPIRE 能否推广的前提（报告 I3）。
2. 三个模型在真机上的差距（95/75/60）来自哪一步（提假设、写代码、读日志）没有拆分；Lil'Log 引用的"写 harness 与利用 harness 是两种能力"提示这一差距未必是"提出改进的能力"。
3. 集群加速亚线性的原因是观察性的（重复探索、等待），没有做去重或分工机制的对照实验。
4. "人力降到最低"针对的是研发循环；硬件维护、任务定义、验证器搭建仍是人。

## 6. 关系定位

ENPIRE 在讲稿公式里 $z$ = 训练代码/配方/基础设施，$r$ = 物理任务成功，$\log$ = 真机日志与训练曲线，$A$ = 前沿 coding agent。对小红书长文它同时是 L6（策略权重被 RL 更新）与 L7（8 工位群体）的实证；对 T21 它给出了"群体提升假设吞吐量而非 rollout 数"这一最诚实的数据；对 T10 它的 EN 模块解决了 RoboClaw（notes/31）用 EAP 解决的同一个自复位问题。与 HARBOR（仿真 RL 工程 harness 化）、Nautilus（一句 prompt 到工作流）、AgenticRobotics（策略改进控制平面）同属 T2 的"研究自动化"分叉（notes/08）。

## 7. 延伸批判

ENPIRE 最有价值的发现是负面的：仿真 100% 不等于真机 60%，8 倍机器人不等于 8 倍速度，纯 BC 到不了 50 次连续成功。这三条分别对应 Lil'Log 的 RSI 挑战里的奖励作弊/过度乐观、多样性塌缩、负面结果。下一步最值得做的不是更多任务，而是把 E 模块里 Agent 的假设去重（ShinkaEvolve 式新颖性拒绝采样）和把 Markdown 研究总结换成结构化、可检索的记忆（HyMeS 式"记忆在代码里"），看 8 工位的加速比能否逼近线性。另一个开放问题：ENPIRE 的验证器（两台相机判断扎带是否穿过）是人写的；当验证器也交给 agent 演化时，如何保持 AHE 式的"只读 verifier"原则，是 Robot RSI 的真正难题。
