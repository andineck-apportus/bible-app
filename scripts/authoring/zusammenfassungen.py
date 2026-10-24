#!/usr/bin/env python3
"""Zusammenfassungen aus der Kernanalyse (docs/VERDICHTUNG.md, Ablauf Schritt 3) – Hochdeutsch und Züridüütsch.

Eingabe: scripts/authoring/zusammenfassungen_daten/<BUCH>.json, eine Liste von
    {"core": "CORE-RUT-001-006-018", "ids": ["TU-RUT-001-006-018"], "de": "…", "gsw": "…"}
`ids`: die Datensätze, deren Zusammenfassung so lautet – Texteinheit (Feld summary_de) oder Zusammenfassung (text_de).
Beim Kapitel z. B. ["SUM-CH-RUT-001", "TU-RUT-001-001-022"], damit Kapitel-Zusammenfassung und kapitelweite Texteinheit
gleich lauten.

Prüft:
- Kernanalyse vorhanden;
- Umfang je Ebene (Abschnitt 2–4, Kapitel 3–5, Buch 4–6 Sätze; Mundart gleich viele Sätze ±1); strukturierte Zusammenfassung:
  Zeilen mit «– » sind eine Liste aller Glieder (zählt als ein Satz, beliebig viele Punkte, Mundart gleich viele);
- kein «ß»;
- keine Stellen-Marken (Zusammenfassungen werden als reiner Text gezeigt);
- die Momente der Kernanalyse kommen vor: je Moment mindestens ein Schlüsselwort oder ein Wort aus dem Momentsatz
  (Hinweis, kein Fehler).

Schreibt die Felder in die Datensätze, die frühere Fassung ins revision_log, `core_basis` (Kernanalyse und Fingerabdruck)
und die Mundart in die Lokalisierung (L10N-GSW-ZH-…) samt Fingerabdruck. Die Autorenwerkzeuge der Bücher übernehmen
dieselben Texte über scripts/authoring/_lib.py (summary_override), damit ein erneuter Lauf sie nicht zurücksetzt.

    python3 scripts/authoring/zusammenfassungen.py [BUCH …]
"""
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
D = ROOT / "data"
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts/authoring"))
import localizations  # noqa: E402
from _lib import SUMMARY_SRC, load_summary_overrides  # noqa: E402

LANG = "gsw-u-sd-chzh"
BUDGET = {"section": (2, 4), "chapter": (3, 5), "book": (4, 6)}
DATE = os.environ.get("BIBLE_REVISION_DATE", "2026-10-23")
AUTH = "KI-Entwurf (Claude) vom {d} aus der Kernanalyse {c} (docs/VERDICHTUNG.md); von einer getrennten KI-Instanz gegen Text und Kernanalyse geprüft; keine fachliche Prüfung."
AUTH_GSW = "KI-Entwurf (Claude) vom {d}; Mundartfassung der neuen Zusammenfassung; Mundart noch nicht muttersprachlich geprüft."


def sentences(t):
    t = re.sub(r"\b(z|u|v|d|s|bzw|vgl|ca|usw|Kap|Mt|Mk|Lk|Joh)\.(?=\s)", r"\1", t)  # Abkürzungen
    return [s for s in re.split(r"(?:(?<=[.!?])|(?<=[.!?][»“\"']))\s+(?=[«„A-ZÄÖÜ0-9])", t.strip()) if s]


def shape(t):
    """(Sätze ausserhalb der Liste, Listenpunkte). Listenpunkte: Zeilen, die mit «– » beginnen."""
    lines = [x.strip() for x in t.split("\n") if x.strip()]
    items = [x for x in lines if re.match(r"^[–-]\s+", x)]
    rest = " ".join(x for x in lines if x not in items)
    return len(sentences(rest)) if rest else 0, len(items)


def find(rid):
    hits = [p for p in D.rglob(f"{rid}.json") if "localizations" not in p.parts]
    if len(hits) != 1:
        raise SystemExit(f"ERROR: {rid}: {len(hits)} Dateien gefunden")
    return hits[0]


def core_fp(core):
    return localizations.fingerprint(json.dumps({k: core.get(k) for k in ("core_de", "moments", "structure") if k != "structure" or core.get(k)}, ensure_ascii=False, sort_keys=True))


def check(e, errs, warns):
    cp = D / "core-analyses" / f"{e['core']}.json"
    if not cp.exists():
        errs.append(f"{e['core']}: Kernanalyse fehlt")
        return None
    core = json.loads(cp.read_text(encoding="utf-8"))
    lo, hi = BUDGET[core["level"]]
    (n_de, l_de), (n_gsw, l_gsw) = shape(e["de"]), shape(e["gsw"])
    if l_de:  # strukturierte Zusammenfassung: Liste zählt als ein Satz, enthält alle Glieder (VERDICHTUNG.md, Regel 6)
        if l_de < 2:
            errs.append(f"{e['core']}: Liste mit nur {l_de} Punkt")
        if not 1 <= n_de + 1 <= hi:
            errs.append(f"{e['core']}: {n_de} Sätze neben der Liste, erlaubt höchstens {hi - 1} ({core['level']})")
        if l_gsw != l_de:
            errs.append(f"{e['core']}: Mundart hat {l_gsw} Listenpunkte, Hochdeutsch {l_de}")
        glieder = sum(len(x.get("elements", [])) for x in (core.get("structure") or {}).get("units", []))
        if glieder and l_de > glieder:
            warns.append(f"{e['core']}: mehr Listenpunkte ({l_de}) als Glieder in der Struktur ({glieder})")
    elif not lo <= n_de <= hi:
        errs.append(f"{e['core']}: {n_de} Sätze, erlaubt {lo}–{hi} ({core['level']})")
    if abs(n_de - n_gsw) > 1:
        errs.append(f"{e['core']}: Mundart hat {n_gsw} Sätze, Hochdeutsch {n_de}")
    for k in ("de", "gsw"):
        if "ß" in e[k]:
            errs.append(f"{e['core']}: «ß» in {k}")
        if "[[" in e[k]:
            errs.append(f"{e['core']}: Stellen-Marke in {k} (reiner Text verlangt)")
    low = e["de"].lower()
    for i, m in enumerate(core["moments"], 1):
        words = [w.lower() for w in m.get("keywords", [])] + [w.lower() for w in re.findall(r"\w{6,}", m["text_de"])]
        if not any(w in low for w in words):
            warns.append(f"{e['core']}: Moment {i} ({m['reference']}) in der Zusammenfassung nicht erkennbar")
    return core


def run(books):
    ov = load_summary_overrides()
    sel = {rid: e for rid, e in ov.items() if not books or e["core"].split("-")[1] in books}
    errs, warns = [], []
    cores = {}
    for e in {id(v): v for v in sel.values()}.values():
        cores[e["core"]] = check(e, errs, warns)
    for w in warns:
        print("HINWEIS:", w)
    if errs:
        print("\n".join("FEHLER: " + x for x in errs))
        sys.exit(1)
    if "--check" in sys.argv:
        print(f"PASS: {len(cores)} Zusammenfassungen geprüft (nur Prüfung)")
        return
    n = 0
    for rid, e in sel.items():
        core = cores[e["core"]]
        path = find(rid)
        rec = json.loads(path.read_text(encoding="utf-8"))
        field = "summary_de" if rec["type"] == "text_unit" else "text_de"
        auth_field = "summary_authorship_de" if rec["type"] == "text_unit" else "authorship_de"
        basis = {"core": e["core"], "fingerprint": core_fp(core)}
        if rec.get(field) != e["de"] or rec.get("core_basis") != basis:
            if rec.get(field) != e["de"]:
                log = rec.setdefault("revision_log", [])
                entry = {"date": DATE, "change_de": f"Neu aus der Kernanalyse {e['core']} (docs/VERDICHTUNG.md)", "previous": {field: rec.get(field)}}
                # Nachbesserungen am selben Tag aus demselben Werkzeug: ein Eintrag, die Fassung davor bleibt «previous»
                if not (log and log[-1].get("date") == DATE and log[-1].get("change_de") == entry["change_de"]):
                    log.append(entry)
            rec[field] = e["de"]
            rec[auth_field] = AUTH.format(d=DATE, c=e["core"])
            rec["core_basis"] = basis
            path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            n += 1
        lp = D / "localizations" / LANG / f"{rid}.json"
        loc = json.loads(lp.read_text(encoding="utf-8")) if lp.exists() else {
            "id": f"L10N-GSW-ZH-{rid}", "type": "localization", "status": "draft", "tags": [], "localizes": rid, "language": LANG,
            "target_context": "CTX-CH-ZH-GSW-2026", "fields": {}, "source_fingerprint": {},
            "review_de": "Noch keine muttersprachliche Prüfung dokumentiert.", "knowledge": {"asserted_at": DATE, "supersedes": None}}
        fp = localizations.fingerprint(e["de"])
        if loc["fields"].get(field) != e["gsw"] or loc["source_fingerprint"].get(field) != fp:
            if field in loc["fields"] and loc["fields"][field] != e["gsw"]:
                log = loc.setdefault("revision_log", [])
                entry = {"date": DATE, "change_de": f"Neu aus der Kernanalyse {e['core']}", "previous": {field: loc["fields"][field]}}
                if not (log and log[-1].get("date") == DATE and log[-1].get("change_de") == entry["change_de"]):
                    log.append(entry)
            loc["fields"][field] = e["gsw"]
            loc["source_fingerprint"][field] = fp
            loc["authorship_de"] = AUTH_GSW.format(d=DATE)
            lp.parent.mkdir(parents=True, exist_ok=True)
            lp.write_text(json.dumps(loc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            n += 1
    print(f"PASS: {len(sel)} Zusammenfassungen geprüft ({len(cores)} Kernanalysen, {len(warns)} Hinweise); {n} Dateien geschrieben; Quelle {SUMMARY_SRC.relative_to(ROOT)}")


if __name__ == "__main__":
    run([a for a in sys.argv[1:] if a != "--check"])
