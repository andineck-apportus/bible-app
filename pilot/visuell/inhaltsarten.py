#!/usr/bin/env python3
"""Inhaltsarten der ganzen Bibel je Kapitel (Schätzung nach der vorherrschenden Art je Kapitel) und Versanteile.
Grundlage: Navigationsgerüst NAV-PROT66-KJV (Verszahlen) und die Bücherübersicht im Strukturkatalog. Grob: ein Kapitel zählt
ganz zu seiner vorherrschenden Art; gemischte Kapitel (z. B. Lied in einer Erzählung) sind nicht aufgeteilt.
Ausgabe: pilot/visuell/inhaltsarten.json
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ARTEN = {
    "erz": "Erzählung", "rede": "Rede und Lehre (mit Gleichnissen)", "gesetz": "Gesetz und Weisung", "liste": "Listen und Stammbäume",
    "bau": "Bau, Masse, Gebiete", "poesie": "Lied und Gebet", "weisheit": "Weisheit und Dialog", "prophetie": "Prophetenwort",
    "vision": "Vision und Apokalyptik", "brief": "Brief und Argument",
}
# Buch: Grundart, Ausnahmen {Kapitel: Art}
K = {
 "GEN": ("erz", {5: "liste", 10: "liste", 11: "liste", 36: "liste", 46: "liste", 49: "poesie"}),
 "EXO": ("erz", {15: "poesie", **{c: "gesetz" for c in range(20, 24)}, **{c: "bau" for c in range(25, 32)}, **{c: "bau" for c in range(35, 41)}}),
 "LEV": ("gesetz", {8: "erz", 9: "erz", 10: "erz"}),
 "NUM": ("erz", {1: "liste", 2: "bau", 3: "liste", 4: "liste", 5: "gesetz", 6: "gesetz", 7: "liste", 15: "gesetz", 18: "gesetz", 19: "gesetz",
                 26: "liste", 28: "gesetz", 29: "gesetz", 30: "gesetz", 33: "liste", 34: "bau", 35: "gesetz", 36: "gesetz"}),
 "DEU": ("gesetz", {1: "rede", 2: "rede", 3: "rede", 4: "rede", 27: "rede", 28: "rede", 29: "rede", 30: "rede", 31: "erz", 32: "poesie", 33: "poesie", 34: "erz"}),
 "JOS": ("erz", {**{c: "bau" for c in range(13, 22)}}),
 "JDG": ("erz", {5: "poesie"}), "RUT": ("erz", {}), "1SA": ("erz", {}), "2SA": ("erz", {22: "poesie"}),
 "1KI": ("erz", {6: "bau", 7: "bau"}), "2KI": ("erz", {}),
 "1CH": ("erz", {**{c: "liste" for c in range(1, 10)}, **{c: "liste" for c in range(23, 28)}, 12: "liste"}),
 "2CH": ("erz", {3: "bau", 4: "bau"}), "EZR": ("erz", {2: "liste"}), "NEH": ("erz", {3: "liste", 7: "liste", 10: "liste", 11: "liste", 12: "liste"}),
 "EST": ("erz", {}),
 "JOB": ("weisheit", {1: "erz", 2: "erz", 42: "erz"}), "PSA": ("poesie", {}), "PRO": ("weisheit", {}), "ECC": ("weisheit", {}), "SNG": ("poesie", {}),
 "ISA": ("prophetie", {36: "erz", 37: "erz", 38: "erz", 39: "erz", 6: "vision"}),
 "JER": ("prophetie", {**{c: "erz" for c in (26, 27, 28, 29, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 52)}}),
 "LAM": ("poesie", {}),
 "EZK": ("prophetie", {1: "vision", 8: "vision", 9: "vision", 10: "vision", 37: "vision", **{c: "bau" for c in range(40, 49)}}),
 "DAN": ("vision", {**{c: "erz" for c in range(1, 7)}}),
 "HOS": ("prophetie", {1: "erz", 3: "erz"}), "JOL": ("prophetie", {}), "AMO": ("prophetie", {7: "vision", 8: "vision", 9: "vision"}),
 "OBA": ("prophetie", {}), "JON": ("erz", {2: "poesie"}), "MIC": ("prophetie", {}), "NAM": ("prophetie", {}), "HAB": ("prophetie", {3: "poesie"}),
 "ZEP": ("prophetie", {}), "HAG": ("prophetie", {}), "ZEC": ("prophetie", {**{c: "vision" for c in range(1, 7)}}), "MAL": ("prophetie", {}),
 "MAT": ("erz", {1: "liste", 5: "rede", 6: "rede", 7: "rede", 10: "rede", 13: "rede", 18: "rede", 23: "rede", 24: "rede", 25: "rede"}),
 "MRK": ("erz", {4: "rede", 13: "rede"}),
 "LUK": ("erz", {6: "rede", 12: "rede", 14: "rede", 15: "rede", 16: "rede", 17: "rede", 21: "rede"}),
 "JHN": ("erz", {5: "rede", 6: "rede", 8: "rede", 10: "rede", 14: "rede", 15: "rede", 16: "rede", 17: "poesie"}),
 "ACT": ("erz", {}),
 "REV": ("vision", {1: "vision", 2: "brief", 3: "brief"}),
}
BRIEFE = ["ROM", "1CO", "2CO", "GAL", "EPH", "PHP", "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD"]
for b in BRIEFE:
    K[b] = ("brief", {})
K["JHN"][1][17] = "rede"  # Gebet Jesu als Rede gezählt


def main():
    nav = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
    gruppe = {b: g for g in nav["groups"] for b in g["books"]}
    tot, je_gruppe, je_buch = {}, {}, {}
    for bk in nav["books"]:
        grund, aus = K[bk["code"]]
        for c, n in enumerate(bk["verses_per_chapter"], 1):
            a = aus.get(c, grund)
            tot[a] = tot.get(a, 0) + n
            g = gruppe[bk["code"]]["de"]
            je_gruppe.setdefault(g, {}).setdefault(a, 0)
            je_gruppe[g][a] += n
            je_buch.setdefault(bk["code"], {}).setdefault(a, 0)
            je_buch[bk["code"]][a] += n
    summe = sum(tot.values())
    out = {"verse": summe, "arten": ARTEN, "gesamt": {a: tot.get(a, 0) for a in ARTEN},
           "anteil": {a: round(100 * tot.get(a, 0) / summe, 1) for a in ARTEN}, "je_gruppe": je_gruppe, "je_buch": je_buch,
           "buecher": [{"code": b["code"], "de": b["de"], "abbr": b["abbr"], "verse": sum(b["verses_per_chapter"]), "kapitel": len(b["verses_per_chapter"]),
                        "gruppe": gruppe[b["code"]]["de"], "testament": gruppe[b["code"]]["testament"]} for b in nav["books"]]}
    (ROOT / "pilot/visuell/inhaltsarten.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for a in ARTEN:
        print(f"{ARTEN[a]:38} {tot.get(a, 0):6} Verse {out['anteil'][a]:5}%")
    print("Summe", summe)


if __name__ == "__main__":
    main()
