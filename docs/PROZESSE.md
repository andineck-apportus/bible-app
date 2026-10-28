# Prozesse

Versionierte Beschreibung, wie gearbeitet wird. Erzeugt aus `scripts/authoring/prozesse.py` (Daten: `data/processes/`);
in der App unter Einstellungen → Prozesse als Ablauf dargestellt. Inhalte verweisen auf die Fassung, nach der sie entstanden sind;
frühere Fassungen bleiben abrufbar.

Rollen: **Bearbeitende Instanz**; **Weitere Instanz (prüft)**; **Werkzeug (feste Prüfung)**; **Bildmodell**; **Herausgeber**.

## Quellen und Urtext (`PROC-QUELLEN`)

Nur Quellen verwenden, deren Recht geklärt ist, und den Urtext nachvollziehbar übernehmen.

### Fassung 1.1 – gültig ab 2026-10-13 (aktuell)

*Änderung:* Quellenkatalog mit Abgleich im Validator; Anfragen an Rechteinhaber protokolliert.

1. **Quelle finden** (Bearbeitende Instanz): Editionen, Handschriften, Übersetzungen und Hilfsmittel für den Abschnitt suchen; Fassung, Fundort und Nutzungsbedingungen festhalten.
2. **Recht prüfen** (Bearbeitende Instanz): Nutzungsrecht bestimmen: gemeinfrei, CC0, CC BY, CC BY-SA in den freien Kern; nicht kommerzielle Quellen nur in die Studienschicht; geschützte Quellen nur nennen.
3. **Katalog abgleichen** (Werkzeug (feste Prüfung)): Der Validator prüft, dass jede Herkunftsadresse im Katalog steht und verwendete Quellen auf vorhandene Dateien zeigen. Prüft: Herkunft im Katalog, Schichten nicht vermischt. Zurück zu «Recht prüfen», wenn Herkunft fehlt oder Schicht falsch.
4. **Urtext übernehmen** (Bearbeitende Instanz): Edition und Datenversion festlegen, Originaldatei mit Prüfsumme nachweisen, Wörter (Token) mit Morphologie übernehmen.
5. **Vollständigkeit prüfen** (Werkzeug (feste Prüfung)): Versumfang, Verszählung und Wort-IDs gegen die Edition prüfen. Prüft: alle Verse vorhanden, Zählung nach Versifikation. Zurück zu «Urtext übernehmen», wenn Lücke oder Zählfehler.
6. **Anfragen** (Herausgeber): Bei Quellen mit unklarem Recht fragt der Herausgeber beim Rechteinhaber an; Anfrage und Antwort werden protokolliert.

*Weiter, wenn:* Quelle im Katalog, Recht geklärt, Text vollständig und geprüft.
*Ausführlich:* LIZENZEN.md, docs/QUELLEN.md, docs/ANFRAGEN.md

### Fassung 1.0 – gültig ab 2026-10-09

*Änderung:* Lizenzschichten: freier Kern und Studienschicht getrennt.

1. **Quelle finden** (Bearbeitende Instanz): Editionen, Handschriften, Übersetzungen und Hilfsmittel für den Abschnitt suchen; Fassung, Fundort und Nutzungsbedingungen festhalten.
2. **Recht prüfen** (Bearbeitende Instanz): Nutzungsrecht bestimmen: gemeinfrei, CC0, CC BY, CC BY-SA in den freien Kern; nicht kommerzielle Quellen nur in die Studienschicht; geschützte Quellen nur nennen.
3. **Urtext übernehmen** (Bearbeitende Instanz): Edition und Datenversion festlegen, Originaldatei mit Prüfsumme nachweisen, Wörter (Token) mit Morphologie übernehmen.
4. **Vollständigkeit prüfen** (Werkzeug (feste Prüfung)): Versumfang, Verszählung und Wort-IDs gegen die Edition prüfen. Prüft: alle Verse vorhanden, Zählung nach Versifikation. Zurück zu «Urtext übernehmen», wenn Lücke oder Zählfehler.

*Weiter, wenn:* Quelle mit geklärtem Recht und vollständiger, geprüfter Text.
*Ausführlich:* LIZENZEN.md, docs/QUELLEN.md

## Lesarten (Textkritik) (`PROC-LESARTEN`)

Zeigen, wo alte Handschriften voneinander abweichen, mit Zeugen, ohne zu entscheiden, was richtig ist.

### Fassung 1.0 – gültig ab 2026-10-09 (aktuell)

*Änderung:* Erste Fassung.

1. **Zeugen vergleichen** (Werkzeug (feste Prüfung)): Handschriften und Textausgaben Wort für Wort vergleichen (Kollation); Abweichungen als Lesarten mit ihren Zeugen erfassen.
2. **Lesarten ordnen** (Bearbeitende Instanz): Lesarten zu Variationsstellen zusammenfassen; Belegarten trennen (Handschrift, Apparat, Sekundärtranskription).
3. **Textgrundlage festhalten** (Bearbeitende Instanz): Die Lesart, der die Übersetzung folgt, als begründete, revidierbare Entscheidung mit Alternativen ablegen – keine Entscheidung über «richtig».
4. **Gegenprüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft Zeugenangaben und Zuordnung gegen die Quellen. Prüft: Zeugen stimmen, Belegart richtig. Zurück zu «Lesarten ordnen», wenn Abweichung.
5. **Validator** (Werkzeug (feste Prüfung)): Verweise auf Lesarten, Zeugen und Wort-IDs prüfen. Prüft: alle Verweise gültig.

*Weiter, wenn:* Alle Lesarten mit Zeugen, Textgrundlage begründet.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.
*Ausführlich:* docs/GESICHERTHEIT.md

## Übersetzung aus dem Urtext (`PROC-UEBERSETZUNG`)

Eine eigene, nachvollziehbare Übersetzung aus dem Urtext: treu, verständlich, mit offengelegten Entscheiden.

### Fassung 1.2 – gültig ab 2026-10-24 (aktuell)

*Änderung:* Wendungen, die heute gegen ihren Sinn wirken, gibt der Lesetext dem Sinn nach wieder; die wörtliche Fassung bleibt als Alternative (z. B. Mt 5,37).

1. **Übersetzen** (Bearbeitende Instanz): Aus dem Urtext (Griechisch, Hebräisch) übersetzen, wörtlich orientiert in verständlichem Deutsch; Grundentscheide des Buchs einhalten (Schlüsselwörter, Erzählzeit).
2. **Wörter zuordnen** (Bearbeitende Instanz): Jedes deutsche Wort den Wörtern des Urtexts zuordnen (Wortzuordnung).
3. **Entscheide festhalten** (Bearbeitende Instanz): Wo die Übersetzung glättet, deutet oder einer Tradition folgt, Entscheid mit Begründung und Alternative festhalten. Wirkt eine wörtliche Wendung heute gegen ihren Sinn, gibt der Lesetext den Sinn wieder; die wörtliche Fassung steht als Alternative.
4. **Inhalt prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den Urtext: Bedeutung, Zeitform, Satzart, Handelnde, Wer-zu-wem. Prüft: treu zum Urtext, nichts ergänzt, nichts weggelassen. Zurück zu «Übersetzen», wenn Abweichung vom Urtext.
5. **Sprache prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft Grammatik, Schweizer Rechtschreibung, heutigen Ausdruck und Lesefluss; geglättet wird nur, soweit Bedeutung, Zeitform, Satzart und Wortzuordnung erhalten bleiben. Prüft: Grammatik und Rechtschreibung, keine steifen oder wörtlich übertragenen Wendungen. Zurück zu «Übersetzen», wenn sprachlicher Mangel.
6. **Validator** (Werkzeug (feste Prüfung)): Wortzuordnung, Verse und Verweise prüfen. Prüft: jedes Wort zugeordnet, Verse vollständig.

*Weiter, wenn:* Lesetext inhaltlich und sprachlich geprüft, Wortzuordnung vollständig.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.
*Ausführlich:* docs/ENTSCHEIDUNGEN.md

### Fassung 1.1 – gültig ab 2026-10-13

*Änderung:* Sprachliche Prüfung als eigener Schritt nach der inhaltlichen.

1. **Übersetzen** (Bearbeitende Instanz): Aus dem Urtext (Griechisch, Hebräisch) übersetzen, wörtlich orientiert in verständlichem Deutsch; Grundentscheide des Buchs einhalten (Schlüsselwörter, Erzählzeit).
2. **Wörter zuordnen** (Bearbeitende Instanz): Jedes deutsche Wort den Wörtern des Urtexts zuordnen (Wortzuordnung).
3. **Entscheide festhalten** (Bearbeitende Instanz): Wo die Übersetzung glättet, deutet oder einer Tradition folgt, Entscheid mit Begründung und Alternative festhalten.
4. **Inhalt prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den Urtext: Bedeutung, Zeitform, Satzart, Handelnde, Wer-zu-wem. Prüft: treu zum Urtext, nichts ergänzt, nichts weggelassen. Zurück zu «Übersetzen», wenn Abweichung vom Urtext.
5. **Sprache prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft Grammatik, Schweizer Rechtschreibung, heutigen Ausdruck und Lesefluss; geglättet wird nur, soweit Bedeutung, Zeitform, Satzart und Wortzuordnung erhalten bleiben. Prüft: Grammatik und Rechtschreibung, keine steifen oder wörtlich übertragenen Wendungen. Zurück zu «Übersetzen», wenn sprachlicher Mangel.
6. **Validator** (Werkzeug (feste Prüfung)): Wortzuordnung, Verse und Verweise prüfen. Prüft: jedes Wort zugeordnet, Verse vollständig.

*Weiter, wenn:* Lesetext inhaltlich und sprachlich geprüft, Wortzuordnung vollständig.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.

### Fassung 1.0 – gültig ab 2026-10-09

*Änderung:* Erste Fassung: Übersetzung mit Wortzuordnung und Entscheiden, inhaltliche Prüfung.

1. **Übersetzen** (Bearbeitende Instanz): Aus dem Urtext (Griechisch, Hebräisch) übersetzen, wörtlich orientiert in verständlichem Deutsch; Grundentscheide des Buchs einhalten (Schlüsselwörter, Erzählzeit).
2. **Wörter zuordnen** (Bearbeitende Instanz): Jedes deutsche Wort den Wörtern des Urtexts zuordnen (Wortzuordnung).
3. **Entscheide festhalten** (Bearbeitende Instanz): Wo die Übersetzung glättet, deutet oder einer Tradition folgt, Entscheid mit Begründung und Alternative festhalten. Wirkt eine wörtliche Wendung heute gegen ihren Sinn, gibt der Lesetext den Sinn wieder; die wörtliche Fassung steht als Alternative.
4. **Inhalt prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den Urtext: Bedeutung, Zeitform, Satzart, Handelnde, Wer-zu-wem. Prüft: treu zum Urtext, nichts ergänzt, nichts weggelassen. Zurück zu «Übersetzen», wenn Abweichung vom Urtext.
5. **Validator** (Werkzeug (feste Prüfung)): Wortzuordnung, Verse und Verweise prüfen. Prüft: jedes Wort zugeordnet, Verse vollständig.

*Weiter, wenn:* Lesetext geprüft, Wortzuordnung vollständig.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.

## Weitere Sprachen und Mundarten (`PROC-MUNDART`)

Jede Sprache und Mundart eigenständig aus dem Urtext, nicht aus dem Hochdeutschen abgeleitet.

### Fassung 1.0 – gültig ab 2026-10-13 (aktuell)

*Änderung:* Erste Fassung (Züridüütsch).

1. **Aus dem Urtext übersetzen** (Bearbeitende Instanz): Jede Sprach- oder Mundartfassung entsteht als eigene Schicht direkt aus dem Urtext, mit Wortzuordnung; die hochdeutsche Fassung dient nur zur Kontrolle.
2. **Schicht beschreiben** (Bearbeitende Instanz): Sprache, Zielgruppe, Schreibweise (z. B. Züridüütsch nach Dieth) und Ton festhalten; Entscheide wie bei der Übersetzung.
3. **Inhalt prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz vergleicht mit dem Urtext und der Kontrollübersetzung. Prüft: treu zum Urtext. Zurück zu «Aus dem Urtext übersetzen», wenn Abweichung.
4. **Sprache prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft Schreibweise, Wortwahl und Lesefluss der Mundart. Prüft: festgelegte Schreibweise, idiomatisch. Zurück zu «Aus dem Urtext übersetzen», wenn Mangel.
5. **Muttersprachlich prüfen** (Herausgeber): Eine Person mit dieser Muttersprache liest gegen; erst dann wird die Prüfung eingetragen.

*Weiter, wenn:* Inhaltlich und sprachlich geprüft; muttersprachliche Prüfung vorgesehen.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.

## Befunde, Deutungen, Hintergrund (`PROC-STUDIE`)

Was dasteht, wie man es verstehen kann und was damals galt – sauber getrennt und belegt.

### Fassung 1.1 – gültig ab 2026-10-18 (aktuell)

*Änderung:* Antike Quellen werden am Text nachgeschlagen; Ergebnis als Prüfvermerk bei jeder Notiz.

1. **Befunde** (Bearbeitende Instanz): Was im Text steht: Wortbedeutung, Grammatik, Aufbau, wiederkehrende Begriffe – getrennt von jeder Deutung.
2. **Deutungen** (Bearbeitende Instanz): Wie man den Text verstehen kann: mehrere begründbare Verständnisse mit Befunden, Gegenargumenten und Gesichertheit; keine Entscheidung über richtig oder falsch.
3. **Hintergrund damals** (Bearbeitende Instanz): Zeit, Ort, Kultur und Sprachgebrauch der Adressaten mit antiken Quellen.
4. **Quellen nachschlagen** (Weitere Instanz (prüft)): Eine weitere Instanz schlägt jede antike Quelle in frei zugänglichen Ausgaben nach: bestätigt, berichtigt, teilweise oder nicht prüfbar. Was sich nicht belegen lässt, wird abgeschwächt oder gestrichen. Prüft: Stelle sagt, was die Notiz behauptet. Zurück zu «Hintergrund damals», wenn Angabe falsch oder nicht belegt.
5. **Gegen den Text prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft Befunde und Deutungen gegen den Text und auf Trennung der Ebenen. Prüft: Befund ≠ Deutung, Alternativen sichtbar. Zurück zu «Befunde», wenn Vermischung oder Fehler.
6. **Validator** (Werkzeug (feste Prüfung)): Stellenmarken, Verweise und Ursprachwörter prüfen. Prüft: Stellen gültig, Ursprachwörter erfasst.

*Weiter, wenn:* Ebenen getrennt, Quellen nachgeschlagen, gegen den Text geprüft.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.
*Ausführlich:* docs/QUELLENPRUEFUNG.md, docs/GESICHERTHEIT.md

### Fassung 1.0 – gültig ab 2026-10-12

*Änderung:* Erste Fassung.

1. **Befunde** (Bearbeitende Instanz): Was im Text steht: Wortbedeutung, Grammatik, Aufbau, wiederkehrende Begriffe – getrennt von jeder Deutung.
2. **Deutungen** (Bearbeitende Instanz): Wie man den Text verstehen kann: mehrere begründbare Verständnisse mit Befunden, Gegenargumenten und Gesichertheit; keine Entscheidung über richtig oder falsch.
3. **Hintergrund damals** (Bearbeitende Instanz): Zeit, Ort, Kultur und Sprachgebrauch der Adressaten mit antiken Quellen.
4. **Gegen den Text prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft Befunde und Deutungen gegen den Text und auf Trennung der Ebenen. Prüft: Befund ≠ Deutung, Alternativen sichtbar. Zurück zu «Befunde», wenn Vermischung oder Fehler.
5. **Validator** (Werkzeug (feste Prüfung)): Stellenmarken, Verweise und Ursprachwörter prüfen. Prüft: Stellen gültig, Ursprachwörter erfasst.

*Weiter, wenn:* Ebenen getrennt, gegen den Text geprüft.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.
*Ausführlich:* docs/GESICHERTHEIT.md

## Damals → Prinzip → Heute (`PROC-DAMALS-HEUTE`)

Den Text treu lassen und daneben gekennzeichnet übertragen.

### Fassung 1.0 – gültig ab 2026-10-23 (aktuell)

*Änderung:* Erste Fassung.

1. **Damals** (Bearbeitende Instanz): Hintergrund der ersten Leser: Situation, Sitte, Bedeutung damals.
2. **Prinzip** (Bearbeitende Instanz): Den Grundsatz ableiten, der über die damalige Situation hinaus gilt, mit Begründung.
3. **Heute** (Bearbeitende Instanz): Anwendung je Zielgruppe mit Grenze. Heutiges steht nie im Bibeltext, in Zusammenfassung oder Bild.
4. **Prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft die Herleitung Damals → Prinzip → Heute und die Kennzeichnung. Prüft: Text bleibt treu, Stufen gekennzeichnet. Zurück zu «Prinzip», wenn Herleitung trägt nicht.

*Weiter, wenn:* Drei Stufen getrennt und geprüft.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.
*Ausführlich:* docs/DAMALS-PRINZIP-HEUTE.md

## Kernanalyse und Zusammenfassungen (`PROC-VERDICHTUNG`)

Auf jeder Ebene verdichten, nicht nacherzählen; Zusammenfassung und Bild aus derselben Kernanalyse.

### Fassung 2.2 – gültig ab 2026-10-25 (aktuell)

*Änderung:* Umfang je Ebene geschärft: Abschnitt verliert keine relevante Information; Kapitel enthält jede Abschnitts-Kernaussage.

1. **Struktur bestimmen** (Bearbeitende Instanz): Wie der Text gebaut ist: Reihe, Gegensatz, Bedingung und Folge, Baum, Raum, Weg, Rahmen, Dialog … (Strukturkatalog).
2. **Kernanalyse** (Bearbeitende Instanz): Kernaussage, tragende Momente in Reihenfolge, Sprecher, bewusst Weggelassenes; kein Glied der Struktur fällt weg.
3. **Kernanalyse prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den Text: Handelnde, Wer-zu-wem, Zeitform, Ankündigung statt Bericht, nichts Wesentliches fehlt. Prüft: gibt wieder, was dasteht, Struktur vollständig. Zurück zu «Kernanalyse», wenn Abweichung.
4. **Zusammenfassen** (Bearbeitende Instanz): Aus der Kernanalyse die Zusammenfassung je Ebene mit festem Umfang; Abschnitt: keine relevante Information geht verloren; Kapitel: Kernaussage jedes Abschnitts.
5. **Zusammenfassung prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den übersetzten Text, dann sprachlich in allen Sprachen. Prüft: treu, Umfang je Ebene, sprachlich richtig. Zurück zu «Zusammenfassen», wenn Mangel.
6. **Gleichlauf** (Werkzeug (feste Prüfung)): Fingerabdrücke der Verse; ändert sich der Text, meldet der Validator die Zusammenfassung als veraltet. Prüft: Text unverändert seit Prüfung. Zurück zu «Kernanalyse», wenn Text geändert.

*Weiter, wenn:* Struktur, Kernanalyse und Zusammenfassung geprüft.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.
*Ausführlich:* docs/VERDICHTUNG.md, docs/STRUKTURKATALOG.md

### Fassung 2.1 – gültig ab 2026-10-24

*Änderung:* Struktur zuerst: Strukturanalyse vor der Kernanalyse; kein Glied der Logik fällt weg.

1. **Struktur bestimmen** (Bearbeitende Instanz): Wie der Text gebaut ist: Reihe, Gegensatz, Bedingung und Folge, Baum, Raum, Weg, Rahmen, Dialog … (Strukturkatalog).
2. **Kernanalyse** (Bearbeitende Instanz): Kernaussage, tragende Momente in Reihenfolge, Sprecher, bewusst Weggelassenes; kein Glied der Struktur fällt weg.
3. **Kernanalyse prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den Text: Handelnde, Wer-zu-wem, Zeitform, Ankündigung statt Bericht, nichts Wesentliches fehlt. Prüft: gibt wieder, was dasteht, Struktur vollständig. Zurück zu «Kernanalyse», wenn Abweichung.
4. **Zusammenfassen** (Bearbeitende Instanz): Aus der Kernanalyse die Zusammenfassung je Ebene mit festem Umfang; Abschnitt: keine relevante Information geht verloren; Kapitel: Kernaussage jedes Abschnitts.
5. **Zusammenfassung prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den übersetzten Text, dann sprachlich in allen Sprachen. Prüft: treu, Umfang je Ebene, sprachlich richtig. Zurück zu «Zusammenfassen», wenn Mangel.
6. **Gleichlauf** (Werkzeug (feste Prüfung)): Fingerabdrücke der Verse; ändert sich der Text, meldet der Validator die Zusammenfassung als veraltet. Prüft: Text unverändert seit Prüfung. Zurück zu «Kernanalyse», wenn Text geändert.

*Weiter, wenn:* Struktur, Kernanalyse und Zusammenfassung geprüft.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.
*Ausführlich:* docs/VERDICHTUNG.md, docs/STRUKTURKATALOG.md

### Fassung 2.0 – gültig ab 2026-10-23

*Änderung:* Kernanalyse als gemeinsame Grundlage von Zusammenfassung und Bild; feste Umfänge je Ebene.

1. **Kernanalyse** (Bearbeitende Instanz): Kernaussage, tragende Momente in Reihenfolge, Sprecher, bewusst Weggelassenes; kein Glied der Struktur fällt weg.
2. **Kernanalyse prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den Text: Handelnde, Wer-zu-wem, Zeitform, Ankündigung statt Bericht, nichts Wesentliches fehlt. Prüft: gibt wieder, was dasteht, Struktur vollständig. Zurück zu «Kernanalyse», wenn Abweichung.
3. **Zusammenfassen** (Bearbeitende Instanz): Aus der Kernanalyse die Zusammenfassung je Ebene mit festem Umfang; Abschnitt: keine relevante Information geht verloren; Kapitel: Kernaussage jedes Abschnitts.
4. **Zusammenfassung prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den übersetzten Text, dann sprachlich in allen Sprachen. Prüft: treu, Umfang je Ebene, sprachlich richtig. Zurück zu «Zusammenfassen», wenn Mangel.
5. **Gleichlauf** (Werkzeug (feste Prüfung)): Fingerabdrücke der Verse; ändert sich der Text, meldet der Validator die Zusammenfassung als veraltet. Prüft: Text unverändert seit Prüfung. Zurück zu «Kernanalyse», wenn Text geändert.

*Weiter, wenn:* Kernanalyse und Zusammenfassung geprüft.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.
*Ausführlich:* docs/VERDICHTUNG.md

### Fassung 1.0 – gültig ab 2026-10-12

*Änderung:* Erste Fassung: Zusammenfassungen direkt aus dem Text.

1. **Zusammenfassen** (Bearbeitende Instanz): Zusammenfassung je Ebene direkt aus dem Text.
2. **Prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft gegen den Text. Prüft: treu. Zurück zu «Zusammenfassen», wenn Mangel.

*Weiter, wenn:* Gegen den Text geprüft.
*Stand:* Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat.

## Bildauftrag (`PROC-BILDAUFTRAG`)

Vor jedem Bild steht ein stilunabhängiger Auftrag, der gegen den Text geprüft ist.

### Fassung 2.0 – gültig ab 2026-10-23 (aktuell)

*Änderung:* Aus der Kernanalyse; Worte im Bild (Stichwortband, Sprechblasen) in allen Sprachen.

1. **Auftrag aus der Kernanalyse** (Bearbeitende Instanz): Je tragendem Moment ein Bildfeld: wer, was, wer zu wem, Reihenfolge; Personen und Dinge nur aus dem Bildlexikon.
2. **Worte im Bild** (Bearbeitende Instanz): Stichwortband und Sprechblasen aus dem Lesetext, für sich verständlich, in allen Sprachen.
3. **Auftrag prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft den Auftrag wie eine Zusammenfassung gegen den Text und die Worte sprachlich. Prüft: Wer-zu-wem, Reihenfolge, keine Satzfragmente. Zurück zu «Auftrag aus der Kernanalyse», wenn Abweichung.
4. **Gleichlauf** (Werkzeug (feste Prüfung)): Fingerabdrücke von Versen und Zusammenfassung; ändert sich der Text, meldet der Validator «Bildauftrag veraltet». Prüft: Text unverändert. Zurück zu «Auftrag aus der Kernanalyse», wenn Text geändert.

*Weiter, wenn:* Auftrag und Worte geprüft.
*Ausführlich:* docs/BILDAUFTRAEGE-ANLEITUNG.md, docs/VERDICHTUNG.md

### Fassung 1.0 – gültig ab 2026-10-14

*Änderung:* Erste Fassung: Bildlexikon und Bildaufträge.

1. **Auftrag aus der Kernanalyse** (Bearbeitende Instanz): Je tragendem Moment ein Bildfeld: wer, was, wer zu wem, Reihenfolge; Personen und Dinge nur aus dem Bildlexikon.
2. **Auftrag prüfen** (Weitere Instanz (prüft)): Eine weitere Instanz prüft den Auftrag wie eine Zusammenfassung gegen den Text und die Worte sprachlich. Prüft: Wer-zu-wem, Reihenfolge, keine Satzfragmente. Zurück zu «Auftrag aus der Kernanalyse», wenn Abweichung.
3. **Gleichlauf** (Werkzeug (feste Prüfung)): Fingerabdrücke von Versen und Zusammenfassung; ändert sich der Text, meldet der Validator «Bildauftrag veraltet». Prüft: Text unverändert. Zurück zu «Auftrag aus der Kernanalyse», wenn Text geändert.

*Weiter, wenn:* Auftrag geprüft.
*Ausführlich:* docs/BILDSPRACHE.md, docs/BILDAUFTRAEGE-ANLEITUNG.md

## Gezeichnete Bilder (Symbol, Anime) (`PROC-BILD-ZEICHNUNG`)

Bilder aus Zeichen des Bildlexikons, mit Blindtest geprüft. Abgelöst durch den Aquarellstil, wo dieser vorliegt.

### Fassung 2.0 – gültig ab 2026-10-22 (aktuell)

*Änderung:* Blindtest ohne Legende mit Zielwerten; Anordnung im Browser geprüft.

1. **Zeichnen** (Werkzeug (feste Prüfung)): Das Werkzeug zeichnet das Bild aus Bildauftrag und Zeichen des Bildlexikons (Stil Symbol bzw. Anime).
2. **Anordnung prüfen** (Werkzeug (feste Prüfung)): Im Browser: Text ragt nicht über Zellen, Blasen und Pfeile überdecken nichts.
3. **Blindtest ohne Legende** (Weitere Instanz (prüft)): Eine weitere Instanz sieht nur das Bild: Welche Stelle? Was geschieht? Wer ist wer? Ein Vergleich mit der Kernanalyse vergibt Punkte. Prüft: Stelle erkannt, Kernaussage getroffen, Wer-zu-wem ohne Fehler. Zurück zu «Zeichnen», wenn Zielwert nicht erreicht (höchstens drei Runden).
4. **Liste offener Punkte** (Herausgeber): Was nach drei Runden offen ist, kommt auf eine kurze Liste für den Herausgeber.

*Weiter, wenn:* Zielwerte erreicht oder Restpunkte vermerkt.
*Ausführlich:* docs/BILDPROZESS.md, docs/SYMBOLPROZESS.md

### Fassung 1.0 – gültig ab 2026-10-14

*Änderung:* Erste Fassung: Blindtest mit Legende.

1. **Zeichnen** (Werkzeug (feste Prüfung)): Das Werkzeug zeichnet das Bild aus Bildauftrag und Zeichen des Bildlexikons (Stil Symbol bzw. Anime).
2. **Blindtest** (Weitere Instanz (prüft)): Eine weitere Instanz beschreibt das Bild mit der Legende, ohne den Auftrag. Prüft: Handelnde, Wer-zu-wem, Reihenfolge. Zurück zu «Zeichnen», wenn Abweichung.
3. **Liste offener Punkte** (Herausgeber): Was nach drei Runden offen ist, kommt auf eine kurze Liste für den Herausgeber.

*Weiter, wenn:* Blindtest ohne Abweichung oder Restpunkte vermerkt.
*Ausführlich:* docs/BILDSPRACHE.md

## Bilder im Aquarellstil (`PROC-BILD-AQUARELL`)

Gemalte Szenen nach dem Styleguide «Visuelle Bibel», geprüft nach festen Regeln, bis kein Mensch mehr drüberschauen muss.

### Fassung 2.3 – gültig ab 2026-10-28 (aktuell)

*Änderung:* Zwei prüfende Instanzen: eine günstige prüft alles, eine genauere entscheidet nur, wo eine Pflichtregel nicht besteht (Messung am Prüfsatz mit 20 Bildern bekannten Urteils). Gesicht Jesu: auch schräg oder im Profil gilt als sichtbar.

1. **Szenenplan** (Bearbeitende Instanz): Je Bildfeld: Malauftrag (Personen links/rechts nach Reihenfolge der Reden, Gefühle über Körper und Geste), wörtliche Rede aus dem Lesetext, Belege B/R/I und Feldregeln (was der Text verlangt oder verbietet).
2. **Zitate und Band** (Werkzeug (feste Prüfung)): Jede Blase steht wörtlich im Vers (… für Kürzungen); Stichwortband höchstens 54 Zeichen. Prüft: Zitat wörtlich, Band lesbar. Zurück zu «Szenenplan», wenn Abweichung.
3. **Malen** (Bildmodell): Das Bildmodell malt zwei Varianten nach Malauftrag, Stilreferenz und Figurenblatt.
4. **Blind beschreiben** (Weitere Instanz (prüft)): Eine weitere Instanz sieht nur das Bild: Personen, Gegenstände, Handlung, vermutete Bibelstelle.
5. **Regeln prüfen** (Weitere Instanz (prüft)): Dieselbe Instanz beantwortet jede Regel einzeln: allgemeine Regeln, Figurenregeln, Feldregeln; zählt verlangte Dinge. Verfehlte Pflichtregeln fragt eine zweite, genauere Instanz noch zweimal; die Mehrheit der drei Antworten gilt. Prüft: alle Pflichtregeln erfüllt.
6. **Köpfe orten** (Weitere Instanz (prüft)): Auf einem eingeblendeten Koordinatengitter werden alle Köpfe geortet und die erwarteten Figuren zugeordnet.
7. **Variante wählen** (Werkzeug (feste Prüfung)): Brauchbar ist eine Variante, die alle Pflichtregeln erfüllt, Platz für alle Blasen hat und die Reihenfolge der Sprecher einhält; gewählt wird die mit den meisten Punkten. Prüft: Pflichtregeln, Platz für Blasen, wer zuerst spricht, steht links. Zurück zu «Malen», wenn keine brauchbare Variante: neu malen mit Hinweis aus den verfehlten Regeln, höchstens drei Runden.
8. **Blasen setzen** (Werkzeug (feste Prüfung)): Blasen nur auf leerem Papier: eine Belegungskarte aus dem Bild selbst zeigt, wo gemalt ist (Figuren, Hände, gehaltene Dinge, Bauten); dazu die georteten Köpfe. Beste Anordnung aller Blasen über den Köpfen, mindestens 12 Punkte vom Bildrand, Schrift mindestens 19, keine Spitze läuft durch eine andere Blase. Umriss und Spitze als eine Linie, abgeschwächt und leicht von Hand gezogen; Gedanken als Wolke.
9. **Schlussprüfung** (Weitere Instanz (prüft)): Eine weitere Instanz prüft die fertige Kachel: Spitze beim richtigen Sprecher, keine Blase über Gesicht, Geste, gehaltenem Gegenstand oder Haupthandlung, alle Worte lesbar, Moment getroffen (mindestens 1 von 2). Was nicht besteht, fragt die zweite Instanz noch zweimal; die Mehrheit gilt. Prüft: Sprecher richtig, nichts verdeckt, lesbar, Moment. Zurück zu «Blasen setzen», wenn zweiter Blasenversuch nur im oberen Band.
10. **Prüfvermerk** (Werkzeug (feste Prüfung)): Ergebnis mit Fingerabdruck von Bild, Regeln, Szenenplan und Verfahren im Datensatz; Stufe «geprüft» nur, wenn alle Felder bestanden. Ändert sich etwas, gilt die Prüfung als veraltet.

*Weiter, wenn:* Alle Pflichtregeln und die Schlussprüfung bestanden.
*Regeln:* scripts/authoring/bilder_aquarell_daten/pruefregeln.json@2026-10-28d
*Ausführlich:* docs/BILDSTIL.md

### Fassung 2.2 – gültig ab 2026-10-28

*Änderung:* Blasen nur auf leerem Papier (Belegungskarte aus dem Bild), Mindestabstand zum Rand, keine Spitze durch eine andere Blase; Umriss mit Spitze als eine Linie, abgeschwächt und leicht von Hand gezogen (Hinweise Herausgeber).

1. **Szenenplan** (Bearbeitende Instanz): Je Bildfeld: Malauftrag (Personen links/rechts nach Reihenfolge der Reden, Gefühle über Körper und Geste), wörtliche Rede aus dem Lesetext, Belege B/R/I und Feldregeln (was der Text verlangt oder verbietet).
2. **Zitate und Band** (Werkzeug (feste Prüfung)): Jede Blase steht wörtlich im Vers (… für Kürzungen); Stichwortband höchstens 54 Zeichen. Prüft: Zitat wörtlich, Band lesbar. Zurück zu «Szenenplan», wenn Abweichung.
3. **Malen** (Bildmodell): Das Bildmodell malt zwei Varianten nach Malauftrag, Stilreferenz und Figurenblatt.
4. **Blind beschreiben** (Weitere Instanz (prüft)): Eine weitere Instanz sieht nur das Bild: Personen, Gegenstände, Handlung, vermutete Bibelstelle.
5. **Regeln prüfen** (Weitere Instanz (prüft)): Dieselbe Instanz beantwortet jede Regel einzeln: allgemeine Regeln, Figurenregeln, Feldregeln; zählt verlangte Dinge. Verfehlte Pflichtregeln werden zweimal neu gefragt, die Mehrheit gilt. Prüft: alle Pflichtregeln erfüllt.
6. **Köpfe orten** (Weitere Instanz (prüft)): Auf einem eingeblendeten Koordinatengitter werden alle Köpfe geortet und die erwarteten Figuren zugeordnet.
7. **Variante wählen** (Werkzeug (feste Prüfung)): Brauchbar ist eine Variante, die alle Pflichtregeln erfüllt, Platz für alle Blasen hat und die Reihenfolge der Sprecher einhält; gewählt wird die mit den meisten Punkten. Prüft: Pflichtregeln, Platz für Blasen, wer zuerst spricht, steht links. Zurück zu «Malen», wenn keine brauchbare Variante: neu malen mit Hinweis aus den verfehlten Regeln, höchstens drei Runden.
8. **Blasen setzen** (Werkzeug (feste Prüfung)): Blasen nur auf leerem Papier: eine Belegungskarte aus dem Bild selbst zeigt, wo gemalt ist (Figuren, Hände, gehaltene Dinge, Bauten); dazu die georteten Köpfe. Beste Anordnung aller Blasen über den Köpfen, mindestens 12 Punkte vom Bildrand, Schrift mindestens 19, keine Spitze läuft durch eine andere Blase. Umriss und Spitze als eine Linie, abgeschwächt und leicht von Hand gezogen; Gedanken als Wolke.
9. **Schlussprüfung** (Weitere Instanz (prüft)): Eine weitere Instanz prüft die fertige Kachel: Spitze beim richtigen Sprecher, keine Blase über Gesicht, Geste, gehaltenem Gegenstand oder Haupthandlung, alle Worte lesbar, Moment getroffen (mindestens 1 von 2). Prüft: Sprecher richtig, nichts verdeckt, lesbar, Moment. Zurück zu «Blasen setzen», wenn zweiter Blasenversuch nur im oberen Band.
10. **Prüfvermerk** (Werkzeug (feste Prüfung)): Ergebnis mit Fingerabdruck von Bild, Regeln, Szenenplan und Verfahren im Datensatz; Stufe «geprüft» nur, wenn alle Felder bestanden. Ändert sich etwas, gilt die Prüfung als veraltet.

*Weiter, wenn:* Alle Pflichtregeln und die Schlussprüfung bestanden.
*Regeln:* scripts/authoring/bilder_aquarell_daten/pruefregeln.json@2026-10-28b
*Ausführlich:* docs/BILDSTIL.md

### Fassung 2.1 – gültig ab 2026-10-28

*Änderung:* Köpfe auf Koordinatengitter, Zweitmeinung (Mehrheit aus drei), beste Blasenanordnung, feste Regeln für Platz, Schriftgrösse und Reihenfolge schon bei der Wahl.

1. **Szenenplan** (Bearbeitende Instanz): Je Bildfeld: Malauftrag (Personen links/rechts nach Reihenfolge der Reden, Gefühle über Körper und Geste), wörtliche Rede aus dem Lesetext, Belege B/R/I und Feldregeln (was der Text verlangt oder verbietet).
2. **Zitate und Band** (Werkzeug (feste Prüfung)): Jede Blase steht wörtlich im Vers (… für Kürzungen); Stichwortband höchstens 54 Zeichen. Prüft: Zitat wörtlich, Band lesbar. Zurück zu «Szenenplan», wenn Abweichung.
3. **Malen** (Bildmodell): Das Bildmodell malt zwei Varianten nach Malauftrag, Stilreferenz und Figurenblatt.
4. **Blind beschreiben** (Weitere Instanz (prüft)): Eine weitere Instanz sieht nur das Bild: Personen, Gegenstände, Handlung, vermutete Bibelstelle.
5. **Regeln prüfen** (Weitere Instanz (prüft)): Dieselbe Instanz beantwortet jede Regel einzeln: allgemeine Regeln, Figurenregeln, Feldregeln; zählt verlangte Dinge. Verfehlte Pflichtregeln werden zweimal neu gefragt, die Mehrheit gilt. Prüft: alle Pflichtregeln erfüllt.
6. **Köpfe orten** (Weitere Instanz (prüft)): Auf einem eingeblendeten Koordinatengitter werden alle Köpfe geortet und die erwarteten Figuren zugeordnet.
7. **Variante wählen** (Werkzeug (feste Prüfung)): Brauchbar ist eine Variante, die alle Pflichtregeln erfüllt, Platz für alle Blasen hat und die Reihenfolge der Sprecher einhält; gewählt wird die mit den meisten Punkten. Prüft: Pflichtregeln, Platz für Blasen, wer zuerst spricht, steht links. Zurück zu «Malen», wenn keine brauchbare Variante: neu malen mit Hinweis aus den verfehlten Regeln, höchstens drei Runden.
8. **Blasen setzen** (Werkzeug (feste Prüfung)): Beste Anordnung aller Blasen über den Köpfen, Schrift mindestens 19, Gedanken als Wolke.
9. **Schlussprüfung** (Weitere Instanz (prüft)): Eine weitere Instanz prüft die fertige Kachel: Spitze beim richtigen Sprecher, keine Blase über Gesicht, Geste oder Haupthandlung, alle Worte lesbar, Moment getroffen (mindestens 1 von 2). Prüft: Sprecher richtig, nichts verdeckt, lesbar, Moment. Zurück zu «Blasen setzen», wenn zweiter Blasenversuch nur im oberen Band.
10. **Prüfvermerk** (Werkzeug (feste Prüfung)): Ergebnis mit Fingerabdruck von Bild, Regeln, Szenenplan und Verfahren im Datensatz; Stufe «geprüft» nur, wenn alle Felder bestanden. Ändert sich etwas, gilt die Prüfung als veraltet.

*Weiter, wenn:* Alle Pflichtregeln und die Schlussprüfung bestanden.
*Regeln:* scripts/authoring/bilder_aquarell_daten/pruefregeln.json@2026-10-28b
*Ausführlich:* docs/BILDSTIL.md

### Fassung 2.0 – gültig ab 2026-10-28

*Änderung:* Automatische Prüfung: Regeln auf drei Ebenen, Wahl der Variante, Blasen und Schlussprüfung ohne Handarbeit.

1. **Szenenplan** (Bearbeitende Instanz): Je Bildfeld: Malauftrag (Personen links/rechts nach Reihenfolge der Reden, Gefühle über Körper und Geste), wörtliche Rede aus dem Lesetext, Belege B/R/I und Feldregeln (was der Text verlangt oder verbietet).
2. **Zitate und Band** (Werkzeug (feste Prüfung)): Jede Blase steht wörtlich im Vers (… für Kürzungen); Stichwortband höchstens 54 Zeichen. Prüft: Zitat wörtlich, Band lesbar. Zurück zu «Szenenplan», wenn Abweichung.
3. **Malen** (Bildmodell): Das Bildmodell malt zwei Varianten nach Malauftrag, Stilreferenz und Figurenblatt.
4. **Blind beschreiben** (Weitere Instanz (prüft)): Eine weitere Instanz sieht nur das Bild: Personen, Gegenstände, Handlung, vermutete Bibelstelle.
5. **Regeln prüfen** (Weitere Instanz (prüft)): Dieselbe Instanz beantwortet jede Regel einzeln (allgemein, Figur, Feld), zählt verlangte Dinge und gibt Kopfpositionen an. Prüft: alle Pflichtregeln erfüllt.
6. **Variante wählen** (Werkzeug (feste Prüfung)): Brauchbar ist eine Variante, die alle Pflichtregeln erfüllt; gewählt wird die mit den meisten Punkten. Prüft: Pflichtregeln. Zurück zu «Malen», wenn keine brauchbare Variante: neu malen mit Hinweis, höchstens drei Runden.
7. **Blasen setzen** (Werkzeug (feste Prüfung)): Blasen nacheinander über oder neben dem Kopf der sprechenden Person.
8. **Schlussprüfung** (Weitere Instanz (prüft)): Eine weitere Instanz prüft die fertige Kachel: Spitze beim richtigen Sprecher, keine Blase über Gesicht, Geste oder Haupthandlung, alle Worte lesbar, Moment getroffen (mindestens 1 von 2). Prüft: Sprecher richtig, nichts verdeckt, lesbar, Moment. Zurück zu «Blasen setzen», wenn zweiter Blasenversuch nur im oberen Band.
9. **Prüfvermerk** (Werkzeug (feste Prüfung)): Ergebnis mit Fingerabdruck von Bild, Regeln, Szenenplan und Verfahren im Datensatz; Stufe «geprüft» nur, wenn alle Felder bestanden. Ändert sich etwas, gilt die Prüfung als veraltet.

*Weiter, wenn:* Alle Pflichtregeln und die Schlussprüfung bestanden.
*Regeln:* scripts/authoring/bilder_aquarell_daten/pruefregeln.json@2026-10-28
*Ausführlich:* docs/BILDSTIL.md

### Fassung 1.0 – gültig ab 2026-10-27

*Änderung:* Styleguide V1.2 übernommen; Auswahl und Blasen von Hand, Blindtest.

1. **Szenenplan** (Bearbeitende Instanz): Je Bildfeld: Malauftrag, wörtliche Rede aus dem Lesetext, Belege B/R/I.
2. **Zitate** (Werkzeug (feste Prüfung)): Jede Blase steht wörtlich im Vers. Prüft: Zitat wörtlich. Zurück zu «Szenenplan», wenn Abweichung.
3. **Malen** (Bildmodell): Das Bildmodell malt Varianten nach Malauftrag, Stilreferenz und Figurenblatt.
4. **Auswählen und Blasen setzen** (Bearbeitende Instanz): Die bearbeitende Instanz wählt eine Variante und setzt die Blasen.
5. **Blindtest** (Weitere Instanz (prüft)): Eine weitere Instanz beschreibt die fertigen Felder ohne Auftrag; Abweichungen führen zu neuem Malen. Prüft: Stelle, Wer-zu-wem, Figuren. Zurück zu «Malen», wenn Abweichung.
6. **Prüfvermerk** (Bearbeitende Instanz): Ergebnis und offene Punkte im Datensatz.

*Weiter, wenn:* Blindtest ohne Abweichung, offene Punkte vermerkt.
*Ausführlich:* docs/BILDSTIL.md

## Prüfen und veröffentlichen (`PROC-FREIGABE`)

Jeder Stand ist geprüft, versioniert und nachvollziehbar.

### Fassung 2.0 – gültig ab 2026-10-28 (aktuell)

*Änderung:* Bildläufe werden automatisch zusammengeführt, wenn alle Prüfungen bestanden sind (Entscheid Herausgeber).

1. **Validator** (Werkzeug (feste Prüfung)): Schema, IDs, Verweise, Bibelstellen, Quellen, Gleichlauf mit dem Text, Prüfvermerke. Prüft: keine Fehler.
2. **App-Tests** (Werkzeug (feste Prüfung)): Bau der App und automatische Tests im Browser. Prüft: alle Tests bestanden.
3. **Zusammenführen** (Werkzeug (feste Prüfung)): Läufe der Bildwerkstatt werden automatisch in den Hauptstand übernommen, wenn alle Prüfungen bestanden sind; bei Widersprüchen bricht das Zusammenführen ab.
4. **Veröffentlichen** (Werkzeug (feste Prüfung)): Jeder Stand des Hauptzweigs wird gebaut, geprüft und veröffentlicht; jede Änderung bleibt mit Grund in der Versionsgeschichte.
5. **Grundsätze** (Herausgeber): Der Herausgeber entscheidet Grundsätze und offene Fragen; Entscheide stehen mit Datum in der Dokumentation.

*Weiter, wenn:* Validator und Tests bestanden.
*Ausführlich:* AGENTS.md

### Fassung 1.0 – gültig ab 2026-10-09

*Änderung:* Erste Fassung: bearbeitende Instanz führt Änderungen nach bestandenen Prüfungen zusammen.

1. **Validator** (Werkzeug (feste Prüfung)): Schema, IDs, Verweise, Bibelstellen, Quellen, Gleichlauf mit dem Text, Prüfvermerke. Prüft: keine Fehler.
2. **App-Tests** (Werkzeug (feste Prüfung)): Bau der App und automatische Tests im Browser. Prüft: alle Tests bestanden.
3. **Zusammenführen** (Bearbeitende Instanz): Die bearbeitende Instanz führt geprüfte Änderungen in den Hauptstand.
4. **Veröffentlichen** (Werkzeug (feste Prüfung)): Jeder Stand des Hauptzweigs wird gebaut, geprüft und veröffentlicht; jede Änderung bleibt mit Grund in der Versionsgeschichte.
5. **Grundsätze** (Herausgeber): Der Herausgeber entscheidet Grundsätze und offene Fragen; Entscheide stehen mit Datum in der Dokumentation.

*Weiter, wenn:* Validator und Tests bestanden.
*Ausführlich:* AGENTS.md
