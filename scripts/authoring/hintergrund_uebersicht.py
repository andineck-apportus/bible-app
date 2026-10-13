#!/usr/bin/env python3
"""Autorenwerkzeug: Hintergrund damals für die oberen Ebenen (Bibel, Testamente, Buchgruppen).

Aufruf: python3 scripts/authoring/hintergrund_uebersicht.py

Schreibt data/contexts/CTX-HIST-*.json, data/background/overview/BG-*.json (background_note mit `scope`) und
die Züridüütsch-Lokalisierungen data/localizations/gsw-u-sd-chzh/BG-*.json. Bibelstellen als Marken [[…]].
Idempotent; bestehende Dateien werden nur bei inhaltlicher Änderung neu geschrieben (dann mit revision_log).
KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import localizations  # noqa: E402

D = ROOT / "data"
DATE = "2026-10-13"
LANG = "gsw-u-sd-chzh"
AUTH = "KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-13; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft."

CONTEXTS = [
    {"id": "CTX-HIST-BIBLE-FORMATION", "period": {"from": -1000, "to": 400, "era": "BCE-CE", "approx": True},
     "region": "Levante, Mesopotamien, Ägypten, östlicher Mittelmeerraum",
     "language_context": ["he", "arc", "grc"],
     "audience": "Entstehung, Überlieferung und Sammlung der biblischen Schriften",
     "note_de": "Grober Rahmen von den ältesten vermuteten Textteilen bis zur Festlegung der Listen im 4. Jahrhundert n. Chr.; Einzeldatierungen sind umstritten."},
    {"id": "CTX-HIST-ISRAEL-IRON-PERSIAN", "period": {"from": -1000, "to": -330, "era": "BCE", "approx": True},
     "region": "Israel und Juda, Babylonien, Perserreich",
     "language_context": ["he", "arc"],
     "audience": "Israel und Juda von der Königszeit über das Exil bis in die Perserzeit",
     "note_de": "Zeit, in der nach verbreiteter Ansicht der grösste Teil der Schriften des Alten Testaments entstand und gesammelt wurde."},
    {"id": "CTX-HIST-SECOND-TEMPLE", "period": {"from": -515, "to": 70, "era": "BCE-CE", "approx": True},
     "region": "Judäa und jüdische Diaspora (u. a. Alexandria, Babylonien)",
     "language_context": ["he", "arc", "grc"],
     "audience": "Judentum in der Zeit des Zweiten Tempels",
     "note_de": "Vom Wiederaufbau des Tempels bis zu seiner Zerstörung durch die Römer."},
    {"id": "CTX-HIST-EARLY-CHRISTIANITY", "period": {"from": 30, "to": 130, "era": "CE", "approx": True},
     "region": "Judäa, Galiläa, Städte des östlichen Mittelmeers, Rom",
     "language_context": ["grc", "arc", "lat"],
     "audience": "Erste christliche Gemeinden im Römischen Reich",
     "note_de": "Von Jesus und den ersten Gemeinden bis zur Zeit der jüngsten Schriften des Neuen Testaments."},
]

T = lambda lang, word, de, translit=None: {"lang": lang, "word": word, **({"translit": translit} if translit else {}), "de": de}

# (id, scope, Schlüssel, Kontext, Konfidenz, Thema, Text, unsicher, Belege, Quellen, Fachwörter, Mundart: Thema, Text, unsicher, Fachwörter)
NOTES = [
 ("BG-BIBLE-0001", "bible", None, "CTX-HIST-BIBLE-FORMATION", "high",
  "Eine Bibliothek aus rund tausend Jahren",
  "Die Bibel ist keine einzelne Schrift, sondern eine Sammlung. Ihre Texte entstanden über rund tausend Jahre: Als besonders alt gelten einzelne Lieder wie das Deboralied ([[JDG.5.1-JDG.5.31]]), die jüngsten Schriften des Neuen Testaments stammen aus der Zeit um 100 n. Chr. Geschrieben wurde auf Hebräisch, in einigen Abschnitten auf Aramäisch (z. B. [[DAN.2.4-DAN.7.28]]; [[EZR.4.8-EZR.6.18]]), das Neue Testament in der griechischen Alltagssprache Koine. Vieles wurde zuerst mündlich weitergegeben, gesammelt und über Generationen bearbeitet.",
  "Wie alt einzelne Teile sind, ist umstritten. Traditionelle Auslegung datiert viele Schriften früher (z. B. die Tora zu Mose), die historisch-kritische Forschung meist später und rechnet mit längerer Bearbeitung.",
  ["JDG.5.1-JDG.5.31", "DAN.2.4-DAN.7.28", "EZR.4.8-EZR.6.18"], [],
  [T("grc", "κοινή", "gemeinsame (Sprache)")],
  "E Bibliothek us öppe tuusig Jaar",
  "D Bible isch kei einzelni Schrift, sondern e Sammlig. Iri Text sind über öppe tuusig Jaar entstande: Als bsunders alt gälted einzelni Lieder wie s Deboralied ([[JDG.5.1-JDG.5.31]]), di jüngschte Schrifte vom Nöie Teschtamänt stammed us de Ziit um 100 n. Chr. Gschribe worde isch uf Hebräisch, i es paar Abschnitt uf Aramäisch (z. B. [[DAN.2.4-DAN.7.28]]; [[EZR.4.8-EZR.6.18]]), s Nöi Teschtamänt i de griechische Alltagssprach Koine. Vil isch zerscht mündlich wiitergää, gsammlet und über Generatione bearbeitet worde.",
  "Wie alt einzelni Teil sind, isch umstritte. Di traditionell Uslegig datiert vili Schrifte früener (z. B. d Tora uf de Mose), d historisch-kritisch Forschig meischtens spööter und rächnet mit ere längere Bearbeitig.",
  ["gmeinsami (Sprach)"]),
 ("BG-BIBLE-0002", "bible", None, "CTX-HIST-BIBLE-FORMATION", "probable",
  "Wie aus Schriften ein Kanon wurde",
  "Welche Schriften zur Bibel gehören, wurde über Jahrhunderte geklärt; das griechische Wort Kanon bedeutet «Richtschnur». Die hebräische Bibel war in ihrem Umfang um das 1. bis 2. Jahrhundert n. Chr. weitgehend festgelegt. Die griechische Übersetzung, die Septuaginta, enthielt weitere Schriften, die katholische und orthodoxe Kirchen als «deuterokanonisch» zählen und evangelische meist als «Apokryphen» abgrenzen. Für das Neue Testament nennt der Osterfestbrief des Athanasius von Alexandria (367 n. Chr.) als erste erhaltene Liste genau die 27 heute üblichen Schriften. Diese App folgt vorerst dem evangelischen Kanon mit 66 Büchern.",
  "Wann und wie der hebräische Kanon abgeschlossen wurde, ist umstritten; die früher oft genannte «Synode von Jamnia» (um 90 n. Chr.) gilt heute nicht mehr als förmlicher Beschluss. Einzelne Schriften des Neuen Testaments (z. B. Hebräerbrief, Offenbarung) waren noch im 4. Jahrhundert nicht überall anerkannt.",
  [], ["Athanasius, 39. Osterfestbrief (367 n. Chr.)"],
  [T("grc", "κανών", "Richtschnur, Massstab"), T("lat", "septuaginta", "siebzig", "septuaginta")],
  "Wie us Schrifte en Kanon worde isch",
  "Weli Schrifte zur Bible ghöred, isch über Jaarhunderti klärt worde; s griechische Wort Kanon heisst «Richtschnuer». D hebräisch Bible isch im Umfang öppe im 1. bis 2. Jaarhundert n. Chr. wiitgehend feschtgleit gsii. D griechisch Übersetzig, d Septuaginta, hät wiiteri Schrifte enthalte, wo di katholisch und di orthodox Chile als «deuterokanonisch» zelled und di evangelische meischtens als «Apokryphe» abgränzed. Fürs Nöi Teschtamänt nännt de Oschterfeschtbrief vom Athanasius vo Alexandria (367 n. Chr.) als erschti erhalteni Lischte gnau di 27 Schrifte, wo hüt üblich sind. Die App folgt vorläufig em evangelische Kanon mit 66 Büecher.",
  "Wänn und wie de hebräisch Kanon abgschlosse worde isch, isch umstritte; di früener oft gnännt «Synode vo Jamnia» (um 90 n. Chr.) gilt hüt nüme als förmliche Bschluss. Einzelni Schrifte vom Nöie Teschtamänt (z. B. de Hebräerbrief, d Offebarig) sind no im 4. Jaarhundert nöd überall aagnoo gsii.",
  ["Richtschnuer, Massstab", "sibezg"]),
 ("BG-OT-0001", "testament", "OT", "CTX-HIST-ISRAEL-IRON-PERSIAN", "probable",
  "Ein kleines Volk zwischen Grossmächten",
  "Die Schriften des Alten Testaments entstanden in einem kleinen Land an der Landbrücke zwischen Ägypten und Mesopotamien. Prägend waren die Königreiche Israel im Norden und Juda im Süden, die Eroberung Samarias durch die Assyrer (722/720 v. Chr., [[2KI.17.6]]), die Zerstörung Jerusalems und des Tempels durch die Babylonier (587/586 v. Chr., [[2KI.25.8-2KI.25.10]]) mit der Verschleppung ins Exil und die Rückkehr unter persischer Herrschaft ab 539 v. Chr. ([[EZR.1.1-EZR.1.4]]); der neue Tempel wurde um 515 v. Chr. geweiht. Viele Forscher sehen Exil und Perserzeit als die Zeit, in der grosse Teile der Schriften gesammelt und geformt wurden.",
  "Die genannten Daten sind durch ausserbiblische Quellen gut gestützt. Wie viel der Überlieferung aus der frühen Königszeit oder früher stammt, ist umstritten; Archäologie und Texte werden dabei unterschiedlich gewichtet.",
  ["2KI.17.6", "2KI.25.8-2KI.25.10", "EZR.1.1-EZR.1.4"], ["Babylonische Chronik (zu 597 v. Chr.)", "Kyros-Zylinder (nach 539 v. Chr.)"],
  [],
  "Es chliises Volk zwüsche Grossmächt",
  "D Schrifte vom Alte Teschtamänt sind i me chliine Land entstande, uf de Landbrugg zwüsche Ägypte und Mesopotamie. Prägt händ s d Königriich Israel im Norde und Juda im Süde, d Eroberig vo Samaria dur d Assyrer (722/720 v. Chr., [[2KI.17.6]]), d Zerstörig vo Jerusalem und vom Tempel dur d Babylonier (587/586 v. Chr., [[2KI.25.8-2KI.25.10]]) mit de Verschleppig is Exil und d Ruggkeer under persischer Herrschaft ab 539 v. Chr. ([[EZR.1.1-EZR.1.4]]); de nöi Tempel isch um 515 v. Chr. iigweit worde. Vili Forscher gsend s Exil und d Perserziit als d Ziit, wo groossi Teil vo de Schrifte gsammlet und gformt worde sind.",
  "Di gnännte Date sind dur Quälle usserhalb vo de Bible guet gstützt. Wie vil vo de Überlieferig us de früene Königsziit oder no früener stammt, isch umstritte; Archäologie und Text wärded debii verschide gwichtet.",
  []),
 ("BG-OT-0002", "testament", "OT", "CTX-HIST-SECOND-TEMPLE", "high",
  "Tanach: die jüdische Ordnung",
  "Im Judentum heisst die Bibel Tanach, nach den Anfangsbuchstaben ihrer drei Teile: Tora (Weisung), Nevi'im (Propheten) und Ketuvim (Schriften). Es sind dieselben Bücher wie im evangelischen Alten Testament, aber in anderer Reihenfolge: Die Chronik steht am Schluss, Daniel, Rut, Ester und die Klagelieder gehören zu den Schriften. Christliche Bibeln folgen der Ordnung der griechischen Übersetzung (Septuaginta, ab dem 3. Jh. v. Chr. in Alexandria entstanden), die die Propheten ans Ende stellt, gleichsam als Übergang zum Neuen Testament.",
  "Die Reihenfolge innerhalb der Schriften schwankt in alten Listen; die Septuaginta entstand über einen längeren Zeitraum (die Tora zuerst) und ist keine einheitliche Übersetzung.",
  [], [],
  [T("heb", "תַּנַ״ךְ", "Tanach (Abkürzung der drei Teile)", "tanach"), T("heb", "תּוֹרָה", "Weisung", "tora"),
   T("heb", "נְבִיאִים", "Propheten", "nevi'im"), T("heb", "כְּתוּבִים", "Schriften", "ketuvim")],
  "Tanach: di jüdisch Ornig",
  "Im Judetum heisst d Bible Tanach, nach de Aafangsbuechstabe vo irne drüü Teil: Tora (Wiisig), Nevi'im (Prophete) und Ketuvim (Schrifte). Es sind di gliiche Büecher wie im evangelische Alte Teschtamänt, aber in ere andere Reiefolg: D Chronik staat am Schluss, de Daniel, d Rut, d Ester und d Chlaaglieder ghöred zu de Schrifte. Christlichi Bible folged de Ornig vo de griechische Übersetzig (Septuaginta, ab em 3. Jh. v. Chr. z Alexandria entstande), wo d Prophete as Änd stellt, wie en Überggang zum Nöie Teschtamänt.",
  "D Reiefolg innerhalb vo de Schrifte schwankt i alte Lischte; d Septuaginta isch über e längeri Ziit entstande (d Tora zerscht) und isch kei einheitlichi Übersetzig.",
  ["Tanach (Abchürzig vo de drüü Teil)", "Wiisig", "Prophete", "Schrifte"]),
 ("BG-NT-0001", "testament", "NT", "CTX-HIST-EARLY-CHRISTIANITY", "probable",
  "Unter römischer Herrschaft",
  "Jesus lebte im 1. Jahrhundert in Galiläa und Judäa, die unter römischer Kontrolle standen: zuerst unter Herodes dem Grossen (gestorben 4 v. Chr.), dann unter seinen Söhnen; Judäa wurde ab 6 n. Chr. von römischen Präfekten verwaltet, darunter Pontius Pilatus (26–36 n. Chr., [[LUK.3.1]]). Die Gemeinden nach Ostern breiteten sich in den Städten des östlichen Mittelmeers aus, wo Griechisch die gemeinsame Sprache war. Einen tiefen Einschnitt bildeten der Jüdische Krieg und die Zerstörung des Tempels durch die Römer im Jahr 70 n. Chr.",
  "Die genauen Lebensdaten Jesu sind nicht sicher: Die Geburt wird meist vor 4 v. Chr. angesetzt, der Tod um 30 oder 33 n. Chr.",
  ["LUK.2.1-LUK.2.2", "LUK.3.1"], ["Flavius Josephus, Jüdischer Krieg", "Tacitus, Annalen 15,44"],
  [],
  "Under römischer Herrschaft",
  "De Jesus hät im 1. Jaarhundert z Galiläa und z Judäa gläbt, wo under römischer Kontrolle gstande sind: zerscht under em Herodes em Groosse (gstorbe 4 v. Chr.), dänn under sine Söön; Judäa isch ab 6 n. Chr. vo römische Präfekte verwaltet worde, under anderem vom Pontius Pilatus (26–36 n. Chr., [[LUK.3.1]]). D Gmeinde nach Oschtere händ sich i de Stedt vom öschtliche Mittelmeer usbreitet, wo Griechisch di gmeinsam Sprach gsii isch. En töiffe Iischnitt sind de Jüdisch Chrieg und d Zerstörig vom Tempel dur d Römer im Jaar 70 n. Chr. gsii.",
  "Di gnaue Läbesdate vom Jesus sind nöd sicher: D Geburt wird meischtens vor 4 v. Chr. aagsetzt, de Tod um 30 oder 33 n. Chr.",
  []),
 ("BG-NT-0002", "testament", "NT", "CTX-HIST-EARLY-CHRISTIANITY", "probable",
  "Zuerst Briefe, dann Evangelien",
  "Die ältesten Schriften des Neuen Testaments sind Briefe des Paulus aus den Jahren um 50 bis 60 n. Chr., als erster wohl der 1. Thessalonicherbrief. Die Evangelien wurden nach verbreiteter Ansicht zwischen etwa 65 und 100 n. Chr. geschrieben, das Markusevangelium meist als ältestes. Vorher wurde von Jesus mündlich erzählt; Paulus gibt solche Überlieferung selbst weiter ([[1CO.15.3-1CO.15.8]]). Das Wort Evangelium bedeutet «gute Nachricht».",
  "Die Datierungen sind umstritten: Manche setzen die Evangelien früher an (vor 70 n. Chr.), andere einzelne Briefe deutlich später. Bei mehreren Briefen ist die Verfasserschaft umstritten.",
  ["1TH.1.1", "1CO.15.3-1CO.15.8"], [],
  [T("grc", "εὐαγγέλιον", "gute Nachricht")],
  "Zerscht Brief, dänn Evangelie",
  "Di eltischte Schrifte vom Nöie Teschtamänt sind Brief vom Paulus us de Jaar um 50 bis 60 n. Chr., als erschte wahrschiinli de 1. Thessalonicherbrief. D Evangelie sind nach verbreiteter Aasicht zwüsche öppe 65 und 100 n. Chr. gschribe worde, s Markusevangelium meischtens als s eltischt. Vorhär hät me vom Jesus mündlich verzellt; de Paulus git sonigi Überlieferig sälber wiiter ([[1CO.15.3-1CO.15.8]]). S Wort Evangelium heisst «gueti Nachricht».",
  "D Datierige sind umstritte: Es paar setzed d Evangelie früener aa (vor 70 n. Chr.), anderi einzelni Brief tüütli spööter. Bi meerere Brief isch umstritte, wär si gschribe hät.",
  ["gueti Nachricht"]),
 ("BG-GROUP-01-0001", "book_group", "GROUP-01", "CTX-HIST-ISRAEL-IRON-PERSIAN", "possible",
  "Tora: Weisung für ein Volk",
  "Die fünf Bücher bilden im Judentum die Tora, den wichtigsten Teil der Bibel; sie wird im Synagogengottesdienst fortlaufend gelesen. Die Überlieferung nennt Mose als Verfasser. Die historisch-kritische Forschung sieht in den Büchern verschiedene Überlieferungen, die über Jahrhunderte zusammengewachsen sind und nach verbreiteter Ansicht in persischer Zeit (5./4. Jh. v. Chr.) ihre weitgehend heutige Gestalt erhielten. Gesetze und Erzählungen sind dabei eng verbunden: Die Weisungen stehen im Rahmen der Geschichte von der Befreiung aus Ägypten.",
  "Wie die Entstehung genau verlief, ist offen. Das klassische Modell von vier Quellen (J, E, D, P) wird heute vielfach durch andere Modelle ersetzt oder ergänzt; traditionelle Ausleger halten im Kern an der Verfasserschaft des Mose fest.",
  ["DEU.31.9", "DEU.34.5-DEU.34.8"], [],
  [T("heb", "תּוֹרָה", "Weisung", "tora")],
  "Tora: Wiisig für es Volk",
  "Di füüf Büecher sind im Judetum d Tora, de wichtigscht Teil vo de Bible; si wird im Gottesdienscht i de Synagoge fortlaufend gläse. D Überlieferig nännt de Mose als Verfasser. D historisch-kritisch Forschig gseet i de Büecher verschideni Überlieferige, wo über Jaarhunderti zämegwachse sind und nach verbreiteter Aasicht i persischer Ziit (5./4. Jh. v. Chr.) iri wiitgehend hütig Gstalt übercho händ. Gsetz und Verzellige sind debii äng verbunde: D Wiisige stönd im Raame vo de Gschicht vo de Befreiig us Ägypte.",
  "Wie d Entstehig gnau verloffe isch, isch offe. S klassisch Modell vo vier Quälle (J, E, D, P) wird hüt vilfach dur anderi Modell ersetzt oder ergänzt; traditionelli Usleger halted im Kärn dra fescht, dass de Mose de Verfasser isch.",
  ["Wiisig"]),
 ("BG-GROUP-01-0002", "book_group", "GROUP-01", "CTX-HIST-ISRAEL-IRON-PERSIAN", "possible",
  "Ägypten, Auszug und ausserbiblische Spuren",
  "Exodus erzählt vom Auszug Israels aus Ägypten ([[EXO.12.37-EXO.12.41]]). Die älteste ausserbiblische Erwähnung Israels steht auf der Siegesstele des Pharao Merenptah (um 1208 v. Chr.): Sie nennt «Israel» als Volk in Kanaan. Direkte ägyptische Belege für einen Auszug gibt es nicht. Für die Bibel ist der Auszug die Gründungserinnerung schlechthin; Feste wie Passa und viele Gebote beziehen sich darauf ([[DEU.5.15]]).",
  "Wie weit die Erzählung historische Ereignisse wiedergibt, ist stark umstritten: Die Spannbreite reicht von einem weitgehend historischen Auszug über die Erinnerung kleinerer Gruppen bis zu einer vor allem literarischen Gründungserzählung.",
  ["EXO.12.37-EXO.12.41", "DEU.5.15"], ["Merenptah-Stele (um 1208 v. Chr.), Ägyptisches Museum Kairo"],
  [],
  "Ägypte, Uszug und Spure usserhalb vo de Bible",
  "S Exodus verzellt vom Uszug vo Israel us Ägypte ([[EXO.12.37-EXO.12.41]]). Di eltischt Erwäänig vo Israel usserhalb vo de Bible staat uf de Siegesstele vom Pharao Merenptah (um 1208 v. Chr.): Si nännt «Israel» als Volk z Kanaan. Diräkti ägyptischi Bewiis für en Uszug gits nöd. Für d Bible isch de Uszug d Gründigserinnerig überhaupt; Fescht wie s Passa und vili Gebot bezieend sich druf ([[DEU.5.15]]).",
  "Wie wiit d Verzellig gschichtlichi Ereigniss widergit, isch stark umstritte: D Bandbreiti gaat vo me wiitgehend gschichtliche Uszug über d Erinnerig vo chliinere Gruppe bis zu ere vor allem literarische Gründigsverzellig.",
  []),
 ("BG-GROUP-02-0001", "book_group", "GROUP-02", "CTX-HIST-ISRAEL-IRON-PERSIAN", "probable",
  "Geschichte, zweimal erzählt",
  "Die Bücher Josua bis Könige erzählen von der Landnahme bis zum Exil; sie enden mit dem König Jojachin in babylonischer Gefangenschaft ([[2KI.25.27-2KI.25.30]]). Seit Martin Noth (1943) fassen viele Forscher Deuteronomium bis Könige als «deuteronomistisches Geschichtswerk» zusammen, das die Geschichte am Massstab des Deuteronomiums misst: Treue zu dem einen Gott und ein Heiligtum in Jerusalem. Die Chronik erzählt dieselbe Königszeit später noch einmal, mit David und dem Tempel im Mittelpunkt. Esra und Nehemia führen in die Perserzeit. Ausserbiblische Inschriften nennen Könige wie Omri und Ahab; die Tel-Dan-Inschrift (9. Jh. v. Chr.) spricht nach verbreiteter Lesung vom «Haus Davids».",
  "Wie zuverlässig die Erzählungen über die frühe Zeit (Landnahme, Richter, David und Salomo) historisch sind, ist umstritten. Auch das Modell eines einheitlichen deuteronomistischen Geschichtswerks wird heute unterschiedlich beurteilt.",
  ["2KI.25.27-2KI.25.30", "1CH.29.26-1CH.29.30", "EZR.1.1"], ["Mescha-Stele (um 840 v. Chr.)", "Kurkh-Monolith Salmanassars III. (853 v. Chr.)", "Tel-Dan-Inschrift (9. Jh. v. Chr.)"],
  [],
  "Gschicht, zwei Mal verzellt",
  "D Büecher Josua bis Könige verzelled vo de Landnaam bis is Exil; si höred mit em König Jojachin i babylonischer Gfangeschaft uf ([[2KI.25.27-2KI.25.30]]). Sit em Martin Noth (1943) fassed vili Forscher Deuteronomium bis Könige als «deuteronomistischs Gschichtswärch» zäme, wo d Gschicht am Massstab vom Deuteronomium misst: Tröii zu däm einte Gott und es Heiligtum z Jerusalem. D Chronik verzellt di gliich Königsziit spööter nomal, mit em David und em Tempel i de Mitti. Esra und Nehemia füered i d Perserziit. Inschrifte usserhalb vo de Bible nänned König wie de Omri und de Ahab; d Tel-Dan-Inschrift (9. Jh. v. Chr.) redt nach verbreiteter Läsig vom «Huus vom David».",
  "Wie zueverlässig d Verzellige über di früe Ziit (Landnaam, Richter, David und Salomo) gschichtlich sind, isch umstritte. Au s Modell vo me einheitliche deuteronomistische Gschichtswärch wird hüt verschide beurteilt.",
  []),
 ("BG-GROUP-03-0001", "book_group", "GROUP-03", "CTX-HIST-ISRAEL-IRON-PERSIAN", "probable",
  "Gebete, Lieder und Weisheit",
  "Die Psalmen sind ein Gebets- und Liederbuch, das über Jahrhunderte gewachsen ist; es ist in fünf Bücher gegliedert, die je mit einem Lobpreis enden (z. B. [[PSA.41.13]]; [[PSA.72.19]]; [[PSA.89.52]]; [[PSA.106.48]]). Hebräische Dichtung arbeitet weniger mit Reim als mit Parallelismus: Ein Gedanke wird in der zweiten Zeile wiederholt, gesteigert oder kontrastiert. Weisheit war im Alten Orient eine verbreitete Gattung; [[PRO.22.17-PRO.24.22]] berührt sich eng mit der ägyptischen Lehre des Amenemope. Hiob und Kohelet stellen die gängigen Antworten kritisch in Frage.",
  "Die Zuschreibung an David und Salomo ist Überlieferung; viele Psalmenüberschriften gelten als spätere Zusätze. Bei Sprüche und Amenemope wird meist angenommen, dass Sprüche die ägyptische Lehre aufnimmt, die Richtung der Abhängigkeit ist aber diskutiert worden.",
  ["PSA.41.13", "PSA.72.19", "PSA.89.52", "PSA.106.48", "PRO.22.17-PRO.24.22"], ["Lehre des Amenemope (Ägypten, Ende 2. Jt. v. Chr.)"],
  [T("heb", "תְּהִלִּים", "Lobgesänge (Psalmen)", "tehillim"), T("heb", "חָכְמָה", "Weisheit", "chochma")],
  "Gebät, Lieder und Wiisheit",
  "D Psalme sind es Gebäts- und Liederbuech, wo über Jaarhunderti gwachse isch; es isch i füüf Büecher gliederet, wo jedes mit eme Lobpriis ufhört (z. B. [[PSA.41.13]]; [[PSA.72.19]]; [[PSA.89.52]]; [[PSA.106.48]]). Hebräischi Dichtig schaffet weniger mit Riim als mit Parallelismus: En Gedanke wird i de zweite Ziile widerholt, gsteigeret oder em andere gägenüberstellt. Wiisheit isch im Alte Orient e verbreiteti Gattig gsii; [[PRO.22.17-PRO.24.22]] berüert sich äng mit de ägyptische Lehr vom Amenemope. Hiob und Kohelet stelled di gängige Antworte kritisch i Frag.",
  "Dass d Psalme vom David und d Sprüch vom Salomo sind, isch Überlieferig; vili Psalmeüberschrifte gälted als spööteri Zuesätz. Bi de Sprüch und em Amenemope nimmt me meischtens aa, dass d Sprüch di ägyptisch Lehr ufnänd, d Richtig vo de Abhängigkeit isch aber diskutiert worde.",
  ["Lobgsäng (Psalme)", "Wiisheit"]),
 ("BG-GROUP-04-0001", "book_group", "GROUP-04", "CTX-HIST-ISRAEL-IRON-PERSIAN", "probable",
  "Propheten in Krisenzeiten",
  "Prophetie gab es im ganzen Alten Orient; aus Mari und Assyrien sind Prophetensprüche überliefert. Die grossen Prophetenbücher begleiten die Krisen Judas: Jesaja wirkte im 8. Jh. v. Chr. in Jerusalem zur Zeit der assyrischen Bedrohung; Jeremia erlebte den Untergang Judas 587/586 v. Chr.; Ezechiel wirkte unter den Verschleppten in Babylonien. Viele Forscher sehen in Jesaja 40–55 eine spätere Fortschreibung aus der Exilszeit, weil dort der Perserkönig Kyros genannt wird ([[ISA.45.1]]). Das Buch Daniel spielt im Exil.",
  "Die Aufteilung Jesajas in mehrere Teile ist verbreitet, wird aber von traditionellen Auslegern abgelehnt. Daniel wird von der historisch-kritischen Forschung meist in die Zeit der Verfolgung unter Antiochus IV. (167–164 v. Chr.) datiert, traditionell ins 6. Jh. v. Chr. Im Judentum gehören Daniel und die Klagelieder nicht zu den Propheten, sondern zu den Schriften.",
  ["ISA.1.1", "ISA.45.1", "JER.1.1-JER.1.3", "EZK.1.1-EZK.1.3"], ["Prophetentexte aus Mari (18. Jh. v. Chr.)"],
  [T("heb", "נָבִיא", "Prophet", "navi")],
  "Prophete i Chriseziite",
  "Prophetie hät s im ganze Alte Orient gää; us Mari und Assyrie sind Prophetesprüch überliferet. Di groosse Prophetebüecher begleited d Krise vo Juda: De Jesaja hät im 8. Jh. v. Chr. z Jerusalem gwürkt, i de Ziit vo de assyrische Bedroohig; de Jeremia hät de Undergang vo Juda 587/586 v. Chr. erläbt; de Ezechiel hät under de Verschleppte z Babylonie gwürkt. Vili Forscher gsend i Jesaja 40–55 e spööteri Fortschriibig us de Exilsziit, wil dört de Perserkönig Kyros gnännt wird ([[ISA.45.1]]). S Buech Daniel spilt im Exil.",
  "D Ufteilig vom Jesaja i meereri Teil isch verbreitet, wird aber vo traditionelle Usleger abglehnt. De Daniel wird vo de historisch-kritische Forschig meischtens i d Ziit vo de Verfolgig under em Antiochus IV. (167–164 v. Chr.) datiert, traditionell is 6. Jh. v. Chr. Im Judetum ghöred de Daniel und d Chlaaglieder nöd zu de Prophete, sondern zu de Schrifte.",
  ["Prophet"]),
 ("BG-GROUP-05-0001", "book_group", "GROUP-05", "CTX-HIST-ISRAEL-IRON-PERSIAN", "probable",
  "Zwölf auf einer Rolle",
  "Die zwölf kleineren Propheten galten im Judentum als ein einziges Buch, «die Zwölf», das auf eine Schriftrolle passte; schon Jesus Sirach (um 180 v. Chr.) spricht von den «zwölf Propheten» ([[SIR.49.10]]). Die Sammlung umfasst rund drei Jahrhunderte: Amos und Hosea wirkten im 8. Jh. v. Chr. im Nordreich Israel ([[AMO.1.1]]; [[HOS.1.1]]), Haggai und Sacharja um 520 v. Chr. beim Wiederaufbau des Tempels ([[HAG.1.1]]), Maleachi in persischer Zeit.",
  "Die Datierung von Joel, Obadja und Jona ist umstritten; Jona wird oft als Lehrerzählung gelesen, traditionell auch als Bericht.",
  ["AMO.1.1", "HOS.1.1", "HAG.1.1"], ["Jesus Sirach 49,10"],
  [],
  "Zwölf uf eire Rolle",
  "Di zwölf chliinere Prophete händ im Judetum als eis einzigs Buech gulte, «di Zwölf», wo uf ei Schriftrolle passt hät; scho de Jesus Sirach (um 180 v. Chr.) redt vo de «zwölf Prophete» ([[SIR.49.10]]). D Sammlig umfasst öppe drüü Jaarhunderti: De Amos und de Hosea händ im 8. Jh. v. Chr. im Nordriich Israel gwürkt ([[AMO.1.1]]; [[HOS.1.1]]), de Haggai und de Sacharja um 520 v. Chr. bim Wideruufbau vom Tempel ([[HAG.1.1]]), de Maleachi i persischer Ziit.",
  "D Datierig vom Joel, vom Obadja und vom Jona isch umstritte; de Jona wird oft als Lehrverzellig gläse, traditionell au als Bricht.",
  []),
 ("BG-GROUP-06-0001", "book_group", "GROUP-06", "CTX-HIST-EARLY-CHRISTIANITY", "probable",
  "Vier Erzählungen von Jesus",
  "Die Evangelien erzählen Leben, Tod und Auferstehung Jesu; ihre Form steht antiken Lebensbeschreibungen (bios) nahe. Matthäus, Markus und Lukas heissen Synoptiker, weil man sie in einer Zusammenschau nebeneinanderlegen kann; sie teilen viel Stoff, oft wörtlich. Verbreitet ist die Erklärung, dass Matthäus und Lukas das Markusevangelium und eine zweite, verlorene Spruchsammlung («Q») benutzten. Johannes erzählt eigenständig. Lukas sagt selbst, dass er Überlieferungen gesammelt und geordnet hat ([[LUK.1.1-LUK.1.4]]).",
  "Neben der Zwei-Quellen-Theorie werden andere Modelle vertreten (z. B. Lukas kannte Matthäus, ohne «Q»). Die Verfasser werden in den Evangelien selbst nicht genannt (vgl. aber [[JHN.21.24]]); die Überschriften «Evangelium nach …» sind ab dem 2. Jahrhundert bezeugt.",
  ["LUK.1.1-LUK.1.4", "JHN.21.24"], ["Irenäus, Gegen die Häresien 3,1,1 (um 180 n. Chr.)"],
  [T("grc", "βίος", "Leben, Lebensbeschreibung"), T("grc", "σύνοψις", "Zusammenschau")],
  "Vier Verzellige vom Jesus",
  "D Evangelie verzelled vom Läbe, vom Tod und vo de Uferstehig vom Jesus; iri Form isch nööch bi antike Läbesbeschriibige (bios). Matthäus, Markus und Lukas heissed Synoptiker, wil me si inere Zämeschau näbenand cha legge; si teiled vil Stoff, oft wörtlich. Verbreitet isch d Erkläärig, dass de Matthäus und de Lukas s Markusevangelium und e zweiti, verloreni Spruchsammlig («Q») bruucht händ. De Johannes verzellt eigeständig. De Lukas seit sälber, dass er Überlieferige gsammlet und gornet hät ([[LUK.1.1-LUK.1.4]]).",
  "Näbe de Zwei-Quälle-Theorie wärded anderi Modell vertrete (z. B. de Lukas heg de Matthäus kännt, ohni «Q»). D Verfasser wärded i de Evangelie sälber nöd gnännt (vgl. aber [[JHN.21.24]]); d Überschrifte «Evangelium nach …» sind ab em 2. Jaarhundert bezüügt.",
  ["Läbe, Läbesbeschriibig", "Zämeschau"]),
 ("BG-GROUP-07-0001", "book_group", "GROUP-07", "CTX-HIST-EARLY-CHRISTIANITY", "probable",
  "Von Jerusalem bis Rom",
  "Die Apostelgeschichte ist der zweite Teil eines Doppelwerks; wie das Lukasevangelium ist sie Theophilus gewidmet ([[ACT.1.1]]; vgl. [[LUK.1.3]]). Sie erzählt, wie die Botschaft von Jerusalem bis nach Rom gelangt ([[ACT.1.8]]; [[ACT.28.14]]). In einigen Abschnitten erzählt sie in der Wir-Form ([[ACT.16.10-ACT.16.17]]). Einen festen Zeitpunkt liefert eine Inschrift aus Delphi: Sie datiert die Amtszeit des Statthalters Gallio in Achaia um 51/52 n. Chr., vor den Paulus in Korinth gebracht wurde ([[ACT.18.12]]).",
  "Die Wir-Abschnitte werden traditionell als Hinweis auf einen Reisebegleiter des Paulus gedeutet, von anderen als literarisches Mittel. Die Apostelgeschichte wird meist um 80–90 n. Chr. datiert, von manchen früher (um 62) oder später (2. Jh.).",
  ["ACT.1.1", "ACT.1.8", "ACT.18.12", "ACT.28.14"], ["Gallio-Inschrift, Delphi (um 52 n. Chr.)"],
  [],
  "Vo Jerusalem bis Rom",
  "D Apostelgschicht isch de zweit Teil vo me Doppelwärch; wie s Lukasevangelium isch si em Theophilus gwidmet ([[ACT.1.1]]; vgl. [[LUK.1.3]]). Si verzellt, wie d Botschaft vo Jerusalem bis uf Rom chunnt ([[ACT.1.8]]; [[ACT.28.14]]). I es paar Abschnitt verzellt si i de Mir-Form ([[ACT.16.10-ACT.16.17]]). En feschte Ziitpunkt liferet e Inschrift us Delphi: Si datiert d Amtsziit vom Statthalter Gallio z Achaia um 51/52 n. Chr., vor dä de Paulus z Korinth bracht worde isch ([[ACT.18.12]]).",
  "D Mir-Abschnitt wärded traditionell als Hiiwiis uf en Reisebegleiter vom Paulus düütet, vo andere als literarischs Mittel. D Apostelgschicht wird meischtens um 80–90 n. Chr. datiert, vo es paar früener (um 62) oder spööter (2. Jh.).",
  []),
 ("BG-GROUP-08-0001", "book_group", "GROUP-08", "CTX-HIST-EARLY-CHRISTIANITY", "probable",
  "Briefe an Gemeinden in Städten",
  "Paulus schrieb an Gemeinden in Städten des Römischen Reiches (Rom, Korinth, Philippi, Thessalonich, die Gemeinden in Galatien) und an Einzelne. Die Briefe folgen der antiken Briefform mit Absender, Empfänger und Gruss und wurden oft einem Schreiber diktiert ([[ROM.16.22]]); sie wurden in den Gemeinden vorgelesen und weitergegeben ([[COL.4.16]]). Sie sind die ältesten erhaltenen christlichen Schriften. In der Bibel sind sie nach Länge geordnet, nicht nach Entstehung.",
  "Sieben Briefe gelten fast allgemein als von Paulus selbst (Römer, 1. und 2. Korinther, Galater, Philipper, 1. Thessalonicher, Philemon). Bei Epheser, Kolosser, 2. Thessalonicher und den Briefen an Timotheus und Titus ist die Verfasserschaft umstritten.",
  ["ROM.16.22", "COL.4.16", "1TH.1.1"], [],
  [],
  "Brief a Gmeinde i Stedt",
  "De Paulus hät a Gmeinde i Stedt vom Römische Riich gschribe (Rom, Korinth, Philippi, Thessalonich, d Gmeinde z Galatie) und a einzelni Lüüt. D Brief folged de antike Briefform mit Absänder, Empfänger und Gruess und sind oft eme Schriiber diktiert worde ([[ROM.16.22]]); me hät si i de Gmeinde vorgläse und wiitergää ([[COL.4.16]]). Si sind di eltischte erhaltene christliche Schrifte. I de Bible sind si nach de Längi gornet, nöd nach de Entstehig.",
  "Sibe Brief gälted fascht allgemein als vom Paulus sälber (Römer, 1. und 2. Korinther, Galater, Philipper, 1. Thessalonicher, Philemon). Bim Epheser, Kolosser, 2. Thessalonicher und de Brief a Timotheus und Titus isch umstritte, wär si gschribe hät.",
  []),
 ("BG-GROUP-09-0001", "book_group", "GROUP-09", "CTX-HIST-EARLY-CHRISTIANITY", "probable",
  "Briefe an weite Kreise",
  "Der Hebräerbrief nennt keinen Verfasser; die Zuschreibung an Paulus wurde schon in der Alten Kirche bezweifelt – Origenes meinte, wer ihn geschrieben habe, wisse in Wahrheit Gott. Die übrigen Briefe (Jakobus, 1. und 2. Petrus, 1. bis 3. Johannes, Judas) heissen «katholische», das heisst allgemeine Briefe, weil die meisten nicht an eine einzelne Gemeinde gerichtet sind ([[JAS.1.1]]; [[1PE.1.1]]).",
  "Wer diese Briefe geschrieben hat und wann, ist bei mehreren umstritten, besonders beim 2. Petrusbrief. Einige von ihnen waren noch im 4. Jahrhundert nicht überall als Teil des Kanons anerkannt.",
  ["HEB.13.22-HEB.13.25", "JAS.1.1", "1PE.1.1"], ["Eusebius, Kirchengeschichte 6,25,14 (Origenes über den Hebräerbrief)"],
  [T("grc", "καθολικός", "allgemein")],
  "Brief a wiiti Chreis",
  "De Hebräerbrief nännt kein Verfasser; dass er vom Paulus sei, hät me scho i de Alte Chile bezwiiflet – de Origenes hät gmeint, wär en gschribe heg, wüssi i Würklichkeit Gott. Di andere Brief (Jakobus, 1. und 2. Petrus, 1. bis 3. Johannes, Judas) heissed «katholischi», das heisst allgemeini Brief, wil di meischte nöd a e einzelni Gmeind grichtet sind ([[JAS.1.1]]; [[1PE.1.1]]).",
  "Wär die Brief gschribe hät und wänn, isch bi meerere umstritte, bsunders bim 2. Petrusbrief. Es paar devo sind no im 4. Jaarhundert nöd überall als Teil vom Kanon aagnoo gsii.",
  ["allgemein"]),
 ("BG-GROUP-10-0001", "book_group", "GROUP-10", "CTX-HIST-EARLY-CHRISTIANITY", "probable",
  "Bilder gegen die Macht Roms",
  "Die Offenbarung gehört zur Gattung Apokalypse, griechisch «Enthüllung»: Sie deutet die Gegenwart in Visionen und Bildern, wie schon das Buch Daniel. Der Seher Johannes schreibt von der Insel Patmos ([[REV.1.9]]) an sieben Gemeinden in der römischen Provinz Asia ([[REV.1.11]]). Im Hintergrund stehen der Kaiserkult und der Druck, sich ihm anzupassen. Die Zahl 666 ([[REV.13.18]]) wird oft als Zahlenwert des Namens «Kaiser Nero» in hebräischen Buchstaben gedeutet.",
  "Meist wird die Offenbarung in die späte Regierungszeit Domitians (um 95 n. Chr.) datiert, gestützt auf Irenäus; andere denken an die Zeit um 68/69 n. Chr. Die Deutung der Zahl 666 auf Nero ist verbreitet, aber nicht sicher; einige Handschriften lesen 616.",
  ["REV.1.9", "REV.1.11", "REV.13.18"], ["Irenäus, Gegen die Häresien 5,30,3"],
  [T("grc", "ἀποκάλυψις", "Enthüllung, Offenbarung")],
  "Bilder gäge d Macht vo Rom",
  "D Offebarig ghört zur Gattig Apokalypse, griechisch «Enthüllig»: Si düütet d Gägewart i Visione und Bilder, wie scho s Buech Daniel. De Seher Johannes schriibt vo de Insle Patmos ([[REV.1.9]]) a sibe Gmeinde i de römische Provinz Asia ([[REV.1.11]]). Im Hintergrund stönd de Kaiserkult und de Druck, sich dem aazpasse. D Zaal 666 ([[REV.13.18]]) wird oft als Zaalewärt vom Name «Kaiser Nero» i hebräische Buechstabe düütet.",
  "Meischtens wird d Offebarig i di spoot Regierigsziit vom Domitian (um 95 n. Chr.) datiert, gstützt uf de Irenäus; anderi dänked a d Ziit um 68/69 n. Chr. D Düütig vo de Zaal 666 uf de Nero isch verbreitet, aber nöd sicher; es paar Handschrifte läsed 616.",
  ["Enthüllig, Offebarig"]),
]


def write_if_changed(path, rec, change_de):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        old = json.loads(path.read_text(encoding="utf-8"))
        cmp = lambda r: {k: v for k, v in r.items() if k not in ("revision_log", "knowledge")}
        if cmp(old) == cmp(rec):
            return False
        rec["revision_log"] = old.get("revision_log", []) + [{"date": DATE, "change_de": change_de, "previous": cmp(old)}]
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


n = 0
for c in CONTEXTS:
    rec = {"id": c["id"], "type": "context", "status": "draft", "tags": ["TAG-HISTORICAL-BACKGROUND"], **{k: v for k, v in c.items() if k != "id"}}
    n += write_if_changed(D / "contexts" / f"{c['id']}.json", rec, "Kontext überarbeitet")
for (rid, scope, key, ctx, conf, topic, text, unc, ev, src, terms, g_topic, g_text, g_unc, g_terms) in NOTES:
    assert len(g_terms) == len(terms), rid
    rec = {"id": rid, "type": "background_note", "status": "draft", "tags": ["TAG-HISTORICAL-BACKGROUND"], "scope": scope}
    if scope == "testament":
        rec["testament"] = key
    if scope == "book_group":
        rec["group"] = key
    rec.update({"context": ctx, "topic_de": topic, "text_de": text, "confidence": conf, "uncertain_de": unc,
                "evidence_refs": ev, **({"sources_de": src} if src else {}), **({"terms": terms} if terms else {}),
                "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}})
    n += write_if_changed(D / "background" / "overview" / f"{rid}.json", rec, "Hintergrund überarbeitet")
    fields = {"topic_de": g_topic, "text_de": g_text, "uncertain_de": g_unc, **({"terms": g_terms} if terms else {})}
    loc = {"id": "L10N-GSW-ZH-" + rid, "type": "localization", "status": "draft", "tags": [], "localizes": rid, "language": LANG,
           "target_context": "CTX-CH-ZH-GSW-2026", "fields": fields,
           "source_fingerprint": {k: localizations.fingerprint(rec.get(k)) for k in fields},
           "authorship_de": AUTH_GSW, "review_de": "Noch keine muttersprachliche Prüfung dokumentiert.",
           "knowledge": {"asserted_at": DATE, "supersedes": None}}
    n += write_if_changed(D / "localizations" / LANG / f"{rid}.json", loc, "Fassung erneuert")
print(f"PASS: {len(NOTES)} Hintergrundnotizen für die oberen Ebenen, {len(CONTEXTS)} Kontexte; {n} Dateien geschrieben")
