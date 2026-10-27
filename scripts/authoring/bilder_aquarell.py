#!/usr/bin/env python3
"""Autorenwerkzeug: Bilder im Aquarellstil ablegen (docs/BILDSTIL.md).

1. Übernehmen (nach einem Lauf von bilder_aquarell_gen.py in der Action):
     python3 scripts/authoring/bilder_aquarell.py uebernehmen <lauf-ordner> JHN-002-K1=v2 JHN-002-K2=v1 …
   legt die gewählten Bilder als data/illustrations/aquarell/img/<Szene>.webp ab (960×640) und vermerkt die Herkunft
   in bilder_aquarell_daten/auswahl.json.
2. Schreiben:
     python3 scripts/authoring/bilder_aquarell.py
   schreibt Stil ILLSTYLE-AQUARELL und je Bild (Abschnitt, Kapitel) Datensatz und SVG: je Bildfeld eine Kachel mit dem
   Bild, darüber die Sprechblasen als Text je Sprache (Hochdeutsch, Züridüütsch) und darunter das Stichwortband aus dem
   Bildauftrag. Prüft, dass jede Blase wörtlich (bis auf … für Kürzungen) im Lesetext des genannten Verses steht.

Blasen: in auswahl.json je Szene «bubbles» (in der Reihenfolge von «speech» im Szenenplan): x, y, w (Rahmen oben links und
Breite, Bildkoordinaten 600×400) und tail (Spitze zeigt auf den Kopf der sprechenden Person).
"""
import datetime
import html
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
D = ROOT / "data/illustrations"
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
OUT = D / "aquarell"
DATE = os.environ.get("BIBLE_REVISION_DATE") or datetime.date.today().isoformat()
W, H = 600, 400          # Bildfläche je Kachel (Seitenverhältnis 3 : 2)
BAND = 46                # Stichwortband unter dem Bild
INK, PAPER = "#4A4D45", "#FBF8F1"
LIC = "CC0 1.0 (KI-generiert mit dem Bildmodell von OpenAI; keine Urheberrechte beansprucht)"
AUTH = (f"KI-Bild: gemalt mit dem Bildmodell von OpenAI nach Szenenplan, Figurenblatt und Stilreferenz (docs/BILDSTIL.md); "
        f"Auswahl, Blasen und Datensatz KI-Entwurf (Claude) vom {DATE} auf Wunsch von Andi Neck; keine fachliche Prüfung.")


def lade(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))


def schreibe(p, rec):
    p = pathlib.Path(p)
    neu = json.dumps(rec, ensure_ascii=False, indent=2) + "\n"
    if p.exists() and p.read_text(encoding="utf-8") == neu:
        return 0
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(neu, encoding="utf-8")
    return 1


def uebernehmen(lauf, wahl):
    from PIL import Image
    lauf = pathlib.Path(lauf)
    aus_p = DATEN / "auswahl.json"
    aus = lade(aus_p) if aus_p.exists() else {}
    meta = {e["szene"]: e for e in lade(lauf / "lauf.json")["bilder"]}
    for w in wahl:
        sz, var = w.split("=")
        src = lauf / f"{sz}__{var}.png"
        (OUT / "img").mkdir(parents=True, exist_ok=True)
        Image.open(src).convert("RGB").resize((960, 640), Image.LANCZOS).save(OUT / "img" / f"{sz}.webp", quality=80, method=6)
        alt = aus.get(sz, {})
        aus[sz] = {"datei": f"img/{sz}.webp", "lauf": lauf.name, "variante": var, "modell": meta[sz].get("modell"),
                   "bubbles": alt.get("bubbles", []), "uebernommen": DATE}
        print("übernommen", sz, var)
    aus_p.write_text(json.dumps(aus, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def norm(s):
    return " ".join(re.sub(r"[«»“”„\"'.,;:!?…–-]", " ", s.lower()).split())


def zeilen(text, breite, fs):
    """Umbruch nach geschätzter Zeichenbreite, ausgeglichen (keine einzelnen Wörter allein auf der letzten Zeile)."""
    def gierig(maxz):
        out, cur = [], ""
        for w in text.split():
            if cur and len(cur) + 1 + len(w) > maxz:
                out.append(cur)
                cur = w
            else:
                cur = f"{cur} {w}".strip()
        return out + ([cur] if cur else [])
    maxz = max(8, int(breite / (fs * 0.53)))
    best = gierig(maxz)
    for m in range(maxz - 1, 7, -1):  # schmaler setzen, solange die Zeilenzahl gleich bleibt
        t = gierig(m)
        if len(t) > len(best):
            break
        best = t
    return best


def blase(b, sp, n):
    fs = b.get("fs", 21)
    pad, lh = 14, fs + 4
    lines = {lg: zeilen(sp[lg], b["w"] - 2 * pad, fs) for lg in ("de", "gsw")}
    h = 2 * pad + lh * max(len(v) for v in lines.values()) - (lh - fs)
    x, y, w = b["x"], b["y"], b["w"]
    tx, ty = b["tail"]
    # Spitze: kurzer Keil von der Rahmenkante, die der sprechenden Person zugewandt ist
    if ty > y + h:
        cx = min(max(tx, x + 26), x + w - 26)
        base, shift = [(cx - 11, y + h - 1), (cx + 11, y + h - 1)], (0, -2)
    elif tx > x + w:
        cy = min(max(ty, y + 20), y + h - 20)
        base, shift = [(x + w - 1, cy - 11), (x + w - 1, cy + 11)], (-2, 0)
    elif tx < x:
        cy = min(max(ty, y + 20), y + h - 20)
        base, shift = [(x + 1, cy - 11), (x + 1, cy + 11)], (2, 0)
    else:
        cx = min(max(tx, x + 26), x + w - 26)
        base, shift = [(cx - 11, y + 1), (cx + 11, y + 1)], (0, 2)
    pts = " ".join(f"{u:.0f},{v:.0f}" for u, v in base) + f" {tx:.0f},{ty:.0f}"
    out = [f'<g class="ill-bubble" data-speech="{n}">',
           f'<polygon points="{pts}" fill="{PAPER}" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="18" fill="{PAPER}" fill-opacity=".94" stroke="{INK}" stroke-width="1.2"/>',
           f'<polygon points="{pts}" fill="{PAPER}" stroke="none" transform="translate({shift[0]} {shift[1]})"/>']
    for lg, ls in lines.items():
        y0 = y + pad + fs * 0.82 + (h - 2 * pad - (lh * len(ls) - (lh - fs))) / 2
        tsp = "".join(f'<tspan x="{x + w / 2:.1f}" y="{y0 + i * lh:.1f}">{html.escape(t)}</tspan>' for i, t in enumerate(ls))
        out.append(f'<text class="lw lw-{lg}" text-anchor="middle" font-family="sans-serif" font-size="{fs}" fill="#2F312C">{tsp}</text>')
    out.append("</g>")
    return "".join(out)


def band(n, kw):
    out = [f'<rect x="0" y="{H}" width="{W}" height="{BAND}" fill="{PAPER}"/>',
           f'<circle cx="24" cy="{H + BAND / 2}" r="12" fill="none" stroke="{INK}" stroke-width="1.4"/>',
           f'<text x="24" y="{H + BAND / 2 + 5}" text-anchor="middle" font-family="sans-serif" font-size="14" fill="{INK}" class="pn-n">{n}</text>']
    for lg in ("de", "gsw"):
        t = kw.get(lg) or kw.get("de") or ""
        fs = 19 if len(t) <= 46 else max(13, int(19 * 46 / len(t)))
        out.append(f'<text class="lw lw-{lg}" x="{(W + 40) / 2}" y="{H + BAND / 2 + fs * 0.36:.1f}" text-anchor="middle" font-family="sans-serif" font-size="{fs}" font-style="italic" fill="#3B3D37">{html.escape(t)}</text>')
    return "".join(out)


def kachel(i, sz_id, sz, aus, kw, x, y):
    a = aus[sz_id]
    teile = [f'<svg class="ill-tile" data-span="1" data-scene="{sz_id}" x="{x}" y="{y}" width="{W}" height="{H + BAND}" viewBox="0 0 {W} {H + BAND}">',
             f'<image href="{a["datei"]}" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="xMidYMid slice"/>']
    for n, (sp, b) in enumerate(zip(sz["speech"], a.get("bubbles", []))):
        teile.append(blase(b, sp, n))
    teile.append(band(i, kw))
    teile.append(f'<rect x=".5" y=".5" width="{W - 1}" height="{H + BAND - 1}" fill="none" stroke="#D8D0C0" stroke-width="1"/></svg>')
    return "".join(teile)


def pruefe_zitate(plan):
    texte = {"de": lade(ROOT / "data/translations/TRANS-JHN-002-001-025-DE-WORKING.json")["text_by_reference"],
             "gsw": lade(ROOT / "data/translations/TRANS-JHN-002-001-025-GSW-ZH-WORKING.json")["text_by_reference"]}
    fehler = []
    for sid, sz in plan.items():
        for sp in sz["speech"]:
            for lg in ("de", "gsw"):
                teile = [t for t in sp[lg].split("…") if t.strip()]
                if not all(norm(t) in norm(texte[lg][sp["ref"]]) for t in teile):
                    fehler.append(f"{sid}: «{sp[lg]}» steht so nicht in {sp['ref']} ({lg})")
    return fehler


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "uebernehmen":
        uebernehmen(sys.argv[2], sys.argv[3:])
        return
    plan_d = lade(DATEN / "szenen-jhn-002.json")
    plan, fig = plan_d["szenen"], lade(DATEN / "figuren.json")
    aus = lade(DATEN / "auswahl.json")
    fehler = pruefe_zitate(plan)
    if fehler:
        sys.exit("FEHLER Zitate:\n" + "\n".join(fehler))
    n = 0
    stil = {"id": "ILLSTYLE-AQUARELL", "type": "illustration_style", "status": "draft", "tags": ["TAG-JOHN"], "key": "aquarell",
            "labels": {"de": "Aquarell", "en": "Watercolour"},
            "description_de": "Minimalistischer Aquarell-Comic nach dem Styleguide «Visuelle Bibel» V1.2 (docs/BILDSTIL.md): warmweisses Papier, wenige dünne Linien, transparente Flächen, natürliche erwachsene Figuren, viel Weissraum. Gemalte Szenen je Bildfeld; Worte als Text darüber in der gewählten Sprache. Ersetzt in der App die Stile Symbol und Anime, wo vorhanden.",
            "style_reference": "docs/referenz/stilreferenz-aquarell-comic.jpg", "character_sheet": "data/illustrations/aquarell/figurenblatt.webp",
            "renderings": {k: {"description_en": v} for k, v in sorted(fig["figuren"].items())},
            "license": LIC, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
    alt_p = D / "styles/ILLSTYLE-AQUARELL.json"
    if alt_p.exists():
        alt = lade(alt_p)
        stil["knowledge"] = alt.get("knowledge", stil["knowledge"])
        stil["revision_log"] = alt.get("revision_log", [])
    n += schreibe(alt_p, stil)
    for b in plan_d["bilder"]:
        brief = lade(D / f"briefs/{b['brief']}.json")
        felder = [plan[s] for s in b["felder"]]
        fehlt = [s for s in b["felder"] if s not in aus]
        if fehlt:
            print(f"übersprungen {b['id']}: Bild fehlt für {fehlt}")
            continue
        if len(brief["panels"]) != len(b["felder"]):
            sys.exit(f"{b['id']}: {len(b['felder'])} Felder, Bildauftrag hat {len(brief['panels'])}")
        cols = 1 if len(b["felder"]) == 1 else 2
        rows = (len(b["felder"]) + cols - 1) // cols
        gap = 12
        tw, th = cols * W + (cols - 1) * gap, rows * (H + BAND) + (rows - 1) * gap
        tiles = []
        for i, (sid, p_) in enumerate(zip(b["felder"], brief["panels"]), 1):
            r_, c_ = divmod(i - 1, cols)
            x = c_ * (W + gap) + ((W + gap) // 2 if r_ == rows - 1 and len(b["felder"]) % cols and cols > 1 else 0)
            tiles.append(kachel(i, sid, plan[sid], aus, p_.get("keywords") or {}, x, r_ * (H + BAND + gap)))
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {tw} {th}">' + "".join(tiles) + "</svg>"
        fp = OUT / f"{b['id']}.svg"
        if not fp.exists() or fp.read_text(encoding="utf-8").strip() != svg:
            fp.write_text(svg + "\n", encoding="utf-8")
            n += 1
        depicts = sorted({x for s in felder for x in s["depicts"]} | {x for s in felder for sp in s["speech"] for x in (sp["from"], sp["to"])})
        alt_de = f"{len(felder)} gemalte Bilder: " + " ".join(f"{i} {p_['action_de']}" for i, p_ in enumerate(brief["panels"], 1))
        rec = {"id": b["id"], "type": "illustration", "status": "draft", "tags": ["TAG-JOHN"], "style": "ILLSTYLE-AQUARELL", "brief": b["brief"],
               "level": b["level"], "reference": b["reference"], "target": b["target"], "file": f"data/illustrations/aquarell/{b['id']}.svg",
               "depicts": depicts, "alt_de": alt_de, "note_de": b.get("note_de"),
               "scenes": [{"scene": s, "image": aus[s]["datei"], "model": aus[s].get("modell"), "run": aus[s].get("lauf"), "variant": aus[s].get("variante"),
                           "speech": [{"from": sp["from"], "to": sp["to"], "ref": sp["ref"]} for sp in plan[s]["speech"]]} for s in b["felder"]],
               "evidence": [plan[s]["evidence"] for s in b["felder"]],
               "license": LIC, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
        old_p = OUT / f"{b['id']}.json"
        if old_p.exists():
            old = lade(old_p)
            for k in ("check", "revision_log", "knowledge"):
                if k in old:
                    rec[k] = old[k]
        n += schreibe(old_p, rec)
    print(f"PASS: Aquarellstil – {n} Dateien geschrieben")


if __name__ == "__main__":
    main()
