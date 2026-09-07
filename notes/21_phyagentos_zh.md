# 21 · PhyAgentOS 深度解读：把 Harness 做成操作系统

> **PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive and Physical Execution**
> arXiv 2607.16636（2026-07-18）· Yang Liu, Weixing Chen, Xinshuai Song et al.（共 11 位作者）
> 所属主线：T7、T15、T16、T17、T23 · 材料来源：检索地图 T7/T15/T16/T23 代表工作；报告第 4 章、第 5.2 节

## 1. 一句话定位

PhyAgentOS 把调度、验证、记忆、评测、安全做成系统级服务：以会话（session）而不是动作作为调度、兼容性预检、监督执行、证据收集与验收的最小单元；用 State-as-a-File 把跨层状态物化为 Markdown + YAML 以解耦认知与物理执行；SessionVerifier 区分"执行终止"与"语义完成"；验证过的结果经 epistemic memory 沉淀为可复用知识与纠正性教训；在 19+ 个仿真与真实本体上验证。它是 Lil'Log "harness 像 OS"这一类比在机器人侧的字面实现。

## 2. 要解决的问题

VLA、世界模型、agentic 规划器各自推进物理智能，但它们的组合缺少共同的执行抽象、共享状态、语义验证与跨异构本体的持久经验。每个项目重写一遍"调用—验证—记忆—恢复"的胶水，且这些胶水无法跨本体复用、无法审计。

## 3. 方法

- **Session-Centered Runtime**：会话是最小调度单元，包含兼容性预检（本体、传感器、技能是否匹配）、监督执行、证据收集、验收。
- **认知-物理边界 + State-as-a-File**：认知层与执行层通过文件化的状态（Markdown + YAML）通信，任何一层都可以读、写、审计、回滚——这就是 Lil'Log 的"文件系统即持久记忆"。
- **SessionVerifier**：把"程序跑完了"与"任务在语义上完成了"分开判断。
- **Epistemic memory**：验证过的结果沉淀为可复用知识与纠正性教训，供后续会话检索。
- **自进化**：以上服务使系统能在会话之间积累与修正，形成"自进化操作系统"。

## 4. 实验结果与口径

- 摘要给出的是覆盖范围（19+ 仿真与真实本体）与系统能力，而非单一成功率数字；具体任务级结果见正文。
- 口径：系统论文，评测重点是跨本体的可复用性与治理能力，与单任务成功率论文不同类。

## 5. 局限

1. "OS"的抽象越通用，每个本体上的性能调优空间越小；PhyAgentOS 在单一基准上与专用系统（如 Harness VLA）的对比摘要未给出。
2. State-as-a-File 让状态可审计，但文件读写的延迟决定它只适用于会话级/子任务级，不适用于动作频率的治理——Zetta（notes/07）与 Harness Engineering for Physical AI（notes/23）处理的是那一层。
3. SessionVerifier 的"语义完成"判断依赖什么模型、准确率多少，摘要未说明。

## 6. 关系定位

PhyAgentOS 同时落在五条主线上，是本仓库连接度最高的系统工作。对 T16 它是 Runtime 主线的"内置治理"代表（与 Runtime Governance 的"外置治理"形成对照，notes/25）；对 T23 它的 SessionVerifier 与 Thea 的 Evaluation as Exit Codes（notes/22）是同一问题的两种接口；对 T7 它把自进化放在会话粒度；对 Lil'Log 的三模式，它同时实现了工作流自动化与文件系统记忆。

## 7. 延伸批判

PhyAgentOS 最大的贡献是命名与分层——它让"验证、记忆、调度、安全"从每个项目的私有代码变成可讨论的服务接口。但 OS 的价值来自生态：如果没有第二个团队在 PhyAgentOS 上跑自己的策略，它就只是一个更大的项目脚手架。因此对它最公平的检验不是任务成功率，而是 EmbodiedGovBench 式的七维治理评测（越权、漂移、恢复、可移植、升级安全、人工接管、审计），以及"一个新本体接入需要多少行配置"这类工程指标——两者论文都没有给。另一个未走之路：State-as-a-File 与 ENPIRE 的 Markdown 研究总结（notes/06）是同一机制，两者结合可以让"研究经验"也成为 OS 的一等状态。
