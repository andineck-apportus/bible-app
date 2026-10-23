# Verdichten: vom Text zu Zusammenfassung und Bild

Stand 2026-10-23, festgelegt von Andi Neck. Gilt für alle Ebenen über dem Vers: Abschnitt, Kapitel, Buch, Buchgruppe,
Testament, Bibel, dazu Merkverse. Zusammenfassung und Bild entstehen aus derselben Grundlage, der **Kernanalyse**, damit
sie dasselbe auswählen und dasselbe weglassen und nicht zweimal überarbeitet werden müssen.

Darauf bauen auf:
- [BILDPROZESS.md](BILDPROZESS.md): wie aus der Kernanalyse ein verständliches Bild wird;
- [SYMBOLPROZESS.md](SYMBOLPROZESS.md): wie die Bildzeichen entstehen und geprüft werden.

## Grundsatz

Auf jeder Ebene wird verdichtet, nicht nacherzählt. Zusammenfassung und Bild zeigen die tragenden Momente, nicht jedes Detail;
wer alles will, liest den Text. Ein Bild ist kein Comic des ganzen Textes, sondern hilft, ihn zu erfassen und zu behalten.

## Die Kernanalyse

Eine je Einheit (Abschnitt, Kapitel, Buch, Buchgruppe, Testament, Bibel), stilunabhängig und sprachunabhängig auf Hochdeutsch
festgehalten; Übersetzungen der Felder als `localization` wie bei Zusammenfassungen.

| Feld | Inhalt |
|---|---|
| `core_de` | Kernaussage in einem Satz: was will diese Einheit sagen? |
| `purpose_de` | nur Buch und höher: wozu das Buch bzw. die Gruppe geschrieben ist (Zweck, Adressaten) |
| `moments` | die tragenden Momente (Umfang je Ebene unten), je mit Bibelstelle, einem Satz, Begründung der Wahl, Erkennungsmoment und Schlüsselwörtern wörtlich aus der Übersetzung |
| `omitted_de` | was bewusst wegfällt, mit Grund |
| `mode` | Textart: Erzählung, Rede, Gleichnis, Auftrag, Aussage, Aufzählung, Gebet (bei gemischten Einheiten je Moment) |
| `voice` | wer im Text spricht (bei Briefen der Verfasser), bei Auftrag zusätzlich der Empfänger |
| `persons`, `places` | wichtige Personen und Orte (IDs aus dem Bildlexikon) |
| `basis` | Fingerabdrücke des Textes bzw. der Kernanalysen darunter (veraltet, wenn sich etwas ändert) |

## Was ausgewählt wird

Ein Moment wird gewählt, wenn er möglichst viele dieser Fragen bejaht, in dieser Reihenfolge des Gewichts:

1. **Trägt er die Kernaussage?** Die Kernaussage geht vor der Bekanntheit (Entscheid 2026-10-23).
2. **Betont ihn der Text selbst?** Wendepunkt, Höhepunkt einer Rede, wörtliche Rede an der entscheidenden Stelle,
   Wiederholung, Rahmen (Anfang und Schluss).
3. **Zeigt er den Bogen?** Bei längeren Einheiten Anfang, Wendepunkt und Ausgang.
4. **Erkennt man daran die Stelle?** Der Erkennungsmoment, z. B. Brot und Fische, nicht die Zahl der Körbe.

Weggelassen werden, wenn sie die Kernaussage nicht tragen: Nebenfiguren, Zahlen, Ortsangaben, Wiederholungen, Übergänge.
Erklärungen gehören in «Hintergrund damals», nicht in Zusammenfassung oder Bild. Nichts wird hinzugefügt, was der Text nicht
sagt; eine Deutung wird als Deutung gekennzeichnet.

## Umfang je Ebene

| Ebene | Momente | Zusammenfassung | Bild |
|---|---|---|---|
| Abschnitt | 1–3 | 2–4 Sätze | 1–3 Felder, ein Feld je Moment |
| Kapitel | ein Moment je Hauptabschnitt, höchstens 4 | 3–5 Sätze | höchstens 4 Felder |
| Buch | 4–6 Stationen | 4–6 Sätze | Zeitleiste oder Karte mit den Stationen |
| Buchgruppe, Testament, Bibel | 4–6 Stationen | 4–6 Sätze | Stationen mit Beschriftung |
| Merkvers | 1 | – (der Vers selbst) | ein Bild mit dem Verswort |

## Von unten nach oben, von oben nach unten

- **Von unten:** Das Kapitel wählt seine Momente aus den Momenten seiner Abschnitte, das Buch aus den Kapiteln, die
  Buchgruppe aus den Büchern, das Testament aus den Gruppen. Was oben steht, kommt immer aus der Ebene darunter; oben kann
  nichts erscheinen, was unten fehlt.
- **Von oben:** Bevor ein Buch seine Stationen wählt, wird sein Zweck festgehalten (`purpose_de`). Gewählt wird, was diesen
  Zweck trägt. Dasselbe gilt für Buchgruppe, Testament und Bibel.
- Reihenfolge der Arbeit je Buch: Abschnitte → Zweck des Buches → Kapitel → Buch; danach Buchgruppe und höher, wenn alle
  Bücher der Gruppe so weit sind.

## Ablauf

1. **Kernanalyse** erstellen (KI-Bearbeiter), von unten nach oben wie beschrieben.
2. **Prüfung der Kernanalyse** durch eine getrennte KI-Instanz gegen den Text: Ist die Kernaussage belegt? Tragen die
   gewählten Momente sie? Fehlt etwas Wesentliches? Stimmen Textart und Sprecher? Abweichungen werden nachgebessert.
3. **Zusammenfassung** aus der Kernanalyse neu schreiben (alle Zusammenfassungen werden neu erstellt, Entscheid
   2026-10-23), mit dem Umfang der Ebene; danach die sprachliche Prüfung in allen Sprachen (AGENTS.md).
4. **Bildauftrag** aus denselben Momenten (BILDPROZESS.md).
5. **Gemeinsame Prüfung:** Zusammenfassung und Bild nennen dieselben Momente; das Bild besteht den Blindtest ohne Legende;
   beide stimmen mit dem Text überein. Frühere Fassungen bleiben im revision_log.
6. **Synchron halten:** Ändert sich der Text oder eine Kernanalyse darunter, gelten Kernanalyse, Zusammenfassung und Bild
   darüber als veraltet und werden in dieser Reihenfolge erneuert.

## Werkzeug und Ablage

- Eingabe der Bearbeiter: `scripts/authoring/kernanalysen_daten/<BUCH>.json` (eine Liste von Einheiten).
- `python3 scripts/authoring/kernanalyse.py [BUCH …]` prüft und schreibt `data/core-analyses/CORE-<suffix>.json`
  (Typ `core_analysis`).
- Geprüft werden:
  - Umfang je Ebene und Pflichtfelder;
  - Stellen innerhalb der Einheit;
  - Schlüsselwörter wörtlich in der hochdeutschen Arbeitsübersetzung;
  - Personen und Orte im Bildlexikon;
  - Momente höherer Ebenen aus Momenten der Ebene darunter.
- `basis` hält Fingerabdrücke fest: beim Abschnitt des Textes, darüber der Kernanalysen der Kinder. Erneuert werden sie
  nur mit `BIBLE_CORE_CONFIRM=1`, nach einer Prüfung.

- Zusammenfassungen aus der Kernanalyse: `scripts/authoring/zusammenfassungen_daten/<BUCH>.json` (Hochdeutsch und
  Züridüütsch je Einheit), `python3 scripts/authoring/zusammenfassungen.py [BUCH …]` prüft Umfang und Momente und schreibt
  Datensatz, Mundart-Lokalisierung, revision_log und `core_basis` (Kernanalyse mit Fingerabdruck). Ältere
  Autorenwerkzeuge übernehmen diese Texte über `scripts/authoring/_lib.py`, damit ein erneuter Lauf sie nicht zurücksetzt.

## Pilot

Rut (Erzählung), Titus (Brief), Markus 5 (Heilungen) und die Bergpredigt Mt 5–7 (Rede), jeweils mit Kapitel und Buch.
Andi Neck sieht sich die Kernanalysen an, bevor Zusammenfassungen und Bilder neu entstehen.
