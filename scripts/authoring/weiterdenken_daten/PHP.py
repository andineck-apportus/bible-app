"""Weiterdenken zum Philipperbrief (Entscheid Andi Neck 2026-10-28): Fragen zum Weiterdenken und «Wie man es gelesen hat»
für alle Abschnitte, Kapitel und das Buch. KI-Entwürfe ohne fachliche Prüfung; Quellen in frei zugänglichen Ausgaben
nachgeschlagen (source_check), soweit möglich.

Prüfvermerk (PROC-WEITERDENKEN@1.0, Schritte 3 und 4): Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung,
Claude) gegen die hochdeutsche Arbeitsübersetzung geprüft: alle 35 Fragen und Hintergrundsätze (offen, nicht suggestiv,
am Text belegt, Zitate per Skript wörtlich verglichen, Stellenmarken), Mundart nach pruefe_mundart; Kernaussagen (gist_de)
der Kernanalysen gegen den Text;
Quellen von 4 der 6 Einträge «Wie man es gelesen hat» erneut
nachgeschlagen (Vermerk im source_check). Grenzen: nicht gegen den Urtext geprüft; Zitate aus Büchern ohne
Arbeitsübersetzung nicht verglichen; Mundart-Zitate nicht an die Mundart-Übersetzungsschicht angeglichen; keine fachliche
und keine muttersprachliche Prüfung durch eine Person."""
DATE = "2026-10-28"
PROCESS = "PROC-WEITERDENKEN@1.0"
TAGS = ["TAG-PHILIPPIANS"]
AUTHORSHIP_DE = "KI-Entwurf (Claude) vom 2026-10-28 (Weiterdenken Philipper, Entscheid Andi Neck); keine fachliche Prüfung."

REFLECTIONS = [
    # Buch
    {"id": "REFL-PHP-0001", "subject": "SUM-BOOK-PHP", "order": 1,
     "question_de": "Wie kann jemand im Gefängnis so viel von Freude schreiben?",
     "note_de": "Paulus liegt in Fesseln ([[PHP.1.13]]) und ruft trotzdem: «Freut euch im Herrn allezeit!» ([[PHP.4.4]]).",
     "gsw": {"question_de": "Wie chan öpper im Gfängnis so vil vo Fröid schriibe?",
             "note_de": "De Paulus liit i Fessle ([[PHP.1.13]]) und rüeft glich: «Fröied eu immer im Herr!» ([[PHP.4.4]])."}},
    {"id": "REFL-PHP-0002", "subject": "SUM-BOOK-PHP", "order": 2,
     "question_de": "Was verbindet Paulus und diese Gemeinde so eng?",
     "note_de": "Er dankt für ihre Gemeinschaft «vom ersten Tag an» ([[PHP.1.5]]) und erinnert daran, dass sie als einzige Gemeinde für ihn sorgte ([[PHP.4.15]]).",
     "gsw": {"question_de": "Was verbindet de Paulus und die Gmeind so äng?",
             "note_de": "Er dankt für iri Gmeinschaft «vom erschte Tag a» ([[PHP.1.5]]) und erinneret dra, dass si als einzigi Gmeind für en gsorget hät ([[PHP.4.15]])."}},
    # Kapitel
    {"id": "REFL-PHP-0003", "subject": "SUM-CH-PHP-001", "order": 1,
     "question_de": "Wie kann jemand zugleich leben und sterben wollen?",
     "note_de": "Paulus weiss nicht, was er wählen soll: bei Christus sein oder um der Philipper willen bleiben ([[PHP.1.22-PHP.1.24]]).",
     "gsw": {"question_de": "Wie chan öpper zgliich wele läbe und stärbe?",
             "note_de": "De Paulus weiss nöd, was er söll wääle: bi Christus sii oder wäge de Philipper bliibe ([[PHP.1.22-PHP.1.24]])."}},
    {"id": "REFL-PHP-0004", "subject": "SUM-CH-PHP-002", "order": 1,
     "question_de": "Was heisst es, sich nach unten zu bewegen statt nach oben?",
     "note_de": "Der Weg Christi führt hinab bis zum Kreuz ([[PHP.2.6-PHP.2.8]]), erst dann hinauf ([[PHP.2.9]]).",
     "gsw": {"question_de": "Was heisst es, sich nach une z bewege statt nach obe?",
             "note_de": "De Wäg vo Christus füert abe bis as Chrüz ([[PHP.2.6-PHP.2.8]]), erscht dänn ufe ([[PHP.2.9]])."}},
    {"id": "REFL-PHP-0005", "subject": "SUM-CH-PHP-003", "order": 1,
     "question_de": "Was wäre für dich Gewinn, was Verlust?",
     "note_de": "Paulus zählt auf, was ihm einmal Gewinn war, und nennt es um Christi willen Verlust ([[PHP.3.5-PHP.3.8]]).",
     "gsw": {"question_de": "Was wär für dich Gwünn, was Verlurscht?",
             "note_de": "De Paulus zellt uf, was ihm emal Gwünn gsii isch, und nännt s wäge Christus Verlurscht ([[PHP.3.5-PHP.3.8]])."}},
    {"id": "REFL-PHP-0006", "subject": "SUM-CH-PHP-004", "order": 1,
     "question_de": "Kann man Freude befehlen?",
     "note_de": "Paulus wiederholt: «Freut euch im Herrn allezeit! Noch einmal sage ich: Freut euch!» ([[PHP.4.4]]).",
     "gsw": {"question_de": "Chan mer Fröid befäle?",
             "note_de": "De Paulus widerholt: «Fröied eu immer im Herr! No einisch säg ich: Fröied eu!» ([[PHP.4.4]])."}},
    # 1,1–2
    {"id": "REFL-PHP-0007", "subject": "TU-PHP-001-001-002", "order": 1,
     "question_de": "Warum nennt sich Paulus hier Knecht und nicht Apostel?",
     "note_de": "Paulus und Timotheus stellen sich als «Knechte Christi Jesu» vor ([[PHP.1.1]]); einen Titel nennt Paulus nicht.",
     "gsw": {"question_de": "Wieso nännt sich de Paulus da Chnächt und nöd Apostel?",
             "note_de": "De Paulus und de Timotheus stelled sich als «Chnächt vo Christus Jesus» vor ([[PHP.1.1]]); en Titel nännt de Paulus nöd."}},
    {"id": "REFL-PHP-0008", "subject": "TU-PHP-001-001-002", "order": 2,
     "question_de": "Wer sind «alle Heiligen» – und gehören die Aufseher und Diakone dazu?",
     "note_de": "Der Brief geht an alle Heiligen in Philippi, «samt den Aufsehern und Diakonen» ([[PHP.1.1]]).",
     "gsw": {"question_de": "Wär sind «alli Heilige» – und ghöred d Ufseher und Diakone dezue?",
             "note_de": "De Brief gaat a alli Heilige z Philippi, «mitsamt de Ufseher und Diakone» ([[PHP.1.1]])."}},
    # 1,3–11
    {"id": "REFL-PHP-0009", "subject": "TU-PHP-001-003-011", "order": 1,
     "question_de": "Wofür bist du anderen Menschen dankbar?",
     "note_de": "Paulus dankt Gott «bei jedem Gedenken an euch» ([[PHP.1.3]]).",
     "gsw": {"question_de": "Für was bisch du andere Mänsche dankbar?",
             "note_de": "De Paulus dankt Gott, «jedesmal, wänn ich a eu dänke» ([[PHP.1.3]])."}},
    {"id": "REFL-PHP-0010", "subject": "TU-PHP-001-003-011", "order": 2,
     "question_de": "Warum soll Liebe an Erkenntnis zunehmen?",
     "note_de": "Paulus betet, dass ihre Liebe an Erkenntnis wächst, «sodass ihr prüfen könnt, worauf es ankommt» ([[PHP.1.9-PHP.1.10]]).",
     "gsw": {"question_de": "Wieso söll Liebi a Erkänntnis zuenää?",
             "note_de": "De Paulus bätet, dass iri Liebi a Erkänntnis wachst, «sodass ir chönd prüefe, worum s gaat» ([[PHP.1.9-PHP.1.10]])."}},
    # 1,12–26
    {"id": "REFL-PHP-0011", "subject": "TU-PHP-001-012-026", "order": 1,
     "question_de": "Kann aus einer Niederlage etwas Gutes werden?",
     "note_de": "Paulus schreibt, seine Gefangenschaft habe «eher zur Förderung des Evangeliums geführt» ([[PHP.1.12]]).",
     "gsw": {"question_de": "Chan us ere Niderlag öppis Guets wärde?",
             "note_de": "De Paulus schriibt, sini Gfangeschaft heb «ehner zum Vorwärtscho vom Evangelium gfüert» ([[PHP.1.12]])."}},
    {"id": "REFL-PHP-0012", "subject": "TU-PHP-001-012-026", "order": 2,
     "question_de": "Ist es gleichgültig, aus welchem Motiv jemand Gutes tut?",
     "note_de": "Manche verkündigen Christus aus Neid und Streitsucht, und Paulus sagt: «Was soll's? … Und darüber freue ich mich» ([[PHP.1.15]]; [[PHP.1.18]]).",
     "gsw": {"question_de": "Isch es gliichgültig, us welem Grund öpper Guets tuet?",
             "note_de": "Es paar verchündiged de Christus us Niid und Striitsucht, und de Paulus seit: «Was solls? … Und drüber fröi ich mich» ([[PHP.1.15]]; [[PHP.1.18]])."}},
    {"id": "REFL-PHP-0013", "subject": "TU-PHP-001-012-026", "order": 3,
     "question_de": "Wie würdest du den Satz «Für mich ist das Leben …» zu Ende führen?",
     "note_de": "Paulus schreibt: «Für mich ist das Leben Christus und das Sterben Gewinn» ([[PHP.1.21]]).",
     "gsw": {"question_de": "Wie würdsch du de Satz «Für mich isch s Läbe …» fertig mache?",
             "note_de": "De Paulus schriibt: «Dänn für mich isch s Läbe Christus und s Sterbe Gwünn» ([[PHP.1.21]])."}},
    # 1,27–30
    {"id": "REFL-PHP-0014", "subject": "TU-PHP-001-027-030", "order": 1,
     "question_de": "Was heisst es, als «Bürger» zu leben, wie es dem Evangelium entspricht?",
     "note_de": "Paulus wählt ein Wort aus dem städtischen Leben: «Lebt als Bürger» ([[PHP.1.27]]); Philippi war eine römische Kolonie ([[ACT.16.12]]).",
     "gsw": {"question_de": "Was heisst es, als «Bürger» z läbe, wie s em Evangelium entspricht?",
             "note_de": "De Paulus wäält es Wort us em Stadtläbe: «Läbed als Bürger» ([[PHP.1.27]]); Philippi isch e römischi Kolonie gsii ([[ACT.16.12]])."}},
    {"id": "REFL-PHP-0015", "subject": "TU-PHP-001-027-030", "order": 2,
     "question_de": "Kann Leiden ein Geschenk sein?",
     "note_de": "Paulus schreibt, es sei ihnen «geschenkt», nicht nur an Christus zu glauben, sondern auch für ihn zu leiden ([[PHP.1.29]]).",
     "gsw": {"question_de": "Chan Liide es Gschänk sii?",
             "note_de": "De Paulus schriibt, es seig ine «gschänkt», nöd nu a Christus z glaube, sondern au für en z liide ([[PHP.1.29]])."}},
    # 2,1–11
    {"id": "REFL-PHP-0016", "subject": "TU-PHP-002-001-011", "order": 1,
     "question_de": "Was müsste sich ändern, wenn jeder auf das achtet, was den anderen dient?",
     "note_de": "«Jeder achte nicht nur auf das Eigene, sondern jeder auch auf das der anderen» ([[PHP.2.4]]).",
     "gsw": {"question_de": "Was müessti sich ändere, wänn jede uf das luegt, was de andere dient?",
             "note_de": "«Jede söll nöd nu uf s Eige luege, sondern jede au uf das vo de andere» ([[PHP.2.4]])."}},
    {"id": "REFL-PHP-0017", "subject": "TU-PHP-002-001-011", "order": 2,
     "question_de": "Was bedeutet es, an Gottgleichheit nicht festzuhalten wie an einer Beute?",
     "note_de": "Christus «hielt es nicht für ein Beutestück, Gott gleich zu sein», sondern entäusserte sich ([[PHP.2.6-PHP.2.7]]).",
     "gsw": {"question_de": "Was bedüütet s, a de Gottgliichheit nöd feschthebe wie a ere Büüt?",
             "note_de": "De Christus «hät es nöd für e Büüt ghalte, Gott gliich z sii», sondern «hät sich sälber läär gmacht» ([[PHP.2.6-PHP.2.7]])."}},
    {"id": "REFL-PHP-0018", "subject": "TU-PHP-002-001-011", "order": 3,
     "question_de": "Wer beugt hier die Knie – und wer bekennt?",
     "note_de": "«Im Himmel und auf der Erde und unter der Erde» soll jedes Knie sich beugen ([[PHP.2.10-PHP.2.11]]); die Worte klingen an [[ISA.45.23]] an.",
     "gsw": {"question_de": "Wär böigt da d Chnü – und wär bekännt?",
             "note_de": "«Im Himmel und uf de Erde und under de Erde» söll sich jedes Chnü böige ([[PHP.2.10-PHP.2.11]]); d Wort tönd a [[ISA.45.23]] aa."}},
    # 2,12–18
    {"id": "REFL-PHP-0019", "subject": "TU-PHP-002-012-018", "order": 1,
     "question_de": "Wer wirkt hier – die Philipper oder Gott?",
     "note_de": "«Wirkt eure Rettung aus … denn Gott ist es, der in euch wirkt» ([[PHP.2.12-PHP.2.13]]).",
     "gsw": {"question_de": "Wär würkt da – d Philipper oder Gott?",
             "note_de": "«Mit Furcht und Zittere schaffed a eurer Rettig. Dänn Gott isch es, wo i eu würkt» ([[PHP.2.12-PHP.2.13]])."}},
    {"id": "REFL-PHP-0020", "subject": "TU-PHP-002-012-018", "order": 2,
     "question_de": "Warum ist ausgerechnet Murren so wichtig?",
     "note_de": "«Tut alles ohne Murren und Widerrede» ([[PHP.2.14]]) – erst dann folgt das Bild von den Lichtern in der Welt ([[PHP.2.15]]).",
     "gsw": {"question_de": "Wieso isch usgrächnet s Murre so wichtig?",
             "note_de": "«Mached alles ohni Muule und Widerred» ([[PHP.2.14]]) – erscht dänn chunnt s Bild vo de Liechter i de Wält ([[PHP.2.15]])."}},
    # 2,19–30
    {"id": "REFL-PHP-0021", "subject": "TU-PHP-002-019-030", "order": 1,
     "question_de": "Wer ist für dich jemand, der sich «aufrichtig» um andere sorgt?",
     "note_de": "Paulus sagt über Timotheus, er habe keinen, der sich so aufrichtig sorgen wird ([[PHP.2.20]]).",
     "gsw": {"question_de": "Wär isch für dich öpper, wo sich «ufrichtig» um anderi sorget?",
             "note_de": "De Paulus seit über de Timotheus, er heb keine, wo sich so ufrichtig wird sorge ([[PHP.2.20]])."}},
    {"id": "REFL-PHP-0022", "subject": "TU-PHP-002-019-030", "order": 2,
     "question_de": "Warum ist Epaphroditus unruhig, weil die Philipper von seiner Krankheit gehört haben?",
     "note_de": "Nicht seine Krankheit beunruhigt ihn, sondern die Sorge der anderen ([[PHP.2.26]]).",
     "gsw": {"question_de": "Wieso isch de Epaphroditus unrüeig, wil d Philipper vo sinere Chrankheit ghört händ?",
             "note_de": "Nöd sini Chrankheit macht en unrüeig, sondern d Sorg vo de andere ([[PHP.2.26]])."}},
    # 3,1–11
    {"id": "REFL-PHP-0023", "subject": "TU-PHP-003-001-011", "order": 1,
     "question_de": "Warum zählt Paulus erst seine Vorzüge auf, bevor er sie Verlust nennt?",
     "note_de": "Er nennt Herkunft, Gesetzestreue und Eifer ([[PHP.3.5-PHP.3.6]]) und rechnet dann um: Was Gewinn war, hält er für Verlust ([[PHP.3.7]]).",
     "gsw": {"question_de": "Wieso zellt de Paulus zerscht sini Vorzüg uf, bevor er sie Verlurscht nännt?",
             "note_de": "Er nännt Herkunft, Gsetzestreui und Iifer ([[PHP.3.5-PHP.3.6]]) und rächnet dänn um: Was Gwünn gsii isch, hebt er für Verlurscht ([[PHP.3.7]])."}},
    {"id": "REFL-PHP-0024", "subject": "TU-PHP-003-001-011", "order": 2,
     "question_de": "Gegen wen richten sich die harten Worte am Anfang – und wie geht man heute mit solcher Polemik um?",
     "note_de": "Paulus warnt: «Gebt acht auf die Hunde … gebt acht auf die Zerschneidung!» ([[PHP.3.2]]); gemeint sind wohl Lehrer, die bei den Gemeinden für die Beschneidung warben, nicht das jüdische Volk – Paulus zählt sich selbst zu Israel ([[PHP.3.5]]).",
     "gsw": {"question_de": "Gäge wän richted sich di harte Wort am Aafang – und wie gaat mer hüt mit settiger Polemik um?",
             "note_de": "De Paulus warnt: «Passed uf d Hünd uf … passed uf d Zerschniidig uf!» ([[PHP.3.2]]); gmeint sind wohl Lehrer, wo bi de Gmeinde für d Beschniidig gworbe händ, nöd s jüdisch Volk – de Paulus zellt sich sälber zu Israel ([[PHP.3.5]])."}},
    {"id": "REFL-PHP-0025", "subject": "TU-PHP-003-001-011", "order": 3,
     "question_de": "Was heisst es, jemanden zu «erkennen» – mehr als etwas über ihn zu wissen?",
     "note_de": "Paulus will Christus erkennen, «die Kraft seiner Auferstehung und die Gemeinschaft mit seinen Leiden» ([[PHP.3.10]]).",
     "gsw": {"question_de": "Was heisst es, öpper z «erchänne» – meh als öppis über en z wüsse?",
             "note_de": "De Paulus wott de Christus erchänne, «d Chraft vo sinere Uferstehig und d Gmeinschaft mit sine Liide» ([[PHP.3.10]])."}},
    # 3,12–21
    {"id": "REFL-PHP-0026", "subject": "TU-PHP-003-012-021", "order": 1,
     "question_de": "Was hilft es, zu vergessen, was hinter einem liegt?",
     "note_de": "«Ich vergesse, was hinter mir liegt, und strecke mich nach dem aus, was vor mir liegt» ([[PHP.3.13]]).",
     "gsw": {"question_de": "Was hilft s, z vergässe, was hinder eim liit?",
             "note_de": "«Ich vergiss, was hinder mir liit, und streck mich nach dem us, was vor mir liit» ([[PHP.3.13]])."}},
    {"id": "REFL-PHP-0027", "subject": "TU-PHP-003-012-021", "order": 2,
     "question_de": "Darf man sagen: «Werdet miteinander meine Nachahmer»?",
     "note_de": "Paulus sagt es ([[PHP.3.17]]) – nachdem er gerade betont hat, er habe das Ziel noch nicht erreicht ([[PHP.3.12]]).",
     "gsw": {"question_de": "Dörf mer säge: «Wärded mitenand mini Nachahmer»?",
             "note_de": "De Paulus seit s ([[PHP.3.17]]) – nachdem er grad betont hät, er heb s Ziel no nöd erreicht ([[PHP.3.12]])."}},
    {"id": "REFL-PHP-0028", "subject": "TU-PHP-003-012-021", "order": 3,
     "question_de": "Was bedeutet der Satz «unser Bürgerrecht ist im Himmel» für das Leben auf der Erde?",
     "note_de": "«Unser Bürgerrecht ist im Himmel, von wo wir auch den Retter erwarten» ([[PHP.3.20]]).",
     "gsw": {"question_de": "Was bedüütet de Satz «öises Bürgerrächt isch im Himmel» für s Läbe uf de Ärde?",
             "note_de": "«Öises Bürgerrächt isch im Himmel, vo wo mir au de Retter erwarted» ([[PHP.3.20]])."}},
    # 4,1–9
    {"id": "REFL-PHP-0029", "subject": "TU-PHP-004-001-009", "order": 1,
     "question_de": "Warum nennt Paulus den Streit zweier Frauen beim Namen?",
     "note_de": "Euodia und Syntyche haben «im Evangelium mit mir gekämpft», schreibt Paulus ([[PHP.4.2-PHP.4.3]]); er bittet beide gleich und ergreift keine Partei.",
     "gsw": {"question_de": "Wieso nännt de Paulus de Striit vo zwei Fraue bim Name?",
             "note_de": "D Euodia und d Syntyche händ «im Evangelium mit mir kämpft», schriibt de Paulus ([[PHP.4.2-PHP.4.3]]); er bittet beidi gliich und nimmt kei Partei."}},
    {"id": "REFL-PHP-0030", "subject": "TU-PHP-004-001-009", "order": 2,
     "question_de": "Was würdest du vor Gott bringen, wenn du dich um nichts sorgen müsstest?",
     "note_de": "«Sorgt euch um nichts, sondern in allem lasst eure Anliegen … vor Gott kund werden» ([[PHP.4.6]]).",
     "gsw": {"question_de": "Was würdsch du vor Gott bringe, wänn d dich um nüüt müesstisch sorge?",
             "note_de": "«Mached eu kei Sorge, sondern i allem bringed eui Aaliige dur Bätte und Flehe mit Dank vor Gott» ([[PHP.4.6]])."}},
    {"id": "REFL-PHP-0031", "subject": "TU-PHP-004-001-009", "order": 3,
     "question_de": "Worauf richtest du deine Gedanken?",
     "note_de": "Paulus zählt auf, was wahr, ehrbar, gerecht, rein, liebenswert ist und einen guten Ruf hat ([[PHP.4.8]]) – Werte, die auch nichtchristliche Zeitgenossen kannten.",
     "gsw": {"question_de": "Uf was richtisch du dini Gedanke?",
             "note_de": "De Paulus zellt uf, was wahr, ehrbar, grächt, rein, liebeswärt isch und en guete Ruef hät ([[PHP.4.8]]) – Wärt, wo au nöd-chrischtlichi Ziitgenosse kännt händ."}},
    # 4,10–20
    {"id": "REFL-PHP-0032", "subject": "TU-PHP-004-010-020", "order": 1,
     "question_de": "Wie lernt man, mit wenig und mit viel auszukommen?",
     "note_de": "Paulus sagt, er sei «eingeweiht», satt zu sein und zu hungern ([[PHP.4.12]]) – er spricht von etwas Gelerntem.",
     "gsw": {"question_de": "Wie lernt mer, mit wenig und mit vil uszcho?",
             "note_de": "De Paulus seit, er seig «iigweiht», satt z sii und z hungere ([[PHP.4.12]]) – er redt vo öppis Glehrtem."}},
    {"id": "REFL-PHP-0033", "subject": "TU-PHP-004-010-020", "order": 2,
     "question_de": "Warum sagt Paulus hier nicht einfach Danke?",
     "note_de": "Er freut sich über die Gabe, betont aber zweimal, er sei nicht darauf aus ([[PHP.4.11]]; [[PHP.4.17]]).",
     "gsw": {"question_de": "Wieso seit de Paulus da nöd eifach Danke?",
             "note_de": "Er fröit sich über d Gab, betont aber zwei Mal, er seig nöd druf us ([[PHP.4.11]]; [[PHP.4.17]])."}},
    # 4,21–23
    {"id": "REFL-PHP-0034", "subject": "TU-PHP-004-021-023", "order": 1,
     "question_de": "Was bedeutet es, dass Grüsse «aus dem Haus des Kaisers» kommen?",
     "note_de": "Paulus richtet Grüsse aus, «besonders aber die aus dem Haus des Kaisers» ([[PHP.4.22]]); wer gemeint ist, sagt der Text nicht.",
     "gsw": {"question_de": "Was bedüütet s, dass Grüess «us em Huus vom Kaiser» chömed?",
             "note_de": "De Paulus richtet Grüess us, «bsunders aber die us em Huus vom Kaiser» ([[PHP.4.22]]); wär gmeint isch, seit de Text nöd."}},
    {"id": "REFL-PHP-0035", "subject": "TU-PHP-004-021-023", "order": 2,
     "question_de": "Wem würdest du zum Schluss eines Briefes «Gnade» wünschen?",
     "gsw": {"question_de": "Wem würdsch du am Schluss vo me Brief «Gnad» wünsche?"}},
]

RECEPTIONS = [
    {"id": "RCPT-PHP-0001", "subject": "SUM-BOOK-PHP", "tradition": "church_fathers", "period_de": "erste Hälfte 2. Jahrhundert",
     "text_de": "Polykarp, Bischof von Smyrna, schreibt selbst einen Brief an die Gemeinde in Philippi. Darin erinnert er daran, dass Paulus bei ihnen war und ihnen Briefe geschrieben hat, in die sie sich vertiefen sollen – ein früher Hinweis, dass der Philipperbrief dort gelesen wurde.",
     "sources_de": ["Polykarp, Brief an die Philipper 3,2"],
     "confidence": "high",
     "gsw": {"period_de": "erschti Hälfti 2. Jahrhundert",
             "text_de": "De Polykarp, Bischof vo Smyrna, schriibt sälber en Brief a d Gmeind z Philippi. Drin erinneret er dra, dass de Paulus bi ine gsii isch und ine Brief gschribe hät, wo si sich söled drii vertüüfe – en früene Hiiwiis, dass mer de Philipperbrief dört gläse hät."}},
    {"id": "RCPT-PHP-0002", "subject": "TU-PHP-002-001-011", "tradition": "modern_scholarship", "period_de": "seit 1927/1928",
     "text_de": "Ernst Lohmeyer gliederte [[PHP.2.6-PHP.2.11]] als Lied in sechs Strophen zu je drei Zeilen; seine Untersuchung gilt als grundlegend. Seither wird der Abschnitt oft «Christushymnus» genannt; ob Paulus ihn selbst verfasst oder übernommen hat und wie er zu gliedern ist, wird bis heute diskutiert.",
     "sources_de": ["Ernst Lohmeyer, Kyrios Jesus. Eine Untersuchung zu Phil. 2,5–11 (1927/1928)"],
     "confidence": "high",
     "gsw": {"period_de": "sit 1927/1928",
             "text_de": "De Ernst Lohmeyer hät [[PHP.2.6-PHP.2.11]] als Lied i sächs Strophe zu je drei Ziile gliederet; sini Untersuechig gilt als grundleggend. Sitdem nännt mer de Abschnitt oft «Christushymnus»; öb de Paulus en sälber verfasst oder übernoo hät und wie mer en söll gliedere, wird bis hüt diskutiert."}},
    {"id": "RCPT-PHP-0003", "subject": "TU-PHP-002-001-011", "tradition": "liturgy", "period_de": "bis heute",
     "text_de": "In der römisch-katholischen Leseordnung ist der Christushymnus ([[PHP.2.6-PHP.2.11]]) die zweite Lesung am Palmsonntag, zu Beginn der Karwoche; auch die ökumenische Leseordnung vieler evangelischer Kirchen (Revised Common Lectionary) sieht ihn für diesen Tag vor.",
     "sources_de": ["Römisches Messlektionar, Palmsonntag", "Revised Common Lectionary, Palmsonntag"],
     "confidence": "high",
     "gsw": {"period_de": "bis hüt",
             "text_de": "I de römisch-katholische Läseornig isch de Christushymnus ([[PHP.2.6-PHP.2.11]]) di zweit Läsig am Palmsunntig, am Aafang vo de Karwuche; au di ökumenisch Läseornig vo vile evangelische Chilche (Revised Common Lectionary) gseht en für dä Tag vor."}},
    {"id": "RCPT-PHP-0004", "subject": "TU-PHP-004-001-009", "tradition": "liturgy", "period_de": "seit dem Mittelalter",
     "text_de": "Der dritte Adventssonntag heisst in der westlichen Kirche «Gaudete» («Freut euch») nach dem Eröffnungsvers der Messe, der [[PHP.4.4-PHP.4.5]] aufnimmt: «Freut euch im Herrn allezeit … Der Herr ist nahe.» Die Freude mitten in der Vorbereitungszeit wird oft mit rosa Gewändern sichtbar gemacht.",
     "sources_de": ["Introitus «Gaudete in Domino semper» zum dritten Adventssonntag"],
     "confidence": "high",
     "gsw": {"period_de": "sit em Mittelalter",
             "text_de": "De dritt Adväntssunntig heisst i de westliche Chilche «Gaudete» («Fröied eu») nach em Iigangsvers vo de Mäss, wo [[PHP.4.4-PHP.4.5]] ufnimmt: «Fröied eu im Herr allziit … De Herr isch nöch.» D Fröid mitts i de Vorbereitigsziit macht mer oft mit rosa Gwänder sichtbar."}},
    {"id": "RCPT-PHP-0005", "subject": "TU-PHP-004-001-009", "tradition": "music", "period_de": "um 1683–1685",
     "text_de": "Henry Purcell vertont [[PHP.4.4-PHP.4.7]] in englischer Sprache als Anthem «Rejoice in the Lord alway»; wegen der Glockenmotive im Vorspiel heisst es auch «Bell Anthem».",
     "sources_de": ["Henry Purcell, «Rejoice in the Lord alway», Z. 49"],
     "confidence": "high",
     "gsw": {"period_de": "um 1683–1685",
             "text_de": "De Henry Purcell vertont [[PHP.4.4-PHP.4.7]] uf Änglisch als Anthem «Rejoice in the Lord alway»; wäge de Glogge-Motiv im Vorspil heisst s au «Bell Anthem»."}},
    {"id": "RCPT-PHP-0006", "subject": "TU-PHP-001-012-026", "tradition": "music", "period_de": "vor 1608; 1609",
     "text_de": "Das evangelische Sterbelied «Christus, der ist mein Leben, Sterben ist mein Gewinn» nimmt [[PHP.1.21]] auf. Der Text ist vor 1608 entstanden, sein Dichter unbekannt; die Melodie von Melchior Vulpius erschien 1609 in Jena. Johann Sebastian Bach verwendet das Lied in seiner Kantate BWV 95.",
     "sources_de": ["Kirchenlied «Christus, der ist mein Leben» (Text vor 1608, Melodie Melchior Vulpius, Jena 1609)", "Johann Sebastian Bach, Kantate «Christus, der ist mein Leben», BWV 95"],
     "confidence": "high",
     "gsw": {"period_de": "vor 1608; 1609",
             "text_de": "S evangelisch Stärbelied «Christus, der ist mein Leben, Sterben ist mein Gewinn» nimmt [[PHP.1.21]] uf. De Text isch vor 1608 entstande, de Dichter isch unbekannt; d Melodie vom Melchior Vulpius isch 1609 z Jena erschine. De Johann Sebastian Bach bruucht s Lied i sinere Kantate BWV 95."}},
]

# Quellenprüfung (docs/QUELLENPRUEFUNG.md)
SOURCE_CHECKS = {
 "RCPT-PHP-0001": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Polykarp, Brief an die Philipper, Kapitel 3",
    "found_at": "https://www.newadvent.org/fathers/0136.htm",
    "finding_de": "Paulus hat ihnen, als er abwesend war, geschrieben; die Briefe sollen sie im Glauben aufbauen."
   }
  ]
 },
 "RCPT-PHP-0002": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Ernst Lohmeyer, Kyrios Jesus",
    "found_at": "https://tyndalebulletin.org/article/30672-the-christ-hymn-in-philippians-2-5-11.pdf; https://en.wikipedia.org/wiki/Ernst_Lohmeyer",
    "finding_de": "Lohmeyer gliederte den Hymnus in sechs Strophen zu je drei Zeilen; seine Arbeit gilt als grundlegend. Erscheinungsangabe «1927/28», vorher «1928»; die Aussage, Paulus habe den Hymnus vorgefunden, ist dort nicht als Lohmeyers These belegt und wurde gestrichen."
   }
  ]
 },
 "RCPT-PHP-0003": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Leseordnungen Palmsonntag",
    "found_at": "https://www.devout.org/lectionary/palm-sunday-a; https://www.workingpreacher.org/commentaries/revised-common-lectionary/sunday-of-the-passion-palm-sunday-2/commentary-on-philippians-25-11-4",
    "finding_de": "[[PHP.2.6-PHP.2.11]] ist zweite Lesung am Palmsonntag (Lesejahr A belegt); auch das Revised Common Lectionary sieht den Christushymnus für den Palmsonntag vor. Vorher «alle Lesejahre» und «viele andere Kirchen» ohne Beleg; präzisiert."
   }
  ]
 },
 "RCPT-PHP-0004": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Introitus «Gaudete in Domino semper»",
    "found_at": "https://archives.themiscellany.org/2017/12/17/history-and-traditions-of-gaudete-sunday/",
    "finding_de": "Der dritte Adventssonntag heisst nach dem Eröffnungsvers aus [[PHP.4.4-PHP.4.5]]; rosa Gewänder möglich."
   }
  ]
 },
 "RCPT-PHP-0005": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Henry Purcell, «Rejoice in the Lord alway», Z. 49",
    "found_at": "https://en.wikipedia.org/wiki/Rejoice_in_the_Lord_alway",
    "finding_de": "Um 1683–1685 (vorher «um 1682–1685»); Text [[PHP.4.4-PHP.4.7]]; «Bell Anthem» wegen der glockenartigen Bassfigur."
   }
  ]
 },
 "RCPT-PHP-0006": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Kirchenlied «Christus, der ist mein Leben»",
    "found_at": "https://bach-cantatas.com/CM/Christus-der-ist-mein-Leben.htm",
    "finding_de": "Text vor 1608, Dichter unbekannt; Melodie von Melchior Vulpius, gedruckt Jena 1609; Sterbelied. Vorher «erschien 1609 in Jena» und «bis heute bei Beerdigungen» – berichtigt bzw. gestrichen."
   },
   {
    "source": "Bach, BWV 95",
    "found_at": "https://en.wikipedia.org/wiki/Christus,_der_ist_mein_Leben,_BWV_95",
    "finding_de": "Bachs Kantate trägt den Titel des Liedes."
   }
  ]
 }
}
for _x in RECEPTIONS:
    _x["source_check"] = SOURCE_CHECKS[_x["id"]]

# Zweite Quellenprüfung durch eine weitere Instanz (2026-10-29)
RECHECK_DE = " Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung, Claude) erneut nachgeschlagen; keine fachliche Prüfung."
RECHECKED = ["RCPT-PHP-0002", "RCPT-PHP-0003", "RCPT-PHP-0005", "RCPT-PHP-0006"]
RECHECK_EXTRA = {}
for _x in RECEPTIONS:
    if _x["id"] in RECHECKED:
        _sc = dict(_x["source_check"])
        _sc["method_de"] = _sc["method_de"] + RECHECK_DE
        if _x["id"] in RECHECK_EXTRA:
            _sc["checked"] = _sc["checked"] + [RECHECK_EXTRA[_x["id"]]]
        _x["source_check"] = _sc

# Prüfvermerk der Prüfrunde vom 2026-10-29 (getrennte Instanz; docs/WEITERDENKEN.md, Feld check)
CHECK = {"date": "2026-10-29", "by": "weitere Instanz (KI)", "limits_de": "Nicht gegen den Urtext geprüft, sondern gegen die hochdeutsche und die Mundart-Arbeitsübersetzung (Zitate per Skript wörtlich verglichen); Quellen der Rezeption nur in frei zugänglichen Ausgaben nachgeschlagen; keine fachliche und keine muttersprachliche Prüfung durch eine Person.", "process": "PROC-WEITERDENKEN@1.0"}
# in der Prüfung (oder bei der Zitat-Prüfung am selben Tag) berichtigt
CHECK_CORRECTED = ["RCPT-PHP-0002", "RCPT-PHP-0003", "RCPT-PHP-0005", "RCPT-PHP-0006", "REFL-PHP-0001", "REFL-PHP-0002", "REFL-PHP-0006", "REFL-PHP-0007", "REFL-PHP-0009", "REFL-PHP-0010", "REFL-PHP-0011", "REFL-PHP-0012", "REFL-PHP-0013", "REFL-PHP-0016", "REFL-PHP-0017", "REFL-PHP-0018", "REFL-PHP-0019", "REFL-PHP-0020", "REFL-PHP-0023", "REFL-PHP-0024", "REFL-PHP-0026", "REFL-PHP-0027", "REFL-PHP-0028", "REFL-PHP-0029", "REFL-PHP-0030", "REFL-PHP-0033"]
