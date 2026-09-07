# 《RoboCurve：GPT-6 Astra 直接控制机器人》转写

- 作者：罗清雨（知乎专栏「知行合一」）
- 链接：https://zhuanlan.zhihu.com/p/208031326825455257 （访问日期 2026-09-08；页面对脚本抓取超时，以下为用户提供的正文）
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

GPT-6 经常能够做到：identify ✓、approach ✓、grasp ✓、move above target ✓、precise insertion ✗。也就是说：语义与规划很强，但精密接触仍然弱。

## 但这反而可能预示一种很强的架构

这两天 Twitter 上机器人圈最兴奋的一句话是："给这个东西接一个 flow head 会怎样？"意思是把现在的 GPT-6 → 离散 EEF waypoint → IK，换成：

GPT-6（Semantic / Reasoning）→ latent action intention → Flow / Diffusion Action Head → 30~100 Hz Action → Robot ←（tactile / vision）

GPT-6 负责：task reasoning、object grounding、spatial reasoning、long-horizon planning、error recovery、new instruction understanding。Action head 负责：precise trajectory、contact、force、insertion、grasp refinement、高频 control。这实际上非常接近 System 2 VLM + System 1 VLA。

## 作者认为这次 demo 真正重要的地方

不是"GPT-6 已经超过 π0.5，可以直接做机器人了"——远远没有。而是它说明了一件以前未必那么明显的事情：General Multimodal Intelligence 可能已经强到可以承担机器人 VLA 中非常大一部分高层能力。剩下最明显的瓶颈越来越集中在精密接触控制。未来架构很可能不是单纯把 VLA 越做越大，而是 GPT-6 负责"知道为什么、下一步要干什么"，低层 VLA 负责"这 500 ms 到底怎么动"。

Ego 数据最有价值的部分可能越来越偏向前半段——任务理解、affordance、skill composition、状态变化预测；而精准 motor policy 再用 robot data / sim / RL 补上。
