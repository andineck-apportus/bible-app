# Damals → Prinzip → Heute

Stand 2026-10-23, festgelegt von Andi Neck. Diese Regel beantwortet, wo wir beim Wortlaut bleiben und wo wir für eine andere
Zeit, Kultur oder Zielgruppe übertragen.

## Grundsatz

Wir übersetzen den Text nicht in die heutige Zeit, sondern bauen eine Brücke daneben. Jede Ebene hat eine feste Aufgabe, und
in der App ist immer sichtbar, auf welcher man ist. Heutiges (z. B. soziale Medien) steht nie im Bibeltext, in der
Zusammenfassung oder im Bild, sondern in der Anwendung, gekennzeichnet und für eine bestimmte Zielgruppe.

| Ebene | Aufgabe | Beispiel Mt 6,5–6 |
|---|---|---|
| Bibeltext (`translation`) | treu zum Urtext; heutige Wörter nur, wo die Bedeutung gleich bleibt (als `decisions` festgehalten) | «geh in deine Kammer, schliess deine Tür» |
| Kernanalyse, Zusammenfassung, Bild | verdichten, was dasteht; Bilder zeigen die Welt von damals ([VERDICHTUNG.md](VERDICHTUNG.md)) | Strassenecke gegenüber Kammer mit geschlossener Tür |
| **Damals** (`background_note`) | erklärt Zeit, Ort, Kultur und fremde Begriffe | «Heuchler» hiess ursprünglich Schauspieler; die Kammer war der Innenraum ohne Fenster |
| **Prinzip** (`principle`) | was über die Zeit hinaus gilt; als Folgerung gekennzeichnet, nicht als Befund | Frömmigkeit ist kein Auftritt vor Publikum; Gott sieht, was niemand sieht |
| **Heute** (`application`) | Übertragung für eine Zielgruppe (`context`), mit Grenze | Jugendliche: Glauben nicht für Likes inszenieren |

## Wo die Grenze liegt

- **Im Bibeltext erlaubt:** ein heute verständliches Wort mit derselben Bedeutung (z. B. «Zimmer» statt «Kammer», wenn das
  griechische Wort das trägt), eine einfachere Sprachebene in einer eigenen Fassung (eigene Übersetzungsschicht mit
  `target_context` und `register_de`, aus dem Urtext). Jede bewusste Abweichung vom Wörtlichen steht in `decisions`.
- **Im Bibeltext nicht erlaubt:** heutige Gegenstände, Medien, Institutionen oder Beispiele, die der Text nicht nennt
  («Instagram», «Franken»). Masse, Münzen und Bräuche bleiben; ihr heutiger Gegenwert steht unter «Damals».
- **Zusammenfassung und Bild** bleiben in der Welt des Textes. Ein heutiges Bild wäre eine Anwendung und gehört, wenn
  überhaupt, als eigenes, gekennzeichnetes Bild zur Anwendung.
- **Prinzip:** so allgemein, dass es für alle Zielgruppen gilt, so nah am Text, dass man die Herleitung sieht
  (`derived_from` auf Befund oder Deutung).
- **Heute:** immer mit Zielgruppe (`context`), mit Grenze (`limitations_de`: was der Text nicht sagt) und als
  Anwendung gekennzeichnet. Mehrere Anwendungen nebeneinander sind erwünscht; keine gilt als die richtige.

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

Zielgruppen sind `context`-Datensätze mit `label_de` (kurzer Name für die Auswahl in der App), `audience` und `situation_de`
(was diese Gruppe heute prägt). Vorhanden:

- `CTX-CH-DE-2026` – Allgemein: deutschsprachige heutige Bibellesende;
- `CTX-CH-YOUTH-2026` – Jugendliche: Jugendliche und junge Erwachsene in der Schweiz.

Weitere (Familie, Beruf, Kirche, Menschen ohne kirchlichen Hintergrund) werden nach Bedarf ergänzt.

Grundsätze und Anwendungen erscheinen nur bei Abschnitten, deren Verse sie betreffen. Massgeblich ist das Feld
`reference`, z. B. `MAT.6.5-MAT.6.6`. Fehlt es, gilt bei Grundsätzen die erste Stellen-Marke ihrer Aussage und bei
Anwendungen der Bereich ihres Grundsatzes.

## In der App

Am Abschnittstitel öffnet «Damals → Heute» ein Blatt mit drei Stufen: Damals (Hintergrund), Prinzip, Heute. Unter «Heute»
wählt man die Zielgruppe; die Wahl bleibt gespeichert. «Verstehen» zeigt weiterhin, was dasteht und wie man es verstehen kann.

## Pilot

Mt 6,5–6 mit der Zielgruppe «Jugendliche» (`APP-MAT-1007`). Danach weitere Abschnitte der Bergpredigt.
