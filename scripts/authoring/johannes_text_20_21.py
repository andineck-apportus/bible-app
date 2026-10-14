#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 20–21 (leeres Grab, Erscheinungen des Auferstandenen, Nachtragskapitel) – Texteinheiten,
Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und
vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_20_21.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben.

Die Grundentscheide zu den johanneischen Schlüsselwörtern (οἱ Ἰουδαῖοι, σημεῖον, δόξα/δοξάζω, μένω, ἀμὴν ἀμήν, κόσμος,
λόγος …) stehen in scripts/authoring/johannes_text_01_03.py; hier werden sie für Kapitel 20–21 angewandt. Zusätzlich gilt
für das ganze Evangelium: ἀγαπάω «lieben», φιλέω «lieb haben» (Mundart «liebe» / «gärn haa»), siehe [[JHN.21.15]].

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
CHAPTERS = ((20, 31), (21, 25))
RIGHT = "ὅτι leitet die direkte Rede ein"
RIGHT_G = "ὅτι leitet di diräkt Red ii"

DE = {
 # ------------------------------------------------------------ Kapitel 20
 "JHN.20.1": "[Am]{1} [ersten Tag]{3} [der Woche]{4,5} [aber]{2} [kommt]{9} [Maria]{6} [aus Magdala]{7,8} [früh]{10}, [als es]{13} [noch]{12} [dunkel]{11} [war]{13}, [zum]{14,15} [Grab]{16}, und{17} [sieht]{18}, dass [der Stein]{19,20} [vom]{22,23} [Grab]{24} [weggenommen]{21} ist.",
 "JHN.20.2": "[Da]{2} [läuft sie]{1} und{3} [kommt]{4} [zu]{5} [Simon]{6} [Petrus]{7} und{8} [zu]{9} [dem anderen]{10,11} [Jünger]{12}, [den]{13} [Jesus]{15,16} [lieb hatte]{14}, und{17} [sagt]{18} [zu ihnen]{19}: «[Sie haben]{20} [den Herrn]{21,22} [aus]{23} [dem Grab]{24,25} [weggenommen]{20}, und{26} [wir wissen]{28} [nicht]{27}, [wo]{29} [sie]{30} [ihn]{31} [hingelegt haben]{30}.»",
 "JHN.20.3": "[Da]{2} [brachen]{1} [Petrus]{3,4} und{5} [der andere]{6,7} [Jünger]{8} [auf]{1}, und{9} [sie gingen]{10} [zum]{11,12} [Grab]{13}.",
 "JHN.20.4": "[Die beiden]{3,4} [liefen]{1} [aber]{2} [zusammen]{5}; und{6} [der andere]{7,8} [Jünger]{9} [lief voraus]{10}, [schneller]{11} [als]{12} [Petrus]{13}, und{14} [kam]{15} [als Erster]{16} [zum]{17,18} [Grab]{19}.",
 "JHN.20.5": "Und{1} [er beugte sich vor]{2} und [sieht]{3} [die]{5} [Leinenbinden]{6} [daliegen]{4}; [hinein ging er]{9} [jedoch]{8} [nicht]{7}.",
 "JHN.20.6": "[Da]{2} [kommt]{1} [auch]{3} [Simon]{4} [Petrus]{5}, der [ihm]{7} [folgte]{6}, und{8} [ging]{9} [in]{10} [das Grab]{11,12} [hinein]{9}, und{13} [er schaut]{14} [die]{15} [Leinenbinden]{16} [daliegen]{17}.",
 "JHN.20.7": "Und{1} [das]{2} [Schweisstuch]{3}, [das]{4} [auf]{6} [seinem]{9} [Kopf]{7,8} [gewesen war]{5}, [lag]{14} [nicht]{10} [bei]{11} [den]{12} [Leinenbinden]{13}, [sondern]{15} [für sich]{16} [zusammengewickelt]{17} [an]{18} [einer eigenen]{19} [Stelle]{20}.",
 "JHN.20.8": "[Da]{1} [ging]{3} [nun]{2} [auch]{4} [der andere]{5,6} [Jünger]{7} [hinein]{3}, [der]{8} [als Erster]{10} [zum]{11,12} [Grab]{13} [gekommen war]{9}, und{14} [er sah]{15} und{16} [glaubte]{17}.",
 "JHN.20.9": "[Denn]{2} [sie kannten]{3} [die]{4} [Schrift]{5} [noch nicht]{1}, [dass]{6} [er]{8} [von]{9} [den Toten]{10} [auferstehen]{11} [müsse]{7}.",
 "JHN.20.10": "[Da]{2} [gingen]{1} [die Jünger]{6,7} [wieder]{3} [nach Hause]{4,5:idiom}.",
 "JHN.20.11": "[Maria]{1} [aber]{2} [stand]{3} [draussen]{7} [beim]{4,5} [Grab]{6} [und weinte]{8}. [Während]{9} [sie]{11} [nun]{10} [weinte]{11}, [beugte sie sich vor]{12} und schaute [ins]{13,14} [Grab]{15}.",
 "JHN.20.12": "Und{1} [sie schaut]{2} [zwei]{3} [Engel]{4} [in]{5} [weissen Gewändern]{6} [dasitzen]{7}, [einen]{8} [beim]{9,10} [Kopf]{11} und{12} [einen]{13} [bei]{14} [den]{15} [Füssen]{16}, [wo]{17} [der Leib]{19,20} [Jesu]{21,22} [gelegen hatte]{18}.",
 "JHN.20.13": "Und{1} [jene]{4} [sagen]{2} [zu ihr]{3}: «[Frau]{5}, [warum]{6} [weinst du]{7}?» [Sie sagt]{8} [zu ihnen]{9}: «[Sie haben]{11} [meinen]{14} [Herrn]{12,13} [weggenommen]{11}, und{15} [ich weiss]{17} [nicht]{16}, [wo]{18} [sie]{19} [ihn]{20} [hingelegt haben]{19}.» ~10(" + RIGHT + ")",
 "JHN.20.14": "[Als sie]{2} [das]{1} [gesagt hatte]{2}, [wandte sie sich um]{3-6} und{7} [schaut]{8} [Jesus]{9,10} [dastehen]{11}, und{12} [sie wusste]{14} [nicht]{13}, [dass]{15} es [Jesus]{16} [war]{17}.",
 "JHN.20.15": "[Jesus]{3} [sagt]{1} [zu ihr]{2}: «[Frau]{4}, [warum]{5} [weinst du]{6}? [Wen]{7} [suchst du]{8}?» [Sie]{9} [meinte]{10}, [dass]{11} es [der Gärtner]{12,13} [sei]{14}, und [sagt]{15} [zu ihm]{16}: «[Herr]{17}, [wenn]{18} [du]{19} [ihn]{21} [weggetragen hast]{20}, [sag]{22} [mir]{23}, [wo]{24} [du]{25} [ihn]{26} [hingelegt hast]{25}, [und ich]{27} [werde]{29} [ihn]{28} [holen]{29}.»",
 "JHN.20.16": "[Jesus]{3} [sagt]{1} [zu ihr]{2}: «[Mariam]{4}!» [Sie]{6} [wandte sich um]{5} und [sagt]{7} [zu ihm]{8} [auf Hebräisch]{9}: «[Rabbuni]{10}!», [das]{11} [heisst]{12}: «[Lehrer]{13}!»",
 "JHN.20.17": "[Jesus]{3} [sagt]{1} [zu ihr]{2}: «[Halte]{6} [mich]{5} [nicht]{4} [fest]{6}! [Denn]{8} [ich bin]{9} [noch nicht]{7} [zum]{10,11} [Vater]{12} [hinaufgestiegen]{9}. [Geh]{13} [aber]{14} [zu]{15} [meinen]{18} [Brüdern]{16,17} und{19} [sag]{20} [ihnen]{21}: ‹[Ich steige hinauf]{22} [zu]{23} [meinem]{26} [Vater]{24,25} und{27} [eurem]{29} [Vater]{28}, und{30} zu [meinem]{32} [Gott]{31} und{33} [eurem]{35} [Gott]{34}.›»",
 "JHN.20.18": "[Mariam]{2} [aus Magdala]{3,4} [kommt]{1} und [verkündet]{5} [den Jüngern]{6,7}: «[Ich habe]{9} [den Herrn]{10,11} [gesehen]{9}», und{12} [dass er]{14} [ihr]{15} [dies]{13} [gesagt habe]{14}. ~8(" + RIGHT + ")",
 "JHN.20.19": "[Als es]{1} [nun]{2} [Abend]{3} [war]{1} [an jenem]{4,6} [Tag]{5}, [dem ersten]{7,8} [der Woche]{9}, und{10} [die Türen]{11,12} da, [wo]{14} [die Jünger]{16,17} [waren]{15}, [aus]{18} [Furcht]{19,20} [vor den Juden]{21,22} [verschlossen waren]{13}, [kam]{23} [Jesus]{24,25} und{26} [trat]{27} [in]{28} [die Mitte]{29,30} und{31} [sagt]{32} [zu ihnen]{33}: «[Friede]{34} [euch]{35}!»",
 "JHN.20.20": "Und{1} [als er]{3} [das]{2} [gesagt hatte]{3}, [zeigte er]{4} [ihnen]{10} [die]{5} [Hände]{6} und{7} [die]{8} [Seite]{9}. [Da]{12} [freuten sich]{11} [die Jünger]{13,14}, [als sie]{15} [den Herrn]{16,17} [sahen]{15}.",
 "JHN.20.21": "[Da]{2} [sagte]{1} [Jesus]{4,5} [wieder]{6} [zu ihnen]{3}: «[Friede]{7} [euch]{8}! [Wie]{9} [der Vater]{12,13} [mich]{11} [gesandt hat]{10}, [so sende]{15} [auch ich]{14} [euch]{16}.»",
 "JHN.20.22": "Und{1} [als er]{3} [das]{2} [gesagt hatte]{3}, [hauchte er sie an]{4} und{5} [sagt]{6} [zu ihnen]{7}: «[Empfangt]{8} [heiligen]{10} [Geist]{9}!",
 "JHN.20.23": "[Wem]{1,2} [ihr]{3} [die]{4} [Sünden]{5} [vergebt]{3}, [dem]{7} [sind sie vergeben]{6}; [wem]{8,9} [ihr]{10} sie [behaltet]{10}, dem [sind sie behalten]{11}.»",
 "JHN.20.24": "[Thomas]{1} [aber]{2}, [einer]{3} [der Zwölf]{4-6}, [der]{7} [«Zwilling»]{9} [genannt wird]{8}, [war]{11} [nicht]{10} [bei]{12} [ihnen]{13}, [als]{14} [Jesus]{16} [kam]{15}.",
 "JHN.20.25": "[Da]{2} [sagten]{1} [die anderen]{4,5} [Jünger]{6} [zu ihm]{3}: «[Wir haben]{7} [den Herrn]{8,9} [gesehen]{7}!» [Er]{10} [aber]{11} [sagte]{12} [zu ihnen]{13}: «[Wenn]{14} [ich]{16} [nicht]{15} [an]{17} [seinen]{20} [Händen]{18,19} [das]{21} [Mal]{22} [der Nägel]{23,24} [sehe]{16} und{25} [meinen]{29} [Finger]{27,28} [in]{30} [das]{31} [Mal]{32} [der Nägel]{33,34} [lege]{26} und{35} [meine]{37} [Hand]{38,39} [in]{40} [seine]{43} [Seite]{41,42} [lege]{36}, [werde ich]{46} [gewiss nicht]{44,45} [glauben]{46}.»",
 "JHN.20.26": "Und{1} [nach]{2} [acht]{4} [Tagen]{3} [waren]{6} [seine]{10} [Jünger]{8,9} [wieder]{5} [drinnen]{7}, und{11} [Thomas]{12} [bei]{13} [ihnen]{14}. Da [kommt]{15} [Jesus]{16,17} [bei verschlossenen]{20} [Türen]{18,19} und{21} [trat]{22} [in]{23} [die Mitte]{24,25} und{26} [sagte]{27}: «[Friede]{28} [euch]{29}!»",
 "JHN.20.27": "[Dann]{1} [sagt er]{2} [zu Thomas]{3,4}: «[Reich]{5} [deinen]{8} [Finger]{6,7} [hierher]{9} und{10} [sieh]{11} [meine]{14} [Hände]{12,13}, und{15} [reich]{16} [deine]{19} [Hand]{17,18} [her]{16} und{20} [lege sie]{21} [in]{22} [meine]{25} [Seite]{23,24}, und{26} [sei]{28} [nicht]{27} [ungläubig]{29}, [sondern]{30} [gläubig]{31}!»",
 "JHN.20.28": "[Thomas]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihm]{5}: «[Mein]{8} [Herr]{6,7} und{9} [mein]{12} [Gott]{10,11}!»",
 "JHN.20.29": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: «[Weil]{5} [du]{6} [mich]{7} [gesehen hast]{6}, [hast du geglaubt]{8}? [Selig]{9} sind, [die]{10} [nicht]{11} [gesehen]{12} und{13} [doch geglaubt haben]{14}!»",
 "JHN.20.30": "[Noch]{4} [viele]{1} [andere]{5} [Zeichen]{6} [hat]{7} [Jesus]{8,9} [nun]{3} [zwar]{2} [vor]{10} [den Jüngern]{11,12} [getan]{7}, [die]{13} [nicht]{14} [in]{17} [diesem]{20} [Buch]{18,19} [aufgeschrieben]{16} [sind]{15}.",
 "JHN.20.31": "[Diese]{1} [aber]{2} [sind aufgeschrieben]{3}, [damit]{4} [ihr glaubt]{5}, [dass]{6} [Jesus]{7} [der Christus]{9,10} [ist]{8}, [der Sohn]{11,12} [Gottes]{13,14}, und{15} [damit]{16} [ihr]{19} [als Glaubende]{17} [Leben]{18} [habt]{19} [in]{20} [seinem]{23} [Namen]{21,22}.",
 # ------------------------------------------------------------ Kapitel 21
 "JHN.21.1": "[Danach]{1,2} [offenbarte sich]{3,4} [Jesus]{6,7} [den Jüngern]{8,9} [noch einmal]{5} [am]{10,11} [See]{12} [von Tiberias]{13,14}. [Er offenbarte sich]{15} [aber]{16} [so]{17}:",
 "JHN.21.2": "[Es waren]{1} [beisammen]{2} [Simon]{3} [Petrus]{4} und{5} [Thomas]{6}, [der]{7} [«Zwilling»]{9} [genannt wird]{8}, und{10} [Natanaël]{11} [aus]{12,13} [Kana]{14} [in]{15} [Galiläa]{16} und{17} [die Söhne]{18} [des Zebedäus]{19,20} und{21} [zwei]{27} [andere]{22} [von]{23} [seinen]{26} [Jüngern]{24,25}.",
 "JHN.21.3": "[Simon]{3} [Petrus]{4} [sagt]{1} [zu ihnen]{2}: «[Ich gehe]{5} [fischen]{6}.» [Sie sagen]{7} [zu ihm]{8}: «[Auch]{10} [wir]{11} [kommen]{9} [mit]{12} [dir]{13}.» [Sie gingen hinaus]{14} und{15} [stiegen]{16} [in]{17} [das Boot]{18,19}, und{20} [in]{21} [jener]{22,23} [Nacht]{24} [fingen sie]{25} [nichts]{26}.",
 "JHN.21.4": "[Als es]{4} [aber]{2} [schon]{3} [Morgen]{1} [geworden war]{4}, [stand]{5} [Jesus]{6} [am]{7,8} [Ufer]{9}; [die Jünger]{13,14} [wussten]{12} [jedoch]{11} [nicht]{10}, [dass]{15} es [Jesus]{16} [war]{17}.",
 "JHN.21.5": "[Da]{2} [sagt]{1} [Jesus]{4,5} [zu ihnen]{3}: «[Kinder]{6}, [habt ihr]{10} [etwa]{7} [etwas]{8} [zu essen]{9}?» [Sie antworteten]{11} [ihm]{12}: «[Nein]{13}.»",
 "JHN.21.6": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: «[Werft]{5} [das]{12} [Netz]{13} [auf]{6} [die rechte]{7,8} [Seite]{9} [des Bootes]{10,11} [aus]{5}, und{14} [ihr werdet]{15} etwas [finden]{15}.» [Da]{17} [warfen sie es aus]{16}, und{18} [sie vermochten]{22} [es]{20} [nicht mehr]{19} [einzuziehen]{21} [wegen]{23} [der Menge]{24,25} [der Fische]{26,27}.",
 "JHN.21.7": "[Da]{2} [sagt]{1} [jener]{5} [Jünger]{3,4}, [den]{6} [Jesus]{8,9} [liebte]{7}, [zu Petrus]{10,11}: «[Es ist]{14} [der Herr]{12,13}!» [Als]{18} [nun]{16} [Simon]{15} [Petrus]{17} [hörte]{18}, [dass]{19} [es]{22} [der Herr]{20,21} [sei]{22}, [gürtete er]{25} [das]{23} [Obergewand]{24} [um]{25} – [er war]{26} [nämlich]{27} [nackt]{28} – und{29} [warf sich]{30,31} [in]{32} [den See]{33,34}.",
 "JHN.21.8": "[Die anderen]{1,3} [Jünger]{4} [aber]{2} [kamen]{7} [mit dem]{5} [Boot]{6} – [denn]{9} [sie waren]{10} [nicht]{8} [weit]{11} [vom]{12,13} [Land]{14}, [sondern]{15} nur [etwa]{16} [zweihundert]{19} [Ellen]{18} [entfernt]{17} – [und schleppten]{20} [das]{21} [Netz]{22} [mit den Fischen]{23,24} [nach]{20}.",
 "JHN.21.9": "[Als]{1} [sie]{3} [nun]{2} [an]{4} [Land]{5,6} [gestiegen waren]{3}, [sehen sie]{7} [ein Kohlenfeuer]{8} [am Boden]{9} und{10} [Fisch]{11}, [der darauf lag]{12}, und{13} [Brot]{14}.",
 "JHN.21.10": "[Jesus]{3,4} [sagt]{1} [zu ihnen]{2}: «[Bringt]{5} [von]{6} [den Fischen]{7,8}, [die]{9} [ihr]{10} [eben]{11} [gefangen habt]{10}!»",
 "JHN.21.11": "[Da]{2} [stieg]{1} [Simon]{3} [Petrus]{4} [hinauf]{1} und{5} [zog]{6} [das]{7} [Netz]{8} [an]{9} [Land]{10,11}, [voll]{12} [grosser]{14} [Fische]{13}, [hundertdreiundfünfzig]{15-17}; und{18} [obwohl]{20} es [so viele]{19} [waren]{20}, [zerriss]{22} [das]{23} [Netz]{24} [nicht]{21}.",
 "JHN.21.12": "[Jesus]{3,4} [sagt]{1} [zu ihnen]{2}: «[Kommt]{5}, [esst]{6}!» [Keiner]{7} [der Jünger]{10,11} [aber]{8} [wagte]{9}, [ihn]{13} [zu fragen]{12}: «[Wer]{15} [bist]{16} [du]{14}?» – [sie wussten]{17} ja, [dass]{18} es [der Herr]{19,20} [war]{21}.",
 "JHN.21.13": "[Jesus]{2,3} [kommt]{1} und{4} [nimmt]{5} [das]{6} [Brot]{7} und{8} [gibt]{9} es [ihnen]{10}, und{11} [ebenso]{14} [den]{12} [Fisch]{13}.",
 "JHN.21.14": "[Das]{1} war [schon]{2} [das dritte Mal]{3}, dass sich [Jesus]{5,6} [den Jüngern]{7,8} [offenbarte]{4}, [nachdem er]{9} [von]{10} [den Toten]{11} [auferweckt worden war]{9}.",
 "JHN.21.15": "[Als]{1} [sie]{3} [nun]{2} [gegessen hatten]{3}, [sagt]{4} [Jesus]{8,9} [zu Simon]{5,6} [Petrus]{7}: «[Simon]{10}, [Sohn des Johannes]{11}, [liebst du]{12} [mich]{13} [mehr]{14} [als diese]{15}?» [Er sagt]{16} [zu ihm]{17}: «[Ja]{18}, [Herr]{19}, [du]{20} [weisst]{21}, [dass]{22} [ich]{23} [dich]{24} [lieb habe]{23}.» [Er sagt]{25} [zu ihm]{26}: «[Weide]{27} [meine]{30} [Lämmer]{28,29}!»",
 "JHN.21.16": "[Er sagt]{1} [wieder]{3}, [ein zweites Mal]{4}, [zu ihm]{2}: «[Simon]{5}, [Sohn des Johannes]{6}, [liebst du]{7} [mich]{8}?» [Er sagt]{9} [zu ihm]{10}: «[Ja]{11}, [Herr]{12}, [du]{13} [weisst]{14}, [dass]{15} [ich]{16} [dich]{17} [lieb habe]{16}.» [Er sagt]{18} [zu ihm]{19}: «[Hüte]{20} [meine]{23} [Schafe]{21,22}!»",
 "JHN.21.17": "[Er sagt]{1} [zu ihm]{2} [zum dritten Mal]{3,4}: «[Simon]{5}, [Sohn des Johannes]{6}, [hast du]{7} [mich]{8} [lieb]{7}?» [Petrus]{10,11} [wurde traurig]{9}, [weil]{12} [er]{13} [zum dritten Mal]{15,16} [zu ihm]{14} [gesagt hatte]{13}: «[Hast du]{17} [mich]{18} [lieb]{17}?», und{19} [er sagte]{20} [zu ihm]{21}: «[Herr]{22}, [du]{24} [weisst]{25} [alles]{23}; [du]{26} [erkennst]{27}, [dass]{28} [ich]{29} [dich]{30} [lieb habe]{29}.» [Jesus]{33,34} [sagt]{31} [zu ihm]{32}: «[Weide]{35} [meine]{38} [Schafe]{36,37}!",
 "JHN.21.18": "[Amen]{1}, [amen]{2}, [ich sage]{3} [dir]{4}: [Als]{5} [du]{6} [jünger]{7} [warst]{6}, [gürtetest du]{8} [dich selbst]{9} und{10} [gingst umher]{11}, [wohin]{12} [du wolltest]{13}; [wenn]{14} [du]{16} [aber]{15} [alt geworden bist]{16}, [wirst du]{17} [deine]{20} [Hände]{18,19} [ausstrecken]{17}, und{21} [ein anderer]{22} [wird]{24} [dich]{23} [gürten]{24} und{25} [dich bringen]{26}, [wohin]{27} [du]{29} [nicht]{28} [willst]{29}.»",
 "JHN.21.19": "[Das]{1} [aber]{2} [sagte er]{3}, [um anzuzeigen]{4}, [durch was für einen]{5} [Tod]{6} [er]{7} [Gott]{8,9} [verherrlichen würde]{7}. Und{10} [als er]{12} [das]{11} [gesagt hatte]{12}, [sagt er]{13} [zu ihm]{14}: «[Folge]{15} [mir]{16}!»",
 "JHN.21.20": "[Petrus]{2,3} [wendet sich um]{1} und [sieht]{4} [den]{5} [Jünger]{6} [folgen]{11}, [den]{7} [Jesus]{9,10} [liebte]{8}, [der]{12} sich [auch]{13} [beim]{15,16} [Mahl]{17} [an]{18} [seine]{21} [Brust]{19,20} [gelehnt]{14} und{22} [gesagt hatte]{23}: «[Herr]{24}, [wer]{25} [ist es]{26}, [der]{27} [dich]{29} [ausliefert]{28}?»",
 "JHN.21.21": "[Als]{3} [Petrus]{4,5} [nun]{2} [diesen]{1} [sah]{3}, [sagt er]{6} [zu Jesus]{7,8}: «[Herr]{9}, [was]{12} [aber]{11} wird [mit diesem]{10}?»",
 "JHN.21.22": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: «[Wenn]{5} [ich will]{7}, [dass er]{6} [bleibt]{8}, [bis]{9} [ich komme]{10}, [was]{11} [geht]{12} es [dich]{13} [an]{12}? [Du]{14}, [folge]{16} [mir]{15}!»",
 "JHN.21.23": "[Da]{2} [verbreitete sich]{1} [dieses]{3} [Wort]{4,5} [unter]{6} [den Brüdern]{7,8}: [Jener]{12} [Jünger]{10,11} [stirbt]{14} [nicht]{13}. [Jesus]{19,20} hatte [ihm]{18} [aber]{17} [nicht]{15} [gesagt]{16}, [dass]{21} er [nicht]{22} [sterbe]{23}, [sondern]{24}: «[Wenn]{25} [ich will]{27}, [dass er]{26} [bleibt]{28}, [bis]{29} [ich komme]{30}, [was]{31} [geht]{32} es [dich]{33} [an]{32}?» ~9(ὅτι leitet den Inhalt des Wortes ein)",
 "JHN.21.24": "[Das]{1} [ist]{2} [der Jünger]{3,4}, [der]{5} [von]{7} [diesen Dingen]{8} [Zeugnis ablegt]{6} und{9} [der]{10} [dies]{12} [geschrieben hat]{11}, und{13} [wir wissen]{14}, [dass]{15} [sein]{17} [Zeugnis]{18,19} [wahr]{16} [ist]{20}.",
 "JHN.21.25": "[Es gibt]{1} [aber]{2} [auch]{3} [vieles]{5} [andere]{4}, [was]{6} [Jesus]{8,9} [getan hat]{7}; [wenn]{11} [das]{10} [einzeln]{13,14} [aufgeschrieben würde]{12}, [könnte]{20}, [meine ich]{17}, [nicht einmal]{15} [die Welt]{18,19} [selbst]{16} [die]{21} [Bücher]{23} [fassen]{20}, [die dann geschrieben würden]{22}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 20
 "JHN.20.1": "[Am]{1} [erschte Tag]{3} [vo de Wuche]{4,5} [aber]{2} [chunnt]{9} [d Maria]{6} [vo Magdala]{7,8} [früe]{10}, [wo s]{13} [no]{12} [tunkel]{11} [gsii isch]{13}, [zum]{14,15} [Grab]{16}, und{17} [gseht]{18}, dass [de Stei]{19,20} [vom]{22,23} [Grab]{24} [wäggnoo]{21} isch.",
 "JHN.20.2": "[Dänn]{2} [rännt si]{1} und{3} [chunnt]{4} [zum]{5} [Simon]{6} [Petrus]{7} und{8} [zum]{9,10} [andere]{11} [Jünger]{12}, [wo]{13} [de Jesus]{15,16} [gärn ghaa hät]{14}, und{17} [seit]{18} [zu ine]{19}: «[Si händ]{20} [de Herr]{21,22} [us]{23} [em Grab]{24,25} [wäggnoo]{20}, und{26} [mer wüssed]{28} [nöd]{27}, [wo]{29} [si]{30} [en]{31} [anegleit händ]{30}.»",
 "JHN.20.3": "[Dänn]{2} [sind]{1} [de Petrus]{3,4} und{5} [de ander]{6,7} [Jünger]{8} [ufbroche]{1} und{9} [sind]{10} [zum]{11,12} [Grab]{13} [gange]{10}.",
 "JHN.20.4": "[Di zwei]{3,4} [sind]{1} [aber]{2} [mitenand]{5} [grännt]{1}; und{6} [de ander]{7,8} [Jünger]{9} [isch voruusgrännt]{10}, [schnäller]{11} [als]{12} [de Petrus]{13}, und{14} [isch]{15} [als Erschte]{16} [zum]{17,18} [Grab]{19} [choo]{15}.",
 "JHN.20.5": "Und{1} [er hät sich bückt]{2} und [gseht]{3} [d]{5} [Liinebinde]{6} [dalige]{4}; [aber]{8} [ine gange isch er]{9} [nöd]{7}.",
 "JHN.20.6": "[Dänn]{2} [chunnt]{1} [au]{3} [de Simon]{4} [Petrus]{5}, wo [ihm]{7} [nachechunnt]{6}, und{8} [isch]{9} [is]{10,11} [Grab]{12} [ine gange]{9}, und{13} [er gseht]{14} [d]{15} [Liinebinde]{16} [dalige]{17}.",
 "JHN.20.7": "Und{1} [s]{2} [Schweisstuech]{3}, [wo]{4} [uf]{6} [sim]{9} [Chopf]{7,8} [gsii isch]{5}, [isch]{14} [nöd]{10} [bi]{11} [de]{12} [Liinebinde]{13} [gläge]{14}, [sondern]{15} [für sich]{16} [zämegwicklet]{17} [a]{18} [eme eigete]{19} [Ort]{20}.",
 "JHN.20.8": "[Dänn]{1} [isch]{3} [jetzt]{2} [au]{4} [de ander]{5,6} [Jünger]{7} [ine gange]{3}, [wo]{8} [als Erschte]{10} [zum]{11,12} [Grab]{13} [choo isch]{9}, und{14} [er hät gseh]{15} und{16} [hät glaubt]{17}.",
 "JHN.20.9": "[Si händ]{3} [nämli]{2} [d]{4} [Schrift]{5} [no nöd]{1} [kännt]{3}, [dass]{6} [er]{8} [vo]{9} [de Tote]{10} [mües]{7} [uferstaa]{11}.",
 "JHN.20.10": "[Dänn]{2} [sind]{1} [d Jünger]{6,7} [wider]{3} [hei]{4,5:idiom} [gange]{1}.",
 "JHN.20.11": "[D Maria]{1} [aber]{2} [isch]{3} [dusse]{7} [bim]{4,5} [Grab]{6} [gstande]{3} [und hät briegget]{8}. [Wo]{9} si [jetzt]{10} [eso briegget hät]{11}, [hät si sich bückt]{12} und [is]{13,14} [Grab]{15} ine gluegt.",
 "JHN.20.12": "Und{1} [si gseht]{2} [zwei]{3} [Ängel]{4} [in]{5} [wiisse Chleider]{6} [dasitze]{7}, [eine]{8} [bim]{9,10} [Chopf]{11} und{12} [eine]{13} [bi]{14} [de]{15} [Füess]{16}, [wo]{17} [de Liib]{19,20} [vom Jesus]{21,22} [gläge isch]{18}.",
 "JHN.20.13": "Und{1} [die]{4} [säged]{2} [zu ere]{3}: «[Frau]{5}, [werum]{6} [brieggisch]{7}?» [Si seit]{8} [zu ine]{9}: «[Si händ]{11} [min]{14} [Herr]{12,13} [wäggnoo]{11}, und{15} [ich weiss]{17} [nöd]{16}, [wo]{18} [si]{19} [en]{20} [anegleit händ]{19}.» ~10(" + RIGHT_G + ")",
 "JHN.20.14": "[Wo si]{2} [das]{1} [gseit hät]{2}, [hät si sich umdrääit]{3-6} und{7} [gseht]{8} [de Jesus]{9,10} [dastaa]{11}, und{12} [si hät]{14} [nöd]{13} [gwüsst]{14}, [dass]{15} es [de Jesus]{16} [isch]{17}.",
 "JHN.20.15": "[De Jesus]{3} [seit]{1} [zu ere]{2}: «[Frau]{4}, [werum]{5} [brieggisch]{6}? [Wän]{7} [suechsch]{8}?» [Si]{9} [hät gmeint]{10}, [dass]{11} es [de Gärtner]{12,13} [sig]{14}, und [seit]{15} [zu ihm]{16}: «[Herr]{17}, [wänn]{18} [du]{19} [en]{21} [wäggträge häsch]{20}, [säg]{22} [mer]{23}, [wo]{24} [du]{25} [en]{26} [anegleit häsch]{25}, [dänn hol]{29} [ich]{27} [en]{28}.»",
 "JHN.20.16": "[De Jesus]{3} [seit]{1} [zu ere]{2}: «[Mariam]{4}!» [Si]{6} [hät sich umdrääit]{5} und [seit]{7} [zu ihm]{8} [uf Hebräisch]{9}: «[Rabbuni]{10}!», [das]{11} [heisst]{12}: «[Lehrer]{13}!»",
 "JHN.20.17": "[De Jesus]{3} [seit]{1} [zu ere]{2}: «[Heb]{6} [mich]{5} [nöd]{4} [fescht]{6}! [Ich bi]{9} [nämli]{8} [no nöd]{7} [zum]{10,11} [Vatter]{12} [ufegstige]{9}. [Gang]{13} [aber]{14} [zu]{15} [mine]{18} [Brüedere]{16,17} und{19} [säg]{20} [ine]{21}: ‹[Ich stiig ufe]{22} [zu]{23} [mim]{26} [Vatter]{24,25} und{27} [euem]{29} [Vatter]{28}, und{30} zu [mim]{32} [Gott]{31} und{33} [euem]{35} [Gott]{34}.›»",
 "JHN.20.18": "[D Mariam]{2} [vo Magdala]{3,4} [chunnt]{1} und [verchündet]{5} [de Jünger]{6,7}: «[Ich han]{9} [de Herr]{10,11} [gseh]{9}», und{12} [dass er]{14} [ere]{15} [das]{13} [gseit heig]{14}. ~8(" + RIGHT_G + ")",
 "JHN.20.19": "[Wo s]{1} [jetzt]{2} [Aabig]{3} [gsii isch]{1} [a däm]{4,6} [Tag]{5}, [em erschte]{7,8} [vo de Wuche]{9}, und{10} [d Tüüre]{11,12} dört, [wo]{14} [d Jünger]{16,17} [gsii sind]{15}, [us]{18} [Angscht]{19,20} [vor de Jude]{21,22} [bschlosse gsii sind]{13}, [isch]{23} [de Jesus]{24,25} [choo]{23} und{26} [isch]{27} [i]{28} [d Mitti]{29,30} [gstande]{27} und{31} [seit]{32} [zu ine]{33}: «[Fride]{34} [mit eu]{35}!»",
 "JHN.20.20": "Und{1} [wo er]{3} [das]{2} [gseit hät]{3}, [hät er]{4} [ine]{10} [d]{5} [Händ]{6} und{7} [d]{8} [Siite]{9} [zeigt]{4}. [Da]{12} [händ sich]{11} [d Jünger]{13,14} [gfröit]{11}, [wo si]{15} [de Herr]{16,17} [gseh händ]{15}.",
 "JHN.20.21": "[Dänn]{2} [hät]{1} [de Jesus]{4,5} [wider]{6} [zu ine]{3} [gseit]{1}: «[Fride]{7} [mit eu]{8}! [Wie]{9} [de Vatter]{12,13} [mich]{11} [gschickt hät]{10}, [so schick]{15} [au ich]{14} [eu]{16}.»",
 "JHN.20.22": "Und{1} [wo er]{3} [das]{2} [gseit hät]{3}, [hät er si aaghuucht]{4} und{5} [seit]{6} [zu ine]{7}: «[Nämed]{8} [heilige]{10} [Geischt]{9}!",
 "JHN.20.23": "[Wem]{1,2} [ir]{3} [d]{4} [Sünde]{5} [vergäbed]{3}, [däm]{7} [sind si vergää]{6}; [wem]{8,9} [ir]{10} si [bhalted]{10}, däm [sind si bhalte]{11}.»",
 "JHN.20.24": "[De Thomas]{1} [aber]{2}, [eine]{3} [vo de Zwölf]{4-6}, [wo]{7} [mer]{8} [«Zwilling»]{9} [seit]{8}, [isch]{11} [nöd]{10} [bi]{12} [ine]{13} [gsii]{11}, [wo]{14} [de Jesus]{16} [choo isch]{15}.",
 "JHN.20.25": "[Dänn]{2} [händ]{1} [di andere]{4,5} [Jünger]{6} [zu ihm]{3} [gseit]{1}: «[Mer händ]{7} [de Herr]{8,9} [gseh]{7}!» [Er]{10} [aber]{11} [hät]{12} [zu ine]{13} [gseit]{12}: «[Wänn]{14} [ich]{16} [nöd]{15} [a]{17} [sine]{20} [Händ]{18,19} [s]{21} [Mal]{22} [vo de Nägel]{23,24} [gseh]{16} und{25} [min]{29} [Finger]{27,28} [i]{30} [s]{31} [Mal]{32} [vo de Nägel]{33,34} [lege]{26} und{35} [mini]{37} [Hand]{38,39} [i]{40} [sini]{43} [Siite]{41,42} [lege]{36}, [glaub ich]{46} [ganz sicher nöd]{44,45}.»",
 "JHN.20.26": "Und{1} [nach]{2} [acht]{4} [Täg]{3} [sind]{6} [sini]{10} [Jünger]{8,9} [wider]{5} [dinne]{7} [gsii]{6}, und{11} [de Thomas]{12} [bi]{13} [ine]{14}. Da [chunnt]{15} [de Jesus]{16,17} [bi bschlossne]{20} [Tüüre]{18,19} und{21} [isch]{22} [i]{23} [d Mitti]{24,25} [gstande]{22} und{26} [hät gseit]{27}: «[Fride]{28} [mit eu]{29}!»",
 "JHN.20.27": "[Dänn]{1} [seit er]{2} [zum Thomas]{3,4}: «[Streck]{5} [din]{8} [Finger]{6,7} [da ane]{9} und{10} [lueg]{11} [mini]{14} [Händ]{12,13} [aa]{11}, und{15} [streck]{16} [dini]{19} [Hand]{17,18} [här]{16} und{20} [leg si]{21} [i]{22} [mini]{25} [Siite]{23,24}, und{26} [bis]{28} [nöd]{27} [ungläubig]{29}, [sondern]{30} [gläubig]{31}!»",
 "JHN.20.28": "[De Thomas]{2} [hät gantwortet]{1} und{3} [zu ihm]{5} [gseit]{4}: «[Min]{8} [Herr]{6,7} und{9} [min]{12} [Gott]{10,11}!»",
 "JHN.20.29": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: «[Wil]{5} [du]{6} [mich]{7} [gseh häsch]{6}, [häsch glaubt]{8}? [Sälig]{9} sind [die]{10}, wo [nöd]{11} [gseh händ]{12} und{13} [trotzdem glaubt händ]{14}!»",
 "JHN.20.30": "[No]{4} [vili]{1} [anderi]{5} [Zeiche]{6} [hät]{7} [de Jesus]{8,9} [zwar]{2} [vor]{10} [de Jünger]{11,12} [gmacht]{7}, [wo]{13} [nöd]{14} [i]{17} [däm]{20} [Buech]{18,19} [ufgschribe]{16} [sind]{15}. ~3(οὖν «also» nach μέν; nöd eigens widergää)",
 "JHN.20.31": "[Die]{1} [aber]{2} [sind ufgschribe]{3}, [demit]{4} [ir glaubed]{5}, [dass]{6} [de Jesus]{7} [de Christus]{9,10} [isch]{8}, [de Sohn]{11,12} [vo Gott]{13,14}, und{15} [demit]{16} [ir]{19} [als Gläubigi]{17} [Läbe]{18} [händ]{19} [in]{20} [sim]{23} [Name]{21,22}.",
 # ------------------------------------------------------------ Kapitel 21
 "JHN.21.1": "[Nachher]{1,2} [hät]{3} [sich]{4} [de Jesus]{6,7} [de Jünger]{8,9} [no einisch]{5} [offebaret]{3}, [am]{10,11} [See]{12} [vo Tiberias]{13,14}. [Er hät sich]{15} [aber]{16} [eso]{17} [offebaret]{15}:",
 "JHN.21.2": "[Es sind]{1} [binenand]{2} [gsii]{1}: [de Simon]{3} [Petrus]{4} und{5} [de Thomas]{6}, [wo]{7} [mer]{8} [«Zwilling»]{9} [seit]{8}, und{10} [de Natanaël]{11} [vo]{12,13} [Kana]{14} [z]{15} [Galiläa]{16} und{17} [d Söön]{18} [vom Zebedäus]{19,20} und{21} [zwei]{27} [anderi]{22} [vo]{23} [sine]{26} [Jünger]{24,25}.",
 "JHN.21.3": "[De Simon]{3} [Petrus]{4} [seit]{1} [zu ine]{2}: «[Ich gaa]{5} [go fische]{6}.» [Si säged]{7} [zu ihm]{8}: «[Mir]{11} [chömed]{9} [au]{10} [mit]{12} [dir]{13}.» [Si sind usegange]{14} und{15} [is]{17,18} [Boot]{19} [gstige]{16}, und{20} [i]{21} [dere]{22,23} [Nacht]{24} [händ si]{25} [nüüt]{26} [gfange]{25}.",
 "JHN.21.4": "[Wo s]{4} [aber]{2} [scho]{3} [Morge]{1} [worde isch]{4}, [isch]{5} [de Jesus]{6} [am]{7,8} [Ufer]{9} [gstande]{5}; [d Jünger]{13,14} [händ]{12} [aber]{11} [nöd]{10} [gwüsst]{12}, [dass]{15} es [de Jesus]{16} [isch]{17}.",
 "JHN.21.5": "[Dänn]{2} [seit]{1} [de Jesus]{4,5} [zu ine]{3}: «[Chind]{6}, [händ ir]{10} [ächt]{7} [öppis]{8} [z ässe]{9}?» [Si händ]{11} [ihm]{12} [gantwortet]{11}: «[Nei]{13}.»",
 "JHN.21.6": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: «[Rüered]{5} [s]{12} [Netz]{13} [uf]{6} [di rächt]{7,8} [Siite]{9} [vom Boot]{10,11} [us]{5}, und{14} [ir wärded]{15} öppis [finde]{15}.» [Dänn]{17} [händ si s]{16} [usegrüert]{16}, und{18} [si händ]{22} [s]{20} [nüme]{19} [chöne]{22} [iizie]{21} [wäge]{23} [de Mängi]{24,25} [vo Fisch]{26,27}.",
 "JHN.21.7": "[Dänn]{2} [seit]{1} [dä]{5} [Jünger]{3,4}, [wo]{6} [de Jesus]{8,9} [gliebt hät]{7}, [zum Petrus]{10,11}: «[Es isch]{14} [de Herr]{12,13}!» [Wo]{18} [jetzt]{16} [de Simon]{15} [Petrus]{17} [ghört hät]{18}, [dass]{19} es [de Herr]{20,21} [isch]{22}, [hät er sich]{25} [s]{23} [Oberchleid]{24} [umgürtet]{25} – [er isch]{26} [nämli]{27} [blutt]{28} [gsii]{26} – und{29} [hät]{30} [sich]{31} [in]{32} [de See]{33,34} [gstürzt]{30}.",
 "JHN.21.8": "[Di andere]{1,3} [Jünger]{4} [aber]{2} [sind]{7} [mit em]{5} [Boot]{6} [choo]{7} – [si sind]{10} [nämli]{9} [nöd]{8} [wiit]{11} [vom]{12,13} [Land]{14} [gsii]{10}, [sondern]{15} nu [öppe]{16} [zweihundert]{19} [Elle]{18} [ewäg]{17} – und [händ]{20} [s]{21} [Netz]{22} [mit de Fisch]{23,24} [nachegschleikt]{20}.",
 "JHN.21.9": "[Wo]{1} [si]{3} [jetzt]{2} [a]{4} [Land]{5,6} [gstige sind]{3}, [gsehnd si]{7} [es Cholefüür]{8} [am Bode]{9} und{10} [Fisch]{11}, [wo druf liit]{12}, und{13} [Broot]{14}.",
 "JHN.21.10": "[De Jesus]{3,4} [seit]{1} [zu ine]{2}: «[Bringed]{5} [vo]{6} [de Fisch]{7,8}, [wo]{9} [ir]{10} [grad]{11} [gfange händ]{10}!»",
 "JHN.21.11": "[Dänn]{2} [isch]{1} [de Simon]{3} [Petrus]{4} [ufegstige]{1} und{5} [hät]{6} [s]{7} [Netz]{8} [a]{9} [Land]{10,11} [zoge]{6}, [voll]{12} vo [grosse]{14} [Fisch]{13}, [hundertdrüüefüfzg]{15-17}; und{18} [obwohl]{20} es [so vil]{19} [gsii sind]{20}, [isch]{22} [s]{23} [Netz]{24} [nöd]{21} [verrisse]{22}.",
 "JHN.21.12": "[De Jesus]{3,4} [seit]{1} [zu ine]{2}: «[Chömed]{5}, [ässed]{6}!» [Keine]{7} [vo de Jünger]{10,11} [aber]{8} [hät sich traut]{9}, [en]{13} [z fröge]{12}: «[Wer]{15} [bisch]{16} [du]{14}?» – [si händ]{17} ja [gwüsst]{17}, [dass]{18} es [de Herr]{19,20} [isch]{21}.",
 "JHN.21.13": "[De Jesus]{2,3} [chunnt]{1} und{4} [nimmt]{5} [s]{6} [Broot]{7} und{8} [git]{9} s [ine]{10}, und{11} [ebeso]{14} [de]{12} [Fisch]{13}.",
 "JHN.21.14": "[Das]{1} isch [scho]{2} [s dritt Mal]{3} gsii, dass sich [de Jesus]{5,6} [de Jünger]{7,8} [offebaret hät]{4}, [nachdem er]{9} [vo]{10} [de Tote]{11} [uferweckt worde isch]{9}.",
 "JHN.21.15": "[Wo]{1} [si]{3} [jetzt]{2} [ggässe händ]{3}, [seit]{4} [de Jesus]{8,9} [zum Simon]{5,6} [Petrus]{7}: «[Simon]{10}, [Sohn vom Johannes]{11}, [liebsch]{12} [mich]{13} [meh]{14} [als die]{15}?» [Er seit]{16} [zu ihm]{17}: «[Ja]{18}, [Herr]{19}, [du]{20} [weisch]{21}, [dass]{22} [ich]{23} [dich]{24} [gärn han]{23}.» [Er seit]{25} [zu ihm]{26}: «[Weid]{27} [mini]{30} [Lämmli]{28,29}!»",
 "JHN.21.16": "[Er seit]{1} [wider]{3}, [es zweits Mal]{4}, [zu ihm]{2}: «[Simon]{5}, [Sohn vom Johannes]{6}, [liebsch]{7} [mich]{8}?» [Er seit]{9} [zu ihm]{10}: «[Ja]{11}, [Herr]{12}, [du]{13} [weisch]{14}, [dass]{15} [ich]{16} [dich]{17} [gärn han]{16}.» [Er seit]{18} [zu ihm]{19}: «[Hüet]{20} [mini]{23} [Schaf]{21,22}!»",
 "JHN.21.17": "[Er seit]{1} [zu ihm]{2} [zum dritte Mal]{3,4}: «[Simon]{5}, [Sohn vom Johannes]{6}, [häsch]{7} [mich]{8} [gärn]{7}?» [De Petrus]{10,11} [isch truurig worde]{9}, [wil]{12} [er]{13} [zum dritte Mal]{15,16} [zu ihm]{14} [gseit hät]{13}: «[Häsch]{17} [mich]{18} [gärn]{17}?», und{19} [er hät]{20} [zu ihm]{21} [gseit]{20}: «[Herr]{22}, [du]{24} [weisch]{25} [alles]{23}; [du]{26} [erchännsch]{27}, [dass]{28} [ich]{29} [dich]{30} [gärn han]{29}.» [De Jesus]{33,34} [seit]{31} [zu ihm]{32}: «[Weid]{35} [mini]{38} [Schaf]{36,37}!",
 "JHN.21.18": "[Amen]{1}, [amen]{2}, [ich säge]{3} [dir]{4}: [Wo]{5} [du]{6} [jünger]{7} [gsii bisch]{6}, [häsch]{8} [dich sälber]{9} [gürtet]{8} und{10} [bisch umegloffe]{11}, [wo]{12} [du häsch wele]{13}; [wänn]{14} [du]{16} [aber]{15} [alt worde bisch]{16}, [wirsch]{17} [dini]{20} [Händ]{18,19} [usstrecke]{17}, und{21} [en andere]{22} [wird]{24} [dich]{23} [gürte]{24} und{25} [dich bringe]{26}, [wo]{27} [du]{29} [nöd]{28} [wottsch]{29}.»",
 "JHN.21.19": "[Das]{1} [aber]{2} [hät er gseit]{3}, [zum aazeige]{4}, [mit was für eme]{5} [Tod]{6} [er]{7} [Gott]{8,9} [würd verherrliche]{7}. Und{10} [wo er]{12} [das]{11} [gseit hät]{12}, [seit er]{13} [zu ihm]{14}: «[Chumm]{15} [mir]{16} [nache]{15}!»",
 "JHN.21.20": "[De Petrus]{2,3} [drääit sich um]{1} und [gseht]{4} [de]{5} [Jünger]{6} [nachechoo]{11}, [wo]{7} [de Jesus]{9,10} [gliebt hät]{8}, [dä]{12}, wo sich [au]{13} [bim]{15,16} [Aabigässe]{17} [a]{18} [sini]{21} [Bruscht]{19,20} [aaglänt hät]{14} und{22} [gseit hät]{23}: «[Herr]{24}, [wer]{25} [isch es]{26}, [wo]{27} [dich]{29} [usliferet]{28}?»",
 "JHN.21.21": "[Wo]{3} [de Petrus]{4,5} [jetzt]{2} [dä]{1} [gseh hät]{3}, [seit er]{6} [zum Jesus]{7,8}: «[Herr]{9}, [was]{12} isch [aber]{11} [mit däm]{10}?»",
 "JHN.21.22": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: «[Wänn]{5} [ich wott]{7}, [dass er]{6} [bliibt]{8}, [bis]{9} [ich chume]{10}, [was]{11} [gaat]{12} das [dich]{13} [aa]{12}? [Du]{14} – [chumm]{16} [mir]{15} [nache]{16}!»",
 "JHN.21.23": "[Dänn]{2} [hät sich]{1} [das]{3} [Wort]{4,5} [under]{6} [de Brüedere]{7,8} [verbreitet]{1}: [Dä]{12} [Jünger]{10,11} [stirbt]{14} [nöd]{13}. [De Jesus]{19,20} hät [ihm]{18} [aber]{17} [nöd]{15} [gseit]{16}, [dass]{21} er [nöd]{22} [stärbi]{23}, [sondern]{24}: «[Wänn]{25} [ich wott]{27}, [dass er]{26} [bliibt]{28}, [bis]{29} [ich chume]{30}, [was]{31} [gaat]{32} das [dich]{33} [aa]{32}?» ~9(ὅτι leitet de Inhalt vom Wort ii)",
 "JHN.21.24": "[Das]{1} [isch]{2} [de Jünger]{3,4}, [wo]{5} [über]{7} [das alles]{8} [Zügnis ablegt]{6} und{9} [wo]{10} [das]{12} [gschribe hät]{11}, und{13} [mer wüssed]{14}, [dass]{15} [sis]{17} [Zügnis]{18,19} [wahr]{16} [isch]{20}.",
 "JHN.21.25": "[Es git]{1} [aber]{2} [au]{3} [no vil]{5} [anders]{4}, [wo]{6} [de Jesus]{8,9} [gmacht hät]{7}; [wänn]{11} [das]{10} [einzeln]{13,14} [ufgschribe würd]{12}, [chönnt]{20}, [mein ich]{17}, [nöd emal]{15} [d Wält]{18,19} [sälber]{16} [di]{21} [Büecher]{23} [fasse]{20}, [wo dänn gschribe würded]{22}.",
}

GRUND = "Grundentscheid in scripts/authoring/johannes_text_01_03.py"

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("JHN.20.1", "ersten Tag der Woche", "literal", "μιᾷ τῶν σαββάτων", "ersten der Sabbate", None, "σάββατα heisst auch «Woche»; gemeint ist der Tag nach dem Sabbat (vgl. [[MRK.16.2]]). Ebenso [[JHN.20.19]]."),
 ("JHN.20.1", "Maria aus Magdala", "interpretive", "Μαρία Μαγδαληνὴ", "Maria, die Magdalenerin", ["Maria Magdalena"], "Herkunftsbezeichnung nach dem Ort Magdala am See Gennesaret; ebenso [[JHN.20.18]]."),
 ("JHN.20.2", "lieb hatte", "literal", "ἐφίλει", None, ["liebte"], "Durchgehend gilt in dieser Übersetzung: ἀγαπάω «lieben», φιλέω «lieb haben». Denselben Jünger nennt das Evangelium sonst den, «den Jesus liebte» (ἀγαπάω, [[JHN.13.23]], [[JHN.21.7]], [[JHN.21.20]]); hier steht φιλέω. Siehe die Entscheidung zu [[JHN.21.15]]."),
 ("JHN.20.2", "den Herrn", "literal", "κύριον", None, None, "κύριος ist in den Ostergeschichten die Bezeichnung des Auferstandenen ([[JHN.20.18]], [[JHN.20.20]], [[JHN.20.25]], [[JHN.21.7]]); in [[JHN.20.15]] ist «Herr» dagegen die höfliche Anrede an einen vermeintlichen Gärtner."),
 ("JHN.20.5", "Leinenbinden", "interpretive", "ὀθόνια", None, ["Leinentücher", "Leinenstreifen"], "ὀθόνιον bezeichnet ein (kleineres) Stück Leinen. Ob Binden oder Tücher gemeint sind, lässt sich nicht sicher sagen; vgl. [[JHN.19.40]]."),
 ("JHN.20.6", "er schaut", "literal", "θεωρεῖ", None, ["er sieht", "er betrachtet"], "In [[JHN.20.5]]–[[JHN.20.8]] stehen drei Verben des Sehens: βλέπει («sieht»), θεωρεῖ («schaut») und εἶδεν («sah»). Die Übersetzung hält θεωρέω als «schauen» auseinander (ebenso [[JHN.20.12]], [[JHN.20.14]]). Ob Johannes eine Steigerung des Sehens andeuten will oder die Verben einfach abwechselt, ist umstritten."),
 ("JHN.20.7", "Schweisstuch", "traditional", "σουδάριον", None, ["Kopftuch", "Tuch"], "Lehnwort aus dem Lateinischen (sudarium, «Schweisstuch»); ein Tuch für das Gesicht, wie bei Lazarus ([[JHN.11.44]])."),
 ("JHN.20.8", "er sah und glaubte", "literal", "εἶδεν ἐπίστευσεν", None, None, "Was er glaubte, sagt der Text nicht ausdrücklich. Meist wird es als Glaube an die Auferstehung verstanden; [[JHN.20.9]] («sie kannten die Schrift noch nicht») steht dazu in Spannung und wird verschieden erklärt. Andere lesen: Er glaubte Marias Bericht. Gegen diese Lesart spricht, dass πιστεύω ohne Objekt im Evangelium sonst den Glauben an Jesus bezeichnet."),
 ("JHN.20.9", "die Schrift", "literal", "γραφὴν", None, None, "Welche Schriftstelle gemeint ist, sagt der Text nicht."),
 ("JHN.20.10", "nach Hause", "adapted", "πρὸς αὑτοὺς", "zu sich", ["zu den Ihren"], "Griechische Wendung für «heim, nach Hause»."),
 ("JHN.20.13", "Frau", "literal", "Γύναι", None, None, "Respektvolle Anrede, nicht abschätzig; so redet Jesus auch seine Mutter an ([[JHN.2.4]], [[JHN.19.26]])."),
 ("JHN.20.16", "Mariam", "literal", "Μαριάμ", None, ["Maria"], "Johannes wechselt zwischen Μαρία ([[JHN.20.1]], [[JHN.20.11]]) und der semitischen Form Μαριάμ ([[JHN.20.16]], [[JHN.20.18]]); die Übersetzung behält den Wechsel bei. RP liest an beiden Stellen Μαρία (SBLGNT-Apparat); nach den CNTR-Transkriptionen schreiben auch 02 und 05 in [[JHN.20.16]] sowie 02, 05 und 032 in [[JHN.20.18]] μαρια."),
 ("JHN.20.16", "auf Hebräisch", "literal", "Ἑβραϊστί", None, ["auf Aramäisch"], "Rabbuni ist aramäisch. Ἑβραϊστί bezeichnet bei Johannes die Sprache der Juden im Land, auch bei aramäischen Wörtern (vgl. [[JHN.19.13]], [[JHN.19.17]])."),
 ("JHN.20.16", "Rabbuni", "literal", "Ραββουνι", None, None, "Erweiterte Form von «Rabbi», etwa «mein Lehrer, mein Meister»; Johannes übersetzt selbst."),
 ("JHN.20.17", "Halte mich nicht fest", "interpretive", "Μή μου ἅπτου", "Berühre mich nicht", ["Rühre mich nicht an", "Klammere dich nicht an mich"], "ἅπτομαι heisst «anfassen, sich festhalten an». Der Imperativ Präsens mit μή verbietet oft ein Tun, das schon im Gang ist: «Hör auf, mich festzuhalten». Die vertraute Wiedergabe «Rühre mich nicht an» (lateinisch Noli me tangere) versteht es als Verbot der Berührung; dagegen wird angeführt, dass Thomas Jesus berühren soll ([[JHN.20.27]]). Wie die Begründung «denn ich bin noch nicht zum Vater hinaufgestiegen» zu verstehen ist, wird verschieden gedeutet. Redaktionelle Entscheidung."),
 ("JHN.20.17", "Brüdern", "interpretive", "ἀδελφούς", None, ["Geschwistern"], "Gemeint sind die Jünger ([[JHN.20.18]]). ἀδελφοί kann Brüder und Schwestern umfassen. Erst hier nennt Jesus die Jünger seine Brüder; ebenso [[JHN.21.23]]."),
 ("JHN.20.17", "Ich steige hinauf", "literal", "Ἀναβαίνω", None, ["Ich fahre auf", "Ich gehe hinauf"], "Präsens: der Aufstieg zum Vater hat schon begonnen oder steht unmittelbar bevor. ἀναβαίνω wie in [[JHN.3.13]] und [[JHN.6.62]]."),
 ("JHN.20.17", "zu meinem Vater und eurem Vater, und zu meinem Gott und eurem Gott", "literal", "πατέρα μου πατέρα ὑμῶν θεόν μου θεὸν ὑμῶν", None, None, "Jesus sagt nicht «unser Vater»: Er verbindet die Jünger mit seinem Vater und unterscheidet zugleich «mein» und «euer». Wie stark die Unterscheidung zu gewichten ist, wird verschieden beurteilt."),
 ("JHN.20.19", "vor den Juden", "interpretive", "Ἰουδαίων", None, ["vor den jüdischen Führern", "vor den Judäern"], "Grundentscheid (" + GRUND + "): οἱ Ἰουδαῖοι wird wörtlich mit «die Juden» wiedergegeben. Das Wort steht im Johannesevangelium 71-mal (Zählung nach MACULA-Lemma) und meint je nach Stelle das jüdische Volk, die Bewohner Judäas oder die führenden Kreise in Jerusalem, die Jesus ablehnen; hier wohl Letztere, denn auch die Jünger sind Juden. Die wörtliche Wiedergabe hält den Sprachgebrauch des Evangeliums sichtbar; sie ist kein Urteil über das jüdische Volk. Gegenargument: Heute wird «die Juden» leicht pauschal gehört; deshalb übersetzen manche kontextbezogen, etwa «die jüdischen Führer»."),
 ("JHN.20.19", "Friede euch", "literal", "Εἰρήνη ὑμῖν", None, ["Friede sei mit euch"], "Der übliche Gruss (hebräisch šālôm). Im Zusammenhang erinnert er an die Abschiedsrede ([[JHN.14.27]], [[JHN.16.33]]). Ebenso [[JHN.20.21]], [[JHN.20.26]]."),
 ("JHN.20.20", "Seite", "literal", "πλευρὰν", None, None, "Die mit der Lanze geöffnete Seite ([[JHN.19.34]])."),
 ("JHN.20.21", "gesandt hat", "literal", "ἀπέσταλκέν", None, None, "ἀποστέλλω und πέμπω («so sende auch ich euch») sind beide mit «senden» wiedergegeben; Johannes gebraucht beide für die Sendung Jesu durch den Vater, ein klarer Bedeutungsunterschied ist nicht erkennbar."),
 ("JHN.20.22", "hauchte er sie an", "adapted", "ἐνεφύσησεν", "hauchte er (hinein)", ["blies er sie an"], "Das Verb hat kein Objekt; «sie» ist ergänzt. Es kommt im Johannesevangelium nur hier vor. Dasselbe Verb steht nach gängiger Angabe in der griechischen Übersetzung von [[GEN.2.7]] (Gott haucht dem Menschen Lebensatem ein) und [[EZK.37.9]] (in den Projektdaten nicht geprüft); ob Johannes darauf anspielt, ist eine verbreitete Deutung, keine Aussage des Textes."),
 ("JHN.20.22", "heiligen Geist", "literal", "πνεῦμα ἅγιον", None, ["den Heiligen Geist"], "Ohne Artikel. Wie sich diese Gabe zur Verheissung des Beistands ([[JHN.14.16]]–[[JHN.14.17]], [[JHN.16.7]]) und zu Pfingsten ([[ACT.2.1]]–[[ACT.2.4]]) verhält, wird verschieden gedeutet."),
 ("JHN.20.23", "sind sie vergeben", "literal", "ἀφέωνται", None, ["werden sie vergeben"], "Perfekt Passiv: «sind vergeben (worden)». Das Passiv lässt Gott als Handelnden mitdenken. Ob die Jünger Gottes Vergebung zusprechen, sie vollmächtig gewähren oder bestätigen, beantworten die kirchlichen Lehrtraditionen unterschiedlich; die Übersetzung entscheidet das nicht. Zur Lesart ἀφίενται siehe Alternative."),
 ("JHN.20.23", "behaltet", "interpretive", "κρατῆτε", "festhaltet", ["nicht vergebt"], "κρατέω «festhalten, ergreifen»; als Gegenstück zu «vergeben»: die Sünden bleiben bestehen."),
 ("JHN.20.24", "«Zwilling»", "literal", "Δίδυμος", None, ["Didymus"], "Δίδυμος heisst «Zwilling» und übersetzt den aramäischen Namen Thomas (tᵉʾômāʾ, «Zwilling»). Ebenso [[JHN.11.16]], [[JHN.21.2]]."),
 ("JHN.20.25", "das Mal der Nägel", "literal", "τύπον ἥλων", "den Abdruck der Nägel", ["die Nägelmale"], None),
 ("JHN.20.27", "sei nicht ungläubig, sondern gläubig", "adapted", "μὴ γίνου ἄπιστος πιστός", "werde nicht ungläubig, sondern gläubig", ["sei nicht ohne Glauben, sondern glaube"], "γίνομαι heisst «werden»; im Deutschen ist «sei» natürlicher. Das Wortspiel ἄπιστος/πιστός ist mit «ungläubig/gläubig» nachgebildet. Ob Thomas Jesus tatsächlich berührt, erzählt der Text nicht."),
 ("JHN.20.28", "Mein Herr und mein Gott", "literal", "κύριός θεός", None, None, "Nominativ mit Artikel als Anrede, wie im Griechischen üblich. Der Satz ist «zu ihm», also an Jesus gerichtet; die Deutung als blosser Ausruf des Staunens wird vertreten, passt aber weniger zu dieser Einleitung. Das Bekenntnis nimmt [[JHN.1.1]] und [[JHN.1.18]] auf."),
 ("JHN.20.29", "Weil du mich gesehen hast, hast du geglaubt?", "interpretive", "Ὅτι ἑώρακάς με πεπίστευκας;", None, ["Weil du mich gesehen hast, hast du geglaubt."], "Der SBLGNT setzt hier ein Fragezeichen; die Übersetzung folgt ihm. Die frühen Handschriften haben keine Satzzeichen; der Satz kann ebenso als Feststellung gelesen werden. Redaktionelle Entscheidung."),
 ("JHN.20.29", "Selig", "traditional", "μακάριοι", None, ["Glücklich", "Glücklich zu preisen"], "μακάριος preist jemanden als von Gott beschenkt glücklich (vgl. [[JHN.13.17]])."),
 ("JHN.20.29", "die nicht gesehen und doch geglaubt haben", "literal", "μὴ ἰδόντες πιστεύσαντες", None, ["die nicht sehen und doch glauben"], "Aorist-Partizipien; sie können zeitlos die späteren Glaubenden meinen. «doch» ist ergänzt."),
 ("JHN.20.30", "Zeichen", "literal", "σημεῖα", None, ["Wunder", "Wunderzeichen"], "Grundentscheid (" + GRUND + "): σημεῖον durchgehend «Zeichen», nicht «Wunder». Johannes nennt die Taten Jesu Zeichen, die auf ihn hinweisen ([[JHN.2.11]]); das Wort steht im Evangelium 17-mal (Zählung nach MACULA-Lemma)."),
 ("JHN.20.31", "damit ihr glaubt", "interpretive", "πιστεύητε", None, ["damit ihr zum Glauben kommt", "damit ihr im Glauben bleibt"], "Lesart mit Wirkung auf den Sinn. Der SBLGNT liest mit WH πιστεύητε (Präsens); das kann «weiter glauben, im Glauben bleiben» betonen. Treg, NA28 und RP lesen πιστεύσητε (Aorist); das kann «zum Glauben kommen» betonen (siehe Alternative). Daraus wird oft auf den Zweck des Buches geschlossen: Stärkung von Glaubenden oder Werbung für den Glauben. Gegenargument: Johannes gebraucht den Aorist auch gegenüber Jüngern, die schon glauben ([[JHN.11.15]], [[JHN.13.19]], [[JHN.14.29]]), und das Präsens gegenüber Menschen, die noch nicht glauben ([[JHN.6.29]]); die Zeitform allein entscheidet die Frage nicht. «damit ihr glaubt» lässt beides offen; redaktionelle Entscheidung."),
 ("JHN.20.31", "der Christus", "traditional", "χριστὸς", None, ["der Messias", "der Gesalbte"], "χριστός übersetzt hebräisch māšîaḥ «Gesalbter»."),
 ("JHN.20.31", "Leben", "literal", "ζωὴν", None, None, "Bei Johannes das Leben aus Gott, oft «ewiges Leben» genannt ([[JHN.3.16]])."),
 ("JHN.21.1", "offenbarte sich", "literal", "ἐφανέρωσεν ἑαυτὸν", None, ["zeigte sich"], "φανερόω «sichtbar machen, offenbaren». Ebenso [[JHN.21.14]]."),
 ("JHN.21.1", "See von Tiberias", "adapted", "θαλάσσης Τιβεριάδος", "Meer von Tiberias", ["See Gennesaret"], "θάλασσα heisst «Meer»; gemeint ist der See Gennesaret, den Johannes auch «See von Galiläa» nennt ([[JHN.6.1]]). Ebenso «See» in [[JHN.21.7]]."),
 ("JHN.21.2", "die Söhne des Zebedäus", "adapted", "οἱ Ζεβεδαίου", "die des Zebedäus", None, "Nur hier im Johannesevangelium erwähnt; ihre Namen nennt es nicht."),
 ("JHN.21.2", "Natanaël", "literal", "Ναθαναὴλ", None, ["Nathanael"], "Vgl. [[JHN.1.45]]–[[JHN.1.49]]; erst hier erfährt man, dass er aus Kana stammt."),
 ("JHN.21.5", "Kinder", "adapted", "Παιδία", None, ["Jungs", "Freunde"], "Vertrauliche Anrede an Erwachsene (vgl. [[1JN.2.18]])."),
 ("JHN.21.5", "etwas zu essen", "interpretive", "τι προσφάγιον", "eine Zukost", ["Fisch"], "προσφάγιον ist, was man zum Brot isst, meist Fisch; im Johannesevangelium nur hier. Die Frage mit μή erwartet ein Nein («etwa»)."),
 ("JHN.21.7", "liebte", "literal", "ἠγάπα", None, None, "Hier ἀγαπάω, in [[JHN.20.2]] für denselben Jünger φιλέω; siehe die Entscheidung zu [[JHN.21.15]]."),
 ("JHN.21.7", "Obergewand", "interpretive", "ἐπενδύτην", None, ["Überwurf", "Fischerkittel"], "ἐπενδύτης ist ein über anderem getragenes Kleidungsstück; im Johannesevangelium nur hier."),
 ("JHN.21.7", "nackt", "interpretive", "γυμνός", None, ["leicht bekleidet", "nur im Untergewand"], "γυμνός kann «ganz nackt» oder «nur leicht bekleidet» heissen; zur Arbeit legte man das Obergewand ab."),
 ("JHN.21.8", "zweihundert Ellen", "literal", "πηχῶν διακοσίων", None, ["etwa neunzig Meter"], "Eine Elle (Unterarmlänge) misst nach gängiger Angabe etwa 45 cm; zweihundert Ellen wären also rund neunzig Meter."),
 ("JHN.21.8", "Boot", "literal", "πλοιαρίῳ", "Bötchen", None, "Verkleinerungsform von πλοῖον; Johannes wechselt zwischen beiden Wörtern für dasselbe Boot ([[JHN.21.3]], [[JHN.21.6]])."),
 ("JHN.21.9", "ein Kohlenfeuer", "literal", "ἀνθρακιὰν", None, None, "Im Johannesevangelium steht ἀνθρακιά nur hier und beim Feuer im Hof des Hohepriesters, an dem Petrus Jesus verleugnete ([[JHN.18.18]]). Ob der Anklang beabsichtigt ist, ist eine Deutung."),
 ("JHN.21.9", "Fisch", "literal", "ὀψάριον", None, ["Fischspeise"], "ὀψάριον ist zubereiteter Fisch als Beilage zum Brot, wie bei der Speisung ([[JHN.6.9]], [[JHN.6.11]])."),
 ("JHN.21.11", "stieg Simon Petrus hinauf", "interpretive", "ἀνέβη", None, ["stieg Simon Petrus ins Boot", "ging Simon Petrus ans Ufer hinauf"], "Wohin er hinaufsteigt, sagt der Text nicht: ins Boot oder ans Ufer."),
 ("JHN.21.11", "hundertdreiundfünfzig", "literal", "ἑκατὸν πεντήκοντα τριῶν", None, None, "Die genaue Zahl ist seit der Alten Kirche gedeutet worden; nach gängiger Angabe sieht Augustinus in 153 die Summe der Zahlen 1 bis 17, Hieronymus verbindet sie mit der Zahl der damals bekannten Fischarten (für alle Völker). Der Text gibt keine Deutung; die Zahl kann auch einfach die Genauigkeit eines Augenzeugenberichts ausdrücken."),
 ("JHN.21.12", "esst", "adapted", "ἀριστήσατε", "frühstückt", ["haltet das Morgenmahl"], "ἀριστάω heisst «die (erste) Mahlzeit halten». Ebenso [[JHN.21.15]] («gegessen hatten»)."),
 ("JHN.21.14", "das dritte Mal", "literal", "τρίτον", None, None, "Gezählt werden die Erscheinungen vor den Jüngern: [[JHN.20.19]], [[JHN.20.26]] und diese; die Begegnung mit Maria ([[JHN.20.14]]) zählt der Erzähler nicht mit."),
 ("JHN.21.14", "auferweckt worden war", "literal", "ἐγερθεὶς", None, ["auferstanden war"], "Passiv von ἐγείρω «aufwecken»: Gott ist der Handelnde. In [[JHN.20.9]] steht dagegen ἀναστῆναι «auferstehen»."),
 ("JHN.21.15", "Sohn des Johannes", "adapted", "Ἰωάννου", "des Johannes", ["Sohn des Jona"], "Genitiv der Abstammung wie in [[JHN.1.42]]. Zur Lesart Ἰωνᾶ siehe Alternative."),
 ("JHN.21.15", "lieb habe", "interpretive", "ἀγαπᾷς φιλῶ", None, ["liebe (ohne Unterschied zu «lieben»)"], "Jesus fragt zweimal mit ἀγαπάω («liebst du mich»), Petrus antwortet jedes Mal mit φιλέω («ich habe dich lieb»); beim dritten Mal fragt Jesus selbst mit φιλέω ([[JHN.21.17]]). Die Übersetzung gibt die beiden Verben wie im ganzen Evangelium verschieden wieder («lieben» / «lieb haben»), damit der Wechsel sichtbar bleibt; sie will damit keine Abstufung festlegen. Deutung A: Der Wechsel ist bedeutsam. Petrus wagt nach seiner Verleugnung nur das bescheidenere Wort; beim dritten Mal kommt Jesus ihm entgegen, und Petrus wird traurig, weil Jesus nun sogar dieses Wort in Frage stellt. Gegenargument und Deutung B: Johannes gebraucht beide Verben ohne erkennbaren Unterschied, etwa für die Liebe des Vaters zum Sohn (ἀγαπάω [[JHN.3.35]], φιλέω [[JHN.5.20]]), für Lazarus (φιλέω [[JHN.11.3]], ἀγαπάω [[JHN.11.5]]) und für den Jünger, «den Jesus liebte» (ἀγαπάω [[JHN.13.23]], φιλέω [[JHN.20.2]]); auch sonst wechselt das Gespräch die Wörter (βόσκω/ποιμαίνω, ἀρνία/πρόβατα, οἶδα/γινώσκω), und [[JHN.21.17]] begründet die Trauer ausdrücklich mit dem «dritten Mal». Im Evangelium steht ἀγαπάω 37-mal, φιλέω 13-mal (Zählung nach MACULA-Lemma). Nach der CNTR-Transkription liest 032 in der dritten Frage ἀγαπᾷς statt φιλεῖς (im SBLGNT-Apparat nicht erfasst)."),
 ("JHN.21.15", "mehr als diese", "interpretive", "πλέον τούτων", None, ["mehr als diese (anderen Jünger) mich lieben", "mehr als dies hier (Boot, Netze, Fischfang)"], "τούτων kann männlich («diese [Jünger]») oder sächlich («dies») sein. Am häufigsten wird gelesen: «mehr als die anderen Jünger mich lieben» (vgl. [[MRK.14.29]]). Die Übersetzung lässt die Mehrdeutigkeit stehen."),
 ("JHN.21.15", "Weide meine Lämmer", "literal", "Βόσκε ἀρνία", None, None, "βόσκω «weiden, füttern» ([[JHN.21.17]]) und ποιμαίνω «hüten, als Hirte leiten» ([[JHN.21.16]]); ἀρνία «Lämmer» und πρόβατα «Schafe». Vgl. die Hirtenrede ([[JHN.10.11]]–[[JHN.10.16]]). Ob die Wechsel etwas bedeuten, ist umstritten (siehe oben)."),
 ("JHN.21.17", "zum dritten Mal", "literal", "τὸ τρίτον", None, None, "Die dreifache Frage wird verbreitet als Gegenstück zur dreifachen Verleugnung gelesen ([[JHN.18.17]], [[JHN.18.25]], [[JHN.18.27]]); der Text stellt die Verbindung nicht ausdrücklich her."),
 ("JHN.21.17", "erkennst", "literal", "γινώσκεις", None, ["weisst"], "Zwei Verben des Wissens: οἶδας «du weisst», γινώσκεις «du erkennst»."),
 ("JHN.21.18", "Amen, amen, ich sage dir", "literal", "ἀμὴν ἀμὴν λέγω σοι", None, ["Wahrlich, wahrlich, ich sage dir"], "Grundentscheid (" + GRUND + "): Das doppelte ἀμὴν ἀμήν bleibt als «Amen, amen» stehen; es steht im Johannesevangelium 25-mal (Zählung nach den SBLGNT-Tokens) und leitet ein gewichtiges Wort ein."),
 ("JHN.21.18", "wirst du deine Hände ausstrecken", "interpretive", "ἐκτενεῖς χεῖράς", None, None, "Nach [[JHN.21.19]] deutet das Wort auf den Tod des Petrus. Viele Auslegungen seit der Alten Kirche beziehen das Ausstrecken der Hände und das «Gürten» durch einen anderen auf eine Kreuzigung; der Text sagt das nicht ausdrücklich. Die Überlieferung vom Märtyrertod des Petrus in Rom steht ausserhalb des Neuen Testaments."),
 ("JHN.21.19", "verherrlichen würde", "literal", "δοξάσει", None, ["ehren würde"], "Grundentscheid (" + GRUND + "): δοξάζω durchgehend «verherrlichen». Auch der Tod Jesu ist bei Johannes Verherrlichung ([[JHN.12.23]], [[JHN.13.31]]). Die Wendung «um anzuzeigen, durch was für einen Tod» steht wörtlich gleich für Jesus in [[JHN.12.33]] und [[JHN.18.32]]."),
 ("JHN.21.19", "Folge mir", "literal", "Ἀκολούθει μοι", None, None, "Präsens: «folge mir (weiter)». Vgl. [[JHN.1.43]], [[JHN.13.36]]."),
 ("JHN.21.20", "ausliefert", "literal", "παραδιδούς", None, ["verrät"], "παραδίδωμι heisst «übergeben, ausliefern»; im ganzen Evangelium durchgehend «ausliefern». Die Szene: [[JHN.13.21]]–[[JHN.13.25]]."),
 ("JHN.21.22", "bleibt", "literal", "μένειν", None, ["am Leben bleibt"], "Grundentscheid (" + GRUND + "): μένω durchgehend «bleiben». Hier ist das Am-Leben-Bleiben gemeint; das Wort trägt im Evangelium sonst das Bleiben in Jesus ([[JHN.15.4]]). Ebenso [[JHN.21.23]]."),
 ("JHN.21.22", "bis ich komme", "literal", "ἕως ἔρχομαι", None, None, "Präsens nach ἕως; gemeint ist das Kommen am Ende (vgl. [[JHN.14.3]])."),
 ("JHN.21.23", "verbreitete sich", "adapted", "ἐξῆλθεν", "ging hinaus", None, "Gemeint ist: Das Wort ging unter den Glaubenden um."),
 ("JHN.21.23", "Wort", "literal", "λόγος", None, ["Rede", "Gerücht"], "Grundentscheid (" + GRUND + "): λόγος durchgehend «Wort»; hier im Alltagssinn «Rede, Aussage»."),
 ("JHN.21.23", "den Brüdern", "interpretive", "ἀδελφοὺς", None, ["den Geschwistern", "den Glaubenden"], "Gemeint ist die Gemeinschaft der Glaubenden, Männer und Frauen (vgl. [[JHN.20.17]])."),
 ("JHN.21.24", "geschrieben hat", "interpretive", "γράψας", None, ["hat schreiben lassen"], "γράφω kann auch «schreiben lassen» heissen (vgl. Pilatus in [[JHN.19.19]]). Wer «wir» sind, sagt der Text nicht; die Wir-Form wird oft als Stimme eines Kreises um den Jünger gedeutet (siehe BG-JHN-BOOK-0001)."),
 ("JHN.21.24", "wir wissen", "literal", "οἴδαμεν", None, None, None),
 ("JHN.21.25", "die Welt", "literal", "κόσμον", None, None, "Grundentscheid (" + GRUND + "): κόσμος durchgehend «Welt»; hier im räumlichen Sinn."),
 ("JHN.21.25", "meine ich", "literal", "οἶμαι", None, None, "Der Erzähler spricht hier in der Ich-Form. Die Aussage wird meist als bewusste Übertreibung verstanden, wie sie auch sonst am Schluss antiker Schriften vorkommt."),
]

DEC_GSW = [
 ("JHN.20.1", "erschte Tag vo de Wuche", "literal", "μιᾷ σαββάτων", "erschte vo de Sabbät", None, "σάββατα heisst au «Wuche»."),
 ("JHN.20.2", "gärn ghaa hät", "literal", "ἐφίλει", None, ["gliebt hät"], "Im ganze Evangelium: ἀγαπάω «liebe», φιλέω «gärn haa». Lueg d Entscheidig zu [[JHN.21.15]]."),
 ("JHN.20.5", "Liinebinde", "interpretive", "ὀθόνια", None, ["Liinetüecher"], None),
 ("JHN.20.6", "er gseht", "literal", "θεωρεῖ", None, ["er luegt aa"], "βλέπω und θεωρέω sind i de Mundart beidi «gseh»; s Hochdüütsch underscheidet «sieht» und «schaut»."),
 ("JHN.20.10", "hei", "adapted", "πρὸς αὑτοὺς", "zu sich", None, None),
 ("JHN.20.17", "Heb mich nöd fescht", "interpretive", "Μή μου ἅπτου", "Rüer mich nöd aa", None, "ἅπτομαι heisst «aalänge, sich fescht hebe». S Verbot mit Imperativ Präsens meint oft: «hör uf, mich fescht z hebe». De Thomas söll de Jesus spööter aalänge ([[JHN.20.27]]). Redaktionelle Entscheid."),
 ("JHN.20.17", "Brüedere", "interpretive", "ἀδελφούς", None, ["Gschwüschterti"], "Gmeint sind d Jünger ([[JHN.20.18]])."),
 ("JHN.20.19", "vor de Jude", "interpretive", "Ἰουδαίων", None, ["vor de jüdische Füerer"], "Grundentscheid (" + GRUND + "): οἱ Ἰουδαῖοι wörtlich «d Jude». Da sind wohl di füerende Chreis z Jerusalem gmeint, dänn au d Jünger sind Jude. Kei Urteil über s jüdisch Volk."),
 ("JHN.20.19", "Fride mit eu", "adapted", "Εἰρήνη ὑμῖν", "Fride eu", None, "De üblich Gruess (hebräisch šālôm)."),
 ("JHN.20.21", "gschickt hät", "literal", "ἀπέσταλκέν", None, ["gsandt hät"], "ἀποστέλλω und πέμπω sind beidi «schicke»."),
 ("JHN.20.22", "hät er si aaghuucht", "adapted", "ἐνεφύσησεν", None, None, "S Verb hät keis Objekt; «si» isch ergänzt."),
 ("JHN.20.23", "bhalted", "interpretive", "κρατῆτε", "fescht hebed", None, None),
 ("JHN.20.24", "«Zwilling»", "literal", "Δίδυμος", None, ["Didymus"], "Griechisch für de aramäisch Name Thomas (tᵉʾômāʾ, «Zwilling»)."),
 ("JHN.20.28", "Min Herr und min Gott", "literal", "κύριός θεός", None, None, "A de Jesus grichtet («zu ihm»)."),
 ("JHN.20.29", "Wil du mich gseh häsch, häsch glaubt?", "interpretive", "Ὅτι ἑώρακάς με πεπίστευκας;", None, ["Wil du mich gseh häsch, häsch glaubt."], "De SBLGNT setzt da es Fragezeiche; d Übersetzig folgt em. Als Feschtstellig gläse gaat s au. Redaktionelle Entscheid."),
 ("JHN.20.29", "Sälig", "traditional", "μακάριοι", None, ["Glücklich"], None),
 ("JHN.20.30", "Zeiche", "literal", "σημεῖα", None, ["Wunder"], "Grundentscheid (" + GRUND + "): σημεῖον durchgehend «Zeiche», nöd «Wunder»."),
 ("JHN.20.31", "demit ir glaubed", "interpretive", "πιστεύητε", None, ["demit ir zum Glaube chömed", "demit ir im Glaube bliibed"], "Läsart: De SBLGNT (mit WH) hät πιστεύητε (Präsens, eher «wiiter glaube»), Treg, NA28 und RP händ πιστεύσητε (Aorist, eher «zum Glaube choo»); lueg d Alternative. D Ziitform allei entscheidet nöd, für wen s Buech gschribe isch ([[JHN.11.15]], [[JHN.13.19]]). «demit ir glaubed» laat beides offe."),
 ("JHN.21.5", "Chind", "adapted", "Παιδία", None, ["Manne"], "Vertrauti Aared."),
 ("JHN.21.7", "blutt", "interpretive", "γυμνός", None, ["nu liecht aagleit"], None),
 ("JHN.21.9", "es Cholefüür", "literal", "ἀνθρακιὰν", None, ["es Gluetfüür"], "S gliich Wort staat bim Füür, wo de Petrus de Jesus verleugnet hät ([[JHN.18.18]]); drum a beide Stelle «Cholefüür». Öb de Aaklang gwollt isch, isch e Düütig."),
 ("JHN.21.11", "hundertdrüüefüfzg", "literal", "ἑκατὸν πεντήκοντα τριῶν", None, None, "D Zaal isch sit de Alte Chile vilfach düütet worde; de Text sälber git kei Düütig."),
 ("JHN.21.15", "Sohn vom Johannes", "adapted", "Ἰωάννου", "vom Johannes", None, "Wie [[JHN.1.42]]."),
 ("JHN.21.15", "gärn han", "interpretive", "ἀγαπᾷς φιλῶ", None, ["liebe"], "De Jesus fröget zweimal mit ἀγαπάω («liebsch mich»), de Petrus antwortet mit φιλέω («ich han dich gärn»); s dritt Mal fröget de Jesus sälber mit φιλέω. D Übersetzig underscheidet d Wörter wie im ganze Evangelium. «Gärn haa» cha i de Mundart schwächer tööne als «liebe»; das isch kei Entscheid für e Abstufig. Düütig A: De Wächsel bedüütet öppis (de Petrus wagt nach de Verleugnig nu s bescheideneri Wort). Gägeargument, Düütig B: De Johannes bruucht beidi Verbe ohni erkennbare Underschid ([[JHN.3.35]] / [[JHN.5.20]]; [[JHN.13.23]] / [[JHN.20.2]]), und [[JHN.21.17]] begründet d Truur mit em «dritte Mal»."),
 ("JHN.21.15", "meh als die", "interpretive", "πλέον τούτων", None, ["meh als di andere Jünger mich liebed", "meh als das da"], "τούτων cha «die (Jünger)» oder «das (da)» heisse."),
 ("JHN.21.18", "Amen, amen, ich säge dir", "literal", "ἀμὴν ἀμὴν λέγω σοι", None, None, "Grundentscheid (" + GRUND + "): s doppelt Amen bliibt staa."),
 ("JHN.21.19", "würd verherrliche", "literal", "δοξάσει", None, ["würd ehre"], "Grundentscheid (" + GRUND + "): δοξάζω durchgehend «verherrliche»."),
 ("JHN.21.22", "bliibt", "literal", "μένειν", None, ["am Läbe bliibt"], "Grundentscheid (" + GRUND + "): μένω durchgehend «bliibe»."),
 ("JHN.21.23", "verbreitet", "adapted", "ἐξῆλθεν", "isch usegange", None, None),
 ("JHN.21.24", "gschribe hät", "interpretive", "γράψας", None, ["hät la schriibe"], "Wer «mer» isch, seit de Text nöd."),
 ("JHN.21.25", "d Wält", "literal", "κόσμον", None, None, "Grundentscheid (" + GRUND + "): κόσμος durchgehend «Wält»."),
]

AUTO = "Laut der automatischen Zuordnung"
AUTO_G = "Nach de automatische Zueornig"
# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-JHN-020-016-03:R2", "JHN.20.16", "zu ihm auf Hebräisch", "zu ihm", "zu ihm uf Hebräisch", "zu ihm", "gering",
  "Ohne die Angabe der Sprache.", "Ohni d Aagab vo de Spraach.",
  {"R1": [("Ἑβραϊστί", "auf Hebräisch", "WH, Treg, NA28")], "R2": [("–", "(fehlt)", "RP")]},
  {"R1": [("Ἑβραϊστί", "uf Hebräisch", "WH, Treg, NA28")], "R2": [("–", "(fäält)", "RP")]},
  ["Die Angabe kann zur Erklärung ergänzt oder als überflüssig weggelassen worden sein.",
   AUTO + " lesen 01, 03, 05, 032, 𝔓5 und 𝔓66 mit Ἑβραϊστί, 02 ohne; 04 ist hier nicht erhalten."],
  ["D Aagab cha zur Erkläärig ergänzt oder als überflüssig wäggloo worde sii.",
   AUTO_G + " läsed 01, 03, 05, 032, 𝔓5 und 𝔓66 mit Ἑβραϊστί, 02 ohni; 04 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-JHN-020-017-02:R2", "JHN.20.17", "zum Vater hinaufgestiegen", "zu meinem Vater hinaufgestiegen", "zum Vatter ufegstige", "zu mim Vatter ufegstige", "gering",
  "Mit «mein» wie später im Vers.", "Mit «mim» wie spööter im Vers.",
  {"R1": [("πατέρα", "Vater", "WH, Treg, NA28")], "R2": [("πατέρα μου", "meinem Vater", "RP")]},
  {"R1": [("πατέρα", "Vatter", "WH, Treg, NA28")], "R2": [("πατέρα μου", "mim Vatter", "RP")]},
  ["«mein» kann an «zu meinem Vater» im selben Vers angeglichen sein.",
   AUTO + " lesen 01 und 03 ohne μου, 05 mit; 02 und 𝔓66 haben im erfassten Wortlaut ebenfalls πατέρα μου, werden aber wegen weiterer Abweichungen keiner Lesart zugeordnet; 032 hat im erfassten Wortlaut kein μου (ebenfalls nicht zugeordnet); 04 ist hier nicht erhalten."],
  ["«mim» cha as «zu mim Vatter» im gliiche Vers aaglichen sii.",
   AUTO_G + " läsed 01 und 03 ohni μου, 05 mit; 02 und 𝔓66 händ im erfasste Wortlut au πατέρα μου (nöd zuegordnet), 032 ohni; 04 isch nöd erhalte."]),
 ("VAR-SBLGNTAPP-JHN-020-018-03:R2", "JHN.20.18", "«Ich habe den Herrn gesehen»", "sie habe den Herrn gesehen", "«Ich han de Herr gseh»", "si heig de Herr gseh", "gering",
  "Indirekte statt direkter Rede (ἑώρακεν «sie hat gesehen»).", "Indiräkti statt diräkti Red (ἑώρακεν «si hät gseh»).",
  {"R1": [("Ἑώρακα", "ich habe gesehen", "WH, Treg, NA28")], "R2": [("ἑώρακεν", "sie hat gesehen", "RP")]},
  {"R1": [("Ἑώρακα", "ich han gseh", "WH, Treg, NA28")], "R2": [("ἑώρακεν", "si hät gseh", "RP")]},
  ["Die indirekte Rede passt glatter zur Fortsetzung «und dass er ihr dies gesagt habe»; die direkte Rede ist der schwierigere Satzbau.",
   AUTO + " lesen 01, 03, 032 und 𝔓66 Ἑώρακα, 02 und 05 ἑώρακεν; 04 und 𝔓5 sind hier nicht erhalten."],
  ["Di indiräkt Red passt glätter zur Fortsetzig.",
   AUTO_G + " läsed 01, 03, 032 und 𝔓66 Ἑώρακα, 02 und 05 ἑώρακεν."]),
 ("VAR-SBLGNTAPP-JHN-020-019-02:R2", "JHN.20.19", "wo die Jünger waren", "wo die Jünger versammelt waren", "wo d Jünger gsii sind", "wo d Jünger versammlet gsii sind", "gering",
  "Mit συνηγμένοι «versammelt».", "Mit συνηγμένοι «versammlet».",
  {"R1": [("μαθηταὶ", "Jünger", "WH, Treg, NA28")], "R2": [("μαθηταὶ συνηγμένοι", "Jünger versammelt", "RP")]},
  {"R1": [("μαθηταὶ", "Jünger", "WH, Treg, NA28")], "R2": [("μαθηταὶ συνηγμένοι", "Jünger versammlet", "RP")]},
  ["Das Wort kann verdeutlichend ergänzt sein (vgl. [[MAT.18.20]]); ein Ausfall beim Abschreiben ist ebenfalls denkbar.",
   AUTO + " lesen 01 (Erstschrift), 02, 03, 05 und 032 ohne, die Korrektur in 01 und 𝔓66 mit συνηγμένοι; 04 ist hier nicht erhalten."],
  ["S Wort cha zur Verdüütlichig ergänzt sii; en Usfall bim Abschriibe isch au dänkbar.",
   AUTO_G + " läsed 01 (Erschtschrift), 02, 03, 05 und 032 ohni, d Korrektur in 01 und 𝔓66 mit συνηγμένοι."]),
 ("VAR-SBLGNTAPP-JHN-020-023-01:R2", "JHN.20.23", "dem sind sie vergeben", "dem werden sie vergeben", "däm sind si vergää", "däm wärded si vergää", "gering",
  "Präsens ἀφίενται statt Perfekt ἀφέωνται.", "Präsens ἀφίενται statt Perfekt ἀφέωνται.",
  {"R1": [("ἀφέωνται", "sind vergeben", "WH, Treg, NA28")], "R2": [("ἀφίενται", "werden vergeben", "RP")]},
  {"R1": [("ἀφέωνται", "sind vergää", "WH, Treg, NA28")], "R2": [("ἀφίενται", "wärded vergää", "RP")]},
  ["Die Formen sind sich ähnlich; das Perfekt betont den Zustand («sind vergeben»), das Präsens den Vorgang.",
   AUTO + " lesen 02, 05, 𝔓5 und 𝔓66 ἀφέωνται, 032 ἀφίενται; 03 (ἀφειονται) liess sich nicht eindeutig zuordnen; 01 hat im erfassten Wortlaut die Zukunftsform ἀφεθήσεται («wird vergeben werden»); 04 ist hier nicht erhalten."],
  ["D Forme sind sich ähnlich; s Perfekt betont de Zuestand, s Präsens de Vorgang.",
   AUTO_G + " läsed 02, 05, 𝔓5 und 𝔓66 ἀφέωνται, 032 ἀφίενται; 03 isch nöd eidüütig, 01 hät d Zuekunftsform ἀφεθήσεται."]),
 ("VAR-SBLGNTAPP-JHN-020-030-01:R2", "JHN.20.30", "vor den Jüngern", "vor seinen Jüngern", "vor de Jünger", "vor sine Jünger", "gering",
  "Mit αὐτοῦ «seinen».", "Mit αὐτοῦ «sine».",
  {"R1": [("μαθητῶν", "Jüngern", "WH, Treg")], "R2": [("μαθητῶν αὐτοῦ", "seinen Jüngern", "NA28, RP")]},
  {"R1": [("μαθητῶν", "Jünger", "WH, Treg")], "R2": [("μαθητῶν αὐτοῦ", "sine Jünger", "NA28, RP")]},
  ["Das Fürwort kann ergänzt oder ausgefallen sein; der Sinn bleibt gleich.",
   AUTO + " lesen 02 und 03 ohne, 01, 04, 05, 032 und 𝔓66 mit αὐτοῦ."],
  ["S Fürwort cha ergänzt oder usgfalle sii; de Sinn bliibt gliich.",
   AUTO_G + " läsed 02 und 03 ohni, 01, 04, 05, 032 und 𝔓66 mit αὐτοῦ."]),
 ("VAR-SBLGNTAPP-JHN-020-031-01:R2", "JHN.20.31", "damit ihr glaubt", "damit ihr zum Glauben kommt", "demit ir glaubed", "demit ir zum Glaube chömed", "mittel",
  "Aorist πιστεύσητε statt Präsens πιστεύητε. Der Aorist kann das Zum-Glauben-Kommen betonen, das Präsens das Im-Glauben-Bleiben; daraus wird oft auf die Leserschaft geschlossen (Werbung oder Stärkung). Die Zeitform allein entscheidet das nicht (siehe Entscheidung).",
  "Aorist πιστεύσητε statt Präsens πιστεύητε. De Aorist cha s Zum-Glaube-Choo betone, s Präsens s Im-Glaube-Bliibe; d Ziitform allei entscheidet aber nöd, für wen s Buech gschribe isch.",
  {"R1": [("πιστεύητε", "ihr glaubt (weiter)", "SBLGNT, WH")], "R2": [("πιστεύσητε", "ihr kommt zum Glauben", "Treg, NA28, RP")]},
  {"R1": [("πιστεύητε", "ir glaubed (wiiter)", "SBLGNT, WH")], "R2": [("πιστεύσητε", "ir chömed zum Glaube", "Treg, NA28, RP")]},
  ["Die beiden Formen unterscheiden sich nur durch ein σ und können beim Abschreiben leicht verwechselt werden; dieselbe Schwankung zeigt der SBLGNT-Apparat auch in [[JHN.19.35]].",
   AUTO + " lesen 01, 03 und 𝔓66 (dort beschädigt) πιστεύητε, 02, 04, 05 und 032 πιστεύσητε (032 in der Schreibung πιστευσηται)."],
  ["Di beide Forme underscheided sich nu dur es σ und chönd bim Abschriibe liecht verwächslet wärde.",
   AUTO_G + " läsed 01, 03 und 𝔓66 (beschädigt) πιστεύητε, 02, 04, 05 und 032 πιστεύσητε."]),
 ("VAR-SBLGNTAPP-JHN-021-003-01:R2", "JHN.21.3", "stiegen in das Boot", "stiegen sogleich in das Boot", "is Boot gstige", "grad is Boot gstige", "gering",
  "Mit εὐθύς «sogleich».", "Mit εὐθύς «grad».",
  {"R1": [("πλοῖον", "Boot", "WH, Treg, NA28")], "R2": [("πλοῖον εὐθύς", "Boot sogleich", "RP")]},
  {"R1": [("πλοῖον", "Boot", "WH, Treg, NA28")], "R2": [("πλοῖον εὐθύς", "Boot grad", "RP")]},
  ["«sogleich» kann die Erzählung beleben; Markus gebraucht das Wort oft.",
   AUTO + " haben unter den Handschriften nur 02 εὐθύς; 01, 03, 04, 05, 032 und 𝔓66 lesen ohne."],
  ["«grad» cha d Erzellig belebe.",
   AUTO_G + " hät under de Handschrifte nu 02 εὐθύς; 01, 03, 04, 05, 032 und 𝔓66 läsed ohni."]),
 ("VAR-SBLGNTAPP-JHN-021-014-02:R2", "JHN.21.14", "den Jüngern offenbarte", "seinen Jüngern offenbarte", "de Jünger offebaret hät", "sine Jünger offebaret hät", "gering",
  "Mit αὐτοῦ «seinen».", "Mit αὐτοῦ «sine».",
  {"R1": [("μαθηταῖς", "Jüngern", "WH, Treg, NA28")], "R2": [("μαθηταῖς αὐτοῦ", "seinen Jüngern", "RP")]},
  {"R1": [("μαθηταῖς", "Jünger", "WH, Treg, NA28")], "R2": [("μαθηταῖς αὐτοῦ", "sine Jünger", "RP")]},
  ["Das Fürwort kann ergänzt sein; der Sinn bleibt gleich.",
   AUTO + " lesen 01, 02, 03, 04 und 032 ohne, 05 mit αὐτοῦ."],
  ["S Fürwort cha ergänzt sii; de Sinn bliibt gliich.",
   AUTO_G + " läsed 01, 02, 03, 04 und 032 ohni, 05 mit αὐτοῦ."]),
 ("VAR-SBLGNTAPP-JHN-021-015-01:R2", "JHN.21.15", "Simon, Sohn des Johannes", "Simon, Sohn des Jona", "Simon, Sohn vom Johannes", "Simon, Sohn vom Jona", "gering",
  "Ἰωνᾶ statt Ἰωάννου; ebenso in [[JHN.21.16]] und [[JHN.21.17]].", "Ἰωνᾶ statt Ἰωάννου; gliich i [[JHN.21.16]] und [[JHN.21.17]].",
  {"R1": [("Ἰωάννου", "des Johannes", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ", "des Jona", "RP")]},
  {"R1": [("Ἰωάννου", "vom Johannes", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ", "vom Jona", "RP")]},
  ["«Sohn des Jona» kann an [[MAT.16.17]] (Βαριωνᾶ) angeglichen sein.",
   AUTO + " lesen 03, 04, 05 und 032 Ἰωάννου, 02 Ἰωνᾶ; in 01 hat die Erstschrift nur «Simon» ohne Vatersnamen, die Korrektur Ἰωάννου."],
  ["«Sohn vom Jona» cha a [[MAT.16.17]] aaglichen sii.",
   AUTO_G + " läsed 03, 04, 05 und 032 Ἰωάννου, 02 Ἰωνᾶ; in 01 hät d Erschtschrift nu «Simon», d Korrektur Ἰωάννου."]),
 ("VAR-SBLGNTAPP-JHN-021-016-01:R2", "JHN.21.16", "Simon, Sohn des Johannes", "Simon, Sohn des Jona", "Simon, Sohn vom Johannes", "Simon, Sohn vom Jona", "gering",
  "Wie in [[JHN.21.15]].", "Wie i [[JHN.21.15]].",
  {"R1": [("Ἰωάννου", "des Johannes", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ", "des Jona", "RP")]},
  {"R1": [("Ἰωάννου", "vom Johannes", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ", "vom Jona", "RP")]},
  ["Wie in [[JHN.21.15]].", AUTO + " lesen 01, 03, 04, 05 und 032 Ἰωάννου, 02 Ἰωνᾶ."],
  ["Wie i [[JHN.21.15]].", AUTO_G + " läsed 01, 03, 04, 05 und 032 Ἰωάννου, 02 Ἰωνᾶ."]),
 ("VAR-SBLGNTAPP-JHN-021-017-01:R2", "JHN.21.17", "Simon, Sohn des Johannes", "Simon, Sohn des Jona", "Simon, Sohn vom Johannes", "Simon, Sohn vom Jona", "gering",
  "Wie in [[JHN.21.15]].", "Wie i [[JHN.21.15]].",
  {"R1": [("Ἰωάννου", "des Johannes", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ", "des Jona", "RP")]},
  {"R1": [("Ἰωάννου", "vom Johannes", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ", "vom Jona", "RP")]},
  ["Wie in [[JHN.21.15]].", AUTO + " lesen 01, 03, 04, 05 und 032 Ἰωάννου, 02 Ἰωνᾶ."],
  ["Wie i [[JHN.21.15]].", AUTO_G + " läsed 01, 03, 04, 05 und 032 Ἰωάννου, 02 Ἰωνᾶ."]),
 ("VAR-SBLGNTAPP-JHN-021-017-05:R2", "JHN.21.17", "Weide meine Schafe", "Weide meine Schäflein", "Weid mini Schaf", "Weid mini Schäfli", "gering",
  "Verkleinerungsform προβάτια «Schäflein».", "Verchliinerigsform προβάτια «Schäfli».",
  {"R1": [("πρόβατά", "Schafe", "WH, NA28, RP")], "R2": [("προβάτιά", "Schäflein", "Treg")]},
  {"R1": [("πρόβατά", "Schaf", "WH, NA28, RP")], "R2": [("προβάτιά", "Schäfli", "Treg")]},
  ["Die seltene Verkleinerungsform kann durch das geläufige πρόβατα ([[JHN.21.16]]) ersetzt worden sein, oder umgekehrt an ἀρνία ([[JHN.21.15]]) angeglichen.",
   AUTO + " lesen 02, 03 und 04 sowie die Korrektur in 032 προβάτια, 01, 05 und die Erstschrift von 032 πρόβατα."],
  ["Di sälte Verchliinerigsform cha dur s gläufig πρόβατα ersetzt worde sii, oder umgekehrt.",
   AUTO_G + " läsed 02, 03 und 04 und d Korrektur in 032 προβάτια, 01, 05 und d Erschtschrift vo 032 πρόβατα."]),
 ("VAR-SBLGNTAPP-JHN-021-025-03:R2", "JHN.21.25", "die dann geschrieben würden.", "die dann geschrieben würden. Amen.", "wo dänn gschribe würded.", "wo dänn gschribe würded. Amen.", "gering",
  "Mit abschliessendem «Amen».", "Mit eme «Amen» am Schluss.",
  {"R1": [("βιβλία", "Bücher", "WH, Treg, NA28")], "R2": [("βιβλία Ἀμήν", "Bücher. Amen", "RP")]},
  {"R1": [("βιβλία", "Büecher", "WH, Treg, NA28")], "R2": [("βιβλία Ἀμήν", "Büecher. Amen", "RP")]},
  ["Ein «Amen» am Buchschluss entspricht dem Gebrauch beim gottesdienstlichen Lesen und kann so in den Text gelangt sein.",
   AUTO + " lesen alle erfassten Handschriften (01 in der Korrektur, 02, 03, 04, 05, 032) ohne «Amen» (𝔓109 lässt sich keiner Lesart zuordnen); den Zusatz haben unter den erfassten Texten die gedruckten Ausgaben KJTR, RP und Stephanus. In der CNTR-Transkription von 01 steht [[JHN.21.25]] nur als Korrektur; die Erstschrift hat für den Vers keinen Text."],
  ["Es «Amen» am Schluss vom Buech entspricht em Bruuch bim Vorläse im Gottesdienscht.",
   AUTO_G + " läsed alli erfasste Handschrifte ohni «Amen»; de Zuesatz händ di druckte Usgabe KJTR, RP und Stephanus. I de CNTR-Transkription vo 01 staat [[JHN.21.25]] nu als Korrektur."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-020-001-031", "JHN.20.1-JHN.20.31", "section", "Das leere Grab und die Erscheinungen des Auferstandenen",
  ["TU-JHN-020-001-010", "TU-JHN-020-011-018", "TU-JHN-020-019-023", "TU-JHN-020-024-029", "TU-JHN-020-030-031"],
  "Am ersten Tag der Woche findet Maria aus Magdala den Stein vom Grab weggenommen. Petrus und der andere Jünger laufen hin und finden die Leinenbinden und das Schweisstuch; der andere Jünger sieht und glaubt. Jesus begegnet Maria, die ihn zuerst für den Gärtner hält, und sendet sie mit einer Botschaft zu seinen Brüdern. Am Abend tritt er bei verschlossenen Türen zu den Jüngern, zeigt ihnen Hände und Seite, sendet sie, haucht sie an und sagt: «Empfangt heiligen Geist!» Wem sie die Sünden vergeben, dem sind sie vergeben; wem sie sie behalten, dem sind sie behalten. Thomas will nur glauben, wenn er die Wunden sieht und berührt; acht Tage später fordert Jesus ihn dazu auf, und Thomas bekennt: «Mein Herr und mein Gott!» Ein Schlusswort sagt, wozu die Zeichen aufgeschrieben sind: damit die Lesenden glauben, dass Jesus der Christus, der Sohn Gottes, ist, und Leben haben in seinem Namen.",
  SEG + " [[JHN.20.30]]–[[JHN.20.31]] wird oft als erster Schluss des Evangeliums verstanden (siehe BG-JHN-BOOK-0001)."),
 ("TU-JHN-020-001-010", "JHN.20.1-JHN.20.10", "narrative", "Das leere Grab", None,
  "Maria aus Magdala sieht frühmorgens den Stein vom Grab weggenommen und meldet Simon Petrus und dem anderen Jünger, man habe den Herrn weggenommen. Die beiden laufen zum Grab; der andere Jünger kommt zuerst an, Petrus geht als Erster hinein. Sie sehen die Leinenbinden und das zusammengewickelte Schweisstuch; der andere Jünger sieht und glaubt; denn, so der Erzähler, sie kannten die Schrift noch nicht, dass er von den Toten auferstehen müsse. Dann gehen sie nach Hause.", None),
 ("TU-JHN-020-011-018", "JHN.20.11-JHN.20.18", "narrative", "Jesus begegnet Maria aus Magdala", None,
  "Maria steht weinend am Grab und sieht zwei Engel, die sie fragen, warum sie weint. Dann steht Jesus da; sie hält ihn für den Gärtner, bis er sie mit Namen anspricht und sie ihn «Rabbuni» nennt. Jesus sagt, sie solle ihn nicht festhalten, und sendet sie zu seinen Brüdern mit der Botschaft, dass er zu seinem und ihrem Vater, seinem und ihrem Gott hinaufsteigt. Maria verkündet den Jüngern: «Ich habe den Herrn gesehen.»", None),
 ("TU-JHN-020-019-023", "JHN.20.19-JHN.20.23", "narrative", "Jesus sendet die Jünger", None,
  "Am Abend desselben Tages sind die Jünger aus Furcht vor den Juden hinter verschlossenen Türen. Jesus tritt in ihre Mitte, grüsst sie mit «Friede euch» und zeigt ihnen Hände und Seite; sie freuen sich. Er sendet sie, wie der Vater ihn gesandt hat, haucht sie an und sagt: «Empfangt heiligen Geist!» Wem sie die Sünden vergeben, dem sind sie vergeben; wem sie sie behalten, dem sind sie behalten.", None),
 ("TU-JHN-020-024-029", "JHN.20.24-JHN.20.29", "narrative", "Thomas", None,
  "Thomas war nicht dabei und will nur glauben, wenn er die Male der Nägel sieht und seine Hand in Jesu Seite legt. Acht Tage später kommt Jesus wieder bei verschlossenen Türen, fordert Thomas auf, Finger und Hand herzureichen, und sagt ihm, er solle nicht ungläubig, sondern gläubig sein. Thomas antwortet: «Mein Herr und mein Gott!» Jesus fragt, ob er geglaubt habe, weil er ihn gesehen hat, und preist die selig, die nicht gesehen und doch geglaubt haben.", None),
 ("TU-JHN-020-030-031", "JHN.20.30-JHN.20.31", "narrative", "Wozu dieses Buch geschrieben ist", None,
  "Jesus hat vor den Jüngern noch viele andere Zeichen getan, die nicht in diesem Buch stehen. Diese aber sind aufgeschrieben, damit die Lesenden glauben, dass Jesus der Christus, der Sohn Gottes, ist, und als Glaubende Leben haben in seinem Namen.", None),
 ("TU-JHN-021-001-025", "JHN.21.1-JHN.21.25", "section", "Am See von Tiberias: Fischfang, Mahl, Petrus und der Jünger, den Jesus liebte",
  ["TU-JHN-021-001-014", "TU-JHN-021-015-019", "TU-JHN-021-020-023", "TU-JHN-021-024-025"],
  "Sieben Jünger fischen eine Nacht lang ohne Erfolg. Am Morgen steht Jesus unerkannt am Ufer; auf sein Wort werfen sie das Netz rechts aus und können es wegen der vielen Fische nicht mehr einziehen. Der Jünger, den Jesus liebte, erkennt den Herrn, und Petrus wirft sich in den See. Am Ufer gibt Jesus ihnen Brot und Fisch; es ist das dritte Mal, dass er sich den Jüngern nach der Auferweckung offenbart. Dreimal fragt er Petrus, ob er ihn liebe (beim dritten Mal: ob er ihn lieb habe), und beauftragt ihn, seine Lämmer und Schafe zu weiden und zu hüten. Er kündigt ihm an, dass im Alter ein anderer ihn gürten und bringen wird, wohin er nicht will – nach dem Erzähler ein Hinweis auf den Tod, durch den Petrus Gott verherrlichen wird –, und sagt: «Folge mir!» Auf die Frage nach dem Jünger, den Jesus liebte, antwortet Jesus: Wenn er wolle, dass jener bleibe, bis er komme, gehe das Petrus nichts an. Das Gerücht, jener Jünger sterbe nicht, wird richtiggestellt. Der Schluss nennt diesen Jünger als Zeugen und Schreiber und sagt, Jesus habe noch so vieles getan, dass nach Meinung des Erzählers die Welt die Bücher nicht fassen könnte.",
  SEG + " Kapitel 21 wird in der Forschung oft als Nachtrag nach dem ersten Schluss [[JHN.20.30]]–[[JHN.20.31]] betrachtet, von anderen als ursprünglicher Teil des Werks (siehe BG-JHN-BOOK-0001). In den erfassten CNTR-Transkriptionen von 01, 02, 03, 04, 05 und 032 steht das Kapitel; in 01 ist [[JHN.21.25]] nur als Korrektur erfasst."),
 ("TU-JHN-021-001-014", "JHN.21.1-JHN.21.14", "narrative", "Der Fischfang und das Mahl am See", None,
  "Simon Petrus, Thomas, Natanaël, die Söhne des Zebedäus und zwei weitere Jünger fangen eine Nacht lang nichts. Am Morgen steht Jesus am Ufer, ohne dass sie ihn erkennen, und sagt ihnen, sie sollen das Netz auf der rechten Seite auswerfen; nun können sie es wegen der Menge der Fische nicht mehr einziehen. Der Jünger, den Jesus liebte, sagt: «Es ist der Herr!», und Petrus wirft sich in den See. An Land finden sie ein Kohlenfeuer mit Fisch und Brot; auf Jesu Aufforderung, von den Fischen zu bringen, zieht Petrus das Netz mit 153 grossen Fischen an Land, und es zerreisst nicht. Jesus lädt sie zum Essen ein und gibt ihnen Brot und Fisch. Es ist das dritte Mal, dass er sich den Jüngern nach der Auferweckung offenbart.", None),
 ("TU-JHN-021-015-019", "JHN.21.15-JHN.21.19", "narrative", "Jesus und Petrus: «Weide meine Schafe»", None,
  "Nach dem Essen fragt Jesus Petrus dreimal, ob er ihn liebe (beim dritten Mal: ob er ihn lieb habe); Petrus antwortet jedes Mal, Jesus wisse, dass er ihn lieb habe, und wird beim dritten Mal traurig. Jesus beauftragt ihn, seine Lämmer zu weiden und seine Schafe zu hüten und zu weiden. Dann kündigt er ihm an, dass im Alter ein anderer ihn gürten und bringen wird, wohin er nicht will; der Erzähler deutet das auf den Tod, durch den Petrus Gott verherrlichen wird. Jesus sagt zu ihm: «Folge mir!»", None),
 ("TU-JHN-021-020-023", "JHN.21.20-JHN.21.23", "narrative", "Der Jünger, den Jesus liebte", None,
  "Petrus sieht den Jünger, den Jesus liebte, folgen und fragt, was mit ihm werde. Jesus antwortet: Wenn er wolle, dass jener bleibe, bis er komme, was gehe es Petrus an; er solle ihm folgen. Daraus entsteht unter den Brüdern das Wort, jener Jünger sterbe nicht; der Erzähler stellt richtig, dass Jesus das nicht gesagt hat.", None),
 ("TU-JHN-021-024-025", "JHN.21.24-JHN.21.25", "narrative", "Das Zeugnis des Jüngers und der Schluss", None,
  "Dieser Jünger ist es, der von diesen Dingen Zeugnis ablegt und dies geschrieben hat; «wir» wissen, dass sein Zeugnis wahr ist. Jesus hat noch vieles andere getan; würde alles einzeln aufgeschrieben, könnte nach Meinung des Erzählers die Welt die Bücher nicht fassen.", None),
]
UNITS_GSW = {
 "TU-JHN-020-001-031": ("S läär Grab und de Uferstande erschiint", "Am erschte Tag vo de Wuche findt d Maria vo Magdala de Stei vom Grab wäggnoo. De Petrus und de ander Jünger ränned hii und finded d Liinebinde und s Schweisstuech; de ander Jünger gseht und glaubt. De Jesus begägnet de Maria, wo en zerscht für de Gärtner hebt, und schickt si mit ere Botschaft zu sine Brüedere. Am Aabig staat er bi bschlossne Tüüre bi de Jünger, zeigt ine d Händ und d Siite, schickt si, huucht si aa und seit: «Nämed heilige Geischt!» Wem si d Sünde vergäbed, däm sind si vergää; wem si si bhalted, däm sind si bhalte. De Thomas wott nu glaube, wänn er d Wunde gseht und aalängt; acht Täg spööter forderet en de Jesus dezue uf, und de Thomas bekännt: «Min Herr und min Gott!» Es Schlusswort seit, für was d Zeiche ufgschribe sind: demit d Läser glaubed, dass de Jesus de Christus, de Sohn vo Gott, isch, und Läbe händ in sim Name."),
 "TU-JHN-020-001-010": ("S läär Grab", "D Maria vo Magdala gseht am früene Morge de Stei vom Grab wäggnoo und seit em Simon Petrus und em andere Jünger, mer heig de Herr wäggnoo. Di zwei ränned zum Grab; de ander Jünger isch zerscht dört, de Petrus gaat als Erschte ine. Si gsehnd d Liinebinde und s zämegwicklet Schweisstuech; de ander Jünger gseht und glaubt; dänn, seit de Erzäller, si händ d Schrift no nöd kännt, dass er vo de Tote mües uferstaa. Dänn gönd si hei."),
 "TU-JHN-020-011-018": ("De Jesus begägnet de Maria vo Magdala", "D Maria staat am Grab und briegget und gseht zwei Ängel, wo si fröged, werum si briegget. Dänn staat de Jesus da; si hebt en für de Gärtner, bis er si mit em Name aaredt und si en «Rabbuni» nännt. De Jesus seit, si söll en nöd fescht hebe, und schickt si zu sine Brüedere mit de Botschaft, dass er zu sim und irem Vatter, zu sim und irem Gott ufestiigt. D Maria verchündet de Jünger: «Ich han de Herr gseh.»"),
 "TU-JHN-020-019-023": ("De Jesus schickt d Jünger", "Am Aabig vom gliiche Tag sind d Jünger us Angscht vor de Jude hinder bschlossne Tüüre. De Jesus staat i iri Mitti, grüesst si mit «Fride mit eu» und zeigt ine d Händ und d Siite; si fröied sich. Er schickt si, wie de Vatter en gschickt hät, huucht si aa und seit: «Nämed heilige Geischt!» Wem si d Sünde vergäbed, däm sind si vergää; wem si si bhalted, däm sind si bhalte."),
 "TU-JHN-020-024-029": ("De Thomas", "De Thomas isch nöd debii gsii und wott nu glaube, wänn er d Mal vo de Nägel gseht und sini Hand i d Siite vom Jesus leit. Acht Täg spööter chunnt de Jesus wider bi bschlossne Tüüre, seit em Thomas, er söll de Finger und d Hand herstrecke, und er söll nöd ungläubig, sondern gläubig sii. De Thomas antwortet: «Min Herr und min Gott!» De Jesus fröget, öb er glaubt heig, wil er en gseh hät, und nännt die sälig, wo nöd gseh und trotzdem glaubt händ."),
 "TU-JHN-020-030-031": ("Für was das Buech gschribe isch", "De Jesus hät vor de Jünger no vili anderi Zeiche gmacht, wo nöd i däm Buech stönd. Die aber sind ufgschribe, demit d Läser glaubed, dass de Jesus de Christus, de Sohn vo Gott, isch, und als Gläubigi Läbe händ in sim Name."),
 "TU-JHN-021-001-025": ("Am See vo Tiberias: Fischfang, Ässe, de Petrus und de Jünger, wo de Jesus gliebt hät", "Sibe Jünger fisched e Nacht lang ohni Erfolg. Am Morge staat de Jesus am Ufer, aber si erchänned en nöd; uf sis Wort rüered si s Netz rächts us und chönd s wäge de vile Fisch nüme iizie. De Jünger, wo de Jesus gliebt hät, erchännt de Herr, und de Petrus stürzt sich in See. Am Ufer git ine de Jesus Broot und Fisch; es isch s dritt Mal, dass er sich de Jünger nach de Uferweckig offebaret. Drüümal fröget er de Petrus, öb er en liebi (s dritt Mal: öb er en gärn heig), und git em de Uftrag, sini Lämmli und Schaf z weide und z hüete. Er seit em aa, dass en im Alter en andere wird gürte und bringe, wo er nöd wott – nach em Erzäller en Hiiwiis uf de Tod, mit däm de Petrus Gott wird verherrliche –, und seit: «Chumm mir nache!» Uf d Frag nach em Jünger, wo de Jesus gliebt hät, antwortet de Jesus: Wänn er well, dass dä bliibi, bis er chömi, gang das de Petrus nüüt aa. S Grücht, dä Jünger stärbi nöd, wird richtiggstellt. De Schluss nännt dä Jünger als Züüge und Schriiber und seit, de Jesus heig no so vil gmacht, dass nach de Meinig vom Erzäller d Wält d Büecher nöd chönnt fasse."),
 "TU-JHN-021-001-014": ("De Fischfang und s Ässe am See", "De Simon Petrus, de Thomas, de Natanaël, d Söön vom Zebedäus und zwei wiiteri Jünger fanged e Nacht lang nüüt. Am Morge staat de Jesus am Ufer, ohni dass si en erchänned, und seit ine, si söled s Netz uf de rächte Siite usrüere; jetzt chönd si s wäge de vile Fisch nüme iizie. De Jünger, wo de Jesus gliebt hät, seit: «Es isch de Herr!», und de Petrus stürzt sich in See. A Land finded si es Cholefüür mit Fisch und Broot; wo de Jesus seit, si söled vo de Fisch bringe, zieht de Petrus s Netz mit 153 grosse Fisch a Land, und es verriisst nöd. De Jesus ladet si zum Ässe ii und git ine Broot und Fisch. Es isch s dritt Mal, dass er sich de Jünger nach de Uferweckig offebaret."),
 "TU-JHN-021-015-019": ("De Jesus und de Petrus: «Weid mini Schaf»", "Nach em Ässe fröget de Jesus de Petrus drüümal, öb er en liebi (s dritt Mal: öb er en gärn heig); de Petrus antwortet jedes Mal, de Jesus wüssi, dass er en gärn heig, und wird s dritt Mal truurig. De Jesus git em de Uftrag, sini Lämmli z weide und sini Schaf z hüete und z weide. Dänn seit er em, dass im Alter en andere en wird gürte und bringe, wo er nöd wott; de Erzäller düütet das uf de Tod, mit däm de Petrus Gott wird verherrliche. De Jesus seit zu ihm: «Chumm mir nache!»"),
 "TU-JHN-021-020-023": ("De Jünger, wo de Jesus gliebt hät", "De Petrus gseht de Jünger, wo de Jesus gliebt hät, nachechoo und fröget, was mit ihm sig. De Jesus antwortet: Wänn er well, dass dä bliibi, bis er chömi, was gang das de Petrus aa; er söll ihm nachechoo. Drus entstaat under de Brüedere s Wort, dä Jünger stärbi nöd; de Erzäller stellt richtig, dass de Jesus das nöd gseit hät."),
 "TU-JHN-021-024-025": ("S Zügnis vom Jünger und de Schluss", "Dä Jünger isch es, wo vo däm Zügnis ablegt und das gschribe hät; «mer» wüssed, dass sis Zügnis wahr isch. De Jesus hät no vil anders gmacht; wänn alles einzeln ufgschribe würd, chönnt nach de Meinig vom Erzäller d Wält d Büecher nöd fasse."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("Johanneische Schlüsselwörter folgen den Grundentscheiden in scripts/authoring/johannes_text_01_03.py: σημεῖον «Zeichen», "
  "δοξάζω «verherrlichen», μένω «bleiben», ἀμὴν ἀμήν «Amen, amen», κόσμος «Welt», λόγος «Wort», οἱ Ἰουδαῖοι wörtlich «die "
  "Juden» (eine Deutungsentscheidung; kontextbezogen wäre etwa «die jüdischen Führer» möglich, siehe [[JHN.20.19]]). "
  "Zusätzlich: ἀγαπάω «lieben», φιλέω «lieb haben» (siehe [[JHN.21.15]]); παραδίδωμι «ausliefern»."),
 ("[[JHN.20.31]]: Der SBLGNT liest mit WH πιστεύητε («damit ihr glaubt», Präsens), Treg, NA28 und RP πιστεύσητε; "
  "die Übersetzung lässt offen, ob «zum Glauben kommen» oder «im Glauben bleiben» gemeint ist (Entscheidung und Alternative)."),
 ("Kapitel 21 folgt auf den Schluss [[JHN.20.30]]–[[JHN.20.31]] und wird oft als Nachtrag beurteilt, von anderen als "
  "ursprünglicher Teil des Werks; die Übersetzung behandelt es wie den übrigen Text. In der CNTR-Transkription von 01 steht "
  "[[JHN.21.25]] nur als Korrektur (die Erstschrift hat für den Vers keinen Text)."),
 ("Johannes erzählt oft im Präsens («sie sagt», «er kommt»); das ist beibehalten. ὅτι vor direkter Rede ist nicht eigens übersetzt."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Johanneischi Schlüsselwörter nach de Grundentscheid in scripts/authoring/johannes_text_01_03.py: σημεῖον «Zeiche», "
  "δοξάζω «verherrliche», μένω «bliibe», ἀμὴν ἀμήν «Amen, amen», κόσμος «Wält», λόγος «Wort», οἱ Ἰουδαῖοι wörtlich «d Jude» "
  "(Düütigsentscheid). Dezue: ἀγαπάω «liebe», φιλέω «gärn haa» ([[JHN.21.15]]); Gott, de Vatter."),
 ("[[JHN.20.31]]: De SBLGNT hät πιστεύητε («demit ir glaubed»), anderi Usgabe πιστεύσητε; lueg Entscheidig und Alternative."),
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
        refs_c = [f"JHN.{c}.{v}" for v in range(1, last + 1) if f"JHN.{c}.{v}" in toks]
        if len(refs_c) != last:
            raise SystemExit(f"JHN {c}: Verse ohne Tokens")
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Liib), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-JHN-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; historisches Präsens beibehalten; johanneische Schlüsselwörter einheitlich. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/johannes_text_20_21.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 20–21 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
