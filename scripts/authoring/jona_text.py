#!/usr/bin/env python3
"""Autorenwerkzeug: Jona – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem hebräischen Text
(Westminster Leningrad Codex), Übersetzungsentscheidungen und vollständige Wortzuordnung je Morphem.

Aufruf: python3 scripts/authoring/jona_text.py

Auszeichnung wie in scripts/authoring/_lib.py; die Zahlen sind die Morphem-Positionen im Vers
(data/tokens/WLC-JON-00c.json). Die Verse stehen in der KJV-Zählung der Daten: JON.1.17 ist hebräisch 2,1,
JON.2.1–2.10 sind hebräisch 2,2–2,11 (die Tokens tragen die hebräische Stelle in «source_reference»).
Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, localize, write  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; aus dem hebräischen Text (WLC) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-JONAH"]
OBJ = "Objektzeichen אֶת, im Deutschen nicht wiedergegeben"
OBJ_G = "Objektzeiche אֶת, nöd übersetzbar"
Q = "Fragepartikel הֲ; im Deutschen durch die Satzstellung ausgedrückt"
Q_G = "Fragewort הֲ; dur d Satzstellig usdruckt"
LEMOR = "לֵאמֹר «um zu sagen» leitet die Rede ein; im Deutschen durch den Doppelpunkt wiedergegeben"
LEMOR_G = "לֵאמֹר «zum säge» leitet d Red ii; im Düütsche dur de Doppelpunkt usdruckt"

DE = {
 # ------------------------------------------------------------ Kapitel 1
 "JON.1.1": "Und{1} [es erging]{2} [das Wort]{3} [JHWHs]{4} [an]{5} [Jona]{6}, [den Sohn]{7} [Amittais]{8}: ~9(" + LEMOR + ") ~10(" + LEMOR + ")",
 "JON.1.2": "«[Steh auf]{1}, [geh]{2} [nach]{3} [Ninive]{4}, [der]{5,7} [grossen]{8} [Stadt]{6}, und{9} [ruf]{10} [gegen]{11} [sie]{12} [aus]{10}; [denn]{13} [ihre]{16} [Bosheit]{15} [ist]{14} [vor]{17} [mein]{19} [Angesicht]{18} [heraufgestiegen]{14}.»",
 "JON.1.3": "Da{1} [machte sich]{2} [Jona]{3} [auf]{2}, [um]{4} [nach]{7} [Tarschisch]{6} [zu fliehen]{5}, [weg vom Angesicht]{8,9,10} [JHWHs]{11}. Und{12} [er stieg hinab]{13} [nach Jafo]{14} und{15} [fand]{16} [ein Schiff]{17}, [das]{18} [nach Tarschisch]{19} [fuhr]{18}; und{20} [er bezahlte]{21} [das Fahrgeld]{22} [dafür]{23} und{24} [stieg]{25} [ins Schiff]{26,27} [hinab]{25}, [um]{28} [mit]{30} [ihnen]{31} [nach]{33} [Tarschisch]{32} [zu fahren]{29}, [weg vom Angesicht]{34,35,36} [JHWHs]{37}.",
 "JON.1.4": "Aber{1} [JHWH]{2} [schleuderte]{3} [einen grossen]{5} [Wind]{4} [auf]{6} [das]{7} [Meer]{8}, und{9} [es entstand]{10} [ein grosser]{12} [Sturm]{11} [auf dem]{13} [Meer]{14}, und{15} [das]{16} [Schiff]{17} [drohte]{18} [zu]{19} [zerbrechen]{20}.",
 "JON.1.5": "Da{1} [fürchteten sich]{2} [die]{3} [Seeleute]{4}, und{5} [sie schrien]{6}, [jeder]{7} [zu]{8} [seinem]{10} [Gott]{9}, und{11} [sie warfen]{12} [die]{14} [Ladung]{15}, [die]{16} [im]{17} [Schiff]{18} war, [ins]{19,20} [Meer]{21}, [um]{22} es [für sich]{24,25,26} [leichter zu machen]{23}. [Jona]{28} aber{27} [war]{29} [in]{30} [den innersten Raum]{31} [des]{32} [Schiffes]{33} [hinabgestiegen]{29} und{34} [hatte sich hingelegt]{35} und{36} [war in tiefen Schlaf gesunken]{37}. ~13(" + OBJ + ")",
 "JON.1.6": "Da{1} [trat]{2} [der Kapitän]{5,6,7} [zu]{3} [ihm]{4} [heran]{2} und{8} [sagte]{9} [zu]{10} [ihm]{11}: «[Was]{12} [ist mit]{13} [dir]{14}, [dass du schläfst]{15}? [Steh auf]{16}, [ruf]{17} [zu]{18} [deinem]{20} [Gott]{19}! [Vielleicht]{21} [denkt]{22} [der]{23} [Gott]{24} [an]{22} [uns]{25,26}, und{27} [wir gehen]{29} [nicht]{28} [zugrunde]{29}.»",
 "JON.1.7": "Und{1} [sie sagten]{2}, [einer]{3} [zum]{4} [andern]{5,6}: «[Kommt]{7}, und{8} [lasst uns]{9} [Lose]{10} [werfen]{9}, [damit]{11} [wir erfahren]{12}, [wessentwegen]{13-16} [dieses]{17,19,20} [Unheil]{18} [über uns]{21,22} gekommen ist!» Und{23} [sie warfen]{24} [Lose]{25}, und{26} [das]{28} [Los]{29} [fiel]{27} [auf]{30} [Jona]{31}.",
 "JON.1.8": "Da{1} [sagten sie]{2} [zu]{3} [ihm]{4}: «[Sag]{5,6} [uns]{8,9} [doch]{7}, [wessentwegen]{10-13} [dieses]{14,16,17} [Unheil]{15} [über uns]{18,19} gekommen ist! [Was]{20} ist [dein]{22} [Gewerbe]{21}, und{23} [woher]{24,25} [kommst du]{26}? [Was]{27} ist [dein]{29} [Land]{28}, und{30} [aus welchem]{31,32,33} [Volk]{34} [bist du]{35}?»",
 "JON.1.9": "Und{1} [er sagte]{2} [zu]{3} [ihnen]{4}: «[Ein Hebräer]{5} [bin ich]{6}, und{7} [JHWH]{9}, [den Gott]{10} [des]{11} [Himmels]{12}, [der]{13} [das]{16} [Meer]{17} und{18} [das]{20} [trockene Land]{21} [gemacht hat]{14}, [fürchte]{23} [ich]{22}.» ~8(" + OBJ + ") ~15(" + OBJ + ") ~19(" + OBJ + ")",
 "JON.1.10": "Da{1} [fürchteten sich]{2} [die]{3} [Männer]{4} [mit grosser]{6} [Furcht]{5} und{7} [sagten]{8} [zu]{9} [ihm]{10}: «[Was]{11} [hast du]{13} [da]{12} [getan]{13}!» [Denn]{14} [die]{16} [Männer]{17} [wussten]{15}, [dass]{18} [er]{23} [vor dem Angesicht]{19,20,21} [JHWHs]{22} [floh]{24}; [denn]{25} [er hatte]{26} es [ihnen]{27,28} [erzählt]{26}.",
 "JON.1.11": "Und{1} [sie sagten]{2} [zu]{3} [ihm]{4}: «[Was]{5} [sollen wir]{6} [mit]{7} [dir]{8} [tun]{6}, [damit]{9} [das]{11} [Meer]{12} [still wird]{10} [und von uns ablässt]{13,14,15}?» [Denn]{16} [das]{17} [Meer]{18} [wurde immer]{19,20} [stürmischer]{21}.",
 "JON.1.12": "Und{1} [er sagte]{2} [zu]{3} [ihnen]{4}: «[Hebt]{5} [mich]{6} [hoch]{5} und{7} [werft]{8} [mich]{9} [ins]{10,11} [Meer]{12}, [dann]{13} [wird]{14} [das]{15} [Meer]{16} [still]{14} [und von euch ablassen]{17,18,19}. [Denn]{20} [ich]{22} [weiss]{21}, [dass]{23} [meinetwegen]{24-27} [dieser]{32,33} [grosse]{30,31} [Sturm]{28,29} [über euch]{34,35} gekommen ist.»",
 "JON.1.13": "Und{1} [die]{3} [Männer]{4} [ruderten]{2}, [um]{5} [ans]{7,8} [trockene Land]{9} [zurückzukommen]{6}, aber{10} [sie konnten]{12} es [nicht]{11}; [denn]{13} [das]{14} [Meer]{15} [wurde]{16,17} [gegen sie]{19,20} [immer]{16,17} [stürmischer]{18}.",
 "JON.1.14": "Da{1} [riefen sie]{2} [zu]{3} [JHWH]{4} und{5} [sagten]{6}: «[Ach]{7}, [JHWH]{8}, [lass uns]{11} [doch]{10} [nicht]{9} [zugrunde gehen]{11} [wegen]{12} [des Lebens]{13} [dieses]{14,16,17} [Mannes]{15}, und{18} [leg]{20} [nicht]{19} [unschuldiges]{24} [Blut]{23} [auf]{21} [uns]{22}! [Denn]{25} [du]{27}, [JHWH]{26}, [hast getan]{31}, [wie]{28,29} [es dir gefallen hat]{30}.»",
 "JON.1.15": "Und{1} [sie hoben]{2} [Jona]{4} [hoch]{2} und{5} [warfen]{6} [ihn]{7} [ins]{8,9} [Meer]{10}. Da{11} [hörte]{12} [das]{13} [Meer]{14} [auf]{12} [mit]{15} [seinem]{17} [Toben]{16}. ~3(" + OBJ + ")",
 "JON.1.16": "Da{1} [fürchteten]{2} [die]{3} [Männer]{4} [JHWH]{8} [mit grosser]{6} [Furcht]{5}, und{9} [sie brachten]{10} [ein Schlachtopfer]{11} [für]{12} [JHWH]{13} [dar]{10} und{14} [gelobten]{15} [Gelübde]{16}. ~7(" + OBJ + ")",
 "JON.1.17": "Und{1} [JHWH]{3} [bestimmte]{2} [einen grossen]{5} [Fisch]{4}, [um]{6} [Jona]{9} [zu verschlingen]{7}. Und{10} [Jona]{12} [war]{11} [im]{13} [Bauch]{14} [des]{15} [Fisches]{16} [drei]{17} [Tage]{18} und{19} [drei]{20} [Nächte]{21}. ~8(" + OBJ + ")",
 # ------------------------------------------------------------ Kapitel 2 (hebräisch 2,2–11)
 "JON.2.1": "Und{1} [Jona]{3} [betete]{2} [zu]{4} [JHWH]{5}, [seinem]{7} [Gott]{6}, [aus]{8} [dem Bauch]{9} [des]{10} [Fisches]{11}.",
 "JON.2.2": "Und{1} [er sprach]{2}: «[Ich rief]{3} [aus]{4} [meiner]{6,7} [Not]{5} [zu]{8} [JHWH]{9}, und{10} [er antwortete]{11} [mir]{12}. [Aus]{13} [dem Schoss]{14} [des Totenreichs]{15} [schrie ich um Hilfe]{16} – [du hörtest]{17} [meine]{19} [Stimme]{18}.",
 "JON.2.3": "Und{1} [du warfst]{2} [mich]{3} [in die Tiefe]{4}, [ins]{5} [Herz]{6} [der Meere]{7}, und{8} [Strömung]{9} [umgab]{10} [mich]{11}; [alle]{12} [deine]{14} [Brecher]{13} und{15} [deine]{17} [Wellen]{16} [gingen]{20} [über]{18} [mich]{19} [hinweg]{20}.",
 "JON.2.4": "Und{1} [ich]{2} [dachte]{3}: [Verstossen bin ich]{4} [aus]{5,6} [deinen]{8} [Augen]{7}. [Doch]{9} [werde ich wieder]{10} [aufblicken]{11,12} [zu]{13} [deinem]{16} [heiligen]{15} [Tempel]{14}.",
 "JON.2.5": "[Wasser]{3} [umfing]{1} [mich]{2} [bis an]{4} [die Kehle]{5}, [die Urflut]{6} [umgab]{7} [mich]{8}, [Schilf]{9} [war]{10} [um]{11} [meinen]{13} [Kopf]{12} [gewunden]{10}.",
 "JON.2.6": "[Zu]{1} [den Wurzeln]{2} [der Berge]{3} [stieg ich hinab]{4}; [die]{5} [Erde]{6} – [ihre]{8} [Riegel]{7} [schlossen sich hinter]{9} [mir]{10} [für]{11} [immer]{12}. Da{13} [holtest du]{14} [mein]{18} [Leben]{17} [aus]{15} [der Grube]{16} [herauf]{14}, [JHWH]{19}, [mein]{21} [Gott]{20}.",
 "JON.2.7": "[Als]{1} [meine]{6} [Seele]{5} [in]{3} [mir]{4} [verschmachtete]{2}, [dachte ich an]{9} [JHWH]{8}, und{10} [mein]{15} [Gebet]{14} [kam]{11} [zu]{12} [dir]{13}, [in]{16} [deinen]{19} [heiligen]{18} [Tempel]{17}. ~7(" + OBJ + ")",
 "JON.2.8": "[Die sich an]{1} [nichtige]{3} [Götzen]{2} [halten]{1}, [verlassen]{6} [ihre]{5} [Treue]{4}.",
 "JON.2.9": "[Ich]{2} aber{1} [will]{6} [dir]{7,8} [mit]{3} [der Stimme]{4} [des Dankes]{5} [opfern]{6}; [was]{9} [ich gelobt habe]{10}, [will ich erfüllen]{11}. [Die Rettung]{12,13} [gehört]{14} [JHWH]{15}.»",
 "JON.2.10": "Da{1} [sprach]{2} [JHWH]{3} [zum]{4} [Fisch]{5}, und{6} [der spie]{7} [Jona]{9} [ans]{10,11} [trockene Land]{12} [aus]{7}. ~8(" + OBJ + ")",
 # ------------------------------------------------------------ Kapitel 3
 "JON.3.1": "Und{1} [es erging]{2} [das Wort]{3} [JHWHs]{4} [ein zweites Mal]{7} [an]{5} [Jona]{6}: ~8(" + LEMOR + ") ~9(" + LEMOR + ")",
 "JON.3.2": "«[Steh auf]{1}, [geh]{2} [nach]{3} [Ninive]{4}, [der]{5,7} [grossen]{8} [Stadt]{6}, und{9} [ruf]{10} [ihr]{11,12} [die]{14} [Botschaft]{15} [zu]{10}, [die]{16} [ich]{17} [dir]{19,20} [sage]{18}!» ~13(" + OBJ + ")",
 "JON.3.3": "Da{1} [machte sich]{2} [Jona]{3} [auf]{2} und{4} [ging]{5} [nach]{6} [Ninive]{7}, [nach]{8} [dem Wort]{9} [JHWHs]{10}. [Ninive]{12} aber{11} [war]{13} [eine Stadt]{14}, [gross]{15} [vor]{16} [Gott]{17}, [ein Weg]{18} [von drei]{19} [Tagen]{20}.",
 "JON.3.4": "Und{1} [Jona]{3} [begann]{2}, [in]{6} [die Stadt]{7} [hineinzugehen]{4,5}, [einen Weg]{8} [von einem]{10} [Tag]{9}, und{11} [er rief aus]{12} und{13} [sprach]{14}: «[Noch]{15} [vierzig]{16} [Tage]{17}, und{18} [Ninive]{19} [wird umgestürzt]{20}!»",
 "JON.3.5": "Da{1} [glaubten]{2} [die Leute]{3} [von Ninive]{4} [an]{5} [Gott]{6}, und{7} [sie riefen]{8} [ein Fasten]{9} [aus]{8} und{10} [zogen]{11} [Sacktuch]{12} [an]{11}, [vom]{13} [Grössten]{14,15} [bis zum]{16,17} [Kleinsten]{18,19}.",
 "JON.3.6": "Und{1} [die]{3} [Kunde]{4} [gelangte]{2} [zum]{5} [König]{6} [von Ninive]{7}; und{8} [er stand]{9} [von]{10} [seinem]{12} [Thron]{11} [auf]{9} und{13} [legte]{14} [seinen]{16} [Mantel]{15} [von sich]{17,18,19} [ab]{14} und{20} [hüllte sich]{21} [in Sacktuch]{22} und{23} [setzte sich]{24} [in]{25} [die]{26} [Asche]{27}.",
 "JON.3.7": "Und{1} [er liess ausrufen]{2} und{3} [sagen]{4} [in]{5} [Ninive]{6}: «[Auf Befehl]{7,8} [des]{9} [Königs]{10} und{11} [seiner]{13} [Grossen]{12}: [Mensch]{16,17} und{18} [Vieh]{19,20}, [Rind]{21,22} und{23} [Schaf]{24,25} [sollen]{27} [nicht]{26} [das Geringste]{28} [kosten]{27}; [sie sollen]{30} [nicht]{29} [weiden]{30}, und{31} [Wasser]{32} [sollen sie]{34} [nicht]{33} [trinken]{34}. ~14(" + LEMOR + ") ~15(" + LEMOR + ")",
 "JON.3.8": "Und{1} [sie sollen sich]{2} [in Sacktuch]{3} [hüllen]{2}, [Mensch]{4,5} und{6} [Vieh]{7,8}, und{9} [sie sollen]{10} [mit]{13} [aller Kraft]{14} [zu]{11} [Gott]{12} [rufen]{10}, und{15} [sie sollen umkehren]{16}, [jeder]{17} [von]{18} [seinem]{20} [bösen]{21,22} [Weg]{19} und{23} [von]{24} [der]{25} [Gewalttat]{26}, [die]{27} [an]{28} [ihren]{30} [Händen]{29} ist.",
 "JON.3.9": "[Wer]{1} [weiss]{2}, ob [Gott]{6,7} [umkehrt]{3} und{4} [es ihn reut]{5} und{8} [er sich abwendet]{9} [von]{10} [der Glut]{11} [seines]{13} [Zorns]{12}, und{14} [wir]{16} [nicht]{15} [zugrunde gehen]{16}.»",
 "JON.3.10": "Und{1} [Gott]{3,4} [sah]{2} [ihre]{7} [Taten]{6}, [dass]{8} [sie umkehrten]{9} [von]{10} [ihrem]{12} [bösen]{13,14} [Weg]{11}. Da{15} [reute]{16} [Gott]{17,18} [das]{19,20} [Unheil]{21}, [das]{22} [er angekündigt hatte]{23}, [ihnen]{26,27} [anzutun]{24,25}, und{28} [er tat es]{30} [nicht]{29}. ~5(" + OBJ + ")",
 # ------------------------------------------------------------ Kapitel 4
 "JON.4.1": "Das aber{1} [missfiel]{2} [Jona]{3,4} [mit grossem]{6} [Missfallen]{5}, und{7} [er wurde zornig]{8-10:idiom}.",
 "JON.4.2": "Und{1} [er betete]{2} [zu]{3} [JHWH]{4} und{5} [sagte]{6}: «[Ach]{7}, [JHWH]{8}, ist [das]{11} [nicht]{10} [mein]{13} [Wort]{12} gewesen, [solange]{14} [ich]{16} [in]{17} [meinem]{19} [Land]{18} [war]{15}? [Darum]{20,21} [bin ich]{22} [zuerst]{22} [nach]{26} [Tarschisch]{25} [geflohen]{23,24}; [denn]{27} [ich wusste]{28}, [dass]{29} [du]{30} [ein gnädiger]{32} und{33} [barmherziger]{34} [Gott]{31} bist, [langsam]{35} [zum Zorn]{36} und{37} [reich]{38} [an Treue]{39}, und{40} [dich]{41} [das]{42,43} [Unheil]{44} [reut]{41}. ~9(" + Q + ")",
 "JON.4.3": "[Und nun]{1,2}, [JHWH]{3}, [nimm]{4} [doch]{5} [mein]{8} [Leben]{7} [von]{9} [mir]{10}; [denn]{11} [besser]{12} ist [mein]{14} [Tod]{13} [als]{15} [mein]{17} [Leben]{16}.» ~6(" + OBJ + ")",
 "JON.4.4": "Und{1} [JHWH]{3} [sprach]{2}: «[Ist es recht]{4,5}, dass [du]{7,8} [zornig bist]{6}?»",
 "JON.4.5": "Und{1} [Jona]{3} [ging]{2} [aus]{4} [der]{5} [Stadt]{6} [hinaus]{2} und{7} [setzte sich]{8} [östlich]{9,10} [der Stadt]{11,12} hin. Und{13} [er machte]{14} [sich]{15,16} [dort]{17} [eine Hütte]{18}, und{19} [er sass]{20} [darunter]{21,22} [im]{23} [Schatten]{24}, [bis]{25,26} [er sähe]{27}, [was]{28} [in]{30} [der Stadt]{31} [geschehen würde]{29}.",
 "JON.4.6": "Und{1} [JHWH]{3} [Gott]{4} [bestimmte]{2} [einen Rizinus]{5}, und{6} [der wuchs]{7} [über]{8,9,10} [Jona]{11} [empor]{7}, [um]{12} [Schatten]{14} [über]{15} [seinem]{17} [Kopf]{16} [zu sein]{13}, [um]{18} [ihn]{20,21} [von]{22} [seinem]{24} [Unmut]{23} [zu retten]{19}. Und{25} [Jona]{27} [freute sich]{26} [über]{28} [den]{29} [Rizinus]{30} [mit grosser]{32} [Freude]{31}.",
 "JON.4.7": "Da{1} [bestimmte]{2} [Gott]{3,4} [einen Wurm]{5}, [als]{6} [die]{8} [Morgenröte]{9} [aufstieg]{7} [am]{10} [folgenden Tag]{11}, und{12} [der stach]{13} [den]{15} [Rizinus]{16}, und{17} [er verdorrte]{18}. ~14(" + OBJ + ")",
 "JON.4.8": "[Und es geschah]{1,2}, [als]{3} [die]{5} [Sonne]{6} [aufging]{4}, da{7} [bestimmte]{8} [Gott]{9} [einen sengenden]{12} [Ostwind]{10,11}, und{13} [die]{15} [Sonne]{16} [stach]{14} [auf]{17} [den Kopf]{18} [Jonas]{19}, und{20} [er wurde ohnmächtig]{21}. Und{22} [er wünschte]{23} [sich]{25,26} [zu sterben]{27,28} und{29} [sagte]{30}: «[Besser]{31} ist [mein]{33} [Tod]{32} [als]{34} [mein]{36} [Leben]{35}.» ~24(" + OBJ + ")",
 "JON.4.9": "Da{1} [sprach]{2} [Gott]{3} [zu]{4} [Jona]{5}: «[Ist es recht]{6,7}, dass [du]{9,10} [zornig bist]{8} [wegen]{11} [des]{12} [Rizinus]{13}?» Und{14} [er sagte]{15}: «[Mit Recht]{16} [bin ich]{18,19} [zornig]{17}, [bis]{20} [zum Tod]{21}!»",
 "JON.4.10": "Und{1} [JHWH]{3} [sprach]{2}: «[Du]{4} [hast Mitleid]{5} [mit]{6} [dem]{7} [Rizinus]{8}, [um den]{9,12,13} [du dich]{11} [nicht]{10} [abgemüht hast]{11} und{14} [den]{17} [du]{16} [nicht]{15} [grossgezogen hast]{16}, [der]{18} [in einer Nacht]{19,20:idiom} [entstand]{21} und{22} [in einer Nacht]{23,24:idiom} [zugrunde ging]{25}.",
 "JON.4.11": "Und{1} [ich]{2}, [sollte ich]{4} [nicht]{3} [Mitleid haben]{4} [mit]{5} [Ninive]{6}, [der]{7,9} [grossen]{10} [Stadt]{8}, [in der]{11,13,14} [mehr]{15} [als]{16} [hundertzwanzigtausend]{17,18,19} [Menschen]{20} [sind]{12}, [die]{21} [nicht]{22} [zwischen]{24} [ihrer]{26} [Rechten]{25} [und]{27} [ihrer]{29} [Linken]{28} [zu unterscheiden wissen]{23}, und{30} dazu [viel]{32} [Vieh]{31}?»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 1
 "JON.1.1": "Und{1} [es isch]{2} [s Wort]{3} [vo JHWH]{4} [zum]{5} [Jona]{6} [cho]{2}, [em Sohn]{7} [vom Amittai]{8}: ~9(" + LEMOR_G + ") ~10(" + LEMOR_G + ")",
 "JON.1.2": "«[Stand uf]{1}, [gang]{2} [uf]{3} [Ninive]{4}, [di]{5,7} [gross]{8} [Stadt]{6}, und{9} [rüef]{10} [gäge]{11} [si]{12} [us]{10}; [dänn]{13} [iri]{16} [Bosheit]{15} [isch]{14} [vor]{17} [mis]{19} [Aagsicht]{18} [ufegstige]{14}.»",
 "JON.1.3": "Da{1} [hät sich]{2} [de Jona]{3} [ufgmacht]{2}, [zum]{4} [uf]{7} [Tarschisch]{6} [z flüchte]{5}, [wäg vom Aagsicht]{8,9,10} [vo JHWH]{11}. Und{12} [er isch]{13} [uf Jafo]{14} [abegange]{13} und{15} [hät]{16} [es Schiff]{17} [gfunde]{16}, [wo]{18} [uf Tarschisch]{19} [gfaare isch]{18}; und{20} [er hät]{21} [s Faargält]{22} [defür]{23} [zaalt]{21} und{24} [isch]{25} [drii]{26,27} [abegstige]{25}, [zum]{28} [mit]{30} [ine]{31} [uf]{33} [Tarschisch]{32} [z faare]{29}, [wäg vom Aagsicht]{34,35,36} [vo JHWH]{37}.",
 "JON.1.4": "Aber{1} [JHWH]{2} [hät]{3} [en grosse]{5} [Wind]{4} [uf]{6} [s]{7} [Meer]{8} [gschleuderet]{3}, und{9} [es hät]{10} [en grosse]{12} [Sturm]{11} [uf em]{13} [Meer]{14} [ggää]{10}, und{15} [s]{16} [Schiff]{17} [isch nooch draa gsii]{18}, [z]{19} [verbräche]{20}.",
 "JON.1.5": "Da{1} [händ sich]{2} [d]{3} [Seelüüt]{4} [gfürchtet]{2}, und{5} [jede]{7} [hät]{6} [zu]{8} [sim]{10} [Gott]{9} [gschroue]{6}, und{11} [si händ]{12} [d]{14} [Ladig]{15}, [wo]{16} [im]{17} [Schiff]{18} gsii isch, [is]{19,20} [Meer]{21} [grüert]{12}, [zum]{22} es [für sich]{24,25,26} [liechter z mache]{23}. [De Jona]{28} aber{27} [isch]{29} [is]{30} [Innerscht]{31} [vom]{32} [Schiff]{33} [abegstige]{29} und{34} [hät sich higleit]{35} und{36} [isch tüüf iigschlaafe]{37}. ~13(" + OBJ_G + ")",
 "JON.1.6": "Da{1} [isch]{2} [de Kapitään]{5,6,7} [zu]{3} [im]{4} [häre cho]{2} und{8} [hät]{9} [zu]{10} [im]{11} [gseit]{9}: «[Was]{12} [isch mit]{13} [dir]{14}, [dass d schlaafsch]{15}? [Stand uf]{16}, [rüef]{17} [zu]{18} [dim]{20} [Gott]{19}! [Vilicht]{21} [dänkt]{22} [de]{23} [Gott]{24} [a]{22} [öis]{25,26}, und{27} [mir gönd]{29} [nöd]{28} [zgrund]{29}.»",
 "JON.1.7": "Und{1} [si händ]{2}, [eine]{3} [zum]{4} [andere]{5,6}, [gseit]{2}: «[Chömed]{7}, und{8} [mir wänd]{9} [Lös]{10} [wärfe]{9}, [demit]{11} [mir erfaared]{12}, [wäge wäm]{13-16} [das]{17,19,20} [Unheil]{18} [über öis]{21,22} cho isch!» Und{23} [si händ]{24} [Lös]{25} [gworfe]{24}, und{26} [s]{28} [Los]{29} [isch]{27} [uf]{30} [de Jona]{31} [gfalle]{27}.",
 "JON.1.8": "Da{1} [händ si]{2} [zu]{3} [im]{4} [gseit]{2}: «[Säg]{5,6} [öis]{8,9} [doch]{7}, [wäge wäm]{10-13} [das]{14,16,17} [Unheil]{15} [über öis]{18,19} cho isch! [Was]{20} isch [dis]{22} [Gwärb]{21}, und{23} [vo wo]{24,25} [chunnsch]{26}? [Was]{27} isch [dis]{29} [Land]{28}, und{30} [us wellem]{31,32,33} [Volk]{34} [bisch du]{35}?»",
 "JON.1.9": "Und{1} [er hät]{2} [zu]{3} [ine]{4} [gseit]{2}: «[En Hebräer]{5} [bin ich]{6}, und{7} [JHWH]{9}, [de Gott]{10} [vom]{11} [Himmel]{12}, [wo]{13} [s]{16} [Meer]{17} und{18} [s]{20} [troche Land]{21} [gmacht hät]{14}, [fürcht]{23} [ich]{22}.» ~8(" + OBJ_G + ") ~15(" + OBJ_G + ") ~19(" + OBJ_G + ")",
 "JON.1.10": "Da{1} [händ sich]{2} [d]{3} [Mane]{4} [mit ere grosse]{6} [Furcht]{5} [gfürchtet]{2} und{7} [händ]{8} [zu]{9} [im]{10} [gseit]{8}: «[Was]{11} [häsch du]{13} [da]{12} [gmacht]{13}!» [Dänn]{14} [d]{16} [Mane]{17} [händ gwüsst]{15}, [dass]{18} [er]{23} [vor em Aagsicht]{19,20,21} [vo JHWH]{22} [am Flüchte gsii isch]{24}; [dänn]{25} [er hät]{26} s [ine]{27,28} [verzellt]{26}.",
 "JON.1.11": "Und{1} [si händ]{2} [zu]{3} [im]{4} [gseit]{2}: «[Was]{5} [söled mir]{6} [mit]{7} [dir]{8} [mache]{6}, [demit]{9} [s]{11} [Meer]{12} [still wird]{10} [und vo öis ablaat]{13,14,15}?» [Dänn]{16} [s]{17} [Meer]{18} [isch immer]{19,20} [stürmischer worde]{21}.",
 "JON.1.12": "Und{1} [er hät]{2} [zu]{3} [ine]{4} [gseit]{2}: «[Lüpfed]{5} [mich]{6} [uf]{5} und{7} [rüered]{8} [mich]{9} [is]{10,11} [Meer]{12}, [dänn]{13} [wird]{14} [s]{15} [Meer]{16} [still]{14} [und laat vo eu ab]{17,18,19}. [Wil]{20} [ich]{22} [weiss]{21}, [dass]{23} [wäge mir]{24-27} [dä]{32,33} [gross]{30,31} [Sturm]{28,29} [über eu]{34,35} cho isch.»",
 "JON.1.13": "Und{1} [d]{3} [Mane]{4} [händ gruederet]{2}, [zum]{5} [as]{7,8} [troche Land]{9} [zruggzcho]{6}, aber{10} [si händ]{12} s [nöd]{11} [chöne]{12}; [dänn]{13} [s]{14} [Meer]{15} [isch]{16,17} [gäge si]{19,20} [immer]{16,17} [stürmischer worde]{18}.",
 "JON.1.14": "Da{1} [händ si]{2} [zu]{3} [JHWH]{4} [grüeft]{2} und{5} [gseit]{6}: «[Ach]{7}, [JHWH]{8}, [lass öis]{11} [doch]{10} [nöd]{9} [zgrund gaa]{11} [wäge]{12} [em Läbe]{13} [vo dem]{14,16,17} [Maa]{15}, und{18} [leg]{20} [nöd]{19} [unschuldigs]{24} [Bluet]{23} [uf]{21} [öis]{22}! [Dänn]{25} [du]{27}, [JHWH]{26}, [häsch gmacht]{31}, [wie]{28,29} [s dir gfalle hät]{30}.»",
 "JON.1.15": "Und{1} [si händ]{2} [de Jona]{4} [ufglüpft]{2} und{5} [händ]{6} [en]{7} [is]{8,9} [Meer]{10} [grüert]{6}. Da{11} [hät]{12} [s]{13} [Meer]{14} [mit]{15} [sim]{17} [Tobe]{16} [ufghört]{12}. ~3(" + OBJ_G + ")",
 "JON.1.16": "Da{1} [händ]{2} [d]{3} [Mane]{4} [JHWH]{8} [mit ere grosse]{6} [Furcht]{5} [gfürchtet]{2}, und{9} [si händ]{10} [für]{12} [JHWH]{13} [es Schlachtopfer]{11} [dargebracht]{10} und{14} [Glübd]{16} [abgleit]{15}. ~7(" + OBJ_G + ")",
 "JON.1.17": "Und{1} [JHWH]{3} [hät]{2} [en grosse]{5} [Fisch]{4} [bstellt]{2}, [zum]{6} [de Jona]{9} [z verschlucke]{7}. Und{10} [de Jona]{12} [isch]{11} [im]{13} [Buuch]{14} [vom]{15} [Fisch]{16} [gsii]{11}, [drei]{17} [Täg]{18} und{19} [drei]{20} [Nächt]{21}. ~8(" + OBJ_G + ")",
 # ------------------------------------------------------------ Kapitel 2 (hebräisch 2,2–11)
 "JON.2.1": "Und{1} [de Jona]{3} [hät]{2} [us]{8} [em Buuch]{9} [vom]{10} [Fisch]{11} [zu]{4} [JHWH]{5}, [sim]{7} [Gott]{6}, [bättet]{2}.",
 "JON.2.2": "Und{1} [er hät gseit]{2}: «[Ich han grüeft]{3} [us]{4} [minere]{6,7} [Not]{5} [zu]{8} [JHWH]{9}, und{10} [er hät]{11} [mir]{12} [ggantwortet]{11}. [Us]{13} [em Schooss]{14} [vom Toterich]{15} [han ich um Hilf gschroue]{16} – [du häsch]{17} [mini]{19} [Stimm]{18} [ghört]{17}.",
 "JON.2.3": "Und{1} [du häsch]{2} [mich]{3} [i d Tüüfi]{4} [gworfe]{2}, [is]{5} [Herz]{6} [vo de Meer]{7}, und{8} [Strömig]{9} [hät]{10} [mich]{11} [umgää]{10}; [all]{12} [dini]{14} [Brächer]{13} und{15} [dini]{17} [Wälle]{16} [sind]{20} [über]{18} [mich]{19} [ewäg gange]{20}.",
 "JON.2.4": "Und{1} [ich]{2} [han tänkt]{3}: [Verstosse bin ich]{4} [us]{5,6} [dine]{8} [Auge]{7}. [Doch]{9} [wird ich wider]{10} [ufluege]{11,12} [zu]{13} [dim]{16} [heilige]{15} [Tämpel]{14}.",
 "JON.2.5": "[Wasser]{3} [hät]{1} [mich]{2} [umfange]{1} [bis a]{4} [d Chäle]{5}, [d Urflut]{6} [hät]{7} [mich]{8} [umgää]{7}, [Schilf]{9} [isch]{10} [um]{11} [min]{13} [Chopf]{12} [gwicklet gsii]{10}.",
 "JON.2.6": "[Zu]{1} [de Wurzle]{2} [vo de Bärg]{3} [bin ich abegstige]{4}; [d]{5} [Erde]{6} – [iri]{8} [Riegel]{7} [händ sich hinder]{9} [mir]{10} [gschlosse]{9} [für]{11} [immer]{12}. Da{13} [häsch du]{14} [mis]{18} [Läbe]{17} [us]{15} [de Grueb]{16} [ufegholt]{14}, [JHWH]{19}, [min]{21} [Gott]{20}.",
 "JON.2.7": "[Wo]{1} [mini]{6} [Seel]{5} [i]{3} [mir]{4} [verschmachtet isch]{2}, [han ich a]{9} [JHWH]{8} [tänkt]{9}, und{10} [mis]{15} [Gebätt]{14} [isch]{11} [zu]{12} [dir]{13} [cho]{11}, [i]{16} [din]{19} [heilige]{18} [Tämpel]{17}. ~7(" + OBJ_G + ")",
 "JON.2.8": "[Die, wo sich a]{1} [nüütigi]{3} [Götze]{2} [hebed]{1}, [verlönd]{6} [iri]{5} [Tröii]{4}.",
 "JON.2.9": "[Ich]{2} aber{1} [wott]{6} [dir]{7,8} [mit]{3} [de Stimm]{4} [vom Dank]{5} [opfere]{6}; [was]{9} [ich versproche han]{10}, [wott ich iilöse]{11}. [D Rettig]{12,13} [ghört]{14} [JHWH]{15}.»",
 "JON.2.10": "Da{1} [hät]{2} [JHWH]{3} [zum]{4} [Fisch]{5} [gredt]{2}, und{6} [dä hät]{7} [de Jona]{9} [as]{10,11} [troche Land]{12} [usegchotzt]{7}. ~8(" + OBJ_G + ")",
 # ------------------------------------------------------------ Kapitel 3
 "JON.3.1": "Und{1} [es isch]{2} [s Wort]{3} [vo JHWH]{4} [es zweits Mal]{7} [zum]{5} [Jona]{6} [cho]{2}: ~8(" + LEMOR_G + ") ~9(" + LEMOR_G + ")",
 "JON.3.2": "«[Stand uf]{1}, [gang]{2} [uf]{3} [Ninive]{4}, [di]{5,7} [gross]{8} [Stadt]{6}, und{9} [rüef]{10} [ire]{11,12} [d]{14} [Botschaft]{15} [zue]{10}, [wo]{16} [ich]{17} [dir]{19,20} [säge]{18}!» ~13(" + OBJ_G + ")",
 "JON.3.3": "Da{1} [hät sich]{2} [de Jona]{3} [ufgmacht]{2} und{4} [isch]{5} [uf]{6} [Ninive]{7} [gange]{5}, [nach]{8} [em Wort]{9} [vo JHWH]{10}. [Ninive]{12} aber{11} [isch]{13} [e Stadt]{14} [gsii]{13}, [gross]{15} [vor]{16} [Gott]{17}, [en Wäg]{18} [vo drei]{19} [Täg]{20}.",
 "JON.3.4": "Und{1} [de Jona]{3} [hät aagfange]{2}, [i]{6} [d Stadt]{7} [ine z gaa]{4,5}, [en Wäg]{8} [vo eim]{10} [Taag]{9}, und{11} [er hät usgrüeft]{12} und{13} [gseit]{14}: «[No]{15} [vierzg]{16} [Täg]{17}, und{18} [Ninive]{19} [wird umgstürzt]{20}!»",
 "JON.3.5": "Da{1} [händ]{2} [d Lüüt]{3} [vo Ninive]{4} [a]{5} [Gott]{6} [glaubt]{2}, und{7} [si händ]{8} [es Faschte]{9} [usgrüeft]{8} und{10} [händ]{11} [Sacktuech]{12} [aagleit]{11}, [vom]{13} [Gröschte]{14,15} [bis zum]{16,17} [Chliinschte]{18,19}.",
 "JON.3.6": "Und{1} [d]{3} [Nachricht]{4} [isch]{2} [zum]{5} [König]{6} [vo Ninive]{7} [cho]{2}; und{8} [er isch]{9} [vo]{10} [sim]{12} [Troon]{11} [ufgstande]{9} und{13} [hät]{14} [sin]{16} [Mantel]{15} [vo sich]{17,18,19} [abzoge]{14} und{20} [hät sich]{21} [in Sacktuech]{22} [ghüllt]{21} und{23} [sich]{24} [i]{25} [d]{26} [Äsche]{27} [gsetzt]{24}.",
 "JON.3.7": "Und{1} [er hät la usrüefe]{2} und{3} [säge]{4} [z]{5} [Ninive]{6}: «[Uf Befeel]{7,8} [vom]{9} [König]{10} und{11} [vo sine]{13} [Grosse]{12}: [Mänsch]{16,17} und{18} [Vee]{19,20}, [Rind]{21,22} und{23} [Schaf]{24,25} [söled]{27} [nöd]{26} [s Gringscht]{28} [verchoschte]{27}; [si söled]{30} [nöd]{29} [weide]{30}, und{31} [Wasser]{32} [söled si]{34} [nöd]{33} [trinke]{34}. ~14(" + LEMOR_G + ") ~15(" + LEMOR_G + ")",
 "JON.3.8": "Und{1} [si söled sich]{2} [in Sacktuech]{3} [hülle]{2}, [Mänsch]{4,5} und{6} [Vee]{7,8}, und{9} [si söled]{10} [mit]{13} [aller Chraft]{14} [zu]{11} [Gott]{12} [rüefe]{10}, und{15} [si söled umchere]{16}, [jede]{17} [vo]{18} [sim]{20} [böse]{21,22} [Wäg]{19} und{23} [vo]{24} [de]{25} [Gwalt]{26}, [wo]{27} [a]{28} [ire]{30} [Händ]{29} isch.",
 "JON.3.9": "[Wär]{1} [weiss]{2}, öb [Gott]{6,7} [umcheert]{3} und{4} [es en reut]{5} und{8} [er sich abwändet]{9} [vo]{10} [de Gluet]{11} [vo sim]{13} [Zorn]{12}, und{14} [mir]{16} [nöd]{15} [zgrund gönd]{16}.»",
 "JON.3.10": "Und{1} [Gott]{3,4} [hät]{2} [ires]{7} [Tue]{6} [gsee]{2}, [dass]{8} [si umgcheert sind]{9} [vo]{10} [irem]{12} [böse]{13,14} [Wäg]{11}. Da{15} [hät s]{16} [Gott]{17,18} [greut]{16} [wäge em]{19,20} [Unheil]{21}, [wo]{22} [er aagchündt hät]{23}, [ine]{26,27} [aaztue]{24,25}, und{28} [er hät s]{30} [nöd]{29} [gmacht]{30}. ~5(" + OBJ_G + ")",
 # ------------------------------------------------------------ Kapitel 4
 "JON.4.1": "Das aber{1} [isch]{2} [em Jona]{3,4} [bös]{2} [vorcho]{2}, [en grosse]{6} [Ärger]{5}, und{7} [er isch toub worde]{8-10:idiom}.",
 "JON.4.2": "Und{1} [er hät]{2} [zu]{3} [JHWH]{4} [bättet]{2} und{5} [gseit]{6}: «[Ach]{7}, [JHWH]{8}, isch [das]{11} [nöd]{10} [mis]{13} [Wort]{12} gsii, [solang]{14} [ich]{16} [i]{17} [mim]{19} [Land]{18} [gsii bin]{15}? [Drum]{20,21} [bin ich]{22} [zersch]{22} [uf]{26} [Tarschisch]{25} [gflüchtet]{23,24}; [dänn]{27} [ich han gwüsst]{28}, [dass]{29} [du]{30} [en gnädige]{32} und{33} [barmhärzige]{34} [Gott]{31} bisch, [langsam]{35} [zum Zorn]{36} und{37} [riich]{38} [a Tröii]{39}, und{40} [dich]{41} [s]{42,43} [Unheil]{44} [reut]{41}. ~9(" + Q_G + ")",
 "JON.4.3": "[Und jetzt]{1,2}, [JHWH]{3}, [nimm]{4} [doch]{5} [mis]{8} [Läbe]{7} [vo]{9} [mir]{10}; [dänn]{11} [besser]{12} isch [min]{14} [Tod]{13} [als]{15} [mis]{17} [Läbe]{16}.» ~6(" + OBJ_G + ")",
 "JON.4.4": "Und{1} [JHWH]{3} [hät gseit]{2}: «[Isch es rächt]{4,5}, dass [du]{7,8} [toub bisch]{6}?»",
 "JON.4.5": "Und{1} [de Jona]{3} [isch]{2} [us]{4} [de]{5} [Stadt]{6} [use gange]{2} und{7} [hät sich]{8} [östlich]{9,10} [vo de Stadt]{11,12} [anegsetzt]{8}. Und{13} [er hät]{14} [sich]{15,16} [dört]{17} [e Hütte]{18} [gmacht]{14}, und{19} [isch]{20} [drunder]{21,22} [im]{23} [Schatte]{24} [gsässe]{20}, [bis]{25,26} [er gseet]{27}, [was]{28} [i]{30} [de Stadt]{31} [passiert]{29}.",
 "JON.4.6": "Und{1} [JHWH]{3} [Gott]{4} [hät]{2} [en Rizinus]{5} [bstellt]{2}, und{6} [dä isch]{7} [über]{8,9,10} [de Jona]{11} [ufegwachse]{7}, [zum]{12} [Schatte]{14} [über]{15} [sim]{17} [Chopf]{16} [z sii]{13}, [zum]{18} [en]{20,21} [vo]{22} [sim]{24} [Unmuet]{23} [z rette]{19}. Und{25} [de Jona]{27} [hät sich]{26} [über]{28} [de]{29} [Rizinus]{30} [gfröit]{26}, [mit ere grosse]{32} [Fröid]{31}.",
 "JON.4.7": "Da{1} [hät]{2} [Gott]{3,4} [en Wurm]{5} [bstellt]{2}, [wo]{6} [d]{8} [Morgeröti]{9} [ufgange isch]{7} [am]{10} [nächschte Taag]{11}, und{12} [dä hät]{13} [de]{15} [Rizinus]{16} [gstoche]{13}, und{17} [er isch verdorret]{18}. ~14(" + OBJ_G + ")",
 "JON.4.8": "[Und es isch gscheh]{1,2}, [wo]{3} [d]{5} [Sunne]{6} [ufgange isch]{4}, da{7} [hät]{8} [Gott]{9} [en heisse]{12} [Oschtwind]{10,11} [bstellt]{8}, und{13} [d]{15} [Sunne]{16} [hät]{14} [uf]{17} [de Chopf]{18} [vom Jona]{19} [gstoche]{14}, und{20} [er isch ohnmächtig worde]{21}. Und{22} [er hät]{23} [sich]{25,26} [gwünscht]{23}, [z sterbe]{27,28}, und{29} [gseit]{30}: «[Besser]{31} isch [min]{33} [Tod]{32} [als]{34} [mis]{36} [Läbe]{35}.» ~24(" + OBJ_G + ")",
 "JON.4.9": "Da{1} [hät]{2} [Gott]{3} [zum]{4} [Jona]{5} [gseit]{2}: «[Isch es rächt]{6,7}, dass [du]{9,10} [toub bisch]{8} [wäge]{11} [em]{12} [Rizinus]{13}?» Und{14} [er hät gseit]{15}: «[Mit Rächt]{16} [bin ich]{18,19} [toub]{17}, [bis]{20} [in Tod]{21}!»",
 "JON.4.10": "Und{1} [JHWH]{3} [hät gseit]{2}: «[Du]{4} [häsch Mitleid]{5} [mit]{6} [em]{7} [Rizinus]{8}, [wo]{9} [du dich]{11} [nöd]{10} [drum]{12,13} [abgmüet häsch]{11} und{14} [wo]{17} [du]{16} [nöd]{15} [groozoge häsch]{16}, [wo]{18} [i ere Nacht]{19,20:idiom} [worde isch]{21} und{22} [i ere Nacht]{23,24:idiom} [zgrund gange isch]{25}.",
 "JON.4.11": "Und{1} [ich]{2}, [sött ich]{4} [nöd]{3} [Mitleid ha]{4} [mit]{5} [Ninive]{6}, [de]{7,9} [grosse]{10} [Stadt]{8}, [wo]{11} [mee]{15} [als]{16} [hundertzwänzgtuusig]{17,18,19} [Mänsche]{20} [drin]{13,14} [sind]{12}, [wo]{21} [nöd]{22} [zwüsche]{24} [irer]{26} [Rächte]{25} [und]{27} [irer]{29} [Linke]{28} [chönd underscheide]{23}, und{30} dezue [vill]{32} [Vee]{31}?»",
}

JHWH_DE = ("Der Gottesname wird im Judentum nicht ausgesprochen; gelesen wird «Adonai» (der Herr). Viele deutsche Bibeln schreiben "
           "«der HERR». Hier steht der Name in seinen vier Konsonanten, damit sichtbar bleibt, dass im Hebräischen ein Name steht.")
JHWH_GSW = ("De Gottesname wird im Judetum nöd usgsproche; gläse wird «Adonai» (de Herr). Vili düütschi Bible schriibed «der HERR». "
            "Da staat de Name i sine vier Konsonante, demit me gseet, dass im Hebräische en Name staat.")
RAA_DE = ("רָעָה ist ein Leitwort des Buches. Die Wurzel רעע «böse, schlecht sein» steht in Jona zehnmal (nach den Lemmata von MACULA: "
          "Nomen רָעָה 7×, Adjektiv רַע 2×, Verb רָעַע 1×; das gleich geschriebene רָעָה «weiden» in [[JON.3.7]] ist ein anderes Wort): "
          "die «Bosheit» Ninives ([[JON.1.2]]), das «Unheil» des Sturms ([[JON.1.7]], [[JON.1.8]]), der «böse» Weg der Niniviten "
          "([[JON.3.8]], [[JON.3.10]]), das «Unheil», das Gott angekündigt hat und das ihn reut ([[JON.3.10]], [[JON.4.2]]), Jonas "
          "«Missfallen» ([[JON.4.1]]) und sein «Unmut» ([[JON.4.6]]). Das Deutsche braucht verschiedene Wörter; im Hebräischen verknüpft "
          "das eine Wort die Erzählung.")
RAA_GSW = ("רָעָה isch es Leitwort vom Buech. D Wurzle רעע «bös, schlächt sii» staat im Jona zäämal (nach de Lemmata vo MACULA: "
           "Nomen רָעָה 7×, Adjektiv רַע 2×, Verb רָעַע 1×; s gliich gschribne רָעָה «weide» i [[JON.3.7]] isch es anders Wort): "
           "d «Bosheit» vo Ninive ([[JON.1.2]]), s «Unheil» vom Sturm ([[JON.1.7]], [[JON.1.8]]), de «bös» Wäg vo de Niniviter "
           "([[JON.3.8]], [[JON.3.10]]), s «Unheil», wo Gott aagchündt hät und wo en reut ([[JON.3.10]], [[JON.4.2]]), de «Ärger» vom "
           "Jona ([[JON.4.1]]) und sin «Unmuet» ([[JON.4.6]]). Im Düütsche bruucht s verschideni Wörter; im Hebräische verbindet s eine "
           "Wort d Erzählig.")
NIHAM_DE = ("נִחַם (Nifal) meint, dass jemand eine Absicht oder ein angekündigtes Urteil aus innerer Bewegung zurücknimmt. «Reuen» ist "
            "die traditionelle Wiedergabe; sie setzt bei Gott keine Schuld voraus. [[JER.18.8]] beschreibt genau diesen Fall: Kehrt ein Volk "
            "von seiner Bosheit um, so reut Gott das angedrohte Unheil. Wie sich das zu [[NUM.23.19]] und [[1SA.15.29]] («Gott ist nicht ein "
            "Mensch, dass ihn etwas reute») verhält, wird in der Auslegung verschieden beantwortet. Das Wort steht in Jona dreimal "
            "([[JON.3.9]], [[JON.3.10]], [[JON.4.2]]).")
NIHAM_GSW = ("נִחַם (Nifal) meint, dass öpper e Absicht oder es aagchündts Urteil us innerer Bewegig zruggnimmt. «Reue» isch di "
             "traditionell Widergaab; si setzt bi Gott kei Schuld voruus. [[JER.18.8]] beschriibt grad dä Fall: Wänn es Volk vo sinere "
             "Bosheit umcheert, dänn reut Gott s aadroote Unheil. Wie sich das zu [[NUM.23.19]] und [[1SA.15.29]] verhaltet, beantwortet "
             "d Uslegig verschide. S Wort staat im Jona drüümal ([[JON.3.9]], [[JON.3.10]], [[JON.4.2]]).")

# Übersetzungsentscheidungen: (Stelle, Zieltext, Art, hebräisch, wörtlicher, andere Möglichkeiten, Begründung)
DEC_DE = [
 # Kapitel 1
 ("JON.1.1", "Jona", "literal", "יוֹנָה", None, None,
  "Der Name bedeutet «Taube». Ein Prophet Jona, Sohn Amittais, aus Gat-Hefer wird in [[2KI.14.25]] zur Zeit Jerobeams II. (8. Jh. v. Chr.) "
  "erwähnt. Ob das Buch diesen Propheten historisch meint oder eine bekannte Gestalt in eine Lehrerzählung stellt, ist umstritten."),
 ("JON.1.1", "JHWHs", "interpretive", "יְהוָה", None, ["des HERRN", "des Ewigen", "Jahwes"], JHWH_DE),
 ("JON.1.2", "grossen", "literal", "הָעִיר הַגְּדוֹלָה", None, None,
  "«Die grosse Stadt» ist eine Leitformel des Buches ([[JON.1.2]], [[JON.3.2]], [[JON.3.3]], [[JON.4.11]]). Das Wort גָּדוֹל «gross» steht in "
  "Jona 14-mal (nach den Lemmata von MACULA): Stadt, Wind, Sturm, Furcht, Fisch, «vom Grössten bis zum Kleinsten», die Grossen Ninives, Missfallen, Freude. Darum steht im "
  "Deutschen möglichst immer «gross»."),
 ("JON.1.2", "Bosheit", "interpretive", "רָעָתָם", "ihr Böses", ["ihre Schlechtigkeit"], RAA_DE),
 ("JON.1.2", "gegen", "literal", "עָלֶיהָ", None, ["über sie"],
  "קָרָא עַל «ausrufen gegen, über». In [[JON.3.2]] steht dagegen קְרָא אֵלֶיהָ «ruf ihr zu»; ob der Wechsel etwas bedeutet, ist umstritten."),
 ("JON.1.3", "weg vom Angesicht", "literal", "מִלִּפְנֵי", None, ["vor JHWH weg", "aus der Gegenwart JHWHs"],
  "Die Wendung steht zweimal in 1,3 und wieder in [[JON.1.10]]. Manche verstehen sie so, dass Jona sich dem Dienst «vor JHWH» entzieht (vgl. "
  "[[1KI.17.1]] «vor dem ich stehe»); andere so, dass er das Land verlassen will, in dem JHWH verehrt wird. Dass Jona JHWH für den Schöpfer "
  "von Meer und Land hält, sagt er selbst ([[JON.1.9]])."),
 ("JON.1.3", "Tarschisch", "literal", "תַּרְשִׁישָׁה", None, None,
  "Tarschisch liegt im fernen Westen am Meer; oft wird es mit Tartessos in Südspanien gleichgesetzt, sicher ist die Lage nicht. Jona flieht in "
  "die Gegenrichtung zu Ninive im Osten."),
 ("JON.1.3", "er stieg hinab", "literal", "וַיֵּרֶד", "er ging hinab", None,
  "«Hinabsteigen» (יָרַד) zieht sich durch die Flucht: nach Jafo, ins Schiff ([[JON.1.3]]), in den innersten Raum ([[JON.1.5]]) und im Gebet "
  "bis zu den Wurzeln der Berge ([[JON.2.6]]). Darum steht im Deutschen jedes Mal «hinab»."),
 ("JON.1.4", "schleuderte", "literal", "הֵטִיל", None, ["warf"],
  "Dasselbe Verb steht für das Werfen der Ladung ([[JON.1.5]]) und Jonas ([[JON.1.12]], [[JON.1.15]])."),
 ("JON.1.4", "drohte", "interpretive", "חִשְּׁבָה", "das Schiff dachte daran", ["war nahe daran"],
  "Wörtlich «das Schiff dachte, zu zerbrechen»: Das Schiff wird wie ein denkendes Wesen beschrieben."),
 ("JON.1.5", "Gott", "interpretive", "אֱלֹהָיו", None, ["seinen Göttern"],
  "אֱלֹהִים kann «Gott» oder «Götter» heissen; gemeint sind die Götter der verschiedenen Seeleute."),
 ("JON.1.5", "Ladung", "interpretive", "הַכֵּלִים", "die Geräte", ["die Gegenstände", "die Fracht"],
  "כְּלִי ist jedes Gerät oder Gefäss; hier wohl Ausrüstung und Fracht."),
 ("JON.1.5", "Schiffes", "literal", "הַסְּפִינָה", None, None,
  "Hier steht סְפִינָה statt אֳנִיָּה wie sonst im Kapitel; das Wort ist im Alten Testament sonst nicht belegt (allgemeines Wissen, nicht an "
  "Daten geprüft). Vielleicht ist ein Schiff mit Deck gemeint."),
 ("JON.1.5", "war in tiefen Schlaf gesunken", "literal", "וַיֵּרָדַם", None, ["schlief fest"],
  "רָדַם «in tiefen Schlaf sinken» klingt an יָרַד «hinabsteigen» an: Jona sinkt immer tiefer. Dasselbe Verb steht z. B. in [[JDG.4.21]]."),
 ("JON.1.6", "der Kapitän", "adapted", "רַב הַחֹבֵל", "der Oberste der Seeleute", ["der Schiffsführer"],
  "חֹבֵל ist der Seemann (vermutlich «der mit den Tauen»)."),
 ("JON.1.6", "Steh auf", "literal", "קוּם", None, None,
  "Der Kapitän sagt zu Jona dieselben Worte wie Gott in [[JON.1.2]]: «Steh auf … ruf»."),
 ("JON.1.6", "denkt", "interpretive", "יִתְעַשֵּׁת", None, ["sich besinnt auf uns", "sich um uns kümmert"],
  "Seltenes Verb; die Bedeutung «an jemanden denken» wird aus dem Zusammenhang und aus dem Aramäischen erschlossen."),
 ("JON.1.6", "zugrunde", "literal", "נֹאבֵד", None, ["umkommen"],
  "אָבַד «zugrunde gehen» kehrt wieder ([[JON.1.14]], [[JON.3.9]]) und zuletzt beim Rizinus ([[JON.4.10]])."),
 ("JON.1.7", "Unheil", "interpretive", "הָרָעָה", "das Böse", None, "Dasselbe Wort wie «Bosheit» in [[JON.1.2]]; siehe dort."),
 ("JON.1.9", "Ein Hebräer", "literal", "עִבְרִי", None, ["Ein Knecht JHWHs"],
  "Bezeichnung für Israeliten, meist im Gespräch mit Fremden oder aus ihrem Mund (z. B. [[GEN.39.14]], [[1SA.4.6]]). Die Septuaginta liest "
  "«Knecht des Herrn» (nach allgemeinem Wissen, nicht an Daten geprüft)."),
 ("JON.1.9", "fürchte", "interpretive", "יָרֵא", None, ["verehre"],
  "יָרֵא meint hier Gottesfurcht im Sinn von Verehrung. «Fürchten» bleibt stehen, weil das Wort die Szene verbindet: Die Seeleute fürchten "
  "sich ([[JON.1.5]]), fürchten sich «mit grosser Furcht» ([[JON.1.10]]) und fürchten am Ende JHWH ([[JON.1.16]]). Jona bekennt die "
  "Gottesfurcht, die Seeleute zeigen sie."),
 ("JON.1.10", "mit grosser", "literal", "יִרְאָה גְדוֹלָה", "sie fürchteten eine grosse Furcht", ["fürchteten sich sehr"],
  "Das Hebräische verstärkt das Verb mit dem verwandten Nomen; ebenso in [[JON.1.16]], [[JON.4.1]] und [[JON.4.6]]."),
 ("JON.1.11", "und von uns ablässt", "adapted", "מֵעָלֵינוּ", "von über uns weg", None,
  "Wörtlich «damit das Meer still werde von über uns weg»."),
 ("JON.1.11", "wurde immer", "literal", "הוֹלֵךְ וְסֹעֵר", "ging und stürmte", None,
  "הָלַךְ mit einem zweiten Partizip beschreibt eine zunehmende Bewegung; ebenso in [[JON.1.13]]."),
 ("JON.1.13", "ruderten", "interpretive", "וַיַּחְתְּרוּ", "sie gruben", ["sie ruderten mit aller Kraft"],
  "חָתַר heisst sonst «durchbrechen, einbrechen»; hier das angestrengte Rudern gegen die Wellen."),
 ("JON.1.14", "des Lebens", "literal", "בְּנֶפֶשׁ", None, ["wegen dieses Mannes"],
  "Die Seeleute bitten, für den Tod Jonas nicht als Mörder zu gelten."),
 ("JON.1.16", "Schlachtopfer", "literal", "זֶבַח", None, None,
  "Wo und wann die Seeleute opfern, sagt der Text nicht. Aus der Furcht vor dem Sturm ([[JON.1.5]]) ist Furcht vor JHWH geworden."),
 ("JON.1.17", "bestimmte", "interpretive", "וַיְמַן", None, ["bereitete", "beorderte", "liess kommen"],
  "מָנָה (Piel) heisst «zuteilen, bestimmen». Das Wort steht in Jona viermal (nach MACULA): beim Fisch und bei Rizinus, Wurm und Ostwind "
  "([[JON.4.6]], [[JON.4.7]], [[JON.4.8]]). Gott verfügt über Tiere, Pflanzen und Wetter."),
 ("JON.1.17", "Fisch", "literal", "דָּג", None, ["Wal", "Seeungeheuer"],
  "Der Text sagt «ein grosser Fisch» (דָּג גָּדוֹל) und nennt keine Art. Die Septuaginta sagt κῆτος «grosses Meerestier» (nach allgemeinem "
  "Wissen); daher steht in [[MAT.12.40]] und vielen Übersetzungen «Wal». Ob der Fisch eher Strafe oder Rettung ist, wird verschieden gedeutet; "
  "im Gebet ([[JON.2.6]]) erscheint die Rettung als Heraufholen aus der Tiefe. Die «drei Tage und drei Nächte» nimmt [[MAT.12.40]] auf."),
 # Kapitel 2
 ("JON.2.1", "Fisches", "literal", "הַדָּגָה", None, None,
  "Hier steht die weibliche Form דָּגָה, in [[JON.1.17]] und [[JON.2.10]] דָּג. Meist gilt das als gleichbedeutende Nebenform. Eine jüdische "
  "Auslegungstradition, die Raschi zur Stelle aufnimmt, erzählt daraus, Jona sei in einen zweiten, weiblichen Fisch gebracht worden."),
 ("JON.2.2", "Ich rief", "interpretive", "קָרָאתִי", None, ["Ich rufe"],
  "Das Gebet ([[JON.2.2]]–[[JON.2.9]]) ist als Danklied eines Einzelnen gestaltet: Es blickt auf Not, Hilferuf und Rettung zurück "
  "(Vergangenheitsformen) und endet mit Opfer, Gelübde und Bekenntnis ([[JON.2.9]]). Viele Wendungen erinnern an Psalmen (z. B. [[PSA.120.1]], "
  "[[PSA.18.6]], [[PSA.42.7]], [[PSA.69.1]]). Umstritten ist, ob das Lied ursprünglich zur Erzählung gehörte und wie es zu Jonas Lage passt: "
  "Manche lesen das Verschlungenwerden durch den Fisch schon als Rettung aus dem Ertrinken; andere sehen eine gewollte Spannung, weil Jona "
  "dankt, ohne seine Flucht zu erwähnen. Hier wird keine Deutung festgelegt."),
 ("JON.2.2", "des Totenreichs", "interpretive", "שְׁאוֹל", "der Scheol", ["der Unterwelt"],
  "שְׁאוֹל ist im Alten Testament der Ort der Toten. Jona beschreibt seine Lage im Wasser als Todesnähe."),
 ("JON.2.3", "Strömung", "interpretive", "נָהָר", "ein Strom", ["Flut"],
  "נָהָר ist sonst der Fluss; im Meer ist wohl die Strömung gemeint. Der zweite Teil des Verses stimmt wörtlich mit [[PSA.42.7]] überein."),
 ("JON.2.4", "Doch", "interpretive", "אַךְ", None, ["Wie werde ich je wieder …?"],
  "אַךְ heisst «doch, gewiss». Einige Ausleger ändern einen Buchstaben und lesen אֵיךְ «wie?»: «Wie soll ich je wieder aufblicken …?» Dann "
  "wäre der Satz Klage, nicht Zuversicht. Die Übersetzung folgt dem überlieferten Text."),
 ("JON.2.4", "Tempel", "literal", "הֵיכַל", None, None, "Gemeint ist der Tempel in Jerusalem, vielleicht zugleich Gottes himmlische Wohnung."),
 ("JON.2.5", "die Kehle", "interpretive", "נֶפֶשׁ", None, ["das Leben", "die Seele"],
  "נֶפֶשׁ bezeichnet ursprünglich Kehle und Atem, dann das Leben. «Bis an die Kehle» beschreibt das Ertrinken; vgl. [[PSA.69.1]]."),
 ("JON.2.5", "die Urflut", "literal", "תְּהוֹם", None, ["die Tiefe"], "תְּהוֹם ist die Urflut, wie in [[GEN.1.2]]."),
 ("JON.2.5", "Schilf", "interpretive", "סוּף", None, ["Seetang", "Algen"],
  "סוּף ist das Schilf (vgl. יַם סוּף «Schilfmeer»); hier wohl Meerespflanzen."),
 ("JON.2.6", "den Wurzeln", "interpretive", "קִצְבֵי", "den Enden", ["den Gründen"],
  "Die Berge gelten als im Urmeer gegründet; Jona steigt bis zu ihrem untersten Ende hinab."),
 ("JON.2.6", "der Grube", "interpretive", "שַׁחַת", None, ["dem Verderben"], "שַׁחַת ist die Grube, ein Bild für Grab und Totenwelt."),
 ("JON.2.8", "Götzen", "interpretive", "הַבְלֵי שָׁוְא", "Hauche der Nichtigkeit", ["nichtige Götter", "leeren Trug"],
  "הֶבֶל «Hauch» steht oft für Götzen (z. B. [[DEU.32.21]]); dieselbe Wendung steht in [[PSA.31.6]]."),
 ("JON.2.8", "Treue", "interpretive", "חַסְדָּם", None, ["ihre Gnade", "den, der ihnen treu ist"],
  "Wörtlich «ihre Treue» (חֶסֶד). Entweder geben sie die Treue auf, die sie Gott schulden, oder sie verlassen den, der ihnen Treue erweist. "
  "Manche lesen den Satz als Spitze gegen die Heiden – die Seeleute und die Niniviten handeln im Buch aber gerade nicht so; das kann man als "
  "Ironie verstehen."),
 ("JON.2.9", "der Stimme", "literal", "בְּקוֹל", None, ["mit lautem Dank"], "תּוֹדָה ist der Dank und zugleich das Dankopfer."),
 ("JON.2.9", "gehört", "interpretive", "לַיהוָה", "ist JHWHs", ["kommt von JHWH", "ist bei JHWH"],
  "Ein bekenntnishafter Schluss; vgl. [[PSA.3.8]]."),
 ("JON.2.10", "der spie", "literal", "וַיָּקֵא", None, ["warf … aus"], "קִיא heisst «erbrechen»; der Ausdruck ist drastisch."),
 # Kapitel 3
 ("JON.3.2", "ihr", "interpretive", "אֵלֶיהָ", None, ["gegen sie"],
  "Hier steht אֵלֶיהָ «zu ihr», in [[JON.1.2]] עָלֶיהָ «gegen sie». Manche sehen darin einen Wechsel von der Anklage zur Ansprache; die "
  "beiden Präpositionen werden aber oft gleichbedeutend gebraucht."),
 ("JON.3.2", "Botschaft", "literal", "הַקְּרִיאָה", "den Ruf", ["Predigt"],
  "קְרִיאָה ist mit קָרָא «rufen» verwandt und nur hier belegt (allgemeines Wissen, nicht an Daten geprüft). Was Jona ausrufen soll, wird erst "
  "in [[JON.3.4]] hörbar."),
 ("JON.3.3", "vor", "interpretive", "לֵאלֹהִים", "gross für Gott", ["eine überaus grosse Stadt", "gross in Gottes Augen"],
  "Die Wendung kann eine Steigerung sein («göttlich gross», d. h. riesig; vgl. [[GEN.23.6]], [[GEN.30.8]]). Sie kann aber auch heissen, dass "
  "Ninive für Gott gross, also wichtig ist; darauf läuft das Buch in [[JON.4.11]] hinaus. Beide Lesarten sind möglich; die Übersetzung lässt "
  "den Wortlaut stehen."),
 ("JON.3.3", "von drei", "interpretive", "מַהֲלַךְ שְׁלֹשֶׁת יָמִים", None, ["drei Tagereisen gross"],
  "Unklar ist, ob drei Tage den Durchmesser, den Umfang oder die Zeit für einen Gang durch alle Teile meinen. Das historische Ninive war nach "
  "Ausgrabungen deutlich kleiner (allgemeines Wissen, nicht an Daten geprüft); viele lesen die Angabe darum als erzählerische Grösse."),
 ("JON.3.4", "vierzig", "literal", "אַרְבָּעִים", None, ["drei"],
  "Die Septuaginta liest «noch drei Tage» (nach allgemeinem Wissen, nicht an Daten geprüft). Jonas ganze Botschaft umfasst im Hebräischen "
  "fünf Wörter."),
 ("JON.3.4", "wird umgestürzt", "interpretive", "נֶהְפָּכֶת", None, ["wird zerstört", "wird umgewendet"],
  "הָפַךְ ist das Wort für den Untergang Sodoms ([[GEN.19.25]]). Es kann aber auch «umwenden, verwandeln» heissen (z. B. [[EXO.7.17]]). So "
  "lässt sich der Satz im Nachhinein doppeldeutig lesen: Ninive wird «umgewendet» – nicht zerstört, sondern verändert. Ob der Erzähler das "
  "beabsichtigt, ist offen."),
 ("JON.3.5", "glaubten", "literal", "וַיַּאֲמִינוּ", None, ["vertrauten"],
  "הֶאֱמִין בְּ «glauben an, vertrauen auf»; dieselbe Wendung wie bei Abraham ([[GEN.15.6]])."),
 ("JON.3.5", "Sacktuch", "adapted", "שַׂקִּים", "Säcke", ["Trauerkleider"],
  "Grober Stoff, meist aus Ziegenhaar, als Zeichen von Trauer und Busse getragen."),
 ("JON.3.7", "Auf Befehl", "literal", "מִטַּעַם", None, ["Auf Erlass"],
  "טַעַם (eigentlich «Geschmack, Urteil») ist hier der amtliche Erlass, wie im Aramäischen. Im selben Vers steht das verwandte Verb טָעַם "
  "«kosten»; ein Wortspiel ist möglich."),
 ("JON.3.8", "Vieh", "literal", "בְּהֵמָה", None, None,
  "Auch die Tiere sollen fasten und Sacktuch tragen. Das kann man als übersteigerte, fast komische Darstellung lesen oder als Zeichen, dass "
  "die ganze Stadt samt Tieren in die Busse einbezogen ist; vgl. das Vieh in [[JON.4.11]]."),
 ("JON.3.8", "sie sollen umkehren", "literal", "וְיָשֻׁבוּ", None, ["sich abwenden"],
  "שׁוּב «umkehren» verbindet [[JON.3.8]]–[[JON.3.10]]: Die Menschen sollen umkehren, vielleicht «kehrt» Gott «um» ([[JON.3.9]]), und sie "
  "kehren um ([[JON.3.10]])."),
 ("JON.3.8", "Gewalttat", "literal", "הֶחָמָס", None, ["Unrecht"],
  "חָמָס ist rohe Gewalt und Unrecht; mit diesem Wort wird auch die Schuld vor der Flut benannt ([[GEN.6.11]])."),
 ("JON.3.9", "Wer", "literal", "מִי יוֹדֵעַ", None, ["Vielleicht"],
  "«Wer weiss, ob er umkehrt und es ihn reut» steht fast gleich in [[JOL.2.14]]: Busse erzwingt Gottes Erbarmen nicht, sie hofft darauf."),
 ("JON.3.9", "es ihn reut", "interpretive", "וְנִחַם", None, ["es tut ihm leid", "er ändert seinen Entschluss", "er erbarmt sich"], NIHAM_DE),
 ("JON.3.9", "der Glut", "literal", "חֲרוֹן אַפּוֹ", "der Glut seiner Nase", None,
  "Der Zorn wird im Hebräischen mit der schnaubenden Nase verbunden."),
 ("JON.3.10", "reute", "interpretive", "וַיִּנָּחֶם", None, ["tat leid", "liess ab"], "Siehe [[JON.3.9]]."),
 ("JON.3.10", "Unheil", "interpretive", "הָרָעָה", "das Böse", None,
  "Dasselbe Wort wie beim «bösen» Weg: Weil sie von ihrem Bösen umkehren, lässt Gott von dem Bösen ab, das er angekündigt hatte."),
 # Kapitel 4
 ("JON.4.1", "missfiel", "interpretive", "וַיֵּרַע רָעָה גְדוֹלָה", "es war böse für Jona, ein grosses Böses", ["es verdross Jona sehr"],
  "Das Wort רָעָה, von dem Ninive umgekehrt ist und das Gott nicht getan hat, trifft nun Jona: Gottes Erbarmen ist für ihn ein «grosses "
  "Übel». Siehe [[JON.1.2]]."),
 ("JON.4.1", "er wurde zornig", "adapted", "וַיִּחַר לוֹ", "es entbrannte ihm", None, "Feste Wendung für Zorn; ebenso in [[JON.4.4]] und [[JON.4.9]]."),
 ("JON.4.2", "er betete", "literal", "וַיִּתְפַּלֵּל", None, None,
  "Dasselbe Verb wie in [[JON.2.1]]; diesmal ist das Gebet eine Klage über Gottes Erbarmen."),
 ("JON.4.2", "zuerst", "interpretive", "קִדַּמְתִּי", "ich kam zuvor", ["darum bin ich eilends geflohen"],
  "Jona wollte dem zuvorkommen, was er von Gott erwartete."),
 ("JON.4.2", "ein gnädiger", "traditional", "חַנּוּן וְרַחוּם", None, ["huldvoll und mitfühlend"],
  "Jona zitiert das Gottesbekenntnis aus [[EXO.34.6]] (dort in umgekehrter Reihenfolge «barmherzig und gnädig»). Genau dieselbe Reihe mit dem "
  "Schluss «und es reut ihn das Unheil» steht in [[JOL.2.13]]; vgl. [[PSA.86.15]], [[PSA.103.8]], [[NEH.9.17]]. Was Israel tröstet, nennt "
  "Jona als Grund seiner Flucht."),
 ("JON.4.2", "langsam", "literal", "אֶרֶךְ אַפַּיִם", "lang an Nase", ["geduldig", "langmütig"],
  "«Lang an Nase (Atem)» heisst: Der Zorn kommt nicht schnell."),
 ("JON.4.2", "an Treue", "interpretive", "חֶסֶד", None, ["an Gnade", "an Güte", "an Huld"],
  "Wie im Buch Rut steht für חֶסֶד «Treue»: verlässliche Zuwendung, die mehr gibt als geschuldet; vgl. [[JON.2.8]]."),
 ("JON.4.2", "reut", "interpretive", "וְנִחָם", None, ["es tut dir leid um"], "Siehe [[JON.3.9]]."),
 ("JON.4.3", "Leben", "interpretive", "נַפְשִׁי", None, ["meine Seele"],
  "Wie Elija ([[1KI.19.4]]) bittet Jona um den Tod. Der Vergleich wird verschieden ausgewertet: Elija ist erschöpft und verfolgt, Jona ärgert "
  "sich über Gottes Erbarmen."),
 ("JON.4.4", "Ist es recht", "interpretive", "הַהֵיטֵב", None, ["Bist du sehr zornig?"],
  "הֵיטֵב kann «gut, recht» oder verstärkend «sehr» heissen. Die Septuaginta versteht «Bist du sehr betrübt?» (nach allgemeinem Wissen, nicht an "
  "Daten geprüft). Jona antwortet hier nicht."),
 ("JON.4.5", "setzte sich", "interpretive", "וַיֵּשֶׁב", None, ["hatte sich gesetzt"],
  "Manche halten 4,5 für eine Rückblende: Jona wäre schon während der vierzig Tage hinausgegangen. Andere lesen der Reihe nach: Jona wartet "
  "trotz Gottes Entscheidung, ob doch noch etwas geschieht."),
 ("JON.4.5", "eine Hütte", "literal", "סֻכָּה", None, ["eine Laubhütte"], "סֻכָּה ist eine Hütte aus Zweigen, wie beim Laubhüttenfest."),
 ("JON.4.6", "JHWH", "literal", "יְהוָה אֱלֹהִים", None, None,
  "Nur hier steht im Buch die Verbindung «JHWH Gott» ohne Suffix (wie in [[GEN.2.4]] und den folgenden Kapiteln). Sonst wechseln «JHWH», "
  "«Gott» und «der Gott»; ob der Wechsel eine Bedeutung trägt, wird verschieden beurteilt."),
 ("JON.4.6", "einen Rizinus", "interpretive", "קִיקָיוֹן", None, ["einen Kürbis", "einen Flaschenkürbis", "einen Efeu", "einen Wunderbaum"],
  "Die Pflanze ist nicht sicher bestimmbar; das Wort kommt nur in Jona 4 vor (fünfmal nach MACULA). Oft wird an den schnell wachsenden "
  "Rizinus (Wunderbaum) gedacht. Die Septuaginta sagt «Kürbis», Hieronymus übersetzte in der Vulgata «Efeu»; Augustinus schrieb ihm deswegen "
  "(Brief 71), weil die neue Wiedergabe in einer Gemeinde Unruhe ausgelöst hatte. Für die Aussage ist der Name der Pflanze nebensächlich."),
 ("JON.4.6", "Unmut", "interpretive", "מֵרָעָתוֹ", "seinem Bösen", ["seinem Unglück", "seinem Elend"],
  "Wieder das Leitwort רָעָה ([[JON.1.2]]); gemeint ist wohl Jonas Missmut ([[JON.4.1]]), vielleicht auch das Leiden unter der Hitze."),
 ("JON.4.6", "zu retten", "literal", "לְהַצִּיל", None, ["zu befreien"], "הִצִּיל ist ein gewöhnliches Wort für Rettung."),
 ("JON.4.7", "stach", "interpretive", "וַתַּךְ", "schlug", ["nagte an"], "נָכָה (Hifil) «schlagen»; dasselbe Verb für die Sonne in [[JON.4.8]]."),
 ("JON.4.8", "sengenden", "interpretive", "חֲרִישִׁית", None, ["schwülen", "stillen"],
  "Das Wort ist sonst nicht belegt (allgemeines Wissen, nicht an Daten geprüft); die Bedeutung «heiss, sengend» ist erschlossen."),
 ("JON.4.8", "Ostwind", "literal", "רוּחַ קָדִים", None, None, "Der heisse Wind aus der Wüste."),
 ("JON.4.8", "er wurde ohnmächtig", "interpretive", "וַיִּתְעַלָּף", None, ["er wurde schwach"], "Er wurde matt bis zur Bewusstlosigkeit."),
 ("JON.4.9", "zum Tod", "literal", "עַד מָוֶת", None, ["sterbenselend"], "Die Wendung verstärkt: zornig bis zum Sterben."),
 ("JON.4.10", "hast Mitleid", "interpretive", "חַסְתָּ", None, ["es jammert dich um", "du schonst"],
  "חוּס heisst «Mitleid haben, verschonen»; dasselbe Verb steht in Gottes Gegenfrage [[JON.4.11]]."),
 ("JON.4.10", "in einer Nacht", "adapted", "בִּן לַיְלָה", "Sohn einer Nacht", None,
  "Das Hebräische drückt Herkunft und Alter mit «Sohn» aus."),
 ("JON.4.10", "zugrunde ging", "literal", "אָבָד", None, ["verdarb"],
  "Dasselbe Verb wie «zugrunde gehen» in [[JON.1.6]], [[JON.1.14]] und [[JON.3.9]]."),
 ("JON.4.11", "Mitleid haben", "interpretive", "אָחוּס", None, None,
  "Der Satz hat keine Fragepartikel; dass er eine Frage ist, ergibt sich aus dem Zusammenhang. Als Aussage («Ich aber habe kein Mitleid …») "
  "passt er kaum zum Buch. Das Buch endet mit dieser Frage; eine Antwort Jonas wird nicht erzählt."),
 ("JON.4.11", "hundertzwanzigtausend", "adapted", "שְׁתֵּים עֶשְׂרֵה רִבּוֹ", "zwölf Zehntausende", None,
  "רִבּוֹ ist eine Zehntausend. Ob die Zahl die ganze Bevölkerung oder nur die kleinen Kinder meint, hängt an der Deutung der folgenden "
  "Wendung."),
 ("JON.4.11", "zu unterscheiden wissen", "interpretive", "לֹא יָדַע בֵּין", "nicht wissen zwischen", None,
  "Die Wendung kann kleine Kinder meinen, die rechts und links noch nicht unterscheiden; dann wäre die Gesamtzahl viel grösser. Oder sie meint "
  "alle Einwohner, die Gottes Weisung nicht kennen und darum Recht und Unrecht nicht unterscheiden können. Beides wird vertreten."),
 ("JON.4.11", "Vieh", "literal", "בְהֵמָה", None, None,
  "Das Buch endet mit «viel Vieh»: Gottes Mitleid schliesst auch die Tiere ein (vgl. [[JON.3.7]], [[PSA.36.6]])."),
]

DEC_GSW = [
 # Kapitel 1
 ("JON.1.1", "Jona", "literal", "יוֹנָה", None, None,
  "De Name heisst «Tube». En Prophet Jona, Sohn vom Amittai, us Gat-Hefer wird i [[2KI.14.25]] zur Ziit vom Jerobeam II. (8. Jh. v. Chr.) "
  "erwäänt. Öb s Buech dä Prophet historisch meint oder e bekannti Gstalt in e Leererzählig stellt, isch umstritte."),
 ("JON.1.1", "vo JHWH", "interpretive", "יְהוָה", None, ["vom HERR", "vom Ewige", "vo Jahwe"], JHWH_GSW),
 ("JON.1.2", "gross", "literal", "הָעִיר הַגְּדוֹלָה", None, None,
  "«Di gross Stadt» isch e Leitformle vom Buech ([[JON.1.2]], [[JON.3.2]], [[JON.3.3]], [[JON.4.11]]). S Wort גָּדוֹל «gross» staat im Jona "
  "14-mal (nach de Lemmata vo MACULA): Stadt, Wind, Sturm, Furcht, Fisch, «vom Gröschte bis zum Chliinschte», di Grosse vo Ninive, Ärger, Fröid."),
 ("JON.1.2", "Bosheit", "interpretive", "רָעָתָם", "ires Böse", ["iri Schlächtigkeit"], RAA_GSW),
 ("JON.1.2", "gäge", "literal", "עָלֶיהָ", None, ["über si"],
  "קָרָא עַל «usrüefe gäge». I [[JON.3.2]] staat dergäge קְרָא אֵלֶיהָ «rüef ire zue»; öb de Wächsel öppis bedüütet, isch umstritte."),
 ("JON.1.3", "wäg vom Aagsicht", "literal", "מִלִּפְנֵי", None, ["vor JHWH wäg"],
  "Di Wändig staat zweimal i 1,3 und wider i [[JON.1.10]]. Die einte verstönd s so, dass sich de Jona em Dienscht «vor JHWH» entziet (vgl. "
  "[[1KI.17.1]]); anderi so, dass er s Land wott verlaa, wo JHWH verehrt wird."),
 ("JON.1.3", "Tarschisch", "literal", "תַּרְשִׁישָׁה", None, None,
  "Tarschisch liit im wiite Weschte am Meer; oft dänkt me a Tartessos z Südspanie, sicher isch das nöd. De Jona flüchtet i di anderi "
  "Richtig als Ninive im Oschte."),
 ("JON.1.3", "abegange", "literal", "וַיֵּרֶד", None, None,
  "«Abegaa» (יָרַד) ziet sich dur d Flucht: uf Jafo, is Schiff ([[JON.1.3]]), is Innerscht ([[JON.1.5]]) und im Gebätt bis zu de Wurzle vo "
  "de Bärg ([[JON.2.6]])."),
 ("JON.1.4", "gschleuderet", "literal", "הֵטִיל", None, ["grüert"],
  "S gliich Verb staat für s Rüere vo de Ladig ([[JON.1.5]]) und vom Jona ([[JON.1.12]], [[JON.1.15]])."),
 ("JON.1.4", "isch nooch draa gsii", "interpretive", "חִשְּׁבָה", "s Schiff hät tänkt", None,
  "Wörtlich «s Schiff hät tänkt, z verbräche»: S Schiff wird wie öppis beschribe, wo dänkt."),
 ("JON.1.5", "Gott", "interpretive", "אֱלֹהָיו", None, ["sine Götter"], "אֱלֹהִים cha «Gott» oder «Götter» heisse."),
 ("JON.1.5", "isch tüüf iigschlaafe", "literal", "וַיֵּרָדַם", None, None,
  "רָדַם «tüüf iischlaafe» tönt wie יָרַד «abegaa»: De Jona sinkt immer tüüfer."),
 ("JON.1.6", "de Kapitään", "adapted", "רַב הַחֹבֵל", "de Oberscht vo de Seelüüt", None, "חֹבֵל isch de Seemaa."),
 ("JON.1.6", "Stand uf", "literal", "קוּם", None, None, "De Kapitään seit em Jona di gliiche Wort wie Gott i [[JON.1.2]]: «Stand uf … rüef»."),
 ("JON.1.6", "dänkt", "interpretive", "יִתְעַשֵּׁת", None, ["sich um öis kümmeret"],
  "Es seltes Verb; d Bedüütig wird us em Zämehang und us em Aramäische erschlosse."),
 ("JON.1.7", "Unheil", "interpretive", "הָרָעָה", "s Böse", None, "S gliich Wort wie «Bosheit» i [[JON.1.2]]."),
 ("JON.1.9", "En Hebräer", "literal", "עִבְרִי", None, ["En Chnächt vo JHWH"],
  "So nänned sich Israelite vor allem gägenüber Frömde (z. B. [[GEN.39.14]], [[1SA.4.6]]). D Septuaginta liest «Chnächt vom Herr» (nach "
  "allgemeinem Wüsse, nöd a Date prüeft)."),
 ("JON.1.9", "fürcht", "interpretive", "יָרֵא", None, ["verehr"],
  "Gmeint isch Gottesfurcht. «Fürchte» bliibt staa, wil s Wort d Szene verbindet: D Seelüüt fürched sich ([[JON.1.5]]), fürched sich «mit ere "
  "grosse Furcht» ([[JON.1.10]]) und fürched am Schluss JHWH ([[JON.1.16]])."),
 ("JON.1.10", "mit ere grosse", "literal", "יִרְאָה גְדוֹלָה", "si händ e grossi Furcht gfürchtet", None,
  "S Hebräisch verstercht s Verb mit em verwandte Nomen; ebeso i [[JON.1.16]], [[JON.4.1]] und [[JON.4.6]]."),
 ("JON.1.13", "händ gruederet", "interpretive", "וַיַּחְתְּרוּ", "si händ grabe", None,
  "חָתַר heisst suscht «durebräche»; da s aagsträngte Ruedere gäge d Wälle."),
 ("JON.1.17", "bstellt", "interpretive", "וַיְמַן", None, ["parat gmacht", "la cho"],
  "מָנָה heisst «zueteile, bestimme». S Wort staat im Jona viermal (nach MACULA): bim Fisch und bim Rizinus, Wurm und Oschtwind ([[JON.4.6]], "
  "[[JON.4.7]], [[JON.4.8]]). Gott verfüegt über Tier, Pflanze und Wätter."),
 ("JON.1.17", "Fisch", "literal", "דָּג", None, ["Wal"],
  "De Text seit «en grosse Fisch» und nännt kei Art. D Septuaginta seit κῆτος «grosses Meertier» (nach allgemeinem Wüsse); drum staat i "
  "[[MAT.12.40]] und i vilne Übersetzige «Wal». D «drei Täg und drei Nächt» nimmt [[MAT.12.40]] uf."),
 # Kapitel 2
 ("JON.2.1", "Fisch", "literal", "הַדָּגָה", None, None,
  "Da staat di wiiblich Form דָּגָה, i [[JON.1.17]] und [[JON.2.10]] דָּג. Meischtens gilt das als gliichbedüütendi Nebeform; e jüdischi "
  "Uslegigstradition, wo de Raschi ufnimmt, verzellt drus vo me zweite, wiibliche Fisch."),
 ("JON.2.2", "Ich han grüeft", "interpretive", "קָרָאתִי", None, ["Ich rüef"],
  "S Gebätt ([[JON.2.2]]–[[JON.2.9]]) isch als Dankliid vo me Einzelne gstaltet: Es luegt uf Not, Hilferuef und Rettig zrugg und hört mit "
  "Opfer, Versproche und Bekänntnis uf ([[JON.2.9]]). Vili Wändige erinnered a Psalme (z. B. [[PSA.120.1]], [[PSA.18.6]], [[PSA.42.7]], "
  "[[PSA.69.1]]). Umstritte isch, öb s Liid vo Aafang aa zur Erzählig ghört hät und wie s zu de Lag vom Jona passt: Die einte läsed s "
  "Verschluckt-Wärde dur de Fisch scho als Rettig us em Vertränke; anderi gsänd e gwollti Spannig, wil de Jona danket, ohni sini Flucht z "
  "erwääne. Da wird kei Dütig feschtgleit."),
 ("JON.2.2", "vom Toterich", "interpretive", "שְׁאוֹל", "vo de Scheol", ["vo de Underwält"],
  "שְׁאוֹל isch im Alte Teschtamänt de Ort vo de Tote."),
 ("JON.2.3", "Strömig", "interpretive", "נָהָר", "en Strom", None,
  "נָהָר isch suscht de Fluss; im Meer isch wohl d Strömig gmeint. De zweit Teil vom Vers stimmt wörtlich mit [[PSA.42.7]] überii."),
 ("JON.2.4", "Doch", "interpretive", "אַךְ", None, ["Wie söll ich je wider …?"],
  "אַךְ heisst «doch, sicher». Es paar Usleger änderet en Buechstabe und läsed אֵיךְ «wie?»; dänn wär de Satz e Chlag. D Übersetzig "
  "folgt em überlieferete Text."),
 ("JON.2.5", "d Chäle", "interpretive", "נֶפֶשׁ", None, ["s Läbe", "d Seel"],
  "נֶפֶשׁ isch zersch Chäle und Ate, dänn s Läbe. «Bis a d Chäle» beschriibt s Vertränke; vgl. [[PSA.69.1]]."),
 ("JON.2.5", "d Urflut", "literal", "תְּהוֹם", None, ["d Tüüfi"], "תְּהוֹם isch d Urflut wie i [[GEN.1.2]]."),
 ("JON.2.8", "Götze", "interpretive", "הַבְלֵי שָׁוְא", "Hüüch vo de Nüütigkeit", ["nüütigi Götter"],
  "הֶבֶל «Hauch» staat oft für Götze (z. B. [[DEU.32.21]]); di gliich Wändig i [[PSA.31.6]]."),
 ("JON.2.8", "Tröii", "interpretive", "חַסְדָּם", None, ["iri Gnad"],
  "Wörtlich «iri Tröii» (חֶסֶד): Entweder gänd si d Tröii uf, wo si Gott schuldig sind, oder si verlönd dä, wo ine tröi isch."),
 ("JON.2.9", "ghört", "interpretive", "לַיהוָה", "isch vo JHWH", ["chunnt vo JHWH"], "En bekänntnishafte Schluss; vgl. [[PSA.3.8]]."),
 ("JON.2.10", "usegchotzt", "literal", "וַיָּקֵא", "erbroche", ["usgspeut"], "קִיא heisst «erbräche»; de Usdruck isch drastisch."),
 # Kapitel 3
 ("JON.3.2", "ire", "interpretive", "אֵלֶיהָ", None, ["gäge si"],
  "Da staat אֵלֶיהָ «zu ire», i [[JON.1.2]] עָלֶיהָ «gäge si». Di beide Präpositione wärded aber oft gliichbedüütend bruucht."),
 ("JON.3.3", "vor", "interpretive", "לֵאלֹהִים", "gross für Gott", ["e riisegrossi Stadt", "gross i de Auge vo Gott"],
  "D Wändig cha e Steigerig sii («göttlich gross», also riisig; vgl. [[GEN.23.6]], [[GEN.30.8]]). Si cha aber au heisse, dass Ninive für "
  "Gott gross, also wichtig isch; dörthi lauft s Buech i [[JON.4.11]]. Beides isch möglich."),
 ("JON.3.3", "vo drei", "interpretive", "מַהֲלַךְ שְׁלֹשֶׁת יָמִים", None, None,
  "Unklar isch, öb drei Täg de Durchmässer, de Umfang oder d Ziit für en Gang dur alli Teil meined. S historisch Ninive isch nach de "
  "Usgrabige vill chliiner gsii (allgemeis Wüsse, nöd a Date prüeft)."),
 ("JON.3.4", "vierzg", "literal", "אַרְבָּעִים", None, ["drei"],
  "D Septuaginta liest «no drei Täg» (nach allgemeinem Wüsse, nöd a Date prüeft). D ganz Botschaft vom Jona sind im Hebräische füüf Wörter."),
 ("JON.3.4", "wird umgstürzt", "interpretive", "נֶהְפָּכֶת", None, ["wird zerstört", "wird umgcheert"],
  "הָפַךְ isch s Wort für de Undergang vo Sodom ([[GEN.19.25]]). Es cha aber au «umchere, verwandle» heisse (z. B. [[EXO.7.17]]). So cha "
  "me de Satz im Nachhinein doppelsinnig läse: Ninive wird «umgcheert» – nöd zerstört, sondern veränderet."),
 ("JON.3.5", "glaubt", "literal", "וַיַּאֲמִינוּ", None, ["vertraut"], "Di gliich Wändig wie bim Abraham ([[GEN.15.6]])."),
 ("JON.3.5", "Sacktuech", "adapted", "שַׂקִּים", "Säck", ["Truurchleider"], "Grobe Stoff, als Zeiche vo Truur und Buess treit."),
 ("JON.3.7", "Uf Befeel", "literal", "מִטַּעַם", None, None,
  "טַעַם (eigentlich «Gschmack, Urteil») isch da de amtlich Erlass. Im gliiche Vers staat s verwandt Verb טָעַם «verchoschte»."),
 ("JON.3.8", "si söled umchere", "literal", "וְיָשֻׁבוּ", None, None,
  "שׁוּב «umchere» verbindet [[JON.3.8]]–[[JON.3.10]]: D Mänsche söled umchere, vilicht «cheert» Gott «um» ([[JON.3.9]]), und si chered um "
  "([[JON.3.10]])."),
 ("JON.3.8", "Gwalt", "literal", "הֶחָמָס", None, ["Unrächt"], "חָמָס isch roochi Gwalt; mit dem Wort wird au d Schuld vor de Sintflut gnännt ([[GEN.6.11]])."),
 ("JON.3.9", "Wär", "literal", "מִי יוֹדֵעַ", None, ["Vilicht"],
  "Fascht gliich staat s i [[JOL.2.14]]: Buess zwingt Gott nöd zum Erbarme, si hofft druf."),
 ("JON.3.9", "es en reut", "interpretive", "וְנִחַם", None, ["es tuet im leid", "er änderet sin Entschluss"], NIHAM_GSW),
 ("JON.3.10", "greut", "interpretive", "וַיִּנָּחֶם", None, ["leid taa"], "Lueg [[JON.3.9]]."),
 ("JON.3.10", "Unheil", "interpretive", "הָרָעָה", "s Böse", None,
  "S gliich Wort wie bim «böse» Wäg: Wil si vo irem Böse umchered, laat Gott vom Böse ab, wo n er aagchündt hät."),
 # Kapitel 4
 ("JON.4.1", "bös", "interpretive", "וַיֵּרַע רָעָה גְדוֹלָה", "es isch bös gsii für de Jona, es grosses Böses", None,
  "S Wort רָעָה, vo dem Ninive umgcheert isch und wo Gott nöd gmacht hät, trifft jetzt de Jona: S Erbarme vo Gott isch für in es «grosses "
  "Übel». Lueg [[JON.1.2]]."),
 ("JON.4.2", "en gnädige", "traditional", "חַנּוּן וְרַחוּם", None, None,
  "De Jona zitiert s Gottesbekänntnis us [[EXO.34.6]] (dört umgcheert «barmhärzig und gnädig»). Genau di gliich Reie mit em Schluss «und es "
  "reut en s Unheil» staat i [[JOL.2.13]]; vgl. [[PSA.86.15]], [[PSA.103.8]], [[NEH.9.17]]. Was Israel tröschtet, nännt de Jona als Grund "
  "für sini Flucht."),
 ("JON.4.2", "langsam", "literal", "אֶרֶךְ אַפַּיִם", "lang a de Nase", ["gedultig"], "«Lang a de Nase (Ate)» heisst: De Zorn chunnt nöd schnäll."),
 ("JON.4.2", "a Tröii", "interpretive", "חֶסֶד", None, ["a Gnad", "a Güeti"], "Wie im Buech Rut staat für חֶסֶד «Tröii»; vgl. [[JON.2.8]]."),
 ("JON.4.4", "Isch es rächt", "interpretive", "הַהֵיטֵב", None, ["Bisch du seer toub?"],
  "הֵיטֵב cha «guet, rächt» oder verstercht «seer» heisse. De Jona git da kei Antwort."),
 ("JON.4.5", "anegsetzt", "interpretive", "וַיֵּשֶׁב", None, None,
  "Es paar halted 4,5 für e Ruggbländ (de Jona wär scho während de vierzg Täg usegange); anderi läsed s der Reie nach."),
 ("JON.4.6", "en Rizinus", "interpretive", "קִיקָיוֹן", None, ["en Chürbis", "en Efeu", "en Wunderbaum"],
  "D Pflanze cha me nöd sicher bestimme; s Wort chunnt nu i Jona 4 vor (füüfmal nach MACULA). D Septuaginta seit «Chürbis», de Hieronymus "
  "hät i de Vulgata «Efeu» übersetzt; de Augustinus hät im deswäge gschribe (Brief 71), wil di nöi Widergaab i ere Gmeind Unrue usglöst hät."),
 ("JON.4.6", "Unmuet", "interpretive", "מֵרָעָתוֹ", "sim Böse", ["sim Unglück"],
  "Wider s Leitwort רָעָה ([[JON.1.2]]); gmeint isch wohl de Ärger vom Jona ([[JON.4.1]]), vilicht au d Hitz."),
 ("JON.4.8", "heisse", "interpretive", "חֲרִישִׁית", None, ["schwüele"], "S Wort isch suscht nöd belegt; d Bedüütig «heiss, sängig» isch erschlosse."),
 ("JON.4.10", "häsch Mitleid", "interpretive", "חַסְתָּ", None, ["es tuet dir leid um", "du schonsch"],
  "חוּס heisst «Mitleid ha, verschone»; s gliich Verb staat i de Gägefraag vo Gott [[JON.4.11]]."),
 ("JON.4.10", "i ere Nacht", "adapted", "בִּן לַיְלָה", "Sohn vo nere Nacht", None, "S Hebräisch drückt Herkunft und Alter mit «Sohn» us."),
 ("JON.4.10", "zgrund gange isch", "literal", "אָבָד", None, None, "S gliich Verb wie «zgrund gaa» i [[JON.1.6]], [[JON.1.14]] und [[JON.3.9]]."),
 ("JON.4.11", "Mitleid ha", "interpretive", "אָחוּס", None, None,
  "De Satz hät keis Fragewort; dass er e Fraag isch, ergit sich us em Zämehang. S Buech hört mit dere Fraag uf; e Antwort vom Jona wird nöd "
  "verzellt."),
 ("JON.4.11", "hundertzwänzgtuusig", "adapted", "שְׁתֵּים עֶשְׂרֵה רִבּוֹ", "zwölf Zäätuusigi", None, "רִבּוֹ isch e Zäätuusig."),
 ("JON.4.11", "chönd underscheide", "interpretive", "לֹא יָדַע בֵּין", "nöd wüsse zwüsche", None,
  "D Wändig cha chliini Chind meine, wo rächts und links no nöd underscheided; oder alli Iiwoner, wo Gottes Wiisig nöd känned und drum "
  "Rächt und Unrächt nöd chönd underscheide. Beides wird vertrette."),
 ("JON.4.11", "Vee", "literal", "בְהֵמָה", None, None,
  "S Buech hört mit «vill Vee» uf: S Mitleid vo Gott schliesst au d Tier ii (vgl. [[JON.3.7]], [[PSA.36.6]])."),
]

UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung)
 ("TU-JON-001-001-017", "JON.1.1-JON.1.17", "narrative", "Die Flucht vor JHWH",
  ["TU-JON-001-001-003", "TU-JON-001-004-016", "TU-JON-001-017-017"],
  "Jona soll gegen Ninive predigen, flieht aber Richtung Tarschisch. JHWH schickt einen Sturm; die heidnischen Seeleute beten, losen, "
  "werfen Jona auf sein eigenes Wort hin ins Meer und fürchten am Ende JHWH. Ein grosser Fisch verschlingt Jona."),
 ("TU-JON-001-001-003", "JON.1.1-JON.1.3", "narrative", "Auftrag und Flucht", None,
  "JHWH schickt Jona nach Ninive, der grossen Stadt. Jona steigt hinab nach Jafo und nimmt ein Schiff in die Gegenrichtung, weg vom Angesicht JHWHs."),
 ("TU-JON-001-004-016", "JON.1.4-JON.1.16", "narrative", "Sturm auf dem Meer", None,
  "Im Sturm schreien die Seeleute zu ihren Göttern, während Jona schläft. Das Los fällt auf ihn; er bekennt sich zu JHWH und lässt sich ins "
  "Meer werfen. Das Meer wird still, und die Seeleute opfern JHWH."),
 ("TU-JON-001-017-017", "JON.1.17", "narrative", "Der grosse Fisch", None,
  "JHWH bestimmt einen grossen Fisch, der Jona verschlingt; drei Tage und drei Nächte ist Jona in seinem Bauch. In der hebräischen Zählung "
  "ist das Vers 2,1."),
 ("TU-JON-002-001-010", "JON.2.1-JON.2.10", "narrative", "Gebet aus der Tiefe",
  ["TU-JON-002-001-009", "TU-JON-002-010-010"],
  "Aus dem Bauch des Fisches betet Jona ein Danklied: Er war in der Tiefe dem Tod nahe und hat erfahren, dass JHWH ihn heraufholt. Auf JHWHs "
  "Wort speit der Fisch Jona an Land."),
 ("TU-JON-002-001-009", "JON.2.1-JON.2.9", "prayer", "Jonas Danklied", None,
  "Jona beschreibt in der Sprache der Psalmen, wie er in die Tiefe des Meeres sank und JHWH sein Rufen hörte; er gelobt Opfer und bekennt: "
  "Die Rettung gehört JHWH."),
 ("TU-JON-002-010-010", "JON.2.10", "narrative", "Ans Land gespien", None,
  "JHWH spricht zum Fisch, und dieser speit Jona aufs trockene Land."),
 ("TU-JON-003-001-010", "JON.3.1-JON.3.10", "narrative", "Ninive kehrt um",
  ["TU-JON-003-001-004", "TU-JON-003-005-010"],
  "Beim zweiten Auftrag gehorcht Jona und kündigt Ninive den Untergang in vierzig Tagen an. Vom König bis zum Vieh tut die Stadt Busse; Gott "
  "sieht ihre Umkehr, und es reut ihn das angekündigte Unheil."),
 ("TU-JON-003-001-004", "JON.3.1-JON.3.4", "narrative", "Die Botschaft an Ninive", None,
  "Das Wort JHWHs ergeht ein zweites Mal an Jona. Er geht in die grosse Stadt und ruft: «Noch vierzig Tage, und Ninive wird umgestürzt.»"),
 ("TU-JON-003-005-010", "JON.3.5-JON.3.10", "narrative", "Die Umkehr der Stadt", None,
  "Die Niniviten glauben Gott und fasten. Der König befiehlt Busse für Menschen und Tiere, in der Hoffnung, dass Gott umkehrt. Gott sieht ihre "
  "Taten und führt das Unheil nicht aus."),
 ("TU-JON-004-001-011", "JON.4.1-JON.4.11", "narrative", "Jonas Zorn und Gottes Mitleid",
  ["TU-JON-004-001-004", "TU-JON-004-005-011"],
  "Jona ist zornig, weil Gott gnädig ist, und wünscht sich den Tod. Mit einem Rizinus, einem Wurm und einem heissen Ostwind stellt Gott ihm "
  "eine Frage: Soll er kein Mitleid haben mit Ninive, der grossen Stadt? Das Buch endet offen."),
 ("TU-JON-004-001-004", "JON.4.1-JON.4.4", "dialogue", "Ich wusste, dass du gnädig bist", None,
  "Jona klagt, er habe gewusst, dass Gott gnädig und barmherzig ist; deshalb sei er geflohen. Er bittet um den Tod. JHWH fragt, ob sein Zorn recht ist."),
 ("TU-JON-004-005-011", "JON.4.5-JON.4.11", "narrative", "Der Rizinus und die grosse Stadt", None,
  "Jona wartet östlich der Stadt. Gott lässt einen Rizinus wachsen und wieder verdorren; Jona will sterben. Gott hält ihm vor: Er hat Mitleid "
  "mit einer Pflanze – soll Gott nicht Mitleid haben mit Ninive, seinen Menschen und seinem Vieh?"),
]
UNITS_GSW = {
 "TU-JON-001-001-017": ("D Flucht vor JHWH", "De Jona söll gäge Ninive predige, flüchtet aber Richtig Tarschisch. JHWH schickt en Sturm; di heidnische Seelüüt bätted, löösled, rüered de Jona uf sis eiget Wort hii is Meer und fürched am Schluss JHWH. En grosse Fisch verschluckt de Jona."),
 "TU-JON-001-001-003": ("Uftrag und Flucht", "JHWH schickt de Jona uf Ninive, di gross Stadt. De Jona gaat abe uf Jafo und nimmt es Schiff i di anderi Richtig, wäg vom Aagsicht vo JHWH."),
 "TU-JON-001-004-016": ("Sturm uf em Meer", "Im Sturm schreied d Seelüüt zu irne Götter, und de Jona schlaaft. S Los fallt uf in; er bekännt sich zu JHWH und laat sich is Meer rüere. S Meer wird still, und d Seelüüt opfered JHWH."),
 "TU-JON-001-017-017": ("De grosse Fisch", "JHWH bstellt en grosse Fisch, wo de Jona verschluckt; drei Täg und drei Nächt isch de Jona i sim Buuch. I de hebräische Zellig isch das de Vers 2,1."),
 "TU-JON-002-001-010": ("Gebätt us de Tüüfi", "Us em Buuch vom Fisch bättet de Jona es Dankliid: Er isch i de Tüüfi em Tod nooch gsii und hät erfaare, dass JHWH in ufehollt. Uf s Wort vo JHWH chotzt de Fisch de Jona as Land."),
 "TU-JON-002-001-009": ("S Dankliid vom Jona", "De Jona beschriibt i de Spraach vo de Psalme, wie n er i d Tüüfi vom Meer abegsunke isch und JHWH sis Rüefe ghört hät; er verspricht Opfer und bekännt: D Rettig ghört JHWH."),
 "TU-JON-002-010-010": ("As Land gspeut", "JHWH redt zum Fisch, und dä chotzt de Jona uf s troche Land."),
 "TU-JON-003-001-010": ("Ninive cheert um", "Bim zweite Uftrag folget de Jona und chündet Ninive de Undergang i vierzg Täg aa. Vom König bis zum Vee tuet d Stadt Buess; Gott gseet, dass si umchered, und s aagchündt Unheil reut en."),
 "TU-JON-003-001-004": ("D Botschaft a Ninive", "S Wort vo JHWH chunnt es zweits Mal zum Jona. Er gaat i di gross Stadt und rüeft: «No vierzg Täg, und Ninive wird umgstürzt.»"),
 "TU-JON-003-005-010": ("D Umchehr vo de Stadt", "D Niniviter glaubed Gott und faschted. De König befiehlt Buess für Mänsche und Tier, i de Hoffnig, dass Gott umcheert. Gott gseet ires Tue und macht s Unheil nöd."),
 "TU-JON-004-001-011": ("De Zorn vom Jona und s Mitleid vo Gott", "De Jona isch toub, wil Gott gnädig isch, und wünscht sich de Tod. Mit eme Rizinus, eme Wurm und eme heisse Oschtwind stellt Gott im e Fraag: Söll er kei Mitleid ha mit Ninive, de grosse Stadt? S Buech hört offe uf."),
 "TU-JON-004-001-004": ("Ich han gwüsst, dass du gnädig bisch", "De Jona chlagt, er heig gwüsst, dass Gott gnädig und barmhärzig isch; drum sig er gflüchtet. Er bittet um de Tod. JHWH fragt, öb sin Zorn rächt isch."),
 "TU-JON-004-005-011": ("De Rizinus und di gross Stadt", "De Jona wartet östlich vo de Stadt. Gott laat en Rizinus wachse und wider verdorre; de Jona wott sterbe. Gott hebt im vor: Er hät Mitleid mit ere Pflanze – söll Gott kei Mitleid ha mit Ninive, sine Mänsche und sim Vee?"),
}

CHAPTERS = ((1, 17), (2, 10), (3, 10), (4, 11))


def notes_for(c, lang):
    if lang == "de":
        notes = [AUTH + " Die Übersetzung ist nicht von Fachleuten geprüft.",
                 "Verszählung: Die Daten folgen der Navigationszählung (KJV). In der hebräischen Zählung (WLC) beginnt Kapitel 2 schon mit "
                 "[[JON.1.17]]: hebräisch 2,1–11 entspricht hier 1,17–2,10. Die Tokens tragen dort die hebräische Stelle in «source_reference». "
                 "Deutsche Bibeln wie Luther 1912 und Elberfelder 1905 zählen wie das Hebräische.",
                 "Aus der Wüste Juda sind Teile von Jona in Zwölfprophetenrollen erhalten (MurXII aus dem Wadi Murabbaat sowie 4QXIIa, 4QXIIf und "
                 "4QXIIg aus Qumran). Ihre Transkription liegt nur unter einer nicht kommerziellen Lizenz vor und gehört deshalb nicht zum freien "
                 "Datenkern. Nach einer maschinellen Kollation mit dem WLC (Sekundärtranskription, nicht am Faksimile geprüft; viele Wörter sind von "
                 "den Herausgebern ergänzt) stimmen die erhaltenen Wörter fast durchweg überein oder weichen nur in der Schreibweise ab; über alle vier "
                 "Handschriften zusammen sind zehn Wörter mit anderen Konsonanten markiert. Die Übersetzung folgt dem WLC.",
                 "Die Septuaginta und andere alte Übersetzungen sind nicht in den Daten. Wo Entscheidungen sie erwähnen, beruht das auf allgemeinem "
                 "Wissen und ist nicht an Daten geprüft. Für Jona markiert MACULA keine Ketiv/Qere-Formen."]
    else:
        notes = [AUTH_GSW + " D Übersetzig isch nöd vo Fachlüüt prüeft.",
                 "Verszellig: D Date folged de Navigationszellig (KJV). I de hebräische Zellig (WLC) faat s Kapitel 2 scho mit [[JON.1.17]] aa: "
                 "hebräisch 2,1–11 isch da 1,17–2,10. D Tokens träged dört di hebräisch Stell i «source_reference». Düütschi Bible wie Luther 1912 "
                 "und Elberfelder 1905 zelled wie s Hebräisch.",
                 "Us de Wüescht Juda sind Teil vom Jona i Zwölfprophete-Rolle erhalte (MurXII us em Wadi Murabbaat und 4QXIIa, 4QXIIf und 4QXIIg "
                 "us Qumran). Iri Transkription git s nu under ere nöd kommerzielle Lizänz; drum ghöred si nöd zum freie Datechärn. Nach eme "
                 "maschinelle Vergliich mit em WLC (Sekundärtranskription, nöd am Faksimile prüeft; vili Wörter sind vo de Herusgäber ergänzt) "
                 "stimmed di erhaltene Wörter fascht alli überii oder sind nu anders gschribe; über alli vier Handschrifte zäme sind zää Wörter "
                 "mit andere Konsonante markiert. D Übersetzig folgt em WLC.",
                 "D Septuaginta und anderi alti Übersetzige sind nöd i de Date. Wo Entscheidige si erwääned, beruet das uf allgemeinem Wüsse und "
                 "isch nöd a Date prüeft. Für de Jona markiert MACULA kei Ketiv/Qere-Forme."]
    return notes


def run():
    n = write(D / "works" / "WORK-JON.json", {"id": "WORK-JON", "type": "work", "status": "draft", "tags": TAGS,
                                             "name": "Jona", "original_language": "he"})
    for uid, rng, kind, title, parts, summary in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-JON", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}),
               **({"segmentation_note_de": "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung. "
                                           "Die Einheiten folgen der KJV-Zählung; [[JON.1.17]] (hebräisch 2,1) bildet darum einen eigenen Teil "
                                           "von Kapitel 1, obwohl er inhaltlich zum Gebet in Kapitel 2 überleitet."} if parts and uid.startswith("TU-JON-001") else
                  {"segmentation_note_de": "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."} if parts else {}),
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-14; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"WLC-JON-{c:03d}.json")
        refs_c = [f"JON.{c}.{v}" for v in range(1, last + 1)]
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-JON-{c:03d}-001-{last:03d}-{code}-WORKING"
            dec = [{"reference": r, "target": tg, "kind": kd, "heb": heb, **({"more_literal": ml} if ml else {}),
                    **({"other_options": oo} if oo else {}), "note": nt}
                   for r, tg, kd, heb, ml, oo, nt in decs if r in refs_c]
            for d in dec:
                if d["target"] not in texts[d["reference"]]:
                    raise SystemExit(f"{tid}: Entscheidung {d['target']!r} nicht im Text {d['reference']}")
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"JON.{c}.1-JON.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
                            "register_de": "Nah am hebräischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Personennamen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-JON-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem hebräischen Text (Westminster Leningrad Codex, Morpheme nach MACULA Hebrew): Satzbau und Bilder des Hebräischen möglichst sichtbar, verständliches Deutsch. Leitwörter (gross, hinabsteigen, Bosheit/Unheil, fürchten, bestimmen, zugrunde gehen, Mitleid haben) werden möglichst gleich wiedergegeben. Der Gottesname steht als JHWH. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
                                       if lang == "de" else "Direkt aus dem hebräischen Text (WLC) übersetzt, mit Wortzuordnung zu den Morphemen; die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle. Der Gottesname steht als JHWH. Nicht aus einer veröffentlichten Mundart-Bibel übernommen."),
                        "based_on_edition": "ED-WLC", "based_on_tokens": ts_id, "text_by_reference": texts,
                        "translation_notes": notes_for(c, lang),
                        "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                        "decisions": dec,
                        "decisions_note_de": "Übersetzungsentscheidungen: wörtlich (literal), sprachlich angepasst (adapted), Deutungsentscheidung (interpretive) oder der vertrauten Wiedergabe folgend (traditional). " + (AUTH if lang == "de" else AUTH_GSW)})
            n += write(D / "translations" / f"{tid}.json", rec)
            aid = f"ALIGN-JON-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"JON.{c}.1-JON.{c}.{last}",
                "source_language": "he", "target_language": rec["language"], "source_basis": "ED-WLC", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} Morphem-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/jona_text.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Jona – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
