#!/usr/bin/env python3
"""Autorenwerkzeug: Titusbrief – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/titus_text.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, write  # noqa: E402

DATE = "2026-10-13"
AUTH = "KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-TITUS"]
K = {"de": "Kontrolle", "gsw": "gsw"}

DE = {
 # ------------------------------------------------------------ Kapitel 1
 "TIT.1.1": "Paulus{1}, Knecht{2} Gottes{3} und{5} Apostel{4} Jesu{6} Christi{7}, [für]{8} [den Glauben]{9} [der Auserwählten]{10} Gottes{11} und{12} für [die Erkenntnis]{13} [der Wahrheit]{14}, die{15} [der Frömmigkeit]{17} [entspricht]{16},",
 "TIT.1.2": "[in]{1} [der Hoffnung]{2} auf [ewiges]{4} Leben{3}, [das]{5} [der]{7} Gott{9}, [der nicht lügt]{8}, [vor]{10} [ewigen]{12} Zeiten{11} [verheissen hat]{6};",
 "TIT.1.3": "[Zu seiner Zeit]{3,4} aber{2} [hat er]{1} [sein]{7} [Wort]{5,6} [offenbart]{1} [in]{8} [der Verkündigung]{9}, [die]{10} [mir]{12} [anvertraut worden ist]{11} [nach]{13} [dem Auftrag]{14} Gottes{18}, [unseres]{17} [Retters]{15,16}.",
 "TIT.1.4": "An Titus{1}, mein [echtes]{2} Kind{3} [im]{4} [gemeinsamen]{5} Glauben{6}: Gnade{7} und{8} Friede{9} [von]{10} Gott{11}, [dem Vater]{12}, und{13} [von Christus Jesus]{14,15}, [unserem]{18} [Retter]{16,17}.",
 "TIT.1.5": "[Deswegen]{1,2} [habe ich]{3} dich{4} [in]{5} Kreta{6} [zurückgelassen]{3}, [damit]{7} du [das]{8}, [was noch fehlt]{9}, [in Ordnung bringst]{10} und{11} [in jeder]{13} Stadt{14} [Älteste]{15} [einsetzt]{12}, [wie]{16} ich{17} [es dir]{18} [aufgetragen habe]{19}:",
 "TIT.1.6": "[wenn]{1} [einer]{2} [untadelig]{4} [ist]{3}, [Mann]{7} [einer einzigen Frau]{5,6}, [der gläubige]{10} Kinder{8} [hat]{9}, [die nicht]{11} [im Ruf]{12,13} [eines liederlichen Lebens]{14} stehen [oder]{15} [widerspenstig]{16} sind.",
 "TIT.1.7": "Denn{2} [der]{3} Aufseher{4} [muss]{1} [als]{7} Verwalter{9} Gottes{8} untadelig{5} sein{6}: nicht{10} [eigenmächtig]{11}, nicht{12} [jähzornig]{13}, [kein]{14} [Trinker]{15}, [kein]{16} [Schläger]{17}, nicht{18} [auf schändlichen Gewinn aus]{19},",
 "TIT.1.8": "sondern{1} [gastfreundlich]{2}, [dem Guten zugetan]{3}, [besonnen]{4}, [gerecht]{5}, [fromm]{6}, [beherrscht]{7};",
 "TIT.1.9": "einer, der sich [an das]{2} [zuverlässige]{6} Wort{7} [hält]{1}, das [der]{4} Lehre{5} [entspricht]{3}, [damit]{8} er [fähig]{9} [ist]{10}, [sowohl]{11} [mit]{13} [der]{14} [gesunden]{16,17} Lehre{15} [zu ermahnen]{12} [als auch]{18} [die]{19} [Widersprechenden]{20} [zurechtzuweisen]{21}.",
 "TIT.1.10": "Denn{2} [es gibt]{1} [viele]{3} [Widerspenstige]{5}, [Schwätzer]{6} und{7} [Verführer]{8}, [besonders]{9} [die]{10} [aus]{11} [der]{12} [Beschneidung]{13}. ~4(καί verbindet «viele» und «Widerspenstige»; in einigen Ausgaben fehlt es; nicht eigens wiedergegeben)",
 "TIT.1.11": "[Denen]{1} [muss]{2} man [den Mund stopfen]{3:idiom}, [denn sie]{4} [bringen]{7} [ganze]{5} [Familien]{6} [durcheinander]{7}, [indem sie lehren]{8}, [was]{9} [nicht]{10} [sein darf]{11}, [um]{14} [schändlichen]{12} [Gewinns]{13} [willen]{14}.",
 "TIT.1.12": "[Einer]{2} [von]{3} [ihnen]{4}, [ihr]{6} [eigener]{5} [Prophet]{7}, [hat gesagt]{1}: «Kreter{8} sind [immer]{9} [Lügner]{10}, [böse]{11} [Tiere]{12}, [faule]{14} [Bäuche]{13}.»",
 "TIT.1.13": "[Dieses]{3} [Zeugnis]{1,2} [ist]{4} [wahr]{5}. [Aus]{6} [diesem]{7} [Grund]{8} [weise]{9} [sie]{10} [scharf]{11} [zurecht]{9}, [damit]{12} [sie gesund]{13} [im]{14,15} [Glauben]{16} [sind]{13}",
 "TIT.1.14": "und [nicht]{1} [auf]{2} [jüdische]{3} [Mythen]{4} [achten]{2} [und]{5} [auf Gebote]{6} [von Menschen]{7}, [die sich]{8} [von der]{9} [Wahrheit]{10} [abwenden]{8}.",
 "TIT.1.15": "[Alles]{1} ist [rein]{2} [für die]{3} [Reinen]{4}; [für die]{5} [Befleckten]{7} [aber]{6} und{8} [Ungläubigen]{9} ist [nichts]{10} [rein]{11}, [sondern]{12} [befleckt sind]{13} [sowohl]{15} [ihr]{14} [Verstand]{16,17} [als auch]{18} [ihr Gewissen]{19,20}.",
 "TIT.1.16": "Sie [behaupten]{2}, Gott{1} [zu kennen]{3}, [mit den]{4} [Werken]{6} [aber]{5} [verleugnen sie ihn]{7}; [abscheulich]{8} [sind sie]{9} und{10} [ungehorsam]{11} und{12} [für]{13} [jedes]{14} [gute]{16} [Werk]{15} [untauglich]{17}.",
 # ------------------------------------------------------------ Kapitel 2
 "TIT.2.1": "[Du]{1} [aber]{2} [rede]{3}, [was]{4} [der]{6} [gesunden]{7} [Lehre]{8} [entspricht]{5}.",
 "TIT.2.2": "[Ältere Männer]{1} [sollen]{3} [nüchtern]{2} [sein]{3}, [würdig]{4}, [besonnen]{5}, [gesund]{6} [im]{7} [Glauben]{8}, [in der]{9} [Liebe]{10}, [in der]{11} [Ausdauer]{12}.",
 "TIT.2.3": "[Ältere Frauen]{1} [ebenso]{2}: [in]{3} [ihrem Verhalten]{4} [ehrwürdig]{5}, [nicht]{6} [verleumderisch]{7}, [nicht]{8} [dem vielen]{10} [Wein]{9} [verfallen]{11}, [Lehrerinnen des Guten]{12},",
 "TIT.2.4": "[damit]{1} sie [die]{3} [jungen Frauen]{4} [anleiten]{2}, [ihre Männer]{5} und [Kinder]{7} [zu lieben]{6},",
 "TIT.2.5": "[besonnen]{1} zu sein, [rein]{2}, [häuslich tätig]{3}, [gütig]{4}, [ihren]{6} [eigenen]{7} [Männern]{8} [untergeordnet]{5}, [damit]{9} [das]{11} [Wort]{12} [Gottes]{13,14} [nicht]{10} [in Verruf kommt]{15}.",
 "TIT.2.6": "[Die]{1} [jüngeren Männer]{2} [ermahne]{4} [ebenso]{3}, [besonnen zu sein]{5}",
 "TIT.2.7": "[in]{1} [allem]{2}. [Zeige]{4} [dich selbst]{3} [als]{4} [Vorbild]{5} [guter]{6} [Werke]{7}, [in]{8} [der]{9} [Lehre]{10} [Unverfälschtheit]{11}, [Würde]{12},",
 "TIT.2.8": "[gesunde]{2}, [unanfechtbare]{3} [Rede]{1}, [damit]{4} [der]{5} [Gegner]{6,7} [beschämt wird]{8}, [weil er]{10} [nichts]{9} [Schlechtes]{14} [über]{12} [uns]{13} [zu sagen]{11} [hat]{10}.",
 "TIT.2.9": "[Sklaven]{1} sollen sich [ihren]{2} [Herren]{3} [in]{5} [allem]{6} [unterordnen]{4}, [ihnen gefällig]{7} [sein]{8}, [nicht]{9} [widersprechen]{10},",
 "TIT.2.10": "[nichts]{1} [unterschlagen]{2}, [sondern]{3} [volle]{4}, [gute]{7} [Treue]{5} [beweisen]{6}, [damit]{8} sie [die]{9,11} [Lehre]{10} [Gottes]{15}, [unseres]{14} [Retters]{12,13}, [in]{17} [allem]{18} [schmücken]{16}.",
 "TIT.2.11": "Denn{2} [erschienen ist]{1} [die]{3} [Gnade]{4} [Gottes]{5,6}, [rettend]{7} [für alle]{8} [Menschen]{9};",
 "TIT.2.12": "[sie erzieht]{1} [uns]{2}, [damit]{3} wir, [indem wir]{4} [der]{5} [Gottlosigkeit]{6} und{7} [den]{8} [weltlichen]{9} [Begierden]{10} [absagen]{4}, [besonnen]{11} und{12} [gerecht]{13} und{14} [fromm]{15} [leben]{16} [in]{17} [der]{18} [jetzigen]{19} [Zeit]{20}",
 "TIT.2.13": "[und erwarten]{1} [die]{2} [selige]{3} [Hoffnung]{4} und{5} [das Erscheinen]{6} [der]{7} [Herrlichkeit]{8} [unseres]{14} [grossen]{9,10} [Gottes]{11} und{12} [Retters]{13} [Jesus]{15} [Christus]{16},",
 "TIT.2.14": "[der]{1} [sich selbst]{3} [für]{4} [uns]{5} [hingegeben hat]{2}, [um]{6} [uns]{8} [loszukaufen]{7} [von]{9} [aller]{10} [Gesetzlosigkeit]{11} und{12} [sich]{14} [ein Volk]{15} [zum Eigentum]{16} [zu reinigen]{13}, [eifrig]{17} [in guten]{18} [Werken]{19}.",
 "TIT.2.15": "[Das]{1} [sage]{2} und{3} [ermahne]{4} und{5} [weise zurecht]{6} [mit]{7} [aller]{8} [Vollmacht]{9}. [Niemand]{10} [soll]{12} [dich]{11} [geringschätzen]{12}.",
 # ------------------------------------------------------------ Kapitel 3
 "TIT.3.1": "[Erinnere]{1} [sie]{2} daran, sich [den Regierenden]{3} und [Behörden]{4} [unterzuordnen]{5}, [gehorsam zu sein]{6}, [zu]{7} [jedem]{8} [guten]{10} [Werk]{9} [bereit]{11} [zu sein]{12},",
 "TIT.3.2": "[niemanden]{1} [zu verleumden]{2}, [nicht streitsüchtig]{3} [zu sein]{4}, [freundlich]{5}, [volle]{6} [Sanftmut]{8} [zu zeigen]{7} [gegenüber]{9} [allen]{10} [Menschen]{11}.",
 "TIT.3.3": "Denn{2} [auch]{4} [wir]{5} [waren]{1} [einst]{3} [unverständig]{6}, [ungehorsam]{7}, [irregeführt]{8}, [Sklaven]{9} [vielfältiger]{13} [Begierden]{10} und{11} [Lüste]{12}; [wir lebten]{18} [in]{14} [Bosheit]{15} und{16} [Neid]{17}, [verhasst]{19}, und [hassten]{20} [einander]{21}.",
 "TIT.3.4": "[Als]{1} [aber]{2} [die]{3} [Güte]{4} und{5} [die]{6} [Menschenfreundlichkeit]{7} [Gottes]{12}, [unseres]{11} [Retters]{9,10}, [erschien]{8},",
 "TIT.3.5": "[nicht]{1} [aufgrund von]{2} [Werken]{3}, [die]{4,7} [wir]{9} [in]{5} [Gerechtigkeit]{6} [getan hätten]{8}, [sondern]{10} [nach]{11} [seinem]{12,13} [Erbarmen]{14} [hat er]{15} [uns]{16} [gerettet]{15} [durch]{17} [das Bad]{18} [der Wiedergeburt]{19} und{20} [der Erneuerung]{21} [des heiligen Geistes]{22,23},",
 "TIT.3.6": "[den]{1} er [über]{3} [uns]{4} [reichlich]{5} [ausgegossen hat]{2} [durch]{6} [Jesus]{7} [Christus]{8}, [unseren]{11} [Retter]{9,10},",
 "TIT.3.7": "[damit]{1} wir, [gerecht gemacht]{2} [durch]{3} [seine]{4} [Gnade]{5}, [Erben]{6} [werden]{7} [gemäss]{8} [der Hoffnung]{9} [auf ewiges]{11} [Leben]{10}.",
 "TIT.3.8": "[Zuverlässig]{1} ist [das]{2} [Wort]{3}. Und{4} [ich will]{7}, [dass du]{8} [in diesen Dingen]{5,6} [fest auftrittst]{9}, [damit]{10} [die]{15}, die [zum Glauben an]{16} [Gott]{17} [gekommen sind]{16}, [darauf bedacht sind]{11}, [sich]{14} [für gute]{12} [Werke]{13} [einzusetzen]{14}. [Das]{18} [ist]{19} [gut]{20} und{21} [nützlich]{22} [für die]{23} [Menschen]{24}.",
 "TIT.3.9": "[Törichte]{1} [Streitfragen]{3} [aber]{2} und{4} [Geschlechtsregister]{5} und{6} [Zank]{7} und{8} [Streit]{9} [um das Gesetz]{10} [meide]{11}; [denn]{13} [sie sind]{12} [nutzlos]{14} und{15} [leer]{16}.",
 "TIT.3.10": "[Einen Menschen]{2}, [der Spaltungen verursacht]{1}, [weise]{8} [nach]{3} [einer ersten]{4} und{5} [zweiten]{6} [Ermahnung]{7} [ab]{8},",
 "TIT.3.11": "[da du weisst]{1}, [dass]{2} [ein solcher]{4,5} [verdreht ist]{3} und{6} [sündigt]{7}; [er hat sich selbst das Urteil gesprochen]{8,9}.",
 "TIT.3.12": "[Wenn]{1} [ich]{2} [Artemas]{3} [zu]{4} [dir]{5} [schicke]{2} [oder]{6} [Tychikus]{7}, [beeile dich]{8}, [zu]{10} [mir]{11} [nach]{12} [Nikopolis]{13} [zu kommen]{9}; [denn]{15} [ich habe beschlossen]{16}, [dort]{14} [den Winter zu verbringen]{17}.",
 "TIT.3.13": "[Zenas]{1}, [den]{2} [Rechtsgelehrten]{3}, und{4} [Apollos]{5} [rüste]{7} [sorgfältig]{6} [für die Reise aus]{7}, [damit]{8} [ihnen]{10} [nichts]{9} [fehlt]{11}.",
 "TIT.3.14": "[Auch]{3} [die Unseren]{4,5} [aber]{2} [sollen lernen]{1}, [sich]{8} [für gute]{6} [Werke]{7} [einzusetzen]{8}, [für]{9} [die]{10} [dringenden]{11} [Bedürfnisse]{12}, [damit]{13} [sie]{15} [nicht]{14} [ohne Frucht]{16} [sind]{15}.",
 "TIT.3.15": "[Es grüssen]{1} [dich]{2} [alle]{6}, [die]{3} [bei]{4} [mir]{5} sind. [Grüsse]{7} [die, die]{8} [uns]{10} [im]{11} [Glauben]{12} [lieben]{9}. [Die]{13} [Gnade]{14} sei [mit]{15} [euch]{17} [allen]{16}.",
}

GSW = {
 "TIT.1.1": "Paulus{1}, Chnächt{2} vo Gott{3} und{5} Apostel{4} vo Jesus{6} Christus{7}, [für]{8} [de Glaube]{9} [vo de Uuserwählte]{10} vo Gott{11} und{12} für [d Erchänntnis]{13} [vo de Wahrheit]{14}, wo{15} [de Frömmigkeit]{17} [entspricht]{16},",
 "TIT.1.2": "[i]{1} [de Hoffnig]{2} uf [ewigs]{4} Läbe{3}, [wo]{5} [de]{7} Gott{9}, [wo nöd lügt]{8}, [vor]{10} [ewige]{12} Ziite{11} [versproche hät]{6};",
 "TIT.1.3": "[Zu sinere Ziit]{3,4} aber{2} [hät er]{1} [sis]{7} [Wort]{5,6} [offebaret]{1} [i de Verchündigung]{8,9}, [wo]{10} [mir]{12} [aavertrout worde isch]{11}, [nach]{13} [em Uftrag]{14} vo Gott{18}, [öisem]{17} [Retter]{15,16}.",
 "TIT.1.4": "Am Titus{1}, mim [ächte]{2} Chind{3} [im]{4} [gmeinsame]{5} Glaube{6}: Gnad{7} und{8} Fride{9} [vo]{10} Gott{11}, [em Vatter]{12}, und{13} [vo Christus Jesus]{14,15}, [öisem]{18} [Retter]{16,17}.",
 "TIT.1.5": "[Wäge däm]{1,2} [han ich]{3} dich{4} [z]{5} Kreta{6} [zrugglaa]{3}, [demit]{7} du [das]{8}, [wo no fäält]{9}, [in Ornig bringsch]{10} und{11} [i jeder]{13} Stadt{14} [Ältischte]{15} [iisetzisch]{12}, [wie]{16} ich{17} [dir]{18} [s ufträit han]{19}:",
 "TIT.1.6": "[wänn]{1} [öpper]{2} [untadelig]{4} [isch]{3}, [de Maa]{7} [vo nu eire Frau]{5,6}, [wo gläubigi]{10} Chind{8} [hät]{9}, [wo nöd]{11} [im Ruef]{12,13} [vo me liederliche Läbe]{14} stönd [oder]{15} [widerspänstig]{16} sind.",
 "TIT.1.7": "Dänn{2} [de]{3} Ufseher{4} [mues]{1} [als]{7} Verwalter{9} vo Gott{8} untadelig{5} sii{6}: nöd{10} [eigemächtig]{11}, nöd{12} [jähzornig]{13}, [kein]{14} [Süffel]{15}, [kein]{16} [Schleger]{17}, nöd{18} [uf schändliche Gwünn uus]{19},",
 "TIT.1.8": "sondern{1} [gaschtfründlich]{2}, [em Guete zueta]{3}, [bsunne]{4}, [grächt]{5}, [fromm]{6}, [beherrscht]{7};",
 "TIT.1.9": "eine, wo sich [as]{2} [zueverlässige]{6} Wort{7} [haltet]{1}, wo [de]{4} Lehr{5} [entspricht]{3}, [demit]{8} er [fähig]{9} [isch]{10}, [sowohl]{11} [mit]{13} [de]{14} [gsunde]{16,17} Lehr{15} [z ermaane]{12} [als au]{18} [die]{19}, [wo widerspräched]{20}, [zrächtzwiise]{21}.",
 "TIT.1.10": "Dänn{2} [es git]{1} [vili]{3} [Widerspänstigi]{5}, [Schwätzer]{6} und{7} [Verfüerer]{8}, [vor allem]{9} [die]{10} [us]{11} [de]{12} [Beschniidig]{13}. ~4(καί verbindet «vili» und «Widerspänstigi»; fäält i es paar Usgabe; nöd eigens widergää)",
 "TIT.1.11": "[Dene]{1} [mues]{2} me [s Muul stopfe]{3:idiom}, [dänn si]{4} [bringed]{7} [ganzi]{5} [Familie]{6} [durenand]{7}, [wil si lehred]{8}, [was]{9} [nöd]{10} [sii dörf]{11}, [wäge]{14} [schändlichem]{12} [Gwünn]{13}.",
 "TIT.1.12": "[Eine]{2} [vo]{3} [ine]{4}, [ire]{6} [eige]{5} [Prophet]{7}, [hät gseit]{1}: «Kreter{8} sind [immer]{9} [Lugner]{10}, [bösi]{11} [Tier]{12}, [fuuli]{14} [Büüch]{13}.»",
 "TIT.1.13": "[Das]{3} [Zügnis]{1,2} [isch]{4} [wahr]{5}. [Us]{6} [dem]{7} [Grund]{8} [wiis]{9} [si]{10} [schaarf]{11} [zrächt]{9}, [demit]{12} [si gsund]{13} [im]{14,15} [Glaube]{16} [sind]{13}",
 "TIT.1.14": "und [nöd]{1} [uf]{2} [jüdischi]{3} [Mythe]{4} [lose]{2} [und]{5} [uf Gebot]{6} [vo Mänsche]{7}, [wo sich]{8} [vo de]{9} [Wahrheit]{10} [abwänded]{8}.",
 "TIT.1.15": "[Alles]{1} isch [rein]{2} [für die]{3} [Reine]{4}; [für die]{5} [Befleckte]{7} [aber]{6} und{8} [Unglöubige]{9} isch [nüt]{10} [rein]{11}, [sondern]{12} [befleckt sind]{13} [sowohl]{15} [ire]{14} [Verstand]{16,17} [als au]{18} [ires Gwüsse]{19,20}.",
 "TIT.1.16": "Si [säged]{2}, si [kännted]{3} Gott{1}, [mit de]{4} [Wärch]{6} [aber]{5} [verleugned si en]{7}; [abschüülich]{8} [sind si]{9} und{10} [unghorsam]{11} und{12} [für]{13} [jedes]{14} [guete]{16} [Wärch]{15} [unbruuchbar]{17}.",
 "TIT.2.1": "[Du]{1} [aber]{2} [säg]{3}, [was]{4} [de]{6} [gsunde]{7} [Lehr]{8} [entspricht]{5}.",
 "TIT.2.2": "[Älteri Mane]{1} [söled]{3} [nüechter]{2} [sii]{3}, [würdig]{4}, [bsunne]{5}, [gsund]{6} [im]{7} [Glaube]{8}, [i de]{9} [Liebi]{10}, [i de]{11} [Uusduur]{12}.",
 "TIT.2.3": "[Älteri Fraue]{1} [gliich]{2}: [i]{3} [irem Verhalte]{4} [ehrwürdig]{5}, [nöd]{6} [verlüümderisch]{7}, [nöd]{8} [em viele]{10} [Wii]{9} [verfalle]{11}, [Lehrerinne vom Guete]{12},",
 "TIT.2.4": "[demit]{1} si [di]{3} [junge Fraue]{4} [aaleited]{2}, [iri Mane]{5} und [Chind]{7} [gern z haa]{6},",
 "TIT.2.5": "[bsunne]{1} z sii, [rein]{2}, [im Huus tätig]{3}, [güetig]{4}, [irne]{6} [eigete]{7} [Mane]{8} [underornet]{5}, [demit]{9} [s]{11} [Wort]{12} [vo Gott]{13,14} [nöd]{10} [in Verruef chunnt]{15}.",
 "TIT.2.6": "[Di]{1} [jüngere Mane]{2} [ermaan]{4} [gliich]{3}, [bsunne z sii]{5}",
 "TIT.2.7": "[i]{1} [allem]{2}. [Zeig]{4} [dich sälber]{3} [als]{4} [Vorbild]{5} [für gueti]{6} [Wärch]{7}, [i]{8} [de]{9} [Lehr]{10} [Unverfälschtheit]{11}, [Würde]{12},",
 "TIT.2.8": "[gsundi]{2}, [unaafechtbari]{3} [Red]{1}, [demit]{4} [de]{5} [Gägner]{6,7} [sich schämt]{8}, [wil er]{10} [nüt]{9} [Schlächts]{14} [über]{12} [üs]{13} [z säge]{11} [hät]{10}.",
 "TIT.2.9": "[Sklave]{1} söled sich [irne]{2} [Herre]{3} [i]{5} [allem]{6} [underordne]{4}, [ine gfellig]{7} [sii]{8}, [nöd]{9} [widerspräche]{10},",
 "TIT.2.10": "[nüt]{1} [veruntreue]{2}, [sondern]{3} [volli]{4}, [gueti]{7} [Tröii]{5} [bewiise]{6}, [demit]{8} si [d]{9,11} [Lehr]{10} [vo Gott]{15}, [öisem]{14} [Retter]{12,13}, [i]{17} [allem]{18} [schmücked]{16}.",
 "TIT.2.11": "Dänn{2} [erschine isch]{1} [d]{3} [Gnad]{4} [vo Gott]{5,6}, [wo]{7} [allne]{8} [Mänsche]{9} [Rettig bringt]{7};",
 "TIT.2.12": "[si erziet]{1} [üs]{2}, [demit]{3} mir, [indem mir]{4} [de]{5} [Gottlosigkeit]{6} und{7} [de]{8} [wältliche]{9} [Glüscht]{10} [absäged]{4}, [bsunne]{11} und{12} [grächt]{13} und{14} [fromm]{15} [läbed]{16} [i]{17} [de]{18} [jetzige]{19} [Ziit]{20}",
 "TIT.2.13": "[und erwarted]{1} [di]{2} [sälige]{3} [Hoffnig]{4} und{5} [s Erschiine]{6} [vo de]{7} [Herrlichkeit]{8} [vo öisem]{14} [groosse]{9,10} [Gott]{11} und{12} [Retter]{13} [Jesus]{15} [Christus]{16},",
 "TIT.2.14": "[wo]{1} [sich sälber]{3} [für]{4} [üs]{5} [häregää hät]{2}, [zum]{6} [üs]{8} [loszchaufe]{7} [vo]{9} [allere]{10} [Gsetzlosigkeit]{11} und{12} [sich]{14} [es Volk]{15} [als Eigetum]{16} [z reinige]{13}, [iifrig]{17} [für gueti]{18} [Wärch]{19}.",
 "TIT.2.15": "[Das]{1} [säg]{2} und{3} [ermaan]{4} und{5} [wiis zrächt]{6} [mit]{7} [voller]{8} [Vollmacht]{9}. [Niemer]{10} [söll]{12} [dich]{11} [gringschätze]{12}.",
 "TIT.3.1": "[Erinner]{1} [si]{2} dra, sich [de Regierende]{3} und [Behörde]{4} [underzordne]{5}, [ghorsam z sii]{6}, [für]{7} [jedes]{8} [guete]{10} [Wärch]{9} [parat]{11} [z sii]{12},",
 "TIT.3.2": "[niemer]{1} [z verlüümde]{2}, [nöd strittig]{3} [z sii]{4}, [fründlich]{5}, [volli]{6} [Sanftmuet]{8} [z zeige]{7} [gägenüber]{9} [allne]{10} [Mänsche]{11}.",
 "TIT.3.3": "Dänn{2} [au]{4} [mir]{5} [sind]{1} [früener]{3} [unverständig]{6}, [unghorsam]{7}, [verirrt]{8}, [Sklave]{9} [vo allerlei]{13} [Glüscht]{10} und{11} [Vergnüege]{12} [gsii]{1}; [mir händ]{18} [i]{14} [Bosheit]{15} und{16} [Niid]{17} [gläbt]{18}, [verhasst]{19}, und [händ]{20} [enand]{21} [ghasst]{20}.",
 "TIT.3.4": "[Wo]{1} [aber]{2} [d]{3} [Güeti]{4} und{5} [d]{6} [Mänschefründlichkeit]{7} [vo Gott]{12}, [öisem]{11} [Retter]{9,10}, [erschine isch]{8},",
 "TIT.3.5": "[nöd]{1} [wäge]{2} [Wärch]{3}, [wo]{4,7} [mir]{9} [i]{5} [Grächtigkeit]{6} [taa hettet]{8}, [sondern]{10} [nach]{11} [sim]{12,13} [Erbarme]{14} [hät er]{15} [üs]{16} [grettet]{15} [dur]{17} [s Bad]{18} [vo de Widergeburt]{19} und{20} [vo de Erneuerig]{21} [vom heilige Geischt]{22,23},",
 "TIT.3.6": "[wo]{1} er [über]{3} [üs]{4} [riichlich]{5} [usgosse hät]{2} [dur]{6} [Jesus]{7} [Christus]{8}, [öise]{11} [Retter]{9,10},",
 "TIT.3.7": "[demit]{1} mir, [grächt gmacht]{2} [dur]{3} [sini]{4} [Gnad]{5}, [Erbe]{6} [wärded]{7} [gemäss]{8} [de Hoffnig]{9} [uf ewigs]{11} [Läbe]{10}.",
 "TIT.3.8": "[Zueverlässig]{1} isch [s]{2} [Wort]{3}. Und{4} [ich wott]{7}, [dass du]{8} [i dene Sache]{5,6} [fescht uftrittsch]{9}, [demit]{10} [die]{15}, [wo zum Glaube a]{16} [Gott]{17} [cho sind]{16}, [druf achted]{11}, [sich]{14} [für gueti]{12} [Wärch]{13} [iizsetze]{14}. [Das]{18} [isch]{19} [guet]{20} und{21} [nützlich]{22} [für d]{23} [Mänsche]{24}.",
 "TIT.3.9": "[Törichti]{1} [Striitfrage]{3} [aber]{2} und{4} [Stammbäum]{5} und{6} [Zank]{7} und{8} [Striit]{9} [ums Gsetz]{10} [meid]{11}; [dänn]{13} [si sind]{12} [nutzlos]{14} und{15} [läär]{16}.",
 "TIT.3.10": "[En Mänsch]{2}, [wo Spaltige verursachet]{1}, [wiis]{8} [nach]{3} [ere erschte]{4} und{5} [zweite]{6} [Ermaanig]{7} [ab]{8},",
 "TIT.3.11": "[wil du weisch]{1}, [dass]{2} [so eine]{4,5} [verdrait isch]{3} und{6} [sündiget]{7}; [er hät sich sälber s Urteil gsproche]{8,9}.",
 "TIT.3.12": "[Wänn]{1} [ich]{2} [de Artemas]{3} [zu]{4} [dir]{5} [schicke]{2} [oder]{6} [de Tychikus]{7}, [mach vorwärts]{8}, [zu]{10} [mir]{11} [uf]{12} [Nikopolis]{13} [z cho]{9}; [dänn]{15} [ich ha beschlosse]{16}, [dört]{14} [de Winter z verbringe]{17}.",
 "TIT.3.13": "[De Zenas]{1}, [de]{2} [Rächtsglehrt]{3}, und{4} [de Apollos]{5} [rüscht]{7} [sorgfältig]{6} [für d Reis us]{7}, [demit]{8} [ine]{10} [nüt]{9} [fäält]{11}.",
 "TIT.3.14": "[Au]{3} [di Öise]{4,5} [aber]{2} [söled lerne]{1}, [sich]{8} [für gueti]{6} [Wärch]{7} [iizsetze]{8}, [für]{9} [di]{10} [dringende]{11} [Bedürfnis]{12}, [demit]{13} [si]{15} [nöd]{14} [ohni Frucht]{16} [sind]{15}.",
 "TIT.3.15": "[Es grüessed]{1} [dich]{2} [alli]{6}, [wo]{3} [bi]{4} [mir]{5} sind. [Grüess]{7} [die, wo]{8} [üs]{10} [im]{11} [Glaube]{12} [gern händ]{9}. [D]{13} [Gnad]{14} sig [mit]{15} [eu]{17} [allne]{16}.",
}

# Übersetzungsentscheidungen: (Stelle, Zieltext, Art, griechisch, wörtlicher, andere Möglichkeiten, Begründung)
DEC_DE = [
 ("TIT.1.1", "Knecht", "traditional", "δοῦλος", "Sklave", ["Diener"], "δοῦλος heisst wörtlich «Sklave». Als Selbstbezeichnung (wie «Knecht Gottes» bei Mose und den Propheten) meint es jemanden, der ganz Gott gehört; «Knecht» folgt der vertrauten Wiedergabe."),
 ("TIT.1.1", "Frömmigkeit", "literal", "εὐσέβειαν", None, ["Gottesfurcht", "gelebter Glaube", "Gottseligkeit"], "εὐσέβεια ist Ehrfurcht vor Gott, die sich im Leben zeigt; ein Leitwort der Briefe an Timotheus und Titus."),
 ("TIT.1.1", "für den Glauben", "interpretive", "κατὰ πίστιν", "gemäss dem Glauben", ["um des Glaubens willen"], "κατά kann den Massstab («gemäss») oder das Ziel («für, um … willen») angeben; hier ist der Dienst am Glauben der Auserwählten gemeint."),
 ("TIT.1.3", "Zu seiner Zeit", "interpretive", "καιροῖς ἰδίοις", "zu eigenen Zeiten", ["zur rechten Zeit", "zu der von ihm bestimmten Zeit"], "Der Dativ Plural meint die von Gott festgesetzte Zeit."),
 ("TIT.1.5", "Älteste", "literal", "πρεσβυτέρους", None, ["Presbyter"], "Die Ältesten leiteten die Gemeinden. In [[TIT.1.7]] heisst derselbe Kreis offenbar «Aufseher»."),
 ("TIT.1.6", "Mann einer einzigen Frau", "literal", "μιᾶς γυναικὸς ἀνήρ", None, ["einer Frau treu", "nur einmal verheiratet"], "Die Bedeutung ist umstritten: Treue in der Ehe, keine zweite Ehe nach Scheidung oder Tod oder keine Vielehe."),
 ("TIT.1.6", "gläubige", "interpretive", "πιστά", None, ["zuverlässige", "treue"], "πιστός heisst «gläubig» oder «zuverlässig». Ob die Kinder selbst Christen sein sollen oder ob ihr Verhalten gemeint ist, bleibt offen."),
 ("TIT.1.7", "Aufseher", "literal", "ἐπίσκοπον", None, ["Bischof", "Gemeindeleiter"], "Aus ἐπίσκοπος entstand das Wort «Bischof». Ein Bischofsamt im späteren Sinn ist hier noch nicht vorausgesetzt; der Abschnitt wechselt von «Älteste» zu «Aufseher»."),
 ("TIT.1.11", "Familien", "interpretive", "οἴκους", "Häuser", ["Hausgemeinschaften"], "Gemeint sind Haushalte; in ihnen versammelten sich auch die Gemeinden."),
 ("TIT.1.12", "Prophet", "literal", "προφήτης", None, ["Dichter", "Seher"], "Gemeint ist ein Dichter aus Kreta; die alte Überlieferung nennt Epimenides. «Prophet» im Sinn von Seher und Dichter."),
 ("TIT.1.14", "jüdische", "literal", "Ἰουδαϊκοῖς μύθοις", None, None, "Was diese «jüdischen Mythen» genau waren, ist unbekannt; vermutlich Spekulationen über Abstammung und Gesetz (vgl. [[TIT.3.9]])."),
 ("TIT.2.5", "untergeordnet", "literal", "ὑποτασσομένας", None, ["sich einfügen"], "Teil einer Haustafel, die die damalige Ordnung des Hauses voraussetzt; begründet wird sie mit dem Ruf der Gemeinde nach aussen."),
 ("TIT.2.9", "Sklaven", "literal", "Δούλους", None, ["Knechte"], "δοῦλοι sind Unfreie, nicht Angestellte; «Knechte» würde das verdecken."),
 ("TIT.2.10", "Treue", "interpretive", "πίστιν", "Glauben", ["Zuverlässigkeit"], "πίστις heisst hier im Zusammenhang mit «unterschlagen» am ehesten Treue und Zuverlässigkeit."),
 ("TIT.2.13", "unseres grossen Gottes und Retters Jesus Christus", "interpretive", "μεγάλου θεοῦ καὶ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ", None, ["des grossen Gottes und unseres Retters Jesus Christus"], "Ein Artikel für «Gott» und «Retter» spricht dafür, dass beide Titel Jesus Christus meinen; andere lesen zwei Personen. Die Entscheidung ist theologisch bedeutsam und umstritten."),
 ("TIT.3.5", "das Bad", "literal", "λουτροῦ", None, ["die Waschung"], "λουτρόν ist ein Bad bzw. eine Waschung; viele Ausleger beziehen «Bad der Wiedergeburt» auf die Taufe."),
 ("TIT.3.8", "sich für gute", "interpretive", "καλῶν ἔργων προΐστασθαι", "guten Werken vorzustehen", ["sich in guten Werken hervorzutun", "einen ehrbaren Beruf auszuüben"], "προΐστασθαι heisst «vorstehen, sich bemühen um»; manche denken an ehrbare Berufe."),
 ("TIT.3.10", "der Spaltungen verursacht", "interpretive", "αἱρετικὸν", None, ["Ketzer", "Sektierer"], "αἱρετικός meint hier jemanden, der Parteiungen bildet. «Ketzer» trägt die spätere Bedeutung von Irrlehre ein."),
 ("TIT.3.13", "Rechtsgelehrten", "interpretive", "νομικὸν", None, ["Juristen", "Gesetzeslehrer"], "Ob Zenas ein jüdischer Gesetzeskundiger oder ein römischer Jurist war, ist offen."),
]
DEC_GSW = [
 ("TIT.1.1", "Chnächt", "traditional", "δοῦλος", "Sklav", ["Diener"], "δοῦλος heisst wörtlich «Sklav». Als Bezeichnig für sich sälber (wie «Chnächt vo Gott» bim Mose und de Prophete) meint s öpper, wo ganz Gott ghört; «Chnächt» folgt de vertroute Widergab."),
 ("TIT.1.1", "Frömmigkeit", "literal", "εὐσέβειαν", None, ["Gottesfurcht", "gläbte Glaube"], "εὐσέβεια isch Ehrfurcht vor Gott, wo sich im Läbe zeigt; es Leitwort vo de Brief a Timotheus und Titus."),
 ("TIT.1.1", "für de Glaube", "interpretive", "κατὰ πίστιν", "gemäss em Glaube", ["wäge em Glaube"], "κατά cha de Massstab («gemäss») oder s Ziil («für, wäge») aagää; da isch de Dienscht am Glaube vo de Uuserwählte gmeint."),
 ("TIT.1.3", "Zu sinere Ziit", "interpretive", "καιροῖς ἰδίοις", "zu eigete Ziite", ["zur rächte Ziit"], "Gmeint isch d Ziit, wo Gott feschtgleit hät."),
 ("TIT.1.5", "Ältischte", "literal", "πρεσβυτέρους", None, ["Presbyter"], "D Ältischte händ d Gmeinde gleitet. I [[TIT.1.7]] heisst de gliich Chreis offebar «Ufseher»."),
 ("TIT.1.6", "Maa vo nu eire Frau", "literal", "μιᾶς γυναικὸς ἀνήρ", None, ["einere Frau tröi", "nu eimal ghürate"], "D Bedüütig isch umstritte: Tröii i de Ee, kei zweiti Ee nach Scheidig oder Tod oder kei Vilee."),
 ("TIT.1.6", "gläubigi", "interpretive", "πιστά", None, ["zueverlässigi", "tröii"], "πιστός heisst «gläubig» oder «zueverlässig». Öb d Chind sälber Christe söled sii oder öb ires Verhalte gmeint isch, bliibt offe."),
 ("TIT.1.7", "Ufseher", "literal", "ἐπίσκοπον", None, ["Bischof", "Gmeindleiter"], "Us ἐπίσκοπος isch s Wort «Bischof» worde. Es Bischofsamt im spööttere Sinn isch da no nöd voruusgsetzt."),
 ("TIT.1.11", "Familie", "interpretive", "οἴκους", "Hüüser", ["Huusgmeinschafte"], "Gmeint sind Hushaltige; i ine händ sich au d Gmeinde versammlet."),
 ("TIT.1.12", "Prophet", "literal", "προφήτης", None, ["Dichter", "Seher"], "Gmeint isch en Dichter us Kreta; di alt Überlieferig nännt de Epimenides."),
 ("TIT.1.14", "jüdischi", "literal", "Ἰουδαϊκοῖς μύθοις", None, None, "Was die «jüdische Mythe» gnau gsii sind, weiss me nöd; wahrschiinli Spekulatione über Abstammig und Gsetz (vgl. [[TIT.3.9]])."),
 ("TIT.2.5", "underornet", "literal", "ὑποτασσομένας", None, ["sich iifüege"], "Teil vo ere Huustafle, wo di damalig Ornig vom Huus voruussetzt; begründet wird si mit em Ruef vo de Gmeind gäge usse."),
 ("TIT.2.9", "Sklave", "literal", "Δούλους", None, ["Chnächt"], "δοῦλοι sind Unfreii, nöd Aagstellti; «Chnächt» würd das zuedecke."),
 ("TIT.2.10", "Tröii", "interpretive", "πίστιν", "Glaube", ["Zueverlässigkeit"], "πίστις heisst da im Zämehang mit «veruntreue» am ehnder Tröii und Zueverlässigkeit."),
 ("TIT.2.13", "vo öisem groosse Gott und Retter Jesus Christus", "interpretive", "μεγάλου θεοῦ καὶ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ", None, ["vom groosse Gott und vo öisem Retter Jesus Christus"], "Ein Artikel für «Gott» und «Retter» redt defür, dass beidi Titel de Jesus Christus meined; anderi läsed zwei Persone. D Entscheidig isch theologisch wichtig und umstritte."),
 ("TIT.3.5", "s Bad", "literal", "λουτροῦ", None, ["d Wäschig"], "λουτρόν isch es Bad oder e Wäschig; vili Usleger bezieend «Bad vo de Widergeburt» uf d Toufi."),
 ("TIT.3.8", "für gueti", "interpretive", "καλῶν ἔργων προΐστασθαι", "guete Wärch vorzstaa", ["en ehrbare Bruef uusüebe"], "προΐστασθαι heisst «vorstaa, sich bemüe um»; es paar dänked a ehrbari Brüef."),
 ("TIT.3.10", "wo Spaltige verursachet", "interpretive", "αἱρετικὸν", None, ["Ketzer", "Sektierer"], "αἱρετικός meint da öpper, wo Parteie bildet. «Ketzer» treit di spööter Bedüütig vo Irrlehr ii."),
 ("TIT.3.13", "Rächtsglehrt", "interpretive", "νομικὸν", None, ["Jurischt", "Gsetzeslehrer"], "Öb de Zenas en jüdische Gsetzeskundige oder en römische Jurischt gsii isch, isch offe."),
]

# Lesarten, die die Übersetzung verändern: (Lesart, Stelle, de von, de zu, gsw von, gsw zu, Wirkung, Hinweis de, Hinweis gsw,
#  Wörter {Lesart: [(griechisch, de, Hinweis)]}, Wörter gsw, Entstehung de, Entstehung gsw)
ALTS = [
 ("VAR-SBLGNTAPP-TIT-001-004-01:R2", "TIT.1.4", "Gnade und Friede", "Gnade, Barmherzigkeit und Friede", "Gnad und Fride", "Gnad, Barmhärzigkeit und Fride", "gering",
  "Die dreigliedrige Formel steht so auch in [[1TI.1.2]] und [[2TI.1.2]].", "Di drüüteilig Formle staat so au i [[1TI.1.2]] und [[2TI.1.2]].",
  {"R1": [("χάρις καὶ εἰρήνη", "Gnade und Friede", "zweigliedrig")], "R2": [("χάρις ἔλεος εἰρήνη", "Gnade, Barmherzigkeit, Friede", "dreigliedrig")]},
  {"R1": [("χάρις καὶ εἰρήνη", "Gnad und Fride", "zweiteilig")], "R2": [("χάρις ἔλεος εἰρήνη", "Gnad, Barmhärzigkeit, Fride", "drüüteilig")]},
  ["Abschreiber kannten die dreigliedrige Formel aus den Briefen an Timotheus und konnten den Titusbrief daran angleichen.", "Laut der automatischen Zuordnung hat der Codex Alexandrinus (5. Jh.) die dreigliedrige Formel, Sinaiticus und Ephraemi die zweigliedrige."],
  ["Abschriiber händ di drüüteilig Formle us de Brief a Timotheus kännt und händ de Titusbrief dra chöne aagliiche.", "Nach de automatische Zueornig hät de Codex Alexandrinus (5. Jh.) di drüüteilig Formle, de Sinaiticus und de Ephraemi di zweiteilig."]),
 ("VAR-SBLGNTAPP-TIT-001-004-02:R2", "TIT.1.4", "von Christus Jesus", "vom Herrn Jesus Christus", "vo Christus Jesus", "vom Herr Jesus Christus", "gering",
  "Gleicher Bezug auf Jesus, mit dem Titel «Herr».", "Di gliich Person, mit em Titel «Herr».",
  {"R1": [("Χριστοῦ Ἰησοῦ", "Christus Jesus", "ohne «Herr»")], "R2": [("κυρίου Ἰησοῦ χριστοῦ", "des Herrn Jesus Christus", "mit «Herr»")]},
  {"R1": [("Χριστοῦ Ἰησοῦ", "Christus Jesus", "ohni «Herr»")], "R2": [("κυρίου Ἰησοῦ χριστοῦ", "vom Herr Jesus Christus", "mit «Herr»")]},
  ["Die Wendung «Herr Jesus Christus» war in Gottesdienst und Briefen sehr geläufig und konnte beim Abschreiben die seltenere Form verdrängen."],
  ["D Wändig «Herr Jesus Christus» isch im Gottesdienscht und i Brief seer gläufig gsii und hät bim Abschriibe di sälteneri Form chöne verdränge."]),
 ("VAR-SBLGNTAPP-TIT-002-005-01:R2", "TIT.2.5", "häuslich tätig", "zu Hause bleibend", "im Huus tätig", "deheim bliibend", "gering",
  "Die Wörter unterscheiden sich um einen Buchstaben.", "D Wörter underscheided sich um ein Buechstabe.",
  {"R1": [("οἰκουργούς", "im Haus tätig", "seltenes Wort")], "R2": [("οἰκουρούς", "das Haus hütend", "geläufigeres Wort")]},
  {"R1": [("οἰκουργούς", "im Huus tätig", "sälts Wort")], "R2": [("οἰκουρούς", "s Huus hüetend", "gläufigers Wort")]},
  ["Das seltene οἰκουργός kann beim Abschreiben durch das bekanntere οἰκουρός ersetzt worden sein; umgekehrt kann ein Buchstabe dazugekommen sein."],
  ["S sälte οἰκουργός cha bim Abschriibe dur s bekanntere οἰκουρός ersetzt worde sii; umgekeert cha en Buechstabe dezuecho sii."]),
 ("VAR-SBLGNTAPP-TIT-002-007-02:R2", "TIT.2.7", "Würde", "Würde, Unvergänglichkeit", "Würde", "Würde, Unvergänglichkeit", "gering",
  "Zusatz eines weiteren Begriffs.", "Zuesatz vo me wiitere Begriff.",
  {"R1": [("σεμνότητα", "Würde", "ohne Zusatz")], "R2": [("σεμνότητα ἀφθαρσίαν", "Würde, Unvergänglichkeit", "mit Zusatz")]},
  {"R1": [("σεμνότητα", "Würde", "ohni Zuesatz")], "R2": [("σεμνότητα ἀφθαρσίαν", "Würde, Unvergänglichkeit", "mit Zuesatz")]},
  ["ἀφθαρσία klingt ähnlich wie ἀφθορία kurz davor und kann als Erklärung oder Doppelung in den Text gekommen sein.", "Laut der automatischen Zuordnung hat schon 𝔓32 (um 200) wie Sinaiticus, Alexandrinus und Ephraemi die Form ohne Zusatz."],
  ["ἀφθαρσία tönt ähnlich wie ἀφθορία churz vorhär und cha als Erkläärig oder Doppelig in Text cho sii.", "Nach de automatische Zueornig hät scho 𝔓32 (um 200) wie de Sinaiticus, de Alexandrinus und de Ephraemi d Form ohni Zuesatz."]),
 ("VAR-SBLGNTAPP-TIT-002-013-01:R2", "TIT.2.13", "Jesus Christus", "Christus Jesus", "Jesus Christus", "Christus Jesus", "gering",
  "Nur die Reihenfolge ändert sich.", "Nu d Reiefolg änderet.",
  {"R1": [("Ἰησοῦ Χριστοῦ", "Jesus Christus", "")], "R2": [("Χριστοῦ Ἰησοῦ", "Christus Jesus", "")]},
  {"R1": [("Ἰησοῦ Χριστοῦ", "Jesus Christus", "")], "R2": [("Χριστοῦ Ἰησοῦ", "Christus Jesus", "")]},
  ["Beide Reihenfolgen sind in den Briefen geläufig; Abschreiber konnten sie leicht vertauschen."],
  ["Beidi Reiefolge sind i de Brief gläufig; Abschriiber händ si liecht chöne vertuusche."]),
 ("VAR-SBLGNTAPP-TIT-003-008-01:R2", "TIT.3.8", "Das ist gut", "Das ist das Gute", "Das isch guet", "Das isch s Guete", "gering",
  "Mit Artikel wird «gut» zu «das Gute».", "Mit Artikel wird «guet» zu «s Guete».",
  {"R1": [("ἐστιν καλὰ", "ist gut", "ohne Artikel")], "R2": [("ἐστιν τὰ καλὰ", "ist das Gute", "mit Artikel")]},
  {"R1": [("ἐστιν καλὰ", "isch guet", "ohni Artikel")], "R2": [("ἐστιν τὰ καλὰ", "isch s Guete", "mit Artikel")]},
  ["Der Artikel kann zur Verdeutlichung ergänzt worden sein; für den Sinn macht er wenig aus."],
  ["De Artikel cha zur Verdüütlichig ergänzt worde sii; für de Sinn macht er wenig us."]),
 ("VAR-SBLGNTAPP-TIT-003-015-01:R2", "TIT.3.15", "allen.", "allen. Amen.", "allne.", "allne. Amen.", "gering",
  "Liturgischer Schluss.", "Liturgische Schluss.",
  {"R1": [("ὑμῶν", "euch", "ohne Amen")], "R2": [("ὑμῶν ἀμήν", "euch. Amen", "mit Amen")]},
  {"R1": [("ὑμῶν", "eu", "ohni Amen")], "R2": [("ὑμῶν ἀμήν", "eu. Amen", "mit Amen")]},
  ["Briefe wurden im Gottesdienst vorgelesen; ein «Amen» am Schluss lag nahe und wurde vielen Briefen später angefügt."],
  ["Brief sind im Gottesdienscht vorgläse worde; es «Amen» am Schluss isch nooch glege und isch vilne Brief spööter aaghänkt worde."]),
]

UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung)
 ("TU-TIT-001-001-016", "TIT.1.1-TIT.1.16", "section", "Ordnung für die Gemeinden auf Kreta",
  ["TU-TIT-001-001-004", "TU-TIT-001-005-009", "TU-TIT-001-010-016"],
  "Paulus beauftragt Titus, in den Städten Kretas Älteste einzusetzen, die selbst glaubwürdig leben und an der gesunden Lehre festhalten, und gegen Lehrer vorzugehen, die Familien verwirren."),
 ("TU-TIT-001-001-004", "TIT.1.1-TIT.1.4", "greeting", "Gruss: Apostel für den Glauben", None,
  "Ein ungewöhnlich ausführlicher Briefanfang: Paulus beschreibt seinen Auftrag als Dienst am Glauben, an der Erkenntnis der Wahrheit und an der Hoffnung auf ewiges Leben."),
 ("TU-TIT-001-005-009", "TIT.1.5-TIT.1.9", "section", "Wer die Gemeinde leiten soll", None,
  "Älteste bzw. Aufseher sollen untadelig leben, in Ehe und Familie, im Umgang mit Geld, Wein und Macht, und an der verlässlichen Lehre festhalten."),
 ("TU-TIT-001-010-016", "TIT.1.10-TIT.1.16", "section", "Gegen leeres Gerede", None,
  "Lehrer, die aus Gewinnsucht Familien verwirren, sollen zurechtgewiesen werden. Ein kretisches Dichterwort wird zitiert. Entscheidend ist nicht das Bekenntnis, sondern ob die Taten ihm entsprechen."),
 ("TU-TIT-002-001-015", "TIT.2.1-TIT.2.15", "section", "Gesunde Lehre im Alltag", ["TU-TIT-002-001-010", "TU-TIT-002-011-015"],
  "Was der gesunden Lehre entspricht, zeigt sich im Alltag von Alten und Jungen, Frauen und Männern, Sklaven. Begründet wird es mit der Gnade Gottes, die erschienen ist und zu einem neuen Leben erzieht."),
 ("TU-TIT-002-001-010", "TIT.2.1-TIT.2.10", "household_code", "Was zu wem passt", None,
  "Eine Haustafel: Weisungen für ältere Männer und Frauen, junge Frauen und Männer, für Titus selbst und für Sklaven. Mehrfach wird begründet, dass die Gemeinde nach aussen keinen Anstoss geben soll."),
 ("TU-TIT-002-011-015", "TIT.2.11-TIT.2.15", "section", "Die Gnade Gottes ist erschienen", None,
  "Die Gnade Gottes ist für alle Menschen erschienen. Sie erzieht zu einem besonnenen Leben in der Gegenwart, in Erwartung des Erscheinens Jesu Christi, der sich für sein Volk hingegeben hat."),
 ("TU-TIT-003-001-015", "TIT.3.1-TIT.3.15", "section", "Freundlich zu allen, weil Gott freundlich war", ["TU-TIT-003-001-007", "TU-TIT-003-008-011", "TU-TIT-003-012-015"],
  "Die Gemeinde soll sich in die öffentliche Ordnung einfügen und allen Menschen freundlich begegnen, denn sie verdankt ihre Rettung nicht eigenen Werken, sondern Gottes Güte. Fruchtlose Streitfragen soll sie meiden. Der Brief endet mit Reiseplänen und Grüssen."),
 ("TU-TIT-003-001-007", "TIT.3.1-TIT.3.7", "section", "Gottes Güte ist erschienen", None,
  "Weil auch die Glaubenden einmal verirrt waren und Gott sie aus Erbarmen gerettet hat, sollen sie allen Menschen mit Sanftmut begegnen."),
 ("TU-TIT-003-008-011", "TIT.3.8-TIT.3.11", "section", "Was nützt und was nicht", None,
  "Gute Werke nützen den Menschen; Streit um Geschlechtsregister und Gesetz ist leer. Wer Spaltungen verursacht, soll nach zweimaliger Ermahnung gemieden werden."),
 ("TU-TIT-003-012-015", "TIT.3.12-TIT.3.15", "greeting", "Reisepläne und Grüsse", None,
  "Paulus will in Nikopolis überwintern, kündigt Mitarbeiter an, bittet um Hilfe für Zenas und Apollos und grüsst."),
]
UNITS_GSW = {
 "TU-TIT-001-001-016": ("Ornig für d Gmeinde uf Kreta", "De Paulus git em Titus de Uftrag, i de Stedt vo Kreta Ältischti iizsetze, wo sälber glaubwürdig läbed und a de gsunde Lehr fescht haltet, und gäge Lehrer vorzgaa, wo Familie durenand bringed."),
 "TU-TIT-001-001-004": ("Gruess: Apostel für de Glaube", "En ungwöönlich usfüerliche Briefaafang: De Paulus beschriibt sin Uftrag als Dienscht am Glaube, a de Erchänntnis vo de Wahrheit und a de Hoffnig uf ewigs Läbe."),
 "TU-TIT-001-005-009": ("Wär d Gmeind söll leite", "Ältischti oder Ufseher söled untadelig läbe, i de Ee und i de Familie, im Umgang mit Gält, Wii und Macht, und a de verlässliche Lehr fescht halte."),
 "TU-TIT-001-010-016": ("Gäge lääri Schnurrerei", "Lehrer, wo us Gwünnsucht Familie durenand bringed, söled zrächtgwise wärde. Es Dichterwort us Kreta wird zitiert. Entscheidend isch nöd s Bekänntnis, sondern öb d Tate dem entspräched."),
 "TU-TIT-002-001-015": ("Gsundi Lehr im Alltag", "Was de gsunde Lehr entspricht, zeigt sich im Alltag vo Alte und Junge, Fraue und Mane, Sklave. Begründet wird s mit de Gnad vo Gott, wo erschine isch und zu me nöie Läbe erziet."),
 "TU-TIT-002-001-010": ("Was zu wem passt", "E Huustafle: Wiisige für älteri Mane und Fraue, jungi Fraue und Mane, für de Titus sälber und für Sklave. Meermals wird begründet, dass d Gmeind gäge usse kein Aastoss söll gää."),
 "TU-TIT-002-011-015": ("D Gnad vo Gott isch erschine", "D Gnad vo Gott isch für alli Mänsche erschine. Si erziet zu me bsunnene Läbe i de Gägewart, i de Erwartig vom Erschiine vo Jesus Christus, wo sich für sis Volk häregää hät."),
 "TU-TIT-003-001-015": ("Fründlich zu allne, wil Gott fründlich gsii isch", "D Gmeind söll sich i di öffentlich Ornig iifüege und allne Mänsche fründlich begägne, dänn si verdankt iri Rettig nöd eigete Wärch, sondern de Güeti vo Gott. Fruchtlosi Striitfrage söll si meide. De Brief hört mit Reiseplän und Grüess uf."),
 "TU-TIT-003-001-007": ("D Güeti vo Gott isch erschine", "Wil au d Gläubige emal verirrt gsii sind und Gott si us Erbarme grettet hät, söled si allne Mänsche mit Sanftmuet begägne."),
 "TU-TIT-003-008-011": ("Was nützt und was nöd", "Gueti Wärch nützed de Mänsche; Striit um Stammbäum und Gsetz isch läär. Wär Spaltige verursachet, söll nach zweimaliger Ermaanig gmide wärde."),
 "TU-TIT-003-012-015": ("Reiseplän und Grüess", "De Paulus wott z Nikopolis überwintere, chündet Mitarbeiter aa, bittet um Hilf für de Zenas und de Apollos und grüesst."),
}


def run():
    import json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _lib import localize  # noqa: E402
    n = 0
    n += write(D / "works" / "WORK-TIT.json", {"id": "WORK-TIT", "type": "work", "status": "draft", "tags": TAGS,
                                              "name": "Brief an Titus", "original_language": "grc"})
    for uid, rng, kind, title, parts, summary in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-TIT", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}),
               "segmentation_note_de": "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung." if parts else None,
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        rec = {k: v for k, v in rec.items() if v is not None}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-13; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-tit").glob("*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in ((1, 16), (2, 15), (3, 15)):
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-TIT-{c:03d}.json")
        refs_c = [f"TIT.{c}.{v}" for v in range(1, last + 1)]
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-TIT-{c:03d}-001-{last:03d}-{code}-WORKING"
            dec = [{"reference": r, "target": tg, "kind": kd, "grc": grc, **({"more_literal": ml} if ml else {}),
                    **({"other_options": oo} if oo else {}), "note": nt}
                   for r, tg, kd, grc, ml, oo, nt in decs if r in refs_c]
            for d in dec:
                if d["target"] not in texts[d["reference"]]:
                    raise SystemExit(f"{tid}: Entscheidung {d['target']!r} nicht im Text {d['reference']}")
            alts = []
            for a in ALTS:
                vid, ref, f_de, t_de, f_g, t_g, eff, n_de, n_g, w_de, w_g, o_de, o_g = a
                if ref not in refs_c:
                    continue
                f_, t_, nt, ws, og = (f_de, t_de, n_de, w_de, o_de) if lang == "de" else (f_g, t_g, n_g, w_g, o_g)
                if f_ not in texts[ref]:
                    raise SystemExit(f"{tid}: Alternative {f_!r} nicht im Text {ref}")
                alts.append({"reading": vid, "reference": ref, "from_text": f_, "to_text": t_, "effect": eff, "note": nt,
                             "readings": {k: [{"grc": g, "text": x, **({"note": h} if h else {})} for g, x, h in v] for k, v in ws.items()},
                             "origin": og})
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"TIT.{c}.1-TIT.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-TIT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
                                       if lang == "de" else "Direkt aus dem SBLGNT übersetzt, mit Wortzuordnung zu den Token; die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle. Nicht aus einer veröffentlichten Mundart-Bibel übernommen."),
                        "based_on_edition": "ED-SBLGNT", "based_on_tokens": ts_id, "follows_readings": follows,
                        "text_by_reference": texts, "authorship_de": AUTH if lang == "de" else AUTH_GSW,
                        "knowledge": {"asserted_at": DATE, "supersedes": None}, "decisions": dec,
                        "decisions_note_de": "Übersetzungsentscheidungen: wörtlich (literal), sprachlich angepasst (adapted), Deutungsentscheidung (interpretive) oder der vertrauten Wiedergabe folgend (traditional). " + (AUTH if lang == "de" else AUTH_GSW)})
            if alts:
                rec["alternatives"] = alts
                rec["alternatives_note_de"] = "Wiedergabe abweichender Lesarten, soweit sie die Übersetzung verändern. " + (AUTH if lang == "de" else AUTH_GSW)
                rec["alternatives_origin_note"] = ("Mögliche Erklärungen, wie die Unterschiede entstanden sein könnten. Sie stehen nebeneinander; keine ist als richtig entschieden."
                                                   if lang == "de" else "Möglichi Erkläärige, wie d Underschid entstande sii chönnted. Si stönd näbenand; keini isch als richtig entschide.")
            n += write(D / "translations" / f"{tid}.json", rec)
            aid = f"ALIGN-TIT-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"TIT.{c}.1-TIT.{c}.{last}",
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/titus_text.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Titus – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
