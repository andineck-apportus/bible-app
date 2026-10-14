#!/usr/bin/env python3
"""Autorenwerkzeug: Jona – Befunde, Deutungen, Grundsätze, Anwendungen, offene Fragen, Beziehungen, Hintergrund
(Abschnitte), Kapitel-Zusammenfassungen, Kontext und Studie; jeweils mit Züridüütsch-Lokalisierung.
Der Buchhintergrund BG-JON-BOOK-0001 besteht schon (scripts/authoring/hintergrund_buecher.py) und wird hier nicht geschrieben.
Die Texteinheiten schreibt scripts/authoring/jona_text.py; dieses Werkzeug hängt an die kleinste vorhandene Einheit an.

Zählungen (MACULA-Lemmata bzw. Strong-Nummern in data/annotations/MACULA-WLC-JON-00*.json, Stellen in KJV-Zählung):
גָּדוֹל 14-mal (dazu Verb גדל in 4,10); יהוה 26-mal (Kap. 1: 12, 2: 6, 3: 2, 4: 6); אֱלֹהִים 16-mal (Kap. 1: 4, 2: 2,
3: 6, 4: 4), davon 5-mal mit Artikel; אֵל 1-mal (4,2); Nomen רָעָה 7-mal, Adjektiv רַע 2-mal, Verb רעע 1-mal;
ירד 4-mal (1,3 zweimal; 1,5; 2,6); רדם 2-mal; טול 4-mal; מנה (Piel) 4-mal; נִינְוֵה 9-mal; קוּם 6-mal.

Aufruf: python3 scripts/authoring/jona_study.py
KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
"""
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D  # noqa: E402

TAGS = ["TAG-JONAH"]
CHAPTER = {1: "TU-JON-001-001-017", 2: "TU-JON-002-001-010", 3: "TU-JON-003-001-010", 4: "TU-JON-004-001-011"}


def U(c, a, b):
    """Kleinste vorhandene Texteinheit (aus jona_text.py), die Kapitel c, Verse a–b umfasst; sonst die Kapiteleinheit."""
    best = CHAPTER[c]
    span = None
    for p in (D / "text-units").glob(f"TU-JON-{c:03d}-*.json"):
        m = re.fullmatch(r"TU-JON-(\d{3})-(\d{3})-(\d{3})", p.stem)
        if not m:
            continue
        lo, hi = int(m.group(2)), int(m.group(3))
        if lo <= a and b <= hi and (span is None or hi - lo < span):
            best, span = p.stem, hi - lo
    return best


CTX = "CTX-JON-NARRATIVE"
CONTEXT = {"id": CTX, "type": "context", "status": "draft", "tags": TAGS + ["TAG-UNCERTAINTY"],
           "period": {"from": -790, "to": -250, "era": "BCE", "approx": True},
           "region": "Israel, das östliche Mittelmeer (Jafo, Tarschisch) und Ninive in Assyrien",
           "language_context": ["he"],
           "audience": "Erzählte Zeit: der Prophet Jona im 8. Jahrhundert v. Chr. unter Jerobeam II.; Leserschaft: Israel bzw. Juda zur (umstrittenen) Abfassungszeit",
           "note_de": "Die Erzählung knüpft an den Propheten Jona, Sohn Amittais, aus [[2KI.14.25]] an (erste Hälfte des 8. Jahrhunderts v. Chr.). Wann sie aufgeschrieben wurde, ist umstritten: vorgeschlagen werden das 8. Jahrhundert, die Zeit nach dem Exil (persische Zeit, 5.–4. Jahrhundert v. Chr.) und die frühe hellenistische Zeit. Spätestens um 190 v. Chr. gehörte das Buch zu den «zwölf Propheten» ([[SIR.49.10]]). Die Zeitangaben sind Näherungen."}

# (id, Abschnitt, Art, Aussage, Belege, Konfidenz, Begründung | Mundart: Aussage, Begründung)
FINDINGS = [
 ("FIND-JON-0001", CHAPTER[1], "literary_structure",
  "Das Buch hat zwei Hälften, die gleich beginnen: «Und es erging das Wort JHWHs an Jona» ([[JON.1.1]]; [[JON.3.1]], dort «ein zweites Mal»). Jede Hälfte hat zwei Szenen: Jona und die Seeleute auf dem Schiff (Kapitel 1), Jonas Gebet im Fisch (Kapitel 2); Jona und die Leute von Ninive (Kapitel 3), Jonas Gespräch mit Gott vor der Stadt (Kapitel 4). In beiden Hälften wenden sich zuerst Nichtisraeliten an Gott (die Seeleute, die Niniviten), danach betet Jona ([[JON.2.1]]; [[JON.4.2]]).",
  ["JON.1.1-JON.1.3", "JON.3.1-JON.3.3", "JON.2.1", "JON.4.2"], "high", "Beobachtung am Ablauf der Erzählung; die Kapiteleinteilung ist jünger als der Text, fällt hier aber mit den Szenen zusammen.",
  "S Buech hät zwei Hälfte, wo gliich aafanged: «Und es isch s Wort vo JHWH zum Jona cho» ([[JON.1.1]]; [[JON.3.1]], det «es zweits Mal»). Jedi Hälfti hät zwei Szene: de Jona und d Seelüüt uf em Schiff (Kapitel 1), s Gebätt vom Jona im Fisch (Kapitel 2); de Jona und d Lüüt vo Ninive (Kapitel 3), s Gspröch vom Jona mit Gott vor de Stadt (Kapitel 4). I beidne Hälfte wänded sich zerscht Nöd-Israelite a Gott (d Seelüüt, d Niniviter), dänn bättet de Jona ([[JON.2.1]]; [[JON.4.2]]).",
  "Beobachtig am Ablauf vo de Erzählig; d Kapiteliiteilig isch jünger als de Text, fallt da aber mit de Szene zäme."),
 ("FIND-JON-0002", U(1, 1, 3), "repetition",
  "Der Auftrag lautet beide Male fast gleich: «Steh auf, geh nach Ninive, der grossen Stadt» ([[JON.1.2]]; [[JON.3.2]]). Auch die Antwort beginnt gleich, «da machte sich Jona auf» (wörtlich «da stand Jona auf»), geht aber verschieden weiter: «um nach Tarschisch zu fliehen» ([[JON.1.3]]) bzw. «und ging nach Ninive» ([[JON.3.3]]). Dazwischen weckt der Kapitän den schlafenden Jona mit denselben Worten «Steh auf, ruf …» ([[JON.1.6]]), die Gott beim Auftrag gebraucht hat.",
  ["JON.1.2-JON.1.3", "JON.1.6", "JON.3.2-JON.3.3"], "high", "Beobachtung am Wortlaut; das Verb קוּם steht nach den MACULA-Lemmata 6-mal im Buch (1,2; 1,3; 1,6; 3,2; 3,3; 3,6), der Imperativ «ruf» (קְרָא) in 1,2; 1,6 und 3,2.",
  "De Uftrag luutet beidi Mal fascht gliich: «Stand uf, gang uf Ninive, di gross Stadt» ([[JON.1.2]]; [[JON.3.2]]). Au d Antwort fangt gliich aa, «da hät sich de Jona ufgmacht» (wörtlich «isch ufgstande»), gaat aber verschide wiiter: «zum uf Tarschisch z flüchte» ([[JON.1.3]]) bzw. «und isch uf Ninive gange» ([[JON.3.3]]). Dezwüsche weckt de Kapitään de schlaafend Jona mit de gliiche Wort «Stand uf, rüef …» ([[JON.1.6]]), wo Gott bim Uftrag bruucht hät.",
  "Beobachtig am Wortluut; s Verb קוּם staat nach de MACULA-Lemmata 6 Mal im Buech (1,2; 1,3; 1,6; 3,2; 3,3; 3,6), de Imperativ «rüef» (קְרָא) i 1,2; 1,6 und 3,2."),
 ("FIND-JON-0003", CHAPTER[1], "key_terms",
  "Das Wort «gross» (gadol) steht 14-mal im Buch: die grosse Stadt Ninive (viermal: [[JON.1.2]]; [[JON.3.2]]; [[JON.3.3]]; [[JON.4.11]]), ein grosser Wind und ein grosser Sturm ([[JON.1.4]]; [[JON.1.12]]), grosse Furcht ([[JON.1.10]]; [[JON.1.16]]), ein grosser Fisch ([[JON.1.17]]), «gross und klein» ([[JON.3.5]]), die Grossen des Königs ([[JON.3.7]]), Jonas grosses Missfallen ([[JON.4.1]]) und seine grosse Freude über die Rizinusstaude ([[JON.4.6]]). Dazu kommt das Verb «gross werden lassen» in [[JON.4.10]]: Jona hat die Staude nicht grossgezogen.",
  ["JON.1.2", "JON.1.4", "JON.1.10", "JON.1.12", "JON.1.16", "JON.1.17", "JON.3.2-JON.3.3", "JON.3.5", "JON.3.7", "JON.4.1", "JON.4.6", "JON.4.10-JON.4.11"], "high",
  "Zählung nach den MACULA-Lemmata (Lemma גָּדוֹל 14-mal, Verb גָּדַל einmal).",
  "S Wort «gross» (gadol) staat 14 Mal im Buech: di gross Stadt Ninive (vier Mal: [[JON.1.2]]; [[JON.3.2]]; [[JON.3.3]]; [[JON.4.11]]), en grosse Wind und en grosse Sturm ([[JON.1.4]]; [[JON.1.12]]), grossi Furcht ([[JON.1.10]]; [[JON.1.16]]), en grosse Fisch ([[JON.1.17]]), «gross und chlii» ([[JON.3.5]]), di Grosse vom König ([[JON.3.7]]), de gross Ärger vom Jona ([[JON.4.1]]) und sini gross Fröid a de Rizinusstuude ([[JON.4.6]]). Dezue chunnt s Verb «gross wärde laa» i [[JON.4.10]]: De Jona hät d Stuude nöd groozoge.",
  "Zellig nach de MACULA-Lemmata (Lemma גָּדוֹל 14 Mal, Verb גָּדַל ei Mal)."),
 ("FIND-JON-0004", CHAPTER[3], "key_terms",
  "Das Wort «böse, Bosheit, Unheil» (ra'a) verbindet die Teile des Buches: Die Bosheit Ninives ist vor Gott aufgestiegen ([[JON.1.2]]); die Seeleute fragen, wer an «diesem Unheil» schuld ist ([[JON.1.7-JON.1.8]]); die Niniviten kehren um von ihrem «bösen Weg», und Gott reut «das Unheil», das er ihnen angesagt hat ([[JON.3.8]]; [[JON.3.10]]). Gleich danach heisst es: «Das war Jona böse, ein grosses Übel» ([[JON.4.1]]). Jona weiss, dass Gott sich das Unheil gereuen lässt ([[JON.4.2]]); die Staude soll Jona von «seinem Übel» befreien ([[JON.4.6]]).",
  ["JON.1.2", "JON.1.7-JON.1.8", "JON.3.8", "JON.3.10", "JON.4.1-JON.4.2", "JON.4.6"], "high",
  "Zählung nach den MACULA-Lemmata: Nomen רָעָה 7-mal, Adjektiv רַע 2-mal (3,8; 3,10), Verb רעע einmal (4,1). Das Verb יִרְעוּ in [[JON.3.7]] («weiden») gehört zu einer anderen Wurzel.",
  "S Wort «bös, Bosheit, Unheil» (ra'a) verbindt d Teil vom Buech: D Bosheit vo Ninive isch vor Gott ufgstige ([[JON.1.2]]); d Seelüüt fröged, wär a «dem Unheil» schuld isch ([[JON.1.7-JON.1.8]]); d Niniviter chered um vo irem «böse Wäg», und Gott reut «s Unheil», won er ine aagseit hät ([[JON.3.8]]; [[JON.3.10]]). Grad dänn heisst s: «Das isch em Jona bös gsii, es grosses Übel» ([[JON.4.1]]). De Jona weiss, dass Gott sich s Unheil la reue ([[JON.4.2]]); d Stuude söll de Jona vo «sim Übel» befreie ([[JON.4.6]]).",
  "Zellig nach de MACULA-Lemmata: Nome רָעָה 7 Mal, Adjektiv רַע 2 Mal (3,8; 3,10), Verb רעע ei Mal (4,1). S Verb יִרְעוּ i [[JON.3.7]] («weide») ghört zu ere andere Wurzle."),
 ("FIND-JON-0005", U(1, 1, 6), "repetition",
  "Jonas Flucht wird als Abstieg erzählt: Er geht hinab nach Jafo, steigt hinab ins Schiff ([[JON.1.3]]), ist hinabgestiegen in den innersten Raum des Schiffes und in tiefen Schlaf gesunken ([[JON.1.5]]); im Psalm sagt er: «Zu den Wurzeln der Berge stieg ich hinab» ([[JON.2.6]]). Das Verb «hinabsteigen» (jarad) steht viermal; «in tiefen Schlaf fallen» (wajjeradam, [[JON.1.5]]) klingt daran an. Erst Gott holt ihn herauf: «Da holtest du mein Leben aus der Grube herauf» ([[JON.2.6]]).",
  ["JON.1.3", "JON.1.5", "JON.2.6"], "high", "Zählung nach den MACULA-Lemmata (Verb ירד 4-mal, Verb רדם 2-mal: 1,5; 1,6). Der Anklang zwischen den beiden Verben ist eine Beobachtung am Klang, kein gemeinsamer Wortstamm.",
  "D Flucht vom Jona wird als Abstiig verzellt: Er gaat abe uf Jafo, stiigt abe is Schiff ([[JON.1.3]]), isch is Innerscht vom Schiff abegstige und tüüf iigschlaafe ([[JON.1.5]]); im Psalm seit er: «Zu de Wurzle vo de Bärg bin ich abegstige» ([[JON.2.6]]). S Verb «abestiige» (jarad) staat vier Mal; «in tüüfe Schlaaf falle» (wajjeradam, [[JON.1.5]]) tönt ähnlich. Erscht Gott holt en ufe: «Da häsch du mis Läbe us de Grueb ufegholt» ([[JON.2.6]]).",
  "Zellig nach de MACULA-Lemmata (Verb ירד 4 Mal, Verb רדם 2 Mal: 1,5; 1,6). De Aaklang zwüsche de beide Verbe isch e Beobachtig am Klang, kein gmeinsame Wortstamm."),
 ("FIND-JON-0006", U(1, 4, 16), "literary_observation",
  "Die Seeleute und die Leute von Ninive handeln vorbildlich, während Jona zögert: Die Seeleute beten, jeder zu seinem Gott ([[JON.1.5]]), versuchen Jona zu retten ([[JON.1.13]]), rufen JHWH an ([[JON.1.14]]) und fürchten JHWH, opfern und legen Gelübde ab ([[JON.1.16]]). Die Niniviten glauben Gott, fasten und kehren um, vom Grössten bis zum Kleinsten ([[JON.3.5-JON.3.9]]). Was Jona im Fisch verspricht – opfern und Gelübde erfüllen ([[JON.2.9]]) –, entspricht dem, was die Seeleute schon getan haben: Sie haben geopfert und Gelübde abgelegt.",
  ["JON.1.5", "JON.1.13-JON.1.16", "JON.2.9", "JON.3.5-JON.3.9"], "high", "Beobachtung am Wortlaut; «Opfer» (זֶבַח/זבח) und «Gelübde» (נדר) stehen nach MACULA nur in [[JON.1.16]] und [[JON.2.9]].",
  "D Seelüüt und d Lüüt vo Ninive handled vorbildlich, wäärend de Jona zöögeret: D Seelüüt bätted, jede zu sim Gott ([[JON.1.5]]), probiered de Jona z rette ([[JON.1.13]]), rüefed de JHWH aa ([[JON.1.14]]) und fürchted de JHWH, opfered und leged Glübd ab ([[JON.1.16]]). D Niniviter glaubed Gott, fasted und chered um, vom Gröschte bis zum Chliischte ([[JON.3.5-JON.3.9]]). Was de Jona im Fisch verspricht – opfere und Glübd iilöse ([[JON.2.9]]) –, entspricht dem, wo d Seelüüt scho gmacht händ: Si händ gopferet und Glübd abgleit.",
  "Beobachtig am Wortluut; «Opfer» (זֶבַח/זבח) und «Glübd» (נדר) stönd nach MACULA nu i [[JON.1.16]] und [[JON.2.9]]."),
 ("FIND-JON-0007", U(2, 2, 9), "form",
  "[[JON.2.2-JON.2.9]] ist ein Psalm in gebundener Sprache, mitten in einer Prosaerzählung. Er ist ein Danklied: Er blickt auf eine Rettung aus Wassernot zurück («ich rief …, und er antwortete mir», [[JON.2.2]]), obwohl Jona noch im Fisch ist; vom Fisch, von Ninive und von Jonas Flucht sagt er nichts. Mehrere Zeilen klingen an Psalmen an: [[JON.2.2]] an [[PSA.120.1]], [[JON.2.3]] wörtlich an [[PSA.42.7]] («alle deine Brecher und deine Wellen gingen über mich hinweg»), [[JON.2.8]] an [[PSA.31.6]], [[JON.2.9]] an [[PSA.3.8]].",
  ["JON.2.2-JON.2.9", "PSA.120.1", "PSA.42.7", "PSA.31.6", "PSA.3.8"], "high", "Beobachtung an Form und Wortlaut; die Übereinstimmung mit [[PSA.42.7]] ist wörtlich, die übrigen sind Anklänge.",
  "[[JON.2.2-JON.2.9]] isch en Psalm i bundener Spraach, mitts i ere Prosaerzählig. Er isch es Dankliid: Er luegt uf e Rettig us Wassernot zrugg («ich han grüeft …, und er hät mer gantwortet», [[JON.2.2]]), obwohl de Jona no im Fisch isch; vom Fisch, vo Ninive und vo de Flucht vom Jona seit er nüt. Meereri Ziile töned wie Psalme: [[JON.2.2]] wie [[PSA.120.1]], [[JON.2.3]] wörtlich wie [[PSA.42.7]] («all dini Brächer und dini Wälle sind über mich ewäg gange»), [[JON.2.8]] wie [[PSA.31.6]], [[JON.2.9]] wie [[PSA.3.8]].",
  "Beobachtig a Form und Wortluut; d Überiistimmig mit [[PSA.42.7]] isch wörtlich, di andere sind Aaklänk."),
 ("FIND-JON-0008", U(4, 6, 11), "literary_structure",
  "Das Buch endet mit einer Frage Gottes, auf die keine Antwort folgt: «Und ich, sollte ich nicht Mitleid haben mit Ninive, der grossen Stadt, in der mehr als hundertzwanzigtausend Menschen sind, die nicht zwischen ihrer Rechten und ihrer Linken zu unterscheiden wissen, und dazu viel Vieh?» ([[JON.4.11]]). Sie ist als Schluss vom Kleineren aufs Grössere gebaut: Jona hat Mitleid mit dem Rizinus, um den er sich nicht abgemüht hat ([[JON.4.10]]); dasselbe Verb «Mitleid haben, jammern» (chus) steht in beiden Versen. Das Buch beginnt auch mit Fragen (der Seeleute, [[JON.1.6-JON.1.11]]) und hat im vierten Kapitel drei Fragen Gottes an Jona ([[JON.4.4]]; [[JON.4.9]]; [[JON.4.11]]).",
  ["JON.4.4", "JON.4.9-JON.4.11", "JON.1.6-JON.1.11"], "high", "Beobachtung am Wortlaut; Verb חוּס nach MACULA nur in 4,10 und 4,11.",
  "S Buech hört mit ere Frag vo Gott uf, und e Antwort chunnt keini: «Und ich, sött ich nöd Mitleid ha mit Ninive, de grosse Stadt, wo mee als hundertzwänzgtuusig Mänsche drin sind, wo nöd zwüsche irer Rächte und irer Linke chönd underscheide, und dezue vill Vee?» ([[JON.4.11]]). Si isch als Schluss vom Chliinere ufs Grösser bout: De Jona hät Mitleid mit em Rizinus, wo n er sich nöd drum abgmüet hät ([[JON.4.10]]); s gliich Verb «Mitleid ha, duure» (chus) staat i beidne Värs. S Buech fangt au mit Frage aa (vo de Seelüüt, [[JON.1.6-JON.1.11]]) und hät im vierte Kapitel drüü Frage vo Gott a de Jona ([[JON.4.4]]; [[JON.4.9]]; [[JON.4.11]]).",
  "Beobachtig am Wortluut; Verb חוּס nach MACULA nu i 4,10 und 4,11."),
 ("FIND-JON-0009", CHAPTER[1], "names",
  "Die Gottesnamen sind ungleich verteilt: JHWH steht 26-mal (Kapitel 1: 12, Kapitel 2: 6, Kapitel 3: 2, Kapitel 4: 6), Elohim («Gott», «Götter») 16-mal (Kapitel 1: 4, Kapitel 2: 2, Kapitel 3: 6, Kapitel 4: 4), dazu einmal El ([[JON.4.2]]). In Kapitel 3 überwiegt Elohim: Die Niniviten glauben «Gott» ([[JON.3.5]]), und «Gott» sieht ihr Tun und lässt sich das Unheil gereuen ([[JON.3.10]]); JHWH steht dort nur in der Wendung «Wort JHWHs» ([[JON.3.1]]; [[JON.3.3]]). Die Seeleute schreien zuerst «jeder zu seinem Gott» ([[JON.1.5]]), am Ende rufen sie JHWH an und fürchten ihn ([[JON.1.14]]; [[JON.1.16]]). In [[JON.4.6]] steht «JHWH Elohim», in [[JON.4.7-JON.4.9]] Elohim, in [[JON.4.10]] wieder JHWH.",
  ["JON.1.5", "JON.1.14", "JON.1.16", "JON.3.1", "JON.3.3", "JON.3.5", "JON.3.10", "JON.4.2", "JON.4.6-JON.4.10"], "high",
  "Zählung nach den MACULA-Lemmata (יהוה 26-mal; אֱלֹהִים 16-mal, davon 5-mal mit Artikel: 1,6; 3,9; 3,10 zweimal; 4,7; אֵל einmal). Mitgezählt sind auch «sein Gott» der Seeleute ([[JON.1.5]]) und «dein Gott» ([[JON.1.6]]).",
  "D Gottesnäme sind ungliich verteilt: JHWH staat 26 Mal (Kapitel 1: 12, Kapitel 2: 6, Kapitel 3: 2, Kapitel 4: 6), Elohim («Gott», «Götter») 16 Mal (Kapitel 1: 4, Kapitel 2: 2, Kapitel 3: 6, Kapitel 4: 4), dezue ei Mal El ([[JON.4.2]]). Im Kapitel 3 überwiegt Elohim: D Niniviter glaubed «Gott» ([[JON.3.5]]), und «Gott» gseet ires Tue und laat sich s Unheil reue ([[JON.3.10]]); JHWH staat det nu i de Wändig «Wort vom JHWH» ([[JON.3.1]]; [[JON.3.3]]). D Seelüüt schreied zerscht «jede zu sim Gott» ([[JON.1.5]]), am Änd rüefed s de JHWH aa und fürchted en ([[JON.1.14]]; [[JON.1.16]]). I [[JON.4.6]] staat «JHWH Elohim», i [[JON.4.7-JON.4.9]] Elohim, i [[JON.4.10]] wider JHWH.",
  "Zellig nach de MACULA-Lemmata (יהוה 26 Mal; אֱלֹהִים 16 Mal, devo 5 Mal mit Artikel: 1,6; 3,9; 3,10 zwei Mal; 4,7; אֵל ei Mal). Mitzellt sind au «sin Gott» vo de Seelüüt ([[JON.1.5]]) und «din Gott» ([[JON.1.6]])."),
 ("FIND-JON-0010", U(4, 1, 4), "quotation",
  "Jona begründet seine Flucht mit einem Bekenntnis: «Ich wusste, dass du ein gnädiger und barmherziger Gott bist, langsam zum Zorn und reich an Treue, und dich das Unheil reut» ([[JON.4.2]]). Die ersten Glieder stammen aus [[EXO.34.6]]; die ganze Reihe einschliesslich «und dich das Unheil reut» (dort in der 3. Person) steht fast wörtlich gleich in [[JOL.2.13]]. Die Frage des Königs von Ninive «Wer weiss, ob Gott umkehrt und es ihn reut …» ([[JON.3.9]]) hat ihre Entsprechung in [[JOL.2.14]].",
  ["JON.4.2", "EXO.34.6-EXO.34.7", "JOL.2.13-JOL.2.14", "JON.3.9"], "high", "Vergleich der hebräischen Texte; in [[JON.4.2]] fehlen «und Treue» (וֶאֱמֶת) aus [[EXO.34.6]] und der ganze Vers [[EXO.34.7]] (Gnade für Tausende, Vergebung, aber auch das Heimsuchen der Schuld); «und dich das Unheil reut» steht nicht in Exodus, wohl aber in [[JOL.2.13]].",
  "De Jona begründet sini Flucht mit eme Bekänntnis: «Ich ha gwüsst, dass du en gnädige und barmhärzige Gott bisch, langsam zum Zorn und riich a Tröii, und dass dich s Unheil reut» ([[JON.4.2]]). Di erschte Glider stammed us [[EXO.34.6]]; di ganz Reie mitsamt «und dass dich s Unheil reut» (det i de 3. Person) staat fascht wörtlich gliich i [[JOL.2.13]]. D Frag vom König vo Ninive «Wär weiss, öb Gott umcheert und es en reut …» ([[JON.3.9]]) hät ires Gägestück i [[JOL.2.14]].",
  "Vergliich vo de hebräische Text; i [[JON.4.2]] fähled «und Tröii» (וֶאֱמֶת) us [[EXO.34.6]] und de ganz Vers [[EXO.34.7]] (Gnad für Tuusigi, Vergääbig, aber au s Heisueche vo de Schuld); «und dass dich s Unheil reut» staat nöd im Exodus, aber i [[JOL.2.13]]."),
 ("FIND-JON-0011", U(1, 17, 17), "key_terms",
  "Viermal heisst es, Gott «bestimmte» (wajman) etwas: einen grossen Fisch ([[JON.1.17]]), eine Rizinusstaude ([[JON.4.6]]), einen Wurm ([[JON.4.7]]) und einen heissen Ostwind ([[JON.4.8]]). Ebenso viermal steht «werfen, schleudern» (hetil) im ersten Kapitel: JHWH schleudert einen Wind aufs Meer, die Seeleute werfen die Ladung und am Ende Jona ins Meer ([[JON.1.4-JON.1.5]]; [[JON.1.12]]; [[JON.1.15]]).",
  ["JON.1.4-JON.1.5", "JON.1.12", "JON.1.15", "JON.1.17", "JON.4.6-JON.4.8"], "high", "Zählung nach den MACULA-Lemmata (מנה im Piel 4-mal, טול 4-mal).",
  "Vier Mal heisst s, Gott heig öppis «bestimmt» (wajman): en grosse Fisch ([[JON.1.17]]), e Rizinusstuude ([[JON.4.6]]), en Wurm ([[JON.4.7]]) und en heisse Oschtwind ([[JON.4.8]]). Gliich vier Mal staat «wärfe, schleudere» (hetil) im erschte Kapitel: De JHWH schleuderet en Wind ufs Meer, d Seelüüt wärfed d Ladig und am Änd de Jona is Meer ([[JON.1.4-JON.1.5]]; [[JON.1.12]]; [[JON.1.15]]).",
  "Zellig nach de MACULA-Lemmata (מנה im Piel 4 Mal, טול 4 Mal)."),
]

# (id, Abschnitt, gestützt auf, Aussage, Konfidenz, Vorbehalt, Gegenargumente, Fachwörter | Mundart …)
INTERPRETATIONS = [
 ("INT-JON-0001", CHAPTER[1], ["FIND-JON-0003", "FIND-JON-0011", "FIND-JON-0006"],
  "Gattung: Das Buch ist eine Lehrerzählung. Es knüpft an einen historischen Propheten an ([[2KI.14.25]]), erzählt aber mit Übertreibung (die Stadt von drei Tagesreisen, der Fisch, Vieh in Sackleinen), Ironie (der Prophet flieht, die Heiden gehorchen) und einer offenen Schlussfrage, um seine Leser zum Nachdenken zu bringen. Manche sprechen von Satire, andere von einem Gleichnis (Maschal).",
  "probable", "Die Gattungsbestimmung ist eine redaktionelle Einordnung; der Text selbst gibt keine Gattung an. «Lehrerzählung» sagt nichts darüber, ob einzelne Ereignisse geschehen sind.",
  ["Jüdische und christliche Tradition lesen das Buch über weite Strecken als Bericht über wirkliche Ereignisse; es ist wie ein Geschichtsbericht erzählt, nennt einen bekannten Propheten mit Vater und Herkunft ([[2KI.14.25]]) und reale Orte.",
   "Jesus stellt Jona und die Niniviten neben die Königin des Südens ([[MAT.12.41-MAT.12.42]]); viele Ausleger folgern daraus, dass er das Erzählte als geschehen voraussetzte. Andere halten dagegen, dass ein solcher Vergleich auch mit einer bekannten Erzählung funktioniert.",
   "Gegen «Satire» wird eingewandt, dass Jona nicht lächerlich gemacht wird: Gott ringt bis zuletzt um ihn, und sein Gebet und sein Bekenntnis ([[JON.4.2]]) sind ernst gemeint."],
  [("heb", "מָשָׁל", "Gleichnis, Spruch, Lehrerzählung", "maschal")],
  "Gattig: S Buech isch e Lehrerzählig. Es chnüpft a en historische Prophet aa ([[2KI.14.25]]), verzellt aber mit Übertriibig (d Stadt vo drüü Tagesreise, de Fisch, Vee i Sackliine), Ironie (de Prophet flüücht, d Heide folged) und ere offene Schlussfrag, zum d Läser zum Nachedänke bringe. Es paar reded vo Satire, anderi vo me Gliichnis (Maschal).",
  "D Bestimmig vo de Gattig isch e redaktionelli Iiordnig; de Text sälber git kei Gattig aa. «Lehrerzählig» seit nüt drüber, öb einzelni Ereignis passiert sind.",
  ["Di jüdisch und di chrischtlich Tradition läsed s Buech über wiiti Strecke als Bricht über würklichi Ereignis; es isch wie en Gschichtsbricht verzellt, nännt en bekannte Prophet mit Vatter und Herkunft ([[2KI.14.25]]) und echti Ort.",
   "De Jesus stellt de Jona und d Niniviter näbe d Königin vom Süde ([[MAT.12.41-MAT.12.42]]); vil Usleger folgered drus, dass er das Verzellte als gscheh vorussetzt hät. Anderi händ degäge, dass so en Vergliich au mit ere bekannte Erzählig funktioniert.",
   "Gäge «Satire» wird iigwändet, dass de Jona nöd lächerlich gmacht wird: Gott ringt bis zletscht um en, und sis Gebätt und sis Bekänntnis ([[JON.4.2]]) sind ärnscht gmeint."],
  ["Gliichnis, Spruch, Lehrerzählig"]),
 ("INT-JON-0002", CHAPTER[1], ["FIND-JON-0009"],
  "Datierung: Viele Ausleger datieren das Buch in die Zeit nach dem Exil (persische oder frühe hellenistische Zeit). Sie verweisen auf späte Sprachformen und aramäische Wörter (z. B. «Befehl», ta'am, [[JON.3.7]]; das Relativwort sche- in [[JON.1.7]]; [[JON.1.12]]; [[JON.4.10]]), der sonst unbelegte Titel «König von Ninive» ([[JON.3.6]]), ein Erlass von König und Grossen gemeinsam ([[JON.3.7]]) und darauf, dass Ninive als Stadt der Vergangenheit erscheint («Ninive war eine grosse Stadt», [[JON.3.3]]). Spätester Zeitpunkt ist etwa 190 v. Chr. ([[SIR.49.10]]).",
  "possible", "Sprachliche Datierung ist unsicher: Aramäische Wörter gab es auch früher, besonders im Norden Israels.",
  ["Wer früh datiert (8. Jahrhundert, Zeit Jerobeams II.), verweist auf [[2KI.14.25]] und darauf, dass Assyrien damals eine Schwächephase hatte; der Titel «König von Ninive» könne volkstümlich gemeint sein.",
   "«Ninive war eine grosse Stadt» kann auch heissen, dass sie es zur Zeit des Geschehens war, ohne vorauszusetzen, dass sie nicht mehr besteht.",
   "Eine mittlere Datierung ins 7. oder 6. Jahrhundert v. Chr. wird ebenfalls vertreten."],
  [("heb", "טַעַם", "Befehl, Erlass (aramäisches Lehnwort)", "ta'am"), ("heb", "שֶׁ", "Relativpartikel «der, die, das; welcher» (späte bzw. nördliche Form neben אֲשֶׁר)", "sche")],
  "Datierig: Vili Usleger datiered s Buech i d Ziit nach em Exil (persischi oder früehi hellenistischi Ziit). Si verwiised uf spaati Spraachforme und aramäischi Wörter (z. B. «Befääl», ta'am, [[JON.3.7]]; s Relativwort sche- i [[JON.1.7]]; [[JON.1.12]]; [[JON.4.10]]), de Titel «König vo Ninive» ([[JON.3.6]]), wo susch niene belegt isch, en Erlass vom König und de Grosse zäme ([[JON.3.7]]) und druf, dass Ninive als Stadt vo de Vergangeheit erschiint («Ninive isch e grossi Stadt gsii», [[JON.3.3]]). Spöötischt isch s öppe 190 v. Chr. dagsii ([[SIR.49.10]]).",
  "Sprachlichi Datierig isch unsicher: Aramäischi Wörter hät s au früener ggää, bsunders im Norde vo Israel.",
  ["Wär früe datiert (8. Jaarhundert, Ziit vom Jerobeam II.), verwiist uf [[2KI.14.25]] und druf, dass Assyrie dänn e schwachi Phase gha hät; de Titel «König vo Ninive» chönn volkstümlich gmeint sii.",
   "«Ninive isch e grossi Stadt gsii» cha au heisse, dass si s zur Ziit vom Gscheh gsii isch, ooni vorusszsetze, dass si nüme staat.",
   "E mittleri Datierig is 7. oder 6. Jaarhundert v. Chr. wird au vertrete."],
  ["Befääl, Erlass (aramäischs Leenwort)", "Relativwort «wo» (spaati bzw. nördlichi Form näbe אֲשֶׁר)"]),
 ("INT-JON-0003", U(2, 2, 9), ["FIND-JON-0007", "FIND-JON-0005"],
  "Der Psalm [[JON.2.2-JON.2.9]] gehörte von Anfang an zum Buch: Er nimmt das Motiv des Abstiegs auf ([[JON.2.6]]), verbindet sich über Opfer und Gelübde mit den Seeleuten ([[JON.1.16]]; [[JON.2.9]]) und zeigt einen Jona, der fromme Worte findet, aber bis Kapitel 4 nicht verändert ist. Gerade die Spannung zwischen Psalm und Erzählung kann beabsichtigt sein.",
  "possible", "Ob der Psalm ursprünglich ist, lässt sich am Text allein nicht entscheiden; beide Positionen werden in der Forschung vertreten.",
  ["Viele halten den Psalm für nachträglich eingefügt: Er ist Dank, wo man eine Bitte erwartet, nennt weder Fisch noch Ninive, und [[JON.2.10]] schliesst glatt an [[JON.2.1]] an.",
   "Die Sprache des Psalms ist weitgehend aus anderen Psalmen bekannt ([[PSA.42.7]]; [[PSA.120.1]]); das spricht für ein vorhandenes Lied, das eingesetzt wurde – sei es vom Erzähler selbst oder von einem späteren Bearbeiter."],
  [],
  "De Psalm [[JON.2.2-JON.2.9]] hät vo Aafang a zum Buech ghört: Er nimmt s Motiv vom Abstiig uf ([[JON.2.6]]), verbindt sich über Opfer und Glübd mit de Seelüüt ([[JON.1.16]]; [[JON.2.9]]) und zeigt en Jona, wo fromi Wort findt, aber bis zum Kapitel 4 nöd veränderet isch. Grad d Spannig zwüsche Psalm und Erzählig cha gwollt sii.",
  "Öb de Psalm ursprünglich isch, cha me am Text elei nöd entscheide; beidi Positione wärded i de Forschig vertrete.",
  ["Vil halted de Psalm für nachträglich iigfüegt: Er isch Dank, wo me e Bitt erwartet, nännt weder Fisch no Ninive, und [[JON.2.10]] schlüüsst glatt a [[JON.2.1]] aa.",
   "D Spraach vom Psalm isch wiitgehend us andere Psalme bekannt ([[PSA.42.7]]; [[PSA.120.1]]); das spricht für es vorhandnigs Lied, wo iigsetzt worde isch – sig s vom Erzähler sälber oder vo me spöötere Bearbeiter."],
  []),
 ("INT-JON-0004", U(4, 6, 11), ["FIND-JON-0008", "FIND-JON-0010", "FIND-JON-0006"],
  "Zweck: Das Buch zeigt, dass Gottes Erbarmen auch den Feinden Israels gilt (Universalität). Die Seeleute und Ninive werden angenommen, als sie umkehren; die Schlussfrage ([[JON.4.11]]) stellt Gottes Mitleid mit Menschen und Vieh einer ganzen fremden Stadt gegen Jonas Mitleid mit einer Staude.",
  "probable", "Die drei hier genannten Zwecke schliessen sich nicht aus; welcher im Vordergrund steht, ist eine redaktionelle Gewichtung.",
  ["Kritik an prophetischer Erwartung: Das Buch zeigt einen Propheten, dessen angesagtes Gericht nicht eintrifft ([[JON.3.4]]; [[JON.3.10]]), und fragt, ob Prophetie überhaupt unbedingte Vorhersage ist (vgl. [[JER.18.7-JER.18.10]]); im Mittelpunkt stünde dann Jonas Rolle, nicht die der Völker.",
   "Frage der Gerechtigkeit gegenüber Feinden (Theodizee): Assyrien zerstörte Samaria ([[2KI.17.5-2KI.17.6]]); Nahum kündigt Ninive den Untergang an ([[NAM.1.1-NAM.1.3]]). Jonas Zorn wäre dann die Frage, ob Gnade für die Gewalttätigen gerecht ist; das Buch beantwortet sie nicht, es stellt sie.",
   "Gegen eine Spitze gegen ein «enges» Judentum der Nachexilszeit wird eingewandt, dass das Buch selbst ein jüdisches Buch ist und Jonas Einwand mit Israels eigenem Bekenntnis begründet ([[JON.4.2]])."],
  [("heb", "חוּס", "Mitleid haben, jammern, schonen", "chus")],
  "Zwäck: S Buech zeigt, dass s Erbarme vo Gott au de Find vo Israel gilt (Universalität). D Seelüüt und Ninive wärded aagnoo, wo s umchered; d Schlussfrag ([[JON.4.11]]) stellt s Mitleid vo Gott mit Mänsche und Vee vo ere ganze fremde Stadt gäge s Mitleid vom Jona mit ere Stuude.",
  "Di drüü Zwäck, wo da gnännt sind, schlüüssed sich nöd us; wele im Vordergrund staat, isch e redaktionelli Gwichtig.",
  ["Kritik a prophetischer Erwartig: S Buech zeigt en Prophet, wo s aagseit Gricht nöd iitrifft ([[JON.3.4]]; [[JON.3.10]]), und fröget, öb Prophetie überhaupt e unbedingti Voraussag isch (vgl. [[JER.18.7-JER.18.10]]); im Mittelpunkt wür dänn d Rolle vom Jona staa, nöd die vo de Völker.",
   "Frag vo de Grächtigkeit gägenüber Find (Theodizee): Assyrie hät Samaria zerstört ([[2KI.17.5-2KI.17.6]]); de Nahum seit Ninive de Undergang aa ([[NAM.1.1-NAM.1.3]]). De Zorn vom Jona wär dänn d Frag, öb Gnad für d Gwalttätige grächt isch; s Buech beantwortet si nöd, es stellt si.",
   "Gäge e Spitze gäge es «engs» Judetum nach em Exil wird iigwändet, dass s Buech sälber es jüdischs Buech isch und de Iiwand vom Jona mit em eigete Bekänntnis vo Israel begründet ([[JON.4.2]])."],
  ["Mitleid ha, duure, schoone"]),
 ("INT-JON-0005", U(3, 1, 4), ["FIND-JON-0004"],
  "Jonas einziger Spruch «Noch vierzig Tage, und Ninive wird umgestürzt» ([[JON.3.4]]) ist doppeldeutig: Das Verb hafach heisst «umstürzen» wie bei Sodom ([[GEN.19.25]]), kann aber auch «verwandeln, umwenden» bedeuten. So erfüllt sich der Spruch auf andere Weise: Ninive wird nicht zerstört, sondern verwandelt.",
  "possible", "Die Doppeldeutigkeit ist möglich, aber im Text nicht ausdrücklich gemacht; [[JON.3.10]] spricht davon, dass Gott das Unheil nicht tut.",
  ["Der Wortlaut «umgestürzt» meint im Zusammenhang eindeutig Zerstörung; der Erzähler sagt selbst, Gott habe das angesagte Unheil nicht getan ([[JON.3.10]]). Die zweite Bedeutung wird dann erst vom Leser eingetragen."],
  [("heb", "נֶהְפָּכֶת", "umgestürzt (werdend); auch: verwandelt", "nehpachet"), ("heb", "הָפַךְ", "umstürzen, umwenden, verwandeln", "hafach")],
  "Dä einzig Spruch vom Jona «No vierzg Täg, und Ninive wird umgstürzt» ([[JON.3.4]]) isch zwöidüütig: S Verb hafach heisst «umstürze» wie bi Sodom ([[GEN.19.25]]), cha aber au «verwandle, umchere» heisse. So erfüllt sich de Spruch uf e anderi Art: Ninive wird nöd zerstört, sondern verwandlet.",
  "D Zwöidüütigkeit isch möglich, aber im Text nöd usdrücklich gmacht; [[JON.3.10]] redt devo, dass Gott s Unheil nöd macht.",
  ["De Wortluut «umgstürzt» meint im Zämehang eidüütig Zerstörig; de Erzähler seit sälber, Gott heig s aagseit Unheil nöd gmacht ([[JON.3.10]]). Di zweit Bedüütig treit dänn erscht de Läser ii."],
  ["umgstürzt (wo grad wird); au: verwandlet", "umstürze, umchere, verwandle"]),
 ("INT-JON-0006", U(1, 17, 17), ["FIND-JON-0005"],
  "Rezeption: Jesus nimmt Jona als «Zeichen» auf. Nach [[MAT.12.39-MAT.12.41]] entsprechen die drei Tage und drei Nächte Jonas im Bauch des Seetiers dem Menschensohn «im Herzen der Erde»; nach [[LUK.11.29-LUK.11.32]] war Jona selbst für die Niniviten ein Zeichen, und die Niniviten, die auf seine Predigt umkehrten, werden diese Generation verurteilen. Das ist eine Deutung des Jonabuches im Neuen Testament, kein Beleg innerhalb des Jonabuches selbst.",
  "high", "Die Evangelien setzen verschiedene Akzente (Matthäus: Fisch und Auferweckung; Lukas: Predigt und Umkehr). Ob «Zeichen des Jona» ursprünglich die Predigt oder die Rettung aus dem Tod meinte, ist umstritten.",
  ["Christliche Auslegung hat Jona seit der Alten Kirche als Vorbild (Typos) für Tod und Auferstehung Jesu gelesen; aus dieser Sicht ist der Bezug mehr als Rezeption, nämlich im Plan Gottes angelegt.",
   "Jüdische Auslegung liest das Buch ohne diesen Bezug; am Versöhnungstag (Jom Kippur) wird es als Prophetenlesung über Umkehr gelesen."],
  [("grc", "σημεῖον Ἰωνᾶ", "Zeichen des Jona"), ("grc", "κῆτος", "grosses Seetier (in der Septuaginta für den «grossen Fisch»)")],
  "Rezeption: De Jesus nimmt de Jona als «Zeiche» uf. Nach [[MAT.12.39-MAT.12.41]] entspräched di drüü Täg und drüü Nächt vom Jona im Buuch vom Meertier em Mänschesohn «im Härz vo de Ärde»; nach [[LUK.11.29-LUK.11.32]] isch de Jona sälber für d Niniviter es Zeiche gsii, und d Niniviter, wo uf sini Predig umcheert sind, wärded die Generation verurteile. Das isch e Düütig vom Jonabuech im Neue Teschtamänt, kein Beleg im Jonabuech sälber.",
  "D Evangelie setzed verschideni Akzänt (Matthäus: Fisch und Uferweckig; Lukas: Predig und Umchehr). Öb «Zeiche vom Jona» ursprünglich d Predig oder d Rettig us em Tod gmeint hät, isch umstritte.",
  ["Di chrischtlich Uslegig hät de Jona sit de Alte Chile als Vorbild (Typos) für de Tod und d Uferstehig vom Jesus gläse; us dere Sicht isch de Bezug me als Rezeption, nämlich im Plan vo Gott aaglegt.",
   "Di jüdisch Uslegig list s Buech ooni dä Bezug; am Versöönigstaag (Jom Kippur) wird s als Prophetelesig über d Umchehr gläse."],
  ["Zeiche vom Jona", "grosses Meertier (i de Septuaginta für de «grosse Fisch»)"]),
 ("INT-JON-0007", CHAPTER[3], ["FIND-JON-0009"],
  "Der Wechsel der Gottesnamen ist erzählerisch gesteuert: Wo Nichtisraeliten ohne Kenntnis JHWHs handeln, steht eher Elohim («Gott»), wo es um den Gott Israels und seinen Bund geht, steht JHWH. Die Seeleute kommen vom «Gott» zum Namen JHWH ([[JON.1.5]]; [[JON.1.16]]); die Niniviten glauben «Gott» ([[JON.3.5]]).",
  "possible", "Die Verteilung ist nicht streng: Auch Jona betet im Psalm zu «JHWH, meinem Gott» ([[JON.2.6]]), und in [[JON.4.7-JON.4.9]] handelt Elohim an Jona.",
  ["Ältere Literarkritik erklärte den Wechsel mit verschiedenen Quellen oder Bearbeitungen.",
   "Andere halten den Wechsel weitgehend für stilistische Abwechslung ohne festes Prinzip."],
  [("heb", "יהוה", "JHWH, der Name des Gottes Israels", "JHWH"), ("heb", "אֱלֹהִים", "Gott; Götter", "elohim")],
  "De Wächsel vo de Gottesnäme isch erzählerisch gstüüret: Wo Nöd-Israelite ooni Kenntnis vom JHWH handled, staat eener Elohim («Gott»), wo s um de Gott vo Israel und sin Bund gaat, staat JHWH. D Seelüüt chömed vom «Gott» zum Name JHWH ([[JON.1.5]]; [[JON.1.16]]); d Niniviter glaubed «Gott» ([[JON.3.5]]).",
  "D Verteilig isch nöd sträng: Au de Jona bättet im Psalm zum «JHWH, mim Gott» ([[JON.2.6]]), und i [[JON.4.7-JON.4.9]] handlet Elohim am Jona.",
  ["Elteri Literarkritik hät de Wächsel mit verschidene Quälle oder Bearbeitige erklärt.",
   "Anderi halted de Wächsel wiitgehend für stilistischi Abwächslig ooni feschts Prinzip."],
  ["JHWH, de Name vom Gott vo Israel", "Gott; Götter"]),
]

# (id, abgeleitet aus, Aussage, Konfidenz | Mundart)
PRINCIPLES = [
 ("PRIN-JON-0001", ["FIND-JON-0010", "INT-JON-0004"],
  "Gottes Barmherzigkeit ist nicht auf das eigene Volk beschränkt; sie gilt auch denen, die man als Feinde erlebt ([[JON.4.11]]).", "probable",
  "D Barmhärzigkeit vo Gott isch nöd uf s eiget Volk beschränkt; si gilt au dene, wo me als Find erläbt ([[JON.4.11]])."),
 ("PRIN-JON-0002", ["FIND-JON-0004", "INT-JON-0005"],
  "Gerichtsankündigungen zielen auf Umkehr; wo Menschen umkehren, kann Gott das angesagte Unheil zurücknehmen ([[JON.3.10]]; [[JER.18.7-JER.18.8]]).", "probable",
  "Grichtsaakündigunge ziiled uf Umchehr; wo Mänsche umchered, cha Gott s aagseit Unheil zruggnee ([[JON.3.10]]; [[JER.18.7-JER.18.8]])."),
 ("PRIN-JON-0003", ["FIND-JON-0006"],
  "Gottesfurcht und Umkehr finden sich auch bei Menschen ausserhalb der eigenen Glaubensgemeinschaft, manchmal eher als bei den Beauftragten selbst ([[JON.1.16]]; [[JON.3.5]]).", "probable",
  "Gottesfurcht und Umchehr findt me au bi Mänsche usserhalb vo de eigete Glaubesgmeinschaft, mängisch eener als bi dene, wo de Uftrag händ, ([[JON.1.16]]; [[JON.3.5]])."),
 ("PRIN-JON-0004", ["FIND-JON-0008", "FIND-JON-0004"],
  "Wer ein Bekenntnis zu Gottes Gnade kennt, kann sich trotzdem darüber ärgern, wenn sie anderen gilt; die Frage nach dem eigenen Zorn bleibt offen gestellt ([[JON.4.2]]; [[JON.4.4]]).", "possible",
  "Wär es Bekänntnis zur Gnad vo Gott kännt, cha sich glich drüber ärgere, wänn si andere gilt; d Frag nach em eigete Zorn bliibt offe gstellt ([[JON.4.2]]; [[JON.4.4]])."),
]
# (id, Grundsatz, Aussage, Grenzen | Mundart)
APPLICATIONS = [
 ("APP-JON-0001", "PRIN-JON-0001",
  "Heute kann das heissen, die eigenen Vorbehalte gegenüber Gruppen zu prüfen, denen man Gutes nicht gönnt – etwa politischen Gegnern, früheren Tätern oder Fremden – und sich zu fragen, ob man ihnen Umkehr und einen Neuanfang zugesteht.",
  "Das Buch spricht von einer Stadt, die umkehrt; es fordert nicht, Unrecht hinzunehmen oder Opfern Versöhnung abzuverlangen. Gerechtigkeit und Schutz der Betroffenen bleiben eigene Fragen.",
  "Hüt cha das heisse, di eigete Vorbehält gägenüber Gruppe z prüefe, wo me Guets nöd gönnt – öppe politische Gägner, früenere Täter oder Fremde – und sich z fröge, öb me ine Umchehr und en Neuaafang zuestaat.",
  "S Buech redt vo ere Stadt, wo umchert; es verlangt nöd, Unrächt aaznee oder vo Opfer Versöönig z verlange. Grächtigkeit und de Schutz vo de Betroffne blibed eigeti Frage."),
 ("APP-JON-0002", "PRIN-JON-0002",
  "Warnungen – in Predigt, Erziehung oder öffentlicher Debatte – sind dann am Ziel, wenn sie zur Veränderung führen, nicht wenn sie recht behalten.",
  "Der Text spricht von Gottes Gericht über eine Stadt; die Übertragung auf menschliche Warnungen ist eine Analogie und keine Aussage des Textes.",
  "Warnige – i de Predig, i de Erziehig oder i de öffentliche Debatte – sind dänn am Ziil, wänn s zu ere Veränderig füered, nöd wänn s rächt bhalted.",
  "De Text redt vom Gricht vo Gott über e Stadt; d Übertragig uf mänschlichi Warnige isch e Analogie und kei Ussag vom Text."),
 ("APP-JON-0003", "PRIN-JON-0003",
  "Gemeinden und Glaubende können mit Respekt wahrnehmen, wo Menschen ausserhalb ihrer Kreise ehrlich, gottesfürchtig oder hilfsbereit handeln, wie die Seeleute, die Jona zu retten versuchen ([[JON.1.13]]).",
  "Das Buch macht keine Aussage darüber, ob alle Religionen gleichwertig sind; die Seeleute wenden sich am Ende JHWH zu ([[JON.1.16]]).",
  "Gmeinde und Glaubendi chönd mit Reschpäkt wahrnee, wo Mänsche usserhalb vo irne Chreis ehrlich, gottesfürchtig oder hilfsbereit handled, wie d Seelüüt, wo de Jona probiered z rette ([[JON.1.13]]).",
  "S Buech macht kei Ussag drüber, öb alli Religione gliichwärtig sind; d Seelüüt wänded sich am Änd em JHWH zue ([[JON.1.16]])."),
 ("APP-JON-0004", "PRIN-JON-0004",
  "Die offene Schlussfrage lädt ein, sie persönlich zu beantworten: Worüber ärgere ich mich, wenn es anderen gut geht? Was ist mir wichtiger, mein eigenes Behagen (die Staude) oder das Leben anderer?",
  "Jonas Zorn hat in der Erzählung einen geschichtlichen Hintergrund (Assyrien als Gewaltmacht); er ist nicht einfach kleinlich, und die Frage sollte nicht vorschnell moralisierend beantwortet werden.",
  "Di offe Schlussfrag laadt ii, si persönlich z beantworte: Über was ärgere ich mich, wänn s andere guet gaat? Was isch mir wichtiger, mis eige Behage (d Stuude) oder s Läbe vo andere?",
  "De Zorn vom Jona hät i de Erzählig en gschichtliche Hindergrund (Assyrie als Gwaltmacht); er isch nöd eifach chliinlich, und d Frag sött me nöd vorschnäll moralisierend beantworte."),
]
# (id, Abschnitt, Frage, Stand | Mundart)
QUESTIONS = [
 ("QUESTION-JON-0001", CHAPTER[1], "Ist das Buch Jona ein Bericht über Ereignisse des 8. Jahrhunderts v. Chr., eine Lehrerzählung, eine Satire oder ein Gleichnis?",
  "Alle vier Einordnungen werden vertreten; der Text gibt seine Gattung nicht an. Die Entscheidung hängt auch von Vorentscheidungen über Wunder und über die Bedeutung der Worte Jesu ab.",
  "Isch s Buech Jona en Bricht über Ereignis vom 8. Jaarhundert v. Chr., e Lehrerzählig, e Satire oder es Gliichnis?",
  "Alli vier Iiordnige wärded vertrete; de Text git sini Gattig nöd aa. D Entscheidig hangt au vo Vorentscheidige über Wunder und über d Bedüütig vo de Wort vom Jesus ab."),
 ("QUESTION-JON-0002", U(2, 2, 9), "Gehörte der Psalm [[JON.2.2-JON.2.9]] von Anfang an zum Buch?",
  "Umstritten. Gegen die Ursprünglichkeit sprechen Form (Dank statt Bitte) und fehlende Bezüge zur Handlung; dafür sprechen Wortbezüge (Abstieg, Opfer und Gelübde) und die erzählerische Spannung, die er erzeugt.",
  "Hät de Psalm [[JON.2.2-JON.2.9]] vo Aafang a zum Buech ghört?",
  "Umstritte. Gäge d Ursprünglichkeit spräched d Form (Dank statt Bitt) und d fählende Bezüg zur Handlig; defür spräched Wortbezüg (Abstiig, Opfer und Glübd) und d erzählerisch Spannig, won er erzüügt."),
 ("QUESTION-JON-0003", U(4, 1, 4), "Warum ist Jona zornig: weil seine Ankündigung nicht eintrifft, weil Gott dem Feind Israels gnädig ist, oder weil er Gottes Gerechtigkeit in Frage gestellt sieht?",
  "Der Text nennt nur Jonas eigene Begründung ([[JON.4.2]]); die Ausleger gewichten die Gründe verschieden.",
  "Werum isch de Jona toub: wil sini Aakündigung nöd iitrifft, wil Gott em Find vo Israel gnädig isch, oder wil er d Grächtigkeit vo Gott in Frag gstellt gseet?",
  "De Text nännt nu d eiget Begründig vom Jona ([[JON.4.2]]); d Usleger gwichted d Gründ verschide."),
 ("QUESTION-JON-0004", U(3, 1, 4), "Wie ist die Angabe zu verstehen, Ninive sei «eine Stadt von drei Tagesreisen» gewesen ([[JON.3.3]])?",
  "Vorschläge: die Fläche eines Grossraums mit mehreren Städten (vgl. [[GEN.10.11-GEN.10.12]]), die Dauer eines Besuchs mit Predigt in allen Stadtteilen, oder bewusste erzählerische Übertreibung. Die ausgegrabene Stadt war für eine dreitägige Durchquerung zu klein.",
  "Wie isch d Aagab z verstaa, Ninive sig «e Stadt vo drüü Tagesreise» gsii ([[JON.3.3]])?",
  "Vorschleeg: d Flächi vo me Grossruum mit meerere Stedt (vgl. [[GEN.10.11-GEN.10.12]]), d Duur vo me Bsuech mit Predig i allne Stadtteil, oder bewussti erzählerischi Übertriibig. Di usgrabe Stadt isch für e Durchquerig vo drüü Täg z chlii gsii."),
]
# (id, von, zu, Art, Konfidenz)
RELATIONS = [
 ("REL-JON-0001", U(1, 1, 3), "2KI.14.25", "background", "high"),
 ("REL-JON-0002", U(4, 1, 4), "EXO.34.6-EXO.34.7", "parallel_quotation", "high"),
 ("REL-JON-0003", U(4, 1, 4), "JOL.2.13-JOL.2.14", "parallel_text", "high"),
 ("REL-JON-0004", CHAPTER[3], "NAM.1.1-NAM.1.3", "thematic", "probable"),
 ("REL-JON-0005", CHAPTER[3], "JER.18.7-JER.18.10", "thematic", "probable"),
 ("REL-JON-0006", U(1, 17, 17), "MAT.12.39-MAT.12.41", "allusion", "high"),
 ("REL-JON-0007", CHAPTER[3], "LUK.11.29-LUK.11.32", "allusion", "high"),
 ("REL-JON-0008", U(2, 2, 9), "PSA.42.7", "parallel_text", "high"),
 ("REL-JON-0009", U(2, 2, 9), "PSA.120.1", "motif", "probable"),
 ("REL-JON-0010", U(3, 1, 4), "GEN.19.25", "motif", "possible"),
 ("REL-JON-0011", U(3, 5, 10), "MAT.12.41", "allusion", "high"),
 ("REL-JON-0012", U(4, 6, 11), "1KI.19.4", "motif", "probable"),
]

# (id, Abschnitt, Stelle, Kontext, Konfidenz, Thema, Text, Unsicherheit, Belege, Quellen, Fachwörter | Mundart: Thema, Text, Unsicherheit, Fachwörter)
BACKGROUND = [
 ("BG-JON-0001", U(3, 1, 4), "JON.3.3", CTX, "probable", "Ninive: Lage, Grösse und «drei Tagesreisen»",
  "Ninive lag am Ostufer des Tigris, gegenüber dem heutigen Mossul im Nordirak; die Ruinen bilden zwei Hügel, Kujundschik und Nebi Junus («Prophet Jona», mit einem überlieferten Jonagrab). Unter Sanherib (705–681 v. Chr.) wurde Ninive Hauptstadt Assyriens; seine Stadtmauer war rund 12 km lang. 612 v. Chr. eroberten Babylonier und Meder die Stadt. Die Angabe «eine Stadt von drei Tagesreisen» ([[JON.3.3]]) übersteigt diese Grösse deutlich; Jona geht «eine Tagesreise» hinein ([[JON.3.4]]). [[GEN.10.11-GEN.10.12]] nennt Ninive zusammen mit Kalach und Resen «die grosse Stadt».",
  "Die Masse der Stadt beziehen sich auf ihre grösste Ausdehnung im 7. Jahrhundert v. Chr.; im frühen 8. Jahrhundert war sie kleiner. Die Bedeutung von «drei Tagesreisen» ist umstritten (siehe offene Frage).",
  ["JON.3.3-JON.3.4", "GEN.10.11-GEN.10.12", "NAM.3.1"], [], [("heb", "נִינְוֵה", "Ninive", "ninwe"), ("heb", "מַהֲלַךְ שְׁלֹשֶׁת יָמִים", "ein Weg von drei Tagen", "mahalach schloschet jamim")],
  "Ninive: Lag, Grössi und «drüü Tagesreise»",
  "Ninive isch am Oschtufer vom Tigris gläge, vis-à-vis vom hütige Mossul im Nordirak; d Ruine bilded zwei Hügel, Kujundschik und Nebi Junus («Prophet Jona», mit eme überlieferete Jonagraab). Under em Sanherib (705–681 v. Chr.) isch Ninive Hauptstadt vo Assyrie worde; sini Stadtmuur isch rund 12 km lang gsii. 612 v. Chr. händ Babylonier und Meder d Stadt eroberet. D Aagab «e Stadt vo drüü Tagesreise» ([[JON.3.3]]) gaat wiit über die Grössi use; de Jona gaat «ei Tagesreis» drii ([[JON.3.4]]). [[GEN.10.11-GEN.10.12]] nännt Ninive zäme mit Kalach und Resen «di gross Stadt».",
  "D Mass vo de Stadt beziend sich uf iri gröschti Usdeenig im 7. Jaarhundert v. Chr.; im früene 8. Jaarhundert isch si chliiner gsii. Was «drüü Tagesreise» bedüütet, isch umstritte (lueg di offe Frag).",
  ["Ninive", "en Wäg vo drüü Täg"]),
 ("BG-JON-0002", CHAPTER[1], "JON.1.2", CTX, "probable", "Assyrien im 8. Jahrhundert v. Chr.",
  "In der ersten Hälfte des 8. Jahrhunderts v. Chr., zur Zeit Jerobeams II. von Israel, war Assyrien geschwächt: Die assyrische Eponymenliste nennt für diese Jahre Aufstände, Seuchen und eine Sonnenfinsternis (datiert auf den 15. Juni 763 v. Chr.). Ab Tiglat-Pileser III. (745–727 v. Chr.) wurde Assyrien zur beherrschenden Grossmacht; 722/720 v. Chr. fiel Samaria, die Hauptstadt Israels ([[2KI.17.5-2KI.17.6]]). Assyrische Könige rühmen sich in ihren Inschriften grausamer Strafen an besiegten Gegnern; [[NAM.3.1]] nennt Ninive «Stadt der Blutschuld».",
  "Manche haben die Unruhen und die Sonnenfinsternis der 760er-Jahre mit der Bereitschaft Ninives zur Umkehr verbunden; das ist eine Vermutung ohne Beleg. Assyrische Quellen erwähnen weder Jona noch eine Umkehr Ninives.",
  ["2KI.14.23-2KI.14.25", "2KI.17.5-2KI.17.6", "NAM.3.1"], ["Assyrische Eponymenliste (Eintrag zur Sonnenfinsternis im Eponymat des Bur-Saggile)"], [],
  "Assyrie im 8. Jaarhundert v. Chr.",
  "I de erschte Hälfti vom 8. Jaarhundert v. Chr., zur Ziit vom Jerobeam II. vo Israel, isch Assyrie gschwächt gsii: Di assyrisch Eponymeliste nännt für die Jaar Ufständ, Süüche und e Sunnefinschternis (datiert uf de 15. Juni 763 v. Chr.). Ab em Tiglat-Pileser III. (745–727 v. Chr.) isch Assyrie di beherrschend Grossmacht worde; 722/720 v. Chr. isch Samaria gfalle, d Hauptstadt vo Israel ([[2KI.17.5-2KI.17.6]]). Assyrischi Könige rüemed sich i irne Inschrifte vo grausame Strafe a bsiegte Gägner; [[NAM.3.1]] nännt Ninive «Stadt vo de Bluetschuld».",
  "Es paar händ d Unrue und d Sunnefinschternis vo de 760er-Jaar mit de Bereitschaft vo Ninive zur Umchehr verbunde; das isch e Vermuetig ooni Beleg. Assyrischi Quälle erwääned weder de Jona no e Umchehr vo Ninive.",
  []),
 ("BG-JON-0003", U(1, 1, 3), "JON.1.3", CTX, "probable", "Jafo und Tarschisch",
  "Jafo (Joppe, heute Jaffa, Teil von Tel Aviv) war ein Hafen an der Küste; dorthin wurde nach [[2CH.2.16]] und [[EZR.3.7]] Zedernholz aus dem Libanon geflösst. Tarschisch ist ein Ziel weit im Westen über das Meer; «Tarschisch-Schiffe» sind grosse Hochseeschiffe ([[1KI.10.22]]), und Tarschisch handelte mit Silber, Eisen, Zinn und Blei ([[EZK.27.12]]). Ninive liegt im Osten, auf dem Landweg; Jona wählt die entgegengesetzte Richtung. Jona bezahlt «ihren Lohn» ([[JON.1.3]]; das Fürwort bezieht sich auf das Schiff), wohl den Fahrpreis.",
  "Wo Tarschisch lag, ist unsicher: vorgeschlagen werden Tartessos in Südwestspanien, Sardinien (die Nora-Inschrift nennt einen Ort TRŠŠ) und Tarsus in Kilikien (so Josephus).",
  ["JON.1.3", "JON.4.2", "2CH.2.16", "EZR.3.7", "1KI.10.22", "EZK.27.12", "ISA.66.19"], ["Flavius Josephus, Jüdische Altertümer 9,208"],
  [("heb", "תַּרְשִׁישׁ", "Tarschisch", "tarschisch"), ("heb", "יָפוֹ", "Jafo (Joppe, Jaffa)", "jafo")],
  "Jafo und Tarschisch",
  "Jafo (Joppe, hüt Jaffa, en Teil vo Tel Aviv) isch en Hafe a de Chüschte gsii; det ane isch nach [[2CH.2.16]] und [[EZR.3.7]] Zedereholz us em Libanon gflösst worde. Tarschisch isch es Ziil wiit im Weschte überem Meer; «Tarschisch-Schiff» sind grossi Hochseeschiff ([[1KI.10.22]]), und Tarschisch hät mit Silber, Iise, Zinn und Blei ghandlet ([[EZK.27.12]]). Ninive liit im Oschte, uf em Landwääg; de Jona wäält di entgägegsetzt Richtig. De Jona zaalt «ire Loon» ([[JON.1.3]]; s «ire» meint s Schiff), wohl de Faarpriis.",
  "Wo Tarschisch gläge isch, isch unsicher: Vorgschlage wärded Tartessos im Südweschte vo Spanie, Sardinie (d Nora-Inschrift nännt en Ort TRŠŠ) und Tarsus z Kilikie (so de Josephus).",
  ["Tarschisch", "Jafo (Joppe, Jaffa)"]),
 ("BG-JON-0004", U(1, 4, 16), "JON.1.7", CTX, "probable", "Seefahrt und Losentscheid",
  "Die Seeleute (mallachim) und ihr Kapitän, wörtlich wohl «der Oberste der Seilleute» ([[JON.1.6]]), stammen aus verschiedenen Völkern und beten zu verschiedenen Göttern ([[JON.1.5]]). Bei Seenot warf man die Ladung über Bord, um das Schiff zu erleichtern (vgl. [[ACT.27.18-ACT.27.19]]). Das Los galt als Mittel, eine verborgene Schuld durch Gott aufzudecken, wie bei Achan ([[JOS.7.14-JOS.7.18]]) und bei Jonatan ([[1SA.14.41-1SA.14.42]]); «Im Gewandbausch wird das Los geworfen, aber von JHWH kommt jede Entscheidung» ([[PRO.16.33]]). Nur hier heisst das Schiff sefina ([[JON.1.5]]), sonst steht onija.",
  "Wie das Los geworfen wurde (Steine, Stäbchen, beschriftete Scherben), sagt der Text nicht.",
  ["JON.1.4-JON.1.7", "ACT.27.18-ACT.27.19", "JOS.7.14-JOS.7.18", "1SA.14.41-1SA.14.42", "PRO.16.33"], [],
  [("heb", "גּוֹרָל", "Los", "goral"), ("heb", "מַלָּח", "Seemann", "mallach"), ("heb", "סְפִינָה", "Schiff (mit Deck?)", "sefina"), ("heb", "אֳנִיָּה", "Schiff", "onija")],
  "Seefaart und Losentscheid",
  "D Seelüüt (mallachim) und ire Kapitään, wörtlich wohl «de Oberscht vo de Seillüüt» ([[JON.1.6]]), chömed us verschidene Völker und bätted zu verschidene Götter ([[JON.1.5]]). Bi Seenot hät me d Ladig über Bord gworfe, zum s Schiff liechter mache (vgl. [[ACT.27.18-ACT.27.19]]). S Los hät als Mittel gulte, e versteckti Schuld dur Gott ufzdecke, wie bim Achan ([[JOS.7.14-JOS.7.18]]) und bim Jonatan ([[1SA.14.41-1SA.14.42]]); «I de Gwandfalte wird s Los gworfe, aber vom JHWH chunnt jedi Entscheidig» ([[PRO.16.33]]). Nu da heisst s Schiff sefina ([[JON.1.5]]), susch staat onija.",
  "Wie s Los gworfe worde isch (Stei, Stäbli, aagschribni Schärbe), seit de Text nöd.",
  ["Los", "Seemaa", "Schiff (mit Deck?)", "Schiff"]),
 ("BG-JON-0005", U(1, 17, 17), "JON.1.17", CTX, "high", "Der «grosse Fisch»",
  "Der hebräische Text spricht von einem «grossen Fisch» (dag gadol, [[JON.1.17]]); in [[JON.2.1]] steht die weibliche Form daga. Die Septuaginta übersetzt mit kētos, «grosses Meerestier, Seeungeheuer»; dieses Wort steht auch in [[MAT.12.40]]. Die verbreitete Vorstellung eines «Wals» stammt aus späteren Übersetzungen, nicht aus dem hebräischen Text. Die Tiefe des Meeres steht im Psalm für die Nähe des Todes («aus dem Schoss des Totenreichs», [[JON.2.2]]).",
  "Welches Tier gemeint ist, sagt der Text nicht; die Erzählung betont, dass Gott es «bestimmt» ([[JON.1.17]]).",
  ["JON.1.17", "JON.2.1-JON.2.2", "JON.2.10", "MAT.12.40"], ["Septuaginta, Jona 2,1 (Ausgabe Rahlfs)"],
  [("heb", "דָּג גָּדוֹל", "grosser Fisch", "dag gadol"), ("heb", "דָּגָה", "Fisch (weibliche Form)", "daga"), ("heb", "שְׁאוֹל", "Unterwelt, Totenreich", "sche'ol"), ("grc", "κῆτος", "grosses Meerestier")],
  "De «gross Fisch»",
  "De hebräisch Text redt vo me «grosse Fisch» (dag gadol, [[JON.1.17]]); i [[JON.2.1]] staat di wiiblich Form daga. D Septuaginta übersetzt mit kētos, «grosses Meertier, Seeungheuer»; das Wort staat au i [[MAT.12.40]]. Di verbreitet Vorstellig vo me «Wal» chunnt vo spöötere Übersetzige, nöd us em hebräische Text. D Tüüfi vom Meer staat im Psalm für d Nööchi vom Tod («us em Schooss vom Toterich», [[JON.2.2]]).",
  "Weles Tier gmeint isch, seit de Text nöd; d Erzählig betont, dass Gott s «bestimmt» ([[JON.1.17]]).",
  ["grosse Fisch", "Fisch (wiiblichi Form)", "Underwält, Toterich", "grosses Meertier"]),
 ("BG-JON-0006", U(3, 5, 10), "JON.3.8", CTX, "probable", "Sackleinen und Fasten, auch für das Vieh",
  "Sackleinen (sak), ein grobes Tuch aus Ziegen- oder Kamelhaar, und Fasten waren Zeichen der Trauer und der Busse ([[2SA.3.31]]; [[JOL.1.13-JOL.1.14]]); der König setzt sich in die Asche ([[JON.3.6]]; vgl. [[JOB.2.8]]). Dass auch die Tiere fasten und in Sackleinen gehüllt werden ([[JON.3.7-JON.3.8]]), ist ungewöhnlich. Ähnliches berichtet [[JDT.4.10]] (auch das Vieh in Sackleinen) und Herodot von den Persern, die bei der Trauer um ihren Feldherrn Masistios sich selbst, ihre Pferde und Zugtiere schoren. Der Erlass ergeht im Namen «des Königs und seiner Grossen» ([[JON.3.7]]).",
  "Ob der Brauch, Tiere in die Trauer einzubeziehen, in Assyrien geübt wurde, ist nicht belegt; viele lesen die Stelle als bewusste Übersteigerung.",
  ["JON.3.5-JON.3.8", "2SA.3.31", "JOL.1.13-JOL.1.14", "JOB.2.8", "JDT.4.10"], ["Herodot, Historien 9,24"],
  [("heb", "שַׂק", "Sack, Sackleinen", "sak"), ("heb", "צוֹם", "Fasten", "tsom")],
  "Sackliine und Faschte, au für s Vee",
  "Sackliine (sak), es groobs Tuech us Geiss- oder Kamelhaar, und Faschte sind Zeiche vo Truur und Buess gsii ([[2SA.3.31]]; [[JOL.1.13-JOL.1.14]]); de König sitzt in Äsche ([[JON.3.6]]; vgl. [[JOB.2.8]]). Dass au d Tier fasted und in Sackliine iipackt wärded ([[JON.3.7-JON.3.8]]), isch ussergwöönlich. Ähnlichs verzellt [[JDT.4.10]] (au s Vee i Sackliine) und de Herodot vo de Perser, wo bi de Truur um iren Fäldherr Masistios sich sälber, iri Ross und Zugtier gschore händ. De Erlass gaat im Name «vom König und sine Grosse» use ([[JON.3.7]]).",
  "Öb de Bruuch, Tier i d Truur iizbeziee, z Assyrie üeblich gsii isch, isch nöd belegt; vil läsed d Stell als bewussti Übersteigerig.",
  ["Sack, Sackliine", "Faschte"]),
 ("BG-JON-0007", U(4, 6, 11), "JON.4.6", CTX, "probable", "Die Rizinusstaude (qiqajon)",
  "Das Wort qiqajon kommt in der Bibel nur in Jona 4 vor (fünfmal, [[JON.4.6-JON.4.10]]). Meist wird es mit dem Rizinus (Wunderbaum) gleichgesetzt, der schnell wächst und grosse Blätter hat; Herodot nennt das ägyptische Rizinusöl «kiki», und die Mischna kennt ein «Kik-Öl». Die Septuaginta übersetzt «Kürbis»; Hieronymus setzte in der Vulgata «Efeu» (hedera). Nach einem Brief Augustins (Brief 71) führte diese neue Übersetzung in der Gemeinde von Oea (Tripolis) zu einem Aufruhr, weil man an «Kürbis» gewöhnt war.",
  "Die botanische Bestimmung ist nicht sicher; die Erzählung lässt die Pflanze in einer Nacht wachsen und vergehen ([[JON.4.10]]).",
  ["JON.4.6-JON.4.10"], ["Herodot, Historien 2,94", "Mischna, Schabbat 2,1", "Augustinus, Brief 71 (an Hieronymus)"],
  [("heb", "קִיקָיוֹן", "Rizinus (?), Staude", "qiqajon"), ("heb", "שֶׁמֶן קִיק", "Kik-Öl (Mischna)", "schemen qiq"), ("grc", "κίκι", "Rizinusöl (ägyptisches Wort nach Herodot)")],
  "D Rizinusstuude (qiqajon)",
  "S Wort qiqajon chunnt i de Bible nu im Jona 4 vor (füf Mal, [[JON.4.6-JON.4.10]]). Meischtens setzt me s em Rizinus (Wunderbaum) gliich, wo schnäll wachst und grossi Blätter hät; de Herodot nännt s ägyptisch Rizinusöl «kiki», und d Mischna kännt es «Kik-Öl». D Septuaginta übersetzt «Kürbis»; de Hieronymus hät i de Vulgata «Efeu» (hedera) gsetzt. Nach eme Brief vom Augustinus (Brief 71) hät die nöi Übersetzig i de Gmeind vo Oea (Tripolis) zu me Ufruer gfüert, wil me a «Kürbis» gwöönt gsii isch.",
  "D botanisch Bestimmig isch nöd sicher; d Erzählig laat d Pflanze i einere Nacht wachse und vergaa ([[JON.4.10]]).",
  ["Rizinus (?), Stuude", "Kik-Öl (Mischna)", "Rizinusöl (ägyptischs Wort nach em Herodot)"]),
 ("BG-JON-0008", U(4, 6, 11), "JON.4.8", CTX, "high", "Der Ostwind",
  "Der «Ostwind» (qadim) ist der heisse, trockene Wind aus der Wüste, heute Chamsin oder Scharav genannt. Er lässt Pflanzen verdorren ([[EZK.17.10]]; [[HOS.13.15]]) und kann auf dem Meer Schiffe zerbrechen ([[PSA.48.7]]). In [[JON.4.8]] heisst er zusätzlich charischit; die Bedeutung dieses nur hier belegten Wortes ist unsicher («glühend», «schwül» oder «still»).",
  "Die Übersetzung von charischit ist unsicher.",
  ["JON.4.8", "EZK.17.10", "HOS.13.15", "PSA.48.7"], [],
  [("heb", "רוּחַ קָדִים", "Ostwind", "ruach qadim"), ("heb", "חֲרִישִׁית", "glühend (?), schwül (?)", "charischit")],
  "De Oschtwind",
  "De «Oschtwind» (qadim) isch de heiss, trochni Wind us de Wüeschti, hüt Chamsin oder Scharav gnännt. Er laat Pflanze verdoore ([[EZK.17.10]]; [[HOS.13.15]]) und cha uf em Meer Schiff verbräche ([[PSA.48.7]]). I [[JON.4.8]] heisst er dezue no charischit; was das Wort, wo nu da vorchunnt, bedüütet, isch unsicher («glüeiig», «schwüel» oder «still»).",
  "D Übersetzig vo charischit isch unsicher.",
  ["Oschtwind", "glüeiig (?), schwüel (?)"]),
 ("BG-JON-0009", CHAPTER[3], "JON.3.4", CTX, "probable", "Jona in der frühen jüdischen Überlieferung",
  "Jesus Sirach (um 190 v. Chr.) nennt «die zwölf Propheten» ([[SIR.49.10]]). Im Buch Tobit ist Ninives Untergang Thema: In der kürzeren griechischen Fassung beruft sich Tobit auf das, was «Jona der Prophet» über Ninive gesagt hat ([[TOB.14.4]]); in der längeren Fassung (Codex Sinaiticus) steht dort Nahum. Josephus erzählt in den Jüdischen Altertümern die Flucht nach «Tarsus in Kilikien», den Fisch und Jonas Ansage, Ninive werde seine Herrschaft verlieren; die Umkehr Ninives und Kapitel 4 übergeht er. Die Septuaginta liest in [[JON.3.4]] «noch drei Tage» statt «noch vierzig Tage».",
  "Die Angaben sind nicht an den Handschriften bzw. am griechischen Text geprüft. Abgeglichen (Recherche vom 2026-10-14) wurden nur Sekundärquellen: zu [[TOB.14.4]] (Jona in Vaticanus und Alexandrinus, Nahum in Sinaiticus) eine Fachdiskussion, zu Josephus 9,208 (Joppe, «Tarsus in Kilikien», Verlust der Herrschaft) eine englische Übersetzung (Whiston). Dass Josephus die Umkehr Ninives und Kapitel 4 übergeht, ist nicht am Text nachgeprüft. Vor Übernahme in Befunde nachprüfen.",
  ["SIR.49.10", "TOB.14.4", "JON.3.4"], ["Flavius Josephus, Jüdische Altertümer 9,206–214", "Tobit 14,4 (kürzere griechische Fassung, Codex Vaticanus und Alexandrinus; längere Fassung, Codex Sinaiticus)", "Septuaginta, Jona 3,4 (Ausgabe Rahlfs)"],
  [],
  "De Jona i de früene jüdische Überlieferig",
  "De Jesus Sirach (öppe 190 v. Chr.) nännt «di zwölf Prophete» ([[SIR.49.10]]). Im Buech Tobit isch de Undergang vo Ninive es Thema: I de chürzere griechische Fassig beruft sich de Tobit uf das, wo «de Jona, de Prophet» über Ninive gseit hät ([[TOB.14.4]]); i de längere Fassig (Codex Sinaiticus) staat det Nahum. De Josephus verzellt i de Jüdische Altertümer d Flucht uf «Tarsus z Kilikie», de Fisch und d Aasag vom Jona, Ninive wärdi sini Herrschaft verliere; d Umchehr vo Ninive und s Kapitel 4 laat er us. D Septuaginta list i [[JON.3.4]] «no drüü Täg» statt «no vierzg Täg».",
  "D Aagabe sind nöd a de Handschrifte bzw. am griechische Text prüeft. Vergliche (Recherche vom 2026-10-14) worde sind nu Sekundärquälle: zu [[TOB.14.4]] (Jona im Vaticanus und Alexandrinus, Nahum im Sinaiticus) e Fachdiskussion, zum Josephus 9,208 (Joppe, «Tarsus z Kilikie», Verluscht vo de Herrschaft) en änglischi Übersetzig (Whiston). Dass de Josephus d Umchehr vo Ninive und s Kapitel 4 uslaat, isch nöd am Text nochepprüeft. Vor de Übernaam i Befund nochepruefe.",
  []),
]

# (id, Text | Mundart)
SUMMARIES = [
 ("SUM-CH-JON-001", "JHWH sendet Jona nach Ninive, der grossen Stadt, deren Bosheit vor ihn gekommen ist. Jona flieht in die Gegenrichtung und nimmt in Jafo ein Schiff nach Tarschisch. JHWH schleudert einen Sturm aufs Meer; die Seeleute beten zu ihren Göttern, werfen das Los, und es fällt auf Jona. Auf seinen Rat werfen sie ihn ins Meer, nachdem sie vergeblich zu rudern versucht haben; das Meer wird ruhig, und die Seeleute fürchten JHWH, opfern und legen Gelübde ab. Ein grosser Fisch verschlingt Jona; er ist drei Tage und drei Nächte in seinem Bauch.",
  "De JHWH schickt de Jona uf Ninive, i di gross Stadt, wo iri Bosheit vor en cho isch. De Jona flüücht i di anderi Richtig und nimmt z Jafo es Schiff uf Tarschisch. De JHWH schleuderet en Sturm ufs Meer; d Seelüüt bätted zu irne Götter, wärfed s Los, und s trifft de Jona. Uf sin Root rüered s en is Meer, nachdem s vergäbe probiert händ z ruedere; s Meer wird ruig, und d Seelüüt fürchted de JHWH, opfered und leged Glübd ab. En grosse Fisch verschluckt de Jona; er isch drüü Täg und drüü Nächt i sim Buuch."),
 ("SUM-CH-JON-002", "Aus dem Bauch des Fisches betet Jona zu JHWH. Sein Gebet ist ein Psalm: Er schildert, wie er in die Tiefe des Meeres und bis zu den Wurzeln der Berge hinabsank und wie JHWH sein Leben aus der Grube heraufholte; er will opfern und seine Gelübde erfüllen und bekennt: «Die Rettung gehört JHWH.» Auf JHWHs Wort speit der Fisch Jona aufs Land.",
  "Us em Buuch vom Fisch bättet de Jona zum JHWH. Sis Gebätt isch en Psalm: Er schilderet, wien er i d Tüüfi vom Meer und bis zu de Wurzle vo de Bärg abegsunke isch und wie de JHWH sis Läbe us de Grueb ufegholt hät; er wott opfere und sini Glübd erfüle und bekännt: «D Rettig ghört JHWH.» Uf s Wort vom JHWH spöit de Fisch de Jona as Land."),
 ("SUM-CH-JON-003", "Zum zweiten Mal ergeht JHWHs Wort an Jona; diesmal geht er nach Ninive und ruft: «Noch vierzig Tage, und Ninive wird umgestürzt.» Die Leute von Ninive glauben Gott, rufen ein Fasten aus und ziehen Sackleinen an. Der König steht von seinem Thron auf, setzt sich in die Asche und befiehlt mit seinen Grossen, dass Menschen und Vieh fasten, Sackleinen tragen, zu Gott rufen und von ihrem bösen Weg umkehren. Gott sieht ihre Umkehr, das angesagte Unheil reut ihn, und er führt es nicht aus.",
  "Zum zweite Mal chunnt s Wort vom JHWH zum Jona; dasmal gaat er uf Ninive und rüeft: «No vierzg Täg, und Ninive wird umgstürzt.» D Lüüt vo Ninive glaubed Gott, rüefed es Faschte us und leged Sackliine aa. De König staat vo sim Troon uf, sitzt i d Äsche und befiehlt mit sine Grosse, dass Mänsche und Vee fasted, Sackliine träged, zu Gott rüefed und vo irem böse Wäg umchered. Gott gseet iri Umchehr, s aagseit Unheil reut en, und er macht s nöd."),
 ("SUM-CH-JON-004", "Jona ist darüber sehr verärgert und sagt, gerade deshalb sei er geflohen: Er wisse, dass Gott gnädig und barmherzig ist; er will lieber sterben. Gott fragt: «Ist es recht, dass du zornig bist?» Jona setzt sich östlich der Stadt hin. Gott lässt eine Rizinusstaude wachsen, die ihm Schatten gibt, dann einen Wurm, der sie verdorren lässt, und einen heissen Ostwind. Jona wünscht sich wieder den Tod. Gott hält ihm vor: Er habe Mitleid mit der Staude, um die er sich nicht abgemüht hat; sollte Gott da nicht Mitleid haben mit Ninive, mit mehr als 120 000 Menschen und viel Vieh? Mit dieser Frage endet das Buch.",
  "De Jona isch drüber seer verärgeret und seit, grad drum sig er gflüchtet: Er wüssi, dass Gott gnädig und barmhärzig isch; er wett lieber stärbe. Gott fröget: «Isch s rächt, dass du toub bisch?» De Jona sitzt östlich vo de Stadt ane. Gott laat e Rizinusstuude wachse, wo n em Schatte git, dänn en Wurm, wo si laat verdoore, und en heisse Oschtwind. De Jona wünscht sich wider de Tod. Gott hebt em vor: Er heig Mitleid mit de Stuude, wo n er sich nöd drum abgmüet hät; sött dänn Gott nöd Mitleid ha mit Ninive, mit mee als 120 000 Mänsche und vil Vee? Mit dere Frag hört s Buech uf."),
]


def run():
    from _study import write_study
    missing = [u for u in CHAPTER.values() if not (D / "text-units" / f"{u}.json").exists()]
    if missing:
        raise SystemExit(f"Texteinheiten fehlen (zuerst scripts/authoring/jona_text.py ausführen): {', '.join(missing)}")
    trans = sorted(p.stem for p in (D / "translations").glob("TRANS-JON-00*-WORKING.json"))
    write_study({"TAGS": TAGS, "CONTEXT": CONTEXT, "FINDINGS": FINDINGS, "INTERPRETATIONS": INTERPRETATIONS,
                 "PRINCIPLES": PRINCIPLES, "APPLICATIONS": APPLICATIONS, "QUESTIONS": QUESTIONS, "RELATIONS": RELATIONS,
                 "BACKGROUND": BACKGROUND, "SUMMARIES": SUMMARIES,
                 "STUDY": ("STUDY-JON-0001", "Jona: ganzes Buch (Hebräisch)", CHAPTER[1], trans,
                           ["Mundart muttersprachlich prüfen",
                            "Angaben zu [[TOB.14.4]] (Fassungen) und Josephus, Jüdische Altertümer 9,206–214 am Text prüfen",
                            "Textkritische Daten (Septuaginta, Qumran, Murabba'at) aus freien Quellen ergänzen",
                            "Fachliche Prüfung der Deutungen und des Hintergrunds"])}, "Jona")


if __name__ == "__main__":
    run()
