# 22 · Thea 深度解读：物理世界不白送的两样东西——读状态、判结果

> **Towards the Harness of Embodied Agents**（Thea）
> arXiv 2608.11246（2026-08-03）· Qi Wang, Tianyi Wang, Chengyang Li et al.（共 9 位作者）
> 所属主线：T15、T23 · 材料来源：报告第 4 章 T15/T23、第 5.3 节

## 1. 一句话定位

Thea 直接把 coding agent 的 harness 范式搬到机器人：一个 agentic 循环编排机器人能力，每个能力包装成可调用的工具，继承 coding agent harness 的核心组件并按物理世界的要求修改。它的洞见是：物理世界拒绝提供软件白送的两种能力——读取世界状态与判断动作结果——于是引入 **Scene Graph as Context**（持久的符号化世界表示）和 **Evaluation as Exit Codes**（检测动作何时应终止、判断是否成功、失败时诊断原因）。

## 2. 要解决的问题

coding agent 的成功确立了一个范式：agent 的成就取决于模型周围的基础设施而不只是模型。这个范式能否延伸到具身 agent？软件 harness 依赖两个廉价前提：状态可读（文件、变量、日志）与结果可判（编译、测试的退出码）。机器人两者都没有——相机不是文件系统，动作没有退出码。

## 3. 方法

- **Scene Graph as Context**：用持久的符号化场景图充当"文件系统"——物体、关系、状态可被 agent 读取、引用与更新，是 agent 上下文的一部分而不是每步重新感知。
- **Evaluation as Exit Codes**：给每个动作一个类似退出码的评估——何时该终止（动作完成或卡住）、是否成功、失败原因诊断——让 agentic 循环能像处理编译错误一样处理物理失败。
- 其余组件（工具调用、上下文管理、记忆）继承 coding agent harness 并做物理修改。

## 4. 实验结果与口径

- 摘要定位为框架论文，未给单一头条数字；评测范围与任务需看正文。
- 口径：系统层贡献；与 Guava（notes/24）同属"什么构成有效的具身 harness"的探索，与 PhyAgentOS（notes/21）同属 harness 系统化。

## 5. 局限

1. 场景图的构建本身依赖感知模型；场景图错误会以"可读状态"的形式被 agent 信任——这是把感知不确定性藏进符号表示的经典风险。
2. Exit codes 的诊断粒度决定 harness 的有效性；接触失效（抓滑、插不到底）如何被编码为退出码，摘要未说明。
3. 没有时间维度：Harness Engineering for Physical AI（notes/23）指出物理 harness 必须处理延迟与调度，Thea 的两个补丁不涉及这一点。

## 6. 关系定位

报告第 5.3 节把机器人 harness 与软件 harness 的本质差异概括为三点——读状态难、判结果难、有时间——前两点来自 Thea，第三点来自 Harness Engineering for Physical AI。Thea 的 Evaluation as Exit Codes 与 PhyAgentOS 的 SessionVerifier、AGM 的证据门控进度指针、ENPIRE 的验证工具是 T23 主线上四种"把'成没成'做成显式接口"的方式。Scene Graph as Context 与 Analytic Concept-Centric Memory（notes/15）在"结构化符号世界表示"上同向。

## 7. 延伸批判

"退出码"是一个极好的比喻，也是一个危险的比喻：编译器的退出码是确定的，物理动作的"退出码"是一个概率判断。Thea 把这个判断做成接口，却没有说明接口背后的判断器有多准——这正是 PRIMO R1（67%）与 LLM-as-a-Verifier（87.4%）报告的那类数字。一个自然的扩展是让 exit code 带置信度与证据（AGM 式的物理证据、Consilience 式的置信度轨迹），让 agentic 循环能对低置信退出码选择复核而不是直接相信。另一个未走之路：场景图作为持久上下文，天然是多机器人共享世界知识（T19/T21 的空缺层）的候选载体。
