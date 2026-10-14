#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 18–19 (Passion: Gefangennahme, Verhöre, Kreuzigung, Begräbnis) – Texteinheiten,
Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und
vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_18_19.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben. Die Grundentscheide zur Wiedergabe der
johanneischen Schlüsselwörter und von οἱ Ἰουδαῖοι stehen in scripts/authoring/johannes_text_01_03.py; hier gelten sie
unverändert. In Johannes 18–19 fehlt im SBLGNT kein Vers.

KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1)
bzw. aus der CNTR-Transkription (Sekundärtranskription), nicht aus eigener Prüfung der Handschriften.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, localize, write  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
AUTH_GSW_L10N = "KI-Entwurf (Claude) vom 2026-10-14; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft."
TAGS = ["TAG-JOHN"]
CHAPTERS = ((18, 40), (19, 42))

DE = {
 # ------------------------------------------------------------ Kapitel 18
 "JHN.18.1": "[Nachdem]{2} [Jesus]{3} [das]{1} [gesagt hatte]{2}, [ging er]{4} [mit]{5} [seinen]{6,8} [Jüngern]{7} [hinaus]{4} [auf die andere Seite]{9} [des Baches]{10,11} [Kidron]{12,13}; [dort]{14} [war]{15} [ein Garten]{16}, [in]{17} [den]{18} [er]{20} und{21} [seine]{22,24} [Jünger]{23} [hineingingen]{19}.",
 "JHN.18.2": "[Aber]{2} [auch]{3} [Judas]{4}, [der]{5} [ihn]{7} [auslieferte]{6}, [kannte]{1} [den]{8} [Ort]{9}, [denn]{10} [Jesus]{13} [war]{12} [oft]{11} [dort]{14} [mit]{15} [seinen]{16,18} [Jüngern]{17} [zusammengekommen]{12}.",
 "JHN.18.3": "[Judas]{1,3} [nun]{2} [nahm]{4} [die]{5} [Kohorte]{6} und{7} [Diener]{15} [von]{8} [den Hohepriestern]{9,10} und{11} [von]{12} [den Pharisäern]{13,14} [mit]{4} und [kommt]{16} [dorthin]{17} [mit]{18} [Laternen]{19} und{20} [Fackeln]{21} und{22} [Waffen]{23}.",
 "JHN.18.4": "[Jesus]{1} [nun]{2}, [der]{3} [alles]{4} [wusste]{3}, [was]{5} [auf]{7} [ihn]{8} [zukam]{6}, [ging hinaus]{9} und{10} [sagt]{11} [zu ihnen]{12}: «[Wen]{13} [sucht ihr]{14}?»",
 "JHN.18.5": "[Sie antworteten]{1} [ihm]{2}: «[Jesus]{3}, [den Nazoräer]{4,5}.» [Er sagt]{6} [zu ihnen]{7}: «[Ich]{8} [bin es]{9}.» [Es stand]{10} [aber]{11} [auch]{12} [Judas]{13}, [der]{14} [ihn]{16} [auslieferte]{15}, [bei]{17} [ihnen]{18}.",
 "JHN.18.6": "[Als]{1} [er]{3} [nun]{2} [zu ihnen]{4} [sagte]{3}: «[Ich]{5} [bin es]{6}», [wichen sie]{7} [zurück]{8-10} und{11} [fielen]{12} [zu Boden]{13}.",
 "JHN.18.7": "[Da]{2} [fragte er]{3} [sie]{4} [wieder]{1}: «[Wen]{5} [sucht ihr]{6}?» [Sie]{7} [aber]{8} [sagten]{9}: «[Jesus]{10}, [den Nazoräer]{11,12}.»",
 "JHN.18.8": "[Jesus]{2} [antwortete]{1}: «[Ich habe]{3} [euch]{4} [gesagt]{3}, [dass]{5} [ich]{6} [es bin]{7}. [Wenn]{8} [ihr]{11} [also]{9} [mich]{10} [sucht]{11}, dann [lasst]{12} [diese]{13} [gehen]{14}!»",
 "JHN.18.9": "[So]{1} [sollte]{2} [das]{3} [Wort]{4} [erfüllt werden]{2}, [das]{5} [er gesagt hatte]{6}: «[Von]{13} [denen]{14}, [die]{8} [du]{9} [mir]{10} [gegeben hast]{9}, [habe ich]{12} [keinen]{11,15} [verloren]{12}.» ~7(ὅτι leitet die direkte Rede ein)",
 "JHN.18.10": "[Simon]{1} [Petrus]{3} [nun]{2}, [der]{4} [ein Schwert]{5} [hatte]{4}, [zog]{6} [es]{7} und{8} [schlug]{9} [den]{10} [Knecht]{13} [des Hohepriesters]{11,12} und{14} [hieb]{15} [ihm]{16} [das]{17} [rechte]{19,20} [Ohr]{18} [ab]{15}. [Der Name]{23} [des Knechtes]{24,25} [aber]{22} [war]{21} [Malchus]{26}.",
 "JHN.18.11": "[Da]{2} [sagte]{1} [Jesus]{3,4} [zu Petrus]{5,6}: «[Steck]{7} [das]{8} [Schwert]{9} [in]{10} [die]{11} [Scheide]{12}! [Den Becher]{13,14}, [den]{15} [mir]{17} [der Vater]{18,19} [gegeben hat]{16}, [soll ich]{22} [ihn]{23} [etwa nicht]{20,21} [trinken]{22}?»",
 "JHN.18.12": "[Die Kohorte]{1,3} [nun]{2} und{4} [der Oberst]{5,6} und{7} [die Diener]{8,9} [der Juden]{10,11} [nahmen]{12} [Jesus]{13,14} [fest]{12} und{15} [fesselten]{16} [ihn]{17}",
 "JHN.18.13": "und{1} [führten]{2} ihn [zuerst]{5} [zu]{3} [Hannas]{4}; [er war]{6} [nämlich]{7} [der Schwiegervater]{8} [des Kajafas]{9,10}, [der]{11} [in]{14} [jenem]{16} [Jahr]{15} [Hohepriester]{13} [war]{12}.",
 "JHN.18.14": "[Kajafas]{3} [aber]{2} [war]{1} es, [der]{4} [den Juden]{6,7} [geraten hatte]{5}, [es sei besser]{9}, [dass]{8} [ein]{10} [Mensch]{11} [für]{13} [das]{14} [Volk]{15} [sterbe]{12}.",
 "JHN.18.15": "[Simon]{5} [Petrus]{6} [aber]{2} [folgte]{1} [Jesus]{3,4}, und{7} [ein anderer]{8} [Jünger]{9}. [Dieser]{13} [Jünger]{10,12} [aber]{11} [war]{14} [mit dem Hohepriester]{16,17} [bekannt]{15} und{18} [ging]{19} [mit]{19} [Jesus]{20,21} [hinein]{19} [in]{22} [den]{23} [Hof]{24} [des Hohepriesters]{25,26}.",
 "JHN.18.16": "[Petrus]{1,3} [aber]{2} [stand]{4} [draussen]{8} [an]{5} [der]{6} [Tür]{7}. [Da]{10} [ging]{9} [der andere]{13,14} [Jünger]{11,12}, [der]{15} [mit dem Hohepriester]{17,18} [bekannt]{16} war, [hinaus]{9} und{19} [sprach mit]{20} [der Türhüterin]{21,22} und{23} [führte]{24} [Petrus]{25,26} [hinein]{24}.",
 "JHN.18.17": "[Da]{2} [sagt]{1} [die Magd]{5,6}, [die Türhüterin]{7,8}, [zu Petrus]{3,4}: «[Bist]{15} [du]{11} [etwa]{9} [auch]{10} [einer]{12} [der Jünger]{13,14} [dieses]{18} [Menschen]{16,17}?» [Er]{20} [sagt]{19}: «[Ich bin es]{22} [nicht]{21}.»",
 "JHN.18.18": "[Die Knechte]{3,4} [aber]{2} und{5} [die Diener]{6,7} [standen]{1} da; [sie hatten]{9} [ein Kohlenfeuer]{8} [gemacht]{9}, [weil]{10} [es]{12} [kalt]{11} [war]{12}, und{13} [wärmten sich]{14}. [Aber]{16} [auch]{17} [Petrus]{18,19} [stand]{15,22} [bei]{20} [ihnen]{21} und{23} [wärmte sich]{24}.",
 "JHN.18.19": "[Der Hohepriester]{1,3} [nun]{2} [befragte]{4} [Jesus]{5,6} [über]{7} [seine]{8,10} [Jünger]{9} und{11} [über]{12} [seine]{13,15} [Lehre]{14}.",
 "JHN.18.20": "[Jesus]{3} [antwortete]{1} [ihm]{2}: «[Ich]{4} [habe]{6} [offen]{5} [zur]{7} [Welt]{8} [geredet]{6}; [ich]{9} [habe]{11} [immer]{10} [in]{12} [der Synagoge]{13} [gelehrt]{11} und{14} [im]{15,16} [Tempel]{17}, [wo]{18} [alle]{19} [Juden]{20,21} [zusammenkommen]{22}, und{23} [im]{24} [Verborgenen]{25} [habe ich]{26} [nichts]{27} [geredet]{26}.",
 "JHN.18.21": "[Was]{1} [fragst du]{3} [mich]{2}? [Frag]{4} [die]{5}, [die gehört haben]{6}, [was]{7} [ich]{8} [zu ihnen]{9} [geredet habe]{8}! [Siehe]{10}, [sie]{11} [wissen]{12}, [was]{13} [ich]{15} [gesagt habe]{14}.»",
 "JHN.18.22": "[Als er]{3} [das]{1} [aber]{2} [sagte]{4}, [gab]{9} [einer]{5} [der Diener]{7,8}, [der dabeistand]{6}, [Jesus]{11,12} [einen Schlag ins Gesicht]{10} [und sagte]{13}: «[So]{14} [antwortest du]{15} [dem Hohepriester]{16,17}?»",
 "JHN.18.23": "[Jesus]{3} [antwortete]{1} [ihm]{2}: «[Wenn]{4} [ich]{6} [unrecht]{5} [geredet habe]{6}, [so lege]{7} [über]{8} [das]{9} [Unrecht]{10} [Zeugnis ab]{7}; [wenn]{11} [aber]{12} [recht]{13}, [warum]{14} [schlägst du]{16} [mich]{15}?»",
 "JHN.18.24": "[Da]{2} [schickte]{1} [Hannas]{4,5} [ihn]{3} [gefesselt]{6} [zu]{7} [Kajafas]{8}, [dem Hohepriester]{9,10}.",
 "JHN.18.25": "[Simon]{3} [Petrus]{4} [aber]{2} [stand]{1,5} da und{6} [wärmte sich]{7}. [Da]{9} [sagten sie]{8} [zu ihm]{10}: «[Bist]{18} [du]{13} [etwa]{11} [auch]{12} [einer]{14} [seiner]{15,17} [Jünger]{16}?» [Er]{20} [leugnete]{19} und{21} [sagte]{22}: «[Ich bin es]{24} [nicht]{23}.»",
 "JHN.18.26": "[Es sagt]{1} [einer]{2} [von]{3} [den Knechten]{4,5} [des Hohepriesters]{6,7} – [er]{9} [war]{9} [ein Verwandter]{8} [dessen]{10}, dem [Petrus]{12} [das]{13} [Ohr]{14} [abgehauen hatte]{11} –: «[Habe]{18} [ich]{16} [dich]{17} [nicht]{15} [im]{19,20} [Garten]{21} [mit]{22} [ihm]{23} [gesehen]{18}?»",
 "JHN.18.27": "[Da]{2} [leugnete]{3} [Petrus]{4} [wieder]{1}, und{5} [sogleich]{6} [krähte]{8} [ein Hahn]{7}.",
 "JHN.18.28": "[Nun]{2} [führen sie]{1} [Jesus]{3,4} [von]{5} [Kajafas]{6,7} [ins]{8,9} [Prätorium]{10}. [Es war]{11} [aber]{12} [früh am Morgen]{13}. Und{14} [sie selbst]{15} [gingen]{17} [nicht]{16} [ins]{18,19} [Prätorium]{20} [hinein]{17}, [um]{21} [nicht]{22} [unrein zu werden]{23}, [sondern]{24} [das Passa]{26,27} [essen zu können]{25}.",
 "JHN.18.29": "[Da]{2} [kam]{1} [Pilatus]{3,4} [zu]{6} [ihnen]{7} [heraus]{5} und{8} [sagt]{9}: «[Was für eine]{10} [Anklage]{11} [bringt ihr]{12} [gegen]{13} [diesen]{14,16} [Menschen]{15} [vor]{12}?»",
 "JHN.18.30": "[Sie antworteten]{1} und{2} [sagten]{3} [zu ihm]{4}: «[Wenn]{5} [dieser]{8} [nicht]{6} [Böses]{9} [täte]{7,10}, [hätten wir]{12} [ihn]{15} [dir]{13} [nicht]{11} [ausgeliefert]{14}.»",
 "JHN.18.31": "[Da]{2} [sagte]{1} [Pilatus]{4,5} [zu ihnen]{3}: «[Nehmt]{6} [ihr]{8} [ihn]{7} und{9} [richtet]{14} [ihn]{15} [nach]{10} [eurem]{11,13} [Gesetz]{12}!» [Die Juden]{18,19} [sagten]{16} [zu ihm]{17}: «[Uns]{20} [ist es]{22} [nicht]{21} [erlaubt]{22}, [jemanden]{24} [zu töten]{23}.»",
 "JHN.18.32": "[So]{1} [sollte]{6} [das]{2} [Wort]{3} [Jesu]{4,5} [erfüllt werden]{6}, [das]{7} [er gesagt hatte]{8}, [um anzuzeigen]{9}, [welchen]{10} [Todes]{11} [er]{12} [sterben]{13} [würde]{12}.",
 "JHN.18.33": "[Da]{2} [ging]{1} [Pilatus]{7,8} [wieder]{3} [ins]{4,5} [Prätorium]{6} [hinein]{1} und{9} [rief]{10} [Jesus]{11,12} und{13} [sagte]{14} [zu ihm]{15}: «[Bist]{17} [du]{16} [der König]{18,19} [der Juden]{20,21}?»",
 "JHN.18.34": "[Jesus]{2} [antwortete]{1}: «[Sagst]{7} [du]{5} [das]{6} [von dir selbst aus]{3,4}, [oder]{8} [haben]{10} [dir]{11} [andere]{9} [von]{12} [mir]{13} [erzählt]{10}?»",
 "JHN.18.35": "[Pilatus]{2,3} [antwortete]{1}: «[Bin]{7} [ich]{5} [etwa]{4} [ein Jude]{6}? [Dein]{10,11} [Volk]{8,9} und{12} [die Hohepriester]{13,14} [haben]{15} [dich]{16} [mir]{17} [ausgeliefert]{15}. [Was]{18} [hast du getan]{19}?»",
 "JHN.18.36": "[Jesus]{2} [antwortete]{1}: «[Mein]{5,6} [Reich]{3,4} [ist]{8} [nicht]{7} [aus]{9} [dieser]{10,12} [Welt]{11}. [Wenn]{13} [mein]{21,22} [Reich]{19,20} [aus]{14} [dieser]{15,17} [Welt]{16} [wäre]{18}, [würden]{28} [meine]{25,26} [Diener]{23,24} [kämpfen]{27}, [damit]{29} [ich]{31} [nicht]{30} [den Juden]{32,33} [ausgeliefert würde]{31}. [Nun]{34} [aber]{35} [ist]{41} [mein]{38,39} [Reich]{36,37} [nicht]{40} [von hier]{42}.»",
 "JHN.18.37": "[Da]{2} [sagte]{1} [Pilatus]{4,5} [zu ihm]{3}: «[Also]{6} [bist]{8} [du]{9} [doch]{6} [ein König]{7}?» [Jesus]{11,12} [antwortete]{10}: «[Du]{13} [sagst]{14}, [dass]{15} [ich]{17} [ein König]{16} [bin]{17}. [Ich]{18} [bin]{21} [dazu]{19,20} [geboren]{21} und{22} [dazu]{23,24} [in]{26} [die]{27} [Welt]{28} [gekommen]{25}, [um]{29} [der]{31} [Wahrheit]{32} [Zeugnis zu geben]{30}. [Jeder]{33}, [der]{34} [aus]{36} [der]{37} [Wahrheit]{38} [ist]{35}, [hört]{39} [auf meine]{40,41} [Stimme]{42}.»",
 "JHN.18.38": "[Pilatus]{3,4} [sagt]{1} [zu ihm]{2}: «[Was]{5} [ist]{6} [Wahrheit]{7}?» Und{8} [als er]{10} [das]{9} [gesagt hatte]{10}, [ging er]{12} [wieder]{11} [hinaus]{12} [zu]{13} [den Juden]{14,15} und{16} [sagt]{17} [zu ihnen]{18}: «[Ich]{19} [finde]{21} [keine]{20} [Schuld]{24} [an]{22} [ihm]{23}.",
 "JHN.18.39": "[Es ist]{1} [aber]{2} [Brauch]{3} [bei euch]{4}, [dass]{5} [ich]{7} [euch]{8} [am]{9,10} [Passa]{11} [einen]{6} [freilasse]{7}. [Wollt ihr]{12} [also]{13}, [dass ich]{14} [euch]{15} [den König]{16,17} [der Juden]{18,19} [freilasse]{14}?»",
 "JHN.18.40": "[Da]{2} [schrien sie]{1} [wieder]{3}: «[Nicht]{5} [diesen]{6}, [sondern]{7} [Barabbas]{8,9}!» [Barabbas]{12,13} [aber]{11} [war]{10} [ein Räuber]{14}. ~4(λέγοντες «sagend» leitet die direkte Rede ein)",
 # ------------------------------------------------------------ Kapitel 19
 "JHN.19.1": "[Da]{1} [nun]{2} [nahm]{3} [Pilatus]{4,5} [Jesus]{6,7} und{8} [liess ihn geisseln]{9}.",
 "JHN.19.2": "Und{1} [die Soldaten]{2,3} [flochten]{4} [einen Kranz]{5} [aus]{6} [Dornen]{7} und [setzten]{8} ihn [ihm]{9} [auf]{8} [den]{10} [Kopf]{11}, und{12} [sie legten]{15} [ihm]{16} [einen purpurnen]{14} [Mantel]{13} [um]{15}.",
 "JHN.19.3": "Und{1} [sie traten]{2} [zu]{3} [ihm]{4} [hin]{2} und{5} [sagten]{6}: «[Sei gegrüsst]{7}, [König]{8,9} [der Juden]{10,11}!» Und{12} [sie gaben]{13} [ihm]{14} [Schläge ins Gesicht]{15}.",
 "JHN.19.4": "Und{1} [Pilatus]{5,6} [ging]{2} [wieder]{3} [hinaus]{4} und{7} [sagt]{8} [zu ihnen]{9}: «[Seht]{10}, [ich bringe]{11} [ihn]{13} [zu euch]{12} [heraus]{14}, [damit]{15} [ihr erkennt]{16}, [dass]{17} [ich]{20} [keine]{18} [Schuld]{19} [an]{21} [ihm]{22} [finde]{20}.»",
 "JHN.19.5": "[Da]{2} [kam]{1} [Jesus]{3,4} [heraus]{5}; [er trug]{6} [den]{7} [Dornenkranz]{8,9} und{10} [den]{11} [purpurnen]{12} [Mantel]{13}. Und{14} [er sagt]{15} [zu ihnen]{16}: «[Seht]{17}, [der Mensch]{18,19}!»",
 "JHN.19.6": "[Als]{1} [ihn]{4} [nun]{2} [die Hohepriester]{5,6} und{7} [die Diener]{8,9} [sahen]{3}, [schrien sie]{10}: «[Kreuzige]{12}, [kreuzige]{13}!» [Pilatus]{16,17} [sagt]{14} [zu ihnen]{15}: «[Nehmt]{18} [ihr]{20} [ihn]{19} und{21} [kreuzigt]{22} ihn! [Denn]{24} [ich]{23} [finde]{26} [keine]{25} [Schuld]{29} [an]{27} [ihm]{28}.» ~11(λέγοντες «sagend» leitet die direkte Rede ein)",
 "JHN.19.7": "[Die Juden]{3,4} [antworteten]{1} [ihm]{2}: «[Wir]{5} [haben]{7} [ein Gesetz]{6}, und{8} [nach]{9} [dem]{10} [Gesetz]{11} [muss er]{12} [sterben]{13}, [weil]{14} [er]{18} [sich]{17} [zum Sohn]{15} [Gottes]{16} [gemacht hat]{18}.»",
 "JHN.19.8": "[Als]{1} [Pilatus]{4,5} [nun]{2} [dieses]{6,7} [Wort]{8} [hörte]{3}, [fürchtete er sich]{10} [noch mehr]{9}",
 "JHN.19.9": "und{1} [ging]{2} [wieder]{6} [ins]{3,4} [Prätorium]{5} [hinein]{2} und{7} [sagt]{8} [zu Jesus]{9,10}: «[Woher]{11} [bist]{12} [du]{13}?» [Jesus]{14,16} [aber]{15} [gab]{19} [ihm]{20} [keine]{18} [Antwort]{17}.",
 "JHN.19.10": "[Da]{2} [sagt]{1} [Pilatus]{4,5} [zu ihm]{3}: «[Mit mir]{6} [redest du]{8} [nicht]{7}? [Weisst du]{10} [nicht]{9}, [dass]{11} [ich]{13} [Vollmacht]{12} [habe]{13}, [dich]{15} [freizulassen]{14}, und{16} [Vollmacht]{17} [habe]{18}, [dich]{20} [zu kreuzigen]{19}?»",
 "JHN.19.11": "[Jesus]{3} [antwortete]{1} [ihm]{2}: «[Du hättest]{5} [keine]{4,9} [Vollmacht]{6} [über]{7} [mich]{8}, [wenn]{10} [es]{12} [dir]{14} [nicht]{11} [von oben]{15} [gegeben]{13} [wäre]{12}. [Darum]{16,17} [hat]{24} [der]{18}, der [mich]{20} [dir]{21} [ausgeliefert hat]{19}, [grössere]{22} [Sünde]{23}.»",
 "JHN.19.12": "[Daraufhin]{1,2} [suchte]{5} [Pilatus]{3,4} [ihn]{7} [freizulassen]{6}. [Die Juden]{8,10} [aber]{9} [schrien]{11}: «[Wenn]{13} [du]{15} [diesen]{14} [freilässt]{15}, [bist du]{17} [nicht]{16} [Freund]{18} [des Kaisers]{19,20}. [Jeder]{21}, [der]{22} [sich]{24} [zum König]{23} [macht]{25}, [stellt sich gegen]{26} [den Kaiser]{27,28}.» ~12(λέγοντες «sagend» leitet die direkte Rede ein)",
 "JHN.19.13": "[Als]{4} [Pilatus]{1,3} [nun]{2} [diese]{5,7} [Worte]{6} [hörte]{4}, [führte er]{8} [Jesus]{10,11} [hinaus]{9} und{12} [setzte sich]{13} [auf]{14} [den Richterstuhl]{15} [an]{16} [dem Ort]{17}, [der]{18} «[Steinpflaster]{19}» [heisst]{18}, [auf Hebräisch]{20} [aber]{21} «[Gabbata]{22}».",
 "JHN.19.14": "[Es war]{1} [aber]{2} [der Rüsttag]{3} [des Passa]{4,5}; [es war]{7} [um]{8} [die sechste]{9} [Stunde]{6}. Und{10} [er sagt]{11} [zu den Juden]{12,13}: «[Seht]{14}, [euer]{15,17} [König]{16}!»",
 "JHN.19.15": "[Da]{2} [schrien]{1} [jene]{3}: «[Weg]{4}, [weg]{5} mit ihm, [kreuzige]{6} [ihn]{7}!» [Pilatus]{10,11} [sagt]{8} [zu ihnen]{9}: «[Euren]{12,14} [König]{13} [soll ich kreuzigen]{15}?» [Die Hohepriester]{17,18} [antworteten]{16}: «[Wir haben]{20} [keinen]{19} [König]{21} [ausser]{22,23} [den Kaiser]{24}.»",
 "JHN.19.16": "[Da]{1} [nun]{2} [lieferte er]{3} [ihn]{4} [ihnen]{5} [aus]{3}, [damit]{6} [er gekreuzigt würde]{7}. [Sie übernahmen]{8} [nun]{9} [Jesus]{10,11}.",
 "JHN.19.17": "Und{1} [er trug]{2} [das]{4} [Kreuz]{5} [selbst]{3} und [ging hinaus]{6} [zur]{7,8} [sogenannten]{9} [Schädelstätte]{10,11}, [die]{12} [auf Hebräisch]{14} «[Golgota]{15}» [heisst]{13}.",
 "JHN.19.18": "[Dort]{1} [kreuzigten sie]{3} [ihn]{2} und{4} [mit]{5} [ihm]{6} [zwei]{8} [andere]{7}, [auf dieser]{9} und{10} [auf jener Seite]{11}, [Jesus]{14,15} [aber]{13} [in der Mitte]{12}.",
 "JHN.19.19": "[Pilatus]{5,6} [schrieb]{1} [aber]{2} [auch]{3} [eine Tafel]{4} und{7} [brachte sie]{8} [am]{9,10} [Kreuz]{11} [an]{8}. [Es war]{12} [aber]{13} [geschrieben]{14}: «[Jesus]{15}, [der Nazoräer]{16,17}, [der König]{18,19} [der Juden]{20,21}.»",
 "JHN.19.20": "[Diese]{1,3} [Tafel]{4} [nun]{2} [lasen]{6} [viele]{5} [der Juden]{7,8}, [denn]{9} [der Ort]{12,13}, [wo]{16} [Jesus]{18,19} [gekreuzigt wurde]{17}, [war]{11} [nahe]{10} [bei der]{14} [Stadt]{15}; und{20} [sie war]{21} [auf Hebräisch]{23}, [Lateinisch]{24} und [Griechisch]{25} [geschrieben]{22}.",
 "JHN.19.21": "[Da]{2} [sagten]{1} [die Hohepriester]{5,6} [der Juden]{7,8} [zu Pilatus]{3,4}: «[Schreib]{10} [nicht]{9}: ‹[Der König]{11,12} [der Juden]{13,14}›, [sondern]{15}: ‹[Er]{17} [hat gesagt]{18}: [Ich bin]{22} [König]{19} [der Juden]{20,21}.›» ~16(ὅτι leitet die wörtliche Wiedergabe ein)",
 "JHN.19.22": "[Pilatus]{2,3} [antwortete]{1}: «[Was]{4} [ich geschrieben habe]{5}, [habe ich geschrieben]{6}.»",
 "JHN.19.23": "[Die Soldaten]{1,3} [nun]{2}, [als]{4} [sie]{5} [Jesus]{6,7} [gekreuzigt hatten]{5}, [nahmen]{8} [seine]{9,11} [Kleider]{10} und{12} [machten]{13} [vier]{14} [Teile]{15}, [für jeden]{16} [Soldaten]{17} [einen Teil]{18}, und{19} dazu [das]{20} [Untergewand]{21}. [Das]{24} [Untergewand]{25} [aber]{23} [war]{22} [ohne Naht]{26}, [von oben an]{27-29} [in einem Stück]{31,32} [gewebt]{30}.",
 "JHN.19.24": "[Da]{2} [sagten sie]{1} [zueinander]{3,4}: «[Lasst]{6} [es]{7} [uns]{6} [nicht]{5} [zerreissen]{6}, [sondern]{8} [darum]{10,11} [losen]{9}, [wem]{12} [es gehören soll]{13}.» [So]{14} [sollte]{17} [die]{15} [Schrift]{16} [erfüllt werden]{17}, [die]{18} [sagt]{19}: «[Sie haben]{20} [meine]{21,23} [Kleider]{22} [unter sich]{24} [verteilt]{20}, und{25} [über]{26} [mein]{27,29} [Gewand]{28} [haben sie]{30} [das Los]{31} [geworfen]{30}.» [Das]{36} [taten]{37} [also]{34} [die Soldaten]{32,35}. ~33(μέν ohne ausdrückliches Gegenstück; nicht eigens wiedergegeben)",
 "JHN.19.25": "[Es standen]{1} [aber]{2} [beim]{3,4} [Kreuz]{5} [Jesu]{6,7} [seine]{8,10} [Mutter]{9} und{11} [die Schwester]{12,13} [seiner]{14,16} [Mutter]{15}, [Maria]{17}, [die Frau]{18} [des Klopas]{19,20}, und{21} [Maria]{22} [aus Magdala]{23,24}.",
 "JHN.19.26": "[Als]{3} [Jesus]{1} [nun]{2} [seine]{4} [Mutter]{5} [sah]{3} und{6} [den]{7} [Jünger]{8}, [den]{10} [er liebte]{11}, [dabeistehen]{9}, [sagt er]{12} [zu seiner]{13} [Mutter]{14}: «[Frau]{15}, [siehe]{16}, [dein]{17,19} [Sohn]{18}!»",
 "JHN.19.27": "[Dann]{1} [sagt er]{2} [zum]{3} [Jünger]{4}: «[Siehe]{5}, [deine]{6,8} [Mutter]{7}!» Und{9} [von]{10} [jener]{11,12} [Stunde]{13} [an]{10} [nahm]{14} [der Jünger]{15,16} [sie]{17} [zu sich]{18-20}.",
 "JHN.19.28": "[Danach]{1,2}, [da]{3} [Jesus]{4,5} [wusste]{3}, [dass]{6} [schon]{7} [alles]{8} [vollbracht ist]{9}, [sagt er]{14}, [damit]{10} [die]{12} [Schrift]{13} [vollendet würde]{11}: «[Mich dürstet]{15}.»",
 "JHN.19.29": "[Ein Gefäss]{1} [voll]{4} [Essig]{3} [stand]{2} da. [Sie steckten]{11} [nun]{6} [einen Schwamm]{5} [voll]{7} [mit dem]{8} [Essig]{9} [auf einen Ysopzweig]{10} und [hielten ihn]{12} [ihm]{13} [an den]{14} [Mund]{15}.",
 "JHN.19.30": "[Als]{1} [Jesus]{6,7} [nun]{2} [den]{4} [Essig]{5} [genommen hatte]{3}, [sagte er]{8}: «[Es ist vollbracht]{9}.» Und{10} [er neigte]{11} [das]{12} [Haupt]{13} und [übergab]{14} [den]{15} [Geist]{16}.",
 "JHN.19.31": "[Die Juden]{1,3} [nun]{2} – [weil]{4} [Rüsttag]{5} [war]{6}, [damit]{7} [die]{13} [Leiber]{14} [nicht]{8} [am]{15,16} [Sabbat]{17} [am]{10,11} [Kreuz]{12} [blieben]{9}; [denn]{19} [jener]{23,24} [Sabbat]{25} [war]{18} [ein grosser]{20} [Tag]{21,22} – [baten]{26} [Pilatus]{27,28}, [dass]{29} [ihnen]{31} [die]{32} [Beine]{33} [gebrochen]{30} und{34} sie [abgenommen würden]{35}.",
 "JHN.19.32": "[Da]{2} [kamen]{1} [die Soldaten]{3,4} und{5} [brachen]{9} [dem]{6} [ersten]{8} [die]{10} [Beine]{11} und{12} [dem]{13} [anderen]{14}, [der]{15} [mit ihm]{17} [gekreuzigt worden war]{16}. ~7(μέν ohne ausdrückliches Gegenstück; nicht eigens wiedergegeben)",
 "JHN.19.33": "[Bei]{1} [Jesus]{3,4} [aber]{2} [angekommen]{5}, [brachen sie]{12} [ihm]{13} [die]{14} [Beine]{15} [nicht]{11}, [als]{6} [sie sahen]{7}, [dass er]{9} [schon]{8} [tot war]{10}.",
 "JHN.19.34": "[Sondern]{1} [einer]{2} [der Soldaten]{3,4} [stiess]{9} [ihm]{6} [mit einer Lanze]{5} [in]{9} [die]{7} [Seite]{8}, und{10} [sogleich]{12} [kam]{11} [Blut]{13} und{14} [Wasser]{15} [heraus]{11}.",
 "JHN.19.35": "Und{1} [der]{2} [es gesehen hat]{3}, [hat es bezeugt]{4}, und{5} [sein]{7} [Zeugnis]{9,10} [ist]{8} [wahr]{6}; und{11} [jener]{12} [weiss]{13}, [dass]{14} [er]{16} [Wahres]{15} [sagt]{16}, [damit]{17} [auch]{18} [ihr]{19} [glaubt]{20}.",
 "JHN.19.36": "[Denn]{2} [das]{3} [geschah]{1}, [damit]{4} [die]{5} [Schrift]{6} [erfüllt würde]{7}: «[Kein]{9} [Knochen]{8} [von ihm]{11} [wird zerbrochen werden]{10}.»",
 "JHN.19.37": "Und{1} [wieder]{2} [sagt]{5} [eine andere]{3} [Schrift]{4}: «[Sie werden]{6} [auf]{7} [den]{8} [blicken]{6}, den [sie durchbohrt haben]{9}.»",
 "JHN.19.38": "[Danach]{1,3} [aber]{2} [bat]{4} [Josef]{7} [von]{8} [Arimatäa]{9}, [der]{10} [ein Jünger]{11} [Jesu]{12,13} [war]{10}, [aber]{15} [heimlich]{14} [aus]{16} [Furcht]{17,18} [vor den Juden]{19,20}, [Pilatus]{5,6}, [dass]{21} [er]{22} [den Leib]{23,24} [Jesu]{25,26} [abnehmen dürfe]{22}; und{27} [Pilatus]{29,30} [erlaubte es]{28}. [Da]{32} [kam er]{31} und{33} [nahm]{34} [seinen]{35,37} [Leib]{36} [ab]{34}.",
 "JHN.19.39": "[Es kam]{1} [aber]{2} [auch]{3} [Nikodemus]{4}, [der]{5} [das erste Mal]{10,11} [bei Nacht]{9} [zu]{7} [ihm]{8} [gekommen war]{6}; [er brachte]{12} [eine Mischung]{13} [aus Myrrhe]{14} und{15} [Aloe]{16}, [etwa]{17} [hundert]{19} [Pfund]{18}.",
 "JHN.19.40": "[Sie nahmen]{1} [nun]{2} [den Leib]{3,4} [Jesu]{5,6} und{7} [banden]{8} [ihn]{9} [mit]{11} [den Duftstoffen]{12,13} [in Leinenbinden]{10}, [wie]{14} es [bei den Juden]{17,18} [beim Begraben]{19} [Brauch]{15} [ist]{16}.",
 "JHN.19.41": "[Es war]{1} [aber]{2} [an]{3} [dem]{4} [Ort]{5}, [wo]{6} [er gekreuzigt worden war]{7}, [ein Garten]{8}, und{9} [in]{10} [dem]{11} [Garten]{12} [ein neues]{14} [Grab]{13}, [in]{15} [das]{16} [noch nie]{17} [jemand]{18} [gelegt worden war]{19,20}.",
 "JHN.19.42": "[Dort]{1} [nun]{2} [legten sie]{13} [Jesus]{14,15} [hin]{13}, [wegen]{3} [des]{4} [Rüsttags]{5} [der Juden]{6,7}, [weil]{8} [das]{11} [Grab]{12} [nahe]{9} [war]{10}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 18
 "JHN.18.1": "[Wo]{2} [de Jesus]{3} [das]{1} [gseit gha hät]{2}, [isch er]{4} [mit]{5} [sine]{6,8} [Jünger]{7} [use gange]{4}, [übere uf di ander Siite]{9} [vom Bach]{10,11} [Kidron]{12,13}; [dört]{14} [isch]{15} [en Garte]{16} [gsii]{15}, [wo]{18} [er]{20} und{21} [sini]{22,24} [Jünger]{23} [ine]{17} [gange sind]{19}.",
 "JHN.18.2": "[De Judas]{4}, [wo]{5} [en]{7} [usgliferet hät]{6}, [hät]{1} [de]{8} [Ort]{9} [aber]{2} [au]{3} [kännt]{1}, [wil]{10} [de Jesus]{13} [oft]{11} [mit]{15} [sine]{16,18} [Jünger]{17} [dört]{14} [zämechoo isch]{12}.",
 "JHN.18.3": "[De Judas]{1,3} [hät]{4} [also]{2} [d]{5} [Kohorte]{6} [mitgnoo]{4} und{7} [Diener]{15} [vo]{8} [de Hoheprieschter]{9,10} und{11} [vo]{12} [de Pharisäer]{13,14}, und [chunnt]{16} [mit]{18} [Latärne]{19} und{20} [Fackle]{21} und{22} [Waffe]{23} [dört häre]{17}.",
 "JHN.18.4": "[De Jesus]{1} [hät]{3} [also]{2} [alles]{4} [gwüsst]{3}, [was]{5} [uf]{7} [en]{8} [zuechunnt]{6}; [er isch usegange]{9} und{10} [seit]{11} [zu ine]{12}: «[Wän]{13} [sueched ir]{14}?»",
 "JHN.18.5": "[Si händ]{1} [em]{2} [gantwortet]{1}: «[De Jesus]{3}, [de Nazoräer]{4,5}.» [Er seit]{6} [zu ine]{7}: «[Ich]{8} [bi s]{9}.» [Bi]{17} [ine]{18} [isch]{10} [aber]{11} [au]{12} [de Judas]{13} [gstande]{10}, [wo]{14} [en]{16} [usgliferet hät]{15}.",
 "JHN.18.6": "[Wo]{1} [er]{3} [also]{2} [zu ine]{4} [gseit hät]{3}: «[Ich]{5} [bi s]{6}», [sind si]{7} [zrugg]{8-10} [gwiche]{7} und{11} [sind]{12} [a Bode]{13} [gfalle]{12}.",
 "JHN.18.7": "[Da]{2} [hät er]{3} [si]{4} [nomal]{1} [gfröget]{3}: «[Wän]{5} [sueched ir]{6}?» [Si]{7} [aber]{8} [händ gseit]{9}: «[De Jesus]{10}, [de Nazoräer]{11,12}.»",
 "JHN.18.8": "[De Jesus]{2} [hät gantwortet]{1}: «[Ich han]{3} [eu]{4} [gseit]{3}, [dass]{5} [ich]{6} [es bi]{7}. [Wänn]{8} [ir]{11} [also]{9} [mich]{10} [sueched]{11}, dänn [lönd]{12} [die]{13} [gaa]{14}!»",
 "JHN.18.9": "[Eso]{1} [hät sich]{2} [s]{3} [Wort]{4} [söle erfülle]{2}, [wo]{5} [er gseit hät]{6}: «[Vo]{13} [dene]{14}, [wo]{8} [du]{9} [mir]{10} [gää häsch]{9}, [han ich]{12} [keine]{11,15} [verlore]{12}.» ~7(ὅτι leitet di diräkt Red ii)",
 "JHN.18.10": "[De Simon]{1} [Petrus]{3} [hät]{4} [also]{2} [es Schwärt]{5} [gha]{4}; [er hät]{6} [s]{7} [zoge]{6} und{8} [hät]{9} [de]{10} [Chnächt]{13} [vom Hoheprieschter]{11,12} [troffe]{9} und{14} [hät]{15} [em]{16} [s]{17} [rächt]{19,20} [Oor]{18} [abghaue]{15}. [De Name]{23} [vom Chnächt]{24,25} [isch]{21} [aber]{22} [Malchus]{26} [gsii]{21}.",
 "JHN.18.11": "[Da]{2} [hät]{1} [de Jesus]{3,4} [zum Petrus]{5,6} [gseit]{1}: «[Steck]{7} [s]{8} [Schwärt]{9} [i]{10} [d]{11} [Scheide]{12}! [De Bächer]{13,14}, [wo]{15} [mir]{17} [de Vatter]{18,19} [gää hät]{16}, [sött ich]{22} [dä]{23} [öppe nöd]{20,21} [trinke]{22}?»",
 "JHN.18.12": "[D Kohorte]{1,3} [also]{2} und{4} [de Oberscht]{5,6} und{7} [d Diener]{8,9} [vo de Jude]{10,11} [händ]{12} [de Jesus]{13,14} [feschtgnoo]{12} und{15} [händ]{16} [en]{17} [gfesslet]{16}",
 "JHN.18.13": "und{1} [händ]{2} en [zerscht]{5} [zum]{3} [Hannas]{4} [gfüert]{2}; [er isch]{6} [nämli]{7} [de Schwiegervatter]{8} [vom Kajafas]{9,10} [gsii]{6}, [wo]{11} [i]{14} [säbem]{16} [Jahr]{15} [Hoheprieschter]{13} [gsii isch]{12}.",
 "JHN.18.14": "[De Kajafas]{3} [aber]{2} [isch]{1} dä [gsii]{1}, [wo]{4} [de Jude]{6,7} [graate hät]{5}, [es sig besser]{9}, [wänn]{8} [ein]{10} [Mänsch]{11} [für]{13} [s]{14} [Volk]{15} [stirbt]{12}.",
 "JHN.18.15": "[De Simon]{5} [Petrus]{6} [aber]{2} [isch]{1} [em Jesus]{3,4} [nachegange]{1}, und{7} [en andere]{8} [Jünger]{9}. [Dä]{10,13} [Jünger]{12} [aber]{11} [isch]{14} [mit em Hoheprieschter]{16,17} [bekannt]{15} [gsii]{14} und{18} [isch]{19} [mit]{19} [em Jesus]{20,21} [in]{22} [de]{23} [Hof]{24} [vom Hoheprieschter]{25,26} [ine gange]{19}.",
 "JHN.18.16": "[De Petrus]{1,3} [aber]{2} [isch]{4} [dusse]{8} [a]{5} [de]{6} [Tüür]{7} [gstande]{4}. [Da]{10} [isch]{9} [de ander]{13,14} [Jünger]{11,12}, [wo]{15} [mit em Hoheprieschter]{17,18} [bekannt]{16} gsii isch, [use choo]{9} und{19} [hät]{20} [mit de Tüürhüeteri]{21,22} [gredt]{20} und{23} [hät]{24} [de Petrus]{25,26} [ine gfüert]{24}.",
 "JHN.18.17": "[Da]{2} [seit]{1} [d Magd]{5,6}, [d Tüürhüeteri]{7,8}, [zum Petrus]{3,4}: «[Bisch]{15} [du]{11} [öppe]{9} [au]{10} [eine]{12} [vo de Jünger]{13,14} [vo däm]{16,18} [Mänsch]{17}?» [Er]{20} [seit]{19}: «[Ich bi s]{22} [nöd]{21}.»",
 "JHN.18.18": "[D Chnächt]{3,4} [aber]{2} und{5} [d Diener]{6,7} [sind]{1} da [gstande]{1}; [si händ]{9} [es Cholefüür]{8} [gmacht]{9}, [wil]{10} [es]{12} [chalt]{11} [gsii isch]{12}, und{13} [händ sich gwärmt]{14}. [Aber]{16} [au]{17} [de Petrus]{18,19} [isch]{15} [bi]{20} [ine]{21} [gstande]{22} und{23} [hät sich gwärmt]{24}.",
 "JHN.18.19": "[De Hoheprieschter]{1,3} [hät]{4} [also]{2} [de Jesus]{5,6} [über]{7} [sini]{8,10} [Jünger]{9} und{11} [über]{12} [sini]{13,15} [Lehr]{14} [usgfröget]{4}.",
 "JHN.18.20": "[De Jesus]{3} [hät]{1} [em]{2} [gantwortet]{1}: «[Ich]{4} [han]{6} [offe]{5} [zur]{7} [Wält]{8} [gredt]{6}; [ich]{9} [han]{11} [immer]{10} [i de Synagoge]{12,13} [glehrt]{11} und{14} [im]{15,16} [Tämpel]{17}, [wo]{18} [alli]{19} [Jude]{20,21} [zämechömed]{22}, und{23} [im]{24} [Verborgne]{25} [han ich]{26} [nüüt]{27} [gredt]{26}.",
 "JHN.18.21": "[Für was]{1} [frögsch]{3} [mich]{2}? [Frög]{4} [die]{5}, [wo]{6} [zueglost händ]{6}, [was]{7} [ich]{8} [zu ine]{9} [gredt han]{8}! [Lueg]{10}, [die]{11} [wüssed]{12}, [was]{13} [ich]{15} [gseit han]{14}.»",
 "JHN.18.22": "[Wo er]{3} [das]{1} [aber]{2} [gseit hät]{4}, [hät]{9} [eine]{5} [vo de Diener]{7,8}, [wo]{6} [debii gstande isch]{6}, [em Jesus]{11,12} [e Ohrfiige]{10} [gää]{9} [und gseit]{13}: «[Eso]{14} [antwortisch du]{15} [em Hoheprieschter]{16,17}?»",
 "JHN.18.23": "[De Jesus]{3} [hät]{1} [em]{2} [gantwortet]{1}: «[Wänn]{4} [ich]{6} [unrächt]{5} [gredt han]{6}, [dänn leg]{7} [über]{8} [s]{9} [Unrächt]{10} [Zügnis ab]{7}; [wänn]{11} [aber]{12} [rächt]{13}, [werum]{14} [schlaasch]{16} [mich]{15}?»",
 "JHN.18.24": "[Da]{2} [hät]{1} [de Hannas]{4,5} [en]{3} [gfesslet]{6} [zum]{7} [Kajafas]{8}, [em Hoheprieschter]{9,10}, [gschickt]{1}.",
 "JHN.18.25": "[De Simon]{3} [Petrus]{4} [aber]{2} [isch]{1} da [gstande]{5} und{6} [hät sich gwärmt]{7}. [Da]{9} [händ si]{8} [zu ihm]{10} [gseit]{8}: «[Bisch]{18} [du]{13} [öppe]{11} [au]{12} [eine]{14} [vo sine]{15,17} [Jünger]{16}?» [Er]{20} [hät abgstritte]{19} und{21} [gseit]{22}: «[Ich bi s]{24} [nöd]{23}.»",
 "JHN.18.26": "[Da seit]{1} [eine]{2} [vo]{3} [de Chnächt]{4,5} [vom Hoheprieschter]{6,7} – [er isch]{9} [en Verwandte]{8} [vo däm]{10} [gsii]{9}, wo [de Petrus]{12} [s]{13} [Oor]{14} [abghaue hät]{11} –: «[Han]{18} [ich]{16} [dich]{17} [nöd]{15} [im]{19,20} [Garte]{21} [mit]{22} [ihm]{23} [gseh]{18}?»",
 "JHN.18.27": "[Da]{2} [hät]{3} [de Petrus]{4} [wider]{1} [abgstritte]{3}, und{5} [grad]{6} [hät]{8} [en Güggel]{7} [gchräit]{8}.",
 "JHN.18.28": "[Dänn]{2} [füered si]{1} [de Jesus]{3,4} [vom]{5,6} [Kajafas]{7} [is]{8,9} [Prätorium]{10}. [Es isch]{11} [aber]{12} [früe am Morge]{13} [gsii]{11}. Und{14} [si sälber]{15} [sind]{17} [nöd]{16} [is]{18,19} [Prätorium]{20} [ine gange]{17}, [demit]{21} [si]{23} [nöd]{22} [unrein wärded]{23}, [sondern]{24} [s Passa]{26,27} [chönd ässe]{25}.",
 "JHN.18.29": "[Da]{2} [isch]{1} [de Pilatus]{3,4} [zu]{6} [ine]{7} [use]{5} [choo]{1} und{8} [seit]{9}: «[Was für e]{10} [Aaklag]{11} [bringed ir]{12} [gäge]{13} [dä]{14,16} [Mänsch]{15} [vor]{12}?»",
 "JHN.18.30": "[Si händ gantwortet]{1} und{2} [zu ihm]{4} [gseit]{3}: «[Wänn]{5} [dä]{8} [nöd]{6} [Böses]{9} [tät]{7,10}, [hetted mir]{12} [en]{15} [dir]{13} [nöd]{11} [usgliferet]{14}.»",
 "JHN.18.31": "[Da]{2} [hät]{1} [de Pilatus]{4,5} [zu ine]{3} [gseit]{1}: «[Nämed]{6} [ir]{8} [en]{7} und{9} [richted]{14} [en]{15} [nach]{10} [eurem]{11,13} [Gsetz]{12}!» [D Jude]{18,19} [händ]{16} [zu ihm]{17} [gseit]{16}: «[Mir]{20} [dörfed]{22} [niemer]{21,24} [töte]{23}.»",
 "JHN.18.32": "[Eso]{1} [hät sich]{6} [s]{2} [Wort]{3} [vom Jesus]{4,5} [söle erfülle]{6}, [wo]{7} [er gseit hät]{8}, [zum aazeige]{9}, [was für en]{10} [Tod]{11} [er]{12} [stärbe]{13} [würd]{12}.",
 "JHN.18.33": "[Da]{2} [isch]{1} [de Pilatus]{7,8} [wider]{3} [is]{4,5} [Prätorium]{6} [ine gange]{1} und{9} [hät]{10} [de Jesus]{11,12} [grüeft]{10} und{13} [zu ihm]{15} [gseit]{14}: «[Bisch]{17} [du]{16} [de König]{18,19} [vo de Jude]{20,21}?»",
 "JHN.18.34": "[De Jesus]{2} [hät gantwortet]{1}: «[Seisch]{7} [du]{5} [das]{6} [vo dir uus]{3,4}, [oder]{8} [händ]{10} [dir]{11} [anderi]{9} [vo]{12} [mir]{13} [verzellt]{10}?»",
 "JHN.18.35": "[De Pilatus]{2,3} [hät gantwortet]{1}: «[Bin]{7} [ich]{5} [öppe]{4} [en Jud]{6}? [Dis]{10,11} [Volk]{8,9} und{12} [d Hoheprieschter]{13,14} [händ]{15} [dich]{16} [mir]{17} [usgliferet]{15}. [Was]{18} [häsch gmacht]{19}?»",
 "JHN.18.36": "[De Jesus]{2} [hät gantwortet]{1}: «[Mis]{5,6} [Riich]{3,4} [isch]{8} [nöd]{7} [us]{9} [dere]{10,12} [Wält]{11}. [Wänn]{13} [mis]{21,22} [Riich]{19,20} [us]{14} [dere]{15,17} [Wält]{16} [wär]{18}, [dänn]{28} [würded]{27} [mini]{25,26} [Diener]{23,24} [kämpfe]{27}, [demit]{29} [ich]{31} [nöd]{30} [de Jude]{32,33} [usgliferet wird]{31}. [Jetzt]{34} [aber]{35} [isch]{41} [mis]{38,39} [Riich]{36,37} [nöd]{40} [vo da]{42}.»",
 "JHN.18.37": "[Da]{2} [hät]{1} [de Pilatus]{4,5} [zu ihm]{3} [gseit]{1}: «[Also]{6} [bisch]{8} [du]{9} [doch]{6} [en König]{7}?» [De Jesus]{11,12} [hät gantwortet]{10}: «[Du]{13} [seisch]{14}, [dass]{15} [ich]{17} [en König]{16} [bi]{17}. [Ich]{18} [bi]{21} [defür]{19,20} [gebore]{21} und{22} [defür]{23,24} [i]{26} [d]{27} [Wält]{28} [choo]{25}, [zum]{29} [d]{31} [Wahrheit]{32} [bezüüge]{30}. [Jede]{33}, [wo]{34} [us]{36} [de]{37} [Wahrheit]{38} [isch]{35}, [lost]{39} [uf mini]{40,41} [Stimm]{42}.»",
 "JHN.18.38": "[De Pilatus]{3,4} [seit]{1} [zu ihm]{2}: «[Was]{5} [isch]{6} [Wahrheit]{7}?» Und{8} [wo er]{10} [das]{9} [gseit gha hät]{10}, [isch er]{12} [wider]{11} [use]{12} [zu]{13} [de Jude]{14,15} [gange]{12} und{16} [seit]{17} [zu ine]{18}: «[Ich]{19} [find]{21} [kei]{20} [Schuld]{24} [a]{22} [ihm]{23}.",
 "JHN.18.39": "[Es isch]{1} [aber]{2} [de Bruuch]{3} [bi eu]{4}, [dass]{5} [ich]{7} [eu]{8} [am]{9,10} [Passa]{11} [eine]{6} [freilaa]{7}. [Wänd ir]{12} [also]{13}, [dass ich]{14} [eu]{15} [de König]{16,17} [vo de Jude]{18,19} [freilaa]{14}?»",
 "JHN.18.40": "[Da]{2} [händ si]{1} [wider]{3} [brüelet]{1}: «[Nöd]{5} [dä]{6}, [sondern]{7} [de Barabbas]{8,9}!» [De Barabbas]{12,13} [aber]{11} [isch]{10} [en Röiber]{14} [gsii]{10}. ~4(λέγοντες leitet di diräkt Red ii)",
 # ------------------------------------------------------------ Kapitel 19
 "JHN.19.1": "[Da]{1} [hät]{3} [de Pilatus]{4,5} [also]{2} [de Jesus]{6,7} [gnoo]{3} und{8} [hät en la gisle]{9}.",
 "JHN.19.2": "Und{1} [d Soldate]{2,3} [händ]{4} [en Chranz]{5} [us]{6} [Dorne]{7} [gflochte]{4} und [händ]{8} en [ihm]{9} [uf]{8} [de]{10} [Chopf]{11} [gsetzt]{8}, und{12} [si händ]{15} [ihm]{16} [en purpurrote]{14} [Mantel]{13} [umgleit]{15}.",
 "JHN.19.3": "Und{1} [si sind]{2} [zu]{3} [ihm]{4} [häre choo]{2} und{5} [händ gseit]{6}: «[Sig gegrüesst]{7}, [König]{8,9} [vo de Jude]{10,11}!» Und{12} [si händ]{13} [ihm]{14} [Ohrfiige]{15} [gää]{13}.",
 "JHN.19.4": "Und{1} [de Pilatus]{5,6} [isch]{2} [wider]{3} [use]{4} [gange]{2} und{7} [seit]{8} [zu ine]{9}: «[Lueged]{10}, [ich bring]{11} [en]{13} [zu eu]{12} [use]{14}, [demit]{15} [ir erchänned]{16}, [dass]{17} [ich]{20} [kei]{18} [Schuld]{19} [a]{21} [ihm]{22} [find]{20}.»",
 "JHN.19.5": "[Da]{2} [isch]{1} [de Jesus]{3,4} [use]{5} [choo]{1}; [er hät]{6} [de]{7} [Dornechranz]{8,9} und{10} [de]{11} [purpurrot]{12} [Mantel]{13} [aagha]{6}. Und{14} [er seit]{15} [zu ine]{16}: «[Lueged]{17}, [de Mänsch]{18,19}!»",
 "JHN.19.6": "[Wo]{1} [en]{4} [also]{2} [d Hoheprieschter]{5,6} und{7} [d Diener]{8,9} [gseh händ]{3}, [händ si brüelet]{10}: «[Chrüüzig]{12}, [chrüüzig]{13}!» [De Pilatus]{16,17} [seit]{14} [zu ine]{15}: «[Nämed]{18} [ir]{20} [en]{19} und{21} [chrüüziged]{22} en! [Ich]{23} [find]{26} [nämli]{24} [kei]{25} [Schuld]{29} [a]{27} [ihm]{28}.» ~11(λέγοντες leitet di diräkt Red ii)",
 "JHN.19.7": "[D Jude]{3,4} [händ]{1} [em]{2} [gantwortet]{1}: «[Mir]{5} [händ]{7} [es Gsetz]{6}, und{8} [nach]{9} [em]{10} [Gsetz]{11} [mues er]{12} [stärbe]{13}, [wil]{14} [er]{18} [sich]{17} [zum Sohn]{15} [vo Gott]{16} [gmacht hät]{18}.»",
 "JHN.19.8": "[Wo]{1} [de Pilatus]{4,5} [also]{2} [das]{6,7} [Wort]{8} [ghört hät]{3}, [hät er]{10} [no meh]{9} [Angscht überchoo]{10}",
 "JHN.19.9": "und{1} [isch]{2} [wider]{6} [is]{3,4} [Prätorium]{5} [ine gange]{2} und{7} [seit]{8} [zum Jesus]{9,10}: «[Vo wo]{11} [bisch]{12} [du]{13}?» [De Jesus]{14,16} [aber]{15} [hät]{19} [em]{20} [kei]{18} [Antwort]{17} [gää]{19}.",
 "JHN.19.10": "[Da]{2} [seit]{1} [de Pilatus]{4,5} [zu ihm]{3}: «[Mit mir]{6} [redsch]{8} [nöd]{7}? [Weisch]{10} [nöd]{9}, [dass]{11} [ich]{13} [d Vollmacht]{12} [han]{13}, [dich]{15} [freizlaa]{14}, und{16} [d Vollmacht]{17} [han]{18}, [dich]{20} [z chrüüzige]{19}?»",
 "JHN.19.11": "[De Jesus]{3} [hät]{1} [em]{2} [gantwortet]{1}: «[Du hettsch]{5} [kei]{4,9} [Vollmacht]{6} [über]{7} [mich]{8}, [wänn]{10} [s]{12} [dir]{14} [nöd]{11} [vo obe]{15} [gää]{13} [worde wär]{12}. [Drum]{16,17} [hät]{24} [dä]{18}, wo [mich]{20} [dir]{21} [usgliferet hät]{19}, [di grösser]{22} [Sünd]{23}.»",
 "JHN.19.12": "[Drufabe]{1,2} [hät]{5} [de Pilatus]{3,4} [probiert]{5}, [en]{7} [freizlaa]{6}. [D Jude]{8,10} [aber]{9} [händ brüelet]{11}: «[Wänn]{13} [du]{15} [dä]{14} [freilaasch]{15}, [bisch]{17} [nöd]{16} [de Fründ]{18} [vom Kaiser]{19,20}. [Jede]{21}, [wo]{22} [sich]{24} [zum König]{23} [macht]{25}, [stellt sich gäge]{26} [de Kaiser]{27,28}.» ~12(λέγοντες leitet di diräkt Red ii)",
 "JHN.19.13": "[Wo]{4} [de Pilatus]{1,3} [also]{2} [die]{5,7} [Wort]{6} [ghört hät]{4}, [hät er]{8} [de Jesus]{10,11} [use]{9} [gfüert]{8} und{12} [hät sich]{13} [uf]{14} [de Richterstuel]{15} [gsetzt]{13}, [a]{16} [däm Ort]{17}, [wo]{18} «[Steipflaschter]{19}» [heisst]{18}, [uf Hebräisch]{20} [aber]{21} «[Gabbata]{22}».",
 "JHN.19.14": "[Es isch]{1} [aber]{2} [de Rüschttag]{3} [vom Passa]{4,5} [gsii]{1}; [es isch]{7} [öppe]{8} [di sächst]{9} [Stund]{6} [gsii]{7}. Und{10} [er seit]{11} [zu de Jude]{12,13}: «[Lueged]{14}, [eue]{15,17} [König]{16}!»",
 "JHN.19.15": "[Da]{2} [händ]{1} [die]{3} [brüelet]{1}: «[Wäg]{4}, [wäg]{5} mit em, [chrüüzig]{6} [en]{7}!» [De Pilatus]{10,11} [seit]{8} [zu ine]{9}: «[Eue]{12,14} [König]{13} [söll ich chrüüzige]{15}?» [D Hoheprieschter]{17,18} [händ gantwortet]{16}: «[Mir händ]{20} [kei]{19} [König]{21} [usser]{22,23} [em Kaiser]{24}.»",
 "JHN.19.16": "[Da]{1} [hät er]{3} [en]{4} [ine]{5} [also]{2} [usgliferet]{3}, [demit]{6} [er gchrüüziget wird]{7}. [Si händ]{8} [de Jesus]{10,11} [also]{9} [übernoo]{8}.",
 "JHN.19.17": "Und{1} [er hät]{2} [s]{4} [Chrüüz]{5} [sälber]{3} [treit]{2} und [isch]{6} [zum]{7,8} [sogenannte]{9} [Schädelplatz]{10,11} [use gange]{6}, [wo]{12} [uf Hebräisch]{14} «[Golgota]{15}» [heisst]{13}.",
 "JHN.19.18": "[Dört]{1} [händ si]{3} [en]{2} [gchrüüziget]{3}, und{4} [mit]{5} [ihm]{6} [zwei]{8} [anderi]{7}, [uf dere]{9} und{10} [uf säbere Siite]{11}, [de Jesus]{14,15} [aber]{13} [i de Mitti]{12}.",
 "JHN.19.19": "[De Pilatus]{5,6} [hät]{1} [aber]{2} [au]{3} [e Tafele]{4} [gschribe]{1} und{7} [hät si]{8} [am]{9,10} [Chrüüz]{11} [aagmacht]{8}. [Es isch]{12} [aber]{13} [gschribe gsii]{14}: «[Jesus]{15}, [de Nazoräer]{16,17}, [de König]{18,19} [vo de Jude]{20,21}.»",
 "JHN.19.20": "[Die]{1,3} [Tafele]{4} [händ]{6} [also]{2} [vili]{5} [vo de Jude]{7,8} [gläse]{6}, [wil]{9} [de Ort]{12,13}, [wo]{16} [de Jesus]{18,19} [gchrüüziget worde isch]{17}, [nööch]{10} [bi de]{14} [Stadt]{15} [gsii isch]{11}; und{20} [si isch]{21} [uf Hebräisch]{23}, [Latiinisch]{24} und [Griechisch]{25} [gschribe gsii]{22}.",
 "JHN.19.21": "[Da]{2} [händ]{1} [d Hoheprieschter]{5,6} [vo de Jude]{7,8} [zum Pilatus]{3,4} [gseit]{1}: «[Schriib]{10} [nöd]{9}: ‹[De König]{11,12} [vo de Jude]{13,14}›, [sondern]{15}: ‹[Dä]{17} [hät gseit]{18}: [Ich bi]{22} [König]{19} [vo de Jude]{20,21}.›» ~16(ὅτι leitet di wörtlich Widergab ii)",
 "JHN.19.22": "[De Pilatus]{2,3} [hät gantwortet]{1}: «[Was]{4} [ich gschribe han]{5}, [han ich gschribe]{6}.»",
 "JHN.19.23": "[D Soldate]{1,3} [also]{2}, [wo]{4} [si]{5} [de Jesus]{6,7} [gchrüüziget gha händ]{5}, [händ]{8} [sini]{9,11} [Chleider]{10} [gnoo]{8} und{12} [händ]{13} [vier]{14} [Teil]{15} [draus gmacht]{13}, [für jede]{16} [Soldat]{17} [ein Teil]{18}, und{19} au [s]{20} [Undergwand]{21}. [S]{24} [Undergwand]{25} [aber]{23} [isch]{22} [ohni Naht]{26} [gsii]{22}, [vo obe aa]{27-29} [i eim Stuck]{31,32} [gwobe]{30}.",
 "JHN.19.24": "[Da]{2} [händ si]{1} [zunenand]{3,4} [gseit]{1}: «[Mer wänd]{6} [s]{7} [nöd]{5} [verriisse]{6}, [sondern]{8} [drum]{10,11} [lose]{9}, [wem]{12} [s ghöre söll]{13}.» [Eso]{14} [hät sich]{17} [d]{15} [Schrift]{16} [söle erfülle]{17}, [wo]{18} [seit]{19}: «[Si händ]{20} [mini]{21,23} [Chleider]{22} [under sich]{24} [verteilt]{20}, und{25} [über]{26} [mis]{27,29} [Gwand]{28} [händ si]{30} [s Los]{31} [gworfe]{30}.» [Das]{36} [händ]{37} [also]{34} [d Soldate]{32,35} [gmacht]{37}. ~33(μέν: nöd eigens widergää)",
 "JHN.19.25": "[Bim]{3,4} [Chrüüz]{5} [vom Jesus]{6,7} [aber]{2} [sind]{1} [sini]{8,10} [Mueter]{9} [gstande]{1} und{11} [d Schwöschter]{12,13} [vo sinere]{14,16} [Mueter]{15}, [d Maria]{17}, [d Frau]{18} [vom Klopas]{19,20}, und{21} [d Maria]{22} [vo Magdala]{23,24}.",
 "JHN.19.26": "[Wo]{3} [de Jesus]{1} [also]{2} [sini]{4} [Mueter]{5} [gseh hät]{3} und{6} [de]{7} [Jünger]{8}, [wo]{10} [er gliebt hät]{11}, [wo debii gstande isch]{9}, [seit er]{12} [zu sinere]{13} [Mueter]{14}: «[Frau]{15}, [lueg]{16}, [din]{17,19} [Sohn]{18}!»",
 "JHN.19.27": "[Dänn]{1} [seit er]{2} [zum]{3} [Jünger]{4}: «[Lueg]{5}, [dini]{6,8} [Mueter]{7}!» Und{9} [vo]{10} [säbere]{11,12} [Stund]{13} [aa]{10} [hät]{14} [de Jünger]{15,16} [si]{17} [zu sich]{18-20} [gnoo]{14}.",
 "JHN.19.28": "[Dänn]{1,2}, [wil]{3} [de Jesus]{4,5} [gwüsst hät]{3}, [dass]{6} [scho]{7} [alles]{8} [vollbracht isch]{9}, [seit er]{14}, [demit]{10} [d]{12} [Schrift]{13} [volländet wird]{11}: «[Ich han Durscht]{15}.»",
 "JHN.19.29": "[Es Gfäss]{1} [voll]{4} [Essig]{3} [isch]{2} da [gstande]{2}. [Si händ]{11} [also]{6} [en Schwamm]{5} [voll]{7} [mit em]{8} [Essig]{9} [uf en Ysopzwiig]{10} [gsteckt]{11} und [händ en]{12} [ihm]{13} [a de]{14} [Mund]{15} [ghebt]{12}.",
 "JHN.19.30": "[Wo]{1} [de Jesus]{6,7} [also]{2} [de]{4} [Essig]{5} [gnoo gha hät]{3}, [hät er gseit]{8}: «[Es isch vollbracht]{9}.» Und{10} [er hät]{11} [de]{12} [Chopf]{13} [gneigt]{11} und [hät]{14} [de]{15} [Geischt]{16} [übergää]{14}.",
 "JHN.19.31": "[D Jude]{1,3} [also]{2} – [wil]{4} [Rüschttag]{5} [gsii isch]{6}, [demit]{7} [d]{13} [Liiber]{14} [nöd]{8} [am]{15,16} [Sabbat]{17} [am]{10,11} [Chrüüz]{12} [bliibed]{9}; [dänn]{19} [säbe]{23,24} [Sabbat]{25} [isch]{18} [en grosse]{20} [Tag]{21,22} [gsii]{18} – [händ]{26} [de Pilatus]{27,28} [bätte]{26}, [dass]{29} [mer]{30} [ine]{31} [d]{32} [Bei]{33} [bricht]{30} und{34} [si abnimmt]{35}.",
 "JHN.19.32": "[Da]{2} [sind]{1} [d Soldate]{3,4} [choo]{1} und{5} [händ]{9} [em]{6} [erschte]{8} [d]{10} [Bei]{11} [broche]{9} und{12} [em]{13} [andere]{14}, [wo]{15} [mit ihm]{17} [gchrüüziget worde isch]{16}. ~7(μέν: nöd eigens widergää)",
 "JHN.19.33": "[Wo si]{5} [aber]{2} [zum]{1} [Jesus]{3,4} [choo sind]{5} und [gseh händ]{7}, [dass er]{9} [scho]{8} [tot isch]{10}, [händ si]{12} [ihm]{13} [d]{14} [Bei]{15} [nöd]{11} [broche]{12}. ~6(ὡς «als»: mit «wo» zämegfasst)",
 "JHN.19.34": "[Sondern]{1} [eine]{2} [vo de Soldate]{3,4} [hät]{9} [ihm]{6} [mit ere Lanze]{5} [i]{9} [d]{7} [Siite]{8} [gstoche]{9}, und{10} [grad]{12} [isch]{11} [Bluet]{13} und{14} [Wasser]{15} [usechoo]{11}.",
 "JHN.19.35": "Und{1} [dä]{2}, wo [s gseh hät]{3}, [hät s bezüügt]{4}, und{5} [sis]{7} [Zügnis]{9,10} [isch]{8} [wahr]{6}; und{11} [dä]{12} [weiss]{13}, [dass]{14} [er]{16} [d Wahrheit]{15} [seit]{16}, [demit]{17} [au]{18} [ir]{19} [glaubed]{20}.",
 "JHN.19.36": "[Das]{3} [isch]{1} [nämli]{2} [gscheh]{1}, [demit]{4} [d]{5} [Schrift]{6} [erfüllt wird]{7}: «[Kei]{9} [Chnoche]{8} [vo ihm]{11} [wird broche]{10}.»",
 "JHN.19.37": "Und{1} [wider]{2} [seit]{5} [en anderi]{3} [Schrift]{4}: «[Si wärded]{6} [uf]{7} [dä]{8} [luege]{6}, wo [si durchbohrt händ]{9}.»",
 "JHN.19.38": "[Dänn]{1,3} [aber]{2} [hät]{4} [de Josef]{7} [vo]{8} [Arimatäa]{9}, [wo]{10} [en Jünger]{11} [vom Jesus]{12,13} [gsii isch]{10}, [aber]{15} [heimli]{14} [us]{16} [Angscht]{17,18} [vor de Jude]{19,20}, [de Pilatus]{5,6} [bätte]{4}, [dass]{21} [er]{22} [de Liib]{23,24} [vom Jesus]{25,26} [dörf abnää]{22}; und{27} [de Pilatus]{29,30} [hät s erlaubt]{28}. [Da]{32} [isch er choo]{31} und{33} [hät]{34} [sin]{35,37} [Liib]{36} [abgnoo]{34}.",
 "JHN.19.39": "[Es isch]{1} [aber]{2} [au]{3} [de Nikodemus]{4} [choo]{1}, [wo]{5} [s erscht Mal]{10,11} [znacht]{9} [zu]{7} [ihm]{8} [choo isch]{6}; [er hät]{12} [e Mischig]{13} [us Myrrhe]{14} und{15} [Aloe]{16} [mitbracht]{12}, [öppe]{17} [hundert]{19} [Pfund]{18}.",
 "JHN.19.40": "[Si händ]{1} [also]{2} [de Liib]{3,4} [vom Jesus]{5,6} [gnoo]{1} und{7} [händ]{8} [en]{9} [mit]{11} [de Duftstoff]{12,13} [i Liinebinde]{10} [iigwicklet]{8}, [wie]{14} s [bi de Jude]{17,18} [bim Begrabe]{19} [de Bruuch]{15} [isch]{16}.",
 "JHN.19.41": "[Es isch]{1} [aber]{2} [a]{3} [däm]{4} [Ort]{5}, [wo]{6} [er gchrüüziget worde isch]{7}, [en Garte]{8} [gsii]{1}, und{9} [i]{10} [däm]{11} [Garte]{12} [es nöis]{14} [Grab]{13}, [wo]{15,16} [no nie]{17} [öpper]{18} [drii gleit worde isch]{19,20}.",
 "JHN.19.42": "[Dört]{1} [also]{2} [händ si]{13} [de Jesus]{14,15} [hiigleit]{13}, [wäge]{3} [em]{4} [Rüschttag]{5} [vo de Jude]{6,7}, [wil]{8} [s]{11} [Grab]{12} [nööch]{9} [gsii isch]{10}.",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("JHN.18.1", "des Baches", "adapted", "χειμάρρου", "des Winterbaches", ["des Wadis"], "χείμαρρος ist ein Bach, der nur in der Regenzeit Wasser führt. Der Kidron fliesst zwischen Jerusalem und dem Ölberg."),
 ("JHN.18.2", "auslieferte", "literal", "παραδιδοὺς", None, ["verriet"], "παραδίδωμι heisst «übergeben, ausliefern» und ist in Johannes 18–19 durchgehend so wiedergegeben: für Judas ([[JHN.18.2]], [[JHN.18.5]]), für die Ankläger ([[JHN.18.30]], [[JHN.18.35]], [[JHN.19.11]]) und für Pilatus ([[JHN.19.16]]). In [[JHN.19.30]] steht dasselbe Verb für Jesu Sterben («übergab den Geist»). «Verraten» ist die vertraute Wiedergabe bei Judas, verdeckt aber diese Kette."),
 ("JHN.18.3", "Kohorte", "literal", "σπεῖραν", None, ["Truppe", "Abteilung"], "Nach gängiger Angabe eine römische Einheit von mehreren hundert Mann. Ob eine ganze Kohorte oder eine Abteilung gemeint ist, sagt der Text nicht. Zusammen mit dem χιλίαρχος ([[JHN.18.12]]) nennt Johannes römische Soldaten neben den Dienern der Hohepriester."),
 ("JHN.18.3", "Diener", "interpretive", "ὑπηρέτας", None, ["Gerichtsdiener", "Tempelwachen"], "ὑπηρέτης ist ein Untergebener im Dienst einer Behörde, hier wohl die Tempelwache. Dasselbe Wort steht in [[JHN.18.36]] für die «Diener» Jesu; die einheitliche Wiedergabe hält den Bezug sichtbar."),
 ("JHN.18.5", "den Nazoräer", "literal", "τὸν Ναζωραῖον", None, ["aus Nazaret"], "Ναζωραῖος (anders als Ναζαρηνός bei Markus) wird meist als Herkunftsbezeichnung nach Nazaret verstanden; die genaue Ableitung des Wortes ist umstritten. Ebenso [[JHN.18.7]] und [[JHN.19.19]]."),
 ("JHN.18.5", "Ich bin es", "interpretive", "Ἐγώ εἰμι", "Ich bin", ["Ich bin’s"], "Als Antwort auf «Jesus, den Nazoräer» heisst ἐγώ εἰμι zunächst «ich bin es». Johannes verwendet die Wendung aber auch ohne Ergänzung als Selbstaussage Jesu ([[JHN.8.24]], [[JHN.8.28]], [[JHN.8.58]], [[JHN.13.19]]), die an Gottes Selbstvorstellung in der griechischen Bibel anklingt (vgl. [[EXO.3.14]], [[ISA.43.10]]). Dass die Häscher bei diesen Worten zurückweichen und zu Boden fallen ([[JHN.18.6]]), deuten viele als Hinweis auf diesen Doppelsinn; andere sehen darin nur Erschrecken vor dem gefassten Auftreten Jesu. Die Übersetzung wählt «Ich bin es», weil es eine Antwort ist, und nennt «Ich bin» als wörtlichere Fassung; redaktionelle Entscheidung. Ebenso [[JHN.18.6]] und [[JHN.18.8]]. Petrus antwortet dagegen zweimal οὐκ εἰμί, «Ich bin es nicht» ([[JHN.18.17]], [[JHN.18.25]])."),
 ("JHN.18.6", "Ich bin es", "interpretive", "Ἐγώ εἰμι", "Ich bin", None, "Wie [[JHN.18.5]]."),
 ("JHN.18.8", "ich es bin", "interpretive", "ἐγώ εἰμι", "ich bin", None, "Wie [[JHN.18.5]]."),
 ("JHN.18.9", "So sollte", "adapted", "ἵνα πληρωθῇ", "damit … erfüllt würde", None, "Der griechische Satz ist verkürzt («[Das geschah,] damit …»). Das Wort bezieht sich auf [[JHN.17.12]] (vgl. [[JHN.6.39]]). Ebenso [[JHN.18.32]] und [[JHN.19.24]]."),
 ("JHN.18.10", "Knecht", "traditional", "δοῦλον", "Sklaven", ["Diener"], None),
 ("JHN.18.11", "Den Becher", "literal", "τὸ ποτήριον", None, ["Den Kelch"], "Der Becher ist ein Bild für das zugemessene Geschick (vgl. [[MRK.14.36]])."),
 ("JHN.18.12", "der Oberst", "interpretive", "ὁ χιλίαρχος", "der Befehlshaber über tausend", ["der Tribun", "der Kommandant"], "Ein römischer Offizier, nach gängiger Angabe Befehlshaber einer Kohorte."),
 ("JHN.18.12", "der Juden", "interpretive", "τῶν Ἰουδαίων", None, ["der jüdischen Behörden", "der jüdischen Führer", "der Judäer"], "οἱ Ἰουδαῖοι ist im Johannesevangelium durchgehend wörtlich mit «die Juden» wiedergegeben (Grundentscheid, siehe Hinweise zur Übersetzung). In Johannes 18–19 sind damit meist die jüdischen Behörden in Jerusalem gemeint, die Jesus an Pilatus übergeben ([[JHN.18.31]], [[JHN.19.7]], [[JHN.19.12]]); an anderen Stellen die Bevölkerung Judäas oder das jüdische Volk mit seinen Bräuchen ([[JHN.19.20]], [[JHN.19.40]]). Jesus, seine Jünger und Josef von Arimatäa sind selbst Juden. Eine Wiedergabe wie «die jüdischen Führer» wäre eine Deutung; die wörtliche ist es ebenfalls, weil sie leicht als Aussage über alle Juden gelesen wird. Redaktionelle Entscheidung: wörtlich, mit diesem Hinweis."),
 ("JHN.18.13", "in jenem Jahr", "literal", "τοῦ ἐνιαυτοῦ ἐκείνου", "jenes Jahres", None, "Wie [[JHN.11.49]]. Die Wendung wird meist so verstanden, dass sie das entscheidende Jahr hervorhebt; ob Johannes an einen jährlichen Wechsel des Amtes dachte, wird verschieden beurteilt."),
 ("JHN.18.15", "ein anderer", "literal", "ἄλλος", None, None, "Der Text nennt den Jünger nicht. Oft wird er mit dem Jünger gleichgesetzt, «den Jesus liebte» ([[JHN.13.23]], [[JHN.19.26]]); das bleibt eine Vermutung."),
 ("JHN.18.18", "ein Kohlenfeuer", "literal", "ἀνθρακιὰν", None, None, "Dasselbe seltene Wort steht in [[JHN.21.9]]."),
 ("JHN.18.19", "Der Hohepriester", "literal", "ἀρχιερεὺς", None, None, "Nach [[JHN.18.13]] wird Jesus zuerst zu Hannas gebracht und erst nach [[JHN.18.24]] zu Kajafas. Ob «der Hohepriester» hier Hannas meint (als früherer Hohepriester, der den Titel behielt) oder Kajafas, wird verschieden beurteilt; der Text sagt es nicht."),
 ("JHN.18.20", "zur Welt", "literal", "τῷ κόσμῳ", None, ["öffentlich"], "κόσμος ist im Johannesevangelium durchgehend mit «Welt» wiedergegeben (vgl. [[JHN.18.36]], [[JHN.18.37]]); hier meint es die Öffentlichkeit."),
 ("JHN.18.22", "einen Schlag ins Gesicht", "interpretive", "ῥάπισμα", None, ["eine Ohrfeige", "einen Stockschlag"], "ῥάπισμα kann einen Schlag mit der flachen Hand oder mit einem Stock bezeichnen. Ebenso [[JHN.19.3]]."),
 ("JHN.18.24", "schickte", "interpretive", "ἀπέστειλεν", None, ["hatte geschickt"], "Der Aorist lässt sich auch vorzeitig verstehen («hatte geschickt»); dann wäre das Verhör [[JHN.18.19]]–[[JHN.18.23]] eines vor Kajafas. Die Übersetzung folgt dem einfachen Erzählablauf."),
 ("JHN.18.28", "Prätorium", "literal", "πραιτώριον", None, ["Amtssitz des Statthalters"], "Lateinisches Lehnwort: der Amtssitz des römischen Statthalters in Jerusalem."),
 ("JHN.18.28", "das Passa", "interpretive", "τὸ πάσχα", None, ["das Passamahl", "das Passalamm"], "Nach Johannes steht das Passamahl am Morgen der Verurteilung noch bevor (vgl. [[JHN.19.14]], [[JHN.19.31]]); bei Markus ist das letzte Mahl Jesu ein Passamahl ([[MRK.14.12]]). Wie sich die beiden Zeitangaben zueinander verhalten, wird verschieden erklärt; manche verstehen πάσχα hier weiter als die Festmahlzeiten der Passawoche."),
 ("JHN.18.31", "Uns ist es nicht erlaubt, jemanden zu töten", "literal", "Ἡμῖν οὐκ ἔξεστιν ἀποκτεῖναι οὐδένα", None, None, "Ob der jüdische Rat unter römischer Herrschaft Todesurteile vollstrecken durfte, ist historisch umstritten. [[JHN.18.32]] deutet den Satz auf die Todesart: die römische Kreuzigung als «Erhöhung» (vgl. [[JHN.12.32]]–[[JHN.12.33]])."),
 ("JHN.18.35", "Volk", "literal", "ἔθνος", None, ["Nation"], "Wie [[JHN.11.48]]–[[JHN.11.52]]."),
 ("JHN.18.36", "Reich", "interpretive", "βασιλεία", None, ["Königsherrschaft", "Königtum"], "βασιλεία meint hier zuerst das Königtum, die Herrschaft Jesu, im Gegenüber zur Frage nach dem «König der Juden». «Nicht aus dieser Welt» (ἐκ) nennt die Herkunft dieser Herrschaft; daraus folgt nicht, dass sie mit der Welt nichts zu tun hätte. «Diener» ist dasselbe Wort wie in [[JHN.18.3]]."),
 ("JHN.18.37", "Du sagst, dass ich ein König bin", "interpretive", "Σὺ λέγεις ὅτι βασιλεύς εἰμι", None, ["Du sagst es: Ich bin ein König", "Du sagst es, denn ich bin ein König"], "ὅτι kann den Inhalt des Gesagten einleiten oder begründen; je nachdem klingt die Antwort zurückhaltend oder bejahend (vgl. [[MRK.15.2]]). Das folgende ἐγώ wird hier, wie in den gängigen Ausgaben, zum nächsten Satz gezogen."),
 ("JHN.18.37", "Wahrheit", "literal", "ἀληθείᾳ", None, None, "ἀλήθεια ist ein Schlüsselwort des Johannesevangeliums (vgl. [[JHN.1.14]], [[JHN.14.6]]) und durchgehend mit «Wahrheit» wiedergegeben. Pilatus nimmt es in [[JHN.18.38]] auf."),
 ("JHN.18.40", "ein Räuber", "interpretive", "λῃστής", None, ["ein Bandit", "ein Aufständischer"], "λῃστής kann nach gängiger Angabe im 1. Jahrhundert auch bewaffnete Banden und Aufständische bezeichnen (vgl. [[MRK.14.48]], [[MRK.15.7]])."),
 ("JHN.19.1", "liess ihn geisseln", "adapted", "ἐμαστίγωσεν", "geisselte ihn", None, "Pilatus veranlasst die Geisselung; ausgeführt haben sie Soldaten."),
 ("JHN.19.5", "er sagt", "interpretive", "λέγει", None, ["Pilatus sagt"], "Der Sprecher ist nicht genannt; meist wird an Pilatus gedacht (vgl. [[JHN.19.4]]). Ebenso [[JHN.19.14]]."),
 ("JHN.19.5", "Seht, der Mensch!", "literal", "Ἰδοὺ ὁ ἄνθρωπος", None, ["Seht, was für ein Mensch!"], "Ob der Satz Spott, Mitleid oder eine Bitte um Einlenken ausdrückt, lässt der knappe Wortlaut offen; die christliche Auslegung hat ihn vielfach weitergedeutet («Ecce homo»)."),
 ("JHN.19.7", "zum Sohn Gottes", "literal", "υἱὸν θεοῦ", None, ["zu einem Sohn Gottes"], "Ohne Artikel. Welches Gesetz gemeint ist, sagen die Ankläger nicht; oft wird an das Verbot der Gotteslästerung gedacht ([[LEV.24.16]])."),
 ("JHN.19.8", "noch mehr", "interpretive", "μᾶλλον", None, ["umso mehr", "sehr"], "Von einer früheren Furcht des Pilatus war nicht die Rede; μᾶλλον kann auch einfach steigernd verstanden werden."),
 ("JHN.19.10", "Vollmacht", "literal", "ἐξουσίαν", None, ["Macht", "Befugnis"], "Ebenso [[JHN.19.11]]."),
 ("JHN.19.11", "von oben", "interpretive", "ἄνωθεν", None, ["von Gott"], "ἄνωθεν heisst «von oben» und «von neuem»; in [[JHN.3.3]] und [[JHN.3.7]] trägt das Wort beide Bedeutungen (siehe die Entscheidung dort). Hier ist «von oben», also von Gott her, gemeint. Das Partizip δεδομένον ist sächlich; gegeben ist demnach nicht die «Vollmacht» (weiblich), sondern das ganze Geschehen. Deshalb «es»."),
 ("JHN.19.11", "mich dir ausgeliefert hat", "interpretive", "ὁ παραδούς μέ σοι", None, None, "Gemeint ist wohl Kajafas bzw. die jüdische Führung, die Jesus Pilatus übergab ([[JHN.18.30]], [[JHN.18.35]]); andere denken an Judas."),
 ("JHN.19.12", "Daraufhin", "interpretive", "ἐκ τούτου", "Von da an", ["Deswegen"], "Zeitlich oder begründend."),
 ("JHN.19.12", "Freund des Kaisers", "interpretive", "φίλος τοῦ Καίσαρος", None, ["Freund des Kaisers (als Ehrentitel)"], "Kann allgemein Loyalität meinen oder einen Ehrentitel für Vertraute des Kaisers (lateinisch amicus Caesaris); ob Pilatus ihn trug, sagt der Text nicht."),
 ("JHN.19.13", "setzte sich auf den Richterstuhl", "interpretive", "ἐκάθισεν ἐπὶ βήματος", None, ["setzte ihn auf den Richterstuhl"], "ἐκάθισεν kann auch transitiv verstanden werden: Pilatus setzte Jesus (zum Spott) auf den Richterstuhl. Grammatisch ist beides möglich; die Übersetzung liest es intransitiv (redaktionelle Entscheidung)."),
 ("JHN.19.13", "auf Hebräisch", "literal", "Ἑβραϊστὶ", None, ["auf Aramäisch"], "Gemeint ist wohl die aramäische Landessprache; so werden auch Gabbata und Golgota meist als aramäische Wörter erklärt. Ebenso [[JHN.19.17]] und [[JHN.19.20]]."),
 ("JHN.19.14", "der Rüsttag", "interpretive", "παρασκευὴ", "die Vorbereitung", ["der Freitag"], "Der Tag der Vorbereitung auf das Passa; nach gängiger Erklärung der Tag, an dem die Passalämmer geschlachtet wurden. Andere verstehen παρασκευή hier als den Freitag (Vorbereitung auf den Sabbat) in der Passawoche (vgl. [[JHN.19.31]], [[JHN.19.42]]). Vgl. [[JHN.18.28]]."),
 ("JHN.19.14", "die sechste", "literal", "ἕκτη", None, ["Mittag"], "Bei Zählung ab Sonnenaufgang etwa Mittag. [[MRK.15.25]] nennt für die Kreuzigung die dritte Stunde; der Unterschied wird verschieden erklärt."),
 ("JHN.19.15", "Weg, weg mit ihm", "adapted", "Ἆρον ἆρον", "Nimm weg, nimm weg", None, None),
 ("JHN.19.16", "ihnen", "literal", "αὐτοῖς", None, None, "Grammatisch beziehen sich «ihnen» und «sie übernahmen» auf die zuvor genannten Hohepriester ([[JHN.19.15]]); die Kreuzigung führen nach [[JHN.19.23]] römische Soldaten aus."),
 ("JHN.19.17", "trug das Kreuz selbst", "literal", "βαστάζων αὑτῷ τὸν σταυρὸν", None, None, "Johannes erwähnt Simon von Kyrene nicht (anders [[MRK.15.21]])."),
 ("JHN.19.17", "Schädelstätte", "traditional", "Κρανίου Τόπον", "Schädelort", None, "Golgota ist die griechische Umschrift des aramäischen gulgultāʾ «Schädel» (vgl. [[MRK.15.22]])."),
 ("JHN.19.19", "eine Tafel", "interpretive", "τίτλον", "eine Aufschrift", ["ein Schild"], "τίτλος (lateinisch titulus): eine Tafel mit Namen und Vergehen des Verurteilten."),
 ("JHN.19.23", "Untergewand", "literal", "χιτῶνα", None, ["Leibrock", "Hemd"], "Der χιτών wurde direkt auf dem Leib getragen, das ἱμάτιον («Kleid, Mantel») darüber."),
 ("JHN.19.24", "Sie haben meine Kleider unter sich verteilt", "literal", "Διεμερίσαντο τὰ ἱμάτιά μου ἑαυτοῖς", None, None, "Zitat aus [[PSA.22.18]]; der Wortlaut stimmt nach gängiger Angabe mit der griechischen Übersetzung des Psalms überein (in den Projektdaten nicht geprüft). Die beiden parallelen Vershälften erzählt Johannes als zwei Handlungen: Verteilung der Kleider und Los über das Untergewand."),
 ("JHN.19.25", "die Frau", "interpretive", "ἡ", "die (des Klopas)", ["die Tochter", "die Mutter"], "Das Verwandtschaftsverhältnis ist nicht genannt; «Frau» ist die häufigste Ergänzung. Ob «die Schwester seiner Mutter» und «Maria, die (Frau) des Klopas» dieselbe Person sind (dann drei Frauen) oder zwei (vier Frauen), lässt der Satz offen."),
 ("JHN.19.25", "Maria aus Magdala", "interpretive", "Μαρία ἡ Μαγδαληνή", "Maria, die Magdalenerin", ["Maria Magdalena"], "Herkunftsbezeichnung nach dem Ort Magdala am See Gennesaret."),
 ("JHN.19.26", "den er liebte", "literal", "ὃν ἠγάπα", None, None, "Der Jünger, «den Jesus liebte», wird im Johannesevangelium nie mit Namen genannt (vgl. [[JHN.13.23]], [[JHN.21.20]], [[JHN.21.24]])."),
 ("JHN.19.26", "Frau", "literal", "Γύναι", None, None, "Eine respektvolle Anrede, die Jesus auch in [[JHN.2.4]] gegenüber seiner Mutter verwendet; im Deutschen klingt sie kühler als im Griechischen."),
 ("JHN.19.27", "zu sich", "adapted", "εἰς τὰ ἴδια", "in das Eigene", ["in sein Haus"], None),
 ("JHN.19.28", "vollbracht ist", "literal", "τετέλεσται", None, ["vollendet ist"], "Dasselbe Wort wie in [[JHN.19.30]]; siehe dort."),
 ("JHN.19.28", "vollendet würde", "interpretive", "τελειωθῇ", None, ["erfüllt würde"], "Johannes verwendet hier τελειόω «vollenden, ans Ziel bringen» statt des sonst gebrauchten πληρόω «erfüllen» (vgl. [[JHN.19.24]], [[JHN.19.36]]); das Wort ist mit τετέλεσται verwandt. Ob sich der Nebensatz auf «sagt er» oder auf «dass schon alles vollbracht ist» bezieht, ist umstritten. Als Schriftbezug für «Mich dürstet» werden meist [[PSA.69.21]] und [[PSA.22.15]] genannt."),
 ("JHN.19.29", "Essig", "traditional", "ὄξους", None, ["sauren Wein"], "Nach gängiger Erklärung billiger, saurer Wein, wie ihn Soldaten tranken; klingt an [[PSA.69.21]] an (vgl. [[MRK.15.36]])."),
 ("JHN.19.29", "auf einen Ysopzweig", "literal", "ὑσσώπῳ", "Ysop", None, "Mit Ysop wurde beim Auszug aus Ägypten das Blut des Passalamms an die Türpfosten gestrichen ([[EXO.12.22]]). Wie ein Ysopzweig einen vollgesogenen Schwamm tragen konnte, wird verschieden erklärt."),
 ("JHN.19.30", "Es ist vollbracht", "traditional", "Τετέλεσται", "Es ist vollendet worden", ["Es ist vollendet", "Es ist zu Ende gebracht", "Es ist erfüllt"], "Perfekt Passiv von τελέω «zu Ende führen, vollenden, erfüllen»: Etwas ist abgeschlossen, und das Ergebnis bleibt. Das Wort nimmt [[JHN.19.28]] auf und erinnert an das Werk, das Jesus nach [[JHN.4.34]] und [[JHN.17.4]] vollenden soll, sowie an [[JHN.13.1]] (εἰς τέλος «bis zum Ende, ganz»). Im Text ist es eine Feststellung, kein Ausruf der Erschöpfung. Was genau als vollbracht gilt – das Werk, die Schrift, die Liebe bis zum Ende, die Hingabe für andere –, beantworten Auslegungstraditionen verschieden. «Es ist vollbracht» folgt der vertrauten deutschen Wiedergabe und hält diese Offenheit; redaktionelle Entscheidung."),
 ("JHN.19.30", "übergab den Geist", "literal", "παρέδωκεν τὸ πνεῦμα", None, ["gab den Geist auf", "verschied"], "Das Verb ist παραδίδωμι, in der Passionserzählung sonst «ausliefern» ([[JHN.19.16]]). Hier gibt Jesus selbst sein Leben hin (vgl. [[JHN.10.18]]). Manche hören darin auch einen Hinweis auf die Gabe des Geistes ([[JHN.7.39]], [[JHN.20.22]]); das ist Deutung."),
 ("JHN.19.31", "Leiber", "literal", "σώματα", None, ["Leichname"], None),
 ("JHN.19.31", "blieben", "literal", "μείνῃ", None, None, "μένω ist im Johannesevangelium durchgehend mit «bleiben» wiedergegeben; hier ohne theologischen Nebensinn. Zum Hintergrund vgl. [[DEU.21.22]]–[[DEU.21.23]]."),
 ("JHN.19.31", "ein grosser", "literal", "μεγάλη", None, ["ein hoher Feiertag"], "Meist so erklärt: Nach der Darstellung des Johannes ([[JHN.19.14]]) fiel der Sabbat in jenem Jahr mit dem Passafest zusammen."),
 ("JHN.19.34", "Blut", "literal", "αἷμα", None, None, "Johannes unterstreicht das Geschehen mit dem Zeugnis in [[JHN.19.35]]. Medizinische Erklärungen und symbolische Deutungen (etwa auf Taufe und Abendmahl, vgl. [[1JN.5.6]]) werden vertreten; der Text selbst deutet es nicht."),
 ("JHN.19.35", "jener", "interpretive", "ἐκεῖνος", None, ["er selbst"], "Meist auf den Zeugen selbst bezogen; manche beziehen ἐκεῖνος auf Christus oder Gott als Bürgen des Zeugnisses."),
 ("JHN.19.35", "glaubt", "interpretive", "πιστεύητε", None, ["zum Glauben kommt"], "Präsens: glaubt (weiterhin). Andere Handschriften haben den Aorist «zum Glauben kommt» (siehe Alternative); vgl. [[JHN.20.31]]."),
 ("JHN.19.36", "Kein Knochen von ihm wird zerbrochen werden", "literal", "Ὀστοῦν οὐ συντριβήσεται αὐτοῦ", None, None, "Vgl. [[EXO.12.46]] und [[NUM.9.12]] (Passalamm) sowie [[PSA.34.20]] (der Gerechte)."),
 ("JHN.19.37", "sie durchbohrt haben", "literal", "ἐξεκέντησαν", None, None, "Zitat aus [[ZEC.12.10]]. Nach gängiger Angabe steht der Wortlaut dem hebräischen Text näher als der griechischen Übersetzung (Septuaginta), die dort nicht «durchbohren» liest; in den Projektdaten nicht geprüft."),
 ("JHN.19.38", "heimlich", "literal", "κεκρυμμένος", "verborgen", None, None),
 ("JHN.19.39", "Pfund", "interpretive", "λίτρας", "Litren", None, "Eine λίτρα (lateinisch libra, das römische Pfund) wog nach gängiger Angabe etwa 327 Gramm; hundert davon wären rund 33 Kilogramm, eine auffallend grosse Menge. Die Umrechnung antiker Gewichte ist nicht genau und in den Projektdaten nicht belegt."),
 ("JHN.19.40", "den Duftstoffen", "interpretive", "τῶν ἀρωμάτων", None, ["den wohlriechenden Ölen", "den Gewürzen"], "Hier die trockene Mischung aus Myrrhe und Aloe ([[JHN.19.39]])."),
 ("JHN.19.40", "in Leinenbinden", "interpretive", "ὀθονίοις", None, ["in Leinentücher"], "ὀθόνιον bezeichnet Leinenstreifen oder -tücher; vgl. [[JHN.20.5]]–[[JHN.20.7]]."),
]

DEC_GSW = [
 ("JHN.18.2", "usgliferet hät", "literal", "παραδιδοὺς", None, ["verrate hät"], "παραδίδωμι heisst «übergää, uslifere» und isch i Johannes 18–19 überall eso widergää; au i [[JHN.19.30]] staat s gliich Verb («hät de Geischt übergää»)."),
 ("JHN.18.3", "Kohorte", "literal", "σπεῖραν", None, ["Truppe"], "Nach gängiger Aagab e römischi Iiheit vo mehrere hundert Maa."),
 ("JHN.18.3", "Diener", "interpretive", "ὑπηρέτας", None, ["Tämpelwach"], "Wohl d Tämpelwach. S gliich Wort staat i [[JHN.18.36]] für d «Diener» vom Jesus."),
 ("JHN.18.5", "bi s", "interpretive", "εἰμι", "bi", None, "Als Antwort heisst ἐγώ εἰμι «ich bi s». Bim Johannes isch s aber au e Säg vom Jesus über sich sälber ([[JHN.8.24]], [[JHN.8.58]]), wo a Gott sini Vorstellig aaklingt ([[EXO.3.14]], [[ISA.43.10]]). Dass d Lüüt zrugg wiiched und a Bode gheied ([[JHN.18.6]]), verstönd vili als Hiiwiis uf dä Doppelsinn, anderi als Erschrecke. Redaktionelle Entscheid: «Ich bi s», wil s e Antwort isch. Gliich [[JHN.18.6]] und [[JHN.18.8]]. De Petrus seit dergäge zwei Mal «Ich bi s nöd» ([[JHN.18.17]], [[JHN.18.25]])."),
 ("JHN.18.11", "De Bächer", "literal", "τὸ ποτήριον", None, ["De Kelch"], "Es Bild für das, wo eim zuegmässe isch (vgl. [[MRK.14.36]])."),
 ("JHN.18.12", "vo de Jude", "interpretive", "τῶν Ἰουδαίων", None, ["vo de jüdische Behörde", "vo de jüdische Füerer"], "οἱ Ἰουδαῖοι isch im ganze Johannesevangelium wörtlich mit «d Jude» widergää (Grundentscheid). I Johannes 18–19 sind meischtens di jüdische Behörde z Jerusalem gmeint; de Jesus, sini Jünger und de Josef vo Arimatäa sind sälber Jude. «D jüdische Füerer» wär e Düütig; di wörtlich Widergab aber au, wil mer si liecht als Uussag über alli Jude list. Redaktionelle Entscheid: wörtlich, mit däm Hiiwiis."),
 ("JHN.18.18", "es Cholefüür", "literal", "ἀνθρακιὰν", None, ["es Gluetfüür"], "ἀνθρακιά isch es Füür us Holzchole. S gliich sälte Wort staat nu no i [[JHN.21.9]]; drum heisst s a beide Stelle «Cholefüür»."),
 ("JHN.18.27", "en Güggel", "adapted", "ἀλέκτωρ", "en Hahn", None, None),
 ("JHN.18.36", "Riich", "interpretive", "βασιλεία", None, ["Königsherrschaft"], "Gmeint isch zerscht d Herrschaft vom Jesus als König. «Nöd us dere Wält» nännt, wo die Herrschaft herchunnt; es heisst nöd, dass si mit de Wält nüüt z tue hett."),
 ("JHN.18.37", "Du seisch, dass ich en König bi", "interpretive", "Σὺ λέγεις ὅτι βασιλεύς εἰμι", None, ["Du seisch es: Ich bi en König"], "ὅτι cha de Inhalt iileite oder begründe; je nachdem tönt d Antwort zrugghaltend oder bejahend."),
 ("JHN.19.5", "Lueged, de Mänsch!", "literal", "Ἰδοὺ ὁ ἄνθρωπος", None, None, "Wer s seit, staat nöd da; meischtens dänkt mer a de Pilatus. Öb s Spott oder Mitleid isch, laat de Text offe."),
 ("JHN.19.11", "vo obe", "interpretive", "ἄνωθεν", None, None, "ἄνωθεν heisst «vo obe» und «vo nöiem»; i [[JHN.3.3]] treit s Wort beides. Da isch «vo obe», vo Gott här, gmeint. S Partizip isch sächlich: nöd d Vollmacht, sondern s ganz Gscheh isch «gää»; drum «s»."),
 ("JHN.19.13", "hät sich", "interpretive", "ἐκάθισεν", None, ["hät en (de Jesus) … gsetzt"], "ἐκάθισεν cha au heisse: de Pilatus hät de Jesus uf de Richterstuel gsetzt. Grammatisch gaat beides."),
 ("JHN.19.13", "uf Hebräisch", "literal", "Ἑβραϊστὶ", None, ["uf Aramäisch"], "Gmeint isch wohl d aramäisch Landesspraach."),
 ("JHN.19.14", "de Rüschttag", "interpretive", "παρασκευὴ", None, ["de Friitig"], "De Tag vor em Passa; nach gängiger Erklärig de Tag, wo d Passalämmer gschlachtet worde sind; anderi verstönd en als Friitig i de Passawuche. Vgl. [[JHN.18.28]], [[JHN.19.31]]."),
 ("JHN.19.25", "d Frau", "interpretive", "ἡ", "die (vom Klopas)", ["d Tochter", "d Mueter"], "S Verwandtschaftsverhältnis staat nöd da. Öb d Schwöschter vo de Mueter und d Maria vom Klopas di gliich Person sind (drüü Fraue) oder nöd (vier Fraue), laat de Satz offe."),
 ("JHN.19.26", "er gliebt hät", "literal", "ἠγάπα", None, None, "Im ganze Evangelium: ἀγαπάω «liebe», φιλέω «gärn haa». De Jünger, wo de Jesus gliebt hät, wird nie mit Name gnännt (vgl. [[JHN.13.23]], [[JHN.21.20]])."),
 ("JHN.19.26", "Frau", "literal", "Γύναι", None, None, "E respektvolli Aared (vgl. [[JHN.2.4]]); uf Dütsch tönt si chüeler als uf Griechisch."),
 ("JHN.19.28", "volländet wird", "interpretive", "τελειωθῇ", None, ["erfüllt wird"], "Da staat τελειόω «vollände, as Ziel bringe», verwandt mit τετέλεσται, nöd s süsch üblich πληρόω «erfülle»."),
 ("JHN.19.30", "Es isch vollbracht", "traditional", "Τετέλεσται", "Es isch volländet worde", ["Es isch volländet", "Es isch erfüllt"], "Perfekt Passiv vo τελέω «z Änd füere, vollände»: öppis isch abgschlosse, und s Ergebnis bliibt. S Wort nimmt [[JHN.19.28]] uf und erinneret as Wärch, wo de Jesus söll vollände ([[JHN.4.34]], [[JHN.17.4]]). Es isch e Feschtstellig, kei Uusruef vo Erschöpfig. Was gnau vollbracht isch, beantworted d Uuslegigstraditione verschide. Redaktionelle Entscheid."),
 ("JHN.19.30", "hät de Geischt übergää", "literal", "παρέδωκεν τὸ πνεῦμα", None, ["isch gstorbe"], "S Verb isch παραδίδωμι, sus «uslifere»; da git de Jesus sälber sis Läbe häre (vgl. [[JHN.10.18]])."),
 ("JHN.19.35", "glaubed", "interpretive", "πιστεύητε", None, ["zum Glaube chömed"], "Präsens: wiiter glaube. Anderi Handschrifte händ de Aorist (lueg d Alternative); vgl. [[JHN.20.31]]."),
 ("JHN.19.39", "Pfund", "interpretive", "λίτρας", "Litre", None, "E λίτρα (s römisch Pfund) hät nach gängiger Aagab öppe 327 Gramm gwoge; hundert wäred rund 33 Kilo. D Umrächnig isch nöd gnau und i de Projektdate nöd belegt."),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-JHN-018-001-02:R2", "JHN.18.1", "des Baches Kidron", "des Baches der Zedern", "vom Bach Kidron", "vom Bach vo de Zedere", "gering",
  "τῶν Κέδρων «der Zedern» statt τοῦ Κεδρών «des Kidron».", "τῶν Κέδρων «vo de Zedere» statt τοῦ Κεδρών «vom Kidron».",
  {"R1": [("τοῦ Κεδρὼν", "des Kidron", None)], "R2": [("τῶν Κέδρων", "der Zedern", "WH, RP")]},
  {"R1": [("τοῦ Κεδρὼν", "vom Kidron", None)], "R2": [("τῶν Κέδρων", "vo de Zedere", "WH, RP")]},
  ["Der Name Kidron klingt im Griechischen wie der Genitiv Plural von κέδρος «Zeder»; Abschreiber konnten ihn so verstehen und den Artikel angleichen.",
   "Laut der automatischen Zuordnung lesen 01, 02, 032, 05 und 𝔓66 τοῦ (R1), 03 und 04 τῶν (R2)."],
  ["De Name Kidron tönt uf Griechisch wie «vo de Zedere» (κέδρος «Zeder»); Abschriiber händ en so chöne verstaa.",
   "Nach de automatische Zueornig läsed 01, 02, 032, 05 und 𝔓66 τοῦ, 03 und 04 τῶν."]),
 ("VAR-SBLGNTAPP-JHN-018-005-01:R2", "JHN.18.5", "Er sagt zu ihnen", "Jesus sagt zu ihnen", "Er seit zu ine", "De Jesus seit zu ine", "gering",
  "Der Sprecher wird ausdrücklich genannt.", "De Sprächer wird usdrücklich gnännt.",
  {"R1": [("αὐτοῖς", "zu ihnen", None)], "R2": [("αὐτοῖς ὁ Ἰησοῦς", "zu ihnen … Jesus", "RP")]},
  {"R1": [("αὐτοῖς", "zu ine", None)], "R2": [("αὐτοῖς ὁ Ἰησοῦς", "zu ine … de Jesus", "RP")]},
  ["Abschreiber haben den Sprecher oft ausdrücklich ergänzt.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 032, 04, 05 und 𝔓66 ohne den Namen; den Zusatz haben unter den erfassten Texten nur die gedruckten Ausgaben KJTR, RP und Stephanus."],
  ["Abschriiber händ de Sprächer oft ergänzt.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 032, 04, 05 und 𝔓66 ohni Name; de Zuesatz händ nu di druckte Usgabe KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-JHN-018-014-01:R2", "JHN.18.14", "für das Volk sterbe", "für das Volk umkomme", "für s Volk stirbt", "für s Volk umchunnt", "gering",
  "ἀπολέσθαι «umkommen» statt ἀποθανεῖν «sterben».", "ἀπολέσθαι «umchoo» statt ἀποθανεῖν «stärbe».",
  {"R1": [("ἀποθανεῖν", "sterben", None)], "R2": [("ἀπολέσθαι", "umkommen", None)]},
  {"R1": [("ἀποθανεῖν", "stärbe", None)], "R2": [("ἀπολέσθαι", "umchoo", None)]},
  ["In [[JHN.11.50]], auf das der Vers zurückverweist, steht ἀπόληται «umkommen» für das ganze Volk; ein Abschreiber kann das Wort von dort übernommen haben.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 04 und 𝔓66 ἀποθανεῖν, 02 ἀπολέσθαι; 05 hat hier keinen erfassten Text."],
  ["I [[JHN.11.50]] staat ἀπόληται «umchoo» fürs ganz Volk; en Abschriiber cha s Wort vo dört übernoo ha.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 04 und 𝔓66 ἀποθανεῖν, 02 ἀπολέσθαι."]),
 ("VAR-SBLGNTAPP-JHN-018-020-03:R2", "JHN.18.20", "wo alle Juden zusammenkommen", "wo die Juden immer zusammenkommen", "wo alli Jude zämechömed", "wo d Jude immer zämechömed", "gering",
  "πάντοτε «immer» statt πάντες «alle».", "πάντοτε «immer» statt πάντες «alli».",
  {"R1": [("πάντες", "alle", None)], "R2": [("πάντοτε", "immer", None)]},
  {"R1": [("πάντες", "alli", None)], "R2": [("πάντοτε", "immer", None)]},
  ["Die beiden Wörter unterscheiden sich nur in wenigen Buchstaben, und πάντοτε steht kurz vorher im selben Vers.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 032, 04 und 𝔓66 πάντες; πάντοτε haben unter den erfassten Texten nur die Ausgaben KJTR, RP und Stephanus."],
  ["Di beide Wörter underscheided sich nu i wenige Buechstabe, und πάντοτε staat churz vorher im gliiche Vers.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 032, 04 und 𝔓66 πάντες; πάντοτε händ nu KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-JHN-018-030-01:R2", "JHN.18.30", "dieser nicht Böses täte", "dieser nicht ein Übeltäter wäre", "dä nöd Böses tät", "dä nöd en Übeltäter wär", "gering",
  "Ein Wort (κακοποιός) statt zwei (κακὸν ποιῶν), gleicher Sinn.", "Eis Wort (κακοποιός) statt zwei, gliiche Sinn.",
  {"R1": [("κακὸν ποιῶν", "Böses tuend", None)], "R2": [("κακοποιός", "Übeltäter", None)]},
  {"R1": [("κακὸν ποιῶν", "Böses tue", None)], "R2": [("κακοποιός", "Übeltäter", None)]},
  ["κακοποιός ist das geläufigere Einzelwort für dieselbe Sache.",
   "Laut der automatischen Zuordnung lesen 03, 032, 04 und 𝔓66 κακὸν ποιῶν, 02 κακοποιός; 01 liest anders als beide erfassten Lesarten."],
  ["κακοποιός isch s gängiger Wort für di gliich Sach.",
   "Nach de automatische Zueornig läsed 03, 032, 04 und 𝔓66 κακὸν ποιῶν, 02 κακοποιός; 01 lisst anders."]),
 ("VAR-SBLGNTAPP-JHN-018-040-01:R2", "JHN.18.40", "Da schrien sie wieder", "Da schrien wieder alle", "Da händ si wider brüelet", "Da händ alli wider brüelet", "gering",
  "Mit «alle».", "Mit «alli».",
  {"R1": [("πάλιν", "wieder", "WH, NA28")], "R2": [("πάλιν πάντες", "wieder alle", "Treg, RP")]},
  {"R1": [("πάλιν", "wider", "WH, NA28")], "R2": [("πάλιν πάντες", "wider alli", "Treg, RP")]},
  ["Der Zusatz kann verdeutlichen, dass die ganze Menge schreit (vgl. [[MRK.15.13]]).",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 𝔓66 (Erstschrift) und 𝔓90 ohne «alle», 02 und die Korrektur in 𝔓66 mit ihm."],
  ["De Zuesatz cha verdüütliche, dass di ganz Mängi brüelet.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 𝔓66 (Erschtschrift) und 𝔓90 ohni «alli», 02 und d Korrektur in 𝔓66 mit."]),
 ("VAR-SBLGNTAPP-JHN-019-003-01:R2", "JHN.19.3", "Und sie traten zu ihm hin und sagten", "Und sie sagten", "Und si sind zu ihm häre choo und händ gseit", "Und si händ gseit", "gering",
  "Ohne «sie traten zu ihm hin».", "Ohni «si sind zu ihm häre choo».",
  {"R1": [("ἤρχοντο πρὸς αὐτὸν καὶ", "sie traten zu ihm hin und", None)], "R2": [("–", "(fehlt)", "RP")]},
  {"R1": [("ἤρχοντο πρὸς αὐτὸν καὶ", "si sind zu ihm häre choo und", None)], "R2": [("–", "(fäält)", "RP")]},
  ["Die Worte können beim Abschreiben ausgefallen sein, wenn der Blick von einem καί zum nächsten sprang; die kürzere Fassung kann auch die ältere sein und später ausgemalt worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 𝔓66 und 𝔓90 mit den Worten, 02 ohne sie."],
  ["D Wort chönd bim Abschriibe usgfalle sii; di chürzer Fassig cha au di elter sii.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 𝔓66 und 𝔓90 mit de Wort, 02 ohni."]),
 ("VAR-SBLGNTAPP-JHN-019-006-01:R2", "JHN.19.6", "kreuzige!»", "kreuzige ihn!»", "chrüüzig!»", "chrüüzig en!»", "gering",
  "Mit Objekt «ihn».", "Mit Objekt «en».",
  {"R1": [("σταύρωσον", "kreuzige", None)], "R2": [("σταύρωσον αὐτόν", "kreuzige ihn", "RP")]},
  {"R1": [("σταύρωσον", "chrüüzig", None)], "R2": [("σταύρωσον αὐτόν", "chrüüzig en", "RP")]},
  ["Das Objekt kann ergänzt sein, wie es in [[JHN.19.15]] steht.",
   "Laut der automatischen Zuordnung lesen 01 und 02 mit «ihn», 03, 032 und 𝔓90 ohne; 𝔓66 liest anders als beide erfassten Lesarten."],
  ["S Objekt cha ergänzt sii, wie s i [[JHN.19.15]] staat.",
   "Nach de automatische Zueornig läsed 01 und 02 mit «en», 03, 032 und 𝔓90 ohni; 𝔓66 lisst anders."]),
 ("VAR-SBLGNTAPP-JHN-019-007-01:R2", "JHN.19.7", "nach dem Gesetz muss er", "nach unserem Gesetz muss er", "nach em Gsetz mues er", "nach üsem Gsetz mues er", "gering",
  "Mit «unserem».", "Mit «üsem».",
  {"R1": [("νόμον", "Gesetz", None)], "R2": [("νόμον ἡμῶν", "unserem Gesetz", "RP")]},
  {"R1": [("νόμον", "Gsetz", None)], "R2": [("νόμον ἡμῶν", "üsem Gsetz", "RP")]},
  ["«Unser» verdeutlicht den Bezug auf das zuvor genannte Gesetz.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 𝔓66 ohne «unser», 02 mit ihm; 𝔓90 liest anders als beide erfassten Lesarten."],
  ["«Eus» verdüütlicht de Bezug.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 𝔓66 ohni «üs», 02 mit; 𝔓90 lisst anders."]),
 ("VAR-SBLGNTAPP-JHN-019-011-04:R2", "JHN.19.11", "mich dir ausgeliefert hat", "mich dir ausliefert", "mich dir usgliferet hät", "mich dir usliferet", "gering",
  "Präsens- statt Aoristpartizip.", "Präsens statt Vergangeheit.",
  {"R1": [("παραδούς", "der ausgeliefert hat", "WH, NA28")], "R2": [("παραδιδούς", "der ausliefert", "Treg, RP")]},
  {"R1": [("παραδούς", "wo usgliferet hät", "WH, NA28")], "R2": [("παραδιδούς", "wo usliferet", "Treg, RP")]},
  ["Die Formen unterscheiden sich in einer Silbe; das Präsens kann von der festen Bezeichnung des Judas als ὁ παραδιδούς ([[JHN.18.2]], [[JHN.18.5]]) beeinflusst sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 𝔓66 παραδούς, 02 und 032 παραδιδούς."],
  ["Di Forme underscheided sich i einere Silbe; s Präsens cha vo de Bezeichnig vom Judas ([[JHN.18.2]]) beiiflusst sii.",
   "Nach de automatische Zueornig läsed 01, 03 und 𝔓66 παραδούς, 02 und 032 παραδιδούς."]),
 ("VAR-SBLGNTAPP-JHN-019-016-02:R2", "JHN.19.16", "Sie übernahmen nun Jesus.", "Sie übernahmen nun Jesus und führten ihn ab.", "Si händ de Jesus also übernoo.", "Si händ de Jesus also übernoo und abgfüert.", "gering",
  "Mit Zusatz «und führten ihn ab».", "Mit Zuesatz «und abgfüert».",
  {"R1": [("Ἰησοῦν", "Jesus", None)], "R2": [("Ἰησοῦν καὶ ἤγαγον", "Jesus und führten ihn ab", "RP")]},
  {"R1": [("Ἰησοῦν", "de Jesus", None)], "R2": [("Ἰησοῦν καὶ ἤγαγον", "de Jesus und händ en abgfüert", "RP")]},
  ["Der knappe Satz wurde in der Überlieferung auf verschiedene Weise vervollständigt.",
   "Nach den CNTR-Transkriptionen hat 03 keinen Zusatz; 01, 02, 032 und 𝔓66 haben einen Zusatz mit ἀπήγαγον «führten ab», in verschiedenem Satzbau (deshalb ordnet die automatische Zuordnung sie keiner der beiden erfassten Lesarten zu). καὶ ἤγαγον haben unter den erfassten Texten die Ausgaben KJTR, RP und Stephanus."],
  ["De churz Satz isch i de Überliferig verschide ergänzt worde.",
   "Nach de CNTR-Transkriptione hät 03 kei Zuesatz; 01, 02, 032 und 𝔓66 händ en Zuesatz mit ἀπήγαγον «händ abgfüert», i verschidenem Satzbau. καὶ ἤγαγον händ KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-JHN-019-024-01:R2", "JHN.19.24", "erfüllt werden, die sagt", "erfüllt werden", "söle erfülle, wo seit", "söle erfülle", "gering",
  "Ohne «die sagt».", "Ohni «wo seit».",
  {"R1": [("ἡ λέγουσα", "die sagt", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  {"R1": [("ἡ λέγουσα", "wo seit", "Treg, NA28, RP")], "R2": [("–", "(fäält)", "WH")]},
  ["Die Einleitungsformel kann ergänzt oder als überflüssig weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne, 02, 032 und 𝔓66 mit «die sagt»."],
  ["D Iileitig cha ergänzt oder wäggloo worde sii.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni, 02, 032 und 𝔓66 mit «wo seit»."]),
 ("VAR-SBLGNTAPP-JHN-019-028-01:R2", "JHN.19.28", "da Jesus wusste", "da Jesus sah", "wil de Jesus gwüsst hät", "wil de Jesus gseh hät", "gering",
  "ἰδών «sehend» statt εἰδώς «wissend».", "ἰδών «gseh» statt εἰδώς «gwüsst».",
  {"R1": [("εἰδὼς", "wissend", None)], "R2": [("ἰδὼν", "sehend", "RP")]},
  {"R1": [("εἰδὼς", "gwüsst", None)], "R2": [("ἰδὼν", "gseh", "RP")]},
  ["Die beiden Formen unterscheiden sich nur in einem Buchstaben und klingen ähnlich.",
   "Laut der automatischen Zuordnung lesen 01, 02 und 032 εἰδώς, 03 und 𝔓66 ἰδών."],
  ["Di beide Forme underscheided sich nu i eim Buechstabe.",
   "Nach de automatische Zueornig läsed 01, 02 und 032 εἰδώς, 03 und 𝔓66 ἰδών."]),
 ("VAR-SBLGNTAPP-JHN-019-035-03:R2", "JHN.19.35", "auch ihr glaubt", "auch ihr zum Glauben kommt", "au ir glaubed", "au ir zum Glaube chömed", "mittel",
  "Aorist statt Präsens: «zum Glauben kommen» statt «glauben, im Glauben bleiben».", "Aorist statt Präsens: «zum Glaube choo» statt «wiiter glaube».",
  {"R1": [("πιστεύητε", "glaubt", "WH, Treg")], "R2": [("πιστεύσητε", "zum Glauben kommt", "NA28, RP")]},
  {"R1": [("πιστεύητε", "glaubed", "WH, Treg")], "R2": [("πιστεύσητε", "zum Glaube chömed", "NA28, RP")]},
  ["Die Formen unterscheiden sich in einem Buchstaben; dieselbe Unsicherheit besteht in [[JHN.20.31]]. Aus der Form allein lässt sich nicht sicher ableiten, ob die Angesprochenen schon glauben.",
   "Laut der automatischen Zuordnung lesen 01 (Erstschrift), 03 und 𝔓66 πιστεύητε, die Korrektur in 01 sowie 02 und 032 πιστεύσητε."],
  ["Di Forme underscheided sich i eim Buechstabe; di gliich Unsicherheit git s i [[JHN.20.31]].",
   "Nach de automatische Zueornig läsed 01 (Erschtschrift), 03 und 𝔓66 πιστεύητε, d Korrektur in 01 sowie 02 und 032 πιστεύσητε."]),
 ("VAR-SBLGNTAPP-JHN-019-039-02:R2", "JHN.19.39", "eine Mischung", "eine Rolle", "e Mischig", "e Rolle", "gering",
  "ἕλιγμα «Rolle, Bündel» statt μίγμα «Mischung».", "ἕλιγμα «Rolle, Bündel» statt μίγμα «Mischig».",
  {"R1": [("μίγμα", "Mischung", "Treg, NA28, RP")], "R2": [("ἕλιγμα", "Rolle", "WH")]},
  {"R1": [("μίγμα", "Mischig", "Treg, NA28, RP")], "R2": [("ἕλιγμα", "Rolle", "WH")]},
  ["Die beiden Wörter sehen sich im Schriftbild ähnlich; μίγμα passt zur Aufzählung zweier Stoffe, ἕλιγμα ist das seltenere Wort.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 032 ἕλιγμα, 02 und 𝔓66 μίγμα. Der SBLGNT folgt hier Treg, NA28 und RP gegen WH."],
  ["Di beide Wörter gsehnd sich im Schriftbild ähnlich.",
   "Nach de automatische Zueornig läsed 01, 03 und 032 ἕλιγμα, 02 und 𝔓66 μίγμα. De SBLGNT folgt da Treg, NA28 und RP."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-018-001-040", "JHN.18.1-JHN.18.40", "section", "Gefangennahme, Verhör und Verleugnung, Jesus vor Pilatus",
  ["TU-JHN-018-001-011", "TU-JHN-018-012-014", "TU-JHN-018-015-018", "TU-JHN-018-019-024", "TU-JHN-018-025-027",
   "TU-JHN-018-028-032", "TU-JHN-018-033-038", "TU-JHN-018-039-040"],
  "Im Garten jenseits des Kidron kommt Judas mit einer Kohorte und Dienern der Hohepriester und Pharisäer. Jesus geht hinaus, fragt, wen sie suchen, und antwortet «Ich bin es»; sie weichen zurück und fallen zu Boden. Er verlangt, seine Jünger gehen zu lassen, und weist Petrus zurecht, der einem Knecht des Hohepriesters das Ohr abgehauen hat. Jesus wird gefesselt und zu Hannas geführt; der Hohepriester befragt ihn, Jesus verweist auf sein öffentliches Reden und wird geschlagen, dann wird er zu Kajafas geschickt. Unterdessen leugnet Petrus im Hof dreimal, ein Jünger Jesu zu sein, und ein Hahn kräht. Am Morgen wird Jesus ins Prätorium gebracht. Pilatus verhört ihn; Jesus sagt, sein Reich sei nicht aus dieser Welt und er sei gekommen, der Wahrheit Zeugnis zu geben. Pilatus findet keine Schuld an ihm und bietet an, ihn zum Passa freizulassen; sie schreien nach Barabbas.", SEG),
 ("TU-JHN-018-001-011", "JHN.18.1-JHN.18.11", "narrative", "Die Gefangennahme im Garten", None,
  "Judas führt eine Kohorte und Diener der Hohepriester und Pharisäer in den Garten, in dem Jesus oft mit seinen Jüngern gewesen war. Jesus, der weiss, was auf ihn zukommt, geht hinaus und fragt, wen sie suchen. Auf seine Antwort «Ich bin es» weichen sie zurück und fallen zu Boden. Er verlangt, seine Jünger gehen zu lassen; so erfüllt sich sein Wort, keinen von ihnen verloren zu haben. Simon Petrus haut Malchus, dem Knecht des Hohepriesters, das rechte Ohr ab; Jesus heisst ihn das Schwert einstecken, denn er will den Becher trinken, den der Vater ihm gegeben hat.", None),
 ("TU-JHN-018-012-014", "JHN.18.12-JHN.18.14", "narrative", "Jesus wird zu Hannas geführt", None,
  "Die Kohorte, ihr Oberst und die Diener der Juden nehmen Jesus fest, fesseln ihn und führen ihn zuerst zu Hannas, dem Schwiegervater des Hohepriesters Kajafas. Der Erzähler erinnert daran, dass Kajafas geraten hatte, es sei besser, dass ein Mensch für das Volk stirbt.", None),
 ("TU-JHN-018-015-018", "JHN.18.15-JHN.18.18", "narrative", "Petrus verleugnet Jesus zum ersten Mal", None,
  "Simon Petrus und ein anderer Jünger, der mit dem Hohepriester bekannt ist, folgen Jesus; dieser Jünger bringt Petrus in den Hof. Die Türhüterin fragt Petrus, ob er auch einer der Jünger dieses Menschen sei; er sagt: «Ich bin es nicht.» Dann steht er bei den Knechten und Dienern am Kohlenfeuer und wärmt sich.", None),
 ("TU-JHN-018-019-024", "JHN.18.19-JHN.18.24", "narrative", "Verhör vor dem Hohepriester", None,
  "Der Hohepriester befragt Jesus über seine Jünger und seine Lehre. Jesus antwortet, er habe offen in Synagoge und Tempel geredet; man solle die fragen, die ihn gehört haben. Ein Diener schlägt ihn ins Gesicht; Jesus fragt, warum er ihn schlägt, wenn er recht geredet hat. Hannas schickt ihn gefesselt zu Kajafas.", None),
 ("TU-JHN-018-025-027", "JHN.18.25-JHN.18.27", "narrative", "Petrus verleugnet Jesus zum zweiten und dritten Mal", None,
  "Am Feuer gefragt, ob er zu den Jüngern Jesu gehöre, leugnet Petrus erneut. Ein Verwandter des Mannes, dem Petrus das Ohr abgehauen hatte, fragt, ob er ihn nicht im Garten gesehen habe; Petrus leugnet wieder, und sogleich kräht ein Hahn.", None),
 ("TU-JHN-018-028-032", "JHN.18.28-JHN.18.32", "narrative", "Die Ankläger vor Pilatus", None,
  "Früh am Morgen wird Jesus von Kajafas ins Prätorium geführt. Die Ankläger bleiben draussen, um nicht unrein zu werden und das Passa essen zu können. Pilatus fragt nach der Anklage; sie antworten, sie hätten ihn nicht ausgeliefert, wenn er nicht Böses täte. Als Pilatus sie auffordert, ihn nach ihrem Gesetz zu richten, sagen die Juden, sie dürften niemanden töten. Der Erzähler sieht darin Jesu Wort über die Art seines Todes erfüllt.", None),
 ("TU-JHN-018-033-038", "JHN.18.33-JHN.18.38", "narrative", "Jesus und Pilatus: Königtum und Wahrheit", None,
  "Pilatus fragt Jesus, ob er der König der Juden sei. Jesus fragt zurück, ob die Frage von ihm selbst komme; Pilatus verweist auf Jesu Volk und die Hohepriester, die ihn ausgeliefert haben. Jesus sagt, sein Reich sei nicht aus dieser Welt, sonst würden seine Diener kämpfen. Auf die Frage, ob er also doch ein König sei, antwortet er: «Du sagst, dass ich ein König bin», und sagt, er sei geboren und in die Welt gekommen, um der Wahrheit Zeugnis zu geben. Pilatus fragt: «Was ist Wahrheit?», geht hinaus und erklärt den Juden, er finde keine Schuld an ihm.", None),
 ("TU-JHN-018-039-040", "JHN.18.39-JHN.18.40", "narrative", "Barabbas", None,
  "Pilatus bietet an, ihnen nach dem Brauch zum Passa den König der Juden freizulassen. Sie schreien: nicht diesen, sondern Barabbas. Barabbas war ein Räuber.", None),
 ("TU-JHN-019-001-042", "JHN.19.1-JHN.19.42", "section", "Verurteilung, Kreuzigung, Tod und Begräbnis Jesu",
  ["TU-JHN-019-001-003", "TU-JHN-019-004-007", "TU-JHN-019-008-012", "TU-JHN-019-013-016", "TU-JHN-019-017-022",
   "TU-JHN-019-023-024", "TU-JHN-019-025-027", "TU-JHN-019-028-030", "TU-JHN-019-031-037", "TU-JHN-019-038-042"],
  "Pilatus lässt Jesus geisseln; Soldaten verspotten ihn mit Dornenkranz und Purpurmantel als König der Juden. Jesus wird hinausgeführt («Seht, der Mensch!»), und Pilatus erklärt erneut, er finde keine Schuld an ihm; die Hohepriester und Diener fordern die Kreuzigung, die Juden berufen sich darauf, dass er sich zum Sohn Gottes gemacht habe. Pilatus spricht noch einmal mit Jesus über seine Vollmacht und sucht ihn freizulassen, als die Juden ihm vorhalten, er sei sonst nicht Freund des Kaisers, führt er Jesus hinaus und setzt sich auf den Richterstuhl. Am Rüsttag des Passa, um die sechste Stunde, nachdem die Hohepriester erklärt haben, sie hätten keinen König ausser dem Kaiser, liefert er ihn zur Kreuzigung aus. Jesus trägt sein Kreuz selbst nach Golgota und wird zwischen zwei anderen gekreuzigt; die Tafel nennt ihn in drei Sprachen König der Juden. Die Soldaten teilen seine Kleider und losen um das Untergewand. Jesus vertraut seine Mutter und den Jünger, den er liebte, einander an. Er sagt «Mich dürstet», nimmt den Essig, spricht «Es ist vollbracht» und übergibt den Geist. Ein Soldat stösst ihm eine Lanze in die Seite, Blut und Wasser kommen heraus; der Erzähler beruft sich auf das Zeugnis dessen, der es gesehen hat, und auf zwei Schriftworte. Josef von Arimatäa und Nikodemus binden den Leib mit Duftstoffen in Leinenbinden und legen ihn in ein neues Grab in einem Garten.", SEG),
 ("TU-JHN-019-001-003", "JHN.19.1-JHN.19.3", "narrative", "Geisselung und Verspottung", None,
  "Pilatus lässt Jesus geisseln. Die Soldaten setzen ihm einen Dornenkranz auf, legen ihm einen purpurnen Mantel um, grüssen ihn als König der Juden und schlagen ihn ins Gesicht.", None),
 ("TU-JHN-019-004-007", "JHN.19.4-JHN.19.7", "narrative", "«Seht, der Mensch!»", None,
  "Pilatus geht hinaus und kündigt an, er bringe Jesus heraus, damit sie erkennen, dass er keine Schuld an ihm findet. Jesus kommt mit Dornenkranz und Purpurmantel heraus, und es heisst: «Seht, der Mensch!» Die Hohepriester und Diener schreien «Kreuzige!»; Pilatus sagt, sie sollten ihn selbst kreuzigen, er finde keine Schuld an ihm. Die Juden antworten, nach ihrem Gesetz müsse er sterben, weil er sich zum Sohn Gottes gemacht habe.", None),
 ("TU-JHN-019-008-012", "JHN.19.8-JHN.19.12", "narrative", "Vollmacht von oben", None,
  "Pilatus fürchtet sich noch mehr und fragt Jesus im Prätorium, woher er sei; Jesus gibt keine Antwort. Als Pilatus auf seine Vollmacht hinweist, antwortet Jesus, er hätte keine über ihn, wenn es ihm nicht von oben gegeben wäre; wer ihn ausgeliefert habe, habe grössere Sünde. Pilatus sucht ihn freizulassen, doch die Juden schreien, dann sei er nicht Freund des Kaisers.", None),
 ("TU-JHN-019-013-016", "JHN.19.13-JHN.19.16", "narrative", "Die Verurteilung", None,
  "Pilatus führt Jesus hinaus und setzt sich auf den Richterstuhl am Ort, der Steinpflaster, auf Hebräisch Gabbata, heisst. Es ist der Rüsttag des Passa, um die sechste Stunde. Er sagt zu den Juden: «Seht, euer König!» Sie schreien: «Weg mit ihm, kreuzige ihn!», und die Hohepriester erklären: «Wir haben keinen König ausser den Kaiser.» Da liefert Pilatus ihn zur Kreuzigung aus, und sie übernehmen Jesus.", None),
 ("TU-JHN-019-017-022", "JHN.19.17-JHN.19.22", "narrative", "Kreuzigung und Aufschrift", None,
  "Jesus trägt sein Kreuz selbst zur Schädelstätte, Golgota, und wird dort zwischen zwei anderen gekreuzigt. Pilatus schreibt eine Tafel und bringt sie am Kreuz an: «Jesus, der Nazoräer, der König der Juden», auf Hebräisch, Lateinisch und Griechisch; viele Juden lesen sie. Die Hohepriester verlangen, er solle stattdessen schreiben, Jesus habe gesagt: «Ich bin König der Juden»; Pilatus antwortet: «Was ich geschrieben habe, habe ich geschrieben.»", None),
 ("TU-JHN-019-023-024", "JHN.19.23-JHN.19.24", "narrative", "Die Kleider Jesu", None,
  "Die Soldaten teilen seine Kleider in vier Teile und losen um das Untergewand, das ohne Naht in einem Stück gewebt ist. Der Erzähler sieht darin [[PSA.22.18]] erfüllt.", None),
 ("TU-JHN-019-025-027", "JHN.19.25-JHN.19.27", "narrative", "Die Mutter Jesu und der Jünger", None,
  "Beim Kreuz stehen Jesu Mutter, die Schwester seiner Mutter, Maria, die (Frau) des Klopas, und Maria aus Magdala. Jesus sagt zu seiner Mutter, der Jünger, den er liebte, sei ihr Sohn, und zum Jünger, sie sei seine Mutter. Von da an nimmt der Jünger sie zu sich.", None),
 ("TU-JHN-019-028-030", "JHN.19.28-JHN.19.30", "narrative", "Der Tod Jesu", None,
  "Im Wissen, dass schon alles vollbracht ist, sagt Jesus «Mich dürstet», damit die Schrift vollendet würde. Man hält ihm einen Schwamm mit Essig auf einem Ysopzweig an den Mund. Als er den Essig genommen hat, sagt er «Es ist vollbracht», neigt das Haupt und übergibt den Geist.", None),
 ("TU-JHN-019-031-037", "JHN.19.31-JHN.19.37", "narrative", "Der Lanzenstich", None,
  "Weil Rüsttag ist und die Leiber am grossen Sabbat nicht am Kreuz bleiben sollen, bitten die Juden Pilatus, den Gekreuzigten die Beine brechen und sie abnehmen zu lassen. Die Soldaten brechen den beiden anderen die Beine; Jesus ist schon tot, deshalb brechen sie ihm die Beine nicht, aber einer stösst ihm eine Lanze in die Seite, und Blut und Wasser kommen heraus. Der Erzähler beruft sich auf das wahre Zeugnis dessen, der es gesehen hat, damit auch die Angesprochenen glauben, und führt zwei Schriftworte an.", None),
 ("TU-JHN-019-038-042", "JHN.19.38-JHN.19.42", "narrative", "Das Begräbnis", None,
  "Josef von Arimatäa, aus Furcht vor den Juden ein heimlicher Jünger, bittet Pilatus um den Leib Jesu und nimmt ihn ab. Nikodemus bringt etwa hundert Pfund Myrrhe und Aloe. Sie binden den Leib mit den Duftstoffen in Leinenbinden, wie es bei den Juden Brauch ist, und legen ihn wegen des Rüsttags in ein nahes, neues Grab in einem Garten beim Ort der Kreuzigung.", None),
]
UNITS_GSW = {
 "TU-JHN-018-001-040": ("Gfangenaam, Verhör und Verleugnig, de Jesus vor em Pilatus", "Im Garte ännet em Kidron chunnt de Judas mit ere Kohorte und mit Diener vo de Hoheprieschter und Pharisäer. De Jesus gaat use, fröget, wän si sueched, und antwortet «Ich bi s»; si wiiched zrugg und gheied a Bode. Er verlangt, dass mer sini Jünger laat gaa, und wiist de Petrus zrächt, wo eme Chnächt vom Hoheprieschter s Oor abghaue hät. De Jesus wird gfesslet und zum Hannas gfüert; de Hoheprieschter fröget en uus, de Jesus verwiist uf sis öffentlich Rede und wird gschlage, dänn wird er zum Kajafas gschickt. Underdesse strittet de Petrus im Hof drüümal ab, en Jünger vom Jesus z sii, und en Güggel chräit. Am Morge wird de Jesus is Prätorium bracht. De Pilatus verhört en; de Jesus seit, sis Riich sig nöd us dere Wält und er sig choo, zum d Wahrheit bezüüge. De Pilatus findt kei Schuld a ihm und bietet aa, en zum Passa freizlaa; si brüeled nach em Barabbas."),
 "TU-JHN-018-001-011": ("D Gfangenaam im Garte", "De Judas füert e Kohorte und Diener vo de Hoheprieschter und Pharisäer i de Garte, wo de Jesus oft mit sine Jünger gsii isch. De Jesus, wo weiss, was uf en zuechunnt, gaat use und fröget, wän si sueched. Uf sini Antwort «Ich bi s» wiiched si zrugg und gheied a Bode. Er verlangt, dass mer sini Jünger laat gaa; eso erfüllt sich sis Wort, er heig keine vo ine verlore. De Simon Petrus haut em Malchus, em Chnächt vom Hoheprieschter, s rächt Oor ab; de Jesus seit em, er söll s Schwärt iistecke, dänn er wott de Bächer trinke, wo em de Vatter gää hät."),
 "TU-JHN-018-012-014": ("De Jesus wird zum Hannas gfüert", "D Kohorte, ire Oberscht und d Diener vo de Jude nämed de Jesus fescht, fessled en und füered en zerscht zum Hannas, em Schwiegervatter vom Hoheprieschter Kajafas. De Erzäller erinneret dra, dass de Kajafas graate hät, es sig besser, wänn ein Mänsch für s Volk stirbt."),
 "TU-JHN-018-015-018": ("De Petrus verleugnet de Jesus s erscht Mal", "De Simon Petrus und en andere Jünger, wo mit em Hoheprieschter bekannt isch, gönd em Jesus nache; dä Jünger bringt de Petrus in Hof. D Tüürhüeteri fröget de Petrus, öb er au eine vo de Jünger vo däm Mänsch sig; er seit: «Ich bi s nöd.» Dänn staat er bi de Chnächt und Diener am Cholefüür und wärmt sich."),
 "TU-JHN-018-019-024": ("Verhör vor em Hoheprieschter", "De Hoheprieschter fröget de Jesus über sini Jünger und sini Lehr uus. De Jesus antwortet, er heig offe i de Synagoge und im Tämpel gredt; mer söll die fröge, wo zueglost händ. En Diener git em e Ohrfiige; de Jesus fröget, werum er en schlaat, wänn er rächt gredt hät. De Hannas schickt en gfesslet zum Kajafas."),
 "TU-JHN-018-025-027": ("De Petrus verleugnet de Jesus s zweit und s dritt Mal", "Am Füür gfröget, öb er zu de Jünger vom Jesus ghöri, strittet de Petrus wider ab. En Verwandte vo däm, wo de Petrus s Oor abghaue hät, fröget, öb er en nöd im Garte gseh heig; de Petrus strittet s wider ab, und grad chräit en Güggel."),
 "TU-JHN-018-028-032": ("D Aakläger vor em Pilatus", "Früe am Morge wird de Jesus vom Kajafas is Prätorium gfüert. D Aakläger bliibed dusse, demit si nöd unrein wärded und s Passa chönd ässe. De Pilatus fröget nach de Aaklag; si säged, si hetted en nöd usgliferet, wänn er nöd Böses tät. Wo de Pilatus seit, si söled en nach irem Gsetz richte, säged d Jude, si dörfed niemer töte. De Erzäller gseht drin s Wort vom Jesus erfüllt, wie er stärbe würd."),
 "TU-JHN-018-033-038": ("De Jesus und de Pilatus: König und Wahrheit", "De Pilatus fröget de Jesus, öb er de König vo de Jude sig. De Jesus fröget zrugg, öb d Frag vo ihm sälber chömi; de Pilatus verwiist uf s Volk vom Jesus und d Hoheprieschter, wo en usgliferet händ. De Jesus seit, sis Riich sig nöd us dere Wält, süsch würded sini Diener kämpfe. Uf d Frag, öb er also doch en König sig, antwortet er: «Du seisch, dass ich en König bi», und seit, er sig gebore und i d Wält choo, zum d Wahrheit bezüüge. De Pilatus fröget: «Was isch Wahrheit?», gaat use und seit de Jude, er find kei Schuld a ihm."),
 "TU-JHN-018-039-040": ("De Barabbas", "De Pilatus bietet aa, ine nach em Bruuch zum Passa de König vo de Jude freizlaa. Si brüeled: nöd dä, sondern de Barabbas. De Barabbas isch en Röiber gsii."),
 "TU-JHN-019-001-042": ("Verurteilig, Chrüüzigung, Tod und Begräbnis vom Jesus", "De Pilatus laat de Jesus gisle; Soldate verspotted en mit Dornechranz und Purpurmantel als König vo de Jude. De Jesus wird usegfüert («Lueged, de Mänsch!»), und de Pilatus seit nomal, er find kei Schuld a ihm; d Hoheprieschter und d Diener verlanged d Chrüüzigung, d Jude beruefed sich druf, dass er sich zum Sohn vo Gott gmacht heig. De Pilatus redt nomal mit em Jesus über sini Vollmacht und probiert, en freizlaa, wo d Jude em vorhebed, er sig süsch nöd de Fründ vom Kaiser, füert er de Jesus use und setzt sich uf de Richterstuel. Am Rüschttag vom Passa, öppe i de sächste Stund, nachdem d Hoheprieschter gseit händ, si heiged kei König usser em Kaiser, liferet er en zur Chrüüzigung us. De Jesus treit sis Chrüüz sälber uf Golgota und wird zwüsche zwei andere gchrüüziget; d Tafele nännt en i drüü Spraache König vo de Jude. D Soldate teiled sini Chleider und losed ums Undergwand. De Jesus vertrout sini Mueter und de Jünger, wo er gliebt hät, enand aa. Er seit «Ich han Durscht», nimmt de Essig, seit «Es isch vollbracht» und übergit de Geischt. En Soldat sticht em mit ere Lanze i d Siite, Bluet und Wasser chömed use; de Erzäller beruft sich uf s Zügnis vo däm, wo s gseh hät, und uf zwei Schriftwort. De Josef vo Arimatäa und de Nikodemus wickled de Liib mit Duftstoff i Liinebinde und legged en in es nöis Grab in eme Garte."),
 "TU-JHN-019-001-003": ("Gislig und Spott", "De Pilatus laat de Jesus gisle. D Soldate setzed em en Dornechranz uf, legged em en purpurrote Mantel um, grüessed en als König vo de Jude und gänd em Ohrfiige."),
 "TU-JHN-019-004-007": ("«Lueged, de Mänsch!»", "De Pilatus gaat use und seit, er bringi de Jesus use, demit si erchänned, dass er kei Schuld a ihm findt. De Jesus chunnt mit Dornechranz und Purpurmantel use, und es heisst: «Lueged, de Mänsch!» D Hoheprieschter und d Diener brüeled «Chrüüzig!»; de Pilatus seit, si söled en sälber chrüüzige, er find kei Schuld a ihm. D Jude antworted, nach em Gsetz mües er stärbe, wil er sich zum Sohn vo Gott gmacht heig."),
 "TU-JHN-019-008-012": ("Vollmacht vo obe", "De Pilatus überchunnt no meh Angscht und fröget de Jesus im Prätorium, vo wo er sig; de Jesus git kei Antwort. Wo de Pilatus uf sini Vollmacht hiiwiist, antwortet de Jesus, er hett kei über ihn, wänn s em nöd vo obe gää worde wär; wer en usgliferet heig, heig di grösser Sünd. De Pilatus probiert, en freizlaa, aber d Jude brüeled, dänn sig er nöd de Fründ vom Kaiser."),
 "TU-JHN-019-013-016": ("D Verurteilig", "De Pilatus füert de Jesus use und setzt sich uf de Richterstuel a däm Ort, wo Steipflaschter, uf Hebräisch Gabbata, heisst. Es isch de Rüschttag vom Passa, öppe di sächst Stund. Er seit zu de Jude: «Lueged, eue König!» Si brüeled: «Wäg mit em, chrüüzig en!», und d Hoheprieschter säged: «Mir händ kei König usser em Kaiser.» Da liferet de Pilatus en zur Chrüüzigung us, und si übernämed de Jesus."),
 "TU-JHN-019-017-022": ("Chrüüzigung und Ufschrift", "De Jesus treit sis Chrüüz sälber zum Schädelplatz, Golgota, und wird dört zwüsche zwei andere gchrüüziget. De Pilatus schriibt e Tafele und macht si am Chrüüz aa: «Jesus, de Nazoräer, de König vo de Jude», uf Hebräisch, Latiinisch und Griechisch; vili Jude läsed si. D Hoheprieschter verlanged, er söll statt däm schriibe, de Jesus heig gseit: «Ich bi König vo de Jude»; de Pilatus antwortet: «Was ich gschribe han, han ich gschribe.»"),
 "TU-JHN-019-023-024": ("D Chleider vom Jesus", "D Soldate teiled sini Chleider i vier Teil und losed ums Undergwand, wo ohni Naht i eim Stuck gwobe isch. De Erzäller gseht drin [[PSA.22.18]] erfüllt."),
 "TU-JHN-019-025-027": ("D Mueter vom Jesus und de Jünger", "Bim Chrüüz stönd d Mueter vom Jesus, d Schwöschter vo sinere Mueter, d Maria, d (Frau) vom Klopas, und d Maria vo Magdala. De Jesus seit zu sinere Mueter, de Jünger, wo er gliebt hät, sig ire Sohn, und zum Jünger, si sig sini Mueter. Vo da aa nimmt de Jünger si zu sich."),
 "TU-JHN-019-028-030": ("De Tod vom Jesus", "De Jesus weiss, dass scho alles vollbracht isch, und seit «Ich han Durscht», demit d Schrift volländet wird. Mer hebt em en Schwamm mit Essig uf eme Ysopzwiig a de Mund. Wo er de Essig gnoo hät, seit er «Es isch vollbracht», neigt de Chopf und übergit de Geischt."),
 "TU-JHN-019-031-037": ("De Lanzestich", "Wil Rüschttag isch und d Liiber am grosse Sabbat nöd am Chrüüz söled bliibe, bitted d Jude de Pilatus, er söll de Gchrüüzigte d Bei bräche und si abnää la. D Soldate bräched de beide andere d Bei; de Jesus isch scho tot, drum bräched si ihm d Bei nöd, aber eine sticht em mit ere Lanze i d Siite, und Bluet und Wasser chömed use. De Erzäller beruft sich uf s wahr Zügnis vo däm, wo s gseh hät, demit au di Aagsprochne glaubed, und füert zwei Schriftwort aa."),
 "TU-JHN-019-038-042": ("S Begräbnis", "De Josef vo Arimatäa, us Angscht vor de Jude en heimliche Jünger, bittet de Pilatus um de Liib vom Jesus und nimmt en ab. De Nikodemus bringt öppe hundert Pfund Myrrhe und Aloe. Si wickled de Liib mit de Duftstoff i Liinebinde, wie s bi de Jude de Bruuch isch, und legged en wäge em Rüschttag in es nööchs, nöis Grab in eme Garte bim Ort vo de Chrüüzigung."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("Die Grundentscheide für das ganze Johannesevangelium stehen bei Johannes 1–3 (scripts/authoring/johannes_text_01_03.py) "
  "und gelten hier unverändert: κόσμος «Welt», ἀλήθεια «Wahrheit», μένω «bleiben», ἄνωθεν mit Doppelsinn «von oben/von neuem» "
  "(hier [[JHN.19.11]] «von oben»), ἐγώ εἰμι «Ich bin …» – als Antwort auf eine Frage «Ich bin es» mit Hinweis auf den "
  "Doppelsinn ([[JHN.18.5]]–[[JHN.18.8]])."),
 ("οἱ Ἰουδαῖοι ist durchgehend wörtlich mit «die Juden» wiedergegeben. In Johannes 18–19 sind damit meist die jüdischen "
  "Behörden in Jerusalem gemeint, nicht das jüdische Volk insgesamt; Jesus und seine Jünger sind selbst Juden. Die "
  "Wiedergabe ist eine Deutungsentscheidung; die Alternative «die jüdischen Führer» ist bei [[JHN.18.12]] genannt."),
 ("παραδίδωμι ist durchgehend mit «ausliefern» wiedergegeben, in [[JHN.19.30]] mit «übergab (den Geist)». τετέλεσται "
  "([[JHN.19.28]], [[JHN.19.30]]) ist beide Male «vollbracht». οὖν, bei Johannes ein häufiges erzählendes Bindewort, ist mit "
  "«nun», «da» oder «also» wiedergegeben; λέγων/λέγοντες und ὅτι vor direkter Rede sind nicht eigens übersetzt. Johannes "
  "erzählt oft im Präsens («er sagt»); das ist beibehalten."),
 ("Handschriftenbefund aus den Daten: CNTR-Transkriptionen von 01, 02, 03, 032 und 𝔓66 liegen für alle Verse von Johannes "
  "18–19 vor (𝔓66 mit beschädigten Stellen), von 04 für [[JHN.18.1]]–[[JHN.18.36]], von 05 für [[JHN.18.1]]–[[JHN.18.13]], "
  "von 𝔓108 für [[JHN.18.1]]–[[JHN.18.5]], von 𝔓90 für [[JHN.18.36]]–[[JHN.19.7]] und von 𝔓121 für [[JHN.19.17]]–"
  "[[JHN.19.18]] und [[JHN.19.25]]–[[JHN.19.26]]. Die CNTR-Transkription von 𝔓52 enthält Text zu [[JHN.18.31]]–"
  "[[JHN.18.33]] und [[JHN.18.37]]–[[JHN.18.38]]; ein grosser Teil davon ist dort als beschädigt oder ergänzt markiert. "
  "Datierungen der Handschriften sind hier nicht angegeben, weil sie nicht aus den Projektdaten stammen."),
 "In Johannes 18–19 fehlt im SBLGNT kein Vers.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("D Grundentscheid fürs ganz Johannesevangelium stönd bi Johannes 1–3 (scripts/authoring/johannes_text_01_03.py): "
  "κόσμος «Wält», ἀλήθεια «Wahrheit», μένω «bliibe», ἐγώ εἰμι «Ich bi …», als Antwort «Ich bi s» ([[JHN.18.5]]–[[JHN.18.8]])."),
 ("οἱ Ἰουδαῖοι isch überall wörtlich «d Jude». I Johannes 18–19 sind meischtens di jüdische Behörde z Jerusalem gmeint, "
  "nöd s ganz jüdisch Volk; das isch e Düütigsentscheid (lueg bi [[JHN.18.12]])."),
 ("De Text vo 𝔓52 i de CNTR-Transkription ghört zu [[JHN.18.31]]–[[JHN.18.33]] und [[JHN.18.37]]–[[JHN.18.38]]; vil "
  "devo isch dört als beschädigt oder ergänzt markiert."),
]


def run():
    import json
    n = 0
    if not (D / "works" / "WORK-JHN.json").exists():
        raise SystemExit("WORK-JHN fehlt")
    for uid, rng, kind, title, parts, summary, seg in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-JHN", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}), "segmentation_note_de": seg,
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        rec = {k: v for k, v in rec.items() if v is not None}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      AUTH_GSW_L10N, DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-jhn").glob("*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-JHN-{c:03d}.json")
        refs_c = [f"JHN.{c}.{v}" for v in range(1, last + 1) if f"JHN.{c}.{v}" in toks]
        if len(refs_c) != last:
            raise SystemExit(f"Kapitel {c}: Verse ohne Tokens – Liste prüfen")
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-JHN-{c:03d}-001-{last:03d}-{code}-WORKING"
            dec = [{"reference": r, "target": tg, "kind": kd, "grc": grc, **({"more_literal": ml} if ml else {}),
                    **({"other_options": oo} if oo else {}), **({"note": nt} if nt else {})}
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
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"JHN.{c}.1-JHN.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Riich, Liib), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-JHN-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; historisches Präsens beibehalten. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
            aid = f"ALIGN-JHN-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"JHN.{c}.1-JHN.{c}.{last}",
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/johannes_text_18_19.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 18–19 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
