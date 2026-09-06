# 《Agent + Robot 论文检索地图》转写

来源：用户提供的两页表格图片。三列：主线 / 建议检索关键词 / 代表工作。机器可读版本见 `data/topics.csv`（增加了第 0 条基础主线）。

| # | 主线 | 建议检索关键词 | 代表工作 |
|---|---|---|---|
| 1 | Agent + Robot 总览 | Agentic Robotics / Embodied Agent / LLM Robot Agent / Physical AI Agent | AgenticLab、Agentic Robot、ManiAgent |
| 2 | Coding Agent 控机器人 | Code-as-Policy robotics / robot coding agent / coding agents robot manipulation | Code as Policies、CaP-X、RHO、ASPIRE |
| 3 | OpenClaw / ROS | OpenClaw robotics / ROS2 agentic robot / MCP robotics | ROSClaw、OpenClawPi、AgentRob |
| 4 | 长程任务 | long-horizon robotic manipulation agent / hierarchical robot agent | RoboClaw、H-WM、Agentic Robot、REMAC |
| 5 | Robot Memory | robot memory / memory-augmented VLA / episodic memory robotics / history-dependent manipulation | RoboMME、PonderPounce、ViReSkill |
| 6 | Reflection / 反思纠错 | robot self-reflection / closed-loop replanning robot / failure reflection robotics | REMAC、AgenticLab、ASPIRE |
| 7 | Self-Evolution / 自进化 | self-evolving robot agent / lifelong embodied learning / continual robot learning | Arcadia、ASPIRE、PhyAgentOS、Growing with Your Embodied Agent |
| 8 | Skill Library / 技能库 | robot skill memory / atomic skill library / autonomous skill discovery | Agentic Skill Discovery、Atomic Skill Library、ViReSkill |
| 9 | VLA + RL | VLA reinforcement learning / online RL VLA / offline-to-online robot policy | TwinRL、LWD、SAC Flow、CaP-RL、TT-VLA |
| 10 | 部署数据回流 | learning while deploying robot / fleet robot learning / deployment feedback robot policy | Learning While Deploying、RoboClaw、Arcadia |
| 11 | 数字孪生 / Sim2Real | digital twin robot RL / sim-from-real robotics / simulation guided robot learning | TwinRL、Arcadia |
| 12 | World Model | robot world model planning / hierarchical world model robotics | H-WM |
| 13 | 快慢双系统 | dual-system VLA / fast slow robot reasoning / System 1 System 2 robotics | Fast-in-Slow、OneTwoVLA、StreamVLA、LaST0、RationalVLA |
| 14 | Edge Agent / 端侧部署 | edge embodied AI / on-device VLA / robot inference latency | Fast-in-Slow、Harness Engineering |
| 15 | Harness | robot harness / Physical AI harness / VLA harness | RHO、Harness VLA、Harness Engineering、PhyAgentOS |
| 16 | Runtime | embodied agent runtime / robot runtime governance | PhyAgentOS、Runtime Governance |
| 17 | 安全 | embodied agent safety / robot agent safety envelope / policy constrained execution | ROSClaw、Runtime Governance、RationalVLA |
| 18 | 标准接口 / Hardware API | agent hardware interface / AI hardware standard / MCP physical devices | MHS、ROSClaw |
| 19 | 多机器人协作 | multi-robot LLM / multi-agent robot collaboration | RoCo、REMAC、RoboOS |
| 20 | 跨本体 | cross-embodiment robot agent / heterogeneous robot collaboration | RoboOS、ASPIRE、Harness VLA |
| 21 | 群体学习 / Fleet Learning | fleet learning robotics / shared robot experience / collective robot learning | LWD、RoboOS |
| 22 | 主动感知 | active perception robot agent / VLM active perception manipulation | AgenticLab 等 |
| 23 | Verifier / 成功验证 | robot verifier agent / semantic verification robotics / precondition postcondition VLM | Harness VLA、PhyAgentOS、REMAC |

溯源：AgenticLab = arXiv 2602.01662（v1 题为 PLanAR）；MHS = Anthropic Model Hardware Standard 研究预览（2026-08-27）；OpenClawPi = 松灵机器人（AgileX）OpenClaw 技能库；Harness Engineering = arXiv 2606.09416《Harness Engineering for Physical AI》；Runtime Governance = arXiv 2604.07833《Harnessing Embodied Agents: Runtime Governance for Policy-Constrained Execution》。
