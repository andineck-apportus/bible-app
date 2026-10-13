# Datenmodell: Ist-Stand und Ziel

## Vorhandene Objekte in v0.27

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

Gesamt: 3441 Datensätze im freien Kern (`data/`), 0 in der Studienschicht (`data-nc/`).

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
Eigene Handschriften-/Zeugenobjekte mit Korrekturschichten; eigenständige Lemma-/Lexikonobjekte; Argumente/Gegenargumente als eigene Objekte; einheitliche Quellenbelege mit genauen Fundstellen; durchgängige Zeit- und Revisionsmetadaten; typspezifische Schemas; Umrechnung zwischen Versifikationen (Daten vorhanden, Auswertung offen); SQLite-Projektion.

## Übersetzungsschichten (mehrere Sprachen und Kulturen)
Ziel: aus den Urtexten und den erarbeiteten Artefakten (Wortzuordnung, Entscheidungen, Lesarten, Befunde, Hintergrund) in beliebige Sprachen und kulturelle Kontexte übersetzen. Jede Fassung ist ein eigener `translation`-Datensatz mit `language` (BCP-47, z. B. `de-CH`, `gsw-u-sd-chzh` für Zürichdeutsch), `language_label_de`, `target_context` (ein `context`-Datensatz: Ort, Sprache, Zielgruppe, Zeit), `orthography_de`, `register_de`, `method_de`, `decisions`, `alternatives` und einer eigenen Wortzuordnung (`alignment` mit `target_language`). Sie wird aus dem Urtext übersetzt; `control_translation` nennt die hochdeutsche Kontrollfassung. `review_de` hält fest, ob und von wem die Sprache geprüft wurde. Die Studienprojektion liefert die Schichten unter `layers` (Standard `de`); der Lesestrom bietet sie als «Lesetext» an. Vorhanden: Hochdeutsch (wörtlich) und Züridüütsch (Dieth-Schreibung) für Mt 6,5–15, Lk 11,1–4 und Mk 3,20–35. Titel und Zusammenfassungen der Texteinheiten in weiteren Sprachen stehen seit v0.31 als Lokalisierungen (Felder `title`, `summary_de`), nicht mehr im Original.

**Feldnamen (seit v0.31):** Felder, deren Inhalt in der Sprache der Schicht steht, haben sprachneutrale Namen: in `alternatives` `from_text`, `to_text`, `note`, `readings` (`{grc, text, note}`), `origin`; in `decisions` `more_literal`, `other_options`, `note`; `alternatives_origin_note`; in Wortzuordnungen `note`. Felder mit Endung `_de` sind Hochdeutsch: die Originale der Erklärtexte (Hochdeutsch ist deren Ausgangs- und Kontrollsprache) und die Dokumentation für das Team (`method_de`, `authorship_de`, `review_de` …). Eine Übersetzung eines `_de`-Erklärtexts ist eine Lokalisierung.

**Vorrang:** Arbeitsübersetzungen derselben Sprache dürfen sich nicht überschneiden (Validator); eine überholte Fassung wird `deprecated`. Welche Abschnitte ausgearbeitet sind, ergibt sich aus den Daten (Texteinheit oberster Ebene mit Arbeitsübersetzung).

## Lokalisierungen (`localization`)
Erklärende Inhalte (Befunde, Deutungen, Grundsätze, Anwendungen, Fragen, Hintergrund, Zusammenfassungen) werden nicht im Originaldatensatz übersetzt, sondern je Sprache in einem eigenen Datensatz `data/localizations/<BCP-47>/<ID>.json`: `localizes` (ID des Originals), `language`, `target_context`, `fields` (gleiche Feldnamen wie im Original, z. B. `claim_de`; bei `terms` eine Liste der Bedeutungen in derselben Reihenfolge), `source_fingerprint` (SHA-256, 16 Zeichen, je Feld über den JSON-Wert des Originals), `authorship_de`, `review_de`, `revision_log`. Der Validator prüft, dass jedes Feld im Original existiert und Typ/Listenlänge passen; ein Feld, dessen Original sich seit der Übersetzung geändert hat, gilt als veraltet (WARN) und wird von `scripts/localizations.py` nicht ausgeliefert. So bleibt jede Sprache unabhängig revidierbar, und ein neuer Quellenstand oder eine neue Deutung überschreibt keine Übersetzung stillschweigend. Projektion: `i18n: {Sprachgrundtag: {Feld: Wert}}` je Objekt; im Lesestrom liegen die Lokalisierungen in den Sprachpaketen. Formatänderungen am Original (z. B. Migration v0.31) führen den Fingerabdruck nach und vermerken das im `revision_log` der Lokalisierung.

## Vergleichsübersetzungen je Sprache
Vergleichsübersetzungen (`translation_kind: historical_comparison`) tragen `language` wie jede Übersetzung. Welche davon eine Schicht zeigt, bestimmt deren Zielkontext: `comparison_languages` (Liste von Sprachgrundtags in Anzeigereihenfolge) im `context`-Datensatz; ohne Angabe nur die eigene Sprache. Eine neue Sprache bekommt so eigene Vergleichsfassungen, ohne die bestehenden zu berühren.

## Übersetzungsentscheidungen und Vergleichsübersetzungen
Eigene Arbeitsübersetzungen (`translation_kind: literal_original_working`) können `decisions` führen: je Stelle der deutsche Zieltext (`target`, muss im Übersetzungstext vorkommen), die Art (`literal` wörtlich, `adapted` sprachlich angepasst, `interpretive` Deutungsentscheidung, `traditional` folgt der vertrauten Wiedergabe), optional eine wörtlichere Fassung (`more_literal`), weitere Möglichkeiten (`other_options`) und eine Begründung (`note`). Der Validator prüft Art und Zieltext. Ältere gemeinfreie deutsche Übersetzungen liegen als `translation_kind: historical_comparison` nur für die ausgearbeiteten Verse vor und dienen ausschliesslich dem Vergleich.

## Fachwörter (`terms`)
Hintergrundnotizen und Deutungen können `terms` führen: Wörter der Ursprache, auf die der Text sich bezieht, mit `lang` (grc, heb, arc, lat), `word` (Originalschrift), `translit` (Pflicht ausser bei Griechisch, das automatisch umgeschrieben wird) und `de` (Bedeutung). Der Lesestrom zeigt sie mit Umschrift und Anhören-Knopf; griechische Einschübe im Fliesstext erhalten dasselbe automatisch.

## Querverweise und verlinkte Stellen
Querverweise liegen als `crossref_set` vor; der Lesestrom bettet für die ausgearbeiteten Kapitel je Vers die zehn bestbewerteten ein und zeigt sie im Versblatt. Bibelstellen im Fliesstext stehen seit v0.31 als sprachneutrale Marken `[[MAT.6.34]]` bzw. `[[MRK.3.28-MRK.3.29]]` (Konvention in [BIBELSTELLEN.md](BIBELSTELLEN.md), Werkzeug `scripts/prose_refs.py`). Die App zeigt sie im Schreibstil der Lesesprache (im eigenen Buch ohne Buchname, Folgestellen verkürzt) und macht sie antippbar; Ziele ausserhalb der 66 Bücher (z. B. Sirach, Tobit) bleiben Text. Ein Sprung bietet den Rückweg zur Ausgangsstelle an. Der Validator prüft die Marken und meldet Stellen in deutscher Schreibweise, die noch nicht markiert sind.

## Studienprojektion und Pakete
Der Lesestrom erhält die ausgearbeiteten Abschnitte über `scripts/project_study.py` (alle Schlüssel kanonische Bibelstellen); welche Abschnitte ausgearbeitet sind, ermittelt `worked_sections()` aus den Daten. `scripts/build_reading_stream.py` teilt die Projektion auf:
- **Kern** (in `index.html`): Navigation, Abschnitte mit hochdeutschen Titeln, Sprachschichten ohne Inhalt, hochdeutsche Zusammenfassungen, Quellenbeschreibungen, Paketverzeichnis.
- **`b/<BUCH>`** (sprachunabhängig): griechische Wörter, Varianten, Befunde/Deutungen/Grundsätze/Anwendungen/Fragen/Beziehungen (Original), Hintergrund, Querverweise, Handschriften-Zuordnungen.
- **`l/<Sprache>/<BUCH>`**: Übersetzungsschicht des Buchs (Text, Entscheidungen, Lesarten-Alternativen, Wortzuordnung), Vergleichsübersetzungen dieser Sprache, Lesarten-Erklärungen, Lokalisierungen der Objekte des Buchs.
- **`l/<Sprache>/common`**: lokalisierte Titel und Zusammenfassungen der Abschnitte und aller Zusammenfassungen.

Ausgaben: `build/reading-stream/` (Kern + Pakete als `.json.gz`, deterministisch; zum Veröffentlichen), `build/reading-stream-txt/` (dieselben Pakete als gzip in Base64, `.gz.txt`, für Hosts ohne Binärdateien) und `app/reading-stream/index.html` (Einzeldatei mit allen Paketen eingebettet; offline und für die Tests). Die App lädt Pakete erst, wenn ein Eintrag eines Buchs gezeigt oder die Sprache gewechselt wird (Lesetext, dessen Vergleichssprachen und Hochdeutsch als Rückfall), und entpackt sie im Browser. Eine neue Sprache oder ein neues Buch fügt nur Pakete hinzu; der Kern wächst mit der Zahl der ausgearbeiteten Abschnitte, nicht mit deren Inhalt.

## Versifikation (`versification_map`)
`data/versification/VRS-TVTMS-<BUCH>.json` enthält die Zuordnungen zwischen den Zähltraditionen (Hebräisch, Latein, Griechisch, Englisch KJV/NRSV und weitere) aus TVTMS (STEPBible, CC BY 4.0), wörtlich mit Handlung (`action`) und den Bedingungen (`tests`), unter denen eine Zeile gilt; wo eindeutig zusätzlich kanonisch (`source_ref`, `standard_ref`, Teilvers `source_sub`/`standard_sub`). Die Umrechnung selbst ist noch nicht umgesetzt: Sie braucht die Verszahlen bzw. den Text der jeweiligen Ausgabe, um die Bedingungen auszuwerten. Siehe [BIBELSTELLEN.md](BIBELSTELLEN.md).

## Typnamen und Schema
Seit v0.6 sind die Typnamen kanonisch in `snake_case` (`study`, `text_unit`); das Schema listet alle verwendeten Typen und Statuswerte. Die Umstellung der v0.5-Daten (`studie`, `text-unit`) erfolgte per `scripts/migrations/v0_6.py` und ist in `provenance/migrations/2026-10-09-v0.6.json` protokolliert. Das Schema ist weiterhin generisch; typspezifische Pflichtfelder folgen.
