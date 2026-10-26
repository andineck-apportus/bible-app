# Zeichen, die man erraten kann – Erstellung und Prüfung

Stand 2026-10-23 (Auftrag Andi Neck). Gegenstück zu [BILDPROZESS.md](BILDPROZESS.md) für die Bildzeichen im Lexikon
(`data/illustrations/lexicon/FIG-ZEICHEN-*`, heute 191; Stand der Einleitung 2026-10-23, neue Zeichen in den Runden unten). Personen, Orte und Gegenstände folgen denselben Schritten,
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
   - zuerst offen nach dem Abbild fragen («Was ist abgebildet?», Gegenstand oder Lebewesen, ohne Bedeutung), dann frei
     benennen («Was könnte es in einer Bilderbibel bedeuten? ein bis drei Wörter»), siehe «Prüfung in Einsatzgrösse», Punkt 5;
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
   «Bild erkannt» 0/1), mit `--frage abbild` zuerst die offene Frage nach dem Abbild (Punkt 5), mit `--silhouette` nur der
   Umriss.
4. **Zwei Masse:** «erkannt» (mindestens zwei von vier Antworten treffen die Bedeutung) und «Bild erkannt» (die Mehrheit sieht,
   was gezeichnet ist). Ist das Bild erkannt, die Bedeutung aber nicht, ist das Zeichen gut gezeichnet, aber ein Begriff:
   dann Wortzeichen, nicht neu zeichnen.
5. **Zuerst nach dem Abbild fragen (Regel seit 2026-10-24, Runde 6c).** KI-Testpersonen erkennen manche Zeichen, Menschen
   nicht: Die Henne mit Küken (Runde 6) benannten 12 von 12 Instanzen als «Henne mit Küken», Andi Neck sah «eine Fruchtplatte»
   (brauner Hügel mit gelben Kugeln). Die Instanzen schliessen aus wenigen Merkmalen und dem Zusammenhang auf das Gemeinte.
   Deshalb fragt der Test zuerst offen «Was ist abgebildet?» (Gegenstand, Lebewesen; ohne Bedeutung, ohne Hinweis auf die
   Bibel) und erst danach «Was könnte es bedeuten?» (`zeichen_test.py --frage abbild`). **Ein Zeichen gilt nur als erkannt,
   wenn das Abbild selbst richtig benannt wird**; eine getroffene Bedeutung bei falschem oder nur ungefährem Abbild («Hügel
   mit Kugeln», «Vogel auf Nest») zählt nicht. Zusätzlich wird der Umriss geprüft (`--silhouette`, alles einfarbig schwarz,
   32 px): Er kommt dem ersten Blick eines Menschen näher. Die alte Henne wurde als Umriss als «Busch mit Flamme» oder
   «kniende Person» gelesen, der erste Neuentwurf als «Wagen mit Zugtier» (Küken als Räder unter einem Kasten), ein Vogel von
   vorn über einer Figur als «Engel». Getragen haben erst frei stehende Teile mit eigenem Umriss: Junge mit Kopf und Schnabel
   statt Kugeln, Flügel mit getrennten Schwungfedern statt Fläche, Abstand zwischen Vogel und Figur.

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

### Hände als eine Silhouette (Runde 8, 2026-10-25)

Hinweis Andi Neck: Finger wirkten «draufgeklatscht», weil jede Fingerform und die Handfläche ihre eigene Kontur hatten
(Rand quer über die Innenseite der Hand); die betenden Hände waren kaum als Handflächen erkennbar. Regel: Hände (und
andere aus Teilen gebaute Formen) haben **eine Kontur nur aussen** – Teile zuerst dick in Tinte, darüber dieselben Teile
hautfarben ohne Strich; die Fugen zwischen den Fingern bleiben als Linien bis zur Handfläche. Betende Hände: zwei
Handflächen mit gestuften Fingerspitzen, Daumen vorn, Ärmel. Blindtest Runde 8 (32 px, 4 Instanzen): beten, grüssen,
Schwur je 4 von 4 mit voller Bedeutung; Hand als Hand erkannt, aber als Geste gelesen
([Bericht](../reports/zeichen-blindtest-2026-10-25-runde8-haende.json)).

Nachtrag Runde 10: Die gestuften Fingerspitzen der betenden Hände wirkten auf Andi Neck wie Füsse, obwohl der Blindtest
bestand. Neu nach dem Vorbild des Emojis «gefaltete Hände»: zwei Handflächen, Fingerspitzen oben spitz zusammen, Finger
geschlossen (nur feine Längslinien), ohne Daumen. Lehre: Bei Händen und anderen Körperteilen entscheidet der menschliche
Eindruck; bekannte Vorbilder (Emoji, Piktogramme) zuerst ansehen
([Bericht](../reports/zeichen-blindtest-2026-10-25-runde10-beten.json)).

## Durchsicht und Gestaltungsregeln (Runde 11, 2026-10-25)

Anlass (Andi Neck): Hände teils gut, teils unverständlich oder schlecht gezeichnet; Almosen wirkt wie eine Schüssel; «der
Prozess muss besser werden». Befund: Der Blindtest («was bedeutet das?») ist zu nachsichtig – eine KI errät die Bedeutung
auch aus schlechten Zeichnungen (betende Hände wie Füsse bestanden 4/4). Eine Gestaltungskritik aller 421 Zeichen ohne
Personen (drei getrennte Instanzen, Massstab Piktogramm-Designer) ergab: 139 ok, 241 überarbeiten, 41 neu.

**Ablauf für jedes neue oder überarbeitete Zeichen (verbindlich):**
1. **Vorbild zuerst:** bewährte Lösung suchen und benennen (Emoji, Leitsystem-/Verkehrspiktogramm, Symbole der unterstützten
   Kommunikation) – beschreiben, nicht kopieren. Hauptmotiv vor Detail: Was muss man auf einen Blick sehen?
2. **Zwei bis drei Fassungen** zeichnen, gross und in 32 px ansehen (Read), selbst verwerfen, was ein Designer nicht abgäbe.
3. **Gestaltungskritik:** `zeichen_test.py … --frage kritik --befragen 3` – bestanden nur mit Mehrheitsurteil «ok» und
   Mittelwerten ≥ 4 in Abbild, Zeichnung und Sinn. Sonst überarbeiten (höchstens drei Runden, dann als offen melden).
4. **Blindtest** wie bisher (`--frage abbild --befragen 4 --bewerten`): Sinn muss ohne Namen ankommen.
5. **Menschliches Urteil zuletzt:** Andi Neck sieht die Übersicht; sein Eindruck geht jedem Test vor.

**Gestaltungsregeln (aus der Durchsicht):**
- **Hände** nur aus der gemeinsamen Handbibliothek (offen, empfangend wie 🫴, gebend von oben wie 🫳, zeigend, haltend,
  Faust, betend wie 🙏, zwei Hände wie 🤲 / 🙌): eine Silhouette mit Kontur nur aussen, Daumen klar abgesetzt, Finger
  verschieden lang, Ärmel als Manschette. Keine Fäustlinge, Keile, Balken oder «Wurst-Arme» quer über Körper.
- **Handlungen nicht als blosse Pfeile** (bringen, fliehen, erhöhen …): Figur oder Gegenstand in Handlung zeigen
  (🏃 fliehen, Figur trägt etwas = bringen); Pfeile nur als Zusatz.
- **Keine Bedien-Symbole** (Lautsprecher, WLAN-Bögen, Häkchen-Boxen, Download-Pfeile) für biblische Begriffe.
- **Jeder Begriff sein eigenes Bild:** keine Doppelten (Licht ≠ Stern/Zeichen, Reich Gottes ≠ Königsherrschaft, Tage ≠
  Sonne ≠ Hitze, Wahrheit ≠ vollbracht, Sünde ≠ unrein).
- **Verneinung einheitlich:** roter Kreis mit Schrägstrich = «nicht tun / verboten» (über dem Motiv); rotes X = «falsch,
  Nein»; leer = leerer Gegenstand, kein Verbotsschild.
- **Gefühle und Zustände** als Gesicht im Emoji-Stil (Freude, Trauer, Zorn, Sorge, Hass), nicht als Wolke oder Klecks.
- **Landschaften und Orte** mit Kontur und klarer Form (Ufer, Wasserlinie, Furchen), nicht als blasse Streifen.
- Nichts am Rand abschneiden; Teile verbunden (keine schwebenden Einzelteile ohne Bezug).

Überarbeitete Zeichen liegen in `scripts/authoring/bildsymbole_daten/ueberarbeitet/<thema>.json` ({Lexikon-ID: {vb, svg}});
`bilder_anime.library()` ersetzt damit die bisherige Zeichnung unter derselben ID.

## Runde 12: Emoji zuerst, prägnant (Entscheid Andi Neck 2026-10-25)

Befund aus Runde 11 (Andi Neck): «Wenn du versuchst, Körperteile detailliert zu malen, wird es unverständlicher.» Von Hand
gezeichnete SVG-Piktogramme erreichen die Qualität bewährter Sätze nicht zuverlässig, und die KI-Gestaltungskritik schwankt
von Runde zu Runde. Darum:

- **Emoji, wo es geht:** Grundlage ist Twemoji (Twitter, Inc. und Mitwirkende, CC BY 4.0, [LIZENZEN.md](../LIZENZEN.md)).
  Ein Zeichen ist ein Emoji, höchstens zwei, in fester Anordnung (`einzeln`, `paar`, `abzeichen`, `verbot` = «nicht tun»,
  `nein` = «falsch»); Hände und Gesichter im Hautton der Figuren. Werkzeug: `scripts/authoring/emoji_zeichen.py`,
  Zuordnung `scripts/authoring/emoji_zuordnung.json` (je Zeichen mit Grund).
- **Sonst prägnant:** Eigene Zeichnungen nur für Biblisches ohne Emoji (Tempel, Gesetzestafeln, Personen der Bibel …), im
  Stil der Emoji: wenige grosse Formen, keine feinen Körperdetails, höchstens drei Elemente.
- **Ideenfindung:** je Zeichen bis drei Vorschläge (Emoji-Namen, Anordnung, Grund), zuerst das eine Emoji, das den Begriff
  im Alltag schon trägt; dazu vier naheliegende, aber verschiedene Begriffe als Ablenker (keine Synonyme).
- **Kontrolle der Verständlichkeit:** Unterscheidungstest `zeichen_test.py --frage auswahl` (vier Instanzen wählen unter
  der Bedeutung und den Ablenkern; bestanden ab drei Vierteln). Er prüft, ob ein Zeichen sich von verwandten Begriffen
  abhebt – strenger und fairer als freies Benennen, das eine KI auch bei schwachen Zeichen errät. Fällt Vorschlag 1 durch,
  wird Vorschlag 2 geprüft usw.
- **Kontrolle der Umsetzung:** Gestaltungskritik (`--frage kritik`) nur noch für Zusammensetzungen und eigene Zeichnungen;
  einzelne Emoji sind professionell gezeichnet.
- **Mensch zuletzt:** Andi Neck sieht nur noch die Grenzfälle (kein Vorschlag bestanden) und eine Übersicht.

Ergebnis Runde 12 (2026-10-25): 421 Zeichen geprüft; bisherige Zeichen bestanden den Unterscheidungstest zu 376, Vorschlag 1
zu 348 von 416, Vorschlag 2 zu 22 von 45, Vorschlag 3 zu 3 von 10. Übernommen: 333 Emoji-Zeichen; bisher behalten: 48
«eigen» (kein passendes Emoji) und 2 Doppelte (Licht, vollbracht). Lehre: Der Unterscheidungstest mit fünf Antworten ist für
eine KI leicht; er taugt als Sicherung gegen Fehlgriffe, nicht als Qualitätsmass. Nächster Schritt: prägnante eigene Zeichen
für die 48 «eigen» nach den Regeln oben; schwerere Ablenker (engste Nachbarbegriffe im Lexikon) für eine strengere Prüfung.

Nachtrag (2026-10-25, Hinweise Andi Neck: uneinheitlich; Küken für «geboren werden», Honigtopf als «Land»): Emoji werden im
Stil der Figuren gesetzt (dunkle Kontur, Hautton, gedämpfte Farben). Neu fest im Ablauf ist die **Kontextprüfung**: getrennte
Instanzen sehen jedes Zeichen mit seinen echten Verwendungen (Bild, Szene/Kästchen/Sprechblase, Handlung) und urteilen ok /
ersetzen / eigen nach Sinn an jeder Stelle, Ton und Würde (nichts Niedliches, Albernes, Modernes), Tauglichkeit als Gegenstand
in einer Szene und Verwechslung. Ergebnis: 161 ok, 54 ersetzt, 118 zurück auf eigene Zeichnung; gemeldete Fehlzuordnungen in
Bildaufträgen (z. B. «lösen» beim Losbinden der Eselin) stehen im Bericht und werden an der Quelle korrigiert.

## Runde 13: einheitlich und passend zum Text (2026-10-25)

- Stil: `einheitlich()` gibt allen eigenen Zeichen (sign, object, place, action; nicht Personen, nicht breite Landschaften) dieselbe Kontur wie den Emoji. Personen-Emoji werden umgefärbt (Haar dunkel, Jeans in Erdtönen).
- Verwendungsprüfung: Die Verwendungen je Zeichen und Feld (mit Text des Feldes) werden auf getrennte Instanzen verteilt; sie melden {datei, bild, feld, wo, alt, neu|null, fehlt}. Korrekturen werden per Skript eingespielt; was mehrfach als «fehlt» gemeldet wird, bekommt ein neues Lexikon-Zeichen.
- Sichtprüfung danach durch eine weitere Instanz auf gerenderten Bildern und einer Tafel aller Zeichen: Stilbrüche, Verwechslungen, Verstösse gegen Lexikonregeln, Fehlgriffe je Feld.
- Lehre: Bei jedem Zeichenwechsel Legende, Merkmale und Bildbeschreibungen (caption, daraus Alt-Text) mit nachführen; sonst widerspricht der Alt-Text dem Bild.

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
| Zuflucht unter Flügeln (6c: Vogel breitet den Flügel über kniende Frau) | Henne: Andi Neck «Fruchtplatte», als Umriss «Busch, kniende Person» | 4 · 4 · 4 von 4 (Abbild 4 · 4 · 4, Umriss 4 · 4 · 4) | 2 | «Adler über Person», «Schutz unter Flügeln» | erkannt |
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

Wortzeichen (das Bild wird gesehen, die Bedeutung nur mit dem Wort aus der Übersetzung): Treue, leuchten, rein,
weites Tor (nur im Paar mit dem engen Tor), Mammon, Talent, Löser, besonnen, fromm, freundlich, Sanftmut, eigenmächtig,
verleumden («Lästern», «Lüge»), sich unterordnen, töricht («Zweifel»), dazu wie bisher Kopf mit Haar (Neuentwurf schlechter,
die alte Zeichnung bleibt) und Jota. Knapp erkannt (2 von 4): grüssen, Kind, klug. «Ruhe / Zuhause» (Rut 3,1) ist erkannt,
steht im Pilotbild aber im Titel eines Feldes, der kein Zeichen trägt.

Entscheide, die frühere Regeln ändern: Die Zuflucht ist jetzt ein grosser Vogel im Profil, der den Flügel wie ein Dach über
eine kleine kniende Frau breitet (Runde 6c, nach [[RUT.2.12]]; Bild des Schutzes, nicht Darstellung Gottes; von der Henne
FIG-OBJ-HENNE und dem Adler des Johannes getrennt). Vorher nur Flügel (als Cherub oder Engel gelesen), dann eine Henne mit
Küken, die Andi Neck als «Fruchtplatte» las (Daten: `reports/zeichen-blindtest-2026-10-24-runde6c.json`; auch eine neu
gezeichnete Henne bestand den Test, die Figur unter dem Flügel trifft aber die Bedeutung öfter, 12 statt 7 von 12).
Enges und weites Tor haben Türme und Zinnen (ohne sie als Mauer oder Tür gelesen). Münzen ohne Prägung, wo die Form genügt (Haufen, Stapel, Truhe); die einzelne Münze
(Denar, Mammon, Gewinn) mit Prägung.

Offen: Salz, Splitter, Kammer, Becher leer, Freude, Licht (32 px nicht erkannt, nicht Teil dieser Runde); Test der ganzen
Strukturbilder mit den neuen Zeichen.

### Runde 7 (Tod und Böses, 2026-10-24)

Anlass (Andi Neck, 2026-10-24): «Tod und Sterben werden in den Bildern stark ausgeblendet und Symbole weggelassen. Das
verzerrt das Bild.» Regel dazu in BILDSPRACHE.md («Tod und Böses nicht ausblenden»). Gemessen wie Runde 6c
(`zeichen_test.py --frage abbild --verteilen`): 32 px allein je Stufe vier Instanzen, als Umriss vier, in der Zelle und bei
160 px je zwei; Bewertung durch eine weitere Instanz. Daten: `reports/zeichen-blindtest-2026-10-24-runde7.json`.

| Zeichen | vorher | Stufe 1 · 2 · 3 (32 px allein) | Umriss | gewählt | gelesen als | Urteil |
|---|---|---|---|---|---|---|
| gestorben / Verstorbener (neu) | Grab (Tod) 0/16 «Grab» | 8/8 · 4/4 · 3/4 | 8/8 · 4/4 · 4/4 | 2 | «Leichnam auf Bahre → Tod» | erkannt |
| Totenklage (neu) | – | 4/4 · 8/8 · 4/4 | 2/4 · 7/8 · 3/4 | 2 | «Weinende Person, Arme erhoben → Klage, Trauer» | erkannt |
| töten / Mord (neu, mit Stein) | – | 0/4 · 0/4 · 0/8 | 2/4 · 0/4 · 7/8 | – | «Steinigung» | verworfen |
| töten / Mord (mit Keule) | – | 2/4 · 4/4 · 2/4 | 3/4 · 3/4 · 3/4 | – | «Totschlag», «Kain und Abel» | verworfen |
| töten / Mord (mit Schwert) | – | 4/4 · 4/4 · 4/4 | 3/4 · 3/4 · 2/4 | 2 | «Mann schwingt Schwert → Mord» | erkannt |
| Feuer der Hölle (Gehenna, neu) | Flamme (Feuer) | 8/8 · 4/4 · 4/4 | 4/8 · 0/4 · 0/4 | 1 | «Feuer in Schlucht → Hölle» | erkannt |
| verfolgen (neu) | – | 4/4 · 8/8 · 4/4 | 0/4 · 8/8 · 1/4 | 2 | «Mann verfolgt Fliehenden → Verfolgung» | erkannt |
| Hass (neu gezeichnet) | zerbrochenes Herz 0/4 «Kummer» | 0/4 · 4/4 · 2/4 | 0/4 · 0/4 · 0/4 | 2 | «zwei grimmige Männer, abgewandt → Feindschaft» | erkannt (Umriss nicht) |

Vorhandene Zeichen in derselben Messung (32 px allein, 16 Antworten): Gericht (Waage), krank, Feuer, Kreuz, Gefängnis je 16/16;
das Böse 10/16 (meist «Sünde»), Sünde 13/16 («Unreinheit»), Wolf als Bild 16/16 (Bedeutung «falscher Prophet, Feind»),
Dämon 2/16 (Wortzeichen); Grab für «Tod» 0/16 (immer «Grab»); Trauer (Tropfen) 0/16 als Bild erkannt («Wassertropfen»,
als Umriss «Blut»).

Lehren: Ein Stein in der erhobenen Hand liest sich als Steinigung, eine Keule als Kain und Abel, das Schwert als Mord. Ohne
Tränen werden erhobene Hände als Verzweiflung gelesen. Das zerbrochene Herz liest sich als Kummer; Hass trägt die Abwendung
mit bösem Blick. Die Rauchwolke über der Gehenna machte den Umriss zur brennenden Stadt. Für «er starb», «gestorben» steht
künftig der Verstorbene auf der Bahre, das Grab für «begraben» und «Grab». Offen: die Trauer als Tropfen (in Zellen nicht als
Trauer gesehen; in Szenen bleiben es Tränen im Gesicht), Hass als Umriss, ein Test der ganzen Bilder ohne Legende.

### Runde 9 (Wortzeichen für «ohne Worte», 2026-10-25)

Anlass: Titelblasen, Spaltenköpfe, Stichwortbänder, leere Zellen und Sprechblasen der Pilotbilder (Mt 5–7, Rut, Titus)
sollen ein Zeichen tragen, in der Ansicht «ohne Worte» statt der Worte und neu auch neben ihnen. Der Automat (`nw_icons`)
fand für 211 von 351 Stellen nichts. Zuordnung von Hand für alle 351 Stellen
(`scripts/authoring/bildauftraege_daten/_wortzeichen.json`, je Stelle ein bis zwei Zeichen und ein kurzer Grund): Der
Auto-Treffer bleibt 79-mal, wird 38-mal ergänzt und 23-mal ersetzt, z. B. Waage «Gericht» → «gerecht» bei
«Gerechtigkeit», «fehlt» → «geben, Weg» bei «damit ihnen nichts fehlt», «klug, zeigen» → «Spalter, ablehnen».
Vorhandene Zeichen tragen die meisten Stellen: «Ihr habt gehört …» = Ohr und Gesetzestafeln, «Ich aber sage euch …» =
Jesus und sprechen, «nicht … / sondern …» = Kreuz und Haken, Vorfahren ohne Porträt = Vater.

Neu sind nur vier Zeichen, eines ist neu gezeichnet (Detailstufe 2 nach «Mittlere Stufe zuerst»). Gemessen mit
`zeichen_test.py --frage abbild --befragen 4 --bewerten`, 32 px allein. Daten:
`reports/zeichen-blindtest-2026-10-25-runde9.json`.

| Zeichen | Stellen | gezeichnet | 32 px allein | gelesen als | Urteil |
|---|---|---|---|---|---|
| lehren (neu) | 13 | Lehrer mit Bart hebt den Finger, offene Schriftrolle, kleiner Zuhörer | 4/4 | «Mann mit Schriftrolle, Kind → lehren» | erkannt |
| im Verborgenen (neu) | 8 | Haus im Schnitt, verriegelte Tür, darin kniet jemand und betet | 3/4 | «betender Mensch im Haus → Gebet im Verborgenen» | erkannt |
| erinnern (neu) | 2 | Zeigefinger mit roter Fadenschleife | 4/4 | «Finger mit roter Schleife → erinnern» | erkannt |
| sich sorgen (neu gezeichnet) | 6 | besorgtes Gesicht, Schweisstropfen, Knäuel darüber (vorher nur Tropfen) | 4/4 | «besorgter Mann → Sorge» | erkannt |
| vollkommen (neu) | 3 | 9a dicker Ring mit Füllung; 9b dünner Ring ohne Füllung | 0/4 · 0/4 | 9a «goldene Münze → Schatz»; 9b «goldener Ring → Bund» | Wortzeichen |

Vorhandene Zeichen, auf die sich die Zuordnung stützt (gleiche Messung): hören, Gesetzestafeln, gerecht je 4/4; Haken
(Wahrheit) als «richtig», gute Werke als «Barmherzigkeit», bewahren als «Schutz» (Hände nicht gesehen); segnen 2/4
(zweimal «zeigt auf Kind → zurechtweisen»), es trägt «selig»; «nicht richten» 0/4 («durchgestrichene Waage →
Ungerechtigkeit»). Offen: «nicht richten» (vier Stellen) und «selig» brauchen ein besseres Zeichen; die Zeichen in der
Zelle, als Umriss und im ganzen Bild ohne Legende sind noch nicht geprüft.

### Runde 14 (Ersatzzeichen in Johannes, 2026-10-26)

Anlass (Andi Neck): In den Johannes-Bildern standen Ersatzzeichen – «verkündigen» (Rufer) für «Zeugnis ablegen»,
«sich ausbreiten / hinausgehen» (Erdkugel mit Fussspuren) für «senden», die Taube bei «Er hauchte sie an» ([[JHN.20.22]]),
der Keimling für «die Reben» ([[JHN.15.5]]); die zwei Mitgekreuzigten ([[JHN.19.18]], [[JHN.19.32]]) fehlten, weil das
Lexikon keine Figur für sie hatte. Neu nach «Runde 12: Emoji zuerst» und Stil «einheitlich». Gemessen wie Runde 6c
(`zeichen_test.py --frage abbild --verteilen --befragen 4 --bewerten`, 32 px, je Fassung vier Instanzen, die Fassungen auf
getrennte Sätze verteilt). Daten: `reports/zeichen-blindtest-2026-10-26-runde14.json`.

| Zeichen | Fassungen (gezeichnet) | Abbild erkannt | Bedeutung getroffen | gewählt | Urteil |
|---|---|---|---|---|---|
| Zeugnis ablegen (`FIG-ZEICHEN-ZEUGNIS`) | 1 Auge + sprechender Kopf · 2 Kopf mit Auge · 3 Auge + erhobene Hand · 4 Hand mit Auge | 8/8 · 4/4 · 4/4 · 4/4 | 0/8 «Prophet, Seher» · 1/4 «sehen» · 0/4 «siehe» · 0/4 «nicht sehen» | 1 | Wortzeichen |
| senden (`FIG-ZEICHEN-SENDEN`) | 1 Zeigehand + gehende Person · 2 gehende Person mit Zeigehand | 4/4 · 8/8 | 0/4 «du gehst» · 3/8 «senden, gesandt» | 2 | knapp (sonst «hingehen») |
| anhauchen (`FIG-ZEICHEN-ANHAUCHEN`) | 1 ausatmendes Gesicht · 2 blasende Wolke · 3 Person mit Atemwolke · 4/5 ausatmendes Gesicht + Person(en) | je alle | 0 («seufzen», «Wind, Geist», «Geist, Atem», «Klage», «Trost») | 3 | Wortzeichen |
| Rebe (`FIG-OBJ-REBE`, eigene Zeichnung) | 1 Zweig mit Weinblatt, Ranke und Traube · 2 Stamm mit abzweigender Rebe | 4/4 · 8/8 | 4/4 · 4/8 (sonst «Weinberg») | 1 | erkannt |

Lehren: Abstrakte Handlungen ohne eigenes Emoji (bezeugen, anhauchen) zerfallen in ihre Teile: Auge + Kopf wird
«Prophet, Seher», ein ausatmendes Gesicht «seufzen», eine Atemwolke «Geist, Atem». Sie bleiben Wortzeichen und stehen bei den
Worten (im ganzen Bild Joh 20,19–23 las eine Instanz das Anhauchen-Zeichen neben «Empfangt heiligen Geist!» richtig). Die
Rebe ist als Zweig mit Blatt erkennbar; ein Stamm daneben macht sie zum «Weinberg».

**Figur «Mitgekreuzigter»** (`FIG-ROLLE-MITGEKREUZIGTER`): neutraler Mann in graubraunem Gewand, ohne Erkennungszeichen und
ohne Tat (Johannes nennt sie nicht «Räuber»); in Szenen am Kreuz in einfacher Form wie Jesus, aber ohne Tafel und Nimbus,
mit `twin` zweimal (links und rechts) und mit `far` kleiner im Hintergrund. Blindtest: Das Feld Joh 19,18 ohne Stichwortband
lasen 3 von 3 Instanzen als «Jesus zwischen den zwei Mitgekreuzigten»; das Porträt allein als «allgemeine männliche Figur»
(gewollt: keine Merkmale, die eine Tat oder Gruppe zuschreiben). Die Instanzen nannten sie aus der Überlieferung
«Schächer, Verbrecher».

Ersetzt in den Johannes-Bildaufträgen (Zellen und `_wortzeichen.json`, Legenden nachgeführt): «verkündigen» und «zeigen», wo
Zeugnis gemeint ist (u. a. [[JHN.1.7]], [[JHN.5.31-JHN.5.39]], [[JHN.8.13]], [[JHN.15.26-JHN.15.27]], [[JHN.19.35]],
[[JHN.21.24]]); «hinausgehen» bei «so sende auch ich euch» ([[JHN.20.21]]); Taube → anhauchen ([[JHN.20.22]]); Keimling →
Rebe ([[JHN.15.5]]). Die Mitgekreuzigten stehen in [[JHN.19.18]] (Feld 2), [[JHN.19.31-JHN.19.34]] und im Kapitelbild
Joh 19 (Feld 3) im Bild.

### Runde 15 (Figuren und Zeichen für Lukas 1–2 und 8, 2026-10-26)

Anlass: Für die Lukas-Bilder fehlten Personen, die Hirten, die Krippe und das Schreibtäfelchen. Neu im Lexikon (Daten in
`bildlexikon_daten/LUK.json`, `figuren_daten/LUK.json`, `bildsymbole_daten/LUK.json`): `FIG-ZACHARIAS`, `FIG-ELISABET`,
`FIG-ENGEL-GABRIEL`, `FIG-SIMEON`, `FIG-HANNA-PROPHETIN`, `FIG-JESUS-JUNGE`, `FIG-JOHANNA`, `FIG-SUSANNA`, `FIG-GRUPPE-HIRTEN`,
`FIG-OBJ-KRIPPE`, `FIG-OBJ-SCHREIBTAFEL`. Grundsatz: nichts über den Text hinaus (keine Heiligenattribute, kein Nimbus ausser bei
Jesus nach der bestehenden Regel). Gemessen wie Runde 14: Gegenstände mit `zeichen_test.py --entwuerfe … --verteilen --frage abbild
--befragen 4 --bewerten` (32 px, je Fassung vier Instanzen); Personen und Gruppe als Porträt ohne Namen, je drei getrennte Instanzen
(`claude -p`, nur Lesezugriff) mit {abbild, wer, merkmale, sicherheit}, bewertet von einer weiteren Instanz gegen den Lexikon-Eintrag;
dazu alle elf in Einsatzgrösse 32 px (vier Instanzen). Daten: `reports/zeichen-blindtest-2026-10-26-runde15.json`.

| Eintrag | Gezeichnet | Porträt (3 Instanzen) | 32 px (4 Instanzen) | Nachbesserung |
|---|---|---|---|---|
| Zacharias | alter Priester, weisser Kopfbund, blaue Schärpe, goldener Räucheraltar ([[LUK.1.9]]) | 3/3 «Zacharias» | 4/4 | – |
| Elisabet | ältere Frau, olivgrünes Kopftuch, kein Zeichen | 3/3 alte Frau, Elisabet neben Sara | Bild 4/4 | meergrün las sich in 32 px als «Maria» (Blau) |
| Engel Gabriel | wie jeder Engel, schmaler Goldsaum, Name im Bild ([[LUK.1.19]]) | 3/3 «Engel, am ehesten Gabriel» | Bild 3/4, Bedeutung 4/4 | – |
| Simeon | alter Mann vor Tempelsäulen, hält das Kind ([[LUK.2.28]]) | ohne Kind 1/3 (2/3 «Eli»), mit Kind 3/3 | 4/4 | Kind als Zeichen |
| Hanna, Prophetin | sehr alte Frau, dunkelbraunes Kopftuch, Tempelsäulen | 3/3 «Prophetin Hanna» | 4/4 | – |
| Jesus als Junge | Kreuznimbus, weisses Gewand, roter Mantel, Junge | langes Haar 3/3 Jesus (einmal offen, ob jung); kurzes Haar 3/3 «Zwölfjähriger» | 4/4 «Jesus als Kind» | kurzes Haar |
| Johanna, Susanna | schlichte Frauen ohne Zeichen, nur durch den Namen unterschieden | je 3/3 «Frau aus dem Volk», nie Maria aus Magdala | Bild 4/4 | Kopftuchfarben (s. u.) |
| Hirten | Hirtengewand, heller Mantel, Schaf vorn, Stäbe | 3/3 «Hirten von Betlehem» | 4/4 | – |
| Futterkrippe mit Kind | 1 Holztrog mit Beinen · 2 Kastenkrippe · 3 flach, grosses Kind | – | je 4/4; gewählt 2 | – |
| Schreibtafel | 1 dunkle Wachsfläche + Griffel · 2 aufgeklappt · 3 helle Fläche | – | 4/4 · 4/4 · 0/4 («Gesetz») ; gewählt 1 | – |

Lehren: Farben ohne Zeichen tragen Bedeutung, auch wenn keine gemeint ist: ein sandgelbes Kopftuch wird in 32 px blondes Haar,
ein cremefarbenes graues Haar (alte Frau), Lavendel wird Purpur («Lydia»), Meergrün wird Marias Blau. Für Figuren ohne
Erkennungszeichen deshalb mittlere, eindeutig «textile» Töne wählen (olivgrün, altrosa, terrakotta). Eine Person, die nur in
einer Szene vorkommt, wird am sichersten über ihre Handlung im Text erkannt (Simeon mit dem Kind); Säulen allein machen einen
alten Mann zu «Eli am Heiligtum». Eine helle Schreibfläche liest sich als Gesetzestafel, eine dunkle Wachsfläche mit Griffel als
Schreibtafel. Nebenbefund an bestehenden Figuren (nicht geändert): in 32 px las sich das Fläschchen der Maria von Betanien als
Säugling, die Kelle der Marta als Hammer, der Ölkrug der Salome als Wasserkrug.

Nachtrag Gesamtbild (Schritt 8, 2026-10-26, v0.130): Die elf Einträge stehen in den Bildaufträgen zu Lk 1–2 und 8 (zehn Bilder).
Sechs Bilder hat je eine getrennte Instanz ohne Auftrag und ohne Legende beschrieben (`reports/bild-blindtest-2026-10-26-lukas-figuren.json`,
Befund im Feld `check` der Bilder): Gabriel, Zacharias als Priester, Elisabet, Hanna, Johanna und Susanna (über das Namensschild),
die Hirten als Gruppe, die Krippe mit dem gewickelten Kind, die Schreibtafel und der zwölfjährige Jesus wurden erkannt. Grenzen: Ein
gehaltenes Kind (Simeon, Maria) und der Räucheraltar des Zacharias liegen tief vor der Brust und werden vom Namensschild am unteren
Rand weitgehend verdeckt; Simeons Schild steht deshalb erst im Bild, in dem er das Kind nicht trägt. Simeon trägt das Kind nur, wo
der Text es sagt ([[LUK.2.28]]); sonst `stage.hold` `"LEER"`.

### Reihenfolge der Überarbeitung

1. Die 20 meistverwendeten schwachen Zeichen (rund die Hälfte aller schwachen Verwendungen).
2. Übrige Handlungen und Gegenstände.
3. Begriffe als Wortzeichen, sobald Worte im Bild umgesetzt sind (BILDPROZESS.md).
