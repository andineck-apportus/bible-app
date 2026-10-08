# Herkunft und Umfang der Übernahme

Am 8. Oktober 2026 für das vom Nutzer angelegte Repository `https://github.com/andineck/bible-app.git` vorbereitet. Gewünschter lokaler Pfad des Nutzers: `/Users/andineck/dev/bible-app`. Diese Cloud-Sitzung hat keinen direkten Zugriff auf diesen Mac-Pfad.

## Grundlagen
1. Fünf tatsächlich vorliegende ZIP-Pakete `bible-knowledge-v0.1.zip` bis `bible-knowledge-v0.5.zip`. Die Bytes sind unverändert unter `archive/packages/` archiviert; Prüfsummen und Herkunfts-IDs stehen in `provenance/packages.json`.
2. Aktuelle Arbeitsdateien aus v0.5. Original-README zusätzlich unter `docs/README-original-v0.5.md`; die versionierten Zusatz-READMEs bleiben erhalten.
3. Wiedergefundene Anforderungen aus dem Projektgespräch „Bibel App“ (Beginn 30.08.2026, fortgeführt bis 08.10.2026): insbesondere Kontextachsen, Zoom-System, Zeitversionierung, Tags, Git und Quellenprozess. Die abgerufenen Erinnerungen sind Zusammenfassungen; ein vollständiges wörtliches Gesprächstranskript liegt dieser Übernahme nicht bei.
4. Sichtbares Gespräch vom 25.09.2026 zu Übersetzungsmethoden.

## Neu in dieser Übernahme
Deutsche Gesamtdokumentation, Einstieg, Metadatenübersicht, Arbeitsprozess, Entscheidungsübersicht, Roadmap, Arbeitsregeln, Paketarchiv und Inventar. Diese Ergänzungen erklären den Stand; sie stellen keine neu abgeschlossene Forschung oder implementierte App dar.

## Rekonstruierte Geschichte
Die fünf Pakete wurden der Reihe nach als Git-Snapshots importiert. Auf GitHub bestehen dafür fünf eigene Commits; ihre Zuordnung steht in `provenance/github-imports.json`. Die zusätzliche lokale Arbeitskopie verwendet Tags `import/v0.1` bis `import/v0.5`; diese lokalen Tags wurden nicht nach GitHub übertragen. Commit-Zeitpunkte zeigen den Import, nicht die ursprüngliche Entstehung. Der versehentlich in v0.4 enthaltene Python-Bytecode wird nicht als aktive Quelldatei importiert, bleibt jedoch im unveränderten ZIP enthalten. Der innere Ordnername des v0.2-ZIP lautet noch v0.1; die Paketdatei und Prüfsumme bestimmen die Herkunft.

## Grenzen der Vollständigkeit
Vollständig gesichert sind die fünf auffindbaren Pakete und die daraus übernommenen aktuellen Dateien. Nicht vorliegende Rohquellen, unveröffentlichte lokale Mac-Dateien, ein vollständiges Originalgespräch sowie noch geplante Funktionen werden nicht als enthalten behauptet. Historische Quellenprüfungen werden als Angaben des übernommenen Arbeitsstands bewahrt, nicht als neue Prüfung dieser Sitzung.
