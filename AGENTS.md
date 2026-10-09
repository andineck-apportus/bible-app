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
- Lizenzgrundsatz ([LIZENZEN.md](LIZENZEN.md)): eigene Inhalte CC0; nur gemeinfreie, CC0- oder CC-BY-Quellen übernehmen; CC BY-SA nur ohne freiere Alternative und in LIZENZEN.md aufführen; NC/geschützte Quellen nie übernehmen, nur zitieren.
- Keine Lektoratsentscheidung über richtig/falsch: Unterschiede ausgeben und nach Gesichertheit bewerten, Bewertungsmethode offenlegen ([docs/VISION.md](docs/VISION.md)).

## Technische Regeln
Stabile IDs erhalten. Neue Schema-/Typänderungen explizit migrieren. Vorhandene Metadaten nicht stillschweigend normalisieren. `archive/packages/` und deren Prüfsummen nicht verändern. Bei Codeänderungen die relevanten bestehenden Prüfungen ausführen; deren Grenzen im Ergebnis benennen.

## Git-Ablauf
Der Nutzer arbeitet auch nur vom Smartphone über Claude, ohne eigenen Rechner. Deshalb führt die KI alle Git-Operationen selbständig aus, ohne Rückfrage und ohne manuellen Review-Schritt:
- Vor jeder Arbeit `origin/main` holen und darauf aufsetzen.
- Änderungen auf einem Feature-Branch committen (aussagekräftige Commit-Message), Prüfungen ausführen, Branch nach GitHub pushen.
- Den Feature-Branch selbständig nach `main` mergen und `main` pushen; gemergte Branches danach löschen, soweit die Umgebung das zulässt (in Claude-Cloud-Sitzungen blockiert der Git-Proxy das Löschen entfernter Branches; dann stehen lassen).
- Bei Konflikten mit fremden Änderungen auf `main` diese nie verwerfen; zusammenführen oder nachfragen. Kein Force-Push auf `main`.

## Zusammenarbeit
KI kann recherchieren, Entwürfe strukturieren, Quellen zuordnen, Inkonsistenzen zeigen und Prüfungen ausführen. Fachliche Bewertung und Review dürfen nicht als geschehen ausgegeben werden, wenn keine prüfende Person bzw. Prüfung dokumentiert ist. Neue technische Vorschläge klar von bereits vereinbarten Anforderungen trennen.
