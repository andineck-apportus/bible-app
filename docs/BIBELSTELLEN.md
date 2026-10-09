# Bibelstellen: kanonische Schreibweise

Ab v0.6 werden alle Bibelstellen in den Daten in genau einer maschinenlesbaren Form gespeichert. Sie ist die Grundlage für Verknüpfung, Zoom, Suche, Zählungen und die spätere SQLite-Projektion. Deutsche Schreibweisen wie «Mk 3,29» sind nur Anzeige und werden nie als Referenz gespeichert.

## Form

| Umfang | Kanonisch | Anzeige (de) |
|---|---|---|
| Buch | `MRK` | Mk |
| Kapitel | `MRK.3` | Mk 3 |
| Vers | `MRK.3.29` | Mk 3,29 |
| Versbereich | `MRK.3.22-MRK.3.30` | Mk 3,22–30 |
| Kapitelübergreifend | `JHN.3.16-JHN.4.2` | Joh 3,16–4,2 |
| Kapitelbereich | `PSA.23-PSA.24` | Ps 23–24 |

Regeln:
- Buchcodes nach **USFM/Paratext** (drei Zeichen, z. B. `MAT`, `MRK`, `LUK`, `JHN`, `1CO`). Die vollständige Liste steht in `scripts/refs.py`.
- Kapitel und Vers sind positive Ganzzahlen ohne führende Nullen, getrennt durch Punkte.
- Bereiche nennen beide Enden vollständig (`MRK.3.22-MRK.3.30`, nicht `MRK.3.22-30`). Beide Enden haben dieselbe Genauigkeit, liegen im selben Buch, und das Ende liegt nach dem Anfang.
- Mehrere getrennte Stellen sind eine Liste von Stellen, kein zusammengesetzter Text.
- Die deutsche Anzeige folgt den Loccumer Richtlinien (Mt, Mk, Lk, Joh, Apg, Röm, 1 Kor …).

## Was nicht in die Stelle gehört
- **Wort- oder Tokenposition:** wird über Token-IDs bzw. Token-Positionen der jeweiligen Edition angegeben (z. B. `TOK-SBLGNT-MRK-003-029-004`), nicht über Zusätze wie «29a».
- **Lesart:** wird über das Variantenobjekt referenziert (`VAR-MRK-003-029-001:R1`).
- **Edition/Übersetzung:** steht in eigenen Feldern; die Stelle selbst ist editionsneutral.

## Versifikation
Eine Stelle bezieht sich vorerst auf die übliche Versifikation der verwendeten Ausgangsedition (für das NT: SBLGNT/NA28). Abweichende Zählungen (z. B. Psalmüberschriften, Joel 3/4, Maleachi 3/4, deutsche gegenüber hebräischer Zählung) sind bekannt, aber noch nicht modelliert. Wenn ein Datensatz mit abweichender Zählung arbeitet, muss ein künftiges Feld `versification` sie angeben; eine Zuordnungstabelle ist offen.

## Werkzeuge
- `scripts/refs.py` prüft kanonische Stellen (`parse`), wandelt lockere Eingaben um (`canonical("Mk 3,22–30")` → `MRK.3.22-MRK.3.30`) und erzeugt die Anzeige (`display_de`).
- `scripts/validate.py` prüft alle Stellenfelder der Daten gegen diese Konvention.
- Ob ein Vers in einem Kapitel tatsächlich existiert, wird noch nicht geprüft; dafür fehlt eine Versifikationstabelle.

## Felder mit Bibelstellen
`reference`, `to_ref`, `range` (Bereich der Texteinheit), die Listen `evidence_refs` und `imported_scope`, die Schlüssel von `text_by_reference` sowie `tokens[].reference`. Neue Felder mit Stellen müssen in `scripts/validate.py` (`REF_FIELDS` bzw. `REF_LIST_FIELDS`) eingetragen werden.

## Migration
Die v0.5-Daten verwendeten `Mk 3:29`, `Mark 3:29`, `Mk 3:22-30` und `{"start": "3:22", "end": "3:30"}`. Sie wurden am 2026-10-09 mit `scripts/migrations/v0_6.py` umgestellt; jede Änderung mit altem und neuem Wert steht in `provenance/migrations/2026-10-09-v0.6.json`.
