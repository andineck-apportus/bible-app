# Weiterdenken: Brücke, Fragen, Rezeption, Anwendung

Stand 2026-10-28, festgelegt von Andi Neck (vorher «Damals → Prinzip → Heute», Stand 2026-10-23; frühere Fassung im
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
`question_de` (endet mit «?»), `note_de` (höchstens ein Satz Hintergrund mit Stelle, optional), `order`, `status` (`draft`),
`process` («PROC-WEITERDENKEN@Fassung»), `authorship_de`, `tags`, `knowledge`, `revision_log` (bei Änderungen).

- Zwei bis vier Fragen je Abschnitt, aus dem Text gewonnen: offenes Ende, Leerstelle, Frage des Textes selbst, Wer-zu-wem.
  Keine Suggestivfrage, keine versteckte Deutung als Tatsache, keine Antwort.
- Die erste Frage ist die grosse Frage oben im Reiter; «Nächste Frage ›» blättert weiter.
- Kapitel und höhere Ebenen: eine Frage der Ebene (Abschnitt, der das ganze Kapitel umfasst, bzw. `SUM-…`). Die erste Frage
  jeder Ebene (oder, wenn sie keine hat, die erste darunter) ist die **Tür von oben**: Buch, Buchgruppe, Testament und
  Bibel zeigen je Kind eine Frage («In den Kapiteln weiterdenken» …).

## Wie man es gelesen hat (`reception`)

`data/receptions/RCPT-<BUCH>-nnnn.json`: `subject`, `tradition` (`jewish`, `church_fathers`, `liturgy`, `art`, `music`,
`literature`, `reformation`, `modern_scholarship`), `period_de`, `text_de` (eigene Worte), `sources_de`, `confidence`
(`high`, `probable`, `possible`), optional `uncertain_de` und `source_check` (wie bei Hintergrund,
[QUELLENPRUEFUNG.md](QUELLENPRUEFUNG.md)), `process`, `authorship_de`.

- Stimmen nebeneinander, keine wird als die richtige gewertet; problematische Wirkungen (z. B. judenfeindliche Lesarten)
  werden benannt.
- Quellen nur, wo sie sicher sind; sonst ohne Stellenangabe und mit dem Vermerk «Stellenangabe nicht nachgeschlagen
  (ungeprüft)». Ohne `source_check` zeigt die App «Quellen noch nicht nachgeschlagen».

Beide Typen werden wie andere Erklärtexte lokalisiert (`localization`, Felder `question_de`, `note_de` bzw. `period_de`,
`text_de`). Werkzeug: `scripts/authoring/weiterdenken.py` mit Datenmodulen `scripts/authoring/weiterdenken_daten/<BUCH>.py`.
Prozess: PROC-WEITERDENKEN ([PROZESSE.md](PROZESSE.md)).

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

Am Titel jeder Ebene öffnet «Vertiefen» ein Blatt mit den Reitern «Verstehen» und «Weiterdenken»
([LESEN-UND-VERTIEFEN.md](LESEN-UND-VERTIEFEN.md)). «Damals» steht unter Verstehen › «Umfeld damals». Weiterdenken zeigt oben
die Frage, darunter die Brücke, «Wie man es gelesen hat», «Weitere Fragen» und, wenn eingeschaltet, «Anwendungsideen» mit
Zielgruppe und Grenze; auf Kapitel- und höheren Ebenen zusätzlich je Kind eine Frage als Tür nach unten.

## Pilot

Fragen und Rezeption: Lukas 15 (Kapitel und drei Abschnitte, 2026-10-28, KI-Entwurf). Anwendungen: Mt 6,5–6 mit der
Zielgruppe «Jugendliche» (`APP-MAT-1007`). Die übrigen Inhalte entstehen in eigenen Runden.
