# 07 · 自进化续作合评：Zetta、SHAPER、PRACTICE、SkillGLoW、HiSME、MEMENTO

> 覆盖：Zetta ζ（arXiv 2608.16590，2026-08）· SHAPER（2608.11350，2026-08）· PRACTICE（2608.30760，2026-08）· SkillGLoW（2609.02217，2026-09）· HiSME（2605.28390，2026-05，清华 + 华为）· MEMENTO（2607.22832，2026-07）
> 所属主线：T7、T8、T15、T24 · 材料来源：报告第 3.4 节；具身纪元文章点名 HiSME 与 Zetta

## 1. 一句话定位

讲稿的时间线止于 2026 年 6 月；7-9 月的六篇工作把"优化外部产物 $z$"推向三个方向：**运行时**（Zetta 在线演化代码形式的 critic 与恢复技能；SHAPER 演化技能与 context-code harness）、**技能库的维护**（PRACTICE 训练一个技能学习器做增/改/合/删；SkillGLoW 以"过程族"为复用单元；HiSME 演化"怎样演化技能"的元技能）、**搜索算法**（MEMENTO 的记忆引导单精英模因演化）。共同点是基座策略全部冻结。

## 2. 各篇要点

**Zetta ζ**（闭环具身 harness）。诊断：现有 harness 基本是开环的——rollout 中按固定技能执行，只在 episode 结束后反思，而物理交互需要以超过大 agentic 模型频率的速度跟踪机器人-环境状态。方法：三个时间尺度分离的循环——动作频率的治理（运行时 critic）、rollout 级的 critic-恢复提议、验证门控的技能更新；配 Z-Infra 把 agent 逻辑与异构执行资源解耦。结果：LIBERO-Pro 90.8%、RoboCasa 93.6%（"在当前 rollout 预算下"），推理加速 11.1 倍。口径：仿真基准；90.8% 与 Harness VLA 的 +38.6pp、RHO 的 45.0% 分别对应不同基座与协议，不能并排。

**SHAPER**（技能-harness 演化）。面向"固定接口"场景——很多 train-free 代码方法依赖可编程机器人 API，而这类 API 未必存在；SHAPER 让同一个冻结模型既当规划器又当优化器，通过目标环境 rollout 演化可复用技能与 context-code harness。它把 Lil'Log 的"optimizer code"一级搬进了具身场景。

**PRACTICE**（从经验到专长）。诊断：现有基于经验的方法靠人工设计的 prompt 流程抽取与更新技能，面对新而多样的经验时僵化。方法：训练一个技能学习器，读历史技能与新轨迹，输出结构化批量编辑（增、改、合、删），再分层整合成一致的技能库；执行器冻结；两阶段课程训练学习器。意义：技能库维护本身成为被训练的对象。

**SkillGLoW**（过程族技能整合）。诊断：文本技能要么是一份全局文档（塌缩为泛泛的纪律），要么是按任务堆积的条目池（膨胀且绑定在写它的实例上）；两者在"每个任务都需要不同解法"的长程负载上以相反方式失效。方法：把任务写出的局部技能聚合成过程族，压缩成去实例化的全局先验，实例细节按任务重新生成而不存储；commit gate 只在真实执行证明不劣化时接纳先验。结果：四个基准（数学推理、终端自动化、软件修复、具身控制）× 三个模型，先验带来 +17.2 个百分点（摘要截断处）；报告第 3.4 节引用的 ALFWorld 73.9→83.9% 来自未修改先验库的零样本迁移。

**HiSME**（分层技能元进化）。诊断：测试时技能演化要么是硬编码策略，要么依赖昂贵的参数更新。方法：从执行轨迹学"元技能"——怎样生成与修改技能——同时优化技能与技能演化策略；权重不变。结果（具身纪元文章转述）：MineDojo 任务成功率 0.700→0.856。它是 Lil'Log 优化阶梯里"optimizer code"一级的另一个实例。

**MEMENTO**（记忆引导的模因演化）。先演化一个 rollout 评估器（把 rollout 映射为标量适应度与结构化反馈指标），再用适应度选精英、用反馈指标条件化记忆引导的爬山与宏突变。它提醒我们：在代码策略的演化搜索里，评估器本身也是被演化的对象——这与 AHE"verifier 只读"的原则形成张力。

## 3. 局限（共同）

1. 六篇几乎全部在仿真（LIBERO-Pro、RoboCasa、MineDojo、ALFWorld）验证；只有 Zetta 强调运行时频率，但真机数据摘要未说明。
2. "冻结基座 + 演化外围"的收益都以基座能力为前提；跨基座的收益是否单调（Harness Updating ≠ Harness Benefit 的问题）没有系统报告。
3. 技能库维护（PRACTICE、SkillGLoW）的验证仍是任务成功率；技能之间的一致性、冲突与可审计性缺少专门指标。

## 4. 关系定位与延伸批判

这六篇加上 ASPIRE（notes/04）与 SkillOpt（notes/05）形成 T7 的完整谱系：$z$ 从技能文档（SkillOpt）→ 技能库（ASPIRE、PRACTICE、SkillGLoW）→ 元技能（HiSME）→ 运行时 critic 与恢复技能（Zetta）→ 整套 harness（SHAPER），$A$ 被允许改的东西越来越靠近执行时刻。Zetta 的"动作频率治理"把 harness 拉进了实时系统的领域，与 Harness Engineering for Physical AI 的 Projection/Isolation/Transfer（notes/23）是同一问题的两种表述。最值得追问的是**验证门**：SkillGLoW 的 commit gate、Zetta 的验证门控更新、PRACTICE 的分层整合都以"真实执行不劣化"为准，但这些执行都在仿真里；当验证要付出真机成本时，谁来承担 held-out rollout？这是 T7 与 T11（数字孪生作为验证器，notes/30）必须合流的原因。
