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


ACTIONS_GSW = {'Bei der Hochzeit sagt Maria zu Jesus, dass der Wein ausgegangen ist; Jesus antwortet, seine Stunde sei noch nicht gekommen.': 'A de Hochziit seit d Maria zum Jesus, de Wii seg usgange; de Jesus antwortet, sini Stund seg no nöd choo.', 'Maria sagt zu den Dienern, sie sollen tun, was Jesus ihnen sagt.': 'D Maria seit de Diener, si söled mache, was de Jesus ine säg.', 'Jesus lässt die sechs steinernen Krüge mit Wasser füllen und schickt die Diener zum Speisemeister.': 'De Jesus laat di sächs steinige Chrüeg mit Wasser fülle und schickt d Diener zum Spiismeischter.', 'Der Speisemeister kostet den Wein und spricht zum Bräutigam vom guten Wein; es ist der Anfang der Zeichen, die Jünger glauben an Jesus.': 'De Spiismeischter probiert de Wii und redt mit em Brüütigam vom guete Wii; das isch de Aafang vo de Zeiche, d Jünger glaubed a de Jesus.', 'Jesus treibt mit einer Geissel die Händler, Schafe und Rinder aus dem Tempel, schüttet die Münzen aus und stösst die Tische um.': 'De Jesus tribt mit ere Geissle d Händler, d Schaf und d Rinder us em Tämpel, schüttet s Münz us und heit d Tisch um.', 'Die Juden fragen nach einem Zeichen; Jesus antwortet: Reisst diesen Tempel nieder, in drei Tagen werde ich ihn aufrichten.': 'D Jude fröged nach eme Zeiche; de Jesus antwortet: Riissed dä Tämpel ab, i drüü Täg stell ich en uf.', 'Viele in Jerusalem glauben wegen der Zeichen an Jesus; er vertraut sich ihnen nicht an, weil er weiss, was im Menschen ist.': 'Vili z Jerusalem glaubed wäge de Zeiche a de Jesus; er vertrout sich ine nöd aa, wil er weiss, was im Mänsch isch.', 'Hochzeit zu Kana: Das Wasser in den Krügen ist zu Wein geworden – der Anfang der Zeichen.': 'Hochziit z Kana: S Wasser i de Chrüeg isch zu Wii worde – de Aafang vo de Zeiche.', 'Jesus treibt die Händler aus dem Tempel.': 'De Jesus tribt d Händler us em Tämpel.', 'Viele glauben wegen der Zeichen; Jesus vertraut sich ihnen nicht an.': 'Vili glaubed wäge de Zeiche; de Jesus vertrout sich ine nöd aa.', 'Adler (Evangelistensymbol), Licht, Schriftrolle.': 'Adler (Symbol vom Evangelischt), Liecht, Schriftrolle.'}


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
        rec = {"id": rid, "type": "illustration_brief", "status": "draft", "tags": ["TAG-JOHN"], "level": b["level"],
               "reference": b["reference"], "target": b["target"], "panels": b["panels"],
               "actions_de": [p["action_de"] for p in b["panels"]], "interpretation_note_de": b["note"], "basis": basis,
               "basis_note_de": "Fingerabdrücke des Textes, gegen den der Auftrag geprüft wurde (Verse der hochdeutschen Arbeitsübersetzung, Zusammenfassung des Ziels). "
                                "Bei Abweichung gilt der Auftrag als veraltet, bis er erneut geprüft ist.",
               "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
        n += write(path, rec)
        n += localize(rid, rec, {"interpretation_note_de": b["note_gsw"], "actions_de": [ACTIONS_GSW[p["action_de"]] for p in b["panels"]]}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026", AUTH_GSW, DATE)
    print(f"PASS: {len(BRIEFS)} Bildaufträge; {n} Dateien geschrieben" + (" (Text erneut geprüft und bestätigt)" if confirm else ""))


if __name__ == "__main__":
    run()
