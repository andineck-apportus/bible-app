# Changelog

Änderungen am Bibel-Wissensfundus. Die Einträge v0.1–v0.5 sind aus den vorhandenen Paketen rekonstruiert; sie sind keine Behauptung über ursprüngliche Veröffentlichungsdaten. Alle fünf Pakete wurden am 8. Oktober 2026 nach GitHub übernommen. Der aktuelle Einstieg und die Bedienung stehen in [README.md](README.md), offene Arbeiten in [Status und Roadmap](docs/STATUS-UND-ROADMAP.md).

## v0.121 — 2026-10-26 — Markus 1–4 und 6–8 nach «Struktur zuerst»

- **41 Abschnitte und 7 Kapitel neu** (Kernanalysen mit Struktur, unabhängig geprüft; Zusammenfassungen Hochdeutsch und Züridüütsch; Bilder): Sandwich-Erzählungen 3,20–35 und 6,7–30 als Rahmen, Zwölferliste in der Reihenfolge des Markus, vier Böden in Gleichnis und Deutung, Lasterliste 7,21–22 vollständig, zweistufige Heilung 8,22–26; nichts aus Matthäus oder Lukas übernommen. Korrigiert u. a.: «beraten, wie sie ihn umbringen könnten» (3,6) statt Tötungsbeschluss, Herodes nicht erschrocken (6,14–16), kein Hochzeitszeichen beim Geburtstagsmahl, Schweigegebot an die Leute (7,36).
- Noch 185 Bilder in alter Verdichtung (Markus 9–16, Johannes, Lk 11).

## v0.120 — 2026-10-26 — Matthäus vollständig nach «Struktur zuerst»

- **Mt 19–28 und das Buch Matthäus neu** (Kernanalysen mit Struktur, unabhängig geprüft; Zusammenfassungen Hochdeutsch und Züridüütsch; Bilder): sieben Weherufe vollständig, Gleichnisse Mt 24–25, Weltgericht mit den sechs Werken zweimal, dreifache Verleugnung als Steigerung, drei Gruppen von Spöttern, Taufbefehl als Auftrag und Zusage; Buch mit Zweck («Gott mit uns») und Klammer 1,23 ↔ 28,20 als Deutung. Korrigiert u. a.: Hohepriester und Pharisäer versiegeln das Grab selbst (27,66), keine erfundene Trauer der Frauen, Immanuel als Prophetenwort, Menschensohn = Jesus als Deutung gekennzeichnet; Züridüütsch vereinheitlicht («Hoheprieschter», «Ee», «Lehrer»).
- **Neutrale Trennlinie** (`stage.trenner`) zwischen Erzähler und Gleichnis oder zwei Orten im selben Feld; vorher stand dafür das Zeichen «Abstand» mit irreführender Legende.
- Damit ist Matthäus ganz fertig (176 Einheiten). Noch 233 Bilder in alter Verdichtung (Markus ausser Kap. 5, Johannes, Lk 11).

## v0.119 — 2026-10-26 — Matthäus 11–18 nach «Struktur zuerst»

- **43 Abschnitte und 7 Kapitel neu** (Kernanalysen mit Struktur, unabhängig geprüft; Zusammenfassungen Hochdeutsch und Züridüütsch; Bilder): alle sieben Gleichnisse in Mt 13 mit ihren Deutungen, Wehe-Reihe 11,20–24 (über Kafarnaum kein «Wehe», als Musterbruch vermerkt), Stufenverfahren 18,15–17 vollständig, siebenundsiebzigmal; Sprechblasen im Wortlaut. Kapitelbild 13 zeigt jetzt Senfstaude und Sauerteig, Kapitelbild 18 den Mühlstein.
- **Werkzeuge:** Wortzeichen für ein bestimmtes Bild griffen nicht, wenn `bilder_anime.py` als Skript lief (behoben); Spaltenköpfe behalten eine Verneinung; der Vermerk «von einer getrennten Instanz geprüft» bei Zusammenfassungen erscheint nur noch, wenn die Kernanalyse tatsächlich ein `review` hat.
- Noch 298 Bilder in alter Verdichtung (Mt 19–28, Markus, Johannes, Lk 11).

## v0.118 — 2026-10-26 — Matthäus 1–4 und 8–10 nach «Struktur zuerst»

- **30 Abschnitte und 7 Kapitel neu** (Kernanalysen mit Struktur, unabhängig geprüft mit `review`; Zusammenfassungen Hochdeutsch und Züridüütsch; Bilder): Stammbaum 3×14 (dritte Reihe mit 13 Namen vermerkt), drei Versuchungen mit «Es steht geschrieben», Zwölferliste, Erfüllungszitate. Korrigiert u. a.: Rahel allein (keine erfundenen Mütter), keine Soldaten beim Hauptmann, keine «vier Männer» bei Matthäus, Sprechblasen als ganze Sätze, «begraben» mit Grab statt «verstorben».
- Offen zum Entscheid: Vorsteher in Mt 9,18 (Legende zeigt «Jairus», Matthäus nennt keinen Namen); Kreuz als Erkennungszeichen bei Johannes dem Täufer (anachronistisch). Noch 348 Bilder in alter Verdichtung.

## v0.117 — 2026-10-26 — Philipper und 1.–3. Johannes nach «Struktur zuerst»; Sprechblasen verdecken nichts

- **Philipper, 1., 2. und 3. Johannes neu** wie der Pilot: 52 Kernanalysen mit Strukturanalyse, von einer getrennten Instanz gegen den Text geprüft (Feld `review`; u. a. vollständige Reihen Phil 2,6–11, 3,5–6, 4,8 und 1 Joh 2,12–14; «hofft zu kommen» statt angekündigtem Besuch; Diotrephes stösst die hinaus, die aufnehmen wollen; 1 Joh 5,20 wörtlich), Zusammenfassungen (Hochdeutsch und Züridüütsch) und alle Bilder neu daraus; Gegensätze mit der positiven Seite hervorgehoben.
- **«Das Böse»** wieder als dunkler, zackiger Schatten (wie im Lexikon beschrieben) statt Schlange.
- **Sprechblasen** (Hinweis Andi Neck): Bei Gott hält die Blase Abstand zum Strahlenkranz, die Spitze zeigt sichtbar hinein; verdeckt eine Blase ein Zeichen, einen Gegenstand, ein Gesicht oder eine andere Blase, sucht die Platzierung eine freie Stelle nahe beim Sprecher. Neue Prüfung in `pruefe_bilder.py` (Blase überdeckt kein kleineres Zeichen, Blasen überlappen nicht); alle 537 Bilder bestehen.
- Noch 385 Bilder anderer Bücher (restlicher Matthäus, Markus, Johannes, Lk 11) in alter Verdichtung.

## v0.116 — 2026-10-26 — Jona und Obadja nach «Struktur zuerst»; Versbilder für alle Abschnitte

- **Jona und Obadja neu** wie der Pilot: 21 Kernanalysen mit Strukturanalyse, von einer getrennten Instanz gegen den Text geprüft (Feld `review`; u. a. Gewalttat am Bruder in Obd 1,10 sichtbar gemacht, Parallele Jona 1–2 ↔ 3–4 ergänzt, Sprecher präzisiert), Zusammenfassungen (Hochdeutsch und Züridüütsch) und alle 21 Bilder neu daraus; Abschnitte als Szene oder Strukturbild (z. B. die acht Verbote in Obd 1,12–14), Kapitel und Buch als Comic. Noch 437 Bilder anderer Bücher in alter Verdichtung.
- **Neues Zeichen «Geduld, langsam zum Zorn»** (ruhiges Gesicht mit Sanduhr); das offene Meer ist im Hintergrund wieder die eigene Zeichnung statt eines riesigen Wellen-Emoji.
- **Bilder bei den Versen für alle Abschnitte zusammen** ein- und ausblendbar (Hinweis Andi Neck), nicht mehr einzeln.
- **Abstand zur Seitenleiste:** Der Lesebereich begann 20 px unter der Seitenleiste, der Text klebte an ihrer Linie; jetzt mit Abstand. Ohne Versbilder steht der Text wie gewohnt mittig.

## v0.115 — 2026-10-26 — Bildkarten: Aufdecken zeigt auch die Worte im Bild

Hinweis Andi Neck: «Aufdecken» deckt jetzt zusätzlich zu Titel und Zusammenfassung alle Worte im Bild auf (Sprechblasen, Stichwortbänder, Kästchen).

## v0.114 — 2026-10-26 — Lernen: klare Selbstbewertung mit Symbolen

Hinweis Andi Neck: «Nochmal / Schwer / Gut / Leicht» war nicht verständlich.
- Drei Knöpfe mit Symbol und Erklärung, bei Karteikarten und Bildkarten gleich: **✗ Nicht gewusst** (kommt gleich nochmals), **◐ Teilweise** (kommt morgen wieder), **✓ Gewusst** (kommt in 3, 7, 14 … Tagen wieder; die Zahl steht auf dem Knopf). «Gewusst» springt frühestens auf 3 Tage, damit es sich von «Teilweise» unterscheidet.

## v0.113 — 2026-10-26 — Lernen: Bildkarten ohne Worte

- **Neue Lernmethode «Bildkarten ohne Worte»** (Menü › Lernen): Ein Abschnittsbild erscheint nur mit Zeichen; man erzählt den Abschnitt aus dem Gedächtnis und kann einzelne Felder antippen, um ihre Worte zu sehen. «Aufdecken» zeigt Titel und Zusammenfassung, danach bewertet man sich (Nochmal, Schwer, Gut, Leicht); fällige Karten kommen nach dem Leitner-System wieder. Umfang wie bei den Merkversen: Kapitel, Buch oder alle Bücher mit Bildern. Lernstand bleibt auf dem Gerät.

## v0.112 — 2026-10-26 — Neue Zeichen für «ohne Worte»

- **Vier neue Zeichen** statt Behelfslösungen: «bleiben, warten» (stehende Person mit Stecknadel), «mehr» (Pluszeichen), «einsetzen» in ein Amt (Hand über einer älteren Person), «gesund» auch im Glauben (angespannter Oberarm). Eingesetzt bei «Bleib sitzen, meine Tochter!», «Bleib auf meinem Feld!», «Wie viel mehr!», «Setze Älteste ein!» und «Sie sollen gesund im Glauben sein».
- «Der Mann wird nicht ruhen» bleibt bei Boas + schlafen + nicht (passt zum Sinn).

## v0.111 — 2026-10-26 — «Ohne Worte» nur mit Zeichen

Hinweis Andi Neck: Anfangsbuchstaben sind zu schwer zu erraten; im Fragezeichen-Modus braucht es 100 % Symbole, keinen Text.
- **Keine Anfangsbuchstaben mehr:** Sprechblasen, Stichwortbänder, Kästchen, Köpfe und Titel zeigen ohne Worte nur noch Zeichen; Antippen zeigt gleich die Worte.
- **Jedes Wortfeld hat ein Zeichen:** Die 44 Sätze, die noch keins hatten (50 Felder, meist Sprechblasen der Comic-Bilder), bekamen eine geprüfte Zuordnung in `_wortzeichen.json` (z. B. «Talita kum!» → Mädchen + aufstehen). Fehlt künftig eines, meldet `bilder_anime.py` es in `reports/ohne-worte-fehlt.json`; `pruefe_bilder.py` schlägt fehl, wenn ohne Worte irgendein Text sichtbar ist oder ein Feld leer bleibt.
- Noch behelfsmässig (eigene Zeichen fehlen): «bleiben/warten», «nicht ruhen», «mehr», «einsetzen», «gesund im Glauben».

## v0.110 — 2026-10-25 — «Ohne Worte» auf allen Bildern

Hinweis Andi Neck: hilft beim Lernen und später für die Lernkarten.
- Der Knopf «Ohne Worte» steht jetzt bei jedem Bild mit Worten, auf allen Ebenen (Bibel bis Abschnitt): Sprechblasen zeigen die Anfangsbuchstaben, Stichwortbänder und Kästchen ihre Zeichen, Namensschilder verschwinden; Antippen deckt stufenweise auf. `pruefe_bilder.py` prüft «ohne Worte» entsprechend für alle 537 Bilder (kein Wort ohne Ersatz, kein leeres Feld): bestanden.

## v0.109 — 2026-10-25 — Legende je Bild einblendbar, «ohne Worte» startet aus

Hinweise Andi Neck:
- **Legende je Kachel:** Ein Bild (eine Kachel) antippen blendet seine eigene Legende direkt darunter ein, nochmals antippen blendet sie aus; auch per Tastatur. Die ganze Erklärung zum Bild öffnet der Link «Erklärung zum Bild» unter den Bildern.
- **«Ohne Worte» ist beim Öffnen der App immer ausgeschaltet** (wird nicht mehr gespeichert).

## v0.108 — 2026-10-25 — Kapitel und Buch wieder als Comic, Bild antippen für die Erklärung, «ohne Worte» beim Abschnitt

Hinweise Andi Neck:
- **Kapitel- und Buchbilder wieder als Comic-Szenen** (Mt 5–7, Rut 1–4 und Rut, Titus 1–3 und Titus; 31 Strukturfelder umgebaut): Figuren, Sprechblasen und Zeichen statt Strukturbild; jedes Kapitelbild deckt weiterhin jeden Abschnitt ab, was in einem Feld nicht zu sehen ist, nennt die Bildhilfe. Die Abschnittsebene behält die Strukturbilder. Offen: Blindtest ohne Legende durch eine getrennte Instanz.
- **Bild antippen zeigt die Erklärung** (statt Link «Legende und Hinweise»): zuerst die Erklärung je Feld, dann Bild, Figuren und Zeichen; auch bei den Versbildern.
- **«Ohne Worte» auf der Abschnittsebene,** als Knopf mit Fragezeichen oben beim Umschalter Text/Bild (auf dem Handy nur das Symbol). Prüfung «ohne Worte» in `pruefe_bilder.py` entsprechend auf die Abschnittsbilder umgestellt; das Urteil der Waage hat jetzt auch eine Fassung ohne Worte.
- **Höchstens zwei Kacheln nebeneinander** (Raster mit zwei Spalten, jede mindestens 220 px); im Layout-Test geprüft.

## v0.107 — 2026-10-25 — Drei feste Ansichten, Seitenleiste ab 1200 px, Handy: Bilder wischen

Hinweise Andi Neck (Ideen 1, 3 und 4 aus der Besprechung der Anordnung):
- **Drei Stufen statt fliessender Zwischengrössen:** Handy – Kacheln einzeln zum seitlichen Wischen (Versuch; die nächste schaut am Rand hervor); mittel – Bild in voller Breite unter dem Text, zwei Kacheln nebeneinander; breit – Text links, Bild rechts, sobald der Lesebereich Platz hat. Keine Kachel wird schmaler als 220 px.
- **Seitenleiste erst ab 1200 px** (vorher 900 px); darunter bleibt sie über das Menü erreichbar und ihr Platz geht an die Bilder.
- **Neuer Test** `test_bible_layout.cjs`: prüft im Browser bei sieben Breiten Stufe, Mindestbreiten, dass kein Bild aus dem Fenster ragt, Legende bündig und Seitenleiste.
- **Blatt ziehen in Chrome:** Mit der Maus am Kopf startete Chrome teils eine Textauswahl oder ein natives Ziehen und brach die Geste ab; das wird jetzt unterbunden.

## v0.106 — 2026-10-25 — «Eine Ebene tiefer» unter dem Text, Legende links unter dem Bild

Hinweise Andi Neck:
- **«Zu den Testamenten» usw.** steht neben dem Bild gleich am Ende des Texts (vorher unter dem ganzen Eintrag, weit unten); in schmaler Ansicht und «ohne Worte» weiterhin unten.
- **«Legende und Hinweise»** steht linksbündig direkt unter den Bildern (Bildkacheln und Legende gleich breit, höchstens 684 px).
- **Bild neben dem Text** richtet sich jetzt nach dem Lesebereich ohne Seitenleiste (Container-Abfrage, ab 770 px), damit das Bild nicht abgeschnitten wird; zwei Kacheln nebeneinander ab 460 px. Versbilder rechts erst ab 1300 px Fensterbreite.

## v0.105 — 2026-10-25 — Blatt mit Maus und Finger nach unten ziehen

Hinweis Andi Neck: Wischen ging nicht (mit der Maus); erwartet: Das Blatt geht mit nach unten und verschwindet kurz vor unten ganz.
- Griff und Kopf reagieren jetzt auf Maus und Finger (Pointer-Ereignisse statt nur Touch): Das Blatt folgt der Bewegung, der Hintergrund hellt dabei auf. Bei 80 % der Höhe verschwindet es sofort; beim Loslassen nach mehr als einem Drittel (oder nach schnellem Zug) ebenfalls, sonst federt es zurück. Nach einem Zug löst das Loslassen keinen Klick aus.

## v0.104 — 2026-10-25 — Suche mit Buchanfang, Bilder nicht zu klein, Blatt wegwischen

Hinweise Andi Neck:
- **Suche:** Ein eindeutiger Buchanfang genügt («matt 5» findet Matthäus 5) und wird beim Weitertippen gleich als Kürzel übernommen («Mt 5»), damit Kapitel und Vers direkt folgen können. Mehrdeutige Anfänge («ma») bleiben, wie sie sind; Textsuche unverändert.
- **Bilder nicht zu klein:** Neben dem Text steht ein Bild erst ab 1000 px Fensterbreite und bleibt dort mindestens 460 px breit; schmaler steht es in voller Breite unter dem Text (vorher ab 760 px, die Bilder schrumpften bis zur Unlesbarkeit). Versbilder ebenso, mindestens 400 px.
- **Blatt unten wegwischen:** Griff und Kopf mit «Schliessen» bleiben beim Scrollen oben stehen; nach unten wischen am Griff oder Kopf schliesst das Blatt (wie in mobilen Apps), im Inhalt ebenfalls, wenn ganz nach oben gescrollt ist.

## v0.103 — 2026-10-25 — Gross gesetzte Zeichen mit feiner Kontur

Hinweis Andi Neck: «komischer fetter Rand um das Wasser und den Baum» (Bild «Die Bibel»).
- Die einheitliche Kontur wächst mit der Zeichengrösse; gross in einer Szene (Berg, Grab, neue Schöpfung) wurde sie viel dicker als die Umrisse der Figuren. Zeichen ab 44 Einheiten Bildgrösse verweisen jetzt auf eine Variante mit etwa einem Drittel der Strichstärke (`bilder_anime.duenn`, `gross_setzen`); klein (Stichwortband, Zellen) bleibt die Kontur, wie sie war.

## v0.102 — 2026-10-25 — Text bleibt im Kasten, Prüfung immer dabei

Hinweis Andi Neck: Einige Texte ragten über ihren Kasten (z. B. «Plappert nicht wie die Heiden»).
- **Ursache:** Im Stichwortband unter den Feldern wurde die Schriftgrösse bemessen, bevor die Zeichen davor ihren Platz bekamen. Jetzt geht der Platz der Zeichen zuerst ab; passt der Text auch klein nicht, entfällt das Zeichen und die Worte gehen vor.
- **Prüfung erweitert:** `pruefe_bilder.py` prüfte nur Text in den Zellen der Strukturbilder. Neu auch alle anderen Kästen (Stichwortband, Titelblase, Spaltenköpfe, Namensschild): Text und Zeichen bleiben im Rahmen und überdecken sich nicht, in beiden Sprachen und ohne Worte.
- **Fest eingebaut:** `bilder_anime.py` führt die Prüfung nach jedem Zeichnen selbst aus und bricht bei Befunden ab.

## v0.101 — 2026-10-25 — Ein Stil für alle Zeichen, jedes Zeichen gegen den Text geprüft

Hinweis Andi Neck: «alles kritisch prüfen … einheitlich und passend zum Text».
- **Ein Stil:** Auch die eigenen Zeichnungen (Zeichen, Gegenstände, Orte, Handlungen) bekommen die dunkle Aussenkontur und die gedämpften Farben der Emoji (`bilder_anime.einheitlich`); Personen-Emoji mit dunklem Haar und Erdtönen statt Jeans-Blau.
- **Verwendungsprüfung:** Sechs getrennte Instanzen prüften jede Verwendung eines Zeichens in allen 537 Bildern gegen den Bibeltext des Feldes: 217 Korrekturen, z. B. «fliehen» bei Dämonenaustreibungen, «Sorge» bei Furcht, «Stern» für die Vorzeichen der Endzeit, «Gericht Gottes» für menschliche Gerichte, «ablehnen» statt «verleugnen».
- **Neue Zeichen:** «sich fürchten» (erschrockenes Gesicht) und «austreiben» (Dämon-Schatten mit Pfeil hinaus).
- **Sichtprüfung** der gerenderten Bilder durch eine weitere Instanz: Dämon wieder als Schatten ohne Fratze (Lexikonregel), Friede als Olivenzweig statt Taube (Verwechslung mit dem Geist), «freundlich» unterscheidbar von «Erbarmen», «rein» ohne modernes T-Shirt; neun Emoji zurück auf die eigene Zeichnung (u. a. Herz, Stroh, Scheffel, Vergebung); fehlende Verneinungen ergänzt («Sorgt euch um nichts», «ich verurteile dich nicht»).
- **Legenden und Bildbeschreibungen** an die heutigen Zeichen angepasst (beschrieben noch alte Zeichnungen, z. B. «verschlossenes Grab»); schweizerdeutsche Texte sind KI-Entwurf ohne Muttersprachler-Prüfung.
- Offen: kleine Strichzeichnung «Stammbaum», einige weitere Feinheiten der Sichtprüfung (`reports/zeichen-sichtpruefung-2026-10-25.json`).

## v0.100 — 2026-10-25 — Emoji im Stil der Bilder, im Kontext geprüft

Hinweise Andi Neck: Emoji und Eigenes wirkten nebeneinander uneinheitlich; ein Küken für «geboren werden», ein Honigtopf als «Land».
- **Stil angeglichen:** Emoji bekommen automatisch die dunkle Kontur der Figuren, deren Hautton und leicht gedämpfte Farben (`emoji_zeichen.py`, Funktion `stil`).
- **Kontextprüfung** (drei getrennte Instanzen, alle 333 Emoji-Zeichen mit ihren echten Verwendungen): Sinn an jeder Stelle, Ton und Würde (nichts Niedliches, Albernes, Modernes), Tauglichkeit als Gegenstand in Szenen. Ergebnis: 161 ok, 54 durch ein besseres Emoji ersetzt (z. B. Baby statt Küken, Schatztruhe, Anker für Ausdauer), 118 zurück auf die eigene Zeichnung (u. a. Kreuz, Grab, Schiff, Weg, Land, Kuss, Schwamm, Salböl, Gewänder, Stadt); 14 weitere Emoji entfernt, weil sonst verschiedene Begriffe dasselbe Zeichen hätten. Jetzt 201 Emoji-Zeichen. Bericht `reports/zeichen-runde12-kontext-2026-10-25.json`.
- Lehre (SYMBOLPROZESS.md): Ein Auswahltest ohne Kontext lässt sinnwidrige und unwürdige Zeichen durch; die Prüfung im echten Bild gehört fest in den Ablauf.

## v0.99 — 2026-10-25 — Bildzeichen aus Twemoji

Entscheid Andi Neck: «Emoji, wo es geht; sonst prägnant» (detailliert gemalte Körperteile wurden unverständlicher).
- **333 Bildzeichen aus Twemoji** (CC BY 4.0, Twitter, Inc. und Mitwirkende): ein Emoji oder zwei in fester Anordnung (nebeneinander, Zusatzzeichen, Verbotskreis «nicht tun», rotes X «falsch»), Hände und Gesichter im Hautton der Figuren. Werkzeug `emoji_zeichen.py`, Auszug `vendor/twemoji/twemoji-auszug.json`, Lizenz in LIZENZEN.md, Quellenkatalog (SRC-TWEMOJI) und Bildlegende.
- **Automatische Wahl** (`zeichen_runde.py`): vier Instanzen schlugen je Zeichen bis drei Emoji und vier Ablenker vor; neuer Unterscheidungstest `zeichen_test.py --frage auswahl` (richtige Bedeutung unter fünf wählen, vier Instanzen) prüfte das bisherige Zeichen und die Vorschläge nacheinander. Gewählt wurde der erste bestandene Vorschlag, sonst das bessere Zeichen.
- **Bisher behalten:** 48 biblische Besonderheiten ohne passendes Emoji (Tempel, Gesetzestafeln, Altar, Thron, Golgota …), Licht und vollbracht (sonst doppelt), Personen und Rollen (Porträts).
- Grenze: Der Unterscheidungstest ist nachsichtig (auch die bisherigen Zeichen bestanden 376 von 421); er fängt grobe Fehldeutungen und Verwechslungen ab, die Qualität der Zeichnung kommt von Twemoji. Bericht `reports/zeichen-runde12-2026-10-25.json`.

## v0.98 — 2026-10-25 — Zeichen-Durchsicht Runde 11

Hinweis Andi Neck: Hände teils unverständlich, Almosen wie Schüssel, Prozess verbessern.
- **Gestaltungskritik** aller 421 Zeichen ohne Personen (drei getrennte Instanzen): 139 ok, 241 überarbeiten, 41 neu. Neue Prüfstufe `zeichen_test.py --frage kritik` (beurteilt die Zeichnung statt die Bedeutung zu raten); Gestaltungsregeln in SYMBOLPROZESS.md (Hände aus einer gemeinsamen Handbibliothek `haende.py`, Handlungen nicht als blosse Pfeile, keine Bedien-Symbole, keine Doppelten, Gefühle als Gesichter, Orte mit Kontur).
- **127 Zeichen neu gezeichnet** (fünf Instanzen), davon 41 mit bestandener Kritik und Blindtest übernommen; dazu die Auswahl von Andi Neck auf der Auswahlseite (25 neue Fassungen, 6 bisherige behalten). Ersetzungen liegen in `bildsymbole_daten/ueberarbeitet/`; `bilder_anime.library()` übernimmt sie unter derselben Lexikon-ID.
- Befund: Von Hand gezeichnete SVG-Piktogramme erreichen die Qualität bewährter Sätze nicht zuverlässig, und die KI-Kritik schwankt; nächster Schritt ist ein offener, professionell gezeichneter Grundsatz (Emoji) als Basis.

## v0.97 — 2026-10-25 — Ohne Worte: ganzes Feld antippen, leere Glieder benannt

Hinweise Andi Neck:
- **Ganzes Feld antippen:** Ohne Worte deckt das Antippen jetzt auf dem ganzen Feld auf, auch bei Spaltenköpfen und Titelblase (der Rahmen gehört zur umschaltbaren Gruppe), nicht nur auf dem Zeichen. Die App-Prüfung tippt dafür die Ecke eines Feldes an.
- **Leere Glieder:** Wo der Text ein Glied nicht nennt (z. B. Tit 2: kein «damit» bei den älteren Männern), steht statt eines Strichs «im Text nicht genannt» – auch ohne Worte sichtbar, weil es nichts aufzudecken gibt.

## v0.96 — 2026-10-25 — Betende Hände wie das Emoji

Hinweis Andi Neck: die betenden Hände sahen aus wie Füsse. Neu nach dem Vorbild des Emojis «gefaltete Hände»: zwei Handflächen, Fingerspitzen oben zusammen, Finger geschlossen. Drei Fassungen geprüft (auch ineinander gefaltete Hände), alle im Blindtest 4/4; gewählt die Emoji-Fassung.

## v0.95 — 2026-10-25 — Zeichen auch neben den Worten

Hinweis Andi Neck: die Zeichen der Ansicht «ohne Worte» auch mit Worten einblenden.
- **Zeichen neben den Worten:** Titelblase (Zeichen links), Spaltenköpfe, Kästchen ohne eigenes Zeichen und – wo zugeordnet – das Stichwortband zeigen jetzt ein Zeichen, auch in der normalen Ansicht.
- **Geprüfte Zuordnung** für alle 351 Wortfelder der Pilotbilder (`bildauftraege_daten/_wortzeichen.json`, getrennte Instanz): 79 Auto-Treffer bestätigt, 38 ergänzt, 23 ersetzt (z. B. «Gerechtigkeit» → gerecht statt Gericht), 211 neu belegt. Der Automat bleibt nur Rückfall.
- **Neue Zeichen** (Runde 9, 32 px, 4 Instanzen): lehren 4/4, im Verborgenen 3/4, erinnern 4/4; «sich sorgen» neu gezeichnet (besorgtes Gesicht, 4/4); «vollkommen» nur als Wortzeichen erkannt. Offen: «nicht richten» (0/4) und «selig» (segnen, 2/4) brauchen bessere Zeichen.

## v0.94 — 2026-10-25 — Ohne Worte ohne leere Felder, Bilder je Abschnitt, Hände

Hinweise Andi Neck:
- **Ohne Worte – keine leeren Felder:** Titelblase, Spaltenköpfe, Stichwortband, Worte in Sprechblasen und Kästchen ohne eigenes Zeichen zeigen automatisch passende Zeichen (über die Worte gesucht: alle Wörter eines Lexikonnamens müssen vorkommen, zuerst Zeichen aus demselben Feld), sonst die Anfangsbuchstaben. Pfeilbeschriftungen und Namensschilder fallen weg. `pruefe_bilder.py` prüft, dass kein Feld leer bleibt und kein Wort ohne Ersatz steht.
- **Zeichen gross und mittig:** Ohne Worte füllt das Zeichen das ganze Kästchen; erst beim Antippen rückt es kleiner nach oben, darunter die Anfangsbuchstaben; beim zweiten Antippen die Worte. Gilt auch für Köpfe, Blase und Band.
- **Bilder bei den Versen je Abschnitt:** Schalter «Bilder» beim Abschnittstitel auf der Versebene statt einer Einstellung.
- **Hände:** eine Kontur nur aussen (keine Linie mehr zwischen Fingern und Handfläche) bei Hand, Schwur und Grüssen; betende Hände neu gezeichnet (zwei Handflächen, gestufte Fingerspitzen, Daumen vorn). Blindtest Runde 8 bei 32 px: beten, grüssen, Schwur je 4 von 4.

## v0.93 — 2026-10-25 — Bild neben dem Text, Bilder bei den Versen, Kapitel ohne Worte

Hinweise Andi Neck:
- **Bild rechts neben dem Text** auf breiten Bildschirmen, auch bei breiten Strukturbildern; mit Bildern nutzt die Ansicht die ganze Breite (Text in Lesebreite links).
- **Bilder bei den Versen** (Einstellung, Standard aus): auf der Versebene beim ersten Vers eines Feldes das passende Feld des Abschnittsbilds, auf dem Desktop rechts daneben.
- **Kapitelbild ohne Worte** (Schalter beim Bild): Worte verdeckt, Kästchen der Strukturbilder mit grossem Zeichen bzw. Anfangsbuchstaben; Antippen zeigt erst die Anfangsbuchstaben, dann die Worte; die Zusammenfassung daneben ist verdeckt, bis man sie antippt. Die Fassung ohne Worte ist im Bild hinterlegt; `pruefe_bilder.py` prüft auch sie.
- **Verdichtung geschärft:** Abschnitt ohne Verlust relevanter Information (bis 6 Sätze; fehlender Moment ist ein Fehler), Kapitel mit der Kernaussage jedes Abschnitts und der Hauptaussage des Kapitels (geprüft).

## v0.92 — 2026-10-24 — Mt 5,37 «Euer Ja sei ein Ja»

Hinweis Andi Neck:
- **Mt 5,37** lautet jetzt «Euer Ja sei ein Ja, euer Nein ein Nein; was aber darüber hinausgeht, ist vom Bösen» (Züridüütsch «Eues Ja söll es Ja sii, eues Nei es Nei; …»). Die wörtliche Fassung «Eure Rede aber sei: «Ja, ja», «nein, nein»» steht als wörtlichere Fassung in den Übersetzungsentscheidungen, weil «jaja/neinnein» heute abschwächend klingt (Grundsatz in ENTSCHEIDUNGEN.md). Frühere Fassung im `revision_log`.
- Angepasst: Kernanalysen und Zusammenfassungen Mt 5,33–37 und Mt 5, Texteinheit, Bild Mt 5,33–37 (Feld 3, Stichwortband) und Kapitelbild Mt 5.

## v0.91 — 2026-10-24 — Tod und Böses nicht ausblenden; Abstand zum Rahmen

Hinweise Andi Neck:
- **Tod und Böses nicht ausblenden** (BILDSPRACHE.md, BILDPROZESS.md Leitlinie 11, Entscheid): Wer stirbt, getötet, verfolgt, gerichtet oder betrauert wird, ist im Bild zu sehen – nicht weggelassen, nicht beschönigt, nicht ausgemalt (keine Wunden, kein Blut im Detail, keine Verherrlichung). Weglassen nur mit Grund.
- **Neue Zeichen** (Runde 7, bei 32 px geprüft): Verstorbener auf der Bahre, Totenklage, töten (Schwert, ohne Blut), Feuer der Hölle (Gehenna), verfolgen; Hass neu (Rücken an Rücken).
- **Pilotbilder ergänzt:** Tod von Elimelech, Machlon und Kiljon (Rut 1, auch in der Kernanalyse des Buches nicht mehr «Vorgeschichte»), das gestorbene Mädchen und die Totenklage (Mk 5, Augen geschlossen), «töten» und «Feuer der Hölle» (Mt 5), «verfolgt» (Seligpreisungen), Kreuz bei «hingegeben» (Tit 2,14); im Buchbild Matthäus Jesus am Kreuz statt nur des leeren Kreuzes.
- **Abstand zum Rahmen:** Titelblase, Sprecherbild und Sprechblasen haben Luft zum Kachelrahmen; `pruefe_bilder.py` prüft das.

## v0.90 — 2026-10-24 — Pfeile genau von Zelle zu Zelle

Hinweis Andi Neck: Pfeile in den Strukturbildern waren leicht verschoben.
- Pfeile zwischen Spalten, in Pfeilketten und Weichen beginnen und enden genau an den Zellen.
- `pruefe_bilder.py` prüft das bei jedem Lauf (Anfang und Ende höchstens 3 Einheiten von einer Zelle, nicht darin).

## v0.89 — 2026-10-24 — Zeichen «Zuflucht» neu, Test fragt zuerst nach dem Abbild

Rückmeldung Andi Neck: die Henne mit Küken (Rut 2,12 «unter seinen Flügeln») sah aus wie eine Fruchtplatte.
- **Neues Zeichen:** ein grosser Vogel breitet den Flügel wie ein Dach über eine kniende Frau (Rut); bei 32 px von allen Testpersonen als «Vogel über Person» und «Schutz unter Flügeln» erkannt, auch als reiner Umriss.
- **Test verbessert:** Die KI-Testpersonen hatten die alte Henne in Farbe fast immer erkannt, ein Mensch nicht. Der Zeichentest fragt jetzt zuerst offen nach dem Abgebildeten, dann nach der Bedeutung, und prüft zusätzlich den schwarzen Umriss (`zeichen_test.py --frage abbild --silhouette`); erkannt gilt nur, wenn das Abbild richtig benannt wird (SYMBOLPROZESS.md).
- Entscheide: Detail und Merkmale eines Zeichens entscheidet der Test, nicht eine Einzelvorgabe; die Regel «Tore ohne Zinnen» entfällt.

## v0.88 — 2026-10-24 — Zeichen in Einsatzgrösse geprüft, Kästen füllen die Zeile

Hinweise Andi Neck:
- **Kasten ohne Nachbarn füllt die Breite:** jede Zeile in Rastern und Pfeilketten füllt die Breite, auch eine kürzere letzte; die Prüfung `pruefe_bilder.py` meldet Leerraum.
- **Erkennbarkeit in Einsatzgrösse:** Zeichen werden bei 32 px im Kasten geprüft, nicht nur gross (`zeichen_test.py`, SYMBOLPROZESS.md «Prüfung in Einsatzgrösse», Runde 6). Bestand der Pilotbilder: 127 Zeichen gemessen; 24 neu gezeichnet (Erkennung bei 32 px vorher 3, nachher 18), darunter alle mit Händen: Hände mit Ärmel und abgesetztem Daumen, Almosen als Münze in der Bettlerschale.
- **Detailstufen:** je Zeichen drei Stufen blind getestet; mittel (Umriss + 1–2 Merkmale) erkennt man bei 32 px am besten (47 % gegenüber 32 % einfach, 46 % detailliert); Detailregeln und tragende Merkmale je Zeichen im Lexikon. Münzen mit Prägung, wo sie hilft (Denar, Mammon, Gewinn).
- **Zeichen für schwierige Begriffe:** 17 neue, erkannt u. a. gerecht, suchen und finden, auf Sand bauen, bitter, Lohn schon erhalten, Ruhe, Streit; als Wortzeichen (nur mit Wort) u. a. besonnen, fromm, freundlich, Sanftmut, verleumden, sich unterordnen.
- Grössere Zeichen in den Kästen; Zeichen in den Pilotbildern ergänzt (u. a. klug/töricht, Haus auf Sand/Felsen).

## v0.87 — 2026-10-24 — Mehr Zeichen, saubere Strukturbilder, Kapitel mit allen Abschnitten

Hinweise Andi Neck:
- **Mehr Zeichen:** 16 neue Bildzeichen für die Strukturbilder (Auge, Hand, Ohrfeige, Kopf mit Haar, Obergewand, guter und fauler Baum, Axt an der Wurzel, Almosen, weites Tor, Sonne, Regen, Meilenstein, Trost, Mammon, Jota als Wortzeichen), Untergewand als antike Tunika statt T-Shirt; Blindtest Runde 5 (SYMBOLPROZESS.md). In den Zellen der Pilotbilder rund 240 Zeichen ergänzt.
- **Text bleibt in den Kästen, Beschriftungen überdecken nichts:** neue Prüfung im Browser (`pruefe_bilder.py`, de und gsw); lange Wörter werden getrennt, Zeitleisten auf dem Handy senkrecht, Mindestbreite der Zellen, Pfeilbeschriftungen auf einem Schild mit passendem Abstand.
- **Gott oder Mammon** (Mt 6,24) als Verzweigung «entweder – oder» statt beides in einem Kasten.
- **Weniger Leerfläche:** hohe schmale Strukturbilder werden breit (mit schmaler Fassung fürs Handy).
- **Kapitel enthalten jeden Abschnitt** (VERDICHTUNG.md, Regel 9): geprüft in Struktur, Zusammenfassung und Kapitelbild; Zusammenfassungen von Rut 1–2, Titus 1, Mt 5–7 und Bilder von Rut 3, Titus 3, Mk 5, Mt 6–7 ergänzt.
- **Struktur zuerst auch beim Bild:** Ein Bild mit Kernanalyse darf nur Darstellungen nutzen, die deren Strukturanalyse vorsieht; Bilder ohne Strukturanalyse werden als offen gemeldet (`bildauftraege.py`).

## v0.86 — 2026-10-24 — Pilot «Struktur zuerst»: Zusammenfassungen und Strukturbilder

Entscheide Andi Neck vom 2026-10-24 (Verdichtung: Struktur zuerst, Strukturkatalog):
- **Strukturanalyse im Pilot:** Alle 58 Kernanalysen (Rut, Titus, Mk 5, Mt 5–7) haben ein Feld `structure` mit Baumuster, allen Gliedern, Merkmalen (Sprecher, Musterbruch, Modalität, Deutung …) und Darstellung, von einer getrennten KI-Instanz auf Strukturtreue geprüft. Was vorher «weggelassen» war und trägt, steht jetzt drin (z. B. alle Verheissungen der Seligpreisungen, beide Zweige von Bedingungen, der ganze Ältestenspiegel, alle Namen des Stammbaums in Rut 4).
- **Zusammenfassungen neu** (Hochdeutsch und Züridüütsch): wo der Text Reihe, Gegensatz oder Raster ist, als Liste aller Glieder («– die Armen im Geist → ihnen gehört das Reich der Himmel»); die App zeigt die Liste als Liste und liest sie Satz für Satz vor.
- **Strukturbilder:** Reden, Lehre und Briefe als Raster, Spalten («Ihr habt gehört … Ich aber sage euch …»), Weiche mit beiden Zweigen, Pfeilkette («denn», «damit»), Waage («wie viel mehr»), Zeitleiste, Gliederung, Dialog, Kreis, Ringe, zwei Ebenen und Stammbaum; Erzählungen bleiben Szenen. Das Thema steht im Band (z. B. «Wenn ihr aber fastet»).
- **Kacheln einzeln:** Jede Kachel ist ein eigenes Bild; auf dem Handy stehen sie untereinander in voller Breite, breite Strukturbilder haben eine schmale Fassung fürs Handy.
- **Worte im Bild sprachlich geprüft** (getrennte KI-Instanz): rund 30 Befunde verbessert (Satzteile zu ganzen Sätzen, Zeitformen, «zur Frau nehmen» statt «erwerben» in der Mundart, Bezüge von «es/ihn»). Vereinheitlichung der Mundart-Schreibung (din/diin, Söi/Säu …) folgt mit der allgemeinen Überarbeitung des Züridüütsch.
- Werkzeuge: `kernanalyse.py --check`, Entwurfsordner (`BIBLE_CORE_SRC`, `BIBLE_SUMMARY_SRC`), `vorschau_auftrag.py`, `bildworte.py` mit den Worten der Strukturbilder.

## v0.85 — 2026-10-24 — Gleicher Massstab für alle Personen

Hinweis Andi Neck: Jesus wirkte als Redner am Rand teilweise wie ein Kind, andere übergross.
- Alle Erwachsenen eines Felds werden im gleichen Massstab gezeichnet; Gruppen sind nicht mehr grösser als Einzelne. Die Angabe `stage.size` verkleinert nur noch Kinder; der Redner steht am Rand, nicht kleiner (BILDPROZESS.md, Leitlinie 9).
- Alle 537 Bilder neu gezeichnet.

## v0.84 — 2026-10-24 — Bildanordnung: nichts verdecken, Kacheln in lesbarer Grösse

Hinweise Andi Neck:
- **Sprechblasen verdecken nichts Wesentliches:** Der Zeichner merkt sich Zeichen, Gegenstände und Gesichter und sucht für die Blase eine freie Lage nahe beim Sprecher, sonst wird sie etwas kleiner (z. B. das Licht-Zeichen in Mt 5,14–16 ist wieder sichtbar).
- **Pfeile weichen aus:** Handlungspfeile führen nicht mehr über fremde Köpfe, Zeichen oder Sprechblasen; sie wölben sich stärker oder setzen seitlich am Kopf an (z. B. Scheidebrief Mt 5,31, Mantel Mt 5,40, Krone Mt 6,33).
- **Gedankenwolke deutlich:** Denkblasen sind jetzt eine Wolke mit Bögen rundum und drei kleiner werdenden Kreisen zur Figur.
- **Kacheln in lesbarer Grösse:** Jede Kachel wird höchstens etwa 340 px breit gezeigt; Bilder mit mehreren Kacheln werden breiter und stehen auf breiten Bildschirmen unter dem Text statt gequetscht in der halben Spalte.
- **Durchsichtiger Hintergrund** zwischen den Kacheln statt Weiss.
- Regeln ergänzt: BILDPROZESS.md (Leitlinien 9 «nichts verdecken» und 10 «Bildaussage trifft das Thema», Sichtprüfung), BILDAUFTRAEGE-ANLEITUNG.md («Thema benennen», «Nichts verdecken»).
- Vorbereitung «Struktur zuerst»: Kernanalysen können ein Feld `structure` tragen (Prüfung in `kernanalyse.py`); Zusammenfassungen dürfen eine Liste aller Glieder enthalten (Zeilen mit «– »), die App zeigt sie als Liste und liest sie als Sätze vor. Strukturkatalog aus der Analyse aller 66 Bücher (docs/STRUKTURKATALOG.md) mit den Entscheiden vom 2026-10-24.
- Alle 537 Bilder neu gezeichnet.

## v0.83 — 2026-10-23 — Sprechblasen und Worte besser gesetzt

Hinweise Andi Neck:
- **Zwei Zeilen statt kleiner Schrift:** Längere Worte brechen in Band und Sprechblase auf zwei Zeilen um.
- **Sprechblase nahe beim Sprecher:** Bei einer einzelnen Blase steht sie tief über dem Sprecher, wenn dort kein anderes Gesicht ist. Sie weicht nicht mehr ans andere Ende des Felds aus, sondern auch unter die Darstellung Gottes. Die Spitze bleibt dadurch kurz und eindeutig.
- **Keine Zeichen über Sprechblasen:** Freie Zeichen, zum Beispiel eine Krone, weichen den Blasen aus.
- Alle 537 Bilder neu gezeichnet.

## v0.82 — 2026-10-23 — Worte im Bild sprachlich geprüft

- **Neue Prüfregel** (Hinweis Andi Neck): Stichwortband und Sprechblasen müssen für sich allein verständlich und grammatisch richtig sein, in jeder Sprache, ohne Satzfragmente. Die Regel steht in der Anleitung, in BILDPROZESS.md und in AGENTS.md. Das Werkzeug `bildworte.py` listet die Worte für die Prüfung auf.
- **Pilotbilder überarbeitet:** 250 von 292 Worten neu, zum Beispiel «Hören und tun!» statt «hört und sie tut», «Seid gerechter als die Pharisäer!» statt «weit über».
- **Rut 4 Züridüütsch** (Hinweise Andi Neck), mit Übersetzungsentscheid:
  - 4,10 «han ich mir zur Frau gnoo» statt «erworbe» (tönt nach gekauft);
  - 4,17 «D Noomi hät en Sohn übercho!».
  
  Bibeltext, Zusammenfassungen und Titel sind angepasst.

## v0.81 — 2026-10-23 — Pilotbilder mit Worten, Figuren Runde 4

- **Worte im Bild** (Entscheid Andi Neck 2026-10-23):
  - Stichwortband als Leiste unter jedem Feld, mit 1–4 Wörtern wörtlich aus dem Text;
  - Namensschild für Hauptfiguren beim ersten Auftreten;
  - Kernwort in der Sprechblase statt einer Zeichenkette;
  - Briefrand für Aufträge im Brief.
  
  Ein Bild gilt für alle Übersetzungen; die App zeigt die Worte der gewählten Textsprache (Hochdeutsch oder Züridüütsch). Der Validator prüft, dass die Stichwörter so im Text stehen.
- **66 Pilotbilder neu aus den Kernanalysen:** Rut, Titus, Mk 5, Bergpredigt Mt 5–7 mit Merkversen. Ein Feld je tragendem Moment, Bildtyp nach Textart; Redner bei Lehre klein am Rand. Blindtest ohne Legende vorher und nachher, eine Nachbesserungsrunde (docs/BILDPROZESS.md).
- **Kreuzigung** (Entscheid Andi Neck): Jesus am Kreuz in einfacher Form, ohne Wunden, in Joh 19, Mk 15,33–34 und Mt 27,45–46.
- **Kurze Legende:**
  - Je Figur und Zeichen ein Erkennungstext von höchstens 60 Zeichen, Hochdeutsch und Züridüütsch.
  - Die Mundart ist ein KI-Entwurf, nicht muttersprachlich geprüft.
- **Figuren Runde 4:**
  - gemeinsames Jüngermerkmal, klarere Apostel-Zeichen;
  - verwechselbare Paare getrennt;
  - Mengen ohne Kind vorn, die Zwölf mit der Zahl 12;
  - Gefässe, Lose, Ninive und Moab neu.
  
  Blindtest Runde 4: 76 % getroffen, Personen 33 → 47 %.
- **Alle 537 Bilder neu gezeichnet:** Noomi ohne Kind als Zeichen; keine Pfeilwinkel «>» zwischen nahen Figuren; die Zeichen von Rollen wie Jünger und «Mensch» erscheinen nur im Lexikon.
- **Werkzeuge:**
  - `vorschau_bild.py`, `bildtest_paket.py`;
  - `BIBLE_BRIEF_ONLY` bestätigt nur ausgewählte Bildaufträge;
  - `stage.size` verkleinert Figuren;
  - `stage.pose` «cross» zeichnet Jesus am Kreuz.

## v0.80 — 2026-10-23 — Figuren und Zeichen, Runde 3 (Arbeitszweig figuren-qualitaet)

- **Abgestimmte Grundformen** (Hinweise Andi Neck):
  - Locken auf dem Scheitel statt seitlich;
  - Kopftuch tiefer, ohne Bogen über den Brauen;
  - Glatze mit tiefem Haarkranz;
  - dünnere Kontur der Zeichen;
  - Wanderstab schräg über der Schulter, ohne Arm;
  - Altersfalten dezenter.
- **Gruppen:** drei grössere Figuren (vier, wo der Text vier nennt), eine Gruppenfarbe aus dem Lexikon, Zeichen gross vorn. Die Matte ist jetzt ein Strohgeflecht, die Gegner haben einen strengen Blick statt verschränkter Arme.
- **58 Personen und Rollen:**
  - Satan als Rauchschatten;
  - Besessene mit Schatten dahinter;
  - Königin von Saba klar weiblich;
  - Titus mit Kreta statt Brief;
  - Nebenfiguren mit eigenem Zeichen.
- **29 Gegenstände und Orte** neu gezeichnet, Landschaften mit Tiefe, vier Doppelbilder unterscheidbar.
- **Blindtest Runde 3** (docs/SYMBOLPROZESS.md):
  - Überarbeitete Einträge 31 % → 50 % getroffen, gemessen nach einer strengeren Regel.
  - Offen: Apostel, gemischte Gruppen als Familie, mehrere verwechselbare Paare.
- Die Bilder der Bibelstellen sind noch nicht neu gezeichnet; die App zeigt bis dahin den früheren Stand.

## v0.79 — 2026-10-23 — Bildlexikon in sechs Gruppen

- **Klarere Gruppen** (Rückfrage Andi Neck): Im Bildlexikon und in der Legende stehen die Einträge jetzt in sechs Gruppen statt acht Arten: Gott, Jesus, Heiliger Geist · Menschen · Dinge, Natur und Zeit · Orte · Handlungen und Gefühle · Begriffe.
  - Die frühere Sammelart «Zeichen» ist nach der Testklasse aufgeteilt. Glaube, Hoffnung und Gnade stehen unter Begriffe, Herz, Blut und Abend unter Dinge, Natur und Zeit, beten und weinen unter Handlungen und Gefühle.
  - Neues Feld `display_group` im Lexikon. `kind` bleibt für die Bildplatzierung unverändert.

## v0.78 — 2026-10-23 — Fokus nach der Suche

- **Fokus auf dem gewählten Treffer** (Andi Neck): Wählt man in der Suche einen Abschnitt (Klick oder Tab und Enter), liegt der Fokus danach auf diesem Abschnitt im Navigator. Enter öffnet ihn, Tab führt zu den weiteren Abschnitten. Bei Kapitel, Buch und Buchgruppe liegt der Fokus auf dem gewählten Feld.

## v0.77 — 2026-10-23 — Ein Bildstil: Anime

- **Stil «Symbol» eingestellt** (Andi Neck): Die App zeigt nur noch Anime-Bilder, ohne Stil-Umschalter. Die Symbol-Daten bleiben im Repository (Status deprecated), werden aber nicht mehr gebaut.
- **Figuren und Zeichen zuerst:** Vor neuen Bildern werden alle 569 Lexikon-Einträge im Stil Anime geprüft, verbessert und erneut geprüft (docs/SYMBOLPROZESS.md).

## v0.76 — 2026-10-23 — Zusammenfassungen aus der Kernanalyse (Pilot)

- **Neue Zusammenfassungen** für Rut, Titus, Markus 5 und die Bergpredigt Mt 5–7 auf Abschnitts-, Kapitel- und Buchebene (58), je auf Hochdeutsch und Züridüütsch.
  - Sie entstehen aus den Kernanalysen, mit festem Umfang je Ebene (docs/VERDICHTUNG.md).
  - Eine getrennte KI-Instanz hat Inhalt (Momente, Sprecher, Auftrag statt Tatsache) und Sprache geprüft; die Befunde sind eingearbeitet.
  - Die früheren Fassungen stehen im revision_log.
  - Die Mundart ist nicht muttersprachlich geprüft.
- **Werkzeug** `scripts/authoring/zusammenfassungen.py`: prüft Umfang, Momente und Satzzahl der Mundart und schreibt Datensatz, Lokalisierung und `core_basis`.
  - Die älteren Buchwerkzeuge übernehmen die neuen Texte (`_lib.py`), ein erneuter Lauf setzt sie nicht zurück.
  - Der Validator meldet Zusammenfassungen als veraltet, wenn sich die Kernanalyse ändert.
- **Bilder dieser Stellen** sind als «neu zu erstellen» vermerkt (`rework` im Bildauftrag, 66 Aufträge). Sie zeigen bis dahin noch die frühere Fassung; der Validator meldet das als Hinweis statt als Fehler.
- Kernanalyse Rut 2,18–23 bereinigt: Die Kernaussage nannte einen Moment, der als weggelassen geführt war.

## v0.75 — 2026-10-23 — Alternativen markiert, Knöpfe auf allen Ebenen

- **Gepunktet unterstrichen = Alternativen** (Andi Neck): Unterstrichen sind jetzt auch Stellen, an denen die Handschriften abweichen (andere Lesarten, z. B. Mt 6,13), nicht nur Übersetzungsentscheide. Antippen öffnet das Versblatt bei der Lesart, mit ihren Quellen.
- **Keine eigenen Zeichen für einzelne Quellen** (Andi Neck): Der Knopf «Rolle» entfällt. Die Rollen vom Toten Meer stehen als eine Quelle unter vielen im Versblatt unter «Alte Handschriften». Die Versnummer ist umrandet, wenn Handschriften vorhanden sind.
- **«Verstehen» und «Damals → Heute» auf allen Ebenen** (Andi Neck): Die Knöpfe stehen bei Bibel, Testament, Buchgruppe, Buch, Kapitel und Abschnitt.
  - «Verstehen» zeigt die Kernanalyse: wozu geschrieben, worum es geht, die tragenden Momente und was weggelassen ist; Pilot bei Rut, Titus, Mk 5 und Mt 5–7.
  - Wo noch nichts erarbeitet ist, sagt das Blatt das offen.
- **Legende «Zeichen im Text»** in «So arbeiten wir» angepasst; dazu der Grundsatz, dass zu jeder Angabe die Quelle genannt ist.

## v0.74 — 2026-10-23 — Lesen und vertiefen: feste Regeln

- **Feste Darstellung** (Andi Neck, docs/LESEN-UND-VERTIEFEN.md): Verse fortlaufend, Urtext und Details sowie Umschrift sind immer an. Lesarten- und Hintergrundzeilen im Text gibt es nicht mehr. Die fünf Schalter sind aus den Einstellungen entfernt.
- **Jede Information hat ein Zuhause:** Alles zu einem Vers steht im Versblatt, alles zum Abschnitt hinter «Verstehen» und «Damals → Heute».
- **Versnummer:** Jede Versnummer öffnet das Versblatt. Umrandet ist sie nur, wenn der Vers ausgearbeitet ist (vorher war im Urtext-Modus jede umrandet).
- **Unterstreichung:** eine einzige Strichart (gepunktet) für Übersetzungsentscheide, statt zwei.
- **Stand dieser Stelle:** Am Ende jedes Versblatts steht, was erfasst ist und was noch nicht, z. B. «hebräische Handschriften noch nicht verglichen». So wird Fehlendes nicht als «gibt es nicht» gelesen.
- **Neuer Menüpunkt «So arbeiten wir»:** Er erklärt, was wo steht, die Zeichen im Text, den Weg zu einer Stelle, wer prüft, den Stand und den Link zu Daten und Regeln auf GitHub.

## v0.73 — 2026-10-23 — Damals → Prinzip → Heute

- **Grundsatz** (Andi Neck, docs/DAMALS-PRINZIP-HEUTE.md):
  - Der Bibeltext bleibt treu zum Urtext.
  - Übertragen wird daneben, in drei gekennzeichneten Stufen: Hintergrund damals, abgeleitetes Prinzip, Anwendung heute je Zielgruppe.
  - Heutiges, z. B. soziale Medien, steht nie im Text, in Zusammenfassung oder Bild.
- **In der App:** Am Abschnittstitel öffnet «Damals → Heute» (vorher «Geschichte») ein Blatt mit den drei Stufen.
  - Unter «Heute» wählt man die Zielgruppe; die Wahl bleibt gespeichert.
  - «Verstehen» zeigt nur noch, was dasteht und wie man es verstehen kann.
- **Zielgruppen:**
  - Neu ist «Jugendliche» (`CTX-CH-YOUTH-2026`).
  - Die bisherige Zielgruppe heisst in der Auswahl «Allgemein».
  - Eine Anwendung kann mit `reference` auf einzelne Verse eingeschränkt werden.
- **Pilot:** Mt 6,5–6 für Jugendliche (`APP-MAT-1007`): Glaube nicht als Bühne, beten ohne zu posten. Die Grenze ist angegeben: Der Text verbietet nicht, vom Glauben zu erzählen (Mt 5,16).

## v0.72 — 2026-10-23 — Kernanalysen Pilot

- **Kernanalysen** (docs/VERDICHTUNG.md, neuer Typ `core_analysis` in `data/core-analyses/`):
  - Jede Einheit hat eine Kernaussage, 1–6 tragende Momente und eine Liste des bewusst Weggelassenen.
  - Jeder Moment hat einen Erkennungsmoment (fürs Bild) und Stichwörter wörtlich aus der hochdeutschen Arbeitsübersetzung (fürs Wortband).
  - Erfasst sind auch Textart, Sprecher sowie Personen und Orte.
  - Pilot mit 58 Einheiten:
    - Rut: Abschnitte, Kapitel, Buch;
    - Titus: Abschnitte, Kapitel, Buch;
    - Markus 5: Abschnitte, Kapitel;
    - Bergpredigt Mt 5–7: Abschnitte, Kapitel.
  - Entstanden als KI-Entwurf und geprüft von einer getrennten KI-Instanz gegen den Text; die Befunde sind eingearbeitet und je Einheit unter `review` festgehalten.
  - Keine fachliche Prüfung durch Personen; Durchsicht durch Andi Neck steht aus.
- **Werkzeug** `scripts/authoring/kernanalyse.py`:
  - prüft Umfang je Ebene, ob die Stellen innerhalb der Einheit liegen und ob die Stichwörter im Text stehen;
  - prüft, ob die Personen und Orte im Bildlexikon stehen;
  - prüft «oben nichts, was unten fehlt»;
  - schreibt Fingerabdrücke von Text bzw. Kinderanalysen.

## v0.71 — 2026-10-22 — Pfad unten statt Lesetiefe

- **Eine Navigation nach oben und unten** (Andi Neck): Die Leiste unten zeigt den Pfad mit echten Namen («Bibel › NT › Evangelien › Mt › 5 › Die Seligpreisungen › 9»); jedes Glied springt direkt auf seine Ebene. Rechts öffnet ein Knopf mit der nächsten Ebene («Kapitel ↓», «Abschnitt ↓», «Vers ↓») die Auswahl am aktuellen Ort (Liste oder Raster, zuletzt gelesener Eintrag markiert). Auf Versebene entfällt der Knopf.
- **Entscheide zu Bildern** (Andi Neck): Zielwerte vorerst zum Ausprobieren und nach dem Pilot überprüfen; Namensschilder für Hauptfiguren beim ersten Auftreten; kurze, gleichmässige Legendentexte je Figur und Zeichen.
- **Verdichtung** (docs/VERDICHTUNG.md, Entscheide Andi Neck): eine gemeinsame Kernanalyse je Einheit als Grundlage für Zusammenfassung und Bild, Auswahlregeln (Kernaussage vor Bekanntheit), Umfang je Ebene, von unten nach oben; alle Zusammenfassungen werden neu erstellt. BILDPROZESS.md auf den Bildteil gekürzt.
- **Zeichen: Prozess und Ausgangsmessung** (docs/SYMBOLPROZESS.md, reports/zeichen-blindtest-2026-10-23.json): alle 191 Bildzeichen ohne Legende getestet; frei erkannt: Gegenstände 66 %, Handlungen 47 %, Begriffe 20 %. 82 bleiben, 66 werden überarbeitet, 43 Begriffe werden Wortzeichen.
- **Vorschlag Bildprozess** (docs/BILDPROZESS.md): Bilder, die man ohne Legende lesen kann – Bildtypen je Textart, Erkennungsmoment, Stichwortband, Blindtest ohne Legende mit Zielwerten, Prüfprotokoll; Entscheide offen.
- **Suchfeld sofort aktiv** (Andi Neck): Beim Öffnen der Navigation steht der Cursor im Suchfeld; man kann gleich tippen.
- **Abgewandte Figuren mit Gesicht** (Hinweis Andi Neck, Händler in Joh 2): Statt Hinterkopf gespiegelt mit Blick zur Seite, damit die Figur wie in der Legende erkennbar bleibt (beide Stile, alle 90 Stellen mit «away»).
- **Titus: Auftrag statt Tatsache** (Hinweis Andi Neck): Der Brief ist von Paulus. Wo Bilder Titus handelnd zeigen, beschreibt die Legende jetzt den Auftrag («Auftrag an Titus – …: Titus soll …»); bei Tit 1,6–8 spricht Paulus, nicht Titus.
- **Richtige Stelle nach dem Navigieren** (Hinweis Andi Neck): Der gewählte Eintrag steht jetzt genau oben unter der Kopfleiste und bleibt dort, während sich darüber noch etwas aufbaut; Titelzeile und Pfad zeigen sofort die gewählte Stelle (vorher teils den Eintrag davor, z. B. «Maleachi 4,6» vor Matthäus). Beim Nachladen nach oben bleibt der oberste sichtbare Eintrag stehen, statt zu springen; die Leisten bleiben nach dem Sprung sichtbar.
- **Ausgearbeitete Verse markiert, bevor das Buch geladen ist** (z. B. Rut im Navigator).
- **Testament-Umschalter** (Andi Neck): «AT | NT» als kleiner runder Umschalter wie Text/Bild, direkt vor den Buchgruppen (voller Name als Hinweis).
- **Abschnitt direkt öffnen** (Andi Neck): Im Navigator öffnet ein Tipp auf die Abschnittszeile (Pfeil-Knopf) den Abschnitt sofort; «Verse» rechts zeigt nur seine Verse zur Wahl. Auch in der Auswahl unten zeigt ein Pfeil, dass die Zeile öffnet.
- **Entfernt:** «Lesetiefe wählen» sowie die Knöpfe «Kontext» und «Vertiefen»; ihre Aufgabe übernehmen Pfad und Auswahl.
- **Abschnitte auch in noch nicht ausgearbeiteten Kapiteln:** Navigator und Auswahl bieten dort die vorläufigen Fünf-Vers-Abschnitte an («Verse 1–5» …), damit jedes Kapitel dieselben Stufen hat.

## v0.70 — 2026-10-22 — Navigation: Suche und Auswahl

- **Reihenfolge** (Andi Neck): «Zuletzt gelesen» steht vor der Suche, «Ausgearbeitete Stellen» am Ende des Navigators.
- **Suche** findet je nach Eingabe Vers, Abschnitt, Kapitel und Buch («Mt 5,3» → Vers, Abschnitt, Kapitel, Buch; «Mt 5» → Kapitel, seine Abschnitte, Buch) und Abschnitte über ihren Titel («Feindesliebe»); jeder Treffer mit Ebene und, beim Vers, dem Anfang des Textes.
- **Treffer antippen:** Ein Vers öffnet sich direkt. Höhere Ebenen werden im Navigator ausgewählt: Der Pfad («Auswahl: Die Bibel › Neues Testament › Evangelien › Matthäus › Kapitel 5») ist klickbar, darunter ist die nächste Ebene wählbar (Kapitel, Abschnitt, Verse); «… öffnen» springt hin.
- Abschnitte unter «Abschnitt wählen» werden ebenfalls ausgewählt statt gleich geöffnet; danach stehen nur ihre Verse zur Wahl.

## v0.69 — 2026-10-20 — Veröffentlichung über Cloudflare Pages

- **Automatischer Build** (GitHub Actions, `.github/workflows/deploy.yml`): Daten prüfen, Python- und App-Tests (jsdom, Playwright), bauen; bei Push auf `main` Veröffentlichung von `build/bible/` auf Cloudflare Pages (Projekt `atmo-bible`). Braucht die Repo-Geheimnisse `CLOUDFLARE_API_TOKEN` und `CLOUDFLARE_ACCOUNT_ID`.
- **Cache:** Pakete mit Prüfsumme in der Adresse (`?v=…`, im Manifest der Seite), dürfen ein Jahr im Cache bleiben; `index.html` und `manifest.json` immer neu prüfen (`_headers`, vom Build erzeugt).
- **Einzeldatei nicht mehr im Repo:** `app/bible/index.html` (rund 72 MB) wird beim Build erzeugt und in GitHub Actions als Download abgelegt; das Repo wächst nicht mehr mit jeder Fassung (Grenze von GitHub: 100 MB je Datei).

## v0.68 — 2026-10-20 — Name: Atmo Bible

- **Name** (Andi Neck): «Atmo Bible – open, free, from overview to original». Steht nur dort, wo er gebraucht wird: Seitentitel, Name für den Startbildschirm, «Über diese Fassung», README; Begründung und verworfene Varianten in docs/ENTSCHEIDUNGEN.md.
- **Bereinigt:** Der Arbeitsname «Lesestrom» ist aus App, Skripten, Tests und Dokumentation entfernt; dort steht neutral «App».
- **Speicher unabhängig vom Namen:** Schlüssel `bible:settings`, `bible:learn`, `bible:recent`; die alten (`lesestrom…`) werden beim ersten Start übernommen, Einstellungen und Lernstand bleiben erhalten.
- Historische Einträge (Changelog, Revisionsprotokolle der Datensätze) behalten den alten Namen.

## v0.67 — 2026-10-18 — Aufgeräumt: app/bible; Quellen nachgeschlagen, Apparat ergänzt

- **App-Verzeichnis aufgeräumt** (Andi Neck): Der Lesestrom liegt jetzt in `app/bible/` (vorher `app/reading-stream/`); Bauskript `scripts/build_bible.py`, Prüfungen `scripts/test_bible*.cjs`, aufgeteilte Fassungen in `build/bible/` und `build/bible-txt/`. Der erste Studienprototyp (`app/prototype/`, `scripts/build_prototype.py`) ist entfernt und nur noch in der Git-Historie.
- **Antike Quellen am Text nachgeschlagen** (Matthäus): Alle 88 Hintergrundnotizen mit ausserbiblischen Quellen (Josephus, Philo, Mischna, Talmud, Qumran, Septuaginta, Kirchenväter, griechisch-römische Autoren) in frei zugänglichen Ausgaben geprüft: 73 bestätigt, 11 berichtigt, 3 teilweise bestätigt, 1 nicht nachprüfbar; ebenso die Quellenangaben in Befunden und Deutungen. Berichtigt u. a.: Josephus nennt in Ant 20,200 den Hohepriester nicht (jetzt 20,203); Macrobius erwähnt den Kindermord (Satz «keine andere Quelle» gestrichen); Sir 51 spricht der Lehrer, nicht die Weisheit; Josephus spricht von Schätzung und Tribut, nicht von Kopfsteuer. Neues Feld `source_check` an jeder geprüften Notiz, im Lesestrom unter der Notiz angezeigt; Anleitung [docs/QUELLENPRUEFUNG.md](docs/QUELLENPRUEFUNG.md). KI-Prüfung, keine fachliche Prüfung; einige Stellen nur über Sekundärquellen belegt (vermerkt).
- **SBLGNT-Apparat Matthäus vollständig:** die 7 vom Import nicht zugeordneten Einträge (1,7–8; 11,9; 16,2–3; 16,3; 19,17; 26,60; 26,61) von Hand nachgetragen (`sblgntapp_nachtrag_mat.py`), als Alternativen in der Übersetzung, mit automatischer Kollation der Handschriften; die Kollation kann jetzt Stellen über Versgrenzen vergleichen. Widersprüche zu den CNTR-Transkriptionen sind benannt (z. B. 032 bei 16,2b–3).
- **Texte vom Toten Meer: Jesaja und Psalmen:** 22 Rollen zu Jesaja (darunter die grosse Jesaja-Rolle 1QIsaᵃ, 1290 Verse) und 40 zu den Psalmen (darunter 11QPsᵃ) aus ETCBC dss, nicht kommerzielle Schicht, mit Wort-für-Wort-Vergleich zum Leningrad-Codex. Vergleichstext direkt aus MACULA Hebrew (keine neue Tokenschicht), Psalmzählung über scripts/versification.py. Besserer Abgleich: ungleich lange Abschnitte nach Ähnlichkeit ausgerichtet (z. B. Jes 53,11 «Licht» als zusätzliches Wort statt Verschiebung), «und» am Wortanfang zählt nicht mehr als blosse Schreibweise; Rut, Jona, Obadja neu verglichen. App: Verse ohne Übersetzung zeigen ein Zeichen «Rolle»/«n Rollen», das die Handschriften im Blatt öffnet; Leningrad-Codex mit Endbuchstaben.
- **Bilder, Pfeile nachgetragen:** Pfeile, die wegen der früheren Pfeilstummel weggelassen waren, sind wieder da (Mk 3,7–10 Menge → Jesus; Mt 7,13 Menge → weites Tor; Mt 10,42 Becher → Jünger; Bartimäus und die zwei Blinden rufen Jesus; Simon von Kyrene: Soldat → Simon, Simon jetzt in der Mitte); 1 Joh 2,24–27: Gott → ewiges Leben mit Abstand zum Strahlenkranz.
- **Navigation:** Die Abschnitte eines Kapitels stehen eingeklappt unter «Abschnitt wählen»; darunter direkt die Versnummern (Hinweis Andi Neck).
- **Zeichner, kurze Wege und Platz:** Kurze Handlungslinien (nahe Personen) als Winkel «>» bzw. «<» statt Pfeilstummel (Vorschlag Andi Neck); Zeichen neben dem Kopf wählen die freie Seite und weichen sonst über den Kopf aus (nicht mehr auf Nachbargesichter oder über den Rand); gehaltene Gegenstände können Anfang oder Ziel einer Linie sein.
- **Menü:** Zuoberst «Übersetzung (Lesetext)» (Hochdeutsch/Züridüütsch) und «Sprache (Bedienung)», weil man sie oft wechselt (Hinweis Andi Neck); dann Einstellungen, Lernen, Bildlexikon, Quellen und Rechte. In den Einstellungen nicht mehr doppelt.
- **Pfeile und Abläufe** (Hinweis Andi Neck): Pfeile von Gott gehen direkt vom Rand des Strahlenkranzes zum Ziel, statt zuerst nach oben zu steigen (Bogen jetzt quer zur Verbindungslinie); die Posaune sitzt am Mund, der Trichter zeigt von der Figur weg. Merkverse zeigen Ursache → Wirkung (z. B. Arme → Reich der Himmel). Neue Regel «Abläufe sichtbar machen» in der Anleitung; alle Bildaufträge werden danach überarbeitet.
- **Navigation und Menü neu geordnet** (Hinweis Andi Neck): Suche, «Zuletzt gelesen» und «Ausgearbeitete Stellen» stehen jetzt oben im Blatt «Navigieren» (nicht mehr im Menü); vor der aktuellen Stelle in der Kopfzeile eine Lupe, damit man die Navigation findet. Menüeinträge mit Symbol einheitlich linksbündig.
- **Merkverse umschaltbar** (Hinweis Andi Neck: Karten störten den Lesefluss): Einstellung «Merkverse» mit Aus, Zeichen (Standard: kleines Lesezeichen am Vers, Karte auf Antippen) und Karte (im Text).
- **Lernen** (neu im Menü): Merkverse eines Kapitels, eines Buches, alle oder nur die heute fälligen üben, mit fünf Methoden: Karteikarten mit aktivem Abruf und Selbstbewertung (Leitner-System, Wiederholung nach 1, 3, 7, 14, 30, 60 Tagen), Anfangsbuchstaben, Lückentext stufenweise (25 % bis alles), Wörter ordnen, «Wo steht das?» (Stelle zum Vers bzw. zum Bild). Vorlesen der Verse; Lernstand nur auf diesem Gerät. Prüfung `scripts/test_bible_lernen.cjs`.
- **Merkvers-Karten (Muster Mt 5):** Auf der Versebene erscheint bei ausgewählten Kernversen eine Karte mit Bild zum Einprägen, dem Verswortlaut der gewählten Fassung (Hochdeutsch oder Züridüütsch) und der Stelle; Legende wie bei den anderen Bildern. Bildaufträge mit der neuen Ebene `verse` (`bildauftraege_daten/MAT-MERKVERSE.json`), je ein Feld in beiden Stilen: Mt 5,3; 5,8; 5,9; 5,13; 5,14; 5,16; 5,17; 5,44. Bilder ohne Schrift; der Text kommt aus der Übersetzung. Einzelne Felder ohne Feldnummer.
- **Bilder höchstens zweispaltig, alle Felder gleich gross** (Hinweis Andi Neck): drei Felder neu als zwei oben und eines mittig darunter (vorher drei kleine nebeneinander, 178 Bilder je Stil); ein einzelnes Feld nicht mehr doppelt vergrössert, im Lesestrom halb breit. So haben alle Felder auf dem Handy dieselbe Grösse.
- **Zeichner:** Hand am ausgestreckten Arm (Stil Anime) ohne abstehenden Daumen – er las sich je nach Armrichtung als «Daumen hoch» bzw. «Daumen runter» (Hinweis Andi Neck); Krone und Dornenkrone sitzen auf dem Kopf; lange Gegenstände (Schwert, Rohr) im Stil Anime seitlich mit sichtbarer Hand.

## v0.66 — 2026-10-18 — Matthäusevangelium ganz übersetzt, mit Bildern

- **Matthäus ganz aus dem Urtext** (SBLGNT): Hochdeutsch und Züridüütsch für alle 28 Kapitel mit vollständiger Wortzuordnung, 176 Texteinheiten (Abschnitte und Kapitel), 2100 Übersetzungsentscheidungen, 590 Lesarten-Alternativen (Apparat und automatische Kollation der Handschriften `WREAD-CNTR-MAT`). Einheitliche Begriffe über das ganze Buch (Reich der Himmel, Menschensohn, Menge/Menschenmengen, sich niederwerfen/anbeten, Fallstrick, Heuchler …); die grossen Reden ohne äussere Anführungszeichen. Werkzeuge `scripts/authoring/matthaeus_text_*.py`; das bestehende Vaterunser (Mt 6,5–15) bleibt unverändert. Im SBLGNT fehlende Verse (17,21; 18,11; 23,14) als Lesarten benannt.
- **Studieninhalte** für alle Kapitel (`matthaeus_study_a–d.py`): 178 Befunde, 102 Deutungen mit Gegenargumenten, 220 Hintergrundnotizen, Grundsätze, Anwendungen, offene Fragen, Beziehungen, 28 Kapitel-Zusammenfassungen in beiden Sprachen, vier Studien. Mt 17,5 im Wortlaut an 3,17 angeglichen.
- **Bilder für ganz Matthäus**: 171 neue Bildaufträge (alle Abschnitte und Kapitel), je in beiden Stilen; Bildlexikon jetzt 569 Einträge. KI-Blindtest (getrennte Instanzen, nur Bild und Legende) über alle 171 Anime-Bilder und 57 Symbolbilder: nur 23 bzw. 1 ohne Mängel. Danach alle sieben Bereiche nachgebessert. Zweite Blindrunde als Stichprobe (84 Anime-, 24 Symbolbilder): gemeldete Mängel bei denselben Bildern von 181 auf 157 (Anime) bzw. 16 auf 13 (Symbol) gesunken, die meisten Bilder haben weiterhin Restpunkte. Prüfvermerk (`check`) mit Restpunkten an jedem Bild.
- **Lesestrom:** verschachtelte Texteinheiten (Mt 6 mit dem Vaterunser 6,5–15 und dessen Teilen) werden bis zur kleinsten Einheit aufgelöst; Inhalte der Zwischenebene erscheinen beim Kapitel (`project_study.py`, Feld `merged`). Tests an den grösseren Umfang angepasst (3059 Verse in Mundart). `app/reading-stream/index.html` ist jetzt rund 69 MB (GitHub-Grenze 100 MB).
- **Zeichner** (`bilder_auto.py`, `bilder_anime.py`): Was eine Figur sagt, steht in einer Blase (Teile durch einen feinen Strich getrennt; vorher als «Blase an Blase» gelesen, dritte Aussage ging verloren); Nachthimmel, Denkblase, Figur auf einem Ort (`on`), auf dem Wasser gehen (`on_water`); Knien im Stil Anime deutlicher (stärker geneigt, gefaltete Hände); liegende Figuren ganz im Feld; freie Zeichen nicht mehr in tiefe Sprechblasen. Anime: feines Lid, freundlichere Brauen, lachende Augen bei Freude.

## v0.65 — 2026-10-17 — Bilder für alle übersetzten Stellen, zwei Blindrunden

- **Bilder auf allen Ebenen:** Für alle übersetzten Bücher (Matthäus, Markus, Lukas, Johannes, Philipper, Titus, 1–3 Johannes, Rut, Obadja, Jona) gibt es je Buch, Kapitel und Abschnitt ein Bild im Stil Symbol und im Stil Anime (358 Bildaufträge, 716 Bilder). Die Bilder setzt ein neuer Zeichner (`scripts/authoring/bilder_auto.py`) direkt aus dem Bildauftrag; Personen, Zeichen und Orte kommen aus dem Bildlexikon (jetzt 496 Einträge). Anleitung: [docs/BILDAUFTRAEGE-ANLEITUNG.md](docs/BILDAUFTRAEGE-ANLEITUNG.md).
- **Obere Ebenen ergänzt:** Erzeltern (Verheissung an Abraham), Landnahme, Königtum, Zerstörung und Rückkehr, Pfingsten mit Feuerzungen, der Weg nach Rom, die Briefe der Offenbarung an die Gemeinden; Propheten mit Linie vom Strahlenkranz.
- **Zwei KI-Blindrunden** (getrennte Instanzen, nur Bild und Legende): Runde 1 über alle Anime-Bilder und eine Stichprobe der Symbolbilder, danach 20 Bereiche nachgebessert; Runde 2 über je ein Paket pro Bereich und Stil. Behoben im Zeichner: freundlichere Gesichter (feines Lid, höhere Brauen), Handlungslinien über den Köpfen statt durchs Gesicht, verbundene Sprechblasen, Leserichtung (wer zuerst spricht, steht links), Gruppen als Menge, abgewandte Figuren mit Hinterkopf, Sitzen und Knien, Gebetshände, Speien am Fischmaul, Linien zu freien Zeichen. Legenden beschreiben jetzt, was das Zeichen zeigt.
- **Prüfvermerke** (`check`) für alle neuen Bilder mit Ergebnis und Restpunkten; nicht einzeln geprüfte Symbolbilder sind als solche gekennzeichnet.

## v0.64 — 2026-10-17 — Anime auf allen Ebenen, drei Prüfrunden

- **Anime für alle 18 Bilder:** Bibel, beide Testamente, alle zehn Buchgruppen, Johannes, Johannes 2 und seine drei Abschnitte. Gegenstände und Zeichen wie im Symbolstil, Personen mit Ausdruck (ruhig, ernst, nachdenklich, besorgt, staunend, froh – nie zornig oder drohend).
- **Drei KI-Blindrunden** (getrennte Instanzen, nur Bild und Legende), danach jeweils nachgebessert: Tränen auf den Wangen statt schwebend, Pfeile von Wegführung und Rückkehr in der richtigen Richtung, Mose trägt die Tafeln erst am Sinai, Propheten sprechen mit Gott in der Sprechblase, Paulus mit Brief (Brief als gefaltetes Blatt mit Siegel statt «E-Mail-Umschlag»), Jesus in Johannes 2,23–25 mit ruhigem, abgewandtem Blick statt geschlossener Augen (wirkte hochmütig), höherer Haaransatz bei Mose und König (wirkten grimmig), «ihr» in der Tempelantwort als Gruppe (auch im Symbolstil), Buchrolle beim Adler sichtbar.
- **Prüfvermerke** für alle Anime-Bilder und die geänderten Symbolbilder mit Restpunkten; inhaltliche Lücken der Bildaufträge in STATUS-UND-ROADMAP.
- Stil-Umschalter nun auch auf den Ebenen Bibel, Testament und Buchgruppe.

## v0.63 — 2026-10-17 — Stil-Umschalter beim Bild, Bildlexikon je Stil

- **Stil-Umschalter direkt beim Bild** («Symbol | Anime» neben «Legende und Hinweise») und in der Legende, nur wo es das Bild in mehreren Stilen gibt; die Einstellung im Menü bleibt.
- **Bildlexikon** im Menü: alle Figuren, Gegenstände und Zeichen, die ein Stil zeichnet, nach Art geordnet (Gott/Jesus/Geist, Personen, Rollen, Gruppen, Gegenstände, Orte, Handlungen, Zeichen), mit Umschalter zwischen den Stilen. Die Legende eines Bildes zeigt die Darstellungen seines Stils.
- **Anime nach zweiter Prüfrunde:** Geissel aus geflochtenen Stricken, erhoben über dem davonlaufenden Schaf statt über dem Händler (nach Johannes 2,15), Jesus in der Antwort ernst statt lächelnd, Diener giesst ein statt «zu werfen», Jesus blickt zu Maria. Geissel auch im Symbolstil neu.
- Neuer Test `scripts/test_reading_stream_bilder.cjs`.

## v0.62 — 2026-10-17 — Anime: ganzes Kapitel 2 der Abschnitte; nahtlose Sprechblasen

- **Anime** jetzt für alle drei Abschnitte von Johannes 2: Tempelreinigung (Jesus mit erhobener Geissel, umgestossener Tisch, Münzen, erschrockener Händler, Schaf, Tauben im Käfig; Frage nach einem Zeichen und Antwort Tempel mit Riss → drei Sonnen → Tempel) und Johannes 2,23–25 (Menschen mit leuchtenden Augen unter Sternen und Herzen, Abstand zu Jesus). Neue Figuren Händler und Menge.
- **Sprechblasen** in beiden Stilen als eine einzige Form mit eingebauter Spitze; kein weisses Abdeckrechteck mehr am Übergang (`scripts/authoring/_bubble.py`).

## v0.61 — 2026-10-17 — Bildstil «Anime» (Pilot)

- **Neuer Stil «Anime»** (Einstellungen → Bilder): comicartig ohne Text, damit für alle Sprachen lesbar. Personen mit Gesicht und Ausdruck (Sorge, Ruhe, Entschlossenheit, Staunen, Freude), Manga-Panels mit schrägen Rändern, Bewegungs- und Emotionszeichen; Sprechblasen nur mit Zeichen. Pilot: Hochzeit in Kana (Johannes 2,1–12), gezeichnet nach demselben Bildauftrag wie das Symbolbild. Wo es noch kein Anime-Bild gibt, erscheint das Symbolbild.
- **Lexikon:** Die Regel «ohne ausgeführtes Gesicht» gilt jetzt nur für den Symbolstil; in Stilen mit Gesichtern Züge und Hautton von Menschen der Levante im 1. Jahrhundert, keine Karikatur.
- Vorgemerkt in docs/BILDSPRACHE.md: Bildsprachen je Kultur und Sprache als eigene Stil-Schicht mit Zielkontext.
- Eigene Zeichnungen (CC0), KI-Entwurf, nicht fachlich geprüft; KI-Blindtest im Bild-Datensatz.

## v0.60 — 2026-10-17 — Menü geordnet, Bildlegende kompakt

- **Menü:** Das Hauptmenü enthält nur noch Suche, «Zuletzt gelesen», «Ausgearbeitete Stellen», «⚙ Einstellungen», «Quellen und Rechte» und «Über diese Fassung». Alle Einstellungen stehen in einem eigenen Blatt, gegliedert in **Darstellung** (Farben, Textgrösse, Sprache, Bilder, Verse fortlaufend), **Bibeltext** (Lesetext, Lesarten, Hintergrund, Urtext, Umschrift), **Urtext anhören** (Aussprache, Stimmen, Tempo, Proben) und **Vorlesen** (Stimme, Tempo, Gottesname, Probe); «Zurück zum Menü» oben.
- **Bildlegende:** Statt der doppelten Beschreibung («Vier Felder: …» und Liste) steht je Bildfeld eine kurze Bildhilfe mit Nummer wie im Bild, fettem Kurztitel, was man sieht und wofür die Zeichen stehen, die Stelle klein dahinter (neues Feld `captions_de` im Bildauftrag, Mundart als Lokalisierung). Die Hinweise beginnen nicht mehr mit einer Aufzählung der Felder. Bildbeschreibung (`alt_de`) bleibt für Screenreader.
- Mose: Merkmal ohne interne Kennung.

## v0.59 — 2026-10-17 — Logo auf dem Handy

- Das Herz im Logo erscheint auf Touch-Geräten beim Antippen nur kurz (900 ms) und kehrt dann zur Ursprungsform zurück; vorher blieb es nach dem ersten Tippen stehen. Am Desktop weiterhin beim Darüberfahren.

## v0.58 — 2026-10-17 — Sprechblasen, Seitenleiste

- Die Spitze einer Sprechblase geht jetzt von der Seite aus, die der sprechenden Figur zugewandt ist (unten, oben, links oder rechts), statt immer von unten; spricht Gott (Strahlenkranz), kommt sie seitlich. Blasen, die neben der Figur standen, stehen jetzt über ihr (Kana Feld 1, Tempelreinigung, Propheten, Gebet, Paulus). Keine langen, schräg verzogenen Spitzen mehr.
- **Seitenleiste** (breite Ansicht): Ab Kapitelebene steht oben der Schritt zum vorherigen und unten zum nächsten Elternteil (z. B. «↑ Lukas 24» … «↓ Apostelgeschichte 1»), so kommt man über Buch-, Kapitel- und Abschnittsgrenzen hinweg; der Titel oben (z. B. «Johannes») führt eine Ebene hinauf. Beim Weiterscrollen in ein anderes Buch passt sich die Leiste an. Neuer Test `scripts/test_reading_stream_sidebar.cjs`.

## v0.57 — 2026-10-14 — Bildsprache auf allen Ebenen, Gottessymbol

- **Bilder auf allen Ebenen über den Versen:** neu für die ganze Bibel, Altes und Neues Testament und alle zehn Buchgruppen (je ein bis vier Bildfelder nach der Zusammenfassung, mit einer typischen Bibelstelle je Feld). Gleiche Szenen sehen überall gleich aus (Schöpfung, Meerdurchzug, Sinai, Exil und Hoffnung, Verkündigung Jesu, Kreuz und leeres Grab, Pfingsten, Briefe, neue Schöpfung).
- **Gottessymbol:** goldener Strahlenkranz mit dem Gottesnamen יהוה (Entscheid Andi Neck), möglichst als Sprechender gezeigt (z. B. «Es werde Licht», die Weisung am Sinai). Die Hand aus der Wolke entfällt.
- **13 neue Lexikon-Einträge** (u. a. Gesetzestafeln, Meer, Schöpfung, Prophet, Leier, Hoffnung, Umkehr, Gericht, neue Schöpfung, Exil und Rückkehr, Ausbreitung, Brief, Gemeinde) und Darstellungen für Gott, Heiligen Geist, Mose, Paulus, König, Soldat, Kreuz, Grab, Jerusalem, Berg, Haus, Weg, Boot, Beten und Trauer. Mose trägt die Tafeln erst ab dem Sinai.
- **Blindtest** (zwei Runden) für alle neuen Bilder; nach den Befunden u. a. Taube im Sturzflug statt «Lilie», keine Sonne mehr beim leeren Grab, Tränen neben den Köpfen, Gott spricht am Sinai, Prophet den Menschen zugewandt. Ergebnisse und offene Punkte in den Bild-Datensätzen.
- Legende: Stellenangaben auch für ganze Kapitel und Bereiche über Kapitel («2. Mose 19–34»).

## v0.56 — 2026-10-14 — Bildlexikon, Bildaufträge, Blindtest

- **Bildlexikon** (142 Einträge, stilunabhängig): Personen, Rollen, Gruppen, Gegenstände, Orte, Handlungs- und Bedeutungszeichen mit Pflichtmerkmalen (Grundlage Text, Tradition oder Gestaltung), Verwechslungsregeln und Mundart. Dieselbe Figur sieht in jedem Bild und später in jedem Stil gleich aus.
- **Bildaufträge** je Stelle (stilunabhängig): Bildfelder, wer zu wem spricht (Sprechblasen mit Zeichen), Handlung je Feld; geprüft gegen den Text wie eine Zusammenfassung. Korrigiert: In Kana spricht Maria zu den **Dienern** ([[JHN.2.5]]).
- **Synchron mit dem Text:** Fingerabdrücke der Verse und Zusammenfassungen im Auftrag; der Validator meldet «Bildauftrag veraltet», wenn sich der Text ändert. Bestätigung nur nach erneuter Prüfung (`BIBLE_BRIEF_CONFIRM=1`).
- **Bilder neu gezeichnet** (Johannes, Johannes 2, 2,1–12, 2,13–22, 2,23–25): u. a. leerer Weinkrug mit Traubenzeichen und leerer Becher für «kein Wein mehr», Ohr für «hört auf ihn», Diener giessen Wasser ein, Speisemeister spricht zum Bräutigam, Stern über Jesus und glaubende Jünger; Tempel mit Riss → drei Sonnen → Tempel für «in drei Tagen»; Tauben im Käfig, Becher ohne Fuss, Kranz statt Krone, brauner Adler.
- **Blindtest auf Verständlichkeit** in zwei Runden (getrennte KI-Instanz, nur Bild und Legende); Ergebnis und offene Punkte im Bild-Datensatz und im Legendenblatt. Kein Test mit Menschen.
- **Legende** nach Lexikon: Figuren und Zeichen nach Art sortiert, Bildfelder mit Handlung, Prüfergebnis.
- **Umschalter Text/Bild** auf dem Handy als kleine Symbolknöpfe neben «Verstehen»/«Geschichte».
- **Schema v0.11:** neue Typen `figure` und `illustration_brief` (ohne Migration); Stil mit `renderings` statt eigener Figurenliste. Regeln in AGENTS.md (Lexikon, Bildauftrag, Blindtest, Synchronität) und [docs/BILDSPRACHE.md](docs/BILDSPRACHE.md).
- Offen: ein verständlicheres Gottessymbol (die Hand aus der Wolke wird ersetzt).

## v0.55 — 2026-10-14 — Bildsprache (Stil «Symbol»)

- **Bilder auf den Zoomstufen:** Zu Buch, Kapitel und Abschnitt kann es Bilder geben; auf breiten Bildschirmen (ab 760 px) stehen Text und Bild nebeneinander, auf dem Handy schaltet «Text | Bild» für alle Einträge um. «Legende und Hinweise» öffnet ein Blatt mit Bildbeschreibung, den gezeigten Figuren und dem Hinweis, was das Bild deutet. Im Menü: «Bilder» – Aus oder ein Stil; weitere Stile (z. B. Skizze, Anime) sind vorgesehen.
- **Stil «Symbol»** mit festen Figuren (Jesus mit Kreuznimbus, Maria in Blau, Jünger, Braut, Bräutigam, Gäste, Diener, Speisemeister, Händler, Zeichen) und wiederverwendeten Szenen; erste Bilder: Johannesevangelium (Adler, Licht, Buch), Kapitel 2 (drei Felder) und die Abschnitte 2,1–12, 2,13–22, 2,23–25. Eigene Zeichnungen (CC0), KI-Entwurf, nicht geprüft.
- **Schema v0.10:** neue Typen `illustration_style` und `illustration` (ohne Migration), Validator-Prüfungen, Werkzeug `scripts/authoring/bilder_symbol.py`.

## v0.54 — 2026-10-14 — Gottesname beim Vorlesen

- Beim Vorlesen wird JHWH als «Jahwe» gesprochen (Einstellung im Menü: «Jahwe» oder «Adonai»); der geschriebene Text bleibt JHWH. Hinweis im Menü zur jüdischen Tradition, den Namen nicht auszusprechen.

## v0.53 — 2026-10-14 — Anhören: anhalten, Aussprache auch für Hebräisch

- Alle Anhören-Knöpfe (Wörter, Proben) zeigen während der Wiedergabe das Pausenzeichen; ein erneuter Klick hält an. Läuft gerade das Vorlesen, wird es dabei angehalten. «Vorlesen probehören» als runder Knopf wie die übrigen (kein Zeilenumbruch mehr).
- Aussprache-Einstellung gilt jetzt für Griechisch und Hebräisch: «Heutig» (Gerätestimme Neugriechisch bzw. Neuhebräisch) oder «Schulaussprache» (Umschrift, deutsche Stimme); Aramäisch immer über die Umschrift. Stimmenwahl je Sprache (Griechisch, Hebräisch bzw. Stimme für die Umschrift); Proben für Griechisch, Hebräisch und Aramäisch.
- Hinweis zu besseren Stimmen um Mac und Chrome ergänzt.

## v0.52 — 2026-10-14 — Sprachprüfung aller Übersetzungen und Zusammenfassungen

- **Neue Regel** (AGENTS.md): Nach der inhaltlichen Prüfung folgt bei jeder Arbeit eine sprachliche Prüfung in allen Sprachen und Übersetzungsschichten; Bibeltext nur so weit geglättet, wie Treue zum Urtext, Zeitform, Satzart und Wortzuordnung erhalten bleiben. Autorenwerkzeuge übernehmen Datum und Grund einer Überarbeitung aus `BIBLE_REVISION_DATE`/`BIBLE_REVISION_REASON`.
- **Erster Durchgang** (KI, getrennt nach Büchern) über Bibeltext, Titel und Zusammenfassungen aller Zoomstufen in Hochdeutsch und Züridüütsch: Johannes, Markus, Rut, Obadja, Jona, Philipper, Titus, 1–3 Johannes, Vaterunser sowie Bibel, Testamente, Buchgruppen und alle Buchzusammenfassungen. Korrigiert u. a. altertümliche Wendungen («heisst ihn … tun», «allezeit»), Nominal- und Partizipialstil, Wortstellung, Kongruenz, Fälle, Zeichensetzung, unklare Bezüge, hochdeutsche Muster und Genitive in der Mundart, Mundart-Schreibung; vereinzelt Wiedergabe genauer gefasst (z. B. Ankündigung statt Bericht). Mehrere Hundert Stellen; frühere Fassungen im revision_log.
- Offen: Mundart-Schreibung zwischen Büchern und zwischen Text- und Studienwerkzeugen weiter uneinheitlich (z. B. sig/seg, det/dört, Erzäller/Erzäler) – Festlegung durch eine muttersprachliche Person nötig; Vorschläge für die gesperrten Vaterunser- und Mk-3-Datensätze stehen im Bericht der Sprachprüfung.

## v0.51 — 2026-10-14 — Johannes: Zusammenfassungen sprachlich korrigiert

- Kana (Kapitel 2 und Abschnitt 2,1–12): wie in 2,3–5 wiedergegeben («Sie haben keinen Wein mehr» – «seine Stunde sei noch nicht gekommen» – die Mutter sagt den Dienern, sie sollen tun, was er ihnen sagt), statt «heisst die Diener tun» und ohne deutendes «doch». Ebenso 4,16 und 5,8 ohne «heissen + Grundform». Mundart angeglichen; frühere Fassungen im revision_log.

## v0.50 — 2026-10-14 — Vorlesen natürlicher

- **Zusammenhängend lesen:** Verse bis zum nächsten Titel werden als ein Text übergeben und nur an echten Satzenden geteilt (nicht nach Abkürzungen, Zahlen, «:» oder «;»), damit die Satzmelodie über Versgrenzen läuft; überlange Sätze werden an «;», «:» bzw. Kommas geteilt. Anzeige und Markierung folgen dem Vers, in dem der gesprochene Abschnitt beginnt, und, wo die Stimme es meldet, Wort für Wort.
- **Vorlesestimme:** «Auto» wählt die vermutlich natürlichste deutsche Stimme des Geräts (Premium, Natural, Erweitert, Google vor Kompakt- und Effektstimmen); im Menü eigene Auswahl, Vorlesetempo (Ruhig, Normal, Zügig, getrennt vom Tempo für Ursprachwörter), Probehören und Hinweis, wo sich bessere Stimmen installieren lassen.
- Vorgemerkt: Vertonung mit neuronalen Cloud-Stimmen (siehe Status und Roadmap).

## v0.49 — 2026-10-14 — Vorlesen: Titel, Pausen, Startknopf als Pause

- Titel werden als eigener, etwas leiser und langsamer gesprochener Satz gelesen, mit kurzer Pause davor und danach; ohne Schlusspunkt, damit «Johannes 2» nicht als «Johannes zweiter» gelesen wird.
- Buchnummern als Ordnungszahl: «1. Johannes 3» → «Erster Johannes drei», «2. Mose» → «Zweites Buch Mose» (englisch «First John»); auch in Bibelstellen der Zusammenfassungen.
- Der Startknopf des gerade gelesenen Titels zeigt wie der Player das Pausenzeichen; ein Klick darauf hält an bzw. liest weiter.

## v0.48 — 2026-10-14 — Vorlesen

- **Vorlesemodus:** Neben jedem Titel (Einträge aller Zoomstufen, Kapitel- und Abschnittstitel im Bibeltext) startet ein kleiner Knopf das Vorlesen ab dieser Stelle. Gelesen wird ohne Unterbruch weiter durch dieselbe Ebene: Überschrift und Zusammenfassung bzw. Verse mit Kapitel- und Abschnittstiteln; Einträge ohne Text werden übersprungen, Bibelstellen-Marken als Buch, Kapitel und Vers gesprochen.
- **Player** unten, minimal: Anzeige des vorgelesenen Teils, zurück, Pause/weiter, vor, schliessen. Der vorgelesene Teil ist im Text hinterlegt und bleibt im Blick. Stimme des Geräts (Web Speech API, Sprechtempo aus den Einstellungen); Züridüütsch wird mit einer deutschen Stimme gelesen. Pause setzt am Satzanfang wieder ein, weil Anhalten/Fortsetzen nicht auf allen Geräten zuverlässig ist.
- Neue Prüfung `scripts/test_reading_stream_vorlesen.cjs` (Playwright, nachgebildete Sprachausgabe).

## v0.47 — 2026-10-14 — Logo mit Herz, «Zuletzt gelesen» eingeklappt

- Logo: Beim Darüberfahren, Fokussieren oder Antippen wechselt es zu einem Herz mit denselben oberen Bögen, demselben unteren Mittelpunkt und gleichem Aussenmass; das innere Kreuz bleibt mit 50 % Deckkraft auf denselben Achsen.
- Menü: «Zuletzt gelesen» ist wie die ausgearbeiteten Stellen eingeklappt (mit Anzahl).

## v0.46 — 2026-10-14 — Lesestrom ohne «Ausgearbeitet»-Hinweise

- Buch- und Kapiteleinträge zeigen keine Verweise «Ausgearbeitet: …» mehr; ausgearbeitete Abschnitte erscheinen ohnehin beim Vertiefen, die Liste bleibt im Menü.

## v0.45 — 2026-10-14 — Mundart: «Ältischti»

- Züridüütsch einheitlich «Ältischti» (Gemeindeälteste) und «ältischt…» (älteste), statt «Elteschti» bzw. «eltischt…», in Übersetzungen, Wortzuordnungen, Lokalisierungen und Autorenwerkzeugen (31 Datensätze, 15 Skripte); frühere Schreibung im revision_log vermerkt.

## v0.44 — 2026-10-14 — Johannesevangelium aus dem Urtext

- **Import Johannes:** SBLGNT mit MACULA-Annotation (15 625 Wörter; Schreibvarianten wie Μωσῆς/Μωϋσῆς im Importer ausdrücklich gelistet, ᾿ als Elisionszeichen), SBLGNT-Apparat (770 von 773 Einträgen zugeordnet), Bewertung «Übereinstimmung der Editionen», CNTR-Transkriptionen von 30 Handschriften und 5 Ausgaben, neu u. a. 𝔓66, 𝔓52, 𝔓90, 𝔓5, 𝔓6, 𝔓22, 𝔓28, 𝔓39, 𝔓95, 𝔓106–𝔓109, 𝔓119–𝔓122, 𝔓134, 029, 0162, 0258, 0323 (Metadaten nach gängiger Einordnung, nicht eigens geprüft); maschinelle Kollation aller 21 Kapitel; STEPBible TAGNT (Ausgaben je Wort); Luther 1912 und Elberfelder 1905 zum Vergleich.
- **Übersetzung** Hochdeutsch und Züridüütsch mit vollständiger Wortzuordnung für alle 879 Verse (5,4 ohne SBLGNT-Text, Wortlaut als Lesart bei 5,3), Entscheidungen mit einheitlichen Grundentscheiden (λόγος, ἐγώ εἰμι, δόξα, σημεῖον, μένω, «die Juden» als gekennzeichnete Deutungsentscheidung, παράκλητος, ἀγαπάω/φιλέω), Lesarten-Alternativen. 7,53–8,11 (Ehebrecherin) in ⟦ ⟧ übersetzt; die Einordnung als spätere Einfügung steht als verbreitetes Urteil mit dem Handschriftenbefund der erfassten Transkriptionen.
- **Studieninhalte** Kapitel 1–21: Befunde, Deutungen mit Gegenargumenten, Grundsätze, Anwendungen, Fragen, Beziehungen (auch zu Markus 14–16), Hintergrund zu Abschnitten, Kapitelzusammenfassungen, drei Studien; Kontext CTX-JHN-READERS-0095. Buchzusammenfassung neu gegen den Text gefasst.
- KI-Entwurf mit getrennter KI-Gegenlesung (Übersetzung Vers für Vers, Handschriftenangaben und Zählungen per Skript); keine fachliche oder muttersprachliche Prüfung. Ausserbiblische Quellen- und Literaturangaben der Studien sind nicht nachgeschlagen und als offene Prüfpunkte in STUDY-JHN-0001…0003 vermerkt.

## v0.43 — 2026-10-14 — Menü ohne «Zur ganzen Bibel»

- Menüeintrag «Zur ganzen Bibel» entfernt; dasselbe leistet ein Tippen auf das Logo oben links.

## v0.42 — 2026-10-14 — Zwei Urteile in Zusammenfassungen korrigiert

- **Markus 16:** Dass der kürzere und der längere Markusschluss spätere Ergänzungen sind, steht nicht mehr als Tatsache da, sondern als verbreitetes textkritisches Urteil, mit den Belegen (SBLGNT-Doppelklammern ⟦ ⟧; Sinaiticus 01 und Vaticanus 03 enden nach den CNTR-Transkriptionen mit Markus 16,8) und beim längeren Schluss mit der Gegenposition (Minderheit: ursprünglich; kirchlich weithin als kanonisch anerkannt). Betroffen: TU-MRK-016-001-020 (auch Titel), TU-MRK-016-001-008, TU-MRK-016-009-020 (Titel ohne «spätere Ergänzung»), SUM-CH-MRK-016.
- **Rut 1:** Noomi nennt sich nicht selbst «Mara», sondern bittet die Frauen, sie so zu nennen (Rut 1,20); TU-RUT-001-001-022.
- Hochdeutsch und Züridüütsch; frühere Fassungen im revision_log.

## v0.41 — 2026-10-14 — Zusammenfassungen geprüft, «Zuletzt gelesen»

- **Zusammenfassungen aller Zoomstufen** gegen die eigenen Übersetzungen bzw. den Bibeltext geprüft (KI-Durchgang): rund 150 Korrekturen in Abschnitten, Kapiteln, Büchern, Buchgruppen und Testamenten, z. B. Obadja 15–18 (Entronnene, Josef als Flamme), Rut 1,1–5 (Reihenfolge: Elimelech stirbt vor den Heiraten), Jona 3 (Gott führt das Unheil nicht aus), Markus 3,6 (sie beraten, statt beschliessen), Matthäus 6,14–15 (Bedingung der Vergebung). Die Mundart-Fassungen der Buch- und Gruppenzusammenfassungen waren eigenständige Texte und sind jetzt Übertragungen des Hochdeutschen. Frühere Fassungen im revision_log.
- **Regel** (AGENTS.md): Am Schluss jeder Arbeit alle Zusammenfassungen gegen den Text prüfen; Werkzeug `scripts/authoring/revise_summary.py` für Datensätze ohne laufendes Autorenwerkzeug.
- **Menü:** «Zuletzt gelesen» (Abschnitt- bzw. Kapitelebene, bis 12 Einträge, nur auf diesem Gerät im Browser-Speicher, mit «Verlauf löschen»); die Liste der ausgearbeiteten Stellen ist eingeklappt.

## v0.40 — 2026-10-14 — Jona, 1–3 Johannes und das ganze Markusevangelium aus dem Urtext

- **Jona** (48 Verse, Hebräisch): WLC mit Umrechnung der Verszählung (hebräisch 2,1–11 = KJV 1,17–2,10), Texte vom Toten Meer (MurXII, 4QXII a/f/g; nicht kommerzielle Schicht), Übersetzungen Hochdeutsch und Züridüütsch mit Wortzuordnung, Entscheidungen, Studieninhalte.
- **1–3 Johannes** (132 Verse, Griechisch): SBLGNT, 84 Variantenstellen, Handschriften 01, 02, 03, 04 sowie 𝔓9 und 0232 (CNTR), Übersetzungen mit Wortzuordnung, Entscheidungen, Lesarten-Alternativen (Comma Johanneum anhand der Daten erklärt), Studieninhalte. 3 Joh 1,15 der griechischen Zählung ist nach TVTMS an 1,14 angehängt; die Umrechnung griechisch → KJV (`versification.greek_verse_map`) gilt jetzt auch in den Importern für SBLGNT, CNTR und die Vergleichsbibeln.
- **Markus ganz** (zusätzlich zu 3,20–35): Übersetzungen Hochdeutsch und Züridüütsch mit Wortzuordnung für alle Kapitel, Entscheidungen und Lesarten-Alternativen; Markusschlüsse (kürzerer Schluss in 16,8, längerer 16,9–20) in ⟦ ⟧ und als spätere Ergänzungen erklärt; Verse ohne SBLGNT-Text (7,16; 9,44.46; 11,26; 15,28) ohne Übersetzung, ihr Wortlaut als Lesart. Maschinelle Kollation für alle Kapitel, neu mit 𝔓88, 𝔓137, 059, 0188, 0214, 0315. Studieninhalte für Kapitel 1–16. Luther 1912 und Elberfelder 1905 für Markus, Jona und 1–3 Johannes.
- Kollation: Lesarten mit «…», die sich im Grundtext nicht verankern lassen, werden übersprungen und vermerkt (`not_collated`); falsche Tags (immer TAG-MARK) in den Kollationen von Matthäus, Lukas, Philipper und Titus korrigiert.
- Alles KI-Entwurf mit getrennter KI-Gegenlesung (Übersetzung Vers für Vers, Zählungen per Skript, Quellenangaben teils per Websuche bestätigt); keine fachliche oder muttersprachliche Prüfung.

## v0.39 — 2026-10-14 — Wörterbuch, Ausgaben je Wort, Ketiv/Qere

- **Schemaänderung (explizit):** neue Typen `lexicon` (`data/lexica/`) und `tagged_text_alignment` (`data/tagged-alignments/`); Schema-Titel v0.9. Keine Migration nötig, bestehende Datensätze unverändert. Beschreibung in [docs/DATENMODELL.md](docs/DATENMODELL.md).
- **Wörterbuch im Wortblatt:** UBS Dictionary of the Greek New Testament (überarbeitetes Louw-Nida) und UBS Dictionary of Biblical Hebrew (aus SDBH), beide von UBS unter **CC BY-SA 4.0** veröffentlicht (Lizenztext im Repository geprüft) — anders als die SDBH-/MARBLE-Felder in MACULA, die «used with permission» bleiben und weiter ausgeschlossen sind. Dazu STEPBible TBESG/TBESH als Kurzglossen (CC BY 4.0); die TBESH-Bedeutungsspalte (Abridged BDB, © Online Bible) ist nicht übernommen. Nur Einträge für Wörter der importierten Bücher (Griechisch 3019 UBS-Einträge, Hebräisch 595). Im Wortblatt («Urtext und Details») «Wörterbuch» mit Bedeutungen, Bedeutungsfeld und Kennzeichen «hier» nach der Stellenliste des Wörterbuchs; Wörterbuchtext englisch.
- **Ausgaben je Wort (NT):** STEPBible TAGNT für Matthäus, Markus, Lukas, Philipper, Titus, 1–3 Johannes den SBLGNT-Wörtern zugeordnet (Markus 11 274 von 11 286 Wörtern; nicht zugeordnete gemeldet in `reports/stepbible-tagged-<BUCH>.json`). Im Versblatt Block «Wörter in den Textausgaben»: je Wort «fehlt in TR, Byz», «nur in …», andere Lesung der übrigen Ausgaben, Wörter anderer Ausgaben mit «+». Ausdrücklich Ausgabenbefund, nicht Handschriften.
- **Ketiv/Qere (AT):** aus STEPBible TAHOT die geschriebenen Formen für Rut (12, dazu 3,12 «geschrieben, nicht gelesen»), Obadja (1), Jona (0); im hebräischen Wortblatt «Geschrieben (Ketiv)» / «Gelesen (Qere)». Zusätzlich dStrong je Morphem für die Wörterbuch-Zuordnung.
- Importer `scripts/import_stepbible_tagged.py` und `scripts/import_lexica.py` (Commits und SHA-256 fest); Quellenkatalog nachgeführt (TAGNT, TAHOT, TBESG, TBESH, UBS-Wörterbücher verwendet; neu SRC-STEP-TBESG, SRC-UBS-DBH); Validator prüft Token-Verweise der Zuordnungen; Tests ergänzt. Erwartete Zahlen der Lesestrom-Tests an die neuen ausgearbeiteten Abschnitte (Markus ganz, Jona, 1–3 Joh) angepasst.

## v0.38 — 2026-10-13 — Texte vom Toten Meer (nicht kommerzielle Schicht)

- Erste Daten in `data-nc/`: biblische Rollen vom Toten Meer aus ETCBC dss (Abegg u. a., CC BY-NC 4.0) für Rut (2QRuth a/b, 4QRuth a/b) und Obadja (4QXII g, MurXII), je Vers mit Fragment und Zeile. Von den Herausgebern ergänzte Buchstaben stehen in eckigen Klammern; ganz ergänzte Wörter gelten nicht als Bezeugung.
- Maschineller Vergleich mit dem Westminster Leningrad Codex je Wort: gleich, nur Schreibweise (Lesehilfen ו/י, lange Endungen), teilweise erhalten, abweichend, zusätzlich. Gefunden u. a. 4QRuth a 1,1–2 «בשדה» statt «בשדי» und 1,2 «וישבו» statt «ויהיו». Nicht am Faksimile geprüft.
- Importer `scripts/import_dss.py` (alle AT-Bücher möglich; Verszählung über die WLC-Umrechnung). Lesestrom: im Versblatt («Urtext und Details») Block «Texte vom Toten Meer»; Daten in eigenen Paketen `n/<BUCH>`, abschaltbar mit `BIBLE_APP_NO_NC=1`.
- Quellenkatalog: ETCBC dss als verwendet (nur `data-nc/`); Validator-Tests prüfen jetzt auch mit `data-nc/`.
- Septuaginta (CATSS) wartet auf die unterschriebene Nutzungserklärung; die NTVMR-Schnittstelle ist aus dieser Umgebung gesperrt und braucht die Antwort des INTF (docs/ANFRAGEN.md).

## v0.37 — 2026-10-13 — Quellenkatalog, Quellenkarte, Anfragen

- **Quellenkatalog:** 66 Quellen als `source`-Datensätze mit `catalog` (Bereich, Schicht, Nutzungsrecht frei/BY-SA/nicht kommerziell/auf Anfrage/geschützt, Verwendung verwendet/zitiert/vorgesehen/nicht verwendet, Begründung). Die sechs bestehenden Quelldatensätze sind ergänzt, nicht ersetzt. Werkzeug `scripts/authoring/quellen_katalog.py`.
- **Immer aktuell:** Der Validator verlangt, dass jede Herkunftsadresse in Datensätzen im Katalog steht, verwendete Quellen auf vorhandene Dateien zeigen und keine nicht kommerzielle oder geschützte Quelle im freien Kern als verwendet gilt (mit Negativtests).
- **Quellenkarte** `app/quellenkarte/index.html`, erzeugt aus dem Katalog (`scripts/build_source_map.py`); im Lesestrom als Blatt «Quellen und Rechte» im Menü, mit Filtern und Begründung je Quelle.
- **Anfragen** [docs/ANFRAGEN.md](docs/ANFRAGEN.md): Rechteinhaber nach Nutzen geordnet, mit Kontakt, Prüfdatum und Entwürfen (DBG, INTF, CATSS, UBS, Crossway, Bildrechte); Abschnitt zur Rolle eines gemeinnützigen Vereins. «Erlaubnis» und «Anfrage» sind zu einer Klasse zusammengefasst.

## v0.36 — 2026-10-13 — Verszählung des Alten Testaments umgerechnet

- Umrechnung der hebräischen Verszählung (WLC) in die Navigationszählung (KJV) nach TVTMS (`scripts/versification.py`), eingebaut in den MACULA-Hebrew-Import. Für alle 39 Bücher geprüft (`scripts/check_versification_ot.py`): nach der Umrechnung stimmen alle Kapitel mit der Navigation überein; Neh 7,68 fehlt im hebräischen Text und bleibt leer. Damit kann jedes Buch des Alten Testaments importiert und übersetzt werden.
- Psalmüberschriften, die im Hebräischen eigene Verse sind, stehen vor Vers 1 und sind als Überschrift markiert; geteilte Verse (z. B. Jes 63,19/64,1) folgen TVTMS. Jeder umgerechnete Token behält die hebräische Stelle.
- Rut und Obadja bleiben unverändert (gleiche Zählung). Tests: `scripts/test_versification.py`.

## v0.35 — 2026-10-13 — Rut und Philipper aus dem Urtext

- **Grundsatz** (Entscheid Andi Neck): Der Lesetext geht immer vom Urtext aus; Luther 1912 und Elberfelder 1905 dienen nur dem Vergleich.
- **Rut** (85 Verse, Hebräisch): WLC mit MACULA-Hebrew-Annotation (2026 Morpheme); Arbeitsübersetzungen Hochdeutsch und Züridüütsch aus dem Hebräischen mit Wortzuordnung je Morphem, 66 Übersetzungsentscheidungen (u. a. חֶסֶד, גֹּאֵל, כָּנָף, «Füsse aufdecken», Ketiv/Qere in 4,5), Studieninhalte (14 Befunde, 8 Deutungen mit Gegenargumenten, 9 Hintergrundnotizen, Grundsätze, Anwendungen, Fragen, Beziehungen, Kapitelzusammenfassungen). Freie textkritische Daten (Qumran, LXX) fehlen weiterhin.
- **Philipper** (104 Verse, Griechisch): SBLGNT mit MACULA-Annotation (1626 Wörter), 45 Variantenstellen mit Gesichertheitsbewertung (2 versübergreifende Apparateinträge zu 1,16–17 nicht sicher zuordenbar, siehe `reports/`), Handschriften 01, 02, 03, 04, 𝔓46 und 𝔓15/16 sowie fünf Ausgabentexte (CNTR) mit maschineller Zuordnung. Übersetzungen Hochdeutsch und Züridüütsch mit Wortzuordnung, 52 Entscheidungen (u. a. Christushymnus 2,6–11, πίστις Χριστοῦ 3,9), 11 Lesarten-Alternativen, Studieninhalte.
- Beide Bücher von einem getrennten KI-Durchgang gegengelesen (Übersetzung Vers für Vers, Zählungen per Skript, Quellenangaben); Korrekturen eingearbeitet, z. B. «Moabiter, nicht Moabiterin» als Talmud (Jevamot 76b) statt Mischna, Wochenfest als Fest der Erstlinge, Mundart-Formen vereinheitlicht. Keine fachliche oder muttersprachliche Prüfung.
- Importer: MACULA-Hebrew-Import für alle Bücher des Alten Testaments vorbereitet; bricht ab, wenn die hebräische Verszählung von der Navigationszählung abweicht (Umrechnung noch offen). SBLGNT-Apparat für Philipper, CNTR mit 𝔓46 und 𝔓15/16, Vergleichsbibeln für Rut und Philipper.

## v0.34 — 2026-10-13 — Hintergrund damals für alle 66 Bücher

- 84 neue Hintergrundnotizen auf Buchebene (`scope: book`) für die 64 bisher fehlenden Bücher, für 20 Bücher mit einer zweiten Notiz (z. B. Genesis und altorientalische Fluterzählungen, Jesaja und die grosse Jesajarolle, Daniel und die Datierungsfrage, Markusschlüsse, Datierung der Offenbarung, Nord- oder Südgalatien). Je Notiz Entstehung, Zeit, Ort, Adressaten, die vertretenen Positionen (traditionell und historisch-kritisch, ohne Entscheid), «Nicht sicher», Belegstellen als Marken, ausserbiblische Quellen und Ursprachwörter; alle in Züridüütsch.
- Autorenwerkzeug `scripts/authoring/hintergrund_buecher.py` mit Datenmodulen je Buchgruppe in `scripts/authoring/buecher/`; prüft Pflichtfelder, Kontexte, Marken, unmarkierte Stellen und Umschriften.
- Entstehung: KI-Entwürfe (Claude), danach von einem getrennten KI-Durchgang auf Daten, Quellenangaben und Ausgewogenheit gegengelesen (11 Korrekturen, z. B. Esther/Nehemia in Qumran, Talmud zur Chronik, Sirach zu Jesaja, Luthers Jakobus-Vorrede, 𝔓52-Datierung). Die Gegenlesung konnte Webseiten teils nicht abrufen und stützt sich dann auf Kenntnis der Primärtexte. Keine fachliche Prüfung durch eine Person; Mundart nicht muttersprachlich geprüft.
- Browserprüfung: Hintergrund auf Buchebene in Mundart.

## v0.33 — 2026-10-13 — Titus und Obadja als Muster (Griechisch und Hebräisch)

- **Titus** (ganzer Brief, 46 Verse): SBLGNT-Text mit MACULA-Annotation (659 Wörter), 24 Variantenstellen mit Gesichertheitsbewertung, Handschriften 01, 02, 04 und 𝔓32 sowie fünf Ausgabentexte (CNTR) mit maschineller Zuordnung zu den Lesarten. Arbeitsübersetzungen Hochdeutsch und Züridüütsch aus dem Griechischen mit vollständiger Wortzuordnung, Übersetzungsentscheidungen und sieben Lesarten-Alternativen; Vergleich mit Luther 1912 und Elberfelder 1905.
- **Obadja** (21 Verse): erster hebräischer Text. Westminster Leningrad Codex mit MACULA-Hebrew-Annotation (435 Morpheme; Lemma, Morphologie, Glossen, LXX-Entsprechung); Wortlisten der SDBH («used with permission») bewusst nicht übernommen. Arbeitsübersetzungen Hochdeutsch und Züridüütsch aus dem Hebräischen mit Wortzuordnung auf Morphem-Ebene und Entscheidungen (`heb`); Gottesname als «JHWH» bzw. erklärt. Freie textkritische Daten zu Obadja fehlen; das ist in den Übersetzungsnotizen vermerkt.
- **Studieninhalte** je Buch: Kontext, Befunde, Deutungen mit Gegenargumenten, Grundsätze, Anwendungen, offene Fragen, Beziehungen, Hintergrund damals (auch auf Buchebene, `scope: book`) und Kapitelzusammenfassungen, alle auch in Züridüütsch (Lokalisierungen). KI-Entwurf; ein zweiter KI-Durchgang hat gegengelesen, die Korrekturen sind eingearbeitet. Keine fachliche oder muttersprachliche Prüfung.
- **Hebräisch im Lesestrom:** Text rechts nach links, Wort-für-Wort-Blatt (Morpheme zu Wörtern gruppiert, Glossen, LXX-Entsprechung), lesefreundliche Umschrift (`scripts/hebrew_translit.py`, gleiche Regeln im Browser) und Anhören; Quellenangaben WLC/MACULA Hebrew.
- **Werkzeuge:** `scripts/import_macula_hebrew_book.py`, `scripts/import_comparison_bibles.py` (Luther 1912 und Elberfelder 1905 je Buch, Quelle per SHA-256 fixiert); CNTR-Importer für Titus samt 𝔓32 und ohne Überschreiben bestehender Zeugen-Metadaten; Autorenwerkzeuge mit gemeinsamer Auszeichnung für Übersetzung und Wortzuordnung (`scripts/authoring/_lib.py`, `_study.py`, `titus_*.py`, `obadja_*.py`), die nur bei Änderung schreiben und die frühere Fassung im `revision_log` festhalten.
- Validator: hebräische Übersetzungsentscheidungen (Konsonantenabgleich mit dem Text), Hintergrund mit `scope: book`. Entscheidungsmarken im Text sind keine Knöpfe mehr, sondern umbrechende Textspannen (lange Entscheidungen zerrissen sonst die Zeile).

## v0.32 — 2026-10-13 — Hintergrund damals für Bibel, Testamente und Buchgruppen

- 17 neue Hintergrundnotizen für die oberen Ebenen: Bibel (Entstehung über rund tausend Jahre; wie der Kanon entstand), Altes Testament (Israel zwischen Grossmächten; Tanach und christliche Ordnung), Neues Testament (unter römischer Herrschaft; zuerst Briefe, dann Evangelien) und alle zehn Buchgruppen (u. a. Tora und Exodus mit ausserbiblischen Spuren, Geschichtsbücher, Psalmen und Weisheit, Propheten, Evangelien, Apostelgeschichte, Briefe, Offenbarung). Jede Notiz mit Einschätzung, «Nicht sicher», Belegstellen, ausserbiblischen Quellen und Ursprachwörtern; alle in Züridüütsch. KI-Entwurf, fachlich ungeprüft.
- Datenmodell: `background_note` mit `scope` (`bible`, `testament`, `book_group`, `book`) und `testament`/`group`; vier historische Kontexte (`CTX-HIST-*`). Autorenwerkzeug `scripts/authoring/hintergrund_uebersicht.py`.
- Lesestrom: Knopf «Geschichte» bei Bibel, Testament und Buchgruppe öffnet den Hintergrund; geladen als eigenes Paket `b/_overview` (Mundart in `l/gsw/common`).

## v0.31 — 2026-10-13 — Für die ganze Bibel und viele Sprachen aufgeräumt

- **Pakete:** Der Lesestrom besteht aus einem Kern und nachladbaren, gzip-komprimierten Paketen je Buch (`b/<BUCH>`: Griechisch, Varianten, Deutungen, Hintergrund, Querverweise) und je Sprache und Buch (`l/<Sprache>/<BUCH>`, `l/<Sprache>/common`). Die App lädt sie erst bei Bedarf (Navigation, Weiterlesen, Sprachwechsel). Veröffentlicht wird `build/reading-stream/` (Kern 145 KB, Pakete zusammen 82 KB); `app/reading-stream/index.html` bleibt als Einzeldatei mit allen Paketen (offline, Tests). Für Hosts, die keine Binärdateien ausliefern (z. B. das Claude-Artefakt), gibt es dieselben Pakete als gzip in Base64 (`build/reading-stream-txt/`, `.gz.txt`).
- **Bibelstellen im Fliesstext** als sprachneutrale Marken `[[MAT.6.34]]` statt «Mt 6,34» (186 Marken); die App zeigt sie je Sprache an und verlinkt sie. Werkzeug `scripts/prose_refs.py`; der Validator prüft Marken und meldet unmarkierte Stellen.
- **Titel und Zusammenfassungen** der Texteinheiten in weiteren Sprachen sind Lokalisierungen (wie alle anderen Übersetzungen von Erklärtexten).
- **Neutrale Feldnamen** in Übersetzungsschichten (`from_text`, `to_text`, `note`, `readings`, `origin`, `more_literal`, `other_options`); `_de` nur noch für hochdeutsche Originale und Dokumentation.
- **Vorrang** ohne Heuristik: Arbeitsübersetzungen derselben Sprache dürfen sich nicht überschneiden (Validator); ausgearbeitete Abschnitte werden aus den Daten ermittelt statt von Hand gelistet.
- **Versifikation:** Zuordnungsdaten zwischen hebräischer, lateinischer, griechischer und englischer Zählung aus TVTMS (STEPBible, CC BY 4.0, 22 874 Zeilen, `data/versification/`). Der Validator prüft alle Stellen gegen die Verszahlen der Navigation (KJV) und meldet Abweichungen als WARN (derzeit 5 Querverweise auf 3 Joh 1,15). Die Umrechnung selbst folgt mit dem ersten Text in anderer Zählung.
- Migration `scripts/migrations/v0_31.py`, Protokoll `provenance/migrations/2026-10-13-v0.31.json` (531 Änderungen); Lokalisierungen mit nachgeführtem Fingerabdruck. Historische Autorenwerkzeuge in `scripts/authoring/` sind gegen erneutes Ausführen gesperrt.
- «Zeit des …» im Hintergrund nennt den Evangelisten des jeweiligen Buchs (vorher immer Markus).
- Prüfungen: Validator-Negativtests für Marken und Überschneidungen; Browserprüfung der aufgeteilten Fassung (`scripts/test_reading_stream_split.cjs`).

## v0.30 — 2026-10-13 — Vergleichsübersetzungen je Sprache

- Vergleichsübersetzungen (`historical_comparison`) sind sprachgebunden. Welche Sprachen eine Übersetzungsschicht zum Vergleich zeigt, legt ihr Zielkontext fest (`comparison_languages` im `context`-Datensatz, Reihenfolge = Anzeige); ohne Angabe nur die eigene Sprache.
- `CTX-CH-ZH-GSW-2026`: `["gsw", "de"]` (redaktionelle Annahme: Mundart-Lesende kennen die Bibel meist auf Hochdeutsch). Für Züridüütsch ist noch keine Vergleichsfassung erfasst; das Versblatt sagt das ausdrücklich und zeigt danach Luther 1912 und Elberfelder 1905 unter «Hochdeutsch».
- Projektion: Vergleichseinträge tragen `lang`, Schichten `compare_languages`.
- `node_modules/` in `.gitignore`.

## v0.29 — 2026-10-13 — Alle Inhalte in Mundart, Lokalisierungen, Weiterlesen beim Scrollen

- Neuer Datensatztyp `localization` (`data/localizations/<BCP-47>/<ID>.json`): übersetzt einzelne Felder eines Originaldatensatzes (`localizes`, `fields` mit den Feldnamen des Originals, bei `terms` die Bedeutungen in Reihenfolge). `source_fingerprint` hält je Feld fest, von welchem Stand des Originals übersetzt wurde. Originale tragen keine Übersetzungen; neue Sprachen und neue Deutungen ändern einander nicht.
- Veraltete Felder (Original seit der Übersetzung geändert) meldet `scripts/validate.py` als WARN; die Projektion liefert sie nicht aus, die App zeigt dann das Original. Gemeinsamer Lader `scripts/localizations.py`.
- Züridüütsch für alle Studieninhalte der drei ausgearbeiteten Abschnitte: 11 Befunde, 10 Deutungen (inkl. Gegenargumente und Wortbedeutungen), 2 Grundsätze, 2 Anwendungen, 3 offene Fragen, 25 Hintergrundnotizen, 85 Zusammenfassungen (Bibel, Testamente, 10 Gruppen, 66 Bücher, 6 Kapitel) – 138 Lokalisierungen. Wortbedeutungen und mögliche Entstehung der Lesarten in den gsw-Übersetzungsschichten. Autorenwerkzeug `scripts/authoring/zueridueuetsch_inhalte.py`. KI-Entwurf, muttersprachlich noch nicht geprüft.
- Lesestrom: Studienblatt, Hintergrund, Wort-Blatt, Quellen-Blatt und Zusammenfassungen aller Ebenen folgen dem gewählten Lesetext. Noch Hochdeutsch: Bedienung, Buch- und Gruppennamen, Handschriften- und Ausgabenbeschreibungen.
- Weiterlesen ohne Knopf: nachgeladen wird, sobald «Weiterlesen» in die Nähe des sichtbaren Bereichs kommt (auch wenn der Inhalt kürzer als der Bildschirm ist) sowie beim Ziehen über Anfang oder Ende hinaus (Mausrad, Wischen). Der Knopf bleibt für Tastatur und Vorlesehilfen.
- Prüfungen: Validator-Negativtests für Lokalisierungen (falsches Feld, falsche Listenlänge, veraltet); Bedienungsprüfung für Mundart-Inhalte.

## v0.28 — 2026-10-13 — Abschnittstitel und -zusammenfassungen in Mundart

- Texteinheiten tragen Titel und Zusammenfassung je Sprache (`title_by_language`, `summary_by_language`, Schlüssel BCP-47); hochdeutsche Felder bleiben Standard. Für die neun ausgearbeiteten Einheiten liegt Züridüütsch vor («S Vatterunser», «Nöd zum Schiin und nöd mit vil Wort», «De Striit um de Beelzebul» …).
- Lesestrom zeigt Titel und Zusammenfassungen der gewählten Lesetext-Schicht: im Strom, am Abschnittskopf, in Blättern, Navigator, Pfad und Seitenleiste.
- Noch Hochdeutsch: Zusammenfassungen der oberen Ebenen (Bibel, Testamente, Gruppen, Bücher, Kapitel), Hintergrund, Deutungen und die Bedienung.

## v0.27 — 2026-10-13 — Züridüütsch als zweite Übersetzungsschicht

- Vorgabe: aus den Urtexten und den erarbeiteten Artefakten in beliebige Sprachen und Kulturen übersetzen; zuerst Züridüütsch neben Hochdeutsch.
- Datenmodell: Übersetzungsschichten je Sprache (`language` BCP-47, `target_context`, `orthography_de`, `register_de`, `control_translation`, `review_de`), Wortzuordnung mit `target_language`. Neuer Kontext `CTX-CH-ZH-GSW-2026`.
- Züridüütsch (Dieth-Schreibung, aus dem SBLGNT) für Mt 6,5–15, Lk 11,1–4 und Mk 3,20–35: 31 Verse, 15 Lesarten-Alternativen, 36 markierte Übersetzungsentscheidungen, vollständige Wortzuordnung für Mt 6,9–13 und Lk 11,2–4. Autorenwerkzeug `scripts/authoring/zueridueuetsch.py`. KI-Entwurf; Prüfung der Mundart durch eine muttersprachliche Person vorgesehen (Andi Neck), noch nicht erfolgt.
- Lesestrom: Menü «Lesetext» (Hochdeutsch | Züridüütsch); Lesarten im Text, Entscheidungs-Markierungen und Versblatt folgen der gewählten Schicht; fehlt ein Vers in einer Schicht, erscheint Hochdeutsch mit Hinweis.
- Datenbestand: 3441 Datensätze.

## v0.26 — 2026-10-13 — Titel in der Kopfzeile

- Der Titel-Knopf in der Kopfzeile hatte innen keinen Abstand (die allgemeine Knopf-Regel setzte ihn auf null); der Titel hat jetzt innen Abstand und bleibt über die volle Breite antippbar.

## v0.25 — 2026-10-13 — Seitenleiste auf breiten Bildschirmen

- Die Seitenleiste (ab 900 px Breite) hatte keinen Innenabstand und eine eigene Formensprache. Jetzt: Überschrift der Ebene, Einträge mit Abstand, Hover-Fläche, aktuelle Position gefüllt, Punkt für ausgearbeitete Einträge; der aktuelle Eintrag wird beim Öffnen in Sicht gerollt.

## v0.24 — 2026-10-13 — Einheitliche Formensprache

- Eine Rundung für alles Antippbare und alle Kästen (`--r: 6px`): Segmentleisten, Chips, Raster im Navigator, Pfad, Schliessen, Symbolknöpfe, Versnummern, Lesarten-Karten, Zeugen-Kästen, Suchfeld, «Zurück zu …». Keine Pillen und Kreise mehr; einzige Ausnahme ist der Ein/Aus-Schalter, der als Toggle seine gewohnte Form behält.
- Einstellungen: Beschriftung links, Auswahl rechts; bricht die Auswahl um, steht sie rechtsbündig unter der Beschriftung («Aussprache», «Tempo»). Stimmen werden als einzelne Chips statt als umbrechende Segmentleiste gezeigt.
- Leichter Hover-Hintergrund auf Kopf- und Fussleisten-Knöpfen.

## v0.23 — 2026-10-13 — Navigator, Querverweise, verlinkte Stellen

- Neuer Navigator (Tippen auf die Titelzeile): «Du bist hier» als antippbarer Pfad, dann Altes/Neues Testament → Buchgruppe → Buch → Kapitel → Vers als Raster; ausgearbeitete Bücher, Kapitel und Verse sind mit einem Punkt markiert, ausgearbeitete Abschnitte des Kapitels direkt wählbar; «öffnen» führt auf Buch- oder Kapitelebene. Ersetzt die alte Inhaltsliste.
- Querverweise: 344 799 Verweise von OpenBible.info (CC BY) importiert (`data/crossrefs/`, Typ `crossref_set`). Im Versblatt erscheinen die zehn bestbewerteten als antippbare Stellen.
- Bibelstellen in Erklärtexten, Vergleichslisten und «Ähnliche Stellen» sind antippbar (auch Listen wie «Jes 63,16; 64,7» und Kapitelbezüge wie «(6,14–15)»). Nach einem Sprung erscheint «Zurück zu …».
- «Verse fortlaufend» ist jetzt Standard (gespeicherte Einstellung wird einmalig umgestellt). Verse ohne Text erscheinen im Fliesstext nur als Nummer mit «…» und einem Hinweis am Anfang.
- Bekannte Grenze: Sprungziele ausserhalb der ausgearbeiteten Stellen zeigen noch keinen Text. Vorschlag: eine gemeinfreie deutsche Übersetzung (z. B. Luther 1912) als Lesetext-Ersatz einbetten, bis eigene Übersetzungen vorliegen.

## v0.22 — 2026-10-13 — Schliessen-Knopf, Verse fortlaufend

- «Schliessen» (bzw. «Fertig» im Menü) mit Symbol, runder Fläche und Hover-Effekt; beim Öffnen eines Blatts erscheint kein Fokusrahmen mehr um den Knopf (der Fokus liegt auf dem Blatt).
- Neue Option «Verse fortlaufend»: Verse als Fliesstext hintereinander statt je auf einer eigenen Zeile; Lesarten- und Hintergrund-Hinweise fliessen mit. Standard aus.
- Schriften der Symbolknöpfe und Hinweise unabhängig von der Umgebung festgelegt.

## v0.21 — 2026-10-13 — Einheitliche Symbole in den Blättern

- Versblatt, Verstehen-Blatt und Hintergrund-Blatt enden jetzt mit «Abschnitt: …» und denselben Symbolen «Verstehen» und «Geschichte» wie beim Abschnittstitel, statt der alten Textlinks.
- Quellenangabe: MorphGNT ausdrücklich auf Mk 3,22–30 bezogen.

## v0.20 — 2026-10-13 — Ruhigerer Lesefluss, Wort-Info

- Unterstrichene Stellen (Tradition, Deutung) sind antippbar und öffnen ein Wort-Blatt: griechischer Wortlaut mit Umschrift und Anhören, Grundform, zugehörige Deutungen, wörtlichere Fassung, weitere Möglichkeiten, Begründung und die Wiedergabe in Luther 1912 und Elberfelder 1905. Dafür führen die Übersetzungsentscheidungen jetzt den griechischen Wortlaut (`grc`, vom Validator gegen den Vers geprüft); fünf Deutungen haben Fachwörter (`terms`) erhalten.
- Das «+» am Versende entfällt: Hat ein Vers Details, ist seine Versnummer umrandet und antippbar.
- «Diesen Abschnitt verstehen» und «Hintergrund damals» stehen nicht mehr unter dem Abschnitt, sondern als Symbole «Verstehen» und «Geschichte» beim Abschnittstitel.
- Hinweise «Damals» im Text sind kompakter (ein Symbol, Themen nebeneinander).
- Aramäisch wird zuverlässig über die Umschrift mit einer deutschen Stimme vorgelesen; Hebräisch ohne Vokalzeichen an die hebräische Stimme, sonst ebenfalls über die Umschrift.

## v0.19 — 2026-10-13 — Ursprungswörter zum Anhören

- Wunsch: Wo eine Erklärung sich auf ein griechisches, hebräisches oder aramäisches Wort bezieht, das Wort klein mit Aussprache und Anhören-Knopf zeigen.
- Neues Feld `terms` (Sprache, Originalschrift, Umschrift, Bedeutung) für 15 Hintergrundnotizen und eine Deutung, z. B. ὑποκριτής «Schauspieler, Heuchler», aram. אַבָּא abba, hebr. מָחָר machar. Validator prüft die Felder; Regel in AGENTS.md ergänzt.
- Griechische Einschübe in Erklärtexten erhalten automatisch Umschrift und Anhören-Knopf; ohne Urtext-Modus erscheint nur die Umschrift (statt wie bisher ausgeblendet zu werden).
- Hebräisch/Aramäisch wird mit einer hebräischen Gerätestimme gesprochen; fehlt sie, liest eine deutsche Stimme die Umschrift.

## v0.18 — 2026-10-13 — Übersetzungsentscheidungen sichtbar

- Frage: Wie stark beeinflussen bestehende Übersetzungen unsere Übersetzung? Antwort im Datenmodell: Übersetzungsentscheidungen (`decisions`) für Mt 6,9–13 und Lk 11,2–4, je als wörtlich, sprachlich angepasst, Deutungsentscheidung oder der vertrauten Wiedergabe folgend, mit wörtlicherer Fassung, weiteren Möglichkeiten und Begründung. Ausdrücklich vermerkt: «führe uns durch die Versuchung» gibt den Wortlaut nicht wieder (εἰς «hinein», μή verneint).
- Vergleich mit gemeinfreien älteren Übersetzungen: Lutherbibel 1912 und Elberfelder 1905, nur für die Vaterunser-Verse.
- Lesestrom: Versblatt mit «Wie ist übersetzt?» und «Ältere deutsche Übersetzungen»; im Urtext-Modus sind Stellen, die einer Tradition folgen (gepunktet) oder eine Deutung wählen (gestrichelt), im Text unterstrichen.
- Validator prüft Art und Zieltext der Entscheidungen; neuer Negativtest.

## v0.17 — 2026-10-13 — Umschrift, Anhören, neue Voreinstellungen

- Griechische Wörter zusätzlich in lateinischer Umschrift (nach dem Muster des SBL-Handbuchs, betonte Silbe markiert, z. B. πονηροῦ → ponēroú), abschaltbar im Menü.
- Anhören-Knopf bei griechischen Wörtern, Lesarten, Handschriftentexten und ganzen Versen (Stimmen des Geräts über die Web-Speech-Schnittstelle). Einstellungen: Aussprache Neugriechisch oder Schulaussprache (Umschrift, gelesen von einer deutschen Stimme), Stimmenauswahl, Tempo, Probe. Beides nähert die Aussprache des 1. Jahrhunderts nur an; ohne installierte Stimme erscheint ein Hinweis.
- Hebräisch: Sprachausgabe ist vorbereitet (he-IL); Umschrift folgt mit den ersten hebräischen Texten.
- Voreinstellung: «Andere Lesarten im Text», «Hintergrund im Text» und «Urtext und Details» sind jetzt eingeschaltet (gespeicherte ältere Einstellungen werden einmalig darauf umgestellt).
- Umschalten im Menü lässt die Leseposition stehen (der oberste sichtbare Eintrag bleibt an seiner Stelle; das Menü behält seine Scrollposition).

## v0.16 — 2026-10-12 — Das Vaterunser

- Wunsch: das Vaterunser komplett bearbeiten.
- Text: Matthäus und Lukas vollständig importiert (SBLGNT mit MACULA-Annotation; Apparat Mt 820/827, Lk 1133/1142 Stellen zugeordnet, Rest protokolliert; Gesichertheitsbewertung). Importer: Gross/Klein-Abweichung SBLGNT/MACULA wird wie eine Akzentabweichung protokolliert; Apparatüberschrift «Matthew» erkannt.
- Textzeugen: CNTR-Transkriptionen für Matthäus und Lukas, dazu 𝔓45, 𝔓75 und sieben Amulette bzw. Einzeltexte mit dem Vaterunser (3.–6. Jh.; Metadaten nach papyri.info/DCLP). Zuordnung zu den Lesarten für Mt 6,5–15 und Lk 11,1–4 (Abgleich mit dem SBLGNT-Apparat jeweils 18/18 bzw. 6/6).
- Studie Vaterunser (`STUDY-LP-0001`, KI-Entwürfe, ungeprüft): Texteinheiten Mt 6,5–15 (drei Teile) und Lk 11,1–4; deutsche Arbeitsübersetzung mit neun Alternativen (u. a. Lobpreis am Schluss, «vergeben haben/vergeben», kurze und lange Lukasfassung), je mit Wortbedeutungen und Entstehungserklärungen; vollständige Wortzuordnung Mt 6,9–13 und Lk 11,2–4; 6 Befunde, 7 Deutungen mit Gegenargumenten (u. a. drei Deutungen von ἐπιούσιος, Versuchung, «der Böse/das Böse», Vergebung), Grundsatz, Anwendung, 2 offene Fragen, 7 Beziehungen, 12 Hintergrundnotizen, 2 Kapitelzusammenfassungen. Autorenwerkzeug `scripts/authoring/vaterunser.py`.
- Lesestrom: trägt jetzt mehrere ausgearbeitete Stellen (neue Projektion `scripts/project_study.py`, Schlüssel nach Bibelstelle); Menü listet die ausgearbeiteten Stellen; Studienblatt zeigt Anwendung, Fragen und Beziehungen je Abschnitt; Textzeugen-Blatt mit Papyri und Amuletten.
- Tests erweitert (Vaterunser in Struktur- und Bedienungstest). Abschnittsebene hat jetzt 6705 statt 6704 Einträge, weil Mt 6 nach echten Einheiten gegliedert ist.

## v0.15 — 2026-10-12 — Lesarten bis zur Quelle

- Rückmeldung: Bei anderen Lesarten bis zur Quelle eintauchen können, auch übersetzt.
- Handschriften: Transkriptionen der sechs ältesten Handschriften des Markusevangeliums (01 א, 02 A, 03 B, 04 C, 05 D, 032 W) und fünf Ausgabentexte (WH, RP, Stephanus, KJTR, SR) aus dem Center for New Testament Restoration importiert (CC BY-SA 4.0, Commit fixiert, SHA-256). Neue Typen `witness`, `witness_transcription`, `witness_reading_set`; neue Ausgaben ED-ST, ED-KJTR, ED-SR; Kurzbeschreibungen (`about_de`) für alle Ausgaben.
- Maschinelle Zuordnung Handschrift → Lesart für die 28 Variantenstellen in Mk 3,20–35 (`scripts/collate_witnesses.py`, `METHOD-AUTO-COLLATION-V1`), Erstschrift und Korrektur getrennt. Selbstprüfung gegen den SBLGNT-Apparat: 50/52.
- Befund: Ephraemi (C) liest in 3,29 laut CNTR ἁμαρτίας, nicht κρίσεως wie in der Arbeitsnotiz `VAR-MRK-003-029-001`; die Arbeitsnotiz bleibt erhalten, die Abweichung wird angezeigt. In 3,20 widersprechen sich SBLGNT-Apparat und CNTR-Text bei Robinson-Pierpont.
- Übersetzungs-Alternativen um Wortbedeutungen der Lesarten und mögliche Entstehungserklärungen ergänzt (Revision protokolliert).
- Lesestrom: Blatt «Bis zur Quelle» je Lesart. Validator prüft die neuen Typen; DOM-Test erweitert.

## v0.14 — 2026-10-12 — Hintergrund damals

- Rückmeldung: Auf Versebene passt der Lesestrom, es fehlt der Hintergrund damals.
- Neuer Datentyp `background_note` (`data/background/`): 13 Notizen zu Mk 3,20–35 über Zeit, Ort, Kultur und Religion, je mit Kontext, Sicherheitsgrad, Unsicherheiten, Vergleichsstellen und ausserbiblischen Fundstellen (nur zitiert). Neuer Kontext `CTX-MARK-READERS-0070` (erste Leserschaft des Markus), neuer Tag `TAG-HISTORICAL-BACKGROUND`. KI-Entwürfe, fachlich ungeprüft.
- Lesestrom: «Damals» im Versblatt, «Hintergrund damals» je Abschnitt, optional kurze Hinweise im Text (Menü).
- Validator prüft Pflichtfelder und Kontextverweis der Hintergrundnotizen; zwei neue Negativtests; DOM-Test erweitert. 1131 Datensätze.

## v0.13 — 2026-10-12 — Lesestrom als Hauptrichtung, zugänglicher und ungestörter

- Vorgabe: Bibelstudium zugänglich für Personen ohne Griechisch und Hebräisch; ungestört lesen und «abtauchen in die Tiefe»; Hintergrund nur auf Wunsch ([VISION.md](docs/VISION.md)).
- Lesestrom neu aufgebaut (`app/reading-stream/template.html`): Vollbild ohne Geräterahmen, Leisten blenden beim Lesen aus, Verse fliessen als Text, keine technischen Zähler, ein Vertiefen-Link je Eintrag, deutsche Stellenangaben (3,20), Farben nach System, Einstellungen lokal gespeichert.
- Lesarten, Studieninhalte und Quellen als Blätter über dem Text; «+» nur an Versen mit abweichenden Lesarten. Urtext, Wort für Wort, Editionenvergleich und IDs nur im Modus «Urtext und Details»; optional «Andere Lesarten im Text zeigen». Griechische Einschübe in Erklärungen werden ohne diesen Modus ausgeblendet oder umschrieben (nur Darstellung).
- Neue Datentypen im freien Kern: `navigation_structure` (`data/navigation/NAV-PROT66-KJV.json`, Testkonfiguration) und `summary` (`data/summaries/`, 83 Entwürfe). Bisher lagen sie in der Vorlage; die Inhalte sind unverändert übernommen. Schema und Validator ergänzt (1116 Datensätze, PASS).
- `scripts/build_reading_stream.py` bettet Navigation, Zusammenfassungen und Markus-Projektion ein; DOM-Test an die neue Bedienung angepasst.
- Studienprototyp `app/prototype/` als abgelöst gekennzeichnet; `build_prototype.py` bleibt als Datenprojektion.
- Prüfungen: Validator, Validator-Negativtests, Struktur- und DOM-Test; Ansicht in Chromium in Handybreite, hell und dunkel. Keine Prüfung auf echten Geräten, keine fachliche Prüfung.

## v0.12 — 2026-10-11 — Markus im Lesestrom

- Pilotstudie Mk 3,20–35 im neuen Lesestrom: drei kanonische Abschnitte, 16 Arbeitsübersetzungen, sechs Alternativen, 249 Wörter und 28 Variantenstellen.
- Aufklappbare Wortdetails, Quellenvergleich und getrennte Studienebenen mit Gegenargumenten, Prüfstatus, Bewertungsgrenzen und Attribution. Direkteinstieg im Menü und bei Markus.
- Reproduzierbarer Build aus bestehender Datenprojektion; kanonische Daten unverändert. Struktur-, Daten- und DOM-Interaktionstests erfolgreich; visuelle Geräteprüfung ausstehend.

## v0.11 — 2026-10-11 — Fortlaufender Lesetiefe-Prototyp

- Separater, eigenständig lauffähiger Entwurf `app/reading-stream/index.html`: auf jeder Ebene scrollend lesen, an interessanten Einträgen vertiefen und zur Leseposition zurückkehren.
- Vollständiges 66-Bücher-Mengengerüst mit 1’189 Kapiteln, 6’704 ausdrücklich technischen Testblöcken und 31’102 Verspositionen; 66 deutsche KI-Buchzusammenfassungen als ungeprüfter Entwurf.
- Mobile-/Tablet-Ansichten, neutrales Hell/Dunkel, Stellensuche, DE/EN-Oberfläche, Textgrösse und eigene Auswahlfelder. Kompaktes SVG-Logo mit gedrehtem B und zwei Quadraten.
- Datenquelle und Grenzen dokumentiert; numerische Kapitel-/Versstruktur unabhängig aus eBible-USFM nachgezählt. Keine neuen kanonischen Text- oder Studiendaten, bestehender Markus-Prototyp unverändert.
- Strukturprüfung mit Node.js ohne Zusatzpakete; DOM-Prüfungen im Arbeitslauf. Visuelle Prüfung auf echten Geräten steht aus.

## v0.10 — 2026-10-09 — Prototyp für allgemeine Leser

- Prototyp nach Rückmeldung neu gestaltet: einfacher und allgemeiner, schlicht, hell/dunkel, mit gezeichnetem Überblicksbild. Drei Wege (Überblick, Lesen, Vertiefen) über eine untere Leiste; Studienpfad; Einstellungen für Lesarten, Urtext-Modus, Schriftgrösse und Farben.
- Abweichende Lesarten: nur Stellen, die die deutsche Übersetzung verändern (6 in Mk 3,20–35), auf Wunsch eingeblendet; Erklärung in einfacher Sprache mit Bezeugung («Steht in 4 von 5 wichtigen Textausgaben»), ohne Entscheidung über richtig/falsch.
- Urtext, Wort für Wort, Grammatik und alle 28 Apparatstellen nur im Modus «Urtext und Details».
- Neue Daten (KI-Entwurf): `alternatives` in den Übersetzungen (deutsche Wiedergabe abweichender Lesarten mit Wirkung «bedeutsam»/«gering»), `summary_de` für die Texteinheiten 3,20–35. Validator prüft, dass jede Alternative auf eine vorhandene Lesart zeigt und ihr Ausgangstext in der Übersetzung vorkommt.

## v0.9 — 2026-10-09 — Studienprototyp Mk 3,20–35

- Klickbarer Prototyp `app/prototype/mk3-20-35.html`, erzeugt mit `scripts/build_prototype.py` aus den Daten des freien Kerns (keine eigenen Inhalte im Prototyp): Zoomstufen Buch → Abschnitt → Einheit → Vers → Wort; Textschichten Deutsch, Griechisch, Wort für Wort; Variantenstellen mit Editionen und Gesichertheitsstufe samt Grenzen der Methode; Wortdetails (Grundform, Häufigkeit in Markus, Form, Satzrolle, Bezug, deutsche Entsprechung, Glossen, Vergleich MACULA/MorphGNT); Kette Befund → Deutung → Prinzip → Anwendung; Studienpfad in sechs Schritten; hell und dunkel, für Smartphones ausgelegt.
- Neue Daten (KI-Entwürfe, ungeprüft): Texteinheiten 3,20–21, 3,31–35 und Abschnitt 3,20–35; Befund FIND-MRK-0005 zur Verschachtelung; Deutung INT-MRK-0003 mit Vorbehalt und Gegenargument; deutsche Arbeitsübersetzung 3,20–21 und 3,31–35 (Wortzuordnung folgt).
- Validator prüft auch `parts` von Texteinheiten.

## v0.8 — 2026-10-09 — Ganzes Markusevangelium, Gesichertheitsbewertung, Lizenzschichten

- Lizenzmodell: eigene Inhalte CC0; freier Kern `data/` (gemeinfrei, CC0, CC BY, CC BY-SA) und Studienschicht `data-nc/` für nicht kommerzielle Quellen, strikt getrennt; Betreiber gemeinnütziger Verein ([LIZENZEN.md](LIZENZEN.md)).
- Text und Annotation getrennt: Token-Sets enthalten nur die Wörter der Edition; sprachliche Angaben liegen als eigene Annotationsschichten daneben.
- Ganzes Markusevangelium importiert: SBLGNT-Text (Faithlife/SBLGNT, Commit `c4d241a9c1c4`, CC BY 4.0) mit 11 286 Wörtern; MACULA Greek (Commit `8423afe47b9e`, CC BY 4.0) als Annotation (Lemma, Morphologie, Syntaxrolle, Referenten, Glossen). MARBLE-Wortbedeutungen bewusst nicht übernommen (nur «used with permission»). Neuer Importer `scripts/import_sblgnt_book.py`.
- Pilot-Token-Set Mk 3,22–30 migriert (`scripts/migrations/v0_8.py`): gleiche Token-IDs jetzt im Kapitel-Set, MorphGNT-Werte unverändert als eigene Schicht, alter Datensatz als `deprecated` erhalten. Zeichen «text»/«word» kommen jetzt aus der Edition (Elision ʼ statt ’ bei MorphGNT); Quellenangaben im Alignment entsprechend neu erzeugt.
- SBLGNT-Apparat für ganz Markus: 929 von 930 Einträgen an Tokens gebunden (neu: Siglen Holmes, Greeven, ⟦WH⟧; mehrere Auslassungen «…»; Markierungen ⸁ und ⸄⸅); 1 versübergreifender Eintrag (7,21–22) bewusst nicht importiert und protokolliert. Die 10 Pilotstellen sind inhaltlich unverändert (jetzt in `data/variants/sblgntapp-mrk/`).
- Gesichertheitsbewertung als Datentyp (`assessment_set`, `assessment_method`) mit Methode «Übereinstimmung der Editionen» und offengelegten Grenzen; für alle 929 Stellen berechnet ([GESICHERTHEIT.md](docs/GESICHERTHEIT.md)).
- Validator prüft zusätzlich Annotationen (Referenten nur als Token-IDs), Bewertungen und die Trennung Kern/Studienschicht; neue Negativtests `scripts/test_validate.py`.
- Unabhängiges Gegenlesen durch einen separaten KI-Durchgang (alle Tokens, alle MACULA-Zeilen, alle 929 Stellen und Bewertungen nachgerechnet). Korrigiert: MACULA-Platzhalter für «kein Referent» nicht mehr als Verweis gespeichert (jetzt `…_unresolved`), MACULA-IDs im Feld `frame` in Token-IDs umgesetzt, Lesarttexte behalten das Elisionszeichen der Edition (ʼ), Lesarten ohne gezählte Edition gekennzeichnet (`no_counted_edition`), Pfad in LIZENZEN.md, Autor der Cherith-Glossen, Migrationsprotokoll um neu erzeugte Änderungen ergänzt.

## 2026-10-09 — Vision und Lizenz

- Vision in vier Stufen festgehalten ([VISION.md](docs/VISION.md)): transparente Textbasis mit Gesichertheitsbewertung statt Lektorat; Übertragung in heutige Zeit, Kultur und Sprachen; Zoomstufen und Studienanleitung; Visualisierung (u. a. Raumobjekte), UX und Beiträge Dritter. Vorgaben und abgeleitete Vorschläge getrennt.
- Lizenz festgelegt: eigene Inhalte CC0 1.0 ([LICENSE](LICENSE)); Fremddaten mit Lizenz in [LIZENZEN.md](LIZENZEN.md); im Kern nur gemeinfreie, CC0- und CC-BY-Quellen.
- Folgerung: MorphGNT-Annotation (CC BY-SA) soll durch eine CC-BY-Annotation ersetzt werden; nicht kommerzielle Datensätze werden nicht übernommen.
- AGENTS.md um Lizenzgrundsatz und «Gesichertheit statt Lektorat» ergänzt.

## 2026-10-09 — Quellenlandschaft für die ganze Bibel

- [QUELLEN.md](docs/QUELLEN.md) auf die ganze Bibel erweitert: AT hebräisch/aramäisch, Septuaginta, NT, alte Übersetzungen, Kirchenväter, Lexika, Kontext; Lizenzen und Zugang je Quelle mit Links.
- Neu: beantragbare Zugänge (INTF, Deutsche Bibelgesellschaft, CATSS, TLG, Brill, Brepols, ETCBC u. a.), Abdeckungsmatrix «nur offene Quellen» und offene Entscheidung zur kommerziellen Nutzung.
- Recherche über die Websites der Anbieter; nicht an Primärquellen bestätigte Angaben sind als [ungeprüft] markiert.

## v0.7 — 2026-10-09 — Varianten auf Editionsebene, vollständige Arbeitsübersetzung

- Quellenlandschaft dokumentiert: [QUELLEN.md](docs/QUELLEN.md) mit Rechte-Ampel und empfohlener Reihenfolge.
- SBLGNT-Apparat (Faithlife/SBLGNT, CC BY 4.0, Commit `c4d241a9c1c4`) für Mk 3,22–30 importiert: 10 Variantenstellen in 3,25–29 mit Lesarten von Westcott-Hort, Tregelles, NA28 und Robinson-Pierpont, als `evidence_level: edition_apparatus` getrennt von Handschriftenbelegen. Neuer Importer `scripts/import_sblgnt_apparatus.py` bindet jede Stelle über die SBLGNT-Markierungen ⸀/⸂⸃ an Token-IDs und prüft die Wortgleichheit.
- Editionsdatensätze für WH, Tregelles, NA28 und Robinson-Pierpont; Quellendatensatz für den Apparat.
- Bestehende Varianten und das Alignment zu Mk 3,29 additiv an Token-IDs gebunden (`scripts/migrations/v0_7.py`, Protokoll in `provenance/migrations/2026-10-09-v0.7.json`).
- Eigene wörtlich orientierte Arbeitsübersetzung Mk 3,22–30 und vollständige Wortzuordnung aller 140 Tokens mit Grammatik- und Alternativnotizen (KI-Entwurf, `draft`); 3,29 unverändert aus der bisherigen Arbeitsübersetzung übernommen. Erzeugt mit `scripts/authoring/mk3_22_30_translation.py`.
- Gegenlesen durch einen separaten KI-Durchgang: drei Fehler korrigiert (3,26 Aorist jetzt «gespalten worden ist»; Notiz zu εἰσελθών; Apparatlesarten nicht mehr pauschal als Ersetzung klassifiziert), mehrere Präzisierungen übernommen (u. a. 3,27 «hineingehen … plündern … plündern»). Keine fachliche Prüfung durch eine Person.
- Validator prüft zusätzlich Token-IDs, Editionen in Lesarten, weitere Verweisfelder und bei `coverage: complete` die lückenlose Zuordnung sowie das Vorkommen jedes Zieltexts in der Übersetzung.
- Pilotstudie führt die neuen Ergebnisse in `outputs`.
- Offen: Zeugenangabe Ephraemi (C) in `VAR-MRK-003-029-001` prüfen; kein automatischer Test für den Apparat-Importer.

## v0.6 — 2026-10-09 — Bibelstellen vereinheitlicht, griechischer Text importiert

- Kanonische Bibelstellen eingeführt (`MRK.3.29`, `MRK.3.22-MRK.3.30`, USFM-Buchcodes) mit Dokumentation [BIBELSTELLEN.md](docs/BIBELSTELLEN.md) und Werkzeug `scripts/refs.py` (Prüfung, Umwandlung deutscher/englischer Eingaben, deutsche Anzeige).
- Bestehende Daten per `scripts/migrations/v0_6.py` migriert: Bibelstellen, Typnamen `study`/`text_unit`, Tippfehler in einem Statuswert, fehlende `outputs` der Pilotstudie. 12 Änderungen protokolliert in `provenance/migrations/2026-10-09-v0.6.json`; Aussagen, Status, Konfidenz und IDs unverändert.
- Schema auf alle Typen und Statuswerte erweitert; Validator prüft jetzt Schema, Verweise zwischen Datensätzen, Lesarten und Bibelstellen.
- Importer korrigiert: MorphGNT-Referenzen haben die Form `0203xx` (Markus = 02), nicht `6203xx`. Quelle, Upstream-Commit, SHA-256, Lizenzangaben und Importdatum werden im Datensatz festgehalten; Import ohne Commit wird abgelehnt.
- Mk 3,22–30 aus MorphGNT SBLGNT 6.12 (Commit `a2afca0e96e3`) importiert: 140 Tokens, 91 Wortformen, 64 Lemmata (`imported_unreviewed`). Zählungen unabhängig gegen die Quelldatei nachgezählt.
- Arbeitstranskription Mk 3,29–30 mit SBLGNT abgeglichen: eine Abweichung (`ἀλλ’`/`ἀλλὰ`).
- Grenzen: keine typspezifischen Schemas, keine Versifikationsprüfung, keine fachliche Prüfung der Morphologie; Lizenzangaben vor Veröffentlichung klären.

## 2026-10-08 — Dokumentation vereinheitlicht

- Eine zentrale README.md für Projektüberblick, Einstieg und vorhandene Programme.
- Versionsnotizen aus den bisherigen READMEs in diesem Changelog zusammengeführt.
- README-v0.3.md, README-v0.4.md, README-v0.5.md und docs/README-original-v0.5.md aus dem aktuellen Dateibaum entfernt.
- Verweise und Herkunftsinventar angepasst. Historische Originaldateien bleiben in Git und den unveränderten ZIP-Paketen erhalten.

## 2026-10-08 — Repository konsolidiert

- Die fünf Paketstände v0.1–v0.5 als einzelne Archiv-Commits übernommen.
- Originalpakete mit SHA-256-Prüfsummen und Dateiinventar archiviert.
- Konzept, Datenmodell, Metadaten, Arbeitsprozess, Entscheidungen, Übersetzungsmethoden und Roadmap dokumentiert.
- Arbeitsregeln für KI-Unterstützung in AGENTS.md ergänzt.
- 36 Datensätze einschliesslich 6 Tags gesichert; bestehende ID-/Tag-Prüfung und synthetische Importtests erfolgreich ausgeführt.
- Grenzen dokumentiert: keine vollständige JSON-Schema-Validierung, noch keine SQLite-Projektion oder Benutzer-App, fehlende Primärquellenprüfung und vollständige Tokenbestände.

## v0.5 — Varianten und Übersetzungszuordnung

- Zweite Variantenstelle zu Mk 3,29 ergänzt: ἐστιν / ἔσται.
- Redaktionelle Entscheidung mit bevorzugter Lesart, Alternative, Begründung, Quellen und Sicherheitsgrad ergänzt.
- Eigene deutsche Arbeitsübersetzung von Mk 3,29 und erste griechisch-deutsche Wort-/Phrasenzuordnungen aufgenommen.
- Bestehenden v0.4-Bestand beibehalten; insgesamt 36 Datensätze einschliesslich 6 Tags.
- Zeugenangaben laut damaligem Arbeitsstand anhand einer Sekundärtranskription verglichen; keine eigene Prüfung von Handschriftenbildern und keine vollständige Kollation der Perikope.
- Griechischer Beispieltext weiterhin Arbeitstranskription, Alignments unvollständig, keine verifizierten Gesamtzahlen für Token oder Lemmata. Die Lesartpräferenz bleibt eine revidierbare Entscheidung.

Quellenhinweise aus den Versionsnotizen:
- https://github.com/morphgnt/sblgnt
- https://www.greeklab.org/interlinear.php?book=Mark&cap=3&verse=29
- https://tips.translation.bible/tip_source/bratcher-nida-1961/page/84/

## v0.4 — Importvorbereitung verbessert

- Erzeugte Token- und Zähldatensätze mit `id`, `type`, `status` und `tags` versehen, damit der vorhandene Validator sie lesen kann.
- Ablehnung fehlerhafter Zielzeilen und unvollständiger Versabdeckung ergänzt; Eingabedatei mit SHA-256 dokumentiert.
- Synthetische Importtests für vollständige und unvollständige Eingaben ergänzt.
- Ablauf festgehalten: konkrete Quelldatei und Upstream-Commit dokumentieren, importieren, validieren und Text/Morphologie an der benannten Edition prüfen.
- Kein echter Quelltext mitgeliefert; keine belastbaren Wortzahlen für Mk 3,22–30 veröffentlicht.

## v0.3 — Editionsgebundener Import vorbereitet

- Editionsobjekt für SBLGNT und Quellenhinweis auf MorphGNT SBLGNT Edition 6.12 ergänzt.
- Importer für eine lokal bereitgestellte MorphGNT-Datei zur Perikope Mk 3,22–30 hinzugefügt; Ausgabe in `data/tokens/` und `data/counts/` vorgesehen.
- Importvorbereitung auf sieben durch Leerzeichen getrennte Spalten und den im Skript erwarteten Referenzcode ausgerichtet. Der Abgleich mit einer tatsächlichen versionierten Quelldatei blieb offen.
- Vollständiger Quellimport, Primärprüfung der Lesarten und Übersetzungsalignment noch ausstehend.

Quellen und Attribution aus den damaligen Notizen: SBL Greek New Testament, herausgegeben von Michael W. Holmes, © Society of Biblical Literature und Logos Bible Software; dort als CC BY 4.0 bezeichnet. MorphGNT SBLGNT Edition 6.12, J. K. Tauber; Morphologie/Lemmatisierung dort als CC BY-SA bezeichnet. Diese übernommenen Angaben ersetzen keine Prüfung der Bedingungen der konkret importierten Fassung.
- https://github.com/Faithlife/SBLGNT
- https://github.com/morphgnt/sblgnt

## v0.2 — Pilotstudie erweitert

- Ersten Studienbericht zu Markus 3,22–30 ergänzt.
- Quellenhinweise, vorläufige Variantenstelle Sünde/Gericht, zusätzliche Befunde, Parallelstellen und eine offene Forschungsfrage aufgenommen.
- Arbeitstranskription von Mk 3,29–30 und ausdrücklich nicht verifizierte Leerzeichenzählungen für diese zwei Verse ergänzt; keine Lemmazählung.
- Insgesamt 30 Datensätze einschliesslich 6 Tags.

## v0.1 — Strukturierter Wissensfundus angelegt

- Pilot Markus 3,22–30 mit Werk, natürlicher Texteinheit, Studie, Befunden, alternativen Interpretationen, Prinzip und kontextabhängiger Anwendung angelegt.
- Historischen Kontext und heutige Anwendung CH/de-CH 2026 getrennt; Themen und 6 kontrollierte Tags eingeführt.
- Stabile IDs, Tag-Referenzen, frühe Wissenszeit-/Vorgängerfelder, generisches Schema und einfachen Validator angelegt; insgesamt 19 Datensätze einschliesslich Tags.
- Git als massgebliche Quelle festgehalten; SQLite als spätere abgeleitete Projektion vorgesehen.
- Fachliche Aussagen als vorläufig markiert; geprüfte Textbestände, genaue Quellenbelege und Argument-/Evidenzobjekte als nächste Arbeiten festgehalten.
