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


RAND_LINIE = "#8E9087"   # Blasenumriss: abgeschwächt (Hinweis Andi Neck 2026-10-28)
RANDABSTAND = 12         # Mindestabstand der Blasen zum Bildrand (600×400)


def _umriss(x, y, w, h, r, kante, basis, spitze, seed):
    """Umriss einer Blase als ein einziger Pfad (Rahmen und Spitze zusammen, damit der Rand auch bei schräger Spitze
    durchgeht), mit leichter, gleichbleibender Unruhe wie von Hand gezogen."""
    import math
    def bogen(cx, cy, a0, a1, n=6):
        return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    pts = []
    b1, b2 = basis
    # oben (links→rechts)
    pts += bogen(x + r, y + r, 180, 270)
    if kante == "oben":
        pts += [b1, spitze, b2]
    pts += bogen(x + w - r, y + r, 270, 360)
    if kante == "rechts":
        pts += [b1, spitze, b2]
    pts += bogen(x + w - r, y + h - r, 0, 90)
    if kante == "unten":
        pts += [b2, spitze, b1]
    pts += bogen(x + r, y + h - r, 90, 180)
    if kante == "links":
        pts += [b2, spitze, b1]
    # dichter abtasten und quer zur Linie leicht versetzen (deterministisch je Blase)
    dicht = []
    for (u0, v0), (u1, v1) in zip(pts, pts[1:] + pts[:1]):
        l = math.hypot(u1 - u0, v1 - v0)
        k = max(1, int(l / 9))
        for i in range(k):
            dicht.append((u0 + (u1 - u0) * i / k, v0 + (v1 - v0) * i / k))
    out = []
    for i, (u, v) in enumerate(dicht):
        if (u, v) == spitze:
            out.append((u, v))
            continue
        d = 0.75 * math.sin(i * 0.9 + seed) + 0.45 * math.sin(i * 2.3 + seed * 1.7)
        out.append((u + d * math.cos(i + seed), v + d * math.sin(i * 1.3 + seed)))
    return "M" + " L".join(f"{u:.1f},{v:.1f}" for u, v in out) + " Z"


def blase(b, sp, n):
    fs = b.get("fs", 21)
    pad, lh = 14, fs + 4
    lines = {lg: zeilen(sp[lg], b["w"] - 2 * pad, fs) for lg in ("de", "gsw")}
    h = 2 * pad + lh * max(len(v) for v in lines.values()) - (lh - fs)
    x, y, w = b["x"], b["y"], b["w"]
    tx, ty = b["tail"]
    r = min(18, h / 2)
    # Spitze an der Kante, die der sprechenden Person zugewandt ist; Basis breiter bei schräger Spitze
    if ty > y + h:
        cx = min(max(tx, x + r + 12), x + w - r - 12)
        br = 10 + min(6, abs(tx - cx) / 8)
        kante, basis = "unten", [(cx - br, y + h), (cx + br, y + h)]
    elif tx > x + w:
        cy = min(max(ty, y + r + 8), y + h - r - 8)
        kante, basis = "rechts", [(x + w, cy - 9), (x + w, cy + 9)]
    elif tx < x:
        cy = min(max(ty, y + r + 8), y + h - r - 8)
        kante, basis = "links", [(x, cy - 9), (x, cy + 9)]
    else:
        cx = min(max(tx, x + r + 12), x + w - r - 12)
        kante, basis = "oben", [(cx - 10, y), (cx + 10, y)]
    stil = f'stroke="{RAND_LINIE}" stroke-width="1.3" stroke-linejoin="round" stroke-linecap="round"'
    if sp.get("denken"):  # Gedanke: Wolke mit kleinen Kreisen statt Spitze
        bx, by = (basis[0][0] + basis[1][0]) / 2, (basis[0][1] + basis[1][1]) / 2
        kreise = "".join(f'<circle cx="{bx + (tx - bx) * t:.0f}" cy="{by + (ty - by) * t:.0f}" r="{r_}" fill="{PAPER}" {stil}/>'
                         for t, r_ in ((0.3, 7), (0.62, 5), (0.9, 3.5)))
        rr = min(h / 2, 34)
        d = _umriss(x, y, w, h, rr, None, basis, None, n * 3.1 + 1)
        out = [f'<g class="ill-bubble ill-thought" data-speech="{n}">', kreise, f'<path d="{d}" fill="{PAPER}" fill-opacity=".95" {stil}/>']
    else:
        d = _umriss(x, y, w, h, r, kante, basis, (tx, ty), n * 3.1 + 1)
        out = [f'<g class="ill-bubble" data-speech="{n}">', f'<path d="{d}" fill="{PAPER}" fill-opacity=".95" {stil}/>']
    for lg, ls in lines.items():
        y0 = y + pad + fs * 0.82 + (h - 2 * pad - (lh * len(ls) - (lh - fs))) / 2
        tsp = "".join(f'<tspan x="{x + w / 2:.1f}" y="{y0 + i * lh:.1f}">{html.escape(t)}</tspan>' for i, t in enumerate(ls))
        out.append(f'<text class="lw lw-{lg}" text-anchor="middle" font-family="sans-serif" font-size="{fs}" fill="#2F312C">{tsp}</text>')
    out.append("</g>")
    return "".join(out)


def belegung(bild):
    """Wo im Bild gemalt ist (600×400, wahr = belegt): alles, was sich vom Papier abhebt, etwas geweitet. Blasen dürfen nur auf
    weitgehend leeres Papier (Hinweis Andi Neck 2026-10-28: nichts Wichtiges überdecken – Köpfe allein genügten nicht)."""
    import io
    import numpy as np
    from PIL import Image, ImageFilter
    daten = bild if isinstance(bild, bytes) else pathlib.Path(bild).read_bytes()
    a = np.asarray(Image.open(io.BytesIO(daten)).convert("RGB").resize((W, H), Image.LANCZOS)).astype(int)
    lum, spread = a.mean(axis=2), a.max(axis=2) - a.min(axis=2)
    papier = float(np.percentile(lum, 95))
    roh = (lum < papier - 18) | (spread > 38)
    weit = Image.fromarray((roh * 255).astype("uint8")).filter(ImageFilter.MaxFilter(7))
    return np.asarray(weit) > 0


def _hoehe(sp, w, fs):
    return 2 * 14 + (fs + 4) * max(len(zeilen(sp[lg], w - 28, fs)) for lg in ("de", "gsw")) - 4


def _schneidet(a, b, rand=0):
    return not (a[2] + rand <= b[0] or b[2] + rand <= a[0] or a[3] + rand <= b[1] or b[3] + rand <= a[1])


def blasen_auto(speech, koepfe, weitere=(), streng=False, belegt=None):
    """Blasen nach den Köpfen setzen: über (oder neben) dem Kopf der sprechenden Person, kurze Spitze zum Kopf, keine Blase über
    einem Kopf oder einer anderen Blase, Lesereihenfolge links→rechts bzw. oben→unten. Köpfe: {Figur: {"kopf": [x0,y0,x1,y1]}} in
    0–1000. weitere: Kopfrahmen aller anderen Personen aus der Blindbeschreibung (werden ebenfalls nie verdeckt).
    Gibt (Blasen, Fehler) zurück; eine Blase ohne gültigen Platz ist ein Fehler."""
    rand = 0.6 if streng else 0.25   # Köpfe grosszügig meiden: die Ortung ist ungenau

    def px(b):
        x0, y0, x1, y1 = b[0] * W / 1000, b[1] * H / 1000, b[2] * W / 1000, b[3] * H / 1000
        dx, dy = (x1 - x0) * rand, (y1 - y0) * rand * 0.35   # seitlich und unten Rand; oben keiner, dort sitzt die Blase
        return (x0 - dx, y0, x1 + dx, y1 + dy)
    kb = {f: px(k["kopf"]) for f, k in koepfe.items()}
    hindernisse = list(kb.values()) + [px(b) for b in weitere if b and len(b) == 4]
    summe = None
    if belegt is not None:  # Summenbild für schnelle Flächenanteile
        import numpy as np
        summe = np.pad(belegt.astype(np.int32).cumsum(0).cumsum(1), ((1, 0), (1, 0)))

    def anteil(x0, y0, x1, y1):
        x0, y0, x1, y1 = max(0, int(x0)), max(0, int(y0)), min(W, int(x1)), min(H, int(y1))
        return float(summe[y1, x1] - summe[y0, x1] - summe[y1, x0] + summe[y0, x0]) / max(1, (x1 - x0) * (y1 - y0))
    oben = min([k[1] for k in hindernisse] or [H])      # oberes Band: über allen Köpfen

    def kandidaten(n, grenze=None):
        """Alle zulässigen Plätze für Blase n (ohne Rücksicht auf andere Blasen), nach eigenen Kosten sortiert."""
        sp = speech[n]
        if sp["from"] not in kb:
            return []
        hx0, hy0, hx1, hy1 = kb[sp["from"]]
        hx = (hx0 + hx1) / 2
        out = []
        for fs in (21, 19):          # kleiner wird die Schrift auf dem Handy unleserlich (Durchsicht 2026-10-28)
            for w in range(170, 391, 20):
                h = _hoehe(sp, w, fs)
                for x in range(RANDABSTAND, W - RANDABSTAND - w + 1, 6):
                    for y in range(10, H - RANDABSTAND - h + 1, 6):
                        box = (x, y, x + w, y + h)
                        if any(_schneidet(box, k, 4) for k in hindernisse):
                            continue
                        belegt_ = anteil(x - 4, y - 4, x + w + 4, y + h + 4) if summe is not None else 0
                        if belegt_ > 0.05:      # Blase nur auf leerem Papier
                            continue
                        if streng and y + h > oben - 6:
                            continue
                        if y + h <= hy0 - 6:           # über dem Kopf: Spitze nach unten zur Kopfmitte oben
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
                        kosten = (belegt_ * 600 + seit * 0.5 + (0 if y + h <= oben - 6 else 90) + max(0, lang - 50) * 1.5 + max(0, 14 - lang) * 6
                                  + y * 0.25 + (21 - fs) * 12 + (h - 2 * 14) * 1.2 + (w - 170) * 0.05)
                        out.append((kosten, {"x": x, "y": y, "w": w, "h": h, "fs": fs, "tail": [round(tail[0]), round(tail[1])]}))
        out.sort(key=lambda e: e[0])
        return out[:grenze]

    def spitze_frei(g, v):  # die Spitze einer Blase läuft nicht durch eine andere Blase
        x0, y0 = g["x"] + g["w"] / 2, g["y"] + g["h"] / 2
        tx, ty = g["tail"]
        for i in range(1, 21):
            u, w_ = x0 + (tx - x0) * i / 20, y0 + (ty - y0) * i / 20
            if g["x"] <= u <= g["x"] + g["w"] and g["y"] <= w_ <= g["y"] + g["h"]:
                continue
            if v["x"] - 4 <= u <= v["x"] + v["w"] + 4 and v["y"] - 4 <= w_ <= v["y"] + v["h"] + 4:
                return False
        return True

    def frei(g, andere):
        return not any(_schneidet((g["x"], g["y"], g["x"] + g["w"], g["y"] + g["h"]), (v["x"], v["y"], v["x"] + v["w"], v["y"] + v["h"]), 8)
                       or not spitze_frei(g, v) or not spitze_frei(v, g) for v in andere)

    def reihenfolge(gesetzt):  # frühere Rede links bzw. oben
        k = 0
        ns = sorted(gesetzt)
        for i, m in enumerate(ns):
            for n in ns[i + 1:]:
                v, g = gesetzt[m], gesetzt[n]
                if g["x"] + g["w"] / 2 < v["x"] + v["w"] / 2 - 20 and g["y"] < v["y"] + v["h"] / 2:
                    k += 120
        return k

    kand = [kandidaten(n) for n in range(len(speech))]
    beste = [None]

    import itertools

    def suche(folge, j, gesetzt, kosten):
        if beste[0] and kosten >= beste[0][0]:
            return
        if j == len(folge):
            gesamt_ = kosten + reihenfolge(gesetzt)
            if not beste[0] or gesamt_ < beste[0][0]:
                beste[0] = (gesamt_, dict(gesetzt))
            return
        n = folge[j]
        breite_ = 1 if j == len(folge) - 1 else (400 if j == 0 else 60)   # letzte Blase: günstigster freier Platz
        versucht = 0
        for k_, g in kand[n]:
            if versucht >= breite_:
                break
            if frei(g, gesetzt.values()):
                versucht += 1
                gesetzt[n] = g
                suche(folge, j + 1, gesetzt, kosten + k_)
                del gesetzt[n]

    for folge in itertools.permutations(range(len(speech))):   # jede Blase einmal zuerst setzen
        suche(folge, 0, {}, 0)
    if beste[0]:
        return [beste[0][1][n] for n in range(len(speech))], []
    # keine Lösung für alle: so viele wie möglich, je die günstigste freie
    gesetzt, fehler = {}, []
    for n in range(len(speech)):
        g = next((g for _, g in kand[n] if frei(g, gesetzt.values())), None)
        if g:
            gesetzt[n] = g
        else:
            fehler.append(f"Blase {n + 1}: " + (f"Kopf von {speech[n]['from']} unbekannt" if speech[n]["from"] not in kb else f"kein freier Platz bei {speech[n]['from']}"))
    return [gesetzt.get(n) for n in range(len(speech))], fehler


def reihe_ok(speech, koepfe):
    """Feste Regel Lesereihenfolge: wer zuerst spricht, steht (mit dem Kopf) links von dem, der danach spricht – sonst stehen
    die Blasen in falscher Reihenfolge (Mk 4 S3, Durchsicht 2026-10-28; Regel schon in BILDAUFTRAEGE-ANLEITUNG.md)."""
    xs = []
    for sp in speech:
        k = koepfe.get(sp["from"])
        if k:
            xs.append((sp["from"], (k["kopf"][0] + k["kopf"][2]) / 2))
    for (f0, x0), (f1, x1) in zip(xs, xs[1:]):
        if f0 != f1 and x0 > x1 + 30:
            return False
    return True


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
    vers = sorted({((aus[s].get("schluss") or {}).get("prozess") or (aus[s].get("pruefung") or {}).get("prozess")) for s in b["felder"]} - {None})
    c = {"stufe": stufe, "process": vers[-1] if vers else "PROC-BILD-AQUARELL@1.0",
         "method_de": "Prüfung nach dem Prozess in «process» (docs/PROZESSE.md): je Feld Blindbeschreibung, Prüfregeln auf drei Ebenen "
                      "(allgemein, Figur, Feld) und Vergleich mit dem Moment durch weitere Instanzen; danach Schlussprüfung der fertigen Kachel.",
         "felder": felder, "open_de": offen,
         "limits_de": "Stand Entwurf: kein Test mit Leserinnen und Lesern, keine fachliche und keine muttersprachliche Prüfung (Züridüütsch). "
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
