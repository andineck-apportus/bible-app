# Lesetiefe-Prototyp · 2026-10-11

Eigenständiger UX-Entwurf aus dem Designgespräch mit Andi Neck. Einstieg: [app/reading-stream/index.html](../app/reading-stream/index.html). Die Datei direkt im Browser öffnen; kein Build, Server oder Internetzugriff erforderlich. Mobile und Tablet/Desktop lassen sich oben umschalten. Der bestehende datenbasierte Markus-Prototyp bleibt separat erhalten.

## Vereinbarte Bedienidee

Jede Zoomstufe ist eine fortlaufende Lesefassung. Scrollen führt zum nächsten Inhalt derselben Ebene; Vertiefen öffnet die darunterliegende Fassung am aktuellen Eintrag. Kontext führt zur übergeordneten Zusammenfassung zurück. Lesepositionen werden während der Sitzung erhalten. Das Inhaltsverzeichnis und die Stellensuche sind zusätzliche Sprungmöglichkeiten.

- Start bei der ganzen Bibel; Ebenenwähler für den direkten Wechsel der Lesetiefe.
- Ruhige, typografische Gestaltung, inspiriert vom Auftritt der Fondation Beyeler; keine übernommenen Markenassets, Bilder oder Schriften.
- Mobile-first mit wenig ungenutztem Raum; auf breiteren Ansichten zusätzliche Navigation links.
- Neutraler Hell-/Dunkelmodus ohne Grünstich, Oberflächensprachen Deutsch und Englisch, Textgrösse.
- Einheitliche Auswahlfelder statt betriebssystemabhängiger Dropdown-Popups.
- Logo: geometrisches B um 90 Grad gegen den Uhrzeigersinn gedreht, darunter zwei Quadrate nebeneinander mit gemeinsamen Kanten; reine SVG-Pfade.

## Umfang und Grenzen

Testhierarchie: Bibel → Testament → Buchgruppe → Buch → Kapitel → technischer Testblock → Vers. 66 Bücher, 1’189 Kapitel, 6’701 Testblöcke und drei kanonische Pilotabschnitte und 31’102 Verspositionen. Protestantischer Kanon und KJV-Zählung sind eine deklarierte Testkonfiguration, keine endgültige Festlegung des Kanons oder Versifikationsmodells.

Alle 66 Bücher haben kurze deutsche KI-Zusammenfassungen (`draft`, fachlich ungeprüft). Hinzu kommen Zusammenfassungen für die obersten Ebenen und vier Beispielkapitel. Die restlichen Kapitel und Verse ausserhalb der Markus-Pilotstelle zeigen ausdrücklich Platzhalter. Oberflächensprache und Inhaltssprache sind getrennt: Englisch übersetzt die Bedienelemente, nicht die deutschen Inhaltsentwürfe.

Ausnahme Markus 3,20–35: drei echte Texteinheiten aus `data/text-units/`, mit unveränderten IDs. Die übrigen Testblöcke umfassen bis zu fünf Verse und sind **keine natürlichen Texteinheiten**. Buchgruppen und Kapitel sind Navigationshilfen. Die vereinbarte semantische Gliederung nach Gedankengängen, auch über Kapitelgrenzen hinweg, ist noch anzubinden. Eine eigene Satz-/Wort-Zoomstufe fehlt weiterhin. In der Pilotstelle sind Wortdetails und heutige Anwendung aufklappbar.

Dieser Entwurf importiert seine Inhalte nicht in `data/` und ersetzt keine vorhandenen Studien oder Schema-IDs. Lokale Navigations-IDs sind nur UI-Zustand; Buch-, Kapitel- und Versknoten führen zusätzlich `canonicalRef` nach USFM-Buchcode. Testblock-IDs sind keine redaktionell freigegebenen Abschnitts-IDs. Die Kapitel-/Verszahlen wurden für den Repository-Import aus der als gemeinfrei bezeichneten eBible-KJV-Ausgabe unabhängig nachgezählt; kein Bibeltext wurde daraus kopiert. Herkunft und Prüfsumme: [provenance.json](../app/reading-stream/provenance.json).

## Technische Grenzen und nächste Schritte

- Eigenständige HTML/CSS/JavaScript-Datei ohne externe Abhängigkeiten. Geräteumschaltung und Icons benötigen keine ChatGPT-Laufzeit.
- Geräteansichten halten ihren Zustand separat. Einstellungen und Lesepositionen werden noch nicht dauerhaft gespeichert.
- Alle Ebenen haben vollständige Datenströme; jeweils zehn weitere Einträge werden bei Bedarf angehängt. Bereits geladene Einträge werden noch nicht virtualisiert. Sehr lange Lesesitzungen können daher den DOM vergrössern.
- Suche nach Buch/Bibelstelle, noch keine Volltextsuche.
- Nächster Schritt: weitere kanonische Daten und echte Zusammenfassungen/Gliederungen anbinden; Rückkehrposition, Touch-Bedienung und Tastaturzugang in echten Browsern und auf Geräten prüfen.

## Prüfungen

`node scripts/test_reading_stream.cjs` prüft vollständige Ebenen, Zählungen, Referenzsuche und Grenzen der Lesereihenfolge ohne Zusatzpakete. Im Arbeitslauf wurden zusätzlich DOM-Interaktionen mit jsdom geprüft: Vertiefen, Rückkehr zur gespeicherten Position, Inhaltsverzeichnis, Menü, Sprache, Textgrösse und Themes. Das ersetzt keine visuelle Prüfung auf realen Geräten und keine fachliche Inhaltsprüfung.

## Integrierte Markus-Pilotstudie (v0.12)

Menü → Pilotstudie Markus 3,20–35 oder Stellensuche. Auf Abschnittsebene fortlaufende Zusammenfassungen und getrennte Befunde, Deutungen samt Gegenargumenten, Prinzip, Anwendung und offene Frage. Vertiefen öffnet die Verse: 16 unveränderte Arbeitsübersetzungen, sechs alternative Wiedergaben/Lesarten, 249 griechische Wörter und 28 Variantenstellen. Wortzuordnung nur dort, wo vorhanden (3,22–30). Editionenkonsens ist keine Handschriftenzählung; berichtete Handschriften bleiben ungeprüfte Arbeitsnotizen. Quellen, Lizenzen und Bewertungsgrenzen sind in der Oberfläche sichtbar. Keine modernen Parallelübersetzungen hinzugefügt.

`template.html` bearbeiten, danach `python3 scripts/build_reading_stream.py`: verwendet die vorhandene Projektion aus `build_prototype.py` und bettet die Daten in `index.html` ein. Erzeugte Dateien nicht von Hand ändern. Keine kanonischen Daten geändert.

Zusätzlicher optionaler DOM-Test: `npm install --no-save jsdom`, dann `node scripts/test_reading_stream_dom.cjs`. Prüft beide Geräteansichten, Piloteinstieg, Details, Rückkehrposition und Durchlesen über Kapitelgrenzen. Keine visuelle Browser-/Geräteprüfung.
