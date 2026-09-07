# 32 · VLA + RL 合评：信用分配、免外部奖励与测试时 RL

> 覆盖：Temporal GRPO（arXiv 2608.13026，2026-08）· TEMPO（2608.07314，2026-08）· WCM（2607.29613，2026-07）· Z-1（2606.31846，2026-06）· SAC Flow（2509.25756，2025-09）· TT-VLA（2601.06748，2026-01）· RL²-VLA（2607.26991，2026-07）· T²VLA（2606.29892，2026-06）· CaP-RL（见 notes/02）
> 所属主线：T9 · 材料来源：检索地图 T9 代表工作；报告第 4 章 T9

## 1. 一句话定位

VLA + RL 在 2026 年从"能不能"变成了"怎么分配信用、怎么在没有奖励时做、怎么在测试时做"。信用分配：Temporal GRPO 按可检测的任务阶段分配优势，解决轨迹级信用混叠；TEMPO 冻结 VLM 主干，语义投影层低频、动作专家高频的双时间尺度更新；WCM 让 critic 同时预测未来 latent 与价值以匹配部分可观测性（149 个任务上 SOTA）。免外部奖励：T²VLA 发现离散动作 VLA 的生成置信度与成功显著相关，用它作内在奖励做测试时 RL；RL²-VLA 只在预测失败时激活潜空间组合式引导（OOD 最多 +17.3%）。效率：Z-1 在 π0.5 上只用公开 RoboCasa 示范做 SFT 再做任务级 GRPO，24 任务 80.6%；SAC Flow 把 flow rollout 视为残差 RNN，用门控/Transformer 速度网络稳定 off-policy RL；TT-VLA 用逐步任务进度的密集奖励做测试时 RL。

## 2. 各篇要点

**Temporal GRPO**：GRPO 式后训练把一个 rollout 级优势加到轨迹里每个动作上，完成了几个有效阶段却在后面失败的 rollout 会惩罚产生早期进度的动作——"轨迹级信用混叠"。方法：构造可检测的任务阶段，把每个 rollout 与阶段特定的动作区间对齐，只比较同阶段的 rollout。它把"阶段检测"（一个验证器问题）变成了 RL 信用分配的前提。

**TEMPO**：SFT 易分布不匹配，现有 RL 对所有组件用同一更新策略。方法：冻结预训练视觉语言主干保留通用语义，适配限于两个组件——语义投影层（慢时间尺度）与动作专家（快时间尺度）。它是双系统思想在训练动力学上的体现。

**WCM**：critic 基于单帧观测或单帧 VLM latent，与机器人控制的部分可观测性根本不匹配；朴素地加历史会指数复杂且标量回报回归监督不足。方法：World Critic Model，同时预测未来 latent 与价值；149 任务 SOTA（报告转述）。

**Z-1**：面向 flow-based VLA 的 RL 后训练；基于 π0.5，只用公开 RoboCasa 示范 SFT，再任务级 GRPO；RoboCasa 24 任务 80.6%（报告转述）。

**SAC Flow**：flow 策略的 off-policy RL 不稳定，因为 flow rollout 在代数上等价于残差递归计算，会像 RNN 一样梯度消失/爆炸；用现代序列模型原理重参数化速度网络（Flow-G 门控、Flow-T Transformer）。

**TT-VLA / T²VLA / RL²-VLA**：三种测试时改进——TT-VLA 用逐步进度奖励在部署中做 RL；T²VLA 用生成置信度当内在奖励，架构无关；RL²-VLA 自适应地只在基座可能失败时介入，用潜空间组合式引导打破"动作样本集中在相似行为、继承相关失败模式"的问题。

## 3. 口径与局限

- 80.6%（RoboCasa 24 任务）、+17.3%（OOD）、149 任务 SOTA 分别来自不同基准与基座，不可并排。
- Temporal GRPO 需要"可检测的阶段"，其检测器的准确率决定信用分配的正确性——阶段检测与 PRIMO R1 的进度估计（notes/17）是同一问题。
- 置信度作为内在奖励（T²VLA）有 Consilience（notes/19）讨论的过度乐观风险：置信高不等于物理成功。
- 绝大多数在仿真；ARLI（notes/27）指出真机 RL 还要处理推理延迟。

## 4. 关系定位与延伸批判

这一组与 LWD（notes/28）、Q-Planning（notes/29）、TwinRL（notes/30）合起来构成 T9 的完整图景：训练时（Z-1、TEMPO、WCM、SAC Flow）、部署时（LWD、Q-Planning、TT-VLA、T²VLA、RL²-VLA）、仿真预热（TwinRL）。三个观察：（1）信用分配正在向"阶段"收敛——Temporal GRPO 的阶段、BATON 的子任务、AGM 的子目标、PRIMO R1 的进度是同一对象在 RL、探索、记忆、验证四个视角下的名字；（2）"何时介入"成为共同问题——RL²-VLA 的失败预测门控与 StreamVLA 的完成态门控（notes/26）同构；（3）免外部奖励的代价是信号来自策略自身，Lil'Log 的奖励作弊警告在这里最锋利。未走之路：把 LLM-as-a-Verifier 的连续分数（notes/19）当作 Temporal GRPO 的阶段奖励，是把 T23 与 T9 接起来最便宜的实验。
