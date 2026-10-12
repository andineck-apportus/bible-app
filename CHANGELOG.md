# Changelog

Änderungen am Bibel-Wissensfundus. Die Einträge v0.1–v0.5 sind aus den vorhandenen Paketen rekonstruiert; sie sind keine Behauptung über ursprüngliche Veröffentlichungsdaten. Alle fünf Pakete wurden am 8. Oktober 2026 nach GitHub übernommen. Der aktuelle Einstieg und die Bedienung stehen in [README.md](README.md), offene Arbeiten in [Status und Roadmap](docs/STATUS-UND-ROADMAP.md).

## v0.16 — 2026-10-12 — Das Vaterunser

- Wunsch: das Vaterunser komplett bearbeiten.
- Text: Matthäus und Lukas vollständig importiert (SBLGNT mit MACULA-Annotation; Apparat Mt 820/827, Lk 1133/1142 Stellen zugeordnet, Rest protokolliert; Gesichertheitsbewertung). Importer: Gross/Klein-Abweichung SBLGNT/MACULA wird wie eine Akzentabweichung protokolliert; Apparatüberschrift «Matthew» erkannt.
- Textzeugen: CNTR-Transkriptionen für Matthäus und Lukas, dazu 𝔓45, 𝔓75 und sieben Amulette bzw. Einzeltexte mit dem Vaterunser (3.–6. Jh.; Metadaten nach papyri.info/DCLP). Zuordnung zu den Lesarten für Mt 6,5–15 und Lk 11,1–4 (Abgleich mit dem SBLGNT-Apparat jeweils 18/18 bzw. 6/6).
- Studie Vaterunser (`STUDY-LP-0001`, KI-Entwürfe, ungeprüft): Texteinheiten Mt 6,5–15 (drei Teile) und Lk 11,1–4; deutsche Arbeitsübersetzung mit neun Alternativen (u. a. Lobpreis am Schluss, «vergeben haben/vergeben», kurze und lange Lukasfassung), je mit Wortbedeutungen und Entstehungserklärungen; vollständige Wortzuordnung Mt 6,9–13 und Lk 11,2–4; 6 Befunde, 7 Deutungen mit Gegenargumenten (u. a. drei Deutungen von ἐπιούσιος, Versuchung, «der Böse/das Böse», Vergebung), Grundsatz, Anwendung, 2 offene Fragen, 7 Beziehungen, 12 Hintergrundnotizen, 2 Kapitelzusammenfassungen. Autorenwerkzeug `scripts/authoring/vaterunser.py`.
- Lesestrom: trägt jetzt mehrere ausgearbeitete Stellen (neue Projektion `scripts/project_study.py`, Schlüssel nach Bibelstelle); Menü listet die ausgearbeiteten Stellen; Studienblatt zeigt Anwendung, Fragen und Beziehungen je Abschnitt; Textzeugen-Blatt mit Papyri und Amuletten.
- Tests erweitert (Vaterunser in Struktur- und Bedienungstest). Abschnittsebene hat jetzt 6705 statt 6704 Einträge, weil Mt 6 nach echten Einheiten gegliedert ist.

## v0.15 — 2026-10-12 — Lesarten bis zur Quelle

- Rückmeldung: Bei anderen Lesarten bis zur Quelle eintauchen können, auch übersetzt.
- Handschriften: Transkriptionen der sechs ältesten Handschriften des Markusevangeliums (01 א, 02 A, 03 B, 04 C, 05 D, 032 W) und fünf Ausgabentexte (WH, RP, Stephanus, KJTR, SR) aus dem Center for New Testament Restoration importiert (CC BY-SA 4.0, Commit fixiert, SHA-256). Neue Typen `witness`, `witness_transcription`, `witness_reading_set`; neue Ausgaben ED-ST, ED-KJTR, ED-SR; Kurzbeschreibungen (`about_de`) für alle Ausgaben.
- Maschinelle Zuordnung Handschrift → Lesart für die 28 Variantenstellen in Mk 3,20–35 (`scripts/collate_witnesses.py`, `METHOD-AUTO-COLLATION-V1`), Erstschrift und Korrektur getrennt. Selbstprüfung gegen den SBLGNT-Apparat: 50/52.
- Befund: Ephraemi (C) liest in 3,29 laut CNTR ἁμαρτίας, nicht κρίσεως wie in der Arbeitsnotiz `VAR-MRK-003-029-001`; die Arbeitsnotiz bleibt erhalten, die Abweichung wird angezeigt. In 3,20 widersprechen sich SBLGNT-Apparat und CNTR-Text bei Robinson-Pierpont.
- Übersetzungs-Alternativen um Wortbedeutungen der Lesarten und mögliche Entstehungserklärungen ergänzt (Revision protokolliert).
- Lesestrom: Blatt «Bis zur Quelle» je Lesart. Validator prüft die neuen Typen; DOM-Test erweitert.

## v0.14 — 2026-10-12 — Hintergrund damals

- Rückmeldung: Auf Versebene passt der Lesestrom, es fehlt der Hintergrund damals.
- Neuer Datentyp `background_note` (`data/background/`): 13 Notizen zu Mk 3,20–35 über Zeit, Ort, Kultur und Religion, je mit Kontext, Sicherheitsgrad, Unsicherheiten, Vergleichsstellen und ausserbiblischen Fundstellen (nur zitiert). Neuer Kontext `CTX-MARK-READERS-0070` (erste Leserschaft des Markus), neuer Tag `TAG-HISTORICAL-BACKGROUND`. KI-Entwürfe, fachlich ungeprüft.
- Lesestrom: «Damals» im Versblatt, «Hintergrund damals» je Abschnitt, optional kurze Hinweise im Text (Menü).
- Validator prüft Pflichtfelder und Kontextverweis der Hintergrundnotizen; zwei neue Negativtests; DOM-Test erweitert. 1131 Datensätze.

## v0.13 — 2026-10-12 — Lesestrom als Hauptrichtung, zugänglicher und ungestörter

- Vorgabe: Bibelstudium zugänglich für Personen ohne Griechisch und Hebräisch; ungestört lesen und «abtauchen in die Tiefe»; Hintergrund nur auf Wunsch ([VISION.md](docs/VISION.md)).
- Lesestrom neu aufgebaut (`app/reading-stream/template.html`): Vollbild ohne Geräterahmen, Leisten blenden beim Lesen aus, Verse fliessen als Text, keine technischen Zähler, ein Vertiefen-Link je Eintrag, deutsche Stellenangaben (3,20), Farben nach System, Einstellungen lokal gespeichert.
- Lesarten, Studieninhalte und Quellen als Blätter über dem Text; «+» nur an Versen mit abweichenden Lesarten. Urtext, Wort für Wort, Editionenvergleich und IDs nur im Modus «Urtext und Details»; optional «Andere Lesarten im Text zeigen». Griechische Einschübe in Erklärungen werden ohne diesen Modus ausgeblendet oder umschrieben (nur Darstellung).
- Neue Datentypen im freien Kern: `navigation_structure` (`data/navigation/NAV-PROT66-KJV.json`, Testkonfiguration) und `summary` (`data/summaries/`, 83 Entwürfe). Bisher lagen sie in der Vorlage; die Inhalte sind unverändert übernommen. Schema und Validator ergänzt (1116 Datensätze, PASS).
- `scripts/build_reading_stream.py` bettet Navigation, Zusammenfassungen und Markus-Projektion ein; DOM-Test an die neue Bedienung angepasst.
- Studienprototyp `app/prototype/` als abgelöst gekennzeichnet; `build_prototype.py` bleibt als Datenprojektion.
- Prüfungen: Validator, Validator-Negativtests, Struktur- und DOM-Test; Ansicht in Chromium in Handybreite, hell und dunkel. Keine Prüfung auf echten Geräten, keine fachliche Prüfung.

## v0.12 — 2026-10-11 — Markus im Lesestrom

- Pilotstudie Mk 3,20–35 im neuen Lesestrom: drei kanonische Abschnitte, 16 Arbeitsübersetzungen, sechs Alternativen, 249 Wörter und 28 Variantenstellen.
- Aufklappbare Wortdetails, Quellenvergleich und getrennte Studienebenen mit Gegenargumenten, Prüfstatus, Bewertungsgrenzen und Attribution. Direkteinstieg im Menü und bei Markus.
- Reproduzierbarer Build aus bestehender Datenprojektion; kanonische Daten unverändert. Struktur-, Daten- und DOM-Interaktionstests erfolgreich; visuelle Geräteprüfung ausstehend.

## v0.11 — 2026-10-11 — Fortlaufender Lesetiefe-Prototyp

- Separater, eigenständig lauffähiger Entwurf `app/reading-stream/index.html`: auf jeder Ebene scrollend lesen, an interessanten Einträgen vertiefen und zur Leseposition zurückkehren.
- Vollständiges 66-Bücher-Mengengerüst mit 1’189 Kapiteln, 6’704 ausdrücklich technischen Testblöcken und 31’102 Verspositionen; 66 deutsche KI-Buchzusammenfassungen als ungeprüfter Entwurf.
- Mobile-/Tablet-Ansichten, neutrales Hell/Dunkel, Stellensuche, DE/EN-Oberfläche, Textgrösse und eigene Auswahlfelder. Kompaktes SVG-Logo mit gedrehtem B und zwei Quadraten.
- Datenquelle und Grenzen dokumentiert; numerische Kapitel-/Versstruktur unabhängig aus eBible-USFM nachgezählt. Keine neuen kanonischen Text- oder Studiendaten, bestehender Markus-Prototyp unverändert.
- Strukturprüfung mit Node.js ohne Zusatzpakete; DOM-Prüfungen im Arbeitslauf. Visuelle Prüfung auf echten Geräten steht aus.

## v0.10 — 2026-10-09 — Prototyp für allgemeine Leser

- Prototyp nach Rückmeldung neu gestaltet: einfacher und allgemeiner, schlicht, hell/dunkel, mit gezeichnetem Überblicksbild. Drei Wege (Überblick, Lesen, Vertiefen) über eine untere Leiste; Studienpfad; Einstellungen für Lesarten, Urtext-Modus, Schriftgrösse und Farben.
- Abweichende Lesarten: nur Stellen, die die deutsche Übersetzung verändern (6 in Mk 3,20–35), auf Wunsch eingeblendet; Erklärung in einfacher Sprache mit Bezeugung («Steht in 4 von 5 wichtigen Textausgaben»), ohne Entscheidung über richtig/falsch.
- Urtext, Wort für Wort, Grammatik und alle 28 Apparatstellen nur im Modus «Urtext und Details».
- Neue Daten (KI-Entwurf): `alternatives` in den Übersetzungen (deutsche Wiedergabe abweichender Lesarten mit Wirkung «bedeutsam»/«gering»), `summary_de` für die Texteinheiten 3,20–35. Validator prüft, dass jede Alternative auf eine vorhandene Lesart zeigt und ihr Ausgangstext in der Übersetzung vorkommt.

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
