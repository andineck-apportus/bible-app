#!/usr/bin/env python3
"""Beispielbilder für die Analyse «Visuelle Sprache der Bibel» (2026-11-21).

Strukturbilder sind aus Daten gezeichnet (SVG); gemalte Teile (Aquarell) kommen aus dem Bildlexikon, den geprüften Szenen
oder dem Pilotlauf (pilot/visuell/malen.py). Zitate stammen aus den Arbeitsübersetzungen (data/translations/*-DE-WORKING).
Jede Funktion gibt ein SVG- oder HTML-Stück zurück; seite.py setzt sie zusammen.
"""
import base64
import glob
import html
import io
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / "pilot/visuell"

# Papierfarben (Bildstil, docs/BILDSTIL.md): Figuren stehen immer auf Papier, auch im dunklen Modus der Seite.
PAPER, INK, MUTED, RULE = "#FBF8F2", "#3E413B", "#7A7C73", "#DDD6C8"
FAM = {  # Darstellungsfamilie → Farbe (Palette des Bildstils, ergänzt um Malve)
    "erz": ("#BD8067", "Erzählung"),
    "rede": ("#C5A16D", "Rede und Lehre"),
    "ordnung": ("#A4AA87", "Gesetz, Listen, Bau"),
    "lied": ("#8CA8B3", "Lied, Gebet, Weisheit"),
    "proph": ("#9C8AA5", "Prophetie und Vision"),
    "brief": ("#62665D", "Brief und Argument"),
}
ART_FAM = {"erz": "erz", "rede": "rede", "gesetz": "ordnung", "liste": "ordnung", "bau": "ordnung", "poesie": "lied", "weisheit": "lied",
           "prophetie": "proph", "vision": "proph", "brief": "brief"}


def esc(s):
    return html.escape(str(s), quote=True)


def texte(muster):
    d = {}
    for f in glob.glob(str(ROOT / "data/translations" / muster)):
        d.update(json.loads(pathlib.Path(f).read_text(encoding="utf-8"))["text_by_reference"])
    return d


def bild(pfad, breite=900, qualitaet=74, crop=None):
    """Bild als data:-Adresse (JPEG, verkleinert)."""
    from PIL import Image
    im = Image.open(pfad).convert("RGB")
    if crop:
        w, h = im.size
        im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
    if im.width > breite:
        im = im.resize((breite, round(im.height * breite / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=qualitaet, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def t(x, y, s, size=13, fill=INK, anchor="start", weight=400, style="", fam="var(--f-text)"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" '
            f'font-family="{fam}" {style}>{esc(s)}</text>')


def umbruch(s, n):
    zeilen, z = [], ""
    for w in s.split():
        if len(z) + len(w) + 1 > n and z:
            zeilen.append(z)
            z = w
        else:
            z = (z + " " + w).strip()
    return zeilen + ([z] if z else [])


def tml(x, y, s, n, size=13, lh=1.35, **kw):
    return "".join(t(x, y + i * size * lh, z, size, **kw) for i, z in enumerate(umbruch(s, n)))


# ------------------------------------------------------------------ Bibelebene: Bibliothek nach Inhaltsarten

def bibliothek():
    d = json.loads((P / "inhaltsarten.json").read_text(encoding="utf-8"))
    buecher = d["buecher"]
    W, H, x0 = 1000, 350, 20
    at = [b for b in buecher if b["testament"] == "OT"]
    nt = [b for b in buecher if b["testament"] == "NT"]
    f = (W - 2 * x0 - 38 * 1.2) / sum(b["verse"] for b in at)
    teile = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="bib-t"><title id="bib-t">Die 66 Bücher als Bibliothek: Breite nach Versen, '
             f'Farben nach Inhaltsart</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    reihen = [(at, 46, "Altes Testament · 39 Bücher"), (nt, 214, "Neues Testament · 27 Bücher")]
    reihenfolge = ["erz", "rede", "ordnung", "lied", "proph", "brief"]
    for liste, y, titel in reihen:
        teile.append(t(x0, y - 12, titel, 13, INK, weight=600))
        x = x0
        gruppe, gx = None, x0
        for b in liste:
            w = max(1.6, b["verse"] * f)
            comp = d["je_buch"][b["code"]]
            fam = {}
            for a, n in comp.items():
                fam[ART_FAM[a]] = fam.get(ART_FAM[a], 0) + n
            yy = y
            hb = 92
            titel_b = f'{b["de"]}: {b["verse"]} Verse – ' + ", ".join(f'{FAM[k][1]} {round(100 * v / b["verse"])} %' for k, v in fam.items())
            teile.append(f'<g><title>{esc(titel_b)}</title>')
            for k in reihenfolge:
                if k in fam:
                    h = hb * fam[k] / b["verse"]
                    teile.append(f'<rect x="{x:.1f}" y="{yy:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{FAM[k][0]}"/>')
                    yy += h
            teile.append("</g>")
            if w > 15:
                teile.append(t(x + w / 2, y + hb + 13, ABK[b["code"]], 9.5, MUTED, "middle"))
            if b["gruppe"] != gruppe:
                if gruppe:
                    teile.append(f'<line x1="{gx}" x2="{x - 1.2:.1f}" y1="{y + hb + 22}" y2="{y + hb + 22}" stroke="{MUTED}" stroke-width="1"/>')
                    teile.append(t((gx + x - 1.2) / 2, y + hb + 35, kurz(gruppe), 10, MUTED, "middle"))
                gruppe, gx = b["gruppe"], x
            x += w + 1.2
        teile.append(f'<line x1="{gx}" x2="{x - 1.2:.1f}" y1="{y + hb + 22}" y2="{y + hb + 22}" stroke="{MUTED}" stroke-width="1"/>')
        teile.append(t((gx + x - 1.2) / 2, y + hb + 35, kurz(gruppe), 10, MUTED, "middle"))
    teile.append("</svg>")
    return "".join(teile)


ABK = dict(zip("GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH EZR NEH EST JOB PSA PRO ECC SNG ISA JER LAM EZK DAN HOS JOL AMO OBA JON MIC NAM HAB ZEP HAG ZEC MAL MAT MRK LUK JHN ACT ROM 1CO 2CO GAL EPH PHP COL 1TH 2TH 1TI 2TI TIT PHM HEB JAS 1PE 2PE 1JN 2JN 3JN JUD REV".split(),
    "Gen Ex Lev Num Dtn Jos Ri Rut 1Sam 2Sam 1Kön 2Kön 1Chr 2Chr Esra Neh Est Hiob Ps Spr Pred Hld Jes Jer Klgl Ez Dan Hos Joel Am Obd Jona Mi Nah Hab Zef Hag Sach Mal Mt Mk Lk Joh Apg Röm 1Kor 2Kor Gal Eph Phil Kol 1Thess 2Thess 1Tim 2Tim Tit Phlm Hebr Jak 1Petr 2Petr 1Joh 2Joh 3Joh Jud Offb".split()))


def kurz(g):
    return {"Die fünf Bücher Mose": "Mose", "Geschichtsbücher": "Geschichte", "Poesie und Weisheit": "Poesie", "Grosse Propheten": "Grosse Proph.",
            "Zwölf Propheten": "Zwölf", "Evangelien": "Evangelien", "Apostelgeschichte": "Apg", "Paulusbriefe": "Paulusbriefe",
            "Weitere Briefe": "Briefe", "Offenbarung": "Offb"}.get(g, g)


def anteile():
    d = json.loads((P / "inhaltsarten.json").read_text(encoding="utf-8"))
    zeilen = sorted(d["anteil"].items(), key=lambda kv: -kv[1])
    out = ['<div class="bars" role="list">']
    for a, pct in zeilen:
        farbe = FAM[ART_FAM[a]][0]
        out.append(f'<div class="bar" role="listitem"><span class="bar-l">{esc(d["arten"][a])}</span>'
                   f'<span class="bar-t"><span class="bar-f" style="width:{pct / 41 * 100:.1f}%;background:{farbe}"></span></span>'
                   f'<span class="bar-v">{str(pct).replace(".", ",")} %</span></div>')
    out.append("</div>")
    return "".join(out)


def legende():
    return '<div class="leg">' + "".join(f'<span><i style="background:{c}"></i>{esc(n)}</span>' for c, n in FAM.values()) + "</div>"


# ------------------------------------------------------------------ Testament/Gruppe: Zeitleiste

def zeitleiste():
    W, H = 1000, 330
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="zl-t"><title id="zl-t">Zeitleiste der biblischen Geschichte mit Büchern nach Handlungszeit</title>'
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    ep_alt = [("Urgeschichte", "Gen 1–11"), ("Väter", "Gen 12–50"), ("Ägypten, Auszug, Wüste", "Ex – Dtn"), ("Landnahme, Richter", "Jos, Ri, Rut")]
    o.append(t(20, 28, "ohne gesicherte Jahreszahl", 11, MUTED, style='font-style="italic"'))
    for i, (name, b) in enumerate(ep_alt):
        x = 20 + i * 92
        o.append(f'<rect x="{x}" y="40" width="86" height="44" rx="4" fill="#EADFCB" stroke="#CDBFA6" stroke-dasharray="3 3"/>')
        o.append(tml(x + 6, 57, name, 14, 10.5, fill=INK))
        o.append(t(x + 6, 100, b, 10, MUTED))
    X0, X1 = 410, 960
    def px(j):
        return X0 + (j + 1050) / (100 + 1050) * (X1 - X0)
    ya = 150
    o.append(f'<line x1="{X0}" x2="{X1}" y1="{ya}" y2="{ya}" stroke="{INK}" stroke-width="1.4"/>')
    for j, lab in [(-1000, "1000"), (-800, "800"), (-600, "600"), (-400, "400"), (-200, "200"), (0, "0"), (100, "100")]:
        o.append(f'<line x1="{px(j):.0f}" x2="{px(j):.0f}" y1="{ya - 4}" y2="{ya + 4}" stroke="{INK}"/>' + t(px(j), ya + 18, lab, 10, MUTED, "middle"))
    o.append(t(X0 - 6, ya + 4, "v. Chr.", 10, MUTED, "end") + t(X1, ya + 32, "n. Chr.", 10, MUTED, "end"))
    ep = [(-1050, -930, "Königtum", ["1–2 Sam", "1 Kön 1–11", "1 Chr, 2 Chr 1–9"]), (-930, -586, "Zwei Reiche", ["1 Kön 12 – 2 Kön", "Jes, Jer, Am, Hos", "Jona, Mi, Nah, Hab, Zef"]),
          (-586, -538, "Exil", ["Klgl, Obd", "Ez, Dan"]), (-538, -400, "Rückkehr", ["Esra, Neh, Est", "Hag, Sach, Mal"]),
          (-400, -5, "zwischen den Testamenten", ["kein biblisches Buch"]), (-5, 30, "Jesus", ["Evangelien"]), (30, 100, "Kirche", ["Apg", "Briefe, Offb"])]
    farben = ["#E3CDB0", "#E9D9C1", "#D9DFE2", "#E3E6D6", "#F0ECE4", "#EBD3C7", "#DCE3E6"]
    for i, (a, b, name, buecher) in enumerate(ep):
        y = 56 if i % 2 == 0 else 96
        w = px(b) - px(a)
        o.append(f'<rect x="{px(a):.1f}" y="{y}" width="{w:.1f}" height="34" rx="3" fill="{farben[i]}" stroke="#D2C7B4"/>')
        if w > 60:
            o.append(t(px(a) + 5, y + 21, name, 10.5, INK, weight=600))
        else:
            o.append(t(px(a) + w / 2, y - 5, name, 10.5, INK, "middle", 600))
        mitte = px(a) + w / 2
        for k, z in enumerate(buecher):
            o.append(t(mitte, 200 + k * 15 + (36 if i in (2, 5) else 0), z, 10, MUTED, "middle"))
        o.append(f'<line x1="{mitte:.1f}" x2="{mitte:.1f}" y1="{ya + 22}" y2="{188 + (36 if i in (2, 5) else 0)}" stroke="#D2C7B4"/>')
    for j in (-722, -586, -538):
        o.append(f'<circle cx="{px(j):.1f}" cy="{ya}" r="3.5" fill="#BD8067"/>')
    o.append(t(px(-722), ya - 10, "722", 10, "#8A4B33", "middle") + t(px(-586) - 3, ya - 10, "586", 10, "#8A4B33", "end") + t(px(-538) + 3, ya - 10, "538", 10, "#8A4B33", "start"))
    o.append(t(20, 300, "722 Samaria fällt · 586 Jerusalem zerstört · 538 Rückkehr erlaubt. Jahreszahlen sind gängige Schätzungen (R).", 10.5, MUTED))
    o.append(t(20, 318, "Die Bücher stehen bei der Zeit, von der sie erzählen oder in die sie sich selbst stellen; Psalmen, Weisheit und Joel haben keine feste Stelle.", 10.5, MUTED))
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ Buch Jona: Struktur neben den Szenen

def jona_struktur():
    W, H = 1000, 250
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="jo-t"><title id="jo-t">Jona: zwei parallele Hälften und der Abstieg</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    zeilen = [("Kap. 1", "Das Wort JHWHs ergeht an Jona", "1,1", "Jona flieht", "1,3", "Die Seeleute fürchten JHWH", "1,16"),
              ("Kap. 3", "Das Wort JHWHs ergeht ein zweites Mal", "3,1", "Jona geht", "3,3", "Die Leute von Ninive glauben an Gott", "3,5"),
              ("Kap. 2", "Jona betet aus dem Bauch des Fisches", "2,1", "dankt", "2,9", "«Die Rettung gehört JHWH»", "2,9"),
              ("Kap. 4", "Jona betet zornig", "4,2", "Gott fragt", "4,4", "Gottes Frage bleibt offen", "4,11")]
    o.append(t(20, 26, "Zwei Hälften laufen parallel", 13, INK, weight=600) + t(650, 26, "Der Abstieg (Leitwort «hinab»)", 13, INK, weight=600))
    for i, (k, a, ar, b, br, c, cr) in enumerate(zeilen):
        y = 48 + i * 46 + (12 if i >= 2 else 0)
        farbe = "#EFE2D4" if i < 2 else "#E2E8EA"
        o.append(f'<rect x="20" y="{y}" width="610" height="36" rx="4" fill="{farbe}"/>')
        o.append(t(30, y + 22, k, 11, MUTED, weight=600))
        for xx, s, r in [(80, a, ar), (334, b, br), (420, c, cr)]:
            o.append(t(xx, y + 16, s, 11.5, INK) + t(xx, y + 30, r, 9.5, MUTED))
        o.append(t(320, y + 22, "→", 12, MUTED) + t(406, y + 22, "→", 12, MUTED))
    # Treppe hinab
    st = [("stieg hinab nach Jafo", "1,3"), ("ins Schiff hinab", "1,3"), ("in den innersten Raum hinabgestiegen", "1,5"), ("zu den Wurzeln der Berge stieg ich hinab", "2,6")]
    for i, (s, r) in enumerate(st):
        x, y = 650 + i * 18, 46 + i * 44
        o.append(f'<path d="M{x} {y} h200 v44" fill="none" stroke="#8CA8B3" stroke-width="2"/>')
        o.append(t(x + 6, y + 18, s, 11.5, INK) + t(x + 6, y + 32, r, 9.5, MUTED))
    o.append(f'<path d="M920 228 C 948 190, 948 120, 930 72" fill="none" stroke="#BD8067" stroke-width="2" marker-end="url(#pf)"/>')
    o.append('<defs><marker id="pf" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#BD8067"/></marker></defs>')
    o.append(t(990, 150, "«holtest du mein", 10, "#8A4B33", "end") + t(990, 163, "Leben … herauf»", 10, "#8A4B33", "end") + t(990, 176, "2,6", 9.5, MUTED, "end"))
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ Brief: Titus 3,3–7 einst ↔ als aber

def titus_einst(vignette):
    d = texte("TRANS-TIT-003-*-DE-WORKING.json")
    einst = ["unverständig", "ungehorsam", "irregeführt", "Sklaven vielfältiger Begierden und Lüste", "in Bosheit und Neid", "verhasst", "hassten einander"]
    assert all(x in d["TIT.3.3"] for x in einst)
    W, H = 1000, 360
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="t3-t"><title id="t3-t">Titus 3,3–7: einst und als aber</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    o.append(t(30, 34, "einst", 16, "#62665D", weight=600, fam="var(--f-display)") + t(30, 52, "Tit 3,3", 10.5, MUTED))
    for i, s in enumerate(einst):
        o.append(t(30, 82 + i * 27, s, 13.5, "#5A5D55"))
    o.append(f'<line x1="300" x2="300" y1="20" y2="{H - 20}" stroke="{RULE}" stroke-width="1.5"/>')
    o.append(f'<rect x="318" y="20" width="250" height="96" rx="6" fill="#F1E6D6"/>')
    o.append(t(332, 44, "Als aber …", 16, "#8A4B33", weight=600, fam="var(--f-display)") + t(332, 62, "Tit 3,4", 10.5, MUTED))
    o.append(tml(332, 84, "die Güte und die Menschenfreundlichkeit Gottes, unseres Retters, erschien", 36, 12.5))
    o.append(f'<g opacity=".55"><text x="332" y="150" font-size="13" fill="{INK}" font-family="var(--f-text)" text-decoration="line-through">nicht aufgrund von Werken, die wir in</text>'
             f'<text x="332" y="168" font-size="13" fill="{INK}" font-family="var(--f-text)" text-decoration="line-through">Gerechtigkeit getan hätten</text></g>' + t(332, 186, "Tit 3,5", 10.5, MUTED))
    stufen = [("sondern nach seinem Erbarmen hat er uns gerettet", "3,5"), ("durch das Bad der Wiedergeburt und der Erneuerung des heiligen Geistes", "3,5"),
              ("gerecht gemacht durch seine Gnade", "3,7"), ("Erben gemäss der Hoffnung auf ewiges Leben", "3,7")]
    for s, _ in stufen:
        assert s.split(" ", 1)[1][:20] in d["TIT.3.5"] + d["TIT.3.7"] or s[:20] in d["TIT.3.5"] + d["TIT.3.7"]
    for i, (s, r) in enumerate(stufen):
        y = 214 + i * 36
        o.append(f'<rect x="318" y="{y - 18}" width="462" height="30" rx="4" fill="#E7ECEE"/>' + t(330, y + 1, s, 11.8, INK) + t(772, y + 1, r, 10, MUTED, "end"))
        if i:
            o.append(t(312, y - 20, "↓", 11, MUTED))
    if vignette:
        o.append(f'<image href="{vignette}" x="790" y="24" width="190" height="142" preserveAspectRatio="xMidYMid slice"/>')
        o.append(t(885, 182, "Vignette: Taufe (R)", 9.5, MUTED, "middle"))
    o.append("</svg>")
    return "".join(o)


def titus_nicht_sondern():
    d = texte("TRANS-TIT-001-*-DE-WORKING.json")
    nicht = ["nicht eigenmächtig", "nicht jähzornig", "kein Trinker", "kein Schläger", "nicht auf schändlichen Gewinn aus"]
    sondern = ["gastfreundlich", "dem Guten zugetan", "besonnen", "gerecht", "fromm", "beherrscht"]
    assert all(x in d["TIT.1.7"] for x in nicht) and all(x in d["TIT.1.8"] for x in sondern)
    W, H = 1000, 250
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="t1-t"><title id="t1-t">Titus 1,7–8: nicht … sondern</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    o.append(t(30, 34, "Der Aufseher muss als Verwalter Gottes untadelig sein:", 14, INK, weight=600) + t(30, 52, "Tit 1,7", 10.5, MUTED))
    for i, s in enumerate(nicht):
        y = 86 + i * 30
        o.append(f'<rect x="30" y="{y - 19}" width="420" height="26" rx="3" fill="#EEE9E1"/>')
        o.append(f'<text x="44" y="{y}" font-size="13.5" fill="#6E6F68" font-family="var(--f-text)" text-decoration="line-through">{esc(s)}</text>')
    o.append(t(470, 140, "sondern", 15, "#8A4B33", weight=600, fam="var(--f-display)") + t(470, 158, "Tit 1,8", 10.5, MUTED))
    for i, s in enumerate(sondern):
        y = 82 + i * 27
        o.append(f'<rect x="560" y="{y - 18}" width="300" height="24" rx="3" fill="#E5EBDF"/>' + t(574, y, s, 13.5, INK))
    o.append(t(880, 230, "5 Glieder ↔ 6 Glieder: so im Text", 10, MUTED, "end"))
    o.append("</svg>")
    return "".join(o)


def titus_buchband(vig_kreta, vig_hafen):
    W, H = 1000, 300
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="tb-t"><title id="tb-t">Titus als Buch: Form je Feld</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    felder = [("1,5", "Älteste in Kreta", "Szene", vig_kreta), ("1,6–9", "nicht … sondern", "Spalten", None), ("1,10–16", "Worte ↔ Werke", "Spalten", None),
              ("2,1–10", "Gruppen der Gemeinde", "Raster", None), ("2,11–14", "denn: die Gnade ist erschienen", "Pfeil", None),
              ("3,1–2", "Weisungen", "Raster", None), ("3,3–7", "einst ↔ als aber", "Spalten", None), ("3,8–11", "gute Werke ↔ Streit", "Spalten", None),
              ("3,12–15", "Zenas und Apollos", "Szene", vig_hafen)]
    w = 104
    for i, (ref, name, form, vig) in enumerate(felder):
        x = 16 + i * (w + 4)
        szene = form == "Szene"
        o.append(f'<rect x="{x}" y="58" width="{w}" height="130" rx="5" fill="{"#F3E7DA" if szene else "#ECEFEA"}" stroke="{RULE}"/>')
        if vig:
            o.append(f'<image href="{vig}" x="{x + 3}" y="61" width="{w - 6}" height="78" preserveAspectRatio="xMidYMid slice"/>')
        else:
            o.append(miniform(form, x + w / 2, 100))
        o.append(t(x + 6, 156, ref, 10, MUTED) + tml(x + 6, 172, name, 16, 10.5))
        o.append(t(x + w / 2, 208, form, 10, "#8A4B33" if szene else "#5C6B52", "middle", 600))
    for a, b, lab in [(0, 4, "Pflichten … denn: Gnade"), (5, 6, "Weisungen … denn: einst – jetzt")]:
        xa, xb = 16 + a * (w + 4) + 10, 16 + b * (w + 4) + w - 10
        o.append(f'<path d="M{xa} 236 Q {(xa + xb) / 2} 266 {xb} 236" fill="none" stroke="#9C8AA5" stroke-width="1.6"/>' + t((xa + xb) / 2, 278, lab, 10.5, "#6A5A73", "middle"))
    o.append(t(16, 34, "Kapitel 1", 12, INK, weight=600) + t(16 + 3 * (w + 4), 34, "Kapitel 2", 12, INK, weight=600) + t(16 + 5 * (w + 4), 34, "Kapitel 3", 12, INK, weight=600))
    o.append("</svg>")
    return "".join(o)


def miniform(form, cx, cy):
    g = f'stroke="#7F8F75" stroke-width="1.6" fill="none"'
    if form == "Spalten":
        return (f'<line x1="{cx}" x2="{cx}" y1="{cy - 28}" y2="{cy + 28}" {g}/>' + "".join(
            f'<line x1="{cx - 36}" x2="{cx - 8}" y1="{cy - 20 + k * 12}" y2="{cy - 20 + k * 12}" {g}/><line x1="{cx + 8}" x2="{cx + 36}" y1="{cy - 20 + k * 12}" y2="{cy - 20 + k * 12}" {g}/>' for k in range(4)))
    if form == "Raster":
        return "".join(f'<rect x="{cx - 36 + c * 25}" y="{cy - 26 + r * 18}" width="21" height="14" {g}/>' for r in range(3) for c in range(3))
    if form == "Pfeil":
        return f'<path d="M{cx - 36} {cy} H{cx + 30} M{cx + 22} {cy - 7} L{cx + 32} {cy} L{cx + 22} {cy + 7}" {g}/><rect x="{cx - 44}" y="{cy - 14}" width="20" height="28" {g}/>'
    return ""


# ------------------------------------------------------------------ Hymnus: Philipper 2,6–11

def phil2():
    d = texte("TRANS-PHP-002-*-DE-WORKING.json")
    ab = [("in der Gestalt Gottes", "2,6"), ("entäusserte sich selbst", "2,7"), ("nahm die Gestalt eines Sklaven an", "2,7"),
          ("erniedrigte er sich selbst", "2,8"), ("gehorsam bis zum Tod, ja zum Tod am Kreuz", "2,8")]
    auf = [("Darum hat Gott ihn auch über alles erhöht", "2,9"), ("den Namen geschenkt, der über jedem Namen ist", "2,9"),
           ("damit im Namen Jesu jedes Knie sich beuge", "2,10"), ("und jede Zunge bekenne, dass Jesus Christus der Herr ist", "2,11")]
    alle = " ".join(d[f"PHP.2.{v}"] for v in range(6, 12))
    assert all(s in alle for s, _ in ab + auf), [s for s, _ in ab + auf if s not in alle]
    W, H = 1000, 400
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="ph-t"><title id="ph-t">Philipper 2,6–11 als Weg hinab und hinauf</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    pts_ab = [(300 + i * 42, 36 + i * 62) for i in range(5)]
    tief = (500, 334)
    pts_auf = [(580 + i * 46, 270 - i * 72) for i in range(4)]
    weg = "M" + " L".join(f"{x} {y}" for x, y in pts_ab + [tief] + pts_auf)
    o.append(f'<path d="{weg}" fill="none" stroke="#D9CBB6" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>')
    for (x, y), (s, r) in zip(pts_ab, ab):
        z = umbruch(s, 30)
        o.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#62665D"/>' + "".join(t(x - 16, y + 4 + k * 16, zz, 12.5, INK, "end") for k, zz in enumerate(z))
                 + t(x - 16, y + 4 + len(z) * 16, r, 9.5, MUTED, "end"))
    for (x, y), (s, r) in zip(pts_auf, auf):
        z = umbruch(s, 30)
        o.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#BD8067"/>' + "".join(t(x + 16, y + 4 + k * 16, zz, 12.5, INK) for k, zz in enumerate(z))
                 + t(x + 16, y + 4 + len(z) * 16, r, 9.5, MUTED))
    o.append(t(40, 380, "hinab: er selbst handelt (2,6–8)", 12, "#62665D", weight=600) + t(960, 380, "hinauf: Gott handelt (2,9–11)", 12, "#8A4B33", "end", 600))
    o.append(t(500, 362, "Wende: «Darum» (2,9)", 11, MUTED, "middle"))
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ Prophetie: Obadja hoch → tief, Karte

def obadja():
    d = texte("TRANS-OBA-*-DE-WORKING.json")
    zit = [("Wer stürzt mich zu Boden?", "OBA.1.3"), ("Wenn du auch hoch baust wie der Adler", "OBA.1.4"), ("von dort stürze ich dich hinab", "OBA.1.4"),
           ("Wie du getan hast, wird dir getan werden", "OBA.1.15"), ("Retter werden hinaufziehen auf den Berg Zion", "OBA.1.21"),
           ("die Königsherrschaft wird JHWH gehören", "OBA.1.21")]
    assert all(s in d[r] for s, r in zit)
    geo = json.loads((ROOT / "pilot/struktur/levante-naturalearth.json").read_text(encoding="utf-8"))
    W, H = 1000, 380
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="ob-t"><title id="ob-t">Obadja: Edom hoch und tief, Zion hinauf; Lage auf der Karte</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    o.append(f'<path d="M60 130 C 230 140, 380 290, 580 320" fill="none" stroke="#9C8AA5" stroke-width="3"/>')
    o.append(f'<path d="M60 320 C 230 310, 380 160, 580 130" fill="none" stroke="#BD8067" stroke-width="3" stroke-dasharray="7 5"/>')
    o.append(tml(40, 30, "«Wenn du auch hoch baust wie der Adler … von dort stürze ich dich hinab» (1,4)", 36, 12.5, fill="#5A4A63"))
    o.append(t(60, 122, "Edom hoch", 12, "#5A4A63", weight=600))
    o.append(tml(330, 30, "«Retter werden hinaufziehen auf den Berg Zion … die Königsherrschaft wird JHWH gehören» (1,21)", 36, 12.5, fill="#8A4B33"))
    o.append(t(580, 122, "Zion oben", 12, "#8A4B33", "end", 600))
    o.append(f'<rect x="200" y="200" width="240" height="46" rx="5" fill="{PAPER}" stroke="{RULE}"/>')
    o.append(t(320, 220, "«Wie du getan hast,", 12.5, INK, "middle") + t(320, 237, "wird dir getan werden» (1,15)", 12.5, INK, "middle"))
    o.append(t(60, 344, "Zion unten", 12, "#8A4B33", weight=600) + t(580, 344, "Edom unten", 12, "#5A4A63", "end", 600))
    o.append(t(40, 370, "Umkehrung (Spiegel): was Edom tat, fällt auf Edom zurück; der Berg Zion steigt.", 10.5, MUTED))
    lon0, lon1, lat0, lat1 = 34.75, 36.05, 30.05, 32.15
    mx, my, mw, mh = 640, 20, 330, 340
    def p(lon, lat):
        return mx + (lon - lon0) / (lon1 - lon0) * mw, my + (lat1 - lat) / (lat1 - lat0) * mh
    o.append(f'<rect x="{mx}" y="{my}" width="{mw}" height="{mh}" fill="#F3EEE4" stroke="{RULE}"/>')
    for poly in geo["lakes:Dead Sea"]:
        o.append('<path d="M' + " L".join("%.1f %.1f" % p(x, y) for x, y in poly) + 'Z" fill="#B9CCD3"/>')
    for poly in geo["rivers_lake_centerlines:Jordan"]:
        o.append('<path d="M' + " L".join("%.1f %.1f" % p(x, y) for x, y in poly if y < lat1) + '" fill="none" stroke="#9FB7C0" stroke-width="1.4"/>')
    ex, ey = p(35.55, 30.55)
    o.append(f'<ellipse cx="{ex}" cy="{ey}" rx="62" ry="58" fill="#9C8AA5" fill-opacity=".18" stroke="#9C8AA5" stroke-dasharray="4 3"/>' + t(ex, ey + 4, "Edom", 12.5, "#5A4A63", "middle", 600))
    jx, jy = p(35.23, 31.78)
    o.append(f'<circle cx="{jx}" cy="{jy}" r="4.5" fill="#BD8067"/>' + t(jx - 8, jy + 4, "Jerusalem (Zion)", 11.5, "#8A4B33", "end"))
    tx, ty = p(35.5, 31.5)
    o.append(t(tx + 22, ty, "Totes Meer", 10, "#5F7D88"))
    o.append(t(mx + 8, my + mh - 10, "Lage ungefähr (R)", 9.5, MUTED))
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ Stammbaum: Matthäus 1, drei mal vierzehn

def matthaeus1():
    reihen = [["Abraham", "Isaak", "Jakob", "Juda", "Perez", "Hezron", "Ram", "Amminadab", "Nachschon", "Salmon", "Boas", "Obed", "Isai", "David"],
              ["Salomo", "Rehabeam", "Abija", "Asaf", "Joschafat", "Joram", "Usija", "Jotam", "Ahas", "Hiskija", "Manasse", "Amos", "Joschija", "Jechonja"],
              ["Schealtiël", "Serubbabel", "Abihud", "Eljakim", "Azor", "Zadok", "Achim", "Eliud", "Eleasar", "Mattan", "Jakob", "Josef", "Jesus"]]
    d = texte("TRANS-MAT-001-*-DE-WORKING.json")
    alle = " ".join(d[f"MAT.1.{v}"] for v in range(2, 17))
    assert all(n in alle for r in reihen for n in r if n != "Jesus")
    frauen = {"Juda": "Tamar", "Salmon": "Rahab", "Boas": "Rut", "David": "Frau des Urija"}
    W, H = 1000, 330
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="mt-t"><title id="mt-t">Matthäus 1: drei Reihen von Generationen</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    titel = ["von Abraham bis David", "von David bis zur Wegführung nach Babylon", "von der Wegführung nach Babylon bis zum Christus"]
    for r, namen in enumerate(reihen):
        y = 40 + r * 92
        o.append(t(20, y - 8, f"vierzehn Generationen {titel[r]}", 12, INK, weight=600) + t(980, y - 8, f"im Text genannt: {len(namen)} Namen", 10, MUTED, "end"))
        for i, n in enumerate(namen):
            x = 20 + i * 69.3
            o.append(f'<rect x="{x}" y="{y}" width="65" height="34" rx="3" fill="{"#F1E1D2" if n in ("David", "Jesus") else "#ECEEE7"}"/>')
            o.append(t(x + 32.5, y + 21, n, 10.2 if len(n) < 10 else 9, INK, "middle"))
            if n in frauen and r == 0 or (n == "David" and r == 0):
                o.append(t(x + 32.5, y + 48, "+ " + frauen[n], 9.5, "#8A4B33", "middle"))
    o.append(t(20, 318, "Mt 1,17 nennt dreimal vierzehn; in der dritten Reihe stehen dreizehn Namen. Wie gezählt wird, ist eine Deutungsfrage; das Bild glättet die Zahl nicht.", 10.5, MUTED))
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ Poesie: Psalm 1, zwei Wege

def psalm1(vb, vs):
    W, H = 1000, 360
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="ps-t"><title id="ps-t">Psalm 1: zwei Wege</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    for x, vig, titel, z1, z2, farbe in [(40, vb, "Der Gerechte", "wie ein Baum, gepflanzt an Wasserbächen", "Ps 1,3", "#5C6B52"),
                                         (520, vs, "Die Gottlosen", "wie Spreu, die der Wind verweht", "Ps 1,4", "#6A5A73")]:
        if vig:
            o.append(f'<image href="{vig}" x="{x}" y="14" width="440" height="210" preserveAspectRatio="xMidYMid meet"/>')
        else:
            o.append(f'<rect x="{x + 70}" y="14" width="300" height="210" fill="#EEE9E1"/>' + t(x + 220, 124, "(Vignette folgt)", 11, MUTED, "middle"))
        o.append(t(x + 220, 250, titel, 17, farbe, "middle", 600, fam="var(--f-display)") + t(x + 220, 272, z1, 12.5, INK, "middle") + t(x + 220, 290, z2, 10, MUTED, "middle"))
    o.append(f'<line x1="500" x2="500" y1="30" y2="290" stroke="{RULE}"/>')
    o.append(t(500, 326, "JHWH kennt den Weg der Gerechten, der Weg der Gottlosen vergeht (Ps 1,6)", 13, INK, "middle"))
    o.append(t(500, 348, "Stichworte sinngemäss: Für die Psalmen gibt es noch keine Arbeitsübersetzung. Die Vignetten malen nur die Bildworte des Psalms.", 10, MUTED, "middle"))
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ Vision: Offenbarung, drei Siebenerreihen

def offb():
    W, H = 1000, 270
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="of-t"><title id="of-t">Offenbarung 6–16: drei Siebenerreihen mit Einschüben</title><rect width="{W}" height="{H}" fill="{PAPER}"/>']
    reihen = [("7 Siegel", "6,1 – 8,1", "Kap. 7"), ("7 Posaunen", "8,2 – 11,19", "10,1 – 11,14"), ("7 Schalen", "16,1–21", None)]
    for r, (name, ref, einschub) in enumerate(reihen):
        y = 34 + r * 76
        o.append(t(20, y + 22, name, 13, INK, weight=600) + t(20, y + 38, ref, 10, MUTED))
        for i in range(7):
            x = 150 + i * 92 + (40 if i == 6 and einschub else 0)
            o.append(f'<rect x="{x}" y="{y}" width="80" height="40" rx="4" fill="{"#E7DFEA" if i == 6 else "#EFEBF1"}" stroke="#C7BBCD"/>' + t(x + 40, y + 25, str(i + 1), 13, "#5A4A63", "middle"))
            if i == 5 and einschub:
                o.append(f'<rect x="{x + 85}" y="{y + 6}" width="38" height="28" rx="3" fill="{PAPER}" stroke="#9C8AA5" stroke-dasharray="3 3"/>' + t(x + 104, y + 54, einschub, 9.5, "#6A5A73", "middle"))
        if r < 2:
            xs = 150 + 6 * 92 + 40 + 40
            o.append(f'<path d="M{xs} {y + 40} C {xs} {y + 62}, 190 {y + 52}, 190 {y + 76}" fill="none" stroke="#9C8AA5" stroke-width="1.4" marker-end="url(#pf2)"/>')
    o.append('<defs><marker id="pf2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#9C8AA5"/></marker></defs>')
    o.append(t(20, 258, "Gestrichelt: Einschub vor dem siebten Glied bei Siegeln und Posaunen (so im Text). Ob die Reihen nacheinander folgen oder dasselbe neu zeigen, ist Deutung.", 10.5, MUTED))
    o.append("</svg>")
    return "".join(o)


# ------------------------------------------------------------------ Vers: Merkkarte

def merkkarte(bild_url):
    d = texte("TRANS-LUK-015*-DE-WORKING.json")
    v = d["LUK.15.24"]
    assert "war tot und ist wieder lebendig geworden" in v and "war verloren und ist gefunden worden" in v
    return (f'<div class="merk"><div class="merk-v"><img src="{bild_url}" alt="Der Vater umarmt den heimgekehrten Sohn (Lk 15,20)">'
            f'<div><p class="merk-ref">Lukas 15,24</p><p class="merk-z">«denn dieser mein Sohn war <span class="luecke">tot</span> und ist wieder '
            f'<span class="luecke">lebendig</span> geworden; er war <span class="luecke">verloren</span> und ist gefunden worden.»</p>'
            f'<p class="merk-h">Antippen deckt die Lücken auf. Wiederholen: heute · morgen · in einer Woche · später</p></div></div></div>')
