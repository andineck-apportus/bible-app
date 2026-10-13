# Datenmodell: Ist-Stand und Ziel

## Vorhandene Objekte in v0.23

| Ordner | `type` | Anzahl | Aufgabe |
|---|---|---:|---|
| works | work | 3 | Biblisches Werk |
| text-units | text_unit | 9 | Natürliche Texteinheiten: Mk 3,20–35 (Abschnitt und drei Teile), Mt 6,5–15 (Abschnitt und drei Teile), Lk 11,1–4 |
| studies | study | 2 | Pilotstudie mit Ergebnissen und offenen Fragen |
| sources | source / dataset | 6 | Quellenhinweise und externe Datensätze |
| editions | critical_edition | 8 | Editionen (SBLGNT, WH, Tregelles, NA28, Robinson-Pierpont) |
| text-samples | text_sample | 1 | Nicht verifizierte Arbeitstranskription (historisch) |
| tokens | token_set | 69 | SBLGNT-Wörter von Matthäus, Markus und Lukas, ein Set je Kapitel (Markus 11 286 Tokens, Matthäus 18 329, Lukas 19 446); dazu das abgelöste Pilot-Set Mk 3,22–30 (`deprecated`) |
| annotations | annotation_set | 69 | Sprachliche Annotation je Token: MACULA Greek je Kapitel (Mt, Mk, Lk); MorphGNT für Mk 3,22–30 (Pilot) |
| counts | lemma_count | 4 | Zählungen: ganzes Markusevangelium (MACULA), Pilot (MorphGNT) |
| variants | variant | 2884 | Stellen auf Editionsebene aus dem SBLGNT-Apparat: Markus 929, Matthäus 820, Lukas 1133 (`variants/sblgntapp-*/`); 2 Stellen mit berichteten Handschriften (Arbeitsnotizen) |
| assessments | assessment_set | 68 | Gesichertheitsbewertungen je Kapitel nach einer offengelegten Methode |
| methods | assessment_method | 2 | Beschreibung einer Bewertungsmethode mit Annahmen und Grenzen |
| findings | finding | 11 | Textliche/literarische/textkritische Befunde |
| decisions | editorial_decision | 1 | Frühere Lesartpräferenz (historisch; künftig als Bewertung) |
| translations | translation | 6 | Eigene deutsche Arbeitsübersetzung: Mk 3,29 (v0.5), 3,22–30 (v0.7), 3,20–21 und 3,31–35 (v0.9), mit `alternatives` |
| alignments | alignment | 4 | Wort-/Phrasenzuordnungen; Mk 3,22–30 vollständig über Token-IDs (`coverage: complete`) |
| interpretations | interpretation | 10 | Alternative Verständnisse |
| principles | principle | 2 | Abgeleitetes Prinzip |
| contexts | context | 5 | Historischer Kontext (Galiläa um 30; erste Leserschaft des Markus um 70) und heutiger Kontext |
| applications | application | 2 | Kontextabhängige Anwendung |
| topics | topic | 2 | Inhaltliche Themen |
| relations | relation | 10 | Beziehungen zu Parallelstellen |
| questions | open_question | 3 | Offene Forschungsfrage |
| tags | tag | 11 | Kontrollierte Tags |
| navigation | navigation_structure | 1 | Kanon- und Zählgerüst für die Navigation: Testamente, Buchgruppen, Bücher mit Versen je Kapitel (protestantischer Kanon, KJV-Zählung als Testkonfiguration) |
| witnesses | witness | 15 | Textzeugen: sechs Majuskeln, die Papyri 𝔓45 und 𝔓75 sowie sieben Amulette bzw. Einzeltexte mit dem Vaterunser (Trismegistos-Nummer); mit Gregory-Aland-Nummer, Sigle, Datierung, Material, Aufbewahrungsort, kurzer Beschreibung und Links zu Abbildungen/Katalog |
| witness-texts | witness_transcription | 46 | Transkriptionen je Textzeuge (`witness`) oder Ausgabe (`edition`) für Matthäus, Markus und Lukas, Format MES, Herkunft mit Commit und SHA-256 (CNTR, CC BY-SA 4.0) |
| witness-readings | witness_reading_set | 3 | Maschinelle Zuordnung «welche Handschrift/Ausgabe hat welche Lesart» für Mk 3,20–35, Mt 6,5–15 und Lk 11,1–4, getrennt nach Erstschrift und Korrektur, mit Textausschnitt (`METHOD-AUTO-COLLATION-V1`) |
| background | background_note | 25 | Hintergrund damals zu Mk 3,20–35 und zum Vaterunser: Zeit, Ort, Kultur, Religion; je mit `context`, `subject`, `reference`, `topic_de`, `text_de`, `confidence`, optional `uncertain_de`, `evidence_refs` (Bibelstellen) und `sources_de` (ausserbiblische Fundstellen, nur zitiert) |
| crossrefs | crossref_set | 66 | Querverweise je Ausgangsbuch (OpenBible.info, CC BY): je Vers die Ziele mit Stimmen, nach Stimmen sortiert; Zielbereiche über Buchgrenzen geteilt und markiert. Der Validator prüft alle Stellen. |
| summaries | summary | 85 | Zusammenfassungen je Ebene (Bibel, Testament, Gruppe, Buch, Kapitel); `scope`, `reference`, `group`, `text_de`; alle `draft` |

Gesamt: 3435 Datensätze im freien Kern (`data/`), 0 in der Studienschicht (`data-nc/`).

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

## Übersetzungsentscheidungen und Vergleichsübersetzungen
Eigene Arbeitsübersetzungen (`translation_kind: literal_original_working`) können `decisions` führen: je Stelle der deutsche Zieltext (`target`, muss im Übersetzungstext vorkommen), die Art (`literal` wörtlich, `adapted` sprachlich angepasst, `interpretive` Deutungsentscheidung, `traditional` folgt der vertrauten Wiedergabe), optional eine wörtlichere Fassung (`more_literal_de`), weitere Möglichkeiten (`other_options_de`) und eine Begründung. Der Validator prüft Art und Zieltext. Ältere gemeinfreie deutsche Übersetzungen liegen als `translation_kind: historical_comparison` nur für die ausgearbeiteten Verse vor und dienen ausschliesslich dem Vergleich.

## Fachwörter (`terms`)
Hintergrundnotizen und Deutungen können `terms` führen: Wörter der Ursprache, auf die der Text sich bezieht, mit `lang` (grc, heb, arc, lat), `word` (Originalschrift), `translit` (Pflicht ausser bei Griechisch, das automatisch umgeschrieben wird) und `de` (Bedeutung). Der Lesestrom zeigt sie mit Umschrift und Anhören-Knopf; griechische Einschübe im Fliesstext erhalten dasselbe automatisch.

## Querverweise und verlinkte Stellen
Querverweise liegen als `crossref_set` vor; der Lesestrom bettet für die ausgearbeiteten Kapitel je Vers die zehn bestbewerteten ein und zeigt sie im Versblatt. Bibelstellen in deutschen Erklärtexten (z. B. «Mk 14,36», «Jes 63,16; 64,7», «Ex 16,4.19–20», relativ «(6,14–15)») erkennt die App beim Anzeigen und macht sie antippbar; Ziele ausserhalb der 66 Bücher (z. B. Sirach) bleiben Text. Ein Sprung bietet den Rückweg zur Ausgangsstelle an.

## Studienprojektion
Der Lesestrom erhält die ausgearbeiteten Abschnitte über `scripts/project_study.py` (alle Schlüssel kanonische Bibelstellen). Neue Abschnitte werden in `scripts/build_reading_stream.py` (Liste `SECTIONS`) eingetragen; die Daten selbst bleiben in `data/`.

## Typnamen und Schema
Seit v0.6 sind die Typnamen kanonisch in `snake_case` (`study`, `text_unit`); das Schema listet alle verwendeten Typen und Statuswerte. Die Umstellung der v0.5-Daten (`studie`, `text-unit`) erfolgte per `scripts/migrations/v0_6.py` und ist in `provenance/migrations/2026-10-09-v0.6.json` protokolliert. Das Schema ist weiterhin generisch; typspezifische Pflichtfelder folgen.
