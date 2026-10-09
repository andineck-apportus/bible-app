# Gesichertheit statt Lektorat

Grundsatz aus der [Vision](VISION.md): Die Textbasis ist nicht ein von Personen entschiedenes Richtig/Falsch, sondern alle Lesarten werden ausgegeben und nach Gesichertheit bewertet. Dieses Dokument beschreibt, wie das in den Daten umgesetzt ist (Stand v0.8).

## Bausteine

| Baustein | Typ | Inhalt |
|---|---|---|
| Variantenstelle | `variant` | Alle Lesarten einer Stelle, an die Wörter gebunden (`base_tokens`). `evidence_level` sagt, worauf die Angaben beruhen: `edition_apparatus` (gedruckte Editionen) oder berichtete Handschriften. |
| Methode | `assessment_method` | Frage, Eingangsdaten, Vorgehen, Skala und **Annahmen und Grenzen** einer Bewertungsart. |
| Bewertung | `assessment_set` | Ergebnisse einer Methode für viele Stellen (je Kapitel eine Datei): pro Lesart Stützung, Anteil und Stufe. |

Regeln:
- Eine Bewertung **entscheidet nicht**; sie misst etwas Bestimmtes und sagt, was sie nicht misst.
- Mehrere Methoden können für dieselbe Stelle nebeneinander stehen und sich widersprechen. Die Darstellung zeigt sie gemeinsam.
- Jede Bewertung nennt ihre Methode; maschinell berechnete Bewertungen sind reproduzierbar (Skript im Repository).
- Fachurteile von Personen sind eine eigene Methode, namentlich und datiert.
- Bewertungen, die NC-Quellen verwenden, liegen in `data-nc/` ([LIZENZEN.md](../LIZENZEN.md)).

## Methode 1: Übereinstimmung der Editionen (`METHOD-EDITION-AGREEMENT-V1`)

Zählt pro Lesart, wie viele von fünf Editionen (SBLGNT, Westcott-Hort, Tregelles, NA28, Robinson-Pierpont) sie im Text haben. Stufen: breit (≥ 4), mehrheitlich (3), geteilt (2), vereinzelt (1), keine (0).

Beispiel Mk 3,25:

| Stelle | Lesart | Editionen | Stufe |
|---|---|---|---|
| οὐ ___ | δυνήσεται «wird können» | SBLGNT, WH, Tregelles, NA28 | breit |
| | δύναται «kann» | RP | vereinzelt |
| ___ | ἡ οἰκία ἐκείνη σταθῆναι | SBLGNT, NA28 | geteilt |
| | ἡ οἰκία ἐκείνη στῆναι | WH, Tregelles | geteilt |
| | σταθῆναι ἡ οἰκία ἐκείνη | RP | vereinzelt |

Ergebnis für das ganze Markusevangelium (929 Stellen): Die SBLGNT-Lesart ist 707-mal breit, 182-mal mehrheitlich, 34-mal geteilt und 6-mal vereinzelt gestützt; an 13 Stellen haben zwei Lesarten gleich viele Editionen.

**Was diese Methode nicht misst:** die Bezeugung in Handschriften. Die Editionen sind keine unabhängigen Zeugen; «4 gegen 1» heisst oft «kritische Editionen gegen byzantinischen Mehrheitstext». Die Angaben zu den Editionen stammen aus dem SBLGNT-Apparat und sind nicht an den Editionen selbst geprüft.

## Geplante weitere Methoden (Vorschlag, nicht vereinbart)
- **Handschriftenbezeugung:** Alter, geografische Verbreitung und Textgruppe der Zeugen, aus offenen Transkriptionen (NTVMR CC BY 4.0, CNTR).
- **Frühe Zeugen:** Stützung durch Handschriften bis 400 n. Chr. (CNTR).
- **Alte Übersetzungen und Kirchenväter**, soweit offen verfügbar.
- **Zitierte Fachurteile:** z. B. Einschätzungen aus ECM oder Kommentaren, als Verweis mit Fundstelle.
- **Fachurteil im Projekt:** namentlich, datiert, mit Begründung.

## Darstellung (Vorschlag)
Lesetext mit der jeweils am breitesten gestützten Lesart, Stellen mit Unterschieden markiert; beim Antippen alle Lesarten mit Stufe je Methode und den Grenzen der Methode. Die Hervorhebung ist eine Darstellungsentscheidung, keine Aussage über richtig/falsch.
