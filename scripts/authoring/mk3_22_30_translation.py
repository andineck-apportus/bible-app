"""Autorenwerkzeug: erzeugt Arbeitsübersetzung TRANS-MRK-003-022-030-DE-WORKING und Wortzuordnung ALIGN-MRK-003-022-030-001 (inkl. Abdeckungsprüfung). Aufruf: python3 scripts/authoring/mk3_22_30_translation.py . """
import json, pathlib, sys
ROOT = pathlib.Path(sys.argv[1])
toks = [t for t in json.loads((ROOT / "data/tokens/SBLGNT-MRK-003.json").read_text())["tokens"]
        if 22 <= int(t["reference"].split(".")[-1]) <= 30]
TEXT = {
 22: "Und die Schriftgelehrten, die von Jerusalem herabgekommen waren, sagten: «Er hat Beelzebul», und: «Durch den Herrscher der Dämonen treibt er die Dämonen aus.»",
 23: "Und er rief sie herbei und sagte in Gleichnissen zu ihnen: «Wie kann Satan Satan austreiben?",
 24: "Und wenn ein Reich gegen sich selbst gespalten ist, kann jenes Reich nicht bestehen.",
 25: "Und wenn ein Haus gegen sich selbst gespalten ist, wird jenes Haus nicht bestehen können.",
 26: "Und wenn der Satan sich gegen sich selbst erhoben hat und gespalten worden ist, kann er nicht bestehen, sondern hat ein Ende.",
 27: "Aber niemand kann in das Haus des Starken hineingehen und seinen Hausrat plündern, wenn er nicht zuerst den Starken bindet; und dann wird er sein Haus plündern.",
 28: "Amen, ich sage euch: Alles wird den Söhnen der Menschen vergeben werden, die Sünden und die Lästerungen, so viele sie auch lästern mögen.",
 29: "Wer aber gegen den Heiligen Geist lästert, hat auf ewig keine Vergebung, sondern ist einer ewigen Sünde schuldig.»",
 30: "Denn sie sagten: «Er hat einen unreinen Geist.»",
}
U = None  # nicht eigens übersetzt
# (Vers, [Positionen], Zieltext (Teile mit " … "), Art, Notiz)
A = [
 (22,[1],"Und","lexical",None),(22,[2,3],"die Schriftgelehrten","phrase",None),
 (22,[4,7],"die … herabgekommen waren","phrase","Artikel + Partizip als Relativsatz"),
 (22,[5,6],"von Jerusalem","phrase",None),(22,[8],"sagten","lexical","Imperfekt; auch «sagten immer wieder»"),
 (22,[9],U,"untranslated","ὅτι leitet direkte Rede ein; durch Doppelpunkt/Anführungszeichen wiedergegeben"),
 (22,[10],"Beelzebul","lexical",None),(22,[11],"Er hat","lexical","Subjekt im Verb enthalten; sinngemäss «ist von Beelzebul besessen»"),
 (22,[12],"und","lexical",None),(22,[13],U,"untranslated","ὅτι recitativum"),
 (22,[14,15,16,17,18],"Durch den Herrscher der Dämonen","phrase","ἐν instrumental; ἄρχων auch «Oberster», «Fürst»"),
 (22,[19],"treibt er … aus","lexical",None),(22,[20,21],"die Dämonen","phrase",None),
 (23,[1],"Und","lexical",None),(23,[2],"er rief … herbei","lexical","Partizip als finites Verb aufgelöst; «und» ergänzt"),
 (23,[3],"sie","lexical",None),(23,[4,5],"in Gleichnissen","phrase","παραβολή auch «Bildwort», «Rätselwort»"),
 (23,[6],"sagte","lexical","Imperfekt"),(23,[7],"zu ihnen","lexical",None),(23,[8],"Wie","lexical",None),
 (23,[9],"kann","lexical",None),(23,[10],"Satan","lexical","Subjekt"),(23,[11],"Satan","lexical","Objekt"),
 (23,[12],"austreiben","lexical",None),
 (24,[1],"Und","lexical",None),(24,[2],"wenn","lexical",None),(24,[3],"ein Reich","lexical",None),
 (24,[4,5],"gegen sich selbst","phrase",None),(24,[6],"gespalten ist","lexical","Konjunktiv Aorist Passiv; auch «gespalten wird», «entzweit», «uneins»"),
 (24,[7],"nicht","lexical",None),(24,[8],"kann","lexical",None),(24,[9],"bestehen","lexical","Aorist Passiv von ἵστημι: passivische Form mit intransitiver Bedeutung «standhalten, bestehen»"),
 (24,[10,11,12],"jenes Reich","phrase",None),
 (25,[1],"Und","lexical",None),(25,[2],"wenn","lexical",None),(25,[3],"ein Haus","lexical","οἰκία auch «Hausgemeinschaft», «Familie»"),
 (25,[4,5],"gegen sich selbst","phrase",None),(25,[6],"gespalten ist","lexical",None),(25,[7],"nicht","lexical",None),
 (25,[8],"wird … können","lexical","Futur gemäss SBLGNT; RP liest δύναται (Präsens), vgl. VAR-SBLGNTAPP-MRK-003-025-01"),
 (25,[9,10,11],"jenes Haus","phrase",None),(25,[12],"bestehen","lexical",None),
 (26,[1],"Und","lexical",None),(26,[2],"wenn","lexical",None),(26,[3,4],"der Satan","phrase",None),
 (26,[5],"sich … erhoben hat","lexical","ἀνίστημι «aufstehen», hier «sich erheben gegen»"),
 (26,[6,7],"gegen sich selbst","phrase",None),(26,[8],"und","lexical",None),
 (26,[9],"gespalten worden ist","lexical","Aorist Passiv gemäss SBLGNT (Ereignis); Treg/RP μεμέρισται (Perfekt, Zustand) wäre «gespalten ist»"),
 (26,[10],"nicht","lexical",None),(26,[11],"kann er","lexical",None),(26,[12],"bestehen","lexical",None),
 (26,[13],"sondern","lexical",None),(26,[14],"ein Ende","lexical",None),(26,[15],"hat","lexical","τέλος ἔχει sinngemäss «ist am Ende»"),
 (27,[1],"Aber","lexical",None),(27,[2],"niemand","lexical",None),(27,[3],"kann","lexical",None),
 (27,[4,5,6],"in das Haus","phrase",None),(27,[7,8],"des Starken","phrase",None),
 (27,[9],"hineingehen","lexical","Partizip εἰσελθών als erstes Infinitiv-Glied (koordiniert mit διαρπάσαι) aufgelöst; «und» ergänzt"),
 (27,[10,11],"Hausrat","phrase","σκεῦος «Gerät», «Gefäss», Plural «Habe»"),(27,[12],"seinen","lexical",None),
 (27,[13],"plündern","lexical","διαρπάζω; in 3,27 zweimal gleich wiedergegeben"),(27,[14,15],"wenn … nicht","phrase","ἐὰν μή «es sei denn»; Subjekt «er» ergänzt"),
 (27,[16],"zuerst","lexical",None),(27,[17,18],"den Starken","phrase",None),(27,[19],"bindet","lexical",None),
 (27,[20],"und","lexical",None),(27,[21],"dann","lexical",None),(27,[22,23],"Haus","phrase",None),
 (27,[24],"sein","lexical",None),(27,[25],"wird er … plündern","lexical","Futur gemäss SBLGNT; RP διαρπάσῃ (Konjunktiv)"),
 (28,[1],"Amen","lexical","Hebräisches Lehnwort, als Beteuerung am Satzanfang"),(28,[2],"ich sage","lexical",None),(28,[3],"euch","lexical",None),
 (28,[4],U,"untranslated","ὅτι leitet den Inhalt ein; Doppelpunkt"),(28,[5],"Alles","lexical",None),
 (28,[6],"wird … vergeben werden","lexical","Futur Passiv"),
 (28,[7,8,9,10],"den Söhnen der Menschen","idiom","Semitismus für «den Menschen»; wörtlich belassen"),
 (28,[11,12],"die Sünden","phrase","ἁμάρτημα «Verfehlung», «Sündentat»"),(28,[13],"und","lexical",None),
 (28,[14,15],"die Lästerungen","phrase",None),(28,[16,17],"so viele … auch","phrase","ὅσα: inneres Objekt zu βλασφημήσωσιν, Neutrum in Übereinstimmung mit πάντα, nicht mit dem femininen βλασφημίαι; RP ὅσας"),
 (28,[18],"sie … lästern mögen","lexical","Konjunktiv Aorist in verallgemeinerndem Relativsatz"),
 (29,[1],"Wer","lexical",None),(29,[2],"aber","lexical",None),
 (29,[3],U,"untranslated","ἄν verallgemeinernd; in «Wer» enthalten"),
 (29,[4],"lästert","lexical","Konjunktiv Aorist in verallgemeinerndem Relativsatz"),
 (29,[5,6,7,8,9],"gegen den Heiligen Geist","phrase","εἰς hier «gegen»"),(29,[10,11,12],"hat … keine Vergebung","phrase",None),
 (29,[13,14,15],"auf ewig","idiom",None),(29,[16],"sondern","lexical",None),(29,[17],"schuldig","lexical","ἔνοχος mit Genitiv: «verfallen», «schuldig»"),
 (29,[18],"ist","lexical","Lesart ἐστιν, vgl. VAR-MRK-003-029-002"),
 (29,[19,20],"einer ewigen Sünde","phrase","Lesart ἁμαρτήματος (R1); Alternative R2 «dem ewigen Gericht verfallen», vgl. VAR-MRK-003-029-001"),
 (30,[1],"Denn","lexical","ὅτι kausal; auch «weil»"),(30,[2],"sie sagten","lexical","Imperfekt"),
 (30,[3],"Geist","lexical",None),(30,[4],"einen unreinen","lexical",None),(30,[5],"Er hat","lexical",None),
]
by_id = {t["id"]: t for t in toks}
def source_text(ids):
    out=[]; prev=None
    for i in ids:
        pos=int(i[-3:])
        if prev is not None and pos!=prev+1: out.append("…")
        out.append(by_id[i]["word"]); prev=pos
    return " ".join(out)
seen = {}
entries = []
for v, pos, target, kind, note in A:
    ids = [f"TOK-SBLGNT-MRK-003-{v:03d}-{p:03d}" for p in pos]
    for i in ids:
        assert i in by_id, i
        assert i not in seen, ("doppelt", i)
        seen[i] = True
    if target is not None:
        for part in target.split(" … "):
            assert part in TEXT[v], (v, part)
    e = {"reference": f"MRK.3.{v}", "source_tokens": ids,
         "source": source_text(ids), "target": target, "kind": kind}
    if note: e["note_de"] = note
    entries.append(e)
missing = [t["id"] for t in toks if t["id"] not in seen]
assert not missing, missing
print("Abdeckung vollständig:", len(seen), "Tokens,", len(entries), "Zuordnungen")

sblgnt_units = sorted(p.stem for p in (ROOT / "data/variants/sblgntapp-mrk").glob("VAR-SBLGNTAPP-MRK-003-*.json")
                      if 22 <= int(p.stem.split("-")[-2]) <= 30)
trans = {
 "id": "TRANS-MRK-003-022-030-DE-WORKING", "type": "translation", "status": "draft",
 "tags": ["TAG-MARK", "TAG-HOLY-SPIRIT", "TAG-BLASPHEMY"],
 "reference": "MRK.3.22-MRK.3.30", "language": "de-CH",
 "translation_kind": "literal_original_working",
 "method_de": "Wörtlich orientierte Arbeitsübersetzung: Wortarten und Satzbau des Griechischen möglichst sichtbar, verständliches Deutsch; Partizipien teils als finite Verben aufgelöst. Schweizer Rechtschreibung.",
 "based_on_edition": "ED-SBLGNT", "based_on_tokens": "TOKSET-SBLGNT-MRK-003",
 "follows_readings": [f"{u}:R1" for u in sblgnt_units] + ["VAR-MRK-003-029-001:R1", "VAR-MRK-003-029-002:R1"],
 "text_by_reference": {f"MRK.3.{v}": t for v, t in TEXT.items()},
 "incorporates": "TRANS-MRK-003-029-DE-WORKING",
 "translation_notes": [
  "Mk 3,29 wörtlich aus TRANS-MRK-003-029-DE-WORKING übernommen; nur das schliessende Anführungszeichen ergänzt.",
  "Die Rede Jesu reicht von 3,23b bis 3,29; die Anführungszeichen markieren das.",
  "Die Übersetzung folgt an allen Apparatstellen dem SBLGNT-Text (siehe follows_readings); im Deutschen sichtbar in 3,25 (Futur), 3,26 (Aorist: «gespalten worden ist»), 3,27 (Futur) und 3,29 (Sünde/Gericht).",
  "Einzelentscheidungen und Alternativen stehen in ALIGN-MRK-003-022-030-001.",
  "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
 ],
 "authorship_de": "KI-Entwurf (Claude) vom 2026-10-09; keine fachliche Prüfung erfolgt.",
 "knowledge": {"asserted_at": "2026-10-09", "supersedes": None},
}
align = {
 "id": "ALIGN-MRK-003-022-030-001", "type": "alignment", "status": "draft",
 "tags": ["TAG-MARK"], "reference": "MRK.3.22-MRK.3.30",
 "source_language": "grc", "target_language": "de-CH",
 "source_basis": "ED-SBLGNT", "source_tokens_set": "TOKSET-SBLGNT-MRK-003",
 "target_translation": "TRANS-MRK-003-022-030-DE-WORKING",
 "coverage": "complete", "coverage_de": "Jedes der 140 SBLGNT-Tokens ist genau einer Zuordnung zugewiesen; «untranslated» bedeutet: nicht als eigenes Wort wiedergegeben.",
 "target_convention_de": "« … » trennt nicht zusammenhängende Teile des deutschen Wortlauts.",
 "alignments": entries,
 "incorporates": "ALIGN-MRK-003-029-001",
 "authorship_de": "KI-Entwurf (Claude) vom 2026-10-09; keine fachliche Prüfung erfolgt.",
 "knowledge": {"asserted_at": "2026-10-09", "supersedes": None},
}
for path, obj in (("data/translations/TRANS-MRK-003-022-030-DE-WORKING.json", trans),
                  ("data/alignments/ALIGN-MRK-003-022-030-001.json", align)):
    (ROOT / path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("geschrieben")
