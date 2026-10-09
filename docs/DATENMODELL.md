# Datenmodell: Ist-Stand und Ziel

## Vorhandene Objekte in v0.8

| Ordner | `type` | Anzahl | Aufgabe |
|---|---|---:|---|
| works | work | 1 | Biblisches Werk |
| text-units | text_unit | 1 | Natürliche Texteinheit und Versbereich |
| studies | study | 1 | Pilotstudie mit Ergebnissen und offenen Fragen |
| sources | source / dataset | 5 | Quellenhinweise und externe Datensätze |
| editions | critical_edition | 5 | Editionen (SBLGNT, WH, Tregelles, NA28, Robinson-Pierpont) |
| text-samples | text_sample | 1 | Nicht verifizierte Arbeitstranskription (historisch) |
| tokens | token_set | 17 | SBLGNT-Wörter Markus, ein Set je Kapitel (11 286 Tokens); dazu das abgelöste Pilot-Set Mk 3,22–30 (`deprecated`) |
| annotations | annotation_set | 17 | Sprachliche Annotation je Token: MACULA Greek je Kapitel; MorphGNT für Mk 3,22–30 (Pilot) |
| counts | lemma_count | 2 | Zählungen: ganzes Markusevangelium (MACULA), Pilot (MorphGNT) |
| variants | variant | 931 | 929 Stellen auf Editionsebene aus dem SBLGNT-Apparat (`variants/sblgntapp-mrk/`); 2 Stellen mit berichteten Handschriften (Arbeitsnotizen) |
| assessments | assessment_set | 16 | Gesichertheitsbewertungen je Kapitel nach einer offengelegten Methode |
| methods | assessment_method | 1 | Beschreibung einer Bewertungsmethode mit Annahmen und Grenzen |
| findings | finding | 4 | Textliche/literarische/textkritische Befunde |
| decisions | editorial_decision | 1 | Frühere Lesartpräferenz (historisch; künftig als Bewertung) |
| translations | translation | 2 | Eigene deutsche Arbeitsübersetzung: Mk 3,29 (v0.5) und Mk 3,22–30 (v0.7) |
| alignments | alignment | 2 | Wort-/Phrasenzuordnungen; Mk 3,22–30 vollständig über Token-IDs (`coverage: complete`) |
| interpretations | interpretation | 2 | Alternative Verständnisse |
| principles | principle | 1 | Abgeleitetes Prinzip |
| contexts | context | 2 | Historischer und heutiger Kontext |
| applications | application | 1 | Kontextabhängige Anwendung |
| topics | topic | 2 | Inhaltliche Themen |
| relations | relation | 3 | Beziehungen zu Parallelstellen |
| questions | open_question | 1 | Offene Forschungsfrage |
| tags | tag | 6 | Kontrollierte Tags |

Gesamt: 1025 Datensätze im freien Kern (`data/`), 0 in der Studienschicht (`data-nc/`).

## Schichten des Texts
1. **Token** (`token_set`): die Wörter einer Edition in ihrer Reihenfolge, mit stabiler ID `TOK-<EDITION>-<BUCH>-<KKK>-<VVV>-<NNN>`. «text» unverändert aus der Edition (inkl. Interpunktion und Apparatzeichen), «word» ohne diese Zeichen. Keine Deutung.
2. **Annotation** (`annotation_set`): sprachliche Angaben je Token-ID aus einer bestimmten Quelle (MACULA, MorphGNT …). Mehrere Annotationen desselben Tokens können nebeneinander bestehen und sich unterscheiden.
3. **Variante** (`variant`): Lesarten einer Stelle, an Tokens gebunden (`base_tokens`), mit Bezeugung durch Editionen oder Handschriften (`evidence_level`).
4. **Bewertung** (`assessment_set` + `assessment_method`): Gesichertheit der Lesarten nach einer offengelegten Methode; mehrere Methoden nebeneinander, keine Entscheidung über richtig/falsch. Siehe [GESICHERTHEIT.md](GESICHERTHEIT.md).
5. **Übersetzung und Zuordnung** (`translation`, `alignment`): bis auf das Token rückverfolgbar.

## Bestehende Referenzen
`work`, `primary_unit`, `subject`, `based_on`, `derived_from`, `principle`, `context`, `outputs`, `evidence_objects`, `related`, `from`, `edition`, `imported_records`, `supersedes` und `tags` verknüpfen Datensätze. `VAR-…:R1` referenziert eine Lesart innerhalb eines Variantenobjekts. Bibelstellen (`reference`, `to_ref`, `range`, `evidence_refs`, `imported_scope`) folgen seit v0.6 einheitlich [BIBELSTELLEN.md](BIBELSTELLEN.md). Varianten (`base_tokens`) und Alignments (`source_tokens`) verweisen seit v0.7 auf SBLGNT-Token-IDs; Annotationen (`annotates`, Einträge je Token-ID) und Bewertungen (`assesses`, `results[].reading`) seit v0.8. Der Validator prüft alle diese Verweise und bei `coverage: complete` die lückenlose Zuordnung.

Beispielkette: `FIND-MRK-0001` → `INT-MRK-0001` → `PRIN-MRK-0001` → `APP-MRK-0001`; die Anwendung verweist auf `CTX-CH-DE-2026`. Die textkritische Entscheidung und die Arbeitsübersetzung referenzieren eine bestimmte Lesart.

## Noch nicht implementiert
Eigene Handschriften-/Zeugenobjekte mit Korrekturschichten; eigenständige Lemma-/Lexikonobjekte; Argumente/Gegenargumente als eigene Objekte; einheitliche Quellenbelege mit genauen Fundstellen; durchgängige Zeit- und Revisionsmetadaten; typspezifische Schemas; Versifikationstabelle; SQLite-Projektion; Benutzeroberfläche.

## Typnamen und Schema
Seit v0.6 sind die Typnamen kanonisch in `snake_case` (`study`, `text_unit`); das Schema listet alle verwendeten Typen und Statuswerte. Die Umstellung der v0.5-Daten (`studie`, `text-unit`) erfolgte per `scripts/migrations/v0_6.py` und ist in `provenance/migrations/2026-10-09-v0.6.json` protokolliert. Das Schema ist weiterhin generisch; typspezifische Pflichtfelder folgen.
