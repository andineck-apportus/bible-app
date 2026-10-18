"""Nachtrag: Einträge des SBLGNT-Apparats zu Matthäus, die der Import nicht automatisch zuordnen konnte.

Aufruf: python3 scripts/authoring/sblgntapp_nachtrag_mat.py
Quelle: reports/sblgntapp-MAT-nicht-zugeordnet.json (7 Einträge). Die Zuordnung zu den SBLGNT-Wörtern ist hier von Hand
festgelegt (Werkzeug scripts/import_sblgnt_apparatus.py konnte Markierungen über Versgrenzen, Satzzeichen-Varianten und
zwei Einträge an einer Markierung nicht auswerten). Lesarten und Siglen unverändert aus dem Apparat.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "data/variants/sblgntapp-mat"
REPORT = json.loads((ROOT / "reports/sblgntapp-MAT-nicht-zugeordnet.json").read_text(encoding="utf-8"))
SIGLA = {"WH": "ED-WH", "⟦WH⟧": "ED-WH", "Treg": "ED-TREG", "NA28": "ED-NA28", "RP": "ED-RP", "NIV": None}
SOURCE = {"url": "https://github.com/Faithlife/SBLGNT", "upstream_commit": "c4d241a9c1c479a55b989ba35a4976c1d0b8052c",
          "file": "data/sblgntapp/text/Matt.txt", "sha256": REPORT["source_sha256"],
          "license": "CC BY 4.0, © 2010 Society of Biblical Literature und Logos Bible Software"}


def toks(ch, v, a, b=None):
    return [f"TOK-SBLGNT-MAT-{ch:03d}-{v:03d}-{n:03d}" for n in range(a, (b or a) + 1)]


# (ID, Stelle, Wörter, Apparateintrag, [(Text, Siglen)], Hinweis)
ENTRIES = [
    ("VAR-SBLGNTAPP-MAT-001-007-01", "MAT.1.7-MAT.1.8", toks(1, 7, 15) + toks(1, 8, 1),
     "7–8 Ἀσάφ Ἀσὰφ WH Treg NA28 ] Ἀσά Ἀσὰ NIV RP",
     [("Ἀσάφ … Ἀσὰφ", ["WH", "Treg", "NA28"]), ("Ἀσά … Ἀσὰ", ["NIV", "RP"])],
     "Asaf (Name des Psalmdichters) oder Asa (Name des Königs, vgl. [[1KI.15.9]])."),
    ("VAR-SBLGNTAPP-MAT-011-009-01", "MAT.11.9", toks(11, 9, 3, 5),
     "; προφήτην ἰδεῖν WH ] ἰδεῖν; προφήτην Treg NA28 RP",
     [("ἐξήλθατε; προφήτην ἰδεῖν;", ["WH"]), ("ἐξήλθατε ἰδεῖν; προφήτην;", ["Treg", "NA28", "RP"])],
     "Nur Satzzeichen: «Wozu seid ihr hinausgegangen? Einen Propheten zu sehen?» bzw. «Was zu sehen seid ihr hinausgegangen? Einen Propheten?»"),
    ("VAR-SBLGNTAPP-MAT-016-002-01", "MAT.16.2-MAT.16.3", toks(16, 2, 6, 13) + toks(16, 3, 1, 23),
     "16:2–3 Ὀψίας γενομένης … οὐ δύνασθε Treg NA28 RP ] ⟦WH⟧",
     [("Ὀψίας γενομένης … οὐ δύνασθε", ["Treg", "NA28", "RP"]), ("", ["⟦WH⟧"])],
     "Westcott-Hort setzen die Wetterworte in doppelte eckige Klammern (nach ihrem Urteil nicht ursprünglich)."),
    ("VAR-SBLGNTAPP-MAT-016-003-01", "MAT.16.3", toks(16, 3, 10),
     "τὸ Treg NA28 ⟦WH⟧ ] Ὑποκριταί τὸ RP",
     [("τὸ", ["Treg", "NA28", "⟦WH⟧"]), ("Ὑποκριταί, τὸ", ["RP"])],
     "RP liest zusätzlich die Anrede «Heuchler»."),
    ("VAR-SBLGNTAPP-MAT-019-017-01", "MAT.19.17", toks(19, 17, 7, 14),
     "ἐρωτᾷς περὶ τοῦ ἀγαθοῦ; εἷς ἐστιν ὁ ἀγαθός WH Treg NA28 ] λέγεις ἀγαθόν; Οὐδεὶς ἀγαθός εἰ μὴ εἷς ὁ θεός RP",
     [("ἐρωτᾷς περὶ τοῦ ἀγαθοῦ; εἷς ἐστιν ὁ ἀγαθός", ["WH", "Treg", "NA28"]),
      ("λέγεις ἀγαθόν; Οὐδεὶς ἀγαθός εἰ μὴ εἷς ὁ θεός", ["RP"])],
     "«Was fragst du mich nach dem Guten? Einer ist der Gute» bzw. (wie [[MRK.10.18]]; [[LUK.18.19]]) «Was nennst du mich gut? Niemand ist gut ausser einer, Gott»."),
    ("VAR-SBLGNTAPP-MAT-026-060-01", "MAT.26.60", toks(26, 60, 4, 10),
     "60–61 πολλῶν προσελθόντων ψευδομαρτύρων. ὕστερον δὲ προσελθόντες δύο WH Treg NA28 ] καὶ πολλῶν ψευδομαρτύρων προσελθόντων, οὐχ εὗρον. Ὕστερον δὲ προσελθόντες δύο ψευδομάρτυρες RP",
     [("πολλῶν προσελθόντων ψευδομαρτύρων. ὕστερον δὲ προσελθόντες δύο", ["WH", "Treg", "NA28"]),
      ("καὶ πολλῶν ψευδομαρτύρων προσελθόντων, οὐχ εὗρον. Ὕστερον δὲ προσελθόντες δύο ψευδομάρτυρες", ["RP"])],
     "RP wiederholt «sie fanden keinen» und nennt die zwei ausdrücklich «falsche Zeugen»."),
    ("VAR-SBLGNTAPP-MAT-026-061-01", "MAT.26.61", toks(26, 61, 14),
     "οἰκοδομῆσαι WH Treg NA28 ] + αὐτόν RP",
     [("οἰκοδομῆσαι", ["WH", "Treg", "NA28"]), ("οἰκοδομῆσαι αὐτόν", ["RP"])],
     "RP ergänzt das Objekt «ihn» (den Tempel)."),
]


def main():
    known = {e["entry"] for e in REPORT["entries"]}
    n = 0
    for vid, ref, base, entry, rds, note in ENTRIES:
        assert entry in known, entry
        readings = []
        for i, (txt, sig) in enumerate(rds, 1):
            r = {"reading_id": f"R{i}", "text": txt, "is_sblgnt_text": i == 1,
                 "editions": [SIGLA[s] for s in sig if SIGLA.get(s)], "sigla": sig}
            if i > 1:
                r["relation_to_sblgnt"] = "unclassified"
            readings.append(r)
        rec = {"id": vid, "type": "variant", "status": "imported_unreviewed", "tags": ["TAG-MATTHEW", "TAG-TEXT-CRITICISM"],
               "reference": ref, "evidence_level": "edition_apparatus", "apparatus": "SRC-SBLGNT-APPARATUS", "base_edition": "ED-SBLGNT",
               "base_tokens": base, "readings": readings, "apparatus_entry": entry,
               "note_de": "Vergleich gedruckter Editionen laut SBLGNT-Apparat; keine Handschriftenbelege. " + note,
               "source": SOURCE,
               "import": {"tool": "scripts/authoring/sblgntapp_nachtrag_mat.py", "imported_on": "2026-10-18",
                          "note_de": "Vom automatischen Import nicht zugeordnet; Wortzuordnung von Hand (KI), Lesarten und Siglen unverändert."}}
        p = OUT / f"{vid}.json"
        txt = json.dumps(rec, ensure_ascii=False, indent=2) + "\n"
        if not p.exists() or p.read_text(encoding="utf-8") != txt:
            p.write_text(txt, encoding="utf-8")
            n += 1
    print(f"PASS: SBLGNT-Apparat Matthäus, Nachtrag {len(ENTRIES)} Einträge; {n} Dateien geschrieben")


if __name__ == "__main__":
    sys.exit(main())
