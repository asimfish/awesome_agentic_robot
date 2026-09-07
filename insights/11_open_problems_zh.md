# 研究机会清单：19 个待验证问题，每项配一个起步实验

> 本清单把 43 份解读里散落的"未走之路"与"延伸批判"统一归档，按合订本的 Part A-G 排列。入选标准：边际信息量高于"再发一个新机制"，且原则上可用现有开源资产（LIBERO-Pro、RoboCasa、RoboMME/RoboMemArena、CaP-Gym、Harness VLA/ASPIRE/RATs 的技能库、开源 VLA 如 π0.5/OpenVLA/GR00T）在中等预算内起步。"无人做过"一律限定为"本次检索未见"。每条给出：缺口 · 为什么重要 · 最小可行实验（MVE）· 相关解读。

---

## Part A · 主线：Coding Agent 与自进化

**1. 分层验证器及其误差账本（只做一件事就做这条）**
缺口：AGM 的高频几何门控（2.43M 参数）、PRIMO R1 的过程级视频批评者（RoboFail 67%）、LLM-as-a-Verifier 的连续评分（RoboRewardBench 87.4%）、VASO 的形式检查各自独立，没有人把它们组合并报告每层的假阳性/假阴性率。
为什么重要：验证器是自进化循环的上限（I3）；不知道每层错在哪里，就无法设计选择门的容错。
MVE：在 RoboMemArena 或 LIBERO-Pro 上固定一个冻结 VLA + agent 配方，分别用四种验证器（及其两两组合）充当"成没成"的判断，用脚本真值算每种验证器的混淆矩阵，再看自进化（例如 ASPIRE 式技能沉淀）在噪声验证下的收益曲线。
相关：notes/12、17、18、19、09。

**2. 把 SkillOpt 的训练纪律搬到机器人技能库**
缺口：SkillOpt 的四条纪律（有界编辑、held-out 严格提升门、拒绝编辑缓冲、epoch 慢更新）只在便宜验证器的软件任务上验证；ASPIRE、RATs、Harness VLA 的技能库更新没有 held-out 门。
为什么重要：没有选择门的技能库会积累"看起来聪明但没有改进"的技能（RSI 定义里的"变化不是改进"）。
MVE：用 RATs 或 ASPIRE 的开源技能库，把技能更新改为 SkillOpt 式流程，held-out 用 LIBERO-Pro 的一半任务；对照无门控更新，报告库规模 vs 零样本成功率曲线是否更陡。
相关：notes/05、04、09、07。

**3. 代码策略与 Harness VLA 的同基座组合**
缺口：RHO（代码策略仓库，LIBERO-PRO 45.0%）与 Harness VLA（VLA 调用规则，LIBERO-Pro +38.6pp）从未在同一原语与同一 VLA 上组合。
为什么重要：ENPIRE 的混合方案（代码管几何阶段、VLA 管接触阶段）说明两者互补，但只有一个数据点。
MVE：同一 π0.5 + 同一原语集，三个条件——纯 RHO、纯 Harness VLA、RHO 管交接 + Harness VLA 管调用——LIBERO-Pro 上并排。
相关：notes/03、20、06。

**4. 群体假设去重**
缺口：ENPIRE 8 倍机器人只有 2-3 倍加速，原因是 agent 重复探索相似假设；ShinkaEvolve 的新颖性拒绝采样与 SkillGLoW 的过程族去重是现成工具，没人接到多 agent 真机研究上。
为什么重要：决定 fleet autoresearch 的经济性；也是 Lil'Log"多样性塌缩"在机器人侧的形态。
MVE：先在 Gym-PushT（仿真）复现 ENPIRE 的 1/4/8 agent 曲线，再加假设去重（对提出的实验配置做嵌入去重），看加速比变化；预测 P4 由此检验。
相关：notes/06、42、07。

## Part B · 记忆、反思与验证

**5. 权重内 vs 权重外记忆的同基准对照**
缺口：NativeMEM（32.4 → 84.0%）、Remember Smarter（LIBERO-Plus 53.6 → 70.6%）与 AGM、HyMeS（RoboMemArena 41.3 → 60.1%）在不同基准、不同协议上报数。
为什么重要：I4 的选择规则（时序/计数用权重内，跨会话/可编辑用权重外）目前是推断，不是实验结论。
MVE：在 RoboMME 的四类记忆任务上，同一 π0.5 基座，加权重内记忆（NativeMEM 式）与加外部记忆（AGM 式）各一版，再在 RoboMME-Interference 的干扰会话下测衰减。
相关：notes/10、11、12、13、15。

**6. 技能的显式进入条件**
缺口：BATON 指出 VLA 原语只有退出条件；RoboHarness 的 Memory Bridge、Harness VLA 的 MOVE_TO 预定位、RoboClaw 的 EAP 逆向技能终态都是隐含的进入条件，没有一个技能库把它作为字段。
为什么重要：长程代价从 $T^K$ 变 $T \cdot K$ 的前提是子任务可独立探索，而独立性由进入条件保证。
MVE：对一个 VLA 原语（如"抓取"）在仿真里采样起始位姿分布并标注成败，拟合一个进入条件分类器；把它接进 BATON 式 agent 的交接决策，看长程任务成功率与探索 episode 数。
相关：notes/14、24、20、31、09。

**7. 反思类方法的"每次成功平均尝试数"口径**
缺口：PhysReflect-VLA（+5.4pp）、Agentic RAG-VLM（25 → 78.3%）、Zeva 式 CSR@K 都含重试，与更贵的 retry 无法区分。
为什么重要：不报告尝试数，就无法判断"反思"是否真的写进了持久对象。
MVE：对任一开源反思框架，同时报告单次成功率、CSR@K 与每次成功的平均尝试数，并加一个"随机重试同样预算"的对照。
相关：notes/16、07。

**8. 评估器进循环的后果**
缺口：Zetta 在线演化 critic、MEMENTO 先演化评估器、Motus2 把评估器做成共享权重的接口，都与 Lil'Log/AHE 的"评估器只读"冲突；无人对照。
为什么重要：这是 Robot RSI 的核心风险（Goodhart），也是预测 P5 的内容。
MVE：在 CaP-Gym 上跑一个自进化 agent，两条件——评估器冻结 vs 评估器随 agent 一起演化——用脚本真值测"评估器报告的成功"与"真实成功"的差距随轮数如何变化。
相关：notes/19、07、33、42。

## Part C · Harness、Runtime、双系统、端侧

**9. Projection / Isolation / Transfer 的 ROS 2 profile**
缺口：Harness Engineering for Physical AI 只提出了三个功能，没有实现；MHS 有设备发现协议但未公开权限模型。
为什么重要：让延迟预算、deadline、fallback 成为声明式配置，是 harness 层可移植的前提（预测 P3）。
MVE：在 ROS 2 上实现 Isolation（VLA 推理的时隙与 deadline）与 Transfer（超时回退到验证过的基线控制器），用 PhyAI 的 control-time Roofline 度量，在 CloudEdgeVLA 的延迟注入设置下测成功率。
相关：notes/23、27、36。

**10. 双系统的"何时切换"作为验证问题**
缺口：StreamVLA 的完成态门控与 RL²-VLA 的失败预测门控是两种切换判据，没有并排；切换误判的代价未量化。
为什么重要：切换判据本质上是一个在线验证器，其准确率决定慢系统介入的收益。
MVE：同一双系统骨干上实现两种门控，记录切换时刻与真实子任务边界的偏差，报告误切换率与成功率的关系。
相关：notes/26、32、19。

**11. 治理层与自进化层的接口**
缺口：Runtime Governance 的能力准入、EmbodiedGovBench 的升级安全、ICAN-Deploy 的身份稳定都为"新能力上线"准备，但没有任何自进化系统（ASPIRE、Zetta、PRACTICE）接入它们。
为什么重要：closed loop 这一格在两篇观点文章里只有定义没有机制。
MVE：把 ASPIRE 式技能库的"新技能入库"改为经过一个只读治理层（能力边界检查 + 审计记录），报告治理层拒绝率与任务成功率的权衡。
相关：notes/25、04、07、39。

**12. 长期运行口径的普及**
缺口：Habilis-β 的 TPH × MTBI 只有一个平台；ENPIRE 的 MRU/MTU 只有一篇。
为什么重要："Experience Scaling"需要指标（预测 P6）。
MVE：为任一开源 VLA + agent 系统跑一小时连续运行协议，报告 TPH、MTBI 与介入原因分类；与单次成功率对照，看排序是否改变。
相关：notes/27、06、08。

## Part D · 学习闭环

**13. 失败样本的价值：Q-Planning vs 只回收成功**
缺口：Q-Planning 的对照（90/80 vs 成功样本 SFT 55/30）是同批 rollout 上最干净的一组数字，但只有两个任务；VERITAS、RoboClaw 只回收成功数据。
为什么重要：决定数据回流管线该保留什么。
MVE：在 VERITAS 或 RoboClaw 式管线上加 Q-Planning 的小 Q 函数，同一批 rollout 下比较"只用成功 SFT"与"成败都用于 Q"的成功率与样本效率。
相关：notes/29、18、31。

**14. Fleet 数据的准入与锚点保护**
缺口：LWD 16 台机器人共享经验，但没有讨论数据准入；Memory Anchors 说明约 10% 锚点经验决定是否遗忘旧任务；通信攻击说明共享经验会共享污染。
为什么重要：fleet 学习的第一条安全性质是"一台机器人的坏数据不会毁掉全体"。
MVE：仿真多机器人设置里向共享缓冲注入一定比例的错误标注 rollout，测共享策略在新旧任务上的退化；加锚点保护与来源验证（Claim Provenance 式）看能否抵消。
相关：notes/28、15、37。

**15. twin 作为验证器的假阳性/假阴性率**
缺口：RoboSnap、Agentic Real2Sim、PerceptTwin 报告重建质量或"计划成功率"，没有一篇报告"twin 里过了、真机上挂了"的比例。
为什么重要：sandbox 的价值不在保真度本身，而在它作为筛选器的错误率。
MVE：对同一批 agent 生成的技能/计划，先在 twin 里评测再在真机评测，报告 2×2 混淆矩阵；按任务类型（接触密集 vs 几何为主）分层。
相关：notes/30、33、19。

**19. Agent-as-Teleoperator：用前沿 VLM agent 采集数据集的等量对照**
缺口：RoboCurve 的 GPT-6 Astra 演示（block → bowl 19/20、插入 10%）显示前沿 VLM 能以 waypoint 工具调用完成几何阶段；VERITAS 证明验证过的自主 rollout ≈ 人类示范（70 vs 65），但没有人用前沿 VLM agent 系统地采数据并与等量人类遥操作示范对照，也没有人处理 agent 数据在接触段的覆盖空洞与 waypoint 轨迹的形态偏差。
为什么重要：如果成立，示范采集的人力可以压到"只接管最后几厘米"；这是数据回流（T10）成本结构的根本变化。
MVE：同一任务 50 条 agent 采集（独立验证、执行层稠密轨迹、重定时）vs 50 条人类示范训同一 flow head，报告总成功率、接触段成功率、jerk；再做 agent-only / agent + 人接管末段 / agent + 闭环插入原语三组消融。
相关：notes/44、45、18、29、31、33。

## Part E · 总览、接口、多机

**16. 共享经验与共享世界知识层**
缺口：小红书长文四层共享里，只有状态记忆（RoboOS-NeXT）与策略（LWD）有实证；MeCo 的相似任务记忆化是共享经验的雏形，Thea 的场景图与 STEM 记忆是共享世界知识的候选载体。
为什么重要：fleet 的价值在多样性（I8），多样性的前提是经验能被其他机器人读懂。
MVE：两台仿真机器人、不同任务，一台的 ASPIRE 式技能与 AGM 式子目标记忆导出为结构化记录，另一台检索使用；报告零样本迁移收益与检索错误率。
相关：notes/37、22、04、12。

**17. 接口标准的权限模型**
缺口：MHS 与 ROSClaw 让任何模型接任何机器人，AgentRob 与通信攻击展示了被劫持的后果；MHS 预览未公开权限模型。
为什么重要：接口越开放，"任何被劫持的模型接任何机器人"越容易。
MVE：在 ROSClaw 式执行层上定义能力级权限（哪些技能需要人工确认、哪些可自动），复现 AgentRob 式注入攻击，报告拦截率与任务完成率的权衡。
相关：notes/36、39、25。

## Part F-G · 安全与基础

**18. Robot Autoresearch Bench**
缺口：软件侧有 PaperBench、RE-Bench、MLE-bench、KernelBench 衡量 AI 做研发；机器人侧的 ENPIRE、HARBOR、Nautilus、AgenticRobotics 没有共同基准，收敛速度、MRU/MTU、假设多样性、真机迁移差距无法跨论文比较。
为什么重要：没有基准，"自动研究"的数字只能定性定位（见口径账本）。
MVE：以 CaP-Gym 或 RoboCasa 为固定环境，定义 3-5 个有脚本验证器的任务，固定人类专家基线（RE-Bench 式），让不同 coding agent + harness 在固定预算下 hillclimb；报告收敛曲线、MRU/MTU、假设去重后的唯一假设数，以及仿真到真机的迁移差距。
相关：notes/43、06、08、25。
