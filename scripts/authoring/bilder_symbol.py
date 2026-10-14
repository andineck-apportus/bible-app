#!/usr/bin/env python3
"""Autorenwerkzeug: Bildsprache «Symbol» – Stil (Figuren-Legende) und Bilder mit Metadaten.

Die Zeichnungen liegen als SVG in data/illustrations/symbol/ (Bibliothek _bibliothek.svg mit Figuren, Gegenständen und
Szenen; je Bild eine kleine SVG-Datei, die Bausteine der Bibliothek verwendet). Dieses Werkzeug schreibt die Datensätze
dazu (Typ illustration_style bzw. illustration) samt Züridüütsch-Lokalisierung von Bildbeschreibung und Deutungshinweis.

Bilder sind bildliche Deutung, nicht Text: Sie legen Kleidung, Anordnung und Gewichtung fest, die der Bibeltext offenlässt.
Personen ohne Gesicht; Jesus erkennbar am Kreuznimbus. KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck;
keine fachliche Prüfung. Eigene Zeichnungen, CC0 1.0.

Aufruf: python3 scripts/authoring/bilder_symbol.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, localize, write  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; eigene Zeichnung, keine fachliche Prüfung."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-14; Mundart noch nicht muttersprachlich geprüft."
LIC = "CC0 1.0 (eigene Zeichnung)"

FIGURES = [
    ("ill-p-jesus", "Jesus", "Jesus", "Kreuznimbus (goldener Schein mit Kreuz), weisses Gewand, roter Mantel – nach alter Bildtradition"),
    ("ill-p-maria", "Maria, Mutter Jesu", "Mary, mother of Jesus", "Blauer Schleier und blaues Gewand – nach alter Bildtradition"),
    ("ill-p-juenger", "Jünger", "Disciple", "Erdfarbenes Gewand mit Gürtel"),
    ("ill-p-braut", "Braut", "Bride", "Weisser Schleier, Blumenkranz"),
    ("ill-p-braeutigam", "Bräutigam", "Bridegroom", "Festgewand, goldener Kranz"),
    ("ill-p-gast", "Gäste, Menschen", "Guests, people", "Gedeckte Farben, teils mit Kopftuch"),
    ("ill-p-diener", "Diener", "Servant", "Schürze"),
    ("ill-p-meister", "Speisemeister", "Master of the feast", "Grünes Gewand, Goldgürtel"),
    ("ill-p-haendler", "Händler", "Trader", "Kopftuch, Geldbeutel"),
    ("ill-zeichen", "Zeichen", "Sign", "Goldener Stern: ein «Zeichen» im Sinn des Johannesevangeliums"),
]

STYLE = {
    "id": "ILLSTYLE-SYMBOL", "type": "illustration_style", "status": "draft", "tags": [],
    "key": "symbol", "labels": {"de": "Symbol", "en": "Symbol"},
    "description_de": "Flache, klare Symbolbilder mit festen Figuren. Personen ohne Gesicht, erkennbar an Farbe und Zeichen; "
                      "dieselben Figuren und Gegenstände kehren auf allen Zoomstufen wieder.",
    "library": "data/illustrations/symbol/_bibliothek.svg",
    "figures": [{"symbol": s, "label_de": de, "label_en": en, "sign_de": sign} for s, de, en, sign in FIGURES],
    "license": LIC, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None},
}

# id-suffix, level, reference, target, depicts, alt_de, note_de, alt_gsw, note_gsw
ILL = [
    ("JHN", "book", "JHN", "SUM-BOOK-JHN", [],
     "Ein Adler mit ausgebreiteten Flügeln vor aufgehendem Licht, darunter ein offenes Buch.",
     "Der Adler ist seit der Alten Kirche das Symbol des Evangelisten Johannes; Licht und Buch nehmen den Anfang auf "
     "(«Im Anfang war das Wort», «das Licht der Menschen»). Die Zuordnung der Tiere zu den Evangelisten ist Tradition, nicht Text.",
     "En Adler mit uusbreitete Flügel vor em ufgehende Liecht, drunder es offes Buech.",
     "De Adler isch sit de Alte Chile s Symbol vom Evangelischt Johannes; Liecht und Buech nämed de Aafang uf "
     "(«Im Aafang isch s Wort gsii», «s Liecht vo de Mänsche»). D Zuednig vo de Tier zu de Evangelischte isch Tradition, nöd Text."),
    ("JHN-002", "chapter", "JHN.2", "SUM-CH-JHN-002", ["ill-p-jesus", "ill-p-maria", "ill-p-juenger", "ill-p-gast", "ill-p-zeichen"],
     "Drei Bildfelder: die Hochzeit zu Kana, Jesus mit der Peitsche vor dem Tempel, Jesus und die Menge in Jerusalem.",
     "Die drei Felder entsprechen den drei Abschnitten des Kapitels; Einzelheiten siehe dort.",
     "Drüü Bildfälder: d Hochziit z Kana, de Jesus mit de Geissle vor em Tämpel, de Jesus und d Mängi z Jerusalem.",
     "Di drüü Fälder entspräched de drüü Abschnitt vom Kapitel; Einzelheite lueg dört."),
    ("JHN-002-001-012", "section", "JHN.2.1-JHN.2.12", "TU-JHN-002-001-012",
     ["ill-p-jesus", "ill-p-maria", "ill-p-braut", "ill-p-braeutigam", "ill-p-gast", "ill-p-juenger", "ill-p-diener", "ill-p-meister", "ill-zeichen"],
     "Hochzeitstafel mit Braut und Bräutigam, Gästen und Jüngern. Vorne sechs steinerne Krüge mit Wasser, der letzte mit Wein; "
     "Jesus weist auf die Krüge, Maria spricht zum Diener, der Diener bringt dem Speisemeister einen Becher; ein goldener Stern als Zeichen.",
     "Der Text nennt Braut und Bräutigam nicht als Handelnde; der Bräutigam wird nur angesprochen ([[JHN.2.9-JHN.2.10]]). "
     "Dass Maria und Jesus nebeneinander stehen und wo die Jünger sitzen, ist Bildgestaltung.",
     "Hochziitstafele mit Brut und Brüütigam, Gäscht und Jünger. Vorne sächs steinigi Chrüeg mit Wasser, de letscht mit Wii; "
     "de Jesus zeigt uf d Chrüeg, d Maria redt mit em Diener, de Diener bringt em Spiismeischter en Becher; en goldige Stern als Zeiche.",
     "De Text nännt Brut und Brüütigam nöd als Handelndi; de Brüütigam wird nu aagredt ([[JHN.2.9-JHN.2.10]]). "
     "Dass d Maria und de Jesus näbenand stönd und wo d Jünger sitzed, isch Bildgstaltig."),
    ("JHN-002-013-022", "section", "JHN.2.13-JHN.2.22", "TU-JHN-002-013-022",
     ["ill-p-jesus", "ill-p-juenger", "ill-p-haendler"],
     "Jesus mit einer Peitsche aus Stricken vor dem Tempel; ein umgestossener Tisch, rollende Münzen, ein Händler, ein Schaf, auffliegende Tauben; ein Jünger daneben.",
     "Dass ein Jünger dabeisteht, folgt aus [[JHN.2.17]] («seine Jünger erinnerten sich»), die Anordnung ist Bildgestaltung. "
     "Ob Jesus die Peitsche gegen Menschen oder nur gegen die Tiere gebraucht, lässt [[JHN.2.15]] offen; das Bild zeigt sie erhoben, ohne Schlag.",
     "De Jesus mit ere Geissle us Strick vor em Tämpel; en umgschtossne Tisch, rollendi Münze, en Händler, es Schaf, uffliegendi Tube; en Jünger dernäbe.",
     "Dass en Jünger dernäbe staat, folgt us [[JHN.2.17]] («sini Jünger händ sich erinneret»), d Aaordnig isch Bildgstaltig. "
     "Öb de Jesus d Geissle gäge Mänsche oder nu gäge d Tier bruucht, laat [[JHN.2.15]] offe; s Bild zeigt si ufgha, ohni Schlag."),
    ("JHN-002-023-025", "section", "JHN.2.23-JHN.2.25", "TU-JHN-002-023-025",
     ["ill-p-jesus", "ill-p-gast", "ill-zeichen"],
     "Eine Menge unter goldenen Sternen (Zeichen) und, durch eine gestrichelte Linie getrennt, Jesus; im Hintergrund der Tempel.",
     "Die Linie steht für [[JHN.2.24]]: Jesus vertraute sich ihnen nicht an. Wie der Abstand zu verstehen ist, deutet der Text mit [[JHN.2.25]] selbst; das Bild fügt keine Bewertung der Menge hinzu.",
     "E Mängi under goldige Stärn (Zeiche) und, dur e gstrichleti Linie trännt, de Jesus; im Hindergrund de Tämpel.",
     "D Linie staat für [[JHN.2.24]]: De Jesus hät sich ine nöd aavertrout. Wie de Abstand z verstaa isch, düütet de Text mit [[JHN.2.25]] sälber; s Bild füegt kei Wertig vo de Mängi dezue."),
]


def run():
    n = write(D / "illustrations/styles/ILLSTYLE-SYMBOL.json", dict(STYLE))
    for suf, level, ref, target, depicts, alt, note, alt_g, note_g in ILL:
        rid = f"ILL-SYM-{suf}"
        f = D / "illustrations/symbol" / f"{rid}.svg"
        if not f.exists():
            raise SystemExit(f"{rid}: Zeichnung fehlt ({f})")
        depicts = [d.replace("ill-p-zeichen", "ill-zeichen") for d in depicts]
        known = {x[0] for x in FIGURES}
        for d in depicts:
            if d not in known:
                raise SystemExit(f"{rid}: Figur {d} nicht in der Legende")
        rec = {"id": rid, "type": "illustration", "status": "draft", "tags": ["TAG-JOHN"], "style": "ILLSTYLE-SYMBOL",
               "level": level, "reference": ref, "target": target, "file": f"data/illustrations/symbol/{rid}.svg",
               "depicts": depicts, "alt_de": alt, "note_de": note, "license": LIC, "authorship_de": AUTH,
               "knowledge": {"asserted_at": DATE, "supersedes": None}}
        n += write(D / "illustrations/symbol" / f"{rid}.json", rec)
        n += localize(rid, rec, {"alt_de": alt_g, "note_de": note_g}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026", AUTH_GSW, DATE)
    print(f"PASS: Bildsprache Symbol – Stil und {len(ILL)} Bilder; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
