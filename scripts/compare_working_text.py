#!/usr/bin/env python3
"""Vergleicht die Arbeitstranskription (text_sample) Wort für Wort mit den importierten SBLGNT-Tokens.

Ausgabe: reports/compare-TEXT-MRK-003-029-030-WORKING-vs-SBLGNT.json
Vergleich auf Wortebene ohne Interpunktion und textkritische Zeichen; Unicode NFC.
Ein Unterschied ist ein Befund über die Arbeitstranskription, keine textkritische Aussage.
"""
import difflib
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data/text-samples/TEXT-MRK-003-029-030-WORKING.json"
TOKENS = ROOT / "data/tokens/SBLGNT-MRK-003-022-030.json"
OUT = ROOT / "reports/compare-TEXT-MRK-003-029-030-WORKING-vs-SBLGNT.json"


def words(text):
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"[⸀-⸅,.·;:!?«»“”]", "", text)
    return text.split()


sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
tokset = json.loads(TOKENS.read_text(encoding="utf-8"))
result = {}
for ref, text in sample["text_by_reference"].items():
    a = words(text)
    b = [unicodedata.normalize("NFC", t["word"]) for t in tokset["tokens"] if t["reference"] == ref]
    diffs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op != "equal":
            diffs.append({"op": op, "working": a[i1:i2], "sblgnt": b[j1:j2], "working_position": i1 + 1})
    result[ref] = {"working_words": len(a), "sblgnt_tokens": len(b), "identical": not diffs, "differences": diffs}

OUT.write_text(json.dumps({
    "compares": sample["id"],
    "with": tokset["id"],
    "source_sha256": tokset["source"]["sha256"],
    "method": "Wortvergleich ohne Interpunktion und textkritische Zeichen, Unicode NFC",
    "results": result,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
for ref, r in result.items():
    print(ref, "identisch" if r["identical"] else r["differences"])
