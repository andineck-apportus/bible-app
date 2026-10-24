#!/usr/bin/env python3
"""Zeichen in Einsatzgrösse prüfen (docs/SYMBOLPROZESS.md, «Prüfung in Einsatzgrösse» und «Detailstufen», 2026-10-24).

Zeichnet Bildzeichen so gross, wie sie im Bild erscheinen (Standard: 32 px hoch wie ein Zeichen in einer Zelle eines
Strukturbilds), nummeriert und ohne Namen, auf Testblätter. Der Schlüssel (Nummer → Lexikon-ID) liegt getrennt vom Blatt,
damit eine getrennte KI-Instanz nur das Blatt sieht und blind benennt.

    python3 scripts/authoring/zeichen_test.py AUSGABE FIG-ZEICHEN-BETEN FIG-ZEICHEN-HAND …   # diese Zeichen (aus der Bibliothek)
    python3 scripts/authoring/zeichen_test.py AUSGABE --auftraege RUT,TIT,MAT-2              # alle Zeichen in Zellen dieser Bildaufträge
    python3 scripts/authoring/zeichen_test.py AUSGABE --entwuerfe E.json --verteilen …       # Entwürfe in Detailstufen

Optionen:
  --px 32            Höhe des Zeichens in CSS-Pixeln (für die Einzelprüfung zusätzlich --px 160)
  --dpr 2            Pixeldichte des Bildschirms (2 = gewöhnlicher Handy- oder Retina-Bildschirm)
  --zelle            im Zusammenhang: das Zeichen in seiner Zelle mit Text (bilder_diagramm.Cells, Massstab so, dass das
                     Zeichen --px hoch ist); Text aus dem ersten Bildauftrag mit dem Zeichen bzw. aus dem Feld «zelle» des Entwurfs
  --entwuerfe E.json Entwürfe statt Bibliothek: {"FIG-…@1": {"vb", "svg", "bedeutung", "gezeichnet", "zelle"?}, …};
                     ohne IDs auf der Befehlszeile werden alle Entwürfe geprüft
  --verteilen        Detailstufen (…@1, …@2, …@3) auf getrennte Sätze verteilen: jeder Satz (und damit jede Instanz)
                     sieht ein Zeichen nur in einer Stufe, alle Stufen kommen gleich oft vor
  --frage detail     zusätzlich je Zeichen: «Würde mehr Detail helfen, ist es egal, oder stört es?» und «Womit verwechselbar?»
  --nur-zeichen      nur FIG-ZEICHEN-*
  --je-blatt 20 --seed 7
  --befragen 4       danach N getrennte Instanzen je Blatt blind benennen lassen (claude -p, nur Lesezugriff auf das Blatt)
  --bewerten         danach eine weitere Instanz die Antworten bewerten lassen: Bedeutung 0/1/2 und «Bild erkannt» 0/1

Ausgabe:
    AUSGABE/blind/[satz-N/]blatt-NN.png und AUSGABE/blind/frage.txt   (nur das gehört in die blinde Instanz)
    AUSGABE/schluessel.json                                           (Nummer → ID, getrennt)
    AUSGABE/antworten.json, AUSGABE/bewertung.json                    (mit --befragen / --bewerten)

«Erkannt» heisst wie in Runde 3–5: mindestens zwei von vier Antworten treffen die Bedeutung (Wert 2); «Bild erkannt»: die
Mehrheit sieht, was gezeichnet ist. Grenzen: KI-Instanzen ersetzen keine Prüfung mit Leserinnen und Lesern; die Grösse am
Bildschirm hängt vom Gerät ab.
"""
import json
import os
import pathlib
import random
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts/authoring"))

FRAGE = ("Auf dem Bild {blatt} siehst du nummerierte kleine Bildzeichen aus einer Bilderbibel (Neues und Altes Testament). "
         "Jedes Zeichen steht für einen Gegenstand, eine Handlung oder einen Begriff. Lies die Bilddatei mit dem Read-Werkzeug. "
         "Nenne für jede Nummer in einem bis drei Wörtern auf Deutsch, was das Zeichen bedeutet. Rate, wenn du unsicher bist. ")
FRAGE_ZELLE = ("Auf dem Bild {blatt} siehst du nummerierte Zellen aus einem Schaubild einer Bilderbibel; jede Zelle hat ein kleines "
               "Bildzeichen über dem Text. Lies die Bilddatei mit dem Read-Werkzeug. Nenne für jede Nummer in einem bis drei Wörtern "
               "auf Deutsch, was das kleine Bildzeichen selbst zeigt (was gezeichnet ist, nicht was im Text steht). ")
ANTWORT = "Antworte nur mit einem JSON-Objekt {{\"N01\": \"…\", …}}, ohne weiteren Text."
ANTWORT_DETAIL = ("Beantworte je Nummer zusätzlich: Würde mehr Detail helfen, das Zeichen zu erkennen, ist es egal, oder würde es "
                  "stören (\"mehr\", \"egal\" oder \"stört\")? Womit könntest du es verwechseln (ein bis drei Wörter)? Antworte nur "
                  "mit einem JSON-Objekt {{\"N01\": {{\"antwort\": \"…\", \"detail\": \"mehr|egal|stört\", \"verwechslung\": \"…\"}}, …}}, "
                  "ohne weiteren Text.")


def walk_icons(o, out):
    if isinstance(o, dict):
        if isinstance(o.get("icons"), list):
            for i in o["icons"]:
                if isinstance(i, str):
                    out.setdefault(i, o)
        for v in o.values():
            walk_icons(v, out)
    elif isinstance(o, list):
        for v in o:
            walk_icons(v, out)


def from_briefs(names):
    out = {}
    for n in names:
        for b in json.loads((ROOT / "scripts/authoring/bildauftraege_daten" / f"{n}.json").read_text(encoding="utf-8")):
            for p in b.get("panels", []):
                if p.get("diagram"):
                    walk_icons(p["diagram"], out)
    return out


def render(out, pages, width, dpr):
    js = ("const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');(async()=>{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{width},height:400}},deviceScaleFactor:{dpr}}});"
          f"for(const n of {json.dumps(pages)}){{await p.goto('file://{out}/'+n+'.html');await p.waitForTimeout(150);"
          f"await p.screenshot({{path:'{out}/'+n+'.png',fullPage:true}});}}await b.close();}})();")
    env = {**os.environ, "PLAYWRIGHT_MODULE": os.environ.get("PLAYWRIGHT_MODULE", "/opt/npm-tools/node_modules/playwright")}
    subprocess.run(["node", "-e", js], check=True, env=env)
    for n in pages:
        (out / f"{n}.html").unlink()


def ask(cwd, prompt, model):
    r = subprocess.run(["claude", "-p", prompt, "--model", model, "--allowedTools", "Read",
                        "--disallowedTools", "Bash,Grep,Glob,WebFetch,WebSearch,Edit,Write"],
                       cwd=cwd, capture_output=True, text=True, timeout=900)
    m = re.search(r"\{.*\}", r.stdout, re.S)
    try:
        return json.loads(m.group(0)) if m else {"_roh": r.stdout}
    except json.JSONDecodeError:
        return {"_roh": r.stdout}


def base(k):
    return k.split("@")[0]


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    out = pathlib.Path(args.pop(0)).resolve()
    opts = {"--px": "32", "--dpr": "2", "--je-blatt": "20", "--seed": "7", "--befragen": "0", "--auftraege": "",
            "--modell": "claude-opus-5-5", "--entwuerfe": "", "--frage": ""}
    flags, ids, i = set(), [], 0
    while i < len(args):
        a = args[i]
        if a in opts:
            opts[a] = args[i + 1]; i += 2; continue
        if a.startswith("--"):
            flags.add(a)
        else:
            ids.append(a)
        i += 1
    px, dpr, per = float(opts["--px"]), float(opts["--dpr"]), int(opts["--je-blatt"])
    ctx = from_briefs([x for x in opts["--auftraege"].split(",") if x]) if opts["--auftraege"] else {}
    if opts["--auftraege"] and not opts["--entwuerfe"]:
        ids += sorted(k for k in ctx if k not in ids)
    ent = json.loads(pathlib.Path(opts["--entwuerfe"]).read_text(encoding="utf-8")) if opts["--entwuerfe"] else {}
    if ent and not ids:
        ids = list(ent)
    if "--nur-zeichen" in flags:
        ids = [k for k in ids if base(k).startswith("FIG-ZEICHEN-")]

    import bilder_anime as A
    import bilder_auto as _auto
    lib, vb = A.library()
    extra = []
    for n, (k, v) in enumerate(ent.items()):  # Entwürfe als eigene Symbole (ohne Namen im Symbol)
        sid = f"tst-{n:03d}"
        extra.append(f'<symbol id="{sid}" viewBox="{v["vb"]}">{v["svg"]}</symbol>')
        vb[k] = (sid, v["vb"])
    lib += '<svg width="0" height="0"><defs>' + "".join(extra) + "</defs></svg>"
    A._VB.update(vb)
    ids = list(dict.fromkeys(ids))
    missing = [k for k in ids if k not in vb]
    if missing:
        sys.exit(f"FEHLER: ohne Zeichnung: {', '.join(missing)}")
    if opts["--auftraege"] and not ent:  # Personen, Rollen, Gruppen und Gott sind Porträts, keine Zeichen (eigener Test, Runde 1–4)
        lexk = {p.stem: json.loads(p.read_text(encoding="utf-8"))["kind"] for p in (ROOT / "data/illustrations/lexicon").glob("FIG-*.json")}
        ids = [k for k in ids if lexk.get(k) not in ("person", "role", "group", "divine")]

    # Sätze: ohne --verteilen ein Satz; mit --verteilen je Stufe ein Satz, jedes Grundzeichen einmal je Satz
    if "--verteilen" in flags:
        bases = list(dict.fromkeys(base(k) for k in ids))
        levels = {b: sorted(k for k in ids if base(k) == b) for b in bases}
        n = max(len(v) for v in levels.values())
        sets = [[levels[b][(bi + s) % len(levels[b])] for bi, b in enumerate(bases)] for s in range(n)]
    else:
        sets = [ids]
    zelle = "--zelle" in flags
    if zelle:
        import bilder_diagramm as DG
        comp = A.AniComposer(_auto.gather_lex(), A.EXTRA_META)
        comp.vbmap = vb
        cells = DG.Cells(comp)
        k_scale = px / cells.ICON_H
    frage = (FRAGE_ZELLE if zelle else FRAGE) + (ANTWORT_DETAIL if opts["--frage"] == "detail" else ANTWORT)
    blind = out / "blind"
    blind.mkdir(parents=True, exist_ok=True)
    key, pages = {}, []
    for si, ss in enumerate(sets):
        ss = list(ss)
        random.Random(int(opts["--seed"]) + si).shuffle(ss)
        sub = f"satz-{si + 1}/" if len(sets) > 1 else ""
        (blind / sub).mkdir(parents=True, exist_ok=True)
        for pg in range(0, len(ss), per):
            items = []
            name = f"{sub}blatt-{pg // per + 1:02d}"
            for j, k in enumerate(ss[pg:pg + per]):
                no = f"N{j + 1:02d}"
                key.setdefault(name, {})[no] = k
                sym, box = vb[k]
                if zelle:
                    src = (ent.get(k) or {}).get("zelle") or ctx.get(base(k)) or {"a": "…"}
                    z = {kk: v for kk, v in src.items() if kk in ("a", "b", "tone", "role")}
                    z["icons"] = [k]
                    w = 90
                    h = cells.height(z, w)
                    inner = cells.draw(z, 1, 1, w, h)
                    svg = f'<svg viewBox="0 0 {w + 2} {h + 2:.1f}" width="{(w + 2) * k_scale:.0f}" height="{(h + 2) * k_scale:.0f}">{inner}</svg>'
                else:
                    iw = _auto.icon_w(box, px)
                    svg = f'<svg viewBox="{box}" width="{iw:.1f}" height="{px:.1f}" preserveAspectRatio="xMidYMid meet"><use href="#{sym}"/></svg>'
                items.append(f'<div class="c"><b>{no}</b>{svg}</div>')
            colw = int((92 * k_scale) if zelle else max(px * 1.9, 60)) + 20
            cols = 4 if zelle else 5
            (blind / f"{name}.html").write_text(
                f'<html><head><meta charset="utf-8"><style>.lw{{display:none}}.lw-de{{display:inline}}</style></head><body style="margin:0;background:#fff;font:13px sans-serif">'
                f'<div style="display:none">{lib}</div>'
                f'<div style="display:grid;grid-template-columns:repeat({cols},{colw}px);gap:14px;padding:10px">{"".join(items)}</div>'
                f'<style>.c{{text-align:center;border:1px solid #ddd;padding:6px 2px;background:#FFFDF6}}.c b{{display:block;color:#888;font-size:12px;margin-bottom:6px}}.c svg{{display:block;margin:auto}}</style></body></html>',
                encoding="utf-8")
            pages.append(name)
    render(blind, pages, cols * (colw + 14) + 20, dpr)
    (blind / "frage.txt").write_text(frage.format(blatt="blatt-NN.png") + "\n", encoding="utf-8")
    meta = {"px": px, "dpr": dpr, "zelle": zelle, "frage": opts["--frage"] or "benennen", "saetze": len(sets), "blaetter": key}
    (out / "schluessel.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"PASS: {sum(len(s) for s in sets)} Zeichen in {len(sets)} Satz/Sätzen, {len(pages)} Blätter in {blind} "
          f"({px:g} px, dpr {dpr:g}{', in der Zelle' if zelle else ''}); Schlüssel {out / 'schluessel.json'}")

    n = int(opts["--befragen"])
    if n:
        from concurrent.futures import ThreadPoolExecutor
        jobs = [(pgn, r) for pgn in pages for r in range(n)]
        with ThreadPoolExecutor(8) as ex:
            res = list(ex.map(lambda j: ask(blind / os.path.dirname(j[0]), frage.format(blatt=f"{blind}/{j[0]}.png"), opts["--modell"]), jobs))
        ans = {}
        for (pgn, r), a in zip(jobs, res):
            for no, k in key[pgn].items():
                v = a.get(no, "")
                if not isinstance(v, dict):
                    v = {"antwort": v}
                ans.setdefault(k, []).append(v)
        (out / "antworten.json").write_text(json.dumps(ans, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"PASS: {n} Instanzen je Blatt, Antworten in {out / 'antworten.json'}")
    if "--bewerten" in flags:
        ans = json.loads((out / "antworten.json").read_text(encoding="utf-8"))
        lex = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (ROOT / "data/illustrations/lexicon").glob("FIG-*.json")}

        def info(k):
            e = ent.get(k) or {}
            L = lex.get(base(k)) or {}
            return {"bedeutung": e.get("bedeutung") or (L.get("names", {}).get("de", "") + " – " + L.get("identity_de", "")[:220]),
                    "gezeichnet": e.get("gezeichnet") or (L.get("legend") or {}).get("de", "")}
        task = {k: {**info(k), "antworten": [x.get("antwort", "") for x in v]} for k, v in ans.items()}
        tmp = out / "bewertung_auftrag.json"
        tmp.write_text(json.dumps(task, indent=1, ensure_ascii=False), encoding="utf-8")
        prompt = (f"Lies {tmp}. Für jedes Bildzeichen stehen Bedeutung, was gezeichnet ist, und freie Antworten blinder Betrachter. "
                  "Bewerte jede Antwort zweifach: «scores»: 2 = trifft die Bedeutung (gleicher Begriff oder gleichwertig), 1 = verwandt, "
                  "0 = falsch; «bild»: 1 = die Antwort zeigt, dass das Gezeichnete richtig gesehen wurde (auch wenn die Bedeutung "
                  "nicht getroffen ist), sonst 0. Antworte nur mit JSON {\"ID\": {\"scores\": [..], \"bild\": [..], "
                  "\"note\": \"kurz, häufigste Fehldeutung\"}, …} für alle IDs.")
        b = ask(out, prompt, opts["--modell"])
        (out / "bewertung.json").write_text(json.dumps(b, indent=1, ensure_ascii=False), encoding="utf-8")
        tr = sum(1 for k, v in b.items() if isinstance(v, dict) and sum(1 for s in v.get("scores", []) if s == 2) >= 2)
        print(f"PASS: bewertet, erkannt (≥2 Treffer) {tr} von {len(ans)}; {out / 'bewertung.json'}")


if __name__ == "__main__":
    main()
