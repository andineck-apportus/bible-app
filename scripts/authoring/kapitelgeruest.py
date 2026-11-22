#!/usr/bin/env python3
"""Kapitelgerüst: Merkbilder je Kapitel im Aquarellstil (Entscheid Andi Neck 2026-11-22, docs/ENTSCHEIDUNGEN.md «Merkbilder»).

Ein Merkbild je Kapitel folgt genau den Feldern des Bildauftrags BRIEF-<BUCH>-<KKK> (Stelle, Handlung, Stichwortband) und malt
jedes Feld als Szene. Damit sich die Kapitel im Gedächtnis nicht vermischen, hat jedes Kapitel eine eigene Grundfarbe (Palette),
die sich von den Nachbarkapiteln deutlich unterscheidet; die App nimmt dieselbe Farbe für die Kapitelleiste.

Quelle: scripts/authoring/bilder_aquarell_daten/kapitel/<BUCH>.json (Format FORMAT unten). Daraus entsteht der Szenenplan
scripts/authoring/bilder_aquarell_daten/szenen-kap-<buch>.json. Pflichtfragen fragen nur nach Sichtbarem (wer, was, wo, Haltung), nie nach Material oder Stoff (Sacktuch, Leinen): eine lockere
Aquarellskizze zeigt das nicht eindeutig (Jona 3,10, Lauf 90). Belege und Pflichtregeln werden aus dem Bildauftrag abgeleitet:
B-Beleg = Handlung des Feldes mit Stelle; Pflichtregel = «kern_en» (was sichtbar sein muss). Gott wird nicht gemalt
(docs/BILDSTIL.md); handelt im Feld Gott, beschreibt «moment_de» die sichtbare Folge, an der die Prüfung das Bild misst; Personen ohne Wiederkehr malt das Bild als gewöhnliche Menschen, ihr Name steht als Namensschild
(personen.py), ihre Malbeschreibung steht in «figuren».

    python3 scripts/authoring/kapitelgeruest.py pruefen [BUCH …]
    python3 scripts/authoring/kapitelgeruest.py schreiben [BUCH …]
    python3 scripts/authoring/kapitelgeruest.py felder BUCH        # Felder der Bildaufträge zum Schreiben der Quelle
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
QUELLE = DATEN / "kapitel"
BRIEFS = ROOT / "data/illustrations/briefs"
LEX = ROOT / "data/illustrations/lexicon"

FORMAT = """
{
  "buch": "JON",
  "quelle_de": "woher die Felder stammen (Bildaufträge der Kapitel)",
  "figuren": {"FIG-…": "English painting description (für Figuren ohne eigene Beschreibung im Stil, z. B. Personen nur mit Namensschild)"},
  "kapitel": {
    "1": {"palette": "graublau",
          "note_de": "Bildhinweis 1–2 Sätze mit [[JON.1.1]]: was gezeigt, was weggelassen, was gedeutet ist",
          "felder": [{"bild_en": "Malauftrag Englisch (≥ 150 Zeichen)", "depicts": ["FIG-…"], "kern_en": "Ja-Frage: was sichtbar sein muss?",
                      "kern_de": "dasselbe kurz deutsch"}]}
  }
}
"""

# Paletten der Merkbilder: deutlich verschieden, für Aquarell auf warmweissem Papier; hex = Farbe der Kapitelleiste in der App
PALETTEN = {
    "ocker": ("warm ochre, sand and terracotta", "#D9A441"),
    "graublau": ("cool grey-blue and slate, with sea-green accents", "#5E86A8"),
    "gruen": ("fresh spring green and olive", "#6FA35A"),
    "rot": ("deep madder red and warm rose", "#C2554B"),
    "violett": ("dusky violet and lavender", "#8A6BAE"),
    "tuerkis": ("clear turquoise and teal", "#2E9A9A"),
    "gold": ("golden yellow and amber light", "#E0B32E"),
    "nacht": ("deep indigo night blue with a few warm lamp lights", "#2F3E6B"),
    "braun": ("earthy umber brown and stone grey", "#8A6A4A"),
    "rosa": ("soft dawn pink and peach", "#E39A8E"),
}


def lade(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))


def briefs(buch):
    out = {}
    for p in sorted(BRIEFS.glob(f"BRIEF-{buch}-[0-9][0-9][0-9].json")):
        b = lade(p)
        if b.get("level") == "chapter":
            out[int(p.stem.rsplit("-", 1)[1])] = b
    return out


def beschrieben():
    st = lade(ROOT / "data/illustrations/styles/ILLSTYLE-AQUARELL.json").get("renderings") or {}
    return {k for k, v in st.items() if v.get("description_en")} | set(lade(DATEN / "figuren.json")["figuren"])


def pruefe(d, buch):
    f = []
    br = briefs(buch)
    if d.get("buch") != buch:
        f.append("buch passt nicht zum Dateinamen")
    besch = beschrieben() | set(d.get("figuren") or {})
    lex = {p.stem for p in LEX.glob("FIG-*.json")}
    vorher = None
    for k, kap in sorted((d.get("kapitel") or {}).items(), key=lambda x: int(x[0])):
        n = int(k)
        b = br.get(n)
        if not b:
            f.append(f"Kapitel {k}: kein Bildauftrag BRIEF-{buch}-{n:03d}")
            continue
        if kap.get("palette") not in PALETTEN:
            f.append(f"Kapitel {k}: palette {kap.get('palette')!r} unbekannt ({', '.join(PALETTEN)})")
        if vorher is not None and kap.get("palette") == vorher:
            f.append(f"Kapitel {k}: gleiche Palette wie das Kapitel davor")
        vorher = kap.get("palette")
        if not kap.get("note_de"):
            f.append(f"Kapitel {k}: note_de fehlt")
        fe = kap.get("felder") or []
        if len(fe) != len(b["panels"]):
            f.append(f"Kapitel {k}: {len(fe)} Felder, der Bildauftrag hat {len(b['panels'])}")
        for i, x in enumerate(fe, 1):
            if len(x.get("bild_en") or "") < 150:
                f.append(f"Kapitel {k} Feld {i}: bild_en fehlt oder zu kurz")
            if i <= len(b["panels"]):   # Stichwortband höchstens 54 Zeichen (bilder_aquarell.BAND_MAX), sonst «band» mit Wortlaut aus dem Text
                kw = x.get("band") or b["panels"][i - 1].get("keywords") or {}
                for lg in ("de", "gsw"):
                    if len(kw.get(lg) or "") > 54:
                        f.append(f"Kapitel {k} Feld {i}: Band ({lg}) länger als 54 Zeichen – «band» setzen")
            if not x.get("kern_en", "").endswith("?") or not x.get("kern_de"):
                f.append(f"Kapitel {k} Feld {i}: kern_en (Ja-Frage) und kern_de nötig")
            for fid in x.get("depicts") or []:
                if fid == "FIG-GOTT":
                    f.append(f"Kapitel {k} Feld {i}: Gott wird nicht gemalt")
                elif fid not in lex:
                    f.append(f"Kapitel {k} Feld {i}: {fid} nicht im Bildlexikon")
                elif fid not in besch:
                    f.append(f"Kapitel {k} Feld {i}: {fid} ohne Malbeschreibung (in figuren beschreiben)")
    return f


def schreibe(buch, d):
    br = briefs(buch)
    code = buch.lower()
    trans = sorted(p.stem for p in (ROOT / "data/translations").glob(f"TRANS-{buch}-*-WORKING.json"))
    tag = next((p.stem for p in (ROOT / "data/tags").glob("TAG-*.json") if lade(p).get("book") == buch), None)
    bilder, szenen = [], {}
    for k, kap in sorted(d["kapitel"].items(), key=lambda x: int(x[0])):
        n = int(k)
        b = br[n]
        pal, hexf = PALETTEN[kap["palette"]]
        ids = []
        for i, (x, pa) in enumerate(zip(kap["felder"], b["panels"]), 1):
            sid = f"{buch}-{n:03d}-M{i}"
            ids.append(sid)
            szenen[sid] = {
                "brief": b["id"], "panel": i, "reference": pa["reference"], "form": "szene",
                "form_grund_de": "Merkbild des Kapitels: erzählter Moment, gemalt (docs/ENTSCHEIDUNGEN.md «Merkbilder»).",
                "depicts": x.get("depicts", []),
                "bild_en": x["bild_en"].rstrip() + f" COLOUR OF THIS CHAPTER: the whole picture is dominated by {pal}; keep the rest of the palette quiet.",
                "speech": [],
                **({"band": x["band"]} if x.get("band") else {}),
                # Handelt im Feld Gott (wird nicht gemalt), beschreibt «moment_de» die sichtbare Folge; daran misst die Prüfung das Bild
                **({"moment_de": x["moment_de"]} if x.get("moment_de") else {}),   # Band gekürzt, wenn das Stichwort des Bildauftrags zu lang ist
                "evidence": [{"s": "B", "ref": pa["reference"], "de": pa["action_de"]},
                             {"s": "R", "de": "Kleidung, Landschaft, Gegenstände: plausible Ausgestaltung nach Epoche und Ort."},
                             {"s": "I", "de": "Gesichtsausdruck, Haltung und Grundfarbe des Kapitels: gestaltet, vom Text nicht genannt."}],
                "pruefung": [{"id": f"M{i}-KERN", "art": "muss", "stufe": "pflicht", "s": "B", "ref": pa["reference"], "de": x["kern_de"], "en": x["kern_en"]}]
                            + (x.get("pruefung") or []),
            }
        bilder.append({"id": f"ILL-AQU-{buch}-{n:03d}", "brief": b["id"], "level": "chapter", "reference": f"{buch}.{n}",
                       "target": b.get("target") or f"SUM-CH-{buch}-{n:03d}", "felder": ids, "note_de": kap["note_de"],
                       "merkbild": {"palette": kap["palette"], "farbe": hexf}})
    # Malbeschreibungen: eigene (Quelle), sonst die des Bildlexikons im Stil (dieselbe wie beim Einzelporträt), damit Figuren gleich aussehen
    st = lade(ROOT / "data/illustrations/styles/ILLSTYLE-AQUARELL.json").get("renderings") or {}
    allg = lade(DATEN / "figuren.json")["figuren"]
    figuren = dict(d.get("figuren") or {})
    for sz in szenen.values():
        for fid in sz["depicts"]:
            if fid not in figuren and fid not in allg and (st.get(fid) or {}).get("description_en"):
                figuren[fid] = st[fid]["description_en"]
    plan = {"_hinweis": f"Kapitelgerüst {buch} (scripts/authoring/kapitelgeruest.py aus kapitel/{buch}.json): ein Merkbild je Kapitel, "
                        "Felder nach dem Bildauftrag, eigene Grundfarbe je Kapitel.",
            "basis": trans, "tags": [tag] if tag else [], "figurenblatt": None,
            "figuren": figuren, "kenn_en": d.get("kenn_en", {}), "pruef": d.get("pruef", {}),
            "bilder": bilder, "szenen": szenen}
    (DATEN / f"szenen-kap-{code}.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return list(szenen)


def felder(buch):
    for n, b in sorted(briefs(buch).items()):
        print(f"## Kapitel {n} ({b['reference']})")
        for pa in b["panels"]:
            print(f"  {pa['n']} {pa['reference']} «{pa['keywords']['de']}» fig {pa.get('figures')} obj {pa.get('objects')}\n     {pa['action_de']}")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("pruefen", "schreiben", "felder"):
        print(__doc__ + "\nFormat:" + FORMAT)
        sys.exit(1)
    if sys.argv[1] == "felder":
        felder(sys.argv[2].upper())
        return
    buecher = [b.upper() for b in sys.argv[2:]] or sorted(p.stem for p in QUELLE.glob("*.json"))
    ok = True
    for b in buecher:
        d = lade(QUELLE / f"{b}.json")
        f = pruefe(d, b)
        if f:
            ok = False
            print(f"{b}: {len(f)} Fehler\n  " + "\n  ".join(f))
            continue
        print(f"{b}: in Ordnung ({len(d['kapitel'])} Kapitel)")
        if sys.argv[1] == "schreiben":
            print("  Szenen: " + ",".join(schreibe(b, d)))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
