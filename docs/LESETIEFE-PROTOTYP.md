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

Testhierarchie: Bibel → Testament → Buchgruppe → Buch → Kapitel → technischer Testblock → Vers. 66 Bücher, 1’189 Kapitel, 6’704 Testblöcke und 31’102 Verspositionen. Protestantischer Kanon und KJV-Zählung sind eine deklarierte Testkonfiguration, keine endgültige Festlegung des Kanons oder Versifikationsmodells.

Alle 66 Bücher haben kurze deutsche KI-Zusammenfassungen (`draft`, fachlich ungeprüft). Hinzu kommen Zusammenfassungen für die obersten Ebenen und vier Beispielkapitel. Die restlichen Kapitel und Verse zeigen ausdrücklich Platzhalter. Oberflächensprache und Inhaltssprache sind getrennt: Englisch übersetzt die Bedienelemente, nicht die deutschen Inhaltsentwürfe.

Die Testblöcke umfassen bis zu fünf Verse und sind **keine natürlichen Texteinheiten**. Buchgruppen und Kapitel sind Navigationshilfen. Die vereinbarte semantische Gliederung nach Gedankengängen, auch über Kapitelgrenzen hinweg, ist noch anzubinden. Satz- und Wortebenen sowie historische und heutige Perspektiven sind im neuen Entwurf nicht implementiert; der bisherige Markus-Studienprototyp enthält andere Funktionen.

Dieser Entwurf importiert seine Inhalte nicht in `data/` und ersetzt keine vorhandenen Studien oder Schema-IDs. Lokale Navigations-IDs sind nur UI-Zustand; Buch-, Kapitel- und Versknoten führen zusätzlich `canonicalRef` nach USFM-Buchcode. Testblock-IDs sind keine redaktionell freigegebenen Abschnitts-IDs. Die Kapitel-/Verszahlen wurden für den Repository-Import aus der als gemeinfrei bezeichneten eBible-KJV-Ausgabe unabhängig nachgezählt; kein Bibeltext wurde daraus kopiert. Herkunft und Prüfsumme: [provenance.json](../app/reading-stream/provenance.json).

## Technische Grenzen und nächste Schritte

- Eigenständige HTML/CSS/JavaScript-Datei ohne externe Abhängigkeiten. Geräteumschaltung und Icons benötigen keine ChatGPT-Laufzeit.
- Geräteansichten halten ihren Zustand separat. Einstellungen und Lesepositionen werden noch nicht dauerhaft gespeichert.
- Alle Ebenen haben vollständige Datenströme; jeweils zehn weitere Einträge werden bei Bedarf angehängt. Bereits geladene Einträge werden noch nicht virtualisiert. Sehr lange Lesesitzungen können daher den DOM vergrössern.
- Suche nach Buch/Bibelstelle, noch keine Volltextsuche.
- Nächster Schritt: vorhandene kanonische Daten und echte Zusammenfassungen/Gliederungen anbinden; Rückkehrposition, Touch-Bedienung und Tastaturzugang in echten Browsern und auf Geräten prüfen.

## Prüfungen

`node scripts/test_reading_stream.cjs` prüft vollständige Ebenen, Zählungen, Referenzsuche und Grenzen der Lesereihenfolge ohne Zusatzpakete. Im Arbeitslauf wurden zusätzlich DOM-Interaktionen mit jsdom geprüft: Vertiefen, Rückkehr zur gespeicherten Position, Inhaltsverzeichnis, Menü, Sprache, Textgrösse und Themes. Das ersetzt keine visuelle Prüfung auf realen Geräten und keine fachliche Inhaltsprüfung.
