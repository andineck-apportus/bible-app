# Changelog

Änderungen am Bibel-Wissensfundus. Die Einträge v0.1–v0.5 sind aus den vorhandenen Paketen rekonstruiert; sie sind keine Behauptung über ursprüngliche Veröffentlichungsdaten. Alle fünf Pakete wurden am 8. Oktober 2026 nach GitHub übernommen. Der aktuelle Einstieg und die Bedienung stehen in [README.md](README.md), offene Arbeiten in [Status und Roadmap](docs/STATUS-UND-ROADMAP.md).

## v0.9 — 2026-10-09 — Studienprototyp Mk 3,20–35

- Klickbarer Prototyp `app/prototype/mk3-20-35.html`, erzeugt mit `scripts/build_prototype.py` aus den Daten des freien Kerns (keine eigenen Inhalte im Prototyp): Zoomstufen Buch → Abschnitt → Einheit → Vers → Wort; Textschichten Deutsch, Griechisch, Wort für Wort; Variantenstellen mit Editionen und Gesichertheitsstufe samt Grenzen der Methode; Wortdetails (Grundform, Häufigkeit in Markus, Form, Satzrolle, Bezug, deutsche Entsprechung, Glossen, Vergleich MACULA/MorphGNT); Kette Befund → Deutung → Prinzip → Anwendung; Studienpfad in sechs Schritten; hell und dunkel, für Smartphones ausgelegt.
- Neue Daten (KI-Entwürfe, ungeprüft): Texteinheiten 3,20–21, 3,31–35 und Abschnitt 3,20–35; Befund FIND-MRK-0005 zur Verschachtelung; Deutung INT-MRK-0003 mit Vorbehalt und Gegenargument; deutsche Arbeitsübersetzung 3,20–21 und 3,31–35 (Wortzuordnung folgt).
- Validator prüft auch `parts` von Texteinheiten.

## v0.8 — 2026-10-09 — Ganzes Markusevangelium, Gesichertheitsbewertung, Lizenzschichten

- Lizenzmodell: eigene Inhalte CC0; freier Kern `data/` (gemeinfrei, CC0, CC BY, CC BY-SA) und Studienschicht `data-nc/` für nicht kommerzielle Quellen, strikt getrennt; Betreiber gemeinnütziger Verein ([LIZENZEN.md](LIZENZEN.md)).
- Text und Annotation getrennt: Token-Sets enthalten nur die Wörter der Edition; sprachliche Angaben liegen als eigene Annotationsschichten daneben.
- Ganzes Markusevangelium importiert: SBLGNT-Text (Faithlife/SBLGNT, Commit `c4d241a9c1c4`, CC BY 4.0) mit 11 286 Wörtern; MACULA Greek (Commit `8423afe47b9e`, CC BY 4.0) als Annotation (Lemma, Morphologie, Syntaxrolle, Referenten, Glossen). MARBLE-Wortbedeutungen bewusst nicht übernommen (nur «used with permission»). Neuer Importer `scripts/import_sblgnt_book.py`.
- Pilot-Token-Set Mk 3,22–30 migriert (`scripts/migrations/v0_8.py`): gleiche Token-IDs jetzt im Kapitel-Set, MorphGNT-Werte unverändert als eigene Schicht, alter Datensatz als `deprecated` erhalten. Zeichen «text»/«word» kommen jetzt aus der Edition (Elision ʼ statt ’ bei MorphGNT); Quellenangaben im Alignment entsprechend neu erzeugt.
- SBLGNT-Apparat für ganz Markus: 929 von 930 Einträgen an Tokens gebunden (neu: Siglen Holmes, Greeven, ⟦WH⟧; mehrere Auslassungen «…»; Markierungen ⸁ und ⸄⸅); 1 versübergreifender Eintrag (7,21–22) bewusst nicht importiert und protokolliert. Die 10 Pilotstellen sind inhaltlich unverändert (jetzt in `data/variants/sblgntapp-mrk/`).
- Gesichertheitsbewertung als Datentyp (`assessment_set`, `assessment_method`) mit Methode «Übereinstimmung der Editionen» und offengelegten Grenzen; für alle 929 Stellen berechnet ([GESICHERTHEIT.md](docs/GESICHERTHEIT.md)).
- Validator prüft zusätzlich Annotationen (Referenten nur als Token-IDs), Bewertungen und die Trennung Kern/Studienschicht; neue Negativtests `scripts/test_validate.py`.
- Unabhängiges Gegenlesen durch einen separaten KI-Durchgang (alle Tokens, alle MACULA-Zeilen, alle 929 Stellen und Bewertungen nachgerechnet). Korrigiert: MACULA-Platzhalter für «kein Referent» nicht mehr als Verweis gespeichert (jetzt `…_unresolved`), MACULA-IDs im Feld `frame` in Token-IDs umgesetzt, Lesarttexte behalten das Elisionszeichen der Edition (ʼ), Lesarten ohne gezählte Edition gekennzeichnet (`no_counted_edition`), Pfad in LIZENZEN.md, Autor der Cherith-Glossen, Migrationsprotokoll um neu erzeugte Änderungen ergänzt.

## 2026-10-09 — Vision und Lizenz

- Vision in vier Stufen festgehalten ([VISION.md](docs/VISION.md)): transparente Textbasis mit Gesichertheitsbewertung statt Lektorat; Übertragung in heutige Zeit, Kultur und Sprachen; Zoomstufen und Studienanleitung; Visualisierung (u. a. Raumobjekte), UX und Beiträge Dritter. Vorgaben und abgeleitete Vorschläge getrennt.
- Lizenz festgelegt: eigene Inhalte CC0 1.0 ([LICENSE](LICENSE)); Fremddaten mit Lizenz in [LIZENZEN.md](LIZENZEN.md); im Kern nur gemeinfreie, CC0- und CC-BY-Quellen.
- Folgerung: MorphGNT-Annotation (CC BY-SA) soll durch eine CC-BY-Annotation ersetzt werden; nicht kommerzielle Datensätze werden nicht übernommen.
- AGENTS.md um Lizenzgrundsatz und «Gesichertheit statt Lektorat» ergänzt.

## 2026-10-09 — Quellenlandschaft für die ganze Bibel

- [QUELLEN.md](docs/QUELLEN.md) auf die ganze Bibel erweitert: AT hebräisch/aramäisch, Septuaginta, NT, alte Übersetzungen, Kirchenväter, Lexika, Kontext; Lizenzen und Zugang je Quelle mit Links.
- Neu: beantragbare Zugänge (INTF, Deutsche Bibelgesellschaft, CATSS, TLG, Brill, Brepols, ETCBC u. a.), Abdeckungsmatrix «nur offene Quellen» und offene Entscheidung zur kommerziellen Nutzung.
- Recherche über die Websites der Anbieter; nicht an Primärquellen bestätigte Angaben sind als [ungeprüft] markiert.

## v0.7 — 2026-10-09 — Varianten auf Editionsebene, vollständige Arbeitsübersetzung

- Quellenlandschaft dokumentiert: [QUELLEN.md](docs/QUELLEN.md) mit Rechte-Ampel und empfohlener Reihenfolge.
- SBLGNT-Apparat (Faithlife/SBLGNT, CC BY 4.0, Commit `c4d241a9c1c4`) für Mk 3,22–30 importiert: 10 Variantenstellen in 3,25–29 mit Lesarten von Westcott-Hort, Tregelles, NA28 und Robinson-Pierpont, als `evidence_level: edition_apparatus` getrennt von Handschriftenbelegen. Neuer Importer `scripts/import_sblgnt_apparatus.py` bindet jede Stelle über die SBLGNT-Markierungen ⸀/⸂⸃ an Token-IDs und prüft die Wortgleichheit.
- Editionsdatensätze für WH, Tregelles, NA28 und Robinson-Pierpont; Quellendatensatz für den Apparat.
- Bestehende Varianten und das Alignment zu Mk 3,29 additiv an Token-IDs gebunden (`scripts/migrations/v0_7.py`, Protokoll in `provenance/migrations/2026-10-09-v0.7.json`).
- Eigene wörtlich orientierte Arbeitsübersetzung Mk 3,22–30 und vollständige Wortzuordnung aller 140 Tokens mit Grammatik- und Alternativnotizen (KI-Entwurf, `draft`); 3,29 unverändert aus der bisherigen Arbeitsübersetzung übernommen. Erzeugt mit `scripts/authoring/mk3_22_30_translation.py`.
- Gegenlesen durch einen separaten KI-Durchgang: drei Fehler korrigiert (3,26 Aorist jetzt «gespalten worden ist»; Notiz zu εἰσελθών; Apparatlesarten nicht mehr pauschal als Ersetzung klassifiziert), mehrere Präzisierungen übernommen (u. a. 3,27 «hineingehen … plündern … plündern»). Keine fachliche Prüfung durch eine Person.
- Validator prüft zusätzlich Token-IDs, Editionen in Lesarten, weitere Verweisfelder und bei `coverage: complete` die lückenlose Zuordnung sowie das Vorkommen jedes Zieltexts in der Übersetzung.
- Pilotstudie führt die neuen Ergebnisse in `outputs`.
- Offen: Zeugenangabe Ephraemi (C) in `VAR-MRK-003-029-001` prüfen; kein automatischer Test für den Apparat-Importer.

## v0.6 — 2026-10-09 — Bibelstellen vereinheitlicht, griechischer Text importiert

- Kanonische Bibelstellen eingeführt (`MRK.3.29`, `MRK.3.22-MRK.3.30`, USFM-Buchcodes) mit Dokumentation [BIBELSTELLEN.md](docs/BIBELSTELLEN.md) und Werkzeug `scripts/refs.py` (Prüfung, Umwandlung deutscher/englischer Eingaben, deutsche Anzeige).
- Bestehende Daten per `scripts/migrations/v0_6.py` migriert: Bibelstellen, Typnamen `study`/`text_unit`, Tippfehler in einem Statuswert, fehlende `outputs` der Pilotstudie. 12 Änderungen protokolliert in `provenance/migrations/2026-10-09-v0.6.json`; Aussagen, Status, Konfidenz und IDs unverändert.
- Schema auf alle Typen und Statuswerte erweitert; Validator prüft jetzt Schema, Verweise zwischen Datensätzen, Lesarten und Bibelstellen.
- Importer korrigiert: MorphGNT-Referenzen haben die Form `0203xx` (Markus = 02), nicht `6203xx`. Quelle, Upstream-Commit, SHA-256, Lizenzangaben und Importdatum werden im Datensatz festgehalten; Import ohne Commit wird abgelehnt.
- Mk 3,22–30 aus MorphGNT SBLGNT 6.12 (Commit `a2afca0e96e3`) importiert: 140 Tokens, 91 Wortformen, 64 Lemmata (`imported_unreviewed`). Zählungen unabhängig gegen die Quelldatei nachgezählt.
- Arbeitstranskription Mk 3,29–30 mit SBLGNT abgeglichen: eine Abweichung (`ἀλλ’`/`ἀλλὰ`).
- Grenzen: keine typspezifischen Schemas, keine Versifikationsprüfung, keine fachliche Prüfung der Morphologie; Lizenzangaben vor Veröffentlichung klären.

## 2026-10-08 — Dokumentation vereinheitlicht

- Eine zentrale README.md für Projektüberblick, Einstieg und vorhandene Programme.
- Versionsnotizen aus den bisherigen READMEs in diesem Changelog zusammengeführt.
- README-v0.3.md, README-v0.4.md, README-v0.5.md und docs/README-original-v0.5.md aus dem aktuellen Dateibaum entfernt.
- Verweise und Herkunftsinventar angepasst. Historische Originaldateien bleiben in Git und den unveränderten ZIP-Paketen erhalten.

## 2026-10-08 — Repository konsolidiert

- Die fünf Paketstände v0.1–v0.5 als einzelne Archiv-Commits übernommen.
- Originalpakete mit SHA-256-Prüfsummen und Dateiinventar archiviert.
- Konzept, Datenmodell, Metadaten, Arbeitsprozess, Entscheidungen, Übersetzungsmethoden und Roadmap dokumentiert.
- Arbeitsregeln für KI-Unterstützung in AGENTS.md ergänzt.
- 36 Datensätze einschliesslich 6 Tags gesichert; bestehende ID-/Tag-Prüfung und synthetische Importtests erfolgreich ausgeführt.
- Grenzen dokumentiert: keine vollständige JSON-Schema-Validierung, noch keine SQLite-Projektion oder Benutzer-App, fehlende Primärquellenprüfung und vollständige Tokenbestände.

## v0.5 — Varianten und Übersetzungszuordnung

- Zweite Variantenstelle zu Mk 3,29 ergänzt: ἐστιν / ἔσται.
- Redaktionelle Entscheidung mit bevorzugter Lesart, Alternative, Begründung, Quellen und Sicherheitsgrad ergänzt.
- Eigene deutsche Arbeitsübersetzung von Mk 3,29 und erste griechisch-deutsche Wort-/Phrasenzuordnungen aufgenommen.
- Bestehenden v0.4-Bestand beibehalten; insgesamt 36 Datensätze einschliesslich 6 Tags.
- Zeugenangaben laut damaligem Arbeitsstand anhand einer Sekundärtranskription verglichen; keine eigene Prüfung von Handschriftenbildern und keine vollständige Kollation der Perikope.
- Griechischer Beispieltext weiterhin Arbeitstranskription, Alignments unvollständig, keine verifizierten Gesamtzahlen für Token oder Lemmata. Die Lesartpräferenz bleibt eine revidierbare Entscheidung.

Quellenhinweise aus den Versionsnotizen:
- https://github.com/morphgnt/sblgnt
- https://www.greeklab.org/interlinear.php?book=Mark&cap=3&verse=29
- https://tips.translation.bible/tip_source/bratcher-nida-1961/page/84/

## v0.4 — Importvorbereitung verbessert

- Erzeugte Token- und Zähldatensätze mit `id`, `type`, `status` und `tags` versehen, damit der vorhandene Validator sie lesen kann.
- Ablehnung fehlerhafter Zielzeilen und unvollständiger Versabdeckung ergänzt; Eingabedatei mit SHA-256 dokumentiert.
- Synthetische Importtests für vollständige und unvollständige Eingaben ergänzt.
- Ablauf festgehalten: konkrete Quelldatei und Upstream-Commit dokumentieren, importieren, validieren und Text/Morphologie an der benannten Edition prüfen.
- Kein echter Quelltext mitgeliefert; keine belastbaren Wortzahlen für Mk 3,22–30 veröffentlicht.

## v0.3 — Editionsgebundener Import vorbereitet

- Editionsobjekt für SBLGNT und Quellenhinweis auf MorphGNT SBLGNT Edition 6.12 ergänzt.
- Importer für eine lokal bereitgestellte MorphGNT-Datei zur Perikope Mk 3,22–30 hinzugefügt; Ausgabe in `data/tokens/` und `data/counts/` vorgesehen.
- Importvorbereitung auf sieben durch Leerzeichen getrennte Spalten und den im Skript erwarteten Referenzcode ausgerichtet. Der Abgleich mit einer tatsächlichen versionierten Quelldatei blieb offen.
- Vollständiger Quellimport, Primärprüfung der Lesarten und Übersetzungsalignment noch ausstehend.

Quellen und Attribution aus den damaligen Notizen: SBL Greek New Testament, herausgegeben von Michael W. Holmes, © Society of Biblical Literature und Logos Bible Software; dort als CC BY 4.0 bezeichnet. MorphGNT SBLGNT Edition 6.12, J. K. Tauber; Morphologie/Lemmatisierung dort als CC BY-SA bezeichnet. Diese übernommenen Angaben ersetzen keine Prüfung der Bedingungen der konkret importierten Fassung.
- https://github.com/Faithlife/SBLGNT
- https://github.com/morphgnt/sblgnt

## v0.2 — Pilotstudie erweitert

- Ersten Studienbericht zu Markus 3,22–30 ergänzt.
- Quellenhinweise, vorläufige Variantenstelle Sünde/Gericht, zusätzliche Befunde, Parallelstellen und eine offene Forschungsfrage aufgenommen.
- Arbeitstranskription von Mk 3,29–30 und ausdrücklich nicht verifizierte Leerzeichenzählungen für diese zwei Verse ergänzt; keine Lemmazählung.
- Insgesamt 30 Datensätze einschliesslich 6 Tags.

## v0.1 — Strukturierter Wissensfundus angelegt

- Pilot Markus 3,22–30 mit Werk, natürlicher Texteinheit, Studie, Befunden, alternativen Interpretationen, Prinzip und kontextabhängiger Anwendung angelegt.
- Historischen Kontext und heutige Anwendung CH/de-CH 2026 getrennt; Themen und 6 kontrollierte Tags eingeführt.
- Stabile IDs, Tag-Referenzen, frühe Wissenszeit-/Vorgängerfelder, generisches Schema und einfachen Validator angelegt; insgesamt 19 Datensätze einschliesslich Tags.
- Git als massgebliche Quelle festgehalten; SQLite als spätere abgeleitete Projektion vorgesehen.
- Fachliche Aussagen als vorläufig markiert; geprüfte Textbestände, genaue Quellenbelege und Argument-/Evidenzobjekte als nächste Arbeiten festgehalten.
