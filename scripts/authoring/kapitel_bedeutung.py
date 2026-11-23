#!/usr/bin/env python3
"""Verständlichkeit der Merkbilder (Kapitelbilder) prüfen, 2026-11-23 (wie zeichen_bedeutung.py für Zeichen).

1. Blind: Testblätter mit je vier Kapiteln als Bildreihen (Felder nebeneinander, ohne Worte, ohne Stellenangabe). Zwei getrennte
   Instanzen sagen je Feld, welche Szene bzw. Geschichte gezeigt ist.
2. Bewerten: eine weitere Instanz vergleicht mit der Handlung des Feldes im Bildauftrag: 2 = Szene erkannt, 1 = teilweise (Personen
   oder Handlung stimmen), 0 = andere Szene.
Bestanden: Summe beider Instanzen ≥ 2. Ein Merkbild soll ohne Worte an seine Szene erinnern; durchgefallene Felder werden mit dem
Stichwort (wie in der App) erneut gezeigt («passt mit dem Wort?»). Grenzen: KI-Instanzen ersetzen keine Prüfung mit Lesenden.

    python3 scripts/authoring/kapitel_bedeutung.py AUSGABE BUCH [BUCH …]
"""
import json
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from zeichen_bedeutung import frage  # noqa: E402

BLIND = ("Lies die Bilddatei {datei} (Read-Werkzeug). Sie zeigt nummerierte Bildreihen aus einer Bibel-App; jede Reihe ist ein Kapitel, "
         "jedes Feld (von links: a, b, c, d) eine Szene. Gib je Feld an, welche biblische Szene oder Geschichte du erkennst (kurz, Deutsch). "
         "Antworte nur mit JSON: {{\"1a\": \"…\", \"1b\": \"…\", …}}")
WERTEN = ("Bewerte blinde Deutungen von Bildfeldern. Je Feld: was es zeigen soll und zwei Antworten von Personen, die nur das Bild sahen. "
          "Gib je Antwort 2 (Szene erkannt), 1 (teilweise: Personen oder Handlung stimmen) oder 0 (andere Szene). Antworte nur mit JSON: "
          "{{\"ID\": [A, B], …}}\n\n{daten}")
KONTEXT = ("Lies die Bilddatei {datei}. Nummerierte Bildreihen einer Bibel-App; unter jedem Feld steht in der App ein Stichwort. "
           "Die Stichworte: {woerter}. Beurteile je Feld, ob Bild und Stichwort zusammen die Szene klar machen («passt»), nur schwach "
           "(«schwach») oder in die Irre führen («irrefuehrend»). Antworte nur mit JSON: {{\"1a\": {{\"urteil\": \"…\", \"grund\": \"…\"}}, …}}")


def blatt(reihen, pfad):
    from PIL import Image, ImageDraw, ImageFont
    zw, zh = 240, 160
    im = Image.new("RGB", (4 * (zw + 10) + 50, len(reihen) * (zh + 20) + 10), "white")
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype("DejaVuSans-Bold.ttf", 22)
    for r, felder in enumerate(reihen):
        y = 10 + r * (zh + 20)
        d.text((8, y + zh // 2 - 12), str(r + 1), fill="black", font=f)
        for c, sid in enumerate(felder):
            b = Image.open(ROOT / f"data/illustrations/aquarell/img/{sid}.webp").convert("RGB").resize((zw, zh))
            im.paste(b, (44 + c * (zw + 10), y))
            d.text((48 + c * (zw + 10), y + 4), "abcd"[c], fill="black", font=f)
    im.save(pfad)


def main():
    out = pathlib.Path(sys.argv[1]).resolve()
    (out / "blind").mkdir(parents=True, exist_ok=True)
    kap, info = [], {}
    for b in sys.argv[2:]:
        plan = json.loads((DATEN / f"szenen-kap-{b.lower()}.json").read_text(encoding="utf-8"))
        for bi in plan["bilder"]:
            brief = json.loads((ROOT / f"data/illustrations/briefs/{bi['brief']}.json").read_text(encoding="utf-8"))
            if all((ROOT / f"data/illustrations/aquarell/img/{s}.webp").exists() for s in bi["felder"]):
                kap.append(bi["felder"])
                for s, pa in zip(bi["felder"], brief["panels"]):
                    info[s] = {"stelle": pa["reference"], "handlung": pa["action_de"],
                               "band": (plan["szenen"][s].get("band") or pa.get("keywords") or {}).get("de", "")}
    saetze = [kap[i:i + 4] for i in range(0, len(kap), 4)]
    for n, s in enumerate(saetze, 1):
        blatt(s, out / "blind" / f"blatt-{n:02d}.png")
    key = lambda n, r, c: saetze[n - 1][r][c]
    auftr = [(n, i) for n in range(1, len(saetze) + 1) for i in (0, 1)]
    with ThreadPoolExecutor(6) as ex:
        antw = list(ex.map(lambda t: frage(out / "blind", BLIND.format(datei=f"blatt-{t[0]:02d}.png"), "claude-sonnet-4-6"), auftr))
    blind = {}
    for (n, i), a in zip(auftr, antw):
        for r, reihe in enumerate(saetze[n - 1]):
            for c, sid in enumerate(reihe):
                blind.setdefault(sid, ["", ""])[i] = a.get(f"{r + 1}{'abcd'[c]}", "")
    ids = list(info)
    punkte = {}
    teile = [ids[i:i + 30] for i in range(0, len(ids), 30)]
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(lambda t: frage(out, WERTEN.format(daten="\n".join(f"{s}: soll zeigen «{info[s]['handlung']}»; A: {blind[s][0]}; B: {blind[s][1]}" for s in t)),
                                        "claude-sonnet-4-6"), teile):
            punkte.update(r)
    schwach = [s for s in ids if sum(punkte.get(s, [0, 0])) < 2]
    kontext = {}
    if schwach:   # mit Stichwort, wie in der App
        ks = [[s] for s in schwach]
        ks = [ks[i:i + 6] for i in range(0, len(ks), 6)]
        (out / "kontext").mkdir(exist_ok=True)
        for n, s in enumerate(ks, 1):
            blatt(s, out / "kontext" / f"blatt-{n:02d}.png")
        with ThreadPoolExecutor(6) as ex:
            rs = list(ex.map(lambda t: frage(out / "kontext", KONTEXT.format(datei=f"blatt-{t[0]:02d}.png",
                                                                             woerter="; ".join(f"{r + 1}a: «{info[x[0]]['band']}»" for r, x in enumerate(t[1]))),
                                             "claude-sonnet-4-6"), enumerate(ks, 1)))
        for (n, s), r in zip(enumerate(ks, 1), rs):
            for i, x in enumerate(s):
                kontext[x[0]] = r.get(f"{i + 1}a", {})
    erg = {s: {"stelle": info[s]["stelle"], "punkte": punkte.get(s), "blind": blind[s], "kontext": kontext.get(s),
               "ergebnis": "bestanden" if sum(punkte.get(s, [0, 0])) >= 2 or (kontext.get(s) or {}).get("urteil") == "passt" else
               ("schwach" if (kontext.get(s) or {}).get("urteil") == "schwach" else "durchgefallen")} for s in ids}
    (out / "ergebnis.json").write_text(json.dumps(erg, ensure_ascii=False, indent=1), encoding="utf-8")
    print({k: sum(v["ergebnis"] == k for v in erg.values()) for k in ("bestanden", "schwach", "durchgefallen")})
    for s, v in erg.items():
        if v["ergebnis"] != "bestanden":
            print(f"{s} {v['stelle']} {v['ergebnis']}: blind {v['blind']}; {v['kontext']}")


if __name__ == "__main__":
    main()
