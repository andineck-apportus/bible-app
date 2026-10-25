#!/usr/bin/env python3
"""Autorenwerkzeug: Bildlexikon – die stilunabhängige Schicht der Bildsprache.

Je Eintrag ein Datensatz vom Typ ``figure`` in data/illustrations/lexicon/FIG-<NAME>.json: WER oder WAS etwas ist
und WORAN man es in jedem Bildstil erkennt (Symbol, Skizze, später Anime/Malerei über einen Bildgenerator).
Darstellungen je Stil gehören nicht hierher, sondern in den jeweiligen Stil (data/illustrations/styles/).

Felder: kind (divine, person, role, group, object, place, action, sign), names (de/en), identity_de (ein Satz),
era (bei Personen und Rollen), traits (Pflicht-Erkennungsmerkmale mit basis text/tradition/design), palette
(verbindliche Grundfarben), rules_de, distinct_from (Einträge, mit denen nicht verwechselt werden darf), appears_in
(Bereiche in den bisher übersetzten Büchern, per Suche in den hochdeutschen Arbeitsübersetzungen ermittelt).

basis ehrlich: «text» nur, wenn der Bibeltext es sagt (mit Stelle); altkirchliche oder ikonographische Attribute
«tradition»; eigene Festlegungen «design». Keine antijüdischen Bildtraditionen; Ämter und Gruppen neutral.

Züridüütsch-Lokalisierung nur für identity_de. KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck;
keine fachliche Prüfung.

Aufruf: python3 scripts/authoring/bildlexikon.py
"""
import glob
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, localize, write  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-14; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft."
OUT = D / "illustrations" / "lexicon"
KINDS = {"divine", "person", "role", "group", "object", "place", "action", "sign"}
ERAS = {"patriarchs", "exodus", "judges", "kingdom", "exile", "second_temple", "nt", "any"}
BOOKS = ["RUT", "OBA", "JON", "MAT", "MRK", "LUK", "JHN", "PHP", "TIT", "1JN", "2JN", "3JN"]
BOOK_TAG = {"RUT": "TAG-RUTH", "OBA": "TAG-OBADIAH", "JON": "TAG-JONAH", "MAT": "TAG-MATTHEW", "MRK": "TAG-MARK",
            "LUK": "TAG-LUKE", "JHN": "TAG-JOHN", "PHP": "TAG-PHILIPPIANS", "TIT": "TAG-TITUS",
            "1JN": "TAG-JOHANNINE", "2JN": "TAG-JOHANNINE", "3JN": "TAG-JOHANNINE"}
MAX_RANGES = 10
APPEARS_NOTE = ("Per Suche in den hochdeutschen Arbeitsübersetzungen ermittelt (Suchmuster im Werkzeug "
                "scripts/authoring/bildlexikon.py); je Kapitel der Bereich von der ersten bis zur letzten Fundstelle; "
                "bei mehr als 10 Kapiteln nur die 10 mit den meisten Fundstellen.")
APPEARS_NONE = "Allgemeines Bildzeichen, nicht an bestimmte Stellen gebunden."

# Grundregeln, die für alle Personen gelten
FACE = ("Erkennbar an Farbe, Kleidung und Zeichen, nicht am Gesicht; im Stil Symbol ohne ausgeführtes Gesicht, in Stilen mit Gesichtern (Anime u. a.) "
        "Züge und Hautton von Menschen der Levante im 1. Jahrhundert")
NO_CARICATURE = "Keine Karikatur, keine verzerrten oder «typisierten» Gesichts- und Körpermerkmale"


def T(trait, basis, ref=None, note=None):
    t = {"trait_de": trait, "basis": basis}
    if ref:
        t["ref"] = f"[[{ref}]]"
    if note:
        t["note_de"] = note
    return t


ENTRIES = []


_GRUPPEN = None


_KURZ = None


def legend_short(fid):
    """Kurzer Legendentext je Sprache aus bildlexikon_daten/_legende.json ({FIG: {"de": …, "gsw": …}})."""
    global _KURZ
    if _KURZ is None:
        import pathlib as _p
        f = _p.Path(__file__).resolve().parent / "bildlexikon_daten" / "_legende.json"
        _KURZ = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    return _KURZ.get(fid)


def display_group(fid, kind):
    """Anzeigegruppe (Bildlexikon, Legende): divine, people, thing, place, action, concept (Entscheid 2026-10-23).
    Zeichen werden nach der Testklasse aufgeteilt (bildlexikon_daten/_gruppen.json); kind bleibt für die Bildplatzierung."""
    global _GRUPPEN
    if _GRUPPEN is None:
        import pathlib as _p
        f = _p.Path(__file__).resolve().parent / "bildlexikon_daten" / "_gruppen.json"
        _GRUPPEN = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    if kind in ("person", "role", "group"):
        return "people"
    if kind == "object":
        return "thing"
    if kind in ("sign", "action"):
        return _GRUPPEN.get(fid, "action" if kind == "action" else "concept")
    return kind


def E(fid, kind, de, en, ident, gsw, traits, pal, rules, era=None, find=None, distinct=(), tags=(), terms=None):
    ENTRIES.append(dict(id=fid, kind=kind, de=de, en=en, ident=ident, gsw=gsw, traits=traits, pal=pal, rules=rules,
                        era=era, find=find, distinct=list(distinct), tags=list(tags), terms=terms))


# ---------------------------------------------------------------------------------------------------------------
# 1. Göttlich
# ---------------------------------------------------------------------------------------------------------------
E("FIG-GOTT", "divine", "Gott", "God",
  "Der Gott Israels, im Alten Testament mit dem Eigennamen JHWH genannt ([[JON.1.1]]), von Jesus als «Vater» angeredet ([[MAT.6.9]]).",
  "De Gott vo Israel, im Alte Teschtamänt mit em Eigename JHWH gnännt ([[JON.1.1]]), vom Jesus als «Vater» aagredt ([[MAT.6.9]]).",
  [T("Goldener Strahlenkranz (Glorie) um eine helle Scheibe mit dem Gottesnamen יהוה in hebräischen Buchstaben", "tradition",
     note="Entscheid Andi Neck 2026-10-14. Der Gottesname im Strahlenkranz ist seit der Reformation in reformierten und lutherischen Kirchen verbreitet; "
          "er zeigt Gott, ohne ihn abzubilden. Ersetzt den Entwurf «segnende Hand aus der Wolke», der zu wenig verständlich war."),
   T("Kann sprechen und handeln: Sprechblasen und Handlungszeichen gehen vom Strahlenkranz aus", "design")],
  ("#D9A441", "#FFFDF6"),
  ["Gott nie als Mensch, nie mit Gesicht oder Körper darstellen",
   "Kreuznimbus über einer menschlichen Figur bleibt Jesus vorbehalten",
   "Nicht mit dem Zeichen «Licht» (FIG-ZEICHEN-LICHT, gefüllte Scheibe ohne Schrift) oder dem Zeichen-Stern verwechselbar",
   "Die Buchstaben werden nicht ausgesprochen dargestellt (keine Umschrift im Bild); Vorlesen nach der Einstellung «Jahwe» bzw. «Adonai»"],
  terms=[{"lang": "heb", "word": "יהוה", "translit": "JHWH", "de": "Gottesname (Tetragramm), im hebräischen Text ohne Vokale geschrieben"}],
  find=[(r"\bGott(es)?\b|JHWH", None)], distinct=["FIG-JESUS", "FIG-HEILIGER-GEIST", "FIG-ZEICHEN-STERN"])

E("FIG-HEILIGER-GEIST", "divine", "Heiliger Geist", "Holy Spirit",
  "Der Geist Gottes, der wie eine Taube auf Jesus herabkommt ([[JHN.1.32]], [[MRK.1.10]]) und den Jesus als Beistand verheisst ([[JHN.14.26]]).",
  "De Geischt vo Gott, wo wie e Tuube uf de Jesus abechunnt ([[JHN.1.32]], [[MRK.1.10]]) und wo de Jesus als Biistand verheisst ([[JHN.14.26]]).",
  [T("Weisse Taube im Flug von oben nach unten", "text", "JHN.1.32", "Der Text sagt «wie eine Taube»: ein Vergleich, das Bild nimmt ihn auf."),
   T("Kreuznimbus bzw. goldener Schein um die Taube", "tradition"),
   T("Feuerzungen", "text", "ACT.2.3", "Nur für Pfingsten bzw. das Wirken des Geistes in der Gemeinde; Apostelgeschichte noch nicht übersetzt.")],
  ("#FFFFFF", "#D9A441"),
  ["Nie als Mensch darstellen",
   "Die Geist-Taube trägt immer Nimbus oder Lichtschein und kommt von oben; die Taube als Tier (FIG-OBJ-TAUBE) nie mit Nimbus",
   "Nicht mit einem Engel verwechselbar (keine Flügelgestalt mit Körper)"],
  find=[(r"[Hh]eilige[nmr]? Geist|Geist wie eine Taube|Geist der Wahrheit|Beistand", None)],
  distinct=["FIG-OBJ-TAUBE", "FIG-ROLLE-ENGEL", "FIG-GOTT"], tags=["TAG-HOLY-SPIRIT"])

E("FIG-JESUS", "divine", "Jesus", "Jesus",
  "Jesus aus Nazaret, Sohn der Maria ([[MRK.6.3]]); die Evangelien bekennen ihn als Christus und Sohn Gottes ([[MRK.1.1]], [[JHN.20.31]]).",
  "De Jesus vo Nazaret, de Sohn vo de Maria ([[MRK.6.3]]); d Evangelie bekänned en als Chrischtus und Sohn vo Gott ([[MRK.1.1]], [[JHN.20.31]]).",
  [T("Kreuznimbus (goldener Schein mit Kreuz)", "tradition"),
   T("Weisses Gewand, roter Mantel", "tradition", note="Farben nach alter Bildtradition, in der Symbol-Bibliothek festgelegt (#F4F1EA/#A33A2E).")],
  ("#F4F1EA", "#A33A2E"),
  [FACE, "In jeder Szene die einzige menschliche Figur mit Kreuznimbus",
   "Den purpurnen Spottmantel der Passion ([[JHN.19.2]]) als eigenes Gewandstück zeigen, nicht mit dem roten Mantel gleichsetzen",
   "Als jüdischer Mann seiner Zeit darstellen, nicht europäisiert"],
  era="nt", find=[(r"\bJesus\b|\bJesu\b|\bChristus\b", None)], distinct=["FIG-GOTT", "FIG-ROLLE-ENGEL"])

# ---------------------------------------------------------------------------------------------------------------
# 2. Personen
# ---------------------------------------------------------------------------------------------------------------
NAMESAKE = "Gleichnamige Personen nie nur am Namen unterscheiden, sondern an Farbe und Zeichen"
# Gemeinsames Jüngermerkmal (Runde 4, 2026-10-23): ohne gemeinsames Merkmal wurden die Zwölf im Blindtest Runde 3 nicht als Jünger erkannt
JUENGER_T = T("Jüngermerkmal wie die Zwölf: erdfarbenes Jüngergewand mit dunklem Gürtel, Wanderstab an der linken Schulter", "design",
              note="Wanderstab nach [[MRK.6.8]]; Gewandfarbe und Gürtel wie FIG-GRUPPE-ZWOELF, dazu eigene Mantelfarbe und eigenes Zeichen auf der Brust")

# --- Marias
E("FIG-MARIA-MUTTER-JESU", "person", "Maria, Mutter Jesu", "Mary, mother of Jesus",
  "Die Mutter Jesu; bei Johannes nur «die Mutter Jesu» genannt ([[JHN.2.1]], [[JHN.19.25]]), bei Markus Maria ([[MRK.6.3]]).",
  "D Mueter vom Jesus; bim Johannes nu «d Mueter vom Jesus» gnännt ([[JHN.2.1]], [[JHN.19.25]]), bim Markus Maria ([[MRK.6.3]]).",
  [T("Blauer Schleier und blaues Gewand", "tradition")],
  ("#3E6E9E", "#2E5478"),
  [FACE, NAMESAKE, "Kein Nimbus in den Szenen der Evangelien, damit sie nicht mit Jesus verwechselt wird",
   "Dunkelblau bleibt ihr vorbehalten; andere Frauen nicht in Blau"],
  era="nt", find=[(r"Mutter|Maria", ["JHN.2.1-JHN.2.12", "JHN.19.25-JHN.19.27", "MRK.3.31-MRK.3.35", "MRK.6.3"])],
  distinct=["FIG-MARIA-MAGDALA", "FIG-MARIA-BETANIEN", "FIG-MARIA-KLOPAS", "FIG-MARIA-MUTTER-JAKOBUS"])

E("FIG-MARIA-MAGDALA", "person", "Maria aus Magdala", "Mary Magdalene",
  "Jüngerin aus Magdala, Zeugin der Kreuzigung und erste Zeugin des Auferstandenen ([[JHN.20.1-JHN.20.18]], [[MRK.16.1]]).",
  "Jüngerin vo Magdala, Züügin vo de Chrüüzigung und di erscht Züügin vom Uferstandne ([[JHN.20.1-JHN.20.18]], [[MRK.16.1]]).",
  [T("Alabastergefäss mit Deckel", "tradition", note="Knüpft an [[MRK.16.1]] an (wohlriechende Öle, um ihn zu salben)."),
   T("Weinroter Mantel über hellem Gewand", "design"),
   T("Offenes Felsengrab hinter ihr: sie kommt früh am Morgen zum Grab", "text", "JHN.20.1", "Unterscheidet sie von Maria von Betanien (Blindtest Runde 3)")],
  ("#8E3B5E", "#E2CDA8"),
  [FACE, NAMESAKE,
   "Nicht mit der Sünderin aus [[LUK.7.37]] oder mit Maria von Betanien gleichsetzen; diese Gleichsetzung ist spätere westliche Tradition",
   "Nicht mit offenem Haar oder als Büsserin darstellen"],
  era="nt", find=[(r"Magdala", None)],
  distinct=["FIG-MARIA-BETANIEN", "FIG-MARIA-MUTTER-JESU", "FIG-SALOME", "FIG-MARIA-MUTTER-JAKOBUS"])

E("FIG-MARIA-BETANIEN", "person", "Maria von Betanien", "Mary of Bethany",
  "Schwester von Marta und Lazarus in Betanien, die Jesus mit Nardenöl die Füsse salbt ([[JHN.11.1-JHN.11.2]], [[JHN.12.3]]).",
  "D Schwöschter vo de Marta und vom Lazarus z Betanie, wo em Jesus mit Nardeöl d Füess salbt ([[JHN.11.1-JHN.11.2]], [[JHN.12.3]]).",
  [T("Schlankes Nardenfläschchen, aus dem Öl auf einen Fuss tropft", "text", "JHN.12.3"),
   T("Offenes Haar (sie trocknet seine Füsse mit ihren Haaren)", "text", "JHN.12.3"),
   T("Graugrünes Gewand", "design")],
  ("#6B8E7A", "#E9D8B4"),
  [FACE, NAMESAKE, "Nicht mit Maria aus Magdala oder der namenlosen Frau aus [[MRK.14.3]] gleichsetzen"],
  era="nt", find=[(r"Maria", ["JHN.11", "JHN.12.3"])],
  distinct=["FIG-MARIA-MAGDALA", "FIG-MARTA", "FIG-MARIA-MUTTER-JESU"])

E("FIG-MARIA-KLOPAS", "person", "Maria, Frau des Klopas", "Mary, wife of Clopas",
  "Eine der Frauen beim Kreuz Jesu ([[JHN.19.25]]).",
  "Eini vo de Fraue bim Chrüüz vom Jesus ([[JHN.19.25]]).",
  [T("Violettgraues Kopftuch", "design")],
  ("#7A6A8E", "#D8CBB0"),
  [FACE, NAMESAKE,
   "Ob sie mit der «Schwester seiner Mutter» oder mit Maria, der Mutter des Jakobus, identisch ist, lässt der Text offen; im Bild nicht festlegen"],
  era="nt", find=[(r"Klopas", None)], distinct=["FIG-MARIA-MUTTER-JAKOBUS", "FIG-MARIA-MUTTER-JESU"])

E("FIG-MARIA-MUTTER-JAKOBUS", "person", "Maria, Mutter des Jakobus und Joses", "Mary, mother of James and Joses",
  "Eine der Frauen, die die Kreuzigung von fern sehen und am ersten Tag der Woche zum Grab gehen ([[MRK.15.40]], [[MRK.16.1]]).",
  "Eini vo de Fraue, wo d Chrüüzigung vo wiitem gsänd und am erschte Tag vo de Wuche zum Grab gönd ([[MRK.15.40]], [[MRK.16.1]]).",
  [T("Olivfarbenes Gewand", "design"), T("Ölkrug mit wohlriechendem Öl", "text", "MRK.16.1")],
  ("#6E7F5A", "#D8CBB0"),
  [FACE, NAMESAKE, "Ihr Ölgefäss offen, ohne Deckel, damit es sich vom Salbgefäss der Maria aus Magdala unterscheidet"],
  era="nt", find=[(r"Maria", ["MRK.15.40", "MRK.15.47", "MRK.16.1"])],
  distinct=["FIG-MARIA-KLOPAS", "FIG-MARIA-MAGDALA", "FIG-SALOME"])

E("FIG-SALOME", "person", "Salome (Jüngerin)", "Salome (disciple)",
  "Eine der Frauen, die Jesus in Galiläa folgten und beim Kreuz und am Grab sind ([[MRK.15.40-MRK.15.41]], [[MRK.16.1]]).",
  "Eini vo de Fraue, wo em Jesus z Galiläa nachegfolgt sind und bim Chrüüz und am Grab sind ([[MRK.15.40-MRK.15.41]], [[MRK.16.1]]).",
  [T("Ockerfarbenes Kopftuch", "design"), T("Ölkrug mit wohlriechendem Öl", "text", "MRK.16.1"),
   T("Älter, mit grauem Haar", "design", note="Wenn sie die Mutter der Söhne des Zebedäus ist ([[MAT.27.56]]), hat sie erwachsene Söhne")],
  ("#B07A3E", "#F2E6CC"),
  [FACE, "Nicht mit der Tochter der Herodias verwechseln, die im Text keinen Namen trägt ([[MRK.6.22]])"],
  era="nt", find=[(r"Salome", None)], distinct=["FIG-TOCHTER-HERODIAS", "FIG-MARIA-MAGDALA"])

# --- Johannes, Jakobus, Simon, Judas: Gleichnamige
E("FIG-JOHANNES-TAEUFER", "person", "Johannes der Täufer", "John the Baptist",
  "Der von Gott gesandte Zeuge, der in der Wüste tauft und auf Jesus als das Lamm Gottes weist ([[JHN.1.6]], [[JHN.1.29]], [[MRK.1.4]]).",
  "De vo Gott gschickt Züüg, wo i de Wüeschti tauft und uf de Jesus als s Lamm vo Gott zeigt ([[JHN.1.6]], [[JHN.1.29]], [[MRK.1.4]]).",
  [T("Gewand aus Kamelhaar mit Ledergurt", "text", "MRK.1.6"),
   T("Kreuzstab", "tradition"),
   T("Lamm als Hinweis auf Jesus", "tradition", note="Nach seinem Wort «Siehe, das Lamm Gottes» ([[JHN.1.29]]); im Bild als Hinweiszeichen, nicht als Tier der Szene."),
   T("Ausgestreckter Zeigefinger zu Jesus hin", "tradition")],
  ("#8A6A3A", "#5B4630"),
  [FACE, NAMESAKE, "Nicht mit Johannes, dem Sohn des Zebedäus, verwechseln",
   "Der Kreuzstab ist kein Kreuz der Kreuzigung: dünn, lang, kleines Querholz"],
  era="nt", find=[(r"Johannes", ["JHN.1.6-JHN.1.40", "JHN.3.23-JHN.3.27", "JHN.4.1", "JHN.5.33-JHN.5.36", "JHN.10.40-JHN.10.41",
                                  "MRK.1.4-MRK.1.14", "MRK.2.18", "MRK.6.14-MRK.6.29", "MRK.8.28", "MRK.11.30-MRK.11.32", "LUK.11.1"])],
  distinct=["FIG-JOHANNES-ZEBEDAEUS", "FIG-DER-AELTESTE", "FIG-OBJ-KREUZ"])

E("FIG-JOHANNES-ZEBEDAEUS", "person", "Johannes, Sohn des Zebedäus", "John, son of Zebedee",
  "Einer der Zwölf, Bruder des Jakobus, Fischer am See von Galiläa ([[MRK.1.19-MRK.1.20]], [[MRK.3.17]]).",
  "Eine vo de Zwölf, de Brüeder vom Jakobus, Fischer am See vo Galiläa ([[MRK.1.19-MRK.1.20]], [[MRK.3.17]]).",
  [T("Jüngergewand mit taubenblauem Mantel", "design"),
   T("Kelch mit Schlange", "tradition", note="Altkirchliche Legende vom Giftbecher; die Schlange unterscheidet ihn vom Becher des Mundschenks (Blindtest Runde 3)."),
   T("Ohne Bart, jugendlich, kurzes Haar", "tradition"), JUENGER_T],
  ("#9C7A4C", "#6A8FB3"),
  [FACE, NAMESAKE,
   "Gleichsetzung mit dem Evangelisten, dem Jünger, den Jesus liebte, und dem «Ältesten» der Briefe ist Tradition; im Bild nur mit Hinweis auf die Deutung verbinden",
   "Den Adler (Symbol des Evangelisten) nicht ihm, sondern dem Buch Johannes zuordnen"],
  era="nt", find=[(r"Johannes", ["MRK.1.19", "MRK.1.29", "MRK.3.17", "MRK.5.37", "MRK.9.2", "MRK.9.38", "MRK.10.35",
                                  "MRK.10.41", "MRK.13.3", "MRK.14.33"]), (r"Zebedäus", ["JHN.21.2"])],
  distinct=["FIG-JOHANNES-TAEUFER", "FIG-LIEBLINGSJUENGER", "FIG-DER-AELTESTE", "FIG-JAKOBUS-ZEBEDAEUS"])

E("FIG-LIEBLINGSJUENGER", "person", "Der Jünger, den Jesus liebte", "The disciple whom Jesus loved",
  "Ein namenloser Jünger im Johannesevangelium, der beim Mahl an der Brust Jesu liegt und beim Kreuz steht ([[JHN.13.23]], [[JHN.19.26]]).",
  "En Jünger ohni Name im Johannesevangelium, wo bim Mahl a de Bruscht vom Jesus liit und bim Chrüüz staat ([[JHN.13.23]], [[JHN.19.26]]).",
  [T("Nah bei Jesus, an seine Brust gelehnt (beim Mahl)", "text", "JHN.13.23"),
   T("Jüngergewand mit hellem Mantel", "design"), T("Kurzes, lockiges Haar, ohne Bart", "design"),
   T("Herz als Zeichen: der Jünger, den Jesus liebte", "text", "JHN.13.23"), JUENGER_T],
  ("#9C7A4C", "#E2CDA8"),
  [FACE, "Der Text nennt keinen Namen; die Gleichsetzung mit Johannes, dem Sohn des Zebedäus, ist Tradition und im Bild als Deutung zu kennzeichnen"],
  era="nt", find=[(r"den Jesus liebte|den er liebte|den Jesus lieb hatte", None)],
  distinct=["FIG-JOHANNES-ZEBEDAEUS"])

E("FIG-JAKOBUS-ZEBEDAEUS", "person", "Jakobus, Sohn des Zebedäus", "James, son of Zebedee",
  "Einer der Zwölf, Bruder des Johannes, Fischer am See von Galiläa ([[MRK.1.19]], [[MRK.3.17]]).",
  "Eine vo de Zwölf, de Brüeder vom Johannes, Fischer am See vo Galiläa ([[MRK.1.19]], [[MRK.3.17]]).",
  [T("Grosse naturweisse Jakobsmuschel mit Rippen", "tradition", note="Allein auf der Brust: Muschel am Stab las sich als Fächer (Blindtest Runde 2), orange als Fächer (Runde 3)."),
   T("Jüngergewand mit petrolfarbenem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#2F6F73"),
  [FACE, NAMESAKE, "Nicht mit Jakobus, dem Sohn des Alphäus, verwechseln"],
  era="nt", find=[(r"Jakobus", ["MRK.1.19", "MRK.1.29", "MRK.3.17", "MRK.5.37", "MRK.9.2", "MRK.10.35-MRK.10.41", "MRK.13.3", "MRK.14.33"]),
                  (r"Zebedäus", ["JHN.21.2"])],
  distinct=["FIG-JAKOBUS-ALPHAEUS", "FIG-JOHANNES-ZEBEDAEUS"])

E("FIG-JAKOBUS-ALPHAEUS", "person", "Jakobus, Sohn des Alphäus", "James, son of Alphaeus",
  "Einer der Zwölf ([[MRK.3.18]]).",
  "Eine vo de Zwölf ([[MRK.3.18]]).",
  [T("Walkerstange: langer Stab mit flachem, geradem Brett", "tradition"), T("Jüngergewand mit schiefergrauem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#6B6B8A"),
  [FACE, NAMESAKE, "Ob er mit «Jakobus dem Kleinen» ([[MRK.15.40]]) identisch ist, bleibt offen; im Bild nicht festlegen"],
  era="nt", find=[(r"Alphäus", ["MRK.3.18"])], distinct=["FIG-JAKOBUS-ZEBEDAEUS", "FIG-LEVI"])

E("FIG-PETRUS", "person", "Simon Petrus", "Simon Peter",
  "Fischer aus Betsaida, einer der Zwölf, dem Jesus den Namen Kephas, «Fels», gibt ([[JHN.1.42]], [[MRK.3.16]]).",
  "Fischer vo Betsaida, eine vo de Zwölf, wo de Jesus de Name Kephas, «Fels», git ([[JHN.1.42]], [[MRK.3.16]]).",
  [T("Schlüssel", "tradition", note="Nach [[MAT.16.19]]; Matthäus 16 ist noch nicht übersetzt."),
   T("Jüngergewand mit ockerfarbenem Mantel", "tradition"),
   T("Kurzer grauer Bart, krauses Haar", "tradition"), JUENGER_T],
  ("#9C7A4C", "#C08A2A"),
  [FACE, NAMESAKE, "Nicht mit Simon dem Kananäer oder Simon von Kyrene verwechseln",
   "Schlüssel nur bei Petrus; Marta erhält eine Schöpfkelle, keinen Schlüsselbund"],
  era="nt", find=[(r"Petrus|Kephas", None), (r"Simon", ["MRK.1.16-MRK.1.36"])],
  distinct=["FIG-SIMON-KANANAEUS", "FIG-SIMON-KYRENE", "FIG-ANDREAS"],
  terms=[{"lang": "grc", "word": "Κηφᾶς", "de": "Kephas (griechische Umschrift eines aramäischen Wortes für «Fels»)"}])

E("FIG-ANDREAS", "person", "Andreas", "Andrew",
  "Fischer, Bruder des Simon Petrus, zuerst Jünger des Johannes, dann einer der Zwölf ([[JHN.1.40]], [[MRK.1.16]]).",
  "Fischer, de Brüeder vom Simon Petrus, zerscht Jünger vom Johannes, dänn eine vo de Zwölf ([[JHN.1.40]], [[MRK.1.16]]).",
  [T("Schräges Kreuz in X-Form aus zwei Holzbalken", "tradition"), T("Jüngergewand mit olivgrünem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#6E8B3D"),
  [FACE, "Das X-Kreuz nie mit dem Kreuz Jesu verwechselbar: schräg, aus zwei gleich langen Balken, ohne Tafel"],
  era="nt", find=[(r"Andreas", None)], distinct=["FIG-PETRUS", "FIG-OBJ-KREUZ"])

E("FIG-PHILIPPUS", "person", "Philippus", "Philip",
  "Einer der Zwölf aus Betsaida, der Natanaël zu Jesus führt ([[JHN.1.43-JHN.1.46]], [[MRK.3.18]]).",
  "Eine vo de Zwölf vo Betsaida, wo de Natanaël zum Jesus füert ([[JHN.1.43-JHN.1.46]], [[MRK.3.18]]).",
  [T("Stabkreuz: langer Holzstab mit kleinem goldenem Kreuz oben", "tradition", note="Kurzes Kreuz allein las sich als Kreuz des Kreuzträgers (Blindtest Runde 3)"),
   T("Jüngergewand mit fliederfarbenem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#8F6BA8"),
  [FACE, "Nicht mit Philippus, dem Bruder des Herodes ([[MRK.6.17]]), verwechseln"],
  era="nt", find=[(r"Philippus", ["JHN", "MRK.3.18"])], distinct=["FIG-NATANAEL"])

E("FIG-NATANAEL", "person", "Natanaël", "Nathanael",
  "Jünger aus Kana, den Jesus unter dem Feigenbaum gesehen hat ([[JHN.1.45-JHN.1.49]], [[JHN.21.2]]).",
  "Jünger vo Kana, wo de Jesus under em Fiigebaum gseh hät ([[JHN.1.45-JHN.1.49]], [[JHN.21.2]]).",
  [T("Kleiner Feigenbaum mit Feigen", "text", "JHN.1.48"), T("Jüngergewand mit feigengrünem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#5E7F3A"),
  [FACE, "Die Gleichsetzung mit Bartholomäus ist Tradition; im Bild zwei Einträge, nur mit Hinweis verbinden"],
  era="nt", find=[(r"Natanaël", None)], distinct=["FIG-BARTHOLOMAEUS", "FIG-PHILIPPUS"])

E("FIG-BARTHOLOMAEUS", "person", "Bartholomäus", "Bartholomew",
  "Einer der Zwölf, in der Liste bei Markus genannt ([[MRK.3.18]]).",
  "Eine vo de Zwölf, i de Lischte bim Markus gnännt ([[MRK.3.18]]).",
  [T("Messer, gesenkt mit der Spitze nach unten", "tradition", note="Schräg nach oben las es sich als Opfermesser Abrahams (Blindtest Runde 3)"),
   T("Jüngergewand mit rotbraunem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#7A4E3A"),
  [FACE, "Messer gesenkt gezeigt, nicht als Waffe; nicht mit dem Schwert des Paulus verwechselbar"],
  era="nt", find=[(r"Bartholomäus", None)], distinct=["FIG-NATANAEL", "FIG-PAULUS"])

E("FIG-MATTHAEUS", "person", "Matthäus", "Matthew",
  "Einer der Zwölf, in der Liste bei Markus genannt ([[MRK.3.18]]).",
  "Eine vo de Zwölf, i de Lischte bim Markus gnännt ([[MRK.3.18]]).",
  [T("Buch und Schreibfeder", "tradition", note="Als Evangelist; das Engel- bzw. Menschensymbol gehört zum Buch Matthäus."),
   T("Zwei Münzen beim Buch: Matthäus, der Zöllner", "text", "MAT.10.3"),
   T("Jüngergewand mit stahlblauem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#3F5A7A"),
  [FACE, "Die Gleichsetzung mit Levi aus [[MRK.2.14]] stützt sich auf [[MAT.9.9]]; bei Markus zwei Namen, im Bild nur mit Hinweis verbinden"],
  era="nt", find=[(r"Matthäus", None)], distinct=["FIG-LEVI", "FIG-ROLLE-SCHRIFTGELEHRTER"])

E("FIG-LEVI", "person", "Levi, Sohn des Alphäus", "Levi, son of Alphaeus",
  "Zöllner, den Jesus von der Zollstelle weg in die Nachfolge ruft ([[MRK.2.14]]).",
  "En Zöllner, wo de Jesus vo de Zollstell eweg i d Nachfolg rüeft ([[MRK.2.14]]).",
  [T("Zolltisch mit Münzen", "text", "MRK.2.14"), T("Gewand mit graugrünem Mantel", "design")],
  ("#4A6B5A", "#D9A441"),
  [FACE, "Nicht als Händler darstellen (kein Kopftuch mit Geldbeutel)", NO_CARICATURE],
  era="nt", find=[(r"\bLevi\b", None)], distinct=["FIG-MATTHAEUS", "FIG-ROLLE-HAENDLER", "FIG-JAKOBUS-ALPHAEUS"])

E("FIG-THOMAS", "person", "Thomas", "Thomas",
  "Einer der Zwölf, «Didymus» (Zwilling) genannt, der den Auferstandenen sehen und berühren will ([[JHN.20.24-JHN.20.28]]).",
  "Eine vo de Zwölf, «Didymus» (Zwilling) gnännt, wo de Uferstandni wott gseh und berüere ([[JHN.20.24-JHN.20.28]]).",
  [T("Hand mit Wundmal, auf das ein Finger zeigt (er will die Wunden berühren)", "text", "JHN.20.25-JHN.20.27",
     "Ersetzt das Winkelmass der Tradition, das sich als Baumeister las (Blindtest Runde 3)"),
   T("Jüngergewand mit bernsteinfarbenem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#A0703A"),
  [FACE, "Nicht als «Zweifler» karikieren; sein Bekenntnis ([[JHN.20.28]]) gehört zum Bild"],
  era="nt", find=[(r"Thomas", None)],
  terms=[{"lang": "grc", "word": "Δίδυμος", "de": "Zwilling"}])

E("FIG-THADDAEUS", "person", "Thaddäus", "Thaddaeus",
  "Einer der Zwölf, in der Liste bei Markus genannt ([[MRK.3.18]]).",
  "Eine vo de Zwölf, i de Lischte bim Markus gnännt ([[MRK.3.18]]).",
  [T("Knorrige Holzkeule, oben dick, ohne runden Kopf", "tradition"), T("Jüngergewand mit kräftig moosgrünem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#5F7A2A"),
  [FACE, "Gleichsetzung mit Judas, nicht der Iskariot ([[JHN.14.22]]), ist Tradition; im Bild zwei Einträge"],
  era="nt", find=[(r"Thaddäus", None)], distinct=["FIG-JUDAS-NICHT-ISKARIOT"])

E("FIG-SIMON-KANANAEUS", "person", "Simon der Kananäer", "Simon the Cananaean",
  "Einer der Zwölf, mit Beinamen «der Kananäer» ([[MRK.3.18]]).",
  "Eine vo de Zwölf, mit em Biiname «de Kananäer» ([[MRK.3.18]]).",
  [T("Handsäge mit Zahnblatt und Holzgriff", "tradition"), T("Jüngergewand mit rostrotem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#9A4E4E"),
  [FACE, NAMESAKE, "Nicht mit Simon Petrus oder Simon von Kyrene verwechseln"],
  era="nt", find=[(r"Kananäer", None)], distinct=["FIG-PETRUS", "FIG-SIMON-KYRENE"])

E("FIG-JUDAS-ISKARIOT", "person", "Judas Iskariot", "Judas Iscariot",
  "Einer der Zwölf, der die gemeinsame Kasse führt und Jesus ausliefert ([[JHN.12.4-JHN.12.6]], [[MRK.14.10]]).",
  "Eine vo de Zwölf, wo di gmeinsam Kasse füert und de Jesus uusliferet ([[JHN.12.4-JHN.12.6]], [[MRK.14.10]]).",
  [T("Kasse (Kästchen) mit Einwurfschlitz, eine Münze fällt hinein", "text", "JHN.12.6"), T("Jüngergewand mit graublauem Mantel", "design"), JUENGER_T],
  ("#9C7A4C", "#7A8A9A"),
  [FACE, NAMESAKE,
   "Keine antijüdische Bildtradition: nicht in Gelb, keine Karikatur, keine abweichenden Gesichts- oder Haarmerkmale, kein Geldsack als Erkennungszeichen",
   "Nicht dunkler oder bedrohlicher gekleidet als die übrigen Jünger",
   "Nicht mit Judas, nicht der Iskariot, verwechseln"],
  era="nt", find=[(r"Judas|Iskariot", ["JHN.6.71", "JHN.12.4", "JHN.13", "JHN.18", "MRK.3.19", "MRK.14"])],
  distinct=["FIG-JUDAS-NICHT-ISKARIOT", "FIG-ROLLE-HAENDLER"])

E("FIG-JUDAS-NICHT-ISKARIOT", "person", "Judas, nicht der Iskariot", "Judas, not Iscariot",
  "Ein Jünger, der Jesus beim Abschiedsmahl fragt, warum er sich nur ihnen offenbart ([[JHN.14.22]]).",
  "En Jünger, wo de Jesus bim Abschiidsmahl fröget, werum er sich nu ine offebaart ([[JHN.14.22]]).",
  [T("Jüngergewand mit graugrünem Mantel", "design"), T("Sprechblase mit Fragezeichen (seine Frage an Jesus)", "text", "JHN.14.22"),
   T("Brot und Becher unter der Sprechblase (die Frage fällt beim Abschiedsmahl)", "design", note="Mahl nach [[JHN.13.2]]"),
   T("Lockiges Haar (zur Unterscheidung von Thomas)", "design"), JUENGER_T],
  ("#9C7A4C", "#5F8F8A"),
  [FACE, NAMESAKE, "Nie mit dem Kästchen des Judas Iskariot"],
  era="nt", find=[(r"nicht der Iskariot", None)], distinct=["FIG-JUDAS-ISKARIOT", "FIG-THADDAEUS"])

# --- weitere Personen der Evangelien
E("FIG-MARTA", "person", "Marta", "Martha",
  "Schwester von Maria und Lazarus in Betanien, die Jesus als Christus bekennt und beim Mahl bedient ([[JHN.11.20-JHN.11.27]], [[JHN.12.2]]).",
  "D Schwöschter vo de Maria und vom Lazarus z Betanie, wo de Jesus als Chrischtus bekännt und bim Mahl serviert ([[JHN.11.20-JHN.11.27]], [[JHN.12.2]]).",
  [T("Schöpfkelle", "tradition", note="Anknüpfend an ihr Dienen beim Mahl ([[JHN.12.2]])."), T("Terrakottafarbenes Gewand", "design")],
  ("#B4704A", "#E9D8B4"),
  [FACE, "Nicht als Dienerin im Sinn der Rolle FIG-ROLLE-DIENER (keine Schürze)"],
  era="nt", find=[(r"Marta", None)], distinct=["FIG-MARIA-BETANIEN", "FIG-ROLLE-DIENER"])

E("FIG-LAZARUS", "person", "Lazarus", "Lazarus",
  "Bruder von Marta und Maria in Betanien, den Jesus aus dem Grab ruft ([[JHN.11.1]], [[JHN.11.43-JHN.11.44]]).",
  "De Brüeder vo de Marta und de Maria z Betanie, wo de Jesus us em Grab usegrüeft hät ([[JHN.11.1]], [[JHN.11.43-JHN.11.44]]).",
  [T("Mit Binden umwickelt, Schweisstuch (beim Herauskommen)", "text", "JHN.11.44"),
   T("Offenes Felsengrab, der Stein weggerollt (als Zeichen)", "text", "JHN.11.38-JHN.11.41"),
   T("Helles Gewand mit graubraunem Gürtel (beim Mahl)", "design")],
  ("#E7DCC4", "#8A7A60"),
  [FACE, "Nicht als Mumie oder Schreckgestalt"],
  era="nt", find=[(r"Lazarus", None)])

E("FIG-NIKODEMUS", "person", "Nikodemus", "Nicodemus",
  "Pharisäer und Ratsherr, der nachts zu Jesus kommt und ihn später mit Myrrhe und Aloe begräbt ([[JHN.3.1-JHN.3.2]], [[JHN.19.39]]).",
  "En Pharisäer und Ratsherr, wo znacht zum Jesus chunnt und en spöter mit Myrrhe und Aloe begrabt ([[JHN.3.1-JHN.3.2]], [[JHN.19.39]]).",
  [T("Öllampe (er kommt bei Nacht)", "text", "JHN.3.2"), T("Nachtblaues Obergewand und nachtblauer Turban (keine Kapuze)", "design"),
   T("Gefäss mit Myrrhe und Aloe (bei der Grablegung)", "text", "JHN.19.39")],
  ("#3B4A6B", "#C9BFAA"),
  [FACE, "Als Pharisäer neutral und würdig nach Amt", NO_CARICATURE],
  era="nt", find=[(r"Nikodemus", None)], distinct=["FIG-ROLLE-PHARISAEER", "FIG-JOSEF-ARIMATAEA"])

E("FIG-JOSEF-ARIMATAEA", "person", "Josef von Arimatäa", "Joseph of Arimathea",
  "Angesehenes Ratsmitglied und heimlicher Jünger, der Pilatus um den Leib Jesu bittet und ihn begräbt ([[MRK.15.43-MRK.15.46]], [[JHN.19.38]]).",
  "Es aagsehnigs Ratsmitglid und heimlich en Jünger, wo de Pilatus um de Liib vom Jesus bittet und en begrabt ([[MRK.15.43-MRK.15.46]], [[JHN.19.38]]).",
  [T("Leinentuch über der Schulter", "text", "MRK.15.46"), T("Grauer Ratsherrenmantel über schieferblauem Gewand", "design")],
  ("#5A5A5A", "#7A8AA0"),
  [FACE, "Nicht mit Josef, dem Vater Jesu ([[JHN.1.45]]), verwechseln"],
  era="nt", find=[(r"Josef|Arimatäa", ["JHN.19.38-JHN.19.42", "MRK.15.43-MRK.15.46"])], distinct=["FIG-NIKODEMUS"])

E("FIG-KAJAFAS", "person", "Kajafas", "Caiaphas",
  "Hohepriester in jenem Jahr, der rät, einer solle für das Volk sterben ([[JHN.11.49-JHN.11.50]], [[JHN.18.24]]).",
  "Hohepriester i dem Jaar, wo raatet, eine söll für s Volk sterbe ([[JHN.11.49-JHN.11.50]], [[JHN.18.24]]).",
  [T("Amtskleid des Hohepriesters mit Brustschild", "design", note="Neutral nach Amt (siehe FIG-ROLLE-HOHEPRIESTER)."),
   T("Goldene Stirnplatte", "design")],
  ("#4A5A7A", "#D9A441"),
  [FACE, NO_CARICATURE, "Nicht bedrohlich oder dämonisch darstellen; neutral nach Amt"],
  era="nt", find=[(r"Kajafas", None)], distinct=["FIG-HANNAS", "FIG-ROLLE-HOHEPRIESTER"])

E("FIG-HANNAS", "person", "Hannas", "Annas",
  "Schwiegervater des Kajafas und früherer Hohepriester, zu dem Jesus zuerst geführt wird ([[JHN.18.13]], [[JHN.18.24]]).",
  "De Schwigervater vom Kajafas und früener Hohepriester, zu dem de Jesus zerscht gfüert wird ([[JHN.18.13]], [[JHN.18.24]]).",
  [T("Amtskleid des Hohepriesters mit Brustschild, ohne Stirnplatte, grauer Überwurf", "design"), T("Stab", "design")],
  ("#6A6A7A", "#D9A441"),
  [FACE, NO_CARICATURE, "Nicht bedrohlich oder dämonisch darstellen; neutral nach Amt"],
  era="nt", find=[(r"Hannas", None)], distinct=["FIG-KAJAFAS", "FIG-ROLLE-HOHEPRIESTER"])

E("FIG-MALCHUS", "person", "Malchus", "Malchus",
  "Knecht des Hohepriesters, dem Petrus bei der Festnahme Jesu das rechte Ohr abhaut ([[JHN.18.10]]).",
  "De Chnächt vom Hohepriester, wo de Petrus bi de Feschtnahm vom Jesus s rächt Ohr abghaue hät ([[JHN.18.10]]).",
  [T("Dienergewand des Hohepriesterhauses", "design"),
   T("Rechtes Ohr verletzt: Ohr mit Verband und kurzes Schwert als Zeichen", "text", "JHN.18.10", "Gewalt nur angedeutet, keine Wunde")],
  ("#B8A98A", "#4A5A7A"),
  [FACE, "Seine Verletzung nicht mit dem Zeichen «hören» (FIG-ZEICHEN-HOEREN) verwechselbar; keine Blutdarstellung"],
  era="nt", find=[(r"Malchus", None)], distinct=["FIG-ZEICHEN-HOEREN", "FIG-ROLLE-DIENER"])

E("FIG-PILATUS", "person", "Pontius Pilatus", "Pontius Pilate",
  "Römischer Statthalter, der Jesus verhört und zur Kreuzigung übergibt ([[JHN.18.28-JHN.19.16]], [[MRK.15.1-MRK.15.15]]).",
  "De römisch Statthalter, wo de Jesus verhört und zur Chrüüzigung übergit ([[JHN.18.28-JHN.19.16]], [[MRK.15.1-MRK.15.15]]).",
  [T("Toga mit Purpursaum", "design"), T("Richterstuhl, gezeichnet als römischer Amtsstuhl mit gekreuzten Beinen auf einem Podest", "text", "JHN.19.13"),
   T("Ergrautes Haar (älter, Amtsautorität)", "design")],
  ("#F2E6CC", "#6A2E5E"),
  [FACE, "Die Händewaschung ([[MAT.27.24]]) nur in Matthäus-Szenen"],
  era="nt", find=[(r"Pilatus", None)], distinct=["FIG-ROLLE-SOLDAT", "FIG-HERODES-ANTIPAS"])

E("FIG-BARABBAS", "person", "Barabbas", "Barabbas",
  "Gefangener, der bei einem Aufstand gemordet hatte und an Jesu Stelle freigelassen wird ([[MRK.15.7]], [[MRK.15.15]], [[JHN.18.40]]).",
  "En Gfangne, wo bi me Ufstand gmordet hät und anstatt vom Jesus freiglaa wird ([[MRK.15.7]], [[MRK.15.15]], [[JHN.18.40]]).",
  [T("Gefesselte Hände", "text", "MRK.15.7"), T("Dunkles, einfaches Gewand", "design")],
  ("#7A6A5A", "#3B3226"),
  [FACE, NO_CARICATURE],
  era="nt", find=[(r"Barabbas", None)])

E("FIG-HERODES-ANTIPAS", "person", "Herodes (Antipas)", "Herod (Antipas)",
  "Landesherr von Galiläa, bei Markus «König» genannt, der Johannes den Täufer enthaupten lässt ([[MRK.6.14-MRK.6.29]]).",
  "De Landesherr vo Galiläa, bim Markus «König» gnännt, wo de Johannes de Täufer lat la chöpfe ([[MRK.6.14-MRK.6.29]]).",
  [T("Goldener Reif als Diadem", "text", "MRK.6.14", "Der Text nennt ihn «König»; historisch war er Tetrarch."),
   T("Violettes Gewand mit dunkelviolettem Mantel und Goldsaum", "design")],
  ("#6A2E5E", "#D9A441"),
  [FACE, NO_CARICATURE, "Nicht mit Herodes dem Grossen aus [[MAT.2.1]] verwechseln"],
  era="nt", find=[(r"Herodes", None)], distinct=["FIG-ROLLE-KOENIG", "FIG-PILATUS"])

E("FIG-HERODIAS", "person", "Herodias", "Herodias",
  "Frau des Herodes, zuvor Frau seines Bruders Philippus, die den Tod des Johannes betreibt ([[MRK.6.17-MRK.6.24]]).",
  "D Frau vom Herodes, vorher d Frau vo sim Brüeder Philippus, wo de Tod vom Johannes betriibt ([[MRK.6.17-MRK.6.24]]).",
  [T("Pflaumenfarbenes Gewand mit Goldschmuck: Stirnreif, Ohrgehänge, Halskette", "design")],
  ("#7A3E6A", "#D9A441"),
  [FACE, NO_CARICATURE, "Nicht dämonisieren oder sexualisieren"],
  era="nt", find=[(r"Herodias", None)], distinct=["FIG-TOCHTER-HERODIAS"])

E("FIG-TOCHTER-HERODIAS", "person", "Tochter der Herodias", "Daughter of Herodias",
  "Ein Mädchen, das beim Mahl des Herodes tanzt und auf Rat ihrer Mutter den Kopf des Johannes erbittet ([[MRK.6.22-MRK.6.28]]).",
  "Es Meitli, wo bim Mahl vom Herodes tanzet und uf de Raat vo sinere Mueter de Chopf vom Johannes verlangt ([[MRK.6.22-MRK.6.28]]).",
  [T("Mädchen, das tanzt", "text", "MRK.6.22"), T("Handtrommel mit Schellen und Bändern als Zeichen des Tanzes", "design"), T("Rosa Gewand", "design")],
  ("#D4537E", "#F2E6CC"),
  [FACE, "Der Text nennt sie «Mädchen»: nie sexualisiert darstellen",
   "Den Namen Salome hat sie erst aus späterer Überlieferung; nicht mit Salome aus [[MRK.15.40]] verwechseln"],
  era="nt", find=[(r"Tochter der Herodias|Mädchen", ["MRK.6.22-MRK.6.28"])], distinct=["FIG-SALOME", "FIG-HERODIAS"])

E("FIG-SIMON-KYRENE", "person", "Simon von Kyrene", "Simon of Cyrene",
  "Ein Mann vom Feld, Vater von Alexander und Rufus, den die Soldaten zwingen, das Kreuz Jesu zu tragen ([[MRK.15.21]]).",
  "En Maa vom Fäld, de Vater vom Alexander und vom Rufus, wo d Soldate zwinged, s Chrüüz vom Jesus z träge ([[MRK.15.21]]).",
  [T("Kreuzbalken auf der Schulter", "text", "MRK.15.21", "Auf der Brust las er sich als «Balken im Auge» (Blindtest Runde 3)"), T("Feldarbeitergewand", "design")],
  ("#8A7A50", "#5B4630"),
  [FACE, NAMESAKE, "Nicht mit Simon Petrus oder Simon dem Kananäer verwechseln"],
  era="nt", find=[(r"Kyrene", None)], distinct=["FIG-PETRUS", "FIG-SIMON-KANANAEUS"])

E("FIG-JAIRUS", "person", "Jairus", "Jairus",
  "Synagogenvorsteher, der Jesus für seine sterbende Tochter um Hilfe bittet ([[MRK.5.22-MRK.5.43]]).",
  "En Synagogevorschteher, wo de Jesus für sini Tochter, wo am Sterbe isch, um Hilf bittet ([[MRK.5.22-MRK.5.43]]).",
  [T("Gebetsmantel mit Quasten, über den Kopf gelegt; eine Hand am Gebetsmantel", "design"), T("Voller dunkelbrauner Bart", "design"),
   T("Kniend bittend (in seiner ersten Szene)", "text", "MRK.5.22")],
  ("#4F6B7A", "#E7DCC4"),
  [FACE, NO_CARICATURE],
  era="nt", find=[(r"Jairus|Synagogenvorsteher", ["MRK.5"])])

E("FIG-BARTIMAEUS", "person", "Bartimäus", "Bartimaeus",
  "Blinder Bettler bei Jericho, Sohn des Timäus, der nach Jesus ruft und geheilt wird ([[MRK.10.46-MRK.10.52]]).",
  "En blinde Bättler bi Jericho, de Sohn vom Timäus, wo em Jesus rüeft und gheilt wird ([[MRK.10.46-MRK.10.52]]).",
  [T("Blind: durchgestrichenes Auge als Zeichen", "text", "MRK.10.46"),
   T("Geflickter Bettlermantel, der ihm von der Schulter rutscht (er wirft ihn ab)", "text", "MRK.10.50", "Unterscheidet ihn von FIG-ROLLE-BLINDER und FIG-ROLLE-ZWEITER-BLINDER"),
   T("Graues Haar, kurzer grauer Bart", "design")],
  ("#8A7A60", "#5B4630"),
  [FACE, "Blindheit nicht durch verbundene Augen oder entstellte Züge, sondern durch das Zeichen «blind» und die Haltung zeigen"],
  era="nt", find=[(r"Bartimäus|Blinde|blind", ["MRK.10.46-MRK.10.52"])], distinct=["FIG-ROLLE-KRANKER", "FIG-ROLLE-BLINDER", "FIG-ROLLE-ZWEITER-BLINDER"])

E("FIG-GERASENER", "person", "Der Mann mit dem Namen Legion", "The man called Legion",
  "Ein Mann in den Grabhöhlen bei Gerasa mit einem unreinen Geist, der sich «Legion» nennt und von Jesus befreit wird ([[MRK.5.1-MRK.5.20]]).",
  "En Maa i de Grabhöhline bi Gerasa mit eme unsuubere Geischt, wo sich «Legion» nännt und vom Jesus befreit wird ([[MRK.5.1-MRK.5.20]]).",
  [T("Gesprengte Kette", "text", "MRK.5.4"), T("Offenes Haar, voller Bart", "design"),
   T("Nach der Heilung bekleidet und sitzend", "text", "MRK.5.15")],
  ("#8A8070", "#5B4630"),
  [FACE, "Nicht reisserisch oder als Monster; Würde des Menschen wahren", "Der unreine Geist nicht als Figur, höchstens als dunkler Schatten"],
  era="nt", find=[(r"Legion|unreinen Geist|Besessene", ["MRK.5.1-MRK.5.20"])], distinct=["FIG-SATAN", "FIG-ROLLE-KRANKER"])

E("FIG-MOSE", "person", "Mose", "Moses",
  "Der Prophet, durch den das Gesetz gegeben wurde; erscheint mit Elija bei der Verklärung Jesu ([[JHN.1.17]], [[MRK.9.4]]).",
  "De Prophet, dur de s Gsetz ggee worde isch; er erschiint mit em Elija bi de Verklärig vom Jesus ([[JHN.1.17]], [[MRK.9.4]]).",
  [T("Zwei Gesetzestafeln (erst ab dem Sinai)", "tradition", note="Nach [[EXO.34.29]]; Exodus noch nicht übersetzt. Blindtest 2026-10-14: Tafeln beim Meerdurchzug waren zeitlich falsch."), T("Weisser Bart", "tradition"), T("Stab in der Hand", "text", "EXO.4.2")],
  ("#7A5A34", "#E7DCC4"),
  [FACE, "Keine Hörner (Übersetzungstradition der Vulgata zu [[EXO.34.29]]), weil sie missverständlich und antijüdisch gebraucht wurden",
   "Lichtstrahlen um den Kopf statt Hörner nur, wenn ein Nimbus-Konflikt mit Jesus ausgeschlossen ist"],
  era="exodus", find=[(r"\bMose\b", None)], distinct=["FIG-ELIJA", "FIG-JESUS"])

E("FIG-ELIJA", "person", "Elija", "Elijah",
  "Der Prophet, dessen Wiederkunft erwartet wurde; erscheint mit Mose bei der Verklärung Jesu ([[JHN.1.21]], [[MRK.9.4]]).",
  "De Prophet, wo mer erwartet hät, dass er wider chunnt; er erschiint mit em Mose bi de Verklärig vom Jesus ([[JHN.1.21]], [[MRK.9.4]]).",
  [T("Fellmantel", "tradition", note="Nach [[2KI.1.8]] und [[2KI.2.13]]; Könige noch nicht übersetzt."), T("Feuerwagen als Hinweis", "tradition", note="Nach [[2KI.2.11]]; vorher Feuerrad (Blindtest Runde 2 vom 2026-10-23: «brennendes Rad»)")],
  ("#5B4630", "#D97A2A"),
  [FACE, "Nicht mit Johannes dem Täufer verwechseln: Elija trägt Fellmantel ohne Kreuzstab"],
  era="kingdom", find=[(r"Elija", None)], distinct=["FIG-JOHANNES-TAEUFER", "FIG-MOSE"])

E("FIG-SATAN", "person", "Satan (Teufel)", "Satan (devil)",
  "Der Widersacher, der Jesus in der Wüste versucht und in Judas fährt ([[MRK.1.13]], [[JHN.13.27]]).",
  "De Widersacher, wo de Jesus i de Wüeschti versuecht und in de Judas ine fahrt ([[MRK.1.13]], [[JHN.13.27]]).",
  [T("Dunkler, rauchiger Schatten ohne feste Gestalt, schwebend, mit zwei hellen Augen", "design", note="Keine Mantel- oder Sackform (Blindtest Runde 2 vom 2026-10-23), keine Fratze, keine Hörner.")],
  ("#3B3226", "#6A4A6A"),
  ["Nie als Mensch, nie mit Gesicht", "Keine Hörner, Hakennase oder andere Züge, die je gegen Juden oder andere Gruppen gebraucht wurden",
   "Nie einer realen Volks- oder Religionsgruppe ähnlich"],
  era="any", find=[(r"Satan|Teufel", None)], distinct=["FIG-GERASENER"])

# --- Rut
E("FIG-RUT", "person", "Rut", "Ruth",
  "Moabiterin, Schwiegertochter Noomis, die mit ihr nach Betlehem geht und Boas heiratet ([[RUT.1.16]], [[RUT.4.13]]).",
  "Moabiterin, d Schwigertochter vo de Noomi, wo mit ere uf Betlehem gaat und de Boas hüraatet ([[RUT.1.16]], [[RUT.4.13]]).",
  [T("Ährengarbe im Arm", "text", "RUT.2.2", "Sie liest Ähren auf; die Garbe als Erkennungszeichen ist Bildtradition."),
   T("Olivgrünes Gewand mit gerstengelbem Kopftuch", "design")],
  ("#7A8B4A", "#E8B84A"),
  [FACE, NO_CARICATURE, "Nicht mit Orpa verwechseln: Rut wendet sich Noomi zu, Orpa geht zurück"],
  era="judges", find=[(r"\bRut\b|Moabiterin", ["RUT"])], distinct=["FIG-ORPA", "FIG-NOOMI"])

E("FIG-NOOMI", "person", "Noomi", "Naomi",
  "Frau Elimelechs aus Betlehem, die in Moab Mann und Söhne verliert und mit Rut zurückkehrt ([[RUT.1.3-RUT.1.5]], [[RUT.1.20]]).",
  "D Frau vom Elimelech vo Betlehem, wo z Moab de Maa und d Söhn verlüürt und mit de Rut zrugg chunnt ([[RUT.1.3-RUT.1.5]], [[RUT.1.20]]).",
  [T("Dunkles Witwenkopftuch", "design"),
   T("Ältere Frau mit grauem Haar", "design", note="Kein Kind als Zeichen: In den Bildern vor [[RUT.4.16]] wirkte es wie ein eigenes Kind (Bildtest ohne Legende 2026-10-23); Obed nur dort, wo der Text ihn nennt")],
  ("#2E2E38", "#C9BFAA"),
  [FACE, "Ältere Frau, aber nicht gebrechlich"],
  era="judges", find=[(r"Noomi", None)], distinct=["FIG-RUT", "FIG-ROLLE-WITWE"])

E("FIG-ORPA", "person", "Orpa", "Orpah",
  "Moabiterin, Schwiegertochter Noomis, die auf deren Rat zu ihrem Volk zurückkehrt ([[RUT.1.4]], [[RUT.1.14]]).",
  "Moabiterin, d Schwigertochter vo de Noomi, wo uf iren Raat hii zu irem Volk zruggaat ([[RUT.1.4]], [[RUT.1.14]]).",
  [T("Altrosa Gewand", "design"), T("Reisebündel: sie kehrt zu ihrem Volk zurück", "text", "RUT.1.14-RUT.1.15")],
  ("#C08A8A", "#E2CDA8"),
  [FACE, "Nicht abwertend darstellen; ihr Rückweg folgt Noomis Rat"],
  era="judges", find=[(r"Orpa", None)], distinct=["FIG-RUT"])

E("FIG-BOAS", "person", "Boas", "Boaz",
  "Wohlhabender Verwandter Elimelechs in Betlehem, der als Löser Rut heiratet ([[RUT.2.1]], [[RUT.4.9-RUT.4.13]]).",
  "En vermögende Verwandte vom Elimelech z Betlehem, wo als Löser d Rut hüraatet ([[RUT.2.1]], [[RUT.4.9-RUT.4.13]]).",
  [T("Worfelgabel und Gerste (er worfelt Gerste auf der Tenne)", "text", "RUT.3.2"),
   T("Petrolfarbener Mantel über hellem Gewand mit Goldsaum (wohlhabend)", "design", note="Nach [[RUT.2.1]]")],
  ("#2F5F6F", "#E8B84A"),
  [FACE, "Nicht mit dem ungenannten näheren Löser verwechseln"],
  era="judges", find=[(r"Boas", None)], distinct=["FIG-LOESER"])

E("FIG-LOESER", "person", "Der nähere Löser", "The nearer redeemer",
  "Ungenannter, näherer Verwandter Elimelechs, der auf das Lösungsrecht verzichtet und dazu seinen Schuh auszieht ([[RUT.3.12]], [[RUT.4.1-RUT.4.8]]).",
  "En ungnännte, nöcher Verwandte vom Elimelech, wo uf s Löserächt verzichtet und derzue sin Schue uszieht ([[RUT.3.12]], [[RUT.4.1-RUT.4.8]]).",
  [T("Ausgezogener Schuh (Sandale) von der Seite", "text", "RUT.4.8", "Von oben gezeichnet las sich die Sandale als Brot (Blindtest Runde 3)"), T("Braungraues Gewand", "design")],
  ("#8A7A6A", "#5B4630"),
  [FACE, "Ohne Namen; nicht abwertend darstellen"],
  era="judges", find=[(r".", ["RUT.3.12-RUT.3.13", "RUT.4.1-RUT.4.8"])], distinct=["FIG-BOAS"])

E("FIG-ELIMELECH", "person", "Elimelech", "Elimelech",
  "Mann Noomis aus Betlehem, der wegen einer Hungersnot nach Moab zieht und dort stirbt ([[RUT.1.1-RUT.1.3]]).",
  "De Maa vo de Noomi vo Betlehem, wo wäge ere Hungersnot uf Moab zieht und det stirbt ([[RUT.1.1-RUT.1.3]]).",
  [T("Stab mit grossem Reisebündel", "design", note="Wegzug nach Moab ([[RUT.1.1]])")],
  ("#6A5A4A", "#C9BFAA"), [FACE],
  era="judges", find=[(r"Elimelech", None)], distinct=["FIG-MACHLON", "FIG-KILJON"])

E("FIG-MACHLON", "person", "Machlon", "Mahlon",
  "Sohn Elimelechs und Noomis, Mann der Rut, stirbt in Moab ([[RUT.1.2-RUT.1.5]], [[RUT.4.10]]).",
  "De Sohn vom Elimelech und vo de Noomi, de Maa vo de Rut; er stirbt z Moab ([[RUT.1.2-RUT.1.5]], [[RUT.4.10]]).",
  [T("Gewand mit olivgrünem Band (wie Rut)", "design"), T("Jung, ohne Bart", "design"), T("Feld (Erbteil), auf dem sein Name erhalten bleibt", "text", "RUT.4.10")],
  ("#7A6A5A", "#7A8B4A"), [FACE],
  era="judges", find=[(r"Machlon", None)], distinct=["FIG-KILJON"])

E("FIG-KILJON", "person", "Kiljon", "Chilion",
  "Sohn Elimelechs und Noomis, Mann der Orpa, stirbt in Moab ([[RUT.1.2-RUT.1.5]]).",
  "De Sohn vom Elimelech und vo de Noomi, de Maa vo de Orpa; er stirbt z Moab ([[RUT.1.2-RUT.1.5]]).",
  [T("Gewand mit altrosa Band (wie Orpa)", "design"), T("Jung, ohne Bart, lockiges Haar", "design")],
  ("#7A6A5A", "#8E6A7A"), [FACE],
  era="judges", find=[(r"Kiljon", None)], distinct=["FIG-MACHLON"])

E("FIG-OBED", "person", "Obed", "Obed",
  "Sohn von Rut und Boas, Grossvater Davids ([[RUT.4.17]]).",
  "De Sohn vo de Rut und vom Boas, de Grossvater vom David ([[RUT.4.17]]).",
  [T("Säugling in hellem Tuch", "text", "RUT.4.16")],
  ("#F2E6CC", "#E8B84A"), [FACE],
  era="judges", find=[(r"Obed", None), (r"Kind|Sohn", ["RUT.4.13-RUT.4.16"])])

# --- Jona, Obadja
E("FIG-JONA", "person", "Jona", "Jonah",
  "Prophet, Sohn Amittais, der vor dem Auftrag nach Ninive flieht, vom grossen Fisch verschlungen wird und dann doch predigt ([[JON.1.1-JON.1.3]], [[JON.1.17]], [[JON.3.4]]).",
  "De Prophet, de Sohn vom Amittai, wo vor em Uftrag uf Ninive flieht, vom grosse Fisch verschluckt wird und dänn glich prediget ([[JON.1.1-JON.1.3]], [[JON.1.17]], [[JON.3.4]]).",
  [T("Grosser Fisch hinter ihm (als Hinweis)", "text", "JON.1.17", "Nicht auf der Brust: so las er sich als Fischer (Blindtest Runde 2 vom 2026-10-23)"),
   T("Meerblaues Gewand", "design")],
  ("#4A6E8A", "#6FB2E6"),
  [FACE, "Den Fisch nicht als Wal mit Fontäne; der Text sagt «grosser Fisch»"],
  era="kingdom", find=[(r"\bJona\b", None)], distinct=["FIG-OBJ-GROSSER-FISCH", "FIG-ROLLE-KAPITAEN"])

E("FIG-OBADJA", "person", "Obadja", "Obadiah",
  "Prophet, dessen Schauung über Edom das Buch Obadja enthält ([[OBA.1.1]]).",
  "De Prophet, wo sini Schauig über Edom im Buech Obadja staat ([[OBA.1.1]]).",
  [T("Schriftrolle mit Siegel", "design"), T("Violettgraues Prophetengewand", "design"), T("Rauer Prophetenmantel", "tradition")],
  ("#6A5A7A", "#E7DCC4"),
  [FACE, "Nicht mit Obadja, dem Hofmeister Ahabs aus [[1KI.18.3]], gleichsetzen (Gleichsetzung nur in jüdischer Tradition)"],
  era="exile", find=[(r"Obadja", None)])

# --- Briefe
E("FIG-PAULUS", "person", "Paulus", "Paul",
  "Apostel und Verfasser der Briefe an die Philipper und an Titus, im Philipperbrief in Fesseln ([[PHP.1.1]], [[PHP.1.13]], [[TIT.1.1]]).",
  "Apostel und Verfasser vo de Brief a d Philipper und an Titus, im Philipperbrief gfesslet ([[PHP.1.1]], [[PHP.1.13]], [[TIT.1.1]]).",
  [T("Schwert an der Seite", "tradition"), T("Brief in der Hand", "text", "PHP.1.1", "Er schreibt Briefe an Gemeinden"),
   T("Kette (im Philipperbrief)", "text", "PHP.1.13"), T("Rotbrauner Mantel", "design")],
  ("#6A3F2F", "#A79A80"),
  [FACE, "Schwert gesenkt oder in der Scheide, nie als Angriffswaffe"],
  era="nt", find=[(r"\b(Paulus|ich|mich|mir)\b", ["PHP", "TIT"])], distinct=["FIG-BARTHOLOMAEUS", "FIG-DER-AELTESTE"])

E("FIG-TIMOTHEUS", "person", "Timotheus", "Timothy",
  "Mitarbeiter und Mitabsender des Paulus, den er nach Philippi senden will ([[PHP.1.1]], [[PHP.2.19-PHP.2.22]]).",
  "De Mitarbeiter und Mitabsänder vom Paulus, wo er uf Philippi wott schicke ([[PHP.1.1]], [[PHP.2.19-PHP.2.22]]).",
  [T("Jung, mit Reisestab und Brief", "design"), T("Hellblaues Gewand", "design")],
  ("#5A7A9A", "#E2CDA8"), [FACE],
  era="nt", find=[(r"Timotheus", None)], distinct=["FIG-EPAPHRODITUS", "FIG-TITUS"])

E("FIG-EPAPHRODITUS", "person", "Epaphroditus", "Epaphroditus",
  "Abgesandter der Gemeinde Philippi, der Paulus die Gaben bringt, schwer krank wird und den Paulus zurückschickt ([[PHP.2.25-PHP.2.30]], [[PHP.4.18]]).",
  "De Gsandt vo de Gmeind Philippi, wo em Paulus d Gaabe bringt, schwer chrank wird und wo de Paulus zruggschickt ([[PHP.2.25-PHP.2.30]], [[PHP.4.18]]).",
  [T("Korb mit Gaben (Brot, Krug, Tuch mit Band), keine Münzen", "text", "PHP.4.18", "Der Gabenbeutel las sich als Geldbeutel (Judas, Zöllner; Blindtest Runde 3)"), T("Grünliches Reisegewand", "design")],
  ("#7A8A5A", "#E2CDA8"), [FACE],
  era="nt", find=[(r"Epaphroditus", None)], distinct=["FIG-TIMOTHEUS", "FIG-ROLLE-BOTE", "FIG-JUDAS-ISKARIOT"])

E("FIG-EUODIA", "person", "Euodia", "Euodia",
  "Mitarbeiterin des Paulus in Philippi, die er bittet, mit Syntyche eines Sinnes zu sein ([[PHP.4.2-PHP.4.3]]).",
  "Mitarbeiterin vom Paulus z Philippi, wo er bittet, mit de Syntyche einig z sii ([[PHP.4.2-PHP.4.3]]).",
  [T("Altrosa Gewand", "design"), T("Kopftuch in hellem Altrosa", "design")],
  ("#A8687A", "#F2E6CC"),
  [FACE, "Nicht als zankende Frauen karikieren; Paulus nennt beide Mitkämpferinnen ([[PHP.4.3]])"],
  era="nt", find=[(r"Euodia", None)], distinct=["FIG-SYNTYCHE"])

E("FIG-SYNTYCHE", "person", "Syntyche", "Syntyche",
  "Mitarbeiterin des Paulus in Philippi, die er bittet, mit Euodia eines Sinnes zu sein ([[PHP.4.2-PHP.4.3]]).",
  "Mitarbeiterin vom Paulus z Philippi, wo er bittet, mit de Euodia einig z sii ([[PHP.4.2-PHP.4.3]]).",
  [T("Hellblaugraues Gewand", "design"), T("Handschlag: Paulus bittet sie und Euodia, eines Sinnes zu sein", "text", "PHP.4.2")],
  ("#6A8AA8", "#F2E6CC"),
  [FACE, "Nicht als zankende Frauen karikieren; Paulus nennt beide Mitkämpferinnen ([[PHP.4.3]])"],
  era="nt", find=[(r"Syntyche", None)], distinct=["FIG-EUODIA"])

E("FIG-TITUS", "person", "Titus", "Titus",
  "Mitarbeiter des Paulus, den er auf Kreta zurückgelassen hat, um Älteste einzusetzen ([[TIT.1.4-TIT.1.5]]).",
  "De Mitarbeiter vom Paulus, wo er uf Kreta zrugglaa hät, dass er det Ältischti iisetzt ([[TIT.1.4-TIT.1.5]]).",
  [T("Insel mit Städten (Kreta)", "text", "TIT.1.5", "Er soll dort in jeder Stadt Älteste einsetzen; den Brief trägt Paulus"), T("Moosgrünes Gewand", "design"),
   T("Lockiges Haar", "design", note="Er war Grieche ([[GAL.2.3]]); keine typisierten Merkmale, nur zur Unterscheidung")],
  ("#5A6A3A", "#E2CDA8"), [FACE],
  era="nt", find=[(r"Titus", None)], distinct=["FIG-TIMOTHEUS"])

E("FIG-DER-AELTESTE", "person", "Der Älteste (Briefschreiber)", "The Elder (letter writer)",
  "Der namenlose Verfasser des 2. und 3. Johannesbriefs, der sich «der Älteste» nennt ([[2JN.1.1]], [[3JN.1.1]]).",
  "De namelos Verfasser vom 2. und 3. Johannesbrief, wo sich «de Ältischt» nännt ([[2JN.1.1]], [[3JN.1.1]]).",
  [T("Brief mit Schreibfeder", "text", "3JN.1.13"), T("Graues Gewand, weisser Überwurf", "design")],
  ("#6A6A6A", "#E7DCC4"),
  [FACE, "Die Gleichsetzung mit dem Apostel Johannes ist Tradition; im Bild nur als Deutung",
   "Nicht mit der Rolle FIG-ROLLE-AELTESTER (Ältestenamt) verwechseln"],
  era="nt", find=[(r"Älteste", ["2JN", "3JN"])], distinct=["FIG-JOHANNES-ZEBEDAEUS", "FIG-ROLLE-AELTESTER"])

E("FIG-AUSERWAEHLTE-HERRIN", "person", "Die auserwählte Herrin", "The elect lady",
  "Empfängerin des 2. Johannesbriefs mit ihren Kindern ([[2JN.1.1]], [[2JN.1.5]]); ob eine Frau oder eine Gemeinde gemeint ist, ist umstritten.",
  "D Empfängerin vom 2. Johannesbrief mit irne Chind ([[2JN.1.1]], [[2JN.1.5]]); öb e Frau oder e Gmeind gmeint isch, isch umstritte.",
  [T("Brief und zwei grössere Kinder als Zeichen (kein Kleinkind)", "text", "2JN.1.1", "Deutung als Person; als Gemeinde-Bild nur mit Hinweis. Ein Kleinkind las sich als Maria mit Kind (Blindtest Runde 3).")],
  ("#6A4A7A", "#F2E6CC"),
  [FACE, "Die Deutung (Person oder Gemeinde) im Bild als Deutung kennzeichnen"],
  era="nt", find=[(r"Herrin", ["2JN"])])

E("FIG-GAIUS", "person", "Gaius", "Gaius",
  "Empfänger des 3. Johannesbriefs, gelobt für seine Gastfreundschaft gegenüber durchreisenden Geschwistern ([[3JN.1.1]], [[3JN.1.5-3JN.1.8]]).",
  "De Empfänger vom 3. Johannesbrief, globt für sini Gaschtfründschaft gägenüber Gschwüschterte, wo dureräised ([[3JN.1.1]], [[3JN.1.5-3JN.1.8]]).",
  [T("Offene Tür, aus der Licht fällt (Gastfreundschaft)", "text", "3JN.1.5-3JN.1.8"), T("Warmes Braun", "design")],
  ("#8A6A4A", "#F6EBD9"), [FACE],
  era="nt", find=[(r"Gaius", None)], distinct=["FIG-DIOTREPHES"])

E("FIG-DIOTREPHES", "person", "Diotrephes", "Diotrephes",
  "Gemeindeglied, das der Erste sein will und die Boten des Ältesten abweist ([[3JN.1.9-3JN.1.10]]).",
  "Es Gmeindsmitglid, wo de Erscht wott sii und d Bote vom Ältischte abwiist ([[3JN.1.9-3JN.1.10]]).",
  [T("Geschlossene, verriegelte Tür und abweisende Hand", "text", "3JN.1.10"), T("Graubraunes Gewand", "design")],
  ("#6A5A5A", "#C9BFAA"),
  [FACE, NO_CARICATURE, "Nicht dämonisieren; das Bild zeigt die Handlung, keine Wertung des Menschen"],
  era="nt", find=[(r"Diotrephes", None)], distinct=["FIG-GAIUS"])

E("FIG-DEMETRIUS", "person", "Demetrius", "Demetrius",
  "Ein Mann, dem von allen ein gutes Zeugnis ausgestellt wird ([[3JN.1.12]]).",
  "En Maa, wo vo allne es guets Zügnis überchunnt ([[3JN.1.12]]).",
  [T("Empfehlungsbrief in der Hand", "design"), T("Grüngraues Gewand", "design")],
  ("#4A7A6A", "#E7DCC4"), [FACE],
  era="nt", find=[(r"Demetrius", None)])

# ---------------------------------------------------------------------------------------------------------------
# 3. Rollen und Gruppen
# ---------------------------------------------------------------------------------------------------------------
E("FIG-ROLLE-DIENER", "role", "Diener", "Servant",
  "Jemand, der anderen aufwartet, etwa die Diener bei der Hochzeit zu Kana ([[JHN.2.5]], [[JHN.2.9]]).",
  "Öpper, wo anderne uufwartet, öppe d Diener a de Hochziit z Kana ([[JHN.2.5]], [[JHN.2.9]]).",
  [T("Schürze", "design"), T("Tablett mit Krug und Bechern über der Schürze", "design", note="Diener tragen auf ([[JHN.2.8]])"), T("Gewand in Sandbeige", "design")],
  ("#C9B48E", "#F6EBD9"),
  [FACE, "Die Tempeldiener (Wache) in Johannes 7 und 18 sind eine eigene Rolle (FIG-ROLLE-TEMPELWACHE)"],
  era="any", find=[(r"\bDiener", ["JHN.2", "JHN.12.26", "MRK.9.35", "MRK.10.43"])],
  distinct=["FIG-ROLLE-TEMPELWACHE", "FIG-MARTA"])

E("FIG-ROLLE-TEMPELWACHE", "role", "Tempeldiener (Wache)", "Temple officer (guard)",
  "Diener der Hohepriester und Pharisäer, die Jesus festnehmen sollen ([[JHN.7.32]], [[JHN.18.3]]).",
  "Diener vo de Hohepriester und Pharisäer, wo de Jesus söllid feschtneh ([[JHN.7.32]], [[JHN.18.3]]).",
  [T("Laterne bzw. Fackel", "text", "JHN.18.3"), T("Stock, Gürtel, dunkelblaugraues Gewand", "design")],
  ("#4A5A6A", "#C9BFAA"),
  [FACE, NO_CARICATURE, "Keine römische Rüstung (sonst Verwechslung mit FIG-ROLLE-SOLDAT)"],
  era="nt", find=[(r"\bDiener", ["JHN.7", "JHN.18", "JHN.19.6"])], distinct=["FIG-ROLLE-SOLDAT", "FIG-ROLLE-DIENER"])

E("FIG-ROLLE-GAST", "role", "Gast", "Guest",
  "Eingeladene bei einem Fest oder Mahl, etwa bei der Hochzeit zu Kana ([[JHN.2.2]]).",
  "Iiglade a me Fescht oder Mahl, öppe a de Hochziit z Kana ([[JHN.2.2]]).",
  [T("Helles Festgewand mit Goldsaum", "design"), T("Festbecher mit zwei Henkeln", "design")],
  ("#F2EAD6", "#D9A441"), [FACE],
  era="any", find=[(r"Gäste|Gast\b|eingeladen", None)], distinct=["FIG-GRUPPE-MENGE"])

E("FIG-ROLLE-BRAUT", "role", "Braut", "Bride",
  "Die Frau, die Hochzeit hält; bei Johannes nur im Bildwort genannt ([[JHN.3.29]]).",
  "D Frau, wo Hochziit hät; bim Johannes nu im Bildwort gnännt ([[JHN.3.29]]).",
  [T("Weisser Schleier, Blumenkranz", "design")],
  ("#FFFFFF", "#D4537E"),
  [FACE, "In Kana nennt der Text die Braut nicht; im Bild als Bildgestaltung kennzeichnen"],
  era="any", find=[(r"\bBraut\b", None)], distinct=["FIG-ROLLE-BRAEUTIGAM"])

E("FIG-ROLLE-BRAEUTIGAM", "role", "Bräutigam", "Bridegroom",
  "Der Mann, der Hochzeit hält; in Kana vom Speisemeister angesprochen ([[JHN.2.9-JHN.2.10]], [[MRK.2.19]]).",
  "De Maa, wo Hochziit hät; z Kana vom Spiismeischter aagredt ([[JHN.2.9-JHN.2.10]], [[MRK.2.19]]).",
  [T("Festgewand in Violett, Blütenkranz", "design")],
  ("#5A3E7A", "#D9A441"),
  [FACE, "Goldener Kranz ist kein Königsreif und kein Nimbus"],
  era="any", find=[(r"Bräutigam", None)], distinct=["FIG-ROLLE-KOENIG", "FIG-ROLLE-BRAUT"])

E("FIG-ROLLE-SPEISEMEISTER", "role", "Speisemeister", "Master of the feast",
  "Der Verantwortliche für das Festmahl, der den Wein kostet ([[JHN.2.8-JHN.2.10]]).",
  "De Verantwortlich für s Feschtmahl, wo de Wii versuecht ([[JHN.2.8-JHN.2.10]]).",
  [T("Grünes Gewand, Goldgürtel", "design"), T("Becher in der Hand", "design", note="Er kostet den Wein ([[JHN.2.9]])")],
  ("#4F7A4A", "#D9A441"), [FACE],
  era="nt", find=[(r"Speisemeister", None)], distinct=["FIG-ROLLE-DIENER"])

E("FIG-ROLLE-HAENDLER", "role", "Händler", "Trader",
  "Verkäufer und Geldwechsler im Tempelbereich ([[JHN.2.14]], [[MRK.11.15]]).",
  "Verchäufer und Gäldwächsler im Tämpelbereich ([[JHN.2.14]], [[MRK.11.15]]).",
  [T("Mann mit vollem Bart und Stirnband", "design", note="Ohne Kopftuch: damit wurde er als Frau gelesen (Blindtest Runde 2 vom 2026-10-23)"), T("Marktstand mit Sonnendach als Zeichen", "design", note="Kein Geldbeutel oder Geldsack (Regel unten)")],
  ("#C2884A", "#5B4630"),
  [FACE, NO_CARICATURE, "Keine antijüdischen Händler-Stereotype (Hakennase, gierige Haltung, Geldsack)"],
  era="nt", find=[(r"Verkäufer|Händler|Geldwechsler|verkauften|kauften", ["JHN.2", "MRK.11.15"])],
  distinct=["FIG-JUDAS-ISKARIOT", "FIG-LEVI"])

E("FIG-ROLLE-JUENGER", "role", "Jünger", "Disciple",
  "Menschen, die Jesus nachfolgen und von ihm lernen ([[JHN.1.37]], [[MRK.1.17-MRK.1.18]]).",
  "Mänsche, wo em Jesus nachefolged und vo im lärned ([[JHN.1.37]], [[MRK.1.17-MRK.1.18]]).",
  [T("Erdfarbenes Gewand mit Gürtel", "design"),
   T("Zwei Fussspuren: die goldene voraus (Jesus), die braune folgt ihr", "text", "MRK.1.17-MRK.1.18"),
   T("Wanderstab an der linken Schulter wie die Zwölf", "design", note="Nach [[MRK.6.8]]; gemeinsames Jüngermerkmal seit Runde 4")],
  ("#9C7A4C", "#5B4630"),
  [FACE, "Benannte Jünger tragen zusätzlich ihr eigenes Zeichen", "Jüngerinnen gleich würdig darstellen"],
  era="nt", find=[(r"Jünger", None)], distinct=["FIG-GRUPPE-ZWOELF"])

E("FIG-GRUPPE-ZWOELF", "group", "Die Zwölf", "The Twelve",
  "Der engere Kreis von zwölf Jüngern, den Jesus einsetzt ([[MRK.3.14-MRK.3.19]], [[JHN.6.67]]).",
  "De ängeri Chreis vo zwölf Jünger, wo de Jesus iisetzt ([[MRK.3.14-MRK.3.19]], [[JHN.6.67]]).",
  [T("Drei Jünger stehen für alle zwölf; vorn die Zahl 12", "text", "MRK.3.14", "Zahl im Bild statt Wanderstäben, die im Blindtest Runde 3 als Hirten gelesen wurden (Worte und Zahlen im Bild erlaubt, Entscheid 2026-10-23)"),
   T("Nur Männer, alle mit gleicher Gewandfarbe und Gürtel", "design")],
  ("#9C7A4C", "#5B4630"),
  [FACE, "Wenn einzeln erkennbar, nur mit den Zeichen der benannten Jünger"],
  era="nt", find=[(r"\b(die|den|der|von den) Zwölf\b", None)], distinct=["FIG-ROLLE-JUENGER"])

E("FIG-GRUPPE-MENGE", "group", "Menge", "Crowd",
  "Viele Menschen, die Jesus folgen, ihm zuhören oder über ihn streiten ([[MRK.2.4]], [[JHN.7.12]]).",
  "Vill Mänsche, wo em Jesus nachegönd, im zuelosed oder über in strited ([[MRK.2.4]], [[JHN.7.12]]).",
  [T("Gestaffelte Figuren in gedeckten Farben, dahinter weitere nur als Umriss; Männer und Frauen gemischt, ohne Kind vorn (sonst als Familie gelesen)", "design")],
  ("#A79A80", "#C9BFAA"),
  [FACE, NO_CARICATURE, "Die Menge nie als «die Juden» einfärben oder vereinheitlichen"],
  era="any", find=[(r"\bMenge\b", None)], distinct=["FIG-ROLLE-GAST"])

E("FIG-ROLLE-HOHEPRIESTER", "role", "Hohepriester", "High priest",
  "Die führenden Priester am Tempel in Jerusalem ([[MRK.14.53]], [[JHN.18.13]]).",
  "Di füerende Priester am Tämpel z Jerusalem ([[MRK.14.53]], [[JHN.18.13]]).",
  [T("Kopfbund, Brustschild mit zwölf Steinen", "tradition", note="Nach der Beschreibung in [[EXO.28.4]]; wie die Kleidung zur Zeit Jesu aussah, ist nicht im Einzelnen belegt.")],
  ("#4A5A7A", "#D9A441"),
  [FACE, NO_CARICATURE, "Neutral nach Amt: nicht dunkel, bedrohlich oder dämonisch; keine antijüdischen Bildmuster"],
  era="nt", find=[(r"Hohe(n)?priester", None)], distinct=["FIG-ROLLE-PRIESTER", "FIG-KAJAFAS", "FIG-HANNAS"])

E("FIG-ROLLE-PRIESTER", "role", "Priester", "Priest",
  "Diensthabende Priester am Tempel ([[JHN.1.19]], [[MRK.1.44]]).",
  "Priester, wo am Tämpel Dienscht händ ([[JHN.1.19]], [[MRK.1.44]]).",
  [T("Weisses Leinengewand, Kopfbund", "tradition", note="Nach [[EXO.28.40]].")],
  ("#F6EBD9", "#4A5A7A"),
  [FACE, NO_CARICATURE, "Ohne Brustschild (der bleibt dem Hohepriester)"],
  era="nt", find=[(r"\bPriester", None)], distinct=["FIG-ROLLE-HOHEPRIESTER"])

E("FIG-ROLLE-PHARISAEER", "role", "Pharisäer", "Pharisee",
  "Angehöriger einer jüdischen Bewegung, die das Gesetz im Alltag genau befolgen will ([[MRK.7.3]], [[JHN.3.1]], [[PHP.3.5]]).",
  "Aaghörige vo ere jüdische Bewegig, wo s Gsetz im Alltag gnau wott befolge ([[MRK.7.3]], [[JHN.3.1]], [[PHP.3.5]]).",
  [T("Gebetskapsel (Gebetsriemen) an der Stirn und Quasten am Gewand", "text", "MAT.23.5"),
   T("Gebetsmantel mit Streifen über den Schultern", "design", note="Gebetsmantel mit Quasten nach [[NUM.15.38]]; die Streifen folgen späterer jüdischer Praxis"),
   T("Kopf frei (kein Kopfüberwurf, keine Kapuze), Bart, grau-blaues Gewand", "design")],
  ("#5A6A7A", "#4F6D8A"),
  [FACE, NO_CARICATURE, "Neutral und würdig; nicht als Bösewichte gekennzeichnet (auch Nikodemus und Paulus sind Pharisäer)"],
  era="nt", find=[(r"Pharisäer", None)], distinct=["FIG-ROLLE-SCHRIFTGELEHRTER", "FIG-NIKODEMUS"])

E("FIG-ROLLE-SCHRIFTGELEHRTER", "role", "Schriftgelehrter", "Scribe",
  "Kenner und Ausleger der Schriften ([[MRK.1.22]], [[MRK.12.28]]).",
  "Känner und Uusleger vo de Schrifte ([[MRK.1.22]], [[MRK.12.28]]).",
  [T("Offene Schriftrolle, darüber der lehrend erhobene Zeigefinger", "design", note="Er legt die Schrift aus ([[MRK.1.22]]); mit Schreibrohr las er sich als Schreiber (Blindtest Runde 3)"), T("Braunes Gewand", "design")],
  ("#6A5A4A", "#E7DCC4"),
  [FACE, NO_CARICATURE, "Neutral nach Amt"],
  era="nt", find=[(r"Schriftgelehrte", None)], distinct=["FIG-ROLLE-PHARISAEER", "FIG-OBADJA"])

E("FIG-ROLLE-SOLDAT", "role", "Soldat (römisch)", "Soldier (Roman)",
  "Römischer Soldat, etwa bei Verspottung und Kreuzigung Jesu; der Hauptmann führt eine Hundertschaft ([[JHN.19.2]], [[MRK.15.39]]).",
  "En römische Soldat, öppe bi de Verspottig und de Chrüüzigung vom Jesus; de Hauptmaa füert e Hundertschaft ([[JHN.19.2]], [[MRK.15.39]]).",
  [T("Helm mit rotem Busch, roter Umhang", "design")],
  ("#8E1F2F", "#8FA3A0"), [FACE, "Helm macht ihn eindeutig; roter Umhang kurz, nicht mit dem Mantel Jesu verwechselbar",
                           "Helmbusch längs, ohne Stab; quer gestellter Busch und Rebstock-Stab bleiben dem Hauptmann (FIG-ROLLE-HAUPTMANN)"],
  era="nt", find=[(r"Soldat|Hauptmann|Kohorte", None)], distinct=["FIG-ROLLE-TEMPELWACHE", "FIG-JESUS"])

E("FIG-ROLLE-HIRTE", "role", "Hirte", "Shepherd",
  "Jemand, der eine Herde hütet; Jesus nennt sich den guten Hirten ([[JHN.10.11]]).",
  "Öpper, wo e Herde hüetet; de Jesus nännt sich de guet Hirt ([[JHN.10.11]]).",
  [T("Grosses Schaf", "design", note="Ohne Stab: Stab und kleines Schaf überluden das Zeichen (Blindtest Runde 2 vom 2026-10-23)")],
  ("#8A7A50", "#F6EBD9"),
  [FACE, "Jesus als Hirte bleibt Jesus (mit Kreuznimbus), nicht diese Rolle"],
  era="any", find=[(r"Hirt", None)], distinct=["FIG-JESUS", "FIG-MOSE"])

E("FIG-ROLLE-FISCHER", "role", "Fischer", "Fisherman",
  "Jemand, der vom Fischfang lebt, wie Simon und Andreas am See von Galiläa ([[MRK.1.16]], [[JHN.21.3]]).",
  "Öpper, wo vom Fische läbt, wie de Simon und de Andreas am See vo Galiläa ([[MRK.1.16]], [[JHN.21.3]]).",
  [T("Netz", "text", "MRK.1.16"), T("Graublaues Arbeitsgewand", "design")],
  ("#6A7F8A", "#8A6A3A"), [FACE],
  era="nt", find=[(r"Fischer|Netz|fischen", None)], distinct=["FIG-ROLLE-JUENGER"])

E("FIG-ROLLE-KRANKER", "role", "Kranker", "Sick person",
  "Ein kranker, gelähmter oder blinder Mensch, der Hilfe sucht ([[MRK.2.3-MRK.2.4]], [[JHN.5.3]]).",
  "En chranke, glähmte oder blinde Mänsch, wo Hilf suecht ([[MRK.2.3-MRK.2.4]], [[JHN.5.3]]).",
  [T("Flache Strohmatte mit Geflecht und Fransen", "text", "MRK.2.4", "Gerollt las sie sich als Schriftrolle (Blindtest Runde 3); getragen ([[JHN.5.8]]) in der Szene"),
   T("Verband um den Kopf", "design"),
   T("Bei Blindheit Stab, bei Lähmung liegend", "design")],
  ("#C9BFAA", "#8A7A60"),
  [FACE, "Mit Würde; Krankheit nie als Strafe oder Schreckbild darstellen (vgl. [[JHN.9.3]])"],
  era="any", find=[(r"krank|Kranke|gelähmt|Gelähmte|blind|Blinde|lahm", ["MRK", "JHN", "PHP"])], distinct=["FIG-BARTIMAEUS"])

E("FIG-ROLLE-ENGEL", "role", "Engel", "Angel",
  "Bote Gottes, etwa die Engel im Grab Jesu ([[JHN.20.12]], [[MRK.1.13]]).",
  "En Bot vo Gott, öppe d Ängel im Grab vom Jesus ([[JHN.20.12]], [[MRK.1.13]]).",
  [T("Weisses Gewand", "text", "JHN.20.12"), T("Flügel", "tradition")],
  ("#FFFFFF", "#D9A441"),
  [FACE, "Kein Kreuznimbus; nicht mit dem Heiligen Geist (Taube) oder Jesus verwechselbar",
   "Das griechische Wort ἄγγελος heisst auch «Bote»; ob ein Engel oder ein menschlicher Bote gemeint ist, entscheidet der Zusammenhang"],
  era="any", find=[(r"Engel", None)], distinct=["FIG-HEILIGER-GEIST", "FIG-ROLLE-BOTE", "FIG-JESUS"],
  terms=[{"lang": "grc", "word": "ἄγγελος", "de": "Bote; Engel"}])

E("FIG-ROLLE-WITWE", "role", "Witwe", "Widow",
  "Eine Frau, deren Mann gestorben ist, etwa die arme Witwe am Opferkasten ([[MRK.12.42]]).",
  "E Frau, wo ire Maa gstorbe isch, öppe di arm Witwe am Opferchaschte ([[MRK.12.42]]).",
  [T("Dunkles Kopftuch", "design"), T("Zwei kleine Münzen (am Opferkasten)", "text", "MRK.12.42")],
  ("#4A4A4A", "#C9BFAA"),
  [FACE, "Würdig, nicht mitleidheischend"],
  era="any", find=[(r"Witwe", None)], distinct=["FIG-NOOMI"])

E("FIG-ROLLE-AELTESTER", "role", "Ältester", "Elder",
  "Angesehener Mann mit Leitungsverantwortung, etwa die Ältesten im Tor von Betlehem oder die Ältesten der Gemeinde auf Kreta ([[RUT.4.2]], [[TIT.1.5]]).",
  "En aagsehne Maa mit Leitigsverantwortig, öppe d Ältischte im Tor vo Betlehem oder d Ältischte vo de Gmeind uf Kreta ([[RUT.4.2]], [[TIT.1.5]]).",
  [T("Stadttor als Zeichen: Älteste sitzen im Tor", "text", "RUT.4.1-RUT.4.2"), T("Grauer Überwurf, langer grauer Bart", "design")],
  ("#6A5A4A", "#C9BFAA"),
  [FACE, "Je Buch verschiedene Ämter: Stadtälteste (Rut), jüdischer Rat (Markus), Gemeindeälteste (Titus)",
   "Nicht mit dem Briefschreiber «der Älteste» (FIG-DER-AELTESTE) verwechseln"],
  era="any", find=[(r"Ältest", ["RUT", "MRK", "TIT"])], distinct=["FIG-DER-AELTESTE"])

E("FIG-ROLLE-BOTE", "role", "Bote", "Messenger",
  "Ein Mensch, der eine Nachricht überbringt ([[MRK.1.2]], [[OBA.1.1]]).",
  "En Mänsch, wo e Nachricht überbringt ([[MRK.1.2]], [[OBA.1.1]]).",
  [T("Brauner Reisemantel", "design"), T("Brief in der Hand", "design"), T("Wanderstab", "design")],
  ("#8A6A3A", "#E2CDA8"),
  [FACE, "Ohne Flügel (sonst Engel)"],
  era="any", find=[(r"\bBote", None)], distinct=["FIG-ROLLE-ENGEL", "FIG-EPAPHRODITUS"])

E("FIG-ROLLE-KAPITAEN", "role", "Kapitän", "Captain",
  "Der Schiffsführer auf dem Schiff nach Tarschisch, der Jona weckt ([[JON.1.6]]).",
  "De Schiffsfüerer uf em Schiff uf Tarschisch, wo de Jona weckt ([[JON.1.6]]).",
  [T("Segelschiff als Zeichen", "design", note="Er führt das Schiff ([[JON.1.6]]); vorher Steuerruder, las sich als Löffel"), T("Dunkelblauer Umhang, Stirnband", "design")],
  ("#2F4F6F", "#8A6A3A"), [FACE],
  era="any", find=[(r"Kapitän", None)], distinct=["FIG-GRUPPE-SEELEUTE"])

E("FIG-GRUPPE-SEELEUTE", "group", "Seeleute", "Sailors",
  "Die Besatzung des Schiffes nach Tarschisch, die im Sturm zu ihren Göttern und dann zu JHWH ruft ([[JON.1.5]], [[JON.1.14-JON.1.16]]).",
  "D Bsatzig vom Schiff uf Tarschisch, wo im Sturm zu irne Gött und dänn zu JHWH rüeft ([[JON.1.5]], [[JON.1.14-JON.1.16]]).",
  [T("Kurze Arbeitskittel, Stirnband, Seilrolle über der Schulter", "design")],
  ("#2F4F6F", "#E2CDA8"), [FACE, NO_CARICATURE],
  era="any", find=[(r"Seeleute|die Männer", ["JON.1"])], distinct=["FIG-ROLLE-KAPITAEN"])

E("FIG-ROLLE-KOENIG", "role", "König", "King",
  "Ein Herrscher, etwa der König von Ninive, der sich in Sacktuch hüllt ([[JON.3.6]]), oder Herodes ([[MRK.6.14]]).",
  "En Herrscher, öppe de König vo Ninive, wo sich in Sacktuech iiwicklet ([[JON.3.6]]), oder de Herodes ([[MRK.6.14]]).",
  [T("Goldene Bügelkrone, violettes Gewand mit goldenem Mantel", "design"), T("Im Buch Jona: Sacktuch statt Mantel (nach der Umkehr)", "text", "JON.3.6")],
  ("#6A2E5E", "#D9A441"),
  [FACE, "Königsreif nicht mit dem goldenen Kranz des Bräutigams oder einem Nimbus verwechselbar",
   "Jesus als «König Israels» ([[JHN.1.49]]) nicht mit dieser Rolle, sondern mit Kreuznimbus und Dornenkranz bzw. Tafel"],
  era="any", find=[(r"König", ["JON.3", "MRK.6"])], distinct=["FIG-HERODES-ANTIPAS", "FIG-ROLLE-BRAEUTIGAM", "FIG-JESUS"])

E("FIG-GRUPPE-EDOM", "group", "Edom (Esau)", "Edom (Esau)",
  "Das Nachbarvolk Israels, nach seinem Stammvater auch Esau genannt, über das Obadja spricht ([[OBA.1.1]], [[OBA.1.6]]).",
  "S Nachbervolk vo Israel, nach sim Stammvater au Esau gnännt, wo de Obadja drüber redt ([[OBA.1.1]], [[OBA.1.6]]).",
  [T("Felsenwohnungen hoch im Gebirge", "text", "OBA.1.3"),
   T("Rötliche Farbe", "tradition", note="Der Name wird als «rot» gedeutet ([[GEN.25.30]]); Genesis noch nicht übersetzt.")],
  ("#9A4E3A", "#C9A27A"),
  [FACE, NO_CARICATURE, "Kein Volk als böse kennzeichnen; das Gericht betrifft das Verhalten ([[OBA.1.10-OBA.1.14]])"],
  era="exile", find=[(r"Edom|Esau", None)],
  terms=[{"lang": "heb", "word": "אֱדוֹם", "translit": "ʾĕdôm", "de": "Edom (gedeutet als «rot»)"}])

# ---------------------------------------------------------------------------------------------------------------
# 4. Gegenstände und Orte
# ---------------------------------------------------------------------------------------------------------------
E("FIG-OBJ-KRUG-WASSER", "object", "Krug mit Wasser", "Jar of water",
  "Steinerner Krug mit Wasser, wie die sechs Wasserkrüge für die Reinigung in Kana ([[JHN.2.6-JHN.2.7]]).",
  "En steinige Chrueg mit Wasser, wie di sächs Wasserchrüeg für d Reinigung z Kana ([[JHN.2.6-JHN.2.7]]).",
  [T("Steinerner Krug", "text", "JHN.2.6"), T("Blaues Tropfen-Emblem auf dem Krug", "design"), T("Gefüllt bis oben", "text", "JHN.2.7")],
  ("#C89B72", "#6FB2E6"),
  ["Tropfen-Emblem immer sichtbar; nie mit Trauben-Emblem kombinieren"],
  find=[(r"Wasserkrüge|Krüge mit Wasser", None)], distinct=["FIG-OBJ-KRUG-WEIN", "FIG-OBJ-KRUG-WEIN-LEER"])

E("FIG-OBJ-KRUG-WEIN", "object", "Krug mit Wein", "Jar of wine",
  "Krug mit Wein, etwa das zu Wein gewordene Wasser in Kana ([[JHN.2.9-JHN.2.10]]).",
  "En Chrueg mit Wii, öppe s Wasser, wo z Kana zu Wii worde isch ([[JHN.2.9-JHN.2.10]]).",
  [T("Trauben-Emblem auf dem Krug", "design"), T("Weinroter Füllstand am Rand sichtbar", "design")],
  ("#C89B72", "#8E1F2F"),
  ["Trauben-Emblem immer sichtbar", "Voll: Füllstand bis zum Rand (FIG-ZEICHEN-VOLL)"],
  find=[(r"Wein", ["JHN.2.9-JHN.2.10"])], distinct=["FIG-OBJ-KRUG-WASSER", "FIG-OBJ-KRUG-WEIN-LEER"])

E("FIG-OBJ-KRUG-WEIN-LEER", "object", "Leerer Weinkrug", "Empty wine jar",
  "Ein Weinkrug, aus dem nichts mehr kommt: «Sie haben keinen Wein mehr» ([[JHN.2.3]]).",
  "En Wiichrueg, wo nüüt meh drin isch: «Si händ kei Wii meh» ([[JHN.2.3]]).",
  [T("Trauben-Emblem", "design"), T("Sichtbar leer: derselbe feste Krug wie der Weinkrug, nur leicht geneigt, die Öffnung gross und dunkel, kein Wein", "design"),
   T("Daneben ein gestrichelter, leerer Tropfen: es kommt nichts mehr", "design")],
  ("#C89B72", "#E2CDA8"),
  ["Immer zusammen mit dem Zeichen «fehlt/leer» (FIG-ZEICHEN-FEHLT), wenn der Mangel die Aussage ist",
   "Der Text nennt keinen leeren Krug; das Bild drückt den Mangel aus"],
  find=[(r"Wein", ["JHN.2.3"])], distinct=["FIG-OBJ-KRUG-WEIN", "FIG-OBJ-KRUG-WASSER", "FIG-OBJ-WEINSCHLAUCH"])

E("FIG-OBJ-BECHER-LEER", "object", "Leerer Becher", "Empty cup",
  "Ein Trinkbecher ohne Inhalt.",
  "En Trinkbächer ohni Inhalt.",
  [T("Kleiner ockerfarbener Trinkbecher ohne Fuss, mit Henkel, schräg gekippt: innen nur die Wand und der dunkle Boden, nichts darin", "design")],
  ("#D9A55C", "#FFFDF6"),
  ["Becher ohne Fuss; der Kelch mit Fuss gehört zu Johannes, dem Sohn des Zebedäus", "Klein und mit Henkel, nicht als weites Gefäss mit hellem Inhalt (sonst Scheffel mit Mehl)"],
  distinct=["FIG-OBJ-BECHER-VOLL", "FIG-OBJ-BECHER-SCHMUTZIG", "FIG-JOHANNES-ZEBEDAEUS"])

E("FIG-OBJ-BECHER-VOLL", "object", "Voller Becher (Wein)", "Full cup (wine)",
  "Ein Trinkbecher mit Wein.",
  "En Trinkbächer mit Wii.",
  [T("Becher ohne Fuss mit weinroter Oberfläche", "design")],
  ("#D9A55C", "#8E1F2F"),
  ["Der «Becher», den Jesus trinken soll ([[JHN.18.11]], [[MRK.10.38]]), ist ein Bildwort; nur mit Deutungshinweis verwenden"],
  distinct=["FIG-OBJ-BECHER-LEER"])

E("FIG-OBJ-BROT", "object", "Brot", "Bread",
  "Rundes Fladenbrot, etwa die fünf Gerstenbrote bei der Speisung ([[JHN.6.9]], [[MRK.6.41]]).",
  "Es runds Fladebrot, öppe di föif Gärschtebrot bi de Speisig ([[JHN.6.9]], [[MRK.6.41]]).",
  [T("Rundes, flaches Brot", "design"), T("Gerstenbrot", "text", "JHN.6.9")],
  ("#D9A55C", "#9C6F1C"),
  ["Kein Hefezopf oder Kastenbrot"],
  find=[(r"Brot", None)])

E("FIG-OBJ-FISCH", "object", "Fisch", "Fish",
  "Fisch als Speise oder Fang am See von Galiläa ([[JHN.6.9]], [[JHN.21.11]]).",
  "Fisch als Ässe oder Fang am See vo Galiläa ([[JHN.6.9]], [[JHN.21.11]]).",
  [T("Kleiner silbergrauer Fisch, naturalistisch: Rücken- und Brustflosse, Gabelschwanz, Kiemenbogen, Schuppen, heller Bauch", "design")],
  ("#8FA3A0", "#6FB2E6"),
  ["Nicht mit dem grossen Fisch des Jona verwechseln", "Kein Fischsymbol aus zwei Bögen (Ichthys)"],
  find=[(r"Fisch", ["MRK", "JHN"])], distinct=["FIG-OBJ-GROSSER-FISCH"])

E("FIG-OBJ-GROSSER-FISCH", "object", "Grosser Fisch (Jona)", "Great fish (Jonah)",
  "Der grosse Fisch, den JHWH bestimmt, um Jona zu verschlingen ([[JON.1.17]], [[JON.2.10]]).",
  "De gross Fisch, wo JHWH bestimmt, dass er de Jona verschluckt ([[JON.1.17]], [[JON.2.10]]).",
  [T("Grosser Fisch", "text", "JON.1.17"), T("Blaugrau, grösser als das Boot", "design"),
   T("Weit offenes Maul mit dunklem Schlund; zwei kleine Fische daneben zeigen die Grösse", "design")],
  ("#4A6E8A", "#8FA3A0"),
  ["Kein Wal mit Fontäne", "Nicht bedrohlich-monsterhaft"],
  find=[(r"Fisch", ["JON"])], distinct=["FIG-OBJ-FISCH"])

E("FIG-OBJ-BOOT", "object", "Boot", "Boat",
  "Fischerboot auf dem See von Galiläa; bei Jona ein Handelsschiff ([[MRK.4.37]], [[JON.1.3]]).",
  "Es Fischerboot uf em See vo Galiläa; bim Jona es Handelsschiff ([[MRK.4.37]], [[JON.1.3]]).",
  [T("Fischerboot mit einem Segel und Rudern", "design"), T("Bei Jona: grösseres Schiff mit Ladung", "text", "JON.1.5")],
  ("#8A6A3A", "#6FB2E6"), [],
  find=[(r"Boot|Schiff", None)])

E("FIG-OBJ-KREUZ", "object", "Kreuz", "Cross",
  "Das Kreuz, an dem Jesus hingerichtet wird ([[JHN.19.17-JHN.19.19]], [[MRK.15.21]]).",
  "S Chrüüz, wo de Jesus dra higrichtet wird ([[JHN.19.17-JHN.19.19]], [[MRK.15.21]]).",
  [T("Holzkreuz mit Tafel oben", "text", "JHN.19.19"), T("Dunkles Holz", "design")],
  ("#7A5A34", "#5B4630"),
  ["Nicht mit Kreuznimbus, Kreuzstab des Täufers, Stabkreuz des Philippus oder X-Kreuz des Andreas verwechselbar",
   "Keine Blutdarstellung"],
  find=[(r"Kreuz", None)], distinct=["FIG-JOHANNES-TAEUFER", "FIG-ANDREAS", "FIG-PHILIPPUS"])

E("FIG-OBJ-SCHAF", "object", "Schaf", "Sheep",
  "Schaf als Herdentier, als Opfertier im Tempel oder im Bildwort vom Hirten ([[JHN.2.14]], [[JHN.10.11]]).",
  "Es Schaf als Herdetier, als Opfertier im Tämpel oder im Bildwort vom Hirt ([[JHN.2.14]], [[JHN.10.11]]).",
  [T("Weisses Wollschaf", "design")],
  ("#F6EBD9", "#B4B2A9"),
  ["Ohne Nimbus; das «Lamm Gottes» ([[JHN.1.29]]) als Christus-Bild nur mit Kreuznimbus und als Deutung"],
  find=[(r"Schaf", None)], distinct=["FIG-JOHANNES-TAEUFER"])

E("FIG-OBJ-TAUBE", "object", "Taube (Tier)", "Dove (animal)",
  "Taube als Tier, etwa als Opfertier bei den Händlern im Tempel ([[JHN.2.14]], [[MRK.11.15]]).",
  "Tuube als Tier, öppe als Opfertier bi de Händler im Tämpel ([[JHN.2.14]], [[MRK.11.15]]).",
  [T("Graue Taube, sitzend oder im Käfig", "design")],
  ("#B4B2A9", "#FFFFFF"),
  ["Nie mit Nimbus oder Lichtschein und nie von oben herabkommend; das bleibt dem Heiligen Geist vorbehalten"],
  find=[(r"Taube", ["JHN.2", "MRK.11"])], distinct=["FIG-HEILIGER-GEIST"])

E("FIG-OBJ-MUENZEN", "object", "Münzen", "Coins",
  "Geld in Münzen, etwa beim Tisch der Geldwechsler oder die zwei Lepta der Witwe ([[JHN.2.15]], [[MRK.12.42]]).",
  "Gäld i Münze, öppe uf em Tisch vo de Gäldwächsler oder di zwei Lepta vo de Witwe ([[JHN.2.15]], [[MRK.12.42]]).",
  [T("Drei runde Münzen, gold und silbern, dunkle Kontur", "design")],
  ("#D9A441", "#B4B2A9"),
  ["Nicht mit dem Zeichen-Stern verwechselbar (rund, ohne Zacken)", "Tragende Merkmale (Runde 6, Einsatzgrösse 32 px; beim Neuzeichnen nicht weglassen): Drei runde Münzen, gold und silbern, dunkle Kontur", "Detailstufe 1 von 3 gewählt. Blindtest 2026-10-24 (Runde 6), 32 px allein, getroffen je Stufe 1 · 2 · 3: 4 · 4 · 4 von 4; gelesen als «Geld, Münzen»"],
  find=[(r"Münze|Denar|Lepta|Geld", None)], distinct=["FIG-ZEICHEN-STERN"])

E("FIG-OBJ-PEITSCHE", "object", "Geissel aus Stricken", "Whip of cords",
  "Die Geissel aus Stricken, mit der Jesus die Händler aus dem Tempel treibt ([[JHN.2.15]]).",
  "D Geissle us Strick, wo de Jesus d Händler mit us em Tämpel triibt ([[JHN.2.15]]).",
  [T("Aus Stricken geflochten", "text", "JHN.2.15"), T("Kurzer Holzgriff, drei geflochtene Stricke mit Knoten am Ende", "design")],
  ("#B07A3E", "#7A5A34"),
  ["Erhoben, nie im Schlag auf Menschen; ob sie Menschen oder nur Tiere traf, lässt der Text offen"], find=[(r"Geissel", None)])

E("FIG-OBJ-LAMPE", "object", "Öllampe", "Oil lamp",
  "Kleine Tonlampe mit Docht ([[MRK.4.21]], [[JHN.5.35]]).",
  "Es chliises Tonlämpli mit Docht ([[MRK.4.21]], [[JHN.5.35]]).",
  [T("Flache Tonlampe mit kleiner Flamme", "design")],
  ("#C89B72", "#F2C76E"),
  ["Keine Laterne mit Glas (anachronistisch); Laternen und Fackeln der Wache ([[JHN.18.3]]) eigens zeichnen"],
  find=[(r"Lampe|Leuchte", None)])

E("FIG-OBJ-SCHRIFTROLLE", "object", "Schriftrolle / Buch", "Scroll / book",
  "Geschriebenes Wort: Schriftrolle, Brief oder Buch ([[2JN.1.12]], [[3JN.1.13]]).",
  "Gschribnigs Wort: Schriftrolle, Brief oder Buech ([[2JN.1.12]], [[3JN.1.13]]).",
  [T("Schriftrolle mit zwei Stäben", "design"), T("Briefe: gefaltetes Blatt mit Siegel", "design")],
  ("#F2E6CC", "#8A6A3A"),
  ["Gebundenes Buch nur als Tradition (Evangelisten, Paulus); in Szenen zur Zeit des Textes Rolle oder Brief"],
  find=[(r"\bBuch|Bücher|Papier|Tinte|\bTafel\b", None)])

E("FIG-ORT-TEMPEL", "place", "Tempel", "Temple",
  "Der Tempel in Jerusalem mit Vorhöfen und Säulenhallen ([[JHN.2.14]], [[MRK.11.15]]).",
  "De Tämpel z Jerusalem mit Vorhöf und Süülehalle ([[JHN.2.14]], [[MRK.11.15]]).",
  [T("Hohes, helles Gebäude mit Säulen und Goldkante", "design")],
  ("#E7DCC4", "#D9A441"),
  ["Nicht als Kirche (kein Turm, kein Kreuz)"],
  find=[(r"Tempel", None)], distinct=["FIG-ORT-JERUSALEM"])

E("FIG-ORT-JERUSALEM", "place", "Jerusalem", "Jerusalem",
  "Die Stadt mit dem Tempel, Ziel der Feste und Ort von Kreuzigung und Auferstehung ([[JHN.2.13]], [[MRK.11.11]]).",
  "D Stadt mit em Tämpel, Ziil vo de Fescht und Ort vo Chrüüzigung und Uferstehig ([[JHN.2.13]], [[MRK.11.11]]).",
  [T("Stadtmauer mit Tor, dahinter der Tempel", "design")],
  ("#E2CDA8", "#C9BFAA"), [],
  find=[(r"Jerusalem", None)], distinct=["FIG-ORT-TEMPEL"])

E("FIG-ORT-HAUS", "place", "Haus", "House",
  "Einfaches Wohnhaus mit Flachdach ([[MRK.2.1-MRK.2.4]]).",
  "Es eifachs Wohnhuus mit Flachdach ([[MRK.2.1-MRK.2.4]]).",
  [T("Flachdach (abdeckbar)", "text", "MRK.2.4"), T("Würfelform, eine Tür", "design")],
  ("#E2CDA8", "#8A6A3A"),
  ["Kein Giebeldach"], find=[(r"\bHaus\b", ["RUT", "MRK", "JHN"])])

E("FIG-ORT-WEG", "place", "Weg", "Road",
  "Weg oder Strasse, auf dem Jesus mit den Jüngern unterwegs ist ([[MRK.8.27]], [[MRK.10.52]]).",
  "En Wäg oder e Strass, wo de Jesus mit de Jünger underwägs isch ([[MRK.8.27]], [[MRK.10.52]]).",
  [T("Heller, geschwungener Pfad", "design")],
  ("#D8CBB0", "#A79A80"),
  ["Bildwort «Ich bin der Weg» ([[JHN.14.6]]) nur mit Deutungshinweis"], find=[(r"\bWeg\b", None)])

E("FIG-ORT-BERG", "place", "Berg", "Mountain",
  "Berg oder Anhöhe, etwa der Berg der Verklärung oder der Ölberg ([[MRK.9.2]], [[MRK.13.3]]).",
  "En Bärg oder e Höchi, öppe de Bärg vo de Verklärig oder de Ölbärg ([[MRK.9.2]], [[MRK.13.3]]).",
  [T("Grüngrauer Hügel mit einem Gipfel", "design")],
  ("#8A9A7A", "#6E8B3D"), [], find=[(r"\bBerg", None)])

E("FIG-ORT-SEE", "place", "See", "Lake",
  "Der See von Galiläa (See von Tiberias) ([[MRK.1.16]], [[JHN.6.1]]).",
  "De See vo Galiläa (See vo Tiberias) ([[MRK.1.16]], [[JHN.6.1]]).",
  [T("Blaue Wasserfläche mit Wellenlinien und Ufer", "design"), T("Hügel am Gegenufer, Schilf am Rand", "design")],
  ("#6FB2E6", "#3E6E9E"),
  ["Das offene Meer bei Jona mit hohen Wellen und ohne Ufer zeichnen"],
  find=[(r"\bSee\b|Meer von Galiläa|Meer von Tiberias", ["MRK", "JHN"])], distinct=["FIG-ORT-WUESTE"])

E("FIG-ORT-WUESTE", "place", "Wüste", "Wilderness",
  "Unbewohntes, karges Land, etwa wo Johannes tauft und Jesus versucht wird ([[MRK.1.4]], [[MRK.1.12-MRK.1.13]]).",
  "Unbewohnts, chargs Land, öppe wo de Johannes tauft und de Jesus versuecht wird ([[MRK.1.4]], [[MRK.1.12-MRK.1.13]]).",
  [T("Sandfarbener Boden, Felsen, einzelner Strauch", "design")],
  ("#E8C98A", "#C9A27A"),
  ["Nicht als Sanddünenwüste: steinig und karg"], find=[(r"Wüste|einsamen Ort", None)])

E("FIG-ORT-GRAB", "place", "Grab", "Tomb",
  "Felsengrab mit Rollstein, etwa das Grab Jesu oder des Lazarus ([[MRK.15.46]], [[JHN.11.38]]).",
  "Es Felsegrab mit Rollstei, öppe s Grab vom Jesus oder vom Lazarus ([[MRK.15.46]], [[JHN.11.38]]).",
  [T("Aus dem Felsen gehauen, runder Stein vor dem Eingang", "text", "MRK.15.46"),
   T("Leeres Grab: Stein weggerollt, Leinenbinden sichtbar", "text", "JHN.20.5")],
  ("#A79A80", "#3B3226"),
  ["Keine Gebeine oder Schreckbilder"], find=[(r"Grab|Gruft", None)])

# ---------------------------------------------------------------------------------------------------------------
# 5. Handlungszeichen (Sprechblasen und Gesten)
# ---------------------------------------------------------------------------------------------------------------
E("FIG-ZEICHEN-SPRECHEN", "action", "sprechen", "speak",
  "Bedeutung: Eine Figur sagt etwas; der Inhalt steht als Symbol in der Blase.",
  "Bedüütig: E Figur seit öppis; de Inhalt staat als Symbol i de Blase.",
  [T("Als Zeichen: drei Schallbögen", "design"), T("Gesprochenes selbst steht in einer weissen Sprechblase mit Spitze zum Sprechenden, nur mit Lexikon-Symbolen", "design")],
  ("#FFFFFF", "#3B3226"),
  ["Spitze zeigt immer auf den Mund bzw. Kopf des Sprechenden",
   "Nicht verwechseln mit «verkündigen» (Strahlen, mehrere Empfänger) und «fragen» (Fragezeichen)",
   "Keine Denkblase (Wolkenrand) für gesprochene Rede"],
  distinct=["FIG-ZEICHEN-VERKUENDIGEN", "FIG-ZEICHEN-FRAGEN"])

E("FIG-ZEICHEN-FRAGEN", "action", "fragen", "ask",
  "Bedeutung: Eine Figur stellt eine Frage an eine andere.",
  "Bedüütig: E Figur stellt eren andere e Frag.",
  [T("Sprechblase mit Fragezeichen", "design"), T("Spitze zum Fragenden, Blick zum Gefragten", "design")],
  ("#FFFFFF", "#3B3226"),
  ["Nicht verwechseln mit «nicht verstehen» (graues Fragezeichen im Nebel, ohne Blase)"],
  distinct=["FIG-ZEICHEN-NICHT-VERSTEHEN", "FIG-ZEICHEN-SPRECHEN"])

E("FIG-ZEICHEN-HOEREN", "action", "hören / gehorchen", "hear / obey",
  "Bedeutung: hören; mit Pfeil zur Handlung: gehorchen, das Gehörte tun (z. B. [[JHN.2.5]], [[JHN.2.7]]).",
  "Bedüütig: lose; mit Pfiil zur Handlig: folge, s Ghört tue (z. B. [[JHN.2.5]], [[JHN.2.7]]).",
  [T("Stilisiertes Ohr neben dem Kopf", "design"), T("Gehorchen: Ohr mit Pfeil zur ausgeführten Handlung", "design")],
  ("#E2CDA8", "#3B3226"),
  ["Nicht verwechseln mit der Verletzung des Malchus ([[JHN.18.10]])"],
  distinct=["FIG-MALCHUS"])

E("FIG-ZEICHEN-ZEIGEN", "action", "zeigen / weisen", "point / direct",
  "Bedeutung: Eine Figur weist auf jemanden oder etwas hin oder gibt eine Anweisung.",
  "Bedüütig: E Figur zeigt uf öpper oder öppis oder git en Aawiisig.",
  [T("Ausgestreckter Arm mit Zeigefinger", "design"), T("Gestrichelter Pfeil zum Ziel", "design")],
  ("#3B3226", "#F4F1EA"),
  ["Nicht verwechseln mit «geben» (Gegenstand in der Hand) und «segnen» (Hand über einer Person, Lichtpunkte)"],
  distinct=["FIG-ZEICHEN-GEBEN", "FIG-ZEICHEN-SEGNEN"])

E("FIG-ZEICHEN-GEBEN", "action", "geben", "give",
  "Bedeutung: Eine Figur reicht einer anderen etwas.",
  "Bedüütig: E Figur git eren andere öppis.",
  [T("Ausgestreckte Hand mit Ärmel, darüber eine Münze", "design")],
  ("#3B3226", "#D9A441"),
  ["Nicht verwechseln mit «bringen» (Figur unterwegs mit Gegenstand, Bewegungslinien)", "Tragende Merkmale (Runde 6, Einsatzgrösse 32 px; beim Neuzeichnen nicht weglassen): Ausgestreckte Hand mit Ärmel, darüber eine Münze", "Detailstufe 1 von 3 gewählt. Blindtest 2026-10-24 (Runde 6), 32 px allein, getroffen je Stufe 1 · 2 · 3: 4 · 4 · 4 von 4; gelesen als «Münze geben»"],
  distinct=["FIG-ZEICHEN-BRINGEN", "FIG-ZEICHEN-ZEIGEN"])

E("FIG-ZEICHEN-BRINGEN", "action", "bringen", "bring",
  "Bedeutung: Eine Figur trägt etwas zu jemandem hin (z. B. [[JHN.2.8]]).",
  "Bedüütig: E Figur treit öppis zu öpperem ane (z. B. [[JHN.2.8]]).",
  [T("Figur im Schritt mit Gegenstand", "design"), T("Bewegungslinien hinter der Figur, Pfeil auf dem Weg zum Ziel", "design")],
  ("#3B3226", "#C08A2A"),
  ["Nicht verwechseln mit «geben» (stehende Übergabe)"],
  distinct=["FIG-ZEICHEN-GEBEN"])

E("FIG-ZEICHEN-FEHLT", "sign", "fehlt / leer", "missing / empty",
  "Bedeutung: Etwas fehlt oder ist aufgebraucht (z. B. der Wein in [[JHN.2.3]]).",
  "Bedüütig: Öppis fehlt oder isch ufbruucht (z. B. de Wii i [[JHN.2.3]]).",
  [T("Gestrichelter Umriss des fehlenden Gegenstands", "design"), T("Kleiner leerer Kreis mit Schrägstrich", "design")],
  ("#B4B2A9", "#3B3226"),
  ["Grau, nie rot; nicht verwechseln mit «ablehnen» (rote abwehrende Hand)"],
  distinct=["FIG-ZEICHEN-ABLEHNEN", "FIG-ZEICHEN-VOLL"])

E("FIG-ZEICHEN-VOLL", "sign", "voll", "full",
  "Bedeutung: Etwas ist bis oben gefüllt (z. B. die Krüge in [[JHN.2.7]]).",
  "Bedüütig: Öppis isch bis obe gfüllt (z. B. d Chrüeg i [[JHN.2.7]]).",
  [T("Füllstand bis zum Rand mit Wellenlinie", "design"), T("Kleine Markierung «bis oben» am Rand", "design")],
  ("#6E8B3D", "#3B3226"),
  ["Nicht überlaufend, wenn der Text es nicht sagt"],
  distinct=["FIG-ZEICHEN-FEHLT"])

E("FIG-ZEICHEN-STERN", "sign", "Zeichen (σημεῖον)", "Sign (σημεῖον)",
  "Bedeutung: Eine Tat Jesu, die das Johannesevangelium «Zeichen» (σημεῖον) nennt, weil sie auf seine Herrlichkeit hinweist ([[JHN.2.11]], [[JHN.20.30-JHN.20.31]]).",
  "Bedüütig: E Tat vom Jesus, wo s Johannesevangelium «Zeiche» (σημεῖον) nännt, will si uf sini Herrlichkeit hiiwiist ([[JHN.2.11]], [[JHN.20.30-JHN.20.31]]).",
  [T("Goldener Stern", "design")],
  ("#D9A441", "#F7DB9A"),
  ["Nicht verwechseln mit dem Stern der Sterndeuter ([[MAT.2.2]]), mit Münzen oder einem Nimbus",
   "Bei Markus nur, wo der Text «Zeichen» sagt ([[MRK.8.11-MRK.8.12]]); Machttaten sonst ohne Stern"],
  find=[(r"Zeichen", ["JHN"])], distinct=["FIG-OBJ-MUENZEN", "FIG-GOTT"],
  terms=[{"lang": "grc", "word": "σημεῖον", "de": "Zeichen"}])

E("FIG-ZEICHEN-GLAUBEN", "sign", "glauben", "believe",
  "Bedeutung: Jemand vertraut, kommt zum Glauben (z. B. [[JHN.2.11]]).",
  "Bedüütig: Öpper vertrout, chunnt zum Glaube (z. B. [[JHN.2.11]]).",
  [T("Herz mit Lichtstrahl von oben", "design")],
  ("#D4537E", "#F7DB9A"),
  ["Herz ohne Lichtstrahl nicht verwenden (Verwechslung mit «lieben»)",
   "Nicht verwechseln mit «Freude» (Funken um die Figur)"],
  distinct=["FIG-ZEICHEN-FREUDE"])

E("FIG-ZEICHEN-BETEN", "action", "beten", "pray",
  "Bedeutung: Eine Figur wendet sich an Gott (z. B. [[LUK.11.1]], [[JON.2.1]]).",
  "Bedüütig: E Figur wändet sich a Gott (z. B. [[LUK.11.1]], [[JON.2.1]]).",
  [T("Zwei aneinandergelegte Handflächen, Finger nach oben (gestufte Fingerspitzen), Daumen vorn", "tradition"), T("Ärmel unten und feine Strahlen seitlich oben", "design")],
  ("#3B3226", "#F7DB9A"),
  ["Nicht verwechseln mit «Freude» (Arme hoch mit Funken) und «segnen» (Hand über anderer Person)"],
  distinct=["FIG-ZEICHEN-FREUDE", "FIG-ZEICHEN-SEGNEN"])

E("FIG-ZEICHEN-SEGNEN", "action", "segnen", "bless",
  "Bedeutung: Jemand spricht einem anderen Gutes von Gott zu (z. B. [[MRK.10.16]]).",
  "Bedüütig: Öpper spricht eme andere Guets vo Gott zue (z. B. [[MRK.10.16]]).",
  [T("Grosse Figur legt einer kleineren die Hand auf den Kopf", "design"), T("Goldene Lichtstriche über der Hand", "design")],
  ("#3B3226", "#F7DB9A"),
  ["Nicht verwechseln mit «heilen» (Berührung mit grünem Lichtpunkt an der kranken Stelle)", "Tragende Merkmale (Runde 6, Einsatzgrösse 32 px; beim Neuzeichnen nicht weglassen): Grosse Figur legt einer kleineren die Hand auf den Kopf; Goldene Lichtstriche über der Hand", "Detailstufe 2 von 3 gewählt. Blindtest 2026-10-24 (Runde 6), 32 px allein, getroffen je Stufe 1 · 2 · 3: 3 · 4 · 4 von 4; gelesen als «Segnen»"],
  distinct=["FIG-ZEICHEN-HEILEN", "FIG-ZEICHEN-BETEN"])

E("FIG-ZEICHEN-HEILEN", "action", "heilen", "heal",
  "Bedeutung: Ein kranker Mensch wird gesund (z. B. [[MRK.1.31]], [[JHN.5.9]]).",
  "Bedüütig: En chranke Mänsch wird gsund (z. B. [[MRK.1.31]], [[JHN.5.9]]).",
  [T("Berührende Hand", "design"), T("Grüner Lichtpunkt mit kleinem Spross an der geheilten Stelle", "design")],
  ("#6E8B3D", "#F7DB9A"),
  ["Nicht verwechseln mit «segnen»"], distinct=["FIG-ZEICHEN-SEGNEN"])

E("FIG-ZEICHEN-VERKUENDIGEN", "action", "verkündigen", "proclaim",
  "Bedeutung: Eine Botschaft wird öffentlich vielen gesagt (z. B. [[MRK.1.14]], [[JON.3.4]]).",
  "Bedüütig: E Botschaft wird öffentlich vilne gseit (z. B. [[MRK.1.14]], [[JON.3.4]]).",
  [T("Goldener Rufer (Lautsprecher) mit Schallwellen", "design")],
  ("#FFFFFF", "#D9A441"),
  ["Nicht verwechseln mit «sprechen» (einfache Blase zu einer Person)"],
  distinct=["FIG-ZEICHEN-SPRECHEN"])

E("FIG-ZEICHEN-ABLEHNEN", "action", "verwerfen / ablehnen", "reject / refuse",
  "Bedeutung: Jemand weist eine Person oder Botschaft zurück (z. B. [[JHN.1.11]], [[3JN.1.10]]).",
  "Bedüütig: Öpper wiist e Person oder e Botschaft zrugg (z. B. [[JHN.1.11]], [[3JN.1.10]]).",
  [T("Grosse Faust mit Daumen nach unten", "design"), T("Ärmel oben und Fingerlinien (ohne sie nur «Daumen runter» gelesen)", "design")],
  ("#8E1F2F", "#3B3226"),
  ["Nicht verwechseln mit «fehlt/leer» (graues Zeichen, keine Person)", "Tragende Merkmale (Runde 6, Einsatzgrösse 32 px; beim Neuzeichnen nicht weglassen): Grosse Faust mit Daumen nach unten; Ärmel oben und Fingerlinien (ohne sie nur «Daumen runter» gelesen)", "Detailstufe 2 von 3 gewählt. Blindtest 2026-10-24 (Runde 6), 32 px allein, getroffen je Stufe 1 · 2 · 3: 0 · 3 · 0 von 4; gelesen als «ablehnen, schlecht»"],
  distinct=["FIG-ZEICHEN-FEHLT"])

E("FIG-ZEICHEN-NICHT-VERSTEHEN", "sign", "nicht verstehen", "not understand",
  "Bedeutung: Jemand versteht das Gesagte nicht oder missversteht es (z. B. [[JHN.3.4]], [[MRK.9.32]]).",
  "Bedüütig: Öpper verstaat s Gseit nöd oder verstaat s falsch (z. B. [[JHN.3.4]], [[MRK.9.32]]).",
  [T("Graue Nebelwolke mit Fragezeichen", "design")],
  ("#8FA3A0", "#3B3226"),
  ["Ohne Sprechblase; nicht verwechseln mit «fragen»"], distinct=["FIG-ZEICHEN-FRAGEN"])

E("FIG-ZEICHEN-STUNDE", "sign", "Zeit / Stunde", "Time / hour",
  "Bedeutung: Die Zeit oder «Stunde», besonders die Stunde Jesu bei Johannes: «noch nicht gekommen» oder «gekommen» ([[JHN.2.4]], [[JHN.17.1]]).",
  "Bedüütig: D Ziit oder «Stund», bsunders d Stund vom Jesus bim Johannes: «no nöd cho» oder «cho» ([[JHN.2.4]], [[JHN.17.1]]).",
  [T("Sanduhr", "design", note="Die Sanduhr gab es in neutestamentlicher Zeit noch nicht; sie ist ein heutiges Bildzeichen, kein Gegenstand der Szene."),
   T("«Noch nicht»: oben voll; «gekommen»: durchgelaufen", "design")],
  ("#C08A2A", "#E8C98A"),
  ["Nur als Zeichen, nie als Gegenstand in der Szene", "Uhrzeitangaben ([[JHN.1.39]]) nicht mit diesem Zeichen"],
  find=[(r"(meine|seine|die|eine|diese[rn]?) Stunde (ist |war )?(noch nicht )?(gekommen|kommt)|Stunde gekommen|Stunde kommt|aus dieser Stunde|in diese Stunde", ["JHN"])])

E("FIG-ZEICHEN-FREUDE", "sign", "Freude", "Joy",
  "Bedeutung: Jemand freut sich (z. B. [[JHN.3.29]], [[JHN.20.20]]).",
  "Bedüütig: Öpper freut sich (z. B. [[JHN.3.29]], [[JHN.20.20]]).",
  [T("Goldene Funken um die Figur", "design")],
  ("#F2C76E", "#3B3226"),
  ["Nicht verwechseln mit «beten» (ruhige Haltung, Linie nach oben) und «glauben» (Herz)"],
  distinct=["FIG-ZEICHEN-BETEN", "FIG-ZEICHEN-GLAUBEN"])

E("FIG-ZEICHEN-TRAUER", "sign", "Trauer", "Grief",
  "Bedeutung: Jemand trauert oder weint (z. B. [[JHN.11.33-JHN.11.35]], [[JHN.20.11]]).",
  "Bedüütig: Öpper truuret oder briegget (z. B. [[JHN.11.33-JHN.11.35]], [[JHN.20.11]]).",
  [T("Gesenkter Kopf", "design"), T("Graublaue Träne neben dem Kopf", "design")],
  ("#6A7F8A", "#3B3226"),
  ["Träne klein und grau, nicht mit dem blauen Wasser-Tropfen-Emblem verwechselbar"],
  distinct=["FIG-OBJ-KRUG-WASSER"])


# ---------------------------------------------------------------------------------------------------------------
# Werkzeug
# ---------------------------------------------------------------------------------------------------------------
def load_texts():
    texts = {}
    for f in sorted(glob.glob(str(D / "translations" / "TRANS-*-DE-WORKING.json"))):
        texts.update(json.loads(pathlib.Path(f).read_text(encoding="utf-8")).get("text_by_reference") or {})
    return texts


def key(ref):
    b, c, v = ref.split(".")
    return BOOKS.index(b), int(c), int(v)


def in_scope(ref, item):
    """item: Buch (JHN), Kapitel (JHN.2), Vers (JHN.2.3) oder Bereich innerhalb eines Kapitels (JHN.2.1-JHN.2.12)."""
    if "-" in item:
        a, b = item.split("-")
        return key(a) <= key(ref) <= key(b)
    parts = item.split(".")
    return ref == item if len(parts) == 3 else ref.split(".")[:len(parts)] == parts


def appears(fid, find, texts):
    hits = set()
    for pat, within in find:
        rx = re.compile(pat)
        found = {r for r, t in texts.items() if r.split(".")[0] in BOOKS and rx.search(t)
                 and (within is None or any(in_scope(r, w) for w in within))}
        if within:
            for w in within:
                if not any(in_scope(r, w) for r in found):
                    raise SystemExit(f"{fid}: Muster {pat!r} findet in {w} nichts")
        elif not found:
            raise SystemExit(f"{fid}: Muster {pat!r} findet nichts")
        hits |= found
    by_ch = {}
    for r in hits:
        b, c, _ = r.split(".")
        by_ch.setdefault((b, int(c)), []).append(r)
    chapters = sorted(by_ch, key=lambda k: (-len(by_ch[k]), BOOKS.index(k[0]), k[1]))[:MAX_RANGES]
    out = []
    for ch in sorted(chapters, key=lambda k: (BOOKS.index(k[0]), k[1])):
        rs = sorted(by_ch[ch], key=key)
        out.append(f"[[{rs[0]}]]" if len(rs) == 1 else f"[[{rs[0]}-{rs[-1]}]]")
    return out, sorted({r.split(".")[0] for r in hits}, key=BOOKS.index), len(hits), len(by_ch)


def build(e, texts):
    fid = e["id"]
    if not re.fullmatch(r"FIG-[A-Z0-9]+(-[A-Z0-9]+)*", fid):
        raise SystemExit(f"{fid}: ID ungültig")
    if e["kind"] not in KINDS:
        raise SystemExit(f"{fid}: kind {e['kind']!r} ungültig")
    if e["kind"] in ("person", "role") and e["era"] not in ERAS:
        raise SystemExit(f"{fid}: era fehlt oder ungültig")
    for t in e["traits"]:
        if t["basis"] not in ("text", "tradition", "design") or (t["basis"] == "text") != bool(t.get("ref")):
            raise SystemExit(f"{fid}: Merkmal {t['trait_de']!r}: basis/ref passen nicht")
    for c in e["pal"]:
        if not re.fullmatch(r"#[0-9A-F]{6}", c):
            raise SystemExit(f"{fid}: Farbe {c} ungültig")
    rec = {"id": fid, "type": "figure", "status": "draft", "tags": [], "kind": e["kind"],
           "names": {"de": e["de"], "en": e["en"]}, "identity_de": e["ident"]}
    if e["era"]:
        rec["era"] = e["era"]
    rec["display_group"] = display_group(fid, e["kind"])
    rec["traits"] = e["traits"]
    kz = legend_short(fid)
    if kz:  # kurzer Erkennungstext für die Legende «Figuren und Zeichen» (höchstens etwa 60 Zeichen, BILDPROZESS.md)
        if any(len(v) > 70 for v in kz.values()):
            raise SystemExit(f"{fid}: Legendentext zu lang ({kz})")
        rec["legend"] = kz
    rec["palette"] = {"primary": e["pal"][0], "secondary": e["pal"][1]}
    rec["rules_de"] = e["rules"]
    if e["distinct"]:
        rec["distinct_from"] = e["distinct"]
    if e["terms"]:
        rec["terms"] = e["terms"]
    tags = list(e["tags"])
    if e["find"]:
        rec["appears_in"], books, nv, nc = appears(fid, e["find"], texts)
        rec["appears_in_note_de"] = APPEARS_NOTE + f" Fundstellen gesamt: {nv} Verse in {nc} Kapiteln."
        if e["kind"] in ("person", "role", "group"):
            tags += [BOOK_TAG[b] for b in books]
    else:
        rec["appears_in"], rec["appears_in_note_de"] = [], APPEARS_NONE
    rec["tags"] = list(dict.fromkeys(tags))
    rec["authorship_de"] = AUTH
    rec["knowledge"] = {"asserted_at": DATE, "supersedes": None}
    return rec


# ---------------------------------------------------------------------------------------------------------------
# Ergänzungen nach dem ersten Blindtest (2026-10-14): Zeichen, die in den Bildern vorkommen
# ---------------------------------------------------------------------------------------------------------------
E("FIG-ZEICHEN-ABSTAND", "sign", "Abstand / vertraut sich nicht an", "Distance / does not entrust himself",
  "Bedeutung: Zwischen Personen besteht innerer Abstand; jemand vertraut sich anderen nicht an (z. B. [[JHN.2.24]]).",
  "Bedüütig: Zwüsched Persone isch en innere Abstand; öpper vertrout sich andere nöd aa (z. B. [[JHN.2.24]]).",
  [T("Senkrechte gestrichelte Linie zwischen den Figuren", "design"), T("Die Figur auf der einen Seite wendet sich leicht ab", "design")],
  ("#B4A98F", "#7A7568"), ["Kein Urteil über die Personen: Die Linie zeigt Abstand, nicht Schuld"],
  distinct=["FIG-ZEICHEN-ABLEHNEN"])
E("FIG-ZEICHEN-HOCHZEIT", "sign", "Hochzeit / Fest", "Wedding / feast",
  "Bedeutung: Ort und Anlass ist ein Hochzeitsfest (z. B. [[JHN.2.1]]).",
  "Bedüütig: Ort und Aalass isch es Hochziitsfäscht (z. B. [[JHN.2.1]]).",
  [T("Grüne Girlande mit roten Blüten über dem Brautpaar", "design"), T("Festtafel", "design")],
  ("#6E8B3D", "#D4537E"), ["Nur zusammen mit Braut und Bräutigam oder Festtafel"])
E("FIG-ZEICHEN-TAGE", "sign", "Tage zählen", "Counting days",
  "Bedeutung: Eine Zahl von Tagen, z. B. «in drei Tagen» ([[JHN.2.19]]): so viele Sonnen wie Tage.",
  "Bedüütig: E Zaal vo Täg, z. B. «i drüü Täg» ([[JHN.2.19]]): so vil Sunne wie Täg.",
  [T("Kleine Sonnen in einer Reihe, je eine pro Tag", "design")],
  ("#F2C76E", "#D9A441"), ["Nicht mit dem Zeichen-Stern verwechseln (Sonne mit Strahlen, Stern mit vier Spitzen)", "Für Stunde/Zeit allgemein die Sanduhr"],
  distinct=["FIG-ZEICHEN-STERN", "FIG-ZEICHEN-STUNDE"])
E("FIG-ZEICHEN-NIEDERREISSEN", "sign", "niederreissen / zerstören", "tear down / destroy",
  "Bedeutung: Etwas wird abgerissen oder zerstört (z. B. «Reisst diesen Tempel nieder», [[JHN.2.19]]).",
  "Bedüütig: Öppis wird abgrisse oder zerstört (z. B. «Riissed dä Tämpel ab», [[JHN.2.19]]).",
  [T("Gebäude mit Riss", "design")],
  ("#8C8070", "#3B3226"), ["Zeigt den Vorgang, nicht, wer ihn ausführt"])
E("FIG-SYMBOL-ADLER", "sign", "Adler (Symbol des Evangelisten Johannes)", "Eagle (symbol of John the Evangelist)",
  "Bedeutung: Seit der Alten Kirche steht der Adler für das Johannesevangelium (nach [[REV.4.7]] und [[EZK.1.10]], Zuordnung durch die Tradition).",
  "Bedüütig: Sit de Alte Chile staat de Adler für s Johannesevangelium (nach [[REV.4.7]] und [[EZK.1.10]], d Zuedornig macht d Tradition).",
  [T("Adler mit ausgebreiteten Flügeln, ganz braun mit goldbraunem Nacken, gebogenem gelbem Schnabel (Steinadler)", "design", note="Nicht weisser Kopf und Schwanz: das läse sich als Weisskopfseeadler, ein nationales Wappentier (Blindtest 2026-10-14)"),
   T("Zuordnung zu Johannes", "tradition", note="Irenäus und spätere Tradition; die Zuordnung der vier Wesen zu den Evangelisten war nicht immer gleich")],
  ("#7A5230", "#E8D9B0"), ["Nicht mit der Taube (Heiliger Geist) verwechseln: Adler braun mit Hakenschnabel, Taube weiss mit Kreuznimbus"],
  distinct=["FIG-HEILIGER-GEIST", "FIG-OBJ-TAUBE"])
E("FIG-ZEICHEN-LICHT", "sign", "Licht / Herrlichkeit", "Light / glory",
  "Bedeutung: Licht, Herrlichkeit, Offenbarung (z. B. «das Licht der Menschen», [[JHN.1.4]]; «er offenbarte seine Herrlichkeit», [[JHN.2.11]]).",
  "Bedüütig: Liecht, Herrlichkeit, Offebarig (z. B. «s Liecht vo de Mänsche», [[JHN.1.4]]; «er hät sini Herrlichkeit offebaret», [[JHN.2.11]]).",
  [T("Heller goldener Schein mit funkelndem Kern", "design", note="Statt Scheibe mit Strahlen: diese wurde im Blindtest (2026-10-17) als Sonne gelesen")],
  ("#F2C76E", "#D9A441"), ["Nicht mit dem Kreuznimbus verwechseln (der gehört zu Personen)", "Keine Sonnenscheibe (Verwechslung mit Sonne und Gottessymbol)"], distinct=["FIG-ZEICHEN-STERN", "FIG-ZEICHEN-TAGE"])

# --- Obere Ebenen (Bibel, Testamente, Buchgruppen), 2026-10-14 ---
E("FIG-OBJ-GESETZESTAFELN", "object", "Gesetzestafeln", "Tablets of the law",
  "Die zwei steinernen Tafeln der Weisung am Sinai ([[EXO.31.18]], [[EXO.34.1]]); Zeichen für Bund und Tora.",
  "Di zwei steinige Tafle vo de Wiisig am Sinai ([[EXO.31.18]], [[EXO.34.1]]); Zeiche für de Bund und d Tora.",
  [T("Zwei steinerne Tafeln mit runden oberen Ecken", "tradition"), T("Zeilenstriche statt Schrift, keine Ziffern", "design")],
  ("#C9BFAA", "#8C8070"), ["Keine römischen Ziffern (spätere Bildtradition)"], distinct=["FIG-OBJ-SCHRIFTROLLE"])
E("FIG-ORT-MEER", "place", "Meer (geteilt beim Auszug)", "Sea (parted at the Exodus)",
  "Das Meer, durch das Israel beim Auszug aus Ägypten auf trockenem Boden zieht ([[EXO.14.21-EXO.14.22]]).",
  "S Meer, wo Israel bim Uszug us Ägypte uf tröchnem Bode dureziet ([[EXO.14.21-EXO.14.22]]).",
  [T("Zwei blaue Wasserwände mit Wellen, dazwischen ein heller Weg", "text", ref="EXO.14.22")],
  ("#4C9BD6", "#D8CBB0"), ["Nicht mit dem See (Galiläa) verwechseln"], distinct=["FIG-ORT-SEE"])
E("FIG-ZEICHEN-SCHOEPFUNG", "sign", "Schöpfung", "Creation",
  "Bedeutung: Gott erschafft Himmel und Erde ([[GEN.1.1]]): Erde mit Pflanzen, Sonne, Mond und Sterne.",
  "Bedüütig: Gott erschafft Himmel und Erde ([[GEN.1.1]]): Erde mit Pflanze, Sunne, Mond und Stärn.",
  [T("Grüner Erdhügel mit Pflanze, darüber Sonne, Mondsichel und kleine Sterne", "design")],
  ("#6E8B3D", "#F2C76E"), ["Sterne hier als Punkte, nicht als vierzackiger Zeichen-Stern"], distinct=["FIG-ZEICHEN-STERN", "FIG-ZEICHEN-NEUE-SCHOEPFUNG"])
E("FIG-ROLLE-PROPHET", "role", "Prophet / Prophetin", "Prophet",
  "Eine Person, die im Namen Gottes spricht, Unrecht anklagt und Hoffnung ankündigt (z. B. [[ISA.6.8]], [[AMO.5.24]]).",
  "E Person, wo im Name vo Gott redt, Unrächt aaklagt und Hoffnig aachündet (z. B. [[ISA.6.8]], [[AMO.5.24]]).",
  [T("Dunkler, rauer Mantel", "tradition", note="nach [[ZEC.13.4]] und [[2KI.1.8]]"), T("Schriftrolle in der Hand, die andere Hand erhoben", "design")],
  ("#5B4E3C", "#E7DCC4"), ["Ohne Nimbus", "Benannte Propheten (Elija, Jona, Obadja) mit eigenem Eintrag"], era="any", distinct=["FIG-MOSE", "FIG-ELIJA"])
E("FIG-OBJ-LEIER", "object", "Leier (Harfe)", "Lyre (harp)",
  "Saiteninstrument für Lieder und Gebete, das Instrument Davids ([[1SA.16.23]], [[PSA.33.2]]); Zeichen für Psalmen und Dichtung. Hebräisch כִּנּוֹר (kinnor).",
  "Saiteinstrumänt für Lieder und Gebät, s Instrumänt vom David ([[1SA.16.23]], [[PSA.33.2]]); Zeiche für Psalme und Dichtig. Hebräisch כִּנּוֹר (kinnor).",
  [T("Leier mit zwei Armen und Querholz, vier bis fünf Saiten", "design")],
  ("#B07A3E", "#F4F1EA"), [],
  terms=[{"lang": "heb", "word": "כִּנּוֹר", "translit": "kinnor", "de": "Leier, Harfe"}])
E("FIG-ZEICHEN-HOFFNUNG", "sign", "Hoffnung / Neubeginn", "Hope / new beginning",
  "Bedeutung: Aus dem Abgehauenen wächst Neues (nach [[ISA.11.1]]: ein Spross aus dem Stumpf Isais).",
  "Bedüütig: Us em Abghauene wachst Nöis (nach [[ISA.11.1]]: en Schoss us em Stumpe vom Isai).",
  [T("Baumstumpf mit grünem Spross", "text", ref="ISA.11.1")],
  ("#8A6A3A", "#6E8B3D"), [])
E("FIG-ZEICHEN-UMKEHR", "action", "umkehren", "turn back / repent",
  "Bedeutung: Menschen kehren um, wenden sich (wieder) Gott zu (z. B. [[JON.3.10]], [[HOS.14.2]]).",
  "Bedüütig: Mänsche chered um, wänded sich (wider) Gott zue (z. B. [[JON.3.10]], [[HOS.14.2]]).",
  [T("Pfeil, der im Bogen umkehrt", "design")],
  ("#3B3226", "#6E8B3D"), [], distinct=["FIG-ZEICHEN-BRINGEN"])
E("FIG-ZEICHEN-GERICHT", "sign", "Gericht / Gerechtigkeit", "Judgement / justice",
  "Bedeutung: Gott richtet und schafft Recht (z. B. [[AMO.5.24]], [[REV.20.12]]); gewogen werden ([[DAN.5.27]]).",
  "Bedüütig: Gott richtet und schafft Rächt (z. B. [[AMO.5.24]], [[REV.20.12]]); gwoge wärde ([[DAN.5.27]]).",
  [T("Waage mit zwei Schalen", "tradition")],
  ("#8C8070", "#D9A441"), ["Keine Darstellung von Strafen oder Gewalt"])
E("FIG-ZEICHEN-NEUE-SCHOEPFUNG", "sign", "Neue Schöpfung / neues Jerusalem", "New creation / new Jerusalem",
  "Bedeutung: Hoffnung auf einen neuen Himmel und eine neue Erde, die Stadt im Licht mit Strom und Baum des Lebens ([[REV.21.1-REV.21.2]], [[REV.22.1-REV.22.2]]).",
  "Bedüütig: Hoffnig uf en nöie Himmel und e nöii Erde, d Stadt im Liecht mit Strom und Baum vom Läbe ([[REV.21.1-REV.21.2]], [[REV.22.1-REV.22.2]]).",
  [T("Helle Stadt mit Toren im goldenen Licht", "text", ref="REV.21.23"), T("Blauer Strom und grüner Baum davor", "text", ref="REV.22.2")],
  ("#F7DB9A", "#4C9BD6"), [], distinct=["FIG-ORT-JERUSALEM", "FIG-ZEICHEN-SCHOEPFUNG"])
E("FIG-ZEICHEN-EXIL", "sign", "Wegführung und Rückkehr", "Exile and return",
  "Bedeutung: Das Volk wird aus dem Land weggeführt und kehrt später zurück ([[2KI.25.11]], [[EZR.1.3]]).",
  "Bedüütig: S Volk wird us em Land wäggfüert und chunnt spöter zrugg ([[2KI.25.11]], [[EZR.1.3]]).",
  [T("Weg mit zwei Pfeilen: dunkel weg vom Ort, gestrichelt zurück", "design")],
  ("#8C8070", "#3B3226"), [], distinct=["FIG-ZEICHEN-UMKEHR"])
E("FIG-ZEICHEN-AUSBREITEN", "action", "sich ausbreiten / hinausgehen", "spread out / go out",
  "Bedeutung: Die Botschaft geht von einem Ort aus in viele Richtungen ([[ACT.1.8]]).",
  "Bedüütig: D Botschaft gaat vo eim Ort uus i vili Richtige ([[ACT.1.8]]).",
  [T("Mehrere Pfeile, die von einem Punkt fächerförmig ausgehen", "design")],
  ("#3B3226", "#D9A441"), [], distinct=["FIG-ZEICHEN-BRINGEN"])
E("FIG-OBJ-BRIEF", "object", "Brief", "Letter",
  "Ein Brief an eine Gemeinde oder eine Person (z. B. [[PHP.1.1]], [[3JN.1.1]]).",
  "En Brief a e Gmeind oder e Person (z. B. [[PHP.1.1]], [[3JN.1.1]]).",
  [T("Dreifach gefaltetes Blatt mit sichtbaren Faltkanten, Zeilen in Handschrift und rotem Siegel", "design")],
  ("#F4F1EA", "#A33A2E"), ["Für Bücher und Schriftrollen FIG-OBJ-SCHRIFTROLLE", "Kein flaches Blatt mit umgeknickter Ecke (wird als Urkunde oder Schuldschein gelesen)"],
  distinct=["FIG-OBJ-SCHRIFTROLLE", "FIG-ZEICHEN-SCHULD"])
E("FIG-GRUPPE-GEMEINDE", "group", "Gemeinde", "Congregation / church",
  "Menschen, die sich im Namen Jesu versammeln, oft in einem Haus ([[ROM.16.5]], [[PHM.1.2]]).",
  "Mänsche, wo sich im Name vo Jesus versammled, mängisch imene Huus ([[ROM.16.5]], [[PHM.1.2]]).",
  [T("Gruppe vor einem Haus, Männer und Frauen", "text", ref="ROM.16.5")],
  ("#8E9AAF", "#E2CDA8"), ["Kein Kirchengebäude (Hausgemeinden zur Zeit der Briefe)"], distinct=["FIG-GRUPPE-MENGE"])

# ---------------------------------------------------------------------------------------------------------------
# Weitere Einträge aus bildlexikon_daten/*.json (für die Bilder aller übersetzten Bücher, ab 2026-10-17)
# Aufbau je Eintrag: id, kind, de, en, ident, gsw, traits [{trait_de, basis, ref?, note_de?}], pal [2 Farben], rules [],
# era?, find? [[Muster, [Bereiche]]], distinct? [], terms?
# ---------------------------------------------------------------------------------------------------------------
def load_extra():
    for f in sorted((pathlib.Path(__file__).resolve().parent / "bildlexikon_daten").glob("[!_]*.json")):
        for x in json.loads(f.read_text(encoding="utf-8")):
            traits = [T(t["trait_de"], t["basis"], t.get("ref"), t.get("note_de")) for t in x["traits"]]
            find = [(a, b) for a, b in x["find"]] if x.get("find") else None
            E(x["id"], x["kind"], x["de"], x["en"], x["ident"], x["gsw"], traits, tuple(x["pal"]), x.get("rules", []),
              era=x.get("era"), find=find, distinct=x.get("distinct", []), terms=x.get("terms"))


load_extra()


def run():
    texts = load_texts()
    ids = [e["id"] for e in ENTRIES]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit(f"Doppelte IDs: {sorted(dup)}")
    for e in ENTRIES:
        for d in e["distinct"]:
            if d not in ids:
                raise SystemExit(f"{e['id']}: distinct_from {d} unbekannt")
    n, kinds = 0, {}
    for e in ENTRIES:
        rec = build(e, texts)
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
        n += write(OUT / f"{rec['id']}.json", rec)
        n += localize(rec["id"], rec, {"identity_de": e["gsw"]}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026", AUTH_GSW, DATE)
    summary = ", ".join(f"{k} {v}" for k, v in sorted(kinds.items()))
    print(f"PASS: Bildlexikon – {len(ENTRIES)} Einträge ({summary}); {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
