# Bildsprache

Bilder fassen auf den Zoomstufen (Buch, Kapitel, Abschnitt) bildlich, was die Zusammenfassung in Worten sagt. Sie sind **Deutung, nicht Text**: Sie legen mehr fest als der Text (Kleidung, Anordnung, Gewichtung), stehen neben der Zusammenfassung und ersetzen sie nicht. Die App kennzeichnet jedes Bild entsprechend («Legende und Hinweise»). Datenfelder: [DATENMODELL.md](DATENMODELL.md#bildsprache-seit-v055-lexikon-und-bildaufträge-seit-v056).

## Drei Schichten

1. **Bildlexikon** (`data/illustrations/lexicon/FIG-*.json`, stilunabhängig): Wer oder was ist das, woran erkennt man es (Pflichtmerkmale mit Grundlage: Text, Tradition oder eigene Gestaltung), womit darf es nicht verwechselt werden. Gilt für die ganze Bibel; so trägt Maria überall Blau, Jesus überall den Kreuznimbus, ein Diener überall die Schürze. Werkzeug: `scripts/authoring/bildlexikon.py`.
2. **Bildauftrag** je Stelle (`data/illustrations/briefs/BRIEF-*.json`, stilunabhängig): Bildfelder in Reihenfolge, je Feld Stelle, Figuren, Gegenstände, Zeichen, Sprechblasen (wer zu wem, mit welchen Zeichen) und die Handlung in einem Satz. Der Auftrag wird wie eine Zusammenfassung gegen den Text geprüft (Handelnde, Wer-zu-wem, Zeitform, Ankündigung statt Bericht). Werkzeug: `scripts/authoring/bildauftraege.py`.
3. **Stil** (`data/illustrations/styles/ILLSTYLE-*.json`): wie dieser Stil jeden Lexikon-Eintrag zeichnet (`renderings`). Stil «Symbol»: eigene SVG-Bibliothek (`data/illustrations/symbol/_bibliothek.svg`), Bilder in `scripts/authoring/bilder_symbol.py` aus den Bauteilen zusammengesetzt. Stil «Anime» (seit v0.61, seit v0.64 auf allen Ebenen mit Bildern: Bibel, Testamente, Buchgruppen, Johannes, Johannes 2 und seine Abschnitte): comicartig ohne Text, Personen mit Gesicht und Ausdruck, Manga-Panels mit schrägen Rändern, Bewegungs- und Emotionszeichen (Schweisstropfen = Sorge, Tränen über die Wangen = Trauer, Strichkranz = Staunen, Funkeln = Freude; Ausdrücke ruhig, ernst, nachdenklich, besorgt, staunend, froh – nie zornig oder drohend; Dreiviertelansicht für Abwenden); Werkzeug `scripts/authoring/bilder_anime.py`, Bibliothek `data/illustrations/anime/_bibliothek.svg` (Gegenstände und Zeichen aus dem Symbolstil übernommen, damit sie in beiden Stilen gleich gelesen werden). Fehlt ein Bild im gewählten Stil, zeigt die App das Symbolbild. Beim Bild und in der Legende lässt sich der Stil umschalten; das Bildlexikon im Menü zeigt je Stil alle gezeichneten Einträge (Grafik-Index). Weitere Stile (Skizze, Malerei) zeichnen dieselben Aufträge mit denselben Pflichtmerkmalen; bei Bildgeneratoren mit Figurenblättern und Referenzbildern je Lexikon-Eintrag, damit Figuren über Bilder hinweg gleich bleiben.

## Bildsprachen je Kultur und Sprache (vorgemerkt)

Bilder ohne Text taugen vorerst für alle Sprachen. Später soll es Bildsprachen je Kultur geben, nach demselben Muster wie die Übersetzungsschichten (eigene Schicht mit `target_context`, nie stillschweigend abgeleitet):
- **Stil mit Zielkontext:** ein `illustration_style` kann `target_context` und `language` tragen (z. B. ein Stil für Westafrika oder für Kinder in der Schweiz); die App wählt nach Sprache bzw. Leserkontext.
- **Zeichen, die kulturell verschieden gelesen werden** (Gesten, Farben von Trauer und Freude, Herz, Daumen, Leserichtung der Panels von links oder rechts), als Varianten am Lexikon-Eintrag mit Kontext und Begründung; der Bildauftrag bleibt gleich.
- **Prüfung** durch Menschen aus dem jeweiligen Kontext eintragen, nicht behaupten; der KI-Blindtest ersetzt sie nicht.

## Gestaltungsregeln

- **Handlungen:** mehrere Schritte als nummerierte Bildfelder; Gesagtes als Sprechblase mit Zeichen statt Wörtern, die Spitze zeigt auf die sprechende Figur, die Geste (Arm) auf die angesprochene. Die Blase steht möglichst direkt über der sprechenden Figur; steht sie daneben (z. B. beim Strahlenkranz), geht die Spitze von der zugewandten Seite aus (links, rechts, oben oder unten). Die Spitze ist kurz und gerade; eine lange, schräg verzogene Spitze ist ein Gestaltungsfehler. Das Werkzeug wählt die Seite selbst (`bubble()` in `bilder_symbol.py`). Beispiel Kana: «Der Wein ist ausgegangen» = leerer Krug mit Traubenzeichen + leerer Becher + «fehlt»; «Hört auf ihn» = Jesus → Ohr.
- **Mehrzahl** («ihr», «die Leute») in Sprechblasen als Gruppe von drei Figuren, nie als einzelne Figur (Blindtest: eine Figur wird als «dieser eine» gelesen).
- **Gott als Absender:** Spricht ein Prophet in Gottes Auftrag, steht der Strahlenkranz über ihm mit einer goldenen Linie zum Propheten; der Gottesname gehört dann nicht in die Sprechblase (Blindtest: dort wird er als Inhalt gelesen).
- **Zeichen** (Stern = Zeichen/σημεῖον, Herz mit Lichtstrahl = glauben, Sanduhr = Stunde/Zeit, Sonnen = Anzahl Tage, Tempel mit Riss = niederreissen, gestrichelte Linie = Abstand …) kommen nur aus dem Lexikon und behalten überall dieselbe Bedeutung.
- **Gott** nie als Mensch, ohne Gesicht oder Körper. Zeichen (Entscheid Andi Neck, 2026-10-14): **goldener Strahlenkranz mit dem Gottesnamen יהוה** in hebräischen Buchstaben, wie seit der Reformation in reformierten und lutherischen Kirchen. Gott soll als Gegenüber erscheinen: Wo möglich spricht er (Sprechblase mit Spitze zum Strahlenkranz) oder ist Adressat einer Rede. Ohne Sprechblase über einer Szene wird der Strahlenkranz leicht als Sonne gelesen (Blindtest); deshalb keine Sonne oder Lichtscheibe in derselben Szene. Der Kreuznimbus über einer menschlichen Figur bleibt Jesus vorbehalten.
- **Heiliger Geist:** weisse Taube mit goldenem Schein im Sturzflug (Kopf unten, Schwanzfächer oben); die Taube als Tier (Opfertier) nie mit Schein, sitzend oder im Käfig.
- **Personen** im Stil «Symbol» ohne ausgeführtes Gesicht (im Stil «Anime» mit Gesicht und Ausdruck, siehe oben), erkennbar an Farbe, Kleidung und Zeichen. Keine Karikatur, keine «typisierten» Merkmale einer Volksgruppe; «die Juden» im Johannesevangelium als neutrale Menge, nie eingefärbt oder vereinheitlicht.
- Was der Text offenlässt (z. B. ob die Geissel Menschen traf, [[JHN.2.15]]), bleibt im Bild offen oder wird im Auftrag (`interpretation_note_de`) als Deutung benannt. Nicht erzählte Vorgänge (der Wechsel von Wasser zu Wein) werden nicht als Vorgang gezeigt.
- Symbole, die an nationale, politische oder kirchliche Sonderzeichen erinnern, vermeiden (z. B. Adler nicht mit weissem Kopf und Schwanz).

## Zeichner für alle Stellen (seit v0.65)

Für die Bücher, Kapitel und Abschnitte aller übersetzten Bücher setzt der Zeichner `scripts/authoring/bilder_auto.py` die Bilder in beiden Stilen direkt aus dem Bildauftrag zusammen; nur Johannes 2 und die oberen Ebenen (Bibel, Testamente, Buchgruppen) sind von Hand gezeichnet. Bausteine:
- **Figurenbaukasten** `scripts/authoring/figuren.py` (plus `figuren_daten/`): Aussehen jeder Person, Rolle und Gruppe aus dem Lexikon (Farben, Haar, Bart, Kopfbedeckung, Alter, Attribut) – im Stil «Symbol» als Ganzfigur, im Stil «Anime» als Brustbild mit denselben Farben.
- **Bauteile** `scripts/authoring/bildsymbole.py` (plus `bildsymbole_daten/`): Zeichnungen für Orte, Gegenstände und Zeichen; der Stil «Anime» übernimmt sie.
- **Handlungslinien** (goldener Bogen: Gott sendet, sieht, bestimmt; gepunkteter Bogen: werfen, speien; gestrichelter Weg: gehen) machen sichtbar, was geschieht; Kleidung kann wechseln (Sacktuch bei der Busse).
- Wer zu Gott spricht, betet mit gefalteten Händen (kein erhobener Arm, der drohend wirkt); wer zu Menschen spricht, öffnet die Hand nach vorn.
- Ein Schiff steht immer im Wasser; wer in einem Fisch oder Grab ist, erscheint in einem Fenster.
Wie man Aufträge dafür schreibt: [BILDAUFTRAEGE-ANLEITUNG.md](BILDAUFTRAEGE-ANLEITUNG.md).

## Ebenen

Bilder gibt es auf allen Ebenen über den Versen: Bibel, Testamente, Buchgruppen, Buch, Kapitel, Abschnitt. Bildaufträge der oberen Ebenen (Bibel, Testament, Buchgruppe) haben keine Bibelstelle als Ganzes; ihr Ziel ist die Zusammenfassung (`SUM-BIBLE`, `SUM-OT`, `SUM-NT`, `SUM-GROUP-xx`), und jedes Bildfeld nennt eine typische Stelle (z. B. [[EXO.14]] für die Befreiung). Gleiche Szenen sehen auf allen Ebenen gleich aus (z. B. Sinai in Bibel, Altem Testament und Tora). Stand 2026-10-17, in beiden Stilen: Bibel, beide Testamente, alle zehn Buchgruppen sowie Buch, Kapitel und Abschnitte aller übersetzten Bücher.

## Prüfung auf Verständlichkeit (Blindtest)

1. Bild rendern (PNG).
2. Eine getrennte KI-Instanz beschreibt es **ohne** Bildauftrag, nur mit der Legende, wie sie die App zeigt: wer, wer zu wem, was gesagt/getan, Sicherheit; dazu alles Unklare.
3. Beschreibung mit dem Auftrag vergleichen. Weicht sie bei Handelnden, Wer-zu-wem, Handlung oder Reihenfolge ab, Symbol oder Anordnung nachbessern und erneut prüfen.
4. Die Testseite für das Rendern braucht `<meta charset="utf-8">`, sonst erscheint der Gottesname als Zeichensalat (Fehler der Testseite, nicht der App).
5. Ergebnis in `check` des Bild-Datensatzes (`date`, `method_de`, `result_de`, `open_de`, `limits_de`). Der Blindtest ist die Beschreibung einer einzelnen KI-Instanz und ersetzt keine Prüfung mit Leserinnen und Lesern und keine fachliche Prüfung.

## Synchron mit dem Text

Jeder Bildauftrag speichert in `basis` Fingerabdrücke der Verse je Bildfeld (aus der angegebenen Übersetzung) und der Zusammenfassung seines Ziels. Ändert sich der Text, meldet `scripts/validate.py` «Bildauftrag veraltet». Dann:

1. Auftrag und Bild gegen den neuen Text prüfen und nötigenfalls anpassen (Auftrag, Lexikon, Zeichnung, Bildbeschreibung in allen Sprachen).
2. Blindtest wiederholen, falls sich das Bild geändert hat.
3. Bestätigen: `BIBLE_REVISION_DATE=… BIBLE_REVISION_REASON="…" BIBLE_BRIEF_CONFIRM=1 python3 scripts/authoring/bildauftraege.py`.

Ohne `BIBLE_BRIEF_CONFIRM=1` schreibt das Werkzeug die alten Fingerabdrücke zurück, damit ein veralteter Auftrag nicht stillschweigend als geprüft gilt. Wird ein Lexikon-Eintrag geändert, alle Bilder mit dieser Figur neu zeichnen und prüfen.
