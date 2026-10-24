#!/usr/bin/env python3
"""Worte im Bild auflisten (Stichwortband, Namensschilder, Sprechblasen) für die sprachliche Prüfung.

    python3 scripts/authoring/bildworte.py [PRÄFIX …]        # z. B. RUT MAT-005; ohne Präfix alle Aufträge mit Worten

Ausgabe je Bildauftrag und Feld: Versbereich, Band, Blasen und Worte der Strukturbilder je Sprache (de, gsw). Regeln: BILDAUFTRAEGE-ANLEITUNG.md,
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
            dg = q.get("diagram")
            if dg:  # Strukturbild: Titel, Köpfe, Zellen und Beschriftungen
                def cell(name, c):
                    for k in ("role", "a", "b"):
                        if c.get(k):
                            parts.append((f"{name} {k}", lab(c[k])))
                if dg.get("title"):
                    parts.append(("Titel", lab(dg["title"])))
                for i, h in enumerate(dg.get("head") or []):
                    parts.append((f"Kopf {i + 1}", lab(h)))
                for k in ("yes_label", "no_label", "top_label", "bottom_label", "verdict", "there", "back"):
                    if dg.get(k):
                        parts.append((k, lab(dg[k])))
                for i, lk in enumerate(dg.get("links") or []):
                    if lk:
                        parts.append((f"Pfeil {i + 1}", lab(lk)))
                for key in ("cells", "left", "right", "top", "bottom", "core"):
                    for i, c in enumerate(dg.get(key) or []):
                        cell(f"{key} {i + 1}", c)
                for i, r in enumerate(dg.get("rows") or []):
                    for j, c in enumerate(r):
                        cell(f"Zeile {i + 1}.{j + 1}", c)
                for k in ("cond", "yes", "no", "ring"):
                    if dg.get(k):
                        cell(k, dg[k])
                for i, t in enumerate(dg.get("turns") or []):
                    cell(f"Rede {i + 1} {t.get('who', '')[4:]}", t.get("cell") or {})
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
