# bible-app

Git-versionierter Bibel-Wissensfundus: Quellen, Textbefunde, konkurrierende Interpretationen, Prinzipien und kontextabhängige Anwendungen nachvollziehbar miteinander verbinden.

**Stand: 9. Oktober 2026 · Datenstand v0.6 · Pilot Markus 3,22–30.**

Dies ist der Konzept- und Datenprototyp, noch keine lauffähige Benutzer-App. Vorhanden sind 38 strukturierte Datensätze einschliesslich 6 Tags, der importierte griechische Text Mk 3,22–30 aus MorphGNT SBLGNT 6.12 (140 Tokens mit Lemma und Morphologie, Status `imported_unreviewed`), eine einheitliche Bibelstellen-Konvention, ein generisches Schema und ein Validator. SQLite ist als abgeleitete Projektion vorgesehen, aber noch nicht implementiert. Vollständige Wortzuordnungen und eigene Handschriftenprüfungen fehlen noch.

## Einstieg

| Datei | Inhalt |
|---|---|
| [CHANGELOG.md](CHANGELOG.md) | Änderungen und Entwicklung von v0.1 bis heute |
| [docs/KONZEPT.md](docs/KONZEPT.md) | Ziel, Analyseebenen, Zoom-System und Kontextdimensionen |
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
python3 scripts/test_import.py
python3 scripts/refs.py "Mk 3,22–30"   # Stelle in kanonische Form umwandeln
```

Der Validator prüft das Schema (`schema/record.schema.json`, ausgewertete Teilmenge von JSON Schema), eindeutige IDs, Tags, Verweise zwischen Datensätzen einschliesslich Lesarten (`VAR-…:R1`) und alle Bibelstellen gegen die Konvention. Ein PASS ist keine wissenschaftliche Freigabe; typspezifische Pflichtfelder werden noch nicht geprüft.

Import des griechischen Texts (bereits ausgeführt; Ergebnis in `data/tokens/` und `data/counts/`):

```sh
curl -LO https://raw.githubusercontent.com/morphgnt/sblgnt/6.12/62-Mk-morphgnt.txt
python3 scripts/import_morphgnt.py 62-Mk-morphgnt.txt \
  --upstream-commit a2afca0e96e367fb2ca113395bae978115942dfb --upstream-ref 6.12
python3 scripts/compare_working_text.py   # Abgleich mit der alten Arbeitstranskription
```

Der Importer schreibt Quelle, Upstream-Commit, SHA-256, Lizenzangaben und Importdatum in die erzeugten Datensätze und bricht ohne Upstream-Commit oder bei unvollständigen Versen ab. Die Importtests verwenden ausschliesslich synthetische Daten im echten MorphGNT-Zeilenformat.

## Ablage und Historie

- `data/`: kanonische strukturierte Arbeitsdaten; Git ist die massgebliche Quelle.
- `schema/`: vorhandenes generisches Schema, noch nicht an alle v0.5-Typen angepasst.
- `scripts/`: Prüfung, Import, Bibelstellen-Werkzeug; `scripts/migrations/` dokumentierte Datenmigrationen.
- `reports/`: Auswertungen; `working-text-counts.json` ist eine ältere Demonstration ohne Aussagekraft für die Perikope.
- `archive/packages/`: fünf unveränderte Originalpakete v0.1–v0.5.
- `provenance/`: Paketprüfsummen, Dateiinventar und Migrationsprotokolle (`provenance/migrations/`).

Die fünf Archiv-Commits auf GitHub dokumentieren rekonstruierte Paketstände, keine ursprüngliche Entwicklungshistorie. Ihre Zuordnung steht in `provenance/github-imports.json`. Die ZIP-Dateien enthalten zusätzlich die unveränderten Originalbytes. Vor Veröffentlichung oder Weiterverbreitung fremder Texte bleiben die jeweils tatsächlichen Quellen- und Lizenzbedingungen massgeblich; es wurde keine pauschale Projektlizenz festgelegt.
