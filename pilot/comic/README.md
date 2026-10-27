# Pilot: Comic-Seite je Abschnitt (Johannes 2)

Anlass: Eine Comic-Seite von ChatGPT zu Kana (Stil «reduzierter Aquarell-Comic») erzählte die Geschichte in Bildfeldern mit Sprechblasen – lesbar, erwachsen, mit gleichbleibenden Figuren innerhalb der Seite. Andi Neck hat Stil 4 gewählt (2026-10-27).

Je Abschnitt entsteht eine Seite aus Lesetext, Bildauftrag (Pflichtmomente in Reihenfolge) und Figurenblatt (`figuren.json`: Aussehen nach Bildlexikon, dazu Alter und Unterscheidungsmerkmale). Gegenüber der ChatGPT-Vorlage verbessert: Maria eine Generation älter als Jesus, Speisemeister, Diener und Bräutigam klar unterscheidbar, steinerne Krüge nach Joh 2,6, Rot nur für Jesus, Jesus und die Jünger im Schlussbild.

Varianten: `leer` (Sprechblasen ohne Text – die App setzt den Text in der Sprache des Lesers darüber), `de`, `gsw`.

Start: Actions → «bildpilot-comic» → Run workflow (Secret `OPENAI_API_KEY`). Lokal: `OPENAI_API_KEY=… python3 pilot/comic/comic.py`, ohne Schlüssel mit `--trocken` nur die Prompts.
