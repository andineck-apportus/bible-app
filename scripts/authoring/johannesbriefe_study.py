#!/usr/bin/env python3
"""Autorenwerkzeug: 1.–3. Johannesbrief – Befunde, Deutungen, Grundsätze, Anwendungen, offene Fragen, Beziehungen,
Hintergrund zu Abschnitten, Kapitel-Zusammenfassungen, Kontext und je eine Studie pro Brief (STUDY-1JN-0001,
STUDY-2JN-0001, STUDY-3JN-0001); jeweils mit Züridüütsch-Lokalisierung. Hintergrund zum ganzen Buch steht in
BG-1JN-BOOK-0001, BG-2JN-BOOK-0001 und BG-3JN-BOOK-0001 (scripts/authoring/hintergrund_buecher.py) und wird hier nicht
geschrieben.

Abschnitte: Jede Aussage nennt den Versbereich, auf den sie sich bezieht; zugeordnet wird die kleinste vorhandene
Texteinheit (data/text-units/TU-1JN-…, TU-2JN-…, TU-3JN-…), die ihn ganz enthält, sonst die Kapiteleinheit. Die
Texteinheiten schreibt scripts/authoring/johannesbriefe_text.py; dieses Werkzeug legt keine an.
Wortzählungen: nach den MACULA-Lemmata zum SBLGNT (data/annotations/MACULA-SBLGNT-1JN-00n.json usw.); check_counts()
prüft vor dem Schreiben jede im Text genannte Zahl an diesen Daten.
Handschriften zu [[1JN.5.7-1JN.5.8]] und [[1JN.4.3]]: nach den CNTR-Sekundärtranskriptionen in data/witness-texts/
(nicht am Faksimile geprüft).

Aufruf: python3 scripts/authoring/johannesbriefe_study.py
KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
"""
import json
import re
import unicodedata
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D  # noqa: E402

TAGS = ["TAG-JOHANNINE"]
CHAPTERS = {("1JN", 1): "TU-1JN-001-001-010", ("1JN", 2): "TU-1JN-002-001-029", ("1JN", 3): "TU-1JN-003-001-024",
            ("1JN", 4): "TU-1JN-004-001-021", ("1JN", 5): "TU-1JN-005-001-021", ("2JN", 1): "TU-2JN-001-001-013",
            ("3JN", 1): "TU-3JN-001-001-014"}
_UNITS = sorted(p.stem for p in (D / "text-units").rglob("TU-*JN-*.json"))


def U(book, ch, v1, v2=None):
    """Kleinste vorhandene Texteinheit, die book ch, Verse v1–v2 ganz enthält; sonst die Kapiteleinheit."""
    v2 = v2 or v1
    best = None
    for uid in _UNITS:
        m = re.fullmatch(r"TU-([123]JN)-(\d{3})-(\d{3})-(\d{3})", uid)
        if m and m[1] == book and int(m[2]) == ch and int(m[3]) <= v1 and int(m[4]) >= v2:
            if best is None or int(m[4]) - int(m[3]) < best[0]:
                best = (int(m[4]) - int(m[3]), uid)
    return best[1] if best else CHAPTERS[(book, ch)]


# ---------------------------------------------------------------------------------------------------------------
# Zählungen: jede im Text genannte Zahl wird hier an den MACULA-Lemmata bzw. SBLGNT-Token geprüft.
def _tokens(book):
    out = []
    for f in sorted((D / "tokens").glob(f"SBLGNT-{book}-*.json")):
        ann = json.loads((D / "annotations" / f"MACULA-{f.stem}.json").read_text(encoding="utf-8"))["entries"]
        for t in json.loads(f.read_text(encoding="utf-8"))["tokens"]:
            e = ann.get(t["id"], {})
            out.append((t["reference"], e.get("lemma"), e.get("morph") or ""))
    return out


def _cv(ref):
    _, c, v = ref.split(".")
    return int(c), int(v)


def check_counts():
    t1, t2, t3 = _tokens("1JN"), _tokens("2JN"), _tokens("3JN")
    n = lambda T, lems, f=lambda r: True: sum(1 for r, lm, _ in T if lm in lems and f(r))
    expect = {
        "1JN Verse": (len({r for r, _, _ in t1}), 105),
        "ἀγαπάω": (n(t1, {"ἀγαπάω"}), 28), "ἀγάπη": (n(t1, {"ἀγάπη"}), 18), "ἀγαπητός": (n(t1, {"ἀγαπητός"}), 6),
        "ἀγαπ- 4,7–21": (n(t1, {"ἀγαπάω", "ἀγάπη"}, lambda r: _cv(r)[0] == 4 and _cv(r)[1] >= 7), 27),
        "ἀγαπ- Kap. 1–2": (n(t1, {"ἀγαπάω", "ἀγάπη"}, lambda r: _cv(r)[0] <= 2), 5),
        "γινώσκω": (n(t1, {"γινώσκω"}), 25), "οἶδα": (n(t1, {"οἶδα"}), 15),
        "οἴδαμεν": (sum(1 for r, lm, m in t1 if lm == "οἶδα" and m.endswith("1P")), 7),
        "ἐν τούτῳ": (sum(1 for i in range(len(t1) - 1) if t1[i][1] == "ἐν" and t1[i + 1][1] == "οὗτος"), 14),
        "μένω": (n(t1, {"μένω"}), 24), "μένω Kap. 2": (n(t1, {"μένω"}, lambda r: _cv(r)[0] == 2), 11),
        "μένω 2JN": (n(t2, {"μένω"}), 3),
        "φῶς": (n(t1, {"φῶς"}), 6), "σκοτία": (n(t1, {"σκοτία"}), 6), "σκότος": (n(t1, {"σκότος"}), 1),
        "Licht/Finsternis nach 2,11": (n(t1, {"φῶς", "σκοτία", "σκότος"}, lambda r: _cv(r) > (2, 11)), 0),
        "κόσμος": (n(t1, {"κόσμος"}), 23), "κόσμος Kap. 4": (n(t1, {"κόσμος"}, lambda r: _cv(r)[0] == 4), 9),
        "ἁμαρτία": (n(t1, {"ἁμαρτία"}), 17), "ἁμαρτάνω": (n(t1, {"ἁμαρτάνω"}), 10),
        "θάνατος 5,16–17": (n(t1, {"θάνατος"}, lambda r: _cv(r)[0] == 5), 4),
        "ἀντίχριστος 1JN": (n(t1, {"ἀντίχριστος"}), 4), "ἀντίχριστος 2JN": (n(t2, {"ἀντίχριστος"}), 1),
        "τεκνίον/παιδίον": (n(t1, {"τεκνίον", "παιδίον"}), 9), "χρῖσμα": (n(t1, {"χρῖσμα"}), 3),
        "ἀλήθεια 1JN": (n(t1, {"ἀλήθεια"}), 9), "ἀλήθεια 2JN": (n(t2, {"ἀλήθεια"}), 5), "ἀλήθεια 3JN": (n(t3, {"ἀλήθεια"}), 6),
        "ἐκκλησία 1JN+2JN": (n(t1, {"ἐκκλησία"}) + n(t2, {"ἐκκλησία"}), 0), "ἐκκλησία 3JN": (n(t3, {"ἐκκλησία"}), 3),
        "διδαχή 2JN": (n(t2, {"διδαχή"}), 3), "ἐντολή 2JN": (n(t2, {"ἐντολή"}), 4),
        "2JN Wörter": (len(t2), 245), "3JN Wörter": (len(t3), 219), "2JN Verse": (len({r for r, _, _ in t2}), 13),
        "3JN Verse": (len({r for r, _, _ in t3}), 14),
    }
    bad = {k: v for k, v in expect.items() if v[0] != v[1]}
    if bad:
        raise SystemExit(f"Zählungen stimmen nicht mit den Daten überein: {bad}")
    # Handschriften und Ausgaben zu 1 Joh 5,7–8 (CNTR)
    comma = {}
    for w in ("GA01", "GA02", "GA03", "ST", "KJTR", "RP", "WH", "SR"):
        v = json.loads((D / "witness-texts" / f"CNTR-{w}-1JN.json").read_text(encoding="utf-8"))["verses"]
        plain = "".join(c for c in unicodedata.normalize("NFD", v.get("1JN.5.7") or "") if not unicodedata.combining(c)).lower()
        comma[w] = "ουραν" in plain
    if comma != {"GA01": False, "GA02": False, "GA03": False, "ST": True, "KJTR": True, "RP": False, "WH": False, "SR": False}:
        raise SystemExit(f"Befund zu 1 Joh 5,7 passt nicht zu den CNTR-Texten: {comma}")


CONTEXT = {"id": "CTX-JOHANNINE-READERS", "type": "context", "status": "draft", "tags": TAGS + ["TAG-UNCERTAINTY"],
           "period": {"from": 90, "to": 110, "era": "CE", "approx": True},
           "region": "Wohl Hausgemeinden in der römischen Provinz Asia; die altkirchliche Überlieferung denkt an Ephesus",
           "language_context": ["grc"],
           "audience": "Gemeinden in der Tradition des Johannesevangeliums nach einer Spaltung (1 Joh), eine befreundete Gemeinde "
                       "(2 Joh) und ein einzelner Gastgeber, Gaius (3 Joh)",
           "note_de": "Datierung und Ort sind erschlossen (meist um 90–110 n. Chr.); siehe BG-1JN-BOOK-0001, BG-2JN-BOOK-0001 und "
                      "BG-3JN-BOOK-0001. Ob alle drei Briefe vom selben Verfasser stammen und an denselben Gemeindekreis gingen, "
                      "ist umstritten (INT-1JN-0006)."}

MAC = "Zählung nach den MACULA-Lemmata zum SBLGNT."
MAC_G = "Zellig nach de MACULA-Lemmata zum SBLGNT."
KONK = " Die Angaben zum übrigen Neuen Testament folgen den gängigen Konkordanzen und sind hier nicht nachgezählt."
KONK_G = " D Aagaabe zum übrige Nöie Teschtamänt folged de gängige Konkordanze und sind da nöd nochezellt."
JHN_NOTE = (" Der griechische Wortlaut des Johannesevangeliums ist im Projekt noch nicht als Token erfasst; die Angaben dazu "
            "folgen dem SBLGNT und sind hier nicht an Projektdaten geprüft.")
JHN_NOTE_G = (" De griechisch Wortluut vom Johannesevangelium isch im Projekt no nöd als Token erfasst; d Aagaabe dezue folged "
              "em SBLGNT und sind da nöd a Projektdate prüeft.")

# =================================================================================================================
# 1. Johannesbrief
# (id, Abschnitt, Art, Aussage, Belege, Konfidenz, Begründung | Mundart: Aussage, Begründung)
FINDINGS_1JN = [
 ("FIND-1JN-0001", U("1JN", 4, 7, 21), "key_terms",
  "Liebe ist das häufigste Leitwort des Briefes: Das Verb «lieben» (ἀγαπάω) steht 28-mal, das Nomen «Liebe» (ἀγάπη) 18-mal, zusammen 46 Belege in 105 Versen; dazu kommt sechsmal die Anrede «Geliebte» (ἀγαπητοί). Mehr als die Hälfte der 46 Belege, nämlich 27, steht in [[1JN.4.7-1JN.4.21]]; in den Kapiteln 1 und 2 sind es nur fünf. Zweimal heisst es «Gott ist Liebe» ([[1JN.4.8]]; [[1JN.4.16]]).",
  ["1JN.2.5", "1JN.2.15", "1JN.3.1", "1JN.3.11-1JN.3.18", "1JN.4.7-1JN.4.21", "1JN.5.1-1JN.5.3"],
  "high", MAC + " Das Adjektiv ἀγαπητός ist nicht in den 46 Belegen enthalten.",
  "Liebi isch s hüüfigscht Leitwort vom Brief: S Verb «liebe» (ἀγαπάω) staat 28 Mal, s Nomen «Liebi» (ἀγάπη) 18 Mal, zäme 46 Beleg i 105 Värs; dezue chunnt sächs Mal d Aarede «Liebi» oder «Gliebti» (ἀγαπητοί). Meh als d Hälfti vo de 46 Beleg, nämli 27, staat i [[1JN.4.7-1JN.4.21]]; i de Kapitel 1 und 2 sind s nu föif. Zwei Mal heisst s «Gott isch Liebi» ([[1JN.4.8]]; [[1JN.4.16]]).",
  MAC_G + " S Adjektiv ἀγαπητός isch nöd i de 46 Beleg drin."),
 ("FIND-1JN-0002", U("1JN", 2, 3, 6), "key_terms",
  "Erkennen und Wissen prägen den Brief: «erkennen» (γινώσκω) steht 25-mal, «wissen» (οἶδα) 15-mal. Typisch ist die Formel «daran (ἐν τούτῳ) erkennen wir»: Sie nennt ein Merkmal, an dem sich etwas zeigt, etwa «daran erkennen wir, dass wir ihn erkannt haben: wenn wir seine Gebote halten» ([[1JN.2.3]]; ähnlich [[1JN.2.5]]; [[1JN.3.16]]; [[1JN.3.19]]; [[1JN.3.24]]; [[1JN.4.2]]; [[1JN.4.13]]; [[1JN.5.2]]). Die Wendung ἐν τούτῳ («darin, daran») kommt insgesamt 14-mal vor. Ob sie auf das Vorangehende oder das Folgende zurückweist, ist an mehreren Stellen nicht eindeutig.",
  ["1JN.2.3-1JN.2.5", "1JN.3.16", "1JN.3.19", "1JN.3.24", "1JN.4.2", "1JN.4.6", "1JN.4.13", "1JN.5.2"],
  "high", MAC + " Die acht genannten Stellen verbinden ἐν τούτῳ mit einer Form von γινώσκω; in [[1JN.4.6]] steht stattdessen ἐκ τούτου.",
  "Erchänne und Wüsse prägted de Brief: «erchänne» (γινώσκω) staat 25 Mal, «wüsse» (οἶδα) 15 Mal. Typisch isch d Formle «dra (ἐν τούτῳ) erchänned mir»: Si nännt es Merkmal, wo sich öppis dra zeigt, öppe «dra erchänned mir, dass mir en erchännt händ: wänn mir sini Gebot halted» ([[1JN.2.3]]; ähnlich [[1JN.2.5]]; [[1JN.3.16]]; [[1JN.3.19]]; [[1JN.3.24]]; [[1JN.4.2]]; [[1JN.4.13]]; [[1JN.5.2]]). D Wändig ἐν τούτῳ («drin, dra») chunnt insgesamt 14 Mal vor. Öb si uf das devor oder uf das dernaa zeigt, isch a meerere Stelle nöd eidüütig.",
  MAC_G + " Di acht gnännte Stelle verbinded ἐν τούτῳ mit ere Form vo γινώσκω; i [[1JN.4.6]] staat statt dem ἐκ τούτου."),
 ("FIND-1JN-0003", U("1JN", 5, 18, 21), "repetition",
  "Siebenmal sagt der Brief «wir wissen» (οἴδαμεν), verteilt auf sechs Verse: dass wir ihm gleich sein werden, wenn er erscheint ([[1JN.3.2]]); dass wir vom Tod ins Leben hinübergegangen sind, weil wir die Geschwister lieben ([[1JN.3.14]]); zweimal, dass Gott hört und wir das Erbetene haben ([[1JN.5.15]]); und am Schluss dreimal hintereinander: dass wer aus Gott geboren ist, nicht sündigt; dass wir aus Gott sind und die ganze Welt im Bösen liegt; dass der Sohn Gottes gekommen ist und uns Einsicht gegeben hat ([[1JN.5.18-1JN.5.20]]). Kurz davor nennt der Brief seinen Zweck: «damit ihr wisst, dass ihr ewiges Leben habt» ([[1JN.5.13]]).",
  ["1JN.3.2", "1JN.3.14", "1JN.5.13", "1JN.5.15", "1JN.5.18-1JN.5.20"],
  "high", MAC + " Gezählt sind Formen von οἶδα in der 1. Person Plural.",
  "Sibe Mal seit de Brief «mir wüssed» (οἴδαμεν), verteilt uf sächs Värs: dass mir em gliich sii wärded, wänn er erschiint ([[1JN.3.2]]); dass mir vom Tod is Läbe übere gange sind, wil mir d Gschwüschterti liebed ([[1JN.3.14]]); zwei Mal, dass Gott ghört und mir das händ, wo mir drum bätted händ ([[1JN.5.15]]); und am Schluss drüü Mal hinderenand: dass wär us Gott gebore isch, nöd sündiget; dass mir us Gott sind und di ganz Wält im Böse liit; dass de Sohn vo Gott cho isch und üs Iisicht gää hät ([[1JN.5.18-1JN.5.20]]). Churz devor nännt de Brief sin Zwäck: «demit ir wüssed, dass ir ewigs Läbe händ» ([[1JN.5.13]]).",
  MAC_G + " Zellt sind Forme vo οἶδα i de 1. Person Plural."),
 ("FIND-1JN-0004", U("1JN", 2, 24, 28), "key_terms",
  "«Bleiben» (μένω) steht im Brief 24-mal, elfmal davon in Kapitel 2; im 2. Johannesbrief noch dreimal. Es bezeichnet eine dauernde, gegenseitige Verbundenheit: «Wer seine Gebote hält, bleibt in ihm und er in ihm» ([[1JN.3.24]]; ähnlich [[1JN.4.13]]; [[1JN.4.15-1JN.4.16]]). Bleiben sollen auch das von Anfang an Gehörte ([[1JN.2.24]]) und die «Salbung» (χρῖσμα, [[1JN.2.27]]). Den Gegensatz bilden die Weggegangenen: «Wären sie von uns gewesen, so wären sie bei uns geblieben» ([[1JN.2.19]]).",
  ["1JN.2.6", "1JN.2.19", "1JN.2.24-1JN.2.28", "1JN.3.24", "1JN.4.13-1JN.4.16", "2JN.1.2", "2JN.1.9"],
  "high", MAC,
  "«Bliibe» (μένω) staat im Brief 24 Mal, elf Mal devo im Kapitel 2; im 2. Johannesbrief no drüü Mal. Es meint e dauerndi, gägesiitigi Verbundeheit: «Wär sini Gebot haltet, bliibt in im und er in im» ([[1JN.3.24]]; ähnlich [[1JN.4.13]]; [[1JN.4.15-1JN.4.16]]). Bliibe söled au das, wo me vo Aafang aa ghört hät ([[1JN.2.24]]), und d «Salbig» (χρῖσμα, [[1JN.2.27]]). S Gägestück sind die, wo wäggange sind: «Wänn si vo üs gsii wäred, wäred si bi üs blibe» ([[1JN.2.19]]).",
  MAC_G),
 ("FIND-1JN-0005", U("1JN", 1, 5, 10), "key_terms",
  "Licht und Finsternis rahmen den ersten Teil: «Licht» (φῶς) steht sechsmal, «Finsternis» (σκοτία) sechsmal und das gleichbedeutende σκότος einmal, alle in [[1JN.1.5-1JN.2.11]] und danach nicht mehr. Der Abschnitt beginnt mit «Gott ist Licht, und Finsternis ist in ihm keine» ([[1JN.1.5]]) und endet mit dem, der seinen Bruder hasst und «nicht weiss, wohin er geht, weil die Finsternis seine Augen geblendet hat» ([[1JN.2.11]]). Mit dem «Wandeln im Licht» verbindet der Abschnitt die Gemeinschaft miteinander, die Reinigung von Sünde und die Liebe zum Bruder ([[1JN.1.7-1JN.1.9]]; [[1JN.2.10]]).",
  ["1JN.1.5-1JN.1.7", "1JN.2.8-1JN.2.11"],
  "high", MAC,
  "Liecht und Fiischteri raamed de erscht Teil ii: «Liecht» (φῶς) staat sächs Mal, «Fiischteri» (σκοτία) sächs Mal und s gliichbedüütend σκότος ei Mal, alli i [[1JN.1.5-1JN.2.11]] und dernaa nüme. De Abschnitt fangt aa mit «Gott isch Liecht, und Fiischteri isch kei i im» ([[1JN.1.5]]) und hört uf mit dem, wo sin Brueder hasst und «nöd weiss, wo n er hiigaat, wil d Fiischteri sini Auge blendet hät» ([[1JN.2.11]]). Mit em «Laufe im Liecht» verbindet de Abschnitt d Gmeinschaft mitenand, s Reinige vo de Sünd und d Liebi zum Brueder ([[1JN.1.7-1JN.1.9]]; [[1JN.2.10]]).",
  MAC_G),
 ("FIND-1JN-0006", U("1JN", 2, 15, 17), "key_terms",
  "«Welt» (κόσμος) steht 23-mal, neunmal davon in Kapitel 4, und hat zwei Seiten. Einerseits ist sie Ziel von Gottes Handeln: Christus ist Sühne «für die ganze Welt» ([[1JN.2.2]]), Gott hat seinen Sohn «in die Welt» gesandt ([[1JN.4.9]]) als «Retter der Welt» ([[1JN.4.14]]). Andererseits steht sie Gott gegenüber: «Liebt nicht die Welt» ([[1JN.2.15-1JN.2.17]]), sie kennt die Glaubenden nicht ([[1JN.3.1]]), die falschen Propheten sind «aus der Welt» ([[1JN.4.5]]), und «die ganze Welt liegt im Bösen» ([[1JN.5.19]]). Der Glaube «besiegt die Welt» ([[1JN.5.4-1JN.5.5]]).",
  ["1JN.2.2", "1JN.2.15-1JN.2.17", "1JN.3.1", "1JN.4.1-1JN.4.5", "1JN.4.9", "1JN.4.14", "1JN.5.4-1JN.5.5", "1JN.5.19"],
  "high", MAC + " Die Einteilung in zwei Seiten ist eine Beobachtung am Wortlaut; einzelne Stellen lassen sich auch neutral lesen («in dieser Welt», [[1JN.4.17]]).",
  "«Wält» (κόσμος) staat 23 Mal, nüün Mal devo im Kapitel 4, und hät zwei Siite. Einersiits isch si s Ziil vo Gottes Handle: Christus isch Süeni «für di ganz Wält» ([[1JN.2.2]]), Gott hät sin Sohn «i d Wält» gschickt ([[1JN.4.9]]) als «Retter vo de Wält» ([[1JN.4.14]]). Andersiits staat si Gott gägenüber: «Liebed nöd d Wält» ([[1JN.2.15-1JN.2.17]]), si kännt d Gläubige nöd ([[1JN.3.1]]), di falsche Prophete sind «us de Wält» ([[1JN.4.5]]), und «di ganz Wält liit im Böse» ([[1JN.5.19]]). De Glaube «bsiegt d Wält» ([[1JN.5.4-1JN.5.5]]).",
  MAC_G + " D Iiteilig i zwei Siite isch e Beobachtig am Wortluut; einzelni Stelle cha me au neutral läse («i dere Wält», [[1JN.4.17]])."),
 ("FIND-1JN-0007", U("1JN", 1, 5, 10), "argument_structure",
  "Der Brief prüft Ansprüche an ihren Folgen. Dreimal beginnt er mit «wenn wir sagen» ([[1JN.1.6]]; [[1JN.1.8]]; [[1JN.1.10]]), dreimal mit «wer sagt» ([[1JN.2.4]]; [[1JN.2.6]]; [[1JN.2.9]]), dazu «wenn jemand sagt: Ich liebe Gott» ([[1JN.4.20]]). Als Prüfsteine nennt er immer wieder drei Dinge: Gottes Gebote halten und leben, wie Jesus gelebt hat ([[1JN.2.3-1JN.2.6]]; [[1JN.3.24]]; [[1JN.5.2-1JN.5.3]]); die Geschwister lieben ([[1JN.2.9-1JN.2.11]]; [[1JN.3.14]]; [[1JN.4.20-1JN.4.21]]); bekennen, dass Jesus der Christus, der Sohn Gottes und im Fleisch gekommen ist ([[1JN.2.22-1JN.2.23]]; [[1JN.4.2-1JN.4.3]]; [[1JN.4.15]]; [[1JN.5.1]]; [[1JN.5.5]]). In [[1JN.3.23]] stehen Glaube und Liebe in einem Gebot beisammen.",
  ["1JN.1.6-1JN.1.10", "1JN.2.3-1JN.2.11", "1JN.2.22-1JN.2.23", "1JN.3.23-1JN.3.24", "1JN.4.2-1JN.4.3", "1JN.4.20-1JN.4.21", "1JN.5.1-1JN.5.5"],
  "high", "Beobachtung am Wortlaut; die Bündelung zu drei Prüfsteinen ist eine verbreitete Lesehilfe (etwa schon bei Robert Law, 1909: «The Tests of Life»), keine Gliederung, die der Brief selbst ausweist.",
  "De Brief prüeft Aasprüch a ire Folge. Drüü Mal fangt er aa mit «wänn mir säged» ([[1JN.1.6]]; [[1JN.1.8]]; [[1JN.1.10]]), drüü Mal mit «wär seit» ([[1JN.2.4]]; [[1JN.2.6]]; [[1JN.2.9]]), dezue «wänn öpper seit: Ich lieb Gott» ([[1JN.4.20]]). Als Prüefstei nännt er immer wider drüü Sache: Gottes Gebot halte und läbe, wie de Jesus gläbt hät ([[1JN.2.3-1JN.2.6]]; [[1JN.3.24]]; [[1JN.5.2-1JN.5.3]]); d Gschwüschterti liebe ([[1JN.2.9-1JN.2.11]]; [[1JN.3.14]]; [[1JN.4.20-1JN.4.21]]); bekänne, dass de Jesus de Christus, de Sohn vo Gott und im Fleisch cho isch ([[1JN.2.22-1JN.2.23]]; [[1JN.4.2-1JN.4.3]]; [[1JN.4.15]]; [[1JN.5.1]]; [[1JN.5.5]]). I [[1JN.3.23]] staat Glaube und Liebi i eim Gebot binenand.",
  "Beobachtig am Wortluut; d Bündelig zu drüü Prüefstei isch e verbreiteti Läsehilf (öppe scho bim Robert Law, 1909: «The Tests of Life»), kei Gliderig, wo de Brief sälber uuswiist."),
 ("FIND-1JN-0008", U("1JN", 1, 1, 4), "parallel_text",
  "Der Anfang des Briefes ([[1JN.1.1-1JN.1.4]]) teilt viele Wörter mit dem Prolog des Johannesevangeliums ([[JHN.1.1-JHN.1.14]]): «Anfang» (ἀρχή), «Wort» (λόγος), «Leben» (ζωή), «war bei» (ἦν πρός: «beim Vater» [[1JN.1.2]], «bei Gott» [[JHN.1.1]]), «wir haben geschaut» (ἐθεασάμεθα, [[1JN.1.1]]; [[JHN.1.14]]). Bald darauf folgen «Licht» und «Finsternis» ([[1JN.1.5]]; [[JHN.1.5]]). Später kehren «eingeboren» (μονογενής, [[1JN.4.9]]; [[JHN.1.14]]; [[JHN.1.18]]) und der Satz «Gott hat niemand je gesehen» wieder ([[1JN.4.12]]; [[JHN.1.18]], dort mit einem anderen Verb für «sehen»). Die Unterschiede: Der Brief beginnt mit dem sächlichen «Was» (ὅ), sagt «von Anfang an» (ἀπ' ἀρχῆς) statt «im Anfang», spricht vom «Wort des Lebens» statt vom Wort, das Gott war, und betont Hören, Sehen und Betasten (ψηλαφάω).",
  ["1JN.1.1-1JN.1.5", "1JN.4.9", "1JN.4.12", "JHN.1.1-JHN.1.18"],
  "high", "Beobachtung am Wortlaut." + JHN_NOTE,
  "De Aafang vom Brief ([[1JN.1.1-1JN.1.4]]) teilt vili Wörter mit em Prolog vom Johannesevangelium ([[JHN.1.1-JHN.1.14]]): «Aafang» (ἀρχή), «Wort» (λόγος), «Läbe» (ζωή), «isch gsii bi» (ἦν πρός: «bim Vatter» [[1JN.1.2]], «bi Gott» [[JHN.1.1]]), «mir händ gschaut» (ἐθεασάμεθα, [[1JN.1.1]]; [[JHN.1.14]]). Bald druf chömed «Liecht» und «Fiischteri» ([[1JN.1.5]]; [[JHN.1.5]]). Spööter chömed «eigebore» (μονογενής, [[1JN.4.9]]; [[JHN.1.14]]; [[JHN.1.18]]) und de Satz «Gott hät nie öpper gseh» wider ([[1JN.4.12]]; [[JHN.1.18]], dört mit eme andere Verb für «gseh»). D Underschiid: De Brief fangt mit em sächliche «Was» (ὅ) aa, seit «vo Aafang aa» (ἀπ' ἀρχῆς) statt «im Aafang», redt vom «Wort vom Läbe» statt vom Wort, wo Gott gsii isch, und betont Ghööre, Gseh und Aalange (ψηλαφάω).",
  "Beobachtig am Wortluut." + JHN_NOTE_G),
 ("FIND-1JN-0009", U("1JN", 3, 4, 10), "argument_structure",
  "Über Sünde sagt der Brief scheinbar Gegensätzliches. Einerseits: «Wenn wir sagen, wir haben keine Sünde, betrügen wir uns selbst» ([[1JN.1.8]]; vgl. [[1JN.1.10]]), und «wenn jemand sündigt, haben wir einen Beistand beim Vater» ([[1JN.2.1]]). Andererseits: «Jeder, der in ihm bleibt, sündigt nicht» ([[1JN.3.6]]), und «jeder, der aus Gott geboren ist, tut keine Sünde … und er kann nicht sündigen, weil er aus Gott geboren ist» ([[1JN.3.9]]; vgl. [[1JN.5.18]]). «Sünde» (ἁμαρτία) steht 17-mal, «sündigen» (ἁμαρτάνω) zehnmal. In [[1JN.3.4]] wird Sünde als «Gesetzlosigkeit» (ἀνομία) bestimmt.",
  ["1JN.1.8-1JN.2.2", "1JN.3.4-1JN.3.10", "1JN.5.16-1JN.5.18"],
  "high", MAC + " Wie sich die Aussagen zueinander verhalten, ist Deutung (INT-1JN-0002).",
  "Über Sünd seit de Brief schiinbar Gägesätzlichs. Einersiits: «Wänn mir säged, mir heged kei Sünd, betrüged mir üs sälber» ([[1JN.1.8]]; vgl. [[1JN.1.10]]), und «wänn öpper sündiget, händ mir en Biistand bim Vatter» ([[1JN.2.1]]). Andersiits: «Jede, wo in im bliibt, sündiget nöd» ([[1JN.3.6]]), und «jede, wo us Gott gebore isch, tuet kei Sünd … und er cha nöd sündige, wil er us Gott gebore isch» ([[1JN.3.9]]; vgl. [[1JN.5.18]]). «Sünd» (ἁμαρτία) staat 17 Mal, «sündige» (ἁμαρτάνω) zää Mal. I [[1JN.3.4]] wird Sünd als «Gsetzlosigkeit» (ἀνομία) bestimmt.",
  MAC_G + " Wie sich d Aussage zuenand verhalted, isch Düütig (INT-1JN-0002)."),
 ("FIND-1JN-0010", U("1JN", 5, 13, 17), "terminology",
  "In [[1JN.5.16-1JN.5.17]] unterscheidet der Brief «Sünde nicht zum Tod» (ἁμαρτία μὴ πρὸς θάνατον) und «Sünde zum Tod» (ἁμαρτία πρὸς θάνατον); θάνατος steht dort viermal. Für die erste soll man bitten (αἰτέω), und Gott wird Leben geben; über die zweite sagt der Verfasser: «nicht von jener sage ich, dass man bitten (ἐρωτάω) soll». Ein ausdrückliches Verbot steht nicht da. Welche Sünde gemeint ist, sagt der Brief nicht; er fügt an: «Jede Ungerechtigkeit ist Sünde, und es gibt Sünde nicht zum Tod» ([[1JN.5.17]]).",
  ["1JN.5.14-1JN.5.17"], "high", MAC + " Der Wechsel von αἰτέω zu ἐρωτάω ist beobachtet; ob er etwas bedeutet, ist Deutung.",
  "I [[1JN.5.16-1JN.5.17]] underscheidet de Brief «Sünd nöd zum Tod» (ἁμαρτία μὴ πρὸς θάνατον) und «Sünd zum Tod» (ἁμαρτία πρὸς θάνατον); θάνατος staat dört vier Mal. Für di erscht söll me bitte (αἰτέω), und Gott wird Läbe gää; über di zweit seit de Verfasser: «nöd vo dere säg ich, dass me söll bitte (ἐρωτάω)». Es usdrücklichs Verbot staat nöd da. Weli Sünd gmeint isch, seit de Brief nöd; er füegt aa: «Jedi Ungrächtigkeit isch Sünd, und es git Sünd nöd zum Tod» ([[1JN.5.17]]).",
  MAC_G + " De Wächsel vo αἰτέω zu ἐρωτάω isch beobachtet; öb er öppis bedüütet, isch Düütig."),
 ("FIND-1JN-0011", U("1JN", 5, 6, 12), "text_critical",
  "Das sogenannte «Comma Johanneum» fehlt in den alten griechischen Handschriften, die im Projekt vorliegen: In den Transkriptionen von Codex Sinaiticus (WIT-GA-01, 4. Jh.), Codex Vaticanus (WIT-GA-03, 4. Jh.) und Codex Alexandrinus (WIT-GA-02, 5. Jh.) lautet [[1JN.5.7-1JN.5.8]] nur: «Denn drei sind es, die bezeugen: der Geist und das Wasser und das Blut, und die drei sind auf das eine hin.» Den Zusatz «im Himmel: der Vater, das Wort und der Heilige Geist, und diese drei sind eins; und drei sind es, die bezeugen auf der Erde» haben unter den vorliegenden Ausgaben nur der Textus Receptus nach Stephanus (ED-ST) und der griechische Text hinter der King-James-Bibel (ED-KJTR). Byzantinischer Mehrheitstext (ED-RP), Westcott-Hort (ED-WH), SR und SBLGNT haben ihn nicht; auch die Elberfelder Bibel von 1905 übersetzt ihn nicht.",
  ["1JN.5.6-1JN.5.8"], "high",
  "Nach den CNTR-Sekundärtranskriptionen (data/witness-texts/CNTR-GA01-1JN, -GA02-1JN, -GA03-1JN) und den CNTR-Ausgabentexten; nicht am Faksimile bzw. an den gedruckten Ausgaben geprüft. Codex Ephraemi (GA 04) und Papyrus 9 enthalten die Stelle nicht. Zur späteren Geschichte siehe BG-1JN-0005.",
  "S sogenannt «Comma Johanneum» fäält i de alte griechische Handschrifte, wo im Projekt vorlieged: I de Transkriptione vom Codex Sinaiticus (WIT-GA-01, 4. Jh.), vom Codex Vaticanus (WIT-GA-03, 4. Jh.) und vom Codex Alexandrinus (WIT-GA-02, 5. Jh.) heisst [[1JN.5.7-1JN.5.8]] nu: «Dänn drüü sind s, wo bezüüged: de Geischt und s Wasser und s Bluet, und di drüü sind uf s Eint hii.» De Zuesatz «im Himmel: de Vatter, s Wort und de Heilig Geischt, und die drüü sind eis; und drüü sind s, wo bezüüged uf de Erde» händ under de vorliegende Usgaabe nu de Textus Receptus nach em Stephanus (ED-ST) und de griechisch Text hinder de King-James-Bible (ED-KJTR). De byzantinisch Meerheitstext (ED-RP), Westcott-Hort (ED-WH), SR und SBLGNT händ en nöd; au d Elberfelder Bible vo 1905 übersetzt en nöd.",
  "Nach de CNTR-Sekundärtranskriptione (data/witness-texts/CNTR-GA01-1JN, -GA02-1JN, -GA03-1JN) und de CNTR-Usgaabetext; nöd am Faksimile bzw. a de druckte Usgaabe prüeft. De Codex Ephraemi (GA 04) und de Papyrus 9 händ d Stell nöd. Zur spöötere Gschicht lueg BG-1JN-0005."),
 ("FIND-1JN-0012", U("1JN", 4, 1, 6), "text_critical",
  "In [[1JN.4.3]] ist der Wortlaut des Bekenntnisses unterschiedlich überliefert. Im SBLGNT (wie bei Westcott-Hort, Tregelles und NA28) steht kurz: «jeder Geist, der Jesus nicht bekennt». Der byzantinische Text (ED-RP) und der Textus Receptus haben die längere Form «der nicht bekennt, dass Jesus Christus im Fleisch gekommen ist», wie in [[1JN.4.2]] (VAR-SBLGNTAPP-1JN-004-003-02). In den Transkriptionen hat Codex Sinaiticus eine längere Form mit «Herr» und «im Fleisch gekommen», Codex Alexandrinus und Codex Vaticanus die kurze.",
  ["1JN.4.2-1JN.4.3"], "high",
  "Editionen nach dem SBLGNT-Apparat (VAR-SBLGNTAPP-1JN-004-003-01 und -02); Handschriften nach den CNTR-Sekundärtranskriptionen, nicht am Faksimile geprüft. Eine in der Literatur oft genannte lateinische Lesart («der Jesus auflöst») ist im Projekt nicht erfasst und wird hier nicht ausgewertet.",
  "I [[1JN.4.3]] isch de Wortluut vom Bekänntnis verschide überliferet. Im SBLGNT (wie bi Westcott-Hort, Tregelles und NA28) staat churz: «jede Geischt, wo de Jesus nöd bekännt». De byzantinisch Text (ED-RP) und de Textus Receptus händ di länger Form «wo nöd bekännt, dass de Jesus Christus im Fleisch cho isch», wie i [[1JN.4.2]] (VAR-SBLGNTAPP-1JN-004-003-02). I de Transkriptione hät de Codex Sinaiticus e längeri Form mit «Herr» und «im Fleisch cho», de Codex Alexandrinus und de Codex Vaticanus di churz.",
  "Editione nach em SBLGNT-Apparat (VAR-SBLGNTAPP-1JN-004-003-01 und -02); Handschrifte nach de CNTR-Sekundärtranskriptione, nöd am Faksimile prüeft. E latiinischi Läsart, wo i de Literatur oft gnännt wird («wo de Jesus uflööst»), isch im Projekt nöd erfasst und wird da nöd uusgwärtet."),
 ("FIND-1JN-0013", U("1JN", 2, 18, 23), "key_terms",
  "Das Wort «Antichrist» (ἀντίχριστος) steht im Neuen Testament nur in den Johannesbriefen: viermal im ersten ([[1JN.2.18]] zweimal, [[1JN.2.22]]; [[1JN.4.3]]) und einmal im zweiten ([[2JN.1.7]]). Die Leser haben gehört, «dass der Antichrist kommt»; jetzt aber «sind viele Antichristen geworden» ([[1JN.2.18]]). Bestimmt wird der Antichrist nicht als einzelne Endzeitgestalt, sondern über ein Bekenntnis: wer leugnet, dass Jesus der Christus ist, und so Vater und Sohn leugnet ([[1JN.2.22]]), bzw. wer Jesus nicht bekennt ([[1JN.4.3]]; vgl. [[2JN.1.7]]).",
  ["1JN.2.18-1JN.2.23", "1JN.4.3", "2JN.1.7"], "high", MAC + KONK,
  "S Wort «Antichrischt» (ἀντίχριστος) staat im Nöie Teschtamänt nu i de Johannesbrief: vier Mal im erschte ([[1JN.2.18]] zwei Mal, [[1JN.2.22]]; [[1JN.4.3]]) und ei Mal im zweite ([[2JN.1.7]]). D Läser händ ghört, «dass de Antichrischt chunnt»; jetzt aber «sind vili Antichrischte worde» ([[1JN.2.18]]). De Antichrischt wird nöd als einzelni Gstalt vo de Ändziit bestimmt, sondern über es Bekänntnis: wär abstriitet, dass de Jesus de Christus isch, und eso Vatter und Sohn abstriitet ([[1JN.2.22]]), bzw. wär de Jesus nöd bekännt ([[1JN.4.3]]; vgl. [[2JN.1.7]]).",
  MAC_G + KONK_G),
 ("FIND-1JN-0014", U("1JN", 2, 1, 2), "terminology",
  "Zwei Wörter für das Werk Christi stehen in [[1JN.2.1-1JN.2.2]] beisammen: «Beistand» (παράκλητος) und «Sühne» (ἱλασμός). Im Johannesevangelium heisst παράκλητος der Geist, den der Vater senden wird, dort «ein anderer Beistand» ([[JHN.14.16]]; [[JHN.14.26]]; [[JHN.15.26]]; [[JHN.16.7]]); im Brief ist es Jesus Christus selbst, «beim Vater». ἱλασμός steht im Neuen Testament nur hier und in [[1JN.4.10]]: Gott «hat seinen Sohn gesandt als Sühne für unsere Sünden».",
  ["1JN.2.1-1JN.2.2", "1JN.4.10", "JHN.14.16", "JHN.14.26", "JHN.15.26", "JHN.16.7"], "high",
  "Beobachtung am Wortlaut." + KONK + JHN_NOTE,
  "Zwei Wörter für s Wärch vo Christus staat i [[1JN.2.1-1JN.2.2]] binenand: «Biistand» (παράκλητος) und «Süeni» (ἱλασμός). Im Johannesevangelium heisst παράκλητος de Geischt, wo de Vatter wird schicke, dört «en andere Biistand» ([[JHN.14.16]]; [[JHN.14.26]]; [[JHN.15.26]]; [[JHN.16.7]]); im Brief isch s de Jesus Christus sälber, «bim Vatter». ἱλασμός staat im Nöie Teschtamänt nu da und i [[1JN.4.10]]: Gott «hät sin Sohn gschickt als Süeni für öisi Sünde».",
  "Beobachtig am Wortluut." + KONK_G + JHN_NOTE_G),
 ("FIND-1JN-0015", U("1JN", 2, 12, 14), "literary_structure",
  "Der Verfasser nennt sich nie mit Namen, redet die Leser aber familiär an: «Kinder» (τεκνία) siebenmal und παιδία zweimal, zusammen neunmal, dazu sechsmal «Geliebte». In [[1JN.2.12-1JN.2.14]] stehen sechs Sätze in zwei Dreiergruppen: dreimal «ich schreibe euch» (γράφω), dann dreimal «ich habe euch geschrieben» (ἔγραψα), jeweils an Kinder, Väter und junge Männer, mit einem Grund («weil …»). Das «Wir» des Anfangs ([[1JN.1.1-1JN.1.4]]) wechselt mit einem «Ich» ab ([[1JN.2.1]]; [[1JN.2.7]]; [[1JN.5.13]]).",
  ["1JN.1.1-1JN.1.4", "1JN.2.1", "1JN.2.12-1JN.2.14", "1JN.5.13"], "high", MAC,
  "De Verfasser nännt sich nie mit Name, redt d Läser aber familiär aa: «Chind» (τεκνία) sibe Mal und παιδία zwei Mal, zäme nüün Mal, dezue sächs Mal «Gliebti». I [[1JN.2.12-1JN.2.14]] staat sächs Sätz i zwei Dreiergruppe: drüü Mal «ich schriibe eu» (γράφω), dänn drüü Mal «ich ha eu gschribe» (ἔγραψα), jedes Mal a Chind, Vätter und jungi Manne, mit eme Grund («wil …»). S «Mir» vom Aafang ([[1JN.1.1-1JN.1.4]]) wächslet mit eme «Ich» ab ([[1JN.2.1]]; [[1JN.2.7]]; [[1JN.5.13]]).",
  MAC_G),
]

# (id, Abschnitt, gestützt auf, Aussage, Konfidenz, Vorbehalt, Gegenargumente, Fachwörter | Mundart: Aussage, Vorbehalt, Gegenargumente, Fachwörter)
INTERPRETATIONS_1JN = [
 ("INT-1JN-0001", U("1JN", 4, 1, 6), ["FIND-1JN-0007", "FIND-1JN-0012", "FIND-1JN-0013"],
  "Die Weggegangenen ([[1JN.2.19]]) setzten am ehesten die Bedeutung des irdischen Lebens und Sterbens Jesu herab: Sie bekannten nicht, dass Jesus Christus «im Fleisch gekommen» ist ([[1JN.4.2-1JN.4.3]]), und trennten womöglich den Menschen Jesus vom himmlischen Christus ([[1JN.2.22]]). Darauf antwortet «nicht im Wasser allein, sondern im Wasser und im Blut» ([[1JN.5.6]]): Der Christus ist auch im Tod Jesu gegenwärtig. Eine Lehre dieser Art schreibt Irenäus dem Kerinth zu (BG-1JN-0001); welche Gruppe genau gemeint ist, lässt sich nicht festlegen.",
  "possible",
  "Die Gegner werden nur aus der Polemik des Briefes erschlossen; er nennt keine Namen und referiert ihre Lehre nicht. Zuordnungen zu später bekannten Gruppen sind Rekonstruktionen.",
  ["Andere denken an Doketen, die lehrten, Christus habe nur scheinbar einen Leib gehabt und nur scheinbar gelitten; gegen solche Leute schreibt Ignatius von Antiochien um 110 n. Chr. (BG-1JN-0002). Dazu passt «im Fleisch gekommen» gut, weniger gut die Leugnung, «dass Jesus der Christus ist» ([[1JN.2.22]]).",
   "Andere lesen [[1JN.2.22]] wörtlich als jüdische Bestreitung der Messianität Jesu, wie sie das Johannesevangelium voraussetzt ([[JHN.9.22]]); dagegen spricht, dass die Gegner «von uns ausgegangen» sind ([[1JN.2.19]]) und der Brief keinen Streit um die Tora führt.",
   "Raymond E. Brown (The Community of the Beloved Disciple, 1979) sieht in beiden Gruppen Erben des Johannesevangeliums, die es verschieden auslegten: Die Weggegangenen hätten die Gottheit Jesu und die eigene Geistbegabung so betont, dass sein Menschsein und das sittliche Verhalten unwichtig wurden.",
   "Wieder andere bezweifeln, dass hinter allen Aussagen eine fest umrissene Gegnergruppe steht: Viele Sätze ermahnen die eigene Gemeinde und lassen sich ohne Bezug auf eine Irrlehre lesen."],
  [("grc", "ἐν σαρκί", "im Fleisch, in leiblicher Wirklichkeit"), ("grc", "δοκέω", "scheinen; davon «Doketismus»: Christus sei nur scheinbar Mensch gewesen")],
  "Die, wo wäggange sind ([[1JN.2.19]]), händ am eheschte d Bedüütig vom irdische Läbe und Stärbe vom Jesus chlii gmacht: Si händ nöd bekännt, dass de Jesus Christus «im Fleisch cho» isch ([[1JN.4.2-1JN.4.3]]), und händ vilicht de Mänsch Jesus vom himmlische Christus trännt ([[1JN.2.22]]). Druf antwortet «nöd im Wasser allei, sondern im Wasser und im Bluet» ([[1JN.5.6]]): De Christus isch au im Tod vom Jesus gägewärtig. E Lehr vo dere Art schriibt de Irenäus em Kerinth zue (BG-1JN-0001); weli Gruppe gnau gmeint isch, cha me nöd feschtlegge.",
  "D Gägner wärded nu us de Polemik vom Brief erschlosse; er nännt kei Näme und referiert iri Lehr nöd. Zueornige zu Gruppe, wo me spööter kännt, sind Rekonstruktione.",
  ["Anderi dänked a Doketischte, wo glehrt händ, Christus heb nu schiinbar en Liib gha und nu schiinbar glitte; gäge settigi Lüüt schriibt de Ignatius vo Antiochie um 110 n. Chr. (BG-1JN-0002). Dezue passt «im Fleisch cho» guet, weniger guet s Abstriite, «dass de Jesus de Christus isch» ([[1JN.2.22]]).",
   "Anderi läsed [[1JN.2.22]] wörtlich als jüdischs Abstriite, dass de Jesus de Messias isch, wie s s Johannesevangelium voruussetzt ([[JHN.9.22]]); dergäge spricht, dass d Gägner «vo üs uusgange» sind ([[1JN.2.19]]) und de Brief kei Striit um d Tora füert.",
   "De Raymond E. Brown (The Community of the Beloved Disciple, 1979) gseht i beidne Gruppe Erbe vom Johannesevangelium, wo s verschide uusgleit händ: Die, wo wäggange sind, hebed d Gottheit vom Jesus und di eiget Geischtbegaabig so betont, dass sis Mänschsii und s sittlich Verhalte unwichtig worde sind.",
   "No anderi bezwiifled, dass hinder allne Aussage e fescht umrisseni Gägnergruppe staat: Vili Sätz ermahned di eiget Gmeind und lönd sich ohni Bezug uf e Irrlehr läse."],
  ["im Fleisch, i liiblicher Würklichkeit", "schiine; devo «Doketismus»: Christus seg nu schiinbar Mänsch gsii"]),
 ("INT-1JN-0002", U("1JN", 3, 4, 10), ["FIND-1JN-0009"],
  "Die Sätze «wer aus Gott geboren ist, sündigt nicht» ([[1JN.3.6]]; [[1JN.3.9]]) beschreiben am ehesten die Grundrichtung eines Lebens, nicht völlige Sündlosigkeit: Wer aus Gott geboren ist, lebt nicht dauerhaft und mit Zustimmung in der Sünde. Dafür wird angeführt, dass die griechischen Verben hier im Präsens stehen, das eine andauernde Handlung ausdrücken kann, und dass derselbe Brief Sünde bei Glaubenden voraussetzt ([[1JN.1.8-1JN.2.2]]).",
  "possible",
  "Die Bevorzugung ist eine redaktionelle Abwägung. Das Argument mit dem Präsens trägt nur begrenzt: Auch [[1JN.1.8]] und [[1JN.5.16]] stehen im Präsens und meinen Sünde bei Glaubenden.",
  ["Andere sehen zwei Fronten: [[1JN.1.8-1JN.1.10]] richte sich gegen Leute, die sich für sündlos hielten, [[1JN.3.4-1JN.3.10]] gegen Leute, die Sünde für bedeutungslos erklärten; die Aussagen sollten nicht zum Ausgleich gebracht werden.",
   "Andere lesen [[1JN.3.9]] als Aussage über das, was die Geburt aus Gott ihrem Wesen nach bewirkt («kann nicht»), während [[1JN.1.8]] die noch nicht vollendete Wirklichkeit beschreibt; beides gelte zugleich (in der Reformation zugespitzt als «gerecht und Sünder zugleich»).",
   "Andere verstehen «Sünde» in Kapitel 3 eng als «Gesetzlosigkeit» (ἀνομία, [[1JN.3.4]]) im Sinn des endzeitlichen Abfalls, etwa der Leugnung Christi; diese Sünde begehe, wer aus Gott geboren ist, nicht.",
   "Wieder andere nehmen die Sätze als Ideal oder Anspruch, an dem sich die Gemeinde messen soll, ohne dass der Verfasser behauptet, es sei schon erreicht."],
  [("grc", "ἁμαρτία", "Sünde"), ("grc", "ἀνομία", "Gesetzlosigkeit"), ("grc", "σπέρμα", "Same")],
  "D Sätz «wär us Gott gebore isch, sündiget nöd» ([[1JN.3.6]]; [[1JN.3.9]]) beschriibed am eheschte d Grundrichtig vo me Läbe, nöd völligi Sündlosigkeit: Wär us Gott gebore isch, läbt nöd duurend und mit Zuestimmig i de Sünd. Defür wird aagfüert, dass di griechische Verbe da im Präsens staat, wo e duurendi Handlig cha uusdrücke, und dass de gliich Brief Sünd bi Gläubige voruussetzt ([[1JN.1.8-1JN.2.2]]).",
  "D Bevorzugig isch e redaktionelli Abwägig. S Argumänt mit em Präsens treit nu bedingt: Au [[1JN.1.8]] und [[1JN.5.16]] staat im Präsens und meined Sünd bi Gläubige.",
  ["Anderi gsend zwei Fronte: [[1JN.1.8-1JN.1.10]] gäng gäge Lüüt, wo sich für sündlos ghalte händ, [[1JN.3.4-1JN.3.10]] gäge Lüüt, wo d Sünd für bedüütigslos erklärt händ; me söll d Aussage nöd mitenand uusgliiche.",
   "Anderi läsed [[1JN.3.9]] als Aussag über das, was d Geburt us Gott irem Wäse nach bewürkt («cha nöd»), während [[1JN.1.8]] di no nöd vollendet Würklichkeit beschriibt; beides gelti glichziitig (i de Reformation zuegspitzt als «grächt und Sünder glichziitig»).",
   "Anderi verstönd «Sünd» im Kapitel 3 äng als «Gsetzlosigkeit» (ἀνομία, [[1JN.3.4]]) im Sinn vom Abfall i de Ändziit, öppe em Abstriite vo Christus; die Sünd tüeg nöd, wär us Gott gebore isch.",
   "No anderi nämed d Sätz als Ideal oder Aaspruch, wo sich d Gmeind dra söll mässe, ohni dass de Verfasser behauptet, es seg scho erreicht."],
  ["Sünd", "Gsetzlosigkeit", "Saame"]),
 ("INT-1JN-0003", U("1JN", 5, 13, 17), ["FIND-1JN-0010", "FIND-1JN-0013"],
  "Mit der «Sünde zum Tod» ([[1JN.5.16]]) ist am ehesten die bewusste Abkehr von Christus gemeint, wie sie der Brief bei den Weggegangenen sieht: Wer den Sohn nicht hat, hat das Leben nicht ([[1JN.5.12]]). Für sie verlangt der Verfasser keine Fürbitte, verbietet sie aber auch nicht.",
  "possible",
  "Der Brief bestimmt die «Sünde zum Tod» nicht; jede Antwort wird aus dem Zusammenhang erschlossen.",
  ["Andere verweisen auf die Unterscheidung im Alten Testament zwischen versehentlicher Sünde und Sünde «mit erhobener Hand», für die es kein Sühnopfer gab ([[NUM.15.27-NUM.15.31]]).",
   "Andere denken an Sünde, die als Gericht zum leiblichen Tod führt, wie bei Hananias und Saphira ([[ACT.5.1-ACT.5.11]]) oder bei Kranken und Verstorbenen in Korinth ([[1CO.11.30]]).",
   "In der späteren Bussordnung der Kirche wurde die Stelle mit der Unterscheidung von schweren und leichten Sünden («Todsünden» und «lässlichen Sünden») verbunden; dass der Brief eine solche Liste im Blick hat, lässt sich nicht zeigen.",
   "Manche halten fest, dass nach [[1JN.1.9]] jede bekannte Sünde vergeben wird; die «Sünde zum Tod» sei darum keine Tat, die nicht vergeben werden könnte, sondern eine Haltung, die Vergebung nicht sucht."],
  [("grc", "ἁμαρτία πρὸς θάνατον", "Sünde zum Tod"), ("grc", "αἰτέω", "bitten"), ("grc", "ἐρωτάω", "fragen, bitten")],
  "Mit de «Sünd zum Tod» ([[1JN.5.16]]) isch am eheschte s bewusste Abwände vo Christus gmeint, wie s de Brief bi dene gseht, wo wäggange sind: Wär de Sohn nöd hät, hät s Läbe nöd ([[1JN.5.12]]). Für si verlangt de Verfasser kei Fürbitt, verbüütet si aber au nöd.",
  "De Brief bestimmt d «Sünd zum Tod» nöd; jedi Antwort wird us em Zämehang erschlosse.",
  ["Anderi verwiised uf d Underscheidig im Alte Teschtamänt zwüsched versehentlicher Sünd und Sünd «mit erhobener Hand», für die s kei Süenopfer gää hät ([[NUM.15.27-NUM.15.31]]).",
   "Anderi dänked a Sünd, wo als Gricht zum liibliche Tod füert, wie bim Hananias und de Saphira ([[ACT.5.1-ACT.5.11]]) oder bi Chranke und Verstorbne z Korinth ([[1CO.11.30]]).",
   "I de spöötere Buessornig vo de Chile isch d Stell mit de Underscheidig vo schwääre und liechte Sünde («Todsünde» und «lässlichi Sünde») verbunde worde; dass de Brief e settigi Lischte im Blick hät, cha me nöd zeige.",
   "Mängi haltet fescht, dass nach [[1JN.1.9]] jedi bekännti Sünd vergää wird; d «Sünd zum Tod» seg drum kei Tat, wo nöd chönt vergää wärde, sondern e Haltig, wo kei Vergäbig suecht."],
  ["Sünd zum Tod", "bitte", "frage, bitte"]),
 ("INT-1JN-0004", U("1JN", 5, 6, 12), ["FIND-1JN-0011"],
  "Der Satz über die drei Zeugen «im Himmel» (Comma Johanneum) gehört nach der äusseren Bezeugung am wahrscheinlichsten nicht zum ursprünglichen Brief: Er fehlt in allen alten griechischen Handschriften und bei den griechischen Kirchenvätern, ist zuerst lateinisch belegt und kam erst im 16. Jahrhundert in den gedruckten griechischen Text (BG-1JN-0005). Er entstand wohl aus einer Auslegung, die Geist, Wasser und Blut auf Vater, Sohn und Geist bezog.",
  "probable",
  "Bewertet ist nach dem Alter, der Verbreitung und den Sprachen der Zeugen (äussere Bezeugung); innere Gründe sprechen in dieselbe Richtung, sind aber weniger eindeutig. Keine Lektoratsentscheidung über Wahrheit oder Wert der Aussage; die Trinitätslehre hängt nicht an dieser Stelle.",
  ["Verteidiger des Textus Receptus führen an, ohne den Zusatz stehe das männliche «drei, die bezeugen» (τρεῖς … οἱ μαρτυροῦντες) bei sächlichen Wörtern (Geist, Wasser, Blut); mit dem Zusatz, der «Vater» und «Wort» nennt, sei die Grammatik glatter. Dagegen wird eingewandt, dass die drei als Zeugen persönlich gedacht sind und «Geist» schon im Johannesevangelium persönlich behandelt wird.",
   "Man beruft sich auf Cyprian (3. Jh.), der von Vater, Sohn und Geist schreibt, «diese drei sind eins»; ob er dabei den Zusatz zitiert oder [[1JN.5.8]] dreifaltig auslegt, ist umstritten.",
   "Manche halten den Zusatz theologisch für sachgemäss und seine lange kirchliche Verwendung für ein Argument; das betrifft die Rezeption, nicht die Frage, was der Verfasser geschrieben hat."],
  [("lat", "Comma Johanneum", "«johanneischer Satzteil»: der Zusatz in [[1JN.5.7-1JN.5.8]]", "Comma Johanneum"), ("grc", "μαρτυρέω", "bezeugen")],
  "De Satz über di drüü Züüge «im Himmel» (Comma Johanneum) ghört nach de üssere Bezüügig am wahrschiinlichschte nöd zum ursprüngliche Brief: Er fäält i allne alte griechische Handschrifte und bi de griechische Chilevätter, isch zerscht latiinisch beleit und isch erscht im 16. Jaarhundert in druckte griechische Text cho (BG-1JN-0005). Er isch wahrschiinli us ere Uuslegig entstande, wo Geischt, Wasser und Bluet uf Vatter, Sohn und Geischt bezoge hät.",
  "Bewärtet isch nach em Alter, de Verbreitig und de Spraache vo de Züüge (üsseri Bezüügig); inneri Gründ spreched i di gliich Richtig, sind aber weniger eidüütig. Kei Lektoratsentscheid über Wahrheit oder Wärt vo de Aussag; d Trinitätslehr hangt nöd a dere Stell.",
  ["Verteidiger vom Textus Receptus füered aa, ohni de Zuesatz stöng s männlich «drüü, wo bezüüged» (τρεῖς … οἱ μαρτυροῦντες) bi sächliche Wörter (Geischt, Wasser, Bluet); mit em Zuesatz, wo «Vatter» und «Wort» nännt, seg d Grammatik glätter. Dergäge wird iigwändt, dass di drüü als Züüge persönlich dänkt sind und «Geischt» scho im Johannesevangelium persönlich behandlet wird.",
   "Me beruefft sich uf de Cyprian (3. Jh.), wo vo Vatter, Sohn und Geischt schriibt, «die drüü sind eis»; öb er debii de Zuesatz zitiert oder [[1JN.5.8]] drüüfaltig uusleit, isch umstritte.",
   "Mängi haltet de Zuesatz theologisch für sachgmäss und sini lang chilchlich Verwändig für es Argumänt; das betrifft d Rezeption, nöd d Frag, was de Verfasser gschribe hät."],
  ["«johanneische Satzteil»: de Zuesatz i [[1JN.5.7-1JN.5.8]]", "bezüüge"]),
 ("INT-1JN-0005", U("1JN", 1, 1, 4), ["FIND-1JN-0008"],
  "«Was von Anfang an war» ([[1JN.1.1]]) meint am ehesten Jesus selbst, wie ihn die Zeugen gehört, gesehen und betastet haben, also das in der Geschichte erschienene «Leben» ([[1JN.1.2]]). Der Brief greift die Sprache des Johannesprologs auf, legt den Ton aber auf die leibliche, überprüfbare Erfahrung; das passt zum Streit um das Kommen «im Fleisch» ([[1JN.4.2]]).",
  "possible",
  "Das sächliche «was» lässt offen, ob eine Person oder eine Botschaft gemeint ist; die Beziehung zum Johannesevangelium (abhängig, vorausgehend oder gemeinsame Tradition) ist umstritten (INT-1JN-0006).",
  ["Andere verstehen «von Anfang an» wie in [[1JN.2.7]] und [[1JN.2.24]] als Anfang der Verkündigung bzw. des Glaubens der Leser; gemeint sei die Botschaft, wie sie seit Beginn überliefert wird, nicht die Präexistenz.",
   "Andere lesen «Wort des Lebens» nicht als Christustitel wie in [[JHN.1.1]], sondern als «die lebenschaffende Botschaft»; das sächliche «was» stütze diese Lesart.",
   "Ob das «Wir» Augenzeugen meint oder die Gemeinschaft der Tradenten, die sich mit den ersten Zeugen eins weiss, ist umstritten; davon hängt auch ab, was der Abschnitt über den Verfasser aussagt."],
  [("grc", "ἀπ' ἀρχῆς", "von Anfang an"), ("grc", "λόγος τῆς ζωῆς", "Wort des Lebens"), ("grc", "ψηλαφάω", "betasten")],
  "«Was vo Aafang aa gsii isch» ([[1JN.1.1]]) meint am eheschte de Jesus sälber, wie n en d Züüge ghört, gseh und aaglanget händ, also s «Läbe», wo i de Gschicht erschine isch ([[1JN.1.2]]). De Brief nimmt d Spraach vom Johannesprolog uf, leit de Ton aber uf di liiblich, überprüefbar Erfaarig; das passt zum Striit um s Cho «im Fleisch» ([[1JN.4.2]]).",
  "S sächlich «was» laat offe, öb e Person oder e Botschaft gmeint isch; d Beziehig zum Johannesevangelium (abhängig, vorher oder gmeinsami Tradition) isch umstritte (INT-1JN-0006).",
  ["Anderi verstönd «vo Aafang aa» wie i [[1JN.2.7]] und [[1JN.2.24]] als Aafang vo de Verchündigung bzw. vom Glaube vo de Läser; gmeint seg d Botschaft, wie si sit em Aafang überliferet wird, nöd d Präexistänz.",
   "Anderi läsed «Wort vom Läbe» nöd als Christustitel wie i [[JHN.1.1]], sondern als «d Botschaft, wo Läbe schafft»; s sächlich «was» stützi die Läsart.",
   "Öb s «Mir» Augezüüge meint oder d Gmeinschaft vo dene, wo d Tradition wiitergänd und sich mit de erschte Züüge eis wüssed, isch umstritte; devo hangt au ab, was de Abschnitt über de Verfasser seit."],
  ["vo Aafang aa", "Wort vom Läbe", "aalange, betaschte"]),
 ("INT-1JN-0006", U("1JN", 1, 1, 4), ["FIND-1JN-0008", "FIND-1JN-0014", "FIND-2JN-0003"],
  "Der 1. Johannesbrief stammt am ehesten aus demselben Kreis wie das Johannesevangelium und setzt dessen Überlieferung voraus, vielleicht schon in schriftlicher Form; ob derselbe Verfasser schrieb, bleibt offen. Für die enge Verwandtschaft sprechen Wortschatz, Gegensatzpaare (Licht und Finsternis, Wahrheit und Lüge) und gemeinsame Sätze ([[1JN.4.12]]; [[JHN.1.18]]).",
  "possible",
  "Sprachvergleiche können Verwandtschaft zeigen, aber Verfasserschaft weder beweisen noch ausschliessen; der Brief nennt keinen Verfasser (BG-1JN-BOOK-0001).",
  ["Die altkirchliche Überlieferung schreibt Evangelium und Briefe demselben Johannes zu; Irenäus etwa zitiert den 1. und den 2. Brief als Worte des «Johannes, des Jüngers des Herrn» (Gegen die Häresien, Buch 3, Kapitel 16), den die Kirche mit dem Apostel gleichsetzte; viele Ausleger halten an einem gemeinsamen Verfasser fest und erklären die Unterschiede aus der anderen Gattung und Lage.",
   "C. H. Dodd (1937) betonte sprachliche und theologische Unterschiede: Der Brief hat Wörter, die im Evangelium fehlen (etwa «Sühne», «Antichrist», «Salbung»), erwartet die Wiederkunft Christi ausdrücklicher ([[1JN.2.28]]) und nennt Jesus, nicht den Geist, «Beistand» ([[1JN.2.1]]); er dachte an einen anderen Verfasser aus demselben Kreis.",
   "Manche halten den Brief für älter als die Endfassung des Evangeliums; andere sehen in ihm eine Auslegung des Evangeliums gegen Leser, die es einseitig verstanden (so Raymond E. Brown)."],
  [],
  "De 1. Johannesbrief stammt am eheschte us em gliiche Chreis wie s Johannesevangelium und setzt sini Überliferig voruus, vilicht scho schriftlich; öb de gliich Verfasser gschribe hät, bliibt offe. Für di äng Verwandtschaft spreched de Wortschatz, d Gägesatzpaar (Liecht und Fiischteri, Wahrheit und Lugi) und gmeinsami Sätz ([[1JN.4.12]]; [[JHN.1.18]]).",
  "Spraachvergliich chönd Verwandtschaft zeige, aber Verfasserschaft weder bewiise no uusschlüüsse; de Brief nännt kein Verfasser (BG-1JN-BOOK-0001).",
  ["D altchilchlich Überliferig schriibt Evangelium und Brief em gliiche Johannes zue; de Irenäus öppe zitiert de 1. und de 2. Brief als Wort vom «Johannes, em Jünger vom Herr» (Gäge d Häresie, Buech 3, Kapitel 16), wo d Chile em Apostel gliichgsetzt hät; vili Usleger haltet a me gmeinsame Verfasser fescht und erkläred d Underschiid us de andere Gattig und Lag.",
   "De C. H. Dodd (1937) hät spraachlichi und theologischi Underschiid betont: De Brief hät Wörter, wo im Evangelium fääled (öppe «Süeni», «Antichrischt», «Salbig»), erwartet s Wiederchoo vo Christus usdrücklicher ([[1JN.2.28]]) und nännt de Jesus, nöd de Geischt, «Biistand» ([[1JN.2.1]]); er hät a en andere Verfasser us em gliiche Chreis dänkt.",
   "Mängi haltet de Brief für älter als d Ändfassig vom Evangelium; anderi gsend i im e Uuslegig vom Evangelium gäge Läser, wo s einsiitig verstande händ (so de Raymond E. Brown)."],
  []),
 ("INT-1JN-0007", U("1JN", 2, 1, 2), ["FIND-1JN-0014"],
  "«Sühne» (ἱλασμός, [[1JN.2.2]]; [[1JN.4.10]]) meint am ehesten, dass Christus die Sünde wegschafft, die zwischen Gott und Menschen steht. Ausgangspunkt ist dabei Gottes Liebe: Nicht Menschen stimmen Gott um, sondern Gott selbst sendet den Sohn ([[1JN.4.10]]).",
  "possible",
  "Das Wort ist im Neuen Testament selten; seine Bedeutung wird aus der griechischen Bibel (etwa dem Versöhnungstag, [[LEV.16.1-LEV.16.34]]) und aus dem Zusammenhang erschlossen.",
  ["C. H. Dodd verstand ἱλασμός als «Sühnung» im Sinn der Beseitigung der Sünde (englisch expiation) und bestritt, dass Gottes Zorn besänftigt werden müsse.",
   "Leon Morris und andere hielten dagegen, das Wort schliesse im Griechischen das Abwenden von Zorn ein (englisch propitiation); auch wenn Gott selbst die Sühne schafft, gehe es um die Beziehung zu ihm, nicht nur um die Sünde als Sache.",
   "Manche betonen den Zusatz «für die ganze Welt» ([[1JN.2.2]]) als Hinweis auf die Reichweite der Sühne; wie weit er geht, war in der Theologiegeschichte umstritten."],
  [("grc", "ἱλασμός", "Sühne, Sühnemittel"), ("grc", "παράκλητος", "Beistand, Fürsprecher")],
  "«Süeni» (ἱλασμός, [[1JN.2.2]]; [[1JN.4.10]]) meint am eheschte, dass Christus d Sünd wägschafft, wo zwüsched Gott und Mänsche staat. Uusgangspunkt isch debii Gottes Liebi: Nöd Mänsche stimmed Gott um, sondern Gott sälber schickt de Sohn ([[1JN.4.10]]).",
  "S Wort isch im Nöie Teschtamänt sälte; sini Bedüütig wird us de griechische Bible (öppe em Versöönigstag, [[LEV.16.1-LEV.16.34]]) und us em Zämehang erschlosse.",
  ["De C. H. Dodd hät ἱλασμός als «Süenig» im Sinn vom Wägschaffe vo de Sünd verstande (änglisch expiation) und bestritte, dass me Gottes Zorn müessi bsänftige.",
   "De Leon Morris und anderi händ dergäge ghalte, s Wort schlüüssi im Griechische s Abwände vo Zorn ii (änglisch propitiation); au wänn Gott sälber d Süeni schafft, gang s um d Beziehig zu im, nöd nu um d Sünd als Sach.",
   "Mängi betoned de Zuesatz «für di ganz Wält» ([[1JN.2.2]]) als Hiiwiis, wie wiit d Süeni reicht; wie wiit genau, isch i de Theologiegschicht umstritte gsii."],
  ["Süeni, Süenmittel", "Biistand, Fürspräächer"]),
]

PRINCIPLES_1JN = [
 ("PRIN-1JN-0001", ["FIND-1JN-0001", "FIND-1JN-0007"],
  "Liebe zu Gott zeigt sich in der Liebe zu den Menschen, die man sieht, und zwar in Taten, nicht nur in Worten ([[1JN.3.17-1JN.3.18]]; [[1JN.4.20-1JN.4.21]]).", "probable",
  "Liebi zu Gott zeigt sich i de Liebi zu de Mänsche, wo me gseht, und zwar i Tate, nöd nu i Wort ([[1JN.3.17-1JN.3.18]]; [[1JN.4.20-1JN.4.21]])."),
 ("PRIN-1JN-0002", ["FIND-1JN-0009", "INT-1JN-0002"],
  "Ehrlichkeit über eigene Schuld und Vertrauen auf Vergebung gehören zusammen; wer Sünde leugnet, betrügt sich, wer sie bekennt, findet Gott treu ([[1JN.1.8-1JN.2.2]]).", "probable",
  "Eerlichkeit über di eiget Schuld und Vertroue uf Vergäbig ghöred zäme; wär d Sünd abstriitet, betrüügt sich, wär si bekännt, findet Gott tröi ([[1JN.1.8-1JN.2.2]])."),
 ("PRIN-1JN-0003", ["FIND-1JN-0003", "FIND-1JN-0002"],
  "Gewissheit des Glaubens gründet in dem, was Gott getan hat und gibt, nicht im eigenen Gefühl: «Gott ist grösser als unser Herz» ([[1JN.3.19-1JN.3.20]]; [[1JN.5.13]]).", "probable",
  "D Gwüssheit vom Glaube gründet i dem, was Gott tue hät und git, nöd im eigete Gfüel: «Gott isch grösser als öises Härz» ([[1JN.3.19-1JN.3.20]]; [[1JN.5.13]])."),
 ("PRIN-1JN-0004", ["FIND-1JN-0007", "INT-1JN-0001"],
  "Geistliche Ansprüche und Lehren sind zu prüfen, und zwar daran, ob sie Jesus als wirklichen Menschen bekennen und zu Liebe und Gehorsam führen ([[1JN.4.1-1JN.4.3]]).", "probable",
  "Geischtlichi Aasprüch und Lehre muess me prüefe, und zwar dra, öb si de Jesus als würkliche Mänsch bekänned und zu Liebi und Ghorsam füered ([[1JN.4.1-1JN.4.3]])."),
]
APPLICATIONS_1JN = [
 ("APP-1JN-0001", "PRIN-1JN-0001",
  "In Gemeinden und Familien kann das heissen, Hilfe konkret zu machen: Zeit, Geld oder Wohnraum mit jemandem zu teilen, der in Not ist, statt nur Anteilnahme zu bekunden ([[1JN.3.17]]).",
  "Der Brief spricht zuerst von der Liebe unter Glaubenden («die Brüder»); wie weit das auf alle Menschen auszudehnen ist, sagt er nicht ausdrücklich. Er verlangt nicht, sich selbst oder Abhängige in Not zu bringen.",
  "I Gmeinde und Familie cha das heisse, Hilf konkret z mache: Ziit, Gäld oder Wonruum mit öpperem z teile, wo in Not isch, statt nu Aateilnaam z zeige ([[1JN.3.17]]).",
  "De Brief redt zerscht vo de Liebi under Gläubige («d Brüeder»); wie wiit me das uf alli Mänsche cha uusdeene, seit er nöd usdrücklich. Er verlangt nöd, sich sälber oder Abhängigi in Not z bringe."),
 ("APP-1JN-0002", "PRIN-1JN-0002",
  "Gemeinden können Räume schaffen, in denen Versagen ausgesprochen werden darf, etwa in Gebet, Seelsorge oder Gottesdienst mit Schuldbekenntnis, ohne dass Blossstellung droht.",
  "Bekenntnis vor Gott ersetzt nicht die Verantwortung gegenüber Geschädigten; der Text eignet sich nicht dazu, Opfer zu schneller Vergebung zu drängen.",
  "Gmeinde chönd Rüüm schaffe, wo me Versaage dörf uusspräche, öppe im Gebätt, i de Seelsorg oder im Gottesdienscht mit Schuldbekänntnis, ohni dass me bloossgstellt wird.",
  "S Bekänntnis vor Gott ersetzt nöd d Verantwortig gägenüber dene, wo Schade gnoo händ; de Text taugt nöd dezue, Opfer zu schnäller Vergäbig z dränge."),
 ("APP-1JN-0003", "PRIN-1JN-0003",
  "Wer an sich zweifelt oder von Schuldgefühlen geplagt ist, darf sich daran halten, dass Gott grösser ist als das anklagende Herz; Seelsorge kann diese Verheissung stark machen, statt neue Leistungsnachweise zu verlangen.",
  "Der Brief ist kein Ersatz für Behandlung bei Angststörungen oder Depression. Er spricht Gewissheit denen zu, die an den Sohn glauben ([[1JN.5.13]]), und verbindet sie mit gelebter Liebe ([[1JN.3.18-1JN.3.19]]).",
  "Wär a sich zwiiflet oder vo Schuldgfüel plaaget isch, dörf sich dra halte, dass Gott grösser isch als s Härz, wo aaklagt; Seelsorg cha die Verheissig starch mache, statt nöii Leischtigsnachwiis z verlange.",
  "De Brief isch kein Ersatz für e Behandlig bi Angschtstörige oder Depression. Er spricht d Gwüssheit dene zue, wo a de Sohn glaubed ([[1JN.5.13]]), und verbindet si mit gläbter Liebi ([[1JN.3.18-1JN.3.19]])."),
 ("APP-1JN-0004", "PRIN-1JN-0004",
  "Bei neuen geistlichen Angeboten, Bewegungen oder charismatischen Lehrern kann man fragen: Wird Jesus als wirklicher Mensch und Gekreuzigter ernst genommen, und führt die Lehre zu Liebe und Verantwortung oder zu Überheblichkeit?",
  "Der Brief führt einen innerkirchlichen Konflikt mit scharfen Worten («Antichrist», «Lügner»); diese Sprache taugt nicht dazu, heutige Andersdenkende pauschal abzustempeln.",
  "Bi nöie geischtliche Aagebot, Bewegige oder charismatische Lehrer cha me frage: Wird de Jesus als würkliche Mänsch und als Gchrüüzigte ernscht gnoo, und füert d Lehr zu Liebi und Verantwortig oder zu Überheblichkeit?",
  "De Brief füert en Konflikt innerhalb vo de Chile mit schaarfe Wort («Antichrischt», «Lügner»); die Spraach taugt nöd dezue, hütigi Andersdänkendi pauschal abzstämple."),
]
QUESTIONS_1JN = [
 ("QUESTION-1JN-0001", U("1JN", 2, 20, 27),
  "Was ist die «Salbung» (χρῖσμα), die die Leser haben und die sie «über alles» lehrt, sodass sie niemanden brauchen, der sie lehrt ([[1JN.2.20]]; [[1JN.2.27]])?",
  "Gedeutet wird sie als Gabe des Heiligen Geistes, als das von Anfang an gehörte Wort, oder als beides; wie sich die Aussage zum Lehren des Briefes selbst verhält, bleibt zu klären.",
  "Was isch d «Salbig» (χρῖσμα), wo d Läser händ und wo si «über alles» lehrt, sodass si niemer bruuched, wo si lehrt ([[1JN.2.20]]; [[1JN.2.27]])?",
  "Si wird düütet als Gaab vom Heilige Geischt, als s Wort, wo me vo Aafang aa ghört hät, oder als beides; wie sich d Aussag zum Lehre vom Brief sälber verhaltet, isch no z kläre."),
 ("QUESTION-1JN-0002", U("1JN", 2, 12, 14),
  "Wen meinen die Anreden «Kinder», «Väter» und «junge Männer» in [[1JN.2.12-1JN.2.14]], und warum wechselt der Verfasser von «ich schreibe» zu «ich habe geschrieben»?",
  "Vorgeschlagen werden Altersgruppen, Stufen des Glaubens oder eine Anrede an alle («Kinder») mit zwei Untergruppen; der Zeitwechsel wird als Stilmittel, als Rückverweis auf einen früheren Brief oder auf das schon Geschriebene gedeutet.",
  "Wär meined d Aarede «Chind», «Vätter» und «jungi Manne» i [[1JN.2.12-1JN.2.14]], und werum wächslet de Verfasser vo «ich schriibe» zu «ich ha gschribe»?",
  "Vorgschlage wärded Altersgruppe, Stuefe vom Glaube oder e Aarede a alli («Chind») mit zwei Undergruppe; de Ziitwächsel wird als Stilmittel, als Rückverwiis uf en früenere Brief oder uf das, wo scho gschribe isch, düütet."),
 ("QUESTION-1JN-0003", U("1JN", 5, 6, 12),
  "Was bedeutet, Jesus Christus sei «durch Wasser und Blut» gekommen, und wie bezeugen Geist, Wasser und Blut gemeinsam ([[1JN.5.6-1JN.5.8]])?",
  "Gedacht wird an Taufe und Kreuzestod Jesu, an Wasser und Blut aus der Seite des Gekreuzigten ([[JHN.19.34]]) oder an Taufe und Abendmahl der Gemeinde; die Deutungen schliessen sich teilweise nicht aus.",
  "Was bedüütet s, dass de Jesus Christus «dur Wasser und Bluet» cho isch, und wie bezüüged Geischt, Wasser und Bluet zäme ([[1JN.5.6-1JN.5.8]])?",
  "Me dänkt a d Taufi und de Chrüüzestod vom Jesus, a Wasser und Bluet us de Siite vom Gchrüüzigte ([[JHN.19.34]]) oder a Taufi und Abigmaal vo de Gmeind; d Düütige schlüüssed sich zum Teil nöd uus."),
 ("QUESTION-1JN-0004", U("1JN", 5, 18, 21),
  "Warum endet der Brief unvermittelt mit «Kinder, hütet euch vor den Götzenbildern» ([[1JN.5.21]])?",
  "Gemeint sein können wörtlich die Kulte der Umgebung (BG-1JN-0004) oder bildlich falsche Gottesvorstellungen, etwa die Lehre der Weggegangenen, im Gegensatz zum «wahrhaftigen Gott» ([[1JN.5.20]]).",
  "Werum hört de Brief unvermittlet uf mit «Chind, hüeted eu vor de Götzebilder» ([[1JN.5.21]])?",
  "Gmeint chönd wörtlich d Kult vo de Umgäbig sii (BG-1JN-0004) oder bildlich falschi Vorstellige vo Gott, öppe d Lehr vo dene, wo wäggange sind, im Gägesatz zum «waarhaftige Gott» ([[1JN.5.20]])."),
]
RELATIONS_1JN = [
 ("REL-1JN-0001", U("1JN", 1, 1, 4), "JHN.1.1-JHN.1.14", "parallel_text", "high"),
 ("REL-1JN-0002", U("1JN", 4, 7, 12), "JHN.1.18", "parallel_saying", "high"),
 ("REL-1JN-0003", U("1JN", 4, 7, 12), "JHN.3.16", "thematic", "high"),
 ("REL-1JN-0004", U("1JN", 2, 7, 11), "JHN.13.34-JHN.13.35", "parallel_saying", "high"),
 ("REL-1JN-0005", U("1JN", 3, 11, 18), "JHN.15.12-JHN.15.13", "parallel_saying", "probable"),
 ("REL-1JN-0006", U("1JN", 3, 11, 15), "GEN.4.1-GEN.4.16", "background", "high"),
 ("REL-1JN-0007", U("1JN", 2, 1, 2), "JHN.14.16", "thematic", "probable"),
 ("REL-1JN-0008", U("1JN", 5, 6, 8), "JHN.19.34-JHN.19.35", "motif", "possible"),
 ("REL-1JN-0009", U("1JN", 5, 13, 17), "NUM.15.27-NUM.15.31", "thematic", "possible"),
 ("REL-1JN-0010", U("1JN", 2, 18, 23), "MRK.13.21-MRK.13.22", "thematic", "probable"),
 ("REL-1JN-0011", U("1JN", 1, 1, 4), "LUK.24.39", "motif", "possible"),
 ("REL-1JN-0012", U("1JN", 4, 1, 6), "2JN.1.7", "parallel_text", "high"),
 ("REL-1JN-0013", U("1JN", 5, 13, 17), "JHN.20.31", "parallel_form", "high"),
]

# Hintergrund: (id, Abschnitt, Stelle, Kontext, Konfidenz, Thema, Text, unsicher, Belege, Quellen, Fachwörter | Mundart)
BACKGROUND_1JN = [
 ("BG-1JN-0001", U("1JN", 5, 6, 12), "1JN.5.6", "CTX-JOHANNINE-READERS", "possible", "Kerinth bei Irenäus",
  "Irenäus von Lyon beschreibt um 180 n. Chr. einen Lehrer namens Kerinth (Gegen die Häresien, Buch 1, Kapitel 26, Abschnitt 1): Die Welt sei nicht vom höchsten Gott geschaffen, sondern von einer fernen Macht; Jesus sei wie alle Menschen ein Sohn Josefs und Marias gewesen; bei der Taufe sei der Christus in Gestalt einer Taube auf ihn herabgekommen und habe ihn vor dem Leiden wieder verlassen, sodass Jesus litt und auferstand, der Christus aber leidensunfähig blieb. Eine solche Trennung von Jesus und dem Christus würde zu [[1JN.2.22]] («wer leugnet, dass Jesus der Christus ist») und zu [[1JN.5.6]] passen («nicht im Wasser allein, sondern im Wasser und im Blut»). Irenäus erzählt auch, Johannes, der Jünger des Herrn, sei in Ephesus aus einem Badehaus geflohen, als er Kerinth darin sah, den «Feind der Wahrheit»; erzählt hätten es Leute, die es von Polykarp gehört hatten (Buch 3, Kapitel 3, Abschnitt 4). Nach Irenäus schrieb Johannes sein Evangelium auch gegen den Irrtum Kerinths (Buch 3, Kapitel 11, Abschnitt 1).",
  "Irenäus schreibt rund drei Generationen nach den Briefen und nennt die Johannesbriefe nicht als Schriften gegen Kerinth. Die Badehaus-Geschichte ist eine Anekdote aus zweiter Hand. Ob die Gegner des Briefes Kerinth oder ähnliche Lehrer waren, bleibt eine Vermutung (INT-1JN-0001).",
  ["1JN.2.22", "1JN.4.2-1JN.4.3", "1JN.5.6"],
  ["Irenäus, Gegen die Häresien 1,26,1 (Lehre Kerinths)", "Irenäus, Gegen die Häresien 3,3,4 (Johannes und Kerinth im Badehaus; Polykarp)",
   "Irenäus, Gegen die Häresien 3,11,1 (Johannesevangelium gegen Kerinth)", "Eusebius, Kirchengeschichte 3,28,6 und 4,14,6 (Wiedergabe der Badehaus-Geschichte)"],
  [],
  "De Kerinth bim Irenäus",
  "De Irenäus vo Lyon beschriibt um 180 n. Chr. en Lehrer, wo Kerinth gheisse hät (Gäge d Häresie, Buech 1, Kapitel 26, Abschnitt 1): D Wält seg nöd vom höchschte Gott gschaffe, sondern vo ere färne Macht; de Jesus seg wie alli Mänsche en Sohn vom Josef und vo de Maria gsii; bi de Taufi seg de Christus i de Gstalt vo ere Tuube uf en abecho und heb en vor em Liide wider verlaa, sodass de Jesus glitte hät und uferstande isch, de Christus aber nöd hät chöne liide. E settigi Trännig vo Jesus und Christus würd zu [[1JN.2.22]] («wär abstriitet, dass de Jesus de Christus isch») und zu [[1JN.5.6]] passe («nöd im Wasser allei, sondern im Wasser und im Bluet»). De Irenäus verzellt au, de Johannes, de Jünger vom Herr, seg z Ephesus us eme Badhuus gflüchtet, won er de Kerinth drin gseh hät, de «Fiind vo de Wahrheit»; verzellt hebed s Lüüt, wo s vom Polykarp ghört händ (Buech 3, Kapitel 3, Abschnitt 4). Nach em Irenäus hät de Johannes sis Evangelium au gäge de Irrtum vom Kerinth gschribe (Buech 3, Kapitel 11, Abschnitt 1).",
  "De Irenäus schriibt öppe drüü Generatione nach de Brief und nännt d Johannesbrief nöd als Schrifte gäge de Kerinth. D Badhuus-Gschicht isch en Anekdote us zweiter Hand. Öb d Gägner vom Brief de Kerinth oder ähnlichi Lehrer gsii sind, bliibt e Vermuetig (INT-1JN-0001).",
  []),
 ("BG-1JN-0002", U("1JN", 4, 1, 6), "1JN.4.2", "CTX-JOHANNINE-READERS", "probable", "Doketismus und Ignatius",
  "Ignatius von Antiochien schrieb um 110 n. Chr. auf dem Weg nach Rom Briefe an Gemeinden in der Provinz Asia. An die Gemeinde in Smyrna schreibt er, Christus habe «wahrhaft» gelitten und sei «wahrhaft» auferstanden, nicht, wie einige Ungläubige sagen, nur «zum Schein»; «sie selbst sind Schein» (An die Smyrnäer, Kapitel 2). Das griechische Wort für «scheinen» (δοκεῖν) gab später dem Doketismus den Namen. Ähnlich betont er im Brief an die Trallianer, Jesus sei wahrhaft geboren, habe wahrhaft gegessen und getrunken und sei wahrhaft gekreuzigt worden. Solche Lehren waren also in derselben Gegend und Zeit verbreitet, in der man die Johannesbriefe meist ansetzt.",
  "Ignatius zitiert die Johannesbriefe nicht ausdrücklich, und die Gegner des Ignatius sind nicht ohne Weiteres dieselben wie die des Briefes. Ob man um 100 schon von einer festen Lehre «Doketismus» sprechen kann, ist umstritten.",
  ["1JN.4.2-1JN.4.3", "2JN.1.7"],
  ["Ignatius, An die Smyrnäer 2", "Ignatius, An die Trallianer 9–10"],
  [("grc", "δοκέω", "scheinen, den Anschein haben")],
  "Doketismus und de Ignatius",
  "De Ignatius vo Antiochie hät um 110 n. Chr. uf em Wäg uf Rom Brief a Gmeinde i de Provinz Asia gschribe. A d Gmeind z Smyrna schriibt er, Christus heb «waarhaft» glitte und seg «waarhaft» uferstande, nöd, wie es paar Ungläubigi säged, nu «zum Schii»; «si sälber sind Schii» (A d Smyrnäer, Kapitel 2). S griechisch Wort für «schiine» (δοκεῖν) hät spööter em Doketismus de Name gää. Ähnlich betont er im Brief a d Trallianer, de Jesus seg waarhaft gebore, heb waarhaft gässe und trunke und seg waarhaft gchrüüziget worde. Settigi Lehre sind also i de gliiche Gägend und Ziit verbreitet gsii, wo me d Johannesbrief meischtens aasetzt.",
  "De Ignatius zitiert d Johannesbrief nöd usdrücklich, und d Gägner vom Ignatius sind nöd eifach di gliiche wie die vom Brief. Öb me um 100 scho vo ere feschte Lehr «Doketismus» cha rede, isch umstritte.",
  ["schiine, de Aaschii haa"]),
 ("BG-1JN-0003", U("1JN", 1, 1, 4), "1JN.1.1", "CTX-JOHANNINE-READERS", "possible", "Die Überlieferung von Johannes in Ephesus",
  "Nach Irenäus veröffentlichte Johannes, der Jünger des Herrn, sein Evangelium, als er in Ephesus in der Provinz Asia lebte (Gegen die Häresien, Buch 3, Kapitel 1, Abschnitt 1); die Gemeinde in Ephesus, von Paulus gegründet, habe Johannes bis in die Zeit Trajans (Kaiser 98–117) bei sich gehabt (Buch 3, Kapitel 3, Abschnitt 4). Irenäus beruft sich auf Polykarp von Smyrna, den er in seiner Jugend gehört habe. Ephesus war Hauptstadt der Provinz Asia, eine Hafenstadt mit dem berühmten Tempel der Artemis und einer frühen christlichen Gemeinde ([[ACT.19.1-ACT.19.41]]; [[REV.2.1-REV.2.7]]). Daher werden die Johannesbriefe meist in Gemeinden dieser Gegend verortet.",
  "Ob Irenäus mit «Johannes, der Jünger des Herrn» den Zebedäussohn meint oder einen anderen Johannes, ist umstritten; Papias kannte nach Eusebius auch einen «Presbyter Johannes» (BG-2JN-BOOK-0001). Der Brief selbst nennt weder Ort noch Empfänger.",
  ["1JN.1.1-1JN.1.4", "ACT.19.1-ACT.19.41", "REV.2.1-REV.2.7"],
  ["Irenäus, Gegen die Häresien 3,1,1 (Johannes in Ephesus)", "Irenäus, Gegen die Häresien 3,3,4 (Johannes bis in die Zeit Trajans)"],
  [],
  "D Überliferig vom Johannes z Ephesus",
  "Nach em Irenäus hät de Johannes, de Jünger vom Herr, sis Evangelium veröffentlicht, won er z Ephesus i de Provinz Asia gläbt hät (Gäge d Häresie, Buech 3, Kapitel 1, Abschnitt 1); d Gmeind z Ephesus, vom Paulus gründet, heb de Johannes bis i d Ziit vom Trajan (Kaiser 98–117) bi sich gha (Buech 3, Kapitel 3, Abschnitt 4). De Irenäus beruefft sich uf de Polykarp vo Smyrna, won er i sinere Jugend ghört heb. Ephesus isch d Hauptstadt vo de Provinz Asia gsii, e Hafestadt mit em berüemte Tämpel vo de Artemis und ere früene christliche Gmeind ([[ACT.19.1-ACT.19.41]]; [[REV.2.1-REV.2.7]]). Drum wärded d Johannesbrief meischtens i Gmeinde vo dere Gägend aagsidlet.",
  "Öb de Irenäus mit «Johannes, de Jünger vom Herr» de Sohn vom Zebedäus meint oder en andere Johannes, isch umstritte; de Papias hät nach em Eusebius au en «Presbyter Johannes» kännt (BG-2JN-BOOK-0001). De Brief sälber nännt weder Ort no Empfänger.",
  []),
 ("BG-1JN-0004", U("1JN", 5, 18, 21), "1JN.5.21", "CTX-JOHANNINE-READERS", "possible", "Götterbilder in den Städten Asiens",
  "In den Städten der Provinz Asia waren Götterbilder allgegenwärtig: in Tempeln, auf Plätzen, in Häusern und bei Festen, Vereinsmählern und Handwerkerzünften. In Ephesus stand der Tempel der Artemis, und die Apostelgeschichte erzählt vom Aufruhr der Silberschmiede, die kleine Tempel der Göttin herstellten ([[ACT.19.23-ACT.19.41]]). Dazu kam der Kult der Kaiser, für die mehrere Städte Asiens Tempel errichteten. Wer sich davon fernhielt, konnte gesellschaftlich und wirtschaftlich anecken; die Offenbarung nennt für Gemeinden Asiens Streit um Götzenopferfleisch ([[REV.2.14]]; [[REV.2.20]]).",
  "Ob [[1JN.5.21]] wörtlich an solche Kulte denkt oder bildlich an falsche Gottesbilder, ist umstritten (QUESTION-1JN-0004). Wie stark der Kaiserkult um 100 den Alltag einzelner Christen bestimmte, ist verschieden eingeschätzt.",
  ["1JN.5.20-1JN.5.21", "ACT.19.23-ACT.19.41", "REV.2.14", "REV.2.20"], [],
  [("grc", "εἴδωλον", "Götterbild, Götze")],
  "Götterbilder i de Stedt vo Asie",
  "I de Stedt vo de Provinz Asia sind Götterbilder überall gsii: i Tämpel, uf Plätz, i Hüüser und bi Fescht, Vereinsässe und Handwärkerzünft. Z Ephesus isch de Tämpel vo de Artemis gstande, und d Apostelgschicht verzellt vom Ufruer vo de Silberschmiid, wo chliini Tämpel vo de Göttin gmacht händ ([[ACT.19.23-ACT.19.41]]). Dezue isch de Kult vo de Kaiser cho, für die meereri Stedt vo Asie Tämpel baut händ. Wär sich devo färn ghalte hät, hät gsellschaftlich und wirtschaftlich chöne aaegge; d Offebarig nännt für Gmeinde vo Asie Striit um Götzeopferfleisch ([[REV.2.14]]; [[REV.2.20]]).",
  "Öb [[1JN.5.21]] wörtlich a settigi Kult dänkt oder bildlich a falschi Gottesbilder, isch umstritte (QUESTION-1JN-0004). Wie starch de Kaiserkult um 100 de Alltag vo einzelne Christe bestimmt hät, wird verschide iigschätzt.",
  ["Götterbild, Götz"]),
 ("BG-1JN-0005", U("1JN", 5, 6, 12), "1JN.5.7", "CTX-HIST-BIBLE-FORMATION", "probable", "Wie der Zusatz zu den drei Zeugen in die Bibeln kam",
  "Der Zusatz über die drei Zeugen im Himmel ist zuerst in lateinischen Quellen belegt; als ältester sicherer Beleg gilt der «Liber apologeticus», der Priszillian (gestorben 385) oder seinem Kreis zugeschrieben wird. In lateinischen Bibelhandschriften des Mittelalters wurde er verbreitet. In griechischen Handschriften fehlt er bis ins späte Mittelalter; die wenigen griechischen Zeugen sind spät, und mehrere haben ihn nur am Rand. Erasmus von Rotterdam liess ihn in seinen griechischen Ausgaben von 1516 und 1519 weg, weil er ihn in keiner griechischen Handschrift fand, und nahm ihn 1522 in die dritte Auflage auf, nachdem man ihm eine griechische Handschrift mit dem Zusatz vorgelegt hatte (heute Minuskel 61, Codex Montfortianus, um 1520, dort aus dem Lateinischen übersetzt). Über den Textus Receptus gelangte er in viele Bibeln der Reformationszeit und in die King-James-Bibel von 1611 (FIND-1JN-0011).",
  "Die Zahl der griechischen Handschriften mit dem Zusatz wird in der Literatur unterschiedlich angegeben, je nachdem, ob Randnotizen mitgezählt werden. Ob Erasmus ein Versprechen gab, den Zusatz bei einem griechischen Beleg aufzunehmen, wird ebenfalls verschieden dargestellt.",
  ["1JN.5.7-1JN.5.8"],
  ["Liber apologeticus (Priszillian zugeschrieben, 4. Jh.)", "Erasmus, Novum Instrumentum (1516); Novum Testamentum (1519, 1522)", "Minuskel 61 (Codex Montfortianus), Dublin, Trinity College"],
  [("lat", "Comma Johanneum", "«johanneischer Satzteil»", "Comma Johanneum")],
  "Wie de Zuesatz zu de drüü Züüge i d Bible cho isch",
  "De Zuesatz über di drüü Züüge im Himmel isch zerscht i latiinische Quelle beleit; als eltschte sichere Beleg gilt de «Liber apologeticus», wo em Priszillian (gstorbe 385) oder sim Chreis zuegschribe wird. I latiinische Bible-Handschrifte vom Mittelalter isch er verbreitet worde. I griechische Handschrifte fäält er bis is spaat Mittelalter; di wenige griechische Züüge sind spaat, und meereri händ en nu am Rand. De Erasmus vo Rotterdam hät en i sine griechische Usgaabe vo 1516 und 1519 wäggloo, wil er en i kei griechische Handschrift gfunde hät, und hät en 1522 i di dritt Uflaag ufgnoo, nachdem me n em e griechischi Handschrift mit em Zuesatz vorgleit hät (hüt Minuskel 61, Codex Montfortianus, um 1520, dört us em Latiinische übersetzt). Über de Textus Receptus isch er i vili Bible vo de Reformationsziit und i d King-James-Bible vo 1611 cho (FIND-1JN-0011).",
  "D Zaal vo de griechische Handschrifte mit em Zuesatz wird i de Literatur verschide aagää, je nachdem, öb me Randnotize mitzellt. Öb de Erasmus es Verspräche gää hät, de Zuesatz bi me griechische Beleg ufznää, wird au verschide dargstellt.",
  ["«johanneische Satzteil»"]),
]

SUMMARIES_1JN = [
 ("SUM-CH-1JN-001", "Der Verfasser verkündet, was von Anfang an war und was er und andere gehört, gesehen und betastet haben: das Wort des Lebens, damit die Leser Gemeinschaft mit ihnen und mit Vater und Sohn haben. Gott ist Licht; wer im Licht lebt, hat Gemeinschaft, und wer seine Sünden bekennt, dem vergibt Gott.",
  "De Verfasser verchündet, was vo Aafang aa gsii isch und was er und anderi ghört, gseh und aaglanget händ: s Wort vom Läbe, demit d Läser Gmeinschaft mit ine und mit Vatter und Sohn händ. Gott isch Liecht; wär im Liecht läbt, hät Gmeinschaft, und wär sini Sünde bekännt, dem vergit Gott."),
 ("SUM-CH-1JN-002", "Jesus Christus ist Beistand beim Vater und Sühne für die Sünden der ganzen Welt. Wer Gott kennt, hält seine Gebote und liebt den Bruder. Der Verfasser schreibt Kindern, Vätern und jungen Männern, warnt davor, die Welt zu lieben, und deutet den Weggang einer Gruppe als Zeichen der letzten Stunde: Antichrist ist, wer leugnet, dass Jesus der Christus ist. Die Leser sollen in dem bleiben, was sie von Anfang an gehört haben.",
  "De Jesus Christus isch Biistand bim Vatter und Süeni für d Sünde vo de ganze Wält. Wär Gott kännt, haltet sini Gebot und liebt de Brueder. De Verfasser schriibt Chind, Vätter und junge Manne, warnt devor, d Wält z liebe, und düütet s Wäggaa vo ere Gruppe als Zeiche vo de letschte Stund: Antichrischt isch, wär abstriitet, dass de Jesus de Christus isch. D Läser söled i dem bliibe, was si vo Aafang aa ghört händ."),
 ("SUM-CH-1JN-003", "Die Glaubenden heissen Kinder Gottes und werden ihm gleich sein, wenn er erscheint. Wer aus Gott geboren ist, sündigt nicht; an Gerechtigkeit und Bruderliebe zeigt sich, wer Kind Gottes ist. Liebe zeigt sich in Taten, nach dem Vorbild dessen, der sein Leben für uns hingab. Auch wenn das Herz verurteilt, ist Gott grösser.",
  "D Gläubige heissed Chind vo Gott und wärded em gliich sii, wänn er erschiint. Wär us Gott gebore isch, sündiget nöd; a de Grächtigkeit und a de Liebi zum Brueder zeigt sich, wär es Chind vo Gott isch. Liebi zeigt sich i Tate, nach em Vorbild vo dem, wo sis Läbe für üs gää hät. Au wänn s Härz verurteilt, isch Gott grösser."),
 ("SUM-CH-1JN-004", "Die Geister sind zu prüfen: Aus Gott ist der Geist, der bekennt, dass Jesus Christus im Fleisch gekommen ist. Gott ist Liebe; er hat zuerst geliebt und seinen Sohn als Sühne gesandt. Wer in der Liebe bleibt, bleibt in Gott; vollkommene Liebe treibt die Furcht aus. Wer Gott liebt, muss auch den Bruder lieben.",
  "D Geischter muess me prüefe: Us Gott isch de Geischt, wo bekännt, dass de Jesus Christus im Fleisch cho isch. Gott isch Liebi; er hät zerscht gliebt und sin Sohn als Süeni gschickt. Wär i de Liebi bliibt, bliibt i Gott; vollkommni Liebi tribt d Angscht uus. Wär Gott liebt, muess au de Brueder liebe."),
 ("SUM-CH-1JN-005", "Wer glaubt, dass Jesus der Christus ist, ist aus Gott geboren und besiegt die Welt. Geist, Wasser und Blut bezeugen den Sohn; wer den Sohn hat, hat das Leben. Der Brief ist geschrieben, damit die Leser wissen, dass sie ewiges Leben haben. Er spricht von Gebetserhörung und von Fürbitte bei «Sünde nicht zum Tod», schliesst mit dreifachem «wir wissen» und warnt vor Götzenbildern.",
  "Wär glaubt, dass de Jesus de Christus isch, isch us Gott gebore und bsiegt d Wält. Geischt, Wasser und Bluet bezüüged de Sohn; wär de Sohn hät, hät s Läbe. De Brief isch gschribe, demit d Läser wüssed, dass si ewigs Läbe händ. Er redt vo Gebätserhörig und vo Fürbitt bi «Sünd nöd zum Tod», hört mit eme drüüfache «mir wüssed» uf und warnt vor Götzebilder."),
]

# =================================================================================================================
# 2. Johannesbrief
FINDINGS_2JN = [
 ("FIND-2JN-0001", U("2JN", 1, 1, 4), "key_terms",
  "Der kurze Brief ist von «Wahrheit» (ἀλήθεια) geprägt: fünfmal in den ersten vier Versen ([[2JN.1.1-2JN.1.4]]). Daneben stehen «Gebot» (ἐντολή, viermal), «wandeln» (περιπατέω, dreimal), «bleiben» (μένω, dreimal) und «Lehre» (διδαχή, dreimal in [[2JN.1.9-2JN.1.10]]). Wahrheit und Liebe werden verbunden: Der Älteste liebt die Empfänger «in Wahrheit» ([[2JN.1.1]]), und Gnade, Erbarmen und Friede kommen «in Wahrheit und Liebe» ([[2JN.1.3]]).",
  ["2JN.1.1-2JN.1.6", "2JN.1.9-2JN.1.10"], "high", MAC,
  "De churz Brief isch vo «Wahrheit» (ἀλήθεια) prägt: föif Mal i de erschte vier Värs ([[2JN.1.1-2JN.1.4]]). Denäbe staat «Gebot» (ἐντολή, vier Mal), «laufe, wandle» (περιπατέω, drüü Mal), «bliibe» (μένω, drüü Mal) und «Lehr» (διδαχή, drüü Mal i [[2JN.1.9-2JN.1.10]]). Wahrheit und Liebi wärded verbunde: De Ältischt liebt d Empfänger «i de Wahrheit» ([[2JN.1.1]]), und Gnaad, Erbarme und Fride chömed «i Wahrheit und Liebi» ([[2JN.1.3]]).",
  MAC_G),
 ("FIND-2JN-0002", U("2JN", 1, 7, 11), "parallel_text",
  "[[2JN.1.7]] nimmt [[1JN.4.2-1JN.4.3]] auf: Viele Verführer sind «in die Welt ausgegangen», die nicht bekennen, dass Jesus Christus «im Fleisch kommt»; das ist «der Verführer und der Antichrist». Anders als in [[1JN.4.2]] (Perfekt ἐληλυθότα, «gekommen ist») steht hier ein Partizip Präsens (ἐρχόμενον, «kommend»). Neu gegenüber dem 1. Brief ist die Folgerung für die Gastfreundschaft: Wer diese Lehre nicht bringt, soll nicht ins Haus aufgenommen und nicht gegrüsst werden; wer ihn grüsst, hat teil an seinen bösen Werken ([[2JN.1.10-2JN.1.11]]).",
  ["1JN.4.2-1JN.4.3", "2JN.1.7-2JN.1.11"], "high", "Beobachtung am Wortlaut.",
  "[[2JN.1.7]] nimmt [[1JN.4.2-1JN.4.3]] uf: Vili Verfüerer sind «i d Wält uusgange», wo nöd bekänned, dass de Jesus Christus «im Fleisch chunnt»; das isch «de Verfüerer und de Antichrischt». Anders als i [[1JN.4.2]] (Perfekt ἐληλυθότα, «cho isch») staat da es Partizip Präsens (ἐρχόμενον, «chömmend»). Nöi gägenüber em 1. Brief isch d Folgerig für d Gaschtfründschaft: Wär die Lehr nöd bringt, söll me nöd is Huus ufnää und nöd grüesse; wär en grüesst, hät Teil a sine böse Wärch ([[2JN.1.10-2JN.1.11]]).",
  "Beobachtig am Wortluut."),
 ("FIND-2JN-0003", U("2JN", 1, 12, 13), "literary_structure",
  "Der 2. und der 3. Johannesbrief sind ähnlich gebaut: Beide beginnen mit «der Älteste» (ὁ πρεσβύτερος) und «den ich liebe in Wahrheit» ([[2JN.1.1]]; [[3JN.1.1]]), beide freuen sich «sehr» (ἐχάρην λίαν) über Leute, die «in der Wahrheit wandeln» ([[2JN.1.4]]; [[3JN.1.3-3JN.1.4]]), und beide schliessen fast gleich: Der Älteste hätte viel zu schreiben, will es aber nicht mit Tinte (und Papier bzw. Schreibrohr) tun, sondern hofft, «von Mund zu Mund» zu reden ([[2JN.1.12]]; [[3JN.1.13-3JN.1.14]]). Beide sind sehr kurz: nach dem SBLGNT 245 bzw. 219 Wörter in 13 bzw. 14 Versen (nach anderer Zählung 15).",
  ["2JN.1.1", "2JN.1.4", "2JN.1.12-2JN.1.13", "3JN.1.1-3JN.1.4", "3JN.1.13-3JN.1.14"], "high",
  "Beobachtung am Wortlaut; Wortzahlen nach den SBLGNT-Token im Projekt. Im griechischen Text ist der Schluss von 3 Joh ein eigener Vers 15; hier wird nach der Zählung der King-James-Bibel gezählt.",
  "De 2. und de 3. Johannesbrief sind ähnlich baut: Beidi fanged aa mit «de Ältischt» (ὁ πρεσβύτερος) und «wo n ich lieb i de Wahrheit» ([[2JN.1.1]]; [[3JN.1.1]]), beidi fröied sich «sehr» (ἐχάρην λίαν) über Lüüt, wo «i de Wahrheit laufed» ([[2JN.1.4]]; [[3JN.1.3-3JN.1.4]]), und beidi hööred fascht gliich uf: De Ältischt hett vil z schriibe, wott s aber nöd mit Tinte (und Papier bzw. Schriibrohr) mache, sondern hofft, «vo Mund zu Mund» z rede ([[2JN.1.12]]; [[3JN.1.13-3JN.1.14]]). Beidi sind sehr churz: nach em SBLGNT 245 bzw. 219 Wörter i 13 bzw. 14 Värs (nach anderer Zellig 15).",
  "Beobachtig am Wortluut; Wortzaale nach de SBLGNT-Token im Projekt. Im griechische Text isch de Schluss vom 3 Joh en eigete Värs 15; da wird nach de Zellig vo de King-James-Bible zellt."),
]
INTERPRETATIONS_2JN = [
 ("INT-2JN-0001", U("2JN", 1, 1, 4), ["FIND-2JN-0001", "FIND-2JN-0003"],
  "Die «auserwählte Herrin» und ihre «Kinder» ([[2JN.1.1]]) sind am ehesten eine Gemeinde und ihre Glieder; die «auserwählte Schwester», deren Kinder grüssen ([[2JN.1.13]]), ist die Gemeinde des Ältesten. Dafür spricht, dass der Brief zwischen «du» und «ihr» wechselt und von einem Gebot spricht, das «wir» von Anfang an haben ([[2JN.1.5]]).",
  "possible",
  "Die Bevorzugung ist eine redaktionelle Abwägung; der Brief erklärt die Anrede nicht. Bildliche Anreden einer Gemeinde als Frau kennt das Neue Testament auch sonst ([[1PE.5.13]]; [[EPH.5.25-EPH.5.32]]).",
  ["Andere lesen die Anrede wörtlich: Gemeint sei eine einzelne Frau, vielleicht Gastgeberin einer Hausgemeinde; dann wären die «Kinder» ihre Kinder oder Hausgenossen.",
   "Andere halten Κυρία («Herrin») oder Ἐκλεκτή («Auserwählte») für einen Eigennamen; dagegen wird eingewandt, dass dann die Schwester in [[2JN.1.13]] denselben Namen trüge.",
   "Manche denken an die ganze Kirche als «Herrin»; das passt schlecht zu einer «Schwester», die ebenfalls «auserwählt» ist."],
  [("grc", "ἐκλεκτὴ κυρία", "auserwählte Herrin")],
  "D «uuserwäält Herrin» und iri «Chind» ([[2JN.1.1]]) sind am eheschte e Gmeind und iri Glider; d «uuserwäält Schwöschter», wo iri Chind grüessed ([[2JN.1.13]]), isch d Gmeind vom Ältischte. Defür spricht, dass de Brief zwüsched «du» und «ir» wächslet und vo me Gebot redt, wo «mir» vo Aafang aa händ ([[2JN.1.5]]).",
  "D Bevorzugig isch e redaktionelli Abwägig; de Brief erklärt d Aarede nöd. Bildlichi Aarede vo ere Gmeind als Frau kännt s Nöi Teschtamänt au süscht ([[1PE.5.13]]; [[EPH.5.25-EPH.5.32]]).",
  ["Anderi läsed d Aarede wörtlich: Gmeint seg e einzelni Frau, vilicht e Gaschtgäberin vo ere Huusgmeind; dänn wäred d «Chind» iri Chind oder Huusgnosse.",
   "Anderi haltet Κυρία («Herrin») oder Ἐκλεκτή («Uuserwäälti») für en Eigename; dergäge wird iigwändt, dass dänn d Schwöschter i [[2JN.1.13]] de gliich Name trüeg.",
   "Mängi dänked a di ganz Chile als «Herrin»; das passt schlächt zu ere «Schwöschter», wo au «uuserwäält» isch."],
  ["uuserwäälti Herrin"]),
 ("INT-2JN-0002", U("2JN", 1, 7, 11), ["FIND-2JN-0002"],
  "Das Verbot, Irrlehrer «ins Haus» aufzunehmen und zu grüssen ([[2JN.1.10-2JN.1.11]]), betrifft am ehesten die Aufnahme reisender Lehrer in die Hausgemeinde, also Unterkunft, Unterstützung und eine Plattform zum Lehren. Wer sie so aufnimmt, macht sich zum Teilhaber ihrer Verkündigung. Ein Verbot jeder Freundlichkeit gegenüber Andersdenkenden ist damit nicht ausgesprochen.",
  "possible",
  "«Haus» kann die Privatwohnung wie die darin versammelte Gemeinde meinen; der Brief unterscheidet das nicht. Der Gruss (χαίρειν) war die übliche Begrüssung und Verabschiedung, auch in Briefen.",
  ["Andere lesen das Verbot umfassend als Abbruch jeder Gemeinschaft mit den Verführern, um die Gemeinde vor Ansteckung zu schützen; dann verlangt der Text tatsächlich eine harte Abgrenzung.",
   "Kritiker sehen einen Widerspruch zur Gastfreundschaft und Feindesliebe, die Jesus lehrt ([[MAT.5.44-MAT.5.47]]); andere halten dagegen, es gehe nicht um Feinde, sondern um Lehrer, die die Gemeinde beanspruchen.",
   "Manche weisen darauf hin, dass Diotrephes im 3. Brief ein ähnliches Mittel gegen die Boten des Ältesten anwendet ([[3JN.1.9-3JN.1.10]]); dieselbe Praxis konnte also gegen beide Seiten gewendet werden."],
  [("grc", "χαίρειν", "sei gegrüsst; Gruss beim Kommen und Gehen"), ("grc", "κοινωνέω", "teilhaben, Gemeinschaft haben")],
  "S Verbot, Irrlehrer «is Huus» ufznää und z grüesse ([[2JN.1.10-2JN.1.11]]), betrifft am eheschte s Ufnää vo reisende Lehrer i d Huusgmeind, also Underkunft, Unterstützig und e Plattform zum Lehre. Wär si eso ufnimmt, macht sich zum Teilhaber vo irer Verchündigung. Es Verbot vo jedere Fründlichkeit gägenüber Andersdänkende isch dermit nöd uusgsproche.",
  "«Huus» cha d Privatwonig wie au d Gmeind, wo sich drin versammlet, meine; de Brief underscheidet das nöd. De Gruess (χαίρειν) isch di üblich Begrüessig und Verabschiidig gsii, au i Brief.",
  ["Anderi läsed s Verbot umfassend als Abbruch vo jedere Gmeinschaft mit de Verfüerer, zum d Gmeind vor Aasteckig z schütze; dänn verlangt de Text würkli e harti Abgränzig.",
   "Kritiker gsend en Widerspruch zur Gaschtfründschaft und Fiindesliebi, wo de Jesus lehrt ([[MAT.5.44-MAT.5.47]]); anderi haltet dergäge, es gang nöd um Fiind, sondern um Lehrer, wo d Gmeind für sich beanspruched.",
   "Mängi wiised druf hii, dass de Diotrephes im 3. Brief es ähnlichs Mittel gäge d Bote vom Ältischte aawändet ([[3JN.1.9-3JN.1.10]]); di gliich Praxis hät also gäge beidi Siite chöne gwändet wärde."],
  ["bisch grüesst; Gruess bim Cho und Gaa", "teilhaa, Gmeinschaft haa"]),
 ("INT-2JN-0003", U("2JN", 1, 1, 4), ["FIND-2JN-0003"],
  "«Der Älteste» ([[2JN.1.1]]; [[3JN.1.1]]) ist am ehesten ein bekannter, älterer Leiter mit Ansehen über mehrere Gemeinden hinweg, der sich als Träger der Überlieferung «von Anfang an» versteht; der Titel genügt, ohne Namen, weil die Empfänger ihn kennen. Wer er war, lässt sich nicht sicher sagen.",
  "possible",
  "Die Bezeichnung kann Alter, Amt oder die Rolle als Traditionsträger meinen; der Brief erklärt sie nicht (siehe BG-2JN-BOOK-0001).",
  ["Die kirchliche Überlieferung sieht in ihm den Apostel Johannes; dafür spricht die Nähe zum 1. Brief und zum Evangelium, dagegen, dass sich ein Apostel kaum nur «der Älteste» nennen würde (vgl. aber [[1PE.5.1]], wo Petrus sich «Mitältester» nennt).",
   "Viele denken an den «Presbyter Johannes», den Papias nach Eusebius neben dem Apostel nennt; Eusebius erwähnt auch, dass man in Ephesus zwei Gräber zeigte, die beide Johannes zugeschrieben wurden (Kirchengeschichte, Buch 3, Kapitel 39, Abschnitte 4–6).",
   "Andere halten den Ältesten für einen sonst unbekannten Leiter; ob er auch den 1. Brief schrieb, ist dann offen."],
  [("grc", "πρεσβύτερος", "der Ältere, der Älteste; Ältester als Leitungsamt")],
  "«De Ältischt» ([[2JN.1.1]]; [[3JN.1.1]]) isch am eheschte en bekannte, älter Leiter mit Aasee über meereri Gmeinde ewäg, wo sich als Träger vo de Überliferig «vo Aafang aa» verstaat; de Titel länget, ohni Name, wil d Empfänger en känned. Wär er gsii isch, cha me nöd sicher säge.",
  "D Bezeichnig cha s Alter, es Amt oder d Rolle als Träger vo de Tradition meine; de Brief erklärt si nöd (lueg BG-2JN-BOOK-0001).",
  ["Di chilchlich Überliferig gseht i im de Apostel Johannes; defür spricht d Nööchi zum 1. Brief und zum Evangelium, dergäge, dass sich en Apostel chuum nu «de Ältischt» nänne würd (vgl. aber [[1PE.5.1]], wo sich de Petrus «Mitältischte» nännt).",
   "Vili dänked a de «Presbyter Johannes», wo de Papias nach em Eusebius näbe em Apostel nännt; de Eusebius erwäänt au, dass me z Ephesus zwei Gräber zeigt hät, wo beidi em Johannes zuegschribe worde sind (Chilegschicht, Buech 3, Kapitel 39, Abschnitt 4–6).",
   "Anderi haltet de Ältischt für en süscht unbekannte Leiter; öb er au de 1. Brief gschribe hät, isch dänn offe."],
  ["de Älter, de Ältischt; Ältischte als Leitigsamt"]),
]
PRINCIPLES_2JN = [
 ("PRIN-2JN-0001", ["FIND-2JN-0001", "INT-2JN-0002"],
  "Liebe und Wahrheit gehören zusammen: Gemeinden sollen gastfreundlich sein, aber nicht jede Lehre mit ihren Mitteln fördern ([[2JN.1.4-2JN.1.11]]).", "possible",
  "Liebi und Wahrheit ghöred zäme: Gmeinde söled gaschtfründlich sii, aber nöd jedi Lehr mit irne Mittel fördere ([[2JN.1.4-2JN.1.11]])."),
]
APPLICATIONS_2JN = [
 ("APP-2JN-0001", "PRIN-2JN-0001",
  "Gemeinden können offen für Gäste und Fragende sein und zugleich sorgfältig entscheiden, wen sie predigen oder unterrichten lassen und welche Projekte sie finanziell tragen.",
  "Die Stelle rechtfertigt keine Unfreundlichkeit oder Ausgrenzung von Menschen, die zweifeln oder anders glauben; sie betrifft reisende Lehrer, die Unterstützung für ihre Verkündigung suchten.",
  "Gmeinde chönd offe sii für Gäscht und Lüüt, wo Frage händ, und glichziitig sorgfältig entscheide, wär bi ine predige oder unterrichte dörf und weli Projekt si finanziell träged.",
  "D Stell rächtfertiget kei Unfründlichkeit oder Uusgränzig vo Mänsche, wo zwiifled oder anders glaubed; si betrifft reisendi Lehrer, wo Unterstützig für iri Verchündigung gsuecht händ."),
]
QUESTIONS_2JN = [
 ("QUESTION-2JN-0001", U("2JN", 1, 7, 11),
  "Warum steht in [[2JN.1.7]] «der im Fleisch kommt» (Präsens) statt «gekommen ist» wie in [[1JN.4.2]]?",
  "Gedeutet wird als zeitloses Bekenntnis zur Menschwerdung, als Bezug auf die erwartete Wiederkunft im Fleisch oder als blosse Stilvariante; der Text entscheidet es nicht.",
  "Werum staat i [[2JN.1.7]] «wo im Fleisch chunnt» (Präsens) statt «cho isch» wie i [[1JN.4.2]]?",
  "Düütet wird s als ziitloses Bekänntnis zur Mänschwerdig, als Bezug uf s erwartet Wiederchoo im Fleisch oder als bloossi Stilvariante; de Text entscheidet s nöd."),
 ("QUESTION-2JN-0002", U("2JN", 1, 7, 11),
  "Was meint «wer weitergeht (προάγων) und nicht in der Lehre des Christus bleibt» ([[2JN.1.9]])? Ist es die Lehre über Christus oder die Lehre, die Christus gab?",
  "Der Genitiv lässt beides zu. «Weitergehen» wird oft als Anspruch der Gegner gedeutet, über die Überlieferung hinaus fortgeschritten zu sein; belegt ist das nur aus dem Brief selbst.",
  "Was meint «wär wiitergaat (προάγων) und nöd i de Lehr vo Christus bliibt» ([[2JN.1.9]])? Isch s d Lehr über Christus oder d Lehr, wo Christus gää hät?",
  "De Genitiv laat beides zue. «Wiitergaa» wird oft als Aaspruch vo de Gägner düütet, über d Überliferig uus wiiter z sii; beleit isch das nu us em Brief sälber."),
]
RELATIONS_2JN = [
 ("REL-2JN-0001", U("2JN", 1, 4, 6), "1JN.2.7-1JN.2.8", "parallel_saying", "high"),
 ("REL-2JN-0002", U("2JN", 1, 4, 6), "JHN.13.34", "parallel_saying", "probable"),
 ("REL-2JN-0003", U("2JN", 1, 7, 11), "1JN.2.18-1JN.2.23", "parallel_text", "high"),
 ("REL-2JN-0004", U("2JN", 1, 7, 11), "MAT.10.11-MAT.10.14", "thematic", "possible"),
 ("REL-2JN-0005", U("2JN", 1, 12, 13), "3JN.1.13-3JN.1.14", "parallel_form", "high"),
 ("REL-2JN-0006", U("2JN", 1, 1, 4), "1PE.5.13", "motif", "possible"),
]
BACKGROUND_2JN = [
 ("BG-2JN-0001", U("2JN", 1, 7, 11), "2JN.1.10", "CTX-JOHANNINE-READERS", "probable", "Hausgemeinden und reisende Lehrer",
  "Die frühen Gemeinden versammelten sich in Privathäusern ([[ROM.16.5]]; [[1CO.16.19]]; [[PHM.1.2]]). Wer Glaubende beherbergte, stellte oft auch den Raum für Versammlung und Lehre. Zwischen den Gemeinden reisten Apostel, Propheten, Lehrer und Boten; sie lebten von der Gastfreundschaft der Gemeinden. Das brachte Missbrauch mit sich: Die Didache, eine Gemeindeordnung wohl vom Ende des 1. oder Anfang des 2. Jahrhunderts, verlangt, einen reisenden Apostel wie den Herrn aufzunehmen, aber nur einen oder zwei Tage; wer drei Tage bleibt oder Geld verlangt, sei ein falscher Prophet (Didache, Kapitel 11). Durchreisende Glaubende sollen unterstützt werden, wer aber bleiben will, soll arbeiten (Kapitel 12). Vor diesem Hintergrund war die Aufnahme eines Lehrers eine Entscheidung der Hausgemeinde, nicht nur eine private Freundlichkeit.",
  "Ob die Didache und die Johannesbriefe dieselbe Praxis voraussetzen, ist nicht belegt; Datierung und Herkunft der Didache sind umstritten.",
  ["2JN.1.10-2JN.1.11", "3JN.1.5-3JN.1.10", "ROM.16.5", "1CO.16.19", "PHM.1.2"],
  ["Didache 11,4–6 (reisende Apostel); 12,1–5 (durchreisende Glaubende)"],
  [("grc", "οἰκία", "Haus, Haushalt")],
  "Huusgmeinde und reisendi Lehrer",
  "Di früene Gmeinde händ sich i Privathüüser versammlet ([[ROM.16.5]]; [[1CO.16.19]]; [[PHM.1.2]]). Wär Gläubigi bherbergt hät, hät oft au de Ruum für d Versammlig und d Lehr gstellt. Zwüsched de Gmeinde sind Apostel, Prophete, Lehrer und Bote greist; si händ vo de Gaschtfründschaft vo de Gmeinde gläbt. Das hät Missbruuch mit sich brocht: D Didache, e Gmeindsornig wahrschiinli vom Änd vom 1. oder Aafang vom 2. Jaarhundert, verlangt, en reisende Apostel wie de Herr ufznää, aber nu ein oder zwei Täg; wär drüü Täg bliibt oder Gäld verlangt, seg en falsche Prophet (Didache, Kapitel 11). Gläubigi, wo dureräised, söll me unterstütze, wär aber wott bliibe, söll schaffe (Kapitel 12). Vor dem Hintergrund isch s Ufnää vo me Lehrer en Entscheid vo de Huusgmeind gsii, nöd nu e privati Fründlichkeit.",
  "Öb d Didache und d Johannesbrief di gliich Praxis voruussetzed, isch nöd beleit; Datierig und Härkunft vo de Didache sind umstritte.",
  ["Huus, Hushalt"]),
 ("BG-2JN-0002", U("2JN", 1, 12, 13), "2JN.1.12", "CTX-JOHANNINE-READERS", "probable", "Papier, Tinte und Schreibrohr",
  "Der Älteste spricht von «Papier und Tinte» ([[2JN.1.12]]) und von «Tinte und Schreibrohr» ([[3JN.1.13]]). χάρτης bezeichnet ein Blatt Papyrus: Aus dem Mark der Papyruspflanze wurden Streifen kreuzweise aufeinandergelegt, gepresst und geglättet. Tinte (μέλαν, «das Schwarze») bestand meist aus Russ und einem Bindemittel wie Gummi; geschrieben wurde mit einem zugespitzten Schilfrohr (κάλαμος). Private Briefe auf Papyrus sind aus Ägypten zu Tausenden erhalten; viele sind etwa so lang wie der 2. und 3. Johannesbrief. Weil es keine allgemeine Post gab, gab man Briefe Reisenden mit; oft sollte der Überbringer zusätzlich mündlich berichten. Die Bevorzugung des Gesprächs «von Mund zu Mund» ist ein verbreiteter Briefschluss.",
  "Dass beide Briefe auf je ein Papyrusblatt passten, wird aus ihrer Länge erschlossen (vgl. BG-2JN-BOOK-0001); die Originale sind nicht erhalten.",
  ["2JN.1.12", "3JN.1.13-3JN.1.14"], [],
  [("grc", "χάρτης", "Papyrusblatt"), ("grc", "μέλαν", "Tinte (wörtlich «das Schwarze»)"), ("grc", "κάλαμος", "Schilfrohr, Schreibrohr")],
  "Papier, Tinte und Schriibrohr",
  "De Ältischt redt vo «Papier und Tinte» ([[2JN.1.12]]) und vo «Tinte und Schriibrohr» ([[3JN.1.13]]). χάρτης meint es Blatt Papyrus: Us em Mark vo de Papyrusplanze hät me Streife chrüüzwiis ufenand gleit, presst und glättet. D Tinte (μέλαν, «s Schwarz») isch meischtens us Russ und eme Bindmittel wie Gummi gsii; gschribe hät me mit eme zuegspitzte Schilfrohr (κάλαμος). Privati Brief uf Papyrus sind us Ägypte z Tuusige erhalte; vili sind öppe so lang wie de 2. und de 3. Johannesbrief. Wil s kei allgemeini Poscht gää hät, hät me Brief Reisende mitgää; oft hät de Überbringer zuesätzlich müesse verzelle. Dass me lieber «vo Mund zu Mund» redt, isch en verbreitete Briefschluss.",
  "Dass beidi Brief uf je eis Papyrusblatt passt händ, wird us irer Längi erschlosse (vgl. BG-2JN-BOOK-0001); d Original sind nöd erhalte.",
  ["Papyrusblatt", "Tinte (wörtlich «s Schwarz»)", "Schilfrohr, Schriibrohr"]),
]
SUMMARIES_2JN = [
 ("SUM-CH-2JN-001", "Der Älteste schreibt der «auserwählten Herrin» und ihren Kindern, die er in Wahrheit liebt. Er freut sich, dass einige in der Wahrheit wandeln, und erinnert an das Gebot von Anfang an, einander zu lieben. Er warnt vor Verführern, die nicht bekennen, dass Jesus Christus im Fleisch kommt, und weist an, solche Lehrer nicht aufzunehmen. Mehr will er bei einem Besuch mündlich sagen.",
  "De Ältischt schriibt de «uuserwäälte Herrin» und irne Chind, won er i de Wahrheit liebt. Er fröit sich, dass es paar i de Wahrheit laufed, und erinneret as Gebot vo Aafang aa, enand z liebe. Er warnt vor Verfüerer, wo nöd bekänned, dass de Jesus Christus im Fleisch chunnt, und seit, me söll settigi Lehrer nöd ufnää. Meh wott er bi me Bsuech mündlich säge."),
]

# =================================================================================================================
# 3. Johannesbrief
FINDINGS_3JN = [
 ("FIND-3JN-0001", U("3JN", 1, 9, 10), "names",
  "Der Brief nennt drei Männer: Gaius, den Empfänger, den der Älteste lobt, weil er reisende Brüder, und zwar Fremde, treu aufnimmt ([[3JN.1.1-3JN.1.8]]); Diotrephes, der «gern der Erste» unter ihnen sein will (φιλοπρωτεύων), den Ältesten nicht aufnimmt, ihn mit bösen Worten verleumdet, selbst die Brüder nicht aufnimmt und die, die es wollen, hindert und aus der Gemeinde wirft ([[3JN.1.9-3JN.1.10]]); und Demetrius, dem alle und «die Wahrheit selbst» ein gutes Zeugnis geben ([[3JN.1.12]]). Das Verb «aufnehmen» (ἐπιδέχομαι) steht zweimal, beide Male für Diotrephes.",
  ["3JN.1.1-3JN.1.12"], "high", MAC + " Dass φιλοπρωτεύω im Neuen Testament nur hier steht, folgt den gängigen Konkordanzen.",
  "De Brief nännt drüü Manne: de Gaius, de Empfänger, wo de Ältischt lobt, wil er reisendi Brüeder, und zwar Frömdi, tröi ufnimmt ([[3JN.1.1-3JN.1.8]]); de Diotrephes, wo «gärn de Erscht» under ine wott sii (φιλοπρωτεύων), de Ältischt nöd ufnimmt, en mit böse Wort verleumdet, sälber d Brüeder nöd ufnimmt und die, wo s wänd, hinderet und us de Gmeind rüert ([[3JN.1.9-3JN.1.10]]); und de Demetrius, wo alli und «d Wahrheit sälber» es guets Zügnis gänd ([[3JN.1.12]]). S Verb «ufnää» (ἐπιδέχομαι) staat zwei Mal, beidi Mal für de Diotrephes.",
  MAC_G + " Dass φιλοπρωτεύω im Nöie Teschtamänt nu da staat, folgt de gängige Konkordanze."),
 ("FIND-3JN-0002", U("3JN", 1, 5, 8), "key_terms",
  "Das Wort «Gemeinde» (ἐκκλησία) steht dreimal im 3. Johannesbrief ([[3JN.1.6]]; [[3JN.1.9]]; [[3JN.1.10]]) und weder im 1. noch im 2. Brief. «Wahrheit» (ἀλήθεια) steht sechsmal, darunter in der Wendung, wer solche Brüder aufnimmt, werde zum «Mitarbeiter für die Wahrheit» (συνεργοὶ τῇ ἀληθείᾳ, [[3JN.1.8]]). Die Reisenden sind «um des Namens willen ausgezogen» und nehmen nichts von den Heiden an ([[3JN.1.7]]); Gaius soll sie, «wie es Gottes würdig ist», für die Weiterreise ausrüsten (προπέμπω, [[3JN.1.6]]).",
  ["3JN.1.5-3JN.1.10", "3JN.1.12"], "high", MAC + " Dass ἐκκλησία auch im Johannesevangelium fehlt, folgt den gängigen Konkordanzen.",
  "S Wort «Gmeind» (ἐκκλησία) staat drüü Mal im 3. Johannesbrief ([[3JN.1.6]]; [[3JN.1.9]]; [[3JN.1.10]]) und weder im 1. no im 2. Brief. «Wahrheit» (ἀλήθεια) staat sächs Mal, au i de Wändig, wär settigi Brüeder ufnämi, werdi zum «Mitarbeiter für d Wahrheit» (συνεργοὶ τῇ ἀληθείᾳ, [[3JN.1.8]]). D Reisende sind «wäge em Name uuszoge» und nämed nüt vo de Heide aa ([[3JN.1.7]]); de Gaius söll si «so, wie s Gott würdig isch, wiiterschicke» (προπέμπω, [[3JN.1.6]]).",
  MAC_G + " Dass ἐκκλησία au im Johannesevangelium fäält, folgt de gängige Konkordanze."),
 ("FIND-3JN-0003", U("3JN", 1, 11, 12), "parallel_text",
  "[[3JN.1.11]] klingt an den 1. Brief an: «Wer Gutes tut, ist aus Gott; wer Böses tut, hat Gott nicht gesehen» – vgl. «jeder, der sündigt, hat ihn nicht gesehen» ([[1JN.3.6]]) und «wer Gerechtigkeit tut, ist aus ihm geboren» ([[1JN.2.29]]; [[1JN.3.10]]). Auch das Zeugnis, dessen Wahrheit die Leser kennen ([[3JN.1.12]]), erinnert an das Johannesevangelium ([[JHN.19.35]]; [[JHN.21.24]]).",
  ["3JN.1.11-3JN.1.12", "1JN.2.29", "1JN.3.6", "1JN.3.10", "JHN.19.35", "JHN.21.24"], "high", "Beobachtung am Wortlaut." + JHN_NOTE,
  "[[3JN.1.11]] tönt wie de 1. Brief: «Wär Guets tuet, isch us Gott; wär Böses tuet, hät Gott nöd gseh» – vgl. «jede, wo sündiget, hät en nöd gseh» ([[1JN.3.6]]) und «wär Grächtigkeit tuet, isch us im gebore» ([[1JN.2.29]]; [[1JN.3.10]]). Au s Zügnis, vo dem d Läser wüssed, dass es waar isch ([[3JN.1.12]]), erinneret as Johannesevangelium ([[JHN.19.35]]; [[JHN.21.24]]).",
  "Beobachtig am Wortluut." + JHN_NOTE_G),
]
INTERPRETATIONS_3JN = [
 ("INT-3JN-0001", U("3JN", 1, 9, 10), ["FIND-3JN-0001"],
  "Der Konflikt mit Diotrephes ist am ehesten ein Streit um Einfluss und Zuständigkeit: Ein örtlicher Leiter will über den Zugang zu seiner Gemeinde selbst bestimmen und weist die Boten eines auswärtigen, angesehenen Ältesten ab. Der Brief wirft ihm Ehrgeiz und üble Nachrede vor, nicht falsche Lehre.",
  "possible",
  "Wir hören nur die Seite des Ältesten; Diotrephes' Gründe sind nicht überliefert. Ob er ein Amt hatte, sagt der Text nicht.",
  ["Schon Adolf von Harnack sah in Diotrephes einen frühen Vertreter eines örtlichen Leitungsamts (Monepiskopat), das sich gegen die alte, überregionale Autorität reisender Apostel und Ältester durchsetzte.",
   "Ernst Käsemann (1951) kehrte die Rollen um: Diotrephes sei ein rechtgläubiger Bischof gewesen, der den Ältesten als verdächtigen Lehrer ausgeschlossen habe; die These hat wenig Zustimmung gefunden, zeigt aber, wie einseitig die Quellenlage ist.",
   "Andere vermuten, Diotrephes habe zu den Lehrern gehört, vor denen der 1. und 2. Brief warnen, oder habe zumindest ihre Sache gestützt; der 3. Brief deutet das nicht an.",
   "Wieder andere sehen eine persönliche Rivalität ohne grundsätzlichen Hintergrund; das Wort «gern der Erste sein» würde dazu passen."],
  [("grc", "φιλοπρωτεύω", "gern der Erste sein, den Vorrang beanspruchen"), ("grc", "ἐπιδέχομαι", "aufnehmen, anerkennen")],
  "De Konflikt mit em Diotrephes isch am eheschte en Striit um Iifluss und Zueständigkeit: En Leiter vor Ort wott sälber bestimme, wär i sini Gmeind dörf, und wiist d Bote vo me uswärtige, aagsehne Ältischte ab. De Brief wirft em Ehrgiiz und üble Nachred vor, nöd falschi Lehr.",
  "Mir ghööred nu d Siite vom Ältischte; d Gründ vom Diotrephes sind nöd überliferet. Öb er es Amt gha hät, seit de Text nöd.",
  ["Scho de Adolf von Harnack hät im Diotrephes en früene Vertreter vo me Leitigsamt vor Ort (Monepiskopat) gseh, wo sich gäge di alt, überregional Autorität vo reisende Apostel und Ältischte durgsetzt hät.",
   "De Ernst Käsemann (1951) hät d Rolle umdräit: De Diotrephes seg en rächtgläubige Bischof gsii, wo de Ältischt als verdächtige Lehrer uusgschlosse heb; d These hät wenig Zuestimmig gfunde, zeigt aber, wie einsiitig d Quellelaag isch.",
   "Anderi vermueted, de Diotrephes heb zu de Lehrer ghört, vor dene de 1. und de 2. Brief warned, oder heb wenigschtens iri Sach gstützt; de 3. Brief deutet das nöd aa.",
   "No anderi gsend e persönlichi Rivalität ohni grundsätzliche Hintergrund; s Wort «gärn de Erscht sii» würd dezue passe."],
  ["gärn de Erscht sii, de Vorrang beanspruche", "ufnää, aaerchänne"]),
 ("INT-3JN-0002", U("3JN", 1, 9, 10), ["FIND-3JN-0001", "FIND-2JN-0002"],
  "Der Brief, den der Älteste «an die Gemeinde» geschrieben hat und den Diotrephes offenbar nicht gelten liess ([[3JN.1.9]]), ist wahrscheinlich verloren.",
  "possible",
  "Der Text nennt nur «ich habe etwas der Gemeinde geschrieben»; Inhalt und Verbleib sind unbekannt.",
  ["Manche identifizieren ihn mit dem 2. Johannesbrief: Beide Briefe sind gleich gebaut und könnten zusammen überbracht worden sein. Dagegen spricht, dass der 2. Brief vor Irrlehrern warnt, während es in [[3JN.1.9-3JN.1.10]] um die Aufnahme der eigenen Boten geht.",
   "Andere denken an den 1. Johannesbrief; der hat aber keine Briefform mit Empfängern und Grüssen."],
  [],
  "De Brief, wo de Ältischt «a d Gmeind» gschribe hät und wo de Diotrephes offebar nöd hät gälte loo ([[3JN.1.9]]), isch wahrschiinli verlore.",
  "De Text seit nu «ich ha de Gmeind öppis gschribe»; Inhalt und Verbliib sind unbekannt.",
  ["Mängi setzed en em 2. Johannesbrief gliich: Beidi Brief sind gliich baut und chönted zäme überbracht worde sii. Dergäge spricht, dass de 2. Brief vor Irrlehrer warnt, während s i [[3JN.1.9-3JN.1.10]] ums Ufnää vo de eigete Bote gaat.",
   "Anderi dänked a de 1. Johannesbrief; dä hät aber kei Briefform mit Empfänger und Grüess."],
  []),
]
PRINCIPLES_3JN = [
 ("PRIN-3JN-0001", ["FIND-3JN-0002", "BG-3JN-0001"],
  "Wer andere im Dienst am Evangelium unterstützt, wird zum «Mitarbeiter für die Wahrheit» ([[3JN.1.5-3JN.1.8]]).", "probable",
  "Wär anderi im Dienscht am Evangelium unterstützt, wird zum «Mitarbeiter für d Wahrheit» ([[3JN.1.5-3JN.1.8]])."),
 ("PRIN-3JN-0002", ["FIND-3JN-0001", "INT-3JN-0001"],
  "Leitung in der Gemeinde dient der Gemeinschaft; wer «der Erste sein» will und andere ausschliesst, verfehlt sie ([[3JN.1.9-3JN.1.11]]).", "possible",
  "Leitig i de Gmeind dient de Gmeinschaft; wär «de Erscht sii» wott und anderi uusschlüüsst, verfäält si ([[3JN.1.9-3JN.1.11]])."),
]
APPLICATIONS_3JN = [
 ("APP-3JN-0001", "PRIN-3JN-0001",
  "Wer Missionarinnen, Hilfswerk-Mitarbeitende oder Gäste aus anderen Gemeinden beherbergt oder ihre Weiterreise unterstützt, nimmt an ihrer Arbeit teil; das kann auch mit kleinen Mitteln geschehen.",
  "Der Text setzt reisende Boten voraus, die auf private Gastgeber angewiesen waren; heutige Werke haben andere Strukturen und Kontrollen, die nicht ersetzt werden sollen.",
  "Wär Missionarinne, Mitarbeitendi vo Hilfswärch oder Gäscht us andere Gmeinde bherbergt oder iri Wiiterreis unterstützt, nimmt a irer Arbet teil; das cha au mit chliine Mittel gscheh.",
  "De Text setzt reisendi Bote voruus, wo uf privati Gaschtgäber aagwise gsii sind; hütigi Wärch händ anderi Strukture und Kontrolle, wo me nöd söll ersetze."),
 ("APP-3JN-0002", "PRIN-3JN-0002",
  "Leitungsgremien können sich fragen, ob sie Zugang und Mitsprache aus Sorge um die Gemeinde regeln oder um eigenen Einfluss zu sichern, und Konflikte offen statt durch Ausschluss und Gerede austragen.",
  "Der Brief gibt nur die Sicht des Ältesten wieder; er eignet sich nicht dazu, heutige Leitungspersonen vorschnell mit Diotrephes gleichzusetzen.",
  "Leitigsgremie chönd sich frage, öb si Zuegang und Mitsprach us Sorg um d Gmeind reglet oder zum eigete Iifluss sichere, und Konflikt offe statt dur Uusschluss und Gred uustrage.",
  "De Brief git nu d Sicht vom Ältischte wider; er taugt nöd dezue, hütigi Leitigspersone vorschnäll em Diotrephes gliichzsetze."),
]
QUESTIONS_3JN = [
 ("QUESTION-3JN-0001", U("3JN", 1, 1, 4),
  "Wer war Gaius ([[3JN.1.1]]), und gehörte er zur Gemeinde des Diotrephes?",
  "Gaius war ein häufiger Name; Verbindungen zu anderen Männern dieses Namens im Neuen Testament ([[ACT.19.29]]; [[ROM.16.23]]; [[1CO.1.14]]) lassen sich nicht belegen. Ob er in derselben oder einer benachbarten Gemeinde lebte, ist offen.",
  "Wär isch de Gaius gsii ([[3JN.1.1]]), und hät er zur Gmeind vom Diotrephes ghört?",
  "Gaius isch en hüüfige Name gsii; Verbindige zu andere Manne mit dem Name im Nöie Teschtamänt ([[ACT.19.29]]; [[ROM.16.23]]; [[1CO.1.14]]) cha me nöd belege. Öb er i de gliiche oder i ere benachbarte Gmeind gläbt hät, isch offe."),
 ("QUESTION-3JN-0002", U("3JN", 1, 11, 12),
  "Ist Demetrius ([[3JN.1.12]]) der Überbringer des Briefes, den der Älteste empfiehlt?",
  "Die Empfehlung passt zu einem Boten, den Gaius aufnehmen soll; ausdrücklich sagt der Brief das nicht.",
  "Isch de Demetrius ([[3JN.1.12]]) de Überbringer vom Brief, wo de Ältischt empfiehlt?",
  "D Empfälig passt zu me Bot, wo de Gaius söll ufnää; usdrücklich seit de Brief das nöd."),
]
RELATIONS_3JN = [
 ("REL-3JN-0001", U("3JN", 1, 5, 8), "ROM.12.13", "thematic", "probable"),
 ("REL-3JN-0002", U("3JN", 1, 5, 8), "HEB.13.2", "thematic", "probable"),
 ("REL-3JN-0003", U("3JN", 1, 5, 8), "TIT.3.13", "thematic", "probable"),
 ("REL-3JN-0004", U("3JN", 1, 5, 8), "MAT.10.40-MAT.10.42", "thematic", "possible"),
 ("REL-3JN-0005", U("3JN", 1, 9, 10), "MRK.10.42-MRK.10.45", "thematic", "possible"),
 ("REL-3JN-0006", U("3JN", 1, 11, 12), "1JN.3.6", "parallel_saying", "high"),
 ("REL-3JN-0007", U("3JN", 1, 9, 10), "2JN.1.10-2JN.1.11", "thematic", "probable"),
]
BACKGROUND_3JN = [
 ("BG-3JN-0001", U("3JN", 1, 5, 8), "3JN.1.6", "CTX-JOHANNINE-READERS", "probable", "Gastfreundschaft und Ausrüstung für die Weiterreise",
  "Gasthäuser an den Strassen hatten einen schlechten Ruf; wer konnte, übernachtete bei Verwandten, Geschäftsfreunden oder Glaubensgenossen. Jüdische und christliche Gemeinden pflegten die Gastfreundschaft als Pflicht ([[ROM.12.13]]; [[HEB.13.2]]; [[1PE.4.9]]). προπέμπω («weiterschicken, geleiten») meint mehr als verabschieden: Man gab Reisenden Proviant, Geld oder Begleitung für die nächste Etappe mit ([[ROM.15.24]]; [[1CO.16.6]]; [[TIT.3.13]]). Dass die Boten «nichts von den Heiden» annehmen ([[3JN.1.7]]), unterscheidet sie von umherziehenden Philosophen und Kultpropheten, die von ihren Zuhörern lebten; sie waren darum auf die Gemeinden angewiesen.",
  "Ob ἐθνικοί hier Nichtchristen allgemein meint oder Menschen, denen die Boten das Evangelium brachten, ist offen. Wie verbreitet bezahlte Wanderlehrer waren, wird verschieden eingeschätzt.",
  ["3JN.1.5-3JN.1.8", "ROM.12.13", "ROM.15.24", "1CO.16.6", "TIT.3.13", "HEB.13.2", "1PE.4.9"], [],
  [("grc", "προπέμπω", "weiterschicken, geleiten, für die Weiterreise ausstatten"), ("grc", "ξένος", "Fremder, Gast"), ("grc", "ἐθνικός", "heidnisch; Nichtjude bzw. Nichtchrist")],
  "Gaschtfründschaft und «Wiiterschicke»",
  "Gaschthüüser a de Strasse händ en schlächte Ruef gha; wär hät chöne, hät bi Verwandte, Gschäftsfründ oder Glaubensgnosse übernachtet. Jüdischi und christlichi Gmeinde händ d Gaschtfründschaft als Pflicht pflegt ([[ROM.12.13]]; [[HEB.13.2]]; [[1PE.4.9]]). «Wiiterschicke» (προπέμπω) meint meh als verabschiede: Me hät Reisende Proviant, Gäld oder Begleitig für di nächscht Etappe mitgää ([[ROM.15.24]]; [[1CO.16.6]]; [[TIT.3.13]]). Dass d Bote «nüt vo de Heide» aanämed ([[3JN.1.7]]), underscheidet si vo umeziehende Philosophe und Kultprophete, wo vo irne Zuehörer gläbt händ; si sind drum uf d Gmeinde aagwise gsii.",
  "Öb ἐθνικοί da Nichtchriste allgemein meint oder Mänsche, wo d Bote s Evangelium brocht händ, isch offe. Wie verbreitet zaalti Wanderlehrer gsii sind, wird verschide iigschätzt.",
  ["wiiterschicke, für d Wiiterreis uusrüschte", "Frömde, Gascht", "heidnisch; Nichtjud bzw. Nichtchrischt"]),
 ("BG-3JN-0002", U("3JN", 1, 1, 4), "3JN.1.2", "CTX-JOHANNINE-READERS", "probable", "Briefformeln in Gruss und Schluss",
  "Der 3. Johannesbrief folgt eng dem Muster privater griechischer Briefe: Absender und Empfänger, dann ein Wunsch für das Wohlergehen und die Gesundheit des Empfängers («dass es dir in allem gut gehe und du gesund seist», [[3JN.1.2]]), Freude über erhaltene Nachrichten, Hauptteil, Ankündigung eines Besuchs und Grüsse. Solche Gesundheitswünsche sind in Papyrusbriefen sehr häufig. Ungewöhnlich für ein christliches Schreiben ist der Gruss «die Freunde» (οἱ φίλοι) statt «die Brüder» ([[3JN.1.14]]); er erinnert an [[JHN.15.13-JHN.15.15]], wo Jesus die Jünger «Freunde» nennt.",
  "Ob «die Freunde» bewusst an das Johannesevangelium anknüpft oder einfach die übliche Briefsprache aufnimmt, ist offen.",
  ["3JN.1.1-3JN.1.4", "3JN.1.13-3JN.1.14", "JHN.15.13-JHN.15.15"], [],
  [("grc", "ὑγιαίνω", "gesund sein"), ("grc", "φίλος", "Freund")],
  "Briefformle im Gruess und am Schluss",
  "De 3. Johannesbrief folgt äng em Muschter vo private griechische Brief: Absänder und Empfänger, dänn en Wunsch für s Wohlergaa und d Gsundheit vom Empfänger («dass es dir i allem guet gaat und du gsund bisch», [[3JN.1.2]]), Fröid über Nachrichte, wo me übercho hät, Hauptteil, Aakündigung vo me Bsuech und Grüess. Settigi Gsundheitswünsch sind i Papyrusbrief sehr hüüfig. Ungwöönlich für es christlichs Schriibe isch de Gruess «d Fründ» (οἱ φίλοι) statt «d Brüeder» ([[3JN.1.14]]); er erinneret a [[JHN.15.13-JHN.15.15]], wo de Jesus d Jünger «Fründ» nännt.",
  "Öb «d Fründ» bewusst as Johannesevangelium aaknüpft oder eifach di üblich Briefspraach ufnimmt, isch offe.",
  ["gsund sii", "Fründ"]),
]
SUMMARIES_3JN = [
 ("SUM-CH-3JN-001", "Der Älteste lobt Gaius, weil er in der Wahrheit wandelt und reisende Brüder treu aufnimmt und für die Weiterreise ausrüstet; so werden er und andere zu Mitarbeitern für die Wahrheit. Diotrephes dagegen will der Erste sein, weist den Ältesten und die Brüder ab und schliesst Gastgeber aus der Gemeinde aus. Für Demetrius legt der Älteste ein gutes Zeugnis ab und hofft, Gaius bald zu sehen.",
  "De Ältischt lobt de Gaius, wil er i de Wahrheit lauft und reisendi Brüeder tröi ufnimmt und wiiterschickt; so wärded er und anderi zu Mitarbeiter für d Wahrheit. De Diotrephes dergäge wott de Erscht sii, wiist de Ältischt und d Brüeder ab und schlüüsst Gaschtgäber us de Gmeind uus. Für de Demetrius git de Ältischt es guets Zügnis ab und hofft, de Gaius bald z gseh."),
]

OQ_COMMON = ["Mundart muttersprachlich prüfen", "Fachliche Prüfung der Deutungen und des Hintergrunds"]


def run():
    from _study import write_study
    missing = sorted(set(CHAPTERS.values()) - set(_UNITS))
    if missing:
        raise SystemExit(f"Texteinheiten fehlen noch (zuerst johannesbriefe_text.py ausführen): {missing}")
    check_counts()

    def extra(book):
        return sorted((p.stem for p in (D / "translations").rglob(f"TRANS-{book}-*-WORKING.json")), key=lambda x: ("-GSW-" in x, x))

    cfg = {"TAGS": TAGS, "CONTEXT": CONTEXT}
    write_study({**cfg, "FINDINGS": FINDINGS_1JN, "INTERPRETATIONS": INTERPRETATIONS_1JN, "PRINCIPLES": PRINCIPLES_1JN,
                 "APPLICATIONS": APPLICATIONS_1JN, "QUESTIONS": QUESTIONS_1JN, "RELATIONS": RELATIONS_1JN,
                 "BACKGROUND": BACKGROUND_1JN, "SUMMARIES": SUMMARIES_1JN,
                 "STUDY": ("STUDY-1JN-0001", "1. Johannesbrief: ganzes Buch", CHAPTERS[("1JN", 1)], extra("1JN"),
                           OQ_COMMON + ["Patristische Angaben (BG-1JN-0001 bis -0003, BG-1JN-0005) an Ausgaben prüfen",
                                        "Handschriftenbefunde (FIND-1JN-0011, FIND-1JN-0012) am Faksimile prüfen"])},
                "1. Johannesbrief")
    write_study({**cfg, "FINDINGS": FINDINGS_2JN, "INTERPRETATIONS": INTERPRETATIONS_2JN, "PRINCIPLES": PRINCIPLES_2JN,
                 "APPLICATIONS": APPLICATIONS_2JN, "QUESTIONS": QUESTIONS_2JN, "RELATIONS": RELATIONS_2JN,
                 "BACKGROUND": BACKGROUND_2JN, "SUMMARIES": SUMMARIES_2JN,
                 "STUDY": ("STUDY-2JN-0001", "2. Johannesbrief: ganzes Buch", CHAPTERS[("2JN", 1)], extra("2JN"),
                           OQ_COMMON + ["Angaben zur Didache (BG-2JN-0001) an einer Ausgabe prüfen"])},
                "2. Johannesbrief")
    write_study({**cfg, "FINDINGS": FINDINGS_3JN, "INTERPRETATIONS": INTERPRETATIONS_3JN, "PRINCIPLES": PRINCIPLES_3JN,
                 "APPLICATIONS": APPLICATIONS_3JN, "QUESTIONS": QUESTIONS_3JN, "RELATIONS": RELATIONS_3JN,
                 "BACKGROUND": BACKGROUND_3JN, "SUMMARIES": SUMMARIES_3JN,
                 "STUDY": ("STUDY-3JN-0001", "3. Johannesbrief: ganzes Buch", CHAPTERS[("3JN", 1)], extra("3JN"), OQ_COMMON)},
                "3. Johannesbrief")


if __name__ == "__main__":
    run()
