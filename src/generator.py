# -*- coding: utf-8 -*-
"""Generate README.md from data/papers.csv, data/topics.csv and data/header.md (awesome-ml4co style)."""
import csv, datetime, html, os, re, sys, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(ROOT, *p)

def slug(name):
    # mimic GitHub's heading anchors (html-pipeline): lowercase, drop anything that is not a word
    # character / space / hyphen (CJK is kept), then turn every space into one hyphen
    s = re.sub(r"[^\w\s-]", "", name.lower())
    return s.replace(" ", "-")

def notes_index_table():
    """Table of the deep-dive notes grouped by the same parts as report/ (PARTS defined in scripts/build_full_report.py)."""
    spec = importlib.util.spec_from_file_location("bfr", D("scripts", "build_full_report.py"))
    bfr = importlib.util.module_from_spec(spec); spec.loader.exec_module(bfr)
    rows, n = ["| Part | 编号 · 解读 | 一句话 |", "|---|---|---|"], 0
    for key, title, _desc, files in bfr.PARTS:
        if key in ("0", "1"): continue
        for i, f in enumerate(files):
            first = f.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
            num, _, rest = first.partition(" · ")
            name, _, sub = rest.partition("：")
            label = f"**{key}** · {title}" if i == 0 else f"{key}"
            rows.append(f"| {label} | [{num} · {name}](notes/{f.name}) | {sub} |"); n += 1
    return "\n".join(rows), n

def full_report_pages():
    try:
        import fitz
        return fitz.open(D("report", "survey_full_report.pdf")).page_count
    except Exception:
        return "—"

def heading(t):
    return t["name_zh"] if t["name_zh"] == t["name_en"] else f"{t['name_zh']} | {t['name_en']}"

def main():
    topics = list(csv.DictReader(open(D("data", "topics.csv"), encoding="utf-8")))
    papers = list(csv.DictReader(open(D("data", "papers.csv"), encoding="utf-8")))
    topics.sort(key=lambda t: int(t["order"]))
    header = open(D("data", "header.md"), encoding="utf-8").read()
    notes_index, n_notes = notes_index_table()
    n_full = full_report_pages()
    header = (header.replace("{N_PAPERS}", str(len(papers))).replace("{N_TOPICS}", str(len(topics))).replace("{DATE}", datetime.date.today().isoformat())
              .replace("{N_NOTES}", str(n_notes)).replace("{N_FULL_PAGES}", str(n_full)).replace("{NOTES_INDEX}", notes_index))
    footer = open(D("data", "footer.md"), encoding="utf-8").read()
    out = [header, "", "## 论文清单", "",
           f"共 {len(topics)} 条主线、{len(papers)} 篇论文，按主线分组、组内按时间排序。每条主线先给检索关键词与代表工作，再列条目；⭐ 为源材料点名的核心工作。点击主线标题可回到本目录。", "",
           "<table>"]
    # content table, two columns per row like awesome-ml4co
    cells = []
    for t in topics:
        label = f"{t['order']}. {t['name_zh']}（{t['name_en']}）" if t["name_zh"] != t["name_en"] else f"{t['order']}. {t['name_en']}"
        cells.append(f"\t<td>&emsp;<a href=\"#{slug(heading(t))}\">{html.escape(label)}</a></td>")
    for i in range(0, len(cells), 2):
        out.append("<tr>"); out.extend(cells[i:i+2]); out.append("</tr>")
    out += ["</table>", ""]
    by_topic = {t["topic_id"]: [] for t in topics}
    for p in papers:
        for tid in p["topics"].split(";"):
            tid = tid.strip()
            if tid in by_topic: by_topic[tid].append(p)
    for t in topics:
        rows = sorted(by_topic[t["topic_id"]], key=lambda p: p["date"])
        out.append(f"### [{heading(t)}](#论文清单)")
        out.append("")
        out.append(f"检索关键词：`{t['keywords']}`　代表工作：{t['representative']}　（{len(rows)} 篇）")
        out.append("")
        for i, p in enumerate(rows, 1):
            star = "⭐" if p["tier"] == "core" else ""
            links = f"[paper]({p['url']})"
            if p["code_url"]: links += f" [code]({p['code_url']})"
            out.append(f"{i}. **{star}{p['title']}.** {p['venue']}, {p['year']}. {links}")
            out.append("")
            out.append(f"    *{p['authors']}*")
            if p["note_zh"]:
                out.append("")
                out.append(f"    > {p['note_zh']}")
            out.append("")
    out += ["## 统计", ""]
    tiers = {}
    for p in papers: tiers[p["tier"]] = tiers.get(p["tier"], 0) + 1
    years = {}
    for p in papers: years[p["year"]] = years.get(p["year"], 0) + 1
    out.append(f"- 共 {len(papers)} 条：核心 ⭐ {tiers.get('core',0)}、扩展 {tiers.get('extended',0)}、基础 {tiers.get('foundation',0)}。")
    out.append("- 按年份：" + "、".join(f"{y} 年 {years[y]} 篇" for y in sorted(years)) + "。")
    out.append("- 按主线：" + "、".join(f"{t['name_zh']} {len(by_topic[t['topic_id']])}" for t in topics) + "。")
    out += ["", footer]
    open(D("README.md"), "w", encoding="utf-8").write("\n".join(out))
    print(f"README.md written: {len(papers)} papers, {len(topics)} topics")

if __name__ == "__main__":
    main()
