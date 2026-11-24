#!/usr/bin/env python3
"""Strukturbilder aus den Bildaufträgen für die übrigen Zoomstufen (Entscheid Andi Neck 2026-11-24).

Für Bibel, Testamente, Buchgruppen, Kapitel und Abschnitte, die noch kein Bild im Aquarellstil haben, entsteht aus dem
bestehenden Bildauftrag (Felder mit Stelle, Stichwort, Figuren, Gegenständen, Zeichen) ein gezeichnetes Strukturbild
(struktur_kachel.py): je Feld eine Karte mit dem Stichwort und bis zu drei Bildern aus dem Bildlexikon. Es wird nichts
gemalt; die Bilder sind die geprüften Einzelbilder des Lexikons (freigestellt). Personen ohne Wiederkehr erscheinen nicht
als Bild (personen.py), ihr Name steht im Stichwort; Gott ist der gezeichnete Strahlenkranz.

Kartentext und Bilder je Karte kommen aus kartentexte.py (strukturgeruest_daten/karten.json: kurzer vollständiger Text, keine
Karte ohne Bild, Entscheid 2026-11-24). Ohne gültigen Eintrag dort gilt die frühere Regel: Stichwort aus dem Bildauftrag,
Personen und Gruppen, dann Gegenstände und Orte, dann Zeichen; nur Einträge mit geprüftem Bild. Malt das Lexikon später fehlende Einträge, erscheinen sie
beim nächsten Lauf («fehlend» listet sie).

    python3 scripts/authoring/strukturgeruest.py schreiben     # Szenenpläne szenen-struktur-<buch>.json
    python3 scripts/authoring/strukturgeruest.py fehlend       # Lexikon-Einträge, deren Bild den Karten noch fehlt
"""
import collections
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
BRIEFS = ROOT / "data/illustrations/briefs"
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import personen as P  # noqa: E402
import vignetten as V  # noqa: E402

EBENEN = ("bible", "testament", "group", "chapter", "section")
KARTEN_DATEI = ROOT / "scripts/authoring/strukturgeruest_daten/karten.json"
KARTEN = json.loads(KARTEN_DATEI.read_text(encoding="utf-8")) if KARTEN_DATEI.exists() else {}


def KARTEN_GUELTIG(b):
    """Karten aus kartentexte.py gelten, wenn sie zum aktuellen Bildauftrag passen (Fingerabdruck) und ohne Befund sind."""
    import kartentexte as K
    ks = KARTEN.get(b["id"])
    if not ks or len(ks) != len(b["panels"]) or any(k.get("befunde") for k in ks):
        return False
    akt = K.gsw_aktionen(b)
    return all(k.get("fp") == K.fingerabdruck(b, i, akt[i] if i < len(akt) else "") for i, k in enumerate(ks))
MAX_BILDER = 3


def lade(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))


def schon_aquarell():
    """Bildaufträge, die schon ein Aquarellbild aus einem anderen Plan haben (Merkbilder, Pilotkapitel, Buchebene)."""
    out = set()
    for p in DATEN.glob("szenen-*.json"):
        if p.name.startswith("szenen-struktur-"):
            continue
        for b in lade(p)["bilder"]:
            out.add(b["brief"])
    return out


def kandidaten(pa):
    for f in pa.get("figures", []) + pa.get("objects", []) + pa.get("signs", []):
        if f == "FIG-GOTT" or not P.nur_namensschild(f):
            yield f


def kurz(s, n=70):
    """Handlung als Kartentext: ganz, wenn kurz; sonst bis zum Doppelpunkt; sonst bis zum letzten Wort vor n Zeichen."""
    s = s.strip().rstrip(".")
    if len(s) <= n:
        return s
    if ":" in s and len(s.split(":")[0]) >= 8:
        return s.split(":")[0]
    return s[:n].rsplit(" ", 1)[0] + " …"


def depicts(pa):
    return [f for f in dict.fromkeys(kandidaten(pa)) if V.bild(f)][:MAX_BILDER]


# Einprägsame Strukturen (Rückmeldung Andi Neck 2026-11-24: «vorher war es bedeutend voller hier mit Strukturen, die sich einprägen
# lassen»; auf Versebene waren drei Bilder zusammen zu klein): je Feld des Bildauftrags eine eigene Kachel. Hat das Feld ein
# Diagramm (Raster, Pfeilkette, Gegenüberstellung, Stufen, Ebenen …), wird es in der passenden Strukturform gezeichnet, mit dem
# Wortlaut des Diagramms und den Zeichen als Bilder aus dem Bildlexikon; sonst eine Karte mit grossen Bildern (kartentexte.py).
# Die App stellt auf Versebene jede Kachel neben die Verse ihres Felds. Zuerst für die Bücher und Kapitel in FELDWEISE.
FELDWEISE = ("BRIEF-MAT-005",)


def feldweise(b):
    return b["level"] == "section" and b["id"].startswith(FELDWEISE)


def _bilder(icons):
    return [f for f in dict.fromkeys(icons or []) if f == "FIG-GOTT" or (V.bild(f) and not P.nur_namensschild(f))][:MAX_BILDER]


def _glied(c, seite=None):
    """Zelle eines Diagramms → Glied der Strukturkachel."""
    a = c.get("a") or {}
    e = {"de": a.get("de", ""), "gsw": a.get("gsw") or a.get("de", "")}
    if c.get("b"):
        e["unter"] = {"de": c["b"].get("de", ""), "gsw": c["b"].get("gsw") or c["b"].get("de", "")}
    if c.get("role"):
        e["rolle"] = {"de": c["role"].get("de", ""), "gsw": c["role"].get("gsw") or c["role"].get("de", "")}
    if c.get("tone") == "new":
        e["betont"] = True
    if c.get("strike"):
        e["gestrichen"] = True
    if seite:
        e["seite"] = seite
    d = _bilder(([c["who"]] if isinstance(c.get("who"), str) else []) + list(c.get("icons") or []))
    if d:
        e["depicts"] = d
    return e


def _text(x):
    return {"de": x.get("de", ""), "gsw": x.get("gsw") or x.get("de", "")} if isinstance(x, dict) and x.get("de") else None


def diagramm_struktur(d):
    """Diagramm eines Bildauftrags (diagram.visual) → Strukturkachel (struktur_kachel.py). Allgemein für alle Formen."""
    v = d.get("visual")
    sx = {"quelle": "diagramm"}
    if _text(d.get("title")):
        sx["titel"] = _text(d["title"])
    zellen = [c for c in d.get("cells") or [] if isinstance(c, dict) and c.get("a") and not c.get("empty")]
    if v in ("columns", "balance") or (v == "mirror" and d.get("rows")):
        kopf = d.get("head") or []
        if len(kopf) >= 2 and _text(kopf[0]) and _text(kopf[1]):
            sx["kopf"] = {"a": _text(kopf[0]), "b": _text(kopf[1])}
        el = []
        for r in d.get("rows") or []:
            for c, sd in zip(r, ("a", "b")):
                if isinstance(c, dict) and c.get("a"):
                    el.append(_glied(c, sd))
        if not el and (d.get("left") or d.get("right")):
            el = [_glied(c, "a") for c in d.get("left") or [] if c.get("a")] + [_glied(c, "b") for c in d.get("right") or [] if c.get("a")]
        if not el:   # Spalten ohne Zeilen: Zellen abwechselnd
            el = [_glied(c, "ab"[i % 2]) for i, c in enumerate(zellen)]
        return {**sx, "typ": "spalten", "elemente": el} if el else None
    if v == "switch":
        el = [_glied(d[k], sd) for k, sd in (("yes", "a"), ("no", "b")) if isinstance(d.get(k), dict) and d[k].get("a")]
        if _text((d.get("cond") or {}).get("a")):
            sx["mitte"] = _text(d["cond"]["a"])
        if _text(d.get("yes_label")) and _text(d.get("no_label")):
            sx["kopf"] = {"a": _text(d["yes_label"]), "b": _text(d["no_label"])}
        return {**sx, "typ": "spalten", "elemente": el} if el else None
    if v == "levels":
        el = [_glied(c, "a") for c in d.get("top") or [] if c.get("a")] + [_glied(c, "b") for c in d.get("bottom") or [] if c.get("a")]
        kopf = {k: _text(d.get(l)) for k, l in (("a", "top_label"), ("b", "bottom_label")) if _text(d.get(l))}
        if kopf:
            sx["kopf"] = kopf
        return {**sx, "typ": "ebenen", "elemente": el} if el else None
    if v in ("arrows", "stairs", "dialogue", "timeline"):
        quelle = zellen or [t for t in d.get("turns") or [] if isinstance(t, dict) and t.get("a")]
        el = []
        for c in quelle:
            sd = "a" if c.get("tone") == "old" else ("b" if v == "stairs" and el and c.get("role") else None)
            el.append(_glied(c, sd))
        if v == "stairs":   # nach «Ich aber sage euch» gehören die Stufen zur neuen Seite
            neu = False
            for e in el:
                neu = neu or e.get("seite") == "b"
                if neu and not e.get("seite"):
                    e["seite"] = "b"
        links = [(_text(x) if x else None) for x in d.get("links") or []]
        if any(links):
            sx["verbindungen"] = [None] + links
        return {**sx, "typ": "kette", "elemente": el} if el else None
    # Raster und alle übrigen Formen: die Zellen nebeneinander
    if not zellen:
        for k in ("top", "bottom", "left", "right", "ring", "core", "there", "back", "up"):
            x = d.get(k)
            zellen += [c for c in (x if isinstance(x, list) else [x]) if isinstance(c, dict) and c.get("a")]
    el = [_glied(c) for c in zellen]
    return {**sx, "typ": "raster", "elemente": el} if el else None


def plan_code(b):
    return "oben" if b["level"] in ("bible", "testament", "group") else b["id"].split("-")[1].lower()


def schreibe():
    fertig = schon_aquarell()
    plaene = collections.defaultdict(lambda: {"bilder": [], "szenen": {}})
    for p in sorted(BRIEFS.glob("BRIEF-*.json")):
        b = lade(p)
        if b.get("level") not in EBENEN or b["id"] in fertig or not b.get("panels"):
            continue
        rest = b["id"][len("BRIEF-"):]
        sid = f"S-{rest}"
        el = []
        loc = ROOT / f"data/localizations/gsw-u-sd-chzh/{b['id']}.json"
        akt_gsw = (lade(loc).get("fields") or {}).get("actions_de") or [] if loc.exists() else []
        karten = KARTEN.get(b["id"]) if KARTEN_GUELTIG(b) else None
        for i, pa in enumerate(b["panels"]):
            if karten:   # kartentexte.py: kurzer vollständiger Text und Bilder je Karte (Entscheid 2026-11-24)
                k = karten[i]
                e = {"de": k["de"], "gsw": k["gsw"]}
                if pa.get("reference"):
                    e["ref"] = pa["reference"]
                if k.get("bilder"):
                    e["depicts"] = [f for f in k["bilder"] if f == "FIG-GOTT" or V.bild(f)]
                el.append(e)
                continue
            kw = pa.get("keywords") or {}
            if kw.get("de"):
                e = {"de": kw["de"], "gsw": kw.get("gsw") or kw["de"]}
            else:   # obere Ebenen ohne Stichwort: Handlung, bei langen nur der Teil vor dem Doppelpunkt
                e = {"de": kurz(pa.get("action_de", "")), "gsw": kurz(akt_gsw[i] if i < len(akt_gsw) else pa.get("action_de", ""))}
            if pa.get("reference"):
                e["ref"] = pa["reference"]
            d = depicts(pa)
            if d:
                e["depicts"] = d
            el.append(e)
        if not any(e.get("depicts") for e in el):   # ohne jedes Bild bringt das Strukturbild nichts; bis das Lexikon die Bilder hat, bleibt das bisherige
            continue
        pl = plaene[plan_code(b)]
        if feldweise(b):   # je Feld eine Kachel: Diagramm als Strukturform, sonst eine Karte mit grossen Bildern
            felder = []
            for i, (pa, e) in enumerate(zip(b["panels"], el), 1):
                fid = f"{sid}-{i}"
                sx = diagramm_struktur(pa["diagram"]) if pa.get("diagram") else None
                if not sx:
                    sx = {"typ": "raster", "elemente": [e]}
                pl["szenen"][fid] = {
                    "brief": b["id"], "panel": i, "reference": pa.get("reference") or b.get("reference") or "", "form": "struktur",
                    "form_grund_de": "Feld des Bildauftrags als eigene Kachel: Diagramm in der passenden Strukturform, sonst eine Karte "
                                     "mit grossen Bildern (Rückmeldung Andi Neck 2026-11-24, strukturgeruest.py).",
                    "depicts": [], "bild_en": "", "speech": [],
                    "evidence": [{"s": "B", "ref": pa["reference"], "de": pa.get("action_de", "")}] if pa.get("reference") else
                                [{"s": "I", "de": "Feld aus dem Bildauftrag."}],
                    "pruefung": [], "struktur": sx, "band": {"de": "", "gsw": ""}}
                felder.append(fid)
            pl["bilder"].append({"id": f"ILL-AQU-{rest}", "brief": b["id"], "level": b["level"], "reference": b.get("reference") or "",
                                 "target": b.get("target"), "felder": felder,
                                 "note_de": b.get("interpretation_note_de") or "Strukturbild: je Feld des Bildauftrags eine Kachel; Bilder aus dem Bildlexikon."})
            continue
        pl["szenen"][sid] = {
            "brief": b["id"], "panel": 1, "reference": b.get("reference") or "", "form": "struktur",
            "form_grund_de": "Strukturbild aus dem Bildauftrag: je Feld eine Karte mit Stichwort und Bildern aus dem Bildlexikon "
                             "(Entscheid Andi Neck 2026-11-24, scripts/authoring/strukturgeruest.py).",
            "depicts": [], "bild_en": "", "speech": [],
            "evidence": [{"s": "B", "ref": pa["reference"], "de": pa.get("action_de", "")} for pa in b["panels"] if pa.get("reference")]
                        or [{"s": "I", "de": "Übersicht aus der Zusammenfassung; Auswahl redaktionell."}],
            "pruefung": [],
            "struktur": {"typ": "reihe", "elemente": el, **({"mit_buch": True} if b["level"] in ("bible", "testament", "group") else {})},
            "band": {"de": "", "gsw": ""},
        }
        pl["bilder"].append({"id": f"ILL-AQU-{rest}", "brief": b["id"], "level": b["level"], "reference": b.get("reference") or "",
                             "target": b.get("target"), "felder": [sid], "gesamt": True,
                             "note_de": b.get("interpretation_note_de") or "Strukturbild: Felder und Stichworte aus dem Bildauftrag, Bilder aus dem Bildlexikon."})
    n = 0
    for code, pl in plaene.items():
        plan = {"_hinweis": "Strukturgerüst (scripts/authoring/strukturgeruest.py): Strukturbilder aus den Bildaufträgen, Bilder aus dem Bildlexikon.",
                "basis": [], "tags": [], "figurenblatt": None, "figuren": {}, "kenn_en": {}, "pruef": {}, **pl}
        (DATEN / f"szenen-struktur-{code}.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += len(pl["bilder"])
    print(f"{n} Strukturbilder in {len(plaene)} Plänen")


def fehlend():
    c = collections.Counter()
    for p in BRIEFS.glob("BRIEF-*.json"):
        b = lade(p)
        if b.get("level") not in EBENEN:
            continue
        for pa in b.get("panels", []):
            for f in kandidaten(pa):
                if f != "FIG-GOTT" and not V.bild(f):
                    c[f] += 1
    for f, n in c.most_common():
        print(f"{n:4d} {f}")
    print(f"{len(c)} Einträge ohne Bild")


if __name__ == "__main__":
    {"schreiben": schreibe, "fehlend": fehlend}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda: print(__doc__))()
