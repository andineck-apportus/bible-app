# Strukturkatalog: Baumuster, Merkmale, Darstellungen

Status: gilt seit 2026-10-24 (Entscheid Andi Neck). Inhalt KI-Entwurf, fachlich nicht geprüft. Grundlage sind die acht Strukturanalysen der ganzen Bibel
vom 2026-10-24 (Tora; Geschichtsbücher; Poesie und Weisheit; grosse Propheten; kleine Propheten; Evangelien und Apostelgeschichte;
Paulusbriefe; Hebräer, katholische Briefe und Offenbarung). Stellen sind aus den Analysen übernommen, nicht neu erhoben.
Forschungsvorschläge sind als «Vorschlag» gekennzeichnet. Ergänzt [VERDICHTUNG.md](VERDICHTUNG.md). Offene Fragen am 2026-10-24 von Andi Neck entschieden (Abschnitt 7).

Verszählung: Die Marken folgen der Navigationszählung (KJV) wie alle Marken der App ([BIBELSTELLEN.md](BIBELSTELLEN.md)).
Die Analysen zählen deutsch bzw. hebräisch; ihre Stellen sind mit den TVTMS-Daten umgerechnet (47 Marken, z. B. Joel 3,1 deutsch =
[[JOL.2.28]], Mal 3,19 deutsch = [[MAL.4.1]], Psalmen mit Überschrift einen Vers tiefer). Wo deutsche Zählung im Text steht, ist sie als
«dt.» gekennzeichnet.

## 1. Zweck und Gebrauch

Die Strukturanalyse steht am Anfang jeder Kernanalyse (Feld `structure`, [VERDICHTUNG.md](VERDICHTUNG.md), «Struktur zuerst»).
Ablauf je Einheit:

1. **Baumuster bestimmen** (`pattern`): Wie ist der Text gebaut? Aus Abschnitt 3 wählen; bei Gattungsformen den Untertyp
   (`form_type`) angeben.
2. **Verschachteln**: Muster liegen ineinander (eine Reihe im Rahmen, ein Gegensatz aus zwei Ketten, ein Kreislauf als Raster
   über mehrere Durchgänge). Das äussere Muster trägt die Einheit, innere Muster sind Kinder.
3. **Glieder vollständig erfassen** (`elements`): alle Glieder, die das Muster verlangt, je mit Stelle und Verbindung.
   Weglassen darf man Ausschmückung, nicht Glieder (Regel 1 der Strukturtreue).
4. **Merkmale setzen** (`features`, Abschnitt 2b): Sprecher, Musterbruch, offenes Ende, Textfassungen, Deutung usw. Manche
   sind je Muster Pflicht.
5. **Darstellung wählen** (`visual`, Abschnitt 2c): aus der begrenzten Liste, passend zum Muster.

Die Prüfung «Strukturtreue» stellt je Muster die Prüffrage aus Abschnitt 3.

## 2. Drei Ebenen

Die Analysen schlagen über 150 neue Namen vor. Viele davon sind keine eigenen Baumuster, sondern Merkmale (Ironie, Leitwort,
offenes Ende) oder Bildtypen (Lagerplan, Organigramm, Weg im Grundriss). Deshalb drei getrennte Ebenen:

| Ebene | Frage | Anzahl | Beispiel Seligpreisungen [[MAT.5.3-MAT.5.12]] |
|---|---|---|---|
| Baumuster `pattern` | Wie ist der Text gebaut, was darf nicht fehlen? | 33 in 9 Familien | `series` im `frame` (1. und 8. Glied gleiche Verheissung) |
| Merkmal `features` | Was gilt zusätzlich, ohne eigene Gestalt? | 15 | `speakers` (Jesus zu Jüngern und Volk), `crossref` (Lk 6) |
| Darstellung `visual` | Welcher Bildtyp zeigt die Struktur? | 20 | `grid` (acht Felder plus Anrede) |

Grundsatz der Trennung: Ein Name wird **Baumuster**, wenn er eigene Pflichtglieder und eine eigene Prüffrage hat. Er wird
**Merkmal**, wenn er zu vielen Mustern hinzutreten kann. Er wird **Darstellung**, wenn er nur beschreibt, wie etwas gezeichnet
wird. Er wird **Untertyp**, wenn Glieder und Prüffrage gleich bleiben und nur eine Variante dazukommt.

### 2a. Baumuster: Familien

| Familie | Baumuster |
|---|---|
| A Zeit und Ablauf | `sequence`, `cycle`, `curve`, `fulfilment`, `interleave` |
| B Reihen und Ordnungen | `series`, `numbered`, `matrix`, `register`, `tree`, `climax` |
| C Gegenüberstellung und Spiegelung | `contrast`, `balance`, `reversal`, `parallel`, `frame` |
| D Logik und Argument | `condition`, `cause`, `argument`, `objection` |
| E Rede und Gattungsform | `dialogue`, `form`, `poem` |
| F Bild und Deutung | `parable`, `sign_act`, `typology` |
| G Raum, Gestalt und Weg | `space`, `route`, `territory`, `outward` |
| H Vision und Ebenen | `vision`, `realms` |
| I Buch- und Sammlungsbau | `collection` |

Alle 16 bisherigen Namen bleiben. Geschärft werden zwei: `numbered` gilt nur noch, wo die Zahl selbst die Ordnung trägt (sonst
`series`); `vision` heisst Visionsbericht und legt keine Zeitachse mehr fest (Befund Offenbarung). Neu sind 17 Muster.

**Entscheid Gattungsformen:** ein Muster `form` mit Untertyp `form_type` und Pflichtgliedern je Untertyp (Verzeichnis in 3.22),
nicht je Gattung ein eigenes Muster. Gründe: (1) Alle Formen haben denselben Bau, eine feste Folge benannter Glieder, und dieselbe
Prüffrage: Sind alle Pflichtglieder da, und ist ein fehlendes Glied als Musterbruch vermerkt? (2) Der Renderer braucht dafür
einen Bildtyp (`outline` als Formularbild mit benannten Feldern, leere Felder sichtbar) statt fünfzehn. (3) Neue Formen
(z. B. weitere Psalmgattungen) werden im Verzeichnis ergänzt, ohne Schema und Renderer zu ändern. Ausnahmen mit eigener Logik
bleiben eigene Muster: `vision` (Bild und Deutung, Skizzen), `objection` (fremde Stimme), `dialogue` (Sprecherfolge),
`sign_act` (zwei Ebenen).

### 2b. Merkmale

| `id` | Merkmal | Inhalt | Pflicht bei |
|---|---|---|---|
| `speakers` | Sprecher und Stimmen | wer spricht zu wem, Stimmwechsel, verworfene Reden (Hiobs Freunde, [[JOB.42.7-JOB.42.8]]), Einwände, Parolen, Rahmenerzähler ↔ Ich ([[ECC.1.1]] ↔ [[ECC.1.12]]), Ich-/Er-/Wir-Bericht (Neh, Apg), Erzählerkommentar ([[2KI.17.7-2KI.17.23]]), eingebettete Dokumente mit Absender → Empfänger (Esra 4–7), Anlass und Adressat | `dialogue`, `objection`, `form`, `poem` mit Stimmwechsel, alle Briefe und Reden |
| `stance` | Sprecherhaltung | Ironie, Narrenrede, Spott ([[1CO.4.8-1CO.4.13]]; [[2CO.11.1-2CO.12.13]]; Listen in [[DAN.3.2-DAN.3.3]] und [[DAN.3.5]]) | wo vorhanden |
| `authority` | Autoritätsebene | Herkunft einer Weisung: Herr / ich / Meinung ([[1CO.7.10]], [[1CO.7.12]], [[1CO.7.25]], [[1CO.7.40]]); Gotteswort / Prophet / Volk; ausserkanonische Überlieferung ([[JUD.1.9]], [[JUD.1.14-JUD.1.15]]) | Weisungen mit wechselnder Herkunft |
| `genre` | Gattung | Einordnung (Klagelied, Hymnus, Königspsalm, Testament, Mandatsbrief, Spottlied …); Forschungsbegriff, nicht Textangabe | immer, wenn bestimmbar; bei `form` gleich `form_type` |
| `leitwort` | Leitwort, Formel, Motiv | wiederkehrendes Wort, Kehrvers in Prosa, Gliederungsformel, Motivleiste; Rolle: gliedernd, deutend, verklammernd, Zweck (Erkenntnisformel in Ezechiel, etwa 70-mal) | wo der Text so gegliedert ist |
| `pattern_break` | Musterbruch und Einschub | Glied bricht die Reihe (3 + 1; [[2TI.2.13]]), fehlendes Glied (Zofar im 3. Redegang; kein Dank in [[GAL.1.6]]), Einschub an seinem Platz ([[REV.7]]; [[REV.10.1-REV.11.14]]), Einzahl ↔ Mehrzahl ([[GAL.5.22]]) | wo vorhanden; nie glätten |
| `open_end` | Offenes Ende | Schluss ohne Auflösung, Schlussfrage ([[JON.4.11]]; [[NAM.3.19]]; [[MRK.16.8]]; [[ACT.28.31]]; [[LAM.5.22]]; [[PHM.1.21]]) | wo vorhanden |
| `modality` | Modalität | Ankündigung ↔ Bericht, Auftrag ↔ Tatsache, Bitte ↔ Zusage, «vielleicht», «wer weiss» ([[JOL.2.14]]; [[JON.3.9]]; [[ZEP.2.3]]), Erfahrungssatz ↔ Garantie (Spr) | Prophetie, Weisheit, Gebet |
| `wordplay` | Wortspiel, Namensdeutung | Glied hängt an Klang oder Name; als `terms` mit Urwort erfassen ([[ISA.5.7]]; [[JER.1.11-JER.1.12]]; [[AMO.8.2]]; [[MIC.1.10-MIC.1.15]]; [[DAN.5.25-DAN.5.28]]; [[PHM.1.11]]) | wo tragend |
| `text_forms` | Textfassungen und Verszählung | abweichende Fassungen (Jer MT ↔ LXX; Est hebr. ↔ griech.; Dan Zusätze; 1 Sam 17–18 LXX), Textkritik ([[MRK.16.9-MRK.16.20]]; [[JHN.7.53-JHN.8.11]]; [[1JN.5.7-1JN.5.8]]), abweichende Zählung | immer, wenn bekannt |
| `interpretation` | Deutung statt Text | Forschungsvorschlag (Chiasmus, Gliederungsthese, Zeitschichten Jes 1–39/40–55/56–66), Auslegung (Reichsdeutungen, Messiasdeutung), Rekonstruktion (Masse, Karten); mit Quelle oder Begriff | jede Angabe, die nicht im Text steht |
| `crossref` | Bezüge über Buchgrenzen | Zitat, Erfüllung, Umkehrung eines anderen Wortes ([[JOL.3.10]] ↔ [[MIC.4.3]]), Brückenstelle ([[2CH.36.22-2CH.36.23]] = [[EZR.1.1-EZR.1.3]]), Querverweis-Netz (Gnadenformel [[JOL.2.13]], [[JON.4.2]], [[MIC.7.18-MIC.7.19]], [[NAM.1.3]]) | wo der Text selbst verweist; sonst als Deutung |
| `chronology` | Zeitgerüst | Daten und Synchronismen ([[LUK.3.1-LUK.3.2]]; Hag; Ez), Buchordnung ≠ Zeitordnung ([[EZR.4.6-EZR.4.23]]; Jer; [[EZK.29.17]]), Zeitangaben ohne festen Anker ([[DAN.9.24-DAN.9.27]]), Korrespondenz-Zeitleiste (2 Kor) | Prophetenbücher, Esra, Est, Hag, Sach |
| `numbers` | Zahlen und Masse | Zahlen als Text, Symbolzahlen und Zahlengleichungen ([[REV.11.2-REV.11.3]]; [[REV.12.6]]; [[REV.12.14]]), Masse in Ellen, abweichende Zahlen in Parallelen | wo Zahlen vorkommen; nie runden, umrechnen nur als Annahme |
| `weight` | Gewichtung | Längenverhältnis und Schwerpunkt (Fluchteil [[DEU.28.15-DEU.28.68]] viermal länger; Juda und Josef in [[GEN.49]]; Israel-Strophe in Am 2; Juda, Levi, Benjamin in 1 Chr 1–9) | wo die Länge Aussage trägt |

### 2c. Darstellungen

Vorgabe für den Renderer: 20 Bildtypen. Jeder Bildtyp hat Varianten, aber keine eigenen Regeln je Bibelstelle.

| `id` | Darstellung | Beschreibung | bedient vor allem |
|---|---|---|---|
| `scenes` | Bildfolge | 1–4 Szenen in Reihenfolge | `sequence`, `parable`, `sign_act` |
| `timeline` | Zeitleiste | Achse mit Stationen; Varianten: Datumsmarken, Bögen Ankündigung → Erfüllung (auch über Buchgrenzen), Zoom Tage → Stunden, Marke «jetzt / noch nicht», Achse ohne festen Anker, geteilter Balken (Lebenswende) | `sequence`, `fulfilment`, `curve`, Merkmal `chronology` |
| `lanes` | Doppelbahn | zwei parallele Bahnen mit Querverbindungen oder im Reissverschluss; Pendel | `interleave` |
| `grid` | Raster | Felder in Zeilen und Spalten, leere Zellen sichtbar; Varianten: Liste mit Zahl, Schema-Raster, Alphabet-Raster (22 Felder), Bedingungsraster 2×2, Tabelle Fest × Gabe | `series`, `numbered`, `matrix`, `register`, `poem` |
| `columns` | Spalten | zwei oder mehr Spalten Zeile für Zeile; Varianten: Gegenüberstellung, Synopse mit Markierung «nur hier / nur dort / beide», linke Spalte durchgestrichen («nicht … sondern»), Bilanz | `contrast`, `parallel`, `balance`, `typology` |
| `mirror` | Spiegelachse | Paare symmetrisch zu einer Achse; Variante X-Diagramm (eine Grösse steigt, eine fällt) | `reversal` |
| `switch` | Weiche | Verzweigung mit allen Zweigen; Varianten: Entscheidungsbaum mit Unterfällen, Warteschleife, gestrichelter Zweig für offene Folge, Stufen mit Weiche je Stufe | `condition` |
| `arrows` | Pfeilkette | Felder mit «→»; Varianten: rückwärts, Dominokette mit Wende, Belegkästen, zwei Stockwerke (Zuspruch unten, Anspruch oben) | `cause`, `argument` |
| `tree` | Baum | Stammbaum, Kette über Generationen, Organigramm, Auswahltrichter, hervorgehobener Ast | `tree` |
| `rings` | Ringe | konzentrische Darstellung; Varianten: Mitte betont (Chiasmus), Ausweitung nach aussen, Zonenplan, Strahlenbild (Theophanie) | `frame`, `outward`, `space` (Zonen) |
| `circle` | Kreis | Kreislauf, Spirale, Jahresrad, Kreispfeil (Spiegelstrafe) | `cycle`, `cause` (Spiegelstrafe) |
| `stairs` | Treppe und Kurve | Treppe auf oder ab, V-Kurve, Stimmungskurve, Höhenprofil | `climax`, `curve`, `reversal` |
| `map` | Karte | Weg mit Stationen, Gebiete und Streifen, Reihe auf Karte (Kompass, Ring zur Mitte), Ringe um ein Zentrum, Panorama vom Berg; unsichere Lagen gestrichelt | `route`, `territory`, `outward`, `series` (Völkersprüche) |
| `model` | Modell und Grundriss | Grundriss, Schnitt, 3D-Modell mit Massen; Varianten: Weg im Grundriss (nummerierte Wegpunkte), Lagerplan mit Himmelsrichtungen, Bühne (Raumwechsel), Lageskizze mit Bewegungspfeilen | `space`, `route` |
| `figure` | Beschriftete Figur | emblematische Skizze einer Gestalt oder eines Gegenstands mit Legende Bild → Sache; Bildtafel (Körperteil → Vergleichsbild); nie naturalistisch | `space` (Gestalt), `vision`, `parable`, `poem` (Beschreibungslied) |
| `levels` | Zwei Ebenen | oben/unten: Himmel ↔ Erde, Bild ↔ Sache, Handlung ↔ Deutung, Typos ↔ Antitypos, wörtlich ↔ gemeint | `realms`, `parable`, `sign_act`, `typology`, `fulfilment` (Zitat ↔ Ereignis) |
| `dialogue` | Dialogspalten | Sprecher in Spalten oder Sprechblasen; Varianten: Rundenraster (Runde × Sprecher), Einwand als fremde Stimme markiert | `dialogue`, `objection` |
| `balance` | Waage | zwei Schalen mit allen Gliedern, Ausschlag; Variante zwei Stufen «wie viel mehr» | `balance` |
| `outline` | Gliederungsbild | Band oder Blöcke mit Marken; Varianten: Formularbild (benannte Felder, leere sichtbar), Briefbild, Buchband mit Formelmarken, Strophenbild mit Kehrversband, Parallelismus-Leiter, Regal (Sammlung), Bild im Bild (Schachtelung) | `form`, `poem`, `collection`, `frame`, Merkmal `leitwort` |
| `network` | Netz | Personen- oder Stellennetz mit Pfeilen; Beziehungsdreieck; Themenkarte (Cluster); Querverweis-Netz | `register` (Grusslisten), `collection` (Themen), Merkmal `crossref` |

## 3. Katalog der Baumuster

Je Eintrag: Glieder, Prüffrage für «Strukturtreue», Form der Zusammenfassung, Darstellung, Beispiele, Fallstricke,
aufgegangene Vorschläge der Analysen.

### A Zeit und Ablauf

#### 3.1 `sequence` Ablauf
- **Glieder:** Stationen in Textreihenfolge (Handelnde, wer zu wem, was), Wendepunkt, Ausgang; Zeitangaben, wo sie tragen.
- **Prüffrage:** Sind Anfang, Wendepunkt und Ausgang da? Folgt die Reihenfolge dem Text, nicht einer Harmonisierung?
  Bleibt Ankündigung Ankündigung?
- **Zusammenfassung:** Fliesstext in der Reihenfolge des Textes.
- **Darstellung:** `scenes`; `timeline` bei Daten (Tage und Stunden als Zoom, Marke «noch nicht»).
- **Beispiele:** Rut [[RUT.1-RUT.4]]; [[MRK.5]]; Passionswoche mit Tagen und Stunden [[MRK.11.1-MRK.16.8]]; datierte Worte
  [[HAG.1.1-HAG.2.23]]; Ablauf beim Kommen des Herrn [[1TH.4.13-1TH.4.18]]; «noch nicht» [[2TH.2.1-2TH.2.12]]; drei Welten
  [[2PE.3.5-2PE.3.13]].
- **Fallstricke:** Buchordnung als Zeitordnung lesen ([[EZR.4.6-EZR.4.23]]); Parallelberichte angleichen ([[LUK.24]] ↔ [[ACT.1.3]];
  Passionstage Mk ↔ Joh); Endzeitabläufe als Fahrplan isolieren (Anlass Trauer, Ziel Trost in 1 Thess 4).
- **Aufgegangen in:** Erweiterung `sequence` «Zeitraster mit zwei Massstäben» (Variante von `timeline`); «Zeitstrahl mit
  «noch nicht»» (Variante von `timeline`); Datierungen siehe Merkmal `chronology`.

#### 3.2 `cycle` Kreislauf und Spirale
- **Glieder:** Stationen des Umlaufs mit ihren Formeln; je Durchgang, welche Glieder vorhanden sind; Veränderung von Durchgang
  zu Durchgang (Verfall, Vertiefung).
- **Prüffrage:** Bleiben fehlende Glieder sichtbar (bei Simson kein Schreien, keine Ruhe)? Wird Verfall als Spirale gezeigt,
  nicht als glatter Kreis?
- **Zusammenfassung:** Glieder mit «→» und Rückkehr; danach je Durchgang die Abweichung.
- **Darstellung:** `circle` (Kreis, Spirale, Jahresrad); mehrere Durchgänge zusätzlich als `grid` (siehe `matrix`).
- **Untertypen:** Kreislauf; Abwärtsspirale; Themenspirale (wenige Themen kehren vertieft wieder); Kalender (Feste im Jahreslauf).
- **Beispiele:** Richterzyklus [[JDG.2.11-JDG.2.19]] und [[JDG.3.7-JDG.16.31]]; Murren-Erzählungen [[NUM.11-NUM.21]] (mit Strafe,
  anders als Ex 15–17); Geschichtsrückblick [[EZK.20.5-EZK.20.29]]; drei Durchgänge Gericht → Heil in Micha ([[MIC.1.2]], [[MIC.3.1]],
  [[MIC.6.1]]); Kreisläufe der Welt [[ECC.1.4-ECC.1.7]]; Festkalender [[LEV.23]], [[NUM.28-NUM.29]], [[EZK.45.18-EZK.46.15]];
  Themenspirale 1. Johannes.
- **Fallstricke:** Kreis glätten, obwohl der Text zerfällt; Wiederholungen in 1 Joh als überflüssig streichen.
- **Aufgegangen in:** `spiral` (Abwärtsspirale, Geschichtsbücher; Themenspirale, 1 Joh), `calendar`, `judgment_salvation`
  (bei mehreren Durchgängen).

#### 3.3 `curve` Verlauf und Wende
- **Glieder:** Ausgangslage, Scharnier (Wort oder Ereignis, wörtlich mit Stelle), Endlage; bei Kurven Tief- und Hochpunkte.
- **Prüffrage:** Sind beide Pole und das Scharnier erhalten? Endet die Kurve, wo der Text endet (Ps 88 ohne Lob; Klgl 3 mit dem Hoch
  in der Mitte)?
- **Zusammenfassung:** «zuerst … dann (Scharnier) … schliesslich …».
- **Darstellung:** `stairs` (Kurve, Knick); `timeline` als geteilter Balken bei Lebenswenden.
- **Beispiele:** [[PSA.13]] (viermal «Wie lange?» → Bitte → Vertrauen); Wende [[PSA.73.17]]; [[JER.20.7-JER.20.18]] (Vertrauen → Fluch,
  nicht umdrehen); [[LAM.3]]; Wende im Innern Gottes [[HOS.11.8-HOS.11.9]]; Klage ↔ Erhörung mit Wende [[JOL.2.18]]; Stichtag
  [[HAG.2.15-HAG.2.19]]; Lebenswende [[2CH.26.16]], [[2CH.33.12-2CH.33.13]].
- **Fallstricke:** Klagepsalmen nur als Klage oder nur als Lob; Wende im Joelbuch übersehen.
- **Aufgegangen in:** `mood`, `mood_curve`, `turn`, `two_phase`, `judgment_salvation` (als Diptychon mit Wendepunkt).

#### 3.4 `fulfilment` Ankündigung → Erfüllung
- **Glieder:** Ankündigung (Wort, Fluch, Verheissung, Themenansage) mit Sprecher und Stelle; jede Erfüllung mit Stelle;
  Erfüllungsvermerk, falls im Text; Gefährdungen dazwischen.
- **Prüffrage:** Sind beide Enden belegt? Stellt der Text die Erfüllung selbst fest, oder ist es Auslegung (dann `interpretation`)?
  Sind alle Glieder der Verheissung da (Land, Nachkommen, Segen)?
- **Zusammenfassung:** «angekündigt in … – erfüllt in …».
- **Darstellung:** `timeline` mit Bögen, auch über Buchgrenzen; `levels` für Erfüllungszitate (Zitat oben, Ereignis unten).
- **Beispiele:** [[JOS.6.26]] → [[1KI.16.34]]; [[1KI.13.2]] → [[2KI.23.15-2KI.23.18]]; [[2SA.12.10-2SA.12.12]] → [[2SA.13]] bis
  [[1KI.2.25]]; Abrahamsverheissung [[GEN.12.1-GEN.12.3]] mit Gefährdungen; Erfüllungszitate [[MAT.1.22-MAT.1.23]], [[MAT.2.15]];
  Themenansage [[HEB.2.17]] → [[HEB.3.1-HEB.5.10]]; Fernbezüge [[REV.2.7]] → [[REV.22.2]].
- **Fallstricke:** rabbinische oder neutestamentliche Erfüllungsdeutung in den Text schreiben (z. B. «vierfach» = vier Söhne);
  Verheissung auf ein Glied verkürzen.
- **Aufgegangen in:** `fulfillment`, `fulfilment`, `arcs`, `thread`, `announce`.

#### 3.5 `interleave` Wechsel und Doppelbahn
- **Glieder:** zwei (selten mehr) Stränge, Wechselstellen, Querverbindungen (Synchronismen), Richtung je Strang.
- **Prüffrage:** Bleiben beide Stränge und der Rhythmus des Wechsels erhalten? Wird nichts zu einem Strang verschmolzen?
- **Zusammenfassung:** «im Wechsel: A … / B …».
- **Darstellung:** `lanes`.
- **Beispiele:** Samuel ↔ Eli-Söhne [[1SA.2.11-1SA.2.26]]; Juda ↔ Israel von [[1KI.15]] bis [[2KI.17]]; Erzählung ↔ Rede in Matthäus;
  Lehre ↔ Mahnung im Hebräerbrief; König des Südens ↔ des Nordens [[DAN.11.2-DAN.11.45]]; Juda ↔ Ninive [[NAM.1.9-NAM.2.2]];
  Gemeindeordnung ↔ Abgrenzung in 1 Tim.
- **Fallstricke:** nur einen Strang verdichten (Hebr nur Lehre); Angeredete vertauschen (Nah).
- **Aufgegangen in:** `synchrony`, `alternation`, `pendulum`, `interleave`.

### B Reihen und Ordnungen

#### 3.6 `series` Reihe gleich gebauter Glieder
- **Glieder:** alle Glieder mit Stelle; je Glied die Teile des Bauschemas (wer → was; Tat → Folge; Name → Bedeutung); Einleitung
  und Schluss der Reihe; Abweichungen.
- **Prüffrage:** Stimmt die Zahl der Glieder? Hat jedes Glied beide Hälften? Bleibt ein Musterbruch (3 + 1, Einschub, letztes Glied
  als Pointe) erhalten?
- **Zusammenfassung:** Liste, alle Glieder knapp im Bauschema.
- **Darstellung:** `grid`; `map` für Reihen von Orten; `figure` für Rundgänge durch Kosmos und Tierwelt.
- **Untertypen:** Katalog (Laster, Tugenden, Leiden, Gaben, Ämterspiegel); Reihe auf Karte (Völkersprüche, oft auf den Hörer
  zulaufend); Fragereihe; Vorbildreihe; Prüfsteine («daran erkennen wir»); Dreiergruppen; Teleskop (letztes Glied enthält die
  nächste Reihe, [[REV.8.1-REV.8.2]]; [[REV.11.15]] → [[REV.15.1]]).
- **Beispiele:** [[MAT.5.3-MAT.5.12]]; sechs Wehe [[ISA.5.8-ISA.5.24]]; Völkersprüche [[AMO.1.3-AMO.2.16]], [[ZEP.2.4-ZEP.2.15]],
  [[JER.46-JER.51]]; sieben Fälle des Weihgebets [[1KI.8.31-1KI.8.53]]; Fragekatalog [[JOB.38.1-JOB.40.2]]; Glaubenszeugen [[HEB.11]];
  Werke ↔ Frucht [[GAL.5.19-GAL.5.23]]; Vorbilder [[PHP.2.5-PHP.2.30]]; Prüfsteine [[1JN.2.3-1JN.2.11]]; Triaden in Judas.
- **Fallstricke:** auf «einige» kürzen (sechs Wehe, vier Thronnamen [[ISA.9.6]], 14 Paare); geografische Reihenfolge verlieren;
  Pointe am Schluss streichen (Israel in Am 2; Ziel [[HEB.11.39-HEB.11.40]]).
- **Aufgegangen in:** `map_series`, `nations_ring`, `refrain_series` (mit Merkmal `leitwort`), `questions`, `exemplum`, `tests`,
  `triad`, `telescope`; Erweiterung `series` «3 + 1» (mit Merkmal `pattern_break`).

#### 3.7 `numbered` Zahlenordnung
- **Glieder:** Zahl(en) wörtlich, Gruppierung (2 × 3 + 1, 3 × 3 + 1, 4 + 3, 2 + 2 + 1, 3 × 14, x / x + 1), alle gezählten Glieder; ob der
  Text zählt oder die Auslegung.
- **Prüffrage:** Zählt der Text selbst (sonst `interpretation`: «sieben Zeichen» Joh, «sieben Bitten»)? Sind Gruppierung und alle
  Glieder da?
- **Zusammenfassung:** Zahl nennen, Gruppen benennen, alle Glieder.
- **Darstellung:** `grid` mit Zahl; `circle` bei Zahlenrädern (7 × 7 + 1).
- **Beispiele:** Schöpfungswoche [[GEN.1.1-GEN.2.3]] (Räume ↔ Bewohner, Tag 7 ohne Abendformel); Plagen [[EXO.7.14-EXO.12.30]];
  Jericho [[JOS.6.3-JOS.6.4]]; Stammbaum 3 × 14 [[MAT.1.17]]; Zahlensprüche [[PRO.6.16-PRO.6.19]], [[PRO.30.15-PRO.30.31]], Am 1–2;
  2 × 7 Paare [[ECC.3.1-ECC.3.8]]; Jobeljahr [[LEV.25.8-LEV.25.13]]; Siebenerreihen der Offenbarung; leere Reihe der sieben Donner
  [[REV.10.3-REV.10.4]].
- **Fallstricke:** Zahl ohne Liste («sieben Gräuel»); Zählweisen still festlegen (Dekalog jüdisch, lutherisch, reformiert).
- **Aufgegangen in:** `numeric_saying`, `numerical_saying`; Teil von `triad`.

#### 3.8 `matrix` Schema-Raster
- **Glieder:** Zeilen (Einheiten), Spalten (Schritte oder Formelteile), Zellen mit Stelle, leere Zellen, abweichende Zeile.
- **Prüffrage:** Sind alle Zeilen und Spalten da? Bleiben leere Zellen leer (Smyrna und Philadelphia ohne Tadel, Laodizea ohne Lob)?
  Ist die abweichende Zeile markiert (Dan 5 ohne Umkehr)?
- **Zusammenfassung:** Schema einmal nennen, dann je Einheit die Besonderheit.
- **Darstellung:** `grid`.
- **Beispiele:** Richter × Zyklusglieder; Hoferzählungen [[DAN.2-DAN.6]]; Sendschreiben [[REV.2-REV.3]] (7 × 8); drei Übungen
  [[MAT.6.1-MAT.6.18]] (3 × 4); Wegabschnitt [[MRK.8.31-MRK.10.45]] (3 × 3); drei Verlorene [[LUK.15]]; vier Gruppen Geretteter
  [[PSA.107.4-PSA.107.32]]; Weltgericht [[MAT.25.31-MAT.25.46]] (6 Werke × 4); Königsurteile 1–2 Kön; Posaunen ↔ Schalen
  [[REV.8.2-REV.11.19]] ↔ [[REV.15-REV.16]] (gleiche Ziele, Ausmass Viertel → Drittel → alles); Rückkehrwellen Esra 1–6 / Esra 7–10 /
  Neh; fünf Warnstellen im Hebräerbrief.
- **Fallstricke:** leere Zellen mit Standardformeln füllen; Raster als Zeitfolge lesen (Offb: Rekapitulation, Teleskop, Linearität
  sind Deutungen).
- **Aufgegangen in:** `matrix` (Schema-Raster, Evangelien; Sendschreiben, Offb), `scheme_grid`, `rating`, `template_repeat`,
  `recapitulation`, `formula` im Sinn «Formular» (Geschichtsbücher; einzelner Eintrag als `form` `regnal`).

#### 3.9 `register` Verzeichnis
- **Glieder:** Gliederung in Gruppen, Summe(n), Anfangs- und Endglied, Pointe, eingestreute Erzählsplitter.
- **Prüffrage:** Bleiben Gliederung, Summe und Pointe (Urija als letzter Held [[2SA.23.39]])? Wird die Liste nicht gestrichen, wo sie
  Hauptteil ist? Bleiben abweichende Zahlen stehen (Esra 2 ↔ Neh 7)?
- **Zusammenfassung:** Gruppen und Summe, Pointe; nicht jedes Glied einzeln.
- **Darstellung:** `grid` als gruppierter Balken; `map` mit Punkten; `network` für Grusslisten.
- **Abgrenzung zu `series`:** In der Reihe trägt jedes Glied Aussage und muss bleiben; im Verzeichnis tragen Gliederung und Summe.
- **Beispiele:** besiegte Könige [[JOS.12]]; Heimkehrer [[EZR.2]]; Heldenliste [[2SA.23.8-2SA.23.39]]; Betroffene [[EZR.10.18-EZR.10.44]];
  Völkerliste [[ACT.2.9-ACT.2.11]]; Grusslisten [[ROM.16]], [[COL.4.7-COL.4.17]], [[2TI.4.9-2TI.4.21]].
- **Fallstricke:** Listen als «langweilig» weglassen; Teilzahlen und Summe angleichen ([[EZR.1.9-EZR.1.11]]).
- **Aufgegangen in:** `register`; «Personennetz» (Variante von `network`).

#### 3.10 `tree` Baum, Stammbaum, Ordnung
- **Glieder:** Wurzel, Äste, Knoten mit Namen; Richtung (absteigend, aufsteigend); Haupt- und Nebenlinie; Gewichtung; Erzählsplitter;
  bei Ämtern Zuständigkeit; bei Auswahl die Stufen.
- **Prüffrage:** Sind Haupt- und Nebenlinie da, Richtung und Gewichtung richtig, ausserhalb des Schemas Genanntes (vier Frauen in
  Mt 1) erhalten?
- **Zusammenfassung:** Kette oder Gliederung.
- **Darstellung:** `tree` (Stammbaum, Kette, Organigramm, Trichter).
- **Untertypen:** Stammbaum; Organigramm und Dienstordnung; Auswahlweg (schrittweise Einengung); Weitergabekette.
- **Beispiele:** Stammbäume [[GEN.5]], [[GEN.11.10-GEN.11.26]] (Henoch bricht die Formel); Völkertafel [[GEN.10]]; Söhne Jakobs nach
  Müttern [[GEN.29.31-GEN.30.24]]; [[RUT.4.18-RUT.4.22]]; aufsteigend [[LUK.3.23-LUK.3.38]]; Levitensippen [[NUM.3-NUM.4]]; Ämter
  [[DEU.16.18-DEU.18.22]]; Genealogien mit Splitter [[1CH.1-1CH.9]] (Jabez [[1CH.4.9-1CH.4.10]]); Dienstordnungen [[1CH.23-1CH.27]];
  Los [[JOS.7.14-JOS.7.18]]; Heeresreduktion [[JDG.7.2-JDG.7.7]]; Weitergabe [[2TI.1.5]], [[2TI.2.2]]; drei Generationen [[EZK.18]] (mit
  `condition`).
- **Fallstricke:** Nebenlinien (Kain, Ismael, Esau) als unwichtig streichen; Altersangaben in Gen 5 und 11 harmonisieren (MT, LXX,
  Samaritanus weichen ab).
- **Aufgegangen in:** `organigram`, `funnel`, `tradition`, `generations` (verschachtelt mit `condition`); Erweiterungen `tree`
  «Haupt- und Nebenlinie» und «Genealogie mit Erzählsplittern»; Darstellung «Organigramm».

#### 3.11 `climax` Steigerung, Abnahme, Staffel
- **Glieder:** Stufen in Reihenfolge, Richtung, was wächst oder abnimmt, Schlussglied, Begründung am Ende.
- **Prüffrage:** Sind alle Stufen da, Richtung und Schlussbegründung ([[ROM.5.5]]) erhalten?
- **Zusammenfassung:** Stufen in Reihenfolge, mit «→».
- **Darstellung:** `stairs`.
- **Untertypen:** Steigerung; Abnahme; wachsende Formel; Staffel (gleiche Handlung nach Stand oder Vermögen abgestuft).
- **Beispiele:** [[ROM.8.29-ROM.8.30]]; [[2PE.1.5-2PE.1.7]]; [[ROM.5.3-ROM.5.5]]; Ausbreitung der Sünde [[GEN.3-GEN.11]] (Vorschlag:
  Sünde → Gottesrede → Strafe → Gnadenzeichen); Segen 3/5/7 Wörter [[NUM.6.24-NUM.6.26]]; Greuel [[EZK.8.5-EZK.8.16]]; Tempelstrom
  [[EZK.47.3-EZK.47.5]]; acht Verbote abwärts [[OBA.1.12-OBA.1.14]]; abnehmende Form Klgl 1–5; wachsende Formel [[REV.4.5]], [[REV.8.5]],
  [[REV.11.19]], [[REV.16.18-REV.16.21]]; Staffel [[LEV.4]], [[LEV.5.7-LEV.5.13]], Verarmungsstufen [[LEV.25.25-LEV.25.47]].
- **Fallstricke:** Leitern kürzen (acht Glieder in 2 Petr 1); Begründung am Ende weglassen.
- **Aufgegangen in:** `decline`, `growing_formula`, `scale`.

### C Gegenüberstellung und Spiegelung

#### 3.12 `contrast` Gegensatz
- **Glieder:** zwei Seiten mit Bezeichnung, Paare Zeile für Zeile, Verbindungswort («ihr habt gehört – ich aber», «nicht – sondern»,
  «einst – jetzt», «aber nicht», «und doch»).
- **Prüffrage:** Sind die Seiten nicht vertauscht, beide vorhanden, alle Paare da? Bleibt ein Ungleichgewicht (Einzahl Frucht ↔
  Mehrzahl Werke) sichtbar?
- **Zusammenfassung:** Gegenüberstellung je Paar; «nicht … sondern …».
- **Darstellung:** `columns`; `grid` mit geteilten Feldern für Paarreihen.
- **Untertypen:** Paarreihe; «nicht … sondern» (falsche Gründe ausgeschlossen); einst – jetzt; Reihe gegen Reihe; zwei Ketten;
  Trotzdem (Mangel ↔ Vertrauen, ohne Ursache); Gegenbild (Nachahmung des Originals).
- **Beispiele:** Antithesen [[MAT.5.21-MAT.5.48]]; zwei Wege [[PSA.1]]; [[DEU.7.7-DEU.7.8]], [[DEU.9.4-DEU.9.6]]; Feldrede
  [[LUK.6.20-LUK.6.26]]; «aber nicht» [[2CO.4.8-2CO.4.9]], «und doch» [[2CO.6.8-2CO.6.10]]; Sinai ↔ Zion [[HEB.12.18-HEB.12.24]]; zwei
  Ketten [[JAS.1.14-JAS.1.18]]; Trotzdem [[HAB.3.17-HAB.3.19]]; Gegenbilder Lamm ↔ Tier, Siegel ↔ Malzeichen ([[REV.7.3]] ↔ [[REV.13.16]]);
  Edom ↔ blühende Wüste [[ISA.34-ISA.35]].
- **Fallstricke:** «ihr habt gehört» mit «das AT» gleichsetzen ([[MAT.5.43]] steht so nicht im AT); nur eine Seite zeigen; Dualismen
  auflösen.
- **Aufgegangen in:** `antithetic-series`, `despite`, `parody`, Erweiterung `contrast` «nicht … sondern», `diptych` im Sinn
  antithetischer Gegenstücke (Jes 34 ↔ 35).

#### 3.13 `balance` Vergleich und Abwägung
- **Glieder:** beide Seiten mit allen Gliedern, Massstab, Ausschlag oder Entscheid (falls im Text), Richtung des Schlusses.
- **Prüffrage:** Wird kein «richtig ↔ falsch» erfunden, wo zwei gültige Seiten stehen? Ist die Richtung von «wie viel mehr» richtig?
  Wird ein Übergewicht nicht als Gleichgewicht gezeigt ([[ROM.5.15-ROM.5.17]])?
- **Zusammenfassung:** «besser A … als B …»; «wenn schon …, wie viel mehr …»; «einerseits – andererseits – Entscheid».
- **Darstellung:** `balance`; `columns` für Vergleichsreihen.
- **Untertypen:** Besser-als-Spruch; Spannungspaar; Abwägung mit Entscheid; Schluss vom Kleineren aufs Grössere; Vergleichsreihe
  «besser»; Bilanz (Umbuchung von Werten).
- **Beispiele:** [[PRO.15.16-PRO.15.17]]; [[PRO.26.4-PRO.26.5]]; [[ECC.7.1-ECC.7.14]]; [[JON.4.10-JON.4.11]]; [[MAL.1.8]];
  [[HEB.2.2-HEB.2.3]], [[HEB.9.13-HEB.9.14]], [[HEB.12.25]]; «besser» [[HEB.7.19]] bis [[HEB.12.24]]; Abwägung [[PHP.1.21-PHP.1.26]];
  Bilanz [[PHP.3.4-PHP.3.8]].
- **Fallstricke:** [[PRO.26.4-PRO.26.5]] als Widerspruch auflösen; «wie viel mehr» zum blossen Vergleich machen.
- **Aufgegangen in:** `balance`, `a_fortiori`, `deliberation`, `synkrisis`, «Bilanz (Gewinn ↔ Verlust)».

#### 3.14 `reversal` Umkehrung, Abstieg und Aufstieg
- **Glieder:** Ausgangslage, Umschlagpunkt, Endlage; Paare «vorher ↔ nachher» auf gleicher Höhe; bei Überkreuzung beide Figuren; bei
  der V-Bewegung alle Stufen und das Scharnier.
- **Prüffrage:** Sind die Paare vollständig, der Umschlagpunkt ([[EST.6.1]]; «darum» [[PHP.2.9]]) und beide Hälften erhalten?
- **Zusammenfassung:** Paare «A wird zu B»; bei Abstieg und Aufstieg Stufen mit Scharnier.
- **Darstellung:** `mirror` (Spiegelachse, X-Diagramm); `stairs` (V-Kurve, Höhenprofil).
- **Untertypen:** Umkehrung der Lage; Überkreuzung zweier Figuren; gegenläufige Bewegung; Abstieg und Aufstieg; Vorher – Nachher
  (Anfang und Ende gespiegelt); Umkehrung eines Wortes oder Namens.
- **Beispiele:** Umkehrungstabelle [[EST.9.1]]; Josef [[GEN.37-GEN.50]] mit [[GEN.50.20]]; [[1SA.2.4-1SA.2.8]]; [[LUK.1.51-LUK.1.53]];
  leer ↔ voll [[RUT.1.21]] ↔ [[RUT.4.14-RUT.4.17]]; David ↑ / Saul ↓ (1 Sam 16–31); Blindgeborener [[JHN.9]]; [[PHP.2.6-PHP.2.11]];
  [[1PE.3.18-1PE.3.22]]; Abstieg [[JON.1.3-JON.2.6]]; hoch ↔ tief [[OBA.1.3-OBA.1.4]]; Vorher – Nachher [[JOB.1.2-JOB.1.3]] ↔
  [[JOB.42.12-JOB.42.13]]; Versäumnis ↔ Heilshandeln [[EZK.34.4]] ↔ [[EZK.34.16]]; Kindernamen [[HOS.1.4-HOS.1.9]] ↔ [[HOS.2.23]].
- **Fallstricke:** nur Erhöhung oder nur Erniedrigung zeigen; die unscheinbare Mitte (schlaflose Nacht) weglassen.
- **Aufgegangen in:** `reversal` (alle Analysen), `crossing`, `counter`, `mirror` (Vorher-Nachher; Spiegelung), `descent-ascent`,
  `arc`, `elevation`.

#### 3.15 `parallel` Parallelfassung und Wiederholung
- **Glieder:** Fassungen mit Stellen, gemeinsame Glieder, Unterschiede («nur hier / nur dort / beide»), bei Anweisung ↔ Ausführung die
  Übereinstimmung; Richtung der Abhängigkeit nur als `interpretation`.
- **Prüffrage:** Wird nicht harmonisiert? Sind die Unterschiede (Zahlen, Anstifter, Reihenfolge) ausgegeben? Wird jede Fassung nach
  ihrem eigenen Bau verdichtet?
- **Zusammenfassung:** gemeinsamer Kern, dann die Unterschiede.
- **Darstellung:** `columns` als Synopse.
- **Untertypen:** Parallelfassung (in einem oder in zwei Büchern); Wiedererzählung; parallele Hälften; Parallelszenen; Spiegelszene
  (bewusste Parallele zu anderer Szene); Diptychon (Parallelführung mit Überbietung); Anweisung ↔ Ausführung.
- **Beispiele:** Dekalog [[EXO.20.1-EXO.20.17]] ↔ [[DEU.5.6-DEU.5.21]]; [[JDG.4]] ↔ [[JDG.5]]; [[2SA.24]] ↔ [[1CH.21]] (HERR ↔ Satan);
  [[EXO.25-EXO.31]] ↔ [[EXO.35-EXO.40]]; [[JON.1-JON.2]] ↔ [[JON.3-JON.4]]; [[SNG.3.1-SNG.3.5]] ↔ [[SNG.5.2-SNG.6.3]]; [[JDG.19]] ↔ [[GEN.19]];
  [[LUK.1.5-LUK.2.52]]; Berufung des Paulus [[ACT.9.1-ACT.9.19]], [[ACT.22.3-ACT.22.16]], [[ACT.26.9-ACT.26.18]]; [[2PE.2.1-2PE.3.3]] ↔
  [[JUD.1.4-JUD.1.18]]; Reichsreihen [[DAN.2]], [[DAN.7]], [[DAN.8]].
- **Fallstricke:** Seligpreisungen Mt und Lk vermischen; Wiederholung in Ex 35–40 streichen («genau wie geboten» trägt).
- **Aufgegangen in:** `synopsis` (Tora; grosse Propheten; Offb), `parallel_version`, `retelling`, `parallel_halves`, `parallel_scenes`,
  `mirror_scene`, `diptych` (Parallelführung), `instruction_execution`.

#### 3.16 `frame` Rahmen, Chiasmus, Schachtelung
- **Glieder:** Rahmenglieder (A … A') mit Stellen, Paare, Mitte; bei Schachtelung äussere und innere Erzählung.
- **Prüffrage:** Sind Rahmen und Mitte erhalten? Ist der Chiasmus vom Text gesichert oder ein Vorschlag (dann `interpretation`)?
  Bleibt die Schachtelung eine Einheit, deren Mitte den Rahmen deutet?
- **Zusammenfassung:** Gliederung mit Mitte; «X umschliesst Y».
- **Darstellung:** `rings` (Mitte betont); `outline` als Bild im Bild.
- **Untertypen:** Inklusio; Chiasmus; konzentrischer Buchbau; Schachtelung (A – B – A').
- **Beispiele:** [[MAT.1.23]] ↔ [[MAT.28.20]]; [[PSA.8.2]] = [[PSA.8.9]]; Anhang [[2SA.21-2SA.24]] (anerkannt); [[ROM.2.6-ROM.2.11]];
  Schachtelungen [[MRK.5.21-MRK.5.43]], [[MRK.11.12-MRK.11.25]], [[JHN.18.15-JHN.18.27]]; Klgl nach Umfang 22-22-66-22-22; Gaben – Liebe –
  Gaben [[1CO.12-1CO.14]]; Prolog ↔ Epilog [[REV.1.1-REV.1.8]] ↔ [[REV.22.6-REV.22.21]]; Gen 2 ↔ Offb 22 als Rahmen der Bibel.
- **Fallstricke:** Vorschläge als Befund zeigen (Flut, Levitikus als Mitte, Vaterunser als Mitte der Bergpredigt); Schachtelung in zwei
  Geschichten zerlegen.
- **Aufgegangen in:** `nest`; Rahmenteil von `vision_ring`.

### D Logik und Argument

#### 3.17 `condition` Bedingung → Folge
- **Glieder:** Bedingung(en) wörtlich, jeder Zweig mit Folge, Unterfälle, Geltung (an wen); Art: Verheissung, Drohung,
  Selbstverfluchung, Rechtsfall, offene Hoffnung.
- **Prüffrage:** Sind beide Zweige da? Wird keine Bedingung zur Folge, keine Gabe zur Bedingung ([[DEU.7.8]])? Bleibt eine offene Folge
  offen? Bleibt der Rückweg nach dem Fluch ([[LEV.26.40-LEV.26.45]]; [[DEU.30.1-DEU.30.10]])?
- **Zusammenfassung:** «wenn … dann …; wenn nicht … dann …».
- **Darstellung:** `switch`; `grid` für Bedingungsraster und Eid-Tabellen.
- **Untertypen:** Weiche; Bedingungsraster (zwei Bedingungen gekreuzt); kasuistischer Rechtssatz mit Unterfällen (Entscheidungsbaum,
  auch mit Warteschleife); gestuftes Verfahren (nächste Stufe nur, wenn die vorige scheitert); Eid (Selbstverfluchung, kein
  Verheissungszweig); offene Hoffnung.
- **Beispiele:** [[DEU.28]]; [[LEV.26]]; [[ISA.1.19-ISA.1.20]]; [[JER.18.7-JER.18.10]] (2 × 2); Wächter [[EZK.3.17-EZK.3.21]],
  [[EZK.33.1-EZK.33.9]]; Rinderstoss [[EXO.21.28-EXO.21.36]]; Aussatz [[LEV.13-LEV.14]]; Eid [[JOB.31]]; Stufen [[MAT.18.15-MAT.18.17]];
  [[MAT.6.14-MAT.6.15]]; vier Bedingungen, drei Folgen [[2CH.7.14]]; «und wenn nicht» [[DAN.3.17-DAN.3.18]]; Witwenregel
  [[1TI.5.3-1TI.5.16]]; gebrochene Reihe [[2TI.2.11-2TI.2.13]].
- **Fallstricke:** Fluchzweig ohne Segenszweig oder umgekehrt; «vielleicht» zur Zusage machen; Kasuistik auf «gerecht/ungerecht»
  verkürzen.
- **Aufgegangen in:** `law`, `oath`, `matrix` im Sinn «Bedingungsraster» (grosse Propheten), `stages`, `open_condition`,
  `generations` (verschachtelt mit `tree`).

#### 3.18 `cause` Ursache, Begründung, Zweck
- **Glieder:** Kettenglieder in Richtung; Verbindungswörter (denn, darum, damit, weil); Zweck; bei Zuspruch → Anspruch das Scharnierwort.
- **Prüffrage:** Stimmt die Richtung (Präambel des Dekalogs vor den Geboten; Begründung nicht als Bedingung)? Sind Zuspruch und Anspruch
  beide da? Ist ein Erzählerkommentar als Kommentar gekennzeichnet?
- **Zusammenfassung:** Pfeilkette in Worten, Verbindungswörter behalten.
- **Darstellung:** `arrows` (auch zwei Stockwerke); `circle` als Kreispfeil für die Spiegelstrafe.
- **Untertypen:** Kette; Begründung; Zweck; Zuspruch → Anspruch (auch umgekehrt mit nachgestelltem «denn», Tit); Regel «nicht – sondern
  – denn/damit»; Spiegelstrafe (Tat fällt auf den Täter zurück); Ätiologie (Ereignis → Name, Brauch, «bis auf diesen Tag»).
- **Beispiele:** [[MRK.5.34]]; [[TIT.2.11-TIT.2.12]]; [[ROM.1.16-ROM.1.17]]; Scharnier [[ROM.12.1]], [[EPH.4.1]], [[COL.3.1]];
  [[EPH.4.25-EPH.4.32]]; [[2KI.17.7-2KI.17.23]]; [[OBA.1.15]]; [[MIC.2.1-MIC.2.5]]; Credo [[DEU.26.5-DEU.26.10]]; Ursache-Fragen
  [[AMO.3.3-AMO.3.8]]; Purim [[EST.9.20-EST.9.32]]; Steine [[JOS.4.6-JOS.4.7]].
- **Fallstricke:** Paränese ohne «nun» ([[ROM.12.1]]); Pflichten ohne Begründung ([[TIT.2.11-TIT.2.14]]); «nicht aus Werken» ohne «zu guten Werken»
  ([[EPH.2.8-EPH.2.10]]).
- **Aufgegangen in:** `indicative-imperative`, `triad-rule`, `talion`, `etiology`, `narrator_comment` (mit Merkmal `speakers`).

#### 3.19 `argument` Beweisgang
- **Glieder:** These, Belege (Schriftzitat mit Quelle, Beispiel, Erfahrung), Schritte, Wende («nun aber»), Folgerung; bei Auslegung
  das Zitat und die ausgelegten Stichworte.
- **Prüffrage:** Ist jede Stufe eines Kettenschlusses da, die Wende, die Folgerung? Sind Zitate als Zitate mit Quelle erkennbar?
- **Zusammenfassung:** «These – denn … – also …».
- **Darstellung:** `arrows` mit Belegkästen; Dominokette.
- **Untertypen:** Kettenschluss vorwärts und rückwärts; Schriftkette; Zitat und Auslegung; Beispiel → «diese sind»; Beweis aus der
  Zeitachse.
- **Beispiele:** [[1CO.15.13-1CO.15.20]]; rückwärts [[ROM.10.14-ROM.10.15]]; Schriftkette [[ROM.3.10-ROM.3.18]], [[ROM.15.9-ROM.15.12]];
  Abraham [[ROM.4]]; 430 Jahre [[GAL.3.15-GAL.3.18]]; Auslegung von Ps 95 [[HEB.3.7-HEB.4.11]]; Melchisedek [[HEB.7]]; [[JUD.1.5-JUD.1.19]];
  [[ACT.2.14-ACT.2.36]]; [[ACT.13.16-ACT.13.41]]; [[ACT.7]].
- **Fallstricke:** Kettenschluss halbieren; Reden nur als Szene «X predigt» darstellen.
- **Aufgegangen in:** `argument`, `sorites`, `catena`, `midrash`.

#### 3.20 `objection` Einwand und Antwort
- **Glieder:** These, Einwand wörtlich mit Herkunft (fingiert, Parole der Adressaten, Einwurf des Volkes), Abweisung («Das sei ferne!»),
  Antwort mit Begründung.
- **Prüffrage:** Wird der Einwand nie als Meinung des Autors ausgegeben? Bleibt er stehen (ohne ihn verschwindet die Gestalt)?
- **Zusammenfassung:** «Einwand: … – Antwort: …».
- **Darstellung:** `dialogue`, Einwand als fremde Stimme markiert.
- **Untertypen:** Diatribe; Parole und Korrektur; Diskussionswort (Behauptung Gottes → «Worin …?» → Begründung).
- **Beispiele:** [[ROM.3.8]]; [[ROM.6.1-ROM.6.2]]; [[ROM.6.15]]; [[ROM.9.14]]; [[1CO.6.12-1CO.6.13]]; [[1CO.8.1]]; [[1CO.10.23]];
  [[GAL.2.17]]; [[JAS.2.18-JAS.2.20]]; sechs Diskussionsworte [[MAL.1.2-MAL.4.3]].
- **Fallstricke:** Parolen der Korinther als Paulus-Lehre; welche Sätze Zitate sind, ist teils `interpretation` ([[1CO.7.1]]).
- **Aufgegangen in:** `objection`, `diatribe`, `slogan`, `disputation`.

### E Rede und Gattungsform

#### 3.21 `dialogue` Rede und Gegenrede
- **Glieder:** Sprecher in Reihenfolge, Kern je Rede, Runden, Antworten, fehlende Reden, Bewertung durch den Text.
- **Prüffrage:** Ist bei jeder Aussage der Sprecher genannt? Sind verworfene Reden gekennzeichnet? Bleiben Runden und Lücken sichtbar?
  Hat ein Missverständnis beide Ebenen?
- **Zusammenfassung:** wer sagt was, in Reihenfolge.
- **Darstellung:** `dialogue`; `grid` als Rundenraster; `levels` für Missverständnisse.
- **Untertypen:** Rede und Gegenrede; Redegänge in Runden; Klagedialog mit Gott; Berufungsdialog mit Einwänden; Missverständnis
  (doppeldeutiges Wort → wörtlich verstanden → Klärung); Wechselrede.
- **Beispiele:** Redegänge [[JOB.4-JOB.27]] (Bildad kurz, Zofar fehlt); fünf Einwände [[EXO.3.1-EXO.4.17]]; Klagedialog
  [[HAB.1.2-HAB.2.5]]; zwei Runden [[LUK.10.25-LUK.10.37]]; Missverständnis [[JHN.3.3-JHN.3.5]], [[JHN.4.10-JHN.4.15]]; Jeremia ↔ Hananja
  [[JER.28]]; Boten zwischen Palast und Tor [[EST.4]].
- **Fallstricke:** Freundesreden Hiobs als biblische Lehre zitieren; Elihu mit Gott gleichsetzen.
- **Aufgegangen in:** `rounds`, `lament_dialogue`, `misunderstanding`; `voices` siehe Merkmal `speakers`.

#### 3.22 `form` Gattungsform mit festem Ablauf
- **Glieder:** die Pflichtglieder des Untertyps (Verzeichnis unten) mit Stellen; fehlende Glieder als `pattern_break`.
- **Prüffrage:** Sind alle Pflichtglieder vorhanden oder als fehlend vermerkt? Ist die Gattungsbezeichnung als Einordnung gekennzeichnet?
- **Zusammenfassung:** Glieder in der Folge der Form, je knapp.
- **Darstellung:** `outline` als Formularbild; Varianten: Gerichtsschema mit Rollen, Briefbild, Tabelle für Haustafeln.

| `form_type` | Form | Pflichtglieder | Beispiele |
|---|---|---|---|
| `lament` | Klagelied (Einzelner, Volk, Leichenklage) | Anrede – Klage (Gott, Feinde, Ich/Wir) – Vertrauen oder Rückblick – Bitte – Wende und Lobgelübde, wo vorhanden | [[PSA.13]]; [[PSA.22]]; [[PSA.44]]; [[PSA.88]] (ohne Wende); [[2SA.1.19-2SA.1.27]]; [[LAM.1.1]] |
| `hymn` | Hymnus, Eulogie | Aufruf zum Lob – Begründung «denn» – erneuter Aufruf | [[PSA.117]]; [[PSA.100]]; [[EPH.1.3-EPH.1.14]] |
| `thanksgiving` | Danklied | Lobankündigung – Bericht von Not, Schreien, Rettung – Lob, Aufruf | [[PSA.30]]; [[PSA.116]]; [[JON.2.2-JON.2.9]] |
| `liturgy` | Liturgie | Frage am Tor – Antwort als Bedingungsliste – Zusage; oder Bekenntnis des Volkes – Antwort Gottes (angenommen oder verworfen) | [[PSA.15]]; [[PSA.24]]; [[HOS.6.1-HOS.6.6]]; [[HOS.14.1-HOS.14.8]]; [[MIC.7.8-MIC.7.20]] |
| `lawsuit` | Rechtsstreit und Verfahren | Vorladung, Zeugen – Anklage – Beweis (oft Geschichte, Wohltaten) – Verteidigung oder Frage – Urteil, Weisung oder Angebot; erzählt auch als Instanzenweg mit Unschuldserklärungen | [[ISA.1.2-ISA.1.20]]; [[MIC.6.1-MIC.6.8]]; [[HOS.4.1-HOS.4.3]]; [[DEU.32.1-DEU.32.43]]; [[ISA.43.8-ISA.43.13]]; [[JER.26]]; [[JOS.22]]; [[RUT.4.1-RUT.4.12]]; [[LUK.23.1-LUK.23.25]]; [[ACT.21-ACT.26]]; Zeugenreihe [[JHN.5.31-JHN.5.47]] |
| `woe` | Weheruf | «Wehe» – Adressat – Tat – Folge (oft spiegelnd) | [[ISA.5.8-ISA.5.24]]; [[HAB.2.6-HAB.2.20]]; [[MAT.23]]; [[AMO.6.1-AMO.6.7]] |
| `call` | Berufungsbericht | Begegnung – Auftrag – Einwand – Zusage – Zeichen | [[EXO.3.1-EXO.4.17]]; [[JER.1.4-JER.1.19]]; [[ISA.6]] (mit Verstockungsauftrag) |
| `annunciation` | Geburtsankündigung | Erscheinung – Erschrecken – «Fürchte dich nicht» – Name und Bestimmung – Einwand – Zeichen | [[LUK.1.5-LUK.1.25]]; [[LUK.1.26-LUK.1.38]]; [[JDG.13]] |
| `theophany` | Theophanie | Kommen Gottes mit Herkunft – Reaktion der Natur – Wirkung, Frage | [[MIC.1.3-MIC.1.4]]; [[NAM.1.3-NAM.1.6]]; [[HAB.3.3-HAB.3.15]] |
| `treaty` | Bund und Vertragsformular | Präambel – Vorgeschichte – Grundsatz – Einzelbestimmungen – Segen und Fluch – Zeugen – Hinterlegung, Verlesung; erzählter Bundesschluss: Verlesung – Zusage des Volkes – Ritus – Zeugen | Dtn als Ganzes (Forschungsvergleich); [[EXO.24.1-EXO.24.11]]; [[JOS.24]]; [[NEH.10]] |
| `regnal` | Königsformular | Synchronismus – Alter – Regierungsjahre – Hauptstadt – Mutter (Juda) – Urteil – Quelle – Tod, Begräbnis – Nachfolger | [[1KI.15]] bis [[2KI.25]]; kleine Richter [[JDG.10.1-JDG.10.5]], [[JDG.12.8-JDG.12.15]] |
| `case_ruling` | Anfrage und Entscheid | Anfrage – Vorlage bei Gott oder Priester – Entscheid – allgemeine Regel oder Anwendung | [[NUM.27.1-NUM.27.11]]; [[HAG.2.11-HAG.2.14]]; [[ZEC.7.3]] → [[ZEC.8.18-ZEC.8.19]] |
| `letter` | Briefformular | Präskript – Proömium (Dank oder Eulogie) – Korpus – Paränese – Schluss (Reisen, Grüsse, eigenhändig, Segen) | [[ROM.1.1-ROM.1.17]]; [[GAL.1.6-GAL.1.9]] (kein Dank); [[PHM.1.1-PHM.1.25]] |
| `household` | Haustafel | Überschrift – Paare oder Gruppen – Pflicht – Gegenpflicht – Begründung oder Zweck | [[EPH.5.21-EPH.6.9]]; [[COL.3.18-COL.4.1]]; [[1PE.2.13-1PE.3.7]]; [[TIT.2.1-TIT.2.10]] |
| `testament` | Abschiedsrede | Rückblick – Weitergabe – Warnung vor kommenden Zeiten – Auftrag – Abschied | [[2TI.4.6-2TI.4.8]]; [[2PE.1.12-2PE.1.15]]; [[ACT.20.18-ACT.20.35]] |

- **Fallstricke:** Gattungsbegriffe sind Forschungsbegriffe; Mischformen (Ps 19, Ps 22) als Mischform angeben; Haustafel einseitig;
  Vertragsvergleich als Tatsache.
- **Aufgegangen in:** `lawsuit` (Tora; grosse und kleine Propheten), `procedure`, `trial`, `liturgy` (beide Bedeutungen), `theophany`,
  `treaty`, `letter`, `household`, `relations`, `tora_inquiry`, `formula` im Sinn «Königsformular» (einzelner Eintrag); `law` als Fallrecht.

#### 3.23 `poem` Gedichtbau
- **Glieder:** Parallelismus (beide Halbverse), Strophen, Kehrvers mit Stellen, Akrostichon (Buchstaben, Lücken, Umstellungen),
  Beschreibungsrichtung, Rahmen.
- **Prüffrage:** Bleibt der Kehrvers? Wird die Alphabetform genannt, mit Lücken ([[PSA.145.13-PSA.145.14]], Nun fehlt im MT) und
  Umstellungen (Pe vor Ajin in Klgl 2–4)? Bleiben zusammengehörige Psalmen zusammen ([[PSA.42-PSA.43]]; [[PSA.9-PSA.10]])?
- **Zusammenfassung:** Aufbau benennen, Kehrvers zitieren.
- **Darstellung:** `outline` (Leiter, Strophenbild mit Kehrversband); `grid` als Alphabet-Raster; `figure` als Bildtafel.
- **Untertypen:** Parallelismus; Strophen mit Kehrvers; Akrostichon; Beschreibungslied (Körperteil → Vergleichsbild in fester Richtung).
- **Beispiele:** Leiter [[PSA.19.2]]; Kehrvers [[PSA.42.5]], [[PSA.42.11]], [[PSA.43.5]]; [[PSA.80.3]], [[PSA.80.7]], [[PSA.80.19]] (wachsend);
  Litanei [[PSA.136]]; [[PSA.119]]; [[PRO.31.10-PRO.31.31]]; Klgl 1–4; Beschreibungslieder [[SNG.4.1-SNG.4.7]] (oben → unten),
  [[SNG.7.1-SNG.7.9]] (unten → oben); [[2SA.1.19-2SA.1.27]].
- **Fallstricke:** Kehrvers als Wiederholung streichen; Bildsprache wörtlich bebildern; Teilakrostichon (Nah 1) als sicher zeigen.
- **Aufgegangen in:** `acrostic`, `ladder`, `wasf`.

### F Bild und Deutung

#### 3.24 `parable` Gleichnis, Bildrede, Allegorie
- **Glieder:** Bildhälfte mit allen tragenden Bildelementen; Sachhälfte nur, soweit der Text deutet; Zuordnungen; Pointe; Frage oder
  Anwendung an die Hörer.
- **Prüffrage:** Wird nur gedeutet, wo der Text deutet? Werden Bild und Sache nicht deckungsgleich gemacht ([[ROM.7.1-ROM.7.6]])?
  Ist Bildsprache als Bild gekennzeichnet?
- **Zusammenfassung:** Bildhälfte; Sachhälfte, wenn der Text sie gibt.
- **Darstellung:** `levels`; `figure` mit Legende Bild → Sache je Teil.
- **Untertypen:** Gleichnis; juristisches Gleichnis (Selbstanklage); Fabel; Bildwort und Metapher; Bildfeld-Tafel (Aussage in vielen
  wechselnden Bildern); Allegorie mit Zuordnungstabelle.
- **Beispiele:** [[MRK.4.3-MRK.4.20]]; [[2SA.12.1-2SA.12.7]]; [[ISA.5.1-ISA.5.7]]; [[JDG.9.7-JDG.9.20]]; [[EZK.17]]; Ez 16 und 23 (nur als
  Tabelle); Bildfeld Hosea 4–14; [[ECC.12.1-ECC.12.7]] (Deutung umstritten); Waffenrüstung [[EPH.6.13-EPH.6.17]]; Bau [[1CO.3.10-1CO.3.15]].
- **Fallstricke:** drastische Bildsprache szenisch bebildern oder verharmlosen; Allegorien des Hohenliedes als Text ausgeben.
- **Aufgegangen in:** `fable`, `metaphor`, `metaphor_board`, «Figur-Skizze mit Bild ↔ Sache je Teil» (Variante von `figure`).

#### 3.25 `sign_act` Zeichenhandlung
- **Glieder:** Auftrag, Handlung oder Name oder Gegenstand, Ausführung (falls berichtet), Deutung durch den Text, Zeitbezug.
- **Prüffrage:** Ist die Deutung immer dabei? Sind Zahlen ungeglättet (390/40 Tage, LXX abweichend)? Wird nur Aufgetragenes nicht als
  Ausgeführtes dargestellt?
- **Zusammenfassung:** «Handlung → Bedeutung».
- **Darstellung:** `levels` (Handlung oben, Bedeutung unten); `grid` für Reihen «Handlung → Deutung».
- **Beispiele:** Ahijas Mantel [[1KI.11.29-1KI.11.39]]; Kindernamen [[ISA.7.3]], [[ISA.7.14]], [[ISA.8.1-ISA.8.4]], [[ISA.8.18]]; [[JER.13.1-JER.13.11]];
  Ackerkauf [[JER.32.6-JER.32.15]]; [[EZK.4-EZK.5]]; zwei Hölzer [[EZK.37.15-EZK.37.28]]; [[HOS.1]], [[HOS.3]]; Krönung [[ZEC.6.9-ZEC.6.15]];
  Hirtenstäbe [[ZEC.11.4-ZEC.11.17]].
- **Fallstricke:** Zeichenhandlung ohne Deutung (wirkt absurd); messianische Lesart ([[ISA.7.14]]) in den Text schieben.
- **Aufgegangen in:** `sign_act`, `symbolic_act`.

#### 3.26 `typology` Vorbild und Gegenbild
- **Glieder:** Typos mit Stelle, Antitypos, Entsprechungen Zeile für Zeile, Übergewicht («viel mehr»), Kennzeichnung durch den Text
  («allegorisch geredet» [[GAL.4.24]]; «Gegenbild» [[1PE.3.21]]; «Abbild und Schatten» [[HEB.8.5]]).
- **Prüffrage:** Stellt der Text selbst die Beziehung her (sonst `crossref` oder `interpretation`)? Wird das Übergewicht nicht als
  gleichgewichtige Spiegelung gezeigt? Wird «Schatten» nicht als «falsch» wiedergegeben?
- **Zusammenfassung:** «wie … so …», Zuordnungen.
- **Darstellung:** `levels` (vertikal); `columns` als Zuordnungstabelle.
- **Abgrenzung:** `parable` deutet ein Bild; `typology` verbindet zwei wirkliche Grössen zu verschiedenen Zeiten; `realms` zeigt zwei
  gleichzeitige Bühnen.
- **Beispiele:** [[ROM.5.12-ROM.5.21]]; [[1CO.10.1-1CO.10.13]]; [[1CO.15.21-1CO.15.22]]; [[GAL.4.21-GAL.4.31]]; [[HEB.9.24]]; [[1PE.3.20-1PE.3.21]];
  [[COL.2.16-COL.2.17]]; Plagen Ägyptens hinter Posaunen und Schalen (Offb 8–16).
- **Fallstricke:** Hagar ↔ Sara als Juden ↔ Christen vereinfachen.
- **Aufgegangen in:** `typology`, «Urbild ↔ Schatten».

### G Raum, Gestalt und Weg

#### 3.27 `space` Raum, Bauwerk, Gestalt
- **Glieder:** Teile und ihre Lage, Masse mit Stelle, Material, Zonen und Zugangsregeln, Richtung der Beschreibung, Lücken.
- **Prüffrage:** Wird nur Genanntes gezeigt, Fehlendes offen gelassen (Höhen in Ez 40–48)? Masse in Ellen, Umrechnung als Annahme?
  Werden Wesen nicht vermischt ([[EZK.1]] ↔ [[EZK.10.14]] ↔ [[REV.4]])? Bleibt «wie» als Annäherung erkennbar?
- **Zusammenfassung:** knappe Beschreibung der Teile und ihrer Lage.
- **Darstellung:** `model` (Grundriss, Schnitt, 3D, Zonenplan, Lagerplan, Bühne); `figure` (Gestalt, Wesen, emblematisch); `rings` für Zonen.
- **Untertypen:** Bauwerk; Zonen abgestufter Heiligkeit; Lagerplan; Gestalt mit Rangfolge der Teile; Wesen und Embleme; Bühne
  (Szene lebt vom Raumwechsel).
- **Beispiele:** Stiftshütte [[EXO.25-EXO.27]]; Arche [[GEN.6.15-GEN.6.16]]; Lager [[NUM.2-NUM.3]]; Tempel [[1KI.6-1KI.7]]; Tempelvision
  [[EZK.40-EZK.48]]; Statue [[DAN.2.31-DAN.2.45]]; Thronwagen [[EZK.1]]; Thronsaal [[REV.4]]; Menschensohn [[REV.1.12-REV.1.20]]; Neues
  Jerusalem [[REV.21.9-REV.22.5]]; Mauer [[NEH.3]]; Heiligtum [[HEB.9.1-HEB.9.10]]; Pilatus drinnen ↔ draussen [[JHN.18.28-JHN.19.16]].
- **Fallstricke:** Ex 33 (Zelt ausserhalb) mit der Stiftshütte vermischen; Tempelvision mit Salomos Tempel verwechseln; zwei Stammeslisten
  in Ez 48 vereinheitlichen; Symbolwesen naturalistisch zeichnen.
- **Aufgegangen in:** `zones`, `ranked_figure`, `stage`; Darstellung «Lagerplan».

#### 3.28 `route` Weg, Reise, Bewegung
- **Glieder:** Stationen mit genannten Orten, Richtung, Hin- und Rückweg, Weichen, Bewegungen von Gruppen oder einer Erscheinung, Etappen.
- **Prüffrage:** Nur genannte Orte? Unsichere Lagen gekennzeichnet? Konventionen («erste Missionsreise») als Konvention? Gespiegelte
  Rückwege erhalten?
- **Zusammenfassung:** Stationen in Reihenfolge.
- **Darstellung:** `map`; `model` als Weg im Grundriss oder Lageskizze.
- **Untertypen:** Reise; Stationenliste; Rundgang mit Vermessung; Weg einer Erscheinung; Ritualweg im Raum; Bewegung von Gruppen.
- **Beispiele:** Stationen [[NUM.33.1-NUM.33.49]]; Jakob [[GEN.25.19-GEN.35.29]]; Flucht und Rückkehr Davids [[2SA.15-2SA.19]]; Elija
  [[2KI.2.1-2KI.2.14]]; Weiche [[ACT.16.6-ACT.16.10]]; Versöhnungstag [[LEV.16]]; Tempelrundgang [[EZK.8]]; Herrlichkeit
  [[EZK.10.18-EZK.10.19]], [[EZK.11.23]] ↔ [[EZK.43.1-EZK.43.5]]; Ai [[JOS.8]]; zwei Chöre [[NEH.12.31-NEH.12.43]]; Emmaus [[LUK.24.13-LUK.24.35]];
  Lebenslauf als Argument [[GAL.1.13-GAL.2.14]].
- **Fallstricke:** Reisebericht [[LUK.9.51-LUK.19.27]] mit erfundener Route; Karte als Endzeitkarte ([[ZEC.14.4]]).
- **Aufgegangen in:** `tour`, `movement`, `tactical_sketch`; Darstellung «Weg im Grundriss».

#### 3.29 `territory` Gebiet und Verteilung
- **Glieder:** Gebiete, Grenzlinien und Grenzpunkte, Zuteilung (wem), Städtelisten, Etappen der Verteilung, Masse.
- **Prüffrage:** Sind alle Anteile da, verschiedene Listen nicht vereinheitlicht, Rekonstruktionen gekennzeichnet?
- **Zusammenfassung:** Anteile und ihre Ordnung.
- **Darstellung:** `map` (Gebietskarte, Streifenkarte).
- **Beispiele:** [[JOS.13-JOS.19]]; Asylstädte [[JOS.20.7-JOS.20.8]]; Levitenstädte [[JOS.21]]; [[NUM.34-NUM.35]]; Streifen
  [[EZK.47.13-EZK.48.35]]; [[OBA.1.19-OBA.1.20]]; Ostjordanland [[NUM.32]].
- **Fallstricke:** Landverteilung als Liste weglassen (zweiter Hauptteil Josuas und Erfüllung).
- **Aufgegangen in:** `territory`, `allotment`.

#### 3.30 `outward` Ausweitung
- **Glieder:** Zentrum, Ringe in Reihenfolge nach aussen, was je Ring geschieht.
- **Prüffrage:** Läuft die Richtung von innen nach aussen? Wird kein Rückweg erfunden (anders als `frame`)? Sind alle Ringe da?
- **Zusammenfassung:** «von … über … bis …».
- **Darstellung:** `rings` (nach aussen); `map` mit Ringen.
- **Beispiele:** Schma [[DEU.6.4-DEU.6.9]]; Lob in Kreisen [[PSA.22.22-PSA.22.31]]; [[PSA.148]]; Programm [[ACT.1.8]] mit Apg 1–7 / 8–12 / 13–28;
  Gebet [[JHN.17]]; Lobpreis [[REV.5.8-REV.5.14]].
- **Aufgegangen in:** `outward`, `rings`, `expansion`; Darstellung «Kreise von innen nach aussen».

### H Vision und Ebenen

#### 3.31 `vision` Visionsbericht
- **Glieder:** Einleitung (Datum, Ort, «ich sah», «im Geist»), Bild in Teilen, Frage («Was siehst du?», «Was ist das?»), Deutung (wer
  deutet), Gotteswort oder Auftrag; bei Reihen Abfolge, Gruppierung (4 + 3; 2 + 2 + 1), Einschübe, Verschränkung; Gehörtes und Gesehenes.
- **Prüffrage:** Kommt die Deutung nur aus dem Text? Werden Reichsdeutungen, Zeitrechnungen und Zuordnungen nicht als Text gezeigt?
  Bleiben Visionsreihen ohne festgelegte Zeitachse? Sind Einschübe da?
- **Zusammenfassung:** nummerierte Abfolge mit Deutung im Text; parallele Reihen benennen.
- **Darstellung:** `figure` (emblematisch, beschriftet); `grid` (Reihen ohne Zeitachse); `rings` (Thronsaal, Visionszyklus); `levels`.
- **Untertypen:** Deutungsvision; Thronvision; Geschichtsschau; Visionszyklus (konzentrisch, Vorschlag); Visionsreihe; Hören ↔ Sehen.
- **Beispiele:** [[JER.1.11-JER.1.14]]; [[JER.24]]; [[AMO.7.1-AMO.7.9]], [[AMO.8.1-AMO.8.3]], [[AMO.9.1-AMO.9.4]] (Fürbitte nur bei 1–2);
  Nachtgesichte [[ZEC.1.7-ZEC.6.8]]; [[ISA.6]]; [[EZK.1]]; [[DAN.7]]; Siegel, Posaunen, Schalen [[REV.6-REV.16]]; Löwe gehört, Lamm gesehen
  [[REV.5.5-REV.5.6]], ebenso [[REV.7.4]] ↔ [[REV.7.9]].
- **Fallstricke:** Visionen als Ereignisbericht; Nachtgesichte als Zeitfolge; kleines Horn Dan 7 und 8 gleichsetzen; weisse Reiter
  [[REV.6.2]] und [[REV.19.11]] gleichsetzen.
- **Aufgegangen in:** `vision_qa`, `vision_dialogue`, `vision_ring`, `hear_see`; Verschränkung über `series` (Teleskop), `matrix`
  (Rekapitulation) und Merkmal `pattern_break` (`insertion`).

#### 3.32 `realms` Zwei Bühnen
- **Glieder:** obere und untere Bühne (Himmel ↔ Erde, sichtbar ↔ unsichtbar), Szenen je Bühne in Reihenfolge, Verbindungen (Lied
  antwortet auf Geschehen), Wissensvorsprung des Lesers.
- **Prüffrage:** Sind beide Bühnen da (Himmelsszenen in Hi 1–2; Lieder der Offenbarung)?
- **Zusammenfassung:** «auf der Erde … – im Himmel …».
- **Darstellung:** `levels`.
- **Beispiele:** [[JOB.1-JOB.2]]; [[1KI.22.10]] ↔ [[1KI.22.19-1KI.22.23]]; [[2KI.6.15-2KI.6.17]]; [[ISA.6]]; [[DAN.7.2-DAN.7.14]];
  Engelfürsten [[DAN.10.13]]; Lieder [[REV.4.8]], [[REV.5.9-REV.5.14]], [[REV.11.15-REV.11.18]], [[REV.19.1-REV.19.8]]; [[REV.12]].
- **Fallstricke:** Prolog Hiobs weglassen (Buch wird zur Diskussion ohne Wissensvorsprung); «der Satan» als späteren Teufel darstellen.
- **Aufgegangen in:** `two_stages`, `two_realms`, `levels`.

### I Buch- und Sammlungsbau

#### 3.33 `collection` Sammlung und Buchbau
- **Glieder:** Teile mit Überschriften und Nahtstellen (Doxologien, Formeln), Art der Verbindung (Stichwort, Thema, Grossschema),
  sich kreuzende Gliederungen, Verfasserangaben je Teil.
- **Prüffrage:** Wird keine Gedankenfolge erfunden, wo nur Sammlung ist (Spr 10–22; Jak)? Sind alle Teile des Grossschemas da (auch
  Heilsteile)? Bleiben Verfasserangaben bei ihrem Teil?
- **Zusammenfassung:** Teile mit Überschrift und Thema; bei Einzelspruchsammlung Themen bündeln, keine Reihenfolge erfinden.
- **Darstellung:** `outline` (Regal, Blockband, Buchband mit Marken); `network` (Themenkarte).
- **Untertypen:** Sammlung mit Nahtstellen; Einzelspruchsammlung; Stichwortkette; prophetisches Grossschema (Gericht über das eigene
  Volk → Völker → Heil); Kreuzgliederung (zwei Gliederungen überlagern sich).
- **Beispiele:** Psalter, Doxologien [[PSA.41.13]], [[PSA.72.18-PSA.72.20]], [[PSA.89.52]], [[PSA.106.48]]; Sprüche [[PRO.1.1]], [[PRO.10.1]],
  [[PRO.22.17]], [[PRO.25.1]], [[PRO.30.1]], [[PRO.31.1]]; [[PRO.10.1-PRO.22.16]]; Ezechiel [[EZK.1-EZK.24]] / [[EZK.25-EZK.32]] /
  [[EZK.33-EZK.48]]; Daniel (Sprache ↔ Gattung, Scharnier [[DAN.7]]); Stichworte [[JAS.1.4-JAS.1.5]], [[JAS.1.12-JAS.1.13]]; Zwölfprophetenbuch.
- **Fallstricke:** ganzes Buch Salomo zuweisen; Zeitschichten (Jes) als Tatsache oder verschweigen.
- **Aufgegangen in:** `collection`, `sayings`, `catchword`, `triptych`, `cross_outline`.

### Merkmale und Darstellungen aus den Vorschlägen

- Merkmal `speakers`: `voices`, `narrator_comment` (mit `cause`), `embedded_document`.
- Merkmal `stance`: «Sprecherhaltung (Ironie, Narrenrede)».
- Merkmal `authority`: «Autoritätsebene».
- Merkmal `genre`: `genre`.
- Merkmal `leitwort`: `leitwort`, `keyword`, `keyword_trace`, `motif`, «Leitwort», `heading_formula`, `formula` im Sinn
  «Gliederungsformel» (Evangelien), «Antwortkatalog (περὶ δέ)», Kehrvers in Prosa.
- Merkmal `pattern_break`: «Musterbruch», `insertion`, «3 + 1».
- Merkmal `open_end`: `open_end`, `open_ending`.
- Merkmal `modality`: Teil von `open_condition`.
- Merkmal `wordplay`: `wordplay`.
- Merkmal `text_forms`: Hinweis `text_forms`.
- Merkmal `interpretation`: `layers`.
- Merkmal `crossref`: `intertext_net`.
- Merkmal `chronology`: `dated_frame`, `dated_oracles`, `dual_timeline`, `thematic_order`, `synchronism`, `open_timeline`,
  «Korrespondenz-Zeitleiste».
- Merkmal `numbers`: `number_key`.
- Darstellung `network`: «Personennetz / Beziehungsdreieck», `network`.
- Darstellungen für Raum: «Weg im Grundriss», «Lagerplan» (`model`); «Organigramm» (`tree`); «Kreise von innen nach aussen» (`rings`).

## 4. Bücherübersicht

Gesamtaufbau als Muster, dann die wichtigsten Strukturen. Alles aus den Analysen; Vorschläge der Forschung als «Vorschlag».

| Buch | Gesamtaufbau | Wichtigste Strukturen |
|---|---|---|
| Gen (`GEN`) | Prolog + Gliederungsformel «Toledot» (`leitwort`); Urgeschichte `climax`, Vätergeschichte `sequence`; Haupt- und Nebenlinie `tree` | Schöpfungswoche `numbered` [[GEN.1.1-GEN.2.3]]; Ausbreitung der Sünde `climax` [[GEN.3-GEN.11]]; Verheissung mit Gefährdungen `fulfilment` [[GEN.12.1-GEN.12.3]]; Josef `reversal` [[GEN.37-GEN.50]] |
| Ex (`EXO`) | `route` Ägypten → Sinai; Achse Dienst für Pharao → Dienst für Gott; Anweisung → Bruch → Ausführung `parallel` | Plagen 3 × 3 + 1 `numbered` [[EXO.7.14-EXO.12.30]]; Dekalog mit Präambel [[EXO.20.1-EXO.20.17]]; Heiligtum mit Zonen `space` [[EXO.25-EXO.27]]; Goldenes Kalb mit drei Fürbitten [[EXO.32-EXO.34]] |
| Lev (`LEV`) | Gottesrede-Formel gliedert (`leitwort`); Frage der Gegenwart Gottes; Mitte Lev 16 oder 19 (Vorschlag) | Opferarten `matrix` [[LEV.1.1-LEV.6.7]] (dt. 1,1–5,26); Staffel `climax` [[LEV.4]]; Ritualweg `route` [[LEV.16]]; Festkalender `cycle` [[LEV.23]]; Segen und Fluch mit Rückweg [[LEV.26]] |
| Num (`NUM`) | `route` Sinai → Wüste → Moab; zwei Generationen `contrast` (Vorschlag Olson) | Volkszählungen `parallel` [[NUM.1]] ↔ [[NUM.26]]; Lagerplan `space` [[NUM.2-NUM.3]]; Kundschafter [[NUM.13-NUM.14]]; Bileam (3 + 1, Fluch → Segen) [[NUM.22-NUM.24]] |
| Dtn (`DEU`) | Reden Moses mit Überschriften [[DEU.1.1]], [[DEU.4.44]], [[DEU.29.1]], [[DEU.33.1]]; Vertragsformular `form` `treaty` (Vorschlag) | Dekalog `parallel` zu Ex 20 [[DEU.5.6-DEU.5.21]]; Schma `outward` [[DEU.6.4-DEU.6.9]]; Segen und Fluch `condition` [[DEU.28]]; Lied des Mose `lawsuit` [[DEU.32.1-DEU.32.43]] |
| Jos (`JOS`) | Eroberung / Verteilung; Rahmen Verheissung [[JOS.1.2-JOS.1.6]] → Erfüllung [[JOS.21.43-JOS.21.45]] | Los als Auswahlweg `tree` [[JOS.7.14-JOS.7.18]]; Landverteilung `territory` [[JOS.13-JOS.19]]; Bundesschluss `treaty` [[JOS.24]]; Summarien ↔ Restnotizen [[JOS.13.1-JOS.13.7]] |
| Ri (`JDG`) | `cycle` als Abwärtsspirale; Kehrvers «kein König» [[JDG.17.6]], [[JDG.21.25]]; Rahmen konzentrisch (Vorschlag) | Zyklusformeln als `matrix` [[JDG.3.7-JDG.16.31]]; Debora Prosa ↔ Lied `parallel` [[JDG.4-JDG.5]]; Jotamfabel `parable` [[JDG.9.7-JDG.9.20]]; Gibea ↔ Sodom [[JDG.19]] |
| Rut (`RUT`) | vier Akte `sequence`; Leere → Fülle `reversal`; Weg Moab ↔ Betlehem | leer ↔ voll [[RUT.1.21]] ↔ [[RUT.4.14-RUT.4.17]]; Kap. 2 ↔ 3 gleich gebaut `parallel`; Löserverfahren `lawsuit` [[RUT.4.1-RUT.4.12]]; Stammbaum [[RUT.4.18-RUT.4.22]] |
| 1 Sam (`1SA`) | nach Hauptfiguren überlappend; Überkreuzung `reversal` (Samuel/Eli, David/Saul) | Hannas Lied [[1SA.2.1-1SA.2.10]]; Wechselbau `interleave` [[1SA.2.11-1SA.2.26]]; Berufung 3 + 1 [[1SA.3]]; Salbung Davids als Auswahl [[1SA.16.1-1SA.16.13]] |
| 2 Sam (`2SA`) | Höhepunkt (7) → Schuld (11) → angekündigte Folgen (13–20) `fulfilment`; Anhang `frame` [[2SA.21-2SA.24]] | Wortspiel «Haus» [[2SA.7]]; Natans Gleichnis [[2SA.12.1-2SA.12.7]]; Strafansage [[2SA.12.10-2SA.12.12]]; Flucht und Rückkehr gespiegelt [[2SA.15-2SA.19]] |
| 1 Kön (`1KI`) | Salomo (1–11); ab 12 Doppelbahn Juda/Israel `interleave` mit Königsformular `regnal`; Prophetenzyklen | Tempel `space` [[1KI.6-1KI.7]]; Weihgebet sieben Fälle [[1KI.8.31-1KI.8.53]]; Karmel und Horeb 3 + 1 [[1KI.18]], [[1KI.19.11-1KI.19.12]]; zwei Bühnen [[1KI.22.19-1KI.22.23]] |
| 2 Kön (`2KI`) | ein Reich → zwei → eins → Exil; Formular und Bewertungsraster `matrix` | Himmelfahrt Elijas `route` [[2KI.2.1-2KI.2.14]]; Begründung des Falls als Erzählerkommentar [[2KI.17.7-2KI.17.23]]; Erfüllung [[2KI.23.15-2KI.23.18]]; offener Schluss [[2KI.25.27-2KI.25.30]] |
| 1 Chr (`1CH`) | Genealogien `tree` [[1CH.1-1CH.9]] (um Juda, Levi, Benjamin, Vorschlag) + David; `parallel` zu Samuel–Könige | Erzählsplitter [[1CH.4.9-1CH.4.10]]; Volkszählung [[1CH.21]] ↔ [[2SA.24]]; Dienstordnungen [[1CH.23-1CH.27]] |
| 2 Chr (`2CH`) | Tempel und nur Juda; `parallel` mit Auslassungen und Zusätzen; Schluss Kyrus | Bedingungsformel [[2CH.7.14]]; Lebenswenden `curve` [[2CH.26.16]], [[2CH.33.12-2CH.33.13]]; Brückenstelle [[2CH.36.22-2CH.36.23]] |
| Esra (`EZR`) | Schablone Erlass → Rückkehr → Bau → Widerstand → Vollendung → Fest, mit Neh dreimal `matrix`; Sprachwechsel | Heimkehrerliste `register` [[EZR.2]]; Widerstand thematisch (`chronology`) [[EZR.4.6-EZR.4.23]]; Briefwechsel (`speakers`); Formel «gute Hand» [[EZR.7.6]] |
| Neh (`NEH`) | Mauerbau – Erneuerung – Besiedlung – Rückfall; Ich-Bericht | Mauer nach Abschnitten [[NEH.3]]; Kehrformel «Gedenke meiner» [[NEH.5.19]], [[NEH.13.31]]; Verpflichtung ↔ Bruch [[NEH.10]] ↔ [[NEH.13]]; zwei Chöre [[NEH.12.31-NEH.12.43]] |
| Est (`EST`) | `reversal` mit Mitte [[EST.6.1]]; Gastmähler gliedern (Vorschlag); Ziel Purim | Umkehrungstabelle [[EST.9.1]]; Datumsgerüst (`chronology`); Weiche [[EST.4.13-EST.4.16]]; Ätiologie [[EST.9.20-EST.9.32]]; Fassungen hebr. ↔ griech. |
| Hiob (`JOB`) | Rahmen Prosa – Poesie – Prosa `frame`; innen `dialogue` in Runden | Himmel ↔ Erde `realms` [[JOB.1-JOB.2]]; Redegänge [[JOB.4-JOB.27]]; Eid [[JOB.31]]; Fragekatalog [[JOB.38.1-JOB.40.2]]; Urteil über die Reden [[JOB.42.7-JOB.42.8]] |
| Ps (`PSA`) | `collection` in fünf Büchern mit Doxologien; Doppeltor Ps 1–2, Schluss Ps 146–150 | Klage → Lob `lament` [[PSA.13]], [[PSA.22]]; Kehrvers [[PSA.42-PSA.43]]; Akrostichon [[PSA.119]]; Fallgruppen `matrix` [[PSA.107]]; Torliturgie [[PSA.15]] |
| Spr (`PRO`) | `collection` mit Überschriften; Rahmen Gottesfurcht [[PRO.1.7]], [[PRO.31.30]] | zwei Frauen [[PRO.9]]; Besser-als und Spannungspaar `balance` [[PRO.26.4-PRO.26.5]]; Zahlensprüche [[PRO.30.15-PRO.30.31]]; Akrostichon [[PRO.31.10-PRO.31.31]] |
| Pred (`ECC`) | Motto-Rahmen `frame` [[ECC.1.2]] ↔ [[ECC.12.8]], Nachwort in 3. Person; Mitte ohne Konsens | Kreisläufe [[ECC.1.4-ECC.1.7]]; 14 Paare [[ECC.3.1-ECC.3.8]]; Freude-Texte als Formel [[ECC.2.24-ECC.2.26]], [[ECC.9.7-ECC.9.10]]; Bildgedicht [[ECC.12.1-ECC.12.7]] |
| Hld (`SNG`) | Stimmenwechsel (`speakers`); Kehrvers [[SNG.2.7]], [[SNG.3.5]], [[SNG.8.4]]; Gliederung umstritten | Beschreibungslieder [[SNG.4.1-SNG.4.7]], [[SNG.7.1-SNG.7.9]]; Suchszenen `parallel`; Zugehörigkeitsformel [[SNG.2.16]], [[SNG.6.3]], [[SNG.7.10]]; Höhepunkt [[SNG.8.6-SNG.8.7]] ([[SNG.6.13]] = dt. 7,1) |
| Jes (`ISA`) | Teile 1–39 / 40–55 / 56–66 (Forschung) mit Brücke [[ISA.36-ISA.39]]; Leitmotive; Kehrvers [[ISA.48.22]], [[ISA.57.21]] | Rechtsstreit [[ISA.1.2-ISA.1.20]]; Weinberglied [[ISA.5.1-ISA.5.7]]; Kehrvers des Zorns [[ISA.9.8-ISA.10.4]]; viertes Knechtslied `frame` [[ISA.52.13-ISA.53.12]] |
| Jer (`JER`) | `collection` aus Worten und Erzählungen, nicht chronologisch; Leitwort sechs Verben [[JER.1.10]]; MT ↔ LXX | Töpfer 2 × 2 [[JER.18.7-JER.18.10]]; Zeichenhandlungen [[JER.13]], [[JER.32]]; neuer Bund [[JER.31.31-JER.31.34]]; Völkersprüche auf Karte [[JER.46-JER.51]] |
| Klgl (`LAM`) | konzentrisch nach Umfang `frame`; Abnahme der Form `climax`; Akrostichon `poem` | Mitte Hoffnung [[LAM.3.21-LAM.3.24]]; Erzähler ↔ Zion [[LAM.1.12]]; einst ↔ jetzt [[LAM.4.1-LAM.4.10]]; offenes Ende [[LAM.5.22]] |
| Ez (`EZK`) | Grossschema `collection`; Rahmen Herrlichkeit geht [[EZK.10.18-EZK.10.19]] ↔ kehrt zurück [[EZK.43.1-EZK.43.5]]; Datierungen | Thronwagen `space` [[EZK.1]]; Verantwortung [[EZK.18]]; Hirten `reversal` [[EZK.34]]; Totengebeine [[EZK.37.1-EZK.37.14]]; Tempelvision [[EZK.40-EZK.48]] |
| Dan (`DAN`) | Kreuzgliederung Sprache ↔ Gattung, Scharnier Kap. 7; aramäischer Teil konzentrisch (Vorschlag) | Hoferzählungen `matrix` [[DAN.2-DAN.6]]; Statue [[DAN.2.31-DAN.2.45]]; Reichsreihen `parallel` [[DAN.2]], [[DAN.7]], [[DAN.8]]; 70 Wochen [[DAN.9.24-DAN.9.27]] ([[DAN.4.1-DAN.4.3]] = dt. 3,31–33) |
| Hos (`HOS`) | Ehe und Kinder 1–3, je Gericht → Heil; Spruchsammlung 4–14 mit Bildfeld | Kindernamen und Umkehrung [[HOS.1.4-HOS.1.9]], [[HOS.2.23]]; dreifaches «darum» [[HOS.2.2-HOS.2.23]]; Busse und Antwort [[HOS.6.1-HOS.6.6]]; Wende [[HOS.11.8-HOS.11.9]] |
| Joel (`JOL`) | Diptychon Klage ↔ Erhörung, Wende [[JOL.2.18]] `curve` | Antwort Punkt für Punkt [[JOL.2.19-JOL.2.27]]; «wer weiss» [[JOL.2.12-JOL.2.14]]; Geist auf alle [[JOL.2.28-JOL.2.32]] (dt. 3,1–5); Pflugscharen zu Schwertern [[JOL.3.10]] |
| Am (`AMO`) | Reihen mit Zuspitzung auf Israel; drei Hymnenstücke [[AMO.4.13]], [[AMO.5.8-AMO.5.9]], [[AMO.9.5-AMO.9.6]] | Völkersprüche [[AMO.1.3-AMO.2.16]]; Plagen mit Kehrvers [[AMO.4.6-AMO.4.12]]; konzentrische Klage (Vorschlag) [[AMO.5.1-AMO.5.17]]; Visionen mit Amazja [[AMO.7.10-AMO.7.17]] |
| Obd (`OBA`) | Gericht über Edom → Tag des HERRN über alle Völker; hoch ↔ tief `reversal` | acht Verbote [[OBA.1.12-OBA.1.14]]; Spiegelstrafe [[OBA.1.15]]; Landverteilung [[OBA.1.19-OBA.1.21]] |
| Jona (`JON`) | parallele Hälften `parallel`; Abstieg; offenes Ende | Abstieg [[JON.1.3-JON.2.6]]; Psalm `thanksgiving` [[JON.2.2-JON.2.9]] ([[JON.1.17]] = dt. 2,1); Schluss vom Kleineren [[JON.4.10-JON.4.11]] |
| Mi (`MIC`) | drei Durchgänge Gericht → Heil mit «Hört» `cycle` | Ortsnamen-Wortspiele [[MIC.1.10-MIC.1.15]]; derselbe Berg [[MIC.3.12]] ↔ [[MIC.4.1-MIC.4.5]]; Rechtsstreit [[MIC.6.1-MIC.6.8]]; «Wer ist ein Gott wie du?» [[MIC.7.18-MIC.7.20]] |
| Nah (`NAM`) | Hymnus → Wechselrede → Schlacht → Weheruf, auf Ninive zulaufend | Theophanie [[NAM.1.2-NAM.1.8]] (teilweise akrostichisch, umstritten); Wechselrede `interleave` [[NAM.1.9-NAM.2.2]]; Schlussfrage [[NAM.3.19]] |
| Hab (`HAB`) | Dialog → Weherufe → Psalm; Klage → Freude `curve` | Klagedialog [[HAB.1.2-HAB.2.5]]; fünf Weherufe `woe` [[HAB.2.6-HAB.2.20]]; Theophanie [[HAB.3.3-HAB.3.15]]; Trotzdem [[HAB.3.17-HAB.3.19]] |
| Zef (`ZEP`) | universal → Juda → Völker → Jerusalem → Heil; Rahmen Zorntag ↔ Festtag `frame` | Schöpfung rückwärts [[ZEP.1.2-ZEP.1.3]]; Tag des Zorns [[ZEP.1.14-ZEP.1.16]]; Völker im Kompass [[ZEP.2.4-ZEP.2.15]]; Jubel [[ZEP.3.14-ZEP.3.17]] |
| Hag (`HAG`) | vier datierte Worte `sequence` (`chronology`) | zwei Häuser [[HAG.1.4]]; Anfrage an die Priester `case_ruling` [[HAG.2.11-HAG.2.14]]; Siegelring als Umkehrung von [[JER.22.24]] [[HAG.2.23]] |
| Sach (`ZEC`) | 1–8 datiert mit Nachtgesichten, 9–14 zwei «Aussprüche», Formel «an jenem Tag» | Nachtgesichte (konzentrisch, Vorschlag) [[ZEC.1.7-ZEC.6.8]]; Leuchter [[ZEC.4.2-ZEC.4.3]]; Fastenfrage mit später Antwort [[ZEC.8.18-ZEC.8.19]]; Hirtenstäbe [[ZEC.11.4-ZEC.11.17]] ([[ZEC.1.18-ZEC.1.21]] = dt. 2,1–4) |
| Mal (`MAL`) | sechs Diskussionsworte `objection` als `matrix`; Schluss Mose und Elia [[MAL.4.4-MAL.4.6]] | Jakob ↔ Esau [[MAL.1.2-MAL.1.5]]; Lesart [[MAL.2.16]]; Zehnter `condition` [[MAL.3.8-MAL.3.12]]; Unterschied [[MAL.3.18]] ([[MAL.4.1-MAL.4.6]] = dt. 3,19–24) |
| Mt (`MAT`) | Erzählung ↔ Rede `interleave` mit fünf Redeschlüssen [[MAT.7.28]], [[MAT.11.1]], [[MAT.13.53]], [[MAT.19.1]], [[MAT.26.1]]; Rahmen Immanuel | Stammbaum 3 × 14 [[MAT.1.1-MAT.1.17]]; Bergpredigt `frame` [[MAT.5.17]] ↔ [[MAT.7.12]]; Erfüllungszitate; Stufenverfahren [[MAT.18.15-MAT.18.17]] |
| Mk (`MRK`) | `route` Galiläa → Weg → Jerusalem, Wende [[MRK.8.27-MRK.8.30]]; Rahmen «Sohn Gottes» | Schachtelungen [[MRK.5.21-MRK.5.43]]; Wegabschnitt 3 × 3 [[MRK.8.22-MRK.10.52]]; Streitgespräche → Beschluss [[MRK.2.1-MRK.3.6]]; offenes Ende [[MRK.16.8]] |
| Lk (`LUK`) | `route` nach Jerusalem; Rahmen Tempel; Doppelwerk mit Apg | Kindheit als Diptychon [[LUK.1.5-LUK.2.52]]; Feldrede [[LUK.6.20-LUK.6.26]]; drei Verlorene [[LUK.15]]; Instanzenweg [[LUK.23.1-LUK.23.25]] |
| Joh (`JHN`) | Zeichen / Erhöhung; Festkalender; Zweck [[JHN.20.30-JHN.20.31]]; Nachtrag Kap. 21 | Prolog [[JHN.1.1-JHN.1.18]]; Missverständnis [[JHN.3.3-JHN.3.5]]; gegenläufige Treppe [[JHN.9]]; Bühne drinnen ↔ draussen [[JHN.18.28-JHN.19.16]] |
| Apg (`ACT`) | `outward` nach [[ACT.1.8]]; Wachstumsnotizen [[ACT.6.7]], [[ACT.9.31]], [[ACT.12.24]]; offenes Ende [[ACT.28.31]] | Pfingstrede `argument` [[ACT.2.14-ACT.2.36]]; Wiedererzählung [[ACT.9.1-ACT.9.19]]; Weiche auf der Karte [[ACT.16.6-ACT.16.10]]; Instanzenweg [[ACT.21-ACT.26]] |
| Röm (`ROM`) | `letter` mit These [[ROM.1.16-ROM.1.17]]; Lehrteil → Paränese, Scharnier [[ROM.12.1]] | Einwand und Antwort [[ROM.6.1-ROM.6.2]]; Adam – Christus [[ROM.5.12-ROM.5.21]]; Kette [[ROM.8.29-ROM.8.30]]; Rückwärtskette [[ROM.10.14-ROM.10.15]] |
| 1 Kor (`1CO`) | Antwortkatalog nach «Was aber … betrifft» [[1CO.7.1]], [[1CO.8.1]], [[1CO.12.1]], [[1CO.16.1]] | Parolen [[1CO.6.12-1CO.6.13]]; Autoritätsebenen [[1CO.7.10-1CO.7.12]]; Gaben – Liebe – Gaben [[1CO.12-1CO.14]]; Kettenschluss mit Wende [[1CO.15.13-1CO.15.20]] |
| 2 Kor (`2CO`) | Apologie in drei Blöcken; Reiserahmen [[2CO.2.12-2CO.2.13]] ↔ [[2CO.7.5-2CO.7.7]]; Einheit umstritten | alter ↔ neuer Bund [[2CO.3.6-2CO.3.18]]; «aber nicht» [[2CO.4.8-2CO.4.9]]; Narrenrede (`stance`) [[2CO.11.1-2CO.12.13]] |
| Gal (`GAL`) | Lebenslauf → Beweisgang → Ermahnung; Briefformular ohne Dank [[GAL.1.6-GAL.1.9]] | Lebenslauf als Argument [[GAL.1.13-GAL.2.14]]; Hagar – Sara [[GAL.4.21-GAL.4.31]]; Werke ↔ Frucht [[GAL.5.19-GAL.5.23]] |
| Eph (`EPH`) | Zuspruch (1–3) → Anspruch (4–6), Scharnier [[EPH.4.1]]; Leitwort «wandeln» | Eulogie mit Kehrvers [[EPH.1.3-EPH.1.14]]; einst ↔ jetzt [[EPH.2.1-EPH.2.22]]; Haustafel [[EPH.5.21-EPH.6.9]]; Waffenrüstung [[EPH.6.13-EPH.6.17]] |
| Phil (`PHP`) | Freundschaftsbrief mit Vorbildreihe; Leitwort Freude | Abwägung [[PHP.1.21-PHP.1.26]]; Christushymnus als V [[PHP.2.6-PHP.2.11]]; Bilanz [[PHP.3.4-PHP.3.8]]; Tugendreihe [[PHP.4.8]] |
| Kol (`COL`) | Hymnus → Polemik → Anspruch, Scharnier [[COL.3.1]] | Hymnus in zwei Strophen [[COL.1.15-COL.1.20]]; Schatten ↔ Körper [[COL.2.16-COL.2.17]]; ablegen ↔ anziehen [[COL.3.5-COL.3.14]]; Haustafel [[COL.3.18-COL.4.1]] |
| 1 Thess (`1TH`) | Danksagung (Rückblick) → Paränese; Triade [[1TH.1.3]] ↔ [[1TH.5.8]] | Bekehrung in drei Gliedern [[1TH.1.9-1TH.1.10]]; Ablauf «zuerst – danach» [[1TH.4.13-1TH.4.18]]; Tag ↔ Nacht [[1TH.5.1-1TH.5.11]] |
| 2 Thess (`2TH`) | Korrekturbrief zur Endzeitfrage | Vergeltung in zwei Richtungen [[2TH.1.6-2TH.1.10]]; «noch nicht» [[2TH.2.1-2TH.2.12]]; Arbeit [[2TH.3.6-2TH.3.12]]; eigenhändiger Gruss [[2TH.3.17]] |
| 1 Tim (`1TI`) | Mandatsbrief ohne Dank; Ordnung ↔ Abgrenzung `interleave` | Amtsspiegel [[1TI.3.1-1TI.3.13]]; Hymnus Erde ↔ Himmel [[1TI.3.16]]; Witwenregel [[1TI.5.3-1TI.5.16]]; Treuesprüche [[1TI.1.15]], [[1TI.3.1]], [[1TI.4.9]] |
| 2 Tim (`2TI`) | Abschiedsrede `testament` im Briefformular | Weitergabekette [[2TI.2.2]]; Treuespruch mit Bruch [[2TI.2.11-2TI.2.13]]; Schrift: Herkunft – Nutzen – Zweck [[2TI.3.14-2TI.3.17]]; Personennotizen [[2TI.4.9-2TI.4.21]] |
| Tit (`TIT`) | Mandatsbrief; zweimal Pflichten → «denn» Gnade (`cause`) | Ältestenspiegel [[TIT.1.6-TIT.1.9]]; Gruppentafel [[TIT.2.1-TIT.2.10]]; zwei Erscheinungen [[TIT.2.11-TIT.2.14]]; einst ↔ als aber [[TIT.3.3-TIT.3.7]] |
| Phlm (`PHM`) | Briefformular in Kleinstform; Leitwörter Herz, erquicken | Bitte statt Befehl [[PHM.1.8-PHM.1.9]]; Wortspiel [[PHM.1.11]]; Beziehungsdreieck (`network`) [[PHM.1.17-PHM.1.19]]; offener Schluss [[PHM.1.21]] |
| Hebr (`HEB`) | Lehre ↔ Mahnung `interleave`; Vergleichsreihe «besser» `balance` | damals ↔ jetzt [[HEB.1.1-HEB.1.2]]; Zitatenkette [[HEB.1.5-HEB.1.13]]; wie viel mehr [[HEB.9.13-HEB.9.14]]; Glaubenszeugen [[HEB.11]]; Sinai ↔ Zion [[HEB.12.18-HEB.12.24]] |
| Jak (`JAS`) | Stichwortkette und Themenreihe `collection`; Rahmen Geduld (Vorschlag) | zwei Ketten [[JAS.1.14-JAS.1.18]]; Glaube und Werke `objection` [[JAS.2.14-JAS.2.26]]; Zungen-Bilder [[JAS.3.3-JAS.3.12]]; zwei Weisheiten [[JAS.3.13-JAS.3.18]] |
| 1 Petr (`1PE`) | Zuspruch → Ermahnung; Leitformel Leiden → Herrlichkeit [[1PE.1.11]], [[1PE.4.13]], [[1PE.5.1]] | Steinbau [[1PE.2.4-1PE.2.8]]; Haustafel [[1PE.2.13-1PE.3.7]]; Christusbogen [[1PE.3.18-1PE.3.22]]; Noah – Taufe [[1PE.3.20-1PE.3.21]] |
| 2 Petr (`2PE`) | Testament: Leiter → Zeugnis → Warnung → Antwort an Spötter | Tugendleiter [[2PE.1.5-2PE.1.7]]; Gericht und Bewahrung [[2PE.2.4-2PE.2.10]]; Antwort an Spötter [[2PE.3.3-2PE.3.10]]; Parallele zu Judas |
| 1 Joh (`1JN`) | Themenspirale `cycle`; Dualismen `contrast`; Zweck [[1JN.5.13]] | «Wenn wir sagen» [[1JN.1.6-1JN.2.2]]; Prüfsteine [[1JN.2.3-1JN.2.11]]; Liebeskette [[1JN.4.7-1JN.4.21]]; Spannung [[1JN.1.8]] ↔ [[1JN.3.9]] |
| 2 Joh (`2JN`) | Briefformular; Rahmen [[2JN.1.1]] ↔ [[2JN.1.13]]; Leitwort Wahrheit | Liebe und Gebote [[2JN.1.4-2JN.1.6]]; Abweisung mit Bedingung [[2JN.1.7-2JN.1.11]] |
| 3 Joh (`3JN`) | Briefformular; Personenkonstellation (`network`) | Aufnahme ↔ Abweisung [[3JN.1.5-3JN.1.10]]; Merksatz [[3JN.1.11]]; Empfehlung [[3JN.1.12]] |
| Jud (`JUD`) | Beispiel → «diese» `argument`; Triaden | Gerichtsbeispiele [[JUD.1.5-JUD.1.7]]; Bildreihe [[JUD.1.12-JUD.1.13]]; vier Mahnungen [[JUD.1.20-JUD.1.21]]; Rahmen «bewahren» [[JUD.1.1]], [[JUD.1.21]], [[JUD.1.24]] |
| Offb (`REV`) | Visionsbericht mit verschränkten Siebenerreihen `vision`; zwei Bühnen `realms`; Briefrahmen | Sendschreiben `matrix` [[REV.2-REV.3]]; Siegel, Posaunen, Schalen [[REV.6-REV.16]]; Babylon ↔ Neues Jerusalem [[REV.17.1]] ↔ [[REV.21.9]]; Fernbezüge [[REV.2.7]] → [[REV.22.2]] |

## 5. Fallstricke quer durch die Bibel

**Glieder verlieren**
- Heilsteile weglassen, weil ein Buch nach Gericht klingt (Hosea, Amos [[AMO.9.11-AMO.9.15]], Zefanja, Lev 26, Dtn 30).
- Reihen kürzen: sechs Wehe, acht Glieder der Tugendleiter, 14 Paare in Pred 3, alle Völker, alle Zeichennamen.
- Listen streichen, obwohl sie Hauptteil sind (Jos 13–21; 1 Chr 1–9; Neh 3).
- Einschübe weglassen ([[REV.7]]; [[AMO.7.10-AMO.7.17]]); Begründungen weglassen (Tit 2; Haustafeln).

**Stimmen und Richtung**
- Sprecher verlieren: Hiobs Freunde, Einwände (Röm), Parolen (1 Kor), Ironie (2 Kor 11), Kreter-Zitat [[TIT.1.12]], Rahmenerzähler (Pred).
- Richtung vertauschen: Gabe ↔ Bedingung (Dtn 7–9), wer freut sich über wen ([[ZEP.3.14]] ↔ [[ZEP.3.17]]), Antworten der Priester
  ([[HAG.2.11-HAG.2.14]]).
- Gott als Handelnden abschwächen ([[LAM.2.1-LAM.2.8]]).

**Offenheit erhalten**
- Offene Enden schliessen (Jona, Nahum, [[MRK.16.8]], Apg 28, Klgl 5, Phlm 21).
- «Vielleicht» und «wer weiss» zur Zusage machen; Erfahrungssätze als Garantie ([[PRO.22.6]]); [[MAL.3.10]] als allgemeines Versprechen.
- Spannungen glätten: vollständige ↔ unvollständige Landnahme; doppelte Einführung Davids ([[1SA.16.14-1SA.16.23]] ↔ [[1SA.17.55-1SA.17.58]]);
  [[PRO.26.4-PRO.26.5]]; [[1JN.1.8]] ↔ [[1JN.3.9]]; Verstockung durch Pharao und durch Gott.

**Fassungen und Text**
- Parallelfassungen harmonisieren (Ri 4/5; Sam/Chr; Dekalog; Kindheitsgeschichten Mt/Lk; Lk 24/Apg 1).
- Textkritik übergehen: [[MRK.16.9-MRK.16.20]]; [[JHN.7.53-JHN.8.11]]; [[1JN.5.7-1JN.5.8]]; [[LUK.22.43-LUK.22.44]]; [[MAT.23.14]]; Jer MT ↔ LXX;
  Est ohne Gottesnamen im hebräischen Text; Zusätze zu Daniel; Nun-Zeile in Ps 145.
- Verszählung: Psalmüberschriften als Vers 1; Lev 5–6; Num 17; [[DEU.29.1]]; 1 Kön 5; 1 Chr 6; [[NEH.4.1-NEH.4.23]] und Neh 10; [[SNG.6.13]]; Dan 3/4 und 5/6;
  Hos 2; 12; 14; Joel 3–4; Jona 2; Sach 2; [[MAL.4.1-MAL.4.6]]. Psalmen in LXX/Vulgata ab Ps 10 eins tiefer.

**Deutung und Text**
- Deutungen als Text ausgeben: Reichsfolgen in Dan 2/7, «Babylon = Rom», 666, Millenniumsmodelle, Gog, Satansfall in [[ISA.14.12]] und
  [[EZK.28.11-EZK.28.19]], messianische Lesarten ([[ISA.7.14]]; [[MIC.5.2]]; [[ZEC.9.9]]) in der Zusammenfassung.
- Forschungsvorschläge als Befund (Chiasmen, Dreiteilung Jesaja, Teilungshypothesen 2 Kor/Phil, Verfasserschaft).
- Rekonstruktionen ohne Kennzeichnung (Tempelmasse, Mauerverlauf Neh 3, Stationen Num 33, Reiseroute Lk).

**Ordnung**
- Buchordnung ≠ Zeitordnung: Jer (Jojakim nach Zidkija), [[EZK.29.17]], [[EZR.4.6-EZR.4.23]], Dan (Visionen springen zurück).
- Zählungen der Auslegung als Text («sieben Zeichen», «erste Missionsreise», «sieben Bitten»).

## 6. Folgerungen für Datenmodell und Prüfung (Vorschlag)

**Feld `structure` in der Kernanalyse**

```json
"structure": {
  "root": "s1",
  "units": [
    {
      "id": "s1",
      "pattern": "frame",
      "subtype": "inclusio",
      "form_type": null,
      "range": "MAT.5.3-MAT.5.12",
      "elements": [
        {"label": "Arme im Geist → Himmelreich", "ref": "MAT.5.3", "role": "A", "links": ["MAT.5.10"]},
        {"label": "Reihe der Seligpreisungen", "child": "s2"}
      ],
      "features": {
        "speakers": [{"who": "Jesus", "to": "Jünger und Volk"}],
        "crossref": [{"ref": "LUK.6.20-LUK.6.26", "kind": "Parallelfassung"}]
      },
      "visual": "grid",
      "basis": "text"
    }
  ]
}
```

- `pattern` aus der Liste der 33; `subtype` und `form_type` aus kontrollierten Listen (Abschnitt 3).
- `elements` mit `label`, `ref`, `role` (z. B. Bedingung/Folge, A/A', Zeile/Spalte), `links` (Gegenpaar, Pfeil, Erfüllung), `child` für
  Verschachtelung; bei `matrix` `row` und `col`, leere Zellen ausdrücklich als `empty`.
- `features` als Objekt mit den 15 Schlüsseln aus 2b.
- `basis`: `text` (vom Text gesichert) oder `proposal` (Forschungsvorschlag, mit Quelle). Ein Muster mit `proposal` darf im Bild
  erscheinen, aber nur als Deutung gekennzeichnet (Entscheid 3).
- Marken immer in Navigationszählung (KJV); die deutsche Zählung erscheint nur in der Anzeige (Umrechnung `scripts/versification.py`, TVTMS).

**Prüfung «Strukturtreue» (Erweiterung)**
1. Pflichtglieder je Muster bzw. `form_type` vorhanden oder als `pattern_break` vermerkt.
2. Zahl der Glieder gegen die Zahl im Text (`series`, `numbered`, Reihen in `form`).
3. Leere Zellen in `matrix` leer, nicht aufgefüllt.
4. Pflichtmerkmale: `speakers` bei `dialogue`, `objection`, Briefen und Reden; `modality` bei Prophetie und Gebet; `text_forms`, wenn
   für das Buch bekannt.
5. Zuordnung `pattern` → zulässige `visual` gemäss Tabelle 2c; Abweichung begründen.
6. `basis: proposal` nie ohne Kennzeichnung in Zusammenfassung oder Bild.
7. Zusammenfassung enthält die Verbindungswörter des Musters (denn, darum, wenn – dann, nicht – sondern, wie viel mehr).

**Ergänzungen in VERDICHTUNG.md**
- Tabelle der 16 Baumuster durch Verweis auf diesen Katalog ersetzen (Kurzliste der 33 behalten).
- Regeln der Strukturtreue ergänzen: (6) Stimmen trennen; (7) Offenheit erhalten (offene Enden, «vielleicht», Spannungen);
  (8) Parallelfassungen nicht harmonisieren; (9) Text, Deutung und Forschungsvorschlag trennen; (10) Verzeichnisse nach Gliederung und
  Summe verdichten, Reihen nach allen Gliedern.
- Umfang je Ebene: vollständige Reihen mit mehr als 8 Gliedern erlaubt (Entscheid 2, umgesetzt).

## 7. Entscheide (2026-10-24, Andi Neck)

1. **Gattungsformen:** ein Muster `form` mit Untertypen (`form_type`) und Pflichtgliedern, wie in 3.22 vorgeschlagen.
2. **Lange Reihen:** Ausnahme von der Grenze «Raster bis 8 Felder»: Tragende Reihen bleiben vollständig, das Bild gruppiert oder
   verkleinert, damit keine wichtige Information verloren geht ([VERDICHTUNG.md](VERDICHTUNG.md), Regel 6).
3. **Forschungsgliederungen:** dürfen auch im Bild erscheinen, als Deutung gekennzeichnet (`basis: proposal`; Regel 7).
4. **Textfassung:** Verdichtet wird die Grundlage der Arbeitsübersetzung; andere Fassungen als Hinweis (`text_forms`) in
   Zusammenfassung und Kernanalyse, nicht im Bild. Mehrere Fassungen im Bild verwirren; sie gehören ins vertiefte Studium auf
   Versebene (Regel 8).

## Anhang: Verbleib aller Vorschläge der Analysen

`a_fortiori` → `balance`; `acrostic` → `poem`; `allotment` → `territory`; `alternation` → `interleave`; `announce` → `fulfilment`;
`antithetic-series` → `contrast`; `arc` → `reversal`; `arcs` → `fulfilment`; `argument` → `argument`; `balance` → `balance`;
`calendar` → `cycle`; `catchword` → `collection`; `catena` → `argument`; `collection` → `collection`; `counter` → `reversal`;
`cross_outline` → `collection`; `crossing` → `reversal`; `dated_frame` → Merkmal `chronology`; `dated_oracles` → Merkmal `chronology`;
`decline` → `climax`; `deliberation` → `balance`; `descent-ascent` → `reversal`; `despite` → `contrast`; `diatribe` → `objection`;
`diptych` → `parallel` bzw. `contrast`; `disputation` → `objection`; `dual_timeline` → Merkmal `chronology`; `elevation` → `reversal`;
`embedded_document` → Merkmal `speakers`; `etiology` → `cause`; `exemplum` → `series`; `expansion` → `outward`; `fable` → `parable`;
`formula` (Formular) → `matrix` bzw. `form` `regnal`; `formula` (Gliederungsformel) → Merkmal `leitwort`; `fulfilment`, `fulfillment` →
`fulfilment`; `funnel` → `tree`; `generations` → `condition` in `tree`; `genre` → Merkmal `genre`; `growing_formula` → `climax`;
`hear_see` → `vision`; `heading_formula` → Merkmal `leitwort`; `household` → `form` `household`; `indicative-imperative` → `cause`;
`insertion` → Merkmal `pattern_break`; `instruction_execution` → `parallel`; `interleave` → `interleave`; `intertext_net` → Merkmal
`crossref`; `judgment_salvation` → `curve` bzw. `cycle`; `keyword`, `keyword_trace`, `leitwort` → Merkmal `leitwort`; `ladder` → `poem`;
`lament_dialogue` → `dialogue`; `law` → `condition` bzw. `form` `case_ruling`; `lawsuit` → `form` `lawsuit`; `layers` → Merkmal
`interpretation`; `letter` → `form` `letter`; `levels` → `realms`; `liturgy` → `form` `liturgy`; `map_series` → `series`; `matrix`
(Schema-Raster, Sendschreiben) → `matrix`; `matrix` (Bedingungsraster) → `condition`; `metaphor`, `metaphor_board` → `parable`;
`midrash` → `argument`; `mirror` → `reversal`; `mirror_scene` → `parallel`; `misunderstanding` → `dialogue`; `mood`, `mood_curve` →
`curve`; `motif` → Merkmal `leitwort`; `movement` → `route`; `narrator_comment` → `cause` mit Merkmal `speakers`; `nations_ring` →
`series`; `nest` → `frame`; `network` → Darstellung `network`; `number_key` → Merkmal `numbers`; `numeric_saying`, `numerical_saying` →
`numbered`; `oath` → `condition`; `objection` → `objection`; `open_condition` → `condition` mit Merkmal `modality`; `open_end`,
`open_ending` → Merkmal `open_end`; `open_timeline` → Merkmal `chronology`; `organigram` → `tree`; `outward` → `outward`;
`parallel_halves`, `parallel_scenes`, `parallel_version` → `parallel`; `parody` → `contrast`; `pendulum` → `interleave`;
`procedure` → `form` `lawsuit`; `questions` → `series`; `ranked_figure` → `space`; `rating` → `matrix`; `recapitulation` → `matrix`;
`refrain_series` → `series`; `register` → `register`; `relations` → `form` `household`; `retelling` → `parallel`; `reversal` →
`reversal`; `rings` → `outward`; `rounds` → `dialogue`; `sayings` → `collection`; `scale` → `climax`; `scheme_grid` → `matrix`;
`sign_act`, `symbolic_act` → `sign_act`; `slogan` → `objection`; `sorites` → `argument`; `spiral` → `cycle`; `stage` → `space`;
`stages` → `condition`; `synchronism` → Merkmal `chronology`; `synchrony` → `interleave`; `synkrisis` → `balance`; `synopsis` →
`parallel`; `tactical_sketch` → `route`; `talion` → `cause`; `telescope` → `series`; `template_repeat` → `matrix`; `territory` →
`territory`; `tests` → `series`; `text_forms` → Merkmal `text_forms`; `thematic_order` → Merkmal `chronology`; `theophany` → `form`
`theophany`; `thread` → `fulfilment`; `tora_inquiry` → `form` `case_ruling`; `tour` → `route`; `tradition` → `tree`; `treaty` → `form`
`treaty`; `trial` → `form` `lawsuit`; `triad` → `series`; `triad-rule` → `cause`; `triptych` → `collection`; `turn` → `curve`;
`two_phase` → `curve`; `two_realms`, `two_stages` → `realms`; `typology` → `typology`; `vision_dialogue`, `vision_qa`, `vision_ring` →
`vision`; `voices` → Merkmal `speakers`; `wasf` → `poem`; `wordplay` → Merkmal `wordplay`; `zones` → `space`.
Ohne Code vorgeschlagen: «Weg im Grundriss», «Lagerplan» → Darstellung `model`; «Kreise von innen nach aussen» → `rings` (`outward`);
«Organigramm» → `tree`; «Haupt- und Nebenlinie», «Genealogie mit Erzählsplittern» → `tree`; «nicht … sondern» → `contrast`;
«3 + 1», «Musterbruch» → Merkmal `pattern_break`; «Zeitraster mit zwei Massstäben», «Zeitstrahl mit «noch nicht»» → `timeline`;
«Autoritätsebene» → `authority`; «Sprecherhaltung (Ironie, Narrenrede)» → `stance`; «Leitwort», «Antwortkatalog (περὶ δέ)» → `leitwort`;
«Korrespondenz-Zeitleiste» → `chronology`; «Personennetz / Beziehungsdreieck» → `network`; «Bilanz (Gewinn ↔ Verlust)» → `balance`;
«Figur-Skizze mit Bild ↔ Sache je Teil» → `figure`; «Urbild ↔ Schatten» → `typology`.
