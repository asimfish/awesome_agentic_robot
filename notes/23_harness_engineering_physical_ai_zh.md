# 23 · Harness Engineering for Physical AI 深度解读：机器人中间件就是 harness 层

> **Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer**
> arXiv 2606.09416（2026-06-08）· ACM/IFIP Middleware 2026（Big Ideas）· Sanghoon Lee, Jiyeong Chae, Kyung-Joon Park
> 所属主线：T14、T15、T16 · 材料来源：小红书长文 03 节（Real-time-aware Harness）；检索地图 T14/T15 代表工作；报告第 2.3 节、第 7 章 I5

## 1. 一句话定位

这篇短文提出一个命名：学习策略、规划器与 VLA 已经作为因果参与者进入部署机器人的控制路径，但把它们与时序、调度、网络整合起来的那一层还没有名字；语言 agent 社区叫它 harness——机器人的中间件就是这个 harness。物理 AI 的 harness 与软件 harness 的区别在于**介入的位置**：软件 harness 在工具调用边界介入，物理 harness 必须同时在控制、计算、通信三处介入，因为学习策略的输出同时改变轨迹、日程与带宽。它提出三个缺失的强制功能——Projection、Isolation、Transfer——并建议做成 ROS 2 Harness Profile。

## 2. 要解决的问题

VLA 与学习策略进入机器人后，一次推理花 2 秒不再只是"慢"：它改变了控制回路的时序，可能让下游控制器读到过期命令，可能挤占通信带宽，可能让安全反射来不及介入。现有中间件（ROS 2 等）把这些模型当普通节点处理，没有为"输出不可预测、延迟不可预测、失败不可预测"的参与者设计强制机制。

## 3. 方法（提案）

- **Projection**：在输出处约束动作——把学习策略的输出投影到安全/可行集合内，而不是相信它。
- **Isolation**：限定模型推理的执行与传输时隙——推理不能无限占用计算与网络，deadline 必须被强制。
- **Transfer**：检查失败时回退到经过验证的基线——策略、规划器不可用或输出不可接受时，控制权移交给已验证的备份。
- 落地建议：把三者做成 ROS 2 Harness Profile，使它们成为声明式配置而非每个项目重写的代码。

## 4. 实验结果与口径

- 这是立场/大想法论文（Big Ideas track），没有实验数字。
- 与之相关的系统证据来自同期工作：PhyAI 的 control-time Roofline（区分推理受限与环境受限的控制）、CloudEdgeVLA 在 40 步延迟下 63.8-78.0% vs 对比方法最高 6.4%、EcoVLA 在 20 Hz 约束下能效 +236%、ARLI 证明延迟破坏马尔可夫假设（notes/27）。

## 5. 局限

1. 三个功能的形式化定义（投影到什么集合、时隙如何分配、回退的触发条件）留给后续工作。
2. "中间件就是 harness"的命名如果被接受，会把 Lil'Log 意义上的 harness（工具、记忆、评估、工作流）与实时系统意义上的 harness（调度、投影、回退）合在一个词下——两者的设计目标不同，可能需要分层命名。
3. 没有讨论多机器人（通信介入的自然延伸）。

## 6. 关系定位

这篇论文是报告 I5（harness 从软件名词变成实时系统问题）的直接来源，也是小红书长文"Real-time-aware Harness"（知道模型最大延迟、技能 deadline、断网 fallback、哪些动作必须本地完成）的学术版本。Zetta 的"动作频率治理"（notes/07）是 Isolation 的一个实例；Runtime Governance 的回滚与人工接管（notes/25）是 Transfer 的治理层版本；PonderPounce 的认知"年龄"字段（notes/11）是 Isolation 在接口上的一个微观体现。与 Thea（notes/22）合起来构成机器人 harness 与软件 harness 的三点差异。

## 7. 延伸批判

这篇论文最有力的地方是它把 harness 问题交还给了一个成熟的工程社区（中间件、实时系统），而不是留在 prompt 工程里。最值得做的后续是把 Projection / Isolation / Transfer 写成 ROS 2 profile 并与 MHS（notes/36）的设备发现协议对接，让"延迟预算、deadline、fallback"成为机器人描述文件的一部分——报告开放问题第 4 条。一个未被讨论的张力：Projection（约束输出）与 Harness VLA（学 VLA 何时可靠）是同一问题的两种解法，前者在毫秒级硬约束，后者在秒级软决策；两者的分层关系没有人正式写出来。
