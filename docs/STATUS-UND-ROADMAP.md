# Status und nächste Schritte · 2026-10-09 (v0.9)

## Gesichert und vorhanden
- Alle Originalpakete v0.1–v0.5; rekonstruierte Git-Historie mit je einem Snapshot.
- **Studienprototyp Mk 3,20–35** (`app/prototype/`): Zoomstufen Buch → Abschnitt → Einheit → Vers → Wort, Textschichten Deutsch/Griechisch/Wort für Wort, Variantenstellen mit Gesichertheit, Wortdetails mit zwei Annotationen, Kette Befund → Deutung → Prinzip → Anwendung, Studienpfad in sechs Schritten. Erzeugt mit `scripts/build_prototype.py` nur aus Daten des freien Kerns.
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
6. Der kürzere Markusschluss steht in SBLGNT innerhalb von 16,8 (Tokens 16,8/21–52) und ist noch nicht als eigener Abschnitt ausgewiesen; ebenso der längere Schluss 16,9–20 ⟦ ⟧.
7. Der Apparateintrag 7,21–22 liesse sich mit versübergreifenden `base_tokens` eindeutig zuordnen; noch nicht umgesetzt.

## Befunde aus dem Import
- Die alte Arbeitstranskription von Mk 3,29–30 weicht nur in einem Wort von SBLGNT ab: `ἀλλ’` statt `ἀλλὰ` (3,29). Vergleich: `reports/compare-TEXT-MRK-003-029-030-WORKING-vs-SBLGNT.json`. Die Transkription bleibt als historischer Arbeitsstand erhalten.
- SBLGNT markiert in 3,29 `ἁμαρτήματος` als Variantenstelle; das stimmt mit `VAR-MRK-003-029-001` überein. Die weiteren SBLGNT-Variantenstellen in 3,25–28 sind seit v0.7 auf Editionsebene erfasst (`VAR-SBLGNTAPP-*`).
- Zeugenangabe zu prüfen: `VAR-MRK-003-029-001` führt Ephraemi (C) bei κρίσεως. Nach dem Gegenlesen besteht der Verdacht, dass C* ἁμαρτίας und erst ein Korrektor (C²) κρίσεως liest. Am kritischen Apparat bzw. NTVMR prüfen und ggf. Korrekturschichten trennen.
- `VAR-SBLGNTAPP-MRK-003-029-01` (nur ἁμαρτήματος) und `VAR-MRK-003-029-001` (αἰωνίου ἁμαρτήματος) betreffen dieselbe Stelle mit unterschiedlicher Abgrenzung.
- Die Art der Abweichung (Umstellung, Auslassung, Ersetzung) ist bei Apparatlesarten noch nicht klassifiziert (`unclassified`).
- Die Glossen von R1 (`ἁμαρτήματος`) und R3 (`ἁμαρτίας`) in `VAR-MRK-003-029-001` lauten beide «ewiger Sünde»; der Unterschied ist sprachlich noch zu beschreiben.

## Fachlich noch offen
- Eigene Prüfung der berichteten Lesarten an Primärmaterial und kritischem Apparat einschliesslich Korrekturschichten.
- Fachliche Prüfung der importierten Morphologie/Lemmata für die Perikope.
- Fachliche Prüfung der Arbeitsübersetzung und Wortzuordnung Mk 3,22–30.
- Präzise wissenschaftliche Fundstellen, weitere Gegenargumente und eigenständige Kontextanwendungen.
- Kritische Prüfung des abgeleiteten Prinzips: Es enthält stärkere Begriffe als die begrenzte Beobachtung zum Wissen der Schriftgelehrten. Diese Ableitung ist nicht allein durch den Pilotbestand abgesichert.

## Nächster Meilenstein v0.10 (Vorschlag)
Rückmeldungen zum Prototyp einarbeiten; Wortzuordnung für 3,20–21 und 3,31–35; Handschriftenbelege aus der NTVMR-API (CC BY 4.0) als zweite Bewertungsmethode; Zeugenangabe Ephraemi (C) in Mk 3,29 klären; Versifikationsmodell auf Basis von STEPBible TVTMS; typspezifische Schemas.

## Danach
Primärbelege; standardisierte Revisions-/Reviewmetadaten; Versifikationsmodell; SQLite-Projektion; anschliessend eine Oberfläche auf der stabilisierten Datenbasis. Technische Produktentscheidungen bleiben offen.
