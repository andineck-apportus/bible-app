#!/usr/bin/env python3
"""Buchgerüst: Buchebene aller 66 Bücher im Aquarellstil, Form je Station (Entscheid Andi Neck 2026-11-21, docs/VISUELLE-SPRACHE.md).

Quelle je Buch: scripts/authoring/bilder_aquarell_daten/buch/<BUCH>.json (Format siehe FORMAT unten). Daraus entstehen:
  - der Szenenplan scripts/authoring/bilder_aquarell_daten/szenen-buch-<buch>.json (gemalte Stationen und Strukturstationen),
  - der Bildauftrag data/illustrations/briefs/BRIEF-<BUCH>.json, falls es noch keinen gibt (sonst muss das Gerüst ihm folgen),
  - neue Einträge im Bildlexikon data/illustrations/lexicon/FIG-*.json für Personen, die dort fehlen.

  python3 scripts/authoring/buchgeruest.py pruefen [BUCH …]   Format, Stellen, Längen, Lexikon prüfen (ohne zu schreiben)
  python3 scripts/authoring/buchgeruest.py schreiben [BUCH …] prüfen und Plan, Bildauftrag, Lexikon schreiben

Vorläufig von oben: Wo ein Buch noch keine Abschnittsanalysen hat, stammen die Stationen aus dem Strukturkatalog und der
Zusammenfassung des Buchs; sie werden ersetzt, sobald das Buch von unten bearbeitet ist. Ohne Arbeitsübersetzung ist das Band ein
Titel in eigenen Worten (kein Zitat), und es gibt keine Sprechblasen.
"""
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
QUELLE = DATEN / "buch"
LEX = ROOT / "data/illustrations/lexicon"
BRIEFS = ROOT / "data/illustrations/briefs"
HEUTE = datetime.date.today().isoformat()
AUTOR = "KI-Entwurf (Claude) vom {d} auf Wunsch von Andi Neck (Buchgerüst, docs/VISUELLE-SPRACHE.md); vorläufig von oben, keine fachliche Prüfung."

FORMAT = """
{
  "buch": "GEN",
  "zweck_de": "wozu das Buch geschrieben ist (1–2 Sätze, Deutung als solche kennzeichnen)",
  "note_de": "Bildhinweis für die Legende (2–3 Sätze, mit [[GEN.1.1]]-Marken): was gezeigt wird, was weggelassen ist, was gedeutet ist",
  "quelle_de": "woher die Stationen stammen (z. B. Strukturkatalog Bücherübersicht; SUM-BOOK-GEN)",
  "figuren": {"FIG-…": "English painting description: age, hair, beard, clothing colours, recognisable signs"},
  "kenn_en": {"FIG-…": "short English recognition phrase visible in any pose"},
  "pruef": {"FIG-…": [ {"id": "F-…", "art": "muss", "stufe": "pflicht", "de": "…", "en": "…?"} ]},
  "neue_figuren": {"FIG-…": {"de": "Name", "en": "Name", "gsw": "Name", "kind": "person|group|object|place", "era": "ot|nt",
                    "identity_de": "wer (mit [[…]]-Marke)", "traits_de": ["Merkmal 1", "Merkmal 2"], "legend_de": "kurz", "legend_gsw": "kurz"}},
  "stationen": [
    {"id": "GEN-B1", "reference": "GEN.1.1-GEN.2.3", "action_de": "was der Text hier sagt (1–2 Sätze)",
     "band": {"de": "Titel, höchstens 46 Zeichen", "gsw": "Titel auf Züridüütsch"},
     "form": "szene", "form_grund_de": "warum diese Form",
     "bild_en": "Malauftrag Englisch …", "depicts": ["FIG-…"],
     "evidence": [{"s": "B", "ref": "GEN.1.3", "de": "…"}, {"s": "R", "de": "…"}, {"s": "I", "de": "…"}],
     "pruefung": [{"id": "B1-…", "art": "muss|nicht", "stufe": "pflicht|soll", "s": "B|R|I", "ref": "GEN.1.3", "de": "…", "en": "…?"}]},
    {"id": "GEN-B2", "reference": "…", "action_de": "…", "band": {…}, "form": "struktur", "form_grund_de": "…",
     "struktur": {"typ": "spalten|kette|raster|kurve|spiegel|reihe|ebenen|ringe",
                  "titel": {"de": "…", "gsw": "…"},
                  "kopf": {"a": {"de": "…", "gsw": "…"}, "b": {"de": "…", "gsw": "…"}},
                  "mitte": {"de": "…", "gsw": "…", "ref": "…"},
                  "elemente": [{"de": "…", "gsw": "…", "ref": "GEN.1.3", "seite": "a|b", "richtung": "ab|auf", "betont": true, "gestrichen": true}]},
     "evidence": [{"s": "B", "ref": "…", "de": "…"}]}
  ]
}
"""

TYPEN = {  # Anzahl Elemente (min, max) und erlaubte Zusatzfelder
    "spalten": (4, 12), "kette": (3, 5), "raster": (3, 12), "kurve": (4, 8), "spiegel": (2, 4), "reihe": (3, 7), "ebenen": (2, 6), "ringe": (2, 6),
}
LABEL_MAX = 40
BAND_MAX = 46


def lade(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))


def nav():
    d = lade(ROOT / "data/navigation/NAV-PROT66-KJV.json")
    return {b["code"]: b for b in d["books"]}


NAV = nav()


def stelle_ok(ref, buch):
    """Stelle im Format BUCH.K.V oder BUCH.K.V-BUCH.K.V (Navigationszählung), innerhalb des Buchs."""
    if not isinstance(ref, str):
        return False
    teile = ref.split("-")
    if len(teile) > 2:
        return False
    for t in teile:
        m = re.fullmatch(r"([1-3A-Z]{3})\.(\d+)(?:\.(\d+))?", t)
        if not m or m.group(1) != buch:
            return False
        k = int(m.group(2))
        vpc = NAV[buch]["verses_per_chapter"]
        if not 1 <= k <= len(vpc):
            return False
        if m.group(3) and not 1 <= int(m.group(3)) <= vpc[k - 1]:
            return False
    return True


def lexikon_ids():
    return {p.stem for p in LEX.glob("FIG-*.json")}


def pruefe(d, buch):
    f = []
    lex = lexikon_ids() | set(d.get("neue_figuren", {}))
    if d.get("buch") != buch:
        f.append("buch passt nicht zum Dateinamen")
    for k in ("zweck_de", "note_de", "quelle_de", "stationen"):
        if not d.get(k):
            f.append(f"{k} fehlt")
    brief_p = BRIEFS / f"BRIEF-{buch}.json"
    brief = lade(brief_p) if brief_p.exists() else None
    st = d.get("stationen") or []
    if not 3 <= len(st) <= 6:
        f.append(f"{len(st)} Stationen, erlaubt 3–6")
    if brief and len(brief["panels"]) != len(st):
        f.append(f"Bildauftrag BRIEF-{buch} hat {len(brief['panels'])} Felder, das Gerüst {len(st)}: dem Bildauftrag folgen")
    ids = set()
    for i, s in enumerate(st, 1):
        sid = s.get("id", f"#{i}")
        if sid != f"{buch}-B{i}":
            f.append(f"{sid}: id muss {buch}-B{i} heissen")
        ids.add(sid)
        if not stelle_ok(s.get("reference"), buch):
            f.append(f"{sid}: reference {s.get('reference')!r} ungültig")
        if brief and brief["panels"][i - 1]["reference"] != s.get("reference"):
            f.append(f"{sid}: reference muss {brief['panels'][i - 1]['reference']} sein (Bildauftrag)")
        if not s.get("action_de"):
            f.append(f"{sid}: action_de fehlt")
        b = s.get("band") or {}
        if not brief:
            for lg in ("de", "gsw"):
                if not b.get(lg) or len(b[lg]) > BAND_MAX:
                    f.append(f"{sid}: band.{lg} fehlt oder länger als {BAND_MAX}")
        for e in s.get("evidence") or []:
            if e.get("s") not in ("B", "R", "I") or not e.get("de") or (e["s"] == "B" and not stelle_ok(e.get("ref"), buch)):
                f.append(f"{sid}: Beleg ungültig {e}")
        if not any(e.get("s") == "B" for e in s.get("evidence") or []):
            f.append(f"{sid}: mindestens ein B-Beleg nötig")
        form = s.get("form")
        if not s.get("form_grund_de"):
            f.append(f"{sid}: form_grund_de fehlt")
        if form == "szene":
            if not s.get("bild_en") or len(s["bild_en"]) < 200:
                f.append(f"{sid}: bild_en fehlt oder zu kurz")
            if "FIG-GOTT" in (s.get("depicts") or []):
                f.append(f"{sid}: Gott wird nicht gemalt (FIG-GOTT nicht in depicts)")
            for x in s.get("depicts") or []:
                if x not in lex:
                    f.append(f"{sid}: {x} nicht im Bildlexikon (in neue_figuren beschreiben)")
                if x not in (d.get("figuren") or {}) and x not in lade(DATEN / "figuren.json")["figuren"]:
                    f.append(f"{sid}: {x} ohne Malbeschreibung in figuren")
            pr = s.get("pruefung") or []
            if not any(r.get("stufe") == "pflicht" for r in pr):
                f.append(f"{sid}: mindestens eine Pflichtregel nötig")
            for r in pr:
                if not all(r.get(k) for k in ("id", "art", "stufe", "de", "en")) or r["art"] not in ("muss", "nicht") or r["stufe"] not in ("pflicht", "soll"):
                    f.append(f"{sid}: Regel ungültig {r.get('id')}")
                if r.get("ref") and not stelle_ok(r["ref"], buch):
                    f.append(f"{sid}: Regel {r.get('id')} ref ungültig")
        elif form == "struktur":
            sx = s.get("struktur") or {}
            typ = sx.get("typ")
            if typ not in TYPEN:
                f.append(f"{sid}: struktur.typ {typ!r} unbekannt")
                continue
            el = sx.get("elemente") or []
            lo, hi = TYPEN[typ]
            if not lo <= len(el) <= hi:
                f.append(f"{sid}: {typ} braucht {lo}–{hi} Elemente, hat {len(el)}")
            for j, e in enumerate(el + [x for x in (sx.get("mitte"), sx.get("titel")) if x] + list((sx.get("kopf") or {}).values())):
                for lg in ("de", "gsw"):
                    if not e.get(lg) or len(e[lg]) > LABEL_MAX:
                        f.append(f"{sid}: Beschriftung {e.get('de')!r} ({lg}) fehlt oder länger als {LABEL_MAX}")
                if e.get("ref") and not stelle_ok(e["ref"], buch):
                    f.append(f"{sid}: Element-Stelle {e['ref']!r} ungültig")
            if typ in ("spalten", "spiegel", "ebenen"):
                if {e.get("seite") for e in el} != {"a", "b"}:
                    f.append(f"{sid}: {typ}: jedes Element braucht seite a oder b, beide Seiten belegt")
                if not sx.get("kopf"):
                    f.append(f"{sid}: {typ}: kopf a und b nötig")
            if typ == "kurve" and not all(e.get("richtung") in ("ab", "auf") for e in el):
                f.append(f"{sid}: kurve: jedes Element braucht richtung ab oder auf")
            if typ == "ringe" and not sx.get("mitte"):
                f.append(f"{sid}: ringe: mitte nötig")
        else:
            f.append(f"{sid}: form muss szene oder struktur sein")
    for fid, nf in (d.get("neue_figuren") or {}).items():
        if fid in lexikon_ids():
            f.append(f"neue_figuren: {fid} gibt es schon")
        if not re.fullmatch(r"FIG-[A-Z0-9-]+", fid):
            f.append(f"neue_figuren: Kennung {fid} ungültig")
        for k in ("de", "en", "gsw", "kind", "era", "identity_de", "traits_de", "legend_de", "legend_gsw"):
            if not nf.get(k):
                f.append(f"neue_figuren {fid}: {k} fehlt")
    return f


def schreibe(buch, d):
    code = buch.lower()
    brief_p = BRIEFS / f"BRIEF-{buch}.json"
    st = d["stationen"]
    hat_brief = brief_p.exists()
    trans = sorted(p.stem for p in (ROOT / "data/translations").glob(f"TRANS-{buch}-*-WORKING.json"))
    tag = next((p.stem for p in (ROOT / "data/tags").glob("TAG-*.json") if lade(p).get("book") == buch), None)
    szenen = {}
    for i, s in enumerate(st, 1):
        sz = {"brief": f"BRIEF-{buch}", "panel": i, "reference": s["reference"], "form": s["form"], "form_grund_de": s["form_grund_de"],
              "depicts": s.get("depicts", []) if s["form"] == "szene" else [], "bild_en": s.get("bild_en", ""), "speech": [],
              "evidence": s["evidence"], "pruefung": s.get("pruefung", [])}
        if s["form"] == "struktur":
            sz["struktur"] = s["struktur"]
        if not hat_brief:
            sz["band"] = s["band"]
        szenen[s["id"]] = sz
    plan = {"_hinweis": f"Buchgerüst {buch} (scripts/authoring/buchgeruest.py aus buch/{buch}.json). Form je Station: «szene» wird gemalt und "
                        "automatisch geprüft, «struktur» zeichnet das Werkzeug aus den Elementen. " + ("Vorläufig von oben; Band ist ein Titel in eigenen Worten."
                                                                                                         if not trans else "Band aus dem Bildauftrag (Wortlaut der Arbeitsübersetzung)."),
            "basis": trans if hat_brief else [], "tags": [tag] if tag else [], "figurenblatt": None, "stand": d.get("stand") or HEUTE,
            "figuren": d.get("figuren", {}), "kenn_en": d.get("kenn_en", {}), "pruef": d.get("pruef", {}),
            "bilder": [{"id": f"ILL-AQU-{buch}", "brief": f"BRIEF-{buch}", "level": "book", "reference": buch, "target": f"SUM-BOOK-{buch}",
                        "felder": [s["id"] for s in st], "note_de": d["note_de"]}],
            "szenen": szenen}
    (DATEN / f"szenen-buch-{code}.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not hat_brief:
        sys.path.insert(0, str(ROOT / "scripts"))
        import localizations
        summ = lade(ROOT / f"data/summaries/SUM-BOOK-{buch}.json")
        brief = {"id": f"BRIEF-{buch}", "type": "illustration_brief", "status": "draft", "tags": [tag] if tag else [], "level": "book", "reference": buch,
                 "target": f"SUM-BOOK-{buch}",
                 "panels": [{"n": i, "reference": s["reference"], "figures": [], "objects": [], "signs": [], "speech": [], "action_de": s["action_de"],
                             "keywords": s["band"], "form": s["form"]} for i, s in enumerate(st, 1)],
                 "actions_de": [s["action_de"] for s in st], "captions_de": [s["band"]["de"] for s in st],
                 "interpretation_note_de": d["note_de"], "purpose_de": d["zweck_de"], "source_de": d["quelle_de"],
                 "basis": [{"record": f"SUM-BOOK-{buch}", "field": "summary", "fingerprint": localizations.fingerprint(summ.get("summary_de") or summ.get("text_de"))}],
                 "basis_note_de": "Fingerabdruck der Zusammenfassung des Buchs, gegen die der Auftrag geprüft wurde. Vorläufig von oben (Buchgerüst): "
                                  "Stationen aus Strukturkatalog und Zusammenfassung, noch ohne Abschnittsanalysen und ohne Arbeitsübersetzung.",
                 "authorship_de": AUTOR.format(d=HEUTE), "knowledge": {"asserted_at": HEUTE, "supersedes": None}}
        brief_p.write_text(json.dumps(brief, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for fid, nf in (d.get("neue_figuren") or {}).items():
        p = LEX / f"{fid}.json"
        if p.exists():
            continue
        rec = {"id": fid, "type": "figure", "status": "draft", "tags": [tag] if tag else [], "kind": nf["kind"],
               "names": {"de": nf["de"], "en": nf["en"]}, "identity_de": nf["identity_de"], "era": nf["era"],
               "display_group": {"person": "people", "group": "groups", "object": "objects", "place": "places"}.get(nf["kind"], "people"),
               "traits": [{"trait_de": t, "basis": "design"} for t in nf["traits_de"]],
               "legend": {"de": nf["legend_de"], "gsw": nf["legend_gsw"]},
               "rules_de": ["Erkennbar an Farbe, Kleidung und Zeichen; Menschen des antiken Vorderen Orients, keine Karikatur"],
               "authorship_de": AUTOR.format(d=HEUTE), "knowledge": {"asserted_at": HEUTE, "supersedes": None}}
        p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("pruefen", "schreiben"):
        print(__doc__ + "\nFormat:" + FORMAT)
        sys.exit(1)
    buecher = [b.upper() for b in sys.argv[2:]] or sorted(p.stem for p in QUELLE.glob("*.json"))
    alle_ok = True
    for b in buecher:
        p = QUELLE / f"{b}.json"
        if not p.exists():
            print(f"{b}: keine Datei {p.relative_to(ROOT)}")
            alle_ok = False
            continue
        try:
            d = lade(p)
        except json.JSONDecodeError as ex:
            print(f"{b}: JSON-Fehler {ex}")
            alle_ok = False
            continue
        f = pruefe(d, b)
        if f:
            alle_ok = False
            print(f"{b}: {len(f)} Fehler\n  " + "\n  ".join(f))
            continue
        n_sz = sum(s["form"] == "szene" for s in d["stationen"])
        print(f"{b}: in Ordnung ({len(d['stationen'])} Stationen, {n_sz} Szenen)")
        if sys.argv[1] == "schreiben":
            schreibe(b, d)
    sys.exit(0 if alle_ok else 1)


if __name__ == "__main__":
    main()
