"""Weiterdenken der oberen Ebenen (Entscheid Andi Neck 2026-10-28): Fragen zum Weiterdenken und «Wie man es gelesen hat»
für die Bibel (SUM-BIBLE), die Testamente (SUM-OT, SUM-NT) und die Buchgruppen (SUM-GROUP-01 … SUM-GROUP-10).
IDs REFL-ALL-nnnn / RCPT-ALL-nnnn («ALL» = keine einzelne Buchkennung). KI-Entwürfe ohne fachliche Prüfung; Quellen in
frei zugänglichen Ausgaben nachgeschlagen (source_check), soweit möglich. Für diese Ebenen gibt es keine Kernanalyse,
darum auch keine Kernaussage (gist_de).

Prüfvermerk (PROC-WEITERDENKEN@1.0, Schritte 3 und 4): Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung,
Claude) gegen die hochdeutsche Arbeitsübersetzung geprüft: alle 16 Fragen und Hintergrundsätze (offen, nicht suggestiv,
am Text belegt, Zitate per Skript wörtlich verglichen, Stellenmarken), Mundart nach pruefe_mundart;
Quellen von 15 der 15 Einträge «Wie man es gelesen hat» erneut
nachgeschlagen (Vermerk im source_check). Grenzen: nicht gegen den Urtext geprüft; Zitate aus Büchern ohne
Arbeitsübersetzung nicht verglichen; Mundart-Zitate nicht an die Mundart-Übersetzungsschicht angeglichen; keine fachliche
und keine muttersprachliche Prüfung durch eine Person."""
DATE = "2026-10-28"
PROCESS = "PROC-WEITERDENKEN@1.0"
TAGS = []
AUTHORSHIP_DE = "KI-Entwurf (Claude) vom 2026-10-28 (Weiterdenken obere Ebenen, Entscheid Andi Neck); keine fachliche Prüfung."

REFLECTIONS = [
    # Bibel
    {"id": "REFL-ALL-0001", "subject": "SUM-BIBLE", "order": 1,
     "question_de": "Ist die Bibel eher ein Buch oder eine Bibliothek?",
     "note_de": "Sie versammelt Erzählungen, Gesetze, Gebete, Weisheit, Prophetie und Briefe aus vielen Jahrhunderten und mehreren Sprachen.",
     "gsw": {"question_de": "Isch d Bible ender es Buech oder e Bibliothek?",
             "note_de": "Si versammlet Gschichte, Gsetz, Gebät, Wiisheit, Prophetie und Brief us vile Jahrhundert und mehrere Sprache."}},
    {"id": "REFL-ALL-0002", "subject": "SUM-BIBLE", "order": 2,
     "question_de": "Welche Stimme in der Bibel ist dir am nächsten – und welche am fremdesten?",
     "gsw": {"question_de": "Weli Stimm i de Bible isch dir am nöchschte – und weli am frömdischte?"}},
    # Altes Testament
    {"id": "REFL-ALL-0003", "subject": "SUM-OT", "order": 1,
     "question_de": "Was ändert sich, wenn man diese Schriften zuerst so liest, wie Israel sie gehört hat?",
     "note_de": "Dieselben Schriften sind die Bibel des Judentums und der erste Teil der christlichen Bibel; Anordnung und Lesart unterscheiden sich.",
     "gsw": {"question_de": "Was änderet sich, wänn mer die Schrifte zerscht so list, wie Israel si ghört hät?",
             "note_de": "Di gliiche Schrifte sind d Bible vom Judetum und de erscht Teil vo de chrischtliche Bible; Aaornig und Läsart underscheided sich."}},
    {"id": "REFL-ALL-0004", "subject": "SUM-OT", "order": 2,
     "question_de": "Warum werden Scheitern, Klage und Zweifel hier nicht verschwiegen?",
     "gsw": {"question_de": "Wieso wärded Scheitere, Chlag und Zwiifel da nöd verschwige?"}},
    # Neues Testament
    {"id": "REFL-ALL-0005", "subject": "SUM-NT", "order": 1,
     "question_de": "Was verbindet die Evangelien, die Apostelgeschichte, die Briefe und die Offenbarung?",
     "note_de": "Sie stammen von verschiedenen Verfassern, sind in verschiedenen Lagen entstanden und erzählen, deuten und mahnen auf je eigene Weise.",
     "gsw": {"question_de": "Was verbindet d Evangelie, d Apostelgschicht, d Brief und d Offebarig?",
             "note_de": "Si stammed vo verschidene Verfasser, sind i verschidene Laage entstande und verzelled, düüted und mahned uf iri eigeti Art."}},
    {"id": "REFL-ALL-0006", "subject": "SUM-NT", "order": 2,
     "question_de": "Wie liest man das Neue Testament, ohne das Alte zu vergessen?",
     "note_de": "Die neutestamentlichen Schriften zitieren die Schriften Israels auf Schritt und Tritt (etwa [[MAT.1.22-MAT.1.23]]; [[LUK.4.17-LUK.4.21]]).",
     "gsw": {"question_de": "Wie list mer s Nöi Teschtament, ohni s Alt z vergässe?",
             "note_de": "Di nöitestamentliche Schrifte zitiered d Schrifte vo Israel uf Schritt und Tritt (öppe [[MAT.1.22-MAT.1.23]]; [[LUK.4.17-LUK.4.21]])."}},
    # Buchgruppen
    {"id": "REFL-ALL-0007", "subject": "SUM-GROUP-01", "order": 1,
     "question_de": "Warum beginnt die Bibel mit Erzählungen und nicht mit Geboten?",
     "note_de": "Die fünf Bücher Mose verbinden Erzählung und Weisung; das erste Gebot am Sinai beginnt mit einer Erinnerung an die Befreiung ([[EXO.20.2]]).",
     "gsw": {"question_de": "Wieso fangt d Bible mit Gschichte aa und nöd mit Gebot?",
             "note_de": "Di föif Büecher Mose verbinded Gschicht und Wiisig; s erscht Gebot am Sinai fangt mit ere Erinnerig a d Befreiig aa ([[EXO.20.2]])."}},
    {"id": "REFL-ALL-0008", "subject": "SUM-GROUP-02", "order": 1,
     "question_de": "Warum erzählt ein Volk seine Geschichte mit so vielen Niederlagen?",
     "note_de": "Die Bücher von Josua bis Ester erzählen vom Leben im Land, von Königen, vom Untergang und von der Rückkehr.",
     "gsw": {"question_de": "Wieso verzellt es Volk sini Gschicht mit so vile Niderlage?",
             "note_de": "D Büecher vom Josua bis zur Ester verzelled vom Läbe im Land, vo Könige, vom Undergang und vo de Rückchehr."}},
    {"id": "REFL-ALL-0009", "subject": "SUM-GROUP-03", "order": 1,
     "question_de": "Welche Worte findest du hier für das, wofür dir selbst Worte fehlen?",
     "note_de": "Hiob, die Psalmen, die Sprüche, der Prediger und das Hohelied geben Klage, Lob, Lebensklugheit, Zweifel und Liebe eine Sprache.",
     "gsw": {"question_de": "Weli Wort findsch du da für das, wo dir sälber d Wort fääled?",
             "note_de": "De Hiob, d Psalme, d Sprüch, de Prediger und s Hoheliid gänd de Chlag, em Lob, de Läbesklugheit, em Zwiifel und de Liebi e Sprach."}},
    {"id": "REFL-ALL-0010", "subject": "SUM-GROUP-04", "order": 1,
     "question_de": "Was machte prophetische Rede für ihre ersten Hörer unbequem?",
     "note_de": "Die grossen Propheten kritisieren Unrecht und falsche Sicherheit und sprechen zugleich von Trost und Neuanfang.",
     "gsw": {"question_de": "Was hät prophetischi Red für iri erschte Zuehörer unbequem gmacht?",
             "note_de": "Di grosse Prophete kritisiered Unrächt und falschi Sicherheit und redet zgliich vo Troscht und Nöiaafang."}},
    {"id": "REFL-ALL-0011", "subject": "SUM-GROUP-05", "order": 1,
     "question_de": "Warum stehen zwölf so verschiedene Stimmen nebeneinander?",
     "note_de": "Die zwölf kleinen Propheten reichen von wenigen Versen (Obadja) bis zu vierzehn Kapiteln (Hosea, Sacharja); Jona erzählt mehr, als er verkündet.",
     "gsw": {"question_de": "Wieso stönd zwölf so verschideni Stimme näbenand?",
             "note_de": "Di zwölf chliine Prophete gönd vo wenige Vers (Obadja) bis zu vierzää Kapitel (Hosea, Sacharja); de Jona verzellt meh, als er verchündet."}},
    {"id": "REFL-ALL-0012", "subject": "SUM-GROUP-06", "order": 1,
     "question_de": "Warum gibt es vier Evangelien und nicht nur eines?",
     "note_de": "Matthäus, Markus, Lukas und Johannes erzählen von Jesus mit eigenen Schwerpunkten und manchmal unterschiedlichen Einzelheiten.",
     "gsw": {"question_de": "Wieso git s vier Evangelie und nöd nu eis?",
             "note_de": "De Matthäus, de Markus, de Lukas und de Johannes verzelled vo Jesus mit eigete Schwärpünkt und mängisch underschidliche Einzelheite."}},
    {"id": "REFL-ALL-0013", "subject": "SUM-GROUP-07", "order": 1,
     "question_de": "Wie wird aus einer kleinen Gruppe in Jerusalem eine Bewegung bis nach Rom?",
     "note_de": "Die Apostelgeschichte folgt dem Weg «in Jerusalem und in ganz Judäa und Samarien und bis an das Ende der Erde» ([[ACT.1.8]]) und endet mit Paulus in Rom ([[ACT.28.30-ACT.28.31]]).",
     "gsw": {"question_de": "Wie wird us ere chliine Gruppe z Jerusalem e Bewegig bis uf Rom?",
             "note_de": "D Apostelgschicht folgt em Wäg «z Jerusalem und im ganze Judäa und Samarie und bis as Änd vo de Ärde» ([[ACT.1.8]]) und hört mit em Paulus z Rom uf ([[ACT.28.30-ACT.28.31]])."}},
    {"id": "REFL-ALL-0014", "subject": "SUM-GROUP-08", "order": 1,
     "question_de": "Wie liest man Briefe, die an andere Menschen geschrieben wurden?",
     "note_de": "Die Paulusbriefe antworten auf bestimmte Fragen und Konflikte bestimmter Gemeinden und Personen.",
     "gsw": {"question_de": "Wie list mer Brief, wo a anderi Mänsche gschribe worde sind?",
             "note_de": "D Paulusbrief antwortet uf bstimmti Froge und Konflikt vo bstimmte Gmeinde und Persone."}},
    {"id": "REFL-ALL-0015", "subject": "SUM-GROUP-09", "order": 1,
     "question_de": "Was hält Gemeinden zusammen, wenn sie unter Druck geraten?",
     "note_de": "Der Hebräerbrief, Jakobus, die Petrus-, Johannes- und Judasbriefe sprechen von Ausdauer, Glaube und Tat, Wahrheit und Liebe.",
     "gsw": {"question_de": "Was hebt Gmeinde zäme, wänn si under Druck chömed?",
             "note_de": "De Hebräerbrief, de Jakobus, d Petrus-, Johannes- und Judasbrief redet vo Usduur, Glaube und Tat, Wahrheit und Liebi."}},
    {"id": "REFL-ALL-0016", "subject": "SUM-GROUP-10", "order": 1,
     "question_de": "Wie wirken Bilder von Untergang und neuer Welt auf Menschen, die bedrängt sind?",
     "note_de": "Die Offenbarung richtet sich an sieben Gemeinden in Kleinasien ([[REV.1.4]]) und endet mit dem Bild einer neuen Stadt ([[REV.21.1-REV.21.4]]).",
     "gsw": {"question_de": "Wie würked Bilder vo Undergang und nöier Wält uf Mänsche, wo bedrängt sind?",
             "note_de": "D Offebarig richtet sich a sibe Gmeinde z Chliiasie ([[REV.1.4]]) und hört mit em Bild vo nere nöie Stadt uf ([[REV.21.1-REV.21.4]])."}},
]

RECEPTIONS = [
    {"id": "RCPT-ALL-0001", "subject": "SUM-BIBLE", "tradition": "church_fathers", "period_de": "um 391–405",
     "text_de": "Hieronymus übersetzt die Schriften Israels nicht mehr nur aus der griechischen Septuaginta, sondern aus dem Hebräischen ins Lateinische. Seine Übersetzung wird als «Vulgata» die Bibel der westlichen Kirche; anfangs stiess sie auf Widerstand, etwa in Oea, wo eine Gemeinde gegen ein neues Wort im Buch Jona protestierte.",
     "sources_de": ["Hieronymus, Vorrede zu den Büchern Samuel und Könige («Prologus galeatus», 391/392)", "Augustinus, Brief 71,5"],
     "confidence": "high",
     "gsw": {"period_de": "um 391–405",
             "text_de": "De Hieronymus übersetzt d Schrifte vo Israel nüme nu us de griechische Septuaginta, sondern us em Hebräische is Latiinisch. Sini Übersetzig wird als «Vulgata» d Bible vo de weschtliche Chilche; am Aafang hät si Widerstand ghaa, öppe z Oea, wo e Gmeind gäge es nöis Wort im Buech Jona protestiert hät."}},
    {"id": "RCPT-ALL-0002", "subject": "SUM-BIBLE", "tradition": "modern_scholarship", "period_de": "Anfang 13. Jahrhundert; 1551",
     "text_de": "Die heutige Einteilung in Kapitel geht auf Stephan Langton zurück, den späteren Erzbischof von Canterbury (Anfang des 13. Jahrhunderts); die Verszählung des Neuen Testaments führte der Drucker Robert Estienne (Stephanus) 1551 ein. Kapitel und Verse helfen beim Finden, stammen aber nicht von den biblischen Verfassern.",
     "sources_de": ["Stephan Langton, Kapiteleinteilung der lateinischen Bibel", "Robert Estienne, Neues Testament mit Verszählung (1551)"],
     "confidence": "high",
     "gsw": {"period_de": "Aafang 13. Jahrhundert; 1551",
             "text_de": "Di hütig Iiteilig i Kapitel gaat uf de Stephan Langton zrugg, de speter Erzbischof vo Canterbury (Aafang vom 13. Jahrhundert); d Verszellig vom Nöie Teschtament hät de Drucker Robert Estienne (Stephanus) 1551 iigfüert. Kapitel und Vers hälfed bim Finde, stammed aber nöd vo de biblische Verfasser."}},
    {"id": "RCPT-ALL-0003", "subject": "SUM-OT", "tradition": "jewish", "period_de": "3. oder frühes 2. Jahrhundert v. Chr.",
     "text_de": "Der Aristeasbrief erzählt, wie zweiundsiebzig jüdische Gelehrte in Alexandria das Gesetz Mose ins Griechische übersetzten. Von dieser Legende hat die griechische Übersetzung der Schriften Israels ihren Namen: Septuaginta («die Siebzig»). Sie wurde zur Bibel der griechisch sprechenden Juden und der frühen Christen.",
     "sources_de": ["Aristeasbrief"],
     "confidence": "high",
     "gsw": {"period_de": "3. oder frües 2. Jahrhundert v. Chr.",
             "text_de": "De Aristeasbrief verzellt, wie zweiesibezg jüdischi Gleerti z Alexandria s Gsetz vom Mose is Griechisch übersetzt händ. Vo dere Legände hät di griechisch Übersetzig vo de Schrifte vo Israel ire Name: Septuaginta («di Sibezg»). Si isch d Bible vo de griechisch redende Jude und vo de früene Chrischte worde."}},
    {"id": "RCPT-ALL-0004", "subject": "SUM-OT", "tradition": "church_fathers", "period_de": "2. Jahrhundert",
     "text_de": "Marcion nahm die Schriften Israels nicht in seine Bibel auf, weil ihr Gott ein anderer sei als der Vater Jesu; er wurde um 144 in Rom ausgeschlossen, und Tertullian schrieb ein grosses Werk gegen ihn. Wo das Alte Testament bis heute gegen das Neue ausgespielt wird, wird das oft mit Marcion verglichen und als judenfeindlich kritisiert.",
     "sources_de": ["Tertullian, Gegen Marcion (Adversus Marcionem)"],
     "confidence": "high",
     "gsw": {"period_de": "2. Jahrhundert",
             "text_de": "De Marcion hät d Schrifte vo Israel nöd i sini Bible ufgnoo, wil ire Gott en andere seig als de Vatter vo Jesus; er isch um 144 z Rom usgschlosse worde, und de Tertullian hät es grosses Wärch gäge en gschribe. Wo s Alt Teschtament bis hüt gäge s Nöi usgspilt wird, vergliicht mer das oft mit em Marcion und kritisiert s als judefeindlich."}},
    {"id": "RCPT-ALL-0005", "subject": "SUM-NT", "tradition": "church_fathers", "period_de": "367",
     "text_de": "Athanasius von Alexandria zählt in seinem 39. Osterfestbrief die siebenundzwanzig Schriften des Neuen Testaments auf – die älteste bekannte Liste, die genau unserem heutigen Neuen Testament entspricht.",
     "sources_de": ["Athanasius, 39. Osterfestbrief (367)"],
     "confidence": "high",
     "gsw": {"period_de": "367",
             "text_de": "De Athanasius vo Alexandria zellt i sim 39. Oschterfeschtbrief di sibenezwänzg Schrifte vom Nöie Teschtament uf – di eltischt bekannt Lischte, wo genau öisem hütige Nöie Teschtament entspricht."}},
    {"id": "RCPT-ALL-0006", "subject": "SUM-GROUP-01", "tradition": "liturgy", "period_de": "seit der Antike, bis heute",
     "text_de": "In der Synagoge wird die Tora, die fünf Bücher Mose, in Abschnitten fortlaufend gelesen. Schon der Talmud kennt beides: in Babylonien die ganze Tora in einem Jahr, im Land Israel in drei Jahren. Heute ist der Jahreszyklus üblich; er beginnt nach dem Laubhüttenfest wieder von vorn.",
     "sources_de": ["Babylonischer Talmud, Megilla 29b"],
     "confidence": "high",
     "gsw": {"period_de": "sit de Antike, bis hüt",
             "text_de": "I de Synagoge list mer d Tora, di föif Büecher Mose, i Abschnitt fortlaufend. Scho de Talmud kännt beides: z Babylonie di ganz Tora i eim Jahr, im Land Israel i drü Jahr. Hüt isch de Jahreszyklus üeblich; er fangt nach em Loubhüttefescht wider vo vorne aa."}},
    {"id": "RCPT-ALL-0007", "subject": "SUM-GROUP-02", "tradition": "modern_scholarship", "period_de": "seit 1943",
     "text_de": "Martin Noth fasste die Bücher Deuteronomium bis Könige als ein «deuteronomistisches Geschichtswerk» auf, das die Geschichte Israels bis zum Exil im Licht des Deuteronomiums deutet. Die Annahme ist seither viel diskutiert und abgewandelt worden. In der jüdischen Bibel heissen Josua bis Könige «frühere Propheten»; Rut, Chronik, Esra, Nehemia und Ester stehen dort unter den «Schriften».",
     "sources_de": ["Martin Noth, Überlieferungsgeschichtliche Studien (1943)", "Babylonischer Talmud, Bava Batra 14b"],
     "confidence": "high",
     "gsw": {"period_de": "sit 1943",
             "text_de": "De Martin Noth hät d Büecher Deuteronomium bis Könige als es «deuteronomistischs Gschichtswärch» ufgfasst, wo d Gschicht vo Israel bis zum Exil im Liecht vom Deuteronomium düütet. D Aanaam isch sitdem vil diskutiert und abgwandlet worde. I de jüdische Bible heissed Josua bis Könige «früeneri Prophete»; Rut, Chronik, Esra, Nehemia und Ester stönd dört under de «Schrifte»."}},
    {"id": "RCPT-ALL-0008", "subject": "SUM-GROUP-03", "tradition": "liturgy", "period_de": "6. Jahrhundert bis heute",
     "text_de": "Die Regel des Benedikt von Nursia legt fest, dass im Stundengebet der Mönche jede Woche der ganze Psalter gebetet wird. Seither prägen die Psalmen das tägliche Gebet in den Klöstern.",
     "sources_de": ["Regel Benedikts, Kapitel 18"],
     "confidence": "high",
     "gsw": {"period_de": "6. Jahrhundert bis hüt",
             "text_de": "D Regle vom Benedikt vo Nursia leit fescht, dass im Stundegebät vo de Mönch jedi Wuche de ganz Psalter bätet wird. Sitdem präged d Psalme s täglich Gebät i de Chlöschter."}},
    {"id": "RCPT-ALL-0009", "subject": "SUM-GROUP-04", "tradition": "jewish", "period_de": "Babylonischer Talmud, etwa 3.–6. Jahrhundert",
     "text_de": "Eine Überlieferung im Talmud ordnet die Propheten: Josua, Richter, Samuel, Könige, Jeremia, Ezechiel, Jesaja und die Zwölf. Klagelieder und Daniel stehen dort nicht bei den Propheten, sondern bei den «Schriften». In der christlichen Anordnung, die der griechischen und lateinischen Überlieferung folgt, stehen Klagelieder und Daniel bei den Propheten; Daniel zählt dort zu den vier grossen Propheten.",
     "sources_de": ["Babylonischer Talmud, Bava Batra 14b"],
     "confidence": "high",
     "gsw": {"period_de": "Babylonische Talmud, öppe 3.–6. Jahrhundert",
             "text_de": "E Überliferig im Talmud ordnet d Prophete: Josua, Richter, Samuel, Könige, Jeremia, Ezechiel, Jesaja und di Zwölf. D Chlaglieder und de Daniel stönd dört nöd bi de Prophete, sondern bi de «Schrifte». I de chrischtliche Aaornig, wo de griechische und latiinische Überliferig folgt, stönd d Chlaglieder und de Daniel bi de Prophete; de Daniel ghört dört zu de vier grosse Prophete."}},
    {"id": "RCPT-ALL-0010", "subject": "SUM-GROUP-05", "tradition": "jewish", "period_de": "um 180 v. Chr.; Talmud",
     "text_de": "Schon Jesus Sirach spricht von «den zwölf Propheten» als Gruppe. In der jüdischen Überlieferung gelten sie als ein einziges Buch («die Zwölf»), das auf einer Rolle geschrieben wurde.",
     "sources_de": ["Jesus Sirach 49,10", "Babylonischer Talmud, Bava Batra 14b"],
     "confidence": "high",
     "gsw": {"period_de": "um 180 v. Chr.; Talmud",
             "text_de": "Scho de Jesus Sirach redt vo «de zwölf Prophete» als Gruppe. I de jüdische Überliferig gälted si als es einzigs Buech («di Zwölf»), wo uf ei Rolle gschribe worde isch."}},
    {"id": "RCPT-ALL-0011", "subject": "SUM-GROUP-06", "tradition": "church_fathers", "period_de": "2. Jahrhundert",
     "text_de": "Tatian verband die vier Evangelien zu einer einzigen fortlaufenden Erzählung (Diatessaron), die in den syrischsprachigen Kirchen bis ins 5. Jahrhundert der gebräuchliche Evangelientext war. Irenäus von Lyon dagegen begründete, warum es genau vier Evangelien sein müssen, und verglich sie mit den vier Lebewesen vor Gottes Thron ([[REV.4.7]]); daraus entstanden die Sinnbilder der Evangelisten (Mensch, Löwe, Stier, Adler), die später anders zugeordnet wurden, als Irenäus es tat.",
     "sources_de": ["Irenäus, Gegen die Häresien 3,11,8", "Tatian, Diatessaron"],
     "confidence": "high",
     "gsw": {"period_de": "2. Jahrhundert",
             "text_de": "De Tatian hät di vier Evangelie zu nere einzige fortlaufende Gschicht verbunde (Diatessaron), wo i de syrischsprachige Chilche bis is 5. Jahrhundert de gebrüüchlich Evangelietext gsii isch. De Irenäus vo Lyon dagäge hät begründet, wieso s genau vier Evangelie müend sii, und si mit de vier Läbewäse vor em Thron vo Gott vergliche ([[REV.4.7]]); drus sind d Sinnbilder vo de Evangelischte entstande (Mänsch, Löi, Stier, Adler), wo mer speter andersch zueordnet hät als de Irenäus."}},
    {"id": "RCPT-ALL-0012", "subject": "SUM-GROUP-07", "tradition": "liturgy", "period_de": "seit der Alten Kirche, bis heute",
     "text_de": "In vielen Kirchen wird die Apostelgeschichte in der Osterzeit gelesen; in der römisch-katholischen Leseordnung bildet sie von Ostern bis Pfingsten die erste Lesung der Sonntage und Werktage.",
     "sources_de": ["Römisches Messlektionar, Osterzeit"],
     "confidence": "high",
     "gsw": {"period_de": "sit de Alte Chilche, bis hüt",
             "text_de": "I vile Chilche list mer d Apostelgschicht i de Oschterziit; i de römisch-katholische Läseornig isch si vo Oschtere bis Pfingschte di erscht Läsig vo de Sunntig und Wärchtig."}},
    {"id": "RCPT-ALL-0013", "subject": "SUM-GROUP-08", "tradition": "church_fathers", "period_de": "Mitte 2. Jahrhundert; frühes 3. Jahrhundert",
     "text_de": "Marcion stellte als einer der Ersten eine Sammlung von zehn Paulusbriefen zusammen (das «Apostolikon»), ohne die Briefe an Timotheus und Titus, und kürzte sie nach seiner Lehre. Tertullian setzt sich in seinem Werk gegen Marcion mit dieser Sammlung auseinander. Die Kirche überlieferte vierzehn (mit dem Hebräerbrief) bzw. dreizehn Paulusbriefe.",
     "sources_de": ["Tertullian, Gegen Marcion (Adversus Marcionem)", "Athanasius, 39. Osterfestbrief (367): vierzehn Paulusbriefe"],
     "confidence": "high",
     "gsw": {"period_de": "Mitti 2. Jahrhundert; frües 3. Jahrhundert",
             "text_de": "De Marcion hät als eine vo de Erschte e Sammlig vo zää Paulusbrief zämegstellt (s «Apostolikon»), ohni d Brief a de Timotheus und de Titus, und hät si nach sinere Lehr kürzt. De Tertullian setzt sich i sim Wärch gäge de Marcion mit dere Sammlig usenand. D Chilche hät vierzää (mit em Hebräerbrief) bzw. drizää Paulusbrief überliferet."}},
    {"id": "RCPT-ALL-0014", "subject": "SUM-GROUP-09", "tradition": "church_fathers", "period_de": "frühes 4. Jahrhundert",
     "text_de": "Eusebius berichtet, dass sieben Briefe – Jakobus, zwei Petrus-, drei Johannes- und der Judasbrief – «katholische» Briefe genannt werden; das Wort heisst «allgemein». Mehrere von ihnen waren in der Alten Kirche umstritten (vgl. Eusebius, Kirchengeschichte 3,25,3).",
     "sources_de": ["Eusebius, Kirchengeschichte 2,23,25"],
     "confidence": "high",
     "gsw": {"period_de": "frües 4. Jahrhundert",
             "text_de": "De Eusebius verzellt, dass mer sibe Brief – Jakobus, zwei Petrus-, drei Johannes- und de Judasbrief – «katholischi» Brief nännt; s Wort heisst «allgemein». Mehreri devo sind i de Alte Chilche umstritte gsii (vgl. Eusebius, Chilchegschicht 3,25,3)."}},
    {"id": "RCPT-ALL-0015", "subject": "SUM-GROUP-10", "tradition": "church_fathers", "period_de": "3. Jahrhundert; 1522",
     "text_de": "Dionysius von Alexandria verglich Sprache und Stil der Offenbarung mit dem Johannesevangelium und folgerte, sie stamme von einem anderen Johannes. In der östlichen Kirche blieb die Offenbarung lange umstritten; Martin Luther äusserte 1522 in seiner Vorrede ebenfalls Zweifel an ihr.",
     "sources_de": ["Eusebius, Kirchengeschichte 7,25", "Martin Luther, Vorrede auf die Offenbarung (1522)"],
     "confidence": "high",
     "gsw": {"period_de": "3. Jahrhundert; 1522",
             "text_de": "De Dionysius vo Alexandria hät Sprach und Stil vo de Offebarig mit em Johannesevangelium vergliche und gfolgeret, si stammi vo me andere Johannes. I de öschtliche Chilche isch d Offebarig lang umstritte bliibe; de Martin Luther hät 1522 i sinere Vorred au Zwiifel a ire gäussert."}},
]

# Quellenprüfung (docs/QUELLENPRUEFUNG.md)
SOURCE_CHECKS = {
 "RCPT-ALL-0001": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Hieronymus, «Prologus galeatus»",
    "found_at": "https://en.wikipedia.org/wiki/Prologus_Galeatus",
    "finding_de": "Vorrede zu Samuel/Könige (391/392) für die Übersetzung aus dem Hebräischen."
   },
   {
    "source": "Augustinus, Brief 71,5",
    "found_at": "https://www.newadvent.org/fathers/1102071.htm",
    "finding_de": "Widerstand gegen die neue Übersetzung in Oea. Vorher «für rund ein Jahrtausend» ohne Beleg; gestrichen."
   }
  ]
 },
 "RCPT-ALL-0002": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Kapitel- und Verseinteilung",
    "found_at": "https://www.simplycatholic.com/bibles-organization/",
    "finding_de": "Kapitel durch Stephan Langton, Erzbischof von Canterbury, um 1227 (vorher «um 1200»); Verse im Neuen Testament 1551 durch Robert Estienne (dort «Robert Stephens»); Ortsangabe «Genf» und «Pariser Drucker» gestrichen."
   }
  ]
 },
 "RCPT-ALL-0003": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Aristeasbrief",
    "found_at": "https://en.wikipedia.org/wiki/Letter_of_Aristeas",
    "finding_de": "Hellenistische Schrift des 3. oder frühen 2. Jh. v. Chr. (vorher «2. Jh.»); 72 Übersetzer, je sechs aus jedem Stamm; übersetzt wird das Gesetz."
   }
  ]
 },
 "RCPT-ALL-0004": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Marcion; Tertullian, Gegen Marcion",
    "found_at": "https://en.wikipedia.org/wiki/Marcion_of_Sinope",
    "finding_de": "Marcion lehnte den Gott der hebräischen Bibel als Vater Jesu ab, hielt die Schriften aber nicht für falsch; Ausschluss in Rom 144. «Fünf Bücher» Tertullians nicht belegt und gestrichen; Wortlaut präzisiert."
   }
  ]
 },
 "RCPT-ALL-0005": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Athanasius, 39. Osterfestbrief",
    "found_at": "https://earlychurchtexts.com/public/athanasius_39th_festal_letter.htm",
    "finding_de": "367 erstmals genau die 27 Schriften des heutigen Neuen Testaments."
   }
  ]
 },
 "RCPT-ALL-0006": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Babylonischer Talmud, Megilla 29b",
    "found_at": "https://en.wikipedia.org/wiki/Triennial_cycle",
    "finding_de": "Im Land Israel wird die Tora in drei Jahren gelesen, in Babylonien in einem Jahr; der Zyklus beginnt nach dem Laubhüttenfest. «Simchat Tora» an der Fundstelle nicht genannt; Wortlaut angepasst."
   }
  ]
 },
 "RCPT-ALL-0007": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Martin Noth, Überlieferungsgeschichtliche Studien",
    "found_at": "https://en.wikipedia.org/wiki/Martin_Noth",
    "finding_de": "Noth sah die Bücher Josua bis Könige, eng mit dem Deuteronomium verbunden, als einheitliches Geschichtswerk; die Fundstelle nennt die Ausgabe 1957, das Erscheinungsjahr 1943 ist dort nicht belegt."
   },
   {
    "source": "Babylonischer Talmud, Bava Batra 14b",
    "found_at": "https://cojs.org/?p=4832",
    "finding_de": "Propheten: Josua, Richter, Samuel, Könige …; Rut und weitere Bücher bei den Schriften."
   }
  ]
 },
 "RCPT-ALL-0008": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Regel Benedikts, Kapitel 18",
    "found_at": "https://archive.osb.org/rb/text/rbefjo3.html",
    "finding_de": "Der ganze Psalter mit 150 Psalmen soll jede Woche gesungen werden. Ein unbelegter Zusatz zum jüdischen Gebet wurde gestrichen."
   }
  ]
 },
 "RCPT-ALL-0009": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Babylonischer Talmud, Bava Batra 14b",
    "found_at": "https://cojs.org/?p=4832",
    "finding_de": "Reihenfolge der Propheten: Josua, Richter, Samuel, Könige, Jeremia, Ezechiel, Jesaja, die Zwölf; Klagelieder und Daniel bei den Schriften."
   }
  ]
 },
 "RCPT-ALL-0010": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Jesus Sirach, Kapitel 49, Vers 10",
    "found_at": "https://www.biblegateway.com/verse/en/Sirach%2049:10",
    "finding_de": "«die Gebeine der zwölf Propheten»."
   },
   {
    "source": "Babylonischer Talmud, Bava Batra 14b",
    "found_at": "https://cojs.org/?p=4832",
    "finding_de": "«die Zwölf» als ein Eintrag in der Reihe der Propheten."
   }
  ]
 },
 "RCPT-ALL-0011": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Irenäus, Gegen die Häresien 3,11,8",
    "found_at": "https://bkv.unifr.ch/works/cpg-1306/versions/against-heresies/divisions/456/",
    "finding_de": "Es kann nicht mehr und nicht weniger als vier Evangelien geben; Vergleich mit den vier Lebewesen (Löwe, Kalb, Mensch, Adler), bei Irenäus Johannes = Löwe, Markus = Adler."
   },
   {
    "source": "Tatian, Diatessaron",
    "found_at": "https://www.newworldencyclopedia.org/entry/Tatian",
    "finding_de": "Vier Evangelien zu einer Erzählung vereint; in syrischsprachigen Kirchen bis ins 5. Jh. gebräuchlich. Der Verweis auf Eusebius 4,29,6 und die Datierung «um 170–180» waren nicht belegt und wurden gestrichen."
   }
  ]
 },
 "RCPT-ALL-0012": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Apostelgeschichte in der Osterzeit",
    "found_at": "https://liturgy.co.nz/no-old-testament-in-the-easter-season",
    "finding_de": "In der Osterzeit ersetzt die Apostelgeschichte die alttestamentliche Lesung; der Brauch wird auf Augustinus und Kyrill von Jerusalem zurückgeführt. Ein Verweis auf Predigten Augustins ohne Stellenangabe wurde gestrichen."
   }
  ]
 },
 "RCPT-ALL-0013": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Marcions «Apostolikon»",
    "found_at": "https://en.wikipedia.org/wiki/Marcion_of_Sinope",
    "finding_de": "Zehn Paulusbriefe ohne die Pastoralbriefe. «Fünftes Buch, Brief für Brief» und «um 207–208» nicht belegt; gestrichen bzw. allgemeiner gefasst."
   },
   {
    "source": "Athanasius, 39. Osterfestbrief",
    "found_at": "https://earlychurchtexts.com/public/athanasius_39th_festal_letter.htm",
    "finding_de": "Vierzehn Paulusbriefe einschliesslich Hebräerbrief."
   }
  ]
 },
 "RCPT-ALL-0014": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Eusebius, Kirchengeschichte 2,23,25",
    "found_at": "https://www.biola.edu/blogs/good-book-blog/2021/why-the-church-needs-the-catholic-epistles",
    "finding_de": "«der Judasbrief, der selbst einer der sieben sogenannten katholischen ist». Die Begründung «weil sie sich nicht an eine einzelne Gemeinde richten» steht nicht bei Eusebius und wurde gestrichen."
   }
  ]
 },
 "RCPT-ALL-0015": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Dionysius von Alexandria bei Eusebius, Kirchengeschichte 7,25",
    "found_at": "https://earlychristianwritings.com/dionysiusalexandria.html",
    "finding_de": "Nach Sprache, Stil und Charakter nicht vom Verfasser des Johannesevangeliums."
   },
   {
    "source": "Martin Luther, Vorrede auf die Offenbarung (1522)",
    "found_at": "https://www.universitylutheran.church/luther-on-revelation.html",
    "finding_de": "Luther hält das Buch für «weder apostolisch noch prophetisch» und äussert Zweifel."
   }
  ]
 }
}
UNCERTAIN = {}
for _x in RECEPTIONS:
    _x["source_check"] = SOURCE_CHECKS[_x["id"]]
    if _x["id"] in UNCERTAIN:
        _x["uncertain_de"] = UNCERTAIN[_x["id"]]

# Zweite Quellenprüfung durch eine weitere Instanz (2026-10-29)
RECHECK_DE = " Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung, Claude) erneut nachgeschlagen; keine fachliche Prüfung."
RECHECKED = ["RCPT-ALL-0001", "RCPT-ALL-0002", "RCPT-ALL-0003", "RCPT-ALL-0004", "RCPT-ALL-0005", "RCPT-ALL-0006", "RCPT-ALL-0007", "RCPT-ALL-0008", "RCPT-ALL-0009", "RCPT-ALL-0010", "RCPT-ALL-0011", "RCPT-ALL-0012", "RCPT-ALL-0013", "RCPT-ALL-0014", "RCPT-ALL-0015"]
RECHECK_EXTRA = {
 "RCPT-ALL-0002": {
  "source": "Kapiteleinteilung (zweite Prüfung)",
  "found_at": "https://en.wikipedia.org/wiki/Chapters_and_verses_of_the_Bible",
  "finding_de": "Langtons Kapiteleinteilung wird dort auf 1205 datiert, also vor seiner Zeit als Erzbischof (ab 1207); die Angabe «um 1227» aus der ersten Prüfung ist nicht gedeckt und wurde durch «Anfang des 13. Jahrhunderts» ersetzt. Verszählung des Neuen Testaments 1551 durch Estienne bestätigt."
 },
 "RCPT-ALL-0007": {
  "source": "Martin Noth, Überlieferungsgeschichtliche Studien (zweite Prüfung)",
  "found_at": "https://www.deutsche-biographie.de/118588826.html",
  "finding_de": "Die Neue Deutsche Biographie nennt «Überlieferungsgeschichtl. Stud., 1943, ³1967»: Das Erscheinungsjahr 1943 ist belegt; Ergebnis von «teilweise» auf «bestätigt» gesetzt, Unsicherheitsvermerk gestrichen."
 },
 "RCPT-ALL-0009": {
  "source": "Babylonischer Talmud, Bava Batra 14b (zweite Prüfung)",
  "found_at": "https://cojs.org/?p=4832",
  "finding_de": "Reihenfolge der Propheten und der Schriften bestätigt. Der Satz über die christliche Anordnung war missverständlich («vier grosse Propheten und Daniel», obwohl Daniel einer der vier ist) und wurde umformuliert."
 }
}
for _x in RECEPTIONS:
    if _x["id"] in RECHECKED:
        _sc = dict(_x["source_check"])
        _sc["method_de"] = _sc["method_de"] + RECHECK_DE
        if _x["id"] in RECHECK_EXTRA:
            _sc["checked"] = _sc["checked"] + [RECHECK_EXTRA[_x["id"]]]
        _x["source_check"] = _sc

# Prüfvermerk der Prüfrunde vom 2026-10-29 (getrennte Instanz; docs/WEITERDENKEN.md, Feld check)
CHECK = {"date": "2026-10-29", "by": "weitere Instanz (KI)", "limits_de": "Nicht gegen den Urtext geprüft; Zitate aus Büchern ohne Arbeitsübersetzung nicht verglichen; Quellen der Rezeption nur in frei zugänglichen Ausgaben nachgeschlagen; keine fachliche und keine muttersprachliche Prüfung durch eine Person.", "process": "PROC-WEITERDENKEN@1.0"}
# in der Prüfung (oder bei der Zitat-Prüfung am selben Tag) berichtigt
CHECK_CORRECTED = ["RCPT-ALL-0001", "RCPT-ALL-0002", "RCPT-ALL-0003", "RCPT-ALL-0004", "RCPT-ALL-0005", "RCPT-ALL-0006", "RCPT-ALL-0007", "RCPT-ALL-0008", "RCPT-ALL-0009", "RCPT-ALL-0010", "RCPT-ALL-0011", "RCPT-ALL-0012", "RCPT-ALL-0013", "RCPT-ALL-0014", "RCPT-ALL-0015"]
