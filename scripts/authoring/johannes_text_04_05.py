#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 4–5 (Samarien, zweites Zeichen in Kana, Heilung am Teich Betesda, Rede über den Sohn) –
Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen,
Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_04_05.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben. Die Grundentscheide für die johanneischen
Schlüsselwörter sind in scripts/authoring/johannes_text_01_03.py begründet und hier übernommen.

Besonderheiten:
- [[JHN.5.4]] fehlt im SBLGNT (keine Tokens); der Vers erhält keinen Text. Der Zusatz am Ende von [[JHN.5.3]] und
  der Wortlaut von Vers 4 stehen als Alternative bei [[JHN.5.3]] (wie [[MRK.15.28]] in markus_text_14_16.py).
  Weil die automatische Kollation (Fenster um ξηρῶν) den Zusatz nicht erfasst, stützen sich die Handschriftenangaben
  dort auf die CNTR-Transkriptionen selbst.
- ἤδη am Ende von [[JHN.4.35]] gehört nach der Zeichensetzung des SBLGNT zum folgenden Satz ([[JHN.4.36]]).

KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1)
bzw. aus der CNTR-Transkription (Sekundärtranskription), nicht aus eigener Prüfung der Handschriften.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, write  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-JOHN"]
CHAPTERS = ((4, 54), (5, 47))

DE = {
 # ------------------------------------------------------------ Kapitel 4
 "JHN.4.1": "[Als]{1} [nun]{2} [Jesus]{4,5} [erfuhr]{3}, [dass]{6} [die Pharisäer]{8,9} [gehört hatten]{7}, [dass]{10} [Jesus]{11} [mehr]{12} [Jünger]{13} [gewinne]{14} und{15} [taufe]{16} [als]{17} [Johannes]{18} –",
 "JHN.4.2": "– [obwohl]{1} [Jesus]{2} [selbst]{3} [nicht]{4} [taufte]{5}, [sondern]{6} [seine]{9} [Jünger]{7,8} –,",
 "JHN.4.3": "[verliess er]{1} [Judäa]{2,3} und{4} [ging]{5} [wieder]{6} [nach]{7} [Galiläa]{8,9}.",
 "JHN.4.4": "[Er]{3} [musste]{1} [aber]{2} [durch]{5} [Samarien]{6,7} [ziehen]{4}.",
 "JHN.4.5": "[Er kommt]{1} [nun]{2} [in]{3} [eine Stadt]{4} [Samariens]{5,6}, [die]{7} [Sychar]{8} [heisst]{7}, [nahe]{9} [bei dem]{10} [Grundstück]{11}, [das]{12} [Jakob]{14} [seinem]{17,19} [Sohn]{18} [Josef]{15,16} [gegeben hatte]{13}.",
 "JHN.4.6": "[Dort]{3} [war]{1} [aber]{2} [die Quelle]{4} [Jakobs]{5,6}. [Jesus]{7,9} [nun]{8}, [ermüdet]{10} [von]{11} [der Wanderung]{12,13}, [setzte sich]{14}, [wie er war]{15}, [an]{16} [die Quelle]{17,18}. [Es war]{20} [ungefähr]{21} [die sechste]{22} [Stunde]{19}.",
 "JHN.4.7": "[Da kommt]{1} [eine Frau]{2} [aus]{3} [Samarien]{4,5}, [um]{6} [Wasser]{7} [zu schöpfen]{6}. [Jesus]{10,11} [sagt]{8} [zu ihr]{9}: «[Gib]{12} [mir]{13} [zu trinken]{14}!»",
 "JHN.4.8": "[Seine]{4} [Jünger]{1,3} [waren]{5} [nämlich]{2} [in]{6} [die Stadt]{7,8} [gegangen]{5}, [um]{9} [Essen]{10} [zu kaufen]{11}.",
 "JHN.4.9": "[Die]{4} [samaritische]{6,7} [Frau]{5} [sagt]{1} [nun]{2} [zu ihm]{3}: «[Wie]{8} [bittest]{15} [du]{9}, [der du]{11} [ein Jude]{10} [bist]{11}, [mich]{12,13} [um etwas zu trinken]{14}, [wo ich doch]{18} [eine samaritische]{17} [Frau]{16} [bin]{18}?» [Juden]{22} [verkehren]{21} [nämlich]{20} [nicht]{19} [mit Samaritern]{23}.",
 "JHN.4.10": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihr]{5}: «[Wenn]{6} [du]{7} [die Gabe]{8,9} [Gottes]{10,11} [kenntest]{7} und{12} [wer]{13} [es ist]{14}, [der]{15} [zu dir]{17} [sagt]{16}: ‹[Gib]{18} [mir]{19} [zu trinken]{20}!›, [dann hättest]{22} [du]{21} [ihn]{24} [gebeten]{23}, und{25} [er hätte]{27} [dir]{28} [lebendiges]{30} [Wasser]{29} [gegeben]{26}.»",
 "JHN.4.11": "[Die Frau]{3,4} [sagt]{1} [zu ihm]{2}: «[Herr]{5}, [du hast]{8} [kein]{6} [Schöpfgefäss]{7}, und{9} [der Brunnen]{10,11} [ist]{12} [tief]{13}. [Woher]{14} [hast du]{16} [also]{15} [das lebendige]{19,20} [Wasser]{17,18}?",
 "JHN.4.12": "[Bist]{4} [du]{2} [etwa]{1} [grösser]{3} [als]{5} [unser]{7} [Vater]{6} [Jakob]{8}, [der]{9} [uns]{11} [den Brunnen]{12,13} [gegeben hat]{10}? Und{14} [er selbst]{15} [hat]{18} [aus]{16} [ihm]{17} [getrunken]{18}, und{19} [seine]{22} [Söhne]{20,21} und{23} [sein]{26} [Vieh]{24,25}.»",
 "JHN.4.13": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihr]{5}: «[Jeder]{6}, [der]{7} [von]{9} [diesem]{12} [Wasser]{10,11} [trinkt]{8}, [wird]{13} [wieder]{14} [Durst bekommen]{13}.",
 "JHN.4.14": "[Wer]{1} [aber]{2} [von]{5} [dem Wasser]{6,7} [trinkt]{3,4}, [das]{8} [ich]{9} [ihm]{11} [geben werde]{10}, [wird]{14} [in Ewigkeit]{15-17} [nie]{12,13} [mehr Durst haben]{14}; [sondern]{18} [das Wasser]{19,20}, [das]{21} [ich]{22} [ihm]{23} [geben werde]{22}, [wird]{24} [in]{25} [ihm]{26} [zu einer Quelle]{27} [werden]{24}, [deren Wasser]{28} [ins]{30} [ewige]{32} [Leben]{31} [sprudelt]{29}.»",
 "JHN.4.15": "[Die Frau]{4,5} [sagt]{1} [zu ihm]{2,3}: «[Herr]{6}, [gib]{7} [mir]{8} [dieses]{9} [Wasser]{10,11}, [damit]{12} [ich]{14} [keinen]{13} [Durst mehr habe]{14} [und auch nicht]{15} [hierher]{17} [kommen muss]{16}, [um zu schöpfen]{18}.»",
 "JHN.4.16": "[Er sagt]{1} [zu ihr]{2}: «[Geh]{3}, [ruf]{4} [deinen]{5,7} [Mann]{6} und{8} [komm]{9} [hierher]{10}!»",
 "JHN.4.17": "[Die Frau]{2,3} [antwortete]{1} und{4} [sagte]{5} [zu ihm]{6}: «[Ich habe]{8} [keinen]{7} [Mann]{9}.» [Jesus]{12,13} [sagt]{10} [zu ihr]{11}: «[Zu Recht]{14} [hast du gesagt]{15}: ‹[Einen Mann]{17} [habe ich]{19} [nicht]{18}.› ~16(ὅτι leitet die direkte Rede ein)",
 "JHN.4.18": "[Fünf]{1} [Männer]{3} [hast du]{4} [nämlich]{2} [gehabt]{4}, und{5} der, [den]{7} [du]{8} [jetzt]{6} [hast]{8}, [ist]{10} [nicht]{9} [dein]{11} [Mann]{12}. [Das]{13} [hast du]{15} [wahrheitsgemäss]{14} [gesagt]{15}.»",
 "JHN.4.19": "[Die Frau]{3,4} [sagt]{1} [zu ihm]{2}: «[Herr]{5}, [ich sehe]{6}, [dass]{7} [du]{10} [ein Prophet]{8} [bist]{9}.",
 "JHN.4.20": "[Unsere]{3} [Väter]{1,2} [haben]{8} [auf]{4} [diesem]{7} [Berg]{5,6} [angebetet]{8}, und{9} [ihr]{10} [sagt]{11}, [dass]{12} [in]{13} [Jerusalem]{14} [der Ort]{16,17} [ist]{15}, [wo]{18} [man]{20} [anbeten]{19} [muss]{20}.»",
 "JHN.4.21": "[Jesus]{3,4} [sagt]{1} [zu ihr]{2}: «[Glaube]{5} [mir]{6}, [Frau]{7}: [Es kommt]{9} [die Stunde]{10}, [da]{11} [ihr]{20} [weder]{12} [auf]{13} [diesem]{16} [Berg]{14,15} [noch]{17} [in]{18} [Jerusalem]{19} [den Vater]{21,22} [anbeten werdet]{20}. ~8(ὅτι leitet den Inhalt ein)",
 "JHN.4.22": "[Ihr]{1} [betet an]{2}, [was]{3} [ihr]{5} [nicht]{4} [kennt]{5}; [wir]{6} [beten an]{7}, [was]{8} [wir kennen]{9}; [denn]{10} [das Heil]{11,12} [kommt]{16} [von]{13} [den Juden]{14,15}.",
 "JHN.4.23": "[Aber]{1} [es kommt]{2} [die Stunde]{3}, und{4} [sie ist]{6} [jetzt]{5} [da]{6}, [da]{7} [die wahren]{8,9} [Anbeter]{10} [den Vater]{12,13} [in]{14} [Geist]{15} und{16} [Wahrheit]{17} [anbeten werden]{11}; [denn]{19} [auch]{18} [der Vater]{20,21} [sucht]{23} [solche]{22}, [die]{24} [ihn]{26} [anbeten]{25}.",
 "JHN.4.24": "[Gott]{2,3} ist [Geist]{1}, und{4} [die]{5} [ihn]{7} [anbeten]{6}, [müssen]{12} [in]{8} [Geist]{9} und{10} [Wahrheit]{11} [anbeten]{13}.»",
 "JHN.4.25": "[Die Frau]{3,4} [sagt]{1} [zu ihm]{2}: «[Ich weiss]{5}, [dass]{6} [der Messias]{7} [kommt]{8}, [der]{9} [Christus]{11} [genannt wird]{10}. [Wenn]{12} [jener]{14} [kommt]{13}, [wird er]{15} [uns]{16} [alles]{17} [verkünden]{15}.»",
 "JHN.4.26": "[Jesus]{3,4} [sagt]{1} [zu ihr]{2}: «[Ich]{5} [bin es]{6}, [der]{7} [mit dir]{9} [redet]{8}.»",
 "JHN.4.27": "Und{1} [in diesem Augenblick]{2,3} [kamen]{4} [seine]{7} [Jünger]{5,6}, und{8} [sie wunderten sich]{9}, [dass]{10} [er]{13} [mit]{11} [einer Frau]{12} [redete]{13}. [Doch]{15} [keiner]{14} [sagte]{16}: «[Was]{17} [suchst du]{18}?», [oder]{19}: «[Was]{20} [redest du]{21} [mit]{22} [ihr]{23}?»",
 "JHN.4.28": "[Die Frau]{6,7} [liess]{1} [nun]{2} [ihren]{5} [Wasserkrug]{3,4} [stehen]{1} und{8} [ging]{9} [in]{10} [die Stadt]{11,12} und{13} [sagt]{14} [zu den Leuten]{15,16}:",
 "JHN.4.29": "«[Kommt]{1}, [seht]{2} [einen Menschen]{3}, [der]{4} [mir]{6} [alles]{7} [gesagt hat]{5}, [was]{8} [ich getan habe]{9}! [Ist]{12} [das]{11} [etwa]{10} [der Christus]{13,14}?»",
 "JHN.4.30": "[Sie gingen]{1} [aus]{2} [der Stadt]{3,4} [hinaus]{1} und{5} [machten sich auf den Weg]{6} [zu]{7} [ihm]{8}.",
 "JHN.4.31": "[Inzwischen]{1-3} [baten]{4} [ihn]{5} [die Jünger]{6,7} [und sagten]{8}: «[Rabbi]{9}, [iss]{10}!»",
 "JHN.4.32": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: «[Ich]{5} [habe]{7} [eine Speise]{6} [zu essen]{8}, [die]{9} [ihr]{10} [nicht]{11} [kennt]{12}.»",
 "JHN.4.33": "[Da]{2} [sagten]{1} [die Jünger]{3,4} [zueinander]{5,6}: «[Hat]{9} [ihm]{10} [etwa]{7} [jemand]{8} [etwas zu essen]{11} [gebracht]{9}?»",
 "JHN.4.34": "[Jesus]{3,4} [sagt]{1} [zu ihnen]{2}: «[Meine]{5} [Speise]{6} [ist]{7}, [dass]{8} [ich]{9} [den Willen]{10,11} [dessen]{12} [tue]{9}, [der mich gesandt hat]{13,14}, und{15} [sein]{17} [Werk]{18,19} [vollende]{16}.",
 "JHN.4.35": "[Sagt]{3} [ihr]{2} [nicht]{1}: ‹[Noch]{5} [vier Monate]{6} [sind es]{7}, und{8} [dann kommt]{11} [die Ernte]{9,10}›? [Siehe]{12}, [ich sage]{13} [euch]{14}: [Hebt]{15} [eure]{18} [Augen]{16,17} [auf]{15} und{19} [seht]{20} [die Felder]{21,22} [an]{20}: [Sie]{23} [sind]{25} [weiss]{24} [zur]{26} [Ernte]{27}. [Schon]{28} ~4(ὅτι leitet die direkte Rede ein)",
 "JHN.4.36": "[empfängt]{4} [der Schnitter]{1,2} [Lohn]{3} und{5} [sammelt]{6} [Frucht]{7} [zum]{8} [ewigen]{10} [Leben]{9}, [damit]{11} [sich]{15} [der Sämann]{12,13} und{16} [der Schnitter]{17,18} [miteinander]{14} [freuen]{15}.",
 "JHN.4.37": "[Denn]{2} [hierin]{1,3} [ist]{6} [das Wort]{4,5} [wahr]{7}: ‹[Einer]{9} [ist]{10} [der Sämann]{11,12}, und{13} [ein anderer]{14} [der Schnitter]{15,16}.› ~8(ὅτι leitet das zitierte Wort ein)",
 "JHN.4.38": "[Ich]{1} [habe]{2} [euch]{3} [gesandt]{2}, [zu ernten]{4}, [wofür]{5} [ihr]{7} [euch]{8} [nicht]{6} [abgemüht habt]{8}; [andere]{9} [haben sich abgemüht]{10}, und{11} [ihr]{12} [seid]{17} [in]{13} [ihre]{16} [Arbeit]{14,15} [eingetreten]{17}.»",
 "JHN.4.39": "[Viele]{6} [der Samariter]{10,11} [aus]{1} [jener]{5} [Stadt]{3,4} [aber]{2} [glaubten]{7} [an]{8} [ihn]{9} [wegen]{12} [des Wortes]{13,14} [der Frau]{15,16}, [die bezeugte]{17}: «[Er hat]{19} [mir]{20} [alles]{21} [gesagt]{19}, [was]{22} [ich getan habe]{23}.» ~18(ὅτι leitet die direkte Rede ein)",
 "JHN.4.40": "[Als]{1} [nun]{2} [die Samariter]{6,7} [zu]{4} [ihm]{5} [kamen]{3}, [baten sie]{8} [ihn]{9}, [bei]{11} [ihnen]{12} [zu bleiben]{10}; und{13} [er blieb]{14} [dort]{15} [zwei]{16} [Tage]{17}.",
 "JHN.4.41": "Und{1} [noch viel]{2} [mehr]{3} [glaubten]{4} [wegen]{5} [seines]{8} [Wortes]{6,7},",
 "JHN.4.42": "[und]{2} [sie sagten]{4} [zu der Frau]{1,3}: «[Nicht mehr]{6} [wegen]{7} [deines]{9} [Redens]{8,10} [glauben wir]{11}; [wir haben]{14} [nämlich]{13} [selbst]{12} [gehört]{14} und{15} [wissen]{16}, [dass]{17} [dieser]{18} [wirklich]{20} [der Retter]{21,22} [der Welt]{23,24} [ist]{19}.» ~5(ὅτι leitet die direkte Rede ein)",
 "JHN.4.43": "[Nach]{1} [den]{3} [zwei]{4} [Tagen]{5} [aber]{2} [zog er]{6} [von dort]{7} [weiter]{6} [nach]{8} [Galiläa]{9,10}.",
 "JHN.4.44": "[Jesus]{3} [selbst]{1} [hatte]{4} [nämlich]{2} [bezeugt]{4}, [dass]{5} [ein Prophet]{6} [in]{7} [seiner eigenen]{8,9} [Heimat]{10} [kein]{12} [Ansehen]{11} [hat]{13}.",
 "JHN.4.45": "[Als]{1} [er]{3} [nun]{2} [nach]{4} [Galiläa]{5,6} [kam]{3}, [nahmen]{7} [ihn]{8} [die Galiläer]{9,10} [auf]{7}, [weil sie]{12} [alles]{11} [gesehen hatten]{12}, [was]{13} [er]{14} [in]{15} [Jerusalem]{16} [am]{17,18} [Fest]{19} [getan hatte]{14}; [denn]{22} [auch]{20} [sie]{21} [waren]{23} [zum]{24,25} [Fest]{26} [gekommen]{23}.",
 "JHN.4.46": "[Er kam]{1} [nun]{2} [wieder]{3} [nach]{4} [Kana]{5,6} [in Galiläa]{7,8}, [wo]{9} [er]{10} [das Wasser]{11,12} [zu Wein]{13} [gemacht hatte]{10}. Und{14} [es war]{15} [ein]{16} [königlicher Beamter]{17}, [dessen]{18} [Sohn]{19,20} [in]{22} [Kafarnaum]{23} [krank war]{21}.",
 "JHN.4.47": "[Als dieser]{1} [hörte]{2}, [dass]{3} [Jesus]{4} [aus]{6} [Judäa]{7,8} [nach]{9} [Galiläa]{10,11} [gekommen sei]{5}, [ging er]{12} [zu]{13} [ihm]{14} [hin]{12} und{15} [bat]{16} ihn, [dass]{17} [er]{18} [hinabkomme]{18} und{19} [seinen]{21} [Sohn]{22,23} [heile]{20}; [denn]{25} [er war nahe daran]{24}, [zu sterben]{26}.",
 "JHN.4.48": "[Da]{2} [sagte]{1} [Jesus]{3,4} [zu ihm]{5,6}: «[Wenn]{7} [ihr]{12} [nicht]{8} [Zeichen]{9} und{10} [Wunder]{11} [seht]{12}, [glaubt ihr]{15} [gewiss nicht]{13,14}.»",
 "JHN.4.49": "[Der königliche Beamte]{4,5} [sagt]{1} [zu ihm]{2,3}: «[Herr]{6}, [komm hinab]{7}, [bevor]{8} [mein]{12} [Kind]{10,11} [stirbt]{9}!»",
 "JHN.4.50": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: «[Geh]{5}! [Dein]{8} [Sohn]{6,7} [lebt]{9}.» [Der Mann]{11,12} [glaubte]{10} [dem Wort]{13,14}, [das]{15} [Jesus]{18,19} [zu ihm]{17} [gesagt hatte]{16}, und{20} [machte sich auf den Weg]{21}.",
 "JHN.4.51": "[Als]{4} [er]{3} [aber]{2} [schon]{1} [hinabzog]{4}, [kamen]{8} [ihm]{9} [seine]{7} [Knechte]{5,6} [entgegen]{8} [und sagten]{10}, [sein]{14} [Junge]{12,13} [lebe]{15}. ~11(ὅτι leitet die wiedergegebene Rede ein)",
 "JHN.4.52": "[Da]{2} [erkundigte er sich]{1} [bei]{5} [ihnen]{6} [nach der Stunde]{3,4}, [in der]{7,8} [es ihm]{10} [besser]{9} [gegangen war]{10}. [Sie sagten]{11} [nun]{12} [zu ihm]{13}: «[Gestern]{15} [um die siebte]{17} [Stunde]{16} [hat]{18} [ihn]{19} [das Fieber]{20,21} [verlassen]{18}.» ~14(ὅτι leitet die direkte Rede ein)",
 "JHN.4.53": "[Da]{2} [erkannte]{1} [der Vater]{3,4}, [dass]{5} es [jene]{6} [Stunde]{7,8} war, [in]{9} [der]{10} [Jesus]{13,14} [zu ihm]{12} [gesagt hatte]{11}: «[Dein]{17} [Sohn]{15,16} [lebt]{18}.» Und{19} [er]{21} [glaubte]{20}, er [und]{22} [sein]{25} [ganzes]{26} [Haus]{23,24}.",
 "JHN.4.54": "[Dies]{1} [aber]{2} [tat]{6} [Jesus]{7,8} [wiederum]{3} [als zweites]{4} [Zeichen]{5}, [als er]{9} [aus]{10} [Judäa]{11,12} [nach]{13} [Galiläa]{14,15} [gekommen war]{9}.",
 # ------------------------------------------------------------ Kapitel 5 (5,4 fehlt im SBLGNT)
 "JHN.5.1": "[Danach]{1,2} [war]{3} [ein Fest]{4} [der Juden]{5,6}, und{7} [Jesus]{9} [zog hinauf]{8} [nach]{10} [Jerusalem]{11}.",
 "JHN.5.2": "[Es gibt]{1} [aber]{2} [in]{3} [Jerusalem]{4,5} [beim]{6,7} [Schaftor]{8} [einen Teich]{9}, [der]{10} [auf Hebräisch]{12} [Betesda]{13} [genannt wird]{11}; [er hat]{16} [fünf]{14} [Säulenhallen]{15}.",
 "JHN.5.3": "[In]{1} [ihnen]{2} [lag]{3} [eine Menge]{4} [von Kranken]{5,6}: [Blinde]{7}, [Lahme]{8}, [Ausgezehrte]{9}.",
 "JHN.5.5": "[Dort]{5} [war]{1} [aber]{2} [ein]{3} [Mensch]{4}, [der]{9} [achtunddreissig]{6,7} [Jahre]{8} [in]{10} [seiner]{11,13} [Krankheit]{12} [zugebracht hatte]{9}.",
 "JHN.5.6": "[Als]{2} [Jesus]{3,4} [diesen]{1} [daliegen]{5} [sah]{2} und{6} [erkannte]{7}, [dass]{8} [er]{12} [schon]{10} [lange]{9,11} [so dalag]{12}, [sagt er]{13} [zu ihm]{14}: «[Willst du]{15} [gesund]{16} [werden]{17}?»",
 "JHN.5.7": "[Der Kranke]{3,4} [antwortete]{1} [ihm]{2}: «[Herr]{5}, [ich habe]{8} [keinen]{7} [Menschen]{6}, [der]{9} [mich]{15}, [wenn]{10} [das Wasser]{12,13} [aufgewühlt wird]{11}, [in]{16} [den Teich]{17,18} [bringt]{14}; [während]{19,20} [ich]{23} [aber]{21} [hingehe]{22}, [steigt]{27} [ein anderer]{24} [vor]{25} [mir]{26} [hinab]{27}.»",
 "JHN.5.8": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: «[Steh auf]{5}, [nimm]{6} [deine]{7,9} [Matte]{8} und{10} [geh umher]{11}!»",
 "JHN.5.9": "Und{1} [sofort]{2} [wurde]{3} [der Mensch]{5,6} [gesund]{4}, und{7} [er nahm]{8} [seine]{9,11} [Matte]{10} und{12} [ging umher]{13}. [Es war]{14} [aber]{15} [Sabbat]{16} [an]{17} [jenem]{18} [Tag]{19,20}.",
 "JHN.5.10": "[Da]{2} [sagten]{1} [die Juden]{3,4} [zu dem Geheilten]{5,6}: «[Es ist]{8} [Sabbat]{7}, und{9} [es ist]{11} [dir]{12} [nicht]{10} [erlaubt]{11}, [die Matte]{14,15} [zu tragen]{13}.»",
 "JHN.5.11": "[Er]{1} [aber]{2} [antwortete]{3} [ihnen]{4}: «[Der]{5} [mich]{7} [gesund]{8} [gemacht hat]{6}, [der]{9} [hat]{11} [zu mir]{10} [gesagt]{11}: ‹[Nimm]{12} [deine]{13,15} [Matte]{14} und{16} [geh umher]{17}!›»",
 "JHN.5.12": "[Sie fragten]{1} [ihn]{3} [nun]{2}: «[Wer]{4} [ist]{5} [der Mensch]{6,7}, [der]{8} [zu dir]{10} [gesagt hat]{9}: ‹[Nimm]{11} sie und{12} [geh umher]{13}›?»",
 "JHN.5.13": "[Der Geheilte]{1,3} [aber]{2} [wusste]{5} [nicht]{4}, [wer]{6} [es war]{7}; [denn]{9} [Jesus]{8,10} [hatte sich entfernt]{11}, [da]{13} [eine Menge]{12} [an]{14} [dem Ort]{15,16} [war]{13}.",
 "JHN.5.14": "[Danach]{1,2} [findet]{3} [ihn]{4} [Jesus]{5,6} [im]{7,8} [Tempel]{9} und{10} [sagte]{11} [zu ihm]{12}: «[Sieh]{13}, [du bist]{15} [gesund]{14} [geworden]{15}. [Sündige]{17} [nicht mehr]{16}, [damit]{18} [dir]{21} [nicht]{19} [etwas]{22} [Schlimmeres]{20} [geschieht]{23}!»",
 "JHN.5.15": "[Der Mensch]{2,3} [ging weg]{1} und{4} [meldete]{5} [den Juden]{6,7}, [dass]{8} [Jesus]{9} [es sei]{10}, [der]{11} [ihn]{13} [gesund]{14} [gemacht habe]{12}.",
 "JHN.5.16": "Und{1} [deswegen]{2,3} [verfolgten]{4} [die Juden]{5,6} [Jesus]{7,8}, [weil]{9} [er]{11} [dies]{10} [am]{12} [Sabbat]{13} [tat]{11}.",
 "JHN.5.17": "[Er]{1} [aber]{2} [antwortete]{3} [ihnen]{4}: «[Mein]{7} [Vater]{5,6} [wirkt]{10} [bis]{8} [jetzt]{9}, [und auch ich]{11} [wirke]{12}.»",
 "JHN.5.18": "[Deshalb]{1,2} [nun]{3} [suchten]{5} [die Juden]{7,8} [umso mehr]{4}, [ihn]{6} [zu töten]{9}, [weil]{10} [er]{13} [nicht]{11} [nur]{12} [den Sabbat]{14,15} [auflöste]{13}, [sondern]{16} [auch]{17} [Gott]{21,22} [seinen eigenen]{19} [Vater]{18} [nannte]{20} und [sich selbst]{24} [Gott]{26,27} [gleich]{23} [machte]{25}.",
 "JHN.5.19": "[Jesus]{3,4} [antwortete]{1} [nun]{2} und{5} [sagte]{6} [zu ihnen]{7}: «[Amen]{8}, [amen]{9}, [ich sage]{10} [euch]{11}: [Der Sohn]{14,15} [kann]{13} [nichts]{12,19} [von]{17} [sich selbst]{18} [aus]{17} [tun]{16}, [ausser]{20,21} [was]{22} [er]{23} [den Vater]{24,25} [tun]{26} [sieht]{23}; [denn]{28} [was]{27,29} [jener]{30} [tut]{31}, [das]{32} [tut]{37} [auch]{33} [der Sohn]{34,35} [ebenso]{36}.",
 "JHN.5.20": "[Denn]{2} [der Vater]{1,3} [hat]{4} [den Sohn]{5,6} [lieb]{4} und{7} [zeigt]{9} [ihm]{10} [alles]{8}, [was]{11} [er selbst]{12} [tut]{13}; und{14} [grössere]{15} [Werke]{19} [als diese]{16} [wird er]{17} [ihm]{18} [zeigen]{17}, [damit]{20} [ihr]{21} [euch wundert]{22}.",
 "JHN.5.21": "[Denn]{2} [wie]{1} [der Vater]{3,4} [die Toten]{6,7} [auferweckt]{5} und{8} [lebendig macht]{9}, [so]{10} [macht]{16} [auch]{11} [der Sohn]{12,13} [lebendig]{16}, [welche]{14} [er will]{15}.",
 "JHN.5.22": "[Denn]{2} [der Vater]{3,4} [richtet]{5} [auch]{1} [niemanden]{6}, [sondern]{7} [er hat]{11} [das ganze]{10} [Gericht]{8,9} [dem Sohn]{12,13} [gegeben]{11},",
 "JHN.5.23": "[damit]{1} [alle]{2} [den Sohn]{4,5} [ehren]{3}, [wie]{6} [sie]{7} [den Vater]{8,9} [ehren]{7}. [Wer]{10} [den Sohn]{13,14} [nicht]{11} [ehrt]{12}, [ehrt]{16} [den Vater]{17,18} [nicht]{15}, [der]{19} [ihn]{21} [gesandt hat]{20}.",
 "JHN.5.24": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Wer]{6} [mein]{9} [Wort]{7,8} [hört]{10} und{11} [dem]{13} [glaubt]{12}, [der mich gesandt hat]{14,15}, [hat]{16} [ewiges]{18} [Leben]{17}, und{19} [er kommt]{23} [nicht]{22} [ins]{20} [Gericht]{21}, [sondern]{24} [er ist]{25} [aus]{26} [dem Tod]{27,28} [in]{29} [das Leben]{30,31} [hinübergegangen]{25}. ~5(ὅτι leitet die Rede ein)",
 "JHN.5.25": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Es kommt]{6} [die Stunde]{7}, und{8} [sie ist]{10} [jetzt]{9} [da]{10}, [da]{11} [die Toten]{12,13} [die Stimme]{15,16} [des Sohnes]{17,18} [Gottes]{19,20} [hören werden]{14}, und{21} [die]{22} [sie gehört haben]{23}, [werden leben]{24}. ~5(ὅτι leitet die Rede ein)",
 "JHN.5.26": "[Denn]{2} [wie]{1} [der Vater]{3,4} [Leben]{6} [in]{7} [sich selbst]{8} [hat]{5}, [so]{9} [hat er]{13} [auch]{10} [dem Sohn]{11,12} [gegeben]{13}, [Leben]{14} [in]{16} [sich selbst]{17} [zu haben]{15}.",
 "JHN.5.27": "Und{1} [er hat]{3} [ihm]{4} [Vollmacht]{2} [gegeben]{3}, [Gericht]{5} [zu halten]{6}, [weil]{7} [er]{10} [der Menschensohn]{8,9} [ist]{10}.",
 "JHN.5.28": "[Wundert euch]{2} [nicht]{1} [darüber]{3}; [denn]{4} [es kommt]{5} [die Stunde]{6}, [in]{7} [der]{8} [alle]{9}, [die]{10} [in]{11} [den Gräbern]{12,13} sind, [seine]{17} [Stimme]{15,16} [hören werden]{14}",
 "JHN.5.29": "und{1} [herauskommen werden]{2}: [die]{3} [das Gute]{4,5} [getan haben]{6}, [zur]{7} [Auferstehung]{8} [des Lebens]{9}, [die]{10} [aber]{11} [das Schlechte]{12,13} [verübt haben]{14}, [zur]{15} [Auferstehung]{16} [des Gerichts]{17}.",
 "JHN.5.30": "[Ich]{3} [kann]{2} [nichts]{1,7} [von]{5} [mir selbst]{6} [aus]{5} [tun]{4}. [Wie]{8} [ich höre]{9}, [so richte ich]{10}, und{11} [mein]{14,15} [Gericht]{12,13} [ist]{17} [gerecht]{16}, [weil]{18} [ich]{20} [nicht]{19} [meinen]{23,24} [Willen]{21,22} [suche]{20}, [sondern]{25} [den Willen]{26,27} [dessen]{28}, [der mich gesandt hat]{29,30}.",
 "JHN.5.31": "[Wenn]{1} [ich]{2} [über]{4} [mich selbst]{5} [Zeugnis ablege]{3}, [ist]{10} [mein]{8} [Zeugnis]{6,7} [nicht]{9} [wahr]{11}.",
 "JHN.5.32": "[Ein anderer]{1} [ist es]{2}, [der]{3} [über]{5} [mich]{6} [Zeugnis ablegt]{4}, und{7} [ich weiss]{8}, [dass]{9} [das Zeugnis]{12,13} [wahr]{10} [ist]{11}, [das]{14} [er]{15} [über]{16} [mich]{17} [ablegt]{15}.",
 "JHN.5.33": "[Ihr]{1} [habt]{2} [zu]{3} [Johannes]{4} [gesandt]{2}, und{5} [er hat]{6} [für]{7} [die Wahrheit]{8} [Zeugnis abgelegt]{6}.",
 "JHN.5.34": "[Ich]{1} [aber]{2} [nehme]{8} [das Zeugnis]{6,7} [nicht]{3} [von]{4} [einem Menschen]{5} [an]{8}, [sondern]{9} [ich sage]{11} [dies]{10}, [damit]{12} [ihr]{13} [gerettet werdet]{14}.",
 "JHN.5.35": "[Jener]{1} [war]{2} [die Lampe]{3,4}, [die]{5} [brennt]{6} und{7} [scheint]{8}; [ihr]{9} [aber]{10} [wolltet]{11} [euch]{12} [eine Zeit lang]{13,14} [in]{15} [seinem]{16,18} [Licht]{17} [freuen]{12}.",
 "JHN.5.36": "[Ich]{1} [aber]{2} [habe]{3} [das]{4} [Zeugnis]{5}, [das grösser ist]{6} [als das]{7} [des Johannes]{8}; [denn]{10} [die Werke]{9,11}, [die]{12} [mir]{14} [der Vater]{15,16} [gegeben hat]{13}, [damit]{17} [ich]{18} [sie]{19} [vollende]{18}, [eben diese]{20} [Werke]{21,22}, [die]{23} [ich tue]{24}, [legen]{25} [über]{26} [mich]{27} [Zeugnis ab]{25}, [dass]{28} [der Vater]{29,30} [mich]{31} [gesandt hat]{32}.",
 "JHN.5.37": "Und{1} [der Vater]{2,5}, [der mich gesandt hat]{3,4}, [er]{6} [hat]{7} [über]{8} [mich]{9} [Zeugnis abgelegt]{7}. [Ihr habt]{14} [weder]{10} [jemals]{13} [seine]{12} [Stimme]{11} [gehört]{14} [noch]{15} [seine]{17} [Gestalt]{16} [gesehen]{18},",
 "JHN.5.38": "und{1} [ihr habt]{6} [sein]{4} [Wort]{2,3} [nicht]{5} so, dass es [in]{7} [euch]{8} [bleibt]{9}, [weil]{10} [ihr]{15} [dem]{14} [nicht]{16} [glaubt]{17}, [den]{11} [jener]{13} [gesandt hat]{12}.",
 "JHN.5.39": "[Ihr erforscht]{1} [die Schriften]{2,3}, [weil]{4} [ihr]{5} [meint]{6}, [in]{7} [ihnen]{8} [ewiges]{10} [Leben]{9} [zu haben]{11}; und{12} [gerade sie]{13} [sind es]{14}, [die]{15} [über]{17} [mich]{18} [Zeugnis ablegen]{16};",
 "JHN.5.40": "und{1} [ihr wollt]{3} [nicht]{2} [zu]{5} [mir]{6} [kommen]{4}, [um]{7} [Leben]{8} [zu haben]{9}.",
 "JHN.5.41": "[Ehre]{1} [von]{2} [Menschen]{3} [nehme ich]{5} [nicht]{4} [an]{5},",
 "JHN.5.42": "[aber]{1} [ich habe]{2} [an euch]{3} [erkannt]{2}, [dass]{4} [ihr]{10} [die Liebe]{5,6} [zu Gott]{7,8} [nicht]{9} [in]{11} [euch]{12} [habt]{10}.",
 "JHN.5.43": "[Ich]{1} [bin]{2} [im]{3,4} [Namen]{5} [meines]{8} [Vaters]{6,7} [gekommen]{2}, und{9} [ihr nehmt]{11} [mich]{12} [nicht]{10} [an]{11}; [wenn]{13} [ein anderer]{14} [in]{16} [seinem eigenen]{19,20} [Namen]{17,18} [kommt]{15}, [den]{21} [werdet ihr annehmen]{22}.",
 "JHN.5.44": "[Wie]{1} [könnt]{2} [ihr]{3} [glauben]{4}, [die ihr]{8} [Ehre]{5} [voneinander]{6,7} [annehmt]{8} und{9} [die Ehre]{10,11}, [die]{12} [von]{13} [dem einzigen]{14,15} [Gott]{16} kommt, [nicht]{17} [sucht]{18}?",
 "JHN.5.45": "[Meint]{2} [nicht]{1}, [dass]{3} [ich]{4} [euch]{6} [beim]{7,8} [Vater]{9} [anklagen werde]{5}. [Es gibt]{10} [einen, der]{11} [euch]{13} [anklagt]{12}: [Mose]{14}, [auf]{15} [den]{16} [ihr]{17} [eure Hoffnung gesetzt habt]{18}.",
 "JHN.5.46": "[Denn]{2} [wenn]{1} [ihr]{3} [Mose]{4} [glauben würdet]{3}, [würdet ihr]{6} [mir]{7} [glauben]{5}; [denn]{9} [über]{8} [mich]{10} [hat]{12} [jener]{11} [geschrieben]{12}.",
 "JHN.5.47": "[Wenn]{1} [ihr]{7} [aber]{2} [seinen]{4} [Schriften]{3,5} [nicht]{6} [glaubt]{7}, [wie]{8} [werdet ihr]{12} [meinen]{10} [Worten]{9,11} [glauben]{12}?»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 4
 "JHN.4.1": "[Wo]{1} [de Jesus]{4,5} [jetzt]{2} [erfaare hät]{3}, [dass]{6} [d Pharisäer]{8,9} [ghört händ]{7}, [dass]{10} [de Jesus]{11} [meh]{12} [Jünger]{13} [gwünni]{14} und{15} [taufi]{16} [als]{17} [de Johannes]{18} –",
 "JHN.4.2": "– [obwohl]{1} [de Jesus]{2} [sälber]{3} [nöd]{4} [tauft hät]{5}, [sondern]{6} [sini]{9} [Jünger]{7,8} –,",
 "JHN.4.3": "[hät er]{1} [Judäa]{2,3} [verlaa]{1} und{4} [isch]{5} [wider]{6} [nach]{7} [Galiläa]{8,9} [gange]{5}.",
 "JHN.4.4": "[Er]{3} [hät]{1} [aber]{2} [dur]{5} [Samarie]{6,7} [düre]{4} [müese]{1}.",
 "JHN.4.5": "[Er chunnt]{1} [also]{2} [in]{3} [e Stadt]{4} [z Samarie]{5,6}, [wo]{7} [Sychar]{8} [heisst]{7}, [nöch bi]{9} [em]{10} [Grundstück]{11}, [wo]{12} [de Jakob]{14} [sim]{17,19} [Sohn]{18} [Josef]{15,16} [gää hät]{13}.",
 "JHN.4.6": "[Dört]{3} [isch]{1} [aber]{2} [em Jakob]{5,6} [sini Quälle]{4} [gsii]{1}. [De Jesus]{7,9} [also]{8}, [müed]{10} [vo]{11} [de Wanderig]{12,13}, [isch]{14}, [wie n er gsii isch]{15}, [bi]{16} [de Quälle]{17,18} [abgsässe]{14}. [Es isch]{20} [öppe]{21} [di sächst]{22} [Stund]{19} [gsii]{20}.",
 "JHN.4.7": "[Da chunnt]{1} [e Frau]{2} [us]{3} [Samarie]{4,5}, [go]{6} [Wasser]{7} [schöpfe]{6}. [De Jesus]{10,11} [seit]{8} [zu ire]{9}: «[Gib]{12} [mer]{13} [z trinke]{14}!»",
 "JHN.4.8": "[Sini]{4} [Jünger]{1,3} [sind]{5} [nämli]{2} [i]{6} [d Stadt]{7,8} [gange]{5}, [go]{9} [Ässe]{10} [poschte]{11}.",
 "JHN.4.9": "[D]{4} [samaritanisch]{6,7} [Frau]{5} [seit]{1} [dänn]{2} [zu ihm]{3}: «[Wie]{8} [chasch]{15} [du]{9}, [wo]{11} [en Jud]{10} [bisch]{11}, [mich]{12,13} [um öppis z trinke]{14} [bitte]{15}, [wo ich doch]{18} [e samaritanischi]{17} [Frau]{16} [bin]{18}?» [D Jude]{22} [händ]{21} [nämli]{20} [nüüt]{19} [mit de Samaritaner]{23} [z tue]{21}.",
 "JHN.4.10": "[De Jesus]{2} [hät]{1} [ire]{5} [gantwortet]{1} und{3} [gseit]{4}: «[Wänn]{6} [du]{7} [d Gaab]{8,9} [vo Gott]{10,11} [kännti]{7} und{12} [wer]{13} [es isch]{14}, [wo]{15} [zu dir]{17} [seit]{16}: ‹[Gib]{18} [mer]{19} [z trinke]{20}!›, [dänn hettsch]{22} [du]{21} [en]{24} [bätte]{23}, und{25} [er hett]{27} [dir]{28} [läbigs]{30} [Wasser]{29} [gää]{26}.»",
 "JHN.4.11": "[D Frau]{3,4} [seit]{1} [zu ihm]{2}: «[Herr]{5}, [du häsch]{8} [kei]{6} [Schöpfchessel]{7}, und{9} [de Brunne]{10,11} [isch]{12} [tüüf]{13}. [Vo wo]{14} [häsch]{16} [dänn]{15} [s läbig]{19,20} [Wasser]{17,18}?",
 "JHN.4.12": "[Bisch]{4} [du]{2} [öppe]{1} [grösser]{3} [als]{5} [üse]{7} [Vatter]{6} [Jakob]{8}, [wo]{9} [üs]{11} [de Brunne]{12,13} [gää hät]{10}? Und{14} [er sälber]{15} [hät]{18} [drus]{16,17} [trunke]{18}, und{19} [sini]{22} [Söön]{20,21} und{23} [sis]{26} [Vee]{24,25}.»",
 "JHN.4.13": "[De Jesus]{2} [hät]{1} [ire]{5} [gantwortet]{1} und{3} [gseit]{4}: «[Jede]{6}, [wo]{7} [vo]{9} [däm]{12} [Wasser]{10,11} [trinkt]{8}, [überchunnt]{13} [wider]{14} [Durscht]{13}.",
 "JHN.4.14": "[Wer]{1} [aber]{2} [vo]{5} [em Wasser]{6,7} [trinkt]{3,4}, [wo]{8} [ich]{9} [ihm]{11} [gää wirde]{10}, [wird]{14} [i alli Ewigkeit]{15-17} [nie]{12,13} [meh Durscht ha]{14}; [sondern]{18} [s Wasser]{19,20}, [wo]{21} [ich]{22} [ihm]{23} [gää wirde]{22}, [wird]{24} [in]{25} [ihm]{26} [zu ere Quälle]{27} [wärde]{24}, [wo s Wasser]{28} [is]{30} [ewig]{32} [Läbe]{31} [usesprudlet]{29}.»",
 "JHN.4.15": "[D Frau]{4,5} [seit]{1} [zu ihm]{2,3}: «[Herr]{6}, [gib]{7} [mer]{8} [das]{9} [Wasser]{10,11}, [demit]{12} [ich]{14} [kei]{13} [Durscht meh ha]{14} [und au nüme]{15} [da ane]{17} [mues cho]{16} [go schöpfe]{18}.»",
 "JHN.4.16": "[Er seit]{1} [zu ire]{2}: «[Gang]{3}, [rüef]{4} [din]{5,7} [Maa]{6} und{8} [chumm]{9} [da ane]{10}!»",
 "JHN.4.17": "[D Frau]{2,3} [hät gantwortet]{1} und{4} [zu ihm]{6} [gseit]{5}: «[Ich ha]{8} [kei]{7} [Maa]{9}.» [De Jesus]{12,13} [seit]{10} [zu ire]{11}: «[Du häsch]{15} [s richtig]{14} [gseit]{15}: ‹[En Maa]{17} [han ich]{19} [nöd]{18}.› ~16(ὅτι leitet di diräkt Red ii)",
 "JHN.4.18": "[Föif]{1} [Mane]{3} [häsch]{4} [nämli]{2} [gha]{4}, und{5} dä, [wo]{7} [du]{8} [jetzt]{6} [häsch]{8}, [isch]{10} [nöd]{9} [din]{11} [Maa]{12}. [Das]{13} [häsch]{15} [wahr]{14} [gseit]{15}.»",
 "JHN.4.19": "[D Frau]{3,4} [seit]{1} [zu ihm]{2}: «[Herr]{5}, [ich gsee]{6}, [dass]{7} [du]{10} [en Prophet]{8} [bisch]{9}.",
 "JHN.4.20": "[Üsi]{3} [Vätter]{1,2} [händ]{8} [uf]{4} [däm]{7} [Bärg]{5,6} [aabättet]{8}, und{9} [ir]{10} [säged]{11}, [dass]{12} [z]{13} [Jerusalem]{14} [de Ort]{16,17} [sig]{15}, [wo]{18} [mer]{20} [aabätte]{19} [mues]{20}.»",
 "JHN.4.21": "[De Jesus]{3,4} [seit]{1} [zu ire]{2}: «[Glaub]{5} [mer]{6}, [Frau]{7}: [Es chunnt]{9} [d Stund]{10}, [wo]{11} [ir]{20} [weder]{12} [uf]{13} [däm]{16} [Bärg]{14,15} [no]{17} [z]{18} [Jerusalem]{19} [de Vatter]{21,22} [aabätte wärded]{20}. ~8(ὅτι leitet de Inhalt ii)",
 "JHN.4.22": "[Ir]{1} [bätted aa]{2}, [was]{3} [ir]{5} [nöd]{4} [känned]{5}; [mir]{6} [bätted aa]{7}, [was]{8} [mir känned]{9}; [dänn]{10} [s Heil]{11,12} [chunnt]{16} [vo]{13} [de Jude]{14,15}.",
 "JHN.4.23": "[Aber]{1} [es chunnt]{2} [d Stund]{3}, und{4} [si isch]{6} [jetzt]{5} [da]{6}, [wo]{7} [di wahre]{8,9} [Aabätter]{10} [de Vatter]{12,13} [i]{14} [Geischt]{15} und{16} [Wahrheit]{17} [aabätte wärded]{11}; [dänn]{19} [au]{18} [de Vatter]{20,21} [suecht]{23} [settig]{22}, [wo]{24} [en]{26} [aabätted]{25}.",
 "JHN.4.24": "[Gott]{2,3} isch [Geischt]{1}, und{4} [die, wo]{5} [en]{7} [aabätted]{6}, [münd]{12} [i]{8} [Geischt]{9} und{10} [Wahrheit]{11} [aabätte]{13}.»",
 "JHN.4.25": "[D Frau]{3,4} [seit]{1} [zu ihm]{2}: «[Ich weiss]{5}, [dass]{6} [de Messias]{7} [chunnt]{8}, [wo]{9} [mer]{10} [Christus]{11} [nännt]{10}. [Wänn]{12} [dä]{14} [chunnt]{13}, [wird er]{15} [üs]{16} [alles]{17} [verchünde]{15}.»",
 "JHN.4.26": "[De Jesus]{3,4} [seit]{1} [zu ire]{2}: «[Ich]{5} [bi s]{6}, [wo]{7} [mit dir]{9} [redt]{8}.»",
 "JHN.4.27": "Und{1} [i däm Momänt]{2,3} [sind]{4} [sini]{7} [Jünger]{5,6} [choo]{4}, und{8} [si händ gstuunt]{9}, [dass]{10} [er]{13} [mit]{11} [ere Frau]{12} [redt]{13}. [Aber]{15} [keine]{14} [hät gseit]{16}: «[Was]{17} [suechsch]{18}?», [oder]{19}: «[Was]{20} [redsch]{21} [mit]{22} [ire]{23}?»",
 "JHN.4.28": "[D Frau]{6,7} [hät]{1} [dänn]{2} [ire]{5} [Wasserchrueg]{3,4} [stoo laa]{1} und{8} [isch]{9} [i]{10} [d Stadt]{11,12} [gange]{9} und{13} [seit]{14} [de Lüüt]{15,16}:",
 "JHN.4.29": "«[Chömed]{1}, [lueged]{2} [en Mänsch]{3}, [wo]{4} [mer]{6} [alles]{7} [gseit hät]{5}, [was]{8} [ich gmacht ha]{9}! [Isch]{12} [das]{11} [ächt]{10} [de Christus]{13,14}?»",
 "JHN.4.30": "[Si sind]{1} [us]{2} [de Stadt]{3,4} [usegange]{1} und{5} [händ sich]{6} [zu]{7} [ihm]{8} [uf de Wäg gmacht]{6}.",
 "JHN.4.31": "[Underdesse]{1-3} [händ]{4} [en]{5} [d Jünger]{6,7} [bätte]{4} [und gseit]{8}: «[Rabbi]{9}, [iss]{10}!»",
 "JHN.4.32": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: «[Ich]{5} [ha]{7} [e Spiis]{6} [z ässe]{8}, [wo]{9} [ir]{10} [nöd]{11} [känned]{12}.»",
 "JHN.4.33": "[Da]{2} [händ]{1} [d Jünger]{3,4} [zunenand]{5,6} [gseit]{1}: «[Hät]{9} [em]{10} [ächt]{7} [öpper]{8} [öppis z ässe]{11} [praacht]{9}?»",
 "JHN.4.34": "[De Jesus]{3,4} [seit]{1} [zu ine]{2}: «[Mini]{5} [Spiis]{6} [isch]{7}, [dass]{8} [ich]{9} [de Wille]{10,11} [vo däm]{12} [tue]{9}, [wo mich gschickt hät]{13,14}, und{15} [sis]{17} [Wärch]{18,19} [vollände]{16}.",
 "JHN.4.35": "[Säged]{3} [ir]{2} [nöd]{1}: ‹[No]{5} [vier Mönet]{6} [isch es]{7}, und{8} [dänn chunnt]{11} [d Ärnt]{9,10}›? [Lueged]{12}, [ich säge]{13} [eu]{14}: [Hebed]{15} [eui]{18} [Auge]{16,17} [uf]{15} und{19} [lueged]{20} [d Fälder]{21,22} [aa]{20}: [Si]{23} [sind]{25} [wiiss]{24} [für]{26} [d Ärnt]{27}. [Scho]{28} ~4(ὅτι leitet di diräkt Red ii)",
 "JHN.4.36": "[überchunnt]{4} [de Schnitter]{1,2} [Lohn]{3} und{5} [sammlet]{6} [Frucht]{7} [für]{8} [s ewig]{10} [Läbe]{9}, [demit]{11} [sich]{15} [de Sämaa]{12,13} und{16} [de Schnitter]{17,18} [mitenand]{14} [fröied]{15}.",
 "JHN.4.37": "[Dänn]{2} [da drin]{1,3} [isch]{6} [das Wort]{4,5} [wahr]{7}: ‹[Eine]{9} [isch]{10} [de Sämaa]{11,12}, und{13} [en andere]{14} [de Schnitter]{15,16}.› ~8(ὅτι leitet s zitiert Wort ii)",
 "JHN.4.38": "[Ich]{1} [ha]{2} [eu]{3} [gschickt]{2}, [go ärnte]{4}, [wofür]{5} [ir]{7} [eu]{8} [nöd]{6} [abgmüeht händ]{8}; [anderi]{9} [händ sich abgmüeht]{10}, und{11} [ir]{12} [sind]{17} [i]{13} [iri]{16} [Arbet]{14,15} [iiträtte]{17}.»",
 "JHN.4.39": "[Vili]{6} [vo de Samaritaner]{10,11} [us]{1} [dere]{5} [Stadt]{3,4} [aber]{2} [händ]{7} [a]{8} [en]{9} [glaubt]{7} [wäge]{12} [em Wort]{13,14} [vo de Frau]{15,16}, [wo bezüügt hät]{17}: «[Er hät]{19} [mer]{20} [alles]{21} [gseit]{19}, [was]{22} [ich gmacht ha]{23}.» ~18(ὅτι leitet di diräkt Red ii)",
 "JHN.4.40": "[Wo]{1} [d Samaritaner]{6,7} [dänn]{2} [zu]{4} [ihm]{5} [choo sind]{3}, [händ si]{8} [en]{9} [bätte]{8}, [bi]{11} [ine]{12} [z bliibe]{10}; und{13} [er isch]{14} [zwei]{16} [Täg]{17} [dört]{15} [bliibe]{14}.",
 "JHN.4.41": "Und{1} [no vil]{2} [meh]{3} [händ glaubt]{4} [wäge]{5} [sim]{8} [Wort]{6,7},",
 "JHN.4.42": "[und]{2} [zu de Frau]{1,3} [händ si gseit]{4}: «[Mir glaubed]{11} [nüme]{6} [wäge]{7} [dim]{9} [Gred]{8,10}; [mir händ]{14} [nämli]{13} [sälber]{12} [ghört]{14} und{15} [wüssed]{16}, [dass]{17} [dä]{18} [würkli]{20} [de Retter]{21,22} [vo de Wält]{23,24} [isch]{19}.» ~5(ὅτι leitet di diräkt Red ii)",
 "JHN.4.43": "[Nach]{1} [dene]{3} [zwei]{4} [Täg]{5} [aber]{2} [isch er]{6} [vo dört]{7} [nach]{8} [Galiläa]{9,10} [wiitergange]{6}.",
 "JHN.4.44": "[De Jesus]{3} [sälber]{1} [hät]{4} [nämli]{2} [bezüügt]{4}, [dass]{5} [en Prophet]{6} [in]{7} [sinere eigete]{8,9} [Heimet]{10} [kei]{12} [Aasee]{11} [hät]{13}.",
 "JHN.4.45": "[Wo]{1} [er]{3} [dänn]{2} [nach]{4} [Galiläa]{5,6} [choo isch]{3}, [händ]{7} [en]{8} [d Galiläer]{9,10} [ufgnoo]{7}, [wil si]{12} [alles]{11} [gseh händ]{12}, [was]{13} [er]{14} [z]{15} [Jerusalem]{16} [am]{17,18} [Fäscht]{19} [gmacht hät]{14}; [dänn]{22} [au]{20} [si]{21} [sind]{23} [as]{24,25} [Fäscht]{26} [gange]{23}.",
 "JHN.4.46": "[Er isch]{1} [dänn]{2} [wider]{3} [nach]{4} [Kana]{5,6} [z Galiläa]{7,8} [choo]{1}, [wo]{9} [er]{10} [s Wasser]{11,12} [zu Wii]{13} [gmacht hät]{10}. Und{14} [es hät]{15} [en]{16} [königliche Beamte]{17} [gää]{15}, [wo sin]{18} [Sohn]{19,20} [z]{22} [Kafarnaum]{23} [chrank gsii isch]{21}.",
 "JHN.4.47": "[Wo dä]{1} [ghört hät]{2}, [dass]{3} [de Jesus]{4} [us]{6} [Judäa]{7,8} [nach]{9} [Galiläa]{10,11} [choo sig]{5}, [isch er]{12} [zu]{13} [ihm]{14} [gange]{12} und{15} [hät en bätte]{16}, [dass]{17} [er]{18} [abechämi]{18} und{19} [sin]{21} [Sohn]{22,23} [heili]{20}; [dänn]{25} [er isch]{24} [am Stärbe]{26} [gsii]{24}.",
 "JHN.4.48": "[Da]{2} [hät]{1} [de Jesus]{3,4} [zu ihm]{5,6} [gseit]{1}: «[Wänn]{7} [ir]{12} [nöd]{8} [Zeiche]{9} und{10} [Wunder]{11} [gsehnd]{12}, [glaubed ir]{15} [sicher nöd]{13,14}.»",
 "JHN.4.49": "[De königlich Beamt]{4,5} [seit]{1} [zu ihm]{2,3}: «[Herr]{6}, [chumm abe]{7}, [bevor]{8} [mis]{12} [Chind]{10,11} [stirbt]{9}!»",
 "JHN.4.50": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: «[Gang]{5}! [Din]{8} [Sohn]{6,7} [läbt]{9}.» [De Maa]{11,12} [hät]{10} [em Wort]{13,14} [glaubt]{10}, [wo]{15} [de Jesus]{18,19} [zu ihm]{17} [gseit hät]{16}, und{20} [hät sich uf de Wäg gmacht]{21}.",
 "JHN.4.51": "[Wo]{4} [er]{3} [aber]{2} [scho]{1} [underwägs abe gsii isch]{4}, [sind]{8} [em]{9} [sini]{7} [Chnächt]{5,6} [entgäge choo]{8} [und händ gseit]{10}, [sin]{14} [Bueb]{12,13} [läbi]{15}. ~11(ὅτι leitet di widergää Red ii)",
 "JHN.4.52": "[Da]{2} [hät er sich]{1} [bi]{5} [ine]{6} [nach de Stund]{3,4} [erkundiget]{1}, [wo]{7,8} [s em]{10} [besser]{9} [ggange sig]{10}. [Si händ]{11} [dänn]{12} [zu ihm]{13} [gseit]{11}: «[Geschter]{15} [um di sibet]{17} [Stund]{16} [hät]{18} [en]{19} [s Fieber]{20,21} [verlaa]{18}.» ~14(ὅτι leitet di diräkt Red ii)",
 "JHN.4.53": "[Da]{2} [hät]{1} [de Vatter]{3,4} [gmerkt]{1}, [dass]{5} es [die]{6} [Stund]{7,8} gsii isch, [wo]{9,10} [de Jesus]{13,14} [zu ihm]{12} [gseit hät]{11}: «[Din]{17} [Sohn]{15,16} [läbt]{18}.» Und{19} [er]{21} [hät glaubt]{20}, er [und]{22} [sis]{25} [ganz]{26} [Huus]{23,24}.",
 "JHN.4.54": "[Das]{1} [aber]{2} [hät]{6} [de Jesus]{7,8} [wider]{3} [als zweits]{4} [Zeiche]{5} [gmacht]{6}, [wo n er]{9} [us]{10} [Judäa]{11,12} [nach]{13} [Galiläa]{14,15} [choo isch]{9}.",
 # ------------------------------------------------------------ Kapitel 5 (5,4 fehlt im SBLGNT)
 "JHN.5.1": "[Dänn]{1,2} [isch]{3} [es Fäscht]{4} [vo de Jude]{5,6} [gsii]{3}, und{7} [de Jesus]{9} [isch]{8} [uf]{10} [Jerusalem]{11} [ufegange]{8}.",
 "JHN.5.2": "[Es hät]{1} [aber]{2} [z]{3} [Jerusalem]{4,5} [bim]{6,7} [Schaaftor]{8} [en Teich]{9}, [wo]{10} [uf Hebräisch]{12} [Betesda]{13} [heisst]{11}; [er hät]{16} [föif]{14} [Säulehalle]{15}.",
 "JHN.5.3": "[I]{1} [dene]{2} [isch]{3} [e Mängi]{4} [Chranki]{5,6} [gläge]{3}: [Blindi]{7}, [Lahmi]{8}, [Uusgmerglete]{9}.",
 "JHN.5.5": "[Dört]{5} [isch]{1} [aber]{2} [en]{3} [Mänsch]{4} [gsii]{1}, [wo]{9} [achtedriissg]{6,7} [Jahr]{8} [i]{10} [sinere]{11,13} [Chranket]{12} [zuebracht hät]{9}.",
 "JHN.5.6": "[Wo]{2} [de Jesus]{3,4} [dä]{1} [ligge]{5} [gseh hät]{2} und{6} [gmerkt hät]{7}, [dass]{8} [er]{12} [scho]{10} [lang]{9,11} [eso dalit]{12}, [seit er]{13} [zu ihm]{14}: «[Wotsch]{15} [gsund]{16} [wärde]{17}?»",
 "JHN.5.7": "[De Chrank]{3,4} [hät]{1} [em]{2} [gantwortet]{1}: «[Herr]{5}, [ich ha]{8} [kei]{7} [Mänsch]{6}, [wo]{9} [mich]{15}, [wänn]{10} [s Wasser]{12,13} [ufgwüelt wird]{11}, [in]{16} [de Teich]{17,18} [bringt]{14}; [bis]{19,20} [ich]{23} [aber]{21} [chume]{22}, [gaat]{27} [en andere]{24} [vor]{25} [mir]{26} [abe]{27}.»",
 "JHN.5.8": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: «[Stand uf]{5}, [nimm]{6} [dini]{7,9} [Matte]{8} und{10} [lauf umenand]{11}!»",
 "JHN.5.9": "Und{1} [sofort]{2} [isch]{3} [de Mänsch]{5,6} [gsund]{4} [worde]{3}, und{7} [er hät]{8} [sini]{9,11} [Matte]{10} [gnoo]{8} und{12} [isch umenand gloffe]{13}. [Es isch]{14} [aber]{15} [Sabbat]{16} [gsii]{14} [a]{17} [däm]{18} [Tag]{19,20}.",
 "JHN.5.10": "[Da]{2} [händ]{1} [d Jude]{3,4} [zu däm, wo gheilt worde isch]{5,6}, [gseit]{1}: «[Es isch]{8} [Sabbat]{7}, und{9} [es isch]{11} [dir]{12} [nöd]{10} [erlaubt]{11}, [d Matte]{14,15} [z träge]{13}.»",
 "JHN.5.11": "[Er]{1} [aber]{2} [hät]{3} [ine]{4} [gantwortet]{3}: «[Dä, wo]{5} [mich]{7} [gsund]{8} [gmacht hät]{6}, [dä]{9} [hät]{11} [mer]{10} [gseit]{11}: ‹[Nimm]{12} [dini]{13,15} [Matte]{14} und{16} [lauf umenand]{17}!›»",
 "JHN.5.12": "[Si händ]{1} [en]{3} [dänn]{2} [gfröget]{1}: «[Wer]{4} [isch]{5} [de Mänsch]{6,7}, [wo]{8} [zu dir]{10} [gseit hät]{9}: ‹[Nimm]{11} si und{12} [lauf umenand]{13}›?»",
 "JHN.5.13": "[De Gheilt]{1,3} [aber]{2} [hät]{5} [nöd]{4} [gwüsst]{5}, [wer]{6} [es isch]{7}; [dänn]{9} [de Jesus]{8,10} [hät sich verzoge]{11}, [wil]{13} [e Mängi]{12} [am]{14,15} [Ort]{16} [gsii isch]{13}.",
 "JHN.5.14": "[Dänn]{1,2} [findt]{3} [en]{4} [de Jesus]{5,6} [im]{7,8} [Tämpel]{9} und{10} [hät]{11} [zu ihm]{12} [gseit]{11}: «[Lueg]{13}, [du bisch]{15} [gsund]{14} [worde]{15}. [Sündig]{17} [nüme]{16}, [demit]{18} [dir]{21} [nöd]{19} [öppis]{22} [Schlimmers]{20} [passiert]{23}!»",
 "JHN.5.15": "[De Mänsch]{2,3} [isch furtgange]{1} und{4} [hät]{5} [de Jude]{6,7} [gmäldet]{5}, [dass]{8} es [de Jesus]{9} [sig]{10}, [wo]{11} [en]{13} [gsund]{14} [gmacht heig]{12}.",
 "JHN.5.16": "Und{1} [drum]{2,3} [händ]{4} [d Jude]{5,6} [de Jesus]{7,8} [verfolgt]{4}, [wil]{9} [er]{11} [das]{10} [am]{12} [Sabbat]{13} [gmacht hät]{11}.",
 "JHN.5.17": "[Er]{1} [aber]{2} [hät]{3} [ine]{4} [gantwortet]{3}: «[Min]{7} [Vatter]{5,6} [wirkt]{10} [bis]{8} [jetzt]{9}, [und au ich]{11} [wirke]{12}.»",
 "JHN.5.18": "[Drum]{1,2} [händ]{5} [d Jude]{7,8} [dänn]{3} [no meh]{4} [gsuecht]{5}, [en]{6} [z töte]{9}, [wil]{10} [er]{13} [nöd]{11} [nu]{12} [de Sabbat]{14,15} [ufglööst hät]{13}, [sondern]{16} [au]{17} [Gott]{21,22} [sin eigete]{19} [Vatter]{18} [gnännt hät]{20} und [sich sälber]{24} [Gott]{26,27} [gliich]{23} [gmacht hät]{25}.",
 "JHN.5.19": "[De Jesus]{3,4} [hät]{1} [dänn]{2} [gantwortet]{1} und{5} [zu ine]{7} [gseit]{6}: «[Amen]{8}, [amen]{9}, [ich säge]{10} [eu]{11}: [De Sohn]{14,15} [cha]{13} [nüüt]{12,19} [vo]{17} [sich sälber]{18} [uus]{17} [mache]{16}, [usser]{20,21} [was]{22} [er]{23} [de Vatter]{24,25} [mache]{26} [gseht]{23}; [dänn]{28} [was]{27,29} [dä]{30} [macht]{31}, [das]{32} [macht]{37} [au]{33} [de Sohn]{34,35} [gliich]{36}.",
 "JHN.5.20": "[Dänn]{2} [de Vatter]{1,3} [hät]{4} [de Sohn]{5,6} [gärn]{4} und{7} [zeigt]{9} [ihm]{10} [alles]{8}, [was]{11} [er sälber]{12} [macht]{13}; und{14} [grösseri]{15} [Wärch]{19} [als die]{16} [wird er]{17} [ihm]{18} [zeige]{17}, [demit]{20} [ir]{21} [stuuned]{22}.",
 "JHN.5.21": "[Dänn]{2} [wie]{1} [de Vatter]{3,4} [d Tote]{6,7} [uferweckt]{5} und{8} [läbig macht]{9}, [so]{10} [macht]{16} [au]{11} [de Sohn]{12,13} [die]{14} [läbig]{16}, [won er will]{15}.",
 "JHN.5.22": "[Dänn]{2} [de Vatter]{3,4} [richtet]{5} [au]{1} [niemer]{6}, [sondern]{7} [er hät]{11} [s ganz]{10} [Gricht]{8,9} [em Sohn]{12,13} [gää]{11},",
 "JHN.5.23": "[demit]{1} [alli]{2} [de Sohn]{4,5} [ehred]{3}, [wie]{6} [si]{7} [de Vatter]{8,9} [ehred]{7}. [Wer]{10} [de Sohn]{13,14} [nöd]{11} [ehrt]{12}, [ehrt]{16} [de Vatter]{17,18} [nöd]{15}, [wo]{19} [en]{21} [gschickt hät]{20}.",
 "JHN.5.24": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Wer]{6} [mis]{9} [Wort]{7,8} [ghört]{10} und{11} [däm]{13} [glaubt]{12}, [wo mich gschickt hät]{14,15}, [hät]{16} [ewigs]{18} [Läbe]{17}, und{19} [er chunnt]{23} [nöd]{22} [is]{20} [Gricht]{21}, [sondern]{24} [er isch]{25} [vom]{26,27} [Tod]{28} [is]{29,30} [Läbe]{31} [übere gange]{25}. ~5(ὅτι leitet d Red ii)",
 "JHN.5.25": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Es chunnt]{6} [d Stund]{7}, und{8} [si isch]{10} [jetzt]{9} [da]{10}, [wo]{11} [d Tote]{12,13} [d Stimm]{15,16} [vom Sohn]{17,18} [vo Gott]{19,20} [ghöre wärded]{14}, und{21} [die, wo]{22} [si ghört händ]{23}, [wärded läbe]{24}. ~5(ὅτι leitet d Red ii)",
 "JHN.5.26": "[Dänn]{2} [wie]{1} [de Vatter]{3,4} [Läbe]{6} [in]{7} [sich sälber]{8} [hät]{5}, [so]{9} [hät er]{13} [au]{10} [em Sohn]{11,12} [gää]{13}, [Läbe]{14} [in]{16} [sich sälber]{17} [z ha]{15}.",
 "JHN.5.27": "Und{1} [er hät]{3} [ihm]{4} [Vollmacht]{2} [gää]{3}, [Gricht]{5} [z halte]{6}, [wil]{7} [er]{10} [de Mänschesohn]{8,9} [isch]{10}.",
 "JHN.5.28": "[Stuuned]{2} [nöd]{1} [drüber]{3}; [dänn]{4} [es chunnt]{5} [d Stund]{6}, [i]{7} [dere]{8} [alli]{9}, [wo]{10} [i]{11} [de Gräber]{12,13} sind, [sini]{17} [Stimm]{15,16} [ghöre wärded]{14}",
 "JHN.5.29": "und{1} [usechoo wärded]{2}: [die, wo]{3} [s Gueti]{4,5} [gmacht händ]{6}, [zur]{7} [Uferstehig]{8} [vom Läbe]{9}, [die]{10} [aber]{11}, [wo]{10} [s Schlächti]{12,13} [taa händ]{14}, [zur]{15} [Uferstehig]{16} [vom Gricht]{17}.",
 "JHN.5.30": "[Ich]{3} [cha]{2} [nüüt]{1,7} [vo]{5} [mir sälber]{6} [uus]{5} [mache]{4}. [Wie]{8} [ich ghöre]{9}, [so richt ich]{10}, und{11} [mis]{14,15} [Gricht]{12,13} [isch]{17} [grächt]{16}, [wil]{18} [ich]{20} [nöd]{19} [min]{23,24} [Wille]{21,22} [sueche]{20}, [sondern]{25} [de Wille]{26,27} [vo däm]{28}, [wo mich gschickt hät]{29,30}.",
 "JHN.5.31": "[Wänn]{1} [ich]{2} [über]{4} [mich sälber]{5} [Zügnis ablegge]{3}, [isch]{10} [mis]{8} [Zügnis]{6,7} [nöd]{9} [wahr]{11}.",
 "JHN.5.32": "[En andere]{1} [isch es]{2}, [wo]{3} [über]{5} [mich]{6} [Zügnis ablegt]{4}, und{7} [ich weiss]{8}, [dass]{9} [s Zügnis]{12,13} [wahr]{10} [isch]{11}, [wo]{14} [er]{15} [über]{16} [mich]{17} [ablegt]{15}.",
 "JHN.5.33": "[Ir]{1} [händ]{2} [zum]{3} [Johannes]{4} [gschickt]{2}, und{5} [er hät]{6} [für]{7} [d Wahrheit]{8} [Zügnis abgleit]{6}.",
 "JHN.5.34": "[Ich]{1} [aber]{2} [nime]{8} [s Zügnis]{6,7} [nöd]{3} [vo]{4} [eme Mänsch]{5} [aa]{8}, [sondern]{9} [ich säge]{11} [das]{10}, [demit]{12} [ir]{13} [grettet wärded]{14}.",
 "JHN.5.35": "[Dä]{1} [isch]{2} [d Lampe]{3,4} [gsii]{2}, [wo]{5} [brännt]{6} und{7} [schiint]{8}; [ir]{9} [aber]{10} [händ]{11} [eu]{12} [es Ziitli]{13,14} [i]{15} [sim]{16,18} [Liecht]{17} [fröie]{12} [wele]{11}.",
 "JHN.5.36": "[Ich]{1} [aber]{2} [ha]{3} [s]{4} [Zügnis]{5}, [wo grösser isch]{6} [als das]{7} [vom Johannes]{8}; [dänn]{10} [d Wärch]{9,11}, [wo]{12} [mir]{14} [de Vatter]{15,16} [gää hät]{13}, [demit]{17} [ich]{18} [si]{19} [vollände]{18}, [genau die]{20} [Wärch]{21,22}, [wo]{23} [ich tue]{24}, [legged]{25} [über]{26} [mich]{27} [Zügnis ab]{25}, [dass]{28} [de Vatter]{29,30} [mich]{31} [gschickt hät]{32}.",
 "JHN.5.37": "Und{1} [de Vatter]{2,5}, [wo mich gschickt hät]{3,4}, [dä]{6} [hät]{7} [über]{8} [mich]{9} [Zügnis abgleit]{7}. [Ir händ]{14} [weder]{10} [je]{13} [sini]{12} [Stimm]{11} [ghört]{14} [no]{15} [sini]{17} [Gstalt]{16} [gseh]{18},",
 "JHN.5.38": "und{1} [ir händ]{6} [sis]{4} [Wort]{2,3} [nöd]{5} eso, dass es [in]{7} [eu]{8} [bliibt]{9}, [wil]{10} [ir]{15} [däm]{14} [nöd]{16} [glaubed]{17}, [wo]{11} [dä]{13} [gschickt hät]{12}.",
 "JHN.5.39": "[Ir erforsched]{1} [d Schrifte]{2,3}, [wil]{4} [ir]{5} [meined]{6}, [i]{7} [ine]{8} [ewigs]{10} [Läbe]{9} [z ha]{11}; und{12} [grad si]{13} [sind s]{14}, [wo]{15} [über]{17} [mich]{18} [Zügnis ablegged]{16};",
 "JHN.5.40": "und{1} [ir wänd]{3} [nöd]{2} [zu]{5} [mir]{6} [choo]{4}, [zum]{7} [Läbe]{8} [ha]{9}.",
 "JHN.5.41": "[Ehr]{1} [vo]{2} [Mänsche]{3} [nim ich]{5} [nöd]{4} [aa]{5},",
 "JHN.5.42": "[aber]{1} [ich ha]{2} [a eu]{3} [gmerkt]{2}, [dass]{4} [ir]{10} [d Liebi]{5,6} [zu Gott]{7,8} [nöd]{9} [in]{11} [eu]{12} [händ]{10}.",
 "JHN.5.43": "[Ich]{1} [bin]{2} [im]{3,4} [Name]{5} [vo mim]{6,8} [Vatter]{7} [choo]{2}, und{9} [ir nämed]{11} [mich]{12} [nöd]{10} [aa]{11}; [wänn]{13} [en andere]{14} [i]{16} [sim eigete]{19,20} [Name]{17,18} [chunnt]{15}, [dä]{21} [wärded ir aanää]{22}.",
 "JHN.5.44": "[Wie]{1} [chönd]{2} [ir]{3} [glaube]{4}, [wo ir]{8} [Ehr]{5} [vonenand]{6,7} [aanämed]{8} und{9} [d Ehr]{10,11}, [wo]{12} [vo]{13} [em einzige]{14,15} [Gott]{16} chunnt, [nöd]{17} [sueched]{18}?",
 "JHN.5.45": "[Meined]{2} [nöd]{1}, [dass]{3} [ich]{4} [eu]{6} [bim]{7,8} [Vatter]{9} [verchlage wirde]{5}. [Es git]{10} [eine, wo]{11} [eu]{13} [verchlagt]{12}: [de Mose]{14}, [uf]{15} [dä]{16} [ir]{17} [eui Hoffnig gsetzt händ]{18}.",
 "JHN.5.46": "[Dänn]{2} [wänn]{1} [ir]{3} [em Mose]{4} [würded glaube]{3}, [würded ir]{6} [mir]{7} [glaube]{5}; [dänn]{9} [über]{8} [mich]{10} [hät]{12} [dä]{11} [gschribe]{12}.",
 "JHN.5.47": "[Wänn]{1} [ir]{7} [aber]{2} [sine]{4} [Schrifte]{3,5} [nöd]{6} [glaubed]{7}, [wie]{8} [wärded ir]{12} [mine]{10} [Wort]{9,11} [glaube]{12}?»",
}

GRUND = "Grundentscheid für Johannes (begründet in scripts/authoring/johannes_text_01_03.py)."
DEC_DE = [
 ("JHN.4.1", "gewinne", "adapted", "ποιεῖ", "mache", ["zu Jüngern mache"], "μαθητὰς ποιεῖν «Jünger machen» heisst: Menschen zu Schülern gewinnen."),
 ("JHN.4.4", "musste", "literal", "ἔδει", None, None, "δεῖ steht bei Johannes oft für Gottes Plan (vgl. [[JHN.3.14]]; [[JHN.3.30]]). Hier kann auch einfach der kürzeste Weg von Judäa nach Galiläa gemeint sein; der Text entscheidet das nicht."),
 ("JHN.4.6", "Quelle", "literal", "πηγὴ", None, ["Brunnen"], "Der Erzähler nennt die Stelle πηγή «Quelle» ([[JHN.4.6]]), die Frau φρέαρ «Brunnen», «Schacht» ([[JHN.4.11]]–[[JHN.4.12]]). Beide Wörter sind auseinandergehalten; πηγή kehrt in Jesu Wort von der Quelle in [[JHN.4.14]] wieder."),
 ("JHN.4.6", "wie er war", "interpretive", "οὕτως", "so", ["einfach so", "ohne Weiteres"], "οὕτως kann «so, wie er war» (müde, unvorbereitet) oder «einfach so» heissen."),
 ("JHN.4.6", "die sechste", "interpretive", "ὥρα ἦν ὡς ἕκτη", "Stunde war ungefähr die sechste", ["gegen Mittag"], "Nach der üblichen Zählung ab Sonnenaufgang etwa Mittag. Eine Minderheit rechnet bei Johannes mit einer Zählung ab Mitternacht (dann etwa 6 Uhr); das ist umstritten."),
 ("JHN.4.9", "ein Jude", "literal", "Ἰουδαῖος", None, None, "Ἰουδαῖος wird wörtlich mit «Jude» wiedergegeben. " + GRUND + " Hier bezeichnet die Samariterin Jesus nach seiner Volkszugehörigkeit; ebenso [[JHN.4.22]]."),
 ("JHN.4.9", "verkehren", "interpretive", "συγχρῶνται", None, ["benutzen keine Gefässe gemeinsam mit", "haben keinen Umgang mit"], "συγχράομαι heisst «gemeinsam gebrauchen» bzw. «Umgang haben». Manche verstehen den Satz enger: Juden benutzten keine Trinkgefässe gemeinsam mit Samaritern (aus Reinheitsgründen). Der Satz ist eine Erklärung des Erzählers."),
 ("JHN.4.10", "lebendiges", "literal", "ὕδωρ ζῶν", None, ["fliessendes"], "«Lebendiges Wasser» heisst im Alltag fliessendes Quellwasser (im Unterschied zu Zisternenwasser). Die Frau versteht es so ([[JHN.4.11]]); Jesus meint Wasser, das Leben gibt ([[JHN.4.14]]; vgl. [[JER.2.13]]). Der Doppelsinn ist beibehalten."),
 ("JHN.4.11", "Herr", "literal", "Κύριε", None, ["mein Herr"], "κύριε ist auch eine höfliche Anrede («mein Herr»). Die Übersetzung bleibt bei «Herr»; wie viel die Frau damit meint, zeigt erst der Verlauf des Gesprächs ([[JHN.4.19]]; [[JHN.4.29]])."),
 ("JHN.4.14", "ewige", "literal", "ζωὴν αἰώνιον", None, None, "ζωὴ αἰώνιος «ewiges Leben» meint im jüdischen Sprachgebrauch das Leben der kommenden Weltzeit; bei Johannes ist es schon gegenwärtig zugänglich ([[JHN.5.24]])."),
 ("JHN.4.20", "angebetet", "literal", "προσεκύνησαν", None, ["sich niedergeworfen"], "προσκυνέω bezeichnet die Gebärde des Niederfallens und die Anbetung. «Dieser Berg» ist nach dem Zusammenhang der Garizim, das Heiligtum der Samariter; der Name steht nicht im Text."),
 ("JHN.4.21", "Frau", "literal", "γύναι", None, None, "Die Anrede «Frau» ist im Griechischen nicht abweisend; Jesus redet auch seine Mutter so an ([[JHN.2.4]]; [[JHN.19.26]])."),
 ("JHN.4.21", "Es kommt", "literal", "ἔρχεται ὥρα", "Es kommt eine Stunde", None, "«Die Stunde» ist bei Johannes ein Leitwort ([[JHN.2.4]]; [[JHN.5.25]]; [[JHN.5.28]])."),
 ("JHN.4.23", "in", "interpretive", "ἐν πνεύματι καὶ ἀληθείᾳ", None, ["im Geist und in der Wahrheit"], "Ohne Artikel, wie im Griechischen. Ob πνεῦμα den Geist Gottes oder die innere, nicht an einen Ort gebundene Haltung meint, ist offen; Johannes verbindet beides ([[JHN.3.5]]–[[JHN.3.8]]). Ebenso [[JHN.4.24]]."),
 ("JHN.4.24", "Geist", "literal", "πνεῦμα ὁ θεός", None, ["Gott ist ein Geist"], "Ohne Verb: «Geist (ist) Gott». Gemeint ist nicht «ein Geist unter anderen», sondern Gottes Wesen; daher kein unbestimmter Artikel."),
 ("JHN.4.25", "der Messias", "literal", "Μεσσίας", None, None, "Μεσσίας gibt das hebräische bzw. aramäische Wort für «Gesalbter» wieder; χριστός ist die griechische Übersetzung (vgl. [[JHN.1.41]])."),
 ("JHN.4.26", "Ich bin es", "interpretive", "Ἐγώ εἰμι", None, ["Ich bin, der mit dir redet", "Ich bin’s, der mit dir redet"], "ἐγώ εἰμι wird bei Johannes einheitlich mit «Ich bin …» wiedergegeben. " + GRUND + " Als Antwort bzw. Identifikation steht «Ich bin es» (verbindlich für [[JHN.4.26]], [[JHN.6.20]], [[JHN.9.9]], [[JHN.18.5]]–[[JHN.18.8]]); hier antwortet es auf die Frage nach dem Messias. Manche hören zugleich einen Anklang an Gottes Selbstvorstellung (vgl. [[ISA.52.6]], griechisch ἐγώ εἰμι αὐτὸς ὁ λαλῶν); das ist eine Deutung."),
 ("JHN.4.29", "etwa", "interpretive", "μήτι", None, ["doch nicht etwa", "ob er wohl"], "μήτι leitet eine vorsichtige Frage ein, die eher Zweifel ausdrückt; hier klingt zugleich Hoffnung an."),
 ("JHN.4.34", "vollende", "literal", "τελειώσω", None, None, "τελειόω «vollenden» nimmt Johannes in [[JHN.5.36]] und [[JHN.17.4]] wieder auf; vgl. τετέλεσται in [[JHN.19.30]]."),
 ("JHN.4.35", "Schon", "interpretive", "ἤδη", None, ["dass sie schon weiss sind zur Ernte"], "Der SBLGNT setzt vor ἤδη ein Satzzeichen und zieht es zum folgenden Satz ([[JHN.4.36]]: «Schon empfängt der Schnitter Lohn»); die Verszählung lässt es in [[JHN.4.35]]. Andere Ausgaben verbinden es mit «weiss zur Ernte»."),
 ("JHN.4.39", "glaubten", "literal", "ἐπίστευσαν εἰς αὐτὸν", None, ["kamen zum Glauben an ihn"], "πιστεύω ist ein Leitwort des Evangeliums (98-mal nach den MACULA-Lemmata im SBLGNT-Text) und wird durchgehend mit «glauben» wiedergegeben."),
 ("JHN.4.42", "der Retter", "literal", "ὁ σωτὴρ τοῦ κόσμου", None, ["der Heiland der Welt"], "σωτήρ heisst «Retter»; κόσμος wird einheitlich mit «Welt» wiedergegeben. " + GRUND),
 ("JHN.4.44", "Heimat", "interpretive", "πατρίδι", None, ["Vaterstadt", "Vaterland"], "Welche Heimat gemeint ist, ist umstritten: Galiläa (vgl. [[JHN.1.46]]), dann wäre die freundliche Aufnahme ([[JHN.4.45]]) oberflächlich; oder Judäa bzw. Jerusalem, das Jesus eben verlassen hat. Das «nämlich» (γάρ) lässt beide Lesarten zu."),
 ("JHN.4.46", "königlicher Beamter", "interpretive", "βασιλικὸς", None, ["Hofbeamter", "Königlicher"], "βασιλικός «königlich» meint wohl einen Beamten oder Offizier im Dienst des Herodes Antipas, der in Galiläa als «König» bezeichnet wurde; auch ein Verwandter des Königshauses ist sprachlich möglich."),
 ("JHN.4.48", "Zeichen", "literal", "σημεῖα καὶ τέρατα", None, None, "σημεῖον wird einheitlich mit «Zeichen» wiedergegeben, nicht mit «Wunder»: Johannes betont, dass die Taten auf Jesus hinweisen. " + GRUND + " τέρας «Wunder», «Vorzeichen» steht nur hier in der festen Verbindung «Zeichen und Wunder». Das «ihr» ist Plural: Jesus spricht über den Beamten hinaus."),
 ("JHN.4.51", "Knechte", "literal", "δοῦλοι", None, ["Sklaven", "Diener"], "δοῦλος bezeichnet einen unfreien Diener."),
 ("JHN.4.51", "Junge", "literal", "παῖς", None, ["Kind", "Knabe"], "Für das Kind stehen nebeneinander υἱός «Sohn» ([[JHN.4.46]]), παιδίον «Kind» ([[JHN.4.49]]) und παῖς «Junge» (hier); die Wörter sind unterschieden wiedergegeben."),
 ("JHN.4.52", "um die siebte", "interpretive", "ὥραν ἑβδόμην", None, None, "Nach der Zählung ab Sonnenaufgang etwa 13 Uhr (vgl. [[JHN.4.6]])."),
 ("JHN.4.54", "als zweites", "literal", "πάλιν δεύτερον σημεῖον", "wiederum ein zweites Zeichen", None, "Das erste Zeichen ist der Wein in Kana ([[JHN.2.11]]). Die Zählung bezieht sich auf die Zeichen in Galiläa; in Jerusalem erwähnt [[JHN.2.23]] weitere Zeichen."),
 ("JHN.5.1", "ein Fest", "literal", "ἑορτὴ", None, None, "Welches Fest gemeint ist, sagt der SBLGNT-Text nicht (ohne Artikel). Mit Artikel («das Fest», siehe Alternative) dachten Ausleger an das Laubhüttenfest oder das Passa."),
 ("JHN.5.2", "Es gibt", "literal", "ἔστιν", None, None, "Präsens: Der Teich wird als noch bestehend beschrieben. Manche schliessen daraus auf eine Abfassung vor 70 n. Chr., andere halten es für erzählerisches Präsens."),
 ("JHN.5.2", "Schaftor", "interpretive", "ἐπὶ τῇ προβατικῇ", "bei dem Schafs-", ["beim Schafteich", "beim Schafmarkt"], "προβατική «zu den Schafen gehörig» braucht ein ergänztes Wort. Meist wird «Tor» ergänzt (vgl. das Schaftor in [[NEH.3.1]]); verbindet man προβατικῇ mit κολυμβήθρᾳ, ergibt sich «beim Schafteich» und der Name gehört zu einem anderen Ort."),
 ("JHN.5.2", "auf Hebräisch", "literal", "Ἑβραϊστὶ", None, ["auf Aramäisch"], "Ἑβραϊστί bezeichnet hier wohl die Landessprache, die damals in Judäa überwiegend Aramäisch war. Der Name ist in den Handschriften sehr unterschiedlich überliefert (siehe Alternative)."),
 ("JHN.5.3", "Ausgezehrte", "interpretive", "ξηρῶν", "Vertrocknete", ["Gelähmte", "Verkrüppelte"], "ξηρός «trocken, verdorrt» bezeichnet abgemagerte oder gelähmte Glieder (vgl. die «verdorrte Hand» in [[MRK.3.1]])."),
 ("JHN.5.8", "Matte", "adapted", "κράβαττόν", None, ["Bahre", "Tragbett", "Liege"], "κράβαττος ist ein einfaches Lager oder eine Tragbahre, die man zusammenrollen und tragen kann."),
 ("JHN.5.10", "die Juden", "interpretive", "οἱ Ἰουδαῖοι", None, ["die jüdischen Führer", "die jüdischen Behörden", "die Judäer"], "Wörtlich «die Juden» (" + GRUND + "). Nach dem Zusammenhang sind hier Autoritäten in Jerusalem gemeint, die über die Sabbatpraxis wachen und Jesus verfolgen; der Geheilte und Jesus sind selbst Juden. «Die jüdischen Führer» wäre eine deutende Wiedergabe. Ebenso [[JHN.5.15]], [[JHN.5.16]] und [[JHN.5.18]]."),
 ("JHN.5.17", "wirkt", "literal", "ἐργάζεται", None, ["arbeitet"], "ἐργάζομαι «arbeiten, wirken». Das Wort greift den Sabbatvorwurf auf: Nach jüdischer Auslegung jener Zeit (etwa bei Philo von Alexandria) ruht Gott auch am Sabbat nicht vom Erhalten und Richten der Welt; dieser Hintergrund ist eine verbreitete Erklärung, keine Aussage des Textes."),
 ("JHN.5.18", "auflöste", "literal", "ἔλυε", None, ["brach", "ausser Kraft setzte"], "λύω «lösen, auflösen». Imperfekt: wiederholtes oder grundsätzliches Tun."),
 ("JHN.5.19", "Amen", "literal", "Ἀμὴν ἀμὴν", "Amen, amen", ["Wahrlich, wahrlich", "Ganz gewiss"], "Das doppelte Amen steht nur bei Johannes (25-mal im SBLGNT-Text) und wird einheitlich mit «Amen, amen» wiedergegeben. " + GRUND),
 ("JHN.5.20", "hat den Sohn lieb", "literal", "φιλεῖ τὸν υἱὸν", None, ["liebt den Sohn"], "Hier steht φιλέω, in derselben Aussage [[JHN.3.35]] ἀγαπάω. Grundentscheid: ἀγαπάω «lieben», φιλέω «lieb haben», damit der Wechsel der Verben sichtbar bleibt; ob Johannes damit einen Bedeutungsunterschied verbindet, ist umstritten (vgl. [[JHN.21.15]]–[[JHN.21.17]])."),
 ("JHN.5.22", "Gericht", "literal", "κρίσιν", None, ["Urteil"], "κρίσις und κρίνω umfassen das Richten und das Verurteilen; einheitlich «Gericht» bzw. «richten»."),
 ("JHN.5.24", "Wort", "literal", "λόγον", None, None, "λόγος wird einheitlich mit «Wort» wiedergegeben. " + GRUND),
 ("JHN.5.24", "hinübergegangen", "literal", "μεταβέβηκεν", None, None, "Perfekt: Der Übergang vom Tod ins Leben ist schon geschehen und wirkt fort."),
 ("JHN.5.27", "der Menschensohn", "interpretive", "υἱὸς ἀνθρώπου", "Sohn eines Menschen", ["ein Menschensohn", "ein Mensch"], "Nur hier im Evangelium ohne Artikel, wie in der griechischen Fassung von [[DAN.7.13]], wo «einer wie ein Menschensohn» Herrschaft empfängt. Man kann es als Titel lesen (Daniel) oder als Hinweis auf Jesu Menschsein (weil er Mensch ist, richtet er Menschen)."),
 ("JHN.5.29", "Auferstehung", "literal", "ἀνάστασιν ζωῆς", None, ["Auferstehung zum Leben"], "Vgl. [[DAN.12.2]]."),
 ("JHN.5.31", "wahr", "interpretive", "ἀληθής", None, ["gültig"], "Gemeint ist die rechtliche Geltung eines Zeugnisses: Ein einzelner Zeuge in eigener Sache genügt nicht (vgl. [[DEU.19.15]]). Später sagt Jesus, sein Zeugnis sei auch dann wahr ([[JHN.8.14]])."),
 ("JHN.5.32", "Ein anderer", "interpretive", "ἄλλος", None, None, "Wer gemeint ist, ist umstritten: meist der Vater ([[JHN.5.37]]), manche denken an Johannes ([[JHN.5.33]])."),
 ("JHN.5.35", "die Lampe", "literal", "ὁ λύχνος", None, ["das Licht"], "λύχνος ist eine Öllampe; «das Licht» (φῶς) ist Johannes nach [[JHN.1.8]] gerade nicht."),
 ("JHN.5.36", "gesandt hat", "literal", "ἀπέσταλκεν", None, None, "ἀποστέλλω und πέμπω werden bei Johannes gleichbedeutend gebraucht und beide mit «senden» wiedergegeben."),
 ("JHN.5.38", "bleibt", "literal", "μένοντα", None, None, "μένω wird einheitlich mit «bleiben» wiedergegeben (40-mal nach den MACULA-Lemmata im SBLGNT-Text). " + GRUND),
 ("JHN.5.39", "Ihr erforscht", "interpretive", "Ἐραυνᾶτε", None, ["Erforscht"], "Die Form kann Aussage oder Aufforderung sein. Der Zusammenhang («weil ihr meint …») spricht eher für die Aussage."),
 ("JHN.5.41", "Ehre", "adapted", "δόξαν", None, ["Herrlichkeit", "Anerkennung"], "δόξα wird bei Johannes mit «Herrlichkeit» wiedergegeben (" + GRUND + "). Wo es um Ansehen bei Menschen geht, steht «Ehre»; dass dasselbe Wort gemeint ist wie in «Herrlichkeit» ([[JHN.1.14]]), soll diese Entscheidung sichtbar halten. Zu [[JHN.5.44]] siehe dort."),
 ("JHN.5.44", "Ehre", "adapted", "δόξαν", None, ["Herrlichkeit", "Anerkennung"], "Zweimal δόξα: die Ehre, die Menschen voneinander annehmen, und die Ehre von Gott. Weil es um Ansehen und Anerkennung geht, steht «Ehre» (wie [[JHN.5.41]]); dass Johannes dasselbe Wort braucht wie für die Herrlichkeit ([[JHN.1.14]]), geht im Deutschen verloren."),
 ("JHN.5.42", "die Liebe zu Gott", "interpretive", "τὴν ἀγάπην τοῦ θεοῦ", "die Liebe Gottes", None, "Der Genitiv kann die Liebe zu Gott oder Gottes eigene Liebe meinen; beides wird vertreten."),
 ("JHN.5.47", "Worten", "literal", "ῥήμασιν", None, None, "Hier ῥῆμα «Wort, Ausspruch», nicht λόγος; gegenübergestellt sind die «Schriften» (γράμματα) des Mose."),
]
DEC_GSW = [
 ("JHN.4.6", "Quälle", "literal", "πηγὴ", None, ["Brunne"], "De Erzähler seit πηγή «Quälle», d Frau φρέαρ «Brunne» ([[JHN.4.11]]); beidi Wort sind usenandghalte."),
 ("JHN.4.9", "en Jud", "literal", "Ἰουδαῖος", None, None, "Ἰουδαῖος wörtlich «Jud». " + "Grundentscheid für Johannes (begründet in scripts/authoring/johannes_text_01_03.py)."),
 ("JHN.4.9", "nüüt", "interpretive", "συγχρῶνται", None, ["kei Gschirr mitenand bruuche"], "συγχράομαι heisst «mitenand bruuche» oder «Umgang ha»."),
 ("JHN.4.10", "läbigs", "literal", "ὕδωρ ζῶν", None, ["fliessends"], "«Läbigs Wasser» heisst im Alltag fliessends Quällwasser; de Jesus meint Wasser, wo Läbe git ([[JHN.4.14]]). De Doppelsinn isch bhalte."),
 ("JHN.4.26", "Ich bi s", "interpretive", "Ἐγώ εἰμι", None, ["Ich bi, wo mit dir redt"], "ἐγώ εἰμι isch bim Johannes überall «Ich bi …»; als Antwort «Ich bi s». Da isch es d Antwort uf d Frag nach em Messias; mänggi ghöred au en Aaklang a Gott, wo sich vorstellt ([[ISA.52.6]]). Das isch e Düütig."),
 ("JHN.4.35", "Scho", "interpretive", "ἤδη", None, ["dass si scho wiiss sind"], "De SBLGNT zieht ἤδη zum nächschte Satz ([[JHN.4.36]])."),
 ("JHN.4.42", "de Retter", "literal", "ὁ σωτὴρ τοῦ κόσμου", None, ["de Heiland vo de Wält"], "κόσμος einheitlich «Wält»."),
 ("JHN.4.48", "Zeiche", "literal", "σημεῖα", None, None, "σημεῖον einheitlich «Zeiche», nöd «Wunder»; τέρατα isch «Wunder»."),
 ("JHN.5.2", "Schaaftor", "interpretive", "ἐπὶ τῇ προβατικῇ", None, ["Schaafteich"], "«Tor» isch ergänzt (vgl. [[NEH.3.1]])."),
 ("JHN.5.8", "Matte", "adapted", "κράβαττόν", None, ["Bahre", "Liegi"], None),
 ("JHN.5.10", "d Jude", "interpretive", "οἱ Ἰουδαῖοι", None, ["di jüdische Füerer", "di jüdische Behörde"], "Wörtlich «d Jude» (Grundentscheid). Gmeint sind da Autoritäte z Jerusalem; de Gheilt und de Jesus sind sälber Jude."),
 ("JHN.5.19", "Amen", "literal", "Ἀμὴν ἀμὴν", None, None, "S doppelt Amen einheitlich «Amen, amen, ich säge eu»."),
 ("JHN.5.27", "de Mänschesohn", "interpretive", "υἱὸς ἀνθρώπου", "Sohn vo me Mänsch", ["en Mänsch"], "Nu da ohni Artikel, wie i de griechische Fassig vo [[DAN.7.13]]."),
 ("JHN.5.38", "bliibt", "literal", "μένοντα", None, None, "μένω einheitlich «bliibe»."),
 ("JHN.5.39", "Ir erforsched", "interpretive", "Ἐραυνᾶτε", None, ["Erforsched"], "D Form cha Uussag oder Ufforderig sii."),
 ("JHN.5.41", "Ehr", "adapted", "δόξαν", None, ["Herrlichkeit", "Aaerchännig"], "δόξα isch süsch «Herrlichkeit»; wo s um Aasee bi Mänsche gaat, staat «Ehr». Lueg au [[JHN.5.44]]."),
 ("JHN.5.44", "Ehr", "adapted", "δόξαν", None, ["Herrlichkeit", "Aaerchännig"], "Zweimal δόξα: d Ehr, wo d Mänsche vonenand nämed, und die vo Gott. Wil s um s Aasee gaat, staat «Ehr» (wie [[JHN.5.41]]); dass s s gliich Wort isch wie «Herrlichkeit», gaat verlore."),
 ("JHN.5.20", "hät de Sohn gärn", "literal", "φιλεῖ τὸν υἱὸν", None, ["liebt de Sohn"], "Da staat φιλέω, i [[JHN.3.35]] ἀγαπάω. Grundentscheid: ἀγαπάω «liebe», φιλέω «gärn haa», demit me de Wächsel gseht."),
]

ALTS = [
 ("VAR-SBLGNTAPP-JHN-004-001-01:R2", "JHN.4.1", "Als nun Jesus erfuhr", "Als nun der Herr erfuhr", "Wo de Jesus jetzt erfaare hät", "Wo de Herr jetzt erfaare hät", "gering",
  "κύριος «der Herr» statt Ἰησοῦς. Der SBLGNT-Text folgt hier NA28; WH, Treg, NIV und RP lesen κύριος.", "κύριος «de Herr» statt Ἰησοῦς. De SBLGNT folgt da NA28; WH, Treg, NIV und RP läsed κύριος.",
  {"R1": [("Ἰησοῦς", "Jesus", "SBLGNT, NA28")], "R2": [("κύριος", "der Herr", "WH, Treg, NIV, RP")]},
  {"R1": [("Ἰησοῦς", "de Jesus", "SBLGNT, NA28")], "R2": [("κύριος", "de Herr", "WH, Treg, NIV, RP")]},
  ["Weil der Satz Jesus kurz darauf noch einmal nennt, kann «der Herr» eingesetzt worden sein, um die Wiederholung zu vermeiden; umgekehrt kann «Jesus» den Titel verdeutlicht haben.",
   "In den CNTR-Transkriptionen steht bei 02, 03, 04, 032 und 𝔓75 sowie in der Korrektur von 𝔓66 die Abkürzung für κύριος (κσ), bei 01, 05 und in der Erstschrift von 𝔓66 die Abkürzung für Ἰησοῦς. Die automatische Zuordnung hat diese Abkürzungen keiner Lesart zugeordnet («liest anders»); die Angabe beruht auf dem erfassten Wortlaut."],
  ["Wil de Satz de Jesus grad nachher nomal nännt, cha «de Herr» iigsetzt worde sii, zum d Widerholig vermiide; umgekehrt cha «Jesus» de Titel verdüütlicht ha.",
   "I de CNTR-Transkriptione staat bi 02, 03, 04, 032 und 𝔓75 und i de Korrektur vo 𝔓66 d Abchürzig für κύριος, bi 01, 05 und i de Erschtschrift vo 𝔓66 die für Ἰησοῦς."]),
 ("VAR-SBLGNTAPP-JHN-004-042-01:R2", "JHN.4.42", "der Retter der Welt ist", "wirklich der Retter der Welt, der Christus, ist", "de Retter vo de Wält isch", "würkli de Retter vo de Wält, de Christus, isch", "gering",
  "Mit dem Zusatz «der Christus».", "Mit em Zuesatz «de Christus».",
  {"R1": [("κόσμου", "der Welt", None)], "R2": [("κόσμου ὁ χριστός", "der Welt, der Christus", "mit Zusatz")]},
  {"R1": [("κόσμου", "vo de Wält", None)], "R2": [("κόσμου ὁ χριστός", "vo de Wält, de Christus", "mit Zuesatz")]},
  ["Der Zusatz nimmt die Frage der Frau ([[JHN.4.29]]) auf und kann als Verdeutlichung ergänzt worden sein.",
   "Laut der automatischen Zuordnung haben 01, 02, 03, 04, 032, 𝔓66 und 𝔓75 keinen Zusatz, 05 hat ihn; unter den gedruckten Ausgaben haben ihn KJTR, RP und Stephanus."],
  ["De Zuesatz nimmt d Frag vo de Frau ([[JHN.4.29]]) uf.",
   "Nach de automatische Zueornig händ 01, 02, 03, 04, 032, 𝔓66 und 𝔓75 kei Zuesatz, 05 hät en."]),
 ("VAR-SBLGNTAPP-JHN-004-051-03:R2", "JHN.4.51", "sein Junge lebe", "«Dein Junge lebt!»", "sin Bueb läbi", "«Din Bueb läbt!»", "gering",
  "σου «dein» statt αὐτοῦ «sein»: Die Botschaft der Knechte wird zur direkten Rede.", "σου «din» statt αὐτοῦ «sin»: D Botschaft vo de Chnächt wird diräkti Red.",
  {"R1": [("αὐτοῦ", "sein", None)], "R2": [("σου", "dein", None)]},
  {"R1": [("αὐτοῦ", "sin", None)], "R2": [("σου", "din", None)]},
  ["«Dein» gleicht die Meldung an das Wort Jesu an ([[JHN.4.50]]; [[JHN.4.53]]).",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 04, 032, 𝔓45, 𝔓66 (Erstschrift) und 𝔓75 αὐτοῦ; 05 und die Korrektur in 𝔓66 haben σου, zusammen mit υἱός «Sohn» statt παῖς."],
  ["«Din» glicht d Mäldig as Wort vom Jesus aa ([[JHN.4.50]]).",
   "Nach de automatische Zueornig läsed 01, 02, 03, 04, 032, 𝔓45, 𝔓66 (Erschtschrift) und 𝔓75 αὐτοῦ; 05 und d Korrektur i 𝔓66 händ σου."]),
 ("VAR-SBLGNTAPP-JHN-005-001-01:R2", "JHN.5.1", "ein Fest der Juden", "das Fest der Juden", "es Fäscht vo de Jude", "s Fäscht vo de Jude", "mittel",
  "Mit Artikel ist ein bestimmtes, bekanntes Fest gemeint.", "Mit Artikel isch es bestimmts, bekannts Fäscht gmeint.",
  {"R1": [("ἑορτή", "ein Fest", None)], "R2": [("ἡ ἑορτή", "das Fest", "mit Artikel")]},
  {"R1": [("ἑορτή", "es Fäscht", None)], "R2": [("ἡ ἑορτή", "s Fäscht", "mit Artikel")]},
  ["Mit Artikel dachten Ausleger meist an das Laubhüttenfest oder das Passa; der Artikel kann ergänzt worden sein, um das Fest näher zu bestimmen, oder ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 04 mit Artikel, 02, 03, 05, 029, 032, 𝔓45, 𝔓66 und 𝔓75 ohne."],
  ["Mit Artikel händ Uusleger meischt as Laubhüttefäscht oder as Passa tänkt.",
   "Nach de automatische Zueornig läsed 01 und 04 mit Artikel, 02, 03, 05, 029, 032, 𝔓45, 𝔓66 und 𝔓75 ohni."]),
 ("VAR-SBLGNTAPP-JHN-005-002-01:R2", "JHN.5.2", "Betesda", "Betzata", "Betesda", "Betzata", "gering",
  "Anderer Name des Teiches. Der SBLGNT-Text folgt hier Treg, NIV und RP; WH und NA28 lesen Βηθζαθά.", "En andere Name vom Teich. De SBLGNT folgt da Treg, NIV und RP; WH und NA28 läsed Βηθζαθά.",
  {"R1": [("Βηθεσδά", "Betesda", "SBLGNT, Treg, NIV, RP")], "R2": [("Βηθζαθά", "Betzata", "WH, NA28")]},
  {"R1": [("Βηθεσδά", "Betesda", "SBLGNT, Treg, NIV, RP")], "R2": [("Βηθζαθά", "Betzata", "WH, NA28")]},
  ["Der fremde Ortsname wurde von den Abschreibern sehr unterschiedlich geschrieben; Βηθεσδά kann als «Haus der Barmherzigkeit» gedeutet werden, was eine Angleichung an die Heilung begünstigt haben könnte.",
   "Im erfassten Wortlaut der CNTR-Transkriptionen: 02 und 04 βηθεσδα; 01 βηθζαθα; 03, 029, 032 und 𝔓75 βηθσαιδα («Betsaida»); 𝔓66 βηδσαιδα(ν); 05 βελζεθα. Die automatische Zuordnung führt die Betsaida-Formen bei R1, sie sind aber ein dritter Name."],
  ["De fremd Ortsname isch vo de Abschriiber sehr verschide gschribe worde.",
   "Im erfasste Wortlut: 02 und 04 βηθεσδα; 01 βηθζαθα; 03, 029, 032 und 𝔓75 βηθσαιδα («Betsaida»); 𝔓66 βηδσαιδα(ν); 05 βελζεθα."]),
 ("VAR-SBLGNTAPP-JHN-005-003-01:R2", "JHN.5.3", "eine Menge", "eine grosse Menge", "e Mängi", "e grossi Mängi", "gering",
  "Mit πολύ «gross».", "Mit πολύ «gross».",
  {"R1": [("πλῆθος", "eine Menge", None)], "R2": [("πλῆθος πολύ", "eine grosse Menge", "mit Zusatz")]},
  {"R1": [("πλῆθος", "e Mängi", None)], "R2": [("πλῆθος πολύ", "e grossi Mängi", "mit Zuesatz")]},
  ["Das Wort kann als Verstärkung ergänzt worden sein.",
   "Laut der automatischen Zuordnung hat 02 den Zusatz; 01, 03, 04, 05, 029, 032, 𝔓66 und 𝔓75 haben ihn nicht."],
  ["S Wort cha als Verstercherig ergänzt worde sii.",
   "Nach de automatische Zueornig hät 02 de Zuesatz; 01, 03, 04, 05, 029, 032, 𝔓66 und 𝔓75 händ en nöd."]),
 ("VAR-SBLGNTAPP-JHN-005-003-02:R2", "JHN.5.3", "Blinde, Lahme, Ausgezehrte.",
  "Blinde, Lahme, Ausgezehrte, die auf die Bewegung des Wassers warteten. [4] Ein Engel stieg nämlich von Zeit zu Zeit in den Teich hinab und wühlte das Wasser auf; wer nun nach dem Aufwühlen des Wassers als Erster hineinstieg, wurde gesund, mit welcher Krankheit er auch behaftet war.",
  "Blindi, Lahmi, Uusgmerglete.",
  "Blindi, Lahmi, Uusgmerglete, wo uf d Bewegig vom Wasser gwartet händ. [4] En Ängel isch nämli vo Ziit zu Ziit i de Teich abegstige und hät s Wasser ufgwüelt; wer dänn nach em Ufwüele als Erschte inegstige isch, isch gsund worde, ganz egal, was für e Chranket er gha hät.",
  "bedeutsam",
  "Mit dem Zusatz am Ende von [[JHN.5.3]] und einem eigenen Vers [[JHN.5.4]] wird erklärt, warum die Kranken am Teich liegen und was der Kranke in [[JHN.5.7]] mit dem Aufwühlen des Wassers meint. Im SBLGNT fehlt beides; deshalb hat [[JHN.5.4]] hier keinen Text. Der Zusatz gilt in der Textforschung weithin als spätere Erläuterung; das ist ein verbreitetes Urteil, keine Feststellung dieser Übersetzung.",
  "Mit em Zuesatz am Änd vo [[JHN.5.3]] und eme eigete Vers [[JHN.5.4]] wird erklärt, wieso d Chranke am Teich ligged und was de Chrank i [[JHN.5.7]] mit em Ufwüele vom Wasser meint. Im SBLGNT fäält beides; drum hät [[JHN.5.4]] da kei Text. I de Textforschig gilt de Zuesatz wiitume als spööteri Erlüüterig.",
  {"R1": [("ξηρῶν", "Ausgezehrte (ohne Zusatz und ohne Vers 4)", "SBLGNT, WH, Treg, NA28")],
   "R2": [("ξηρῶν, ἐκδεχομένων τὴν τοῦ ὕδατος κίνησιν. 4 ἄγγελος γὰρ κατὰ καιρὸν κατέβαινεν ἐν τῇ κολυμβήθρᾳ, καὶ ἐτάρασσεν τὸ ὕδωρ· ὁ οὖν πρῶτος ἐμβὰς μετὰ τὴν ταραχὴν τοῦ ὕδατος, ὑγιὴς ἐγίνετο, ᾧ δήποτε κατείχετο νοσήματι",
          "Ausgezehrte, die auf die Bewegung des Wassers warteten. 4 Ein Engel stieg nämlich von Zeit zu Zeit in den Teich hinab und wühlte das Wasser auf; wer nun nach dem Aufwühlen des Wassers als Erster hineinstieg, wurde gesund, mit welcher Krankheit er auch behaftet war.", "RP; Zusatz in 5,3 und Vers 4")]},
  {"R1": [("ξηρῶν", "Uusgmerglete (ohni Zuesatz und ohni Vers 4)", "SBLGNT, WH, Treg, NA28")],
   "R2": [("ξηρῶν, ἐκδεχομένων τὴν τοῦ ὕδατος κίνησιν. 4 ἄγγελος γὰρ κατὰ καιρὸν κατέβαινεν ἐν τῇ κολυμβήθρᾳ, καὶ ἐτάρασσεν τὸ ὕδωρ· ὁ οὖν πρῶτος ἐμβὰς μετὰ τὴν ταραχὴν τοῦ ὕδατος, ὑγιὴς ἐγίνετο, ᾧ δήποτε κατείχετο νοσήματι",
          "Uusgmerglete, wo uf d Bewegig vom Wasser gwartet händ. 4 En Ängel isch nämli vo Ziit zu Ziit i de Teich abegstige und hät s Wasser ufgwüelt; wer dänn nach em Ufwüele als Erschte inegstige isch, isch gsund worde, ganz egal, was für e Chranket er gha hät.", "RP; Zuesatz in 5,3 und Vers 4")]},
  ["Der Zusatz kann als Erklärung entstanden sein, damit die Bemerkung des Kranken über das aufgewühlte Wasser ([[JHN.5.7]]) verständlich wird; er gibt eine volkstümliche Erklärung für ein zeitweises Aufwallen des Wassers wieder. Wer ihn für ursprünglich hält, erklärt das Fehlen damit, dass Abschreiber an der Engelsvorstellung Anstoss nahmen. Die Textforschung urteilt weithin, dass er nicht ursprünglich ist; viele Kirchen und Ausgaben, die dem Mehrheitstext folgen, lesen ihn als Teil des Textes.",
   "Nach den CNTR-Transkriptionen (die automatische Kollation erfasst den Zusatz nicht, weil ihr Vergleichsfenster bei ξηρῶν endet): Den Zusatz am Ende von [[JHN.5.3]] («die auf die Bewegung des Wassers warteten») haben 05 (zusätzlich mit παραλυτικῶν «Gelähmte»), 032 (in der Form ἐκδεχόμενοι) und 02 als Korrektur; die Erstschrift von 02 hat ihn nicht. Ohne ihn enden 01, 03, 04, 029, 𝔓66 und 𝔓75 mit ξηρῶν. Für Vers 4 ist nur in 02 Text erfasst, mit Abweichungen (ἄγγελος γὰρ κυρίου «ein Engel des Herrn», ἐλούετο «badete» statt κατέβαινεν «stieg hinab»); bei 01, 03, 04, 05, 029, 032, 𝔓66 und 𝔓75 ist für Vers 4 kein Text erfasst, bei 𝔓45 ist die Stelle nicht sicher erhalten. Unter den gedruckten Ausgaben haben KJTR, RP und Stephanus Zusatz und Vers 4, WH und SR nicht. Der Zusatz in [[JHN.5.3]] und Vers [[JHN.5.4]] sind in den Handschriften also nicht immer zusammen überliefert."],
  ["De Zuesatz cha als Erklärig entstande sii, demit d Bemerkig vom Chranke über s ufgwüelt Wasser ([[JHN.5.7]]) verständlich wird. Wer en für ursprünglich hebt, erklärt s Fääle demit, dass Abschriiber a de Ängelsvorstellig Aastoss gnoo händ. D Textforschig urteilt wiitume, dass er nöd ursprünglich isch; vili Chile und Usgabe, wo em Mehrheitstext folged, läsed en als Teil vom Text.",
   "Nach de CNTR-Transkriptione: De Zuesatz am Änd vo [[JHN.5.3]] händ 05, 032 und 02 als Korrektur; ohni en sind 01, 03, 04, 029, 𝔓66 und 𝔓75. Für Vers 4 isch nu i 02 Text erfasst (mit Abwiichige); bi 01, 03, 04, 05, 029, 032, 𝔓66 und 𝔓75 isch für Vers 4 kei Text erfasst. KJTR, RP und Stephanus händ Zuesatz und Vers 4, WH und SR nöd."]),
 ("VAR-SBLGNTAPP-JHN-005-016-01:R2", "JHN.5.16", "verfolgten die Juden Jesus", "verfolgten die Juden Jesus und suchten ihn zu töten", "händ d Jude de Jesus verfolgt", "händ d Jude de Jesus verfolgt und gsuecht, en z töte", "mittel",
  "Mit dem Zusatz steht die Tötungsabsicht schon hier und nicht erst in [[JHN.5.18]].", "Mit em Zuesatz staat d Absicht, en z töte, scho da und nöd erscht i [[JHN.5.18]].",
  {"R1": [("ἐδίωκον οἱ Ἰουδαῖοι τὸν Ἰησοῦν", "verfolgten die Juden Jesus", None)], "R2": [("ἐδίωκον τὸν Ἰησοῦν οἱ Ἰουδαῖοι καὶ ἐζήτουν αὐτὸν ἀποκτεῖναι", "verfolgten die Juden Jesus und suchten ihn zu töten", "mit Zusatz")]},
  {"R1": [("ἐδίωκον οἱ Ἰουδαῖοι τὸν Ἰησοῦν", "händ d Jude de Jesus verfolgt", None)], "R2": [("ἐδίωκον τὸν Ἰησοῦν οἱ Ἰουδαῖοι καὶ ἐζήτουν αὐτὸν ἀποκτεῖναι", "händ d Jude de Jesus verfolgt und gsuecht, en z töte", "mit Zuesatz")]},
  ["Der Zusatz kann aus [[JHN.5.18]] vorweggenommen sein; das «umso mehr» dort setzt eine frühere Tötungsabsicht nicht zwingend voraus.",
   "Im erfassten Wortlaut hat 02 den Zusatz; 01, 03, 04, 05, 032, 𝔓66 und 𝔓75 haben ihn nicht (die automatische Zuordnung führt die meisten wegen des vorangestellten καί als «liest anders»)."],
  ["De Zuesatz cha us [[JHN.5.18]] vorwäggnoo sii.",
   "Im erfasste Wortlut hät 02 de Zuesatz; 01, 03, 04, 05, 032, 𝔓66 und 𝔓75 händ en nöd."]),
 ("VAR-SBLGNTAPP-JHN-005-030-01:R2", "JHN.5.30", "dessen, der mich gesandt hat", "des Vaters, der mich gesandt hat", "vo däm, wo mich gschickt hät", "vom Vatter, wo mich gschickt hät", "gering",
  "Mit «Vater».", "Mit «Vatter».",
  {"R1": [("τοῦ πέμψαντός με", "dessen, der mich gesandt hat", None)], "R2": [("τοῦ πέμψαντός με πατρός", "des Vaters, der mich gesandt hat", "mit Zusatz")]},
  {"R1": [("τοῦ πέμψαντός με", "vo däm, wo mich gschickt hät", None)], "R2": [("τοῦ πέμψαντός με πατρός", "vom Vatter, wo mich gschickt hät", "mit Zuesatz")]},
  ["«Vater» macht ausdrücklich, was der Zusammenhang sagt (vgl. [[JHN.5.37]]).",
   "Laut der automatischen Zuordnung haben 01, 02, 03, 05, 032, 𝔓66 und 𝔓75 keinen Zusatz (04 ist hier nicht erhalten); unter den gedruckten Ausgaben haben ihn KJTR, RP und Stephanus."],
  ["«Vatter» macht usdrücklich, was de Zämehang seit.",
   "Nach de automatische Zueornig händ 01, 02, 03, 05, 032, 𝔓66 und 𝔓75 kei Zuesatz; KJTR, RP und Stephanus händ en."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-004-001-054", "JHN.4.1-JHN.4.54", "section", "Jesus in Samarien und das zweite Zeichen in Kana",
  ["TU-JHN-004-001-015", "TU-JHN-004-016-026", "TU-JHN-004-027-038", "TU-JHN-004-039-042", "TU-JHN-004-043-054"],
  "Als Jesus erfährt, die Pharisäer hätten gehört, dass er mehr Jünger gewinne und taufe als Johannes, verlässt er Judäa und zieht durch Samarien nach Galiläa. An der Jakobsquelle bei Sychar bittet er eine samaritische Frau um Wasser und spricht mit ihr über lebendiges Wasser, über ihre Männer und über die Anbetung des Vaters in Geist und Wahrheit; auf ihre Erwartung des Messias antwortet er: «Ich bin es, der mit dir redet.» Die Frau ruft die Leute ihrer Stadt; Jesus spricht zu den Jüngern von seiner Speise und von der Ernte. Viele Samariter glauben an ihn und nennen ihn den Retter der Welt. In Kana bittet ihn ein königlicher Beamter um Hilfe für seinen todkranken Sohn in Kafarnaum; Jesus sagt ihm: «Dein Sohn lebt», und der Mann erfährt, dass das Fieber den Jungen in eben der Stunde verlassen hat, in der Jesus das sagte. Er und sein ganzes Haus glauben; es ist das zweite Zeichen Jesu.", SEG),
 ("TU-JHN-004-001-015", "JHN.4.1-JHN.4.15", "dialogue", "Lebendiges Wasser an der Jakobsquelle", None,
  "Weil die Pharisäer gehört haben, dass Jesus mehr Jünger gewinnt als Johannes, verlässt er Judäa und muss durch Samarien ziehen. Müde setzt er sich bei Sychar an die Jakobsquelle und bittet eine samaritische Frau um etwas zu trinken. Sie fragt, wie er als Jude sie um Wasser bitten könne. Jesus spricht von lebendigem Wasser, das er geben würde und das im Trinkenden zur Quelle wird, die ins ewige Leben sprudelt; die Frau bittet um dieses Wasser, um keinen Durst mehr zu haben und nicht mehr schöpfen zu müssen.", None),
 ("TU-JHN-004-016-026", "JHN.4.16-JHN.4.26", "dialogue", "Anbetung in Geist und Wahrheit", None,
  "Jesus fordert die Frau auf, ihren Mann zu rufen. Als sie sagt, sie habe keinen Mann, bestätigt er es: Sie habe fünf Männer gehabt, und der jetzige sei nicht ihr Mann. Sie hält ihn für einen Propheten und stellt die Anbetung auf «diesem Berg» der in Jerusalem gegenüber. Jesus kündigt eine Stunde an, die schon jetzt da ist, in der die wahren Anbeter den Vater in Geist und Wahrheit anbeten; das Heil komme von den Juden. Als die Frau vom kommenden Messias spricht, sagt Jesus: «Ich bin es, der mit dir redet.»", None),
 ("TU-JHN-004-027-038", "JHN.4.27-JHN.4.38", "dialogue", "Die Speise Jesu und die Ernte", None,
  "Die Jünger kommen und wundern sich, dass Jesus mit einer Frau redet. Die Frau lässt ihren Krug stehen, geht in die Stadt und ruft die Leute zu dem Menschen, der ihr alles gesagt hat, was sie getan hat – ob er wohl der Christus sei; die Leute machen sich auf den Weg zu ihm. Den Jüngern, die ihn zum Essen auffordern, sagt Jesus, seine Speise sei, den Willen dessen zu tun, der ihn gesandt hat, und sein Werk zu vollenden. Die Felder seien weiss zur Ernte; er habe sie gesandt zu ernten, wofür andere sich abgemüht haben.", None),
 ("TU-JHN-004-039-042", "JHN.4.39-JHN.4.42", "narrative", "Die Samariter glauben", None,
  "Viele Samariter der Stadt glauben an Jesus wegen des Zeugnisses der Frau. Auf ihre Bitte bleibt er zwei Tage bei ihnen, und noch viel mehr glauben wegen seines Wortes. Sie sagen der Frau, sie glaubten nicht mehr wegen ihres Redens; sie hätten selbst gehört und wüssten, dass er wirklich der Retter der Welt ist.", None),
 ("TU-JHN-004-043-054", "JHN.4.43-JHN.4.54", "narrative", "Das zweite Zeichen: der Sohn des königlichen Beamten", None,
  "Nach zwei Tagen zieht Jesus nach Galiläa weiter; er selbst hatte bezeugt, dass ein Prophet in seiner Heimat kein Ansehen hat. Die Galiläer nehmen ihn auf, weil sie gesehen haben, was er am Fest in Jerusalem getan hat. In Kana bittet ihn ein königlicher Beamter, hinabzukommen und seinen sterbenskranken Sohn in Kafarnaum zu heilen. Jesus antwortet: «Wenn ihr nicht Zeichen und Wunder seht, glaubt ihr gewiss nicht», und auf die erneute Bitte: «Geh! Dein Sohn lebt.» Der Mann glaubt dem Wort; unterwegs melden ihm seine Knechte, der Junge lebe, und er erfährt, dass das Fieber ihn in der Stunde verlassen hat, in der Jesus das sagte. Er und sein ganzes Haus glauben. Es ist das zweite Zeichen, das Jesus nach seiner Ankunft aus Judäa in Galiläa tut.", None),
 ("TU-JHN-005-001-047", "JHN.5.1-JHN.5.47", "section", "Heilung am Sabbat und Rede über den Sohn",
  ["TU-JHN-005-001-009", "TU-JHN-005-010-018", "TU-JHN-005-019-030", "TU-JHN-005-031-047"],
  "An einem Fest der Juden heilt Jesus in Jerusalem am Teich Betesda einen Mann, der achtunddreissig Jahre krank war, und sagt zu ihm, er solle seine Matte nehmen und umhergehen. Weil es Sabbat ist, halten die Juden dem Geheilten das Tragen der Matte vor und verfolgen Jesus; als er sagt, sein Vater wirke bis jetzt und auch er wirke, suchen sie ihn umso mehr zu töten, weil er Gott seinen eigenen Vater nennt und sich Gott gleich macht. Jesus antwortet: Der Sohn kann nichts von sich aus tun, sondern nur, was er den Vater tun sieht; er macht lebendig, welche er will, und der Vater hat ihm das ganze Gericht gegeben. Wer sein Wort hört und dem glaubt, der ihn gesandt hat, hat ewiges Leben. Für ihn legen Johannes, seine Werke, der Vater und die Schriften Zeugnis ab; doch seine Zuhörer wollen nicht zu ihm kommen, und Mose, auf den sie hoffen, klagt sie an. [[JHN.5.4]] steht nicht im SBLGNT.",
  SEG + " [[JHN.5.4]] fehlt im SBLGNT und hat keinen Text; der Bereich der Kapiteleinheit schliesst die Versnummer trotzdem ein."),
 ("TU-JHN-005-001-009", "JHN.5.1-JHN.5.9", "narrative", "Die Heilung am Teich Betesda", None,
  "An einem Fest der Juden zieht Jesus nach Jerusalem. Am Teich Betesda beim Schaftor liegen in fünf Säulenhallen viele Kranke. Einen Mann, der achtunddreissig Jahre krank ist, fragt Jesus, ob er gesund werden wolle; der Mann klagt, er habe niemanden, der ihn in den Teich bringe, wenn das Wasser aufgewühlt wird. Jesus sagt: «Steh auf, nimm deine Matte und geh umher!» Der Mann wird sofort gesund, nimmt seine Matte und geht umher. Es ist Sabbat. Der im SBLGNT fehlende Vers [[JHN.5.4]] (ein Engel wühlt das Wasser auf, und wer zuerst hineinsteigt, wird gesund) ist unter den erfassten Handschriften nur in 02 überliefert und steht in den Ausgaben KJTR, RP und Stephanus; er ist als Lesart bei [[JHN.5.3]] aufgeführt.", None),
 ("TU-JHN-005-010-018", "JHN.5.10-JHN.5.18", "narrative", "Der Konflikt um den Sabbat", None,
  "Die Juden halten dem Geheilten vor, am Sabbat dürfe er die Matte nicht tragen; er beruft sich auf den, der ihn gesund gemacht hat, weiss aber nicht, wer es war. Jesus findet ihn im Tempel und mahnt ihn, nicht mehr zu sündigen; darauf meldet der Mann den Juden, dass es Jesus war. Die Juden verfolgen Jesus, weil er dies am Sabbat tat. Auf seine Antwort «Mein Vater wirkt bis jetzt, und auch ich wirke» suchen sie umso mehr, ihn zu töten, weil er Gott seinen eigenen Vater nennt und sich Gott gleich macht.", None),
 ("TU-JHN-005-019-030", "JHN.5.19-JHN.5.30", "discourse", "Der Sohn tut die Werke des Vaters", None,
  "Jesus antwortet: Der Sohn kann nichts von sich aus tun, sondern nur, was er den Vater tun sieht; der Vater hat ihn lieb und wird ihm grössere Werke zeigen. Wie der Vater Tote auferweckt und lebendig macht, so macht der Sohn lebendig, welche er will; der Vater hat ihm das ganze Gericht gegeben, damit alle den Sohn ehren wie den Vater. Wer sein Wort hört und dem glaubt, der ihn gesandt hat, hat ewiges Leben und ist aus dem Tod ins Leben hinübergegangen. Die Stunde kommt und ist jetzt da, in der die Toten die Stimme des Sohnes Gottes hören; und es kommt die Stunde, in der alle in den Gräbern herauskommen werden, zur Auferstehung des Lebens oder des Gerichts. Jesus richtet, wie er hört, und sucht den Willen dessen, der ihn gesandt hat.", None),
 ("TU-JHN-005-031-047", "JHN.5.31-JHN.5.47", "discourse", "Zeugnisse für den Sohn", None,
  "Jesus sagt, sein Zeugnis über sich selbst wäre nicht wahr; ein anderer legt Zeugnis über ihn ab. Johannes hat für die Wahrheit Zeugnis abgelegt und war eine brennende Lampe; grösser ist das Zeugnis der Werke, die der Vater ihm zu vollenden gegeben hat, und der Vater selbst hat über ihn Zeugnis abgelegt. Seine Zuhörer erforschen die Schriften, die über ihn Zeugnis ablegen, wollen aber nicht zu ihm kommen, um Leben zu haben; sie nehmen Ehre voneinander an und suchen nicht die Ehre, die von Gott kommt. Nicht Jesus wird sie beim Vater anklagen; es ist Mose, auf den sie hoffen, der sie anklagt, denn über Jesus hat er geschrieben.", None),
]
UNITS_GSW = {
 "TU-JHN-004-001-054": ("De Jesus z Samarie und s zweit Zeiche z Kana", "Wo de Jesus erfaart, d Pharisäer heigid ghört, dass er meh Jünger gwünni und taufi als de Johannes, verlaat er Judäa und zieht dur Samarie uf Galiläa. Bi de Jakobsquälle bi Sychar bittet er e samaritanischi Frau um Wasser und redt mit ire über läbigs Wasser, über iri Mane und über s Aabätte vom Vatter i Geischt und Wahrheit; uf iri Erwartig vom Messias seit er: «Ich bi s, wo mit dir redt.» D Frau rüeft d Lüüt vo irere Stadt; de Jesus redt mit de Jünger vo sinere Spiis und vo de Ärnt. Vili Samaritaner glaubed a en und nänned en de Retter vo de Wält. Z Kana bittet en en königliche Beamte um Hilf für sin todchranke Sohn z Kafarnaum; de Jesus seit em: «Din Sohn läbt», und de Maa erfaart, dass s Fieber de Bueb grad i dere Stund verlaa hät, wo de Jesus das gseit hät. Er und sis ganz Huus glaubed; es isch s zweit Zeiche vom Jesus."),
 "TU-JHN-004-001-015": ("Läbigs Wasser a de Jakobsquälle", "Wil d Pharisäer ghört händ, dass de Jesus meh Jünger gwünnt als de Johannes, verlaat er Judäa und mues dur Samarie. Müed sitzt er bi Sychar a d Jakobsquälle und bittet e samaritanischi Frau um öppis z trinke. Si fröget, wie er als Jud si um Wasser bitte chönn. De Jesus redt vo läbigem Wasser, won er würd gää und wo i däm, wo trinkt, zu ere Quälle wird, wo is ewig Läbe usesprudlet; d Frau bittet um das Wasser, demit si kei Durscht meh hät und nüme mues go schöpfe."),
 "TU-JHN-004-016-026": ("Aabätte i Geischt und Wahrheit", "De Jesus schickt d Frau go ire Maa rüefe. Wo si seit, si heig kei Maa, bestätiget er s: Si heig föif Mane gha, und dä, wo si jetzt heig, sig nöd ire Maa. Si hebt en für en Prophet und stellt s Aabätte uf «däm Bärg» em Aabätte z Jerusalem gägenüber. De Jesus seit e Stund aa, wo scho jetzt da isch, wo di wahre Aabätter de Vatter i Geischt und Wahrheit aabätted; s Heil chömm vo de Jude. Wo d Frau vom Messias redt, wo chunnt, seit de Jesus: «Ich bi s, wo mit dir redt.»"),
 "TU-JHN-004-027-038": ("D Spiis vom Jesus und d Ärnt", "D Jünger chömed und stuuned, dass de Jesus mit ere Frau redt. D Frau laat iren Chrueg stoo, gaat i d Stadt und rüeft d Lüüt zu däm Mänsch, wo ire alles gseit hät, was si gmacht hät – öb er ächt de Christus sig; d Lüüt mached sich zu ihm uf de Wäg. De Jünger, wo en zum Ässe uffordered, seit de Jesus, sini Spiis sig, de Wille vo däm z tue, wo en gschickt hät, und sis Wärch z vollände. D Fälder sigid wiiss für d Ärnt; er heig si gschickt go ärnte, wofür sich anderi abgmüeht händ."),
 "TU-JHN-004-039-042": ("D Samaritaner glaubed", "Vili Samaritaner us de Stadt glaubed wäge em Zügnis vo de Frau a de Jesus. Uf iri Bitt bliibt er zwei Täg bi ine, und no vil meh glaubed wäge sim Wort. Si säged de Frau, si glaubid nüme wäge irem Gred; si heigid sälber ghört und wüssid, dass er würkli de Retter vo de Wält isch."),
 "TU-JHN-004-043-054": ("S zweit Zeiche: de Sohn vom königliche Beamte", "Nach zwei Täg gaat de Jesus wiiter uf Galiläa; er sälber hät bezüügt, dass en Prophet i sinere Heimet kei Aasee hät. D Galiläer nämed en uf, wil si gseh händ, was er am Fäscht z Jerusalem gmacht hät. Z Kana bittet en en königliche Beamte, abezcho und sin todchranke Sohn z Kafarnaum z heile. De Jesus antwortet: «Wänn ir nöd Zeiche und Wunder gsehnd, glaubed ir sicher nöd», und uf di nöi Bitt: «Gang! Din Sohn läbt.» De Maa glaubt em Wort; underwägs mälded em sini Chnächt, de Bueb läbi, und er erfaart, dass s Fieber en i dere Stund verlaa hät, wo de Jesus das gseit hät. Er und sis ganz Huus glaubed. Es isch s zweit Zeiche, wo de Jesus nach sinere Aachunft us Judäa z Galiläa macht."),
 "TU-JHN-005-001-047": ("Heilig am Sabbat und Red über de Sohn", "A me Fäscht vo de Jude heilt de Jesus z Jerusalem bim Teich Betesda en Maa, wo achtedriissg Jahr chrank gsii isch, und seit em, er söll sini Matte nää und umenand laufe. Wil Sabbat isch, händ d Jude em Gheilte s Träge vo de Matte vor und verfolged de Jesus; won er seit, sin Vatter wirki bis jetzt und au er wirki, sueched si no meh, en z töte, wil er Gott sin eigete Vatter nännt und sich Gott gliich macht. De Jesus antwortet: De Sohn cha nüüt vo sich uus mache, nu das, won er de Vatter gseht mache; er macht läbig, won er will, und de Vatter hät ihm s ganz Gricht gää. Wer sis Wort ghört und däm glaubt, wo en gschickt hät, hät ewigs Läbe. Für ihn legged de Johannes, sini Wärch, de Vatter und d Schrifte Zügnis ab; aber sini Zuehörer wänd nöd zu ihm choo, und de Mose, uf dä si hoffed, verchlagt si. [[JHN.5.4]] staat nöd im SBLGNT."),
 "TU-JHN-005-001-009": ("D Heilig bim Teich Betesda", "A me Fäscht vo de Jude gaat de Jesus uf Jerusalem. Bim Teich Betesda bim Schaaftor ligged i föif Säulehalle vili Chranki. En Maa, wo achtedriissg Jahr chrank isch, fröget de Jesus, öb er gsund wärde well; de Maa chlagt, er heig niemer, wo en in Teich bringt, wänn s Wasser ufgwüelt wird. De Jesus seit: «Stand uf, nimm dini Matte und lauf umenand!» De Maa wird sofort gsund, nimmt sini Matte und lauft umenand. Es isch Sabbat. De Vers [[JHN.5.4]], wo im SBLGNT fäält (en Ängel wüelt s Wasser uf, und wer zerscht inestiigt, wird gsund), isch under de erfasste Handschrifte nu i 02 überliferet und staat i de Usgabe KJTR, RP und Stephanus; er staat als Läsart bi [[JHN.5.3]]."),
 "TU-JHN-005-010-018": ("De Striit um de Sabbat", "D Jude händ em Gheilte vor, am Sabbat dörf er d Matte nöd träge; er beruefft sich uf dä, wo en gsund gmacht hät, weiss aber nöd, wer s gsii isch. De Jesus findt en im Tämpel und mahnt en, nüme z sündige; dänn mäldet de Maa de Jude, dass es de Jesus gsii isch. D Jude verfolged de Jesus, wil er das am Sabbat gmacht hät. Uf sini Antwort «Min Vatter wirkt bis jetzt, und au ich wirke» sueched si no meh, en z töte, wil er Gott sin eigete Vatter nännt und sich Gott gliich macht."),
 "TU-JHN-005-019-030": ("De Sohn macht d Wärch vom Vatter", "De Jesus antwortet: De Sohn cha nüüt vo sich uus mache, nu das, won er de Vatter gseht mache; de Vatter hät en gärn und wird em grösseri Wärch zeige. Wie de Vatter d Tote uferweckt und läbig macht, so macht de Sohn läbig, won er will; de Vatter hät em s ganz Gricht gää, demit alli de Sohn ehred wie de Vatter. Wer sis Wort ghört und däm glaubt, wo en gschickt hät, hät ewigs Läbe und isch vom Tod is Läbe übere gange. D Stund chunnt und isch jetzt da, wo d Tote d Stimm vom Sohn vo Gott ghöred; und es chunnt d Stund, wo alli i de Gräber usechömed, zur Uferstehig vom Läbe oder vom Gricht. De Jesus richtet, wie n er ghört, und suecht de Wille vo däm, wo en gschickt hät."),
 "TU-JHN-005-031-047": ("Zügnis für de Sohn", "De Jesus seit, sis Zügnis über sich sälber wär nöd wahr; en andere legt Zügnis über ihn ab. De Johannes hät für d Wahrheit Zügnis abgleit und isch e brännendi Lampe gsii; grösser isch s Zügnis vo de Wärch, won em de Vatter gää hät zum Vollände, und de Vatter sälber hät über ihn Zügnis abgleit. Sini Zuehörer erforsched d Schrifte, wo über ihn Zügnis ablegged, wänd aber nöd zu ihm choo, zum Läbe ha; si nämed Ehr vonenand aa und sueched nöd d Ehr, wo vo Gott chunnt. Nöd de Jesus wird si bim Vatter verchlage; es isch de Mose, uf dä si hoffed, wo si verchlagt, dänn über de Jesus hät er gschribe."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("Die Grundentscheide für die johanneischen Schlüsselwörter (λόγος «Wort», ἐγώ εἰμι «Ich bin …», δόξα «Herrlichkeit», "
  "σημεῖον «Zeichen», μένω «bleiben», ἀμὴν ἀμήν «Amen, amen», κόσμος «Welt», οἱ Ἰουδαῖοι «die Juden») sind bei den "
  "Übersetzungen zu Johannes 1–3 begründet (Autorenwerkzeug scripts/authoring/johannes_text_01_03.py). Hier sind sie "
  "übernommen; die Stellen in Kapitel 4–5 sind in decisions vermerkt. Abweichung: δόξα in [[JHN.5.41]] und [[JHN.5.44]] "
  "(Ansehen bei Menschen) ist mit «Ehre» wiedergegeben, je mit eigener Entscheidung. ἐγώ εἰμι als Antwort ([[JHN.4.26]]) "
  "«Ich bin es». φιλέω ([[JHN.5.20]]) «lieb haben», ἀγαπάω «lieben»."),
 ("οἱ Ἰουδαῖοι ist wörtlich mit «die Juden» wiedergegeben. Das Wort bezeichnet bei Johannes je nach Stelle das jüdische Volk "
  "([[JHN.4.9]]; [[JHN.4.22]]: «das Heil kommt von den Juden») oder, wie in [[JHN.5.10]]–[[JHN.5.18]], Autoritäten in "
  "Jerusalem, die gegen Jesus vorgehen; Jesus selbst wird in [[JHN.4.9]] «Jude» genannt. Die Wiedergabe «die jüdischen "
  "Führer» ist eine Deutung und als Alternative in decisions vermerkt."),
 ("[[JHN.5.4]] steht nicht im SBLGNT und hat deshalb hier keinen Text. Der Zusatz am Ende von [[JHN.5.3]] («die auf die "
  "Bewegung des Wassers warteten») und Vers 4 (der Engel, der das Wasser aufwühlt) stehen als Alternative bei [[JHN.5.3]], "
  "mit dem Befund der CNTR-Transkriptionen: Vers 4 ist dort nur in 02 erfasst. Dass der Zusatz nicht ursprünglich ist, ist "
  "ein in der Textforschung verbreitetes Urteil; Ausgaben nach dem Mehrheitstext lesen ihn."),
 ("Der Satz «Juden verkehren nämlich nicht mit Samaritern» ([[JHN.4.9]]) fehlt nach der CNTR-Transkription in 05 und in der "
  "Erstschrift von 01 (dort von einer Korrektur ergänzt). Der SBLGNT-Apparat führt dazu keine Variante; deshalb steht hier "
  "keine Alternative."),
 ("In [[JHN.4.1]] folgt der SBLGNT-Text NA28 (Ἰησοῦς) gegen WH, Treg, NIV und RP (κύριος), in [[JHN.5.2]] Treg, NIV und RP "
  "(Βηθεσδά) gegen WH und NA28 (Βηθζαθά); die anderen Wortlaute stehen als Alternativen."),
 ("ἤδη am Ende von [[JHN.4.35]] ist nach der Zeichensetzung des SBLGNT zum folgenden Satz gezogen («Schon empfängt der "
  "Schnitter Lohn», [[JHN.4.36]])."),
 ("Johannes erzählt oft im Präsens («er kommt», «sie sagt»); das ist beibehalten. ὅτι vor direkter Rede ist nicht eigens "
  "übersetzt. Zahlenangaben zu Wortvorkommen beruhen auf den MACULA-Lemmata bzw. den Tokens des SBLGNT-Texts."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("D Grundentscheid für di johanneische Schlüsselwörter sind bi de Übersetzige zu Johannes 1–3 begründet "
  "(scripts/authoring/johannes_text_01_03.py) und da übernoo: «Amen, amen, ich säge eu», «Zeiche», «Wält», «bliibe», "
  "«Ich bi …» (als Antwort i [[JHN.4.26]] «Ich bi s»), «d Jude», «de Vatter». δόξα isch i [[JHN.5.41]] und [[JHN.5.44]] «Ehr»; "
  "φιλέω ([[JHN.5.20]]) «gärn haa», ἀγαπάω «liebe»."),
 ("οἱ Ἰουδαῖοι isch wörtlich «d Jude». I [[JHN.5.10]]–[[JHN.5.18]] sind Autoritäte z Jerusalem gmeint; «di jüdische Füerer» "
  "wär e Deutig und staat als Alternative."),
 ("[[JHN.5.4]] staat nöd im SBLGNT und hät drum da kei Text; de Zuesatz i [[JHN.5.3]] und de Vers [[JHN.5.4]] stönd als Alternative bi [[JHN.5.3]]."),
]


def run():
    import json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _lib import localize  # noqa: E402
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
                      "KI-Entwurf (Claude) vom 2026-10-14; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-jhn").glob("*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-JHN-{c:03d}.json")
        refs_c = [f"JHN.{c}.{v}" for v in range(1, last + 1) if f"JHN.{c}.{v}" in toks]  # 5,4 fehlt im SBLGNT
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            missing = [r for r in refs_c if r not in markup]
            if missing:
                raise SystemExit(f"{lang}: Verse ohne Übersetzung {missing}")
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/johannes_text_04_05.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 4–5 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
