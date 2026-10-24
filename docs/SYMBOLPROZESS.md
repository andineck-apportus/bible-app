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
4. **Unverwechselbare Form.** Klare Umrisse, in der Grösse erkennbar, in der das Zeichen erscheint (in Zellen 32 px, siehe
   «Prüfung in Einsatzgrösse»); Farbe nie als einziges Unterscheidungsmerkmal.
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
   - in der Einsatzgrösse (in einer Zelle 32 px hoch, allein und in der Zelle mit Text) und bei 160 px;
     die Zielwerte gelten für die Einsatzgrösse (siehe unten).
   Eine dritte Instanz bewertet die freien Antworten gegen die Bedeutung (0 falsch, 1 verwandt, 2 getroffen).
5. **Auswahl:** bester Entwurf, der den Zielwert seiner Klasse erreicht. Erreicht keiner ihn, wird das Zeichen bei
   Gegenständen und Handlungen neu entworfen, bei Begriffen zum Wortzeichen.
6. **Kurzer Legendentext:** ein Erkennungstext von höchstens etwa 60 Zeichen für «Figuren und Zeichen», bei allen Einträgen
   gleich knapp; die ausführliche Bedeutung bleibt im Lexikon und im Symbolindex.
7. **Protokoll am Lexikon-Eintrag:** Datum, Modell, Ergebnisse, Verwechslungen; der Symbolindex zeigt die Erklärung.
8. **Im Gesamtbild prüfen:** Das neue Zeichen wird in zwei typischen Bildern verwendet und im Blindtest ohne Legende
   geprüft (BILDPROZESS.md, Schritt 5).
9. **Bei Änderungen:** Ändert sich ein Zeichen, werden alle Bilder neu gezeichnet und geprüft, die es verwenden.

## Prüfung in Einsatzgrösse (Regel seit 2026-10-24)

Anlass (Andi Neck, 2026-10-24): Zeichen mit Händen hatten den Blindtest bei 160 px bestanden, sind in den Zellen der
Strukturbilder aber nur etwa 28–36 px hoch und dort nicht lesbar. Deshalb:

1. **Geprüft wird in der Grösse, in der das Zeichen erscheint:** in einer Zelle eines Strukturbilds 32 px hoch (Zeichenhöhe
   20 Einheiten), zusätzlich bei 160 px. **Die Zielwerte der Klassen gelten für 32 px.** Zeichen, die nur bei 160 px erkannt
   werden, gelten als nicht erkannt.
2. **Geprüft wird auch im Zusammenhang:** das Zeichen in seiner Zelle mit Text. Die Instanz nennt, was gezeichnet ist (nicht
   was im Text steht); so zeigt sich, ob das Bild bei 32 px überhaupt gesehen wird.
3. **Werkzeug:** `python3 scripts/authoring/zeichen_test.py AUSGABE …` zeichnet Testblätter ohne Namen (32 CSS-Pixel bei
   Pixeldichte 2, wie auf einem gewöhnlichen Handybildschirm) und legt den Schlüssel getrennt ab
   (`AUSGABE/blind/…png` für die blinde Instanz, `AUSGABE/schluessel.json` getrennt). Mit `--auftraege RUT,TIT` alle Zeichen
   aus den Zellen dieser Bildaufträge, mit `--zelle` in der Zelle, mit `--px 160` gross, mit `--befragen 4` vier getrennte
   Instanzen (`claude -p`, nur Lesezugriff auf das Blatt), mit `--bewerten` eine weitere Instanz (Bedeutung 0/1/2 und
   «Bild erkannt» 0/1).
4. **Zwei Masse:** «erkannt» (mindestens zwei von vier Antworten treffen die Bedeutung) und «Bild erkannt» (die Mehrheit sieht,
   was gezeichnet ist). Ist das Bild erkannt, die Bedeutung aber nicht, ist das Zeichen gut gezeichnet, aber ein Begriff:
   dann Wortzeichen, nicht neu zeichnen.

## Detailstufen (Regel seit 2026-10-24)

Andi Neck: «Fragen, ob mehr Detaillierungsgrad die Erkenntlichkeit verbessert, unnötig ist oder gar verschlechtert.» Für jedes
neue oder neu gezeichnete Zeichen:

1. **Drei Stufen zeichnen:** 1 einfach (Silhouette), 2 mittel (Silhouette und ein bis zwei Erkennungsmerkmale), 3 detailliert
   (mehrere Merkmale, z. B. Prägung und Perlrand, Fingerlinien, Glanzlicht). Technisch: Merkmale der Stufen 2 und 3 werden in
   der Zeichnung markiert, sodass alle Stufen aus einer Zeichnung entstehen.
2. **Blindtest bei 32 px allein, 32 px in der Zelle und 160 px**, die Stufen auf getrennte Sätze verteilt
   (`zeichen_test.py --entwuerfe E.json --verteilen --frage detail`): jede Instanz sieht ein Zeichen nur in einer Stufe.
   Zusatzfragen je Zeichen: «Würde mehr Detail helfen, ist es egal, oder stört es?» und «Womit könntest du es verwechseln?».
3. **Gewählt wird die Stufe mit den meisten Treffern bei 32 px allein;** bei Gleichstand die mit mehr «Bild erkannt», sonst die
   einfachere.
4. **Tragende Merkmale ins Lexikon:** Die Merkmale, die die Erkennung tragen, stehen als `traits` am Lexikon-Eintrag und als
   Regel «Tragende Merkmale … beim Neuzeichnen nicht weglassen», dazu die gewählte Stufe und das Messergebnis.

### Detailregeln (aus Runde 6)

- **Mittlere Stufe zuerst.** Bei 32 px trafen Stufe 1 32 %, Stufe 2 47 %, Stufe 3 46 % der Antworten. Das erste
  Erkennungsmerkmal bringt den Gewinn, weitere nichts mehr; bei 160 px hilft Stufe 3 (47 statt 34 von 92 Treffern).
  Mehr Detail lohnt sich nur für grosse Darstellungen.
- **Hände:** Ärmel am Handgelenk und abgesetzter Daumen tragen (Stufe 2: 26 von 40 Treffern, Stufe 1: 17); Fingernägel und
  Handlinien (Stufe 3: 21) helfen nicht. Die Handlung trägt ein eindeutiger Gegenstand oder Zusammenhang (Bettelschale mit
  fallender Münze, Krug über der Hand, Schriftrolle unter der Schwurhand), nicht die Hand allein. Wo eine Geste nicht
  eindeutig ist, eine bekannte Gebärde oder ein Piktogramm wählen (Daumen nach unten, Warndreieck, winkende Hand mit
  Bewegungsbögen).
- **Münzen:** Die Prägung (Kopf im Profil) trägt: Denar ohne Prägung 1 von 4 («Stein», «leer»), mit Prägung 4 von 4; alle
  Münzzeichen zusammen 19 → 27 von 36. Perlrand und Glanzlicht verschwinden bei 32 px (Stufe 3 ebenfalls 27). Bei Haufen und
  Stapeln genügt die Form (Münzen 4/4 in allen Stufen).
- **Figuren:** Augen und Mund (Stufe 2) helfen bei Handlungen zwischen Personen (7 → 16 von 24); Wangenrot (Stufe 3) nicht.
  Ausnahme Trost: mit lächelnden Gesichtern «Freundschaft», ohne Gesichtszüge «trösten».
- **Strichstärke:** Linien unter etwa 1 Einheit (bei einer Zeichnung von rund 30 Einheiten Höhe, also unter etwa 1 CSS-Pixel
  bei 32 px) und Flächen unter etwa 2 Einheiten verschwinden: Nägel (0,6), Handfalten (0,8), Perlrand (0,7) wirkten nicht.
  Was trug, hatte Kontur ab 1,2 Einheiten oder Flächen ab 3 Einheiten (Ärmel, Prägung, Lippen, Zügel).
- **Was stört:** Zusatzteile, die eine andere bekannte Geschichte erzählen. Schleier beim Bettler → «Witwe opfert ihr
  Scherflein»; zweites Herz beim Kuss → «Liebespaar»; Lichtstrahlen über einer Person → «Engel», «Heiliger»; Krone auf dem
  Kopf → «König». Jedes Merkmal muss die gemeinte Bedeutung stützen.
- **Was fehlt, wenn die Silhouette scheitert:** das unterscheidende Teil. Henne ohne Kamm und Schnabel → «Geldsack»; enges Tor
  ohne Figur im Spalt → «geschlossenes Tor»; Daumen nach unten ohne Ärmel → nur «Daumen runter», mit Ärmel «ablehnen».
- **Selbsteinschätzung nicht verwenden:** Die Instanzen wünschten in allen Stufen etwa gleich oft «mehr Detail» und fanden es
  fast nie störend; entschieden wird nach der Messung.

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
| Rollen | 61 | 70 % | 69 % | 33 |
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

### Runde 4, 2026-10-23

Überarbeitet nach Runde 3:
- Gemeinsames Jüngermerkmal: Jüngergewand, Gürtel und Wanderstab bis Schulterhöhe.
- Klarere Apostel-Zeichen.
- Verwechselbare Paare getrennt: Maria Magdala und Maria von Betanien, Blinde, Soldat und Hauptmann.
- Mengen ohne Kind vorn, mit Umrissen dahinter.
- Die Zwölf mit der Zahl 12, Jünger mit Fussspuren.
- Neu gezeichnet: Gefässe, Lose, Splitter, Ninive, Moab, enges Tor.

Gemessen mit neuen Instanzen und derselben strengen Regel wie Runde 3, also direkt vergleichbar.
Daten: `reports/figuren-blindtest-2026-10-23-runde4.json`.

| Art | Anzahl | getroffen Runde 3 | getroffen Runde 4 | behalten Runde 3 → 4 |
|---|---|---|---|---|
| Gott, Jesus, Geist | 4 | 100 % | 100 % | 4 → 4 |
| Personen | 79 | 33 % | 47 % | 18 → 27 |
| Rollen | 61 | 69 % | 69 % | 33 → 35 |
| Gruppen | 46 | 54 % | 67 % | 22 → 24 |
| Gegenstände | 139 | 91 % | 94 % | 122 → 126 |
| Orte | 48 | 88 % | 88 % | 41 → 39 |
| Alle | 377 | 70 % | 76 % | 240 → 255 |

54 Einträge wurden besser erkannt, 23 schlechter (Streuung der Testpersonen).

Offen nach Runde 4:
- Pilatus (95 Verwendungen) wird nicht als Römer erkannt.
- Glaubende und Menge sind nicht unterscheidbar.
- Apostel werden trotz Jüngermerkmal über ihr Attribut als Handwerker oder Räuber gelesen.
- Gegenstände in der Hand werden als Erkennungszeichen einer anderen Figur gelesen: Lazarus mit Grab als Josef von Arimatäa, Frau mit Saum als Lydia.
- Frauen mit Krug oder Brot werden als Witwe von Zarpat oder Samariterin gelesen.
- Prätorium (Feldzeichen als Kreuz gelesen), Salz, Last, enges Tor.

Im fertigen Bild helfen Namensschild, Stichwortband und Szene. Der Blindtest der ganzen Bilder ohne Legende
(BILDPROZESS.md) misst, ob das reicht.

### Runde 5 (Strukturbilder, 2026-10-24)

Für die Strukturbilder der Bergpredigt (Raster, Spalten mit Textzellen) braucht es mehr Bildzeichen, damit man Inhalte
schneller erfasst. Neu: 16 Zeichen (Daten `scripts/authoring/bildlexikon_daten/STRUKTUR.json`, Zeichnungen
`scripts/authoring/bildsymbole_daten/STRUKTUR.json`). Neu gezeichnet: das Untergewand (`FIG-OBJ-GEWAND`), das wie ein
heutiges T-Shirt aussah; jetzt eine lange Tunika mit Gürtel.

Gemessen wie Runde 3/4: allein und ohne Legende, je vier blinde Instanzen bei 160 px und zwei bei 48 px, eine weitere
Instanz bewertet. Fünf Zeichen wurden nach der ersten Messung nachgebessert und mit neuen Instanzen erneut gemessen.
Daten: `reports/zeichen-blindtest-2026-10-24-runde5.json`.

| Zeichen | Klasse | erste Messung (160 px) | nach Nachbesserung | 48 px | Urteil |
|---|---|---|---|---|---|
| Auge, Hand, Sonne, Regen, Meilenstein, Mantel (Obergewand), Untergewand, guter Baum, Axt an der Wurzel | Gegenstand | 4 von 4 | – | 2 von 2 | behalten |
| Ohrfeige | Handlung | 4 von 4 | – | 2 von 2 | behalten |
| Mammon | Begriff | 4 von 4 («Reichtum, Geldsack») | – | 2 von 2 | behalten |
| Almosen geben | Handlung | 3 von 4 | – | 0 von 2 («bezahlen») | behalten |
| Weites Tor | Ort | 4 von 4 («Stadttor») | 4 von 4 | 0 von 2 («Grab») | behalten, Weite nur im Paar mit dem engen Tor |
| Kopf mit Haar | Gegenstand | 0 von 4 («Heiliger») | 3 von 4 (vergrössertes Haar) | 0 von 2 | behalten |
| Trost | Handlung | 0 von 4 («Trauer») | 4 von 4 («Tränen abwischen») | 2 von 2 | behalten |
| Fauler Baum | Gegenstand | 0 von 4 («verdorrter Baum») | 4 von 4 (dritte Fassung: Krone, faule Früchte, Würmer, Fliegen) | 0 von 2 | behalten |
| Jota | Begriff | 0 von 4 («Schriftrolle») | 0 von 4 («Buchstabe», Jod nicht erkannt) | 0 von 2 | Wortzeichen mit «Jota» |

Lehren: Ein Funkeln am Kopf liest sich als Heiligkeit. Kahle Äste lesen sich als «verdorrt», dunkle Früchte als Feigen;
«faul» braucht Würmer und Fliegen. Trost wird erst erkannt, wenn die Träne schon weggewischt ist und das Gesicht lächelt.
Der kleinste Buchstabe bleibt ohne Wort ein Begriff. Bei 48 px tragen feine Merkmale (Fliegen, Haar in der Lupe) nicht;
in Strukturbildern stehen die Zeichen deshalb neben ihrem Stichwort. Der Test der ganzen Strukturbilder steht noch aus.

### Runde 6 (Einsatzgrösse 32 px, 2026-10-24)

Nach der Rückmeldung von Andi Neck zu den Händen und Münzen (siehe «Prüfung in Einsatzgrösse» und «Detailstufen»). Gemessen
mit `zeichen_test.py`: 32 px allein (je Stufe vier Instanzen), 32 px in der Zelle und 160 px (je zwei), Bewertung durch eine
weitere Instanz. Daten: `reports/zeichen-blindtest-2026-10-24-runde6.json`.

**Ausgangsmessung:** alle 127 Zeichen, Gegenstände und Orte aus den Zellen der Pilot-Strukturbilder (Rut, Titus,
Bergpredigt, Markus-Pilot), allein bei 32 px. Bild erkannt: 118; Bedeutung erkannt: 65. Gegenstände und Orte tragen
(Brot, Lampe, Schaf, Haus auf dem Felsen je 4/4). Nicht erkannt wurden vor allem Hände (Almosen «Bezahlung», ablehnen
«Winken», grüssen «Bund», segnen «mahnender Finger», Trost «weinen»), Salz («Manna»), Splitter («Gebot»), enges Tor
(«Mauer») und Begriffe, deren Bild zwar gesehen wird (Herz «Liebe», Tod «Grab», Hoffnung «Spross»).

**Neu gezeichnet** wurden 28 Zeichen (Hände, Münzen, Figurenpaare, Tore), **neu** sind 17. Von den 24 neu gezeichneten, die
vorher gemessen waren, wurden vorher 3 erkannt, nachher 18 (Bild erkannt: vorher 18, nachher 24). Fünf Zeichen wurden nach
der ersten Messung nochmals neu gezeichnet und gleich gemessen (6b). Treffer je Stufe bei 32 px allein (1 einfach, 2 mittel,
3 detailliert):

| Zeichen | vorher (32 px) | Stufe 1 · 2 · 3 | gewählt | gelesen als | Urteil |
|---|---|---|---|---|---|
| Almosen geben | 0/4 «Bezahlung, Bestechung» | 4 · 4 · 4 von 4 (6b) | 1 | «Almosen geben» | erkannt |
| trösten / getröstet werden | 0/4 «weinen» | 3 · 0 · 1 von 4 | 1 | «trösten, Freundschaft» | erkannt |
| verwerfen / ablehnen | 0/4 «Winken» | 0 · 3 · 0 von 4 | 2 | «ablehnen, schlecht» | erkannt |
| warnen / ermahnen | 0/4 «Erinnern, Gebot» | 4 · 4 · 4 von 4 | 1 | «Warnung» | erkannt |
| segnen | 0/4 «Mahnender Finger, Zeugnis ablegen» | 3 · 4 · 4 von 4 | 2 | «Segnen» | erkannt |
| grüssen | 0/4 «Bund» | 2 · 0 · 0 von 4 | 1 | «Winken» | knapp erkannt |
| Hand (rechte Hand) | 2/4 «Schwur, Schwören» | 2 · 3 · 3 von 4 | 2 | «Halt, Hand» | erkannt |
| schwören / Schwur | 0/4 «Lobpreis, Hand erheben» | 0 · 4 · 4 von 4 | 2 | «Schwören, Schwur» | erkannt |
| Frieden / zusammengehören | 0/4 «Bund schliessen, Bund» | 0 · 4 · 4 von 4 | 2 | «Versöhnung» | erkannt |
| Treue / zusammenhalten | 0/4 «Versöhnung, Liebe schenken» | 0 · 0 · 0 von 4 | 2 | «Versöhnung, Freundschaft» | Wortzeichen |
| Hände waschen | 0/4 «Waschschüssel, Wasserschale» | 1 · 4 · 1 von 4 | 2 | «Waschen der Hände, Hände waschen» | erkannt |
| Mitleid / Erbarmen | 0/4 «Liebe, Liebe schenken» | 0 · 4 · 4 von 4 | 2 | «Barmherzigkeit» | erkannt |
| Kuss | 0/4 «Mund» | 1 · 4 · 0 von 4 | 2 | «Kuss» | erkannt |
| Kind / Kinder | 0/4 «Frau» | 2 · 1 · 2 von 4 | 3 | «Geist, Kind folgt» | knapp erkannt |
| Zuflucht unter Flügeln | 0/4 «Engel, Cherub» | 0 · 0 · 0 von 4 | 3 | «Henne mit Küken» | Wortzeichen |
| leuchten (wie Lichter) | 0/4 «Heiliger Geist, Feuer» | 0 · 0 · 0 von 4 | 1 | «Öllampe» | Wortzeichen |
| rein / rein werden | 0/4 «Stern, Tau» | 0 · 0 · 0 von 4 | 1 | «Gewand» | Wortzeichen |
| verleugnen | 0/4 «Bund gebrochen, Vergänglich» | 0 · 3 · 4 von 4 | 3 | «Hahn verleugnen, verleugnen» | erkannt |
| Enges Tor | 0/4 «Mauer, Mauer einstürzen» | 0 · 4 · 3 von 4 (6b) | 2 | «enge Pforte» | erkannt |
| Weites Tor | 0/4 «Stadttor, leeres Grab» | 0 · 0 · 0 von 4 (6b) | 1 | «Stadttor» | Wortzeichen |
| Münzen | nicht gemessen | 4 · 4 · 4 von 4 | 1 | «Geld, Münzen» | erkannt |
| Denar (Münze) | nicht gemessen | 1 · 4 · 4 von 4 | 2 | «Silbermünze (Denar), Silbermünze» | erkannt |
| Mammon (Geld als Herr) | 0/4 «Schatz, Reichtum» | 0 · 0 · 0 von 4 | 2 | «Reichtum» | Wortzeichen |
| Gewinn | 1/4 «Zinsen, Gewinn» | 2 · 3 · 3 von 4 | 2 | «Reichtum, Reichtum mehren» | erkannt |
| geben | 4/4 «Münze geben» | 4 · 4 · 4 von 4 | 1 | «Münze geben» | erkannt |
| Schatz / Lohn | 4/4 «Schatz» | 4 · 4 · 4 von 4 | 1 | «Schatztruhe, Schatz» | erkannt |
| Talent (Silbergeld im Sack) | nicht gemessen | 0 · 0 · 0 von 4 | 1 | «Silber, Geldbeutel» | Wortzeichen |
| lösen (Löser, Löserecht) | nicht gemessen | 0 · 0 · 1 von 4 | 3 | «Schuld erlassen, Verlorener Sohn» | Wortzeichen |
| gerecht | neu | 4 · 4 · 4 von 4 | 1 | «gerecht, Gerechtigkeit» | erkannt |
| besonnen / beherrscht | neu | 0 · 0 · 0 von 4 | 2 | «Pferd» | Wortzeichen |
| fromm | neu | 0 · 0 · 0 von 4 | 2 | «Engel, Heiliger» | Wortzeichen |
| freundlich / gütig | neu | 0 · 0 · 0 von 4 | 1 | «froh, Freude» | Wortzeichen |
| Sanftmut / sanftmütig | neu | 0 · 0 · 0 von 4 | 1 | «Schaf» | Wortzeichen |
| dem Guten zugetan | neu | 0 · 0 · 3 von 4 | 3 | «Liebe richtig, Liebe gut» | erkannt |
| eigenmächtig | neu | 0 · 0 · 0 von 4 | 1 | «König krönen, Königin» | Wortzeichen |
| verleumden / Verleumdung | neu | 1 · 1 · 1 von 4 (6b) | 1 | «Lüge» | Wortzeichen |
| sich unterordnen | neu | 0 · 1 · 0 von 4 | 2 | «Huldigung, Bitten vor König» | Wortzeichen |
| suchen und finden | neu | 4 · 4 · 4 von 4 | 1 | «suchen» | erkannt |
| Haus auf Sand gebaut | neu | 4 · 4 · 4 von 4 | 1 | «Haus auf Sand» | erkannt |
| bitter | neu | 3 · 4 · 4 von 4 | 2 | «Bitterkeit, bittere Galle» | erkannt |
| klug / weise | neu | 0 · 0 · 2 von 4 | 3 | «Erleuchtung» | knapp erkannt |
| töricht | neu | 0 · 0 · 0 von 4 (6b) | 1 | «Zweifel» | Wortzeichen |
| Lohn schon erhalten | neu | 0 · 4 · 4 von 4 | 2 | «Bezahlt» | erkannt |
| Ruhe / Zuhause | neu | 4 · 4 · 4 von 4 | 1 | «Zuhause» | erkannt |
| streiten / Streit | neu | 4 · 4 · 4 von 4 | 1 | «Streit» | erkannt |

Wortzeichen (das Bild wird gesehen, die Bedeutung nur mit dem Wort aus der Übersetzung): Treue, Zuflucht, leuchten, rein,
weites Tor (nur im Paar mit dem engen Tor), Mammon, Talent, Löser, besonnen, fromm, freundlich, Sanftmut, eigenmächtig,
verleumden («Lästern», «Lüge»), sich unterordnen, töricht («Zweifel»), dazu wie bisher Kopf mit Haar (Neuentwurf schlechter,
die alte Zeichnung bleibt) und Jota. Knapp erkannt (2 von 4): grüssen, Kind, klug. «Ruhe / Zuhause» (Rut 3,1) ist erkannt,
steht im Pilotbild aber im Titel eines Feldes, der kein Zeichen trägt.

Entscheide, die frühere Regeln ändern: Die Zuflucht ist jetzt eine Henne mit Küken (vorher nur Flügel, als Cherub oder Engel
gelesen; Bild nach [[MAT.23.37]], nicht als Darstellung Gottes, nur mit Wort). Enges und weites Tor haben Türme und Zinnen
(ohne sie als Mauer oder Tür gelesen). Münzen ohne Prägung, wo die Form genügt (Haufen, Stapel, Truhe); die einzelne Münze
(Denar, Mammon, Gewinn) mit Prägung.

Offen: Salz, Splitter, Kammer, Becher leer, Freude, Licht (32 px nicht erkannt, nicht Teil dieser Runde); Test der ganzen
Strukturbilder mit den neuen Zeichen.

### Reihenfolge der Überarbeitung

1. Die 20 meistverwendeten schwachen Zeichen (rund die Hälfte aller schwachen Verwendungen).
2. Übrige Handlungen und Gegenstände.
3. Begriffe als Wortzeichen, sobald Worte im Bild umgesetzt sind (BILDPROZESS.md).
