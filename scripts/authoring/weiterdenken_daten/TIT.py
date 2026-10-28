"""Weiterdenken zum Titusbrief (Entscheid Andi Neck 2026-10-28): Fragen zum Weiterdenken und «Wie man es gelesen hat»
für alle Abschnitte, Kapitel und das Buch. KI-Entwürfe ohne fachliche Prüfung; Quellen in frei zugänglichen Ausgaben
nachgeschlagen (source_check), soweit möglich. Pauschalurteile des Textes (über Kreter, «die aus der Beschneidung») werden
als Teil des Textes befragt, nicht übernommen.

Prüfvermerk (PROC-WEITERDENKEN@1.0, Schritte 3 und 4): Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung,
Claude) gegen die hochdeutsche Arbeitsübersetzung geprüft: alle 21 Fragen und Hintergrundsätze (offen, nicht suggestiv,
am Text belegt, Zitate per Skript wörtlich verglichen, Stellenmarken), Mundart nach pruefe_mundart; Kernaussagen (gist_de)
der Kernanalysen gegen den Text;
Quellen von 2 der 4 Einträge «Wie man es gelesen hat» erneut
nachgeschlagen (Vermerk im source_check). Grenzen: nicht gegen den Urtext geprüft; Zitate aus Büchern ohne
Arbeitsübersetzung nicht verglichen; Mundart-Zitate nicht an die Mundart-Übersetzungsschicht angeglichen; keine fachliche
und keine muttersprachliche Prüfung durch eine Person."""
DATE = "2026-10-28"
PROCESS = "PROC-WEITERDENKEN@1.0"
TAGS = ["TAG-TITUS"]
AUTHORSHIP_DE = "KI-Entwurf (Claude) vom 2026-10-28 (Weiterdenken Titus, Entscheid Andi Neck); keine fachliche Prüfung."

REFLECTIONS = [
    # Buch
    {"id": "REFL-TIT-0001", "subject": "SUM-BOOK-TIT", "order": 1,
     "question_de": "Warum kommt dieser Brief immer wieder auf «gute Werke» zurück?",
     "note_de": "Die Wendung zieht sich durch alle drei Kapitel ([[TIT.1.16]]; [[TIT.2.7]]; [[TIT.2.14]]; [[TIT.3.8]]; [[TIT.3.14]]) – neben dem Satz, dass Gott nicht aufgrund von Werken rettet ([[TIT.3.5]]).",
     "gsw": {"question_de": "Wieso chunnt dä Brief immer wider uf «gueti Wärch» zrugg?",
             "note_de": "D Wändig zieht sich dur alli drü Kapitel ([[TIT.1.16]]; [[TIT.2.7]]; [[TIT.2.14]]; [[TIT.3.8]]; [[TIT.3.14]]) – näbe em Satz, dass Gott nöd wäge Wärch rettet ([[TIT.3.5]])."}},
    {"id": "REFL-TIT-0002", "subject": "SUM-BOOK-TIT", "order": 2,
     "question_de": "Was gilt in diesem Brief für damals auf Kreta, und was darüber hinaus?",
     "note_de": "Der Brief richtet sich an Titus auf Kreta ([[TIT.1.5]]), spricht aber auch von der Gnade, die «für alle Menschen» erschienen ist ([[TIT.2.11]]).",
     "gsw": {"question_de": "Was gilt i dem Brief für dänn uf Kreta, und was drüber use?",
             "note_de": "De Brief richtet sich a de Titus uf Kreta ([[TIT.1.5]]), redt aber au vo de Gnad, wo «allne Mänsche Rettig bringt» ([[TIT.2.11]])."}},
    # Kapitel
    {"id": "REFL-TIT-0003", "subject": "SUM-CH-TIT-001", "order": 1,
     "question_de": "Woran erkennt man, ob jemand Gott kennt?",
     "note_de": "Das Kapitel endet mit Leuten, die behaupten, Gott zu kennen, ihn aber mit den Werken verleugnen ([[TIT.1.16]]).",
     "gsw": {"question_de": "Wora erchännt mer, öb öpper Gott kännt?",
             "note_de": "S Kapitel hört mit Lüüt uf, wo behaupted, si kännted Gott, en aber mit de Wärch verleugned ([[TIT.1.16]])."}},
    {"id": "REFL-TIT-0004", "subject": "SUM-CH-TIT-002", "order": 1,
     "question_de": "Warum ist es dem Brief so wichtig, was Aussenstehende denken?",
     "note_de": "Mehrmals heisst es «damit …»: damit das Wort Gottes nicht in Verruf kommt, der Gegner beschämt wird, die Lehre geschmückt wird ([[TIT.2.5]]; [[TIT.2.8]]; [[TIT.2.10]]).",
     "gsw": {"question_de": "Wieso isch es em Brief so wichtig, was Ussestehendi dänked?",
             "note_de": "Mee als eimal heisst s «demit …»: demit s Wort vo Gott nöd in Verruef chunnt, de Gägner sich schämt, d Lehr gschmückt wird ([[TIT.2.5]]; [[TIT.2.8]]; [[TIT.2.10]])."}},
    {"id": "REFL-TIT-0005", "subject": "SUM-CH-TIT-003", "order": 1,
     "question_de": "Was ändert es, wenn man daran denkt, wie man selbst einmal war?",
     "note_de": "«Denn auch wir waren einst unverständig, ungehorsam, irregeführt» ([[TIT.3.3]]) – so wird die Mahnung zur Freundlichkeit begründet ([[TIT.3.2]]).",
     "gsw": {"question_de": "Was änderet s, wänn mer dra dänkt, wie mer sälber emal gsii isch?",
             "note_de": "«Dänn au mir sind früener unverständig, unghorsam, verirrt … gsii» ([[TIT.3.3]]) – so wird d Mahnig zur Fründlichkeit begründet ([[TIT.3.2]])."}},
    # 1,1–4
    {"id": "REFL-TIT-0006", "subject": "TU-TIT-001-001-004", "order": 1,
     "question_de": "Was bedeutet es, jemanden «mein echtes Kind im gemeinsamen Glauben» zu nennen?",
     "note_de": "So nennt Paulus Titus ([[TIT.1.4]]) – nicht verwandt, sondern durch den gemeinsamen Glauben verbunden.",
     "gsw": {"question_de": "Was bedüütet s, öpper «mim ächte Chind im gmeinsame Glaube» z schriibe?",
             "note_de": "So nännt de Paulus de Titus ([[TIT.1.4]]) – nöd verwandt, sondern dur de gmeinsam Glaube verbunde."}},
    {"id": "REFL-TIT-0007", "subject": "TU-TIT-001-001-004", "order": 2,
     "question_de": "Warum betont der Gruss, dass Gott «nicht lügt»?",
     "note_de": "Die Hoffnung auf ewiges Leben hat «der Gott, der nicht lügt», verheissen ([[TIT.1.2]]); wenig später fällt das Wort von den lügenden Kretern ([[TIT.1.12]]).",
     "gsw": {"question_de": "Wieso betont de Gruess, dass Gott «nöd lügt»?",
             "note_de": "D Hoffnig uf ewigs Läbe hät «de Gott, wo nöd lügt», verheisse ([[TIT.1.2]]); weni speter fallt s Wort vo de Kreter, wo lüged ([[TIT.1.12]])."}},
    # 1,5–9
    {"id": "REFL-TIT-0008", "subject": "TU-TIT-001-005-009", "order": 1,
     "question_de": "Welche dieser Eigenschaften würdest du von Menschen in Verantwortung erwarten – und welche fehlen dir?",
     "note_de": "Die Liste nennt fast nur Charakter und Lebensführung ([[TIT.1.6-TIT.1.8]]); nur eine Fähigkeit wird verlangt: ermahnen und widerlegen können ([[TIT.1.9]]).",
     "gsw": {"question_de": "Weli vo dene Eigeschafte würdsch du vo Mänsche i de Verantwortig erwarte – und weli fääled dir?",
             "note_de": "D Lischte nännt fascht nu Charakter und Läbesfüerig ([[TIT.1.6-TIT.1.8]]); nu ei Fähigkeit wird verlangt: ermahne und widerlege chöne ([[TIT.1.9]])."}},
    {"id": "REFL-TIT-0009", "subject": "TU-TIT-001-005-009", "order": 2,
     "question_de": "Warum steht «gastfreundlich» an erster Stelle der guten Eigenschaften?",
     "note_de": "Nach den Verboten beginnt die Reihe der guten Eigenschaften mit «gastfreundlich» ([[TIT.1.8]]).",
     "gsw": {"question_de": "Wieso staat «gaschtfründlich» zvorderscht bi de guete Eigeschafte?",
             "note_de": "Nach de Verbot fangt d Reihe vo de guete Eigeschafte mit «gaschtfründlich» aa ([[TIT.1.8]])."}},
    # 1,10–16
    {"id": "REFL-TIT-0010", "subject": "TU-TIT-001-010-016", "order": 1,
     "question_de": "Was macht ein Pauschalurteil über ein ganzes Volk mit denen, die es trifft?",
     "note_de": "Der Brief zitiert einen Kreter: «Kreter sind immer Lügner» und nennt das Zeugnis wahr ([[TIT.1.12-TIT.1.13]]); unter den Verführern werden «besonders die aus der Beschneidung» genannt ([[TIT.1.10]]).",
     "gsw": {"question_de": "Was macht es Pauschalurteil über es ganzes Volk mit dene, wo s trifft?",
             "note_de": "De Brief zitiert en Kreter: «Kreter sind immer Lugner» und nännt s Zügnis wahr ([[TIT.1.12-TIT.1.13]]); under de Verfüerer wärded «vor allem die us de Beschniidig» gnännt ([[TIT.1.10]])."}},
    {"id": "REFL-TIT-0011", "subject": "TU-TIT-001-010-016", "order": 2,
     "question_de": "«Alles ist rein für die Reinen» – was sagt dieser Satz über den Blick des Betrachters?",
     "note_de": "Für die Befleckten ist nichts rein, «befleckt sind sowohl ihr Verstand als auch ihr Gewissen» ([[TIT.1.15]]).",
     "gsw": {"question_de": "«Alles isch rein für die Reine» – was seit dä Satz über de Blick vo dem, wo aaluegt?",
             "note_de": "Für di Befleckte isch nüüt rein, «befleckt sind sowohl ire Verstand als au ires Gwüsse» ([[TIT.1.15]])."}},
    # 2,1–10
    {"id": "REFL-TIT-0012", "subject": "TU-TIT-002-001-010", "order": 1,
     "question_de": "Was an diesen Anweisungen gehört zur Gesellschaft von damals, was nicht?",
     "note_de": "Frauen sollen ihren Männern untergeordnet sein, Sklaven ihren Herren ([[TIT.2.5]]; [[TIT.2.9]]); der Brief stellt die damaligen Ordnungen nicht in Frage.",
     "gsw": {"question_de": "Was a dene Aawiisige ghört zur Gsellschaft vo dänn, was nöd?",
             "note_de": "Fraue söled irne Manne undergordnet sii, Sklave irne Herre ([[TIT.2.5]]; [[TIT.2.9]]); de Brief stellt di dänn gültige Ornige nöd in Frag."}},
    {"id": "REFL-TIT-0013", "subject": "TU-TIT-002-001-010", "order": 2,
     "question_de": "Wie lehrt man mehr durch sein Vorbild als durch Worte?",
     "note_de": "Titus soll sich «selbst als Vorbild guter Werke» zeigen ([[TIT.2.7]]); die älteren Frauen sollen «Lehrerinnen des Guten» sein ([[TIT.2.3]]).",
     "gsw": {"question_de": "Wie lehrt mer meh mit sim Vorbild als mit Wort?",
             "note_de": "De Titus söll sich «sälber als Vorbild für gueti Wärch» zeige ([[TIT.2.7]]); di eltere Fraue söled «Lehrerinne vom Guete» sii ([[TIT.2.3]])."}},
    # 2,11–15
    {"id": "REFL-TIT-0014", "subject": "TU-TIT-002-011-015", "order": 1,
     "question_de": "Wie kann Gnade erziehen?",
     "note_de": "Die erschienene Gnade Gottes «erzieht uns» zu einem besonnenen, gerechten und frommen Leben ([[TIT.2.11-TIT.2.12]]).",
     "gsw": {"question_de": "Wie chan Gnad erzie?",
             "note_de": "D Gnad vo Gott, wo erschine isch, «erziet üs» zu me bsunnene, grächte und fromme Läbe ([[TIT.2.11-TIT.2.12]])."}},
    {"id": "REFL-TIT-0015", "subject": "TU-TIT-002-011-015", "order": 2,
     "question_de": "Was heisst «für alle Menschen» in einem Brief, der vorher so scharf abgrenzt?",
     "note_de": "Die Gnade ist «rettend für alle Menschen» erschienen ([[TIT.2.11]]).",
     "gsw": {"question_de": "Was heisst «allne Mänsche» i me Brief, wo vorher so scharf abgränzt?",
             "note_de": "D Gnad vo Gott isch erschine, «wo allne Mänsche Rettig bringt» ([[TIT.2.11]])."}},
    # 3,1–7
    {"id": "REFL-TIT-0016", "subject": "TU-TIT-003-001-007", "order": 1,
     "question_de": "Was bedeutet «Menschenfreundlichkeit» Gottes?",
     "note_de": "«Als aber die Güte und die Menschenfreundlichkeit Gottes, unseres Retters, erschien» ([[TIT.3.4]]); kurz zuvor sollen die Glaubenden selbst «gegenüber allen Menschen» Sanftmut zeigen ([[TIT.3.2]]).",
     "gsw": {"question_de": "Was bedüütet «Mänschefründlichkeit» vo Gott?",
             "note_de": "«Wo aber d Güeti und d Mänschefründlichkeit vo Gott, öisem Retter, erschine isch» ([[TIT.3.4]]); churz vorher söled d Gläubige sälber «gägenüber allne Mänsche» Sanftmuet zeige ([[TIT.3.2]])."}},
    {"id": "REFL-TIT-0017", "subject": "TU-TIT-003-001-007", "order": 2,
     "question_de": "Wie wird man freundlich zu Menschen, die man schwierig findet?",
     "note_de": "Titus soll die Glaubenden daran erinnern, freundlich zu sein und «volle Sanftmut zu zeigen gegenüber allen Menschen» ([[TIT.3.1-TIT.3.2]]).",
     "gsw": {"question_de": "Wie wird mer fründlich zu Mänsche, wo mer schwierig findt?",
             "note_de": "De Titus söll d Gläubige draa erinnere, fründlich z sii und «volli Sanftmuet z zeige gägenüber allne Mänsche» ([[TIT.3.1-TIT.3.2]])."}},
    # 3,8–11
    {"id": "REFL-TIT-0018", "subject": "TU-TIT-003-008-011", "order": 1,
     "question_de": "Wann ist ein Streit nutzlos – und wann muss man ihn führen?",
     "note_de": "Titus soll Streitfragen und Streit um das Gesetz meiden, «denn sie sind nutzlos und leer» ([[TIT.3.9]]); zugleich soll er fest auftreten ([[TIT.3.8]]).",
     "gsw": {"question_de": "Wänn isch en Striit nutzlos – und wänn mues mer en füere?",
             "note_de": "De Titus söll Striitfroge und Striit ums Gsetz meide, «dänn si sind nutzlos und läär» ([[TIT.3.9]]); zgliich söll er fescht uftrete ([[TIT.3.8]])."}},
    {"id": "REFL-TIT-0019", "subject": "TU-TIT-003-008-011", "order": 2,
     "question_de": "Warum zwei Ermahnungen, bevor man jemanden abweist?",
     "note_de": "«Einen Menschen, der Spaltungen verursacht, weise nach einer ersten und zweiten Ermahnung ab» ([[TIT.3.10]]).",
     "gsw": {"question_de": "Wieso zwei Ermahnige, bevor mer öpper abwiist?",
             "note_de": "«En Mänsch, wo Spaltige verursachet, wiis nach ere erschte und zweite Ermaanig ab» ([[TIT.3.10]])."}},
    # 3,12–15
    {"id": "REFL-TIT-0020", "subject": "TU-TIT-003-012-015", "order": 1,
     "question_de": "Was erzählen die vielen Namen am Schluss über die frühen Gemeinden?",
     "note_de": "Artemas, Tychikus, Zenas, der Rechtsgelehrte, und Apollos sind unterwegs und müssen ausgerüstet werden ([[TIT.3.12-TIT.3.13]]).",
     "gsw": {"question_de": "Was verzelled di vile Näme am Schluss über di früene Gmeinde?",
             "note_de": "De Artemas, de Tychikus, de Zenas, de Rächtsgleert, und de Apollos sind understwägs und müend usgrüschtet wärde ([[TIT.3.12-TIT.3.13]])."}},
    {"id": "REFL-TIT-0021", "subject": "TU-TIT-003-012-015", "order": 2,
     "question_de": "Was heisst es, «nicht ohne Frucht» zu sein?",
     "note_de": "Die Glaubenden sollen sich für gute Werke einsetzen, «für die dringenden Bedürfnisse» ([[TIT.3.14]]).",
     "gsw": {"question_de": "Was heisst es, «nöd ohni Frucht» z sii?",
             "note_de": "D Gläubige söled sich für gueti Wärch iisetze, «für di dringende Bedürfnis» ([[TIT.3.14]])."}},
]

RECEPTIONS = [
    {"id": "RCPT-TIT-0001", "subject": "TU-TIT-001-010-016", "tradition": "church_fathers", "period_de": "um 200; 4. Jahrhundert",
     "text_de": "Der Vers «Kreter sind immer Lügner, böse Tiere, faule Bäuche» ([[TIT.1.12]]) wird schon von Clemens von Alexandria dem Dichter Epimenides von Kreta zugeschrieben; Hieronymus nennt in seinem Titus-Kommentar ebenfalls Epimenides. Später wurde der Satz eines Kreters, alle Kreter lögen, zum Beispiel für das «Lügner-Paradox» der Logik.",
     "sources_de": ["Clemens von Alexandria, Stromateis 1,14", "Hieronymus, Kommentar zum Titusbrief, zu 1,12"],
     "confidence": "high",
     "gsw": {"period_de": "um 200; 4. Jahrhundert",
             "text_de": "De Vers «Kreter sind immer Lügner, bösi Tier, fuuli Büüch» ([[TIT.1.12]]) schriibt scho de Clemens vo Alexandria em Dichter Epimenides vo Kreta zue; de Hieronymus nännt i sim Titus-Kommentar au de Epimenides. Speter isch de Satz vo me Kreter, alli Kreter lüged, zum Biispil für s «Lügner-Paradox» vo de Logik worde."}},
    {"id": "RCPT-TIT-0002", "subject": "SUM-BOOK-TIT", "tradition": "modern_scholarship", "period_de": "seit dem 18. Jahrhundert",
     "text_de": "Seit dem 18. Jahrhundert werden die beiden Briefe an Timotheus und der Brief an Titus zusammen «Pastoralbriefe» genannt, weil sie sich an Leiter von Gemeinden richten. Seit dem 19. Jahrhundert halten viele Forschende sie wegen Sprache, Gemeindeordnung und Lage für Schriften aus der Zeit nach Paulus; andere halten an Paulus als Verfasser fest.",
     "sources_de": ["D. N. Berdot (1703) und Paul Anton (1726): Bezeichnung «Pastoralbriefe»", "Friedrich Schleiermacher (1807): Beginn der Echtheitskritik"],
     "confidence": "high",
     "gsw": {"period_de": "sit em 18. Jahrhundert",
             "text_de": "Sit em 18. Jahrhundert nännt mer di beide Brief a de Timotheus und de Brief a de Titus zäme «Pastoralbrief», wil si sich a Leiter vo Gmeinde richted. Sit em 19. Jahrhundert halted vil Forschendi si wäge Sprach, Gmeindsornig und Laag für Schrifte us de Ziit nach em Paulus; anderi halted am Paulus als Verfasser fescht."}},
    {"id": "RCPT-TIT-0003", "subject": "TU-TIT-002-011-015", "tradition": "liturgy", "period_de": "bis heute",
     "text_de": "In der römisch-katholischen Leseordnung ist [[TIT.2.11-TIT.2.14]] die zweite Lesung der Christmette in der Heiligen Nacht, [[TIT.3.4-TIT.3.7]] die der Messe am Weihnachtsmorgen: Dass die Gnade Gottes und seine Menschenfreundlichkeit «erschienen» sind, wird auf die Geburt Jesu bezogen.",
     "sources_de": ["Römisches Messlektionar, Weihnachten (Messe in der Heiligen Nacht; Messe am Morgen)"],
     "confidence": "high",
     "gsw": {"period_de": "bis hüt",
             "text_de": "I de römisch-katholische Läseornig isch [[TIT.2.11-TIT.2.14]] di zweit Läsig vo de Chrischtmette i de Heilige Nacht, [[TIT.3.4-TIT.3.7]] die vo de Mäss am Wienachtsmorge: Dass d Gnad vo Gott und sini Mänschefründlichkeit «erschine» sind, bezieht mer uf d Geburt vo Jesus."}},
    {"id": "RCPT-TIT-0004", "subject": "SUM-BOOK-TIT", "tradition": "reformation", "period_de": "1522",
     "text_de": "Martin Luther nennt den Titusbrief in seiner Vorrede zu diesem Brief eine kurze Epistel, aber ein Muster christlicher Lehre.",
     "sources_de": ["Martin Luther, Vorrede auf die Epistel an Titus (1522)"],
     "confidence": "probable",
     "gsw": {"period_de": "1522",
             "text_de": "De Martin Luther nännt de Titusbrief i sinere Vorred zu dem Brief e churzi Epistel, aber es Muschter vo de chrischtliche Lehr."}},
]

# Quellenprüfung (docs/QUELLENPRUEFUNG.md)
SOURCE_CHECKS = {
 "RCPT-TIT-0001": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Clemens von Alexandria, Stromateis 1,14",
    "found_at": "https://en.wikipedia.org/wiki/Epimenides_paradox",
    "finding_de": "Clemens verbindet den Vers aus [[TIT.1.12]] mit Epimenides; der Satz wird später als Variante des Lügner-Paradoxes behandelt."
   },
   {
    "source": "Hieronymus, Kommentar zum Titusbrief zu 1,12",
    "found_at": "https://www.bsw.org/filologia-neotestamentaria/vol-24-2011/the-famous-liar-and-the-apostolic-truth/637/article-p63.html",
    "finding_de": "Hieronymus: der Vers finde sich in den «Orakeln» des Kreters Epimenides."
   }
  ]
 },
 "RCPT-TIT-0002": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Bezeichnung «Pastoralbriefe»; Echtheitskritik",
    "found_at": "https://en.wikipedia.org/wiki/Pastoral_epistles",
    "finding_de": "Die Bezeichnung wurde 1703 durch D. N. Berdot und 1726 durch Paul Anton verbreitet; die Echtheitskritik beginnt mit Schleiermacher 1807. Vorher nur Paul Anton als Quelle genannt."
   }
  ]
 },
 "RCPT-TIT-0003": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Römisches Messlektionar, Weihnachten",
    "found_at": "https://liturgyoffice.org/Resources/Scripture/Titus.pdf",
    "finding_de": "[[TIT.2.11-TIT.2.14]] in der Messe in der Heiligen Nacht, [[TIT.3.4-TIT.3.7]] in der Messe am Morgen."
   }
  ]
 },
 "RCPT-TIT-0004": {
  "date": "2026-10-29",
  "result": "partly",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Martin Luther, Vorrede auf die Epistel an Titus",
    "found_at": "https://lutheranspokesman.org/2025/11/01/titus-shattering-the-glass-hammer-myth/ (Zitat nach Luther’s Works 35, 389–390)",
    "finding_de": "«This is a short epistle, but a model of Christian doctrine» belegt; das Jahr 1522 ist an der Fundstelle nicht genannt. Eine weitergehende Aussage über Glaube und Werke wurde gestrichen."
   }
  ]
 }
}
UNCERTAIN = {"RCPT-TIT-0004": "Das Jahr 1522 (Septembertestament) ist an der Fundstelle nicht genannt."}
for _x in RECEPTIONS:
    _x["source_check"] = SOURCE_CHECKS[_x["id"]]
    if _x["id"] in UNCERTAIN:
        _x["uncertain_de"] = UNCERTAIN[_x["id"]]

# Zweite Quellenprüfung durch eine weitere Instanz (2026-10-29)
RECHECK_DE = " Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung, Claude) erneut nachgeschlagen; keine fachliche Prüfung."
RECHECKED = ["RCPT-TIT-0002", "RCPT-TIT-0004"]
RECHECK_EXTRA = {}
for _x in RECEPTIONS:
    if _x["id"] in RECHECKED:
        _sc = dict(_x["source_check"])
        _sc["method_de"] = _sc["method_de"] + RECHECK_DE
        if _x["id"] in RECHECK_EXTRA:
            _sc["checked"] = _sc["checked"] + [RECHECK_EXTRA[_x["id"]]]
        _x["source_check"] = _sc
