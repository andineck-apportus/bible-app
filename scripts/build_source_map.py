#!/usr/bin/env python3
"""Quellenkarte aus dem Quellenkatalog (source-Datensätze mit `catalog` in data/sources/) erzeugen.

Aufruf: python3 scripts/build_source_map.py
Ausgabe: app/quellenkarte/index.html (eigenständige Seite) und build/quellenkarte/artifact.html (ohne Dokumentrahmen,
für die Veröffentlichung als Claude-Artefakt). Gleiche Daten nutzt die App (Blatt «Quellen und Rechte»).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ORDER = {"free": 0, "sa": 1, "nc": 2, "ask": 3, "prot": 4}


def catalog():
    out = []
    for p in sorted((ROOT / "data/sources").glob("*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        c = r.get("catalog")
        if not c:
            continue
        out.append({"id": r["id"], "title": r.get("title", r["id"]), "url": r.get("url", ""), "area": c["area"],
                    "layer": c["layer"], "rights": c["rights"], "license": c["license"], "use": c["use"],
                    "why": c["why_de"], "checked": c.get("checked", "")})
    out.sort(key=lambda s: (ORDER[s["rights"]], s["use"] != "used", s["title"]))
    return out


def main():
    cat = catalog()
    date = max(s["checked"] for s in cat)
    d = ".".join(reversed(date.split("-")))
    page = (ROOT / "app/quellenkarte/template.html").read_text(encoding="utf-8")
    page = page.replace("/*CATALOG*/", json.dumps(cat, ensure_ascii=False)).replace("__DATE__", d)
    full = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n' + page + "\n</body>\n</html>\n")
    (ROOT / "app/quellenkarte/index.html").write_text(full, encoding="utf-8")
    out = ROOT / "build/quellenkarte"
    out.mkdir(parents=True, exist_ok=True)
    (out / "artifact.html").write_text(page, encoding="utf-8")
    used = sum(s["use"] == "used" for s in cat)
    print(f"PASS: Quellenkarte mit {len(cat)} Quellen ({used} verwendet) -> app/quellenkarte/index.html")


if __name__ == "__main__":
    main()
