# 小红书原帖转写：Harness 之后，Agent+Robot 下一站是什么？

- 作者：具身RL日记
- 平台：小红书（39 张图文卡片）
- 链接：https://www.xiaohongshu.com/explore/6a9d2fb10000000026033df2
- 标签：#具身智能 #VLA #Agent #强化学习 #Harness #世界模型 #多智能体

## 导读（帖子正文）

2026 年，Agent × Robot 正在成为具身智能的一条显性主线。CaP-X 开始探索 Coding Agent 能否直接生成机器人策略；RoboClaw 把数据采集、训练和部署串进同一个 Agent Loop；ROSClaw、Harness VLA、PhyAgentOS 则继续补上 Runtime、Memory、Verifier、安全执行等系统能力；Anthropic 的 MHS 又把问题推进到"Agent 如何标准化接入真实硬件"。但沿着这条路线继续看，会发现：Harness 只是起点。

01｜Memory：机器人不只要看见现在，还要记住过去——物体去过哪里、任务做到哪一步、刚才为什么失败。
02｜Reflection & Evolution：从 Retry → Replan → Reflection → Skill Memory → Policy Update，让一次失败真正沉淀成下一次成功的经验。
03｜Edge & Runtime：Agent 可以慢思考，机器人却必须毫秒级响应。复杂推理可以上云，安全控制、反馈闭环和异常处理必须留在端侧。
04｜Agent × VLA × RL：代码、Prompt、Skill 能快速进化，但长期积累的真实经验最终还要反哺 VLA，通过 RL / Offline-to-Online Learning 写回模型权重。
05｜Sim / World Model：真实世界试错太贵。更合理的闭环可能是：Real → Sim → Learn → Verify → Real。
06｜Multi-Robot：下一步不只是单机终身学习，而是一台机器人学会后，通过 Shared Memory、Shared Skill、Fleet Learning，把经验同步给整个机器人群体。

未来机器人真正的 Scaling，不只来自更大的模型，而来自：Foundation Model × Memory × Skills × Harness × Runtime × Data Flywheel × Embodiment。

## 图片卡片逐页转写

### 卡片 1：标题

Harness 只是开始：Agent+Robot 真正值得关注的 6 个下一站

过去一年大家都在谈 VLA 和 WAM（世界-动作模型）。最近又开始谈 Agent 和 Harness。但如果把这些词拆开看，很容易陷入一种"新概念替代旧概念"的错觉。作者的观点：它们不是互相替代，而是在逐渐拼成一个真正的机器人系统。

### 01｜Memory：今天的机器人最大的问题之一，是它没有真正的"过去"（卡片 2-7）

传统 VLA 最典型的输入：当前图像 + 当前语言指令 + 当前 proprioception → Action。这非常像一个"每隔几十毫秒醒来一次、但不断轻微失忆的人"。短程 Pick & Place 没问题；但任务一旦变成长程（"先把红色杯子放到柜子里，再把蓝色杯子放到桌子上，最后把刚才第一个杯子取出来"），第一个杯子已经不在当前画面中，模型必须记住：刚才看见了什么？自己执行了什么？哪个杯子已经移动？柜门有没有关？任务做到第几步？

所以长程 Manipulation 的核心变量，从 State 变成 History。

- **RoboMME**（2026）直接把这个问题单独做成 Benchmark：Temporal / Spatial / Object / Procedural 四类记忆任务，共 16 个 manipulation task（计数抓了几次、记住被遮挡物体的位置、记住之前被指示的目标、记住一段演示动作的顺序）。意义：Memory 不再只是 LLM Agent 的辅助模块，而开始变成 Robot Policy 本身的一项核心能力。
- **PonderPounce**（2026.08）：不再专门设计复杂 Robot Memory Module，而让一个慢速 MLLM 保留整段 Episode Context，再异步把压缩后的 cognition 信息发送给快速 VLA。在 RoboMME 上 9B 配置达到 60.83%，相比 current-observation π0.5 的 17.93% 提升明显。结构：Slow Brain = 长上下文 + 记忆 + 推理；Fast Brain = 当前视觉 + 本体状态 + 动作；二者异步通信。

作者预测机器人 Memory 最终不会只有一个 Transformer Context，至少出现四类：
- Working Memory：当前任务做到哪（step 3/8，当前目标 = cup，drawer = opened）
- Episodic Memory：具体某次经历（"昨天抓这个透明杯子时，因为反光导致抓取位置偏左"）
- Semantic Memory：从很多经历里抽象出的知识（透明物体视觉不稳定；软包装受力后会变形；这个抽屉容易卡住）
- Skill Memory：把成功执行的方法本身保存下来。**ViReSkill** 很典型：失败 → 根据当前视觉重新规划；成功 → 把经过验证的 Plan 存进 Skill Memory；下次类似场景直接复用。

真正值得关注的不只是 Long Context，而是：机器人什么时候应该记？记什么？什么时候忘？什么时候把一次 Episode 提炼成 Knowledge？这已接近传统 Agent 的 Memory Engineering，只是机器人版本多了一层：Spatial + Temporal + Physical。

### 02｜Reflection：失败一次以后，机器人到底学到了什么？（卡片 7-12）

今天很多机器人会 Retry，但 Retry ≠ Learning。第一次没抓起来，Agent 说"再抓一次"，第二次成功，任务结束；下次碰到同样问题，机器人可能又重新失败一遍。

真正的闭环应该是：Execution → Verification → Failure Attribution → Reflection → Replan → Validation → Memory / Skill Update。失败不仅改变当前 Plan，还应该改变未来 Behavior。这是 2026 年 Agentic Robotics 特别明显的趋势。

- **AgenticLab** 已经把 Perception → Task decomposition → Execution → Online verification → Replanning 做成真实机械臂闭环，并明确观察到遮挡、场景变化、多步 grounding consistency 等问题。
- **Harness VLA** 进一步让 Agent 根据 Task-specific execution traces、Global success rules、Failure models 学习 Frozen VLA 的"使用说明书"。它甚至不修改 VLA 权重。Agent 学的是：这个 VLA 什么情况下靠谱？什么时候应该 retry？什么时候应该先 MOVE_TO？什么时候应该重新 Grounding？什么时候别让 VLA 做，而交给 analytic primitive？
- **ASPIRE** 再往前推一层：机器人运行程序 → 收集 multimodal traces → Coding Agent 分析为什么失败 → 修改机器人代码 → 重新验证 → 验证有效后把修复方式沉淀进 Skill Library → 以后复用。这时系统已经出现"经验复利"：第 1 次任务留下一个 Skill，第 100 次任务以后可能已经拥有几十个经过真实执行验证的 Skill。

作者提出"自进化"分层（不是看到 Agent 会 Replan 就叫 Self-Evolution）：
- L1 Retry：再试一次
- L2 Replan：根据新状态修改计划
- L3 Reflection：分析为什么失败
- L4 Memory Evolution：把经验保存下来
- L5 Skill Evolution：形成新的 reusable skill / code / strategy
- L6 Policy Evolution：真正修改 VLA / Policy 权重
- L7 Fleet Evolution：一台机器人获得的经验，成为整个机器人群体的训练数据

2026 年已经开始从 L2/L3 快速向 L4-L7 延伸。

### 03｜机器人必须有两个时间尺度：Agent 负责秒，Controller 负责毫秒（卡片 12-16）

Agent × Robot 在 Demo 里特别容易被忽视的问题：Latency。Coding Agent 可以思考 2 秒，机械臂不能等 2 秒再决定要不要刹车。机器人天然存在两个时间尺度：
- Slow Loop（LLM / VLM / Agent）：任务理解、任务拆解、Memory Retrieval、异常归因、重新规划、生成 Skill；几百毫秒～数秒运行一次。
- Fast Loop（Controller / Policy / Safety Runtime）：servo、impedance control、collision avoidance、force limit、trajectory tracking、emergency stop；几十 Hz、几百 Hz 甚至更高。

这也是 **Fast-in-Slow、OneTwoVLA、StreamVLA、LaST0** 这批工作都在研究的：什么时候需要慢思考，什么时候应该直接行动。Fast-in-Slow 把 System 1 嵌入 System 2，并报告在 action chunking 设置下达到 117.7 Hz；StreamVLA 只在 subtask transition 时触发慢推理，其余时间锁住高层意图，让 Flow Matching action head 持续执行；LaST0 更进一步，甚至不一定非要用语言做 reasoning，把未来视觉、3D geometry 和 proprioception 放进 latent spatio-temporal CoT，由低频 reasoning expert 给高频 acting expert 提供物理表征。

这和 Agent Harness 发生了有趣的汇合。**Harness Engineering for Physical AI** 提出：软件 Agent 的 Harness 主要管 Tool Call，但机器人 Harness 必须同时管 Control、Compute、Communication。模型一次推理慢了，不只是"回答慢"，它会改变控制 schedule；网络堵塞，不只是"请求晚到"，它会改变机器人 trajectory。所以未来 Robot Harness 很可能必须成为 Real-time-aware Harness：知道这个模型最大 latency 是多少、这个 Skill deadline 是多少、网络掉线以后调用哪个 fallback、哪些动作必须本地完成。

原则："Cloud can think. Edge must survive."——云端负责聪明，端侧负责：无论云端发生什么，我都不能撞人。

### 04｜Agent + VLA + RL：真正的自进化最终还是要"写回权重"（卡片 16-22）

这点容易被 Harness 的热度掩盖。Skill Memory、Code Generation、Prompt Evolution 都很重要，但系统层记忆不能完全替代模型学习。比如机器人插 USB，第一次偏 3mm，Agent 可以记"下次向左修正一点"，这可以放进 Skill；但随着交互次数增加，它最终应该学会视觉特征 → 接触状态 → 力反馈 → 微动作之间的连续关系，这部分最终适合进入 Policy Weight。

所以未来真正有意思的架构不是 Agent or VLA，而是：Agent → 管学习过程；VLA → 承载学习后的运动能力；RL → 把真实反馈写回 Policy。

- **CaP-X** 很有代表性：不只是 Benchmark Code-as-Policy，还提出 CaP-Agent0（通过 multi-turn interaction、execution feedback、visual differencing、skill synthesis、ensemble reasoning 提高 Agent 鲁棒性）和 CaP-RL（利用可验证 Reward 对 Coding Agent 进一步做 RL）。CaP-X 真正有意思的不是"代码终于打败 VLA"，而是 Agentic Test-time Compute + Environment Feedback + RL 开始结合。
- **RoboClaw** 解决另一个痛点：传统 pipeline Collect Data → Train → Deploy 三阶段分开；RoboClaw 尝试 Collection ↔ Learning ↔ Deployment 由同一个 Agent Loop 串起来。尤其是 EAP（Entangled Action Pairs）：把正向 Skill 和恢复 / inverse Skill 绑定，机器人完成动作后可以自己恢复场景、继续采数据，减少人工 reset。论文报告相对 baseline 的 long-horizon success 提升 25%，同时降低 53.7% 的人工时间投入。作者认为这件事被低估：机器人 RL 最贵的可能不是 GPU，而是人——每失败一次，有人扶机器人、重新摆杯子、重置抽屉、检查环境。如果 Agent 能自己 Reset，机器人第一次拥有真正意义上的 Autonomous Experience Generation。
- **Learning While Deploying (LWD)**：直接做到 Fleet Scale，16 台双臂机器人，部署过程中收集 autonomous rollout + human intervention，再用 offline-to-online RL 更新同一个 generalist VLA，然后重新部署，形成 Deploy → Experience → RL → Updated Policy → Redeploy。论文在 8 个真实操作任务上报告单一 generalist policy 随 fleet experience 增加持续提升，最终平均成功率达到 95%。

这非常接近作者认为未来真正重要的一条路线：Robot Data Flywheel。机器人不是"训练完 → 出厂 → 永远不变"，而是机器人本身成为训练数据生产设备。

### 05｜Real → Sim → Learn → Real，可能比"真机自由探索"现实得多（卡片 22-26）

软件 Agent 可以 run → fail → retry × 1000；机器人不行，碰一次可能坏一个零件。所以真机上的 Self-Evolution 必须解决 Physical Exploration Cost。这是为什么 Simulation / Digital Twin / World Model 会和 Agent 自进化越来越深地结合——不是为了回到"全部在仿真训练机器人"，而是让 Sim 变成机器人的安全测试环境。

例如 Agent 生成新的 insert_connector skill，正确流程不应该是"生成代码 → 真机直接跑"，而是：生成 Skill → Static Check → Digital Twin rollout → Domain Randomization → Failure Mining → Safety Verification → Hardware-in-the-loop → Small-scale Real Deployment → Real Feedback → Simulation Update → 重新训练。形成 Real → Sim → Learn → Verify → Real。

- **TwinRL** 很接近这个思想：先根据真实环境建立 Digital Twin，在 Twin 中并行 RL，生成 interactive trajectories、找到 failure-prone configurations，再利用这些经验指导后续 real-world RL。论文报告只使用约 20 分钟 on-robot interaction，就在四项任务实验中达到接近 100% 的 ID / OOD 成功表现，并比此前 real-world RL 方法快 30% 以上收敛。
- **Arcadia** 从更大的生命周期角度：真实探索 → Generative Scene Reconstruction → Representation Learning → Sim-from-Real evaluation → Deployment Feedback 串成完整闭环。

World Model 在 Agentic Robot 中有一个经常被忽略的角色：它不一定非得直接预测 Action，还可以是机器人给新 Skill 做"脑内预演"的地方，也就是 Physical Agent 的 Sandbox。这和 Claude Code 很像：Claude Code 有测试环境，机器人也必须有；区别只是机器人的 Test Environment 是 Physics。

### 06｜Multi-Robot：真正的大规模进化，不应该发生在一台机器人身上（卡片 26-31）

假如机器人 A 花了 3 个小时学会"如何抓一个透明杯子"，机器人 B 换了一个房间，为什么还要重新学 3 个小时？

Multi-Agent Robot 早已存在：
- 2023 年的 **RoCo** 已经让不同 Robot Agent 用自然语言讨论谁负责什么、谁能到达哪里、谁需要避让，再把协商后的 waypoint 交给底层 motion planner。
- **MALMM** 把一个机器人系统内部进一步拆成 Planner / Controller / Supervisor 多个 Agent。
- **RoboOS** 明确提出 Embodied Brain + Cerebellum Skill Library + Real-Time Shared Memory，把 Shared Memory 用于不同 embodiment 之间的时空状态同步，同时研究 edge-cloud communication 和多机器人协作。
- **REMAC** 进一步加入 pre-condition check、post-condition check、self-reflection、self-evolvement，让多机器人长期任务可以根据场景持续修改协同计划。

作者认为真正的大故事在后面：Shared Skill（机器人 A 学会一个 Skill，B 可以下载）、Shared Experience（A："这种透明杯子从侧面抓更稳定"，B 直接获得）、Shared World Knowledge（一个机器人发现"这款冰箱门需要先向外拉，再向左"，整个 Fleet 更新）、Shared Policy Improvement（Fleet 所有真实执行数据统一回流，共同更新 Generalist VLA，再重新部署给所有机器人）。

这时机器人产业第一次可能获得类似互联网产品的 Network Effect。软件为什么进化快？100 万用户每天都在产生反馈。未来如果有 100 万台 Robot，每台每天执行 100 次任务，那就是 1 亿次 Physical Interaction / Day。真正可怕的 Scaling Law 可能不是再多买 10 万张 GPU，而是 Experience Scaling。

### 完整架构图（卡片 31-34）

Human Goal
→ Agent / System 2（Reasoning、Planning、Reflection、Memory Retrieval）
→ Harness / Runtime（Context、Tool Routing、Permission、Scheduling、Verification、Recovery）
→ Skill Layer（Code Skill、Analytic Primitive、VLA Primitive、RL Policy）
→ Fast System / System 1（VLA、Motion Planner、Controller、Safety Reflex）
→ Hardware / MHS / ROS 2
→ Physical World
→ Evidence + Episode + Failure + Human Feedback
→ Memory / Skill / Dataset
→ Sim / Digital Twin / RL / Continual Learning
→ New Skill / New Policy
→ 重新部署

整个系统从 Goal → Action 变成 Goal → Action → Experience → Learning → Better Action。后面这个循环才真正接近 Self-Evolving Robot。

### 2026 年重点盯住三个"闭环"（卡片 34-35）

- 第一条 Execution Loop：Plan → Act → Verify → Replan。解决"这次任务能不能做完？"AgenticLab、Agentic Robot、Harness VLA、PhyAgentOS 都在这里。
- 第二条 Learning Loop：Experience → Reflection → Skill / Policy Update → Redeploy。解决"下次能不能比这次做得更好？"ViReSkill、ASPIRE、RoboClaw、Arcadia、TwinRL、LWD 都在这里。
- 第三条 Fleet Loop：Robot A Experience → Shared Memory / Dataset → Global Update → Robot B。解决"一台机器人学到的东西，能不能变成整个群体的能力？"RoboOS、REMAC、LWD 已经开始出现一些答案。

### 重新定义（卡片 35-39）

Agent + Robot 的下一阶段是什么？不只是 Harness，而是 **Persistent Physical Agent**：一个机器人系统必须能够记住过去、理解现在、预测未来、发现失败、修正计划、学习技能、更新策略、共享经验、安全执行。

Harness 解决的是：Agent 怎样稳定地使用已有能力。真正下一步要解决的是：机器人怎样通过长期物理交互，不断产生新的能力。两个问题连起来，才是 Physical Agent → Self-Evolving Physical Agent。

**为什么更看好"Agent + VLA + RL"，而不是三选一？** 过去容易问"Agent 能不能替代 VLA？""VLA 足够强以后还需要 Agent 吗？""RL 会不会最终统一一切？"——这几个问题可能本身就问错了。未来更可能是：VLA 提供通用运动先验；Agent 提供长程推理、工具调用和经验组织；RL 用真实反馈把长尾能力写回 Policy；World Model / Digital Twin 提供低成本试错；Memory 保存跨 Episode 经验；Harness 管执行；Runtime 管安全；Fleet 提供持续数据。它们共同组成一台长期工作的机器人。

下一阶段值得关注的不只是 Model Scaling，也不只是 Harness Scaling，而是 **System Scaling + Experience Scaling**。机器人的终局可能从来都不是"训练出一个完美模型，然后部署"，而是：先训练出一个足够好的机器人，让它开始工作；然后让工作本身，继续训练机器人。这可能才是 Physical AI 真正出现 Scaling Flywheel 的那一天。

——具身RL日记
