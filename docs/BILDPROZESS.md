# Bilder, die man lesen kann – Erstellung und Prüfung (Vorschlag)

Stand 2026-10-23, Vorschlag zur Entscheidung durch Andi Neck. Ergänzt [BILDSPRACHE.md](BILDSPRACHE.md) und
[BILDAUFTRAEGE-ANLEITUNG.md](BILDAUFTRAEGE-ANLEITUNG.md); nach dem Entscheid werden die dortigen Regeln angepasst.

## Ziel

Die Bilder sollen den gelesenen Text grafisch wiedergeben. Man soll die Bibel auf jeder Ebene (Bibel, Testament, Buchgruppe,
Buch, Kapitel, Abschnitt, Merkvers) auch in Bildform lesen und verstehen können: Wer das Bild ansieht, erkennt die Stelle und
ihre Kernaussage, ohne die Legende zu lesen.

Rückmeldung vom 2026-10-23 (Andi Neck): Aus den Bildern lässt sich selten auf den Text schliessen, auch bei bekannten Stellen.
Was gut funktioniert: die festen Erkennungszeichen (Gott, Jesus, Geist) und der Symbolindex.

## Warum die heutigen Bilder schwer zu lesen sind

1. **Sprechblasen als Bilderrätsel.** Gesagtes steht als Folge von bis zu sechs Zeichen ohne Worte. Abstrakte Begriffe
   (Gnade, Glaube, Hoffnung, Gerechtigkeit) werden zu Zeichenketten, die man erst entschlüsseln muss.
2. **Abstraktes überwiegt.** Viele Felder zeigen zwei Figuren und Zeichen statt der Szene, an der man eine Geschichte
   erkennt (Sturm auf dem See, Hand auf dem Aussätzigen, leeres Grab).
3. **Kein Erkennungsmoment.** Ein Feld deckt oft mehrere Verse ab und zeigt einen Durchschnitt statt des einen Augenblicks,
   den man mit der Stelle verbindet.
4. **Gleich aussehende Nebenfiguren.** «Menge», «Jünger», «Mann» unterscheiden sich kaum von Bild zu Bild.
5. **Gleiche Form für alle Textarten.** Erzählung, Rede, Brief, Gebet und Lehre werden gleich gebaut; dadurch erscheinen
   Aufträge als Tatsache (Titus) und Reden als Handlung.
6. **Die Prüfung misst das Falsche.** Der Blindtest bekam die Legende dazu. Er prüfte, ob Bild und Legende zusammenpassen,
   nicht, ob man das Bild allein versteht.

## Leitlinien für verständliche Bilder

1. **Ein Feld, ein Kernmoment.** Jedes Feld zeigt den Augenblick, an dem man die Stelle erkennt: wer tut was mit wem,
   wer sagt was zu wem. Lieber ein starkes Feld als drei schwache.
2. **Konkret vor abstrakt.** Ort, Gegenstände, Gesten und Haltung erzählen zuerst. Abstrakte Zeichen nur aus einem kleinen,
   getesteten Grundbestand (rund 30, im Symbolindex erklärt), höchstens zwei je Feld.
3. **Wenige Worte im Bild** (Entscheid nötig, heute verboten):
   - ein Stichwortband je Feld mit 1–4 Wörtern aus dem Wortlaut der gewählten Übersetzung, z. B. «Steh auf!»,
     «Selig die Armen», «Wer bist du?»;
   - in Sprechblasen ein Kernwort plus höchstens zwei Zeichen statt einer Zeichenkette.
   Die Worte kommen aus der Übersetzungsschicht (Hochdeutsch, Züridüütsch, später weitere Sprachen); das Bild bleibt eines,
   nur das Wortband wechselt mit der Sprache. Bilderbibeln und Comics verankern Bilder genau so.
4. **Bildtyp nach Textart.** Die Textart bestimmt die Form:

   | Textart | Bildtyp |
   |---|---|
   | Erzählung | Szene im Ablauf (1–3 Felder), Erkennungsmoment gross |
   | Rede, Lehre, Gleichnis | Redner klein am Rand, Inhalt gross als «Bild im Bild» (Gleichnis als eigene Szene) |
   | Auftrag im Brief | Briefrahmen mit Absender und Empfänger («Paulus an Titus»), darin die verlangte Handlung |
   | Aussage über Gott, Christus, Heil | Schema: benannte Grössen mit Pfeilen (Ursache → Wirkung) |
   | Aufzählung (Tugenden, Laster, Gebote) | Raster mit Wort und Zeichen je Eintrag |
   | Gebet, Lob, Klage | Betende Figur, Gott als Gegenüber, Kernwort des Gebets |

5. **Ebenengerecht.**
   - Bibel, Testament, Buchgruppe, Buch: Zeitleiste oder Karte mit beschrifteten Stationen statt Bilderrätsel.
   - Kapitel: Bildfolge der Abschnitte, je Feld der kurze Abschnittstitel.
   - Abschnitt: 1–3 Felder im Erzählverlauf.
   - Merkvers: ein Bild mit dem Verswort.
6. **Wiedererkennbare Personen.** Hauptfiguren mit festem Erkennungszeichen wie heute bei Gott und Jesus; bei erstem
   Auftreten in einem Bild auf Wunsch mit Namensschild. Nebenfiguren je Geschichte mit eigener Farbe.
7. **Auf dem Handy lesbar.** Höchstens zwei Felder nebeneinander, Mindestgrösse für Zeichen und Schrift, im Abschnitt
   höchstens drei Felder.

## Ablauf je Stelle

1. **Textanalyse** (KI-Bearbeiter, strukturiert, im Bildauftrag gespeichert):
   - `mode`: Erzählung, Rede, Gleichnis, Auftrag, Aussage, Aufzählung, Gebet;
   - `voice`: wer im Text spricht (bei Briefen der Verfasser), bei Auftrag zusätzlich der Empfänger;
   - `core_de`: Kernaussage in einem Satz;
   - `moment_de`: der Erkennungsmoment je Feld;
   - `keywords`: 1–4 Wörter je Feld, wörtlich aus der Übersetzung;
   - Personen, Orte, Gegenstände, Ursache → Wirkung.
2. **Bildentwurf** nach dem Bildtyp der Textart.
3. **Automatische Regelprüfung** (`scripts/validate.py`, blockiert die Veröffentlichung):
   - Pflichtfelder vorhanden; Stichwörter stehen so im Text;
   - wer im Bild spricht, spricht oder wird angesprochen im Text; bei Briefen spricht der Verfasser oder er wird zitiert;
   - bei `mode: Auftrag` Briefrahmen und Legende «Auftrag an …»;
   - höchstens zwei abstrakte Zeichen je Feld, nur aus dem getesteten Grundbestand;
   - jede Figur der Legende ist im Bild mit Gesicht zu sehen.
4. **Zeichnen** in beiden Stilen.
5. **Blindtest ohne Legende.** Ein unabhängiges KI-Modell sieht nur das Bild, die Ebene und das Buch, nicht Auftrag und Legende:
   - (a) Welche Stelle ist es? Auswahl aus vier Kandidaten derselben Ebene, z. B. den Abschnitten desselben Kapitels;
   - (b) Was geschieht oder wird gesagt? Freie Beschreibung;
   - (c) Wer ist wer? Geschieht etwas oder wird es verlangt?
   Ein zweiter Durchgang vergleicht die Antworten mit `core_de`, `moment_de` und `voice` und vergibt Punkte.
6. **Nachbessern** bis zum Zielwert, höchstens drei Runden. Was danach offen ist, kommt auf eine kurze Liste für Andi Neck.
7. **Prüfprotokoll** im Bild-Datensatz: Datum, Modell, Punktzahl, offene Punkte, Fingerabdruck von Text und Bild.
   Ändert sich eines davon, gilt die Prüfung als veraltet.
8. **Rückmeldung aus der App** (später): bei der Legende «Bild verständlich? ja / nein». Gesammelte Antworten fliessen in
   die Regeln und die Liste der nachzubessernden Bilder.

## Zielwerte

| Messgrösse | Ziel |
|---|---|
| Stelle richtig erkannt (Blindtest a) | mindestens 80 % je Buch |
| Kernaussage getroffen (Blindtest b, 0–2 Punkte) | im Mittel mindestens 1,5 |
| Wer-ist-wer und Erzählung/Auftrag (Blindtest c) | ohne Fehler |
| Einzelzeichen im Grundbestand allein erkannt | mindestens 70 %, sonst neu zeichnen oder durch ein Wort ersetzen |

Die Zahlen sind KI-Messungen. Sie ersetzen keine Prüfung mit Leserinnen und Lesern; die Rückmeldungen aus der App sind
dafür der Anfang.

## Zeichen-Grundbestand

Jedes abstrakte Zeichen wird einzeln getestet: Ein Modell sieht nur das Zeichen und nennt die Bedeutung, dazu eine Auswahl aus
vier Begriffen. Was nicht erkannt wird, wird neu gezeichnet oder durch ein Wort ersetzt. Der Grundbestand steht im Symbolindex
mit Erklärung; nur er darf in Bildern abstrakt verwendet werden.

## Einführung in Etappen

1. **Ausgangslage messen:** Blindtest ohne Legende für alle 537 Bilder. Ergibt je Buch und Ebene die heutigen Werte.
2. **Pilot:**
   - Regeln, neue Felder, Bildtypen und Stichwortband im Zeichner einbauen;
   - neu erstellen: Rut (Erzählung), Titus (Brief), Markus 5 (Heilungen) und die Bergpredigt Mt 5–7 (Rede);
   - Werte vorher und nachher vergleichen; Andi Neck sieht sich den Pilot an.
3. **Ausrollen** auf alle Bücher mit KI-Bearbeitern in Gruppen, mit Liste der offenen Fälle.
4. **Zeichen-Grundbestand** testen und bereinigen, Symbolindex nachführen.

## Zu entscheiden

1. Worte im Bild: Stichwortband und Kernwort in Sprechblasen erlauben? (Empfehlung: ja)
2. Zielwerte wie oben?
3. Pilotstellen wie oben?
4. Namensschilder für Hauptfiguren beim ersten Auftreten: ja oder nur über die Legende?
