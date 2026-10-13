# Bibelstellen: kanonische Schreibweise

Ab v0.6 werden alle Bibelstellen in den Daten in genau einer maschinenlesbaren Form gespeichert. Sie ist die Grundlage für Verknüpfung, Zoom, Suche, Zählungen und die spätere SQLite-Projektion. Deutsche Schreibweisen wie «Mk 3,29» sind nur Anzeige und werden nie als Referenz gespeichert.

## Form

| Umfang | Kanonisch | Anzeige (de) |
|---|---|---|
| Buch | `MRK` | Mk |
| Kapitel | `MRK.3` | Mk 3 |
| Vers | `MRK.3.29` | Mk 3,29 |
| Versbereich | `MRK.3.22-MRK.3.30` | Mk 3,22–30 |
| Kapitelübergreifend | `JHN.3.16-JHN.4.2` | Joh 3,16–4,2 |
| Kapitelbereich | `PSA.23-PSA.24` | Ps 23–24 |

Regeln:
- Buchcodes nach **USFM/Paratext** (drei Zeichen, z. B. `MAT`, `MRK`, `LUK`, `JHN`, `1CO`). Die vollständige Liste steht in `scripts/refs.py`.
- Kapitel und Vers sind positive Ganzzahlen ohne führende Nullen, getrennt durch Punkte.
- Bereiche nennen beide Enden vollständig (`MRK.3.22-MRK.3.30`, nicht `MRK.3.22-30`). Beide Enden haben dieselbe Genauigkeit, liegen im selben Buch, und das Ende liegt nach dem Anfang.
- Mehrere getrennte Stellen sind eine Liste von Stellen, kein zusammengesetzter Text.
- Die deutsche Anzeige folgt den Loccumer Richtlinien (Mt, Mk, Lk, Joh, Apg, Röm, 1 Kor …).

## Was nicht in die Stelle gehört
- **Wort- oder Tokenposition:** wird über Token-IDs bzw. Token-Positionen der jeweiligen Edition angegeben (z. B. `TOK-SBLGNT-MRK-003-029-004`), nicht über Zusätze wie «29a».
- **Lesart:** wird über das Variantenobjekt referenziert (`VAR-MRK-003-029-001:R1`).
- **Edition/Übersetzung:** steht in eigenen Feldern; die Stelle selbst ist editionsneutral.

## Versifikation
- **Bezugszählung** ist die der Navigation (`data/navigation/NAV-PROT66-KJV.json`, KJV, 31 102 Verse). Laut TVTMS weicht die KJV im NT an wenigen Stellen von deren Standardzählung (NRSV) ab, u. a. 2 Kor 13,12–14, 3 Joh 14–15 und Offb 12,17–18. Für Matthäus, Markus und Lukas kommen im SBLGNT keine Versnummern vor, die es in der KJV nicht gibt (Prüfung des Validators); einzelne Versgrenzen liegen laut TVTMS leicht anders (z. B. Mk 3,20, «StartDifferent»), und Verse wie Mk 9,44 fehlen im SBLGNT.
- Ein Datensatz mit anderer Zählung gibt sie im Feld `versification` an. Der Validator meldet Stellen, die es in der Bezugszählung nicht gibt, als WARN, wenn der Datensatz KJV angibt oder nichts angibt (Stand v0.31: 5 Querverweise von OpenBible.info auf 3 Joh 1,15, obwohl der Datensatz KJV angibt).
- Zuordnungsdaten zwischen den Traditionen (Hebräisch, Latein, Griechisch/LXX, Englisch …) liegen als `versification_map` vor (TVTMS, STEPBible, CC BY 4.0). Umrechnung hebräisch → Navigationszählung (KJV) ist seit v0.36 umgesetzt (`scripts/versification.py`): Der Import (`scripts/import_macula_hebrew_book.py`) rechnet die Stellen des WLC nach den TVTMS-Zeilen um, deren Bedingungen am hebräischen Text erfüllt sind, und bricht ab, wenn die Verszahlen je Kapitel danach nicht der Navigation entsprechen. Ganze Verse werden umnummeriert; Psalmüberschriften (eigener hebräischer Vers) werden dem ersten Vers vorangestellt und als `title` markiert, weil die Navigation keinen Vers 0 kennt; die wenigen geteilten bzw. zusammengelegten Verse (1 Chr 12,4–5; 1 Kön 22,43–44; 1 Sam 20,42/21,1; Num 25,19/26,1; Jes 63,19/64,1; Ps 13,5–6) folgen TVTMS, die Teilungsstelle ist im Code am Text belegt. Neh 7,68 fehlt im WLC und bleibt leer. Jeder umgerechnete Token behält `source_reference`/`source_word_no`. `scripts/check_versification_ot.py` prüft alle 39 Bücher (Stand: alle stimmen mit der Navigation überein). Andere Richtungen (Septuaginta, Vulgata) folgen bei Bedarf.

## Stellen im Fliesstext
In Erklärtexten stehen Bibelstellen als Marke `[[MAT.6.34]]` (Bereich `[[MRK.3.28-MRK.3.29]]`), nicht als «Mt 6,34». Die Anzeige erzeugt die App je Sprache (im Kontextbuch ohne Buchname, Folgestellen im selben Buch «; 64,7» bzw. Kapitel «.12» verkürzt). `scripts/prose_refs.py` wandelt deutsche Schreibweisen um (`mark`), listet Marken (`marks`) und noch unmarkierte Stellen (`unmarked`) und erzeugt die Anzeige (`render`). Angaben zu ausserbiblischen Werken («Didache 8,2», «Henochbuch 10,4») sind keine Bibelstellen und bleiben Text.

## Werkzeuge
- `scripts/refs.py` prüft kanonische Stellen (`parse`), wandelt lockere Eingaben um (`canonical("Mk 3,22–30")` → `MRK.3.22-MRK.3.30`) und erzeugt die Anzeige (`display_de`).
- `scripts/validate.py` prüft alle Stellenfelder der Daten gegen diese Konvention.
- Ob ein Vers in der Bezugszählung existiert, prüft der Validator gegen die Verszahlen der Navigation (WARN, siehe oben).

## Felder mit Bibelstellen
`reference`, `to_ref`, `range` (Bereich der Texteinheit), die Listen `evidence_refs` und `imported_scope`, die Schlüssel von `text_by_reference` sowie `tokens[].reference`. Neue Felder mit Stellen müssen in `scripts/validate.py` (`REF_FIELDS` bzw. `REF_LIST_FIELDS`) eingetragen werden.

## Migration
Die v0.5-Daten verwendeten `Mk 3:29`, `Mark 3:29`, `Mk 3:22-30` und `{"start": "3:22", "end": "3:30"}`. Sie wurden am 2026-10-09 mit `scripts/migrations/v0_6.py` umgestellt; jede Änderung mit altem und neuem Wert steht in `provenance/migrations/2026-10-09-v0.6.json`.
