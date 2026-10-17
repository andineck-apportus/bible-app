# Bildsprache

Bilder fassen auf den Zoomstufen (Buch, Kapitel, Abschnitt) bildlich, was die Zusammenfassung in Worten sagt. Sie sind **Deutung, nicht Text**: Sie legen mehr fest als der Text (Kleidung, Anordnung, Gewichtung), stehen neben der Zusammenfassung und ersetzen sie nicht. Die App kennzeichnet jedes Bild entsprechend («Legende und Hinweise»). Datenfelder: [DATENMODELL.md](DATENMODELL.md#bildsprache-seit-v055-lexikon-und-bildaufträge-seit-v056).

## Drei Schichten

1. **Bildlexikon** (`data/illustrations/lexicon/FIG-*.json`, stilunabhängig): Wer oder was ist das, woran erkennt man es (Pflichtmerkmale mit Grundlage: Text, Tradition oder eigene Gestaltung), womit darf es nicht verwechselt werden. Gilt für die ganze Bibel; so trägt Maria überall Blau, Jesus überall den Kreuznimbus, ein Diener überall die Schürze. Werkzeug: `scripts/authoring/bildlexikon.py`.
2. **Bildauftrag** je Stelle (`data/illustrations/briefs/BRIEF-*.json`, stilunabhängig): Bildfelder in Reihenfolge, je Feld Stelle, Figuren, Gegenstände, Zeichen, Sprechblasen (wer zu wem, mit welchen Zeichen) und die Handlung in einem Satz. Der Auftrag wird wie eine Zusammenfassung gegen den Text geprüft (Handelnde, Wer-zu-wem, Zeitform, Ankündigung statt Bericht). Werkzeug: `scripts/authoring/bildauftraege.py`.
3. **Stil** (`data/illustrations/styles/ILLSTYLE-*.json`): wie dieser Stil jeden Lexikon-Eintrag zeichnet (`renderings`). Stil «Symbol»: eigene SVG-Bibliothek (`data/illustrations/symbol/_bibliothek.svg`), Bilder in `scripts/authoring/bilder_symbol.py` aus den Bauteilen zusammengesetzt. Stil «Anime» (Pilot seit v0.61, bisher [[JHN.2.1-JHN.2.12]]): comicartig ohne Text, Personen mit Gesicht und Ausdruck, Manga-Panels mit schrägen Rändern, Bewegungs- und Emotionszeichen (Schweisstropfen = Sorge, Strichkranz = Staunen, Funkeln = Freude); Werkzeug `scripts/authoring/bilder_anime.py`, Bibliothek `data/illustrations/anime/_bibliothek.svg` (Gegenstände und Zeichen aus dem Symbolstil übernommen, damit sie in beiden Stilen gleich gelesen werden). Fehlt ein Bild im gewählten Stil, zeigt die App das Symbolbild. Weitere Stile (Skizze, Malerei) zeichnen dieselben Aufträge mit denselben Pflichtmerkmalen; bei Bildgeneratoren mit Figurenblättern und Referenzbildern je Lexikon-Eintrag, damit Figuren über Bilder hinweg gleich bleiben.

## Bildsprachen je Kultur und Sprache (vorgemerkt)

Bilder ohne Text taugen vorerst für alle Sprachen. Später soll es Bildsprachen je Kultur geben, nach demselben Muster wie die Übersetzungsschichten (eigene Schicht mit `target_context`, nie stillschweigend abgeleitet):
- **Stil mit Zielkontext:** ein `illustration_style` kann `target_context` und `language` tragen (z. B. ein Stil für Westafrika oder für Kinder in der Schweiz); die App wählt nach Sprache bzw. Leserkontext.
- **Zeichen, die kulturell verschieden gelesen werden** (Gesten, Farben von Trauer und Freude, Herz, Daumen, Leserichtung der Panels von links oder rechts), als Varianten am Lexikon-Eintrag mit Kontext und Begründung; der Bildauftrag bleibt gleich.
- **Prüfung** durch Menschen aus dem jeweiligen Kontext eintragen, nicht behaupten; der KI-Blindtest ersetzt sie nicht.

## Gestaltungsregeln

- **Handlungen:** mehrere Schritte als nummerierte Bildfelder; Gesagtes als Sprechblase mit Zeichen statt Wörtern, die Spitze zeigt auf die sprechende Figur, die Geste (Arm) auf die angesprochene. Die Blase steht möglichst direkt über der sprechenden Figur; steht sie daneben (z. B. beim Strahlenkranz), geht die Spitze von der zugewandten Seite aus (links, rechts, oben oder unten). Die Spitze ist kurz und gerade; eine lange, schräg verzogene Spitze ist ein Gestaltungsfehler. Das Werkzeug wählt die Seite selbst (`bubble()` in `bilder_symbol.py`). Beispiel Kana: «Der Wein ist ausgegangen» = leerer Krug mit Traubenzeichen + leerer Becher + «fehlt»; «Hört auf ihn» = Jesus → Ohr.
- **Zeichen** (Stern = Zeichen/σημεῖον, Herz mit Lichtstrahl = glauben, Sanduhr = Stunde/Zeit, Sonnen = Anzahl Tage, Tempel mit Riss = niederreissen, gestrichelte Linie = Abstand …) kommen nur aus dem Lexikon und behalten überall dieselbe Bedeutung.
- **Gott** nie als Mensch, ohne Gesicht oder Körper. Zeichen (Entscheid Andi Neck, 2026-10-14): **goldener Strahlenkranz mit dem Gottesnamen יהוה** in hebräischen Buchstaben, wie seit der Reformation in reformierten und lutherischen Kirchen. Gott soll als Gegenüber erscheinen: Wo möglich spricht er (Sprechblase mit Spitze zum Strahlenkranz) oder ist Adressat einer Rede. Ohne Sprechblase über einer Szene wird der Strahlenkranz leicht als Sonne gelesen (Blindtest); deshalb keine Sonne oder Lichtscheibe in derselben Szene. Der Kreuznimbus über einer menschlichen Figur bleibt Jesus vorbehalten.
- **Heiliger Geist:** weisse Taube mit goldenem Schein im Sturzflug (Kopf unten, Schwanzfächer oben); die Taube als Tier (Opfertier) nie mit Schein, sitzend oder im Käfig.
- **Personen** ohne ausgeführtes Gesicht, erkennbar an Farbe, Kleidung und Zeichen. Keine Karikatur, keine «typisierten» Merkmale einer Volksgruppe; «die Juden» im Johannesevangelium als neutrale Menge, nie eingefärbt oder vereinheitlicht.
- Was der Text offenlässt (z. B. ob die Geissel Menschen traf, [[JHN.2.15]]), bleibt im Bild offen oder wird im Auftrag (`interpretation_note_de`) als Deutung benannt. Nicht erzählte Vorgänge (der Wechsel von Wasser zu Wein) werden nicht als Vorgang gezeigt.
- Symbole, die an nationale, politische oder kirchliche Sonderzeichen erinnern, vermeiden (z. B. Adler nicht mit weissem Kopf und Schwanz).

## Ebenen

Bilder gibt es auf allen Ebenen über den Versen: Bibel, Testamente, Buchgruppen, Buch, Kapitel, Abschnitt. Bildaufträge der oberen Ebenen (Bibel, Testament, Buchgruppe) haben keine Bibelstelle als Ganzes; ihr Ziel ist die Zusammenfassung (`SUM-BIBLE`, `SUM-OT`, `SUM-NT`, `SUM-GROUP-xx`), und jedes Bildfeld nennt eine typische Stelle (z. B. [[EXO.14]] für die Befreiung). Gleiche Szenen sehen auf allen Ebenen gleich aus (z. B. Sinai in Bibel, Altem Testament und Tora). Stand 2026-10-14: Bibel, beide Testamente, alle zehn Buchgruppen; Buch nur Johannes; Kapitel und Abschnitte nur Johannes 2.

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
