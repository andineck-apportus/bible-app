#!/usr/bin/env python3
"""Blindtest ohne Legende (BILDPROZESS.md, Schritt 5): Testpaket für eine Reihe von Bildern.

    python3 scripts/authoring/bildtest_paket.py AUSGABE RUT-004-001-012 TIT-001 …

Legt an:
- AUSGABE/bilder/Bild NN.png (Hochdeutsch) und AUSGABE/bilder/fragen.json – nur das, was die Testperson sehen darf:
  Ebene, Buch und vier Kandidaten derselben Ebene (Stelle mit Titel), keine Legende, kein Auftrag;
- AUSGABE/schluessel.json – richtige Antwort, Kernanalyse (Kernaussage, Momente, Sprecher, Textart) für die Bewertung.

Kandidaten: Abschnitt → andere Abschnitte desselben Kapitels (sonst Nachbarkapitel); Kapitel → andere Kapitel desselben
Buches; Buch → andere Bücher mit Bild; Merkvers → andere Merkverse desselben Kapitels. Reihenfolge fest gemischt (Seed 11).
"""
import json
import pathlib
import random
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

D = ROOT / "data"
BRIEFS = {p.stem[6:]: json.loads(p.read_text(encoding="utf-8")) for p in (D / "illustrations/briefs").glob("BRIEF-*.json")}


BOOK_DE = {"RUT": "Rut", "JON": "Jona", "OBA": "Obadja", "MAT": "Matthäus", "MRK": "Markus", "LUK": "Lukas", "JHN": "Johannes",
           "PHP": "Philipper", "TIT": "Titus", "1JN": "1. Johannesbrief", "2JN": "2. Johannesbrief", "3JN": "3. Johannesbrief"}
_VERSES = {}


def verse_de(ref):
    """Vers der hochdeutschen Arbeitsübersetzung."""
    if not _VERSES:
        for p in (D / "translations").glob("TRANS-*-DE-WORKING.json"):
            _VERSES.update(json.loads(p.read_text(encoding="utf-8")).get("text_by_reference") or {})
    return _VERSES.get(ref, "")


def title(target):
    for sub in ("text-units", "summaries"):
        p = D / sub / f"{target}.json"
        if p.exists():
            r = json.loads(p.read_text(encoding="utf-8"))
            return r.get("title") or r.get("title_de") or ""
    return ""


def label(suffix):
    b = BRIEFS[suffix]
    ref = b.get("reference") or suffix
    try:
        shown = refs.display_de(ref)
    except Exception:  # noqa: BLE001
        shown = ref
    lvl = b["level"]
    if lvl == "chapter":  # Kapitel: Titel der Abschnitte, damit die Kandidaten unterscheidbar sind
        secs = [s for s, x in BRIEFS.items() if x["level"] == "section" and s.startswith(suffix + "-")]
        return f"{shown}: " + "; ".join(title(BRIEFS[s]["target"]) for s in sorted(secs))
    if lvl == "book":  # voller Buchname (Abkürzungen sind ohne Vorwissen nicht lesbar)
        return BOOK_DE.get(suffix, shown)
    if lvl == "verse":  # Merkvers: die App zeigt die Karte neben dem Vers; Kandidaten mit Verswortlaut (gekürzt)
        txt = verse_de(ref)
        return f"{shown}: {txt[:110]}{'…' if len(txt) > 110 else ''}"
    t = title(b["target"]) if lvl == "section" else ""
    return f"{shown} {t}".strip()


def candidates(suffix):
    b = BRIEFS[suffix]
    lvl = b["level"]
    parts = suffix.split("-")
    if lvl == "section":
        pool = [s for s, x in BRIEFS.items() if x["level"] == "section" and s.startswith("-".join(parts[:2]) + "-") and s != suffix]
        if len(pool) < 3:
            pool += [s for s, x in BRIEFS.items() if x["level"] == "section" and s.startswith(parts[0] + "-") and s not in pool and s != suffix]
    elif lvl == "chapter":
        pool = [s for s, x in BRIEFS.items() if x["level"] == "chapter" and s.startswith(parts[0] + "-") and s != suffix]
    elif lvl == "verse":
        pool = [s for s, x in BRIEFS.items() if x["level"] == "verse" and s.startswith("-".join(parts[:2]) + "-") and s != suffix]
    else:
        pool = [s for s, x in BRIEFS.items() if x["level"] == "book" and s != suffix]
    rnd = random.Random(f"11-{suffix}")
    pool = sorted(pool)
    rnd.shuffle(pool)
    c = pool[:3] + [suffix]
    rnd.shuffle(c)
    return c


def main():
    out = pathlib.Path(sys.argv[1]).resolve()
    keys = [k.replace("BRIEF-", "") for k in sys.argv[2:]]
    tmp = out / "_render"
    subprocess.run([sys.executable, str(ROOT / "scripts/authoring/vorschau_bild.py"), str(tmp), *keys], check=True)
    (out / "bilder").mkdir(parents=True, exist_ok=True)
    fragen, key = [], {}
    for i, k in enumerate(keys, 1):
        nr = f"{i:02d}"
        shutil.copy(tmp / f"{k}.png", out / "bilder" / f"Bild {nr}.png")
        cands = candidates(k)
        letters = "ABCD"
        fragen.append({"bild": f"Bild {nr}.png", "ebene": {"section": "Abschnitt", "chapter": "Kapitel", "book": "Buch", "verse": "Merkvers"}[BRIEFS[k]["level"]],
                       "buch": refs.display_de(k.split("-")[0]) if BRIEFS[k]["level"] != "book" else "(Bibel)",
                       "kandidaten": {letters[j]: label(c) for j, c in enumerate(cands)}})
        core = D / "core-analyses" / f"CORE-{k}.json"
        ca = json.loads(core.read_text(encoding="utf-8")) if core.exists() else {}
        key[nr] = {"suffix": k, "richtig": letters[cands.index(k)], "kern": ca.get("core_de"), "textart": ca.get("mode"),
                   "sprecher": ca.get("voice"), "momente": [m.get("text_de") for m in ca.get("moments", [])]}
    (out / "bilder" / "fragen.json").write_text(json.dumps(fragen, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "schluessel.json").write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf-8")
    shutil.rmtree(tmp)
    print(f"PASS: {len(keys)} Bilder im Testpaket {out}")


if __name__ == "__main__":
    main()
