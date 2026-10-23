#!/usr/bin/env python3
"""Worte im Bild auflisten (Stichwortband, Namensschilder, Sprechblasen) für die sprachliche Prüfung.

    python3 scripts/authoring/bildworte.py [PRÄFIX …]        # z. B. RUT MAT-005; ohne Präfix alle Aufträge mit Worten

Ausgabe je Bildauftrag und Feld: Versbereich, Band und Blasen je Sprache (de, gsw). Regeln: BILDAUFTRAEGE-ANLEITUNG.md,
Abschnitt «Worte im Bild».
"""
import json
import pathlib
import sys

D = pathlib.Path(__file__).resolve().parents[2] / "data/illustrations/briefs"


def lab(v):
    return v if isinstance(v, dict) else {"de": v, "gsw": v}


def main():
    pre = sys.argv[1:]
    for p in sorted(D.glob("BRIEF-*.json")):
        b = json.loads(p.read_text(encoding="utf-8"))
        suf = b["id"][6:]
        if pre and not any(suf == x or suf.startswith(x + "-") for x in pre):
            continue
        rows = []
        for q in b["panels"]:
            parts = []
            if q.get("keywords"):
                parts.append(("Band", lab(q["keywords"])))
            for sp in q.get("speech", []):
                if sp.get("word"):
                    parts.append((f"Blase {sp['from'][4:]} → {sp['to'][4:]}", lab(sp["word"])))
            if parts:
                rows.append((q["n"], q["reference"], parts))
        if rows:
            print(f"## {suf}")
            for n, ref, parts in rows:
                print(f"  Feld {n} ({ref})")
                for k, v in parts:
                    print(f"    {k}: de «{v.get('de', '')}» | gsw «{v.get('gsw', '')}»")


if __name__ == "__main__":
    main()
