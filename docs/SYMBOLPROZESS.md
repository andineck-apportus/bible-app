# Zeichen, die man erraten kann – Erstellung und Prüfung

Stand 2026-10-23 (Auftrag Andi Neck). Gegenstück zu [BILDPROZESS.md](BILDPROZESS.md) für die Bildzeichen im Lexikon
(`data/illustrations/lexicon/FIG-ZEICHEN-*`, heute 191). Personen, Orte und Gegenstände folgen denselben Schritten,
mit strengeren Zielwerten (siehe unten).

## Ausgangslage

Bisher gab es keinen eigenen Ablauf für Zeichen. Ein Zeichen entstand, wenn ein Bildauftrag einen Begriff brauchte. Die
Bedeutung wurde im Lexikon beschrieben (Pflichtmerkmale, Verwechslungen); geprüft wurde nur im Gesamtbild mit Legende.
Viele Zeichen sind deshalb eigene Abmachungen, die man ohne Legende kaum errät, z. B. offene Hände mit Licht für «Gnade»,
Herz mit Lichtstrahl für «glauben», Hand mit Brot für «gute Werke» (Rückmeldung Andi Neck, 2026-10-23: «Hand» u. a.).

## Grundsätze

1. **Eine Bedeutung je Zeichen**, überall gleich (wie heute).
2. **Bekannte Bildsprache vor eigener Erfindung.** Erst prüfen, ob es ein weit verbreitetes Piktogramm gibt (Verkehrs- und
   Informationszeichen, verbreitete Emoji, kirchliche Grundzeichen); nur wenn nicht, ein eigenes entwerfen.
3. **Konkret statt abstrakt.** Ein Begriff wird durch eine typische Handlung oder einen Gegenstand gezeigt (Metonymie):
   «vergeben» als zerrissener Schuldschein, «gute Werke» als Brot geben an eine Person. Ist das nicht möglich, wird das
   Zeichen ein **Wortzeichen**: Zeichen plus Wort aus der Übersetzung, nie allein (seit Worte im Bild erlaubt sind).
4. **Unverwechselbare Form.** Klare Umrisse, auch klein (24 px) erkennbar; Farbe nie als einziges Unterscheidungsmerkmal.
5. **Kulturell vorsichtig.** Gesten, Farben und Tiere werden in Kulturen verschieden gelesen; Varianten je Zielkontext
   werden am Lexikon-Eintrag geführt (siehe BILDSPRACHE.md), nie stillschweigend.

## Drei Klassen mit Zielwerten

| Klasse | Beispiele | Allein erkannt (frei benannt) | Auswahl aus vier |
|---|---|---|---|
| Gegenstand, Ort, Person | Brot, Krug, Tempel, Boot | mindestens 90 % | mindestens 95 % |
| Handlung, Geste, Zustand | beten, heilen, weinen, schlafen | mindestens 70 % | mindestens 85 % |
| Begriff (abstrakt) | Gnade, Glaube, Gerechtigkeit | – | mindestens 70 %, sonst Wortzeichen |

## Ablauf je Zeichen

1. **Bedarf:** Begriff, Belegstellen, wie oft er in Bildaufträgen vorkommt. Gibt es schon ein Zeichen mit derselben oder
   ähnlicher Bedeutung, wird es verwendet statt ein neues zu zeichnen.
2. **Bedeutung festlegen:** ein Satz «bedeutet …», ein Satz «bedeutet nicht …», Verwechslungskandidaten (`distinct_from`).
3. **Drei Entwürfe** aus verschiedenen Richtungen: bekanntes Piktogramm, konkrete Handlung, Gegenstand.
4. **Blindtest je Entwurf** mit getrennten KI-Instanzen, die nur das Zeichen sehen:
   - frei benennen («Was bedeutet dieses Zeichen in einer Bilderbibel? ein bis drei Wörter»);
   - Auswahl aus vier Begriffen: die Bedeutung und drei naheliegende Verwechslungen;
   - in zwei, später allen Grössen, in denen es vorkommt (24 px, 48 px).
   Eine dritte Instanz bewertet die freien Antworten gegen die Bedeutung (0 falsch, 1 verwandt, 2 getroffen).
5. **Auswahl:** bester Entwurf, der den Zielwert seiner Klasse erreicht. Erreicht keiner ihn, wird das Zeichen bei
   Gegenständen und Handlungen neu entworfen, bei Begriffen zum Wortzeichen.
6. **Kurzer Legendentext:** ein Erkennungstext von höchstens etwa 60 Zeichen für «Figuren und Zeichen», bei allen Einträgen
   gleich knapp; die ausführliche Bedeutung bleibt im Lexikon und im Symbolindex.
7. **Protokoll am Lexikon-Eintrag:** Datum, Modell, Ergebnisse, Verwechslungen; der Symbolindex zeigt die Erklärung.
8. **Im Gesamtbild prüfen:** Das neue Zeichen wird in zwei typischen Bildern verwendet und im Blindtest ohne Legende
   geprüft (BILDPROZESS.md, Schritt 5).
9. **Bei Änderungen:** Ändert sich ein Zeichen, werden alle Bilder neu gezeichnet und geprüft, die es verwenden.

## Bestand prüfen

Alle bestehenden Zeichen durchlaufen Schritt 4 als Ausgangsmessung. Ergebnis je Zeichen: behalten, neu entwerfen oder
Wortzeichen. Bericht: `reports/zeichen-blindtest-<datum>.json` und die Zusammenfassung unten.

## Figuren und Zeichen vor dem Einsatz (Entscheid 2026-10-23)

Andi Neck: Anime ist der einzige Bildstil; die Bildqualität soll allgemein besser werden; alle Figuren und Zeichen werden
vor dem Einfügen in Bilder geprüft, verbessert und erneut geprüft. Gilt für alle 569 Einträge des Bildlexikons im Stil Anime:

1. **Ausgangsmessung** ohne Legende: Personen, Rollen, Gruppen und Gott werden frei beschrieben (wer könnte das sein,
   Merkmale, Unterscheidbarkeit, Zeichenqualität); Gegenstände und Orte frei benannt. Zeichen und Handlungen: Messung
   vom 2026-10-23 (gleiche Zeichnungen wie im eingestellten Stil Symbol). Bewertung gegen Name, Identität und
   Pflichtmerkmale des Lexikons durch eine getrennte Instanz.
2. **Verbessern:** zuerst die Einträge mit schwacher Erkennung und schwacher Zeichenqualität, gewichtet nach Verwendung in
   Bildaufträgen; Personen erhalten feste, aus dem Text oder der Tradition begründete Erkennungsmerkmale.
3. **Erneut messen** mit neuen Instanzen, gleicher Test. Erst dann werden die Bilder neu gezeichnet.

## Ergebnisse

### Ausgangsmessung 2026-10-23

Alle 191 Zeichen, allein und ohne Legende, im Stil «Symbol» (Anime verwendet dieselben Zeichen). Freie Benennung durch vier
KI-Instanzen, Auswahl aus vier Begriffen durch vier andere, Bewertung durch eine fünfte. Daten:
`reports/zeichen-blindtest-2026-10-23.json`.

| Klasse | Anzahl | frei getroffen | frei mindestens verwandt | Auswahl aus vier | Ziel frei |
|---|---|---|---|---|---|
| Gegenstand, Ort, Zeit | 38 | 66 % | 82 % | 89 % | 90 % |
| Handlung, Gefühl | 99 | 47 % | 67 % | 96 % | 70 % |
| Begriff | 54 | 20 % | 69 % | 94 % | – (Wortzeichen) |

Urteil je Zeichen: 82 behalten, 60 nachbessern, 6 neu entwerfen, 43 Begriffe als Wortzeichen. Die schwachen Zeichen
machen 1539 der 2971 Verwendungen in Bildaufträgen aus. Am häufigsten verwendet und schlecht erkannt: «glauben» (87-mal,
gelesen als «Liebe Gottes»), «Tod / sterben» (81, «Grab»), «Freude» (71, «Licht»), «fliehen» (69, «eilen»), «Leben»
(53, «Baum»), «heilen» (52, «säen»), «bringen» (51, «gehen»), «verwerfen» (47, «rufen»), «Reich Gottes» (46, «Krone»).

Lehre für den Test selbst: Die Auswahl aus vier war zu leicht (89–96 %), weil die Ablenker oft zufällig und weit weg waren.
Künftig wählt eine KI-Instanz drei naheliegende Verwechslungen (gleiches Feld, ähnliche Form), bevor getestet wird.
Massgeblich ist bis dahin die freie Benennung.

### Reihenfolge der Überarbeitung

1. Die 20 meistverwendeten schwachen Zeichen (rund die Hälfte aller schwachen Verwendungen).
2. Übrige Handlungen und Gegenstände.
3. Begriffe als Wortzeichen, sobald Worte im Bild umgesetzt sind (BILDPROZESS.md).
