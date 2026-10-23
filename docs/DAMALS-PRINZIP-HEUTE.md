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

## Zielgruppen

Zielgruppen sind `context`-Datensätze mit `label_de` (kurzer Name für die Auswahl in der App), `audience` und `situation_de`
(was diese Gruppe heute prägt). Vorhanden:

- `CTX-CH-DE-2026` – Allgemein: deutschsprachige heutige Bibellesende;
- `CTX-CH-YOUTH-2026` – Jugendliche: Jugendliche und junge Erwachsene in der Schweiz.

Weitere (Familie, Beruf, Kirche, Menschen ohne kirchlichen Hintergrund) werden nach Bedarf ergänzt.

Eine Anwendung kann mit `reference` auf einen Teil des Prinzips eingeschränkt werden (z. B. `MAT.6.5-MAT.6.6`); die App zeigt
sie dann nur bei Abschnitten, die diese Verse enthalten.

## In der App

Am Abschnittstitel öffnet «Damals → Heute» ein Blatt mit drei Stufen: Damals (Hintergrund), Prinzip, Heute. Unter «Heute»
wählt man die Zielgruppe; die Wahl bleibt gespeichert. «Verstehen» zeigt weiterhin, was dasteht und wie man es verstehen kann.

## Pilot

Mt 6,5–6 mit der Zielgruppe «Jugendliche» (`APP-MAT-1007`). Danach weitere Abschnitte der Bergpredigt.
