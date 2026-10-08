# Festlegungen und offene Entscheidungen

## Festgehaltene Anforderungen
- Git ist Source of Truth; Datensätze in strukturiertem JSON/YAML, Dokumentation in Markdown.
- Stabile IDs, Schema-Validierung als Ziel, typisierte Beziehungen und mehrere Tags pro relevantem Objekt.
- SQLite soll eine abgeleitete, neu aufbaubare Projektion werden.
- Quelle/Überlieferung, Textbefund, Interpretation/Auslegung, Prinzip und kontextabhängige Anwendung bleiben unterscheidbar.
- Mehrere Deutungen und Anwendungen je Zeit, Ort/Land, Kultur, Sprache und Zielgruppe sind erwünscht.
- Wissensstand, fachliche Gültigkeit und Git-Historie werden nicht gleichgesetzt; Revisionen erhalten die Vergangenheit.
- Wortzahlen für Ausgangstext und Übersetzung sind editions-/fassungsgebunden und reproduzierbar.
- Pilot: Markus 3,22–30; Zoom von Wortebene bis Themenbogen und damaliger/heutiger Welt.

## Bereits vorliegende Umsetzung
36 JSON-Datensätze in v0.5; 6 kontrollierte Tags; ein generisches frühes Schema; kleiner ID-/Tag-Validator; MorphGNT-Importvorbereitung mit Quellhash; synthetischer Importtest. Der tatsächliche Bestand ist massgeblich gegenüber früheren Zusammenfassungen, die Implementierung und Ziel teilweise vermischen.

## Noch offen
Frontend, Backend, Hosting, Authentifizierung, API, konkrete SQLite-Tabellen, kanonische Typnamen, Revisions-ID-Konvention, vollständige Schemas, Zuständigkeiten für Review, Lizenz für eigene Projektanteile sowie genaue Auswahl und Lizenzierung künftiger Textbestände.

Aus anderen Projekten des Nutzers werden keine Technologieentscheidungen automatisch übernommen.
