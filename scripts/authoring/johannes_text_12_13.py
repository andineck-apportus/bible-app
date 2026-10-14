#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 12–13 (Salbung, Einzug, die Stunde der Verherrlichung, Fusswaschung, Ansage der
Auslieferung, neues Gebot) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_12_13.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben.

Grundentscheide zu den johanneischen Schlüsselwörtern (λόγος, ἐγώ εἰμι, δόξα/δοξάζω, σημεῖον, μένω, ἀμὴν ἀμήν,
κόσμος, οἱ Ἰουδαῖοι, ὑψόω …) sind in scripts/authoring/johannes_text_01_03.py begründet (parallel entstehend) und
gelten hier unverändert; die Entscheidungen unten verweisen darauf.

Besonderheiten:
- In 12,38–40 zitiert der Erzähler Jesaja ([[ISA.53.1]], [[ISA.6.10]]); die Zitate stehen in Anführungszeichen und sind
  in decisions belegt. Weitere Schriftzitate: [[PSA.118.26]] (12,13), [[ZEC.9.9]] (12,15), [[PSA.41.9]] (13,18).
- In Johannes 12–13 fehlt kein Vers im SBLGNT (per Skript geprüft).

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
CHAPTERS = ((12, 50), (13, 38))

DE = {
 # ------------------------------------------------------------ Kapitel 12
 "JHN.12.1": "[Sechs]{5} [Tage]{6} [vor]{4} [dem Passa]{7,8} [nun]{2} [kam]{9} [Jesus]{1,3} [nach]{10} [Betanien]{11}, [wo]{12} [Lazarus]{14} [war]{13}, [den]{15} [Jesus]{19} [von]{17} [den Toten]{18} [auferweckt hatte]{16}.",
 "JHN.12.2": "[Dort]{5} [bereiteten sie]{1} [ihm]{3} [nun]{2} [ein Mahl]{4}, und{6} [Marta]{7,8} [bediente]{9}; [Lazarus]{10,12} [aber]{11} [war]{14} [einer]{13} [von]{15} [denen]{16}, [die]{17} [mit]{18} [ihm]{19} [zu Tisch lagen]{17}.",
 "JHN.12.3": "[Maria]{1,3} [nun]{2} [nahm]{4} [ein Pfund]{5} [Salböl]{6} [aus reiner]{8}, [sehr kostbarer]{9} [Narde]{7}, [salbte]{10} [die Füsse]{11,12} [Jesu]{13,14} und{15} [trocknete]{16} [seine]{22} [Füsse]{20,21} [mit]{17} [ihren]{19} [Haaren]{18}; [das Haus]{23,25} [aber]{24} [wurde]{26} [vom]{27,28} [Duft]{29} [des Salböls]{30,31} [erfüllt]{26}.",
 "JHN.12.4": "[Judas]{3} [Iskariot]{4,5} [aber]{2}, [einer]{6} [seiner]{7,9} [Jünger]{8}, [der]{10} [ihn]{12} [ausliefern]{13} [würde]{11}, [sagt]{1}:",
 "JHN.12.5": "«[Warum]{1,2} [wurde]{7} [dieses]{3} [Salböl]{4,5} [nicht]{6} [für dreihundert]{8} [Denare]{9} [verkauft]{7} und{10} [den Armen]{12} [gegeben]{11}?»",
 "JHN.12.6": "[Das]{3} [sagte er]{1} [aber]{2} [nicht]{4}, [weil]{5} [ihm]{10} [an]{6} [den Armen]{7,8} [lag]{9}, [sondern]{11} [weil]{12} [er]{14} [ein Dieb]{13} [war]{14}; und{15} [er hatte]{18} [die Kasse]{16,17} und [nahm die Einlagen an sich]{19-21}.",
 "JHN.12.7": "[Jesus]{3,4} [sagte]{1} [nun]{2}: «[Lass]{5} [sie]{6}, [damit]{7} [sie]{14} [es]{15} [für]{8} [den Tag]{9,10} [meines]{13} [Begräbnisses]{11,12} [bewahre]{14}.",
 "JHN.12.8": "Denn{3} [die Armen]{1,2} [habt ihr]{5} [allezeit]{4} [bei]{6} [euch]{7}, [mich]{8} [aber]{9} [habt ihr]{12} [nicht]{10} [allezeit]{11}.»",
 "JHN.12.9": "[Eine grosse]{4} [Menge]{3} [von]{5} [den Juden]{6,7} [erfuhr]{1} [nun]{2}, [dass]{8} [er]{10} [dort]{9} [sei]{10}, und{11} [sie kamen]{12} [nicht]{13} [nur]{17} [wegen]{14} [Jesus]{15,16}, [sondern]{18} [um]{19} [auch]{20} [Lazarus]{21,22} [zu sehen]{23}, [den]{24} [er]{25} [von]{26} [den Toten]{27} [auferweckt hatte]{25}.",
 "JHN.12.10": "[Die Hohepriester]{3,4} [aber]{2} [beschlossen]{1}, [auch]{6} [Lazarus]{7,8} [zu töten]{5,9},",
 "JHN.12.11": "[weil]{1} [viele]{2} [der Juden]{6,7} [seinetwegen]{3,4} [weggingen]{5} und{8} [an]{10} [Jesus]{11,12} [glaubten]{9}.",
 "JHN.12.12": "[Am folgenden Tag]{1,2}, als [die grosse]{3,5} [Menge]{4}, [die]{6} [zum]{8,9} [Fest]{10} [gekommen war]{7}, [hörte]{11}, [dass]{12} [Jesus]{14,15} [nach]{16} [Jerusalem]{17} [kommt]{13},",
 "JHN.12.13": "[nahmen sie]{1} [die Palmzweige]{2-5} und{6} [zogen hinaus]{7}, [ihm]{10} [entgegen]{8,9}, und{11} [schrien]{12}: «[Hosanna]{13}! [Gepriesen]{14} sei, [der]{15} [kommt]{16} [im]{17} [Namen]{18} [des Herrn]{19}, und{20} [der König]{21,22} [Israels]{23,24}!»",
 "JHN.12.14": "[Jesus]{3,4} [aber]{2} [fand]{1} [einen jungen Esel]{5} und [setzte sich]{6} [darauf]{7,8}, [wie]{9} [geschrieben steht]{10,11}:",
 "JHN.12.15": "«[Fürchte dich]{2} [nicht]{1}, [Tochter]{3} [Zion]{4}! [Siehe]{5}, [dein]{8} [König]{6,7} [kommt]{9}, [er sitzt]{10} [auf]{11} [dem Fohlen]{12} [eines Esels]{13}.»",
 "JHN.12.16": "[Das]{1} [verstanden]{3} [seine]{4} [Jünger]{5,6} [zuerst]{7,8} [nicht]{2}; [aber]{9} [als]{10} [Jesus]{12} [verherrlicht worden war]{11}, [da]{13} [erinnerten sie sich]{14}, [dass]{15} [dies]{16} [über]{18} [ihn]{19} [geschrieben]{20} [war]{17} und{21} [dass sie]{23} [ihm]{24} [dies]{22} [getan hatten]{23}.",
 "JHN.12.17": "[Die Menge]{3,4} [nun]{2}, [die]{5} [bei]{7} [ihm]{8} [gewesen war]{6}, [als]{9} [er]{12} [Lazarus]{10,11} [aus]{13} [dem Grab]{14,15} [gerufen]{12} und{16} [ihn]{18} [von]{19} [den Toten]{20} [auferweckt hatte]{17}, [bezeugte es]{1}.",
 "JHN.12.18": "[Deshalb]{1,2} [zog]{4} [ihm]{5} [auch]{3} [die Menge]{6,7} [entgegen]{4}, [weil]{8} [sie gehört hatten]{9}, dass [er]{11} [dieses]{10} [Zeichen]{13,14} [getan habe]{12}.",
 "JHN.12.19": "[Die Pharisäer]{1,3} [nun]{2} [sagten]{4} [zueinander]{5,6}: «[Ihr seht]{7}, [dass]{8} [ihr]{10} [gar nichts]{9,11} [erreicht]{10}. [Siehe]{12}, [die Welt]{13,14} [ist]{17} [hinter]{15} [ihm]{16} [hergelaufen]{17}!»",
 "JHN.12.20": "[Es waren]{1} [aber]{2} [einige]{4} [Griechen]{3} [unter]{5} [denen]{6}, [die hinaufzogen]{7}, [um]{8} [am]{10,11} [Fest]{12} [anzubeten]{9}.",
 "JHN.12.21": "[Diese]{1} [nun]{2} [traten]{3} [zu Philippus]{4} [heran]{3}, [dem]{5} [aus]{6} [Betsaida]{7} [in]{8} [Galiläa]{9}, und{10} [baten]{11} [ihn]{12} [und sagten]{13}: «[Herr]{14}, [wir möchten]{15} [Jesus]{16,17} [sehen]{18}.»",
 "JHN.12.22": "[Philippus]{2,3} [kommt]{1} und{4} [sagt es]{5} [dem Andreas]{6,7}; [Andreas]{9} und{10} [Philippus]{11} [kommen]{8} und{12} [sagen es]{13} [Jesus]{14,15}.",
 "JHN.12.23": "[Jesus]{1,3} [aber]{2} [antwortet]{4} [ihnen]{5} [und sagt]{6}: «[Gekommen ist]{7} [die Stunde]{8,9}, [dass]{10} [der Menschensohn]{12-15} [verherrlicht wird]{11}.",
 "JHN.12.24": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Wenn]{5} [das]{7} [Weizenkorn]{8-10} [nicht]{6} [in]{12} [die Erde]{13,14} [fällt]{11} und [stirbt]{15}, [bleibt]{18} [es]{16} [allein]{17}; [wenn]{19} [es]{21} [aber]{20} [stirbt]{21}, [bringt es]{24} [viel]{22} [Frucht]{23}.",
 "JHN.12.25": "[Wer]{1} [sein]{5} [Leben]{3,4} [liebt]{2}, [verliert]{6} [es]{7}; und{8} [wer]{9} [sein]{13} [Leben]{11,12} [in]{14} [dieser]{17} [Welt]{15,16} [hasst]{10}, [wird]{21} [es]{22} [für das]{18} [ewige]{20} [Leben]{19} [bewahren]{21}.",
 "JHN.12.26": "[Wenn]{1} [jemand]{3} [mir]{2} [dient]{4}, [soll er]{6} [mir]{5} [folgen]{6}; und{7} [wo]{8} [ich]{10} [bin]{9}, [dort]{11} [wird]{17} [auch]{12} [mein]{13,15,16} [Diener]{14} [sein]{17}. [Wenn]{18} [jemand]{19} [mir]{20} [dient]{21}, [wird]{22} [der Vater]{24,25} [ihn]{23} [ehren]{22}.",
 "JHN.12.27": "[Jetzt]{1} [ist]{5} [meine]{4} [Seele]{2,3} [erschüttert]{5}, und{6} [was]{7} [soll ich sagen]{8}? ‹[Vater]{9}, [rette]{10} [mich]{11} [aus]{12} [dieser]{15} [Stunde]{13,14}›? [Aber]{16} [gerade deshalb]{17,18} [bin ich]{19} [in]{20} [diese]{23} [Stunde]{21,22} [gekommen]{19}.",
 "JHN.12.28": "[Vater]{1}, [verherrliche]{2} [deinen]{3} [Namen]{4,5}!» [Da]{7} [kam]{6} [eine Stimme]{8} [aus]{9} [dem Himmel]{10,11}: «[Ich habe ihn]{13} [schon]{12} [verherrlicht]{13} und{14} [werde ihn]{16} [wieder]{15} [verherrlichen]{16}.»",
 "JHN.12.29": "[Die Menge]{1,3} [nun]{2}, [die]{4} [dastand]{5} und{6} [es hörte]{7}, [sagte]{8}, [es habe gedonnert]{9,10}; [andere]{11} [sagten]{12}: «[Ein Engel]{13} [hat]{15} [zu ihm]{14} [geredet]{15}.»",
 "JHN.12.30": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4}: «[Nicht]{5} [um]{6} [meinetwillen]{7} [ist]{11} [diese]{10} [Stimme]{8,9} [ergangen]{11}, [sondern]{12} [um]{13} [euretwillen]{14}.",
 "JHN.12.31": "[Jetzt]{1} [ist]{3} [Gericht]{2} [über]{4} [diese]{6} [Welt]{5}; [jetzt]{7} [wird]{13,14} [der Herrscher]{8,9} [dieser]{12} [Welt]{10,11} [hinausgeworfen]{13,14}.",
 "JHN.12.32": "[Und ich]{1}, [wenn]{2} [ich]{3} [von]{4} [der Erde]{5,6} [erhöht bin]{3}, [werde]{8} [alle]{7} [zu]{9} [mir]{10} [ziehen]{8}.»",
 "JHN.12.33": "[Das]{1} [aber]{2} [sagte er]{3}, [um anzuzeigen]{4}, [welchen]{5} [Tod]{6} [er sterben]{8} [sollte]{7}.",
 "JHN.12.34": "[Die Menge]{4,5} [nun]{2} [antwortete]{1} [ihm]{3}: «[Wir]{6} [haben]{7} [aus]{8} [dem Gesetz]{9,10} [gehört]{7}, [dass]{11} [der Christus]{12,13} [in]{15} [Ewigkeit]{16,17} [bleibt]{14}; und{18} [wie]{19} [sagst]{20} [du]{21}, [dass]{22} [der Menschensohn]{25-28} [erhöht werden]{24} [muss]{23}? [Wer]{29} [ist]{30} [dieser]{31} [Menschensohn]{32-35}?»",
 "JHN.12.35": "[Da]{2} [sagte]{1} [Jesus]{4,5} [zu ihnen]{3}: «[Noch]{6} [eine kleine]{7} [Zeit]{8} [ist]{13} [das Licht]{9,10} [unter]{11} [euch]{12}. [Geht euren Weg]{14}, [solange]{15} [ihr]{18} [das Licht]{16,17} [habt]{18}, [damit]{19} [die Finsternis]{21} [euch]{22} [nicht]{20} [überfällt]{23}; und{24} [wer]{25} [in]{27} [der Finsternis]{28,29} [geht]{26}, [weiss]{31} [nicht]{30}, [wohin]{32} [er geht]{33}.",
 "JHN.12.36": "[Solange]{1} [ihr]{4} [das Licht]{2,3} [habt]{4}, [glaubt]{5} [an]{6} [das Licht]{7,8}, [damit]{9} [ihr]{12} [Söhne]{10} [des Lichts]{11} [werdet]{12}.» [Dies]{13} [redete]{14} [Jesus]{15}, und{16} [er ging weg]{17} und [verbarg sich]{18} [vor]{19} [ihnen]{20}.",
 "JHN.12.37": "Obwohl [er]{3} [aber]{2} [so viele]{1} [Zeichen]{4} [vor]{6} [ihnen]{7} [getan hatte]{5}, [glaubten sie]{9} [nicht]{8} [an]{10} [ihn]{11},",
 "JHN.12.38": "[damit]{1} [das Wort]{2,3} [des Propheten]{5,6} [Jesaja]{4} [erfüllt würde]{7}, [das]{8} [er gesprochen hat]{9}: «[Herr]{10}, [wer]{11} [hat]{12} [unserer]{15} [Botschaft]{13,14} [geglaubt]{12}? Und{16} [der Arm]{17,18} [des Herrn]{19} – [wem]{20} [wurde er offenbart]{21}?»",
 "JHN.12.39": "[Deshalb]{1,2} [konnten sie]{4} [nicht]{3} [glauben]{5}, [denn]{6} [Jesaja]{9} [hat]{8} [wiederum]{7} [gesagt]{8}:",
 "JHN.12.40": "«[Er hat]{1} [ihre]{2} [Augen]{3,4} [geblendet]{1} und{5} [ihr]{7} [Herz]{8,9} [verhärtet]{6}, [damit]{10} [sie]{12} [nicht]{11} [mit den]{13} [Augen]{14} [sehen]{12} und{15} [mit dem]{17} [Herzen]{18} [verstehen]{16} und{19} [umkehren]{20} – und{21} [ich werde]{22} [sie]{23} [heilen]{22}.»",
 "JHN.12.41": "[Das]{1} [sagte]{2} [Jesaja]{3}, [weil]{4} [er]{5} [seine]{8} [Herrlichkeit]{6,7} [sah]{5}, und{9} [er redete]{10} [über]{11} [ihn]{12}.",
 "JHN.12.42": "[Dennoch]{1,2} [glaubten]{8} [auch]{3} [von]{4} [den Oberen]{5,6} [viele]{7} [an]{9} [ihn]{10}; [aber]{11} [wegen]{12} [der Pharisäer]{13,14} [bekannten sie es]{16} [nicht]{15}, [um]{17} [nicht]{18} [aus der Synagoge ausgeschlossen]{19} [zu werden]{20}.",
 "JHN.12.43": "[Sie liebten]{1} [nämlich]{2} [die Ehre]{3,4} [bei den Menschen]{5,6} [mehr]{7} [als]{8} [die Ehre]{9,10} [bei Gott]{11,12}.",
 "JHN.12.44": "[Jesus]{1} [aber]{2} [rief laut]{3} und{4} [sagte]{5}: «[Wer]{6} [an]{8} [mich]{9} [glaubt]{7}, [glaubt]{11} [nicht]{10} [an]{12} [mich]{13}, [sondern]{14} [an]{15} [den]{16}, [der]{17} [mich]{18} [gesandt hat]{17},",
 "JHN.12.45": "und{1} [wer]{2} [mich]{4} [sieht]{3}, [sieht]{5} [den]{6}, [der]{7} [mich]{8} [gesandt hat]{7}.",
 "JHN.12.46": "[Ich]{1} [bin]{6} [als Licht]{2} [in]{3} [die Welt]{4,5} [gekommen]{6}, [damit]{7} [jeder]{8}, [der]{9} [an]{11} [mich]{12} [glaubt]{10}, [nicht]{16} [in]{13} [der Finsternis]{14,15} [bleibt]{17}.",
 "JHN.12.47": "Und{1} [wenn]{2} [jemand]{3} [meine]{4} [Worte]{6,7} [hört]{5} und{8} [sie]{10} [nicht]{9} [bewahrt]{10}, [richte]{13} [ich]{11} [ihn]{14} [nicht]{12}; [denn]{16} [ich bin]{17} [nicht]{15} [gekommen]{17}, [um]{18} [die Welt]{20,21} [zu richten]{19}, [sondern]{22} [um]{23} [die Welt]{25,26} [zu retten]{24}.",
 "JHN.12.48": "[Wer]{1} [mich]{3} [verwirft]{2} und{4} [meine]{9} [Worte]{7,8} [nicht]{5} [annimmt]{6}, [hat]{10} [einen]{11}, [der]{12} [ihn]{13} [richtet]{12}: [Das Wort]{14,15}, [das]{16} [ich geredet habe]{17}, [das]{18} [wird]{19} [ihn]{20} [richten]{19} [am]{21,22} [letzten]{23} [Tag]{24}.",
 "JHN.12.49": "[Denn]{1} [ich]{2} [habe]{6} [nicht]{5} [aus]{3} [mir selbst]{4} [geredet]{6}, [sondern]{7} [der Vater]{8,11}, [der]{9} [mich]{10} [gesandt hat]{9}, [er selbst]{12} [hat]{15} [mir]{13} [ein Gebot]{14} [gegeben]{15}, [was]{16} [ich sagen]{17} und{18} [was]{19} [ich reden soll]{20}.",
 "JHN.12.50": "Und{1} [ich weiss]{2}, [dass]{3} [sein]{6} [Gebot]{4,5} [ewiges]{8} [Leben]{7} [ist]{9}. [Was]{10} [ich]{12} [also]{11} [rede]{13}, [rede ich]{20} [so]{19}, [wie]{14} es [mir]{16} [der Vater]{17,18} [gesagt hat]{15}.»",
 # ------------------------------------------------------------ Kapitel 13
 "JHN.13.1": "[Vor]{1} [dem]{3} [Passafest]{4-6} [aber]{2} [wusste]{7} [Jesus]{8,9}, [dass]{10} [seine]{12} [Stunde]{13,14} [gekommen war]{11}, [aus]{17} [dieser]{20} [Welt]{18,19} [zum]{21,22} [Vater]{23} [hinüberzugehen]{15,16}. [Er hatte]{24} [die Seinen]{25,26} [geliebt]{24}, [die]{27} [in]{28} [der Welt]{29,30} waren, und [er liebte]{33} [sie]{34} [bis zur Vollendung]{31,32}.",
 "JHN.13.2": "Und{1} [als]{3} [das Mahl]{2} [im Gang war]{3} – [der Teufel]{4,5} [hatte]{7} [schon]{6} [ins]{8,9} [Herz]{10} [gegeben]{7}, [dass]{11} [Judas]{14}, [Sohn des Simon]{15} [Iskariot]{16}, [ihn]{13} [ausliefern sollte]{12} –,",
 "JHN.13.3": "[da er wusste]{1}, [dass]{2} [ihm]{5} [der Vater]{6,7} [alles]{3} [in]{8} [die]{9} [Hände]{10} [gegeben hatte]{4} und{11} [dass]{12} [er]{15} [von]{13} [Gott]{14} [ausgegangen war]{15} und{16} [zu]{17} [Gott]{18,19} [hingeht]{20},",
 "JHN.13.4": "[steht er]{1} [vom]{2,3} [Mahl]{4} [auf]{1} und{5} [legt]{6} [die Obergewänder]{7,8} [ab]{6}; und{9} [er nahm]{10} [ein Leinentuch]{11} und [band es]{12} [sich]{13} [um]{12}.",
 "JHN.13.5": "[Dann]{1} [giesst er]{2} [Wasser]{3} [in]{4} [das]{5} [Waschbecken]{6} und{7} [fing an]{8}, [den Jüngern]{12,13} [die Füsse]{10,11} [zu waschen]{9} und{14} [mit dem]{16} [Leinentuch]{17} [abzutrocknen]{15}, [das]{18} [er sich umgebunden hatte]{19,20}.",
 "JHN.13.6": "[So]{2} [kommt er]{1} [zu]{3} [Simon]{4} [Petrus]{5}. [Der sagt]{6} [zu ihm]{7}: «[Herr]{8}, [du]{9} [wäschst]{11} [mir]{10} [die Füsse]{12,13}?»",
 "JHN.13.7": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihm]{5}: «[Was]{6} [ich]{7} [tue]{8}, [weisst]{11} [du]{9} [jetzt]{12} [nicht]{10}; [du wirst es]{13} [aber]{14} [danach]{15,16} [erkennen]{13}.»",
 "JHN.13.8": "[Petrus]{3} [sagt]{1} [zu ihm]{2}: «[Nie]{4,5} [in Ewigkeit]{10-12} [sollst du]{6} [mir]{7} [die Füsse]{8,9} [waschen]{6}!» [Jesus]{14} [antwortete]{13} [ihm]{15}: «[Wenn]{16} [ich]{18} [dich]{19} [nicht]{17} [wasche]{18}, [hast du]{21} [keinen]{20} [Anteil]{22} [an]{23} [mir]{24}.»",
 "JHN.13.9": "[Simon]{3} [Petrus]{4} [sagt]{1} [zu ihm]{2}: «[Herr]{5}, [nicht]{6} [nur]{10} [meine]{9} [Füsse]{7,8}, [sondern]{11} [auch]{12} [die Hände]{13,14} und{15} [den Kopf]{16,17}!»",
 "JHN.13.10": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: «[Wer]{5} [gebadet ist]{6}, [hat]{8} [nicht]{7} [nötig]{9}, [sich]{14} [ausser]{10,11} [an den]{12} [Füssen]{13} [zu waschen]{14}, [sondern]{15} [er ist]{16} [ganz]{18} [rein]{17}. Und{19} [ihr]{20} [seid]{22} [rein]{21}, [aber]{23} [nicht]{24} [alle]{25}.»",
 "JHN.13.11": "[Er kannte]{1} [nämlich]{2} [den]{3}, [der]{4} [ihn]{5} [ausliefert]{4}; [deshalb]{6,7} [sagte er]{8}: «[Nicht]{10} [alle]{11} [seid ihr]{13} [rein]{12}.» ~9(ὅτι leitet die direkte Rede ein)",
 "JHN.13.12": "[Als]{1} [er]{3} [ihnen]{6} [nun]{2} [die Füsse]{4,5} [gewaschen]{3} und{7} [seine]{11} [Obergewänder]{9,10} [genommen]{8} und{12} [sich zu Tisch gelegt hatte]{13}, [sagte er]{15} [wieder]{14} [zu ihnen]{16}: «[Versteht ihr]{17}, [was]{18} [ich]{19} [euch]{20} [getan habe]{19}?",
 "JHN.13.13": "[Ihr]{1} [nennt]{2} [mich]{3} ‹[der Lehrer]{4,5}› und{6} ‹[der Herr]{7,8}›, und{9} [ihr sagt]{11} [es zu Recht]{10}, [denn]{13} [ich bin es]{12}.",
 "JHN.13.14": "[Wenn]{1} [nun]{2} [ich]{3}, [der Herr]{8,9} und{10} [der Lehrer]{11,12}, [euch]{5} [die Füsse]{6,7} [gewaschen habe]{4}, [seid]{15} [auch]{13} [ihr]{14} [verpflichtet]{15}, [einander]{16} [die Füsse]{18,19} [zu waschen]{17}.",
 "JHN.13.15": "Denn{2} [ein Beispiel]{1} [habe ich]{3} [euch]{4} [gegeben]{3}, [damit]{5} [auch]{10} [ihr]{11} [tut]{12}, [wie]{6} [ich]{7} [euch]{9} [getan habe]{8}.",
 "JHN.13.16": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Ein Knecht]{7} [ist]{6} [nicht]{5} [grösser]{8} [als]{9} [sein]{11} [Herr]{10}, [noch]{12} [ein Gesandter]{13} [grösser]{14} [als]{15} [der, der]{16} [ihn]{17} [gesandt hat]{16}.",
 "JHN.13.17": "[Wenn]{1} [ihr]{3} [das]{2} [wisst]{3}: [Selig]{4} [seid ihr]{5}, [wenn]{6} [ihr]{7} [es]{8} [tut]{7}.",
 "JHN.13.18": "[Nicht]{1} [von]{2} [euch allen]{3,4} [rede ich]{5}; [ich]{6} [weiss]{7}, [wen]{8} [ich erwählt habe]{9}. [Aber]{10} es geschieht, [damit]{11} [die Schrift]{12,13} [erfüllt wird]{14}: ‹[Der]{15} [mein]{17} [Brot]{18,19} [isst]{16}, [hat]{20} [gegen]{21} [mich]{22} [seine]{25} [Ferse]{23,24} [erhoben]{20}.›",
 "JHN.13.19": "[Schon jetzt]{1,2} [sage ich]{3} [es euch]{4}, [bevor]{5,6} [es geschieht]{7}, [damit]{8} [ihr]{9}, [wenn]{10} [es geschieht]{11}, [glaubt]{9}, [dass]{12} [ich]{13} [bin]{14}.",
 "JHN.13.20": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Wer]{5} [aufnimmt]{6}, [wen]{8} [immer]{7} [ich sende]{9}, [nimmt]{11} [mich]{10} [auf]{11}; [wer]{12} [aber]{13} [mich]{14} [aufnimmt]{15}, [nimmt]{16} [den]{17} [auf]{16}, [der]{18} [mich]{19} [gesandt hat]{18}.»",
 "JHN.13.21": "[Als]{2} [Jesus]{3,4} [das]{1} [gesagt hatte]{2}, [wurde er]{5} [im]{6} [Geist]{7} [erschüttert]{5}, und{8} [er bezeugte]{9} und{10} [sagte]{11}: «[Amen]{12}, [amen]{13}, [ich sage]{14} [euch]{15}: [Einer]{17} [von]{18} [euch]{19} [wird]{20} [mich]{21} [ausliefern]{20}.» ~16(ὅτι leitet die direkte Rede ein)",
 "JHN.13.22": "[Die Jünger]{4,5} [blickten]{1} [einander]{3} [an]{2}, [ratlos]{6}, [von]{7} [wem]{8} [er redet]{9}.",
 "JHN.13.23": "[Einer]{3} [von]{4} [seinen]{5,7} [Jüngern]{6}, [den]{13} [Jesus]{15,16} [liebte]{14}, [lag]{1,2} [an]{8} [der]{9} [Brust]{10} [Jesu]{11,12} [zu Tisch]{1,2}.",
 "JHN.13.24": "[Simon]{4} [Petrus]{5} [nun]{2} [nickt]{1} [diesem]{3} [zu]{1}, [er solle erfragen]{6}, [wer]{7} [es]{9} [wohl]{8} [sei]{9}, [von]{10} [dem]{11} [er redet]{12}.",
 "JHN.13.25": "[Jener]{2} [lehnt sich]{1} [so]{3} [zurück]{1} [an]{4} [die]{5} [Brust]{6} [Jesu]{7,8} [und sagt]{9} [zu ihm]{10}: «[Herr]{11}, [wer]{12} [ist es]{13}?»",
 "JHN.13.26": "[Jesus]{2,3} [antwortet]{1}: «[Der]{4} [ist es]{5}, [dem]{6} [ich]{7} [den Bissen]{9,10} [eintauchen]{8} und{11} [geben werde]{12}.» [Er taucht]{14} [nun]{15} [den Bissen]{16,17} [ein]{14} und [gibt ihn]{18} [Judas]{19}, [dem Sohn des Simon]{20} [Iskariot]{21}. ~13(αὐτῷ nimmt das Relativpronomen ᾧ wieder auf; nicht eigens wiedergegeben)",
 "JHN.13.27": "Und{1} [nach]{2} [dem]{3} [Bissen]{4}, [da]{5} [fuhr]{6} [der Satan]{9,10} [in]{7} [ihn]{8} [hinein]{6}. [Jesus]{14,15} [sagt]{11} [nun]{12} [zu ihm]{13}: «[Was]{16} [du tust]{17}, [das tu]{18} [schnell]{19}!»",
 "JHN.13.28": "[Keiner]{3} [von denen]{5} [aber]{2}, [die zu Tisch lagen]{6}, [verstand]{4}, [wozu]{7,8} [er]{9} [ihm]{10} [das]{1} [gesagt hatte]{9}.",
 "JHN.13.29": "[Einige]{1} [meinten]{3} [nämlich]{2}, [weil]{4} [Judas]{8} [die Kasse]{5,6} [hatte]{7}, [dass]{9} [Jesus]{12,13} [zu ihm]{11} [sagt]{10}: «[Kauf]{14}, [was]{15} [wir]{17} [für]{18} [das Fest]{19,20} [nötig]{16} [haben]{17}!», [oder]{21} [dass]{24} [er]{26} [den Armen]{22,23} [etwas]{25} [geben solle]{26}.",
 "JHN.13.30": "[Jener]{5} [nahm]{1} [nun]{2} [den Bissen]{3,4} und [ging]{6} [sogleich]{7} [hinaus]{6}. [Es war]{8} [aber]{9} [Nacht]{10}.",
 "JHN.13.31": "[Als]{1} [er]{3} [nun]{2} [hinausgegangen war]{3}, [sagt]{4} [Jesus]{5}: «[Jetzt]{6} [ist]{7} [der Menschensohn]{8-11} [verherrlicht worden]{7}, und{12} [Gott]{13,14} [ist]{15} [in]{16} [ihm]{17} [verherrlicht worden]{15}.",
 "JHN.13.32": "[Wenn]{1} [Gott]{2,3} [in]{5} [ihm]{6} [verherrlicht worden ist]{4}, [wird]{10} [auch]{7} [Gott]{8,9} [ihn]{11} [in]{12} [sich selbst]{13} [verherrlichen]{10}, und{14} [er wird]{16} [ihn]{17} [sogleich]{15} [verherrlichen]{16}.",
 "JHN.13.33": "[Kinder]{1}, [noch]{2} [eine kleine Weile]{3} [bin ich]{6} [bei]{4} [euch]{5}. [Ihr werdet]{7} [mich]{8} [suchen]{7}, und{9} [wie]{10} [ich]{11} [zu den Juden]{12,13} [gesagt habe]{11}: ‹[Wohin]{15} [ich]{16} [gehe]{17}, [dahin könnt]{20} [ihr]{18} [nicht]{19} [kommen]{21}›, [so sage ich]{24} [auch]{22} [euch]{23} [jetzt]{25}. ~14(ὅτι leitet die direkte Rede ein)",
 "JHN.13.34": "[Ein neues]{2} [Gebot]{1} [gebe ich]{3} [euch]{4}: [dass]{5} [ihr]{6} [einander]{7} [liebt]{6}. [Wie]{8} [ich]{9} [euch]{10} [geliebt habe]{9}, [so sollt]{11} [auch]{12} [ihr]{13} [einander]{15} [lieben]{14}.",
 "JHN.13.35": "[Daran]{1,2} [werden]{3} [alle]{4} [erkennen]{3}, [dass]{5} [ihr]{8} [meine]{6} [Jünger]{7} [seid]{8}: [wenn]{9} [ihr]{11} [Liebe]{10} [untereinander]{12,13} [habt]{11}.»",
 "JHN.13.36": "[Simon]{3} [Petrus]{4} [sagt]{1} [zu ihm]{2}: «[Herr]{5}, [wohin]{6} [gehst du]{7}?» [Jesus]{9} [antwortete]{8}: «[Wohin]{10} [ich gehe]{11}, [dahin kannst du]{13} [mir]{14} [jetzt]{15} [nicht]{12} [folgen]{16}; [du wirst]{17} [aber]{18} [später]{19} [folgen]{17}.»",
 "JHN.13.37": "[Petrus]{3,4} [sagt]{1} [zu ihm]{2}: «[Herr]{5}, [warum]{6,7} [kann ich]{9} [dir]{10} [jetzt]{12} [nicht]{8} [folgen]{11}? [Mein]{15} [Leben]{13,14} [werde ich]{18} [für]{16} [dich]{17} [hingeben]{18}.»",
 "JHN.13.38": "[Jesus]{2} [antwortet]{1}: «[Dein]{5} [Leben]{3,4} [wirst du]{8} [für]{6} [mich]{7} [hingeben]{8}? [Amen]{9}, [amen]{10}, [ich sage]{11} [dir]{12}: [Ein Hahn]{15} [wird]{16} [nicht]{13,14} [krähen]{16}, [bis]{17,18} [du]{19} [mich]{20} [dreimal]{21} [verleugnet hast]{19}.»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 12
 "JHN.12.1": "[De Jesus]{1,3} [isch]{9} [dänn]{2} [sächs]{5} [Täg]{6} [vor]{4} [em Passa]{7,8} [uf]{10} [Betanie]{11} [choo]{9}, [wo]{12} [de Lazarus]{14} [gsii isch]{13}, [dä, wo]{15} [de Jesus]{19} [vo]{17} [de Tote]{18} [uferweckt hät]{16}.",
 "JHN.12.2": "[Dört]{5} [händ si]{1} [ihm]{3} [dänn]{2} [es Ässe]{4} [gmacht]{1}, und{6} [d Marta]{7,8} [hät bedient]{9}; [de Lazarus]{10,12} [aber]{11} [isch]{14} [eine]{13} [vo]{15} [dene]{16} [gsii]{14}, [wo]{17} [mit]{18} [ihm]{19} [am Tisch gläge sind]{17}.",
 "JHN.12.3": "[D Maria]{1,3} [hät]{4} [dänn]{2} [es Pfund]{5} [Salböl]{6} [us echter]{8}, [sehr tüürer]{9} [Narde]{7} [gnoo]{4}, [hät]{10} [d Füess]{11,12} [vom Jesus]{13,14} [gsalbet]{10} und{15} [hät]{16} [sini]{22} [Füess]{20,21} [mit]{17} [ire]{19} [Haar]{18} [abtröchnet]{16}; [s Huus]{23,25} [aber]{24} [isch]{26} [vom]{27,28} [Duft]{29} [vom Salböl]{30,31} [ganz erfüllt worde]{26}.",
 "JHN.12.4": "[De Judas]{3} [Iskariot]{4,5} [aber]{2}, [eine]{6} [vo sine]{7,9} [Jünger]{8}, [wo]{10} [en]{12} [würd]{11} [uslifere]{13}, [seit]{1}:",
 "JHN.12.5": "«[Werum]{1,2} [isch]{7} [das]{3} [Salböl]{4,5} [nöd]{6} [für drüühundert]{8} [Denar]{9} [verchauft]{7} und{10} [de Arme]{12} [gää worde]{11}?»",
 "JHN.12.6": "[Das]{3} [hät er]{1} [aber]{2} [nöd]{4} [gseit]{1}, [wil]{5} [ihm]{10} [a]{6} [de Arme]{7,8} [öppis gläge isch]{9}, [sondern]{11} [wil]{12} [er]{14} [en Dieb]{13} [gsii isch]{14}; und{15} [er hät]{18} [d Kasse]{16,17} [gha]{18} und [hät das, wo inegleit worde isch, für sich gnoo]{19-21}.",
 "JHN.12.7": "[De Jesus]{3,4} [hät]{1} [dänn]{2} [gseit]{1}: «[Lass]{5} [si]{6}, [demit]{7} [si]{14} [s]{15} [für]{8} [de Tag]{9,10} [vo mim]{13} [Begräbnis]{11,12} [ufbhaltet]{14}.",
 "JHN.12.8": "Dänn{3} [d Arme]{1,2} [händ ir]{5} [immer]{4} [bi]{6} [eu]{7}, [mich]{8} [aber]{9} [händ ir]{12} [nöd]{10} [immer]{11}.»",
 "JHN.12.9": "[E grossi]{4} [Mängi]{3} [vo]{5} [de Jude]{6,7} [hät]{1} [dänn]{2} [erfahre]{1}, [dass]{8} [er]{10} [dört]{9} [isch]{10}, und{11} [si sind]{12} [choo]{12}, [nöd]{13} [nu]{17} [wäge]{14} [em Jesus]{15,16}, [sondern]{18} [zum]{19} [au]{20} [de Lazarus]{21,22} [gseh]{23}, [wo]{24} [er]{25} [vo]{26} [de Tote]{27} [uferweckt hät]{25}.",
 "JHN.12.10": "[D Hoheprieschter]{3,4} [aber]{2} [händ beschlosse]{1}, [dass si]{5} [au]{6} [de Lazarus]{7,8} [umbringed]{9},",
 "JHN.12.11": "[wil]{1} [vili]{2} [vo de Jude]{6,7} [wäge ihm]{3,4} [wäggange sind]{5} und{8} [a]{10} [de Jesus]{11,12} [glaubt händ]{9}.",
 "JHN.12.12": "[Am Tag druf]{1,2}, wo [di gross]{3,5} [Mängi]{4}, [wo]{6} [as]{8,9} [Fäscht]{10} [choo isch]{7}, [ghört hät]{11}, [dass]{12} [de Jesus]{14,15} [uf]{16} [Jerusalem]{17} [chunnt]{13},",
 "JHN.12.13": "[händ si]{1} [d Palmzwiig]{2-5} [gnoo]{1} und{6} [sind]{7} [ihm]{10} [entgäge]{8,9} [usezoge]{7}, und{11} [händ gschroue]{12}: «[Hosanna]{13}! [Globt]{14} sig, [dä, wo]{15} [chunnt]{16} [im]{17} [Name]{18} [vom Herr]{19}, und{20} [de König]{21,22} [vo Israel]{23,24}!»",
 "JHN.12.14": "[De Jesus]{3,4} [aber]{2} [hät]{1} [es Eseli]{5} [gfunde]{1} und [hät sich]{6} [druf]{7,8} [gsetzt]{6}, [wie]{9} [s gschribe staat]{10,11}:",
 "JHN.12.15": "«[Fürcht di]{2} [nöd]{1}, [Tochter]{3} [Zion]{4}! [Lueg]{5}, [din]{8} [König]{6,7} [chunnt]{9}, [er sitzt]{10} [uf]{11} [em Füli]{12} [vo me Esel]{13}.»",
 "JHN.12.16": "[Das]{1} [händ]{3} [sini]{4} [Jünger]{5,6} [zerscht]{7,8} [nöd]{2} [verstande]{3}; [aber]{9} [wo]{10} [de Jesus]{12} [verherrlicht worde isch]{11}, [dänn]{13} [händ si sich erinneret]{14}, [dass]{15} [das]{16} [über]{18} [ihn]{19} [gschribe]{20} [gsii isch]{17} und{21} [dass si]{23} [ihm]{24} [das]{22} [gmacht händ]{23}.",
 "JHN.12.17": "[D Mängi]{3,4} [dänn]{2}, [wo]{5} [bi]{7} [ihm]{8} [gsii isch]{6}, [wo]{9} [er]{12} [de Lazarus]{10,11} [us]{13} [em Grab]{14,15} [grüeft]{12} und{16} [en]{18} [vo]{19} [de Tote]{20} [uferweckt hät]{17}, [hät das bezüügt]{1}.",
 "JHN.12.18": "[Drum]{1,2} [isch]{4} [ihm]{5} [au]{3} [d Mängi]{6,7} [entgäge gange]{4}, [wil]{8} [si ghört händ]{9}, dass [er]{11} [das]{10} [Zeiche]{13,14} [gmacht hät]{12}.",
 "JHN.12.19": "[D Pharisäer]{1,3} [dänn]{2} [händ]{4} [zunenand]{5,6} [gseit]{4}: «[Ir gseend]{7}, [dass]{8} [ir]{10} [gar nüüt]{9,11} [erreiched]{10}. [Lueg]{12}, [d Wält]{13,14} [isch]{17} [hinder]{15} [ihm]{16} [härgloffe]{17}!»",
 "JHN.12.20": "[Es sind]{1} [aber]{2} [es paar]{4} [Grieche]{3} [under]{5} [dene]{6} [gsii]{1}, [wo ufezoge sind]{7}, [zum]{8} [am]{10,11} [Fäscht]{12} [aazbätte]{9}.",
 "JHN.12.21": "[Die]{1} [sind]{3} [dänn]{2} [zum Philippus]{4} [choo]{3}, [dä]{5} [vo]{6} [Betsaida]{7} [z]{8} [Galiläa]{9}, und{10} [händ]{11} [en]{12} [bätte]{11} [und gseit]{13}: «[Herr]{14}, [mir wetted]{15} [de Jesus]{16,17} [gseh]{18}.»",
 "JHN.12.22": "[De Philippus]{2,3} [chunnt]{1} und{4} [seit s]{5} [em Andreas]{6,7}; [de Andreas]{9} und{10} [de Philippus]{11} [chömed]{8} und{12} [säged s]{13} [em Jesus]{14,15}.",
 "JHN.12.23": "[De Jesus]{1,3} [aber]{2} [git]{4} [ine]{5} [Antwort]{4} [und seit]{6}: «[D Stund]{8,9} [isch choo]{7}, [dass]{10} [de Mänschesohn]{12-15} [verherrlicht wird]{11}.",
 "JHN.12.24": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Wänn]{5} [s]{7} [Weizechorn]{8-10} [nöd]{6} [in]{12} [de Bode]{13,14} [gheit]{11} und [stirbt]{15}, [bliibt]{18} [es]{16} [ellei]{17}; [wänn]{19} [es]{21} [aber]{20} [stirbt]{21}, [bringt es]{24} [vil]{22} [Frucht]{23}.",
 "JHN.12.25": "[Wer]{1} [sis]{5} [Läbe]{3,4} [liebt]{2}, [verlüürt]{6} [es]{7}; und{8} [wer]{9} [sis]{13} [Läbe]{11,12} [i]{14} [dere]{17} [Wält]{15,16} [hasst]{10}, [wird]{21} [es]{22} [für s]{18} [ewig]{20} [Läbe]{19} [bewaare]{21}.",
 "JHN.12.26": "[Wänn]{1} [öpper]{3} [mir]{2} [dient]{4}, [söll er]{6} [mir]{5} [nachegaa]{6}; und{7} [wo]{8} [ich]{10} [bi]{9}, [det]{11} [wird]{17} [au]{12} [min]{13,15,16} [Diener]{14} [sii]{17}. [Wänn]{18} [öpper]{19} [mir]{20} [dient]{21}, [wird]{22} [de Vatter]{24,25} [en]{23} [ehre]{22}.",
 "JHN.12.27": "[Jetzt]{1} [isch]{5} [mini]{4} [Seel]{2,3} [erschüttert]{5}, und{6} [was]{7} [söll ich säge]{8}? ‹[Vatter]{9}, [rett]{10} [mich]{11} [us]{12} [dere]{15} [Stund]{13,14}›? [Aber]{16} [grad drum]{17,18} [bin ich]{19} [i]{20} [die]{23} [Stund]{21,22} [choo]{19}.",
 "JHN.12.28": "[Vatter]{1}, [verherrlich]{2} [din]{3} [Name]{4,5}!» [Dänn]{7} [isch]{6} [e Stimm]{8} [vom]{9,10} [Himmel]{11} [choo]{6}: «[Ich han en]{13} [scho]{12} [verherrlicht]{13} und{14} [wirde en]{16} [wider]{15} [verherrliche]{16}.»",
 "JHN.12.29": "[D Mängi]{1,3} [dänn]{2}, [wo]{4} [dagstande isch]{5} und{6} [s ghört hät]{7}, [hät gseit]{8}, [es heig donneret]{9,10}; [anderi]{11} [händ gseit]{12}: «[En Ängel]{13} [hät]{15} [mit ihm]{14} [gredt]{15}.»",
 "JHN.12.30": "[De Jesus]{2} [hät gantwortet]{1} und{3} [gseit]{4}: «[Nöd]{5} [wäge]{6} [mir]{7} [isch]{11} [die]{10} [Stimm]{8,9} [choo]{11}, [sondern]{12} [wäge]{13} [eu]{14}.",
 "JHN.12.31": "[Jetzt]{1} [isch]{3} [Gricht]{2} [über]{4} [die]{6} [Wält]{5}; [jetzt]{7} [wird]{13,14} [de Herrscher]{8,9} [vo dere]{10,12} [Wält]{11} [usegworfe]{13,14}.",
 "JHN.12.32": "[Und ich]{1}, [wänn]{2} [ich]{3} [vo]{4} [de Ärde]{5,6} [erhöcht bi]{3}, [wirde]{8} [alli]{7} [zu]{9} [mir]{10} [zie]{8}.»",
 "JHN.12.33": "[Das]{1} [aber]{2} [hät er gseit]{3}, [zum aazeige]{4}, [was für en]{5} [Tod]{6} [er]{8} [söll]{7} [stärbe]{8}.",
 "JHN.12.34": "[D Mängi]{4,5} [hät]{1} [ihm]{3} [dänn]{2} [gantwortet]{1}: «[Mir]{6} [händ]{7} [us]{8} [em Gsetz]{9,10} [ghört]{7}, [dass]{11} [de Christus]{12,13} [für]{15} [immer]{16,17} [bliibt]{14}; und{18} [wie]{19} [seisch]{20} [du]{21}, [dass]{22} [de Mänschesohn]{25-28} [mues]{23} [erhöcht wärde]{24}? [Wer]{29} [isch]{30} [dä]{31} [Mänschesohn]{32-35}?»",
 "JHN.12.35": "[Dänn]{2} [hät]{1} [de Jesus]{4,5} [zu ine]{3} [gseit]{1}: «[No]{6} [e chliini]{7} [Ziit]{8} [isch]{13} [s Liecht]{9,10} [under]{11} [eu]{12}. [Gönd eue Wäg]{14}, [solang]{15} [ir]{18} [s Liecht]{16,17} [händ]{18}, [demit]{19} [d Fischternis]{21} [eu]{22} [nöd]{20} [überfallt]{23}; und{24} [wer]{25} [i]{27} [de Fischternis]{28,29} [gaat]{26}, [weiss]{31} [nöd]{30}, [wo]{32} [er hiigaat]{33}.",
 "JHN.12.36": "[Solang]{1} [ir]{4} [s Liecht]{2,3} [händ]{4}, [glaubed]{5} [as]{6,7} [Liecht]{8}, [demit]{9} [ir]{12} [Söhn]{10} [vom Liecht]{11} [wärded]{12}.» [Das]{13} [hät]{14} [de Jesus]{15} [gredt]{14}, und{16} [er isch furtgange]{17} und [hät sich]{18} [vor]{19} [ine]{20} [versteckt]{18}.",
 "JHN.12.37": "Obwohl [er]{3} [aber]{2} [so vil]{1} [Zeiche]{4} [vor]{6} [ine]{7} [gmacht hät]{5}, [händ si]{9} [nöd]{8} [a]{10} [ihn]{11} [glaubt]{9},",
 "JHN.12.38": "[demit]{1} [s Wort]{2,3} [vom Prophet]{5,6} [Jesaja]{4} [erfüllt wird]{7}, [wo]{8} [er gseit hät]{9}: «[Herr]{10}, [wer]{11} [hät]{12} [öisere]{15} [Botschaft]{13,14} [glaubt]{12}? Und{16} [de Arm]{17,18} [vom Herr]{19} – [wem]{20} [isch er offebaret worde]{21}?»",
 "JHN.12.39": "[Drum]{1,2} [händ si]{4} [nöd]{3} [chöne]{4} [glaube]{5}, [dänn]{6} [de Jesaja]{9} [hät]{8} [wider]{7} [gseit]{8}:",
 "JHN.12.40": "«[Er hät]{1} [ire]{2} [Auge]{3,4} [blind gmacht]{1} und{5} [ires]{7} [Härz]{8,9} [verhärtet]{6}, [demit]{10} [si]{12} [nöd]{11} [mit de]{13} [Auge]{14} [gseend]{12} und{15} [mit em]{17} [Härz]{18} [verstönd]{16} und{19} [umchehred]{20} – und{21} [ich wirde]{22} [si]{23} [heile]{22}.»",
 "JHN.12.41": "[Das]{1} [hät]{2} [de Jesaja]{3} [gseit]{2}, [wil]{4} [er]{5} [sini]{8} [Herrlichkeit]{6,7} [gseh hät]{5}, und{9} [er hät]{10} [vo]{11} [ihm]{12} [gredt]{10}.",
 "JHN.12.42": "[Trotzdem]{1,2} [händ]{8} [au]{3} [vo]{4} [de Obere]{5,6} [vili]{7} [a]{9} [ihn]{10} [glaubt]{8}; [aber]{11} [wäge]{12} [de Pharisäer]{13,14} [händ si s]{16} [nöd]{15} [bekännt]{16}, [demit]{17} [si]{20} [nöd]{18} [us de Synagoge usgschlosse]{19} [wärded]{20}.",
 "JHN.12.43": "[Si händ]{1} [nämli]{2} [d Ehr]{3,4} [bi de Mänsche]{5,6} [meh]{7} [gliebt]{1} [als]{8} [d Ehr]{9,10} [bi Gott]{11,12}.",
 "JHN.12.44": "[De Jesus]{1} [aber]{2} [hät luut grüeft]{3} und{4} [gseit]{5}: «[Wer]{6} [a]{8} [mich]{9} [glaubt]{7}, [glaubt]{11} [nöd]{10} [a]{12} [mich]{13}, [sondern]{14} [a]{15} [dä]{16}, [wo]{17} [mich]{18} [gschickt hät]{17},",
 "JHN.12.45": "und{1} [wer]{2} [mich]{4} [gseht]{3}, [gseht]{5} [dä]{6}, [wo]{7} [mich]{8} [gschickt hät]{7}.",
 "JHN.12.46": "[Ich]{1} [bi]{6} [als Liecht]{2} [i]{3} [d Wält]{4,5} [choo]{6}, [demit]{7} [jede]{8}, [wo]{9} [a]{11} [mich]{12} [glaubt]{10}, [nöd]{16} [i]{13} [de Fischternis]{14,15} [bliibt]{17}.",
 "JHN.12.47": "Und{1} [wänn]{2} [öpper]{3} [mini]{4} [Wort]{6,7} [ghört]{5} und{8} [si]{10} [nöd]{9} [bewaart]{10}, [richte]{13} [ich]{11} [en]{14} [nöd]{12}; [dänn]{16} [ich bi]{17} [nöd]{15} [choo]{17}, [zum]{18} [d Wält]{20,21} [richte]{19}, [sondern]{22} [zum]{23} [d Wält]{25,26} [rette]{24}.",
 "JHN.12.48": "[Wer]{1} [mich]{3} [ablehnt]{2} und{4} [mini]{9} [Wort]{7,8} [nöd]{5} [aanimmt]{6}, [hät]{10} [eine]{11}, [wo]{12} [en]{13} [richtet]{12}: [S Wort]{14,15}, [wo]{16} [ich gredt han]{17}, [das]{18} [wird]{19} [en]{20} [richte]{19} [am]{21,22} [letschte]{23} [Tag]{24}.",
 "JHN.12.49": "[Dänn]{1} [ich]{2} [han]{6} [nöd]{5} [us]{3} [mir sälber]{4} [gredt]{6}, [sondern]{7} [de Vatter]{8,11}, [wo]{9} [mich]{10} [gschickt hät]{9}, [er sälber]{12} [hät]{15} [mir]{13} [es Gebot]{14} [gää]{15}, [was]{16} [ich säge]{17} und{18} [was]{19} [ich rede söll]{20}.",
 "JHN.12.50": "Und{1} [ich weiss]{2}, [dass]{3} [sis]{6} [Gebot]{4,5} [ewigs]{8} [Läbe]{7} [isch]{9}. [Was]{10} [ich]{12} [also]{11} [rede]{13}, [red ich]{20} [eso]{19}, [wie]{14} [s mir]{16} [de Vatter]{17,18} [gseit hät]{15}.»",
 # ------------------------------------------------------------ Kapitel 13
 "JHN.13.1": "[Vor]{1} [em]{3} [Passafäscht]{4-6} [aber]{2} [hät]{7} [de Jesus]{8,9} [gwüsst]{7}, [dass]{10} [sini]{12} [Stund]{13,14} [choo isch]{11}, [wo-n-er]{15} [us]{17} [dere]{20} [Wält]{18,19} [zum]{21,22} [Vatter]{23} [überegaat]{16}. [Er hät]{24} [di Sine]{25,26} [gliebt]{24}, [wo]{27} [i]{28} [de Wält]{29,30} gsii sind, und [er hät]{33} [si]{34} [bis zur Vollendig]{31,32} [gliebt]{33}.",
 "JHN.13.2": "Und{1} [wo]{3} [s Ässe]{2} [im Gang gsii isch]{3} – [de Tüüfel]{4,5} [hät]{7} [scho]{6} [is]{8,9} [Härz]{10} [gleit]{7}, [dass]{11} [de Judas]{14}, [de Sohn vom Simon]{15} [Iskariot]{16}, [en]{13} [söll uslifere]{12} –,",
 "JHN.13.3": "[wil er gwüsst hät]{1}, [dass]{2} [ihm]{5} [de Vatter]{6,7} [alles]{3} [i]{8} [d]{9} [Händ]{10} [gää hät]{4} und{11} [dass]{12} [er]{15} [vo]{13} [Gott]{14} [usgange isch]{15} und{16} [zu]{17} [Gott]{18,19} [hiigaat]{20},",
 "JHN.13.4": "[staat er]{1} [vom]{2,3} [Ässe]{4} [uf]{1} und{5} [leit]{6} [d Oberchleider]{7,8} [ab]{6}; und{9} [er hät]{10} [es Liinetuech]{11} [gnoo]{10} und [hät]{12} [sich]{13} [s umbunde]{12}.",
 "JHN.13.5": "[Dänn]{1} [schüttet er]{2} [Wasser]{3} [i]{4} [s]{5} [Wäschbecki]{6} und{7} [hät aagfange]{8}, [de Jünger]{12,13} [d Füess]{10,11} [z wäsche]{9} und{14} [mit em]{16} [Liinetuech]{17} [abztröchne]{15}, [wo]{18} [er sich umbunde gha hät]{19,20}.",
 "JHN.13.6": "[So]{2} [chunnt er]{1} [zum]{3} [Simon]{4} [Petrus]{5}. [Dä seit]{6} [zu ihm]{7}: «[Herr]{8}, [du]{9} [wäschisch]{11} [mir]{10} [d Füess]{12,13}?»",
 "JHN.13.7": "[De Jesus]{2} [hät]{1} [ihm]{5} [gantwortet]{1} und{3} [gseit]{4}: «[Was]{6} [ich]{7} [mache]{8}, [weisch]{11} [du]{9} [jetzt]{12} [nöd]{10}; [du wirsch es]{13} [aber]{14} [spöter]{15,16} [verstaa]{13}.»",
 "JHN.13.8": "[De Petrus]{3} [seit]{1} [zu ihm]{2}: «[Nie]{4,5} [im Läbe]{10-12:idiom} [wäschisch du]{6} [mir]{7} [d Füess]{8,9}!» [De Jesus]{14} [hät]{13} [ihm]{15} [gantwortet]{13}: «[Wänn]{16} [ich]{18} [dich]{19} [nöd]{17} [wäsche]{18}, [hesch]{21} [kein]{20} [Teil]{22} [a]{23} [mir]{24}.»",
 "JHN.13.9": "[De Simon]{3} [Petrus]{4} [seit]{1} [zu ihm]{2}: «[Herr]{5}, [nöd]{6} [nu]{10} [mini]{9} [Füess]{7,8}, [sondern]{11} [au]{12} [d Händ]{13,14} und{15} [de Chopf]{16,17}!»",
 "JHN.13.10": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: «[Wer]{5} [badet hät]{6}, [bruucht]{8,9} [sich]{14} [nöd]{7} [z wäsche]{14}, [ussert]{10,11} [a de]{12} [Füess]{13}, [sondern]{15} [er isch]{16} [ganz]{18} [rein]{17}. Und{19} [ir]{20} [sind]{22} [rein]{21}, [aber]{23} [nöd]{24} [alli]{25}.»",
 "JHN.13.11": "[Er hät]{1} [nämli]{2} [dä]{3} [kännt]{1}, [wo]{4} [en]{5} [usliferet]{4}; [drum]{6,7} [hät er gseit]{8}: «[Nöd]{10} [alli]{11} [sind]{13} [rein]{12}.» ~9(ὅτι leitet di diräkt Red ii)",
 "JHN.13.12": "[Wo]{1} [er]{3} [ine]{6} [dänn]{2} [d Füess]{4,5} [gwäsche]{3} und{7} [sini]{11} [Oberchleider]{9,10} [gnoo]{8} und{12} [sich an Tisch gleit hät]{13}, [hät er]{15} [wider]{14} [zu ine]{16} [gseit]{15}: «[Verstönd ir]{17}, [was]{18} [ich]{19} [eu]{20} [gmacht han]{19}?",
 "JHN.13.13": "[Ir]{1} [säged]{2} [mir]{3} ‹[de Lehrer]{4,5}› und{6} ‹[de Herr]{7,8}›, und{9} [ir säged]{11} [s zu Rächt]{10}, [dänn]{13} [ich bi s]{12}.",
 "JHN.13.14": "[Wänn]{1} [also]{2} [ich]{3}, [de Herr]{8,9} und{10} [de Lehrer]{11,12}, [eu]{5} [d Füess]{6,7} [gwäsche han]{4}, [dänn sind]{15} [au]{13} [ir]{14} [verpflichtet]{15}, [enand]{16} [d Füess]{18,19} [z wäsche]{17}.",
 "JHN.13.15": "Dänn{2} [es Biispil]{1} [han ich]{3} [eu]{4} [gää]{3}, [demit]{5} [au]{10} [ir]{11} [mached]{12}, [wie]{6} [ich]{7} [eu]{9} [gmacht han]{8}.",
 "JHN.13.16": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [En Knecht]{7} [isch]{6} [nöd]{5} [grösser]{8} [als]{9} [sin]{11} [Herr]{10}, [und au nöd]{12} [en Gsandte]{13} [grösser]{14} [als]{15} [dä, wo]{16} [en]{17} [gschickt hät]{16}.",
 "JHN.13.17": "[Wänn]{1} [ir]{3} [das]{2} [wüssed]{3}: [Sälig]{4} [sind ir]{5}, [wänn]{6} [ir]{7} [s]{8} [mached]{7}.",
 "JHN.13.18": "[Nöd]{1} [vo]{2} [eu allne]{3,4} [red ich]{5}; [ich]{6} [weiss]{7}, [wele]{8} [ich usgwäält han]{9}. [Aber]{10} es passiert, [demit]{11} [d Schrift]{12,13} [erfüllt wird]{14}: ‹[Dä, wo]{15} [mis]{17} [Broot]{18,19} [isst]{16}, [hät]{20} [gäge]{21} [mich]{22} [sini]{25} [Färse]{23,24} [glüpft]{20}.›",
 "JHN.13.19": "[Scho jetzt]{1,2} [säg ich]{3} [s eu]{4}, [bevor]{5,6} [s passiert]{7}, [demit]{8} [ir]{9}, [wänn]{10} [s passiert]{11}, [glaubed]{9}, [dass]{12} [ich]{13} [bi]{14}.",
 "JHN.13.20": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Wer]{5} [ufnimmt]{6}, [wän]{8} [immer]{7} [ich schicke]{9}, [nimmt]{11} [mich]{10} [uf]{11}; [wer]{12} [aber]{13} [mich]{14} [ufnimmt]{15}, [nimmt]{16} [dä]{17} [uf]{16}, [wo]{18} [mich]{19} [gschickt hät]{18}.»",
 "JHN.13.21": "[Wo]{2} [de Jesus]{3,4} [das]{1} [gseit hät]{2}, [isch er]{5} [im]{6} [Geischt]{7} [erschüttert worde]{5}, und{8} [er hät s bezüügt]{9} und{10} [gseit]{11}: «[Amen]{12}, [amen]{13}, [ich säge]{14} [eu]{15}: [Eine]{17} [vo]{18} [eu]{19} [wird]{20} [mich]{21} [uslifere]{20}.» ~16(ὅτι leitet di diräkt Red ii)",
 "JHN.13.22": "[D Jünger]{4,5} [händ]{1} [enand]{3} [aaglueget]{1}, [ratlos]{6}, [vo]{7} [wem]{8} [er redt]{9}. ~2(εἰς isch im Verb «aaluege» enthalte)",
 "JHN.13.23": "[Eine]{3} [vo]{4} [sine]{5,7} [Jünger]{6}, [wo]{13} [de Jesus]{15,16} [gliebt hät]{14}, [isch]{1,2} [a]{8} [de]{9} [Bruscht]{10} [vom Jesus]{11,12} [am Tisch gläge]{1,2}.",
 "JHN.13.24": "[De Simon]{4} [Petrus]{5} [winkt]{1} [dem]{3} [dänn]{2}, [er söll usefinde]{6}, [wer]{7} [es]{9} [ächt]{8} [sig]{9}, [vo]{10} [dem]{11} [er redt]{12}.",
 "JHN.13.25": "[Dä]{2} [leit sich]{1} [eso]{3} [zrugg]{1} [a]{4} [d]{5} [Bruscht]{6} [vom Jesus]{7,8} [und seit]{9} [zu ihm]{10}: «[Herr]{11}, [wer]{12} [isch es]{13}?»",
 "JHN.13.26": "[De Jesus]{2,3} [git]{1} [Antwort]{1}: «[Dä]{4} [isch es]{5}, [wo]{6} [ich]{7} [de Bisse]{9,10} [iituuche]{8} und{11} [ihm]{13} [gib]{12}.» [Er tuucht]{14} [dänn]{15} [de Bisse]{16,17} [ii]{14} und [git en]{18} [em Judas]{19}, [em Sohn vom Simon]{20} [Iskariot]{21}.",
 "JHN.13.27": "Und{1} [nach]{2} [em]{3} [Bisse]{4}, [dänn]{5} [isch]{6} [de Satan]{9,10} [in]{7} [en]{8} [ine gfahre]{6}. [De Jesus]{14,15} [seit]{11} [also]{12} [zu ihm]{13}: «[Was]{16} [du machsch]{17}, [das mach]{18} [schnäll]{19}!»",
 "JHN.13.28": "[Keine]{3} [vo dene]{5} [aber]{2}, [wo am Tisch gläge sind]{6}, [hät verstande]{4}, [für was]{7,8} [er]{9} [ihm]{10} [das]{1} [gseit hät]{9}.",
 "JHN.13.29": "[Es paar]{1} [händ]{3} [nämli]{2} [gmeint]{3}, [wil]{4} [de Judas]{8} [d Kasse]{5,6} [gha hät]{7}, [dass]{9} [de Jesus]{12,13} [zu ihm]{11} [seit]{10}: «[Chauf]{14}, [was]{15} [mer]{17} [für]{18} [s Fäscht]{19,20} [nötig]{16} [händ]{17}!», [oder]{21} [dass]{24} [er]{26} [de Arme]{22,23} [öppis]{25} [söll gää]{26}.",
 "JHN.13.30": "[Dä]{5} [hät]{1} [dänn]{2} [de Bisse]{3,4} [gnoo]{1} und [isch]{6} [sofort]{7} [usegange]{6}. [Es isch]{8} [aber]{9} [Nacht]{10} [gsii]{8}.",
 "JHN.13.31": "[Wo]{1} [er]{3} [dänn]{2} [usegange isch]{3}, [seit]{4} [de Jesus]{5}: «[Jetzt]{6} [isch]{7} [de Mänschesohn]{8-11} [verherrlicht worde]{7}, und{12} [Gott]{13,14} [isch]{15} [in]{16} [ihm]{17} [verherrlicht worde]{15}.",
 "JHN.13.32": "[Wänn]{1} [Gott]{2,3} [in]{5} [ihm]{6} [verherrlicht worde isch]{4}, [wird]{10} [au]{7} [Gott]{8,9} [ihn]{11} [in]{12} [sich sälber]{13} [verherrliche]{10}, und{14} [er wird]{16} [ihn]{17} [grad]{15} [verherrliche]{16}.",
 "JHN.13.33": "[Chinde]{1}, [no]{2} [es Wiili]{3} [bin ich]{6} [bi]{4} [eu]{5}. [Ir wärded]{7} [mich]{8} [sueche]{7}, und{9} [wie]{10} [ich]{11} [de Jude]{12,13} [gseit han]{11}: ‹[Wo]{15} [ich]{16} [hiigaa]{17}, [det chönd]{20} [ir]{18} [nöd]{19} [hiichoo]{21}›, [so säg ich]{24} [jetzt]{25} [au]{22} [eu]{23}. ~14(ὅτι leitet di diräkt Red ii)",
 "JHN.13.34": "[Es nöis]{2} [Gebot]{1} [gib ich]{3} [eu]{4}: [dass]{5} [ir]{6} [enand]{7} [liebed]{6}. [Wie]{8} [ich]{9} [eu]{10} [gliebt han]{9}, [so söled]{11} [au]{12} [ir]{13} [enand]{15} [liebe]{14}.",
 "JHN.13.35": "[Dra]{1,2} [wärded]{3} [alli]{4} [merke]{3}, [dass]{5} [ir]{8} [mini]{6} [Jünger]{7} [sind]{8}: [wänn]{9} [ir]{11} [Liebi]{10} [undernand]{12,13} [händ]{11}.»",
 "JHN.13.36": "[De Simon]{3} [Petrus]{4} [seit]{1} [zu ihm]{2}: «[Herr]{5}, [wo]{6} [gaasch du hii]{7}?» [De Jesus]{9} [hät gantwortet]{8}: «[Wo]{10} [ich hiigaa]{11}, [det chasch du]{13} [mir]{14} [jetzt]{15} [nöd]{12} [nachegaa]{16}; [du wirsch]{17} [aber]{18} [spöter]{19} [nachechoo]{17}.»",
 "JHN.13.37": "[De Petrus]{3,4} [seit]{1} [zu ihm]{2}: «[Herr]{5}, [werum]{6,7} [chan ich]{9} [dir]{10} [jetzt]{12} [nöd]{8} [nachegaa]{11}? [Mis]{15} [Läbe]{13,14} [wirde ich]{18} [für]{16} [dich]{17} [häregää]{18}.»",
 "JHN.13.38": "[De Jesus]{2} [git]{1} [Antwort]{1}: «[Dis]{5} [Läbe]{3,4} [wirsch du]{8} [für]{6} [mich]{7} [häregää]{8}? [Amen]{9}, [amen]{10}, [ich säge]{11} [dir]{12}: [En Güggel]{15} [wird]{16} [nöd]{13,14} [chräie]{16}, [bis]{17,18} [du]{19} [mich]{20} [drüümal]{21} [verleugnet hesch]{19}.»",
}

GRUND = "Grundentscheid für das ganze Evangelium (begründet in scripts/authoring/johannes_text_01_03.py): "
GRUND_GSW = "Grundentscheid fürs ganz Evangelium (begründet in scripts/authoring/johannes_text_01_03.py): "

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("JHN.12.3", "ein Pfund", "literal", "λίτραν", None, ["etwa 330 Gramm"], "λίτρα ist das römische Pfund (libra), etwa 327 Gramm: eine grosse Menge Salböl."),
 ("JHN.12.3", "aus reiner", "interpretive", "νάρδου πιστικῆς", None, ["aus echter", "aus Pistazien-"], "Wie in [[MRK.14.3]]: πιστικός wird meist als «echt, unverfälscht» verstanden; andere leiten es von einem Pflanzennamen ab. Die Bedeutung bleibt unsicher."),
 ("JHN.12.4", "ausliefern", "literal", "παραδιδόναι", None, ["verraten"], "παραδίδωμι heisst «übergeben, ausliefern» und ist wie in der Markus-Übersetzung durchgehend so wiedergegeben ([[JHN.13.2]], [[JHN.13.11]], [[JHN.13.21]]); «verraten» ist die vertraute Wiedergabe bei Judas."),
 ("JHN.12.5", "Denare", "literal", "δηναρίων", None, None, "Ein Denar war der übliche Tageslohn eines Arbeiters (vgl. [[MAT.20.2]]); dreihundert Denare entsprechen ungefähr dem Verdienst eines Jahres."),
 ("JHN.12.6", "die Kasse", "literal", "τὸ γλωσσόκομον", "das Kästchen", ["den Geldbeutel"], "Ein Behälter für das gemeinsame Geld der Gruppe; ebenso [[JHN.13.29]]."),
 ("JHN.12.6", "nahm die Einlagen an sich", "interpretive", "τὰ βαλλόμενα ἐβάσταζεν", "trug das Hineingeworfene", ["trug die Einlagen"], "βαστάζω heisst «tragen», umgangssprachlich auch «wegtragen, entwenden». Im Zusammenhang («er war ein Dieb») liegt dieser Sinn nahe, ist aber nicht sicher."),
 ("JHN.12.7", "damit sie es für den Tag meines Begräbnisses bewahre", "interpretive", "ἵνα εἰς τὴν ἡμέραν τοῦ ἐνταφιασμοῦ μου τηρήσῃ αὐτό", None, ["Sie sollte es für den Tag meines Begräbnisses aufbewahren", "Lass sie es für den Tag meines Begräbnisses aufbewahren"], "Der Satz ist schwierig, weil Maria das Öl schon verwendet hat. Vorgeschlagen wird u. a.: Jesus deutet die Salbung als vorweggenommene Begräbnissalbung; der Rest des Öls soll aufbewahrt werden; ἵνα ist als Aufforderung zu lesen. Die Übersetzung bleibt wörtlich. Zur Lesart «hat sie es bewahrt» siehe Alternative."),
 ("JHN.12.9", "den Juden", "interpretive", "τῶν Ἰουδαίων", None, ["den Judäern", "den Leuten aus Judäa"], GRUND + "οἱ Ἰουδαῖοι wörtlich «die Juden»; das ist eine Deutungsentscheidung, weil das Wort bei Johannes je nach Stelle das jüdische Volk, die Bewohner Judäas oder die führenden Gegner Jesu bezeichnet. Hier ist eine grosse Menge gewöhnlicher Leute gemeint, nicht die Führungsschicht. Ebenso [[JHN.12.11]]."),
 ("JHN.12.11", "der Juden", "interpretive", "τῶν Ἰουδαίων", None, ["der Judäer"], "Wie [[JHN.12.9]]: Leute aus dem Volk, die sich Jesus zuwenden; Grundentscheid «die Juden»."),
 ("JHN.12.11", "weggingen", "interpretive", "ὑπῆγον", None, ["hingingen", "sich abwandten"], "ὑπάγω heisst «weggehen, hingehen». Gemeint sein kann, dass sie nach Betanien hinausgingen, oder dass sie sich von den Hohepriestern lösten."),
 ("JHN.12.13", "Palmzweige", "literal", "τὰ βαΐα τῶν φοινίκων", "die Zweige der Palmen", None, "Palmzweige gehörten zu Festjubel und Siegesfeiern."),
 ("JHN.12.13", "Hosanna", "literal", "Ὡσαννά", None, None, "Griechische Umschrift von hebräisch hôšîʿâ nnāʾ «hilf doch!» ([[PSA.118.25]]); zur Zeit Jesu auch ein Jubelruf. Die folgenden Worte zitieren [[PSA.118.26]]; «und der König Israels» steht nicht im Psalm und bezieht den Ruf auf den König (vgl. [[JHN.1.49]])."),
 ("JHN.12.13", "Gepriesen", "literal", "εὐλογημένος", None, ["Gesegnet"], "εὐλογέω «preisen, segnen»; als Zuruf an einen Menschen «gepriesen, willkommen geheissen»."),
 ("JHN.12.14", "einen jungen Esel", "literal", "ὀνάριον", "ein Eselchen", None, None),
 ("JHN.12.15", "Fürchte dich nicht, Tochter Zion", "literal", "Μὴ φοβοῦ, θυγάτηρ Σιών", None, None, "Freies Zitat von [[ZEC.9.9]] (dort: «Freue dich sehr, Tochter Zion»); «Fürchte dich nicht» erinnert an [[ISA.40.9]] und [[ZEP.3.16]]. «Tochter Zion» ist eine dichterische Bezeichnung für Jerusalem und seine Bewohner."),
 ("JHN.12.16", "verherrlicht worden war", "literal", "ἐδοξάσθη", None, ["verherrlicht wurde"], GRUND + "δόξα/δοξάζω durchgehend «Herrlichkeit/verherrlichen». Hier ist der Weg Jesu durch Tod und Auferweckung zum Vater gemeint (vgl. [[JHN.12.23]], [[JHN.13.31]]); erst danach verstehen die Jünger (vgl. [[JHN.2.22]])."),
 ("JHN.12.18", "Zeichen", "literal", "σημεῖον", None, ["Wunder", "Wunderzeichen"], GRUND + "σημεῖον durchgehend «Zeichen», nicht «Wunder». Gemeint ist die Auferweckung des Lazarus ([[JHN.11.43]]–[[JHN.11.44]]). Ebenso [[JHN.12.37]]."),
 ("JHN.12.19", "die Welt", "literal", "ὁ κόσμος", None, ["alle Welt", "jedermann"], GRUND + "κόσμος durchgehend «Welt». Im Mund der Pharisäer eine Übertreibung («alle Welt»); unmittelbar danach kommen Griechen zu Jesus ([[JHN.12.20]]). Zur Lesart «die ganze Welt» siehe Alternative."),
 ("JHN.12.20", "Griechen", "interpretive", "Ἕλληνές", None, ["Griechischsprachige", "Nichtjuden"], "Meist werden nichtjüdische Menschen griechischer Sprache und Kultur verstanden, die zum Fest kamen, um anzubeten (sogenannte Gottesfürchtige). Dass griechischsprachige Juden gemeint seien, wird seltener vertreten (für sie steht in [[ACT.6.1]] Ἑλληνισταί)."),
 ("JHN.12.23", "die Stunde", "literal", "ἡ ὥρα", None, None, "Bei Johannes die von Gott bestimmte Stunde von Jesu Tod und Verherrlichung; bisher hiess es, sie sei «noch nicht gekommen» ([[JHN.2.4]], [[JHN.7.30]], [[JHN.8.20]]). Ebenso [[JHN.12.27]], [[JHN.13.1]]."),
 ("JHN.12.23", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", ["der Mensch"], "Selbstbezeichnung Jesu, oft mit Anklang an [[DAN.7.13]]; wie in der Markus-Übersetzung «Menschensohn». Ebenso [[JHN.12.34]], [[JHN.13.31]]."),
 ("JHN.12.24", "Amen, amen, ich sage euch", "literal", "ἀμὴν ἀμὴν λέγω ὑμῖν", None, ["Wahrlich, wahrlich, ich sage euch", "Ganz gewiss, ich sage euch"], GRUND + "das verdoppelte ἀμήν, das im Neuen Testament nur bei Johannes vorkommt, bleibt «Amen, amen». Hebräisch ʾāmēn «gewiss, so ist es» bekräftigt hier das Folgende. Ebenso [[JHN.13.16]], [[JHN.13.20]], [[JHN.13.21]], [[JHN.13.38]]."),
 ("JHN.12.24", "bleibt", "literal", "μένει", None, None, GRUND + "μένω durchgehend «bleiben». Ebenso [[JHN.12.34]] und [[JHN.12.46]]."),
 ("JHN.12.25", "sein Leben liebt", "interpretive", "φιλῶν τὴν ψυχὴν αὐτοῦ", None, ["seine Seele liebt", "an seinem Leben hängt"], "ψυχή meint hier das eigene Leben, das Selbst. Davon unterschieden ist ζωή im «ewigen Leben» am Satzende; beides heisst deutsch «Leben». In [[JHN.12.27]] ist ψυχή mit «Seele» wiedergegeben, in [[JHN.13.37]]–[[JHN.13.38]] wieder mit «Leben»."),
 ("JHN.12.25", "hasst", "literal", "μισῶν", None, ["geringer achtet", "zurückstellt"], "«Lieben – hassen» ist eine semitische Gegenüberstellung im Sinn von «vorziehen – zurückstellen» (vgl. [[LUK.14.26]] mit [[MAT.10.37]]); der Satz fordert nach verbreitetem Verständnis nicht zum Selbsthass auf."),
 ("JHN.12.27", "erschüttert", "literal", "τετάρακται", None, ["aufgewühlt", "verstört"], "ταράσσω «aufwühlen, erschüttern»; wie in [[JHN.11.33]] und [[JHN.13.21]]. Anklang an die Klage in [[PSA.6.3]] und [[PSA.42.6]] (in der Septuaginta mit demselben Verb)."),
 ("JHN.12.27", "Vater, rette mich aus dieser Stunde", "interpretive", "πάτερ, σῶσόν με ἐκ τῆς ὥρας ταύτης", None, ["Vater, rette mich aus dieser Stunde!"], "Die Satzzeichen sind nicht überliefert. Als Frage gelesen erwägt Jesus diese Bitte und verwirft sie; als Ausruf ist es ein wirkliches Gebet (vgl. [[MRK.14.36]]), das er dann dem «Verherrliche deinen Namen» unterordnet. Redaktionelle Entscheidung für die Frage, wie in vielen Ausgaben."),
 ("JHN.12.28", "Ich habe ihn schon verherrlicht", "adapted", "Καὶ ἐδόξασα", "Und ich habe verherrlicht", ["Ich habe ihn verherrlicht"], "καί … καί heisst «sowohl … als auch»; das Objekt «ihn» (den Namen) ist ergänzt. Worauf sich das Verherrlichen in der Vergangenheit bezieht, sagt der Text nicht; oft wird an das bisherige Wirken und die Zeichen Jesu gedacht (vgl. [[JHN.11.4]], [[JHN.11.40]])."),
 ("JHN.12.31", "der Herrscher dieser Welt", "literal", "ὁ ἄρχων τοῦ κόσμου τούτου", None, ["der Fürst dieser Welt"], "Meist auf den Satan als Gegenmacht bezogen (vgl. [[JHN.14.30]], [[JHN.16.11]])."),
 ("JHN.12.32", "erhöht bin", "literal", "ὑψωθῶ", None, ["erhoben werde"], GRUND + "ὑψόω durchgehend «erhöhen». Das Wort kann das Aufgerichtetwerden am Kreuz und die Erhöhung zu Gott meinen; Johannes nennt den ersten Sinn ausdrücklich ([[JHN.12.33]]; vgl. [[JHN.3.14]], [[JHN.8.28]] und [[ISA.52.13]], wo die griechische Bibel dasselbe Verb hat)."),
 ("JHN.12.32", "alle", "literal", "πάντας", None, ["alle Menschen"], "πάντας ist maskulin: «alle» (Menschen); der Text schränkt es nicht ein. Wie weit «alle» reicht, wird verschieden gedeutet."),
 ("JHN.12.34", "dem Gesetz", "interpretive", "τοῦ νόμου", None, ["der Schrift"], "νόμος meint hier die Schrift im Ganzen, nicht nur die fünf Bücher Mose (vgl. [[JHN.10.34]]). Welche Stelle gemeint ist, sagt der Text nicht; erwogen werden u. a. [[PSA.89.36]], [[PSA.110.4]], [[ISA.9.7]] und [[EZK.37.25]]."),
 ("JHN.12.34", "der Christus", "traditional", "ὁ χριστὸς", None, ["der Messias", "der Gesalbte"], "χριστός übersetzt hebräisch māšîaḥ «Gesalbter»; Johannes nennt das hebräische Wort selbst in [[JHN.1.41]]."),
 ("JHN.12.35", "Geht euren Weg", "adapted", "περιπατεῖτε", "Wandelt", ["Lebt"], "περιπατέω «umhergehen» steht bildlich für die Lebensführung; im Bild des Satzes ist aber das Gehen im Licht oder im Dunkeln gemeint."),
 ("JHN.12.35", "solange", "interpretive", "ὡς", "wie", ["während"], "ὡς hat hier zeitlichen Sinn «solange, während». Einige Handschriften und Ausgaben haben ἕως «solange» (VAR-SBLGNTAPP-JHN-012-035-02); an der Übersetzung ändert das nichts. Ebenso [[JHN.12.36]]."),
 ("JHN.12.35", "überfällt", "interpretive", "καταλάβῃ", None, ["überwältigt", "ergreift"], "Dasselbe Verb wie in [[JHN.1.5]] (die Finsternis und das Licht)."),
 ("JHN.12.36", "Söhne des Lichts", "literal", "υἱοὶ φωτὸς", None, ["Kinder des Lichts", "Menschen des Lichts"], "Semitische Wendung: «Sohn von etwas» bezeichnet Zugehörigkeit; gemeint sind Menschen, die zum Licht gehören (vgl. [[LUK.16.8]], [[1TH.5.5]]). υἱοί schliesst Frauen ein."),
 ("JHN.12.37", "Zeichen", "literal", "σημεῖα", None, ["Wunder"], "Grundentscheid «Zeichen» wie in [[JHN.12.18]]."),
 ("JHN.12.38", "Herr, wer hat unserer Botschaft geglaubt?", "literal", "Κύριε, τίς ἐπίστευσεν τῇ ἀκοῇ ἡμῶν;", None, None, "Zitat von [[ISA.53.1]] im Wortlaut der griechischen Übersetzung (Septuaginta), die die Anrede «Herr» enthält; die Anführungszeichen machen das Zitat kenntlich. ἀκοή heisst «das Gehörte», die Botschaft, die man gehört hat. Der «Arm des Herrn» steht für Gottes machtvolles Handeln."),
 ("JHN.12.39", "wiederum", "literal", "πάλιν", None, ["an anderer Stelle"], "Leitet das zweite Jesajazitat ein ([[JHN.12.40]])."),
 ("JHN.12.40", "Er hat ihre Augen geblendet", "interpretive", "Τετύφλωκεν αὐτῶν τοὺς ὀφθαλμοὺς", None, ["Er hat ihre Augen blind gemacht"], "Zitat von [[ISA.6.10]], frei und gekürzt, weder genau nach dem hebräischen Text noch nach der Septuaginta; die Anführungszeichen machen es kenntlich. Bei Jesaja erhält der Prophet den Auftrag, die Herzen zu verstocken; hier ist das Subjekt nicht genannt (meist auf Gott bezogen, von manchen auf den Satan, vgl. [[2CO.4.4]]). Wie sich Gottes Handeln und die Verantwortung der Menschen hier zueinander verhalten, wird verschieden gedeutet; [[JHN.12.42]] sagt zugleich, dass viele doch glaubten."),
 ("JHN.12.40", "und ich werde sie heilen", "interpretive", "καὶ ἰάσομαι αὐτούς", None, ["und ich sie heile"], "ἰάσομαι ist Futur Indikativ. Es kann noch zum Zweck gehören («damit sie nicht … umkehren und ich sie heile») oder als eigener Satz gelesen werden. Die Übersetzung gibt das Futur wieder; zur Lesart im Konjunktiv siehe Alternative."),
 ("JHN.12.41", "seine Herrlichkeit", "interpretive", "τὴν δόξαν αὐτοῦ", None, ["die Herrlichkeit Gottes"], "Im Zusammenhang meist auf Jesus bezogen: Johannes liest die Tempelvision [[ISA.6.1]]–[[ISA.6.5]] als Schau seiner Herrlichkeit (vgl. [[JHN.1.14]]). Andere beziehen αὐτοῦ auf Gott."),
 ("JHN.12.42", "Oberen", "interpretive", "ἀρχόντων", None, ["Ratsherren", "führenden Männern"], "Wohl Mitglieder der jüdischen Führungsschicht in Jerusalem (vgl. [[JHN.3.1]], [[JHN.7.48]])."),
 ("JHN.12.42", "aus der Synagoge ausgeschlossen", "literal", "ἀποσυνάγωγοι", None, None, "Wie in [[JHN.9.22]] und [[JHN.16.2]]. Wie weit dies die Lage zur Zeit Jesu oder die der ersten Leserschaft spiegelt, ist umstritten (vgl. CTX-JHN-READERS-0095)."),
 ("JHN.12.43", "die Ehre", "adapted", "τὴν δόξαν", None, ["die Herrlichkeit", "das Ansehen"], "Ausnahme vom Grundentscheid «Herrlichkeit»: δόξα meint hier Ansehen, Anerkennung (vgl. [[JHN.5.44]]). Johannes spielt mit dem Wort, das in [[JHN.12.41]] die «Herrlichkeit» bezeichnet. Der Genitiv kann «Ehre bei Gott» oder «Ehre von Gott» heissen."),
 ("JHN.12.44", "rief laut", "literal", "ἔκραξεν", None, ["rief"], "Feierliche Ausrufung wie in [[JHN.7.28]], [[JHN.7.37]]. Wann und wo diese Worte gesprochen wurden, sagt der Text nicht; nach [[JHN.12.36]] hatte sich Jesus verborgen."),
 ("JHN.12.47", "bewahrt", "literal", "φυλάξῃ", None, ["befolgt", "hält"], "Zur Lesart «nicht glaubt» siehe Alternative."),
 ("JHN.12.47", "richte", "literal", "κρίνω", None, ["verurteile"], "κρίνω heisst «richten, urteilen», oft mit dem Ausgang der Verurteilung (vgl. [[JHN.3.17]]). Ebenso [[JHN.12.48]]."),
 ("JHN.12.48", "Das Wort", "literal", "ὁ λόγος", None, None, GRUND + "λόγος «Wort». Hier ist die Rede Jesu als Ganze gemeint; die Mehrzahl ῥήματα ist mit «Worte» wiedergegeben."),
 ("JHN.12.49", "ein Gebot", "literal", "ἐντολὴν", None, ["einen Auftrag"], "ἐντολή «Gebot, Auftrag»; wörtlich belassen wegen [[JHN.12.50]] und [[JHN.13.34]]."),
 ("JHN.13.1", "die Seinen", "literal", "τοὺς ἰδίους", None, None, "Vgl. [[JHN.1.11]]."),
 ("JHN.13.1", "bis zur Vollendung", "interpretive", "εἰς τέλος", "bis zum Ende", ["bis ans Ende", "bis zum Äussersten", "ganz und gar"], "εἰς τέλος heisst zeitlich «bis zum Ende» und dem Grad nach «völlig». Oft wird angenommen, Johannes meine beides; vgl. τετέλεσται «es ist vollbracht» ([[JHN.19.30]])."),
 ("JHN.13.2", "als das Mahl im Gang war", "interpretive", "δείπνου γινομένου", "als ein Mahl geschah", ["während des Mahls"], "Partizip Präsens: während des Mahls. Zur Lesart γενομένου siehe Alternative."),
 ("JHN.13.2", "der Teufel hatte schon ins Herz gegeben", "interpretive", "τοῦ διαβόλου ἤδη βεβληκότος εἰς τὴν καρδίαν", "der Teufel hatte schon in das Herz geworfen", ["der Teufel hatte es Judas schon ins Herz gelegt", "der Teufel hatte schon beschlossen"], "Wessen Herz gemeint ist, sagt der SBLGNT-Text nicht ausdrücklich. Meist wird es auf Judas bezogen; grammatisch möglich ist auch, dass der Teufel es sich selbst vorgenommen hatte. Die Übersetzung lässt das offen."),
 ("JHN.13.2", "Sohn des Simon", "adapted", "Σίμωνος", "des Simon", None, "«Sohn» ist ergänzt. Im SBLGNT steht Ἰσκαριώτου im Genitiv und gehört damit zu Simon (wie in [[JHN.6.71]] und [[JHN.13.26]]); zur Lesart Ἰσκαριώτης siehe Alternative."),
 ("JHN.13.4", "die Obergewänder", "interpretive", "τὰ ἱμάτια", "die Kleider", ["das Obergewand"], "ἱμάτια (Mehrzahl) bezeichnet die Oberkleidung. Dieselben Verben τίθημι «ablegen» und λαμβάνω «nehmen» ([[JHN.13.12]]) stehen in [[JHN.10.17]]–[[JHN.10.18]] für das Hingeben und Wiedernehmen des Lebens; ob Johannes darauf anspielt, ist eine Deutungsfrage."),
 ("JHN.13.4", "ein Leinentuch", "literal", "λέντιον", None, ["einen Schurz", "ein Handtuch"], "Lateinisches Lehnwort (linteum): ein Leinentuch, wie es Diener umgebunden trugen."),
 ("JHN.13.8", "Nie in Ewigkeit", "literal", "Οὐ μὴ εἰς τὸν αἰῶνα", None, ["Niemals"], "οὐ μή ist die stärkste Verneinung; εἰς τὸν αἰῶνα verstärkt sie noch."),
 ("JHN.13.8", "Anteil an mir", "adapted", "μέρος μετʼ ἐμοῦ", "Teil mit mir", ["Gemeinschaft mit mir"], "μέρος «Anteil» erinnert an den Erbanteil; gemeint ist Teilhabe an Jesus und an dem, was er gibt."),
 ("JHN.13.10", "Wer gebadet ist", "interpretive", "Ὁ λελουμένος", None, ["Wer ein Bad genommen hat"], "λούομαι «baden» (den ganzen Körper) unterscheidet sich von νίπτω «(einen Teil) waschen». Ob das Bad auf die Taufe, auf die Reinigung durch Jesu Wort (vgl. [[JHN.15.3]]) oder auf Gastsitte anspielt, wird verschieden gedeutet. Textbefund: Die Worte «ausser an den Füssen» (εἰ μὴ τοὺς πόδας) stehen im SBLGNT. Nach der CNTR-Transkription fehlen sie in 01 (dort: οὐκ ἔχει χρείαν νίψασθαι, «hat nicht nötig, sich zu waschen»); 05 liest «hat nicht nötig, den Kopf zu waschen, ausser nur die Füsse», 𝔓66 hat ebenfalls μόνον «nur». Der SBLGNT-Apparat verzeichnet diese Unterschiede nicht (nur εἰ μή / ἤ ohne Sinnunterschied); die Angaben stützen sich auf die Transkriptionen."),
 ("JHN.13.13", "der Lehrer", "literal", "Ὁ διδάσκαλος", None, None, "Nominativ mit Artikel: die Anrede wird als Titel zitiert (vgl. «Rabbi», übersetzt «Lehrer», in [[JHN.1.38]])."),
 ("JHN.13.14", "verpflichtet", "literal", "ὀφείλετε", "schuldig", None, None),
 ("JHN.13.15", "ein Beispiel", "literal", "ὑπόδειγμα", None, ["ein Vorbild"], None),
 ("JHN.13.16", "Ein Knecht", "traditional", "δοῦλος", "Ein Sklave", ["Ein Diener"], None),
 ("JHN.13.16", "ein Gesandter", "literal", "ἀπόστολος", None, ["ein Apostel", "ein Bote"], "Das einzige Vorkommen von ἀπόστολος im Johannesevangelium (per Skript aus den SBLGNT-Tokens geprüft); hier im allgemeinen Sinn «Gesandter»."),
 ("JHN.13.17", "Selig", "traditional", "μακάριοί", None, ["Glücklich", "Wohl euch"], None),
 ("JHN.13.18", "Aber es geschieht, damit", "adapted", "ἀλλʼ ἵνα", "Aber damit", None, "Der griechische Satz ist verkürzt; «es geschieht» ist ergänzt (wie in [[MRK.14.49]])."),
 ("JHN.13.18", "Der mein Brot isst, hat gegen mich seine Ferse erhoben", "literal", "Ὁ τρώγων μου τὸν ἄρτον ἐπῆρεν ἐπʼ ἐμὲ τὴν πτέρναν αὐτοῦ", None, ["hat gegen mich getreten"], "Zitat von [[PSA.41.9]] (im hebräischen und griechischen Psalter ein Vers später gezählt), nicht im Wortlaut der Septuaginta. «Die Ferse erheben» ist ein Bild für hinterhältigen Angriff oder Verachtung durch einen Tischgenossen. τρώγω «kauen, essen» steht auch in [[JHN.6.54]]–[[JHN.6.58]]."),
 ("JHN.13.19", "dass ich bin", "interpretive", "ὅτι ἐγώ εἰμι", None, ["dass ich es bin", "dass ich der bin"], GRUND + "ἐγώ εἰμι durchgehend «ich bin». Ohne Ergänzung (wie hier und in [[JHN.8.24]], [[JHN.8.28]], [[JHN.8.58]]) klingt die Selbstvorstellung Gottes in der Septuaginta an, besonders [[ISA.43.10]] (ἵνα … πιστεύσητε … ὅτι ἐγώ εἰμι, «damit ihr … glaubt, dass ich bin»). Man kann auch ergänzen «dass ich es bin» (der, von dem die Schrift spricht); das ist ebenfalls eine Deutung."),
 ("JHN.13.21", "erschüttert", "literal", "ἐταράχθη", None, ["aufgewühlt"], "Wie [[JHN.12.27]]."),
 ("JHN.13.23", "an der Brust", "interpretive", "ἐν τῷ κόλπῳ", "im Schoss", ["an der Seite"], "Beim Festmahl lag man auf Polstern, auf den linken Arm gestützt; wer rechts neben einem lag, hatte den Kopf auf der Höhe von dessen Brust. Dieselbe Wendung beschreibt in [[JHN.1.18]] die Nähe des Sohnes zum Vater."),
 ("JHN.13.23", "den Jesus liebte", "literal", "ὃν ἠγάπα ὁ Ἰησοῦς", None, None, "Hier erscheint erstmals der «Jünger, den Jesus liebte» (vgl. [[JHN.19.26]], [[JHN.20.2]], [[JHN.21.7]], [[JHN.21.20]]–[[JHN.21.24]]). Der Text nennt seinen Namen nicht; die Gleichsetzung mit Johannes, dem Sohn des Zebedäus, ist eine alte, aber umstrittene Überlieferung."),
 ("JHN.13.26", "den Bissen", "literal", "τὸ ψωμίον", None, ["das Stück Brot"], "Ein Stück Brot, in die Schüssel getaucht. Einem Tischgenossen einen Bissen zu reichen, konnte eine Geste der Ehre sein; vgl. das Zitat in [[JHN.13.18]]."),
 ("JHN.13.27", "der Satan", "literal", "ὁ Σατανᾶς", None, None, "Das einzige Vorkommen des Namens Σατανᾶς im Johannesevangelium (per Skript geprüft); vgl. «der Teufel» in [[JHN.13.2]]."),
 ("JHN.13.27", "schnell", "literal", "τάχιον", "schneller", ["bald"], None),
 ("JHN.13.30", "Nacht", "literal", "νύξ", None, None, "Zeitangabe; Nacht und Finsternis sind bei Johannes auch Bilder (vgl. [[JHN.9.4]], [[JHN.11.10]], [[JHN.12.35]]). Ob er hier über die Zeitangabe hinaus etwas andeuten will, wird verschieden gesehen."),
 ("JHN.13.31", "Jetzt ist der Menschensohn verherrlicht worden", "literal", "Νῦν ἐδοξάσθη ὁ υἱὸς τοῦ ἀνθρώπου", None, ["Jetzt wurde der Menschensohn verherrlicht"], "Aorist: Jesus spricht von der beginnenden Verherrlichung, als sei sie schon geschehen; [[JHN.13.32]] fährt im Futur fort."),
 ("JHN.13.32", "in sich selbst", "interpretive", "ἐν αὑτῷ", None, ["in ihm"], "Der SBLGNT liest αὑτῷ (mit Hauchzeichen: «in sich selbst», also in Gott), NA28 und Treg lesen αὐτῷ «in ihm» (in Jesus). Die frühen Handschriften haben keine Hauchzeichen; die Unterscheidung ist eine Entscheidung der Herausgeber. 02, 04 und 05 haben nach der automatischen Zuordnung ἑαυτῷ «in sich selbst»."),
 ("JHN.13.33", "Kinder", "literal", "τεκνία", "Kindlein", ["meine Kinder"], "Verkleinerungsform; im Johannesevangelium nur hier (per Skript geprüft), im 1. Johannesbrief öfter (z. B. [[1JN.2.1]])."),
 ("JHN.13.33", "zu den Juden", "interpretive", "τοῖς Ἰουδαίοις", None, ["zu den Judäern", "zu den jüdischen Führern"], GRUND + "«die Juden» (siehe [[JHN.12.9]]). Jesus verweist auf [[JHN.7.33]]–[[JHN.7.34]] und [[JHN.8.21]]; dort antworten «die Juden» ([[JHN.7.35]], [[JHN.8.22]]), im Zusammenhang vor allem Gegner Jesu in Jerusalem."),
 ("JHN.13.34", "Ein neues", "literal", "καινὴν", None, None, "Was an dem Gebot «neu» ist, wird verschieden bestimmt: der Massstab «wie ich euch geliebt habe», die Ausrichtung auf die Gemeinschaft der Jünger oder der Zusammenhang mit dem neuen Bund. Das Gebot der Nächstenliebe steht schon in [[LEV.19.18]]."),
 ("JHN.13.34", "so sollt auch ihr einander lieben", "adapted", "ἵνα καὶ ὑμεῖς ἀγαπᾶτε ἀλλήλους", "damit auch ihr einander liebt", ["dass auch ihr einander liebt"], "Das zweite ἵνα nimmt das erste auf. Der Satz kann auch heissen «wie ich euch geliebt habe, damit auch ihr einander liebt» (die Liebe Jesu als Grund und Ermöglichung)."),
 ("JHN.13.37", "hingeben", "literal", "θήσω", "legen", ["einsetzen"], "τίθημι τὴν ψυχήν «das Leben hinlegen» wie beim guten Hirten ([[JHN.10.11]], [[JHN.10.15]]); Jesus nimmt die Wendung in [[JHN.13.38]] auf."),
 ("JHN.13.38", "Ein Hahn wird nicht krähen", "literal", "οὐ μὴ ἀλέκτωρ φωνήσῃ", None, None, "Vgl. [[MRK.14.30]]; Johannes erzählt die Verleugnung in [[JHN.18.15]]–[[JHN.18.27]]."),
]

DEC_GSW = [
 ("JHN.12.3", "es Pfund", "literal", "λίτραν", None, None, "λίτρα isch s römisch Pfund, öppe 327 Gramm."),
 ("JHN.12.4", "uslifere", "literal", "παραδιδόναι", None, ["verrate"], "παραδίδωμι heisst «übergää, uslifere», wie i de Markus-Übersetzig überall «uslifere»."),
 ("JHN.12.6", "hät das, wo inegleit worde isch, für sich gnoo", "interpretive", "τὰ βαλλόμενα ἐβάσταζεν", "hät das, wo inegleit worde isch, treit", None, "βαστάζω heisst «träge», umgangssprachlich au «wägnää, stäle»; im Zämehang liit das nööch, isch aber nöd sicher."),
 ("JHN.12.7", "demit si s für de Tag vo mim Begräbnis ufbhaltet", "interpretive", "ἵνα τηρήσῃ αὐτό", None, ["Si hett s für de Tag vo mim Begräbnis söle ufbhalte"], "De Satz isch schwirig, wil d Maria s Öl scho bruucht hät. Mer deutet en verschide; d Übersetzig bliibt wörtlich. Lueg au d Alternative."),
 ("JHN.12.9", "de Jude", "interpretive", "τῶν Ἰουδαίων", None, ["de Judäer", "de Lüüt us Judäa"], GRUND_GSW + "οἱ Ἰουδαῖοι wörtlich «d Jude». Das isch e Deutigsentscheid, wil s Wort bim Johannes je nach Stell s jüdisch Volk, d Lüüt us Judäa oder d füerende Gägner vom Jesus meint. Da isch e grossi Mängi vo gwöhnliche Lüüt gmeint. Gliich [[JHN.12.11]] und [[JHN.13.33]]."),
 ("JHN.12.13", "Hosanna", "literal", "Ὡσαννά", None, None, "Hebräisch hôšîʿâ nnāʾ «hilf doch!» ([[PSA.118.25]]), zur Ziit vom Jesus au en Jubelruef. Wiiter mit Wort us [[PSA.118.26]]."),
 ("JHN.12.15", "Fürcht di nöd, Tochter Zion", "literal", "Μὴ φοβοῦ, θυγάτηρ Σιών", None, None, "Frei zitiert us [[ZEC.9.9]]; «Tochter Zion» isch Jerusalem."),
 ("JHN.12.16", "verherrlicht worde isch", "literal", "ἐδοξάσθη", None, None, GRUND_GSW + "δόξα/δοξάζω überall «Herrlichkeit/verherrliche»."),
 ("JHN.12.18", "Zeiche", "literal", "σημεῖον", None, ["Wunder"], GRUND_GSW + "σημεῖον überall «Zeiche», nöd «Wunder»."),
 ("JHN.12.19", "d Wält", "literal", "ὁ κόσμος", None, ["alli Wält"], GRUND_GSW + "κόσμος überall «Wält»."),
 ("JHN.12.23", "de Mänschesohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None, "Wie i de Markus-Übersetzig; Aaklang a [[DAN.7.13]]."),
 ("JHN.12.24", "Amen, amen, ich säge eu", "literal", "ἀμὴν ἀμὴν λέγω ὑμῖν", None, ["Würkli, würkli, ich säge eu"], GRUND_GSW + "s doppelt ἀμήν bliibt «Amen, amen»."),
 ("JHN.12.24", "bliibt", "literal", "μένει", None, None, GRUND_GSW + "μένω überall «bliibe»."),
 ("JHN.12.27", "Vatter, rett mich us dere Stund", "interpretive", "πάτερ, σῶσόν με ἐκ τῆς ὥρας ταύτης", None, ["Vatter, rett mich us dere Stund!"], "D Satzzeiche sind nöd überliferet: Frag oder würklichs Gebätt. Redaktionelle Entscheid für d Frag."),
 ("JHN.12.32", "erhöcht bi", "literal", "ὑψωθῶ", None, None, GRUND_GSW + "ὑψόω überall «erhöche»: as Chrüüz ufgrichtet und zu Gott erhöcht; de Johannes säit de erscht Sinn usdrücklich ([[JHN.12.33]])."),
 ("JHN.12.38", "Herr, wer hät öisere Botschaft glaubt?", "literal", "Κύριε, τίς ἐπίστευσεν τῇ ἀκοῇ ἡμῶν;", None, None, "Zitat us [[ISA.53.1]] nach de griechische Übersetzig (Septuaginta); d Aafüerigszeiche mached s Zitat kenntlich."),
 ("JHN.12.40", "Er hät ire Auge blind gmacht", "interpretive", "Τετύφλωκεν αὐτῶν τοὺς ὀφθαλμοὺς", None, None, "Frei und gchürzt zitiert us [[ISA.6.10]]. Wer s Subjekt isch, staat nöd; meischt bezieht mer s uf Gott. Wie Gottes Handle und d Verantwortig vo de Mänsche zämegönd, wird verschide deutet."),
 ("JHN.12.40", "und ich wirde si heile", "interpretive", "καὶ ἰάσομαι αὐτούς", None, ["und ich si heile"], "ἰάσομαι isch Futur; mer cha s au no zum Zwäck zelle. Lueg d Alternative."),
 ("JHN.12.43", "d Ehr", "adapted", "τὴν δόξαν", None, ["d Herrlichkeit"], "Usnaam vom Grundentscheid: δόξα meint da Aasee, Anerchännig; de Johannes spilt aber mit em Wort us [[JHN.12.41]]."),
 ("JHN.13.1", "bis zur Vollendig", "interpretive", "εἰς τέλος", "bis zum Änd", ["ganz und gar"], "εἰς τέλος cha «bis as Änd» und «ganz und gar» heisse."),
 ("JHN.13.2", "de Tüüfel hät scho is Härz gleit", "interpretive", "τοῦ διαβόλου ἤδη βεβληκότος εἰς τὴν καρδίαν", None, ["de Tüüfel hät s em Judas scho is Härz gleit"], "Wessen Härz gmeint isch, säit de SBLGNT-Text nöd usdrücklich; meischt bezieht mer s uf de Judas."),
 ("JHN.13.8", "im Läbe", "adapted", "εἰς τὸν αἰῶνα", "in Ewigkeit", None, "Mundartlichi Verstärkig vo de Verneinig."),
 ("JHN.13.10", "Wer badet hät", "interpretive", "Ὁ λελουμένος", None, None, "λούομαι «bade» (de ganz Liib) und νίπτω «(en Teil) wäsche». «Ussert a de Füess» staat im SBLGNT; nach de CNTR-Transkription fäält s in 01, und 05 hät «de Chopf wäsche, ussert nu d Füess»."),
 ("JHN.13.16", "en Gsandte", "literal", "ἀπόστολος", None, ["en Apostel"], "S einzig ἀπόστολος im Johannesevangelium."),
 ("JHN.13.18", "Dä, wo mis Broot isst, hät gäge mich sini Färse glüpft", "literal", "Ὁ τρώγων μου τὸν ἄρτον ἐπῆρεν ἐπʼ ἐμὲ τὴν πτέρναν αὐτοῦ", None, None, "Zitat us [[PSA.41.9]]; «d Färse lüpfe» isch es Bild für en hinderhältige Aagriff vom ene Tischgnoss."),
 ("JHN.13.19", "dass ich bi", "interpretive", "ὅτι ἐγώ εἰμι", None, ["dass ich s bi"], GRUND_GSW + "ἐγώ εἰμι überall «ich bi». Ohni Ergänzig klingt Gottes Sälbervorstellig us [[ISA.43.10]] aa."),
 ("JHN.13.23", "a de Bruscht", "interpretive", "ἐν τῷ κόλπῳ", "im Schoss", None, "Bim Feschtässe isch mer uf Polschter gläge; wer rächts näbem andere gläge isch, hät de Chopf uf de Höchi vo sinere Bruscht gha."),
 ("JHN.13.33", "Chinde", "literal", "τεκνία", "Chindli", None, None),
 ("JHN.13.37", "häregää", "literal", "θήσω", "härelegge", None, "Wie bim guete Hirt ([[JHN.10.11]])."),
 ("JHN.13.38", "En Güggel", "adapted", "ἀλέκτωρ", "En Hahn", None, None),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-JHN-012-001-01:R2", "JHN.12.1", "wo Lazarus war", "wo Lazarus war, der Verstorbene", "wo de Lazarus gsii isch", "wo de Lazarus gsii isch, dä, wo gstorbe gsii isch", "gering",
  "Mit dem Zusatz ὁ τεθνηκώς «der Verstorbene» (Treg, RP).", "Mit em Zuesatz ὁ τεθνηκώς «dä, wo gstorbe gsii isch» (Treg, RP).",
  {"R1": [("Λάζαρος", "Lazarus", "WH, NA28")], "R2": [("Λάζαρος ὁ τεθνηκώς", "Lazarus, der Verstorbene", "Treg, RP")]},
  {"R1": [("Λάζαρος", "Lazarus", "WH, NA28")], "R2": [("Λάζαρος ὁ τεθνηκώς", "Lazarus, wo gstorbe gsii isch", "Treg, RP")]},
  ["Der Zusatz erinnert an [[JHN.11.39]] und [[JHN.11.44]]; er kann als Verdeutlichung ergänzt oder als überflüssig weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 032 ohne Zusatz, 02, 05 und 𝔓66 mit ihm; 𝔓75 ist hier nicht erhalten."],
  ["De Zuesatz erinneret a [[JHN.11.39]] und [[JHN.11.44]]; er cha als Verdüütlichig ergänzt oder als überflüssig wäggloo worde sii.",
   "Nach de automatische Zueornig läsed 01, 03 und 032 ohni Zuesatz, 02, 05 und 𝔓66 mit; 𝔓75 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-JHN-012-007-02:R2", "JHN.12.7", "damit sie es für den Tag meines Begräbnisses bewahre", "für den Tag meines Begräbnisses hat sie es bewahrt",
  "demit si s für de Tag vo mim Begräbnis ufbhaltet", "für de Tag vo mim Begräbnis hät si s ufbhalte", "mittel",
  "τετήρηκεν «sie hat bewahrt» statt τηρήσῃ «sie bewahre»; im Mehrheitstext (RP) fehlt zugleich ἵνα «damit» (VAR-SBLGNTAPP-JHN-012-007-01). So gelesen deutet Jesus die eben geschehene Salbung als Begräbnissalbung.",
  "τετήρηκεν «si hät ufbhalte» statt τηρήσῃ «si söll ufbhalte»; im Mehrheitstext (RP) fäält au ἵνα «demit». So gläse deutet de Jesus d Salbig, wo grad passiert isch, als Salbig fürs Begräbnis.",
  {"R1": [("ἵνα … τηρήσῃ", "damit sie bewahre", "WH, Treg, NA28")], "R2": [("τετήρηκεν", "hat sie bewahrt", "RP (ohne ἵνα)")]},
  {"R1": [("ἵνα … τηρήσῃ", "demit si ufbhaltet", "WH, Treg, NA28")], "R2": [("τετήρηκεν", "hät si ufbhalte", "RP (ohni ἵνα)")]},
  ["Die Perfektform glättet die Schwierigkeit, dass Maria das Öl schon verwendet hat; deshalb wird sie oft als spätere Erleichterung beurteilt.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 05, 𝔓66 und 𝔓75 τηρήσῃ; 02 hat τετήρηκεν und lässt auch ἵνα weg."],
  ["D Perfektform macht de Satz eifacher, wil d Maria s Öl scho bruucht hät; drum gilt si oft als spööteri Erliichterig.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 05, 𝔓66 und 𝔓75 τηρήσῃ; 02 hät τετήρηκεν und laat au ἵνα wäg."]),
 ("VAR-SBLGNTAPP-JHN-012-013-02:R2", "JHN.12.13", "und der König Israels", "der König Israels", "und de König vo Israel", "de König vo Israel", "gering",
  "Ohne «und»: «der König Israels» wird zur Apposition zu «der da kommt».", "Ohni «und»: «de König vo Israel» erklärt, wer «dä, wo chunnt» isch.",
  {"R1": [("καὶ ὁ βασιλεὺς", "und der König", "WH, Treg, NA28")], "R2": [("βασιλεὺς", "König", "RP")]},
  {"R1": [("καὶ ὁ βασιλεὺς", "und de König", "WH, Treg, NA28")], "R2": [("βασιλεὺς", "König", "RP")]},
  ["Das «und» kann ausgefallen oder als holprig gestrichen worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 𝔓75 mit καὶ ὁ; 02 ohne beides; 05 und 𝔓66 haben im erfassten Wortlaut ὁ βασιλεύς ohne καί (beide werden bei R2 geführt)."],
  ["S «und» cha usgfalle oder als holperig gstriche worde sii.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 𝔓75 mit καὶ ὁ; 02 ohni beides; 05 und 𝔓66 händ ὁ βασιλεύς ohni καί."]),
 ("VAR-SBLGNTAPP-JHN-012-019-01:R2", "JHN.12.19", "die Welt", "die ganze Welt", "d Wält", "di ganz Wält", "gering",
  "Mit ὅλος «ganz».", "Mit ὅλος «ganz».",
  {"R1": [("ὁ κόσμος", "die Welt", "WH, Treg, RP, NA28")], "R2": [("ὁ κόσμος ὅλος", "die ganze Welt", "NIV")]},
  {"R1": [("ὁ κόσμος", "d Wält", "WH, Treg, RP, NA28")], "R2": [("ὁ κόσμος ὅλος", "di ganz Wält", "NIV")]},
  ["Der Zusatz verstärkt die Übertreibung der Pharisäer.",
   "Laut der automatischen Zuordnung hat unter den erfassten Handschriften nur 05 ὅλος; 01, 02, 03, 032, 𝔓66 und 𝔓75 lesen ohne."],
  ["De Zuesatz verstärkt d Übertriibig vo de Pharisäer.",
   "Nach de automatische Zueornig hät under de erfasste Handschrifte nu 05 ὅλος."]),
 ("VAR-SBLGNTAPP-JHN-012-025-01:R2", "JHN.12.25", "verliert", "wird verlieren", "verlüürt", "wird verlüüre", "gering",
  "Futur ἀπολέσει statt Präsens ἀπολλύει.", "Futur ἀπολέσει statt Präsens ἀπολλύει.",
  {"R1": [("ἀπολλύει", "verliert", None)], "R2": [("ἀπολέσει", "wird verlieren", "RP")]},
  {"R1": [("ἀπολλύει", "verlüürt", None)], "R2": [("ἀπολέσει", "wird verlüüre", "RP")]},
  ["Das Futur kann an das folgende φυλάξει «wird bewahren» und an die Parallelen ([[MAT.10.39]], [[LUK.17.33]]) angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 05 (Erstschrift), 𝔓66 und 𝔓75 ἀπολλύει; 02 und die Korrektur in 05 ἀπολέσει."],
  ["S Futur cha as folgend φυλάξει und a d Parallele ([[MAT.10.39]], [[LUK.17.33]]) aaglichen sii.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 05, 𝔓66 und 𝔓75 ἀπολλύει; 02 und d Korrektur in 05 ἀπολέσει."]),
 ("VAR-SBLGNTAPP-JHN-012-040-03:R2", "JHN.12.40", "und ich werde sie heilen", "und ich sie heile", "und ich wirde si heile", "und ich si heile", "gering",
  "Konjunktiv ἰάσωμαι: das Heilen gehört dann sicher noch zum «damit nicht».", "Konjunktiv ἰάσωμαι: s Heile ghört dänn sicher no zum «demit nöd».",
  {"R1": [("ἰάσομαι", "ich werde heilen", "Futur")], "R2": [("ἰάσωμαι", "ich heile", "Konjunktiv, RP")]},
  {"R1": [("ἰάσομαι", "ich wirde heile", "Futur")], "R2": [("ἰάσωμαι", "ich heile", "Konjunktiv, RP")]},
  ["Die beiden Formen unterscheiden sich in einem Vokal; der Konjunktiv glättet die Satzkonstruktion.",
   "Laut der automatischen Zuordnung lesen alle erfassten Handschriften (01, 02, 03, 032, 05, 𝔓66, 𝔓75) ἰάσομαι; ἰάσωμαι haben die gedruckten Ausgaben KJTR, RP und Stephanus."],
  ["Di beide Forme underscheided sich i eim Vokal; de Konjunktiv macht de Satz glatter.",
   "Nach de automatische Zueornig läsed alli erfasste Handschrifte ἰάσομαι; ἰάσωμαι händ di druckte Usgabe KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-JHN-012-041-01:R2", "JHN.12.41", "weil er seine Herrlichkeit sah", "als er seine Herrlichkeit sah", "wil er sini Herrlichkeit gseh hät", "wo-n-er sini Herrlichkeit gseh hät", "gering",
  "ὅτε «als» statt ὅτι «weil».", "ὅτε «wo» statt ὅτι «wil».",
  {"R1": [("ὅτι", "weil", "WH, Treg, NA28")], "R2": [("ὅτε", "als", "RP")]},
  {"R1": [("ὅτι", "wil", "WH, Treg, NA28")], "R2": [("ὅτε", "wo", "RP")]},
  ["Die Wörter unterscheiden sich in einem Buchstaben; «als» verbindet den Satz mit der Vision in [[ISA.6.1]].",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 𝔓66 und 𝔓75 ὅτι, 05 ὅτε; 032 hat ἐπεί «weil»."],
  ["Di Wörter underscheided sich i eim Buechstabe; «wo» verbindet de Satz mit de Vision i [[ISA.6.1]].",
   "Nach de automatische Zueornig läsed 01, 02, 03, 𝔓66 und 𝔓75 ὅτι, 05 ὅτε; 032 hät ἐπεί «wil»."]),
 ("VAR-SBLGNTAPP-JHN-012-047-01:R2", "JHN.12.47", "sie nicht bewahrt", "nicht glaubt", "si nöd bewaart", "nöd glaubt", "gering",
  "πιστεύσῃ «glaubt» statt φυλάξῃ «bewahrt».", "πιστεύσῃ «glaubt» statt φυλάξῃ «bewaart».",
  {"R1": [("φυλάξῃ", "bewahrt", "WH, Treg, NA28")], "R2": [("πιστεύσῃ", "glaubt", "RP")]},
  {"R1": [("φυλάξῃ", "bewaart", "WH, Treg, NA28")], "R2": [("πιστεύσῃ", "glaubt", "RP")]},
  ["«Glauben» passt zum Leitwort von [[JHN.12.44]]–[[JHN.12.46]] und kann von dort angeglichen sein.",
   "Laut der automatischen Zuordnung lesen alle erfassten Handschriften (01, 02, 03, 032, 05, 𝔓66, 𝔓75) φυλάξῃ; πιστεύσῃ haben die gedruckten Ausgaben KJTR, RP und Stephanus."],
  ["«Glaube» passt zum Leitwort vo [[JHN.12.44]]–[[JHN.12.46]] und cha vo det aaglichen sii.",
   "Nach de automatische Zueornig läsed alli erfasste Handschrifte φυλάξῃ; πιστεύσῃ händ di druckte Usgabe KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-JHN-013-002-01:R2", "JHN.13.2", "als das Mahl im Gang war", "als das Mahl stattgefunden hatte", "wo s Ässe im Gang gsii isch", "nachdem s Ässe gsii isch", "mittel",
  "Aorist γενομένου statt Präsens γινομένου. Das kann «nach dem Mahl» heissen, aber auch «als das Mahl begonnen hatte»; in [[JHN.13.26]] wird noch gegessen.",
  "Aorist γενομένου statt Präsens γινομένου. Das cha «nach em Ässe» heisse oder «wo s Ässe aagfange hät»; i [[JHN.13.26]] wird no ggässe.",
  {"R1": [("γινομένου", "im Gang", "WH, Treg, NA28")], "R2": [("γενομένου", "geschehen", "RP")]},
  {"R1": [("γινομένου", "im Gang", "WH, Treg, NA28")], "R2": [("γενομένου", "gsii", "RP")]},
  ["Die Formen unterscheiden sich in einem Buchstaben und wurden leicht verwechselt.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 𝔓75 γινομένου; 02, 05 und 𝔓66 (dort γεναμενου) die Aoristform; 04 ist hier nicht erhalten."],
  ["Di Forme underscheided sich i eim Buechstabe und sind liecht verwächslet worde.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 𝔓75 γινομένου; 02, 05 und 𝔓66 d Aoristform; 04 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-JHN-013-002-03:R2", "JHN.13.2", "Judas, Sohn des Simon Iskariot", "Judas Iskariot, Sohn des Simon", "de Judas, de Sohn vom Simon Iskariot", "de Judas Iskariot, de Sohn vom Simon", "gering",
  "Ἰσκαριώτης (Nominativ) bezieht den Beinamen auf Judas statt auf Simon. Hier folgt der SBLGNT NA28 und RP gegen WH und Treg.",
  "Ἰσκαριώτης (Nominativ) bezieht de Biiname uf de Judas statt uf de Simon. Da folgt de SBLGNT NA28 und RP gäge WH und Treg.",
  {"R1": [("Ἰσκαριώτου", "des Simon Iskariot", "NA28, RP")], "R2": [("Ἰσκαριώτης", "Judas Iskariot", "WH, Treg")]},
  {"R1": [("Ἰσκαριώτου", "vom Simon Iskariot", "NA28, RP")], "R2": [("Ἰσκαριώτης", "de Judas Iskariot", "WH, Treg")]},
  ["Der Beiname steht in [[JHN.6.71]] und [[JHN.13.26]] beim Vater Simon, sonst bei Judas ([[JHN.12.4]]); die Endungen konnten leicht angeglichen werden.",
   "Laut der automatischen Zuordnung lesen 02 und 05 Ἰσκαριώτου; 01, 03, 032, 𝔓66 und 𝔓75 Ἰσκαριώτης; 04 ist hier nicht erhalten."],
  ["De Biiname staat i [[JHN.6.71]] und [[JHN.13.26]] bim Vatter Simon, susch bim Judas ([[JHN.12.4]]).",
   "Nach de automatische Zueornig läsed 02 und 05 Ἰσκαριώτου; 01, 03, 032, 𝔓66 und 𝔓75 Ἰσκαριώτης; 04 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-JHN-013-018-02:R2", "JHN.13.18", "Der mein Brot isst", "Der mit mir das Brot isst", "Dä, wo mis Broot isst", "Dä, wo mit mir s Broot isst", "gering",
  "μετʼ ἐμοῦ «mit mir» statt μου «mein».", "μετʼ ἐμοῦ «mit mir» statt μου «mis».",
  {"R1": [("μου τὸν ἄρτον", "mein Brot", "WH, Treg, NA28")], "R2": [("μετʼ ἐμοῦ τὸν ἄρτον", "mit mir das Brot", "RP")]},
  {"R1": [("μου τὸν ἄρτον", "mis Broot", "WH, Treg, NA28")], "R2": [("μετʼ ἐμοῦ τὸν ἄρτον", "mit mir s Broot", "RP")]},
  ["μου entspricht eher der Septuaginta von [[PSA.41.9]] (ὁ ἐσθίων ἄρτους μου); μετʼ ἐμοῦ kann an [[MRK.14.18]] (ὁ ἐσθίων μετʼ ἐμοῦ) angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 03 und 04 μου; 01, 02, 032, 05 und 𝔓66 μετʼ ἐμοῦ; 𝔓75 ist hier nicht erhalten."],
  ["μου entspricht ehner de Septuaginta vo [[PSA.41.9]]; μετʼ ἐμοῦ cha a [[MRK.14.18]] aaglichen sii.",
   "Nach de automatische Zueornig läsed 03 und 04 μου; 01, 02, 032, 05 und 𝔓66 μετʼ ἐμοῦ."]),
 ("VAR-SBLGNTAPP-JHN-013-024-01:R2", "JHN.13.24", "er solle erfragen, wer es wohl sei", "und sagt zu ihm: «Sag, wer es ist»", "er söll usefinde, wer es ächt sig", "und seit zu ihm: «Säg, wer s isch»", "gering",
  "Statt der indirekten Frage spricht Petrus den Jünger direkt an. Hier folgt der SBLGNT NA28 und RP gegen WH und Treg.",
  "Statt de indirekte Frag redt de Petrus de Jünger diräkt aa. Da folgt de SBLGNT NA28 und RP gäge WH und Treg.",
  {"R1": [("πυθέσθαι τίς ἂν εἴη", "zu erfragen, wer es wohl sei", "NA28, RP")], "R2": [("καὶ λέγει αὐτῷ· Εἰπὲ τίς ἐστιν", "und sagt zu ihm: Sag, wer es ist", "WH, Treg")]},
  {"R1": [("πυθέσθαι τίς ἂν εἴη", "usefinde, wer es ächt sig", "NA28, RP")], "R2": [("καὶ λέγει αὐτῷ· Εἰπὲ τίς ἐστιν", "und seit zu ihm: Säg, wer s isch", "WH, Treg")]},
  ["Der Optativ mit ἄν ist gehobenes Griechisch; er kann ursprünglich sein oder eine stilistische Verbesserung der schlichteren direkten Rede.",
   "Laut der automatischen Zuordnung lesen 02, 032, 05 und die Korrektur in 𝔓66 πυθέσθαι τίς ἂν εἴη; 03 und 04 die direkte Rede. 01 hat nach der CNTR-Transkription beide Formulierungen hintereinander und wird bei R2 geführt; die Erstschrift von 𝔓66 weicht anders ab; 𝔓75 ist hier nicht erhalten."],
  ["De Optativ mit ἄν isch gehobnigs Griechisch; er cha ursprünglich sii oder e stilistischi Verbesserig.",
   "Nach de automatische Zueornig läsed 02, 032, 05 und d Korrektur in 𝔓66 πυθέσθαι τίς ἂν εἴη; 03 und 04 di diräkt Red; 01 hät beidi Formulierige hinderenand."]),
 ("VAR-SBLGNTAPP-JHN-013-026-05:R2", "JHN.13.26", "und gibt ihn Judas", "nimmt ihn und gibt ihn Judas", "und git en em Judas", "nimmt en und git en em Judas", "gering",
  "Mit λαμβάνει καί «nimmt und». Hier folgt der SBLGNT RP (und NIV) gegen WH, Treg und NA28.",
  "Mit λαμβάνει καί «nimmt und». Da folgt de SBLGNT RP (und NIV) gäge WH, Treg und NA28.",
  {"R1": [("δίδωσιν", "gibt", "SBLGNT, NIV, RP")], "R2": [("λαμβάνει καὶ δίδωσιν", "nimmt und gibt", "WH, Treg, NA28")]},
  {"R1": [("δίδωσιν", "git", "SBLGNT, NIV, RP")], "R2": [("λαμβάνει καὶ δίδωσιν", "nimmt und git", "WH, Treg, NA28")]},
  ["«Nimmt» kann an die Mahlworte der anderen Evangelien erinnern («er nahm Brot», [[MRK.14.22]]) und von dort ergänzt sein; es kann auch beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 02, 032, 05 und 𝔓66 ohne λαμβάνει καί, 03 und 04 mit ihm; 𝔓75 ist hier nicht erhalten."],
  ["«Nimmt» cha a d Maalwort vo de andere Evangelie erinnere ([[MRK.14.22]]) und vo det ergänzt sii; es cha au usgfalle sii.",
   "Nach de automatische Zueornig läsed 01, 02, 032, 05 und 𝔓66 ohni λαμβάνει καί, 03 und 04 mit."]),
 ("VAR-SBLGNTAPP-JHN-013-032-01:R2", "JHN.13.32", "Wenn Gott in ihm verherrlicht worden ist, wird auch Gott", "Auch Gott wird", "Wänn Gott in ihm verherrlicht worde isch, wird au Gott", "Au Gott wird", "gering",
  "Ohne den Bedingungssatz, der das Ende von [[JHN.13.31]] wiederholt. Der SBLGNT hat ihn mit Treg, NA28 und RP; WH lässt ihn weg.",
  "Ohni de Bedingigssatz, wo s Änd vo [[JHN.13.31]] widerholt. De SBLGNT hät en mit Treg, NA28 und RP; WH laat en wäg.",
  {"R1": [("εἰ ὁ θεὸς ἐδοξάσθη ἐν αὐτῷ", "Wenn Gott in ihm verherrlicht worden ist", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  {"R1": [("εἰ ὁ θεὸς ἐδοξάσθη ἐν αὐτῷ", "Wänn Gott in ihm verherrlicht worde isch", "Treg, NA28, RP")], "R2": [("–", "(fäält)", "WH")]},
  ["Die Worte können beim Abschreiben übersprungen worden sein, weil zweimal ἐν αὐτῷ steht; sie können auch als Verbindung ergänzt worden sein.",
   "Laut der automatischen Zuordnung hat unter den erfassten Handschriften nur 02 den Bedingungssatz; 01, 03, 032, 04 (beschädigt), 05 und 𝔓66 lesen ohne ihn; 𝔓75 ist hier nicht erhalten."],
  ["D Wort chönd bim Abschriibe übersprunge worde sii, wil zweimal ἐν αὐτῷ staat; si chönd au als Verbindig ergänzt worde sii.",
   "Nach de automatische Zueornig hät under de erfasste Handschrifte nu 02 de Bedingigssatz; 01, 03, 032, 04, 05 und 𝔓66 läsed ohni."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-012-001-050", "JHN.12.1-JHN.12.50", "section", "Salbung, Einzug und die Stunde der Verherrlichung",
  ["TU-JHN-012-001-011", "TU-JHN-012-012-019", "TU-JHN-012-020-036", "TU-JHN-012-037-043", "TU-JHN-012-044-050"],
  "Sechs Tage vor dem Passa salbt Maria in Betanien Jesu Füsse; Judas fragt, warum das Öl nicht für die Armen verkauft wurde, die Hohepriester planen, auch Lazarus zu töten. Beim Einzug in Jerusalem empfängt die Festmenge Jesus mit Palmzweigen und Hosanna, er setzt sich auf einen jungen Esel. Als Griechen ihn sehen wollen, sagt Jesus, die Stunde seiner Verherrlichung sei gekommen: Das Weizenkorn muss sterben, um Frucht zu bringen; eine Stimme vom Himmel antwortet auf sein Gebet, und er kündigt an, erhöht alle zu sich zu ziehen. Dann verbirgt er sich. Der Erzähler deutet den Unglauben vieler mit Worten Jesajas; dennoch glauben manche der Oberen heimlich. Zum Schluss ruft Jesus: Er ist als Licht gekommen, um zu retten, und redet, was der Vater ihm aufgetragen hat.", SEG),
 ("TU-JHN-012-001-011", "JHN.12.1-JHN.12.11", "narrative", "Die Salbung in Betanien", None,
  "Sechs Tage vor dem Passa ist Jesus in Betanien zu Gast; Marta bedient, Lazarus liegt mit zu Tisch. Maria salbt Jesu Füsse mit einem Pfund kostbarem Nardenöl und trocknet sie mit ihren Haaren. Judas Iskariot, der ihn ausliefern wird, fragt, warum das Öl nicht verkauft und der Erlös den Armen gegeben wurde; der Erzähler bemerkt, er sei ein Dieb gewesen und habe die Kasse gehabt. Jesus verteidigt Maria mit Blick auf den Tag seines Begräbnisses. Eine grosse Menge kommt, auch um Lazarus zu sehen; die Hohepriester beschliessen, auch Lazarus zu töten, weil seinetwegen viele an Jesus glauben.", None),
 ("TU-JHN-012-012-019", "JHN.12.12-JHN.12.19", "narrative", "Der Einzug in Jerusalem", None,
  "Am folgenden Tag zieht die Festmenge Jesus mit Palmzweigen entgegen und ruft «Hosanna» mit Worten aus [[PSA.118.26]]. Jesus setzt sich auf einen jungen Esel, wie es in [[ZEC.9.9]] heisst; die Jünger verstehen das erst, als Jesus verherrlicht ist. Die Menge, die bei der Auferweckung des Lazarus dabei war, bezeugt sie; weil man von diesem Zeichen gehört hat, zieht ihm die Menge entgegen. Die Pharisäer sagen zueinander: «Die Welt ist hinter ihm hergelaufen.»", None),
 ("TU-JHN-012-020-036", "JHN.12.20-JHN.12.36", "dialogue", "Die Griechen und die Stunde der Verherrlichung", None,
  "Griechen, die zum Fest gekommen sind, möchten Jesus sehen; Philippus und Andreas sagen es ihm. Jesus antwortet, die Stunde sei gekommen, dass der Menschensohn verherrlicht wird: Das Weizenkorn bringt nur Frucht, wenn es stirbt; wer ihm dient, soll ihm folgen. Er ist erschüttert, bittet aber: «Vater, verherrliche deinen Namen», und eine Stimme aus dem Himmel antwortet; die Menge hält sie für Donner oder für einen Engel, Jesus sagt, sie sei um ihretwillen ergangen. Jetzt sei Gericht über diese Welt und ihr Herrscher werde hinausgeworfen; er werde, von der Erde erhöht, alle zu sich ziehen – der Erzähler bezieht das auf seinen Tod. Die Menge wendet ein, der Christus bleibe nach dem Gesetz in Ewigkeit, und fragt, wer dieser Menschensohn sei; Jesus ruft auf, an das Licht zu glauben, solange sie es haben; dann verbirgt er sich vor ihnen.", None),
 ("TU-JHN-012-037-043", "JHN.12.37-JHN.12.43", "narrative", "Unglaube trotz der Zeichen", None,
  "Der Erzähler stellt fest, dass sie trotz so vieler Zeichen nicht an Jesus glaubten, und deutet das mit zwei Jesajaworten ([[ISA.53.1]], [[ISA.6.10]]); Jesaja habe seine Herrlichkeit gesehen. Dennoch glauben auch viele der Oberen an Jesus, bekennen es aber wegen der Pharisäer nicht, um nicht aus der Synagoge ausgeschlossen zu werden, denn sie lieben die Ehre bei den Menschen mehr als die Ehre bei Gott.", None),
 ("TU-JHN-012-044-050", "JHN.12.44-JHN.12.50", "discourse", "Jesu Ruf: Ich bin als Licht gekommen", None,
  "Jesus ruft laut: Wer an ihn glaubt und ihn sieht, glaubt an den und sieht den, der ihn gesandt hat. Er ist als Licht in die Welt gekommen, nicht um die Welt zu richten, sondern um sie zu retten; wer seine Worte nicht annimmt, den wird das Wort, das er geredet hat, am letzten Tag richten. Er redet nicht aus sich selbst, sondern wie der Vater es ihm geboten hat, und dessen Gebot ist ewiges Leben.", None),
 ("TU-JHN-013-001-038", "JHN.13.1-JHN.13.38", "section", "Fusswaschung, Ansage der Auslieferung und das neue Gebot",
  ["TU-JHN-013-001-011", "TU-JHN-013-012-020", "TU-JHN-013-021-030", "TU-JHN-013-031-038"],
  "Vor dem Passafest, im Wissen, dass seine Stunde gekommen ist, wäscht Jesus beim Mahl seinen Jüngern die Füsse; Petrus wehrt sich zuerst. Jesus deutet die Waschung als Beispiel: Wie er, ihr Herr und Lehrer, gehandelt hat, sollen sie einander tun. Er kündigt an, dass einer von ihnen ihn ausliefern wird, und gibt Judas den Bissen; der Satan fährt in Judas, der sogleich hinausgeht; es ist Nacht. Danach spricht Jesus von seiner Verherrlichung und seinem Weggehen, gibt das neue Gebot, einander zu lieben, wie er sie geliebt hat, und kündigt Petrus an, dass er ihn dreimal verleugnen wird.", SEG),
 ("TU-JHN-013-001-011", "JHN.13.1-JHN.13.11", "narrative", "Die Fusswaschung", None,
  "Vor dem Passafest weiss Jesus, dass seine Stunde gekommen ist, aus der Welt zum Vater hinüberzugehen; er liebt die Seinen bis zur Vollendung. Während des Mahls – der Teufel hat schon ins Herz gegeben, dass Judas ihn ausliefern soll – steht Jesus auf, bindet sich ein Leinentuch um und wäscht den Jüngern die Füsse. Petrus wehrt ab; Jesus sagt, wenn er ihn nicht wasche, habe er keinen Anteil an ihm. Darauf will Petrus auch Hände und Kopf gewaschen haben; Jesus antwortet, wer gebadet sei, sei ganz rein, und die Jünger seien rein, aber nicht alle – denn er kennt den, der ihn ausliefert.", None),
 ("TU-JHN-013-012-020", "JHN.13.12-JHN.13.20", "discourse", "Ein Beispiel des Herrn und Lehrers", None,
  "Jesus nimmt die Obergewänder wieder, legt sich zu Tisch und erklärt: Wenn er, ihr Herr und Lehrer, ihnen die Füsse gewaschen hat, sind auch sie verpflichtet, einander die Füsse zu waschen; er hat ihnen ein Beispiel gegeben. Ein Knecht ist nicht grösser als sein Herr; selig, wer das weiss und tut. Er spricht nicht von allen: Das Schriftwort aus [[PSA.41.9]] soll sich erfüllen. Er sagt es im Voraus, damit sie glauben, «dass ich bin». Wer aufnimmt, wen er sendet, nimmt ihn auf und den, der ihn gesandt hat.", None),
 ("TU-JHN-013-021-030", "JHN.13.21-JHN.13.30", "narrative", "Ansage der Auslieferung; Judas geht hinaus", None,
  "Erschüttert kündigt Jesus an, einer von ihnen werde ihn ausliefern; die Jünger sind ratlos. Auf den Wink des Petrus fragt der Jünger, den Jesus liebte und der an seiner Brust liegt, wer es sei. Jesus antwortet, es sei der, dem er den eingetauchten Bissen gebe, und gibt ihn Judas, dem Sohn des Simon Iskariot. Danach fährt der Satan in Judas; Jesus sagt zu ihm: «Was du tust, das tu schnell.» Keiner versteht es; einige denken an Einkäufe für das Fest oder eine Gabe für die Armen. Judas nimmt den Bissen und geht sogleich hinaus. Es war Nacht.", None),
 ("TU-JHN-013-031-038", "JHN.13.31-JHN.13.38", "dialogue", "Das neue Gebot und die Ansage der Verleugnung", None,
  "Nachdem Judas hinausgegangen ist, sagt Jesus, jetzt sei der Menschensohn verherrlicht worden und Gott in ihm, und Gott werde ihn sogleich verherrlichen. Er ist nur noch kurze Zeit bei den Jüngern; wohin er geht, können sie nicht kommen. Er gibt ihnen ein neues Gebot: einander zu lieben, wie er sie geliebt hat; daran werden alle erkennen, dass sie seine Jünger sind. Petrus fragt, wohin er gehe; Jesus sagt, Petrus könne ihm jetzt nicht folgen, aber später. Petrus will sein Leben für ihn hingeben; Jesus kündigt an, dass Petrus ihn dreimal verleugnen wird, bevor ein Hahn kräht.", None),
]
UNITS_GSW = {
 "TU-JHN-012-001-050": ("Salbig, Iizug und d Stund vo de Verherrlichung", "Sächs Täg vor em Passa salbt d Maria z Betanie d Füess vom Jesus; de Judas fröget, werum mer s Öl nöd für d Arme verchauft heig, d Hoheprieschter planed, au de Lazarus umzbringe. Bim Iizug z Jerusalem empfangt d Feschtmängi de Jesus mit Palmzwiig und Hosanna, er setzt sich uf es Eseli. Wo Grieche en wänd gseh, seit de Jesus, d Stund vo sinere Verherrlichung sig choo: S Weizechorn mues stärbe, zum Frucht bringe; e Stimm vom Himmel antwortet uf sis Gebätt, und er seit, er wärdi, erhöcht, alli zu sich zie. Dänn versteckt er sich. De Erzähler deutet de Unglaube vo vile mit Wort vom Jesaja; trotzdem glaubed es paar vo de Obere heimlich. Zletscht rüeft de Jesus: Er isch als Liecht choo, zum rette, und redt, was em de Vatter ufträit hät."),
 "TU-JHN-012-001-011": ("D Salbig z Betanie", "Sächs Täg vor em Passa isch de Jesus z Betanie z Gascht; d Marta bedient, de Lazarus liit mit am Tisch. D Maria salbt d Füess vom Jesus mit eme Pfund tüürem Nardeöl und tröchnet si mit ire Haar ab. De Judas Iskariot, wo en wird uslifere, fröget, werum mer s Öl nöd verchauft und s Gält de Arme gää heig; de Erzähler seit, er sig en Dieb gsii und heig d Kasse gha. De Jesus verteidiget d Maria im Blick uf de Tag vo sim Begräbnis. E grossi Mängi chunnt, au zum de Lazarus gseh; d Hoheprieschter beschlüüssed, au de Lazarus umzbringe, wil wäge ihm vili a de Jesus glaubed."),
 "TU-JHN-012-012-019": ("De Iizug z Jerusalem", "Am Tag druf gaat d Feschtmängi em Jesus mit Palmzwiig entgäge und rüeft «Hosanna» mit Wort us [[PSA.118.26]]. De Jesus setzt sich uf es Eseli, wie s i [[ZEC.9.9]] heisst; d Jünger verstönd das erscht, wo de Jesus verherrlicht isch. D Mängi, wo bi de Uferweckig vom Lazarus debii gsii isch, bezüügt si; wil mer vo dem Zeiche ghört hät, gaat em d Mängi entgäge. D Pharisäer säged zunenand: «D Wält isch hinder ihm härgloffe.»"),
 "TU-JHN-012-020-036": ("D Grieche und d Stund vo de Verherrlichung", "Grieche, wo as Fäscht choo sind, wetted de Jesus gseh; de Philippus und de Andreas säged s ihm. De Jesus antwortet, d Stund sig choo, dass de Mänschesohn verherrlicht wird: S Weizechorn bringt nu Frucht, wänn s stirbt; wer ihm dient, söll ihm nachegaa. Er isch erschüttert, bittet aber: «Vatter, verherrlich din Name», und e Stimm vom Himmel antwortet; d Mängi meint, es heig donneret oder en Ängel heig gredt, und de Jesus seit, si sig wäge ine choo. Jetzt sig Gricht über die Wält und ire Herrscher wärdi usegworfe; er wärdi, vo de Ärde erhöcht, alli zu sich zie – de Erzähler bezieht das uf sin Tod. D Mängi wändet ii, de Christus bliibi nach em Gsetz für immer, und fröget, wer dä Mänschesohn sig; de Jesus rüeft uf, as Liecht z glaube, solang si s händ; dänn versteckt er sich vor ine."),
 "TU-JHN-012-037-043": ("Unglaube trotz de Zeiche", "De Erzähler stellt fescht, dass si trotz so vile Zeiche nöd a de Jesus glaubt händ, und deutet das mit zwei Wort vom Jesaja ([[ISA.53.1]], [[ISA.6.10]]); de Jesaja heig sini Herrlichkeit gseh. Trotzdem glaubed au vili vo de Obere a de Jesus, bekänned s aber wäge de Pharisäer nöd, demit si nöd us de Synagoge usgschlosse wärded, dänn d Ehr bi de Mänsche isch ine lieber als d Ehr bi Gott."),
 "TU-JHN-012-044-050": ("De Jesus rüeft: Ich bi als Liecht choo", "De Jesus rüeft luut: Wer a ihn glaubt und ihn gseht, glaubt a dä und gseht dä, wo en gschickt hät. Er isch als Liecht i d Wält choo, nöd zum d Wält richte, sondern zum si rette; wer sini Wort nöd aanimmt, dä wird s Wort, won er gredt hät, am letschte Tag richte. Er redt nöd us sich sälber, sondern wie s em de Vatter botte hät, und sis Gebot isch ewigs Läbe."),
 "TU-JHN-013-001-038": ("Füesswäsche, Aasag vo de Uslieferig und s nöi Gebot", "Vor em Passafäscht, wo de Jesus weiss, dass sini Stund choo isch, wäscht er bim Ässe sine Jünger d Füess; de Petrus wehrt sich zerscht. De Jesus deutet s Wäsche als Biispil: Wie er, ire Herr und Lehrer, ghandlet hät, söled si s enand mache. Er seit aa, dass eine vo ine en wird uslifere, und git em Judas de Bisse; de Satan faart in Judas ine, und dä gaat sofort use; es isch Nacht. Dänn redt de Jesus vo sinere Verherrlichung und vo sim Wäggaa, git s nöi Gebot, enand z liebe, wie er si gliebt hät, und seit em Petrus, er wärdi en drüümal verleugne."),
 "TU-JHN-013-001-011": ("S Füesswäsche", "Vor em Passafäscht weiss de Jesus, dass sini Stund choo isch, wo-n-er us dere Wält zum Vatter überegaat; er liebt di Sine bis zur Vollendig. Bim Ässe – de Tüüfel hät scho is Härz gleit, dass de Judas en söll uslifere – staat de Jesus uf, bindet sich es Liinetuech um und wäscht de Jünger d Füess. De Petrus wehrt ab; de Jesus seit, wänn er en nöd wäschi, heig er kein Teil a ihm. Druf wott de Petrus au d Händ und de Chopf gwäsche ha; de Jesus antwortet, wer badet heig, sig ganz rein, und d Jünger sigid rein, aber nöd alli – dänn er kännt dä, wo en usliferet."),
 "TU-JHN-013-012-020": ("Es Biispil vom Herr und Lehrer", "De Jesus nimmt d Oberchleider wider, leit sich an Tisch und erklärt: Wänn er, ire Herr und Lehrer, ine d Füess gwäsche hät, sind au si verpflichtet, enand d Füess z wäsche; er hät ine es Biispil gää. En Knecht isch nöd grösser als sin Herr; sälig, wer das weiss und macht. Er redt nöd vo allne: S Schriftwort us [[PSA.41.9]] söll sich erfülle. Er seit s im voruus, demit si glaubed, «dass ich bi». Wer dä ufnimmt, won er schickt, nimmt ihn uf und dä, wo en gschickt hät."),
 "TU-JHN-013-021-030": ("Aasag vo de Uslieferig; de Judas gaat use", "Erschüttert seit de Jesus aa, eine vo ine wärdi en uslifere; d Jünger sind ratlos. Uf de Wink vom Petrus fröget de Jünger, wo de Jesus gliebt hät und a sinere Bruscht liit, wer s sig. De Jesus antwortet, es sig dä, wo-n-er de iituucht Bisse gäbi, und git en em Judas, em Sohn vom Simon Iskariot. Dänn faart de Satan in Judas ine; de Jesus seit zu ihm: «Was du machsch, das mach schnäll.» Keine verstaat s; es paar dänked a Iichäuf fürs Fäscht oder a e Gaab für d Arme. De Judas nimmt de Bisse und gaat sofort use. Es isch Nacht gsii."),
 "TU-JHN-013-031-038": ("S nöi Gebot und d Aasag vo de Verleugnig", "Wo de Judas usegange isch, seit de Jesus, jetzt sig de Mänschesohn verherrlicht worde und Gott in ihm, und Gott wärdi en grad verherrliche. Er isch nu no churz bi de Jünger; wo-n-er hiigaat, chönd si nöd hiichoo. Er git ine es nöis Gebot: enand z liebe, wie er si gliebt hät; dra wärded alli merke, dass si sini Jünger sind. De Petrus fröget, wo-n-er hiigang; de Jesus seit, de Petrus chönn em jetzt nöd nachegaa, aber spöter. De Petrus wott sis Läbe für ihn häregää; de Jesus seit aa, dass de Petrus en drüümal wird verleugne, bevor en Güggel chräit."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("Grundentscheide: Die Wiedergabe der johanneischen Schlüsselwörter ist in den Arbeitsübersetzungen zu Johannes 1–3 "
  "(scripts/authoring/johannes_text_01_03.py) begründet und gilt hier unverändert: λόγος «Wort», ἐγώ εἰμι «ich bin», "
  "δόξα/δοξάζω «Herrlichkeit/verherrlichen» (Ausnahme mit Begründung: [[JHN.12.43]] «Ehre»), σημεῖον «Zeichen», μένω "
  "«bleiben», ἀμὴν ἀμήν «Amen, amen», κόσμος «Welt», ὑψόω «erhöhen», παραδίδωμι «ausliefern»."),
 ("οἱ Ἰουδαῖοι ist wörtlich mit «die Juden» wiedergegeben ([[JHN.12.9]], [[JHN.12.11]], [[JHN.13.33]]). Das ist eine "
  "Deutungsentscheidung: Je nach Stelle sind das Volk, die Bewohner Judäas oder die führenden Gegner Jesu gemeint; die "
  "Alternativen «die Judäer» bzw. «die jüdischen Führer» stehen in den decisions. Jesus und seine Jünger sind selbst Juden; "
  "die Wiedergabe ist kein Urteil über das jüdische Volk."),
 ("Schriftzitate sind durch Anführungszeichen kenntlich gemacht und in den decisions belegt: [[PSA.118.26]] in [[JHN.12.13]], "
  "[[ZEC.9.9]] in [[JHN.12.15]], [[ISA.53.1]] in [[JHN.12.38]], [[ISA.6.10]] in [[JHN.12.40]] und [[PSA.41.9]] in [[JHN.13.18]]."),
 ("Johannes erzählt oft im Präsens («er kommt», «sagt»); das ist beibehalten. ὅτι vor direkter Rede ist nicht eigens "
  "übersetzt. In Johannes 12–13 fehlt kein Vers im SBLGNT."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Grundentscheid: Di johanneische Schlüsselwörter sind wie i de Arbeitsübersetzige zu Johannes 1–3 "
  "(scripts/authoring/johannes_text_01_03.py) widergää: λόγος «Wort», ἐγώ εἰμι «ich bi», δόξα/δοξάζω «Herrlichkeit/"
  "verherrliche» (Usnaam [[JHN.12.43]] «Ehr»), σημεῖον «Zeiche», μένω «bliibe», ἀμὴν ἀμήν «Amen, amen», κόσμος «Wält», "
  "ὑψόω «erhöche», παραδίδωμι «uslifere»."),
 ("οἱ Ἰουδαῖοι isch wörtlich «d Jude». Das isch en Deutigsentscheid: je nach Stell isch s Volk, d Lüüt us Judäa oder di "
  "füerende Gägner vom Jesus gmeint. De Jesus und sini Jünger sind sälber Jude."),
 ("Schriftzitat sind mit Aafüerigszeiche kenntlich gmacht: [[PSA.118.26]], [[ZEC.9.9]], [[ISA.53.1]], [[ISA.6.10]], [[PSA.41.9]]."),
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
            raise SystemExit(f"JHN {c}: unerwartet fehlende Verse")
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Liecht), ä für offenes e.",
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/johannes_text_12_13.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 12–13 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
