# Anleitung: Buchgerüst je Buch (Buchebene, Form je Station)

Entscheid Andi Neck 2026-11-21 ([docs/VISUELLE-SPRACHE.md](../../../../docs/VISUELLE-SPRACHE.md), [docs/ENTSCHEIDUNGEN.md](../../../../docs/ENTSCHEIDUNGEN.md)).
Je Buch eine Datei `buch/<BUCH>.json` (USFM-Code, z. B. `GEN.json`). Format: `python3 scripts/authoring/buchgeruest.py` ohne Argumente
zeigt es; vollständiges Beispiel: `buch/TIT.json`. Prüfen: `python3 scripts/authoring/buchgeruest.py pruefen GEN` muss «in Ordnung» melden.

## Stationen wählen

- 4–6 Stationen je Buch (3 bei sehr kurzen Büchern wie Obd, Phlm, 2 Joh, 3 Joh, Jud). Gewählt wird, was den Zweck des Buchs trägt
  (`zweck_de` zuerst festhalten), in der Reihenfolge des Buchs, über das ganze Buch verteilt; Heil und Gericht vollständig, offene
  Enden offen ([docs/VERDICHTUNG.md](../../../../docs/VERDICHTUNG.md), Buchebene; [docs/STRUKTURKATALOG.md](../../../../docs/STRUKTURKATALOG.md) Abschnitt 4 Bücherübersicht und 5 Fallstricke).
- Stellen in Navigationszählung (KJV): `GEN.1.1-GEN.2.3`. Jede Station hat mindestens einen B-Beleg mit Stelle innerhalb der Station.
- Für Bücher mit vorhandenem Bildauftrag (`data/illustrations/briefs/BRIEF-<BUCH>.json`: RUT, OBA, MAT, MRK, LUK, JHN, PHP, 1JN, 2JN, 3JN)
  gilt dessen Zahl, Reihenfolge und `reference` der Felder genau; `action_de` von dort übernehmen; kein `band` (das Band kommt aus dem
  Bildauftrag). Du wählst dort nur die Form und schreibst Malauftrag oder Struktur.

## Form je Station

- **szene** (gemalt): nur wenn der Text an dieser Stelle selbst etwas erzählt oder als Geschehen schildert (Erzählung, Berufung,
  Zeichenhandlung, Vision als Ereignis, Gleichnis als Bild im Bild, Brief mit Szene wie «Titus in Kreta»).
- **struktur** (gezeichnet aus Daten): bei Gesetz, Listen, Stammbäumen, Liedern, Weisheit, Prophetenrede, Argumenten, Reihen.
  Typen: `spalten` (zwei Seiten, z. B. nicht … sondern, einst – jetzt, Gerechte – Gottlose; `gestrichen: true` für verneinte Glieder),
  `kette` (Folge mit Pfeilen: Ursache → Wirkung, Argument), `raster` (Reihe gleichartiger Glieder: Gebote, Plagen, Tugenden),
  `kurve` (Abstieg und Aufstieg, Klage → Lob, je Element `richtung` ab/auf, Wende als `mitte`), `spiegel` (Umkehrung hoch ↔ tief,
  zwei Seiten mit Anfang und Ende: Seite a fällt von hoch nach tief, Seite b steigt von tief nach hoch), `reihe` (nummerierte Stationen, Ablauf), `ebenen` (oben/unten: Himmel ↔ Erde, Bild ↔ Sache),
  `ringe` (Rahmen und Mitte, Chiasmus nur mit Textbeleg; `mitte` Pflicht).
- `form_grund_de`: ein Satz, warum.
- Ziel über die ganze Bibel: gemalt, wo erzählt wird; nicht jede Station eines Briefs oder Propheten künstlich als Szene.

## Malauftrag (form szene)

Vorbilder: `buch/TIT.json`, `szenen-jon.json`, `szenen-luk-015.json`; Regeln in [docs/BILDSTIL.md](../../../../docs/BILDSTIL.md) («Szenenpläne schreiben»).
- `bild_en` (Englisch, 400–900 Zeichen): Zeit und Ort nennen (z. B. «Ancient Egypt, Late Bronze Age» / «Judah, 7th century BC»),
  wer steht LEFT/RIGHT/CENTRE, was jede Person tut, Gefühle über Körper und Geste, eindeutige Körpersprache für Handlungen, die geprüft
  werden (sprechen, streiten, beten), wenige Personen, schlichter Hintergrund, «Medium-wide shot, the upper third empty paper.»
- **Gott wird nie gemalt** (kein FIG-GOTT, keine Hand oder Gesicht am Himmel, kein Licht- oder Strahleneffekt). Engel nur, wo der Text
  sie nennt, als Menschen in Weiss ohne Flügel, wenn der Text keine nennt. Keine Gewaltdetails, kein Blut; Kreuzigung schlicht.
- Menschen des antiken Vorderen Orients, keine Karikatur, keine Merkmale einer Volksgruppe als Abwertung.
- Keine Sprechblasen (speech bleibt leer).
- `depicts`: Kennungen aus `data/illustrations/lexicon/` (`ls data/illustrations/lexicon`). Fehlt eine Person oder ein wichtiger
  Gegenstand, unter `neue_figuren` beschreiben (Kennung FIG-NAME in Grossbuchstaben, z. B. FIG-NOAH). Jede gezeigte Kennung braucht
  eine Malbeschreibung in `figuren` (Englisch: Alter, Haar, Bart, Kleidungsfarben, Zeichen), ausser sie steht schon in
  `scripts/authoring/bilder_aquarell_daten/figuren.json` (dann nicht überschreiben, ausser die Darstellung passt nicht, z. B. Jesus am Kreuz).
  Wiederkehrende Personen über Bücher hinweg gleich beschreiben (Mose, David, Elija, Paulus, Petrus …). Terrakottarot trägt nur Jesus.
- `kenn_en`: kurze Erkennungsbeschreibung für Hauptpersonen (sichtbar in jeder Haltung, nicht Füsse).
- `pruefung`: 2–4 Regeln; mindestens eine `pflicht`. Fragen auf Englisch, mit Ja/Nein beantwortbar, nach Sichtbarem; `art` «muss»
  (Ja verlangt) oder «nicht» (Nein verlangt). Regel und Malauftrag dürfen sich nicht widersprechen. Typisch: Kernhandlung sichtbar
  (pflicht), Hauptfigur erkennbar (pflicht), Verbotenes nicht da (pflicht, z. B. kein Blut, keine Figur am Himmel), Nebenzüge (soll).
- `evidence`: B (steht im Text, mit Stelle), R (plausible Ausgestaltung), I (Deutung/Bildgestaltung).

## Struktur (form struktur)

- Beschriftungen in eigenen kurzen Worten (höchstens 40 Zeichen), Hochdeutsch `de` und Züridüütsch `gsw`; je Element möglichst eine
  Stelle `ref`. Keine wörtlichen Zitate erfinden. Zahl der Glieder nicht glätten; wo der Text mehr Glieder hat als Platz ist, die
  tragenden wählen und im `note_de` oder `form_grund_de` sagen.
- `titel` optional (höchstens 40 Zeichen). `kopf.a`/`kopf.b` bei spalten, spiegel, ebenen.

## Band, Texte, Sprache

- `band.de`/`band.gsw`: Titel der Station in eigenen Worten, höchstens 46 Zeichen, ohne Anführungszeichen (es gibt für die meisten
  Bücher noch keine Arbeitsübersetzung; darum keine Zitate).
- Schweizer Schreibung (ss, kein ß). Züridüütsch wie in den vorhandenen Dateien (z. B. «isch», «händ», «Gnad», «Wärch», «Chind», «Gsetz»).
- `note_de`: Hinweis für die Legende: was gezeigt, was weggelassen, was gedeutet ist; Bibelstellen als `[[GEN.1.1]]`.
- Deutungen und Forschungsvorschläge (Chiasmen, Datierungen, Verfasser) als solche kennzeichnen, nie als Text ausgeben.
