# bible-app

Git-versionierter Bibel-Wissensfundus: Quellen, Textbefunde, konkurrierende Interpretationen, Prinzipien und kontextabhängige Anwendungen nachvollziehbar miteinander verbinden.

**Stand: 8. Oktober 2026 · übernommener Datenstand v0.5 · Pilot Markus 3,22–30.**

Dies ist der gesicherte Konzept- und Datenprototyp, noch keine lauffähige Benutzer-App. 36 strukturierte Datensätze einschliesslich 6 Tags, ein generisches Schema, ein vorbereiteter MorphGNT-Importer und ein einfacher Validator sind vorhanden. SQLite ist als abgeleitete Projektion vorgesehen, aber noch nicht implementiert. Vollständige editionsverifizierte griechische Token, vollständige Wortzuordnungen und eigene Handschriftenprüfungen fehlen noch.

## Einstieg

| Datei | Inhalt |
|---|---|
| [CHANGELOG.md](CHANGELOG.md) | Änderungen und Entwicklung von v0.1 bis heute |
| [docs/KONZEPT.md](docs/KONZEPT.md) | Ziel, Analyseebenen, Zoom-System und Kontextdimensionen |
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
```

Der bestehende Validator prüft nur Pflichtfeld-Anwesenheit, eindeutige IDs und Tag-Referenzen. Er führt **keine JSON-Schema-Validierung** durch. Ein PASS ist keine wissenschaftliche Freigabe und kein Nachweis vollständiger Modellkonsistenz; bekannte Schema-Abweichungen stehen in der Roadmap.

Der Importer benötigt eine separat beschaffte, versionierte und lizenzgeprüfte Quelldatei:

```sh
python3 scripts/import_morphgnt.py /pfad/zu/62-Mk-morphgnt.txt
```

Dieser Befehl schreibt Token- und Zähldateien in `data/`. Die Importvorbereitung ist übernommen, der reale Datenimport bleibt offen. Die Importtests verwenden ausschliesslich synthetische Daten.

## Ablage und Historie

- `data/`: kanonische strukturierte Arbeitsdaten; Git ist die massgebliche Quelle.
- `schema/`: vorhandenes generisches Schema, noch nicht an alle v0.5-Typen angepasst.
- `scripts/`: übernommene Programme.
- `reports/`: ältere Demonstrationsauswertungen, keine verifizierten Gesamtzählungen.
- `archive/packages/`: fünf unveränderte Originalpakete v0.1–v0.5.
- `provenance/`: Paketprüfsummen, Dateiinventar und nachvollziehbare Änderungen dieser Übernahme.

Die fünf Archiv-Commits auf GitHub dokumentieren rekonstruierte Paketstände, keine ursprüngliche Entwicklungshistorie. Ihre Zuordnung steht in `provenance/github-imports.json`. Die ZIP-Dateien enthalten zusätzlich die unveränderten Originalbytes. Vor Veröffentlichung oder Weiterverbreitung fremder Texte bleiben die jeweils tatsächlichen Quellen- und Lizenzbedingungen massgeblich; es wurde keine pauschale Projektlizenz festgelegt.
