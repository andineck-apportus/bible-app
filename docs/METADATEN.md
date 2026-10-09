# Metadaten und Zeitmodell

Diese Dokumentation fasst die vereinbarten Anforderungen zusammen. Sie ist kein Beleg dafür, dass alle Felder im bisherigen Prototyp bereits vorhanden sind.

| Bereich | Bereits vorhanden | Ziel / Ergänzung |
|---|---|---|
| Identität | Stabile `id`, `type` | Schema-Version, konsistente Typnamen |
| Tags | Mehrere kontrollierte `tags`; `labels.de` | Mehrsprachige Labels; optionale freie Tags |
| Herkunft | Quellen-URLs, bibliografische Hinweise, teils Prüfnotizen | Genaues Werk/Edition/Version, Autor/Herausgeber, Locator, Abruf-/Prüfdatum, Prüfmethode |
| Edition / Zeuge | Eine Edition; Zeugen als Textlisten | Getrennte stabile Editions- und Zeugen-IDs, Datierung, Schreib-/Korrekturschichten |
| Textposition | Kanonische Bibelstellen (v0.6, [BIBELSTELLEN.md](BIBELSTELLEN.md)); Token-IDs und -Positionen für SBLGNT Mk 3,22–30 | Versifikation; weitere Editionen tokenisieren |
| Import | Upstream-URL, Tag, Commit, Datei, SHA-256, Lizenzangaben, Toolversion, Importdatum (v0.6) | Lizenzangaben vor Veröffentlichung erneut prüfen |
| Sicherheit | `confidence`, teils Begründung | Einheitliche Skala, konkrete Unsicherheiten und Gegenbelege |
| Review | Mehrere Statuswerte und Verifikationsnotizen | Prüfer, Datum, Prüfgegenstand, Ergebnis und Freigabekriterien |
| Revision | Teilweise `supersedes`, `knowledge.asserted_at` | Einheitliche Revisionen mit Grund, Vorgänger und Quellenstand |
| Kontext | `period`, Region/Land, Sprache, Zielgruppe | Kultur, Ort, Situation; mehrere Kontextbezüge |

## Drei getrennte Zeitperspektiven
- **Historische bzw. Kontextzeit:** Wann spielt eine Begebenheit oder in welcher Epoche gilt eine Anwendung? Bisher überwiegend `context.period`.
- **Wissenszeit (Knowledge Time):** Seit wann wurde eine Aussage in diesem Wissensfundus vertreten, und auf welchem Forschungsstand beruhte sie? Bisher nur teilweise `knowledge.asserted_at` bzw. `decision_as_of`.
- **Gültigkeitszeit (Valid Time):** Für welchen Zeitraum beansprucht eine Aussage oder Anwendung Geltung? Noch nicht einheitlich modelliert.

Git-Zeitpunkte dokumentieren technische Änderungen. Sie ersetzen keine dieser fachlichen Zeitdimensionen. Unbekannte oder nur ungefähr bekannte Zeitangaben dürfen nicht durch erfundene exakte Daten ersetzt werden.

## Revisionen
Inhaltliche Änderungen sollen eine neue nachvollziehbare Fassung mit Vorgängerverweis und Änderungsgrund erzeugen. Eine spätere Studie kann ältere Aussagen korrigieren oder deren Geltungsbereich einschränken. Alte Aussagen bleiben rekonstruierbar. Ob Fassungen eigene Datensatz-IDs oder eigene Revisions-IDs erhalten, ist noch als Schemaentscheidung festzulegen.

## Provenienz und Status
`confidence: high` ist eine Einschätzung, keine dokumentierte Quellenprüfung. `secondary_transcription_checked` bedeutet keine eigene Handschriftenprüfung. Ein bekannter Quellenname ohne Locator ist ein Recherchehinweis, kein präziser Beleg. Die Formulierungen der alten Daten müssen bei der nächsten fachlichen Prüfung einzeln bewertet werden.

Wortzahlen sind nur zusammen mit Edition/Übersetzungsfassung, Versumfang und Zählverfahren sinnvoll. Wortformen, Tokens, Lemmata und einmalige Lemmata sind getrennte Messgrössen. Die bisherigen Beispielzählungen dürfen nicht als Statistik für die ganze Perikope ausgegeben werden.
