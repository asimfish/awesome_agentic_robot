# 36 · 接口层合评：两篇 ROSClaw、MHS、OpenClaw 生态与 MCP

> 覆盖：ROSClaw: An OpenClaw ROS 2 Framework（arXiv 2603.26997，2026-03）· ROSClaw: Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration（2604.04664，2026-04）· Anthropic Model Hardware Standard（研究预览，2026-08-27）· OpenClawPi（松灵机器人技能库）· OpenGo（2604.01708）· AgentRob（2602.13591）· ROSBag MCP Server（2511.03497）· Contract-Grounded BT Synthesis（2607.12220）· ChemBot（2604.15671）
> 所属主线：T3、T18、T17、T20 · 材料来源：检索地图 T3/T18 代表工作；报告第 4 章 T3/T18

## 1. 一句话定位

接口层回答"任何基础模型怎么接到任何机器人"。两篇同名的 ROSClaw 目标不同：Cardenas 等把 OpenClaw agent runtime 接到 ROS 2，做成**模型无关的执行层**——能力发现与 affordance 注入、观测归一化、安全包络内的预执行验证、审计日志；换模型或换平台只是改配置，并顺带成为一件测量仪器：同一基底上不同前沿模型的越权动作提议率相差 3.4-4.8 倍，且执行层设计比 prompt 措辞更影响任务完成与安全行为。Zhao 等的 ROSClaw 面向异构多机器人，用 e-URDF 物理约束构建 sim-real 拓扑映射，把采集、训练与执行放进统一的 VLM 控制器。Anthropic 的 MHS（2026-08-27）是标志性事件：一套让 agent 发现、操作、排障任意物理设备的共享规范，被媒体称为"硬件版 MCP"，可通过 MCP、CLI 或代码调用。MCP 正在成为机器人侧的通用接口：ROSBag MCP Server、ChemBot 的 MCP 子 agent 编排、Contract-Grounded BT Synthesis 让 coding agent 先向机器人侧 MCP server 拉取技能契约再合成行为树、AgentRob 通过 MCP 把论坛 agent 连到 Unitree Go2/G1（也展示了被劫持的风险）、OpenGo 是 OpenClaw 驱动的机器狗（技能库 + 调度器 + 反馈自学习）。

## 2. 各篇要点

**ROSClaw（OpenClaw ROS 2）**：今天把基础模型接到机器人需要把感知、执行与安全耦合到单一模型和平台的定制集成。方法：模型无关执行层——动态能力发现 + 标准化 affordance 注入、观测归一化、可配置安全包络内的预执行动作验证、审计日志。发现：越权动作提议率跨模型差 3.4-4.8 倍；执行层设计 > prompt 措辞。

**ROSClaw（异构）**：LLM + 具身 agent 提升了高层推理，但语义理解与物理执行之间仍有缝；VLA/VLN 在长程、时序结构任务上吃力。方法：分层语义-物理框架，e-URDF 物理约束、sim-real 拓扑映射、统一 VLM 控制器串起采集/训练/执行。

**MHS**：让 agent 标准化地发现、操作与排障显微镜、液体处理器、相机、机械臂、激光系统等真实设备的共享规范；来源是 Anthropic 研究预览与媒体报道（非论文）。

**Contract-Grounded BT Synthesis**：从自然语言合成可部署行为树要求接地——每个生成的 BT 只引用机器人真能执行的技能；现有方法把接地责任推给 prompt 作者。方法：coding agent 先从机器人侧 MCP server 拉取技能契约（有哪些技能、参数如何、运行时对 BT 结构的约束），再合成 BT。

**AgentRob**：把在线论坛、LLM agent 与真机通过 MCP 桥接——agent 读帖、抽取自然语言命令并执行；论文同时是一份威胁模型：论坛介导的机器人可被劫持。

**ROSBag MCP Server / ChemBot / OpenGo / OpenClawPi**：MCP 分析 ROS bag、化学实验室 VLA agent 的 MCP 子 agent 编排与双层记忆、OpenClaw 机器狗的实时技能切换、松灵的 OpenClaw 技能库——生态层的实例。

## 3. 口径与局限

- ROSClaw 的"3.4-4.8 倍"是越权动作**提议**率的跨模型比值，不是任务成功率；越权由安全包络定义。
- MHS 是研究预览，没有论文与数字；能否成为事实标准取决于采用。
- MCP 相关工作多为系统描述与演示，少有统计评测。

## 4. 关系定位与延伸批判

报告第 4 章 T3 的判断：模型无关的执行层是 2026 年基础设施层最实用的进展，它把"安全包络"与"审计"做成了配置项。这与 Runtime Governance 的外置治理（notes/25）同向，与"Flexible but still Fragile"的发现（可靠性来自执行层，notes/35）互证。接口标准化决定 harness 层的可移植性：Harness Engineering for Physical AI 提议的 ROS 2 Harness Profile（notes/23）与 MHS 是两条正在逼近的标准线，是否融合值得跟踪（报告开放问题第 4 条）。最值得警惕的是 AgentRob 展示的攻击面：接口越标准、越开放，"任何模型接任何机器人"就意味着"任何被劫持的模型接任何机器人"——T18 与 T17 必须同步推进，而目前 MHS 的预览没有公开其权限模型。
