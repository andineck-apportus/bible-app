# bible-app

Git-versionierter Bibel-Wissensfundus: Quellen, Textbefunde, konkurrierende Interpretationen, Prinzipien und kontextabhängige Anwendungen nachvollziehbar miteinander verbinden.

**Stand: 14. Oktober 2026 · UI v0.58 (Lesestrom) · Urtext: Matthäus, Markus, Lukas, Johannes, Philipper, Titus, 1–3 Johannes (Griechisch), Rut, Obadja, Jona (Hebräisch); ausgearbeitet: das Vaterunser (Mt 6,5–15; Lk 11,1–4) sowie Markus, Johannes, Rut, Obadja, Jona, Philipper, Titus und 1–3 Johannes ganz; Wörterbuch (UBS, CC BY-SA) im Wortblatt. Der Lesetext geht immer vom Urtext aus.**

Dies ist der Konzept- und Datenprototyp, noch keine fertige Benutzer-App. Vorhanden sind 4509 strukturierte Datensätze, darunter:
- der **ganze griechische Text des Markusevangeliums** (SBLGNT, 11 286 Wörter mit stabilen IDs) mit Lemma, Morphologie, Syntaxrollen, Referenten und Glossen aus MACULA Greek als eigener Annotationsschicht,
- **929 Variantenstellen** auf Editionsebene aus dem SBLGNT-Apparat, an die Wörter gebunden, jede mit einer maschinell berechneten **Gesichertheitsbewertung** (Übereinstimmung der Editionen, Methode offengelegt),
- die Pilotstudie Mk 3,22–30 mit Befunden, Deutungen, Prinzip, Anwendung und einer vollständigen deutschen Arbeitsübersetzung mit Wortzuordnung (KI-Entwurf, ungeprüft),
- eine einheitliche Bibelstellen-Konvention, ein generisches Schema und ein Validator.

**Hauptrichtung: der [Lesestrom](app/reading-stream/index.html)** – eine eigenständige HTML-Datei zum Öffnen im Browser. Man liest die Bibel auf jeder Ebene fortlaufend (ganze Bibel, Testamente, Buchgruppen, Bücher, Kapitel, Abschnitte, Verse) und taucht an jeder Stelle eine Stufe tiefer. Der Lesestrom ist für Leserinnen und Leser ohne Griechisch und Hebräisch gemacht: Lesarten (auf Wunsch bis zu den alten Handschriften), Hintergrund zur Zeit damals, Erklärungen und Quellen öffnen sich nur auf Wunsch; Urtext und Grammatik gibt es im Modus «Urtext und Details». Ausgearbeitet sind bisher Markus 3,20–35, das Vaterunser (Mt 6,5–15; Lk 11,1–4) sowie ganze Bücher: Philipper und Titus (Griechisch), Rut und Obadja (Hebräisch); sonst gibt es vorerst das Gerüst und ungeprüfte Zusammenfassungen. [Bedienung, Daten und Grenzen](docs/LESETIEFE-PROTOTYP.md).

Der frühere Studienprototyp `app/prototype/mk3-20-35.html` (v0.9/v0.10) ist abgelöst und bleibt nur als Zwischenstand erhalten. SQLite-Projektion und Handschriftenbelege fehlen noch.

## Einstieg

| Datei | Inhalt |
|---|---|
| [docs/VISION.md](docs/VISION.md) | Vision in vier Stufen: transparente Textbasis, Übertragung, Zoomstufen und Studienanleitung, Visualisierung und UX |
| [LIZENZEN.md](LIZENZEN.md) | Eigene Inhalte CC0; freier Kern und Studienschicht; Lizenzen übernommener Fremddaten |
| [Quellenkarte](app/quellenkarte/index.html) | Alle bekannten Quellen nach Schicht, Nutzungsrecht und Verwendung (aus `data/sources/`); Anfragen an Rechteinhaber: [docs/ANFRAGEN.md](docs/ANFRAGEN.md) |
| [docs/GESICHERTHEIT.md](docs/GESICHERTHEIT.md) | Wie Unterschiede ausgegeben und nach Gesichertheit bewertet werden |
| [CHANGELOG.md](CHANGELOG.md) | Änderungen und Entwicklung von v0.1 bis heute |
| [docs/KONZEPT.md](docs/KONZEPT.md) | Ziel, Analyseebenen, Zoom-System und Kontextdimensionen |
| [docs/QUELLEN.md](docs/QUELLEN.md) | Quellenlandschaft (Handschriften, Editionen, Datensätze, Lexika, Kontext) mit Rechte-Ampel |
| [docs/BIBELSTELLEN.md](docs/BIBELSTELLEN.md) | Kanonische Schreibweise aller Bibelstellen (`MRK.3.29`, `MRK.3.22-MRK.3.30`) |
| [docs/DATENMODELL.md](docs/DATENMODELL.md) | Vorhandene Objekttypen, Beziehungen und geplante Erweiterungen |
| [docs/METADATEN.md](docs/METADATEN.md) | Herkunft, Quellen, Editionen, Zeitachsen, Tags, Unsicherheit |
| [docs/PROZESS.md](docs/PROZESS.md) | Recherche, Textkritik, Übersetzung, Auslegung, Review und Versionierung |
| [docs/ENTSCHEIDUNGEN.md](docs/ENTSCHEIDUNGEN.md) | Festlegungen und noch offene Architekturfragen |
| [docs/STATUS-UND-ROADMAP.md](docs/STATUS-UND-ROADMAP.md) | Tatsächlich vorhandener Stand, erkannte Lücken und nächste Schritte |
| [docs/UEBERSETZUNGSMETHODEN.md](docs/UEBERSETZUNGSMETHODEN.md) | Gesprächsergebnisse zu NGÜ, Neues Leben, Hfa und Elberfelder |
| [docs/MK3-22-30.md](docs/MK3-22-30.md) | Historischer Studienbericht v0.2; aktuellen Status und Changelog beachten |
| [docs/UEBERNAHME.md](docs/UEBERNAHME.md) | Umfang, Herkunft und Grenzen dieser Übernahme |
| [AGENTS.md](AGENTS.md) | Arbeitsregeln für künftige KI-Unterstützung |

## Vorhandene Programme ausführen

Python 3, keine externen Pakete für die vorhandenen Skripte:

```sh
python3 scripts/validate.py
python3 scripts/test_validate.py
python3 scripts/test_import.py
python3 scripts/refs.py "Mk 3,22–30"   # Stelle in kanonische Form umwandeln
python3 scripts/build_reading_stream.py # Lesestrom aus data/ bauen (nutzt die Projektion aus build_prototype.py)
```

Der Validator prüft das Schema (`schema/record.schema.json`, ausgewertete Teilmenge von JSON Schema), eindeutige IDs, Tags, Verweise zwischen Datensätzen einschliesslich Lesarten (`VAR-…:R1`) und Token-IDs, Annotationen, Bewertungen, alle Bibelstellen und die Trennung von freiem Kern (`data/`) und Studienschicht (`data-nc/`). Ein PASS ist keine wissenschaftliche Freigabe; typspezifische Pflichtfelder werden noch nicht geprüft.

Import (bereits ausgeführt; Quellen per Commit fixiert):

```sh
git clone https://github.com/Faithlife/SBLGNT
git clone https://github.com/Clear-Bible/macula-greek
# Text + MACULA-Annotation, ein Token-Set und eine Annotationsschicht je Kapitel
python3 scripts/import_sblgnt_book.py MRK --tag TAG-MARK \
  --sblgnt SBLGNT --sblgnt-commit c4d241a9c1c479a55b989ba35a4976c1d0b8052c \
  --macula macula-greek --macula-commit 8423afe47b9e8f24b7772e808af45c7159a6fe7e
# Apparat: Variantenstellen auf Editionsebene, an Tokens gebunden
python3 scripts/import_sblgnt_apparatus.py MRK SBLGNT \
  --upstream-commit c4d241a9c1c479a55b989ba35a4976c1d0b8052c --tag TAG-MARK
# Gesichertheitsbewertung «Übereinstimmung der Editionen»
python3 scripts/assess_edition_agreement.py MRK
python3 scripts/compare_working_text.py   # Abgleich mit der alten Arbeitstranskription
# Handschriften (CNTR, CC BY-SA 4.0) und Zuordnung zu den Lesarten
git clone https://github.com/Center-for-New-Testament-Restoration/transcriptions
python3 scripts/import_cntr_transcriptions.py MRK transcriptions \
  --upstream-commit 4e743a41a4b2ca010ece53229cd272aa59b1efe6
python3 scripts/collate_witnesses.py "Mk 3,20–35"
python3 scripts/collate_witnesses.py "Mt 6,5–15"; python3 scripts/collate_witnesses.py "Lk 11,1–4"
# Studieninhalte Vaterunser (Ersterstellung, KI-Entwurf)
python3 scripts/authoring/vaterunser.py
python3 scripts/authoring/zueridueuetsch.py   # Züridüütsch-Schicht (Ersterstellung)
# Titus und Obadja (v0.33): gleiche Importer, Hebräisch über MACULA Hebrew (WLC)
python3 scripts/import_sblgnt_book.py TIT --tag TAG-TITUS --sblgnt SBLGNT --sblgnt-commit c4d241a9c1c479a55b989ba35a4976c1d0b8052c \
  --macula macula-greek --macula-commit 8423afe47b9e8f24b7772e808af45c7159a6fe7e
python3 scripts/import_sblgnt_apparatus.py TIT SBLGNT --upstream-commit c4d241a9c1c479a55b989ba35a4976c1d0b8052c --tag TAG-TITUS
python3 scripts/assess_edition_agreement.py TIT
python3 scripts/import_cntr_transcriptions.py TIT transcriptions --upstream-commit 4e743a41a4b2ca010ece53229cd272aa59b1efe6
python3 scripts/collate_witnesses.py "Tit 1,1–16"; python3 scripts/collate_witnesses.py "Tit 2,1–15"; python3 scripts/collate_witnesses.py "Tit 3,1–15"
git clone https://github.com/Clear-Bible/macula-hebrew
python3 scripts/import_macula_hebrew_book.py OBA --macula macula-hebrew --macula-commit 47db250bd55d0d8577f2a94fba114ef16c35b23c --tag TAG-OBADIAH
python3 scripts/import_comparison_bibles.py TIT --open-bibles open-bibles --bible-databases bible_databases   # ebenso OBA
python3 scripts/authoring/titus_text.py; python3 scripts/authoring/titus_study.py
python3 scripts/authoring/obadja_text.py; python3 scripts/authoring/obadja_study.py
# Rut und Philipper (v0.35): gleiche Importer (RUT über MACULA Hebrew, PHP über SBLGNT/MACULA/CNTR), dann
python3 scripts/authoring/ruth_text.py; python3 scripts/authoring/ruth_study.py
python3 scripts/authoring/philipper_text.py; python3 scripts/authoring/philipper_study.py
# Johannes (v0.44): gleiche Importer, zusätzlich STEPBible TAGNT
python3 scripts/import_sblgnt_book.py JHN --tag TAG-JOHN --sblgnt SBLGNT --sblgnt-commit c4d241a9c1c479a55b989ba35a4976c1d0b8052c \
  --macula macula-greek --macula-commit 8423afe47b9e8f24b7772e808af45c7159a6fe7e
python3 scripts/import_sblgnt_apparatus.py JHN SBLGNT --upstream-commit c4d241a9c1c479a55b989ba35a4976c1d0b8052c --tag TAG-JOHN
python3 scripts/assess_edition_agreement.py JHN
python3 scripts/import_cntr_transcriptions.py JHN transcriptions --upstream-commit 4e743a41a4b2ca010ece53229cd272aa59b1efe6
python3 scripts/collate_witnesses.py JHN.1.1-JHN.1.51   # ebenso je Kapitel 2–21
python3 scripts/import_comparison_bibles.py JHN --open-bibles open-bibles --bible-databases bible_databases
python3 scripts/import_stepbible_tagged.py --step STEPBible-Data --step-commit 93ec3621485afd10fd45fcf43630d42de28d8eb8 JHN
for f in scripts/authoring/johannes_text_*.py scripts/authoring/johannes_study_?.py; do python3 $f; done
# Querverweise (OpenBible.info, CC BY) über die Kopie in scrollmapper/bible_databases
python3 scripts/import_openbible_crossrefs.py bible_databases/sources/extras/cross_references.txt \
  --source-url https://github.com/scrollmapper/bible_databases --upstream-commit e1b254cef86d0e65b1a5d1a94b8b112d0f296a2c
```

Die Importer schreiben Quelle, Upstream-Commit, SHA-256, Lizenz und Importdatum in die Datensätze und brechen bei unsicherer Zuordnung ab bzw. führen nicht zuordenbare Einträge in `reports/` auf, statt sie zu raten. `scripts/import_morphgnt.py` ist der frühere Pilot-Importer (v0.6) und wird nur noch durch `scripts/test_import.py` geprüft.

Prüfungen für den Lesestrom (Node.js ≥ 18): `node scripts/test_reading_stream.cjs`; Bedienung zusätzlich mit `npm install --no-save jsdom` und `node scripts/test_reading_stream_dom.cjs`; Vorlesen und Seitenleiste mit Playwright: `node scripts/test_reading_stream_vorlesen.cjs`, `node scripts/test_reading_stream_sidebar.cjs`.

## Ablage und Historie

- `data/`: freier Kern, kanonische strukturierte Daten; Git ist die massgebliche Quelle. Darin seit v0.13 auch `navigation/` (Kanon- und Zählgerüst, Testkonfiguration) und `summaries/` (Zusammenfassungen je Ebene, Entwürfe), seit v0.14 `background/` (Hintergrund damals).
- `data-nc/`: Studienschicht für nicht kommerziell lizenzierte Quellen (noch leer), siehe [LIZENZEN.md](LIZENZEN.md).
- `schema/`: generisches Schema mit allen Typen und Statuswerten; typspezifische Schemas folgen.
- `scripts/`: Prüfung, Import, Bibelstellen-Werkzeug; `scripts/migrations/` dokumentierte Datenmigrationen.
- `app/reading-stream/`: Lesestrom; `template.html` ist die Vorlage, `index.html` die erzeugte eigenständige Seite (nicht von Hand bearbeiten).
- `app/prototype/`: abgelöster Studienprototyp (Zwischenstand, wird mitgebaut, nicht weiterentwickelt).
- `reports/`: Auswertungen; `working-text-counts.json` ist eine ältere Demonstration ohne Aussagekraft für die Perikope.
- `archive/packages/`: fünf unveränderte Originalpakete v0.1–v0.5.
- `provenance/`: Paketprüfsummen, Dateiinventar und Migrationsprotokolle (`provenance/migrations/`).

Die fünf Archiv-Commits auf GitHub dokumentieren rekonstruierte Paketstände, keine ursprüngliche Entwicklungshistorie. Ihre Zuordnung steht in `provenance/github-imports.json`. Die ZIP-Dateien enthalten zusätzlich die unveränderten Originalbytes. Eigene Inhalte stehen unter CC0 1.0 ([LICENSE](LICENSE)); übernommene Fremddaten behalten ihre Lizenz und sind in [LIZENZEN.md](LIZENZEN.md) aufgeführt.
