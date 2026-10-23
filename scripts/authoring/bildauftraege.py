#!/usr/bin/env python3
"""Autorenwerkzeug: Bildaufträge (Typ illustration_brief) – stilunabhängig, je Stelle.

Ein Bildauftrag hält fest, wer im Bild ist (IDs aus dem Bildlexikon data/illustrations/lexicon/), was geschieht, wer zu wem
spricht (Sprechblasen mit Zeichen statt Wörtern) und in welcher Reihenfolge (Bildfelder). Er wird wie eine Zusammenfassung
gegen den Text geprüft; jeder Bildstil (Symbol, Skizze, später Generator) setzt denselben Auftrag um. Die Bildunterschrift
eines Felds ist der Bibeltext der genannten Verse in der gewählten Lesefassung (nicht hier gespeichert).

Gleichlauf mit dem Text: `basis` speichert Fingerabdrücke des Textes, gegen den der Auftrag geprüft wurde (Verse der
hochdeutschen Arbeitsübersetzung und Zusammenfassung des Ziels). Ändert sich der Text, meldet der Validator den Auftrag als
veraltet. Erst nach erneuter Prüfung werden die Fingerabdrücke erneuert:
    BIBLE_BRIEF_CONFIRM=1 python3 scripts/authoring/bildauftraege.py
Ohne diese Bestätigung übernimmt das Werkzeug die gespeicherten Fingerabdrücke unverändert.

KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung.
"""
import json
import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from _lib import D, localize, write  # noqa: E402
import localizations  # noqa: E402
import refs as _refs  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-14; Mundart noch nicht muttersprachlich geprüft."


def P(n, ref, figures, action, speech=(), objects=(), signs=(), stage=None):
    d = {"n": n, "reference": ref, "figures": list(figures), "objects": list(objects), "signs": list(signs),
         "speech": [{"from": a, "to": b, "icons": list(i)} for a, b, i in speech], "action_de": action}
    if stage:
        d["stage"] = stage
    return d


J, M, DI, SM, BR, BG, GA, JU = ("FIG-JESUS", "FIG-MARIA-MUTTER-JESU", "FIG-ROLLE-DIENER", "FIG-ROLLE-SPEISEMEISTER",
                               "FIG-ROLLE-BRAEUTIGAM", "FIG-ROLLE-BRAUT", "FIG-ROLLE-GAST", "FIG-ROLLE-JUENGER")
BRIEFS = [
    {"suffix": "JHN-002-001-012", "level": "section", "reference": "JHN.2.1-JHN.2.12", "target": "TU-JHN-002-001-012",
     "translation": "TRANS-JHN-002-001-025-DE-WORKING",
     "panels": [
         P(1, "JHN.2.3-JHN.2.4", [M, J, BG, BR, GA], "Bei der Hochzeit sagt Maria zu Jesus, dass der Wein ausgegangen ist; Jesus antwortet, seine Stunde sei noch nicht gekommen.",
           speech=[(M, J, ["FIG-OBJ-KRUG-WEIN-LEER", "FIG-OBJ-BECHER-LEER", "FIG-ZEICHEN-FEHLT"]), (J, M, ["FIG-ZEICHEN-STUNDE"])], signs=["FIG-ZEICHEN-HOCHZEIT"]),
         P(2, "JHN.2.5", [M, DI], "Maria sagt zu den Dienern, sie sollen tun, was Jesus ihnen sagt.",
           speech=[(M, DI, ["FIG-JESUS", "FIG-ZEICHEN-HOEREN"])]),
         P(3, "JHN.2.6-JHN.2.8", [J, DI], "Jesus lässt die sechs steinernen Krüge mit Wasser füllen und schickt die Diener zum Speisemeister.",
           speech=[(J, DI, ["FIG-OBJ-KRUG-WASSER", "FIG-ZEICHEN-BRINGEN", "FIG-ROLLE-SPEISEMEISTER"])], objects=["FIG-OBJ-KRUG-WASSER"]),
         P(4, "JHN.2.9-JHN.2.11", [DI, SM, BG, J, JU], "Der Speisemeister kostet den Wein und spricht zum Bräutigam vom guten Wein; es ist der Anfang der Zeichen, die Jünger glauben an Jesus.",
           speech=[(SM, BG, ["FIG-OBJ-BECHER-VOLL", "FIG-ZEICHEN-FREUDE"])], objects=["FIG-OBJ-BECHER-VOLL", "FIG-OBJ-KRUG-WEIN"],
           signs=["FIG-ZEICHEN-FREUDE", "FIG-ZEICHEN-STERN", "FIG-ZEICHEN-GLAUBEN"]),
     ],
     "note": "Braut und Gäste sind im Text nicht genannt bzw. handeln nicht; sie zeigen nur den Ort «Hochzeit». "
             "Die Sprechblasen fassen das Gesagte in Zeichen; der Wortlaut steht als Bildunterschrift. Der Wechsel des Wassers in Wein wird "
             "nicht als Vorgang gezeigt, weil der Text ihn nicht erzählt ([[JHN.2.9]]: «das Wasser, das zu Wein geworden war»).",
     "note_gsw": "D Brut und d Gäscht nännt de Text nöd bzw. si handled nöd; si zeiged nu de Ort «Hochziit». "
                 "D Sprächblase fassed s Gseit i Zeiche; de Wortlut staat als Bildunderschrift. Wie s Wasser zu Wii wird, zeigt s Bild nöd, "
                 "wil de Text das nöd verzellt ([[JHN.2.9]]: «s Wasser, wo zu Wii worde isch»)."},
    {"suffix": "JHN-002-013-022", "level": "section", "reference": "JHN.2.13-JHN.2.22", "target": "TU-JHN-002-013-022",
     "translation": "TRANS-JHN-002-001-025-DE-WORKING",
     "panels": [
         P(1, "JHN.2.14-JHN.2.16", [J, "FIG-ROLLE-HAENDLER"], "Jesus treibt mit einer Geissel die Händler, Schafe und Rinder aus dem Tempel, schüttet die Münzen aus und stösst die Tische um.",
           speech=[(J, "FIG-ROLLE-HAENDLER", ["FIG-ORT-TEMPEL", "FIG-OBJ-MUENZEN", "FIG-ZEICHEN-FEHLT"])],
           objects=["FIG-ORT-TEMPEL", "FIG-OBJ-PEITSCHE", "FIG-OBJ-MUENZEN", "FIG-OBJ-SCHAF", "FIG-OBJ-TAUBE"]),
         P(2, "JHN.2.18-JHN.2.19", ["FIG-GRUPPE-MENGE", J], "Die Juden fragen nach einem Zeichen; Jesus antwortet: Reisst diesen Tempel nieder, in drei Tagen werde ich ihn aufrichten.",
           speech=[("FIG-GRUPPE-MENGE", J, ["FIG-ZEICHEN-STERN", "FIG-ZEICHEN-FRAGEN"]), (J, "FIG-GRUPPE-MENGE", ["FIG-GRUPPE-MENGE", "FIG-ZEICHEN-NIEDERREISSEN", "FIG-ZEICHEN-TAGE", J, "FIG-ORT-TEMPEL"])],
           objects=["FIG-ORT-TEMPEL"]),
     ],
     "note": "Ob Jesus die Geissel gegen Menschen oder nur gegen die Tiere gebraucht, lässt [[JHN.2.15]] offen; das Bild zeigt sie erhoben, ohne Schlag. "
             "Die Fragenden («die Juden», [[JHN.2.18]]) erscheinen als neutrale Menge, ohne Merkmale einer Volksgruppe. Dass Jesus vom Tempel seines Leibes "
             "spricht ([[JHN.2.21]]), sagt der Erzähler; das Bild deutet es nicht aus. Für «in drei Tagen» stehen drei Sonnen, für «niederreissen» der Tempel mit Riss; die kleine Menge vor dem Riss steht für «ihr», der Kopf Jesu vor dem heilen Tempel für «ich».",
     "note_gsw": "Öb de Jesus d Geissle gäge Mänsche oder nu gäge d Tier bruucht, laat [[JHN.2.15]] offe; s Bild zeigt si ufgha, ohni Schlag. "
                 "Die, wo fröged («d Jude», [[JHN.2.18]]), erschiined als neutrali Mängi, ohni Merkmal vo ere Volksgruppe. Dass de Jesus vom Tämpel "
                 "vo sim Liib redt ([[JHN.2.21]]), seit de Erzäller; s Bild düütet das nöd uus. Für «i drüü Täg» staand drüü Sunne, für «abriisse» de Tämpel mit Riss; di chli Mängi vor em Riss staat für «ihr», de Chopf vom Jesus vor em ganze Tämpel für «ich»."},
    {"suffix": "JHN-002-023-025", "level": "section", "reference": "JHN.2.23-JHN.2.25", "target": "TU-JHN-002-023-025",
     "translation": "TRANS-JHN-002-001-025-DE-WORKING",
     "panels": [
         P(1, "JHN.2.23-JHN.2.25", ["FIG-GRUPPE-MENGE", J], "Viele in Jerusalem glauben wegen der Zeichen an Jesus; er vertraut sich ihnen nicht an, weil er weiss, was im Menschen ist.",
           objects=["FIG-ORT-TEMPEL"], signs=["FIG-ZEICHEN-STERN", "FIG-ZEICHEN-GLAUBEN", "FIG-ZEICHEN-ABSTAND"]),
     ],
     "note": "Die gestrichelte Linie steht für [[JHN.2.24]]: Jesus vertraute sich ihnen nicht an. Das Bild bewertet die Menge nicht; die Begründung gibt der Text in [[JHN.2.25]].",
     "note_gsw": "D gstrichleti Linie staat für [[JHN.2.24]]: De Jesus hät sich ine nöd aavertrout. S Bild wertet d Mängi nöd; de Grund git de Text i [[JHN.2.25]]."},
    {"suffix": "JHN-002", "level": "chapter", "reference": "JHN.2", "target": "SUM-CH-JHN-002", "translation": None,
     "panels": [
         P(1, "JHN.2.1-JHN.2.11", [J, BR, BG], "Hochzeit zu Kana: Das Wasser in den Krügen ist zu Wein geworden – der Anfang der Zeichen.",
           objects=["FIG-OBJ-KRUG-WASSER", "FIG-OBJ-KRUG-WEIN"], signs=["FIG-ZEICHEN-HOCHZEIT", "FIG-ZEICHEN-STERN"]),
         P(2, "JHN.2.13-JHN.2.22", [J, "FIG-ROLLE-HAENDLER"], "Jesus treibt die Händler aus dem Tempel."),
         P(3, "JHN.2.23-JHN.2.25", ["FIG-GRUPPE-MENGE", J], "Viele glauben wegen der Zeichen; Jesus vertraut sich ihnen nicht an.",
           signs=["FIG-ZEICHEN-STERN", "FIG-ZEICHEN-GLAUBEN", "FIG-ZEICHEN-ABSTAND"]),
     ],
     "note": "Je ein Feld aus den drei Abschnitten des Kapitels; Einzelheiten dort. Das erste Feld zeigt nur das Ergebnis ([[JHN.2.9]]: «das Wasser, das zu Wein geworden war»), nicht den Vorgang.",
     "note_gsw": "Je es Fäld us de drüü Abschnitt vom Kapitel; Einzelheite lueg dört. S erscht Fäld zeigt nu s Ergäbnis ([[JHN.2.9]]: «s Wasser, wo zu Wii worde isch»), nöd de Vorgang."},
    {"suffix": "JHN", "level": "book", "reference": "JHN", "target": "SUM-BOOK-JHN", "translation": None,
     "panels": [P(1, "JHN", [], "Adler (Evangelistensymbol), Licht, Schriftrolle.", objects=["FIG-OBJ-SCHRIFTROLLE"],
                 signs=["FIG-SYMBOL-ADLER", "FIG-ZEICHEN-LICHT"])],
     "note": "Der Adler ist seit der Alten Kirche das Symbol des Evangelisten Johannes; Licht und Schriftrolle nehmen den Anfang auf («Im Anfang war das Wort», «das Licht der Menschen»). "
             "Die Zuordnung der Tiere zu den Evangelisten ist Tradition, nicht Text.",
     "note_gsw": "De Adler isch sit de Alte Chile s Symbol vom Evangelischt Johannes; Liecht und Schriftrolle nämed de Aafang uf («Im Aafang isch s Wort gsii», «s Liecht vo de Mänsche»). "
                 "D Zuedornig vo de Tier zu de Evangelischte isch Tradition, nöd Text."},
]


G, HG, MOSE, PAU, PR, KO, SO, ME, GEM = ("FIG-GOTT", "FIG-HEILIGER-GEIST", "FIG-MOSE", "FIG-PAULUS", "FIG-ROLLE-PROPHET", "FIG-ROLLE-KOENIG",
                                       "FIG-ROLLE-SOLDAT", "FIG-GRUPPE-MENGE", "FIG-GRUPPE-GEMEINDE")
TAF, BERG, MEER, JER, KREUZ, GRAB, ROLLE, BRIEF, LEIER, BOOT = ("FIG-OBJ-GESETZESTAFELN", "FIG-ORT-BERG", "FIG-ORT-MEER", "FIG-ORT-JERUSALEM",
                                                                "FIG-OBJ-KREUZ", "FIG-ORT-GRAB", "FIG-OBJ-SCHRIFTROLLE", "FIG-OBJ-BRIEF", "FIG-OBJ-LEIER", "FIG-OBJ-BOOT")
Z = lambda x: "FIG-ZEICHEN-" + x  # noqa: E731

# Gemeinsame Felder der oberen Ebenen (gleiche Szene = gleiches Feld im Bild)
F_SCHOEPFUNG = lambda n: P(n, "GEN.1", [G], "Schöpfung: Gott spricht, und es wird Licht; Himmel und Erde, Pflanzen, Sonne, Mond und Sterne entstehen.",  # noqa: E731
                           speech=[(G, Z("SCHOEPFUNG"), [Z("LICHT")])], signs=[Z("SCHOEPFUNG")])
F_MEER = lambda n: P(n, "EXO.14", [MOSE, ME], "Befreiung: Mose führt das Volk auf trockenem Boden durch das geteilte Meer.", objects=[MEER])  # noqa: E731
F_BERG = lambda n, meer=False: P(n, "EXO.19-EXO.34", [G, MOSE, ME],  # noqa: E731
                                 ("Nach dem Weg durch das Meer gibt Gott am Berg die Weisung; Mose bringt die Tafeln zum Volk." if meer else
                                  "Gott und Israel: Am Berg gibt Gott die Weisung; Mose bringt die Tafeln zum Volk."),
                                 speech=[(G, MOSE, [TAF])], objects=[BERG, TAF] + ([MEER] if meer else []))
F_EXIL = lambda n, ref, act: P(n, ref, [G, PR, ME], act, speech=[(PR, ME, [Z("HOFFNUNG")])], objects=[JER],  # noqa: E731
                               signs=[Z("NIEDERREISSEN"), Z("EXIL"), Z("TRAUER"), Z("HOFFNUNG")])
F_KREUZ = lambda n, jesus: P(n, "MRK.15-MRK.16", [J] if jesus else [],  # noqa: E731
                             "Jesus: sein Leben, sein Tod am Kreuz und das leere Grab (Auferstehung)." if jesus else
                             "Jesus stirbt am Kreuz; das Grab ist leer: Er ist auferweckt.", objects=[KREUZ, GRAB])
F_VERKUENDET = lambda n, vier=False: P(n, "MRK.1.14-MRK.1.15", [J, ME],  # noqa: E731
                                       ("Vier Evangelien erzählen von Jesus. Er verkündet die Nähe von Gottes Reich und ruft: Kehrt um und glaubt." if vier else
                                        "Jesus verkündet die Nähe von Gottes Reich und ruft: Kehrt um und glaubt."),
                                       speech=[(J, ME, [G, Z("UMKEHR"), Z("GLAUBEN")])], objects=[ROLLE] if vier else [])
F_NEU = lambda n, menge=False: P(n, "REV.21.1-REV.21.4", [G] + ([ME] if menge else []),  # noqa: E731
                                 ("Am Ende: Gott wohnt bei den Menschen in der erneuerten Schöpfung; Trauer ist vorbei." if menge else
                                  "Hoffnung auf eine erneuerte Schöpfung: die Stadt im Licht, in der Gott bei den Menschen wohnt."),
                                 signs=[Z("NEUE-SCHOEPFUNG")] + ([Z("FREUDE")] if menge else []))
F_PROPHET = lambda n, ref, zwoelf=False: P(n, ref, [G, PR, ME],  # noqa: E731
                                           ("Zwölf Prophetenbücher: Ein Prophet klagt Unrecht an und ruft zu Recht und Umkehr." if zwoelf else
                                            "Ein Prophet klagt Unrecht an und ruft zur Umkehr."),
                                           speech=[(PR, ME, [Z("GERICHT"), Z("UMKEHR")])], objects=[ROLLE] if zwoelf else [])

UPPER = [
    ("BIBLE", "bible", "SUM-BIBLE", [
        F_BERG(1), F_KREUZ(2, True), F_NEU(3),
        P(4, "2TI.3.16", [PR], "Viele Stimmen: Erzählungen und Weisheit, Gebete und Lieder, prophetische Rede, Briefe.", objects=[ROLLE, LEIER, BRIEF])],
     ""
     "Dass diese Geschichte zusammengehört, ist christliche Lesart, wie die Zusammenfassung selbst sagt. Das Gottessymbol (Strahlenkranz mit dem Gottesnamen) zeigt Gott, ohne ihn abzubilden.",
     ""
     "Dass die Gschicht zämeghört, isch christlichi Läsart, wie s d Zämefassig sälber seit. S Gottessymbol (Strahlechranz mit em Gottesname) zeigt Gott, ohni en abzbilde."),
    ("OT", "testament", "SUM-OT", [
        F_SCHOEPFUNG(1), F_MEER(2), F_BERG(3),
        F_EXIL(4, "JER.29.4-JER.29.14", "Scheitern und Neubeginn: Jerusalem ist zerstört, das Volk weggeführt und klagt; ein Prophet kündigt Hoffnung und Rückkehr an.")],
     "Klage und Weisheit sowie die prophetische Kritik zeigen die Bilder der Buchgruppen genauer. "
     "Die Menge steht für das Volk Israel, ohne Merkmale einer Volksgruppe.",
     "Klag und Wiisheit und di prophetisch Kritik zeiged d Bilder vo de Buechgruppe gnauer. "
     "D Mängi staat für s Volk Israel, ohni Merkmal vo ere Volksgruppe."),
    ("NT", "testament", "SUM-NT", [
        F_VERKUENDET(1), F_KREUZ(2, False),
        P(3, "ACT.1.8", [HG, "FIG-ROLLE-JUENGER", GEM], "Der Geist kommt auf die Jünger; die Botschaft breitet sich aus, Gemeinden entstehen und erhalten Briefe.",
          objects=[BRIEF], signs=[Z("AUSBREITEN")]),
        P(4, "REV.20.11-REV.21.4", [G], "Offenbarung: Gericht und Hoffnung auf eine neue Schöpfung.", signs=[Z("GERICHT"), Z("NEUE-SCHOEPFUNG")])],
     "Das leere Grab steht für die Auferstehung; "
     "der auferstandene Jesus selbst ist nicht gezeichnet.",
     "S lääre Grab staat für d Uferstehig; "
     "de uferstandni Jesus sälber isch nöd zeichnet."),
    ("GROUP-01", "group", "SUM-GROUP-01", [
        F_SCHOEPFUNG(1),
        P(2, "GEN.15.5", [G, "FIG-ABRAHAM"], "Verheissung: Gott verheisst Abraham Nachkommen, so zahlreich wie die Sterne, und ein Land.",
          speech=[(G, "FIG-ABRAHAM", [Z("VERHEISSUNG")])], stage={"god_side": "left", "mood": {"FIG-ABRAHAM": "surprised"}, "x": {"FIG-ABRAHAM": 130}}),
        F_BERG(3, meer=True)],
     "Abraham steht für die Erzeltern, denen Gott Nachkommen und Land verheisst ([[GEN.12.1-GEN.12.3]], [[GEN.15.5]]). Dass die Tora vor dem Einzug ins Land endet, zeigt das Bild nicht.",
     "De Abraham staat für d Erzeltere, wo Gott Nachkomme und Land verheisst ([[GEN.12.1-GEN.12.3]], [[GEN.15.5]]). Dass d Tora vor em Iizug is Land ufhört, zeigt s Bild nöd."),
    ("GROUP-02", "group", "SUM-GROUP-02", [
        P(1, "JOS.3.14-JOS.3.17", [ME], "Landnahme: Israel zieht über den Jordan in das Land.", objects=["FIG-ORT-LAND"],
          stage={"x": {ME: 40}, "mood": {ME: "smile"}, "arrows": [[ME, "FIG-ORT-LAND", "go"]]}),
        P(2, "2SA.5.1-2SA.5.10", [KO, ME], "Israel lebt im Land; ein König herrscht in Jerusalem.", objects=[JER]),
        P(3, "2KI.25.8-2KI.25.11", [ME], "Jerusalem wird zerstört und das Volk weggeführt.", objects=[JER],
          signs=[Z("NIEDERREISSEN"), Z("EXIL"), Z("TRAUER")]),
        P(4, "NEH.2.17-NEH.2.18", [ME], "Rückkehr: Menschen kehren zurück und bauen Jerusalem wieder auf.", objects=[JER],
          signs=[Z("AUFBAUEN"), Z("FREUDE")], stage={"mood": {ME: "delight"}, "back_side": "right", "at": {Z("AUFBAUEN"): JER}})],
     "Vier Stationen nach der Zusammenfassung: Landnahme, Königszeit, Zusammenbruch, Rückkehr (Esra, Nehemia).",
     "Vier Statione nach de Zämefassig: Landnahm, Chünigsziit, Zämebruch, Rückchehr (Esra, Nehemia)."),
    ("GROUP-03", "group", "SUM-GROUP-03", [
        P(1, "PSA.13", [ME, G], "Gebete: Klage und Lob vor Gott.", speech=[(ME, G, [Z("TRAUER"), Z("FREUDE")])],
          objects=[LEIER]),
        P(2, "SNG.2", ["FIG-ROLLE-BRAUT", "FIG-ROLLE-BRAEUTIGAM"], "Liebesdichtung: Braut und Bräutigam.", signs=[Z("HOCHZEIT"), Z("FREUDE")]),
        P(3, "ECC.3.1-ECC.3.8", [ME], "Weisheit: Nachdenken über Gerechtigkeit und Vergänglichkeit; alles hat seine Zeit.",
          objects=[ROLLE], signs=[Z("STUNDE"), Z("GERICHT")])],
     "Die Waage steht hier für Gerechtigkeit, die Sanduhr für Vergänglichkeit.",
     "Drüü Fälder: Psalme, Hoheliid, Wiisheit (Sprüch, Hiob, Prediger). D Waag staat da für Gerächtigkeit, d Sanduhr für Vergänglichkeit."),
    ("GROUP-04", "group", "SUM-GROUP-04", [
        F_PROPHET(1, "ISA.1.16-ISA.1.17"),
        F_EXIL(2, "ISA.40.1-ISA.40.2", "Nach dem Zusammenbruch Jerusalems und im Exil kündigt ein Prophet Trost und Hoffnung an.")],
     "Der Prophet ist eine Rollenfigur für Jesaja, Jeremia, Ezechiel und Daniel.",
     "De Prophet isch e Rollefigur für Jesaja, Jeremia, Ezechiel und Daniel."),
    ("GROUP-05", "group", "SUM-GROUP-05", [
        F_PROPHET(1, "AMO.5.14-AMO.5.24", zwoelf=True),
        P(2, "AMO.9.13-AMO.9.15", [G, ME], "Gott bleibt treu: Wiederaufbau und neues Wachstum.", objects=[JER], signs=[Z("HOFFNUNG"), Z("FREUDE")])],
     "",
     ""),
    ("GROUP-06", "group", "SUM-GROUP-06", [F_VERKUENDET(1, vier=True), F_KREUZ(2, False)],
     "",
     ""),
    ("GROUP-07", "group", "SUM-GROUP-07", [
        P(1, "ACT.2.1-ACT.2.4", [HG, "FIG-ROLLE-JUENGER"], "In Jerusalem kommt der Geist auf die Jünger; Zungen wie von Feuer erscheinen auf ihnen.", objects=[JER],
          signs=[Z("FEUERZUNGEN")]),
        P(2, "ACT.28.14-ACT.28.16", [PAU, SO], "Die Botschaft geht von Jerusalem hinaus, bis nach Rom; dort wird Paulus bewacht.",
          objects=[JER, "FIG-ORT-ROM"], signs=[Z("AUSBREITEN")])],
     "Der Soldat steht für die Bewachung des Paulus in Rom ([[ACT.28.16]]).",
     "De Soldat staat für d Bewachig vom Paulus z Rom ([[ACT.28.16]])."),
    ("GROUP-08", "group", "SUM-GROUP-08", [
        P(1, "PHP.1.1-PHP.1.11", [PAU, GEM], "Paulus schreibt Gemeinden Briefe: die Botschaft von Christus für ihr Zusammenleben.",
          speech=[(PAU, GEM, [KREUZ, Z("GLAUBEN")])], objects=[BRIEF])],
     "Das Kreuz steht für die Botschaft von Christus. Ob alle Briefe von Paulus selbst stammen, ist in der Forschung umstritten («unter dem Namen des Paulus überliefert»).",
     "S Chrüz staat für d Botschaft vo Christus. Öb alli Brief vom Paulus sälber stammed, isch i de Forschig umstritte («under em Name vom Paulus überliferet»)."),
    ("GROUP-09", "group", "SUM-GROUP-09", [
        P(1, "HEB.10.23-HEB.10.25", ["FIG-ROLLE-BOTE", GEM], "Weitere Briefe ermutigen Gemeinden: am Glauben festhalten, ausharren, einander lieben und Lehren prüfen.",
          speech=[("FIG-ROLLE-BOTE", GEM, [Z("GLAUBEN"), Z("AUSDAUER"), Z("LIEBE"), Z("PRUEFEN")])],
          stage={"x": {"FIG-ROLLE-BOTE": 40}})],
     "Ein Bote liest einer Hausgemeinde einen Brief vor; die Zeichen nennen die wiederkehrenden Themen. Wer die Briefe schrieb, lässt das Bild offen (Hebräerbrief ohne Verfasserangabe).",
     "En Bott list ere Huusgmeind en Brief vor; d Zeiche nänned di wiederkehrende Theme. Wer d Brief gschribe hät, laat s Bild offe (Hebräerbrief ohni Verfasser)."),
    ("GROUP-10", "group", "SUM-GROUP-10", [
        P(1, "REV.4.1-REV.4.11", [G, KO, SO, ME], "Visionen: Über Bedrängnis und Weltmacht steht Gottes Herrschaft.", signs=[Z("TRAUER")]),
        F_NEU(2, menge=True)],
     "König und Soldat stehen für Weltmacht allgemein, nicht für eine bestimmte Macht; "
     "die Tierbilder der Offenbarung sind nicht gezeichnet.",
     "Chünig und Soldat staand für Wältmacht allgemein, nöd für e bestimmti Macht; "
     "d Tierbilder vo de Offebarig sind nöd zeichnet."),
]
for suffix, lvl, target, panels, note, note_g in UPPER:
    BRIEFS.append({"suffix": suffix, "level": lvl, "reference": None, "target": target, "translation": None, "panels": panels,
                   "note": note, "note_gsw": note_g, "tags": []})


ACTIONS_GSW = {'Bei der Hochzeit sagt Maria zu Jesus, dass der Wein ausgegangen ist; Jesus antwortet, seine Stunde sei noch nicht gekommen.': 'A de Hochziit seit d Maria zum Jesus, de Wii seg usgange; de Jesus antwortet, sini Stund seg no nöd choo.', 'Maria sagt zu den Dienern, sie sollen tun, was Jesus ihnen sagt.': 'D Maria seit de Diener, si söled mache, was de Jesus ine säg.', 'Jesus lässt die sechs steinernen Krüge mit Wasser füllen und schickt die Diener zum Speisemeister.': 'De Jesus laat di sächs steinige Chrüeg mit Wasser fülle und schickt d Diener zum Spiismeischter.', 'Der Speisemeister kostet den Wein und spricht zum Bräutigam vom guten Wein; es ist der Anfang der Zeichen, die Jünger glauben an Jesus.': 'De Spiismeischter probiert de Wii und redt mit em Brüütigam vom guete Wii; das isch de Aafang vo de Zeiche, d Jünger glaubed a de Jesus.', 'Jesus treibt mit einer Geissel die Händler, Schafe und Rinder aus dem Tempel, schüttet die Münzen aus und stösst die Tische um.': 'De Jesus tribt mit ere Geissle d Händler, d Schaf und d Rinder us em Tämpel, schüttet s Münz us und heit d Tisch um.', 'Die Juden fragen nach einem Zeichen; Jesus antwortet: Reisst diesen Tempel nieder, in drei Tagen werde ich ihn aufrichten.': 'D Jude fröged nach eme Zeiche; de Jesus antwortet: Riissed dä Tämpel ab, i drüü Täg stell ich en uf.', 'Viele in Jerusalem glauben wegen der Zeichen an Jesus; er vertraut sich ihnen nicht an, weil er weiss, was im Menschen ist.': 'Vili z Jerusalem glaubed wäge de Zeiche a de Jesus; er vertrout sich ine nöd aa, wil er weiss, was im Mänsch isch.', 'Hochzeit zu Kana: Das Wasser in den Krügen ist zu Wein geworden – der Anfang der Zeichen.': 'Hochziit z Kana: S Wasser i de Chrüeg isch zu Wii worde – de Aafang vo de Zeiche.', 'Jesus treibt die Händler aus dem Tempel.': 'De Jesus tribt d Händler us em Tämpel.', 'Viele glauben wegen der Zeichen; Jesus vertraut sich ihnen nicht an.': 'Vili glaubed wäge de Zeiche; de Jesus vertrout sich ine nöd aa.', 'Adler (Evangelistensymbol), Licht, Schriftrolle.': 'Adler (Symbol vom Evangelischt), Liecht, Schriftrolle.'}


ACTIONS_GSW.update({'Gott und Israel: Am Berg gibt Gott die Weisung; Mose bringt die Tafeln zum Volk.': 'Gott und Israel: Am Bärg git Gott d Wiisig; de Mose bringt d Tafle zum Volk.', 'Jesus: sein Leben, sein Tod am Kreuz und das leere Grab (Auferstehung).': 'De Jesus: sis Läbe, sin Tod am Chrüz und s lääre Grab (Uferstehig).', 'Hoffnung auf eine erneuerte Schöpfung: die Stadt im Licht, in der Gott bei den Menschen wohnt.': 'Hoffnig uf e nöii Schöpfig: d Stadt im Liecht, wo Gott bi de Mänsche wohnt.', 'Viele Stimmen: Erzählungen und Weisheit, Gebete und Lieder, prophetische Rede, Briefe.': 'Vili Stimme: Verzällige und Wiisheit, Gebät und Lieder, prophetischi Red, Brief.', 'Schöpfung: Gott spricht, und es wird Licht; Himmel und Erde, Pflanzen, Sonne, Mond und Sterne entstehen.': 'Schöpfig: Gott redt, und s wird Liecht; Himmel und Erde, Pflanze, Sunne, Mond und Stärn entstönd.', 'Befreiung: Mose führt das Volk auf trockenem Boden durch das geteilte Meer.': 'Befreiig: De Mose füert s Volk uf tröchnem Bode dur s teilte Meer.', 'Scheitern und Neubeginn: Jerusalem ist zerstört, das Volk weggeführt und klagt; ein Prophet kündigt Hoffnung und Rückkehr an.': 'Schiitere und Neuaafang: Jerusalem isch zerstört, s Volk wäggfüert und klagt; en Prophet chündet Hoffnig und Rückchehr aa.', 'Jesus verkündet die Nähe von Gottes Reich und ruft: Kehrt um und glaubt.': 'De Jesus verchündet, dass Gottes Riich nöch isch, und rüeft: Chered um und glaubed.', 'Jesus stirbt am Kreuz; das Grab ist leer: Er ist auferweckt.': 'De Jesus stirbt am Chrüz; s Grab isch läär: Er isch uferweckt.', 'Der Geist kommt auf die Jünger; die Botschaft breitet sich aus, Gemeinden entstehen und erhalten Briefe.': 'De Geischt chunnt uf d Jünger; d Botschaft breitet sich uus, Gmeinde entstönd und überchömed Brief.', 'Offenbarung: Gericht und Hoffnung auf eine neue Schöpfung.': 'Offebarig: Gricht und Hoffnig uf e nöii Schöpfig.', 'Nach dem Weg durch das Meer gibt Gott am Berg die Weisung; Mose bringt die Tafeln zum Volk.': 'Nach em Wäg dur s Meer git Gott am Bärg d Wiisig; de Mose bringt d Tafle zum Volk.', 'Israel lebt im Land; ein König herrscht in Jerusalem.': 'Israel läbt im Land; en Chünig regiert z Jerusalem.', 'Jerusalem wird zerstört und das Volk weggeführt; später kehren Menschen zurück.': 'Jerusalem wird zerstört und s Volk wäggfüert; spöter chömed Mänsche zrugg.', 'Gebete: Klage und Lob vor Gott.': 'Gebät: Klag und Lob vor Gott.', 'Liebesdichtung: Braut und Bräutigam.': 'Liebesdichtig: Brut und Brüütigam.', 'Weisheit: Nachdenken über Gerechtigkeit und Vergänglichkeit; alles hat seine Zeit.': 'Wiisheit: Nachedänke über Gerächtigkeit und Vergänglichkeit; alles hät sini Ziit.', 'Ein Prophet klagt Unrecht an und ruft zur Umkehr.': 'En Prophet klagt Unrächt aa und rüeft zur Umchehr.', 'Nach dem Zusammenbruch Jerusalems und im Exil kündigt ein Prophet Trost und Hoffnung an.': 'Nach em Zämebruch vo Jerusalem und im Exil chündet en Prophet Troscht und Hoffnig aa.', 'Zwölf Prophetenbücher: Ein Prophet klagt Unrecht an und ruft zu Recht und Umkehr.': 'Zwölf Prophetebüecher: En Prophet klagt Unrächt aa und rüeft zu Rächt und Umchehr.', 'Gott bleibt treu: Wiederaufbau und neues Wachstum.': 'Gott bliibt treu: Widerufbau und nöis Wachstum.', 'Vier Evangelien erzählen von Jesus. Er verkündet die Nähe von Gottes Reich und ruft: Kehrt um und glaubt.': 'Vier Evangelie verzälled vom Jesus. Er verchündet, dass Gottes Riich nöch isch, und rüeft: Chered um und glaubed.', 'In Jerusalem kommt der Geist auf die Jünger.': 'Z Jerusalem chunnt de Geischt uf d Jünger.', 'Die Botschaft geht hinaus, bis nach Rom; Paulus reist und wird bewacht.': 'D Botschaft gaat use, bis uf Rom; de Paulus reist und wird bewacht.', 'Paulus schreibt Gemeinden Briefe: die Botschaft von Christus für ihr Zusammenleben.': 'De Paulus schriibt Gmeinde Brief: d Botschaft vo Christus für ires Zämeläbe.', 'Weitere Briefe ermutigen Gemeinden: am Glauben festhalten, ausharren und einander lieben.': 'Wiiteri Brief mached Gmeinde Muet: am Glaube feschthebe, uushalte und enand gern ha.', 'Visionen: Über Bedrängnis und Weltmacht steht Gottes Herrschaft.': 'Visione: Über Bedrängnis und Wältmacht staat Gottes Herrschaft.', 'Am Ende: Gott wohnt bei den Menschen in der erneuerten Schöpfung; Trauer ist vorbei.': 'Am Änd: Gott wohnt bi de Mänsche i de nöie Schöpfig; d Truur isch verbii.'})


# Bildhilfe je Feld für die Legende: Kurztitel, was man sieht, wofür die Zeichen stehen (kompakt; ergänzt action_de, die Handlung nach dem Text)
CAPTIONS = {'BIBLE': [('Sinai: Gott (Strahlenkranz) spricht und gibt die Tafeln; Mose bringt sie dem Volk.', 'Sinai: Gott (Strahlechranz) redt und git d Tafle; de Mose bringt si em Volk.'), ('Jesus: sein Leben, sein Tod am Kreuz und das leere Grab (Auferstehung).', 'Jesus: sis Läbe, sin Tod am Chrüz und s lääre Grab (Uferstehig).'), ('Neue Schöpfung: die leuchtende Stadt mit Strom und Baum; Gott wohnt bei den Menschen.', 'Nöii Schöpfig: di lüüchtend Stadt mit Strom und Baum; Gott wohnt bi de Mänsche.'), ('Viele Stimmen: Erzählung und Weisheit (Rolle), Gebet und Lied (Leier), Prophetie (Prophet), Briefe.', 'Vili Stimme: Verzällig und Wiisheit (Rolle), Gebät und Lied (Leier), Prophetie (Prophet), Brief.')], 'OT': [('Schöpfung: Gott spricht «Licht» (Sprechblase); Erde, Pflanzen, Sonne, Mond und Sterne entstehen.', 'Schöpfig: Gott redt «Liecht» (Sprächblase); Erde, Pflanze, Sunne, Mond und Stärn entstönd.'), ('Befreiung: Mose führt das Volk durch das geteilte Meer.', 'Befreiig: De Mose füert s Volk dur s teilte Meer.'), ('Sinai: Gott (Strahlenkranz) spricht und gibt die Tafeln; Mose bringt sie dem Volk.', 'Sinai: Gott (Strahlechranz) redt und git d Tafle; de Mose bringt si em Volk.'), ('Exil und Hoffnung: Jerusalem zerstört (Risse), das Volk in Tränen weggeführt (Pfeil), später zurück (gestrichelt); ein Prophet kündigt Hoffnung an (Spross).', 'Exil und Hoffnig: Jerusalem zerstört (Riss), s Volk i Träne wäggfüert (Pfiil), spöter zrugg (gstrichlet); en Prophet chündet Hoffnig aa (Schoss).')], 'NT': [('Verkündigung: Jesus ruft: Gottes Reich ist nahe (Gottesname), kehrt um (Pfeil), glaubt (Herz).', 'Verchündigung: De Jesus rüeft: Gottes Riich isch nöch (Gottesname), chered um (Pfiil), glaubed (Härz).'), ('Kreuz und Auferstehung: das Kreuz und das leere Grab.', 'Chrüz und Uferstehig: s Chrüz und s lääre Grab.'), ('Kirche: Der Geist (Taube) kommt auf die Jünger; die Botschaft breitet sich aus (Pfeile), Gemeinden erhalten Briefe.', 'Chile: De Geischt (Tube) chunnt uf d Jünger; d Botschaft breitet sich uus (Pfiil), Gmeinde überchömed Brief.'), ('Offenbarung: Gericht (Waage) und neue Schöpfung (leuchtende Stadt) unter Gott.', 'Offebarig: Gricht (Waag) und nöii Schöpfig (lüüchtend Stadt) under Gott.')], 'GROUP-01': [('Schöpfung: Gott spricht «Licht» (Sprechblase); Erde, Pflanzen, Sonne, Mond und Sterne entstehen.', 'Schöpfig: Gott redt «Liecht» (Sprächblase); Erde, Pflanze, Sunne, Mond und Stärn entstönd.'), ('Befreiung und Weisung: nach dem Meer (links) gibt Gott am Sinai die Tafeln; Mose bringt sie dem Volk.', 'Befreiig und Wiisig: nach em Meer (links) git Gott am Sinai d Tafle; de Mose bringt si em Volk.')], 'GROUP-02': [('Königszeit: ein König in Jerusalem, das Volk im Land.', 'Chünigsziit: en Chünig z Jerusalem, s Volk im Land.'), ('Zerstörung und Rückkehr: Jerusalem mit Rissen, Menschen in Tränen weggeführt (Pfeil), später zurück (gestrichelt).', 'Zerstörig und Rückchehr: Jerusalem mit Riss, Mänsche i Träne wäggfüert (Pfiil), spöter zrugg (gstrichlet).')], 'GROUP-03': [('Psalmen: Ein Mensch mit Leier betet zu Gott, Klage (Träne) und Lob (Funken).', 'Psalme: En Mänsch mit Leier bätet zu Gott, Klag (Träne) und Lob (Funke).'), ('Hoheslied: Liebesdichtung von Braut und Bräutigam.', 'Hoheliid: Liebesdichtig vo Brut und Brüütigam.'), ('Weisheit: Nachdenken über Vergänglichkeit (Sanduhr) und Gerechtigkeit (Waage).', 'Wiisheit: Nachedänke über Vergänglichkeit (Sanduhr) und Gerächtigkeit (Waag).')], 'GROUP-04': [('Anklage: Ein Prophet ruft im Namen Gottes (Strahlenkranz) zu Recht (Waage) und Umkehr (Pfeil).', 'Aaklag: En Prophet rüeft im Name vo Gott (Strahlechranz) zu Rächt (Waag) und Umchehr (Pfiil).'), ('Trost im Exil: Jerusalem zerstört, Menschen weggeführt; der Prophet kündigt Hoffnung an (Spross).', 'Troscht im Exil: Jerusalem zerstört, Mänsche wäggfüert; de Prophet chündet Hoffnig aa (Schoss).')], 'GROUP-05': [('Zwölf Bücher (zwölf Rollen): Ein Prophet ruft im Namen Gottes zu Recht (Waage) und Umkehr (Pfeil).', 'Zwölf Büecher (zwölf Rolle): En Prophet rüeft im Name vo Gott zu Rächt (Waag) und Umchehr (Pfiil).'), ('Wiederherstellung: Gott bleibt treu; Jerusalem steht wieder, Neues wächst (Spross), Freude.', 'Widerherstellig: Gott bliibt treu; Jerusalem staat wider, Nöis wachst (Schoss), Fröid.')], 'GROUP-06': [('Vier Evangelien (vier Rollen): Jesus ruft: Gottes Reich ist nahe, kehrt um, glaubt.', 'Vier Evangelie (vier Rolle): De Jesus rüeft: Gottes Riich isch nöch, chered um, glaubed.'), ('Kreuz und Auferstehung: das Kreuz und das leere Grab.', 'Chrüz und Uferstehig: s Chrüz und s lääre Grab.')], 'GROUP-07': [('Pfingsten: In Jerusalem kommt der Geist (Taube) auf die Jünger.', 'Pfingschte: Z Jerusalem chunnt de Geischt (Tube) uf d Jünger.'), ('Bis nach Rom: Die Botschaft breitet sich aus (Pfeile, Gemeinde, Schiff); Paulus wird bewacht (Soldat).', 'Bis uf Rom: D Botschaft breitet sich uus (Pfiil, Gmeind, Schiff); de Paulus wird bewacht (Soldat).')], 'GROUP-08': [('Briefe an Gemeinden: Paulus spricht von Christus (Kreuz) und Glauben (Herz); sein Brief geht an eine Hausgemeinde.', 'Brief a Gmeinde: De Paulus redt vo Christus (Chrüz) und Glaube (Härz); sin Brief gaat a e Huusgmeind.')], 'GROUP-09': [('Ermutigung: Briefe an Gemeinden – am Glauben festhalten (Herzen), ausharren, einander lieben.', 'Ermuetigung: Brief a Gmeinde – am Glaube feschthebe (Härz), uushalte, enand gern ha.')], 'GROUP-10': [('Gottes Herrschaft: Über Weltmacht (König, Soldat) und Bedrängnis (Tränen) steht Gott.', 'Gottes Herrschaft: Über Wältmacht (Chünig, Soldat) und Bedrängnis (Träne) staat Gott.'), ('Neue Schöpfung: Gott wohnt bei den Menschen in der leuchtenden Stadt; Freude statt Trauer.', 'Nöii Schöpfig: Gott wohnt bi de Mänsche i de lüüchtende Stadt; Fröid statt Truur.')], 'JHN-002-001-012': [('Kein Wein mehr: Maria zeigt Jesus den leeren Krug und Becher; Jesus antwortet, seine Stunde sei noch nicht gekommen (Sanduhr).', 'Kei Wii me: D Maria zeigt em Jesus de läär Chrueg und Becher; de Jesus antwortet, sini Stund seg no nöd choo (Sanduhr).'), ('Hört auf ihn: Maria sagt den Dienern, sie sollen tun, was Jesus sagt (Jesus → Ohr).', 'Losed uf ihn: D Maria seit de Diener, si söled mache, was de Jesus seit (Jesus → Ohr).'), ('Krüge füllen: Jesus lässt die sechs Krüge mit Wasser füllen und zum Speisemeister bringen (Krug → Speisemeister).', 'Chrüeg fülle: De Jesus laat di sächs Chrüeg mit Wasser fülle und zum Spiismeischter bringe (Chrueg → Spiismeischter).'), ('Der gute Wein: Der Speisemeister kostet und sagt zum Bräutigam: Dieser Wein ist ausgezeichnet (Becher, Funken) – den guten hast du bis jetzt aufbewahrt; Anfang der Zeichen (Stern), die Jünger glauben (Herzen).', 'De guet Wii: De Spiismeischter probiert und seit zum Brüütigam: Dä Wii isch usgezeichnet (Becher, Funke) – de guet häsch bis jetzt ufbewahrt; Aafang vo de Zeiche (Stern), d Jünger glaubed (Härz).')], 'JHN-002-013-022': [('Tempelreinigung: Jesus mit erhobener Geissel, Tisch umgestossen, Münzen und Tiere; Sprechblase: kein Handel im Tempel.', 'Tämpelreinigung: De Jesus mit ufghabener Geissle, Tisch umgheit, Münz und Tier; Sprächblase: kei Handel im Tämpel.'), ('Zeichenforderung: Die Menge fragt nach einem Zeichen (Stern, ?); Jesus: Ihr reisst den Tempel nieder (Menge, Riss), in drei Tagen (Sonnen) richte ich ihn auf (Jesus, Tempel).', 'Zeicheforderig: D Mängi fröget nach eme Zeiche (Stern, ?); de Jesus: Ihr riissed de Tämpel ab (Mängi, Riss), i drüü Täg (Sunne) stell ich en uf (Jesus, Tämpel).')], 'JHN-002-023-025': [('Glaube und Abstand: Viele glauben wegen der Zeichen (Sterne, Herzen); Jesus vertraut sich ihnen nicht an (gestrichelte Linie).', 'Glaube und Abstand: Vili glaubed wäge de Zeiche (Stärn, Härz); de Jesus vertrout sich ine nöd aa (gstrichleti Linie).')], 'JHN-002': [('Kana: Das Wasser ist zu Wein geworden (Krüge → Weinkrug), der Anfang der Zeichen (Stern).', 'Kana: S Wasser isch zu Wii worde (Chrüeg → Wiichrueg), de Aafang vo de Zeiche (Stern).'), ('Tempel: Jesus treibt die Händler hinaus.', 'Tämpel: De Jesus tribt d Händler use.'), ('Glaube und Abstand: Viele glauben wegen der Zeichen; Jesus vertraut sich ihnen nicht an.', 'Glaube und Abstand: Vili glaubed wäge de Zeiche; de Jesus vertrout sich ine nöd aa.')], 'JHN': [('Johannes: Adler (Symbol des Evangelisten), Licht und Schriftrolle für den Anfang: das Wort und das Licht der Menschen.', 'Johannes: Adler (Symbol vom Evangelischt), Liecht und Schriftrolle für de Aafang: s Wort und s Liecht vo de Mänsche.')]}


# Bildaufträge aus bildauftraege_daten/*.json (alle übersetzten Bücher, ab 2026-10-17; Aufbau siehe bilder_auto.py)
from bilder_auto import load_briefs as _load_json  # noqa: E402

for _b in _load_json():
    _panels = []
    for _p in _b["panels"]:
        _q = {"n": _p["n"], "reference": _p["reference"], "figures": _p.get("figures", []), "objects": _p.get("objects", []),
              "signs": _p.get("signs", []), "speech": [{"from": s["from"], "to": s["to"], "icons": s["icons"], **({"think": True} if s.get("think") else {}),
                          **({"word": s["word"]} if s.get("word") else {})} for s in _p.get("speech", [])],
              "action_de": _p["action_de"]}
        # Worte im Bild (BILDPROZESS.md): Stichwortband, Namensschilder beim ersten Auftreten, Briefrahmen für Aufträge
        for _k in ("keywords", "names", "letter"):
            if _p.get(_k):
                _q[_k] = _p[_k]
        if _p.get("stage"):
            _q["stage"] = _p["stage"]
        _panels.append(_q)
        ACTIONS_GSW[_p["action_de"]] = _p["action_gsw"]
    CAPTIONS[_b["suffix"]] = [(_p["caption_de"], _p["caption_gsw"]) for _p in _b["panels"]]
    BRIEFS.append({"suffix": _b["suffix"], "level": _b["level"], "reference": _b["reference"], "target": _b["target"],
                   "translation": _b.get("translation"), "panels": _panels, "note": _b["note_de"], "note_gsw": _b["note_gsw"],
                   "tags": _b.get("tags", []), "date": _b.get("date", "2026-10-17")})


# Überarbeitung der oberen Ebenen (2026-10-17): Erzeltern, Landnahme und Rückkehr, Feuerzungen und Rom, weitere Briefe, Propheten im Auftrag Gottes
ACTIONS_GSW.update({
    "Verheissung: Gott verheisst Abraham Nachkommen, so zahlreich wie die Sterne, und ein Land.": "Verheissig: Gott verheisst em Abraham Nachkomme, so vil wie d Stärn, und es Land.",
    "Landnahme: Israel zieht über den Jordan in das Land.": "Landnahm: Israel ziet über de Jordan is Land.",
    "Jerusalem wird zerstört und das Volk weggeführt.": "Jerusalem wird zerstört und s Volk wäggfüert.",
    "Rückkehr: Menschen kehren zurück und bauen Jerusalem wieder auf.": "Rückchehr: Mänsche chömed zrugg und baued Jerusalem wider uf.",
    "In Jerusalem kommt der Geist auf die Jünger; Zungen wie von Feuer erscheinen auf ihnen.": "Z Jerusalem chunnt de Geischt uf d Jünger; Zunge wie us Füür erschiined uf ine.",
    "Die Botschaft geht von Jerusalem hinaus, bis nach Rom; dort wird Paulus bewacht.": "D Botschaft gaat vo Jerusalem use, bis uf Rom; det wird de Paulus bewacht.",
    "Weitere Briefe ermutigen Gemeinden: am Glauben festhalten, ausharren, einander lieben und Lehren prüfen.": "Wiiteri Brief mached Gmeinde Muet: am Glaube feschthebe, uushalte, enand gern ha und Lehre prüefe.",
})
CAPTIONS["GROUP-01"] = [CAPTIONS["GROUP-01"][0],
                        ("Verheissung: Gott (Strahlenkranz) verheisst Abraham Nachkommen wie die Sterne und ein Land (Sternenhimmel über grünem Land).",
                         "Verheissig: Gott (Strahlechranz) verheisst em Abraham Nachkomme wie d Stärn und es Land (Stärnehimmel über grüenem Land)."),
                        CAPTIONS["GROUP-01"][1]]
CAPTIONS["GROUP-02"] = [("Landnahme: Das Volk zieht über den Fluss in das Land (Weg).", "Landnahm: S Volk ziet über de Fluss is Land (Wäg)."),
                        CAPTIONS["GROUP-02"][0],
                        ("Zerstörung: Jerusalem mit Rissen, Menschen in Tränen weggeführt (Pfeil), später zurück (gestrichelt).",
                         "Zerstörig: Jerusalem mit Riss, Mänsche i Träne wäggfüert (Pfiil), spöter zrugg (gstrichlet)."),
                        ("Rückkehr: Menschen kehren zurück und bauen Jerusalem wieder auf (Steine, Pfeil nach oben), Freude.",
                         "Rückchehr: Mänsche chömed zrugg und baued Jerusalem wider uf (Stei, Pfiil ufe), Fröid.")]
CAPTIONS["GROUP-07"] = [("Pfingsten: In Jerusalem kommt der Geist (Taube) auf die Jünger, Feuerzungen über ihnen.",
                         "Pfingschte: Z Jerusalem chunnt de Geischt (Tube) uf d Jünger, Füürzunge über ine."),
                        ("Bis nach Rom: Die Botschaft geht von Jerusalem hinaus (Pfeile) bis nach Rom; dort wird Paulus bewacht (Soldat).",
                         "Bis uf Rom: D Botschaft gaat vo Jerusalem use (Pfiil) bis uf Rom; det wird de Paulus bewacht (Soldat).")]
CAPTIONS["GROUP-09"] = [("Ermutigung: Ein Bote liest einer Gemeinde einen Brief vor: am Glauben festhalten (Herz), ausharren (Anker), einander lieben (zwei Herzen), Lehren prüfen (Rollen mit Haken und Kreuz).",
                         "Ermuetigung: En Bott list ere Gmeind en Brief vor: am Glaube feschthebe (Härz), uushalte (Anker), enand gern ha (zwei Härz), Lehre prüefe (Rolle mit Hake und Chrüz).")]
for _k in ("GROUP-04", "GROUP-05"):
    CAPTIONS[_k][0] = (CAPTIONS[_k][0][0].replace("ruft im Namen Gottes (Strahlenkranz) zu Recht", "ruft im Auftrag Gottes (Strahlenkranz, Linie zum Propheten) zu Recht").replace("ruft im Namen Gottes zu Recht", "ruft im Auftrag Gottes (Strahlenkranz, Linie zum Propheten) zu Recht"),
                       CAPTIONS[_k][0][1].replace("rüeft im Name vo Gott (Strahlechranz) zu Rächt", "rüeft im Uftrag vo Gott (Strahlechranz, Linie zum Prophet) zu Rächt").replace("rüeft im Name vo Gott zu Rächt", "rüeft im Uftrag vo Gott (Strahlechranz, Linie zum Prophet) zu Rächt"))


def text_of(trans_id, ref):
    """Text der Verse eines Bereichs aus einer Übersetzung (für den Fingerabdruck)."""
    if not trans_id:
        return None
    t = json.loads((D / "translations" / f"{trans_id}.json").read_text(encoding="utf-8"))["text_by_reference"]
    vs = _refs.expand(ref) if hasattr(_refs, "expand") else None
    if vs is None:
        a, _, b = ref.partition("-")
        bk, c, v1 = a.split(".")
        v2 = int(b.split(".")[2]) if b else int(v1)
        vs = [f"{bk}.{c}.{v}" for v in range(int(v1), v2 + 1)]
    return " ".join(t[v] for v in vs if v in t)


def summary_of(target):
    for sub in ("text-units", "summaries"):
        p = D / sub / f"{target}.json"
        if p.exists():
            r = json.loads(p.read_text(encoding="utf-8"))
            return r.get("summary_de") or r.get("text_de")
    raise SystemExit(f"Ziel {target} nicht gefunden")


def run():
    confirm_all = os.environ.get("BIBLE_BRIEF_CONFIRM") == "1"
    # nur bestimmte Aufträge bestätigen (Präfixe der Suffixe, kommagetrennt), z. B. BIBLE_BRIEF_ONLY=RUT,MAT-005
    only = [x for x in os.environ.get("BIBLE_BRIEF_ONLY", "").split(",") if x]
    lex = {p.stem for p in (D / "illustrations/lexicon").glob("FIG-*.json")}
    n = 0
    for b in BRIEFS:
        rid = f"BRIEF-{b['suffix']}"
        # «=MAT-005» trifft nur genau diesen Auftrag, «MAT-005» auch alle darunter (Abschnitte, Merkverse)
        confirm = confirm_all and (not only or any(b["suffix"] == x.lstrip("=") or (not x.startswith("=") and b["suffix"].startswith(x + "-")) for x in only))
        if len(CAPTIONS.get(b["suffix"], [])) != len(b["panels"]):
            raise SystemExit(f"{rid}: Bildhilfe (CAPTIONS) passt nicht zur Zahl der Felder")
        for p in b["panels"]:
            for k in ("figures", "objects", "signs"):
                for x in p[k]:
                    if x not in lex:
                        raise SystemExit(f"{rid}: {x} nicht im Bildlexikon")
            for sp in p["speech"]:
                for x in [sp["from"], sp["to"], *sp["icons"]]:
                    if x not in lex:
                        raise SystemExit(f"{rid}: {x} nicht im Bildlexikon")
        basis = [{"record": b["target"], "field": "summary", "fingerprint": localizations.fingerprint(summary_of(b["target"]))}]
        if b["translation"]:
            for p in b["panels"]:
                basis.append({"record": b["translation"], "field": "text_by_reference", "reference": p["reference"],
                              "fingerprint": localizations.fingerprint(text_of(b["translation"], p["reference"]))})
        path = D / "illustrations/briefs" / f"{rid}.json"
        if path.exists() and not confirm:
            old = {(x["record"], x.get("reference")): x["fingerprint"] for x in json.loads(path.read_text(encoding="utf-8")).get("basis", [])}
            for x in basis:
                x["fingerprint"] = old.get((x["record"], x.get("reference")), x["fingerprint"])
        rec = {"id": rid, "type": "illustration_brief", "status": "draft", "tags": b.get("tags", ["TAG-JOHN"]), "level": b["level"],
               **({"reference": b["reference"]} if b["reference"] else {}), "target": b["target"], "panels": b["panels"],
               "actions_de": [p["action_de"] for p in b["panels"]], "captions_de": [c[0] for c in CAPTIONS[b["suffix"]]],
               "interpretation_note_de": b["note"], "basis": basis,
               "basis_note_de": "Fingerabdrücke des Textes, gegen den der Auftrag geprüft wurde (Verse der hochdeutschen Arbeitsübersetzung, sofern angegeben, und Zusammenfassung des Ziels). "
                                "Bei Abweichung gilt der Auftrag als veraltet, bis er erneut geprüft ist.",
               "authorship_de": AUTH if "date" not in b else AUTH.replace("2026-10-14", b["date"]),
               "knowledge": {"asserted_at": b.get("date", DATE), "supersedes": None}}
        # Neu zu zeichnen (z. B. Zusammenfassung neu aus der Kernanalyse): bleibt vermerkt, bis der Auftrag bestätigt wird
        if path.exists() and not confirm and json.loads(path.read_text(encoding="utf-8")).get("rework"):
            rec["rework"] = json.loads(path.read_text(encoding="utf-8"))["rework"]
        n += write(path, rec)
        n += localize(rid, rec, {"interpretation_note_de": b["note_gsw"], "actions_de": [ACTIONS_GSW[p["action_de"]] for p in b["panels"]],
                                  "captions_de": [c[1] for c in CAPTIONS[b["suffix"]]]}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026", AUTH_GSW, DATE)
    print(f"PASS: {len(BRIEFS)} Bildaufträge; {n} Dateien geschrieben" + (" (Text erneut geprüft und bestätigt" + (f": {', '.join(only)})" if only else ")") if confirm_all else ""))


if __name__ == "__main__":
    run()
