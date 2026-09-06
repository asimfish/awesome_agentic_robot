# -*- coding: utf-8 -*-
"""Run the SuperTranslate engine with a lookup translator (manual translations, identity fallback).

usage: <super_translate>/.venv/bin/python manual_translate.py INPUT.pdf OUTPUT_zh.pdf --dict zh/a.py [--dict zh/b.py ...] [--record segments.jsonl]

Each --dict file defines a Python dict `E` mapping exact English segment text -> Chinese translation
(and/or `T` mapping export block index -> translation, resolved against --blocks export.jsonl).
Every segment the engine requests is recorded, so the dictionaries can be extended offline and
the document re-rendered deterministically without any API key.
"""
import argparse, json, os, re, sys
# Location of a checkout of https://github.com/asimfish/super_translate (override with SUPER_TRANSLATE_HOME).
_ST = os.environ.get("SUPER_TRANSLATE_HOME", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "super_translate"))
sys.path.insert(0, _ST)
from pdf_zh_translator import cli, translators

PH = re.compile(r"\u27e6\d+\u27e7")
LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl", "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"', "\u00ad": ""}
def norm(t):
    for k, v in LIG.items(): t = t.replace(k, v)
    return re.sub(r"\s+", " ", t).strip()

class LookupTranslator(translators.Translator):
    def __init__(self, table, record_path):
        self.table, self.record_path, self.hits, self.misses = table, record_path, 0, 0
        self.fh = open(record_path, "w", encoding="utf-8") if record_path else None
    def translate_batch(self, texts):
        out = []
        for t in texts:
            tr = self.table.get(norm(t), t)
            if sorted(PH.findall(t)) != sorted(PH.findall(tr)):
                print("placeholder mismatch, keeping source:", t[:70], file=sys.stderr); tr = t
            self.hits += tr != t; self.misses += tr == t
            if self.fh: self.fh.write(json.dumps({"source": t, "translation": tr, "translated": tr != t}, ensure_ascii=False) + "\n")
            out.append(tr)
        return out

def main():
    p = argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("output")
    p.add_argument("--dict", action="append", default=[]); p.add_argument("--blocks"); p.add_argument("--record")
    a, rest = p.parse_known_args()
    table = {}
    blocks = [json.loads(l) for l in open(a.blocks, encoding="utf-8")] if a.blocks else []
    for d in a.dict:
        ns = {}; exec(open(d, encoding="utf-8").read(), ns)
        for k, v in ns.get("E", {}).items(): table[norm(k)] = v
        for i, v in ns.get("T", {}).items():
            if i < len(blocks): table[norm(blocks[i]["source"])] = v
    lt = LookupTranslator(table, a.record)
    translators.build_translator_from_args = lambda args: lt
    cli.build_translator_from_args = lambda args: lt
    rc = cli.main(["translate", a.input, a.output, "--api-mode", "cache-only", "--cache-file", "/tmp/_unused_cache.jsonl", "--preserve-graphics-text"] + rest)
    if lt.fh: lt.fh.close()
    print(f"segments translated={lt.hits} kept_english={lt.misses}")
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
