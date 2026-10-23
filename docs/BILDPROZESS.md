# Bilder, die man lesen kann – Erstellung und Prüfung

Stand 2026-10-23. Teil der Kette [VERDICHTUNG.md](VERDICHTUNG.md) (Kernanalyse: was gezeigt und was weggelassen wird) →
**Bild** (dieses Dokument) mit den Zeichen aus [SYMBOLPROZESS.md](SYMBOLPROZESS.md). Ergänzt [BILDSPRACHE.md](BILDSPRACHE.md) und
[BILDAUFTRAEGE-ANLEITUNG.md](BILDAUFTRAEGE-ANLEITUNG.md); deren Regeln werden im Pilot angepasst.

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
3. **Wenige Worte im Bild** (Entscheid 2026-10-23: ja; Bilder werden je Übersetzung erzeugt):
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

5. **Ebenengerecht:** Umfang und Auswahl je Ebene nach VERDICHTUNG.md (ein Feld je tragendem Moment; Buch und höher
   als Zeitleiste oder Karte mit beschrifteten Stationen; Kapitel als Bildfolge der Abschnitte mit kurzem Titel).
6. **Wiedererkennbare Personen.** Hauptfiguren mit festem Erkennungszeichen wie heute bei Gott und Jesus und beim ersten
   Auftreten in einem Bild mit Namensschild (Name aus der Übersetzungsschicht; Entscheid 2026-10-23). Nebenfiguren je
   Geschichte mit eigener Farbe.
8. **Kurze, gleichmässige Legende.** Unter «Figuren und Zeichen» steht je Figur und Zeichen ein kurzer Erkennungstext von
   höchstens etwa 60 Zeichen (eine bis zwei kurze Zeilen), bei allen gleich lang gehalten, z. B. Gott: «Goldener
   Strahlenkranz mit dem Gottesnamen יהוה». Ausführliche Erklärungen stehen im Symbolindex, nicht in der Legende
   (Hinweis Andi Neck, 2026-10-23).
7. **Auf dem Handy lesbar.** Höchstens zwei Felder nebeneinander, Mindestgrösse für Zeichen und Schrift, im Abschnitt
   höchstens drei Felder.

## Ablauf je Stelle

1. **Kernanalyse** der Einheit liegt vor und ist geprüft (VERDICHTUNG.md): Kernaussage, tragende Momente mit
   Erkennungsmoment und Schlüsselwörtern, Textart, Sprecher. Das Bild zeigt genau diese Momente, ein Feld je Moment.
2. **Bildentwurf** nach dem Bildtyp der Textart; Gegenstände, Ursache → Wirkung und Gesten aus dem Text.
3. **Automatische Regelprüfung** (`scripts/validate.py`, blockiert die Veröffentlichung; dazu: Legendentext je Figur und Zeichen höchstens etwa 60 Zeichen):
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
   Ein zweiter Durchgang vergleicht die Antworten mit Kernaussage, Momenten und Sprecher der Kernanalyse und vergibt Punkte.
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

Die Zielwerte gelten vorerst zum Ausprobieren (Andi Neck, 2026-10-23). Nach dem Pilot und den ersten Rückmeldungen werden
sie überprüft: Reicht die Verständlichkeit trotz erreichter Werte nicht, werden sie angehoben oder der Test geschärft.

Die Zahlen sind KI-Messungen. Sie ersetzen keine Prüfung mit Leserinnen und Lesern; die Rückmeldungen aus der App sind
dafür der Anfang.

## Zeichen-Grundbestand

Nur getestete Zeichen dürfen abstrakt verwendet werden; Ablauf, Zielwerte und Ausgangsmessung in SYMBOLPROZESS.md.

## Einführung in Etappen

1. **Ausgangslage messen:** Blindtest ohne Legende für die heutigen Bilder der Pilotstellen (später alle 537).
2. **Vorbereiten, parallel:** Worte im Bild (Stichwortband, Wortzeichen) und Bildtypen im Zeichner; die meistverwendeten
   schwachen Zeichen neu entwerfen (SYMBOLPROZESS.md).
3. **Pilot** (VERDICHTUNG.md): Kernanalysen für Rut, Titus, Markus 5 und die Bergpredigt; nach Durchsicht durch Andi Neck
   Zusammenfassungen und Bilder daraus neu; Werte vorher und nachher.
4. **Ausrollen** auf alle Bücher mit KI-Bearbeitern in Gruppen, mit Liste der offenen Fälle.

## Entscheide

1. Worte im Bild: ja (Andi Neck, 2026-10-23). Bilder werden je Übersetzung erzeugt: gleicher Auftrag, Wortband aus der
   jeweiligen Übersetzungsschicht; das passt zum Ziel, die Bibel in verschiedene Sprachen und Kulturen zu übertragen.
2. Auswahl und Umfang über die gemeinsame Kernanalyse (VERDICHTUNG.md), Kernaussage vor Bekanntheit (2026-10-23).

3. Zielwerte wie oben, vorerst zum Ausprobieren; nach dem Pilot überprüfen (2026-10-23).
4. Namensschilder für Hauptfiguren beim ersten Auftreten in einem Bild: ja (2026-10-23).
5. Legende: kurzer, gleichmässiger Erkennungstext je Figur und Zeichen (2026-10-23).
