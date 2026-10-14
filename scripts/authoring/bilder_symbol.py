#!/usr/bin/env python3
"""Autorenwerkzeug: Bildstil «Symbol» – Darstellungen der Lexikon-Einträge und Bilder zu den Bildaufträgen.

Schichten (docs/BILDSPRACHE.md):
1. Bildlexikon (data/illustrations/lexicon/FIG-*.json, stilunabhängig): wer/was, Pflichtmerkmale.
2. Bildauftrag (data/illustrations/briefs/BRIEF-*.json, stilunabhängig): wer, was, wer zu wem, Reihenfolge.
3. Stil (hier «Symbol»): `renderings` ordnet jedem Lexikon-Eintrag ein Bauteil der SVG-Bibliothek zu
   (data/illustrations/symbol/_bibliothek.svg); die Bilder werden hier aus den Bauteilen zusammengesetzt und als SVG geschrieben.

Die Bildfelder folgen den Feldern des Bildauftrags (Nummer oben links). Personen ohne Gesicht; Gott nie als Mensch.
Jedes Bild ist Deutung (siehe interpretation_note_de im Auftrag). Prüfung auf Verständlichkeit: `check` im Bild-Datensatz.

Aufruf: python3 scripts/authoring/bilder_symbol.py
KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; eigene Zeichnungen (CC0), keine fachliche Prüfung.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, localize, write  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; eigene Zeichnung, keine fachliche Prüfung."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-14; Mundart noch nicht muttersprachlich geprüft."
LIC = "CC0 1.0 (eigene Zeichnung)"
OUT = D / "illustrations/symbol"

# Lexikon-Eintrag -> Bauteil der Bibliothek (nur, was dieser Stil schon zeichnet)
RENDER = {
    "FIG-JESUS": "ill-p-jesus", "FIG-MARIA-MUTTER-JESU": "ill-p-maria", "FIG-ROLLE-JUENGER": "ill-p-juenger",
    "FIG-ROLLE-BRAUT": "ill-p-braut", "FIG-ROLLE-BRAEUTIGAM": "ill-p-braeutigam", "FIG-ROLLE-GAST": "ill-p-gast",
    "FIG-GRUPPE-MENGE": "ill-p-menge", "FIG-ROLLE-DIENER": "ill-p-diener", "FIG-ROLLE-SPEISEMEISTER": "ill-p-meister",
    "FIG-ROLLE-HAENDLER": "ill-p-haendler", "FIG-OBJ-KRUG-WASSER": "ill-jar", "FIG-OBJ-KRUG-WEIN": "ill-jar-wein",
    "FIG-OBJ-KRUG-WEIN-LEER": "ill-jar-leer", "FIG-OBJ-BECHER-LEER": "ill-becher-leer", "FIG-OBJ-BECHER-VOLL": "ill-becher",
    "FIG-ORT-TEMPEL": "ill-tempel", "FIG-OBJ-TAUBE": "ill-taube-kaefig", "FIG-OBJ-PEITSCHE": "ill-peitsche",
    "FIG-OBJ-SCHAF": "ill-schaf", "FIG-OBJ-MUENZEN": "ill-muenzen", "FIG-OBJ-SCHRIFTROLLE": "ill-schriftrolle",
    "FIG-ZEICHEN-STERN": "ill-zeichen", "FIG-ZEICHEN-FEHLT": "ill-z-fehlt", "FIG-ZEICHEN-STUNDE": "ill-z-stunde",
    "FIG-ZEICHEN-HOEREN": "ill-z-hoeren", "FIG-ZEICHEN-GLAUBEN": "ill-z-glauben", "FIG-ZEICHEN-FREUDE": "ill-z-freude",
    "FIG-ZEICHEN-FRAGEN": "ill-z-frage", "FIG-ZEICHEN-BRINGEN": "ill-z-pfeil", "FIG-ZEICHEN-ABSTAND": "ill-z-abstand",
    "FIG-ZEICHEN-HOCHZEIT": "ill-z-hochzeit", "FIG-ZEICHEN-TAGE": "ill-sonne", "FIG-ZEICHEN-NIEDERREISSEN": "ill-tempel-riss",
    "FIG-ZEICHEN-LICHT": "ill-licht", "FIG-SYMBOL-ADLER": "ill-adler",
}
VB = {"ill-p": "0 0 30 64", "ill-jar": "0 0 30 56", "ill-jar-wein": "0 0 30 56", "ill-jar-leer": "0 0 40 56", "ill-becher": "0 0 12 14",
      "ill-becher-leer": "0 0 12 14", "ill-tempel": "0 0 200 150", "ill-tempel-riss": "0 0 200 150", "ill-taube-tier": "0 0 40 26",
      "ill-taube-kaefig": "0 0 40 40", "ill-peitsche": "0 0 22 26", "ill-schaf": "0 0 34 22", "ill-muenzen": "0 0 24 14",
      "ill-schriftrolle": "0 0 44 30", "ill-zeichen": "0 0 20 20", "ill-z-fehlt": "0 0 20 20", "ill-z-stunde": "0 0 16 22",
      "ill-z-hoeren": "0 0 26 22", "ill-z-glauben": "0 0 22 24", "ill-z-freude": "0 0 24 16", "ill-z-frage": "0 0 12 20",
      "ill-z-pfeil": "0 0 20 10", "ill-z-abstand": "0 0 8 60", "ill-z-hochzeit": "0 0 44 18", "ill-jesus-kopf": "0 0 24 24",
      "ill-sonne": "0 0 16 16", "ill-licht": "0 0 40 40", "ill-adler": "0 0 120 84"}

INK, PAPER, FLOOR, BUBBLE = "#3B3226", "#F4E7D3", "#E2CDA8", "#FFFFFF"


def use(sym, x, y, w, h, extra=""):
    return f'<use href="#{sym}" x="{x}" y="{y}" width="{w}" height="{h}"{extra}/>'


def fig(fid, x, y=58, w=28, h=60, extra=""):
    return use(RENDER[fid], x, y, w, h, extra)


def gesture(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>'


def bubble(x, y, w, h, tx, ty, inner):
    """Sprechblase; die Spitze zeigt auf die sprechende Figur (tx, ty)."""
    bx = min(max(tx, x + 10), x + w - 10)
    return (f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{BUBBLE}" stroke="{INK}" stroke-width="1.2"/>'
            f'<path d="M{bx - 5} {y + h}L{tx} {ty}L{bx + 5} {y + h}" fill="{BUBBLE}" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>'
            f'<path d="M{bx - 4} {y + h}h8" stroke="{BUBBLE}" stroke-width="2.4"/>{inner}</g>')


def panel(n, px, py, body, w=186, h=140):
    clip = f"ill-cp-{n}-{px}-{py}"
    return (f'<g transform="translate({px} {py})"><clipPath id="{clip}"><rect width="{w}" height="{h}" rx="10"/></clipPath>'
            f'<g clip-path="url(#{clip})"><rect width="{w}" height="{h}" fill="{PAPER}"/><rect y="{h - 22}" width="{w}" height="22" fill="{FLOOR}"/>{body}</g>'
            f'<circle cx="13" cy="13" r="9" fill="#FFFDF6" stroke="{INK}"/><text x="13" y="17.5" text-anchor="middle" font-family="sans-serif" font-size="12" fill="{INK}">{n}</text></g>')


# ---------- Johannes 2,1–12 (vier Felder) ----------
def hochzeit_tafel():
    seated = (use("ill-p-braut", 112, 36, 16, 34) + use("ill-p-braeutigam", 128, 36, 16, 34) + use("ill-p-gast", 144, 38, 15, 32)
              + use("ill-p-gast2", 159, 38, 15, 32))
    table = f'<rect x="104" y="62" width="76" height="6" fill="#FFFDF6" stroke="{INK}"/><path d="M106 68h72l-3 14h-66z" fill="#F2E6CC" stroke="{INK}"/>'
    return use("ill-z-hochzeit", 110, 20, 66, 22) + seated + table


def kana_1():
    b1 = bubble(24, 12, 64, 32, 40, 64, use("ill-jar-leer", 28, 14, 20, 28) + use("ill-becher-leer", 50, 21, 14, 17) + use("ill-z-fehlt", 66, 20, 16, 16))
    b2 = bubble(98, 88, 30, 28, 90, 76, use("ill-z-stunde", 106, 91, 15, 21))
    return hochzeit_tafel() + fig("FIG-MARIA-MUTTER-JESU", 26, 58) + gesture(48, 88, 58, 84) + fig("FIG-JESUS", 62, 56, 30, 64) + b1 + b2


def kana_2():
    b = bubble(14, 12, 100, 34, 46, 62, use("ill-jesus-kopf", 22, 17, 24, 24) + use("ill-z-pfeil", 50, 24, 20, 10) + use("ill-z-hoeren", 76, 17, 30, 25))
    return (fig("FIG-MARIA-MUTTER-JESU", 34, 58) + gesture(58, 88, 84, 84) + fig("FIG-ROLLE-DIENER", 108, 58)
            + fig("FIG-ROLLE-DIENER", 138, 62, 26, 56, ' opacity=".85"') + b)


def kana_3():
    jars = "".join(use("ill-jar", 50 + i * 16, 90, 15, 28) for i in range(6))
    pour = (f'<g transform="rotate(-75 150 76)">{use("ill-jar", 141, 62, 13, 24)}</g>'
            '<path d="M135 82q-4 3-4 10" fill="none" stroke="#4C9BD6" stroke-width="2.4" stroke-linecap="round"/>')
    b = bubble(10, 10, 86, 34, 26, 58, use("ill-jar", 18, 13, 15, 28) + use("ill-z-pfeil", 38, 22, 20, 10) + use("ill-p-meister", 64, 12, 15, 31))
    return fig("FIG-JESUS", 10, 56, 30, 64) + gesture(36, 88, 48, 96) + jars + fig("FIG-ROLLE-DIENER", 150, 58) + pour + b


def kana_4():
    b = bubble(26, 6, 40, 32, 40, 60, use("ill-becher", 36, 10, 20, 23))
    hearts = use("ill-z-glauben", 147, 46, 16, 18) + use("ill-z-glauben", 167, 46, 16, 18)
    return (fig("FIG-ROLLE-DIENER", 2, 66, 22, 50) + use("ill-jar-wein", 22, 98, 11, 20) + fig("FIG-ROLLE-SPEISEMEISTER", 40, 58)
            + use("ill-becher", 62, 80, 11, 13) + gesture(66, 90, 78, 86) + use("ill-z-freude", 43, 46, 28, 17) + b
            + fig("FIG-ROLLE-BRAEUTIGAM", 80, 58) + use("ill-zeichen", 118, 26, 16, 16) + fig("FIG-JESUS", 112, 56, 28, 62)
            + fig("FIG-ROLLE-JUENGER", 144, 68, 22, 50) + fig("FIG-ROLLE-JUENGER", 164, 68, 22, 50) + hearts)


def kana_kapitel():
    jars = "".join(use("ill-jar", 36 + i * 15, 92, 14, 26) for i in range(3))
    return (use("ill-z-hochzeit", 110, 26, 66, 22) + fig("FIG-ROLLE-BRAUT", 122, 56) + fig("FIG-ROLLE-BRAEUTIGAM", 150, 56)
            + fig("FIG-JESUS", 4, 56, 30, 64) + jars + use("ill-z-pfeil", 82, 100, 14, 8) + use("ill-jar-wein", 98, 88, 16, 30)
            + use("ill-zeichen", 96, 58, 20, 20))


# ---------- Johannes 2,13–22 (zwei Felder) ----------
def tempel_1():
    table = f'<g transform="rotate(-18 40 110)"><rect x="12" y="104" width="56" height="6" fill="#B07A3E" stroke="{INK}"/><path d="M18 104v-12M62 104v-12" stroke="{INK}" stroke-width="2.4"/></g>'
    coins = use("ill-muenzen", 10, 120, 22, 13) + use("ill-muenzen", 40, 124, 20, 12)
    b = bubble(116, 6, 66, 30, 96, 58, use("ill-tempel", 121, 10, 26, 20) + use("ill-muenzen", 148, 15, 16, 10) + use("ill-z-fehlt", 165, 13, 14, 14))
    return (use("ill-tempel", 26, 10, 86, 64) + table + coins + fig("FIG-ROLLE-HAENDLER", 2, 56, 26, 58) + fig("FIG-JESUS", 76, 56, 30, 64)
            + gesture(100, 86, 106, 72) + use("ill-peitsche", 104, 50, 18, 22) + use("ill-schaf", 130, 96, 36, 23)
            + use("ill-taube-kaefig", 152, 52, 28, 28) + b)


def tempel_2():
    crowd = (fig("FIG-GRUPPE-MENGE", 44, 70, 20, 44, ' opacity=".6"') + fig("FIG-GRUPPE-MENGE", 6, 58) + fig("FIG-GRUPPE-MENGE", 30, 64, 24, 52)
             + fig("FIG-GRUPPE-MENGE", 54, 62, 25, 54, ' opacity=".85"'))
    b1 = bubble(4, 8, 52, 32, 22, 58, use("ill-zeichen", 11, 14, 20, 20) + use("ill-z-frage", 36, 13, 12, 22))
    suns = "".join(use("ill-sonne", 120 + i * 10, 20, 9, 9) for i in range(3))
    b2 = bubble(62, 8, 120, 34, 150, 58, use("ill-tempel-riss", 67, 13, 30, 23) + use("ill-z-pfeil", 99, 21, 14, 8) + suns
                + use("ill-z-pfeil", 152, 21, 12, 8) + use("ill-tempel", 165, 15, 15, 12))
    return crowd + fig("FIG-JESUS", 140, 56, 30, 64) + gesture(144, 88, 128, 84) + b1 + b2


def glaube_1():
    crowd = (fig("FIG-GRUPPE-MENGE", 70, 70, 20, 44, ' opacity=".55"') + fig("FIG-GRUPPE-MENGE", 18, 68, 22, 48, ' opacity=".7"')
             + "".join(fig("FIG-GRUPPE-MENGE", x, y, w, h) for x, y, w, h in ((4, 64, 25, 54), (34, 60, 27, 58), (60, 66, 24, 52), (86, 62, 26, 56))))
    stars = use("ill-zeichen", 18, 14, 16, 16) + use("ill-zeichen", 48, 6, 13, 13) + use("ill-zeichen", 76, 16, 15, 15)
    hearts = "".join(use("ill-z-glauben", x, y, 14, 16) for x, y in ((10, 44), (41, 40), (65, 46), (92, 42)))
    return (use("ill-tempel", 120, 16, 60, 45, ' opacity=".45"') + crowd + stars + hearts
            + use("ill-z-abstand", 116, 58, 8, 60) + fig("FIG-JESUS", 140, 56, 30, 64))


def kana_svg():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 288">'
            + panel(1, 0, 0, kana_1()) + panel(2, 194, 0, kana_2()) + panel(3, 0, 148, kana_3()) + panel(4, 194, 148, kana_4()) + "</svg>")


def tempel_svg():
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 140">' + panel(1, 0, 0, tempel_1()) + panel(2, 194, 0, tempel_2()) + "</svg>"


def glaube_svg():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 186 140">' + panel(1, 0, 0, glaube_1()) + "</svg>"


def kapitel_svg():
    s = 124 / 186
    parts = [f'<g transform="translate({i * 128} 0) scale({s:.4f})">' + panel(i + 1, 0, 0, body) + "</g>"
             for i, body in enumerate((kana_kapitel(), tempel_1(), glaube_1()))]
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 94">' + "".join(parts) + "</svg>"


def buch_svg():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 250"><rect width="380" height="250" fill="#1F2A44"/>'
            + use("ill-licht", 156, 6, 68, 68) + use("ill-adler", 84, 56, 212, 148)
            + use("ill-schriftrolle", 150, 202, 80, 40) + "</svg>")


GENERATED = {"ILL-SYM-JHN": buch_svg, "ILL-SYM-JHN-002-001-012": kana_svg, "ILL-SYM-JHN-002-013-022": tempel_svg,
             "ILL-SYM-JHN-002-023-025": glaube_svg, "ILL-SYM-JHN-002": kapitel_svg}

# Bild -> (Bildauftrag, Bildbeschreibung DE, Bildbeschreibung GSW)
ILL = {
    "ILL-SYM-JHN": ("BRIEF-JHN", "Ein brauner Adler mit ausgebreiteten Flügeln und gelbem Hakenschnabel unter einem Licht mit Strahlen, darunter eine Schriftrolle.",
                    "En brune Adler mit uusbreitete Flügel und gälem Hakeschnabel under eme Liecht mit Strahle, drunder e Schriftrolle."),
    "ILL-SYM-JHN-002": ("BRIEF-JHN-002", "Drei Felder: 1 Hochzeit (Girlande, Braut und Bräutigam); Jesus, drei Wasserkrüge, ein Pfeil zu einem Weinkrug, darüber ein Stern (Zeichen). "
                        "2 Jesus treibt die Händler aus dem Tempel. 3 Die Menge glaubt wegen der Zeichen, eine gestrichelte Linie trennt sie von Jesus.",
                        "Drüü Fälder: 1 Hochziit (Girlande, Brut und Brüütigam); de Jesus, drüü Wasserchrüeg, en Pfiil zu eme Wiichrueg, drüber en Stern (Zeiche). "
                        "2 De Jesus tribt d Händler us em Tämpel. 3 D Mängi glaubt wäge de Zeiche, e gstrichleti Linie trännt si vom Jesus."),
    "ILL-SYM-JHN-002-001-012": ("BRIEF-JHN-002-001-012",
                                "Vier Felder: 1 Bei der Hochzeit zeigt Maria Jesus den leeren Weinkrug und den leeren Becher, Jesus antwortet mit der Sanduhr (noch nicht). 2 Maria sagt den Dienern: hört auf Jesus. "
                                "3 Jesus weist auf die sechs Krüge, ein Diener giesst Wasser ein; Sprechblase: Wasserkrug, Pfeil, Speisemeister. 4 Der Speisemeister freut sich, hält den Becher und spricht zum Bräutigam; "
                                "über Jesus ein Stern (Zeichen), über den Jüngern Herzen (sie glauben).",
                                "Vier Fälder: 1 A de Hochziit zeigt d Maria em Jesus de läär Wiichrueg und de läär Becher, de Jesus antwortet mit de Sanduhr (no nöd). 2 D Maria seit de Diener: losed uf de Jesus. "
                                "3 De Jesus zeigt uf di sächs Chrüeg, en Diener schüttet Wasser ii; Sprächblase: Wasserchrueg, Pfiil, Spiismeischter. 4 De Spiismeischter freut sich, hebt de Becher und redt mit em Brüütigam; "
                                "über em Jesus en Stern (Zeiche), über de Jünger Härz (si glaubed)."),
    "ILL-SYM-JHN-002-013-022": ("BRIEF-JHN-002-013-022",
                                "Zwei Felder: 1 Jesus mit erhobener Geissel vor dem Tempel; umgestossener Tisch, Münzen, ein Händler weicht, ein Schaf, Tauben im Käfig; Sprechblase: Tempel, Münzen, durchgestrichen. "
                                "2 Die Menge fragt nach einem Zeichen (Stern, Fragezeichen); Jesus antwortet: Tempel mit Riss, drei Sonnen (drei Tage), Tempel.",
                                "Zwei Fälder: 1 De Jesus mit ufghabener Geissle vor em Tämpel; umgheite Tisch, Münze, en Händler gaat ewäg, es Schaf, Tube im Chäfig; Sprächblase: Tämpel, Münze, durgstriche. "
                                "2 D Mängi fröget nach eme Zeiche (Stern, Fragezeiche); de Jesus antwortet: Tämpel mit Riss, drüü Sunne (drüü Täg), Tämpel."),
    "ILL-SYM-JHN-002-023-025": ("BRIEF-JHN-002-023-025", "Eine Menge unter goldenen Sternen (Zeichen), mit Herzen (sie glauben); eine gestrichelte Linie trennt sie von Jesus; im Hintergrund der Tempel.",
                                "E Mängi under goldige Stärn (Zeiche), mit Härz (si glaubed); e gstrichleti Linie trännt si vom Jesus; im Hindergrund de Tämpel."),
}


def run():
    lex = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (D / "illustrations/lexicon").glob("FIG-*.json")}
    for k in RENDER:
        if k not in lex:
            raise SystemExit(f"{k} nicht im Bildlexikon")
    style = {"id": "ILLSTYLE-SYMBOL", "type": "illustration_style", "status": "draft", "tags": [],
             "key": "symbol", "labels": {"de": "Symbol", "en": "Symbol"},
             "description_de": "Flache, klare Symbolbilder. Personen ohne Gesicht, erkennbar an den Pflichtmerkmalen des Bildlexikons; "
                               "Sprechblasen mit Zeichen statt Wörtern; mehrere Schritte als nummerierte Bildfelder.",
             "library": "data/illustrations/symbol/_bibliothek.svg",
             "renderings": {k: {"symbol": v, "viewbox": VB.get(v, VB["ill-p"] if v.startswith("ill-p-") else "0 0 30 64")} for k, v in sorted(RENDER.items())},
             "license": LIC, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
    n = write(D / "illustrations/styles/ILLSTYLE-SYMBOL.json", style, "Darstellungen neu nach Bildlexikon (renderings statt eigener Figurenliste)")
    for rid, gen in GENERATED.items():
        svg = gen()
        f = OUT / f"{rid}.svg"
        if not f.exists() or f.read_text(encoding="utf-8").strip() != svg:
            f.write_text(svg + "\n", encoding="utf-8")
            n += 1
    for rid, (brief_id, alt, alt_g) in ILL.items():
        brief = json.loads((D / "illustrations/briefs" / f"{brief_id}.json").read_text(encoding="utf-8"))
        depicts = sorted({x for p in brief["panels"] for k in ("figures", "objects", "signs") for x in p[k]}
                         | {x for p in brief["panels"] for sp in p["speech"] for x in (sp["from"], sp["to"], *sp["icons"])})
        missing = [x for x in depicts if x not in RENDER]
        rec = {"id": rid, "type": "illustration", "status": "draft", "tags": ["TAG-JOHN"], "style": "ILLSTYLE-SYMBOL",
               "brief": brief_id, "level": brief["level"], "reference": brief["reference"], "target": brief["target"],
               "file": f"data/illustrations/symbol/{rid}.svg", "depicts": [x for x in depicts if x in RENDER],
               **({"not_rendered": missing} if missing else {}), "alt_de": alt, "license": LIC, "authorship_de": AUTH,
               "knowledge": {"asserted_at": DATE, "supersedes": None}}
        old = OUT / f"{rid}.json"
        if old.exists():
            o = json.loads(old.read_text(encoding="utf-8"))
            if "check" in o:
                rec["check"] = o["check"]
        n += write(old, rec, "Bild nach Bildauftrag neu gezeichnet bzw. neu verknüpft")
        n += localize(rid, rec, {"alt_de": alt_g}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026", AUTH_GSW, DATE)
    print(f"PASS: Bildstil Symbol – {len(RENDER)} Darstellungen, {len(ILL)} Bilder; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
