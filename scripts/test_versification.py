#!/usr/bin/env python3
"""Tests der Umrechnung hebräisch -> Navigationszählung (scripts/versification.py) mit den echten TVTMS-Daten
und synthetischem Text (nur Verszahlen und Wortanzahl; für die Teilung ein echtes Teilungswort)."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import versification as V  # noqa: E402


def text(book, counts, words=3, special=None):
    out = {f"{book}.{c}.{v}": [f"w{i}" for i in range(words)] for c, n in counts.items() for v in range(1, n + 1)}
    out.update(special or {})
    return out


def targets(book, verses):
    plan, empty = V.heb_to_kjv(book, verses)
    return plan, V.apply(book, verses, plan), empty


# Joel: hebräisch 4 Kapitel (20, 27, 5, 21) -> KJV 3 Kapitel (20, 32, 21)
plan, out, _ = targets("JOL", text("JOL", {1: 20, 2: 27, 3: 5, 4: 21}))
assert plan["JOL.3.1"][0][0] == "JOL.2.28" and plan["JOL.4.21"][0][0] == "JOL.3.21"
assert sorted({r.rsplit(".", 1)[0] for r in out}) == ["JOL.1", "JOL.2", "JOL.3"]
# Psalm 3: Überschrift als hebräischer Vers 1 -> vor KJV-Vers 1
plan, out, _ = targets("PSA", text("PSA", {3: 9}))
assert plan["PSA.3.1"][0][3] == "title" and plan["PSA.3.2"][0][0] == "PSA.3.1"
assert [s for s, _, _ in out["PSA.3.1"]][:4] == ["PSA.3.1"] * 3 + ["PSA.3.2"]
assert len(out) == 8
# Numeri 25,19 (hebräisch) wird an den Anfang von KJV 26,1 gestellt
counts = {c: 30 for c in range(1, 37)}
counts[25] = 19
plan, out, _ = targets("NUM", text("NUM", counts))
assert out["NUM.26.1"][0][0] == "NUM.25.19" and "NUM.25.19" not in out
# Jesaja 63,19b -> KJV 64,1 ab dem Teilungswort
counts = {c: 30 for c in range(1, 67)}
counts[63], counts[64] = 19, 11
special = {"ISA.63.19": ["a", "b", "לוּא", "c"]}
plan, out, _ = targets("ISA", text("ISA", counts, special=special))
assert [i for s, i, _ in out["ISA.64.1"] if s == "ISA.63.19"] == [2, 3]
assert [i for s, i, _ in out["ISA.63.19"]] == [0, 1]
# Nehemia 7,68 fehlt im hebräischen Text -> leerer Zielvers
counts = {c: 20 for c in range(1, 14)}
counts[7] = 72
plan, out, empty = targets("NEH", text("NEH", counts))
assert empty == ["NEH.7.68"] and "NEH.7.68" not in out and "NEH.7.73" in out
print("PASS: Versifikation hebräisch -> KJV (Joel, Psalmüberschrift, Num 25/26, Jes 63/64, Neh 7,68)")
