#!/usr/bin/env python3
"""Bilder im Aquarellstil malen lassen (docs/BILDSTIL.md) – läuft in der GitHub-Action «bilder-aquarell» mit OPENAI_API_KEY.

Schritte:
  figurenblatt  Figuren- und Objektblatt im Stil der Referenz (docs/referenz/stilreferenz-aquarell-comic.jpg)
  felder        je Szene ein Bild; als Vorlage gehen Stilreferenz und Figurenblatt mit
                (data/illustrations/aquarell/figurenblatt.webp, sobald ausgewählt und abgelegt)

  python3 scripts/authoring/bilder_aquarell_gen.py figurenblatt --varianten 2
  python3 scripts/authoring/bilder_aquarell_gen.py felder --szenen JHN-002-K1,JHN-002-K2 --varianten 2
  python3 scripts/authoring/bilder_aquarell_gen.py felder --trocken          # nur Aufträge ausgeben

Ergebnis: ausgabe/aquarell/<lauf>/ mit PNG-Bildern, lauf.json (Auftrag, Modell, Zeit) und kontaktbogen.html.
Die Auswahl und das Ablegen in data/ macht danach scripts/authoring/bilder_aquarell.py.
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
import uuid

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
STILREF = ROOT / "docs/referenz/stilreferenz-aquarell-comic.jpg"
FIGBLATT = ROOT / "data/illustrations/aquarell/figurenblatt.webp"
MODELLE = ["gpt-image-2.5-flare", "gpt-image-2", "gpt-image-1.5", "gpt-image-1"]
API = "https://api.openai.com/v1/images"


def melde(text):
    print(text, file=sys.stderr)
    if os.environ.get("GITHUB_ACTIONS"):
        print("::error::" + text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A"))


def lade(name):
    return json.loads((DATEN / name).read_text(encoding="utf-8"))


def auftrag_figurenblatt(fig):
    leute = "\n".join(f"- {fig['figuren'][k]}" for k in ("FIG-MARIA-MUTTER-JESU", "FIG-JESUS", "FIG-ROLLE-SPEISEMEISTER", "FIG-ROLLE-BRAEUTIGAM", "FIG-GRUPPE-DIENER", "FIG-GRUPPE-JUENGER"))
    return (f"{fig['figurenblatt_en']}\n\nPEOPLE:\n{leute}\n\nSTYLE (match the drawing style of the attached reference image only – "
            f"its line, wash, palette and white space; ignore its content, layout, ages and text): {fig['stil_en']}")


def vorlagen_fuer(plan_d):
    """Stilreferenz und, wenn der Plan es nicht abschaltet («figurenblatt»: null) oder ein eigenes nennt, das Figurenblatt."""
    fb = plan_d.get("figurenblatt", "data/illustrations/aquarell/figurenblatt.webp")
    return [STILREF] + ([ROOT / fb] if fb and (ROOT / fb).is_file() else [])


def auftrag_feld(sz, fig, mit_blatt=None):
    ids = list(dict.fromkeys([*sz["depicts"], *[x for sp in sz["speech"] for x in (sp["from"], sp["to"])]]))
    leute = "\n".join(f"- {fig['figuren'][k]}" for k in ids if k in fig["figuren"])
    def wer(f):
        return fig["figuren"].get(f, f).split(":")[0]
    sprecher = "".join(f"\n- {wer(sp['from'])} is thinking (shown through face and gaze)." if sp.get("denken") else
                       f"\n- {wer(sp['from'])} are talking to each other (shown through gaze and gesture)." if sp["from"] == sp["to"] else
                       f"\n- {wer(sp['from'])} is speaking to {wer(sp['to']).lower()} (shown through gaze and gesture)." for sp in sz["speech"])
    vorlagen = ("The first attached image shows the drawing style (use only its style). "
                + ("The second attached image is the character sheet: use it only to know who is who (face shape, hair, beard, age, clothing colours) – not for its level of detail; paint everyone much simpler and looser than on the sheet." if (FIGBLATT.is_file() if mit_blatt is None else mit_blatt) else ""))
    return (f"{sz['bild_en']}\n\nPEOPLE AND OBJECTS (keep exactly):\n{leute}\n"
            + (f"\nWHO SPEAKS:{sprecher}\n" if sprecher else "")
            + f"\nPICTURE: {fig['bild_en']}\n\nSTYLE: {fig['stil_en']}\n\n{vorlagen}")


def multipart(felder, dateien):
    grenze = uuid.uuid4().hex
    teile = []
    for k, v in felder.items():
        teile.append(f'--{grenze}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    for k, pfad in dateien:
        typ = "image/jpeg" if pfad.suffix == ".jpg" else "image/webp" if pfad.suffix == ".webp" else "image/png"
        teile.append(f'--{grenze}\r\nContent-Disposition: form-data; name="{k}"; filename="{pfad.name}"\r\nContent-Type: {typ}\r\n\r\n'.encode() + pfad.read_bytes() + b"\r\n")
    teile.append(f"--{grenze}--\r\n".encode())
    return b"".join(teile), f"multipart/form-data; boundary={grenze}"


def male(prompt, vorlagen, schluessel, n):
    letzter = None
    modelle = [os.environ["OPENAI_IMAGE_MODEL"]] if os.environ.get("OPENAI_IMAGE_MODEL") else MODELLE
    for m in modelle:
        felder = {"model": m, "prompt": prompt, "size": "1536x1024", "quality": "high", "n": str(n)}
        if vorlagen:
            daten, typ = multipart(felder, [("image[]", p) for p in vorlagen])
            req = urllib.request.Request(f"{API}/edits", data=daten, headers={"Authorization": f"Bearer {schluessel}", "Content-Type": typ})
        else:  # ohne Vorlage (Stilprobe C): Bild nur aus dem Text
            req = urllib.request.Request(f"{API}/generations", data=json.dumps({**felder, "n": n}).encode(),
                                         headers={"Authorization": f"Bearer {schluessel}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=900) as r:
                d = json.loads(r.read())
            return m, [base64.b64decode(x["b64_json"]) for x in d["data"]]
        except urllib.error.HTTPError as e:
            letzter = f"HTTP {e.code} ({m}): {e.read().decode(errors='replace')[:500]}"
            if e.code in (400, 404) and "model" in letzter.lower():
                continue
            raise RuntimeError(letzter) from None
    raise RuntimeError(f"Kein Bildmodell verfügbar. Zuletzt: {letzter}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("schritt", choices=["figurenblatt", "felder"])
    ap.add_argument("--szenen", default="alle")
    ap.add_argument("--plan", default="szenen-jhn-002.json")
    ap.add_argument("--varianten", type=int, default=1)
    ap.add_argument("--hinweis", default="", help="zusätzliche Anweisung für diesen Lauf (Englisch)")
    ap.add_argument("--ohne-figurenblatt", action="store_true", help="nur die Stilreferenz als Vorlage (z. B. für einen neuen Stilversuch)")
    ap.add_argument("--trocken", action="store_true")
    a = ap.parse_args()
    fig = lade("figuren.json")
    if a.schritt == "figurenblatt":
        auftraege = [("FIGURENBLATT", auftrag_figurenblatt(fig), [STILREF])]
    else:
        plan = lade(a.plan)["szenen"]
        wahl = list(plan) if a.szenen == "alle" else [s.strip() for s in a.szenen.split(",") if s.strip()]
        fehlt = [s for s in wahl if s not in plan]
        if fehlt:
            sys.exit(f"Unbekannte Szenen: {fehlt}")
        vorlagen = [STILREF] + ([FIGBLATT] if FIGBLATT.is_file() and not a.ohne_figurenblatt else [])
        auftraege = [(s, auftrag_feld(plan[s], fig), vorlagen) for s in wahl]
    if a.hinweis:
        auftraege = [(i, p + f"\n\nADDITIONAL INSTRUCTION FOR THIS RUN: {a.hinweis}", v) for i, p, v in auftraege]
    if a.trocken:
        for i, p, v in auftraege:
            print(f"\n## {i} (Vorlagen: {', '.join(x.name for x in v)})\n{p}")
        return
    schluessel = os.environ.get("OPENAI_API_KEY")
    if not schluessel:
        melde("OPENAI_API_KEY fehlt.")
        sys.exit(1)
    lauf = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%S") + f"-aquarell-{a.schritt}"
    out = ROOT / "ausgabe/aquarell" / lauf
    out.mkdir(parents=True, exist_ok=True)
    eintraege, fehler = [], 0
    for i, p, v in auftraege:
        e = {"szene": i, "prompt": p, "vorlagen": [x.name for x in v]}
        try:
            m, bilder = male(p, v, schluessel, a.varianten)
            e["modell"], e["dateien"] = m, []
            for k, b in enumerate(bilder, 1):
                name = f"{i}__v{k}.png"
                (out / name).write_bytes(b)
                e["dateien"].append(name)
            print("ok   ", i, m, len(bilder))
        except Exception as ex:
            e["fehler"] = str(ex)
            fehler += 1
            melde(f"{i}: {ex}")
        eintraege.append(e)
    (out / "lauf.json").write_text(json.dumps({"lauf": lauf, "erzeugt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                                               "bilder": eintraege}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    zellen = "".join(f'<h2>{html.escape(e["szene"])}</h2>' + "".join(f'<img src="{d}" alt="">' for d in e.get("dateien", [])) + (f'<p>{html.escape(e["fehler"])}</p>' if e.get("fehler") else "") for e in eintraege)
    (out / "kontaktbogen.html").write_text(f'<!doctype html><meta charset="utf-8"><title>{lauf}</title><style>body{{font:15px system-ui;margin:16px}}img{{width:min(100%,768px);margin:4px}}</style><h1>{lauf}</h1>{zellen}', encoding="utf-8")
    print(f"\n{len(eintraege) - fehler} von {len(eintraege)} Aufträgen erledigt → {out}")
    if fehler == len(eintraege):
        sys.exit(1)


if __name__ == "__main__":
    main()
