# 39 · 安全合评：EMBGuard、SENTINEL、VASO、Same Weights Different Robot、RationalVLA、通信攻击与 AgentRob

> 覆盖：EMBGuard（arXiv 2605.30924，ICML 2026）· SENTINEL（2510.12985，2025-10）· VASO（见 notes/09）· Same Weights, Different Robot（2606.03724，2026-06）· RationalVLA（见 notes/26）· Communication Attacks（见 notes/37）· AgentRob（见 notes/36）· Runtime Governance / EmbodiedGovBench（见 notes/25）· SafeDojo / ContactGuard（见 notes/33）
> 所属主线：T17 · 材料来源：检索地图 T17 代表工作；报告第 4 章 T17、第 7 章 I7

## 1. 一句话定位

T17 在 2026 年从"过滤不安全计划"扩展为四类工作。**护栏模型**：EMBGuard 是第一个 MLLM 安全护栏，把物理风险推理与 agent 策略解耦——对（视觉观测，动作）对识别危险并推理动作条件的风险，2B/4B 模型接近 GPT-5.1 / Gemini-2.5-Pro 且假阳性更低。**形式化**：SENTINEL 在语义解释、计划生成、物理执行三层用时序逻辑做统一形式评测，替代启发式规则与主观的基础模型判断；VASO 把形式验证接进技能自进化。**世界模型**：SafeDojo 在想象中学安全动作，ContactGuard 接触前中止。**部署视角**：Same Weights, Different Robot 指出 VLA 常被当作 checkpoint 定义的对象，但同一归一化输出经动作反归一化与控制器约定后会变成不同的物理动作——安全审查认证了 checkpoint，却漏掉到达控制器的可执行策略；替换一个看似合理的元数据键就能让 LIBERO-Goal 从 28/28 降到 2/28。加上 RationalVLA 的缺陷指令拒绝、多机器人通信攻击（97.8%）与 AgentRob 的劫持风险，安全的攻击面已经覆盖指令、通信、模型、元数据、接触五个层面。

## 2. 各篇要点

**EMBGuard**：MLLM 具身 agent 在真实环境中遇到物理危险，现有方法缺少显式的危险识别与动作条件风险推理机制，导致漏判或过度判定。方法：解耦的安全护栏，评估（观测，动作）对；2B/4B 模型，性能接近前沿闭源模型且假阳性更低（报告转述）。

**SENTINEL**：第一个在语义解释、计划生成、物理执行三层做统一形式安全评测的框架；把实用安全需求接地到形式时序逻辑语义（状态不变量、时序依赖等），而不是启发式规则或主观 FM 判断。

**Same Weights, Different Robot**：动作反归一化元数据是可执行策略的一部分；只审 checkpoint 会漏掉真实策略。28/28 → 2/28 是一个元数据键替换的后果。

**RationalVLA**：RAMA 基准的六维缺陷指令（模糊、无关、不可行等），理性层判断该不该执行——"拒绝"作为一等输出。

## 3. 口径与局限

- EMBGuard 的"接近前沿模型、假阳性更低"是护栏自身的判别指标；SENTINEL 是评测框架；两者都不直接给任务成功率。
- Same Weights 的 28/28 → 2/28 是单一元数据替换的极端案例，说明的是脆弱性存在，不是常见频率。
- 绝大多数安全评测在仿真或受控场景；真机上的持续运行安全数据（Habilis-β 式的 MTBI，notes/27）几乎没有。

## 4. 关系定位与延伸批判

报告 I7 的判断：安全与治理是 Agent × Robot 里被材料低估、被论文高估的方向——低估是因为观点文章不写它，高估是因为它目前主要在仿真里验证。把 T17 与 T16（notes/25）、T18（notes/36）放在一起，可以看到安全正在从"过滤"扩展到"运行时持续检测 + 恢复 + 可审计 + 升级安全"，并触及动作空间语义这类以前没人看的层面。三个未走之路：（1）自进化系统的新技能（ASPIRE、Zetta）如何通过 EMBGuard/SENTINEL 式的准入——目前没有任何自进化工作接入护栏；（2）Same Weights 的教训应当扩展到 harness 层：harness 配置（延迟预算、fallback）同样是"可执行策略的一部分"，同样需要被认证；（3）通信攻击与 AgentRob 提示接口标准化（MHS）必须附带权限模型，而 MHS 预览没有公开它。
