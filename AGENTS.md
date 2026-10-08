# Arbeitsregeln für bible-app

## Massgeblicher Stand
README.md sowie docs/STATUS-UND-ROADMAP.md zuerst lesen. Git ist Source of Truth; eine künftige SQLite-Datenbank ist nur eine reproduzierbare Projektion. Bestehende Daten nicht wegen einer plausibel klingenden neuen Deutung überschreiben.

## Inhaltliche Regeln
- Quellen/Lesarten, Textbefunde, Interpretation, Prinzip und Anwendung getrennt halten.
- Mehrere begründbare Deutungen und Gegenargumente erhalten; Präferenz als redaktionelle Entscheidung kennzeichnen.
- Edition, Handschrift und Übersetzung nie gleichsetzen. Sekundärtranskription nicht als eigene Faksimile-Prüfung darstellen.
- Fehlende Originaltexte, Belege, Token, Wortzahlen oder Prüfer niemals erfinden.
- Historischen Kontext und heutigen Anwendungskontext gesondert modellieren.
- Epoche, Ort/Land, Kultur, Sprache, Zielgruppe/Situation und Wissensstand berücksichtigen.
- Alle relevanten Objekte unterstützen mehrere kontrollierte Tag-IDs. Tags ersetzen keine typisierten Beziehungen.
- Inhaltliche Revisionen mit Vorgänger, Datum, Grund und Quellenstand festhalten. Frühere Positionen müssen rekonstruierbar bleiben.
- `draft`, `review_pending`, `reference_only` und `imported_unreviewed` sind keine fachliche Freigabe. Konfidenz ist kein Prüfstatus.
- Quellenbezogene Rechte und Attribution vor Textimport prüfen; keine modernen Bibeln oder Apparate pauschal kopieren.

## Technische Regeln
Stabile IDs erhalten. Neue Schema-/Typänderungen explizit migrieren. Vorhandene Metadaten nicht stillschweigend normalisieren. `archive/packages/` und deren Prüfsummen nicht verändern. Bei Codeänderungen die relevanten bestehenden Prüfungen ausführen; deren Grenzen im Ergebnis benennen.

## Zusammenarbeit
KI kann recherchieren, Entwürfe strukturieren, Quellen zuordnen, Inkonsistenzen zeigen und Prüfungen ausführen. Fachliche Bewertung und Review dürfen nicht als geschehen ausgegeben werden, wenn keine prüfende Person bzw. Prüfung dokumentiert ist. Neue technische Vorschläge klar von bereits vereinbarten Anforderungen trennen.
