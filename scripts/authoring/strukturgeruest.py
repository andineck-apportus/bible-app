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
