#!/usr/bin/env python3
"""Autorenwerkzeug: Rut – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem hebräischen Text
(Westminster Leningrad Codex), Übersetzungsentscheidungen und vollständige Wortzuordnung je Morphem.

Aufruf: python3 scripts/authoring/ruth_text.py

Auszeichnung wie in scripts/authoring/_lib.py; die Zahlen sind die Morphem-Positionen im Vers
(data/tokens/WLC-RUT-00c.json). Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft.
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, localize, write  # noqa: E402

DATE = "2026-10-13"
AUTH = "KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; aus dem hebräischen Text (WLC) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-RUTH"]
OBJ = "Objektzeichen אֶת, im Deutschen nicht wiedergegeben"
OBJ_G = "Objektzeiche אֶת, nöd übersetzbar"
Q = "Fragepartikel הֲ; im Deutschen durch die Satzstellung ausgedrückt"
Q_G = "Fragewort הֲ; dur d Satzstellig usdruckt"
VAV = "Verbindungspartikel וְ/וַ; im Deutschen nicht eigens wiedergegeben"
VAV_G = "Verbindigswort וְ/וַ; nöd eigens widergää"
WAYHI = "וַיְהִי «und es geschah» leitet den Erzählschritt ein; nicht eigens wiedergegeben"
WAYHI_G = "וַיְהִי «und es isch gscheh» leitet de Erzählschritt ii; nöd eigens widergää"

DE = {
 # ------------------------------------------------------------ Kapitel 1
 "RUT.1.1": "[Es geschah]{1,2} [in]{3} [den Tagen]{4}, als [die Richter]{6,7} [richteten]{5}: Da{8} [herrschte]{9} [eine Hungersnot]{10} [im]{11} [Land]{12}. Und{13} [ein Mann]{24} [aus]{15} [Betlehem]{16,17} in [Juda]{18} [zog fort]{14}, [um]{19} [im]{21} [Gebiet]{22} [von Moab]{23} [als Fremder zu wohnen]{20}, [er]{25} und{26} [seine Frau]{27,28} und{29} [seine beiden Söhne]{30,31,32}.",
 "RUT.1.2": "Und{1} [der Mann]{3,4} [hiess]{2} [Elimelech]{5}, und{6} [seine Frau]{8,9} [hiess]{7} [Noomi]{10}, und{11} [seine beiden Söhne]{13,14,15} [hiessen]{12} [Machlon]{16} und{17} [Kiljon]{18} – [Efratiter]{19} [aus]{20} [Betlehem]{21,22} in [Juda]{23}. Und{24} [sie kamen]{25} [ins Gebiet]{26} [von Moab]{27} und{28} [blieben]{29} [dort]{30}.",
 "RUT.1.3": "Da{1} [starb]{2} [Elimelech]{3}, [der Mann]{4} [Noomis]{5}, und{6} [sie]{8} [blieb zurück]{7} [mit]{9} [ihren beiden Söhnen]{10,11,12}.",
 "RUT.1.4": "Und{1} [sie nahmen]{2} [sich]{3,4} [moabitische]{6} [Frauen]{5}; [die eine]{8,9} [hiess]{7} [Orpa]{10}, und{11} [die andere]{13,14} [hiess]{12} [Rut]{15}. Und{16} [sie wohnten]{17} [dort]{18} [etwa]{19} [zehn]{20} [Jahre]{21}.",
 "RUT.1.5": "Da{1} [starben]{2} [auch]{3} [die beiden]{4,5}, [Machlon]{6} und{7} [Kiljon]{8}, und{9} [die Frau]{11,12} [blieb zurück]{10}, [ohne]{13} [ihre beiden Kinder]{14,15,16} und{17} [ohne]{18} [ihren Mann]{19,20}.",
 "RUT.1.6": "Da{1} [machte]{2} [sie]{3} [sich]{2} [mit]{4} [ihren Schwiegertöchtern]{5,6} [auf]{2} und{7} [kehrte]{8} [aus]{9} [dem Gebiet]{10} [von Moab]{11} [zurück]{8}; denn{12} [sie hatte]{13} [im]{14} [Gebiet]{15} [von Moab]{16} [gehört]{13}, [dass]{17} [JHWH]{19} [sich]{18} [seines Volkes]{21,22} [angenommen hatte]{18}, [indem er]{23} [ihnen]{25,26} [Brot]{27} [gab]{24}. ~20(" + OBJ + ")",
 "RUT.1.7": "Und{1} [sie zog]{2} [von]{3} [dem Ort]{4,5} [weg]{2}, [wo]{6,8,9} [sie gewesen war]{7}, und{10} [ihre beiden Schwiegertöchter]{11,12,13} [mit ihr]{14,15}; und{16} [sie machten sich]{17} [auf den Weg]{18,19}, [um]{20} [ins]{22} [Land]{23} [Juda]{24} [zurückzukehren]{21}.",
 "RUT.1.8": "Da{1} [sagte]{2} [Noomi]{3} [zu]{4} [ihren beiden Schwiegertöchtern]{5,6,7}: «[Geht]{8}, [kehrt um]{9}, [jede]{10} [in]{11} [das Haus]{12} [ihrer Mutter]{13,14}! [JHWH]{16} [erweise]{15} [euch]{17,18} [Treue]{19}, [so wie]{20,21} [ihr]{22} sie [an den Toten]{23,24,25} und{26} [an mir]{27,28} [erwiesen habt]{22}.",
 "RUT.1.9": "[JHWH]{2} [gebe]{1} [euch]{3,4}, [dass ihr]{5} [Ruhe]{7} [findet]{6}, [jede]{8} [im Haus]{9} [ihres Mannes]{10,11}!» Und{12} [sie küsste]{13} [sie]{14,15}, und{16} [sie erhoben]{17} [ihre Stimme]{18,19} und{20} [weinten]{21}.",
 "RUT.1.10": "Und{1} [sie sagten]{2} [zu ihr]{3,4}: «[Nein]{5}, [mit dir]{6,7} [wollen wir]{8} [zu]{9} [deinem Volk]{10,11} [zurückkehren]{8}!»",
 "RUT.1.11": "Aber{1} [Noomi]{3} [sagte]{2}: «[Kehrt um]{4}, [meine Töchter]{5,6}! [Warum]{7,8} [wollt ihr]{9} [mit mir]{10,11} [gehen]{9}? [Habe ich]{14,15} [denn noch]{13} [Söhne]{16} [in]{17} [meinem Leib]{18,19}, [die]{20} [eure]{22,23} [Männer]{24,25} [werden könnten]{21}? ~12(" + Q + ")",
 "RUT.1.12": "[Kehrt um]{1}, [meine Töchter]{2,3}, [geht]{4}! Denn{5} [ich bin zu alt]{6}, [um]{7} [einen Mann]{9,10} [zu haben]{8}. [Wenn]{11} [ich auch sagte]{12}: ‹[Es gibt]{13} [für mich]{14,15} [Hoffnung]{16}›, [ja, wenn]{17} [ich]{18} [heute Nacht]{19,20} [einen Mann]{21,22} [hätte]{18} und{23} [sogar]{24} [Söhne]{26} [gebären würde]{25} –",
 "RUT.1.13": "[würdet ihr]{3} [darum]{2} [warten]{3}, [bis]{4,5} [sie gross wären]{6}? [Würdet ihr euch]{9} [darum]{8} [verschliessen]{9}, [ohne]{10,11} [einen Mann]{13,14} [zu haben]{12}? [Nein]{15}, [meine Töchter]{16,17}! Denn{18} [es ist]{19} [mir]{20,21} [viel]{22} [bitterer]{19} [als]{23} [euch]{24}, denn{25} [die Hand]{29} [JHWHs]{30} [hat sich]{26} [gegen mich]{27,28} [gewendet]{26}.» ~1(" + Q + ") ~7(" + Q + ")",
 "RUT.1.14": "Da{1} [erhoben sie]{2} [ihre Stimme]{3,4} und{5} [weinten]{6} [noch einmal]{7}. Und{8} [Orpa]{10} [küsste]{9} [ihre Schwiegermutter]{11,12,13}, [aber]{14} [Rut]{15} [hielt sich]{16} [an]{17} [ihr]{18} [fest]{16}.",
 "RUT.1.15": "Da{1} [sagte sie]{2}: «[Sieh]{3}, [deine Schwägerin]{5,6} [ist]{4} [zu]{7} [ihrem Volk]{8,9} und{10} [zu]{11} [ihren Göttern]{12,13} [zurückgekehrt]{4}. [Kehr um]{14}, [deiner Schwägerin]{16,17} [nach]{15}!»",
 "RUT.1.16": "Aber{1} [Rut]{3} [sagte]{2}: «[Dräng]{5} [mich]{6,7} [nicht]{4}, [dich zu verlassen]{8,9,10} und [von dir weg]{13,14,15} [umzukehren]{11,12}! Denn{16} [wohin]{17,18} [du gehst]{19}, [dahin gehe ich]{20}, und{21} [wo]{22,23} [du übernachtest]{24}, [da übernachte ich]{25}. [Dein Volk]{26,27} ist [mein Volk]{28,29}, und{30} [dein Gott]{31,32} ist [mein Gott]{33,34}.",
 "RUT.1.17": "[Wo]{1,2} [du stirbst]{3}, [da sterbe ich]{4}, und{5} [dort]{6} [will ich begraben werden]{7}. [So]{8} [soll]{9} [JHWH]{10} [mir]{11,12} [tun]{9}, und{13} [so]{14} [soll er fortfahren]{15}: [nur]{16} [der Tod]{17,18} [wird]{19} [mich]{20,21} und{22} [dich]{23,24} [trennen]{19}!»",
 "RUT.1.18": "Als{1} [sie sah]{2}, [dass]{3} [sie]{5} [fest entschlossen war]{4}, [mit ihr]{8,9} [zu gehen]{6,7}, da{10} [hörte sie auf]{11}, [auf sie einzureden]{12,13,14,15}.",
 "RUT.1.19": "So{1} [gingen]{2} [die beiden]{3,4}, [bis]{5} [sie]{7} [nach Betlehem]{8,9} [kamen]{6}. [Als]{12} [sie]{14} [nach Betlehem]{15,16} [kamen]{13}, da{17} [geriet]{18} [die ganze Stadt]{19,20,21} [ihretwegen]{22,23} [in Aufruhr]{18}, und{24} [die Frauen sagten]{25}: «[Ist das]{26,27} [Noomi]{28}?» ~10(" + WAYHI + ") ~11(" + WAYHI + ")",
 "RUT.1.20": "Aber{1} [sie sagte]{2} [zu ihnen]{3,4}: «[Nennt]{6} [mich]{7,8} [nicht]{5} [Noomi]{9}, [nennt]{10} [mich]{11,12} [Mara]{13}! Denn{14} [der Allmächtige]{16} [hat es]{15} [mir]{17,18} [sehr]{19} [bitter gemacht]{15}.",
 "RUT.1.21": "[Voll]{2} [bin]{3} [ich]{1} [weggegangen]{3}, und{4} [leer]{5} [hat]{6} [mich]{7} [JHWH]{8} [zurückgebracht]{6}. [Warum]{9,10} [nennt]{11} [ihr mich]{12,13} [Noomi]{14}, [wo doch]{15} [JHWH]{16} [gegen]{18} [mich]{19} [ausgesagt hat]{17} und{20} [der Allmächtige]{21} [mir]{23,24} [Böses angetan hat]{22}?»",
 "RUT.1.22": "So{1} [kehrte]{2} [Noomi]{3} [zurück]{2}, und{4} [mit ihr]{10,11} [Rut]{5}, [die Moabiterin]{6,7}, [ihre Schwiegertochter]{8,9}, [die]{12} [aus]{14} [dem Gebiet]{15} [von Moab]{16} [zurückkam]{13}. Und{17} [sie]{18} [kamen]{19} [nach Betlehem]{20,21} [zu]{22} [Beginn]{23} [der Gerstenernte]{24,25}.",
 # ------------------------------------------------------------ Kapitel 2
 "RUT.2.1": "Nun{1} [hatte]{2} [Noomi]{3} [einen Verwandten]{4} [von Seiten]{5} [ihres Mannes]{6,7}, [einen Mann]{8} [von Vermögen]{9,10} [aus]{11} [der Sippe]{12} [Elimelechs]{13}; und{14} [er hiess]{15,16} [Boas]{17}.",
 "RUT.2.2": "Und{1} [Rut]{3}, [die Moabiterin]{4,5}, [sagte]{2} [zu]{6} [Noomi]{7}: «[Lass mich doch]{9} [aufs Feld]{10,11} [gehen]{8} und{12} [Ähren]{14,15} [auflesen]{13} [hinter]{16} [dem]{17}, [in]{20} [dessen Augen]{21,22} [ich]{18} [Gunst]{19} [finde]{18}!» Und{23} [sie sagte]{24} [zu ihr]{25,26}: «[Geh]{27}, [meine Tochter]{28,29}!»",
 "RUT.2.3": "So{1} [ging sie]{2} und{3} [kam]{4} und{5} [las]{6} [auf dem Feld]{7,8} [hinter]{9} [den Schnittern]{10,11} [Ähren auf]{6}. Und{12} [es traf sich]{13} [zufällig]{14}, [dass sie]{15} [auf das Feldstück]{16,17,18} [des Boas]{19,20} kam, [der]{21} [aus]{22} [der Sippe]{23} [Elimelechs]{24} war.",
 "RUT.2.4": "Und{1} [gerade da]{2} [kam]{4} [Boas]{3} [aus]{5} [Betlehem]{6,7} und{8} [sagte]{9} [zu den Schnittern]{10,11}: «[JHWH]{12} sei [mit euch]{13,14}!» Und{15} [sie sagten]{16} [zu ihm]{17,18}: «[JHWH]{21} [segne]{19} [dich]{20}!»",
 "RUT.2.5": "Und{1} [Boas]{3} [sagte]{2} [zu]{4} [seinem Knecht]{5,6}, [der]{7} [über]{9} [die Schnitter]{10,11} [gesetzt war]{8}: «[Zu wem gehört]{12,13} [diese]{16,17} [junge Frau]{14,15}?»",
 "RUT.2.6": "Und{1} [der Knecht]{3,4}, [der]{5} [über]{7} [die Schnitter]{8,9} [gesetzt war]{6}, [antwortete]{2} und{10} [sagte]{11}: «[Sie ist]{12} [eine moabitische]{14} [junge Frau]{13}, [die]{15} [mit]{17} [Noomi]{18} [aus]{19} [dem Gebiet]{20} [von Moab]{21} [zurückgekommen ist]{16}.",
 "RUT.2.7": "Und{1} [sie hat gesagt]{2}: ‹[Lass mich doch]{4} [Ähren auflesen]{3} und{5} [zwischen]{7} [den Garben]{8} [sammeln]{6}, [hinter]{9} [den Schnittern]{10,11} [her]{9}.› So{12} [ist sie gekommen]{13} und{14} [ist geblieben]{15} [seit]{16,17} [dem Morgen]{18,19} und{20} [bis]{21} [jetzt]{22}; [hier]{23} [hat sie]{24,25} [kaum]{28} [im Haus]{26,27} [gesessen]{24,25}.»",
 "RUT.2.8": "Da{1} [sagte]{2} [Boas]{3} [zu]{4} [Rut]{5}: «[Hör]{8} [doch]{6,7}, [meine Tochter]{9,10}: [Geh]{12} [nicht]{11} [auf]{15} [ein anderes]{17} [Feld]{16}, [um aufzulesen]{13,14}, und{18} [geh]{21} [auch]{19} [nicht]{20} [von hier]{22,23} [weg]{21}, und{24} [halte dich]{26,27} [hier]{25} [zu]{28} [meinen Arbeiterinnen]{29,30}.",
 "RUT.2.9": "[Deine Augen]{1,2} seien [auf das Feld]{3,4} gerichtet, [das]{5} [sie schneiden]{6,7}, und{8} [geh]{9} [hinter]{10} [ihnen]{11} [her]{10}. [Habe ich]{14} [den Knechten]{16,17} [nicht]{12,13} [geboten]{14}, [dich]{21} [nicht]{18,19} [anzurühren]{20}? Und{22} [wenn du Durst hast]{23}, [dann]{24} [geh]{25} [zu]{26} [den Gefässen]{27,28} und{29} [trink]{30} [von dem]{31}, [was]{32} [die Knechte]{35,36} [schöpfen]{33,34}. ~15(" + OBJ + ")",
 "RUT.2.10": "Da{1} [fiel sie]{2} [auf]{3} [ihr Gesicht]{4,5} und{6} [verneigte sich]{7} [zur Erde]{8,9} und{10} [sagte]{11} [zu ihm]{12,13}: «[Warum]{14} [habe ich]{15} [Gunst]{16} [in]{17} [deinen Augen]{18,19} [gefunden]{15}, [dass du]{20} [mich]{22} [beachtest]{21}, [wo ich doch]{23,24} [eine Fremde]{25} bin?»",
 "RUT.2.11": "Und{1} [Boas]{3} [antwortete]{2} und{4} [sagte]{5} [zu ihr]{6,7}: «[Man hat]{9} [mir]{10,11} [genau]{8} [berichtet]{9}, [alles]{12}, [was]{13} [du]{14} [an]{15} [deiner Schwiegermutter]{16,17} [getan hast]{14} [nach]{18} [dem Tod]{19} [deines Mannes]{20,21}, und{22} [wie du]{23} [deinen Vater]{24,25} und{26} [deine Mutter]{27,28} und{29} [das Land]{30} [deiner Herkunft]{31,32} [verlassen hast]{23} und{33} [zu]{35} [einem Volk]{36} [gegangen bist]{34}, [das]{37} [du]{39} [vorher]{40,41:idiom} [nicht]{38} [kanntest]{39}.",
 "RUT.2.12": "[JHWH]{2} [vergelte]{1} [dein Tun]{3,4}, und{5} [dein Lohn]{7,8} [möge]{6} [voll]{9} [sein]{6} [von]{10,11} [JHWH]{12}, [dem Gott]{13} [Israels]{14}, [zu dem]{15} [du gekommen bist]{16}, [um]{17} [unter]{19} [seinen Flügeln]{20,21} [Zuflucht zu suchen]{18}!»",
 "RUT.2.13": "Und{1} [sie sagte]{2}: «[Möge ich]{3} [Gunst]{4} [finden]{3} [in]{5} [deinen Augen]{6,7}, [mein Herr]{8,9}! Denn{10} [du hast]{11} [mich]{12} [getröstet]{11} und{13,14} [hast]{15} [deiner Magd]{18,19} [zu Herzen]{16,17} [geredet]{15}, [obwohl]{20} [ich]{21} [nicht]{22} [bin]{23} [wie]{24} [eine]{25} [deiner Mägde]{26,27}.»",
 "RUT.2.14": "Und{1} [zur]{6} [Essenszeit]{7,8,9} [sagte]{2} [Boas]{5} [zu ihr]{3,4}: «[Komm]{10} [her]{11} und{12} [iss]{13} [vom]{14,15} [Brot]{16} und{17} [tunke]{18} [deinen Bissen]{19,20} [in]{21} [den Essig]{22}!» Und{23} [sie setzte sich]{24} [neben]{25,26} [die Schnitter]{27,28}, und{29} [er reichte]{30} [ihr]{31,32} [geröstetes Korn]{33}, und{34} [sie ass]{35} und{36} [wurde satt]{37} und{38} [liess noch übrig]{39}.",
 "RUT.2.15": "Als{1} [sie aufstand]{2}, [um aufzulesen]{3,4}, [gebot]{6} [Boas]{7} [seinen Knechten]{9,10} [und sagte]{11,12}: «[Auch]{13} [zwischen]{14} [den Garben]{15,16} [darf sie auflesen]{17}, und{18} [beschämt]{20} [sie]{21} [nicht]{19}! ~5(" + VAV + ") ~8(" + OBJ + ")",
 "RUT.2.16": "Und{1} [zieht]{4} [ihr]{5,6} [sogar]{2} [eigens]{3} [etwas aus]{7} [den Bündeln]{8,9} [heraus]{4} und{10} [lasst es liegen]{11}, [damit sie]{12} [es auflesen kann]{13}, und{14} [schimpft]{16} [nicht]{15} [mit ihr]{17,18}!»",
 "RUT.2.17": "So{1} [las sie]{2} [auf dem Feld]{3,4} [auf]{2} [bis]{5} [zum Abend]{6,7}. Und{8} [sie klopfte aus]{9}, [was]{11} [sie aufgelesen hatte]{12}, und{13} [es war]{14} [etwa]{15} [ein Efa]{16} [Gerste]{17}. ~10(" + OBJ + ")",
 "RUT.2.18": "Und{1} [sie hob es auf]{2} und{3} [kam]{4} [in die Stadt]{5,6}, und{7} [ihre Schwiegermutter]{9,10} [sah]{8}, [was]{12} [sie aufgelesen hatte]{13}. Und{14} [sie holte hervor]{15} und{16} [gab]{17} [ihr]{18,19}, [was]{21} [sie übrig gelassen hatte]{22}, [nachdem sie]{23} [satt geworden war]{24,25}. ~11(" + OBJ + ") ~20(" + OBJ + ")",
 "RUT.2.19": "Da{1} [sagte]{2} [ihre Schwiegermutter]{5,6} [zu ihr]{3,4}: «[Wo]{7} [hast du]{8} [heute]{9,10} [aufgelesen]{8}, und{11} [wo]{12} [hast du gearbeitet]{13}? [Gesegnet]{17} [sei]{14} [der, der dich beachtet hat]{15,16}!» Und{18} [sie erzählte]{19} [ihrer Schwiegermutter]{20,21,22}, [bei wem]{24,26,27} [sie gearbeitet hatte]{25}, und{28} [sagte]{29}: «[Der Mann]{31,32}, [bei dem]{33,35,36} [ich]{34} [heute]{37,38} [gearbeitet habe]{34}, [heisst]{30} [Boas]{39}.» ~23(" + OBJ + ")",
 "RUT.2.20": "Da{1} [sagte]{2} [Noomi]{3} [zu]{4} [ihrer Schwiegertochter]{5,6}: «[Gesegnet]{7} [sei er]{8} [von]{9} [JHWH]{10}, [der]{11} [seine Treue]{14,15} [den Lebenden]{16,17,18} und{19} [den Toten]{20,21,22} [nicht]{12} [entzogen hat]{13}!» Und{23} [Noomi]{27} [sagte]{24} [zu ihr]{25,26}: «[Der Mann]{31,32} [ist]{28} [mit uns]{29,30} [nah verwandt]{28}; [er]{36} [ist einer]{33} [von unseren Lösern]{34,35}.»",
 "RUT.2.21": "Und{1} [Rut]{3}, [die Moabiterin]{4,5}, [sagte]{2}: «[Er hat]{8} [sogar]{6,7} [zu mir]{9,10} [gesagt]{8}: ‹[Halte dich]{17,18} [zu]{11} [den Knechten]{12,13}, [die]{14} [zu mir gehören]{15,16}, [bis sie]{19,20} [die ganze]{23} [Ernte]{24,25}, [die]{26} [mir gehört]{27,28}, [eingebracht haben]{21}.›» ~22(" + OBJ + ")",
 "RUT.2.22": "Da{1} [sagte]{2} [Noomi]{3} [zu]{4} [Rut]{5}, [ihrer Schwiegertochter]{6,7}: «[Es ist gut]{8}, [meine Tochter]{9,10}, [wenn]{11} [du]{12} [mit]{13} [seinen Arbeiterinnen]{14,15} [hinausgehst]{12}, [damit]{16} [man]{18} [dich]{19,20} [auf]{21} [einem anderen]{23} [Feld]{22} [nicht]{17} [belästigt]{18}.»",
 "RUT.2.23": "So{1} [hielt sie sich]{2} [zu]{3} [den Arbeiterinnen]{4} [des Boas]{5}, [um aufzulesen]{6,7}, [bis]{8} [die Gerstenernte]{10,11,12} und{13} [die Weizenernte]{14,15,16} [zu Ende waren]{9}. Und{17} [sie wohnte]{18} [bei]{19} [ihrer Schwiegermutter]{20,21}.",
 # ------------------------------------------------------------ Kapitel 3
 "RUT.3.1": "Und{1} [Noomi]{5}, [ihre Schwiegermutter]{6,7}, [sagte]{2} [zu ihr]{3,4}: «[Meine Tochter]{8,9}, [soll ich]{12} [dir]{13,14} [nicht]{10,11} [einen Ort der Ruhe]{15} [suchen]{12}, [wo]{16} [es dir]{18,19} [gut geht]{17}?",
 "RUT.3.2": "[Nun]{1,2}: [Ist]{3} [Boas]{5} [nicht]{4} [unser Verwandter]{6,7}, [bei]{8,10} [dessen Arbeiterinnen]{11,12} [du warst]{9}? [Sieh]{13}, [er]{14} [worfelt]{15} [heute Nacht]{20,21} [die Gerste]{18,19} [auf der Tenne]{17}. ~16(" + OBJ + ")",
 "RUT.3.3": "[Wasch dich]{2} und{3} [salbe dich]{4} und{5} [zieh]{6} [deine Kleider]{7,8} [an]{9,10}, und{11} [geh hinab]{12} [zur Tenne]{13,14}. [Gib dich]{16} [dem Mann]{17,18} [nicht]{15} [zu erkennen]{16}, [bis er]{19,21} [fertig]{20} [gegessen]{22,23} und{24} [getrunken]{25,26} [hat]{20}. ~1(" + VAV + ")",
 "RUT.3.4": "Und{1} [wenn]{2,3} [er]{5} [sich hinlegt]{4}, [dann]{6} [merk dir]{7} [den Ort]{9,10}, [wo]{11,13} [er sich hinlegt]{12}, und{14} [geh hin]{15} und{16} [deck]{17} [seine Füsse]{18,19} [auf]{17} und{20} [leg dich hin]{21}. Und{22} [er]{23} [wird]{24} [dir]{25,26} [sagen]{24}, [was]{28} [du tun sollst]{29,30}.» ~8(" + OBJ + ") ~27(" + OBJ + ")",
 "RUT.3.5": "Und{1} [sie sagte]{2} [zu ihr]{3,4}: «[Alles]{5}, [was]{6} [du]{7} [mir]{8,9} [sagst]{7}, [werde ich tun]{10}.»",
 "RUT.3.6": "So{1} [ging sie hinab]{2} [zur Tenne]{3,4} und{5} [tat]{6} [ganz nach]{7} [allem]{8}, [was]{9} [ihre Schwiegermutter]{12,13} [ihr]{11} [aufgetragen hatte]{10}.",
 "RUT.3.7": "Und{1} [Boas]{3} [ass]{2} und{4} [trank]{5}, und{6} [ihm]{9} [war wohl]{7} [ums Herz]{8}. Und{10} [er ging]{11}, [um sich hinzulegen]{12,13} [am]{14} [Ende]{15} [des Getreidehaufens]{16,17}. [Da]{18} [kam sie]{19} [leise]{20,21} und{22} [deckte]{23} [seine Füsse]{24,25} [auf]{23} und{26} [legte sich hin]{27}.",
 "RUT.3.8": "[Um]{3} [Mitternacht]{4,5,6} [schrak]{8} [der Mann]{9,10} [auf]{8} und{11} [drehte sich um]{12}, und{13} [da]{14} [lag]{16} [eine Frau]{15} [zu seinen Füssen]{17,18}. ~1(" + WAYHI + ") ~2(" + WAYHI + ") ~7(" + VAV + ")",
 "RUT.3.9": "Und{1} [er sagte]{2}: «[Wer]{3} [bist du]{4}?» Und{5} [sie sagte]{6}: «[Ich bin]{7} [Rut]{8}, [deine Dienerin]{9,10}. [So]{11} [breite]{12} [den Zipfel deines Gewandes]{13,14} [über]{15} [deine Dienerin]{16,17} [aus]{12}, denn{18} [du bist]{20} [ein Löser]{19}.»",
 "RUT.3.10": "Und{1} [er sagte]{2}: «[Gesegnet]{3} [seist du]{4} [von]{5} [JHWH]{6}, [meine Tochter]{7,8}! [Du hast]{9} [deine Treue]{10,11} [jetzt]{12,13} [noch schöner erwiesen]{9} [als]{14} [am Anfang]{15,16}, [dass du]{17} [nicht]{18} [den jungen Männern]{21,22} [nachgegangen bist]{19,20}, [ob]{23} [arm]{24} [oder]{25,26} [reich]{27}.",
 "RUT.3.11": "[Und nun]{1,2}, [meine Tochter]{3,4}, [fürchte dich]{6} [nicht]{5}! [Alles]{7}, [was]{8} [du sagst]{9}, [werde ich]{10} [für dich]{11,12} [tun]{10}; denn{13} [jeder]{15} [im Tor]{16} [meines Volkes]{17,18} [weiss]{14}, [dass]{19} [du]{22} [eine tüchtige Frau]{20,21} bist.",
 "RUT.3.12": "[Nun]{1,2}, [es ist]{3} [wahr]{4}, [dass]{5} [ich]{7} [ein Löser]{6} [bin]{7}; [aber]{8} [es gibt]{10} [auch]{9} [einen Löser]{11}, [der näher verwandt ist]{12} [als ich]{13,14}.",
 "RUT.3.13": "[Bleib]{1} [heute Nacht]{2,3} hier; und{4} [dann]{5} [am Morgen]{6,7}: [wenn]{8} [er]{9} [dich]{10} [lösen will]{9}, [gut]{11}, [soll er lösen]{12}; und{13} [wenn]{14} [er]{16} [nicht]{15} [willens ist]{16}, [dich]{19} [zu lösen]{17,18}, [dann]{20} [werde ich]{21} [dich]{22} [lösen]{21}, [ich selbst]{23} – [so wahr]{24} [JHWH]{25} [lebt]{24}! [Leg dich hin]{26} [bis]{27} [zum Morgen]{28,29}.»",
 "RUT.3.14": "So{1} [lag sie]{2} [zu seinen Füssen]{3,4} [bis]{5} [zum Morgen]{6,7}. Und{8} [sie stand auf]{9}, [bevor]{10,11} [einer]{13} [den andern]{15,16} [erkennen konnte]{12}. Und{17} [er sagte]{18}: «[Es darf]{20} [nicht]{19} [bekannt werden]{20}, [dass]{21} [die Frau]{23,24} [zur Tenne]{25,26} [gekommen ist]{22}.» ~14(" + OBJ + ")",
 "RUT.3.15": "Und{1} [er sagte]{2}: «[Gib her]{3} [den Umhang]{4,5}, [den]{6} [du anhast]{7,8}, und{9} [halt]{10} [ihn]{11,12} [auf]{10}!» Und{13} [sie hielt]{14} [ihn]{15,16} [auf]{14}, und{17} [er mass]{18} [sechs Mass]{19} [Gerste]{20} [ab]{18} und{21} [legte sie]{22} [ihr]{23,24} [auf]{22}. Und{25} [er ging]{26} [in die Stadt]{27,28}.",
 "RUT.3.16": "Und{1} [sie kam]{2} [zu]{3} [ihrer Schwiegermutter]{4,5}, und{6} [die sagte]{7}: «[Wie steht es um dich]{8,9:idiom}, [meine Tochter]{10,11}?» Und{12} [sie erzählte]{13} [ihr]{14,15} [alles]{17}, [was]{18} [der Mann]{22,23} [für sie]{20,21} [getan hatte]{19}. ~16(" + OBJ + ")",
 "RUT.3.17": "Und{1} [sie sagte]{2}: «[Diese]{6,7} [sechs Mass]{3} [Gerste]{4,5} [hat er]{8} [mir]{9,10} [gegeben]{8}; denn{11} [er sagte]{12} [zu mir]{13,14}: ‹[Komm]{16} [nicht]{15} [mit leeren Händen]{17} [zu]{18} [deiner Schwiegermutter]{19,20}!›»",
 "RUT.3.18": "Da{1} [sagte sie]{2}: «[Bleib sitzen]{3}, [meine Tochter]{4,5}, [bis]{6,7} [du weisst]{8,9}, [wie]{10} [die Sache]{12} [ausgeht]{11}; denn{13} [der Mann]{16,17} [wird]{15} [nicht]{14} [ruhen]{15}, [bis er]{18,19} [die Sache]{21,22} [heute]{23,24} [zu Ende gebracht hat]{20}.»",
 # ------------------------------------------------------------ Kapitel 4
 "RUT.4.1": "Boas{2} aber{1} [ging hinauf]{3} [zum Tor]{4,5} und{6} [setzte sich]{7} [dort]{8} [hin]{7}. Und{9} [gerade da]{10} [kam]{16} [der Löser]{11,12} [vorbei]{16}, [von dem]{13} [Boas]{15} [gesprochen hatte]{14}. Und{17} [er sagte]{18}: «[Komm herüber]{19,20}, [setz dich]{21,22} [hierher]{23}, [du Soundso]{24,25:idiom}!» Und{26} [er kam herüber]{27} und{28} [setzte sich]{29}.",
 "RUT.4.2": "Und{1} [er nahm]{2} [zehn]{3} [Männer]{4} [von]{5} [den Ältesten]{6} [der Stadt]{7,8} und{9} [sagte]{10}: «[Setzt euch]{11} [hierher]{12}!» Und{13} [sie setzten sich]{14}.",
 "RUT.4.3": "Dann{1} [sagte er]{2} [zum Löser]{3,4}: «[Das Feldstück]{5,6,7}, [das]{8} [unserem Bruder]{10,11} [Elimelech]{12,13} [gehörte]{9}, [verkauft]{14} [Noomi]{15}, [die]{16} [aus]{18} [dem Gebiet]{19} [von Moab]{20} [zurückgekommen ist]{17}.",
 "RUT.4.4": "Und{1} [ich]{2} [dachte]{3}, [ich lege es dir offen]{4,5,6:idiom} [und sage]{7,8}: [Erwirb es]{9} [vor]{10} [denen, die hier sitzen]{11,12}, und{13} [vor]{14} [den Ältesten]{15} [meines Volkes]{16,17}! [Wenn]{18} [du lösen willst]{19}, [dann löse]{20}! Und{21} [wenn]{22} [er]{24} [nicht]{23} [lösen will]{24}, [dann sag es]{25,26} [mir]{27,28}, [damit ich]{29} [es weiss]{30}; denn{31} [es gibt]{32} [ausser]{33} [dir]{34} [keinen]{32}, [der lösen könnte]{35,36}, und{37} [ich]{38} [komme nach]{39} [dir]{40}.» Und{41} [er sagte]{42}: «[Ich]{43} [will lösen]{44}.»",
 "RUT.4.5": "Da{1} [sagte]{2} [Boas]{3}: «[An dem Tag]{4,5}, [an dem du]{7} [das Feld]{8,9} [aus der Hand]{10,11} [Noomis]{12} [erwirbst]{6}, [erwirbst du]{22} es [auch]{13} [von]{14,15} [Rut]{16}, [der Moabiterin]{17,18}, [der Frau]{19} [des Verstorbenen]{20,21}, [um]{23} [den Namen]{25} [des Verstorbenen]{26,27} [auf]{28} [seinem Erbteil]{29,30} [aufrechtzuerhalten]{24}.»",
 "RUT.4.6": "Da{1} [sagte]{2} [der Löser]{3,4}: «[Ich kann]{6} [für mich]{9,10} [nicht]{5} [lösen]{7,8}, [sonst]{11} [schädige ich]{12} [mein eigenes Erbteil]{14,15}. [Löse]{16} [du]{19} [für dich]{17,18} [mein Löserecht]{21,22}, [denn]{23} [ich kann]{25} [nicht]{24} [lösen]{26,27}.» ~13(" + OBJ + ") ~20(" + OBJ + ")",
 "RUT.4.7": "Und{1} [so]{2} [war es früher]{3,4} [in]{5} [Israel]{6} [beim]{7,8} [Lösen]{9} und{10} [beim]{11,12} [Tauschen]{13}, [um]{14} [jede]{16} [Sache]{17} [rechtskräftig zu machen]{15}: [Einer]{19} [zog]{18} [seinen Schuh]{20,21} [aus]{18} und{22} [gab ihn]{23} [dem anderen]{24,25,26}. Und{27} [das]{28} war [die Beglaubigung]{29,30} [in]{31} [Israel]{32}.",
 "RUT.4.8": "So{1} [sagte]{2} [der Löser]{3,4} [zu]{5} [Boas]{6}: «[Erwirb es]{7} [für dich]{8,9}!» Und{10} [er zog]{11} [seinen Schuh]{12,13} [aus]{11}.",
 "RUT.4.9": "Und{1} [Boas]{3} [sagte]{2} [zu den Ältesten]{4,5} und{6} [zum ganzen]{7} [Volk]{8,9}: «[Zeugen]{10} [seid ihr]{11} [heute]{12,13}, [dass]{14} [ich]{15} [alles]{17}, [was]{18} [Elimelech]{20} [gehörte]{19}, und{21} [alles]{23}, [was]{24} [Kiljon]{26} und{27} [Machlon]{28} [gehörte]{25}, [aus der Hand]{29,30} [Noomis]{31} [erworben habe]{15}. ~16(" + OBJ + ") ~22(" + OBJ + ")",
 "RUT.4.10": "Und{1} [auch]{2} [Rut]{4}, [die Moabiterin]{5,6}, [die Frau]{7} [Machlons]{8}, [habe ich]{9} [mir]{10,11} [zur]{12} [Frau]{13} [erworben]{9}, [um]{14} [den Namen]{16} [des Verstorbenen]{17,18} [auf]{19} [seinem Erbteil]{20,21} [aufrechtzuerhalten]{15}, [damit]{22} [der Name]{25} [des Verstorbenen]{26,27} [nicht]{23} [aus dem Kreis]{28,29} [seiner Brüder]{30,31} und{32} [aus]{33} [dem Tor]{34} [seines Ortes]{35,36} [ausgelöscht wird]{24}. [Zeugen]{37} [seid ihr]{38} [heute]{39,40}!» ~3(" + OBJ + ")",
 "RUT.4.11": "Und{1} [das ganze]{3} [Volk]{4,5}, [das]{6} [im]{7} [Tor]{8} war, und{9} [die Ältesten]{10,11} [sagten]{2}: «[Wir sind Zeugen]{12}! [JHWH]{14} [mache]{13} [die Frau]{16,17}, [die]{18} [in]{20} [dein Haus]{21,22} [kommt]{19}, [wie]{23} [Rahel]{24} und{25} [wie]{26} [Lea]{27}, [die]{28} [beide]{30,31} [das Haus]{33} [Israel]{34} [gebaut haben]{29}! Und{35} [bring es]{36} [zu Vermögen]{37} [in]{38} [Efrata]{39}, und{40} [mach dir]{41} [einen Namen]{42} [in]{43} [Betlehem]{44,45}! ~15(" + OBJ + ") ~32(" + OBJ + ")",
 "RUT.4.12": "Und{1} [dein Haus]{3,4} [werde]{2} [wie]{5} [das Haus]{6} [des Perez]{7}, [den]{8} [Tamar]{10} [dem Juda]{11,12} [geboren hat]{9}, [durch]{13} [die Nachkommen]{14,15}, [die]{16} [JHWH]{18} [dir]{19,20} [geben wird]{17} [von]{21} [dieser]{24,25} [jungen Frau]{22,23}!»",
 "RUT.4.13": "So{1} [nahm]{2} [Boas]{3} [Rut]{5}, und{6} [sie wurde]{7} [seine]{8,9} [Frau]{10,11}, und{12} [er ging]{13} [zu ihr]{14,15} [ein]{13}. Und{16} [JHWH]{18} [liess]{17} [sie]{19,20} [schwanger werden]{21}, und{22} [sie gebar]{23} [einen Sohn]{24}. ~4(" + OBJ + ")",
 "RUT.4.14": "Da{1} [sagten]{2} [die Frauen]{3,4} [zu]{5} [Noomi]{6}: «[Gepriesen]{7} sei [JHWH]{8}, [der]{9} [es dir]{12,13} [heute]{15,16} [nicht]{10} [an einem Löser]{14} [hat fehlen lassen]{11}! Und{17} [sein Name]{19,20} [werde bekannt]{18} [in]{21} [Israel]{22}!",
 "RUT.4.15": "Und{1} [er wird]{2} [dir]{3,4} [das Leben]{7} [zurückbringen]{5,6} und{8} dich [in deinem Alter]{12,13} [versorgen]{9,10}; denn{14} [deine Schwiegertochter]{15,16}, [die]{17} [dich]{19} [liebt]{18}, [die]{20,21} [für dich]{23,24} [besser]{22} ist [als]{25} [sieben]{26} [Söhne]{27}, [hat]{28} [ihn]{29} [geboren]{28}.» ~11(" + OBJ + ")",
 "RUT.4.16": "Und{1} [Noomi]{3} [nahm]{2} [das Kind]{5,6} und{7} [legte]{8} [es]{9} [auf]{10} [ihren Schoss]{11,12}, und{13} [sie wurde]{14} [ihm]{15,16} [zur Pflegerin]{17,18}. ~4(" + OBJ + ")",
 "RUT.4.17": "Und{1} [die Nachbarinnen]{5,6} [gaben]{2} [ihm]{3,4} [einen Namen]{7} [und sagten]{8,9}: «[Ein Sohn]{11} [ist]{10} [Noomi]{12,13} [geboren]{10}!» Und{14} [sie nannten]{15} [ihn]{16,17} [Obed]{18}. [Er]{19} [ist der Vater]{20} [Isais]{21}, [des Vaters]{22} [Davids]{23}.",
 "RUT.4.18": "Und{1} [dies]{2} [ist der Stammbaum]{3} [des Perez]{4}: [Perez]{5} [zeugte]{6} [Hezron]{8}, ~7(" + OBJ + ")",
 "RUT.4.19": "und{1} [Hezron]{2} [zeugte]{3} [Ram]{5}, und{6} [Ram]{7} [zeugte]{8} [Amminadab]{10}, ~4(" + OBJ + ") ~9(" + OBJ + ")",
 "RUT.4.20": "und{1} [Amminadab]{2} [zeugte]{3} [Nachschon]{5}, und{6} [Nachschon]{7} [zeugte]{8} [Salma]{10}, ~4(" + OBJ + ") ~9(" + OBJ + ")",
 "RUT.4.21": "und{1} [Salmon]{2} [zeugte]{3} [Boas]{5}, und{6} [Boas]{7} [zeugte]{8} [Obed]{10}, ~4(" + OBJ + ") ~9(" + OBJ + ")",
 "RUT.4.22": "und{1} [Obed]{2} [zeugte]{3} [Isai]{5}, und{6} [Isai]{7} [zeugte]{8} [David]{10}. ~4(" + OBJ + ") ~9(" + OBJ + ")",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 1
 "RUT.1.1": "[Es isch gsii]{1,2} [i]{3} [de Ziit]{4}, wo [d Richter]{6,7} [grichtet händ]{5}: Da{8} [isch]{9} [e Hungersnot]{10} [im]{11} [Land]{12} [gsii]{9}. Und{13} [en Maa]{24} [vo]{15} [Betlehem]{16,17} z [Juda]{18} [isch furtzoge]{14}, [zum]{19} [im]{21} [Gebiet]{22} [vo Moab]{23} [als Frömde z wone]{20}, [er]{25} und{26} [sini Frau]{27,28} und{29} [sini zwei Söön]{30,31,32}.",
 "RUT.1.2": "Und{1} [de Maa]{3,4} [hät]{2} [Elimelech]{5} [gheisse]{2}, und{6} [sini Frau]{8,9} [hät]{7} [Noomi]{10} [gheisse]{7}, und{11} [sini zwei Söön]{13,14,15} [händ]{12} [Machlon]{16} und{17} [Kiljon]{18} [gheisse]{12} – [Efratiter]{19} [vo]{20} [Betlehem]{21,22} z [Juda]{23}. Und{24} [si sind]{25} [is Gebiet]{26} [vo Moab]{27} [cho]{25} und{28} [sind]{29} [dört]{30} [plibe]{29}.",
 "RUT.1.3": "Da{1} [isch]{2} [de Elimelech]{3} [gstorbe]{2}, [de Maa]{4} [vo de Noomi]{5}, und{6} [si]{8} [isch]{7} [mit]{9} [irne zwei Söön]{10,11,12} [zruggplibe]{7}.",
 "RUT.1.4": "Und{1} [si händ]{2} [sich]{3,4} [moabitischi]{6} [Fraue]{5} [gnoo]{2}; [di einti]{8,9} [hät]{7} [Orpa]{10} [gheisse]{7}, und{11} [di ander]{13,14} [hät]{12} [Rut]{15} [gheisse]{12}. Und{16} [si händ]{17} [öppe]{19} [zää]{20} [Jaar]{21} [dört]{18} [gwont]{17}.",
 "RUT.1.5": "Da{1} [sind]{2} [au]{3} [di beide]{4,5}, [de Machlon]{6} und{7} [de Kiljon]{8}, [gstorbe]{2}, und{9} [d Frau]{11,12} [isch zruggplibe]{10}, [ohni]{13} [iri zwei Chind]{14,15,16} und{17} [ohni]{18} [ire Maa]{19,20}.",
 "RUT.1.6": "Da{1} [isch]{2} [si]{3} [mit]{4} [irne Schwigertöchtere]{5,6} [ufbroche]{2} und{7} [isch]{8} [us]{9} [em Gebiet]{10} [vo Moab]{11} [zruggcheert]{8}; dänn{12} [si hät]{13} [im]{14} [Gebiet]{15} [vo Moab]{16} [ghört]{13}, [dass]{17} [JHWH]{19} [sich]{18} [um sis Volk]{21,22} [kümmeret hät]{18} [und]{23} [ine]{25,26} [Broot]{27} [gää hät]{24}. ~20(" + OBJ_G + ")",
 "RUT.1.7": "Und{1} [si isch]{2} [vom]{3,4} [Ort]{5} [furtgange]{2}, [wo]{6,8,9} [si gsii isch]{7}, und{10} [iri zwei Schwigertöchtere]{11,12,13} [mit ere]{14,15}; und{16} [si händ sich]{17} [uf de Wäg]{18,19} [gmacht]{17}, [zum]{20} [is]{22} [Land]{23} [Juda]{24} [zrugg z gaa]{21}.",
 "RUT.1.8": "Da{1} [hät]{2} [d Noomi]{3} [zu]{4} [irne zwei Schwigertöchtere]{5,6,7} [gseit]{2}: «[Gönd]{8}, [chered um]{9}, [jedi]{10} [is]{11} [Huus]{12} [vo irer Mueter]{13,14}! [JHWH]{16} [söll]{15} [eu]{17,18} [Tröii]{19} [erwiise]{15}, [so wie]{20,21} [ir]{22} si [de Verstorbne]{23,24,25} und{26} [mir]{27,28} [erwise händ]{22}.",
 "RUT.1.9": "[JHWH]{2} [söll]{1} [eu]{3,4} [gää]{1}, [dass ir]{5} [Rue]{7} [finded]{6}, [jedi]{8} [im Huus]{9} [vo irem Maa]{10,11}!» Und{12} [si hät]{13} [si]{14,15} [küsst]{13}, und{16} [si händ]{17} [iri Stimm]{18,19} [erhobe]{17} und{20} [händ briegget]{21}.",
 "RUT.1.10": "Und{1} [si händ]{2} [zu ire]{3,4} [gseit]{2}: «[Nei]{5}, [mit dir]{6,7} [gönd mir]{8} [zu]{9} [dim Volk]{10,11} [zrugg]{8}!»",
 "RUT.1.11": "Aber{1} [d Noomi]{3} [hät gseit]{2}: «[Chered um]{4}, [mini Töchtere]{5,6}! [Werum]{7,8} [wänd ir]{9} [mit mir]{10,11} [cho]{9}? [Han ich]{14,15} [dänn no]{13} [Söön]{16} [i]{17} [mim Buuch]{18,19}, [wo]{20} [eui]{22,23} [Mane]{24,25} [chönnted wärde]{21}? ~12(" + Q_G + ")",
 "RUT.1.12": "[Chered um]{1}, [mini Töchtere]{2,3}, [gönd]{4}! Dänn{5} [ich bi z alt]{6}, [zum]{7} [en Maa]{9,10} [z haa]{8}. [Wänn]{11} [ich au säge würd]{12}: ‹[Es git]{13} [für mich]{14,15} [Hoffnig]{16}›, [ja, wänn]{17} [ich]{18} [hüt znacht]{19,20} [en Maa]{21,22} [hett]{18} und{23} [sogar]{24} [Söön]{26} [überchäm]{25} –",
 "RUT.1.13": "[würded ir]{3} [drum]{2} [warte]{3}, [bis]{4,5} [si gross wäred]{6}? [Würded ir eu]{9} [drum]{8} [abschlüüsse]{9}, [ohni]{10,11} [en Maa]{13,14} [z haa]{12}? [Nei]{15}, [mini Töchtere]{16,17}! Dänn{18} [es isch]{19} [für mich]{20,21} [vil]{22} [bitterer]{19} [als]{23} [für eu]{24}, dänn{25} [d Hand]{29} [vo JHWH]{30} [hät sich]{26} [gäge mich]{27,28} [gwändet]{26}.» ~1(" + Q_G + ") ~7(" + Q_G + ")",
 "RUT.1.14": "Da{1} [händ si]{2} [iri Stimm]{3,4} [erhobe]{2} und{5} [händ]{6} [nomal]{7} [briegget]{6}. Und{8} [d Orpa]{10} [hät]{9} [iri Schwigermueter]{11,12,13} [küsst]{9}, [aber]{14} [d Rut]{15} [hät sich]{16} [a]{17} [ire]{18} [feschtghebt]{16}.",
 "RUT.1.15": "Da{1} [hät si gseit]{2}: «[Lueg]{3}, [dini Schwägerin]{5,6} [isch]{4} [zu]{7} [irem Volk]{8,9} und{10} [zu]{11} [irne Götter]{12,13} [zruggange]{4}. [Cher um]{14}, [dinere Schwägerin]{16,17} [nache]{15}!»",
 "RUT.1.16": "Aber{1} [d Rut]{3} [hät gseit]{2}: «[Dräng]{5} [mich]{6,7} [nöd]{4}, [dich z verlaa]{8,9,10} und [vo dir wäg]{13,14,15} [umzchere]{11,12}! Dänn{16} [wo]{17,18} [du anegaasch]{19}, [gaan ich ane]{20}, und{21} [wo]{22,23} [du übernachtisch]{24}, [übernacht ich]{25}. [Dis Volk]{26,27} isch [mis Volk]{28,29}, und{30} [din Gott]{31,32} isch [min Gott]{33,34}.",
 "RUT.1.17": "[Wo]{1,2} [du stirbsch]{3}, [stirb ich]{4}, und{5} [dört]{6} [wott ich begrabe wärde]{7}. [So]{8} [söll]{9} [JHWH]{10} [mit mir]{11,12} [mache]{9}, und{13} [so]{14} [söll er wiitermache]{15}: [nu]{16} [de Tod]{17,18} [wird]{19} [mich]{20,21} und{22} [dich]{23,24} [trenne]{19}!»",
 "RUT.1.18": "Wo{1} [si gseh hät]{2}, [dass]{3} [si]{5} [fescht entschlosse isch]{4}, [mit ere]{8,9} [z gaa]{6,7}, da{10} [hät si ufghört]{11}, [uf si iizrede]{12,13,14,15}.",
 "RUT.1.19": "So{1} [sind]{2} [di beide]{3,4} [gange]{2}, [bis]{5} [si]{7} [uf Betlehem]{8,9} [cho sind]{6}. [Wo]{12} [si]{14} [uf Betlehem]{15,16} [cho sind]{13}, da{17} [isch]{18} [di ganz Stadt]{19,20,21} [wäge ine]{22,23} [in Ufruer cho]{18}, und{24} [d Fraue händ gseit]{25}: «[Isch das]{26,27} [d Noomi]{28}?» ~10(" + WAYHI_G + ") ~11(" + WAYHI_G + ")",
 "RUT.1.20": "Aber{1} [si hät]{2} [zu ine]{3,4} [gseit]{2}: «[Säged]{6} [mir]{7,8} [nöd]{5} [Noomi]{9}, [säged]{10} [mir]{11,12} [Mara]{13}! Dänn{14} [de Allmächtig]{16} [hät]{15} [mir]{17,18} [seer]{19} [bitter mitgspilt]{15}.",
 "RUT.1.21": "[Voll]{2} [bi]{3} [ich]{1} [furtgange]{3}, und{4} [läär]{5} [hät]{6} [mich]{7} [JHWH]{8} [zruggbracht]{6}. [Werum]{9,10} [säged]{11} [ir mir]{12,13} [Noomi]{14}, [wo doch]{15} [JHWH]{16} [gäge]{18} [mich]{19} [usgseit hät]{17} und{20} [de Allmächtig]{21} [mir]{23,24} [Böses aataa hät]{22}?»",
 "RUT.1.22": "So{1} [isch]{2} [d Noomi]{3} [zruggcho]{2}, und{4} [mit ere]{10,11} [d Rut]{5}, [d Moabiterin]{6,7}, [iri Schwigertochter]{8,9}, [wo]{12} [us]{14} [em Gebiet]{15} [vo Moab]{16} [zruggcho isch]{13}. Und{17} [si]{18} [sind]{19} [uf Betlehem]{20,21} [cho]{19}, [am]{22} [Aafang]{23} [vo de Gerschteernt]{24,25}.",
 # ------------------------------------------------------------ Kapitel 2
 "RUT.2.1": "Und{1} [d Noomi]{3} [hät]{2} [en Verwandte]{4} [vo de Siite]{5} [vo irem Maa]{6,7} [gha]{2}, [en Maa]{8} [mit Vermöge]{9,10} [us]{11} [de Sippe]{12} [vom Elimelech]{13}; und{14} [er hät]{15,16} [Boas]{17} [gheisse]{15,16}.",
 "RUT.2.2": "Und{1} [d Rut]{3}, [d Moabiterin]{4,5}, [hät]{2} [zu]{6} [de Noomi]{7} [gseit]{2}: «[Lass mich doch]{9} [ufs Fäld]{10,11} [gaa]{8} und{12} [Ääre]{14,15} [ufläse]{13} [hinder]{16} [dem]{17} [här]{16}, [bi dem]{20,21,22} [ich]{18} [Gnad]{19} [find]{18}!» Und{23} [si hät]{24} [zu ire]{25,26} [gseit]{24}: «[Gang]{27}, [mini Tochter]{28,29}!»",
 "RUT.2.3": "So{1} [isch si gange]{2} und{3} [cho]{4} und{5} [hät]{6} [uf em Fäld]{7,8} [hinder]{9} [de Schnitter]{10,11} [Ääre ufgläse]{6}. Und{12} [es hät sich]{13} [zuefällig]{14} [so gää]{13}, [dass si]{15} [uf s Fäldstück]{16,17,18} [vom Boas]{19,20} cho isch, [wo]{21} [us]{22} [de Sippe]{23} [vom Elimelech]{24} gsii isch.",
 "RUT.2.4": "Und{1} [grad da]{2} [isch]{4} [de Boas]{3} [vo]{5} [Betlehem]{6,7} [cho]{4} und{8} [hät]{9} [zu de Schnitter]{10,11} [gseit]{9}: «[JHWH]{12} sig [mit eu]{13,14}!» Und{15} [si händ]{16} [zu im]{17,18} [gseit]{16}: «[JHWH]{21} [söll]{19} [dich]{20} [sägne]{19}!»",
 "RUT.2.5": "Und{1} [de Boas]{3} [hät]{2} [zu]{4} [sim Chnächt]{5,6}, [wo]{7} [über]{9} [d Schnitter]{10,11} [gsetzt gsii isch]{8}, [gseit]{2}: «[Zu wem ghört]{12,13} [die]{16,17} [jung Frau]{14,15}?»",
 "RUT.2.6": "Und{1} [de Chnächt]{3,4}, [wo]{5} [über]{7} [d Schnitter]{8,9} [gsetzt gsii isch]{6}, [hät gantwortet]{2} und{10} [gseit]{11}: «[Das isch]{12} [e moabitischi]{14} [jungi Frau]{13}, [wo]{15} [mit]{17} [de Noomi]{18} [us]{19} [em Gebiet]{20} [vo Moab]{21} [zruggcho isch]{16}.",
 "RUT.2.7": "Und{1} [si hät gseit]{2}: ‹[Lass mich doch]{4} [Ääre ufläse]{3} und{5} [zwüsche]{7} [de Garbe]{8} [zämeläse]{6}, [hinder]{9} [de Schnitter]{10,11} [här]{9}.› So{12} [isch si cho]{13} und{14} [isch]{15} [sit]{16,17} [em Morge]{18,19} und{20} [bis]{21} [jetzt]{22} [da]{15}; [da]{23} [isch si]{24,25} [chuum]{28} [im Huus]{26,27} [gsässe]{24,25}.»",
 "RUT.2.8": "Da{1} [hät]{2} [de Boas]{3} [zu]{4} [de Rut]{5} [gseit]{2}: «[Los]{8} [emal]{6,7}, [mini Tochter]{9,10}: [Gang]{12} [nöd]{11} [uf]{15} [es anders]{17} [Fäld]{16} [go ufläse]{13,14}, und{18} [gang]{21} [au]{19} [nöd]{20} [vo da]{22,23} [wäg]{21}, und{24} [halt dich]{26,27} [da]{25} [zu]{28} [mine Arbeiterinne]{29,30}.",
 "RUT.2.9": "[Dini Auge]{1,2} söled [uf s Fäld]{3,4} grichtet sii, [wo]{5} [si schnided]{6,7}, und{8} [gang]{9} [hinder]{10} [ine]{11} [här]{10}. [Han ich]{14} [de Chnächt]{16,17} [nöd]{12,13} [befole]{14}, [dich]{21} [nöd]{18,19} [aazrüere]{20}? Und{22} [wänn du Durscht häsch]{23}, [dänn]{24} [gang]{25} [zu]{26} [de Gfäss]{27,28} und{29} [trink]{30} [vo dem]{31}, [wo]{32} [d Chnächt]{35,36} [schöpfed]{33,34}. ~15(" + OBJ_G + ")",
 "RUT.2.10": "Da{1} [isch si]{2} [uf]{3} [ires Gsicht]{4,5} [gfalle]{2} und{6} [hät sich]{7} [bis uf de Bode]{8,9} [verneigt]{7} und{10} [hät]{11} [zu im]{12,13} [gseit]{11}: «[Werum]{14} [han ich]{15} [Gnad]{16} [i]{17} [dine Auge]{18,19} [gfunde]{15}, [dass du]{20} [mich]{22} [beachtisch]{21}, [wo ich doch]{23,24} [e Frömdi]{25} bi?»",
 "RUT.2.11": "Und{1} [de Boas]{3} [hät gantwortet]{2} und{4} [hät]{5} [zu ire]{6,7} [gseit]{5}: «[Mir isch]{10,11} [gnau]{8} [verzellt worde]{9}, [alles]{12}, [wo]{13} [du]{14} [für]{15} [dini Schwigermueter]{16,17} [gmacht häsch]{14} [nach]{18} [em Tod]{19} [vo dim Maa]{20,21}, und{22} [wie du]{23} [din Vatter]{24,25} und{26} [dini Mueter]{27,28} und{29} [s Land]{30} [vo dinere Herkunft]{31,32} [verlaa häsch]{23} und{33} [zu]{35} [eme Volk]{36} [gange bisch]{34}, [wo]{37} [du]{39} [vorher]{40,41:idiom} [nöd]{38} [kännt häsch]{39}.",
 "RUT.2.12": "[JHWH]{2} [söll]{1} [dis Tue]{3,4} [vergälte]{1}, und{5} [din Loo]{7,8} [söll]{6} [voll]{9} [sii]{6} [vo]{10,11} [JHWH]{12}, [em Gott]{13} [vo Israel]{14}, [zu dem]{15} [du cho bisch]{16}, [zum]{17} [under]{19} [sine Flügel]{20,21} [Schutz z sueche]{18}!»",
 "RUT.2.13": "Und{1} [si hät gseit]{2}: «[Möcht ich]{3} [Gnad]{4} [finde]{3} [i]{5} [dine Auge]{6,7}, [min Herr]{8,9}! Dänn{10} [du häsch]{11} [mich]{12} [tröschtet]{11} und{13,14} [häsch]{15} [dinere Magd]{18,19} [is Herz]{16,17} [gredt]{15}, [obwohl]{20} [ich]{21} [nöd]{22} [bi]{23} [wie]{24} [eini]{25} [vo dine Mägd]{26,27}.»",
 "RUT.2.14": "Und{1} [zur]{6} [Ässeziit]{7,8,9} [hät]{2} [de Boas]{5} [zu ire]{3,4} [gseit]{2}: «[Chumm]{10} [häre]{11} und{12} [iss]{13} [vom]{14,15} [Broot]{16} und{17} [tunk]{18} [dis Stück]{19,20} [in]{21} [Essig]{22}!» Und{23} [si isch]{24} [näbe]{25,26} [d Schnitter]{27,28} [anegsässe]{24}, und{29} [er hät]{30} [ire]{31,32} [grööschtets Chorn]{33} [gää]{30}, und{34} [si hät gässe]{35} und{36} [isch satt worde]{37} und{38} [hät no übrig gha]{39}.",
 "RUT.2.15": "Wo{1} [si ufgstande isch]{2}, [zum ufläse]{3,4}, [hät]{6} [de Boas]{7} [sine Chnächt]{9,10} [befole]{6} [und gseit]{11,12}: «[Au]{13} [zwüsche]{14} [de Garbe]{15,16} [dörf si ufläse]{17}, und{18} [beschämed]{20} [si]{21} [nöd]{19}! ~5(" + VAV_G + ") ~8(" + OBJ_G + ")",
 "RUT.2.16": "Und{1} [zieht]{4} [ire]{5,6} [sogar]{2} [extra]{3} [öppis us]{7} [de Bündel]{8,9} [use]{4} und{10} [lönd s ligge]{11}, [demit si]{12} [s ufläse cha]{13}, und{14} [schimpfed]{16} [nöd]{15} [mit ere]{17,18}!»",
 "RUT.2.17": "So{1} [hät si]{2} [uf em Fäld]{3,4} [ufgläse]{2} [bis]{5} [am Aabig]{6,7}. Und{8} [si hät usgchlopft]{9}, [was]{11} [si ufgläse gha hät]{12}, und{13} [es isch]{14} [öppe]{15} [es Efa]{16} [Gerschte]{17} [gsii]{14}. ~10(" + OBJ_G + ")",
 "RUT.2.18": "Und{1} [si hät s ufglade]{2} und{3} [isch]{4} [i d Stadt]{5,6} [cho]{4}, und{7} [iri Schwigermueter]{9,10} [hät gseh]{8}, [was]{12} [si ufgläse gha hät]{13}. Und{14} [si hät füregnoo]{15} und{16} hät [ire]{18,19} [gää]{17}, [was]{21} [si übrig gloo hät]{22}, [nachdem si]{23} [satt gsii isch]{24,25}. ~11(" + OBJ_G + ") ~20(" + OBJ_G + ")",
 "RUT.2.19": "Da{1} [hät]{2} [iri Schwigermueter]{5,6} [zu ire]{3,4} [gseit]{2}: «[Wo]{7} [häsch du]{8} [hüt]{9,10} [ufgläse]{8}, und{11} [wo]{12} [häsch gschaffet]{13}? [Gsägnet]{17} [sig]{14} [dä, wo dich beachtet hät]{15,16}!» Und{18} [si hät]{19} [irer Schwigermueter]{20,21,22} [verzellt]{19}, [bi wem]{24,26,27} [si gschaffet hät]{25}, und{28} [hät gseit]{29}: «[De Maa]{31,32}, [bi dem]{33,35,36} [ich]{34} [hüt]{37,38} [gschaffet han]{34}, [heisst]{30} [Boas]{39}.» ~23(" + OBJ_G + ")",
 "RUT.2.20": "Da{1} [hät]{2} [d Noomi]{3} [zu]{4} [irer Schwigertochter]{5,6} [gseit]{2}: «[Gsägnet]{7} [sig er]{8} [vo]{9} [JHWH]{10}, [wo]{11} [sini Tröii]{14,15} [de Läbige]{16,17,18} und{19} [de Toote]{20,21,22} [nöd]{12} [entzoge hät]{13}!» Und{23} [d Noomi]{27} [hät]{24} [zu ire]{25,26} [gseit]{24}: «[De Maa]{31,32} [isch]{28} [mit üs]{29,30} [nooch verwandt]{28}; [er]{36} [isch eine]{33} [vo öisne Löser]{34,35}.»",
 "RUT.2.21": "Und{1} [d Rut]{3}, [d Moabiterin]{4,5}, [hät gseit]{2}: «[Er hät]{8} [mir]{9,10} [sogar]{6,7} [gseit]{8}: ‹[Halt dich]{17,18} [zu]{11} [de Chnächt]{12,13}, [wo]{14} [zu mir ghöred]{15,16}, [bis si]{19,20} [di ganz]{23} [Ernt]{24,25}, [wo]{26} [mir ghört]{27,28}, [iibracht händ]{21}.›» ~22(" + OBJ_G + ")",
 "RUT.2.22": "Da{1} [hät]{2} [d Noomi]{3} [zu]{4} [de Rut]{5}, [irer Schwigertochter]{6,7}, [gseit]{2}: «[Es isch guet]{8}, [mini Tochter]{9,10}, [wänn]{11} [du]{12} [mit]{13} [sine Arbeiterinne]{14,15} [usegaasch]{12}, [demit]{16} [me]{18} [dich]{19,20} [uf]{21} [eme andere]{23} [Fäld]{22} [nöd]{17} [belästiget]{18}.»",
 "RUT.2.23": "So{1} [hät si sich]{2} [zu]{3} [de Arbeiterinne]{4} [vom Boas]{5} [ghalte]{2}, [zum ufläse]{6,7}, [bis]{8} [d Gerschteernt]{10,11,12} und{13} [d Weizeernt]{14,15,16} [fertig gsii sind]{9}. Und{17} [si hät]{18} [bi]{19} [irer Schwigermueter]{20,21} [gwont]{18}.",
 # ------------------------------------------------------------ Kapitel 3
 "RUT.3.1": "Und{1} [d Noomi]{5}, [iri Schwigermueter]{6,7}, [hät]{2} [zu ire]{3,4} [gseit]{2}: «[Mini Tochter]{8,9}, [söll ich]{12} [dir]{13,14} [nöd]{10,11} [es Daheim]{15} [sueche]{12}, [wo]{16} [s dir]{18,19} [guet gaat]{17}?",
 "RUT.3.2": "[Also]{1,2}: [Isch]{3} [de Boas]{5} [nöd]{4} [öise Verwandte]{6,7}, [bi]{8,10} [dem sine Arbeiterinne]{11,12} [du gsii bisch]{9}? [Lueg]{13}, [er]{14} [worflet]{15} [hüt znacht]{20,21} [d Gerschte]{18,19} [uf de Tänn]{17}. ~16(" + OBJ_G + ")",
 "RUT.3.3": "[Wäsch dich]{2} und{3} [salb dich]{4} und{5} [leg]{6} [dini Chleider]{7,8} [aa]{9,10}, und{11} [gang abe]{12} [uf d Tänn]{13,14}. [Gib dich]{16} [em Maa]{17,18} [nöd]{15} [z erchänne]{16}, [bis er]{19,21} [fertig]{20} [gässe]{22,23} und{24} [trunke]{25,26} [hät]{20}. ~1(" + VAV_G + ")",
 "RUT.3.4": "Und{1} [wänn]{2,3} [er]{5} [sich häreleit]{4}, [dänn]{6} [merk dir]{7} [de Ort]{9,10}, [wo]{11,13} [er sich häreleit]{12}, und{14} [gang ane]{15} und{16} [deck]{17} [sini Füess]{18,19} [uf]{17} und{20} [leg dich ane]{21}. Und{22} [er]{23} [wird]{24} [dir]{25,26} [säge]{24}, [was]{28} [du mache söllsch]{29,30}.» ~8(" + OBJ_G + ") ~27(" + OBJ_G + ")",
 "RUT.3.5": "Und{1} [si hät]{2} [zu ire]{3,4} [gseit]{2}: «[Alles]{5}, [wo]{6} [du]{7} [mir]{8,9} [seisch]{7}, [mach ich]{10}.»",
 "RUT.3.6": "So{1} [isch si]{2} [uf d Tänn]{3,4} [abegange]{2} und{5} [hät]{6} [alles]{8} [gnau so]{7} [gmacht]{6}, [wie]{9} [iri Schwigermueter]{12,13} [ire]{11} [ufträit hät]{10}.",
 "RUT.3.7": "Und{1} [de Boas]{3} [hät gässe]{2} und{4} [trunke]{5}, und{6} [es isch]{7} [im]{9} [wohl gsii]{7} [ums Herz]{8}. Und{10} [er isch gange]{11}, [zum sich häreläge]{12,13} [am]{14} [Änd]{15} [vom Chornhuufe]{16,17}. [Da]{18} [isch si]{19} [liisli]{20,21} [cho]{19} und{22} [hät]{23} [sini Füess]{24,25} [ufdeckt]{23} und{26} [sich häregleit]{27}.",
 "RUT.3.8": "[Um]{3} [Mitternacht]{4,5,6} [isch]{8} [de Maa]{9,10} [ufgschreckt]{8} und{11} [hät sich umdräit]{12}, und{13} [da]{14} [isch]{16} [e Frau]{15} [zu sine Füess]{17,18} [gläge]{16}. ~1(" + WAYHI_G + ") ~2(" + WAYHI_G + ") ~7(" + VAV_G + ")",
 "RUT.3.9": "Und{1} [er hät gseit]{2}: «[Wär]{3} [bisch du]{4}?» Und{5} [si hät gseit]{6}: «[Ich bi]{7} [d Rut]{8}, [dini Dieneri]{9,10}. [So]{11} [spreit]{12} [de Zipfel vo dim Gwand]{13,14} [über]{15} [dini Dieneri]{16,17} [uus]{12}, dänn{18} [du bisch]{20} [en Löser]{19}.»",
 "RUT.3.10": "Und{1} [er hät gseit]{2}: «[Gsägnet]{3} [sigsch du]{4} [vo]{5} [JHWH]{6}, [mini Tochter]{7,8}! [Du häsch]{9} [dini Tröii]{10,11} [jetzt]{12,13} [no schöner zeigt]{9} [als]{14} [am Aafang]{15,16}, [dass du]{17} [nöd]{18} [de junge Mane]{21,22} [nachegloffe bisch]{19,20}, [öb]{23} [arm]{24} [oder]{25,26} [riich]{27}.",
 "RUT.3.11": "[Und jetzt]{1,2}, [mini Tochter]{3,4}, [förcht dich]{6} [nöd]{5}! [Alles]{7}, [wo]{8} [du seisch]{9}, [mach ich]{10} [für dich]{11,12}; dänn{13} [jede]{15} [im Tor]{16} [vo mim Volk]{17,18} [weiss]{14}, [dass]{19} [du]{22} [e tüchtigi Frau]{20,21} bisch.",
 "RUT.3.12": "[Jetzt]{1,2}, [es]{3} [stimmt]{4}, [dass]{5} [ich]{7} [en Löser]{6} [bi]{7}; [aber]{8} [es git]{10} [au]{9} [en Löser]{11}, [wo nööcher verwandt isch]{12} [als ich]{13,14}.",
 "RUT.3.13": "[Bliib]{1} [hüt znacht]{2,3} da; und{4} [dänn]{5} [am Morge]{6,7}: [wänn]{8} [er]{9} [dich]{10} [löse wott]{9}, [guet]{11}, [söll er löse]{12}; und{13} [wänn]{14} [er]{16} [dich]{19} [nöd]{15} [wott]{16} [löse]{17,18}, [dänn]{20} [lös ich]{21} [dich]{22}, [ich sälber]{23} – [so wahr]{24} [JHWH]{25} [läbt]{24}! [Bliib ligge]{26} [bis]{27} [am Morge]{28,29}.»",
 "RUT.3.14": "So{1} [isch si]{2} [zu sine Füess]{3,4} [gläge]{2} [bis]{5} [am Morge]{6,7}. Und{8} [si isch ufgstande]{9}, [bevor]{10,11} [eine]{13} [de ander]{15,16} [hät chöne erchänne]{12}. Und{17} [er hät gseit]{18}: «[Es dörf]{20} [nöd]{19} [uschoo]{20}, [dass]{21} [d Frau]{23,24} [uf d Tänn]{25,26} [cho isch]{22}.» ~14(" + OBJ_G + ")",
 "RUT.3.15": "Und{1} [er hät gseit]{2}: «[Gib]{3} mir [de Umhang]{4,5}, [wo]{6} [du aahäsch]{7,8}, und{9} [heb]{10} [en]{11,12} [uf]{10}!» Und{13} [si hät]{14} [en]{15,16} [ufghebt]{14}, und{17} [er hät]{18} [sächs Mass]{19} [Gerschte]{20} [abgmässe]{18} und{21} [ire]{23,24} [ufgleit]{22}. Und{25} [er isch]{26} [i d Stadt]{27,28} [gange]{26}.",
 "RUT.3.16": "Und{1} [si isch]{2} [zu]{3} [irer Schwigermueter]{4,5} [cho]{2}, und{6} [die hät gseit]{7}: «[Wie staats um dich]{8,9:idiom}, [mini Tochter]{10,11}?» Und{12} [si hät]{13} [ire]{14,15} [alles]{17} [verzellt]{13}, [wo]{18} [de Maa]{22,23} [für si]{20,21} [gmacht hät]{19}. ~16(" + OBJ_G + ")",
 "RUT.3.17": "Und{1} [si hät gseit]{2}: «[Die]{6,7} [sächs Mass]{3} [Gerschte]{4,5} [hät er]{8} [mir]{9,10} [gää]{8}; dänn{11} [er hät]{12} [zu mir]{13,14} [gseit]{12}: ‹[Chumm]{16} [nöd]{15} [mit lääre Händ]{17} [zu]{18} [dinere Schwigermueter]{19,20}!›»",
 "RUT.3.18": "Da{1} [hät si gseit]{2}: «[Bliib sitze]{3}, [mini Tochter]{4,5}, [bis]{6,7} [du weisch]{8,9}, [wie]{10} [d Sach]{12} [usgaat]{11}; dänn{13} [de Maa]{16,17} [git]{15} [kei]{14} [Rue]{15}, [bis er]{18,19} [d Sach]{21,22} [hüt]{23,24} [erlediget hät]{20}.»",
 # ------------------------------------------------------------ Kapitel 4
 "RUT.4.1": "[De Boas]{2} aber{1} [isch]{3} [zum Tor]{4,5} [ufegange]{3} und{6} [isch]{7} [dört]{8} [abghocket]{7}. Und{9} [grad da]{10} [isch]{16} [de Löser]{11,12} [verbiicho]{16}, [vo dem]{13} [de Boas]{15} [gredt gha hät]{14}. Und{17} [er hät gseit]{18}: «[Chumm]{19,20}, [hock ab]{21,22} [da]{23}, [du Soundso]{24,25:idiom}!» Und{26} [er isch cho]{27} und{28} [isch abghocket]{29}.",
 "RUT.4.2": "Und{1} [er hät]{2} [zää]{3} [Mane]{4} [vo]{5} [de Ältischte]{6} [vo de Stadt]{7,8} [gholt]{2} und{9} [gseit]{10}: «[Hocked ab]{11} [da]{12}!» Und{13} [si sind abghocket]{14}.",
 "RUT.4.3": "Dänn{1} [hät er]{2} [zum Löser]{3,4} [gseit]{2}: «[S Fäldstück]{5,6,7}, [wo]{8} [öisem Brueder]{10,11} [Elimelech]{12,13} [ghört hät]{9}, [verchauft]{14} [d Noomi]{15}, [wo]{16} [us]{18} [em Gebiet]{19} [vo Moab]{20} [zruggcho isch]{17}.",
 "RUT.4.4": "Und{1} [ich]{2} [han dänkt]{3}, [ich legs dir offe]{4,5,6:idiom} [und säg]{7,8}: [Erwirb s]{9} [vor]{10} [dene, wo da hocked]{11,12}, und{13} [vor]{14} [de Ältischte]{15} [vo mim Volk]{16,17}! [Wänn]{18} [du löse wottsch]{19}, [dänn lös]{20}! Und{21} [wänn]{22} [er]{24} [nöd]{23} [löse wott]{24}, [dänn säg s]{25,26} [mir]{27,28}, [demit ich]{29} [s weiss]{30}; dänn{31} [es git]{32} [usser]{33} [dir]{34} [keine]{32}, [wo chönnt löse]{35,36}, und{37} [ich]{38} [chume nach]{39} [dir]{40}.» Und{41} [er hät gseit]{42}: «[Ich]{43} [wott löse]{44}.»",
 "RUT.4.5": "Da{1} [hät]{2} [de Boas]{3} [gseit]{2}: «[Am Taag]{4,5}, [wo du]{7} [s Fäld]{8,9} [us de Hand]{10,11} [vo de Noomi]{12} [erwirbsch]{6}, [erwirbsch du]{22} s [au]{13} [vo]{14,15} [de Rut]{16}, [de Moabiterin]{17,18}, [de Frau]{19} [vom Verstorbne]{20,21}, [zum]{23} [de Name]{25} [vom Verstorbne]{26,27} [uf]{28} [sim Erbteil]{29,30} [z erhalte]{24}.»",
 "RUT.4.6": "Da{1} [hät]{2} [de Löser]{3,4} [gseit]{2}: «[Ich cha]{6} [für mich]{9,10} [nöd]{5} [löse]{7,8}, [suscht]{11} [schädig ich]{12} [mis eige Erbteil]{14,15}. [Lös]{16} [du]{19} [für dich]{17,18} [mis Löserächt]{21,22}, [dänn]{23} [ich cha]{25} [nöd]{24} [löse]{26,27}.» ~13(" + OBJ_G + ") ~20(" + OBJ_G + ")",
 "RUT.4.7": "Und{1} [so]{2} [isch es früener]{3,4} [in]{5} [Israel]{6} [gsii]{3,4} [bim]{7,8} [Löse]{9} und{10} [bim]{11,12} [Tuusche]{13}, [zum]{14} [jedi]{16} [Sach]{17} [rächtsgültig z mache]{15}: [Eine]{19} [hät]{18} [sin Schue]{20,21} [abzoge]{18} und{22} [hät en]{23} [em andere]{24,25,26} [gää]{23}. Und{27} [das]{28} isch [d Beglaubigung]{29,30} [in]{31} [Israel]{32} gsii.",
 "RUT.4.8": "So{1} [hät]{2} [de Löser]{3,4} [zum]{5} [Boas]{6} [gseit]{2}: «[Erwirb s]{7} [für dich]{8,9}!» Und{10} [er hät]{11} [sin Schue]{12,13} [abzoge]{11}.",
 "RUT.4.9": "Und{1} [de Boas]{3} [hät]{2} [zu de Ältischte]{4,5} und{6} [zum ganze]{7} [Volk]{8,9} [gseit]{2}: «[Züüge]{10} [sind ir]{11} [hüt]{12,13}, [dass]{14} [ich]{15} [alles]{17}, [wo]{18} [em Elimelech]{20} [ghört hät]{19}, und{21} [alles]{23}, [wo]{24} [em Kiljon]{26} und{27} [em Machlon]{28} [ghört hät]{25}, [us de Hand]{29,30} [vo de Noomi]{31} [erworbe han]{15}. ~16(" + OBJ_G + ") ~22(" + OBJ_G + ")",
 "RUT.4.10": "Und{1} [au]{2} [d Rut]{4}, [d Moabiterin]{5,6}, [d Frau]{7} [vom Machlon]{8}, [han ich]{9} [mir]{10,11} [zur]{12} [Frau]{13} [erworbe]{9}, [zum]{14} [de Name]{16} [vom Verstorbne]{17,18} [uf]{19} [sim Erbteil]{20,21} [z erhalte]{15}, [demit]{22} [de Name]{25} [vom Verstorbne]{26,27} [nöd]{23} [us em Chreis]{28,29} [vo sine Brüeder]{30,31} und{32} [us]{33} [em Tor]{34} [vo sim Ort]{35,36} [usglöscht wird]{24}. [Züüge]{37} [sind ir]{38} [hüt]{39,40}!» ~3(" + OBJ_G + ")",
 "RUT.4.11": "Und{1} [s ganz]{3} [Volk]{4,5}, [wo]{6} [im]{7} [Tor]{8} gsii isch, und{9} [d Ältischte]{10,11} [händ gseit]{2}: «[Mir sind Züüge]{12}! [JHWH]{14} [söll]{13} [d Frau]{16,17}, [wo]{18} [i]{20} [dis Huus]{21,22} [chunnt]{19}, [wie]{23} [d Rahel]{24} und{25} [wie]{26} [d Lea]{27} [mache]{13}, [wo]{28} [beidi]{30,31} [s Huus]{33} [Israel]{34} [baut händ]{29}! Und{35} [bring es]{36} [zu Vermöge]{37} [z]{38} [Efrata]{39}, und{40} [mach dir]{41} [en Name]{42} [z]{43} [Betlehem]{44,45}! ~15(" + OBJ_G + ") ~32(" + OBJ_G + ")",
 "RUT.4.12": "Und{1} [dis Huus]{3,4} [söll]{2} [wie]{5} [s Huus]{6} [vom Perez]{7} [wärde]{2}, [wo]{8} [d Tamar]{10} [em Juda]{11,12} [gebore hät]{9}, [dur]{13} [d Nachkomme]{14,15}, [wo]{16} [JHWH]{18} [dir]{19,20} [git]{17} [vo]{21} [dere]{24,25} [junge Frau]{22,23}!»",
 "RUT.4.13": "So{1} [hät]{2} [de Boas]{3} [d Rut]{5} [gnoo]{2}, und{6} [si isch]{7} [sini]{8,9} [Frau]{10,11} [worde]{7}, und{12} [er isch]{13} [zu ire]{14,15} [gange]{13}. Und{16} [JHWH]{18} [hät]{17} [si]{19,20} [schwanger wärde]{21} [laa]{17}, und{22} [si hät]{23} [en Sohn]{24} [übercho]{23}. ~4(" + OBJ_G + ")",
 "RUT.4.14": "Da{1} [händ]{2} [d Fraue]{3,4} [zu]{5} [de Noomi]{6} [gseit]{2}: «[Globt]{7} sig [JHWH]{8}, [wo]{9} [dich]{12,13} [hüt]{15,16} [nöd]{10} [ohni Löser]{14} [glaa hät]{11}! Und{17} [sin Name]{19,20} [söll bekannt wärde]{18} [in]{21} [Israel]{22}!",
 "RUT.4.15": "Und{1} [er wird]{2} [dir]{3,4} [s Läbe]{7} [zruggbringe]{5,6} und{8} dich [i dim Alter]{12,13} [versorge]{9,10}; dänn{14} [dini Schwigertochter]{15,16}, [wo]{17} [dich]{19} [gern hät]{18}, [wo]{20,21} [für dich]{23,24} [besser]{22} isch [als]{25} [sibe]{26} [Söön]{27}, [hät]{28} [en]{29} [übercho]{28}.» ~11(" + OBJ_G + ")",
 "RUT.4.16": "Und{1} [d Noomi]{3} [hät]{2} [s Chind]{5,6} [gnoo]{2} und{7} [hät]{8} [s]{9} [uf]{10} [ire Schoss]{11,12} [gleit]{8}, und{13} [si isch]{14} [sini]{15,16} [Pflegeri]{17,18} [worde]{14}. ~4(" + OBJ_G + ")",
 "RUT.4.17": "Und{1} [d Nachbarinne]{5,6} [händ]{2} [im]{3,4} [en Name]{7} [gää]{2} [und gseit]{8,9}: «[De Noomi]{12,13} [isch]{10} [en Sohn]{11} [gebore]{10}!» Und{14} [si händ]{15} [en]{16,17} [Obed]{18} [gnännt]{15}. [Er]{19} [isch de Vatter]{20} [vom Isai]{21}, [em Vatter]{22} [vom David]{23}.",
 "RUT.4.18": "Und{1} [das]{2} [isch de Stammbaum]{3} [vom Perez]{4}: [De Perez]{5} [isch de Vatter]{6} [vom Hezron]{8} [gsii]{6}, ~7(" + OBJ_G + ")",
 "RUT.4.19": "und{1} [de Hezron]{2} [isch de Vatter]{3} [vom Ram]{5} [gsii]{3}, und{6} [de Ram]{7} [isch de Vatter]{8} [vom Amminadab]{10} [gsii]{8}, ~4(" + OBJ_G + ") ~9(" + OBJ_G + ")",
 "RUT.4.20": "und{1} [de Amminadab]{2} [isch de Vatter]{3} [vom Nachschon]{5} [gsii]{3}, und{6} [de Nachschon]{7} [isch de Vatter]{8} [vom Salma]{10} [gsii]{8}, ~4(" + OBJ_G + ") ~9(" + OBJ_G + ")",
 "RUT.4.21": "und{1} [de Salmon]{2} [isch de Vatter]{3} [vom Boas]{5} [gsii]{3}, und{6} [de Boas]{7} [isch de Vatter]{8} [vom Obed]{10} [gsii]{8}, ~4(" + OBJ_G + ") ~9(" + OBJ_G + ")",
 "RUT.4.22": "und{1} [de Obed]{2} [isch de Vatter]{3} [vom Isai]{5} [gsii]{3}, und{6} [de Isai]{7} [isch de Vatter]{8} [vom David]{10} [gsii]{8}. ~4(" + OBJ_G + ") ~9(" + OBJ_G + ")",
}

JHWH_DE = ("Der Gottesname wird im Judentum nicht ausgesprochen; gelesen wird «Adonai» (der Herr). Viele deutsche Bibeln schreiben "
           "«der HERR». Hier steht der Name in seinen vier Konsonanten, damit sichtbar bleibt, dass im Hebräischen ein Name steht.")
JHWH_GSW = ("De Gottesname wird im Judetum nöd usgsproche; gläse wird «Adonai» (de Herr). Vili düütschi Bible schriibed «der HERR». "
            "Da staat de Name i sine vier Konsonante, demit me gseet, dass im Hebräische en Name staat.")

# Übersetzungsentscheidungen: (Stelle, Zieltext, Art, hebräisch, wörtlicher, andere Möglichkeiten, Begründung)
DEC_DE = [
 # Kapitel 1
 ("RUT.1.1", "Gebiet", "interpretive", "בִּשְׂדֵי", "in den Feldern Moabs", ["im Land Moab", "auf den Fluren Moabs"],
  "שָׂדֶה heisst «Feld, offenes Land»; gemeint ist das Gebiet Moabs östlich des Toten Meeres. Die Form kann Einzahl oder Mehrzahl sein."),
 ("RUT.1.1", "als Fremder zu wohnen", "literal", "לָגוּר", None, ["um sich niederzulassen"],
  "גּוּר meint das Wohnen als Fremder ohne volle Rechte im Gastland."),
 ("RUT.1.4", "moabitische", "literal", "מֹאֲבִיּוֹת", None, None,
  "Dass Rut Moabiterin ist, betont das Buch immer wieder (z. B. [[RUT.2.2]], [[RUT.4.5]], [[RUT.4.10]]). Nach [[DEU.23.3]] sollen Ammoniter "
  "und Moabiter nicht in die Versammlung JHWHs kommen; [[NEH.13.1]] führt das gegen Ehen mit fremden Frauen an. Das Buch Rut nimmt dazu nicht "
  "ausdrücklich Stellung. Die Mischna (Jevamot 8,3) bezieht das Verbot nur auf Männer; der Babylonische Talmud fasst das in die Formel "
  "«Moabiter, nicht Moabiterin» (Jevamot 76b). Andere lesen Rut als "
  "bewusste Gegenstimme zu Esra und Nehemia (vgl. [[EZR.10.3]]). Hier wird keine Deutung festgelegt."),
 ("RUT.1.6", "JHWH", "interpretive", "יְהוָה", None, ["der HERR", "der Ewige", "Jahwe"], JHWH_DE),
 ("RUT.1.6", "Brot", "literal", "לָחֶם", None, ["Nahrung"],
  "Wortspiel: Die Hungersnot herrschte ausgerechnet in Betlehem, hebräisch «Haus des Brotes» (בֵּית לֶחֶם)."),
 ("RUT.1.8", "Treue", "interpretive", "חֶסֶד", None, ["Güte", "Huld", "Liebe", "Loyalität"],
  "חֶסֶד ist ein Leitwort des Buches ([[RUT.2.20]], [[RUT.3.10]]): verlässliche Zuwendung in einer Beziehung, die über das Geschuldete "
  "hinausgeht. Kein deutsches Wort deckt das ganz ab; hier steht durchgehend «Treue», damit die Wiederholung sichtbar bleibt."),
 ("RUT.1.8", "erweise", "literal", "יַעַשׂ", "tue", None,
  "Die Tokens folgen hier dem Qere (in MACULA als Qere markiert). Geschrieben ist nach der masoretischen Randangabe eine längere Form; die "
  "Bedeutung ändert sich nicht. Das Ketiv selbst ist in den Daten nicht enthalten."),
 ("RUT.1.9", "Ruhe", "literal", "מְנוּחָה", None, ["ein Zuhause", "Geborgenheit"],
  "Gemeint ist ein gesichertes Leben in einer neuen Ehe; vgl. [[RUT.3.1]]."),
 ("RUT.1.12", "einen Mann zu haben", "adapted", "לְאִישׁ", "für einen Mann zu sein", ["zu heiraten"],
  "הָיָה לְאִישׁ ist eine Wendung für das Verheiratetsein; ebenso in [[RUT.1.13]]."),
 ("RUT.1.13", "verschliessen", "interpretive", "תֵּעָגֵנָה", None, ["zurückhalten", "allein bleiben"],
  "Das Verb ist in der Bibel nur hier belegt; die Bedeutung wird aus dem Zusammenhang erschlossen. Im späteren Hebräisch heisst eine Frau, "
  "die nicht wieder heiraten kann, עֲגוּנָה."),
 ("RUT.1.13", "bitterer als euch", "interpretive", "מַר מְאֹד מִכֶּם", None, ["es ist mir euretwegen sehr bitter", "mein Los ist zu bitter für euch"],
  "מִן kann vergleichen («mehr als euch») oder den Grund angeben («euretwegen»). Beides ist grammatisch möglich."),
 ("RUT.1.14", "hielt sich", "literal", "דָּבְקָה", None, ["hing an ihr", "blieb bei ihr"],
  "Dasselbe Verb steht in [[GEN.2.24]] für das Anhangen des Mannes an seine Frau; vgl. auch [[RUT.2.8]] und [[RUT.2.23]]."),
 ("RUT.1.15", "ihren Göttern", "interpretive", "אֱלֹהֶיהָ", None, ["ihrem Gott"],
  "אֱלֹהִים ist eine Mehrzahlform und kann einen Gott oder mehrere Götter meinen. Im Mund Noomis über Moab liegt «Götter» nahe; dieselbe "
  "Form heisst in [[RUT.1.16]] «dein Gott»."),
 ("RUT.1.16", "wohin du gehst, dahin gehe ich", "literal", "תֵּלְכִי אֵלֵךְ", None, ["wo du hingehst, da will ich auch hingehen"],
  "Die Verbformen können Gegenwart, Zukunft oder Absicht ausdrücken. Ruts Worte gelten ihrer Schwiegermutter; sie binden sie an deren Weg, "
  "Volk, Gott und Grab ([[RUT.1.17]]). Heute werden sie oft bei Trauungen gelesen."),
 ("RUT.1.16", "übernachtest", "literal", "תָּלִינִי", None, ["bleibst"],
  "לִין heisst «übernachten». Die vertraute Wiedergabe «wo du bleibst, da bleibe ich auch» deutet es auf das dauernde Wohnen."),
 ("RUT.1.16", "Dein Volk ist mein Volk", "interpretive", "עַמֵּךְ עַמִּי", None, ["Dein Volk soll mein Volk sein"],
  "Im Hebräischen steht ein Satz ohne Verb; ob Rut eine Feststellung oder eine Zusage für die Zukunft ausspricht, muss die Übersetzung entscheiden."),
 ("RUT.1.17", "So soll JHWH mir tun", "literal", "כֹּה יַעֲשֶׂה", None, ["JHWH tue mir dies und das", "JHWH soll mich strafen"],
  "Feste Schwurformel: Wer schwört, ruft eine Strafe auf sich herab, falls er das Versprochene bricht. Rut schwört beim Gott Israels."),
 ("RUT.1.17", "nur der Tod", "interpretive", "כִּי הַמָּוֶת", None, ["wenn mich etwas anderes als der Tod von dir trennt", "nicht einmal der Tod"],
  "כִּי kann in Schwüren beteuern oder eine Bedingung einleiten. Je nach Lesart trennt nur der Tod die beiden oder nicht einmal er."),
 ("RUT.1.20", "Mara", "literal", "מָרָא", None, None,
  "Noomi (נָעֳמִי) bedeutet etwa «meine Liebliche», Mara «die Bittere». Mara ist hier ungewöhnlich mit א statt mit ה geschrieben. Die "
  "Schreibung «Noomi» folgt verbreiteten deutschen Bibeln (englisch Naomi)."),
 ("RUT.1.20", "der Allmächtige", "traditional", "שַׁדַּי", "Schaddai", ["der Gewaltige"],
  "Herkunft und Bedeutung von שַׁדַּי sind unsicher; «der Allmächtige» ist die vertraute Wiedergabe."),
 ("RUT.1.21", "ausgesagt", "interpretive", "עָנָה", None, ["mich gedemütigt"],
  "עָנָה בְּ heisst «gegen jemanden aussagen». Mit anderen Vokalen gelesen (עִנָּה) hiesse es «hat mich gedemütigt»; so verstehen es "
  "manche alte Übersetzungen (in den Daten nicht erfasst)."),
 ("RUT.1.22", "zurückkam", "literal", "הַשָּׁבָה", None, ["die mitkam"],
  "Wörtlich «die Zurückgekehrte». Rut war nie in Juda; das Wort verbindet sie mit Noomis Heimkehr. Manche beziehen es auf Noomi."),
 # Kapitel 2
 ("RUT.2.1", "Mann von Vermögen", "interpretive", "גִּבּוֹר חַיִל", "ein Held an Kraft", ["ein angesehener Mann", "ein tüchtiger Mann", "ein wohlhabender Grundbesitzer"],
  "גִּבּוֹר חַיִל kann einen Kriegshelden, einen tüchtigen oder einen wohlhabenden, angesehenen Mann bezeichnen; hier liegen Vermögen und "
  "Ansehen nahe. Dasselbe חַיִל kennzeichnet Rut in [[RUT.3.11]] und steht im Segen [[RUT.4.11]]."),
 ("RUT.2.1", "Verwandten", "literal", "מוֹדַע", None, ["Bekannten"],
  "Die Tokens folgen hier dem Qere (in MACULA als Qere markiert). Das geschriebene Ketiv wird meist als «Bekannter, Vertrauter» gelesen; "
  "es ist in den Daten nicht enthalten."),
 ("RUT.2.3", "zufällig", "interpretive", "מִקְרֶהָ", "es traf sie ihr Zufall", None,
  "Die Erzählung spricht betont vom Zufall; viele Ausleger sehen darin eine absichtliche Untertreibung, hinter der Gottes Führung steht. "
  "Der Text sagt das nicht ausdrücklich."),
 ("RUT.2.7", "kaum", "interpretive", "מְעָט", None, ["nur kurz"],
  "Der Schluss des Verses ist schwer verständlich; vielleicht ist der Text beschädigt. «Haus» meint wohl eine Schutzhütte auf dem Feld. Die "
  "alten Übersetzungen weichen hier ab (in den Daten nicht erfasst)."),
 ("RUT.2.8", "Hör", "adapted", "לוֹא שָׁמַעַתְּ", "Hast du nicht gehört", None, "Rhetorische Frage, die Aufmerksamkeit verlangt."),
 ("RUT.2.8", "Arbeiterinnen", "adapted", "נַעֲרֹתָי", "jungen Frauen", ["Mägden"],
  "נַעֲרָה heisst «junge Frau», oft eine junge Bedienstete; so wird auch Rut selbst genannt ([[RUT.2.5]]). Davon unterschieden werden "
  "שִׁפְחָה «Magd» ([[RUT.2.13]]) und אָמָה «Dienerin» ([[RUT.3.9]])."),
 ("RUT.2.10", "beachtest", "literal", "לְהַכִּירֵנִי", None, ["dich um mich kümmerst"],
  "Wortspiel: הִכִּיר «beachten, anerkennen» klingt an נָכְרִיָּה «Fremde» an."),
 ("RUT.2.11", "vorher", "adapted", "תְּמוֹל שִׁלְשׁוֹם", "gestern und vorgestern", None, "Feste Wendung für «früher, bisher»."),
 ("RUT.2.12", "Flügeln", "literal", "כְּנָפָיו", None, ["Schutz"],
  "Bild für Gottes Schutz wie der eines Vogels über seinen Jungen. Dasselbe Wort כָּנָף nimmt Rut in [[RUT.3.9]] auf, wenn sie Boas bittet, "
  "seinen Gewandzipfel über sie zu breiten."),
 ("RUT.2.13", "Möge ich", "interpretive", "אֶמְצָא", "ich finde", None,
  "Die Form kann eine Feststellung («ich finde Gunst») oder einen Wunsch ausdrücken."),
 ("RUT.2.17", "Efa", "literal", "כְּאֵיפָה", None, None,
  "Ein Hohlmass; heutige Schätzungen schwanken (oft zwischen etwa 20 und 40 Litern). Für einen Tag Ährenlesen ist es eine grosse Menge."),
 ("RUT.2.20", "seine Treue", "interpretive", "חַסְדּוֹ", None, None,
  "Unklar ist, ob sich «der» auf JHWH oder auf Boas bezieht; beides ist grammatisch möglich. Zu חֶסֶד vgl. [[RUT.1.8]]."),
 ("RUT.2.20", "Lösern", "literal", "מִגֹּאֲלֵנוּ", None, ["Auslösern", "Verwandten mit Einlöserecht"],
  "Ein גֹּאֵל ist ein naher Verwandter, der verkauftes Familienland zurückkauft ([[LEV.25.25]]), in Schuldsklaverei Geratene auslöst "
  "([[LEV.25.48]]) oder für erschlagene Verwandte eintritt. Die Pflicht, die Witwe eines kinderlos verstorbenen Bruders zu heiraten "
  "([[DEU.25.5]]), ist eine eigene Einrichtung; das Buch Rut verbindet beides."),
 # Kapitel 3
 ("RUT.3.1", "einen Ort der Ruhe", "literal", "מָנוֹחַ", None, ["ein Zuhause"], "Nimmt Noomis Wunsch aus [[RUT.1.9]] auf."),
 ("RUT.3.3", "geh hinab", "literal", "וְיָרַדְתְּ", None, None,
  "Die Tokens folgen dem Qere (in MACULA als Qere markiert). Das geschriebene Ketiv sieht aus wie die 1. Person («und ich gehe "
  "hinab»); viele erklären es als alte Form der 2. Person weiblich, mit derselben Bedeutung wie das Qere. Ebenso in [[RUT.3.4]]. "
  "Das Ketiv ist in den Daten nicht enthalten."),
 ("RUT.3.4", "seine Füsse", "interpretive", "מַרְגְּלֹתָיו", "die Stelle zu seinen Füssen", ["leg dich zu seinen Füssen", "deck ihn an den Füssen auf"],
  "מַרְגְּלוֹת ist ein seltenes Wort für die Gegend der Füsse. «Füsse» kann in der Bibel auch verhüllend für die Scham stehen; ob die "
  "Szene eine sexuelle Nebenbedeutung hat, ist umstritten. Die Erzählung lässt das in der Schwebe."),
 ("RUT.3.4", "leg dich hin", "literal", "וְשָׁכָבְתְּ", None, None,
  "Qere wie in [[RUT.3.3]] (in MACULA markiert); das Ketiv sieht aus wie die 1. Person (Erklärungen siehe dort) und ist in den Daten nicht enthalten."),
 ("RUT.3.8", "drehte sich um", "interpretive", "וַיִּלָּפֵת", None, ["beugte sich vor", "tastete umher"],
  "Das Verb ist selten; gemeint ist eine Bewegung des Erschreckten."),
 ("RUT.3.9", "den Zipfel deines Gewandes", "interpretive", "כְנָפֶךָ", "deinen Flügel", ["deinen Mantel", "deinen Saum"],
  "כָּנָף heisst «Flügel» und «Gewandzipfel». Den Gewandzipfel über eine Frau zu breiten ist eine Geste der Heirat ([[EZK.16.8]]). Rut "
  "greift das Wort aus [[RUT.2.12]] auf: Boas soll selbst zu dem Schutz werden, den er ihr unter Gottes Flügeln gewünscht hat."),
 ("RUT.3.9", "Dienerin", "literal", "אֲמָתֶךָ", None, ["Magd"],
  "In [[RUT.2.13]] nannte sich Rut שִׁפְחָה «Magd», hier אָמָה. Manche Ausleger sehen in אָמָה eine Dienerin, die als Ehefrau in Frage kommt."),
 ("RUT.3.9", "ein Löser", "literal", "גֹאֵל", None, None, "Rut verbindet die Bitte um Heirat mit dem Löserecht; vgl. [[RUT.2.20]]."),
 ("RUT.3.10", "deine Treue", "interpretive", "חַסְדֵּךְ", None, ["deine Güte"],
  "Die «erste» Treue ist wohl Ruts Treue gegenüber Noomi ([[RUT.2.11]]), die «spätere», dass sie einen Löser aus der Familie sucht statt "
  "eines jüngeren Mannes."),
 ("RUT.3.11", "eine tüchtige Frau", "interpretive", "אֵשֶׁת חַיִל", "eine Frau von Kraft", ["eine tugendhafte Frau", "eine angesehene Frau", "eine Frau von Wert"],
  "Dasselbe חַיִל wie bei Boas ([[RUT.2.1]]); die beiden erscheinen als ebenbürtig. Die Wendung steht auch in [[PRO.31.10]]; in manchen "
  "hebräischen Bibelausgaben (nach dem Codex Leningradensis) folgt Rut unmittelbar auf die Sprüche."),
 ("RUT.3.11", "jeder im Tor", "adapted", "כָּל שַׁעַר", "das ganze Tor", ["die ganze Stadt"],
  "Das Tor ist der Ort der Öffentlichkeit und des Rechts; gemeint sind die Leute der Stadt."),
 ("RUT.3.14", "bevor", "literal", "בְּטֶרֶם", None, None,
  "Qere (in MACULA markiert); das Ketiv unterscheidet sich nur in der Schreibung, ohne Bedeutungsunterschied."),
 ("RUT.3.15", "sechs Mass", "interpretive", "שֵׁשׁ", "sechs", None,
  "Das Mass ist nicht angegeben; vermutlich eine kleinere Einheit, die eine Frau tragen kann."),
 ("RUT.3.15", "er ging", "literal", "וַיָּבֹא", None, ["sie ging"],
  "Der masoretische Text hat die männliche Form; manche Handschriften und alte Übersetzungen lesen «sie ging» (in den Daten nicht erfasst)."),
 ("RUT.3.16", "Wie steht es um dich", "interpretive", "מִי אַתְּ", "Wer bist du", ["Wie ist es dir ergangen"],
  "Dieselbe Frage stellt Boas in [[RUT.3.9]]. Noomi fragt wohl, als was Rut zurückkommt."),
 ("RUT.3.17", "mit leeren Händen", "adapted", "רֵיקָם", "leer", None,
  "Dasselbe Wort wie in Noomis Klage [[RUT.1.21]]: «leer hat mich JHWH zurückgebracht»."),
 # Kapitel 4
 ("RUT.4.1", "du Soundso", "interpretive", "פְּלֹנִי אַלְמֹנִי", "Peloni Almoni", ["mein Freund", "Herr Soundso"],
  "Feste Wendung für eine Person, die nicht genannt wird. Boas wird den Mann beim Namen gerufen haben; der Erzähler verschweigt ihn – "
  "vielleicht, weil dieser Löser den Namen des Verstorbenen nicht erhalten will ([[RUT.4.6]])."),
 ("RUT.4.3", "verkauft", "interpretive", "מָכְרָה", None, ["hat verkauft", "will verkaufen"],
  "Die Vergangenheitsform kann einen gefassten Entschluss ausdrücken. Wie Noomi zu dem Feld kam und ob es schon verkauft ist, sagt der Text nicht."),
 ("RUT.4.3", "unserem Bruder", "literal", "לְאָחִינוּ", None, ["unserem Verwandten"], "«Bruder» bezeichnet hier einen Verwandten."),
 ("RUT.4.4", "ich lege es dir offen", "adapted", "אֶגְלֶה אָזְנְךָ", "ich will dein Ohr aufdecken", None,
  "Wendung für «jemanden in Kenntnis setzen»."),
 ("RUT.4.4", "wenn er nicht lösen will", "literal", "יִגְאַל", None, ["wenn du nicht lösen willst"],
  "Der masoretische Text hat die 3. Person; vielleicht wendet sich Boas kurz an die Ältesten. Viele Handschriften und alte Übersetzungen "
  "haben die 2. Person (in den Daten nicht erfasst)."),
 ("RUT.4.5", "erwirbst du", "interpretive", "קָנִיתָה", "hast du erworben", ["erwirbst du auch Rut", "erwerbe ich (Ketiv)"],
  "Schlüsselstelle. Die Tokens folgen dem Qere «du erwirbst» (in MACULA als Qere markiert); das geschriebene Ketiv wird als «ich erwerbe» "
  "gelesen – dann kündigt Boas an, er selbst werde Rut heiraten. Oft wird zudem «und von Rut» in «auch Rut» geändert (vgl. [[RUT.4.10]]); "
  "das ist eine Konjektur. Die Verbindung von Landkauf und Heirat erinnert an die Schwagerehe ([[DEU.25.5]]), ist dort aber nicht so "
  "geregelt. Übersetzt ist der überlieferte Qere-Text; keine Lesart ist als richtig entschieden."),
 ("RUT.4.6", "schädige ich mein eigenes Erbteil", "interpretive", "אַשְׁחִית", "verderbe ich", None,
  "Vermutlich, weil ein Sohn mit Rut als Erbe Machlons gälte und das Feld dann nicht beim Löser bliebe. Der Text nennt den Grund nicht."),
 ("RUT.4.7", "Schuh", "literal", "נַעֲלוֹ", None, ["Sandale"],
  "Der Erzähler erklärt einen alten Brauch. In [[DEU.25.9]] wird der Schuh dem verweigernden Schwager zur Schande ausgezogen; hier "
  "besiegelt er eine Übertragung."),
 ("RUT.4.11", "bring es zu Vermögen", "interpretive", "עֲשֵׂה חַיִל", "tu Kraft", ["werde mächtig", "zeuge Nachkommen"],
  "Wieder חַיִל wie in [[RUT.2.1]] und [[RUT.3.11]]; gemeint sein kann Wohlstand, Ansehen oder Kinderreichtum."),
 ("RUT.4.11", "mach dir einen Namen", "interpretive", "קְרָא שֵׁם", "rufe einen Namen", ["werde berühmt"],
  "Die genaue Bedeutung der Wendung ist unsicher."),
 ("RUT.4.12", "Tamar", "literal", "תָמָר", None, None,
  "Vgl. [[GEN.38.29]]: Auch Tamar sicherte durch ungewöhnliches Handeln der Familie Judas Nachkommen."),
 ("RUT.4.14", "werde bekannt", "interpretive", "יִקָּרֵא", "werde gerufen", ["werde gerühmt"],
  "Unklar ist, ob der Name des Lösers (des Kindes) oder JHWHs gemeint ist."),
 ("RUT.4.15", "das Leben", "interpretive", "מֵשִׁיב נֶפֶשׁ", "einer, der die Seele zurückbringt", ["dich erquicken"],
  "«Zurückbringen» (שׁוּב) nimmt Noomis Klage auf: «leer hat mich JHWH zurückgebracht» ([[RUT.1.21]])."),
 ("RUT.4.16", "Pflegerin", "literal", "לְאֹמֶנֶת", None, ["Amme", "Wärterin"],
  "Ob die Geste eine Adoption ausdrückt, ist umstritten."),
 ("RUT.4.18", "Stammbaum", "adapted", "תּוֹלְדוֹת", "Zeugungen", ["Geschlechterfolge"],
  "Die Formel kennt man aus dem Buch Genesis (z. B. [[GEN.5.1]]). Die Liste nennt zehn Generationen von Perez bis David; Boas steht an siebter Stelle."),
 ("RUT.4.20", "Salma", "literal", "שַׂלְמָה", None, ["Salmon"],
  "In [[RUT.4.21]] heisst derselbe Mann שַׂלְמוֹן (Salmon); beide Schreibungen sind beibehalten."),
]

DEC_GSW = [
 # Kapitel 1
 ("RUT.1.1", "Gebiet", "interpretive", "בִּשְׂדֵי", "i de Fälder vo Moab", ["im Land Moab"],
  "שָׂדֶה heisst «Fäld, offes Land»; gmeint isch s Gebiet vo Moab östlich vom Tote Meer."),
 ("RUT.1.1", "als Frömde z wone", "literal", "לָגוּר", None, ["zum sich niderlaa"],
  "גּוּר meint s Wone als Frömde ohni volli Rächt im Gaschtland."),
 ("RUT.1.4", "moabitischi", "literal", "מֹאֲבִיּוֹת", None, None,
  "Dass d Rut e Moabiterin isch, betont s Buech immer wider (z. B. [[RUT.2.2]], [[RUT.4.5]], [[RUT.4.10]]). Nach [[DEU.23.3]] söled "
  "Ammoniter und Moabiter nöd i d Versammlig vo JHWH cho; [[NEH.13.1]] füert das gäge Ee mit frömde Fraue aa. S Buech Rut nimmt dezue nöd "
  "usdrücklich Stellig. D Mischna (Jevamot 8,3) bezieht s Verbot nu uf Mane; de Babylonisch Talmud fasst das i d Formle "
  "«Moabiter, nöd Moabiterin» (Jevamot 76b). Anderi läsed d Rut als "
  "bewussti Gägestimm zu Esra und Nehemia (vgl. [[EZR.10.3]]). Da wird kei Düütig feschtgleit."),
 ("RUT.1.6", "JHWH", "interpretive", "יְהוָה", None, ["de HERR", "de Ewig", "Jahwe"], JHWH_GSW),
 ("RUT.1.6", "Broot", "literal", "לָחֶם", None, ["Ässe"],
  "Wortspiil: D Hungersnot isch usgrächnet z Betlehem gsii, hebräisch «Huus vom Broot» (בֵּית לֶחֶם)."),
 ("RUT.1.8", "Tröii", "interpretive", "חֶסֶד", None, ["Güeti", "Liebi"],
  "חֶסֶד isch es Leitwort vom Buech ([[RUT.2.20]], [[RUT.3.10]]): verlässlichi Zuewändig i nere Beziehig, wo über das usegaat, wo me "
  "schuldig isch. Kei Wort deckt das ganz ab; da staat überall «Tröii», demit me d Widerholig gseet."),
 ("RUT.1.8", "erwiise", "literal", "יַעַשׂ", "mache", None,
  "D Tokens folged da em Qere (i MACULA als Qere markiert). Gschribe isch nach de masoretische Randaagab e lengeri Form; d Bedüütig "
  "änderet nöd. S Ketiv sälber isch i de Date nöd enthalte."),
 ("RUT.1.9", "Rue", "literal", "מְנוּחָה", None, ["es Daheim"], "Gmeint isch es gsicherets Läbe i nere nöie Ee; vgl. [[RUT.3.1]]."),
 ("RUT.1.12", "en Maa z haa", "adapted", "לְאִישׁ", "für en Maa z sii", ["z hürate"],
  "הָיָה לְאִישׁ isch e Wändig für s Ghürate-Sii; gliich i [[RUT.1.13]]."),
 ("RUT.1.13", "abschlüüsse", "interpretive", "תֵּעָגֵנָה", None, ["zruggha", "elei bliibe"],
  "S Verb chunnt i de Bible nu da vor; d Bedüütig schlüüsst me us em Zämehang. Im spööttere Hebräisch heisst e Frau, wo nöd wider cha "
  "hürate, עֲגוּנָה."),
 ("RUT.1.13", "bitterer als für eu", "interpretive", "מַר מְאֹד מִכֶּם", None, ["es isch mir wäge eu seer bitter"],
  "מִן cha vergliiche («meer als eu») oder de Grund aagää («wäge eu»). Beides isch grammatisch möglich."),
 ("RUT.1.14", "feschtghebt", "literal", "דָּבְקָה", None, ["isch bi ire plibe"],
  "S gliich Verb staat i [[GEN.2.24]] für s Aahange vom Maa a sini Frau; vgl. au [[RUT.2.8]] und [[RUT.2.23]]."),
 ("RUT.1.15", "irne Götter", "interpretive", "אֱלֹהֶיהָ", None, ["irem Gott"],
  "אֱלֹהִים isch e Meerzaalform und cha ein Gott oder meereri Götter meine. Im Muul vo de Noomi über Moab liit «Götter» nooch; di gliich "
  "Form heisst i [[RUT.1.16]] «din Gott»."),
 ("RUT.1.16", "wo du anegaasch, gaan ich ane", "literal", "תֵּלְכִי אֵלֵךְ", None, ["wo du hiegaasch, gaan ich au hii"],
  "D Verbforme chönd Gägewart, Zuekunft oder Absicht usdrucke. D Wort vo de Rut gälted irer Schwigermueter; si binded si a dere ire Wäg, "
  "ires Volk, ire Gott und ires Grab ([[RUT.1.17]]). Hüt list me si oft a Hochzite."),
 ("RUT.1.16", "übernachtisch", "literal", "תָּלִינִי", None, ["bliibsch"],
  "לִין heisst «übernachte». Di vertrout Widergab «wo du bleibst, da bleibe ich auch» dütet s uf s dauerhafte Wone."),
 ("RUT.1.16", "Dis Volk isch mis Volk", "interpretive", "עַמֵּךְ עַמִּי", None, ["Dis Volk söll mis Volk sii"],
  "Im Hebräische staat en Satz ohni Verb; öb d Rut öppis feschtstellt oder öppis verspricht für d Zuekunft, mues d Übersetzig entscheide."),
 ("RUT.1.17", "So söll JHWH mit mir mache", "literal", "כֹּה יַעֲשֶׂה", None, ["JHWH söll mich straafe"],
  "Feschti Schwuerformle: Wär schwört, rüeft e Straaf uf sich abe, falls er s Versproche bricht. D Rut schwört bim Gott vo Israel."),
 ("RUT.1.17", "nu de Tod", "interpretive", "כִּי הַמָּוֶת", None, ["wänn mich öppis anders als de Tod vo dir trännt", "nöd emal de Tod"],
  "כִּי cha i Schwüer öppis beteuere oder e Bedingig iileite. Je nach Läsart trännt nu de Tod die zwei oder nöd emal er."),
 ("RUT.1.20", "Mara", "literal", "מָרָא", None, None,
  "Noomi (נָעֳמִי) heisst öppe «mini Liebliichi», Mara «di Bitter». Mara isch da ungwöönlich mit א statt mit ה gschribe. D Schriibig «Noomi» "
  "folgt verbreitete düütsche Bible (änglisch Naomi)."),
 ("RUT.1.20", "de Allmächtig", "traditional", "שַׁדַּי", "Schaddai", None,
  "Herkunft und Bedüütig vo שַׁדַּי sind unsicher; «de Allmächtig» isch di vertrout Widergab."),
 ("RUT.1.21", "usgseit", "interpretive", "עָנָה", None, ["mich demüetiget"],
  "עָנָה בְּ heisst «gäge öpper ussäge». Mit andere Vokal gläse (עִנָּה) hiess es «hät mich demüetiget»; so verstönd s es paar alti "
  "Übersetzige (i de Date nöd erfasst)."),
 ("RUT.1.22", "zruggcho isch", "literal", "הַשָּׁבָה", None, ["wo mitcho isch"],
  "Wörtlich «di Zruggkeerti». D Rut isch nie z Juda gsii; s Wort verbindet si mit em Heichoo vo de Noomi. Es paar beziend s uf d Noomi."),
 # Kapitel 2
 ("RUT.2.1", "Maa mit Vermöge", "interpretive", "גִּבּוֹר חַיִל", "en Held a Chraft", ["en aagsäänige Maa", "en tüchtige Maa"],
  "גִּבּוֹר חַיִל cha en Chriegsheld, en tüchtige oder en riiche, aagsäänige Maa bezeichne; da liit Vermöge und Aasee nooch. S gliich "
  "חַיִל kännzeichnet d Rut i [[RUT.3.11]] und staat im Säge [[RUT.4.11]]."),
 ("RUT.2.1", "Verwandte", "literal", "מוֹדַע", None, ["Bekannte"],
  "D Tokens folged da em Qere (i MACULA als Qere markiert). S gschribnig Ketiv list me meischt als «Bekannte, Vertroute»; es isch i de "
  "Date nöd enthalte."),
 ("RUT.2.3", "zuefällig", "interpretive", "מִקְרֶהָ", "es hät si ire Zuefall troffe", None,
  "D Erzälig redt betont vom Zuefall; vili Usleger gsänd drin e absichtlichi Undertriibig, wo Gott sini Füerig dahinder staat. De Text "
  "seit das nöd usdrücklich."),
 ("RUT.2.7", "chuum", "interpretive", "מְעָט", None, ["nu churz"],
  "De Schluss vom Vers isch schwär verständlich; vilicht isch de Text beschädiget. «Huus» meint wohl e Schutzhütte uf em Fäld. Di alte "
  "Übersetzige wiiched da ab (i de Date nöd erfasst)."),
 ("RUT.2.8", "Los", "adapted", "לוֹא שָׁמַעַתְּ", "Häsch nöd ghört", None, "Rhetorischi Frag, wo Ufmerksamkeit verlangt."),
 ("RUT.2.8", "Arbeiterinne", "adapted", "נַעֲרֹתָי", "junge Fraue", ["Mägd"],
  "נַעֲרָה heisst «jungi Frau», oft e jungi Aagstellti; so wird au d Rut sälber gnännt ([[RUT.2.5]]). Devo underschide wärded שִׁפְחָה "
  "«Magd» ([[RUT.2.13]]) und אָמָה «Dieneri» ([[RUT.3.9]])."),
 ("RUT.2.10", "beachtisch", "literal", "לְהַכִּירֵנִי", None, ["dich um mich kümmerisch"],
  "Wortspiil: הִכִּיר «beachte, aaerchänne» tönt ähnlich wie נָכְרִיָּה «Frömdi»."),
 ("RUT.2.11", "vorher", "adapted", "תְּמוֹל שִׁלְשׁוֹם", "geschter und vorgeschter", None, "Feschti Wändig für «früener, bis jetzt»."),
 ("RUT.2.12", "Flügel", "literal", "כְּנָפָיו", None, ["Schutz"],
  "Bild für de Schutz vo Gott wie de vo me Vogel über sine Junge. S gliich Wort כָּנָף nimmt d Rut i [[RUT.3.9]] uf, wo si de Boas bittet, "
  "de Zipfel vo sim Gwand über si z spreite."),
 ("RUT.2.13", "Möcht ich", "interpretive", "אֶמְצָא", "ich find", None,
  "D Form cha öppis feschtstelle («ich find Gnad») oder en Wunsch usdrucke."),
 ("RUT.2.17", "Efa", "literal", "כְּאֵיפָה", None, None,
  "Es Hohlmass; hütigi Schätzige gönd usenand (oft zwüsche öppe 20 und 40 Liter). Für ein Taag Ääre läse isch das vil."),
 ("RUT.2.20", "sini Tröii", "interpretive", "חַסְדּוֹ", None, None,
  "Unklar isch, öb sich «wo» uf JHWH oder uf de Boas bezieht; beides isch grammatisch möglich. Zu חֶסֶד vgl. [[RUT.1.8]]."),
 ("RUT.2.20", "Löser", "literal", "מִגֹּאֲלֵנוּ", None, ["Uslöser", "Verwandti mit Iilöserächt"],
  "En גֹּאֵל isch en noche Verwandte, wo verchaufts Familieland zruggchauft ([[LEV.25.25]]), Verwandti us de Schuldsklaverei uslöst "
  "([[LEV.25.48]]) oder für erschlageni Verwandti iistaat. D Pflicht, d Witwe vo me chinderlos verstorbne Brueder z hürate ([[DEU.25.5]]), "
  "isch e eigeni Iirichtig; s Buech Rut verbindet beides."),
 # Kapitel 3
 ("RUT.3.1", "es Daheim", "interpretive", "מָנוֹחַ", "en Ort vo Rue", None, "Nimmt de Wunsch vo de Noomi us [[RUT.1.9]] uf."),
 ("RUT.3.3", "gang abe", "literal", "וְיָרַדְתְּ", None, None,
  "D Tokens folged em Qere (i MACULA als Qere markiert). S gschribnig Ketiv gseet uus wie di 1. Person («und ich gaan abe»); vili erkläred s als "
  "alti Form vo de 2. Person wiiblich, mit de gliiche Bedüütig wie s Qere. Gliich i [[RUT.3.4]]. S Ketiv isch i de Date nöd enthalte."),
 ("RUT.3.4", "sini Füess", "interpretive", "מַרְגְּלֹתָיו", "d Stell bi sine Füess", ["leg dich zu sine Füess"],
  "מַרְגְּלוֹת isch es sälts Wort für d Gägend vo de Füess. «Füess» cha i de Bible au verhüllend für d Scham staa; öb d Szene e sexuelli "
  "Nebebedüütig hät, isch umstritte. D Erzälig laat das offe."),
 ("RUT.3.4", "leg dich ane", "literal", "וְשָׁכָבְתְּ", None, None,
  "Qere wie i [[RUT.3.3]] (i MACULA markiert); s Ketiv gseet uus wie di 1. Person (Erklärige lueg dört), und es isch i de Date nöd enthalte."),
 ("RUT.3.8", "hät sich umdräit", "interpretive", "וַיִּלָּפֵת", None, ["hät sich vüregeboge", "hät umetaschtet"],
  "S Verb isch sälte; gmeint isch e Bewegig vo öpperem, wo verschrickt."),
 ("RUT.3.9", "de Zipfel vo dim Gwand", "interpretive", "כְנָפֶךָ", "din Flügel", ["din Mantel"],
  "כָּנָף heisst «Flügel» und «Gwandzipfel». De Gwandzipfel über e Frau spreite isch e Geschte vo de Hochzig ([[EZK.16.8]]). D Rut nimmt "
  "s Wort us [[RUT.2.12]] uf: De Boas söll sälber de Schutz wärde, won er ire under de Flügel vo Gott gwünscht hät."),
 ("RUT.3.9", "Dieneri", "literal", "אֲמָתֶךָ", None, ["Magd"],
  "I [[RUT.2.13]] hät sich d Rut שִׁפְחָה «Magd» gnännt, da אָמָה. Es paar Usleger gsänd i אָמָה e Dieneri, wo als Frau in Frag chunnt."),
 ("RUT.3.9", "en Löser", "literal", "גֹאֵל", None, None, "D Rut verbindet d Bitt um d Hochzig mit em Löserächt; vgl. [[RUT.2.20]]."),
 ("RUT.3.10", "dini Tröii", "interpretive", "חַסְדֵּךְ", None, ["dini Güeti"],
  "Di «erscht» Tröii isch wohl d Tröii vo de Rut zur Noomi ([[RUT.2.11]]), di «spöter», dass si en Löser us de Familie suecht statt en "
  "jüngere Maa."),
 ("RUT.3.11", "e tüchtigi Frau", "interpretive", "אֵשֶׁת חַיִל", "e Frau vo Chraft", ["e aagsäänigi Frau", "e Frau vo Wärt"],
  "S gliich חַיִל wie bim Boas ([[RUT.2.1]]); di zwei sind enand ebebürtig. D Wändig staat au i [[PRO.31.10]]; i es paar hebräische "
  "Bibelusgabe (nach em Codex Leningradensis) chunnt s Buech Rut grad nach de Sprüch."),
 ("RUT.3.11", "jede im Tor", "adapted", "כָּל שַׁעַר", "s ganz Tor", ["di ganz Stadt"],
  "S Tor isch de Ort vo de Öffentlichkeit und vom Rächt; gmeint sind d Lüüt vo de Stadt."),
 ("RUT.3.14", "bevor", "literal", "בְּטֶרֶם", None, None,
  "Qere (i MACULA markiert); s Ketiv underscheidet sich nu i de Schriibig, ohni Bedüütigsunderschiid."),
 ("RUT.3.15", "sächs Mass", "interpretive", "שֵׁשׁ", "sächs", None,
  "S Mass staat nöd da; vermuetlich e chliineri Iiheit, wo e Frau cha träge."),
 ("RUT.3.15", "er isch", "literal", "וַיָּבֹא", None, ["si isch"],
  "De masoretisch Text hät di männlich Form; es paar Handschrifte und alti Übersetzige läsed «si isch gange» (i de Date nöd erfasst)."),
 ("RUT.3.16", "Wie staats um dich", "interpretive", "מִי אַתְּ", "Wär bisch du", ["Wie isch es gange"],
  "Di gliich Frag stellt de Boas i [[RUT.3.9]]. D Noomi fragt wohl, als was d Rut zruggchunnt."),
 ("RUT.3.17", "mit lääre Händ", "adapted", "רֵיקָם", "läär", None,
  "S gliich Wort wie i de Klag vo de Noomi [[RUT.1.21]]: «läär hät mich JHWH zruggbracht»."),
 # Kapitel 4
 ("RUT.4.1", "du Soundso", "interpretive", "פְּלֹנִי אַלְמֹנִי", "Peloni Almoni", ["min Fründ"],
  "Feschti Wändig für e Person, wo nöd gnännt wird. De Boas wird de Maa bim Name grüeft ha; de Erzähler verschwiigt en – vilicht, wil "
  "dä Löser de Name vom Verstorbne nöd wott erhalte ([[RUT.4.6]])."),
 ("RUT.4.3", "verchauft", "interpretive", "מָכְרָה", None, ["hät verchauft", "wott verchaufe"],
  "D Vergangeheitsform cha en gfasste Entschluss usdrucke. Wie d Noomi zu dem Fäld cho isch und öb s scho verchauft isch, seit de Text nöd."),
 ("RUT.4.3", "öisem Brueder", "literal", "לְאָחִינוּ", None, ["öisem Verwandte"], "«Brueder» meint da en Verwandte."),
 ("RUT.4.4", "ich legs dir offe", "adapted", "אֶגְלֶה אָזְנְךָ", "ich wott dis Oor ufdecke", None, "Wändig für «öpperem öppis mitteile»."),
 ("RUT.4.4", "wänn er nöd löse wott", "literal", "יִגְאַל", None, ["wänn du nöd löse wottsch"],
  "De masoretisch Text hät di 3. Person; vilicht wändet sich de Boas churz a d Ältischte. Vili Handschrifte und alti Übersetzige händ di "
  "2. Person (i de Date nöd erfasst)."),
 ("RUT.4.5", "erwirbsch du", "interpretive", "קָנִיתָה", "häsch du erworbe", ["erwirbsch du au d Rut", "erwirb ich (Ketiv)"],
  "Schlüsselstell. D Tokens folged em Qere «du erwirbsch» (i MACULA als Qere markiert); s gschribnig Ketiv list me als «ich erwirb» – "
  "dänn chündet de Boas aa, er sälber wärd d Rut hürate. Oft änderet me zuedem «und vo de Rut» in «au d Rut» (vgl. [[RUT.4.10]]); das "
  "isch e Konjektur. D Verbindig vo Landchauf und Hochzig erinneret a d Schwageree ([[DEU.25.5]]), isch dört aber nöd so gregt. Übersetzt "
  "isch de überliferet Qere-Text; kei Läsart isch als richtig entschide."),
 ("RUT.4.6", "schädig ich mis eige Erbteil", "interpretive", "אַשְׁחִית", "verdirb ich", None,
  "Vermuetlich, wil en Sohn mit de Rut als Erb vom Machlon gälte würd und s Fäld dänn nöd bim Löser bliib. De Text seit de Grund nöd."),
 ("RUT.4.7", "Schue", "literal", "נַעֲלוֹ", None, ["Sandale"],
  "De Erzähler erklärt en alte Bruuch. I [[DEU.25.9]] wird em Schwager, wo nöd wott, de Schue zur Schand abzoge; da bsieglet er e Übertragig."),
 ("RUT.4.11", "bring es zu Vermöge", "interpretive", "עֲשֵׂה חַיִל", "tue Chraft", ["wird mächtig", "überchum Nachkomme"],
  "Wider חַיִל wie i [[RUT.2.1]] und [[RUT.3.11]]; gmeint chönd Wohlstand, Aasee oder vili Chind sii."),
 ("RUT.4.11", "mach dir en Name", "interpretive", "קְרָא שֵׁם", "rüef en Name", ["wird berüemt"],
  "Di gnau Bedüütig vo de Wändig isch unsicher."),
 ("RUT.4.12", "Tamar", "literal", "תָמָר", None, None,
  "Vgl. [[GEN.38.29]]: Au d Tamar hät mit ungwöönlichem Handle de Familie vo Juda Nachkomme gsicheret."),
 ("RUT.4.14", "söll bekannt wärde", "interpretive", "יִקָּרֵא", "söll grüeft wärde", ["söll grüemt wärde"],
  "Unklar isch, öb de Name vom Löser (vom Chind) oder vo JHWH gmeint isch."),
 ("RUT.4.15", "s Läbe", "interpretive", "מֵשִׁיב נֶפֶשׁ", "eine, wo d Seel zruggbringt", None,
  "«Zruggbringe» (שׁוּב) nimmt d Klag vo de Noomi uf: «läär hät mich JHWH zruggbracht» ([[RUT.1.21]])."),
 ("RUT.4.16", "Pflegeri", "literal", "לְאֹמֶנֶת", None, ["Amme"], "Öb d Geschte e Adoption usdruckt, isch umstritte."),
 ("RUT.4.18", "Stammbaum", "adapted", "תּוֹלְדוֹת", "Zeugige", None,
  "D Formle kännt me us em Buech Genesis (z. B. [[GEN.5.1]]). D Lischte nännt zää Generatione vom Perez bis zum David; de Boas staat a "
  "de sibete Stell."),
 ("RUT.4.18", "isch de Vatter", "adapted", "הוֹלִיד", "hät zeugt", None,
  "Im Hebräische staat «er hät zeugt»; uf Züritüütsch seit me ehner «er isch de Vatter gsii». Gliich i de folgende Vers."),
 ("RUT.4.20", "Salma", "literal", "שַׂלְמָה", None, ["Salmon"],
  "I [[RUT.4.21]] heisst de gliich Maa שַׂלְמוֹן (Salmon); beidi Schriibige sind biibhalte."),
]

UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung)
 ("TU-RUT-001-001-022", "RUT.1.1-RUT.1.22", "narrative", "Leer zurück aus Moab",
  ["TU-RUT-001-001-005", "TU-RUT-001-006-018", "TU-RUT-001-019-022"],
  "In einer Hungersnot zieht eine Familie aus Betlehem nach Moab. Noomi verliert Mann und Söhne und kehrt zurück. Ihre moabitische "
  "Schwiegertochter Rut lässt sich nicht abweisen und geht mit ihr; in Betlehem nennt sich Noomi «Mara», die Bittere."),
 ("TU-RUT-001-001-005", "RUT.1.1-RUT.1.5", "narrative", "Hungersnot und Tod in Moab", None,
  "Wegen einer Hungersnot zieht Elimelech mit Noomi und den Söhnen nach Moab. Elimelech stirbt; die Söhne heiraten Moabiterinnen und sterben nach etwa zehn Jahren ebenfalls. Noomi bleibt ohne Mann und Kinder zurück."),
 ("TU-RUT-001-006-018", "RUT.1.6-RUT.1.18", "narrative", "Wohin du gehst", None,
  "Noomi will ihre Schwiegertöchter nach Hause schicken. Orpa kehrt um, Rut aber bindet sich mit einem Schwur an Noomi, ihr Volk und ihren Gott."),
 ("TU-RUT-001-019-022", "RUT.1.19-RUT.1.22", "narrative", "Nennt mich Mara", None,
  "In Betlehem klagt Noomi, JHWH habe sie leer zurückgebracht. Die Ankunft fällt in den Beginn der Gerstenernte."),
 ("TU-RUT-002-001-023", "RUT.2.1-RUT.2.23", "narrative", "Auf dem Feld des Boas",
  ["TU-RUT-002-001-003", "TU-RUT-002-004-017", "TU-RUT-002-018-023"],
  "Rut liest Ähren auf und kommt auf das Feld des Boas, eines Verwandten Elimelechs. Boas behandelt die Fremde mit auffallender "
  "Grosszügigkeit; Noomi erkennt in ihm einen Löser der Familie."),
 ("TU-RUT-002-001-003", "RUT.2.1-RUT.2.3", "narrative", "Rut geht Ähren lesen", None,
  "Der Erzähler stellt Boas vor. Rut bittet, Ähren auflesen zu dürfen, und kommt «zufällig» auf sein Feldstück."),
 ("TU-RUT-002-004-017", "RUT.2.4-RUT.2.17", "dialogue", "Unter den Flügeln JHWHs", None,
  "Boas erkundigt sich nach Rut, gewährt ihr Schutz, Wasser und Brot und wünscht ihr Lohn für das, was sie an Noomi getan hat – von JHWH, "
  "dem Gott Israels, unter dessen Flügeln sie Zuflucht sucht. Am Abend hat sie ein Efa Gerste."),
 ("TU-RUT-002-018-023", "RUT.2.18-RUT.2.23", "narrative", "Einer unserer Löser", None,
  "Noomi hört den Namen Boas, wünscht ihm den Segen JHWHs und sagt, er sei einer ihrer Löser. Rut bleibt bis zum Ende der Ernte bei den Arbeiterinnen des Boas."),
 ("TU-RUT-003-001-018", "RUT.3.1-RUT.3.18", "narrative", "Nachts auf der Tenne",
  ["TU-RUT-003-001-005", "TU-RUT-003-006-015", "TU-RUT-003-016-018"],
  "Noomi schickt Rut nachts zu Boas auf die Tenne. Rut bittet ihn, als Löser seinen Gewandzipfel über sie zu breiten. Boas sagt zu, "
  "verweist aber auf einen näheren Löser."),
 ("TU-RUT-003-001-005", "RUT.3.1-RUT.3.5", "dialogue", "Noomis Plan", None,
  "Noomi will für Rut einen Ort der Ruhe suchen und gibt ihr genaue Anweisungen für die Nacht auf der Tenne."),
 ("TU-RUT-003-006-015", "RUT.3.6-RUT.3.15", "narrative", "Breite deinen Gewandzipfel über mich", None,
  "Rut legt sich zu Boas' Füssen und bittet ihn, als Löser den Zipfel seines Gewandes über sie zu breiten. Boas lobt ihre Treue, sagt die Lösung unter Vorbehalt zu und "
  "schickt sie vor Tagesanbruch mit Gerste zurück."),
 ("TU-RUT-003-016-018", "RUT.3.16-RUT.3.18", "dialogue", "Warte ab, meine Tochter", None,
  "Rut berichtet Noomi. Diese ist sicher, dass Boas die Sache noch am selben Tag zu Ende bringt."),
 ("TU-RUT-004-001-022", "RUT.4.1-RUT.4.22", "narrative", "Ein Löser für Noomi",
  ["TU-RUT-004-001-012", "TU-RUT-004-013-017", "TU-RUT-004-018-022"],
  "Im Tor verzichtet der nähere Löser auf Feld und Heirat. Boas erwirbt beides vor Zeugen und heiratet Rut. Rut gebiert Obed, den die Frauen "
  "Noomis Löser nennen; ein Stammbaum führt bis zu David."),
 ("TU-RUT-004-001-012", "RUT.4.1-RUT.4.12", "narrative", "Verhandlung im Tor", None,
  "Vor zehn Ältesten bietet Boas dem näheren Löser Noomis Feld an. Als dazu die Ehe mit Rut gehört, tritt dieser zurück. Boas erwirbt "
  "alles vor Zeugen; das Volk segnet ihn und Rut."),
 ("TU-RUT-004-013-017", "RUT.4.13-RUT.4.17", "narrative", "Noomi ist ein Sohn geboren", None,
  "JHWH lässt Rut schwanger werden, und sie gebiert einen Sohn. Die Frauen preisen JHWH, der Noomi einen Löser geschenkt hat; Noomi nimmt das Kind auf den Schoss, und die Nachbarinnen nennen es Obed, den Grossvater Davids."),
 ("TU-RUT-004-018-022", "RUT.4.18-RUT.4.22", "genealogy", "Von Perez bis David", None,
  "Ein Stammbaum in zehn Gliedern verbindet Perez, den Sohn Judas und Tamars, über Boas und Obed mit David."),
]
UNITS_GSW = {
 "TU-RUT-001-001-022": ("Läär zrugg us Moab", "I nere Hungersnot zieht e Familie vo Betlehem uf Moab. D Noomi verliert Maa und Söön und chunnt zrugg. Iri moabitisch Schwigertochter Rut laat sich nöd abwiise und gaat mit ere; z Betlehem nännt sich d Noomi «Mara», di Bitter."),
 "TU-RUT-001-001-005": ("Hungersnot und Tod z Moab", "Wäg ere Hungersnot zieht de Elimelech mit de Noomi und de Söön uf Moab. De Elimelech stirbt; d Söön hürated Moabiterinne und sterbed öppe zää Jahr spöter au. D Noomi bliibt ohni Maa und Chind zrugg."),
 "TU-RUT-001-006-018": ("Wo du anegaasch", "D Noomi wott iri Schwigertöchtere heischicke. D Orpa cheert um, d Rut aber bindet sich mit eme Schwuer a d Noomi, ires Volk und ire Gott."),
 "TU-RUT-001-019-022": ("Säged mir Mara", "Z Betlehem chlagt d Noomi, JHWH heig si läär zruggbracht. Si chömed am Aafang vo de Gerschteernt aa."),
 "TU-RUT-002-001-023": ("Uf em Fäld vom Boas", "D Rut list Ääre uf und chunnt uf s Fäld vom Boas, eme Verwandte vom Elimelech. De Boas behandlet di Frömd uffallend grosszügig; d Noomi erchännt in im en Löser vo de Familie."),
 "TU-RUT-002-001-003": ("D Rut gaat go Ääre läse", "De Erzähler stellt de Boas vor. D Rut fragt, öb si dörf Ääre ufläse, und chunnt «zuefällig» uf sis Fäldstück."),
 "TU-RUT-002-004-017": ("Under de Flügel vo JHWH", "De Boas fragt nach de Rut, git ire Schutz, Wasser und Broot und wünscht ere Lohn für das, wo si a de Noomi gmacht hät – vo JHWH, em Gott vo Israel, under dem sine Flügel si Schutz suecht. Am Aabig hät si es Efa Gerschte."),
 "TU-RUT-002-018-023": ("Eine vo öisne Löser", "D Noomi ghört de Name Boas, wünscht im de Säge vo JHWH und seit, er sig eine vo irne Löser. D Rut bliibt bis am Änd vo de Ernt bi de Arbeiterinne vom Boas."),
 "TU-RUT-003-001-018": ("Znacht uf de Tänn", "D Noomi schickt d Rut znacht zum Boas uf d Tänn. D Rut bittet en, als Löser de Zipfel vo sim Gwand über si z spreite. De Boas seit zue, verwiist aber uf en nööchere Löser."),
 "TU-RUT-003-001-005": ("De Plan vo de Noomi", "D Noomi wott für d Rut es Daheim sueche und git ire gnaui Aawiisige für d Nacht uf de Tänn."),
 "TU-RUT-003-006-015": ("Spreit de Zipfel vo dim Gwand über mich", "D Rut leit sich zu de Füess vom Boas und bittet en, als Löser de Zipfel vo sim Gwand über si z spreite. De Boas lobt iri Tröii, seit d Lösig under Vorbehalt zue und schickt si vor em Taag mit Gerschte zrugg."),
 "TU-RUT-003-016-018": ("Wart ab, mini Tochter", "D Rut verzellt s de Noomi. Die isch sicher, dass de Boas d Sach no am gliiche Taag erlediget."),
 "TU-RUT-004-001-022": ("En Löser für d Noomi", "Im Tor verzichtet de nööcher Löser uf Fäld und Hochzig. De Boas erwirbt beides vor Züüge und hüratet d Rut. D Rut überchunnt de Obed, und d Fraue nänned en de Löser vo de Noomi; en Stammbaum füert bis zum David."),
 "TU-RUT-004-001-012": ("Verhandlig im Tor", "Vor zää Ältischte bietet de Boas em nööchere Löser s Fäld vo de Noomi aa. Wo d Ee mit de Rut dezue ghört, tritt dä zrugg. De Boas erwirbt alles vor Züüge; s Volk sägnet in und d Rut."),
 "TU-RUT-004-013-017": ("De Noomi isch en Sohn gebore", "JHWH laat d Rut schwanger wärde, und si überchunnt en Sohn. D Fraue lobed JHWH, wo de Noomi en Löser gschänkt hät; d Noomi nimmt s Chind uf de Schoss, und d Nachberinne nänned s Obed, de Grossvatter vom David."),
 "TU-RUT-004-018-022": ("Vom Perez bis zum David", "En Stammbaum mit zää Glider verbindet de Perez, de Sohn vom Juda und de Tamar, über de Boas und de Obed mit em David."),
}


def qere_refs(c):
    """Verse, in denen MACULA Qere-Formen markiert (Umschrift mit «**»)."""
    ann = json.loads((D / "annotations" / f"MACULA-WLC-RUT-{c:03d}.json").read_text(encoding="utf-8"))["entries"]
    refs = set()
    for tid, e in ann.items():
        if str(e.get("transliteration", "")).startswith("**"):
            _, _, _, ch, v, _ = tid.split("-")
            refs.add((int(ch), int(v)))
    return [f"RUT.{ch}.{v}" for ch, v in sorted(refs)]


def run():
    n = write(D / "works" / "WORK-RUT.json", {"id": "WORK-RUT", "type": "work", "status": "draft", "tags": TAGS,
                                             "name": "Rut", "original_language": "he"})
    for uid, rng, kind, title, parts, summary in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-RUT", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}),
               **({"segmentation_note_de": "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."} if parts else {}),
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-13; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    for c, last in ((1, 22), (2, 23), (3, 18), (4, 22)):
        ts_id, toks = load_tokens(D / "tokens" / f"WLC-RUT-{c:03d}.json")
        refs_c = [f"RUT.{c}.{v}" for v in range(1, last + 1)]
        qr = qere_refs(c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-RUT-{c:03d}-001-{last:03d}-{code}-WORKING"
            dec = [{"reference": r, "target": tg, "kind": kd, "heb": heb, **({"more_literal": ml} if ml else {}),
                    **({"other_options": oo} if oo else {}), "note": nt}
                   for r, tg, kd, heb, ml, oo, nt in decs if r in refs_c]
            for d in dec:
                if d["target"] not in texts[d["reference"]]:
                    raise SystemExit(f"{tid}: Entscheidung {d['target']!r} nicht im Text {d['reference']}")
            marks = ", ".join(f"[[{r}]]" for r in qr)
            if lang == "de":
                notes = [AUTH + " Die Übersetzung ist nicht von Fachleuten geprüft.",
                         "Für das Buch Rut ist noch kein freier textkritischer Apparat erfasst: Qumran-Fragmente, Septuaginta und andere alte "
                         "Übersetzungen sind nicht in den Daten. Wo Entscheidungen alte Übersetzungen erwähnen, beruht das auf allgemeinem "
                         "Wissen und ist nicht an Daten geprüft."]
                if qr:
                    notes.append(f"Ketiv/Qere: In {marks} markiert MACULA Qere-Formen (gelesene statt geschriebene Form). Die Übersetzung "
                                 "folgt diesen Formen; die geschriebenen Ketiv-Formen sind in den Daten nicht enthalten.")
            else:
                notes = [AUTH_GSW + " D Übersetzig isch nöd vo Fachlüüt prüeft.",
                         "Für s Buech Rut isch no kein freie textkritische Apparat erfasst: Qumran-Fragmänt, Septuaginta und anderi alti "
                         "Übersetzige sind nöd i de Date. Wo Entscheidige alti Übersetzige erwääned, beruet das uf allgemeinem Wüsse und isch "
                         "nöd a Date prüeft."]
                if qr:
                    notes.append(f"Ketiv/Qere: I {marks} markiert MACULA Qere-Forme (gläseni statt gschribni Form). D Übersetzig folgt dene "
                                 "Forme; di gschribne Ketiv-Forme sind i de Date nöd enthalte.")
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"RUT.{c}.1-RUT.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
                            "register_de": "Nah am hebräischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Personennamen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-RUT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem hebräischen Text (Westminster Leningrad Codex, Morpheme nach MACULA Hebrew): Satzbau und Bilder des Hebräischen möglichst sichtbar, verständliches Deutsch. Der Gottesname steht als JHWH. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
                                       if lang == "de" else "Direkt aus dem hebräischen Text (WLC) übersetzt, mit Wortzuordnung zu den Morphemen; die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle. Der Gottesname steht als JHWH. Nicht aus einer veröffentlichten Mundart-Bibel übernommen."),
                        "based_on_edition": "ED-WLC", "based_on_tokens": ts_id, "text_by_reference": texts,
                        "translation_notes": notes,
                        "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                        "decisions": dec,
                        "decisions_note_de": "Übersetzungsentscheidungen: wörtlich (literal), sprachlich angepasst (adapted), Deutungsentscheidung (interpretive) oder der vertrauten Wiedergabe folgend (traditional). " + (AUTH if lang == "de" else AUTH_GSW)})
            n += write(D / "translations" / f"{tid}.json", rec)
            aid = f"ALIGN-RUT-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"RUT.{c}.1-RUT.{c}.{last}",
                "source_language": "he", "target_language": rec["language"], "source_basis": "ED-WLC", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} Morphem-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/ruth_text.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Rut – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
