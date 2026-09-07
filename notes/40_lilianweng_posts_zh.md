# 40 · Lil'Log 两篇深度解读：《LLM Powered Autonomous Agents》与《Harness Engineering for Self-Improvement》

> Lilian Weng，Lil'Log · 2023-06-23（lilianweng.github.io/posts/2023-06-23-agent/）· 2026-07-04（lilianweng.github.io/posts/2026-07-04-harness/）
> 所属主线：T0、T15、T24 · 材料来源：本仓库源材料之四；两文 60 条参考文献全部收入 T0（见 notes/41-43）；报告第 5 章

## 1. 一句话定位

2023 年那篇给出了 Agent 的经典分解——LLM 大脑 + Planning（子目标分解、反思与精炼）+ Memory（短期 = 上下文，长期 = 外部向量库与快速检索）+ Tool use（外部 API）——是小红书长文那张完整架构图的直系祖先。2026 年那篇把 harness 定义为"围绕基座模型、编排执行的系统：决定模型如何思考与规划、如何调用工具与行动、如何感知与管理上下文、如何存储产物、如何评估结果"，判断近期的递归自我改进不太可能从模型改写自己的权重开始，而更可能首先发生在 harness 层。

## 2. 2023：LLM Powered Autonomous Agents

- **Planning**：任务分解（CoT、ToT、LLM+P 把问题翻译成 PDDL）与自反思（ReAct 的 Thought/Action/Observation 循环、Reflexion 的反思记忆、Chain of Hindsight、Algorithm Distillation 的上下文内 RL）。
- **Memory**：类比人类的感觉/短期/长期记忆；短期是上下文内学习，长期是外部向量库 + 最大内积搜索（LSH、ANNOY、HNSW、FAISS、ScaNN）。
- **Tool use**：MRKL 的模块化路由、TALM/Toolformer 的自监督工具学习、HuggingGPT 的模型调度、API-Bank 评测、ChemCrow 与 Boiko 等的科学工具 agent。
- **案例与挑战**：Generative Agents 的记忆流 + 反思 + 规划；AutoGPT、GPT-Engineer；三个挑战——有限上下文、长程规划与分解的困难、自然语言接口的不可靠。

对机器人的映射（报告 5.1 节）：Planning → 小红书长文的 Agent/System 2 层；Memory → Memory/Skill/Dataset 三类；Tool use → Harness/Runtime 的 Tool Routing 与 Skill Layer 的四类原语（代码技能、解析原语、VLA 原语、RL 策略）。三个挑战分别对应 T5 记忆、T4 长程、T23 验证器。

## 3. 2026：Harness Engineering for Self-Improvement

- **三种设计模式**：工作流自动化（plan → execute → observe/test → improve）；文件系统即持久记忆（状态与产物存文件而非塞进上下文）；子代理与后台任务（并行搜索假设、监控作业、合并结果）。
- **优化对象阶梯**：instruction prompts → structured context → workflow → harness code → optimizer code。ACE/MCE 在 context 一级，ADAS/AFlow 在 workflow 一级，Meta-Harness/Self-Harness/AHE 在 harness code 一级，STOP/DGM/Hyperagents 在 optimizer code 一级。
- **两个关键发现**：STOP 的自学优化器在 GPT-4 上有效、在 GPT-3.5 与 Mixtral 上退化；Lin 等（Harness Updating ≠ Harness Benefit）拆出两个轴——写 harness 的能力从 Qwen3.5-9B 到 Claude Opus 4.6 几乎持平，利用 harness 的能力非单调、中等模型受益最大。评估器与权限控制必须在演化循环之外：AHE 把 runs 目录、tracer、verifier 与 LLM 配置设为只读，才能把收益归因到 harness 编辑而非奖励作弊。
- **自动研究**：AI Scientist、Nature 上的端到端自动化、ScientistOne、Autodata，以及 Trehan & Chopra 总结的六类失败模式（训练数据默认偏置、实现漂移、记忆退化、过度乐观、领域知识不足、科学品味弱）。
- **RSI 七个挑战**：弱而模糊的评估器、上下文与记忆的生命周期、负面结果、多样性塌缩、奖励作弊、长期成功、人的角色。

对机器人的映射（报告 5.2 节）：工作流自动化 → ENPIRE / ASPIRE / RoboClaw；文件系统记忆 → PhyAgentOS 的 State-as-a-File、ENPIRE 的 Markdown 研究总结；子代理 → ENPIRE 的 Agent 团队 × 集群、HARBOR、RATs；阶梯 → SkillOpt（context）、ASPIRE（workflow/库）、RHO/SHAPER（harness code）、Meta-Harness/HarnessOpt（optimizer code）。

## 4. 两篇没有覆盖的部分

Lil'Log 的 harness 生活在数字世界：状态可读、结果可判、失败可重试一千次。Thea（notes/22）指出物理世界拒绝白送读状态与判结果；Harness Engineering for Physical AI（notes/23）指出第三个缺口——时间。这三点是机器人 harness 与软件 harness 的本质差异，也是本仓库 I3、I5、I6 三条洞见的出发点。

## 5. 延伸批判

两篇文章合起来提供的是**一把尺子**而不是一个方法：任何自称"自进化"的机器人系统都可以被问三个问题——它在阶梯的哪一级改东西、它的评估器在不在循环之外、它的收益是"harness 更新"还是"harness 收益"。用这把尺子量本仓库的核心工作：ENPIRE 在 harness code 一级、评估器由人写且只读、收益归因未拆分（Codex/Claude/Kimi 的差距未解释）；Zetta 在 harness code 一级、评估器（critic）自己被演化——这正是 Lil'Log 警告的配置；SkillOpt 在 context 一级、评估器是 held-out 分数且外置——最符合纪律。这把尺子应当成为本仓库评价新工作的默认清单。
