# bible-app

Git-versionierter Bibel-Wissensfundus: Quellen, Textbefunde, konkurrierende Interpretationen, Prinzipien und kontextabhängige Anwendungen nachvollziehbar miteinander verbinden.

**Stand: 9. Oktober 2026 · Datenstand v0.8 · Markusevangelium; Pilotstudie Markus 3,22–30.**

Dies ist der Konzept- und Datenprototyp, noch keine lauffähige Benutzer-App. Vorhanden sind 1025 strukturierte Datensätze:
- der **ganze griechische Text des Markusevangeliums** (SBLGNT, 11 286 Wörter mit stabilen IDs) mit Lemma, Morphologie, Syntaxrollen, Referenten und Glossen aus MACULA Greek als eigener Annotationsschicht,
- **929 Variantenstellen** auf Editionsebene aus dem SBLGNT-Apparat, an die Wörter gebunden, jede mit einer maschinell berechneten **Gesichertheitsbewertung** (Übereinstimmung der Editionen, Methode offengelegt),
- die Pilotstudie Mk 3,22–30 mit Befunden, Deutungen, Prinzip, Anwendung und einer vollständigen deutschen Arbeitsübersetzung mit Wortzuordnung (KI-Entwurf, ungeprüft),
- eine einheitliche Bibelstellen-Konvention, ein generisches Schema und ein Validator.

Dazu kommt ein erster klickbarer **Studienprototyp für Mk 3,20–35** (`app/prototype/mk3-20-35.html`), der direkt aus diesen Daten erzeugt wird. SQLite-Projektion, eigentliche App und Handschriftenbelege fehlen noch.

## Einstieg

| Datei | Inhalt |
|---|---|
| [docs/VISION.md](docs/VISION.md) | Vision in vier Stufen: transparente Textbasis, Übertragung, Zoomstufen und Studienanleitung, Visualisierung und UX |
| [LIZENZEN.md](LIZENZEN.md) | Eigene Inhalte CC0; freier Kern und Studienschicht; Lizenzen übernommener Fremddaten |
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
python3 scripts/build_prototype.py    # Studienprototyp Mk 3,20–35 aus den Daten erzeugen
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
```

Die Importer schreiben Quelle, Upstream-Commit, SHA-256, Lizenz und Importdatum in die Datensätze und brechen bei unsicherer Zuordnung ab bzw. führen nicht zuordenbare Einträge in `reports/` auf, statt sie zu raten. `scripts/import_morphgnt.py` ist der frühere Pilot-Importer (v0.6) und wird nur noch durch `scripts/test_import.py` geprüft.

## Ablage und Historie

- `data/`: freier Kern, kanonische strukturierte Daten; Git ist die massgebliche Quelle.
- `data-nc/`: Studienschicht für nicht kommerziell lizenzierte Quellen (noch leer), siehe [LIZENZEN.md](LIZENZEN.md).
- `schema/`: generisches Schema mit allen Typen und Statuswerten; typspezifische Schemas folgen.
- `scripts/`: Prüfung, Import, Bibelstellen-Werkzeug; `scripts/migrations/` dokumentierte Datenmigrationen.
- `app/prototype/`: Studienprototyp; `template.html` ist die Vorlage, `mk3-20-35.html` die erzeugte eigenständige Seite (nicht von Hand bearbeiten).
- `reports/`: Auswertungen; `working-text-counts.json` ist eine ältere Demonstration ohne Aussagekraft für die Perikope.
- `archive/packages/`: fünf unveränderte Originalpakete v0.1–v0.5.
- `provenance/`: Paketprüfsummen, Dateiinventar und Migrationsprotokolle (`provenance/migrations/`).

Die fünf Archiv-Commits auf GitHub dokumentieren rekonstruierte Paketstände, keine ursprüngliche Entwicklungshistorie. Ihre Zuordnung steht in `provenance/github-imports.json`. Die ZIP-Dateien enthalten zusätzlich die unveränderten Originalbytes. Eigene Inhalte stehen unter CC0 1.0 ([LICENSE](LICENSE)); übernommene Fremddaten behalten ihre Lizenz und sind in [LIZENZEN.md](LIZENZEN.md) aufgeführt.
