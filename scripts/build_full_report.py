# -*- coding: utf-8 -*-
"""Build report/survey_full_report.html and .pdf: cover -> two-level TOC -> overview figures ->
Part 0 (executive summary: insights/10-12) -> Part 1 (readings of the five source materials: report_zh chapters 1-6)
-> Parts A-G (43 notes grouped like README / Fig.2), each part opened by a divider page.
Requires pandoc (gfm -> html with MathML) and Playwright/Chromium for the PDF."""
import asyncio, pathlib, re, subprocess, datetime

REPO = pathlib.Path(__file__).resolve().parent.parent
N = lambda name: REPO / "notes" / name
OUT_HTML = REPO / "report" / "survey_full_report.html"
OUT_PDF = REPO / "report" / "survey_full_report.pdf"

PARTS = [
 ("0", "执行摘要：趋势、洞察、研究机会与口径账本",
  "一页结论 · 六大趋势 · 十条洞察 · 八条可证伪预测 · 19 个研究机会（各配最小可行实验）· 头条数字的口径账本——全部结论先行，细节见后续各章。",
  [REPO/"insights/10_trends_insights_zh.md", REPO/"insights/11_open_problems_zh.md", REPO/"insights/12_numbers_ledger_zh.md"]),
 ("1", "五份源材料的解读与 25 条主线综述",
  "小红书长文《Harness 之后，Agent+Robot 下一站是什么？》· Code-as-Policy 讲稿 · 23 条主线检索地图 · Lil'Log 两篇 · 具身纪元《GPT-6 … 加速 RobotRSI》及其小红书图文版；随后是 25 条主线的逐线综述。",
  ["REPORT_ZH"]),
 ("A", "主线：Coding Agent 与自进化",
  "从 Code as Policies 到 CaP-X、RHO、ASPIRE、SkillOpt、ENPIRE，以及 7-9 月的自进化续作、自动研究谱系与技能库谱系。优化对象沿阶梯上移：策略代码 → 技能文档 → 技能库 → 训练配方 → 运行时 → 整套 harness。",
  [N("01_code_as_policies_zh.md"), N("02_capx_zh.md"), N("03_rho_zh.md"), N("04_aspire_zh.md"), N("05_skillopt_zh.md"), N("06_enpire_zh.md"),
   N("07_self_evolution_successors_zh.md"), N("08_autoresearch_lineage_zh.md"), N("09_skill_library_lineage_zh.md")]),
 ("B", "记忆、反思与验证",
  "RoboMME 的两个结论、PonderPounce / AGM / HyMeS / BATON 四种记忆路线、权重内记忆合评、反思与纠错、PRIMO R1 与 VERITAS 两类验证器、验证器谱系。",
  [N("10_robomme_zh.md"), N("11_ponderpounce_zh.md"), N("12_agm_zh.md"), N("13_hymes_zh.md"), N("14_baton_zh.md"), N("15_in_weight_memory_zh.md"),
   N("16_reflection_correction_zh.md"), N("17_primo_r1_zh.md"), N("18_veritas_zh.md"), N("19_verifier_lineage_zh.md")]),
 ("C", "Harness、Runtime、双系统与端侧",
  "Harness VLA（全文解读）及其规则记忆如何接到 agent 数据引擎上、PhyAgentOS、Thea、Harness Engineering for Physical AI、其他 harness 框架、治理与运行时、快慢双系统、端侧部署。Harness 从软件名词变成实时系统问题。",
  [N("20_harness_vla_zh.md"), N("45_harness_vla_rules_for_data_engine_zh.md"), N("21_phyagentos_zh.md"), N("22_thea_zh.md"), N("23_harness_engineering_physical_ai_zh.md"), N("24_harness_frameworks_zh.md"),
   N("25_runtime_governance_zh.md"), N("26_dual_systems_zh.md"), N("27_edge_deployment_zh.md")]),
 ("D", "学习闭环：RL、数据回流、数字孪生与世界模型",
  "LWD 的 16 台机器人、Q-Planning 的小 Q 函数、TwinRL 与数字孪生谱系、RoboClaw 的自复位、VLA + RL 的信用分配、世界模型的角色，以及把前沿 VLM agent 做成数据引擎的方案（RoboCurve GPT-6 Astra 演示解读）。",
  [N("28_lwd_zh.md"), N("29_q_planning_zh.md"), N("30_twinrl_digital_twin_zh.md"), N("31_roboclaw_zh.md"), N("32_vla_rl_credit_zh.md"), N("33_world_model_roles_zh.md"), N("44_gpt6_astra_data_engine_zh.md")]),
 ("E", "总览、接口、多机器人与跨本体",
  "AgenticLab 的规划语言接口、Agent + Robot 总览、ROSClaw 与 MHS 的接口层、多机器人协作、生命周期与主动感知。",
  [N("34_agenticlab_zh.md"), N("35_agent_robot_overview_zh.md"), N("36_rosclaw_mhs_interfaces_zh.md"), N("37_multi_robot_zh.md"), N("38_lifecycle_active_perception_zh.md")]),
 ("F", "安全与治理",
  "护栏模型、形式化、世界模型与部署视角四类安全工作；攻击面已覆盖指令、通信、模型、元数据、接触五个层面。",
  [N("39_safety_zh.md")]),
 ("G", "基础：LLM Agent、Harness 工程与 RSI",
  "Lil'Log 两篇、软件侧 RSI 谱系（四个环节）、harness 演化方法（优化阶梯的完整实例集）、AI 研发基准与失败模式。",
  [N("40_lilianweng_posts_zh.md"), N("41_rsi_lineage_zh.md"), N("42_harness_evolution_methods_zh.md"), N("43_ai_research_benchmarks_zh.md")]),
 ("H", "我们的方案：HARVEST 自举式数据引擎",
  "以前沿多模态 Agent 为遥操作员、以规则记忆为脚手架、以独立验证器为准入、以三级补齐覆盖接触段、以训好的动作头交回 Agent 形成自举课程。含系统架构、数据格式、规则生命周期、12 周计划、五条可证伪假设、基线与指标、风险与新颖性声明。",
  [REPO/"docs/proposal/PROPOSAL_agent_data_engine_zh.md"]),
]
all_files = [f for _, _, _, fs in PARTS for f in fs if f != "REPORT_ZH"]
note_files = [f for f in all_files if f.parent.name == "notes"]
missing = [f for f in all_files if not f.exists()]; assert not missing, missing
notes_all = sorted((REPO / "notes").glob("*.md")); uncovered = [f.name for f in notes_all if f not in note_files]; assert not uncovered, uncovered

CSS = """
@page{size:A4;margin:22mm 18mm 20mm 18mm}
@page fig1{size:A3 landscape;margin:12mm}
body{font-family:"PingFang SC","Hiragino Sans GB","Songti SC",sans-serif;color:#1a2332;line-height:1.75;font-size:10.5pt;margin:0}
h1{font-size:17pt;color:#1F3A5F;border-bottom:2.5px solid #0173B2;padding-bottom:8px;margin:0 0 14px;line-height:1.4;page-break-before:always}
h1.first{page-break-before:avoid}
h2{font-size:13pt;color:#0173B2;margin:20px 0 8px}
h3{font-size:11pt;color:#1a2332;margin:14px 0 6px}
h4{font-size:10.5pt;color:#1F3A5F;margin:12px 0 4px}
blockquote{border-left:3px solid #0173B2;background:#f0f6fa;padding:8px 14px;margin:10px 0;color:#41586b;font-size:9.5pt}
blockquote p{margin:2px 0}
table{border-collapse:collapse;width:100%;font-size:8.8pt;margin:10px 0;page-break-inside:auto}
tr{page-break-inside:avoid}
th{background:#1F3A5F;color:#fff;padding:5px 7px;text-align:left;font-weight:600}
td{border:1px solid #cdd9e1;padding:4.5px 7px;vertical-align:top}
tr:nth-child(even) td{background:#f4f8fa}
code{background:#eef2f5;padding:1px 5px;border-radius:3px;font-size:9pt;font-family:Menlo,monospace}
pre{background:#eef2f5;padding:10px 12px;border-radius:6px;font-size:8.8pt;overflow:hidden;white-space:pre-wrap}
strong{color:#1F3A5F} li{margin-bottom:3px} p{margin:6px 0}
hr{border:none;border-top:1px solid #dde5ea;margin:16px 0}
a{color:#0173B2;text-decoration:none}
math{font-size:10.5pt}
.cover{page-break-after:always;padding-top:150px}
.cover .k{font-size:11pt;letter-spacing:.25em;color:#0173B2;font-weight:600;margin-bottom:22px}
.cover .t1{font-size:26pt;font-weight:700;color:#1F3A5F;line-height:1.35;margin-bottom:14px}
.cover .t2{font-size:13pt;color:#41586b;margin-bottom:40px;line-height:1.7}
.cover .meta{font-size:10.5pt;color:#6b7f8f;line-height:2.1}
.toc{page-break-after:always}
.toc h1{page-break-before:avoid}
.toc .part{font-size:11.5pt;font-weight:700;color:#1F3A5F;margin:12px 0 2px}
.toc ol{font-size:10.5pt;line-height:1.9;color:#1a2332;padding-left:1.6em;margin:0}
.figpage1{page:fig1;page-break-before:always;page-break-after:always}
.figpage2{page-break-before:always;page-break-after:always}
.figpage1 svg{height:250mm;width:auto;max-width:100%;display:block;margin:0 auto}
.figpage2 svg{width:100%;height:auto;max-height:250mm}
.figcap{font-size:9.5pt;color:#41586b;margin-top:6px}
.divider{page-break-before:always;page-break-after:always;padding-top:190px}
.divider .k{font-size:12pt;letter-spacing:.3em;color:#0173B2;font-weight:600;margin-bottom:14px}
.divider .t{font-size:24pt;font-weight:700;color:#1F3A5F;line-height:1.35;margin-bottom:18px}
.divider .d{font-size:11.5pt;color:#41586b;line-height:1.8;max-width:150mm}
.divider ol{font-size:10.5pt;color:#1a2332;line-height:1.9;margin-top:22px;padding-left:1.6em}
"""

def md2html(text):
    r = subprocess.run(["pandoc", "-f", "gfm+tex_math_dollars", "-t", "html", "--mathml"], input=text, capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stderr)
    return r.stdout

def title_of(text):
    return text.splitlines()[0].lstrip("# ").strip()

def report_zh_sections():
    t = (REPO / "docs/reports/report_zh.md").read_text(encoding="utf-8")
    t = t.split("\n---\n", 2)[-1] if t.startswith("---") else t          # drop YAML front matter
    t = t[: t.index("\n# 7. 趋势与洞见")]                                  # chapters 导读..6 only (7-9 are covered by Part 0)
    chapters = [c for c in re.split(r"(?m)^(?=# )", t) if c.strip()]
    return chapters

def svg(path):
    s = (REPO / path).read_text(encoding="utf-8")
    return re.sub(r'<svg xmlns="http://www.w3.org/2000/svg" width="\d+" height="\d+"', '<svg xmlns="http://www.w3.org/2000/svg"', s, count=1)

def build_html():
    n_notes = len(notes_all)
    today = datetime.date.today().isoformat()
    body = []
    body.append(f'''<div class="cover"><div class="k">AWESOME AGENTIC ROBOT · 全文报告</div>
<div class="t1">Agent × Robot：从 Harness 到自进化物理智能体</div>
<div class="t2">五份源材料的解读 · 25 条主线综述 · 六大趋势与十条洞察 · 19 个研究机会 · 数字口径账本 · {n_notes} 份深度解读合订 · HARVEST 方案</div>
<div class="meta">仓库：github.com/asimfish/awesome_agentic_robot<br>维护：asimfish · 生成日期：{today}<br>本报告由 scripts/build_full_report.py 从 insights/、docs/reports/report_zh.md 与 notes/ 自动合订；引用请注明仓库与解读编号。</div></div>''')
    # TOC
    toc = ['<div class="toc"><h1 class="first">目录</h1>']
    sections = []  # (part_key, title, html)
    for key, title, desc, files in PARTS:
        items = []
        if files == ["REPORT_ZH"]:
            for ch in report_zh_sections():
                items.append((title_of(ch), md2html(ch)))
        else:
            for f in files:
                txt = f.read_text(encoding="utf-8")
                items.append((title_of(txt), md2html(txt)))
        sections.append((key, title, desc, items))
        toc.append(f'<div class="part">Part {key} · {title}</div><ol>' + "".join(f"<li>{t}</li>" for t, _ in items) + "</ol>")
    toc.append("</div>")
    body.extend(toc)
    body.append(f'<div class="figpage1">{svg("assets/fig1_timeline.svg")}<div class="figcap">图 1 · Agent × Robot 论文时间线（2022-2026）：按七个 Part 分泳道、按发表年月定位，★ 为源材料点名的核心工作，橙色竖带为 2026 年 6-8 月。</div></div>')
    body.append(f'<div class="figpage2">{svg("assets/fig2_taxonomy.svg")}<div class="figcap">图 2 · 分类体系：七个 Part、25 条主线，括号内为条目数——与 README 与本报告的 Part A-G 一一对应。</div></div>')
    for key, title, desc, items in sections:
        body.append(f'<div class="divider"><div class="k">PART {key}</div><div class="t">{title}</div><div class="d">{desc}</div><ol>' + "".join(f"<li>{t}</li>" for t, _ in items) + "</ol></div>")
        for _, h in items:
            body.append(h)
    html = f'<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>Agent × Robot 全文报告 · awesome_agentic_robot</title><style>{CSS}</style></head><body>' + "\n".join(body) + "</body></html>"
    OUT_HTML.parent.mkdir(exist_ok=True)
    OUT_HTML.write_text(html, encoding="utf-8")
    return html

async def to_pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        page = await b.new_page()
        await page.goto(OUT_HTML.as_uri())
        await page.wait_for_timeout(800)
        await page.pdf(path=str(OUT_PDF), prefer_css_page_size=True, print_background=True, display_header_footer=True,
                       header_template='<div></div>',
                       footer_template='<div style="font-size:8px;color:#6b7f8f;width:100%;text-align:center;font-family:sans-serif">awesome_agentic_robot · Agent × Robot 全文报告 · <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
                       margin={"top": "22mm", "bottom": "20mm", "left": "18mm", "right": "18mm"})
        await b.close()

if __name__ == "__main__":
    build_html()
    asyncio.run(to_pdf())
    import fitz
    print("html:", OUT_HTML, OUT_HTML.stat().st_size, "bytes | pdf pages:", fitz.open(str(OUT_PDF)).page_count)
