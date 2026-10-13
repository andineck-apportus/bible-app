"""Autorenwerkzeug: Züridüütsch-Fassung (Mundart) für die ausgearbeiteten Stellen, übersetzt aus dem Griechischen.

Aufruf: python3 scripts/authoring/zueridueuetsch.py

Erzeugt die Übersetzungen TRANS-…-GSW-ZH-WORKING für Mt 6,5–15, Lk 11,1–4 und Mk 3,20–35 (eine Datei je
Abschnitt), die Wortzuordnungen für Mt 6,9–13 und Lk 11,2–4 sowie den Zielkontext CTX-CH-ZH-GSW-2026.
Grundlage ist der SBLGNT-Text (Token-Sets); die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle.
Schreibweise: Dieth-Schreibung (lautnah). Register: nah am Urtext, aber wie man es sagt; Entscheidungen sind
in `decisions` markiert. KI-Entwurf (Claude) vom 2026-10-13; Prüfung der Mundart durch eine muttersprachliche
Person ist vorgesehen und noch nicht erfolgt.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

D = ROOT / "data"
DATE = "2026-10-13"
LANG = "gsw-u-sd-chzh"
AUTH = f"KI-Entwurf (Claude) vom {DATE} auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt."
KN = {"asserted_at": DATE, "supersedes": None}
R = refs.canonical
written = []


def w(folder, rec):
    p = D / folder / f"{rec['id']}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    written.append(rec["id"])


w("contexts", {"id": "CTX-CH-ZH-GSW-2026", "type": "context", "status": "draft", "tags": ["TAG-CULTURAL-TRANSFER"],
               "period": {"from": 2026}, "country": "CH", "region": "Zürich", "language_context": [LANG],
               "audience": "Züridüütsch sprechende Leserinnen und Leser heute",
               "note_de": "Zielkontext der Mundart-Schicht: Zürichdeutsch als gesprochene Alltagssprache; Bibeltext in Mundart ist ungewohnt und wirkt direkter als Hochdeutsch."})

COMMON = {
    "type": "translation", "status": "draft", "language": LANG, "language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch",
    "translation_kind": "literal_original_working", "target_context": "CTX-CH-ZH-GSW-2026",
    "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
    "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
    "method_de": "Direkt aus dem SBLGNT übersetzt, mit Wortzuordnung zu den Token; die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle. Nicht aus einer veröffentlichten Mundart-Bibel übernommen.",
    "based_on_edition": "ED-SBLGNT",
    "authorship_de": AUTH, "knowledge": KN,
    "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen.",
}
DEC_NOTE = "Übersetzungsentscheidungen: wörtlich (literal), sprachlich angepasst (adapted), Deutungsentscheidung (interpretive) oder der vertrauten Wiedergabe folgend (traditional). " + AUTH
ALT_NOTE = "Mundart-Wiedergabe abweichender Lesarten, soweit sie die Übersetzung verändern; Wortbedeutungen und Entstehungserklärungen stehen bei der hochdeutschen Fassung. " + AUTH


def follows(book, ch, v0, v1):
    return sorted(f"{p.stem}:R1" for p in (D / f"variants/sblgntapp-{book.lower()}").glob(f"VAR-SBLGNTAPP-{book}-{ch:03d}-*.json")
                  if v0 <= int(p.stem.split("-")[-2]) <= v1)


def dec(ref, target, kind, grc, literal=None, note=None, others=None):
    d = {"reference": R(ref), "target": target, "kind": kind, "grc": grc}
    if literal:
        d["more_literal_de"] = literal
    if others:
        d["other_options_de"] = others
    if note:
        d["note_de"] = note
    return d


def alt(var, rid, ref, frm, to, effect, note):
    return {"reading": f"{var}:{rid}", "reference": R(ref), "de_from": frm, "de_to": to, "effect": effect, "note_de": note}


# ---------------------------------------------------------------- Matthäus 6,5–15
MT = {
    5: "Und wänn ir bätted, söled ir nöd sii wie d Hüüchler; die stönd nämli gärn i de Synagoge und a de Egge vo de breite Straasse zum bätte, dass d Lüüt si gseend. Amen, ich säg s eu: Si händ ire Loon scho übercho.",
    6: "Du aber, wänn du bätisch, gang i dini Chammer, mach d Tür zue und bätt zu diim Vatter, wo im Verborgne isch; und diin Vatter, wo is Verborgne gseet, wird s dir vergälte.",
    7: "Wänn ir bätted, söled ir nöd plappere wie d Heide; die meined nämli, si wärded erhört, wänn si vil Wort mached.",
    8: "Mached s also nöd wie sii; eue Vatter weiss nämli, was ir bruuched, bevor ir en drum bitted.",
    9: "Eso söled ir also bätte: Öise Vatter i de Himel, diin Name söll gheiliget wärde,",
    10: "diis Riich söll choo, diin Wile söll gschee, wie im Himel, eso au uf de Ärde.",
    11: "Öises täglich Broot gib üs hüt.",
    12: "Und vergib üs öisi Schulde, wie au mir öisne Schuldner vergää händ.",
    13: "Und füer üs nöd i d Versuechig, sondern rett üs vor em Bööse.",
    14: "Wänn ir nämli de Lüüt iri Fääler vergänd, wird eu eue himmlisch Vatter au vergää;",
    15: "wänn ir aber de Lüüt nöd vergänd, wird au eue Vatter eui Fääler nöd vergää.",
}
MT_DEC = [
    dec("Mt 6,5", "Hüüchler", "literal", "ὑποκριταί", note="ὑποκριτής hiess ursprünglich «Schauspieler»."),
    dec("Mt 6,5", "Si händ ire Loon scho übercho", "literal", "ἀπέχουσι τὸν μισθὸν αὐτῶν", note="ἀπέχω ist das Wort der Quittung: «vollständig erhalten haben»."),
    dec("Mt 6,6", "Chammer", "literal", "ταμεῖόν", note="Vorrats- oder Innenraum; in Mundart ist «Chammer» das vertraute Wort."),
    dec("Mt 6,7", "plappere", "interpretive", "βατταλογήσητε", others=["schnädere", "vil läär Wort mache"], note="βατταλογέω ist sonst kaum belegt; «plappere» ist die übliche Deutung."),
    dec("Mt 6,8", "Mached s also nöd wie sii", "adapted", "μὴ οὖν ὁμοιωθῆτε αὐτοῖς", literal="Wärded ine also nöd gliich", note="«sich gleich machen» ist in Mundart unüblich; umschrieben."),
    dec("Mt 6,9", "Öise Vatter", "literal", "Πάτερ ἡμῶν", literal="Vatter öise", note="Im Griechischen steht «Vater» zuerst; in Mundart steht das Possessiv voran."),
    dec("Mt 6,9", "i de Himel", "literal", "ὁ ἐν τοῖς οὐρανοῖς", note="Mehrzahl wie im Griechischen; «i de Himel» ist in Mundart Dativ Plural und zugleich natürlich."),
    dec("Mt 6,9", "söll gheiliget wärde", "literal", "ἁγιασθήτω", note="Passiv-Imperativ; Mundart kennt keinen Imperativ der 3. Person, darum «söll … wärde»."),
    dec("Mt 6,11", "täglich", "traditional", "τὸν ἐπιούσιον", literal="für de nööchscht Taag", others=["für de nööchscht Taag", "wo mer zum Läbe bruuched"], note="Das Wort ist unsicher; «täglich» folgt der vertrauten Tradition. Siehe Deutungen bei der hochdeutschen Fassung."),
    dec("Mt 6,12", "Schulde", "literal", "τὰ ὀφειλήματα", note="Wörtlich Geldschulden; aramäisch zugleich Sünde."),
    dec("Mt 6,12", "vergää händ", "literal", "ἀφήκαμεν", note="Aorist; Mundart hat nur Perfekt."),
    dec("Mt 6,13", "füer üs nöd i d Versuechig", "traditional", "μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν", literal="bring üs nöd ine i d Versuechig", others=["lass üs nöd i d Versuechig ine choo (Deutung nach aramäischem Hintergrund)"], note="Wörtlich nah und zugleich die vertraute Formel."),
    dec("Mt 6,13", "Versuechig", "interpretive", "πειρασμόν", others=["Prüefig"], note="πειρασμός heisst «Versuchung» und «Prüfung»."),
    dec("Mt 6,13", "rett", "literal", "ῥῦσαι", others=["erlös", "bewaar"], note="ῥῦσαι «rette, entreisse»."),
    dec("Mt 6,13", "vor em Bööse", "interpretive", "ἀπὸ τοῦ πονηροῦ", others=["vor em Bööse (Person)", "vor em Übel"], note="Neutrum oder Maskulinum möglich."),
    dec("Mt 6,14", "Fääler", "adapted", "τὰ παραπτώματα", literal="Verfäälige", note="παράπτωμα «Fehltritt, Verfehlung»; «Fääler» ist das gebräuchliche Mundartwort, etwas schwächer als das Griechische."),
]
MT_ALTS = [
    alt("VAR-SBLGNTAPP-MAT-006-005-01", "R2", "Mt 6,5", "wänn ir bätted, söled ir nöd sii wie", "wänn du bätisch, sollsch du nöd sii wie", "gering", "Einzahl statt Mehrzahl, wie in 6,6."),
    alt("VAR-SBLGNTAPP-MAT-006-006-01", "R2", "Mt 6,6", "wird s dir vergälte", "wird s dir öffentlich vergälte", "bedeutsam", "Mit dem Zusatz steht dem verborgenen Beten ein öffentlicher Lohn gegenüber."),
    alt("VAR-SBLGNTAPP-MAT-006-008-01", "R2", "Mt 6,8", "eue Vatter weiss nämli", "Gott, eue Vatter, weiss nämli", "gering", "Westcott-Hort folgen einer Lesart mit «Gott»."),
    alt("VAR-SBLGNTAPP-MAT-006-012-01", "R2", "Mt 6,12", "wie au mir öisne Schuldner vergää händ", "wie au mir öisne Schuldner vergänd", "bedeutsam", "Vergangenheit oder Gegenwart."),
    alt("VAR-SBLGNTAPP-MAT-006-013-01", "R2", "Mt 6,13", "rett üs vor em Bööse", "rett üs vor em Bööse. Dänn diin isch s Riich und d Chraft und d Herrlichkeit i Ewigkeit. Amen", "bedeutsam", "Der vertraute Lobpreis fehlt in den ältesten Handschriften."),
    alt("VAR-SBLGNTAPP-MAT-006-015-01", "R2", "Mt 6,15", "de Lüüt nöd vergänd", "de Lüüt iri Fääler nöd vergänd", "gering", "Der Zusatz wiederholt 6,14."),
]
w("translations", {"id": "TRANS-MAT-006-005-015-GSW-ZH-WORKING", **COMMON, "tags": ["TAG-MATTHEW", "TAG-LORDS-PRAYER"],
                   "reference": R("Mt 6,5–15"), "based_on_tokens": "TOKSET-SBLGNT-MAT-006", "follows_readings": follows("MAT", 6, 5, 15),
                   "control_translation": "TRANS-MAT-006-005-015-DE-WORKING",
                   "text_by_reference": {R(f"Mt 6,{v}"): t for v, t in MT.items()},
                   "translation_notes": [
                       "6,5: «die stönd … gärn … zum bätte» für φιλοῦσιν … ἑστῶτες προσεύχεσθαι (sie lieben es, stehend zu beten).",
                       "6,5: «ich säg s eu» für ἀμὴν λέγω ὑμῖν; «Amen» bleibt stehen.",
                       "6,9: Mundart kennt keinen Imperativ der 3. Person; darum «söll … wärde», «söll choo», «söll gschee».",
                       "6,12: «vergää händ» gibt den Aorist wieder; Mundart hat kein Präteritum.",
                   ],
                   "decisions": MT_DEC, "decisions_note_de": DEC_NOTE, "alternatives": MT_ALTS, "alternatives_note_de": ALT_NOTE})

# ---------------------------------------------------------------- Lukas 11,1–4
LK = {
    1: "Und es isch gsii, won er amene Ort am Bätte gsii isch: Won er ufghört hät, hät eine vo sine Jünger zu ihm gseit: Herr, leer üs bätte, wie au de Johannes sini Jünger gleert hät.",
    2: "Er hät zu ine gseit: Wänn ir bätted, säged: Vatter, diin Name söll gheiliget wärde, diis Riich söll choo.",
    3: "Öises täglich Broot gib üs Taag für Taag.",
    4: "Und vergib üs öisi Sünde, dänn au mir sälber vergänd jedem, wo üs öppis schuldig isch; und füer üs nöd i d Versuechig.",
}
LK_DEC = [
    dec("Lk 11,1", "Und es isch gsii", "literal", "Καὶ ἐγένετο", note="Lukanische Erzählformel; in Mundart ungewohnt, aber möglich."),
    dec("Lk 11,2", "Vatter", "literal", "Πάτερ", note="Kurze Anrede ohne «öise», wie in den ältesten Handschriften."),
    dec("Lk 11,3", "täglich", "traditional", "τὸν ἐπιούσιον", literal="für de nööchscht Taag", others=["für de nööchscht Taag", "wo mer zum Läbe bruuched"], note="Wie Mt 6,11."),
    dec("Lk 11,3", "Taag für Taag", "literal", "τὸ καθʼ ἡμέραν"),
    dec("Lk 11,4", "wo üs öppis schuldig isch", "adapted", "ὀφείλοντι ἡμῖν", literal="wo üs schuldet", note="«öppis» ist ergänzt."),
    dec("Lk 11,4", "füer üs nöd i d Versuechig", "traditional", "μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν", literal="bring üs nöd ine i d Versuechig", note="Wie Mt 6,13."),
]
LK_ALTS = [
    alt("VAR-SBLGNTAPP-LUK-011-002-01", "R2", "Lk 11,2", "Vatter, diin Name", "Öise Vatter im Himel, diin Name", "bedeutsam", "Die längere Anrede entspricht Matthäus."),
    alt("VAR-SBLGNTAPP-LUK-011-002-02", "R2", "Lk 11,2", "diis Riich söll choo", "diis Riich söll choo; diin Wile söll gschee, wie im Himel, eso uf de Ärde", "bedeutsam", "Die Bitte um Gottes Willen steht in vielen Handschriften auch bei Lukas."),
    alt("VAR-SBLGNTAPP-LUK-011-004-01", "R2", "Lk 11,4", "füer üs nöd i d Versuechig", "füer üs nöd i d Versuechig, sondern rett üs vor em Bööse", "bedeutsam", "Die letzte Bitte der Matthäusfassung."),
]
w("translations", {"id": "TRANS-LUK-011-001-004-GSW-ZH-WORKING", **COMMON, "tags": ["TAG-LUKE", "TAG-LORDS-PRAYER"],
                   "reference": R("Lk 11,1–4"), "based_on_tokens": "TOKSET-SBLGNT-LUK-011", "follows_readings": follows("LUK", 11, 1, 4),
                   "control_translation": "TRANS-LUK-011-001-004-DE-WORKING",
                   "text_by_reference": {R(f"Lk 11,{v}"): t for v, t in LK.items()},
                   "translation_notes": ["11,1: «won er» mit Hiatus-n nach Dieth.", "11,4: ἀφίομεν «vergänd» (Gegenwart)."],
                   "decisions": LK_DEC, "decisions_note_de": DEC_NOTE, "alternatives": LK_ALTS, "alternatives_note_de": ALT_NOTE})

# ---------------------------------------------------------------- Markus 3,20–35
MK = {
    20: "Und er chunnt i es Huus; und wider chunnt d Mängi zäme, so dass si nöd emal händ chöne Broot ässe.",
    21: "Und wo das sini Lüüt ghört händ, sind si usegange, zum en feschthebe; si händ nämli gseit: «Er isch nüme bi Troscht.»",
    22: "Und d Schriftgleerte, wo vo Jerusalem abe choo sind, händ gseit: «Er hät de Beelzebul», und: «Dur de Herrscher vo de Dämone tribt er d Dämone us.»",
    23: "Und er hät si zu sich grüeft und i Gliichnis zu ine gseit: «Wie cha de Satan de Satan ustriibe?",
    24: "Und wänn es Riich gäge sich sälber gspalte isch, cha das Riich nöd bestaa.",
    25: "Und wänn es Huus gäge sich sälber gspalte isch, wird das Huus nöd chöne bestaa.",
    26: "Und wänn de Satan gäge sich sälber ufgstande isch und gspalte worde isch, cha er nöd bestaa, sondern hät es Änd.",
    27: "Aber niemert cha is Huus vom Starche ine gaa und sin Huusraat plündere, wänn er nöd zerscht de Starch bindt; und dänn wird er sis Huus plündere.",
    28: "Amen, ich säg s eu: Alles wird de Söhn vo de Mänsche vergää, d Sünde und d Läschterige, so vil si au läschtered.",
    29: "Wär aber gäge de Heilig Geischt läschteret, hät i Ewigkeit kei Vergäbig, sondern isch schuldig a nere ewige Sünd.»",
    30: "Si händ nämli gseit: «Er hät en unreine Geischt.»",
    31: "Und sini Mueter und sini Brüeder chömed, und wo si dusse gstande sind, händ si zu ihm gschickt und en la rüefe.",
    32: "Und e Mängi isch um en ume gsässe, und si säged zu ihm: «Lueg, dini Mueter und dini Brüeder sind dusse und sueched dich.»",
    33: "Und er git ine zur Antwort: «Wär isch mini Mueter, und wär sind mini Brüeder?»",
    34: "Und er luegt die aa, wo im Chreis um en ume sitzed, und seit: «Lueg, mini Mueter und mini Brüeder!",
    35: "Dänn wär de Wile vo Gott tuet, dä isch min Brueder und mini Schwöschter und mini Mueter.»",
}
MK_DEC = [
    dec("Mk 3,20", "d Mängi", "literal", "ὄχλος", others=["d Lüüt"], note="ὄχλος «Volksmenge»."),
    dec("Mk 3,21", "sini Lüüt", "interpretive", "οἱ παρʼ αὐτοῦ", literal="die vo ihm", others=["sini Aaghörige", "sini Familie"], note="Wörtlich «die von ihm her»; meist die Angehörigen, möglich auch weiter «seine Leute»."),
    dec("Mk 3,21", "zum en feschthebe", "literal", "κρατῆσαι αὐτόν", others=["zum en hole"], note="κρατέω «ergreifen, festhalten»."),
    dec("Mk 3,21", "Er isch nüme bi Troscht", "adapted", "ἐξέστη", literal="Er isch usser sich", others=["Er isch vo Sinne", "Er spinnt"], note="ἐξίστημι «ausser sich sein»; die Mundart-Wendung trifft den Sinn, ist aber freier als das Hochdeutsche."),
    dec("Mk 3,22", "de Herrscher vo de Dämone", "literal", "τῷ ἄρχοντι τῶν δαιμονίων", others=["de Oberscht vo de Dämone", "de Fürscht vo de Dämone"]),
    dec("Mk 3,23", "i Gliichnis", "literal", "ἐν παραβολαῖς", others=["i Bilder"], note="παραβολή auch «Bildwort, Rätselwort»."),
    dec("Mk 3,25", "wird das Huus nöd chöne bestaa", "literal", "οὐ δυνήσεται ἡ οἰκία ἐκείνη σταθῆναι", note="Futur wie im SBLGNT."),
    dec("Mk 3,26", "gspalte worde isch", "literal", "ἐμερίσθη", note="Aorist als Ereignis."),
    dec("Mk 3,28", "de Söhn vo de Mänsche", "literal", "τοῖς υἱοῖς τῶν ἀνθρώπων", others=["de Mänsche"], note="Hebraisierende Wendung für «die Menschen»; wörtlich belassen."),
    dec("Mk 3,29", "hät i Ewigkeit kei Vergäbig", "literal", "οὐκ ἔχει ἄφεσιν εἰς τὸν αἰῶνα", others=["hät nie Vergäbig"]),
    dec("Mk 3,29", "isch schuldig a nere ewige Sünd", "literal", "ἔνοχός ἐστιν αἰωνίου ἁμαρτήματος", note="ἁμάρτημα «Verfehlung, Sünde»; RP liest κρίσεως «Gericht»."),
    dec("Mk 3,31", "en la rüefe", "literal", "καλοῦντες αὐτόν", note="Partizip «ihn rufend» als «ihn rufen lassen»."),
    dec("Mk 3,33", "git ine zur Antwort", "adapted", "ἀποκριθεὶς αὐτοῖς λέγει", literal="antwortet ine und seit", note="Partizip und Verb zusammengezogen."),
    dec("Mk 3,35", "de Wile vo Gott", "literal", "τὸ θέλημα τοῦ θεοῦ", note="Mundart hat keinen Genitiv: «vo Gott»."),
]
MK_ALTS = [
    alt("VAR-SBLGNTAPP-MRK-003-020-01", "R2", "Mk 3,20", "Und er chunnt i es Huus", "Und si chömed i es Huus", "bedeutsam", "Jesus allein oder mit seinen Jüngern."),
    alt("VAR-SBLGNTAPP-MRK-003-025-01", "R2", "Mk 3,25", "wird das Huus nöd chöne bestaa", "cha das Huus nöd bestaa", "gering", "Nur die Zeitform ändert sich."),
    alt("VAR-SBLGNTAPP-MRK-003-026-01", "R2", "Mk 3,26", "gspalte worde isch", "gspalte isch", "gering", "Ereignis oder Zustand."),
    alt("VAR-SBLGNTAPP-MRK-003-029-01", "R2", "Mk 3,29", "schuldig a nere ewige Sünd", "em ewige Gricht verfalle", "bedeutsam", "Bleibende Schuld oder Urteil Gottes."),
    alt("VAR-MRK-003-029-002", "R2", "Mk 3,29", "isch schuldig a nere ewige Sünd", "wird schuldig sii a nere ewige Sünd", "gering", "Gegenwart oder Zukunft; berichtete Handschriften, ungeprüft."),
    alt("VAR-SBLGNTAPP-MRK-003-032-03", "R2", "Mk 3,32", "dini Mueter und dini Brüeder sind dusse", "dini Mueter und dini Brüeder und dini Schwöschtere sind dusse", "bedeutsam", "Einige Ausgaben nennen auch die Schwestern."),
]
w("translations", {"id": "TRANS-MRK-003-020-035-GSW-ZH-WORKING", **COMMON, "tags": ["TAG-MARK"],
                   "reference": R("Mk 3,20–35"), "based_on_tokens": "TOKSET-SBLGNT-MRK-003",
                   "follows_readings": follows("MRK", 3, 20, 35) + ["VAR-MRK-003-029-001:R1", "VAR-MRK-003-029-002:R1"],
                   "control_translation": "TRANS-MRK-003-022-030-DE-WORKING",
                   "text_by_reference": {R(f"Mk 3,{v}"): t for v, t in MK.items()},
                   "translation_notes": ["Historisches Präsens (3,20.31.32.33.34) bleibt Präsens; sonst Perfekt statt Aorist/Imperfekt.",
                                         "Wortzuordnung für Markus folgt später; für das Vaterunser liegt sie vor."],
                   "decisions": MK_DEC, "decisions_note_de": DEC_NOTE, "alternatives": MK_ALTS, "alternatives_note_de": ALT_NOTE})

# ---------------------------------------------------------------- Wortzuordnung (Vaterunser)
U = None
ALIGN_MT = [
    (9, [1], "Eso", None), (9, [2], "also", None), (9, [3], "söled … bätte", "Imperativ Präsens"), (9, [4], "ir", "betont"),
    (9, [5], "Vatter", "Anrede"), (9, [6], "Öise", None), (9, [7, 8, 9, 10], "i de Himel", "wörtlich «der in den Himmeln»"),
    (9, [11], "söll gheiliget wärde", "Imperativ Aorist Passiv"), (9, [12, 13], "Name", None), (9, [14], "diin", None),
    (10, [1], "söll choo", None), (10, [2, 3], "Riich", None), (10, [4], "diis", None), (10, [5], "söll gschee", None),
    (10, [6, 7], "Wile", None), (10, [8], "diin", None), (10, [9], "wie", None), (10, [10, 11], "im Himel", None),
    (10, [12], "eso au", "καί «auch»; «eso» ergänzt"), (10, [13, 14], "uf de Ärde", None),
    (11, [1, 2], "Broot", None), (11, [3], "Öises", None), (11, [4, 5], "täglich", "ἐπιούσιος: Bedeutung unsicher"),
    (11, [6], "gib", None), (11, [7], "üs", None), (11, [8], "hüt", None),
    (12, [1], "Und", None), (12, [2], "vergib", None), (12, [3], "üs", None), (12, [4, 5], "Schulde", None), (12, [6], "öisi", None),
    (12, [7], "wie", None), (12, [8], "au", None), (12, [9], "mir", "betont"), (12, [10], "vergää händ", "Aorist"),
    (12, [11, 12], "Schuldner", None), (12, [13], "öisne", None),
    (13, [1], "Und", None), (13, [2], "nöd", None), (13, [3], "füer", "wörtlich «hineinbringen»"), (13, [4], "üs", None),
    (13, [5, 6], "i d Versuechig", None), (13, [7], "sondern", None), (13, [8], "rett", None), (13, [9], "üs", None),
    (13, [10, 11, 12], "vor em Bööse", None),
]
ALIGN_LK = [
    (2, [1], "hät … gseit", None), (2, [2], U, "δέ, nicht eigens wiedergegeben"), (2, [3], "zu ine", None), (2, [4], "Wänn", None),
    (2, [5], "ir bätted", None), (2, [6], "säged", None), (2, [7], "Vatter", None), (2, [8], "söll gheiliget wärde", None),
    (2, [9, 10], "Name", None), (2, [11], "diin", None), (2, [12], "söll choo", None), (2, [13, 14], "Riich", None), (2, [15], "diis", None),
    (3, [1, 2], "Broot", None), (3, [3], "Öises", None), (3, [4, 5], "täglich", None), (3, [6], "gib", "Imperativ Präsens: immer wieder"),
    (3, [7], "üs", None), (3, [8, 9, 10], "Taag für Taag", None),
    (4, [1], "Und", None), (4, [2], "vergib", None), (4, [3], "üs", None), (4, [4, 5], "Sünde", None), (4, [6], "öisi", None),
    (4, [7], "au", None), (4, [8], "dänn", None), (4, [9], "mir sälber", None), (4, [10], "vergänd", None), (4, [11], "jedem", None),
    (4, [12], "wo … öppis schuldig isch", "Partizip als Relativsatz"), (4, [13], "üs", None), (4, [14], "und", None),
    (4, [15], "nöd", None), (4, [16], "füer", None), (4, [17], "üs", None), (4, [18, 19], "i d Versuechig", None),
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
        e = {"reference": f"{book}.{ch}.{v}", "source_tokens": ids, "source": " ".join(by[i]["word"] for i in ids),
             "target": target, "kind": "untranslated" if target is None else ("lexical" if len(ids) == 1 else "phrase")}
        if note:
            e["note_de"] = note
        entries.append(e)
    missing = [t["id"] for t in toks if t["id"] not in seen]
    assert not missing, missing
    w("alignments", {"id": id_, "type": "alignment", "status": "draft", "tags": ["TAG-LORDS-PRAYER"], "reference": R(rng),
                     "source_language": "grc", "target_language": LANG, "source_basis": "ED-SBLGNT",
                     "source_tokens_set": f"TOKSET-SBLGNT-{book}-{ch:03d}", "target_translation": trans_id, "coverage": "complete",
                     "coverage_de": f"Jedes der {len(seen)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                     "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Mundart-Wortlauts.",
                     "alignments": entries, "authorship_de": AUTH, "knowledge": KN})


alignment("ALIGN-MAT-006-009-013-GSW-001", "MAT", 6, "Mt 6,9–13", ALIGN_MT, MT, "TRANS-MAT-006-005-015-GSW-ZH-WORKING", 9, 13)
alignment("ALIGN-LUK-011-002-004-GSW-001", "LUK", 11, "Lk 11,2–4", ALIGN_LK, LK, "TRANS-LUK-011-001-004-GSW-ZH-WORKING", 2, 4)
print(f"PASS: {len(written)} Datensätze geschrieben (Züridüütsch)")
