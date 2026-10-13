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
- Quellenkatalog: Jede Quelle hat einen `source`-Datensatz mit `catalog` (Nutzungsrecht, Verwendung, Begründung) in `data/sources/`, gepflegt über `scripts/authoring/quellen_katalog.py`. Bei jedem Import, jeder neuen Quelle und jeder Lizenzänderung den Katalog nachführen und `scripts/build_source_map.py` ausführen; der Validator prüft, dass jede Herkunftsadresse im Katalog steht und verwendete Quellen auf vorhandene Dateien zeigen. Anfragen an Rechteinhaber und deren Antworten in [docs/ANFRAGEN.md](docs/ANFRAGEN.md) protokollieren.
- Lizenzgrundsatz ([LIZENZEN.md](LIZENZEN.md)): eigene Inhalte CC0. Freier Kern `data/`: nur gemeinfreie, CC0-, CC-BY- und CC-BY-SA-Quellen (bei gleichwertiger Wahl die freiere). Nicht kommerzielle Quellen nur in `data-nc/`, nie mit Kerndaten vermischen; Kerndaten verweisen nicht auf `data-nc/`. Geschützte Quellen und «used with permission»-Daten nie übernehmen, nur zitieren. Jede Fremddatei in LIZENZEN.md aufführen.
- Erwähnt ein Erklärtext ein Wort der Ursprache («das griechische Wort für …»), das Wort als `terms` erfassen (Sprache, Originalschrift, Umschrift bei Nicht-Griechisch, Bedeutung), damit die App es mit Umschrift und Anhören-Knopf zeigt.
- Jede weitere Sprach- oder Mundartfassung ist eine eigene Übersetzungsschicht aus dem Urtext (`language` nach BCP-47, `target_context`, `orthography_de`, `register_de`, `decisions`, Wortzuordnung), nie aus dem Hochdeutschen abgeleitet; die hochdeutsche Fassung dient nur als Kontrolle (`control_translation`). Prüfung durch muttersprachliche Personen eintragen, nicht behaupten.
- Übersetzungen erklärender Inhalte (Befunde, Deutungen, Hintergrund, Zusammenfassungen …) als eigene `localization`-Datensätze mit `source_fingerprint` ablegen, nie in den Originaldatensatz schreiben ([docs/DATENMODELL.md](docs/DATENMODELL.md)).
- Bibelstellen in Erklärtexten als Marke `[[MAT.6.34]]` schreiben, nicht als «Mt 6,34» ([docs/BIBELSTELLEN.md](docs/BIBELSTELLEN.md)). Felder mit Inhalt in der Sprache einer Übersetzungsschicht sprachneutral benennen; `_de` nur für hochdeutsche Originale und Dokumentation.
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
