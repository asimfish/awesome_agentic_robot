# 趋势与洞察：Agent × Robot 从 Harness 到自进化物理智能体（2026 年 9 月）

> 本文是仓库的执行摘要：一页结论、领域时间线、六大趋势、十条洞察、可证伪预测。所有数字的口径见 `insights/12_numbers_ledger_zh.md`，每条判断对应的深度解读见 `notes/`（编号引用为 notes/NN）。**不同工作的成功率禁止直接比大小。**

## 0. 一页结论

1. **优化对象在上移**：2022 年 LLM 写一段策略代码（notes/01）；2026 年 coding agent 优化技能文档（notes/05）、策略仓库（notes/03）、技能库（notes/04）、训练配方（notes/06）、运行时 critic（notes/07）、整套 harness。讲稿公式 $z_{t+1} = A(z_t, \tau_t, r_t, \log_t)$ 是这条线的坐标系。
2. **"冻结 VLA + 外围学习"是默认范式，但有天花板**：Harness VLA、BATON、AGM、HyMeS、Zetta 不改权重（notes/20、14、12、13、07）；LWD 与 Q-Planning 证明真实反馈终要写回某个可训练对象（notes/28、29）。
3. **验证器是新瓶颈也是新 scaling 轴**：AGM 的证据门控、Thea 的 exit codes、PRIMO R1 的过程批评者、VERITAS 的推理时验证、LLM-as-a-Verifier 的连续评分（notes/12、22、17、18、19）。
4. **Harness 变成实时系统问题**：控制/计算/通信三处介入、Projection/Isolation/Transfer（notes/23）；端侧系统工作给出实证（notes/27）。
5. **群体是经验规模化的出路，收益亚线性**：LWD 16 台 → 95%（notes/28）；ENPIRE 8 倍机器人 → 2-3 倍加速，多的是假设吞吐量（notes/06）。
6. **Robot RSI 是串起一切的框架**：改进环节 × 人的参与程度两条轴线（notes/41），把机器人侧与软件侧放进同一张表。
7. **治理与安全被观点文章低估、被论文高估**：Runtime Governance 96.2% 拦截、EmbodiedGovBench 七维（notes/25）；证据多在仿真（notes/39）。
8. **长程问题被重述为技能交接问题**：$T^K \to T \cdot K$，进入条件缺失（notes/14）。
9. **记忆分权重内/权重外两路**：RoboMME"任务依赖"、RoboMME-Interference"检索可恢复"给出选择规则（notes/10、15）。
10. **Sim 是 sandbox 不是训练场**：建 twin 的成本在下降，twin 的可信度仍取决于接触建模（notes/30、33）。

一句话：下一阶段不是 Model Scaling，也不只是 Harness Scaling，而是 **System Scaling + Experience Scaling**——先训练出足够好的机器人让它开始工作，再让工作本身继续训练机器人。

## 1. 领域快照：通往 2026 年 6-8 月的时间线

- **2022-2023 · 范式起点**：Code as Policies（2022-09）把策略变成 LLM 写的程序（notes/01）；RoCo（2023-07）让机器人用 LLM 对话协商（notes/37）；Eureka（2023-10）让 LLM 写奖励函数（notes/08）；软件侧 ReAct、Reflexion、Toolformer、Generative Agents 与 Lil'Log 2023 文确立 Agent = Planning + Memory + Tool use（notes/40）。
- **2024 · 技能与仿真参数的自动化**：Agentic Skill Discovery 让 LLM 从零长出技能库（notes/09）；DrEureka 让 LLM 写域随机化范围并迁移真机（notes/08）；MALMM 三 agent 零样本操作（notes/37）。
- **2025 · 闭环骨架标准化**：Agentic Robot、ManiAgent、PhysiAgent 确立感知 → 分解 → 执行 → 验证 → 重规划（notes/35、16）；双系统 VLA 三条路线（Fast-in-Slow、OneTwoVLA、RationalVLA，notes/26）；RoboOS/RoboOS-NeXT 的共享记忆（notes/37）；Arcadia 的四阶段生命周期（notes/38）；软件侧 DGM、AlphaEvolve、ShinkaEvolve、ACE 打通 harness 演化（notes/42）。
- **2026 年 1-5 月 · 记忆、接口、治理登场**：AgenticLab 的规划语言接口（notes/34）；RoboMME 基准（notes/10）；StreamVLA、LaST0 解决"何时切换"（notes/26）；TwinRL（notes/30）；RoboClaw 的自复位（notes/31）；PRIMO R1（notes/17）；CaP-X 平台（notes/02）；ROSClaw 的模型无关执行层（notes/36）；Runtime Governance 与 EmbodiedGovBench（notes/25）；LWD 的 16 台机器人（notes/28）；SkillOpt 的训练纪律（notes/05）。
- **2026 年 6-8 月 · 密度最高的季度**：Harness 一词成为中心——RHO、Harness VLA、Harness Engineering for Physical AI、PhyAgentOS、Thea、Guava、HARBOR、Zetta、SHAPER、RoboHarness（notes/03、20-24、07）；ENPIRE 与 ASPIRE 把 coding agent 放进真机学习循环与技能库（notes/06、04）；记忆论文集中出现——PonderPounce、AGM、HyMeS、BATON、NativeMEM、LaMem、Remember Smarter（notes/11-15）；验证器成为独立主题——VERITAS、LLM-as-a-Verifier、立场论文（notes/18、19）；VLA+RL 的信用分配（Temporal GRPO、TEMPO、WCM，notes/32）；端侧系统（PhyAI、CloudEdgeVLA、ARLI，notes/27）；Anthropic MHS（2026-08-27，notes/36）。
- **2026 年 9 月 · 叙事汇合**：具身纪元文章把这一切命名为 Robot RSI（notes/41）。

## 2. 六大趋势

### 趋势一：优化对象沿 Lil'Log 阶梯逐级上移，机器人侧已走完全程
prompt → context（SkillOpt）→ workflow（ASPIRE、HARBOR）→ harness code（RHO、SHAPER、Zetta）→ optimizer code（HiSME、HarnessOpt）。每一级都有 2026 年的机器人侧实例（notes/40、42）。含义：一篇新方法的贡献越来越取决于它把哪一级的产物变成可搜索、可验证、可复用的对象。

### 趋势二：冻结基座成为默认，学习发生在外围
Harness VLA、BATON、AGM、HyMeS、Zetta、SHAPER、RoboHarness、AtomBridge、RL²-VLA、VERITAS 全部不改 VLA 权重。原因是权重更新贵、慢、验证难，且闭源前沿模型无权重可改。边界由 BATON（VLA 原语没有进入条件）与小红书长文的 USB 例子划出：接触相关的连续关系外围学不到（notes/14、20）。

### 趋势三：验证器从隐含假设变成显式对象，并开始分层
2026 年前，"成没成"由脚本或人判定；2026 年出现了四类显式验证器——高频几何门控（AGM）、过程级视频批评者（PRIMO R1）、推理时动作验证器（VERITAS）、连续评分与准入判断（LLM-as-a-Verifier、Agentic Harnesses）——加上部署前的形式验证（VASO）与数字孪生预演（PerceptTwin）。立场论文提醒：成功率本身无法证明物理推理（notes/19）。

### 趋势四：Harness 从 prompt 工程变成中间件与实时系统
Harness Engineering for Physical AI 命名了这一层并提出 Projection/Isolation/Transfer；PhyAI 的 control-time Roofline、CloudEdgeVLA 的 40 步延迟、EcoVLA 的 20 Hz、ARLI 的延迟破坏马尔可夫假设、UniFS/Latent Bridge 的频率分层是同一问题的实证（notes/23、27、26）。

### 趋势五：评测口径开始转向"长期运行"
Habilis-β 的 Tasks per Hour × Mean Time Between Intervention、ENPIRE 的 MRU/MTU、AgenticRobotics 的假阳性晋升率、EmbodiedGovBench 的七维治理指标，都在替代"精心复位下的单次成功率"（notes/27、06、08、25）。这是"让机器人长期工作"的必要度量。

### 趋势六：接口标准化与安全同步升温，但尚未合流
MHS（2026-08-27）、ROSClaw 的模型无关执行层、MCP 机器人 server、ROS 2 Harness Profile 提案让"任何模型接任何机器人"成为可能；AgentRob 的劫持、多机器人通信攻击 97.8%、Same Weights Different Robot 的元数据脆弱性说明开放接口的攻击面同步扩大（notes/36、39）。

## 3. 十条核心洞察

I1 **优化对象上移**（趋势一的判断版）：贡献 = 把哪一级产物变成可搜索、可验证、可复用的对象。

I2 **冻结 VLA + 外围学习有天花板**：HyMeS 的"技能在权重里、记忆在代码里"是可操作的分工假设；Q-Planning 的"技能在大权重里、价值在小权重里"是第三条路（notes/13、29）。

I3 **验证器是瓶颈也是 scaling 轴**：一个更好的验证器比一个更好的规划器更稀缺，也更容易成为独立贡献；Goodhart 风险要求评估器在可编辑面之外（notes/19、42）。

I4 **记忆两条路各有适用区**：精确时序、计数、低延迟用权重内（NativeMEM 32.4 → 84.0%）；跨会话、抗干扰、可解释、可编辑用结构化外部记忆 + 检索（RoboMME-Interference）（notes/10、15）。

I5 **Harness 是实时系统问题**："harness 像 OS"在机器人侧是字面意义（notes/23、21）。

I6 **Sim 是 sandbox**：TwinRL、RoboSnap、Agentic Real2Sim、PerceptTwin、SafeDojo 让新技能先在物理仿真里跑；缺的是串起来的 harness（notes/30）。

I7 **治理与安全成为一等公民**：Runtime Governance、EmbodiedGovBench、ICAN-Deploy、EMBGuard、SENTINEL、Same Weights（notes/25、39）；两篇观点文章都没写它。

I8 **群体收益亚线性**：价值在假设与场景的多样性，不在同一策略的 rollout 数；"多样性塌缩"以多个 agent 试同一想法出现（notes/06、28）。

I9 **Coding agent 成为 roboticist**：Eureka → DrEureka → HARBOR → ENPIRE → AgenticRobotics；物理世界加三个约束——读状态难、判结果难、有时间（notes/08、22、23）。

I10 **风险与反例**：harness updating ≠ harness benefit；验证器进了可编辑面（Zetta、MEMENTO、Motus2）；对话降低多机器人任务成功；共享经验会共享污染（notes/42、07、33、37）。

## 4. 可证伪的预测（12-24 个月）

写成可以被证明错的形式；到期后应回来逐条核对。

- **P1（验证器分层）**：到 2027 年中，至少一篇机器人论文会同时报告高频门控验证器与低频 LLM/视频验证器的组合，并给出两层各自的假阳性/假阴性率。若届时验证器仍只作为单一模块出现，P1 错。
- **P2（进入条件）**：到 2027 年中，至少一个开源技能库（ASPIRE、RATs、Harness VLA 类）会把"进入条件"作为技能的显式字段（几何分布或谓词），而不是隐含在 MOVE_TO 预定位里。
- **P3（harness 标准）**：到 2027 年底，会出现一个把 Projection/Isolation/Transfer 之一做成 ROS 2 profile 或 MHS 扩展的公开实现；若 MHS 与 ROS 2 Harness Profile 仍是两条互不引用的线，P3 半错。
- **P4（群体加速比）**：ENPIRE 式多 agent 真机研究若加入假设去重（新颖性拒绝采样或过程族去重），8 机器人加速比会从 2-3 倍提高到 ≥4 倍；若有人做了去重仍停在 3 倍以下，P4 错——瓶颈不在重复而在等待。
- **P5（只读评估器）**：到 2027 年中，至少一篇自进化机器人论文会明确把评估器/验证器设为不可演化并报告"评估器只读 vs 可演化"的对照；若所有自进化工作继续演化自己的 critic 而无对照，P5 错。
- **P6（Experience Scaling 度量）**：TPH × MTBI 或 MRU/MTU 类连续运行指标会出现在至少三篇非原作者的论文中，成为通用口径；否则"Experience Scaling"仍是口号。
- **P7（治理进真机）**：EmbodiedGovBench 式的七维评测会在 ≥8 台机器人的真机集群上被报告一次（LWD 或 ENPIRE 规模）；若治理评测继续停留在仿真，P7 错。
- **P8（frontier LLM 的角色）**：具身纪元文章的判断——前沿 LLM 先成为认知中枢而非末端控制器——在 2027 年中仍成立：不会有主流工作用 GPT-6 级模型以 ≥10 Hz 直接输出连续控制并在接触密集任务上超过专用 VLA。若出现，P8 错，本仓库 I2 需要重写。

## 5. 开放问题清单

见 `insights/11_open_problems_zh.md`：19 个问题，按 Part A-G 排列，每条配缺口、为什么重要、最小可行实验与相关解读。只做一件事就做第 1 条（分层验证器）。
