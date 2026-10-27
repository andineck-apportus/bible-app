# Bildaufträge schreiben (für alle Stellen eines Buches)

Seit v0.65 entstehen die Bilder der übersetzten Bücher nicht mehr einzeln von Hand, sondern werden vom Zeichner
(`scripts/authoring/bilder_auto.py`) in beiden Stilen (Symbol, Anime) direkt aus dem Bildauftrag gesetzt. Wer einen Bildauftrag
schreibt, legt also fest, **was** zu sehen ist; das **Wie** übernimmt der Zeichner, gesteuert über wenige Hinweise (`stage`).
Grundsätze der Bildsprache: [BILDSPRACHE.md](BILDSPRACHE.md). Vorbild: `scripts/authoring/bildauftraege_daten/JON.json`.

## Dateien je Buch

| Datei | Inhalt |
|---|---|
| `scripts/authoring/bildauftraege_daten/<BUCH>.json` | Liste der Bildaufträge (Buch, Kapitel, Abschnitte) |
| `scripts/authoring/bildlexikon_daten/<BUCH>.json` | neue Lexikon-Einträge (Personen, Gegenstände, Orte, Zeichen) |
| `scripts/authoring/bildsymbole_daten/<BUCH>.json` | Zeichnungen (SVG) für neue Gegenstände, Orte und Zeichen |
| `scripts/authoring/figuren_daten/<BUCH>.json` | Aussehen neuer Personen und Rollen (Farben, Haar, Bart, Kopfbedeckung, Attribut) |

Danach in dieser Reihenfolge ausführen: `bildlexikon.py`, `bildauftraege.py`, `bilder_symbol.py`, `bilder_anime.py`
(alle in `scripts/authoring/`), dann `scripts/validate.py`.

## Ebenen und Ziele

- **Buch** (`level: book`, `reference: "RUT"`, `target: "SUM-BOOK-RUT"`, `translation: null`): 2–4 Felder mit den Hauptstationen.
- **Kapitel** (`level: chapter`, `reference: "RUT.1"`, `target: "SUM-CH-RUT-001"`, falls vorhanden, sonst die Kapitel-Einheit `TU-…`; `translation: null`):
  je Abschnitt des Kapitels ein Feld, höchstens 4 (bei mehr Abschnitten die wichtigsten zusammenfassen).
- **Abschnitt** (`level: section`, `reference` und `target` des Abschnitts `TU-…`, `translation` = hochdeutsche Arbeitsübersetzung des Kapitels):
  1–4 Felder in der Reihenfolge des Textes; jedes Feld nennt seinen Versbereich.
- **Merkvers** (`level: verse`, `reference` = ein Vers, `target` = Abschnitt `TU-…`, `translation` wie beim Abschnitt): ein Feld, wenige starke Zeichen zum Einprägen; `note_de` sagt, warum der Vers ein Merkvers ist. Suffix `MAT-005-003`. Die App zeigt die Karte beim Vers mit dem Verswortlaut der gewählten Fassung.
- `suffix`: wie die Ziel-ID ohne `TU-`/`SUM-CH-`/`SUM-BOOK-` (z. B. `RUT-001-001-005`, `RUT-001`, `RUT`).

## Ein Feld

```json
{"n": 1, "reference": "JON.1.1-JON.1.2",
 "figures": ["FIG-GOTT", "FIG-JONA"],          // Personen in der Reihenfolge links → rechts; Gott/Geist kommen nach oben
 "objects": ["FIG-ORT-NINIVE"],                // Orte und Gegenstände
 "signs": ["FIG-ZEICHEN-FREUDE"],              // Zeichen
 "speech": [{"from": "FIG-GOTT", "to": "FIG-JONA", "icons": ["FIG-ORT-NINIVE", "FIG-ZEICHEN-VERKUENDIGEN"]}],
 "action_de": "…", "action_gsw": "…",          // Handlung nach dem Text, ein bis zwei Sätze
 "caption_de": "Kurztitel: was man sieht (Zeichen erklärt).", "caption_gsw": "…",
 "stage": {…}}                                  // Hinweise an den Zeichner (optional)
```

Prüfen wie eine Zusammenfassung: Handelnde, wer zu wem, Zeitform, Ankündigung statt Bericht; nichts zeigen, was der Text nicht
sagt (oder es in `note_de` als Deutung benennen). Sprechblasen ohne Worte nur mit Zeichen (höchstens 6); in neuen Aufträgen ein Kernwort und höchstens zwei Zeichen (siehe «Worte im Bild»).
Mehrzahl («ihr», «die Leute») als Gruppe (`FIG-GRUPPE-…`), nie als Einzelfigur. Gewalt und starke Gefühle erkennbar zeigen, nicht ausmalen (docs/BILDSPRACHE.md, Regel vom
2026-10-23: Gefühl im Gesicht, Handlung über Bewegung und Folge, Tod als liegende Figur, Jesus am Kreuz ohne Wunden im Detail). «Die Juden», Pharisäer, Hohepriester als neutrale Figuren, nie verzerrt.

## Worte im Bild (ab 2026-10-23, Pilot Rut, Titus, Mk 5, Mt 5–7)

Entscheid Andi Neck 2026-10-23 (BILDPROZESS.md): wenige Worte im Bild, aus dem Wortlaut der jeweiligen Übersetzung. Ein Bild gilt für
alle Übersetzungen; jedes Wort steht je Sprache im Auftrag, die App zeigt die gewählte Textsprache.

```json
{"n": 1, "reference": "RUT.4.9-RUT.4.11", …,
 "keywords": {"de": "Wir sind Zeugen!", "gsw": "Mir sind Züüge!"},     // Stichwortband: wenige Wörter (höchstens etwa 6), wörtlich, für sich verständlich
 "names": {"FIG-BOAS": {"de": "Boas", "gsw": "Boas"}},                 // Namensschild: Hauptfiguren beim ersten Auftreten im Bild
 "speech": [{"from": "FIG-BOAS", "to": "FIG-GRUPPE-AELTESTE", "word": {"de": "Zeugen", "gsw": "Züüge"},
             "icons": ["FIG-ORT-FELD"]}],                               // Kernwort + höchstens zwei Zeichen
 "letter": true}                                                        // nur bei Aufträgen im Brief: Briefrand und Brief im Band
```

- **Ein Feld je tragendem Moment** der Kernanalyse (`data/core-analyses/CORE-…json`, `moments`); die Stichwörter nach deren
  `keywords`. Das hochdeutsche Stichwort muss so im Text des Felds stehen (der Validator warnt sonst; Satzzeichen und
  Grossschreibung zählen nicht), das züridüütsche aus der Mundartfassung desselben Verses.
- **Bildtyp nach Textart** (`mode` der Kernanalyse): Erzählung als Szene; Rede, Lehre, Gleichnis mit dem Redner klein am Rand
  und dem Inhalt gross; Auftrag im Brief mit `letter: true` und Absender/Empfänger als Figuren (Paulus links, Titus rechts) –
  das Verlangte als Zeichen in der Sprechblase, nicht als geschehene Szene; Aufzählung als wenige Zeichen nebeneinander.
- **Namensschild** nur beim ersten Auftreten einer benannten Hauptfigur im Bild (nicht bei Gott, Jesus, Gruppen und Rollen); seit
  2026-10-26 auch, wo sonst ein nicht gestütztes Erkennungszeichen die Figur unterscheiden müsste. Der Zeichner setzt es auf die
  Brust, wenn die Figur dort nichts trägt, sonst neben oder über den Kopf (nie über Gesicht, Gehaltenes, Zeichen, Blasen).
- Höchstens zwei abstrakte Zeichen je Feld; Wörter statt Zeichenketten.
- **Thema benennen** (Hinweis Andi Neck 2026-10-24): Band oder Sprechblase nennen das Thema der Stelle mit Worten aus dem Text
  (z. B. «Wenn ihr fastet», nicht nur «Wasche dein Gesicht»). Zeichen, die man ohne Legende nicht versteht, ersetzt ein Wort
  oder die Szene.
- **Nichts verdecken:** Blasen und Pfeile über Gesichtern, Zeichen oder Gegenständen sind ein Fehler (der Zeichner weicht aus;
  bleibt es, Bühne mit `stage.x` oder weniger Zeichen lösen). Gedanken als Denkblase (`think: true`), nicht als Rede.
- **Verständlich und grammatisch richtig** (Hinweis Andi Neck 2026-10-23): Jedes Band und jede Sprechblase muss für sich
  allein verständlich und in der jeweiligen Sprache grammatisch richtig sein, auch ohne den Vers daneben. Gemeint ist ein
  kurzer ganzer Satz oder ein klarer Begriff, keine abgehackten Satzteile (schlecht: «hört und sie tut», «nicht tut»,
  «weit über», «weise … ab»).
  - Das Stichwortband bleibt wörtlich, aber als sinnvolle Einheit gewählt, höchstens etwa 6 Wörter, z. B. «Wer meine Worte
    hört und tut».
  - Die Sprechblase darf die Aussage des Sprechers nah am Text knapp in eigenen Worten fassen, wenn kein wörtlicher Ausschnitt
    für sich steht. Sie darf nichts behaupten, was der Text nicht sagt.
- **Darstellung durch den Zeichner** (Hinweise Andi Neck 2026-10-23):
  - Längere Worte brechen auf zwei Zeilen um, statt kleiner zu werden; das Band wird dann höher.
  - Die Sprechblase steht nahe über ihrem Sprecher; die Spitze zeigt auf ihn, nicht quer durchs Bild.
  - Freie Zeichen weichen den Sprechblasen aus und stehen nie darüber.
  - Beim Prüfen der Bilder gehört dazu: Spitze am richtigen Sprecher? Kein Zeichen über einer Blase? Schrift gut lesbar?
- **Mundart:** Die Worte stammen aus der Mundartfassung, müssen dort aber idiomatisch richtig sein. Zum Beispiel tönt
  «zur Frau erworbe» nach «gchauft»; besser ist «zur Frau gnoo». Ist die Mundartfassung selbst holprig, wird sie mit
  Entscheid und revision_log verbessert (Werkzeug des Buches) und das Wort danach übernommen.
- **Prüfung:** Nach dem Zeichnen listet `python3 scripts/authoring/bildworte.py <Präfix>` alle Worte im Bild je Sprache auf.
  Eine getrennte KI-Instanz prüft sie auf Verständlichkeit für sich allein, Grammatik und Mundart. Gleiches gilt für
  Zusammenfassungen (AGENTS.md). Befunde werden behoben, bevor das Bild veröffentlicht wird; muttersprachliche Prüfung nicht
  behaupten.

## Hinweise an den Zeichner (`stage`)

| Schlüssel | Wirkung |
|---|---|
| `mood: {FIG: expr}` | Ausdruck im Stil Anime: calm, smile, delight, worried, surprised, earnest, determined, pensive, question (fragend), sleep, angry (Zorn), fear (Angst), pain (Schmerz), dead (tot, fahle Haut) |
| `pose: {FIG: p}` | lie, sleep, sit, kneel, fall, away (abgewandt: gespiegelt, Blick zur Seite, Gesicht bleibt sichtbar wie in der Legende) |
| `hold: {FIG: OBJ}` | Figur hält Gegenstand (Gegenstand muss in `objects` stehen); lange Gegenstände (Schwert, Rohr, Kreuz) stehen seitlich mit sichtbarer Hand; `"LEER"` = leere Hände ohne das feste Erkennungszeichen der Figur und ohne Stab (z. B. die Frau aus Samarien, nachdem sie den Krug stehen gelassen hat, [[JHN.4.28]]; Erkennungszeichen, die der Text der Stelle nicht stützt, siehe unten) |
| `in: {FIG: OBJ}`, `in_pos: {FIG: [x, y]}` | Figur im Gegenstand (Boot, Fisch, Grab …), Lage relativ 0–1 |
| `at: {ZEICHEN: FIG}` oder `{ZEICHEN: [FIG, …]}` | Zeichen bei einer oder mehreren Figuren (z. B. Zorn, Schlafen, Nebel); Krone und Dornenkrone sitzen auf dem Kopf |
| `signs_who: {ZEICHEN: [FIG…]}` | wer Tränen/Freude/Herz trägt (Standard: alle Personen ausser Jesus) |
| `count: {ID: n}` | Anzahl (z. B. drei Sonnen, fünf Brote; höchstens 7) |
| `split: n` | gestrichelte Linie (Abstand) nach der n-ten Person |
| `god_side`, `back_side`, `big_side`, `floor_side` | left/right (Gott: auch center) |
| `flip: [OBJ]` | grosser Gegenstand gespiegelt (z. B. Fisch schaut nach rechts) |
| `floor_x: {OBJ: x}`, `air_x`, `air_y`, `big_y`, `bubble_y` | Feinlage in Feldeinheiten (Feld 186 × 140, Boden bei 118) – sparsam |
| `x: {FIG: x}` | Lage einer Person (Mitte, Feldeinheiten); schaltet die automatische Leserichtung ab |
| `arrows: [[von, zu, art]]` | Handlungslinie: `act` (senden, sehen, heilen; von Gott golden), `throw` (werfen, speien), `go` (gehen, gestrichelt). Von und zu Personen setzt der Zeichner die Linie über die Köpfe bzw. auf Schulterhöhe |
| `beside: {ZEICHEN: FIG}` | Zeichen neben dem Kopf statt darüber (z. B. heilende Hand, Fragezeichen) |
| `behind: [OBJ]` | Gegenstand am Boden hinter den Personen |
| `before: true` | Personen stehen vor dem Gebäude im Hintergrund (Gebäude nicht ausweichen) |
| `wear: {FIG: sack \| binden \| #RRGGBB}` | Kleidung: Sacktuch, Leinenbinden oder andere Mantelfarbe |
| `in_water: true`, `sea: "calm"` | Personen stehen im Wasser (kein Uferstreifen); See ruhig statt bewegt |
| `at_top: true` | Zeichen bei einer Figur im Gegenstand oben statt seitlich |
| `on_water: [FIG]` | Figur geht auf dem Wasser (steht über den Wellen, z. B. Jesus); andere Figuren mit `in_water` stehen im Wasser |
| `on: {FIG: ORT}` | Figur steht auf einem Ort im Hintergrund (z. B. Jesus auf dem Berg) |
| `twin: {FIG: x}` | zweite gleiche Figur bei x (z. B. die zwei Mitgekreuzigten links und rechts von Jesus, [[JHN.19.18]]); sie spricht nicht und trägt Pose und Ausdruck der ersten (seit 2026-10-26) |
| `far: [FIG]` | Figur weiter hinten: etwas kleiner und höher (z. B. die Mitgekreuzigten neben Jesus am Kreuz) |
| `night: true` | dunkler Himmel mit Sternen (automatisch, wenn das Zeichen Nacht im Feld steht) |
| `wolke: true` | grosse Wolke oben im Feld, die den Strahlenkranz umhüllt; die Szene darunter liegt leicht im Schatten («eine Wolke überschattete sie, und eine Stimme kam aus der Wolke», [[LUK.9.34-LUK.9.35]], [[MAT.17.5]], [[MRK.9.7]]). Braucht `FIG-GOTT` in `figures` und `FIG-ORT-WOLKE` in `objects` (die kleine Wolke entfällt dann); der Strahlenkranz steht in der Mitte, die Blase Gottes kommt aus der Wolke (seit 2026-10-26) |
| Sprechblase `"think": true` | Denkblase (Wolke mit kleinen Kreisen) statt Sprechblase: «sagt sich im Herzen», überlegt |

Automatisch (seit dem Blindtest vom 2026-10-17): Wer zuerst spricht, steht links vom zweiten Sprecher (ausser `x`, `split` oder
«links/rechts» in der Legende); eine zweite Sprechblase derselben Figur steht neben der ersten oder darunter und ist mit ihr verbunden (seit 2026-10-26 hat jede
Sprech-Angabe ihre eigene Blase; vorher fasste der Zeichner sie zusammen und das Wort der zweiten fiel weg; Regeln für die Lage
in [BILDPROZESS.md](BILDPROZESS.md), «Sprechblasen: feste Prüfungen»);
Gruppen erscheinen als Menge (drei Figuren vorn, zwei dahinter). Die Legende (`caption_de`) muss beschreiben, was das Zeichen im
Bild tatsächlich zeigt (gleiche Wörter wie das Merkmal im Bildlexikon), sonst sucht man vergeblich.

**Erkennungszeichen nur, wo der Text sie stützt** (Entscheid Andi Neck 2026-10-26): Das Erkennungszeichen einer Figur aus dem
Lexikon (Schlüssel des Petrus, Kreuzstab des Täufers, Muschel und Kelch der Zebedäussöhne, Alabastergefäss der Maria aus Magdala,
Feuerwagen Elijas, Stab des Mose, aber auch Hammer des Josef, Kasse des Judas, Richterstuhl des Pilatus) steht nur in Feldern,
deren Verse es stützen (z. B. der Schlüssel in [[MAT.16.19]], die Kasse in [[JHN.12.6]]); sonst `stage.hold` `"LEER"`. Wer sich
dann nicht mehr unterscheiden lässt (gleich aussehende Jünger), bekommt ein Namensschild statt eines nicht gestützten Zeichens.
Die Legende nennt das Zeichen nur, wo es gezeichnet ist. Prüfhilfe: `python3 scripts/authoring/erkennungszeichen.py [--anwenden]`
listet je Feld Figur, Zeichen und ob ein Suchmuster im Versbereich es stützt; `--anwenden` setzt `"LEER"`, kürzt die Legende und
ergänzt ein Namensschild (Lauf vom 2026-10-26: `reports/erkennungszeichen-2026-10-26.json`, 336 gezeigte Zeichen, 255 nicht
gestützt).

Platzierung je Eintrag (in `bildsymbole_daten`: `place`): `band` (Hintergrund über die ganze Breite: Meer, See, Feld),
`back` (Gebäude im Hintergrund), `big` (gross in der Mitte: Schiff, Fisch, Grab), `floor` (am Boden), `hand` (klein, in der Hand),
`air` (frei oben), `head` (bei den Köpfen), `line` (zwischen Figuren).

## Abläufe sichtbar machen: Ursache → Wirkung (seit 2026-10-18)

Ein Bild soll zeigen, was woraus folgt, nicht nur, wer da ist. Für jedes Feld fragen: Was ist Ursache oder Bedingung, was Folge,
Verheissung oder Ziel? Typische Signale im Text: «denn», «weil», «damit», «so dass», «darum», «wenn … dann», «wer … der», Seligpreisungen
(«Selig sind …, denn …»), Gebote mit Begründung, Gleichnisse (Handlung → Ergebnis), Wunder (Bitte/Glaube → Heilung).

- Ursache links, Folge rechts (Leserichtung); dazwischen ein Pfeil `act` von der Ursache zur Folge (z. B. Arme → Krone «Reich der Himmel»).
- Was von Gott kommt, mit goldenem Pfeil vom Strahlenkranz zur Gabe bzw. zur Person (Gott gibt, tröstet, nennt).
- Reaktion auf Handlung: Pfeil von der Handelnden zur Antwortenden (gute Werke → Menschen → Gott preisen).
- Zeichen, die eine Folge darstellen, nicht frei schweben lassen, sondern als Ziel eines Pfeils oder bei der betroffenen Figur (`at`).
- Höchstens zwei bis drei Pfeile je Feld; eine klare Kette ist besser als viele Linien. Die Legende nennt die Kette in Pfeilform
  («Arme im Geist → Reich der Himmel: …»).
- Mehrschrittige Abläufe auf Felder verteilen (Feld 1 Ursache, Feld 2 Folge), wenn ein Feld zu voll würde.

Kurze Wege (nahe Personen) zeichnet der Zeichner als Winkel «>»/«<»; `beside` sucht die freie Seite, sonst über den Kopf; ein gehaltener Gegenstand (`hold`) kann Anfang oder Ziel eines Pfeils sein. Pfeile von Gott gehen direkt vom Rand des Strahlenkranzes zum Ziel (Bogen quer zur Verbindungslinie); Blasinstrumente
(`hold` Posaune) setzt der Zeichner an den Mund, den Trichter in Blickrichtung.

## Neue Lexikon-Einträge

Aufbau wie in `bildlexikon_daten/JON.json`: `id` (`FIG-…`, gleiche Namen für gleiche Dinge in allen Büchern, z. B. `FIG-ZEICHEN-LIEBE`),
`kind` (person, role, group, object, place, action, sign), Namen de/en, `ident`/`gsw` (ein Satz mit Stelle), `traits` mit `basis`
(`text` nur mit `ref`, sonst `tradition` oder `design`), Palette, Regeln, bei Personen und Rollen `era`, optional `find` (Suchmuster
für «kommt vor in»). Personen und Rollen brauchen ein Aussehen in `figuren_daten`, alles andere eine Zeichnung in `bildsymbole_daten`
(`{"FIG-…": {"sym": "ill-…", "vb": "0 0 w h", "svg": "…", "place": "floor", "size": [w, h]}}`, flache Formen, Strich `#3B3226`,
keine Schrift).

## Strukturbilder (`diagram`)

Seit 2026-10-24 («Struktur zuerst», [STRUKTURKATALOG.md](STRUKTURKATALOG.md)) kann ein Feld statt einer Bühne ein Strukturbild
tragen: `"diagram": {"visual": …}` mit einer der Darstellungen grid, columns, mirror, arrows, switch, outline, dialogue,
timeline, balance, stairs, levels, rings, tree. Aufbau und Felder stehen im Kopf von `scripts/authoring/bilder_diagramm.py`.

- Wahl nach der Struktur der Kernanalyse (`structure.units[].visual`); Erzählungen bleiben Szenen.
- Jede Zelle hat ihre Worte je Sprache (`{"de": …, "gsw": …}`), kurz, für sich verständlich, grammatisch richtig; Glieder
  vollständig (eine Reihe mit acht Gliedern zeigt acht Zellen).
- Sprecher als Porträt mit Titelblase (`speaker`, `title`), Zeichen oder Porträts in Zellen (`icons`, `who`), wo sie das
  Erkennen erleichtern.
- Die Kachel ist so gross wie ihr Inhalt; `span: 2` nimmt die ganze Breite (für breite Reihen, Pfeilketten, Raster).

