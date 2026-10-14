# Bildsprache

Bilder fassen auf den Zoomstufen (Buch, Kapitel, Abschnitt) bildlich, was die Zusammenfassung in Worten sagt. Sie sind **Deutung, nicht Text**: Sie legen mehr fest als der Text (Kleidung, Anordnung, Gewichtung), stehen neben der Zusammenfassung und ersetzen sie nicht. Die App kennzeichnet jedes Bild entsprechend («Legende und Hinweise»). Datenfelder: [DATENMODELL.md](DATENMODELL.md#bildsprache-seit-v055-lexikon-und-bildaufträge-seit-v056).

## Drei Schichten

1. **Bildlexikon** (`data/illustrations/lexicon/FIG-*.json`, stilunabhängig): Wer oder was ist das, woran erkennt man es (Pflichtmerkmale mit Grundlage: Text, Tradition oder eigene Gestaltung), womit darf es nicht verwechselt werden. Gilt für die ganze Bibel; so trägt Maria überall Blau, Jesus überall den Kreuznimbus, ein Diener überall die Schürze. Werkzeug: `scripts/authoring/bildlexikon.py`.
2. **Bildauftrag** je Stelle (`data/illustrations/briefs/BRIEF-*.json`, stilunabhängig): Bildfelder in Reihenfolge, je Feld Stelle, Figuren, Gegenstände, Zeichen, Sprechblasen (wer zu wem, mit welchen Zeichen) und die Handlung in einem Satz. Der Auftrag wird wie eine Zusammenfassung gegen den Text geprüft (Handelnde, Wer-zu-wem, Zeitform, Ankündigung statt Bericht). Werkzeug: `scripts/authoring/bildauftraege.py`.
3. **Stil** (`data/illustrations/styles/ILLSTYLE-*.json`): wie dieser Stil jeden Lexikon-Eintrag zeichnet (`renderings`). Stil «Symbol»: eigene SVG-Bibliothek (`data/illustrations/symbol/_bibliothek.svg`), Bilder in `scripts/authoring/bilder_symbol.py` aus den Bauteilen zusammengesetzt. Spätere Stile (Skizze, Anime, Malerei) zeichnen dieselben Aufträge mit denselben Pflichtmerkmalen; bei Bildgeneratoren mit Figurenblättern und Referenzbildern je Lexikon-Eintrag, damit Figuren über Bilder hinweg gleich bleiben.

## Gestaltungsregeln

- **Handlungen:** mehrere Schritte als nummerierte Bildfelder; Gesagtes als Sprechblase mit Zeichen statt Wörtern, die Spitze zeigt auf die sprechende Figur, die Geste (Arm) auf die angesprochene. Beispiel Kana: «Der Wein ist ausgegangen» = leerer Krug mit Traubenzeichen + leerer Becher + «fehlt»; «Hört auf ihn» = Jesus → Ohr.
- **Zeichen** (Stern = Zeichen/σημεῖον, Herz mit Lichtstrahl = glauben, Sanduhr = Stunde/Zeit, Sonnen = Anzahl Tage, Tempel mit Riss = niederreissen, gestrichelte Linie = Abstand …) kommen nur aus dem Lexikon und behalten überall dieselbe Bedeutung.
- **Gott** nie als Mensch, ohne Gesicht oder Körper; der Kreuznimbus über einer menschlichen Figur bleibt Jesus vorbehalten. Das Gottessymbol soll einprägsam sein und Gott als Gegenüber (handelnd, sprechend) zeigen, nicht als Naturerscheinung. *Offen:* Die bisherige «segnende Hand aus der Wolke» war nicht verständlich genug; ein neues Zeichen ist noch zu wählen.
- **Heiliger Geist:** weisse Taube mit Lichtschein, von oben kommend; die Taube als Tier (Opfertier) nie mit Schein, sitzend oder im Käfig.
- **Personen** ohne ausgeführtes Gesicht, erkennbar an Farbe, Kleidung und Zeichen. Keine Karikatur, keine «typisierten» Merkmale einer Volksgruppe; «die Juden» im Johannesevangelium als neutrale Menge, nie eingefärbt oder vereinheitlicht.
- Was der Text offenlässt (z. B. ob die Geissel Menschen traf, [[JHN.2.15]]), bleibt im Bild offen oder wird im Auftrag (`interpretation_note_de`) als Deutung benannt. Nicht erzählte Vorgänge (der Wechsel von Wasser zu Wein) werden nicht als Vorgang gezeigt.
- Symbole, die an nationale, politische oder kirchliche Sonderzeichen erinnern, vermeiden (z. B. Adler nicht mit weissem Kopf und Schwanz).

## Prüfung auf Verständlichkeit (Blindtest)

1. Bild rendern (PNG).
2. Eine getrennte KI-Instanz beschreibt es **ohne** Bildauftrag, nur mit der Legende, wie sie die App zeigt: wer, wer zu wem, was gesagt/getan, Sicherheit; dazu alles Unklare.
3. Beschreibung mit dem Auftrag vergleichen. Weicht sie bei Handelnden, Wer-zu-wem, Handlung oder Reihenfolge ab, Symbol oder Anordnung nachbessern und erneut prüfen.
4. Ergebnis in `check` des Bild-Datensatzes (`date`, `method_de`, `result_de`, `open_de`, `limits_de`). Der Blindtest ist die Beschreibung einer einzelnen KI-Instanz und ersetzt keine Prüfung mit Leserinnen und Lesern und keine fachliche Prüfung.

## Synchron mit dem Text

Jeder Bildauftrag speichert in `basis` Fingerabdrücke der Verse je Bildfeld (aus der angegebenen Übersetzung) und der Zusammenfassung seines Ziels. Ändert sich der Text, meldet `scripts/validate.py` «Bildauftrag veraltet». Dann:

1. Auftrag und Bild gegen den neuen Text prüfen und nötigenfalls anpassen (Auftrag, Lexikon, Zeichnung, Bildbeschreibung in allen Sprachen).
2. Blindtest wiederholen, falls sich das Bild geändert hat.
3. Bestätigen: `BIBLE_REVISION_DATE=… BIBLE_REVISION_REASON="…" BIBLE_BRIEF_CONFIRM=1 python3 scripts/authoring/bildauftraege.py`.

Ohne `BIBLE_BRIEF_CONFIRM=1` schreibt das Werkzeug die alten Fingerabdrücke zurück, damit ein veralteter Auftrag nicht stillschweigend als geprüft gilt. Wird ein Lexikon-Eintrag geändert, alle Bilder mit dieser Figur neu zeichnen und prüfen.
