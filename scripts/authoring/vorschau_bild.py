#!/usr/bin/env python3
"""Vorschau einzelner Bilder im Stil Anime direkt aus dem Bildauftrag (ohne Daten zu schreiben).

    python3 scripts/authoring/vorschau_bild.py AUSGABE RUT-004-001-012 TIT-001 …   [--lang gsw] [--px 760]

Zeichnet je Suffix das Bild mit dem aktuellen Stand von Bildauftrag (data/illustrations/briefs/BRIEF-<suffix>.json, also nach
`bildauftraege.py`), Figuren und Zeichen und legt AUSGABE/<suffix>.png an. Worte im Bild in der gewählten Sprache (Standard de).
"""
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts/authoring"))


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    out = pathlib.Path(args.pop(0)).resolve()
    out.mkdir(parents=True, exist_ok=True)
    lang, px, keys = "de", 760, []
    i = 0
    while i < len(args):
        if args[i] == "--lang":
            lang = args[i + 1]; i += 2; continue
        if args[i] == "--px":
            px = int(args[i + 1]); i += 2; continue
        keys.append(args[i].replace("BRIEF-", "")); i += 1
    import bilder_anime as A
    lib, vb = A.library()
    A._VB.update(vb)
    css = "<style>.lw{display:none}.lw-%s{display:inline}</style>" % lang
    names = []
    for k in keys:
        A.CUR[0] = k.lower()
        svg = A.auto_svg(k, vb).replace("<svg ", f'<svg width="{px}" ', 1)
        (out / f"{k}.html").write_text(f'<html><head><meta charset="utf-8">{css}</head><body style="margin:0;background:#fff">'
                                       f'<div style="display:none">{lib}</div>{svg}</body></html>', encoding="utf-8")
        names.append(k)
    js = ("const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');(async()=>{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{px},height:400}}}});"
          f"for(const n of {json.dumps(names)}){{await p.goto('file://{out}/'+n+'.html');await p.waitForTimeout(100);"
          f"await p.screenshot({{path:'{out}/'+n+'.png',fullPage:true}});}}await b.close();}})();")
    env = {**os.environ, "PLAYWRIGHT_MODULE": os.environ.get("PLAYWRIGHT_MODULE", "/opt/npm-tools/node_modules/playwright")}
    subprocess.run(["node", "-e", js], check=True, env=env)
    for n in names:
        (out / f"{n}.html").unlink()
    print(f"PASS: {len(names)} Bilder in {out}")


if __name__ == "__main__":
    main()
