# Status und nächste Schritte · 2026-10-09

## Gesichert und vorhanden
- Alle Originalpakete v0.1–v0.5; rekonstruierte Git-Historie mit je einem Snapshot.
- Pilot v0.6: 38 Datensätze, darin 6 Tags.
- **Griechischer Text Mk 3,22–30** aus MorphGNT SBLGNT 6.12 (Commit `a2afca0`): 140 Tokens mit Text, Wortform, Lemma, Wortart und Parsing; daraus 91 verschiedene normalisierte Wortformen und 64 Lemmata. Status `imported_unreviewed`.
- **Einheitliche Bibelstellen** nach [BIBELSTELLEN.md](BIBELSTELLEN.md), mit Werkzeug `scripts/refs.py`; alle bestehenden Daten migriert und protokolliert.
- Variantenstellen Mk 3,29: Sünde/Gericht und ist/wird sein, als vorläufige Forschungsdaten.
- Revidierbare textkritische Entscheidung; eigene deutsche Arbeitsübersetzung; teilweise Wort-/Phrasenalignments.
- Quellenhinweise, alternative Interpretationen, Prinzip, heutige Anwendung, Kontexte, Parallelstellen und offene Frage.
- Validator für Schema, IDs, Tags, Verweise, Lesarten und Bibelstellen; synthetische Importtests im echten MorphGNT-Format.

## In v0.6 behobene technische Lücken
1. Validator lädt jetzt das Schema und prüft Verweise sowie Bibelstellen (vorher nur vier Feldnamen, IDs und Tags).
2. Schema und Daten sind konsistent: Typnamen `study`/`text_unit`, alle Typen und Statuswerte im Schema.
3. Die Pilotstudie führt alle Ergebnisse in `outputs`.
4. Der Importer erwartete ein falsches Referenzformat (`6203xx` statt `0203xx`) und hätte die echte Datei immer abgelehnt; behoben, Quelle mit Upstream-Commit wird im Datensatz festgehalten.

## Weiterhin offene technische Lücken
1. Typspezifische Schemas fehlen; der Validator prüft nur die gemeinsamen Felder.
2. Ob ein Vers existiert, wird nicht geprüft (keine Versifikationstabelle).
3. Alignments und Varianten verweisen auf griechischen Text, noch nicht auf Token-IDs.
4. Quellen-, Review- und Zeitmetadaten sind uneinheitlich und lückenhaft.
5. Lizenzangaben: Das MorphGNT-README nennt für den SBLGNT-Text noch die SBLGNT EULA, Faithlife/SBLGNT nennt CC BY 4.0. Vor einer Veröffentlichung klären.

## Befunde aus dem Import
- Die alte Arbeitstranskription von Mk 3,29–30 weicht nur in einem Wort von SBLGNT ab: `ἀλλ’` statt `ἀλλὰ` (3,29). Vergleich: `reports/compare-TEXT-MRK-003-029-030-WORKING-vs-SBLGNT.json`. Die Transkription bleibt als historischer Arbeitsstand erhalten.
- SBLGNT markiert in 3,29 `ἁμαρτήματος` als Variantenstelle; das stimmt mit `VAR-MRK-003-029-001` überein. In den Versen 3,25–28 markiert SBLGNT weitere Variantenstellen, die im Pilot noch nicht erfasst sind.
- Die Glossen von R1 (`ἁμαρτήματος`) und R3 (`ἁμαρτίας`) in `VAR-MRK-003-029-001` lauten beide «ewiger Sünde»; der Unterschied ist sprachlich noch zu beschreiben.

## Fachlich noch offen
- Eigene Prüfung der berichteten Lesarten an Primärmaterial und kritischem Apparat einschliesslich Korrekturschichten.
- Fachliche Prüfung der importierten Morphologie/Lemmata für die Perikope.
- Vollständige Wortzuordnung für alle neun Verse.
- Präzise wissenschaftliche Fundstellen, weitere Gegenargumente und eigenständige Kontextanwendungen.
- Kritische Prüfung des abgeleiteten Prinzips: Es enthält stärkere Begriffe als die begrenzte Beobachtung zum Wissen der Schriftgelehrten. Diese Ableitung ist nicht allein durch den Pilotbestand abgesichert.

## Nächster Meilenstein v0.7 (Vorschlag)
Alignments und Varianten an Token-IDs binden; vollständige Arbeitsübersetzung und Wortzuordnung Mk 3,22–30; weitere SBLGNT-Variantenstellen der Perikope erfassen; typspezifische Schemas für die wichtigsten Typen.

## Danach
Primärbelege; standardisierte Revisions-/Reviewmetadaten; Versifikationsmodell; SQLite-Projektion; anschliessend eine Oberfläche auf der stabilisierten Datenbasis. Technische Produktentscheidungen bleiben offen.
