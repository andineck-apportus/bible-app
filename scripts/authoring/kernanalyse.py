#!/usr/bin/env python3
"""Autorenwerkzeug: Kernanalysen (Typ core_analysis) – gemeinsame Grundlage für Zusammenfassung und Bild.

Ablauf und Regeln: docs/VERDICHTUNG.md. Eingabe: scripts/authoring/kernanalysen_daten/<BUCH>.json (Liste von Einheiten),
Ausgabe: data/core-analyses/CORE-<suffix>.json.

Eine Einheit:
    {"suffix": "RUT-001-006-018", "level": "section|chapter|book", "target": "TU-…|SUM-CH-…|SUM-BOOK-…",
     "reference": "RUT.1.6-RUT.1.18" (bei book: "RUT"), "children": ["RUT-001-001-005", …] (chapter/book),
     "core_de": "…", "gist_de": "Kernaussage in einem Satz (optional; «Vertiefen › Verstehen»)", "purpose_de": "…" (book), "mode": "narrative|speech|parable|instruction|statement|list|prayer",
     "voice": {"speaker": "FIG-…|narrator", "addressee": "FIG-…"} ,
     "moments": [{"reference": "RUT.1.16-RUT.1.17", "text_de": "…", "reason_de": "…", "recognition_de": "…",
                  "keywords": ["Wo du hingehst"], "mode": "…" (optional, sonst der Einheit)}],
     "omitted_de": ["… (Grund)"], "persons": ["FIG-…"], "places": ["FIG-ORT-…"],
     "structure": {"root": "s1", "units": [{"id": "s1", "pattern": "series", "subtype": "…" (frei, optional),
                   "form_type": "lament" (nur bei pattern form), "range": "MAT.5.3-MAT.5.12",
                   "elements": [{"label": "Arme im Geist → Himmelreich", "ref": "MAT.5.3", "role": "…", "links": ["…"],
                                 "child": "s2", "row": "…", "col": "…", "empty": true}],
                   "features": {"speakers": [{"who": "FIG-JESUS", "to": "FIG-GRUPPE-JUENGER"}],
                                "modality": [{"kind": "Zusage", "ref": "MAT.5.4", "note": "…"}]}, "visual": "grid",
                   "basis": "text|proposal", "source_de": "… (Pflicht bei proposal)"}]}}
Strukturanalyse nach docs/STRUKTURKATALOG.md («Struktur zuerst»): Baumuster, Glieder, Merkmale und Darstellung aus den Listen
dort. Eine Reihe, ein Raster oder ein Gegensatz zählt als ein Moment; seine Glieder stehen vollständig in `structure`.

Prüft: Umfang je Ebene, Stellen innerhalb der Einheit, Schlüsselwörter wörtlich in der hochdeutschen Arbeitsübersetzung,
Personen/Orte im Bildlexikon, Kinder vorhanden und Momente höherer Ebenen aus den Momenten der Kinder («oben nichts, was
unten fehlt»). Schreibt Fingerabdrücke (`basis`): Abschnitt = Verse der Arbeitsübersetzung, höhere Ebene = Kernanalysen der
Kinder. Bestehende Fingerabdrücke werden nur mit BIBLE_CORE_CONFIRM=1 erneuert (wie bei den Bildaufträgen).

    python3 scripts/authoring/kernanalyse.py [--check] [BUCH …]

--check: nur prüfen, nichts schreiben. BIBLE_CORE_SRC=<Ordner>: Eingabe aus einem anderen Ordner (Entwürfe).
"""
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
D = ROOT / "data"
sys.path.insert(0, str(ROOT / "scripts"))
import localizations  # noqa: E402

SRC = pathlib.Path(os.environ.get("BIBLE_CORE_SRC") or ROOT / "scripts/authoring/kernanalysen_daten")
OUT = D / "core-analyses"
MODES = {"narrative", "speech", "parable", "instruction", "statement", "list", "prayer"}
BUDGET = {"section": (1, 3), "chapter": (1, 4), "book": (4, 6), "group": (4, 6), "testament": (4, 6), "bible": (4, 6)}
PATTERNS = {"sequence", "cycle", "curve", "fulfilment", "interleave", "series", "numbered", "matrix", "register", "tree",
            "climax", "contrast", "balance", "reversal", "parallel", "frame", "condition", "cause", "argument", "objection",
            "dialogue", "form", "poem", "parable", "sign_act", "typology", "space", "route", "territory", "outward", "vision",
            "realms", "collection"}
FORM_TYPES = {"lament", "hymn", "thanksgiving", "liturgy", "lawsuit", "woe", "call", "annunciation", "theophany", "treaty",
              "regnal", "case_ruling", "letter", "household", "testament"}
FEATURES = {"speakers", "stance", "authority", "genre", "leitwort", "pattern_break", "open_end", "modality", "wordplay",
            "text_forms", "interpretation", "crossref", "chronology", "numbers", "weight"}
FEATURE_KEYS = {"ref", "refs", "note", "word", "role", "who", "to", "kind"}  # Merkmal: Liste solcher Objekte
VISUALS = {"scenes", "timeline", "lanes", "grid", "columns", "mirror", "switch", "arrows", "tree", "rings", "circle", "stairs",
           "map", "model", "figure", "levels", "dialogue", "balance", "outline", "network"}
CHILDREN = {}
LEX = {p.stem for p in (D / "illustrations/lexicon").glob("FIG-*.json")}


def _de_text():
    """Alle Verse der hochdeutschen Arbeitsübersetzungen: {ref: text}."""
    out = {}
    for p in sorted((D / "translations").glob("TRANS-*-DE-WORKING.json")):
        t = json.loads(p.read_text(encoding="utf-8")).get("text_by_reference", {})
        for k, v in t.items():
            out.setdefault(k, v)
    return out


DE = _de_text()


def verses(ref):
    """Verse eines Bereichs innerhalb eines Kapitels oder über Kapitelgrenzen eines Buches (in Reihenfolge von DE)."""
    a, _, b = ref.partition("-")
    pa = a.split(".")
    if len(pa) == 1:  # ganzes Buch
        return [k for k in DE if k.split(".")[0] == pa[0]]
    pb = (b or a).split(".")
    bk, c1 = pa[0], int(pa[1])
    v1 = int(pa[2]) if len(pa) > 2 else 1
    c2 = int(pb[1])
    v2 = int(pb[2]) if len(pb) > 2 else 999
    out = []
    for k in DE:
        kb, kc, kv = k.split(".")
        kc, kv = int(kc), int(kv)
        if kb == bk and (c1, v1) <= (kc, kv) <= (c2, v2):
            out.append(k)
    return sorted(out, key=lambda k: tuple(int(x) for x in k.split(".")[1:]))


def norm(s):
    return re.sub(r"[^\w]+", " ", s.lower()).strip()


def check_unit(u, units, errs):
    sid = u["suffix"]
    lv = u["level"]
    if lv not in BUDGET:
        errs.append(f"{sid}: unbekannte Ebene {lv}")
        return
    lo, hi = BUDGET[lv]
    if not lo <= len(u["moments"]) <= hi:
        errs.append(f"{sid}: {len(u['moments'])} Momente, erlaubt {lo}–{hi} für {lv}")
    for k in ("core_de", "mode", "moments", "omitted_de"):
        if not u.get(k):
            errs.append(f"{sid}: Feld {k} fehlt")
    if lv == "book" and not u.get("purpose_de"):
        errs.append(f"{sid}: purpose_de fehlt (Buch)")
    if u.get("mode") not in MODES:
        errs.append(f"{sid}: mode {u.get('mode')} unbekannt")
    unit_vs = set(verses(u["reference"]))
    if not unit_vs:
        errs.append(f"{sid}: keine Verse der Arbeitsübersetzung für {u['reference']}")
    for x in u.get("persons", []) + u.get("places", []) + [v for v in (u.get("voice") or {}).values() if v and v.startswith("FIG-")]:
        if x not in LEX:
            errs.append(f"{sid}: {x} nicht im Bildlexikon")
    child_moments = []
    for c in u.get("children", []):
        if c not in units:
            errs.append(f"{sid}: Kind {c} fehlt")
        else:
            child_moments += [set(verses(m["reference"])) for m in units[c]["moments"]]
    for i, m in enumerate(u["moments"], 1):
        mv = set(verses(m["reference"]))
        if not mv or not mv <= unit_vs:
            errs.append(f"{sid}: Moment {i} {m['reference']} liegt nicht in der Einheit")
        if m.get("mode") and m["mode"] not in MODES:
            errs.append(f"{sid}: Moment {i} mode {m['mode']} unbekannt")
        for k in ("text_de", "reason_de", "recognition_de", "keywords"):
            if not m.get(k):
                errs.append(f"{sid}: Moment {i} Feld {k} fehlt")
        txt = norm(" ".join(DE.get(v, "") for v in sorted(mv)))
        for kw in m.get("keywords", []):
            if norm(kw) not in txt:
                errs.append(f"{sid}: Moment {i} Schlüsselwort «{kw}» steht nicht so in {m['reference']}")
        if u.get("children") and not any(mv & cm for cm in child_moments):
            errs.append(f"{sid}: Moment {i} {m['reference']} kommt in keinem Moment der Ebene darunter vor")


def check_structure(u, errs):
    """Strukturanalyse (docs/STRUKTURKATALOG.md): Listen, Glieder innerhalb der Einheit, Verschachtelung, Deutung gekennzeichnet."""
    sid, st = u["suffix"], u.get("structure")
    if not st:
        errs.append(f"{sid}: structure fehlt (Struktur zuerst)")
        return
    units = {x.get("id"): x for x in st.get("units", [])}
    if not units or st.get("root") not in units:
        errs.append(f"{sid}: structure.root fehlt oder zeigt auf keine Einheit")
    unit_vs = set(verses(u["reference"]))
    used = set()
    for x in st.get("units", []):
        xid = f"{sid}/{x.get('id')}"
        if x.get("pattern") not in PATTERNS:
            errs.append(f"{xid}: Baumuster {x.get('pattern')} nicht im Katalog")
        if (x.get("pattern") == "form") != bool(x.get("form_type")):
            errs.append(f"{xid}: form_type genau bei Baumuster form angeben")
        if x.get("form_type") and x["form_type"] not in FORM_TYPES:
            errs.append(f"{xid}: form_type {x['form_type']} unbekannt")
        if x.get("visual") not in VISUALS:
            errs.append(f"{xid}: Darstellung {x.get('visual')} nicht im Katalog")
        if x.get("basis", "text") not in ("text", "proposal"):
            errs.append(f"{xid}: basis muss text oder proposal sein")
        if x.get("basis") == "proposal" and not x.get("source_de"):
            errs.append(f"{xid}: Forschungsvorschlag ohne source_de")
        for k, v in (x.get("features") or {}).items():
            if k not in FEATURES:
                errs.append(f"{xid}: Merkmal {k} nicht im Katalog")
            if not isinstance(v, list) or not all(isinstance(i, dict) and i and set(i) <= FEATURE_KEYS for i in v):
                errs.append(f"{xid}: Merkmal {k}: Liste von Objekten mit Schlüsseln aus {sorted(FEATURE_KEYS)} verlangt")
            for i in v if isinstance(v, list) else []:
                for r in ([i["ref"]] if isinstance(i, dict) and i.get("ref") else []) + (i.get("refs") or [] if isinstance(i, dict) else []):
                    if k not in ("crossref", "leitwort") and not set(verses(r)) <= unit_vs:
                        errs.append(f"{xid}: Merkmal {k}: Stelle {r} liegt nicht in der Einheit")
        rv = set(verses(x["range"])) if x.get("range") else unit_vs
        if not rv or not rv <= unit_vs:
            errs.append(f"{xid}: range {x.get('range')} liegt nicht in der Einheit")
        els = x.get("elements") or []
        if len(els) < 2 and x.get("pattern") not in ("space", "figure"):
            errs.append(f"{xid}: weniger als 2 Glieder")
        for i, e in enumerate(els, 1):
            if not e.get("label"):
                errs.append(f"{xid}: Glied {i} ohne label")
            if e.get("ref"):
                ev = set(verses(e["ref"]))
                if not ev or not ev <= unit_vs:
                    errs.append(f"{xid}: Glied {i} {e['ref']} liegt nicht in der Einheit")
            if e.get("child"):
                if e["child"] not in units:
                    errs.append(f"{xid}: Glied {i} child {e['child']} fehlt")
                used.add(e["child"])
            elif not e.get("ref") and not e.get("empty"):
                errs.append(f"{xid}: Glied {i} ohne ref (oder empty/child)")
    for k in units:
        if k != st.get("root") and k not in used:
            errs.append(f"{sid}/{k}: Struktureinheit hängt nirgends (child)")
    if u["level"] == "chapter" and CHILDREN.get(sid):
        # Kapitel: die Kernaussage jedes Abschnitts ist enthalten (Hinweis Andi Neck 2026-10-24) – jeder Abschnitt
        # kommt in der Struktur vor (ein Glied, dessen Stelle in ihm liegt)
        covered = set()
        for x in st.get("units", []):
            for e in x.get("elements") or []:
                if e.get("ref"):
                    covered |= set(verses(e["ref"]))
        for c, cref in CHILDREN[sid]:
            if not set(verses(cref)) & covered:
                errs.append(f"{sid}: Abschnitt {c} ({cref}) fehlt in der Struktur des Kapitels (Kernaussage jedes Abschnitts)")


def run(books):
    files = sorted(SRC.glob("*.json"))
    units = {}
    for f in files:
        for u in json.loads(f.read_text(encoding="utf-8")):
            units[u["suffix"]] = u
    sel = [u for u in units.values() if not books or u["suffix"].split("-")[0] in books]
    errs = []
    CHILDREN.clear()
    CHILDREN.update({sid: [(c, units[c]["reference"]) for c in u.get("children", []) if c in units]
                     for sid, u in units.items() if u["level"] == "chapter"})
    for u in sel:
        check_unit(u, units, errs)
        if u.get("structure") or os.environ.get("BIBLE_STRUCTURE_REQUIRED", "1") == "1":
            check_structure(u, errs)
    if errs:
        print("\n".join("FEHLER: " + e for e in errs))
        sys.exit(1)
    if CHECK_ONLY:
        print(f"PASS: {len(sel)} Kernanalysen geprüft (nur Prüfung)")
        return
    confirm = os.environ.get("BIBLE_CORE_CONFIRM") == "1"
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    order = {"section": 0, "chapter": 1, "book": 2, "group": 3, "testament": 4, "bible": 5}
    for u in sorted(sel, key=lambda x: order[x["level"]]):
        rid = f"CORE-{u['suffix']}"
        if u["level"] == "section":
            basis = [{"field": "text_de", "reference": u["reference"],
                      "fingerprint": localizations.fingerprint(" ".join(DE[v] for v in verses(u["reference"])))}]
        else:
            basis = []
            for c in u["children"]:
                cp = OUT / f"CORE-{c}.json"
                core = json.loads(cp.read_text(encoding="utf-8")) if cp.exists() else units[c]
                basis.append({"record": f"CORE-{c}", "fingerprint": localizations.fingerprint(
                    json.dumps({k: core.get(k) for k in ("core_de", "moments", "structure") if k != "structure" or core.get(k)}, ensure_ascii=False, sort_keys=True))})
        path = OUT / f"{rid}.json"
        if path.exists() and not confirm:
            old = {(x.get("record"), x.get("reference")): x["fingerprint"] for x in json.loads(path.read_text(encoding="utf-8")).get("basis", [])}
            for x in basis:
                x["fingerprint"] = old.get((x.get("record"), x.get("reference")), x["fingerprint"])
        rec = {"id": rid, "type": "core_analysis", "status": "draft", "tags": u.get("tags", []), "level": u["level"],
               "reference": u["reference"], "target": u["target"],
               **({"children": [f"CORE-{c}" for c in u["children"]]} if u.get("children") else {}),
               "core_de": u["core_de"], **({"gist_de": u["gist_de"]} if u.get("gist_de") else {}),
               **({"purpose_de": u["purpose_de"]} if u.get("purpose_de") else {}),
               "mode": u["mode"], **({"voice": u["voice"]} if u.get("voice") else {}),
               **({"structure": u["structure"]} if u.get("structure") else {}),
               "moments": u["moments"], "omitted_de": u["omitted_de"],
               "persons": u.get("persons", []), "places": u.get("places", []),
               "basis": basis,
               "authorship_de": u.get("authorship_de", "KI-Entwurf (Claude) vom 2026-10-23 nach docs/VERDICHTUNG.md; keine fachliche Prüfung."),
               "knowledge": {"asserted_at": u.get("date", "2026-10-23"), "supersedes": None}}
        if u.get("review"):
            rec["review"] = u["review"]
        txt = json.dumps(rec, ensure_ascii=False, indent=1) + "\n"
        if not path.exists() or path.read_text(encoding="utf-8") != txt:
            path.write_text(txt, encoding="utf-8")
            n += 1
    print(f"PASS: {len(sel)} Kernanalysen geprüft; {n} Dateien geschrieben" + (" (Grundlage bestätigt)" if confirm else ""))


CHECK_ONLY = "--check" in sys.argv

if __name__ == "__main__":
    run([a for a in sys.argv[1:] if a != "--check"])
