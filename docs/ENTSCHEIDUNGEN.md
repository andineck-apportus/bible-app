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
- Bibelstellen werden einheitlich kanonisch gespeichert (USFM-Buchcodes, `MRK.3.29`, `MRK.3.22-MRK.3.30`); deutsche Schreibweise nur als Anzeige ([BIBELSTELLEN.md](BIBELSTELLEN.md), festgelegt 2026-10-09).
- Typnamen in `snake_case` (`study`, `text_unit`), festgelegt 2026-10-09.
- Griechischer NT-Grundtext für den Pilot: SBLGNT mit MorphGNT-Annotation, Version 6.12, per Commit fixiert.

## Bereits vorliegende Umsetzung
38 JSON-Datensätze in v0.6; 6 kontrollierte Tags; generisches Schema mit allen Typen/Statuswerten; Validator für Schema, Verweise und Bibelstellen; MorphGNT-Import Mk 3,22–30 mit Quellnachweis; synthetische Importtests. Der tatsächliche Bestand ist massgeblich gegenüber früheren Zusammenfassungen, die Implementierung und Ziel teilweise vermischen.

## Noch offen
Frontend, Backend, Hosting, Authentifizierung, API, konkrete SQLite-Tabellen, Versifikationsmodell, Revisions-ID-Konvention, vollständige Schemas, Zuständigkeiten für Review, Lizenz für eigene Projektanteile sowie genaue Auswahl und Lizenzierung künftiger Textbestände.

Aus anderen Projekten des Nutzers werden keine Technologieentscheidungen automatisch übernommen.
