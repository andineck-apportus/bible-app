#!/usr/bin/env python3
"""Pilot strukturierte Inhalte: Aquarell-Unterlagen und Vignetten malen (Action «bildpilot-struktur», OPENAI_API_KEY).

Liest pilot/struktur/vorlagen/auftraege.json. Aufträge mit Vorlage gehen an den Edits-Endpunkt (Vorlage + Stilreferenz),
die anderen ebenfalls an Edits mit der Stilreferenz allein. Danach misst das Skript, wie genau die gemalte Unterlage der
exakten Vorlage folgt (Kantenvergleich, Werte 0–1), damit die Datenebene nicht danebenliegt.
Ergebnis: pilot/struktur/ausgabe/<lauf>/<name>.png, lauf.json.
"""
import datetime
import json
import os
import pathlib
import sys

HIER = pathlib.Path(__file__).resolve().parent
REPO = HIER.parent.parent
sys.path.insert(0, str(REPO / "scripts/authoring"))
import bilder_aquarell_gen as G  # noqa: E402


def kanten(pfad, groesse):
    import numpy as np
    from PIL import Image, ImageFilter
    im = Image.open(pfad).convert("L").resize(groesse).filter(ImageFilter.GaussianBlur(2)).filter(ImageFilter.FIND_EDGES)
    a = np.asarray(im, dtype=float)
    return a > np.percentile(a, 90)


def deckung(vorlage, bild):
    """Anteil der Vorlagenkanten, die im gemalten Bild innerhalb von ±6 px eine Kante haben (Formtreue)."""
    import numpy as np
    from PIL import Image
    g = (300, 300)
    v, b = kanten(vorlage, g), kanten(bild, g)
    bb = np.asarray(Image.fromarray((b * 255).astype("uint8")).filter(__import__("PIL.ImageFilter", fromlist=["x"]).MaxFilter(7))) > 0
    return round(float((v & bb).sum() / max(1, v.sum())), 3)


def main():
    nur = sys.argv[1].split(",") if len(sys.argv) > 1 and sys.argv[1] != "alle" else None
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    auftraege = json.loads((HIER / "vorlagen/auftraege.json").read_text(encoding="utf-8"))
    schluessel = os.environ["OPENAI_API_KEY"]
    lauf = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%S") + "-struktur"
    out = HIER / "ausgabe" / lauf
    out.mkdir(parents=True, exist_ok=True)
    eintraege = []
    for name, a in auftraege.items():
        if nur and not any(name.startswith(x) for x in nur):
            continue
        vorlagen = ([HIER / a["vorlage"]] if a["vorlage"] else []) + [G.STILREF]
        prompt = a["prompt"] + ("\n\nThe FIRST attached image is the exact template (keep its geometry). The SECOND shows the painting style only." if a["vorlage"]
                                else "\n\nThe attached image shows the painting style only (ignore its content).")
        e = {"name": name, "prompt": prompt}
        try:
            m, bilder = G.male(prompt, vorlagen, schluessel, n)
            e["modell"], e["dateien"] = m, []
            for k, b in enumerate(bilder, 1):
                datei = f"{name}.png" if k == 1 else f"{name}__v{k}.png"
                (out / datei).write_bytes(b)
                e["dateien"].append(datei)
                if a["vorlage"]:
                    e.setdefault("deckung", {})[datei] = deckung(HIER / a["vorlage"], out / datei)
            print("ok", name, e.get("deckung", ""))
        except Exception as ex:
            e["fehler"] = str(ex)
            G.melde(f"{name}: {ex}")
        eintraege.append(e)
    (out / "lauf.json").write_text(json.dumps({"lauf": lauf, "bilder": eintraege}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
