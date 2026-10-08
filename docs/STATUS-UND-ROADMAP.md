# Status und nächste Schritte · 2026-10-08

## Gesichert und vorhanden
- Alle Originalpakete v0.1–v0.5; rekonstruierte lokale Git-Historie mit je einem Snapshot.
- Aktueller Pilot v0.5: 36 Datensätze, darin 6 Tags.
- Variantenstellen Mk 3,29: Sünde/Gericht und ist/wird sein, als vorläufige Forschungsdaten.
- Revidierbare textkritische Entscheidung; eigene deutsche Arbeitsübersetzung; teilweise Wort-/Phrasenalignments.
- Quellenhinweise, alternative Interpretationen, Prinzip, heutige Anwendung, Kontexte, Parallelstellen und offene Frage.
- Importvorbereitung mit SHA-256; synthetische Tests; einfacher Tag-/ID-Validator.

## Bei der Übernahme erkannte technische Lücken
1. `scripts/validate.py` lädt `schema/record.schema.json` nicht. Der bisherige PASS prüft nur vier Feldnamen, ID-Eindeutigkeit und Tags.
2. Schema und Daten sind nicht konsistent: unter anderem `text-unit` statt `text_unit`, `studie` statt `study`; spätere Objekttypen und Statuswerte fehlen im Schema.
3. Referenzen ausserhalb der Tags werden nicht vollständig geprüft. Die Studie listet noch nicht alle später hinzugekommenen Ergebnisse in `outputs` auf.
4. Quellen-, Review- und Zeitmetadaten sind uneinheitlich und lückenhaft.
5. Importer belegt einen Datei-Hash, schreibt jedoch noch keinen verbindlichen Upstream-Commit in den erzeugten Datensatz. Vor einem echten Import müssen Format/Referenzkodierung mit der gewählten Quelle geprüft werden; synthetische Tests verifizieren das externe Format nicht.

Diese Punkte wurden dokumentiert, nicht durch eine stillschweigende Datenmigration verdeckt. Der v0.5-Forschungsbestand ist bytegleich übernommen.

## Fachlich noch offen
- Vollständiger editionsgebundener griechischer Text Mk 3,22–30 und belastbare Token-/Lemma-Zählungen.
- Eigene Prüfung der berichteten Lesarten an Primärmaterial und kritischem Apparat einschliesslich Korrekturschichten.
- Vollständige Wortzuordnung für alle neun Verse.
- Präzise wissenschaftliche Fundstellen, weitere Gegenargumente und eigenständige Kontextanwendungen.
- Kritische Prüfung des abgeleiteten Prinzips: Es enthält stärkere Begriffe als die begrenzte Beobachtung zum Wissen der Schriftgelehrten. Diese Ableitung ist nicht allein durch den Pilotbestand abgesichert.

## Nächster geplanter Meilenstein v0.6
Eine konkrete MorphGNT-Fassung samt Quellen-/Lizenznachweis und Upstream-Commit aufnehmen, Importer gegen das tatsächliche Format prüfen, den gesamten Versumfang importieren und daraus reproduzierbare Zählungen erzeugen. Zeitgleich Modell/Schema/Validator konsistent machen. Die hier ergänzte Dokumentation ist eine Sicherung des Stands und wird nicht als v0.6-Forschungsfortschritt bezeichnet.

## Danach
Primärbelege und vollständige Alignments; standardisierte Revisions-/Reviewmetadaten; SQLite-Projektion; anschliessend eine Oberfläche auf der stabilisierten Datenbasis. Technische Produktentscheidungen bleiben offen.
