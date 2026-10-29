# Weiterdenken: Brücke, Fragen, Rezeption, Anwendung

Stand 2026-10-29 (Prüfvermerk, Zitate wörtlich, Kirchliche Lehre), Grundsatz festgelegt von Andi Neck am 2026-10-28 (vorher «Damals → Prinzip → Heute», Stand 2026-10-23; frühere Fassung im
Git-Verlauf und als Prozess PROC-DAMALS-HEUTE 1.0). Diese Regel beantwortet, wo wir beim Wortlaut bleiben, wo wir für eine
andere Zeit, Kultur oder Zielgruppe übertragen und wie die App zum Weiterdenken anregt, ohne die Antwort vorwegzunehmen.

## Grundsatz

Wir übersetzen den Text nicht in die heutige Zeit, sondern bauen eine Brücke daneben. Jede Ebene hat eine feste Aufgabe, und
in der App ist immer sichtbar, auf welcher man ist. Heutiges (z. B. soziale Medien) steht nie im Bibeltext, in der
Zusammenfassung oder im Bild, sondern höchstens in einer Anwendung, gekennzeichnet und für eine bestimmte Zielgruppe.

| Ebene | Aufgabe | wo in der App | Beispiel Mt 6,5–6 |
|---|---|---|---|
| Bibeltext (`translation`) | treu zum Urtext; heutige Wörter nur, wo die Bedeutung gleich bleibt (als `decisions` festgehalten) | Lesetext | «geh in deine Kammer, schliess deine Tür» |
| Kernanalyse, Zusammenfassung, Bild | verdichten, was dasteht; Bilder zeigen die Welt von damals ([VERDICHTUNG.md](VERDICHTUNG.md)) | Ebene selbst; Kernaussage unter Verstehen | Strassenecke gegenüber Kammer mit geschlossener Tür |
| **Damals** (`background_note`) | erklärt Zeit, Ort, Kultur und fremde Begriffe | Verstehen › «Umfeld damals» | «Heuchler» hiess ursprünglich Schauspieler |
| **Brücke** (`principle`) | was über die Zeit hinaus gilt; als Folgerung gekennzeichnet, nicht als Befund | Weiterdenken, Titel je Textart | Frömmigkeit ist kein Auftritt vor Publikum |
| **Fragen** (`reflection`) | zum Weiterdenken anregen, ohne zu antworten | Weiterdenken oben und «Weitere Fragen» | Für wen betest du eigentlich? |
| **Wie man es gelesen hat** (`reception`) | Rezeption: Auslegung, Liturgie, Kunst, Forschung | Weiterdenken | Kirchenväter, Reformation … |
| **Heute** (`application`) | Übertragung für eine Zielgruppe (`context`), mit Grenze | Weiterdenken, nur mit Einstellung «Anwendungsideen zeigen» (Standard aus) | Jugendliche: Glauben nicht für Likes inszenieren |

## Brücke je Textart

Der Grundsatz heisst in der App nach der Textart (`mode` der Kernanalyse, [STRUKTURKATALOG.md](STRUKTURKATALOG.md)), damit
deutlich ist, was er ist:

| Textart | Titel der Brücke |
|---|---|
| Weisung, Rede, Aussage, Brief, Weisheit (`instruction`, `speech`, `statement`, `letter`, `wisdom`) | «Grundsatz» |
| Erzählung (`narrative`) | «Was die Erzählung zeigt» |
| Gleichnis (`parable`) | «Was das Gleichnis zeigt» |
| Gesetz (`law`) | «Wie Traditionen damit umgehen» |
| Psalm, Gebet (`psalm`, `prayer`) | «Mitbeten» |
| Prophetie, Apokalyptik (`prophecy`, `apocalyptic`) | «Wie es gelesen wurde» |
| Liste, Genealogie (`list`, `genealogy`) | keine Brücke (gibt es dennoch einen Grundsatz, heisst er «Grundsatz») |

Inhalt sind die Grundsätze (`principle`). Ein Grundsatz erscheint bei **allen** Abschnitten, deren Befunde oder Deutungen in
`derived_from` stehen (Projektion `subjects`), nicht nur beim ersten; auf Kapitelebene gesammelt mit Stelle.

## Fragen zum Weiterdenken (`reflection`)

`data/reflections/REFL-<BUCH>-nnnn.json`: `subject` (Texteinheit `TU-…` oder Zusammenfassung einer oberen Ebene `SUM-…`),
`question_de` (endet mit «?», auch «…?» bzw. «?»» bei einem Zitat am Schluss), `note_de` (höchstens ein Satz Hintergrund mit
Stelle, optional), `order`, `status` (`draft`), `process` («PROC-WEITERDENKEN@Fassung»), `authorship_de`, `tags`, `knowledge`,
`check` (Prüfvermerk, siehe unten), `revision_log` (bei Änderungen). Fragen und Hintergrund zu Bibel, Testamenten und
Buchgruppen tragen das Präfix `ALL` (`REFL-ALL-nnnn`, `RCPT-ALL-nnnn`, Datenmodul `ALL.py`); ihr `subject` ist `SUM-BIBLE`,
`SUM-OT`/`SUM-NT` oder `SUM-GROUP-nn` (in der App der Schlüssel `GROUP-nn`).

- **Zitate wörtlich:** Was in «…» steht, ist ein Zitat und steht wörtlich (Auslassungen mit «…») im Bibeltext der Stelle –
  Hochdeutsch in der hochdeutschen Arbeitsübersetzung, die Mundart-Fassung in der Mundart-Arbeitsübersetzung. Gesucht wird in
  den Stellenmarken des Texts und in der Stelle des Bezugs. Begriffe, Gegenformulierungen oder andere mögliche Übersetzungen
  stehen ohne Zitatzeichen. Der Validator prüft das (`scripts/zitate.py`); Zitate aus Büchern ohne Arbeitsübersetzung meldet
  er nur als Hinweis. Dasselbe gilt für die Kernaussage (`gist_de`) der Kernanalysen.

- Zwei bis vier Fragen je Abschnitt, aus dem Text gewonnen: offenes Ende, Leerstelle, Frage des Textes selbst, Wer-zu-wem.
  Keine Suggestivfrage, keine versteckte Deutung als Tatsache, keine Antwort.
- Die erste Frage ist die grosse Frage oben im Reiter; «Nächste Frage ›» blättert weiter.
- Kapitel und höhere Ebenen: eine Frage der Ebene (Abschnitt, der das ganze Kapitel umfasst, bzw. `SUM-…`). Die erste Frage
  jeder Ebene (oder, wenn sie keine hat, die erste darunter) ist die **Tür von oben**: Buch, Buchgruppe, Testament und
  Bibel zeigen je Kind eine Frage («In den Kapiteln weiterdenken» …).

## Wie man es gelesen hat (`reception`)

`data/receptions/RCPT-<BUCH>-nnnn.json`: `subject`, `tradition` (`jewish`, `church_fathers`, `liturgy`, `art`, `music`,
`literature`, `reformation`, `modern_scholarship`, `church_teaching` – kirchliche Lehräusserungen wie Konzilien, Enzykliken,
Bekenntnisschriften, in der App «Kirchliche Lehre», seit 2026-10-29), `period_de`, `text_de` (eigene Worte), `sources_de`,
`confidence` (`high`, `probable`, `possible`), optional `uncertain_de` und `source_check` (wie bei Hintergrund,
[QUELLENPRUEFUNG.md](QUELLENPRUEFUNG.md)), `process`, `authorship_de`, `check`.

- Stimmen nebeneinander, keine wird als die richtige gewertet; problematische Wirkungen (z. B. judenfeindliche Lesarten)
  werden benannt.
- Quellen nur, wo sie sicher sind; sonst ohne Stellenangabe und mit dem Vermerk «Stellenangabe nicht nachgeschlagen
  (ungeprüft)». Ohne `source_check` zeigt die App «Quellen noch nicht nachgeschlagen».

## Prüfvermerk (`check`)

Seit 2026-10-29 (PROC-WEITERDENKEN 1.1) tragen Fragen und Rezeption einen Prüfvermerk der weiteren Instanz, die sie gegen den
Text geprüft hat: `check` = {`date`, `by` (z. B. «weitere Instanz (KI)»), `result` (`confirmed` bestätigt, `corrected` in der
Prüfung berichtigt; die Berichtigung steht im `revision_log`), `limits_de` (was nicht geprüft wurde, z. B. nicht gegen den
Urtext, keine fachliche und keine muttersprachliche Prüfung), optional `process`}. Ein Eintrag ohne `check` ist noch nicht von
einer weiteren Instanz geprüft. Die App zeigt den Vermerk einmal unter «Wie das entstanden ist» (ohne Hinweis auf KI); er
ersetzt keine fachliche Prüfung. Im Datenmodul: `CHECK` und `CHECK_CORRECTED` für alle Einträge, `check` (auch `None`) je
Eintrag. Das erstmalige Eintragen eines Prüfvermerks ist keine inhaltliche Revision (kein `revision_log`).

Beide Typen werden wie andere Erklärtexte lokalisiert (`localization`, Felder `question_de`, `note_de` bzw. `period_de`,
`text_de`). Werkzeug: `scripts/authoring/weiterdenken.py` mit Datenmodulen `scripts/authoring/weiterdenken_daten/<BUCH>.py`
(Urheberschaft, Prozess, Datum und Prüfvermerk je Eintrag möglich; revision_log nur für Dateien, die Git schon erfasst hat; ein
Eintrag je Tag und Grund; auch gestrichene Felder). Prozess: PROC-WEITERDENKEN ([PROZESSE.md](PROZESSE.md)).

## Wo die Grenze liegt

- **Im Bibeltext erlaubt:** ein heute verständliches Wort mit derselben Bedeutung (z. B. «Zimmer» statt «Kammer», wenn das
  griechische Wort das trägt), eine einfachere Sprachebene in einer eigenen Fassung (eigene Übersetzungsschicht mit
  `target_context` und `register_de`, aus dem Urtext). Jede bewusste Abweichung vom Wörtlichen steht in `decisions`.
- **Im Bibeltext nicht erlaubt:** heutige Gegenstände, Medien, Institutionen oder Beispiele, die der Text nicht nennt
  («Instagram», «Franken»). Masse, Münzen und Bräuche bleiben; ihr heutiger Gegenwert steht unter «Damals».
- **Zusammenfassung und Bild** bleiben in der Welt des Textes. Ein heutiges Bild wäre eine Anwendung und gehört, wenn
  überhaupt, als eigenes, gekennzeichnetes Bild zur Anwendung.
- **Grundsatz:** so allgemein, dass er für alle Zielgruppen gilt, so nah am Text, dass man die Herleitung sieht
  (`derived_from` auf Befund oder Deutung).
- **Fragen** regen an und lassen offen; sie geben keine Antwort vor.
- **Heute:** immer mit Zielgruppe (`context`), mit Grenze (`limitations_de`: was der Text nicht sagt) und als
  Anwendung gekennzeichnet; nur sichtbar, wenn Lesende «Anwendungsideen zeigen» einschalten. Mehrere Anwendungen
  nebeneinander sind erwünscht; keine gilt als die richtige.

## Münzen und Gewichte

Entscheid Andi Neck 2026-10-26: «Geld ist ein Wertmittel (von dem her braucht es bildlich keine Unterscheidung); die damaligen Münznamen in den Text und die Umrechnung in die Erklärung.»

- **Bibeltext:** die damaligen Namen, nie heutige oder Schweizer Geldwörter («Rappen», «Batzen», «Groschen», «Franken»). Einheitliche Schreibung, Hochdeutsch / Züridüütsch (Mehrzahl in Klammern):

  | Urtext | Hochdeutsch | Züridüütsch | Wert (für die Erklärung) |
  |---|---|---|---|
  | δηνάριον | Denar (Denare) | Denar (Denar) | römische Silbermünze, üblicher Tageslohn eines Arbeiters ([[MAT.20.2]]) |
  | ἀσσάριον | As, der (Asse) | As, de (As) | Kupfermünze, 1/16 Denar |
  | κοδράντης | Quadrans, der | Quadrans, de | kleinste römische Münze, 1/4 As = 1/64 Denar |
  | λεπτόν | Lepton, das (Lepta) | Lepton, s (Lepta) | kleinste Kupfermünze im Land, 1/2 Quadrans = 1/128 Denar ([[MRK.12.42]]) |
  | δραχμή | Drachme (Drachmen) | Drachme (Drachme) | griechische Silbermünze, etwa ein Denar |
  | δίδραχμον | Doppeldrachme | Doppeldrachme | zwei Drachmen, der halbe Schekel der Tempelabgabe ([[EXO.30.13]]) |
  | στατήρ | Stater | Stater | Silbermünze zu vier Drachmen |
  | μνᾶ | Mine (Minen) | Mine (Mine) | Rechnungseinheit von 100 Drachmen, etwa 100 Tageslöhne |
  | τάλαντον | Talent (Talente) | Talänt (Talänt) | Gewicht von rund 26–36 kg Silber, etwa 6000 Denare |
  | ἀργύριον | Einzahl «Silber», Mehrzahl ἀργύρια «Silberstücke» | «Silber», «Silberstück» | Geld in Silbermünzen; welche, sagt der Text meist nicht |
  | χαλκός | Kupfergeld | Chupfergäld | Kleingeld in Kupfermünzen |

  Allgemeines Geld heisst in der Mundart einheitlich «Gäld» (nicht «Gält»).
- **Erklärung:** Der Wert steht in der Übersetzungsentscheidung der Stelle (`decisions`) und, wo es hilft, in einer Hintergrundnotiz (z. B. BG-LUK-0019, BG-MAT-3017, BG-MAT-4014). Ein heutiger Vergleich (etwa in Franken) gehört höchstens in eine Anwendung mit Zielgruppe und Grenze, nie in den Bibeltext, die Zusammenfassung oder das Bild.
- **Bild:** ein einziges Geld-Zeichen für alle Münzen; die Menge zeigt, wo nötig, die Zahl der Zeichen ([BILDSPRACHE.md](BILDSPRACHE.md)).

## Zielgruppen

Zielgruppen sind `context`-Datensätze mit `label_de` (kurzer Name für die Anzeige bei der Anwendung), `audience` und `situation_de`
(was diese Gruppe heute prägt). Vorhanden:

- `CTX-CH-DE-2026` – Allgemein: deutschsprachige heutige Bibellesende;
- `CTX-CH-YOUTH-2026` – Jugendliche: Jugendliche und junge Erwachsene in der Schweiz.

Weitere (Familie, Beruf, Kirche, Menschen ohne kirchlichen Hintergrund) werden nach Bedarf ergänzt.

Grundsätze und Anwendungen erscheinen nur bei Abschnitten, deren Verse sie betreffen. Massgeblich ist das Feld
`reference`, z. B. `MAT.6.5-MAT.6.6`. Fehlt es, gilt bei Grundsätzen die erste Stellen-Marke ihrer Aussage und bei
Anwendungen der Bereich ihres Grundsatzes.

## In der App

Die Kernaussage (`gist_de`) steht auch auf Züridüütsch (Lokalisierung, `scripts/authoring/kernanalyse.py`, Feld `gsw` im
Datenmodul) und erscheint im gewählten Lesetext; die übrige Kernanalyse nur Hochdeutsch.

Am Titel jeder Ebene öffnet «Vertiefen» ein Blatt mit den Reitern «Verstehen» und «Weiterdenken»
([LESEN-UND-VERTIEFEN.md](LESEN-UND-VERTIEFEN.md)). «Damals» steht unter Verstehen › «Umfeld damals». Weiterdenken zeigt oben
die Frage, darunter die Brücke, «Wie man es gelesen hat», «Weitere Fragen» und, wenn eingeschaltet, «Anwendungsideen» mit
Zielgruppe und Grenze; auf Kapitel- und höheren Ebenen zusätzlich je Kind eine Frage als Tür nach unten.

## Stand (2026-10-29)

Pilot war Lukas 15 (2026-10-28). Seither haben alle ausgearbeiteten Bücher Kernaussagen, Fragen und Rezeption (KI-Entwurf,
von einer weiteren Instanz gegen den Text geprüft, Prüfvermerk `check`; keine fachliche Prüfung):

| Buch | Kernaussagen (`gist_de`, auch Mundart) | Fragen | Wie man es gelesen hat |
|---|---:|---:|---:|
| Matthäus | 176 | 378 | 15 |
| Markus | 108 | 220 | 14 |
| Lukas | 160 | 353 | 18 |
| Johannes | 127 | 250 | 17 |
| Rut, Jona, Obadja, Philipper, Titus, 1.–3. Johannesbrief und obere Ebenen | 102 | 213 | 51 |

Die jüdischen Stimmen zu Lukas und Johannes (RCPT-LUK-0017/0018, RCPT-JHN-0016/0017) sind nach der Prüfrunde ergänzt und am
2026-10-29 von einer getrennten Instanz nachgeschlagen und geprüft (drei berichtigt, eine bestätigt). Anwendungen: Mt 6,5–6 mit der Zielgruppe «Jugendliche» (`APP-MAT-1007`).
