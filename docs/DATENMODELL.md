# Datenmodell: Ist-Stand und Ziel

## Vorhandene Objekte in v0.5

| Ordner | Tatsächliches `type` | Anzahl | Aufgabe |
|---|---|---:|---|
| works | work | 1 | Biblisches Werk |
| text-units | text-unit | 1 | Natürliche Texteinheit und Versbereich |
| studies | studie | 1 | Pilotstudie mit Ergebnissen und offenen Fragen |
| sources | source / dataset | 4 | Quellenhinweise und externer Datensatz |
| editions | critical_edition | 1 | Editionsidentität |
| text-samples | text_sample | 1 | Nicht verifizierte Arbeitstranskription |
| findings | finding | 4 | Textliche/literarische/textkritische Befunde |
| variants | variant | 2 | Variantenstellen und berichtete Lesarten |
| decisions | editorial_decision | 1 | Begründete, revidierbare Lesartpräferenz |
| translations | translation | 1 | Eigene deutsche Arbeitsübersetzung |
| alignments | alignment | 1 | Vorläufige Wort-/Phrasenzuordnungen |
| interpretations | interpretation | 2 | Alternative Verständnisse |
| principles | principle | 1 | Abgeleitetes Prinzip |
| contexts | context | 2 | Historischer und heutiger Kontext |
| applications | application | 1 | Kontextabhängige Anwendung |
| topics | topic | 2 | Inhaltliche Themen |
| relations | relation | 3 | Beziehungen zu Parallelstellen |
| questions | open_question | 1 | Offene Forschungsfrage |
| tags | tag | 6 | Kontrollierte Tags |

Gesamt: 36 Datensätze, einschliesslich der 6 Tags.

## Bestehende Referenzen
`work`, `primary_unit`, `subject`, `based_on`, `derived_from`, `principle`, `context`, `outputs`, `evidence_objects`, `related`, `from` und `tags` verknüpfen Datensätze. `to_ref` und `evidence_refs` enthalten teilweise freie Bibelstellenangaben. `VAR-…:R1` referenziert eine Lesart innerhalb eines Variantenobjekts.

Beispielkette: `FIND-MRK-0001` → `INT-MRK-0001` → `PRIN-MRK-0001` → `APP-MRK-0001`; die Anwendung verweist auf `CTX-CH-DE-2026`. Die textkritische Entscheidung und die Arbeitsübersetzung referenzieren eine bestimmte Lesart.

## Noch nicht implementiert
Eigene Handschriften-/Zeugenobjekte mit Korrekturschichten; vollständige Token- und Lemmaobjekte; vollständige Alignments aller neun Verse; Argumente/Gegenargumente als eigene Objekte; einheitliche Quellenbelege mit genauen Fundstellen; durchgängige Zeit- und Revisionsmetadaten; vollständige Schema-/Referenzvalidierung; SQLite-Projektion; Benutzeroberfläche.

## Kompatibilitätsbefund
Das vorhandene Schema stammt aus v0.1. Es erlaubt `study` und `text_unit`, während Daten `studie` und `text-unit` verwenden. Weitere Typen und Statuswerte kamen ohne entsprechende Schemaerweiterung hinzu. Diese Übernahme erhält die Originaldaten unverändert. Eine geplante Migration muss kanonische Typnamen bestimmen, Schema und Importer gemeinsam anpassen und die Änderung dokumentieren.
