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

## Anzeigegruppen (Entscheid 2026-10-23)

Im Bildlexikon und in der Legende stehen die Einträge in sechs Gruppen (Feld `display_group`): Gott, Jesus, Heiliger Geist ·
Menschen (Personen, Rollen, Gruppen) · Dinge, Natur und Zeit (Gegenstände und konkrete Zeichen wie Herz, Blut, Blitz,
Abend) · Orte · Handlungen und Gefühle · Begriffe (Glaube, Hoffnung, Gnade …; werden Wortzeichen). Die Zuordnung der
Zeichen folgt der Testklasse der Ausgangsmessung (`scripts/authoring/bildlexikon_daten/_gruppen.json`). Das Feld `kind`
bleibt unverändert, weil es die Platzierung in den Bildern steuert. Körperteile sind keine eigene Gruppe: als Zeichen
(z. B. «Herz (das Innere)», «verdorrte Hand») oder als Teil der Figur.

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

### Figuren und Gegenstände im Stil Anime, 2026-10-23

377 Einträge (Gott, Personen, Rollen, Gruppen, Gegenstände, Orte), ohne Legende frei beschrieben von je vier KI-Instanzen, bewertet
von einer fünften gegen Name, Identität und Pflichtmerkmale. Runde 1 vor, Runde 2 nach der ersten Überarbeitung
(Erkennungszeichen gross in der Hand, Frauen- und Altersmerkmale, Gebetsmantel, gestaffelte gemischte Gruppen mit gemeinsamem
Merkmal, 50 Gegenstände und Orte neu gezeichnet, Lexikon angeglichen). Daten: `reports/figuren-blindtest-2026-10-23.json`,
`reports/figuren-blindtest-2026-10-23-runde2.json`.

| Art | Anzahl | getroffen Runde 1 | getroffen Runde 2 | behalten Runde 1 → 2 |
|---|---|---|---|---|
| Gott, Jesus, Geist | 4 | 100 % | 100 % | 4 → 4 |
| Personen | 79 | 14 % | 68 % | 10 → 48 |
| Rollen | 61 | 28 % | 70 % | 12 → 34 |
| Gruppen | 46 | 17 % | 41 % | 6 → 18 |
| Gegenstände | 139 | 73 % | 88 % | 101 → 115 |
| Orte | 48 | 75 % | 90 % | 36 → 43 |
| Alle | 377 | 47 % | 76 % | 169 → 262 |

Offen nach Runde 2: Gruppen (zu viele kleine Köpfe; besser 3–4 grosse Figuren, feste Erkennungsfarbe, grosses Attribut),
mehrdeutige Attribute (Worfelschaufel als Hammer, Matte als Schriftrolle, Muschel als Fächer), Nebenfiguren ohne Attribut,
Satan, Besessener, Königin von Saba (Geschlecht), flache Landschaftsstreifen, Doppelbilder.

### Runde 3, 2026-10-23

Überarbeitet nach Runde 2 und den Hinweisen von Andi Neck:
- Gruppen: drei (bei Text mit vier Personen vier) grössere Figuren, eine Gruppenfarbe, Zeichen gross auf der Brust der vorderen Figur.
- 58 Personen und Rollen mit eindeutigerem Zeichen.
- 29 Gegenstände und Orte, Landschaften mit Himmel und Hügeln.
- Abgestimmte Grundformen:
  - Locken auf dem Scheitel;
  - Kopftuch tiefer in der Stirn;
  - Glatze mit Haarkranz;
  - dünnere Kontur;
  - Wanderstab über der Schulter;
  - dezentere Altersfalten.

Gemessen wie zuvor (vier blinde Beschreiber, ein Bewerter), aber mit neuen Instanzen und einer strengeren Regel: «getroffen» heisst, mindestens zwei von vier Beschreibungen erkennen Figur, Rolle oder Ding. Daten: `reports/figuren-blindtest-2026-10-23-runde3.json`.

| Art | Anzahl | getroffen Runde 2 | getroffen Runde 3 | behalten Runde 3 |
|---|---|---|---|---|
| Gott, Jesus, Geist | 4 | 100 % | 100 % | 4 |
| Personen | 79 | 68 % | 33 % | 18 |
| Rollen | 61 | 70 % | 69 % | 42 → 33 |
| Gruppen | 46 | 41 % | 54 % | 22 |
| Gegenstände | 139 | 88 % | 91 % | 122 |
| Orte | 48 | 90 % | 88 % | 41 |
| Alle | 377 | 76 % | 70 % | 240 |

Die Zahlen sind nicht direkt vergleichbar:
- Die 244 Einträge, die in Runde 3 nicht überarbeitet wurden, galten in Runde 2 alle als getroffen, jetzt nur noch 199 (82 %). Die Messung ist also strenger geworden.
- Die 133 überarbeiteten Einträge (Gruppen, Personen, Rollen, Dinge) stiegen trotzdem von 41 auf 66 getroffen (31 % → 50 %).

Offen nach Runde 3 (Bewerter):
- Apostel: Die traditionellen Attribute (Messer, Säge, Walkerstange, Winkelmass, Kelch) tragen ohne Namen nicht; es fehlt ein gemeinsames Jüngermerkmal.
- Gemischte Gruppen (Mann, Frau, Kind) werden als Familie gelesen.
- Frauen mit Kind werden zu Maria oder Elisabet.
- Gegenstände an Personen ergeben falsche Bildwörter: Saatbeutel wird als Schleuder gelesen, Kreuzbalken als «Balken im Auge».
- Paare, die nicht unterscheidbar sind:
  - Maria Magdala und Maria von Betanien;
  - die zwei jungen Männer in Weiss;
  - Blinde und Besessene;
  - Soldat und Hauptmann.
- Orte, die als bekanntere Orte gelesen werden: Ninive als Babel, Moab als Galiläa.
- Leere und schmutzige Gefässe, Lose, Splitter.

Eine Grenze ist bewusst gesetzt: Viele Nebenfiguren sind ohne Namen nicht erratbar. Im Bild tragen Hauptfiguren deshalb ein
Namensschild beim ersten Auftreten (VERDICHTUNG.md); der Blindtest ohne Namen ist hier die strengste Prüfung.

### Reihenfolge der Überarbeitung

1. Die 20 meistverwendeten schwachen Zeichen (rund die Hälfte aller schwachen Verwendungen).
2. Übrige Handlungen und Gegenstände.
3. Begriffe als Wortzeichen, sobald Worte im Bild umgesetzt sind (BILDPROZESS.md).
