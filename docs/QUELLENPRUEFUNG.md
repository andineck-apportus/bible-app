# Ausserbiblische Quellen am Text nachschlagen

Hintergrundnotizen (`background_note`) nennen in `sources_de` antike Quellen (Josephus, Philo, Mischna, Talmud, Qumran,
Septuaginta, Kirchenväter, griechisch-römische Autoren). Die Entwürfe entstehen aus dem Gedächtnis der KI. Bevor eine Angabe als
belegt gelten kann, wird sie am Text nachgeschlagen; das Ergebnis steht im Feld `source_check` der Notiz.

## Feld `source_check`

```json
"source_check": {
  "date": "2026-10-18",
  "result": "confirmed",            // confirmed | corrected | partly | unverifiable
  "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Textausgaben nachgeschlagen; keine fachliche Prüfung.",
  "checked": [
    {"source": "Josephus, Leben (Vita) 1–6",
     "found_at": "https://… (Ausgabe, Übersetzung)",
     "finding_de": "Stelle sagt, was die Notiz behauptet (priesterliche Herkunft aus öffentlichen Verzeichnissen, Vita 6)."}
  ]
}
```

- `confirmed`: Jede genannte Stelle sagt, was die Notiz ihr zuschreibt.
- `corrected`: Stellenangabe oder Aussage war falsch und ist in Text bzw. `sources_de` berichtigt (alte Angabe in `finding_de` nennen).
- `partly`: Ein Teil ist bestätigt, ein Teil nicht auffindbar; der Text der Notiz sagt das (z. B. in `uncertain_de`).
- `unverifiable`: Keine frei zugängliche Ausgabe gefunden; die Angabe bleibt als ungeprüft gekennzeichnet.

## Arbeitsweise

- Nur frei zugängliche Ausgaben im Web (z. B. Perseus, Sefaria, Lacus Curtius, Early Christian Writings, Wikisource,
  Dead Sea Scrolls Digital Library, CCAT/LXX-Ausgaben). Nichts aus geschützten Übersetzungen in die Daten kopieren; nur
  Fundstelle und eigene kurze Zusammenfassung.
- Zählungen beachten (Josephus: Buch, Kapitel, Abschnitt nach Niese bzw. Whiston; Mischna: Traktat Kapitel,Halacha;
  Talmud: Blatt a/b; Qumran: Schriftrolle Kolumne,Zeile).
- Lässt sich eine Aussage nicht belegen, wird sie abgeschwächt, als unsicher gekennzeichnet oder gestrichen – nicht passend gemacht.
- Die Prüfung ist eine KI-Prüfung; sie ersetzt keine fachliche Prüfung (AGENTS.md).

In den Studienwerkzeugen (`scripts/authoring/*_study_*.py`) steht das Feld als Wörterbuch `SOURCE_CHECKS = {"BG-…": {…}}`
neben `BACKGROUND`; `_study.write_study` schreibt es in die Notiz. Die App zeigt unter der Notiz, ob und mit welchem
Ergebnis nachgeschlagen wurde.
