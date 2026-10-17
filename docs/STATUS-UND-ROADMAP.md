# Status und nächste Schritte · 2026-10-14 (UI v0.60)

## Gesichert und vorhanden
- **Lesestrom als Hauptrichtung** (`app/reading-stream/`, v0.13): die ganze Bibel auf sieben Ebenen fortlaufend lesen und vertiefen; ungestörtes Vollbild mit ausblendenden Leisten; Lesarten, Erklärungen und Quellen als Blätter auf Wunsch; Urtext nur im Modus «Urtext und Details»; deutsche Stellenangaben; Farben nach System. Navigationsgerüst und 83 Zusammenfassungen liegen jetzt in `data/navigation/` und `data/summaries/` (Entwürfe, ungeprüft). Ausgearbeitet ist Markus 3,20–35; sonst fehlt der Bibeltext. Details und Grenzen: [LESETIEFE-PROTOTYP.md](LESETIEFE-PROTOTYP.md).
- **Hintergrund damals** (v0.14): 13 Notizen zu Mk 3,20–35 in `data/background/`, im Lesestrom pro Vers, pro Abschnitt und optional im Text. Ungeprüfte Entwürfe; die zitierten ausserbiblischen Fundstellen sind noch nicht am Originaltext nachgeprüft.
- **Lesarten bis zur Quelle** (v0.15): Transkriptionen der sechs ältesten Handschriften für Markus (א, A, B, C, D, W; CNTR, CC BY-SA 4.0) und fünf Ausgabentexte importiert; maschinelle Zuordnung zu den 28 Variantenstellen in Mk 3,20–35 (Abgleich mit dem SBLGNT-Apparat: 50 von 52 Ausgaben-Zuordnungen stimmen; 3,20 RP ist ein echter Unterschied zwischen SBLGNT-Apparat und CNTR-Text). Im Lesestrom pro Lesart ein Blatt «Bis zur Quelle» mit Wortbedeutungen, Handschriften, Ausgaben, Entstehungserklärungen und Sicherheit.
- **Vaterunser** (v0.16): Mt 6,5–15 und Lk 11,1–4 ausgearbeitet wie Mk 3,20–35 (Übersetzung, Lesarten bis zu Handschriften, Papyri und Amuletten, Wortzuordnung, Befunde, Deutungen, Hintergrund, Anwendung). Matthäus und Lukas vollständig als griechischer Text mit Annotation und Apparat vorhanden. Alles fachlich ungeprüft.
- **Züridüütsch** (v0.27): zweite Übersetzungsschicht aus dem Urtext für alle ausgearbeiteten Stellen, im Lesestrom umschaltbar; Mundart noch nicht muttersprachlich geprüft. Wortzuordnung für Mk 3 in Mundart noch offen.
- **Lokalisierungen** (v0.29): alle erklärenden Inhalte der ausgearbeiteten Abschnitte und alle Zusammenfassungen in Züridüütsch als eigene `localization`-Datensätze mit Quellen-Fingerabdruck; veraltete Übersetzungen werden gemeldet und nicht ausgeliefert. Offen: Bedienung, Buch- und Gruppennamen übersetzen.
- **Johannesevangelium ganz** (v0.44): Übersetzung, Wortzuordnung, Handschriften inkl. 𝔓66/𝔓75/𝔓52, Studieninhalte; ungeprüfter KI-Entwurf mit KI-Gegenlesung, Literaturangaben der Studien noch nicht nachgeschlagen, Mundart nicht muttersprachlich geprüft.
- **Jona, 1–3 Johannes, Markus ganz** (v0.40) und **Wörterbuch, Ausgaben je Wort, Ketiv/Qere** (v0.39): ungeprüfte KI-Entwürfe mit KI-Gegenlesung; Mundart nicht muttersprachlich geprüft.
- **Texte vom Toten Meer** (v0.38, nicht kommerzielle Schicht): Rut und Obadja mit maschinellem Vergleich zum WLC. Offen: weitere Bücher bei Bedarf; Septuaginta nach CATSS-Erklärung; NTVMR nach Antwort des INTF.
- **Rut und Philipper** (v0.35): ganz aus dem Urtext übersetzt (Hochdeutsch, Züridüütsch, Wortzuordnung, Entscheidungen, Studieninhalte); Philipper mit 𝔓46. Ungeprüfte KI-Entwürfe (nur KI-Gegenlesung). Offen wie bei Obadja: freie textkritische Daten zum Alten Testament. Umrechnung der Verszählung seit v0.36 umgesetzt, alle AT-Bücher importierbar.
- **Titus und Obadja als Muster für ganze Bücher** (v0.33): Titus vollständig aus dem Griechischen (Text, Varianten, Handschriften inkl. 𝔓32, Übersetzung Hochdeutsch und Züridüütsch mit Wortzuordnung, Entscheidungen, Studieninhalte, Hintergrund auf Buchebene); Obadja als erster hebräischer Text (WLC/MACULA Hebrew, Übersetzungen mit Wortzuordnung auf Morphem-Ebene, Studieninhalte). Ungeprüfte KI-Entwürfe (nur KI-Gegenlesung). Offen: freie textkritische Daten für Obadja (Qumran, LXX, Apparat), Handschriften-Abgleich am Faksimile, muttersprachliche Prüfung der Mundart, Gottesname in Mundart abschliessend festlegen.
- **Hintergrund der oberen Ebenen** (v0.32): Bibel, Testamente und alle zehn Buchgruppen, Hochdeutsch und Züridüütsch. Hintergrund je Buch für alle 66 Bücher (v0.34). Offen: fachliche Prüfung, Prüfung der zitierten Quellen am Originaltext.
- **Skalierung** (v0.31): Lesestrom in Kern und nachladbare Pakete je Buch und Sprache; Stellen im Fliesstext als sprachneutrale Marken; neutrale Feldnamen; Versifikationsdaten (TVTMS). Umrechnung hebräisch → KJV umgesetzt (v0.36). Offen: Umrechnung für Septuaginta und Vulgata, Buchnamen je Sprache, SQLite-Projektion für Suche über alle Daten.
- **Navigator und Querverweise** (v0.23): hierarchische Navigation, 344 799 Querverweise (OpenBible.info), verlinkte Stellen mit Rücksprung. Offen: Lesetext für Sprungziele ausserhalb der ausgearbeiteten Stellen. **Entscheid 2026-10-13 (Andi Neck):** Der Lesetext geht immer vom Urtext aus (eigene Übersetzungsschichten aus Griechisch bzw. Hebräisch); Luther 1912 und Elberfelder 1905 dienen nur dem Vergleich, nicht als Ersatz-Lesetext. Wo noch keine Übersetzung aus dem Urtext vorliegt, bleibt es bei den Zusammenfassungen.
- **Übersetzungsentscheidungen** (v0.18): für die Vaterunser-Verse gekennzeichnet (wörtlich, angepasst, Deutung, Tradition) und mit Luther 1912 und Elberfelder 1905 verglichen. Für Mk 3,20–35 noch nicht nachgetragen.
- **Umschrift und Anhören** (v0.17): griechische Wörter in lateinischer Umschrift und per Gerätestimme anhörbar; Hebräisch vorbereitet.
- v0.16: 3367 Datensätze im freien Kern.
- Alle Originalpakete v0.1–v0.5; rekonstruierte Git-Historie mit je einem Snapshot.
- **Abgelöst:** Studienprototyp Mk 3,20–35 (`app/prototype/`), bleibt als Zwischenstand; seine Inhalte sind im Lesestrom aufgegangen. Stand v0.10, für allgemeine Leser: Überblick (gezeichnete Verschachtelung der drei Szenen), Lesen (deutscher Text; abweichende Lesarten auf Wunsch, in einfacher Sprache mit Bezeugung), Vertiefen (Was steht da? Wie kann man es verstehen? Was kann es heute bedeuten?), Studienpfad, Einstellungen (Lesarten, Urtext-Modus, Schriftgrösse, Hell/Dunkel). Griechisch, Wort für Wort, Grammatik und alle Apparatstellen nur im Modus «Urtext und Details». Erzeugt mit `scripts/build_prototype.py` nur aus Daten des freien Kerns.
- v0.9: 1032 Datensätze; neu Gliederung Mk 3,20–35 (Texteinheiten, Befund, Deutung mit Gegenargument) und deutsche Arbeitsübersetzung 3,20–21 und 3,31–35 (ohne Wortzuordnung).
- v0.8: 1025 Datensätze im freien Kern, darin 6 Tags; Studienschicht `data-nc/` angelegt (leer).
- **Ganzes Markusevangelium**: SBLGNT-Text (11 286 Wörter, je Kapitel ein Token-Set) mit MACULA-Greek-Annotation (Lemma, Morphologie, Syntaxrolle, Referenten, Glossen; CC BY 4.0). SBLGNT und MACULA stimmen in allen Wortgrenzen überein; eine Akzentabweichung (7,27) protokolliert.
- **929 Variantenstellen** auf Editionsebene für Markus; 1 Apparateintrag (7,21–22, versübergreifend) nicht sicher zuordenbar und daher nicht importiert (`reports/sblgntapp-MRK-nicht-zugeordnet.json`).
- **Gesichertheitsbewertung** als Datentyp mit erster Methode «Übereinstimmung der Editionen» ([GESICHERTHEIT.md](GESICHERTHEIT.md)).
- **Vollständige deutsche Arbeitsübersetzung Mk 3,22–30** mit Zuordnung aller 140 Tokens und Anmerkungen zu Grammatik und Alternativen (KI-Entwurf, von einem zweiten KI-Durchgang gegengelesen, fachlich ungeprüft).
- MorphGNT-Annotation Mk 3,22–30 (Pilot, CC BY-SA) als eigene Schicht neben MACULA erhalten; die beiden Annotationen unterscheiden sich stellenweise (z. B. αἰωνίου in 3,29: MorphGNT Genitiv Neutrum; bei MACULA nennt der Morphologiecode `A-GSF` Femininum, das Feld «gender» aber Neutrum — auch innerhalb einer Quelle widersprüchlich) — ein Beispiel für nebeneinander gezeigte Unterschiede.
- **Einheitliche Bibelstellen** nach [BIBELSTELLEN.md](BIBELSTELLEN.md), mit Werkzeug `scripts/refs.py`; alle bestehenden Daten migriert und protokolliert.
- Variantenstellen Mk 3,29: Sünde/Gericht und ist/wird sein, als vorläufige Forschungsdaten.
- Revidierbare textkritische Entscheidung; eigene deutsche Arbeitsübersetzung; teilweise Wort-/Phrasenalignments.
- Quellenhinweise, alternative Interpretationen, Prinzip, heutige Anwendung, Kontexte, Parallelstellen und offene Frage.
- Validator für Schema, IDs, Tags, Verweise, Lesarten und Bibelstellen; synthetische Importtests im echten MorphGNT-Format.

## In v0.6 behobene technische Lücken
1. Validator lädt jetzt das Schema und prüft Verweise sowie Bibelstellen (vorher nur vier Feldnamen, IDs und Tags).
2. Schema und Daten sind konsistent: Typnamen `study`/`text_unit`, alle Typen und Statuswerte im Schema.
3. Die Pilotstudie führt alle Ergebnisse in `outputs`.
4. Der Importer erwartete ein falsches Referenzformat (`6203xx` statt `0203xx`) und hätte die echte Datei immer abgelehnt; behoben, Quelle mit Upstream-Commit wird im Datensatz festgehalten.

## Weiterhin offene technische Lücken
1. Typspezifische Schemas fehlen; der Validator prüft nur die gemeinsamen Felder.
2. Ob ein Vers existiert, wird nicht geprüft (keine Versifikationstabelle).
3. Quellen-, Review- und Zeitmetadaten sind uneinheitlich und lückenhaft.
4. Typspezifische Prüfungen für Annotationen (z. B. gültige Morphologiecodes) fehlen.
5. Kein automatischer Test für die Importer `import_sblgnt_book.py` und `import_sblgnt_apparatus.py` (sie prüfen die Quellen beim Import selbst).
6. Erledigt (v0.40): Kürzerer Markusschluss (in 16,8) und längerer Schluss 16,9–20 sind übersetzt, in ⟦ ⟧ gesetzt und als spätere Ergänzungen erklärt.
7. Der Apparateintrag 7,21–22 liesse sich mit versübergreifenden `base_tokens` eindeutig zuordnen; noch nicht umgesetzt.

## Befunde aus dem Import
- Die alte Arbeitstranskription von Mk 3,29–30 weicht nur in einem Wort von SBLGNT ab: `ἀλλ’` statt `ἀλλὰ` (3,29). Vergleich: `reports/compare-TEXT-MRK-003-029-030-WORKING-vs-SBLGNT.json`. Die Transkription bleibt als historischer Arbeitsstand erhalten.
- SBLGNT markiert in 3,29 `ἁμαρτήματος` als Variantenstelle; das stimmt mit `VAR-MRK-003-029-001` überein. Die weiteren SBLGNT-Variantenstellen in 3,25–28 sind seit v0.7 auf Editionsebene erfasst (`VAR-SBLGNTAPP-*`).
- Zeugenangabe zu prüfen: `VAR-MRK-003-029-001` führt Ephraemi (C) bei κρίσεως. **Neu (v0.15):** Die CNTR-Transkription von C liest ἁμαρτίας, als unsicher markiert (Wort «by vid» ergänzt); die Arbeitsnotiz bleibt unverändert erhalten, der Lesestrom zeigt die Abweichung an. Nach dem Gegenlesen besteht der Verdacht, dass C* ἁμαρτίας und erst ein Korrektor (C²) κρίσεως liest. Am kritischen Apparat bzw. NTVMR prüfen und ggf. Korrekturschichten trennen.
- `VAR-SBLGNTAPP-MRK-003-029-01` (nur ἁμαρτήματος) und `VAR-MRK-003-029-001` (αἰωνίου ἁμαρτήματος) betreffen dieselbe Stelle mit unterschiedlicher Abgrenzung.
- Die Art der Abweichung (Umstellung, Auslassung, Ersetzung) ist bei Apparatlesarten noch nicht klassifiziert (`unclassified`).
- Die Glossen von R1 (`ἁμαρτήματος`) und R3 (`ἁμαρτίας`) in `VAR-MRK-003-029-001` lauten beide «ewiger Sünde»; der Unterschied ist sprachlich noch zu beschreiben.

## Fachlich noch offen
- Eigene Prüfung der berichteten Lesarten an Primärmaterial und kritischem Apparat einschliesslich Korrekturschichten.
- Fachliche Prüfung der importierten Morphologie/Lemmata für die Perikope.
- Fachliche Prüfung der Arbeitsübersetzung und Wortzuordnung Mk 3,22–30.
- Präzise wissenschaftliche Fundstellen, weitere Gegenargumente und eigenständige Kontextanwendungen.
- Kritische Prüfung des abgeleiteten Prinzips: Es enthält stärkere Begriffe als die begrenzte Beobachtung zum Wissen der Schriftgelehrten. Diese Ableitung ist nicht allein durch den Pilotbestand abgesichert.

## Nächster Meilenstein (Vorschlag)
Rückmeldungen zum Lesestrom auf echten Geräten; natürliche Gliederung (Abschnitte nach Gedankengängen) statt technischer Fünf-Vers-Blöcke; Abgleich der KJV-Testzählung mit einem Versifikationsmodell (STEPBible TVTMS); freier deutscher Lesetext über Markus 3 hinaus; kommunikative (leicht verständliche) Übersetzungsschicht als Alternative zur wörtlichen; Wortzuordnung für 3,20–21 und 3,31–35; Handschriftenbelege aus der NTVMR-API (CC BY 4.0) als zweite Bewertungsmethode; Zeugenangabe Ephraemi (C) in Mk 3,29 klären; Versifikationsmodell auf Basis von STEPBible TVTMS; typspezifische Schemas.

## Danach
- **Bildsprache weiter (vorgemerkt, Andi Neck 2026-10-14):** Blindtest-Restpunkte nachbessern (Tisch, Geissel, Abstand; Offenbarung Feld 1 ohne Handlung; Weisheit-Zeichen); Bilder für alle Bücher, dann Kapitel und Abschnitte; Stil «Symbol» nach [BILDSPRACHE.md](BILDSPRACHE.md) auf weitere Kapitel ausdehnen; weitere Stile (Skizze, Anime, Kirchenmalerei) – Anime und Malerei brauchen einen Bildgenerator (Konto/API, Rechte je Anbieter im Quellenkatalog prüfen), Aufträge aus den geprüften Zusammenfassungen; jedes Bild als Deutung gekennzeichnet.
- **Vorlesen mit neuronalen Stimmen (vorgemerkt, Andi Neck 2026-10-14):** Texte einmalig mit einem Cloud-Dienst (z. B. Azure Neural, de-CH) vertonen und als Audiodateien je Abschnitt ablegen; braucht Konto/API-Schlüssel, Kostenberechnung vorab, Ablage ausserhalb des Git-Repos, automatische Neuvertonung bei Textänderungen. Züridüütsch damit nicht abgedeckt (verfügbare Mundart-Stimmen erst prüfen). Bis dahin: Gerätestimmen (v0.50).
Primärbelege; standardisierte Revisions-/Reviewmetadaten; Versifikationsmodell; SQLite-Projektion; anschliessend eine Oberfläche auf der stabilisierten Datenbasis. Technische Produktentscheidungen bleiben offen.
