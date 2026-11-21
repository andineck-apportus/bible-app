#!/usr/bin/env python3
"""Vignetten für Strukturbilder: kleine gemalte Bilder je Glied (Hybrid, docs/VISUELLE-SPRACHE.md «Daten zeichnen Anordnung, Zahlen
und Worte; das Bildmodell malt nur Figuren, Dinge und Landschaft»). Rückmeldung Andi Neck 2026-11-21: Strukturbilder nur mit Text
und Kästen sind schade; Bildchen für Dinge und Personen sollen dazukommen.

Daten: im Szenenplan je Element der Struktur (und bei «mitte») das Feld «vignette_en» (Englisch, was gemalt wird; Gott nie als
Figur, keine Licht- oder Strahleneffekte, keine Schrift). Ablage:
  data/illustrations/aquarell/img/vign/<Feld>-<Schlüssel>.webp     Bild (256 px, WebP)
  scripts/authoring/bilder_aquarell_daten/vignetten/<Feld>.json   je Schlüssel: sha des Auftrags, Datei, Prüfung
Schlüssel: Nummer des Elements (1, 2, …) oder «m» für die Mitte.

Prüfung je Vignette (zwei Instanzen wie bei den Szenen, hier als feste Fragen): zeigt das Bild den Auftrag; keine Schrift; kein
Heiligenschein, keine Licht- oder Strahleneffekte, keine Figur Gottes; nichts Modernes; kleine Vignette auf weissem Papier.

    python3 scripts/authoring/vignetten.py lauf --szenen GEN-B1,LEV-B4 [--runden 2]   # malen und prüfen (OPENAI_API_KEY)
    python3 scripts/authoring/vignetten.py stand                                      # offene und veraltete Vignetten
"""
import argparse
import datetime
import hashlib
import io
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/authoring"))
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
REG = DATEN / "vignetten"
IMG = ROOT / "data/illustrations/aquarell/img/vign"
PROZESS = "PROC-BILD-AQUARELL@2.5"
GROESSE = 256

VIGNETTE = ("A single small vignette, not a scene filling the sheet: the subject sits in the middle of a large area of untouched warm "
            "white paper and fades out softly at its edges. No frame, no border, no lettering of any kind, no halo, no glowing light, "
            "no rays. God is never shown as a figure, face or hand. Few details, clearly readable when shown very small.")

FRAGEN = [  # id, Frage, verlangte Antwort, Stufe
    ("V-INHALT", "Does the picture clearly show this: {en}", "yes", "pflicht"),
    ("V-SCHRIFT", "Is there any writing, letters, numbers or speech bubble in the picture?", "no", "pflicht"),
    ("V-EFFEKT", "Is there a halo, glowing light, light rays, sparkles or any figure, face or hand in the sky?", "no", "pflicht"),
    ("V-MODERN", "Is anything clearly modern visible (modern clothing, glasses, watches, plastic, machines, modern buildings)?", "no", "pflicht"),
    ("V-VIGNETTE", "Is this a small vignette in the middle of mostly empty white paper (rather than a picture filling the whole sheet)?", "yes", "soll"),
]


def sha(t):
    return hashlib.sha256(t.encode()).hexdigest()[:16]


def auftraege(nur=None):
    """(Feld, Schlüssel, Auftrag) aus allen Szenenplänen, in Reihenfolge."""
    for p in sorted(DATEN.glob("szenen-*.json")):
        for sid, sz in json.loads(p.read_text(encoding="utf-8"))["szenen"].items():
            if sz.get("form") != "struktur" or (nur and sid not in nur):
                continue
            sx = sz["struktur"]
            for k, e in enumerate(sx.get("elemente") or [], 1):
                if e.get("vignette_en"):
                    yield sid, str(k), e["vignette_en"]
            if (sx.get("mitte") or {}).get("vignette_en"):
                yield sid, "m", sx["mitte"]["vignette_en"]


def register(sid):
    p = REG / f"{sid}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def gueltig(sid):
    """Schlüssel → href (relativ zum Bildordner) für bestandene Vignetten, deren Auftrag unverändert ist."""
    r = register(sid)
    out = {}
    for s_id, k, en in auftraege({sid}):
        v = r.get(k)
        if v and v.get("sha") == sha(en) and v.get("ergebnis") == "bestanden" and (ROOT / "data/illustrations/aquarell" / v["datei"]).exists():
            out[k] = v["datei"]
    return out


def pruefe(schluessel, png, en):
    import bilder_pruefung as BP
    text = ("Answer each question about the picture with \"yes\", \"no\" or \"unclear\" and a short reason.\n"
            + "\n".join(f'{i}: {f.format(en=en)}' for i, f, _, _ in FRAGEN)
            + '\nReturn JSON: {"answers": {id: {"answer": "yes"|"no"|"unclear", "reason": "..."}}}')
    erg = []
    a1 = BP.frage(schluessel, BP.SYS_REGELN, text, png).get("answers", {})
    zweit = None
    for i, f, soll, stufe in FRAGEN:
        a = (a1.get(i) or {})
        ok = a.get("answer") == soll
        if not ok and stufe == "pflicht":  # Streitfall: zweite Instanz
            if zweit is None:
                zweit = BP.frage(schluessel, BP.SYS_REGELN, text, png, rolle="zweit").get("answers", {})
            b = zweit.get(i) or {}
            if b.get("answer") == soll:
                ok, a = True, {**b, "reason": f"zweite Instanz: {b.get('reason', '')}"}
        erg.append({"id": i, "stufe": stufe, "ergebnis": "ok" if ok else ("unklar" if a.get("answer") == "unclear" else "fehler"),
                    "antwort": a.get("answer"), "grund": a.get("reason", "")})
    bestanden = all(e["ergebnis"] == "ok" for e in erg if e["stufe"] == "pflicht")
    return {"ergebnis": "bestanden" if bestanden else "durchgefallen", "regeln": erg, "modell": BP.modelle(schluessel)}


def klein(png):
    from PIL import Image
    im = Image.open(io.BytesIO(png)).convert("RGB")
    im.thumbnail((GROESSE, GROESSE), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "WEBP", quality=82, method=6)
    return b.getvalue()


def lauf(a):
    import bilder_aquarell_gen as G
    schluessel = os.environ["OPENAI_API_KEY"]
    fig = json.loads((DATEN / "figuren.json").read_text(encoding="utf-8"))
    nur = None if a.szenen in ("", "alle") else {x.strip() for x in a.szenen.split(",") if x.strip()}
    jetzt = datetime.datetime.now(datetime.timezone.utc)
    out = ROOT / "ausgabe/aquarell" / (jetzt.strftime("%Y%m%d-%H%M%S") + "-auto-vignetten")
    out.mkdir(parents=True, exist_ok=True)
    IMG.mkdir(parents=True, exist_ok=True)
    REG.mkdir(parents=True, exist_ok=True)
    bericht = {}
    for sid, k, en in auftraege(nur):
        r = register(sid)
        if not a.erzwingen and (r.get(k) or {}).get("sha") == sha(en) and r[k].get("ergebnis") == "bestanden":
            continue
        prompt = f"{en}\n\n{VIGNETTE}\n\nSTYLE: {fig['stil_en']}\n\nThe attached image shows the drawing style only (use its line, wash, palette and white space; ignore its content and layout)."
        if a.hinweis:
            prompt += "\n\n" + a.hinweis
        gewaehlt, versuche = None, []
        for runde in range(1, a.runden + 1):
            try:
                _, bilder = G.male(prompt, [G.STILREF], schluessel, a.varianten, groesse="1024x1024", qualitaet="medium")
            except Exception as ex:
                print(f"::warning::{sid}-{k}: {ex}")
                break
            for v, png in enumerate(bilder, 1):
                name = f"{sid}-{k}__r{runde}v{v}.png"
                (out / name).write_bytes(png)
                pr = pruefe(schluessel, png, en)
                versuche.append({"datei": name, **pr})
                if pr["ergebnis"] == "bestanden":
                    gewaehlt = (png, pr)
                    break
            if gewaehlt:
                break
        eintrag = {"sha": sha(en), "auftrag_en": en, "datum": jetzt.date().isoformat(), "prozess": PROZESS}
        if gewaehlt:
            datei = f"img/vign/{sid}-{k}.webp"
            (ROOT / "data/illustrations/aquarell" / datei).write_bytes(klein(gewaehlt[0]))
            eintrag.update({"ergebnis": "bestanden", "datei": datei, "pruefung": gewaehlt[1]})
        else:
            eintrag.update({"ergebnis": "durchgefallen", "datei": None})
            print(f"::warning::{sid}-{k}: keine Variante bestanden")
        r[k] = eintrag
        (REG / f"{sid}.json").write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        bericht.setdefault(sid, {})[k] = {"auftrag_en": en, "versuche": versuche, "ergebnis": eintrag["ergebnis"]}
        print(sid, k, eintrag["ergebnis"])
    (out / "bericht.json").write_text(json.dumps(bericht, ensure_ascii=False, indent=2), encoding="utf-8")
    html = ["<!doctype html><meta charset=utf-8><title>Vignetten</title><body style='font-family:sans-serif'>"]
    for sid, ks in bericht.items():
        for k, b in ks.items():
            html.append(f"<h3>{sid}-{k}: {b['ergebnis']}</h3><p>{b['auftrag_en']}</p>")
            for v in b["versuche"]:
                html.append(f"<figure style='display:inline-block;width:260px'><img src='{v['datei']}' width=256><figcaption>{v['ergebnis']}: "
                            + "; ".join(f"{e['id']} {e['ergebnis']}" for e in v["regeln"] if e["ergebnis"] != "ok") + "</figcaption></figure>")
    (out / "bericht.html").write_text("".join(html), encoding="utf-8")
    import subprocess
    subprocess.run([sys.executable, str(ROOT / "scripts/authoring/bilder_aquarell.py")], check=True)


def stand(_a):
    offen = 0
    for sid, k, en in auftraege():
        v = register(sid).get(k)
        if not v or v.get("sha") != sha(en) or v.get("ergebnis") != "bestanden":
            offen += 1
            print(f"offen {sid}-{k}: {'veraltet' if v and v.get('sha') != sha(en) else (v or {}).get('ergebnis', 'neu')}")
    print(f"{offen} Vignetten offen")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("schritt", choices=["lauf", "stand"])
    ap.add_argument("--szenen", default="alle")
    ap.add_argument("--runden", type=int, default=2)
    ap.add_argument("--varianten", type=int, default=2)
    ap.add_argument("--hinweis", default="")
    ap.add_argument("--erzwingen", action="store_true")
    a = ap.parse_args()
    (lauf if a.schritt == "lauf" else stand)(a)


if __name__ == "__main__":
    main()
