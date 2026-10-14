# Lizenzen

## Grundsatz (festgelegt 2026-10-09)

Das Projekt soll **so frei wie möglich** sein. Betreiber der App ist ein gemeinnütziger Verein; das Projekt verfolgt keinen Erwerbszweck, sondern will neues Wissen schaffen und zugänglich verbreiten.

Die Daten sind in **zwei Schichten** getrennt:

### 1. Freier Kern (`data/`)
- **Eigene Beiträge** des Projekts (Code, Dokumentation, eigene Datensätze, Übersetzungen, Wortzuordnungen, Bewertungen, Grafiken) stehen unter **CC0 1.0** ([LICENSE](LICENSE)): ohne Bedingung nutzbar, auch kommerziell.
- Übernommen werden Quellen unter **gemeinfrei, CC0, CC BY oder CC BY-SA**. Alle erlauben jede Nutzung einschliesslich kommerzieller.
- **CC BY-SA** verlangt, dass Bearbeitungen wieder unter CC BY-SA stehen. Das gilt nur für Dateien, die direkt aus einer solchen Quelle abgeleitet sind; sie sind unten aufgeführt. Bei gleichwertiger Wahl wird die freiere Quelle (CC0/CC BY) bevorzugt.
- Wer nur den freien Kern verwendet, darf alles frei weiterverwenden; Pflichten bestehen höchstens in Namensnennung (CC BY) bzw. gleicher Lizenz (CC BY-SA) für die betroffenen Dateien.

### 2. Studienschicht für nicht kommerzielle Nutzung (`data-nc/`)
- Quellen unter **nicht kommerziellen Lizenzen** (z. B. CC BY-NC, CC BY-NC-SA, Nutzungserklärungen wie bei CATSS) dürfen für den gemeinnützigen Betrieb verwendet werden.
- Sie liegen **ausschliesslich in `data-nc/`**, jeder Datensatz trägt Lizenz und Quelle. Sie werden nie in Dateien des freien Kerns übernommen oder mit ihnen vermischt.
- Kerndaten dürfen auf NC-Datensätze nicht verweisen; NC-Datensätze dürfen auf Kerndaten verweisen. So bleibt der Kern ohne NC-Daten vollständig nutzbar.
- Ergebnisse, die aus einem Vergleich mit NC-Daten entstehen (z. B. eine Gesichertheitsbewertung, die eine NC-Quelle berücksichtigt), gehören ebenfalls in `data-nc/`.
- In der App werden NC-Inhalte mit ihrer Lizenz angezeigt; ein Export «nur freier Kern» lässt sie weg.
- Vor einer Nutzung ausserhalb des gemeinnützigen Betriebs (z. B. Weitergabe an Dritte zu deren Zwecken) gelten die jeweiligen NC-Bedingungen.

### Nicht übernommen
- **Geschützte Quellen** (z. B. NA28, ECM, BHQ, BDAG, HALOT, moderne Bibelübersetzungen) werden nicht übernommen, nur mit Fundstelle zitiert, ausser es liegt eine schriftliche Lizenz vor.
- Daten «used with permission» ohne offene Lizenz (z. B. MARBLE-Wortbedeutungen in MACULA) werden nicht übernommen.

### Beiträge Dritter
Grafiken und Bilder von Personen, Institutionen und Künstlern werden unter CC0, CC BY oder CC BY-SA angenommen; die Lizenz steht im jeweiligen Datensatz.

## Übernommene Fremddaten im freien Kern

| Pfad | Inhalt | Quelle | Lizenz | Pflicht |
|---|---|---|---|---|
| `data/tokens/SBLGNT-{MAT,MRK,LUK,JHN,PHP,TIT,1JN,2JN,3JN}-*.json` | Griechischer Text von Matthäus, Markus, Lukas, Johannes, Philipper, Titus und 1–3 Johannes, in Wörter zerlegt | SBLGNT (Faithlife/SBLGNT) | CC BY 4.0, © 2010 Society of Biblical Literature und Logos Bible Software | Namensnennung |
| `data/variants/sblgntapp-*/VAR-SBLGNTAPP-*.json` | Variantenstellen aus dem SBLGNT-Apparat | Faithlife/SBLGNT | CC BY 4.0, wie oben | Namensnennung |
| `data/annotations/MACULA-SBLGNT-{MAT,MRK,LUK,JHN,PHP,TIT,1JN,2JN,3JN}-*.json`, `data/counts/SBLGNT-{MAT,MRK,LUK,JHN,PHP,TIT,1JN,2JN,3JN}.json` | Lemma, Morphologie, Syntaxrolle, Referenten, Glossen | MACULA Greek (Clear Bible / Biblica); Glossen: Berean Interlinear (gemeinfrei), Cherith Glosses for the Greek New Testament (Andi Wu, © 2023 Cherith Analytics, CC BY 4.0) | CC BY 4.0 | «MACULA Greek Linguistic Datasets, available at https://github.com/Clear-Bible/macula-greek/»; Cherith Glosses mit Autor nennen |
| `data/annotations/MORPHGNT-SBLGNT-MRK-003-022-030.json`, `data/counts/SBLGNT-MRK-003-022-030.json` | Lemma und Morphologie Mk 3,22–30 (Pilot) | MorphGNT 6.12 (J. K. Tauber) | **CC BY-SA 3.0** | Namensnennung; Bearbeitungen dieser Dateien unter CC BY-SA |
| `data/witness-texts/CNTR-*.json` | Transkriptionen der Handschriften 01 (א), 02 (A), 03 (B), 04 (C), 05 (D), 032 (W), weiterer Majuskeln (u. a. 029, 059, 0162, 0188, 0214, 0232, 0258, 0315, 0323), der Papyri 𝔓15/16 und 𝔓46 (Philipper), 𝔓32 (Titus), 𝔓9 (1 Joh), 𝔓45, 𝔓75, 𝔓88, 𝔓137 (Markus) sowie für Johannes 𝔓5, 𝔓6, 𝔓22, 𝔓28, 𝔓39, 𝔓52, 𝔓66, 𝔓90, 𝔓95, 𝔓106–𝔓109, 𝔓119–𝔓122 und 𝔓134, von Amuletten bzw. Einzeltexten (Trismegistos-Nummern) sowie der Ausgabentexte WH, RP, Stephanus, KJTR und SR für Matthäus, Markus, Lukas, Johannes, Philipper, Titus und 1–3 Johannes | Center for New Testament Restoration, Electronic Transcriptions (Alan Bunning), Commit `4e743a41a4b2` | **CC BY-SA 4.0** | «Alan Bunning, Center for New Testament Restoration»; Bearbeitungen unter CC BY-SA |
| `data/witness-readings/WREAD-CNTR-*.json` | Maschinelle Zuordnung der Handschriften zu den Lesarten, mit Textausschnitten aus den CNTR-Transkriptionen | abgeleitet aus den CNTR-Transkriptionen | **CC BY-SA 4.0** | wie oben |
| `data/tokens/WLC-{OBA,RUT}-*.json`, `data/counts/WLC-{OBA,RUT}.json` | Hebräischer Text von Obadja und Rut, in Morpheme zerlegt | Westminster Leningrad Codex (tanach.us) über MACULA Hebrew, `WLC/lowfat/31-Oba-001-lowfat.xml` bzw. `08-Rut-00{1-4}-lowfat.xml`, Commit `47db250b` (SHA-256 je Datei im Datensatz) | Text gemeinfrei; Zerlegung CC BY 4.0 | «MACULA Hebrew Linguistic Datasets, available at https://github.com/Clear-Bible/macula-hebrew/» |
| `data/annotations/MACULA-WLC-{OBA,RUT}-*.json` | Lemma, Morphologie, Syntaxrolle, Referenten, Glossen, akademische Umschrift, LXX-Entsprechung | MACULA Hebrew (Clear Bible / Biblica); Morphologie: OpenScriptures Hebrew Bible (CC BY 4.0); Glossen: Cherith Glosses for the Hebrew Old Testament (Andi Wu, © 2022 Cherith Analytics, CC BY 4.0) | CC BY 4.0 | wie oben; Cherith Glosses mit Autor nennen. **Nicht übernommen:** SDBH-Felder (`sdbh`, `lexdomain`, `coredomain`, `sensenumber`; «used with permission») und `mandarin` |
| `data/translations/TRANS-LUT1912-{TIT,OBA,RUT,PHP,JON,MRK,JHN,1JN,2JN,3JN}.json` | Lutherbibel 1912, Titus, Obadja, Rut, Philipper, Jona, Markus, Johannes und 1–3 Johannes (Vergleich) | seven1m/open-bibles, `deu-luther1912.osis.xml` (Commit `f257a355`) | gemeinfrei | — |
| `data/translations/TRANS-ELB1905-{TIT,OBA,RUT,PHP,JON,MRK,JHN,1JN,2JN,3JN}.json` | Elberfelder 1905, Titus, Obadja, Rut, Philipper, Jona, Markus, Johannes und 1–3 Johannes (Vergleich) | CrossWire-Modul GerElb1905 über scrollmapper/bible_databases (Commit `e1b254ce`) | gemeinfrei | — |
| `data/translations/TRANS-LUT1912-LP.json` | Lutherbibel 1912, nur Mt 6,9–13 und Lk 11,2–4 (Vergleich) | seven1m/open-bibles, `deu-luther1912.osis.xml` (Commit `f257a355`) | gemeinfrei | — |
| `data/translations/TRANS-ELB1905-LP.json` | Elberfelder 1905, nur Mt 6,9–13 und Lk 11,2–4 (Vergleich) | CrossWire-Modul GerElb1905 über scrollmapper/bible_databases (Commit `e1b254ce`) | gemeinfrei | — |
| `data/crossrefs/XREF-OPENBIBLE-*.json` | 344 799 Querverweise mit Nutzerstimmen, alle 66 Bücher | OpenBible.info Cross References (Kopie in scrollmapper/bible_databases, Commit `e1b254ce`, Stand 2024-11-04) | CC BY | «Cross references: OpenBible.info» |
| `data/versification/VRS-TVTMS-*.json` | Versifikations-Zuordnungen zwischen Hebräisch, Latein, Griechisch, Englisch und weiteren Traditionen (Teil «Expanded», 22 874 Zeilen; umformatiert, englische Notiztexte weggelassen) | STEPBible-Data, `Versification/TVTMS …`, Commit `cb4a117f`, SHA-256 `63058e0f…` | CC BY 4.0 | «Data created by www.STEPBible.org based on work at Tyndale House Cambridge»; Änderungen vermerkt (`source.changes_de`); STEPBible bittet, Korrekturen an sie zu melden und die Rohdaten nicht selbst weiterzuverbreiten (Umformatierung für die eigene Anwendung ist ausdrücklich erlaubt) |
| `data/lexica/LEX-UBS-DGNT-GRC.json` | Wörterbuch-Einträge Griechisch (Bedeutungen nach Bedeutungsfeldern, Kurzdefinition, Glossen; nur Wörter der importierten Bücher) | UBS Dictionary of the Greek New Testament v1.1 (englisch), github.com/ubsicap/ubs-open-license, Commit `33dcc8c6`, SHA-256 `d84bb907…`; Lizenztext LICENSE.md (SHA-256 `7abe19ec…`) im Wurzelordner und in `dictionaries/greek/` geprüft am 2026-10-14 | **CC BY-SA 4.0** | «UBS Dictionary of New Testament Greek, © United Bible Societies, 2023. Adapted from Semantic Dictionary of Biblical Greek: © United Bible Societies 2018-2023, which is adapted from Greek-English Lexicon of the New Testament: Based on Semantic Domains, Eds. J P Louw, Eugene Albert Nida © United Bible Societies 1988, 1989.»; Bearbeitungen unter CC BY-SA. Die MARBLE-Felder in MACULA (`domain`, `ln`, «used with permission») bleiben ausgeschlossen |
| `data/lexica/LEX-UBS-DBH-HEB.json` | Wörterbuch-Einträge Hebräisch (wie oben) | UBS Dictionary of Biblical Hebrew v0.9.3 (englisch), gleiches Repository und Commit, SHA-256 `3ed17584…`; Lizenztext in `dictionaries/hebrew/LICENSE.md` geprüft | **CC BY-SA 4.0** | «UBS Dictionary of Biblical Hebrew © United Bible Societies, 2023. Adapted from Semantic Dictionary of Biblical Hebrew © 2000-2023 United Bible Societies.»; Bearbeitungen unter CC BY-SA. **Unterschied zu MACULA:** Die SDBH-Felder in MACULA Hebrew (`sdbh`, `lexdomain`, `coredomain`, `sensenumber`) sind nur «used with permission» und bleiben ausgeschlossen; übernommen wird nur diese von UBS selbst unter CC BY-SA 4.0 veröffentlichte Ausgabe |
| `data/lexica/LEX-STEP-TBESG-GRC.json`, `data/lexica/LEX-STEP-TBESH-HEB.json` | Kurzglossen je (disambiguierter) Strong-Nummer mit Grundform, Umschrift, Kurzgrammatik | STEPBible-Data, `Lexicons/TBESG …`, `Lexicons/TBESH …`, Commit `93ec3621`, SHA-256 `312f723d…` bzw. `464dccad…` | CC BY 4.0 | «Data created by www.STEPBible.org based on work at Tyndale House Cambridge»; Änderungen in `source.changes_de`. **Nicht übernommen:** TBESH-Bedeutungsspalte (Abridged BDB, © Online Bible/Larry Pierce, laut Dateikopf nur mit Erlaubnis) und TBESG-Definitionsspalte (Abbott-Smith/Middle Liddell, Herkunft je Eintrag nicht sicher) |
| `data/tagged-alignments/TALIGN-TAGNT-*.json` | Je SBLGNT-Wort die gedruckten Ausgaben, die es enthalten (NA27/28, THGNT, SBL, WH, Tregelles, TR, Byz), Bedeutungs- und Schreibvarianten, Wörter anderer Ausgaben; maschinell zugeordnet | STEPBible-Data, `Translators Amalgamated OT+NT/TAGNT …`, Commit `93ec3621`, SHA-256 `ab8eaaeb…` (Mat–Jhn) bzw. `524e3237…` (Act–Rev) | CC BY 4.0 | wie oben; englische (nach Berean Study Bible) und spanische Übersetzungsspalten nicht übernommen |
| `data/tagged-alignments/TALIGN-TAHOT-*.json` | Ketiv-Formen (mit Vokalen von Tyndale House), Qere, dStrong je Morphem für Rut, Obadja, Jona; maschinell zugeordnet | STEPBible-Data, `Translators Amalgamated OT+NT/TAHOT …`, Commit `93ec3621`, SHA-256 `195fee1d…` (Jos–Est) bzw. `f3ded203…` (Isa–Mal) | CC BY 4.0 | wie oben |
| `archive/packages/` | Unveränderte frühere Projektpakete v0.1–v0.5 | Projekt | CC0 1.0, soweit eigene Inhalte | — |

Angaben zu Datierung, Fundort und Sammlung der Amulette (`data/witnesses/WIT-TM-*.json`) und der Papyri 𝔓32, 𝔓46 und 𝔓15/16 (`data/witnesses/WIT-GA-P*.json`) stammen aus den Metadaten von papyri.info/DCLP und HGV (github.com/papyri/idp.data); es sind Sachangaben, eigene Formulierung, kein übernommener Text.

Alle übrigen Dateien in `data/`, `docs/`, `scripts/` usw. sind eigene Beiträge unter CC0 1.0.

## Numerische Testdaten des Lesestroms

Seit v0.13 liegt das Mengengerüst als `data/navigation/NAV-PROT66-KJV.json` im freien Kern und wird in `app/reading-stream/index.html` eingebettet. Es enthält nachgezählte Kapitel-/Versanzahlen aus der von eBible.org / CrossWire als **Public Domain** ausgewiesenen KJV-Ausgabe: https://ebible.org/Scriptures/eng-kjv_usfm.zip (Quelldateien 2026-09-26). Aus dieser KJV-Quelle wurden kein Bibeltext und kein fremder Programmcode übernommen. Die Quelle weist auf besondere Druckrechte für den Übersetzungstext im Vereinigten Königreich hin. Prüfsumme und Ableitung sind in `app/reading-stream/provenance.json` dokumentiert. Eine ursprünglich im Chat benutzte, nicht lizenzierte JSON-Zählliste wurde nicht als Fremddatei ins Repository übernommen; alle Zahlen wurden für diesen Import unabhängig aus dem genannten USFM-Bestand gewonnen und abgeglichen.

Logo, Linienicons, Code und redaktionelle Entwürfe dieses Prototyps sind eigene Beiträge unter CC0, ebenso die 83 Zusammenfassungen in `data/summaries/` und die Hintergrundnotizen in `data/background/` (eigene Formulierungen; ausserbiblische Quellen wie Josephus, Mischna oder Talmud werden nur mit Fundstelle genannt, kein Text übernommen) (KI-Entwürfe aus dem Designgespräch, keine Fremdtexte). Deutsche und englische Buchnamen und Abkürzungen sind allgemeine Bezeichnungen, keine übernommenen Werkteile. Keine Assets oder Schriftdateien der Fondation Beyeler übernommen.

## Fremddaten in der Studienschicht (`data-nc/`)

| Pfad | Inhalt | Quelle | Lizenz | Pflicht |
|---|---|---|---|---|
| `data-nc/witness-texts/DSS-*.json`, `data-nc/witnesses/WIT-DSS-*.json` | Biblische Texte vom Toten Meer (Qumran, Murabbaʿat) je Vers mit Fundort, für Rut (2QRuth a/b, 4QRuth a/b) und Obadja (4QXII g, MurXII); maschineller Vergleich mit dem WLC | ETCBC dss, Text-Fabric 2.0.1, Commit `ac91a978`; Daten von Martin G. Abegg Jr., James E. Bowley, Edward M. Cook | **CC BY-NC 4.0** | Namensnennung (Abegg/Bowley/Cook, ETCBC/CACCHT); nur nicht kommerziell |

Im Lesestrom liegen diese Daten in eigenen Paketen `n/<BUCH>`; mit `BIBLE_APP_NO_NC=1` baut `scripts/build_reading_stream.py` ohne sie. Die Einzeldatei `app/reading-stream/index.html` und die veröffentlichte Fassung enthalten sie (gemeinnütziger Betrieb).

Hinweis: Diese Übersicht ist keine Rechtsberatung. Lizenzangaben vor jedem Import erneut prüfen und im Quellendatensatz festhalten.

## Eingebettete Markus-Daten im Lesestrom

Seit v0.15 enthält `app/reading-stream/index.html` zusätzlich Textausschnitte der CNTR-Transkriptionen und die daraus abgeleiteten Zuordnungen (CC BY-SA 4.0, Alan Bunning, Center for New Testament Restoration); die Attribution steht in der Seite beim jeweiligen Blatt.

`app/reading-stream/index.html` enthält seit v0.12 zusätzlich die unveränderte Studienprojektion aus `data/`: SBLGNT-Text/Apparat (CC BY 4.0), MACULA samt genannten Glossen (CC BY 4.0 bzw. gemeinfrei), MorphGNT-Pilotannotation (CC BY-SA 3.0). Urheber und Quellen entsprechen den obigen Einträgen; Attribution und Lizenzlinks sind auch in der eigenständigen Seite eingebettet. Die MorphGNT-Annotationen behalten CC BY-SA 3.0; eigener UI-Code und eigene Studieninhalte bleiben CC0. Seit v0.39 enthalten die Buchpakete `b/<BUCH>` zusätzlich Auszüge der UBS-Wörterbücher (CC BY-SA 4.0) sowie STEPBible-Kurzglossen, Ausgabenangaben (TAGNT) und Ketiv-Formen (TAHOT) (CC BY 4.0); die Attribution steht im Blatt «Quellen» des Verses. Die Darstellung formatiert und kürzt die Datenfelder, ohne fachliche Neubewertung.
