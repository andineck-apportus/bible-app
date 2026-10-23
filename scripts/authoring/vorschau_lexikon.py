#!/usr/bin/env python3
"""Vorschau und Blindtest-Blätter für das Bildlexikon im Stil Anime (docs/SYMBOLPROZESS.md).

Zeichnet die Einträge mit dem aktuellen Stand der Werkzeuge (bilder_anime.library(), ohne Daten zu schreiben) und legt
PNG-Blätter an (Playwright/Chromium).

    python3 scripts/authoring/vorschau_lexikon.py AUSGABE FIG-RUT FIG-PETRUS …      # Vorschau mit Namen
    python3 scripts/authoring/vorschau_lexikon.py AUSGABE --art person,role         # alle Einträge dieser Arten
    python3 scripts/authoring/vorschau_lexikon.py AUSGABE --art object --blind      # nummeriert, ohne Namen; Schlüssel in AUSGABE/schluessel.json

Gegenstände und Zeichen kommen aus der Symbol-Bibliothek; nach Änderungen an bildsymbole*.py zuerst
`python3 scripts/authoring/bilder_symbol.py --bibliothek` ausführen. Grösse je Zelle mit --px (Standard 160).
"""
import json
import os
import pathlib
import random
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
    blind = "--blind" in args
    px = 160
    kinds = None
    ids = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--art":
            kinds = args[i + 1].split(","); i += 2; continue
        if a == "--px":
            px = int(args[i + 1]); i += 2; continue
        if not a.startswith("--"):
            ids.append(a)
        i += 1
    import bilder_anime as A
    lib, vb = A.library()
    lex = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (ROOT / "data/illustrations/lexicon").glob("FIG-*.json")}
    if kinds:
        ids += sorted(k for k in vb if k in lex and lex[k]["kind"] in kinds)
    ids = [k for k in ids if k in vb]
    if blind:
        random.Random(7).shuffle(ids)
    key, pages = {}, []
    per = 24
    for pg in range(0, len(ids), per):
        cells = []
        for j, k in enumerate(ids[pg:pg + per]):
            no = f"N{pg + j + 1:03d}"
            key[no] = k
            label = no if blind else lex[k]["names"]["de"]
            sym, box = vb[k]
            cells.append(f'<div class="c"><b>{label}</b><svg viewBox="{box}"><use href="#{sym}"/></svg></div>')
        name = f"blatt-{pg // per + 1:02d}"
        (out / f"{name}.html").write_text(
            f'<html><body style="margin:0;background:#fff;font:13px sans-serif"><div style="display:none">{lib}</div>'
            f'<div style="display:grid;grid-template-columns:repeat(6,{px + 16}px);gap:6px">{"".join(cells)}</div>'
            f'<style>.c{{text-align:center;border:1px solid #ddd}}.c svg{{width:{px}px;height:{px}px;display:block;margin:auto}}</style></body></html>',
            encoding="utf-8")
        pages.append(name)
    if blind:
        (out / "schluessel.json").write_text(json.dumps(key, indent=1), encoding="utf-8")
    js = ("const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');(async()=>{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{6 * (px + 22)},height:600}}}});"
          f"for(const n of {json.dumps(pages)}){{await p.goto('file://{out}/'+n+'.html');await p.waitForTimeout(150);"
          f"await p.screenshot({{path:'{out}/'+n+'.png',fullPage:true}});}}await b.close();}})();")
    env = {**os.environ, "PLAYWRIGHT_MODULE": os.environ.get("PLAYWRIGHT_MODULE", "/opt/npm-tools/node_modules/playwright")}
    subprocess.run(["node", "-e", js], check=True, env=env)
    for n in pages:
        (out / f"{n}.html").unlink()
    print(f"PASS: {len(ids)} Einträge auf {len(pages)} Blättern in {out}" + (" (blind, Schlüssel separat)" if blind else ""))


if __name__ == "__main__":
    main()
