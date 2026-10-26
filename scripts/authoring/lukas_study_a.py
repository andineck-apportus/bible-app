#!/usr/bin/env python3
"""Autorenwerkzeug: Lukasevangelium Kapitel 1–12 – Befunde, Deutungen, Grundsätze, Anwendungen, offene Fragen,
Beziehungen, Hintergrund zu Abschnitten und Studie; jeweils mit Züridüütsch-Lokalisierung.

Nicht hier geschrieben (bestehen schon und bleiben unverändert, werden höchstens verwiesen):
- die Vaterunser-Datensätze zu [[LUK.11.1-LUK.11.4]] aus scripts/authoring/vaterunser.py (FIND-LP-…, INT-LP-…,
  BG-LP-0012, QUESTION-LP-0002, STUDY-LP-0001) und der Kontext CTX-LUK-READERS-0085;
- der Hintergrund zum ganzen Buch BG-LUK-BOOK-0001 (Verfasser, Datierung, Leserschaft; hintergrund_buecher.py);
- Hintergrund, der schon zu Matthäus, Markus oder Johannes geschrieben ist (z. B. BG-MAT-1001 Stammbäume, BG-MAT-2001
  Hauptmann, BG-MAT-2006 Klage, BG-MAT-4007 Zehnter, BG-MAT-4008 Gräber, BG-MAT-4009 Abel bis Secharja, BG-JHN-1005
  Samaritaner, BG-JHN-2012 zu Tisch liegen, BG-MRK-1003 Synagoge, BG-MRK-1010 Händewaschen, BG-MRK-2001 Weg nach
  Jericho): nur verwiesen.
- Keine Kapitel- oder Buchzusammenfassungen (SUM-CH-LUK-…, SUM-BOOK-LUK): Sie entstehen aus den Kernanalysen
  («Struktur zuerst», docs/VERDICHTUNG.md).

IDs dieses Werkzeugs: Nummern 0001–0499 (FIND-, INT-, PRIN-, APP-, QUESTION-, REL-, BG-LUK-0001 …; STUDY-LUK-0001).
Kontexte werden nur verwendet, nie geschrieben: run() liest CTX-LUK-READERS-0085 aus der Datei und gibt ihn unverändert
weiter, sodass _lib.write nichts ändert.

Abschnitte: Jede Aussage hängt an der kleinsten vorhandenen Texteinheit (data/text-units/TU-LUK-…), die den genannten
Versbereich ganz enthält, sonst an der Kapiteleinheit; kapitelübergreifende Aussagen an der Einheit ihres Kernverses.
Zählungen: nach den MACULA-Lemmata zum SBLGNT (data/annotations/MACULA-SBLGNT-LUK-0nn.json, für Vergleiche auch MAT,
MRK, JHN); run() prüft jede genannte Zahl gegen die Daten (ZAEHLUNGEN, GEIST, STAMMBAUM) und bricht bei Abweichung ab.
Die Markus-Zahlen schliessen [[MRK.16.9-MRK.16.20]] ein. Vergleiche mit Matthäus, Markus und Johannes sind ausdrücklich
als Vergleich gekennzeichnet; ausgegeben wird nur Lukas-Text.
Mundart: Schreibung nach scripts/authoring/lukas_einheitlich.py (pruefe_mundart).

Aufruf: python3 scripts/authoring/lukas_study_a.py
KI-Entwurf (Claude) vom 2026-10-26 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
"""
import json
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D  # noqa: E402

DATUM = "2026-10-26"
TAGS = ["TAG-LUKE"]
CHAPTERS = {1: "TU-LUK-001-001-080", 2: "TU-LUK-002-001-052", 3: "TU-LUK-003-001-038", 4: "TU-LUK-004-001-044",
            5: "TU-LUK-005-001-039", 6: "TU-LUK-006-001-049", 7: "TU-LUK-007-001-050", 8: "TU-LUK-008-001-056",
            9: "TU-LUK-009-001-062", 10: "TU-LUK-010-001-042", 11: "TU-LUK-011-001-054", 12: "TU-LUK-012-001-059"}
_UNITS = sorted(p.stem for p in (D / "text-units").rglob("TU-LUK-*.json"))
READERS = "CTX-LUK-READERS-0085"
GAL = "CTX-GALILEE-0030"
TEMPEL = "CTX-HIST-SECOND-TEMPLE"


def U(ch, v1, v2=None):
    """Kleinste vorhandene Texteinheit, die Kapitel ch, Verse v1–v2 ganz enthält; sonst die Kapiteleinheit."""
    v2 = v2 or v1
    if ch == 11 and v1 <= 4:
        raise SystemExit("[[LUK.11.1-LUK.11.4]] gehört zu vaterunser.py, nicht zu diesem Werkzeug")
    best = None
    for uid in _UNITS:
        m = re.fullmatch(r"TU-LUK-(\d{3})-(\d{3})-(\d{3})", uid)
        if m and int(m[1]) == ch and int(m[2]) <= v1 and int(m[3]) >= v2:
            if best is None or int(m[3]) - int(m[2]) < best[0]:
                best = (int(m[3]) - int(m[2]), uid)
    return best[1] if best else CHAPTERS[ch]


MAC = "Zählung nach den MACULA-Lemmata zum SBLGNT."
MAC_G = "Zellig nach de MACULA-Lemmata zum SBLGNT."

ALLE = {"LUK": ((1, 1), (24, 53)), "MAT": ((1, 1), (28, 20)), "MRK": ((1, 1), (16, 20)), "JHN": ((1, 1), (21, 25))}


def _ganz(buch, lemma, soll):
    return (buch, lemma) + ALLE[buch] + (soll,)


# Jede im Text genannte Zahl: (Buch, Lemma, (Kapitel, Vers) von, (Kapitel, Vers) bis, erwartete Zahl)
ZAEHLUNGEN = [
    _ganz("LUK", "καθεξῆς", 2), _ganz("MAT", "καθεξῆς", 0), _ganz("MRK", "καθεξῆς", 0), _ganz("JHN", "καθεξῆς", 0),
    _ganz("LUK", "αὐτόπτης", 1), _ganz("MAT", "αὐτόπτης", 0), _ganz("MRK", "αὐτόπτης", 0), _ganz("JHN", "αὐτόπτης", 0),
    ("LUK", "ἔλεος", (1, 1), (1, 80), 5), _ganz("LUK", "ἔλεος", 6),
    ("LUK", "μακάριος", (6, 20), (6, 22), 4), ("LUK", "οὐαί", (6, 24), (6, 26), 4), ("LUK", "νῦν", (6, 20), (6, 26), 4),
    _ganz("LUK", "σήμερον", 11), _ganz("MRK", "σήμερον", 1), _ganz("MAT", "σήμερον", 8),
    _ganz("LUK", "προσεύχομαι", 19), _ganz("MRK", "προσεύχομαι", 10), _ganz("MAT", "προσεύχομαι", 15),
    _ganz("LUK", "ἐπιστάτης", 7), ("LUK", "ἐπιστάτης", (5, 1), (9, 62), 6), _ganz("MAT", "ἐπιστάτης", 0),
    _ganz("MRK", "ἐπιστάτης", 0),
    _ganz("LUK", "εὐαγγελίζω", 10), _ganz("MAT", "εὐαγγελίζω", 1), _ganz("MRK", "εὐαγγελίζω", 0),
    _ganz("LUK", "εὐαγγέλιον", 0), _ganz("MRK", "εὐαγγέλιον", 8),
    _ganz("LUK", "χήρα", 9), _ganz("MRK", "χήρα", 3), _ganz("MAT", "χήρα", 0), ("LUK", "χήρα", (1, 1), (12, 59), 4),
    ("LUK", "ἀγαπάω", (6, 27), (6, 36), 6),
    _ganz("LUK", "Ἠλίας", 7), ("LUK", "Ἠλίας", (1, 1), (9, 62), 7),
    _ganz("LUK", "Ἰερουσαλήμ", 27), _ganz("LUK", "Ἱεροσόλυμα", 4),
    _ganz("LUK", "Σαμαρίτης", 3), _ganz("MAT", "Σαμαρίτης", 1), _ganz("MRK", "Σαμαρίτης", 0),
    _ganz("LUK", "σπλαγχνίζομαι", 3),
    ("LUK", "ποιέω", (10, 25), (10, 37), 4),
    ("LUK", "πόσος", (11, 1), (12, 59), 3),
    ("LUK", "οὐαί", (11, 42), (11, 52), 6),
    _ganz("LUK", "πλεονεξία", 1), _ganz("MRK", "πλεονεξία", 1), _ganz("MAT", "πλεονεξία", 0), _ganz("JHN", "πλεονεξία", 0),
    ("LUK", "ἐγώ", (12, 17), (12, 19), 4), ("LUK", "ψυχή", (12, 19), (12, 23), 5),
    ("LUK", "μεριμνάω", (12, 22), (12, 26), 3),
    ("LUK", "ἀκούω", (8, 4), (8, 21), 9),
    _ganz("LUK", "ἀγαλλιάω", 2),
]
# «heiliger Geist»: πνεῦμα mit ἅγιος im selben Vers, höchstens drei Wörter Abstand (FIND-LUK-0003)
GEIST = [("LUK", (1, 1), (4, 44), 9), ("LUK", (1, 1), (24, 53), 13), ("MRK", (1, 1), (16, 20), 4),
         ("MAT", (1, 1), (28, 20), 5)]
# Eigennamen im Stammbaum [[LUK.3.23-LUK.3.38]] ohne «Gott» (FIND-LUK-0025)
STAMMBAUM = 77

# (id, Abschnitt, Art, Aussage, Belege, Konfidenz, Begründung | Mundart: Aussage, Begründung)
FINDINGS = [
 ("FIND-LUK-0001", U(1, 1, 4), "literary_structure",
  "[[LUK.1.1-LUK.1.4]] ist im Griechischen ein einziger, kunstvoll gebauter Satz: ein Vordersatz über die «vielen», die schon einen Bericht verfasst haben, und über die Augenzeugen, die überliefert haben ([[LUK.1.1-LUK.1.2]]), ein Hauptsatz über das eigene Vorhaben ([[LUK.1.3]]) und ein Zwecksatz für Theophilus ([[LUK.1.4]]). Der Verfasser nennt seinen Namen nicht, spricht aber in der Ich-Form und unterscheidet sich von den «Augenzeugen» (αὐτόπται, in den Evangelien nur hier). Er betont seine Sorgfalt: Er ist «allem von Anfang an genau nachgegangen» und schreibt «der Reihe nach» (καθεξῆς, in den Evangelien nur bei Lukas: [[LUK.1.3]]; [[LUK.8.1]]), damit Theophilus erkennt, «wie zuverlässig» (ἀσφάλεια) das Gelernte ist. Ab [[LUK.1.5]] wechselt der Ton: «Es gab in den Tagen des Herodes …» erzählt in einer Sprache, die an die griechische Bibel erinnert.",
  ["LUK.1.1-LUK.1.4", "LUK.1.5"], "high",
  MAC + " Dass der Ton ab [[LUK.1.5]] an die griechische Bibel erinnert (Satzanfänge, Wendungen wie «in den Tagen des …», die Erzählformel «es geschah»), ist eine verbreitete stilistische Beobachtung, keine Zählung.",
  "[[LUK.1.1-LUK.1.4]] isch im Griechische en einzige, kunschtvoll baute Satz: en Vordersatz über di «vile», wo scho en Bricht verfasst händ, und über d Augezüüge, wo s überliferet händ ([[LUK.1.1-LUK.1.2]]), en Hauptsatz über s eige Vorhaa ([[LUK.1.3]]) und en Zwecksatz für de Theophilus ([[LUK.1.4]]). De Verfasser nännt sin Name nöd, redt aber i de Ich-Form und underscheidet sich vo de «Augezüüge» (αὐτόπται, i de Evangelie nu da). Er betont sini Sorgfalt: Er isch «allem vo Aafang aa gnau nachegange» und schriibt «der Reie naa» (καθεξῆς, i de Evangelie nu bim Lukas: [[LUK.1.3]]; [[LUK.8.1]]), demit de Theophilus erchännt, «wie zueverlässig» (ἀσφάλεια) das isch, won er glehrt hät. Ab [[LUK.1.5]] wächslet de Ton: «Es hät i de Täg vom Herodes … ggää» verzellt i ere Spraach, wo a di griechisch Bible erinneret.",
  MAC_G + " Dass de Ton ab [[LUK.1.5]] a di griechisch Bible erinneret (Satzaafäng, Wändige wie «i de Täg vom …», d Erzählformle «es isch gsii»), isch e verbreiteti Beobachtig am Stil, kei Zellig."),
 ("FIND-LUK-0002", U(1, 26, 38), "literary_structure",
  "Die Kapitel 1–2 stellen Johannes und Jesus in Parallelen nebeneinander. Zweimal kündigt der Engel Gabriel eine Geburt an ([[LUK.1.11-LUK.1.20]]; [[LUK.1.26-LUK.1.38]]): Der Angesprochene erschrickt, hört «Fürchte dich nicht», erfährt den Namen des Kindes und was aus ihm wird, und fragt zurück ([[LUK.1.18]]; [[LUK.1.34]]). Es folgen die beiden Geburten mit Beschneidung und Namengebung ([[LUK.1.57-LUK.1.66]]; [[LUK.2.1-LUK.2.21]]), je ein Lobgesang ([[LUK.1.67-LUK.1.79]]; [[LUK.2.29-LUK.2.32]]) und eine Notiz über das Heranwachsen ([[LUK.1.80]]; [[LUK.2.40]]; [[LUK.2.52]]). Die Parallelen sind nicht gleichwertig: Zacharias wird für seine Frage stumm ([[LUK.1.20]]), Maria nicht; Johannes wird «gross sein vor dem Herrn» ([[LUK.1.15]]) und «Prophet des Höchsten» heissen ([[LUK.1.76]]), Jesus «gross» und «Sohn des Höchsten» ([[LUK.1.32]]). Dazwischen begegnen sich die beiden Mütter, und das ungeborene Kind der Elisabet «hüpft» vor Freude ([[LUK.1.39-LUK.1.45]]).",
  ["LUK.1.5-LUK.1.25", "LUK.1.26-LUK.1.38", "LUK.1.57-LUK.1.80", "LUK.2.1-LUK.2.52"], "high",
  "Beobachtung am Wortlaut. Wie weit die Parallelen als bewusstes Schema gemeint sind (oft «Diptychon» genannt) und wo sie enden, wird unterschiedlich abgegrenzt.",
  "D Kapitel 1–2 stelled de Johannes und de Jesus i Parallele nebenand. Zwei Mal chündet de Ängel Gabriel e Geburt aa ([[LUK.1.11-LUK.1.20]]; [[LUK.1.26-LUK.1.38]]): Wär aagredt wird, verschrickt, ghört «Häb kei Angscht», erfaart de Name vom Chind und was us ihm wird, und fröget zrugg ([[LUK.1.18]]; [[LUK.1.34]]). Dänn chömed di beide Geburte mit Beschniidig und Namegäbig ([[LUK.1.57-LUK.1.66]]; [[LUK.2.1-LUK.2.21]]), je es Loblied ([[LUK.1.67-LUK.1.79]]; [[LUK.2.29-LUK.2.32]]) und e Notiz über s Ufwachse ([[LUK.1.80]]; [[LUK.2.40]]; [[LUK.2.52]]). D Parallele sind nöd gliichwärtig: De Zacharias wird für sini Frag stumm ([[LUK.1.20]]), d Maria nöd; de Johannes wird «gross sii vor em Herr» ([[LUK.1.15]]) und «Prophet vom Höchschte» heisse ([[LUK.1.76]]), de Jesus «gross» und «Sohn vom Höchschte» ([[LUK.1.32]]). Dezwüsche begägned sich di beide Müetere, und s ungeborne Chind vo de Elisabet macht vor Fröid «en Gump» ([[LUK.1.39-LUK.1.45]]).",
  "Beobachtig am Wortluut. Wie wiit d Parallele als bewusst Schema gmeint sind (mängisch «Diptychon» gnännt) und wo s ufhöred, wird verschide abgränzt."),
 ("FIND-LUK-0003", U(4, 14, 30), "key_terms",
  "Die Wendung «heiliger Geist» (πνεῦμα ἅγιον) steht in [[LUK.1.1-LUK.4.44]] neun Mal, im ganzen Lukasevangelium 13 Mal; zum Vergleich: im ganzen Markusevangelium vier Mal, bei Matthäus fünf Mal. In den Kapiteln 1–2 werden Menschen «mit heiligem Geist erfüllt» und reden dann prophetisch: Johannes schon im Mutterleib ([[LUK.1.15]]), Elisabet ([[LUK.1.41-LUK.1.42]]), Zacharias ([[LUK.1.67]]); auf Simeon «ruhte» heiliger Geist, und er kommt «im Geist» in den Tempel ([[LUK.2.25-LUK.2.27]]). Bei Jesus ist der Geist Ursprung ([[LUK.1.35]]), kommt bei der Taufe auf ihn herab ([[LUK.3.22]]), führt ihn in die Wüste und nach Galiläa ([[LUK.4.1]]; [[LUK.4.14]]) und ist Inhalt seiner ersten Predigt: «Der Geist des Herrn ist auf mir» ([[LUK.4.18]]).",
  ["LUK.1.15", "LUK.1.35", "LUK.1.41", "LUK.1.67", "LUK.2.25-LUK.2.27", "LUK.3.16", "LUK.3.22", "LUK.4.1", "LUK.4.14", "LUK.4.18"], "high",
  MAC + " Gezählt ist πνεῦμα mit ἅγιος im selben Vers in höchstens drei Wörtern Abstand; nicht mitgezählt sind «im Geist» ohne «heilig» ([[LUK.2.27]]; [[LUK.4.1]]; [[LUK.4.14]]) und «der Geist des Herrn» ([[LUK.4.18]]).",
  "D Wändig «heilige Geischt» (πνεῦμα ἅγιον) staat i [[LUK.1.1-LUK.4.44]] nüün Mal, im ganze Lukasevangelium 13 Mal; zum Vergliich: im ganze Markusevangelium vier Mal, bim Matthäus föif Mal. I de Kapitel 1–2 wärded Mänsche «mit heilige Geischt erfüllt» und reded dänn prophetisch: de Johannes scho im Mueterliib ([[LUK.1.15]]), d Elisabet ([[LUK.1.41-LUK.1.42]]), de Zacharias ([[LUK.1.67]]); uf em Simeon isch heilige Geischt gsii, und er chunnt «im Geischt» in Tämpel ([[LUK.2.25-LUK.2.27]]). Bim Jesus isch de Geischt de Ursprung ([[LUK.1.35]]), chunnt bi de Taufi uf ihn abe ([[LUK.3.22]]), füert en i d Wüeschti und uf Galiläa ([[LUK.4.1]]; [[LUK.4.14]]) und isch de Inhalt vo sinere erschte Predig: «De Geischt vom Herr isch uf mir» ([[LUK.4.18]]).",
  MAC_G + " Zellt isch πνεῦμα mit ἅγιος im gliiche Värs mit höchschtens drüü Wörter Abstand; nöd mitzellt sind «im Geischt» ohni «heilig» ([[LUK.2.27]]; [[LUK.4.1]]; [[LUK.4.14]]) und «de Geischt vom Herr» ([[LUK.4.18]])."),
 ("FIND-LUK-0004", U(1, 39, 56), "key_terms",
  "In [[LUK.1.5-LUK.2.52]] stehen vier poetische Stücke, die nach ihren lateinischen Anfangsworten bekannt sind: Marias Lobgesang (Magnificat, [[LUK.1.46-LUK.1.55]]), der Lobgesang des Zacharias (Benedictus, [[LUK.1.68-LUK.1.79]]), der Gesang der Engel (Gloria, [[LUK.2.14]]) und das Gebet Simeons (Nunc dimittis, [[LUK.2.29-LUK.2.32]]). Sie sind aus parallelen Zeilen gebaut wie die Psalmen und voller Anklänge an die Schrift; Marias Lied erinnert besonders an das Lied der Hanna ([[1SA.2.1-1SA.2.10]]). Gemeinsame Stichworte sind Rettung und Retter (σωτηρία, σωτήρ: [[LUK.1.47]]; [[LUK.1.69]]; [[LUK.1.71]]; [[LUK.1.77]]; vgl. [[LUK.2.11]]; [[LUK.2.30]]), Barmherzigkeit (ἔλεος, fünf Mal in Kapitel 1, im ganzen Lukasevangelium sechs Mal), das Gedenken an die Zusage an Abraham ([[LUK.1.55]]; [[LUK.1.73]]) und der Friede ([[LUK.1.79]]; [[LUK.2.14]]; [[LUK.2.29]]). Die Verben in [[LUK.1.51-LUK.1.54]] stehen in der Vergangenheitsform, obwohl das Kind noch nicht geboren ist: Maria besingt, was Gott getan hat.",
  ["LUK.1.46-LUK.1.55", "LUK.1.68-LUK.1.79", "LUK.2.14", "LUK.2.29-LUK.2.32", "1SA.2.1-1SA.2.10"], "high",
  MAC + " Die Namen der Lieder stammen aus der lateinischen Kirchentradition. Ob die Lieder älter sind als das Evangelium und von Lukas aufgenommen wurden, ist umstritten.",
  "I [[LUK.1.5-LUK.2.52]] staat vier poetischi Stück, wo nach irne latiinische Aafangswort bekannt sind: s Loblied vo de Maria (Magnificat, [[LUK.1.46-LUK.1.55]]), s Loblied vom Zacharias (Benedictus, [[LUK.1.68-LUK.1.79]]), s Lied vo de Ängel (Gloria, [[LUK.2.14]]) und s Gebätt vom Simeon (Nunc dimittis, [[LUK.2.29-LUK.2.32]]). Si sind us parallele Ziile baut wie d Psalme und voll vo Aakläng a d Schrift; s Lied vo de Maria erinneret bsunders as Lied vo de Hanna ([[1SA.2.1-1SA.2.10]]). Gmeinsami Stichwort sind Rettig und Retter (σωτηρία, σωτήρ: [[LUK.1.47]]; [[LUK.1.69]]; [[LUK.1.71]]; [[LUK.1.77]]; vgl. [[LUK.2.11]]; [[LUK.2.30]]), Barmhärzigkeit (ἔλεος, föif Mal im Kapitel 1, im ganze Lukasevangelium sächs Mal), s Dänke a d Zuesag a de Abraham ([[LUK.1.55]]; [[LUK.1.73]]) und de Fride ([[LUK.1.79]]; [[LUK.2.14]]; [[LUK.2.29]]). D Verbe i [[LUK.1.51-LUK.1.54]] staat i de Vergangeheitsform, obwohl s Chind no nöd gebore isch: D Maria besingt, was Gott gmacht hät.",
  MAC_G + " D Näme vo de Lieder stammed us de latiinische Chilletradition. Öb d Lieder elter sind als s Evangelium und vom Lukas ufgnoo worde sind, isch umstritte."),
 ("FIND-LUK-0005", U(6, 20, 26), "repetition",
  "Die Umkehrung von oben und unten kehrt bei Lukas mehrfach wieder. Maria singt: «Er hat Mächtige von Thronen gestürzt und Niedrige erhöht. Hungrige hat er mit Gutem gefüllt und Reiche leer weggeschickt» ([[LUK.1.52-LUK.1.53]]). In der Feldrede stehen vier Seligpreisungen ([[LUK.6.20-LUK.6.22]]) vier Weherufen gegenüber ([[LUK.6.24-LUK.6.26]]), Zeile für Zeile entgegengesetzt: Arme – Reiche, die jetzt Hungernden – die jetzt Satten, die jetzt Weinenden – die jetzt Lachenden, die Gehassten – die, von denen alle gut reden. Die Seligpreisungen reden die Betroffenen direkt an («ihr Armen»), und das Wort «jetzt» (νῦν) steht vier Mal. Simeon sagt, das Kind sei «bestimmt zum Fall und zum Aufstehen vieler in Israel» ([[LUK.2.34]]); ähnlich klingt das Jesajawort, mit dem der Täufer auftritt: «Jedes Tal wird aufgefüllt und jeder Berg und Hügel erniedrigt» ([[LUK.3.5]]).",
  ["LUK.1.51-LUK.1.53", "LUK.2.34", "LUK.3.5", "LUK.6.20-LUK.6.26"], "high",
  MAC + " Die Weherufe haben in der Bergpredigt kein Gegenstück; dort lautet die erste Seligpreisung «Selig die Armen im Geist» (Vergleich mit [[MAT.5.3-MAT.5.12]]).",
  "D Umkehrig vo obe und unde chunnt bim Lukas meermaals vor. D Maria singt: «Er hät Mächtigi vo de Tröön gstürzt und Niedrigi erhöcht. Hungrigi hät er mit Guetem gfüllt und Riichi läär furtgschickt» ([[LUK.1.52-LUK.1.53]]). I de Fäldred staat vier Säligpriisige ([[LUK.6.20-LUK.6.22]]) vier Weheruef gägenüber ([[LUK.6.24-LUK.6.26]]), Ziile für Ziile entgägegsetzt: Armi – Riichi, die, wo jetzt Hunger händ – die, wo jetzt satt sind, die, wo jetzt briegged – die, wo jetzt lached, die, wo me hasst – die, vo dene alli guet reded. Die, wo gmeint sind, wärded diräkt aagredt («ir Arme»), und s Wort «jetzt» (νῦν) staat vier Mal. De Simeon seit, s Chind sig «bestimmt zum Fall und zum Ufstaa vo vile i Israel» ([[LUK.2.34]]); ähnlich tönt s Jesajawort, mit dem de Täufer uftritt: «Jedes Tal wird ufgfüllt, und jede Bärg und Hügel wird abtreit» ([[LUK.3.5]]).",
  MAC_G + " D Weheruef händ i de Bärgpredig kei Gägestück; dört heisst di erscht Säligpriisig «Sälig di Arme im Geischt» (Vergliich mit [[MAT.5.3-MAT.5.12]])."),
 ("FIND-LUK-0006", U(4, 14, 30), "key_terms",
  "Das Wort «heute» (σήμερον) steht im Lukasevangelium elf Mal, bei Markus einmal, bei Matthäus acht Mal. An entscheidenden Stellen kündigt es Heil als gegenwärtig an: «Heute ist euch in der Stadt Davids ein Retter geboren» ([[LUK.2.11]]), «Heute hat sich dieses Schriftwort erfüllt, vor euren Ohren» ([[LUK.4.21]]), «Wir haben heute Unglaubliches gesehen» ([[LUK.5.26]]); später beim Zöllner Zachäus ([[LUK.19.5]]; [[LUK.19.9]]) und am Kreuz ([[LUK.23.43]]). Daneben steht es im gewöhnlichen Sinn ([[LUK.12.28]]; [[LUK.13.32-LUK.13.33]]; [[LUK.22.34]]; [[LUK.22.61]]).",
  ["LUK.2.11", "LUK.4.21", "LUK.5.26", "LUK.19.5", "LUK.19.9", "LUK.23.43"], "high", MAC,
  "S Wort «hüt» (σήμερον) staat im Lukasevangelium elf Mal, bim Markus eimal, bim Matthäus acht Mal. A entscheidende Stelle chündet s aa, dass s Heil jetzt da isch: «Hüt isch eu i de Stadt vom David en Retter gebore worde» ([[LUK.2.11]]), «Hüt hät sich das Schriftwort erfüllt, vor eune Ohre» ([[LUK.4.21]]), «Mir händ hüt Unglaublichs gseh!» ([[LUK.5.26]]); spööter bim Zöllner Zachäus ([[LUK.19.5]]; [[LUK.19.9]]) und am Chrüüz ([[LUK.23.43]]). Denäbe staat s im gwöönliche Sinn ([[LUK.12.28]]; [[LUK.13.32-LUK.13.33]]; [[LUK.22.34]]; [[LUK.22.61]]).",
  MAC_G),
 ("FIND-LUK-0007", U(3, 1, 20), "names",
  "Lukas verankert seine Erzählung dreimal in der Zeitgeschichte: «in den Tagen des Herodes, des Königs von Judäa» ([[LUK.1.5]]); beim Erlass des Kaisers Augustus und der ersten Eintragung, «als Quirinius Statthalter von Syrien war» ([[LUK.2.1-LUK.2.2]]); und mit einer Datierung aus sieben Namen für das Auftreten des Täufers: Kaiser Tiberius (im fünfzehnten Jahr), Pontius Pilatus, Herodes, Philippus, Lysanias sowie die Hohepriester Hannas und Kajaphas ([[LUK.3.1-LUK.3.2]]). Auf diese Liste folgt die Formel der Prophetenberufung: «da erging das Wort Gottes an Johannes» ([[LUK.3.2]]; vgl. [[JER.1.1-JER.1.2]]). Auch das Alter Jesu, «etwa dreissig Jahre», nennt unter den Evangelien nur Lukas ([[LUK.3.23]]).",
  ["LUK.1.5", "LUK.2.1-LUK.2.2", "LUK.3.1-LUK.3.2", "LUK.3.23"], "high",
  "Beobachtung am Wortlaut. Zur geschichtlichen Einordnung der Angaben siehe BG-LUK-0003, BG-LUK-0009 und QUESTION-LUK-0001.",
  "De Lukas verankeret sini Erzälig drüü Mal i de Ziitgschicht: «i de Täg vom Herodes, em König vo Judäa» ([[LUK.1.5]]); bim Erlass vom Kaiser Augustus und de erschte Iitragig, «wo de Quirinius Statthalter vo Syrie gsii isch» ([[LUK.2.1-LUK.2.2]]); und mit ere Datierig us sibe Näme für s Uftrete vom Täufer: Kaiser Tiberius (im füfzähte Jahr), Pontius Pilatus, Herodes, Philippus, Lysanias und d Hoheprieschter Hannas und Kajaphas ([[LUK.3.1-LUK.3.2]]). Uf die Lischte folgt d Formle vo de Prophetebrüefig: «da isch s Wort vo Gott zum Johannes choo» ([[LUK.3.2]]; vgl. [[JER.1.1-JER.1.2]]). Au s Alter vo Jesus, «öppe drissg Jahr», nännt under de Evangelie nu de Lukas ([[LUK.3.23]]).",
  "Beobachtig am Wortluut. Wie mer d Aagaabe gschichtlich iiordnet, lueg BG-LUK-0003, BG-LUK-0009 und QUESTION-LUK-0001."),
 ("FIND-LUK-0008", U(4, 14, 30), "quotation",
  "Lukas stellt den Auftritt in Nazaret an den Anfang des Wirkens Jesu ([[LUK.4.16-LUK.4.30]]), obwohl nach [[LUK.4.23]] schon Taten in Kafarnaum bekannt sind; bei Markus steht die Ablehnung in der Heimat erst viel später (Vergleich mit [[MRK.6.1-MRK.6.6]]). Jesus liest aus Jesaja: [[ISA.61.1-ISA.61.2]], ergänzt um eine Zeile aus [[ISA.58.6]] («Zerschlagene in die Freiheit zu entlassen»). Die Lesung endet mitten im Satz von [[ISA.61.2]]: Nach dem «Gnadenjahr des Herrn» folgt bei Jesaja «und einen Tag der Vergeltung unseres Gottes»; das liest Jesus nicht. Seine Auslegung besteht aus einem Satz: «Heute hat sich dieses Schriftwort erfüllt» ([[LUK.4.21]]). Die Stimmung kippt, als er an Elija und Elischa erinnert, die zu einer Witwe in Sarepta und zum Syrer Naaman gesandt wurden, nicht zu Israeliten ([[LUK.4.25-LUK.4.27]]); man will ihn vom Berg hinabstürzen ([[LUK.4.28-LUK.4.30]]).",
  ["LUK.4.16-LUK.4.30", "ISA.61.1-ISA.61.2", "ISA.58.6", "1KI.17.8-1KI.17.16", "2KI.5.1-2KI.5.14"], "high",
  "Vergleich mit dem Jesajatext; die Ergänzung aus [[ISA.58.6]] und das Ende vor dem «Tag der Vergeltung» sind am Wortlaut sichtbar (siehe die Übersetzungsentscheidung zu [[LUK.4.18]]). Die Zeile «zu heilen, die zerbrochenen Herzens sind» aus [[ISA.61.1]] fehlt im SBLGNT; manche Handschriften haben sie (siehe Alternative). Ob Lukas den Auftritt bewusst vorgezogen hat oder eine eigene Überlieferung wiedergibt, ist Deutung (INT-LUK-0005).",
  "De Lukas stellt s Uftrete z Nazaret an Aafang vom Wirke vo Jesus ([[LUK.4.16-LUK.4.30]]), obwohl nach [[LUK.4.23]] scho Tate z Kafarnaum bekannt sind; bim Markus staat d Ablehnig i de Heimat erscht vil spööter (Vergliich mit [[MRK.6.1-MRK.6.6]]). De Jesus liist us em Jesaja: [[ISA.61.1-ISA.61.2]], ergänzt mit ere Ziile us [[ISA.58.6]] («Zerschlageni i d Freiheit laa»). D Läsig hört mitten im Satz vo [[ISA.61.2]] uf: Nach em «Gnadejahr vom Herr» chunnt bim Jesaja «und en Tag vo de Vergältig vo öisem Gott»; das liist de Jesus nöd. Sini Uslegig bestaat us eim Satz: «Hüt hät sich das Schriftwort erfüllt» ([[LUK.4.21]]). D Stimmig chippt, won er a de Elija und de Elischa erinneret, wo zu ere Witwe z Sarepta und zum Syrer Naaman gschickt worde sind, nöd zu Israelite ([[LUK.4.25-LUK.4.27]]); mer wott en vom Bärg abestürze ([[LUK.4.28-LUK.4.30]]).",
  "Vergliich mit em Jesajatext; d Ergänzig us [[ISA.58.6]] und s Änd vor em «Tag vo de Vergältig» gseht mer am Wortluut (lueg d Übersetzigsentscheidig zu [[LUK.4.18]]). D Ziile «zum die heile, wo es broches Härz händ» us [[ISA.61.1]] fäält im SBLGNT; mängi Handschrifte händ si (lueg d Alternative). Öb de Lukas s Uftrete bewusst vorezoge hät oder e eigeti Überliferig widergit, isch Düütig (INT-LUK-0005)."),
 ("FIND-LUK-0009", U(9, 28, 36), "key_terms",
  "Das Verb «beten» (προσεύχομαι) steht im Lukasevangelium 19 Mal, bei Markus 10 und bei Matthäus 15 Mal. In den Kapiteln 1–12 betet Jesus an Wendepunkten: bei der Taufe, als sich der Himmel öffnet ([[LUK.3.21]]); immer wieder in einsamen Gegenden ([[LUK.5.16]]); eine ganze Nacht vor der Wahl der Zwölf ([[LUK.6.12-LUK.6.13]]); vor der Frage «Wer, sagt ihr, bin ich?» ([[LUK.9.18]]); auf dem Berg, wo sich während des Betens sein Aussehen verändert ([[LUK.9.28-LUK.9.29]]); und bevor ihn die Jünger bitten: «Herr, lehre uns beten» ([[LUK.11.1]]). In [[LUK.10.21]] jubelt er «im Heiligen Geist» und preist den Vater. Bei Taufe und Verklärung erwähnt Markus das Beten nicht (Vergleich mit [[MRK.1.9-MRK.1.11]] und [[MRK.9.2-MRK.9.8]]).",
  ["LUK.3.21", "LUK.5.16", "LUK.6.12", "LUK.9.18", "LUK.9.28-LUK.9.29", "LUK.11.1", "LUK.10.21"], "high",
  MAC + " Die 19 Belege schliessen das Beten anderer ein (etwa [[LUK.1.10]]; [[LUK.18.10-LUK.18.11]]) und die Aufforderung an die Jünger ([[LUK.6.28]]); [[LUK.11.1]] hat zwei Belege.",
  "S Verb «bätte» (προσεύχομαι) staat im Lukasevangelium 19 Mal, bim Markus 10 und bim Matthäus 15 Mal. I de Kapitel 1–12 bättet de Jesus a Wändepünkt: bi de Taufi, wo sich de Himmel uftuet ([[LUK.3.21]]); immer wider i einsame Gägende ([[LUK.5.16]]); e ganzi Nacht vor de Waal vo de Zwölf ([[LUK.6.12-LUK.6.13]]); vor de Frag «Wär, säged ir, sig ich?» ([[LUK.9.18]]); uf em Bärg, wo sich bim Bätte sis Usgseh veränderet ([[LUK.9.28-LUK.9.29]]); und bevor en d Jünger bitted, er söll si s Bätte lehre ([[LUK.11.1]]). I [[LUK.10.21]] jublet er «im Heilige Geischt» und priist de Vatter. Bi de Taufi und bi de Verklärig erwäänt de Markus s Bätte nöd (Vergliich mit [[MRK.1.9-MRK.1.11]] und [[MRK.9.2-MRK.9.8]]).",
  MAC_G + " Di 19 Beleg schlüüssed s Bätte vo andere ii (öppe [[LUK.1.10]]; [[LUK.18.10-LUK.18.11]]) und d Ufforderig a d Jünger ([[LUK.6.28]]); [[LUK.11.1]] hät zwei Beleg."),
 ("FIND-LUK-0010", U(5, 1, 11), "key_terms",
  "Mit «Meister» (ἐπιστάτα) reden nur bei Lukas Menschen Jesus an: sieben Mal, davon sechs Mal in den Kapiteln 5–9 ([[LUK.5.5]]; [[LUK.8.24]] zweimal; [[LUK.8.45]]; [[LUK.9.33]]; [[LUK.9.49]]), sonst nur die zehn Aussätzigen ([[LUK.17.13]]). Matthäus und Markus haben das Wort nicht. Fast immer sprechen Jünger, oft in Not oder Unverständnis. Simon redet Jesus vor dem Fischfang «Meister» an und danach «Herr» (κύριε, [[LUK.5.5]]; [[LUK.5.8]]). Der Erzähler selbst nennt Jesus wiederholt «der Herr» ([[LUK.7.13]]; [[LUK.7.19]]; [[LUK.10.1]]; [[LUK.10.41]]; [[LUK.11.39]]; [[LUK.12.42]]).",
  ["LUK.5.5", "LUK.5.8", "LUK.8.24", "LUK.8.45", "LUK.9.33", "LUK.9.49", "LUK.17.13"], "high",
  MAC + " Die Stellen für «der Herr» im Erzähltext sind eine Auswahl, keine vollständige Zählung (siehe die Übersetzungsentscheidung zu [[LUK.10.1]]).",
  "Mit «Meischter» (ἐπιστάτα) reded nu bim Lukas Mänsche de Jesus aa: sibe Mal, sächs Mal devo i de Kapitel 5–9 ([[LUK.5.5]]; [[LUK.8.24]] zwei Mal; [[LUK.8.45]]; [[LUK.9.33]]; [[LUK.9.49]]), süscht nu di zää Ussätzige ([[LUK.17.13]]). De Matthäus und de Markus händ s Wort nöd. Fascht immer reded Jünger, oft i Not oder wänn si nöd verstönd. De Simon redt de Jesus vor em Fischfang mit «Meischter» aa und nachher mit «Herr» (κύριε, [[LUK.5.5]]; [[LUK.5.8]]). De Erzähler sälber nännt de Jesus immer wider «de Herr» ([[LUK.7.13]]; [[LUK.7.19]]; [[LUK.10.1]]; [[LUK.10.41]]; [[LUK.11.39]]; [[LUK.12.42]]).",
  MAC_G + " D Stelle für «de Herr» im Erzähltext sind e Uswaal, kei vollständigi Zellig (lueg d Übersetzigsentscheidig zu [[LUK.10.1]])."),
 ("FIND-LUK-0011", U(4, 31, 44), "key_terms",
  "Lukas gebraucht das Verb εὐαγγελίζομαι («gute Botschaft bringen, verkündigen») zehn Mal, Matthäus einmal, Markus nie; das Nomen «Evangelium» (εὐαγγέλιον), das bei Markus acht Mal steht, fehlt im Lukasevangelium ganz. Das Verb verbindet die Botschaft der Engel ([[LUK.1.19]]; [[LUK.2.10]]), des Täufers ([[LUK.3.18]]), Jesu ([[LUK.4.18]]; [[LUK.4.43]]; [[LUK.7.22]]; [[LUK.8.1]]) und der ausgesandten Zwölf ([[LUK.9.6]]). Zweimal sind ausdrücklich «Arme» die Empfänger ([[LUK.4.18]]; [[LUK.7.22]]); in [[LUK.4.43]] begründet Jesus damit seine Sendung: «dazu bin ich gesandt worden».",
  ["LUK.1.19", "LUK.2.10", "LUK.3.18", "LUK.4.18", "LUK.4.43", "LUK.7.22", "LUK.8.1", "LUK.9.6"], "high",
  MAC + " Die acht Markus-Belege schliessen [[MRK.16.15]] aus dem längeren Schluss ein. Die Übersetzung gibt das Verb je nach Satz verschieden wieder («gute Nachricht bringen», «die gute Botschaft verkünden», «das Evangelium verkünden»).",
  "De Lukas bruucht s Verb εὐαγγελίζομαι («e gueti Botschaft bringe, verchünde») zää Mal, de Matthäus eimal, de Markus nie; s Nomen «Evangelium» (εὐαγγέλιον), wo bim Markus acht Mal staat, fäält im Lukasevangelium ganz. S Verb verbindet d Botschaft vo de Ängel ([[LUK.1.19]]; [[LUK.2.10]]), vom Täufer ([[LUK.3.18]]), vo Jesus ([[LUK.4.18]]; [[LUK.4.43]]; [[LUK.7.22]]; [[LUK.8.1]]) und vo de Zwölf, won er usgschickt hät ([[LUK.9.6]]). Zwei Mal sind usdrücklich «Armi» die, wo d Botschaft überchömed ([[LUK.4.18]]; [[LUK.7.22]]); i [[LUK.4.43]] begründet de Jesus demit sini Sändig: «dezue bin ich gschickt worde».",
  MAC_G + " Di acht Beleg bim Markus schlüüssed [[MRK.16.15]] us em längere Schluss ii. D Übersetzig git s Verb je nach Satz verschide wider («di gueti Nachricht bringe», «di gueti Botschaft verchünde», «s Evangelium verchünde»)."),
 ("FIND-LUK-0012", U(8, 1, 3), "repetition",
  "Lukas stellt oft eine Erzählung über einen Mann und eine über eine Frau nebeneinander: Zacharias und Maria erhalten eine Ankündigung ([[LUK.1.5-LUK.1.38]]), Simeon und Hanna begrüssen das Kind im Tempel ([[LUK.2.25-LUK.2.38]]), Jesus erinnert an die Witwe von Sarepta und an Naaman ([[LUK.4.25-LUK.4.27]]), er heilt den Knecht des Hauptmanns und erweckt den Sohn der Witwe von Nain ([[LUK.7.1-LUK.7.17]]); auf den Samaritaner folgen Marta und Maria ([[LUK.10.25-LUK.10.42]]). Witwen (χήρα) erwähnt Lukas neun Mal, in den Kapiteln 1–12 vier Mal; bei Markus stehen sie drei Mal, bei Matthäus nie. Schon während des Wirkens in Galiläa erzählt Lukas von Frauen, die mit Jesus und den Zwölf umherzogen und sie «mit ihrem Besitz unterstützten»: Maria Magdalena, Johanna, die Frau eines Verwalters des Herodes, Susanna «und viele andere» ([[LUK.8.1-LUK.8.3]]); bei Markus kommen solche Frauen erst unter dem Kreuz in den Blick (Vergleich mit [[MRK.15.40-MRK.15.41]]).",
  ["LUK.1.5-LUK.1.38", "LUK.2.25-LUK.2.38", "LUK.4.25-LUK.4.27", "LUK.7.1-LUK.7.17", "LUK.8.1-LUK.8.3", "LUK.10.25-LUK.10.42"], "high",
  MAC + " Ob die Paarungen ein bewusstes Gestaltungsmittel sind, wird unterschiedlich beurteilt; welche Stellen dazugehören, ist eine Auswahl.",
  "De Lukas stellt oft e Gschicht über en Maa und eini über e Frau nebenand: De Zacharias und d Maria überchömed e Aakündigung ([[LUK.1.5-LUK.1.38]]), de Simeon und d Hanna begrüessed s Chind im Tämpel ([[LUK.2.25-LUK.2.38]]), de Jesus erinneret a d Witwe vo Sarepta und a de Naaman ([[LUK.4.25-LUK.4.27]]), er heilt de Chnächt vom Hauptmaa und weckt de Sohn vo de Witwe vo Nain uf ([[LUK.7.1-LUK.7.17]]); uf de Samaritaner folged d Marta und d Maria ([[LUK.10.25-LUK.10.42]]). Witwe (χήρα) erwäänt de Lukas nüün Mal, i de Kapitel 1–12 vier Mal; bim Markus staat si drüü Mal, bim Matthäus nie. Scho wäred em Wirke z Galiläa verzellt de Lukas vo Fraue, wo mit em Jesus und de Zwölf umezoge sind und si «mit irem Bsitz understützt händ»: d Maria vo Magdala, d Johanna, d Frau vo eme Verwalter vom Herodes, d Susanna «und vili anderi» ([[LUK.8.1-LUK.8.3]]); bim Markus chömed settigi Fraue erscht under em Chrüüz in Blick (Vergliich mit [[MRK.15.40-MRK.15.41]]).",
  MAC_G + " Öb d Paarige es bewussts Mittel vo de Gstaltig sind, wird verschide beurteilt; weli Stelle dezueghöred, isch e Uswaal."),
 ("FIND-LUK-0013", U(6, 20, 49), "parallel_comparison",
  "Die Feldrede ([[LUK.6.20-LUK.6.49]]) hält Jesus nach dem Abstieg vom Berg «auf einem ebenen Platz» ([[LUK.6.17]]), vor den Jüngern und einer grossen Menge aus Judäa, Jerusalem und dem Küstengebiet von Tyrus und Sidon. Sie umfasst 30 Verse und folgt im Ganzen derselben Ordnung wie die Bergpredigt bei Matthäus (Vergleich mit [[MAT.5.1-MAT.7.29]], 111 Verse): Seligpreisungen am Anfang, Feindesliebe, Nicht-Richten, Baum und Frucht, das Haus auf dem Felsen am Schluss. Im Mittelpunkt steht die Feindesliebe: «Liebt eure Feinde» rahmt [[LUK.6.27-LUK.6.35]], das Verb «lieben» (ἀγαπάω) steht in [[LUK.6.27-LUK.6.36]] sechs Mal, und der Abschnitt mündet in «Seid barmherzig, wie euer Vater barmherzig ist» ([[LUK.6.36]]). Was Matthäus in der Bergpredigt über das Gesetz ([[MAT.5.17-MAT.5.20]]) und über Almosen, Gebet und Fasten sagt ([[MAT.6.1-MAT.6.18]]), fehlt hier; das Vaterunser steht bei Lukas erst in [[LUK.11.2-LUK.11.4]].",
  ["LUK.6.17-LUK.6.49", "MAT.5.1-MAT.7.29"], "high",
  MAC + " Verszahlen nach der Navigation (KJV-Zählung). Ob beide Reden auf eine gemeinsame Quelle zurückgehen (die in der Forschung angenommene Logienquelle «Q») oder wie sie sonst zusammenhängen, ist eine Hypothese, kein Befund.",
  "D Fäldred ([[LUK.6.20-LUK.6.49]]) haltet de Jesus, won er vom Bärg abegstige isch, «uf eme äbene Platz» ([[LUK.6.17]]), vor de Jünger und ere grosse Mängi us Judäa, Jerusalem und vo de Chüschte bi Tyrus und Sidon. Si umfasst 30 Värs und folgt im Ganze de gliiche Ornig wie d Bärgpredig bim Matthäus (Vergliich mit [[MAT.5.1-MAT.7.29]], 111 Värs): Säligpriisige am Aafang, Feindesliebi, nöd richte, Baum und Frucht, s Huus uf em Fels am Schluss. I de Mitti staat d Feindesliebi: «Liebed eui Feind» raamt [[LUK.6.27-LUK.6.35]] ii, s Verb «liebe» (ἀγαπάω) staat i [[LUK.6.27-LUK.6.36]] sächs Mal, und de Abschnitt münded i «Sind barmhärzig, wie eue Vatter barmhärzig isch» ([[LUK.6.36]]). Was de Matthäus i de Bärgpredig über s Gsetz ([[MAT.5.17-MAT.5.20]]) und über Almose, Bätte und Faschte seit ([[MAT.6.1-MAT.6.18]]), fäält da; s Vatterunser staat bim Lukas erscht i [[LUK.11.2-LUK.11.4]].",
  MAC_G + " Värszaale nach de Navigation (KJV-Zellig). Öb beidi Rede uf e gmeinsami Quelle zruggönd (di i de Forschig aagnoo Logiequelle «Q») oder wie s süscht zämehanged, isch e Hypothese, kein Befund."),
 ("FIND-LUK-0014", U(7, 11, 17), "allusion",
  "Elija (Ἠλίας) wird im Lukasevangelium sieben Mal genannt, alle Stellen in den Kapiteln 1–9. Johannes soll «im Geist und in der Kraft Elijas» vorangehen ([[LUK.1.17]]); in Nazaret beruft sich Jesus auf Elija und Elischa ([[LUK.4.25-LUK.4.27]]). Die Auferweckung in Nain erinnert an Elija in Sarepta ([[1KI.17.17-1KI.17.24]]): Eine Witwe verliert ihren einzigen Sohn, und der Satz «und er gab ihn seiner Mutter» ([[LUK.7.15]]) steht ebenso in [[1KI.17.23]]; die Leute rufen: «Ein grosser Prophet ist unter uns aufgestanden!» ([[LUK.7.16]]). Manche meinen, in Jesus sei Elija erschienen ([[LUK.9.8]]; [[LUK.9.19]]); bei der Verklärung reden Mose und Elija mit ihm ([[LUK.9.30-LUK.9.33]]). Am Beginn des Wegs nach Jerusalem wollen Jakobus und Johannes Feuer vom Himmel fallen lassen wie Elija ([[LUK.9.54]]; vgl. [[2KI.1.10-2KI.1.12]]), und die Bitte, sich zuerst zu verabschieden, erinnert an Elischas Berufung vom Pflug weg ([[LUK.9.61-LUK.9.62]]; [[1KI.19.19-1KI.19.21]]).",
  ["LUK.1.17", "LUK.4.25-LUK.4.27", "LUK.7.11-LUK.7.17", "1KI.17.17-1KI.17.24", "LUK.9.8", "LUK.9.19", "LUK.9.30-LUK.9.33", "LUK.9.54", "2KI.1.10-2KI.1.12", "LUK.9.61-LUK.9.62", "1KI.19.19-1KI.19.21"], "high",
  MAC + " Dass [[LUK.7.15]] in der griechischen Bibel wörtlich mit [[1KI.17.23]] übereinstimmt, wird in der Auslegung oft angeführt; eine Ausgabe der Septuaginta ist hier nicht selbst verglichen.",
  "De Elija (Ἠλίας) wird im Lukasevangelium sibe Mal gnännt, all Stelle i de Kapitel 1–9. De Johannes söll «im Geischt und i de Chraft vom Elija» vorusgaa ([[LUK.1.17]]); z Nazaret beruefft sich de Jesus uf de Elija und de Elischa ([[LUK.4.25-LUK.4.27]]). D Uferweckig z Nain erinneret a de Elija z Sarepta ([[1KI.17.17-1KI.17.24]]): E Witwe verlüürt iren einzige Sohn, und de Satz «und er hät en sinere Mueter ggää» ([[LUK.7.15]]) staat gnau eso i [[1KI.17.23]]; d Lüüt rüefed: «En grosse Prophet isch under üs ufgstande!» ([[LUK.7.16]]). Mängi meined, im Jesus sig de Elija erschine ([[LUK.9.8]]; [[LUK.9.19]]); bi de Verklärig reded de Mose und de Elija mit ihm ([[LUK.9.30-LUK.9.33]]). Am Aafang vom Wäg uf Jerusalem wänd de Jakobus und de Johannes Füür vom Himmel la abechoo wie de Elija ([[LUK.9.54]]; vgl. [[2KI.1.10-2KI.1.12]]), und d Bitt, sich zerscht z verabschiede, erinneret dra, wie de Elischa vom Pflueg wäg brüeft worde isch ([[LUK.9.61-LUK.9.62]]; [[1KI.19.19-1KI.19.21]]).",
  MAC_G + " Dass [[LUK.7.15]] i de griechische Bible wörtlich mit [[1KI.17.23]] überiistimmt, wird i de Uslegig oft aagfüert; e Usgaab vo de Septuaginta isch da nöd sälber vergliche."),
 ("FIND-LUK-0015", U(9, 51, 56), "literary_structure",
  "Mit [[LUK.9.51]] beginnt ein neuer Teil: «Als sich die Tage seiner Aufnahme (ἀνάλημψις) erfüllten», fasst Jesus «den festen Entschluss, nach Jerusalem zu gehen» (wörtlich: er richtete sein Angesicht fest). Schon bei der Verklärung reden Mose und Elija von seinem «Weggang» (ἔξοδος), «den er in Jerusalem vollenden sollte» ([[LUK.9.31]]). Das Ziel wird danach immer wieder genannt ([[LUK.9.53]]; [[LUK.13.22]]; [[LUK.13.33]]; [[LUK.17.11]]; [[LUK.18.31]]; [[LUK.19.11]]; [[LUK.19.28]]). Jerusalem kommt im Lukasevangelium 31 Mal vor (in den beiden griechischen Namensformen Ἰερουσαλήμ und Ἱεροσόλυμα, 27 und vier Mal). Das Evangelium beginnt im Tempel von Jerusalem ([[LUK.1.9]]) und endet dort ([[LUK.24.52-LUK.24.53]]). Der Reisebericht nennt wenige Orte: ein Dorf der Samaritaner ([[LUK.9.52]]), ein Dorf, in dem Marta wohnt ([[LUK.10.38]]); viel Raum nehmen Reden, Gleichnisse und Gespräche ein.",
  ["LUK.9.31", "LUK.9.51-LUK.9.53", "LUK.13.22", "LUK.17.11", "LUK.19.28", "LUK.1.9", "LUK.24.52-LUK.24.53"], "high",
  MAC + " Wo der Reisebericht endet (etwa [[LUK.19.27]], [[LUK.19.44]] oder [[LUK.19.48]]), wird verschieden abgegrenzt.",
  "Mit [[LUK.9.51]] fangt en nöie Teil aa: «Wo d Täg vo sinere Ufnaam (ἀνάλημψις) sich erfüllt händ», bschlüüsst de Jesus «fescht, uf Jerusalem z gaa» (wörtlich: er hät sis Gsicht fescht grichtet). Scho bi de Verklärig reded de Mose und de Elija vo sim «Wäggang» (ἔξοδος), «won er z Jerusalem hät söle vollände» ([[LUK.9.31]]). S Ziil wird nachher immer wider gnännt ([[LUK.9.53]]; [[LUK.13.22]]; [[LUK.13.33]]; [[LUK.17.11]]; [[LUK.18.31]]; [[LUK.19.11]]; [[LUK.19.28]]). Jerusalem chunnt im Lukasevangelium 31 Mal vor (i de beide griechische Namesforme Ἰερουσαλήμ und Ἱεροσόλυμα, 27 und vier Mal). S Evangelium fangt im Tämpel vo Jerusalem aa ([[LUK.1.9]]) und hört dört uf ([[LUK.24.52-LUK.24.53]]). De Reisebricht nännt weni Ort: es Dorf vo de Samaritaner ([[LUK.9.52]]), es Dorf, wo d Marta wont ([[LUK.10.38]]); vil Platz bruuched Rede, Gliichnis und Gspröch.",
  MAC_G + " Wo de Reisebricht ufhört (öppe [[LUK.19.27]], [[LUK.19.44]] oder [[LUK.19.48]]), wird verschide abgränzt."),
 ("FIND-LUK-0016", U(9, 18, 22), "key_terms",
  "Die Frage nach Jesus zieht sich durch die Kapitel 5–9: «Wer ist dieser, der Lästerungen redet?» ([[LUK.5.21]]); «Wer ist dieser, der sogar Sünden vergibt?» ([[LUK.7.49]]); «Wer ist denn dieser, dass er sogar den Winden befiehlt?» ([[LUK.8.25]]); Herodes: «Wer aber ist dieser, über den ich solche Dinge höre?» ([[LUK.9.9]]). Auch der Täufer lässt fragen: «Bist du der Kommende?» ([[LUK.7.19-LUK.7.20]]). Die Meinungen, von denen Herodes hört ([[LUK.9.7-LUK.9.8]]), kehren fast wörtlich wieder, als Jesus die Jünger fragt ([[LUK.9.18-LUK.9.19]]); Petrus antwortet: «Der Christus Gottes» ([[LUK.9.20]]). Zwischen der Frage des Herodes und dem Bekenntnis steht bei Lukas nur die Speisung der Fünftausend ([[LUK.9.10-LUK.9.17]]); was Markus zwischen diesen beiden Szenen erzählt, hat Lukas nicht (Vergleich mit [[MRK.6.45-MRK.8.26]]).",
  ["LUK.5.21", "LUK.7.19-LUK.7.20", "LUK.7.49", "LUK.8.25", "LUK.9.7-LUK.9.9", "LUK.9.18-LUK.9.20"], "high",
  "Beobachtung am Wortlaut. Der Vergleich mit Markus folgt den gängigen Synopsen; einzelne Stoffe aus [[MRK.6.45-MRK.8.26]] haben bei Lukas an anderer Stelle Anklänge (etwa [[LUK.12.1]] zu [[MRK.8.15]]).",
  "D Frag nach em Jesus zieht sich dur d Kapitel 5–9: «Wär isch dä, wo Läschterige redt?» ([[LUK.5.21]]); «Wär isch dä, wo sogar Sünde vergit?» ([[LUK.7.49]]); «Wär isch dänn dä, dass er sogar de Wind befiehlt?» ([[LUK.8.25]]); de Herodes: «Wär isch aber dä, vo dem ich settigs ghöre?» ([[LUK.9.9]]). Au de Täufer laat fröge: «Bisch du dä, wo chunnt?» ([[LUK.7.19-LUK.7.20]]). D Meinige, wo de Herodes devo ghört ([[LUK.9.7-LUK.9.8]]), chömed fascht wörtlich wider, wo de Jesus d Jünger fröget ([[LUK.9.18-LUK.9.19]]); de Petrus antwortet: «De Christus vo Gott» ([[LUK.9.20]]). Zwüsche de Frag vom Herodes und em Bekänntnis staat bim Lukas nu d Spiisig vo de Föiftuusig ([[LUK.9.10-LUK.9.17]]); was de Markus zwüsche dene beide Szene verzellt, hät de Lukas nöd (Vergliich mit [[MRK.6.45-MRK.8.26]]).",
  "Beobachtig am Wortluut. De Vergliich mit em Markus folgt de gängige Synopse; einzelni Stoff us [[MRK.6.45-MRK.8.26]] händ bim Lukas a andere Stelle Aakläng (öppe [[LUK.12.1]] zu [[MRK.8.15]])."),
 ("FIND-LUK-0017", U(10, 25, 37), "names",
  "Samaritaner (Σαμαρίτης) erwähnt Lukas drei Mal, Matthäus einmal (im Verbot, in ihre Städte zu gehen; Vergleich mit [[MAT.10.5]]), Markus nie. Am Beginn des Wegs nach Jerusalem nimmt ein Dorf der Samaritaner Jesus nicht auf, weil er nach Jerusalem unterwegs ist; Jesus weist die Jünger zurecht, die Feuer vom Himmel herabrufen wollen ([[LUK.9.52-LUK.9.55]]). Kurz darauf ist es im Gleichnis ein Samaritaner, der den Überfallenen versorgt, nachdem ein Priester und ein Levit vorübergegangen sind ([[LUK.10.30-LUK.10.35]]); später kehrt von zehn geheilten Aussätzigen nur einer zurück, um zu danken, ein Samaritaner ([[LUK.17.11-LUK.17.19]]). Das Verb σπλαγχνίζομαι («Erbarmen haben», wörtlich «im Innersten bewegt sein») steht bei Lukas nur drei Mal: für Jesus vor der Witwe in Nain ([[LUK.7.13]]), für den Samaritaner ([[LUK.10.33]]) und für den Vater des verlorenen Sohnes ([[LUK.15.20]]).",
  ["LUK.9.52-LUK.9.55", "LUK.10.30-LUK.10.35", "LUK.17.11-LUK.17.19", "LUK.7.13", "LUK.10.33", "LUK.15.20"], "high", MAC,
  "Samaritaner (Σαμαρίτης) erwäänt de Lukas drüü Mal, de Matthäus eimal (im Verbot, i iri Städt z gaa; Vergliich mit [[MAT.10.5]]), de Markus nie. Am Aafang vom Wäg uf Jerusalem nimmt es Dorf vo de Samaritaner de Jesus nöd uf, wil er understwägs uf Jerusalem isch; de Jesus wiist d Jünger zrächt, wo Füür vom Himmel wänd abe rüefe ([[LUK.9.52-LUK.9.55]]). Churz druf isch es im Gliichnis en Samaritaner, wo für de Überfallne sorget, nachdem en Prieschter und en Levit verbiigange sind ([[LUK.10.30-LUK.10.35]]); spööter chunnt vo zää gheilte Ussätzige nu eine zrugg, zum danke, en Samaritaner ([[LUK.17.11-LUK.17.19]]). S Verb σπλαγχνίζομαι («Erbarme haa», wörtlich «im Innerschte bewegt sii») staat bim Lukas nu drüü Mal: für de Jesus vor de Witwe z Nain ([[LUK.7.13]]), für de Samaritaner ([[LUK.10.33]]) und für de Vatter vom verlorne Sohn ([[LUK.15.20]]).",
  MAC_G),
 ("FIND-LUK-0018", U(10, 25, 37), "argument_structure",
  "Das Gespräch in [[LUK.10.25-LUK.10.37]] hat zwei gleich gebaute Gänge. Erster Gang: Frage des Gesetzeslehrers («Was muss ich tun …?»), Gegenfrage Jesu («Was steht im Gesetz geschrieben?»), Antwort mit [[DEU.6.5]] und [[LEV.19.18]], Bestätigung: «Tu das, und du wirst leben» ([[LUK.10.25-LUK.10.28]]). Zweiter Gang: Frage («Und wer ist mein Nächster?»), Gleichnis, Gegenfrage («Wer … ist dem … zum Nächsten geworden?»), Antwort («Der, der die Barmherzigkeit an ihm geübt hat»), Auftrag: «Geh, und handle du ebenso!» ([[LUK.10.29-LUK.10.37]]). Das Verb «tun» (ποιέω) steht in diesen Versen vier Mal, am Anfang und am Ende. Die Frage verschiebt sich: Der Gesetzeslehrer fragt, wer sein Nächster sei; Jesus fragt, wer dem Überfallenen zum Nächsten wurde. In seiner Antwort nennt der Gesetzeslehrer den Samaritaner nicht beim Namen ([[LUK.10.37]]).",
  ["LUK.10.25-LUK.10.37", "DEU.6.5", "LEV.19.18"], "high",
  MAC + " Die Zweiteilung wird in der Auslegung oft beschrieben (etwa Kenneth E. Bailey, Through Peasant Eyes, 1980). Dass der Gesetzeslehrer den Namen vermeidet, ist Beobachtung; warum er es tut, ist Deutung.",
  "S Gspröch i [[LUK.10.25-LUK.10.37]] hät zwei gliich bauti Gäng. Erschte Gang: Frag vom Gsetzeslehrer («Was mues ich mache …?»), Gägefrag vo Jesus («Was staat im Gsetz gschribe?»), Antwort mit [[DEU.6.5]] und [[LEV.19.18]], Bestätigung: «Mach das, und du wirsch läbe» ([[LUK.10.25-LUK.10.28]]). Zweite Gang: Frag («Und wär isch min Nächscht?»), Gliichnis, Gägefrag («Wär … isch für dä … de Nächscht worde?»), Antwort («Dä, wo Barmhärzigkeit a ihm güebt hät»), Uftrag: «Gang, und mach du s gliich!» ([[LUK.10.29-LUK.10.37]]). S Verb «tue, mache» (ποιέω) staat i dene Värs vier Mal, am Aafang und am Schluss. D Frag verschiebt sich: De Gsetzeslehrer fröget, wär sin Nächscht sig; de Jesus fröget, wär für de Überfallne de Nächscht worde isch. I sinere Antwort nännt de Gsetzeslehrer de Samaritaner nöd bim Name ([[LUK.10.37]]).",
  MAC_G + " D Zweiteilig wird i de Uslegig oft beschribe (öppe Kenneth E. Bailey, Through Peasant Eyes, 1980). Dass de Gsetzeslehrer de Name vermiidet, isch Beobachtig; werum er s macht, isch Düütig."),
 ("FIND-LUK-0019", U(11, 5, 13), "argument_structure",
  "Auf das Gebet ([[LUK.11.1-LUK.11.4]]) folgen in [[LUK.11.5-LUK.11.13]] ein Gleichnis, eine Aufforderung und ein Vergleich. Gleichnis und Vergleich schliessen vom Kleineren aufs Grössere: Wenn schon ein Freund um Mitternacht aufsteht ([[LUK.11.8]]) und schon ein Vater seinem Kind keine Schlange statt eines Fisches gibt, «wie viel mehr wird der Vater im Himmel den Heiligen Geist denen, die ihn bitten, geben!» ([[LUK.11.13]]). Dieselbe Schlussform «wie viel mehr» (πόσῳ μᾶλλον) steht in [[LUK.12.24]] und [[LUK.12.28]]; in der jüdischen Auslegung ist sie als Schluss vom Leichteren aufs Schwerere geläufig. Wo Lukas «den Heiligen Geist» nennt, steht bei Matthäus «Gutes» (Vergleich mit [[MAT.7.11]]).",
  ["LUK.11.5-LUK.11.13", "LUK.12.24", "LUK.12.28", "MAT.7.11"], "high",
  MAC + " Gezählt ist πόσος in [[LUK.11.1-LUK.12.59]]; die drei Belege sind die genannten.",
  "Uf s Gebätt ([[LUK.11.1-LUK.11.4]]) folged i [[LUK.11.5-LUK.11.13]] es Gliichnis, e Ufforderig und en Vergliich. Gliichnis und Vergliich schlüüssed vom Chliinere ufs Grösser: Wänn scho en Fründ z Mitternacht ufstaat ([[LUK.11.8]]) und scho en Vatter sim Chind kei Schlange statt eme Fisch git, «wie vil meh wird de Vatter im Himmel de Heilig Geischt dene, wo en drum bitted, gää!» ([[LUK.11.13]]). Di gliich Schlussform «wie vil meh» (πόσῳ μᾶλλον) staat i [[LUK.12.24]] und [[LUK.12.28]]; i de jüdische Uslegig isch si als Schluss vom Liechtere ufs Schwärere gläufig. Wo de Lukas «de Heilig Geischt» nännt, staat bim Matthäus «Guets» (Vergliich mit [[MAT.7.11]]).",
  MAC_G + " Zellt isch πόσος i [[LUK.11.1-LUK.12.59]]; di drüü Beleg sind di gnännte."),
 ("FIND-LUK-0020", U(11, 37, 54), "literary_structure",
  "Anlass der Weherufe ist ein Mahl: Ein Pharisäer wundert sich, dass Jesus sich vor dem Essen nicht gewaschen hat ([[LUK.11.37-LUK.11.38]]). Jesus antwortet mit einem Wort über Aussen und Innen von Becher und Schüssel ([[LUK.11.39-LUK.11.41]]) und dann mit sechs Weherufen (οὐαί): drei an die Pharisäer, über den Zehnten von Gartenkräutern bei Vernachlässigung von «Recht und Liebe Gottes», über Ehrenplätze und über unkenntliche Gräber ([[LUK.11.42-LUK.11.44]]); nach dem Einwurf eines Gesetzeslehrers drei an die Gesetzeslehrer, über unerträgliche Lasten, über die Grabmäler der Propheten und über den weggenommenen «Schlüssel der Erkenntnis» ([[LUK.11.45-LUK.11.52]]). Danach beginnen Schriftgelehrte und Pharisäer, ihn zu bedrängen und ihm «aufzulauern» ([[LUK.11.53-LUK.11.54]]). Schon die erste Einladung bei einem Pharisäer führt zu einem Streit ([[LUK.7.36-LUK.7.50]]); eine dritte folgt in [[LUK.14.1-LUK.14.24]].",
  ["LUK.11.37-LUK.11.54", "LUK.7.36", "LUK.14.1"], "high",
  MAC + " Mehrere dieser Weherufe stehen bei Matthäus in anderer Reihenfolge und anderem Rahmen (Vergleich mit [[MAT.23.1-MAT.23.36]]).",
  "Aalass vo de Weheruef isch es Ässe: En Pharisäer wunderet sich, dass sich de Jesus vor em Ässe nöd gwäsche hät ([[LUK.11.37-LUK.11.38]]). De Jesus antwortet mit eme Wort über s Üsser und s Inner vo Bächer und Schüssle ([[LUK.11.39-LUK.11.41]]) und dänn mit sächs Weheruef (οὐαί): drüü a d Pharisäer, über de Zäänte vo Gartechrüüter, wäred si «s Rächt und d Liebi vo Gott» vernachlässiged, über Ehreplätz und über Greber, wo me nöd gseht ([[LUK.11.42-LUK.11.44]]); und nachdem en Gsetzeslehrer öppis iiwirft, drüü a d Gsetzeslehrer, über Laschte, wo me nöd cha träge, über d Grabmäler vo de Prophete und über de Schlüssel vo de Erchänntnis, wo si wäggnoo händ ([[LUK.11.45-LUK.11.52]]). Dänn fanged d Schriftgleerte und d Pharisäer aa, en z bedränge und em «ufzlauere» ([[LUK.11.53-LUK.11.54]]). Scho di erscht Iiladig bi eme Pharisäer füert zu me Striit ([[LUK.7.36-LUK.7.50]]); e dritti folgt i [[LUK.14.1-LUK.14.24]].",
  MAC_G + " Meereri vo dene Weheruef staat bim Matthäus i andere Reiefolg und i eme andere Raame (Vergliich mit [[MAT.23.1-MAT.23.36]])."),
 ("FIND-LUK-0021", U(12, 13, 21), "key_terms",
  "[[LUK.12.13-LUK.12.34]] handelt vom Besitz. Ein Erbstreit ist der Anlass ([[LUK.12.13-LUK.12.14]]); Jesus warnt vor «jeder Habgier» (πλεονεξία, in den Evangelien sonst nur [[MRK.7.22]]) und begründet: «Wenn jemand Überfluss hat, besteht sein Leben nicht aus dem, was er besitzt» ([[LUK.12.15]]). Im Gleichnis spricht der reiche Mann nur mit sich selbst: Er «überlegte bei sich» und redet zu seiner «Seele» (ψυχή); das Fürwort «mein» (μου) steht in [[LUK.12.17-LUK.12.19]] vier Mal: meine Ernte, meine Scheunen, meine Güter, meine Seele. Gott antwortet: «Du Tor! Noch in dieser Nacht fordert man deine Seele von dir zurück» ([[LUK.12.20]]). Das Wort ψυχή («Seele, Leben») verbindet das Gleichnis mit dem folgenden Wort an die Jünger: «Sorgt euch nicht um das Leben» ([[LUK.12.22-LUK.12.23]]); in [[LUK.12.19-LUK.12.23]] steht es fünf Mal. «Sich sorgen» (μεριμνάω) steht in [[LUK.12.22-LUK.12.26]] drei Mal; der Abschnitt endet mit «Verkauft euren Besitz und gebt Almosen!» und «wo euer Schatz ist, da wird auch euer Herz sein» ([[LUK.12.33-LUK.12.34]]).",
  ["LUK.12.13-LUK.12.34", "MRK.7.22"], "high", MAC,
  "[[LUK.12.13-LUK.12.34]] handlet vom Bsitz. En Striit ums Erb isch de Aalass ([[LUK.12.13-LUK.12.14]]); de Jesus warnt vor «jeder Habgier» (πλεονεξία, i de Evangelie süscht nu [[MRK.7.22]]) und begründet: «Wänn öpper Überfluss hät, bestaat sis Läbe nöd us dem, won er bsitzt» ([[LUK.12.15]]). Im Gliichnis redt de riich Maa nu mit sich sälber: Er «hät bi sich überleit» und redt zu sinere «Seel» (ψυχή); s Fürwort «min» (μου) staat i [[LUK.12.17-LUK.12.19]] vier Mal: mini Ärnt, mini Schüüre, mini Güeter, mini Seel. Gott antwortet: «Du Narr! No i dere Nacht forderet me dini Seel vo dir zrugg» ([[LUK.12.20]]). S Wort ψυχή («Seel, Läbe») verbindet s Gliichnis mit em nööchschte Wort a d Jünger: «Mached eu kei Sorge ums Läbe» ([[LUK.12.22-LUK.12.23]]); i [[LUK.12.19-LUK.12.23]] staat s föif Mal. «Sich Sorge mache» (μεριμνάω) staat i [[LUK.12.22-LUK.12.26]] drüü Mal; de Abschnitt hört uf mit «Verchaufed eue Bsitz und gänd Almose!» und «wo eue Schatz isch, dört wird au eues Härz sii» ([[LUK.12.33-LUK.12.34]]).",
  MAC_G),
 ("FIND-LUK-0022", U(7, 36, 50), "argument_structure",
  "In [[LUK.7.36-LUK.7.50]] steht ein kurzes Gleichnis mitten in der Erzählung. Der Pharisäer denkt bei sich, ein Prophet wüsste, «was für eine Frau das ist» ([[LUK.7.39]]); Jesus antwortet auf den ungesagten Gedanken mit dem Gleichnis von zwei Schuldnern, denen 500 und 50 Denare erlassen werden, und lässt Simon selbst urteilen ([[LUK.7.40-LUK.7.43]]). Dann vergleicht er in drei Gegensätzen: kein Wasser für die Füsse – Tränen; kein Kuss – Küsse auf die Füsse; kein Öl für den Kopf – Salböl für die Füsse ([[LUK.7.44-LUK.7.46]]). Es folgen das Urteil «Ihre Sünden, die vielen, sind vergeben, denn sie hat viel geliebt; wem aber wenig vergeben wird, der liebt wenig» ([[LUK.7.47]]), das Wort an die Frau ([[LUK.7.48]]; [[LUK.7.50]]) und die Frage der Tischgenossen: «Wer ist dieser, der sogar Sünden vergibt?» ([[LUK.7.49]]). Die Frau spricht in der ganzen Szene kein Wort. «Dein Glaube hat dich gerettet; geh in Frieden!» sagt Jesus gleichlautend zu der Frau mit dem Blutfluss ([[LUK.8.48]], dort mit der Anrede «Tochter»).",
  ["LUK.7.36-LUK.7.50", "LUK.8.48"], "high",
  "Beobachtung am Wortlaut. Ähnliche Salbungsszenen stehen in [[MRK.14.3-MRK.14.9]] und [[JHN.12.1-JHN.12.8]] (Vergleich); ob sie auf dasselbe Ereignis zurückgehen, ist umstritten.",
  "I [[LUK.7.36-LUK.7.50]] staat es churzes Gliichnis mitten i de Gschicht. De Pharisäer dänkt bi sich, en Prophet wüssti, «was für e Frau das isch» ([[LUK.7.39]]); de Jesus antwortet uf de Gedanke, wo niemer usgsproche hät, mit em Gliichnis vo zwei Schuldner, wo me 500 und 50 Denar erlaa hät, und laat de Simon sälber urteile ([[LUK.7.40-LUK.7.43]]). Dänn verglicht er i drüü Gägesätz: kei Wasser für d Füess – Träne; kein Kuss – Küss uf d Füess; kei Öl für de Chopf – Salböl für d Füess ([[LUK.7.44-LUK.7.46]]). Dänn chömed s Urteil «Iri Sünde, di vile, sind vergää, dänn si hät vil gliebt; wem aber wenig vergää wird, dä liebt wenig» ([[LUK.7.47]]), s Wort a d Frau ([[LUK.7.48]]; [[LUK.7.50]]) und d Frag vo dene, wo mit am Tisch ligged: «Wär isch dä, wo sogar Sünde vergit?» ([[LUK.7.49]]). D Frau seit i de ganze Szene keis Wort. «Din Glaube hät di grettet; gang i Fride!» seit de Jesus gnau gliich zu de Frau mit em Bluetfluss ([[LUK.8.48]], dört mit de Aared «Tochter»).",
  "Beobachtig am Wortluut. Ähnlichi Salbigsszene staat i [[MRK.14.3-MRK.14.9]] und [[JHN.12.1-JHN.12.8]] (Vergliich); öb si uf s gliich Ereignis zruggönd, isch umstritte."),
 ("FIND-LUK-0023", U(7, 18, 23), "quotation",
  "Auf die Frage des Täufers «Bist du der Kommende?» ([[LUK.7.19-LUK.7.20]]) antwortet Jesus nicht mit Ja oder Nein, sondern lässt berichten, was die Boten sehen und hören; der Erzähler schiebt vorher ein, dass Jesus «in jener Stunde» viele heilte ([[LUK.7.21]]). Die Liste in [[LUK.7.22]] nimmt Worte aus Jesaja auf: Blinde sehen, Lahme gehen, Taube hören ([[ISA.35.5-ISA.35.6]]), Tote werden auferweckt ([[ISA.26.19]]), den Armen wird das Evangelium verkündet ([[ISA.61.1]]). Das letzte Glied wiederholt das Programm aus Nazaret ([[LUK.4.18]]). Die Reinigung von Aussätzigen steht in keiner dieser Jesajastellen; sie erinnert an Elischa und Naaman ([[LUK.4.27]]) und an die Heilung in [[LUK.5.12-LUK.5.14]]. Die Auferweckung in Nain ist unmittelbar vorher erzählt ([[LUK.7.11-LUK.7.17]]).",
  ["LUK.7.18-LUK.7.23", "ISA.35.5-ISA.35.6", "ISA.26.19", "ISA.61.1", "LUK.4.18"], "high",
  "Anklänge am Wortlaut; die Zuordnung zu einzelnen Jesajastellen ist in der Auslegung verbreitet. Eine Schrift aus Qumran (4Q521) nennt ähnliche Taten für die Zeit des Gesalbten, darunter Tote beleben und Armen gute Botschaft bringen; sie ist hier nicht selbst geprüft.",
  "Uf d Frag vom Täufer «Bisch du dä, wo chunnt?» ([[LUK.7.19-LUK.7.20]]) antwortet de Jesus nöd mit Ja oder Nei, sondern laat brichte, was d Bote gsehnd und ghöred; de Erzähler schiebt vorher ii, dass de Jesus «i säbere Stund» vili gheilt hät ([[LUK.7.21]]). D Lischte i [[LUK.7.22]] nimmt Wort us em Jesaja uf: Blindi gsehnd, Lahmi laufed, Taubi ghöred ([[ISA.35.5-ISA.35.6]]), Toti wärded uferweckt ([[ISA.26.19]]), de Arme wird s Evangelium verchündet ([[ISA.61.1]]). S letscht Glid widerholt s Programm vo Nazaret ([[LUK.4.18]]). Dass Ussätzigi rein wärded, staat i keinere vo dene Jesajastelle; das erinneret a de Elischa und de Naaman ([[LUK.4.27]]) und a d Heilig i [[LUK.5.12-LUK.5.14]]. D Uferweckig z Nain isch grad vorher verzellt ([[LUK.7.11-LUK.7.17]]).",
  "Aakläng am Wortluut; d Zueornig zu einzelne Jesajastelle isch i de Uslegig verbreitet. E Schrift us Qumran (4Q521) nännt ähnlichi Tate für d Ziit vom Gsalbte, dorunder Toti läbig mache und de Arme e gueti Botschaft bringe; si isch da nöd sälber prüeft."),
 ("FIND-LUK-0024", U(8, 16, 18), "key_terms",
  "In [[LUK.8.4-LUK.8.21]] ist «hören» (ἀκούω) das Leitwort: neun Mal in 18 Versen. Das Gleichnis vom Sämann endet mit dem Ruf «Wer Ohren hat zum Hören, der höre!» ([[LUK.8.8]]); die Deutung beschreibt vier Arten, das Wort zu hören ([[LUK.8.11-LUK.8.15]]); es folgt «Achtet also darauf, wie ihr hört!» ([[LUK.8.18]]). Der Abschnitt schliesst mit der Szene, in der Mutter und Brüder Jesu draussen stehen: «Meine Mutter und meine Brüder sind die, die das Wort Gottes hören und tun» ([[LUK.8.19-LUK.8.21]]). Ähnlich antwortet Jesus später auf die Seligpreisung seiner Mutter: «Vielmehr selig, die das Wort Gottes hören und bewahren!» ([[LUK.11.27-LUK.11.28]]). Bei Lukas steht die Szene mit der Familie nach den Gleichnissen, bei Markus davor, nachdem die Angehörigen ihn zuvor für «von Sinnen» gehalten haben (Vergleich mit [[MRK.3.21]] und [[MRK.3.31-MRK.3.35]]).",
  ["LUK.8.4-LUK.8.21", "LUK.11.27-LUK.11.28", "LUK.6.47-LUK.6.49"], "high", MAC,
  "I [[LUK.8.4-LUK.8.21]] isch «ghöre» (ἀκούω) s Leitwort: nüün Mal i 18 Värs. S Gliichnis vom Sämaa hört uf mit em Ruef «Wär Ohre hät zum Ghöre, söll lose!» ([[LUK.8.8]]); d Düütig beschriibt vier Arte, s Wort z ghöre ([[LUK.8.11-LUK.8.15]]); dänn chunnt «Passed also uf, wie ir lösed!» ([[LUK.8.18]]). De Abschnitt schlüüsst mit de Szene, wo d Mueter und d Brüeder vo Jesus dusse stönd: «Mini Mueter und mini Brüeder sind die, wo s Wort vo Gott ghöred und tüend» ([[LUK.8.19-LUK.8.21]]). Ähnlich antwortet de Jesus spööter, wo e Frau sini Mueter sälig priist: «Vilmeh sälig, die, wo s Wort vo Gott ghöred und bewahred!» ([[LUK.11.27-LUK.11.28]]). Bim Lukas staat d Szene mit de Familie nach de Gliichnis, bim Markus devor, nachdem en d Aaghörige vorher für «nöd bi Sinne» ghalte händ (Vergliich mit [[MRK.3.21]] und [[MRK.3.31-MRK.3.35]]).",
  MAC_G),
 ("FIND-LUK-0025", U(3, 23, 38), "names",
  "Der Stammbaum Jesu steht bei Lukas nicht am Anfang, sondern zwischen der Taufe und der Versuchung ([[LUK.3.23-LUK.3.38]]). Er führt rückwärts von Jesus, der «wie man meinte» Sohn Josefs war ([[LUK.3.23]]), bis zu Adam und endet mit «Gottes» ([[LUK.3.38]]); von Jesus bis Adam sind es 77 Namen. Unmittelbar davor nennt die Stimme aus dem Himmel Jesus «mein geliebter Sohn» ([[LUK.3.22]]), unmittelbar danach sagt der Teufel: «Wenn du Gottes Sohn bist …» ([[LUK.4.3]]; [[LUK.4.9]]). Von Abraham bis David stimmt die Liste weitgehend mit Matthäus überein (Vergleich mit [[MAT.1.2-MAT.1.6]]); danach führt sie über Davids Sohn Natan statt über Salomo ([[LUK.3.31]]) und hat bis Josef fast nur andere Namen (gemeinsam sind Schealtiël und Serubbabel, [[LUK.3.27]]); als Vater Josefs nennt Lukas Eli ([[LUK.3.23]]), Matthäus Jakob (Vergleich mit [[MAT.1.16]]).",
  ["LUK.3.22-LUK.3.38", "LUK.4.3", "LUK.4.9", "MAT.1.1-MAT.1.17"], "high",
  MAC + " Gezählt sind die Eigennamen in [[LUK.3.23-LUK.3.38]] ohne «Gott»; zwei verschiedene Männer heissen im Griechischen Καϊνάμ ([[LUK.3.36]]: Kainam; [[LUK.3.37]]: Kenan). Andere Lesarten verändern die Zahl, etwa in [[LUK.3.33]] (siehe die Alternativen). Dass 77 elfmal sieben ist, deuten manche als bewusste Ordnung; das ist Deutung.",
  "De Stammbaum vo Jesus staat bim Lukas nöd am Aafang, sondern zwüsche de Taufi und de Versuechig ([[LUK.3.23-LUK.3.38]]). Er füert rückwärts vom Jesus, wo «wie mer gmeint hät» de Sohn vom Josef gsii isch ([[LUK.3.23]]), bis zum Adam und hört uf mit «vo Gott» ([[LUK.3.38]]); vom Jesus bis zum Adam sind s 77 Näme. Grad devor nännt d Stimm us em Himmel de Jesus «min liebe Sohn» ([[LUK.3.22]]), grad nachher seit de Tüüfel: «Wänn du Gottes Sohn bisch …» ([[LUK.4.3]]; [[LUK.4.9]]). Vom Abraham bis zum David stimmt d Lischte wiitgehend mit em Matthäus überii (Vergliich mit [[MAT.1.2-MAT.1.6]]); dänn füert si über de Natan, en Sohn vom David, statt über de Salomo ([[LUK.3.31]]) und hät bis zum Josef fascht nu anderi Näme (gmeinsam sind de Schealtiël und de Serubbabel, [[LUK.3.27]]); als Vatter vom Josef nännt de Lukas de Eli ([[LUK.3.23]]), de Matthäus de Jakob (Vergliich mit [[MAT.1.16]]).",
  MAC_G + " Zellt sind d Eigenäme i [[LUK.3.23-LUK.3.38]] ohni «Gott»; zwei verschideni Manne heissed im Griechische Καϊνάμ ([[LUK.3.36]]: Kainam; [[LUK.3.37]]: Kenan). Anderi Läsarte veränderet d Zaal, öppe i [[LUK.3.33]] (lueg d Alternative). Dass 77 elf mal sibe isch, düüted mängi als bewussti Ornig; das isch Düütig."),
 ("FIND-LUK-0026", U(5, 1, 11), "parallel_comparison",
  "Bei Lukas beruft Jesus die ersten Jünger erst, nachdem er in Kafarnaum gelehrt und Simons Schwiegermutter geheilt hat ([[LUK.4.31-LUK.4.39]]); bei Markus steht die Berufung am See vor diesen Szenen (Vergleich mit [[MRK.1.16-MRK.1.20]]). Jesus lehrt vom Boot Simons aus ([[LUK.5.3]]); auf sein Wort hin fangen die Fischer nach einer erfolglosen Nacht so viele Fische, dass die Netze zu reissen und beide Boote zu sinken beginnen ([[LUK.5.4-LUK.5.7]]). Simon fällt nieder: «Geh weg von mir, denn ich bin ein sündiger Mensch, Herr!» ([[LUK.5.8]]); Jesus antwortet: «Fürchte dich nicht! Von jetzt an wirst du Menschen fangen» ([[LUK.5.10]]); das Verb ζωγρέω heisst wörtlich «lebendig fangen». Die Berufenen «verliessen alles» ([[LUK.5.11]]), ebenso kurz darauf Levi ([[LUK.5.28]]). Einen ähnlichen Fischfang erzählt Johannes nach der Auferstehung (Vergleich mit [[JHN.21.1-JHN.21.11]]).",
  ["LUK.4.38-LUK.4.39", "LUK.5.1-LUK.5.11", "LUK.5.28", "MRK.1.16-MRK.1.20", "JHN.21.1-JHN.21.11"], "high",
  "Beobachtung am Wortlaut; die Hinweise auf Markus und Johannes sind ausdrücklich Vergleiche. Ob Lukas und Johannes auf eine gemeinsame Überlieferung zurückgehen, ist umstritten.",
  "Bim Lukas rüeft de Jesus di erschte Jünger erscht, nachdem er z Kafarnaum glehrt und d Schwigermueter vom Simon gheilt hät ([[LUK.4.31-LUK.4.39]]); bim Markus staat d Berüefig am See vor dene Szene (Vergliich mit [[MRK.1.16-MRK.1.20]]). De Jesus lehrt vom Boot vom Simon uus ([[LUK.5.3]]); uf sis Wort hii fanged d Fischer nach ere Nacht ohni Fang so vil Fisch, dass d Netz aafanged z verrisse und beidi Boot aafanged z sinke ([[LUK.5.4-LUK.5.7]]). De Simon fallt nider: «Gang wäg vo mir, ich bi nämli en sündige Mänsch, Herr!» ([[LUK.5.8]]); de Jesus antwortet: «Häb kei Angscht! Vo jetzt aa wirsch Mänsche fange» ([[LUK.5.10]]); s Verb ζωγρέω heisst wörtlich «läbig fange». Die, wo brüeft worde sind, «händ alles la ligge» ([[LUK.5.11]]), gliich wie churz druf de Levi ([[LUK.5.28]]). En ähnliche Fischfang verzellt de Johannes nach de Uferstehig (Vergliich mit [[JHN.21.1-JHN.21.11]]).",
  "Beobachtig am Wortluut; d Hiiwiis uf de Markus und de Johannes sind usdrücklich Vergliich. Öb de Lukas und de Johannes uf e gmeinsami Überliferig zruggönd, isch umstritte."),
 ("FIND-LUK-0027", U(10, 17, 20), "literary_structure",
  "Die Zweiundsiebzig kehren «mit Freude» zurück: «Herr, sogar die Dämonen unterwerfen sich uns in deinem Namen!» ([[LUK.10.17]]). Jesus antwortet in drei Sätzen: «Ich sah den Satan wie einen Blitz vom Himmel fallen» ([[LUK.10.18]]), die Zusage der Vollmacht über «Schlangen und Skorpione» und «die ganze Macht des Feindes» ([[LUK.10.19]]) und eine Umlenkung der Freude: nicht darüber, dass die Geister sich unterwerfen, sondern darüber, «dass eure Namen im Himmel aufgeschrieben sind» ([[LUK.10.20]]). «In eben dieser Stunde» jubelt Jesus im Heiligen Geist und preist den Vater, der dies «Unmündigen» offenbart hat ([[LUK.10.21]]); das Verb ἀγαλλιάω («jubeln») steht im Lukasevangelium nur hier und in Marias Lied ([[LUK.1.47]]).",
  ["LUK.10.17-LUK.10.24", "LUK.1.47"], "high",
  MAC + " Ob «Ich sah» eine Vision, ein Bild oder einen Blick auf die Endzeit meint, ist Deutung (siehe die Übersetzungsentscheidung zu [[LUK.10.18]] und INT-LUK-0009).",
  "D Zweiesibezg chömed «voll Fröid» zrugg: «Herr, sogar d Dämone ordned sich üs under i dim Name!» ([[LUK.10.17]]). De Jesus antwortet i drüü Sätz: «Ich ha de Satan wie en Blitz vom Himmel abegheie gseh» ([[LUK.10.18]]), d Zuesag vo de Vollmacht über «Schlange und Skorpion» und über «di ganz Macht vom Feind» ([[LUK.10.19]]) und e Umlänkig vo de Fröid: nöd drüber, dass sich d Geischter underordned, sondern drüber, «dass eui Näme im Himmel ufgschribe sind» ([[LUK.10.20]]). «Grad i dere Stund» jublet de Jesus im Heilige Geischt und priist de Vatter, wo das «Unmündige» offebart hät ([[LUK.10.21]]); s Verb ἀγαλλιάω («juble») staat im Lukasevangelium nu da und im Lied vo de Maria ([[LUK.1.47]]).",
  MAC_G + " Öb «Ich ha gseh» e Vision, es Bild oder en Blick uf d Ändziit meint, isch Düütig (lueg d Übersetzigsentscheidig zu [[LUK.10.18]] und INT-LUK-0009)."),
]

# (id, Abschnitt, gestützt auf, Aussage, Konfidenz, Vorbehalt, Gegenargumente, Fachwörter | Mundart: Aussage, Vorbehalt, Gegenargumente, Fachwörter)
INTERPRETATIONS = [
 ("INT-LUK-0001", U(1, 1, 4), ["FIND-LUK-0001", "BG-LUK-0001"],
  "Das Vorwort stellt das Evangelium in die Form antiker Sach- und Geschichtswerke: Lukas will nicht der Erste sein, sondern Bekanntes geprüft und geordnet darstellen. Ziel ist Gewissheit für einen, der schon unterrichtet ist ([[LUK.1.4]]). Die Ordnung «der Reihe nach» (καθεξῆς) dient der Überzeugungskraft der Darstellung, nicht unbedingt einer strengen Zeitfolge. Theophilus ist am ehesten eine wirkliche, angesehene Person, der das Werk gewidmet ist.",
  "probable",
  "Ob καθεξῆς eine zeitliche, eine sachliche oder eine erzählerisch überzeugende Ordnung meint, entscheidet das Wort allein nicht; Lukas ordnet manches anders als Markus (FIND-LUK-0008; FIND-LUK-0026).",
  ["Der Name Θεόφιλος («Gottesfreund») kann symbolisch für jeden Leser stehen, der Gott liebt; so deutete ihn schon Origenes in seinen Homilien zum Lukasevangelium. Die ehrende Anrede κράτιστε («hochverehrter») spricht eher für eine wirkliche Person (vgl. [[ACT.23.26]]; [[ACT.24.3]]).",
   "Loveday Alexander (The Preface to Luke's Gospel, 1993) liest das Vorwort vor allem im Licht der Vorreden von Fachbüchern (Medizin, Technik), nicht der Geschichtsschreibung; dann will Lukas eher zuverlässiges Lehrgut weitergeben als Geschichte im Sinn der Historiker schreiben.",
   "Die Bemerkung über die «vielen» ([[LUK.1.1]]) kann eine stille Kritik an den Vorgängern enthalten (ihre Darstellung reiche nicht aus) oder einfach eine übliche, bescheidene Einleitung sein."],
  [("grc", "καθεξῆς", "der Reihe nach, in geordneter Folge"), ("grc", "Θεόφιλος", "Theophilus; «Gottesfreund»"),
   ("grc", "κράτιστε", "hochverehrter, vortrefflichster (Ehrenanrede)")],
  "S Vorwort stellt s Evangelium i d Form vo antike Sach- und Gschichtswärch: De Lukas wott nöd de Erscht sii, sondern Bekannts prüeft und gordnet daarstelle. S Ziil isch Gwüssheit für eine, wo scho underrichtet isch ([[LUK.1.4]]). D Ornig «der Reie naa» (καθεξῆς) dient dem, dass d Daarstellig überzüügt, nöd unbedingt ere sträng ziitliche Abfolg. De Theophilus isch am eheschte e würklichi, aagseheni Person, wo s Wärch ere gwidmet isch.",
  "Öb καθεξῆς e ziitlichi, e sachlichi oder e Ornig meint, wo bim Verzelle überzüügt, entscheidet s Wort elei nöd; de Lukas ordnet mängs anders als de Markus (FIND-LUK-0008; FIND-LUK-0026).",
  ["De Name Θεόφιλος («Gottesfründ») cha symbolisch für jede Läser staa, wo Gott liebt; so hät en scho de Origenes i sine Predige zum Lukasevangelium düütet. D ehrend Aared κράτιστε («hochverehrte») spricht eher für e würklichi Person (vgl. [[ACT.23.26]]; [[ACT.24.3]]).",
   "D Loveday Alexander (The Preface to Luke's Gospel, 1993) liist s Vorwort vor allem im Liecht vo de Vorrede vo Fachbüecher (Medizin, Technik), nöd vo de Gschichtsschriibig; dänn wott de Lukas eher zueverlässigs Lehrguet wiitergää als Gschicht im Sinn vo de Historiker schriibe.",
   "D Bemerkig über di «vile» ([[LUK.1.1]]) cha e stilli Kritik a de Vorgänger enthalte (iri Daarstellig länge nöd) oder eifach e üblichi, bescheideni Iileitig sii."],
  ["der Reie naa, i gordneter Abfolg", "Theophilus; «Gottesfründ»", "hochverehrte, vortrefflichschte (Ehrenaared)"]),
 ("INT-LUK-0002", U(1, 26, 38), ["FIND-LUK-0002"],
  "Die parallele Darstellung stellt Johannes und Jesus in eine Linie und zugleich in eine Rangfolge: Johannes ist der Prophet, der den Weg bereitet ([[LUK.1.17]]; [[LUK.1.76]]), Jesus der Sohn des Höchsten und König auf Davids Thron ([[LUK.1.32-LUK.1.33]]). Damit verbindet Lukas das Neue mit der Geschichte Israels: Es beginnt im Tempel, bei frommen, gesetzestreuen Menschen ([[LUK.1.6]]; [[LUK.2.22-LUK.2.39]]), und Gott erfüllt, was er Abraham zugesagt hat ([[LUK.1.54-LUK.1.55]]; [[LUK.1.72-LUK.1.73]]).",
  "probable",
  "Dass die Parallelen eine Rangfolge ausdrücken, ist weitgehend anerkannt; welche Absicht dahintersteht, ist offen.",
  ["Manche sehen darin eine Auseinandersetzung mit Anhängern des Täufers, die ihn höher stellten als Jesus (vgl. [[ACT.19.1-ACT.19.7]]); die Erzählung ordne Johannes deshalb ausdrücklich unter. Belege für eine solche Gruppe zur Zeit des Lukas sind spärlich.",
   "Andere betonen weniger die Rangfolge als die Abfolge der Zeiten: Johannes gehört für Lukas noch zur Zeit von «Gesetz und Propheten» ([[LUK.16.16]]), Jesus eröffnet die Verkündigung des Reiches Gottes; so Hans Conzelmann (Die Mitte der Zeit, 1954) mit seiner Einteilung in drei Zeiten. Diese Einteilung wird heute oft als zu schematisch beurteilt.",
   "Möglicherweise stammen Teile der Johannes-Erzählung aus einer eigenen Überlieferung über den Täufer, die Lukas mit der über Jesus verbunden hat; dann ist die Parallele auch ein Ergebnis der Quellen."],
  [],
  "D parallel Daarstellig stellt de Johannes und de Jesus i e Linie und zuglich i e Rangfolg: De Johannes isch de Prophet, wo de Wäg parat macht ([[LUK.1.17]]; [[LUK.1.76]]), de Jesus de Sohn vom Höchschte und König uf em Troon vom David ([[LUK.1.32-LUK.1.33]]). Demit verbindet de Lukas s Nöi mit de Gschicht vo Israel: Es fangt im Tämpel aa, bi fromme Lüüt, wo s Gsetz haltet ([[LUK.1.6]]; [[LUK.2.22-LUK.2.39]]), und Gott erfüllt, was er em Abraham zuegseit hät ([[LUK.1.54-LUK.1.55]]; [[LUK.1.72-LUK.1.73]]).",
  "Dass d Parallele e Rangfolg usdrucked, isch wiitgehend aaerchännt; weli Absicht dehinder staat, isch offe.",
  ["Mängi gsehnd drin e Usenandersetzig mit Aahänger vom Täufer, wo en höcher gstellt händ als de Jesus (vgl. [[ACT.19.1-ACT.19.7]]); d Erzälig ordni de Johannes drum usdrücklich under. Beleg für e settigi Gruppe zur Ziit vom Lukas git s weni.",
   "Anderi betoned weniger d Rangfolg als d Abfolg vo de Ziite: De Johannes ghört für de Lukas no zur Ziit vo «Gsetz und Prophete» ([[LUK.16.16]]), de Jesus fangt mit de Verchündigung vom Riich vo Gott aa; so de Hans Conzelmann (Die Mitte der Zeit, 1954) mit sinere Iiteilig i drüü Ziite. Die Iiteilig wird hüt oft als z schematisch beurteilt.",
   "Villicht stammed Teil vo de Johannes-Gschicht us ere eigete Überliferig über de Täufer, wo de Lukas mit dere über de Jesus verbunde hät; dänn isch d Parallele au es Ergäbnis vo de Quelle."],
  []),
 ("INT-LUK-0003", U(6, 20, 26), ["FIND-LUK-0005", "FIND-LUK-0004"],
  "Seligpreisungen und Weherufe sprechen wie Marias Lied von einer Umkehrung, die Gott herbeiführt: Wer jetzt arm ist, hungert und weint, wird getröstet; wer jetzt reich und satt ist, hat «seinen Trost schon erhalten» ([[LUK.6.24]]). Lukas meint dabei wirkliche Armut und wirklichen Hunger, nicht nur eine innere Haltung: Er spricht von den Armen (πτωχός) ohne den Zusatz «im Geist» und stellt ihnen die Reichen gegenüber. Die Seligpreisung ist zuerst eine Zusage an die Jünger, die alles verlassen haben ([[LUK.5.11]]; [[LUK.6.20]]), und eine Warnung an alle, die sich auf Besitz verlassen ([[LUK.12.15-LUK.12.21]]).",
  "probable",
  "Dass Lukas materielle Armut meint, legt der Gegensatz zu den Reichen nahe; ob er die Armen als solche seligpreist oder die armen Jünger, ist offen. Die Umkehrung wird als Werk Gottes beschrieben, nicht als menschliches Programm.",
  ["In der Sprache der Psalmen und der Texte aus Qumran sind die «Armen» (hebräisch עֲנָוִים) auch die Frommen, die ganz auf Gott angewiesen sind; dann ist die religiöse Bedeutung bei Lukas mitzuhören, wie Matthäus sie ausdrücklich macht (Vergleich mit [[MAT.5.3]]).",
   "Die Umkehrung kann als Verheissung für die kommende Welt verstanden werden, die das Jetzt nicht ändert, oder als Ansage, die schon jetzt Folgen hat, etwa im Teilen der Gemeinde ([[ACT.2.44-ACT.2.45]]; [[ACT.4.34]]). Lukas nennt beides: «jetzt» ([[LUK.6.21]]) und «Lohn im Himmel» ([[LUK.6.23]]).",
   "Gegen eine rein politische Lesart spricht, dass Lukas wohlhabende Menschen positiv darstellt, die ihren Besitz teilen (die Frauen in [[LUK.8.3]], Zachäus in [[LUK.19.8]]); verurteilt wird nicht jeder Besitz, sondern Reichtum, der sich selbst genügt."],
  [("grc", "πτωχός", "arm, bettelarm"), ("heb", "עֲנָוִים", "die Gebeugten, Demütigen; die Armen", "ʿanawim")],
  "D Säligpriisige und d Weheruef reded wie s Lied vo de Maria vo ere Umkehrig, wo Gott bewürkt: Wär jetzt arm isch, Hunger hät und briegget, wird tröschtet; wär jetzt riich und satt isch, hät «sin Troscht scho übercho» ([[LUK.6.24]]). De Lukas meint debii würklichi Armuet und würkliche Hunger, nöd nu e inneri Haltig: Er redt vo de Arme (πτωχός) ohni de Zuesatz «im Geischt» und stellt ine d Riiche gägenüber. D Säligpriisig isch zerscht e Zuesag a d Jünger, wo alles la ligge händ ([[LUK.5.11]]; [[LUK.6.20]]), und e Warnig a alli, wo sich uf de Bsitz verlönd ([[LUK.12.15-LUK.12.21]]).",
  "Dass de Lukas materielli Armuet meint, legt de Gägesatz zu de Riiche naach; öb er d Arme als settigi sälig priist oder di arme Jünger, isch offe. D Umkehrig wird als Wärch vo Gott beschribe, nöd als mänschlichs Programm.",
  ["I de Spraach vo de Psalme und vo de Text us Qumran sind d «Arme» (hebräisch עֲנָוִים) au di Fromme, wo ganz uf Gott aagwise sind; dänn isch di religiös Bedüütig bim Lukas mitzghöre, wie de Matthäus si usdrücklich macht (Vergliich mit [[MAT.5.3]]).",
   "D Umkehrig cha als Verheissig für di chömend Wält verstande wärde, wo am Jetzt nüüt änderet, oder als Aasag, wo scho jetzt Folge hät, öppe im Teile vo de Gmeind ([[ACT.2.44-ACT.2.45]]; [[ACT.4.34]]). De Lukas nännt beides: «jetzt» ([[LUK.6.21]]) und «Lohn im Himmel» ([[LUK.6.23]]).",
   "Gäge e rein politischi Läsart spricht, dass de Lukas riichi Mänsche positiv daarstellt, wo iren Bsitz teiled (d Fraue i [[LUK.8.3]], de Zachäus i [[LUK.19.8]]); verurteilt wird nöd jede Bsitz, sondern Riichtum, wo sich sälber gnüegt."],
  ["arm, bettelarm", "di Böigte, Demüetige; d Arme"]),
 ("INT-LUK-0004", U(2, 1, 20), ["FIND-LUK-0007", "BG-LUK-0003"],
  "Lukas erzählt die Geburt Jesu bewusst vor dem Hintergrund des Kaisers Augustus ([[LUK.2.1]]): Der Erlass des Herrschers über «die ganze Welt» bringt das Kind nach Betlehem, in die Stadt Davids. Die Botschaft der Engel gebraucht Worte, die auch in der Verehrung des Kaisers vorkamen: «gute Nachricht», «Retter» (σωτήρ), «Friede» ([[LUK.2.10-LUK.2.14]]). Dem Kaiser, der als Bringer des Friedens gefeiert wurde, steht das Kind in der Futterkrippe gegenüber; der eigentliche Retter ist nicht er.",
  "possible",
  "Ob Lukas die Sprache der Kaiserverehrung absichtlich aufnimmt, ist nicht beweisbar; die Wörter stammen ebenso aus der griechischen Bibel ([[ISA.52.7]]; [[ISA.9.6]]). Zu «Retter» in der Herrscherverehrung siehe BG-TIT-0004.",
  ["Die Angabe kann vor allem erklären, warum ein Kind aus Nazaret in Betlehem geboren wird, und Lukas' Interesse an der Zeitgeschichte zeigen (FIND-LUK-0007), ohne jede Spitze gegen Rom.",
   "Lukas stellt römische Beamte in der Apostelgeschichte oft wohlwollend dar (etwa [[ACT.18.12-ACT.18.17]]); eine scharfe Kritik am Kaiser passt nach Ansicht mancher nicht zu seinem Werk.",
   "Die geschichtlichen Schwierigkeiten der Angabe (QUESTION-LUK-0001) führen manche dazu, die Szene ganz als theologische Gestaltung zu lesen; andere halten an einem geschichtlichen Kern fest."],
  [("grc", "σωτήρ", "Retter, Heiland")],
  "De Lukas verzellt d Geburt vo Jesus bewusst vor em Hindergrund vom Kaiser Augustus ([[LUK.2.1]]): De Erlass vom Herrscher über «di ganz Wält» bringt s Chind uf Betlehem, i d Stadt vom David. D Botschaft vo de Ängel bruucht Wort, wo au i de Verehrig vom Kaiser vorchoo sind: «gueti Nachricht», «Retter» (σωτήρ), «Fride» ([[LUK.2.10-LUK.2.14]]). Em Kaiser, wo als Bringer vom Fride gfiiret worde isch, staat s Chind i de Fuetterchrippe gägenüber; de eigetlich Retter isch nöd er.",
  "Öb de Lukas d Spraach vo de Kaiserverehrig absichtlich ufnimmt, cha mer nöd bewiise; d Wörter stammed gnauso us de griechische Bible ([[ISA.52.7]]; [[ISA.9.6]]). Zu «Retter» i de Herrscherverehrig lueg BG-TIT-0004.",
  ["D Aagaab cha vor allem erkläre, werum es Chind us Nazaret z Betlehem gebore wird, und zeige, dass sich de Lukas für d Ziitgschicht interessiert (FIND-LUK-0007), ohni jedi Spitze gäge Rom.",
   "De Lukas stellt römischi Beamti i de Aposchtelgschicht oft wohlwollend daar (öppe [[ACT.18.12-ACT.18.17]]); e schaarfi Kritik am Kaiser passt nach de Meinig vo mängem nöd zu sim Wärch.",
   "D gschichtliche Schwirigkeite vo de Aagaab (QUESTION-LUK-0001) füered mängi dezue, d Szene ganz als theologischi Gstaltig z läse; anderi haltet a me gschichtliche Chern fescht."],
  ["Retter, Heiland"]),
 ("INT-LUK-0005", U(4, 14, 30), ["FIND-LUK-0008", "FIND-LUK-0006", "BG-LUK-0010"],
  "Die Predigt in Nazaret ist bei Lukas das Programm des ganzen Wirkens Jesu: Er ist mit dem Geist gesalbt, bringt Armen die gute Botschaft, Gefangenen Freilassung, Blinden das Augenlicht und ruft ein «Gnadenjahr» aus ([[LUK.4.18-LUK.4.19]]); darauf kommt Lukas zurück ([[LUK.7.22]]). Dass Jesus vor dem «Tag der Vergeltung» aufhört, betont die Zeit der Gnade. Die Ablehnung in der eigenen Stadt und die Hinweise auf Sarepta und Naaman deuten schon an, dass die Botschaft über Israel hinaus zu den Völkern gehen wird ([[LUK.2.32]]; [[ACT.13.46-ACT.13.47]]).",
  "probable",
  "Dass die Szene programmatisch gemeint ist, wird breit vertreten. Ob das Ende der Lesung eine bewusste Auslassung ist, lässt sich nicht beweisen; Lesungen konnten an Sinnabschnitten enden.",
  ["Das «Gnadenjahr» (ἐνιαυτὸς δεκτός) kann auf das Erlassjahr in [[LEV.25.10]] mit Schuldenerlass und Freilassung anspielen und dann eine soziale Erneuerung meinen (so in der Befreiungstheologie und bei John Howard Yoder, The Politics of Jesus, 1972). Andere verstehen es als Bild für die Heilszeit, ohne konkretes Programm.",
   "Dass sich die Wut erst an den Beispielen von Sarepta und Naaman entzündet, ist eine Deutung des Ablaufs. [[LUK.4.22]] kann schon als skeptische Reaktion gelesen werden («Ist das nicht der Sohn Josefs?»), und das Verb μαρτυρέω, hier «zustimmen», kann mit dem Dativ auch «gegen jemanden zeugen» heissen (so Joachim Jeremias).",
   "Die Beispiele aus der Elija- und Elischa-Geschichte werden von manchen nicht als Hinweis auf die spätere Mission gelesen, sondern als prophetische Kritik an Israel, wie sie bei den Propheten selbst vorkommt."],
  [("grc", "ἐνιαυτὸς δεκτός", "willkommenes Jahr, Gnadenjahr"), ("grc", "μαρτυρέω", "bezeugen; Zeugnis ablegen (für oder gegen)")],
  "D Predig z Nazaret isch bim Lukas s Programm vom ganze Wirke vo Jesus: Er isch mit em Geischt gsalbet, bringt Arme di gueti Botschaft, Gfangene d Freilassig, Blinde s Augeliecht und rüeft es «Gnadejahr» uus ([[LUK.4.18-LUK.4.19]]); da druf chunnt de Lukas zrugg ([[LUK.7.22]]). Dass de Jesus vor em «Tag vo de Vergältig» ufhört, betont d Ziit vo de Gnad. D Ablehnig i de eigete Stadt und d Hiiwiis uf Sarepta und de Naaman düüted scho aa, dass d Botschaft über Israel use zu de Völker gaat ([[LUK.2.32]]; [[ACT.13.46-ACT.13.47]]).",
  "Dass d Szene als Programm gmeint isch, vertrittet vili. Öb s Änd vo de Läsig e bewussti Uslassig isch, cha mer nöd bewiise; Läsige händ a Sinnabschnitt chöne ufhöre.",
  ["S «Gnadejahr» (ἐνιαυτὸς δεκτός) cha uf s Erlassjahr i [[LEV.25.10]] mit Schuldenerlass und Freilassig aaspile und dänn e soziali Erneuerig meine (so i de Befreiigstheologie und bim John Howard Yoder, The Politics of Jesus, 1972). Anderi verstönd s als Bild für d Heilsziit, ohni konkrets Programm.",
   "Dass d Wuet erscht a de Biispil vo Sarepta und vom Naaman uufchunnt, isch e Düütig vom Ablauf. [[LUK.4.22]] cha scho als skeptischi Reaktion gläse wärde («Isch das nöd de Sohn vom Josef?»), und s Verb μαρτυρέω, da «zuestimme», cha mit em Dativ au «gäge öpper züüge» heisse (so de Joachim Jeremias).",
   "D Biispil us de Gschicht vom Elija und vom Elischa läsed mängi nöd als Hiiwiis uf di spööter Mission, sondern als prophetischi Kritik a Israel, wie s si bi de Prophete sälber git."],
  ["willkommes Jahr, Gnadejahr", "bezüüge; Zügnis ablegge (für oder gäge)"]),
 ("INT-LUK-0006", U(6, 27, 36), ["FIND-LUK-0013"],
  "Die Feindesliebe ist die Mitte der Feldrede und wird mit Gottes eigenem Handeln begründet: Er «ist gütig gegen die Undankbaren und Bösen» ([[LUK.6.35]]); darum sollen die Jünger «barmherzig» sein wie der Vater ([[LUK.6.36]]). Die Beispiele (die andere Wange hinhalten, das Hemd nicht verweigern, jedem geben, [[LUK.6.29-LUK.6.30]]) sind zugespitzte Bilder: Sie sollen den Kreislauf von Vergeltung und blosser Gegenseitigkeit durchbrechen, den Jesus bei den «Sündern» sieht, die nur lieben, wer sie liebt ([[LUK.6.32-LUK.6.34]]). Massstab ist nicht eine Regel, sondern die Grosszügigkeit Gottes.",
  "probable",
  "Dass die Beispiele zugespitzt sind und nicht wörtlich als Gesetz gelten, ist eine verbreitete, aber nicht unbestrittene Auslegung.",
  ["Wörtliche Lesart: Die Gebote gelten, wie sie dastehen, auch als Verzicht auf Gewalt im Konflikt; so verstehen es seit dem 16. Jahrhundert viele Täufergemeinden und Friedenskirchen (etwa die Mennoniten).",
   "Walter Wink (Engaging the Powers, 1992) deutete das Hinhalten der Wange als gewaltfreien, aber selbstbewussten Widerstand, der den Angreifer blossstellt. Seine Erklärung stützt sich auf die «rechte Wange» bei Matthäus (Vergleich mit [[MAT.5.39]]), die Lukas nicht nennt.",
   "Die «Goldene Regel» ([[LUK.6.31]]) kann als Grundsatz der Gegenseitigkeit gelesen werden, den [[LUK.6.32-LUK.6.35]] gerade überbietet; andere sehen in ihr die Zusammenfassung der ganzen Rede."],
  [],
  "D Feindesliebi isch d Mitti vo de Fäldred und wird mit em eigete Handle vo Gott begründet: Er «isch güetig zu de Undankbare und Böse» ([[LUK.6.35]]); drum söled d Jünger «barmhärzig» sii wie de Vatter ([[LUK.6.36]]). D Biispil (di ander Backe aneha, s Hemp nöd verwehre, jedem gää, [[LUK.6.29-LUK.6.30]]) sind zuegspitzti Bilder: Si söled de Chreislauf vo Vergältig und blosser Gägesiitigkeit durebräche, wo de Jesus bi de «Sünder» gseht, wo nu die liebed, wo si liebed ([[LUK.6.32-LUK.6.34]]). De Massstab isch nöd e Regle, sondern d Grosszügigkeit vo Gott.",
  "Dass d Biispil zuegspitzt sind und nöd wörtlich als Gsetz gälted, isch e verbreiteti, aber nöd unbestritteni Uslegig.",
  ["Wörtlichi Läsart: D Gebot gälted, wie s dastaat, au als Verzicht uf Gwalt im Konflikt; so verstönd s sit em 16. Jahrhundert vili Täufergmeinde und Friedeschile (öppe d Mennonite).",
   "De Walter Wink (Engaging the Powers, 1992) hät s Aneha vo de Backe als gwaltfreie, aber sälbschtbewusste Widerstand düütet, wo de Aagriifer blossstellt. Sini Erklärig stützt sich uf di «rächt Backe» bim Matthäus (Vergliich mit [[MAT.5.39]]), wo de Lukas nöd nännt.",
   "D «Goldig Regle» ([[LUK.6.31]]) cha als Grundsatz vo de Gägesiitigkeit gläse wärde, wo [[LUK.6.32-LUK.6.35]] grad überbüütet; anderi gsehnd i ire d Zämefassig vo de ganze Red."],
  []),
 ("INT-LUK-0007", U(7, 36, 50), ["FIND-LUK-0022", "BG-LUK-0013"],
  "Die Liebe der Frau ist am ehesten Folge und Zeichen der Vergebung, nicht ihr Grund: Das Gleichnis ([[LUK.7.41-LUK.7.43]]) erzählt, dass mehr liebt, wem mehr geschenkt wurde, und der Nachsatz sagt: «wem aber wenig vergeben wird, der liebt wenig» ([[LUK.7.47]]). Das «denn» (ὅτι) nennt dann, woran man die Vergebung erkennt. Die Frau hat Vergebung schon erfahren oder ist ihrer gewiss, bevor sie kommt; Jesus spricht ihr zu, was schon gilt, und schreibt die Rettung ihrem Glauben zu ([[LUK.7.50]]).",
  "probable",
  "Die Übersetzung lässt mit «denn» beide Lesarten offen (siehe die Übersetzungsentscheidung zu [[LUK.7.47]]). Wann die Frau Vergebung erfahren hat, erzählt der Text nicht.",
  ["Wörtlich kann ὅτι den Grund angeben: Ihr ist vergeben, weil sie viel geliebt hat. So verstand es ein Teil der älteren katholischen Auslegung im Sinn einer Reue aus Liebe; die Reformatoren lehnten das ab. Die Grammatik allein entscheidet nicht.",
   "Das Perfekt ἀφέωνται («sind vergeben») in [[LUK.7.47-LUK.7.48]] kann einen schon bestehenden Zustand meinen oder die jetzt ausgesprochene Vergebung; je nachdem wird [[LUK.7.48]] als Bestätigung oder als Zuspruch gelesen.",
   "Manche halten [[LUK.7.47]] und das Gleichnis für ursprünglich getrennte Stücke, deren Logik nicht ganz zusammenpasst; dann lässt sich die Spannung nicht auflösen."],
  [("grc", "ὅτι", "denn, weil; dass"), ("grc", "ἀφέωνται", "sind vergeben (Perfekt von ἀφίημι)")],
  "D Liebi vo de Frau isch am eheschte Folg und Zeiche vo de Vergäbig, nöd ire Grund: S Gliichnis ([[LUK.7.41-LUK.7.43]]) verzellt, dass dä meh liebt, wo me meh gschänkt hät, und de Nachsatz seit: «wem aber wenig vergää wird, dä liebt wenig» ([[LUK.7.47]]). S «dänn» (ὅτι) nännt dänn, wora mer d Vergäbig erchännt. D Frau hät d Vergäbig scho erläbt oder isch sich ire sicher, bevor si chunnt; de Jesus seit ere zue, was scho gilt, und schriibt d Rettig irem Glaube zue ([[LUK.7.50]]).",
  "D Übersetzig laat mit «dänn» beidi Läsarte offe (lueg d Übersetzigsentscheidig zu [[LUK.7.47]]). Wänn d Frau d Vergäbig erläbt hät, verzellt de Text nöd.",
  ["Wörtlich cha ὅτι de Grund aagää: Ire isch vergää, wil si vil gliebt hät. So hät s en Teil vo de eltere katholische Uslegig verstande, im Sinn vo ere Rüü us Liebi; d Reformatore händ das abglehnt. D Grammatik elei entscheidet nöd.",
   "S Perfekt ἀφέωνται («sind vergää») i [[LUK.7.47-LUK.7.48]] cha en Zuestand meine, wo scho bestaat, oder d Vergäbig, wo jetzt usgsproche wird; je nachdem wird [[LUK.7.48]] als Bestätigung oder als Zuespruch gläse.",
   "Mängi halted [[LUK.7.47]] und s Gliichnis für Stück, wo ursprünglich trännt gsii sind und wo iri Logik nöd ganz zämepasst; dänn laat sich d Spannig nöd uflöse."],
  ["dänn, wil; dass", "sind vergää (Perfekt vo ἀφίημι)"]),
 ("INT-LUK-0008", U(9, 51, 56), ["FIND-LUK-0015", "FIND-LUK-0014"],
  "Der Reisebericht ist weniger eine Wegbeschreibung als eine Komposition: Lukas sammelt unter dem Ziel Jerusalem Lehre für die Jünger, die den Weg Jesu mitgehen. Die «Aufnahme» (ἀνάλημψις, [[LUK.9.51]]) umfasst Leiden, Tod, Auferstehung und Himmelfahrt (vgl. [[ACT.1.2]]; [[ACT.1.11]]); den Weg dorthin geht Jesus bewusst («er richtete sein Angesicht fest»). Die Anklänge an Elija (FIND-LUK-0014) zeigen Jesus als Propheten, der wie Elija in den Himmel aufgenommen wird ([[2KI.2.9-2KI.2.11]]), aber das Strafwunder des Elija ablehnt ([[LUK.9.54-LUK.9.55]]).",
  "probable",
  "Dass die Reise literarisch gestaltet ist, wird weit vertreten; daraus folgt nicht, dass Jesus nicht nach Jerusalem gezogen ist.",
  ["Manche verstehen ἀνάλημψις enger als Tod («aus dem Leben genommen werden») oder nur als Himmelfahrt; die Übersetzung lässt es mit «Aufnahme» offen.",
   "Hans Conzelmann (Die Mitte der Zeit, 1954) sah in der Reise vor allem ein theologisches Schema; andere halten die wenigen Ortsangaben für Reste einer wirklichen Reiseüberlieferung, die Lukas mit Redestoff aufgefüllt hat.",
   "Ob die Anklänge an Elija Jesus als neuen Elija, als den Propheten wie Mose ([[DEU.18.15]]; vgl. [[LUK.9.35]]) oder als den, der beide überbietet, zeigen sollen, wird verschieden beantwortet; die Zurechtweisung in [[LUK.9.55]] spricht gegen eine einfache Gleichsetzung."],
  [("grc", "ἀνάλημψις", "Aufnahme, Hinaufnahme; auch Tod, Hinscheiden")],
  "De Reisebricht isch weniger e Wägbeschriibig als e Komposition: De Lukas sammlet under em Ziil Jerusalem Lehr für d Jünger, wo de Wäg vo Jesus mitgönd. D «Ufnaam» (ἀνάλημψις, [[LUK.9.51]]) umfasst Liide, Tod, Uferstehig und Himmelfahrt (vgl. [[ACT.1.2]]; [[ACT.1.11]]); de Wäg dethii gaat de Jesus bewusst («er hät sis Gsicht fescht grichtet»). D Aakläng a de Elija (FIND-LUK-0014) zeiged de Jesus als Prophet, wo wie de Elija in Himmel ufgnoo wird ([[2KI.2.9-2KI.2.11]]), aber s Strafwunder vom Elija ablehnt ([[LUK.9.54-LUK.9.55]]).",
  "Dass d Reis literarisch gstaltet isch, vertrittet vili; drus folgt nöd, dass de Jesus nöd uf Jerusalem zoge isch.",
  ["Mängi verstönd ἀνάλημψις änger als Tod («us em Läbe gnoo wärde») oder nu als Himmelfahrt; d Übersetzig laat s mit «Ufnaam» offe.",
   "De Hans Conzelmann (Die Mitte der Zeit, 1954) hät i de Reis vor allem es theologischs Schema gseh; anderi haltet di wenige Ortsaagaabe für Räscht vo ere würkliche Reiseüberliferig, wo de Lukas mit Redestoff ufgfüllt hät.",
   "Öb d Aakläng a de Elija de Jesus als nöie Elija, als de Prophet wie de Mose ([[DEU.18.15]]; vgl. [[LUK.9.35]]) oder als dä, wo beidi überbüütet, zeige söled, wird verschide beantwortet; d Zrächtwiisig i [[LUK.9.55]] spricht gäge e eifachi Gliichsetzig."],
  ["Ufnaam, Ufenaam; au Tod, Stärbe"]),
 ("INT-LUK-0009", U(10, 17, 20), ["FIND-LUK-0027"],
  "Das Wort vom Sturz des Satans deutet die Sendung der Zweiundsiebzig: Wo das Reich Gottes verkündet wird und Kranke geheilt werden ([[LUK.10.9]]), ist die Macht des Bösen schon gebrochen. Wie in [[LUK.11.20-LUK.11.22]] ist das Reich Gottes im Wirken Jesu gegenwärtig: Der «Stärkere» hat den Starken besiegt. Zugleich nimmt Jesus der Freude über den Erfolg ihr Gewicht: Grund zur Freude ist die Zugehörigkeit zu Gott ([[LUK.10.20]]).",
  "possible",
  "Das Imperfekt ἐθεώρουν («ich sah») lässt offen, wann und wie Jesus das sah (siehe die Übersetzungsentscheidung zu [[LUK.10.18]]).",
  ["Manche lesen das Wort als Bericht einer Vision Jesu, etwa bei der Taufe oder während der Sendung, ohne damit eine Aussage über das Reich Gottes zu verbinden.",
   "Andere verbinden es mit dem Sturz des «Morgensterns» in [[ISA.14.12]] und mit Vorstellungen eines Sturzes Satans vor aller Zeit; dann spricht Jesus von einem urzeitlichen Ereignis. Das passt weniger zum Anlass, dem Bericht der Zurückgekehrten.",
   "Wieder andere sehen einen Ausblick auf das Endgericht (vgl. [[REV.12.7-REV.12.9]]): Was bei der Sendung geschieht, nimmt den endgültigen Sieg vorweg."],
  [("grc", "ἐθεώρουν", "ich sah, ich schaute (Imperfekt von θεωρέω)")],
  "S Wort vom Sturz vom Satan düütet d Sändig vo de Zweiesibezg: Wo s Riich vo Gott verchündet wird und Chranki gheilt wärded ([[LUK.10.9]]), isch d Macht vom Böse scho broche. Wie i [[LUK.11.20-LUK.11.22]] isch s Riich vo Gott im Wirke vo Jesus scho da: De «Stärcher» hät de Starch besiegt. Zuglich nimmt de Jesus de Fröid über de Erfolg ires Gwicht: De Grund zur Fröid isch, dass mer zu Gott ghört ([[LUK.10.20]]).",
  "S Imperfekt ἐθεώρουν («ich ha gseh») laat offe, wänn und wie de Jesus das gseh hät (lueg d Übersetzigsentscheidig zu [[LUK.10.18]]).",
  ["Mängi läsed s Wort als Bricht vo ere Vision vo Jesus, öppe bi de Taufi oder wäred de Sändig, ohni demit e Ussag über s Riich vo Gott z verbinde.",
   "Anderi verbinded s mit em Sturz vom «Morgestärn» i [[ISA.14.12]] und mit Vorstellige vo me Sturz vom Satan vor aller Ziit; dänn redt de Jesus vo me Ereignis us de Urziit. Das passt weniger zum Aalass, em Bricht vo dene, wo zruggchoo sind.",
   "Wider anderi gsehnd en Usblick uf s Ändgricht (vgl. [[REV.12.7-REV.12.9]]): Was bi de Sändig passiert, nimmt de ändgültig Sieg voruus."],
  ["ich ha gseh, ich ha gluegt (Imperfekt vo θεωρέω)"]),
 ("INT-LUK-0010", U(10, 25, 37), ["FIND-LUK-0018", "FIND-LUK-0017", "BG-LUK-0016"],
  "Das Gleichnis beantwortet die Frage «Wer ist mein Nächster?» nicht mit einer Abgrenzung, sondern kehrt sie um: Nicht wer Hilfe verdient, ist die Frage, sondern wer zum Nächsten wird. Dass ausgerechnet ein Samaritaner, einer aus einer verachteten und feindlich gesinnten Gruppe ([[LUK.9.52-LUK.9.53]]), das Gebot erfüllt, während Priester und Levit vorübergehen, ist die eigentliche Herausforderung für den Gesetzeslehrer. Der Schluss «Geh, und handle du ebenso!» verlangt Tun, nicht nur Wissen ([[LUK.10.28]]; [[LUK.10.37]]).",
  "probable",
  "Die Deutung als Beispielerzählung für tätige Nächstenliebe ist die verbreitetste und am Text gut begründet.",
  ["Die altkirchliche Auslegung las das Gleichnis allegorisch: Der Überfallene ist Adam bzw. die Menschheit, die Räuber sind die bösen Mächte, der Samaritaner ist Christus, die Herberge die Kirche (so Origenes, Homilien zum Lukasevangelium 34; Augustinus, Quaestiones evangeliorum 2,19). Der Text selbst gibt keine solchen Gleichungen vor.",
   "Manche sehen den Schwerpunkt darin, sich in die Lage des Überfallenen zu versetzen, dem ausgerechnet ein Feind hilft; dann geht es auch darum, Hilfe von einem Verachteten anzunehmen.",
   "Ob Priester und Levit aus Furcht vor Unreinheit an einem vermeintlich Toten vorbeigingen ([[LEV.21.1-LEV.21.3]]; [[NUM.19.11]]), sagt das Gleichnis nicht; diese Erklärung ist umstritten (BG-LUK-0016) und kann dazu verleiten, das Judentum als solches zu kritisieren, was der Text nicht tut."],
  [],
  "S Gliichnis beantwortet d Frag «Wär isch min Nächscht?» nöd mit ere Abgränzig, sondern chert si um: Nöd wär Hilf verdient, isch d Frag, sondern wär zum Nächschte wird. Dass usgrächnet en Samaritaner, eine us ere verachtete und feindlich gsinnte Gruppe ([[LUK.9.52-LUK.9.53]]), s Gebot erfüllt, wäred Prieschter und Levit verbiigönd, isch di eigetlich Useforderig für de Gsetzeslehrer. De Schluss «Gang, und mach du s gliich!» verlangt Tue, nöd nu Wüsse ([[LUK.10.28]]; [[LUK.10.37]]).",
  "D Düütig als Biispilgschicht für Nächschteliebi, wo öppis tuet, isch di verbreitetscht und am Text guet begründet.",
  ["Di alt Chile hät s Gliichnis allegorisch gläse: De Überfallni isch de Adam oder d Mänschheit, d Röiber sind di böse Mächt, de Samaritaner isch de Christus, d Herbärg d Chile (so de Origenes, Predige zum Lukasevangelium 34; de Augustinus, Quaestiones evangeliorum 2,19). De Text sälber git kei settigi Gliichige vor.",
   "Mängi gsehnd de Schwärpunkt drin, sich i d Laag vom Überfallne z versetze, wo em usgrächnet en Feind hilft; dänn gaat s au drum, Hilf vo me Verachtete aaznää.",
   "Öb Prieschter und Levit us Angscht vor Unreinheit a me vermeintlich Tote verbiigange sind ([[LEV.21.1-LEV.21.3]]; [[NUM.19.11]]), seit s Gliichnis nöd; die Erklärig isch umstritte (BG-LUK-0016) und cha dezue verleite, s Judetum als settigs z kritisiere, was de Text nöd macht."],
  []),
 ("INT-LUK-0011", U(10, 38, 42), ["FIND-LUK-0012", "FIND-LUK-0018", "BG-LUK-0017"],
  "Maria sitzt «zu den Füssen Jesu» und hört seinem Wort zu ([[LUK.10.39]]): Das ist die Haltung einer Schülerin vor ihrem Lehrer (vgl. [[ACT.22.3]]). Jesus nimmt ihr diesen Platz nicht weg ([[LUK.10.42]]). Seine Antwort an Marta kritisiert nicht das Dienen, sondern das Sich-Sorgen und Aufgeregtsein (μεριμνάω, θορυβάζομαι; [[LUK.10.41]]), das auch die Saat des Wortes erstickt ([[LUK.8.14]]). Nach dem Samaritaner, der zeigt, wie man handelt, zeigt Maria, dass das Hören auf Jesus dem Handeln zugrunde liegt.",
  "possible",
  "Lukas zeichnet Marta nicht als Gegenbild: Sie nimmt Jesus auf ([[LUK.10.38]]), und er redet sie zweimal mit Namen an.",
  ["Die Auslegungsgeschichte hat die Szene oft als Rangordnung des betrachtenden über das tätige Leben gelesen (seit Origenes und Augustinus, im Mittelalter besonders für das Klosterleben); das geht über den Text hinaus.",
   "Meister Eckhart deutete in einer Predigt umgekehrt Marta als die Reifere, die mitten im Tun gesammelt bleibt; auch das ist eine eigene theologische Deutung.",
   "Feministische Auslegungen sehen hier entweder eine Befreiung der Frau zum Lernen oder im Gegenteil eine Beschränkung auf stilles Zuhören statt Dienst und Leitung (etwa Elisabeth Schüssler Fiorenza)."],
  [("grc", "μεριμνάω", "sich sorgen, sich kümmern"), ("grc", "θορυβάζομαι", "sich aufregen, beunruhigt sein")],
  "D Maria sitzt «zu de Füess vom Jesus» und lost sim Wort zue ([[LUK.10.39]]): Das isch d Haltig vo ere Schüelerin vor irem Lehrer (vgl. [[ACT.22.3]]). De Jesus nimmt ere dä Platz nöd wäg ([[LUK.10.42]]). Sini Antwort a d Marta kritisiert nöd s Diene, sondern s Sich-Sorge-Mache und s Ufgregtsii (μεριμνάω, θορυβάζομαι; [[LUK.10.41]]), wo au d Saat vom Wort verstickt ([[LUK.8.14]]). Nach em Samaritaner, wo zeigt, wie mer handlet, zeigt d Maria, dass s Lose uf de Jesus em Handle zgrund liit.",
  "De Lukas zeichnet d Marta nöd als Gägebild: Si nimmt de Jesus uf ([[LUK.10.38]]), und er redt si zwei Mal mit Name aa.",
  ["D Gschicht vo de Uslegig hät d Szene oft als Rangornig vom betrachtende über s tätig Läbe gläse (sit em Origenes und em Augustinus, im Mittelalter bsunders für s Chloschterläbe); das gaat über de Text use.",
   "De Meischter Eckhart hät i ere Predig umgekehrt d Marta als di Riifer düütet, wo mitten im Tue gsammlet bliibt; au das isch e eigeti theologischi Düütig.",
   "Feministischi Uslegige gsehnd da entweder e Befreiig vo de Frau zum Lehre oder im Gägeteil e Beschränkig uf stills Zuelose statt Dienscht und Leitig (öppe d Elisabeth Schüssler Fiorenza)."],
  ["sich Sorge mache, sich kümmere", "sich ufrege, unruhig sii"]),
 ("INT-LUK-0012", U(11, 5, 13), ["FIND-LUK-0019"],
  "Das Wort ἀναίδεια («Schamlosigkeit», [[LUK.11.8]]) bezieht sich am ehesten auf den Bittenden, der sich mitten in der Nacht nicht abweisen lässt. Das Gleichnis ermutigt dann zu beharrlichem, unverlegenem Bitten; der Schluss «wie viel mehr» ([[LUK.11.13]]) zeigt, dass Gott nicht widerwillig ist wie der geweckte Freund, sondern gerne gibt. Ausdrücklich verheissen ist der Heilige Geist, nicht die Erfüllung jedes Wunsches.",
  "possible",
  "Grammatisch kann sich «seine» Schamlosigkeit auf beide Männer beziehen (siehe die Übersetzungsentscheidung zu [[LUK.11.8]]).",
  ["Kenneth E. Bailey (Poet and Peasant, 1976) bezog das Wort auf den Schlafenden: Er steht auf, um nicht als schamlos dazustehen, weil das ganze Dorf die Ehre der Gastfreundschaft teilt. Dann geht es nicht um Hartnäckigkeit, sondern darum, dass man sich auf Gottes Ehre verlassen kann.",
   "Das Wort hat im Griechischen einen negativen Klang (Unverschämtheit); dass Jesus es zustimmend gebraucht, ist auffällig. Manche übersetzen abgeschwächt mit «Beharrlichkeit», was die Schärfe nimmt.",
   "Im Gleichnis von der bittenden Witwe ([[LUK.18.1-LUK.18.8]]) ist Beharrlichkeit bei Lukas ausdrücklich das Thema; das stützt den Bezug auf den Bittenden."],
  [("grc", "ἀναίδεια", "Schamlosigkeit, Unverschämtheit")],
  "S Wort ἀναίδεια («Schamlosigkeit», [[LUK.11.8]]) bezieht sich am eheschte uf dä, wo bittet und sich mitten i de Nacht nöd la abwiise. S Gliichnis ermuetiget dänn, beharrlich und ohni Hemmige z bitte; de Schluss «wie vil meh» ([[LUK.11.13]]) zeigt, dass Gott nöd widerwillig isch wie de gweckt Fründ, sondern gern git. Usdrücklich verheisse isch de Heilig Geischt, nöd dass jede Wunsch erfüllt wird.",
  "Grammatisch cha sich «sini» Schamlosigkeit uf beidi Manne bezie (lueg d Übersetzigsentscheidig zu [[LUK.11.8]]).",
  ["De Kenneth E. Bailey (Poet and Peasant, 1976) hät s Wort uf dä bezoge, wo schlaaft: Er staat uf, demit er nöd als schamlos dastaat, wil s ganz Dorf d Ehr vo de Gaschtfründschaft teilt. Dänn gaat s nöd um Hartnäckigkeit, sondern drum, dass mer sich uf d Ehr vo Gott cha verlaa.",
   "S Wort hät im Griechische en negative Klang (Uverschämtheit); dass de Jesus s zuestimmend bruucht, fallt uf. Mängi übersetzed abgschwächt mit «Beharrlichkeit», was em d Schärfi nimmt.",
   "Im Gliichnis vo de Witwe, wo bittet ([[LUK.18.1-LUK.18.8]]), isch Beharrlichkeit bim Lukas usdrücklich s Thema; das stützt de Bezug uf dä, wo bittet."],
  ["Schamlosigkeit, Uverschämtheit"]),
 ("INT-LUK-0013", U(12, 13, 21), ["FIND-LUK-0021"],
  "Das Gleichnis verurteilt nicht das Ernten und Vorsorgen an sich, sondern ein Leben, das nur um sich selbst kreist: Der reiche Mann redet nur mit sich, sieht im Überfluss nur sich selbst und plant, als gehöre ihm auch die Zeit. Gott nennt ihn einen «Toren» (ἄφρων), wie der Psalm den nennt, der in seinem Herzen sagt, es gebe keinen Gott ([[PSA.14.1]]). «Reich bei Gott» ([[LUK.12.21]]) wird nach dem Folgenden, wer teilt und Almosen gibt ([[LUK.12.33-LUK.12.34]]).",
  "probable",
  "Was «reich bei Gott» genau heisst, sagt [[LUK.12.21]] nicht; die Deutung über [[LUK.12.33]] ist eine Verbindung im Zusammenhang.",
  ["Manche lesen das Gleichnis vor allem als Mahnung an die Sterblichkeit: Nicht Habgier, sondern das Vergessen des Todes ist der Fehler des Mannes (vgl. [[PSA.49.16-PSA.49.20]]; [[ECC.2.18-ECC.2.21]] und das Buch Jesus Sirach, Kapitel 11).",
   "Andere betonen die soziale Seite: Wer in einer Gesellschaft knapper Güter Getreide hortet, entzieht es anderen; der Mann plant keine Hilfe für Arme.",
   "Wieder andere sehen in [[LUK.12.33]] («Verkauft euren Besitz») eine Forderung an alle Jünger, wie sie in [[LUK.18.22]] einem Einzelnen gilt; ob das allgemein oder für bestimmte Menschen gilt, ist umstritten."],
  [("grc", "ἄφρων", "Tor, unvernünftig, ohne Einsicht")],
  "S Gliichnis verurteilt nöd s Ärnte und Vorsorge a sich, sondern es Läbe, wo nu um sich sälber chreist: De riich Maa redt nu mit sich, gseht im Überfluss nu sich sälber und plant, wie wänn em au d Ziit ghörti. Gott nännt en en «Narr» (ἄφρων), wie de Psalm dä nännt, wo i sim Härz seit, es gäb kein Gott ([[PSA.14.1]]). «Riich bi Gott» ([[LUK.12.21]]) wird nach em Nööchschte, wär teilt und Almose git ([[LUK.12.33-LUK.12.34]]).",
  "Was «riich bi Gott» gnau heisst, seit [[LUK.12.21]] nöd; d Düütig über [[LUK.12.33]] isch e Verbindig im Zämehang.",
  ["Mängi läsed s Gliichnis vor allem als Mahnig, dass mer stärblich isch: Nöd d Habgier, sondern dass er de Tod vergisst, isch de Fääler vom Maa (vgl. [[PSA.49.16-PSA.49.20]]; [[ECC.2.18-ECC.2.21]] und das Buch Jesus Sirach, Kapitel 11).",
   "Anderi betoned di sozial Siite: Wär i ere Gsellschaft mit knappe Güeter Getreid hortet, nimmt s andere wäg; de Maa plant kei Hilf für Armi.",
   "Wider anderi gsehnd i [[LUK.12.33]] («Verchaufed eue Bsitz») e Forderig a alli Jünger, wie si i [[LUK.18.22]] für en Einzelne gilt; öb das allgemein oder für bestimmti Mänsche gilt, isch umstritte."],
  ["Narr, unvernünftig, ohni Iisicht"]),
 ("INT-LUK-0014", U(12, 49, 53), ["FIND-LUK-0015", "FIND-LUK-0003"],
  "Mit dem «Feuer» ([[LUK.12.49]]) nimmt Jesus wohl die Ankündigung des Täufers auf, der Kommende werde «mit heiligem Geist und Feuer taufen» ([[LUK.3.16]]). Bevor das Feuer brennt, muss er selbst eine «Taufe» erleiden ([[LUK.12.50]]): sein Leiden in Jerusalem, auf das er zugeht (FIND-LUK-0015). Die angekündigte «Spaltung» ([[LUK.12.51-LUK.12.53]]) ist nicht Absicht, sondern Folge: Seine Botschaft zwingt zur Entscheidung, auch in Familien; das Bild nimmt [[MIC.7.6]] auf.",
  "possible",
  "Der Satz in [[LUK.12.49]] ist sprachlich schwer (siehe die Übersetzungsentscheidung); die Deutung des Feuers ist offen.",
  ["Feuer kann das Gericht meinen wie in [[LUK.3.17]] und [[LUK.9.54]]; dann wünscht Jesus das Gericht herbei, was in Spannung zu [[LUK.9.55]] steht.",
   "Andere verbinden das Feuer mit dem Pfingstgeschehen, bei dem «Zungen wie von Feuer» erscheinen ([[ACT.2.3]]); dann meint es den Geist, der nach Jesu Tod kommt.",
   "Feuer als Läuterung: Es reinigt und scheidet (vgl. [[MAL.3.2-MAL.3.3]]); die Spaltung in [[LUK.12.52-LUK.12.53]] wäre dann diese Scheidung."],
  [],
  "Mit em «Füür» ([[LUK.12.49]]) nimmt de Jesus wohl d Aakündigung vom Täufer uf, dä, wo chunnt, wärdi «mit heilige Geischt und Füür taufe» ([[LUK.3.16]]). Bevor s Füür brännt, mues er sälber e «Taufi» erliide ([[LUK.12.50]]): sis Liide z Jerusalem, wo er druf zuegaat (FIND-LUK-0015). D «Spaltig», won er aachündet ([[LUK.12.51-LUK.12.53]]), isch nöd Absicht, sondern Folg: Sini Botschaft zwingt zur Entscheidig, au i Familie; s Bild nimmt [[MIC.7.6]] uf.",
  "De Satz i [[LUK.12.49]] isch sprachlich schwirig (lueg d Übersetzigsentscheidig); wie mer s Füür düütet, isch offe.",
  ["Füür cha s Gricht meine wie i [[LUK.3.17]] und [[LUK.9.54]]; dänn wünscht sich de Jesus s Gricht häre, was i Spannig zu [[LUK.9.55]] staat.",
   "Anderi verbinded s Füür mit em Pfingschtereignis, wo «Zunge wie vo Füür» erschiined ([[ACT.2.3]]); dänn meint s de Geischt, wo nach em Tod vo Jesus chunnt.",
   "Füür als Lüüterig: Es reiniget und scheidet (vgl. [[MAL.3.2-MAL.3.3]]); d Spaltig i [[LUK.12.52-LUK.12.53]] wär dänn die Scheidig."],
  []),
 ("INT-LUK-0015", U(9, 23, 27), ["FIND-LUK-0016", "FIND-LUK-0015"],
  "Mit «Tag für Tag» (καθ᾽ ἡμέραν, [[LUK.9.23]]) richtet Lukas das Kreuztragen auf das tägliche Leben der Jünger aus: Nachfolge besteht nicht nur in einem einmaligen Martyrium, sondern in der täglichen Bereitschaft, sich selbst nicht zum Massstab zu machen. Das passt zu Lukas' Aufmerksamkeit für Alltag und Besitz (FIND-LUK-0021) und zu den Nachfolgeworten auf dem Weg ([[LUK.9.57-LUK.9.62]]).",
  "possible",
  "Die Wendung fehlt in einem Teil der Handschriften (siehe die Alternative zu [[LUK.9.23]]); der SBLGNT hat sie.",
  ["Manche sehen darin eine Abschwächung des ursprünglich wörtlich gemeinten Rufs zum Martyrium; [[LUK.9.24]] und [[LUK.12.4-LUK.12.9]] zeigen aber, dass Lukas den Tod um Jesu willen nicht ausblendet.",
   "Andere verstehen «Tag für Tag» als Hinweis auf die lange Zeit der Kirche bis zum Kommen des Menschensohnes ([[LUK.9.26-LUK.9.27]])."],
  [("grc", "καθ᾽ ἡμέραν", "Tag für Tag, täglich")],
  "Mit «Tag für Tag» (καθ᾽ ἡμέραν, [[LUK.9.23]]) richtet de Lukas s Chrüüztrage uf s täglich Läbe vo de Jünger uus: Nachfolg bestaat nöd nu i eme einmalige Martyrium, sondern i de tägliche Bereitschaft, sich sälber nöd zum Massstab z mache. Das passt dezue, dass de Lukas uf Alltag und Bsitz achtet (FIND-LUK-0021), und zu de Wort über d Nachfolg uf em Wäg ([[LUK.9.57-LUK.9.62]]).",
  "D Wändig fäält i eme Teil vo de Handschrifte (lueg d Alternative zu [[LUK.9.23]]); de SBLGNT hät si.",
  ["Mängi gsehnd drin e Abschwächig vom Ruef zum Martyrium, wo ursprünglich wörtlich gmeint gsii seg; [[LUK.9.24]] und [[LUK.12.4-LUK.12.9]] zeiged aber, dass de Lukas de Tod wäge Jesus nöd usbländet.",
   "Anderi verstönd «Tag für Tag» als Hiiwiis uf di lang Ziit vo de Chile bis zum Choo vom Mänschesohn ([[LUK.9.26-LUK.9.27]])."],
  ["Tag für Tag, täglich"]),
]

# (id, gestützt auf, Aussage, Konfidenz | Mundart). Die erste Stellen-Marke bestimmt den Abschnitt in der App.
PRINCIPLES = [
 ("PRIN-LUK-0001", ["FIND-LUK-0005", "INT-LUK-0003"],
  "Gott wendet sich den Niedrigen, Armen und Hungernden zu; wer reich und satt ist, hat darin keine Sicherheit vor Gott ([[LUK.6.20-LUK.6.26]]; [[LUK.1.51-LUK.1.53]]).", "probable",
  "Gott wändet sich de Niedrige, Arme und Hungrige zue; wär riich und satt isch, hät drin kei Sicherheit vor Gott ([[LUK.6.20-LUK.6.26]]; [[LUK.1.51-LUK.1.53]])."),
 ("PRIN-LUK-0002", ["FIND-LUK-0008", "FIND-LUK-0023", "INT-LUK-0005"],
  "Die gute Botschaft Jesu gilt zuerst den Armen, Gefangenen, Kranken und Ausgeschlossenen, und sie überschreitet die Grenzen des eigenen Volkes ([[LUK.4.18-LUK.4.27]]; [[LUK.7.22]]).", "probable",
  "Di gueti Botschaft vo Jesus gilt zerscht de Arme, Gfangene, Chranke und Usgschlossne, und si überschriitet d Gränze vom eigete Volk ([[LUK.4.18-LUK.4.27]]; [[LUK.7.22]])."),
 ("PRIN-LUK-0003", ["FIND-LUK-0009", "FIND-LUK-0019", "INT-LUK-0012"],
  "Beten gehört zu den Wendepunkten des Lebens; wer bittet, darf mit einem Vater rechnen, der gerne gibt, vor allem seinen Geist ([[LUK.11.5-LUK.11.13]]; [[LUK.6.12-LUK.6.13]]).", "probable",
  "S Bätte ghört zu de Wändepünkt vom Läbe; wär bittet, dörf mit eme Vatter rächne, wo gern git, vor allem sin Geischt ([[LUK.11.5-LUK.11.13]]; [[LUK.6.12-LUK.6.13]])."),
 ("PRIN-LUK-0004", ["FIND-LUK-0013", "INT-LUK-0006"],
  "Die Liebe der Jünger richtet sich nach Gottes Güte, die auch den Undankbaren gilt, nicht nach Gegenseitigkeit ([[LUK.6.27-LUK.6.36]]).", "probable",
  "D Liebi vo de Jünger richtet sich nach de Güeti vo Gott, wo au de Undankbare gilt, nöd nach Gägesiitigkeit ([[LUK.6.27-LUK.6.36]])."),
 ("PRIN-LUK-0005", ["FIND-LUK-0022", "INT-LUK-0007"],
  "Wer Vergebung erfährt, antwortet mit Liebe; wer sich selbst für gerecht hält, erkennt die eigene Schuld und die Liebe der anderen schwer ([[LUK.7.36-LUK.7.50]]; [[LUK.5.31-LUK.5.32]]).", "probable",
  "Wär Vergäbig erläbt, antwortet mit Liebi; wär sich sälber für grächt haltet, erchännt di eige Schuld und d Liebi vo de andere schwär ([[LUK.7.36-LUK.7.50]]; [[LUK.5.31-LUK.5.32]])."),
 ("PRIN-LUK-0006", ["FIND-LUK-0017", "FIND-LUK-0018", "INT-LUK-0010"],
  "Nächstenliebe fragt nicht zuerst, wer dazugehört, sondern wird dem zum Nächsten, der Hilfe braucht, auch über Gruppen- und Feindbilder hinweg ([[LUK.10.25-LUK.10.37]]; [[LUK.9.52-LUK.9.55]]).", "probable",
  "D Nächschteliebi fröget nöd zerscht, wär dezueghört, sondern wird für dä zum Nächschte, wo Hilf bruucht, au über Gruppe- und Feindbilder ewägg ([[LUK.10.25-LUK.10.37]]; [[LUK.9.52-LUK.9.55]])."),
 ("PRIN-LUK-0007", ["FIND-LUK-0024", "INT-LUK-0011"],
  "Das Wort Jesu zu hören und danach zu handeln hat Vorrang vor Herkunft, Betriebsamkeit und Sorge ([[LUK.8.18-LUK.8.21]]; [[LUK.10.38-LUK.10.42]]; [[LUK.6.46-LUK.6.49]]).", "probable",
  "S Wort vo Jesus z ghöre und denaa z handle hät Vorrang vor Härkunft, Betriebsamkeit und Sorge ([[LUK.8.18-LUK.8.21]]; [[LUK.10.38-LUK.10.42]]; [[LUK.6.46-LUK.6.49]])."),
 ("PRIN-LUK-0008", ["FIND-LUK-0021", "INT-LUK-0013"],
  "Das Leben besteht nicht aus Besitz; Habgier und Sorge verlieren ihre Macht, wo Menschen Gott vertrauen, sein Reich suchen und teilen ([[LUK.12.15-LUK.12.34]]).", "probable",
  "S Läbe bestaat nöd us Bsitz; Habgier und Sorge verlüüred iri Macht, wo Mänsche Gott vertroued, sis Riich sueched und teiled ([[LUK.12.15-LUK.12.34]])."),
 ("PRIN-LUK-0009", ["FIND-LUK-0015", "INT-LUK-0008", "INT-LUK-0015"],
  "Nachfolge ist eine tägliche, entschiedene Bindung an Jesus auf seinem Weg; Gewalt gegen Menschen, die ablehnen, gehört nicht dazu ([[LUK.9.23-LUK.9.24]]; [[LUK.9.51-LUK.9.62]]).", "possible",
  "Nachfolg isch e täglichi, entschideni Bindig a de Jesus uf sim Wäg; Gwalt gäge Mänsche, wo ablehned, ghört nöd dezue ([[LUK.9.23-LUK.9.24]]; [[LUK.9.51-LUK.9.62]])."),
]

# (id, Grundsatz, Aussage, Grenzen | Mundart: Aussage, Grenzen) – Zielgruppe CTX-CH-DE-2026 (in _study.py festgelegt)
APPLICATIONS = [
 ("APP-LUK-0001", "PRIN-LUK-0001",
  "Wer in gesichertem Wohlstand lebt, kann die Weherufe als persönliche Anfrage lesen: Worauf verlasse ich mich, und wem kommt mein Überfluss zugute? Gemeinden können prüfen, ob armutsbetroffene Menschen bei ihnen Platz und Stimme haben.",
  "Der Text verheisst keine Umkehr der Verhältnisse durch menschliche Politik und rechtfertigt keinen Neid; er verurteilt Menschen nicht, weil sie etwas besitzen. Armut wird nicht verklärt: Hunger und Weinen sind Not, kein Ideal.",
  "Wär i gsichertem Wohlstand läbt, cha d Weheruef als persönlichi Aafrag läse: Uf was verlaa ich mich, und wem chunnt min Überfluss zguet? Gmeinde chönd prüefe, öb Mänsche, wo vo Armuet betroffe sind, bi ine Platz und e Stimm händ.",
  "De Text verheisst kei Umkehrig vo de Verhältnis dur mänschlichi Politik und rächtfertiget kein Niid; er verurteilt Mänsche nöd, wil si öppis bsitzed. D Armuet wird nöd verklärt: Hunger und Briegge sind Not, keis Ideal."),
 ("APP-LUK-0002", "PRIN-LUK-0002",
  "Kirchgemeinden und einzelne Christen können fragen, wem ihre Botschaft heute zuerst gilt, etwa Menschen im Gefängnis, mit Behinderung oder mit Schulden, und ob sie Menschen ausserhalb der eigenen Gruppe Gottes Zuwendung zutrauen, wie es Jesus mit Elija und Elischa in Erinnerung ruft.",
  "[[LUK.4.18-LUK.4.19]] ist kein ausgearbeitetes Sozialprogramm; der Text gibt keine Anweisung für Gesetze oder Parteien. Die Heilungen Jesu lassen sich nicht als Methode übertragen.",
  "Chilegmeinde und einzelni Christe chönd frage, wem iri Botschaft hüt zerscht gilt, öppe Mänsche im Gfängnis, mit ere Behinderig oder mit Schulde, und öb si Mänsche usserhalb vo de eigete Gruppe d Zuewändig vo Gott zuetroued, wie s de Jesus mit em Elija und em Elischa i Erinnerig rüeft.",
  "[[LUK.4.18-LUK.4.19]] isch keis usgarbeitets Sozialprogramm; de Text git kei Aawiisig für Gsetz oder Parteie. D Heilige vo Jesus lönd sich nöd als Methode übertrage."),
 ("APP-LUK-0003", "PRIN-LUK-0003",
  "Wer vor einer grossen Entscheidung steht, etwa im Beruf, in einer Partnerschaft oder bei einer Aufgabe in der Gemeinde, kann sich wie Jesus vor der Wahl der Zwölf bewusst Zeit zum Beten nehmen und Gott um seinen Geist bitten.",
  "Der Text verspricht nicht, dass Beten jede Entscheidung leicht macht oder jeden Wunsch erfüllt; verheissen ist der Geist ([[LUK.11.13]]). Beten ersetzt Rat und sorgfältiges Prüfen nicht.",
  "Wär vor ere grosse Entscheidig staat, öppe im Bruef, i ere Partnerschaft oder bi ere Ufgaab i de Gmeind, cha sich wie de Jesus vor de Waal vo de Zwölf bewusst Ziit zum Bätte nää und Gott um sin Geischt bitte.",
  "De Text verspricht nöd, dass s Bätte jedi Entscheidig liecht macht oder jede Wunsch erfüllt; verheisse isch de Geischt ([[LUK.11.13]]). S Bätte ersetzt Root und sorgfältigs Prüefe nöd."),
 ("APP-LUK-0004", "PRIN-LUK-0004",
  "Im Umgang mit Menschen, die einen verletzt, gemobbt oder betrogen haben, kann man nach Schritten suchen, die nicht vergelten: für sie beten, nicht schlecht über sie reden, ihnen Hilfe nicht verweigern, wenn sie in Not sind.",
  "Feindesliebe verlangt nicht, Gewalt oder Missbrauch weiter auszuhalten oder Betroffene zum Schweigen zu bringen; Schutz, Grenzen und rechtliche Schritte bleiben möglich. Der Text sagt nichts Unmittelbares über staatliche Gewalt oder Krieg.",
  "Im Umgang mit Mänsche, wo eim verletzt, gmobbt oder betroge händ, cha mer nach Schritt sueche, wo nöd vergälted: für si bätte, nöd schlächt über si rede, ine d Hilf nöd verwehre, wänn si i Not sind.",
  "Feindesliebi verlangt nöd, Gwalt oder Missbruuch wiiter uszhalte oder Betroffeni zum Schwige z bringe; Schutz, Gränze und rächtlichi Schritt bliibed möglich. De Text seit nüüt Diräkts über staatlichi Gwalt oder Chrieg."),
 ("APP-LUK-0005", "PRIN-LUK-0005",
  "Wer in einer Gemeinde Verantwortung trägt, kann darauf achten, wie Menschen mit belasteter Vergangenheit empfangen werden: ob man sie wie Simon nach ihrem Ruf beurteilt oder ihre Dankbarkeit und Liebe wahrnimmt.",
  "Der Text sagt nicht, dass Schuld gleichgültig ist oder dass Menschen Vergebung durch Liebe verdienen. Er ersetzt nicht, Unrecht gegenüber Geschädigten aufzuarbeiten.",
  "Wär i ere Gmeind Verantwortig treit, cha druf achte, wie Mänsche mit ere belaschtete Vergangeheit empfange wärded: öb mer si wie de Simon nach irem Ruef beurteilt oder iri Dankbarkeit und Liebi wahrnimmt.",
  "De Text seit nöd, dass Schuld gliichgültig isch oder dass Mänsche Vergäbig dur Liebi verdiened. Er ersetzt nöd, dass mer Unrächt gägenüber dene, wo gschädiget worde sind, ufarbeitet."),
 ("APP-LUK-0006", "PRIN-LUK-0006",
  "Wer fragt, wem er helfen muss, kann die Frage umkehren: Wem kann ich jetzt zum Nächsten werden, etwa einer Person, die auf dem Arbeitsweg zusammenbricht, oder Menschen aus einer Gruppe, gegen die ich Vorurteile habe?",
  "Das Gleichnis verlangt nicht, jede Not allein zu lösen oder sich selbst in Gefahr zu bringen; der Samaritaner zieht den Wirt bei. Es ist kein Urteil über Priester, Leviten oder das Judentum.",
  "Wär fröget, wem er mues hälfe, cha d Frag umchere: Für wän chan ich jetzt zum Nächschte wärde, öppe für e Person, wo uf em Arbetswäg zämebricht, oder für Mänsche us ere Gruppe, wo ich Vorurteil gäge si ha?",
  "S Gliichnis verlangt nöd, jedi Not elei z löse oder sich sälber i Gfahr z bringe; de Samaritaner zieht de Wirt bii. Es isch keis Urteil über Prieschter, Levite oder s Judetum."),
 ("APP-LUK-0007", "PRIN-LUK-0007",
  "Wer in Familie, Beruf oder Gemeinde viel leistet, kann regelmässig innehalten, um auf Gottes Wort zu hören, etwa beim Bibellesen oder im Gottesdienst, und prüfen, ob die Sorge um vieles das eine Nötige verdrängt.",
  "Der Text wertet Arbeit, Gastfreundschaft und Dienen nicht ab; Marta wird nicht verworfen. Er schreibt keine bestimmte Form der Andacht vor.",
  "Wär i de Familie, im Bruef oder i de Gmeind vil leischtet, cha regelmässig innehalte, zum uf s Wort vo Gott z lose, öppe bim Bibelläse oder im Gottesdienscht, und prüefe, öb d Sorg um vil Sache s Eint verdrängt, wo nötig isch.",
  "De Text wärtet Arbet, Gaschtfründschaft und Diene nöd ab; d Marta wird nöd verworfe. Er schriibt kei bestimmti Form vo de Andacht vor."),
 ("APP-LUK-0008", "PRIN-LUK-0008",
  "Bei Entscheidungen über Geld, Erbe und Vorsorge kann man fragen, ob man auch für andere plant, und einen festen Teil für Bedürftige vorsehen; bei Erbstreitigkeiten kann man fragen, was dem Frieden in der Familie dient.",
  "Der Text verbietet Vorsorge nicht und schreibt keinen bestimmten Betrag vor. Wer selbst kaum genug hat, wird nicht zum Verzicht aufgerufen, sondern zum Vertrauen ermutigt.",
  "Bi Entscheidige über Gäld, Erb und Vorsorg cha mer frage, öb mer au für anderi plant, und en feschte Teil für Bedürftigi vorgseh; bi Striit ums Erb cha mer frage, was em Fride i de Familie dient.",
  "De Text verbüütet Vorsorg nöd und schriibt kein bestimmte Betrag vor. Wär sälber chuum gnueg hät, wird nöd zum Verzicht ufgrüeft, sondern zum Vertroue ermuetiget."),
 ("APP-LUK-0009", "PRIN-LUK-0009",
  "Christen können sich fragen, wo sie im Alltag Jesus nachfolgen, auch wenn es etwas kostet, und wie sie reagieren, wenn andere ihren Glauben ablehnen: ohne Drohung, Spott oder Druck.",
  "Die harten Worte in [[LUK.9.59-LUK.9.62]] sind kein allgemeines Verbot, Angehörige zu bestatten oder sich zu verabschieden; sie zeigen die Dringlichkeit des Reiches Gottes. Der Text rechtfertigt nicht, Familie oder Pflichten leichtfertig zu vernachlässigen.",
  "Christe chönd sich frage, wo si im Alltag em Jesus nachefolged, au wänn s öppis choschtet, und wie si reagiered, wänn anderi ire Glaube ablehned: ohni Drohig, Spott oder Druck.",
  "Di herte Wort i [[LUK.9.59-LUK.9.62]] sind keis allgemeins Verbot, Aaghörigi z beerdige oder sich z verabschiede; si zeiged, wie dringend s Riich vo Gott isch. De Text rächtfertiget nöd, Familie oder Pflichte liechtfertig z vernachlässige."),
]

# (id, Abschnitt, Frage, Stand | Mundart)
QUESTIONS = [
 ("QUESTION-LUK-0001", U(2, 1, 20),
  "Wie verhält sich die Eintragung «als Quirinius Statthalter von Syrien war» ([[LUK.2.2]]) zur Geburt Jesu «in den Tagen des Herodes» ([[LUK.1.5]])?",
  "Nach Josephus wurde Quirinius 6 n. Chr. Statthalter von Syrien und führte in Judäa eine Schätzung durch; Herodes der Grosse starb nach verbreiteter Rechnung 4 v. Chr. Vorgeschlagen werden: ein Irrtum oder eine Vereinfachung des Lukas; eine frühere Tätigkeit des Quirinius im Osten, die nicht sicher belegt ist; das Verständnis des Wortes für «erste» als «früher als» («diese Eintragung geschah vor der unter Quirinius»), grammatisch möglich, aber umstritten; oder eine längere, in Etappen durchgeführte Erfassung. Eine einzige, reichsweite Schätzung unter Augustus ist ausserhalb des Lukasevangeliums nicht belegt. Siehe BG-LUK-0003 und die Übersetzungsentscheidung zu [[LUK.2.2]].",
  "Wie passt d Iitragig, «wo de Quirinius Statthalter vo Syrie gsii isch» ([[LUK.2.2]]), zur Geburt vo Jesus «i de Täg vom Herodes» ([[LUK.1.5]])?",
  "Nach em Josephus isch de Quirinius 6 n. Chr. Statthalter vo Syrie worde und hät z Judäa e Schätzig duregfüert; de Herodes de Gross isch nach verbreiteter Rächnig 4 v. Chr. gstorbe. Vorgschlage wärded: en Irrtum oder e Vereifachig vom Lukas; e früeneri Tätigkeit vom Quirinius im Oschte, wo nöd sicher belegt isch; s Verständnis vom Wort für «erscht» als «früener als» («die Iitragig isch vor dere under em Quirinius gsii»), grammatisch möglich, aber umstritte; oder e längeri Erfassig i Etappe. E einzigi Schätzig fürs ganz Riich under em Augustus isch usserhalb vom Lukasevangelium nöd belegt. Lueg BG-LUK-0003 und d Übersetzigsentscheidig zu [[LUK.2.2]]."),
 ("QUESTION-LUK-0002", U(10, 1, 12),
  "Sendet Jesus siebzig oder zweiundsiebzig aus ([[LUK.10.1]]; [[LUK.10.17]]), und wofür steht die Zahl?",
  "Die Handschriften sind geteilt; der SBLGNT liest mit WH und NA28 «zweiundsiebzig», Tregelles und RP «siebzig» (siehe die Alternativen). Die Völkertafel in [[GEN.10.1-GEN.10.32]] zählt im hebräischen Text 70, in der griechischen Bibel 72 Völker; dann stünde die Zahl für die Sendung an alle Völker. Möglich ist auch ein Anklang an die siebzig Ältesten, die Mose helfen ([[NUM.11.16-NUM.11.17]]; [[NUM.11.24-NUM.11.26]]; mit Eldad und Medad sind es 72). Bruce M. Metzger hielt die Frage in einem eigenen Aufsatz («Seventy or Seventy-Two Disciples?») für nicht sicher entscheidbar.",
  "Schickt de Jesus sibezg oder zweiesibezg uus ([[LUK.10.1]]; [[LUK.10.17]]), und für was staat d Zaal?",
  "D Handschrifte sind teilt; de SBLGNT liist mit WH und NA28 «zweiesibezg», Tregelles und RP «sibezg» (lueg d Alternative). D Völkertafle i [[GEN.10.1-GEN.10.32]] zellt im hebräische Text 70, i de griechische Bible 72 Völker; dänn stüend d Zaal für d Sändig a alli Völker. Möglich isch au en Aaklang a di sibezg Ältischte, wo em Mose hälfed ([[NUM.11.16-NUM.11.17]]; [[NUM.11.24-NUM.11.26]]; mit em Eldad und em Medad sind s 72). De Bruce M. Metzger hät d Frag i me eigete Ufsatz («Seventy or Seventy-Two Disciples?») für nöd sicher entscheidbar ghalte."),
 ("QUESTION-LUK-0003", U(11, 37, 54),
  "Was meint «Gebt als Almosen, was darin ist, und seht, alles ist für euch rein» ([[LUK.11.41]])?",
  "Erwogen werden: Gebt den Inhalt von Becher und Schüssel den Armen, dann ist das Gefäss rein; gebt das Innere, euer Herz, hin; oder eine Fehlübersetzung eines aramäischen Wortes für «reinigen», das ähnlich klang wie «Almosen geben» (vorgeschlagen unter anderen von Julius Wellhausen). Bei Matthäus heisst es: «Reinige zuerst das Innere des Bechers» (Vergleich mit [[MAT.23.26]]). Siehe die Übersetzungsentscheidung zu [[LUK.11.41]].",
  "Was meint «Gänd als Almose, was drin isch, und lueged, alles isch für eu rein» ([[LUK.11.41]])?",
  "Erwoge wärded: Gänd de Inhalt vo Bächer und Schüssle de Arme, dänn isch s Gfäss rein; gänd s Inner, eues Härz, häre; oder e falschi Übersetzig vo me aramäische Wort für «reinige», wo ähnlich tönt hät wie «Almose gää» (vorgschlage under anderem vom Julius Wellhausen). Bim Matthäus heisst s: «Putz zerscht s Inner vom Bächer» (Vergliich mit [[MAT.23.26]]). Lueg d Übersetzigsentscheidig zu [[LUK.11.41]]."),
 ("QUESTION-LUK-0004", U(11, 37, 54),
  "Wer ist «Secharja, der zwischen dem Altar und dem Haus umkam» ([[LUK.11.51]])?",
  "Am nächsten liegt der Priester Secharja, Sohn Jojadas, der im Vorhof des Tempels gesteinigt wurde ([[2CH.24.20-2CH.24.22]]). Da die Chronikbücher in der hebräischen Bibel am Schluss stehen, umfasste «von Abel bis Secharja» dann alle Morde der Schrift vom ersten bis zum letzten Buch; ob diese Reihenfolge der Bücher zur Zeit Jesu schon feststand, ist umstritten. Matthäus nennt ihn «Sohn des Barachias» wie den Propheten Sacharja (Vergleich mit [[MAT.23.35]] und [[ZEC.1.1]]). Siehe BG-MAT-4009.",
  "Wär isch «de Secharja, wo zwüsche em Altar und em Huus umchoo isch» ([[LUK.11.51]])?",
  "Am nööchschte liit de Prieschter Secharja, de Sohn vom Jojada, wo im Vorhof vom Tämpel gsteiniget worde isch ([[2CH.24.20-2CH.24.22]]). Wil d Chronikbüecher i de hebräische Bible am Schluss stönd, würd «vom Abel bis zum Secharja» dänn alli Mord vo de Schrift vom erschte bis zum letschte Buech umfasse; öb die Reiefolg vo de Büecher zur Ziit vo Jesus scho feschtgstande isch, isch umstritte. De Matthäus nännt en «Sohn vom Barachias» wie de Prophet Sacharja (Vergliich mit [[MAT.23.35]] und [[ZEC.1.1]]). Lueg BG-MAT-4009."),
 ("QUESTION-LUK-0005", U(3, 23, 38),
  "Warum unterscheidet sich der Stammbaum bei Lukas so stark von dem bei Matthäus (Vergleich mit [[MAT.1.1-MAT.1.17]])?",
  "Vorgeschlagen werden: Lukas gebe die Linie Marias, Matthäus die Josefs (eine verbreitete Erklärung, die am Text nicht belegt ist, weil Lukas Josef nennt); Schwagerehe, bei der ein Mann rechtlich als Sohn eines anderen gilt (so schon Julius Africanus, überliefert bei Eusebius, Kirchengeschichte 1,7); oder zwei unabhängige Überlieferungen mit verschiedenen Absichten: Matthäus betont die Königslinie über Salomo, Lukas die Herkunft von Adam und Gott. Siehe FIND-LUK-0025 und BG-MAT-1001.",
  "Werum underscheidet sich de Stammbaum bim Lukas so starch vo dem bim Matthäus (Vergliich mit [[MAT.1.1-MAT.1.17]])?",
  "Vorgschlage wärded: De Lukas gäb d Linie vo de Maria, de Matthäus die vom Josef (e verbreiteti Erklärig, wo am Text nöd belegt isch, wil de Lukas de Josef nännt); Schwagerehe, wo en Maa rächtlich als Sohn vo me andere gilt (so scho de Julius Africanus, überliferet bim Eusebius, Chilegschicht 1,7); oder zwei unabhängigi Überliferige mit verschidene Absichte: De Matthäus betont d Königslinie über de Salomo, de Lukas d Härkunft vom Adam und vo Gott. Lueg FIND-LUK-0025 und BG-MAT-1001."),
 ("QUESTION-LUK-0006", U(5, 33, 39),
  "Wie ist der Satz «Niemand, der alten Wein getrunken hat, will jungen; denn er sagt: ‹Der alte ist gut›» ([[LUK.5.39]]) gemeint?",
  "Der Vers hat bei Markus und Matthäus keine Entsprechung (Vergleich mit [[MRK.2.22]] und [[MAT.9.17]]). Er kann ironisch beschreiben, warum viele das Neue Jesu ablehnen: Sie halten am Gewohnten fest. Er kann auch den Wert des Alten anerkennen und so die Bilder vom neuen Flicken und neuen Wein ([[LUK.5.36-LUK.5.38]]) abmildern. Einige Handschriften haben «besser» statt «gut» (siehe Alternative und Übersetzungsentscheidung zu [[LUK.5.39]]).",
  "Wie isch de Satz «Niemert, wo alte Wii trunke hät, wott junge; er seit nämli: ‹De alt isch guet›» ([[LUK.5.39]]) gmeint?",
  "De Värs hät bim Markus und bim Matthäus kei Entsprächig (Vergliich mit [[MRK.2.22]] und [[MAT.9.17]]). Er cha ironisch beschriibe, werum vili s Nöi vo Jesus ablehned: Si haltet am Gwonte fescht. Er cha au de Wärt vom Alte aaerchänne und so d Bilder vom nöie Blätz und vom junge Wii ([[LUK.5.36-LUK.5.38]]) abmildere. Es paar Handschrifte händ «besser» statt «guet» (lueg d Alternative und d Übersetzigsentscheidig zu [[LUK.5.39]])."),
 ("QUESTION-LUK-0007", U(4, 31, 44),
  "Warum verkündet Jesus nach [[LUK.4.44]] «in den Synagogen Judäas», obwohl er in Galiläa wirkt?",
  "Der SBLGNT liest «Judäas», viele Handschriften «Galiläas» (siehe Alternative); «Galiläa» ist die leichtere Lesart und kann eine Angleichung an die Parallele bei Markus sein (Vergleich mit [[MRK.1.39]]). Lukas kann «Judäa» im weiteren Sinn für das ganze jüdische Land gebrauchen (vgl. [[LUK.1.5]]; [[LUK.7.17]]; [[LUK.23.5]]); dann besteht kein Widerspruch.",
  "Werum verchündet de Jesus nach [[LUK.4.44]] «i de Synagoge vo Judäa», obwohl er z Galiläa wirkt?",
  "De SBLGNT liist «Judäa», vili Handschrifte «Galiläa» (lueg d Alternative); «Galiläa» isch di liechter Läsart und cha e Aagliichig a d Parallele bim Markus sii (Vergliich mit [[MRK.1.39]]). De Lukas cha «Judäa» im wiitere Sinn fürs ganz jüdisch Land bruuche (vgl. [[LUK.1.5]]; [[LUK.7.17]]; [[LUK.23.5]]); dänn git s kein Widerspruch."),
]

RELATIONS = [
 ("REL-LUK-0001", U(1, 5, 25), "MAL.4.5-MAL.4.6", "allusion", "high"),
 ("REL-LUK-0002", U(1, 5, 25), "GEN.18.11", "motif", "probable"),
 ("REL-LUK-0003", U(1, 5, 25), "1SA.1.1-1SA.1.20", "motif", "probable"),
 ("REL-LUK-0004", U(1, 26, 38), "2SA.7.12-2SA.7.16", "allusion", "probable"),
 ("REL-LUK-0005", U(1, 26, 38), "ISA.7.14", "allusion", "possible"),
 ("REL-LUK-0006", U(1, 39, 56), "1SA.2.1-1SA.2.10", "motif", "probable"),
 ("REL-LUK-0007", U(1, 57, 80), "ISA.9.2", "allusion", "probable"),
 ("REL-LUK-0008", U(2, 21, 40), "LEV.12.1-LEV.12.8", "background", "high"),
 ("REL-LUK-0009", U(2, 21, 40), "EXO.13.2", "quotation", "high"),
 ("REL-LUK-0010", U(2, 21, 40), "ISA.49.6", "allusion", "probable"),
 ("REL-LUK-0011", U(3, 1, 20), "ISA.40.3-ISA.40.5", "quotation", "high"),
 ("REL-LUK-0012", U(3, 21, 22), "PSA.2.7", "allusion", "probable"),
 ("REL-LUK-0013", U(3, 21, 22), "ISA.42.1", "allusion", "possible"),
 ("REL-LUK-0014", U(3, 23, 38), "MAT.1.1-MAT.1.17", "parallel_text", "high"),
 ("REL-LUK-0015", U(4, 1, 13), "DEU.8.3", "quotation", "high"),
 ("REL-LUK-0016", U(4, 1, 13), "DEU.6.13", "quotation", "high"),
 ("REL-LUK-0017", U(4, 1, 13), "PSA.91.11-PSA.91.12", "quotation", "high"),
 ("REL-LUK-0018", U(4, 1, 13), "DEU.6.16", "quotation", "high"),
 ("REL-LUK-0019", U(4, 14, 30), "ISA.61.1-ISA.61.2", "quotation", "high"),
 ("REL-LUK-0020", U(4, 14, 30), "ISA.58.6", "quotation", "probable"),
 ("REL-LUK-0021", U(4, 14, 30), "1KI.17.8-1KI.17.16", "background", "high"),
 ("REL-LUK-0022", U(4, 14, 30), "2KI.5.1-2KI.5.14", "background", "high"),
 ("REL-LUK-0023", U(5, 1, 11), "MRK.1.16-MRK.1.20", "parallel_passage", "probable"),
 ("REL-LUK-0024", U(5, 1, 11), "JHN.21.1-JHN.21.11", "motif", "possible"),
 ("REL-LUK-0025", U(6, 1, 5), "1SA.21.1-1SA.21.6", "background", "high"),
 ("REL-LUK-0026", U(6, 20, 26), "MAT.5.3-MAT.5.12", "parallel_passage", "high"),
 ("REL-LUK-0027", U(7, 11, 17), "1KI.17.17-1KI.17.24", "allusion", "probable"),
 ("REL-LUK-0028", U(7, 18, 23), "ISA.35.5-ISA.35.6", "allusion", "probable"),
 ("REL-LUK-0029", U(7, 24, 35), "MAL.3.1", "quotation", "high"),
 ("REL-LUK-0030", U(8, 9, 15), "ISA.6.9", "quotation", "probable"),
 ("REL-LUK-0031", U(9, 28, 36), "MRK.9.2-MRK.9.8", "parallel_passage", "high"),
 ("REL-LUK-0032", U(9, 28, 36), "DEU.18.15", "allusion", "probable"),
 ("REL-LUK-0033", U(9, 51, 56), "2KI.1.10-2KI.1.12", "allusion", "high"),
 ("REL-LUK-0034", U(9, 57, 62), "1KI.19.19-1KI.19.21", "allusion", "probable"),
 ("REL-LUK-0035", U(10, 1, 12), "GEN.19.24-GEN.19.25", "background", "probable"),
 ("REL-LUK-0036", U(10, 25, 37), "DEU.6.5", "quotation", "high"),
 ("REL-LUK-0037", U(10, 25, 37), "LEV.19.18", "quotation", "high"),
 ("REL-LUK-0038", U(11, 14, 23), "EXO.8.19", "allusion", "high"),
 ("REL-LUK-0039", U(11, 29, 32), "JON.3.1-JON.3.10", "background", "high"),
 ("REL-LUK-0040", U(11, 29, 32), "1KI.10.1-1KI.10.13", "background", "high"),
 ("REL-LUK-0041", U(11, 37, 54), "GEN.4.8-GEN.4.10", "background", "high"),
 ("REL-LUK-0042", U(11, 37, 54), "2CH.24.20-2CH.24.22", "background", "probable"),
 ("REL-LUK-0043", U(12, 13, 21), "PSA.14.1", "allusion", "possible"),
 ("REL-LUK-0044", U(12, 22, 34), "PSA.147.9", "motif", "possible"),
 ("REL-LUK-0045", U(12, 49, 53), "MIC.7.6", "allusion", "high"),
]

# Hintergrund: (id, Abschnitt, Stelle, Kontext, Konfidenz, Thema, Text, unsicher, Belege, Quellen, Fachwörter | Mundart)
# Antike Quellen sind nur genannt, nicht am Text nachgeschlagen (kein source_check; siehe docs/QUELLENPRUEFUNG.md).
BACKGROUND = [
 ("BG-LUK-0001", U(1, 1, 4), "LUK.1.1-LUK.1.4", READERS, "probable", "Vorreden in antiken Büchern",
  "Griechische und römische Autoren stellten ihren Werken oft eine Vorrede voran, die Vorgänger erwähnt, die eigene Sorgfalt betont und den Empfänger nennt, dem das Buch gewidmet ist. Josephus widmet seine Schrift «Gegen Apion» dem «hochverehrten» Epaphroditus und knüpft im zweiten Buch mit einem kurzen Rückblick an das erste an; ähnlich verbindet [[ACT.1.1]] die Apostelgeschichte mit dem «ersten Buch» an Theophilus. Auch medizinische und technische Fachbücher, etwa die Arzneimittellehre des Dioskurides, beginnen mit solchen Widmungen. Der Empfänger einer Widmung war oft ein angesehener Förderer, der das Werk abschreiben und weitergeben liess.",
  "Ob Lukas sich eher an Geschichtswerke oder an Fachliteratur anlehnt, ist umstritten (INT-LUK-0001). Wer Theophilus war, ist unbekannt; dass er das Werk förderte oder verbreitete, ist eine Vermutung.",
  ["LUK.1.1-LUK.1.4", "ACT.1.1"], ["Josephus, Gegen Apion 1,1; 2,1", "Dioskurides, Arzneimittellehre (De materia medica), Vorrede"],
  [],
  "Vorrede i antike Büecher",
  "Griechischi und römischi Autore händ irne Wärch oft e Vorred vorussgstellt, wo Vorgänger erwäänt, di eige Sorgfalt betont und dä nännt, wo s Buech ihm gwidmet isch. De Josephus widmet sini Schrift «Gäge Apion» em «hochverehrte» Epaphroditus und knüpft im zweite Buech mit eme churze Rückblick as erscht aa; ähnlich verbindet [[ACT.1.1]] d Aposchtelgschicht mit em «erschte Buech» a de Theophilus. Au medizinischi und technischi Fachbüecher, öppe d Arzneimittellehr vom Dioskurides, fanged mit settige Widmige aa. Dä, wo me s Buech gwidmet hät, isch oft en aagsehne Förderer gsii, wo s Wärch hät la abschriibe und wiitergää.",
  "Öb sich de Lukas eher a Gschichtswärch oder a Fachliteratur aalehnt, isch umstritte (INT-LUK-0001). Wär de Theophilus gsii isch, weiss mer nöd; dass er s Wärch gförderet oder verbreitet hät, isch e Vermuetig.",
  []),
 ("BG-LUK-0002", U(1, 5, 25), "LUK.1.5-LUK.1.10", TEMPEL, "probable", "Priesterdienst und Räucheropfer",
  "Die Priester waren in 24 Dienstgruppen eingeteilt, die abwechselnd Dienst im Tempel taten ([[1CH.24.1-1CH.24.19]]); die Gruppe Abija stand an achter Stelle ([[1CH.24.10]]). Innerhalb der Gruppe wurden die Aufgaben durch das Los verteilt ([[LUK.1.9]]). Das Räucheropfer wurde morgens und abends auf dem goldenen Räucheraltar im Heiligtum dargebracht ([[EXO.30.7-EXO.30.8]]), während das Volk draussen betete ([[LUK.1.10]]). Nach der Mischna wurde für das Räucheropfer nur unter Priestern gelost, die es noch nie dargebracht hatten; für einen Priester konnte es daher ein einmaliges Ereignis im Leben sein. Kinderlosigkeit galt als Schmach ([[LUK.1.25]]; vgl. [[GEN.30.23]]; [[1SA.1.6-1SA.1.11]]).",
  "Die Mischna wurde um 200 n. Chr. aufgeschrieben und gibt die Tempelpraxis nicht in jedem Fall genau wieder. Wie viele Priester eine Dienstgruppe umfasste und wie lange ein Dienst dauerte, ist nicht sicher bekannt.",
  ["LUK.1.5-LUK.1.10", "LUK.1.23", "1CH.24.1-1CH.24.19", "EXO.30.7-EXO.30.8", "LUK.1.25"], ["Mischna, Tamid 5,2"],
  [],
  "Prieschterdienscht und Rauchopfer",
  "D Prieschter sind i 24 Dienschtgruppe iiteilt gsii, wo abwächsligswiis im Tämpel Dienscht gmacht händ ([[1CH.24.1-1CH.24.19]]); d Gruppe Abija isch a achter Stell gsii ([[1CH.24.10]]). Innerhalb vo de Gruppe sind d Ufgaabe dur s Los verteilt worde ([[LUK.1.9]]). S Rauchopfer isch am Morge und am Aabig uf em goldige Rauchaltar im Heiligtum dargebracht worde ([[EXO.30.7-EXO.30.8]]), wäred s Volk dusse bättet hät ([[LUK.1.10]]). Nach de Mischna hät me s Los fürs Rauchopfer nu under Prieschter zoge, wo s no nie dargebracht händ; für en Prieschter hät s drum es einmaligs Ereignis im Läbe chöne sii. Kei Chind z haa, hät als Schand gulte ([[LUK.1.25]]; vgl. [[GEN.30.23]]; [[1SA.1.6-1SA.1.11]]).",
  "D Mischna isch um 200 n. Chr. ufgschribe worde und git d Praxis im Tämpel nöd i jedem Fall gnau wider. Wie vil Prieschter e Dienschtgruppe umfasst hät und wie lang en Dienscht duuret hät, weiss mer nöd sicher.",
  []),
 ("BG-LUK-0003", U(2, 1, 20), "LUK.2.1-LUK.2.5", TEMPEL, "possible", "Augustus, Quirinius und die Eintragung",
  "Augustus war von 27 v. Chr. bis 14 n. Chr. Kaiser. Er liess die römischen Bürger mehrmals zählen und in den Provinzen Land und Bevölkerung für die Steuer erfassen; in Ägypten sind solche Eintragungen in regelmässigen Abständen durch erhaltene Papyri belegt. Josephus berichtet, dass Publius Sulpicius Quirinius nach der Absetzung des Archelaus (6 n. Chr.) als Statthalter Syriens Judäa schätzen liess und dass dagegen ein Aufstand unter Judas aus Galiläa entstand (vgl. [[ACT.5.37]]). Dass jeder in die Stadt seiner Vorfahren gehen musste ([[LUK.2.3]]), ist sonst nicht belegt; ein Erlass des Präfekten von Ägypten aus dem Jahr 104 n. Chr. ordnet jedoch an, dass Leute, die sich auswärts aufhielten, für die Eintragung an ihren Wohnort zurückkehren.",
  "Wie die Eintragung unter Quirinius mit der Geburt Jesu unter Herodes dem Grossen zusammenpasst, ist ungelöst (QUESTION-LUK-0001). Eine einzige, reichsweite Schätzung unter Augustus ist ausserhalb des Lukasevangeliums nicht belegt. Ob der ägyptische Erlass mit der Herkunftsstadt oder nur mit dem Wohnort rechnet, ist für den Vergleich wichtig und wird verschieden beurteilt.",
  ["LUK.2.1-LUK.2.5", "ACT.5.37"],
  ["Josephus, Jüdische Altertümer 17,355; 18,1–4; 18,26", "Augustus, Tatenbericht (Res gestae) 8",
   "Erlass des Präfekten Gaius Vibius Maximus (Papyrus London 904, 104 n. Chr.)"],
  [],
  "Augustus, Quirinius und d Iitragig",
  "De Augustus isch vo 27 v. Chr. bis 14 n. Chr. Kaiser gsii. Er hät d römische Bürger meermaals la zelle und i de Provinze Land und Bevölkerig für d Stüür la erfasse; z Ägypte sind settigi Iitragige i regelmässige Abständ dur erhalteni Papyri belegt. De Josephus brichtet, dass de Publius Sulpicius Quirinius nach de Absetzig vom Archelaus (6 n. Chr.) als Statthalter vo Syrie Judäa hät la schätze und dass dergäge en Ufstand under em Judas us Galiläa uufchoo isch (vgl. [[ACT.5.37]]). Dass jede i d Stadt vo sine Vorfahre hät müese gaa ([[LUK.2.3]]), isch süscht nöd belegt; en Erlass vom Präfekt vo Ägypte us em Jahr 104 n. Chr. ordnet aber aa, dass Lüüt, wo sich uswärts ufghalte händ, für d Iitragig a iren Wonort zruggchered.",
  "Wie d Iitragig under em Quirinius zur Geburt vo Jesus under em Herodes em Grosse passt, isch unglöst (QUESTION-LUK-0001). E einzigi Schätzig fürs ganz Riich under em Augustus isch usserhalb vom Lukasevangelium nöd belegt. Öb de ägyptisch Erlass mit de Härkunftsstadt oder nu mit em Wonort rächnet, isch für de Vergliich wichtig und wird verschide beurteilt.",
  []),
 ("BG-LUK-0004", U(2, 1, 20), "LUK.2.7", TEMPEL, "possible", "Futterkrippe und «Unterkunft»",
  "Einfache Häuser in Judäa hatten oft einen Wohnraum, in dem die Familie auf einer erhöhten Fläche lebte, während Tiere nachts im tieferen Teil standen; Futtertröge konnten in den Boden oder in Stein eingelassen sein. Manche Häuser waren an Höhlen gebaut, die als Stall dienten. Das Wort κατάλυμα, hier mit «Unterkunft» übersetzt, bezeichnet bei Lukas auch den Gästeraum eines Hauses ([[LUK.22.11]]); für eine Herberge mit Wirt gebraucht er ein anderes Wort (πανδοχεῖον, [[LUK.10.34]]). Dann wäre gemeint: Im Gästeraum war kein Platz, und das Kind wurde in eine Futterkrippe im Wohnbereich gelegt. Schon im 2. Jahrhundert wird erzählt, Jesus sei in einer Höhle bei Betlehem geboren.",
  "Wie Häuser in Betlehem zur Zeitenwende gebaut waren, ist nur aus Vergleichsfunden erschlossen. Die Höhlenüberlieferung ist alt, aber nicht aus der Zeit Jesu. «Herberge» ist die vertraute Wiedergabe (siehe die Übersetzungsentscheidung zu [[LUK.2.7]]).",
  ["LUK.2.7", "LUK.2.12", "LUK.2.16", "LUK.22.11", "LUK.10.34"], ["Justin, Dialog mit Tryphon 78", "Protevangelium des Jakobus 18"],
  [("grc", "κατάλυμα", "Unterkunft; Gästeraum"), ("grc", "πανδοχεῖον", "Herberge, Gasthaus"), ("grc", "φάτνη", "Futterkrippe")],
  "Fuetterchrippe und «Underkunft»",
  "Eifachi Hüüser z Judäa händ oft en Wonruum gha, wo d Familie uf ere erhöchte Flächi gläbt hät, wäred d Tier znacht im tüüfere Teil gstande sind; Fuettertrög händ chöne i Bode oder i Stei iigloo sii. Mängi Hüüser sind a Höhline baut gsii, wo als Stall dienet händ. S Wort κατάλυμα, da mit «Underkunft» übersetzt, bezeichnet bim Lukas au de Gäschteruum vo me Huus ([[LUK.22.11]]); für e Herbärg mit eme Wirt bruucht er es anders Wort (πανδοχεῖον, [[LUK.10.34]]). Dänn wär gmeint: Im Gäschteruum isch kei Platz gsii, und s Chind isch in e Fuetterchrippe im Wonbereich gleit worde. Scho im 2. Jahrhundert verzellt me, de Jesus sig in ere Höhli bi Betlehem gebore.",
  "Wie d Hüüser z Betlehem um d Ziitewändi baut gsii sind, weiss mer nu us Vergliichsfund. D Höhli-Überliferig isch alt, aber nöd us de Ziit vo Jesus. «Herbärg» isch di vertrout Widergaab (lueg d Übersetzigsentscheidig zu [[LUK.2.7]]).",
  ["Underkunft; Gäschteruum", "Herbärg, Gaschthuus", "Fuetterchrippe"]),
 ("BG-LUK-0005", U(2, 1, 20), "LUK.2.8-LUK.2.20", TEMPEL, "possible", "Hirten bei Betlehem",
  "Um Betlehem, am Rand der Wüste Juda, wurden Schafe und Ziegen gehalten; David war dort Hirte gewesen ([[1SA.16.11]]; [[1SA.17.15]]). Hirten blieben mit der Herde draussen und wachten nachts abwechselnd ([[LUK.2.8]]). Die Arbeit war hart und wenig angesehen; ein Spruch in der Mischna zählt den Hirten zu den Berufen, die ein Vater seinen Sohn nicht lehren soll, weil ihr Handwerk «das von Räubern» sei. In der Schrift ist der Hirte zugleich ein Bild für Gott und für den erwarteten König aus Davids Haus ([[PSA.23.1]]; [[EZK.34.23]]; [[MIC.5.2-MIC.5.4]]).",
  "Ob die abschätzigen Urteile späterer Quellen schon zur Zeit Jesu galten, ist umstritten (dafür etwa Joachim Jeremias, Jerusalem zur Zeit Jesu; dagegen andere, die auf das positive Hirtenbild der Schrift verweisen). Aus dem Aufenthalt im Freien lässt sich die Jahreszeit der Geburt nicht sicher bestimmen.",
  ["LUK.2.8-LUK.2.20", "1SA.16.11", "PSA.23.1", "EZK.34.23", "MIC.5.2-MIC.5.4"], ["Mischna, Kidduschin 4,14"],
  [],
  "Hirte bi Betlehem",
  "Um Betlehem ume, am Rand vo de Wüeschti Juda, hät me Schaf und Geisse ghalte; de David isch dört Hirt gsii ([[1SA.16.11]]; [[1SA.17.15]]). D Hirte sind mit de Herde dusse blibe und händ znacht abwächsligswiis Wach ghalte ([[LUK.2.8]]). D Arbet isch hert und weni aagsee gsii; en Spruch i de Mischna zellt de Hirt zu de Brüef, wo en Vatter sim Sohn nöd söll lehre, wil ires Handwärch «das vo Röiber» sig. I de Schrift isch de Hirt zuglich es Bild für Gott und für de König us em Huus vom David, wo me erwartet hät ([[PSA.23.1]]; [[EZK.34.23]]; [[MIC.5.2-MIC.5.4]]).",
  "Öb di abschätzige Urteil vo spöötere Quelle scho zur Ziit vo Jesus gulte händ, isch umstritte (defür öppe de Joachim Jeremias, Jerusalem zur Zeit Jesu; dergäge anderi, wo uf s positiv Hirtebild vo de Schrift verwiised). Us em Ufenthalt dusse cha mer d Jahresziit vo de Geburt nöd sicher bestimme.",
  []),
 ("BG-LUK-0006", U(2, 21, 40), "LUK.2.22-LUK.2.24", TEMPEL, "high", "Reinigung der Mutter und Auslösung des Erstgeborenen",
  "Nach [[LEV.12.1-LEV.12.8]] galt eine Mutter nach der Geburt eines Sohnes 40 Tage als unrein; danach brachte sie ein Lamm als Brandopfer und eine Taube als Sündopfer, oder, wenn sie sich kein Lamm leisten konnte, zwei Turteltauben oder zwei junge Tauben. Lukas nennt dieses Opfer der Armen ([[LUK.2.24]]). Jeder erstgeborene Sohn gehörte Gott ([[EXO.13.2]]; [[EXO.13.12-EXO.13.15]]) und wurde mit fünf Schekeln ausgelöst ([[NUM.18.15-NUM.18.16]]); dazu musste das Kind nicht in den Tempel gebracht werden. Dass Lukas Jesus «dem Herrn darbringen» lässt ([[LUK.2.22]]), erinnert an Samuel, den Hanna Gott weihte ([[1SA.1.22-1SA.1.28]]).",
  "Ob Lukas an die Auslösung denkt oder an eine Darbringung ohne Auslösung, sagt er nicht; ein Geldbetrag wird nicht erwähnt. Dass er von «ihrer Reinigung» spricht, obwohl das Gesetz nur die Mutter nennt, wird verschieden erklärt (siehe die Übersetzungsentscheidung zu [[LUK.2.22]]).",
  ["LUK.2.22-LUK.2.24", "LEV.12.1-LEV.12.8", "EXO.13.2", "NUM.18.15-NUM.18.16", "1SA.1.22-1SA.1.28"], [],
  [],
  "Reinigung vo de Mueter und Uslösig vom Erschtgeborne",
  "Nach [[LEV.12.1-LEV.12.8]] hät e Mueter nach de Geburt vo me Sohn 40 Täg als unrein gulte; dänn hät si es Lamm als Brandopfer und e Tuube als Sündopfer bracht, oder, wänn si sich kei Lamm hät chöne leischte, zwei Turteltuube oder zwei jungi Tuube. De Lukas nännt das Opfer vo de Arme ([[LUK.2.24]]). Jede erschtgeborni Sohn hät Gott ghört ([[EXO.13.2]]; [[EXO.13.12-EXO.13.15]]) und isch mit föif Schekel usglöst worde ([[NUM.18.15-NUM.18.16]]); defür hät me s Chind nöd müese in Tämpel bringe. Dass de Lukas de Jesus «em Herr bringe» laat ([[LUK.2.22]]), erinneret a de Samuel, wo d Hanna Gott gweiht hät ([[1SA.1.22-1SA.1.28]]).",
  "Öb de Lukas a d Uslösig dänkt oder a s Bringe ohni Uslösig, seit er nöd; en Gäldbetrag wird nöd erwäänt. Dass er vo «irer Reinigung» redt, obwohl s Gsetz nu d Mueter nännt, wird verschide erklärt (lueg d Übersetzigsentscheidig zu [[LUK.2.22]]).",
  []),
 ("BG-LUK-0007", U(2, 21, 40), "LUK.2.25-LUK.2.38", TEMPEL, "probable", "Warten auf den «Trost Israels»",
  "Viele Juden erwarteten im 1. Jahrhundert, dass Gott sein Volk von Fremdherrschaft befreien und Jerusalem wiederherstellen werde. Die Wendungen «Trost Israels» und «Erlösung Jerusalems» ([[LUK.2.25]]; [[LUK.2.38]]) nehmen Jesaja auf ([[ISA.40.1-ISA.40.2]]; [[ISA.52.9]]). Die Psalmen Salomos, im 1. Jahrhundert v. Chr. entstanden, bitten um einen König aus Davids Haus, der Jerusalem reinigen und die Völker richten soll, und nennen ihn den Gesalbten; von dem «Gesalbten des Herrn» spricht auch Simeon ([[LUK.2.26]]). Hanna, eine betagte Witwe aus dem Stamm Ascher ([[LUK.2.36-LUK.2.37]]), gehört zu den wenigen Frauen, die die Bibel ausdrücklich Prophetin nennt (vgl. [[EXO.15.20]]; [[JDG.4.4]]; [[2KI.22.14]]).",
  "Wie verbreitet und wie einheitlich diese Erwartungen waren, ist umstritten; es gab sehr verschiedene Hoffnungen. Die Zahl «vierundachtzig» kann Hannas Alter oder die Dauer ihrer Witwenschaft meinen.",
  ["LUK.2.25-LUK.2.38", "ISA.40.1-ISA.40.2", "ISA.52.9"], ["Psalmen Salomos 17–18"],
  [],
  "Warte uf de «Troscht vo Israel»",
  "Vili Jude händ im 1. Jahrhundert erwartet, dass Gott sis Volk vo de Frömdherrschaft befreit und Jerusalem wider ufrichtet. D Wändige «Troscht vo Israel» und «Erlösig vo Jerusalem» ([[LUK.2.25]]; [[LUK.2.38]]) nämed de Jesaja uf ([[ISA.40.1-ISA.40.2]]; [[ISA.52.9]]). D Psalme vom Salomo, im 1. Jahrhundert v. Chr. entstande, bitted um en König us em Huus vom David, wo Jerusalem söll reinige und d Völker richte, und nänned en de Gsalbt; vom «Gsalbte vom Herr» redt au de Simeon ([[LUK.2.26]]). D Hanna, e alti Witwe us em Stamm Ascher ([[LUK.2.36-LUK.2.37]]), ghört zu de wenige Fraue, wo d Bible usdrücklich Prophetin nännt (vgl. [[EXO.15.20]]; [[JDG.4.4]]; [[2KI.22.14]]).",
  "Wie verbreitet und wie eiheitlich die Erwartige gsii sind, isch umstritte; es hät ganz verschideni Hoffnige ggää. D Zaal «vierenachtzg» cha s Alter vo de Hanna oder d Duur vo irer Witweziit meine.",
  []),
 ("BG-LUK-0008", U(2, 41, 52), "LUK.2.41-LUK.2.47", TEMPEL, "probable", "Wallfahrt zum Passafest und ein Zwölfjähriger",
  "Nach dem Gesetz sollten die Männer Israels dreimal im Jahr vor Gott erscheinen, darunter zum Passa ([[EXO.23.14-EXO.23.17]]; [[DEU.16.16]]); viele Familien aus Galiläa zogen jedes Jahr nach Jerusalem, eine Reise von mehreren Tagen. Man reiste in Gruppen von Verwandten und Nachbarn, auch zum Schutz; so konnte ein Kind einen Tag lang unbemerkt fehlen ([[LUK.2.44]]). Nach der Mischna ist ein Junge mit dreizehn Jahren zu den Geboten verpflichtet; mit zwölf war man nahe an dieser Grenze. Josephus erzählt von sich selbst, mit etwa vierzehn Jahren hätten ihn Hohepriester und Vornehme wegen seines Verständnisses der Gesetze befragt; Erzählungen über das frühe Verständnis bedeutender Männer waren in der Antike verbreitet.",
  "Ob es zur Zeit Jesu schon eine feste Feier zur religiösen Mündigkeit gab (später Bar Mizwa), ist nicht belegt. Wo im Tempelbezirk Lehrer sassen, ist nicht bekannt.",
  ["LUK.2.41-LUK.2.47", "EXO.23.14-EXO.23.17", "DEU.16.16"], ["Mischna, Avot 5,21", "Josephus, Leben (Vita) 9"],
  [],
  "Wallfahrt as Passafäscht und en Zwölfjärige",
  "Nach em Gsetz händ d Manne vo Israel drüü Mal im Jahr vor Gott söle erschiine, dorunder as Passa ([[EXO.23.14-EXO.23.17]]; [[DEU.16.16]]); vili Familie us Galiläa sind jedes Jahr uf Jerusalem gange, e Reis vo meerere Täg. Mer isch i Gruppe vo Verwandte und Nachbere greist, au zum Schutz; so hät es Chind en Tag lang chöne fääle, ohni dass s öpper gmerkt hät ([[LUK.2.44]]). Nach de Mischna isch en Bueb mit drizäh Jahr zu de Gebot verpflichtet; mit zwölf isch mer nöch a dere Gränze gsii. De Josephus verzellt vo sich sälber, mit öppe vierzäh Jahr hebed en Hoheprieschter und Vornähmi wäge sim Verständnis vo de Gsetz befröget; Gschichte über s früe Verständnis vo bedüütende Manne sind i de Antike verbreitet gsii.",
  "Öb s zur Ziit vo Jesus scho e fescht Fiir zur religiöse Mündigkeit ggää hät (spööter Bar Mizwa), isch nöd belegt. Wo im Tämpelbezirk Lehrer gsässe sind, weiss mer nöd.",
  []),
 ("BG-LUK-0009", U(3, 1, 20), "LUK.3.1-LUK.3.2", GAL, "probable", "Die Herrscher im fünfzehnten Jahr des Tiberius",
  "Tiberius wurde 14 n. Chr. Nachfolger des Augustus. Sein fünfzehntes Jahr fällt je nach Zählung (ab dem Tod des Augustus oder ab einer früheren Mitregentschaft, nach römischem oder syrischem Kalender) auf etwa 27 bis 29 n. Chr. Pontius Pilatus war Statthalter von Judäa von etwa 26 bis 36 n. Chr. Zwei Söhne Herodes' des Grossen regierten als Tetrarchen: Herodes Antipas über Galiläa und Peräa (4 v. Chr. bis 39 n. Chr.), Philippus über die Gebiete nordöstlich des Sees (4 v. Chr. bis 34 n. Chr.). Abilene lag nordwestlich von Damaskus. Kajaphas war von etwa 18 bis 36 n. Chr. Hohepriester; sein Schwiegervater Hannas war es von 6 bis 15 n. Chr. gewesen und blieb einflussreich (vgl. BG-JHN-3004).",
  "Josephus kennt einen Lysanias, der um 36 v. Chr. getötet wurde; ob es später einen Tetrarchen gleichen Namens gab, wie eine Weihinschrift aus Abila nahelegt, oder ob Lukas sich irrt, ist umstritten. Die genauen Amtsjahre sind teils erschlossen. Dass Lukas zwei Hohepriester nennt, obwohl das Wort in der Einzahl steht, spiegelt wohl den Einfluss des Hannas.",
  ["LUK.3.1-LUK.3.2", "JHN.18.13", "ACT.4.6"], ["Josephus, Jüdische Altertümer 15,92; 18,26–35; 18,95", "Weihinschrift aus Abila (Lysanias als Tetrarch)"],
  [],
  "D Herrscher im füfzähte Jahr vom Tiberius",
  "De Tiberius isch 14 n. Chr. Nachfolger vom Augustus worde. Sis füfzäht Jahr fallt je nach Zellig (ab em Tod vom Augustus oder ab ere früenere Mitregentschaft, nach em römische oder em syrische Kaländer) uf öppe 27 bis 29 n. Chr. De Pontius Pilatus isch vo öppe 26 bis 36 n. Chr. Statthalter vo Judäa gsii. Zwee Söhn vom Herodes em Grosse händ als Tetrarche regiert: de Herodes Antipas über Galiläa und Peräa (4 v. Chr. bis 39 n. Chr.), de Philippus über d Gebiet nordöschtlich vom See (4 v. Chr. bis 34 n. Chr.). Abilene isch nordweschtlich vo Damaskus gläge. De Kajaphas isch vo öppe 18 bis 36 n. Chr. Hoheprieschter gsii; sin Schwigervatter Hannas isch es vo 6 bis 15 n. Chr. gsii und isch iiflussriich blibe (vgl. BG-JHN-3004).",
  "De Josephus kännt en Lysanias, wo um 36 v. Chr. umbracht worde isch; öb s spööter en Tetrarch mit em gliiche Name ggää hät, wie s e Weihinschrift us Abila nahelegt, oder öb sich de Lukas irrt, isch umstritte. Di gnaue Amtsjahr sind zum Teil erschlosse. Dass de Lukas zwee Hoheprieschter nännt, obwohl s Wort i de Einzaal staat, spieglet wohl de Iifluss vom Hannas.",
  []),
 ("BG-LUK-0010", U(4, 14, 30), "LUK.4.16-LUK.4.21", GAL, "probable", "Lesung aus den Propheten und das Erlassjahr",
  "Im Synagogengottesdienst wurde am Sabbat aus der Tora und danach aus den Propheten gelesen; anschliessend konnte ein Kundiger auslegen (vgl. [[ACT.13.15]]). Man stand zum Lesen auf und setzte sich zum Lehren ([[LUK.4.16]]; [[LUK.4.20]]). Die Schriften waren Buchrollen; eine vollständige Jesajarolle aus der Zeit vor Christus wurde bei Qumran gefunden. Die Rolle nahm ein Gehilfe (ὑπηρέτης, [[LUK.4.20]]) wieder entgegen, ein Synagogendiener. Das «Gnadenjahr» erinnert an das Erlassjahr: Alle 50 Jahre sollte «Freilassung» (hebräisch דְּרוֹר, griechisch ἄφεσις) ausgerufen werden; Land fiel an die Familien zurück, und verschuldete Israeliten wurden frei ([[LEV.25.8-LEV.25.17]]; [[LEV.25.39-LEV.25.41]]). Ein Text aus Qumran (11QMelchisedek) verbindet [[ISA.61.1-ISA.61.2]] mit dem Erlassjahr und mit einem endzeitlichen Befreier.",
  "Ob die Prophetenlesung zur Zeit Jesu schon fest geordnet war oder frei gewählt werden konnte, ist unbekannt; [[LUK.4.17]] lässt beides zu («fand er die Stelle»). Ob das Erlassjahr je regelmässig gehalten wurde, ist fraglich.",
  ["LUK.4.16-LUK.4.21", "ACT.13.15", "LEV.25.8-LEV.25.17", "ISA.61.1-ISA.61.2"], ["Grosse Jesajarolle aus Qumran (1QIsaᵃ)", "11QMelchisedek (11Q13)"],
  [("grc", "ὑπηρέτης", "Gehilfe, Diener; Synagogendiener"), ("heb", "דְּרוֹר", "Freilassung (im Erlassjahr)", "dᵉror"),
   ("grc", "ἄφεσις", "Freilassung; Erlass, Vergebung")],
  "Läsig us de Prophete und s Erlassjahr",
  "Im Gottesdienscht i de Synagoge hät me am Sabbat us de Tora und dänn us de Prophete vorgläse; nachher hät öpper, wo sich uskännt hät, chöne uslegge (vgl. [[ACT.13.15]]). Zum Vorläse isch mer ufgstande, zum Lehre hät mer sich gsetzt ([[LUK.4.16]]; [[LUK.4.20]]). D Schrifte sind Buechrolle gsii; e vollständigi Jesajarolle us de Ziit vor Christus hät me bi Qumran gfunde. D Rolle hät en Gehilf (ὑπηρέτης, [[LUK.4.20]]) wider entgägegnoo, en Synagogediener. S «Gnadejahr» erinneret as Erlassjahr: All 50 Jahr hät me söle «Freilassig» (hebräisch דְּרוֹר, griechisch ἄφεσις) usrüefe; Land isch a d Familie zruggfalle, und Israelite mit Schulde sind frei worde ([[LEV.25.8-LEV.25.17]]; [[LEV.25.39-LEV.25.41]]). En Text us Qumran (11QMelchisedek) verbindet [[ISA.61.1-ISA.61.2]] mit em Erlassjahr und mit eme Befreier am Änd vo de Ziit.",
  "Öb d Läsig us de Prophete zur Ziit vo Jesus scho fescht gordnet gsii isch oder frei gwählt worde isch, weiss mer nöd; [[LUK.4.17]] laat beides zue («hät er d Stell gfunde»). Öb s Erlassjahr je regelmässig ghalte worde isch, isch fraglich.",
  ["Gehilf, Diener; Synagogediener", "Freilassig (im Erlassjahr)", "Freilassig; Erlass, Vergäbig"]),
 ("BG-LUK-0011", U(7, 1, 10), "LUK.7.2-LUK.7.7", GAL, "possible", "Ein Hauptmann als Wohltäter",
  "Ein Hauptmann (ἑκατοντάρχης) befehligte rund hundert Soldaten. In Kafarnaum, im Gebiet des Herodes Antipas, diente er wohl in dessen Truppen, die nach römischem Muster organisiert waren und auch Nichtjuden umfassten (vgl. BG-MAT-2001). In der antiken Welt stifteten reiche Leute öffentliche Bauten und wurden dafür geehrt; Inschriften belegen auch nichtjüdische Stifter von Synagogen, etwa Julia Severa in Akmonia (Kleinasien, 1. Jahrhundert). Dass jüdische Älteste sich bei Jesus für ihn einsetzen ([[LUK.7.3-LUK.7.5]]), entspricht dem Verhältnis von Gönner und Begünstigten: Wer gestiftet hatte, durfte auf Fürsprache zählen. Der Hauptmann schickt erst Älteste, dann Freunde und kommt nicht selbst, vielleicht auch, um Jesus nicht in das Haus eines Nichtjuden zu bitten ([[LUK.7.6-LUK.7.7]]; vgl. [[ACT.10.28]]).",
  "Dass der Hauptmann Nichtjude war, sagt Lukas nur indirekt ([[LUK.7.9]]: «nicht einmal in Israel»). Eine Synagoge in Kafarnaum aus dem 1. Jahrhundert ist archäologisch nicht sicher nachgewiesen (vgl. BG-MRK-1003). Ob Rücksicht auf Reinheit der Grund für die Boten ist, sagt der Text nicht; er nennt die eigene Unwürdigkeit ([[LUK.7.6-LUK.7.7]]).",
  ["LUK.7.2-LUK.7.10", "ACT.10.28"], ["Inschrift der Julia Severa aus Akmonia (1. Jahrhundert n. Chr.)"],
  [("grc", "ἑκατοντάρχης", "Hauptmann, Befehlshaber über hundert")],
  "En Hauptmaa als Wohltäter",
  "En Hauptmaa (ἑκατοντάρχης) hät öppe hundert Soldate befole. Z Kafarnaum, im Gebiet vom Herodes Antipas, hät er wohl i dem sine Truppe dienet, wo nach römischem Muschter organisiert gsii sind und au Nöd-Jude umfasst händ (vgl. BG-MAT-2001). I de antike Wält händ riichi Lüüt öffentlichi Baute gstiftet und sind defür gehrt worde; Inschrifte beleged au nöd-jüdischi Stifter vo Synagoge, öppe d Julia Severa z Akmonia (Chliiasie, 1. Jahrhundert). Dass sich jüdischi Ältischti bim Jesus für ihn iisetzed ([[LUK.7.3-LUK.7.5]]), entspricht em Verhältnis vo Gönner und Begünschtigte: Wär öppis gstiftet hät, hät uf Fürsprach dörfe zelle. De Hauptmaa schickt zerscht Ältischti, dänn Fründe und chunnt nöd sälber, villicht au, zum de Jesus nöd is Huus vo me Nöd-Jud z bitte ([[LUK.7.6-LUK.7.7]]; vgl. [[ACT.10.28]]).",
  "Dass de Hauptmaa kei Jud gsii isch, seit de Lukas nu indiräkt ([[LUK.7.9]]: «nöd emal in Israel»). E Synagoge z Kafarnaum us em 1. Jahrhundert isch archäologisch nöd sicher nachgwise (vgl. BG-MRK-1003). Öb Rücksicht uf d Reinheit de Grund für d Bote isch, seit de Text nöd; er nännt di eige Unwürdigkeit ([[LUK.7.6-LUK.7.7]]).",
  ["Hauptmaa, Befählshaber über hundert"]),
 ("BG-LUK-0012", U(7, 11, 17), "LUK.7.11-LUK.7.15", GAL, "probable", "Bestattung in Nain und eine Witwe ohne Sohn",
  "Nain lag im Süden Galiläas am Nordhang des Hügels More, etwa zehn Kilometer südöstlich von Nazaret; heute heisst das Dorf Nein. Tote wurden am Todestag ausserhalb der Siedlung bestattet; man trug sie auf einer offenen Bahre (σορός), begleitet von Angehörigen, Klagefrauen und Flötenspielern (vgl. BG-MAT-2006). Nach der Mischna soll selbst der Ärmste für die Bestattung seiner Frau mindestens zwei Flöten und eine Klagefrau stellen. Eine Witwe, die ihren einzigen Sohn verlor, war meist ohne Versorgung und ohne Beistand vor Gericht; die Schrift nennt Witwen und Waisen immer wieder als Schutzbedürftige ([[DEU.10.18]]; [[DEU.24.17]]). Wer einen Toten berührte, wurde nach dem Gesetz unrein ([[NUM.19.11-NUM.19.16]]).",
  "Die Lage von Nain ist durch die Überlieferung des Ortsnamens wahrscheinlich, aber nicht durch Funde aus dem 1. Jahrhundert gesichert. Ob die Regel der Mischna schon zur Zeit Jesu galt, ist offen. Ob das Berühren der Bahre ([[LUK.7.14]]) als Verunreinigung gemeint ist, sagt der Text nicht.",
  ["LUK.7.11-LUK.7.15", "DEU.10.18", "NUM.19.11-NUM.19.16"], ["Mischna, Ketubbot 4,4"],
  [("grc", "σορός", "Totenbahre; Sarg")],
  "Beerdigung z Nain und e Witwe ohni Sohn",
  "Nain isch im Süde vo Galiläa am Nordhang vom Hügel More gläge, öppe zää Kilometer südöschtlich vo Nazaret; hüt heisst s Dorf Nein. Toti sind am Tag, wo si gstorbe sind, usserhalb vo de Siedlig beerdiget worde; mer hät si uf ere offne Bahre (σορός) treit, begleitet vo Aaghörige, Klaagfraue und Flötespiler (vgl. BG-MAT-2006). Nach de Mischna söll sogar de Ärmscht für d Beerdigung vo sinere Frau mindeschtens zwei Flöte und e Klaagfrau stelle. E Witwe, wo iren einzige Sohn verlore hät, isch meischtens ohni Versorgig und ohni Biistand vor Gricht gsii; d Schrift nännt Witwe und Waise immer wider als Mänsche, wo Schutz bruuched ([[DEU.10.18]]; [[DEU.24.17]]). Wär en Tote aagrüert hät, isch nach em Gsetz unrein worde ([[NUM.19.11-NUM.19.16]]).",
  "D Laag vo Nain isch dur d Überliferig vom Ortsname wahrschiinlich, aber nöd dur Fund us em 1. Jahrhundert gsicheret. Öb d Regle vo de Mischna scho zur Ziit vo Jesus gulte hät, isch offe. Öb s Aarüere vo de Bahre ([[LUK.7.14]]) als Verunreinigung gmeint isch, seit de Text nöd.",
  ["Totebahre; Sarg"]),
 ("BG-LUK-0013", U(7, 36, 50), "LUK.7.36-LUK.7.46", GAL, "probable", "Gast beim Mahl: Wasser, Kuss und Öl",
  "Bei einem festlichen Mahl lagen die Gäste auf Polstern, auf den linken Arm gestützt, die Füsse vom Tisch weg (vgl. BG-JHN-2012); so konnte die Frau «von hinten» an die Füsse Jesu herantreten ([[LUK.7.38]]). Solche Mahlzeiten waren oft halböffentlich; Ungeladene konnten zusehen. Zur Gastfreundschaft gehörten Wasser für die staubigen Füsse ([[GEN.18.4]]; [[JDG.19.21]]), ein Begrüssungskuss und Öl für den Kopf (vgl. [[PSA.23.5]]). Ein Denar war der übliche Tageslohn eines Arbeiters (Vergleich mit [[MAT.20.2]]); 500 Denare entsprachen also dem Lohn von mehr als einem Jahr Arbeit, 50 Denare dem von knapp zwei Monaten.",
  "Ob Simons Unterlassungen als Kränkung gemeint sind, wird verschieden beurteilt; Pflicht waren sie nicht. Dass eine Frau, die vor Männern ihr Haar löste, Anstoss erregte, wird meist aus späteren Quellen erschlossen. Was die Frau zur «Sünderin» machte, sagt der Text nicht; die spätere Gleichsetzung mit Maria Magdalena ([[LUK.8.2]]) hat im Text keinen Anhalt.",
  ["LUK.7.36-LUK.7.46", "GEN.18.4", "PSA.23.5"], [],
  [],
  "Gascht bim Ässe: Wasser, Kuss und Öl",
  "Bi me feschtliche Ässe sind d Gäscht uf Polschter gläge, uf de linke Arm gstützt, d Füess vom Tisch wäg (vgl. BG-JHN-2012); so hät d Frau «vo hine» zu de Füess vom Jesus häre chöne ([[LUK.7.38]]). Settigi Ässe sind oft halb öffentlich gsii; Lüüt, wo nöd iiglade gsii sind, händ chöne zueluege. Zur Gaschtfründschaft händ Wasser für di staubige Füess ghört ([[GEN.18.4]]; [[JDG.19.21]]), en Begrüessigskuss und Öl für de Chopf (vgl. [[PSA.23.5]]). En Denar isch de üblich Taglohn vo me Arbeiter gsii (Vergliich mit [[MAT.20.2]]); 500 Denar händ also em Lohn vo meh als eme Jahr Arbet entsproche, 50 Denar dem vo knapp zwei Mönet.",
  "Öb das, wo de Simon nöd gmacht hät, als Chränkig gmeint isch, wird verschide beurteilt; Pflicht isch es nöd gsii. Dass e Frau, wo vor Manne iri Haar ufgmacht hät, Aastoss erregt hät, wird meischtens us spöötere Quelle erschlosse. Was d Frau zur «Sünderin» gmacht hät, seit de Text nöd; dass me si spööter mit de Maria vo Magdala gliichgsetzt hät ([[LUK.8.2]]), hät im Text kein Aahaltspunkt.",
  []),
 ("BG-LUK-0014", U(8, 1, 3), "LUK.8.1-LUK.8.3", GAL, "probable", "Frauen, die Jesus mit ihrem Besitz unterstützten",
  "Wandernde Lehrer waren auf Gastgeber und Unterstützer angewiesen. Lukas nennt Frauen, die über eigene Mittel verfügten: Johanna war die Frau des Chuza, eines Verwalters (ἐπίτροπος) des Herodes Antipas, und gehörte damit zur Oberschicht am Hof ([[LUK.8.3]]; vgl. [[LUK.24.10]]). Maria, «genannt Magdalena», stammte wohl aus Magdala am Westufer des Sees (vgl. BG-JHN-3011). Frauen konnten nach jüdischem und römischem Recht Besitz haben, etwa aus Mitgift oder Erbe; Urkunden einer jüdischen Frau aus dem frühen 2. Jahrhundert (das Archiv der Babatha) zeigen, dass Frauen Land und Geld besassen und darüber vor Gericht stritten. Dass Frauen mit einem Lehrer und seinen Schülern umherzogen, war ungewöhnlich.",
  "Wie ungewöhnlich oder anstössig das Mitziehen von Frauen war, lässt sich aus den Quellen nur schwer bestimmen. Ob Chuza mit dem königlichen Beamten in [[JHN.4.46-JHN.4.53]] zu tun hat, ist reine Vermutung.",
  ["LUK.8.1-LUK.8.3", "LUK.24.10"], ["Archiv der Babatha aus der Wüste Juda (frühes 2. Jahrhundert n. Chr.)"],
  [("grc", "ἐπίτροπος", "Verwalter, Bevollmächtigter")],
  "Fraue, wo de Jesus mit irem Bsitz understützt händ",
  "Lehrer, wo umezoge sind, sind uf Gaschtgeber und Understützer aagwise gsii. De Lukas nännt Fraue, wo über eigeti Mittel verfüegt händ: D Johanna isch d Frau vom Chuza gsii, vo me Verwalter (ἐπίτροπος) vom Herodes Antipas, und hät demit zur Oberschicht am Hof ghört ([[LUK.8.3]]; vgl. [[LUK.24.10]]). D Maria, «wo mer di vo Magdala nännt», isch wohl vo Magdala am Weschtufer vom See choo (vgl. BG-JHN-3011). Fraue händ nach jüdischem und römischem Rächt Bsitz chöne haa, öppe us de Mitgift oder us eme Erb; Urkunde vo ere jüdische Frau us em früene 2. Jahrhundert (s Archiv vo de Babatha) zeiged, dass Fraue Land und Gäld bsässe und drüber vor Gricht gstritte händ. Dass Fraue mit eme Lehrer und sine Schüeler umezoge sind, isch ungwöönlich gsii.",
  "Wie ungwöönlich oder aastössig s Mitzie vo Fraue gsii isch, laat sich us de Quelle nu schwär bestimme. Öb de Chuza mit em königliche Beamte i [[JHN.4.46-JHN.4.53]] z tue hät, isch e reini Vermuetig.",
  ["Verwalter, Bevollmächtigte"]),
 ("BG-LUK-0015", U(9, 51, 56), "LUK.9.52-LUK.9.53", GAL, "probable", "Festpilger aus Galiläa in Samarien",
  "Der kürzeste Weg von Galiläa nach Jerusalem führte durch Samarien; nach Josephus dauerte die Reise so drei Tage. Die Samaritaner verehrten Gott auf dem Berg Garizim, wo ihr Tempel stand, bis ihn der jüdische Herrscher Johannes Hyrkan im späten 2. Jahrhundert v. Chr. zerstörte (zu den Samaritanern allgemein BG-JHN-1005 und BG-MAT-2010). Wer zum Fest nach Jerusalem zog, bestritt damit den Anspruch des Garizim. Josephus berichtet, dass unter dem Statthalter Cumanus (um 50 n. Chr.) Festpilger aus Galiläa in einem samaritanischen Dorf getötet wurden, was blutige Vergeltung auslöste. Dass ein Dorf Jesus nicht aufnimmt, «weil er unterwegs nach Jerusalem war» ([[LUK.9.53]]), entspricht dieser Spannung.",
  "Josephus sagt, die Galiläer seien gewohnt gewesen, zu den Festen durch Samarien zu ziehen; wie oft sie dabei Feindseligkeit erlebten, ist nicht bekannt. Das Jahr der Zerstörung des Garizim-Tempels wird zwischen etwa 128 und 107 v. Chr. angesetzt.",
  ["LUK.9.51-LUK.9.56", "JHN.4.9", "JHN.4.20"],
  ["Josephus, Leben (Vita) 269", "Josephus, Jüdische Altertümer 13,254–256; 20,118–136", "Josephus, Jüdischer Krieg 2,232–246"],
  [],
  "Fäschtpilger us Galiläa in Samarie",
  "De chürzischt Wäg vo Galiläa uf Jerusalem hät dur Samarie gfüert; nach em Josephus hät d Reis eso drüü Täg duuret. D Samaritaner händ Gott uf em Bärg Garizim verehrt, wo ire Tämpel gstande isch, bis en de jüdisch Herrscher Johannes Hyrkan im spoote 2. Jahrhundert v. Chr. zerstört hät (zu de Samaritaner allgemein BG-JHN-1005 und BG-MAT-2010). Wär as Fäscht uf Jerusalem gange isch, hät demit em Garizim sin Aaspruch bestritte. De Josephus brichtet, dass under em Statthalter Cumanus (um 50 n. Chr.) Fäschtpilger us Galiläa i me samaritanische Dorf umbracht worde sind, was e bluetigi Vergältig usglöst hät. Dass es Dorf de Jesus nöd ufnimmt, «wil er understwägs uf Jerusalem gsii isch» ([[LUK.9.53]]), entspricht dere Spannig.",
  "De Josephus seit, d Galiläer segid s gwont gsii, a d Fäscht dur Samarie z zie; wie oft si debii Feindseligkeit erläbt händ, weiss mer nöd. S Jahr, wo de Garizim-Tämpel zerstört worde isch, wird zwüsche öppe 128 und 107 v. Chr. aagsetzt.",
  []),
 ("BG-LUK-0016", U(10, 25, 37), "LUK.10.30-LUK.10.35", GAL, "possible", "Priester, Levit und ein «Halbtoter»",
  "Der Weg von Jerusalem nach Jericho führt rund 25 Kilometer durch die Wüste Juda und fällt dabei um etwa 1000 Meter (zum Weg vgl. BG-MRK-2001). Priester und Leviten wohnten nicht alle in Jerusalem; sie kamen für ihren Dienst in den Tempel (vgl. BG-LUK-0002). Nach [[LEV.21.1-LEV.21.3]] durfte sich ein Priester ausser an nahen Angehörigen nicht an einem Toten verunreinigen; wer einen Toten berührte, war sieben Tage unrein ([[NUM.19.11]]). Der Überfallene lag «halbtot» da ([[LUK.10.30]]); ob er lebte, war von weitem nicht zu erkennen. Öl und Wein waren übliche Mittel zur Wundpflege: Wein reinigte, Öl linderte (vgl. [[ISA.1.6]]). Zwei Denare, zwei Tageslöhne, reichten für mehrere Tage Unterkunft und Kost.",
  "Ob Lukas das Vorübergehen mit Reinheitsvorschriften erklären will, ist umstritten: Priester und Levit gehen «hinab», also von Jerusalem weg, und die spätere jüdische Überlieferung verpflichtet jeden, auch Priester, einen unbestatteten Toten zu begraben. Die Angabe zur Kaufkraft von zwei Denaren ist eine ungefähre Schätzung.",
  ["LUK.10.30-LUK.10.35", "LEV.21.1-LEV.21.3", "NUM.19.11", "ISA.1.6"], [],
  [],
  "Prieschter, Levit und en «Halbtote»",
  "De Wäg vo Jerusalem uf Jericho füert öppe 25 Kilometer dur d Wüeschti Juda und gaat debii um öppe 1000 Meter abe (zum Wäg vgl. BG-MRK-2001). Prieschter und Levite händ nöd alli z Jerusalem gwont; si sind für ire Dienscht in Tämpel choo (vgl. BG-LUK-0002). Nach [[LEV.21.1-LEV.21.3]] hät sich en Prieschter usser a nööche Aaghörige nöd a me Tote dörfe verunreinige; wär en Tote aagrüert hät, isch sibe Täg unrein gsii ([[NUM.19.11]]). De Überfallni isch «halbtot» dagläge ([[LUK.10.30]]); öb er no gläbt hät, hät me vo wiitem nöd chöne gseh. Öl und Wii sind üblichi Mittel für d Wundpfläg gsii: Wii hät greiniget, Öl hät glinderet (vgl. [[ISA.1.6]]). Zwee Denar, zwee Taglöhn, händ für meereri Täg Underkunft und Ässe glänget.",
  "Öb de Lukas s Verbiigaa mit Reinheitsvorschrifte erkläre wott, isch umstritte: De Prieschter und de Levit gönd «abe», also vo Jerusalem wäg, und di spööter jüdisch Überliferig verpflichtet jede, au en Prieschter, en unbeerdigte Tote z begrabe. D Aagaab zur Chaufchraft vo zwee Denar isch e ungfääri Schätzig.",
  []),
 ("BG-LUK-0017", U(10, 38, 42), "LUK.10.39", GAL, "probable", "Zu den Füssen eines Lehrers sitzen",
  "Schüler sassen zu den Füssen ihres Lehrers; Paulus sagt von sich, er sei «zu den Füssen Gamaliels» erzogen worden ([[ACT.22.3]]). Ein Spruch in der Mischna rät: «Dein Haus sei ein Versammlungsort für die Weisen; setz dich in den Staub ihrer Füsse und trink ihre Worte mit Durst.» Dass eine Frau diesen Platz einnimmt, war ungewöhnlich; Frauen sind als Schülerinnen eines Lehrers selten belegt. Die Gastgeberin war für die Bewirtung zuständig; ein Gast mit seinen Begleitern bedeutete viel Arbeit ([[LUK.10.40]]).",
  "Wie weit Frauen zur Zeit Jesu in der Tora unterrichtet wurden, ist umstritten; die rabbinischen Quellen sind später und uneinheitlich. Ob «zu den Füssen sitzen» hier schon die feste Bedeutung «Schülerin sein» hat, ist Deutung (INT-LUK-0011).",
  ["LUK.10.38-LUK.10.42", "ACT.22.3"], ["Mischna, Avot 1,4"],
  [],
  "Zu de Füess vo me Lehrer sitze",
  "Schüeler sind zu de Füess vo irem Lehrer gsässe; de Paulus seit vo sich, er sig «zu de Füess vom Gamaliel» erzoge worde ([[ACT.22.3]]). En Spruch i de Mischna root: «Dis Huus söll en Versammligsort für d Wiise sii; setz di in Staub vo irne Füess und trink iri Wort mit Durscht.» Dass e Frau dä Platz iinimmt, isch ungwöönlich gsii; Fraue sind als Schüelerinne vo me Lehrer sälte belegt. D Gaschtgeberin isch fürs Bewirte zueständig gsii; en Gascht mit sine Begleiter hät vil Arbet bedüütet ([[LUK.10.40]]).",
  "Wie wiit Fraue zur Ziit vo Jesus i de Tora underrichtet worde sind, isch umstritte; di rabbinische Quelle sind spööter und nöd eiheitlich. Öb «zu de Füess sitze» da scho di fescht Bedüütig «Schüelerin sii» hät, isch Düütig (INT-LUK-0011).",
  []),
 ("BG-LUK-0018", U(11, 37, 54), "LUK.11.38-LUK.11.41", GAL, "probable", "Aussen und innen: Reinheit von Gefässen",
  "Fromme Kreise, besonders die Pharisäer, wuschen sich vor dem Essen die Hände, auch ausserhalb des Tempels (vgl. BG-MRK-1010); Lukas sagt, Jesus habe sich nicht «gewaschen» (βαπτίζω, [[LUK.11.38]]). Für Gefässe unterschied die jüdische Überlieferung zwischen Aussenseite und Innenseite: Ein Gefäss konnte aussen unrein und innen rein sein oder umgekehrt, und es wurde erörtert, welche Seite für die Reinheit entscheidend ist. Jesus nimmt dieses Bild auf und wendet es auf den Menschen an: Wer das Äussere reinigt, das Innere aber voll «Raub und Bosheit» lässt, hat das Wichtigere vergessen ([[LUK.11.39-LUK.11.40]]). Zum Zehnten von Gartenkräutern und zu den Gräbern siehe BG-MAT-4007 und BG-MAT-4008.",
  "Die Mischna wurde um 200 n. Chr. aufgeschrieben; wie weit ihre Unterscheidungen schon zur Zeit Jesu galten, ist umstritten. Ob in [[LUK.11.38]] ein Untertauchen oder nur ein Händewaschen gemeint ist, lässt das Wort offen.",
  ["LUK.11.37-LUK.11.41"], ["Mischna, Kelim 25,1–9"],
  [("grc", "βαπτίζω", "eintauchen, waschen; taufen")],
  "Usse und inne: Reinheit vo Gfäss",
  "Frommi Chreis, bsunders d Pharisäer, händ sich vor em Ässe d Händ gwäsche, au usserhalb vom Tämpel (vgl. BG-MRK-1010); de Lukas seit, de Jesus heig sich nöd «gwäsche» (βαπτίζω, [[LUK.11.38]]). Bi Gfäss hät di jüdisch Überliferig zwüsche de Ussesiite und de Innesiite underschide: Es Gfäss hät chöne usse unrein und inne rein sii oder umgekehrt, und mer hät drüber diskutiert, weli Siite für d Reinheit entscheidend isch. De Jesus nimmt das Bild uf und wändet s uf de Mänsch aa: Wär s Üsser putzt, s Inner aber voll «Raub und Bosheit» laat, hät s Wichtiger vergässe ([[LUK.11.39-LUK.11.40]]). Zum Zäänte vo Gartechrüüter und zu de Greber lueg BG-MAT-4007 und BG-MAT-4008.",
  "D Mischna isch um 200 n. Chr. ufgschribe worde; wie wiit iri Underscheidige scho zur Ziit vo Jesus gulte händ, isch umstritte. Öb i [[LUK.11.38]] es Undertauche oder nu es Händwäsche gmeint isch, laat s Wort offe.",
  ["iitauche, wäsche; taufe"]),
 ("BG-LUK-0019", U(12, 1, 12), "LUK.12.6", GAL, "probable", "Spatzen, Groschen und Rappen",
  "Lukas nennt kleine Münzen des römischen Systems. Ein Denar (Silber) war ein Tageslohn (vgl. BG-MAT-3017). Ein As (ἀσσάριον, in der Übersetzung «Groschen») war eine Kupfermünze im Wert eines Sechzehntels eines Denars; für zwei davon bekam man fünf Spatzen ([[LUK.12.6]]), die als billiges Fleisch auf Märkten verkauft wurden; bei Matthäus sind es zwei Spatzen für ein As (Vergleich mit [[MAT.10.29]]). Das Lepton (λεπτόν, «Rappen», [[LUK.12.59]]) war die kleinste Münze im Umlauf; zwei Lepta ergaben einen Quadrans, ein Viertel des As (Vergleich mit [[MRK.12.42]]); ein Lepton war also ein 128stel eines Denars.",
  "Die Umrechnungen beruhen auf dem römischen Reichssystem; in den östlichen Provinzen liefen daneben örtliche Münzen mit anderen Werten. «Lepton» ist eine griechische Bezeichnung für eine Kleinmünze, kein römischer Münzname; die Gleichung mit dem Quadrans folgt [[MRK.12.42]].",
  ["LUK.12.6", "LUK.12.59", "MAT.10.29", "MRK.12.42"], [],
  [("grc", "ἀσσάριον", "As, kleine Kupfermünze"), ("grc", "λεπτόν", "Lepton, kleinste Münze")],
  "Spatze, Batze und Rappe",
  "De Lukas nännt chliini Münze vom römische Süschteem. En Denar (Silber) isch en Taglohn gsii (vgl. BG-MAT-3017). En As (ἀσσάριον, i de Übersetzig «Batze») isch e Kupfermünze gsii, wo en Sächzähntel vo me Denar wärt gsii isch; für zwee devo hät me föif Spatze übercho ([[LUK.12.6]]), wo als billigs Fleisch uf em Märt verchauft worde sind; bim Matthäus sind s zwee Spatze für en As (Vergliich mit [[MAT.10.29]]). S Lepton (λεπτόν, «Rappe», [[LUK.12.59]]) isch di chliinscht Münze im Umlauf gsii; zwei Lepta händ en Quadrans ggää, en Viertel vom As (Vergliich mit [[MRK.12.42]]); es Lepton isch also en 128schtel vo me Denar gsii.",
  "D Umrächnige beruhed uf em römische Riichssüschteem; i de öschtliche Provinze sind denäbe örtlichi Münze mit andere Wärt im Umlauf gsii. «Lepton» isch e griechischi Bezeichnig für e Chliimünze, kein römische Münzname; d Gliichig mit em Quadrans folgt [[MRK.12.42]].",
  ["As, chliini Kupfermünze", "Lepton, chliinschti Münze"]),
 ("BG-LUK-0020", U(12, 54, 59), "LUK.12.54-LUK.12.55", GAL, "high", "Wolken aus dem Westen, Wind aus dem Süden",
  "Im Land Israel kommt der Regen im Winterhalbjahr mit Wolken vom Mittelmeer im Westen; so sieht Elijas Diener eine kleine Wolke «aus dem Meer» aufsteigen, bevor es regnet ([[1KI.18.44-1KI.18.45]]). Südliche und östliche Winde aus der Wüste bringen trockene Hitze, besonders im Frühling und im Herbst. Bauern und Hirten lasen das Wetter an solchen Zeichen ab. Jesus wirft den Menschenmengen vor, dass sie diese Zeichen deuten können, nicht aber die Zeit, in der sie leben ([[LUK.12.56]]).",
  "Die Wetterregeln gelten im Grossen; im Einzelnen wechseln Winde und Regen.",
  ["LUK.12.54-LUK.12.56", "1KI.18.44-1KI.18.45"], [],
  [],
  "Wolche us em Weschte, Wind us em Süde",
  "Im Land Israel chunnt de Rääge im Winterhalbjahr mit Wolche vom Mittelmeer im Weschte; so gseht de Diener vom Elija e chliini Wolche «us em Meer» ufstiige, bevor s rägnet ([[1KI.18.44-1KI.18.45]]). Wind us em Süde und Oschte, us de Wüeschti, bringed trochni Hitz, bsunders im Früelig und im Herbscht. Buure und Hirte händ s Wätter a settige Zeiche abgläse. De Jesus wirft de Lüüt vor, dass si die Zeiche chönd düüte, aber nöd d Ziit, i dere si läbed ([[LUK.12.56]]).",
  "D Wätterregle gälted im Grosse; im Einzelne wächsled Wind und Rääge.",
  []),
]


def _pruefe_zaehlungen():
    """Jede im Text genannte Zahl gegen die MACULA-Lemmata prüfen."""
    cache = {}

    def eintraege(buch):
        if buch not in cache:
            ent = {}
            for f in sorted((D / "annotations").glob(f"MACULA-SBLGNT-{buch}-0*.json")):
                ent.update(json.loads(f.read_text(encoding="utf-8"))["entries"])
            cache[buch] = ent
        return cache[buch]

    def stelle(tid):
        return tuple(int(x) for x in tid.split("-")[3:5])

    fehler = []
    for buch, lemma, von, bis, soll in ZAEHLUNGEN:
        ist = sum(1 for tid, e in eintraege(buch).items() if e.get("lemma") == lemma and von <= stelle(tid) <= bis)
        if ist != soll:
            fehler.append(f"{buch} {lemma} {von}–{bis}: erwartet {soll}, gefunden {ist}")
    for buch, von, bis, soll in GEIST:
        ent = eintraege(buch)
        ids = list(ent)
        ist = 0
        for i, tid in enumerate(ids):
            if ent[tid].get("lemma") != "πνεῦμα" or not von <= stelle(tid) <= bis:
                continue
            nah = [ent[k].get("lemma") for k in ids[max(0, i - 3):i + 4] if stelle(k) == stelle(tid)]
            ist += "ἅγιος" in nah
        if ist != soll:
            fehler.append(f"{buch} heiliger Geist {von}–{bis}: erwartet {soll}, gefunden {ist}")
    namen = sum(1 for tid, e in eintraege("LUK").items()
                if (3, 23) <= stelle(tid) <= (3, 38) and e.get("lemma", "")[:1].isupper())
    if namen != STAMMBAUM:
        fehler.append(f"Stammbaum: erwartet {STAMMBAUM} Namen, gefunden {namen}")
    if fehler:
        raise SystemExit("Zählungen stimmen nicht:\n" + "\n".join(fehler))


def _pruefe_fachwoerter():
    """Griechische und hebräische Wörter in Deutungen und Hintergrund müssen als terms erfasst sein, auch in der Mundart."""
    wort = re.compile(r"[Ͱ-Ͽἀ-῿][Ͱ-Ͽἀ-῿̀-ͯ]*|[֐-׿]+")
    fehlend = []
    for rec in INTERPRETATIONS:
        erfasst = " ".join(t[1] for t in rec[7])
        for texte in ([rec[3], rec[5]] + rec[6], [rec[8], rec[9]] + rec[10]):
            fehlend += [(rec[0], w) for t in texte for w in wort.findall(t) if w not in erfasst]
        if len(rec[7]) != len(rec[11]) or len(rec[6]) != len(rec[10]):
            fehlend.append((rec[0], "Listenlänge Mundart"))
    for rec in BACKGROUND:
        erfasst = " ".join(t[1] for t in rec[10])
        for texte in ([rec[6], rec[7] or ""], [rec[12], rec[13] or ""]):
            fehlend += [(rec[0], w) for t in texte for w in wort.findall(t) if w not in erfasst]
        if len(rec[10]) != len(rec[14]):
            fehlend.append((rec[0], "Listenlänge Mundart"))
    if fehlend:
        raise SystemExit("Ursprachwörter ohne terms: " + "; ".join(f"{i}: {w}" for i, w in fehlend))


def _pruefe_mundart_und_ids():
    """Mundart-Schreibung nach lukas_einheitlich.py; IDs im Bereich 0001–0499; keine bestehenden Fremd-IDs überschreiben."""
    import lukas_einheitlich
    texte = []
    for f in FINDINGS:
        texte += [f[7], f[8]]
    for i in INTERPRETATIONS:
        texte += [i[8], i[9]] + i[10] + i[11]
    for p in PRINCIPLES:
        texte.append(p[4])
    for a in APPLICATIONS:
        texte += [a[4], a[5]]
    for q in QUESTIONS:
        texte += [q[4], q[5]]
    for b in BACKGROUND:
        texte += [b[11], b[12], b[13] or ""] + b[14]
    lukas_einheitlich.pruefe_mundart(texte, "lukas_study_a.py")
    ids = [x[0] for k in (FINDINGS, INTERPRETATIONS, PRINCIPLES, APPLICATIONS, QUESTIONS, RELATIONS, BACKGROUND) for x in k]
    if len(ids) != len(set(ids)):
        raise SystemExit("Doppelte IDs")
    for i in ids + ["STUDY-LUK-0001"]:
        m = re.fullmatch(r"[A-Z]+-LUK-(\d{4})", i)
        if not m or not 1 <= int(m[1]) <= 499:
            raise SystemExit(f"{i}: ausserhalb des Nummernbereichs 0001–0499")
    ordner = {"FIND": "findings", "INT": "interpretations", "PRIN": "principles", "APP": "applications",
              "QUESTION": "questions", "REL": "relations", "BG": "background", "STUDY": "studies"}
    for i in ids + ["STUDY-LUK-0001"]:
        p = D / ordner[i.split("-")[0]] / f"{i}.json"
        if p.exists() and "lukas_study_a" not in p.read_text(encoding="utf-8") and \
                "Lukas 1–12" not in p.read_text(encoding="utf-8") and "TAG-LUKE" not in p.read_text(encoding="utf-8"):
            raise SystemExit(f"{i} existiert schon mit fremdem Inhalt; nicht überschreiben")


def run():
    import _study
    _pruefe_zaehlungen()
    _pruefe_fachwoerter()
    _pruefe_mundart_und_ids()
    _study.DATE = DATUM
    _study.AUTH = f"KI-Entwurf (Claude) vom {DATUM} auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
    _study.AUTH_GSW = (f"KI-Entwurf (Claude) vom {DATUM}; aus dem Hochdeutschen in Züridüütsch gefasst; "
                       "Mundart noch nicht muttersprachlich geprüft.")
    # Bestehenden Kontext unverändert weitergeben: _lib.write erkennt Gleichheit und schreibt nichts.
    context = json.loads((D / "contexts" / f"{READERS}.json").read_text(encoding="utf-8"))
    extra = sorted((p.stem for ch in range(1, 13) for p in (D / "translations").glob(f"TRANS-LUK-{ch:03d}-*-WORKING.json")
                    if not p.stem.startswith("TRANS-LUK-011-001-004")),
                   key=lambda x: ("-GSW-" in x, x))
    _study.write_study({"TAGS": TAGS, "CONTEXT": context, "FINDINGS": FINDINGS, "INTERPRETATIONS": INTERPRETATIONS,
                        "PRINCIPLES": PRINCIPLES, "APPLICATIONS": APPLICATIONS, "QUESTIONS": QUESTIONS, "RELATIONS": RELATIONS,
                        "BACKGROUND": BACKGROUND, "SUMMARIES": [],
                        "STUDY": ("STUDY-LUK-0001", "Lukas 1–12: Studieninhalte", CHAPTERS[1], extra,
                                  ["Mundart muttersprachlich prüfen",
                                   "Fachliche Prüfung der Befunde, Deutungen, Grundsätze, Anwendungen und des Hintergrunds",
                                   "Antike Quellenangaben in BG-LUK-0001 bis BG-LUK-0018 am Text nachschlagen (docs/QUELLENPRUEFUNG.md); "
                                   "bisher nur aus dem Gedächtnis genannt, insbesondere Mischna Tamid 5,2, Kidduschin 4,14, "
                                   "Kelim 25, Josephus Altertümer 15,92 und die Weihinschrift aus Abila",
                                   "Literaturangaben (Alexander 1993, Conzelmann 1954, Yoder 1972, Wink 1992, Bailey 1976 und 1980, "
                                   "Jeremias, Metzger, Wellhausen, Schüssler Fiorenza, Meister Eckhart, Origenes, Augustinus, "
                                   "Julius Africanus) bibliographisch prüfen",
                                   "Septuaginta-Wortlaut zu [[1KI.17.23]] (FIND-LUK-0014) und Qumran-Text 4Q521 (FIND-LUK-0023) prüfen",
                                   "Zählungen beruhen auf MACULA-Lemmata zum SBLGNT; andere Editionen können abweichen",
                                   "Kapitel- und Buchzusammenfassungen entstehen aus den Kernanalysen (nicht Teil dieses Auftrags)"])},
                       "Lukas 1–12")


if __name__ == "__main__":
    run()
