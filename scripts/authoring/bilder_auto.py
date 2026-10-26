#!/usr/bin/env python3
"""Zeichner: setzt ein Bild in beiden Stilen direkt aus einem Bildauftrag zusammen.

Für die vielen Stellen (Buch, Kapitel, Abschnitt aller übersetzten Bücher) werden die Bilder nicht mehr einzeln von
Hand gezeichnet, sondern aus dem Bildauftrag (data/illustrations/briefs/) und den Bauteilen des Stils gesetzt:
1. Hintergrund: Orte (Meer, Feld, Stadt, Tempel …) als Band oder im Hintergrund.
2. Gott (Strahlenkranz) und Geist (Taube) oben; Personen in der Reihenfolge des Auftrags von links nach rechts.
3. Gegenstände am Boden, in der Hand oder gross in der Mitte (Schiff, Fisch); Zeichen über oder bei den Figuren.
4. Sprechblasen über der sprechenden Figur mit den Zeichen des Auftrags; Geste zur angesprochenen Figur.
Feinsteuerung im Auftrag (``stage`` je Feld, stilunabhängig): mood (Ausdruck), pose (lie, kneel, sit, sleep, fall, away),
hold (Figur hält Gegenstand), in (Figur in Gegenstand, z. B. Jona im Fisch), at (Zeichen bei Figur), count (Anzahl),
split (gestrichelte Linie nach der n-ten Figur), tears/joy/hearts (Figuren mit Tränen, Freude, Herz).

Handgezeichnete Bilder (Johannes 2, obere Ebenen) bleiben in bilder_symbol.py und bilder_anime.py.
KI-Entwurf (Claude) vom 2026-10-17 auf Wunsch von Andi Neck; keine fachliche Prüfung.
"""
import json
import os
import re
import math
import pathlib

from _lib import D

# ------------------------------------------------------------------ Auftragsdaten
DATA = pathlib.Path(__file__).resolve().parent / "bildauftraege_daten"


def load_briefs():
    """Bildaufträge aus bildauftraege_daten/*.json (eine Datei je Buch), in Dateireihenfolge."""
    out = []
    for f in sorted(DATA.glob("*.json")):
        if f.name.startswith("_"):  # Hilfsdateien (z. B. _wortzeichen.json)
            continue
        for b in json.loads(f.read_text(encoding="utf-8")):
            b["_file"] = f.name
            out.append(b)
    return out


def alt_text(b, lang="de", anime=False):
    caps = [p["caption_de" if lang == "de" else "caption_gsw"] for p in b["panels"]]
    if len(caps) == 1:
        return caps[0]
    word = {2: ("zwei", "zwei"), 3: ("drei", "drüü"), 4: ("vier", "vier")}[len(caps)][0 if lang == "de" else 1]
    if lang == "de":
        head = (f"Comic in {word} Bildern ohne Text: " if anime else f"{word.capitalize()} Felder: ")
    else:
        head = (f"Comic i {word} Bilder ohni Text: " if anime else f"{word.capitalize()} Fälder: ")
    return head + " ".join(f"{i + 1} {c}" for i, c in enumerate(caps))


# ------------------------------------------------------------------ Platzierung je Lexikon-Eintrag
# place: band (ganze Breite unten), back (Hintergrund rechts), sky (oben), big (gross in der Mitte), floor (am Boden),
#        hand (klein in der Hand), air (frei oben), head (bei den Köpfen), line (zwischen Figuren)
# size: (w, h) in Feldeinheiten (Feld 186 x 140)
META = {
    "FIG-GOTT": ("sky", (40, 40)), "FIG-HEILIGER-GEIST": ("sky", (34, 34)),
    "FIG-ORT-TEMPEL": ("back", (92, 69)), "FIG-ORT-JERUSALEM": ("back", (96, 67)), "FIG-ORT-BERG": ("back", (110, 69)),
    "FIG-ORT-HAUS": ("back", (66, 59)), "FIG-ORT-GRAB": ("back", (78, 54)), "FIG-ORT-WEG": ("band", (186, 70)),
    "FIG-ORT-MEER": ("back", (110, 61)),
    "FIG-OBJ-BOOT": ("big", (70, 56)), "FIG-OBJ-KREUZ": ("floor", (30, 44)), "FIG-OBJ-GESETZESTAFELN": ("hand", (20, 19)),
    "FIG-OBJ-BRIEF": ("hand", (20, 15)), "FIG-OBJ-SCHRIFTROLLE": ("hand", (24, 16)), "FIG-OBJ-LEIER": ("hand", (16, 20)),
    "FIG-OBJ-KRUG-WASSER": ("floor", (16, 30)), "FIG-OBJ-KRUG-WEIN": ("floor", (16, 30)), "FIG-OBJ-KRUG-WEIN-LEER": ("floor", (20, 28)),
    "FIG-OBJ-BECHER-VOLL": ("hand", (10, 12)), "FIG-OBJ-BECHER-LEER": ("hand", (10, 12)), "FIG-OBJ-PEITSCHE": ("hand", (18, 21)),
    "FIG-OBJ-SCHAF": ("floor", (30, 19)), "FIG-OBJ-TAUBE": ("floor", (22, 22)), "FIG-OBJ-MUENZEN": ("floor", (18, 10)),
    "FIG-ZEICHEN-STERN": ("air", (18, 18)), "FIG-ZEICHEN-FEHLT": ("air", (16, 16)), "FIG-ZEICHEN-STUNDE": ("air", (14, 20)),
    "FIG-ZEICHEN-HOEREN": ("air", (22, 19)), "FIG-ZEICHEN-GLAUBEN": ("head", (16, 18)), "FIG-ZEICHEN-FREUDE": ("head", (20, 13)),
    "FIG-ZEICHEN-FRAGEN": ("air", (10, 17)), "FIG-ZEICHEN-BRINGEN": ("air", (20, 10)), "FIG-ZEICHEN-ABSTAND": ("line", (8, 60)),
    "FIG-ZEICHEN-HOCHZEIT": ("air", (60, 24)), "FIG-ZEICHEN-TAGE": ("air", (12, 12)), "FIG-ZEICHEN-NIEDERREISSEN": ("back", (80, 60)),
    "FIG-ZEICHEN-LICHT": ("air", (34, 34)), "FIG-SYMBOL-ADLER": ("big", (120, 84)), "FIG-ZEICHEN-SCHOEPFUNG": ("big", (90, 75)),
    "FIG-ZEICHEN-HOFFNUNG": ("air", (24, 24)), "FIG-ZEICHEN-UMKEHR": ("air", (24, 18)), "FIG-ZEICHEN-GERICHT": ("air", (30, 26)),
    "FIG-ZEICHEN-NEUE-SCHOEPFUNG": ("back", (100, 75)), "FIG-ZEICHEN-EXIL": ("floor", (60, 24)), "FIG-ZEICHEN-AUSBREITEN": ("air", (36, 27)),
    "FIG-GRUPPE-GEMEINDE": ("back", (76, 56)), "FIG-ZEICHEN-BETEN": ("head", (16, 18)), "FIG-ZEICHEN-TRAUER": ("head", (6, 9)),
}
KIND_DEFAULT = {"place": ("back", (90, 64)), "object": ("floor", (24, 24)), "sign": ("air", (20, 20)), "action": ("air", (22, 18))}
HUMAN_KINDS = {"person", "role", "group"}
GROUPS = {"FIG-GRUPPE-MENGE", "FIG-GRUPPE-SEELEUTE", "FIG-GRUPPE-EDOM", "FIG-GRUPPE-ZWOELF"}


def meta(fid, lex, extra):
    if fid in extra:
        return extra[fid]
    if fid in META:
        return META[fid]
    return KIND_DEFAULT.get(lex[fid]["kind"], ("air", (20, 20)))


# ------------------------------------------------------------------ Grundriss eines Felds (stilunabhängig)
W, H, FLOOR_Y = 186, 140, 118


SHIPS = {"FIG-OBJ-SCHIFF", "FIG-OBJ-BOOT"}
WINDOW = {"FIG-OBJ-GROSSER-FISCH", "FIG-ORT-GRAB"}
HEADWEAR = {"FIG-OBJ-DORNENKRONE", "FIG-OBJ-KRONE"}  # mit stage.at auf den Kopf gesetzt
WATER_TOP = 96  # Wellenkamm der Bänder Meer/See


def plan(p, lex, extra):
    """Ordnet die Bestandteile eines Felds an; Ergebnis in Feldeinheiten, von beiden Stilen gezeichnet."""
    st = p.get("stage") or {}
    as_place = [f for f in p["figures"] if f in META and META[f][0] == "back"]  # z. B. Gemeinde (Haus mit Menschen)
    humans = [f for f in p["figures"] if (lex[f]["kind"] in HUMAN_KINDS or f == "FIG-JESUS") and f not in as_place]
    divine = [f for f in p["figures"] if f in ("FIG-GOTT", "FIG-HEILIGER-GEIST")]
    things = as_place + list(p["objects"]) + list(p["signs"])
    if "cross" in (st.get("pose") or {}).values():  # Jesus am Kreuz: das Kreuz zeichnet die Figur selbst
        things = [x for x in things if x != "FIG-OBJ-KREUZ"]
    inside = st.get("in", {})
    row = [h for h in humans if h not in inside]
    place = lambda t: meta(t, lex, extra)[0]  # noqa: E731
    big = [t for t in things if place(t) == "big"]
    back = [t for t in things if place(t) == "back"]
    band = [t for t in things if place(t) == "band"]
    if any(b in SHIPS for b in big) and not band:
        # ein Schiff steht nie auf dem Trockenen: mit Personen an Land ein Hafen, sonst offenes Meer
        band = [("_HAFEN-L" if st.get("big_side") == "left" else "_HAFEN-R") if row else "FIG-ORT-MEER-OFFEN"]
    if st.get("sea") == "calm":
        band = ["_MEER-STILL" if b in ("FIG-ORT-MEER-OFFEN", "FIG-ORT-SEE") else b for b in band]
    held = st.get("hold", {})
    at = st.get("at", {})
    at = {**at, **st.get("beside", {})}
    floor = [t for t in things if place(t) == "floor" and t not in held.values() and t not in at]
    hand_objs = [t for t in things if place(t) == "hand" and t not in held.values() and t not in at]
    air = [t for t in things if place(t) == "air" and t not in st.get("at", {}) and t not in st.get("beside", {}) and t not in held.values()]
    head_signs = [t for t in things if place(t) == "head"]
    lines = [t for t in things if place(t) == "line"]
    x0, x1 = 10, W - 10
    big_w = 0
    if big:
        big_w = min(meta(big[0], lex, extra)[1][0], 112 if row else 160)
        if row:
            if st.get("big_side", "right") == "right":
                x1 = W - 10 - big_w * .82
            else:
                x0 = 10 + big_w * .82
    if back and row and not big and not st.get("before"):
        bw = meta(back[0], lex, extra)[1][0]
        if st.get("back_side", "right") == "right":
            x1 = min(x1, max(W * .5, W - 6 - bw * .7))
        else:
            x0 = max(x0, min(W * .5, 6 + bw * .7))
    fx = st.get("floor_x", {})
    free_floor = [t for t in floor if t not in fx]
    reserve = 0
    if row and free_floor:
        cnt = st.get("count", {})
        reserve = min(72, sum(meta(t, lex, extra)[1][0] * min(int(cnt.get(t, 1)), 3) * .85 for t in free_floor) + 6)
        if st.get("floor_side", "right") == "right":
            x1 -= reserve
        else:
            x0 += reserve
    if x1 - x0 < 40 * max(1, len(row)) * .6:
        x0, x1 = 10, W - 10 - reserve
    slots = []
    if row:
        span = (x1 - x0) / len(row)
        for i, h in enumerate(row):
            x = (st.get("x") or {}).get(h, x0 + span * (i + .5))
            slots.append({"fid": h, "x": x, "span": span, "group": h in GROUPS or lex[h]["kind"] == "group"})
    # Leserichtung: wer zuerst spricht, steht links vom zweiten Sprecher (Blindtest: Antwort links vor Frage wurde falsch gelesen)
    names = [sl["fid"] for sl in slots]
    spk = []
    for sp in p["speech"]:
        if sp["from"] in names and sp["from"] not in spk:
            spk.append(sp["from"])
    cap = p.get("caption_de", "")
    if (len(spk) >= 2 and not st.get("x") and "split" not in st and "links" not in cap and "rechts" not in cap):
        a, b = slots[names.index(spk[0])], slots[names.index(spk[1])]
        if a["x"] > b["x"]:
            a["x"], b["x"] = b["x"], a["x"]
    side = st.get("floor_side", "right")
    return {"st": st, "row": slots, "floor_zone": (x1 + 2, W - 6) if side == "right" else (6, x0 - 2), "reserve": reserve,
            "divine": divine, "big": big, "big_w": big_w, "back": back, "band": band, "floor": floor,
            "hand": hand_objs, "air": air, "head": head_signs, "lines": lines, "inside": inside, "held": held,
            "speech": p["speech"], "humans": humans}


def icon_w(vb, h):
    _, _, w, hh = (float(x) for x in vb.split())
    return max(8.0, min(h * w / hh, h * 1.9))


def look_dir(slots, i, speaker_idx, addr_idx):
    """Blickrichtung (−1 links, +1 rechts) einer Figur: Sprecher zum Angesprochenen, andere zum Sprecher."""
    me = slots[i]["x"]
    if speaker_idx is not None and i == speaker_idx and addr_idx is not None:
        return 1 if slots[addr_idx]["x"] > me else -1
    if speaker_idx is not None and i != speaker_idx:
        return 1 if slots[speaker_idx]["x"] > me else -1
    return 1 if me < W / 2 else -1


def arrow_ctrl(x1, y1, x2, y2, kind="act", bulge=None):
    """Kontrollpunkt der Handlungslinie (Bogen nach oben); bulge überschreibt die Wölbung (Ausweichen)."""
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy) or 1
    nx, ny = -dy / d, dx / d
    if ny > 0:
        nx, ny = -nx, -ny
    if bulge is None:
        bulge = 0 if kind == "go" else min(26 if kind == "throw" else 14, d * .22)
    return (x1 + x2) / 2 + nx * bulge, (y1 + y2) / 2 + ny * bulge


def arrow_pts(x1, y1, x2, y2, kind="act", bulge=None, n=24):
    mx, my = arrow_ctrl(x1, y1, x2, y2, kind, bulge)
    return [((1 - t) ** 2 * x1 + 2 * (1 - t) * t * mx + t * t * x2, (1 - t) ** 2 * y1 + 2 * (1 - t) * t * my + t * t * y2)
            for t in (i / n for i in range(n + 1))]


def arrow_svg(x1, y1, x2, y2, kind="act", divine=True, bulge=None):
    """Handlungslinie: act (Gott sendet, sieht, bestimmt), throw (werfen, speien), go (gehen, dem Boden entlang)."""
    # Bogen quer zur Verbindungslinie (nach oben gewölbt), nicht über den höheren Punkt hinaus: so geht eine Linie von Gott
    # direkt nach unten ab, statt zuerst nach oben (Hinweis Andi Neck 2026-10-18)
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy) or 1
    if d < 22:  # zu kurz für eine lesbare Linie (wirkte als loses Häkchen); die Nähe der Figuren zeigt den Bezug
        return ""
    if d < 36 and False:  # früher Winkel «>»/«<»; im Bildtest ohne Legende als Vergleichszeichen gelesen (2026-10-23), darum auch kurz ein Pfeil
        col = "#C08A2A" if kind == "act" and divine else "#3B3226"
        ang = math.atan2(dy, dx)
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        pts = [(cx - 4 * math.cos(ang) + 6 * math.cos(ang + a_), cy - 4 * math.sin(ang) + 6 * math.sin(ang + a_)) for a_ in (math.pi * .72, 0, -math.pi * .72)]
        pts[1] = (cx + 4 * math.cos(ang), cy + 4 * math.sin(ang))
        path = "M" + "L".join(f"{px:.1f} {py:.1f}" for px, py in pts)
        return (f'<path d="{path}" fill="none" stroke="#FFFDF6" stroke-width="5.6" stroke-linecap="round" stroke-linejoin="round" opacity=".85"/>'
                f'<path d="{path}" fill="none" stroke="{col}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
    mx, my = arrow_ctrl(x1, y1, x2, y2, kind, bulge)
    ang = math.atan2(y2 - my, x2 - mx)
    hx1, hy1 = x2 - 7 * math.cos(ang - .45), y2 - 7 * math.sin(ang - .45)
    hx2, hy2 = x2 - 7 * math.cos(ang + .45), y2 - 7 * math.sin(ang + .45)
    dash = ' stroke-dasharray="5 4"' if kind == "go" else (' stroke-dasharray="2 4"' if kind == "throw" else "")
    col = "#C08A2A" if kind == "act" and divine else "#3B3226"
    return (f'<path d="M{x1:.1f} {y1:.1f}Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="#FFFDF6" stroke-width="4.4" stroke-linecap="round" opacity=".8"/>'
            f'<path d="M{x1:.1f} {y1:.1f}Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="2"{dash} stroke-linecap="round"/>'
            f'<path d="M{hx1:.1f} {hy1:.1f}L{x2:.1f} {y2:.1f}L{hx2:.1f} {hy2:.1f}" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')


# ------------------------------------------------------------------ Worte im Bild (BILDPROZESS.md, Entscheid 2026-10-23)
# Ein Bild für alle Übersetzungen: jedes Wort steht je Sprache als eigener <text> mit Klasse lw-<sprache>; die App blendet
# nur die gewählte Sprache ein (data-tl am App-Element). Ohne App-Stil (Vorschau) gilt Hochdeutsch.
LANGS = ("de", "gsw")


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _lab(v):
    """Wort je Sprache: {"de": …, "gsw": …} oder eine Zeichenkette für alle."""
    if isinstance(v, str):
        return {k: v for k in LANGS}
    return {k: v.get(k) or v.get("de", "") for k in LANGS}


def text_w(s, fs):
    """Geschätzte Breite einer Zeile (serifenlose Schrift, fett)."""
    return sum(.36 if c in "il.,:;!'| " else (.82 if c in "mwMWÄÖÜ" else .6) for c in s) * fs


def ltext(x, y, v, fs=9, anchor="middle", weight="700", fill="#3B3226"):
    lab = _lab(v)
    if len(set(lab.values())) == 1:
        return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="sans-serif" font-size="{fs}" font-weight="{weight}" '
                f'fill="{fill}">{_esc(lab["de"])}</text>')
    return "".join(f'<text class="lw lw-{k}" x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="sans-serif" font-size="{fs}" '
                   f'font-weight="{weight}" fill="{fill}">{_esc(s)}</text>' for k, s in lab.items())


def lwidth(v, fs):
    return max(text_w(s, fs) for s in _lab(v).values())


def split2(s, fs, maxw):
    """Eine Zeile oder zwei möglichst gleich lange Zeilen (Umbruch an einem Leerzeichen), damit die Schrift nicht schrumpft."""
    if text_w(s, fs) <= maxw or " " not in s:
        return [s]
    ws = s.split(" ")
    best = min(range(1, len(ws)), key=lambda i: max(text_w(" ".join(ws[:i]), fs), text_w(" ".join(ws[i:]), fs)))
    return [" ".join(ws[:best]), " ".join(ws[best:])]


def splitn(s, fs, maxw, n):
    """Wie split2, aber bis n Zeilen: so wenige Zeilen wie möglich, sonst n möglichst gleich lange (Sprechblasen, 2026-10-26)."""
    if n <= 2:
        return split2(s, fs, maxw)
    ws = s.split(" ")
    best = None
    for k in range(1, min(n, len(ws)) + 1):
        import itertools
        for cuts in itertools.combinations(range(1, len(ws)), k - 1):
            b = [0, *cuts, len(ws)]
            ls = [" ".join(ws[b[i]:b[i + 1]]) for i in range(k)]
            m = max(text_w(x, fs) for x in ls)
            if best is None or (m <= maxw and (best[0] > maxw or len(ls) < len(best[1]) or (len(ls) == len(best[1]) and m < best[0]))) \
                    or (best[0] > maxw and m < best[0]):
                best = (m, ls)
        if best[0] <= maxw:
            break
    return best[1]


def lwrap(v, fs, maxw, n=2):
    """Zeilen je Sprache, Breite der breitesten Zeile und grösste Zeilenzahl (höchstens n Zeilen)."""
    lines = {k: splitn(s, fs, maxw, n) for k, s in _lab(v).items()}
    return lines, max(text_w(x, fs) for ls in lines.values() for x in ls), max(len(ls) for ls in lines.values())


def ltext_ml(x, yc, v, fs, maxw, weight="700", fill="#3B3226", n=2):
    """Text um die Mitte yc, bei Bedarf auf zwei (bis n) Zeilen umbrochen (je Sprache)."""
    lines, _, _ = lwrap(v, fs, maxw, n)
    lh = fs * 1.15
    out = []
    same = len({tuple(ls) for ls in lines.values()}) == 1
    for k, ls in (list(lines.items())[:1] if same else lines.items()):
        y0 = yc - len(ls) * lh / 2 + fs * .8
        cls = "" if same else f' class="lw lw-{k}"'
        spans = "".join(f'<tspan x="{x:.1f}" y="{y0 + i * lh:.1f}">{_esc(s)}</tspan>' for i, s in enumerate(ls))
        out.append(f'<text{cls} text-anchor="middle" font-family="sans-serif" font-size="{fs}" font-weight="{weight}" fill="{fill}">{spans}</text>')
    return "".join(out)


# ------------------------------------------------------------------ Zeichen zu Worten (Fassung «ohne Worte»)
NW_STOP = {"nicht", "keine", "keinen", "einen", "einem", "einer", "eines", "sein", "seine", "seiner", "seinen", "ihre", "ihren",
           "euer", "eure", "euch", "aber", "denn", "dass", "wenn", "wird", "werden", "sind", "sollt", "soll", "selig", "alle",
           "über", "unter", "durch", "gegen", "ohne", "oder", "noch", "auch", "schon", "jetzt", "sagt", "sage", "gesagt",
           "zeichen", "bild", "gruppe", "person", "mensch", "menschen", "dein", "deine", "deinem", "mein", "meine", "kein",
           "allgemein", "wie", "damit", "kommt", "kommen", "fest", "dort", "hier", "diese", "dieser", "dieses"}


def _nw_tokens(t):
    return [w for w in re.findall(r"[a-zäöüA-ZÄÖÜ]{4,}", str(t or "").lower()) if w not in NW_STOP]


def _nw_match(w, t):
    """Wort des Textes w passt zum Namenswort t: gleich, oder bei mindestens 5 Buchstaben eines Vorsilbe des anderen mit
    höchstens 3 Buchstaben Unterschied («Lichter»/«Licht», «Händen»/«Hände»)."""
    if w == t:
        return True
    return min(len(w), len(t)) >= 5 and abs(len(w) - len(t)) <= 3 and (w.startswith(t) or t.startswith(w))


NW_GLOBAL_KINDS = {"sign", "object", "place", "action", "divine"}


def nw_icons(comp, v, cands=(), n=2):
    """Zeichen zu einem Text für die Fassung «ohne Worte» (Hinweis Andi Neck 2026-10-25: keine leeren Felder).
    Ein Lexikon-Eintrag passt, wenn ALLE Wörter einer Namensfassung (Name vor einer Klammer, Fassungen durch «/» getrennt)
    im Text vorkommen. Zuerst unter den Zeichen, die im selben Feld schon vorkommen; sonst unter allen Zeichen,
    Gegenständen, Orten und Handlungen mit Darstellung (Personen und Rollen nur aus dem Feld selbst). Ergebnis: Liste von
    Lexikon-IDs (höchstens n), leer, wenn nichts passt – dann stehen die Anfangsbuchstaben."""
    txt = v.get("de") if isinstance(v, dict) else v
    words = _nw_tokens(txt)
    if not words:
        return []
    vbm = getattr(comp, "vbmap", {}) or {}
    idx = getattr(comp, "_nw_idx", None)
    if idx is None:
        idx = {}
        for fid, lx in comp.lex.items():
            if fid not in vbm:
                continue
            names = re.sub(r"\(.*?\)", " ", (lx.get("names") or {}).get("de", ""))
            alts = [set(_nw_tokens(a)) for a in re.split(r"[/,]", names)]
            idx[fid] = ([a for a in alts if a], lx.get("kind"))
        comp._nw_idx = idx

    def score(fid):
        best = ()
        for a in idx[fid][0]:
            if all(any(_nw_match(w, t) for w in words) for t in a) and len(a) > len(best):
                best = tuple(sorted(a))
        return best

    out, used = [], set()
    local = list(dict.fromkeys(c for c in cands if c in idx))
    glob_ = sorted(f for f in idx if idx[f][1] in NW_GLOBAL_KINDS)
    for pool in (local, glob_):
        best = sorted(((score(f), f) for f in pool if f not in out), key=lambda x: (-len(x[0]), x[1]))
        for sc, f in best:
            if sc and not set(sc) <= used:
                out.append(f)
                used |= set(sc)
            if len(out) >= n:
                return out
        if out:
            return out
    return out


_WZ = None


def zeichen(comp, wo, v, cands=(), auto=True):
    """Zeichen für ein Wortfeld (wo: zelle, titel, kopf, band, sprechblase): zuerst die geprüfte Zuordnung
    (bildauftraege_daten/_wortzeichen.json, je Bild und Text, sonst je Text), sonst – wenn auto – der Automat nw_icons.
    Zeichen erscheinen auch neben den Worten (Hinweis Andi Neck 2026-10-25), in der Ansicht «ohne Worte» statt ihrer."""
    global _WZ
    if _WZ is None:
        f = pathlib.Path(__file__).resolve().parent / "bildauftraege_daten/_wortzeichen.json"
        _WZ = {}
        if f.exists():
            for e in json.loads(f.read_text(encoding="utf-8")):
                ids = [i for i in e.get("zeichen") or [] if i in (getattr(comp, "vbmap", {}) or {})]
                _WZ[(e["bild"].upper(), e["wo"], e["text"])] = ids
                _WZ.setdefault((None, e["wo"], e["text"]), ids)
    txt = v.get("de") if isinstance(v, dict) else v
    import sys as _s
    # Kennung des laufenden Bildes: CUR_ID (gesetzt von bilder_anime.run); läuft bilder_anime als Skript, heisst das Modul
    # «__main__», und das frühere Nachschlagen über sys.modules["bilder_anime"] fand das Bild nicht (Prüfung 2026-10-26)
    cur = (CUR_ID[0] or "").replace("ILL-ANI-", "").upper() or (
        getattr(_s.modules.get("bilder_anime"), "CUR", [None])[0] or "").upper()
    for k in ((cur, wo, txt), (cur, "alle", txt), (None, wo, txt), (None, "alle", txt)):  # «alle»: gilt für jede Stelle im Bild
        if k in _WZ:
            return list(_WZ[k])
    return nw_icons(comp, v, cands) if auto else []


NW_FEHLT = []  # (Bild, Worte) ohne Zeichen im Modus «ohne Worte»
CUR_ID = [""]
BUBBLE_FAIL = []  # Felder, in denen keine Blasenlage alle Regeln erfüllt (Ausgabe in bilder_anime.run)


def _plain(v):
    return v.get("de") if isinstance(v, dict) else str(v)


def nw_fill(comp, x, y, w, h, icons, v, fill="#3B3226"):
    """Inhalt «ohne Worte» für ein Feld (x, y, w, h): nur Zeichen, gross und mittig (keine Worte, keine Anfangsbuchstaben)."""
    import bilder_diagramm as _bd
    if icons:
        C = _bd.Cells(comp)
        ih = max(8, h - 4)
        return C.icons(icons, x + w / 2, y + (h - ih) / 2, ih, w * .85)
    # keine Anfangsbuchstaben mehr (Hinweis Andi Neck 2026-10-25: «zu schwer zu erraten; 100 % ohne Text»): ohne Zeichen bleibt
    # das Feld leer und wird gemeldet (NW_FEHLT), damit jedes Wortfeld ein Zeichen bekommt
    NW_FEHLT.append((CUR_ID[0], _plain(v)))
    return ""


def panel_icons(p):
    """Alle Lexikon-IDs, die in einem Feld vorkommen (Figuren, Gegenstände, Zeichen, Zellen eines Strukturbilds)."""
    out = list(p.get("figures") or []) + list(p.get("objects") or []) + list(p.get("signs") or [])
    out = [x if isinstance(x, str) else (x.get("id") or x.get("figure") or "") for x in out]
    for s_ in p.get("speech") or []:
        out += list(s_.get("icons") or [])
    dg = p.get("diagram") or {}
    cells = list(dg.get("cells") or []) + [c for r in dg.get("rows") or [] for c in r]
    for k in ("cond", "yes", "no", "left", "right", "verdict", "top", "bottom", "core"):
        if isinstance(dg.get(k), dict):
            cells.append(dg[k])
        elif isinstance(dg.get(k), list):
            cells += [c for c in dg[k] if isinstance(c, dict)]
    for c in cells:
        out += list(c.get("icons") or []) + ([c["who"]] if c.get("who") else [])
    if dg.get("speaker"):
        out.append(dg["speaker"])
    return [x for x in out if x]


def sw(full, alt, frame=""):
    """Umschaltbare Gruppe: Worte (dg-full) und Fassung «ohne Worte» (dg-nw, nur im Modus «ohne Worte» sichtbar). Der Rahmen
    (frame) gehört mit in die Gruppe, damit Antippen auf dem ganzen Feld wirkt, nicht nur auf dem Zeichen (Hinweis 2026-10-25)."""
    return f'<g class="dg-sw">{frame}<g class="dg-full">{full}</g><g class="dg-nw" display="none">{alt}</g></g>'


def word_band(v, letter=False, comp=None, cands=()):
    """Stichwortband unter dem Feld: wenige Wörter aus dem Wortlaut; lieber zwei Zeilen als kleine Schrift (Hinweis Andi Neck).
    Ergebnis: (SVG, Höhe)."""
    extra = 16 + (14 if letter else 0)
    # Zeichen vor den Worten (Hinweis Andi Neck 2026-10-25): ihr Platz geht vom Text ab, bevor die Schrift bemessen wird
    # (sonst ragte der Text über das Band, Hinweis Andi Neck 2026-10-25)
    shown = zeichen(comp, "band", v, cands, auto=False) if comp is not None and not letter else None
    iw = 0
    if shown:
        import bilder_diagramm as _bd
        iw = _bd.Cells(comp).icon_row_w(shown, 12)
    maxw = W - 12 - extra - (iw + 4 if shown else 0)
    fs = 10
    lines, lw, n = lwrap(v, fs, maxw)
    while lw > maxw and fs > 7:
        fs -= .5
        lines, lw, n = lwrap(v, fs, maxw)
    if shown and lw > maxw:  # passt auch klein nicht: ohne Zeichen, die Worte gehen vor
        shown, iw, maxw, fs = None, 0, W - 12 - extra, 10
        lines, lw, n = lwrap(v, fs, maxw)
        while lw > maxw and fs > 7:
            fs -= .5
            lines, lw, n = lwrap(v, fs, maxw)
    h = 16 if n == 1 else 28
    w = min(W - 12, lw + extra)
    x = (W - w) / 2
    y = 1
    icon = ""
    if letter:  # Briefrahmen: kleiner Brief vor dem Wort (Auftrag im Brief)
        icon = (f'<rect x="{x + 6:.1f}" y="{y + h / 2 - 4:.1f}" width="11" height="8" rx="1" fill="#FFFDF6" stroke="#3B3226" stroke-width=".8"/>'
                f'<path d="M{x + 6:.1f} {y + h / 2 - 4:.1f}l5.5 4.4 5.5-4.4" fill="none" stroke="#3B3226" stroke-width=".8"/>')
    tx = x + w / 2 + (7 if letter else 0)
    if comp is None:
        frame = f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="3" fill="#FFF4D6" stroke="#3B3226" stroke-width="1"/>'
        return (f'<g class="ill-words">{frame}' + icon + ltext_ml(tx, y + h / 2, v, fs, maxw) + "</g>", h)
    if shown:
        ih = 12  # gleiche Höhe wie bei der Bemessung oben, damit der reservierte Platz stimmt
        w2 = min(W - 12, lw + extra + iw + 4)
        x = (W - w2) / 2
        icon = _bd.Cells(comp).icons(shown, x + 4 + iw / 2, y + (h - ih) / 2, ih, iw)
        tx = x + 4 + iw + 3 + (w2 - iw - 7) / 2
        w = w2
    frame = f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="3" fill="#FFF4D6" stroke="#3B3226" stroke-width="1"/>'
    alt = frame + nw_fill(comp, x + 2, y + 1, w - 4, h - 2, shown or zeichen(comp, "band", v, cands), v)
    return (f'<g class="ill-words">' + sw(frame + icon + ltext_ml(tx, y + h / 2, v, fs, maxw), alt) + "</g>", h)


def name_tag(x, y, v):
    """Namensschild beim ersten Auftreten einer Hauptfigur (unter dem Kinn, auf der Brust)."""
    fs = 7.5
    w = lwidth(v, fs) + 8
    x = min(W - 3 - w / 2, max(3 + w / 2, x))
    return (f'<g class="ill-name"><rect x="{x - w / 2:.1f}" y="{y - 7.5:.1f}" width="{w:.1f}" height="10" rx="5" fill="#FFFDF6" stroke="#3B3226" stroke-width=".7"/>'
            + ltext(x, y, v, fs) + "</g>")


def think_bubble(x, y, w, h, tx, ty, inner, attrs=""):
    """Denkblase als deutliche Wolke: Bögen rundum und drei kleiner werdende Kreise zur denkenden Figur (Hinweis Andi Neck
    2026-10-24: als Gedankenwolke erkennbar, nicht wie eine Sprechblase mit Rand)."""
    sw, col = 2.0, "#3B3226"
    r = max(5.5, min(9.0, h * .26))
    # Bogenmittelpunkte auf dem Rand eines abgerundeten Rechtecks, etwas nach innen
    pts = []
    nx = max(2, int(round((w - 2 * r) / (r * 1.45))))
    ny = max(1, int(round((h - 2 * r) / (r * 1.45))))
    for k in range(nx + 1):
        px = x + r * .7 + k * (w - 1.4 * r) / nx
        pts += [(px, y + r * .55), (px, y + h - r * .55)]
    for k in range(1, ny):
        py = y + r * .55 + k * (h - 1.1 * r) / ny
        pts += [(x + r * .55, py), (x + w - r * .55, py)]
    ring = "".join(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="#FFFFFF" stroke="{col}" stroke-width="{sw}"/>' for px, py in pts)
    fill = "".join(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r - sw / 2:.1f}" fill="#FFFFFF"/>' for px, py in pts)
    core = (f'<rect x="{x + r * .55:.1f}" y="{y + r * .55:.1f}" width="{w - r * 1.1:.1f}" height="{h - r * 1.1:.1f}" fill="#FFFFFF" '
            f'data-box="{x:.1f},{y:.1f},{w:.1f},{h:.1f}" data-tail="{tx:.1f},{ty:.1f}" data-think="1"{attrs}/>')
    # Kreise zur Figur: vom unteren Wolkenrand Richtung Kopf, enden knapp über dem Kopf
    ox, oy = min(max(tx, x + w * .25), x + w * .75), y + h + r * .3
    dots = "".join(f'<circle cx="{ox + (tx - ox) * f:.1f}" cy="{oy + (ty - 4 - oy) * f:.1f}" r="{rr}" fill="#FFFFFF" stroke="{col}" stroke-width="1.6"/>'
                   for f, rr in ((.22, 4.6), (.55, 3.2), (.85, 2.0)))
    return f'<g>{dots}{ring}{fill}{core}{inner}</g>'


# ------------------------------------------------------------------ gemeinsame Zeichner-Logik
class Composer:
    """Stilunabhängige Zeichenlogik; der Stil liefert die Bauteile (Methoden mit Präfix r_)."""
    uid = "x"

    def __init__(self, lex, extra):
        self.lex, self.extra = lex, extra
        self._n = 0

    def _draw_floor(self, L, st, items, out, pos):
        cnt = st.get("count", {})
        fx = st.get("floor_x", {})
        zx = getattr(self, "_zx", None) or L["floor_zone"][0]
        for t in items:
            w, h = self.m(t)[1]
            k = int(cnt.get(t, 1))
            if t in fx:
                x = fx[t]
            elif L["reserve"]:
                x = zx
                zx += w * min(k, 3) * .85 + 2
            else:
                x = (W - w * min(k, 3)) / 2
            if k > 7:
                w, h = w * .7, h * .7
            for q in range(min(k, 12)):
                dx = q * (w * .8) if k <= 3 else q * (w * (.55 if k <= 7 else .45))
                out.append(self.r_sym(t, x + dx, FLOOR_Y - h + 6 + (q % 2) * 2, w, h))
            pos[t] = (x + w / 2, FLOOR_Y - h / 2)
        self._zx = zx

    def covers(self, x, y, w, h, speaker, heads):
        """Verdeckt das Rechteck ein wesentliches Teil (Zeichen, Gegenstand) oder ein fremdes Gesicht?"""
        r = self.head_r()
        boxes = list(getattr(self, "ess", [])) + [(hx - r, hy - r * 1.2, 2 * r, r * 2.2) for f, (hx, hy) in heads.items() if f != speaker]
        return any(x < ex + ew - 1 and x + w > ex + 1 and y < ey + eh - 1 and y + h > ey + 1 for ex, ey, ew, eh in boxes)

    def clear_bulge(self, x1, y1, x2, y2, kind, f, t, heads, pos, bubbles):
        """Lage einer Handlungslinie, die keine fremden Köpfe, Zeichen oder Blasen schneidet (Hinweis Andi Neck 2026-10-24:
        Pfeile verdecken nichts Wesentliches, wenn sie ausweichen können). Versucht stärkere Wölbung und, bei Personen, einen
        seitlichen Ansatz am Kopf. Endpunkte und ihre eigenen Zeichen zählen nicht. Gibt (x1, y1, x2, y2, bulge) zurück."""
        r = self.head_r()
        ends = [(x1, y1), (x2, y2)] + [pos[k] for k in (f, t) if k in pos]
        near_end = lambda cx, cy: any(math.hypot(cx - ex, cy - ey) < r * 1.6 for ex, ey in ends)  # noqa: E731
        obst = [(hx - r * 1.05, hy - r * 1.35, r * 2.1, r * 2.4) for k, (hx, hy) in heads.items() if k not in (f, t)]
        obst += [b for b in getattr(self, "ess", []) if not near_end(b[0] + b[2] / 2, b[1] + b[3] / 2)]
        bub = [(bx - 2, by - 2, bw + 4, bh + 4) for bx, by, bw, bh in bubbles]

        def bad(a, b, c, d, bulge):
            pts = arrow_pts(a, b, c, d, kind, bulge)
            if any(py < 3 or not 2 <= px <= 184 for px, py in pts):
                return 99
            n = sum(1 for px, py in pts[2:-2] for ox, oy, ow, oh in obst if ox <= px <= ox + ow and oy <= py <= oy + oh)
            return n + 3 * sum(1 for px, py in pts for ox, oy, ow, oh in bub if ox <= px <= ox + ow and oy <= py <= oy + oh)

        base = None if kind != "go" else 0
        b0 = bad(x1, y1, x2, y2, base)
        if b0 == 0 or kind == "go":
            return x1, y1, x2, y2, base
        starts = [(x1, y1)]
        if f in heads:  # seitlich am Kopf ansetzen (Schulterhöhe), Richtung Ziel zuerst
            hx, hy = heads[f]
            sd = 1 if x2 > hx else -1
            starts += [(hx + sd * r * 1.5, hy - r * .2), (hx + sd * r * 1.7, hy + r * 1.1)]
        best = (b0, 0, (x1, y1, base))
        for k, (sx, sy) in enumerate(starts):
            d = math.hypot(x2 - sx, y2 - sy)
            for bulge in [base, 20, 28, 36, 46, 58, 72, -14, -24]:
                if bulge is not None and abs(bulge) >= d * 1.1:
                    continue
                sc = (bad(sx, sy, x2, y2, bulge), k, (sx, sy, bulge))
                if sc[:2] < best[:2]:
                    best = sc
        sx, sy, bulge = best[2]
        return sx, sy, x2, y2, bulge

    # Grenzen für Spitzen (Feldeinheiten; pruefe_bilder.py meldet ab 36 bzw. ab 25 Einheiten flacher als 35°): der Zeichner hält
    # etwas Abstand zu den Prüfgrenzen
    TAIL_MAX, TAIL_FLAT, TAIL_ANG = 33, 22, 38
    BUB_SCALES = (1, .92, .84, .76, .68, .6, .54)

    def _tail(self, x, y, w, h, tx, ty):
        """Ansatz und Masse der Spitze wie in _bubble.bubble_path: (Ansatz x, Ansatz y, Länge, Winkel zur Waagrechten)."""
        R, HALF = getattr(self, "bub_r", (12, 5))
        dx = tx - min(max(tx, x), x + w)
        dy = ty - min(max(ty, y), y + h)
        side = ("b" if dy > 0 else "t") if abs(dy) >= abs(dx) else ("r" if dx > 0 else "l")
        bx = min(max(tx, x + R + HALF), x + w - R - HALF)
        by = min(max(ty, y + R + HALF), y + h - R - HALF)
        px, py = {"b": (bx, y + h), "t": (bx, y), "l": (x, by), "r": (x + w, by)}[side]
        L_ = math.hypot(tx - px, ty - py)
        return px, py, L_, math.degrees(math.atan2(abs(ty - py), abs(tx - px) or 1e-9))

    @staticmethod
    def _seg_hits(x1, y1, x2, y2, box, m=0.0, n=24):
        bx, by, bw, bh = box
        return any(bx + m < x1 + (x2 - x1) * k / n < bx + bw - m and by + m < y1 + (y2 - y1) * k / n < by + bh - m for k in range(1, n))

    @staticmethod
    def _cross(a, b):
        """Schneiden sich die Strecken a und b (je x1, y1, x2, y2)?"""
        def o(p, q, r):
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        p1, p2, p3, p4 = a[:2], a[2:], b[:2], b[2:]
        return o(p1, p2, p3) * o(p1, p2, p4) < 0 and o(p3, p4, p1) * o(p3, p4, p2) < 0

    def place_bubbles(self, L, st, heads, sky, pos, p):
        """Lage aller Sprech- und Denkblasen eines Felds (Abschnitt 10 in panel). Gibt (placed, drawn) zurück:
        placed = [(x, Breite, Unterkante, Höhe)], drawn = [(x, y, w, h, Spitze x, Spitze y, Inhalt, Denkblase, Index[, Folgeblase])].

        Ablauf: Jede Sprech-Angabe wird eine Blase; zwei Angaben derselben Figur bilden ein verbundenes Paar (nebeneinander
        oder untereinander). Für alle Einheiten eines Felds wird je Grösse (gross zuerst, alle gleich gross) die Lage gesucht,
        die alle Regeln erfüllt und die kürzesten Spitzen nahe beim Sprecher hat:
        - keine Blase über einem Gesicht (auch dem eigenen, bei Gruppen mit den hinteren Köpfen), Zeichen, Gegenstand, der
          Kreuzestafel, dem Strahlenkranz oder einer anderen Blase; die Feldnummer bleibt frei;
        - Spitze höchstens TAIL_MAX lang, ab TAIL_FLAT nicht flacher als TAIL_ANG; nicht hinter einer Blase, nicht durch
          Gesichter, Zeichen oder die Tafel, keine zwei Spitzen kreuzen sich."""
        r = self.head_r()
        ih0 = self.icon_h()
        WMAX = 104  # breiter: zweizeilig statt kleiner (Hinweis Andi Neck 2026-10-23)
        VARIANTS = [(WMAX, 2), (66, 2), (84, 3)]
        V4 = (88, 4)  # nur auf der letzten Stufe: vier Zeilen
        group = lambda f: f.startswith("FIG-GRUPPE-") or f in GROUPS  # noqa: E731
        ess = list(getattr(self, "ess", []))

        def face(f, relax):
            hx, hy = heads[f]
            if group(f) and f not in L["inside"] and not relax:  # Gruppe mit den hinteren Köpfen (Hinweis Andi Neck 2026-10-26)
                return (hx - r * 2.05, hy - r * 2.1, r * 4.1, r * 3.15)
            return (hx - r * 1.1, hy - r * 1.3, r * 2.2, r * 2.4)

        # Einheiten: (Liste der Angaben, Ziele der Spitze); Ziele: Scheitel oder seitlich am Kopf (am Kreuz steht die Tafel darüber)
        def build(strip):
          items = []
          for si, sp in enumerate(L["speech"]):
            sp = dict(sp)
            if sp.get("word") and "§W" not in sp["icons"]:  # Kernwort in der Sprechblase, vor höchstens zwei Zeichen
                sp["icons"] = ["§W"] + list(sp["icons"])
            if strip and sp.get("word"):  # letzte Stufe: nur das Wort, ohne Zeichen daneben
                sp["icons"] = ["§W"]
            # Fassungen des Worts: Zeilenbreite und höchstens 2 oder 3 Zeilen (schmaler und höher statt kleiner)
            ws, hb = {}, {}
            for V in VARIANTS + [V4]:
                ws[V] = [lwrap(sp["word"], 10, V[0], V[1])[1] if i == "§W" else icon_w(self.vb(i), ih0) for i in sp["icons"]]
                nl = lwrap(sp["word"], 10, V[0], V[1])[2] if sp.get("word") else 1
                hb[V] = max(ih0, nl * 11.5 + 1)
            f = sp["from"]
            if f in sky:
                tg = None
            elif f in heads:
                hx, hy = heads[f]
                tg = [(hx, hy - r, 0), (hx - r * 1.08, hy - r * .35, 4), (hx + r * 1.08, hy - r * .35, 4)]
            elif f in pos:  # sprechendes Bauteil (z. B. Satan als Schatten): Spitze an den oberen Rand
                tx, ty = pos[f]
                tg = [(tx, ty - self.m(f)[1][1] * .4, 0)]
            else:
                continue
            items.append(dict(sp=sp, si=si, ws=ws, hb=hb, tg=tg, f=f))
          units, used = [], set()
          for k, it in enumerate(items):
            if k in used:
                continue
            mate = next((j for j in range(k + 1, len(items)) if j not in used and items[j]["f"] == it["f"] and it["tg"] is not None
                         and bool(items[j]["sp"].get("think")) == bool(it["sp"].get("think"))), None)
            if mate is not None:
                used.add(mate)
                units.append([it, items[mate]])
            else:
                units.append([it])
          return items, units
        items, units = build(False)

        def dims(it, V, sc):
            return sum(it["ws"][V]) * sc + 5 * (len(it["ws"][V]) - 1) + 12, it["hb"][V] * sc + 12

        # Grössen: Massstab und Zeilenbreite des Worts (schmaler umbrochen, zweizeilig, statt kleiner)
        LEVELS = [(sc, V) for sc in self.BUB_SCALES for V in VARIANTS]

        def box_ok(x, y, w, h, statics, relax):
            if x < 5 or x + w > W - 5 or y < 5 or y + h > H - 15:
                return False
            if y < 25 and x < 27:  # Feldnummer oben links frei lassen
                return False
            for f in heads:
                ex, ey, ew, eh = face(f, relax)
                if x < ex + ew and x + w > ex and y < ey + eh and y + h > ey:
                    return False
            for ex, ey, ew, eh in ess:
                if x < ex + ew - 1 and x + w > ex + 1 and y < ey + eh - 1 and y + h > ey + 1:
                    return False
            for ex, ey, ew, eh in getattr(self, "soft", []):  # wie pruefe_bilder.py: höchstens 15 % eines kleineren Teils
                if ew * eh <= w * h and max(0, min(x + w, ex + ew) - max(x, ex)) * max(0, min(y + h, ey + eh) - max(y, ey)) > .15 * ew * eh:
                    return False
            for gx, gy, gw, gh in list(sky.values()):
                if x < gx + gw + 4 and x + w > gx - 4 and y < gy + gh + 2 and y + h > gy - 2:
                    return False
            for b in statics:  # Blasen Gottes (fest gesetzt)
                if x < b["x"] + b["w"] + 4 and x + w > b["x"] - 4 and y < b["y"] + b["h"] + 3 and y + h > b["y"] - 3:
                    return False
                if self._seg_hits(b["bx"], b["by"], b["tip"][0], b["tip"][1], (x, y, w, h), 1):
                    return False
            return True

        def tail_ok(x, y, w, h, tx, ty, own, statics, relax):
            px, py, L_, ang = self._tail(x, y, w, h, tx, ty)
            tmax, tflat, tang = (self.TAIL_MAX, self.TAIL_FLAT, self.TAIL_ANG) if not relax else (35, 24, 36)  # knapp unter den Prüfgrenzen
            if L_ < 5 or L_ > tmax or (L_ > tflat and ang < tang):
                return None
            if x - 1 < tx < x + w + 1 and y - 1 < ty < y + h + 1:
                return None
            for b in statics:
                if self._seg_hits(px, py, tx, ty, (b["x"], b["y"], b["w"], b["h"]), 1) or self._cross((px, py, tx, ty), (b["bx"], b["by"], *b["tip"])):
                    return None
            for f, (hx, hy) in heads.items():  # nicht durch fremde Gesichter
                if f != own and self._seg_hits(px, py, tx, ty, (hx - r * .95, hy - r * 1.1, r * 1.9, r * 2.1)):
                    return None
            for e in ess:  # nicht über Zeichen, Gegenstände und die Kreuzestafel (ausser dem, an dem sie endet)
                ex, ey, ew, eh = e
                if ex - 3 < tx < ex + ew + 3 and ey - 3 < ty < ey + eh + 3:
                    continue
                if self._seg_hits(px, py, tx, ty, e, min(ew, eh) * .15):
                    return None
            return px, py, L_, ang

        def god(it):
            """Blase Gottes nahe beim Strahlenkranz, Spitze reicht hinein; nicht über anderen Zeichen am Himmel (z. B. der Taube),
            Gesichtern oder Zeichen; Spitze kurz und nicht flach (wie bei Menschen)."""
            gx, gy, gw, gh = sky[it["f"]]
            ws = it["ws"][VARIANTS[0]]
            others = [b for k2, b in sky.items() if k2 != it["f"]]
            best = None
            for sc in (1, .9, .8, .7, .6, .5):
                w, h = dims(it, VARIANTS[0], sc)
                for y in range(5, 76, 3):
                    for x in range(5, int(W - 5 - w) + 1, 3):
                        if y < 25 and x < 27:
                            continue
                        if x < gx + gw + 2 and x + w > gx - 2 and y < gy + gh + 2 and y + h > gy - 2:
                            continue
                        tx, ty = (gx + gw * .78, gy + gh / 2) if x + w / 2 > gx + gw / 2 else (gx + gw * .22, gy + gh / 2)  # Spitze reicht in den Strahlenkranz
                        px, py, L_, ang = self._tail(x, y, w, h, tx, ty)
                        if L_ > self.TAIL_MAX or (L_ > self.TAIL_FLAT and ang < self.TAIL_ANG):
                            continue
                        if any(x < ox + ow + 3 and x + w > ox - 3 and y < oy + oh + 2 and y + h > oy - 2 or self._seg_hits(px, py, tx, ty, (ox, oy, ow, oh))
                               for ox, oy, ow, oh in others):
                            continue
                        if any(x < ex + ew - 1 and x + w > ex + 1 and y < ey + eh - 1 and y + h > ey + 1 for ex, ey, ew, eh in ess if (ex, ey, ew, eh) != (gx, gy, gw, gh)):
                            continue
                        if any(x < fx + fw and x + w > fx and y < fy + fh and y + h > fy for fx, fy, fw, fh in (face(f, 0) for f in heads)):
                            continue
                        c = (1 - sc) * 50 + abs(L_ - 18) + (y - 5) * .2
                        if best is None or c < best[0]:
                            best = (c, dict(it=it, x=x, y=y, w=w, h=h, sc=sc, V=VARIANTS[0], tip=(tx, ty), bx=px, by=py))
                if best is not None:
                    break
            if best is None:  # wie früher: rechts bzw. links neben dem Strahlenkranz (pruefe_bilder.py meldet Befunde)
                w, h = dims(it, VARIANTS[0], .6)
                x = max(28, min(W - 5 - w, gx + gw + 14 if gx < W / 2 else gx - w - 14))
                tx, ty = (gx + gw * .78, gy + gh / 2) if gx < W / 2 else (gx + gw * .22, gy + gh / 2)
                px, py, _, _ = self._tail(x, 8, w, h, tx, ty)
                BUBBLE_FAIL.append((CUR_ID[0], "Gott"))
                return dict(it=it, x=x, y=8, w=w, h=h, sc=.6, V=VARIANTS[0], tip=(tx, ty), bx=px, by=py)
            return best[1]

        statics = [god(u[0]) for u in units if u[0]["tg"] is None]
        free_units = [u for u in units if u[0]["tg"] is not None]

        def cands(u, lv, relax):
            """Gültige Lagen einer Einheit gegen das Feste (Gesichter, Zeichen, Gott), beste zuerst: [(Kosten, [Blasen])]."""
            out_ = []
            pref_y = st.get("bubble_y")
            own = u[0]["f"]
            hy_own = heads[own][1] if own in heads else H
            sc, V = lv
            if V != VARIANTS[0] and not any(it["sp"].get("word") for it in u):
                return []  # ohne Wort keine andere Fassung
            sz = [dims(it, V, sc) for it in u]
            # Anordnungen: einzeln; Paar nebeneinander (Spitze an der linken oder rechten Blase) oder untereinander
            if len(u) == 1:
                lays = [((0, 0),)]
            else:
                (w1, h1), (w2, h2) = sz
                hh = max(h1, h2)
                lays = [((0, (hh - h1) / 2), (w1 + 6, (hh - h2) / 2), 0), ((0, (hh - h1) / 2), (w1 + 6, (hh - h2) / 2), 1)]
                for dx2 in {0, (w1 - w2) / 2, w1 - w2}:
                    lays.append(((max(0, -dx2), 0), (max(0, dx2), h1 + 6), 1))
            for lay in lays:
                offs = lay[:len(u)]
                ti = lay[len(u)] if len(u) > 1 else 0  # Blase mit der Spitze zum Sprecher
                bw_ = max(o[0] + s_[0] for o, s_ in zip(offs, sz))
                bh_ = max(o[1] + s_[1] for o, s_ in zip(offs, sz))
                tw, th = sz[ti]
                for tx, ty, pen in u[0]["tg"]:
                    ox, oy = offs[ti]
                    x0, x1 = max(5, int(tx - self.TAIL_MAX - tw - ox)), min(int(W - 5 - bw_), int(tx + self.TAIL_MAX - ox))
                    y0, y1 = max(5, int(ty - self.TAIL_MAX - th - oy)), min(int(H - 15 - bh_), int(ty + self.TAIL_MAX - oy))
                    for y in range(y0, y1 + 1, 2):
                        if y + bh_ > hy_own + r * .5:
                            continue  # nicht tiefer als der Kopf des Sprechers
                        for x in range(x0, x1 + 1, 2):
                            bs = [(x + o[0], y + o[1], s_[0], s_[1]) for o, s_ in zip(offs, sz)]
                            if not all(box_ok(*b_, statics, relax) for b_ in bs):
                                continue
                            t = tail_ok(*bs[ti], tx, ty, own, statics, relax)
                            if not t:
                                continue
                            c = abs(t[2] - 15) + .12 * abs(bs[ti][0] + bs[ti][2] / 2 - tx) + pen + (1 - sc) * 50 + (VARIANTS + [V4]).index(V) * 2
                            # zur angesprochenen Person hin (Blindtest 2026-10-26: «Frau, siehe, dein Sohn!» stand beim Jünger)
                            for it_, b_ in zip(u, bs):
                                to_ = it_["sp"].get("to")
                                if to_ in heads and to_ != own:
                                    c += .06 * abs(b_[0] + b_[2] / 2 - heads[to_][0])
                            if pref_y is not None:
                                c += abs(y - pref_y) * .3
                            if len(u) > 1:
                                c += 0 if lay[1][1] == lay[0][1] or lay[1][0] > 0 else 2  # nebeneinander leicht bevorzugt
                            blist = []
                            for j, (it, b_) in enumerate(zip(u, bs)):
                                d = dict(it=it, x=b_[0], y=b_[1], w=b_[2], h=b_[3], sc=sc, V=V)
                                if j == ti:
                                    d.update(tip=(tx, ty), bx=t[0], by=t[1])
                                blist.append(d)
                            if len(u) > 1:  # verbundene Blase: kurze Spitze an den Rand der Blase mit der Spitze
                                a, o_ = blist[ti], blist[1 - ti]
                                if abs(o_["y"] - a["y"]) < 1e-6 or o_["y"] < a["y"] + a["h"] / 2 and o_["y"] + o_["h"] > a["y"]:
                                    ex_ = a["x"] + .5 if o_["x"] + o_["w"] <= a["x"] + 1 else a["x"] + a["w"] - .5
                                    my = max(a["y"], o_["y"]) + (min(a["y"] + a["h"], o_["y"] + o_["h"]) - max(a["y"], o_["y"])) / 2
                                    o_.update(tip=(ex_, my), link=True)
                                else:  # untereinander: obere Blase zeigt auf die untere
                                    o_.update(tip=(a["x"] + a["w"] / 2 if abs(a["x"] + a["w"] / 2 - (o_["x"] + o_["w"] / 2)) < o_["w"] / 2 - 14 else o_["x"] + o_["w"] / 2, a["y"] + .5), link=True)
                                o_["bx"], o_["by"] = self._tail(o_["x"], o_["y"], o_["w"], o_["h"], *o_["tip"])[:2]
                            out_.append((c, blist))
            out_.sort(key=lambda z: z[0])
            res, seen = [], []
            for c, bl in out_:  # verschiedene Lagen (sonst nur Nachbarn derselben Lage)
                b0 = bl[0]
                if any(abs(b0["x"] - s_["x"]) < 5 and abs(b0["y"] - s_["y"]) < 5 for s_ in seen):
                    continue
                seen.append(b0)
                res.append((c, bl))
                if len(res) >= 90:
                    break
            return res

        def compatible(A, B):
            for a in A:
                for b in B:
                    if a["x"] < b["x"] + b["w"] + 4 and a["x"] + a["w"] > b["x"] - 4 and a["y"] < b["y"] + b["h"] + 3 and a["y"] + a["h"] > b["y"] - 3:
                        return False
            for P, Q in ((A, B), (B, A)):
                for a in P:
                    if not a.get("tip") or a.get("link"):
                        continue
                    for b in Q:
                        if self._seg_hits(a["bx"], a["by"], a["tip"][0], a["tip"][1], (b["x"], b["y"], b["w"], b["h"]), 1):
                            return False
                        if b.get("tip") and not b.get("link") and self._cross((a["bx"], a["by"], *a["tip"]), (b["bx"], b["by"], *b["tip"])):
                            return False
            return True

        def order_pen(A, B):
            """Leserichtung: eine spätere Einheit steht nicht links über einer früheren."""
            a, b = A[0], B[0]
            if b["x"] + b["w"] / 2 < a["x"] + a["w"] / 2 - 4:
                return 25 if b["y"] + b["h"] < a["y"] + a["h"] / 2 else 10
            return 15 if b["y"] + b["h"] < a["y"] + a["h"] / 2 else 0  # spätere ganz über der früheren

        def search(lists):
            best = [None, 1e9]
            mins = [min((c for c, _ in l_), default=1e9) for l_ in lists]

            def rec(k, chosen, cost):
                if cost + sum(mins[k:]) >= best[1]:
                    return
                if k == len(lists):
                    best[:] = [list(chosen), cost]
                    return
                for c, bl in lists[k]:
                    if cost + c + sum(mins[k + 1:]) >= best[1]:
                        break
                    if all(compatible(bl, ch) for ch in chosen):
                        rec(k + 1, chosen + [bl], cost + c + sum(order_pen(ch, bl) for ch in chosen))
            rec(0, [], 0)
            return best[0]

        sol, how = None, ""
        if free_units:
            cache = {}

            def cl(i, lv, relax):
                if (i, lv, relax) not in cache:
                    cache[(i, lv, relax)] = cands(free_units[i], lv, relax)
                return cache[(i, lv, relax)]
            # Stufen: 0 streng; 1 Gruppen nur mit dem vorderen Kopf, Spitzen bis knapp unter die Prüfgrenze; 2 dazu Wortblasen
            # ohne die Zeichen daneben (Kernwort genügt, BILDPROZESS.md)
            for relax in (0, 1, 2):
                if relax == 2:
                    items, units = build(True)
                    statics = [god(u[0]) for u in units if u[0]["tg"] is None]
                    free_units = [u for u in units if u[0]["tg"] is not None]
                    cache.clear()
                found = None
                levels = LEVELS + ([(sc, V4) for sc in self.BUB_SCALES] + [(.5, V) for V in VARIANTS + [V4]] if relax == 2 else [])
                for n_, lv in enumerate(levels):
                    if found is not None and n_ > found + 3:
                        break  # nach der ersten Lösung noch drei kleinere Stufen vergleichen (kürzere Spitze kann besser sein)
                    lists = []
                    for i in range(len(free_units)):  # jede Einheit wählt ihre Grösse selbst (bis zu dieser Stufe)
                        m_ = sorted((c for l2 in levels[:n_ + 1] for c in cl(i, l2, relax)[:30]), key=lambda z: z[0])
                        lists.append(m_)
                    if os.environ.get("BIBLE_BUBBLE_DEBUG") == "3":
                        print("  Stufe", lv, relax, [[(round(c), [(round(b["x"]), round(b["y"]), round(b["w"]), round(b["h"])) for b in bl]) for c, bl in cl(i, lv, relax)[:6]] for i in range(len(free_units))])
                    if os.environ.get("BIBLE_BUBBLE_DEBUG") == "2":
                        print("  Stufe", lv, relax, [len(l_) for l_ in lists], [[(round(c), [(round(b["x"]), round(b["y"]), round(b["w"]), round(b["h"]), b.get("tip")) for b in bl]) for c, bl in l_[:4]] for l_ in lists])
                    if all(lists):
                        s_ = search(lists)
                        if s_ is not None:
                            cost = sum(c for i, bl in enumerate(s_) for c, b2 in lists[i] if b2 is bl)
                            if sol is None or cost < sol[1]:
                                sol, how = (s_, cost), f"{lv} Stufe {relax}"
                            if found is None:
                                found = n_
                if sol is not None:
                    sol = sol[0]
                    break
            if sol is None:  # keine Lage erfüllt alle Regeln: über dem Sprecher (pruefe_bilder.py meldet den Befund)
                how = "ohne Lösung"
                sol = []
                for u in free_units:
                    bl, y = [], None
                    for it in u:
                        w, h = dims(it, VARIANTS[0], .6)
                        tx, ty, _ = it["tg"][0]
                        y = max(5, ty - h - 16) if y is None else y - h - 6
                        bl.append(dict(it=it, x=max(28, min(W - 5 - w, tx - w / 2)), y=y, w=w, h=h, sc=.6, V=VARIANTS[0], tip=(tx, ty)))
                    sol.append(bl)
        if items and os.environ.get("BIBLE_BUBBLE_DEBUG"):
            print("BLASEN", CUR_ID[0], how, [[(round(b["x"]), round(b["y"]), round(b["w"]), round(b["h"]), b["sc"], b["V"], b.get("tip"), b.get("bx"), b.get("by")) for b in bl] for bl in (sol or [])])
        if how == "ohne Lösung":
            BUBBLE_FAIL.append((CUR_ID[0], len(items)))
        allb = statics + [b for bl in (sol or []) for b in bl]
        allb.sort(key=lambda b: b["it"]["si"])
        placed, drawn = [], []
        for b in allb:
            sp, si = b["it"]["sp"], b["it"]["si"]
            sc, V = b["sc"], b["V"]
            wm, nl = V
            ws = [w * sc for w in b["it"]["ws"][V]]
            ih = ih0 * sc  # Zeichen
            th = b["it"]["hb"][V] * sc  # Textfeld (bis drei Zeilen)
            bx, by, bw, bh = b["x"], b["y"], b["w"], b["h"]
            inner, x = [], bx + 6
            for i, w in zip(sp["icons"], ws):
                if i == "§W":
                    fs_ = min(10, 10 * w / max(1, lwrap(sp["word"], 10, wm, nl)[1]))
                    own = [j for j in sp["icons"] if j != "§W"]
                    mi = [j for j in zeichen(self, "sprechblase", sp["word"], panel_icons(p)) if j not in own]
                    inner.append(sw(ltext_ml(x + w / 2, by + 6 + th / 2, sp["word"], fs_, wm * fs_ / 10, n=nl),
                                    nw_fill(self, x, by + 5 + (th - ih) / 2, w, ih + 2, mi, sp["word"])))
                else:
                    inner.append(self.r_icon(i, x, by + 6 + (th - ih) / 2, w, ih))
                x += w + 5
            tx, ty = b["tip"]
            drawn.append((bx, by, bw, bh, tx, ty, "".join(inner), bool(sp.get("think")), si) + ((True,) if b.get("link") else ()))
            placed.append((bx, bw, by + bh, bh))
        return placed, drawn

    def m(self, t):
        if t.startswith("_"):
            return ("band", (186, 70))
        return meta(t, self.lex, self.extra)

    def panel(self, p):
        if p.get("diagram"):  # Strukturbild (bilder_diagramm.py): Kachel nach Inhalt, Stichwortband wie bei Szenen
            import bilder_diagramm
            dg = p["diagram"]
            if "span" not in dg:  # hohe schmale Kachel wird breit (weniger Leerfläche neben ihr, Hinweis Andi Neck 2026-10-24)
                b1 = bilder_diagramm.diagram(self, dict(dg, span=1))
                if b1[2] > 175 and dg["visual"] != "dialogue":
                    dw = dict(dg, span=2)
                    if dw.get("cols"):
                        dw["cols"] = min(4, dw["cols"] * 2)
                    dg = dw
            body, w, h = bilder_diagramm.diagram(self, dg)
            self.sizes = getattr(self, "sizes", []) + [(w, h)]
            # breite Kachel: zusätzlich eine schmale Fassung fürs Handy (gleicher Inhalt, weniger Spalten)
            alt = None
            if dg.get("span") == 2:
                dn = dict(dg, span=1)
                if dn.get("cols"):
                    dn["cols"] = min(2, dn["cols"])
                if p["diagram"].get("cols"):
                    dn["cols"] = min(2, p["diagram"]["cols"])
                alt = bilder_diagramm.diagram(self, dn)
            self.alts = getattr(self, "alts", []) + [alt]
            self.bands = getattr(self, "bands", [])
            self.bands.append(word_band(p["keywords"], letter=bool(p.get("letter")), comp=self, cands=panel_icons(p)) if p.get("keywords") else "")
            return body
        self.sizes = getattr(self, "sizes", []) + [(W, H)]
        self.alts = getattr(self, "alts", []) + [None]
        self._n += 1
        self._zx = None
        L = plan(p, self.lex, self.extra)
        st = L["st"]
        out = []
        self.ess = []  # wesentliche Teile (Zeichen, Gegenstände, Köpfe): Sprechblasen und Pfeile verdecken sie nicht
        self.soft = []  # grosse Teile (Orte im Hintergrund, grosse Gegenstände): Blasen verdecken höchstens einen kleinen Teil
        self._rec = True
        pos = {}  # Mittelpunkte für Handlungslinien
        # 1. Hintergrund (bei Nacht dunkler Himmel mit Sternen)
        night = st.get("night") or "FIG-ZEICHEN-NACHT" in p["signs"]
        if night:
            out.append(f'<rect x="0" y="0" width="{W}" height="{FLOOR_Y}" fill="#24304E"/>'
                       + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#F2E6CC" opacity=".85"/>'
                                 for x, y, r in ((22, 30, 1), (58, 14, .8), (96, 26, 1.1), (132, 12, .8), (164, 34, 1), (148, 58, .7), (40, 60, .7), (110, 52, .8))))
        for t in L["band"]:
            out.append(self.r_band(t))
        if not L["band"]:
            out.append(self.r_floor())
        if p.get("letter"):  # Auftrag im Brief: Briefrand (gestrichelt), damit das Verlangte nicht als Erzählung gelesen wird
            out.append(f'<rect x="3.5" y="3.5" width="{W - 7}" height="{H - 7}" rx="4" fill="none" stroke="#B08A4A" stroke-width="1.4" stroke-dasharray="6 3"/>')
        for t in L["band"]:
            pos[t] = (W * .78, 112)
        WATER = {"FIG-ORT-SEE", "FIG-ORT-MEER-OFFEN", "_MEER-STILL", "FIG-ORT-UFER"}
        if L["row"] and any(b in WATER for b in L["band"]) and not st.get("in_water") and "FIG-ORT-UFER" not in L["band"]:
            out.append(self.r_sym("_STRAND", 0, 106, 186, 34))  # Personen stehen am Ufer, nicht im Wasser
        for i, t in enumerate(L["back"]):
            w, h = self.m(t)[1]
            side = st.get("back_side", "right")
            x = (W - w - 4) if side == "right" else 4
            if i == 1:
                x = 4 if side == "right" else W - w - 4
            y = (WATER_TOP - h + 6) if L["band"] and t != "FIG-ORT-TIEFE" and not L["band"][0].startswith("_HAFEN") else FLOOR_Y - h + 2
            out.append(self.r_back(t, x, y, w, h))
            pos[t] = (x + w / 2, y + h / 2)
        # 2. Gott/Geist oben
        spk = {s["from"] for s in L["speech"]}
        sky = {}
        for d in L["divine"]:
            w, h = self.m(d)[1]
            if d == "FIG-GOTT":
                x = 26 if (d in spk or st.get("god_side") == "left") else W - w - 6
                if st.get("god_side") == "right":
                    x = W - w - 6
                if st.get("god_side") == "center":
                    x = (W - w) / 2
                y = 3
            else:
                x, y = (W - w) / 2, 4
            sky[d] = (x, y, w, h)
            pos[d] = (x + w / 2, y + h * .6)
            out.append(self.r_sym(d, x, y, w, h))
        # 3. grosse Gegenstände (Schiff, Fisch)
        bigpos = {}
        for t in L["big"][:1]:
            w0, h0 = self.m(t)[1]
            w = L["big_w"]
            h = h0 * w / w0
            if L["row"]:
                x = W - w - 4 if st.get("big_side", "right") == "right" else 4
            else:
                x = (W - w) / 2
            water = L["band"] and L["band"][0] != "FIG-ORT-TIEFE"
            if t in SHIPS:
                wl = 114 if L["band"][0].startswith("_HAFEN") else WATER_TOP + 4
                y = wl - h * .74 if water else FLOOR_Y - h + 8
            elif t == "FIG-OBJ-GROSSER-FISCH" and water:
                y = WATER_TOP - h * .12
            else:
                y = FLOOR_Y - h + (8 if t not in ("FIG-SYMBOL-ADLER",) else 0)
            if st.get("big_y") is not None:
                y = st["big_y"]
            bigpos[t] = (x, y, w, h)
            pos[t] = (x + w / 2, y + h / 2)
            out.append(self.r_sym(t, x, y, w, h, flip=t in st.get("flip", [])))
        heads = {}
        for fid, cont in L["inside"].items():
            if cont in bigpos:
                x, y, w, h = bigpos[cont]
                px, py = (st.get("in_pos") or {}).get(fid, (.5, .45))
                cx, cy = x + w * px, y + h * py
                if cont in WINDOW:
                    rx, ry = w * .17, h * .3
                    cid = f"aw-{self.uid}-{self._n}-{len(heads)}"
                    out.append(f'<clipPath id="{cid}"><ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}"/></clipPath>'
                               f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="#2E3E4E" stroke="#9CB4C4" stroke-width="1.6" stroke-dasharray="3 2"/>')
                    sub = []
                    heads[fid] = self.r_inside(fid, cx, cy + ry * .25, w, p, sub)
                    out.append(f'<g clip-path="url(#{cid})">{"".join(sub)}</g>')
                else:
                    heads[fid] = self.r_inside(fid, cx, cy, w, p, out)
                pos[fid] = (heads[fid][0], heads[fid][1] + 6)
        self._floor_done = set()
        behind = set(st.get("behind", []))
        if behind:
            self._draw_floor(L, st, [t for t in L["floor"] if t in behind], out, pos)
        # 4. Personen (stage.on: Figur steht auf einem Ort, z. B. auf dem Berg)
        slots = L["row"]
        self._lift = {}
        onmap = st.get("on") or {}
        for i_, s_ in enumerate(slots):
            o_ = onmap.get(s_["fid"])
            if o_ and o_ in pos:
                ox, oy = pos[o_]
                oh = self.m(o_)[1][1]
                peers = [f for f, oo in onmap.items() if oo == o_]
                k_ = peers.index(s_["fid"])
                if not (st.get("x") or {}).get(s_["fid"]):
                    s_["x"] = ox + (k_ - (len(peers) - 1) / 2) * 22
                self._lift[s_["fid"]] = max(0, FLOOR_Y - (oy - oh * .02))
        for f_ in st.get("on_water") or []:  # geht auf dem Wasser: Figur steht über den Wellen (Blindtest: Jesus stand so tief wie Petrus)
            self._lift[f_] = getattr(self, "water_lift", 16)
        sp_idx = ad_idx = None
        names = [s["fid"] for s in slots]
        for s in L["speech"]:
            if s["from"] in names:
                sp_idx = names.index(s["from"])
                ad_idx = names.index(s["to"]) if s["to"] in names else None
                break
        # Zweite gleiche Figur (stage.twin {FIG: x}, z. B. die zwei Mitgekreuzigten links und rechts von Jesus, Joh 19,18):
        # zuerst gezeichnet (hinter den anderen), Kopf unter «FIG#2» für Blasen und Pfeile
        twins = [(f_, x_) for f_, x_ in (st.get("twin") or {}).items() if f_ in names]
        n_all = len(slots) + len(twins)
        for f_, x_ in twins:
            s2 = dict(slots[names.index(f_)], x=x_)
            hk = f_ + "#2"
            heads[hk] = self.r_person(s2, n_all, -1 if x_ > W / 2 else 1, None, None, p, out)
            pos[hk] = (heads[hk][0], heads[hk][1] + self.head_r() * 1.9)
        for i, s in enumerate(slots):
            look = look_dir(slots, i, sp_idx, ad_idx)
            to_god = any(sp["from"] == s["fid"] and sp["to"] in sky for sp in L["speech"])
            if to_god:
                look = 1 if sky[[sp["to"] for sp in L["speech"] if sp["from"] == s["fid"] and sp["to"] in sky][0]][0] > s["x"] else -1
            if (st.get("pose") or {}).get(s["fid"]) == "away":
                look = -look
            arm = None
            for sp in L["speech"]:
                if sp["from"] == s["fid"] and sp["to"] in names and sp["to"] != s["fid"]:
                    arm = 1 if slots[names.index(sp["to"])]["x"] > s["x"] else -1
            hold = st.get("hold", {}).get(s["fid"])
            if to_god and hold is None:
                hold = "PRAY"
            n0 = len(out)
            heads[s["fid"]] = self.r_person(s, n_all, look, arm, hold, p, out)
            lift = self._lift.get(s["fid"], 0)
            if lift:
                out[n0:] = [f'<g transform="translate(0 {-lift:.1f})">{"".join(out[n0:])}</g>']
                heads[s["fid"]] = (heads[s["fid"]][0], heads[s["fid"]][1] - lift)
                if s["fid"] in (st.get("on_water") or []):
                    wx, wy = s["x"], getattr(self, "water_feet", FLOOR_Y) - lift + 3
                    out.append(f'<path d="M{wx - 22:.1f} {wy:.1f}q5.5 -4 11 0t11 0t11 0t11 0" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"/>'
                               f'<path d="M{wx - 22:.1f} {wy:.1f}q5.5 -4 11 0t11 0t11 0t11 0" fill="none" stroke="#3E7CA6" stroke-width="1" stroke-linecap="round"/>')
            pos[s["fid"]] = (heads[s["fid"]][0], heads[s["fid"]][1] + self.head_r() * 1.9)  # Körper, nicht Gesicht
            if hold and hold != "PRAY" and hold not in pos:  # gehaltener Gegenstand: Anfang oder Ziel einer Handlungslinie
                side_ = arm or 1
                pos[hold] = (heads[s["fid"]][0] + side_ * self.head_r() * 1.3, heads[s["fid"]][1] + self.head_r() * 1.6)
        # 5. Gegenstände am Boden: eigener Platz am Rand
        cnt = st.get("count", {})
        self._draw_floor(L, st, [t for t in L["floor"] if t not in behind], out, pos)
        for t in L["hand"]:
            if slots:
                s = slots[0]
                w, h = self.m(t)[1]
                hx, hy = heads[s["fid"]]
                out.append(self.r_sym(t, s["x"] + 6, hy + 30, w, h))
        # 6a. Trennlinie ohne Bedeutung (stage.trenner): trennt zwei Ebenen oder Orte im selben Feld, z. B. Erzähler und
        # Gleichnis (Prüfung 2026-10-26: dafür stand sonst das Zeichen «Abstand», dessen Legende etwas anderes sagt)
        if st.get("trenner"):
            k = st.get("split", max(1, len(slots) - 1))
            if 0 < k < len(slots):
                x = (slots[k - 1]["x"] + slots[k]["x"]) / 2
                out.append(f'<path class="trenner" d="M{x:.1f} 44V{FLOOR_Y + 6:.1f}" stroke="#8A7A5A" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round"/>')
        # 6. Linie (Abstand)
        for t in L["lines"]:
            k = st.get("split", max(1, len(slots) - 1))
            if 0 < k < len(slots):
                x = (slots[k - 1]["x"] + slots[k]["x"]) / 2 - 4
                out.append(self.r_sym(t, x, 50, 8, 64))
        # 7. Zeichen bei den Köpfen (Herz, Gebet …)
        for t in L["head"]:
            who = (st.get("signs_who") or {}).get(t)
            if who is None:
                who = [s["fid"] for s in slots if s["fid"] not in ("FIG-JESUS",)] + [f for f in L["inside"]]
            for f in who:
                if f in heads and not self.r_head_sign_native(t):
                    hx, hy = heads[f]
                    w, h = self.m(t)[1]
                    if t == "FIG-ZEICHEN-TRAUER":
                        out.append(self.r_sym(t, hx + 7, hy - 2, w, h))
                    elif f in spk:  # nicht auf die Spitze der Sprechblase
                        out.append(self.r_sym(t, hx + self.head_r() + 3 if hx < W - 40 else hx - self.head_r() - w - 3, hy - self.head_r() - h * .5, w, h))
                    else:
                        out.append(self.r_sym(t, hx - w / 2, hy - self.head_r() - h - 3, w, h))
        # 8. Zeichen bei bestimmten Figuren: über dem Kopf
        at_pairs = [(t, f) for t, fs in (st.get("at") or {}).items() for f in (fs if isinstance(fs, list) else [fs])]
        for t, f in at_pairs:  # at: {ZEICHEN: FIG} oder {ZEICHEN: [FIG, …]}
            w, h = self.m(t)[1]
            if f in heads and t in HEADWEAR:  # Kopfbedeckung auf den Kopf, nicht darüber (Blindtest: Dornenkranz schwebte)
                hx, hy = heads[f]
                k = self.head_r() * 2.3 / w
                w2, h2 = w * k, h * k
                out.append(self.r_sym(t, hx - w2 / 2, hy - self.head_r() * 1.02 - h2 * .55, w2, h2))
                pos.setdefault(t, (hx, hy - self.head_r()))
            elif f in heads:
                hx, hy = heads[f]
                if f in spk and f not in L["inside"]:
                    ax_ = hx + self.head_r() + 3 if hx < W - 40 else hx - self.head_r() - w - 3
                    out.append(self.r_sym(t, ax_, hy - self.head_r() - h * .4, w, h))
                    pos.setdefault(t, (ax_ + w / 2, hy - self.head_r() - h * .4 + h / 2))  # auch Ziel einer Handlungslinie
                elif f in L["inside"] and not st.get("at_top"):
                    out.append(self.r_sym(t, hx - w - 14 if hx > W / 2 else hx + 14, hy - h / 2 - 2, w, h))
                else:
                    out.append(self.r_sym(t, min(W - w - 4, max(26, hx - w / 2)), max(4, hy - self.head_r() - h - 3), w, h))
                    pos.setdefault(t, (min(W - w - 4, max(26, hx - w / 2)) + w / 2, max(4, hy - self.head_r() - h - 3) + h / 2))
            elif f in sky:
                x, y, w0, h0 = sky[f]
                out.append(self.r_sym(t, x + w0 + 2 if x < W / 2 else x - w - 2, y + h0 - h, w, h))
            elif f in pos:
                x, y = pos[f]
                if f in L["back"] or f in bigpos:  # über dem Ort bzw. Gegenstand, nicht auf seiner Mitte
                    y = y - self.m(f)[1][1] * .5 + 2
                out.append(self.r_sym(t, x - w / 2, max(2, y - h - 4), w, h))
                pos[t] = (x, max(2, y - h - 4) + h / 2)
        for t, f in (st.get("beside") or {}).items():
            w, h = self.m(t)[1]
            if f in heads:
                hx, hy = heads[f]
                r_ = self.head_r()
                ry = hy - h / 2
                # Seite mit freiem Platz wählen: nicht auf ein Nachbargesicht und nicht über den Rand (Blindtest-Rückmeldungen)
                cands = [hx + r_ + 4, hx - r_ - w - 4] if hx < W / 2 else [hx - r_ - w - 4, hx + r_ + 4]
                free = lambda cx: 2 <= cx <= W - w - 2 and not any(  # noqa: E731
                    o != f and abs(ox - (cx + w / 2)) < r_ + w / 2 + 1 and abs(oy - hy) < r_ * 2.2 for o, (ox, oy) in heads.items())
                ok = [c for c in cands if free(c)]
                if ok:
                    rx = ok[0]
                else:  # kein Platz daneben: über den Kopf
                    rx, ry = min(W - w - 2, max(2, hx - w / 2)), max(2, hy - r_ - h - 4)
                out.append(self.r_sym(t, rx, ry, w, h))
                pos.setdefault(t, (rx + w / 2, ry + h / 2))  # auch Ziel einer Handlungslinie
        # 9. Handlungslinien
        people = {sl["fid"] for sl in slots}
        r = self.head_r()

        def anchor(f, ox, oy, both):
            """Ansatzpunkt einer Handlungslinie an einer Person: über dem Kopf oder auf Schulterhöhe, nie durchs Gesicht."""
            hx, hy = heads[f]
            dx = 1 if ox > hx else -1
            if both or oy < hy - r:
                return hx + dx * r * .9, hy - r * 1.5
            return hx + dx * r * 1.7, hy + r * 1.1

        def arrows(only_air):
          for a in st.get("arrows", []):
            f, t, kind = a[0], a[1], (a[2] if len(a) > 2 else "act")
            if ((f in L["air"] or t in L["air"]) != only_air):
                continue
            if f in pos and t in pos:
                (x1, y1), (x2, y2) = pos[f], pos[t]
                both = f in people and t in people
                if t in L["back"] and t in pos:  # Ort mit Menschen (Gemeinde, Stadt): Pfeil endet oben am Ort, nicht im Gesicht
                    bx_, by_ = pos[t]
                    y2 = by_ - self.m(t)[1][1] * .3
                lo, hi = sorted((x1, x2))
                between = any(lo + 2 < heads[o][0] < hi - 2 for o in people if o not in (f, t))
                if f in people:
                    x1, y1 = anchor(f, x2, y2, both or between)
                if t in people:
                    x2, y2 = anchor(t, x1, y1, both or between)
                if f == "FIG-OBJ-GROSSER-FISCH" and f in bigpos:  # Speien/Werfen beginnt am Maul
                    bx_, by_, bw_, bh_ = bigpos[f]
                    x1 = bx_ + bw_ * (.94 if f in st.get("flip", []) else .06)
                    y1 = by_ + bh_ * .45
                d = math.hypot(x2 - x1, y2 - y1) or 1
                sh1 = 0 if (f in people or f == "FIG-OBJ-GROSSER-FISCH") else (min(sky[f][2], sky[f][3]) * .4 if f in sky else 12)
                sh2 = 0 if t in people else (14 if t in bigpos or t in pos else 10)
                ax1, ay1 = x1 + (x2 - x1) * sh1 / d, y1 + (y2 - y1) * sh1 / d
                ax2, ay2 = x2 - (x2 - x1) * sh2 / d, y2 - (y2 - y1) * sh2 / d
                cx1, cy1, cx2, cy2, bul = self.clear_bulge(ax1, ay1, ax2, ay2, kind, f, t, heads, pos, placed_now)
                out.append(arrow_svg(cx1, cy1, cx2, cy2, kind, f in sky or t in sky, bul))
        self._rec = False
        # 10. Sprechblasen (Neufassung 2026-10-26, Hinweise Andi Neck): jede Sprech-Angabe des Bildauftrags wird eine eigene Blase
        # (früher wurden Folgeblasen derselben Figur in eine Blase gefasst, das Wort der zweiten fiel weg). Die Lage wird gesucht,
        # nicht geschoben: feste Regeln (keine Blase über Gesicht, Zeichen, Gegenstand, Kreuzestafel oder anderer Blase; Spitze
        # kurz und steil, nicht hinter einer Blase und nicht über Gesichter oder Zeichen), dann die kürzeste Spitze nahe beim
        # Sprecher; nötigenfalls kleiner, nebeneinander statt übereinander. Eine zweite Blase derselben Figur hängt an der ersten.
        placed, drawn = self.place_bubbles(L, st, heads, sky, pos, p)
        placed_now = [(px, pb - ph, pw, ph) for px, pw, pb, ph in placed]
        arrows(False)  # nach der Lage der Blasen berechnet (weichen ihnen aus), aber unter ihnen gezeichnet
        if L["speech"]:  # Prüfung: Zahl der Sprech-Angaben im Feld (pruefe_bilder.py vergleicht mit data-speech der Blasen)
            out.append(f'<g class="ill-sp" data-n="{len(L["speech"])}"/>')
        for d_ in drawn:
            at_ = f' data-speech="{d_[8]}"' + (' data-link="1"' if len(d_) > 9 else "")
            if d_[7]:
                out.append(think_bubble(*d_[:7], at_))
            else:
                out.append(self.r_bubble(*d_[:7], at_))
        # 11. freie Zeichen oben (unter den Blasen)
        top = max([b[2] for b in placed] + [6]) + 4
        free = list(L["air"])
        if free:
            tot = sum((self.m(t)[1][0] + 3) * min(int(cnt.get(t, 1)), 6) for t in free) + 6 * (len(free) - 1)
            x = st.get("air_x", max(28, (W - tot) / 2))
            y = st.get("air_y", top if top < 60 else 10)
            if "air_y" not in st and top >= 60 and placed:
                # tiefe Blasen: Zeichen neben die Blasen (Blindtest: Zeichen standen in einer Sprechblase)
                right = max(px + pw for px, pw, pb, ph in placed) + 6
                left = min(px for px, pw, pb, ph in placed) - 6
                if W - 6 - right >= tot * .6:
                    x = st.get("air_x", right)
                elif left - 28 >= tot * .6:
                    x = st.get("air_x", 28)
                else:
                    y = min(top, 70)
            k = min(1.0, (W - 6 - x) / tot) if tot else 1
            if y == 10 and "air_x" not in st and placed and x < min(px for px, pw, pb, ph in placed):
                k = min(k, (min(px for px, pw, pb, ph in placed) - 6 - x) / tot)
            hmax = max(self.m(t)[1][1] * k for t in free)
            over = lambda yy: any(x < px + pw and x + tot * k > px and yy < pb and yy + hmax > pb - ph for px, pw, pb, ph in placed)  # noqa: E731
            over2 = lambda xx, yy: any(xx < px + pw and xx + tot * k > px and yy < pb and yy + hmax > pb - ph for px, pw, pb, ph in placed)  # noqa: E731
            if over(y):  # freie Zeichen nie über oder in eine Sprechblase (Hinweis Andi Neck: Krone über der Blase)
                y2 = max(pb for px, pw, pb, ph in placed) + 3
                if y2 + hmax < FLOOR_Y - 30:
                    y = y2
                else:
                    right = max(px + pw for px, pw, pb, ph in placed) + 4
                    if right + tot * k <= W - 4:
                        x = right
            # Spitzen der Blasen laufen nicht über freie Zeichen (Prüfung 2026-10-26: Spitze über den Wolken der Finsternis)
            tails = [(self._tail(d_[0], d_[1], d_[2], d_[3], d_[4], d_[5])[:2], d_[4:6]) for d_ in drawn if len(d_) < 10 and not d_[7]]

            def row(x0, y0):
                bx_, out_ = x0, []
                for t in free:
                    w, h = self.m(t)[1]
                    for q in range(min(int(cnt.get(t, 1)), 6)):
                        out_.append((bx_, y0, w * k, h * k))
                        bx_ += w * k + 3 * k
                    bx_ += 6 * k
                return out_

            def tail_hit(x0, y0):
                return any(self._seg_hits(a_[0], a_[1], b_[0], b_[1], r_, min(r_[2], r_[3]) * .1) for (a_, b_) in tails for r_ in row(x0, y0))
            if tails and tail_hit(x, y):
                bot = max(pb for px, pw, pb, ph in placed) + 3
                alts = [(x2, y2) for y2 in (y, 10, top, bot, 70) for x2 in (x, 28, W - 6 - tot * k, max(px + pw for px, pw, pb, ph in placed) + 4)
                        if 4 <= x2 and x2 + tot * k <= W - 4 and 3 <= y2 and y2 + hmax <= FLOOR_Y - 10 and not over2(x2, y2)]
                ok_ = [a_ for a_ in alts if not tail_hit(*a_)]
                if ok_:
                    x, y = ok_[0]
            for t in free:
                w, h = self.m(t)[1]
                w, h = w * k, h * k
                pos[t] = (x + w / 2, y + h / 2)
                for q in range(min(int(cnt.get(t, 1)), 6)):
                    out.append(self.r_sym(t, x, y, w, h))
                    x += w + 3 * k
                x += 6 * k
        placed_now = [(px, pb - ph, pw, ph) for px, pw, pb, ph in placed]
        arrows(True)  # Handlungslinien zu freien Zeichen erst, wenn deren Lage feststeht
        # 12. Worte im Bild: Namensschilder (erstes Auftreten) und Stichwortband
        for fid, v in (p.get("names") or {}).items():
            if fid in heads:
                hx, hy = heads[fid]
                out.append(name_tag(hx, H - 7, v))  # am unteren Rand: verdeckt weder Gesicht noch das Zeichen auf der Brust
        # Stichwortband unter dem Feld (nicht im Bild: es verdeckte Hände, Gegenstände und Kniende; Pilot 2026-10-23)
        self.bands = getattr(self, "bands", [])
        self.bands.append(word_band(p["keywords"], letter=bool(p.get("letter")), comp=self, cands=panel_icons(p)) if p.get("keywords") else "")
        return "".join(out)



def gather_lex():
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (D / "illustrations/lexicon").glob("FIG-*.json")}


def tilt(x, y, ang):
    return f' transform="rotate({ang} {x:.1f} {y:.1f})"'


__all__ = ["ltext", "word_band", "name_tag", "load_briefs", "alt_text", "Composer", "META", "plan", "gather_lex", "W", "H", "FLOOR_Y", "math", "tilt"]
