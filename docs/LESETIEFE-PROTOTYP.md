# Lesestrom · Stand 2026-10-13 (v0.27)

Der Lesestrom ist seit v0.13 die **Hauptrichtung der App**. Einstieg: [app/reading-stream/index.html](../app/reading-stream/index.html). Die Datei direkt im Browser öffnen; Server und Internetzugriff sind nicht nötig. Das Design stammt aus dem Gespräch zwischen Andi Neck und einem Kollegen (v0.11). Der frühere Studienprototyp `app/prototype/` ist abgelöst (siehe unten).

## Vorgabe vom 2026-10-12

«Das Bibelstudium muss noch zugänglicher werden, für Personen, die kein Griechisch oder Hebräisch können. Der Lesestrom muss ungestörter stattfinden können, abtauchen in die Tiefe, und Hintergrundoptionen optionaler.» (Andi Neck)

Umsetzung in v0.13:
- **Ungestört lesen:** Vollbild ohne Geräterahmen. Kopf- und Fussleiste blenden beim Weiterlesen aus und erscheinen beim Zurückscrollen oder durch Tippen auf den Text wieder. Keine technischen Zähler im Lesetext. Verse fliessen als Text, Kapitel- und Abschnittstitel sind leise Zwischenüberschriften.
- **Abtauchen:** Auf jeder Ebene führt ein einziger Link eine Stufe tiefer, mit Text je nach Ebene: «Zu den Testamenten» … «Text lesen». Am Ende jedes ausgearbeiteten Abschnitts steht «Diesen Abschnitt verstehen».
- **Hintergrund nur auf Wunsch:** Lesarten, Erklärungen und Quellen öffnen sich als Blatt über dem Text und schliessen wieder, ohne die Leseposition zu verlieren. Ein unauffälliges «+» erscheint nur an Versen, an denen sich die alten Handschriften unterscheiden.
- **Ohne Griechisch und Hebräisch:** Standardmässig gibt es keinen Urtext. Griechische Einschübe in Erklärungen werden ausgeblendet bzw. als «der griechische Ausdruck» umschrieben. Lesarten erscheinen als deutsche Wiedergaben mit einfacher Angabe der Bezeugung («Steht in 4 von 5 wichtigen Textausgaben»). Es gibt keine Entscheidung über richtig oder falsch.
- **Für Fortgeschrittene:** Im Menü der Schalter «Urtext und Details»: Griechisch Wort für Wort mit Grundform, Form und Satzrolle; Vergleich der Textausgaben; Quellen und IDs. Ein zweiter Schalter «Andere Lesarten im Text zeigen» zeigt die Alternativen direkt unter dem Vers.
- Deutsche Stellenangaben (Markus 3,20), Farben folgen dem System (oder fest hell/dunkel), Einstellungen werden lokal im Browser gespeichert.

## Lesetext in mehreren Sprachen (v0.27)

Menü «Lesetext»: Hochdeutsch oder Züridüütsch. Beide sind aus dem Griechischen übersetzt; Lesarten, Entscheidungen und Wortzuordnung gehören zur jeweiligen Schicht. Die Mundart folgt der Dieth-Schreibung und ist ein ungeprüfter Entwurf.

## Gestaltungsregeln (v0.24)

- Eine Rundung für alle Bedienelemente und Kästen (`--r`, 6 px). Keine Pillen, keine Kreise; Ausnahme ist der Ein/Aus-Schalter.
- Flächen: Auswahl und aktuelle Position als gefüllte Fläche in Tintenfarbe; alles andere mit feiner Linie (`--rule`); Hover als weiche Fläche (`--soft`).
- Einstellungszeilen: Beschriftung links, Auswahl rechts; bei Umbruch rechtsbündig.
- Schrift: Bedienung in der UI-Schrift, Lesetext und Griechisch in der Serifenschrift.

## Navigator und Querverweise (v0.23)

Die Titelzeile öffnet den Navigator: Pfad der aktuellen Position, Suche, dann Testament → Buchgruppe → Buch → Kapitel → Vers als Raster mit Punkt für ausgearbeitete Teile. Im Versblatt stehen Querverweise (OpenBible.info, CC BY, nach Stimmen); Bibelstellen in Erklärtexten sind antippbar; nach einem Sprung führt «Zurück zu …» an die Ausgangsstelle. Verse fortlaufend ist Standard.

## Lesefluss und Wort-Info (v0.20)

Verse mit Details erkennt man an der umrandeten Versnummer; sie öffnet das Versblatt. Unterstrichene Wörter öffnen ein Wort-Blatt (Griechisch, Deutungen, Übersetzungsentscheidung, ältere Übersetzungen). «Verstehen» und «Geschichte» stehen als Symbole beim Abschnittstitel.

## Ursprungswörter (v0.19)

Erklärungen, die sich auf ein Wort der Ursprache beziehen, zeigen es klein mit Umschrift und Anhören-Knopf (Feld `terms`); griechische Einschübe im Text ebenso.

## Übersetzungsentscheidungen (v0.18)

Im Versblatt zeigt «Wie ist übersetzt?», wo die Arbeitsübersetzung wörtlich ist, sprachlich glättet, deutet oder einer vertrauten Wiedergabe folgt, jeweils mit wörtlicherer Fassung und Begründung. «Ältere deutsche Übersetzungen» stellt Luther 1912 und Elberfelder 1905 daneben. Im Urtext-Modus sind Tradition (gepunktet) und Deutung (gestrichelt) im Lesetext unterstrichen. Bisher für das Vaterunser.

## Umschrift und Anhören (v0.17)

Griechisch erscheint zusätzlich in lateinischer Umschrift (z. B. ponēroú) und lässt sich mit dem Lautsprecher-Knopf anhören. Menü: Umschrift an/aus, Aussprache (Neugriechisch mit der Stimme des Geräts oder Schulaussprache über eine deutsche Stimme), Stimme, Tempo, Probe. Die Stimmen kommen vom Gerät; fehlt eine griechische Stimme, lässt sie sich in den Systemeinstellungen nachladen. Voreinstellung seit v0.17: Lesarten, Hintergrund und Urtext im Text eingeschaltet; Umschalten hält die Leseposition.

## Vaterunser (v0.16)

Ausgearbeitet sind jetzt drei Stellen: Mk 3,20–35, Mt 6,5–15 (Vom Beten, mit dem Vaterunser) und Lk 11,1–4. Das Menü listet sie unter «Ausgearbeitete Stellen»; auf Buch- und Kapitelebene führt ein Knopf direkt dorthin. Beim Vaterunser zeigt «Bis zur Quelle» neben den grossen Handschriften auch 𝔓75 (Lukas) und Amulette des 3. bis 6. Jahrhunderts, die das Gebet überliefern. Neue Stellen werden in `scripts/build_reading_stream.py` (Liste `SECTIONS`) eingetragen.

## Lesarten bis zur Quelle (v0.15)

Rückmeldung vom 2026-10-12: Bei den anderen Lesarten weiter eintauchen können, die Unterschiede bis zur Quelle verstehen, auch übersetzt, so dass klar wird, welche Urtexte was sagen. Umsetzung: Im Versblatt hat jede Lesart den Link «Bis zur Quelle». Er öffnet ein Blatt mit:
- **Was ist anders?** Beide deutschen Wiedergaben.
- **Die Wörter im Griechischen**, wörtlich übersetzt und kurz erklärt (z. B. ἁμαρτήματος «einer Verfehlung», κρίσεως «eines Gerichts», ἁμαρτίας «einer Sünde»).
- **Was die alten Handschriften lesen:** Codex Sinaiticus, Vaticanus, Alexandrinus, Ephraemi, Bezae und Washingtonianus (4./5. Jh.), gruppiert nach Lesart. Aufklappbar: Wortlaut der Handschrift, Erstschrift und Korrektur getrennt, Hinweise auf beschädigte oder ergänzte Stellen, kurze Beschreibung, Aufbewahrungsort, Links zu Abbildungen und Katalog. Weicht eine frühere Arbeitsnotiz von der Transkription ab, steht das dabei.
- **Was die gedruckten Ausgaben haben:** SBLGNT, Westcott-Hort, Tregelles, NA28, Robinson-Pierpont sowie Textus Receptus (Stephanus), der griechische Text hinter der King-James-Bibel und die Statistical Restoration, jeweils mit kurzer Erklärung. Widersprechen sich die Quellen (3,20 RP), wird das angezeigt.
- **Wie kann der Unterschied entstanden sein?** Mehrere mögliche Erklärungen nebeneinander (z. B. Augensprung bei 3,32), ohne Entscheidung.
- **Wie sicher ist das?** Zählung der Ausgaben und der alten Handschriften, mit Grenzen.

Daten: `data/witnesses/`, `data/witness-texts/` (CNTR, CC BY-SA 4.0), `data/witness-readings/`, Wortbedeutungen und Erklärungen in den Übersetzungs-Alternativen (`readings_de`, `origin_de`). Werkzeuge: `scripts/import_cntr_transcriptions.py`, `scripts/collate_witnesses.py`. Noch nicht enthalten: spätere Handschriften, alte Übersetzungen (lateinisch, syrisch, koptisch), Kirchenväter, Bilder der Handschriftenstellen.

## Hintergrund damals (v0.14)

Rückmeldung vom 2026-10-12: Auf Versebene passt der Lesestrom; es fehlt der Hintergrund damals. Seit v0.14 gibt es 13 Hintergrundnotizen zu Markus 3,20–35 (`data/background/`), alle als ungeprüfte KI-Entwürfe:
- **Im Versblatt** («+»): unter «Damals» die Notizen zu diesem Vers, z. B. zu Schriftgelehrten aus Jerusalem, Beelzebul, Geisteraustreibung, dem Bild vom Binden des Starken, «Amen», Lästerung, den Brüdern Jesu, dem Sitzen um einen Lehrer, Familie und Ehre. Das «+» erscheint jetzt auch an Versen, zu denen es Hintergrund gibt.
- **Pro Abschnitt:** «Hintergrund damals» am Abschnittsende, auf der Abschnittsebene und im Verstehen-Blatt. Dort stehen auch Zeit und Ort sowie die erste Leserschaft des Markus.
- **Optional im Text:** Der Menüschalter «Hintergrund im Text zeigen» setzt kurze Hinweise («Damals: Beelzebul») unter den Vers, an dem eine Notiz beginnt.
- Jede Notiz zeigt, wie sicher sie ist, was umstritten ist und womit man vergleichen kann (Bibelstellen sowie Fundstellen wie Josephus oder die Mischna, nur zitiert). Hintergrund ist bewusst von Befunden, Deutungen und heutiger Anwendung getrennt.

## Bedienidee (seit v0.11)

Jede Zoomstufe ist eine fortlaufende Lesefassung: Bibel → Testament → Buchgruppe → Buch → Kapitel → Abschnitt → Vers. Scrollen führt zum nächsten Eintrag derselben Ebene, «Vertiefen» öffnet die darunterliegende Fassung am aktuellen Eintrag, «Kontext» führt zur übergeordneten zurück. Lesepositionen bleiben pro Ebene erhalten. Inhaltsverzeichnis (Tippen auf den Ort oben), Ebenenwahl (Mitte unten) und Stellensuche (Menü) sind zusätzliche Sprungmöglichkeiten. Die Gestaltung ist ruhig und typografisch, inspiriert vom Auftritt der Fondation Beyeler; es wurden keine Markenassets übernommen. Logo: geometrisches B, gedreht, mit zwei Quadraten; reine SVG-Pfade.

## Daten

Seit v0.13 liegen die Inhalte im freien Kern, nicht mehr in der Vorlage:
- `data/navigation/NAV-PROT66-KJV.json`: Testamente, zehn Buchgruppen, 66 Bücher mit Namen, Kürzeln und Versen pro Kapitel. Protestantischer Kanon und KJV-Zählung sind eine **deklarierte Testkonfiguration**, keine Festlegung. Herkunft der Zahlen: [provenance.json](../app/reading-stream/provenance.json).
- `data/summaries/`: 83 Zusammenfassungen (Bibel, Testamente, Gruppen, 66 Bücher, vier Beispielkapitel), alle `draft`. Es sind KI-Entwürfe aus dem Designgespräch vom 2026-10-11 (`authorship_de`, `migrated_from`), fachlich ungeprüft.
- Markus 3,20–35: Studienprojektion aus `scripts/build_prototype.py` (Arbeitsübersetzung, sechs Alternativen, 249 Wörter, 28 Variantenstellen, Befunde, Deutungen mit Gegenargumenten, Prinzip, Anwendung, offene Frage).

Build: `template.html` bearbeiten, danach `python3 scripts/build_reading_stream.py`. Das Skript bettet die drei Datenquellen in `index.html` ein. Die erzeugte Datei nicht von Hand ändern.

## Grenzen

- Abschnitte ausserhalb von Markus 3 sind technische Blöcke von bis zu fünf Versen, **keine natürlichen Texteinheiten**. Eine Gliederung nach Gedankengängen fehlt noch.
- Ausserhalb von Markus 3,20–35 fehlt der Bibeltext; die App zeigt dort ruhig «Text noch nicht eingebunden». Die meisten Kapitelzusammenfassungen fehlen ebenfalls.
- Die Umschreibung griechischer Einschübe ist eine reine Darstellung. Sie ist grammatisch nicht immer glatt und ändert die Daten nicht.
- Englisch übersetzt nur die Bedienelemente, nicht die Inhalte.
- Geladene Einträge werden nicht virtualisiert. Volltextsuche fehlt (nur Buch und Stelle).
- Die Versifikation ist noch nicht mit einem Versifikationsmodell (z. B. STEPBible TVTMS) abgeglichen.

## Abgelöst: `app/prototype/`

Der Studienprototyp Mk 3,20–35 (v0.9/v0.10) wird nicht weiterentwickelt. Er bleibt als Zwischenstand erhalten. `scripts/build_prototype.py` bleibt in Gebrauch, weil es die Datenprojektion für den Lesestrom liefert, und erzeugt die alte Seite weiterhin mit.

## Prüfungen

- `node scripts/test_reading_stream.cjs` (ohne Zusatzpakete): vollständige Ebenen, Zählungen, Zusammenfassungen, Elternverweise, kanonische Stellen, Suche, Grenzen, Markus-Projektion.
- `node scripts/test_reading_stream_dom.cjs` (braucht `jsdom`): Piloteinstieg, Studienblatt ohne Griechisch, Lesarten und Hintergrund im Versblatt, Hintergrund-Blatt je Abschnitt, Hinweise im Text, «Bis zur Quelle» für alle sechs Alternativen, Urtext-Modus, Rückkehrposition, Suche, Lesen über die Kapitelgrenze, Lesarten im Text.
- Am 2026-10-12 wurde der Lesestrom in Chromium in Handybreite (390 px) hell und dunkel angesehen. Eine Prüfung auf echten Geräten und mit Bildschirmleser steht aus. Keine dieser Prüfungen ist eine fachliche Inhaltsprüfung.
