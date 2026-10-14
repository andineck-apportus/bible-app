# Changelog

Änderungen am Bibel-Wissensfundus. Die Einträge v0.1–v0.5 sind aus den vorhandenen Paketen rekonstruiert; sie sind keine Behauptung über ursprüngliche Veröffentlichungsdaten. Alle fünf Pakete wurden am 8. Oktober 2026 nach GitHub übernommen. Der aktuelle Einstieg und die Bedienung stehen in [README.md](README.md), offene Arbeiten in [Status und Roadmap](docs/STATUS-UND-ROADMAP.md).

## v0.57 — 2026-10-14 — Bildsprache auf allen Ebenen, Gottessymbol

- **Bilder auf allen Ebenen über den Versen:** neu für die ganze Bibel, Altes und Neues Testament und alle zehn Buchgruppen (je ein bis vier Bildfelder nach der Zusammenfassung, mit einer typischen Bibelstelle je Feld). Gleiche Szenen sehen überall gleich aus (Schöpfung, Meerdurchzug, Sinai, Exil und Hoffnung, Verkündigung Jesu, Kreuz und leeres Grab, Pfingsten, Briefe, neue Schöpfung).
- **Gottessymbol:** goldener Strahlenkranz mit dem Gottesnamen יהוה (Entscheid Andi Neck), möglichst als Sprechender gezeigt (z. B. «Es werde Licht», die Weisung am Sinai). Die Hand aus der Wolke entfällt.
- **13 neue Lexikon-Einträge** (u. a. Gesetzestafeln, Meer, Schöpfung, Prophet, Leier, Hoffnung, Umkehr, Gericht, neue Schöpfung, Exil und Rückkehr, Ausbreitung, Brief, Gemeinde) und Darstellungen für Gott, Heiligen Geist, Mose, Paulus, König, Soldat, Kreuz, Grab, Jerusalem, Berg, Haus, Weg, Boot, Beten und Trauer. Mose trägt die Tafeln erst ab dem Sinai.
- **Blindtest** (zwei Runden) für alle neuen Bilder; nach den Befunden u. a. Taube im Sturzflug statt «Lilie», keine Sonne mehr beim leeren Grab, Tränen neben den Köpfen, Gott spricht am Sinai, Prophet den Menschen zugewandt. Ergebnisse und offene Punkte in den Bild-Datensätzen.
- Legende: Stellenangaben auch für ganze Kapitel und Bereiche über Kapitel («2. Mose 19–34»).

## v0.56 — 2026-10-14 — Bildlexikon, Bildaufträge, Blindtest

- **Bildlexikon** (142 Einträge, stilunabhängig): Personen, Rollen, Gruppen, Gegenstände, Orte, Handlungs- und Bedeutungszeichen mit Pflichtmerkmalen (Grundlage Text, Tradition oder Gestaltung), Verwechslungsregeln und Mundart. Dieselbe Figur sieht in jedem Bild und später in jedem Stil gleich aus.
- **Bildaufträge** je Stelle (stilunabhängig): Bildfelder, wer zu wem spricht (Sprechblasen mit Zeichen), Handlung je Feld; geprüft gegen den Text wie eine Zusammenfassung. Korrigiert: In Kana spricht Maria zu den **Dienern** ([[JHN.2.5]]).
- **Synchron mit dem Text:** Fingerabdrücke der Verse und Zusammenfassungen im Auftrag; der Validator meldet «Bildauftrag veraltet», wenn sich der Text ändert. Bestätigung nur nach erneuter Prüfung (`BIBLE_BRIEF_CONFIRM=1`).
- **Bilder neu gezeichnet** (Johannes, Johannes 2, 2,1–12, 2,13–22, 2,23–25): u. a. leerer Weinkrug mit Traubenzeichen und leerer Becher für «kein Wein mehr», Ohr für «hört auf ihn», Diener giessen Wasser ein, Speisemeister spricht zum Bräutigam, Stern über Jesus und glaubende Jünger; Tempel mit Riss → drei Sonnen → Tempel für «in drei Tagen»; Tauben im Käfig, Becher ohne Fuss, Kranz statt Krone, brauner Adler.
- **Blindtest auf Verständlichkeit** in zwei Runden (getrennte KI-Instanz, nur Bild und Legende); Ergebnis und offene Punkte im Bild-Datensatz und im Legendenblatt. Kein Test mit Menschen.
- **Legende** nach Lexikon: Figuren und Zeichen nach Art sortiert, Bildfelder mit Handlung, Prüfergebnis.
- **Umschalter Text/Bild** auf dem Handy als kleine Symbolknöpfe neben «Verstehen»/«Geschichte».
- **Schema v0.11:** neue Typen `figure` und `illustration_brief` (ohne Migration); Stil mit `renderings` statt eigener Figurenliste. Regeln in AGENTS.md (Lexikon, Bildauftrag, Blindtest, Synchronität) und [docs/BILDSPRACHE.md](docs/BILDSPRACHE.md).
- Offen: ein verständlicheres Gottessymbol (die Hand aus der Wolke wird ersetzt).

## v0.55 — 2026-10-14 — Bildsprache (Stil «Symbol»)

- **Bilder auf den Zoomstufen:** Zu Buch, Kapitel und Abschnitt kann es Bilder geben; auf breiten Bildschirmen (ab 760 px) stehen Text und Bild nebeneinander, auf dem Handy schaltet «Text | Bild» für alle Einträge um. «Legende und Hinweise» öffnet ein Blatt mit Bildbeschreibung, den gezeigten Figuren und dem Hinweis, was das Bild deutet. Im Menü: «Bilder» – Aus oder ein Stil; weitere Stile (z. B. Skizze, Anime) sind vorgesehen.
- **Stil «Symbol»** mit festen Figuren (Jesus mit Kreuznimbus, Maria in Blau, Jünger, Braut, Bräutigam, Gäste, Diener, Speisemeister, Händler, Zeichen) und wiederverwendeten Szenen; erste Bilder: Johannesevangelium (Adler, Licht, Buch), Kapitel 2 (drei Felder) und die Abschnitte 2,1–12, 2,13–22, 2,23–25. Eigene Zeichnungen (CC0), KI-Entwurf, nicht geprüft.
- **Schema v0.10:** neue Typen `illustration_style` und `illustration` (ohne Migration), Validator-Prüfungen, Werkzeug `scripts/authoring/bilder_symbol.py`.

## v0.54 — 2026-10-14 — Gottesname beim Vorlesen

- Beim Vorlesen wird JHWH als «Jahwe» gesprochen (Einstellung im Menü: «Jahwe» oder «Adonai»); der geschriebene Text bleibt JHWH. Hinweis im Menü zur jüdischen Tradition, den Namen nicht auszusprechen.

## v0.53 — 2026-10-14 — Anhören: anhalten, Aussprache auch für Hebräisch

- Alle Anhören-Knöpfe (Wörter, Proben) zeigen während der Wiedergabe das Pausenzeichen; ein erneuter Klick hält an. Läuft gerade das Vorlesen, wird es dabei angehalten. «Vorlesen probehören» als runder Knopf wie die übrigen (kein Zeilenumbruch mehr).
- Aussprache-Einstellung gilt jetzt für Griechisch und Hebräisch: «Heutig» (Gerätestimme Neugriechisch bzw. Neuhebräisch) oder «Schulaussprache» (Umschrift, deutsche Stimme); Aramäisch immer über die Umschrift. Stimmenwahl je Sprache (Griechisch, Hebräisch bzw. Stimme für die Umschrift); Proben für Griechisch, Hebräisch und Aramäisch.
- Hinweis zu besseren Stimmen um Mac und Chrome ergänzt.

## v0.52 — 2026-10-14 — Sprachprüfung aller Übersetzungen und Zusammenfassungen

- **Neue Regel** (AGENTS.md): Nach der inhaltlichen Prüfung folgt bei jeder Arbeit eine sprachliche Prüfung in allen Sprachen und Übersetzungsschichten; Bibeltext nur so weit geglättet, wie Treue zum Urtext, Zeitform, Satzart und Wortzuordnung erhalten bleiben. Autorenwerkzeuge übernehmen Datum und Grund einer Überarbeitung aus `BIBLE_REVISION_DATE`/`BIBLE_REVISION_REASON`.
- **Erster Durchgang** (KI, getrennt nach Büchern) über Bibeltext, Titel und Zusammenfassungen aller Zoomstufen in Hochdeutsch und Züridüütsch: Johannes, Markus, Rut, Obadja, Jona, Philipper, Titus, 1–3 Johannes, Vaterunser sowie Bibel, Testamente, Buchgruppen und alle Buchzusammenfassungen. Korrigiert u. a. altertümliche Wendungen («heisst ihn … tun», «allezeit»), Nominal- und Partizipialstil, Wortstellung, Kongruenz, Fälle, Zeichensetzung, unklare Bezüge, hochdeutsche Muster und Genitive in der Mundart, Mundart-Schreibung; vereinzelt Wiedergabe genauer gefasst (z. B. Ankündigung statt Bericht). Mehrere Hundert Stellen; frühere Fassungen im revision_log.
- Offen: Mundart-Schreibung zwischen Büchern und zwischen Text- und Studienwerkzeugen weiter uneinheitlich (z. B. sig/seg, det/dört, Erzäller/Erzäler) – Festlegung durch eine muttersprachliche Person nötig; Vorschläge für die gesperrten Vaterunser- und Mk-3-Datensätze stehen im Bericht der Sprachprüfung.

## v0.51 — 2026-10-14 — Johannes: Zusammenfassungen sprachlich korrigiert

- Kana (Kapitel 2 und Abschnitt 2,1–12): wie in 2,3–5 wiedergegeben («Sie haben keinen Wein mehr» – «seine Stunde sei noch nicht gekommen» – die Mutter sagt den Dienern, sie sollen tun, was er ihnen sagt), statt «heisst die Diener tun» und ohne deutendes «doch». Ebenso 4,16 und 5,8 ohne «heissen + Grundform». Mundart angeglichen; frühere Fassungen im revision_log.

## v0.50 — 2026-10-14 — Vorlesen natürlicher

- **Zusammenhängend lesen:** Verse bis zum nächsten Titel werden als ein Text übergeben und nur an echten Satzenden geteilt (nicht nach Abkürzungen, Zahlen, «:» oder «;»), damit die Satzmelodie über Versgrenzen läuft; überlange Sätze werden an «;», «:» bzw. Kommas geteilt. Anzeige und Markierung folgen dem Vers, in dem der gesprochene Abschnitt beginnt, und, wo die Stimme es meldet, Wort für Wort.
- **Vorlesestimme:** «Auto» wählt die vermutlich natürlichste deutsche Stimme des Geräts (Premium, Natural, Erweitert, Google vor Kompakt- und Effektstimmen); im Menü eigene Auswahl, Vorlesetempo (Ruhig, Normal, Zügig, getrennt vom Tempo für Ursprachwörter), Probehören und Hinweis, wo sich bessere Stimmen installieren lassen.
- Vorgemerkt: Vertonung mit neuronalen Cloud-Stimmen (siehe Status und Roadmap).

## v0.49 — 2026-10-14 — Vorlesen: Titel, Pausen, Startknopf als Pause

- Titel werden als eigener, etwas leiser und langsamer gesprochener Satz gelesen, mit kurzer Pause davor und danach; ohne Schlusspunkt, damit «Johannes 2» nicht als «Johannes zweiter» gelesen wird.
- Buchnummern als Ordnungszahl: «1. Johannes 3» → «Erster Johannes drei», «2. Mose» → «Zweites Buch Mose» (englisch «First John»); auch in Bibelstellen der Zusammenfassungen.
- Der Startknopf des gerade gelesenen Titels zeigt wie der Player das Pausenzeichen; ein Klick darauf hält an bzw. liest weiter.

## v0.48 — 2026-10-14 — Vorlesen

- **Vorlesemodus:** Neben jedem Titel (Einträge aller Zoomstufen, Kapitel- und Abschnittstitel im Bibeltext) startet ein kleiner Knopf das Vorlesen ab dieser Stelle. Gelesen wird ohne Unterbruch weiter durch dieselbe Ebene: Überschrift und Zusammenfassung bzw. Verse mit Kapitel- und Abschnittstiteln; Einträge ohne Text werden übersprungen, Bibelstellen-Marken als Buch, Kapitel und Vers gesprochen.
- **Player** unten, minimal: Anzeige des vorgelesenen Teils, zurück, Pause/weiter, vor, schliessen. Der vorgelesene Teil ist im Text hinterlegt und bleibt im Blick. Stimme des Geräts (Web Speech API, Sprechtempo aus den Einstellungen); Züridüütsch wird mit einer deutschen Stimme gelesen. Pause setzt am Satzanfang wieder ein, weil Anhalten/Fortsetzen nicht auf allen Geräten zuverlässig ist.
- Neue Prüfung `scripts/test_reading_stream_vorlesen.cjs` (Playwright, nachgebildete Sprachausgabe).

## v0.47 — 2026-10-14 — Logo mit Herz, «Zuletzt gelesen» eingeklappt

- Logo: Beim Darüberfahren, Fokussieren oder Antippen wechselt es zu einem Herz mit denselben oberen Bögen, demselben unteren Mittelpunkt und gleichem Aussenmass; das innere Kreuz bleibt mit 50 % Deckkraft auf denselben Achsen.
- Menü: «Zuletzt gelesen» ist wie die ausgearbeiteten Stellen eingeklappt (mit Anzahl).

## v0.46 — 2026-10-14 — Lesestrom ohne «Ausgearbeitet»-Hinweise

- Buch- und Kapiteleinträge zeigen keine Verweise «Ausgearbeitet: …» mehr; ausgearbeitete Abschnitte erscheinen ohnehin beim Vertiefen, die Liste bleibt im Menü.

## v0.45 — 2026-10-14 — Mundart: «Ältischti»

- Züridüütsch einheitlich «Ältischti» (Gemeindeälteste) und «ältischt…» (älteste), statt «Elteschti» bzw. «eltischt…», in Übersetzungen, Wortzuordnungen, Lokalisierungen und Autorenwerkzeugen (31 Datensätze, 15 Skripte); frühere Schreibung im revision_log vermerkt.

## v0.44 — 2026-10-14 — Johannesevangelium aus dem Urtext

- **Import Johannes:** SBLGNT mit MACULA-Annotation (15 625 Wörter; Schreibvarianten wie Μωσῆς/Μωϋσῆς im Importer ausdrücklich gelistet, ᾿ als Elisionszeichen), SBLGNT-Apparat (770 von 773 Einträgen zugeordnet), Bewertung «Übereinstimmung der Editionen», CNTR-Transkriptionen von 30 Handschriften und 5 Ausgaben, neu u. a. 𝔓66, 𝔓52, 𝔓90, 𝔓5, 𝔓6, 𝔓22, 𝔓28, 𝔓39, 𝔓95, 𝔓106–𝔓109, 𝔓119–𝔓122, 𝔓134, 029, 0162, 0258, 0323 (Metadaten nach gängiger Einordnung, nicht eigens geprüft); maschinelle Kollation aller 21 Kapitel; STEPBible TAGNT (Ausgaben je Wort); Luther 1912 und Elberfelder 1905 zum Vergleich.
- **Übersetzung** Hochdeutsch und Züridüütsch mit vollständiger Wortzuordnung für alle 879 Verse (5,4 ohne SBLGNT-Text, Wortlaut als Lesart bei 5,3), Entscheidungen mit einheitlichen Grundentscheiden (λόγος, ἐγώ εἰμι, δόξα, σημεῖον, μένω, «die Juden» als gekennzeichnete Deutungsentscheidung, παράκλητος, ἀγαπάω/φιλέω), Lesarten-Alternativen. 7,53–8,11 (Ehebrecherin) in ⟦ ⟧ übersetzt; die Einordnung als spätere Einfügung steht als verbreitetes Urteil mit dem Handschriftenbefund der erfassten Transkriptionen.
- **Studieninhalte** Kapitel 1–21: Befunde, Deutungen mit Gegenargumenten, Grundsätze, Anwendungen, Fragen, Beziehungen (auch zu Markus 14–16), Hintergrund zu Abschnitten, Kapitelzusammenfassungen, drei Studien; Kontext CTX-JHN-READERS-0095. Buchzusammenfassung neu gegen den Text gefasst.
- KI-Entwurf mit getrennter KI-Gegenlesung (Übersetzung Vers für Vers, Handschriftenangaben und Zählungen per Skript); keine fachliche oder muttersprachliche Prüfung. Ausserbiblische Quellen- und Literaturangaben der Studien sind nicht nachgeschlagen und als offene Prüfpunkte in STUDY-JHN-0001…0003 vermerkt.

## v0.43 — 2026-10-14 — Menü ohne «Zur ganzen Bibel»

- Menüeintrag «Zur ganzen Bibel» entfernt; dasselbe leistet ein Tippen auf das Logo oben links.

## v0.42 — 2026-10-14 — Zwei Urteile in Zusammenfassungen korrigiert

- **Markus 16:** Dass der kürzere und der längere Markusschluss spätere Ergänzungen sind, steht nicht mehr als Tatsache da, sondern als verbreitetes textkritisches Urteil, mit den Belegen (SBLGNT-Doppelklammern ⟦ ⟧; Sinaiticus 01 und Vaticanus 03 enden nach den CNTR-Transkriptionen mit Markus 16,8) und beim längeren Schluss mit der Gegenposition (Minderheit: ursprünglich; kirchlich weithin als kanonisch anerkannt). Betroffen: TU-MRK-016-001-020 (auch Titel), TU-MRK-016-001-008, TU-MRK-016-009-020 (Titel ohne «spätere Ergänzung»), SUM-CH-MRK-016.
- **Rut 1:** Noomi nennt sich nicht selbst «Mara», sondern bittet die Frauen, sie so zu nennen (Rut 1,20); TU-RUT-001-001-022.
- Hochdeutsch und Züridüütsch; frühere Fassungen im revision_log.

## v0.41 — 2026-10-14 — Zusammenfassungen geprüft, «Zuletzt gelesen»

- **Zusammenfassungen aller Zoomstufen** gegen die eigenen Übersetzungen bzw. den Bibeltext geprüft (KI-Durchgang): rund 150 Korrekturen in Abschnitten, Kapiteln, Büchern, Buchgruppen und Testamenten, z. B. Obadja 15–18 (Entronnene, Josef als Flamme), Rut 1,1–5 (Reihenfolge: Elimelech stirbt vor den Heiraten), Jona 3 (Gott führt das Unheil nicht aus), Markus 3,6 (sie beraten, statt beschliessen), Matthäus 6,14–15 (Bedingung der Vergebung). Die Mundart-Fassungen der Buch- und Gruppenzusammenfassungen waren eigenständige Texte und sind jetzt Übertragungen des Hochdeutschen. Frühere Fassungen im revision_log.
- **Regel** (AGENTS.md): Am Schluss jeder Arbeit alle Zusammenfassungen gegen den Text prüfen; Werkzeug `scripts/authoring/revise_summary.py` für Datensätze ohne laufendes Autorenwerkzeug.
- **Menü:** «Zuletzt gelesen» (Abschnitt- bzw. Kapitelebene, bis 12 Einträge, nur auf diesem Gerät im Browser-Speicher, mit «Verlauf löschen»); die Liste der ausgearbeiteten Stellen ist eingeklappt.

## v0.40 — 2026-10-14 — Jona, 1–3 Johannes und das ganze Markusevangelium aus dem Urtext

- **Jona** (48 Verse, Hebräisch): WLC mit Umrechnung der Verszählung (hebräisch 2,1–11 = KJV 1,17–2,10), Texte vom Toten Meer (MurXII, 4QXII a/f/g; nicht kommerzielle Schicht), Übersetzungen Hochdeutsch und Züridüütsch mit Wortzuordnung, Entscheidungen, Studieninhalte.
- **1–3 Johannes** (132 Verse, Griechisch): SBLGNT, 84 Variantenstellen, Handschriften 01, 02, 03, 04 sowie 𝔓9 und 0232 (CNTR), Übersetzungen mit Wortzuordnung, Entscheidungen, Lesarten-Alternativen (Comma Johanneum anhand der Daten erklärt), Studieninhalte. 3 Joh 1,15 der griechischen Zählung ist nach TVTMS an 1,14 angehängt; die Umrechnung griechisch → KJV (`versification.greek_verse_map`) gilt jetzt auch in den Importern für SBLGNT, CNTR und die Vergleichsbibeln.
- **Markus ganz** (zusätzlich zu 3,20–35): Übersetzungen Hochdeutsch und Züridüütsch mit Wortzuordnung für alle Kapitel, Entscheidungen und Lesarten-Alternativen; Markusschlüsse (kürzerer Schluss in 16,8, längerer 16,9–20) in ⟦ ⟧ und als spätere Ergänzungen erklärt; Verse ohne SBLGNT-Text (7,16; 9,44.46; 11,26; 15,28) ohne Übersetzung, ihr Wortlaut als Lesart. Maschinelle Kollation für alle Kapitel, neu mit 𝔓88, 𝔓137, 059, 0188, 0214, 0315. Studieninhalte für Kapitel 1–16. Luther 1912 und Elberfelder 1905 für Markus, Jona und 1–3 Johannes.
- Kollation: Lesarten mit «…», die sich im Grundtext nicht verankern lassen, werden übersprungen und vermerkt (`not_collated`); falsche Tags (immer TAG-MARK) in den Kollationen von Matthäus, Lukas, Philipper und Titus korrigiert.
- Alles KI-Entwurf mit getrennter KI-Gegenlesung (Übersetzung Vers für Vers, Zählungen per Skript, Quellenangaben teils per Websuche bestätigt); keine fachliche oder muttersprachliche Prüfung.

## v0.39 — 2026-10-14 — Wörterbuch, Ausgaben je Wort, Ketiv/Qere

- **Schemaänderung (explizit):** neue Typen `lexicon` (`data/lexica/`) und `tagged_text_alignment` (`data/tagged-alignments/`); Schema-Titel v0.9. Keine Migration nötig, bestehende Datensätze unverändert. Beschreibung in [docs/DATENMODELL.md](docs/DATENMODELL.md).
- **Wörterbuch im Wortblatt:** UBS Dictionary of the Greek New Testament (überarbeitetes Louw-Nida) und UBS Dictionary of Biblical Hebrew (aus SDBH), beide von UBS unter **CC BY-SA 4.0** veröffentlicht (Lizenztext im Repository geprüft) — anders als die SDBH-/MARBLE-Felder in MACULA, die «used with permission» bleiben und weiter ausgeschlossen sind. Dazu STEPBible TBESG/TBESH als Kurzglossen (CC BY 4.0); die TBESH-Bedeutungsspalte (Abridged BDB, © Online Bible) ist nicht übernommen. Nur Einträge für Wörter der importierten Bücher (Griechisch 3019 UBS-Einträge, Hebräisch 595). Im Wortblatt («Urtext und Details») «Wörterbuch» mit Bedeutungen, Bedeutungsfeld und Kennzeichen «hier» nach der Stellenliste des Wörterbuchs; Wörterbuchtext englisch.
- **Ausgaben je Wort (NT):** STEPBible TAGNT für Matthäus, Markus, Lukas, Philipper, Titus, 1–3 Johannes den SBLGNT-Wörtern zugeordnet (Markus 11 274 von 11 286 Wörtern; nicht zugeordnete gemeldet in `reports/stepbible-tagged-<BUCH>.json`). Im Versblatt Block «Wörter in den Textausgaben»: je Wort «fehlt in TR, Byz», «nur in …», andere Lesung der übrigen Ausgaben, Wörter anderer Ausgaben mit «+». Ausdrücklich Ausgabenbefund, nicht Handschriften.
- **Ketiv/Qere (AT):** aus STEPBible TAHOT die geschriebenen Formen für Rut (12, dazu 3,12 «geschrieben, nicht gelesen»), Obadja (1), Jona (0); im hebräischen Wortblatt «Geschrieben (Ketiv)» / «Gelesen (Qere)». Zusätzlich dStrong je Morphem für die Wörterbuch-Zuordnung.
- Importer `scripts/import_stepbible_tagged.py` und `scripts/import_lexica.py` (Commits und SHA-256 fest); Quellenkatalog nachgeführt (TAGNT, TAHOT, TBESG, TBESH, UBS-Wörterbücher verwendet; neu SRC-STEP-TBESG, SRC-UBS-DBH); Validator prüft Token-Verweise der Zuordnungen; Tests ergänzt. Erwartete Zahlen der Lesestrom-Tests an die neuen ausgearbeiteten Abschnitte (Markus ganz, Jona, 1–3 Joh) angepasst.

## v0.38 — 2026-10-13 — Texte vom Toten Meer (nicht kommerzielle Schicht)

- Erste Daten in `data-nc/`: biblische Rollen vom Toten Meer aus ETCBC dss (Abegg u. a., CC BY-NC 4.0) für Rut (2QRuth a/b, 4QRuth a/b) und Obadja (4QXII g, MurXII), je Vers mit Fragment und Zeile. Von den Herausgebern ergänzte Buchstaben stehen in eckigen Klammern; ganz ergänzte Wörter gelten nicht als Bezeugung.
- Maschineller Vergleich mit dem Westminster Leningrad Codex je Wort: gleich, nur Schreibweise (Lesehilfen ו/י, lange Endungen), teilweise erhalten, abweichend, zusätzlich. Gefunden u. a. 4QRuth a 1,1–2 «בשדה» statt «בשדי» und 1,2 «וישבו» statt «ויהיו». Nicht am Faksimile geprüft.
- Importer `scripts/import_dss.py` (alle AT-Bücher möglich; Verszählung über die WLC-Umrechnung). Lesestrom: im Versblatt («Urtext und Details») Block «Texte vom Toten Meer»; Daten in eigenen Paketen `n/<BUCH>`, abschaltbar mit `BIBLE_APP_NO_NC=1`.
- Quellenkatalog: ETCBC dss als verwendet (nur `data-nc/`); Validator-Tests prüfen jetzt auch mit `data-nc/`.
- Septuaginta (CATSS) wartet auf die unterschriebene Nutzungserklärung; die NTVMR-Schnittstelle ist aus dieser Umgebung gesperrt und braucht die Antwort des INTF (docs/ANFRAGEN.md).

## v0.37 — 2026-10-13 — Quellenkatalog, Quellenkarte, Anfragen

- **Quellenkatalog:** 66 Quellen als `source`-Datensätze mit `catalog` (Bereich, Schicht, Nutzungsrecht frei/BY-SA/nicht kommerziell/auf Anfrage/geschützt, Verwendung verwendet/zitiert/vorgesehen/nicht verwendet, Begründung). Die sechs bestehenden Quelldatensätze sind ergänzt, nicht ersetzt. Werkzeug `scripts/authoring/quellen_katalog.py`.
- **Immer aktuell:** Der Validator verlangt, dass jede Herkunftsadresse in Datensätzen im Katalog steht, verwendete Quellen auf vorhandene Dateien zeigen und keine nicht kommerzielle oder geschützte Quelle im freien Kern als verwendet gilt (mit Negativtests).
- **Quellenkarte** `app/quellenkarte/index.html`, erzeugt aus dem Katalog (`scripts/build_source_map.py`); im Lesestrom als Blatt «Quellen und Rechte» im Menü, mit Filtern und Begründung je Quelle.
- **Anfragen** [docs/ANFRAGEN.md](docs/ANFRAGEN.md): Rechteinhaber nach Nutzen geordnet, mit Kontakt, Prüfdatum und Entwürfen (DBG, INTF, CATSS, UBS, Crossway, Bildrechte); Abschnitt zur Rolle eines gemeinnützigen Vereins. «Erlaubnis» und «Anfrage» sind zu einer Klasse zusammengefasst.

## v0.36 — 2026-10-13 — Verszählung des Alten Testaments umgerechnet

- Umrechnung der hebräischen Verszählung (WLC) in die Navigationszählung (KJV) nach TVTMS (`scripts/versification.py`), eingebaut in den MACULA-Hebrew-Import. Für alle 39 Bücher geprüft (`scripts/check_versification_ot.py`): nach der Umrechnung stimmen alle Kapitel mit der Navigation überein; Neh 7,68 fehlt im hebräischen Text und bleibt leer. Damit kann jedes Buch des Alten Testaments importiert und übersetzt werden.
- Psalmüberschriften, die im Hebräischen eigene Verse sind, stehen vor Vers 1 und sind als Überschrift markiert; geteilte Verse (z. B. Jes 63,19/64,1) folgen TVTMS. Jeder umgerechnete Token behält die hebräische Stelle.
- Rut und Obadja bleiben unverändert (gleiche Zählung). Tests: `scripts/test_versification.py`.

## v0.35 — 2026-10-13 — Rut und Philipper aus dem Urtext

- **Grundsatz** (Entscheid Andi Neck): Der Lesetext geht immer vom Urtext aus; Luther 1912 und Elberfelder 1905 dienen nur dem Vergleich.
- **Rut** (85 Verse, Hebräisch): WLC mit MACULA-Hebrew-Annotation (2026 Morpheme); Arbeitsübersetzungen Hochdeutsch und Züridüütsch aus dem Hebräischen mit Wortzuordnung je Morphem, 66 Übersetzungsentscheidungen (u. a. חֶסֶד, גֹּאֵל, כָּנָף, «Füsse aufdecken», Ketiv/Qere in 4,5), Studieninhalte (14 Befunde, 8 Deutungen mit Gegenargumenten, 9 Hintergrundnotizen, Grundsätze, Anwendungen, Fragen, Beziehungen, Kapitelzusammenfassungen). Freie textkritische Daten (Qumran, LXX) fehlen weiterhin.
- **Philipper** (104 Verse, Griechisch): SBLGNT mit MACULA-Annotation (1626 Wörter), 45 Variantenstellen mit Gesichertheitsbewertung (2 versübergreifende Apparateinträge zu 1,16–17 nicht sicher zuordenbar, siehe `reports/`), Handschriften 01, 02, 03, 04, 𝔓46 und 𝔓15/16 sowie fünf Ausgabentexte (CNTR) mit maschineller Zuordnung. Übersetzungen Hochdeutsch und Züridüütsch mit Wortzuordnung, 52 Entscheidungen (u. a. Christushymnus 2,6–11, πίστις Χριστοῦ 3,9), 11 Lesarten-Alternativen, Studieninhalte.
- Beide Bücher von einem getrennten KI-Durchgang gegengelesen (Übersetzung Vers für Vers, Zählungen per Skript, Quellenangaben); Korrekturen eingearbeitet, z. B. «Moabiter, nicht Moabiterin» als Talmud (Jevamot 76b) statt Mischna, Wochenfest als Fest der Erstlinge, Mundart-Formen vereinheitlicht. Keine fachliche oder muttersprachliche Prüfung.
- Importer: MACULA-Hebrew-Import für alle Bücher des Alten Testaments vorbereitet; bricht ab, wenn die hebräische Verszählung von der Navigationszählung abweicht (Umrechnung noch offen). SBLGNT-Apparat für Philipper, CNTR mit 𝔓46 und 𝔓15/16, Vergleichsbibeln für Rut und Philipper.

## v0.34 — 2026-10-13 — Hintergrund damals für alle 66 Bücher

- 84 neue Hintergrundnotizen auf Buchebene (`scope: book`) für die 64 bisher fehlenden Bücher, für 20 Bücher mit einer zweiten Notiz (z. B. Genesis und altorientalische Fluterzählungen, Jesaja und die grosse Jesajarolle, Daniel und die Datierungsfrage, Markusschlüsse, Datierung der Offenbarung, Nord- oder Südgalatien). Je Notiz Entstehung, Zeit, Ort, Adressaten, die vertretenen Positionen (traditionell und historisch-kritisch, ohne Entscheid), «Nicht sicher», Belegstellen als Marken, ausserbiblische Quellen und Ursprachwörter; alle in Züridüütsch.
- Autorenwerkzeug `scripts/authoring/hintergrund_buecher.py` mit Datenmodulen je Buchgruppe in `scripts/authoring/buecher/`; prüft Pflichtfelder, Kontexte, Marken, unmarkierte Stellen und Umschriften.
- Entstehung: KI-Entwürfe (Claude), danach von einem getrennten KI-Durchgang auf Daten, Quellenangaben und Ausgewogenheit gegengelesen (11 Korrekturen, z. B. Esther/Nehemia in Qumran, Talmud zur Chronik, Sirach zu Jesaja, Luthers Jakobus-Vorrede, 𝔓52-Datierung). Die Gegenlesung konnte Webseiten teils nicht abrufen und stützt sich dann auf Kenntnis der Primärtexte. Keine fachliche Prüfung durch eine Person; Mundart nicht muttersprachlich geprüft.
- Browserprüfung: Hintergrund auf Buchebene in Mundart.

## v0.33 — 2026-10-13 — Titus und Obadja als Muster (Griechisch und Hebräisch)

- **Titus** (ganzer Brief, 46 Verse): SBLGNT-Text mit MACULA-Annotation (659 Wörter), 24 Variantenstellen mit Gesichertheitsbewertung, Handschriften 01, 02, 04 und 𝔓32 sowie fünf Ausgabentexte (CNTR) mit maschineller Zuordnung zu den Lesarten. Arbeitsübersetzungen Hochdeutsch und Züridüütsch aus dem Griechischen mit vollständiger Wortzuordnung, Übersetzungsentscheidungen und sieben Lesarten-Alternativen; Vergleich mit Luther 1912 und Elberfelder 1905.
- **Obadja** (21 Verse): erster hebräischer Text. Westminster Leningrad Codex mit MACULA-Hebrew-Annotation (435 Morpheme; Lemma, Morphologie, Glossen, LXX-Entsprechung); Wortlisten der SDBH («used with permission») bewusst nicht übernommen. Arbeitsübersetzungen Hochdeutsch und Züridüütsch aus dem Hebräischen mit Wortzuordnung auf Morphem-Ebene und Entscheidungen (`heb`); Gottesname als «JHWH» bzw. erklärt. Freie textkritische Daten zu Obadja fehlen; das ist in den Übersetzungsnotizen vermerkt.
- **Studieninhalte** je Buch: Kontext, Befunde, Deutungen mit Gegenargumenten, Grundsätze, Anwendungen, offene Fragen, Beziehungen, Hintergrund damals (auch auf Buchebene, `scope: book`) und Kapitelzusammenfassungen, alle auch in Züridüütsch (Lokalisierungen). KI-Entwurf; ein zweiter KI-Durchgang hat gegengelesen, die Korrekturen sind eingearbeitet. Keine fachliche oder muttersprachliche Prüfung.
- **Hebräisch im Lesestrom:** Text rechts nach links, Wort-für-Wort-Blatt (Morpheme zu Wörtern gruppiert, Glossen, LXX-Entsprechung), lesefreundliche Umschrift (`scripts/hebrew_translit.py`, gleiche Regeln im Browser) und Anhören; Quellenangaben WLC/MACULA Hebrew.
- **Werkzeuge:** `scripts/import_macula_hebrew_book.py`, `scripts/import_comparison_bibles.py` (Luther 1912 und Elberfelder 1905 je Buch, Quelle per SHA-256 fixiert); CNTR-Importer für Titus samt 𝔓32 und ohne Überschreiben bestehender Zeugen-Metadaten; Autorenwerkzeuge mit gemeinsamer Auszeichnung für Übersetzung und Wortzuordnung (`scripts/authoring/_lib.py`, `_study.py`, `titus_*.py`, `obadja_*.py`), die nur bei Änderung schreiben und die frühere Fassung im `revision_log` festhalten.
- Validator: hebräische Übersetzungsentscheidungen (Konsonantenabgleich mit dem Text), Hintergrund mit `scope: book`. Entscheidungsmarken im Text sind keine Knöpfe mehr, sondern umbrechende Textspannen (lange Entscheidungen zerrissen sonst die Zeile).

## v0.32 — 2026-10-13 — Hintergrund damals für Bibel, Testamente und Buchgruppen

- 17 neue Hintergrundnotizen für die oberen Ebenen: Bibel (Entstehung über rund tausend Jahre; wie der Kanon entstand), Altes Testament (Israel zwischen Grossmächten; Tanach und christliche Ordnung), Neues Testament (unter römischer Herrschaft; zuerst Briefe, dann Evangelien) und alle zehn Buchgruppen (u. a. Tora und Exodus mit ausserbiblischen Spuren, Geschichtsbücher, Psalmen und Weisheit, Propheten, Evangelien, Apostelgeschichte, Briefe, Offenbarung). Jede Notiz mit Einschätzung, «Nicht sicher», Belegstellen, ausserbiblischen Quellen und Ursprachwörtern; alle in Züridüütsch. KI-Entwurf, fachlich ungeprüft.
- Datenmodell: `background_note` mit `scope` (`bible`, `testament`, `book_group`, `book`) und `testament`/`group`; vier historische Kontexte (`CTX-HIST-*`). Autorenwerkzeug `scripts/authoring/hintergrund_uebersicht.py`.
- Lesestrom: Knopf «Geschichte» bei Bibel, Testament und Buchgruppe öffnet den Hintergrund; geladen als eigenes Paket `b/_overview` (Mundart in `l/gsw/common`).

## v0.31 — 2026-10-13 — Für die ganze Bibel und viele Sprachen aufgeräumt

- **Pakete:** Der Lesestrom besteht aus einem Kern und nachladbaren, gzip-komprimierten Paketen je Buch (`b/<BUCH>`: Griechisch, Varianten, Deutungen, Hintergrund, Querverweise) und je Sprache und Buch (`l/<Sprache>/<BUCH>`, `l/<Sprache>/common`). Die App lädt sie erst bei Bedarf (Navigation, Weiterlesen, Sprachwechsel). Veröffentlicht wird `build/reading-stream/` (Kern 145 KB, Pakete zusammen 82 KB); `app/reading-stream/index.html` bleibt als Einzeldatei mit allen Paketen (offline, Tests). Für Hosts, die keine Binärdateien ausliefern (z. B. das Claude-Artefakt), gibt es dieselben Pakete als gzip in Base64 (`build/reading-stream-txt/`, `.gz.txt`).
- **Bibelstellen im Fliesstext** als sprachneutrale Marken `[[MAT.6.34]]` statt «Mt 6,34» (186 Marken); die App zeigt sie je Sprache an und verlinkt sie. Werkzeug `scripts/prose_refs.py`; der Validator prüft Marken und meldet unmarkierte Stellen.
- **Titel und Zusammenfassungen** der Texteinheiten in weiteren Sprachen sind Lokalisierungen (wie alle anderen Übersetzungen von Erklärtexten).
- **Neutrale Feldnamen** in Übersetzungsschichten (`from_text`, `to_text`, `note`, `readings`, `origin`, `more_literal`, `other_options`); `_de` nur noch für hochdeutsche Originale und Dokumentation.
- **Vorrang** ohne Heuristik: Arbeitsübersetzungen derselben Sprache dürfen sich nicht überschneiden (Validator); ausgearbeitete Abschnitte werden aus den Daten ermittelt statt von Hand gelistet.
- **Versifikation:** Zuordnungsdaten zwischen hebräischer, lateinischer, griechischer und englischer Zählung aus TVTMS (STEPBible, CC BY 4.0, 22 874 Zeilen, `data/versification/`). Der Validator prüft alle Stellen gegen die Verszahlen der Navigation (KJV) und meldet Abweichungen als WARN (derzeit 5 Querverweise auf 3 Joh 1,15). Die Umrechnung selbst folgt mit dem ersten Text in anderer Zählung.
- Migration `scripts/migrations/v0_31.py`, Protokoll `provenance/migrations/2026-10-13-v0.31.json` (531 Änderungen); Lokalisierungen mit nachgeführtem Fingerabdruck. Historische Autorenwerkzeuge in `scripts/authoring/` sind gegen erneutes Ausführen gesperrt.
- «Zeit des …» im Hintergrund nennt den Evangelisten des jeweiligen Buchs (vorher immer Markus).
- Prüfungen: Validator-Negativtests für Marken und Überschneidungen; Browserprüfung der aufgeteilten Fassung (`scripts/test_reading_stream_split.cjs`).

## v0.30 — 2026-10-13 — Vergleichsübersetzungen je Sprache

- Vergleichsübersetzungen (`historical_comparison`) sind sprachgebunden. Welche Sprachen eine Übersetzungsschicht zum Vergleich zeigt, legt ihr Zielkontext fest (`comparison_languages` im `context`-Datensatz, Reihenfolge = Anzeige); ohne Angabe nur die eigene Sprache.
- `CTX-CH-ZH-GSW-2026`: `["gsw", "de"]` (redaktionelle Annahme: Mundart-Lesende kennen die Bibel meist auf Hochdeutsch). Für Züridüütsch ist noch keine Vergleichsfassung erfasst; das Versblatt sagt das ausdrücklich und zeigt danach Luther 1912 und Elberfelder 1905 unter «Hochdeutsch».
- Projektion: Vergleichseinträge tragen `lang`, Schichten `compare_languages`.
- `node_modules/` in `.gitignore`.

## v0.29 — 2026-10-13 — Alle Inhalte in Mundart, Lokalisierungen, Weiterlesen beim Scrollen

- Neuer Datensatztyp `localization` (`data/localizations/<BCP-47>/<ID>.json`): übersetzt einzelne Felder eines Originaldatensatzes (`localizes`, `fields` mit den Feldnamen des Originals, bei `terms` die Bedeutungen in Reihenfolge). `source_fingerprint` hält je Feld fest, von welchem Stand des Originals übersetzt wurde. Originale tragen keine Übersetzungen; neue Sprachen und neue Deutungen ändern einander nicht.
- Veraltete Felder (Original seit der Übersetzung geändert) meldet `scripts/validate.py` als WARN; die Projektion liefert sie nicht aus, die App zeigt dann das Original. Gemeinsamer Lader `scripts/localizations.py`.
- Züridüütsch für alle Studieninhalte der drei ausgearbeiteten Abschnitte: 11 Befunde, 10 Deutungen (inkl. Gegenargumente und Wortbedeutungen), 2 Grundsätze, 2 Anwendungen, 3 offene Fragen, 25 Hintergrundnotizen, 85 Zusammenfassungen (Bibel, Testamente, 10 Gruppen, 66 Bücher, 6 Kapitel) – 138 Lokalisierungen. Wortbedeutungen und mögliche Entstehung der Lesarten in den gsw-Übersetzungsschichten. Autorenwerkzeug `scripts/authoring/zueridueuetsch_inhalte.py`. KI-Entwurf, muttersprachlich noch nicht geprüft.
- Lesestrom: Studienblatt, Hintergrund, Wort-Blatt, Quellen-Blatt und Zusammenfassungen aller Ebenen folgen dem gewählten Lesetext. Noch Hochdeutsch: Bedienung, Buch- und Gruppennamen, Handschriften- und Ausgabenbeschreibungen.
- Weiterlesen ohne Knopf: nachgeladen wird, sobald «Weiterlesen» in die Nähe des sichtbaren Bereichs kommt (auch wenn der Inhalt kürzer als der Bildschirm ist) sowie beim Ziehen über Anfang oder Ende hinaus (Mausrad, Wischen). Der Knopf bleibt für Tastatur und Vorlesehilfen.
- Prüfungen: Validator-Negativtests für Lokalisierungen (falsches Feld, falsche Listenlänge, veraltet); Bedienungsprüfung für Mundart-Inhalte.

## v0.28 — 2026-10-13 — Abschnittstitel und -zusammenfassungen in Mundart

- Texteinheiten tragen Titel und Zusammenfassung je Sprache (`title_by_language`, `summary_by_language`, Schlüssel BCP-47); hochdeutsche Felder bleiben Standard. Für die neun ausgearbeiteten Einheiten liegt Züridüütsch vor («S Vatterunser», «Nöd zum Schiin und nöd mit vil Wort», «De Striit um de Beelzebul» …).
- Lesestrom zeigt Titel und Zusammenfassungen der gewählten Lesetext-Schicht: im Strom, am Abschnittskopf, in Blättern, Navigator, Pfad und Seitenleiste.
- Noch Hochdeutsch: Zusammenfassungen der oberen Ebenen (Bibel, Testamente, Gruppen, Bücher, Kapitel), Hintergrund, Deutungen und die Bedienung.

## v0.27 — 2026-10-13 — Züridüütsch als zweite Übersetzungsschicht

- Vorgabe: aus den Urtexten und den erarbeiteten Artefakten in beliebige Sprachen und Kulturen übersetzen; zuerst Züridüütsch neben Hochdeutsch.
- Datenmodell: Übersetzungsschichten je Sprache (`language` BCP-47, `target_context`, `orthography_de`, `register_de`, `control_translation`, `review_de`), Wortzuordnung mit `target_language`. Neuer Kontext `CTX-CH-ZH-GSW-2026`.
- Züridüütsch (Dieth-Schreibung, aus dem SBLGNT) für Mt 6,5–15, Lk 11,1–4 und Mk 3,20–35: 31 Verse, 15 Lesarten-Alternativen, 36 markierte Übersetzungsentscheidungen, vollständige Wortzuordnung für Mt 6,9–13 und Lk 11,2–4. Autorenwerkzeug `scripts/authoring/zueridueuetsch.py`. KI-Entwurf; Prüfung der Mundart durch eine muttersprachliche Person vorgesehen (Andi Neck), noch nicht erfolgt.
- Lesestrom: Menü «Lesetext» (Hochdeutsch | Züridüütsch); Lesarten im Text, Entscheidungs-Markierungen und Versblatt folgen der gewählten Schicht; fehlt ein Vers in einer Schicht, erscheint Hochdeutsch mit Hinweis.
- Datenbestand: 3441 Datensätze.

## v0.26 — 2026-10-13 — Titel in der Kopfzeile

- Der Titel-Knopf in der Kopfzeile hatte innen keinen Abstand (die allgemeine Knopf-Regel setzte ihn auf null); der Titel hat jetzt innen Abstand und bleibt über die volle Breite antippbar.

## v0.25 — 2026-10-13 — Seitenleiste auf breiten Bildschirmen

- Die Seitenleiste (ab 900 px Breite) hatte keinen Innenabstand und eine eigene Formensprache. Jetzt: Überschrift der Ebene, Einträge mit Abstand, Hover-Fläche, aktuelle Position gefüllt, Punkt für ausgearbeitete Einträge; der aktuelle Eintrag wird beim Öffnen in Sicht gerollt.

## v0.24 — 2026-10-13 — Einheitliche Formensprache

- Eine Rundung für alles Antippbare und alle Kästen (`--r: 6px`): Segmentleisten, Chips, Raster im Navigator, Pfad, Schliessen, Symbolknöpfe, Versnummern, Lesarten-Karten, Zeugen-Kästen, Suchfeld, «Zurück zu …». Keine Pillen und Kreise mehr; einzige Ausnahme ist der Ein/Aus-Schalter, der als Toggle seine gewohnte Form behält.
- Einstellungen: Beschriftung links, Auswahl rechts; bricht die Auswahl um, steht sie rechtsbündig unter der Beschriftung («Aussprache», «Tempo»). Stimmen werden als einzelne Chips statt als umbrechende Segmentleiste gezeigt.
- Leichter Hover-Hintergrund auf Kopf- und Fussleisten-Knöpfen.

## v0.23 — 2026-10-13 — Navigator, Querverweise, verlinkte Stellen

- Neuer Navigator (Tippen auf die Titelzeile): «Du bist hier» als antippbarer Pfad, dann Altes/Neues Testament → Buchgruppe → Buch → Kapitel → Vers als Raster; ausgearbeitete Bücher, Kapitel und Verse sind mit einem Punkt markiert, ausgearbeitete Abschnitte des Kapitels direkt wählbar; «öffnen» führt auf Buch- oder Kapitelebene. Ersetzt die alte Inhaltsliste.
- Querverweise: 344 799 Verweise von OpenBible.info (CC BY) importiert (`data/crossrefs/`, Typ `crossref_set`). Im Versblatt erscheinen die zehn bestbewerteten als antippbare Stellen.
- Bibelstellen in Erklärtexten, Vergleichslisten und «Ähnliche Stellen» sind antippbar (auch Listen wie «Jes 63,16; 64,7» und Kapitelbezüge wie «(6,14–15)»). Nach einem Sprung erscheint «Zurück zu …».
- «Verse fortlaufend» ist jetzt Standard (gespeicherte Einstellung wird einmalig umgestellt). Verse ohne Text erscheinen im Fliesstext nur als Nummer mit «…» und einem Hinweis am Anfang.
- Bekannte Grenze: Sprungziele ausserhalb der ausgearbeiteten Stellen zeigen noch keinen Text. Vorschlag: eine gemeinfreie deutsche Übersetzung (z. B. Luther 1912) als Lesetext-Ersatz einbetten, bis eigene Übersetzungen vorliegen.

## v0.22 — 2026-10-13 — Schliessen-Knopf, Verse fortlaufend

- «Schliessen» (bzw. «Fertig» im Menü) mit Symbol, runder Fläche und Hover-Effekt; beim Öffnen eines Blatts erscheint kein Fokusrahmen mehr um den Knopf (der Fokus liegt auf dem Blatt).
- Neue Option «Verse fortlaufend»: Verse als Fliesstext hintereinander statt je auf einer eigenen Zeile; Lesarten- und Hintergrund-Hinweise fliessen mit. Standard aus.
- Schriften der Symbolknöpfe und Hinweise unabhängig von der Umgebung festgelegt.

## v0.21 — 2026-10-13 — Einheitliche Symbole in den Blättern

- Versblatt, Verstehen-Blatt und Hintergrund-Blatt enden jetzt mit «Abschnitt: …» und denselben Symbolen «Verstehen» und «Geschichte» wie beim Abschnittstitel, statt der alten Textlinks.
- Quellenangabe: MorphGNT ausdrücklich auf Mk 3,22–30 bezogen.

## v0.20 — 2026-10-13 — Ruhigerer Lesefluss, Wort-Info

- Unterstrichene Stellen (Tradition, Deutung) sind antippbar und öffnen ein Wort-Blatt: griechischer Wortlaut mit Umschrift und Anhören, Grundform, zugehörige Deutungen, wörtlichere Fassung, weitere Möglichkeiten, Begründung und die Wiedergabe in Luther 1912 und Elberfelder 1905. Dafür führen die Übersetzungsentscheidungen jetzt den griechischen Wortlaut (`grc`, vom Validator gegen den Vers geprüft); fünf Deutungen haben Fachwörter (`terms`) erhalten.
- Das «+» am Versende entfällt: Hat ein Vers Details, ist seine Versnummer umrandet und antippbar.
- «Diesen Abschnitt verstehen» und «Hintergrund damals» stehen nicht mehr unter dem Abschnitt, sondern als Symbole «Verstehen» und «Geschichte» beim Abschnittstitel.
- Hinweise «Damals» im Text sind kompakter (ein Symbol, Themen nebeneinander).
- Aramäisch wird zuverlässig über die Umschrift mit einer deutschen Stimme vorgelesen; Hebräisch ohne Vokalzeichen an die hebräische Stimme, sonst ebenfalls über die Umschrift.

## v0.19 — 2026-10-13 — Ursprungswörter zum Anhören

- Wunsch: Wo eine Erklärung sich auf ein griechisches, hebräisches oder aramäisches Wort bezieht, das Wort klein mit Aussprache und Anhören-Knopf zeigen.
- Neues Feld `terms` (Sprache, Originalschrift, Umschrift, Bedeutung) für 15 Hintergrundnotizen und eine Deutung, z. B. ὑποκριτής «Schauspieler, Heuchler», aram. אַבָּא abba, hebr. מָחָר machar. Validator prüft die Felder; Regel in AGENTS.md ergänzt.
- Griechische Einschübe in Erklärtexten erhalten automatisch Umschrift und Anhören-Knopf; ohne Urtext-Modus erscheint nur die Umschrift (statt wie bisher ausgeblendet zu werden).
- Hebräisch/Aramäisch wird mit einer hebräischen Gerätestimme gesprochen; fehlt sie, liest eine deutsche Stimme die Umschrift.

## v0.18 — 2026-10-13 — Übersetzungsentscheidungen sichtbar

- Frage: Wie stark beeinflussen bestehende Übersetzungen unsere Übersetzung? Antwort im Datenmodell: Übersetzungsentscheidungen (`decisions`) für Mt 6,9–13 und Lk 11,2–4, je als wörtlich, sprachlich angepasst, Deutungsentscheidung oder der vertrauten Wiedergabe folgend, mit wörtlicherer Fassung, weiteren Möglichkeiten und Begründung. Ausdrücklich vermerkt: «führe uns durch die Versuchung» gibt den Wortlaut nicht wieder (εἰς «hinein», μή verneint).
- Vergleich mit gemeinfreien älteren Übersetzungen: Lutherbibel 1912 und Elberfelder 1905, nur für die Vaterunser-Verse.
- Lesestrom: Versblatt mit «Wie ist übersetzt?» und «Ältere deutsche Übersetzungen»; im Urtext-Modus sind Stellen, die einer Tradition folgen (gepunktet) oder eine Deutung wählen (gestrichelt), im Text unterstrichen.
- Validator prüft Art und Zieltext der Entscheidungen; neuer Negativtest.

## v0.17 — 2026-10-13 — Umschrift, Anhören, neue Voreinstellungen

- Griechische Wörter zusätzlich in lateinischer Umschrift (nach dem Muster des SBL-Handbuchs, betonte Silbe markiert, z. B. πονηροῦ → ponēroú), abschaltbar im Menü.
- Anhören-Knopf bei griechischen Wörtern, Lesarten, Handschriftentexten und ganzen Versen (Stimmen des Geräts über die Web-Speech-Schnittstelle). Einstellungen: Aussprache Neugriechisch oder Schulaussprache (Umschrift, gelesen von einer deutschen Stimme), Stimmenauswahl, Tempo, Probe. Beides nähert die Aussprache des 1. Jahrhunderts nur an; ohne installierte Stimme erscheint ein Hinweis.
- Hebräisch: Sprachausgabe ist vorbereitet (he-IL); Umschrift folgt mit den ersten hebräischen Texten.
- Voreinstellung: «Andere Lesarten im Text», «Hintergrund im Text» und «Urtext und Details» sind jetzt eingeschaltet (gespeicherte ältere Einstellungen werden einmalig darauf umgestellt).
- Umschalten im Menü lässt die Leseposition stehen (der oberste sichtbare Eintrag bleibt an seiner Stelle; das Menü behält seine Scrollposition).

## v0.16 — 2026-10-12 — Das Vaterunser

- Wunsch: das Vaterunser komplett bearbeiten.
- Text: Matthäus und Lukas vollständig importiert (SBLGNT mit MACULA-Annotation; Apparat Mt 820/827, Lk 1133/1142 Stellen zugeordnet, Rest protokolliert; Gesichertheitsbewertung). Importer: Gross/Klein-Abweichung SBLGNT/MACULA wird wie eine Akzentabweichung protokolliert; Apparatüberschrift «Matthew» erkannt.
- Textzeugen: CNTR-Transkriptionen für Matthäus und Lukas, dazu 𝔓45, 𝔓75 und sieben Amulette bzw. Einzeltexte mit dem Vaterunser (3.–6. Jh.; Metadaten nach papyri.info/DCLP). Zuordnung zu den Lesarten für Mt 6,5–15 und Lk 11,1–4 (Abgleich mit dem SBLGNT-Apparat jeweils 18/18 bzw. 6/6).
- Studie Vaterunser (`STUDY-LP-0001`, KI-Entwürfe, ungeprüft): Texteinheiten Mt 6,5–15 (drei Teile) und Lk 11,1–4; deutsche Arbeitsübersetzung mit neun Alternativen (u. a. Lobpreis am Schluss, «vergeben haben/vergeben», kurze und lange Lukasfassung), je mit Wortbedeutungen und Entstehungserklärungen; vollständige Wortzuordnung Mt 6,9–13 und Lk 11,2–4; 6 Befunde, 7 Deutungen mit Gegenargumenten (u. a. drei Deutungen von ἐπιούσιος, Versuchung, «der Böse/das Böse», Vergebung), Grundsatz, Anwendung, 2 offene Fragen, 7 Beziehungen, 12 Hintergrundnotizen, 2 Kapitelzusammenfassungen. Autorenwerkzeug `scripts/authoring/vaterunser.py`.
- Lesestrom: trägt jetzt mehrere ausgearbeitete Stellen (neue Projektion `scripts/project_study.py`, Schlüssel nach Bibelstelle); Menü listet die ausgearbeiteten Stellen; Studienblatt zeigt Anwendung, Fragen und Beziehungen je Abschnitt; Textzeugen-Blatt mit Papyri und Amuletten.
- Tests erweitert (Vaterunser in Struktur- und Bedienungstest). Abschnittsebene hat jetzt 6705 statt 6704 Einträge, weil Mt 6 nach echten Einheiten gegliedert ist.

## v0.15 — 2026-10-12 — Lesarten bis zur Quelle

- Rückmeldung: Bei anderen Lesarten bis zur Quelle eintauchen können, auch übersetzt.
- Handschriften: Transkriptionen der sechs ältesten Handschriften des Markusevangeliums (01 א, 02 A, 03 B, 04 C, 05 D, 032 W) und fünf Ausgabentexte (WH, RP, Stephanus, KJTR, SR) aus dem Center for New Testament Restoration importiert (CC BY-SA 4.0, Commit fixiert, SHA-256). Neue Typen `witness`, `witness_transcription`, `witness_reading_set`; neue Ausgaben ED-ST, ED-KJTR, ED-SR; Kurzbeschreibungen (`about_de`) für alle Ausgaben.
- Maschinelle Zuordnung Handschrift → Lesart für die 28 Variantenstellen in Mk 3,20–35 (`scripts/collate_witnesses.py`, `METHOD-AUTO-COLLATION-V1`), Erstschrift und Korrektur getrennt. Selbstprüfung gegen den SBLGNT-Apparat: 50/52.
- Befund: Ephraemi (C) liest in 3,29 laut CNTR ἁμαρτίας, nicht κρίσεως wie in der Arbeitsnotiz `VAR-MRK-003-029-001`; die Arbeitsnotiz bleibt erhalten, die Abweichung wird angezeigt. In 3,20 widersprechen sich SBLGNT-Apparat und CNTR-Text bei Robinson-Pierpont.
- Übersetzungs-Alternativen um Wortbedeutungen der Lesarten und mögliche Entstehungserklärungen ergänzt (Revision protokolliert).
- Lesestrom: Blatt «Bis zur Quelle» je Lesart. Validator prüft die neuen Typen; DOM-Test erweitert.

## v0.14 — 2026-10-12 — Hintergrund damals

- Rückmeldung: Auf Versebene passt der Lesestrom, es fehlt der Hintergrund damals.
- Neuer Datentyp `background_note` (`data/background/`): 13 Notizen zu Mk 3,20–35 über Zeit, Ort, Kultur und Religion, je mit Kontext, Sicherheitsgrad, Unsicherheiten, Vergleichsstellen und ausserbiblischen Fundstellen (nur zitiert). Neuer Kontext `CTX-MARK-READERS-0070` (erste Leserschaft des Markus), neuer Tag `TAG-HISTORICAL-BACKGROUND`. KI-Entwürfe, fachlich ungeprüft.
- Lesestrom: «Damals» im Versblatt, «Hintergrund damals» je Abschnitt, optional kurze Hinweise im Text (Menü).
- Validator prüft Pflichtfelder und Kontextverweis der Hintergrundnotizen; zwei neue Negativtests; DOM-Test erweitert. 1131 Datensätze.

## v0.13 — 2026-10-12 — Lesestrom als Hauptrichtung, zugänglicher und ungestörter

- Vorgabe: Bibelstudium zugänglich für Personen ohne Griechisch und Hebräisch; ungestört lesen und «abtauchen in die Tiefe»; Hintergrund nur auf Wunsch ([VISION.md](docs/VISION.md)).
- Lesestrom neu aufgebaut (`app/reading-stream/template.html`): Vollbild ohne Geräterahmen, Leisten blenden beim Lesen aus, Verse fliessen als Text, keine technischen Zähler, ein Vertiefen-Link je Eintrag, deutsche Stellenangaben (3,20), Farben nach System, Einstellungen lokal gespeichert.
- Lesarten, Studieninhalte und Quellen als Blätter über dem Text; «+» nur an Versen mit abweichenden Lesarten. Urtext, Wort für Wort, Editionenvergleich und IDs nur im Modus «Urtext und Details»; optional «Andere Lesarten im Text zeigen». Griechische Einschübe in Erklärungen werden ohne diesen Modus ausgeblendet oder umschrieben (nur Darstellung).
- Neue Datentypen im freien Kern: `navigation_structure` (`data/navigation/NAV-PROT66-KJV.json`, Testkonfiguration) und `summary` (`data/summaries/`, 83 Entwürfe). Bisher lagen sie in der Vorlage; die Inhalte sind unverändert übernommen. Schema und Validator ergänzt (1116 Datensätze, PASS).
- `scripts/build_reading_stream.py` bettet Navigation, Zusammenfassungen und Markus-Projektion ein; DOM-Test an die neue Bedienung angepasst.
- Studienprototyp `app/prototype/` als abgelöst gekennzeichnet; `build_prototype.py` bleibt als Datenprojektion.
- Prüfungen: Validator, Validator-Negativtests, Struktur- und DOM-Test; Ansicht in Chromium in Handybreite, hell und dunkel. Keine Prüfung auf echten Geräten, keine fachliche Prüfung.

## v0.12 — 2026-10-11 — Markus im Lesestrom

- Pilotstudie Mk 3,20–35 im neuen Lesestrom: drei kanonische Abschnitte, 16 Arbeitsübersetzungen, sechs Alternativen, 249 Wörter und 28 Variantenstellen.
- Aufklappbare Wortdetails, Quellenvergleich und getrennte Studienebenen mit Gegenargumenten, Prüfstatus, Bewertungsgrenzen und Attribution. Direkteinstieg im Menü und bei Markus.
- Reproduzierbarer Build aus bestehender Datenprojektion; kanonische Daten unverändert. Struktur-, Daten- und DOM-Interaktionstests erfolgreich; visuelle Geräteprüfung ausstehend.

## v0.11 — 2026-10-11 — Fortlaufender Lesetiefe-Prototyp

- Separater, eigenständig lauffähiger Entwurf `app/reading-stream/index.html`: auf jeder Ebene scrollend lesen, an interessanten Einträgen vertiefen und zur Leseposition zurückkehren.
- Vollständiges 66-Bücher-Mengengerüst mit 1’189 Kapiteln, 6’704 ausdrücklich technischen Testblöcken und 31’102 Verspositionen; 66 deutsche KI-Buchzusammenfassungen als ungeprüfter Entwurf.
- Mobile-/Tablet-Ansichten, neutrales Hell/Dunkel, Stellensuche, DE/EN-Oberfläche, Textgrösse und eigene Auswahlfelder. Kompaktes SVG-Logo mit gedrehtem B und zwei Quadraten.
- Datenquelle und Grenzen dokumentiert; numerische Kapitel-/Versstruktur unabhängig aus eBible-USFM nachgezählt. Keine neuen kanonischen Text- oder Studiendaten, bestehender Markus-Prototyp unverändert.
- Strukturprüfung mit Node.js ohne Zusatzpakete; DOM-Prüfungen im Arbeitslauf. Visuelle Prüfung auf echten Geräten steht aus.

## v0.10 — 2026-10-09 — Prototyp für allgemeine Leser

- Prototyp nach Rückmeldung neu gestaltet: einfacher und allgemeiner, schlicht, hell/dunkel, mit gezeichnetem Überblicksbild. Drei Wege (Überblick, Lesen, Vertiefen) über eine untere Leiste; Studienpfad; Einstellungen für Lesarten, Urtext-Modus, Schriftgrösse und Farben.
- Abweichende Lesarten: nur Stellen, die die deutsche Übersetzung verändern (6 in Mk 3,20–35), auf Wunsch eingeblendet; Erklärung in einfacher Sprache mit Bezeugung («Steht in 4 von 5 wichtigen Textausgaben»), ohne Entscheidung über richtig/falsch.
- Urtext, Wort für Wort, Grammatik und alle 28 Apparatstellen nur im Modus «Urtext und Details».
- Neue Daten (KI-Entwurf): `alternatives` in den Übersetzungen (deutsche Wiedergabe abweichender Lesarten mit Wirkung «bedeutsam»/«gering»), `summary_de` für die Texteinheiten 3,20–35. Validator prüft, dass jede Alternative auf eine vorhandene Lesart zeigt und ihr Ausgangstext in der Übersetzung vorkommt.

## v0.9 — 2026-10-09 — Studienprototyp Mk 3,20–35

- Klickbarer Prototyp `app/prototype/mk3-20-35.html`, erzeugt mit `scripts/build_prototype.py` aus den Daten des freien Kerns (keine eigenen Inhalte im Prototyp): Zoomstufen Buch → Abschnitt → Einheit → Vers → Wort; Textschichten Deutsch, Griechisch, Wort für Wort; Variantenstellen mit Editionen und Gesichertheitsstufe samt Grenzen der Methode; Wortdetails (Grundform, Häufigkeit in Markus, Form, Satzrolle, Bezug, deutsche Entsprechung, Glossen, Vergleich MACULA/MorphGNT); Kette Befund → Deutung → Prinzip → Anwendung; Studienpfad in sechs Schritten; hell und dunkel, für Smartphones ausgelegt.
- Neue Daten (KI-Entwürfe, ungeprüft): Texteinheiten 3,20–21, 3,31–35 und Abschnitt 3,20–35; Befund FIND-MRK-0005 zur Verschachtelung; Deutung INT-MRK-0003 mit Vorbehalt und Gegenargument; deutsche Arbeitsübersetzung 3,20–21 und 3,31–35 (Wortzuordnung folgt).
- Validator prüft auch `parts` von Texteinheiten.

## v0.8 — 2026-10-09 — Ganzes Markusevangelium, Gesichertheitsbewertung, Lizenzschichten

- Lizenzmodell: eigene Inhalte CC0; freier Kern `data/` (gemeinfrei, CC0, CC BY, CC BY-SA) und Studienschicht `data-nc/` für nicht kommerzielle Quellen, strikt getrennt; Betreiber gemeinnütziger Verein ([LIZENZEN.md](LIZENZEN.md)).
- Text und Annotation getrennt: Token-Sets enthalten nur die Wörter der Edition; sprachliche Angaben liegen als eigene Annotationsschichten daneben.
- Ganzes Markusevangelium importiert: SBLGNT-Text (Faithlife/SBLGNT, Commit `c4d241a9c1c4`, CC BY 4.0) mit 11 286 Wörtern; MACULA Greek (Commit `8423afe47b9e`, CC BY 4.0) als Annotation (Lemma, Morphologie, Syntaxrolle, Referenten, Glossen). MARBLE-Wortbedeutungen bewusst nicht übernommen (nur «used with permission»). Neuer Importer `scripts/import_sblgnt_book.py`.
- Pilot-Token-Set Mk 3,22–30 migriert (`scripts/migrations/v0_8.py`): gleiche Token-IDs jetzt im Kapitel-Set, MorphGNT-Werte unverändert als eigene Schicht, alter Datensatz als `deprecated` erhalten. Zeichen «text»/«word» kommen jetzt aus der Edition (Elision ʼ statt ’ bei MorphGNT); Quellenangaben im Alignment entsprechend neu erzeugt.
- SBLGNT-Apparat für ganz Markus: 929 von 930 Einträgen an Tokens gebunden (neu: Siglen Holmes, Greeven, ⟦WH⟧; mehrere Auslassungen «…»; Markierungen ⸁ und ⸄⸅); 1 versübergreifender Eintrag (7,21–22) bewusst nicht importiert und protokolliert. Die 10 Pilotstellen sind inhaltlich unverändert (jetzt in `data/variants/sblgntapp-mrk/`).
- Gesichertheitsbewertung als Datentyp (`assessment_set`, `assessment_method`) mit Methode «Übereinstimmung der Editionen» und offengelegten Grenzen; für alle 929 Stellen berechnet ([GESICHERTHEIT.md](docs/GESICHERTHEIT.md)).
- Validator prüft zusätzlich Annotationen (Referenten nur als Token-IDs), Bewertungen und die Trennung Kern/Studienschicht; neue Negativtests `scripts/test_validate.py`.
- Unabhängiges Gegenlesen durch einen separaten KI-Durchgang (alle Tokens, alle MACULA-Zeilen, alle 929 Stellen und Bewertungen nachgerechnet). Korrigiert: MACULA-Platzhalter für «kein Referent» nicht mehr als Verweis gespeichert (jetzt `…_unresolved`), MACULA-IDs im Feld `frame` in Token-IDs umgesetzt, Lesarttexte behalten das Elisionszeichen der Edition (ʼ), Lesarten ohne gezählte Edition gekennzeichnet (`no_counted_edition`), Pfad in LIZENZEN.md, Autor der Cherith-Glossen, Migrationsprotokoll um neu erzeugte Änderungen ergänzt.

## 2026-10-09 — Vision und Lizenz

- Vision in vier Stufen festgehalten ([VISION.md](docs/VISION.md)): transparente Textbasis mit Gesichertheitsbewertung statt Lektorat; Übertragung in heutige Zeit, Kultur und Sprachen; Zoomstufen und Studienanleitung; Visualisierung (u. a. Raumobjekte), UX und Beiträge Dritter. Vorgaben und abgeleitete Vorschläge getrennt.
- Lizenz festgelegt: eigene Inhalte CC0 1.0 ([LICENSE](LICENSE)); Fremddaten mit Lizenz in [LIZENZEN.md](LIZENZEN.md); im Kern nur gemeinfreie, CC0- und CC-BY-Quellen.
- Folgerung: MorphGNT-Annotation (CC BY-SA) soll durch eine CC-BY-Annotation ersetzt werden; nicht kommerzielle Datensätze werden nicht übernommen.
- AGENTS.md um Lizenzgrundsatz und «Gesichertheit statt Lektorat» ergänzt.

## 2026-10-09 — Quellenlandschaft für die ganze Bibel

- [QUELLEN.md](docs/QUELLEN.md) auf die ganze Bibel erweitert: AT hebräisch/aramäisch, Septuaginta, NT, alte Übersetzungen, Kirchenväter, Lexika, Kontext; Lizenzen und Zugang je Quelle mit Links.
- Neu: beantragbare Zugänge (INTF, Deutsche Bibelgesellschaft, CATSS, TLG, Brill, Brepols, ETCBC u. a.), Abdeckungsmatrix «nur offene Quellen» und offene Entscheidung zur kommerziellen Nutzung.
- Recherche über die Websites der Anbieter; nicht an Primärquellen bestätigte Angaben sind als [ungeprüft] markiert.

## v0.7 — 2026-10-09 — Varianten auf Editionsebene, vollständige Arbeitsübersetzung

- Quellenlandschaft dokumentiert: [QUELLEN.md](docs/QUELLEN.md) mit Rechte-Ampel und empfohlener Reihenfolge.
- SBLGNT-Apparat (Faithlife/SBLGNT, CC BY 4.0, Commit `c4d241a9c1c4`) für Mk 3,22–30 importiert: 10 Variantenstellen in 3,25–29 mit Lesarten von Westcott-Hort, Tregelles, NA28 und Robinson-Pierpont, als `evidence_level: edition_apparatus` getrennt von Handschriftenbelegen. Neuer Importer `scripts/import_sblgnt_apparatus.py` bindet jede Stelle über die SBLGNT-Markierungen ⸀/⸂⸃ an Token-IDs und prüft die Wortgleichheit.
- Editionsdatensätze für WH, Tregelles, NA28 und Robinson-Pierpont; Quellendatensatz für den Apparat.
- Bestehende Varianten und das Alignment zu Mk 3,29 additiv an Token-IDs gebunden (`scripts/migrations/v0_7.py`, Protokoll in `provenance/migrations/2026-10-09-v0.7.json`).
- Eigene wörtlich orientierte Arbeitsübersetzung Mk 3,22–30 und vollständige Wortzuordnung aller 140 Tokens mit Grammatik- und Alternativnotizen (KI-Entwurf, `draft`); 3,29 unverändert aus der bisherigen Arbeitsübersetzung übernommen. Erzeugt mit `scripts/authoring/mk3_22_30_translation.py`.
- Gegenlesen durch einen separaten KI-Durchgang: drei Fehler korrigiert (3,26 Aorist jetzt «gespalten worden ist»; Notiz zu εἰσελθών; Apparatlesarten nicht mehr pauschal als Ersetzung klassifiziert), mehrere Präzisierungen übernommen (u. a. 3,27 «hineingehen … plündern … plündern»). Keine fachliche Prüfung durch eine Person.
- Validator prüft zusätzlich Token-IDs, Editionen in Lesarten, weitere Verweisfelder und bei `coverage: complete` die lückenlose Zuordnung sowie das Vorkommen jedes Zieltexts in der Übersetzung.
- Pilotstudie führt die neuen Ergebnisse in `outputs`.
- Offen: Zeugenangabe Ephraemi (C) in `VAR-MRK-003-029-001` prüfen; kein automatischer Test für den Apparat-Importer.

## v0.6 — 2026-10-09 — Bibelstellen vereinheitlicht, griechischer Text importiert

- Kanonische Bibelstellen eingeführt (`MRK.3.29`, `MRK.3.22-MRK.3.30`, USFM-Buchcodes) mit Dokumentation [BIBELSTELLEN.md](docs/BIBELSTELLEN.md) und Werkzeug `scripts/refs.py` (Prüfung, Umwandlung deutscher/englischer Eingaben, deutsche Anzeige).
- Bestehende Daten per `scripts/migrations/v0_6.py` migriert: Bibelstellen, Typnamen `study`/`text_unit`, Tippfehler in einem Statuswert, fehlende `outputs` der Pilotstudie. 12 Änderungen protokolliert in `provenance/migrations/2026-10-09-v0.6.json`; Aussagen, Status, Konfidenz und IDs unverändert.
- Schema auf alle Typen und Statuswerte erweitert; Validator prüft jetzt Schema, Verweise zwischen Datensätzen, Lesarten und Bibelstellen.
- Importer korrigiert: MorphGNT-Referenzen haben die Form `0203xx` (Markus = 02), nicht `6203xx`. Quelle, Upstream-Commit, SHA-256, Lizenzangaben und Importdatum werden im Datensatz festgehalten; Import ohne Commit wird abgelehnt.
- Mk 3,22–30 aus MorphGNT SBLGNT 6.12 (Commit `a2afca0e96e3`) importiert: 140 Tokens, 91 Wortformen, 64 Lemmata (`imported_unreviewed`). Zählungen unabhängig gegen die Quelldatei nachgezählt.
- Arbeitstranskription Mk 3,29–30 mit SBLGNT abgeglichen: eine Abweichung (`ἀλλ’`/`ἀλλὰ`).
- Grenzen: keine typspezifischen Schemas, keine Versifikationsprüfung, keine fachliche Prüfung der Morphologie; Lizenzangaben vor Veröffentlichung klären.

## 2026-10-08 — Dokumentation vereinheitlicht

- Eine zentrale README.md für Projektüberblick, Einstieg und vorhandene Programme.
- Versionsnotizen aus den bisherigen READMEs in diesem Changelog zusammengeführt.
- README-v0.3.md, README-v0.4.md, README-v0.5.md und docs/README-original-v0.5.md aus dem aktuellen Dateibaum entfernt.
- Verweise und Herkunftsinventar angepasst. Historische Originaldateien bleiben in Git und den unveränderten ZIP-Paketen erhalten.

## 2026-10-08 — Repository konsolidiert

- Die fünf Paketstände v0.1–v0.5 als einzelne Archiv-Commits übernommen.
- Originalpakete mit SHA-256-Prüfsummen und Dateiinventar archiviert.
- Konzept, Datenmodell, Metadaten, Arbeitsprozess, Entscheidungen, Übersetzungsmethoden und Roadmap dokumentiert.
- Arbeitsregeln für KI-Unterstützung in AGENTS.md ergänzt.
- 36 Datensätze einschliesslich 6 Tags gesichert; bestehende ID-/Tag-Prüfung und synthetische Importtests erfolgreich ausgeführt.
- Grenzen dokumentiert: keine vollständige JSON-Schema-Validierung, noch keine SQLite-Projektion oder Benutzer-App, fehlende Primärquellenprüfung und vollständige Tokenbestände.

## v0.5 — Varianten und Übersetzungszuordnung

- Zweite Variantenstelle zu Mk 3,29 ergänzt: ἐστιν / ἔσται.
- Redaktionelle Entscheidung mit bevorzugter Lesart, Alternative, Begründung, Quellen und Sicherheitsgrad ergänzt.
- Eigene deutsche Arbeitsübersetzung von Mk 3,29 und erste griechisch-deutsche Wort-/Phrasenzuordnungen aufgenommen.
- Bestehenden v0.4-Bestand beibehalten; insgesamt 36 Datensätze einschliesslich 6 Tags.
- Zeugenangaben laut damaligem Arbeitsstand anhand einer Sekundärtranskription verglichen; keine eigene Prüfung von Handschriftenbildern und keine vollständige Kollation der Perikope.
- Griechischer Beispieltext weiterhin Arbeitstranskription, Alignments unvollständig, keine verifizierten Gesamtzahlen für Token oder Lemmata. Die Lesartpräferenz bleibt eine revidierbare Entscheidung.

Quellenhinweise aus den Versionsnotizen:
- https://github.com/morphgnt/sblgnt
- https://www.greeklab.org/interlinear.php?book=Mark&cap=3&verse=29
- https://tips.translation.bible/tip_source/bratcher-nida-1961/page/84/

## v0.4 — Importvorbereitung verbessert

- Erzeugte Token- und Zähldatensätze mit `id`, `type`, `status` und `tags` versehen, damit der vorhandene Validator sie lesen kann.
- Ablehnung fehlerhafter Zielzeilen und unvollständiger Versabdeckung ergänzt; Eingabedatei mit SHA-256 dokumentiert.
- Synthetische Importtests für vollständige und unvollständige Eingaben ergänzt.
- Ablauf festgehalten: konkrete Quelldatei und Upstream-Commit dokumentieren, importieren, validieren und Text/Morphologie an der benannten Edition prüfen.
- Kein echter Quelltext mitgeliefert; keine belastbaren Wortzahlen für Mk 3,22–30 veröffentlicht.

## v0.3 — Editionsgebundener Import vorbereitet

- Editionsobjekt für SBLGNT und Quellenhinweis auf MorphGNT SBLGNT Edition 6.12 ergänzt.
- Importer für eine lokal bereitgestellte MorphGNT-Datei zur Perikope Mk 3,22–30 hinzugefügt; Ausgabe in `data/tokens/` und `data/counts/` vorgesehen.
- Importvorbereitung auf sieben durch Leerzeichen getrennte Spalten und den im Skript erwarteten Referenzcode ausgerichtet. Der Abgleich mit einer tatsächlichen versionierten Quelldatei blieb offen.
- Vollständiger Quellimport, Primärprüfung der Lesarten und Übersetzungsalignment noch ausstehend.

Quellen und Attribution aus den damaligen Notizen: SBL Greek New Testament, herausgegeben von Michael W. Holmes, © Society of Biblical Literature und Logos Bible Software; dort als CC BY 4.0 bezeichnet. MorphGNT SBLGNT Edition 6.12, J. K. Tauber; Morphologie/Lemmatisierung dort als CC BY-SA bezeichnet. Diese übernommenen Angaben ersetzen keine Prüfung der Bedingungen der konkret importierten Fassung.
- https://github.com/Faithlife/SBLGNT
- https://github.com/morphgnt/sblgnt

## v0.2 — Pilotstudie erweitert

- Ersten Studienbericht zu Markus 3,22–30 ergänzt.
- Quellenhinweise, vorläufige Variantenstelle Sünde/Gericht, zusätzliche Befunde, Parallelstellen und eine offene Forschungsfrage aufgenommen.
- Arbeitstranskription von Mk 3,29–30 und ausdrücklich nicht verifizierte Leerzeichenzählungen für diese zwei Verse ergänzt; keine Lemmazählung.
- Insgesamt 30 Datensätze einschliesslich 6 Tags.

## v0.1 — Strukturierter Wissensfundus angelegt

- Pilot Markus 3,22–30 mit Werk, natürlicher Texteinheit, Studie, Befunden, alternativen Interpretationen, Prinzip und kontextabhängiger Anwendung angelegt.
- Historischen Kontext und heutige Anwendung CH/de-CH 2026 getrennt; Themen und 6 kontrollierte Tags eingeführt.
- Stabile IDs, Tag-Referenzen, frühe Wissenszeit-/Vorgängerfelder, generisches Schema und einfachen Validator angelegt; insgesamt 19 Datensätze einschliesslich Tags.
- Git als massgebliche Quelle festgehalten; SQLite als spätere abgeleitete Projektion vorgesehen.
- Fachliche Aussagen als vorläufig markiert; geprüfte Textbestände, genaue Quellenbelege und Argument-/Evidenzobjekte als nächste Arbeiten festgehalten.
