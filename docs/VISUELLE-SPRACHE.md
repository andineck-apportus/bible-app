# Visuelle Sprache der ganzen Bibel (Analyse und Vorschlag)

Stand 2026-11-21, Auftrag von Andi Neck. Entwurf, fachlich nicht geprüft; Vorschläge sind noch nicht entschieden
(offene Punkte am Schluss). Ergänzt [BILDSTIL.md](BILDSTIL.md), [BILDPROZESS.md](BILDPROZESS.md), [STRUKTURKATALOG.md](STRUKTURKATALOG.md)
und [VERDICHTUNG.md](VERDICHTUNG.md). Die bebilderte Fassung mit allen Beispielen wird aus `pilot/visuell/seite.py` erzeugt;
Recherche mit Evidenzstufen in `pilot/visuell/recherche.md`.

## Ziel

Die Bibel zugänglich und einprägsam vermitteln und zum Studium anleiten, für Menschen unterschiedlichster Herkunft. Bilder
entstehen regelbasiert für die ganze Bibel, nicht nach persönlicher Vorliebe im Einzelfall.

## Befunde

1. **Inhaltsarten** (Schätzung je Kapitel nach vorherrschender Art, in Versen; `pilot/visuell/inhaltsarten.py`): Erzählung 41,0 %,
   Prophetenwort 12,5 %, Lied und Gebet 9,6 %, Brief und Argument 9,1 %, Weisheit und Dialog 6,9 %, Gesetz 5,5 %, Listen und
   Stammbäume 4,7 %, Rede und Lehre 4,4 %, Bau, Masse, Gebiete 3,8 %, Vision 2,5 %.
2. **Formen in den Kernanalysen** (673 Analysen, zwölf Bücher, äussere Form je Abschnitt): Szene 47 %, Dialog 13 %, Pfeilkette 9 %,
   Spalten 8 %, Raster 6 %, Gliederungsbild 5 %, zwei Ebenen 5 %, Rest unter 2 %. Für die ganze Bibel eher ein Drittel Szenen.
3. **Tests seit Oktober:** Gezeichnete Bilder ohne Bildmodell sind optisch nicht gut genug. Aquarellszenen tragen Erzählungen.
   Szenen zu Anweisungen und Listen (Titus) sind schwach. Stärkere Reduktion mindert die Verständlichkeit. Hybridbilder (gezeichnete
   Anordnung mit gemalten Vignetten oder Aquarelltextur: Seligpreisungen, Stiftshütte, Karte) wirken genau und schön.
4. **Forschung** (Übertragung aus der allgemeinen Lernforschung; Studien zur Bibelkenntnis fehlen): Bild und Wort zusammen
   behalten sich besser, sofern die Bilder unterscheidbar sind; schmückende Details schaden; Erzähltes wird viel besser erinnert als
   Sachtext; Beschriftung am Bildteil; wenige Einheiten je Ansicht; Abrufen mit Abständen festigt; Orte helfen bei Reihenfolgen.

## Vorschlag

**Form je Inhalt** (je Feld gewählt, gemischt erlaubt):

| Inhalt | Hauptform | Ergänzung |
|---|---|---|
| Erzählung | gemalte Szenen, ein Feld je tragendem Moment | Karte, Zeitleiste, Stammbaum |
| Rede, Lehre, Gleichnis | Gleichnis als Szene; Reihen als Raster mit Vignetten | Redner klein am Rand |
| Gesetz, Listen, Bau | Raster, Stammbaum, Modell, Grundriss | Weiche, Karte |
| Lied, Gebet, Weisheit | Strophen- und Parallelismusbild, Gegenüberstellung | Vignette nur für Bildworte des Textes |
| Prophetie, Vision | gegenläufige Bewegung, Völkerkarte, Reihenbild | Zeichenhandlung als Szene, beschriftete Skizze |
| Brief, Argument | Spalten, Pfeilkette, Kurve | Szene nur, wo der Brief erzählt |

**Hybrid:** Daten zeichnen Anordnung, Zahlen, Masse und Worte; das Bildmodell malt nur Figuren, Dinge und Landschaft (Szene oder
Vignette). Nie Text oder Masse im gemalten Bild.

**Ebenen:** Bibel (Bibliothek der 66 Bücher, grosse Geschichte in acht Stationen) · Testament und Gruppe (Zeitleiste, Karte) · Buch
(4–6 Stationen, Buchband) · Kapitel (Felder der Abschnitte) · Abschnitt (Feld je Moment, Form je Feld) · Vers (Merkkarte mit Abruf).
Höhere Ebenen zeigen die Bilder der Ebene darunter.

**Gedächtnisanker:** Ort (fester Platz, Karte), Zeit (eine Zeitleiste), Figur (Bildlexikon), Gestalt (wiederkehrende Formen),
Bildwort (Merkvers). Dazu Abruf im Lernmodus (Reihenfolge, Zuordnung, Lücken) nach 1 Tag, 1 Woche, 1 Monat, und Audio.

**Zugänglichkeit:** Audio zu jeder Szene; Gott nie als Figur; wählbarer Modus ohne Personenbilder; Menschen des antiken Vorderen
Orients; Zeitachse in Rechts-nach-links-Sprachen gespiegelt; Farbe nie allein; Strukturbilder auch als Textstruktur; keine
Comic-Kürzel als Bedeutungsträger.

**Prozess (neue Fassung des Bildprozesses):** Kernanalyse und Struktur → Form je Feld wählen und begründen → Anordnung aus Daten
zeichnen (feste Prüfungen: Glieder, Zahl, Reihenfolge, Wortlaut, Lesbarkeit) → Szenen und Vignetten malen (zwei prüfende Instanzen)
→ zusammensetzen und schlussprüfen → Ebenen von unten nach oben.

**Umfang:** rund 4000 Abschnitte, etwa 9500 Felder, davon etwa ein Drittel Szenen; bisher rund 0,40 Dollar je gemalter Szene
einschliesslich Wiederholungen und Prüfung; ganze Bibel grob 1500–2500 Dollar. Reihenfolge: 1 Gerüst (Bibliothek, Geschichte,
Zeitleiste, Karte, Buchebene aller 66 Bücher, rund 350 Felder) → 2 Erzählungen → 3 Strukturbilder → 4 Einprägen und Test mit
Leserinnen und Lesern.

## Beispiele (pilot/visuell)

Grosse Geschichte (8 Vignetten), Bibliothek, Zeitleiste, Jona Buchebene (Szenen, regulärer Prozess) und Aufbau, Titus als Buchband
mit Form je Feld, Tit 1,7–8 und 3,3–7, Phil 2,6–11, Obadja mit Karte, Mt 1, Psalm 1, Offenbarung 6–16, Lk 15, Seligpreisungen,
Stiftshütte, Karte Joh 2, Bildlexikon, Merkkarte Lk 15,24. Die Vignetten des Pilotlaufs sind ohne automatische Prüfung gemalt; zwei
zeigten eine nicht verlangte Figur aus der Stilvorlage und wurden zugeschnitten.

## Offen (Entscheid Andi Neck)

1. Zuordnung «Form je Inhalt» als Regel für den nächsten Bildprozess.
2. Beginn mit Phase 1 (Gerüst über alle 66 Bücher).
3. Bibliothek als Einstieg in der App.
4. Modus ohne Personenbilder.
5. Audio: Aufnahmen, synthetische Stimme oder später.
