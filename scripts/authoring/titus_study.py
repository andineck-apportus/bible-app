#!/usr/bin/env python3
"""Autorenwerkzeug: Titusbrief – Befunde, Deutungen, Grundsätze, Anwendungen, offene Fragen, Beziehungen,
Hintergrund (Abschnitte und Buch), Kapitel-Zusammenfassungen, Kontext und Studie; jeweils mit Züridüütsch-Lokalisierung.

Aufruf: python3 scripts/authoring/titus_study.py
KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, localize, write  # noqa: E402

DATE = "2026-10-13"
AUTH = "KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-13; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft."
TAGS = ["TAG-TITUS"]
KN = {"asserted_at": DATE, "supersedes": None}
L = ("gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026")

CONTEXT = {"id": "CTX-TIT-READERS", "type": "context", "status": "draft", "tags": TAGS + ["TAG-UNCERTAINTY"],
           "period": {"from": 63, "to": 110, "era": "CE", "approx": True}, "region": "Kreta (römische Provinz Creta et Cyrenaica)",
           "language_context": ["grc"], "audience": "Titus und die jungen Gemeinden in den Städten Kretas",
           "note_de": "Ob der Brief um 63–65 n. Chr. von Paulus selbst oder später (etwa 80–110 n. Chr.) in seinem Namen geschrieben wurde, ist umstritten."}

# (id, Abschnitt, Art, Aussage, Belege, Konfidenz, Begründung | Mundart: Aussage, Begründung)
FINDINGS = [
 ("FIND-TIT-0001", "TU-TIT-001-005-009", "terminology",
  "Der Abschnitt beginnt mit «Älteste» (Mehrzahl, [[TIT.1.5]]) und fährt mit «denn der Aufseher muss …» (Einzahl, [[TIT.1.7]]) fort; das «denn» verbindet beide Begriffe zu einer Begründung.",
  ["TIT.1.5-TIT.1.7"], "high", "Beobachtung am Wortlaut.",
  "De Abschnitt fangt mit «Ältischte» (Meerzaal, [[TIT.1.5]]) aa und fahrt mit «dänn de Ufseher mues …» (Einzaal, [[TIT.1.7]]) wiiter; s «dänn» verbindet beidi Begriff zu ere Begründig.",
  "Beobachtig am Wortluut."),
 ("FIND-TIT-0002", "TU-TIT-001-010-016", "quotation",
  "[[TIT.1.12]] zitiert einen griechischen Vers (Hexameter): «Kreter sind immer Lügner, böse Tiere, faule Bäuche». Die Wendung «Kreter sind immer Lügner» steht auch beim Dichter Kallimachos; Clemens von Alexandria (um 200) schreibt den Vers Epimenides von Kreta zu.",
  ["TIT.1.12"], "probable", "Kallimachos, Hymnos auf Zeus 8; Clemens von Alexandria, Stromata 1,59. Die Zuschreibung an Epimenides ist antike Überlieferung, nicht gesichert.",
  "[[TIT.1.12]] zitiert en griechische Vers (Hexameter): «Kreter sind immer Lugner, bösi Tier, fuuli Büüch». D Wändig «Kreter sind immer Lugner» staat au bim Dichter Kallimachos; de Clemens vo Alexandria (um 200) schriibt de Vers em Epimenides vo Kreta zue.",
  "Kallimachos, Hymnos uf Zeus 8; Clemens vo Alexandria, Stromata 1,59. D Zueschriibig a de Epimenides isch antiki Überlieferig, nöd gsicheret."),
 ("FIND-TIT-0003", "TU-TIT-002-011-015", "key_terms",
  "Das Verb «erscheinen» (ἐπιφαίνω) und das Nomen «Erscheinen» (ἐπιφάνεια) tragen den Brief: Die Gnade Gottes «ist erschienen» ([[TIT.2.11]]), die Herrlichkeit wird erwartet ([[TIT.2.13]]), die Güte Gottes «erschien» ([[TIT.3.4]]).",
  ["TIT.2.11", "TIT.2.13", "TIT.3.4"], "high", "Zählung nach den MACULA-Lemmata.",
  "S Verb «erschiine» (ἐπιφαίνω) und s Nomen «Erschiine» (ἐπιφάνεια) träged de Brief: D Gnad vo Gott «isch erschine» ([[TIT.2.11]]), d Herrlichkeit wird erwartet ([[TIT.2.13]]), d Güeti vo Gott «isch erschine» ([[TIT.3.4]]).",
  "Zellig nach de MACULA-Lemmata."),
 ("FIND-TIT-0004", "TU-TIT-001-001-016", "key_terms",
  "«Retter» (σωτήρ) steht sechsmal, immer paarweise: dreimal für Gott ([[TIT.1.3]]; [[TIT.2.10]]; [[TIT.3.4]]) und jeweils kurz danach für Jesus Christus ([[TIT.1.4]]; [[TIT.2.13]]; [[TIT.3.6]]).",
  ["TIT.1.3-TIT.1.4", "TIT.2.10-TIT.2.13", "TIT.3.4-TIT.3.6"], "high", "Zählung nach den MACULA-Lemmata.",
  "«Retter» (σωτήρ) staat sächs Mal, immer paarwiis: drüü Mal für Gott ([[TIT.1.3]]; [[TIT.2.10]]; [[TIT.3.4]]) und jedesmal churz druf für de Jesus Christus ([[TIT.1.4]]; [[TIT.2.13]]; [[TIT.3.6]]).",
  "Zellig nach de MACULA-Lemmata."),
 ("FIND-TIT-0005", "TU-TIT-002-001-010", "argument_structure",
  "Die Weisungen an die Gruppen werden mit der Wirkung nach aussen begründet: «damit das Wort Gottes nicht in Verruf kommt» ([[TIT.2.5]]), «damit der Gegner beschämt wird» ([[TIT.2.8]]), «damit sie die Lehre Gottes schmücken» ([[TIT.2.10]]).",
  ["TIT.2.5", "TIT.2.8", "TIT.2.10"], "high", "Beobachtung am Wortlaut.",
  "D Wiisige a d Gruppe wärded mit de Würkig gäge usse begründet: «demit s Wort vo Gott nöd in Verruef chunnt» ([[TIT.2.5]]), «demit de Gägner sich schämt» ([[TIT.2.8]]), «demit si d Lehr vo Gott schmücked» ([[TIT.2.10]]).",
  "Beobachtig am Wortluut."),
 ("FIND-TIT-0006", "TU-TIT-003-008-011", "key_terms",
  "«Werk» (ἔργον) steht achtmal im Brief, meist als «gute Werke». Nur einmal wird betont, dass die Rettung nicht aus Werken kommt ([[TIT.3.5]]); kurz danach sollen die Glaubenden sich gerade für gute Werke einsetzen ([[TIT.3.8]]).",
  ["TIT.1.16", "TIT.2.7", "TIT.2.14", "TIT.3.1", "TIT.3.5", "TIT.3.8", "TIT.3.14"], "high", "Zählung nach den MACULA-Lemmata (8 Belege).",
  "«Wärch» (ἔργον) staat acht Mal im Brief, meischtens als «gueti Wärch». Nu eimal wird betont, dass d Rettig nöd us Wärch chunnt ([[TIT.3.5]]); churz druf söled sich d Gläubige grad für gueti Wärch iisetze ([[TIT.3.8]]).",
  "Zellig nach de MACULA-Lemmata (8 Beleg)."),
 ("FIND-TIT-0007", "TU-TIT-001-001-016", "text_history",
  "Der Codex Vaticanus (4. Jh.) enthält den Titusbrief nicht; seine Paulusbriefe brechen im Hebräerbrief ab. Ältester erhaltener Zeuge ist der Papyrus 𝔓32 (um 200) mit Teilen von [[TIT.1.11-TIT.1.15]] und [[TIT.2.3-TIT.2.8]]. In den hier erfassten Lesarten geht 𝔓32 laut automatischer Zuordnung mit den grossen Handschriften des 4. und 5. Jahrhunderts.",
  ["TIT.1.11-TIT.1.15", "TIT.2.3-TIT.2.8"], "probable", "Umfang nach den CNTR-Transkriptionen; Zuordnung maschinell (METHOD-AUTO-COLLATION-V1), nicht am Faksimile geprüft.",
  "De Codex Vaticanus (4. Jh.) enthaltet de Titusbrief nöd; sini Paulusbrief bräched im Hebräerbrief ab. Eltischte erhaltene Züüge isch de Papyrus 𝔓32 (um 200) mit Teil vo [[TIT.1.11-TIT.1.15]] und [[TIT.2.3-TIT.2.8]]. I de da erfasste Läsarte gaat 𝔓32 nach de automatische Zueornig mit de groosse Handschrifte vom 4. und 5. Jaarhundert.",
  "Umfang nach de CNTR-Transkriptione; Zueornig maschinell, nöd am Faksimile prüeft."),
]

# (id, Abschnitt, gestützt auf, Aussage, Konfidenz, Vorbehalt, Gegenargumente, Fachwörter | Mundart: Aussage, Vorbehalt, Gegenargumente, Fachwörter)
INTERPRETATIONS = [
 ("INT-TIT-0001", "TU-TIT-001-005-009", ["FIND-TIT-0001"],
  "«Älteste» und «Aufseher» bezeichnen dieselben Leiter der Gemeinden; ein Bischof über mehreren Ältesten, wie ihn die Kirche später kennt, ist hier noch nicht vorausgesetzt.",
  "probable", "Die Einzahl «der Aufseher» kann auch typisierend gemeint sein («jeder Aufseher»).",
  ["Andere sehen in der Einzahl einen Hinweis darauf, dass sich bereits ein einzelner Leiter aus dem Kreis der Ältesten heraushebt."],
  [("grc", "πρεσβύτερος", "Ältester"), ("grc", "ἐπίσκοπος", "Aufseher")],
  "«Ältischte» und «Ufseher» meined di gliiche Leiter vo de Gmeinde; en Bischof über meerere Ältischte, wie en d Chile spööter kännt, isch da no nöd voruusgsetzt.",
  "D Einzaal «de Ufseher» cha au typisierend gmeint sii («jede Ufseher»).",
  ["Anderi gsend i de Einzaal en Hiiwiis, dass sich scho en einzelne Leiter us em Chreis vo de Ältischte usehebt."],
  ["Ältischte", "Ufseher"]),
 ("INT-TIT-0002", "TU-TIT-001-005-009", ["FIND-TIT-0001"],
  "«Mann einer einzigen Frau» ([[TIT.1.6]]) verlangt eheliche Treue: Ein Leiter soll in seiner Ehe untadelig sein.",
  "possible", "Der Ausdruck ist knapp und wurde schon in der Alten Kirche verschieden verstanden.",
  ["Viele Ausleger der Alten Kirche verstanden ihn als Verbot einer zweiten Ehe, auch nach dem Tod der Frau.",
   "Andere denken vor allem an das Verbot der Vielehe oder einer Wiederheirat nach Scheidung."],
  [],
  "«Maa vo nu eire Frau» ([[TIT.1.6]]) verlangt Tröii i de Ee: En Leiter söll i sinere Ee untadelig sii.",
  "De Usdruck isch knapp und isch scho i de Alte Chile verschide verstande worde.",
  ["Vili Usleger vo de Alte Chile händ en als Verbot vo ere zweite Ee verstande, au nach em Tod vo de Frau.",
   "Anderi dänked vor allem as Verbot vo de Vilee oder vo ere Widerhürat nach ere Scheidig."],
  []),
 ("INT-TIT-0003", "TU-TIT-002-011-015", ["FIND-TIT-0003", "FIND-TIT-0004"],
  "[[TIT.2.13]] nennt Jesus Christus «unseren grossen Gott und Retter»: Ein einziger Artikel verbindet «Gott» und «Retter», und erwartet wird das Erscheinen Christi, nicht das Gottes des Vaters.",
  "probable", "Die Stelle ist für die Frage, ob das Neue Testament Jesus «Gott» nennt, wichtig und deshalb seit langem umstritten.",
  ["Andere lesen zwei Personen: «die Herrlichkeit des grossen Gottes und unseres Retters Jesus Christus». Im Brief bezeichnet «Gott» sonst immer den Vater; Jesus Christus wird neben ihm genannt ([[TIT.1.4]])."],
  [("grc", "ἐπιφάνεια", "Erscheinen"), ("grc", "σωτήρ", "Retter")],
  "[[TIT.2.13]] nännt de Jesus Christus «öise groosse Gott und Retter»: En einzige Artikel verbindet «Gott» und «Retter», und erwartet wird s Erschiine vo Christus, nöd s Erschiine vo Gott em Vatter.",
  "D Stell isch für d Frag, öb s Nöi Teschtamänt de Jesus «Gott» nännt, wichtig und drum sit langem umstritte.",
  ["Anderi läsed zwei Persone: «d Herrlichkeit vom groosse Gott und vo öisem Retter Jesus Christus». Im Brief meint «Gott» süscht immer de Vatter; de Jesus Christus wird näbe im gnännt ([[TIT.1.4]])."],
  ["Erschiine", "Retter"]),
 ("INT-TIT-0004", "TU-TIT-002-001-010", ["FIND-TIT-0005"],
  "Die Haustafel übernimmt die damals übliche Ordnung des Hauses und begründet sie mit dem Ruf der Gemeinde: Die Glaubenden sollen keinen Anlass zu Verachtung geben. Sie ist damit an die Gesellschaft ihrer Zeit gebunden.",
  "probable", "Wie weit diese Bindung reicht, ist für die heutige Anwendung entscheidend und umstritten.",
  ["Andere sehen in der Unterordnung der Frauen eine von Gott gegebene, bleibende Ordnung, die nicht nur mit dem Ruf nach aussen begründet ist.",
   "Andere betonen, dass der Text auch die Sklaverei nicht in Frage stellt; wer diese heute ablehnt, liest die Haustafel ohnehin nicht als zeitlose Ordnung."],
  [],
  "D Huustafle übernimmt di damals üblich Ornig vom Huus und begründet si mit em Ruef vo de Gmeind: D Gläubige söled kei Aalass zu Verachtig gää. Si isch drum a d Gsellschaft vo irere Ziit bunde.",
  "Wie wiit die Bindig gaat, isch für di hütig Aawändig entscheidend und umstritte.",
  ["Anderi gsend i de Underornig vo de Fraue e vo Gott gää, bliibendi Ornig, wo nöd nu mit em Ruef gäge usse begründet isch.",
   "Anderi betoned, dass de Text au d Sklaverei nöd i Frag stellt; wär die hüt ablehnt, liest d Huustafle sowiso nöd als ziitlosi Ornig."],
  []),
 ("INT-TIT-0005", "TU-TIT-003-001-007", ["FIND-TIT-0006"],
  "Das «Bad der Wiedergeburt» ([[TIT.3.5]]) meint die Taufe: Gott rettet aus Erbarmen, und die Taufe ist der Ort, an dem dieses Erbarmen dem Einzelnen zugesprochen wird.",
  "probable", "Die Taufe wird im Text nicht ausdrücklich genannt.",
  ["Andere verstehen das «Bad» als Bild für die innere Reinigung durch den Geist, ohne Bezug auf einen Ritus."],
  [("grc", "λουτρόν", "Bad, Waschung"), ("grc", "παλιγγενεσία", "Wiedergeburt, Neuwerden")],
  "S «Bad vo de Widergeburt» ([[TIT.3.5]]) meint d Toufi: Gott rettet us Erbarme, und d Toufi isch de Ort, wo dem Einzelne das Erbarme zuegsproche wird.",
  "D Toufi wird im Text nöd usdrücklich gnännt.",
  ["Anderi verstönd s «Bad» als Bild für di inner Reinigung dur de Geischt, ohni Bezug uf en Ritus."],
  ["Bad, Wäschig", "Widergeburt, Nöiwärde"]),
]

PRINCIPLES = [
 ("PRIN-TIT-0001", ["FIND-TIT-0005", "INT-TIT-0004"],
  "Glaube zeigt sich im gewöhnlichen Alltag und wird an ihm gemessen: Wer Gott zu kennen behauptet, soll es mit seinen Taten nicht verleugnen ([[TIT.1.16]]).", "probable",
  "Glaube zeigt sich im gwöönliche Alltag und wird a dem gmässe: Wär seit, er kenni Gott, söll s mit sine Tate nöd verleugne ([[TIT.1.16]])."),
 ("PRIN-TIT-0002", ["FIND-TIT-0006", "INT-TIT-0005"],
  "Freundlichkeit gegenüber allen Menschen gründet in Gottes Freundlichkeit, nicht in der eigenen Vortrefflichkeit: Auch die Glaubenden waren einmal verirrt ([[TIT.3.2-TIT.3.5]]).", "probable",
  "Fründlichkeit gägenüber allne Mänsche gründet i de Fründlichkeit vo Gott, nöd i de eigete Vortrefflichkeit: Au d Gläubige sind emal verirrt gsii ([[TIT.3.2-TIT.3.5]])."),
]
APPLICATIONS = [
 ("APP-TIT-0001", "PRIN-TIT-0001",
  "Heute kann das heissen: Glaubwürdigkeit entsteht weniger durch richtige Sätze als durch Verlässlichkeit im Kleinen, am Arbeitsplatz, in der Familie, im Umgang mit Geld. Gemeinden können sich fragen, wie sie von aussen wahrgenommen werden.",
  "Der Text gibt keine Liste heutiger Tugenden vor. Die Haustafel selbst ist an die damalige Ordnung des Hauses gebunden und lässt sich nicht einfach übertragen, besonders nicht in Fragen von Frauen und Sklaverei.",
  "Hüt cha das heisse: Glaubwürdigkeit entstaat weniger dur richtigi Sätz als dur Verlässlichkeit im Chliine, am Arbetsplatz, i de Familie, im Umgang mit Gält. Gmeinde chönd sich frage, wie si vo usse wahrgnoo wärded.",
  "De Text git kei Lischte vo hütige Tugende vor. D Huustafle sälber isch a di damalig Ornig vom Huus bunde und laat sich nöd eifach übertrage, bsunders nöd i Frage vo Fraue und Sklaverei."),
 ("APP-TIT-0002", "PRIN-TIT-0002",
  "Wer sich daran erinnert, selbst auf Erbarmen angewiesen zu sein, kann Menschen mit anderen Überzeugungen gelassener und freundlicher begegnen, auch in öffentlichen Debatten.",
  "Freundlichkeit heisst im Titusbrief nicht, alles gutzuheissen: Derselbe Brief verlangt, Irrlehrer scharf zurechtzuweisen ([[TIT.1.13]]).",
  "Wär sich dra erinneret, dass er sälber uf Erbarme agwise isch, cha Mänsche mit andere Überzüügige gelassener und fründlicher begägne, au i öffentliche Debatte.",
  "Fründlichkeit heisst im Titusbrief nöd, alles guetzheisse: De gliich Brief verlangt, Irrlehrer schaarf zrächtzwiise ([[TIT.1.13]])."),
]
QUESTIONS = [
 ("QUESTION-TIT-0001", "TU-TIT-001-001-016",
  "Hat Paulus den Brief an Titus selbst geschrieben, oder stammt er von einem Schüler, der in seinem Namen schrieb?",
  "Wortschatz, Gemeindeordnung und die nicht in die Apostelgeschichte passenden Reisen werden unterschiedlich gewichtet; beide Annahmen werden vertreten.",
  "Hät de Paulus de Brief a de Titus sälber gschribe, oder stammt er vo me Schüeler, wo i sim Name gschribe hät?",
  "Wortschatz, Gmeindsornig und d Reise, wo nöd i d Apostelgschicht passed, wärded verschide gwichtet; beidi Aanaame wärded vertrete."),
 ("QUESTION-TIT-0002", "TU-TIT-001-010-016",
  "Was genau waren die «jüdischen Mythen», «Geschlechtsregister» und «Streitigkeiten um das Gesetz», gegen die der Brief schreibt?",
  "Der Brief beschreibt die Gegner nur knapp; vermutet werden spekulative Auslegungen der Schrift, Reinheitsregeln und Abstammungsfragen.",
  "Was gnau sind di «jüdische Mythe», «Stammbäum» und «Striit ums Gsetz» gsii, gäge die de Brief schriibt?",
  "De Brief beschriibt d Gägner nu knapp; vermuetet wärded spekulativi Uslegige vo de Schrift, Reinheitsregle und Abstammigsfrage."),
]
RELATIONS = [
 ("REL-TIT-0001", "TU-TIT-001-005-009", "1TI.3.1-1TI.3.7", "parallel_list", "high"),
 ("REL-TIT-0002", "TU-TIT-003-001-007", "EPH.2.8-EPH.2.10", "parallel_argument", "probable"),
 ("REL-TIT-0003", "TU-TIT-002-001-010", "COL.3.18-COL.4.1", "parallel_form", "high"),
 ("REL-TIT-0004", "TU-TIT-001-010-016", "ACT.17.28", "motif", "possible"),
 ("REL-TIT-0005", "TU-TIT-003-001-007", "ROM.13.1-ROM.13.7", "parallel_argument", "probable"),
]

# Hintergrund: (id, Abschnitt oder None, Stelle, Kontext, Konfidenz, Thema, Text, unsicher, Belege, Quellen, Fachwörter, scope | Mundart)
BACKGROUND = [
 ("BG-TIT-0001", "TU-TIT-001-005-009", "TIT.1.5", "CTX-TIT-READERS", "probable", "Kreta im 1. Jahrhundert",
  "Kreta wurde 67 v. Chr. römisch und bildete später mit der Kyrenaika (im heutigen Libyen) eine Provinz; Hauptstadt war Gortyn. Auf der Insel lebten auch Juden; Kreter werden unter den Zuhörern zu Pfingsten genannt ([[ACT.2.11]]). Die Apostelgeschichte erzählt nur, dass Paulus als Gefangener auf dem Weg nach Rom entlang der Südküste Kretas segelte und in Kaloi Limenes anlegte ([[ACT.27.7-ACT.27.13]]); von einer Mission dort berichtet sie nichts.",
  "Wann Paulus und Titus auf Kreta wirkten, ist unbekannt. Wer den Brief Paulus selbst zuschreibt, nimmt meist eine Reise nach einer Freilassung aus der ersten römischen Haft an.",
  ["ACT.2.11", "ACT.27.7-ACT.27.13"], [], [],
  "Kreta im 1. Jaarhundert",
  "Kreta isch 67 v. Chr. römisch worde und hät spööter mit de Kyrenaika (im hütige Libye) e Provinz bildet; Hauptstadt isch Gortyn gsii. Uf de Insle händ au Jude gläbt; Kreter wärded under de Zuehörer a Pfingschte gnännt ([[ACT.2.11]]). D Apostelgschicht verzellt nu, dass de Paulus als Gfangene uf em Wäg uf Rom de Südküscht vo Kreta naa gsäglet isch und z Kaloi Limenes aagleit hät ([[ACT.27.7-ACT.27.13]]); vo ere Mission dört brichtet si nüt.",
  "Wänn de Paulus und de Titus uf Kreta gwürkt händ, weiss me nöd. Wär de Brief em Paulus sälber zueschriibt, nimmt meischtens e Reis nach ere Freilassig us de erschte römische Haft aa.", []),
 ("BG-TIT-0002", "TU-TIT-001-010-016", "TIT.1.12", "CTX-TIT-READERS", "probable", "Der Ruf der Kreter",
  "Bei den Griechen hiess «kretisieren» so viel wie lügen. Ein Grund war, dass die Kreter ein Grab des Zeus auf ihrer Insel zeigten, was anderen Griechen als Lüge über einen unsterblichen Gott galt; der Dichter Kallimachos wirft ihnen das mit denselben Anfangsworten vor wie [[TIT.1.12]]. Der Brief nutzt das bekannte Vorurteil, um die Gegner zu kennzeichnen.",
  "Wie ernst das Zitat gemeint ist und ob es ironisch die Lage der Gemeinde spiegelt, wird unterschiedlich beurteilt.",
  ["TIT.1.12-TIT.1.13"], ["Kallimachos, Hymnos auf Zeus 8"], [("grc", "κρητίζω", "kretisieren: lügen, täuschen")],
  "De Ruef vo de Kreter",
  "Bi de Grieche hät «kretisiere» so vil gheisse wie lüge. En Grund isch gsii, dass d Kreter es Grab vom Zeus uf irere Insle zeigt händ, was andere Grieche als Lugi über en unsterbliche Gott gulte hät; de Dichter Kallimachos wirft ine das mit de gliiche Aafangswörter vor wie [[TIT.1.12]]. De Brief bruucht das bekannte Vorurteil, zum d Gägner z kännzeichne.",
  "Wie ärnscht s Zitat gmeint isch und öb s ironisch d Lag vo de Gmeind spieglet, wird verschide beurteilt.", ["kretisiere: lüge, tüüsche"]),
 ("BG-TIT-0003", "TU-TIT-002-001-010", "TIT.2.2", "CTX-TIT-READERS", "high", "Das antike Haus",
  "Grundeinheit der antiken Gesellschaft war das Haus: der Hausherr, seine Frau, Kinder, Sklaven und oft weitere Angehörige. Philosophen wie Aristoteles beschrieben die richtige Ordnung des Hauses nach den Paaren Mann und Frau, Vater und Kind, Herr und Sklave. Solche «Haustafeln» übernehmen auch [[COL.3.18-COL.4.1]], [[EPH.5.21-EPH.6.9]] und [[1PE.2.18-1PE.3.7]]. Die Gemeinden versammelten sich in Häusern.",
  None, ["COL.3.18-COL.4.1", "EPH.5.21-EPH.6.9", "1PE.2.18-1PE.3.7"], ["Aristoteles, Politik, Buch 1"], [("grc", "οἶκος", "Haus, Haushalt")],
  "S antike Huus",
  "D Grundeinheit vo de antike Gsellschaft isch s Huus gsii: de Huusherr, sini Frau, Chind, Sklave und oft no wiiteri Aaghörigi. Philosophe wie de Aristoteles händ di richtig Ornig vom Huus nach de Paar Maa und Frau, Vatter und Chind, Herr und Sklav beschribe. Sonigi «Huustafle» übernämed au [[COL.3.18-COL.4.1]], [[EPH.5.21-EPH.6.9]] und [[1PE.2.18-1PE.3.7]]. D Gmeinde händ sich i Hüüser versammlet.",
  None, ["Huus, Hushalt"]),
 ("BG-TIT-0004", "TU-TIT-002-011-015", "TIT.2.11", "CTX-TIT-READERS", "probable", "«Erscheinung» und «Retter»: Wörter aus der Herrscherverehrung",
  "«Erscheinung» (ἐπιφάνεια) und «Retter» (σωτήρ) waren im östlichen Mittelmeer geläufige Titel für Götter und Herrscher: Ein König nannte sich «Epiphanes» («der Erschienene»), Städte ehrten Kaiser in Inschriften als «Retter». Der Brief gebraucht dieselben Wörter für Gott und Jesus Christus.",
  "Ob der Brief damit bewusst der Herrscherverehrung widerspricht, ist umstritten; die Wörter stammen auch aus der griechischen Bibel.",
  ["TIT.2.11", "TIT.2.13", "TIT.3.4"], [], [("grc", "ἐπιφάνεια", "Erscheinung"), ("grc", "σωτήρ", "Retter")],
  "«Erschiinig» und «Retter»: Wörter us de Verehrig vo Herrscher",
  "«Erschiinig» (ἐπιφάνεια) und «Retter» (σωτήρ) sind im öschtliche Mittelmeer gläufigi Titel für Götter und Herrscher gsii: En König hät sich «Epiphanes» («de Erschineni») gnännt, Stedt händ Kaiser i Inschrifte als «Retter» gehrt. De Brief bruucht di gliiche Wörter für Gott und Jesus Christus.",
  "Öb de Brief dermit bewusst de Verehrig vo Herrscher widerspricht, isch umstritte; d Wörter stammed au us de griechische Bible.", ["Erschiinig", "Retter"]),
 ("BG-TIT-0005", "TU-TIT-003-012-015", "TIT.3.12", "CTX-TIT-READERS", "probable", "Nikopolis, Winter und Mitarbeiter",
  "Gemeint ist wohl Nikopolis in Epirus (Nordwestgriechenland), das Augustus nach seinem Sieg bei Actium (31 v. Chr.) gegründet hatte; es gab aber mehrere Städte dieses Namens. Im Winter ruhte die Schifffahrt auf dem offenen Meer weitgehend. Tychikus ist aus [[ACT.20.4]] und [[COL.4.7]] bekannt, Apollos aus [[ACT.18.24-ACT.18.28]] und [[1CO.3.4-1CO.3.6]]; Artemas und Zenas werden sonst nirgends erwähnt.",
  "Welches Nikopolis gemeint ist, lässt sich nicht sicher sagen.",
  ["ACT.20.4", "COL.4.7", "ACT.18.24-ACT.18.28", "1CO.3.4-1CO.3.6"], [], [],
  "Nikopolis, Winter und Mitarbeiter",
  "Gmeint isch wahrschiinli Nikopolis im Epirus (Nordweschtgriecheland), wo de Augustus nach sim Sieg bi Actium (31 v. Chr.) gründet hät; es hät aber meereri Stedt mit dem Name gää. Im Winter hät d Schiffaart uf em offene Meer wiitgehend gruet. De Tychikus kännt me us [[ACT.20.4]] und [[COL.4.7]], de Apollos us [[ACT.18.24-ACT.18.28]] und [[1CO.3.4-1CO.3.6]]; de Artemas und de Zenas wärded süscht niene erwäänt.",
  "Weles Nikopolis gmeint isch, cha me nöd sicher säge.", []),
 ("BG-TIT-0006", "TU-TIT-003-001-007", "TIT.3.1", "CTX-TIT-READERS", "probable", "Christen und Behörden",
  "Die Gemeinden waren kleine, oft beargwöhnte Gruppen in den Städten des Reiches. Wie [[ROM.13.1-ROM.13.7]] und [[1PE.2.13-1PE.2.17]] verlangt der Brief, sich in die öffentliche Ordnung einzufügen und allen Menschen freundlich zu begegnen. Eine planmässige Verfolgung im ganzen Reich gab es im 1. Jahrhundert noch nicht.",
  "Wie stark die Gemeinden auf Kreta unter Druck standen, ist nicht bekannt.",
  ["ROM.13.1-ROM.13.7", "1PE.2.13-1PE.2.17"], [], [],
  "Christe und Behörde",
  "D Gmeinde sind chliini, oft beargwöönti Gruppe i de Stedt vom Riich gsii. Wie [[ROM.13.1-ROM.13.7]] und [[1PE.2.13-1PE.2.17]] verlangt de Brief, sich i di öffentlich Ornig iizfüege und allne Mänsche fründlich z begägne. E planmässigi Verfolgig im ganze Riich hät s im 1. Jaarhundert no nöd gää.",
  "Wie stark d Gmeinde uf Kreta under Druck gstande sind, weiss me nöd.", []),
 ("BG-TIT-BOOK-0001", None, "TIT", "CTX-TIT-READERS", "possible", "Wer schrieb an Titus und wann?",
  "Der Titusbrief gehört mit den beiden Briefen an Timotheus zu den «Pastoralbriefen», wie man sie seit dem 18. Jahrhundert nennt. Sie unterscheiden sich in Wortschatz, Stil und Gemeindeordnung von den übrigen Paulusbriefen, und die vorausgesetzten Reisen passen nicht in die Apostelgeschichte. Vertreten werden: Paulus schrieb selbst, etwa 63–65 n. Chr. nach einer Freilassung aus römischer Haft; Paulus schrieb mit Hilfe eines Sekretärs; oder ein Schüler schrieb später (etwa 80–110 n. Chr.) in seinem Namen, um sein Erbe für neue Fragen zu bewahren.",
  "Keine dieser Annahmen ist bewiesen; die Entscheidung hängt davon ab, wie man Stilunterschiede und Gemeindeordnung gewichtet.",
  [], [], [],
  "Wär hät am Titus gschribe und wänn?",
  "De Titusbrief ghört mit de beide Brief a de Timotheus zu de «Pastoralbrief», wie me si sit em 18. Jaarhundert nännt. Si underscheided sich i Wortschatz, Stil und Gmeindsornig vo de andere Paulusbrief, und d Reise, wo voruusgsetzt sind, passed nöd i d Apostelgschicht. Vertrete wird: De Paulus hät sälber gschribe, öppe 63–65 n. Chr. nach ere Freilassig us de römische Haft; de Paulus hät mit Hilf vo me Sekretär gschribe; oder en Schüeler hät spööter (öppe 80–110 n. Chr.) i sim Name gschribe, zum sis Erb für nöii Frage z bewaare.",
  "Keini vo dene Aanaame isch bewise; d Entscheidig hangt devo ab, wie me Stilunderschid und Gmeindsornig gwichtet.", []),
 ("BG-TIT-BOOK-0002", None, "TIT", "CTX-TIT-READERS", "probable", "Titus, der Mitarbeiter",
  "Titus war ein unbeschnittener griechischer Christ, den Paulus zum Treffen nach Jerusalem mitnahm ([[GAL.2.1-GAL.2.3]]). Er vermittelte im Streit mit der Gemeinde in Korinth und organisierte die Sammlung für Jerusalem ([[2CO.7.6-2CO.7.7]]; [[2CO.8.16-2CO.8.17]]). Später wird er in Dalmatien erwähnt ([[2TI.4.10]]). Die Apostelgeschichte nennt ihn nicht.",
  None, ["GAL.2.1-GAL.2.3", "2CO.7.6-2CO.7.7", "2CO.8.16-2CO.8.17", "2TI.4.10"], [], [],
  "De Titus, de Mitarbeiter",
  "De Titus isch en unbeschnittene griechische Christ gsii, wo de Paulus as Träffe uf Jerusalem mitgnoo hät ([[GAL.2.1-GAL.2.3]]). Er hät im Striit mit de Gmeind z Korinth vermittlet und d Sammlig für Jerusalem organisiert ([[2CO.7.6-2CO.7.7]]; [[2CO.8.16-2CO.8.17]]). Spööter wird er z Dalmatie erwäänt ([[2TI.4.10]]). D Apostelgschicht nännt en nöd.",
  None, []),
]

SUMMARIES = [
 ("SUM-CH-TIT-001", "Paulus beauftragt Titus, auf Kreta Älteste einzusetzen, die glaubwürdig leben und an der gesunden Lehre festhalten, und Lehrer zurechtzuweisen, die aus Gewinnsucht Familien verwirren.",
  "De Paulus git em Titus de Uftrag, uf Kreta Ältischti iizsetze, wo glaubwürdig läbed und a de gsunde Lehr fescht haltet, und Lehrer zrächtzwiise, wo us Gwünnsucht Familie durenand bringed."),
 ("SUM-CH-TIT-002", "Was der gesunden Lehre entspricht, zeigt sich im Alltag von Alten und Jungen, Frauen, Männern und Sklaven. Grund dafür ist die erschienene Gnade Gottes, die zu einem besonnenen Leben erzieht.",
  "Was de gsunde Lehr entspricht, zeigt sich im Alltag vo Alte und Junge, Fraue, Mane und Sklave. De Grund defür isch d Gnad vo Gott, wo erschine isch und zu me bsunnene Läbe erziet."),
 ("SUM-CH-TIT-003", "Die Gemeinde soll allen Menschen freundlich begegnen, weil Gott sie nicht wegen ihrer Werke, sondern aus Erbarmen gerettet hat. Unnütze Streitfragen soll Titus meiden. Reisepläne und Grüsse schliessen den Brief.",
  "D Gmeind söll allne Mänsche fründlich begägne, wil Gott si nöd wäge irne Wärch, sondern us Erbarme grettet hät. Unnützi Striitfrage söll de Titus meide. Reiseplän und Grüess schlüüssed de Brief ab."),
]


def run():
    from _study import write_study
    write_study({"TAGS": TAGS, "CONTEXT": CONTEXT, "FINDINGS": FINDINGS, "INTERPRETATIONS": INTERPRETATIONS,
                 "PRINCIPLES": PRINCIPLES, "APPLICATIONS": APPLICATIONS, "QUESTIONS": QUESTIONS, "RELATIONS": RELATIONS,
                 "BACKGROUND": BACKGROUND, "SUMMARIES": SUMMARIES,
                 "STUDY": ("STUDY-TIT-0001", "Titusbrief: ganzes Buch als Muster", "TU-TIT-001-001-016",
                           ["TRANS-TIT-001-001-016-DE-WORKING", "TRANS-TIT-002-001-015-DE-WORKING", "TRANS-TIT-003-001-015-DE-WORKING",
                            "TRANS-TIT-001-001-016-GSW-ZH-WORKING", "TRANS-TIT-002-001-015-GSW-ZH-WORKING", "TRANS-TIT-003-001-015-GSW-ZH-WORKING"],
                           ["Mundart muttersprachlich prüfen", "Weitere Handschriften (z. B. D 06, F 010, G 012) mit freien Transkriptionen ergänzen",
                            "Fachliche Prüfung der Deutungen und des Hintergrunds"])}, "Titus")


if __name__ == "__main__":
    run()
