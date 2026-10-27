# Pilot: malerische Bilder (Johannes 2)

Ziel: prüfen, ob generierte Bilder den Anspruch erfüllen – künstlerischer Wert, schön anzusehen, stimmige Proportionen und Räume, emotional – und dabei so genau steuerbar bleiben wie die bisherigen Bildaufträge. Der Pilot steht ausserhalb von `data/` und ist nicht Teil der App.

## Wie es aufgebaut ist

Die bestehende Bildkette bleibt die Grundlage; neu dazu kommen Regie, Kompositionsvorlage und Stil:

1. **Bildauftrag** (`data/illustrations/briefs/`) und **Bildlexikon**: was zu sehen ist, wer zu wem, Pflichtmerkmale (Maria blau, Jesus weiss/rot mit Kreuznimbus, Speisemeister grün mit Goldgürtel …).
2. **Regie** (`szenen.json`): je Szene Stimmung und emotionaler Kern, Licht, Kamerastandpunkt, Hintergrund und was zu vermeiden ist. Fünf Szenen:
   - A «Sie haben keinen Wein mehr» (2,1–4)
   - B «Füllt die Krüge mit Wasser» (2,6–8)
   - C «Du hast den guten Wein bis jetzt aufbewahrt» (2,9–11)
   - D Tempelreinigung (2,14–16)
   - E «Reisst diesen Tempel nieder» (2,18–21)
3. **Kompositionsvorlage** (`vorlagen/*.png`, erzeugt mit `vorlagen.py`): grobe Tiefenkarte (hell = nah), die festlegt, wo wer steht und wie der Raum aufgebaut ist. Das Modell «tiefe» hält sich daran.
4. **Stil** (`stile.json`): drei Richtungen zum Vergleich – Helldunkel in Öl, Aquarell und Tusche, Farbholzschnitt.
5. **Erzeugung** (`generate.py`): setzt die Prompts zusammen, ruft die Replicate-API auf und schreibt Bilder, `lauf.json` (Prompt, Modell, Seed) und einen `kontaktbogen.html` zum Vergleichen.

## Starten

Einmalig: Bei [replicate.com](https://replicate.com) ein Konto anlegen, unter «API tokens» ein Token erzeugen und im Repo unter *Settings → Secrets and variables → Actions* als `REPLICATE_API_TOKEN` speichern.

Dann: *Actions → bildpilot → Run workflow* (geht auch in der GitHub-App auf dem Smartphone). Voreingestellt sind alle fünf Szenen in allen drei Stilen mit Kompositionsvorlage, also 15 Bilder. Die Bilder liegen danach als Download beim Lauf und auf dem Branch `bildpilot-ausgabe` im Ordner `ausgabe/<lauf>/`.

Lokal geht es auch: `REPLICATE_API_TOKEN=… python3 pilot/malerisch/generate.py` (ohne Token mit `--trocken` nur die Prompts anzeigen).

Kosten: Abrechnung pro Bild nach Replicate-Preisliste; ein voller Lauf mit 15 Bildern liegt in der Grössenordnung von unter einem Franken. «schnell» kostet nur einen Bruchteil davon und eignet sich für Vorversuche.

## Lizenz und Kennzeichnung

- KI-generierte Bilder sind in der Regel nicht urheberrechtlich geschützt; das passt zu CC0. Die Nutzungsbedingungen des gewählten Modells müssen die Verwendung erlauben (FLUX.1 [schnell]: Apache 2.0; die Pro-Modelle über die API erlauben die Nutzung der Ergebnisse). Vor einer Übernahme in `data/` gehören Modell und Bedingungen in den Quellenkatalog und nach `LIZENZEN.md`.
- Die Prompts nennen bewusst keine lebenden Künstler, sondern beschreiben Technik und Tradition.
- Bilder bleiben bildliche Deutung und werden in der App so gekennzeichnet.

## Entscheide

- **Gesichter** (Andi Neck, 2026-10-27): Alle Menschen mit Gesicht und Ausdruck, auch Jesus – er ist Mensch geworden; ein verdecktes oder reduziertes Gesicht wirkt abstossend.

## Offene Entscheide

- **Steinkrüge:** Joh 2,6 nennt steinerne Krüge zu zwei bis drei Mass. Der Lexikon-Eintrag «Krug mit Wasser» zeigt einen verzierten Tonkrug. Die Regie folgt dem Text; das Lexikon sollte nachgezogen werden.
- **Stil:** welche der drei Richtungen (oder eine Mischung) weiterverfolgt wird.

## Wenn der Pilot überzeugt

1. Stil festlegen und ein Stil-LoRA auf einem kleinen, freien Referenzset trainieren, damit alle Bilder aus einem Guss sind.
2. Figurenblätter für die Hauptfiguren (Referenzbilder je Lexikon-Eintrag), damit Jesus, Maria, Petrus … über alle Bilder gleich bleiben.
3. Regie für alle Bildaufträge ergänzen, Kompositionsvorlagen aus dem bestehenden Szenenaufbau (`bilder_auto.py`) ableiten.
4. Kuratierung: mehrere Varianten je Auftrag, Vorauswahl mit KI-Bildprüfung (Inhalt gegen Bildauftrag, Hände, Proportionen), Endauswahl durch einen Menschen; dann als neuer Stil `ILLSTYLE-MALEREI` in die App.
