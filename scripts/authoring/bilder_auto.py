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
import math
import pathlib

from _lib import D

# ------------------------------------------------------------------ Auftragsdaten
DATA = pathlib.Path(__file__).resolve().parent / "bildauftraege_daten"


def load_briefs():
    """Bildaufträge aus bildauftraege_daten/*.json (eine Datei je Buch), in Dateireihenfolge."""
    out = []
    for f in sorted(DATA.glob("*.json")):
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


def lwrap(v, fs, maxw):
    """Zeilen je Sprache, Breite der breitesten Zeile und grösste Zeilenzahl."""
    lines = {k: split2(s, fs, maxw) for k, s in _lab(v).items()}
    return lines, max(text_w(x, fs) for ls in lines.values() for x in ls), max(len(ls) for ls in lines.values())


def ltext_ml(x, yc, v, fs, maxw, weight="700", fill="#3B3226"):
    """Text um die Mitte yc, bei Bedarf auf zwei Zeilen umbrochen (je Sprache)."""
    lines, _, _ = lwrap(v, fs, maxw)
    lh = fs * 1.15
    out = []
    same = len({tuple(ls) for ls in lines.values()}) == 1
    for k, ls in (list(lines.items())[:1] if same else lines.items()):
        y0 = yc - len(ls) * lh / 2 + fs * .8
        cls = "" if same else f' class="lw lw-{k}"'
        spans = "".join(f'<tspan x="{x:.1f}" y="{y0 + i * lh:.1f}">{_esc(s)}</tspan>' for i, s in enumerate(ls))
        out.append(f'<text{cls} text-anchor="middle" font-family="sans-serif" font-size="{fs}" font-weight="{weight}" fill="{fill}">{spans}</text>')
    return "".join(out)


def word_band(v, letter=False):
    """Stichwortband unter dem Feld: wenige Wörter aus dem Wortlaut; lieber zwei Zeilen als kleine Schrift (Hinweis Andi Neck).
    Ergebnis: (SVG, Höhe)."""
    extra = 16 + (14 if letter else 0)
    maxw = W - 12 - extra
    fs = 10
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
    return (f'<g class="ill-words"><rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="3" fill="#FFF4D6" stroke="#3B3226" stroke-width="1"/>'
            + icon + ltext_ml(tx, y + h / 2, v, fs, maxw) + "</g>", h)


def name_tag(x, y, v):
    """Namensschild beim ersten Auftreten einer Hauptfigur (unter dem Kinn, auf der Brust)."""
    fs = 7.5
    w = lwidth(v, fs) + 8
    x = min(W - 3 - w / 2, max(3 + w / 2, x))
    return (f'<g class="ill-name"><rect x="{x - w / 2:.1f}" y="{y - 7.5:.1f}" width="{w:.1f}" height="10" rx="5" fill="#FFFDF6" stroke="#3B3226" stroke-width=".7"/>'
            + ltext(x, y, v, fs) + "</g>")


def think_bubble(x, y, w, h, tx, ty, inner):
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
    core = f'<rect x="{x + r * .55:.1f}" y="{y + r * .55:.1f}" width="{w - r * 1.1:.1f}" height="{h - r * 1.1:.1f}" fill="#FFFFFF"/>'
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

    def m(self, t):
        if t.startswith("_"):
            return ("band", (186, 70))
        return meta(t, self.lex, self.extra)

    def panel(self, p):
        if p.get("diagram"):  # Strukturbild (bilder_diagramm.py): Kachel nach Inhalt, Stichwortband wie bei Szenen
            import bilder_diagramm
            body, w, h = bilder_diagramm.diagram(self, p["diagram"])
            self.sizes = getattr(self, "sizes", []) + [(w, h)]
            # breite Kachel: zusätzlich eine schmale Fassung fürs Handy (gleicher Inhalt, weniger Spalten)
            alt = None
            if p["diagram"].get("span") == 2:
                dn = dict(p["diagram"], span=1)
                if dn.get("cols"):
                    dn["cols"] = min(2, dn["cols"])
                alt = bilder_diagramm.diagram(self, dn)
            self.alts = getattr(self, "alts", []) + [alt]
            self.bands = getattr(self, "bands", [])
            self.bands.append(word_band(p["keywords"], letter=bool(p.get("letter"))) if p.get("keywords") else "")
            return body
        self.sizes = getattr(self, "sizes", []) + [(W, H)]
        self.alts = getattr(self, "alts", []) + [None]
        self._n += 1
        self._zx = None
        L = plan(p, self.lex, self.extra)
        st = L["st"]
        out = []
        self.ess = []  # wesentliche Teile (Zeichen, Gegenstände, Köpfe): Sprechblasen und Pfeile verdecken sie nicht
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
            heads[s["fid"]] = self.r_person(s, len(slots), look, arm, hold, p, out)
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
        # 10. Sprechblasen
        bubbles = []
        # Blindtest Matthäus: Folgeblasen derselben Figur wurden als «Blase an Blase» gelesen. Darum alles, was eine Figur sagt,
        # in eine Blase (Teile durch einen feinen Strich getrennt); so bleibt auch Platz für einen zweiten Sprecher.
        merged = []
        for sp in L["speech"]:
            prev = next((m for m in merged if m["from"] == sp["from"] and bool(m.get("think")) == bool(sp.get("think"))), None)
            if prev is not None:
                prev["icons"] = list(prev["icons"]) + ["|"] + list(sp["icons"])
            else:
                merged.append(dict(sp))
        for sp in merged[:2]:
            if sp["from"] in heads:
                tx, ty = heads[sp["from"]]
                ty -= self.head_r()
            elif sp["from"] in sky:
                x, y, w0, h0 = sky[sp["from"]]
                tx, ty = (x + w0, y + h0 / 2) if x < W / 2 else (x, y + h0 / 2)
            elif sp["from"] in pos:  # sprechendes Bauteil (z. B. Satan als Schatten): Spitze an den oberen Rand
                tx, ty = pos[sp["from"]]
                ty -= self.m(sp["from"])[1][1] * .4
            else:
                continue
            bubbles.append((sp, tx, ty))
        placed, drawn = [], []
        for k, (sp, tx, ty) in enumerate(bubbles):
            ih = self.icon_h()
            if sp.get("word") and "§W" not in sp["icons"]:  # Kernwort in der Sprechblase, vor höchstens zwei Zeichen
                sp["icons"] = ["§W"] + list(sp["icons"])
            WMAX = 104  # breiter: zweizeilig statt kleiner (Hinweis Andi Neck 2026-10-23)
            ws = [4.0 if i == "|" else (lwrap(sp["word"], 10, WMAX)[1] if i == "§W" else icon_w(self.vb(i), ih)) for i in sp["icons"]]
            bw = sum(ws) + 5 * (len(ws) - 1) + 12
            avail = W - 32
            god = sp["from"] in sky
            if god:
                gx, gy, gw, gh = sky[sp["from"]]
                avail = max(W - (gx + gw + 8) - 4, gx - 12)
            if bw > avail:
                sc = (avail - 12 - 5 * (len(ws) - 1)) / sum(ws)
                ws = [w * sc for w in ws]
                ih *= sc
                bw = avail
            bh = ih + 12
            by = st.get("bubble_y", 6)
            if god:
                gx, gy, gw, gh = sky[sp["from"]]
                bx = gx + gw + 8 if gx + gw + 8 + bw <= W - 4 else gx - bw - 8
                by = 6
            else:
                bx = tx - bw / 2
            bx = max(28 if by < 24 else 4, min(W - 4 - bw, bx))
            boxes = [b for k2, b in sky.items() if k2 != sp["from"]] + [(px, pyb - ph, pw, ph) for px, pw, pyb, ph in placed]
            hit = lambda x_, y_: any(x_ < gx + gw + 4 and x_ + bw > gx - 4 and y_ < gy + gh + 2 and y_ + bh > gy - 2 for gx, gy, gw, gh in boxes)  # noqa: E731
            if not god and "bubble_y" not in st and len(bubbles) == 1:  # nur bei einer Blase (zwei Sprecher brauchen den Platz oben)
                # Blase tiefer, nahe über dem Sprecher, wenn dort kein anderes Gesicht ist (kürzere Spitze; Hinweis Andi Neck)
                faces = [(hx - 15, hy - 16, 30, 32) for o_, (hx, hy) in heads.items() if o_ != sp["from"]]
                low = ty - bh - 22
                if low > by and not hit(bx, low) and not any(bx < fx + fw and bx + bw > fx and low < fy + fh and low + bh > fy for fx, fy, fw, fh in faces):
                    by = low
            if hit(bx, by) and not god:
                # Blase nahe beim Sprecher halten (Hinweis Andi Neck: lange schräge Spitzen quer durchs Bild); auch unter eine
                # Gottes-Darstellung ausweichen statt ans andere Ende des Felds
                xs = [tx - bw / 2, tx - bw + 18, tx - 18, 28, W - 4 - bw] + [gx - bw - 6 for gx, gy, gw, gh in boxes] + [gx + gw + 6 for gx, gy, gw, gh in boxes]
                ys = [by] + [gy + gh + 4 for gx, gy, gw, gh in boxes]
                cands = [(abs(cx + bw / 2 - tx) + (cy - by) * .4, cx, cy) for cx in xs for cy in ys
                         if (28 if cy < 24 else 4) <= cx <= W - 4 - bw and cy + bh <= ty - 6 and not hit(cx, cy)]
                if cands:
                    _, bx, by = min(cands)
            if hit(bx, by):
                done = False
                for cand in (bx, 28, W - 4 - bw) + tuple(gx - bw - 6 for gx, gy, gw, gh in boxes) + tuple(gx + gw + 6 for gx, gy, gw, gh in boxes):
                    if 4 <= cand <= W - 4 - bw and not hit(cand, by):
                        bx, done = cand, True
                        break
                if not done and placed:
                    by = max(b[2] for b in placed) + 4
                    done = not hit(bx, by)
                if not done and boxes:
                    gx, gy, gw, gh = boxes[0]
                    room = max(gx - 32, W - (gx + gw) - 10)
                    sc = max(.5, (room - 12 - 5 * (len(ws) - 1)) / sum(ws))
                    ws = [w * sc for w in ws]
                    ih *= sc
                    bw = sum(ws) + 5 * (len(ws) - 1) + 12
                    bh = ih + 12
                    bx = 28 if gx - 32 >= W - (gx + gw) - 10 else gx + gw + 6
            if not god and self.covers(bx, by, bw, bh, sp["from"], heads):
                # Sprechblase verdeckt nichts Wesentliches (Zeichen, Gegenstand, Gesicht; Hinweis Andi Neck 2026-10-24): andere
                # Lage nahe beim Sprecher suchen, sonst etwas kleiner
                for sc in (1, .88, .76):
                    bw2, bh2 = (bw - 12) * sc + 12, (bh - 12) * sc + 12
                    xs = [tx - bw2 / 2, tx - bw2 + 18, tx - 18, 28, W - 4 - bw2] + [ex - bw2 - 4 for ex, ey, ew, eh in self.ess] + [ex + ew + 4 for ex, ey, ew, eh in self.ess]
                    ys = sorted({by, 6, 4} | {ey - bh2 - 3 for ex, ey, ew, eh in self.ess})
                    cands = [(abs(cx + bw2 / 2 - tx) + abs(cy - by) * .3, cx, cy) for cx in xs for cy in ys
                             if (28 if cy < 24 else 4) <= cx <= W - 4 - bw2 and 2 <= cy and cy + bh2 <= ty - 6
                             and not hit(cx, cy) and not self.covers(cx, cy, bw2, bh2, sp["from"], heads)]
                    if cands:
                        _, bx, by = min(cands)
                        if sc < 1:
                            ws = [w * sc for w in ws]
                            ih *= sc
                            bw, bh = bw2, bh2
                        break
            same = [j for j, (sp0, _, _) in enumerate(bubbles[:len(placed)]) if sp0["from"] == sp["from"]]
            link = None
            if same:
                # zweite Blase derselben Figur: neben die erste, sonst darunter und mit ihr verbunden (keine Spitze durch die Blase)
                px, pw, pbot, ph = placed[same[0]]
                ptop = pbot - ph
                lo_x = 28 if ptop < 24 else 4  # Feldnummer oben links frei lassen
                besides = [c for c in (px + pw + 5,) if lo_x <= c <= W - 4 - bw]  # nur rechts daneben (Leserichtung)
                besides = [c for c in besides if not any(c < gx + gw + 4 and c + bw > gx - 4 and ptop < gy + gh + 2 and ptop + bh > gy - 2
                                                         for gx, gy, gw, gh in list(sky.values()))]
                if not besides:  # zu breit: Zeichen etwas verkleinern, damit die Blase neben die erste passt (statt den Kopf zu verdecken)
                    room = W - 4 - (px + pw + 5)
                    if room >= bw * .72:
                        sc = (room - 12 - 5 * (len(ws) - 1)) / sum(ws)
                        ws = [w * sc for w in ws]
                        ih *= sc
                        bw = sum(ws) + 5 * (len(ws) - 1) + 12
                        bh = ih + 12
                        cand = px + pw + 5
                        if not any(cand < gx + gw + 4 and cand + bw > gx - 4 and ptop < gy + gh + 2 and ptop + bh > gy - 2 for gx, gy, gw, gh in sky.values()):
                            besides = [cand]
                if besides:
                    bx, by = besides[0], ptop + (ph - bh) / 2
                    # verbundene Blase: kurze Spitze zur ersten Blase statt zweiter Spitze quer zum Sprecher
                    tx, ty = (px + pw - 3, ptop + ph / 2) if bx > px else (px + 3, ptop + ph / 2)
                else:
                    by = pbot + 5
                    room_h = ty - 6 - by
                    if bh > room_h and not god:
                        sc = max(.55, (room_h - 12) / ih)
                        ws = [w * sc for w in ws]
                        ih *= sc
                        bw = sum(ws) + 5 * (len(ws) - 1) + 12
                        bh = ih + 12
                    bx = max(28 if by < 24 else 4, min(W - 4 - bw, px))
                    link = same[0]
            if not god and not same and ty - (by + bh) < 6:
                nb = max(2, ty - bh - 8)
                if not hit(bx, nb):
                    by = nb
                else:  # nicht wieder in eine andere Blase schieben: seitlich ausweichen, sonst kleiner
                    alt = [c for c in (28, W - 4 - bw) + tuple(px - bw - 6 for px, pw, pb, ph in placed) + tuple(px + pw + 6 for px, pw, pb, ph in placed)
                           if 4 <= c <= W - 4 - bw and not hit(c, nb)]
                    if alt:
                        bx, by = min(alt, key=lambda c: abs(c + bw / 2 - tx)), nb
                    else:
                        sc = max(.6, (ty - 8 - by - 12) / ih) if ty - 8 - by - 12 > 0 else .6
                        ws = [w * sc for w in ws]
                        ih *= sc
                        bw = sum(ws) + 5 * (len(ws) - 1) + 12
                        bh = ih + 12
            inner, x = [], bx + 6
            for i, w in zip(sp["icons"], ws):
                if i == "|":
                    inner.append(f'<line x1="{x + w / 2:.1f}" y1="{by + 8:.1f}" x2="{x + w / 2:.1f}" y2="{by + 4 + ih:.1f}" stroke="#3B3226" stroke-width=".7" stroke-dasharray="2 2"/>')
                elif i == "§W":
                    fs_ = min(10, 10 * w / max(1, lwrap(sp["word"], 10, WMAX)[1]))
                    inner.append(ltext_ml(x + w / 2, by + 6 + ih / 2, sp["word"], fs_, WMAX * fs_ / 10))
                else:
                    inner.append(self.r_icon(i, x, by + 6, w, ih))
                x += w + 5
            if link is not None:  # obere Blase zeigt auf die untere (verbundene Blasen)
                lb = drawn[link]
                drawn[link] = (lb[0], lb[1], lb[2], lb[3], bx + bw / 2, by + 3, lb[6], lb[7])
            drawn.append((bx, by, bw, bh, tx, ty, "".join(inner), bool(sp.get("think"))))
            placed.append((bx, bw, by + bh, bh))
        placed_now = [(px, pb - ph, pw, ph) for px, pw, pb, ph in placed]
        arrows(False)  # nach der Lage der Blasen berechnet (weichen ihnen aus), aber unter ihnen gezeichnet
        for d_ in drawn:
            if d_[7]:
                out.append(think_bubble(*d_[:7]))
            else:
                out.append(self.r_bubble(*d_[:7]))
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
            if over(y):  # freie Zeichen nie über oder in eine Sprechblase (Hinweis Andi Neck: Krone über der Blase)
                y2 = max(pb for px, pw, pb, ph in placed) + 3
                if y2 + hmax < FLOOR_Y - 30:
                    y = y2
                else:
                    right = max(px + pw for px, pw, pb, ph in placed) + 4
                    if right + tot * k <= W - 4:
                        x = right
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
        self.bands.append(word_band(p["keywords"], letter=bool(p.get("letter"))) if p.get("keywords") else "")
        return "".join(out)



def gather_lex():
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (D / "illustrations/lexicon").glob("FIG-*.json")}


def tilt(x, y, ang):
    return f' transform="rotate({ang} {x:.1f} {y:.1f})"'


__all__ = ["ltext", "word_band", "name_tag", "load_briefs", "alt_text", "Composer", "META", "plan", "gather_lex", "W", "H", "FLOOR_Y", "math", "tilt"]
