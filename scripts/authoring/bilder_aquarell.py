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

Blasen: das Werkzeug setzt sie selbst (blasen_auto) nach den Kopfpositionen aus der automatischen Prüfung
(bilder_pruefung.py, in auswahl.json je Szene «pruefung.koepfe») und legt sie als «blasen_auto» ab. Von Hand nur als
Ausnahme: «blasen»: "hand" mit «bubbles» (x, y, w, optional fs, tail; Bildkoordinaten 600×400).
Szenenpläne: alle Dateien bilder_aquarell_daten/szenen-*.json; «basis» nennt die Lesetexte (de, gsw).
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


def uebernehmen(lauf, wahl, pruefungen=None):
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
        aus[sz] = {"datei": f"img/{sz}.webp", "lauf": lauf.name, "variante": var, "modell": meta[sz].get("modell"), "uebernommen": DATE}
        if alt.get("blasen") == "hand":
            aus[sz].update(blasen="hand", bubbles=alt.get("bubbles", []))
        if pruefungen and (sz, var) in pruefungen:
            aus[sz]["pruefung"] = pruefungen[(sz, var)]
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
    if sp.get("denken"):  # Gedanke: Wolke mit kleinen Kreisen statt Spitze
        bx, by = base[0][0] + (base[1][0] - base[0][0]) / 2, base[0][1] + (base[1][1] - base[0][1]) / 2
        kreise = "".join(f'<circle cx="{bx + (tx - bx) * t:.0f}" cy="{by + (ty - by) * t:.0f}" r="{r_}" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/>'
                         for t, r_ in ((0.3, 7), (0.62, 5), (0.9, 3.5)))
        out = [f'<g class="ill-bubble ill-thought" data-speech="{n}">', kreise,
               f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="{min(h / 2, 34):.0f}" fill="{PAPER}" fill-opacity=".94" stroke="{INK}" stroke-width="1.2" stroke-dasharray="1 0"/>']
    else:
        out = None
    pts = " ".join(f"{u:.0f},{v:.0f}" for u, v in base) + f" {tx:.0f},{ty:.0f}"
    out = out or [f'<g class="ill-bubble" data-speech="{n}">',
           f'<polygon points="{pts}" fill="{PAPER}" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="18" fill="{PAPER}" fill-opacity=".94" stroke="{INK}" stroke-width="1.2"/>',
           f'<polygon points="{pts}" fill="{PAPER}" stroke="none" transform="translate({shift[0]} {shift[1]})"/>']
    for lg, ls in lines.items():
        y0 = y + pad + fs * 0.82 + (h - 2 * pad - (lh * len(ls) - (lh - fs))) / 2
        tsp = "".join(f'<tspan x="{x + w / 2:.1f}" y="{y0 + i * lh:.1f}">{html.escape(t)}</tspan>' for i, t in enumerate(ls))
        out.append(f'<text class="lw lw-{lg}" text-anchor="middle" font-family="sans-serif" font-size="{fs}" fill="#2F312C">{tsp}</text>')
    out.append("</g>")
    return "".join(out)


def _hoehe(sp, w, fs):
    return 2 * 14 + (fs + 4) * max(len(zeilen(sp[lg], w - 28, fs)) for lg in ("de", "gsw")) - 4


def _schneidet(a, b, rand=0):
    return not (a[2] + rand <= b[0] or b[2] + rand <= a[0] or a[3] + rand <= b[1] or b[3] + rand <= a[1])


def blasen_auto(speech, koepfe, weitere=()):
    """Blasen nach den Köpfen setzen: über (oder neben) dem Kopf der sprechenden Person, kurze Spitze zum Kopf, keine Blase über
    einem Kopf oder einer anderen Blase, Lesereihenfolge links→rechts bzw. oben→unten. Köpfe: {Figur: {"kopf": [x0,y0,x1,y1]}} in
    0–1000. weitere: Kopfrahmen aller anderen Personen aus der Blindbeschreibung (werden ebenfalls nie verdeckt).
    Gibt (Blasen, Fehler) zurück; eine Blase ohne gültigen Platz ist ein Fehler."""
    def px(b):
        return (b[0] * W / 1000, b[1] * H / 1000, b[2] * W / 1000, b[3] * H / 1000)
    kb = {f: px(k["kopf"]) for f, k in koepfe.items()}
    hindernisse = list(kb.values()) + [px(b) for b in weitere if b and len(b) == 4]

    def setze(n, gesetzt):
        sp = speech[n]
        if sp["from"] not in kb:
            return None
        hx0, hy0, hx1, hy1 = kb[sp["from"]]
        hx = (hx0 + hx1) / 2
        best = None
        for fs in (21, 19, 17):
            for w in range(170, 331, 20):
                h = _hoehe(sp, w, fs)
                for x in range(6, W - 6 - w + 1, 4):
                    for y in range(4, H - 6 - h + 1, 4):
                        box = (x, y, x + w, y + h)
                        if any(_schneidet(box, k, 6) for k in hindernisse):
                            continue
                        if any(_schneidet(box, (g["x"], g["y"], g["x"] + g["w"], g["y"] + g["h"]), 8) for g in gesetzt.values()):
                            continue
                        if y + h <= hy0 - 10:          # über dem Kopf: Spitze nach unten zur Kopfmitte oben
                            tail = (hx, hy0 - 3)
                            lang = hy0 - 3 - (y + h)
                            seit = abs((x + w / 2) - hx)
                            if seit > w / 2 + 40:
                                continue
                        elif x >= hx1 + 10 or x + w <= hx0 - 10:  # daneben: Spitze seitlich zum Kopf
                            if y > hy1 or y + h < hy0 - 60:
                                continue
                            tail = (hx1 + 3, (hy0 + hy1) / 2) if x >= hx1 + 10 else (hx0 - 3, (hy0 + hy1) / 2)
                            lang = (x - hx1) if x >= hx1 + 10 else (hx0 - (x + w))
                            seit = 220            # neben dem Kopf nur, wenn darüber kein Platz ist
                        else:
                            continue
                        kosten = (seit * 0.5 + max(0, lang - 50) * 1.5 + max(0, 14 - lang) * 6 + y * 0.25 + (21 - fs) * 12
                                  + (h - 2 * 14) * 0.6 + (w - 170) * 0.05)
                        for m, v in gesetzt.items():  # Lesereihenfolge: frühere Rede links bzw. oben
                            vor = m < n
                            links = x + w / 2 < v["x"] + v["w"] / 2 - 20 and y < v["y"] + v["h"] / 2
                            rechts = x + w / 2 > v["x"] + v["w"] / 2 + 20 and y + h / 2 > v["y"]
                            if (vor and rechts) or (not vor and links):
                                kosten += 120
                        if best is None or kosten < best[0]:
                            best = (kosten, {"x": x, "y": y, "w": w, "h": h, "fs": fs, "tail": [round(tail[0]), round(tail[1])]})
        return best

    import itertools
    beste = None
    for folge in itertools.permutations(range(len(speech))):   # schwierige Blase zuerst setzen, wenn nötig
        gesetzt, kosten, fehlt = {}, 0, []
        for n in folge:
            r = setze(n, gesetzt)
            if r is None:
                fehlt.append(n)
                continue
            gesetzt[n] = r[1]
            kosten += r[0]
        wert = (len(fehlt), kosten)
        if beste is None or wert < beste[0]:
            beste = (wert, gesetzt, fehlt)
        if not fehlt:
            break
    _, gesetzt, fehlt = beste
    fehler = [f"Blase {n + 1}: " + (f"Kopf von {speech[n]['from']} unbekannt" if speech[n]["from"] not in kb else f"kein freier Platz bei {speech[n]['from']}")
              for n in sorted(fehlt)]
    return [gesetzt.get(n) for n in range(len(speech))], fehler


def band(n, kw):
    out = [f'<rect x="0" y="{H}" width="{W}" height="{BAND}" fill="{PAPER}"/>',
           f'<circle cx="24" cy="{H + BAND / 2}" r="12" fill="none" stroke="{INK}" stroke-width="1.4"/>',
           f'<text x="24" y="{H + BAND / 2 + 5}" text-anchor="middle" font-family="sans-serif" font-size="14" fill="{INK}" class="pn-n">{n}</text>']
    for lg in ("de", "gsw"):
        t = kw.get(lg) or kw.get("de") or ""
        fs = 19 if len(t) <= 46 else max(13, int(19 * 46 / len(t)))
        out.append(f'<text class="lw lw-{lg}" x="{(W + 40) / 2}" y="{H + BAND / 2 + fs * 0.36:.1f}" text-anchor="middle" font-family="sans-serif" font-size="{fs}" font-style="italic" fill="#3B3D37">{html.escape(t)}</text>')
    return "".join(out)


def blasen_von(a):
    return a.get("bubbles", []) if a.get("blasen") == "hand" else a.get("blasen_auto", a.get("bubbles", []))


def kachel(i, sz_id, sz, aus, kw, x, y):
    a = aus[sz_id]
    teile = [f'<svg class="ill-tile" data-span="1" data-scene="{sz_id}" x="{x}" y="{y}" width="{W}" height="{H + BAND}" viewBox="0 0 {W} {H + BAND}">',
             f'<image href="{a["datei"]}" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="xMidYMid slice"/>']
    for n, (sp, b) in enumerate(zip(sz["speech"], blasen_von(a))):
        if b:
            teile.append(blase(b, sp, n))
    teile.append(band(i, kw))
    teile.append(f'<rect x=".5" y=".5" width="{W - 1}" height="{H + BAND - 1}" fill="none" stroke="#D8D0C0" stroke-width="1"/></svg>')
    return "".join(teile)


def texte_von(plan_d):
    t = {}
    for tid in plan_d["basis"]:
        rec = lade(ROOT / f"data/translations/{tid}.json")
        lg = "gsw" if rec.get("language", "").startswith("gsw") or "-GSW" in tid else "de"
        t.setdefault(lg, {}).update(rec["text_by_reference"])
    return t


BAND_MAX = 54   # Zeichen; länger wird die Schrift im Band kleiner als 16 px und auf dem Handy zu klein (Lauf 12, Lk 15)


def pruefe_band(plan_d, texte):
    """Feste Prüfung: Stichwortband höchstens BAND_MAX Zeichen, sonst «band» im Szenenplan (Wortlaut aus dem Text des Felds)."""
    fehler = []
    for b in plan_d["bilder"]:
        panels = lade(D / f"briefs/{b['brief']}.json")["panels"]
        for sid, p_ in zip(b["felder"], panels):
            sz = plan_d["szenen"][sid]
            eigen = b.get("band", {}).get(sid) or sz.get("band")
            kw = eigen or p_.get("keywords") or {}
            for lg in ("de", "gsw"):
                t = kw.get(lg) or ""
                if len(t) > BAND_MAX:
                    fehler.append(f"{sid}: Band «{t}» ({lg}) hat {len(t)} Zeichen, höchstens {BAND_MAX} – «band» im Szenenplan setzen")
                if eigen and t and norm(t) not in norm(" ".join(texte[lg].get(r, "") for r in verse_von(p_.get("reference") or sz["reference"]))):
                    fehler.append(f"{sid}: Band «{t}» ({lg}) steht so nicht im Text {p_.get('reference') or sz['reference']}")
    return fehler


def verse_von(ref):
    a, _, z = ref.partition("-")
    bk, c, v = a.split(".")
    c2, v2 = (z.split(".")[1], z.split(".")[2]) if z else (c, v)
    return [f"{bk}.{c}.{x}" for x in range(int(v), int(v2) + 1)] if c == c2 else [f"{bk}.{c}.{v}"]


def pruefe_zitate(plan, texte):
    fehler = []
    for sid, sz in plan.items():
        for sp in sz["speech"]:
            for lg in ("de", "gsw"):
                teile = [t for t in sp[lg].split("…") if t.strip()]
                if not all(norm(t) in norm(texte[lg][sp["ref"]]) for t in teile):
                    fehler.append(f"{sid}: «{sp[lg]}» steht so nicht in {sp['ref']} ({lg})")
    return fehler


def fig_fuer(fig, plan_d):
    """Figurenangaben für einen Plan: figuren.json, ergänzt bzw. überschrieben durch «figuren», «kenn_en», «pruef» des Plans."""
    f = {k: (dict(v) if isinstance(v, dict) else v) for k, v in fig.items()}
    for k in ("figuren", "kenn_en", "pruef"):
        f.setdefault(k, {}).update(plan_d.get(k, {}))
    return f


def plaene():
    return {p.name: lade(p) for p in sorted(DATEN.glob("szenen-*.json"))}


def pruef_check(b, aus, alt_check, aktuell_sha=None):
    """check des Bild-Datensatzes aus den automatischen Prüfungen der Felder (auswahl.json). aktuell_sha: {Szene: Fingerabdruck
    von Regeln und Szenenplan heute}; weicht er von dem der Prüfung ab, ist die Prüfung veraltet."""
    felder, offen, stufe = [], [], "ki-geprueft"
    for s in b["felder"]:
        pr, sl = aus[s].get("pruefung"), aus[s].get("schluss")
        if not pr:
            felder.append({"scene": s, "ergebnis": "ungeprueft"})
            stufe = "entwurf"
            continue
        f = {"scene": s, "ergebnis": pr["ergebnis"], "punkte": pr["punkte"], "kern": pr.get("kern"), "bild_sha": pr["bild_sha"],
             "plan_sha": pr.get("plan_sha"), "regeln_version": pr.get("regeln_version"), "datum": pr.get("datum"), "modell": pr.get("modell"),
             "regeln": [{k: e[k] for k in ("id", "stufe", "ergebnis")} for e in pr["regeln"]],
             "offen_de": [f"{e['de']} ({e['ergebnis']}: {e['grund']})" for e in pr["regeln"] if e["ergebnis"] != "ok"]}
        if pr.get("veraltet") or (aktuell_sha and aktuell_sha.get(s) and pr.get("plan_sha") != aktuell_sha[s]):
            f["veraltet"] = True
            offen.append(f"{s}: Prüfung veraltet (Regeln oder Szenenplan geändert)")
        if sl:
            f["schluss"] = {"ergebnis": sl["ergebnis"], "kern": sl.get("kern"), "bild_sha": sl.get("bild_sha"),
                            "offen_de": [f"{e['de']} ({e['ergebnis']}: {e['grund']})" for e in sl["regeln"] if e["ergebnis"] != "ok"]
                            + ([f"Moment nicht ganz getroffen: {sl.get('kern_fehlt_de')}"] if (sl.get("kern") or 0) < 2 and sl.get("kern_fehlt_de") else [])}
        if pr["ergebnis"] != "bestanden" or f.get("veraltet") or not sl or sl["ergebnis"] != "bestanden":
            stufe = "entwurf"
        felder.append(f)
        offen += [f"{s}: {x}" for x in f["offen_de"] if "(fehler" in x or "(unklar" in x]
        offen += [f"{s} (Kachel): {x}" for x in (f.get("schluss") or {}).get("offen_de", [])]
    c = {"stufe": stufe,
         "method_de": "Automatische Prüfung (docs/BILDSTIL.md, «Automatische Prüfung»): je Feld Blindbeschreibung, Prüfregeln auf drei Ebenen "
                      "(allgemein, Figur, Feld) und Vergleich mit dem Moment; danach Schlussprüfung der fertigen Kachel mit Blasen. "
                      "Bildprüfmodell von OpenAI, getrennt vom Malmodell.",
         "felder": felder, "open_de": offen,
         "limits_de": "Urteil eines KI-Modells; kein Test mit Menschen, keine fachliche und keine muttersprachliche Prüfung (Züridüütsch). "
                      "Stufe «ki-geprueft» heisst: alle Pflichtregeln erfüllt, keine fachliche Freigabe."}
    if alt_check and "felder" not in alt_check:
        c["frueher"] = alt_check
    elif alt_check and alt_check.get("frueher"):
        c["frueher"] = alt_check["frueher"]
    return c


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "uebernehmen":
        uebernehmen(sys.argv[2], sys.argv[3:])
        return
    fig = lade(DATEN / "figuren.json")
    aus = lade(DATEN / "auswahl.json")
    alle = plaene()
    fehler = []
    for name, pd in alle.items():
        fehler += pruefe_zitate(pd["szenen"], texte_von(pd)) + pruefe_band(pd, texte_von(pd))
    if fehler:
        sys.exit("FEHLER Zitate:\n" + "\n".join(fehler))
    n = 0
    tags = sorted({t for pd in alle.values() for t in pd.get("tags", ["TAG-JOHN"])})
    stil = {"id": "ILLSTYLE-AQUARELL", "type": "illustration_style", "status": "draft", "tags": tags, "key": "aquarell",
            "labels": {"de": "Aquarell", "en": "Watercolour"},
            "description_de": "Minimalistischer Aquarell-Comic nach dem Styleguide «Visuelle Bibel» V1.2 (docs/BILDSTIL.md): warmweisses Papier, wenige dünne Linien, transparente Flächen, natürliche erwachsene Figuren, viel Weissraum. Gemalte Szenen je Bildfeld; Worte als Text darüber in der gewählten Sprache. Ersetzt in der App die Stile Symbol und Anime, wo vorhanden.",
            "style_reference": "docs/referenz/stilreferenz-aquarell-comic.jpg", "character_sheet": "data/illustrations/aquarell/figurenblatt.webp",
            "renderings": {k: {"description_en": v} for k, v in sorted({**fig["figuren"], **{x: y for pd in alle.values() for x, y in pd.get("figuren", {}).items() if x not in fig["figuren"]}}.items())},
            "license": LIC, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
    alt_p = D / "styles/ILLSTYLE-AQUARELL.json"
    if alt_p.exists():
        alt = lade(alt_p)
        stil["knowledge"] = alt.get("knowledge", stil["knowledge"])
        stil["revision_log"] = alt.get("revision_log", [])
    n += schreibe(alt_p, stil)
    for name, plan_d in alle.items():
        plan = plan_d["szenen"]
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
                tiles.append(kachel(i, sid, plan[sid], aus, b.get("band", {}).get(sid) or plan[sid].get("band") or p_.get("keywords") or {}, x, r_ * (H + BAND + gap)))
            svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {tw} {th}">' + "".join(tiles) + "</svg>"
            fp = OUT / f"{b['id']}.svg"
            if not fp.exists() or fp.read_text(encoding="utf-8").strip() != svg:
                fp.write_text(svg + "\n", encoding="utf-8")
                n += 1
            depicts = sorted({x for s in felder for x in s["depicts"]} | {x for s in felder for sp in s["speech"] for x in (sp["from"], sp["to"])})
            alt_de = f"{len(felder)} gemalte Bilder: " + " ".join(f"{i} {p_['action_de']}" for i, p_ in enumerate(brief["panels"], 1))
            rec = {"id": b["id"], "type": "illustration", "status": "draft", "tags": plan_d.get("tags", ["TAG-JOHN"]), "style": "ILLSTYLE-AQUARELL", "brief": b["brief"],
                   "level": b["level"], "reference": b["reference"], "target": b["target"], "file": f"data/illustrations/aquarell/{b['id']}.svg",
                   "depicts": depicts, "alt_de": alt_de, "note_de": b.get("note_de"),
                   "scenes": [{"scene": s, "image": aus[s]["datei"], "model": aus[s].get("modell"), "run": aus[s].get("lauf"), "variant": aus[s].get("variante"),
                               "reference": plan[s]["reference"],
                               "speech": [{"from": sp["from"], "to": sp["to"], "ref": sp["ref"]} for sp in plan[s]["speech"]]} for s in b["felder"]],
                   "evidence": [plan[s]["evidence"] for s in b["felder"]],
                   "license": LIC, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
            old_p = OUT / f"{b['id']}.json"
            old = lade(old_p) if old_p.exists() else {}
            for k in ("revision_log", "knowledge"):
                if k in old:
                    rec[k] = old[k]
            import bilder_pruefung as BP
            allg = lade(DATEN / "pruefregeln.json")
            figp = fig_fuer(fig, plan_d)
            rec["check"] = pruef_check(b, aus, old.get("check"), {s: BP.plan_fingerabdruck(plan[s], figp, allg) for s in b["felder"]})
            n += schreibe(old_p, rec)
    print(f"PASS: Aquarellstil – {n} Dateien geschrieben")


if __name__ == "__main__":
    main()
