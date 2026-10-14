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


def P(n, ref, figures, action, speech=(), objects=(), signs=()):
    return {"n": n, "reference": ref, "figures": list(figures), "objects": list(objects), "signs": list(signs),
            "speech": [{"from": a, "to": b, "icons": list(i)} for a, b, i in speech], "action_de": action}


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
           speech=[(SM, BG, ["FIG-OBJ-BECHER-VOLL"])], objects=["FIG-OBJ-BECHER-VOLL", "FIG-OBJ-KRUG-WEIN"],
           signs=["FIG-ZEICHEN-FREUDE", "FIG-ZEICHEN-STERN", "FIG-ZEICHEN-GLAUBEN"]),
     ],
     "note": "Bildfolge in vier Feldern. Braut und Gäste sind im Text nicht genannt bzw. handeln nicht; sie zeigen nur den Ort «Hochzeit». "
             "Die Sprechblasen fassen das Gesagte in Zeichen; der Wortlaut steht als Bildunterschrift. Der Wechsel des Wassers in Wein wird "
             "nicht als Vorgang gezeigt, weil der Text ihn nicht erzählt ([[JHN.2.9]]: «das Wasser, das zu Wein geworden war»).",
     "note_gsw": "Bildfolg i vier Fälder. D Brut und d Gäscht nännt de Text nöd bzw. si handled nöd; si zeiged nu de Ort «Hochziit». "
                 "D Sprächblase fassed s Gseit i Zeiche; de Wortlut staat als Bildunderschrift. Wie s Wasser zu Wii wird, zeigt s Bild nöd, "
                 "wil de Text das nöd verzellt ([[JHN.2.9]]: «s Wasser, wo zu Wii worde isch»)."},
    {"suffix": "JHN-002-013-022", "level": "section", "reference": "JHN.2.13-JHN.2.22", "target": "TU-JHN-002-013-022",
     "translation": "TRANS-JHN-002-001-025-DE-WORKING",
     "panels": [
         P(1, "JHN.2.14-JHN.2.16", [J, "FIG-ROLLE-HAENDLER"], "Jesus treibt mit einer Geissel die Händler, Schafe und Rinder aus dem Tempel, schüttet die Münzen aus und stösst die Tische um.",
           speech=[(J, "FIG-ROLLE-HAENDLER", ["FIG-ORT-TEMPEL", "FIG-OBJ-MUENZEN", "FIG-ZEICHEN-FEHLT"])],
           objects=["FIG-ORT-TEMPEL", "FIG-OBJ-PEITSCHE", "FIG-OBJ-MUENZEN", "FIG-OBJ-SCHAF", "FIG-OBJ-TAUBE"]),
         P(2, "JHN.2.18-JHN.2.19", ["FIG-GRUPPE-MENGE", J], "Die Juden fragen nach einem Zeichen; Jesus antwortet: Reisst diesen Tempel nieder, in drei Tagen werde ich ihn aufrichten.",
           speech=[("FIG-GRUPPE-MENGE", J, ["FIG-ZEICHEN-STERN", "FIG-ZEICHEN-FRAGEN"]), (J, "FIG-GRUPPE-MENGE", ["FIG-ZEICHEN-NIEDERREISSEN", "FIG-ZEICHEN-TAGE", "FIG-ORT-TEMPEL"])],
           objects=["FIG-ORT-TEMPEL"]),
     ],
     "note": "Ob Jesus die Geissel gegen Menschen oder nur gegen die Tiere gebraucht, lässt [[JHN.2.15]] offen; das Bild zeigt sie erhoben, ohne Schlag. "
             "Die Fragenden («die Juden», [[JHN.2.18]]) erscheinen als neutrale Menge, ohne Merkmale einer Volksgruppe. Dass Jesus vom Tempel seines Leibes "
             "spricht ([[JHN.2.21]]), sagt der Erzähler; das Bild deutet es nicht aus. Für «in drei Tagen» stehen drei Sonnen, für «niederreissen» der Tempel mit Riss.",
     "note_gsw": "Öb de Jesus d Geissle gäge Mänsche oder nu gäge d Tier bruucht, laat [[JHN.2.15]] offe; s Bild zeigt si ufgha, ohni Schlag. "
                 "Die, wo fröged («d Jude», [[JHN.2.18]]), erschiined als neutrali Mängi, ohni Merkmal vo ere Volksgruppe. Dass de Jesus vom Tämpel "
                 "vo sim Liib redt ([[JHN.2.21]]), seit de Erzäller; s Bild düütet das nöd uus. Für «i drüü Täg» staand drüü Sunne, für «abriisse» de Tämpel mit Riss."},
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
F_EXIL = lambda n, ref, act: P(n, ref, [PR, ME], act, speech=[(PR, ME, [Z("HOFFNUNG")])], objects=[JER],  # noqa: E731
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
F_PROPHET = lambda n, ref, zwoelf=False: P(n, ref, [PR, ME],  # noqa: E731
                                           ("Zwölf Prophetenbücher: Ein Prophet klagt Unrecht an und ruft zu Recht und Umkehr." if zwoelf else
                                            "Ein Prophet klagt Unrecht an und ruft zur Umkehr."),
                                           speech=[(PR, ME, [Z("GERICHT"), Z("UMKEHR")])], objects=[ROLLE] if zwoelf else [])

UPPER = [
    ("BIBLE", "bible", "SUM-BIBLE", [
        F_BERG(1), F_KREUZ(2, True), F_NEU(3),
        P(4, "2TI.3.16", [PR], "Viele Stimmen: Erzählungen und Weisheit, Gebete und Lieder, prophetische Rede, Briefe.", objects=[ROLLE, LEIER, BRIEF])],
     "Vier Felder nach der Zusammenfassung: Gott und Israel, Jesus, die Hoffnung auf eine erneuerte Schöpfung und die vielen Arten von Schriften. "
     "Dass diese Geschichte zusammengehört, ist christliche Lesart, wie die Zusammenfassung selbst sagt. Das Gottessymbol (Strahlenkranz mit dem Gottesnamen) zeigt Gott, ohne ihn abzubilden.",
     "Vier Fälder nach de Zämefassig: Gott und Israel, de Jesus, d Hoffnig uf e nöii Schöpfig und di vile Arte vo Schrifte. "
     "Dass die Gschicht zämeghört, isch christlichi Läsart, wie s d Zämefassig sälber seit. S Gottessymbol (Strahlechranz mit em Gottesname) zeigt Gott, ohni en abzbilde."),
    ("OT", "testament", "SUM-OT", [
        F_SCHOEPFUNG(1), F_MEER(2), F_BERG(3),
        F_EXIL(4, "JER.29.4-JER.29.14", "Scheitern und Neubeginn: Jerusalem ist zerstört, das Volk weggeführt und klagt; ein Prophet kündigt Hoffnung und Rückkehr an.")],
     "Vier Felder: Schöpfung, Befreiung, Bund, Exil und Hoffnung. Klage und Weisheit sowie die prophetische Kritik zeigen die Bilder der Buchgruppen genauer. "
     "Die Menge steht für das Volk Israel, ohne Merkmale einer Volksgruppe.",
     "Vier Fälder: Schöpfig, Befreiig, Bund, Exil und Hoffnig. Klag und Wiisheit und di prophetisch Kritik zeiged d Bilder vo de Buechgruppe gnauer. "
     "D Mängi staat für s Volk Israel, ohni Merkmal vo ere Volksgruppe."),
    ("NT", "testament", "SUM-NT", [
        F_VERKUENDET(1), F_KREUZ(2, False),
        P(3, "ACT.1.8", [HG, "FIG-ROLLE-JUENGER", GEM], "Der Geist kommt auf die Jünger; die Botschaft breitet sich aus, Gemeinden entstehen und erhalten Briefe.",
          objects=[BRIEF], signs=[Z("AUSBREITEN")]),
        P(4, "REV.20.11-REV.21.4", [G], "Offenbarung: Gericht und Hoffnung auf eine neue Schöpfung.", signs=[Z("GERICHT"), Z("NEUE-SCHOEPFUNG")])],
     "Vier Felder: Evangelien (Verkündigung; Kreuz und Auferstehung), Apostelgeschichte und Briefe, Offenbarung. Das leere Grab steht für die Auferstehung; "
     "der auferstandene Jesus selbst ist nicht gezeichnet.",
     "Vier Fälder: Evangelie (Verchündigung; Chrüz und Uferstehig), Aposchtelgschicht und Brief, Offebarig. S lääre Grab staat für d Uferstehig; "
     "de uferstandni Jesus sälber isch nöd zeichnet."),
    ("GROUP-01", "group", "SUM-GROUP-01", [F_SCHOEPFUNG(1), F_BERG(2, meer=True)],
     "Zwei Felder: Anfänge der Welt; Befreiung und Weisung. Die Verheissungen an die Erzeltern und das Ende vor dem Einzug ins Land zeigt das Bild noch nicht.",
     "Zwei Fälder: Aafäng vo de Wält; Befreiig und Wiisig. D Verheissige a d Erzeltere und s Änd vor em Iizug is Land zeigt s Bild no nöd."),
    ("GROUP-02", "group", "SUM-GROUP-02", [
        P(1, "2SA.5.1-2SA.5.10", [KO, ME], "Israel lebt im Land; ein König herrscht in Jerusalem.", objects=[JER]),
        P(2, "2KI.25.8-2KI.25.11", [ME], "Jerusalem wird zerstört und das Volk weggeführt; später kehren Menschen zurück.", objects=[JER],
          signs=[Z("NIEDERREISSEN"), Z("EXIL"), Z("TRAUER")])],
     "Zwei Felder: Königszeit; Zusammenbruch und Rückkehr. Die Landnahme ist nicht gezeichnet; die gestrichelte Rückkehr nimmt Esra und Nehemia auf.",
     "Zwei Fälder: Chünigsziit; Zämebruch und Rückchehr. D Landnahm isch nöd zeichnet; di gstrichlet Rückchehr nimmt Esra und Nehemia uf."),
    ("GROUP-03", "group", "SUM-GROUP-03", [
        P(1, "PSA.13", [ME, G], "Gebete: Klage und Lob vor Gott.", speech=[(ME, G, [Z("TRAUER"), Z("FREUDE")])],
          objects=[LEIER]),
        P(2, "SNG.2", ["FIG-ROLLE-BRAUT", "FIG-ROLLE-BRAEUTIGAM"], "Liebesdichtung: Braut und Bräutigam.", signs=[Z("HOCHZEIT"), Z("FREUDE")]),
        P(3, "ECC.3.1-ECC.3.8", [ME], "Weisheit: Nachdenken über Gerechtigkeit und Vergänglichkeit; alles hat seine Zeit.",
          objects=[ROLLE], signs=[Z("STUNDE"), Z("GERICHT")])],
     "Drei Felder: Psalmen, Hoheslied, Weisheit (Sprüche, Hiob, Prediger). Die Waage steht hier für Gerechtigkeit, die Sanduhr für Vergänglichkeit.",
     "Drüü Fälder: Psalme, Hoheliid, Wiisheit (Sprüch, Hiob, Prediger). D Waag staat da für Gerächtigkeit, d Sanduhr für Vergänglichkeit."),
    ("GROUP-04", "group", "SUM-GROUP-04", [
        F_PROPHET(1, "ISA.1.16-ISA.1.17"),
        F_EXIL(2, "ISA.40.1-ISA.40.2", "Nach dem Zusammenbruch Jerusalems und im Exil kündigt ein Prophet Trost und Hoffnung an.")],
     "Zwei Felder: Kritik an Unrecht und Ruf zur Umkehr; Klage über Jerusalem und Hoffnung. Der Prophet ist eine Rollenfigur für Jesaja, Jeremia, Ezechiel und Daniel.",
     "Zwei Fälder: Kritik a Unrächt und Ruef zur Umchehr; Klag über Jerusalem und Hoffnig. De Prophet isch e Rollefigur für Jesaja, Jeremia, Ezechiel und Daniel."),
    ("GROUP-05", "group", "SUM-GROUP-05", [
        F_PROPHET(1, "AMO.5.14-AMO.5.24", zwoelf=True),
        P(2, "AMO.9.13-AMO.9.15", [G, ME], "Gott bleibt treu: Wiederaufbau und neues Wachstum.", objects=[JER], signs=[Z("HOFFNUNG"), Z("FREUDE")])],
     "Zwei Felder: zwölf Schriftrollen für die zwölf Bücher, Ruf zu Recht und Umkehr; Wiederherstellung.",
     "Zwei Fälder: zwölf Schriftrolle für di zwölf Büecher, Ruef zu Rächt und Umchehr; Widerherstellig."),
    ("GROUP-06", "group", "SUM-GROUP-06", [F_VERKUENDET(1, vier=True), F_KREUZ(2, False)],
     "Zwei Felder: vier Schriftrollen für die vier Evangelien, Jesus verkündet; Kreuz und leeres Grab.",
     "Zwei Fälder: vier Schriftrolle für di vier Evangelie, de Jesus verchündet; Chrüz und lääres Grab."),
    ("GROUP-07", "group", "SUM-GROUP-07", [
        P(1, "ACT.2.1-ACT.2.4", [HG, "FIG-ROLLE-JUENGER"], "In Jerusalem kommt der Geist auf die Jünger.", objects=[JER]),
        P(2, "ACT.28.14-ACT.28.16", [PAU, SO, GEM], "Die Botschaft geht hinaus, bis nach Rom; Paulus reist und wird bewacht.",
          objects=[JER, BOOT], signs=[Z("AUSBREITEN")])],
     "Zwei Felder: Pfingsten in Jerusalem; Ausbreitung, Reisen, Konflikte. Der Soldat steht für die Bewachung des Paulus in Rom ([[ACT.28.16]]).",
     "Zwei Fälder: Pfingschte z Jerusalem; Uusbreitig, Reise, Konflikt. De Soldat staat für d Bewachig vom Paulus z Rom ([[ACT.28.16]])."),
    ("GROUP-08", "group", "SUM-GROUP-08", [
        P(1, "PHP.1.1-PHP.1.11", [PAU, GEM], "Paulus schreibt Gemeinden Briefe: die Botschaft von Christus für ihr Zusammenleben.",
          speech=[(PAU, GEM, [KREUZ, Z("GLAUBEN")])], objects=[BRIEF])],
     "Ein Feld: Paulus, Brief und Gemeinde. Das Kreuz steht für die Botschaft von Christus. Ob alle Briefe von Paulus selbst stammen, ist in der Forschung umstritten («unter dem Namen des Paulus überliefert»).",
     "Eis Fäld: De Paulus, en Brief und e Gmeind. S Chrüz staat für d Botschaft vo Christus. Öb alli Brief vom Paulus sälber stammed, isch i de Forschig umstritte («under em Name vom Paulus überliferet»)."),
    ("GROUP-09", "group", "SUM-GROUP-09", [
        P(1, "HEB.10.23-HEB.10.25", [GEM], "Weitere Briefe ermutigen Gemeinden: am Glauben festhalten, ausharren und einander lieben.",
          objects=[BRIEF], signs=[Z("GLAUBEN")])],
     "Ein Feld: mehrere Briefe an Gemeinden. Die Herausforderungen sind nicht einzeln gezeichnet.",
     "Eis Fäld: mehreri Brief a Gmeinde. D Herusforderige sind nöd einzeln zeichnet."),
    ("GROUP-10", "group", "SUM-GROUP-10", [
        P(1, "REV.4.1-REV.4.11", [G, KO, SO, ME], "Visionen: Über Bedrängnis und Weltmacht steht Gottes Herrschaft.", signs=[Z("TRAUER")]),
        F_NEU(2, menge=True)],
     "Zwei Felder: Gottes Herrschaft über Weltmacht und Bedrängnis; erneuerte Schöpfung. König und Soldat stehen für Weltmacht allgemein, nicht für eine bestimmte Macht; "
     "die Tierbilder der Offenbarung sind nicht gezeichnet.",
     "Zwei Fälder: Gottes Herrschaft über Wältmacht und Bedrängnis; nöii Schöpfig. Chünig und Soldat staand für Wältmacht allgemein, nöd für e bestimmti Macht; "
     "d Tierbilder vo de Offebarig sind nöd zeichnet."),
]
for suffix, lvl, target, panels, note, note_g in UPPER:
    BRIEFS.append({"suffix": suffix, "level": lvl, "reference": None, "target": target, "translation": None, "panels": panels,
                   "note": note, "note_gsw": note_g, "tags": []})


ACTIONS_GSW = {'Bei der Hochzeit sagt Maria zu Jesus, dass der Wein ausgegangen ist; Jesus antwortet, seine Stunde sei noch nicht gekommen.': 'A de Hochziit seit d Maria zum Jesus, de Wii seg usgange; de Jesus antwortet, sini Stund seg no nöd choo.', 'Maria sagt zu den Dienern, sie sollen tun, was Jesus ihnen sagt.': 'D Maria seit de Diener, si söled mache, was de Jesus ine säg.', 'Jesus lässt die sechs steinernen Krüge mit Wasser füllen und schickt die Diener zum Speisemeister.': 'De Jesus laat di sächs steinige Chrüeg mit Wasser fülle und schickt d Diener zum Spiismeischter.', 'Der Speisemeister kostet den Wein und spricht zum Bräutigam vom guten Wein; es ist der Anfang der Zeichen, die Jünger glauben an Jesus.': 'De Spiismeischter probiert de Wii und redt mit em Brüütigam vom guete Wii; das isch de Aafang vo de Zeiche, d Jünger glaubed a de Jesus.', 'Jesus treibt mit einer Geissel die Händler, Schafe und Rinder aus dem Tempel, schüttet die Münzen aus und stösst die Tische um.': 'De Jesus tribt mit ere Geissle d Händler, d Schaf und d Rinder us em Tämpel, schüttet s Münz us und heit d Tisch um.', 'Die Juden fragen nach einem Zeichen; Jesus antwortet: Reisst diesen Tempel nieder, in drei Tagen werde ich ihn aufrichten.': 'D Jude fröged nach eme Zeiche; de Jesus antwortet: Riissed dä Tämpel ab, i drüü Täg stell ich en uf.', 'Viele in Jerusalem glauben wegen der Zeichen an Jesus; er vertraut sich ihnen nicht an, weil er weiss, was im Menschen ist.': 'Vili z Jerusalem glaubed wäge de Zeiche a de Jesus; er vertrout sich ine nöd aa, wil er weiss, was im Mänsch isch.', 'Hochzeit zu Kana: Das Wasser in den Krügen ist zu Wein geworden – der Anfang der Zeichen.': 'Hochziit z Kana: S Wasser i de Chrüeg isch zu Wii worde – de Aafang vo de Zeiche.', 'Jesus treibt die Händler aus dem Tempel.': 'De Jesus tribt d Händler us em Tämpel.', 'Viele glauben wegen der Zeichen; Jesus vertraut sich ihnen nicht an.': 'Vili glaubed wäge de Zeiche; de Jesus vertrout sich ine nöd aa.', 'Adler (Evangelistensymbol), Licht, Schriftrolle.': 'Adler (Symbol vom Evangelischt), Liecht, Schriftrolle.'}


ACTIONS_GSW.update({'Gott und Israel: Am Berg gibt Gott die Weisung; Mose bringt die Tafeln zum Volk.': 'Gott und Israel: Am Bärg git Gott d Wiisig; de Mose bringt d Tafle zum Volk.', 'Jesus: sein Leben, sein Tod am Kreuz und das leere Grab (Auferstehung).': 'De Jesus: sis Läbe, sin Tod am Chrüz und s lääre Grab (Uferstehig).', 'Hoffnung auf eine erneuerte Schöpfung: die Stadt im Licht, in der Gott bei den Menschen wohnt.': 'Hoffnig uf e nöii Schöpfig: d Stadt im Liecht, wo Gott bi de Mänsche wohnt.', 'Viele Stimmen: Erzählungen und Weisheit, Gebete und Lieder, prophetische Rede, Briefe.': 'Vili Stimme: Verzällige und Wiisheit, Gebät und Lieder, prophetischi Red, Brief.', 'Schöpfung: Gott spricht, und es wird Licht; Himmel und Erde, Pflanzen, Sonne, Mond und Sterne entstehen.': 'Schöpfig: Gott redt, und s wird Liecht; Himmel und Erde, Pflanze, Sunne, Mond und Stärn entstönd.', 'Befreiung: Mose führt das Volk auf trockenem Boden durch das geteilte Meer.': 'Befreiig: De Mose füert s Volk uf tröchnem Bode dur s teilte Meer.', 'Scheitern und Neubeginn: Jerusalem ist zerstört, das Volk weggeführt und klagt; ein Prophet kündigt Hoffnung und Rückkehr an.': 'Schiitere und Neuaafang: Jerusalem isch zerstört, s Volk wäggfüert und klagt; en Prophet chündet Hoffnig und Rückchehr aa.', 'Jesus verkündet die Nähe von Gottes Reich und ruft: Kehrt um und glaubt.': 'De Jesus verchündet, dass Gottes Riich nöch isch, und rüeft: Chered um und glaubed.', 'Jesus stirbt am Kreuz; das Grab ist leer: Er ist auferweckt.': 'De Jesus stirbt am Chrüz; s Grab isch läär: Er isch uferweckt.', 'Der Geist kommt auf die Jünger; die Botschaft breitet sich aus, Gemeinden entstehen und erhalten Briefe.': 'De Geischt chunnt uf d Jünger; d Botschaft breitet sich uus, Gmeinde entstönd und überchömed Brief.', 'Offenbarung: Gericht und Hoffnung auf eine neue Schöpfung.': 'Offebarig: Gricht und Hoffnig uf e nöii Schöpfig.', 'Nach dem Weg durch das Meer gibt Gott am Berg die Weisung; Mose bringt die Tafeln zum Volk.': 'Nach em Wäg dur s Meer git Gott am Bärg d Wiisig; de Mose bringt d Tafle zum Volk.', 'Israel lebt im Land; ein König herrscht in Jerusalem.': 'Israel läbt im Land; en Chünig regiert z Jerusalem.', 'Jerusalem wird zerstört und das Volk weggeführt; später kehren Menschen zurück.': 'Jerusalem wird zerstört und s Volk wäggfüert; spöter chömed Mänsche zrugg.', 'Gebete: Klage und Lob vor Gott.': 'Gebät: Klag und Lob vor Gott.', 'Liebesdichtung: Braut und Bräutigam.': 'Liebesdichtig: Brut und Brüütigam.', 'Weisheit: Nachdenken über Gerechtigkeit und Vergänglichkeit; alles hat seine Zeit.': 'Wiisheit: Nachedänke über Gerächtigkeit und Vergänglichkeit; alles hät sini Ziit.', 'Ein Prophet klagt Unrecht an und ruft zur Umkehr.': 'En Prophet klagt Unrächt aa und rüeft zur Umchehr.', 'Nach dem Zusammenbruch Jerusalems und im Exil kündigt ein Prophet Trost und Hoffnung an.': 'Nach em Zämebruch vo Jerusalem und im Exil chündet en Prophet Troscht und Hoffnig aa.', 'Zwölf Prophetenbücher: Ein Prophet klagt Unrecht an und ruft zu Recht und Umkehr.': 'Zwölf Prophetebüecher: En Prophet klagt Unrächt aa und rüeft zu Rächt und Umchehr.', 'Gott bleibt treu: Wiederaufbau und neues Wachstum.': 'Gott bliibt treu: Widerufbau und nöis Wachstum.', 'Vier Evangelien erzählen von Jesus. Er verkündet die Nähe von Gottes Reich und ruft: Kehrt um und glaubt.': 'Vier Evangelie verzälled vom Jesus. Er verchündet, dass Gottes Riich nöch isch, und rüeft: Chered um und glaubed.', 'In Jerusalem kommt der Geist auf die Jünger.': 'Z Jerusalem chunnt de Geischt uf d Jünger.', 'Die Botschaft geht hinaus, bis nach Rom; Paulus reist und wird bewacht.': 'D Botschaft gaat use, bis uf Rom; de Paulus reist und wird bewacht.', 'Paulus schreibt Gemeinden Briefe: die Botschaft von Christus für ihr Zusammenleben.': 'De Paulus schriibt Gmeinde Brief: d Botschaft vo Christus für ires Zämeläbe.', 'Weitere Briefe ermutigen Gemeinden: am Glauben festhalten, ausharren und einander lieben.': 'Wiiteri Brief mached Gmeinde Muet: am Glaube feschthebe, uushalte und enand gern ha.', 'Visionen: Über Bedrängnis und Weltmacht steht Gottes Herrschaft.': 'Visione: Über Bedrängnis und Wältmacht staat Gottes Herrschaft.', 'Am Ende: Gott wohnt bei den Menschen in der erneuerten Schöpfung; Trauer ist vorbei.': 'Am Änd: Gott wohnt bi de Mänsche i de nöie Schöpfig; d Truur isch verbii.'})


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
    confirm = os.environ.get("BIBLE_BRIEF_CONFIRM") == "1"
    lex = {p.stem for p in (D / "illustrations/lexicon").glob("FIG-*.json")}
    n = 0
    for b in BRIEFS:
        rid = f"BRIEF-{b['suffix']}"
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
               "actions_de": [p["action_de"] for p in b["panels"]], "interpretation_note_de": b["note"], "basis": basis,
               "basis_note_de": "Fingerabdrücke des Textes, gegen den der Auftrag geprüft wurde (Verse der hochdeutschen Arbeitsübersetzung, sofern angegeben, und Zusammenfassung des Ziels). "
                                "Bei Abweichung gilt der Auftrag als veraltet, bis er erneut geprüft ist.",
               "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
        n += write(path, rec)
        n += localize(rid, rec, {"interpretation_note_de": b["note_gsw"], "actions_de": [ACTIONS_GSW[p["action_de"]] for p in b["panels"]]}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026", AUTH_GSW, DATE)
    print(f"PASS: {len(BRIEFS)} Bildaufträge; {n} Dateien geschrieben" + (" (Text erneut geprüft und bestätigt)" if confirm else ""))


if __name__ == "__main__":
    run()
