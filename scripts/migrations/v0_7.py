#!/usr/bin/env python3
"""Migration v0.6 -> v0.7 (2026-10-09): bestehende Varianten und Alignments an SBLGNT-Token-IDs binden.

Rein additiv: neue Felder `base_edition`/`base_tokens` bzw. `source_tokens`; bestehende Felder,
Aussagen und Status bleiben unverändert. Die Zuordnung wird gegen die importierten Tokens geprüft
(Wortgleichheit ohne Interpunktion und textkritische Zeichen). Protokoll:
provenance/migrations/2026-10-09-v0.7.json. Idempotent.
"""
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOKS = {t["id"]: t for t in json.loads(
    (ROOT / "data/tokens/SBLGNT-MRK-003-022-030.json").read_text(encoding="utf-8"))["tokens"]}
LOG = ROOT / "provenance/migrations/2026-10-09-v0.7.json"


def tid(verse, *positions):
    return [f"TOK-SBLGNT-MRK-003-{verse:03d}-{p:03d}" for p in positions]


def norm(s):
    s = unicodedata.normalize("NFC", s).replace("ʼ", "’")
    return re.sub(r"[⸀-⸅,.·;:!?]", "", s).split()


def check(text, ids):
    words = [norm(TOKS[i]["text"])[0] for i in ids]
    assert norm(text) == words, (text, words)


VARIANTS = {
    "VAR-MRK-003-029-001": tid(29, 19, 20),  # αἰωνίου ἁμαρτήματος (Lesart R1 = SBLGNT-Text)
    "VAR-MRK-003-029-002": tid(29, 18),      # ἐστιν (Lesart R1 = SBLGNT-Text)
}
ALIGN = {
    "βλασφημήσῃ": tid(29, 4),
    "εἰς τὸ πνεῦμα τὸ ἅγιον": tid(29, 5, 6, 7, 8, 9),
    "οὐκ ἔχει ἄφεσιν": tid(29, 10, 11, 12),
    "εἰς τὸν αἰῶνα": tid(29, 13, 14, 15),
    "αἰωνίου ἁμαρτήματος": tid(29, 19, 20),
}

changes = []
for vid, ids in VARIANTS.items():
    path = ROOT / "data/variants" / f"{vid}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    r1 = next(r for r in data["readings"] if r["reading_id"] == "R1")
    check(r1["text"], ids)
    if data.get("base_tokens") != ids:
        data["base_edition"] = "ED-SBLGNT"
        data["base_tokens"] = ids
        changes.append({"file": str(path.relative_to(ROOT)), "field": "base_edition, base_tokens",
                        "old": None, "new": ids, "reason": "Variantenstelle an SBLGNT-Tokens gebunden; R1 entspricht dem SBLGNT-Text"})
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

path = ROOT / "data/alignments/ALIGN-MRK-003-029-001.json"
data = json.loads(path.read_text(encoding="utf-8"))
changed = False
for a in data["alignments"]:
    ids = ALIGN[a["source"]]
    check(a["source"], ids)
    if a.get("source_tokens") != ids:
        a["source_tokens"] = ids
        changed = True
if changed:
    data["source_token_basis"] = "ED-SBLGNT"
    changes.append({"file": str(path.relative_to(ROOT)), "field": "alignments[].source_tokens, source_token_basis",
                    "old": None, "new": {a["source"]: a["source_tokens"] for a in data["alignments"]},
                    "reason": "Zuordnungen an SBLGNT-Tokens gebunden; die zugeordneten Wörter sind in Arbeitstranskription und SBLGNT identisch"})
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if changes:
    LOG.write_text(json.dumps({"migration": "v0.6 -> v0.7", "date": "2026-10-09",
                               "script": "scripts/migrations/v0_7.py",
                               "note": "Rein additiv; keine bestehenden Werte verändert.",
                               "changes": changes}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(changes)} Änderungen" + (f", Protokoll: {LOG.relative_to(ROOT)}" if changes else " (bereits migriert)"))
