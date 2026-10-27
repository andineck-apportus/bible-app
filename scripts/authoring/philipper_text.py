#!/usr/bin/env python3
"""Autorenwerkzeug: Philipperbrief – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/philipper_text.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben in den Lesarten stammen aus der maschinellen Zuordnung
(METHOD-AUTO-COLLATION-V1) bzw. aus der CNTR-Transkription, nicht aus eigener Prüfung der Handschriften.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, write  # noqa: E402

DATE = "2026-10-13"
AUTH = "KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-PHILIPPIANS"]
CHAPTERS = ((1, 30), (2, 30), (3, 21), (4, 23))

DE = {
 # ------------------------------------------------------------ Kapitel 1
 "PHP.1.1": "Paulus{1} und{2} Timotheus{3}, [Knechte]{4} [Christi Jesu]{5,6}, an alle{7} [Heiligen]{8,9} [in Christus Jesus]{10-12}, [die]{13} [in]{15} Philippi{16} [sind]{14}, [samt]{17} [den Aufsehern]{18} und{19} [Diakonen]{20}:",
 "PHP.1.2": "Gnade{1} sei mit [euch]{2} und{3} Friede{4} [von]{5} Gott{6}, [unserem]{8} Vater{7}, und{9} [dem Herrn]{10} Jesus{11} Christus{12}.",
 "PHP.1.3": "[Ich danke]{1} [meinem]{4} [Gott]{2,3} [bei]{5} [jedem]{6} [Gedenken]{7,8} [an euch]{9}",
 "PHP.1.4": "– [allezeit]{1}, [in]{2} [jedem]{3} [meiner]{5} [Gebete]{4} [für]{6} [euch]{8} [alle]{7} [bete ich]{11-13} [mit]{9} [Freude]{10} –",
 "PHP.1.5": "[für]{1} [eure]{4} [Gemeinschaft]{2,3} [im Dienst am]{5,6} [Evangelium]{7} [vom]{8} [ersten]{10} [Tag]{9,11} [an]{8} [bis]{12} [heute]{13,14}.",
 "PHP.1.6": "[Ich bin]{1} [ganz]{2} [davon]{3} [überzeugt]{1}, [dass]{4} [der]{5}, [der]{6} [in]{7} [euch]{8} [ein gutes]{10} [Werk]{9} [angefangen hat]{6}, es [vollenden wird]{11} [bis]{12} [zum Tag]{13} [Christi Jesu]{14,15}.",
 "PHP.1.7": "So{1} [ist es]{2} [für mich]{4} [nur recht]{3}, [dies]{5} [von]{7} [euch]{9} [allen]{8} [zu denken]{6}, [weil]{10,11} [ich]{13} [euch]{17} [im]{14,15} [Herzen]{16} [trage]{12}: [Sowohl]{19} [in]{18} [meinen]{22} [Fesseln]{20,21} [als auch]{23} [bei]{24} [der]{25} [Verteidigung]{26} und{27} [Bekräftigung]{28} [des]{29} [Evangeliums]{30} [seid]{37} [ihr]{36} [alle]{35} [mit mir]{32} [Teilhaber]{31} [an der Gnade]{33,34}.",
 "PHP.1.8": "Denn{2} [Gott]{4,5} ist [mein]{3} [Zeuge]{1}, [wie]{6} [ich mich]{7} [nach euch]{9} [allen]{8} [sehne]{7} [mit]{10} [der innigen Liebe]{11} [Christi Jesu]{12,13}.",
 "PHP.1.9": "Und{1} [darum]{2} [bete ich]{3}, [dass]{4} [eure]{7} [Liebe]{5,6} [noch]{8} [mehr]{9} und{10} [mehr]{11} [zunimmt]{12} [an]{13} [Erkenntnis]{14} und{15} [aller]{16} [Einsicht]{17},",
 "PHP.1.10": "[sodass]{1,2} [ihr]{4} [prüfen könnt]{3}, [worauf es ankommt]{5,6}, [damit]{7} [ihr]{8} [lauter]{9} und{10} [ohne Anstoss]{11} [seid]{8} [auf]{12} [den Tag]{13} [Christi]{14},",
 "PHP.1.11": "[erfüllt]{1} [mit der Frucht]{2} [der Gerechtigkeit]{3}, [die]{4} [durch]{5} Jesus{6} Christus{7} kommt, [zur]{8} [Ehre]{9} und{10} [zum Lob]{11} [Gottes]{12}.",
 "PHP.1.12": "[Ich will]{4} [euch]{3} [aber]{2} [wissen lassen]{1}, [Brüder und Schwestern]{5}, [dass]{6} [das]{7}, [was]{8} [mich]{9} [betrifft]{8}, [eher]{10} [zur]{11} [Förderung]{12} [des]{13} [Evangeliums]{14} [geführt hat]{15},",
 "PHP.1.13": "[sodass]{1} [im]{9} [ganzen]{10} [Prätorium]{11,12} und{13} [bei]{14} [allen]{16} [anderen]{15} [bekannt]{5} [geworden ist]{8}, dass [ich]{4} [um Christi willen]{6,7} [in Fesseln liege]{2,3},",
 "PHP.1.14": "und{1} dass [die meisten]{2,3} [der]{4} [Geschwister]{5}, [im]{6} [Herrn]{7} [durch]{9} [meine]{11} [Fesseln]{10} [ermutigt]{8}, [umso mehr]{12} [wagen]{13}, [das]{15} [Wort]{16} [furchtlos]{14} [zu sagen]{17}.",
 "PHP.1.15": "[Einige]{1} [verkündigen]{15} [Christus]{13,14} [zwar]{2} [auch]{3} [aus]{4} [Neid]{5} und{6} [Streitsucht]{7}, [andere]{8} [aber]{9} [auch]{10} [aus]{11} [gutem Willen]{12}.",
 "PHP.1.16": "[Die einen]{1,2} tun es [aus]{3} [Liebe]{4}, [weil sie wissen]{5}, [dass]{6} [ich]{11} [zur]{7} [Verteidigung]{8} [des]{9} [Evangeliums]{10} [bestimmt bin]{11};",
 "PHP.1.17": "[die anderen]{1,2} [verkündigen]{7} [Christus]{5,6} [aus]{3} [Eigennutz]{4}, [nicht]{8} [lauter]{9}; [sie meinen]{10}, [mir]{15} [in den]{13} [Fesseln]{14} [noch Bedrängnis]{11} [zu bereiten]{12}.",
 "PHP.1.18": "[Was soll's]{1,2:idiom}? [Wenn nur]{3,4} [auf jede]{5} [Weise]{6}, [ob]{7} [zum Vorwand]{8} [oder]{9} [in Wahrheit]{10}, [Christus]{11} [verkündigt wird]{12}! Und{13} [darüber]{14,15} [freue ich mich]{16}. [Ja]{17}, [ich werde mich]{19} [auch]{18} [weiterhin freuen]{19},",
 "PHP.1.19": "denn{2} [ich weiss]{1}, [dass]{3} [dies]{4} [mir]{5} [zur]{7} [Rettung]{8} [ausschlagen wird]{6} [durch]{9} [euer]{11} [Gebet]{10,12} und{13} [den Beistand]{14} [des]{15} [Geistes]{16} [Jesu]{17} [Christi]{18},",
 "PHP.1.20": "[nach]{1} [meiner]{6} [sehnsüchtigen Erwartung]{2,3} und{4} [Hoffnung]{5}, [dass]{7} [ich]{10} [in]{8} [nichts]{9} [beschämt werde]{10}, [sondern]{11} dass [mit]{12} [allem]{13} [Freimut]{14}, [wie]{15} [immer]{16} [so auch]{17} [jetzt]{18}, [Christus]{20} [gross gemacht wird]{19} [an]{21} [meinem]{24} [Leib]{22,23}, [sei es]{25} [durch]{26} [Leben]{27} [oder]{28} [durch]{29} [Tod]{30}.",
 "PHP.1.21": "Denn{2} [für mich]{1} ist [das Leben]{3,4} [Christus]{5} und{6} [das Sterben]{7,8} [Gewinn]{9}.",
 "PHP.1.22": "[Wenn]{1} [aber]{2} [das Leben]{3,4} [im]{5} [Fleisch]{6} – [das]{7} bedeutet [für mich]{8} [Frucht]{9} [der Arbeit]{10} –, [dann]{11} [weiss ich]{15} [nicht]{14}, [was]{12} [ich wählen soll]{13}.",
 "PHP.1.23": "[Ich werde]{1} [aber]{2} [von]{3} [beiden Seiten]{4,5} [bedrängt]{1}: [Ich habe]{8} [das Verlangen]{6,7}, [aufzubrechen]{9-11} und{12} [bei]{13} [Christus]{14} [zu sein]{15}, denn{17} das wäre [bei weitem]{16,18} [das Bessere]{19};",
 "PHP.1.24": "[das]{1} [Bleiben]{3} [im]{4,5} [Fleisch]{6} [aber]{2} ist [um euretwillen]{8,9} [nötiger]{7}.",
 "PHP.1.25": "Und{1} [im Vertrauen]{3} [darauf]{2} [weiss ich]{4}, [dass]{5} [ich bleiben]{6} und{7} [bei]{8} [euch]{10} [allen]{9} [ausharren werde]{8} [zu]{11} [eurem]{13} [Fortschritt]{12,14} und{15} [zur Freude]{16} [im]{17} [Glauben]{18},",
 "PHP.1.26": "[damit]{1} [euer]{4} [Rühmen]{2,3} [in]{6} [Christus Jesus]{7,8} [meinetwegen]{9,10} [überreich werde]{5} [durch]{11} [mein]{12,13} [erneutes]{15} [Kommen]{14} [zu]{16} [euch]{17}.",
 "PHP.1.27": "Nur{1}: [Lebt als Bürger]{7}, [wie es]{2} [dem]{3} [Evangelium]{4} [Christi]{5,6} [entspricht]{2}, [damit]{8} ich, [ob]{9} [ich komme]{10} und{11} [euch]{13} [sehe]{12} [oder]{14} [abwesend bin]{15}, [höre]{16}, [wie es um euch steht]{17-19}: [dass]{20} [ihr]{21} [in]{22} [einem]{23} [Geist]{24} [feststeht]{21} und [einmütig]{25,26} [miteinander kämpft]{27} [für]{28} [den Glauben]{29} [des]{30} [Evangeliums]{31}",
 "PHP.1.28": "und{1} euch [durch nichts]{2,4,5} [von]{6} [den]{7} [Gegnern]{8} [einschüchtern lasst]{3} – [das]{9} [ist]{10} [für sie]{11} [ein Anzeichen]{12} [des Verderbens]{13}, [aber]{15} [eurer]{14} [Rettung]{16}, [und zwar]{17,18} [von]{19} [Gott]{20}.",
 "PHP.1.29": "[Denn]{1} [euch]{2} [ist]{3} [es]{4} [geschenkt worden]{3}, [für]{5} [Christus]{6} – [nicht]{7} [nur]{8} [an]{10} [ihn]{11} [zu glauben]{9,12}, [sondern]{13} [auch]{14} [für]{16} [ihn]{17} [zu leiden]{15,18} –,",
 "PHP.1.30": "[da ihr]{4} [denselben]{1,2} [Kampf]{3} [führt]{4}, [wie]{5} [ihr ihn]{6} [an]{7} [mir]{8} [gesehen habt]{6} und{9} [jetzt]{10} [über]{12} [mich]{13} [hört]{11}.",
 # ------------------------------------------------------------ Kapitel 2
 "PHP.2.1": "[Wenn es]{1} [nun]{3} [irgendeine]{2} [Ermutigung]{4} [in]{5} [Christus]{6} [gibt]{1}, [wenn]{7} [irgendeinen]{8} [Zuspruch]{9} [der Liebe]{10}, [wenn]{11} [irgendeine]{12} [Gemeinschaft]{13} [des Geistes]{14}, [wenn]{15} [irgendwelche]{16} [herzliche Zuneigung]{17} und{18} [Barmherzigkeit]{19},",
 "PHP.2.2": "[dann macht]{1} [meine]{2} [Freude]{3,4} [vollkommen]{1}: [dass]{5} [ihr]{8} [dasselbe]{6,7} [denkt]{8}, [dieselbe]{9,10} [Liebe]{11} [habt]{12}, [einmütig]{13}, [auf das eine]{14,15} [bedacht]{16}.",
 "PHP.2.3": "[Tut nichts]{1} [aus]{2} [Eigennutz]{3} [noch]{4} [aus]{5} [eitler Ruhmsucht]{6}, [sondern]{7} [in]{8} [Demut]{9} [achtet]{11} [einander]{10} [höher]{12} [als euch selbst]{13};",
 "PHP.2.4": "[jeder]{4} [achte]{5} [nicht]{1} nur [auf das]{2} [Eigene]{3}, [sondern]{6} [jeder]{10} [auch]{7} [auf das]{8} [der anderen]{9}.",
 "PHP.2.5": "[Habt]{2} [diese]{1} [Gesinnung]{2} [unter]{3} [euch]{4}, [die]{5} [auch]{6} [in]{7} [Christus Jesus]{8,9} war:",
 "PHP.2.6": "[Er]{1}, [obwohl er]{5} [in]{2} [der Gestalt]{3} [Gottes]{4} [war]{5}, [hielt]{8} [es]{9} [nicht]{6} [für ein Beutestück]{7}, [Gott]{12} [gleich]{11} [zu sein]{10},",
 "PHP.2.7": "[sondern]{1} [er entäusserte]{3} [sich selbst]{2}, [nahm]{6} [die Gestalt]{4} [eines Sklaven]{5} [an]{6} [und wurde]{10} [den Menschen]{9} [gleich]{7,8}. Und{11} [als er]{13} [der äusseren Erscheinung nach]{12} [wie]{14} [ein Mensch]{15} [befunden wurde]{13},",
 "PHP.2.8": "[erniedrigte er]{1} [sich selbst]{2} [und wurde]{3} [gehorsam]{4} [bis]{5} [zum Tod]{6}, [ja]{8} [zum Tod]{7} [am Kreuz]{9}.",
 "PHP.2.9": "[Darum]{1} [hat]{6} [Gott]{3,4} [ihn]{5} [auch]{2} [über alles erhöht]{6} und{7} [ihm]{9} [den Namen]{10,11} [geschenkt]{8}, [der]{12} [über]{13} [jedem]{14} [Namen]{15} ist,",
 "PHP.2.10": "[damit]{1} [im]{2,3} [Namen]{4} [Jesu]{5} [jedes]{6} [Knie]{7} [sich beuge]{8}, [im Himmel]{9} und{10} [auf der Erde]{11} und{12} [unter der Erde]{13},",
 "PHP.2.11": "und{1} [jede]{2} [Zunge]{3} [bekenne]{4}, [dass]{5} Jesus{7} Christus{8} [der Herr]{6} ist, [zur]{9} [Ehre]{10} [Gottes]{11}, [des Vaters]{12}.",
 "PHP.2.12": "[Darum]{1}, [meine]{3} [Lieben]{2}, [wie]{4} [ihr]{6} [immer]{5} [gehorsam wart]{6}, [nicht]{7} [nur]{13} [wie]{8} [in]{9} [meiner]{12} [Anwesenheit]{10,11}, [sondern]{14} [jetzt]{15} [viel]{16} [mehr]{17} [in]{18} [meiner]{21} [Abwesenheit]{19,20}: [Mit]{22} [Furcht]{23} und{24} [Zittern]{25} [wirkt]{29} [eure]{27} [Rettung]{26,28} [aus]{29}.",
 "PHP.2.13": "Denn{2} Gott{1} ist{3} es, [der]{4} [in]{6} [euch]{7} [wirkt]{5}: [sowohl]{8} [das Wollen]{9,10} [als auch]{11} [das Vollbringen]{12,13}, [zu]{14} [seinem]{15} [Wohlgefallen]{16}.",
 "PHP.2.14": "[Tut]{2} [alles]{1} [ohne]{3} [Murren]{4} und{5} [Widerrede]{6},",
 "PHP.2.15": "[damit]{1} [ihr]{2} [untadelig]{3} und{4} [lauter]{5} [werdet]{2}, [makellose]{8} [Kinder]{6} [Gottes]{7} [mitten in]{9} einer [krummen]{11} und{12} [verdrehten]{13} [Generation]{10}, [unter]{14} [der]{15} [ihr]{16} [leuchtet]{16} [wie]{17} [Lichter]{18} [in]{19} [der Welt]{20}",
 "PHP.2.16": "[indem ihr]{3} [am Wort]{1} [des Lebens]{2} [festhaltet]{3}, [mir]{6} [zum]{4} [Ruhm]{5} [auf]{7} [den Tag]{8} [Christi]{9}, [dass]{10} [ich]{14} [nicht]{11} [ins]{12} [Leere]{13} [gelaufen bin]{14} [und auch nicht]{15} [ins]{16} [Leere]{17} [gearbeitet habe]{18}.",
 "PHP.2.17": "[Aber]{1} [selbst wenn]{2,3} [ich als Trankopfer ausgegossen werde]{4} [über]{5} [dem]{6} [Opfer]{7} und{8} [Gottesdienst]{9} [eures]{12} [Glaubens]{10,11}, [freue ich mich]{13} und{14} [freue mich mit]{15} [euch]{17} [allen]{16}.",
 "PHP.2.18": "[Ebenso]{1,3} [aber]{2} [freut]{6} [auch]{4} [ihr]{5} [euch]{6} und{7} [freut euch mit]{8} [mir]{9}!",
 "PHP.2.19": "[Ich hoffe]{1} [aber]{2} [im]{3} [Herrn]{4} Jesus{5}, [Timotheus]{6} [bald]{7} [zu euch]{9} [zu senden]{8}, [damit]{10} [auch ich]{11} [ermutigt werde]{12}, [wenn ich erfahre]{13}, [wie es um euch steht]{14-16}.",
 "PHP.2.20": "Denn{2} [ich habe]{3} [keinen]{1} [Gleichgesinnten]{4}, [der]{5} [sich]{10} [so aufrichtig]{6} [um]{7,8} [euch]{9} [sorgen wird]{10};",
 "PHP.2.21": "denn{3} [alle]{1,2} [suchen]{6} [das Ihre]{4,5}, [nicht]{7} [das]{8}, [was Jesu Christi ist]{9,10}.",
 "PHP.2.22": "[Ihr kennt]{5} [aber]{2} [seine]{4} [Bewährung]{1,3}: [dass]{6} er [wie]{7} [ein Kind]{9} [dem Vater]{8} [mit]{10} [mir]{11} [für]{13} [das]{14} [Evangelium]{15} [gedient hat]{12}.",
 "PHP.2.23": "[Ihn]{1} [hoffe ich]{4} [also]{3} [sofort]{12} [zu senden]{5}, [sobald]{6,7} [ich absehe]{8}, [wie es um mich steht]{9-11}. ~2(μέν bereitet den Gegensatz zu [[PHP.2.24]] vor; nicht eigens wiedergegeben)",
 "PHP.2.24": "[Ich vertraue]{1} [aber]{2} [im]{3} [Herrn]{4} darauf, [dass]{5} [auch]{6} [ich selbst]{7} [bald]{8} [kommen werde]{9}.",
 "PHP.2.25": "[Ich habe es]{3} [aber]{2} [für nötig]{1} [gehalten]{3}, [Epaphroditus]{4}, [meinen]{11} [Bruder]{5,6} und{7} [Mitarbeiter]{8} und{9} [Mitstreiter]{10}, [aber]{13} [euren]{12} [Gesandten]{14} und{15} [Diener]{16} [für]{17} [meinen]{19} [Bedarf]{18}, [zu euch]{21,22} [zu senden]{20},",
 "PHP.2.26": "[denn]{1} [er sehnte sich]{2,3} [nach euch]{5} [allen]{4} und{6} [war voller Unruhe]{7}, [weil]{8} [ihr gehört hattet]{9}, [dass]{10} [er krank war]{11}.",
 "PHP.2.27": "[Er war]{3} [ja]{2} [auch]{1} [krank]{3}, [dem Tod]{5} [nahe]{4}. [Aber]{6} [Gott]{7,8} [hat sich]{9} [über ihn]{10} [erbarmt]{9}, [und]{13} [nicht]{11} [nur]{14} [über ihn]{12}, [sondern]{15} [auch]{16} [über mich]{17}, [damit]{18} [ich]{23} [nicht]{19} [Trauer]{20} [auf]{21} [Trauer]{22} [habe]{23}.",
 "PHP.2.28": "[Umso eiliger]{1} [schicke ich]{3} [ihn]{4} [nun]{2}, [damit]{5} [ihr euch]{9}, [wenn ihr]{6} [ihn]{7} [wieder]{8} [seht]{6}, [freut]{9} [und ich]{10} [weniger Kummer]{11} [habe]{12}.",
 "PHP.2.29": "[Nehmt]{1} [ihn]{3} [also]{2} [auf]{1} [im]{4} [Herrn]{5} [mit]{6} [aller]{7} [Freude]{8}, und{9} [haltet]{13} [solche]{10,11} [in Ehren]{12};",
 "PHP.2.30": "[denn]{1} [wegen]{2} [des]{3} [Werkes]{4} [Christi]{5} [ist er]{8} [bis an]{6} [den Tod]{7} [herangekommen]{8} [und hat]{9} [sein Leben]{10,11} [aufs Spiel gesetzt]{9}, [um]{12} [auszufüllen]{13}, [was]{14} [euch]{15} [am]{17} [Dienst]{20} [für]{18} [mich]{19} [noch fehlte]{16}.",
 # ------------------------------------------------------------ Kapitel 3
 "PHP.3.1": "[Im Übrigen]{1,2}, [meine]{4} [Brüder und Schwestern]{3}: [Freut euch]{5} [im]{6} [Herrn]{7}! [Euch]{11} [dasselbe]{8,9} [zu schreiben]{10}, ist [mir]{12} [zwar]{13} [nicht]{14} [lästig]{15}, [euch]{16} [aber]{17} [gibt es Sicherheit]{18}.",
 "PHP.3.2": "[Gebt acht auf]{1} [die]{2} [Hunde]{3}, [gebt acht auf]{4} [die]{5} [schlechten]{6} [Arbeiter]{7}, [gebt acht auf]{8} [die]{9} [Zerschneidung]{10}!",
 "PHP.3.3": "Denn{2} [wir]{1} [sind]{3} [die]{4} [Beschneidung]{5}, [die wir]{6} [im Geist]{7} [Gottes]{8} [dienen]{9} und{10} [uns]{11} [in]{12} [Christus Jesus]{13,14} [rühmen]{11} und{15} [nicht]{16} [auf]{17} [das Fleisch]{18} [vertrauen]{19},",
 "PHP.3.4": "[obwohl]{1} [ich]{2} [auch]{5} [im]{6} [Fleisch]{7} [Grund zum Vertrauen]{4} [hätte]{3}. [Wenn]{8} [irgendein]{9} [anderer]{11} [meint]{10}, [auf]{13} [das Fleisch]{14} [vertrauen zu können]{12}, [ich]{15} [noch mehr]{16}:",
 "PHP.3.5": "[beschnitten]{1} [am achten Tag]{2}, [aus]{3} [dem Volk]{4} [Israel]{5}, [vom Stamm]{6} [Benjamin]{7}, [Hebräer]{8} [von]{9} [Hebräern]{10}, [was das]{11} [Gesetz]{12} [betrifft]{11}, [Pharisäer]{13},",
 "PHP.3.6": "[was]{1} [den Eifer]{2} [betrifft]{1}, [ein Verfolger]{3} [der]{4} [Gemeinde]{5}, [was]{6} [die Gerechtigkeit]{7} [betrifft]{6}, [die]{8} [im]{9} [Gesetz]{10} gilt, [untadelig]{12} [geworden]{11}.",
 "PHP.3.7": "[Aber]{1} [was]{2} [mir]{4} [Gewinn]{5} [war]{3}, [das]{6} [habe ich]{7} [um]{8} [Christi]{9,10} [willen]{8} [für Verlust]{11} [gehalten]{7}.",
 "PHP.3.8": "[Ja]{1}, [mehr noch]{2}: [Ich halte]{4} [auch]{3} [alles]{5} [für Verlust]{6,7} [wegen]{8} [des Überragenden]{9,10} [der]{11} [Erkenntnis]{12} [Christi Jesu]{13,14}, [meines]{17} [Herrn]{15,16}. [Seinetwegen]{18,19} [habe ich]{22} [alles]{20,21} [verloren]{22} und{23} [halte es]{24} [für Dreck]{25}, [damit]{26} [ich]{28} [Christus]{27} [gewinne]{28}",
 "PHP.3.9": "und{1} [in]{3} [ihm]{4} [gefunden werde]{2}, [indem ich]{6} [nicht]{5} [meine]{7} [Gerechtigkeit]{8} [habe]{6} – [die]{9} [aus]{10} [dem Gesetz]{11} –, [sondern]{12} [die]{13} [durch]{14} [den Glauben an Christus]{15,16}, [die]{17} [Gerechtigkeit]{20} [aus]{18} [Gott]{19} [aufgrund]{21} [des]{22} [Glaubens]{23},",
 "PHP.3.10": "[um]{1} [ihn]{3} [zu erkennen]{2} und{4} [die]{5} [Kraft]{6} [seiner]{7,9} [Auferstehung]{8} und{10} [die Gemeinschaft]{11} [mit seinen]{13} [Leiden]{12}, [indem ich]{14} [seinem]{15,17} [Tod]{16} [gleichgestaltet werde]{14},",
 "PHP.3.11": "[ob ich]{1} [irgendwie]{2} [zur]{4,5} [Auferstehung]{6} [aus]{7,8} [den Toten]{9} [gelange]{3}.",
 "PHP.3.12": "[Nicht]{1}, [dass]{2} [ich es]{4} [schon]{3} [erlangt hätte]{4} [oder]{5} [schon]{6} [vollendet wäre]{7}; [ich jage]{8} [aber]{9} [danach]{8}, [ob ich es]{10} [auch]{11} [ergreife]{12}, [weil]{13,14} [ich]{16} [auch]{15} [von]{17} [Christus]{18} [ergriffen worden bin]{16}.",
 "PHP.3.13": "[Brüder und Schwestern]{1}, [ich]{2} [meine]{5} [von mir selbst]{3} [nicht]{4}, [es ergriffen zu haben]{6}. [Eines]{7} [aber]{8}: [Ich vergesse]{12}, [was]{9,10} [hinter mir]{11} liegt, [und]{14} [strecke mich]{16} [nach dem]{13} [aus]{16}, [was vor mir]{15} liegt,",
 "PHP.3.14": "[auf das Ziel zu]{1,2} [jage ich]{3} [dem]{5} [Siegespreis]{6} [der]{7} [himmlischen]{8} [Berufung]{9} [Gottes]{10,11} [in]{12} [Christus Jesus]{13,14} [nach]{4}.",
 "PHP.3.15": "[Wir alle]{1} [also]{2}, [die]{1} [reif]{3} sind, [wollen]{5} [so]{4} [denken]{5}; und{6} [wenn]{7} [ihr]{10} [in irgendetwas]{8} [anders]{9} [denkt]{10}, [wird]{16} [Gott]{13,14} [euch]{15} [auch]{11} [das]{12} [offenbaren]{16}.",
 "PHP.3.16": "Nur{1}: [Wo]{2,3} [wir angelangt sind]{4}, [auf derselben Linie]{5,6} [lasst uns weitergehen]{7}.",
 "PHP.3.17": "[Werdet]{3} [miteinander]{1} [meine]{2} [Nachahmer]{1}, [Brüder und Schwestern]{4}, und{5} [achtet auf]{6} [die]{7}, die [so]{8} [leben]{9}, [wie]{10} [ihr]{11} [uns]{13} [als Vorbild]{12} [habt]{11}.",
 "PHP.3.18": "Denn{2} [viele]{1} [leben]{3} – [von denen]{4} ich [euch]{7} [oft]{5} [gesagt habe]{6} [und]{9} [jetzt]{8} [auch]{10} [unter Tränen]{11} [sage]{12} – [als]{13} [die Feinde]{14} [des]{15} [Kreuzes]{16} [Christi]{17,18}.",
 "PHP.3.19": "[Ihr]{1} [Ende]{2,3} ist [Verderben]{4}, [ihr]{5} [Gott]{6,7} [der Bauch]{8,9} und{10} [ihre Ehre]{11,12} [in]{13} [ihrer]{16} [Schande]{14,15}; [sie]{17} sind [auf das Irdische]{18,19} [bedacht]{20}.",
 "PHP.3.20": "Denn{2} [unser]{1} [Bürgerrecht]{3,4} [ist]{7} [im]{5} [Himmel]{6}, [von]{8} [wo]{9} [wir]{12} [auch]{10} [den Retter]{11} [erwarten]{12}, [den Herrn]{13} [Jesus Christus]{14,15},",
 "PHP.3.21": "[der]{1} [unseren]{7} [armseligen]{5,6} [Leib]{3,4} [verwandeln wird]{2}, [gleichgestaltet]{8} [seinem]{13} [herrlichen]{11,12} [Leib]{9,10}, [gemäss]{14} [der]{15} [Kraft]{16}, [mit der]{17} [er]{19} [vermag]{18}, [sich]{22} [auch]{20} [alles]{23,24} [zu unterwerfen]{21}.",
 # ------------------------------------------------------------ Kapitel 4
 "PHP.4.1": "[Darum]{1}, [meine]{3} [geliebten]{4} und{5} [ersehnten]{6} [Brüder und Schwestern]{2}, [meine]{10} [Freude]{7} und{8} mein [Siegeskranz]{9}: [So]{11} [steht fest]{12} [im]{13} [Herrn]{14}, [ihr Geliebten]{15}!",
 "PHP.4.2": "[Euodia]{1} [bitte ich]{2}, und{3} [Syntyche]{4} [bitte ich]{5}, [eines Sinnes zu sein]{6-8} [im]{9} [Herrn]{10}.",
 "PHP.4.3": "[Ja]{1}, [ich bitte]{2} [auch]{3} [dich]{4}, [treuer]{5} [Gefährte]{6}: [Hilf]{7} [ihnen]{8}! [Sie]{9} [haben]{13} [im]{10,11} [Evangelium]{12} [mit mir]{14} [gekämpft]{13}, [zusammen]{15} [sowohl mit]{16} [Klemens]{17} [als auch mit]{18} [meinen]{22} [übrigen]{19,20} [Mitarbeitern]{21}, [deren]{23} [Namen]{24,25} [im]{26} [Buch]{27} [des Lebens]{28} stehen.",
 "PHP.4.4": "[Freut euch]{1} [im]{2} [Herrn]{3} [allezeit]{4}! [Noch einmal]{5} [sage ich]{6}: [Freut euch]{7}!",
 "PHP.4.5": "[Eure]{3} [Güte]{1,2} [werde]{4} [allen]{5} [Menschen]{6} [bekannt]{4}. [Der]{7} [Herr]{8} [ist nahe]{9}.",
 "PHP.4.6": "[Sorgt euch]{2} [um nichts]{1}, [sondern]{3} [in]{4} [allem]{5} [lasst]{16} [eure]{15} [Anliegen]{13,14} [durch]{6} [Gebet]{7} und{8} [Flehen]{9,10} [mit]{11} [Danksagung]{12} [vor]{17} [Gott]{18,19} [kund werden]{16}.",
 "PHP.4.7": "Und{1} [der]{2} [Friede]{3} [Gottes]{4,5}, [der]{6} [allen]{8} [Verstand]{9} [übersteigt]{7}, [wird]{10} [eure]{13} [Herzen]{11,12} und{14} [eure]{17} [Gedanken]{15,16} [bewahren]{10} [in]{18} [Christus Jesus]{19,20}.",
 "PHP.4.8": "[Im Übrigen]{1,2}, [Brüder und Schwestern]{3}: [Was]{4} [wahr]{6} [ist]{5}, [was]{7} [ehrbar]{8}, [was]{9} [gerecht]{10}, [was]{11} [rein]{12}, [was]{13} [liebenswert]{14}, [was]{15} [einen guten Ruf hat]{16}, [wenn es]{17} [irgendeine]{18} [Tugend]{19} [gibt]{17} und{20} [wenn es]{21} [irgendein]{22} [Lob]{23} [gibt]{21}: [darauf]{24} [seid bedacht]{25}!",
 "PHP.4.9": "[Was]{1} ihr [auch]{2} [gelernt]{3} und{4} [empfangen]{5} und{6} [gehört]{7} und{8} [gesehen habt]{9} [an]{10} [mir]{11}, [das]{12} [tut]{13}! Und{14} [der]{15} [Gott]{16} [des]{17} [Friedens]{18} [wird]{19} [mit]{20} [euch]{21} [sein]{19}.",
 "PHP.4.10": "[Ich habe mich]{1} [aber]{2} [im]{3} [Herrn]{4} [sehr]{5} [gefreut]{1}, [dass]{6} [ihr]{9} [endlich]{7,8} [wieder aufgeblüht seid]{9}, [für]{11} [mich]{12} [zu sorgen]{10,13}. [Ihr habt]{17} [auch]{16} [daran]{14,15} [gedacht]{17}, [doch]{19} [es fehlte euch die Gelegenheit]{18}.",
 "PHP.4.11": "[Nicht]{1}, [dass]{2} ich das [aus]{3} [Mangel]{4} [sage]{5}; denn{7} [ich]{6} [habe gelernt]{8}, [mir selbst zu genügen]{12,13}, [wo]{9,10} [ich auch bin]{11}.",
 "PHP.4.12": "[Ich kann]{1} [mich]{3} [auch]{2} [einschränken]{3}, [ich kann]{4} [auch]{5} [im Überfluss leben]{6}; [in]{7} [allem]{8} und{9} [in]{10} [jedem]{11} [bin ich eingeweiht]{12}: [sowohl]{13} [satt zu sein]{14} [als auch]{15} [zu hungern]{16}, [sowohl]{17} [Überfluss zu haben]{18} [als auch]{19} [Mangel zu leiden]{20}.",
 "PHP.4.13": "[Alles]{1} [vermag ich]{2} [durch]{3} [den]{4}, der [mich]{6} [stark macht]{5}.",
 "PHP.4.14": "[Doch]{1} [ihr habt]{3} [gut]{2} [daran getan]{3}, [an]{6} [meiner]{5} [Bedrängnis]{7} [Anteil zu nehmen]{4}.",
 "PHP.4.15": "[Ihr wisst]{1} [aber]{2} [auch]{3} [selbst]{4}, [ihr Philipper]{5}, [dass]{6} [am]{7} [Anfang]{8} [des]{9} [Evangeliums]{10}, [als]{11} ich [von]{13} [Makedonien]{14} [aufbrach]{12}, [keine]{15} [Gemeinde]{17} [mit mir]{16} [Gemeinschaft hatte]{18} [auf die Rechnung]{19,20} [von Geben]{21} und{22} [Nehmen]{23} [ausser]{24,25} [ihr]{26} [allein]{27}.",
 "PHP.4.16": "[Denn]{1} [auch]{2} [in]{3} [Thessalonich]{4} [habt ihr]{13} [mir]{12} [mehr als einmal]{5-8:idiom} etwas [für]{9} [meinen]{10} [Bedarf]{11} [geschickt]{13}.",
 "PHP.4.17": "[Nicht]{1}, [dass]{2} ich [auf das Geschenk]{4,5} [aus wäre]{3}; [sondern]{6} [ich bin aus auf]{7} [die]{8} [Frucht]{9}, [die]{10} [sich]{11} [auf]{12} [eurem]{14} [Konto]{13} [vermehrt]{11}.",
 "PHP.4.18": "[Ich habe]{1} [aber]{2} [alles]{3} [erhalten]{1} und{4} [habe Überfluss]{5}. [Ich habe die Fülle]{6}, [seit ich]{7} [von]{8} [Epaphroditus]{9} [eure Gaben]{10-12} [empfangen habe]{7}: [einen Duft]{13} [des Wohlgeruchs]{14}, [ein Opfer]{15}, [angenehm]{16}, [Gott]{18,19} [wohlgefällig]{17}.",
 "PHP.4.19": "[Mein]{4} [Gott]{1,3} [aber]{2} [wird]{5} [all]{6} [euren]{8} [Bedarf]{7} [erfüllen]{5} [nach]{9} [seinem]{12} [Reichtum]{10,11} [in]{13} [Herrlichkeit]{14} [in]{15} [Christus Jesus]{16,17}.",
 "PHP.4.20": "[Unserem]{6} [Gott]{1,3} und{4} [Vater]{5} [aber]{2} sei [die]{7} [Ehre]{8} [in]{9} [alle Ewigkeit]{10-13}. [Amen]{14}.",
 "PHP.4.21": "[Grüsst]{1} [jeden]{2} [Heiligen]{3} [in]{4} [Christus Jesus]{5,6}. [Es grüssen]{7} [euch]{8} [die]{9} [Geschwister]{12}, die [bei]{10} [mir]{11} sind.",
 "PHP.4.22": "[Es grüssen]{1} [euch]{2} [alle]{3} [Heiligen]{4,5}, [besonders]{6} [aber]{7} [die]{8} [aus]{9} [dem]{10} [Haus]{12} [des Kaisers]{11}.",
 "PHP.4.23": "[Die]{1} [Gnade]{2} [des]{3} [Herrn]{4} [Jesus Christus]{5,6} sei [mit]{7} [eurem]{10} [Geist]{8,9}!",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 1
 "PHP.1.1": "De Paulus{1} und{2} de Timotheus{3}, [Chnächt]{4} [vo Christus Jesus]{5,6}, a alli{7} [Heilige]{8,9} [in Christus Jesus]{10-12}, [wo]{13} [z]{15} Philippi{16} [sind]{14}, [mitsamt]{17} [de Ufseher]{18} und{19} [Diakone]{20}:",
 "PHP.1.2": "Gnad{1} sig mit [eu]{2} und{3} Fride{4} [vo]{5} Gott{6}, [öisem]{8} Vatter{7}, und{9} [vom Herr]{10} Jesus{11} Christus{12}.",
 "PHP.1.3": "[Ich dank]{1} [mim]{4} [Gott]{2,3} [jedesmal]{5,6}, [wänn ich]{7,8} [a eu]{9} [dänke]{7,8}",
 "PHP.1.4": "– [immer]{1}, [i]{2} [jedem]{3} [vo mine]{5} [Gebät]{4} [für]{6} [eu]{8} [alli]{7} [bätt ich]{11-13} [mit]{9} [Fröid]{10} –",
 "PHP.1.5": "[für]{1} [eui]{4} [Gmeinschaft]{2,3} [im Dienscht am]{5,6} [Evangelium]{7} [vom]{8} [erschte]{10} [Tag]{9,11} [a]{8} [bis]{12} [hüt]{13,14}.",
 "PHP.1.6": "[Ich bi]{1} [ganz]{2} [devo]{3} [überzüügt]{1}, [dass]{4} [dä]{5}, [wo]{6} [i]{7} [eu]{8} [es guets]{10} [Wärch]{9} [aagfange hät]{6}, es [bis]{12} [zum Tag]{13} [vo Christus Jesus]{14,15} [vollände wird]{11}.",
 "PHP.1.7": "So{1} [isch es]{2} [für mich]{4} [nu rächt]{3}, [das]{5} [vo]{7} [eu]{9} [allne]{8} [z dänke]{6}, [wil]{10,11} [ich]{13} [eu]{17} [im]{14,15} [Härz]{16} [träg]{12}: [Sowohl]{19} [i]{18} [mine]{22} [Fessle]{20,21} [als au]{23} [bi]{24} [de]{25} [Verteidigung]{26} und{27} [Bekräftigung]{28} [vom]{29} [Evangelium]{30} [sind]{37} [ir]{36} [alli]{35} [mit mir]{32} [Teilhaber]{31} [a de Gnad]{33,34}.",
 "PHP.1.8": "Dänn{2} [Gott]{4,5} isch [min]{3} [Züüge]{1}, [wie fescht]{6} [ich mich]{7} [nach eu]{9} [allne]{8} [sehne]{7} [mit]{10} [de innige Liebi]{11} [vo Christus Jesus]{12,13}.",
 "PHP.1.9": "Und{1} [drum]{2} [bätt ich]{3}, [dass]{4} [eui]{7} [Liebi]{5,6} [no]{8} [meh]{9} und{10} [meh]{11} [zuenimmt]{12} [a]{13} [Erchänntnis]{14} und{15} [jeder]{16} [Iisicht]{17},",
 "PHP.1.10": "[sodass]{1,2} [ir]{4} [chönd prüefe]{3}, [worum s gaat]{5,6}, [demit]{7} [ir]{8} [luuter]{9} und{10} [ohni Aastoss]{11} [sind]{8} [uf]{12} [de Tag]{13} [vo Christus]{14},",
 "PHP.1.11": "[voll]{1} [vo de Frucht]{2} [vo de Grächtigkeit]{3}, [wo]{4} [dur]{5} Jesus{6} Christus{7} chunnt, [zur]{8} [Ehr]{9} und{10} [zum Lob]{11} [vo Gott]{12}.",
 "PHP.1.12": "[Ich wott]{4} [eu]{3} [aber]{2} [wüsse laa]{1}, [Brüeder und Schwöschtere]{5}, [dass]{6} [das]{7}, [wo]{8} [mich]{9} [betrifft]{8}, [ehner]{10} [zum]{11} [Vorwärtscho]{12} [vom]{13} [Evangelium]{14} [gfüert hät]{15},",
 "PHP.1.13": "[sodass]{1} [im]{9} [ganze]{10} [Prätorium]{11,12} und{13} [bi]{14} [allne]{16} [andere]{15} [bekannt]{5} [worde isch]{8}, dass [ich]{4} [wäge Christus]{6,7} [i Fessle lig]{2,3},",
 "PHP.1.14": "und{1} dass [di meischte]{2,3} [vo de]{4} [Gschwüschterti]{5}, [im]{6} [Herr]{7} [dur]{9} [mini]{11} [Fessle]{10} [ermuetiget]{8}, [sich]{13} [umso meh]{12} [traued]{13}, [s]{15} [Wort]{16} [ohni Angscht]{14} [z säge]{17}.",
 "PHP.1.15": "[Es paar]{1} [verchündiged]{15} [de Christus]{13,14} [zwar]{2} [au]{3} [us]{4} [Niid]{5} und{6} [Striitsucht]{7}, [anderi]{8} [aber]{9} [au]{10} [us]{11} [guetem Wille]{12}.",
 "PHP.1.16": "[Di einte]{1,2} mached s [us]{3} [Liebi]{4}, [wil si wüssed]{5}, [dass]{6} [ich]{11} [zur]{7} [Verteidigung]{8} [vom]{9} [Evangelium]{10} [bestimmt bi]{11};",
 "PHP.1.17": "[di andere]{1,2} [verchündiged]{7} [de Christus]{5,6} [us]{3} [Eigenutz]{4}, [nöd]{8} [ufrichtig]{9}; [si meined]{10}, [si chönnted]{12} [mir]{15} [i de Gfangeschaft]{13,14} [no meh Not]{11} [mache]{12}.",
 "PHP.1.18": "[Was solls]{1,2:idiom}? [Wänn nu]{3,4} [uf jedi]{5} [Art]{6}, [öb]{7} [als Vorwand]{8} [oder]{9} [ehrlich]{10}, [de Christus]{11} [verchündet wird]{12}! Und{13} [drüber]{14,15} [fröi ich mich]{16}. [Ja]{17}, [ich wirde mich]{19} [au]{18} [wiiterhin fröie]{19},",
 "PHP.1.19": "dänn{2} [ich weiss]{1}, [dass]{3} [mir]{5} [das]{4} [zur]{7} [Rettig]{8} [wird]{6} [dur]{9} [eues]{11} [Bätte]{10,12} und{13} [d Unterstützig]{14} [vom]{15} [Geischt]{16} [vo Jesus]{17} [Christus]{18},",
 "PHP.1.20": "[nach]{1} [minere]{6} [sehnsüchtige Erwartig]{2,3} und{4} [Hoffnig]{5}, [dass]{7} [ich]{10} [i]{8} [nüt]{9} [z Schande wirde]{10}, [sondern]{11} dass [mit]{12} [allem]{13} [Freimuet]{14}, [wie]{15} [immer]{16} [so au]{17} [jetzt]{18}, [de Christus]{20} [gross gmacht wird]{19} [a]{21} [mim]{24} [Liib]{22,23}, [sig s]{25} [dur]{26} [s Läbe]{27} [oder]{28} [dur]{29} [de Tod]{30}.",
 "PHP.1.21": "Dänn{2} [für mich]{1} isch [s Läbe]{3,4} [Christus]{5} und{6} [s Sterbe]{7,8} [Gwünn]{9}.",
 "PHP.1.22": "[Wänn]{1} [aber]{2} [s Läbe]{3,4} [im]{5} [Fleisch]{6} – [das]{7} heisst [für mich]{8} [Frucht]{9} [vo de Arbet]{10} –, [dänn]{11} [weiss ich]{15} [nöd]{14}, [was]{12} [ich wääle söll]{13}.",
 "PHP.1.23": "[Ich bi]{1} [aber]{2} [vo]{3} [beidne Siite]{4,5} [hin- und härgrisse]{1}: [Ich ha]{8} [de Wunsch]{6,7}, [ufzbräche]{9-11} und{12} [bi]{13} [Christus]{14} [z sii]{15}, dänn{17} das wär [wiitus]{16,18} [s Besser]{19};",
 "PHP.1.24": "[s]{1} [Bliibe]{3} [im]{4,5} [Fleisch]{6} [aber]{2} isch [wäge eu]{8,9} [nötiger]{7}.",
 "PHP.1.25": "Und{1} [im Vertroue]{3} [druf]{2} [weiss ich]{4}, [dass]{5} [ich bliib]{6} und{7} [bi]{8} [eu]{10} [allne]{9} [usharr]{8}, [zu]{11} [eurem]{13} [Vorwärtscho]{12,14} und{15} [zur Fröid]{16} [im]{17} [Glaube]{18},",
 "PHP.1.26": "[demit]{1} [eues]{4} [Rüeme]{2,3} [in]{6} [Christus Jesus]{7,8} [wäge mir]{9,10} [no grösser wird]{5}, [wänn]{11} [ich]{12,13} [wider]{15} [zu]{16} [eu]{17} [chume]{14}.",
 "PHP.1.27": "Nu{1}: [Läbed als Bürger]{7}, [wie s]{2} [em]{3} [Evangelium]{4} [vo Christus]{5,6} [entspricht]{2}, [demit]{8} ich, [öb]{9} [ich chum]{10} und{11} [eu]{13} [gseh]{12} [oder]{14} [nöd da bi]{15}, [ghör]{16}, [wie s um eu staat]{17-19}: [dass]{20} [ir]{21} [i]{22} [einem]{23} [Geischt]{24} [fescht stönd]{21} und [einmüetig]{25,26} [mitenand kämpfed]{27} [für]{28} [de Glaube]{29} [vom]{30} [Evangelium]{31}",
 "PHP.1.28": "und{1} [eu]{3} [dur nüt]{2,4,5} [vo]{6} [de]{7} [Gägner]{8} [iischüüchtere lönd]{3} – [das]{9} [isch]{10} [für si]{11} [es Zeiche]{12} [für de Undergang]{13}, [aber]{15} [für eui]{14} [Rettig]{16}, [und zwar]{17,18} [vo]{19} [Gott]{20}.",
 "PHP.1.29": "[Dänn]{1} [eu]{2} [isch]{3} [es]{4} [gschänkt worde]{3}, [für]{5} [Christus]{6} – [nöd]{7} [nu]{8} [a]{10} [en]{11} [z glaube]{9,12}, [sondern]{13} [au]{14} [für]{16} [en]{17} [z liide]{15,18} –,",
 "PHP.1.30": "[wil ir]{4} [de gliich]{1,2} [Kampf]{3} [füered]{4}, [wie]{5} [ir en]{6} [a]{7} [mir]{8} [gseh händ]{6} und{9} [jetzt]{10} [vo]{12} [mir]{13} [ghöred]{11}.",
 # ------------------------------------------------------------ Kapitel 2
 "PHP.2.1": "[Wänn s]{1} [also]{3} [irgend e]{2} [Ermuetigung]{4} [in]{5} [Christus]{6} [git]{1}, [wänn]{7} [irgend en]{8} [Zuespruch]{9} [vo de Liebi]{10}, [wänn]{11} [irgend e]{12} [Gmeinschaft]{13} [vom Geischt]{14}, [wänn]{15} [irgendwelchi]{16} [härzlichi Zueneigig]{17} und{18} [Barmhärzigkeit]{19},",
 "PHP.2.2": "[dänn mached]{1} [mini]{2} [Fröid]{3,4} [vollkomme]{1}: [dass]{5} [ir]{8} [s Gliiche]{6,7} [dänked]{8}, [di gliich]{9,10} [Liebi]{11} [händ]{12}, [einmüetig]{13}, [uf s Eint]{14,15} [bedacht]{16}.",
 "PHP.2.3": "[Mached nüt]{1} [us]{2} [Eigenutz]{3} [und au nöd]{4} [us]{5} [eitler Ruemsucht]{6}, [sondern]{7} [i]{8} [Demuet]{9} [achted]{11} [enand]{10} [höcher]{12} [als eu sälber]{13};",
 "PHP.2.4": "[jede]{4} [söll]{5} [nöd]{1} nu [uf s]{2} [Eige]{3} [luege]{5}, [sondern]{6} [jede]{10} [au]{7} [uf das]{8} [vo de andere]{9}.",
 "PHP.2.5": "[Händ]{2} [die]{1} [Gsinnig]{2} [under]{3} [eu]{4}, [wo]{5} [au]{6} [i]{7} [Christus Jesus]{8,9} gsii isch:",
 "PHP.2.6": "[Er]{1}, [obwohl er]{5} [i]{2} [de Gstalt]{3} [vo Gott]{4} [gsii isch]{5}, [hät]{8} [es]{9} [nöd]{6} [für e Büüt]{7} [ghalte]{8}, [Gott]{12} [gliich]{11} [z sii]{10},",
 "PHP.2.7": "[sondern]{1} [er hät]{3} [sich sälber]{2} [läär gmacht]{3}, [hät]{6} [d Gstalt]{4} [vo me Sklav]{5} [aagnoo]{6} [und isch]{10} [de Mänsche]{9} [gliich]{7,8} [worde]{10}. Und{11} [wo er]{13} [im Uusgseh]{12} [wie]{14} [en Mänsch]{15} [gsii isch]{13},",
 "PHP.2.8": "[hät er]{1} [sich sälber]{2} [erniedriget]{1} [und isch]{3} [ghorsam]{4} [worde]{3} [bis]{5} [in Tod]{6}, [ja]{8} [in Tod]{7} [am Chrüüz]{9}.",
 "PHP.2.9": "[Drum]{1} [hät]{6} [Gott]{3,4} [en]{5} [au]{2} [über alles erhöht]{6} und{7} [em]{9} [de Name]{10,11} [gschänkt]{8}, [wo]{12} [über]{13} [jedem]{14} [Name]{15} staat,",
 "PHP.2.10": "[demit]{1} [im]{2,3} [Name]{4} [vo Jesus]{5} [jedes]{6} [Chnüü]{7} [sich böigt]{8}, [im Himmel]{9} und{10} [uf de Erde]{11} und{12} [under de Erde]{13},",
 "PHP.2.11": "und{1} [jedi]{2} [Zunge]{3} [bekännt]{4}, [dass]{5} Jesus{7} Christus{8} [de Herr]{6} isch, [zur]{9} [Ehr]{10} [vo Gott]{11}, [em Vatter]{12}.",
 "PHP.2.12": "[Drum]{1}, [mini]{3} [Liebe]{2}, [wie]{4} [ir]{6} [immer]{5} [ghorsam gsii sind]{6}, [nöd]{7} [nu]{13} [wie]{8} [wänn ich]{12} [da bi]{9-11}, [sondern]{14} [jetzt]{15} [vil]{16} [meh]{17}, [wo ich]{21} [nöd da bi]{18-20}: [Mit]{22} [Furcht]{23} und{24} [Zittere]{25} [schaffed]{29} [a eurer]{27} [Rettig]{26,28}.",
 "PHP.2.13": "Dänn{2} Gott{1} isch{3} es, [wo]{4} [i]{6} [eu]{7} [würkt]{5}: [sowohl]{8} [s Wele]{9,10} [als au]{11} [s Vollbringe]{12,13}, [zu]{14} [sim]{15} [Wohlgfalle]{16}.",
 "PHP.2.14": "[Mached]{2} [alles]{1} [ohni]{3} [Muule]{4} und{5} [Widerred]{6},",
 "PHP.2.15": "[demit]{1} [ir]{2} [untadelig]{3} und{4} [luuter]{5} [wärded]{2}, [makellosi]{8} [Chind]{6} [vo Gott]{7} [mitts i]{9} ere [chrumme]{11} und{12} [verdreite]{13} [Generation]{10}, [wo]{14,15} [ir]{16} [lüüchted]{16} [wie]{17} [Liechter]{18} [i]{19} [de Wält]{20}",
 "PHP.2.16": "[indem ir]{3} [am Wort]{1} [vom Läbe]{2} [fescht hebed]{3}, [mir]{6} [zum]{4} [Rueme]{5} [uf]{7} [de Tag]{8} [vo Christus]{9}, [dass]{10} [ich]{14} [nöd]{11} [vergäbe]{12,13} [grännt bi]{14} [und au nöd]{15} [vergäbe]{16,17} [gschaffet ha]{18}.",
 "PHP.2.17": "[Aber]{1} [sogar wänn]{2,3} [ich als Trankopfer usgschüttet wirde]{4} [über]{5} [em]{6} [Opfer]{7} und{8} [Gottesdienscht]{9} [vo eurem]{12} [Glaube]{10,11}, [fröi ich mich]{13} und{14} [fröi mich mit]{15} [eu]{17} [allne]{16}.",
 "PHP.2.18": "[Gnau so]{1,3} [aber]{2} [fröied]{6} [au]{4} [ir]{5} [eu]{6} und{7} [fröied eu mit]{8} [mir]{9}!",
 "PHP.2.19": "[Ich hoff]{1} [aber]{2} [im]{3} [Herr]{4} Jesus{5}, [de Timotheus]{6} [bald]{7} [zu eu]{9} [z schicke]{8}, [demit]{10} [au ich]{11} [Muet überchum]{12}, [wänn ich erfahr]{13}, [wie s um eu staat]{14-16}.",
 "PHP.2.20": "Dänn{2} [ich ha]{3} [kein]{1} [Gliichgsinnte]{4}, [wo]{5} [sich]{10} [so ufrichtig]{6} [um]{7,8} [eu]{9} [chümmere wird]{10};",
 "PHP.2.21": "dänn{3} [alli]{1,2} [sueched]{6} [s Eige]{4,5}, [nöd]{7} [das]{8}, [wo em Jesus Christus ghört]{9,10}.",
 "PHP.2.22": "[Ir känned]{5} [aber]{2} [sini]{4} [Bewährig]{1,3}: [dass]{6} er [wie]{7} [es Chind]{9} [em Vatter]{8} [mit]{10} [mir]{11} [für]{13} [s]{14} [Evangelium]{15} [dienet hät]{12}.",
 "PHP.2.23": "[Dä]{1} [hoff ich]{4} [also]{3} [grad]{12} [z schicke]{5}, [sobald]{6,7} [ich gseh]{8}, [wie s um mich staat]{9-11}. ~2(μέν bereitet de Gägesatz zu [[PHP.2.24]] vor; nöd eigens widergää)",
 "PHP.2.24": "[Ich vertroue]{1} [aber]{2} [im]{3} [Herr]{4} druf, [dass]{5} [au]{6} [ich sälber]{7} [bald]{8} [chume]{9}.",
 "PHP.2.25": "[Ich ha s]{3} [aber]{2} [für nötig]{1} [ghalte]{3}, [de Epaphroditus]{4}, [min]{11} [Brueder]{5,6} und{7} [Mitarbeiter]{8} und{9} [Mitstriiter]{10}, [aber]{13} [eue]{12} [Gsandte]{14} und{15} [Diener]{16} [für]{17} [das, wo ich]{19} [bruuch]{18}, [zu eu]{21,22} [z schicke]{20},",
 "PHP.2.26": "[dänn]{1} [er hät]{3} [Sehnsucht gha]{2} [nach eu]{5} [allne]{4} und{6} [isch ganz unruehig gsii]{7}, [wil]{8} [ir ghört händ]{9}, [dass]{10} [er chrank gsii isch]{11}.",
 "PHP.2.27": "[Er isch]{3} [ja]{2} [au]{1} [chrank gsii]{3}, [nooch]{4} [am Tod]{5}. [Aber]{6} [Gott]{7,8} [hät sich]{9} [über en]{10} [erbarmet]{9}, [und]{13} [nöd]{11} [nu]{14} [über en]{12}, [sondern]{15} [au]{16} [über mich]{17}, [demit]{18} [ich]{23} [nöd]{19} [Truur]{20} [uf]{21} [Truur]{22} [ha]{23}.",
 "PHP.2.28": "[Drum]{2} [schick ich]{3} [en]{4} [umso schnäller]{1}, [demit]{5} [ir eu]{9}, [wänn ir]{6} [en]{7} [wider]{8} [gsehnd]{6}, [fröied]{9} [und ich]{10} [weniger Chummer]{11} [ha]{12}.",
 "PHP.2.29": "[Nämed]{1} [en]{3} [also]{2} [uf]{1} [im]{4} [Herr]{5} [mit]{6} [voller]{7} [Fröid]{8}, und{9} [händ]{13} [settigi]{10,11} [in Ehre]{12};",
 "PHP.2.30": "[dänn]{1} [wäge]{2} [em]{3} [Wärch]{4} [vo Christus]{5} [isch er]{8} [bis a]{6} [de Tod]{7} [anecho]{8} [und hät]{9} [sis Läbe]{10,11} [ufs Spiel gsetzt]{9}, [zum]{12} [uuszfülle]{13}, [was]{14} [eu]{15} [bim]{17} [Dienscht]{20} [für]{18} [mich]{19} [no gfäält hät]{16}.",
 # ------------------------------------------------------------ Kapitel 3
 "PHP.3.1": "[Im Übrige]{1,2}, [mini]{4} [Brüeder und Schwöschtere]{3}: [Fröied eu]{5} [im]{6} [Herr]{7}! [Eu]{11} [s Gliiche]{8,9} [z schriibe]{10}, isch [mir]{12} [zwar]{13} [nöd]{14} [lästig]{15}, [eu]{16} [aber]{17} [git s Sicherheit]{18}.",
 "PHP.3.2": "[Passed uf]{1} [d]{2} [Hünd]{3} [uf]{1}, [passed uf]{4} [di]{5} [schlächte]{6} [Arbeiter]{7} [uf]{4}, [passed uf]{8} [d]{9} [Zerschniidig]{10} [uf]{8}!",
 "PHP.3.3": "Dänn{2} [mir]{1} [sind]{3} [d]{4} [Beschniidig]{5}, [mir, wo]{6} [im Geischt]{7} [vo Gott]{8} [diened]{9} und{10} [üs]{11} [in]{12} [Christus Jesus]{13,14} [rüemed]{11} und{15} [nöd]{16} [uf]{17} [s Fleisch]{18} [vertroued]{19},",
 "PHP.3.4": "[obwohl]{1} [ich]{2} [au]{5} [im]{6} [Fleisch]{7} [Grund zum Vertroue]{4} [hett]{3}. [Wänn]{8} [irgend en]{9} [andere]{11} [meint]{10}, [er chönn]{12} [uf]{13} [s Fleisch]{14} [vertroue]{12}, [dänn ich]{15} [no meh]{16}:",
 "PHP.3.5": "[beschnitte]{1} [am achte Tag]{2}, [us]{3} [em Volk]{4} [Israel]{5}, [vom Stamm]{6} [Benjamin]{7}, [Hebräer]{8} [vo]{9} [Hebräer]{10}, [was s]{11} [Gsetz]{12} [aagaat]{11}, [Pharisäer]{13},",
 "PHP.3.6": "[was]{1} [de Iifer]{2} [aagaat]{1}, [en Verfolger]{3} [vo de]{4} [Gmeind]{5}, [was]{6} [d Grächtigkeit]{7} [aagaat]{6}, [wo]{8} [im]{9} [Gsetz]{10} gilt, [untadelig]{12} [gsii]{11}.",
 "PHP.3.7": "[Aber]{1} [was]{2} [mir]{4} [Gwünn]{5} [gsii isch]{3}, [das]{6} [han ich]{7} [wäge]{8} [Christus]{9,10} [für Verluscht]{11} [ghalte]{7}.",
 "PHP.3.8": "[Ja]{1}, [no meh]{2}: [Ich halt]{4} [au]{3} [alles]{5} [für Verluscht]{6,7} [wäge]{8} [em Überragende]{9,10} [vo de]{11} [Erchänntnis]{12} [vo Christus Jesus]{13,14}, [mim]{17} [Herr]{15,16}. [Wäge ihm]{18,19} [han ich]{22} [alles]{20,21} [verlore]{22} und{23} [halt s]{24} [für Dräck]{25}, [demit]{26} [ich]{28} [Christus]{27} [gwünn]{28}",
 "PHP.3.9": "und{1} [in]{3} [ihm]{4} [gfunde wirde]{2}, [indem ich]{6} [nöd]{5} [mini]{7} [Grächtigkeit]{8} [ha]{6} – [die]{9} [us]{10} [em Gsetz]{11} –, [sondern]{12} [die]{13} [dur]{14} [de Glaube a Christus]{15,16}, [d]{17} [Grächtigkeit]{20} [us]{18} [Gott]{19} [uf Grund]{21} [vom]{22} [Glaube]{23},",
 "PHP.3.10": "[zum]{1} [en]{3} [z erchänne]{2} und{4} [d]{5} [Chraft]{6} [vo sinere]{7,9} [Uferstehig]{8} und{10} [d Gmeinschaft]{11} [mit sine]{13} [Liide]{12}, [indem ich]{14} [sim]{15,17} [Tod]{16} [gliichgstaltet wirde]{14},",
 "PHP.3.11": "[öb ich]{1} [irgendwie]{2} [zur]{4,5} [Uferstehig]{6} [us]{7,8} [de Tote]{9} [chume]{3}.",
 "PHP.3.12": "[Nöd]{1}, [dass]{2} [ich s]{4} [scho]{3} [erreicht hett]{4} [oder]{5} [scho]{6} [vollkomme wär]{7}; [ich jag]{8} [aber]{9} [dem nache]{8}, [öb ich s]{10} [au]{11} [packe]{12}, [wil]{13,14} [ich]{16} [au]{15} [vo]{17} [Christus]{18} [packt worde bi]{16}.",
 "PHP.3.13": "[Brüeder und Schwöschtere]{1}, [ich]{2} [mein]{5} [vo mir sälber]{3} [nöd]{4}, [dass ich s packt heig]{6}. [Eis]{7} [aber]{8}: [Ich vergiss]{12}, [was]{9,10} [hinder mir]{11} liit, [und]{14} [streck mich]{16} [nach dem]{13} [us]{16}, [was vor mir]{15} liit,",
 "PHP.3.14": "[uf s Ziil zue]{1,2} [jag ich]{3} [zum]{4,5} [Siegerpriis]{6} [vo de]{7} [himmlische]{8} [Beruefig]{9} [vo Gott]{10,11} [in]{12} [Christus Jesus]{13,14}.",
 "PHP.3.15": "[Mir alli]{1} [also]{2}, [wo]{1} [riif]{3} sind, [wänd]{5} [so]{4} [dänke]{5}; und{6} [wänn]{7} [ir]{10} [i irgendöppisem]{8} [anders]{9} [dänked]{10}, [wird]{16} [Gott]{13,14} [eu]{15} [au]{11} [das]{12} [offebare]{16}.",
 "PHP.3.16": "Nu{1}: [Wo]{2,3} [mir aacho sind]{4}, [uf de gliiche Linie]{5,6} [wämer wiitergaa]{7}.",
 "PHP.3.17": "[Wärded]{3} [mitenand]{1} [mini]{2} [Nachahmer]{1}, [Brüeder und Schwöschtere]{4}, und{5} [lueged uf]{6} [die]{7}, wo [eso]{8} [läbed]{9}, [wie]{10} [ir]{11} [üs]{13} [als Vorbild]{12} [händ]{11}.",
 "PHP.3.18": "Dänn{2} [vili]{1} [läbed]{3} – [vo dene]{4} han ich [eu]{7} [oft]{5} [gseit]{6}, [und]{9} [jetzt]{8} [säg ich s]{12} [au]{10} [mit Träne]{11} – [als]{13} [d Find]{14} [vom]{15} [Chrüüz]{16} [vo Christus]{17,18}.",
 "PHP.3.19": "[Ires]{1} [Änd]{2,3} isch [Verderbe]{4}, [ire]{5} [Gott]{6,7} [de Buuch]{8,9} und{10} [ires Aasee]{11,12} [i]{13} [irer]{16} [Schand]{14,15}; [si]{17} sind [uf s Irdische]{18,19} [uus]{20}.",
 "PHP.3.20": "Dänn{2} [öises]{1} [Bürgerrächt]{3,4} [isch]{7} [im]{5} [Himmel]{6}, [vo]{8} [wo]{9} [mir]{12} [au]{10} [de Retter]{11} [erwarted]{12}, [de Herr]{13} [Jesus Christus]{14,15},",
 "PHP.3.21": "[wo]{1} [öise]{7} [armselige]{5,6} [Liib]{3,4} [verwandle wird]{2}, [gliichgstaltet]{8} [wie sin]{13} [herrliche]{11,12} [Liib]{9,10}, [nach]{14} [de]{15} [Chraft]{16}, [mit dere]{17} [er]{19} [fähig isch]{18}, [sich]{22} [au]{20} [alles]{23,24} [z underwerfe]{21}.",
 # ------------------------------------------------------------ Kapitel 4
 "PHP.4.1": "[Drum]{1}, [mini]{3} [gliebte]{4} und{5} [ersehnte]{6} [Brüeder und Schwöschtere]{2}, [mini]{10} [Fröid]{7} und{8} min [Siegerchranz]{9}: [So]{11} [stönd fescht]{12} [im]{13} [Herr]{14}, [ir Liebe]{15}!",
 "PHP.4.2": "[D Euodia]{1} [bitt ich]{2}, und{3} [d Syntyche]{4} [bitt ich]{5}, [einig z sii]{6-8} [im]{9} [Herr]{10}.",
 "PHP.4.3": "[Ja]{1}, [ich bitt]{2} [au]{3} [dich]{4}, [tröie]{5} [Gfährte]{6}: [Hilf]{7} [ine]{8}! [Si]{9} [händ]{13} [im]{10,11} [Evangelium]{12} [mit mir]{14} [kämpft]{13}, [zäme]{15} [sowohl mit]{16} [em Klemens]{17} [als au mit]{18} [mine]{22} [andere]{19,20} [Mitarbeiter]{21}, [wo]{23} iri [Näme]{24,25} [im]{26} [Buech]{27} [vom Läbe]{28} stönd.",
 "PHP.4.4": "[Fröied eu]{1} [immer]{4} [im]{2} [Herr]{3}! [No einisch]{5} [säg ich]{6}: [Fröied eu]{7}!",
 "PHP.4.5": "[Eui]{3} [Güeti]{1,2} [söll]{4} [allne]{5} [Mänsche]{6} [bekannt wärde]{4}. [De]{7} [Herr]{8} [isch nooch]{9}.",
 "PHP.4.6": "[Mached eu]{2} [kei Sorge]{1}, [sondern]{3} [i]{4} [allem]{5} [bringed]{16} [eui]{15} [Aaliige]{13,14} [dur]{6} [Bätte]{7} und{8} [Flehe]{9,10} [mit]{11} [Dank]{12} [vor]{17} [Gott]{18,19}.",
 "PHP.4.7": "Und{1} [de]{2} [Fride]{3} [vo Gott]{4,5}, [wo]{6} [jede]{8} [Verstand]{9} [übersteigt]{7}, [wird]{10} [eui]{13} [Härze]{11,12} und{14} [eui]{17} [Gedanke]{15,16} [bewache]{10} [in]{18} [Christus Jesus]{19,20}.",
 "PHP.4.8": "[Im Übrige]{1,2}, [Brüeder und Schwöschtere]{3}: [Was]{4} [wahr]{6} [isch]{5}, [was]{7} [ehrbar]{8}, [was]{9} [grächt]{10}, [was]{11} [rein]{12}, [was]{13} [liebenswärt]{14}, [was]{15} [en guete Ruef hät]{16}, [wänn s]{17} [irgend e]{18} [Tugend]{19} [git]{17} und{20} [wänn s]{21} [irgend es]{22} [Lob]{23} [git]{21}: [das]{24} [bedänked]{25}!",
 "PHP.4.9": "[Was]{1} ir [au]{2} [glernt]{3} und{4} [übercho]{5} und{6} [ghört]{7} und{8} [gseh händ]{9} [a]{10} [mir]{11}, [das]{12} [tüend]{13}! Und{14} [de]{15} [Gott]{16} [vom]{17} [Fride]{18} [wird]{19} [mit]{20} [eu]{21} [sii]{19}.",
 "PHP.4.10": "[Ich ha mich]{1} [aber]{2} [im]{3} [Herr]{4} [fescht]{5} [gfröit]{1}, [dass]{6} [ir]{9} [ändlich]{7,8} [wider ufblüet sind]{9}, [für]{11} [mich]{12} [z sorge]{10,13}. [Ir händ]{17} [au]{16} [dra]{14,15} [dänkt]{17}, [aber]{19} [es hät eu d Glägeheit gfäält]{18}.",
 "PHP.4.11": "[Nöd]{1}, [dass]{2} ich das [wäge]{3} [Mangel]{4} [säg]{5}; dänn{7} [ich]{6} [ha glernt]{8}, [mir sälber z gnüege]{12,13}, [wo]{9,10} [ich au bi]{11}.",
 "PHP.4.12": "[Ich cha]{1} [mich]{3} [au]{2} [iischränke]{3}, [ich chan]{4} [au]{5} [im Überfluss läbe]{6}; [i]{7} [allem]{8} und{9} [i]{10} [jedem]{11} [bi ich iigweiht]{12}: [sowohl]{13} [satt z sii]{14} [als au]{15} [z hungere]{16}, [sowohl]{17} [Überfluss z haa]{18} [als au]{19} [Mangel z liide]{20}.",
 "PHP.4.13": "[Alles]{1} [chan ich]{2} [dur]{3} [dä]{4}, wo [mich]{6} [starch macht]{5}.",
 "PHP.4.14": "[Aber]{1} [ir händ]{3} [guet]{2} [dra taa]{3}, [a]{6} [minere]{5} [Not]{7} [Aateil z nää]{4}.",
 "PHP.4.15": "[Ir wüssed]{1} [aber]{2} [au]{3} [sälber]{4}, [ir Philipper]{5}, [dass]{6} [am]{7} [Aafang]{8} [vom]{9} [Evangelium]{10}, [wo]{11} ich [vo]{13} [Mazedonie]{14} [ufbroche bi]{12}, [kei]{15} [Gmeind]{17} [mit mir]{16} [Gmeinschaft gha hät]{18} [uf d Rächnig]{19,20} [vo Gää]{21} und{22} [Nää]{23} [usser]{24,25} [ir]{26} [ellei]{27}.",
 "PHP.4.16": "[Dänn]{1} [au]{2} [z]{3} [Thessalonich]{4} [händ ir]{13} [mir]{12} [meh als einisch]{5-8:idiom} öppis [für]{9} [das]{10}, [wo ich bruucht ha]{11}, [gschickt]{13}.",
 "PHP.4.17": "[Nöd]{1}, [dass]{2} ich [uf s Gschänk]{4,5} [uus wär]{3}; [sondern]{6} [ich bi uus uf]{7} [d]{8} [Frucht]{9}, [wo]{10} [sich]{11} [uf]{12} [eurem]{14} [Konto]{13} [vermeert]{11}.",
 "PHP.4.18": "[Ich ha]{1} [aber]{2} [alles]{3} [übercho]{1} und{4} [ha meh als gnueg]{5}. [Ich ha alles, was ich bruuch]{6}, [sit ich]{7} [vom]{8} [Epaphroditus]{9} [eui Gabe]{10-12} [übercho ha]{7}: [en Duft]{13}, [wo guet schmöckt]{14}, [es Opfer]{15}, [aagnää]{16}, [wo Gott]{18,19} [gfallt]{17}.",
 "PHP.4.19": "[Min]{4} [Gott]{1,3} [aber]{2} [wird]{5} [jede]{6} [Bedarf]{7} [vo eu]{8} [decke]{5} [nach]{9} [sim]{12} [Riichtum]{10,11} [i]{13} [Herrlichkeit]{14} [in]{15} [Christus Jesus]{16,17}.",
 "PHP.4.20": "[Öisem]{6} [Gott]{1,3} und{4} [Vatter]{5} [aber]{2} ghört [d]{7} [Ehr]{8} [i]{9} [alli Ewigkeit]{10-13}. [Amen]{14}.",
 "PHP.4.21": "[Grüessed]{1} [jede]{2} [Heilige]{3} [in]{4} [Christus Jesus]{5,6}. [Es grüessed]{7} [eu]{8} [d]{9} [Gschwüschterti]{12}, wo [bi]{10} [mir]{11} sind.",
 "PHP.4.22": "[Es grüessed]{1} [eu]{2} [alli]{3} [Heilige]{4,5}, [bsunders]{6} [aber]{7} [die]{8} [us]{9} [em]{10} [Huus]{12} [vom Kaiser]{11}.",
 "PHP.4.23": "[D]{1} [Gnad]{2} [vom]{3} [Herr]{4} [Jesus Christus]{5,6} sig [mit]{7} [eurem]{10} [Geischt]{8,9}!",
}

# Übersetzungsentscheidungen: (Stelle, Zieltext, Art, griechisch, wörtlicher, andere Möglichkeiten, Begründung)
DEC_DE = [
 ("PHP.1.1", "Knechte", "traditional", "δοῦλοι", "Sklaven", ["Diener"], "δοῦλος heisst wörtlich «Sklave». Als Selbstbezeichnung meint es Menschen, die ganz Christus gehören; «Knecht» folgt der vertrauten Wiedergabe. In [[PHP.2.7]] wird dasselbe Wort für Christus selbst mit «Sklave» übersetzt, damit der Kontrast zur «Gestalt Gottes» hörbar bleibt."),
 ("PHP.1.1", "Aufsehern und Diakonen", "interpretive", "ἐπισκόποις καὶ διακόνοις", "Aufsehern und Dienern", ["Bischöfen und Diakonen", "Gemeindeleitern und Helfern"], "Aus ἐπίσκοπος entstand «Bischof», aus διάκονος «Diakon». Ein dreistufiges Amt (Bischof, Priester, Diakon) ist hier noch nicht vorausgesetzt; der Plural zeigt mehrere Aufseher in einer Gemeinde. Was die beiden Gruppen genau taten, sagt der Brief nicht."),
 ("PHP.1.5", "Gemeinschaft im Dienst am", "interpretive", "κοινωνίᾳ εἰς", "Gemeinschaft für", ["Teilhabe am", "Partnerschaft für", "Mitwirkung am"], "κοινωνία ist Gemeinschaft durch Teilhabe. Die Philipper waren am Evangelium beteiligt, auch mit Geld (vgl. [[PHP.4.15]], wo dasselbe Verb für Geben und Nehmen steht). «im Dienst am» verdeutlicht εἰς («hin zu, für»)."),
 ("PHP.1.8", "der innigen Liebe", "interpretive", "σπλάγχνοις", "den Eingeweiden", ["dem Herzen", "dem Erbarmen"], "σπλάγχνα sind die Eingeweide, damals Sitz der tiefen Gefühle; deutsch entspricht eher «Herz»."),
 ("PHP.1.12", "Brüder und Schwestern", "interpretive", "ἀδελφοί", "Brüder", ["Geschwister", "liebe Freunde"], "Der griechische Plural ἀδελφοί schliesst Frauen ein; in Philippi gehören Frauen ausdrücklich zur Gemeinde (vgl. [[PHP.4.2]]). Ebenso in [[PHP.3.1]], [[PHP.3.13]], [[PHP.3.17]], [[PHP.4.1]], [[PHP.4.8]]; ohne Anrede «Geschwister»."),
 ("PHP.1.13", "Prätorium", "literal", "πραιτωρίῳ", None, ["kaiserliche Garde", "Amtssitz des Statthalters"], "πραιτώριον kann die Prätorianergarde in Rom oder den Amtssitz eines Statthalters in einer Provinz bezeichnen. Davon hängt ab, wo Paulus gefangen war (Rom, Ephesus oder Cäsarea); das ist umstritten."),
 ("PHP.1.17", "Eigennutz", "interpretive", "ἐριθείας", None, ["Rivalität", "Parteigeist", "Ehrgeiz"], "ἐριθεία meint selbstsüchtiges Streben, oft mit Parteibildung; ebenso in [[PHP.2.3]]."),
 ("PHP.1.19", "Rettung", "interpretive", "σωτηρίαν", None, ["Befreiung", "Heil"], "Der Wortlaut nimmt [[JOB.13.16]] (griechische Fassung) auf. Gemeint sein kann die Freilassung aus der Haft oder die endgültige Rettung vor Gott; der folgende Vers («durch Leben oder durch Tod») spricht eher für Letzteres."),
 ("PHP.1.20", "Freimut", "literal", "παρρησίᾳ", None, ["Offenheit", "Unerschrockenheit"], "παρρησία ist das freie, offene Reden ohne Furcht, ursprünglich das Recht des Bürgers in der Volksversammlung."),
 ("PHP.1.21", "das Leben Christus", "literal", "τὸ ζῆν Χριστὸς", None, ["mein Leben gehört Christus", "Leben heisst für mich Christus"], "Der knappe Satz hat kein Verb. Wörtlich belassen, damit die Spannung zwischen «Leben» und «Sterben» erhalten bleibt; gemeint ist, dass Christus Inhalt und Ziel des Lebens ist."),
 ("PHP.1.22", "Fleisch", "literal", "σαρκί", None, ["Körper", "irdischen Leben"], "σάρξ steht hier nicht für Sünde, sondern für das leibliche, irdische Leben."),
 ("PHP.1.22", "weiss ich", "interpretive", "γνωρίζω", "tue ich kund", ["sage ich"], "γνωρίζω heisst sonst «bekannt machen»; hier vermutlich: Ich kann es nicht sagen."),
 ("PHP.1.23", "aufzubrechen", "literal", "ἀναλῦσαι", "aufzulösen", ["zu sterben", "abzuscheiden"], "ἀναλύειν heisst losbinden, das Lager abbrechen, ein Schiff losmachen; ein Bild für das Sterben."),
 ("PHP.1.27", "Lebt als Bürger", "interpretive", "πολιτεύεσθε", "Führt euer Bürgerleben", ["Führt euer Leben", "Lebt als Gemeinschaft"], "πολιτεύεσθαι heisst «als Bürger (einer Polis) leben». Philippi war römische Kolonie, auf das Bürgerrecht stolz; Paulus nimmt das auf und spricht in [[PHP.3.20]] vom Bürgerrecht im Himmel."),
 ("PHP.1.27", "einmütig", "adapted", "μιᾷ ψυχῇ", "mit einer Seele", None, "ψυχή ist hier das Innere, der Wille; «einmütig» gibt den Sinn wieder."),
 ("PHP.2.1", "Gemeinschaft des Geistes", "literal", "κοινωνία πνεύματος", None, ["Gemeinschaft im Geist", "Teilhabe am Geist"], "Der Genitiv kann die Gemeinschaft meinen, die der Geist schafft, oder die Teilhabe am Geist."),
 ("PHP.2.2", "dasselbe denkt", "literal", "τὸ αὐτὸ φρονῆτε", None, ["gleich gesinnt seid", "auf dasselbe aus seid"], "φρονεῖν (denken, gesinnt sein, auf etwas aus sein) ist ein Leitwort des Briefes (vgl. [[PHP.2.5]], [[PHP.3.15]], [[PHP.4.2]]). Es meint nicht Meinungsgleichheit, sondern eine gemeinsame Ausrichtung."),
 ("PHP.2.3", "Demut", "literal", "ταπεινοφροσύνῃ", None, ["Bescheidenheit", "Niedriggesinntheit"], "In der griechischen Umwelt meist abwertend (die Haltung der Niedrigen); im frühen Christentum aufgewertet. Vgl. [[PHP.2.8]]: Christus «erniedrigte sich»."),
 ("PHP.2.5", "die auch in Christus Jesus war", "interpretive", "ὃ καὶ ἐν Χριστῷ Ἰησοῦ", "die auch in Christus Jesus", ["wie es sich für die gehört, die in Christus Jesus sind"], "Der Nebensatz hat kein Verb. Ergänzt man «war», ist Christus Vorbild; ergänzt man «euch geziemt», ist die Gemeinschaft «in Christus» der Massstab. Beides wird vertreten."),
 ("PHP.2.6", "Gestalt", "literal", "μορφῇ", None, ["Wesen", "Daseinsweise", "Erscheinungsform"], "μορφή ist die Gestalt, in der etwas erscheint und ist. Der Hymnus stellt «Gestalt Gottes» und «Gestalt eines Sklaven» ([[PHP.2.7]]) gegeneinander."),
 ("PHP.2.6", "für ein Beutestück", "interpretive", "ἁρπαγμὸν", "für einen Raub", ["für etwas, das er an sich reissen müsste", "für etwas, das er festhalten oder ausnützen müsste"], "ἁρπαγμός ist sonst kaum belegt. Drei Deutungen: etwas, das er unrechtmässig erst rauben müsste; etwas, das er gewaltsam festhält; oder ein Vorrecht, das man zum eigenen Vorteil ausnützt. Die letzte wird heute oft vertreten; «Beutestück» lässt die Frage offen."),
 ("PHP.2.7", "entäusserte", "traditional", "ἐκένωσεν", "leerte", ["machte sich arm", "gab alles auf", "verzichtete auf alles"], "κενόω heisst «leer machen». Worauf Christus verzichtete, sagt der Text nicht; die folgenden Partizipien (nahm an, wurde gleich) erklären es als Annahme der Sklavengestalt. «Entäussern» folgt der vertrauten Wiedergabe."),
 ("PHP.2.7", "eines Sklaven", "literal", "δούλου", None, ["eines Knechts", "eines Dieners"], "Hier bewusst «Sklave»: Der Gegensatz zur «Gestalt Gottes» ist schroff; der Sklave war rechtlos, der Kreuzestod ([[PHP.2.8]]) eine Sklavenstrafe."),
 ("PHP.2.9", "über alles erhöht", "interpretive", "ὑπερύψωσεν", "übererhöht", ["hoch erhöht", "aufs Höchste erhöht"], "Das zusammengesetzte Verb (ὑπέρ + ὑψόω) steigert; es kann die höchste Stellung oder die Erhöhung über alles bezeichnen."),
 ("PHP.2.11", "der Herr", "literal", "κύριος", None, ["Herr (als Gottesname)"], "[[PHP.2.10-PHP.2.11]] nehmen [[ISA.45.23]] auf, wo Gott spricht: «Mir wird sich jedes Knie beugen.» κύριος steht in der griechischen Bibel für den Gottesnamen; der Hymnus legt Jesus damit den Namen Gottes bei."),
 ("PHP.2.12", "wirkt", "interpretive", "κατεργάζεσθε", "erarbeitet", ["arbeitet an", "verwirklicht", "bringt zur Vollendung"], "κατεργάζεσθαι heisst bewirken, vollbringen. Gemeint ist nicht, dass man sich Rettung verdient: [[PHP.2.13]] begründet, dass Gott das Wollen und Vollbringen wirkt. Die Anrede ist Plural; manche denken an das Wohl der Gemeinschaft."),
 ("PHP.2.15", "Lichter", "literal", "φωστῆρες", None, ["Sterne", "Himmelslichter"], "φωστήρ bezeichnet Himmelskörper; Anklang an [[DAN.12.3]]."),
 ("PHP.2.16", "festhaltet", "interpretive", "ἐπέχοντες", None, ["darbietet", "hochhaltet"], "ἐπέχειν kann «festhalten» oder «darreichen, vorhalten» heissen; je nachdem geht es um Treue oder um Zeugnis nach aussen."),
 ("PHP.2.17", "ich als Trankopfer ausgegossen werde", "literal", "σπένδομαι", None, ["mein Leben hingegeben wird"], "Bild aus dem Opferkult: Wein wurde über oder neben das Opfer gegossen. Paulus deutet damit seinen möglichen Tod."),
 ("PHP.2.25", "Gesandten", "interpretive", "ἀπόστολον", "Apostel", ["Abgesandten", "Boten"], "ἀπόστολος heisst «Gesandter». Hier ist nicht der Kreis der Apostel gemeint, sondern der Beauftragte der Gemeinde, der Paulus die Gabe brachte."),
 ("PHP.3.2", "Hunde", "literal", "κύνας", None, None, "Hunde galten als unrein; «Hund» war Schimpfwort, auch für Nichtjuden. Paulus kehrt das gegen Leute, die auf die Beschneidung drängen. Wen er genau meint, ist umstritten."),
 ("PHP.3.2", "Zerschneidung", "literal", "κατατομήν", None, ["Verstümmelung", "Zerschnittene"], "Wortspiel: κατατομή (Zerschneidung) gegen περιτομή (Beschneidung, [[PHP.3.3]]). Die Schärfe ist gewollt."),
 ("PHP.3.6", "Gemeinde", "literal", "ἐκκλησίαν", None, ["Kirche", "Versammlung"], "ἐκκλησία ist die Versammlung; im Neuen Testament die Gemeinde der Glaubenden."),
 ("PHP.3.8", "Dreck", "interpretive", "σκύβαλα", "Kot", ["Unrat", "Abfall", "Mist"], "σκύβαλον bezeichnet Abfall, Speisereste oder Kot. Das Wort ist derb; «Dreck» hält die Schärfe, ohne eine der Bedeutungen festzulegen."),
 ("PHP.3.9", "den Glauben an Christus", "interpretive", "πίστεως Χριστοῦ", "den Glauben Christi", ["die Treue Christi"], "Der Genitiv kann objektiv (Glaube an Christus) oder subjektiv (Glaube bzw. Treue Christi) verstanden werden. Für die Treue Christi spricht, dass der Glaube des Menschen am Versende eigens genannt wird; für den Glauben an Christus der Sprachgebrauch in [[PHP.1.29]] und [[GAL.2.16]]. Die Wahl ist eine redaktionelle Entscheidung; beide Deutungen haben gewichtige Vertreter."),
 ("PHP.3.10", "Gemeinschaft", "literal", "κοινωνίαν", None, ["Teilhabe"], "Dasselbe Wort wie in [[PHP.1.5]]: Teilhabe an den Leiden Christi."),
 ("PHP.3.12", "weil", "interpretive", "ἐφʼ ᾧ", None, ["wozu", "dafür dass"], "ἐφʼ ᾧ kann begründen («weil») oder ein Ziel angeben («wozu ich auch ergriffen bin»)."),
 ("PHP.3.14", "himmlischen", "interpretive", "ἄνω", "nach oben", ["von oben"], "ἄνω κλῆσις kann die Berufung «nach oben» (in den Himmel) oder die Berufung «von oben» (durch Gott) meinen."),
 ("PHP.3.15", "reif", "interpretive", "τέλειοι", "vollkommen", ["mündig", "erwachsen"], "τέλειος heisst vollkommen oder ausgewachsen, mündig. Nach [[PHP.3.12]] («nicht, dass ich schon vollendet wäre») vielleicht ironisch gegen Leute, die sich für vollkommen hielten."),
 ("PHP.3.19", "der Bauch", "literal", "κοιλία", None, ["die Begierde"], "Gemeint sein kann Genusssucht, Selbstsucht allgemein oder (polemisch) das Festhalten an Speisegeboten. Die Deutung hängt davon ab, wer gemeint ist."),
 ("PHP.3.20", "Bürgerrecht", "interpretive", "πολίτευμα", None, ["Gemeinwesen", "Heimat", "Staatswesen"], "πολίτευμα ist das Gemeinwesen bzw. die Zugehörigkeit zu ihm. Die Bürger der Kolonie Philippi gehörten rechtlich zu Rom; die Glaubenden gehören zum Himmel. Vgl. [[PHP.1.27]]."),
 ("PHP.3.21", "armseligen", "adapted", "ταπεινώσεως", "der Niedrigkeit", ["vergänglichen", "niedrigen"], "Wörtlich «Leib unserer Niedrigkeit» und «Leib seiner Herrlichkeit»; als Eigenschaftswörter wiedergegeben."),
 ("PHP.4.1", "Siegeskranz", "interpretive", "στέφανός", "Kranz", ["Krone", "Ehrenkranz"], "στέφανος ist der Kranz des Siegers im Wettkampf oder der Festkranz, keine Königskrone."),
 ("PHP.4.3", "Gefährte", "interpretive", "σύζυγε", "Jochgenosse", ["Syzygus (als Name)", "Mitarbeiter"], "σύζυγος heisst «einer, der mit im Joch geht». Wer gemeint ist, bleibt unbekannt; manche lesen das Wort als Eigennamen."),
 ("PHP.4.5", "Güte", "interpretive", "ἐπιεικὲς", None, ["Milde", "Freundlichkeit", "Nachsicht", "Gelassenheit"], "τὸ ἐπιεικές meint die Haltung, nicht auf dem eigenen Recht zu bestehen; ein deutsches Wort deckt es nicht ganz ab."),
 ("PHP.4.7", "bewahren", "interpretive", "φρουρήσει", "bewachen", ["behüten", "schützen"], "φρουρεῖν ist ein militärisches Wort: eine Wache halten. In der Garnisonsstadt Philippi war das ein vertrautes Bild."),
 ("PHP.4.8", "Tugend", "literal", "ἀρετὴ", None, ["Tüchtigkeit", "Vortrefflichkeit"], "ἀρετή ist ein Leitbegriff der griechischen Ethik und kommt bei Paulus nur hier vor."),
 ("PHP.4.9", "empfangen", "literal", "παρελάβετε", None, ["übernommen"], "παραλαμβάνειν ist Fachwort für das Empfangen einer Überlieferung."),
 ("PHP.4.11", "mir selbst zu genügen", "interpretive", "αὐτάρκης", "selbstgenügsam", ["zufrieden zu sein", "unabhängig zu sein"], "αὐτάρκεια war ein Ideal der Stoiker: unabhängig von äusseren Umständen. Paulus nimmt das Wort auf, begründet die Kraft dazu aber in [[PHP.4.13]] mit dem, der ihn stark macht."),
 ("PHP.4.12", "bin ich eingeweiht", "literal", "μεμύημαι", None, ["habe ich gelernt"], "μυεῖσθαι ist Fachwort der Mysterienkulte: in ein Geheimnis eingeweiht werden."),
 ("PHP.4.15", "auf die Rechnung", "literal", "λόγον", None, ["was Geben und Nehmen betrifft"], "Geschäftssprache: Konto, Abrechnung von Geben und Nehmen. Ebenso in [[PHP.4.17]] und [[PHP.4.18]] (ἀπέχω: Quittungsformel «ich habe erhalten»)."),
 ("PHP.4.22", "Haus des Kaisers", "literal", "Καίσαρος οἰκίας", None, ["kaiserliche Dienerschaft"], "Gemeint sind nicht Familienmitglieder, sondern Sklaven und Freigelassene im kaiserlichen Dienst; solche gab es in Rom und in den Provinzen."),
]
DEC_GSW = [
 ("PHP.1.1", "Chnächt", "traditional", "δοῦλοι", "Sklave", ["Diener"], "δοῦλος heisst wörtlich «Sklav». Als Bezeichnig für sich sälber meint s Mänsche, wo ganz Christus ghöred; «Chnächt» folgt de vertroute Widergab. I [[PHP.2.7]] staat für Christus sälber «Sklav», demit de Gägesatz zur «Gstalt vo Gott» ghört wird."),
 ("PHP.1.1", "Ufseher und Diakone", "interpretive", "ἐπισκόποις καὶ διακόνοις", "Ufseher und Diener", ["Bischöf und Diakone", "Gmeindleiter und Helfer"], "Us ἐπίσκοπος isch «Bischof» worde, us διάκονος «Diakon». Es drüüstufigs Amt isch da no nöd voruusgsetzt; es git mehreri Ufseher i einere Gmeind. Was die beide Gruppe gnau gmacht händ, seit de Brief nöd."),
 ("PHP.1.5", "Gmeinschaft im Dienscht am", "interpretive", "κοινωνίᾳ εἰς", "Gmeinschaft für", ["Teilhab am", "Partnerschaft für"], "κοινωνία isch Gmeinschaft dur Teilhab. D Philipper händ am Evangelium mitgmacht, au mit Gäld (vgl. [[PHP.4.15]])."),
 ("PHP.1.8", "de innige Liebi", "interpretive", "σπλάγχνοις", "de Ingweid", ["em Härz", "em Erbarme"], "σπλάγχνα sind d Ingweid, damals de Sitz vo de tüüfe Gfüül; mir säged ehner «Härz»."),
 ("PHP.1.12", "Brüeder und Schwöschtere", "interpretive", "ἀδελφοί", "Brüeder", ["Gschwüschterti"], "De griechisch Plural ἀδελφοί schlüüsst d Fraue ii; z Philippi ghöred Fraue usdrücklich zur Gmeind (vgl. [[PHP.4.2]]). Ohni Aared «Gschwüschterti»."),
 ("PHP.1.13", "Prätorium", "literal", "πραιτωρίῳ", None, ["kaiserlichi Garde", "Amtssitz vom Statthalter"], "πραιτώριον cha d Garde z Rom oder de Amtssitz vo me Statthalter meine. Devo hangt ab, wo de Paulus gfange gsii isch (Rom, Ephesus oder Cäsarea); das isch umstritte."),
 ("PHP.1.17", "Eigenutz", "interpretive", "ἐριθείας", None, ["Rivalität", "Parteigeischt", "Ehrgiiz"], "ἐριθεία meint sälbschtsüchtigs Strebe, oft mit Parteibildig; gliich i [[PHP.2.3]]."),
 ("PHP.1.19", "Rettig", "interpretive", "σωτηρίαν", None, ["Befreiig", "Heil"], "De Wortlut nimmt [[JOB.13.16]] (griechischi Fassig) uf. Gmeint cha d Freilassig us de Haft sii oder di ändgültig Rettig vor Gott; de nächscht Vers («dur s Läbe oder dur de Tod») redt ehner für s Zweite."),
 ("PHP.1.20", "Freimuet", "literal", "παρρησίᾳ", None, ["Offeheit", "Unerschrockeheit"], "παρρησία isch s freie, offene Rede ohni Angscht, ursprünglich s Rächt vom Bürger i de Volksversammlig."),
 ("PHP.1.21", "s Läbe Christus", "literal", "τὸ ζῆν Χριστὸς", None, ["mis Läbe ghört Christus"], "De churz Satz hät kei Verb. Wörtlich bhalte, demit d Spannig zwüsche «Läbe» und «Sterbe» bliibt; gmeint isch, dass Christus Inhalt und Ziil vom Läbe isch."),
 ("PHP.1.22", "Fleisch", "literal", "σαρκί", None, ["Körper", "irdische Läbe"], "σάρξ staat da nöd für Sünd, sondern für s liiblich, irdisch Läbe."),
 ("PHP.1.22", "weiss ich", "interpretive", "γνωρίζω", "mach ich bekannt", ["säg ich"], "γνωρίζω heisst suscht «bekannt mache»; da wahrschiinli: Ich chan s nöd säge."),
 ("PHP.1.23", "ufzbräche", "literal", "ἀναλῦσαι", "ufzlöse", ["z sterbe"], "ἀναλύειν heisst losbinde, s Lager abbräche, es Schiff losmache; es Bild für s Sterbe."),
 ("PHP.1.27", "Läbed als Bürger", "interpretive", "πολιτεύεσθε", "Füered euers Bürgerläbe", ["Füered euers Läbe", "Läbed als Gmeinschaft"], "πολιτεύεσθαι heisst «als Bürger (vo ere Polis) läbe». Philippi isch e römischi Kolonie gsii und uf s Bürgerrächt stolz; de Paulus nimmt das uf und redt i [[PHP.3.20]] vom Bürgerrächt im Himmel."),
 ("PHP.1.27", "einmüetig", "adapted", "μιᾷ ψυχῇ", "mit einere Seel", None, "ψυχή isch da s Inner, de Wille; «einmüetig» git de Sinn wider."),
 ("PHP.2.1", "Gmeinschaft", "literal", "κοινωνία πνεύματος", None, ["Teilhab am Geischt"], "De Genitiv cha d Gmeinschaft meine, wo de Geischt schafft, oder d Teilhab am Geischt."),
 ("PHP.2.2", "s Gliiche dänked", "literal", "τὸ αὐτὸ φρονῆτε", None, ["gliich gsinnt sind", "uf s Gliiche uus sind"], "φρονεῖν (dänke, gsinnt sii, uf öppis uus sii) isch es Leitwort vom Brief (vgl. [[PHP.2.5]], [[PHP.3.15]], [[PHP.4.2]]). Es meint nöd di gliich Meinig, sondern di gliich Uusrichtig."),
 ("PHP.2.3", "Demuet", "literal", "ταπεινοφροσύνῃ", None, ["Bescheideheit"], "I de griechische Umwält meischt abwärtend (d Haltig vo de Niedrige); im früene Chrischtetum ufgwärtet. Vgl. [[PHP.2.8]]: Christus «hät sich erniedriget»."),
 ("PHP.2.5", "wo au i Christus Jesus gsii isch", "interpretive", "ὃ καὶ ἐν Χριστῷ Ἰησοῦ", "wo au i Christus Jesus", ["wie s sich für die ghört, wo i Christus Jesus sind"], "De Nebesatz hät kei Verb. Ergänzt me «gsii isch», isch Christus Vorbild; ergänzt me «sich ghört», isch d Gmeinschaft «in Christus» de Massstab. Beides wird vertrete."),
 ("PHP.2.6", "Gstalt", "literal", "μορφῇ", None, ["Wäse", "Daseinswiis"], "μορφή isch d Gstalt, i dere öppis erschiint und isch. De Hymnus stellt «Gstalt vo Gott» und «Gstalt vo me Sklav» ([[PHP.2.7]]) gägenand."),
 ("PHP.2.6", "für e Büüt", "interpretive", "ἁρπαγμὸν", "für en Ruub", ["für öppis, wo er a sich riisse müesst", "für öppis, wo er fescht- oder uusnütze müesst"], "ἁρπαγμός isch suscht chuum belegt. Drei Deutige: öppis, wo er unrächtmässig zersch rouben müesst; öppis, wo er mit Gwalt feschthebt; oder es Vorrächt, wo me zum eigene Vorteil uusnützt. Di letscht wird hüt oft vertrete; «Büüt» laat d Frag offe."),
 ("PHP.2.7", "läär gmacht", "literal", "ἐκένωσεν", None, ["entüüsseret", "uf alles verzichtet"], "κενόω heisst «läär mache». Uf was Christus verzichtet hät, seit de Text nöd; di nächschte Partizip (hät aagnoo, isch gliich worde) erkläred s als Aanaa vo de Sklavegstalt."),
 ("PHP.2.7", "vo me Sklav", "literal", "δούλου", None, ["vo me Chnächt", "vo me Diener"], "Da bewusst «Sklav»: De Gägesatz zur «Gstalt vo Gott» isch schroff; de Sklav isch rächtlos gsii, de Chrüüztod ([[PHP.2.8]]) e Sklavestraf."),
 ("PHP.2.9", "über alles erhöht", "interpretive", "ὑπερύψωσεν", "überhöht", ["höch erhöht", "ufs Höchscht erhöht"], "S zämegsetzt Verb (ὑπέρ + ὑψόω) steigeret; es cha di höchscht Stellig oder d Erhöhig über alles bezeichne."),
 ("PHP.2.11", "de Herr", "literal", "κύριος", None, ["Herr (als Gottesname)"], "[[PHP.2.10-PHP.2.11]] nämed [[ISA.45.23]] uf, wo Gott seit: «Mir wird sich jedes Chnüü böige.» κύριος staat i de griechische Bible für de Gottesname; de Hymnus leit em Jesus so de Name vo Gott bi."),
 ("PHP.2.12", "schaffed", "interpretive", "κατεργάζεσθε", "erarbeited", ["würked uus", "bringed zum Ziil"], "κατεργάζεσθαι heisst bewürke, vollbringe. Gmeint isch nöd, dass me sich d Rettig verdient: [[PHP.2.13]] begründet, dass Gott s Wele und s Vollbringe würkt. D Aared isch Plural; es paar dänked as Wohl vo de Gmeinschaft."),
 ("PHP.2.15", "Liechter", "literal", "φωστῆρες", None, ["Stärne", "Himmelsliechter"], "φωστήρ bezeichnet Himmelskörper; Aaklang a [[DAN.12.3]]."),
 ("PHP.2.16", "fescht hebed", "interpretive", "ἐπέχοντες", None, ["aabüüted", "höch hebed"], "ἐπέχειν cha «feschthebe» oder «aabüüte, vorhebe» heisse; je nachdem gaat s um Tröii oder um Zügnis gäge usse."),
 ("PHP.2.17", "ich als Trankopfer usgschüttet wirde", "literal", "σπένδομαι", None, ["mis Läbe häregää wird"], "Bild us em Opferkult: Wii isch über oder näbe s Opfer gosse worde. De Paulus düütet demit sin mögliche Tod."),
 ("PHP.2.25", "Gsandte", "interpretive", "ἀπόστολον", "Apostel", ["Bote"], "ἀπόστολος heisst «Gsandte». Da isch nöd de Chreis vo de Apostel gmeint, sondern de Beuftragt vo de Gmeind, wo em Paulus d Gab bracht hät."),
 ("PHP.3.2", "Hünd", "literal", "κύνας", None, None, "Hünd händ als unrein gulte; «Hund» isch es Schimpfwort gsii, au für Nöd-Jude. De Paulus dräit das gäge Lüüt, wo uf d Beschniidig drängt händ. Wän er gnau meint, isch umstritte."),
 ("PHP.3.2", "Zerschniidig", "literal", "κατατομήν", None, ["Verstümmlig"], "Wortspiil: κατατομή (Zerschniidig) gäge περιτομή (Beschniidig, [[PHP.3.3]]). D Schärfi isch gwollt."),
 ("PHP.3.6", "Gmeind", "literal", "ἐκκλησίαν", None, ["Chile", "Versammlig"], "ἐκκλησία isch d Versammlig; im Nöie Teschtament d Gmeind vo de Gläubige."),
 ("PHP.3.8", "Dräck", "interpretive", "σκύβαλα", "Kot", ["Mischt", "Abfall"], "σκύβαλον bezeichnet Abfall, Ässesreschte oder Kot. S Wort isch derb; «Dräck» bhaltet d Schärfi, ohni eini vo de Bedüütige feschtzlegge."),
 ("PHP.3.9", "de Glaube a Christus", "interpretive", "πίστεως Χριστοῦ", "de Glaube vo Christus", ["d Tröii vo Christus"], "De Genitiv cha objektiv (Glaube a Christus) oder subjektiv (Glaube oder Tröii vo Christus) verstande wärde. Für d Tröii vo Christus redt, dass de Glaube vom Mänsch am Versänd extra gnännt wird; für de Glaube a Christus de Sprachgebruuch i [[PHP.1.29]] und [[GAL.2.16]]. D Wahl isch e redaktionelli Entscheidig; beidi Düütige händ gwichtigi Vertreter."),
 ("PHP.3.10", "Gmeinschaft", "literal", "κοινωνίαν", None, ["Teilhab"], "S gliich Wort wie i [[PHP.1.5]]: Teilhab a de Liide vo Christus."),
 ("PHP.3.12", "wil", "interpretive", "ἐφʼ ᾧ", None, ["wozue"], "ἐφʼ ᾧ cha begründe («wil») oder es Ziil aagää («wozue ich au packt worde bi»)."),
 ("PHP.3.12", "packe", "adapted", "καταλάβω", "ergriife", ["erreiche"], "Packe und packt worde bhalted s Wortspiil vom Griechische (καταλαμβάνω, «ergriife»)."),
 ("PHP.3.14", "himmlische", "interpretive", "ἄνω", "nach obe", ["vo obe"], "ἄνω κλῆσις cha d Beruefig «nach obe» (in Himmel) oder d Beruefig «vo obe» (dur Gott) meine."),
 ("PHP.3.15", "riif", "interpretive", "τέλειοι", "vollkomme", ["mündig", "erwachse"], "τέλειος heisst vollkomme oder uusgwachse, mündig. Nach [[PHP.3.12]] («nöd, dass ich scho vollkomme wär») villicht ironisch gäge Lüüt, wo sich für vollkomme ghalte händ."),
 ("PHP.3.19", "de Buuch", "literal", "κοιλία", None, ["d Begierd"], "Gmeint cha Gnusssucht sii, Sälbschtsucht allgemein oder (polemisch) s Feschthebe a Speisegebot. D Düütig hangt devo ab, wär gmeint isch."),
 ("PHP.3.20", "Bürgerrächt", "interpretive", "πολίτευμα", None, ["Gmeinwäse", "Heimat"], "πολίτευμα isch s Gmeinwäse oder d Zueghörigkeit dezue. D Bürger vo de Kolonie Philippi händ rächtlich zu Rom ghört; d Gläubige ghöred zum Himmel. Vgl. [[PHP.1.27]]."),
 ("PHP.3.21", "armselige", "adapted", "ταπεινώσεως", "vo de Niedrigkeit", ["vergängliche"], "Wörtlich «Liib vo öisere Niedrigkeit» und «Liib vo sinere Herrlichkeit»; als Eigeschaftswörter widergää."),
 ("PHP.4.1", "Siegerchranz", "interpretive", "στέφανός", "Chranz", ["Chroone", "Ehrechranz"], "στέφανος isch de Chranz vom Sieger im Wettkampf oder de Feschtchranz, kei Königschroone."),
 ("PHP.4.3", "Gfährte", "interpretive", "σύζυγε", "Jochgenoss", ["Syzygus (als Name)", "Mitarbeiter"], "σύζυγος heisst «eine, wo mit im Joch gaat». Wär gmeint isch, weiss me nöd; es paar läsed s Wort als Eigename."),
 ("PHP.4.5", "Güeti", "interpretive", "ἐπιεικὲς", None, ["Milti", "Fründlichkeit", "Naachsicht", "Glasseheit"], "τὸ ἐπιεικές meint d Haltig, nöd uf em eigete Rächt z beharre; kei Wort deckt s ganz ab."),
 ("PHP.4.7", "bewache", "literal", "φρουρήσει", None, ["behüete", "schütze"], "φρουρεῖν isch es militärischs Wort: Wach halte. I de Garnisonsstadt Philippi isch das es vertrauts Bild gsii."),
 ("PHP.4.8", "Tugend", "literal", "ἀρετὴ", None, ["Tüechtigkeit"], "ἀρετή isch en Leitbegriff vo de griechische Ethik und chunnt bim Paulus nu da vor."),
 ("PHP.4.9", "übercho", "literal", "παρελάβετε", None, ["übernoo"], "παραλαμβάνειν isch es Fachwort für s Übernää vo ere Überlieferig."),
 ("PHP.4.11", "mir sälber z gnüege", "interpretive", "αὐτάρκης", "sälbschtgnüegsam", ["zfride z sii", "unabhängig z sii"], "αὐτάρκεια isch es Ideal vo de Stoiker gsii: unabhängig vo de üssere Umständ. De Paulus nimmt s Wort uf, begründet d Chraft dezue aber i [[PHP.4.13]] mit dem, wo en starch macht."),
 ("PHP.4.12", "bi ich iigweiht", "literal", "μεμύημαι", None, ["han ich glernt"], "μυεῖσθαι isch es Fachwort vo de Mysteriekult: in es Gheimnis iigweiht wärde."),
 ("PHP.4.15", "uf d Rächnig", "literal", "λόγον", None, ["was Gää und Nää aagaat"], "Gschäftssprach: Konto, Abrächnig vo Gää und Nää. Gliich i [[PHP.4.17]] und [[PHP.4.18]]."),
 ("PHP.4.22", "Huus vom Kaiser", "literal", "Καίσαρος οἰκίας", None, ["kaiserlichi Dienerschaft"], "Gmeint sind nöd Familiemitglieder, sondern Sklave und Freiglasseni im kaiserliche Dienscht; settigi hät s z Rom und i de Provinze gä."),
]

# Lesarten, die die Übersetzung verändern: (Lesart, Stelle, de von, de zu, gsw von, gsw zu, Wirkung, Hinweis de, Hinweis gsw,
#  Wörter {Lesart: [(griechisch, de, Hinweis)]}, Wörter gsw, Entstehung de, Entstehung gsw)
ALTS = [
 ("VAR-SBLGNTAPP-PHP-001-014-01:R2", "PHP.1.14", "das Wort furchtlos", "das Wort Gottes furchtlos", "s Wort ohni Angscht", "s Wort vo Gott ohni Angscht", "gering",
  "Mit Zusatz wird ausdrücklich gesagt, wessen Wort verkündigt wird. Die Editionen sind hier geteilt.", "Mit em Zuesatz wird usdrücklich gseit, wäm sis Wort verchündet wird. D Usgabe sind da teilt.",
  {"R1": [("τὸν λόγον", "das Wort", "ohne Zusatz")], "R2": [("τὸν λόγον τοῦ θεοῦ", "das Wort Gottes", "mit Zusatz")]},
  {"R1": [("τὸν λόγον", "s Wort", "ohni Zuesatz")], "R2": [("τὸν λόγον τοῦ θεοῦ", "s Wort vo Gott", "mit Zuesatz")]},
  ["«Das Wort Gottes» kann als naheliegende Verdeutlichung zum knappen «das Wort» ergänzt worden sein; umgekehrt kann der Zusatz beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung haben Sinaiticus, Alexandrinus und Vaticanus (4./5. Jh.) den Zusatz, 𝔓46 (um 200) nicht; dessen Wortlaut ist an dieser Stelle teilweise beschädigt bzw. ergänzt."],
  ["«S Wort vo Gott» cha als nöchligendi Verdüütlichig zum churze «s Wort» ergänzt worde sii; umgekeert cha de Zuesatz bim Abschriibe usgfalle sii.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Alexandrinus und de Vaticanus (4./5. Jh.) de Zuesatz, 𝔓46 (um 200) nöd; dört isch de Wortlut a dere Stell zum Teil beschädiget oder ergänzt."]),
 ("VAR-SBLGNTAPP-PHP-002-005-01:R2", "PHP.2.5", "Habt diese Gesinnung unter euch", "Denn diese Gesinnung soll unter euch sein", "Händ die Gsinnig under eu", "Dänn die Gsinnig söll under eu sii", "gering",
  "Mit «denn» und Passiv wird der Vers enger an das Vorangehende angeschlossen.", "Mit «dänn» und Passiv wird de Vers änger as Vorhärige aaghänkt.",
  {"R1": [("τοῦτο φρονεῖτε", "das denkt", "Aufforderung")], "R2": [("τοῦτο γὰρ φρονείσθω", "denn das soll gedacht werden", "mit «denn», Passiv")]},
  {"R1": [("τοῦτο φρονεῖτε", "das dänked", "Ufforderig")], "R2": [("τοῦτο γὰρ φρονείσθω", "dänn das söll dänkt wärde", "mit «dänn», Passiv")]},
  ["Die passive Form kann eine stilistische Glättung sein; «denn» verbindet den Hymnus ausdrücklich mit der Mahnung zuvor.",
   "Laut der automatischen Zuordnung lesen Sinaiticus, Alexandrinus, Vaticanus und Ephraemi die Aufforderung; 𝔓46 hat «denn», aber die aktive Form."],
  ["D passiv Form cha e stilistischi Glättig sii; «dänn» verbindet de Hymnus usdrücklich mit de Mahnig vorhär.",
   "Nach de automatische Zueornig läsed de Sinaiticus, de Alexandrinus, de Vaticanus und de Ephraemi d Ufforderig; 𝔓46 hät «dänn», aber di aktiv Form."]),
 ("VAR-SBLGNTAPP-PHP-002-026-01:R2", "PHP.2.26", "nach euch allen", "danach, euch alle zu sehen", "nach eu allne", "dernaa, eu alli z gseh", "gering",
  "Der Zusatz «zu sehen» präzisiert, wonach Epaphroditus sich sehnte.", "De Zuesatz «z gseh» seit gnauer, nach was sich de Epaphroditus gsehnt hät.",
  {"R1": [("πάντας ὑμᾶς", "euch alle", "ohne Zusatz")], "R2": [("πάντας ὑμᾶς ἰδεῖν", "euch alle zu sehen", "mit Zusatz")]},
  {"R1": [("πάντας ὑμᾶς", "eu alli", "ohni Zuesatz")], "R2": [("πάντας ὑμᾶς ἰδεῖν", "eu alli z gseh", "mit Zuesatz")]},
  ["ἰδεῖν kann ergänzt worden sein, weil ἐπιποθεῖν mit einfachem Objekt knapp klingt (vgl. [[PHP.1.8]]); es kann auch ausgefallen sein.",
   "Laut der automatischen Zuordnung haben Sinaiticus, Alexandrinus und Ephraemi den Zusatz, Vaticanus nicht; 𝔓46 hat an dieser Stelle einen abweichenden Wortlaut."],
  ["ἰδεῖν cha ergänzt worde sii, wil ἐπιποθεῖν mit eme eifache Objekt churz tönt (vgl. [[PHP.1.8]]); es cha au usgfalle sii.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Alexandrinus und de Ephraemi de Zuesatz, de Vaticanus nöd; 𝔓46 hät a dere Stell en andere Wortlut."]),
 ("VAR-SBLGNTAPP-PHP-002-030-01:R2", "PHP.2.30", "des Werkes Christi", "des Werkes des Herrn", "em Wärch vo Christus", "em Wärch vom Herr", "gering",
  "Gemeint ist in jedem Fall der Dienst für Christus; die Lesarten unterscheiden sich im Titel.", "Gmeint isch uf jede Fall de Dienscht für Christus; d Läsarte underscheided sich im Titel.",
  {"R1": [("Χριστοῦ", "Christi", "SBLGNT")], "R2": [("Κυρίου", "des Herrn", "")], "R3": [("τοῦ Χριστοῦ", "des Christus", "mit Artikel")]},
  {"R1": [("Χριστοῦ", "vo Christus", "SBLGNT")], "R2": [("Κυρίου", "vom Herr", "")], "R3": [("τοῦ Χριστοῦ", "vom Christus", "mit Artikel")]},
  ["Die Namen wurden in Handschriften als Kürzel geschrieben (ΚΥ für κυρίου, ΧΥ für Χριστοῦ), die leicht zu verwechseln waren.",
   "Die automatische Zuordnung konnte die Handschriften hier keiner Lesart zuweisen. Im erfassten Wortlaut der CNTR-Transkription steht bei Sinaiticus und Alexandrinus das Kürzel für «Herr», bei Vaticanus und 𝔓46 das für «Christus»; Ephraemi hat keinen Namen. Das ist eine Sekundärtranskription, keine eigene Prüfung der Handschriften."],
  ["D Näme sind i Handschrifte als Chürzel gschribe worde (ΚΥ für κυρίου, ΧΥ für Χριστοῦ), wo me liecht hät chöne verwächsle.",
   "D automatisch Zueornig hät d Handschrifte da keinere Läsart chöne zueteile. Im erfasste Wortlut vo de CNTR-Transkription staat bim Sinaiticus und bim Alexandrinus s Chürzel für «Herr», bim Vaticanus und bi 𝔓46 das für «Christus»; de Ephraemi hät kein Name. Das isch e Sekundärtranskription, kei eigeti Prüefig vo de Handschrifte."]),
 ("VAR-SBLGNTAPP-PHP-003-012-01:R2", "PHP.3.12", "von Christus ergriffen", "von Christus Jesus ergriffen", "vo Christus packt", "vo Christus Jesus packt", "gering",
  "Nur die Länge des Namens ändert sich; die Editionen sind geteilt.", "Nu d Längi vom Name änderet; d Usgabe sind teilt.",
  {"R1": [("Χριστοῦ", "Christus", "kurz")], "R2": [("Χριστοῦ Ἰησοῦ", "Christus Jesus", "lang")], "R3": [("τοῦ Χριστοῦ Ἰησοῦ", "dem Christus Jesus", "mit Artikel")]},
  {"R1": [("Χριστοῦ", "Christus", "churz")], "R2": [("Χριστοῦ Ἰησοῦ", "Christus Jesus", "lang")], "R3": [("τοῦ Χριστοῦ Ἰησοῦ", "em Christus Jesus", "mit Artikel")]},
  ["Die vollere Form «Christus Jesus» ist im Brief häufig und konnte beim Abschreiben leicht ergänzt werden; ebenso leicht konnte ein kurzes Kürzel ausfallen.",
   "Die automatische Zuordnung wies die Handschriften keiner Lesart zu. Im erfassten Wortlaut der CNTR-Transkription haben Sinaiticus, Alexandrinus und 𝔓46 «Christus Jesus», Vaticanus nur «Christus» (Sekundärtranskription, keine eigene Prüfung)."],
  ["Di vollscht Form «Christus Jesus» isch im Brief hüüfig und hät bim Abschriibe liecht chöne ergänzt wärde; gliich liecht hät es churzes Chürzel chöne usfalle.",
   "D automatisch Zueornig hät d Handschrifte keinere Läsart zueteilt. Im erfasste Wortlut vo de CNTR-Transkription händ de Sinaiticus, de Alexandrinus und 𝔓46 «Christus Jesus», de Vaticanus nu «Christus» (Sekundärtranskription, kei eigeti Prüefig)."]),
 ("VAR-SBLGNTAPP-PHP-003-013-01:R2", "PHP.3.13", "von mir selbst nicht", "von mir selbst noch nicht", "vo mir sälber nöd", "vo mir sälber no nöd", "gering",
  "«Noch nicht» betont, dass Paulus unterwegs ist; der Sinn ändert sich kaum.", "«No nöd» betont, dass de Paulus no understwägs isch; de Sinn änderet chuum.",
  {"R1": [("οὐ", "nicht", "")], "R2": [("οὔπω", "noch nicht", "")]},
  {"R1": [("οὐ", "nöd", "")], "R2": [("οὔπω", "no nöd", "")]},
  ["οὔπω kann aus [[PHP.3.12]] («nicht, dass ich schon …») eingedrungen sein, um die Aussage abzumildern; umgekehrt kann eine Silbe ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen Sinaiticus und Alexandrinus οὔπω, Vaticanus und 𝔓46 οὐ; 𝔓15/16 (3./4. Jh.) wird – bei unsicherer Erhaltung – οὔπω zugeordnet."],
  ["οὔπω cha us [[PHP.3.12]] («nöd, dass ich scho …») iidrunge sii, zum d Ussag abzmildere; umgekeert cha e Silbe usgfalle sii.",
   "Nach de automatische Zueornig läsed de Sinaiticus und de Alexandrinus οὔπω, de Vaticanus und 𝔓46 οὐ; 𝔓15/16 (3./4. Jh.) wird – bi unsicherer Erhaltig – οὔπω zueteilt."]),
 ("VAR-SBLGNTAPP-PHP-003-016-01:R2", "PHP.3.16", "lasst uns weitergehen", "lasst uns weitergehen nach der Richtschnur und dasselbe denken", "wämer wiitergaa", "wämer wiitergaa nach de Richtschnuer und s Gliiche dänke", "mittel",
  "Der Zusatz ergänzt den knappen Satz mit Wendungen aus dem Brief und aus [[GAL.6.16]].", "De Zuesatz ergänzt de churz Satz mit Wändige us em Brief und us [[GAL.6.16]].",
  {"R1": [("στοιχεῖν", "weitergehen", "ohne Zusatz")], "R2": [("στοιχεῖν κανόνι τὸ αὐτὸ φρονεῖν", "weitergehen nach der Richtschnur, dasselbe denken", "mit Zusatz")]},
  {"R1": [("στοιχεῖν", "wiitergaa", "ohni Zuesatz")], "R2": [("στοιχεῖν κανόνι τὸ αὐτὸ φρονεῖν", "wiitergaa nach de Richtschnuer, s Gliiche dänke", "mit Zuesatz")]},
  ["Der elliptische Satz lud zur Ergänzung ein; κανών (Richtschnur) steht neben στοιχεῖν in [[GAL.6.16]], «dasselbe denken» in [[PHP.2.2]].",
   "Laut der automatischen Zuordnung haben Sinaiticus, Alexandrinus, Vaticanus und 𝔓46 den kurzen Text; 𝔓15/16 wird ebenfalls dem kurzen Text zugeordnet."],
  ["De abgchürzt Satz hät zum Ergänze iiglade; κανών (Richtschnuer) staat näbe στοιχεῖν i [[GAL.6.16]], «s Gliiche dänke» i [[PHP.2.2]].",
   "Nach de automatische Zueornig händ de Sinaiticus, de Alexandrinus, de Vaticanus und 𝔓46 de churz Text; au 𝔓15/16 wird em churze Text zueteilt."]),
 ("VAR-SBLGNTAPP-PHP-003-021-01:R2", "PHP.3.21", "verwandeln wird, gleichgestaltet", "verwandeln wird, sodass er gleichgestaltet wird", "verwandle wird, gliichgstaltet", "verwandle wird, demit er gliichgstaltet wird", "gering",
  "Der Zusatz macht die Satzverbindung ausdrücklich; der Sinn bleibt gleich.", "De Zuesatz macht d Satzverbindig usdrücklich; de Sinn bliibt gliich.",
  {"R1": [("ἡμῶν σύμμορφον", "unseren …, gleichgestaltet", "ohne Zusatz")], "R2": [("ἡμῶν εἰς τὸ γενέσθαι αὐτὸ σύμμορφον", "unseren …, damit er gleichgestaltet werde", "mit Zusatz")]},
  {"R1": [("ἡμῶν σύμμορφον", "öise …, gliichgstaltet", "ohni Zuesatz")], "R2": [("ἡμῶν εἰς τὸ γενέσθαι αὐτὸ σύμμορφον", "öise …, demit er gliichgstaltet wird", "mit Zuesatz")]},
  ["Eine grammatische Glättung: Das Adjektiv σύμμορφον wird mit «damit er werde» verbunden.",
   "Laut der automatischen Zuordnung haben Sinaiticus, Alexandrinus und Vaticanus den kurzen Text."],
  ["E grammatischi Glättig: S Adjektiv σύμμορφον wird mit «demit er wird» verbunde.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Alexandrinus und de Vaticanus de churz Text."]),
 ("VAR-SBLGNTAPP-PHP-004-013-01:R2", "PHP.4.13", "den, der mich stark macht", "Christus, der mich stark macht", "dä, wo mich starch macht", "Christus, wo mich starch macht", "gering",
  "Der Zusatz nennt ausdrücklich, wer gemeint ist; die Sache ist dieselbe.", "De Zuesatz seit usdrücklich, wär gmeint isch; d Sach isch di gliich.",
  {"R1": [("ἐνδυναμοῦντί με", "der mich stark macht", "ohne Namen")], "R2": [("ἐνδυναμοῦντί με Χριστῷ", "Christus, der mich stark macht", "mit Namen")]},
  {"R1": [("ἐνδυναμοῦντί με", "dä, wo mich starch macht", "ohni Name")], "R2": [("ἐνδυναμοῦντί με Χριστῷ", "Christus, wo mich starch macht", "mit Name")]},
  ["Der Name kann zur Verdeutlichung ergänzt worden sein, besonders wenn der Vers einzeln gelesen wurde (vgl. [[1TI.1.12]]: «Christus Jesus, der mich stark gemacht hat»).",
   "Laut der automatischen Zuordnung haben Sinaiticus, Alexandrinus und Vaticanus den Text ohne Namen."],
  ["De Name cha zur Verdüütlichig ergänzt worde sii, bsunders wänn de Vers elei gläse worde isch (vgl. [[1TI.1.12]]: «Christus Jesus, wo mich starch gmacht hät»).",
   "Nach de automatische Zueornig händ de Sinaiticus, de Alexandrinus und de Vaticanus de Text ohni Name."]),
 ("VAR-SBLGNTAPP-PHP-004-023-01:R2", "PHP.4.23", "mit eurem Geist", "mit euch allen", "mit eurem Geischt", "mit eu allne", "gering",
  "Beide Formen sind übliche Schlussgrüsse.", "Beidi Forme sind üblichi Schlussgrüess.",
  {"R1": [("μετὰ τοῦ πνεύματος ὑμῶν", "mit eurem Geist", "")], "R2": [("μετὰ πάντων ὑμῶν", "mit euch allen", "")]},
  {"R1": [("μετὰ τοῦ πνεύματος ὑμῶν", "mit eurem Geischt", "")], "R2": [("μετὰ πάντων ὑμῶν", "mit eu allne", "")]},
  ["«Mit euch allen» ist ein geläufiger Briefschluss (z. B. [[2CO.13.13]]) und konnte den selteneren Schluss verdrängen; «mit eurem Geist» steht auch in [[GAL.6.18]] und [[PHM.1.25]].",
   "Die automatische Zuordnung wies die Handschriften wegen der Kürzel keiner Lesart zu; im erfassten Wortlaut der CNTR-Transkription haben Sinaiticus, Alexandrinus, Vaticanus und 𝔓46 «mit eurem Geist» (Sekundärtranskription)."],
  ["«Mit eu allne» isch en gläufige Briefschluss (z. B. [[2CO.13.13]]) und hät de sältener Schluss chöne verdränge; «mit eurem Geischt» staat au i [[GAL.6.18]] und [[PHM.1.25]].",
   "D automatisch Zueornig hät d Handschrifte wäge de Chürzel keinere Läsart zueteilt; im erfasste Wortlut vo de CNTR-Transkription händ de Sinaiticus, de Alexandrinus, de Vaticanus und 𝔓46 «mit eurem Geischt» (Sekundärtranskription)."]),
 ("VAR-SBLGNTAPP-PHP-004-023-02:R2", "PHP.4.23", "Geist!", "Geist! Amen.", "Geischt!", "Geischt! Amen.", "gering",
  "Liturgischer Schluss.", "Liturgische Schluss.",
  {"R1": [("ὑμῶν", "euch", "ohne Amen")], "R2": [("ὑμῶν ἀμήν", "euch. Amen", "mit Amen")]},
  {"R1": [("ὑμῶν", "eu", "ohni Amen")], "R2": [("ὑμῶν ἀμήν", "eu. Amen", "mit Amen")]},
  ["Briefe wurden im Gottesdienst vorgelesen; ein «Amen» am Schluss lag nahe und wurde vielen Briefen angefügt.",
   "Laut der automatischen Zuordnung haben Sinaiticus, Alexandrinus und 𝔓46 das «Amen», Vaticanus nicht. Hier stehen frühe Handschriften auf beiden Seiten."],
  ["Brief sind im Gottesdienscht vorgläse worde; es «Amen» am Schluss isch nooch glege und isch vilne Brief aaghänkt worde.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Alexandrinus und 𝔓46 s «Amen», de Vaticanus nöd. Da stönd früeni Handschrifte uf beidne Siite."]),
]

UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung)
 ("TU-PHP-001-001-030", "PHP.1.1-PHP.1.30", "section", "Dank, Gefangenschaft und Zuversicht",
  ["TU-PHP-001-001-002", "TU-PHP-001-003-011", "TU-PHP-001-012-026", "TU-PHP-001-027-030"],
  "Paulus grüsst die Gemeinde in Philippi, dankt für ihre lange Verbundenheit und betet für sie. Er berichtet, dass seine Gefangenschaft dem Evangelium nützt, und wägt Leben und Sterben gegeneinander ab. Die Gemeinde soll dem Evangelium entsprechend leben und gemeinsam standhalten."),
 ("TU-PHP-001-001-002", "PHP.1.1-PHP.1.2", "greeting", "Gruss an die Heiligen in Philippi", None,
  "Paulus und Timotheus, Knechte Christi Jesu, grüssen die ganze Gemeinde, ausdrücklich auch ihre Aufseher und Diakone."),
 ("TU-PHP-001-003-011", "PHP.1.3-PHP.1.11", "prayer", "Dank und Fürbitte", None,
  "Paulus dankt mit Freude für die Gemeinschaft der Philipper am Evangelium seit dem ersten Tag und betet, dass ihre Liebe an Einsicht wachse, damit sie unterscheiden können, worauf es ankommt."),
 ("TU-PHP-001-012-026", "PHP.1.12-PHP.1.26", "section", "Leben ist Christus, Sterben Gewinn", None,
  "Die Gefangenschaft hat das Evangelium gefördert; dass Christus verkündigt wird, freut Paulus selbst dann, wenn es aus unlauteren Motiven geschieht. Er schwankt zwischen dem Wunsch, bei Christus zu sein, und der Aufgabe, für die Gemeinde da zu sein, und rechnet damit, zu bleiben."),
 ("TU-PHP-001-027-030", "PHP.1.27-PHP.1.30", "section", "Würdig des Evangeliums leben", None,
  "Die Gemeinde soll als Bürger leben, wie es dem Evangelium entspricht, einmütig zusammenstehen und sich von Gegnern nicht einschüchtern lassen; auch das Leiden für Christus ist ihr geschenkt."),
 ("TU-PHP-002-001-030", "PHP.2.1-PHP.2.30", "section", "Die Gesinnung Christi", ["TU-PHP-002-001-011", "TU-PHP-002-012-018", "TU-PHP-002-019-030"],
  "Paulus ruft zu Einmütigkeit und Demut auf und begründet das mit dem Weg Christi von der Gestalt Gottes bis zum Kreuz und seiner Erhöhung. Die Gemeinde soll ihre Rettung mit Furcht und Zittern auswirken, denn Gott wirkt in ihr. Dann kündigt er den Besuch des Timotheus an und schickt Epaphroditus zurück."),
 ("TU-PHP-002-001-011", "PHP.2.1-PHP.2.11", "section", "Einmütig in der Gesinnung Christi", None,
  "Die Philipper sollen einmütig sein, einander höher achten als sich selbst und nicht nur auf das Eigene sehen. Ein hymnisch geformter Abschnitt ([[PHP.2.6-PHP.2.11]]) erzählt, wie Christus sich entäusserte, Sklavengestalt annahm und gehorsam wurde bis zum Tod am Kreuz, und wie Gott ihn erhöhte, damit alle ihn als Herrn bekennen."),
 ("TU-PHP-002-012-018", "PHP.2.12-PHP.2.18", "section", "Lichter in der Welt", None,
  "Weil Gott in ihnen das Wollen und Vollbringen wirkt, sollen die Philipper ihre Rettung mit Furcht und Zittern auswirken, ohne Murren leben und wie Lichter leuchten. Paulus freut sich, selbst wenn sein Leben als Opfer ausgegossen wird."),
 ("TU-PHP-002-019-030", "PHP.2.19-PHP.2.30", "section", "Timotheus und Epaphroditus", None,
  "Paulus will Timotheus bald senden, der sich wie ein Sohn bewährt hat, und schickt Epaphroditus zurück, den Gesandten der Gemeinde, der todkrank war und sein Leben für den Dienst eingesetzt hat."),
 ("TU-PHP-003-001-021", "PHP.3.1-PHP.3.21", "section", "Alles für Christus", ["TU-PHP-003-001-011", "TU-PHP-003-012-021"],
  "Paulus warnt scharf vor Leuten, die auf Beschneidung setzen, und erzählt, wie er seine eigenen Vorzüge um Christi willen als Verlust ansieht. Er ist noch unterwegs zum Ziel und ruft dazu auf, seinem Beispiel zu folgen; das Bürgerrecht der Glaubenden ist im Himmel."),
 ("TU-PHP-003-001-011", "PHP.3.1-PHP.3.11", "section", "Gewinn und Verlust", None,
  "Wer auf das Fleisch vertraut, dem hält Paulus seine eigene Herkunft und Gesetzestreue entgegen; doch gegenüber der Erkenntnis Christi erklärt er sie für Verlust. Er sucht die Gerechtigkeit aus Gott durch den Glauben; er will Christus erkennen, die Kraft seiner Auferstehung und die Gemeinschaft seiner Leiden."),
 ("TU-PHP-003-012-021", "PHP.3.12-PHP.3.21", "section", "Dem Ziel entgegen", None,
  "Paulus hat das Ziel noch nicht erreicht, jagt ihm aber nach. Die Gemeinde soll ihn nachahmen und nicht leben wie die vielen, die als Feinde des Kreuzes Christi auf das Irdische bedacht sind; sie erwartet den Retter aus dem Himmel, der den Leib verwandeln wird."),
 ("TU-PHP-004-001-023", "PHP.4.1-PHP.4.23", "section", "Freude, Friede und Dank", ["TU-PHP-004-001-009", "TU-PHP-004-010-020", "TU-PHP-004-021-023"],
  "Paulus mahnt zwei Mitarbeiterinnen zur Einigkeit, ruft zur Freude im Herrn und zum Gebet statt Sorge auf und verspricht den Frieden Gottes. Er dankt für die Gabe der Gemeinde, die er als Opfer für Gott versteht, und schliesst mit Grüssen."),
 ("TU-PHP-004-001-009", "PHP.4.1-PHP.4.9", "section", "Freut euch im Herrn", None,
  "Paulus bittet Euodia und Syntyche, eines Sinnes zu sein. Die Gemeinde soll sich allezeit freuen, freundlich sein, ihre Anliegen vor Gott bringen und bedenken, was wahr, gerecht und liebenswert ist; der Friede Gottes wird sie bewahren."),
 ("TU-PHP-004-010-020", "PHP.4.10-PHP.4.20", "section", "Dank für die Gabe", None,
  "Paulus freut sich über die Unterstützung, betont aber, dass er gelernt hat, in jeder Lage auszukommen, durch den, der ihn stark macht. Die Gabe sieht er als Frucht für die Gemeinde und als Gott wohlgefälliges Opfer; Gott wird all ihren Bedarf erfüllen."),
 ("TU-PHP-004-021-023", "PHP.4.21-PHP.4.23", "greeting", "Grüsse und Segenswunsch", None,
  "Gruss an jeden Heiligen, Grüsse von den Geschwistern bei Paulus und von allen Heiligen, besonders aus dem Haus des Kaisers, und der Segenswunsch der Gnade."),
]
UNITS_GSW = {
 "TU-PHP-001-001-030": ("Dank, Gfangeschaft und Zueversicht", "De Paulus grüesst d Gmeind z Philippi, dankt für iri langi Verbundeheit und bättet für si. Er verzellt, dass sini Gfangeschaft em Evangelium nützt, und wägt Läbe und Sterbe gägenand ab. D Gmeind söll so läbe, wie s em Evangelium entspricht, und zäme standhalte."),
 "TU-PHP-001-001-002": ("Gruess a d Heilige z Philippi", "De Paulus und de Timotheus, Chnächt vo Christus Jesus, grüessed di ganz Gmeind, usdrücklich au iri Ufseher und Diakone."),
 "TU-PHP-001-003-011": ("Dank und Fürbitt", "De Paulus dankt mit Fröid für d Gmeinschaft vo de Philipper am Evangelium sit em erschte Tag und bättet, dass iri Liebi a Iisicht wachst, demit si chönd underscheide, worum s gaat."),
 "TU-PHP-001-012-026": ("Läbe isch Christus, Sterbe Gwünn", "D Gfangeschaft hät s Evangelium vorwärtsbracht; dass Christus verchündet wird, fröit de Paulus sogar dänn, wänn s us unluutere Gründ passiert. Er schwankt zwüsche em Wunsch, bi Christus z sii, und de Ufgab, für d Gmeind da z sii, und rächnet demit, dass er bliibt."),
 "TU-PHP-001-027-030": ("So läbe, wie s em Evangelium entspricht", "D Gmeind söll als Bürger läbe, wie s em Evangelium entspricht, einmüetig zämestaa und sich vo Gägner nöd laa iischüüchtere; au s Liide für Christus isch ere gschänkt."),
 "TU-PHP-002-001-030": ("D Gsinnig vo Christus", "De Paulus rüeft zu Einmüetigkeit und Demuet uf und begründet das mit em Wäg vo Christus vo de Gstalt vo Gott bis as Chrüüz und sinere Erhöhig. D Gmeind söll mit Furcht und Zittere a irer Rettig schaffe, dänn Gott würkt i ere. Dänn chündet er de Bsuech vom Timotheus aa und schickt de Epaphroditus zrugg."),
 "TU-PHP-002-001-011": ("Einmüetig i de Gsinnig vo Christus", "D Philipper söled einmüetig sii, enand höcher achte als sich sälber und nöd nu uf s Eige luege. En Abschnitt i Hymnusform ([[PHP.2.6-PHP.2.11]]) verzellt, wie Christus sich läär gmacht hät, d Gstalt vo me Sklav aagnoo hät und ghorsam worde isch bis zum Tod am Chrüüz, und wie Gott en erhöht hät, demit alli en als Herr bekänned."),
 "TU-PHP-002-012-018": ("Liechter i de Wält", "Wil Gott i ine s Wele und s Vollbringe würkt, söled d Philipper mit Furcht und Zittere a irer Rettig schaffe, ohni Muule läbe und wie Liechter lüüchte. De Paulus fröit sich, sogar wänn sis Läbe als Opfer usgschüttet wird."),
 "TU-PHP-002-019-030": ("Timotheus und Epaphroditus", "De Paulus wott de Timotheus bald schicke, wo sich wie en Sohn bewährt hät, und schickt de Epaphroditus zrugg, de Gsandt vo de Gmeind, wo todchrank gsii isch und sis Läbe für de Dienscht iigsetzt hät."),
 "TU-PHP-003-001-021": ("Alles für Christus", "De Paulus warnt schaarf vor Lüüt, wo uf d Beschniidig setzed, und verzellt, wie er sini eigete Vorzüg wäge Christus als Verluscht aaluegt. Er isch no underwägs zum Ziil und rüeft uf, sim Biispiil z folge; s Bürgerrächt vo de Gläubige isch im Himmel."),
 "TU-PHP-003-001-011": ("Gwünn und Verluscht", "Wär uf s Fleisch vertrout, dem hebt de Paulus sini eigeti Herkunft und Gsetzeströii entgäge; aber gägenüber de Erchänntnis vo Christus erklärt er si für Verluscht. Er suecht d Grächtigkeit us Gott dur de Glaube; er wott Christus erchänne, d Chraft vo sinere Uferstehig und d Gmeinschaft mit sim Liide."),
 "TU-PHP-003-012-021": ("Em Ziil entgäge", "De Paulus hät s Ziil no nöd erreicht, jagt em aber nache. D Gmeind söll en nachahme und nöd läbe wie di vile, wo als Feind vom Chrüüz vo Christus uf s Irdische uus sind; si erwartet de Retter us em Himmel, wo de Liib verwandle wird."),
 "TU-PHP-004-001-023": ("Fröid, Fride und Dank", "De Paulus mahnt zwei Mitarbeiterinne zur Einigkeit, rüeft zur Fröid im Herr und zum Bätte statt Sorge uf und verspricht de Fride vo Gott. Er dankt für d Gab vo de Gmeind, wo er als Opfer für Gott verstaat, und hört mit Grüess uf."),
 "TU-PHP-004-001-009": ("Fröied eu im Herr", "De Paulus bittet d Euodia und d Syntyche, einig z sii. D Gmeind söll sich immer fröie, fründlich sii, iri Aaliige vor Gott bringe und bedänke, was wahr, grächt und liebenswärt isch; de Fride vo Gott wird si bewache."),
 "TU-PHP-004-010-020": ("Dank für d Gab", "De Paulus fröit sich über d Unterstützig, betont aber, dass er glernt hät, i jeder Lag uuszcho, dur dä, wo en starch macht. D Gab gseht er als Frucht für d Gmeind und als Opfer, wo Gott gfallt; Gott wird alles erfülle, was si bruuched."),
 "TU-PHP-004-021-023": ("Grüess und Sägeswunsch", "Gruess a jede Heilige, Grüess vo de Gschwüschterti bim Paulus und vo allne Heilige, bsunders us em Huus vom Kaiser, und de Sägeswunsch vo de Gnad."),
}

NOTES_DE = ["KI-Entwurf ohne fachliche Prüfung.", ("Die Zuordnung von Handschriften zu Lesarten in den Alternativen beruht auf "
            "maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf der CNTR-Transkription, nicht auf eigener Prüfung der Handschriften."),
            ("Die Abfolge [[PHP.1.16]]/[[PHP.1.17]] (in einem Teil der Überlieferung vertauscht) ist im importierten Apparat nicht als eigene Variante erfasst und deshalb hier nicht als Alternative geführt.")]
NOTES_GSW = ["KI-Entwurf ohni fachlichi Prüefig.", "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.", ("D Zueornig vo Handschrifte zu Läsarte "
             "beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de CNTR-Transkription, nöd uf eigeter Prüefig vo de Handschrifte.")]


def run():
    import json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _lib import localize  # noqa: E402
    n = 0
    n += write(D / "works" / "WORK-PHP.json", {"id": "WORK-PHP", "type": "work", "status": "draft", "tags": TAGS,
                                              "name": "Brief an die Philipper", "original_language": "grc"})
    for uid, rng, kind, title, parts, summary in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-PHP", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}),
               "segmentation_note_de": "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung." if parts else None,
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        rec = {k: v for k, v in rec.items() if v is not None}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-13; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-php").glob("*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-PHP-{c:03d}.json")
        refs_c = [f"PHP.{c}.{v}" for v in range(1, last + 1)]
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-PHP-{c:03d}-001-{last:03d}-{code}-WORKING"
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
                if vid.split(":")[0] not in variants:
                    raise SystemExit(f"{tid}: Variante {vid} nicht im Apparat")
                f_, t_, nt, ws, og = (f_de, t_de, n_de, w_de, o_de) if lang == "de" else (f_g, t_g, n_g, w_g, o_g)
                if f_ not in texts[ref]:
                    raise SystemExit(f"{tid}: Alternative {f_!r} nicht im Text {ref}")
                alts.append({"reading": vid, "reference": ref, "from_text": f_, "to_text": t_, "effect": eff, "note": nt,
                             "readings": {k: [{"grc": g, "text": x, **({"note": h} if h else {})} for g, x, h in v] for k, v in ws.items()},
                             "origin": og})
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"PHP.{c}.1-PHP.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-PHP-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
                                       if lang == "de" else "Direkt aus dem SBLGNT übersetzt, mit Wortzuordnung zu den Token; die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle. Nicht aus einer veröffentlichten Mundart-Bibel übernommen."),
                        "based_on_edition": "ED-SBLGNT", "based_on_tokens": ts_id, "follows_readings": follows,
                        "text_by_reference": texts, "authorship_de": AUTH if lang == "de" else AUTH_GSW,
                        "translation_notes": NOTES_DE if lang == "de" else NOTES_GSW,
                        "knowledge": {"asserted_at": DATE, "supersedes": None}, "decisions": dec,
                        "decisions_note_de": "Übersetzungsentscheidungen: wörtlich (literal), sprachlich angepasst (adapted), Deutungsentscheidung (interpretive) oder der vertrauten Wiedergabe folgend (traditional). " + (AUTH if lang == "de" else AUTH_GSW)})
            if alts:
                rec["alternatives"] = alts
                rec["alternatives_note_de"] = "Wiedergabe abweichender Lesarten, soweit sie die Übersetzung verändern. " + (AUTH if lang == "de" else AUTH_GSW)
                rec["alternatives_origin_note"] = ("Mögliche Erklärungen, wie die Unterschiede entstanden sein könnten. Sie stehen nebeneinander; keine ist als richtig entschieden."
                                                   if lang == "de" else "Möglichi Erkläärige, wie d Underschid entstande sii chönnted. Si stönd näbenand; keini isch als richtig entschide.")
            n += write(D / "translations" / f"{tid}.json", rec)
            aid = f"ALIGN-PHP-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"PHP.{c}.1-PHP.{c}.{last}",
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/philipper_text.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Philipper – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
