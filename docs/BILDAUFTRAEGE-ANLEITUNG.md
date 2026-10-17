# Bildaufträge schreiben (für alle Stellen eines Buches)

Seit v0.65 entstehen die Bilder der übersetzten Bücher nicht mehr einzeln von Hand, sondern werden vom Zeichner
(`scripts/authoring/bilder_auto.py`) in beiden Stilen (Symbol, Anime) direkt aus dem Bildauftrag gesetzt. Wer einen Bildauftrag
schreibt, legt also fest, **was** zu sehen ist; das **Wie** übernimmt der Zeichner, gesteuert über wenige Hinweise (`stage`).
Grundsätze der Bildsprache: [BILDSPRACHE.md](BILDSPRACHE.md). Vorbild: `scripts/authoring/bildauftraege_daten/JON.json`.

## Dateien je Buch

| Datei | Inhalt |
|---|---|
| `scripts/authoring/bildauftraege_daten/<BUCH>.json` | Liste der Bildaufträge (Buch, Kapitel, Abschnitte) |
| `scripts/authoring/bildlexikon_daten/<BUCH>.json` | neue Lexikon-Einträge (Personen, Gegenstände, Orte, Zeichen) |
| `scripts/authoring/bildsymbole_daten/<BUCH>.json` | Zeichnungen (SVG) für neue Gegenstände, Orte und Zeichen |
| `scripts/authoring/figuren_daten/<BUCH>.json` | Aussehen neuer Personen und Rollen (Farben, Haar, Bart, Kopfbedeckung, Attribut) |

Danach in dieser Reihenfolge ausführen: `bildlexikon.py`, `bildauftraege.py`, `bilder_symbol.py`, `bilder_anime.py`
(alle in `scripts/authoring/`), dann `scripts/validate.py`.

## Ebenen und Ziele

- **Buch** (`level: book`, `reference: "RUT"`, `target: "SUM-BOOK-RUT"`, `translation: null`): 2–4 Felder mit den Hauptstationen.
- **Kapitel** (`level: chapter`, `reference: "RUT.1"`, `target: "SUM-CH-RUT-001"`, falls vorhanden, sonst die Kapitel-Einheit `TU-…`; `translation: null`):
  je Abschnitt des Kapitels ein Feld, höchstens 4 (bei mehr Abschnitten die wichtigsten zusammenfassen).
- **Abschnitt** (`level: section`, `reference` und `target` des Abschnitts `TU-…`, `translation` = hochdeutsche Arbeitsübersetzung des Kapitels):
  1–4 Felder in der Reihenfolge des Textes; jedes Feld nennt seinen Versbereich.
- `suffix`: wie die Ziel-ID ohne `TU-`/`SUM-CH-`/`SUM-BOOK-` (z. B. `RUT-001-001-005`, `RUT-001`, `RUT`).

## Ein Feld

```json
{"n": 1, "reference": "JON.1.1-JON.1.2",
 "figures": ["FIG-GOTT", "FIG-JONA"],          // Personen in der Reihenfolge links → rechts; Gott/Geist kommen nach oben
 "objects": ["FIG-ORT-NINIVE"],                // Orte und Gegenstände
 "signs": ["FIG-ZEICHEN-FREUDE"],              // Zeichen
 "speech": [{"from": "FIG-GOTT", "to": "FIG-JONA", "icons": ["FIG-ORT-NINIVE", "FIG-ZEICHEN-VERKUENDIGEN"]}],
 "action_de": "…", "action_gsw": "…",          // Handlung nach dem Text, ein bis zwei Sätze
 "caption_de": "Kurztitel: was man sieht (Zeichen erklärt).", "caption_gsw": "…",
 "stage": {…}}                                  // Hinweise an den Zeichner (optional)
```

Prüfen wie eine Zusammenfassung: Handelnde, wer zu wem, Zeitform, Ankündigung statt Bericht; nichts zeigen, was der Text nicht
sagt (oder es in `note_de` als Deutung benennen). Sprechblasen nur mit Zeichen (keine Wörter, keine Zahlen; höchstens 6 Zeichen).
Mehrzahl («ihr», «die Leute») als Gruppe (`FIG-GRUPPE-…`), nie als Einzelfigur. Gewalt nicht ausmalen (Kreuz ohne Körper, Schlag
nicht zeigen). «Die Juden», Pharisäer, Hohepriester als neutrale Figuren, nie verzerrt.

## Hinweise an den Zeichner (`stage`)

| Schlüssel | Wirkung |
|---|---|
| `mood: {FIG: expr}` | Ausdruck im Stil Anime: calm, smile, delight, worried, surprised, earnest, determined, pensive, sleep |
| `pose: {FIG: p}` | lie, sleep, sit, kneel, fall, away (abgewandt) |
| `hold: {FIG: OBJ}` | Figur hält Gegenstand (Gegenstand muss in `objects` stehen) |
| `in: {FIG: OBJ}`, `in_pos: {FIG: [x, y]}` | Figur im Gegenstand (Boot, Fisch, Grab …), Lage relativ 0–1 |
| `at: {ZEICHEN: FIG}` | Zeichen bei einer Figur (z. B. Zorn, Schlafen) |
| `signs_who: {ZEICHEN: [FIG…]}` | wer Tränen/Freude/Herz trägt (Standard: alle Personen ausser Jesus) |
| `count: {ID: n}` | Anzahl (z. B. drei Sonnen, fünf Brote; höchstens 7) |
| `split: n` | gestrichelte Linie (Abstand) nach der n-ten Person |
| `god_side`, `back_side`, `big_side`, `floor_side` | left/right (Gott: auch center) |
| `flip: [OBJ]` | grosser Gegenstand gespiegelt (z. B. Fisch schaut nach rechts) |
| `floor_x: {OBJ: x}`, `air_x`, `air_y`, `big_y`, `bubble_y` | Feinlage in Feldeinheiten (Feld 186 × 140, Boden bei 118) – sparsam |
| `x: {FIG: x}` | Lage einer Person (Mitte, Feldeinheiten); schaltet die automatische Leserichtung ab |
| `arrows: [[von, zu, art]]` | Handlungslinie: `act` (senden, sehen, heilen; von Gott golden), `throw` (werfen, speien), `go` (gehen, gestrichelt). Von und zu Personen setzt der Zeichner die Linie über die Köpfe bzw. auf Schulterhöhe |
| `beside: {ZEICHEN: FIG}` | Zeichen neben dem Kopf statt darüber (z. B. heilende Hand, Fragezeichen) |
| `behind: [OBJ]` | Gegenstand am Boden hinter den Personen |
| `before: true` | Personen stehen vor dem Gebäude im Hintergrund (Gebäude nicht ausweichen) |
| `wear: {FIG: sack \| binden \| #RRGGBB}` | Kleidung: Sacktuch, Leinenbinden oder andere Mantelfarbe |
| `in_water: true`, `sea: "calm"` | Personen stehen im Wasser (kein Uferstreifen); See ruhig statt bewegt |
| `at_top: true` | Zeichen bei einer Figur im Gegenstand oben statt seitlich |

Automatisch (seit dem Blindtest vom 2026-10-17): Wer zuerst spricht, steht links vom zweiten Sprecher (ausser `x`, `split` oder
«links/rechts» in der Legende); eine zweite Sprechblase derselben Figur steht neben der ersten und ist mit ihr verbunden;
Gruppen erscheinen als Menge (drei Figuren vorn, zwei dahinter). Die Legende (`caption_de`) muss beschreiben, was das Zeichen im
Bild tatsächlich zeigt (gleiche Wörter wie das Merkmal im Bildlexikon), sonst sucht man vergeblich.

Platzierung je Eintrag (in `bildsymbole_daten`: `place`): `band` (Hintergrund über die ganze Breite: Meer, See, Feld),
`back` (Gebäude im Hintergrund), `big` (gross in der Mitte: Schiff, Fisch, Grab), `floor` (am Boden), `hand` (klein, in der Hand),
`air` (frei oben), `head` (bei den Köpfen), `line` (zwischen Figuren).

## Neue Lexikon-Einträge

Aufbau wie in `bildlexikon_daten/JON.json`: `id` (`FIG-…`, gleiche Namen für gleiche Dinge in allen Büchern, z. B. `FIG-ZEICHEN-LIEBE`),
`kind` (person, role, group, object, place, action, sign), Namen de/en, `ident`/`gsw` (ein Satz mit Stelle), `traits` mit `basis`
(`text` nur mit `ref`, sonst `tradition` oder `design`), Palette, Regeln, bei Personen und Rollen `era`, optional `find` (Suchmuster
für «kommt vor in»). Personen und Rollen brauchen ein Aussehen in `figuren_daten`, alles andere eine Zeichnung in `bildsymbole_daten`
(`{"FIG-…": {"sym": "ill-…", "vb": "0 0 w h", "svg": "…", "place": "floor", "size": [w, h]}}`, flache Formen, Strich `#3B3226`,
keine Schrift).
