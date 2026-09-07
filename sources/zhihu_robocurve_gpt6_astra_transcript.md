# 《RoboCurve：GPT-6 Astra 直接控制机器人》转写

- 作者：罗清雨（知乎专栏「知行合一」）
- 链接：https://zhuanlan.zhihu.com/p/208031326825455257 · 编辑于 2026-09-07 15:24 · 离线保存 2026-09-08（用户提供的完整离线版：正文、3 张表格、1 张信息图、1 段 14 秒演示视频；本转写据此校对）
- 关系：RoboCurve 第三方测试的解读文章；同一测试也被具身纪元《GPT-6 未必能当好机器人的大脑，却可能帮王兴兴加速 RobotRSI》引用（见 `wechat_embodied_era_robot_rsi_transcript.md`）。版权归原作者。

---

## 新路线

RoboCurve 自己也把它描述为让 GPT-6 Astra 在同一个 agent policy 下直接控制 YAM arms；模型根据视觉和机器人状态做决策，再调用机器人动作接口。

| | π0.5 传统 VLA | GPT-6 Astra 这个 demo |
|---|---|---|
| 输入 | 图像 + 语言 + robot state | 图像 + 语言 + robot state |
| 高层理解 | VLA 内部 | GPT-6 |
| Action 输出 | 学习出来的 action chunk | EEF waypoint / tool call |
| 轨迹细节 | learned action head | IK + controller |
| 高频控制 | VLA/action head | 机器人底层 controller |
| 机器人数据训练 action head | 需要 | GPT-6 本身不需要这个 benchmark 的 BC 训练 |
| 是否是经典 VLA | ✅ | 严格说不是 |

关键点：它严格来说不是 π0.5 / GR00T 那种传统 end-to-end VLA。更准确地说，是 GPT-6 Astra 作为高层视觉-动作 Agent，直接看相机 + proprioception，然后输出 Cartesian EEF tool call；底层 IK + robot controller 执行动作。这反而是这次 demo 最值得研究的地方。

## Benchmark 结果为什么突然让机器人圈兴奋

最简单的 block → bowl：

| Model | Success | 时间 |
|---|---|---|
| Fable 5 | 1/20 = 5% | 8.2 min |
| Fable 5.1 | 8/20 = 40% | 6.8 min |
| GPT-6 Astra | 19/20 = 95% | 2.5 min |

GPT-6 平均只输出 2.1K tokens / run，而 Fable 5.1 为 12.9K。所以不仅成功率提升，reasoning loop 也短很多。

## 但是 precision manipulation 一下就暴露问题

更难的：抓圆形 puzzle piece → 插入精确圆槽。

| Model | Success |
|---|---|
| Fable 5 | 0% |
| Fable 5.1 | 10% |
| GPT-6 Astra | 10% |

GPT-6 经常能够做到：identify ✓、approach ✓、grasp ✓、move above target ✓、precise insertion ✗。也就是说：semantic reasoning 很强，但 precision contact control 仍然弱。

## 但这反而可能预示一种很强的架构

这两天 Twitter 上机器人圈最兴奋的一句话是："给这个东西接一个 flow head 会怎样？"意思是把现在的 GPT-6 → 离散 EEF waypoint → IK，换成：

GPT-6（Semantic / Reasoning）→ latent action intention → Flow / Diffusion Action Head → 30~100 Hz Action → Robot ←（tactile / vision）

GPT-6 负责：task reasoning、object grounding、spatial reasoning、long-horizon planning、error recovery、new instruction understanding。Action head 负责：precise trajectory、contact、force、insertion、grasp refinement、高频 control。这实际上非常接近 System 2 VLM + System 1 VLA。

## 作者认为这次 demo 真正重要的地方

不是"GPT-6 已经超过 π0.5，可以直接做机器人了"——远远没有。而是它说明了一件以前未必那么明显的事情：General Multimodal Intelligence 可能已经强到可以承担机器人 VLA 中非常大一部分高层能力。剩下最明显的瓶颈越来越集中在 high-frequency motor control + contact + dexterity。未来架构很可能不是单纯 VLA → 越来越大，而是 GPT-6 负责"知道为什么、下一步要干什么"，低层 VLA 负责"这 500 ms 到底怎么动"。

Ego 数据最有价值的部分可能越来越偏向前半段——任务理解、affordance、skill composition、状态变化预测；而精准 motor policy 再用 robot data / sim / RL 补上。

## 配图与视频（离线版附件）

**信息图**（`assets/zhihu_robocurve/infographic.jpg`）标题为"GPT-6 Astra 机器人演示：这里面是不是没有 VLA？"，结论："严格来说这不是经典端到端 VLA，而是多模态大模型 Agent + 机器人工具链"。三栏对比：

1. 传统 VLA（π0.5 / GR00T 风格）：图像 + 指令 + 机器人状态 → VLA 主干 → 学习的动作头 → 20-50 Hz action chunk → 机器人；语义理解与低层控制一体化学习，需要大量机器人动作数据。
2. GPT-6 Astra 当前演示（Multimodal Robot Agent）：Top Cam + Wrist Cam L + Wrist Cam R + Robot State + Language → GPT-6 Astra → `move_to(...)` Tool Call → EEF Waypoint → IK / Controller → 机器人；循环为 Observe → Reason → Move → Replan（闭环反馈、重新规划）。高层能力：视觉理解、规划、空间推理、失败恢复；输出不是 learned joint action，而是 waypoint + 工具调用；底层执行依赖 IK、轨迹插值、控制器；强项：开放指令、闭环纠错、长程任务组织；短板：精细插入、毫米级操作。关键判断：VLA 的"LA"被拆到了工具链里。
3. 更可能的下一代形态：GPT-like System 2 + VLA / Flow Head System 1——大模型负责任务理解、规划、组合技能；动作头负责接触、轨迹、精细控制；20-100 Hz 稠密动作。

底部对比表：谁负责高层语义（VLA 内部 / GPT-6 / GPT-like Planner）、谁负责低层动作（Learned Action Head / IK-Controller / VLA-Flow Head）、是否经典 VLA（是 / 严格说不是 / 部分是）、最强能力（精细操作 / 泛化与纠错 / 兼顾）、更像什么（End-to-end policy / Agent + tools / System 2 + System 1）。核心结论："这次火的不是 VLA 已经被取代，而是通用多模态模型开始接管机器人高层闭环控制；真正仍待突破的部分主要集中在高频动作、接触控制与精细 manipulation。"

**演示视频**（14.3 秒，1280×720，30 fps；帧拼图见 `assets/zhihu_robocurve/demo_frames.jpg`，图表放大见 `assets/zhihu_robocurve/robocurve_cost_chart.jpg`）：左半为 RoboCurve 的图表"GPT-6 Astra is 2.4× better and 2.3× cheaper than Fable 5.1 on direct robot control"——横轴每次运行的 API 成本（$1-$4），纵轴完成率；GPT-6 Astra 约 95% 完成率、每次约 1 美元，Fable 5.1 40%、约 2.3 美元，Fable 5 5%、约 2.7 美元；标注"2.4× success rate, 2.3× cheaper"（GPT-6 对 Fable 5.1）与"8× success rate, 1.3× cheaper"（Fable 5.1 对 Fable 5）；每次运行以单点标在 0% 或 100%（二元结果）。右半为 GPT-6 Astra 与 Fable 5.1 的并排真机画面：顶部相机与腕部相机视角，YAM 机械臂抓取红色方块放入碗中，成功时标注 SUCCESS。
