#!/usr/bin/env python3
"""Vorschau direkt aus einer Quelldatei der Bildaufträge (bildauftraege_daten/*.json oder ein Entwurf davon), ohne Daten zu
schreiben – zum Ausprobieren von Szenen und Strukturbildern (`diagram`), bevor `bildauftraege.py` läuft.

    python3 scripts/authoring/vorschau_auftrag.py AUSGABE QUELLE.json SUFFIX … [--lang gsw] [--px 760]

Legt AUSGABE/<SUFFIX>.png an (Worte im Bild in der gewählten Sprache, Standard de).
"""
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts/authoring"))

KEYS = ("keywords", "names", "letter", "diagram", "stage")


def panel(p):
    q = {"n": p["n"], "reference": p["reference"], "figures": p.get("figures", []), "objects": p.get("objects", []),
         "signs": p.get("signs", []), "action_de": p.get("action_de", ""),
         "speech": [{"from": s["from"], "to": s["to"], "icons": s.get("icons", []), **({"think": True} if s.get("think") else {}),
                     **({"word": s["word"]} if s.get("word") else {})} for s in p.get("speech", [])]}
    for k in KEYS:
        if p.get(k):
            q[k] = p[k]
    return q


def main():
    args = sys.argv[1:]
    if len(args) < 3:
        sys.exit(__doc__)
    out = pathlib.Path(args.pop(0)).resolve()
    src = json.loads(pathlib.Path(args.pop(0)).read_text(encoding="utf-8"))
    out.mkdir(parents=True, exist_ok=True)
    lang, px, keys, i = "de", 760, [], 0
    while i < len(args):
        if args[i] in ("--lang", "--px"):
            if args[i] == "--lang":
                lang = args[i + 1]
            else:
                px = int(args[i + 1])
            i += 2
            continue
        keys.append(args[i])
        i += 1
    import bilder_anime as A
    import bilder_auto as _auto
    lib, vb = A.library()
    A._VB.update(vb)
    by = {b["suffix"]: b for b in src}
    css = "<style>.lw{display:none}.lw-%s{display:inline}</style>" % lang
    for k in keys:
        if k not in by:
            sys.exit(f"FEHLER: {k} nicht in der Quelldatei")
        A.CUR[0] = k.lower()
        c = A.AniComposer(_auto.gather_lex(), A.EXTRA_META)
        c.vbmap = vb
        c.uid = "a" + k.lower()
        bodies = [c.panel(panel(p)) for p in by[k]["panels"]]
        svg = A.alayout(bodies, getattr(c, "bands", None), getattr(c, "sizes", None), getattr(c, "alts", None)).replace("<svg ", f'<svg width="{px}" ', 1)
        (out / f"{k}.html").write_text(f'<html><head><meta charset="utf-8">{css}</head><body style="margin:0;background:#E9E4DA">'
                                       f'<div style="display:none">{lib}</div>{svg}</body></html>', encoding="utf-8")
    js = ("const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');(async()=>{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{px},height:400}}}});"
          f"for(const n of {json.dumps(keys)}){{await p.goto('file://{out}/'+n+'.html');await p.waitForTimeout(100);"
          f"await p.screenshot({{path:'{out}/'+n+'.png',fullPage:true}});}}await b.close();}})();")
    env = {**os.environ, "PLAYWRIGHT_MODULE": os.environ.get("PLAYWRIGHT_MODULE", "/opt/npm-tools/node_modules/playwright")}
    subprocess.run(["node", "-e", js], check=True, env=env)
    for n in keys:
        (out / f"{n}.html").unlink()
    print(f"PASS: {len(keys)} Bilder in {out}")


if __name__ == "__main__":
    main()
