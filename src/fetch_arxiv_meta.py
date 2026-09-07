"""Fetch arXiv metadata (title, authors, dates, abstract, categories) for every paper id and save data/paper_meta.json.
Seed ids are listed below; ids found in data/papers.csv are added automatically. Respects the arXiv API rate limit."""
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, time, json, sys, re, os, csv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "paper_meta.json")
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
ids = """
2209.07753 2605.23904 2603.22435 2606.19980 2607.00272
2602.01662 2505.23450 2510.11660 2606.16458 2603.26997 2604.04664 2602.13591 2603.11558 2602.11291 2503.22122
2603.04639 2606.22338 2608.24115 2509.24219 2512.00076 2607.16636 2509.18597 2405.15019 2501.15068
2602.09023 2605.00416 2509.25756 2601.06748 2506.01953 2505.11917 2602.01100 2601.05248 2506.10826
2606.09416 2607.08448 2604.07833 2307.04738 2505.03673 2510.26536 2411.17636 2607.03451
2606.08610 2608.18227 2606.19419 2607.22832 2608.21031 2510.21302 2607.26991 2602.18813 2511.21510
2602.13081 2604.01708 2608.16590 2608.11350 2608.09857 2608.11246 2606.18363 2607.15524
2608.30760 2609.02217 2608.29537 2608.26545 2608.16889 2608.15269 2608.09410 2608.08749 2608.05970 2607.18060 2607.07608 2607.06678 2606.29774 2604.15671
2608.07555 2607.23784 2605.11665 2606.31200 2606.27146 2603.04029 2602.16444
2606.05395 2607.05377 2606.23565 2509.24524 2510.12985 2604.11174 2606.03724 2605.28097 2605.30924
2608.13026 2608.07314 2607.29613 2606.31846 2606.29892 2607.16506 2608.21204 2608.23831
2607.06699 2606.30268 2606.18646 2607.19190 2608.30237 2608.13438 2606.20698
2607.04927 2606.22794 2605.02739 2604.24921 2505.03912 2410.08001
2608.15502 2608.03682 2608.00569 2606.29350 2605.30011
2606.14882 2603.08814 2601.20577 2605.12920 2608.06830 2604.11028
2601.08325 2601.08454 2607.05391 2606.30686 2606.04226
2609.01679 2608.09898 2603.21726 2604.14399 2607.12220 2511.03497 2606.07723 2603.09513 2602.09430
""".split()
csv_path = os.path.join(ROOT, "data", "papers.csv")
if os.path.exists(csv_path):
    ids += [r["id"] for r in csv.DictReader(open(csv_path, encoding="utf-8")) if re.match(r"^\d{4}\.\d{4,5}$", r["id"])]
builder = os.path.join(ROOT, "src", "build_papers_csv.py")
if os.path.exists(builder):
    ids += re.findall(r'^"(\d{4}\.\d{4,5})": \(', open(builder, encoding="utf-8").read(), flags=re.M)
ids = list(dict.fromkeys(ids))
print("total ids", len(ids))
out = {}
for i in range(0, len(ids), 20):
    chunk = ids[i:i+20]
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(chunk), "max_results": 50})
    for attempt in range(3):
        try:
            data = urllib.request.urlopen(url, timeout=90).read(); break
        except Exception as ex:
            print("retry", ex); time.sleep(5)
    root = ET.fromstring(data)
    for e in root.findall("a:entry", NS):
        aid_full = e.find("a:id", NS).text.split("/abs/")[-1]
        aid = re.sub(r"v\d+$", "", aid_full)
        title = " ".join(e.find("a:title", NS).text.split())
        if title.lower().startswith("error"): continue
        out[aid] = {
            "id": aid, "id_version": aid_full,
            "title": title,
            "authors": [a.find("a:name", NS).text for a in e.findall("a:author", NS)],
            "published": e.find("a:published", NS).text[:10],
            "updated": e.find("a:updated", NS).text[:10],
            "abstract": " ".join(e.find("a:summary", NS).text.split()),
            "categories": [c.get("term") for c in e.findall("a:category", NS)],
            "comment": (e.find("arxiv:comment", NS).text if e.find("arxiv:comment", NS) is not None else ""),
            "journal_ref": (e.find("arxiv:journal_ref", NS).text if e.find("arxiv:journal_ref", NS) is not None else ""),
        }
    print(f"chunk {i//20+1}: got {len(out)} so far"); sys.stdout.flush()
    time.sleep(3.5)
missing = [x for x in ids if x not in out]
print("missing:", missing)
json.dump(out, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("saved", len(out))
