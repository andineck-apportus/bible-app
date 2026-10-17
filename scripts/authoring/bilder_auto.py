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
WATER_TOP = 96  # Wellenkamm der Bänder Meer/See


def plan(p, lex, extra):
    """Ordnet die Bestandteile eines Felds an; Ergebnis in Feldeinheiten, von beiden Stilen gezeichnet."""
    st = p.get("stage") or {}
    as_place = [f for f in p["figures"] if f in META and META[f][0] == "back"]  # z. B. Gemeinde (Haus mit Menschen)
    humans = [f for f in p["figures"] if (lex[f]["kind"] in HUMAN_KINDS or f == "FIG-JESUS") and f not in as_place]
    divine = [f for f in p["figures"] if f in ("FIG-GOTT", "FIG-HEILIGER-GEIST")]
    things = as_place + list(p["objects"]) + list(p["signs"])
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


def arrow_svg(x1, y1, x2, y2, kind="act", divine=True):
    """Handlungslinie: act (Gott sendet, sieht, bestimmt), throw (werfen, speien), go (gehen, dem Boden entlang)."""
    mx, my = (x1 + x2) / 2, min(y1, y2) - (26 if kind == "throw" else 14 if kind == "act" else 0)
    if kind == "go":
        my = (y1 + y2) / 2
    ang = math.atan2(y2 - my, x2 - mx)
    hx1, hy1 = x2 - 7 * math.cos(ang - .45), y2 - 7 * math.sin(ang - .45)
    hx2, hy2 = x2 - 7 * math.cos(ang + .45), y2 - 7 * math.sin(ang + .45)
    dash = ' stroke-dasharray="5 4"' if kind == "go" else (' stroke-dasharray="2 4"' if kind == "throw" else "")
    col = "#C08A2A" if kind == "act" and divine else "#3B3226"
    return (f'<path d="M{x1:.1f} {y1:.1f}Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="#FFFDF6" stroke-width="4.4" stroke-linecap="round" opacity=".8"/>'
            f'<path d="M{x1:.1f} {y1:.1f}Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="2"{dash} stroke-linecap="round"/>'
            f'<path d="M{hx1:.1f} {hy1:.1f}L{x2:.1f} {y2:.1f}L{hx2:.1f} {hy2:.1f}" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')


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

    def m(self, t):
        if t.startswith("_"):
            return ("band", (186, 70))
        return meta(t, self.lex, self.extra)

    def panel(self, p):
        self._n += 1
        self._zx = None
        L = plan(p, self.lex, self.extra)
        st = L["st"]
        out = []
        pos = {}  # Mittelpunkte für Handlungslinien
        # 1. Hintergrund
        for t in L["band"]:
            out.append(self.r_band(t))
        if not L["band"]:
            out.append(self.r_floor())
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
        # 4. Personen
        slots = L["row"]
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
            heads[s["fid"]] = self.r_person(s, len(slots), look, arm, hold, p, out)
            pos[s["fid"]] = (heads[s["fid"]][0], heads[s["fid"]][1] + self.head_r() * 1.9)  # Körper, nicht Gesicht
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
            if f in heads:
                hx, hy = heads[f]
                if f in spk and f not in L["inside"]:
                    out.append(self.r_sym(t, hx + self.head_r() + 3 if hx < W - 40 else hx - self.head_r() - w - 3, hy - self.head_r() - h * .4, w, h))
                elif f in L["inside"] and not st.get("at_top"):
                    out.append(self.r_sym(t, hx - w - 14 if hx > W / 2 else hx + 14, hy - h / 2 - 2, w, h))
                else:
                    out.append(self.r_sym(t, min(W - w - 4, max(26, hx - w / 2)), max(4, hy - self.head_r() - h - 3), w, h))
            elif f in sky:
                x, y, w0, h0 = sky[f]
                out.append(self.r_sym(t, x + w0 + 2 if x < W / 2 else x - w - 2, y + h0 - h, w, h))
            elif f in pos:
                x, y = pos[f]
                out.append(self.r_sym(t, x - w / 2, y - h - 4, w, h))
        for t, f in (st.get("beside") or {}).items():
            w, h = self.m(t)[1]
            if f in heads:
                hx, hy = heads[f]
                rx = hx + self.head_r() + 4 if hx < W - 44 else hx - self.head_r() - w - 4
                out.append(self.r_sym(t, rx, hy - h / 2, w, h))
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
                sh1 = 0 if (f in people or f == "FIG-OBJ-GROSSER-FISCH") else (16 if f in sky else 12)
                sh2 = 0 if t in people else (14 if t in bigpos or t in pos else 10)
                out.append(arrow_svg(x1 + (x2 - x1) * sh1 / d, y1 + (y2 - y1) * sh1 / d, x2 - (x2 - x1) * sh2 / d, y2 - (y2 - y1) * sh2 / d, kind, f in sky or t in sky))
        arrows(False)
        # 10. Sprechblasen
        bubbles = []
        for sp in L["speech"][:2]:
            if sp["from"] in heads:
                tx, ty = heads[sp["from"]]
                ty -= self.head_r()
            elif sp["from"] in sky:
                x, y, w0, h0 = sky[sp["from"]]
                tx, ty = (x + w0, y + h0 / 2) if x < W / 2 else (x, y + h0 / 2)
            else:
                continue
            bubbles.append((sp, tx, ty))
        placed, drawn = [], []
        for k, (sp, tx, ty) in enumerate(bubbles):
            ih = self.icon_h()
            ws = [icon_w(self.vb(i), ih) for i in sp["icons"]]
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
            same = [j for j, (sp0, _, _) in enumerate(bubbles[:len(placed)]) if sp0["from"] == sp["from"]]
            link = None
            if same:
                # zweite Blase derselben Figur: neben die erste, sonst darunter und mit ihr verbunden (keine Spitze durch die Blase)
                px, pw, pbot, ph = placed[same[0]]
                ptop = pbot - ph
                lo_x = 28 if ptop < 24 else 4  # Feldnummer oben links frei lassen
                besides = [c for c in (px + pw + 5, px - bw - 5) if lo_x <= c <= W - 4 - bw]
                besides = [c for c in besides if not any(c < gx + gw + 4 and c + bw > gx - 4 and ptop < gy + gh + 2 and ptop + bh > gy - 2
                                                         for gx, gy, gw, gh in list(sky.values()))]
                if not besides:  # zu breit: Zeichen etwas verkleinern, damit die Blase neben die erste passt (statt den Kopf zu verdecken)
                    room = max(W - 4 - (px + pw + 5), px - 5 - lo_x)
                    if room >= bw * .72:
                        sc = (room - 12 - 5 * (len(ws) - 1)) / sum(ws)
                        ws = [w * sc for w in ws]
                        ih *= sc
                        bw = sum(ws) + 5 * (len(ws) - 1) + 12
                        bh = ih + 12
                        cand = px + pw + 5 if W - 4 - (px + pw + 5) >= bw - .5 else px - bw - 5
                        if not any(cand < gx + gw + 4 and cand + bw > gx - 4 and ptop < gy + gh + 2 and ptop + bh > gy - 2 for gx, gy, gw, gh in sky.values()):
                            besides = [cand]
                if besides:
                    bx, by = besides[0], ptop + (ph - bh) / 2
                    # verbundene Blase: kurze Spitze zur ersten Blase statt zweiter Spitze quer zum Sprecher
                    tx, ty = (px + pw - 3, ptop + ph / 2) if bx > px else (px + 3, ptop + ph / 2)
                else:
                    by = pbot + 5
                    bx = max(28 if by < 24 else 4, min(W - 4 - bw, px))
                    link = same[0]
            if not god and not same and ty - (by + bh) < 6:
                by = max(2, ty - bh - 8)
            inner, x = [], bx + 6
            for i, w in zip(sp["icons"], ws):
                inner.append(self.r_icon(i, x, by + 6, w, ih))
                x += w + 5
            if link is not None:  # obere Blase zeigt auf die untere (verbundene Blasen)
                lb = drawn[link]
                drawn[link] = (lb[0], lb[1], lb[2], lb[3], bx + bw / 2, by + 3, lb[6])
            drawn.append((bx, by, bw, bh, tx, ty, "".join(inner)))
            placed.append((bx, bw, by + bh, bh))
        for d_ in drawn:
            out.append(self.r_bubble(*d_))
        # 11. freie Zeichen oben (unter den Blasen)
        top = max([b[2] for b in placed] + [6]) + 4
        free = list(L["air"])
        if free:
            tot = sum((self.m(t)[1][0] + 3) * min(int(cnt.get(t, 1)), 6) for t in free) + 6 * (len(free) - 1)
            x = st.get("air_x", max(28, (W - tot) / 2))
            k = min(1.0, (W - 6 - x) / tot) if tot else 1
            y = st.get("air_y", top if top < 60 else 10)
            for t in free:
                w, h = self.m(t)[1]
                w, h = w * k, h * k
                pos[t] = (x + w / 2, y + h / 2)
                for q in range(min(int(cnt.get(t, 1)), 6)):
                    out.append(self.r_sym(t, x, y, w, h))
                    x += w + 3 * k
                x += 6 * k
        arrows(True)  # Handlungslinien zu freien Zeichen erst, wenn deren Lage feststeht
        return "".join(out)



def gather_lex():
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (D / "illustrations/lexicon").glob("FIG-*.json")}


def tilt(x, y, ang):
    return f' transform="rotate({ang} {x:.1f} {y:.1f})"'


__all__ = ["load_briefs", "alt_text", "Composer", "META", "plan", "gather_lex", "W", "H", "FLOOR_Y", "math", "tilt"]
