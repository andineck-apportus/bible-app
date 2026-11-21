#!/usr/bin/env python3
"""Pilot «Visuelle Sprache» (Analyse 2026-11-21): Vignetten im Aquarellstil malen, ohne Prüfung und ohne Übernahme.

Aufrufe aus der Action «bilder-aquarell», Schritt «pilot-visuell»:
  python3 pilot/visuell/malen.py --auftraege pilot/visuell/auftraege.json [--nur id,id]
Ergebnis: ausgabe/aquarell/<lauf>/<id>.png (die Action sichert es auf dem Branch bildpilot-ausgabe).
"""
import argparse
import datetime
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/authoring"))
import bilder_aquarell_gen as G  # noqa: E402

VIGNETTE = ("A single small vignette, not a scene filling the sheet: the subject sits in the middle of a large area of untouched warm "
            "white paper and fades out softly at its edges. No frame, no border, no lettering of any kind, no halo, no glowing light, "
            "no rays. God is never shown as a figure, face or hand.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--auftraege", default=str(ROOT / "pilot/visuell/auftraege.json"))
    ap.add_argument("--nur", default="")
    ap.add_argument("--varianten", type=int, default=1)
    a = ap.parse_args()
    schluessel = os.environ["OPENAI_API_KEY"]
    fig = json.loads((ROOT / "scripts/authoring/bilder_aquarell_daten/figuren.json").read_text(encoding="utf-8"))
    auf = json.loads(pathlib.Path(a.auftraege).read_text(encoding="utf-8"))["auftraege"]
    nur = {x.strip() for x in a.nur.split(",") if x.strip()}
    out = ROOT / "ausgabe/aquarell" / (datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%S") + "-pilot-visuell")
    out.mkdir(parents=True, exist_ok=True)
    for x in auf:
        if nur and x["id"] not in nur:
            continue
        prompt = f"{x['bild_en']}\n\n{VIGNETTE}\n\nSTYLE: {fig['stil_en']}\n\nThe attached image shows the drawing style only (use its line, wash, palette and white space; ignore its content and layout)."
        try:
            m, bilder = G.male(prompt, [G.STILREF], schluessel, a.varianten)
        except Exception as ex:
            print(f"::warning::{x['id']}: {ex}")
            continue
        for k, b in enumerate(bilder, 1):
            (out / f"{x['id']}{'' if a.varianten == 1 else f'__v{k}'}.png").write_bytes(b)
        print(x["id"], m)
    (out / "auftraege.json").write_text(json.dumps(auf, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
