# Vision

Festgehalten am 2026-10-09. Abschnitt **«Vorgabe»** gibt die Vision des Projektinhabers wieder. Abschnitte **«Ableitung»** sind Vorschläge zur Umsetzung; sie sind noch nicht vereinbart.

## Grundhaltung

**Vorgabe:** Das Ganze ist so frei wie nur möglich (siehe [LIZENZEN.md](../LIZENZEN.md)). Viele Übersetzungen sind mit Lizenzen belastet; das Projekt schafft eine freie Grundlage. Betrieben wird die App von einem gemeinnützigen Verein; Ziel ist kein Geld, sondern neues Wissen, ansprechend und zugänglich verbreitet. Dafür dürfen mehrere Quellen genutzt werden.

**Ableitung (vereinbart 2026-10-09):** Eigene Inhalte unter CC0. Freier Kern mit gemeinfreien, CC0-, CC-BY- und CC-BY-SA-Quellen; nicht kommerzielle Quellen (z. B. BHSA, CATSS-Septuaginta, Qumran-Daten) in einer getrennten Studienschicht. Langfristig Lücken im Kern durch eigene freie Daten schliessen.

---

## Stufe 1 — Eine solide, transparente Textbasis

**Vorgabe:** Um irgendetwas mit der Bibel zu tun, braucht es eine solide Basis. Diese Basis ist **nicht ein von Personen entschiedenes Richtig/Falsch oder Drinnen/Draussen** (Lektorat), sondern: die unterschiedlichen Quellen werden betrachtet und **nach Gesichertheit bewertet**; **Unterschiede werden ausgegeben**.

**Was schon da ist:** Ganzes Markusevangelium mit 929 Variantenstellen auf Editionsebene, an Wörter gebunden; erste Gesichertheitsbewertung «Übereinstimmung der Editionen» mit offengelegten Grenzen ([GESICHERTHEIT.md](GESICHERTHEIT.md)); erste Handschriftenangaben für Mk 3,29; Trennung von Handschrift, Edition und Übersetzung.

**Ableitung:**
- Keine «Haupttext gegen Fussnote»-Logik. Jede Variantenstelle zeigt alle Lesarten mit ihrer Bezeugung.
- **Gesichertheit als eigene, nachvollziehbare Bewertung**, nicht als Entscheidung: Mehrere Bewertungen pro Stelle können nebeneinander bestehen, jede mit Methode, Eingangsdaten, Ergebnis und Datum. Beispiele für Methoden:
  - Übereinstimmung der Editionen (automatisch berechenbar; Beispiel Mk 3,25: δυνήσεται bei WH, Tregelles, NA28 gegen δύναται bei RP).
  - Alter, geografische Verbreitung und Texttyp der Handschriften (aus offenen Transkriptionen).
  - Ergebnisse der kohärenzbasierten Methode (CBGM) der ECM, soweit zitierbar.
  - Begründete Einschätzungen von Fachleuten, namentlich und datiert.
- Ehrlich bleiben: Auch jede Bewertungsmethode enthält Annahmen (Editionen sind z. B. keine unabhängigen Zeugen). Diese Annahmen werden pro Methode dokumentiert und angezeigt.
- Der bestehende Typ `editorial_decision` wird schrittweise zu einer solchen Bewertung (`assessment`) weiterentwickelt; bestehende Entscheidungen bleiben als historische Bewertung erhalten.
- Die Lesbarkeit entsteht durch Darstellung (z. B. die am besten bezeugte Lesart hervorgehoben, Abweichungen mit Gesichertheitsangabe sichtbar), nicht durch Weglassen.

---

## Stufe 2 — Übertragung in heutige Zeit, Kultur und Sprachen

**Vorgabe:** Die Schriften aus ihrer Zeit, Kultur und Sprache in die heutige Zeit, Kultur und Sprachen übersetzen.

**Was schon da ist:** Kontextdimensionen (Zeit, Ort, Kultur, Sprache, Zielgruppe); eine wörtliche deutsche Arbeitsübersetzung von Mk 3,22–30 mit vollständiger Wortzuordnung.

**Ableitung:**
- **Übersetzung in Schichten**, jede mit der Ausgangsbasis verbunden:
  1. Wort-für-Wort (Interlinear, mit Grammatik),
  2. wörtlich orientiert (Satzbau nachvollziehbar),
  3. kommunikativ (heutige, natürliche Sprache),
  4. kulturell erläutert (Begriffe, Bilder und Gepflogenheiten der damaligen Welt für heutige Lesende erklärt, ohne sie im Text zu ersetzen).
- Jede Schicht bleibt über Wortzuordnungen bis zum Ausgangswort rückverfolgbar; Unterschiede an Variantenstellen werden mitgeführt.
- Mehrere Zielsprachen und -kulturen (zuerst Deutsch, Schweizer Schreibweise), jeweils als eigener Kontext.
- KI-unterstützte Entwürfe sind erlaubt und als solche gekennzeichnet; Prüfungen durch Menschen werden dokumentiert, nicht behauptet.
- Alle Übersetzungen des Projekts unter CC0 — eine freie Alternative zu lizenzierten Bibelübersetzungen.

---

## Stufe 3 — Verständnis über Zoomstufen und Anleitung zum Bibelstudium

**Vorgabe:** Von den kleinsten Einheiten bis zum grossen Ganzen mit unterschiedlichen Zoomstufen ein besseres Verständnis schaffen und Anleitung zum Bibelstudium geben.

**Was schon da ist:** Zoom-Konzept (Wort → Satz → Vers → Texteinheit → Abschnitt → Buch → mehrere Bücher → gesamtbiblischer Bogen → damalige/heutige Welt); Analyseebenen Befund → Deutung → Prinzip → Anwendung.

**Ableitung:**
- Für jede Zoomstufe eigene Datenobjekte: Gliederungen (natürliche Texteinheiten, Abschnitte, Bücher), Themen- und Motivlinien, Querbezüge, Zeitleisten, Orte.
- Beispiel Pilot: Wort (βλασφημέω) → Vers (Mk 3,29) → Einheit (3,22–30) → Abschnitt (3,20–35, die Beelzebul-Szene eingebettet in die Szene mit Jesu Familie) → Markusevangelium → Thema «Heiliger Geist» quer durch die Bibel.
- **Anleitung zum Bibelstudium** als eigener Inhaltstyp: geführte Schritte (beobachten, Text und Varianten prüfen, Kontext klären, Deutungen vergleichen, übertragen), die auf die vorhandenen Daten zeigen. Grundlage ist der Arbeitsprozess in [PROZESS.md](PROZESS.md), in einfacher Sprache für Lesende.
- Auf jeder Zoomstufe bleiben Gesichertheit und alternative Deutungen sichtbar.

---

## Stufe 4 — Visuelle Komponenten und UX

**Vorgabe:**
- Visuelle Hilfen sollen das Studium vertiefen; die UX der App ist wichtig.
- Textliche Beschreibungen von Objekten im Raum sollen visualisiert werden.
- Auf jeder Zoomstufe soll die Bedeutung mit Grafiken untermalt werden.
- Unterschiedliche Personen, Institutionen und Künstler können ihre Grafiken und Bilder hinzufügen.

**Vorgabe (2026-10-09, nach dem ersten Prototyp):** Die App soll einfacher und allgemeiner sein, super anwenderfreundlich in Bedienung und Inhalt. Wenn Quelltexte zu unterschiedlichen Übersetzungen führen können, sollen weniger wahrscheinliche Lesarten bei Bedarf einblendbar sein. Urtexte nicht direkt so prominent, sondern in einem Modus für Fortgeschrittene. Design: schlicht, dunkel/hell, etwas künstlerisch angehaucht, aufgeräumt, guter Umgang mit Platz.

**Ableitung:**
- **Standard ist das Lesen:** deutscher Text, ruhige Typografie, drei Wege (Überblick, Lesen, Vertiefen). Fachbegriffe vermeiden («Was steht da?», «Wie kann man es verstehen?», «Was kann es heute bedeuten?»).
- **Abweichende Lesarten** nur dort, wo sie die Übersetzung verändern, auf Wunsch eingeblendet und in einfacher Sprache erklärt («Steht in 4 von 5 wichtigen Textausgaben»).
- **Modus für Fortgeschrittene:** griechischer Text, Wort für Wort, Grammatik, alle Unterschiede der Textausgaben.
- **Arten von Visualisierungen:**
  - Struktur- und Argumentationsdiagramme (z. B. Aufbau von Mk 3,22–30, Verschachtelung in 3,20–35),
  - Karten und Zeitleisten,
  - Beziehungsnetze (Personen, Parallelstellen, Themen),
  - Sprachbilder (z. B. «gespaltenes Haus», «der Starke»),
  - **Raumrekonstruktionen** aus Textbeschreibungen: Arche (Gen 6), Stiftshütte (Ex 25–40), Salomos Tempel (1 Kön 6–7), Tempelvision (Ez 40–48), Neues Jerusalem (Offb 21).
- **Raumobjekte als Daten:** Masse, Materialien und Anordnungen werden aus dem Text als strukturierte Angaben mit Wortbezug erfasst, inklusive Unsicherheiten (z. B. Länge der Elle, unklare Begriffe, Varianten). Darstellungen werden daraus erzeugt; abweichende Rekonstruktionen stehen nebeneinander, jede Annahme ist sichtbar.
- **Beiträge Dritter:** eigenes Objekt für Bilder/Grafiken mit Urheber, Lizenz (CC0 oder CC BY), Bezug (Stelle, Wort, Objekt, Zoomstufe), Art (Rekonstruktion nach Textangaben, Diagramm, künstlerische Deutung) und Prüfstatus. Beiträge ergänzen die Basis, verändern sie aber nicht. Künstlerische Deutungen werden als solche gekennzeichnet.
- **UX-Grundsätze:** schrittweise Vertiefung (zuerst lesbar, auf Wunsch bis zur Handschrift); Unterschiede und Gesichertheit immer erreichbar, aber nicht erschlagend; Zoomen als zentrale Bewegung; für Smartphone tauglich.

---

## Reihenfolge (Ableitung)

1. Stufe 1 auf ganze Bücher ausbauen (Markus vollständig), Gesichertheitsbewertung als Datentyp einführen.
2. Stufe 2 mit zwei Übersetzungsschichten für Mk 3,20–35 erproben.
3. Stufe 3: Gliederungs- und Themenobjekte für Markus; erste Studienanleitung.
4. Stufe 4: erster vertikaler Prototyp der App (Mk 3,20–35 durch alle Zoomstufen, mit Strukturdiagramm); ein Raumobjekt (Stiftshütte) als Machbarkeitsprobe, sobald der hebräische Text importiert ist.

Jeder Schritt bleibt ein vertikaler Durchstich an einem kleinen Textausschnitt, bevor er in die Breite geht.
