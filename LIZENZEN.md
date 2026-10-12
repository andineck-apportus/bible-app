# Lizenzen

## Grundsatz (festgelegt 2026-10-09)

Das Projekt soll **so frei wie möglich** sein. Betreiber der App ist ein gemeinnütziger Verein; das Projekt verfolgt keinen Erwerbszweck, sondern will neues Wissen schaffen und zugänglich verbreiten.

Die Daten sind in **zwei Schichten** getrennt:

### 1. Freier Kern (`data/`)
- **Eigene Beiträge** des Projekts (Code, Dokumentation, eigene Datensätze, Übersetzungen, Wortzuordnungen, Bewertungen, Grafiken) stehen unter **CC0 1.0** ([LICENSE](LICENSE)): ohne Bedingung nutzbar, auch kommerziell.
- Übernommen werden Quellen unter **gemeinfrei, CC0, CC BY oder CC BY-SA**. Alle erlauben jede Nutzung einschliesslich kommerzieller.
- **CC BY-SA** verlangt, dass Bearbeitungen wieder unter CC BY-SA stehen. Das gilt nur für Dateien, die direkt aus einer solchen Quelle abgeleitet sind; sie sind unten aufgeführt. Bei gleichwertiger Wahl wird die freiere Quelle (CC0/CC BY) bevorzugt.
- Wer nur den freien Kern verwendet, darf alles frei weiterverwenden; Pflichten bestehen höchstens in Namensnennung (CC BY) bzw. gleicher Lizenz (CC BY-SA) für die betroffenen Dateien.

### 2. Studienschicht für nicht kommerzielle Nutzung (`data-nc/`)
- Quellen unter **nicht kommerziellen Lizenzen** (z. B. CC BY-NC, CC BY-NC-SA, Nutzungserklärungen wie bei CATSS) dürfen für den gemeinnützigen Betrieb verwendet werden.
- Sie liegen **ausschliesslich in `data-nc/`**, jeder Datensatz trägt Lizenz und Quelle. Sie werden nie in Dateien des freien Kerns übernommen oder mit ihnen vermischt.
- Kerndaten dürfen auf NC-Datensätze nicht verweisen; NC-Datensätze dürfen auf Kerndaten verweisen. So bleibt der Kern ohne NC-Daten vollständig nutzbar.
- Ergebnisse, die aus einem Vergleich mit NC-Daten entstehen (z. B. eine Gesichertheitsbewertung, die eine NC-Quelle berücksichtigt), gehören ebenfalls in `data-nc/`.
- In der App werden NC-Inhalte mit ihrer Lizenz angezeigt; ein Export «nur freier Kern» lässt sie weg.
- Vor einer Nutzung ausserhalb des gemeinnützigen Betriebs (z. B. Weitergabe an Dritte zu deren Zwecken) gelten die jeweiligen NC-Bedingungen.

### Nicht übernommen
- **Geschützte Quellen** (z. B. NA28, ECM, BHQ, BDAG, HALOT, moderne Bibelübersetzungen) werden nicht übernommen, nur mit Fundstelle zitiert, ausser es liegt eine schriftliche Lizenz vor.
- Daten «used with permission» ohne offene Lizenz (z. B. MARBLE-Wortbedeutungen in MACULA) werden nicht übernommen.

### Beiträge Dritter
Grafiken und Bilder von Personen, Institutionen und Künstlern werden unter CC0, CC BY oder CC BY-SA angenommen; die Lizenz steht im jeweiligen Datensatz.

## Übernommene Fremddaten im freien Kern

| Pfad | Inhalt | Quelle | Lizenz | Pflicht |
|---|---|---|---|---|
| `data/tokens/SBLGNT-MRK-*.json` | Griechischer Text des Markusevangeliums, in Wörter zerlegt | SBLGNT (Faithlife/SBLGNT) | CC BY 4.0, © 2010 Society of Biblical Literature und Logos Bible Software | Namensnennung |
| `data/variants/sblgntapp-*/VAR-SBLGNTAPP-*.json` | Variantenstellen aus dem SBLGNT-Apparat | Faithlife/SBLGNT | CC BY 4.0, wie oben | Namensnennung |
| `data/annotations/MACULA-SBLGNT-MRK-*.json`, `data/counts/SBLGNT-MRK.json` | Lemma, Morphologie, Syntaxrolle, Referenten, Glossen | MACULA Greek (Clear Bible / Biblica); Glossen: Berean Interlinear (gemeinfrei), Cherith Glosses for the Greek New Testament (Andi Wu, © 2023 Cherith Analytics, CC BY 4.0) | CC BY 4.0 | «MACULA Greek Linguistic Datasets, available at https://github.com/Clear-Bible/macula-greek/»; Cherith Glosses mit Autor nennen |
| `data/annotations/MORPHGNT-SBLGNT-MRK-003-022-030.json`, `data/counts/SBLGNT-MRK-003-022-030.json` | Lemma und Morphologie Mk 3,22–30 (Pilot) | MorphGNT 6.12 (J. K. Tauber) | **CC BY-SA 3.0** | Namensnennung; Bearbeitungen dieser Dateien unter CC BY-SA |
| `archive/packages/` | Unveränderte frühere Projektpakete v0.1–v0.5 | Projekt | CC0 1.0, soweit eigene Inhalte | — |

Alle übrigen Dateien in `data/`, `docs/`, `scripts/` usw. sind eigene Beiträge unter CC0 1.0.

## Numerische Testdaten des Lesestroms

Seit v0.13 liegt das Mengengerüst als `data/navigation/NAV-PROT66-KJV.json` im freien Kern und wird in `app/reading-stream/index.html` eingebettet. Es enthält nachgezählte Kapitel-/Versanzahlen aus der von eBible.org / CrossWire als **Public Domain** ausgewiesenen KJV-Ausgabe: https://ebible.org/Scriptures/eng-kjv_usfm.zip (Quelldateien 2026-09-26). Aus dieser KJV-Quelle wurden kein Bibeltext und kein fremder Programmcode übernommen. Die Quelle weist auf besondere Druckrechte für den Übersetzungstext im Vereinigten Königreich hin. Prüfsumme und Ableitung sind in `app/reading-stream/provenance.json` dokumentiert. Eine ursprünglich im Chat benutzte, nicht lizenzierte JSON-Zählliste wurde nicht als Fremddatei ins Repository übernommen; alle Zahlen wurden für diesen Import unabhängig aus dem genannten USFM-Bestand gewonnen und abgeglichen.

Logo, Linienicons, Code und redaktionelle Entwürfe dieses Prototyps sind eigene Beiträge unter CC0, ebenso die 83 Zusammenfassungen in `data/summaries/` und die Hintergrundnotizen in `data/background/` (eigene Formulierungen; ausserbiblische Quellen wie Josephus, Mischna oder Talmud werden nur mit Fundstelle genannt, kein Text übernommen) (KI-Entwürfe aus dem Designgespräch, keine Fremdtexte). Deutsche und englische Buchnamen und Abkürzungen sind allgemeine Bezeichnungen, keine übernommenen Werkteile. Keine Assets oder Schriftdateien der Fondation Beyeler übernommen.

## Fremddaten in der Studienschicht (`data-nc/`)

Noch keine.

Hinweis: Diese Übersicht ist keine Rechtsberatung. Lizenzangaben vor jedem Import erneut prüfen und im Quellendatensatz festhalten.

## Eingebettete Markus-Daten im Lesestrom

`app/reading-stream/index.html` enthält seit v0.12 zusätzlich die unveränderte Studienprojektion aus `data/`: SBLGNT-Text/Apparat (CC BY 4.0), MACULA samt genannten Glossen (CC BY 4.0 bzw. gemeinfrei), MorphGNT-Pilotannotation (CC BY-SA 3.0). Urheber und Quellen entsprechen den obigen Einträgen; Attribution und Lizenzlinks sind auch in der eigenständigen Seite eingebettet. Die MorphGNT-Annotationen behalten CC BY-SA 3.0; eigener UI-Code und eigene Studieninhalte bleiben CC0. Die Darstellung formatiert und kürzt die Datenfelder, ohne fachliche Neubewertung.
