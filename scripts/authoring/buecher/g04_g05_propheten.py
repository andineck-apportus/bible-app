"""Hintergrund damals je Buch: Propheten (Jesaja bis Maleachi, ohne Obadja).

KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
Erzeugen mit: python3 scripts/authoring/hintergrund_buecher.py g04_g05_propheten
"""
from hintergrund_buecher import T

IP = "CTX-HIST-ISRAEL-IRON-PERSIAN"
TAYLOR = "Taylor-Prisma Sanheribs (um 691 v. Chr.)"
LACHISH_RELIEFS = "Lachisch-Reliefs aus dem Palast Sanheribs in Ninive"

NOTES = [
    # ---------------------------------------------------------------- Jesaja
    {"id": "BG-ISA-BOOK-0001", "book": "ISA", "context": IP, "confidence": "probable",
     "topic": "Jesaja in Jerusalem: Prophet unter assyrischem Druck",
     "text": "Nach der Überschrift wirkte Jesaja, Sohn des Amoz, in Jerusalem unter den Königen Usija, Jotam, Ahas "
             "und Hiskija ([[ISA.1.1]]); sein Name bedeutet «JHWH ist Rettung». Seine Berufung fällt ins Todesjahr "
             "Usijas, um 740 v. Chr. ([[ISA.6.1]]). Damals stiess Assyrien nach Westen vor: Krieg Arams und Israels "
             "gegen Juda um 734–732 v. Chr. ([[ISA.7.1-ISA.7.9]]), Fall Samarias 722/720 v. Chr., Feldzug Sanheribs "
             "701 v. Chr., der Juda verwüstete, Jerusalem aber nicht einnahm ([[ISA.36.1-ISA.37.38]]). Sanherib "
             "schreibt selbst, er habe Hiskija in Jerusalem «wie einen Vogel im Käfig» eingeschlossen. Kennzeichnend "
             "für das ganze Buch ist der Gottesname «der Heilige Israels» ([[ISA.1.4]]; [[ISA.41.14]]). Die "
             "Erzählungen in [[ISA.36.1-ISA.39.8]] stehen fast gleich in [[2KI.18.13-2KI.20.19]].",
     "uncertain": "Welche Worte in [[ISA.1.1-ISA.39.8]] auf Jesaja selbst zurückgehen, ist umstritten; viele Forscher "
                  "halten etwa [[ISA.13.1-ISA.14.23]] und [[ISA.24.1-ISA.27.13]] für spätere Teile, traditionelle "
                  "Ausleger schreiben sie Jesaja zu. Ob die Erzählungen zuerst im Königebuch oder im Jesajabuch "
                  "standen, ist offen. Den Abzug der Assyrer 701 v. Chr. ([[ISA.37.36-ISA.37.37]]) erklären Bibel "
                  "und assyrische Quellen verschieden; Sanherib berichtet von Belagerung und Tribut, nicht von Verlusten.",
     "evidence_refs": ["ISA.1.1", "ISA.6.1", "ISA.7.1-ISA.7.9", "ISA.36.1-ISA.37.38", "2KI.18.13-2KI.20.19"],
     "sources": [TAYLOR, LACHISH_RELIEFS],
     "terms": [T("heb", "יְשַׁעְיָהוּ", "Jesaja: «JHWH ist Rettung»", "jeschajahu"),
               T("heb", "קְדוֹשׁ יִשְׂרָאֵל", "der Heilige Israels", "kedosch jisra'el")],
     "gsw": {"topic": "De Jesaja z Jerusalem: Prophet under assyrischem Druck",
             "text": "Nach de Überschrift hät de Jesaja, de Sohn vom Amoz, z Jerusalem under de König Usija, Jotam, "
                     "Ahas und Hiskija gwürkt ([[ISA.1.1]]); sin Name heisst «JHWH isch Rettig». Sini Berüefig "
                     "fallt is Todesjaar vom Usija, um 740 v. Chr. ([[ISA.6.1]]). Dänn isch Assyrie gäge Weschte "
                     "vorgstosse: Chrieg vo Aram und Israel gäge Juda um 734–732 v. Chr. ([[ISA.7.1-ISA.7.9]]), Fall "
                     "vo Samaria 722/720 v. Chr., Feldzug vom Sanherib 701 v. Chr., wo Juda verwüeschtet, Jerusalem "
                     "aber nöd iignoo hät ([[ISA.36.1-ISA.37.38]]). De Sanherib schriibt sälber, er heg de Hiskija z "
                     "Jerusalem «wie en Vogel im Chäfig» iigschlosse. Typisch für s ganz Buech isch de Gottesname "
                     "«de Heilig vo Israel» ([[ISA.1.4]]; [[ISA.41.14]]). D Verzellige i [[ISA.36.1-ISA.39.8]] "
                     "stönd fascht gliich i [[2KI.18.13-2KI.20.19]].",
             "uncertain": "Weli Wort i [[ISA.1.1-ISA.39.8]] uf de Jesaja sälber zruggönd, isch umstritte; vili "
                          "Forscher halted öppe [[ISA.13.1-ISA.14.23]] und [[ISA.24.1-ISA.27.13]] für spööteri "
                          "Teil, traditionelli Usleger schriibed si em Jesaja zue. Öb d Verzellige zerscht im "
                          "Königebuech oder im Jesajabuech gstande sind, isch offe. De Abzug vo de Assyrer 701 v. "
                          "Chr. ([[ISA.37.36-ISA.37.37]]) erklääred d Bible und d assyrische Quälle verschide; de "
                          "Sanherib bricht vo Belagerig und Tribut, nöd vo Verluscht.",
             "terms": ["Jesaja: «JHWH isch Rettig»", "de Heilig vo Israel"]}},
    {"id": "BG-ISA-BOOK-0002", "book": "ISA", "context": IP, "confidence": "probable",
     "topic": "Trost für Verbannte und die Grosse Jesajarolle",
     "text": "Ab [[ISA.40.1]] ändert sich die Lage: Jerusalems Schuld gilt als abgetragen, die Verbannten sollen aus "
             "Babel heimkehren ([[ISA.48.20]]), und der Perserkönig Kyros, der Babylon 539 v. Chr. einnahm, wird mit "
             "Namen genannt ([[ISA.44.28]]; [[ISA.45.1]]). Seit dem späten 18. Jahrhundert schreiben viele Forscher "
             "[[ISA.40.1-ISA.55.13]] einem ungenannten Propheten im Exil zu («Deuterojesaja»), seit Bernhard Duhm "
             "(1892) [[ISA.56.1-ISA.66.24]] einem späteren in Jerusalem («Tritojesaja»). Traditionelle Ausleger "
             "sehen das ganze Buch als Werk Jesajas, der Kyros vorausgesagt habe; schon Jesus Sirach schreibt Jesaja "
             "den Trost für Zion zu ([[SIR.48.24]]), und das Neue Testament ([[MAT.3.3]]; [[JHN.12.38-JHN.12.41]]) "
             "führt diese Kapitel unter Jesajas Namen an. Die Grosse Jesajarolle aus Qumran (um 125 v. Chr.) enthält alle 66 Kapitel als ein Buch; "
             "trotz vieler kleiner Abweichungen stimmt sie weitgehend mit den rund tausend Jahre jüngeren "
             "mittelalterlichen Handschriften überein.",
     "uncertain": "Ob die Kapitel von einem, zwei oder drei Verfassern stammen, ist zwischen traditioneller und "
                  "historisch-kritischer Auslegung umstritten. Viele Forscher sehen heute statt dreier getrennter "
                  "Bücher ein über Generationen fortgeschriebenes Buch; die Grenze bei [[ISA.56.1]] und der Anteil "
                  "späterer Zusätze sind auch unter ihnen umstritten. Die Rolle belegt die Gestalt des Buches im "
                  "2. Jahrhundert v. Chr., nicht seine Entstehung.",
     "evidence_refs": ["ISA.40.1", "ISA.44.28", "ISA.45.1", "ISA.48.20", "SIR.48.24", "MAT.3.3"],
     "sources": ["Grosse Jesajarolle 1QIsaᵃ (Qumran, um 125 v. Chr.)", "Kyros-Zylinder (nach 539 v. Chr.)"],
     "terms": [],
     "gsw": {"topic": "Troscht für Verbannti und di Groosse Jesajarolle",
             "text": "Ab [[ISA.40.1]] änderet sich d Lag: D Schuld vo Jerusalem gilt als abtreit, d Verbannte "
                     "söled us Babel heichoo ([[ISA.48.20]]), und de Perserkönig Kyros, wo Babylon 539 v. Chr. "
                     "iignoo hät, wird mit Name gnännt ([[ISA.44.28]]; [[ISA.45.1]]). Sit em spoote 18. "
                     "Jaarhundert schriibed vili Forscher [[ISA.40.1-ISA.55.13]] eme unbekannte Prophet im Exil zue "
                     "(«Deuterojesaja»), sit em Bernhard Duhm (1892) [[ISA.56.1-ISA.66.24]] eme spöötere z "
                     "Jerusalem («Tritojesaja»). Traditionelli Usleger gsend s ganz Buech als Wärch vom Jesaja, wo "
                     "de Kyros vorusgseit heg; scho de Jesus Sirach schriibt em Jesaja de Troscht für Zion zue "
                     "([[SIR.48.24]]), und s Nöi Teschtamänt ([[MAT.3.3]]; [[JHN.12.38-JHN.12.41]]) füert die "
                     "Kapitel under em Name vom Jesaja aa. Di "
                     "Groosse Jesajarolle us Qumran (um 125 v. Chr.) enthaltet alli 66 Kapitel als eis Buech; trotz "
                     "vilne chliine Abwiichige stimmt si wiitgehend mit de öppe tuusig Jaar jüngere "
                     "mittelalterliche Handschrifte überii.",
             "uncertain": "Öb d Kapitel vo eim, zwei oder drüü Verfasser stammed, isch zwüsche traditioneller und "
                          "historisch-kritischer Uslegig umstritte. Vili Forscher gsend hüt statt drüü trännte "
                          "Büecher eis Buech, wo über Generatione wiitergschribe worde isch; d Gränze bi "
                          "[[ISA.56.1]] und de Aateil vo spöötere Zuesätz sind au under ine umstritte. D Rolle zeigt "
                          "d Gstalt vom Buech im 2. Jaarhundert v. Chr., nöd sini Entstehig.",
             "terms": []}},
    # ---------------------------------------------------------------- Jeremia
    {"id": "BG-JER-BOOK-0001", "book": "JER", "context": IP, "confidence": "probable",
     "topic": "Jeremia: vier Jahrzehnte bis zum Untergang Judas",
     "text": "Nach der Überschrift wirkte Jeremia, ein Priestersohn aus Anatot bei Jerusalem, vom 13. Jahr König "
             "Joschijas (627/626 v. Chr.) bis zur Eroberung Jerusalems 587/586 v. Chr. ([[JER.1.1-JER.1.3]]). In "
             "diese Zeit fallen der Zusammenbruch Assyriens, Babylons Sieg über Ägypten bei Karkemisch 605 v. Chr. "
             "([[JER.46.2]]), die erste Verschleppung 597 v. Chr. und die Zerstörung der Stadt. Briefe auf "
             "Tonscherben aus Lachisch stammen aus den letzten Monaten vor dem Fall; in einem heisst es, man achte "
             "auf die Feuerzeichen von Lachisch, denn Aseka sehe man nicht – nach [[JER.34.7]] waren Lachisch und "
             "Aseka die letzten festen Städte. Das Buch erzählt selbst, wie Jeremia seinem Schreiber Baruch "
             "diktierte und die Rolle nach ihrer Verbrennung erweitert neu schreiben liess ([[JER.36.4]]; "
             "[[JER.36.32]]). Zuletzt wurde Jeremia nach Ägypten mitgenommen ([[JER.43.6-JER.43.7]]).",
     "uncertain": "Ob Jeremias Wirken wirklich 627/626 v. Chr. begann, ist umstritten; einige Forscher setzen den "
                  "Beginn später an, weil kaum Worte sicher in die Zeit Joschijas datiert sind. Wie viel des Buches "
                  "auf Jeremia und Baruch zurückgeht und wie viel auf spätere Bearbeiter, deren Prosareden der "
                  "Sprache des Deuteronomiums nahestehen, ist offen. Ob der Lachisch-Brief bedeutet, dass Aseka "
                  "schon gefallen war, wird verschieden gedeutet.",
     "evidence_refs": ["JER.1.1-JER.1.3", "JER.34.7", "JER.36.4", "JER.36.32", "JER.46.2"],
     "sources": ["Lachisch-Briefe (um 588 v. Chr.)", "Babylonische Chronik (zu 605 und 597 v. Chr.)"],
     "terms": [],
     "gsw": {"topic": "De Jeremia: vier Jaarzäänt bis zum Undergang vo Juda",
             "text": "Nach de Überschrift hät de Jeremia, en Priestersohn us Anatot bi Jerusalem, vom 13. Jaar vom "
                     "König Joschija (627/626 v. Chr.) bis zur Eroberig vo Jerusalem 587/586 v. Chr. gwürkt "
                     "([[JER.1.1-JER.1.3]]). I die Ziit fallet de Zämebruch vo Assyrie, de Sieg vo Babylon über "
                     "Ägypte bi Karkemisch 605 v. Chr. ([[JER.46.2]]), di erscht Verschleppig 597 v. Chr. und d "
                     "Zerstörig vo de Stadt. Brief uf Tonscherbe us Lachisch stammed us de letschte Mönet vor em "
                     "Fall; i eim heisst s, me passi uf d Füürzeiche vo Lachisch uf, will me Aseka nöd gseei – nach "
                     "[[JER.34.7]] sind Lachisch und Aseka di letschte feschte Stedt gsii. S Buech verzellt sälber, "
                     "wie de Jeremia sim Schriiber Baruch diktiert und d Rolle nach irer Verbrännig erwiiteret nöi "
                     "hät lah schriibe ([[JER.36.4]]; [[JER.36.32]]). Am Schluss isch de Jeremia uf Ägypte "
                     "mitgnoo worde ([[JER.43.6-JER.43.7]]).",
             "uncertain": "Öb de Jeremia würkli 627/626 v. Chr. aagfange hät, isch umstritte; es paar Forscher "
                          "setzed de Aafang spööter aa, will chuum Wort sicher i d Ziit vom Joschija datiert sind. "
                          "Wie vil vom Buech uf de Jeremia und de Baruch zruggaat und wie vil uf spööteri "
                          "Bearbeiter, wo iri Prosareden nööch bi de Sprach vom Deuteronomium sind, isch offe. Öb "
                          "de Lachisch-Brief heisst, dass Aseka scho gfalle gsii isch, wird verschide düütet.",
             "terms": []}},
    {"id": "BG-JER-BOOK-0002", "book": "JER", "context": "CTX-HIST-BIBLE-FORMATION", "confidence": "probable",
     "topic": "Zwei Fassungen: der kürzere griechische Jeremia",
     "text": "Die griechische Übersetzung (Septuaginta) des Jeremiabuches ist etwa ein Siebtel kürzer als der "
             "hebräische Text der mittelalterlichen Handschriften, auf dem die meisten Bibelübersetzungen beruhen. "
             "Es fehlt zum Beispiel [[JER.33.14-JER.33.26]], und die Sprüche gegen die Völker, im Hebräischen "
             "[[JER.46.1-JER.51.64]], stehen dort nach [[JER.25.13]] und in anderer Reihenfolge. Das ist nicht "
             "bloss Freiheit der Übersetzer: Unter den hebräischen Jeremia-Fragmenten aus Qumran entsprechen einige "
             "der kürzeren Form, andere der längeren. Beide Fassungen waren also auf Hebräisch im Umlauf. Viele "
             "Forscher halten die kürzere für eine ältere Ausgabe des Buches und die längere für eine spätere "
             "Erweiterung.",
     "uncertain": "Ob die kürzere Fassung älter ist oder ob die griechische Übersetzung bzw. ihre hebräische "
                  "Vorlage gekürzt hat, ist umstritten; möglich ist auch, dass beide Fassungen sich getrennt "
                  "weiterentwickelten. Wie gross der Unterschied genau ist, hängt von der Zählweise ab. Die "
                  "Qumran-Fragmente sind klein und decken nur wenige Abschnitte ab.",
     "evidence_refs": ["JER.25.13", "JER.33.14-JER.33.26", "JER.46.1-JER.51.64"],
     "sources": ["Jeremia-Fragmente aus Qumran (u. a. 4QJerᵇ, 4QJerᵈ)"],
     "terms": [],
     "gsw": {"topic": "Zwei Fassige: de chürzer griechisch Jeremia",
             "text": "D griechisch Übersetzig (Septuaginta) vom Jeremiabuech isch öppe en Sibtel chürzer als de "
                     "hebräisch Täxt vo de mittelalterliche Handschrifte, wo di meischte Bibelübersetzige druf "
                     "baued. Es fehlt zum Biispil [[JER.33.14-JER.33.26]], und d Sprüch gäge d Völker, im "
                     "Hebräische [[JER.46.1-JER.51.64]], stönd dört nach [[JER.25.13]] und in ere andere "
                     "Reiefolg. Das isch nöd nur Freiheit vo de Übersetzer: Under de hebräische "
                     "Jeremia-Fragmänt us Qumran entspräched es paar de chürzere Form, anderi de längere. Beid "
                     "Fassige sind also uf Hebräisch im Umlauf gsii. Vili Forscher halted di chürzer für en elteri "
                     "Usgaab vom Buech und di länger für e spööteri Erwiiterig.",
             "uncertain": "Öb di chürzer Fassig elter isch oder öb d griechisch Übersetzig oder iri hebräisch "
                          "Vorlag kürzt hät, isch umstritte; mögli isch au, dass sich beid Fassige trännt "
                          "wiiterentwicklet händ. Wie groos de Unterschiid gnau isch, hangt vo de Zellwiis ab. D "
                          "Qumran-Fragmänt sind chlii und decked nur weni Abschnitt ab.",
             "terms": []}},
    # ---------------------------------------------------------------- Klagelieder
    {"id": "BG-LAM-BOOK-0001", "book": "LAM", "context": IP, "confidence": "probable",
     "topic": "Klagelieder: Trauer nach der Zerstörung Jerusalems",
     "text": "Die fünf Lieder beklagen die Eroberung Jerusalems durch die Babylonier 587/586 v. Chr.: die verlassene "
             "Stadt, den verworfenen Tempel, Hunger während der Belagerung und die Verschleppung ([[LAM.1.1-LAM.1.5]]; "
             "[[LAM.2.7]]; [[LAM.4.10]]). Der hebräische Name des Buches ist sein erstes Wort, «Echa», «Ach, wie!». "
             "Die Lieder [[LAM.1.1-LAM.4.22]] sind Alphabet-Gedichte: Die Strophen beginnen der Reihe nach mit den "
             "22 Buchstaben des hebräischen Alphabets, in [[LAM.3.1-LAM.3.66]] je drei Verse. Das letzte Lied "
             "([[LAM.5.1-LAM.5.22]]) hat ebenfalls 22 Verse, folgt aber nicht dem Alphabet. Das Buch nennt keinen "
             "Verfasser. Die griechische Übersetzung und die jüdische Überlieferung schreiben es Jeremia zu (vgl. "
             "[[2CH.35.25]]). In der hebräischen Bibel steht es bei den Schriften und wird am Gedenktag der "
             "Tempelzerstörung (9. Av) gelesen.",
     "uncertain": "Viele Forscher nehmen mehrere Dichter an, die in Juda bald nach 586 v. Chr. schrieben; ob einzelne "
                  "Lieder erst später entstanden, ist offen. Die Zuschreibung an Jeremia ist Überlieferung, das Buch "
                  "selbst nennt keinen Namen. Ob die Lieder für Klagefeiern gedichtet wurden, ist eine Vermutung.",
     "evidence_refs": ["LAM.1.1", "LAM.2.7", "LAM.3.1-LAM.3.66", "LAM.5.1-LAM.5.22"],
     "sources": [],
     "terms": [T("heb", "אֵיכָה", "«Ach, wie!» (hebräischer Name des Buches)", "echa")],
     "gsw": {"topic": "Chlaaglieder: Truur nach de Zerstörig vo Jerusalem",
             "text": "Di füüf Lieder beklaged d Eroberig vo Jerusalem dur d Babylonier 587/586 v. Chr.: di "
                     "verlasse Stadt, de verworfe Tempel, de Hunger wäred de Belagerig und d Verschleppig "
                     "([[LAM.1.1-LAM.1.5]]; [[LAM.2.7]]; [[LAM.4.10]]). De hebräisch Name vom Buech isch sis erscht "
                     "Wort, «Echa», «Ach, wie!». D Lieder [[LAM.1.1-LAM.4.22]] sind Alphabet-Gedicht: D Strophe "
                     "fanged dr Reie nach mit de 22 Buechstabe vom hebräische Alphabet aa, i [[LAM.3.1-LAM.3.66]] "
                     "je drüü Värs. S letscht Lied ([[LAM.5.1-LAM.5.22]]) hät au 22 Värs, folgt aber nöd em "
                     "Alphabet. S Buech nännt kein Verfasser. D griechisch Übersetzig und di jüdisch Überlieferig "
                     "schriibed s em Jeremia zue (vgl. [[2CH.35.25]]). I de hebräische Bible staat s bi de "
                     "Schrifte und wird am Gedänktag vo de Tempelzerstörig (9. Av) gläse.",
             "uncertain": "Vili Forscher nämed meereri Dichter aa, wo z Juda bald nach 586 v. Chr. gschribe händ; "
                          "öb einzelni Lieder erscht spööter entstande sind, isch offe. Dass s Buech vom Jeremia "
                          "isch, isch Überlieferig, s Buech sälber nännt kein Name. Öb d Lieder für Chlaagfiire "
                          "dichtet worde sind, isch e Vermuetig.",
             "terms": ["«Ach, wie!» (hebräisch Name vom Buech)"]}},
    # ---------------------------------------------------------------- Ezechiel
    {"id": "BG-EZK-BOOK-0001", "book": "EZK", "context": IP, "confidence": "probable",
     "topic": "Ezechiel: ein Priester unter den Verschleppten",
     "text": "Ezechiel, Sohn des Busi, war Priester und wurde 597 v. Chr. mit König Jojachin nach Babylonien "
             "verschleppt ([[EZK.1.1-EZK.1.3]]; [[2KI.24.14-2KI.24.16]]). Er lebte bei den Verbannten am Kanal "
             "Kebar in Tel-Abib ([[EZK.3.15]]). Viele Worte sind nach Jahren der Verschleppung Jojachins datiert, "
             "von 593 v. Chr. ([[EZK.1.2]]) bis 571 v. Chr. ([[EZK.29.17]]). Babylonische Tontafeln (um 592 v. "
             "Chr.) nennen Ölrationen für «Jojachin, den König von Juda». Das Buch ist klar gegliedert: "
             "Gerichtsworte gegen Jerusalem bis zur Nachricht vom Fall der Stadt ([[EZK.33.21]]), Sprüche gegen die "
             "Völker, dann Hoffnung auf Erneuerung, mit der Vision der Totengebeine ([[EZK.37.1-EZK.37.14]]) und dem "
             "Entwurf eines neuen Tempels ([[EZK.40.1-EZK.48.35]]). Gott redet Ezechiel stets als «ben adam» an, "
             "«Menschensohn».",
     "uncertain": "Wie viel des Buches auf Ezechiel selbst zurückgeht und wie viel auf eine spätere Schule, ist "
                  "umstritten; viele Forscher rechnen mit Fortschreibungen, andere lesen das Buch als weitgehend "
                  "einheitlich. Was das «dreissigste Jahr» in [[EZK.1.1]] meint (vielleicht Ezechiels Alter), ist "
                  "unklar. Eine frühe griechische Handschrift (Papyrus 967) hat in [[EZK.36.1-EZK.39.29]] einen "
                  "kürzeren Text und eine andere Kapitelfolge.",
     "evidence_refs": ["EZK.1.1-EZK.1.3", "EZK.3.15", "EZK.29.17", "EZK.33.21", "2KI.24.14-2KI.24.16"],
     "sources": ["Jojachin-Täfelchen aus Babylon (um 592 v. Chr.)"],
     "terms": [T("heb", "בֶּן־אָדָם", "Menschensohn, Mensch", "ben adam")],
     "gsw": {"topic": "De Ezechiel: en Priester under de Verschleppte",
             "text": "De Ezechiel, de Sohn vom Busi, isch Priester gsii und isch 597 v. Chr. mit em König Jojachin "
                     "uf Babylonie verschleppt worde ([[EZK.1.1-EZK.1.3]]; [[2KI.24.14-2KI.24.16]]). Er hät bi de "
                     "Verbannte am Kanal Kebar z Tel-Abib gläbt ([[EZK.3.15]]). Vili Wort sind nach Jaar vo de "
                     "Verschleppig vom Jojachin datiert, vo 593 v. Chr. ([[EZK.1.2]]) bis 571 v. Chr. "
                     "([[EZK.29.17]]). Babylonischi Tontafele (um 592 v. Chr.) nänned Ölratione für «Jojachin, de "
                     "König vo Juda». S Buech isch klar gliederet: Grichtswort gäge Jerusalem bis zur Nachricht "
                     "vom Fall vo de Stadt ([[EZK.33.21]]), Sprüch gäge d Völker, dänn Hoffnig uf Ernöierig, mit de "
                     "Vision vo de Totechnoche ([[EZK.37.1-EZK.37.14]]) und em Entwurf vo me nöie Tempel "
                     "([[EZK.40.1-EZK.48.35]]). Gott redt de Ezechiel immer als «ben adam» aa, «Menschesohn».",
             "uncertain": "Wie vil vom Buech uf de Ezechiel sälber zruggaat und wie vil uf e spööteri Schuel, isch "
                          "umstritte; vili Forscher rächned mit Fortschriibige, anderi läsed s Buech als "
                          "wiitgehend einheitlich. Was s «driissigscht Jaar» i [[EZK.1.1]] meint (vilicht s Alter "
                          "vom Ezechiel), isch unklar. E früeni griechischi Handschrift (Papyrus 967) hät i "
                          "[[EZK.36.1-EZK.39.29]] en chürzere Täxt und e anderi Kapitelfolg.",
             "terms": ["Menschesohn, Mänsch"]}},
    # ---------------------------------------------------------------- Daniel
    {"id": "BG-DAN-BOOK-0001", "book": "DAN", "context": IP, "confidence": "probable",
     "topic": "Daniel: Geschichten am Königshof und Visionen der Weltreiche",
     "text": "Das Buch spielt am babylonischen und persischen Königshof: Daniel kommt als junger Verschleppter nach "
             "Babel ([[DAN.1.1-DAN.1.6]]) und bleibt bis in die Zeit des Kyros ([[DAN.1.21]]; [[DAN.10.1]]). "
             "[[DAN.1.1-DAN.6.28]] erzählt in der dritten Person, wie Juden am fremden Hof ihrem Gott treu bleiben; "
             "in [[DAN.7.1-DAN.12.13]] berichtet Daniel selbst Visionen von vier Weltreichen und vom kommenden Reich "
             "Gottes ([[DAN.7.13-DAN.7.14]]). Belsazar ([[DAN.5.1]]) ist aus babylonischen Texten bekannt: als Sohn "
             "des Königs Nabonid, dem der Vater während eines langen Aufenthalts in Arabien die Herrschaft in "
             "Babylon überliess. Ein «Darius der Meder» ([[DAN.5.31]]) ist ausserhalb der Bibel nicht belegt. In "
             "der hebräischen Bibel steht Daniel bei den Schriften, in christlichen Bibeln bei den Propheten.",
     "uncertain": "Ob Daniel eine geschichtliche Person ist, deren Erlebnisse das Buch berichtet, oder eine "
                  "Erzählfigur, ist umstritten. Traditionelle Ausleger deuten «Darius den Meder» als anderen Namen "
                  "eines bekannten Herrschers (etwa Kyros oder dessen Statthalter Gubaru); kritische Forscher sehen "
                  "darin ein späteres Geschichtsbild mit einem Mederreich vor den Persern. Auch das «dritte Jahr "
                  "Jojakims» ([[DAN.1.1]]) lässt sich mit [[JER.25.1]] nur über unterschiedliche Zählweisen "
                  "vereinbaren.",
     "evidence_refs": ["DAN.1.1", "DAN.1.21", "DAN.5.1", "DAN.5.31", "DAN.7.13-DAN.7.14"],
     "sources": ["Nabonid-Chronik", "Nabonid-Zylinder aus Ur"],
     "terms": [],
     "gsw": {"topic": "De Daniel: Gschichte am Königshof und Visione vo de Wältriich",
             "text": "S Buech spilt am babylonische und persische Königshof: De Daniel chunnt als junge "
                     "Verschleppte uf Babel ([[DAN.1.1-DAN.1.6]]) und bliibt bis i d Ziit vom Kyros ([[DAN.1.21]]; "
                     "[[DAN.10.1]]). [[DAN.1.1-DAN.6.28]] verzellt i de dritte Person, wie Jude am frömde Hof irem "
                     "Gott tröi bliibed; i [[DAN.7.1-DAN.12.13]] bricht de Daniel sälber vo Visione vo vier "
                     "Wältriich und vom choomende Riich vo Gott ([[DAN.7.13-DAN.7.14]]). De Belsazar ([[DAN.5.1]]) "
                     "isch us babylonische Täxt bekannt: als Sohn vom König Nabonid, wo de Vater wäred eme lange "
                     "Ufenthalt z Arabie d Herrschaft z Babylon überlaa hät. En «Darius de Meder» ([[DAN.5.31]]) "
                     "isch usserhalb vo de Bible nöd belegt. I de hebräische Bible staat de Daniel bi de Schrifte, "
                     "i christliche Bible bi de Prophete.",
             "uncertain": "Öb de Daniel e gschichtlichi Person isch, wo s Buech vo irne Erläbnis bricht, oder e "
                          "Verzellfigur, isch umstritte. Traditionelli Usleger düüted de «Darius de Meder» als "
                          "andere Name vo me bekannte Herrscher (öppe de Kyros oder sin Statthalter Gubaru); "
                          "kritischi Forscher gsend drin es spöters Gschichtsbild mit eme Mederriich vor de Perser. "
                          "Au s «dritt Jaar vom Jojakim» ([[DAN.1.1]]) laat sich mit [[JER.25.1]] nur über "
                          "verschideni Zellwiise in Iiklang bringe.",
             "terms": []}},
    {"id": "BG-DAN-BOOK-0002", "book": "DAN", "context": "CTX-HIST-SECOND-TEMPLE", "confidence": "probable",
     "topic": "Zwei Sprachen und die Frage der Datierung",
     "text": "Von [[DAN.2.4]] bis [[DAN.7.28]] ist das Buch nicht hebräisch, sondern aramäisch geschrieben, in der "
             "Verkehrssprache des Alten Orients; der Sprachwechsel deckt sich nicht mit der Grenze zwischen "
             "Erzählungen und Visionen. Die griechische Bibel enthält zusätzliche Stücke (Gebet Asarjas und Lied "
             "der drei Männer, Susanna, Bel und der Drache). Die Überlieferung sieht Daniel im 6. Jahrhundert v. "
             "Chr. als Verfasser, der künftige Reiche vorausgesagt hat. Die historisch-kritische Forschung datiert "
             "die Endgestalt in die Verfolgung unter dem Seleukiden Antiochus IV. (167–164 v. Chr.): "
             "[[DAN.11.21-DAN.11.39]] beschreibt diese Zeit bis zur Entweihung des Tempels ([[DAN.11.31]]; vgl. "
             "[[1MA.1.54]]) sehr genau, das Ende des Königs in [[DAN.11.40-DAN.11.45]] entspricht aber nicht seinem "
             "Tod 164 v. Chr. in Persien. In Qumran fanden sich Reste von acht Daniel-Handschriften und ein «Gebet "
             "des Nabonid», das an [[DAN.4.1-DAN.4.37]] erinnert.",
     "uncertain": "Ob [[DAN.11.1-DAN.11.45]] vorausgesagte oder rückblickend erzählte Geschichte ist, hängt an "
                  "Grundentscheidungen und bleibt zwischen traditioneller und historisch-kritischer Auslegung "
                  "umstritten; auch kritische Forscher halten die Erzählungen oft für älter als die Endgestalt. "
                  "Warum gerade [[DAN.2.4-DAN.7.28]] aramäisch ist, ist ungeklärt. Die Zahl der Qumran-Handschriften "
                  "hängt davon ab, wie man die Fragmente zuordnet.",
     "evidence_refs": ["DAN.2.4", "DAN.7.28", "DAN.11.31", "DAN.11.40-DAN.11.45", "1MA.1.54"],
     "sources": ["Daniel-Handschriften aus Qumran (Höhlen 1, 4 und 6)", "Gebet des Nabonid (4Q242, Qumran)"],
     "terms": [],
     "gsw": {"topic": "Zwei Sprache und d Frag vo de Datierig",
             "text": "Vo [[DAN.2.4]] bis [[DAN.7.28]] isch s Buech nöd hebräisch, sondern aramäisch gschribe, i de "
                     "Verchehrssprach vom Alte Orient; de Sprachwächsel deckt sich nöd mit de Gränze zwüsche "
                     "Verzellige und Visione. Di griechisch Bible enthaltet zuesätzlichi Stuck (Gebät vom Asarja "
                     "und Lied vo de drüü Manne, Susanna, Bel und de Drache). D Überlieferig gseet de Daniel im 6. "
                     "Jaarhundert v. Chr. als Verfasser, wo chünftigi Riich vorusgseit hät. D historisch-kritisch "
                     "Forschig datiert d Ändgstalt i d Verfolgig under em Seleukide Antiochus IV. (167–164 v. Chr.): "
                     "[[DAN.11.21-DAN.11.39]] beschriibt die Ziit bis zur Entweihig vom Tempel ([[DAN.11.31]]; vgl. "
                     "[[1MA.1.54]]) sehr gnau, s Änd vom König i [[DAN.11.40-DAN.11.45]] entspricht aber nöd sim "
                     "Tod 164 v. Chr. z Persie. Z Qumran hät me Räscht vo acht Daniel-Handschrifte gfunde und es "
                     "«Gebät vom Nabonid», wo a [[DAN.4.1-DAN.4.37]] erinneret.",
             "uncertain": "Öb [[DAN.11.1-DAN.11.45]] vorusgseiti oder im Ruggblick verzellti Gschicht isch, hangt "
                          "a Grundentscheidige und bliibt zwüsche traditioneller und historisch-kritischer "
                          "Uslegig umstritte; au kritischi Forscher halted d Verzellige oft für elter als d "
                          "Ändgstalt. Warum grad [[DAN.2.4-DAN.7.28]] aramäisch isch, isch nöd klar. D Zaal vo de "
                          "Qumran-Handschrifte hangt dervo ab, wie me d Fragmänt zueornet.",
             "terms": []}},
    # ---------------------------------------------------------------- Hosea
    {"id": "BG-HOS-BOOK-0001", "book": "HOS", "context": IP, "confidence": "probable",
     "topic": "Hosea: die letzten Jahrzehnte des Nordreichs",
     "text": "Hosea wirkte im Nordreich Israel und stammte wohl auch von dort, anders als Amos, der aus Juda kam. Die "
             "Überschrift nennt König Jerobeam II. von Israel und die judäischen Könige Usija bis Hiskija "
             "([[HOS.1.1]]); meist wird sein Wirken um 750–725 v. Chr. angesetzt. Auf die Blütezeit unter Jerobeam "
             "folgten Königsmorde in rascher Folge ([[2KI.15.8-2KI.15.30]]; vgl. [[HOS.8.4]]) und ein Schwanken "
             "zwischen Assyrien und Ägypten ([[HOS.7.11]]); die Annalen des Assyrerkönigs Tiglat-Pileser III. nennen "
             "Tribut Menahems und die Einsetzung Hoscheas. Hosea deutet seine Ehe mit Gomer als Zeichen für Israels "
             "Untreue gegenüber Gott, der dennoch an seinem Volk festhält ([[HOS.1.2-HOS.1.9]]; "
             "[[HOS.3.1-HOS.3.5]]; [[HOS.11.1-HOS.11.9]]). Nach dem Fall Samarias 722/720 v. Chr. wurde das Buch "
             "wohl in Juda überliefert und weitergeschrieben.",
     "uncertain": "Ob Hoseas Ehe ein wirkliches Geschehen, eine Zeichenhandlung oder ein Gleichnis ist und ob "
                  "[[HOS.1.2-HOS.1.9]] und [[HOS.3.1-HOS.3.5]] dieselbe Frau meinen, ist umstritten. Wie weit die "
                  "Erwähnungen Judas (z. B. [[HOS.1.7]]) auf spätere judäische Bearbeitung zurückgehen, ist offen. "
                  "Der hebräische Text ist an vielen Stellen schwer verständlich.",
     "evidence_refs": ["HOS.1.1", "HOS.1.2-HOS.1.9", "HOS.7.11", "2KI.15.8-2KI.15.30"],
     "sources": ["Annalen Tiglat-Pilesers III. (zu Menahem und Hoschea)"],
     "terms": [],
     "gsw": {"topic": "De Hosea: di letschte Jaarzäänt vom Nordriich",
             "text": "De Hosea hät im Nordriich Israel gwürkt und isch wohl au vo dört cho, anders als de Amos, wo "
                     "us Juda cho isch. D Überschrift nännt de König Jerobeam II. vo Israel und di judäische König Usija bis "
                     "Hiskija ([[HOS.1.1]]); meischtens wird sis Würke um 750–725 v. Chr. aagsetzt. Uf d Blüeteziit "
                     "under em Jerobeam sind Königsmord churz hinderenand gfolgt ([[2KI.15.8-2KI.15.30]]; vgl. "
                     "[[HOS.8.4]]) und es Hin und Här zwüsche Assyrie und Ägypte ([[HOS.7.11]]); d Annale vom "
                     "Assyrerkönig Tiglat-Pileser III. nänned de Tribut vom Menahem und d Iisetzig vom Hoschea. De "
                     "Hosea düütet sini Ehe mit de Gomer als Zeiche für d Untröii vo Israel gägenüber Gott, wo "
                     "glich a sim Volk feschthaltet ([[HOS.1.2-HOS.1.9]]; [[HOS.3.1-HOS.3.5]]; "
                     "[[HOS.11.1-HOS.11.9]]). Nach em Fall vo Samaria 722/720 v. Chr. isch s Buech wohl z Juda "
                     "überliferet und wiitergschribe worde.",
             "uncertain": "Öb d Ehe vom Hosea es würklichs Gscheh, e Zeichehandlig oder es Glichnis isch und öb "
                          "[[HOS.1.2-HOS.1.9]] und [[HOS.3.1-HOS.3.5]] di gliich Frau meined, isch umstritte. Wie "
                          "wiit d Erwäänige vo Juda (z. B. [[HOS.1.7]]) uf e spööteri judäischi Bearbeitig "
                          "zruggönd, isch offe. De hebräisch Täxt isch a vilne Stelle schwär z verstaa.",
             "terms": []}},
    # ---------------------------------------------------------------- Joel
    {"id": "BG-JOL-BOOK-0001", "book": "JOL", "context": IP, "confidence": "possible",
     "topic": "Joel: Heuschrecken und der Tag JHWHs",
     "text": "Die Überschrift nennt weder König noch Jahr ([[JOL.1.1]]); wann Joel wirkte, ist offen. Sein Name "
             "bedeutet «JHWH ist Gott». Anlass ist eine Heuschreckenplage mit Dürre ([[JOL.1.4]]; "
             "[[JOL.1.17-JOL.1.20]]), die Joel als Vorzeichen des «Tages JHWHs», hebräisch «jom JHWH», deutet "
             "([[JOL.2.1-JOL.2.11]]); er ruft zu Fasten und Umkehr am Tempel auf ([[JOL.2.12-JOL.2.17]]). Bekannt "
             "ist die Verheissung, Gott werde seinen Geist auf alle ausgiessen ([[JOL.2.28-JOL.2.32]]); Petrus führt "
             "sie an Pfingsten an ([[ACT.2.16-ACT.2.21]]). Joel teilt viele Wendungen mit anderen Propheten: "
             "«Schwerter zu Pflugscharen» erscheint bei ihm umgekehrt ([[JOL.3.10]]; vgl. [[MIC.4.3]]), und Sätze stehen ebenso bei Amos und Obadja "
             "([[JOL.3.16]] mit [[AMO.1.2]]; [[JOL.2.32]] mit [[OBA.1.17]]).",
     "uncertain": "Traditionell wird Joel wegen seines Platzes im Buch der Zwölf früh datiert, oft ins 9. "
                  "Jahrhundert v. Chr. Viele Forscher setzen das Buch in persische Zeit (um 400 v. Chr.): Es nennt "
                  "keinen König, wohl aber Priester und Älteste, setzt einen Tempel und die Zerstreuung des Volkes "
                  "voraus ([[JOL.3.2]]) und erwähnt Griechen als Abnehmer verkaufter Judäer ([[JOL.3.6]]). Wer bei "
                  "den gemeinsamen Sätzen wen zitiert, ist offen. Ob die Heuschrecken wörtlich oder als Bild für ein "
                  "Heer gemeint sind, ist ebenfalls umstritten.",
     "evidence_refs": ["JOL.1.1", "JOL.1.4", "JOL.2.1-JOL.2.11", "JOL.2.28-JOL.2.32", "ACT.2.16-ACT.2.21"],
     "sources": [],
     "terms": [T("heb", "יוֹאֵל", "Joel: «JHWH ist Gott»", "joel"),
               T("heb", "יוֹם יְהוָה", "Tag JHWHs", "jom JHWH")],
     "gsw": {"topic": "De Joel: Heuschrecke und de Tag vo JHWH",
             "text": "D Überschrift nännt weder König no Jaar ([[JOL.1.1]]); wänn de Joel gwürkt hät, isch offe. Sin "
                     "Name heisst «JHWH isch Gott». Aalass isch e Heuschreckeplag mit Tröchni ([[JOL.1.4]]; "
                     "[[JOL.1.17-JOL.1.20]]), wo de Joel als Vorzeiche vom «Tag vo JHWH», hebräisch «jom JHWH», "
                     "düütet ([[JOL.2.1-JOL.2.11]]); er rüeft zu Faschte und Umkeer am Tempel uf "
                     "([[JOL.2.12-JOL.2.17]]). Bekannt isch d Verheissig, Gott wärdi sin Geischt uf alli usgüüsse "
                     "([[JOL.2.28-JOL.2.32]]); de Petrus füert si a de Pfingschte aa ([[ACT.2.16-ACT.2.21]]). De "
                     "Joel teilt vili Wändige mit andere Prophete: «Schwärter zu Pflueg-Schare» chunnt bi im umgcheert vor "
                     "([[JOL.3.10]]; vgl. [[MIC.4.3]]), und Sätz stönd gliich au bim Amos und bim Obadja ([[JOL.3.16]] mit "
                     "[[AMO.1.2]]; [[JOL.2.32]] mit [[OBA.1.17]]).",
             "uncertain": "Traditionell wird de Joel wäge sim Platz im Buech vo de Zwölf früe datiert, oft is 9. "
                          "Jaarhundert v. Chr. Vili Forscher setzed s Buech i persischi Ziit (um 400 v. Chr.): Es "
                          "nännt kein König, aber Priester und Ältischti, setzt en Tempel und d Zerstreuig vom Volk "
                          "voruus ([[JOL.3.2]]) und erwäänt Grieche als Chäufer vo verchaufte Judäer ([[JOL.3.6]]). "
                          "Wer bi de gmeinsame Sätz wer zitiert, isch offe. Öb d Heuschrecke wörtlich oder als Bild "
                          "für es Heer gmeint sind, isch au umstritte.",
             "terms": ["Joel: «JHWH isch Gott»", "Tag vo JHWH"]}},
    # ---------------------------------------------------------------- Amos
    {"id": "BG-AMO-BOOK-0001", "book": "AMO", "context": IP, "confidence": "probable",
     "topic": "Amos: ein Judäer predigt im reichen Nordreich",
     "text": "Amos stammte aus Tekoa in Juda und war Schafzüchter, hebräisch «noked» ([[AMO.1.1]]; vgl. "
             "[[AMO.7.14]]). Er trat im Nordreich Israel auf, unter anderem am Königsheiligtum von Bet-El, und "
             "wurde von dort ausgewiesen ([[AMO.7.10-AMO.7.17]]). Die Überschrift datiert ihn unter Jerobeam II. "
             "«zwei Jahre vor dem Erdbeben», meist um 760–750 v. Chr.; Archäologen bringen Zerstörungsspuren an "
             "mehreren Orten, etwa in Hazor, mit einem starken Beben um die Mitte des 8. Jahrhunderts in "
             "Verbindung, und noch [[ZEC.14.5]] erinnert daran. Es war eine Zeit von Wohlstand und wachsender "
             "Ungleichheit: Amos kritisiert «Elfenbeinhäuser» und Prunkbetten ([[AMO.3.15]]; [[AMO.6.4]]) – in "
             "Samaria wurden geschnitzte Elfenbeinplatten gefunden – sowie Rechtsbeugung an den Armen "
             "([[AMO.5.11-AMO.5.12]]). Amos gilt vielen als ältester Prophet, dessen Worte als Buch überliefert sind.",
     "uncertain": "Welche Teile später hinzukamen, ist umstritten: Viele Forscher halten etwa den Spruch gegen Juda "
                  "([[AMO.2.4-AMO.2.5]]), die Lobpreisstücke ([[AMO.4.13]]; [[AMO.5.8-AMO.5.9]]; "
                  "[[AMO.9.5-AMO.9.6]]) und den hoffnungsvollen Schluss ([[AMO.9.11-AMO.9.15]]) für Ergänzungen, "
                  "traditionelle Ausleger für Worte des Amos. Die Zuordnung der archäologischen Spuren zu dem in "
                  "[[AMO.1.1]] genannten Beben ist eine Vermutung; auch ob Hosea oder Amos zuerst auftrat, ist offen.",
     "evidence_refs": ["AMO.1.1", "AMO.7.10-AMO.7.17", "AMO.3.15", "AMO.6.4", "ZEC.14.5"],
     "sources": ["Elfenbeinschnitzereien aus Samaria (9./8. Jh. v. Chr.)"],
     "terms": [T("heb", "נֹקֵד", "Schafzüchter, Herdenhalter", "noked")],
     "gsw": {"topic": "De Amos: en Judäer prediget im riiche Nordriich",
             "text": "De Amos isch vo Tekoa z Juda cho und isch Schaafzüchter gsii, hebräisch «noked» ([[AMO.1.1]]; "
                     "vgl. [[AMO.7.14]]). Er isch im Nordriich Israel ufträte, under anderem am Königsheiligtum vo "
                     "Bet-El, und isch vo dört uusgwise worde ([[AMO.7.10-AMO.7.17]]). D Überschrift datiert en "
                     "under em Jerobeam II. «zwei Jaar vor em Ärdbebe», meischtens um 760–750 v. Chr.; Archäologe "
                     "bringed Zerstörigsspure a meerere Ort, öppe z Hazor, mit eme starche Bebe um d Mitti vom 8. "
                     "Jaarhundert in Verbindig, und no [[ZEC.14.5]] erinneret dra. Es isch e Ziit vo Wohlstand und "
                     "wachsender Ungliichheit gsii: De Amos kritisiert «Elfebeihüüser» und Prunkbett "
                     "([[AMO.3.15]]; [[AMO.6.4]]) – z Samaria hät me gschnitzti Elfebeiplatte gfunde – und d "
                     "Rächtsbüügig a de Arme ([[AMO.5.11-AMO.5.12]]). De Amos gilt für vili als ältischte Prophet, "
                     "wo sini Wort als Buech überliferet sind.",
             "uncertain": "Weli Teil spööter dezuechoo sind, isch umstritte: Vili Forscher halted öppe de Spruch "
                          "gäge Juda ([[AMO.2.4-AMO.2.5]]), d Lobpriisstuck ([[AMO.4.13]]; [[AMO.5.8-AMO.5.9]]; "
                          "[[AMO.9.5-AMO.9.6]]) und de hoffnigsvoll Schluss ([[AMO.9.11-AMO.9.15]]) für Ergänzige, "
                          "traditionelli Usleger für Wort vom Amos. D Zueornig vo de archäologische Spure zum Bebe, "
                          "wo [[AMO.1.1]] nännt, isch e Vermuetig; au öb de Hosea oder de Amos zerscht ufträte "
                          "isch, isch offe.",
             "terms": ["Schaafzüchter, Herdehalter"]}},
    # ---------------------------------------------------------------- Jona
    {"id": "BG-JON-BOOK-0001", "book": "JON", "context": IP, "confidence": "probable",
     "topic": "Jona: eine Erzählung über einen Propheten",
     "text": "Anders als die übrigen Prophetenbücher sammelt das Buch Jona kaum Prophetenworte – es enthält nur einen "
             "einzigen Spruch ([[JON.3.4]]) –, sondern erzählt von einem Propheten. Ein Jona, Sohn Amittais, wird "
             "unter Jerobeam II. im 8. Jahrhundert v. Chr. erwähnt ([[2KI.14.25]]). Er soll Ninive das Gericht "
             "ansagen, der grossen assyrischen Stadt, die um 700 v. Chr. Hauptstadt wurde und 612 v. Chr. "
             "unterging. Jona flieht und erlebt dann, wie Gott sich über die umkehrende Stadt erbarmt; dagegen "
             "protestiert er mit dem Bekenntnis aus [[EXO.34.6]] ([[JON.4.2]]). Das Buch endet mit einer offenen "
             "Frage Gottes ([[JON.4.11]]). Jesus spricht vom «Zeichen des Jona» ([[MAT.12.39-MAT.12.41]]). Der "
             "Name Jona bedeutet «Taube».",
     "uncertain": "Traditionell wird das Buch als Bericht über Ereignisse des 8. Jahrhunderts v. Chr. gelesen; dafür "
                  "wird oft auf Jesu Worte verwiesen. Viele Forscher lesen es als Lehrerzählung aus persischer oder "
                  "hellenistischer Zeit, wegen später Sprachformen, des Titels «König von Ninive» ([[JON.3.6]]), "
                  "der Grösse der Stadt ([[JON.3.3]]) und weil assyrische Quellen keine Umkehr Ninives kennen. Ob "
                  "der Psalm [[JON.2.2-JON.2.9]] von Anfang an zum Buch gehörte, ist umstritten.",
     "evidence_refs": ["JON.3.4", "JON.4.2", "JON.4.11", "2KI.14.25", "MAT.12.39-MAT.12.41"],
     "sources": [],
     "terms": [T("heb", "יוֹנָה", "Jona: «Taube»", "jona")],
     "gsw": {"topic": "De Jona: e Verzellig über en Prophet",
             "text": "Anders als di andere Prophetebüecher sammlet s Buech Jona chuum Prophetewort – es enthaltet nur "
                     "en einzige Spruch ([[JON.3.4]]) –, sondern verzellt vo me Prophet. En Jona, Sohn vom Amittai, "
                     "wird under em Jerobeam II. im 8. Jaarhundert v. Chr. erwäänt ([[2KI.14.25]]). Er sött Ninive "
                     "s Gricht aasäge, de groosse assyrische Stadt, wo um 700 v. Chr. Hauptstadt worde und 612 v. "
                     "Chr. undergange isch. De Jona flüchtet und erläbt dänn, wie Gott sich über d Stadt, wo "
                     "umcheert, erbarmet; dergäge protestiert er mit em Bekänntnis us [[EXO.34.6]] ([[JON.4.2]]). S "
                     "Buech hört mit ere offene Frag vo Gott uf ([[JON.4.11]]). De Jesus redt vom «Zeiche vom Jona» "
                     "([[MAT.12.39-MAT.12.41]]). De Name Jona heisst «Tuube».",
             "uncertain": "Traditionell wird s Buech als Bricht über Ereigniss vom 8. Jaarhundert v. Chr. gläse; "
                          "defür wird oft uf d Wort vom Jesus verwise. Vili Forscher läsed s als Lehrverzellig us "
                          "persischer oder hellenistischer Ziit, wäge spoote Sprachforme, em Titel «König vo "
                          "Ninive» ([[JON.3.6]]), de Gröössi vo de Stadt ([[JON.3.3]]) und will assyrischi Quälle "
                          "kei Umkeer vo Ninive känned. Öb de Psalm [[JON.2.2-JON.2.9]] vo Aafang aa zum Buech "
                          "ghört hät, isch umstritte.",
             "terms": ["Jona: «Tuube»"]}},
    # ---------------------------------------------------------------- Micha
    {"id": "BG-MIC-BOOK-0001", "book": "MIC", "context": IP, "confidence": "probable",
     "topic": "Micha: ein Prophet vom Land gegen Samaria und Jerusalem",
     "text": "Micha stammte aus Moreschet, einem Landstädtchen im Hügelland südwestlich von Jerusalem, und wirkte "
             "nach der Überschrift unter Jotam, Ahas und Hiskija, also etwa 735–700 v. Chr. ([[MIC.1.1]]). Seine "
             "Klage über die Orte seiner Heimat, darunter Lachisch ([[MIC.1.10-MIC.1.16]]), passt zum Feldzug "
             "Sanheribs 701 v. Chr., der diese Gegend verwüstete. Micha greift Landraub, bestechliche Richter, "
             "Priester und Propheten an ([[MIC.2.1-MIC.2.2]]; [[MIC.3.11]]) und kündigt sogar die Zerstörung "
             "Jerusalems an ([[MIC.3.12]]). Ein Jahrhundert später wird dieses Wort zitiert, um Jeremia zu "
             "verteidigen ([[JER.26.18]]) – ein seltener Fall, dass die Bibel einen Propheten mit Namen und Wortlaut "
             "anführt. Bekannt sind auch [[MIC.5.2]] (Betlehem, vgl. [[MAT.2.6]]) und [[MIC.6.8]]. Der Name ist eine "
             "Kurzform von «Wer ist wie JHWH?» (vgl. [[MIC.7.18]]).",
     "uncertain": "Viele Forscher schreiben vor allem [[MIC.1.1-MIC.3.12]] Micha selbst zu und sehen in "
                  "[[MIC.4.1-MIC.7.20]] auch Stücke aus Exil und Nachexil, etwa wegen der Erwähnung Babels "
                  "([[MIC.4.10]]); traditionelle Ausleger halten das ganze Buch für Michas Werk. Ob "
                  "[[MIC.4.1-MIC.4.3]] zuerst bei Micha oder bei Jesaja ([[ISA.2.2-ISA.2.4]]) stand oder beide "
                  "einen älteren Text aufnehmen, ist offen.",
     "evidence_refs": ["MIC.1.1", "MIC.1.10-MIC.1.16", "MIC.3.12", "JER.26.18", "MIC.6.8"],
     "sources": [TAYLOR, LACHISH_RELIEFS],
     "terms": [T("heb", "מִיכָה", "Micha: Kurzform von «Wer ist wie JHWH?»", "micha")],
     "gsw": {"topic": "De Micha: en Prophet vom Land gäge Samaria und Jerusalem",
             "text": "De Micha isch vo Moreschet cho, eme Landstädtli im Hügelland südweschtlich vo Jerusalem, und "
                     "hät nach de Überschrift under em Jotam, em Ahas und em Hiskija gwürkt, also öppe 735–700 v. "
                     "Chr. ([[MIC.1.1]]). Sini Chlaag über d Ort vo sinere Heimet, drunder Lachisch "
                     "([[MIC.1.10-MIC.1.16]]), passt zum Feldzug vom Sanherib 701 v. Chr., wo die Gäged verwüeschtet "
                     "hät. De Micha griift Landraub, bestächlichi Richter, Priester und Prophete aa "
                     "([[MIC.2.1-MIC.2.2]]; [[MIC.3.11]]) und kündet sogar d Zerstörig vo Jerusalem aa "
                     "([[MIC.3.12]]). Es Jaarhundert spööter wird das Wort zitiert, zum de Jeremia verteidige "
                     "([[JER.26.18]]) – en sältene Fall, wo d Bible en Prophet mit Name und Wortluut aafüert. "
                     "Bekannt sind au [[MIC.5.2]] (Betlehem, vgl. [[MAT.2.6]]) und [[MIC.6.8]]. De Name isch e "
                     "Churzform vo «Wer isch wie JHWH?» (vgl. [[MIC.7.18]]).",
             "uncertain": "Vili Forscher schriibed vor allem [[MIC.1.1-MIC.3.12]] em Micha sälber zue und gsend i "
                          "[[MIC.4.1-MIC.7.20]] au Stuck us em Exil und em Nachexil, öppe wäg de Erwäänig vo Babel "
                          "([[MIC.4.10]]); traditionelli Usleger halted s ganz Buech für s Wärch vom Micha. Öb "
                          "[[MIC.4.1-MIC.4.3]] zerscht bim Micha oder bim Jesaja ([[ISA.2.2-ISA.2.4]]) gstande isch "
                          "oder öb beid en eltere Täxt ufnänd, isch offe.",
             "terms": ["Micha: Churzform vo «Wer isch wie JHWH?»"]}},
    # ---------------------------------------------------------------- Nahum
    {"id": "BG-NAM-BOOK-0001", "book": "NAM", "context": IP, "confidence": "probable",
     "topic": "Nahum: der Fall Ninives",
     "text": "Das Buch hat ein einziges Thema: den Untergang Ninives, der Hauptstadt des Assyrerreichs, das Juda über "
             "ein Jahrhundert beherrscht und bedrückt hatte ([[NAM.1.1]]; [[NAM.3.1-NAM.3.7]]). Über Nahum aus "
             "Elkosch ist sonst nichts bekannt; wo Elkosch lag, ist unsicher. Der Name bedeutet «Trost». Einen "
             "Zeitrahmen geben zwei Ereignisse: [[NAM.3.8-NAM.3.10]] erinnert an die Eroberung der ägyptischen "
             "Stadt No-Amon (Theben) durch die Assyrer um 663 v. Chr.; Ninive selbst fiel 612 v. Chr. an Babylonier "
             "und Meder, wie die Babylonische Chronik berichtet. Am Anfang steht ein Hymnus über Gottes Eingreifen, "
             "der teilweise dem Alphabet folgt ([[NAM.1.2-NAM.1.8]]) und an [[EXO.34.6-EXO.34.7]] anknüpft "
             "([[NAM.1.3]]) – wie Jona, aber mit umgekehrtem Blick auf Ninive.",
     "uncertain": "Ob das Buch vor 612 v. Chr. als Ankündigung entstand oder danach als Rückblick, etwa für den "
                  "Gottesdienst, gestaltet wurde, ist umstritten. Ob der Hymnus [[NAM.1.2-NAM.1.8]] einmal ein "
                  "vollständiges Alphabet-Gedicht war, ist offen. Wie die Freude über den Untergang eines Feindes "
                  "heute zu lesen ist, wird theologisch verschieden beurteilt.",
     "evidence_refs": ["NAM.1.1", "NAM.1.3", "NAM.3.8-NAM.3.10"],
     "sources": ["Babylonische Chronik (zum Fall Ninives 612 v. Chr.)"],
     "terms": [T("heb", "נַחוּם", "Nahum: «Trost»", "nachum")],
     "gsw": {"topic": "De Nahum: de Fall vo Ninive",
             "text": "S Buech hät es einzigs Thema: de Undergang vo Ninive, de Hauptstadt vom Assyrerriich, wo Juda "
                     "über es Jaarhundert beherrscht und drückt hät ([[NAM.1.1]]; [[NAM.3.1-NAM.3.7]]). Über de Nahum "
                     "vo Elkosch weiss me susch nüt; wo Elkosch gläge isch, isch unsicher. De Name heisst «Troscht». "
                     "En Ziitraame gänd zwei Ereigniss: [[NAM.3.8-NAM.3.10]] erinneret a d Eroberig vo de "
                     "ägyptische Stadt No-Amon (Theben) dur d Assyrer um 663 v. Chr.; Ninive sälber isch 612 v. "
                     "Chr. a d Babylonier und d Meder gfalle, wie d Babylonisch Chronik bricht. Am Aafang staat en "
                     "Hymnus über s Iigriife vo Gott, wo zum Teil em Alphabet folgt ([[NAM.1.2-NAM.1.8]]) und a "
                     "[[EXO.34.6-EXO.34.7]] aaknüpft ([[NAM.1.3]]) – wie de Jona, aber mit umgcheertem Blick uf "
                     "Ninive.",
             "uncertain": "Öb s Buech vor 612 v. Chr. als Aakündigung entstande oder dänach als Ruggblick, öppe für "
                          "de Gottesdienscht, gstaltet worde isch, isch umstritte. Öb de Hymnus "
                          "[[NAM.1.2-NAM.1.8]] emal es vollständigs Alphabet-Gedicht gsii isch, isch offe. Wie me d "
                          "Freud über de Undergang vo me Feind hüt söll läse, wird theologisch verschide beurteilt.",
             "terms": ["Nahum: «Troscht»"]}},
    # ---------------------------------------------------------------- Habakuk
    {"id": "BG-HAB-BOOK-0001", "book": "HAB", "context": IP, "confidence": "probable",
     "topic": "Habakuk: Warum lässt Gott Unrecht zu?",
     "text": "Die Überschrift nennt keine Zeit ([[HAB.1.1]]). Nach [[HAB.1.6]] lässt Gott die «Chaldäer», die "
             "Neubabylonier, aufstehen; das weist meist in die Jahre um 605 v. Chr., als Babylon nach dem Sieg bei "
             "Karkemisch zur Vormacht wurde. Das Buch ist als Zwiegespräch gebaut: Habakuk klagt über Gewalt und "
             "Unrecht, Gott antwortet. Kernsatz der Antwort ist [[HAB.2.4]]: Der Gerechte wird durch seine "
             "«emuna» leben; das hebräische Wort meint Verlässlichkeit, Treue und Vertrauen. Paulus führt den Satz "
             "als Wort über den Glauben an ([[ROM.1.17]]; [[GAL.3.11]]). [[HAB.3.1-HAB.3.19]] ist ein Psalm mit "
             "musikalischen Angaben wie im Psalter. Ein Kommentar aus Qumran (1. Jh. v. Chr.) legt "
             "[[HAB.1.1-HAB.2.20]] Satz für Satz auf die eigene Gegenwart aus.",
     "uncertain": "Die Datierung ist umstritten: Vorgeschlagen werden Zeiten vor, während oder nach dem Aufstieg "
                  "Babylons; manche Forscher vermuten, ältere Klagen über Unrecht in Juda seien später auf die "
                  "Babylonier bezogen worden. Ob der Psalm [[HAB.3.1-HAB.3.19]] ursprünglich zum Buch gehörte, ist "
                  "offen; dass der Qumran-Kommentar ihn nicht auslegt, beweist nichts. Wie «emuna» in [[HAB.2.4]] "
                  "wiederzugeben ist (Glaube oder Treue, und wessen Treue), wird verschieden beurteilt.",
     "evidence_refs": ["HAB.1.6", "HAB.2.4", "ROM.1.17", "HAB.3.1-HAB.3.19"],
     "sources": ["Habakuk-Kommentar aus Qumran (1QpHab, 1. Jh. v. Chr.)"],
     "terms": [T("heb", "אֱמוּנָה", "Verlässlichkeit, Treue, Vertrauen", "emuna")],
     "gsw": {"topic": "De Habakuk: Warum laat Gott Unrächt zue?",
             "text": "D Überschrift nännt kei Ziit ([[HAB.1.1]]). Nach [[HAB.1.6]] laat Gott d «Chaldäer», d "
                     "Nöibabylonier, ufstaa; das wiist meischtens i d Jaar um 605 v. Chr., wo Babylon nach em Sieg "
                     "bi Karkemisch zur Vormacht worde isch. S Buech isch als Zwiegspröch baut: De Habakuk chlaget "
                     "über Gwalt und Unrächt, Gott antwortet. De Kärnsatz vo de Antwort isch [[HAB.2.4]]: De "
                     "Grächt wird dur sini «emuna» läbe; s hebräisch Wort meint Verlässlichkeit, Tröii und "
                     "Vertroue. De Paulus füert de Satz als Wort über de Glaube aa ([[ROM.1.17]]; [[GAL.3.11]]). "
                     "[[HAB.3.1-HAB.3.19]] isch en Psalm mit musikalische Aagabe wie im Psalter. En Kommentar us "
                     "Qumran (1. Jh. v. Chr.) leit [[HAB.1.1-HAB.2.20]] Satz für Satz uf di eige Gägewart uus.",
             "uncertain": "D Datierig isch umstritte: Vorgschlage wärded Ziite vor, wäred oder nach em Ufstiig vo "
                          "Babylon; es paar Forscher vermueted, elteri Chlaage über Unrächt z Juda seged spööter uf "
                          "d Babylonier bezoge worde. Öb de Psalm [[HAB.3.1-HAB.3.19]] ursprünglich zum Buech "
                          "ghört hät, isch offe; dass de Qumran-Kommentar en nöd uslegt, bewiist nüt. Wie me "
                          "«emuna» i [[HAB.2.4]] söll widergää (Glaube oder Tröii, und weme sini Tröii), wird "
                          "verschide beurteilt.",
             "terms": ["Verlässlichkeit, Tröii, Vertroue"]}},
    # ---------------------------------------------------------------- Zefanja
    {"id": "BG-ZEP-BOOK-0001", "book": "ZEP", "context": IP, "confidence": "probable",
     "topic": "Zefanja: der Tag des Zorns in der Zeit Joschijas",
     "text": "Die Überschrift führt Zefanjas Stammbaum über vier Generationen bis auf einen Hiskija zurück und "
             "datiert ihn unter König Joschija (640–609 v. Chr.; [[ZEP.1.1]]). Assyrien war damals im Niedergang; "
             "[[ZEP.2.13-ZEP.2.15]] kündigt den Untergang Ninives an, der 612 v. Chr. eintrat. Zefanja kritisiert "
             "Kulte für Baal, das Himmelsheer und Milkom in Jerusalem ([[ZEP.1.4-ZEP.1.6]]), die Joschija nach "
             "[[2KI.23.4-2KI.23.14]] bei seiner Reform um 622 v. Chr. beseitigen liess. Im Zentrum steht der «Tag "
             "JHWHs» als Tag des Gerichts ([[ZEP.1.14-ZEP.1.18]]); die lateinische Übersetzung von [[ZEP.1.15]], "
             "«dies irae», «Tag des Zorns», gab dem mittelalterlichen Hymnus vom Jüngsten Gericht den Namen. Das "
             "Buch schliesst mit Heilsworten für einen «demütigen und armen» Rest ([[ZEP.3.12-ZEP.3.20]]).",
     "uncertain": "Ob der genannte Hiskija der König ist, bleibt offen. Umstritten ist, ob Zefanja vor Joschijas "
                  "Reform wirkte, wofür die Kultkritik spricht, oder danach. Viele Forscher halten den Schluss "
                  "([[ZEP.3.14-ZEP.3.20]]) und Teile der Völkersprüche für spätere Ergänzungen aus Exil oder "
                  "Nachexil; traditionelle Ausleger schreiben das ganze Buch Zefanja zu.",
     "evidence_refs": ["ZEP.1.1", "ZEP.1.4-ZEP.1.6", "ZEP.1.14-ZEP.1.18", "ZEP.2.13-ZEP.2.15", "2KI.23.4-2KI.23.14"],
     "sources": ["Babylonische Chronik (zum Fall Ninives 612 v. Chr.)"],
     "terms": [T("lat", "dies irae", "Tag des Zorns", "dies irae")],
     "gsw": {"topic": "De Zefanja: de Tag vom Zorn i de Ziit vom Joschija",
             "text": "D Überschrift füert de Stammbaum vom Zefanja über vier Generatione bis uf en Hiskija zrugg und "
                     "datiert en under em König Joschija (640–609 v. Chr.; [[ZEP.1.1]]). Assyrie isch dänn im "
                     "Niedergang gsii; [[ZEP.2.13-ZEP.2.15]] kündet de Undergang vo Ninive aa, wo 612 v. Chr. "
                     "iiträte isch. De Zefanja kritisiert Kult für de Baal, s Himmelsheer und de Milkom z Jerusalem "
                     "([[ZEP.1.4-ZEP.1.6]]), wo de Joschija nach [[2KI.23.4-2KI.23.14]] bi sinere Reform um 622 v. "
                     "Chr. hät lah wegmache. I de Mitti staat de «Tag vo JHWH» als Tag vom Gricht "
                     "([[ZEP.1.14-ZEP.1.18]]); di latiinisch Übersetzig vo [[ZEP.1.15]], «dies irae», «Tag vom "
                     "Zorn», hät em mittelalterliche Hymnus vom Jüngschte Gricht de Name gää. S Buech hört mit "
                     "Heilswort für en «demüetige und arme» Räscht uf ([[ZEP.3.12-ZEP.3.20]]).",
             "uncertain": "Öb de gnännt Hiskija de König isch, bliibt offe. Umstritte isch, öb de Zefanja vor de "
                          "Reform vom Joschija gwürkt hät, wo d Kultkritik derfür spricht, oder dänach. Vili Forscher "
                          "halted de Schluss ([[ZEP.3.14-ZEP.3.20]]) und Teil vo de Völkersprüch für spööteri "
                          "Ergänzige us em Exil oder em Nachexil; traditionelli Usleger schriibed s ganz Buech em "
                          "Zefanja zue.",
             "terms": ["Tag vom Zorn"]}},
    # ---------------------------------------------------------------- Haggai
    {"id": "BG-HAG-BOOK-0001", "book": "HAG", "context": IP, "confidence": "probable",
     "topic": "Haggai: Aufruf zum Tempelbau 520 v. Chr.",
     "text": "Haggais Worte sind auf den Tag genau datiert, vom sechsten bis zum neunten Monat im zweiten Jahr des "
             "Perserkönigs Darius I., also 520 v. Chr. ([[HAG.1.1]]; [[HAG.2.10]]; [[HAG.2.20]]). Fast zwanzig "
             "Jahre nach der Erlaubnis zur Rückkehr lag der Tempel noch in Trümmern, und die Heimgekehrten litten "
             "unter Missernten ([[HAG.1.2-HAG.1.11]]). Haggai drängt den Statthalter Serubbabel aus dem Haus Davids "
             "und den Hohenpriester Josua zum Wiederaufbau. Darius hatte eben Aufstände im ganzen Reich "
             "niedergeschlagen, wovon seine Inschrift von Behistun berichtet; Haggai kündigt an, Gott werde Himmel "
             "und Erde erschüttern ([[HAG.2.6-HAG.2.7]]), und nennt Serubbabel Gottes «Siegelring» "
             "([[HAG.2.21-HAG.2.23]]). Nach [[EZR.5.1]] wirkte er zusammen mit Sacharja; der Tempel wurde 515 v. "
             "Chr. geweiht ([[EZR.6.15]]).",
     "uncertain": "Das Buch spricht von Haggai in der dritten Person; ob er es selbst verfasste oder Schüler es bald "
                  "danach zusammenstellten, ist offen. Was Haggai für Serubbabel erwartete, ein erneuertes "
                  "davidisches Königtum oder eine bescheidenere Rolle, und warum Serubbabel später nicht mehr "
                  "erwähnt wird, ist ungeklärt. Wie sich die frühere Grundsteinlegung nach [[EZR.3.8-EZR.3.10]] zu "
                  "Haggais Aufruf verhält, wird verschieden rekonstruiert.",
     "evidence_refs": ["HAG.1.1", "HAG.2.6-HAG.2.7", "HAG.2.21-HAG.2.23", "EZR.5.1", "EZR.6.15"],
     "sources": ["Behistun-Inschrift des Darius I. (um 520 v. Chr.)"],
     "terms": [],
     "gsw": {"topic": "De Haggai: Ufruef zum Tempelbau 520 v. Chr.",
             "text": "D Wort vom Haggai sind uf de Tag gnau datiert, vom sächste bis zum nüünte Monet im zweite Jaar "
                     "vom Perserkönig Darius I., also 520 v. Chr. ([[HAG.1.1]]; [[HAG.2.10]]; [[HAG.2.20]]). Fascht "
                     "zwänzg Jaar nach de Erlaubnis zur Ruggkeer isch de Tempel no immer i Trümmer gläge, und d "
                     "Heicheerte händ under Missernte glitte ([[HAG.1.2-HAG.1.11]]). De Haggai drängt de "
                     "Statthalter Serubbabel us em Huus vom David und de Hohepriester Josua zum Wideruufbau. De "
                     "Darius hät grad Ufständ im ganze Riich niedergschlage gha, wo sini Inschrift vo Behistun "
                     "devo bricht; de Haggai kündet aa, Gott wärdi Himmel und Ärde erschüttere "
                     "([[HAG.2.6-HAG.2.7]]), und nännt de Serubbabel de «Siegelring» vo Gott "
                     "([[HAG.2.21-HAG.2.23]]). Nach [[EZR.5.1]] hät er zäme mit em Sacharja gwürkt; de Tempel isch "
                     "515 v. Chr. iigweit worde ([[EZR.6.15]]).",
             "uncertain": "S Buech redt vom Haggai i de dritte Person; öb er s sälber gschribe hät oder öb Schüeler "
                          "s bald dänach zämegstellt händ, isch offe. Was de Haggai für de Serubbabel erwartet hät, "
                          "es ernöierts davidischs Königtum oder e bescheideneri Rolle, und warum de Serubbabel "
                          "spööter nüme erwäänt wird, isch nöd klar. Wie sich d früener Grundsteilegig nach "
                          "[[EZR.3.8-EZR.3.10]] zum Ufruef vom Haggai verhaltet, wird verschide rekonstruiert.",
             "terms": []}},
    # ---------------------------------------------------------------- Sacharja
    {"id": "BG-ZEC-BOOK-0001", "book": "ZEC", "context": IP, "confidence": "probable",
     "topic": "Sacharja: Nachtgesichte und ein zweiter Buchteil",
     "text": "Sacharja wirkte zur selben Zeit wie Haggai; seine Worte sind von 520 bis 518 v. Chr. datiert "
             "([[ZEC.1.1]]; [[ZEC.1.7]]; [[ZEC.7.1]]). Im Mittelpunkt von [[ZEC.1.7-ZEC.6.15]] stehen acht "
             "nächtliche Visionen, die ein Engel deutet: Jerusalem wird wieder bewohnt, Tempel und Führung, der "
             "Statthalter Serubbabel und der Hohepriester Josua, werden erneuert ([[ZEC.3.1-ZEC.3.10]]; "
             "[[ZEC.4.6-ZEC.4.10]]). [[ZEC.9.1-ZEC.14.21]] ist anders: keine Daten, kein Name Sacharjas, Sprüche "
             "über die Völker und das künftige Jerusalem, mit der Überschrift «Ausspruch», hebräisch «massa» "
             "([[ZEC.9.1]]; [[ZEC.12.1]]), wie in [[MAL.1.1]]. Aus diesem Teil führen die Evangelien den König auf "
             "dem Esel an ([[ZEC.9.9]]; [[MAT.21.5]]) und den Durchbohrten ([[ZEC.12.10]]; [[JHN.19.37]]).",
     "uncertain": "Die historisch-kritische Forschung schreibt [[ZEC.9.1-ZEC.14.21]] meist einem oder mehreren "
                  "späteren Verfassern zu («Deuterosacharja»), oft in spätpersischer oder frühhellenistischer Zeit; "
                  "dafür wird unter anderem die Erwähnung der Griechen ([[ZEC.9.13]]) angeführt. Traditionelle "
                  "Ausleger sehen das ganze Buch als Werk Sacharjas. Dass [[MAT.27.9-MAT.27.10]] ein Wort aus "
                  "[[ZEC.11.12-ZEC.11.13]] unter Jeremias Namen anführt, wird verschieden erklärt.",
     "evidence_refs": ["ZEC.1.1", "ZEC.1.7-ZEC.6.15", "ZEC.9.1", "ZEC.9.9", "ZEC.12.10"],
     "sources": [],
     "terms": [T("heb", "מַשָּׂא", "Ausspruch, Last", "massa")],
     "gsw": {"topic": "De Sacharja: Nachtgsicht und en zweite Buechteil",
             "text": "De Sacharja hät zur gliiche Ziit wie de Haggai gwürkt; sini Wort sind vo 520 bis 518 v. Chr. "
                     "datiert ([[ZEC.1.1]]; [[ZEC.1.7]]; [[ZEC.7.1]]). I de Mitti vo [[ZEC.1.7-ZEC.6.15]] stönd acht "
                     "nächtlichi Visione, wo en Ängel düütet: Jerusalem wird wider bewohnt, Tempel und Füerig, de "
                     "Statthalter Serubbabel und de Hohepriester Josua, wärded ernöieret ([[ZEC.3.1-ZEC.3.10]]; "
                     "[[ZEC.4.6-ZEC.4.10]]). [[ZEC.9.1-ZEC.14.21]] isch anders: kei Date, kein Name vom Sacharja, "
                     "Sprüch über d Völker und s chünftig Jerusalem, mit de Überschrift «Usspruch», hebräisch "
                     "«massa» ([[ZEC.9.1]]; [[ZEC.12.1]]), wie i [[MAL.1.1]]. Us däm Teil füered d Evangelie de "
                     "König uf em Esel aa ([[ZEC.9.9]]; [[MAT.21.5]]) und de Durchbohrt ([[ZEC.12.10]]; "
                     "[[JHN.19.37]]).",
             "uncertain": "D historisch-kritisch Forschig schriibt [[ZEC.9.1-ZEC.14.21]] meischtens eim oder meerere "
                          "spöötere Verfasser zue («Deuterosacharja»), oft i spootpersischer oder früehellenistischer "
                          "Ziit; derfür wird under anderem d Erwäänig vo de Grieche ([[ZEC.9.13]]) aagfüert. "
                          "Traditionelli Usleger gsend s ganz Buech als Wärch vom Sacharja. Dass "
                          "[[MAT.27.9-MAT.27.10]] es Wort us [[ZEC.11.12-ZEC.11.13]] under em Name vom Jeremia "
                          "aafüert, wird verschide erklärt.",
             "terms": ["Usspruch, Lascht"]}},
    # ---------------------------------------------------------------- Maleachi
    {"id": "BG-MAL-BOOK-0001", "book": "MAL", "context": IP, "confidence": "probable",
     "topic": "Maleachi: Streitgespräche in persischer Zeit",
     "text": "Maleachi heisst «mein Bote»; ob das ein Personenname ist, ist unsicher, denn dasselbe Wort steht in "
             "[[MAL.3.1]], und die griechische Übersetzung gibt [[MAL.1.1]] mit «durch seinen Boten» wieder. Das "
             "Buch setzt einen wieder aufgebauten Tempel mit Opferbetrieb voraus ([[MAL.1.6-MAL.1.14]]) und einen "
             "Statthalter, hebräisch «pecha» ([[MAL.1.8]]), wie er auch bei Haggai für Juda unter persischer "
             "Herrschaft genannt wird ([[HAG.1.1]]). Mischehen ([[MAL.2.11]]) und vernachlässigte Zehntabgaben "
             "([[MAL.3.8-MAL.3.10]]) erinnern an Nehemia ([[NEH.13.10-NEH.13.12]]; [[NEH.13.23-NEH.13.27]]); meist "
             "wird Maleachi deshalb ins 5. Jahrhundert v. Chr. datiert. Typisch sind Streitgespräche: Gott sagt "
             "etwas, das Volk fragt zurück «Worin …?», Gott antwortet ([[MAL.1.2]]). In den meisten westlichen christlichen "
             "Bibeln endet das Alte Testament mit der Ankündigung Elias ([[MAL.4.5-MAL.4.6]]), die das Neue Testament auf "
             "Johannes den Täufer bezieht ([[MAT.11.14]]).",
     "uncertain": "Ob Maleachi vor, während oder nach Nehemia (Mitte 5. Jahrhundert v. Chr.) auftrat, ist umstritten. "
                  "Die jüdische Überlieferung (Targum) setzt den Boten mit Esra gleich; das ist eine spätere Deutung. "
                  "Viele Forscher halten [[MAL.4.4-MAL.4.6]] für einen Nachtrag, der die ganze Prophetensammlung "
                  "abschliesst; in hebräischen Bibeln gehören diese Verse zu Kapitel 3.",
     "evidence_refs": ["MAL.1.1", "MAL.1.8", "MAL.3.1", "MAL.4.5-MAL.4.6", "MAT.11.14"],
     "sources": [],
     "terms": [T("heb", "מַלְאָכִי", "Maleachi: «mein Bote»", "mal'achi"),
               T("heb", "פֶּחָה", "Statthalter", "pecha")],
     "gsw": {"topic": "De Maleachi: Strittgspröch i persischer Ziit",
             "text": "Maleachi heisst «mi Bott»; öb das en Personename isch, isch unsicher, will s gliich Wort i "
                     "[[MAL.3.1]] staat, und di griechisch Übersetzig git [[MAL.1.1]] mit «dur sin Bott» wider. S "
                     "Buech setzt en wider ufbaute Tempel mit Opferbetriib voruus ([[MAL.1.6-MAL.1.14]]) und en "
                     "Statthalter, hebräisch «pecha» ([[MAL.1.8]]), wie au de Haggai eine für Juda under persischer "
                     "Herrschaft nännt ([[HAG.1.1]]). Mischehe ([[MAL.2.11]]) und vernachlässigti Zehnteabgabe "
                     "([[MAL.3.8-MAL.3.10]]) erinnered a de Nehemia ([[NEH.13.10-NEH.13.12]]; "
                     "[[NEH.13.23-NEH.13.27]]); meischtens wird de Maleachi drum is 5. Jaarhundert v. Chr. datiert. "
                     "Typisch sind Strittgspröch: Gott seit öppis, s Volk fröget zrugg «Wodrin …?», Gott antwortet "
                     "([[MAL.1.2]]). I de meischte weschtliche christliche Bible hört s Alt Teschtamänt mit de Aakündigung vom Elia uf "
                     "([[MAL.4.5-MAL.4.6]]), wo s Nöi Teschtamänt uf de Johannes de Täufer bezieht ([[MAT.11.14]]).",
             "uncertain": "Öb de Maleachi vor, wäred oder nach em Nehemia (Mitti 5. Jaarhundert v. Chr.) ufträte "
                          "isch, isch umstritte. Di jüdisch Überlieferig (Targum) setzt de Bott em Esra gliich; das "
                          "isch e spööteri Düütig. Vili Forscher halted [[MAL.4.4-MAL.4.6]] für en Nachtrag, wo di "
                          "ganz Prophetesammlig abschliesst; i hebräische Bible ghöred die Värs zum Kapitel 3.",
             "terms": ["Maleachi: «mi Bott»", "Statthalter"]}},
]
