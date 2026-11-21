#!/usr/bin/env python3
"""Bedeutungsprüfung der gemalten Zeichen des Bildlexikons (FIG-ZEICHEN-*), 2026-11-21.

Die Malprüfung (bilder_aquarell_figuren.py) fragt, ob das Bild der Beschreibung entspricht. Diese Prüfung fragt, ob man das
Zeichen versteht (docs/BILDSTIL.md, «Zeichen und Bilder verständlich machen»; docs/SYMBOLPROZESS.md):

1. Blind: Testblätter mit nummerierten, freigestellten Zeichen ohne Namen, etwa so gross wie in einem Strukturbild auf dem
   Handy. Zwei getrennte Instanzen nennen je Zeichen, was abgebildet ist und welchen Begriff es darstellen soll.
2. Bewerten: eine weitere Instanz vergleicht die Antworten mit Name und Bedeutung im Bildlexikon: 2 = getroffen,
   1 = verwandt oder im Zusammenhang naheliegend, 0 = anderer Begriff, irreführend.
3. Zusammenhang: Zeichen unter 2 Punkten (Summe beider Instanzen) werden mit ihrem Begriff gezeigt, wie im Strukturbild das Wort
   neben dem Bild steht: «Passt das Bild zum Wort, oder führt es in die Irre (womit verwechselbar)?»
Bestanden: Summe ≥ 2 im Blindtest, oder im Zusammenhang «passt» ohne Verwechslungsgefahr. Durchgefallene Zeichen werden neu
entworfen (Beschreibung) und neu gemalt. Grenzen: KI-Instanzen ersetzen keine Prüfung mit Leserinnen und Lesern.

    python3 scripts/authoring/zeichen_bedeutung.py AUSGABE [--je-blatt 12] [--modell claude-sonnet-4-6] [--nur ID,ID]
"""
import json
import pathlib
import random
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/authoring"))
import vignetten as V  # noqa: E402

STIL = ROOT / "data/illustrations/styles/ILLSTYLE-AQUARELL.json"
LEX = ROOT / "data/illustrations/lexicon"
ZELLE = 220   # Pixel je Zeichen auf dem Blatt (entspricht etwa 110 CSS-Pixeln bei doppelter Pixeldichte)


def zeichen(nur=None):
    r = json.loads(STIL.read_text(encoding="utf-8"))["renderings"]
    out = []
    for k, v in sorted(r.items()):
        if not k.startswith("FIG-ZEICHEN-") or (nur and k not in nur):
            continue
        if v.get("image") and (v.get("check") or {}).get("stufe") == "ki-geprueft" and (ROOT / v["image"]).exists():
            out.append(k)
    return out


def info(k):
    lx = json.loads((LEX / f"{k}.json").read_text(encoding="utf-8")) if (LEX / f"{k}.json").exists() else {}
    return {"name": (lx.get("names") or {}).get("de", k), "bedeutung": lx.get("identity_de", ""),
            "legende": (lx.get("legend") or {}).get("de", ""), "nicht": lx.get("rules_de", [])}


def blatt(ids, pfad, start):
    import io
    from PIL import Image, ImageDraw, ImageFont
    r = json.loads(STIL.read_text(encoding="utf-8"))["renderings"]
    sp = 4
    zeilen = -(-len(ids) // sp)
    im = Image.new("RGB", (sp * (ZELLE + 40) + 20, zeilen * (ZELLE + 60) + 20), "white")
    d = ImageDraw.Draw(im)
    try:
        f = ImageFont.truetype("DejaVuSans-Bold.ttf", 26)
    except OSError:
        f = ImageFont.load_default()
    for i, k in enumerate(ids):
        x, y = 20 + (i % sp) * (ZELLE + 40), 20 + (i // sp) * (ZELLE + 60)
        bild = Image.open(io.BytesIO(V.freistellen(r[k]["image"]))).convert("RGBA")
        bb = bild.getchannel("A").point(lambda a: 255 if a > 40 else 0).getbbox() or (0, 0, *bild.size)
        bild = bild.crop(bb)
        bild.thumbnail((ZELLE, ZELLE))
        im.paste(bild, (x + (ZELLE - bild.width) // 2, y + 40 + (ZELLE - bild.height) // 2), bild)
        d.text((x, y), str(start + i), fill="black", font=f)
    im.save(pfad)


def frage(cwd, prompt, modell):
    r = subprocess.run(["claude", "-p", prompt, "--model", modell, "--allowedTools", "Read",
                        "--disallowedTools", "Bash,Grep,Glob,WebFetch,WebSearch,Edit,Write"],
                       cwd=cwd, capture_output=True, text=True, timeout=1200)
    m = re.search(r"\{.*\}", r.stdout, re.S)
    try:
        return json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        return {}


BLIND = ("Lies die Bilddatei {datei} (mit dem Read-Werkzeug). Sie zeigt nummerierte kleine Aquarell-Zeichen aus einer Bibel-App. "
         "Jedes Zeichen steht für einen Begriff (z. B. eine Handlung, eine Eigenschaft, ein Gefühl, eine Sache). "
         "Gib für jede Nummer an: «abbild» (was ist zu sehen, kurz) und «begriff» (welcher Begriff ist wohl gemeint, 1–3 Wörter Deutsch). "
         "Antworte nur mit JSON: {{\"1\": {{\"abbild\": \"…\", \"begriff\": \"…\"}}, …}}")
WERTEN = ("Bewerte blinde Antworten zu Bildzeichen. Je Zeichen: der gemeinte Begriff (Name, Bedeutung) und die Antworten zweier "
          "Personen, die nur das Bild sahen. Gib je Antwort 2 (Begriff getroffen oder gleichbedeutend), 1 (verwandt oder mit dem "
          "Wort daneben naheliegend) oder 0 (anderer Begriff, irreführend). Antworte nur mit JSON: "
          "{{\"ID\": [Punkte Antwort A, Punkte Antwort B], …}}\n\n{daten}")
KONTEXT = ("Lies die Bilddatei {datei}. Sie zeigt nummerierte Aquarell-Zeichen aus einer Bibel-App; in der App steht neben jedem "
           "Zeichen das Wort. Die Wörter: {woerter}. Beurteile je Nummer, ob das Bild zum Wort passt und hilft («passt»), "
           "ob es nur schwach passt («schwach») oder in die Irre führt («irrefuehrend»), und womit es verwechselbar ist. "
           "Antworte nur mit JSON: {{\"1\": {{\"urteil\": \"passt|schwach|irrefuehrend\", \"verwechselbar\": \"…\"}}, …}}")


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    out = pathlib.Path(a[0]).resolve()
    je = int(a[a.index("--je-blatt") + 1]) if "--je-blatt" in a else 12
    modell = a[a.index("--modell") + 1] if "--modell" in a else "claude-sonnet-4-6"
    nur = set(a[a.index("--nur") + 1].split(",")) if "--nur" in a else None
    ids = zeichen(nur)
    random.Random(7).shuffle(ids)
    (out / "blind").mkdir(parents=True, exist_ok=True)
    saetze = [ids[i:i + je] for i in range(0, len(ids), je)]
    schluessel = {}
    for n, s in enumerate(saetze, 1):
        blatt(s, out / "blind" / f"blatt-{n:02d}.png", 1)
        schluessel[n] = s
    (out / "schluessel.json").write_text(json.dumps(schluessel, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(ids)} Zeichen auf {len(saetze)} Blättern")

    # 1. blind, zwei getrennte Instanzen je Blatt
    auftr = [(n, i) for n in schluessel for i in (0, 1)]
    with ThreadPoolExecutor(6) as ex:
        antw = list(ex.map(lambda t: frage(out / "blind", BLIND.format(datei=f"blatt-{t[0]:02d}.png"), modell), auftr))
    blind = {}
    for (n, i), r in zip(auftr, antw):
        for j, k in enumerate(schluessel[n], 1):
            blind.setdefault(k, ["", ""])[i] = r.get(str(j), {})
    (out / "blind.json").write_text(json.dumps(blind, ensure_ascii=False, indent=1), encoding="utf-8")

    # 2. bewerten (eine weitere Instanz, kennt Begriff und Antworten, nicht das Bild)
    punkte = {}
    teile = [ids[i:i + 40] for i in range(0, len(ids), 40)]
    def werte(t):
        daten = "\n".join(f"{k}: gemeint «{info(k)['name']}» ({info(k)['bedeutung'][:160]}); A: {blind[k][0]}; B: {blind[k][1]}" for k in t)
        return frage(out, WERTEN.format(daten=daten), modell)
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(werte, teile):
            punkte.update(r)

    # 3. Zusammenhang für die schwachen
    schwach = [k for k in ids if sum(punkte.get(k, [0, 0])) < 2]
    kontext = {}
    if schwach:
        (out / "kontext").mkdir(exist_ok=True)
        kteile = [schwach[i:i + je] for i in range(0, len(schwach), je)]
        def pruefe(t):
            n, s = t
            blatt(s, out / "kontext" / f"blatt-{n:02d}.png", 1)
            w = "; ".join(f"{j}: «{info(k)['name']}»" for j, k in enumerate(s, 1))
            r = frage(out / "kontext", KONTEXT.format(datei=f"blatt-{n:02d}.png", woerter=w), modell)
            return {k: r.get(str(j), {}) for j, k in enumerate(s, 1)}
        with ThreadPoolExecutor(6) as ex:
            for r in ex.map(pruefe, enumerate(kteile, 1)):
                kontext.update(r)

    ergebnis = {}
    for k in ids:
        p = punkte.get(k, [0, 0])
        kt = kontext.get(k, {})
        ok = sum(p) >= 2 or kt.get("urteil") == "passt"
        ergebnis[k] = {"name": info(k)["name"], "punkte": p, "blind": blind[k], "kontext": kt or None,
                       "ergebnis": "bestanden" if ok else ("schwach" if kt.get("urteil") == "schwach" else "durchgefallen")}
    (out / "ergebnis.json").write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1), encoding="utf-8")
    z = {s: sum(v["ergebnis"] == s for v in ergebnis.values()) for s in ("bestanden", "schwach", "durchgefallen")}
    print(z)
    for k, v in ergebnis.items():
        if v["ergebnis"] != "bestanden":
            print(f"{k} «{v['name']}» {v['ergebnis']}: blind {[b.get('begriff') for b in v['blind'] if b]}; "
                  f"Kontext {v['kontext']}")


if __name__ == "__main__":
    main()
