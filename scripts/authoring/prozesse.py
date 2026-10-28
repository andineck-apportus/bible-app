#!/usr/bin/env python3
"""Versionierte Prozessbeschreibungen (docs/PROZESSE.md, data/processes/).

Jeder Prozess hat Fassungen mit Gültigkeit ab Datum. Eine Fassung besteht aus Schritten; jeder Schritt hat eine Rolle:
  bearbeitung  bearbeitende Instanz (erstellt den Entwurf)
  pruefung     weitere, getrennte Instanz (prüft, ohne den Entwurf erstellt zu haben)
  werkzeug     feste Prüfung im Werkzeug (Regel, Validator, Abgleich)
  modell       Bildmodell (malt nach Auftrag)
  herausgabe   Herausgeber (entscheidet Grundsätze und offene Fragen)
Inhalte verweisen auf «PROC-…@Fassung»; frühere Fassungen bleiben abrufbar und werden in der App weiter dargestellt.

Ändert sich ein Ablauf, wird hier eine neue Fassung angelegt (nicht die alte überschrieben):
  python3 scripts/authoring/prozesse.py      # schreibt data/processes/*.json und docs/PROZESSE.md
"""
import copy
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "data/processes"
ROLLEN = {"bearbeitung": "Bearbeitende Instanz", "pruefung": "Weitere Instanz (prüft)", "werkzeug": "Werkzeug (feste Prüfung)",
          "modell": "Bildmodell", "herausgabe": "Herausgeber"}


def s(id_, rolle, titel, tut, ergebnis=None, prueft=None, zurueck=None):
    x = {"id": id_, "role": rolle, "title_de": titel, "do_de": tut}
    if ergebnis:
        x["result_de"] = ergebnis
    if prueft:
        x["checks_de"] = prueft
    if zurueck:
        x["back"] = {"to": zurueck[0], "when_de": zurueck[1]}
    return x


def fassung(version, ab, aenderung, schritte, freigabe, grenzen=None, regeln=None, docs=None):
    v = {"version": version, "valid_from": ab, "change_de": aenderung, "steps": schritte, "gate_de": freigabe}
    if grenzen:
        v["limits_de"] = grenzen
    if regeln:
        v["rules"] = regeln
    if docs:
        v["docs"] = docs
    return v


def ohne(schritte, *ids):
    return [x for x in copy.deepcopy(schritte) if x["id"] not in ids]


def ersetze(schritte, id_, neu):
    return [neu if x["id"] == id_ else x for x in copy.deepcopy(schritte)]


ENTWURF = "Stand Entwurf: Eine fachliche Prüfung durch Personen ist vorgesehen und wird erst eingetragen, wenn sie stattgefunden hat."
P = {}

# ------------------------------------------------------------------ Quellen und Urtext
q11 = [
    s("q1", "bearbeitung", "Quelle finden", "Editionen, Handschriften, Übersetzungen und Hilfsmittel für den Abschnitt suchen; Fassung, Fundort und Nutzungsbedingungen festhalten."),
    s("q2", "bearbeitung", "Recht prüfen", "Nutzungsrecht bestimmen: gemeinfrei, CC0, CC BY, CC BY-SA in den freien Kern; nicht kommerzielle Quellen nur in die Studienschicht; geschützte Quellen nur nennen.",
      "Eintrag im Quellenkatalog mit Nutzungsrecht, Verwendung und Begründung"),
    s("q3", "werkzeug", "Katalog abgleichen", "Der Validator prüft, dass jede Herkunftsadresse im Katalog steht und verwendete Quellen auf vorhandene Dateien zeigen.",
      prueft=["Herkunft im Katalog", "Schichten nicht vermischt"], zurueck=("q2", "Herkunft fehlt oder Schicht falsch")),
    s("q4", "bearbeitung", "Urtext übernehmen", "Edition und Datenversion festlegen, Originaldatei mit Prüfsumme nachweisen, Wörter (Token) mit Morphologie übernehmen.",
      "Text mit stabilen Wort-IDs"),
    s("q5", "werkzeug", "Vollständigkeit prüfen", "Versumfang, Verszählung und Wort-IDs gegen die Edition prüfen.", prueft=["alle Verse vorhanden", "Zählung nach Versifikation"],
      zurueck=("q4", "Lücke oder Zählfehler")),
    s("q6", "herausgabe", "Anfragen", "Bei Quellen mit unklarem Recht fragt der Herausgeber beim Rechteinhaber an; Anfrage und Antwort werden protokolliert."),
]
P["PROC-QUELLEN"] = {"names": {"de": "Quellen und Urtext", "en": "Sources and original text"}, "group": "text",
    "purpose_de": "Nur Quellen verwenden, deren Recht geklärt ist, und den Urtext nachvollziehbar übernehmen.",
    "versions": [
        fassung("1.0", "2026-10-09", "Lizenzschichten: freier Kern und Studienschicht getrennt.", ohne(q11, "q3", "q6"),
                "Quelle mit geklärtem Recht und vollständiger, geprüfter Text.", docs=["LIZENZEN.md", "docs/QUELLEN.md"]),
        fassung("1.1", "2026-10-13", "Quellenkatalog mit Abgleich im Validator; Anfragen an Rechteinhaber protokolliert.", q11,
                "Quelle im Katalog, Recht geklärt, Text vollständig und geprüft.", docs=["LIZENZEN.md", "docs/QUELLEN.md", "docs/ANFRAGEN.md"])]}

# ------------------------------------------------------------------ Lesarten
l10 = [
    s("l1", "werkzeug", "Zeugen vergleichen", "Handschriften und Textausgaben Wort für Wort vergleichen (Kollation); Abweichungen als Lesarten mit ihren Zeugen erfassen."),
    s("l2", "bearbeitung", "Lesarten ordnen", "Lesarten zu Variationsstellen zusammenfassen; Belegarten trennen (Handschrift, Apparat, Sekundärtranskription)."),
    s("l3", "bearbeitung", "Textgrundlage festhalten", "Die Lesart, der die Übersetzung folgt, als begründete, revidierbare Entscheidung mit Alternativen ablegen – keine Entscheidung über «richtig»."),
    s("l4", "pruefung", "Gegenprüfen", "Eine weitere Instanz prüft Zeugenangaben und Zuordnung gegen die Quellen.", prueft=["Zeugen stimmen", "Belegart richtig"], zurueck=("l2", "Abweichung")),
    s("l5", "werkzeug", "Validator", "Verweise auf Lesarten, Zeugen und Wort-IDs prüfen.", prueft=["alle Verweise gültig"]),
]
P["PROC-LESARTEN"] = {"names": {"de": "Lesarten (Textkritik)", "en": "Readings (textual criticism)"}, "group": "text",
    "purpose_de": "Zeigen, wo alte Handschriften voneinander abweichen, mit Zeugen, ohne zu entscheiden, was richtig ist.",
    "versions": [fassung("1.0", "2026-10-09", "Erste Fassung.", l10, "Alle Lesarten mit Zeugen, Textgrundlage begründet.", ENTWURF, docs=["docs/GESICHERTHEIT.md"])]}

# ------------------------------------------------------------------ Übersetzung
u12 = [
    s("u1", "bearbeitung", "Übersetzen", "Aus dem Urtext (Griechisch, Hebräisch) übersetzen, wörtlich orientiert in verständlichem Deutsch; Grundentscheide des Buchs einhalten (Schlüsselwörter, Erzählzeit).",
      "Lesetext je Vers"),
    s("u2", "bearbeitung", "Wörter zuordnen", "Jedes deutsche Wort den Wörtern des Urtexts zuordnen (Wortzuordnung).", "Wortzuordnung"),
    s("u3", "bearbeitung", "Entscheide festhalten", "Wo die Übersetzung glättet, deutet oder einer Tradition folgt, Entscheid mit Begründung und Alternative festhalten. Wirkt eine wörtliche Wendung heute gegen ihren Sinn, gibt der Lesetext den Sinn wieder; die wörtliche Fassung steht als Alternative.",
      "Entscheide und Alternativen beim Vers"),
    s("u4", "pruefung", "Inhalt prüfen", "Eine weitere Instanz prüft gegen den Urtext: Bedeutung, Zeitform, Satzart, Handelnde, Wer-zu-wem.", prueft=["treu zum Urtext", "nichts ergänzt, nichts weggelassen"],
      zurueck=("u1", "Abweichung vom Urtext")),
    s("u5", "pruefung", "Sprache prüfen", "Eine weitere Instanz prüft Grammatik, Schweizer Rechtschreibung, heutigen Ausdruck und Lesefluss; geglättet wird nur, soweit Bedeutung, Zeitform, Satzart und Wortzuordnung erhalten bleiben.",
      prueft=["Grammatik und Rechtschreibung", "keine steifen oder wörtlich übertragenen Wendungen"], zurueck=("u1", "sprachlicher Mangel")),
    s("u6", "werkzeug", "Validator", "Wortzuordnung, Verse und Verweise prüfen.", prueft=["jedes Wort zugeordnet", "Verse vollständig"]),
]
P["PROC-UEBERSETZUNG"] = {"names": {"de": "Übersetzung aus dem Urtext", "en": "Translation from the original"}, "group": "text",
    "purpose_de": "Eine eigene, nachvollziehbare Übersetzung aus dem Urtext: treu, verständlich, mit offengelegten Entscheiden.",
    "versions": [
        fassung("1.0", "2026-10-09", "Erste Fassung: Übersetzung mit Wortzuordnung und Entscheiden, inhaltliche Prüfung.", ohne(u12, "u5"), "Lesetext geprüft, Wortzuordnung vollständig.", ENTWURF),
        fassung("1.1", "2026-10-13", "Sprachliche Prüfung als eigener Schritt nach der inhaltlichen.", ersetze(u12, "u3", s("u3", "bearbeitung", "Entscheide festhalten", "Wo die Übersetzung glättet, deutet oder einer Tradition folgt, Entscheid mit Begründung und Alternative festhalten.", "Entscheide und Alternativen beim Vers")),
                "Lesetext inhaltlich und sprachlich geprüft, Wortzuordnung vollständig.", ENTWURF),
        fassung("1.2", "2026-10-24", "Wendungen, die heute gegen ihren Sinn wirken, gibt der Lesetext dem Sinn nach wieder; die wörtliche Fassung bleibt als Alternative (z. B. Mt 5,37).", u12,
                "Lesetext inhaltlich und sprachlich geprüft, Wortzuordnung vollständig.", ENTWURF, docs=["docs/ENTSCHEIDUNGEN.md"])]}

m10 = [
    s("m1", "bearbeitung", "Aus dem Urtext übersetzen", "Jede Sprach- oder Mundartfassung entsteht als eigene Schicht direkt aus dem Urtext, mit Wortzuordnung; die hochdeutsche Fassung dient nur zur Kontrolle.", "Lesetext der Schicht"),
    s("m2", "bearbeitung", "Schicht beschreiben", "Sprache, Zielgruppe, Schreibweise (z. B. Züridüütsch nach Dieth) und Ton festhalten; Entscheide wie bei der Übersetzung."),
    s("m3", "pruefung", "Inhalt prüfen", "Eine weitere Instanz vergleicht mit dem Urtext und der Kontrollübersetzung.", prueft=["treu zum Urtext"], zurueck=("m1", "Abweichung")),
    s("m4", "pruefung", "Sprache prüfen", "Eine weitere Instanz prüft Schreibweise, Wortwahl und Lesefluss der Mundart.", prueft=["festgelegte Schreibweise", "idiomatisch"], zurueck=("m1", "Mangel")),
    s("m5", "herausgabe", "Muttersprachlich prüfen", "Eine Person mit dieser Muttersprache liest gegen; erst dann wird die Prüfung eingetragen."),
]
P["PROC-MUNDART"] = {"names": {"de": "Weitere Sprachen und Mundarten", "en": "Further languages and dialects"}, "group": "text",
    "purpose_de": "Jede Sprache und Mundart eigenständig aus dem Urtext, nicht aus dem Hochdeutschen abgeleitet.",
    "versions": [fassung("1.0", "2026-10-13", "Erste Fassung (Züridüütsch).", m10, "Inhaltlich und sprachlich geprüft; muttersprachliche Prüfung vorgesehen.", ENTWURF)]}

# ------------------------------------------------------------------ Studie
st11 = [
    s("t1", "bearbeitung", "Befunde", "Was im Text steht: Wortbedeutung, Grammatik, Aufbau, wiederkehrende Begriffe – getrennt von jeder Deutung."),
    s("t2", "bearbeitung", "Deutungen", "Wie man den Text verstehen kann: mehrere begründbare Verständnisse mit Befunden, Gegenargumenten und Gesichertheit; keine Entscheidung über richtig oder falsch."),
    s("t3", "bearbeitung", "Hintergrund damals", "Zeit, Ort, Kultur und Sprachgebrauch der Adressaten mit antiken Quellen."),
    s("t4", "pruefung", "Quellen nachschlagen", "Eine weitere Instanz schlägt jede antike Quelle in frei zugänglichen Ausgaben nach: bestätigt, berichtigt, teilweise oder nicht prüfbar. Was sich nicht belegen lässt, wird abgeschwächt oder gestrichen.",
      "Prüfvermerk je Notiz", ["Stelle sagt, was die Notiz behauptet"], ("t3", "Angabe falsch oder nicht belegt")),
    s("t5", "pruefung", "Gegen den Text prüfen", "Eine weitere Instanz prüft Befunde und Deutungen gegen den Text und auf Trennung der Ebenen.", prueft=["Befund ≠ Deutung", "Alternativen sichtbar"], zurueck=("t1", "Vermischung oder Fehler")),
    s("t6", "werkzeug", "Validator", "Stellenmarken, Verweise und Ursprachwörter prüfen.", prueft=["Stellen gültig", "Ursprachwörter erfasst"]),
]
P["PROC-STUDIE"] = {"names": {"de": "Befunde, Deutungen, Hintergrund", "en": "Findings, interpretations, background"}, "group": "inhalt",
    "purpose_de": "Was dasteht, wie man es verstehen kann und was damals galt – sauber getrennt und belegt.",
    "versions": [
        fassung("1.0", "2026-10-12", "Erste Fassung.", ohne(st11, "t4"), "Ebenen getrennt, gegen den Text geprüft.", ENTWURF, docs=["docs/GESICHERTHEIT.md"]),
        fassung("1.1", "2026-10-18", "Antike Quellen werden am Text nachgeschlagen; Ergebnis als Prüfvermerk bei jeder Notiz.", st11, "Ebenen getrennt, Quellen nachgeschlagen, gegen den Text geprüft.", ENTWURF,
                docs=["docs/QUELLENPRUEFUNG.md", "docs/GESICHERTHEIT.md"])]}

d10 = [
    s("d1", "bearbeitung", "Damals", "Hintergrund der ersten Leser: Situation, Sitte, Bedeutung damals."),
    s("d2", "bearbeitung", "Prinzip", "Den Grundsatz ableiten, der über die damalige Situation hinaus gilt, mit Begründung."),
    s("d3", "bearbeitung", "Heute", "Anwendung je Zielgruppe mit Grenze. Heutiges steht nie im Bibeltext, in Zusammenfassung oder Bild."),
    s("d4", "pruefung", "Prüfen", "Eine weitere Instanz prüft die Herleitung Damals → Prinzip → Heute und die Kennzeichnung.", prueft=["Text bleibt treu", "Stufen gekennzeichnet"], zurueck=("d2", "Herleitung trägt nicht")),
]
P["PROC-DAMALS-HEUTE"] = {"names": {"de": "Damals → Prinzip → Heute", "en": "Then → principle → today"}, "group": "inhalt",
    "purpose_de": "Den Text treu lassen und daneben gekennzeichnet übertragen.",
    "versions": [fassung("1.0", "2026-10-23", "Erste Fassung.", d10, "Drei Stufen getrennt und geprüft.", ENTWURF, docs=["docs/DAMALS-PRINZIP-HEUTE.md"])]}

# ------------------------------------------------------------------ Verdichtung
v22 = [
    s("v1", "bearbeitung", "Struktur bestimmen", "Wie der Text gebaut ist: Reihe, Gegensatz, Bedingung und Folge, Baum, Raum, Weg, Rahmen, Dialog … (Strukturkatalog).", "Strukturanalyse"),
    s("v2", "bearbeitung", "Kernanalyse", "Kernaussage, tragende Momente in Reihenfolge, Sprecher, bewusst Weggelassenes; kein Glied der Struktur fällt weg.", "Kernanalyse"),
    s("v3", "pruefung", "Kernanalyse prüfen", "Eine weitere Instanz prüft gegen den Text: Handelnde, Wer-zu-wem, Zeitform, Ankündigung statt Bericht, nichts Wesentliches fehlt.", prueft=["gibt wieder, was dasteht", "Struktur vollständig"],
      zurueck=("v2", "Abweichung")),
    s("v4", "bearbeitung", "Zusammenfassen", "Aus der Kernanalyse die Zusammenfassung je Ebene mit festem Umfang; Abschnitt: keine relevante Information geht verloren; Kapitel: Kernaussage jedes Abschnitts.", "Zusammenfassung"),
    s("v5", "pruefung", "Zusammenfassung prüfen", "Eine weitere Instanz prüft gegen den übersetzten Text, dann sprachlich in allen Sprachen.", prueft=["treu", "Umfang je Ebene", "sprachlich richtig"], zurueck=("v4", "Mangel")),
    s("v6", "werkzeug", "Gleichlauf", "Fingerabdrücke der Verse; ändert sich der Text, meldet der Validator die Zusammenfassung als veraltet.", prueft=["Text unverändert seit Prüfung"], zurueck=("v2", "Text geändert")),
]
v10 = [s("v4", "bearbeitung", "Zusammenfassen", "Zusammenfassung je Ebene direkt aus dem Text."),
       s("v5", "pruefung", "Prüfen", "Eine weitere Instanz prüft gegen den Text.", prueft=["treu"], zurueck=("v4", "Mangel"))]
P["PROC-VERDICHTUNG"] = {"names": {"de": "Kernanalyse und Zusammenfassungen", "en": "Core analysis and summaries"}, "group": "inhalt",
    "purpose_de": "Auf jeder Ebene verdichten, nicht nacherzählen; Zusammenfassung und Bild aus derselben Kernanalyse.",
    "versions": [
        fassung("1.0", "2026-10-12", "Erste Fassung: Zusammenfassungen direkt aus dem Text.", v10, "Gegen den Text geprüft.", ENTWURF),
        fassung("2.0", "2026-10-23", "Kernanalyse als gemeinsame Grundlage von Zusammenfassung und Bild; feste Umfänge je Ebene.", ohne(v22, "v1"), "Kernanalyse und Zusammenfassung geprüft.", ENTWURF, docs=["docs/VERDICHTUNG.md"]),
        fassung("2.1", "2026-10-24", "Struktur zuerst: Strukturanalyse vor der Kernanalyse; kein Glied der Logik fällt weg.", v22, "Struktur, Kernanalyse und Zusammenfassung geprüft.", ENTWURF, docs=["docs/VERDICHTUNG.md", "docs/STRUKTURKATALOG.md"]),
        fassung("2.2", "2026-10-25", "Umfang je Ebene geschärft: Abschnitt verliert keine relevante Information; Kapitel enthält jede Abschnitts-Kernaussage.", v22, "Struktur, Kernanalyse und Zusammenfassung geprüft.", ENTWURF, docs=["docs/VERDICHTUNG.md", "docs/STRUKTURKATALOG.md"])]}

# ------------------------------------------------------------------ Bildauftrag
b20 = [
    s("a1", "bearbeitung", "Auftrag aus der Kernanalyse", "Je tragendem Moment ein Bildfeld: wer, was, wer zu wem, Reihenfolge; Personen und Dinge nur aus dem Bildlexikon.", "Bildauftrag"),
    s("a2", "bearbeitung", "Worte im Bild", "Stichwortband und Sprechblasen aus dem Lesetext, für sich verständlich, in allen Sprachen."),
    s("a3", "pruefung", "Auftrag prüfen", "Eine weitere Instanz prüft den Auftrag wie eine Zusammenfassung gegen den Text und die Worte sprachlich.", prueft=["Wer-zu-wem", "Reihenfolge", "keine Satzfragmente"], zurueck=("a1", "Abweichung")),
    s("a4", "werkzeug", "Gleichlauf", "Fingerabdrücke von Versen und Zusammenfassung; ändert sich der Text, meldet der Validator «Bildauftrag veraltet».", prueft=["Text unverändert"], zurueck=("a1", "Text geändert")),
]
P["PROC-BILDAUFTRAG"] = {"names": {"de": "Bildauftrag", "en": "Picture brief"}, "group": "bild",
    "purpose_de": "Vor jedem Bild steht ein stilunabhängiger Auftrag, der gegen den Text geprüft ist.",
    "versions": [
        fassung("1.0", "2026-10-14", "Erste Fassung: Bildlexikon und Bildaufträge.", [x for x in b20 if x["id"] != "a2"], "Auftrag geprüft.", docs=["docs/BILDSPRACHE.md", "docs/BILDAUFTRAEGE-ANLEITUNG.md"]),
        fassung("2.0", "2026-10-23", "Aus der Kernanalyse; Worte im Bild (Stichwortband, Sprechblasen) in allen Sprachen.", b20, "Auftrag und Worte geprüft.", docs=["docs/BILDAUFTRAEGE-ANLEITUNG.md", "docs/VERDICHTUNG.md"])]}

z20 = [
    s("z1", "werkzeug", "Zeichnen", "Das Werkzeug zeichnet das Bild aus Bildauftrag und Zeichen des Bildlexikons (Stil Symbol bzw. Anime)."),
    s("z2", "werkzeug", "Anordnung prüfen", "Im Browser: Text ragt nicht über Zellen, Blasen und Pfeile überdecken nichts."),
    s("z3", "pruefung", "Blindtest ohne Legende", "Eine weitere Instanz sieht nur das Bild: Welche Stelle? Was geschieht? Wer ist wer? Ein Vergleich mit der Kernanalyse vergibt Punkte.", prueft=["Stelle erkannt", "Kernaussage getroffen", "Wer-zu-wem ohne Fehler"],
      zurueck=("z1", "Zielwert nicht erreicht (höchstens drei Runden)")),
    s("z4", "herausgabe", "Liste offener Punkte", "Was nach drei Runden offen ist, kommt auf eine kurze Liste für den Herausgeber."),
]
P["PROC-BILD-ZEICHNUNG"] = {"names": {"de": "Gezeichnete Bilder (Symbol, Anime)", "en": "Drawn pictures (symbol, anime)"}, "group": "bild",
    "purpose_de": "Bilder aus Zeichen des Bildlexikons, mit Blindtest geprüft. Abgelöst durch den Aquarellstil, wo dieser vorliegt.",
    "versions": [
        fassung("1.0", "2026-10-14", "Erste Fassung: Blindtest mit Legende.", ersetze(ohne(z20, "z2"), "z3", s("z3", "pruefung", "Blindtest", "Eine weitere Instanz beschreibt das Bild mit der Legende, ohne den Auftrag.", prueft=["Handelnde", "Wer-zu-wem", "Reihenfolge"], zurueck=("z1", "Abweichung"))),
                "Blindtest ohne Abweichung oder Restpunkte vermerkt.", docs=["docs/BILDSPRACHE.md"]),
        fassung("2.0", "2026-10-22", "Blindtest ohne Legende mit Zielwerten; Anordnung im Browser geprüft.", z20, "Zielwerte erreicht oder Restpunkte vermerkt.", docs=["docs/BILDPROZESS.md", "docs/SYMBOLPROZESS.md"])]}

# ------------------------------------------------------------------ Aquarell
aq21 = [
    s("w1", "bearbeitung", "Szenenplan", "Je Bildfeld: Malauftrag (Personen links/rechts nach Reihenfolge der Reden, Gefühle über Körper und Geste), wörtliche Rede aus dem Lesetext, Belege B/R/I und Feldregeln (was der Text verlangt oder verbietet).",
      "Szenenplan mit Prüfregeln"),
    s("w2", "werkzeug", "Zitate und Band", "Jede Blase steht wörtlich im Vers (… für Kürzungen); Stichwortband höchstens 54 Zeichen.", prueft=["Zitat wörtlich", "Band lesbar"], zurueck=("w1", "Abweichung")),
    s("w3", "modell", "Malen", "Das Bildmodell malt zwei Varianten nach Malauftrag, Stilreferenz und Figurenblatt."),
    s("w4", "pruefung", "Blind beschreiben", "Eine weitere Instanz sieht nur das Bild: Personen, Gegenstände, Handlung, vermutete Bibelstelle."),
    s("w5", "pruefung", "Regeln prüfen", "Dieselbe Instanz beantwortet jede Regel einzeln: allgemeine Regeln, Figurenregeln, Feldregeln; zählt verlangte Dinge. Verfehlte Pflichtregeln werden zweimal neu gefragt, die Mehrheit gilt.",
      prueft=["alle Pflichtregeln erfüllt"]),
    s("w6", "pruefung", "Köpfe orten", "Auf einem eingeblendeten Koordinatengitter werden alle Köpfe geortet und die erwarteten Figuren zugeordnet."),
    s("w7", "werkzeug", "Variante wählen", "Brauchbar ist eine Variante, die alle Pflichtregeln erfüllt, Platz für alle Blasen hat und die Reihenfolge der Sprecher einhält; gewählt wird die mit den meisten Punkten.",
      prueft=["Pflichtregeln", "Platz für Blasen", "wer zuerst spricht, steht links"], zurueck=("w3", "keine brauchbare Variante: neu malen mit Hinweis aus den verfehlten Regeln, höchstens drei Runden")),
    s("w8", "werkzeug", "Blasen setzen", "Beste Anordnung aller Blasen über den Köpfen, Schrift mindestens 19, Gedanken als Wolke."),
    s("w9", "pruefung", "Schlussprüfung", "Eine weitere Instanz prüft die fertige Kachel: Spitze beim richtigen Sprecher, keine Blase über Gesicht, Geste oder Haupthandlung, alle Worte lesbar, Moment getroffen (mindestens 1 von 2).",
      prueft=["Sprecher richtig", "nichts verdeckt", "lesbar", "Moment"], zurueck=("w8", "zweiter Blasenversuch nur im oberen Band")),
    s("w10", "werkzeug", "Prüfvermerk", "Ergebnis mit Fingerabdruck von Bild, Regeln, Szenenplan und Verfahren im Datensatz; Stufe «geprüft» nur, wenn alle Felder bestanden. Ändert sich etwas, gilt die Prüfung als veraltet.",
      "Prüfstufe im Datensatz"),
]
aq20 = ersetze(ersetze(ohne(aq21, "w6"), "w5", s("w5", "pruefung", "Regeln prüfen", "Dieselbe Instanz beantwortet jede Regel einzeln (allgemein, Figur, Feld), zählt verlangte Dinge und gibt Kopfpositionen an.", prueft=["alle Pflichtregeln erfüllt"])),
               "w7", s("w7", "werkzeug", "Variante wählen", "Brauchbar ist eine Variante, die alle Pflichtregeln erfüllt; gewählt wird die mit den meisten Punkten.", prueft=["Pflichtregeln"],
                       zurueck=("w3", "keine brauchbare Variante: neu malen mit Hinweis, höchstens drei Runden")))
aq20 = ersetze(aq20, "w8", s("w8", "werkzeug", "Blasen setzen", "Blasen nacheinander über oder neben dem Kopf der sprechenden Person."))
aq10 = [
    s("w1", "bearbeitung", "Szenenplan", "Je Bildfeld: Malauftrag, wörtliche Rede aus dem Lesetext, Belege B/R/I."),
    s("w2", "werkzeug", "Zitate", "Jede Blase steht wörtlich im Vers.", prueft=["Zitat wörtlich"], zurueck=("w1", "Abweichung")),
    s("w3", "modell", "Malen", "Das Bildmodell malt Varianten nach Malauftrag, Stilreferenz und Figurenblatt."),
    s("w4", "bearbeitung", "Auswählen und Blasen setzen", "Die bearbeitende Instanz wählt eine Variante und setzt die Blasen."),
    s("w9", "pruefung", "Blindtest", "Eine weitere Instanz beschreibt die fertigen Felder ohne Auftrag; Abweichungen führen zu neuem Malen.", prueft=["Stelle", "Wer-zu-wem", "Figuren"], zurueck=("w3", "Abweichung")),
    s("w10", "bearbeitung", "Prüfvermerk", "Ergebnis und offene Punkte im Datensatz."),
]
P["PROC-BILD-AQUARELL"] = {"names": {"de": "Bilder im Aquarellstil", "en": "Watercolour pictures"}, "group": "bild",
    "purpose_de": "Gemalte Szenen nach dem Styleguide «Visuelle Bibel», geprüft nach festen Regeln, bis kein Mensch mehr drüberschauen muss.",
    "versions": [
        fassung("1.0", "2026-10-27", "Styleguide V1.2 übernommen; Auswahl und Blasen von Hand, Blindtest.", aq10, "Blindtest ohne Abweichung, offene Punkte vermerkt.", docs=["docs/BILDSTIL.md"]),
        fassung("2.0", "2026-10-28", "Automatische Prüfung: Regeln auf drei Ebenen, Wahl der Variante, Blasen und Schlussprüfung ohne Handarbeit.", aq20,
                "Alle Pflichtregeln und die Schlussprüfung bestanden.", regeln=["scripts/authoring/bilder_aquarell_daten/pruefregeln.json@2026-10-28"], docs=["docs/BILDSTIL.md"]),
        fassung("2.1", "2026-10-28", "Köpfe auf Koordinatengitter, Zweitmeinung (Mehrheit aus drei), beste Blasenanordnung, feste Regeln für Platz, Schriftgrösse und Reihenfolge schon bei der Wahl.", aq21,
                "Alle Pflichtregeln und die Schlussprüfung bestanden.", regeln=["scripts/authoring/bilder_aquarell_daten/pruefregeln.json@2026-10-28b"], docs=["docs/BILDSTIL.md"])]}

# ------------------------------------------------------------------ Freigabe
f20 = [
    s("r1", "werkzeug", "Validator", "Schema, IDs, Verweise, Bibelstellen, Quellen, Gleichlauf mit dem Text, Prüfvermerke.", prueft=["keine Fehler"]),
    s("r2", "werkzeug", "App-Tests", "Bau der App und automatische Tests im Browser.", prueft=["alle Tests bestanden"]),
    s("r3", "werkzeug", "Zusammenführen", "Läufe der Bildwerkstatt werden automatisch in den Hauptstand übernommen, wenn alle Prüfungen bestanden sind; bei Widersprüchen bricht das Zusammenführen ab."),
    s("r4", "werkzeug", "Veröffentlichen", "Jeder Stand des Hauptzweigs wird gebaut, geprüft und veröffentlicht; jede Änderung bleibt mit Grund in der Versionsgeschichte."),
    s("r5", "herausgabe", "Grundsätze", "Der Herausgeber entscheidet Grundsätze und offene Fragen; Entscheide stehen mit Datum in der Dokumentation."),
]
P["PROC-FREIGABE"] = {"names": {"de": "Prüfen und veröffentlichen", "en": "Check and publish"}, "group": "freigabe",
    "purpose_de": "Jeder Stand ist geprüft, versioniert und nachvollziehbar.",
    "versions": [
        fassung("1.0", "2026-10-09", "Erste Fassung: bearbeitende Instanz führt Änderungen nach bestandenen Prüfungen zusammen.",
                ersetze(f20, "r3", s("r3", "bearbeitung", "Zusammenführen", "Die bearbeitende Instanz führt geprüfte Änderungen in den Hauptstand.")), "Validator und Tests bestanden.", docs=["AGENTS.md"]),
        fassung("2.0", "2026-10-28", "Bildläufe werden automatisch zusammengeführt, wenn alle Prüfungen bestanden sind (Entscheid Herausgeber).", f20, "Validator und Tests bestanden.", docs=["AGENTS.md"])]}


def aktuelle(pid):
    return P[pid]["versions"][-1]["version"]


def fassung_am(pid, datum):
    """Fassung, die an einem Datum galt (letzte mit valid_from ≤ Datum, sonst die erste)."""
    vs = P[pid]["versions"]
    gilt = [v for v in vs if v["valid_from"] <= (datum or "9999")]
    return (gilt[-1] if gilt else vs[0])["version"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    md = ["# Prozesse", "", "Versionierte Beschreibung, wie gearbeitet wird. Erzeugt aus `scripts/authoring/prozesse.py` (Daten: `data/processes/`);",
          "in der App unter Einstellungen → Prozesse als Ablauf dargestellt. Inhalte verweisen auf die Fassung, nach der sie entstanden sind;",
          "frühere Fassungen bleiben abrufbar.", "", "Rollen: " + "; ".join(f"**{v}**" for v in ROLLEN.values()) + ".", ""]
    for pid, p in P.items():
        rec = {"id": pid, "type": "process", "status": "draft", "tags": [], "names": p["names"], "group": p["group"], "purpose_de": p["purpose_de"],
               "current": p["versions"][-1]["version"], "versions": p["versions"]}
        (OUT / f"{pid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        md += [f"## {p['names']['de']} (`{pid}`)", "", p["purpose_de"], ""]
        for v in reversed(p["versions"]):
            md += [f"### Fassung {v['version']} – gültig ab {v['valid_from']}{' (aktuell)' if v is p['versions'][-1] else ''}", "", f"*Änderung:* {v['change_de']}", ""]
            for i, x in enumerate(v["steps"], 1):
                extra = (f" Prüft: {', '.join(x['checks_de'])}." if x.get("checks_de") else "") + (f" Zurück zu «{next(y['title_de'] for y in v['steps'] if y['id'] == x['back']['to'])}», wenn {x['back']['when_de']}." if x.get("back") else "")
                md.append(f"{i}. **{x['title_de']}** ({ROLLEN[x['role']]}): {x['do_de']}{extra}")
            md += ["", f"*Weiter, wenn:* {v['gate_de']}"] + ([f"*Stand:* {v['limits_de']}"] if v.get("limits_de") else []) + \
                  ([f"*Regeln:* {', '.join(v['rules'])}"] if v.get("rules") else []) + ([f"*Ausführlich:* {', '.join(v['docs'])}"] if v.get("docs") else []) + [""]
    (ROOT / "docs/PROZESSE.md").write_text("\n".join(md), encoding="utf-8")
    print(f"PASS: {len(P)} Prozesse, {sum(len(p['versions']) for p in P.values())} Fassungen")


if __name__ == "__main__":
    main()
