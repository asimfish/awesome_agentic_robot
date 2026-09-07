# 27 · 端侧部署合评：PhyAI、EcoVLA、CloudEdgeVLA、ARLI、ST-Merge、Habilis-β

> 覆盖：PhyAI（arXiv 2608.03682，2026-08）· EcoVLA（2608.15502，2026-08，APPT 2026）· CloudEdgeVLA（2608.00569，2026-08）· ARLI / Learning to Act While Waiting（2608.23831，2026-08）· ST-Merge / Fast Enough to Act（2606.29350，2026-06）· Habilis-β（2602.18813，2026-02）
> 所属主线：T14、T9 · 材料来源：小红书长文 03 节（"Cloud can think. Edge must survive."）；报告第 4 章 T14、第 7 章 I5

## 1. 一句话定位

大模型上云、控制在端，延迟、抖动与断网怎么办——这组系统工作给了 2026 年的答案：PhyAI 用一个运行时统一 VLA/WAM 在板载、边缘、云端的推理（对 π0、π0.5、GR00T N1.7、MiniCPM-Robot 提速 1.40-4.65 倍）并提出 control-time Roofline 区分推理受限与环境受限的控制；EcoVLA 做设备-边缘协同推理的能效优化（20 Hz 约束下能效 +236%）；CloudEdgeVLA 把时间错位当作表示学习问题——云端编码慢变任务特征、边缘头结合最新本地视觉，40 步统一延迟窗口下仍 63.8-78.0%，对比方法最高 6.4%；ARLI 说明推理延迟会改变有效环境动力学、破坏马尔可夫假设，标准 RL 在延迟下完全失效，需要带中间信息的异步 RL；ST-Merge 训练无关地合并时空视觉 token（π0.5 在 1024² 下提速 8.3 倍）；Habilis-β 提出生产力-可靠性平面（Tasks per Hour × Mean Time Between Intervention），在一小时连续运行协议下评测端侧 VLA。

## 2. 各篇要点

**PhyAI**：物理 AI 策略在生命周期各阶段（评测、云端 RL rollout、边缘 GPU 服务、板载部署）共享同一 checkpoint 与动作语义，却依赖不同的推理程序。方法：单一运行时，架构特定的条件化/求解器/缓存/输出逻辑放在模型适配器里，共享图执行、kernel、内存管理与并行服务；同一代码库在多种硬件上跑 VLA 与 WAM。control-time Roofline 是它给"控制受限于什么"的诊断工具。

**EcoVLA**：板载推理受算力与能量预算限制，难以同时满足实时与能效；卸载到边缘服务器又受系统条件波动影响带来不可预测延迟。方法：面向 VLA 的设备-边缘协同推理的系统性设计与能效优化。

**CloudEdgeVLA**：在移动机器人上部署十亿参数 VLA 有系统性冲突——语义推理受益于云端 GPU，闭环控制必须本地响应网络延迟与抖动。方法：云端 VLA 把延迟的观测编码为慢变的任务特征，轻量边缘头把它与最新本地视觉结合；"涌现表征"意味着不需要显式的调度或延迟线索。

**ARLI**：大模型的推理延迟导致停顿或抖动，改变有效环境动力学；若不正确处理，标准 RL 算法完全失败。方法：延迟感知的异步 RL，用中间信息增广状态。它是 T9 与 T14 的交点——部署时 RL 必须知道自己的延迟。

**ST-Merge**：视频与高分辩率图像产生海量视觉 token；在视觉编码阶段用 3D 时空坐标做多队列并行匹配与加权聚合融合冗余 token，即插即用、无需训练。

**Habilis-β**：单次成功率在精心复位下的评测不反映实用能力；PRP 平面用 TPH 与 MTBI 在连续运行协议下同时要求高速执行与持续鲁棒。

## 3. 口径与局限

- 提速倍数（1.40-4.65×、8.3×）、能效（+236%）、延迟窗口下的成功率（63.8-78.0%）、TPH/MTBI 是四种不同类型的指标，与任务成功率不可并排。
- CloudEdgeVLA 的 40 步延迟是仿真中的统一延迟窗口，真实网络的抖动分布未必匹配。
- Habilis-β 的一小时连续运行是本仓库少见的"长期运行"口径，但任务与平台单一。

## 4. 关系定位与延伸批判

这组工作是报告 I5（harness 变成实时系统问题）的实证基础，与 Harness Engineering for Physical AI（notes/23）的 Projection/Isolation/Transfer 提案一一对应：ARLI 与 CloudEdgeVLA 处理 Isolation 失效后的补救，PhyAI 的 Roofline 是诊断 Isolation 是否被违反的工具。Habilis-β 的 TPH × MTBI 是本仓库推荐的"Experience Scaling 度量"候选之一（报告开放问题第 8 条）：它衡量的正是"机器人能否长期工作"。未走之路：没有一篇把双系统架构（notes/26）与云边分工放在同一实验里——慢系统在云、快系统在端是最自然的映射，CloudEdgeVLA 最接近，但它的"边缘头"不是一个完整的 System 1。
