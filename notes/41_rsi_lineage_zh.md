# 41 · RSI 谱系：从 Good 1965 到 BigBang-V1——软件侧递归自我改进的四个环节

> 覆盖：Good（1965）· Yudkowsky（LessWrong 2008）· Gödel Machine（cs/0309048，2003）· STaR（2203.14465，NeurIPS 2022）· Reflexion（2303.11366，NeurIPS 2023）· Self-Refine（2303.17651）· Let's Verify Step by Step（2305.20050，ICLR 2024）· Self-Rewarding LMs（2401.10020）· SPIN（2401.01335，ICML 2024）· Meta-Rewarding LMs（2407.19594）· Absolute Zero（2505.03335）· Anchored Self-Play for Code Repair（2607.03523，ICML 2026）· The AI Scientist（2408.06292）· Towards end-to-end automation of AI research（Nature 2026）· ScientistOne（2605.26340）· Autodata（2606.25996）· BigBang-V1（Endless Frontier 技术报告）· HiSME（2605.28390）· Anthropic《When AI builds itself》（2026）
> 所属主线：T24、T0 · 材料来源：具身纪元文章第二节；Lil'Log 2026 文的参考文献

## 1. 一句话定位

具身纪元文章用两条轴线整理 RSI：改进的环节（部署时自演化 / 训练时自迭代 / 自我评估 / 自动研究）× 人的参与程度。这份合评把软件侧的谱系按第一条轴排好，供机器人侧对照（对照表见报告第 6 章）。概念源头是 Good 1965 的"智能爆炸"设想与 Schmidhuber 2003 的 Gödel Machine（只有能证明修改会提高效用时才执行修改）；Yudkowsky 2008 的 LessWrong 长文是概念在 AI 安全社区的系统论述；Anthropic 2026 年的《When AI builds itself》判断路径是"代码建议 → 编程智能体自改代码 → AI 参与设计与训练后继系统"，并认为具身智能可能紧随，但物理制造、实验周期与部署是新的速度瓶颈。

## 2. 四个环节的代表

**部署时自演化（权重不变）**：Reflexion——做完任务后把测试/环境反馈写成反思存进记忆，下次带着经验重试，HumanEval 91%（具身纪元转述）；Self-Refine——同一模型生成 → 自我反馈 → 精炼，不训练；HiSME——从执行轨迹学"怎样生成与修改技能"的元技能并反过来整理技能库，MineDojo 0.700 → 0.856。机器人侧对应：ASPIRE、RoboHarness、Zetta。

**训练时自迭代（上一版制造下一版）**：STaR——生成推理、答对保留、答错看答案重推、筛出的过程微调下一版；SPIN——与自己的历史版本博弈，弱模型变强，无需额外人类数据；Self-Rewarding——模型用 LLM-as-a-Judge 给自己打分并做 DPO，回答与评价能力同时迭代；Absolute Zero——零数据自博弈，模型自己提出可验证任务并求解；Anchored Self-Play——带锚点的自博弈代码修复避免漂移；BigBang-V1——出题者/批评者/元批评者合成约一万条可验证难题更新权重（证据主要来自团队技术报告）。机器人侧对应：RoboClaw、LWD、Q-Planning。

**自我评估（改进 judge / reward model / PRM / verifier）**：Let's Verify Step by Step——过程奖励模型逐步标出推理出错位置而非只看最终答案；Meta-Rewarding——同一模型既当回答者、评审者和"评审的评审"，四轮后 AlpacaEval 2 长度控制胜率 22.9% → 39.4%。机器人侧对应：PRIMO R1、VERITAS、LLM-as-a-Verifier。

**自动研究（提假设、改算法、跑实验、安排下一轮）**：The AI Scientist——从代码模板出发提想法、查新颖性、改代码、跑实验、画图、写论文并接受自动评审；其 Nature 版本《Towards end-to-end automation of AI research》（Nature 651:914-919, 2026）；ScientistOne——以证据链组织自主研究；Autodata——作为数据科学家的 agent 生成高质量合成数据。机器人侧对应：Eureka → DrEureka → HARBOR → ENPIRE。

## 3. 口径与局限

- 这些数字（HumanEval 91%、MineDojo 0.856、AlpacaEval 39.4%）全部是软件/推理基准，与机器人成功率无可比性；它们的意义是展示每个环节"可以被做"，不是"做得多好"。
- Self-Rewarding 与 Meta-Rewarding 把评估器放进了被改进的对象里，与 Lil'Log/AHE"评估器在循环之外"的原则直接冲突——这是 RSI 内部未解决的张力，机器人侧尚未正面处理。
- BigBang-V1 的证据来自技术报告；Anthropic 的文章是路线判断而非实验。

## 4. 关系定位与延伸批判

把四个环节叠到讲稿公式 $z_{t+1} = A(z_t, \tau_t, r_t, \log_t)$ 上：部署时自演化改 $z$ 里的记忆/技能/harness，训练时自迭代改权重，自我评估改 $r$ 的来源，自动研究改整个流程。具身纪元文章的核心判断——前沿 LLM 更可能先成为 Robot RSI 的认知中枢——在这张表上有一个具体形态：LLM 在四个环节里都已经有软件侧的成熟实例，机器人侧缺的是让这些实例的 $\tau$、$r$、$\log$ 来自物理世界，而这要求可重复、可扩展的验证环境（notes/30）与可靠的验证器（notes/19）。Gödel Machine 的原则（可证明有益才修改）在 2026 年以 VASO 的模型检查（notes/09）与 SkillOpt 的严格提升门（notes/05）两种弱化形式回到了实践中——前者证明安全性质，后者证明验证集上的提升；两者都还证明不了"真机上会更好"。
