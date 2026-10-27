#!/usr/bin/env python3
"""Pilot «Comic-Seite je Abschnitt» (Stil 4: reduzierter Aquarell-Comic) mit dem Bildmodell von OpenAI.

Je Abschnitt eine Comic-Seite aus:
- dem Lesetext des Abschnitts (data/translations/…, Hochdeutsch bzw. Züridüütsch),
- dem Bildauftrag (Pflichtmomente in Reihenfolge),
- dem Figurenblatt (figuren.json: Aussehen, Alter, Farben nach Bildlexikon).

Varianten (--varianten):
  leer  Sprechblasen und Erzählkästen leer – die App setzt den Text darüber (ein Bild für alle Sprachen)
  de    Text auf Hochdeutsch im Bild
  gsw   Text auf Züridüütsch im Bild

Aufruf: OPENAI_API_KEY=… python3 pilot/comic/comic.py [--abschnitte 001-012,013-022] [--varianten leer,de] [--trocken]
Modell: OPENAI_IMAGE_MODEL oder der erste verfügbare aus MODELLE.
"""
import argparse
import base64
import datetime
import html
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

HIER = pathlib.Path(__file__).resolve().parent
REPO = HIER.parent.parent
DATA = REPO / "data"
MODELLE = ["gpt-image-2.5-flare", "gpt-image-2", "gpt-image-1.5", "gpt-image-1"]
TEXTE = {
    "de": DATA / "translations/TRANS-JHN-002-001-025-DE-WORKING.json",
    "gsw": DATA / "translations/TRANS-JHN-002-001-025-GSW-ZH-WORKING.json",
}
SPRACHNAME = {"de": "Standard German (Swiss spelling: ss instead of ß)", "gsw": "Zurich Swiss German dialect (Züridüütsch)"}


def melde(text):
    print(text, file=sys.stderr)
    if os.environ.get("GITHUB_ACTIONS"):
        print("::error::" + text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A"))


def verse(sprache, von, bis):
    t = json.loads(TEXTE[sprache].read_text(encoding="utf-8"))["text_by_reference"]
    return [(f"2,{v}", t[f"JHN.2.{v}"]) for v in range(von, bis + 1) if f"JHN.2.{v}" in t]


def prompt_fuer(abschnitt, variante, figuren, stil):
    von, bis = (int(x) for x in abschnitt.split("-"))
    brief = json.loads((DATA / f"illustrations/briefs/BRIEF-JHN-002-{abschnitt}.json").read_text(encoding="utf-8"))
    vorkommend = {f for p in brief["panels"] for f in p["figures"]} | set(figuren["immer"]) | set(figuren["zusatz"].get(abschnitt, []))
    sprache = "de" if variante == "leer" else variante
    text = "\n".join(f"{ref} {satz}" for ref, satz in verse(sprache, von, bis))
    momente = "\n".join(f"{i}. {p['action_de']}" for i, p in enumerate(brief["panels"], 1))
    leute = "\n".join(f"- {figuren['figuren'][f]}" for f in figuren["reihenfolge"] if f in vorkommend and f in figuren["figuren"])
    if variante == "leer":
        schrift = ("Draw the speech bubbles and caption boxes where they belong, each tail pointing clearly at the person speaking, "
                   "but leave every bubble and every caption box completely blank and white. There is no lettering anywhere in the image: "
                   "the app adds the words later in the reader's language, so leave enough empty space inside each bubble for a short sentence.")
    else:
        schrift = (f"Speech bubbles and caption boxes contain short quotes taken word for word from the text below, in {SPRACHNAME[variante]}. "
                   "Copy the wording and spelling exactly, letter by letter, in clear hand-lettered comic type. Use only quotes that appear in the text.")
    return f"""A single comic page telling John 2:{von}–{bis} as a sequence of panels, read left to right, top to bottom.

STYLE: {stil}

STORY (the biblical text this page tells – follow it faithfully, in this order):
{text}

KEY MOMENTS that must each get at least one panel, in this order (German descriptions):
{momente}

Split the story into 6 to 9 panels of varying size on a clean grid with thin gutters. Show who speaks to whom through gaze and gesture. Vary the camera: establishing shot, medium shots, close-ups on faces for emotional moments.

CHARACTERS (keep each one identical in every panel):
{leute}
{figuren['regeln']}

LETTERING: {schrift}"""


def bild(prompt, schluessel, modelle):
    letzter = None
    for m in modelle:
        body = {"model": m, "prompt": prompt, "size": "1536x1024", "quality": "high", "n": 1}
        req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=json.dumps(body).encode(),
                                     headers={"Authorization": f"Bearer {schluessel}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                d = json.loads(r.read())
            return m, base64.b64decode(d["data"][0]["b64_json"])
        except urllib.error.HTTPError as e:
            letzter = f"HTTP {e.code} ({m}): {e.read().decode(errors='replace')[:400]}"
            if e.code in (400, 404) and "model" in letzter.lower():
                continue  # Modell nicht verfügbar → nächstes probieren
            raise RuntimeError(letzter) from None
    raise RuntimeError(f"Kein Bildmodell verfügbar. Zuletzt: {letzter}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--abschnitte", default="001-012,013-022,023-025")
    ap.add_argument("--varianten", default="leer,de")
    ap.add_argument("--trocken", action="store_true")
    a = ap.parse_args()
    figuren = json.loads((HIER / "figuren.json").read_text(encoding="utf-8"))
    stil = figuren["stil"]
    auftraege = [(ab.strip(), v.strip()) for ab in a.abschnitte.split(",") if ab.strip() for v in a.varianten.split(",") if v.strip()]
    for _, v in auftraege:
        if v not in ("leer", "de", "gsw"):
            sys.exit(f"Unbekannte Variante: {v}")
    if a.trocken:
        for ab, v in auftraege:
            print(f"\n## {ab} · {v}\n{prompt_fuer(ab, v, figuren, stil)}")
        return
    schluessel = os.environ.get("OPENAI_API_KEY")
    if not schluessel:
        melde("OPENAI_API_KEY fehlt (als Umgebungsvariable bzw. GitHub-Secret hinterlegen).")
        sys.exit(1)
    modelle = [os.environ["OPENAI_IMAGE_MODEL"]] if os.environ.get("OPENAI_IMAGE_MODEL") else MODELLE
    lauf = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%S") + "-comic"
    out = HIER / "ausgabe" / lauf
    out.mkdir(parents=True, exist_ok=True)
    eintraege, fehler = [], 0
    for ab, v in auftraege:
        p = prompt_fuer(ab, v, figuren, stil)
        e = {"abschnitt": f"JHN.2.{int(ab.split('-')[0])}-JHN.2.{int(ab.split('-')[1])}", "brief": f"BRIEF-JHN-002-{ab}", "variante": v, "prompt": p}
        try:
            modell, daten = bild(p, schluessel, modelle)
            e["modell"], e["datei"] = modell, f"COMIC-JHN-002-{ab}__{v}.png"
            (out / e["datei"]).write_bytes(daten)
            print("ok   ", ab, v, modell)
        except Exception as ex:
            e["fehler"] = str(ex)
            fehler += 1
            melde(f"{ab} · {v}: {ex}")
        eintraege.append(e)
    (out / "lauf.json").write_text(json.dumps({"lauf": lauf, "hinweis_de": "KI-generierte Pilot-Comicseiten, nicht geprüft und nicht in der App. Bildliche Deutung.",
                                               "bilder": eintraege}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    zellen = "".join(f'<figure><img src="{html.escape(e["datei"])}" alt=""><figcaption>{e["abschnitt"]} · {e["variante"]} · {e.get("modell", "")}</figcaption></figure>'
                     if e.get("datei") else f'<figure><figcaption>{e["abschnitt"]} · {e["variante"]}: {html.escape(e["fehler"])}</figcaption></figure>' for e in eintraege)
    (out / "kontaktbogen.html").write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Comic-Pilot Johannes 2</title>'
                                           '<style>body{font:15px system-ui;margin:16px;background:#111;color:#eee}img{width:100%;border-radius:6px}figure{margin:0 0 24px}figcaption{color:#999}</style>'
                                           f'<h1>Comic-Pilot Johannes 2 – {lauf}</h1>{zellen}', encoding="utf-8")
    print(f"\n{len(eintraege) - fehler} von {len(eintraege)} Seiten erzeugt → {out}")
    if fehler == len(eintraege):
        sys.exit(1)


if __name__ == "__main__":
    main()
