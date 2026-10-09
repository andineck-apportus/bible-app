# Datenmodell: Ist-Stand und Ziel

## Vorhandene Objekte in v0.6

| Ordner | Tatsächliches `type` | Anzahl | Aufgabe |
|---|---|---:|---|
| works | work | 1 | Biblisches Werk |
| text-units | text_unit | 1 | Natürliche Texteinheit und Versbereich |
| studies | study | 1 | Pilotstudie mit Ergebnissen und offenen Fragen |
| sources | source / dataset | 4 | Quellenhinweise und externer Datensatz |
| editions | critical_edition | 1 | Editionsidentität |
| text-samples | text_sample | 1 | Nicht verifizierte Arbeitstranskription |
| tokens | token_set | 1 | Importierte SBLGNT-Tokens Mk 3,22–30 mit Lemma und Morphologie (140 Tokens) |
| counts | lemma_count | 1 | Daraus abgeleitete Token-, Wortform- und Lemmazählung |
| findings | finding | 4 | Textliche/literarische/textkritische Befunde |
| variants | variant | 2 | Variantenstellen und berichtete Lesarten |
| decisions | editorial_decision | 1 | Begründete, revidierbare Lesartpräferenz |
| translations | translation | 1 | Eigene deutsche Arbeitsübersetzung |
| alignments | alignment | 1 | Vorläufige Wort-/Phrasenzuordnungen |
| interpretations | interpretation | 2 | Alternative Verständnisse |
| principles | principle | 1 | Abgeleitetes Prinzip |
| contexts | context | 2 | Historischer und heutiger Kontext |
| applications | application | 1 | Kontextabhängige Anwendung |
| topics | topic | 2 | Inhaltliche Themen |
| relations | relation | 3 | Beziehungen zu Parallelstellen |
| questions | open_question | 1 | Offene Forschungsfrage |
| tags | tag | 6 | Kontrollierte Tags |

Gesamt: 38 Datensätze, einschliesslich der 6 Tags. Die Tokens sind Teil des `token_set` und keine eigenen Datensatzdateien; sie haben dennoch stabile IDs (`TOK-SBLGNT-MRK-003-029-004`).

## Bestehende Referenzen
`work`, `primary_unit`, `subject`, `based_on`, `derived_from`, `principle`, `context`, `outputs`, `evidence_objects`, `related`, `from`, `edition`, `imported_records`, `supersedes` und `tags` verknüpfen Datensätze. `VAR-…:R1` referenziert eine Lesart innerhalb eines Variantenobjekts. Bibelstellen (`reference`, `to_ref`, `range`, `evidence_refs`, `imported_scope`) folgen seit v0.6 einheitlich [BIBELSTELLEN.md](BIBELSTELLEN.md). Der Validator prüft alle diese Verweise.

Beispielkette: `FIND-MRK-0001` → `INT-MRK-0001` → `PRIN-MRK-0001` → `APP-MRK-0001`; die Anwendung verweist auf `CTX-CH-DE-2026`. Die textkritische Entscheidung und die Arbeitsübersetzung referenzieren eine bestimmte Lesart.

## Noch nicht implementiert
Eigene Handschriften-/Zeugenobjekte mit Korrekturschichten; eigenständige Lemma-/Lexikonobjekte; Verknüpfung von Alignments und Varianten mit Token-IDs; vollständige Alignments aller neun Verse; Argumente/Gegenargumente als eigene Objekte; einheitliche Quellenbelege mit genauen Fundstellen; durchgängige Zeit- und Revisionsmetadaten; typspezifische Schemas; Versifikationstabelle; SQLite-Projektion; Benutzeroberfläche.

## Typnamen und Schema
Seit v0.6 sind die Typnamen kanonisch in `snake_case` (`study`, `text_unit`); das Schema listet alle verwendeten Typen und Statuswerte. Die Umstellung der v0.5-Daten (`studie`, `text-unit`) erfolgte per `scripts/migrations/v0_6.py` und ist in `provenance/migrations/2026-10-09-v0.6.json` protokolliert. Das Schema ist weiterhin generisch; typspezifische Pflichtfelder folgen.
