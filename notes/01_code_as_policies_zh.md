# 01 · Code as Policies 深度解读：让 LLM 写的程序成为机器人策略

> **Code as Policies: Language Model Programs for Embodied Control**
> arXiv 2209.07753（2022-09）· Robotics at Google · Jacky Liang, Wenlong Huang, Fei Xia et al.（共 8 位作者） · 项目页 code-as-policies.github.io
> 所属主线：T2 · 材料来源：讲稿第 3-9 页；本仓库有正文全译 `papers/pdf_zh/2209.07753_zh.pdf`

## 1. 一句话定位

Code as Policies（CaP）把"机器人策略"重新定义为 LLM 写出的一段程序：程序处理感知模块的输出（例如开放词汇目标检测器给出的物体位置）、调用控制原语 API 并给参数赋值，还能表达反馈循环。它是本仓库 T2 主线的起点，也是 2026 年 CaP-X、RHO、ASPIRE、ENPIRE 全部工作的共同祖先。

## 2. 要解决的问题

2022 年之前，把自然语言接到机器人有两条路：端到端学习语言条件策略（需要大量数据，且难以泛化到新指令），或者用 LLM 做高层规划、把步骤映射到预定义技能（技能集固定，无法表达"把苹果往左移一点"这类需要空间推理和参数化的指令）。CaP 的判断是：LLM 在代码补全上的能力可以直接复用——代码天然具备组合性、能调用第三方库（NumPy、Shapely）做空间几何推理，也能表达条件与循环。

## 3. 方法

核心概念是语言模型程序（Language Model Programs, LMP）：给 LLM 少量"指令 → 代码"示例（few-shot prompt），让它为新指令生成 Python 代码；代码里可以调用感知 API（如 `detect_objects`）、控制 API（如 `pick_place`、`set_velocity`）、第三方库，以及**尚未定义的函数**——分层代码生成（hierarchical code generation）让 LLM 递归地为未定义函数生成实现。论文区分了反应式策略（例如"看到橙子就后退"的 while 循环）与航点式策略，并展示 LMP 可以组合：一个 LMP 解析指令、另一个解析物体名、另一个解析航点。

## 4. 实验结果与口径

- **HumanEval**：分层代码生成把通用代码生成基准的 P@1 提到 39.8%（当时的 state of the art）。这是软件侧指标，不是机器人指标。
- **仿真桌面任务**（UR5e + 积木/碗，50 次试验/任务）：按属性与指令"已见/未见"划分四格。属性与指令均已见时 CaP 与 CLIPort 相当；属性或指令未见时 CLIPort 掉到接近 0，CaP 保持 62-80%（长程 SA-UI 80.0%、空间几何 UA-UI 62.0%）。口径：二元成功率，仿真，成功由脚本判定。
- **真机**：移动机器人导航与操作、桌面抓放；论文主要以定性示例展示，未给出与仿真同规模的统计。

## 5. 局限

1. CaP 优化的是程序接口层：它假设感知 API 与控制原语已经存在且可靠，本身不学习连续控制器（讲稿第 9 页的提醒）。接触密集的任务（插入、倒水）超出它的表达范围。
2. 论文自己列出的三条边界：感知 API 描述范围有限、可用原语有限、依赖 few-shot 示例的质量；对多轮交互与部署时的实时性没有讨论。
3. "未见指令仍有 62-80%"的口径是仿真、脚本判定、属性组合有限，不能与 2026 年 LIBERO-Pro 这类扰动基准直接比较。

## 6. 关系定位

CaP 之后这条线分成三叉：测试时生成（CaP-X 的 CaP-Agent0、MALMM、Neuro-Symbolic CaP，见 notes/02）、训练时搜索（RHO 的多文件策略仓库，notes/03；MEMENTO 的演化搜索）、研究自动化（ENPIRE，notes/06；HARBOR、Nautilus，notes/08）。讲稿把这条演化压成公式 $z_{t+1} = A(z_t, \tau_t, r_t, \log_t)$：CaP 是 $z$ = 一段策略代码、$A$ = 单次 few-shot 生成、没有 $r$ 与 $\log$ 回流的起点。ENPIRE 的 RoboCasa365 实验（代码做 hover pose、VLA 做接触阶段）给了 CaP 与 VLA 分工的实证答案：代码管几何确定的阶段。

## 7. 延伸批判

CaP 的成功率与"原语抽象层级"强相关，而这一点直到 CaP-X（2026）才被系统量化：把人工设计的高层原语撤掉后，同一批模型的成功率随之下降。因此 2022 年 CaP 的数字应当理解为"在设计者提供的脚手架上 LLM 能做到什么"，而不是 LLM 对机器人控制的裸能力。另一个未走之路是安全：LLM 生成的代码直接驱动真机，论文没有讨论执行前验证与权限边界，这个空缺由 2026 年的 ROSClaw 安全包络与 Runtime Governance 填补（notes/25、36）。
