#!/usr/bin/env python3
"""Autorenwerkzeug: Obadja – Befunde, Deutungen, Grundsätze, Anwendungen, offene Fragen, Beziehungen, Hintergrund
(Abschnitte und Buch), Kapitel-Zusammenfassung, Kontext und Studie; jeweils mit Züridüütsch-Lokalisierung.

Aufruf: python3 scripts/authoring/obadja_study.py
KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

TAGS = ["TAG-OBADIAH"]
CONTEXT = {"id": "CTX-OBA-AFTER-587", "type": "context", "status": "draft", "tags": TAGS + ["TAG-UNCERTAINTY"],
           "period": {"from": -587, "to": -500, "era": "BCE", "approx": True}, "region": "Juda und Edom",
           "language_context": ["he"], "audience": "Judäer nach der Zerstörung Jerusalems durch die Babylonier",
           "note_de": "Die meisten Ausleger datieren das Buch bald nach 587/586 v. Chr.; frühere und spätere Ansetzungen werden ebenfalls vertreten."}

FINDINGS = [
 ("FIND-OBA-0001", "TU-OBA-001-001-021", "form",
  "Obadja ist mit 21 Versen das kürzeste Buch des Alten Testaments. Es richtet sich fast ganz gegen ein einziges Volk, Edom.",
  ["OBA.1.1-OBA.1.21"], "high", "Zählung nach dem Westminster Leningrad Codex.",
  "De Obadja isch mit 21 Värs s chürzischt Buech vom Alte Teschtamänt. Es richtet sich fascht ganz gäge es einzigs Volk, Edom.",
  "Zellig nach em Westminster Leningrad Codex."),
 ("FIND-OBA-0002", "TU-OBA-001-001-004", "parallel_text",
  "Die Verse 1–5 stimmen teilweise wörtlich mit [[JER.49.14-JER.49.16]] und [[JER.49.9]] überein, dort ebenfalls in einem Wort gegen Edom.",
  ["OBA.1.1-OBA.1.5", "JER.49.9", "JER.49.14-JER.49.16"], "high", "Vergleich der hebräischen Texte; Reihenfolge und Einzelheiten weichen ab.",
  "D Värs 1–5 stimmed teilwiis wörtlich mit [[JER.49.14-JER.49.16]] und [[JER.49.9]] überii, dört au i me Wort gäge Edom.",
  "Vergliich vo de hebräische Text; Reiefolg und Einzelheite wiiched ab."),
 ("FIND-OBA-0003", "TU-OBA-001-010-014", "repetition",
  "In den Versen 11–14 steht «Tag» zehnmal, meist als «am Tag …» mit einem Wort für Unheil (Unglück, Untergang, Not, Verderben). Dazwischen stehen acht Verbote «nicht …»: nicht zuschauen (zweimal), sich nicht freuen, nicht prahlen, nicht eindringen, nicht plündern, nicht auflauern, nicht ausliefern.",
  ["OBA.1.11-OBA.1.14"], "high", "Zählung nach den MACULA-Lemmata (Lemma «Tag» 10-mal in V. 11–14).",
  "I de Värs 11–14 staat «Taag» zää Mal, meischtens als «am Taag …» mit eme Wort für Unheil (Unglück, Undergang, Not, Verderbe). Dezwüsche stönd acht Verbot «nöd …»: nöd zueluege (zwei Mal), sich nöd fröie, nöd prahle, nöd iidringe, nöd plündere, nöd uflaure, nöd uslifere.",
  "Zellig nach de MACULA-Lemmata (Lemma «Taag» 10 Mal i V. 11–14)."),
 ("FIND-OBA-0004", "TU-OBA-001-015-018", "argument_structure",
  "[[OBA.1.15]] fasst das Gericht in einer Entsprechungsregel zusammen: «Wie du getan hast, wird dir getan werden». Was Edom nach V. 10–14 getan hat, fällt auf es zurück.",
  ["OBA.1.10-OBA.1.15"], "high", "Beobachtung am Wortlaut.",
  "[[OBA.1.15]] fasst s Gricht i ere Regle zäme: «Wie du gmacht häsch, wird mit dir gmacht». Was Edom nach V. 10–14 gmacht hät, fallt uf s zrugg.",
  "Beobachtig am Wortluut."),
 ("FIND-OBA-0005", "TU-OBA-001-001-021", "names",
  "Edom heisst auch «Esau» (siebenmal) und wird «dein Bruder Jakob» gegenübergestellt ([[OBA.1.10]]; vgl. «dein Bruder» in [[OBA.1.12]]). Das erinnert an die Zwillingsbrüder Jakob und Esau ([[GEN.25.23-GEN.25.26]]); Esau gilt als Stammvater Edoms ([[GEN.36.1]]).",
  ["OBA.1.10", "OBA.1.12", "GEN.25.23-GEN.25.26", "GEN.36.1"], "high", "Beobachtung am Wortlaut.",
  "Edom heisst au «Esau» (sibe Mal) und wird «dim Brueder Jakob» gägenüberstellt ([[OBA.1.10]]; vgl. «din Brueder» i [[OBA.1.12]]). Das erinneret a d Zwillingsbrüeder Jakob und Esau ([[GEN.25.23-GEN.25.26]]); de Esau gilt als Stammvatter vo Edom ([[GEN.36.1]]).",
  "Beobachtig am Wortluut."),
 ("FIND-OBA-0006", "TU-OBA-001-001-004", "argument_structure",
  "Edoms Selbstgespräch «Wer stürzt mich zu Boden?» ([[OBA.1.3]]) beantwortet Gott im nächsten Vers: «von dort stürze ich dich hinab» ([[OBA.1.4]]). Beide Male steht dasselbe hebräische Verb «hinabbringen».",
  ["OBA.1.3-OBA.1.4"], "high", "Beobachtung am Wortlaut (Verb ירד im Kausativstamm).",
  "Edom fröget sich sälber «Wär stürzt mich uf de Bode?» ([[OBA.1.3]]), und Gott antwortet im nööchschte Värs: «vo dört stürz ich dich abe» ([[OBA.1.4]]). Beidi Mal staat s gliich hebräisch Verb «abebringe».",
  "Beobachtig am Wortluut (Verb ירד im Kausativstamm)."),
]

INTERPRETATIONS = [
 ("INT-OBA-0001", "TU-OBA-001-010-014", ["FIND-OBA-0003"],
  "Die Verse 11–14 meinen die Eroberung Jerusalems durch die Babylonier 587/586 v. Chr., bei der Edomiter nach anderen Stellen Partei gegen Juda ergriffen ([[PSA.137.7]]; [[LAM.4.21-LAM.4.22]]; [[EZK.25.12-EZK.25.14]]).",
  "probable", "Babylon wird im Buch nicht genannt.",
  ["Wer früh datiert, denkt an die Zeit Jorams: Edom fiel damals von Juda ab ([[2KI.8.20-2KI.8.22]]), und Jerusalem wurde von Philistern und Arabern überfallen ([[2CH.21.16-2CH.21.17]]).",
   "Die jüdische Überlieferung im Talmud setzt Obadja mit dem Hofbeamten Obadja zur Zeit Ahabs gleich ([[1KI.18.3-1KI.18.4]]) und datiert das Buch damit viel früher."],
  [],
  "D Värs 11–14 meined d Eroberig vo Jerusalem dur d Babylonier 587/586 v. Chr., wo Edomiter nach andere Stelle gäge Juda Partei gnoo händ ([[PSA.137.7]]; [[LAM.4.21-LAM.4.22]]; [[EZK.25.12-EZK.25.14]]).",
  "Babylon wird im Buech nöd gnännt.",
  ["Wär früe datiert, dänkt a d Ziit vom Joram: Edom isch dänn vo Juda abgfalle ([[2KI.8.20-2KI.8.22]]), und Jerusalem isch vo Philischter und Araber überfalle worde ([[2CH.21.16-2CH.21.17]]).",
   "Di jüdisch Überlieferig im Talmud setzt de Obadja em Hofbeamte Obadja us de Ziit vom Ahab gliich ([[1KI.18.3-1KI.18.4]]) und datiert s Buech dermit vil früener."],
  []),
 ("INT-OBA-0002", "TU-OBA-001-010-014", ["FIND-OBA-0003"],
  "Die Verbote «schau nicht …, freu dich nicht …» sind ein rhetorisches Mittel: Sie schildern, was Edom getan hat, so, als würde es noch davor gewarnt. Dadurch wird jede einzelne Tat vor Augen gestellt.",
  "probable", "Grammatisch sind es Verbote (אַל mit Jussiv); die Deutung als Rückblick stützt sich auf den Zusammenhang ([[OBA.1.11]]; [[OBA.1.15]]).",
  ["Wer das Buch früh datiert, liest die Verse als Warnung vor einer Tat, die noch bevorsteht."],
  [("heb", "אַל", "nicht (Verbot)", "al")],
  "D Verbot «lueg nöd …, fröi dich nöd …» sind es rhetorischs Mittel: Si schildered, was Edom gmacht hät, wie wänn s no devor gwarnt würd. Dur das wird jedi einzelni Tat vor Auge gstellt.",
  "Grammatisch sind s Verbot (אַל mit Jussiv); d Düütig als Ruggblick stützt sich uf de Zämehang ([[OBA.1.11]]; [[OBA.1.15]]).",
  ["Wär s Buech früe datiert, liest d Värs als Warnig vor ere Tat, wo no bevorstaat."],
  ["nöd (Verbot)"]),
 ("INT-OBA-0003", "TU-OBA-001-015-018", ["FIND-OBA-0004", "FIND-OBA-0005"],
  "Edom steht im Buch nicht nur für ein Nachbarvolk, sondern beispielhaft für alle Völker, die am Tag JHWHs gerichtet werden ([[OBA.1.15-OBA.1.16]]). Spätere jüdische Ausleger haben «Edom» auf Rom bezogen.",
  "possible", "Der Übergang von Edom zu «allen Völkern» in V. 15 kann auch eine spätere Erweiterung des Buches sein.",
  ["Andere betonen, dass das Buch konkret bleibt: Es geht um die Schuld eines bestimmten Nachbarn an einem bestimmten Tag."],
  [("heb", "יוֹם יְהוָה", "Tag JHWHs", "jom JHWH")],
  "Edom staat im Buech nöd nu für es Nochbervolk, sondern bispilhaft für alli Völker, wo am Taag vo JHWH grichtet wärded ([[OBA.1.15-OBA.1.16]]). Spööteri jüdischi Usleger händ «Edom» uf Rom bezoge.",
  "De Überggang vo Edom zu «allne Völker» i V. 15 cha au e spööteri Erwiiterig vom Buech sii.",
  ["Anderi betoned, dass s Buech konkret bliibt: Es gaat um d Schuld vo me bestimmte Nochber a me bestimmte Taag."],
  ["Taag vo JHWH"]),
 ("INT-OBA-0004", "TU-OBA-001-019-021", ["FIND-OBA-0004"],
  "Der Schluss «die Königsherrschaft wird JHWH gehören» ([[OBA.1.21]]) stellt die Rückgewinnung des Landes unter Gottes Herrschaft: Ziel ist nicht Israels Vorherrschaft, sondern dass Gott König ist.",
  "possible", "Die Verse 19–21 beschreiben zugleich eine Ausdehnung des Landes und ein Gericht über Esau.",
  ["Kritische Stimmen sehen in den Versen einen Ausdruck nationaler Hoffnung und Vergeltung, der nicht durch den letzten Satz entschärft wird."],
  [("heb", "מְלוּכָה", "Königsherrschaft", "melucha")],
  "De Schluss «d Königsherrschaft wird em JHWH ghöre» ([[OBA.1.21]]) stellt d Ruggwinnig vom Land under d Herrschaft vo Gott: S Ziil isch nöd d Vorherrschaft vo Israel, sondern dass Gott König isch.",
  "D Värs 19–21 beschriibed zuegliich e Usdeenig vom Land und es Gricht über de Esau.",
  ["Kritischi Stimme gsend i de Värs en Usdruck vo nationaler Hoffnig und Vergeltig, wo dur de letscht Satz nöd entschärft wird."],
  ["Königsherrschaft"]),
]

PRINCIPLES = [
 ("PRIN-OBA-0001", ["FIND-OBA-0003", "INT-OBA-0002"],
  "Wer bei der Not eines Nahestehenden zuschaut, sich freut oder davon profitiert, ist nicht unbeteiligt: «auch du warst wie einer von ihnen» ([[OBA.1.11]]).", "probable",
  "Wär bi de Not vo me Nööchstehende zueluegt, sich fröit oder devo profitiert, isch nöd unbeteiliget: «au du bisch wie eine vo ine gsii» ([[OBA.1.11]])."),
 ("PRIN-OBA-0002", ["FIND-OBA-0006"],
  "Hochmut und das Gefühl, unangreifbar zu sein, sind keine Sicherheit ([[OBA.1.3-OBA.1.4]]).", "probable",
  "Hochmuet und s Gfüül, unaagriifbar z sii, sind kei Sicherheit ([[OBA.1.3-OBA.1.4]])."),
]
APPLICATIONS = [
 ("APP-OBA-0001", "PRIN-OBA-0001",
  "Heute kann das heissen: Schadenfreude über das Unglück anderer, auch in sozialen Medien, und schweigendes Zuschauen bei Unrecht in der Nachbarschaft oder unter Bekannten sind nicht harmlos.",
  "Obadja spricht von Völkern im Krieg; der Text lässt sich nicht einfach auf persönliche Beziehungen übertragen. Er darf auch nicht dazu dienen, heutige Völker als «Edom» zu brandmarken oder Rache zu rechtfertigen.",
  "Hüt cha das heisse: Schadefreud über s Unglück vo andere, au i soziale Medie, und schwiigends Zueluege bi Unrächt i de Nochberschaft oder under Bekannte sind nöd harmlos.",
  "De Obadja redt vo Völker im Chrieg; de Text laat sich nöd eifach uf persönlichi Beziehige übertrage. Er dörf au nöd defür bruucht wärde, hütigi Völker als «Edom» z brandmarke oder Rach z rächtfertige."),
 ("APP-OBA-0002", "PRIN-OBA-0002",
  "Wer sich sicher fühlt, weil er stark, reich oder gut vernetzt ist, kann sich an Edom erinnern: Gerade die Verbündeten haben es getäuscht ([[OBA.1.7]]).",
  "Das ist eine Übertragung; der Text spricht vom Gericht Gottes über ein Volk, nicht von Lebensklugheit.",
  "Wär sich sicher füült, wil er starch, riich oder guet vernetzt isch, cha sich a Edom erinnere: Grad d Verbündete händ s tüüscht ([[OBA.1.7]]).",
  "Das isch e Übertragig; de Text redt vom Gricht vo Gott über es Volk, nöd vo Läbesklugheit."),
]
QUESTIONS = [
 ("QUESTION-OBA-0001", "TU-OBA-001-001-021", "Wann ist das Buch Obadja entstanden?",
  "Meist wird es bald nach 587/586 v. Chr. angesetzt; vertreten werden aber auch das 9. Jahrhundert v. Chr. und eine spätere Bearbeitung in persischer Zeit.",
  "Wänn isch s Buech Obadja entstande?",
  "Meischtens wird s bald nach 587/586 v. Chr. aagsetzt; vertrete wärded aber au s 9. Jaarhundert v. Chr. und e spööteri Bearbeitig i persischer Ziit."),
 ("QUESTION-OBA-0002", "TU-OBA-001-001-004", "Hat Obadja aus Jeremia 49 geschöpft, Jeremia aus Obadja, oder beide aus einem älteren Spruch gegen Edom?",
  "Alle drei Möglichkeiten werden vertreten; der Wortlaut allein entscheidet die Frage nicht.",
  "Hät de Obadja us em Jeremia 49 gschöpft, de Jeremia us em Obadja, oder beidi us eme eltere Spruch gäge Edom?",
  "Alli drüü Möglichkeite wärded vertrete; de Wortluut elei entscheidet d Frag nöd."),
]
RELATIONS = [
 ("REL-OBA-0001", "TU-OBA-001-001-004", "JER.49.14-JER.49.16", "parallel_text", "high"),
 ("REL-OBA-0002", "TU-OBA-001-005-009", "JER.49.9-JER.49.10", "parallel_text", "high"),
 ("REL-OBA-0003", "TU-OBA-001-010-014", "PSA.137.7", "same_event", "probable"),
 ("REL-OBA-0004", "TU-OBA-001-001-021", "GEN.25.19-GEN.25.34", "background", "high"),
 ("REL-OBA-0005", "TU-OBA-001-015-018", "JOL.2.32", "parallel_text", "probable"),
 ("REL-OBA-0006", "TU-OBA-001-001-021", "AMO.9.12", "canonical_context", "probable"),
]

BACKGROUND = [
 ("BG-OBA-0001", "TU-OBA-001-001-004", "OBA.1.3", "CTX-OBA-AFTER-587", "probable", "Edom und seine Felsen",
  "Edom lag südöstlich des Toten Meeres in einem Bergland aus rotem Sandstein mit schwer zugänglichen Höhen; Hauptstadt war Bozra. Durch das Land führten Handelswege. Die Lage galt als sicher, daran knüpft «der du wohnst in den Klüften des Felsens» an.",
  "Ob mit «Sela» ein bestimmter Ort gemeint ist, ist offen. Vorgeschlagen werden die edomitische Siedlung auf dem Umm el-Biyara im Talkessel des späteren Petra und es-Sela bei Bozra; Petra selbst ist eine jüngere Gründung der Nabatäer.",
  ["OBA.1.3", "GEN.36.33", "JER.49.13"], [], [("heb", "סֶלַע", "Fels; vielleicht Ortsname Sela", "sela")],
  "Edom und sini Felse",
  "Edom isch südöschtlich vom Toote Meer gläge, i me Bärgland us rootem Sandstei mit schwär zuegängliche Hööchine; Hauptstadt isch Bozra gsii. Dur s Land händ Handelswääg gfüert. D Lag hät als sicher gulte, und dra chnüpft «du, wo wohnsch i de Chlüft vom Fels» aa.",
  "Öb mit «Sela» en bestimmte Ort gmeint isch, isch offe. Vorgschlage wärded di edomitisch Siidlig uf em Umm el-Biyara im Talkessel vom spöötere Petra und es-Sela bi Bozra; Petra sälber isch e jüngeri Gründig vo de Nabatäer.", ["Fels; vilicht Ortsname Sela"]),
 ("BG-OBA-0002", "TU-OBA-001-010-014", "OBA.1.11", "CTX-OBA-AFTER-587", "probable", "Edom und der Untergang Jerusalems",
  "Als die Babylonier 587/586 v. Chr. Jerusalem eroberten, standen die Edomiter nach mehreren biblischen Stellen auf der Seite der Sieger ([[PSA.137.7]]; [[EZK.35.10-EZK.35.15]]). Danach siedelten Edomiter im Süden Judas; das Gebiet hiess später Idumäa. Eine Tonscherbe aus der judäischen Festung Arad warnt schon vor 587 davor, dass «Edom kommen» könnte.",
  "Wie weit sich Edom aktiv an der Eroberung beteiligte, lässt sich ausserhalb der Bibel nicht nachweisen.",
  ["PSA.137.7", "EZK.35.10-EZK.35.15", "LAM.4.21-LAM.4.22"], ["Arad-Ostrakon 24 (um 600 v. Chr.)"], [],
  "Edom und de Undergang vo Jerusalem",
  "Wo d Babylonier 587/586 v. Chr. Jerusalem eroberet händ, sind d Edomiter nach meerere biblische Stelle uf de Siite vo de Sieger gstande ([[PSA.137.7]]; [[EZK.35.10-EZK.35.15]]). Dänn händ Edomiter im Süde vo Juda gsidlet; s Gebiet hät spööter Idumäa gheisse. E Tonschärbe us de judäische Feschtig Arad warnt scho vor 587 devor, dass «Edom chönnt cho».",
  "Wie wiit sich Edom aktiv a de Eroberig beteiliget hät, cha me usserhalb vo de Bible nöd naawiise.", []),
 ("BG-OBA-0003", "TU-OBA-001-005-009", "OBA.1.8", "CTX-OBA-AFTER-587", "high", "Die Weisheit Edoms und Teman",
  "Edom war für seine Weisheit bekannt ([[JER.49.7]]); Elifas, einer der Freunde Hiobs, stammt aus Teman ([[JOB.2.11]]). Teman ist ein Landesteil oder eine Sippe Edoms ([[GEN.36.11]]) und steht in V. 9 für das ganze Land. Darauf spielt die Drohung an, die Weisen Edoms zu vernichten.",
  None, ["JER.49.7", "JOB.2.11", "GEN.36.11"], [], [],
  "D Wiisheit vo Edom und Teman",
  "Edom isch für sini Wiisheit bekannt gsii ([[JER.49.7]]); de Elifas, eine vo de Fründ vom Hiob, stammt us Teman ([[JOB.2.11]]). Teman isch en Landesteil oder e Sippe vo Edom ([[GEN.36.11]]) und staat i V. 9 für s ganz Land. Druf spilt d Droohig aa, d Wiise vo Edom z vernichte.",
  None, []),
 ("BG-OBA-0004", "TU-OBA-001-015-018", "OBA.1.16", "CTX-OBA-AFTER-587", "high", "Der Becher des Gerichts",
  "«Trinken» ist bei den Propheten ein Bild für das Gericht: Gott reicht den Völkern einen Becher, den sie leeren müssen ([[JER.25.15-JER.25.29]]); auch Edom wird ihn trinken ([[LAM.4.21]]). «Ihr» in V. 16 kann Juda meinen, das den Becher schon getrunken hat, oder Edom, das auf dem Zion gefeiert hat.",
  "Wer mit «ihr» gemeint ist, ist umstritten.",
  ["JER.25.15-JER.25.29", "LAM.4.21"], [], [],
  "De Becher vom Gricht",
  "«Trinke» isch bi de Prophete es Bild für s Gricht: Gott git de Völker en Becher, wo si müend lääre ([[JER.25.15-JER.25.29]]); au Edom wird en trinke ([[LAM.4.21]]). «Ir» i V. 16 cha Juda meine, wo de Becher scho trunke hät, oder Edom, wo uf em Zion gfiiret hät.",
  "Wär mit «ir» gmeint isch, isch umstritte.", []),
 ("BG-OBA-0005", "TU-OBA-001-019-021", "OBA.1.20", "CTX-OBA-AFTER-587", "possible", "Verbannte in der Ferne: Sarepta und Sefarad",
  "Sarepta war eine phönizische Stadt bei Sidon ([[1KI.17.9]]). Wo Sefarad lag, ist unbekannt; oft wird an Sardes in Westkleinasien gedacht, dessen Name in einer lydischen Inschrift ähnlich geschrieben wird. Seit der Spätantike (schon im aramäischen Targum) wurde «Sefarad» auf Spanien bezogen; daher heissen die spanisch-portugiesischen Juden «Sefarden».",
  "Die Gleichsetzung mit Sardes ist eine Vermutung.",
  ["1KI.17.9"], [], [("heb", "סְפָרַד", "Sefarad", "sefarad")],
  "Verbannti i de Färni: Sarepta und Sefarad",
  "Sarepta isch e phönizischi Stadt bi Sidon gsii ([[1KI.17.9]]). Wo Sefarad gläge isch, weiss me nöd; oft dänkt me a Sardes im Weschte vo Chliiasie, wo sin Name i ere lydische Inschrift ähnlich gschribe wird. Sit de Spöötantike (scho im aramäische Targum) hät me «Sefarad» uf Spanie bezoge; drum heissed di spanisch-portugiesische Jude «Sefarde».",
  "D Gliichsetzig mit Sardes isch e Vermuetig.", ["Sefarad"]),
 ("BG-OBA-BOOK-0001", None, "OBA", "CTX-OBA-AFTER-587", "probable", "Obadja: Name, Zeit und Platz im Buch der Zwölf",
  "Der Name Obadja bedeutet «Diener JHWHs»; über den Propheten selbst ist nichts bekannt. Meist wird das Buch bald nach der Zerstörung Jerusalems 587/586 v. Chr. angesetzt. Im hebräischen Buch der Zwölf steht es nach Amos, dessen Schluss Edom nennt ([[AMO.9.12]]); in der griechischen Bibel ist die Reihenfolge der ersten sechs Bücher anders.",
  "Die Datierung ist umstritten (siehe die offene Frage zum Buch).",
  ["AMO.9.12"], [], [("heb", "עֹבַדְיָה", "Obadja: «Diener JHWHs»", "owadja")],
  "Obadja: Name, Ziit und Platz im Buech vo de Zwölf",
  "De Name Obadja heisst «Diener vo JHWH»; über de Prophet sälber weiss me nüt. Meischtens wird s Buech bald nach de Zerstörig vo Jerusalem 587/586 v. Chr. aagsetzt. Im hebräische Buech vo de Zwölf staat s nach em Amos, wo am Schluss Edom nännt ([[AMO.9.12]]); i de griechische Bible isch d Reiefolg vo de erschte sächs Büecher anders.",
  "D Datierig isch umstritte (lueg di offe Frag zum Buech).", ["Obadja: «Diener vo JHWH»"]),
 ("BG-OBA-BOOK-0002", None, "OBA", "CTX-OBA-AFTER-587", "probable", "Was aus Edom wurde",
  "Im 4. Jahrhundert v. Chr. übernahmen die Nabatäer das alte Kerngebiet Edoms. Die Edomiter im Süden Judas, nun Idumäer genannt, wurden zwischen etwa 128 und 111 v. Chr. (die Datierung ist umstritten) vom hasmonäischen Herrscher Johannes Hyrkan unterworfen und zur Beschneidung gezwungen. Herodes der Grosse stammte aus einer idumäischen Familie. In der rabbinischen Literatur steht «Edom» später für Rom.",
  None, [], ["Flavius Josephus, Jüdische Altertümer 13,257–258"], [],
  "Was us Edom worde isch",
  "Im 4. Jaarhundert v. Chr. händ d Nabatäer s alt Kärngebiet vo Edom übernoo. D Edomiter im Süde vo Juda, jetzt Idumäer gnännt, sind zwüsche öppe 128 und 111 v. Chr. (d Datierig isch umstritte) vom hasmonäische Herrscher Johannes Hyrkan underworfe und zur Beschniidig zwunge worde. De Herodes de Groosse isch us ere idumäische Familie cho. I de rabbinische Literatur staat «Edom» spööter für Rom.",
  None, []),
]

SUMMARIES = [
 ("SUM-CH-OBA-001", "Ein Wort gegen Edom: Das Volk, das sich in seinen Felsen sicher fühlte und am Tag des Untergangs Jerusalems gegen seinen Bruder Jakob stand, wird selbst gerichtet. Am Ende steht die Hoffnung auf Heimkehr und darauf, dass die Königsherrschaft JHWH gehört.",
  "Es Wort gäge Edom: S Volk, wo sich i sine Felse sicher gfüült hät und am Taag vom Undergang vo Jerusalem gäge sin Brueder Jakob gstande isch, wird sälber grichtet. Am Änd staat d Hoffnig uf d Heichehr und druf, dass d Königsherrschaft em JHWH ghört."),
]


def run():
    from _study import write_study
    write_study({"TAGS": TAGS, "CONTEXT": CONTEXT, "FINDINGS": FINDINGS, "INTERPRETATIONS": INTERPRETATIONS,
                 "PRINCIPLES": PRINCIPLES, "APPLICATIONS": APPLICATIONS, "QUESTIONS": QUESTIONS, "RELATIONS": RELATIONS,
                 "BACKGROUND": BACKGROUND, "SUMMARIES": SUMMARIES,
                 "STUDY": ("STUDY-OBA-0001", "Obadja: ganzes Buch als Muster (Hebräisch)", "TU-OBA-001-001-021",
                           ["TRANS-OBA-001-001-021-DE-WORKING", "TRANS-OBA-001-001-021-GSW-ZH-WORKING"],
                           ["Mundart muttersprachlich prüfen", "Textkritische Daten (Qumran, Septuaginta) aus freien Quellen ergänzen",
                            "Fachliche Prüfung der Deutungen und des Hintergrunds"])}, "Obadja")


if __name__ == "__main__":
    run()
