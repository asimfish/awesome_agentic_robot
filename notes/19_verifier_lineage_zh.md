# 19 · 验证器谱系：LLM-as-a-Verifier、立场论文、Consilience、Agentic Harnesses

> 覆盖：LLM-as-a-Verifier（arXiv 2607.05391，2026-07）· Position: VLA Cannot Be Verified to Perform Physical Reasoning（2606.30686，2026-06）· Consilience for Verifier-Free Test-Time Scaling（2608.09898，2026-08）· Agentic Harnesses: LLM-Driven Verification Layers（2608.09857，2026-08）
> 相关解读：AGM（notes/12）· PRIMO R1（notes/17）· VERITAS（notes/18）· Thea 的 Evaluation as Exit Codes（notes/22）· PhyAgentOS 的 SessionVerifier（notes/21）· VASO（notes/09）
> 所属主线：T23、T24 · 材料来源：报告第 4 章 T23、第 7 章 I3

## 1. 一句话定位

2026 年 T23 主线的密度说明验证器已成为自进化循环的瓶颈。这一组工作从四个角度处理它：LLM-as-a-Verifier 把验证当作新的 scaling 轴（对评分 token 的 logits 取期望得到连续分数，沿评分粒度、重复评估、标准分解三个维度扩展，RoboRewardBench 87.4%，可作 RL 密集奖励）；立场论文指出成功率无法区分语义匹配与物理泛化，因此现有评测协议无法验证 VLA 是否在做物理推理；Consilience 讨论没有验证器时如何用置信度轨迹选 rollout；Agentic Harnesses 在规划与执行之间放 LLM-as-a-Judge 集成验证层，对抗攻击 97% 拦截。

## 2. 各篇要点

**LLM-as-a-Verifier**：不训练的通用验证框架。与让 LLM 输出离散分数的标准 judge 不同，它对评分 token 的 logits 分布取期望得到连续分数；这个概率形式让验证沿三个维度扩展——分数粒度、重复评估、标准分解。在 RoboRewardBench 上 87.4%，并能作为 RL 的密集奖励（报告第 4 章转述）。它把 Let's Verify Step by Step 的"过程奖励"思想推广到了不训练的通用 judge。

**立场论文（VLA Cannot Be Verified to Perform Physical Reasoning）**：把 VLA 策略分解为语义映射与物理动作决策两部分，论证任务成功率无法区分收益来自哪一部分；"互联网规模语义表征迁移到物理执行泛化"这一流行解释从未被独立验证，且在当前评测协议下不可检验。它要求受控变量的评测设计——对本仓库所有 T5/T9/T15 的成功率数字都是一句提醒。

**Consilience**：测试时扩展通常依赖外部验证器（编译器、测试用例、训练好的价值函数），但很多真实应用没有高质量验证器；基于置信度的无验证器测试时扩展几乎零开销。论文研究置信度轨迹的性质（报告第 4 章转述为"时间不对称性"）来改进 rollout 选择。对机器人的含义：当验证器缺席时，策略自身的置信度是最后的选择信号——但也是最容易被过度乐观污染的信号。

**Agentic Harnesses**：诊断机器人自主系统重执行、轻验证；规划模型偏向用户目标、可能违反科学伦理、记不住先前的安全风险、易受生态系统攻击。方法：在规划与执行之间加 LLM 驱动的验证层评估动作可否被允许，用 LLM-as-a-Judge 集成；报告第 4 章转述的数字是对抗攻击 97% 拦截。它把验证器从"成没成"扩展到"该不该做"，与 T17 安全主线相接。

## 3. 口径与局限

- 87.4%（RoboRewardBench）与 97%（对抗拦截）测的是验证器自身的准确率，不是被验证策略的成功率；两者不可与任务成功率并排。
- LLM-as-a-Verifier 与 Agentic Harnesses 都是不训练的 LLM 判断，延迟决定它们只能低频运行；与 AGM 的 2.43M 高频验证头是不同层级。
- 立场论文没有提出替代指标，只提出评测设计原则；Consilience 的机器人实验范围摘要未说明。

## 4. 关系定位与延伸批判

把 T23 的全部工作按"验证什么、多快、多贵"排列，可以得到一个三层验证器的雏形：高频门控（AGM 的几何证据、Thea 的 exit codes）→ 低频过程复核（PRIMO R1 的视频批评者）→ 连续评分与准入判断（LLM-as-a-Verifier、Agentic Harnesses）；形式验证（VASO）在部署前过滤，数字孪生（notes/30）在部署前预演。报告开放问题第 1 条就是把这个雏形做成可评测的系统。立场论文的警告应当反过来用于验证器本身：验证器判断"成功"时，判断的是语义上像成功还是物理上成功？PRIMO R1 的 67% 与 LLM-as-a-Verifier 的 87.4% 都需要这个拆分。最后，Lil'Log 与 AHE 的"评估器在演化循环之外"原则与 MEMENTO"先演化评估器"、Meta-Rewarding"评审的评审"直接冲突，机器人侧目前没有任何一篇工作正面处理这个冲突。
