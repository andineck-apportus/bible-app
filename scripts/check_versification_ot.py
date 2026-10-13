#!/usr/bin/env python3
"""Prüft die Umrechnung hebräisch -> Navigationszählung (KJV) für Bücher des Alten Testaments.

Aufruf: python3 scripts/check_versification_ot.py --macula PFAD/macula-hebrew [BUCH …]
Liest WLC/lowfat/<NN>-<Buch>-*-lowfat.xml (holt fehlende Dateien mit git checkout und entfernt sie danach wieder),
rechnet mit scripts/versification.py um und vergleicht die Verszahlen je Kapitel mit der Navigation.
"""
import argparse, json, pathlib, re, subprocess, sys
import xml.etree.ElementTree as ET
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import versification  # noqa: E402
from ot_books import FILES  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--macula", type=pathlib.Path, required=True)
ap.add_argument("books", nargs="*")
a = ap.parse_args()
nav = {b["code"]: b["verses_per_chapter"] for b in json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text())["books"]}
fails = 0
for book in a.books or list(FILES):
    pat = f"WLC/lowfat/{FILES[book]}-"
    names = subprocess.run(["git", "-C", str(a.macula), "ls-tree", "--name-only", "HEAD", "WLC/lowfat/"], capture_output=True, text=True).stdout.split()
    names = [n for n in names if n.startswith(pat)]
    fetched = [n for n in names if not (a.macula / n).exists()]
    if fetched:
        subprocess.run(["git", "-C", str(a.macula), "checkout", "HEAD", "--", *fetched], check=True)
    verses = {}
    try:
        for n in names:
            for w in ET.parse(a.macula / n).iter("w"):
                m = re.fullmatch(r"\S+ (\d+):(\d+)!(\d+)", w.get("ref"))
                ref = f"{book}.{int(m[1])}.{int(m[2])}"
                ws = verses.setdefault(ref, {})
                ws[int(m[3])] = ws.get(int(m[3]), "") + (w.text or "")
    finally:
        for n in fetched:
            (a.macula / n).unlink()
    verses = {r: [ws[k] for k in sorted(ws)] for r, ws in verses.items()}
    plan, empty = versification.heb_to_kjv(book, verses)
    out = versification.apply(book, verses, plan)
    got = {}
    for r in out:
        _, c, v = r.split(".")
        got.setdefault(int(c), set()).add(int(v))
    for r in empty:
        _, c, v = r.split(".")
        got.setdefault(int(c), set()).add(int(v))
    want = {c + 1: set(range(1, n + 1)) for c, n in enumerate(nav[book])}
    ok = got == want
    changed = sum(1 for r, p in plan.items() if p[0][3] != "same" or len(p) > 1)
    if not ok:
        fails += 1
        diff = {c: (sorted(want.get(c, set()) - got.get(c, set()))[:5], sorted(got.get(c, set()) - want.get(c, set()))[:5]) for c in set(want) | set(got) if want.get(c) != got.get(c)}
        print(f"FAIL {book}: {dict(list(diff.items())[:4])}")
    else:
        print(f"ok   {book}: {len(verses)} hebräische Verse, {changed} umgerechnet" + (f", leer in WLC: {empty}" if empty else ""))
print("PASS" if not fails else f"FAIL: {fails} Bücher")
sys.exit(1 if fails else 0)
