"""Lokalisierungen (Typ `localization`) laden und gegen den aktuellen Stand der Originale prüfen.

Eine Lokalisierung übersetzt einzelne Felder eines Originaldatensatzes (`localizes`) in eine Sprache
(`language`, BCP-47). `source_fingerprint` hält je Feld fest, von welchem Stand des Originals übersetzt wurde.
Ändert sich das Original, gilt das Feld als veraltet: Es wird nicht ausgeliefert (die App zeigt dann das
Original) und der Validator meldet es. So bleiben neue Quellen, neue Deutungen und neue Sprachen voneinander
unabhängig: Kein Originaldatensatz trägt Übersetzungen in sich.
"""
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def stale_fields(loc, original):
    fp = loc.get("source_fingerprint") or {}
    return sorted(k for k in loc.get("fields", {}) if fp.get(k) != fingerprint(original.get(k)))


def load(originals, root=ROOT):
    """originals: {id: record}. Ergebnis: {id: {sprachgrundtag: {feld: wert}}} – nur aktuelle Felder."""
    out = {}
    for p in sorted((root / "data" / "localizations").rglob("*.json")):
        loc = json.loads(p.read_text(encoding="utf-8"))
        if loc.get("status") == "deprecated":
            continue
        orig = originals.get(loc["localizes"])
        if orig is None:
            continue
        stale = set(stale_fields(loc, orig))
        fields = {k: v for k, v in loc["fields"].items() if k not in stale}
        if fields:
            out.setdefault(loc["localizes"], {})[loc["language"].split("-")[0]] = fields
    return out


def load_all(root=ROOT):
    recs = {}
    for p in sorted((root / "data").rglob("*.json")):
        if "localizations" in p.parts:
            continue
        r = json.loads(p.read_text(encoding="utf-8"))
        recs[r["id"]] = r
    return load(recs, root)
