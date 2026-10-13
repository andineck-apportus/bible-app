"""Autorenwerkzeug: erzeugt die Studieninhalte zum Vaterunser (Mt 6,5–15; Lk 11,1–4).

Aufruf: python3 scripts/authoring/vaterunser.py

Erzeugt: Werke, Kontexte, Texteinheiten, Arbeitsübersetzungen mit Alternativen, Wortzuordnungen
(Mt 6,9–13; Lk 11,2–4, vollständig), Befunde, Deutungen, Grundsatz, Anwendung, offene Fragen,
Beziehungen, Hintergrundnotizen, Kapitelzusammenfassungen und den Studiendatensatz.
Alle Inhalte sind KI-Entwürfe (Claude) vom 2026-10-12 auf Wunsch von Andi Neck, fachlich ungeprüft.
Bestehende Datensätze mit gleicher ID werden überschrieben; das Skript ist nur für die Ersterstellung
gedacht. Spätere inhaltliche Änderungen gehören mit Revisionsvermerk direkt in die Datensätze.
"""
# Seit Migration v0.31 (2026-10-13) sind die erzeugten Daten weiterbearbeitet (sprachneutrale Feldnamen, Stellen-Marken
# [[…]], Titel als Lokalisierungen). Dieses Skript ist der dokumentierte Entstehungsweg, keine laufende Quelle: ein
# erneuter Lauf würde den migrierten Stand überschreiben. Änderungen direkt in data/ vornehmen (mit revision_log).
import sys as _sys
if "--force-historisch" not in _sys.argv:
    _sys.exit("Historisches Autorenwerkzeug (vor Migration v0.31); nicht erneut ausführen. Siehe Kommentar im Skript.")
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

D = ROOT / "data"
DATE = "2026-10-12"
AUTH = f"KI-Entwurf (Claude) vom {DATE} auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
KN = {"asserted_at": DATE, "supersedes": None}
LP = "TAG-LORDS-PRAYER"
written = []


def w(folder, rec):
    p = D / folder / f"{rec['id']}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    written.append(rec["id"])


R = refs.canonical

# --- Werke und Kontexte -------------------------------------------------------------------------
w("works", {"id": "WORK-MAT", "type": "work", "status": "draft", "tags": ["TAG-MATTHEW"],
            "name": "Matthäusevangelium", "original_language": "grc"})
w("works", {"id": "WORK-LUK", "type": "work", "status": "draft", "tags": ["TAG-LUKE"],
            "name": "Lukasevangelium", "original_language": "grc"})
w("contexts", {"id": "CTX-MAT-READERS-0085", "type": "context", "status": "draft",
               "tags": ["TAG-MATTHEW", "TAG-UNCERTAINTY"], "period": {"approx_year": 85, "era": "CE"},
               "region": "umstritten (oft Syrien vermutet)", "language_context": ["grc"],
               "audience": "Erste Leserschaft des Matthäusevangeliums: griechischsprachige Gemeinden mit starker jüdischer Prägung",
               "note_de": "Datierung meist um 80–90 n. Chr.; Ort und Zusammensetzung der Gemeinden sind umstritten."})
w("contexts", {"id": "CTX-LUK-READERS-0085", "type": "context", "status": "draft",
               "tags": ["TAG-LUKE", "TAG-UNCERTAINTY"], "period": {"approx_year": 85, "era": "CE"},
               "region": "umstritten", "language_context": ["grc"],
               "audience": "Erste Leserschaft des Lukasevangeliums: griechischsprachig, vielfach nicht jüdischer Herkunft; gewidmet einem Theophilus (Lk 1,3)",
               "note_de": "Datierung meist um 80–90 n. Chr.; Ort umstritten."})

# --- Texteinheiten ------------------------------------------------------------------------------
def tu(id_, work, rng, kind, title, summary, parts=None, tags=None, note=None):
    rec = {"id": id_, "type": "text_unit", "status": "draft", "tags": tags or [LP], "work": work,
           "range": R(rng), "kind": kind, "title": title}
    if parts:
        rec["parts"] = parts
    if note:
        rec["segmentation_note_de"] = note
    rec.update({"knowledge": KN, "summary_de": summary, "summary_authorship_de": AUTH})
    w("text-units", rec)


tu("TU-MAT-006-005-015", "WORK-MAT", "Mt 6,5–15", "section", "Vom Beten",
   "Jesus warnt davor, zum Schein oder mit vielen Worten zu beten. Er gibt seinen Jüngern das Vaterunser und betont danach, dass Vergebung empfangen und Vergebung gewähren zusammengehören.",
   parts=["TU-MAT-006-005-008", "TU-MAT-006-009-013", "TU-MAT-006-014-015"], tags=["TAG-MATTHEW", LP, "TAG-PRAYER"],
   note="Teil der Bergpredigt (Mt 5–7) und der Reihe über Almosen, Beten und Fasten (6,1–18); Abgrenzung als Gliederungsvorschlag.")
tu("TU-MAT-006-005-008", "WORK-MAT", "Mt 6,5–8", "discourse", "Nicht zum Schein und nicht mit vielen Worten",
   "Beten soll nicht der eigenen Wirkung vor anderen dienen. Gott kennt die Bedürfnisse schon, bevor man bittet.",
   tags=["TAG-MATTHEW", "TAG-PRAYER"])
tu("TU-MAT-006-009-013", "WORK-MAT", "Mt 6,9–13", "prayer", "Das Vaterunser",
   "Ein Gebet in sieben Bitten: drei richten sich auf Gottes Namen, Reich und Willen, vier auf das, was Menschen brauchen: Brot, Vergebung, Bewahrung und Rettung.",
   tags=["TAG-MATTHEW", LP, "TAG-PRAYER"])
tu("TU-MAT-006-014-015", "WORK-MAT", "Mt 6,14–15", "discourse", "Vergeben und Vergebung empfangen",
   "Jesus greift die Bitte um Vergebung auf: Wer anderen vergibt, dem vergibt auch Gott.",
   tags=["TAG-MATTHEW", LP])
tu("TU-LUK-011-001-004", "WORK-LUK", "Lk 11,1–4", "prayer", "Herr, lehre uns beten",
   "Ein Jünger bittet Jesus, sie beten zu lehren. Jesus antwortet mit einer kurzen Fassung des Vaterunsers in fünf Bitten.",
   tags=["TAG-LUKE", LP, "TAG-PRAYER"],
   note="Beginn eines grösseren Abschnitts über das Beten (Lk 11,1–13); hier nur 11,1–4 bearbeitet.")

# --- Übersetzungen ------------------------------------------------------------------------------
MT = {
    5: "Und wenn ihr betet, sollt ihr nicht sein wie die Heuchler; denn sie lieben es, in den Synagogen und an den Ecken der breiten Strassen zu stehen und zu beten, damit sie sich den Menschen zeigen. Amen, ich sage euch: Sie haben ihren Lohn schon erhalten.",
    6: "Du aber, wenn du betest, geh in deine Kammer, schliess deine Tür und bete zu deinem Vater, der im Verborgenen ist; und dein Vater, der ins Verborgene sieht, wird es dir vergelten.",
    7: "Wenn ihr aber betet, plappert nicht wie die Heiden; denn sie meinen, sie würden erhört, wenn sie viele Worte machen.",
    8: "Seid ihnen also nicht gleich; denn euer Vater weiss, was ihr braucht, bevor ihr ihn bittet.",
    9: "So sollt ihr nun beten: Unser Vater in den Himmeln, dein Name werde geheiligt;",
    10: "dein Reich komme; dein Wille geschehe, wie im Himmel, so auch auf Erden.",
    11: "Unser tägliches Brot gib uns heute.",
    12: "Und vergib uns unsere Schulden, wie auch wir unseren Schuldnern vergeben haben.",
    13: "Und führe uns nicht in Versuchung, sondern rette uns vor dem Bösen.",
    14: "Denn wenn ihr den Menschen ihre Verfehlungen vergebt, wird euer himmlischer Vater auch euch vergeben;",
    15: "wenn ihr aber den Menschen nicht vergebt, wird euer Vater eure Verfehlungen auch nicht vergeben.",
}
LK = {
    1: "Und es geschah, als er an einem Ort betete: Als er aufgehört hatte, sagte einer seiner Jünger zu ihm: Herr, lehre uns beten, wie auch Johannes seine Jünger gelehrt hat.",
    2: "Er aber sagte zu ihnen: Wenn ihr betet, sprecht: Vater, dein Name werde geheiligt; dein Reich komme.",
    3: "Unser tägliches Brot gib uns Tag für Tag.",
    4: "Und vergib uns unsere Sünden, denn auch wir selbst vergeben jedem, der uns etwas schuldet; und führe uns nicht in Versuchung.",
}

ORIGIN_NOTE = "Mögliche Erklärungen, wie die Unterschiede entstanden sein könnten. Sie stehen nebeneinander; keine ist als richtig entschieden. " + AUTH


def alt(var, rid, ref, de_from, de_to, effect, note, words, origin, related=None):
    a = {"reading": f"{var}:{rid}", "reference": R(ref), "de_from": de_from, "de_to": de_to, "effect": effect,
         "note_de": note,
         "readings_de": {k: [{"grc": g, "de": de, "note_de": nt} for g, de, nt in v] for k, v in words.items()},
         "origin_de": origin}
    if related:
        a["related_variants"] = related
    return a


MT_ALTS = [
    alt("VAR-SBLGNTAPP-MAT-006-005-01", "R2", "Mt 6,5", "wenn ihr betet, sollt ihr nicht sein wie",
        "wenn du betest, sollst du nicht sein wie", "gering",
        "Einzahl statt Mehrzahl: Angesprochen ist jeder Einzelne, wie in 6,6.",
        {"R1": [["προσεύχησθε, οὐκ ἔσεσθε ὡς", "ihr betet, ihr sollt nicht sein wie", "Mehrzahl"]],
         "R2": [["προσεύχῃ οὐκ ἔσῃ ὥσπερ", "du betest, du sollst nicht sein wie", "Einzahl"]]},
        ["Die Einzahl könnte an die Umgebung angeglichen sein: In 6,2–4 und 6,6 wird jeweils «du» angesprochen.",
         "Umgekehrt könnte die Mehrzahl an 6,7–9 angeglichen sein, wo «ihr» angesprochen wird."]),
    alt("VAR-SBLGNTAPP-MAT-006-006-01", "R2", "Mt 6,6", "wird es dir vergelten", "wird es dir öffentlich vergelten", "bedeutsam",
        "Mit dem Zusatz steht dem verborgenen Beten ein öffentlicher Lohn gegenüber.",
        {"R1": [["σοι", "dir", "ohne Zusatz"]], "R2": [["σοι ἐν τῷ φανερῷ", "dir im Offenen, öffentlich", "Zusatz"]]},
        ["Der Zusatz bildet ein Gegenstück zu «im Verborgenen» und könnte ergänzt worden sein, um den Gegensatz zu betonen; derselbe Zusatz findet sich in manchen Handschriften auch in 6,4 und 6,18.",
         "Wer den Zusatz für ursprünglich hält, muss erklären, warum er in den ältesten Handschriften fehlt; denkbar ist, dass er wegen des Gedankens an öffentlichen Lohn bewusst weggelassen wurde."]),
    alt("VAR-SBLGNTAPP-MAT-006-008-01", "R2", "Mt 6,8", "denn euer Vater weiss", "denn Gott, euer Vater, weiss", "gering",
        "Westcott-Hort folgen hier einer Lesart mit «Gott».",
        {"R1": [["ὁ πατὴρ", "der Vater", "ohne «Gott»"]], "R2": [["ὁ θεὸς ὁ πατὴρ", "Gott, der Vater", "mit «Gott»"]]},
        ["«Gott» kann als Verdeutlichung hinzugefügt worden sein, wie sie auch in der Liturgie üblich ist.",
         "Umgekehrt kann «Gott» beim Abschreiben ausgefallen sein, weil zwei Wortgruppen gleich mit «ὁ» beginnen."]),
    alt("VAR-SBLGNTAPP-MAT-006-012-01", "R2", "Mt 6,12", "wie auch wir unseren Schuldnern vergeben haben",
        "wie auch wir unseren Schuldnern vergeben", "bedeutsam",
        "Vergangenheit oder Gegenwart: Haben wir schon vergeben, oder vergeben wir (jetzt, immer wieder)?",
        {"R1": [["ἀφήκαμεν", "wir haben vergeben", "Aorist: abgeschlossene Handlung"]],
         "R2": [["ἀφίεμεν", "wir vergeben", "Gegenwart"]],
         "other": [["ἀφίομεν", "wir vergeben", "Nebenform der Gegenwart, so auch in Lk 11,4"]]},
        ["Die Gegenwart könnte an Lukas (11,4 «wir vergeben») und an das im Gottesdienst gesprochene Gebet angeglichen sein.",
         "Die Vergangenheitsform kann eine aramäische Ausdrucksweise wiedergeben, die einen gerade jetzt vollzogenen Akt meint («hiermit vergeben wir»); dann ist der Unterschied kleiner, als er im Deutschen aussieht.",
         "Wer die Gegenwart für ursprünglich hält, verweist auf ihre Verbreitung in der Mehrheit der späteren Handschriften."]),
    alt("VAR-SBLGNTAPP-MAT-006-013-01", "R2", "Mt 6,13", "rette uns vor dem Bösen",
        "rette uns vor dem Bösen. Denn dein ist das Reich und die Kraft und die Herrlichkeit in Ewigkeit. Amen",
        "bedeutsam",
        "Der vertraute Lobpreis am Schluss fehlt in den ältesten Handschriften des Matthäusevangeliums.",
        {"R1": [["πονηροῦ", "(dem) Bösen", "Ende des Gebets ohne Lobpreis"]],
         "R2": [["ὅτι σοῦ ἐστιν ἡ βασιλεία καὶ ἡ δύναμις καὶ ἡ δόξα εἰς τοὺς αἰῶνας· ἀμήν",
                 "denn dein ist das Reich und die Kraft und die Herrlichkeit in Ewigkeit. Amen",
                 "Lobpreis (Doxologie)"]]},
        ["Jüdische Gebete schlossen oft mit einem Lobpreis; ein Vorbild ist 1 Chr 29,11. Beim Beten im Gottesdienst wurde das Vaterunser wohl früh mit einem Lobpreis beendet, und dieser gelangte von dort in viele Handschriften.",
         "Die Didache, eine frühchristliche Gemeindeordnung (um 100), gibt das Vaterunser mit dem kürzeren Schluss «denn dein ist die Kraft und die Herrlichkeit in Ewigkeit» wieder. Das zeigt, dass ein Lobpreis sehr früh gebetet wurde, aber in verschiedenen Formen.",
         "Wer den Lobpreis für ursprünglich hält, verweist auf seine Verbreitung in der grossen Mehrheit der Handschriften und im kirchlichen Gebrauch."],
        related=None),
    alt("VAR-SBLGNTAPP-MAT-006-015-01", "R2", "Mt 6,15", "den Menschen nicht vergebt", "den Menschen ihre Verfehlungen nicht vergebt",
        "gering", "Der Zusatz wiederholt nur, was in 6,14 steht.",
        {"R1": [["ἀνθρώποις", "den Menschen", "ohne Zusatz"]],
         "R2": [["ἀνθρώποις τὰ παραπτώματα αὐτῶν", "den Menschen ihre Verfehlungen", "Zusatz wie in 6,14"]]},
        ["Der Zusatz kann aus 6,14 übernommen sein, um die beiden Sätze gleich zu gestalten.",
         "Ebenso kann er beim Abschreiben ausgefallen sein; die Ausgaben sind hier geteilt."]),
]
LK_ALTS = [
    alt("VAR-SBLGNTAPP-LUK-011-002-01", "R2", "Lk 11,2", "Vater, dein Name", "Unser Vater im Himmel, dein Name", "bedeutsam",
        "Die kurze Anrede «Vater» ist bei Lukas gut bezeugt; die längere entspricht Matthäus.",
        {"R1": [["Πάτερ", "Vater", "kurze Anrede"]],
         "R2": [["Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς", "Unser Vater in den Himmeln", "Anrede wie bei Matthäus"]]},
        ["Wer das Vaterunser in der Matthäusfassung auswendig kannte und im Gottesdienst betete, glich beim Abschreiben die kürzere Lukasfassung leicht daran an. Viele Textforscher erklären die längere Anrede bei Lukas so.",
         "Die kürzere Anrede entspricht auch dem aramäischen «Abba», mit dem Jesus Gott nach Mk 14,36 anredet."]),
    alt("VAR-SBLGNTAPP-LUK-011-002-02", "R2", "Lk 11,2", "dein Reich komme",
        "dein Reich komme; dein Wille geschehe, wie im Himmel, so auf der Erde", "bedeutsam",
        "Die Bitte um Gottes Willen steht in vielen Handschriften auch bei Lukas.",
        {"R1": [["σου", "dein (Reich)", "ohne weitere Bitte"]],
         "R2": [["γενηθήτω τὸ θέλημά σου ὡς ἐν οὐρανῷ καὶ ἐπὶ τῆς γῆς", "dein Wille geschehe, wie im Himmel, so auf der Erde", "Bitte wie bei Matthäus"]]},
        ["Auch hier ist eine Angleichung an die vertraute Matthäusfassung die häufigste Erklärung.",
         "Einige wenige spätere Handschriften und Kirchenväter (berichtet für die Minuskeln 700 und 162 sowie Gregor von Nyssa) haben an dieser Stelle stattdessen eine Bitte um den Heiligen Geist: «Dein Heiliger Geist komme über uns und reinige uns.» Diese Angabe ist hier nicht geprüft; sie zeigt, wie frei das Gebet in manchen Kreisen weitergegeben wurde."]),
    alt("VAR-SBLGNTAPP-LUK-011-004-01", "R2", "Lk 11,4", "führe uns nicht in Versuchung",
        "führe uns nicht in Versuchung, sondern rette uns vor dem Bösen", "bedeutsam",
        "Die letzte Bitte der Matthäusfassung steht in vielen, aber nicht in den ältesten Lukas-Handschriften.",
        {"R1": [["πειρασμόν", "Versuchung", "Ende des Gebets"]],
         "R2": [["ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ", "sondern rette uns vor dem Bösen", "Bitte wie bei Matthäus"]]},
        ["Auch dieser Zusatz lässt sich als Angleichung an Matthäus erklären.",
         "Wer ihn für ursprünglich hält, verweist auf seine weite Verbreitung; dass er gerade in 𝔓75, im Sinaiticus und im Vaticanus fehlt, spricht nach Ansicht vieler Textforscher eher für eine spätere Ergänzung."]),
]


def follows(book, ch, v0, v1):
    return sorted(f"{p.stem}:R1" for p in (D / f"variants/sblgntapp-{book.lower()}").glob(f"VAR-SBLGNTAPP-{book}-{ch:03d}-*.json")
                  if v0 <= int(p.stem.split("-")[-2]) <= v1)


METHOD = "Wörtlich orientierte Arbeitsübersetzung: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
w("translations", {
    "id": "TRANS-MAT-006-005-015-DE-WORKING", "type": "translation", "status": "draft", "tags": ["TAG-MATTHEW", LP],
    "reference": R("Mt 6,5–15"), "language": "de-CH", "translation_kind": "literal_original_working", "method_de": METHOD,
    "based_on_edition": "ED-SBLGNT", "based_on_tokens": "TOKSET-SBLGNT-MAT-006",
    "follows_readings": follows("MAT", 6, 5, 15),
    "text_by_reference": {R(f"Mt 6,{v}"): t for v, t in MT.items()},
    "translation_notes": [
        "6,5: ὑποκριταί ursprünglich «Schauspieler»; πλατεῖαι sind die breiten Strassen und Plätze.",
        "6,5: ἀπέχουσιν ist ein Begriff aus Quittungen: «sie haben (den Lohn) vollständig erhalten».",
        "6,6: ταμεῖον ist ein Vorrats- oder Innenraum, oft der einzige abschliessbare Raum eines Hauses.",
        "6,7: βατταλογέω ist sonst kaum belegt; meist als «plappern, leere Worte machen» verstanden.",
        "6,9: «in den Himmeln» gibt den griechischen Plural wieder; im Deutschen ist «im Himmel» üblich.",
        "6,11: Die Bedeutung von ἐπιούσιος ist unsicher (siehe Deutungen). «Täglich» folgt der verbreiteten Tradition und ist eine redaktionelle Entscheidung; ebenso möglich sind «für den kommenden Tag» oder «das zum Leben nötige».",
        "6,12: ὀφειλήματα sind wörtlich «Schulden», im Aramäischen zugleich ein Wort für Sünde.",
        "6,13: πειρασμός heisst «Versuchung» und «Prüfung». τοῦ πονηροῦ kann «dem Bösen» (Sache) oder «dem Bösen» (Person, der Böse) bedeuten.",
        "6,14–15: παραπτώματα «Verfehlungen, Fehltritte».",
    ],
    "authorship_de": AUTH, "knowledge": KN,
    "alternatives": MT_ALTS,
    "alternatives_note_de": "Deutsche Wiedergabe abweichender Lesarten, soweit sie die Übersetzung verändern. " + AUTH,
    "alternatives_origin_note_de": ORIGIN_NOTE,
})
w("translations", {
    "id": "TRANS-LUK-011-001-004-DE-WORKING", "type": "translation", "status": "draft", "tags": ["TAG-LUKE", LP],
    "reference": R("Lk 11,1–4"), "language": "de-CH", "translation_kind": "literal_original_working", "method_de": METHOD,
    "based_on_edition": "ED-SBLGNT", "based_on_tokens": "TOKSET-SBLGNT-LUK-011",
    "follows_readings": follows("LUK", 11, 1, 4),
    "text_by_reference": {R(f"Lk 11,{v}"): t for v, t in LK.items()},
    "translation_notes": [
        "11,1: Καὶ ἐγένετο «und es geschah» ist eine typisch lukanische, an die griechische Bibel angelehnte Erzählformel.",
        "11,2: Die kurze Anrede Πάτερ «Vater» ohne «unser».",
        "11,3: δίδου ist ein Imperativ der Gegenwart: «gib (immer wieder)»; τὸ καθʼ ἡμέραν «Tag für Tag». Zu ἐπιούσιος siehe Mt 6,11.",
        "11,4: Lukas sagt ἁμαρτίαι «Sünden», behält aber im zweiten Satzteil das Bild der Schuld bei (ὀφείλοντι «der schuldet»). ἀφίομεν ist eine Nebenform von ἀφίεμεν.",
    ],
    "authorship_de": AUTH, "knowledge": KN,
    "alternatives": LK_ALTS,
    "alternatives_note_de": "Deutsche Wiedergabe abweichender Lesarten, soweit sie die Übersetzung verändern. " + AUTH,
    "alternatives_origin_note_de": ORIGIN_NOTE,
})

# --- Wortzuordnungen ----------------------------------------------------------------------------
U = None
ALIGN_MT = [
    (9, [1], "So", None), (9, [2], "nun", None), (9, [3], "sollt … beten", "Imperativ Präsens"), (9, [4], "ihr", "betont"),
    (9, [5], "Vater", "Anrede (Vokativ)"), (9, [6], "Unser", None),
    (9, [7, 8, 9, 10], "in den Himmeln", "wörtlich «der in den Himmeln»; Plural"),
    (9, [11], "werde geheiligt", "Imperativ Aorist Passiv: Gott selbst ist wohl als Handelnder gedacht"),
    (9, [12, 13], "Name", None), (9, [14], "dein", None),
    (10, [1], "komme", "Imperativ Aorist"), (10, [2, 3], "Reich", "βασιλεία auch «Königsherrschaft»"), (10, [4], "dein", None),
    (10, [5], "geschehe", None), (10, [6, 7], "Wille", None), (10, [8], "dein", None), (10, [9], "wie", None),
    (10, [10, 11], "im Himmel", None), (10, [12], "so auch", "καί «auch»; «so» ergänzt"), (10, [13, 14], "auf Erden", None),
    (11, [1, 2], "Brot", None), (11, [3], "Unser", None),
    (11, [4, 5], "tägliches", "ἐπιούσιος: Bedeutung unsicher; «für den kommenden Tag» oder «zum Leben nötig» ebenso möglich"),
    (11, [6], "gib", "Imperativ Aorist: einmalig, für heute"), (11, [7], "uns", None), (11, [8], "heute", None),
    (12, [1], "Und", None), (12, [2], "vergib", None), (12, [3], "uns", None),
    (12, [4, 5], "Schulden", "wörtlich Geldschulden; im Aramäischen zugleich Sünde"), (12, [6], "unsere", None),
    (12, [7], "wie", None), (12, [8], "auch", None), (12, [9], "wir", "betont"),
    (12, [10], "vergeben haben", "Aorist; RP liest ἀφίεμεν «wir vergeben»"), (12, [11, 12], "Schuldnern", None),
    (12, [13], "unseren", None),
    (13, [1], "Und", None), (13, [2], "nicht", None), (13, [3], "führe", "wörtlich «hineintragen, hineinführen»"),
    (13, [4], "uns", None), (13, [5, 6], "in Versuchung", "auch «in Prüfung»"), (13, [7], "sondern", None),
    (13, [8], "rette", "ῥύομαι «retten, bewahren, entreissen»"), (13, [9], "uns", None),
    (13, [10, 11, 12], "vor dem Bösen", "Neutrum («das Böse») oder Maskulinum («der Böse») möglich"),
]
ALIGN_LK = [
    (2, [1], "sagte", None), (2, [2], "aber", None), (2, [3], "zu ihnen", None), (2, [4], "Wenn", None),
    (2, [5], "ihr betet", None), (2, [6], "sprecht", "Imperativ Präsens"), (2, [7], "Vater", "Anrede ohne «unser»"),
    (2, [8], "werde geheiligt", None), (2, [9, 10], "Name", None), (2, [11], "dein", None),
    (2, [12], "komme", None), (2, [13, 14], "Reich", None), (2, [15], "dein", None),
    (3, [1, 2], "Brot", None), (3, [3], "Unser", None), (3, [4, 5], "tägliches", "ἐπιούσιος wie Mt 6,11"),
    (3, [6], "gib", "Imperativ Präsens: wiederholt, immer wieder"), (3, [7], "uns", None),
    (3, [8, 9, 10], "Tag für Tag", None),
    (4, [1], "Und", None), (4, [2], "vergib", None), (4, [3], "uns", None), (4, [4, 5], "Sünden", None),
    (4, [6], "unsere", None), (4, [7], "auch", None), (4, [8], "denn", None), (4, [9], "wir selbst", None),
    (4, [10], "vergeben", "Nebenform ἀφίομεν, Gegenwart"), (4, [11], "jedem", None),
    (4, [12], "der … etwas schuldet", "Partizip: «dem, der schuldet»"), (4, [13], "uns", None),
    (4, [14], "und", None), (4, [15], "nicht", None), (4, [16], "führe", None), (4, [17], "uns", None),
    (4, [18, 19], "in Versuchung", None),
]


def alignment(id_, book, ch, rng, spec, text, trans_id, v0, v1):
    toks = [t for t in json.loads((D / f"tokens/SBLGNT-{book}-{ch:03d}.json").read_text(encoding="utf-8"))["tokens"]
            if v0 <= int(t["reference"].split(".")[2]) <= v1]
    by = {t["id"]: t for t in toks}
    seen, entries = set(), []
    for v, pos, target, note in spec:
        ids = [f"TOK-SBLGNT-{book}-{ch:03d}-{v:03d}-{p:03d}" for p in pos]
        for i in ids:
            assert i in by and i not in seen, i
            seen.add(i)
        if target:
            for part in target.split(" … "):
                assert part in text[v], (v, part)
        e = {"reference": f"{book}.{ch}.{v}", "source_tokens": ids,
             "source": " ".join(by[i]["word"] for i in ids), "target": target,
             "kind": "lexical" if len(ids) == 1 else "phrase"}
        if note:
            e["note_de"] = note
        entries.append(e)
    missing = [t["id"] for t in toks if t["id"] not in seen]
    assert not missing, missing
    w("alignments", {"id": id_, "type": "alignment", "status": "draft", "tags": [LP], "reference": R(rng),
                     "source_language": "grc", "target_language": "de-CH", "source_basis": "ED-SBLGNT",
                     "source_tokens_set": f"TOKSET-SBLGNT-{book}-{ch:03d}", "target_translation": trans_id,
                     "coverage": "complete",
                     "coverage_de": f"Jedes der {len(seen)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                     "target_convention_de": "« … » trennt nicht zusammenhängende Teile des deutschen Wortlauts.",
                     "alignments": entries, "authorship_de": AUTH, "knowledge": KN})


alignment("ALIGN-MAT-006-009-013-001", "MAT", 6, "Mt 6,9–13", ALIGN_MT, MT, "TRANS-MAT-006-005-015-DE-WORKING", 9, 13)
alignment("ALIGN-LUK-011-002-004-001", "LUK", 11, "Lk 11,2–4", ALIGN_LK, LK, "TRANS-LUK-011-001-004-DE-WORKING", 2, 4)

# --- Befunde ------------------------------------------------------------------------------------
def find(id_, subject, kind, claim, ev, conf, rationale):
    w("findings", {"id": id_, "type": "finding", "status": "draft", "tags": [LP], "subject": subject, "kind": kind,
                   "claim_de": claim, "evidence_refs": [R(x) for x in ev], "confidence": conf,
                   "confidence_rationale_de": rationale, "authorship_de": AUTH, "knowledge": KN})


find("FIND-LP-0001", "TU-MAT-006-009-013", "literary_structure",
     "Nach der Anrede folgen bei Matthäus drei Bitten mit «dein» (Name, Reich, Wille) und danach vier Bitten mit «uns» bzw. «unser» (Brot, Schulden, Versuchung, Rettung).",
     ["Mt 6,9–13"], "high", "Beobachtung am Wortlaut; die Zählung der Bitten (sechs oder sieben) wird in der Tradition unterschiedlich gehandhabt.")
find("FIND-LP-0002", "TU-LUK-011-001-004", "synoptic_comparison",
     "Lukas hat eine kürzere Fassung: Anrede nur «Vater», ohne die Bitte um Gottes Willen und ohne die Bitte um Rettung vor dem Bösen. Statt «Schulden» sagt er «Sünden», behält aber im zweiten Satzteil das Bild des Schuldners bei.",
     ["Lk 11,2–4", "Mt 6,9–13"], "high", "Vergleich der SBLGNT-Texte; in vielen späteren Handschriften ist die Lukasfassung an Matthäus angeglichen (siehe Lesarten).")
find("FIND-LP-0003", "TU-MAT-006-009-013", "lexical",
     "Das griechische Wort, das meist mit «täglich» übersetzt wird (ἐπιούσιος), kommt im Neuen Testament nur im Vaterunser vor (Mt 6,11; Lk 11,3). Origenes bemerkte im 3. Jahrhundert, es sei bei den Griechen sonst nicht gebräuchlich.",
     ["Mt 6,11", "Lk 11,3"], "high", "Origenes, Über das Gebet 27,7; spätere Funde einzelner Belege sind umstritten. Darum ist die Bedeutung unsicher.")
find("FIND-LP-0004", "TU-MAT-006-005-015", "literary_structure",
     "Von allen Bitten des Vaterunsers greift Matthäus nur die Bitte um Vergebung im Anschluss noch einmal auf (6,14–15).",
     ["Mt 6,12", "Mt 6,14–15"], "high", "Beobachtung am Wortlaut.")
find("FIND-LP-0005", "TU-MAT-006-009-013", "textual",
     "Der Lobpreis «Denn dein ist das Reich…» fehlt bei Matthäus in den ältesten erhaltenen Handschriften (Sinaiticus, Vaticanus, Bezae) und steht im Washingtonianus (4./5. Jh.) sowie in der Mehrheit der späteren Handschriften.",
     ["Mt 6,13"], "high", "Nach den importierten CNTR-Transkriptionen und der maschinellen Zuordnung (WREAD-CNTR-MAT-006-005-015); nicht am Faksimile geprüft.")
find("FIND-LP-0006", "TU-LUK-011-001-004", "textual",
     "Die kurze Lukasfassung (Anrede «Vater», ohne Willensbitte und ohne «sondern rette uns») steht in 𝔓75 und im Vaticanus; der Sinaiticus hat die kurze Anrede, aber die Willensbitte. Alexandrinus, Ephraemi, Bezae und Washingtonianus haben die längeren, an Matthäus angeglichenen Formen.",
     ["Lk 11,2", "Lk 11,4"], "high", "Nach den CNTR-Transkriptionen (WREAD-CNTR-LUK-011-001-004); maschinelle Zuordnung, nicht am Faksimile geprüft.")

# --- Deutungen ----------------------------------------------------------------------------------
def interp(id_, subject, based, claim, conf, caveat, counter, tags=None):
    w("interpretations", {"id": id_, "type": "interpretation", "status": "draft", "tags": tags or [LP],
                          "subject": subject, "based_on": based, "claim_de": claim, "confidence": conf,
                          "caveat_de": caveat, "counterarguments_de": counter, "authorship_de": AUTH, "knowledge": KN})


interp("INT-LP-0001", "TU-MAT-006-009-013", ["FIND-LP-0003"],
       "«Brot für den kommenden Tag»: Das Wort (ἐπιούσιος) wird vom griechischen Ausdruck für «der folgende Tag» (ἡ ἐπιοῦσα ἡμέρα) abgeleitet. Man bittet heute um das Brot für morgen, damit man nicht in Sorge leben muss. Hieronymus berichtet, im Hebräerevangelium stehe hier «mahar» (für morgen).",
       "possible", "Steht in Spannung zu Mt 6,34 («Sorgt nicht für morgen»), wenn man es als Vorsorge versteht.",
       ["Die Bitte «gib uns heute das Brot für morgen» kann gerade das Vertrauen ausdrücken, das 6,34 verlangt: Man legt den nächsten Tag in Gottes Hand.",
        "Die Notiz des Hieronymus bezieht sich auf ein nicht erhaltenes Evangelium und kann eine spätere Rückübersetzung sein."])
interp("INT-LP-0002", "TU-MAT-006-009-013", ["FIND-LP-0003"],
       "«Das zum Leben nötige Brot»: Das Wort (ἐπιούσιος) wird von «für» (ἐπί) und «Dasein, Lebensunterhalt» (οὐσία) abgeleitet. Man bittet um das, was man zum Leben braucht, nicht um Überfluss (vgl. Spr 30,8).",
       "possible", "Sprachlich ist diese Wortbildung ungewöhnlich; man würde eine etwas andere Form erwarten (ἐπούσιος).",
       ["Die Tradition «täglich» (lateinisch cotidianum) und das lukanische «Tag für Tag» passen gut zu dieser Bedeutung."])
interp("INT-LP-0003", "TU-MAT-006-009-013", ["FIND-LP-0003"],
       "«Das Brot der kommenden Welt»: Manche Kirchenväter verstanden das Wort geistlich, als Brot des Gottesreiches oder als Abendmahl; Hieronymus übersetzte in Matthäus mit supersubstantialem («überwesentlich»).",
       "possible", "Diese Deutung liegt weiter vom Alltagsbrot entfernt, an das die Zuhörer Jesu zuerst gedacht haben dürften.",
       ["Die Bitte um das Reich (6,10) und Jesu Mahlgemeinschaften verbinden Alltagsbrot und erwartetes Festmahl; beides muss sich nicht ausschliessen."])
interp("INT-LP-0004", "TU-MAT-006-009-013", ["FIND-LP-0001"],
       "«Führe uns nicht in Versuchung» bittet darum, nicht in eine Prüfung zu geraten, in der man den Glauben verliert. Viele denken dabei an die grosse Bedrängnis der Endzeit, andere an alltägliche Versuchungen.",
       "probable", "Ob Gott selbst als der gedacht ist, der in Versuchung führt, ist umstritten; Jak 1,13 sagt, Gott versuche niemanden.",
       ["Das Griechische ist eine Bitte an Gott und setzt voraus, dass auch Prüfungen in seiner Hand liegen (vgl. Gen 22,1). Die Bitte widerspricht Jak 1,13 nicht, wenn man «Prüfung» und «Verführung zum Bösen» unterscheidet.",
        "Einige Kirchen haben die Formulierung in jüngerer Zeit geändert (z. B. Frankreich 2017: «lass uns nicht in Versuchung eintreten»; Italien 2020: «überlass uns nicht der Versuchung»), andere, etwa die deutschsprachigen katholischen Bistümer 2018, haben sie beibehalten."])
interp("INT-LP-0005", "TU-MAT-006-005-015", ["FIND-LP-0004"],
       "Die Bitte um Vergebung ist bei Matthäus mit der eigenen Bereitschaft zu vergeben verknüpft: Wer selbst nicht vergibt, verschliesst sich der Vergebung Gottes (6,14–15; vgl. Mt 18,23–35).",
       "probable", "Ob die eigene Vergebung Bedingung oder Folge der empfangenen Vergebung ist, wird unterschiedlich gesehen.",
       ["Im Gleichnis Mt 18,23–35 geht die Vergebung des Herrn voraus; die eigene Vergebung ist Antwort darauf, nicht Leistung.",
        "Die Vergangenheitsform «wie wir vergeben haben» (6,12) kann als Ausdruck der Bereitschaft verstanden werden, nicht als Vorleistung."])
interp("INT-LP-0006", "TU-MAT-006-009-013", ["FIND-LP-0001"],
       "«Vor dem Bösen» meint den Bösen als Person (den Teufel), wie in Mt 13,19.38.",
       "possible", "Das Griechische lässt «das Böse» (Neutrum) und «der Böse» (Maskulinum) zu; die Kirchen des Ostens beten meist «vor dem Bösen» im persönlichen Sinn, viele westliche Übersetzungen neutral.",
       ["«Das Böse» im allgemeinen Sinn (Unheil, Bosheit) passt ebenso zum Zusammenhang und zu jüdischen Gebeten um Bewahrung vor Bösem."])
interp("INT-LP-0007", "TU-LUK-011-001-004", ["FIND-LP-0002"],
       "Lukas überliefert eine ältere, kürzere Form, die Matthäus für den Gebrauch in seiner Gemeinde erweitert hat.",
       "possible", "Welche Fassung näher bei Jesus liegt, ist nicht sicher zu entscheiden; vielleicht hat Jesus das Gebet in verschiedenen Formen gelehrt.",
       ["Matthäus könnte die ursprünglichere Wortwahl bewahrt haben (z. B. «Schulden» statt «Sünden»), während Lukas für nichtjüdische Leser vereinfacht.",
        "Beide Fassungen können auf unterschiedliche Gemeindetraditionen zurückgehen, ohne dass eine von der anderen abhängt."])

# --- Grundsatz, Anwendung, Fragen, Beziehungen --------------------------------------------------
w("principles", {"id": "PRIN-LP-0001", "type": "principle", "status": "draft", "tags": [LP, "TAG-CULTURAL-TRANSFER"],
                 "derived_from": ["FIND-LP-0001", "INT-LP-0005"],
                 "statement_de": "Beten nach Jesu Anleitung beginnt mit vertrauensvoller Anrede Gottes und mit Gottes Sache und bringt dann die eigenen Grundbedürfnisse vor: Brot, Vergebung und Bewahrung. Empfangene und gewährte Vergebung gehören zusammen.",
                 "confidence": "probable", "authorship_de": AUTH})
w("applications", {"id": "APP-LP-0001", "type": "application", "status": "draft", "tags": [LP, "TAG-CULTURAL-TRANSFER"],
                   "principle": "PRIN-LP-0001", "context": "CTX-CH-DE-2026",
                   "statement_de": "Wer das Vaterunser heute betet, kann es langsam beten und bei einzelnen Bitten innehalten: Wo brauche ich wirklich «Brot für heute»? Wem muss ich noch vergeben? In einem Land mit Überfluss kann die Brotbitte auch an die erinnern, denen das Nötige fehlt, denn sie heisst «unser» Brot, nicht «mein» Brot.",
                   "limitations_de": "Das ist eine heutige Übertragung, kein Befund am Text. Das Vaterunser wurde in seiner Zeit von Menschen gebetet, für die das tägliche Brot oft unsicher war; das lässt sich nicht einfach auf heutige Lebensverhältnisse übertragen.",
                   "confidence": "possible", "authorship_de": AUTH})
w("questions", {"id": "QUESTION-LP-0001", "type": "open_question", "status": "draft", "tags": [LP, "TAG-UNCERTAINTY"],
                "subject": "TU-MAT-006-009-013",
                "question_de": "Was bedeutet ἐπιούσιος genau: «täglich», «für den kommenden Tag», «zum Leben nötig» oder etwas anderes?",
                "finding_de": "Das Wort ist ausserhalb des Vaterunsers praktisch nicht belegt; die Deutungen stützen sich auf Wortbildung, alte Übersetzungen und frühe Ausleger.",
                "status_of_answer": "open", "knowledge": KN})
w("questions", {"id": "QUESTION-LP-0002", "type": "open_question", "status": "draft", "tags": [LP, "TAG-UNCERTAINTY"],
                "subject": "TU-LUK-011-001-004",
                "question_de": "Welche Fassung des Vaterunsers steht Jesus näher, und wurde es ursprünglich auf Aramäisch gebetet?",
                "finding_de": "Beide Fassungen sind nur griechisch überliefert. Rückübersetzungen ins Aramäische sind Rekonstruktionen.",
                "status_of_answer": "open", "knowledge": KN})
for id_, frm, to, rel, conf in [
    ("REL-LP-0001", "TU-MAT-006-009-013", "Lk 11,2–4", "parallel_passage", "high"),
    ("REL-LP-0002", "TU-MAT-006-014-015", "Mk 11,25", "parallel_saying", "high"),
    ("REL-LP-0003", "TU-MAT-006-009-013", "Mk 14,36", "related_prayer", "probable"),
    ("REL-LP-0004", "TU-MAT-006-009-013", "Mt 26,41", "related_saying", "probable"),
    ("REL-LP-0005", "TU-MAT-006-014-015", "Mt 18,21–35", "thematic", "probable"),
    ("REL-LP-0006", "TU-MAT-006-009-013", "1 Chr 29,11", "background", "possible"),
    ("REL-LP-0007", "TU-MAT-006-009-013", "Ex 16,4", "background", "possible"),
]:
    w("relations", {"id": id_, "type": "relation", "status": "draft", "tags": [LP], "from": frm, "to_ref": R(to),
                    "relation": rel, "confidence": conf})

# --- Hintergrund damals --------------------------------------------------------------------------
G = "CTX-GALILEE-0030"
BG = [
    ("BG-LP-0001", "Zwei Fassungen, zwei Leserkreise", "TU-MAT-006-005-015", "CTX-MAT-READERS-0085", "Mt 6,9–13", "probable",
     "Matthäus stellt das Vaterunser in die Bergpredigt, zwischen Anweisungen zu Almosen, Beten und Fasten (6,1–18), wie sie für jüdische Frömmigkeit typisch waren. Lukas erzählt, dass ein Jünger Jesus darum bittet, wie Johannes der Täufer seine Jünger beten lehrte. Beide schrieben Jahrzehnte nach Jesus für verschiedene Gemeinden, die das Gebet wohl schon regelmässig beteten.",
     "Ob Jesus das Gebet bei einer oder mehreren Gelegenheiten lehrte, ist offen.", ["Mt 6,1–18", "Lk 11,1"], []),
    ("BG-LP-0002", "Beten im Judentum damals", "TU-MAT-006-005-015", G, "Mt 6,5", "probable",
     "Fromme Juden beteten zu festen Zeiten, oft dreimal am Tag (vgl. Dan 6,11; Ps 55,18), dazu das Schma Israel. Wer zur Gebetszeit unterwegs war, betete dort, wo er gerade stand. Jesus kritisiert nicht das Beten in der Öffentlichkeit an sich, sondern das Beten, um gesehen zu werden.",
     "Wie fest die Gebetszeiten und Gebetstexte zur Zeit Jesu schon geregelt waren, ist in der Forschung umstritten.", ["Dan 6,11", "Ps 55,18", "Dtn 6,4–9"], []),
    ("BG-LP-0003", "Heuchler, Kammer, Heiden", "TU-MAT-006-005-008", G, "Mt 6,5–7", "probable",
     "Das griechische Wort für Heuchler bezeichnete ursprünglich Schauspieler auf der Bühne. Die «Kammer» war ein Vorrats- oder Innenraum, in einfachen Häusern oft der einzige Raum ohne Fenster und mit Tür. In heidnischen Gebeten wurden die Gottheiten mit vielen Namen und Beinamen angerufen, damit man die richtige Anrede traf und erhört wurde (vgl. 1 Kön 18,26).",
     None, ["1 Kön 18,26"], []),
    ("BG-LP-0004", "Gott als Vater anreden", "TU-MAT-006-009-013", G, "Mt 6,9", "probable",
     "Auch die hebräische Bibel und jüdische Gebete nennen Gott Vater (Jes 63,16; 64,7; Sir 23,1). Dass Jesus Gott ganz direkt mit «Vater» anredet, auf Aramäisch «Abba» (Mk 14,36), und seine Jünger dazu anleitet, wird oft als besonders vertraut beschrieben. Das frühe Christentum hat das aramäische Wort sogar in griechischen Briefen bewahrt (Röm 8,15; Gal 4,6).",
     "Die verbreitete Erklärung, «Abba» sei die Kindersprache «Papa», gilt heute als überzogen; das Wort wurde auch von Erwachsenen gegenüber ihrem Vater gebraucht.", ["Jes 63,16", "Mk 14,36", "Röm 8,15", "Gal 4,6"], []),
    ("BG-LP-0005", "Den Namen heiligen", "TU-MAT-006-009-013", G, "Mt 6,9–10", "probable",
     "Der «Name» steht in der Bibel für die Person selbst. Nach Ez 36,23 heiligt Gott seinen Namen, indem er an seinem Volk handelt. Ein jüdisches Gebet, das Kaddisch, beginnt ähnlich: «Erhoben und geheiligt werde sein grosser Name … er lasse sein Reich kommen.»",
     "Das Kaddisch ist in seiner heutigen Form deutlich später belegt; wie alt seine Kernsätze sind, ist umstritten.", ["Ez 36,23"], []),
    ("BG-LP-0006", "Das Reich Gottes", "TU-MAT-006-009-013", G, "Mt 6,10", "high",
     "Viele Juden erwarteten, dass Gott seine Herrschaft sichtbar aufrichtet und Unrecht und fremde Herrschaft beendet (vgl. Dan 2,44). Im Galiläa unter römischer Oberherrschaft war das auch politisch brisant. «Reich Gottes» ist das zentrale Thema der Verkündigung Jesu (Mk 1,15).",
     None, ["Dan 2,44", "Mk 1,15"], []),
    ("BG-LP-0007", "Brot für den Tag", "TU-MAT-006-009-013", G, "Mt 6,11", "probable",
     "Viele Menschen lebten von der Hand in den Mund: Tagelöhner erhielten ihren Lohn am Abend und kauften davon das Essen für den nächsten Tag (vgl. Mt 20,1–16; Dtn 24,15). In der Wüste erhielt Israel das Manna Tag für Tag und durfte keinen Vorrat anlegen (Ex 16,4.19–20).",
     "Was das griechische Wort für «täglich» genau bedeutet, ist unsicher (siehe Deutungen).", ["Mt 20,1–16", "Dtn 24,15", "Ex 16,4"],
     ["Origenes, Über das Gebet 27,7", "Hieronymus, Kommentar zu Matthäus, zu 6,11"]),
    ("BG-LP-0008", "Schulden und Sünden", "TU-MAT-006-009-013", G, "Mt 6,12", "probable",
     "Im Aramäischen, das Jesus sprach, bezeichnet dasselbe Wort (ḥôbā) eine Geldschuld und eine Sünde. Verschuldung war in Galiläa verbreitet und konnte bis zur Schuldknechtschaft führen. Das Gesetz kannte einen Schuldenerlass in jedem siebten Jahr (Dtn 15,1–2). Matthäus behält das Bild der Schulden, Lukas sagt «Sünden», spricht aber im selben Vers vom Schuldner.",
     None, ["Dtn 15,1–2", "Mt 18,23–35", "Lk 11,4"], []),
    ("BG-LP-0009", "Versuchung und Prüfung", "TU-MAT-006-009-013", G, "Mt 6,13", "probable",
     "Das griechische Wort meint beides: Versuchung zum Bösen und Prüfung der Treue. Die Bibel erzählt von Prüfungen, etwa Abrahams (Gen 22,1) oder Israels in der Wüste (Dtn 8,2). Viele Juden erwarteten vor dem Kommen des Reiches eine Zeit grosser Bedrängnis.",
     None, ["Gen 22,1", "Dtn 8,2", "Jak 1,13", "Mt 26,41"], []),
    ("BG-LP-0010", "Der Lobpreis am Schluss", "TU-MAT-006-009-013", "CTX-MAT-READERS-0085", "Mt 6,13", "high",
     "Jüdische Gebete endeten oft mit einem Lobpreis Gottes; ein Vorbild ist das Gebet Davids in 1 Chr 29,11. Die Didache, eine frühchristliche Gemeindeordnung aus der Zeit um 100, gibt das Vaterunser fast wie Matthäus wieder, mit dem Schluss «denn dein ist die Kraft und die Herrlichkeit in Ewigkeit», und rät, es dreimal täglich zu beten.",
     "Die Datierung der Didache ist umstritten (meist um 100).", ["1 Chr 29,11"], ["Didache 8,2–3"]),
    ("BG-LP-0011", "Vaterunser auf Amuletten", "TU-MAT-006-009-013", "CTX-MAT-READERS-0085", "Mt 6,9–13", "high",
     "Aus dem 3. bis 6. Jahrhundert sind mehrere kleine Papyrusblätter und eine Tonscherbe mit dem Vaterunser erhalten, oft als Schutz-Amulett getragen. Sie zeigen, wie verbreitet das Gebet war, und dass einfache Leute es nach Gehör aufschrieben, mit vielen Schreibvarianten.",
     "Die Einordnung als Amulett beruht auf Format und Fundzusammenhang; nicht jedes Stück ist sicher eines.", ["Mt 6,9–13"],
     ["P. Antinoopolis 2.54", "P. Oxyrhynchus 60.4010", "Vaterunser auf Ton aus Megara (Athen, Nationalmuseum)"]),
    ("BG-LP-0012", "Johannes und seine Jünger", "TU-LUK-011-001-004", G, "Lk 11,1", "probable",
     "Lehrer und ihre Schülerkreise hatten eigene Gebete; auch von den Jüngern Johannes des Täufers wird erzählt, dass sie fasteten und beteten (Lk 5,33). Ein eigenes Gebet gab einer Gruppe Zusammenhalt und Erkennungszeichen.",
     None, ["Lk 5,33", "Lk 11,1"], []),
]
for id_, topic, subj, ctx, ref, conf, text, unc, ev, src in BG:
    rec = {"id": id_, "type": "background_note", "status": "draft", "tags": [LP, "TAG-HISTORICAL-BACKGROUND"],
           "subject": subj, "context": ctx, "reference": R(ref), "topic_de": topic, "text_de": text, "confidence": conf}
    if unc:
        rec["uncertain_de"] = unc
    rec["evidence_refs"] = [R(x) for x in ev]
    if src:
        rec["sources_de"] = src
    rec.update({"authorship_de": AUTH, "knowledge": KN})
    w("background", rec)

# --- Kapitelzusammenfassungen -------------------------------------------------------------------
for id_, ref, text in [
    ("SUM-CH-MAT-006", "MAT.6", "Jesus spricht über Almosen, Beten und Fasten: nicht vor Menschen, sondern vor Gott. In der Mitte steht das Vaterunser. Danach geht es um Schätze im Himmel und darum, sich nicht zu sorgen, sondern zuerst Gottes Reich zu suchen."),
    ("SUM-CH-LUK-011", "LUK.11", "Jesus lehrt beten: das Vaterunser, ein Gleichnis vom bittenden Freund und die Zusage, dass Gott den Heiligen Geist gibt. Es folgen Streitgespräche über seine Vollmacht und scharfe Worte an Pharisäer und Gesetzeslehrer."),
]:
    w("summaries", {"id": id_, "type": "summary", "status": "draft", "tags": [LP], "scope": "chapter", "reference": ref,
                    "language": "de", "text_de": text, "authorship_de": AUTH, "knowledge": KN})

# --- Studie -------------------------------------------------------------------------------------
outputs = [x for x in written if not x.startswith(("WORK-", "CTX-"))]
w("studies", {"id": "STUDY-LP-0001", "type": "study", "status": "draft", "tags": [LP, "TAG-MATTHEW", "TAG-LUKE"],
              "title": "Das Vaterunser (Mt 6,5–15; Lk 11,1–4)", "primary_unit": "TU-MAT-006-009-013",
              "outputs": outputs + ["WREAD-CNTR-MAT-006-005-015", "WREAD-CNTR-LUK-011-001-004"],
              "authorship_de": AUTH, "knowledge": KN})
print(f"PASS: {len(written)} Datensätze geschrieben")
