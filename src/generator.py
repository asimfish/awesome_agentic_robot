# -*- coding: utf-8 -*-
"""Generate README.md from data/papers.csv, data/topics.csv and data/header.md (awesome-ml4co style)."""
import csv, datetime, html, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(ROOT, *p)

def slug(name):
    # mimic github-slugger: lowercase, drop punctuation, keep every space as one hyphen
    s = re.sub(r"[^a-z0-9 \-]", "", name.lower())
    return s.replace(" ", "-")

def main():
    topics = list(csv.DictReader(open(D("data", "topics.csv"), encoding="utf-8")))
    papers = list(csv.DictReader(open(D("data", "papers.csv"), encoding="utf-8")))
    topics.sort(key=lambda t: int(t["order"]))
    header = open(D("data", "header.md"), encoding="utf-8").read()
    header = header.replace("{N_PAPERS}", str(len(papers))).replace("{N_TOPICS}", str(len(topics))).replace("{DATE}", datetime.date.today().isoformat())
    out = [header, "", "## [Content](#content)", "", "<table>"]
    # content table, two columns per row like awesome-ml4co
    cells = []
    for t in topics:
        label = f"{t['order']}. {t['name_en']} ({t['name_zh']})" if t["name_zh"] != t["name_en"] else f"{t['order']}. {t['name_en']}"
        cells.append(f"\t<td>&emsp;<a href=#{slug(t['name_en'])}>{html.escape(label)}</a></td>")
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
        out.append(f"### [{t['name_en']}](#content)")
        out.append("")
        out.append(f"*{t['name_zh']}* &nbsp;|&nbsp; keywords: `{t['keywords']}` &nbsp;|&nbsp; representative: {t['representative']}")
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
    out += ["## Statistics", ""]
    tiers = {}
    for p in papers: tiers[p["tier"]] = tiers.get(p["tier"], 0) + 1
    years = {}
    for p in papers: years[p["year"]] = years.get(p["year"], 0) + 1
    out.append(f"- {len(papers)} entries: {tiers.get('core',0)} core (⭐), {tiers.get('extended',0)} extended, {tiers.get('foundation',0)} foundation.")
    out.append("- By year: " + ", ".join(f"{y}: {years[y]}" for y in sorted(years)) + ".")
    out.append("- Topic coverage: " + ", ".join(f"{t['name_en']} ({len(by_topic[t['topic_id']])})" for t in topics) + ".")
    out += ["", "## Citation", "", "```bibtex", "@misc{awesome_agentic_robot_2026,", "  title  = {Awesome Agentic Robot: Agent + Robot Papers, Reports and Slides},", "  author = {asimfish},", "  year   = {2026},", "  url    = {https://github.com/asimfish/awesome_agentic_robot}", "}", "```", ""]
    open(D("README.md"), "w", encoding="utf-8").write("\n".join(out))
    print(f"README.md written: {len(papers)} papers, {len(topics)} topics")

if __name__ == "__main__":
    main()
