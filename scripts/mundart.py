#!/usr/bin/env python3
"""Prüft Züritüütsch-Texte gegen die Regeln in docs/ZUERITUEUETSCH.md.

Maschinell prüfbar sind Sonderzeichen der Dieth-Schreibung (è, ò, ù, ì; Umschriften wie ā oder ô bleiben erlaubt), die Wortliste (abgelöste Form -> gültige Form) und einige Muster (hochdeutsches
Präteritum, «um z», Apostroph, Genitiv). Wortwahl und Satzbau prüft eine getrennte Instanz gegen das Dokument.

  python3 scripts/mundart.py            Übersicht je Buch und Regel
  python3 scripts/mundart.py JHN        Einzelfunde eines Buchs (Bibeltext und Lokalisierungen)
  python3 scripts/mundart.py --text "…" einen Text prüfen

Als Modul: pruefe(text) -> Liste (gefunden, Regel, Vorschlag).
"""
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Abgelöste Form -> gültige Form, je mit Regel (Abschnitt in docs/ZUERITUEUETSCH.md). Kleinschreibung; Gross am
# Satzanfang wird mitgeprüft.
WORTLISTE = {
    # 1.3 Dehnungs-h wie im Hochdeutschen
    "fäält": ("fehlt", "1.3"), "fääle": ("fehle", "1.3"), "jaar": ("jahr", "1.3"), "jaare": ("jahre", "1.3"),
    "oore": ("ohre", "1.3"), "oor": ("ohr", "1.3"), "loon": ("lohn", "1.3"), "söön": ("söhn", "1.3"),
    "soon": ("sohn", "1.3"), "ooni": ("ohni", "1.3"), "gsee": ("gseh", "1.3"), "gschee": ("gscheh", "1.3"),
    "leert": ("lehrt", "1.3"), "gleert": ("glehrt", "1.3"), "leerer": ("lehrer", "1.3"),
    "gläämt": ("glähmt", "1.3"), "gläämte": ("glähmte", "1.3"), "faare": ("fahre", "1.3"), "faart": ("fahrt", "1.3"),
    "gfaare": ("gfahre", "1.3"), "waar": ("wahr", "1.3"), "waarhäit": ("wahrheit", "1.3"), "zie": ("zieh", "1.3"),
    "ziend": ("ziehnd", "1.3"),
    # 1.4 ei statt äi
    "zwäi": ("zwei", "1.4"), "gäischt": ("geischt", "1.4"),
    "häilig": ("heilig", "1.4"), "häilige": ("heilige", "1.4"), "käi": ("kei", "1.4"), "äis": ("eis", "1.4"),
    # 1.5 ie nur Zwielaut
    "wieder": ("wider", "1.5"), "viel": ("vil", "1.5"), "vieli": ("vili", "1.5"), "spiele": ("spile", "1.5"),
    # 1.10 Partizip ohne gg-/gch-
    "ggää": ("gää", "1.10"), "ggange": ("gange", "1.10"), "ggässe": ("gässe", "1.10"), "gchauft": ("kauft", "1.10"),
    "praacht": ("bracht", "1.10"), "ggäh": ("gää", "1.10"),
    # Entscheid Mänsch
    "mäntsch": ("mänsch", "Entscheid"), "mäntsche": ("mänsche", "Entscheid"),
    # 2 Formen
    "üs": ("öis", "2"), "üse": ("öise", "2"), "üsi": ("öisi", "2"), "üses": ("öises", "2"), "üsere": ("öisere", "2"),
    "üsem": ("öisem", "2"), "sie": ("si", "2"), "ihr": ("ir / ire", "2"), "nüt": ("nüüt", "2"), "öpis": ("öppis", "2"),
    "gsi": ("gsii", "2"),
    "eu": ("öi", "2"), "euch": ("öi", "2"), "eue": ("öie", "2"), "eui": ("öii", "2"), "wer": ("wär", "2"),
    "demit": ("damit", "2"), "tämpel": ("tempel", "3"), "ärde": ("erde", "1.6"), "drüü": ("drü", "2"),
    "brocht": ("bracht", "1.10"), "gha": ("ghaa", "2"), "brüedere": ("brüeder", "3"),
    # 3 Wortwahl: falsche Vermundartlichung
    "gfüel": ("gfühl", "3"), "stuefe": ("stufe", "3"),
    # Präteritum (2 Verb)
    "war": ("isch … gsii", "2 Präteritum"), "waren": ("sind … gsii", "2 Präteritum"),
    "hatte": ("hät … ghaa", "2 Präteritum"), "hatten": ("händ … ghaa", "2 Präteritum"),
    "kam": ("isch … choo", "2 Präteritum"), "kamen": ("sind … choo", "2 Präteritum"),
    "sagte": ("hät … gseit", "2 Präteritum"), "sagten": ("händ … gseit", "2 Präteritum"),
    "ging": ("isch … gange", "2 Präteritum"), "gingen": ("sind … gange", "2 Präteritum"),
    "sprach": ("hät … gseit", "2 Präteritum"), "wurde": ("isch … worde", "2 Präteritum"),
    "wurden": ("sind … worde", "2 Präteritum"),
}


# Ergänzungen aus der Neuübersetzung 2026-11-21 (Abschnitt 2 «Weitere Festlegungen» und Regeln 1.3, 1.6, 1.8, 1.13)
_ERGAENZT = {
    "1.3": "broot taag aabig raat schlaaf schlaafe lüüg ee vee befeel befole loo oor zää zäät gwont seer "
           "nää schöön böös hööch nööch nooch ääre zäänte bewaare zale",
    "1.6": "härz härze ärnt ärnte gärn stärbe ewägg weg",
    "1.8": "könig könige knecht knächt",
    "2": "zwee zwo füüf ali mane irne öisne welle sölle werum sig sigi seg seigid heig heg häig heiged heigid "
         "wärdi wärdid wüssid übercho niemert chünige jumpfere gsehne frögt",
    "3": "himel schriftgleerte schriftgleert schriftgelehrte hüchler find spraach spraache schleeg uussag lieferet "
         "fischternis fischteri tämpelwiiig brüedere stedt diräkt tumm",
}
_ERGAENZT["Runde 3"] = ("läär lääre lääri lääres spaat spoot spööter schöön schööni schööner schöönscht chräit "
                       "gchräit dräit umdräit gsät chilche volch hääggli hääkli wortlut kein dem bliibid glaubid "
                       "dörfid seigid")
_ZIEL_R3 = {"läär": "leer", "lääre": "leere", "lääri": "leeri", "lääres": "leeres", "spaat": "spät", "spoot": "spät",
            "spööter": "spöter", "schöön": "schön", "schööni": "schöni", "schööner": "schöner",
            "schöönscht": "schönscht", "chräit": "chräht", "gchräit": "gchräht", "dräit": "dräht", "umdräit": "umdräht",
            "gsät": "gsäit", "chilche": "chile", "volch": "volk", "hääggli": "häggli", "hääkli": "häggli",
            "wortlut": "wortluut", "kein": "kei", "dem": "däm", "bliibid": "bliibed", "glaubid": "glaubed",
            "dörfid": "dörfed", "seigid": "seiged"}
_ERGAENZT["Runde 4"] = ("zügnis zügnisse ellei det gförchtet förchte förcht förchted verriisse umchert umchere umchered "
                       "umgchert chräie erniedriget erniedrige aagchündt stärn stärne eues voruusgseit voruussag "
                       "voruussetze voruusgsetzt chilelich chilchlich straaf düütsch düütschi düütsche züridüütsch")
_ZIEL_R4 = {"zügnis": "züügnis", "zügnisse": "züügnisse", "ellei": "elei", "det": "dört", "gförchtet": "gfürchtet",
            "förchte": "fürchte", "förcht": "fürcht", "förchted": "fürchted", "verriisse": "verrisse",
            "umchert": "umchehrt", "umchere": "umchehre", "umchered": "umchehred", "umgchert": "umgchehrt",
            "chräie": "chrähe", "erniedriget": "ernidriget", "erniedrige": "ernidrige", "aagchündt": "aagchündet",
            "stärn": "stern", "stärne": "sterne", "eues": "öies", "voruusgseit": "vorusgseit",
            "voruussag": "vorussag", "voruussetze": "vorussetze", "voruusgsetzt": "vorusgsetzt",
            "chilelich": "chirchlich", "chilchlich": "chirchlich", "straaf": "straf",
            "düütsch": "tüütsch", "düütschi": "tüütschi", "düütsche": "tüütsche", "züridüütsch": "züritüütsch"}
_ZIEL = {
    "broot": "brot", "taag": "tag", "aabig": "abig", "raat": "rat", "schlaaf": "schlaf",
    "schlaafe": "schlafe", "lüüg": "lüg", "ee": "ehe", "vee": "veh", "befeel": "befehl", "befole": "befohle",
    "loo": "lohn", "oor": "ohr", "zää": "zäh", "zäät": "zäht", "gwont": "gwohnt", "seer": "sehr", "nää": "näh",
    "schöön": "schön", "böös": "bös", "hööch": "höch", "nööch": "nöch", "nooch": "nöch", "ääre": "ähre",
    "zäänte": "zehnte", "bewaare": "bewahre", "zale": "zahle", "härz": "herz", "härze": "herze", "ärnt": "ernte",
    "ärnte": "ernte", "gärn": "gern", "stärbe": "sterbe", "ewägg": "wäg", "weg": "wäg", "könig": "chönig",
    "könige": "chönige", "knecht": "chnächt", "knächt": "chnächt", "zwee": "zwei", "zwo": "zwei", "füüf": "föif",
    "ali": "alli", "mane": "manne", "irne": "ire", "öisne": "öise", "welle": "wele", "sölle": "söle",
    "werum": "wieso", "sig": "seig", "sigi": "seig", "seg": "seig", "seigid": "seiged", "heig": "heb", "heg": "heb",
    "häig": "heb", "heiged": "hebed", "heigid": "hebed", "wärdi": "wärd", "wärdid": "wärded",
    "wüssid": "wüssed", "übercho": "überchoo", "niemert": "niemer", "chünige": "chönige", "jumpfere": "jungfraue",
    "gsehne": "gseh", "frögt": "fröget", "himel": "himmel", "schriftgleerte": "schriftglehrte",
    "schriftgleert": "schriftglehrt", "schriftgelehrte": "schriftglehrte", "hüchler": "hüüchler", "find": "fiind",
    "spraach": "sprach", "spraache": "sprache", "schleeg": "schläg", "uussag": "ussag", "lieferet": "liferet",
    "fischternis": "fiischteri", "fischteri": "fiischteri", "tämpelwiiig": "tempelweihi", "brüedere": "brüeder",
    "stedt": "städt", "diräkt": "direkt", "tumm": "dumm",
}
_ZIEL.update(_ZIEL_R3)
_ZIEL.update(_ZIEL_R4)
for _regel, _woerter in _ERGAENZT.items():
    for _w in _woerter.split():
        WORTLISTE.setdefault(_w, (_ZIEL[_w], _regel))

# Formen, die automatisch ersetzt werden dürfen (eindeutig, nur in Mundart-Texten); alle übrigen nur melden.
NICHT_AUTOMATISCH = {"ihr", "war", "waren", "hatte", "hatten", "kam", "kamen", "sagte", "sagten", "ging", "gingen",
                     "sprach", "wurde", "wurden", "weg", "find", "ee", "ali", "zale", "sig", "heg", "seg", "gha", "loo", "dem"}

MUSTER = [
    # Entscheid Andi Neck 2026-11-24: «selig» wie gesprochen; Gott und Jesus ohne Artikel (de Heilig Geischt mit Artikel)
    (re.compile(r"\b[Ss]älig"), "sälig", "3 selig", "selig"),
    # «zum Gott d Ehr z gää» (Zweck: zum … z) bleibt; «em» ist oft Fürwort («seit em Jesus» = sagt ihm Jesus)
    # Gott mit Bestimmung ist Gattungswort und behält den Artikel (Entscheid Andi Neck 2026-11-24): «de Gott vom
    # Abraham», «de Gott vo Israel»; mit Adjektiv («de einzig wahr Gott») trifft das Muster ohnehin nicht
    (re.compile(r"\b(?:[Dd]e|[Vv]om|[Bb]im) (?:Jesus|Gott(?! vom?\b))\b|\b[Zz]um (?:Jesus|Gott(?! vom?\b))\b(?![^.,;:!?»]{0,40}\bz [a-zäöü])"), "Artikel vor Gott/Jesus", "2 Artikel", "Jesus, Gott; vo/zu/bi Jesus"),
    # Gegenrichtung: «Gott vo Israel», «Gott vom Fride» ohne Artikel → «de Gott vo …»; ausgenommen, wo «vo/vom» zum Verb
    # oder zu einem anderen Wort gehört («Gott vo ganzem Herze liebe», «laat Gott vom Böse ab», «was Gott vo sich seit»,
    # «underscheidet de Geischt vo Gott vom Geischt …»)
    (re.compile(r"(?<!\b[Dd]e )(?<!\b[Ee]n )(?<!\b[Ee]m )(?<!\b[Vv]om )(?<!\b[Zz]um )(?<!\b[Bb]im )(?<!\b[Ii]m )(?<!\bkei )"
                r"(?<!\bsin )(?<!\bmin )(?<!\bdin )(?<!\böise )\bGott vom? (?!ganzem\b|sich\b|Böse\b|Chliinere\b|Geischt\b)"), "Gott vo … ohne Artikel", "2 Artikel", "de Gott vo …"),
    # nicht umschreiben mit «em Abraham sin Gott» (Entscheid Andi Neck 2026-11-24)
    (re.compile(r"\bem [A-ZÄÖÜ][a-zäöü]+ sin Gott\b"), "em … sin Gott", "2 Artikel", "de Gott vom …"),
    (re.compile(r"[èòùì]"), "Sonderzeichen", "1.1", "nur ä, ö, ü"),
    (re.compile(r"\bum z\b", re.I), "um z", "2 Infinitiv", "zum / damit"),
    (re.compile(r"[A-Za-zäöü]['’][A-Za-zäöü]|(?<![A-Za-zäöü])['’]s\b|\b[sdz]['’]"), "Apostroph", "1.11", "ohne Apostroph"),
    (re.compile(r"\bdes\b"), "Genitiv «des»", "2 Genitiv", "vo + Dativ"),
    (re.compile(r"\b(?:[Ww]o|[Ww]ie|[Zz]ue|[Cc]ha) (?:er|es|em|en)\b"), "Gleit-n fehlt", "1.12", "won er, wien es, zuen em, chan er"),
    (re.compile(r"\b(?:[Ww]on|[Ww]ien) (?:ich|si|me|mer|ir)\b"), "Gleit-n zu viel", "1.12", "wo ich, wie si"),
    (re.compile(r"\b(?!(?:Sprung|Ursprung|Absprung|Schwung|Zwung|[A-ZÄÖÜa-zäöü]*[Zz]unge)\b)[A-ZÄÖÜ][a-zäöü]+ung(?:e|en)?\b"), "Endung -ung", "1.13", "-ig"),
    (re.compile(r"\b(?:sinds|solls|isch's|hät's|gits)\b"), "Kleinwort angehängt", "1.11", "sind s, soll s"),
]

_GLEIT = re.compile(r"\b([Ww]o|[Ww]ie|[Zz]ue|[Cc]ha) (er|es|em|en)\b")
_GLEIT_ZUVIEL = re.compile(r"\b([Ww]o|[Ww]ie)n (ich|si|me|mer|ir)\b")


def ersetze(text):
    """Wendet die eindeutigen Regeln automatisch an (Wortliste ausser NICHT_AUTOMATISCH, Gleit-n). Gross-/Kleinschreibung
    am Wortanfang bleibt erhalten. Nur auf Mundart-Text anwenden."""
    def wort(m):
        w = m.group(0)
        k = w.lower()
        if k not in WORTLISTE or k in NICHT_AUTOMATISCH or WORTLISTE[k][1] == "2 Präteritum":
            return w
        neu = WORTLISTE[k][0]
        if "…" in neu or "/" in neu:
            return w
        return neu[:1].upper() + neu[1:] if w[:1].isupper() else neu
    text = _WORT.sub(wort, text)
    text = _GLEIT.sub(lambda m: m.group(1) + "n " + m.group(2), text)
    text = _GLEIT_ZUVIEL.sub(lambda m: m.group(1) + " " + m.group(2), text)
    return text

_WORT = re.compile(r"[A-Za-zÄÖÜäöüÀ-ÿ]+")


# Werktitel und wörtliche fremdsprachige Zitate (Regel Runde 4): vor der Prüfung entfernt
FREMD = ["Matthew's Gospel", "Luke's Gospel", "Abba Isn't Daddy", "Das Evangelium des Johannes", "La date de la Cène",
         "Im Anfang war die Tat", "Giv'at ha-Mivtar", "Nevi'im", "ta'am", "La Légende des siècles", "Luke's", "ra'a"]


def pruefe(text):
    """Funde in einem Mundart-Text: Liste (gefunden, Regel, Vorschlag)."""
    funde = []
    for f in FREMD:
        text = (text or "").replace(f, " ")
    for w in _WORT.findall(text or ""):
        if len(w) > 1 and w.isupper():
            continue  # Datensatz-IDs wie FIND-LUK-0008
        k = w.lower()
        if k in WORTLISTE:
            neu, regel = WORTLISTE[k]
            if k == "find" and not w[0].isupper():
                continue  # «ich find» (finden) ist richtig; nur das Nomen «Find» → «Fiind»
            if regel == "2 Präteritum" and w[0].isupper():
                continue  # «Sprach», «War» als Nomen; Präteritum am Satzanfang fängt die getrennte Prüfung
            funde.append((w, regel, neu))
    for rx, was, regel, neu in MUSTER:
        for m in rx.finditer(text or ""):
            funde.append((m.group(0), regel, neu))
    return funde


_OHNE = {"id", "type", "status", "tags", "reference", "language", "subject", "subjects", "revision_log", "knowledge",
         "authorship_de", "check", "localizes", "target", "field", "fields_source"}


def _strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in _OHNE:
                yield from _strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from _strings(v)


_BUECHER = set("GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH EZR NEH EST JOB PSA PRO ECC SNG ISA JER LAM EZK "
                "DAN HOS JOL AMO OBA JON MIC NAM HAB ZEP HAG ZEC MAL MAT MRK LUK JHN ACT ROM 1CO 2CO GAL EPH PHP COL "
                "1TH 2TH 1TI 2TI TIT PHM HEB JAS 1PE 2PE 1JN 2JN 3JN JUD REV".split())


def _buch(name):
    for teil in re.split(r"[-_.]", name):
        if teil in _BUECHER:
            return teil
    return "übrige"


def korpus():
    """(Buch, Art, Stelle, Text) für alle Züritüütsch-Texte."""
    for f in sorted(glob.glob(os.path.join(ROOT, "data/translations/*GSW*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for ref, t in d.get("text_by_reference", {}).items():
            yield ref.split(".")[0], "Bibeltext", ref, t
    for f in sorted(glob.glob(os.path.join(ROOT, "data/localizations/gsw-u-sd-chzh/*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        name = os.path.basename(f)[:-5]
        for t in _strings(d.get("fields", d)):
            yield _buch(name), "Lokalisierung", name, t


def main(argv):
    if len(argv) > 1 and argv[1] == "--text":
        for f in pruefe(" ".join(argv[2:])):
            print(*f, sep="\t")
        return
    nur = argv[1] if len(argv) > 1 else None
    tab = defaultdict(Counter)
    for buch, art, wo, text in korpus():
        if nur and buch != nur:
            continue
        for gef, regel, neu in pruefe(text):
            tab[(buch, art)][regel] += 1
            if nur:
                print(f"{wo}\t{gef} -> {neu}\t[{regel}]")
    if not nur:
        regeln = sorted({r for c in tab.values() for r in c})
        print("Buch Art".ljust(24) + " ".join(r[:12].rjust(12) for r in regeln))
        for (buch, art), c in sorted(tab.items()):
            print(f"{buch} {art}".ljust(24) + " ".join(str(c[r]).rjust(12) for r in regeln))
        print("Summe".ljust(24) + " ".join(str(sum(c[r] for c in tab.values())).rjust(12) for r in regeln))


if __name__ == "__main__":
    main(sys.argv)
