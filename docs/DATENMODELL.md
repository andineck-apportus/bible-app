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
| lexica | lexicon | 4 | Wörterbücher (seit v0.39): UBS Dictionary of the Greek NT und of Biblical Hebrew (CC BY-SA 4.0), STEPBible TBESG/TBESH (Kurzglossen, CC BY 4.0); nur Einträge für Wörter der importierten Bücher |
| tagged-alignments | tagged_text_alignment | 11 | Zuordnung getaggter Fremdtexte zu unseren Tokens (seit v0.39): STEPBible TAGNT (Ausgaben je Wort, NT) und TAHOT (Ketiv/Qere, dStrong je Morphem, AT) |

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
Eigene Handschriften-/Zeugenobjekte mit Korrekturschichten; eigene Lemma-Objekte (Wörterbücher als `lexicon` seit v0.39, aber ohne projektweite Lemma-ID); Argumente/Gegenargumente als eigene Objekte; einheitliche Quellenbelege mit genauen Fundstellen; durchgängige Zeit- und Revisionsmetadaten; typspezifische Schemas; Umrechnung zwischen Versifikationen (Daten vorhanden, Auswertung offen); SQLite-Projektion.

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

## Hintergrund der oberen Ebenen
`background_note` mit `scope`: `bible`, `testament` (+ `testament`: OT/NT), `book_group` (+ `group`: ID aus der Navigation) oder `book` (+ `reference` = Buchcode); ohne `scope` gehört eine Notiz zu einem Abschnitt (`subject`, `reference`). Kontexte für grosse Zeiträume: `CTX-HIST-BIBLE-FORMATION`, `CTX-HIST-ISRAEL-IRON-PERSIAN`, `CTX-HIST-SECOND-TEMPLE`, `CTX-HIST-EARLY-CHRISTIANITY`. Im Lesestrom: Paket `b/_overview`, Knopf «Geschichte» an den Einträgen der oberen Ebenen.

## Versifikation (`versification_map`)
`data/versification/VRS-TVTMS-<BUCH>.json` enthält die Zuordnungen zwischen den Zähltraditionen (Hebräisch, Latein, Griechisch, Englisch KJV/NRSV und weitere) aus TVTMS (STEPBible, CC BY 4.0), wörtlich mit Handlung (`action`) und den Bedingungen (`tests`), unter denen eine Zeile gilt; wo eindeutig zusätzlich kanonisch (`source_ref`, `standard_ref`, Teilvers `source_sub`/`standard_sub`). Hebräisch → KJV ist umgesetzt (`scripts/versification.py`); umgerechnete `token_set` tragen `versification: "KJV"` und je Token `source_reference`/`source_word_no`, Psalmüberschriften `title: true`. Siehe [BIBELSTELLEN.md](BIBELSTELLEN.md).

## Hebräischer Text (seit v0.33)
Hebräische `token_set` (`TOKSET-WLC-<BUCH>-<KAP>`, Ausgabe `ED-WLC`) zerlegen nach MACULA Hebrew in **Morpheme**: Token-ID `TOK-WLC-OBA-001-VVV-NNN`, `position` = Morphem im Vers, `word_no` = Wort im Vers, `text` mit folgendem Maqqef bzw. Sof Pasuq, `word` ohne, `after` = Trennzeichen. Morpheme ohne eigene Schreibung (z. B. der in der Präposition aufgegangene Artikel) stehen in `implicit_morphs`. Wortzuordnungen verweisen auf Morpheme; die App fasst sie zu Wörtern zusammen. Übersetzungsentscheidungen nennen das hebräische Wort in `heb` (statt `grc`); der Validator prüft es über die Konsonanten gegen den Text. Umschrift: lesefreundliche Lesehilfe (`scripts/hebrew_translit.py`), keine wissenschaftliche Transliteration (diese steht aus MACULA in der Annotation).

## Autorenwerkzeuge
`scripts/authoring/_lib.py` erzeugt Übersetzungstext und Wortzuordnung aus einer gemeinsamen Auszeichnung je Vers (`Wort{3}`, `[mehrere Wörter]{3,4}`, `{n:idiom}`, `~n(Hinweis)` für nicht eigens Wiedergegebenes); so können Text und Zuordnung nicht auseinanderlaufen. Fehlende oder doppelt zugeordnete Tokens brechen ab. Geschrieben wird nur bei inhaltlicher Änderung; die vorige Fassung der geänderten Felder kommt mit Datum und Grund ins `revision_log`. `hintergrund_buecher.py` schreibt den Hintergrund auf Buchebene aus Datenmodulen je Buchgruppe (`scripts/authoring/buecher/`). `_study.py` schreibt die Studieninhalte eines Buchs samt Züridüütsch-Lokalisierungen aus einer Konfiguration.

## Wörterbücher, Ausgaben je Wort, Ketiv/Qere (seit v0.39)
**Schemaänderung:** zwei neue Typen in `schema/record.schema.json` (Titel jetzt «v0.9»): `lexicon` und `tagged_text_alignment`. Bestehende Datensätze sind nicht betroffen; es gibt nichts zu migrieren.

- **`lexicon`** (`data/lexica/LEX-<QUELLE>-<SPRACHE>.json`): `title`, `language` (`grc`, `hbo`), `gloss_language` (`en`), `key` (wie die Einträge verschlüsselt sind), `source` (Repository, Commit, Pfad, SHA-256, Lizenz, Attribution, `changes_de`), `counts` und `entries` (Schlüssel → Eintrag). UBS: Schlüssel `MainId`; Eintrag mit `lemma`, `strong` (StrongCodes), `pos`, `senses` (je Bedeutung `lexid`, `code` (Louw-Nida-Nummer beim Griechischen), `domains`, `subdomains`, `definition`, `glosses`, bei mehreren Bedeutungen `occurrences` = Stellen in den importierten Büchern in der Zählung von UBS, `ai_generated`, falls UBS die Bedeutung so markiert). STEPBible: Schlüssel dStrong; Eintrag mit `estrong`, `ustrong`, `lemma`, `translit`, `morph`, `gloss`, `relation`. Der Wörterbuchtext bleibt englisch; die App beschriftet ihn deutsch und nennt die Sprache.
- **`tagged_text_alignment`** (`data/tagged-alignments/TALIGN-<TAGNT|TAHOT>-<BUCH>.json`): `kind` (`edition_presence` bzw. `ketiv_qere`), `book`, `aligned_to`, `source`, `method_de`, `entries` (Schlüssel = unsere Token-ID), `unmatched` (nicht zugeordnete Tokens und Fremdwörter; nie geraten), `counts`. TAGNT: je SBLGNT-Token mit Abweichung `src` (TAGNT-Wort-ID), `type`, `editions` (gedruckte Ausgaben, die das Wort haben), `moved`, `alt` (Bedeutungsvarianten mit Ausgaben), `spelling`, `dstrong`, `grammar`, Kennzeichen `by_position`, `sbl_not_listed`, `via_variant`; `extra_words` = Wörter anderer Ausgaben, die SBLGNT nicht hat, verankert am vorangehenden Token (`after`). Fehlt `editions`, steht das Wort in allen acht Hauptausgaben. TAHOT: `entries` je Wort mit Ketiv (`ketiv.text`, `translit`, `gloss_en`, `tags`), `qere`, `leningrad`, `tokens`; `ketiv_without_qere` (geschrieben, nicht gelesen; in MACULA nicht enthalten) und `dstrong` (dStrong je Morphem).
- **Zuordnung zu den Wörtern** (Projektion, `scripts/project_study.py`): Griechisch über MACULA-Lemma bzw. Strong-Nummer; Hebräisch über Strong-Nummer (mit und ohne Buchstabenzusatz) bzw. dStrong aus TAHOT, aber nur, wenn die Grundform des Eintrags dieselben Konsonanten hat wie das MACULA-Lemma (MACULA nummeriert Vorsilben und Endungen anders als UBS/STEPBible). «Hier» markiert Bedeutungen, deren Stellenliste im Wörterbuch den Vers enthält (Hebräisch in hebräischer Zählung). Der Lesestrom erhält die Einträge nur in den Paketen `b/<BUCH>` (`lex`, `ketiv`, `kq_only`, `ed_extra`), der Kern bleibt klein.
- **Grenzen:** Ausgabenbefund ist kein Handschriftenbefund. Ketiv-Vokale sind von Tyndale House ergänzt. Die Wahl einer UBS-Bedeutung «hier» ist die Einordnung des Wörterbuchs, keine eigene Prüfung. Alles `imported_unreviewed`.
- Importer: `scripts/import_stepbible_tagged.py` (zuerst), dann `scripts/import_lexica.py`; beide prüfen die SHA-256 der Quelldateien und schreiben Berichte nach `reports/stepbible-tagged-<BUCH>.json`. Nach neuen Büchern in `data/tokens/` beide erneut ausführen.

## Typnamen und Schema
Seit v0.6 sind die Typnamen kanonisch in `snake_case` (`study`, `text_unit`); das Schema listet alle verwendeten Typen und Statuswerte. Die Umstellung der v0.5-Daten (`studie`, `text-unit`) erfolgte per `scripts/migrations/v0_6.py` und ist in `provenance/migrations/2026-10-09-v0.6.json` protokolliert. Das Schema ist weiterhin generisch; typspezifische Pflichtfelder folgen.

## Bildsprache (seit v0.55, Lexikon und Bildaufträge seit v0.56)
**Schemaänderungen:** v0.10 führte `illustration_style` und `illustration` ein, v0.11 `figure` und `illustration_brief` (Titel jetzt «v0.11»). Rein additiv; bestehende Datensätze sind nicht betroffen, es gibt nichts zu migrieren. Ablauf und Regeln: [BILDSPRACHE.md](BILDSPRACHE.md).

- **`figure`** (Bildlexikon, `data/illustrations/lexicon/FIG-*.json`, stilunabhängig): `kind` (`divine`, `person`, `role`, `group`, `object`, `place`, `action`, `sign`), `names` (de/en), `identity_de`, `traits` (je `trait_de`, `basis` = `text` | `tradition` | `design`, optional `ref`, `note_de`), `palette`, `rules_de`, `distinct_from`, `appears_in`; Mundart als `localization`. Werkzeug: `scripts/authoring/bildlexikon.py`.
- **`illustration_brief`** (Bildauftrag, `data/illustrations/briefs/BRIEF-<STELLE>.json`, stilunabhängig): `level`, `reference`, `target`, `translation`, `panels` (je `n`, `reference`, `figures`, `objects`, `signs`, `speech` = Liste von `{from, to, icons}`, `action_de`), `interpretation_note_de`, `basis` (Fingerabdrücke der Verse je Feld und der Zusammenfassung des Ziels). Alle IDs müssen im Lexikon stehen. Werkzeug: `scripts/authoring/bildauftraege.py` (ohne `BIBLE_BRIEF_CONFIRM=1` bleiben die alten Fingerabdrücke stehen).
- **`illustration_style`** (`data/illustrations/styles/ILLSTYLE-<STIL>.json`): `key` (z. B. `symbol`), `labels` (de/en), `description_de`, `library` (SVG-Bibliothek), `renderings` (Lexikon-ID → `symbol`, `viewbox`: wie dieser Stil den Eintrag zeichnet), `license`, `authorship_de`.
- **`illustration`** (`data/illustrations/<stil>/ILL-<STIL>-<STELLE>.json` mit Zeichnung `<ID>.svg` daneben): `style`, `brief`, `level`, `reference`, `target`, `file`, `depicts` (Lexikon-IDs mit Darstellung im Stil), optional `not_rendered`, `alt_de`, `check` (Blindtest: `date`, `method_de`, `result_de`, `open_de`, `limits_de`), `license`, `authorship_de`; Mundart als `localization`.
- Bilder sind **bildliche Deutung**, nicht Text: Sie werden als solche angezeigt (Legende mit Hinweis) und ersetzen die Zusammenfassung nicht. Mehrere Stile je Stelle sind vorgesehen; der Lesestrom zeigt den gewählten Stil.
- Der Validator prüft Datei, Stil, Darstellung jeder gezeigten Figur im Stil, Bildauftrag, Lexikon-IDs, Stellen, Ziel und die Fingerabdrücke (Fehler «Bildauftrag veraltet», wenn sich der Text geändert hat). Der Lesestrom bettet Lexikon und Bibliothek in den Kern ein; Bilder liegen im Paket ihres Buchs (Buchebene in `b/_overview`).
