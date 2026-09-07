# -*- coding: utf-8 -*-
"""Overview figures for awesome_agentic_robot (light + dark SVG variants under assets/).
Fig.1  Swimlane timeline: seven parts x 2022-2026, one labelled pill per work, star = named by the source materials.
Fig.2  Taxonomy tree: Agent x Robot -> seven parts -> 25 topic lines with entry counts and representative works.
Data for Fig.1 is hand-curated below (short names, month resolution); Fig.2 counts come from data/papers.csv."""
import csv, pathlib
from xml.sax.saxutils import escape as E

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "assets"; OUT.mkdir(exist_ok=True)

# family key -> (label, colour)
FAM = {
 "A": ("主线：Coding Agent 与自进化", "#0e7490"),
 "B": ("记忆 · 反思 · 验证", "#7c3aed"),
 "C": ("Harness · Runtime · 双系统 · 端侧", "#d97706"),
 "D": ("学习闭环：RL · 数据回流 · 孪生 · 世界模型", "#059669"),
 "E": ("总览 · 接口 · 多机 · 跨本体", "#2563eb"),
 "F": ("安全与治理", "#dc2626"),
 "G": ("基础：LLM Agent · Harness 工程 · RSI", "#475569"),
}
LANES = ["A", "B", "C", "D", "E", "F", "G"]

# (label, year, month, family, star)
WORKS = [
 ("CoT", 2022, 1, "G", 0), ("ReAct", 2022, 10, "G", 0), ("Code as Policies", 2022, 9, "A", 1), ("STaR", 2022, 3, "G", 0),
 ("Reflexion", 2023, 3, "G", 0), ("Toolformer", 2023, 2, "G", 0), ("Generative Agents", 2023, 4, "G", 0), ("Lil'Log Agents", 2023, 6, "G", 0),
 ("Let's Verify", 2023, 5, "G", 0), ("RoCo", 2023, 7, "E", 1), ("RT-2", 2023, 7, "E", 0), ("STOP", 2023, 10, "G", 0), ("Eureka", 2023, 10, "A", 1),
 ("Self-Rewarding", 2024, 1, "G", 0), ("Agentic Skill Discovery", 2024, 5, "A", 1), ("DrEureka", 2024, 6, "A", 1), ("Meta-Rewarding", 2024, 7, "G", 0),
 ("ADAS", 2024, 8, "G", 0), ("AI Scientist", 2024, 8, "G", 0), ("MALMM", 2024, 11, "E", 1),
 ("Atomic Skill Library", 2025, 1, "A", 1), ("REMAC", 2025, 3, "B", 1), ("RoboOS", 2025, 5, "E", 1), ("OneTwoVLA", 2025, 5, "C", 1),
 ("Agentic Robot", 2025, 5, "E", 1), ("DGM", 2025, 5, "G", 0), ("Fast-in-Slow", 2025, 6, "C", 1), ("RationalVLA", 2025, 6, "C", 1),
 ("AlphaEvolve", 2025, 6, "G", 0), ("Growing w/ Embodied Agent", 2025, 9, "A", 1), ("ViReSkill", 2025, 9, "A", 1), ("SAC Flow", 2025, 9, "D", 1),
 ("ShinkaEvolve", 2025, 9, "G", 0), ("ACE", 2025, 10, "G", 0), ("ManiAgent", 2025, 10, "E", 1), ("RoboOS-NeXT", 2025, 10, "E", 1),
 ("Neuro-Symbolic CaP", 2025, 10, "A", 0), ("Arcadia", 2025, 11, "D", 1),
 ("LaST0", 2026, 1, "C", 1), ("TT-VLA", 2026, 1, "D", 1), ("Why LLMs Aren't Scientists", 2026, 1, "G", 0),
 ("StreamVLA", 2026, 2, "C", 1), ("AgenticLab", 2026, 2, "E", 1), ("TwinRL", 2026, 2, "D", 1), ("H-WM", 2026, 2, "D", 1), ("AgentRob", 2026, 2, "E", 1),
 ("RoboMME", 2026, 3, "B", 1), ("RoboClaw", 2026, 3, "D", 1), ("PRIMO R1", 2026, 3, "B", 1), ("CaP-X", 2026, 3, "A", 1), ("ROSClaw", 2026, 3, "E", 1),
 ("Meta-Harness", 2026, 3, "G", 0), ("ROSClaw (hetero)", 2026, 4, "E", 1), ("Runtime Governance", 2026, 4, "F", 1), ("EmbodiedGovBench", 2026, 4, "F", 0),
 ("OpenClawPi", 2026, 4, "E", 1), ("AHE", 2026, 4, "G", 0),
 ("LWD", 2026, 5, "D", 1), ("SkillOpt", 2026, 5, "A", 1), ("HiSME", 2026, 5, "G", 0), ("Harness≠Benefit", 2026, 5, "G", 0), ("VASO", 2026, 6, "F", 0),
 ("HE for Physical AI", 2026, 6, "C", 1), ("RHO", 2026, 6, "A", 1), ("VERITAS", 2026, 6, "B", 1), ("ENPIRE", 2026, 6, "A", 1), ("RoboMME-Interf.", 2026, 6, "B", 1),
 ("ASPIRE", 2026, 6, "A", 1), ("Self-Harness", 2026, 6, "G", 0), ("Guava", 2026, 6, "C", 0), ("HARBOR", 2026, 6, "A", 0),
 ("Harness VLA", 2026, 7, "C", 1), ("PhyAgentOS", 2026, 7, "C", 1), ("Lil'Log Harness", 2026, 7, "G", 0), ("RoboHarness", 2026, 7, "C", 0), ("Q-Planning", 2026, 7, "D", 0),
 ("Zetta", 2026, 8, "A", 0), ("SHAPER", 2026, 8, "A", 0), ("PRACTICE", 2026, 8, "A", 0), ("PonderPounce", 2026, 8, "B", 1), ("AGM", 2026, 8, "B", 0),
 ("BATON", 2026, 8, "B", 0), ("HyMeS", 2026, 8, "B", 0), ("NativeMEM", 2026, 8, "B", 0), ("Thea", 2026, 8, "C", 0), ("PhyAI", 2026, 8, "C", 0),
 ("EMBGuard", 2026, 8, "F", 0), ("Same Weights ≠ Same Robot", 2026, 8, "F", 0), ("MHS", 2026, 8, "E", 1), ("LLM-as-a-Verifier", 2026, 8, "B", 0),
 ("Temporal GRPO", 2026, 8, "D", 0), ("RoboSnap", 2026, 8, "D", 0), ("Motus2", 2026, 8, "D", 0), ("具身纪元 Robot RSI", 2026, 9, "G", 0),
]

# Fig.2: part -> [(topic_id, ...)] ; representative names per line
PARTS = [
 ("A", ["T2", "T7", "T8", "T24"]), ("B", ["T4", "T5", "T6", "T23"]), ("C", ["T13", "T14", "T15", "T16"]),
 ("D", ["T9", "T10", "T11", "T12"]), ("E", ["T1", "T3", "T18", "T19", "T20", "T21", "T22"]), ("F", ["T17"]), ("G", ["T0"]),
]
REPS = {
 "T0": "Lil'Log · ReAct · Reflexion · STOP · DGM", "T1": "AgenticLab · Agentic Robot · ManiAgent", "T2": "Code as Policies · CaP-X · RHO · ENPIRE",
 "T3": "ROSClaw · OpenClawPi · AgentRob", "T4": "RoboClaw · BATON · H-WM", "T5": "RoboMME · PonderPounce · AGM · NativeMEM",
 "T6": "REMAC · PhysReflect-VLA · PRIMO R1", "T7": "ASPIRE · PhyAgentOS · Arcadia · Zetta", "T8": "Agentic Skill Discovery · ViReSkill · RATs",
 "T9": "TwinRL · LWD · Temporal GRPO · TEMPO", "T10": "LWD · RoboClaw · Q-Planning", "T11": "TwinRL · RoboSnap · PerceptTwin",
 "T12": "H-WM · Motus2 · ContactGuard", "T13": "Fast-in-Slow · StreamVLA · LaST0", "T14": "HE for Physical AI · PhyAI · CloudEdgeVLA",
 "T15": "RHO · Harness VLA · Thea · Guava", "T16": "PhyAgentOS · Runtime Governance · FSAR", "T17": "EMBGuard · VASO · Same Weights",
 "T18": "MHS · ROSClaw · MCP servers", "T19": "RoCo · REMAC · RoboOS-NeXT", "T20": "RoboOS · ASPIRE · Harness VLA",
 "T21": "LWD · ENPIRE · RoboOS", "T22": "PhysCaP · ActiveVLA", "T23": "PhyAgentOS · Thea · LLM-as-a-Verifier", "T24": "ENPIRE · PRIMO R1 · VERITAS · Eureka",
}

def load_topics():
    topics = {t["topic_id"]: t for t in csv.DictReader(open(REPO / "data" / "topics.csv", encoding="utf-8"))}
    counts = {k: 0 for k in topics}
    for p in csv.DictReader(open(REPO / "data" / "papers.csv", encoding="utf-8")):
        for tid in p["topics"].split(";"):
            if tid.strip() in counts: counts[tid.strip()] += 1
    return topics, counts

def theme(dark):
    return dict(bg="#0f172a" if dark else "#ffffff", fg="#e2e8f0" if dark else "#1e293b", muted="#94a3b8" if dark else "#64748b",
                grid="#1e293b" if dark else "#e2e8f0", pill_fg="#ffffff", lane_bg=("#111c33", "#0f172a") if dark else ("#f8fafc", "#ffffff"))

def text_w(s, size):
    # rough width estimate: CJK ~1em, latin ~0.55em
    return sum(size * (1.0 if ord(c) > 0x2E80 else 0.56) for c in s)

def fig1(dark=False):
    T = theme(dark)
    W, LEFT, RIGHT, TOP = 1900, 300, 40, 90
    x0, x1 = 2022.0, 2026.85
    def X(y, m): return LEFT + (y + (m - 0.5) / 12 - x0) / (x1 - x0) * (W - LEFT - RIGHT)
    size, ph, gap = 13, 22, 4
    lanes = {k: [] for k in LANES}
    for lab, y, m, fam, star in sorted(WORKS, key=lambda w: (w[1], w[2])):
        lanes[fam].append((lab, y, m, star))
    # place pills into rows per lane, avoiding horizontal overlap
    placed, lane_rows = {}, {}
    for k in LANES:
        rows_end = []
        for lab, y, m, star in lanes[k]:
            w = text_w(("★ " if star else "") + lab, size) + 16
            x = X(y, m) - w / 2
            r = 0
            while r < len(rows_end) and rows_end[r] > x - 6: r += 1
            if r == len(rows_end): rows_end.append(0)
            rows_end[r] = x + w
            placed.setdefault(k, []).append((lab, star, x, w, r))
        lane_rows[k] = max(1, len(rows_end))
    H = TOP + sum(lane_rows[k] * (ph + gap) + 26 for k in LANES) + 70
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="PingFang SC, Helvetica Neue, Arial, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="{T["bg"]}"/>',
         f'<text x="{LEFT}" y="34" font-size="22" font-weight="700" fill="{T["fg"]}">图 1 · Agent × Robot 论文时间线（2022-2026）</text>',
         f'<text x="{LEFT}" y="58" font-size="13" fill="{T["muted"]}">按七个 Part 分泳道、按发表年月定位；★ = 被源材料点名的核心工作。2022 年前的基础文献（Good 1965、Gödel Machine 2003、Yudkowsky 2008、WebGPT 2021 等）未画出。</text>']
    # year grid
    for y in range(2022, 2027):
        xx = X(y, 0.5) - (X(2022, 1.5) - X(2022, 0.5)) / 2
        o.append(f'<line x1="{xx:.1f}" y1="{TOP-10}" x2="{xx:.1f}" y2="{H-40}" stroke="{T["grid"]}" stroke-width="1"/>')
        o.append(f'<text x="{xx+6:.1f}" y="{TOP-16}" font-size="13" fill="{T["muted"]}">{y}</text>')
    # highlight 2026-06..08
    xa, xb = X(2026, 0.5), X(2026, 8.5)
    o.append(f'<rect x="{xa:.1f}" y="{TOP-10}" width="{xb-xa:.1f}" height="{H-TOP-30}" fill="#f59e0b" opacity="{0.10 if dark else 0.08}"/>')
    o.append(f'<text x="{xa+4:.1f}" y="{H-22}" font-size="12" fill="#d97706">2026 年 6-8 月：Harness / 记忆 / 自进化论文密度最高的季度</text>')
    yy = TOP
    for i, k in enumerate(LANES):
        lab, col = FAM[k]
        lane_h = lane_rows[k] * (ph + gap) + 26
        o.append(f'<rect x="0" y="{yy}" width="{W}" height="{lane_h}" fill="{T["lane_bg"][i%2]}" opacity="0.9"/>')
        o.append(f'<rect x="0" y="{yy}" width="8" height="{lane_h}" fill="{col}"/>')
        o.append(f'<text x="20" y="{yy+22}" font-size="14" font-weight="700" fill="{col}">Part {k}</text>')
        o.append(f'<text x="20" y="{yy+42}" font-size="12" fill="{T["muted"]}">{E(lab)}</text>')
        for plab, star, x, w, r in placed[k]:
            py = yy + 13 + r * (ph + gap)
            o.append(f'<rect x="{x:.1f}" y="{py}" width="{w:.1f}" height="{ph}" rx="11" fill="{col}" opacity="{1.0 if star else 0.72}"/>')
            o.append(f'<text x="{x+w/2:.1f}" y="{py+ph/2+4.5}" font-size="{size}" text-anchor="middle" fill="{T["pill_fg"]}" font-weight="{700 if star else 400}">{E(("★ " if star else "") + plab)}</text>')
        yy += lane_h
    o.append("</svg>")
    return "\n".join(o)

def fig2(dark=False):
    T = theme(dark)
    topics, counts = load_topics()
    W = 1500
    row_h, leaf_gap = 52, 8
    n_leaves = sum(len(ls) for _, ls in PARTS)
    H = 110 + n_leaves * row_h + (len(PARTS) - 1) * 14 + 40
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="PingFang SC, Helvetica Neue, Arial, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="{T["bg"]}"/>',
         f'<text x="40" y="36" font-size="22" font-weight="700" fill="{T["fg"]}">图 2 · Agent × Robot 分类体系：七个 Part、25 条主线</text>',
         f'<text x="40" y="60" font-size="13" fill="{T["muted"]}">括号内为该主线的条目数（一篇论文可属多条主线）；右侧为代表工作。与 README 的 25 条主线、合订本的 Part A-G 一一对应。</text>']
    root_x, part_x, leaf_x = 60, 330, 640
    y = 100
    leaf_positions = []
    part_centres = []
    for key, lines in PARTS:
        lab, col = FAM[key]
        y_start = y
        for tid in lines:
            t = topics[tid]
            name = t["name_zh"] if t["name_zh"] == t["name_en"] else f"{t['name_zh']}（{t['name_en']}）"
            o.append(f'<rect x="{leaf_x}" y="{y}" width="{W-leaf_x-40}" height="{row_h-leaf_gap}" rx="8" fill="{col}" opacity="{0.14 if dark else 0.09}" stroke="{col}" stroke-width="1"/>')
            o.append(f'<text x="{leaf_x+14}" y="{y+19}" font-size="14" font-weight="700" fill="{T["fg"]}">{E(tid)} {E(name)} <tspan fill="{col}">({counts[tid]})</tspan></text>')
            o.append(f'<text x="{leaf_x+14}" y="{y+37}" font-size="12" fill="{T["muted"]}">{E(REPS.get(tid, ""))}</text>')
            leaf_positions.append((y + (row_h - leaf_gap) / 2, col))
            y += row_h
        y_end = y - leaf_gap
        cy = (y_start + y_end) / 2
        part_centres.append(cy)
        o.append(f'<rect x="{part_x}" y="{cy-24}" width="270" height="48" rx="10" fill="{col}"/>')
        o.append(f'<text x="{part_x+12}" y="{cy-4}" font-size="14" font-weight="700" fill="#fff">Part {key}</text>')
        o.append(f'<text x="{part_x+12}" y="{cy+15}" font-size="12" fill="#fff">{E(lab)}</text>')
        for ly, _ in leaf_positions[-len(lines):]:
            o.append(f'<path d="M {part_x+270} {cy} C {part_x+300} {cy}, {leaf_x-30} {ly}, {leaf_x} {ly}" stroke="{col}" stroke-width="1.6" fill="none" opacity="0.8"/>')
        y += 14
    rc = (part_centres[0] + part_centres[-1]) / 2
    o.append(f'<rect x="{root_x}" y="{rc-30}" width="220" height="60" rx="12" fill="{T["fg"]}"/>')
    o.append(f'<text x="{root_x+110}" y="{rc-4}" font-size="16" font-weight="700" text-anchor="middle" fill="{T["bg"]}">Agent × Robot</text>')
    o.append(f'<text x="{root_x+110}" y="{rc+16}" font-size="12" text-anchor="middle" fill="{T["bg"]}">{sum(1 for _ in csv.DictReader(open(REPO/"data"/"papers.csv", encoding="utf-8")))} 篇 · 25 条主线</text>')
    for cy, (key, _) in zip(part_centres, PARTS):
        o.append(f'<path d="M {root_x+220} {rc} C {root_x+260} {rc}, {part_x-40} {cy}, {part_x} {cy}" stroke="{FAM[key][1]}" stroke-width="2" fill="none" opacity="0.85"/>')
    o.append("</svg>")
    return "\n".join(o)

if __name__ == "__main__":
    (OUT / "fig1_timeline.svg").write_text(fig1(False), encoding="utf-8")
    (OUT / "fig1_timeline_dark.svg").write_text(fig1(True), encoding="utf-8")
    (OUT / "fig2_taxonomy.svg").write_text(fig2(False), encoding="utf-8")
    (OUT / "fig2_taxonomy_dark.svg").write_text(fig2(True), encoding="utf-8")
    print("figures written:", sorted(p.name for p in OUT.glob("fig*.svg")))
