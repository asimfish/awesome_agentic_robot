# 09 · 技能库谱系：从 LLM 提任务到形式化可验证的技能契约

> 覆盖：Agentic Skill Discovery（arXiv 2405.15019，2024-05）· Atomic Skill Library（2501.15068，2025-01）· ViReSkill（2509.24219，2025-09）· Growing with Your Embodied Agent（2509.18597，2025-09）· Neuro-Symbolic Code-as-Policies（2510.21302，NeurIPS 2025 Spotlight）· RATs / Playful Agentic Robot Learning（2606.19419，2026-06）· VASO（2606.05395，2026-06）
> 所属主线：T8、T2、T6、T17 · 材料来源：检索地图 T8 代表工作；报告第 4 章 T8

## 1. 一句话定位

技能库这条线回答三个问题：技能从哪来、怎么存、怎么信。2024-2025 年的工作解决"从哪来"（LLM 提任务 + RL 学 + VLM 验：Agentic Skill Discovery；VLP 拆子任务 + VLA 微调：Atomic Skill Library；失败重规划、成功即存：ViReSkill；人类纠正编码为技能：Growing）；2026 年的工作开始解决"怎么信"（RATs 用步级验证与失败诊断筛技能；VASO 用模型检查替代轨迹级证据）。

## 2. 各篇要点

**Agentic Skill Discovery**：完全由 LLM 驱动的技能发现——LLM 根据场景描述与机器人配置提出任务，为任务采样奖励函数与成功判定函数，RL 学策略，独立的 VLM 验证；技能库从零生长。它把 Eureka 式"LLM 写奖励"用到了技能库的构建上，并指出了 bottom-up 组合的盲区：只含"推"的库永远长不出"抓"。

**Atomic Skill Library**：三轮数据驱动流程——Vision-Language-Planning 把任务拆成子任务、抽象出原子技能定义、采集数据并微调 VLA 构建技能库；库随三轮更新动态扩展，覆盖的任务范围随之增长。这是"技能 = VLA 微调出的原子动作"的路线，与"技能 = 代码"的路线形成对照。

**ViReSkill**：诊断 LLM/VLM 规划的两个障碍——符号计划很少接地到场景几何与物体物理、相同 prompt 输出不稳定。方法：失败时基于当前场景重规划；成功时把执行过的计划存为技能，下次直接重放而不再调用 LLM/VLM。LIBERO、RLBench 与真机评测。它是 L5 技能演化里"最便宜"的形态：技能就是一次成功的计划。

**Growing with Your Embodied Agent**：人在环路的终身代码生成——把纠正编码为可复用技能，外部记忆 + RAG + hint 机制动态复用；在 Ravens、Franka Kitchen、MetaWorld 与真机上评测，解决需要 20 个以上原语的"盖房子"任务。它承认 LLM 在极长程任务上的推理不足，用人来补。

**Neuro-Symbolic Code-as-Policies**：在代码生成中加入显式符号验证与交互式验证——生成探索性代码主动与环境交互获取缺失观测，同时保持任务相关状态；比 CaP 基线成功率 +46.2%（RLBench 与真机、动态与部分可观测场景）。它是"验证进入技能生成过程"的早期形态。

**RATs（Playful Agentic Robot Learning）**：在下游任务到来前用自主提出的探索任务"玩耍"——提出新颖但可学的任务、规划并执行代码策略、验证中间进度、诊断失败、用密集步级反馈重试、把成功执行蒸馏进持久代码技能库；测试时从冻结库检索技能。LIBERO-PRO 比 CaP-Agent0 +20.6 个百分点，技能可直接检索进其他 Code-as-Policy agent 的上下文。

**VASO**：主张基础模型压低了创建技能的成本，却没有压低信任技能的成本——执行反馈、单元测试、环境奖励、LLM 自评都只是轨迹级证据。方法：每个技能是带两个接口的语义契约（形式接口把状态/观测/控制命令对齐到逻辑命题供模型检查；面向规划器的接口引导可执行行为生成）；模型检查器先过滤逻辑不一致的契约，再验证契约诱导的计划是否满足时序安全约束，反例变成文本梯度更新契约；97.2% 规范符合率。

## 3. 口径与局限

- Agentic Skill Discovery 与 Atomic Skill Library 的数字为各自仿真/真机设置，摘要未给统一指标。
- ViReSkill 的收益取决于"同一场景再次出现"的频率，重放对场景变化的鲁棒性未量化。
- RATs 的 +20.6pp 对比对象是 CaP-Agent0（同一原语族），是本线少有的可比数字。
- VASO 的 97.2% 是"规范符合率"，不是任务成功率；形式接口需要人写命题与状态的对齐，这部分成本论文未量化。

## 4. 关系定位与延伸批判

技能库的两条路线——代码技能（CaP 家族、ViReSkill、RATs、ASPIRE）与权重技能（Atomic Skill Library、Harness VLA 调用的 VLA 原语）——在 2026 年的分工由 ENPIRE 的混合实验与 HyMeS 的口号"技能在权重里、记忆在代码里"给出（notes/13）。本线最重要的转折是 VASO：技能库从"代码片段集合"变成"带验证证据与适用范围的知识库"，与 AgenticRobotics 的证据分级技能库、Harness VLA 的适用范围规则同向。未走之路：没有一篇工作把技能的**进入条件**（BATON 指出 VLA 原语只有退出条件，notes/14）作为技能库的一等字段；把 VASO 的形式接口用于描述进入条件，是把 T8 与 T4 接起来的最短路径。
