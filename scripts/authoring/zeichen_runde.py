#!/usr/bin/env python3
"""Automatische Zeichenwahl (docs/SYMBOLPROZESS.md, «Runde 12»): Vorschläge prüfen und das verständlichste Zeichen wählen.

Eingang: Vorschläge je Lexikon-ID (Ideenfindung, z. B. von getrennten KI-Instanzen):
    {"FIG-…": {"vorschlaege": [{"emoji": [...], "anordnung": "…", "grund": "…"}, …], "ablenker": [4 Begriffe],
               "eigen": false, "eigen_idee": ""}, …}
Ablauf:
  1. Runde 0: das bisherige Zeichen im Unterscheidungstest (zeichen_test.py --frage auswahl, gleiche Ablenker).
  2. Runde 1–3: Vorschlag 1, für Durchgefallene Vorschlag 2, dann 3 – je vier Instanzen.
  3. Wahl je Zeichen: der erste bestandene Vorschlag; sonst das Zeichen mit den meisten richtigen Antworten (bei Gleichstand
     das Emoji, weil professionell gezeichnet). Ohne Emoji-Vorschlag («eigen») bleibt das bisherige Zeichen und wird als
     offen gemeldet.
Ausgabe: scripts/authoring/bildsymbole_daten/emoji_zuordnung.json (gewählte Emoji, mit Ergebnis) und ein Bericht
reports/zeichen-runde12-<datum>.json; danach emoji_zeichen.py ausführen.

    python3 scripts/authoring/zeichen_runde.py VORSCHLAEGE.json ARBEITSORDNER [--instanzen 4]
"""
import datetime
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PY = sys.executable


def lex_name(fid):
    f = ROOT / f"data/illustrations/lexicon/{fid}.json"
    return json.loads(f.read_text(encoding="utf-8"))["names"]["de"] if f.exists() else fid


def test(work, name, drafts, n):
    d = work / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "E.json").write_text(json.dumps(drafts, ensure_ascii=False, indent=1), encoding="utf-8")
    ids = list(drafts)
    cmd = [PY, str(ROOT / "scripts/authoring/zeichen_test.py"), str(d / "t"), *ids, "--entwuerfe", str(d / "E.json"),
           "--frage", "auswahl", "--befragen", str(n)]
    subprocess.run(cmd, check=True, cwd=ROOT)
    return json.loads((d / "t/auswahl.json").read_text(encoding="utf-8"))


def emoji_drafts(work, name, sel):
    z = {k: v for k, v in sel.items()}
    zf = work / f"{name}-Z.json"
    ef = work / f"{name}-Ez.json"
    zf.write_text(json.dumps(z, ensure_ascii=False, indent=1), encoding="utf-8")
    subprocess.run([PY, str(ROOT / "scripts/authoring/emoji_zeichen.py"), "--entwuerfe", str(ef), str(zf)], check=True, cwd=ROOT)
    return json.loads(ef.read_text(encoding="utf-8"))


def main():
    args = sys.argv[1:]
    n = 4
    if "--instanzen" in args:
        i = args.index("--instanzen")
        n = int(args[i + 1])
        del args[i:i + 2]
    vor = json.loads(pathlib.Path(args[0]).read_text(encoding="utf-8"))
    work = pathlib.Path(args[1]).resolve()
    work.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(ROOT / "scripts"))
    sys.path.insert(0, str(ROOT / "scripts/authoring"))
    import bilder_anime as A
    _lib, vb = A.library()
    erg = {fid: {"bisher": None, "versuche": []} for fid in vor}
    # Runde 0: bisheriges Zeichen (aus der Bibliothek, gleiche Ablenker)
    alt = {f"{fid}@0": {"bedeutung": lex_name(fid), "ablenker": e.get("ablenker", [])} for fid, e in vor.items() if fid in vb}
    if alt:
        # Entwürfe ohne svg: zeichen_test nimmt dann das Bibliothekszeichen der Basis-ID
        r0 = test(work, "r0", {k: {**v, "bibliothek": True} for k, v in alt.items()}, n)
        for k, v in r0.items():
            erg[k.split("@")[0]]["bisher"] = v
    offen = [fid for fid, e in vor.items() if e.get("vorschlaege")]
    for rnd in range(3):
        sel = {}
        for fid in offen:
            vs = vor[fid]["vorschlaege"]
            if rnd < len(vs):
                sel[f"{fid}@{rnd + 1}"] = {**vs[rnd], "bedeutung": lex_name(fid), "ablenker": vor[fid].get("ablenker", [])}
        if not sel:
            break
        drafts = emoji_drafts(work, f"r{rnd + 1}", sel)
        for k in drafts:
            drafts[k]["ablenker"] = sel[k]["ablenker"]
        r = test(work, f"r{rnd + 1}", drafts, n)
        for k, v in r.items():
            erg[k.split("@")[0]]["versuche"].append({"vorschlag": rnd + 1, **sel[k], **v})
        offen = [fid for fid in offen if not any(x["bestanden"] for x in erg[fid]["versuche"])]
    zu, bericht = {}, {}
    for fid, e in erg.items():
        ok = [x for x in e["versuche"] if x["bestanden"]]
        best = ok[0] if ok else max(e["versuche"], key=lambda x: x["richtig"], default=None)
        alt_r = (e["bisher"] or {}).get("richtig", -1)
        if best and (ok or best["richtig"] >= alt_r):
            zu[fid] = {"emoji": best["emoji"], "anordnung": best.get("anordnung", "einzeln"), "grund_de": best.get("grund", ""),
                       "test": f"{best['richtig']}/{best['von']} (bisher {alt_r if alt_r >= 0 else '–'})", "bestanden": bool(ok)}
        bericht[fid] = {"name": lex_name(fid), "gewaehlt": "emoji" if fid in zu else "bisher", "bisher": e["bisher"],
                        "versuche": e["versuche"], "eigen": vor[fid].get("eigen", False), "eigen_idee": vor[fid].get("eigen_idee", "")}
    (ROOT / "scripts/authoring/bildsymbole_daten/emoji_zuordnung.json").write_text(json.dumps(zu, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    rep = ROOT / f"reports/zeichen-runde12-{datetime.date.today().isoformat()}.json"
    rep.write_text(json.dumps({"datum": datetime.date.today().isoformat(), "instanzen": n, "methode": "zeichen_test.py --frage auswahl",
                               "zeichen": bericht}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    nb = sum(1 for v in zu.values() if v["bestanden"])
    print(f"PASS: {len(zu)} Zeichen mit Emoji ({nb} bestanden, {len(zu) - nb} besser als bisher), {len(vor) - len(zu)} bleiben bisher; Bericht {rep.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
