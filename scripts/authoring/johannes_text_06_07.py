#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 6–7 (Brot des Lebens, Laubhüttenfest, Beginn des Abschnitts von der Ehebrecherin) –
Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen,
Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_06_07.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- Die Grundentscheide für johanneische Schlüsselwörter (ἀμὴν ἀμήν, ἐγώ εἰμι, σημεῖον, μένω, κόσμος, δόξα/δοξάζω,
  οἱ Ἰουδαῖοι u. a.) sind in scripts/authoring/johannes_text_01_03.py begründet und hier übernommen.
- [[JHN.7.53]] ist der erste Vers des Abschnitts von der Ehebrecherin ([[JHN.7.53]]–[[JHN.8.11]]), den der SBLGNT in
  Doppelklammern ⟦ ⟧ setzt. Der Vers wird übersetzt, weil die Tokens ihn enthalten; die öffnende Klammer steht im
  Übersetzungstext, die schliessende folgt in [[JHN.8.11]] (scripts/authoring/johannes_text_08_09.py). Er bildet die
  eigene Teileinheit TU-JHN-007-053-053. Der Handschriftenbefund ist aus data/witness-texts ermittelt.

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
CHAPTERS = ((6, 71), (7, 53))
SKIP_OTI = "ὅτι leitet die direkte Rede ein"
SKIP_OTI_G = "ὅτι leitet di diräkt Red ii"

DE = {
 # ------------------------------------------------------------ Kapitel 6
 "JHN.6.1": "[Danach]{1,2} [ging]{3} [Jesus]{4,5} [weg]{3} [ans andere Ufer]{6} [des Sees]{7,8} [von Galiläa]{9,10}, [dem von Tiberias]{11,12}.",
 "JHN.6.2": "[Es folgte]{1} [ihm]{3} [aber]{2} [eine grosse]{5} [Menge]{4}, [weil]{6} [sie]{7} [die Zeichen]{8,9} [sahen]{7}, [die]{10} [er]{11} [an]{12} [den Kranken]{13,14} [tat]{11}.",
 "JHN.6.3": "[Jesus]{6} [aber]{2} [stieg]{1} [auf]{3} [den Berg]{4,5} [hinauf]{1} und{7} [sass]{9} [dort]{8} [mit]{10} [seinen]{11,13} [Jüngern]{12}.",
 "JHN.6.4": "[Nahe]{3} [war]{1} [aber]{2} [das Passa]{4,5}, [das Fest]{6,7} [der Juden]{8,9}.",
 "JHN.6.5": "[Als]{1} [nun]{2} [Jesus]{5,6} [die Augen]{3,4} [erhob]{1} und{7} [sah]{8}, [dass]{9} [eine grosse]{10} [Menge]{11} [zu]{13} [ihm]{14} [kommt]{12}, [sagt er]{15} [zu]{16} [Philippus]{17}: «[Woher]{18} [sollen wir]{19} [Brote]{20} [kaufen]{19}, [damit]{21} [diese]{23} [zu essen haben]{22}?»",
 "JHN.6.6": "[Das]{1} [sagte er]{3} [aber]{2}, [um]{4} [ihn]{5} [zu prüfen]{4}; [er selbst]{6} [wusste]{8} [nämlich]{7}, [was]{9} [er]{10} [tun]{11} [würde]{10}.",
 "JHN.6.7": "[Philippus]{3} [antwortete]{1} [ihm]{2}: «[Brote]{6} [für zweihundert]{4} [Denare]{5} [reichen]{8} [nicht]{7} [für sie]{9}, [wenn]{10} [jeder]{11} auch nur [ein wenig]{12,13} [bekommen soll]{14}.»",
 "JHN.6.8": "[Einer]{3} [von]{4} [seinen]{5,7} [Jüngern]{6}, [Andreas]{8}, [der Bruder]{9,10} [des Simon]{11} [Petrus]{12}, [sagt]{1} [zu ihm]{2}:",
 "JHN.6.9": "«[Hier]{3} [ist]{1} [ein Junge]{2}, [der]{4} [fünf]{6} [Gerstenbrote]{7,8} und{9} [zwei]{10} [Fische]{11} [hat]{5}; [aber]{12} [was]{14} [ist]{15} [das]{13} [für]{16} [so viele]{17}?»",
 "JHN.6.10": "[Jesus]{2,3} [sagte]{1}: «[Lasst]{4} [die Menschen]{5,6} [sich lagern]{7}!» [Es war]{8} [aber]{9} [viel]{11} [Gras]{10} [an]{12} [dem]{13} [Ort]{14}. [Da]{16} [lagerten sich]{15} [die Männer]{17,18}, [an Zahl]{19,20} [etwa]{21} [fünftausend]{22}.",
 "JHN.6.11": "[Jesus]{5,6} [nahm]{1} [nun]{2} [die Brote]{3,4}, und{7} [nachdem er gedankt hatte]{8}, [teilte er sie aus]{9} [an die]{10} [Lagernden]{11}, [ebenso]{12} [auch]{13} [von]{14} [den Fischen]{15,16}, [so viel]{17} [sie wollten]{18}.",
 "JHN.6.12": "[Als]{1} [sie]{3} [aber]{2} [satt geworden waren]{3}, [sagt er]{4} [zu seinen]{5,7} [Jüngern]{6}: «[Sammelt]{8} [die übrig gebliebenen]{9,10} [Brocken]{11} [ein]{8}, [damit]{12} [nichts]{13,14} [verloren geht]{15}.»",
 "JHN.6.13": "[Da]{2} [sammelten sie]{1} und{3} [füllten]{4} [zwölf]{5} [Körbe]{6} [mit Brocken]{7} [von]{8} [den fünf]{9,10} [Gerstenbroten]{11-13}, [die]{14} [denen]{16}, [die gegessen hatten]{17}, [übrig geblieben waren]{15}.",
 "JHN.6.14": "[Als]{4} [nun]{2} [die Menschen]{1,3} [das Zeichen]{7} [sahen]{4}, [das]{5} [er getan hatte]{6}, [sagten sie]{8}: «[Das]{10} [ist]{11} [wahrhaftig]{12} [der Prophet]{13,14}, [der]{15} [in]{17} [die Welt]{18,19} [kommt]{16}.» ~9(" + SKIP_OTI + ")",
 "JHN.6.15": "[Weil]{3} [Jesus]{1} [nun]{2} [erkannte]{3}, [dass]{4} [sie]{5} [kommen]{6} und{7} [ihn]{9} [mit Gewalt ergreifen]{8} [wollten]{5}, [um]{10} ihn [zum König]{12} [zu machen]{11}, [zog er sich]{13} [wieder]{14} [auf]{15} [den Berg]{16,17} [zurück]{13}, [er allein]{18,19}.",
 "JHN.6.16": "[Als]{1} [es]{4} [aber]{2} [Abend]{3} [wurde]{4}, [gingen]{5} [seine]{6,8} [Jünger]{7} [hinab]{5} [an]{9} [den See]{10,11}",
 "JHN.6.17": "und{1} [stiegen]{2} [in]{3} [ein Boot]{4} [und fuhren]{5} [über]{6} [den See]{7,8} [nach]{9} [Kafarnaum]{10}. Und{11} [es war]{14} [schon]{13} [dunkel]{12} [geworden]{14}, und{15} [Jesus]{20,21} [war]{17} [noch nicht]{16} [zu]{18} [ihnen]{19} [gekommen]{17}.",
 "JHN.6.18": "[Und]{2} [der See]{1,3} [wurde aufgewühlt]{7}, weil [ein starker]{5} [Wind]{4} [wehte]{6}.",
 "JHN.6.19": "[Als sie]{1} [nun]{2} [etwa]{3} [fünfundzwanzig]{5,6} [oder]{7} [dreissig]{8} [Stadien]{4} [gerudert waren]{1}, [sehen sie]{9} [Jesus]{10,11} [auf]{13} [dem See]{14,15} [gehen]{12} und{16} [nahe]{17} [an das]{18} [Boot]{19} [herankommen]{20}, und{21} [sie fürchteten sich]{22}.",
 "JHN.6.20": "[Er]{1} [aber]{2} [sagt]{3} [zu ihnen]{4}: «[Ich]{5} [bin es]{6}; [fürchtet euch]{8} [nicht]{7}!»",
 "JHN.6.21": "[Da]{2} [wollten sie]{1} [ihn]{4} [in]{5} [das Boot]{6,7} [nehmen]{3}, und{8} [sogleich]{9} [war]{10} [das Boot]{11,12} [am]{13,14} [Land]{15}, [auf]{16} [das]{17} [sie zuhielten]{18}.",
 "JHN.6.22": "[Am folgenden Tag]{1,2} [sah]{10} [die Menge]{3,4}, [die]{5} [am anderen Ufer]{7} [des Sees]{8,9} [stand]{6}, [dass]{11} [kein]{14} [anderes]{13} [Boot]{12} [dort]{16} [gewesen war]{15} [ausser]{17,18} [einem]{19}, und{20} [dass]{21} [Jesus]{27,28} [nicht]{22} [mit]{23} [seinen]{24,26} [Jüngern]{25} [in]{29} [das Boot]{30,31} [gestiegen war]{23}, [sondern]{32} [seine]{34,36} [Jünger]{35} [allein]{33} [weggefahren waren]{37}.",
 "JHN.6.23": "[Es kamen]{2} [jedoch]{1} [Boote]{3} [aus]{4} [Tiberias]{5} [in die Nähe]{6} [des Ortes]{7,8}, [wo]{9} [sie]{10} [das Brot]{11,12} [gegessen hatten]{10}, [nachdem]{13} [der Herr]{14,15} [gedankt hatte]{13}.",
 "JHN.6.24": "[Als]{1} [nun]{2} [die Menge]{4,5} [sah]{3}, [dass]{6} [Jesus]{7} [nicht]{8} [dort]{10} [war]{9}, [auch nicht]{11} [seine]{12,14} [Jünger]{13}, [stiegen sie]{15,16} [in]{17} [die Boote]{18,19} und{20} [kamen]{21} [nach]{22} [Kafarnaum]{23} [und suchten]{24} [Jesus]{25,26}.",
 "JHN.6.25": "Und{1} [als sie]{2} [ihn]{3} [am anderen Ufer]{4} [des Sees]{5,6} [fanden]{2}, [sagten sie]{7} [zu ihm]{8}: «[Rabbi]{9}, [wann]{10} [bist du]{12} [hierher]{11} [gekommen]{12}?»",
 "JHN.6.26": "[Jesus]{3,4} [antwortete]{1} [ihnen]{2} und{5} [sagte]{6}: «[Amen]{7}, [amen]{8}, [ich sage]{9} [euch]{10}: [Ihr sucht]{11} [mich]{12} [nicht]{13}, [weil]{14} [ihr]{15} [Zeichen]{16} [gesehen habt]{15}, [sondern]{17} [weil]{18} [ihr]{19} [von]{20} [den Broten]{21,22} [gegessen habt]{19} und{23} [satt geworden seid]{24}.",
 "JHN.6.27": "[Arbeitet]{1} [nicht]{2} [für die]{3} [Speise]{4}, [die]{5} [vergeht]{6}, [sondern]{7} [für die Speise]{8,9}, [die]{10} [bleibt]{11} [zum]{12} [ewigen]{14} [Leben]{13}, [die]{15} [der Menschensohn]{16-19} [euch]{20} [geben wird]{21}; [denn]{23} [ihn]{22} [hat]{26} [der Vater]{24,25}, [Gott]{27,28}, [beglaubigt]{26}.»",
 "JHN.6.28": "[Da]{2} [sagten sie]{1} [zu]{3} [ihm]{4}: «[Was]{5} [sollen wir tun]{6}, [damit]{7} [wir]{8} [die Werke]{9,10} [Gottes]{11,12} [wirken]{8}?»",
 "JHN.6.29": "[Jesus]{2,3} [antwortete]{1} und{4} [sagte]{5} [zu ihnen]{6}: «[Das]{7} [ist]{8} [das Werk]{9,10} [Gottes]{11,12}, [dass]{13} [ihr]{14} [an]{15} den [glaubt]{14}, [den]{16} [jener]{18} [gesandt hat]{17}.»",
 "JHN.6.30": "[Da]{2} [sagten sie]{1} [zu ihm]{3}: «[Was]{4} [tust]{6} [du]{7} [denn]{5} [für ein Zeichen]{8}, [damit]{9} [wir es sehen]{10} und{11} [dir]{13} [glauben]{12}? [Was]{14} [wirkst du]{15}?",
 "JHN.6.31": "[Unsere]{3} [Väter]{1,2} [haben]{6} [das Manna]{4,5} [in]{7} [der Wüste]{8,9} [gegessen]{6}, [wie]{10} [geschrieben steht]{11,12}: ‹[Brot]{13} [vom]{14,15} [Himmel]{16} [gab er]{17} [ihnen]{18} [zu essen]{19}.›»",
 "JHN.6.32": "[Da]{2} [sagte]{1} [Jesus]{4,5} [zu ihnen]{3}: «[Amen]{6}, [amen]{7}, [ich sage]{8} [euch]{9}: [Nicht]{10} [Mose]{11} [hat]{12} [euch]{13} [das Brot]{14,15} [vom]{16,17} [Himmel]{18} [gegeben]{12}, [sondern]{19} [mein]{22} [Vater]{20,21} [gibt]{23} [euch]{24} [das]{25} [wahre]{30,31} [Brot]{26} [vom]{27,28} [Himmel]{29}.",
 "JHN.6.33": "[Denn]{2} [das Brot]{1,3} [Gottes]{4,5} [ist]{6} [das, was]{7} [vom]{9,10} [Himmel]{11} [herabkommt]{8} und{12} [der Welt]{15,16} [Leben]{13} [gibt]{14}.»",
 "JHN.6.34": "[Da]{2} [sagten sie]{1} [zu]{3} [ihm]{4}: «[Herr]{5}, [gib]{7} [uns]{8} [immer]{6} [dieses]{11} [Brot]{9,10}!»",
 "JHN.6.35": "[Jesus]{3,4} [sagte]{1} [zu ihnen]{2}: «[Ich]{5} [bin]{6} [das Brot]{7,8} [des Lebens]{9,10}. [Wer]{11} [zu]{13} [mir]{14} [kommt]{12}, [wird gewiss nicht]{15,16} [hungern]{17}, und{18} [wer]{19} [an]{21} [mich]{22} [glaubt]{20}, [wird niemals]{23,24,26} [Durst haben]{25}.",
 "JHN.6.36": "[Aber]{1} [ich habe]{2} [euch]{3} [gesagt]{2}: [Ihr habt]{6} [mich]{7} [zwar]{5} [gesehen]{6}, [und]{8} [doch glaubt ihr]{10} [nicht]{9}. ~4(" + SKIP_OTI + ")",
 "JHN.6.37": "[Alles]{1}, [was]{2} [mir]{4} [der Vater]{5,6} [gibt]{3}, [wird]{9} [zu]{7} [mir]{8} [kommen]{9}, und{10} [wer]{11} [zu]{13} [mir]{14} [kommt]{12}, den [werde ich gewiss nicht]{15,16} [hinausstossen]{17,18}.",
 "JHN.6.38": "[Denn]{1} [ich bin]{2} [vom]{3,4} [Himmel]{5} [herabgekommen]{2}, [nicht]{6} [um]{7} [meinen]{11,12} [Willen]{9,10} [zu tun]{8}, [sondern]{13} [den Willen]{14,15} [dessen]{16}, der [mich]{18} [gesandt hat]{17}.",
 "JHN.6.39": "[Das]{1} [aber]{2} [ist]{3} [der Wille]{4,5} [dessen]{6}, der [mich]{8} [gesandt hat]{7}: [dass]{9} [ich]{15} [von]{16,17} [allem]{10}, [was]{11} [er]{12} [mir]{13} [gegeben hat]{12}, [nichts]{14} [verliere]{15}, [sondern]{18} [es]{20} [auferwecke]{19} [am]{21} [letzten]{22} [Tag]{23}.",
 "JHN.6.40": "[Denn]{2} [das]{1} [ist]{3} [der Wille]{4,5} [meines]{6,8} [Vaters]{7}: [dass]{9} [jeder]{10}, [der]{11} [den Sohn]{13,14} [sieht]{12} und{15} [an]{17} [ihn]{18} [glaubt]{16}, [ewiges]{21} [Leben]{20} [hat]{19}; und{22} [ich]{25} [werde]{23} [ihn]{24} [auferwecken]{23} [am]{26} [letzten]{27} [Tag]{28}.»",
 "JHN.6.41": "[Da]{2} [murrten]{1} [die Juden]{3,4} [über]{5} [ihn]{6}, [weil]{7} [er gesagt hatte]{8}: «[Ich]{9} [bin]{10} [das Brot]{11,12}, [das]{13} [vom]{15,16} [Himmel]{17} [herabgekommen ist]{14}»,",
 "JHN.6.42": "und{1} [sagten]{2}: «[Ist]{5} [das]{4} [nicht]{3} [Jesus]{6}, [der Sohn]{7,8} [Josefs]{9}, [dessen]{10} [Vater]{13,14} und{15} [Mutter]{16,17} [wir]{11} [kennen]{12}? [Wie]{18} [sagt er]{20} [jetzt]{19}: ‹[Ich bin]{25} [vom]{22,23} [Himmel]{24} [herabgekommen]{25}›?» ~21(" + SKIP_OTI + ")",
 "JHN.6.43": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihnen]{5}: «[Murrt]{7} [nicht]{6} [untereinander]{8,9}!",
 "JHN.6.44": "[Niemand]{1} [kann]{2} [zu]{4} [mir]{5} [kommen]{3}, [wenn nicht]{6,7} [der Vater]{8,9}, [der]{10} [mich]{12} [gesandt hat]{11}, [ihn]{14} [zieht]{13}; [und ich]{15} [werde]{16} [ihn]{17} [auferwecken]{16} [am]{18,19} [letzten]{20} [Tag]{21}.",
 "JHN.6.45": "[Es steht geschrieben]{1,2} [in]{3} [den Propheten]{4,5}: ‹[Und]{6} [sie werden]{7} [alle]{8} [von Gott]{10} [Belehrte]{9} [sein]{7}.› [Jeder]{11}, [der]{12} [vom]{14,15} [Vater]{16} [gehört]{13} und{17} [gelernt hat]{18}, [kommt]{19} [zu]{20} [mir]{21}.",
 "JHN.6.46": "[Nicht]{1} [dass]{2} [jemand]{6} [den Vater]{3,4} [gesehen hätte]{5}; [nur]{7,8} [der]{9}, der [von]{11} [Gott]{12,13} [ist]{10}, [der]{14} [hat]{15} [den Vater]{16,17} [gesehen]{15}.",
 "JHN.6.47": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Wer]{5} [glaubt]{6}, [hat]{7} [ewiges]{9} [Leben]{8}.",
 "JHN.6.48": "[Ich]{1} [bin]{2} [das Brot]{3,4} [des Lebens]{5,6}.",
 "JHN.6.49": "[Eure]{3} [Väter]{1,2} [haben]{4} [in]{5} [der Wüste]{6,7} [das Manna]{8,9} [gegessen]{4} und{10} [sind gestorben]{11}.",
 "JHN.6.50": "[Dies]{1} [ist]{2} [das Brot]{3,4}, [das]{5} [vom]{6,7} [Himmel]{8} [herabkommt]{9}, [damit]{10} [jemand]{11} [davon]{12,13} [isst]{14} und{15} [nicht]{16} [stirbt]{17}.",
 "JHN.6.51": "[Ich]{1} [bin]{2} [das]{3} [lebendige]{5,6} [Brot]{4}, [das]{7} [vom]{8,9} [Himmel]{10} [herabgekommen ist]{11}. [Wenn]{12} [jemand]{13} [von]{15} [diesem]{16} [Brot]{17,18} [isst]{14}, [wird er]{19} [in]{20} [Ewigkeit]{21,22} [leben]{19}. [Und]{23,26} [das Brot]{24,25}, [das]{27} [ich]{28} [geben werde]{29}, [ist]{33} [mein]{32} [Fleisch]{30,31}, [für]{34} [das Leben]{35,38} [der Welt]{36,37}.»",
 "JHN.6.52": "[Da]{2} [stritten]{1} [die Juden]{5,6} [untereinander]{3,4} [und sagten]{7}: «[Wie]{8} [kann]{9} [dieser]{10} [uns]{11} [sein]{15} [Fleisch]{13,14} [zu essen]{16} [geben]{12}?»",
 "JHN.6.53": "[Da]{2} [sagte]{1} [Jesus]{4,5} [zu ihnen]{3}: «[Amen]{6}, [amen]{7}, [ich sage]{8} [euch]{9}: [Wenn]{10} [ihr]{12} [das Fleisch]{13,14} [des Menschensohnes]{15-18} [nicht]{11} [esst]{12} und{19} [sein]{21} [Blut]{22,23} [nicht trinkt]{20}, [habt ihr]{25} [kein]{24} [Leben]{26} [in]{27} [euch]{28}.",
 "JHN.6.54": "[Wer]{1} [mein]{3} [Fleisch]{4,5} [isst]{2} und{6} [mein]{8} [Blut]{9,10} [trinkt]{7}, [hat]{11} [ewiges]{13} [Leben]{12}, [und ich]{14} [werde]{15} [ihn]{16} [auferwecken]{15} [am]{17} [letzten]{18} [Tag]{19}.",
 "JHN.6.55": "[Denn]{2} [mein]{4} [Fleisch]{1,3} [ist]{6} [wahre]{5} [Speise]{7}, und{8} [mein]{11} [Blut]{9,10} [ist]{13} [wahrer]{12} [Trank]{14}.",
 "JHN.6.56": "[Wer]{1} [mein]{3} [Fleisch]{4,5} [isst]{2} und{6} [mein]{8} [Blut]{9,10} [trinkt]{7}, [bleibt]{13} [in]{11} [mir]{12} [und ich]{14} [in]{15} [ihm]{16}.",
 "JHN.6.57": "[Wie]{1} [mich]{3} [der lebendige]{4,5} [Vater]{6} [gesandt hat]{2} [und ich]{7} [durch]{9} [den Vater]{10,11} [lebe]{8}, [so]{12} [wird]{17} [auch der]{16}, [der]{13} [mich]{15} [isst]{14}, [durch]{18} [mich]{19} [leben]{17}.",
 "JHN.6.58": "[Dies]{1} [ist]{2} [das Brot]{3,4}, [das]{5} [vom]{6} [Himmel]{7} [herabgekommen ist]{8}; [nicht]{9} [wie]{10} [die Väter]{12,13} [gegessen haben]{11} und{14} [gestorben sind]{15}: [Wer]{16} [dieses]{18} [Brot]{19,20} [isst]{17}, [wird]{21} [in]{22} [Ewigkeit]{23,24} [leben]{21}.»",
 "JHN.6.59": "[Das]{1} [sagte er]{2}, [als er]{5} [in]{3} [der Synagoge]{4} [in]{6} [Kafarnaum]{7} [lehrte]{5}.",
 "JHN.6.60": "[Viele]{1} [nun]{2} [von]{4} [seinen]{5,7} [Jüngern]{6}, [die das hörten]{3}, [sagten]{8}: «[Hart]{9} [ist]{10} [dieses]{13} [Wort]{11,12}; [wer]{14} [kann]{15} [es]{16} [hören]{17}?»",
 "JHN.6.61": "[Jesus]{3,4} [aber]{2} [wusste]{1} [bei]{5} [sich selbst]{6}, [dass]{7} [seine]{11,13} [Jünger]{12} [darüber]{9,10} [murrten]{8}, [und sagte]{14} [zu ihnen]{15}: «[Bringt]{18} [euch]{17} [das]{16} [zu Fall]{18}?",
 "JHN.6.62": "[Wenn]{1} [ihr]{3} [nun]{2} [den Menschensohn]{4-7} [hinaufsteigen]{8} [seht]{3} dorthin, [wo]{9} [er]{10} [vorher]{11,12} [war]{10} …?",
 "JHN.6.63": "[Der Geist]{1,2} [ist]{3} es, [der]{4} [lebendig macht]{5}; [das Fleisch]{6,7} [nützt]{9} [nichts]{8,10}. [Die Worte]{11,12}, [die]{13} [ich]{14} [zu euch]{16} [geredet habe]{15}, [sind]{18} [Geist]{17} und{19} [sind]{21} [Leben]{20}.",
 "JHN.6.64": "[Aber]{1} [es sind]{2} [einige]{5} [unter]{3} [euch]{4}, [die]{6} [nicht]{7} [glauben]{8}.» [Jesus]{13,14} [wusste]{9} [nämlich]{10} [von]{11} [Anfang]{12} [an]{11}, [wer]{15} [die]{17} [waren]{16}, die [nicht]{18} [glaubten]{19}, und{20} [wer]{21} [es war]{22}, [der]{23} [ihn]{25} [ausliefern würde]{24}.",
 "JHN.6.65": "Und{1} [er sagte]{2}: «[Darum]{3,4} [habe ich]{5} [euch]{6} [gesagt]{5}: [Niemand]{8} [kann]{9} [zu]{11} [mir]{12} [kommen]{10}, [wenn]{13} es [ihm]{17} [nicht]{14} [vom]{18,19} [Vater]{20} [gegeben]{16} [ist]{15}.» ~7(" + SKIP_OTI + ")",
 "JHN.6.66": "[Daraufhin]{1,2} [zogen sich]{8} [viele]{3} [seiner]{4,5,7} [Jünger]{6} [zurück]{9-11} und{12} [gingen]{16} [nicht mehr]{13} [mit]{14} [ihm]{15} [umher]{16}.",
 "JHN.6.67": "[Da]{2} [sagte]{1} [Jesus]{3,4} [zu den Zwölf]{5,6}: «[Wollt]{10} [etwa]{7} [auch]{8} [ihr]{9} [weggehen]{11}?»",
 "JHN.6.68": "[Simon]{3} [Petrus]{4} [antwortete]{1} [ihm]{2}: «[Herr]{5}, [zu]{6} [wem]{7} [sollen wir gehen]{8}? [Du hast]{12} [Worte]{9} [ewigen]{11} [Lebens]{10};",
 "JHN.6.69": "und{1} [wir]{2} [haben geglaubt]{3} und{4} [erkannt]{5}, [dass]{6} [du]{7} [der Heilige]{9,10} [Gottes]{11,12} [bist]{8}.»",
 "JHN.6.70": "[Jesus]{3,4} [antwortete]{1} [ihnen]{2}: «[Habe]{10} [nicht]{5} [ich]{6} [euch]{7}, [die Zwölf]{8,9}, [erwählt]{10}? Und{11} [einer]{14} [von]{12} [euch]{13} [ist]{16} [ein Teufel]{15}.»",
 "JHN.6.71": "[Er meinte]{1} [aber]{2} [Judas]{3,4}, den Sohn [des Simon]{5} [Iskariot]{6}; [der]{7} [sollte]{9} [ihn]{11} [nämlich]{8} [ausliefern]{10}, [einer]{12} [von]{13} [den Zwölf]{14,15}.",
 # ------------------------------------------------------------ Kapitel 7
 "JHN.7.1": "Und{1} [danach]{2,3} [zog]{4} [Jesus]{5,6} [in]{7} [Galiläa]{8,9} [umher]{4}; [denn]{11} [er wollte]{12} [nicht]{10} [in]{13} [Judäa]{14,15} [umherziehen]{16}, [weil]{17} [die Juden]{20,21} [ihn]{19} [zu töten]{22} [suchten]{18}.",
 "JHN.7.2": "[Nahe]{3} [war]{1} [aber]{2} [das Fest]{4,5} [der Juden]{6,7}, [das Laubhüttenfest]{8,9}.",
 "JHN.7.3": "[Da]{2} [sagten]{1} [seine]{5,7} [Brüder]{6} [zu]{3} [ihm]{4}: «[Geh weg]{8} [von hier]{9} und{10} [zieh]{11} [nach]{12} [Judäa]{13,14}, [damit]{15} [auch]{16} [deine]{17,19} [Jünger]{18} [deine]{21} [Werke]{22,23} [sehen]{20}, [die]{24} [du tust]{25}.",
 "JHN.7.4": "[Niemand]{1} [tut]{6} [nämlich]{2} [etwas]{3} [im Verborgenen]{4,5} und{7} [sucht]{8} [zugleich selbst]{9} [in der Öffentlichkeit]{10,11} [zu stehen]{12}. [Wenn]{13} [du]{15} [diese Dinge]{14} [tust]{15}, [offenbare]{16} [dich]{17} [der Welt]{18,19}!»",
 "JHN.7.5": "[Denn]{2} [auch]{1} [seine]{3,5} [Brüder]{4} [glaubten]{6} [nicht]{1} [an]{7} [ihn]{8}.",
 "JHN.7.6": "[Da]{2} [sagt]{1} [Jesus]{4,5} [zu ihnen]{3}: «[Meine]{8,9} [Zeit]{6,7} [ist]{11} [noch nicht]{10} [da]{11}; [eure]{15,16} [Zeit]{12,14} [aber]{13} [ist]{18} [immer]{17} [bereit]{19}.",
 "JHN.7.7": "[Die Welt]{3,4} [kann]{2} [euch]{6} [nicht]{1} [hassen]{5}; [mich]{7} [aber]{8} [hasst sie]{9}, [weil]{10} [ich]{11} [über]{13} [sie]{14} [bezeuge]{12}, [dass]{15} [ihre]{18} [Werke]{16,17} [böse]{19} [sind]{20}.",
 "JHN.7.8": "[Geht]{2} [ihr]{1} [hinauf]{2} [zum]{3,4} [Fest]{5}! [Ich]{6} [gehe]{8} [nicht]{7} [hinauf]{8} [zu]{9} [diesem]{12} [Fest]{10,11}, [denn]{13} [meine]{14,15} [Zeit]{16} [ist]{18} [noch nicht]{17} [erfüllt]{18}.»",
 "JHN.7.9": "[Nachdem er]{3} [aber]{2} [das]{1} [gesagt hatte]{3}, [blieb]{5} [er]{4} [in]{6} [Galiläa]{7,8}.",
 "JHN.7.10": "[Als]{1} [aber]{2} [seine]{4,6} [Brüder]{5} [zum]{7,8} [Fest]{9} [hinaufgegangen waren]{3}, [da]{10} [ging]{13} [auch]{11} [er]{12} [hinauf]{13}, [nicht]{14} [öffentlich]{15}, [sondern]{16} [gleichsam]{17} [im Verborgenen]{18,19}.",
 "JHN.7.11": "[Die Juden]{1,3} [nun]{2} [suchten]{4} [ihn]{5} [am]{6,7} [Fest]{8} und{9} [sagten]{10}: «[Wo]{11} [ist]{12} [er]{13}?»",
 "JHN.7.12": "Und{1} [es gab]{5} [viel]{6} [Gemurmel]{2} [über]{3} [ihn]{4} [in]{7} [der Menge]{8,9}. [Die einen]{10,11} [sagten]{12}: «[Er ist]{15} [gut]{14}.» [Andere]{16} [aber]{17} [sagten]{18}: «[Nein]{19}, [sondern]{20} [er verführt]{21} [das Volk]{22,23}.» ~13(" + SKIP_OTI + ")",
 "JHN.7.13": "[Niemand]{1} [jedoch]{2} [redete]{4} [offen]{3} [über]{5} [ihn]{6}, [aus]{7} [Furcht]{8,9} [vor den Juden]{10,11}.",
 "JHN.7.14": "[Als]{5} [aber]{2} [das Fest]{3,4} [schon]{1} [zur Hälfte vorüber war]{5}, [ging]{6} [Jesus]{7} [hinauf]{6} [in]{8} [den Tempel]{9,10} und{11} [lehrte]{12}.",
 "JHN.7.15": "[Da]{2} [wunderten sich]{1} [die Juden]{3,4} [und sagten]{5}: «[Wie]{6} [kennt]{9} [dieser]{7} [die Schriften]{8}, obwohl er [nicht]{10} [gelernt hat]{11}?»",
 "JHN.7.16": "[Da]{2} [antwortete]{1} [Jesus]{4,5} [ihnen]{3} und{6} [sagte]{7}: «[Meine]{8,9} [Lehre]{10} [ist]{12} [nicht]{11} [meine]{13}, [sondern]{14} [die dessen]{15}, der [mich]{17} [gesandt hat]{16}.",
 "JHN.7.17": "[Wenn]{1} [jemand]{2} [seinen]{6} [Willen]{4,5} [tun]{7} [will]{3}, [wird er]{8} [an]{9} [der Lehre]{10,11} [erkennen]{8}, [ob]{12} sie [von]{13} [Gott]{14,15} [ist]{16} [oder]{17} ob [ich]{18} [von]{19} [mir selbst]{20} [aus]{19} [rede]{21}.",
 "JHN.7.18": "[Wer]{1} [von]{2} [sich selbst]{3} [aus]{2} [redet]{4}, [sucht]{9} [seine]{7} [eigene]{8} [Ehre]{5,6}; [wer]{10} [aber]{11} [die Ehre]{13,14} [dessen]{15} [sucht]{12}, der [ihn]{17} [gesandt hat]{16}, [der]{18} [ist]{20} [wahrhaftig]{19}, und{21} [Unrecht]{22} [ist]{26} [nicht]{25} [in]{23} [ihm]{24}.",
 "JHN.7.19": "[Hat]{3} [nicht]{1} [Mose]{2} [euch]{4} [das Gesetz]{5,6} [gegeben]{3}? Und{7} [niemand]{8} [von]{9} [euch]{10} [tut]{11} [das Gesetz]{12,13}. [Warum]{14} [sucht ihr]{16} [mich]{15} [zu töten]{17}?»",
 "JHN.7.20": "[Die Menge]{2,3} [antwortete]{1}: «[Du hast]{5} [einen Dämon]{4}! [Wer]{6} [sucht]{8} [dich]{7} [zu töten]{9}?»",
 "JHN.7.21": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihnen]{5}: «[Ein einziges]{6} [Werk]{7} [habe ich getan]{8}, und{9} [ihr alle]{10} [wundert euch]{11}.",
 "JHN.7.22": "[Darum]{1,2}: [Mose]{3} [hat]{4} [euch]{5} [die Beschneidung]{6,7} [gegeben]{4} – [nicht]{8} [dass]{9} sie [von]{10} [Mose]{11,12} [stammt]{13}, [sondern]{14} [von]{15} [den Vätern]{16,17} –, und{18} [ihr beschneidet]{21} [einen Menschen]{22} [am]{19} [Sabbat]{20}.",
 "JHN.7.23": "[Wenn]{1} [ein Mensch]{4} [am]{5} [Sabbat]{6} [die Beschneidung]{2} [empfängt]{3}, [damit]{7} [das Gesetz]{10,11} [des Mose]{12} [nicht]{8} [gebrochen wird]{9}, [zürnt ihr]{14} [mir]{13}, [weil]{15} [ich]{19} [einen ganzen]{16} [Menschen]{17} [am]{20} [Sabbat]{21} [gesund]{18} [gemacht habe]{19}?",
 "JHN.7.24": "[Urteilt]{2} [nicht]{1} [nach]{3} [dem Augenschein]{4}, [sondern]{5} [urteilt]{9} [mit gerechtem]{6,7} [Urteil]{8}!»",
 "JHN.7.25": "[Da]{2} [sagten]{1} [einige]{3} [von]{4} [den Leuten aus Jerusalem]{5,6}: «[Ist]{9} [das]{8} [nicht]{7} der, [den]{10} [sie]{11} [zu töten]{12} [suchen]{11}?",
 "JHN.7.26": "Und{1} [siehe]{2}, [er redet]{4} [offen]{3}, und{5} [sie sagen]{8} [ihm]{7} [nichts]{6}. [Haben]{11} [etwa]{9} [die Oberen]{12,13} [wirklich]{10} [erkannt]{11}, [dass]{14} [dieser]{15} [der Christus]{17,18} [ist]{16}?",
 "JHN.7.27": "[Aber]{1} [von diesem]{2} [wissen wir]{3}, [woher]{4} [er ist]{5}; [wenn]{9} [aber]{7} [der Christus]{6,8} [kommt]{10}, [weiss]{12} [niemand]{11}, [woher]{13} [er ist]{14}.»",
 "JHN.7.28": "[Da]{2} [rief]{1} [Jesus]{7,8} [laut]{1}, [als er]{6} [im]{3,4} [Tempel]{5} [lehrte]{6}, [und sagte]{9,10}: «[Mich]{11} [kennt ihr]{12}, und{13} [ihr wisst]{14}, [woher]{15} [ich bin]{16}! Und{17} [von]{18} [mir selbst]{19} [aus]{18} [bin ich]{21} [nicht]{20} [gekommen]{21}, [sondern]{22} [der]{25} [mich]{27} [gesandt hat]{26}, [ist]{23} [wahrhaftig]{24}; [ihn]{28} [kennt]{31} [ihr]{29} [nicht]{30}.",
 "JHN.7.29": "[Ich]{1} [kenne]{2} [ihn]{3}, [denn]{4} [ich bin]{7} [von]{5} [ihm]{6}, [und er]{8} [hat]{10} [mich]{9} [gesandt]{10}.»",
 "JHN.7.30": "[Da]{2} [suchten sie]{1} [ihn]{3} [festzunehmen]{4}, und{5} [niemand]{6} [legte]{7} [die Hand]{10,11} [an]{8} [ihn]{9}, [weil]{12} [seine]{15,17} [Stunde]{16} [noch nicht]{13} [gekommen war]{14}.",
 "JHN.7.31": "[Viele]{5} [aus]{1} [der Menge]{2,3} [aber]{4} [glaubten]{6} [an]{7} [ihn]{8} und{9} [sagten]{10}: «[Wird]{18} [der Christus]{11,12}, [wenn]{13} [er kommt]{14}, [etwa]{15} [mehr]{16} [Zeichen]{17} [tun]{18}, [als]{19} [dieser]{20} [getan hat]{21}?»",
 "JHN.7.32": "[Die Pharisäer]{2,3} [hörten]{1} [die Menge]{4,5} [das]{9} [über]{7} [ihn]{8} [murmeln]{6}, und{10} [die Hohepriester]{12,13} und{14} [die Pharisäer]{15,16} [sandten]{11} [Diener]{17} [aus]{11}, [um]{18} [ihn]{20} [festzunehmen]{19}.",
 "JHN.7.33": "[Da]{2} [sagte]{1} [Jesus]{3,4}: «[Noch]{5} [eine kleine]{7} [Zeit]{6} [bin ich]{10} [bei]{8} [euch]{9}, und{11} dann [gehe ich]{12} [zu]{13} [dem]{14}, der [mich]{16} [gesandt hat]{15}.",
 "JHN.7.34": "[Ihr werdet]{1} [mich]{2} [suchen]{1} und{3} [nicht]{4} [finden]{5}, und{6} [wo]{7} [ich]{9} [bin]{8}, dahin [könnt]{12} [ihr]{10} [nicht]{11} [kommen]{13}.»",
 "JHN.7.35": "[Da]{2} [sagten]{1} [die Juden]{3,4} [zueinander]{5,6}: «[Wohin]{7} [will]{9} [dieser]{8} [gehen]{10}, [dass]{11} [wir]{12} [ihn]{15} [nicht]{13} [finden werden]{14}? [Will er]{22} [etwa]{16} [in]{17} [die Diaspora]{18,19} [unter den Griechen]{20,21} [gehen]{23} und{24} [die Griechen]{26,27} [lehren]{25}?",
 "JHN.7.36": "[Was]{1} [ist]{2} [das]{5} [für ein Wort]{3,4}, [das]{6} [er gesagt hat]{7}: ‹[Ihr werdet]{8} [mich]{9} [suchen]{8} und{10} [nicht]{11} [finden]{12}, und{13} [wo]{14} [ich]{16} [bin]{15}, dahin [könnt]{19} [ihr]{17} [nicht]{18} [kommen]{20}›?»",
 "JHN.7.37": "[Am]{1,3} [letzten]{4} [Tag]{5} [aber]{2}, [dem grossen]{6,7} [des Festes]{8,9}, [stand]{10} [Jesus]{11,12} [da]{10} und{13} [rief laut]{14} [und sagte]{15}: «[Wenn]{16} [jemand]{17} [Durst hat]{18}, [soll er]{19} [zu]{20} [mir]{21} [kommen]{19} und{22} [trinken]{23}!",
 "JHN.7.38": "[Wer]{1} [an]{3} [mich]{4} [glaubt]{2} – [wie]{5} [die Schrift]{7,8} [gesagt hat]{6}: ‹[Ströme]{9} [lebendigen]{16} [Wassers]{15} [werden]{14} [aus]{10} [seinem]{11,13} [Inneren]{12} [fliessen]{14}.›»",
 "JHN.7.39": "[Das]{1} [sagte er]{3} [aber]{2} [über]{4} [den Geist]{5,6}, [den]{7} [die]{10} [empfangen sollten]{8,9}, die [an]{12} [ihn]{13} [glaubten]{11}; [denn]{15} [der Geist]{17} [war]{16} [noch nicht]{14} da, [weil]{18} [Jesus]{19} [noch nicht]{20} [verherrlicht worden war]{21}.",
 "JHN.7.40": "Einige [aus]{1} [der Menge]{2,3} [nun]{4}, die [diese]{8} [Worte]{6,7} [hörten]{5}, [sagten]{9}: «[Das]{10} [ist]{11} [wahrhaftig]{12} [der Prophet]{13,14}.»",
 "JHN.7.41": "[Andere]{1} [sagten]{2}: «[Das]{3} [ist]{4} [der Christus]{5,6}.» [Wieder andere]{7} [aber]{8} [sagten]{9}: «[Kommt]{17} [denn]{11} [der Christus]{15,16} [etwa]{10} [aus]{12} [Galiläa]{13,14}?",
 "JHN.7.42": "[Hat]{4} [nicht]{1} [die Schrift]{2,3} [gesagt]{4}, [dass]{5} [der Christus]{19,20} [aus]{6} [der Nachkommenschaft]{7,8} [Davids]{9} und{10} [aus]{11} [Betlehem]{12}, [dem Dorf]{13,14}, [wo]{15} [David]{17} [war]{16}, [kommt]{18}?»",
 "JHN.7.43": "[So]{2} [entstand]{3} [seinetwegen]{7,8} [eine Spaltung]{1} [in]{4} [der Menge]{5,6}.",
 "JHN.7.44": "[Einige]{1} [von]{4} [ihnen]{5} [aber]{2} [wollten]{3} [ihn]{7} [festnehmen]{6}, [doch]{8} [niemand]{9} [legte]{10} [die Hände]{13,14} [an]{11} [ihn]{12}.",
 "JHN.7.45": "[Die Diener]{3,4} [kamen]{1} [nun]{2} [zu]{5} [den Hohepriestern]{6,7} und{8} [Pharisäern]{9} zurück, und{10} [jene]{13} [sagten]{11} [zu ihnen]{12}: «[Warum]{14,15} [habt ihr]{17} [ihn]{18} [nicht]{16} [gebracht]{17}?»",
 "JHN.7.46": "[Die Diener]{2,3} [antworteten]{1}: «[Noch nie]{4} [hat]{5} [ein Mensch]{7} [so]{6} [geredet]{5}.»",
 "JHN.7.47": "[Da]{2} [antworteten]{1} [ihnen]{3} [die Pharisäer]{4,5}: «[Habt]{9} [etwa]{6} [auch]{7} [ihr]{8} [euch verführen lassen]{9}?",
 "JHN.7.48": "[Hat]{6} [etwa]{1} [einer]{2} [von]{3} [den Oberen]{4,5} [an]{7} [ihn]{8} [geglaubt]{6} [oder]{9} [von]{10} [den Pharisäern]{11,12}?",
 "JHN.7.49": "[Aber]{1} [dieses]{4} [Volk]{2,3}, [das]{5} [das Gesetz]{8,9} [nicht]{6} [kennt]{7} – [verflucht]{10} [sind sie]{11}!»",
 "JHN.7.50": "[Nikodemus]{2}, [der]{5} [früher]{9} [zu]{7} [ihm]{8} [gekommen war]{6} und [einer]{10} [von]{12} [ihnen]{13} [war]{11}, [sagt]{1} [zu]{3} [ihnen]{4}:",
 "JHN.7.51": "«[Richtet]{5} [etwa]{1} [unser]{4} [Gesetz]{2,3} [einen Menschen]{6,7}, [ohne]{8,9} [ihn]{12,13} [zuerst]{11} [angehört]{10} [und]{14} [erkannt zu haben]{15}, [was]{16} [er tut]{17}?»",
 "JHN.7.52": "[Sie antworteten]{1} und{2} [sagten]{3} [zu ihm]{4}: «[Bist]{11} [etwa]{5} [auch]{6} [du]{7} [aus]{8} [Galiläa]{9,10}? [Forsche nach]{12} und{13} [sieh]{14}, [dass]{15} [aus]{16} [Galiläa]{17,18} [kein]{20} [Prophet]{19} [aufsteht]{21}.»",
 "JHN.7.53": "⟦[Und]{1} [jeder]{3} [ging]{2} [in]{4} [sein]{5,7} [Haus]{6}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 6
 "JHN.6.1": "[Nachher]{1,2} [isch]{3} [de Jesus]{4,5} [furtgange]{3} [as ander Ufer]{6} [vom See]{7,8} [vo Galiläa]{9,10}, [vom See vo Tiberias]{11,12}.",
 "JHN.6.2": "[E grossi]{5} [Mängi]{4} [aber]{2} [isch]{1} [ihm]{3} [nachegloffe]{1}, [wil]{6} [si]{7} [d Zeiche]{8,9} [gseh händ]{7}, [wo]{10} [er]{11} [a]{12} [de Chranke]{13,14} [gmacht hät]{11}.",
 "JHN.6.3": "[De Jesus]{6} [aber]{2} [isch]{1} [uf]{3} [de Bärg]{4,5} [ufegstige]{1} und{7} [isch]{9} [dört]{8} [mit]{10} [sine]{11,13} [Jünger]{12} [gsässe]{9}.",
 "JHN.6.4": "[Nöch]{3} [isch]{1} [aber]{2} [s Passa]{4,5} [gsii]{1}, [s Fäscht]{6,7} [vo de Jude]{8,9}.",
 "JHN.6.5": "[Wo]{1} [de Jesus]{5,6} [also]{2} [d Auge]{3,4} [ufghebt hät]{1} und{7} [gseh hät]{8}, [dass]{9} [e grossi]{10} [Mängi]{11} [zu]{13} [ihm]{14} [chunnt]{12}, [seit er]{15} [zum]{16} [Philippus]{17}: «[Vo wo]{18} [söled mer]{19} [Broot]{20} [chaufe]{19}, [demit]{21} [die]{23} [z ässe händ]{22}?»",
 "JHN.6.6": "[Das]{1} [hät er]{3} [aber]{2} [gseit]{3}, [zum]{4} [en]{5} [prüefe]{4}; [er sälber]{6} [hät]{8} [nämli]{7} [gwüsst]{8}, [was]{9} [er vorghaa hät]{10} [z mache]{11}.",
 "JHN.6.7": "[De Philippus]{3} [hät]{1} [ihm]{2} [gantwortet]{1}: «[Broot]{6} [für zweihundert]{4} [Denar]{5} [länged]{8} [nöd]{7} [für si]{9}, [dass]{10} [jede]{11} au nur [es bitzeli]{12,13} [überchunnt]{14}.»",
 "JHN.6.8": "[Eine]{3} [vo]{4} [sine]{5,7} [Jünger]{6}, [de Andreas]{8}, [de Brüeder]{9,10} [vom Simon]{11} [Petrus]{12}, [seit]{1} [zu ihm]{2}:",
 "JHN.6.9": "«[Da]{3} [isch]{1} [en Bueb]{2}, [wo]{4} [föif]{6} [Gerschtebroot]{7,8} und{9} [zwei]{10} [Fisch]{11} [hät]{5}; [aber]{12} [was]{14} [isch]{15} [das]{13} [für]{16} [so vili]{17}?»",
 "JHN.6.10": "[De Jesus]{2,3} [hät gseit]{1}: «[Lönd]{4} [d Lüüt]{5,6} [abhocke]{7}!» [Es hät]{8} [aber]{9} [vil]{11} [Gras]{10} [ghaa]{8} [a]{12} [däm]{13} [Ort]{14}. [Also]{16} [sind]{15} [d Manne]{17,18} [abghocket]{15}, [öppe]{21} [föiftuusig]{22} [a de Zaal]{19,20}.",
 "JHN.6.11": "[De Jesus]{5,6} [hät]{1} [also]{2} [d Broot]{3,4} [gnoo]{1}, und{7} [nachdem er dankt hät]{8}, [hät er s verteilt]{9} [a d]{10} [Lüüt, wo da gläge sind]{11}, [gnauso]{12} [au]{13} [vo]{14} [de Fisch]{15,16}, [so vil]{17} [si händ wele]{18}.",
 "JHN.6.12": "[Wo]{1} [si]{3} [aber]{2} [satt worde sind]{3}, [seit er]{4} [zu sine]{5,7} [Jünger]{6}: «[Sammled]{8} [di übrigblibne]{9,10} [Brocke]{11} [ii]{8}, [demit]{12} [nüüt]{13,14} [verlore gaat]{15}.»",
 "JHN.6.13": "[Also]{2} [händ si gsammlet]{1} und{3} [händ]{4} [zwölf]{5} [Chörb]{6} [mit Brocke]{7} [gfüllt]{4} [vo]{8} [de föif]{9,10} [Gerschtebroot]{11-13}, [wo]{14} [de Lüüt]{16}, [wo ggässe händ]{17}, [übrig blibe sind]{15}.",
 "JHN.6.14": "[Wo]{4} [also]{2} [d Lüüt]{1,3} [s Zeiche]{7} [gseh händ]{4}, [wo]{5} [er gmacht hät]{6}, [händ si gseit]{8}: «[Das]{10} [isch]{11} [würkli]{12} [de Prophet]{13,14}, [wo]{15} [i]{17} [d Wält]{18,19} [chunnt]{16}.» ~9(" + SKIP_OTI_G + ")",
 "JHN.6.15": "[Wil]{3} [de Jesus]{1} [jetzt]{2} [gmerkt hät]{3}, [dass]{4} [si wänd]{5} [choo]{6} und{7} [en]{9} [mit Gwalt packe]{8}, [für]{10} en [zum König]{12} [z mache]{11}, [hät er sich]{13} [wider]{14} [uf]{15} [de Bärg]{16,17} [zrugzoge]{13}, [ganz elei]{18,19}.",
 "JHN.6.16": "[Wo]{1} [s]{4} [aber]{2} [Aabig]{3} [worde isch]{4}, [sind]{5} [sini]{6,8} [Jünger]{7} [abe]{5} [an]{9} [See]{10,11} [gange]{5}",
 "JHN.6.17": "und{1} [sind]{2} [i]{3} [es Boot]{4} [gstige]{2} und [sind]{5} [über]{6} [de See]{7,8} [uf]{9} [Kafarnaum]{10} [gfaare]{5}. Und{11} [es isch]{14} [scho]{13} [dunkel]{12} [gsii]{14}, und{15} [de Jesus]{20,21} [isch]{17} [no nöd]{16} [zu]{18} [ine]{19} [choo]{17}.",
 "JHN.6.18": "[Und]{2} [de See]{1,3} [isch ufgwüelt worde]{7}, wil [en starche]{5} [Wind]{4} [gwäit hät]{6}.",
 "JHN.6.19": "[Wo si]{1} [also]{2} [öppe]{3} [föifezwänzg]{5,6} [oder]{7} [driissg]{8} [Stadie]{4} [wiit grueret händ]{1}, [gsehnd si]{9} [de Jesus]{10,11} [uf]{13} [em See]{14,15} [laufe]{12} und{16} [nöch]{17} [as]{18} [Boot]{19} [häre choo]{20}, und{21} [si händ Angscht übercho]{22}.",
 "JHN.6.20": "[Er]{1} [aber]{2} [seit]{3} [zu ine]{4}: «[Ich]{5} [bi s]{6}; [händ]{8} [kei]{7} [Angscht]{8}!»",
 "JHN.6.21": "[Si händ]{1} [en]{4} [also]{2} [is]{5,6} [Boot]{7} [nää]{3} [wele]{1}, und{8} [sofort]{9} [isch]{10} [s Boot]{11,12} [am]{13,14} [Land]{15} [gsii]{10}, [wo]{16,17} [si hiigfaare sind]{18}.",
 "JHN.6.22": "[Am nächschte Tag]{1,2} [hät]{10} [d Mängi]{3,4}, [wo]{5} [am andere Ufer]{7} [vom See]{8,9} [gstande isch]{6}, [gseh]{10}, [dass]{11} [kei]{14} [anders]{13} [Boot]{12} [dört]{16} [gsii isch]{15} [usser]{17,18} [eim]{19}, und{20} [dass]{21} [de Jesus]{27,28} [nöd]{22} [mit]{23} [sine]{24,26} [Jünger]{25} [is]{29,30} [Boot]{31} [iigstige isch]{23}, [sondern]{32} dass [sini]{34,36} [Jünger]{35} [elei]{33} [abgfaare sind]{37}.",
 "JHN.6.23": "[Es sind]{2} [aber]{1} [Boot]{3} [vo]{4} [Tiberias]{5} [choo]{2}, [i d Nöchi]{6} [vom Ort]{7,8}, [wo]{9} [si]{10} [s Broot]{11,12} [ggässe händ]{10}, [nachdem]{13} [de Herr]{14,15} [dankt hät]{13}.",
 "JHN.6.24": "[Wo]{1} [also]{2} [d Mängi]{4,5} [gseh hät]{3}, [dass]{6} [de Jesus]{7} [nöd]{8} [dört]{10} [isch]{9}, [au nöd]{11} [sini]{12,14} [Jünger]{13}, [sind si]{15,16} [i]{17} [d Boot]{18,19} [iigstige]{15,16} und{20} [sind]{21} [uf]{22} [Kafarnaum]{23} [choo]{21} [und händ]{24} [de Jesus]{25,26} [gsuecht]{24}.",
 "JHN.6.25": "Und{1} [wo si]{2} [en]{3} [am andere Ufer]{4} [vom See]{5,6} [gfunde händ]{2}, [händ si]{7} [zu ihm]{8} [gseit]{7}: «[Rabbi]{9}, [wänn]{10} [bisch]{12} [da]{11} [häre choo]{12}?»",
 "JHN.6.26": "[De Jesus]{3,4} [hät]{1} [ine]{2} [gantwortet]{1} und{5} [hät gseit]{6}: «[Amen]{7}, [amen]{8}, [ich säge]{9} [eu]{10}: [Ir sueched]{11} [mich]{12} [nöd]{13}, [wil]{14} [ir]{15} [Zeiche]{16} [gseh händ]{15}, [sondern]{17} [wil]{18} [ir]{19} [vo]{20} [de Broot]{21,22} [ggässe händ]{19} und{23} [satt worde sind]{24}.",
 "JHN.6.27": "[Schaffed]{1} [nöd]{2} [für s]{3} [Ässe]{4}, [wo]{5} [vergaat]{6}, [sondern]{7} [für s Ässe]{8,9}, [wo]{10} [bliibt]{11} [bis is]{12} [ewig]{14} [Läbe]{13}, [wo]{15} [de Mänschesohn]{16-19} [eu]{20} [wird gää]{21}; [dänn]{23} [ihn]{22} [hät]{26} [de Vatter]{24,25}, [Gott]{27,28}, [mit sim Siegel bestätiget]{26}.»",
 "JHN.6.28": "[Da]{2} [händ si]{1} [zu]{3} [ihm]{4} [gseit]{1}: «[Was]{5} [söled mer mache]{6}, [demit]{7} [mer]{8} [d Wärch]{9,10} [vo Gott]{11,12} [tüend]{8}?»",
 "JHN.6.29": "[De Jesus]{2,3} [hät gantwortet]{1} und{4} [zu ine]{6} [gseit]{5}: «[Das]{7} [isch]{8} [s Wärch]{9,10} [vo Gott]{11,12}: [dass]{13} [ir]{14} [a]{15} dä [glaubed]{14}, [wo]{16} [er]{18} [gschickt hät]{17}.»",
 "JHN.6.30": "[Da]{2} [händ si]{1} [zu ihm]{3} [gseit]{1}: «[Was]{4} [machsch]{6} [du]{7} [dänn]{5} [für es Zeiche]{8}, [demit]{9} [mer s gsehnd]{10} und{11} [dir]{13} [glaubed]{12}? [Was]{14} [wirksch du]{15}?",
 "JHN.6.31": "[Üsi]{3} [Vätter]{1,2} [händ]{6} [s Manna]{4,5} [i]{7} [de Wüeschti]{8,9} [ggässe]{6}, [wie]{10} [s gschribe staat]{11,12}: ‹[Broot]{13} [vom]{14,15} [Himmel]{16} [hät er]{17} [ine]{18} [z ässe]{19} [gää]{17}.›»",
 "JHN.6.32": "[Da]{2} [hät]{1} [de Jesus]{4,5} [zu ine]{3} [gseit]{1}: «[Amen]{6}, [amen]{7}, [ich säge]{8} [eu]{9}: [Nöd]{10} [de Mose]{11} [hät]{12} [eu]{13} [s Broot]{14,15} [vom]{16,17} [Himmel]{18} [gää]{12}, [sondern]{19} [min]{22} [Vatter]{20,21} [git]{23} [eu]{24} [s]{25} [wahre]{30,31} [Broot]{26} [vom]{27,28} [Himmel]{29}.",
 "JHN.6.33": "[Dänn]{2} [s Broot]{1,3} [vo Gott]{4,5} [isch]{6} [das, wo]{7} [vom]{9,10} [Himmel]{11} [abechunnt]{8} und{12} [de Wält]{15,16} [Läbe]{13} [git]{14}.»",
 "JHN.6.34": "[Da]{2} [händ si]{1} [zu]{3} [ihm]{4} [gseit]{1}: «[Herr]{5}, [gib]{7} [üs]{8} [immer]{6} [das]{11} [Broot]{9,10}!»",
 "JHN.6.35": "[De Jesus]{3,4} [hät]{1} [zu ine]{2} [gseit]{1}: «[Ich]{5} [bi]{6} [s Broot]{7,8} [vom Läbe]{9,10}. [Wer]{11} [zu]{13} [mir]{14} [chunnt]{12}, [wird sicher nie]{15,16} [Hunger ha]{17}, und{18} [wer]{19} [a]{21} [mich]{22} [glaubt]{20}, [wird nie meh]{23,24,26} [Durscht ha]{25}.",
 "JHN.6.36": "[Aber]{1} [ich ha]{2} [eu]{3} [gseit]{2}: [Ir händ]{6} [mich]{7} [zwar]{5} [gseh]{6}, [und]{8} [glaubed]{10} [glich nöd]{9}. ~4(" + SKIP_OTI_G + ")",
 "JHN.6.37": "[Alles]{1}, [wo]{2} [mir]{4} [de Vatter]{5,6} [git]{3}, [wird]{9} [zu]{7} [mir]{8} [choo]{9}, und{10} [wer]{11} [zu]{13} [mir]{14} [chunnt]{12}, dä [rüer ich]{17,18} [sicher nöd]{15,16} [use]{17,18}.",
 "JHN.6.38": "[Dänn]{1} [ich bi]{2} [vom]{3,4} [Himmel]{5} [abechoo]{2}, [nöd]{6} [für]{7} [min]{11,12} [Wille]{9,10} [z tue]{8}, [sondern]{13} [de Wille]{14,15} [vo däm]{16}, wo [mich]{18} [gschickt hät]{17}.",
 "JHN.6.39": "[Das]{1} [aber]{2} [isch]{3} [de Wille]{4,5} [vo däm]{6}, wo [mich]{8} [gschickt hät]{7}: [dass]{9} [ich]{15} [vo]{16,17} [allem]{10}, [wo]{11} [er]{12} [mir]{13} [gää hät]{12}, [nüüt]{14} [verliere]{15}, [sondern]{18} [s]{20} [uferwecke]{19} [am]{21} [letschte]{22} [Tag]{23}.",
 "JHN.6.40": "[Dänn]{2} [das]{1} [isch]{3} [de Wille]{4,5} [vo mim]{6,8} [Vatter]{7}: [dass]{9} [jede]{10}, [wo]{11} [de Sohn]{13,14} [gseht]{12} und{15} [a]{17} [en]{18} [glaubt]{16}, [ewigs]{21} [Läbe]{20} [hät]{19}; und{22} [ich]{25} [wirde]{23} [en]{24} [uferwecke]{23} [am]{26} [letschte]{27} [Tag]{28}.»",
 "JHN.6.41": "[Da]{2} [händ]{1} [d Jude]{3,4} [über]{5} [en]{6} [gmuulet]{1}, [wil]{7} [er gseit hät]{8}: «[Ich]{9} [bi]{10} [s Broot]{11,12}, [wo]{13} [vom]{15,16} [Himmel]{17} [abechoo isch]{14}»,",
 "JHN.6.42": "und{1} [händ gseit]{2}: «[Isch]{5} [das]{4} [nöd]{3} [de Jesus]{6}, [de Sohn]{7,8} [vom Josef]{9}, [vo däm]{10} [mir]{11} [de Vatter]{13,14} und{15} [d Mueter]{16,17} [känned]{12}? [Wie]{18} [seit er]{20} [jetzt]{19}: ‹[Ich bi]{25} [vom]{22,23} [Himmel]{24} [abechoo]{25}›?» ~21(" + SKIP_OTI_G + ")",
 "JHN.6.43": "[De Jesus]{2} [hät gantwortet]{1} und{3} [zu ine]{5} [gseit]{4}: «[Muuled]{7} [nöd]{6} [undereinand]{8,9}!",
 "JHN.6.44": "[Niemer]{1} [cha]{2} [zu]{4} [mir]{5} [choo]{3}, [wänn nöd]{6,7} [de Vatter]{8,9}, [wo]{10} [mich]{12} [gschickt hät]{11}, [en]{14} [zieht]{13}; [und ich]{15} [wirde]{16} [en]{17} [uferwecke]{16} [am]{18,19} [letschte]{20} [Tag]{21}.",
 "JHN.6.45": "[Es staat gschribe]{1,2} [i]{3} [de Prophete]{4,5}: ‹[Und]{6} [si wärded]{7} [alli]{8} [vo Gott]{10} [glehrt]{9} [sii]{7}.› [Jede]{11}, [wo]{12} [vom]{14,15} [Vatter]{16} [ghört]{13} und{17} [glernt hät]{18}, [chunnt]{19} [zu]{20} [mir]{21}.",
 "JHN.6.46": "[Nöd]{1} [dass]{2} [öpper]{6} [de Vatter]{3,4} [gseh hett]{5}; [nur]{7,8} [dä]{9}, wo [vo]{11} [Gott]{12,13} [isch]{10}, [dä]{14} [hät]{15} [de Vatter]{16,17} [gseh]{15}.",
 "JHN.6.47": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Wer]{5} [glaubt]{6}, [hät]{7} [ewigs]{9} [Läbe]{8}.",
 "JHN.6.48": "[Ich]{1} [bi]{2} [s Broot]{3,4} [vom Läbe]{5,6}.",
 "JHN.6.49": "[Eui]{3} [Vätter]{1,2} [händ]{4} [i]{5} [de Wüeschti]{6,7} [s Manna]{8,9} [ggässe]{4} und{10} [sind gstorbe]{11}.",
 "JHN.6.50": "[Das]{1} [isch]{2} [s Broot]{3,4}, [wo]{5} [vom]{6,7} [Himmel]{8} [abechunnt]{9}, [demit]{10} [öpper]{11} [devo]{12,13} [isst]{14} und{15} [nöd]{16} [stirbt]{17}.",
 "JHN.6.51": "[Ich]{1} [bi]{2} [s]{3} [läbig]{5,6} [Broot]{4}, [wo]{7} [vom]{8,9} [Himmel]{10} [abechoo isch]{11}. [Wänn]{12} [öpper]{13} [vo]{15} [däm]{16} [Broot]{17,18} [isst]{14}, [wird er]{19} [für]{20} [immer]{21,22} [läbe]{19}. [Und]{23,26} [s Broot]{24,25}, [wo]{27} [ich]{28} [wirde gää]{29}, [isch]{33} [mis]{32} [Fleisch]{30,31}, [für]{34} [s Läbe]{35,38} [vo de Wält]{36,37}.»",
 "JHN.6.52": "[Da]{2} [händ]{1} [d Jude]{5,6} [undereinand]{3,4} [gstritte]{1} [und gseit]{7}: «[Wie]{8} [cha]{9} [dä]{10} [üs]{11} [sis]{15} [Fleisch]{13,14} [z ässe]{16} [gää]{12}?»",
 "JHN.6.53": "[Da]{2} [hät]{1} [de Jesus]{4,5} [zu ine]{3} [gseit]{1}: «[Amen]{6}, [amen]{7}, [ich säge]{8} [eu]{9}: [Wänn]{10} [ir]{12} [s Fleisch]{13,14} [vom Mänschesohn]{15-18} [nöd]{11} [ässed]{12} und{19} [sis]{21} [Bluet]{22,23} [nöd trinked]{20}, [händ ir]{25} [kei]{24} [Läbe]{26} [i]{27} [eu]{28}.",
 "JHN.6.54": "[Wer]{1} [mis]{3} [Fleisch]{4,5} [isst]{2} und{6} [mis]{8} [Bluet]{9,10} [trinkt]{7}, [hät]{11} [ewigs]{13} [Läbe]{12}, [und ich]{14} [wirde]{15} [en]{16} [uferwecke]{15} [am]{17} [letschte]{18} [Tag]{19}.",
 "JHN.6.55": "[Dänn]{2} [mis]{4} [Fleisch]{1,3} [isch]{6} [wahrs]{5} [Ässe]{7}, und{8} [mis]{11} [Bluet]{9,10} [isch]{13} [wahre]{12} [Trank]{14}.",
 "JHN.6.56": "[Wer]{1} [mis]{3} [Fleisch]{4,5} [isst]{2} und{6} [mis]{8} [Bluet]{9,10} [trinkt]{7}, [bliibt]{13} [i]{11} [mir]{12} [und ich]{14} [i]{15} [ihm]{16}.",
 "JHN.6.57": "[Wie]{1} [mich]{3} [de läbig]{4,5} [Vatter]{6} [gschickt hät]{2} [und ich]{7} [dur]{9} [de Vatter]{10,11} [läbe]{8}, [so]{12} [wird]{17} [au dä]{16}, [wo]{13} [mich]{15} [isst]{14}, [dur]{18} [mich]{19} [läbe]{17}.",
 "JHN.6.58": "[Das]{1} [isch]{2} [s Broot]{3,4}, [wo]{5} [vom]{6} [Himmel]{7} [abechoo isch]{8}; [nöd]{9} [wie]{10} [d Vätter]{12,13} [ggässe händ]{11} und{14} [gstorbe sind]{15}: [Wer]{16} [das]{18} [Broot]{19,20} [isst]{17}, [wird]{21} [für]{22} [immer]{23,24} [läbe]{21}.»",
 "JHN.6.59": "[Das]{1} [hät er gseit]{2}, [wo er]{5} [i]{3} [de Synagoge]{4} [z]{6} [Kafarnaum]{7} [glehrt hät]{5}.",
 "JHN.6.60": "[Vili]{1} [vo]{4} [sine]{5,7} [Jünger]{6}, [wo das ghört händ]{3}, [händ]{8} [also]{2} [gseit]{8}: «[Hert]{9} [isch]{10} [das]{13} [Wort]{11,12}; [wer]{14} [cha]{15} [sich das]{16} [aalose]{17}?»",
 "JHN.6.61": "[De Jesus]{3,4} [aber]{2} [hät]{1} [bi]{5} [sich sälber]{6} [gwüsst]{1}, [dass]{7} [sini]{11,13} [Jünger]{12} [drüber]{9,10} [muuled]{8}, [und hät]{14} [zu ine]{15} [gseit]{14}: «[Bringt]{18} [eu]{17} [das]{16} [z Fall]{18}?",
 "JHN.6.62": "[Wänn]{1} [ir]{3} [jetzt]{2} [de Mänschesohn]{4-7} [ufestiige]{8} [gsehnd]{3} dört hii, [wo]{9} [er]{10} [vorher]{11,12} [gsii isch]{10} …?",
 "JHN.6.63": "[De Geischt]{1,2} [isch]{3} s, [wo]{4} [läbig macht]{5}; [s Fleisch]{6,7} [nützt]{9} [nüüt]{8,10}. [D Wort]{11,12}, [wo]{13} [ich]{14} [zu eu]{16} [gredt ha]{15}, [sind]{18} [Geischt]{17} und{19} [sind]{21} [Läbe]{20}.",
 "JHN.6.64": "[Aber]{1} [es git]{2} [es paar]{5} [under]{3} [eu]{4}, [wo]{6} [nöd]{7} [glaubed]{8}.» [De Jesus]{13,14} [hät]{9} [nämli]{10} [vo]{11} [Aafang]{12} [aa]{11} [gwüsst]{9}, [wer]{15} [die]{17} [sind]{16}, wo [nöd]{18} [glaubed]{19}, und{20} [wer]{21} [dä]{23} [isch]{22}, wo [en]{25} [wird uslifere]{24}.",
 "JHN.6.65": "Und{1} [er hät gseit]{2}: «[Drum]{3,4} [han ich]{5} [eu]{6} [gseit]{5}: [Niemer]{8} [cha]{9} [zu]{11} [mir]{12} [choo]{10}, [wänn]{13} s [ihm]{17} [nöd]{14} [vom]{18,19} [Vatter]{20} [gää]{16} [isch]{15}.» ~7(" + SKIP_OTI_G + ")",
 "JHN.6.66": "[Vo dänn aa]{1,2} [sind]{8} [vili]{3} [vo sine]{4,5,7} [Jünger]{6} [zrugg]{9-11} [gange]{8} und{12} [sind]{16} [nüme]{13} [mit]{14} [ihm]{15} [umezoge]{16}.",
 "JHN.6.67": "[Da]{2} [hät]{1} [de Jesus]{3,4} [zu de Zwölf]{5,6} [gseit]{1}: «[Wänd]{10} [öppe]{7} [au]{8} [ir]{9} [gaa]{11}?»",
 "JHN.6.68": "[De Simon]{3} [Petrus]{4} [hät]{1} [ihm]{2} [gantwortet]{1}: «[Herr]{5}, [zu]{6} [wem]{7} [söled mer gaa]{8}? [Du häsch]{12} [Wort]{9} [vom ewige]{11} [Läbe]{10};",
 "JHN.6.69": "und{1} [mir]{2} [händ glaubt]{3} und{4} [erchännt]{5}, [dass]{6} [du]{7} [de Heilig]{9,10} [vo Gott]{11,12} [bisch]{8}.»",
 "JHN.6.70": "[De Jesus]{3,4} [hät]{1} [ine]{2} [gantwortet]{1}: «[Han]{10} [nöd]{5} [ich]{6} [eu]{7}, [di Zwölf]{8,9}, [usgwählt]{10}? Und{11} [eine]{14} [vo]{12} [eu]{13} [isch]{16} [en Tüüfel]{15}.»",
 "JHN.6.71": "[Er hät]{1} [aber]{2} [de Judas]{3,4} [gmeint]{1}, de Sohn [vom Simon]{5} [Iskariot]{6}; [dä]{7} [sött]{9} [en]{11} [nämli]{8} [uslifere]{10}, [eine]{12} [vo]{13} [de Zwölf]{14,15}.",
 # ------------------------------------------------------------ Kapitel 7
 "JHN.7.1": "Und{1} [nachher]{2,3} [isch]{4} [de Jesus]{5,6} [in]{7} [Galiläa]{8,9} [umezoge]{4}; [dänn]{11} [er hät]{12} [nöd]{10} [in]{13} [Judäa]{14,15} [umezieh]{16} [wele]{12}, [wil]{17} [d Jude]{20,21} [druf uus gsii sind]{18}, [en]{19} [umzbringe]{22}.",
 "JHN.7.2": "[Nöch]{3} [isch]{1} [aber]{2} [s Fäscht]{4,5} [vo de Jude]{6,7} [gsii]{1}, [s Laubhüttefäscht]{8,9}.",
 "JHN.7.3": "[Da]{2} [händ]{1} [sini]{5,7} [Brüedere]{6} [zu]{3} [ihm]{4} [gseit]{1}: «[Gang]{8} [vo da]{9} [wäg]{8} und{10} [gang]{11} [uf]{12} [Judäa]{13,14}, [demit]{15} [au]{16} [dini]{17,19} [Jünger]{18} [dini]{21} [Wärch]{22,23} [gsehnd]{20}, [wo]{24} [du machsch]{25}.",
 "JHN.7.4": "[Niemer]{1} [macht]{6} [nämli]{2} [öppis]{3} [im Verborgne]{4,5} und{7} [wott]{8} [glich sälber]{9} [i de Öffentlichkeit]{10,11} [staa]{12}. [Wänn]{13} [du]{15} [die Sache]{14} [machsch]{15}, [zeig]{16} [dich]{17} [de Wält]{18,19}!»",
 "JHN.7.5": "[Dänn]{2} [au]{1} [sini]{3,5} [Brüedere]{4} [händ]{6} [nöd]{1} [a]{7} [en]{8} [glaubt]{6}.",
 "JHN.7.6": "[Da]{2} [seit]{1} [de Jesus]{4,5} [zu ine]{3}: «[Mini]{8,9} [Ziit]{6,7} [isch]{11} [no nöd]{10} [da]{11}; [eui]{15,16} [Ziit]{12,14} [aber]{13} [isch]{18} [immer]{17} [parat]{19}.",
 "JHN.7.7": "[D Wält]{3,4} [chan]{2} [eu]{6} [nöd]{1} [hasse]{5}; [mich]{7} [aber]{8} [hasst si]{9}, [wil]{10} [ich]{11} [über]{13} [si]{14} [bezüüge]{12}, [dass]{15} [iri]{18} [Wärch]{16,17} [bös]{19} [sind]{20}.",
 "JHN.7.8": "[Gönd]{2} [ir]{1} [ufe]{2} [as]{3,4} [Fäscht]{5}! [Ich]{6} [gang]{8} [nöd]{7} [ufe]{8} [a]{9} [das]{12} [Fäscht]{10,11}, [wil]{13} [mini]{14,15} [Ziit]{16} [no nöd]{17} [erfüllt isch]{18}.»",
 "JHN.7.9": "[Nachdem er]{3} [aber]{2} [das]{1} [gseit hät]{3}, [isch]{5} [er]{4} [in]{6} [Galiläa]{7,8} [bliibe]{5}.",
 "JHN.7.10": "[Wo]{1} [aber]{2} [sini]{4,6} [Brüedere]{5} [as]{7,8} [Fäscht]{9} [ufegange sind]{3}, [dänn]{10} [isch]{13} [au]{11} [er]{12} [ufegange]{13}, [nöd]{14} [öffentlich]{15}, [sondern]{16} [wie]{17} [im Verborgne]{18,19}.",
 "JHN.7.11": "[D Jude]{1,3} [händ]{4} [en]{5} [also]{2} [am]{6,7} [Fäscht]{8} [gsuecht]{4} und{9} [händ gseit]{10}: «[Wo]{11} [isch]{12} [er]{13}?»",
 "JHN.7.12": "Und{1} [es hät]{5} [vil]{6} [Gmurmel]{2} [über]{3} [en]{4} [gää]{5} [i]{7} [de Mängi]{8,9}. [Di einte]{10,11} [händ gseit]{12}: «[Er isch]{15} [guet]{14}.» [Anderi]{16} [aber]{17} [händ gseit]{18}: «[Nei]{19}, [sondern]{20} [er verfüert]{21} [s Volk]{22,23}.» ~13(" + SKIP_OTI_G + ")",
 "JHN.7.13": "[Niemer]{1} [aber]{2} [hät]{4} [offe]{3} [über]{5} [en]{6} [gredt]{4}, [us]{7} [Angscht]{8,9} [vor de Jude]{10,11}.",
 "JHN.7.14": "[Wo]{5} [aber]{2} [s Fäscht]{3,4} [scho]{1} [halb verbii gsii isch]{5}, [isch]{6} [de Jesus]{7} [i]{8} [de Tämpel]{9,10} [ufegange]{6} und{11} [hät glehrt]{12}.",
 "JHN.7.15": "[Da]{2} [händ sich]{1} [d Jude]{3,4} [gwunderet]{1} [und gseit]{5}: «[Wie]{6} [kännt]{9} [dä]{7} [d Schrifte]{8}, wo er doch [nöd]{10} [glernt hät]{11}?»",
 "JHN.7.16": "[Da]{2} [hät]{1} [de Jesus]{4,5} [ine]{3} [gantwortet]{1} und{6} [gseit]{7}: «[Mini]{8,9} [Lehr]{10} [isch]{12} [nöd]{11} [mini]{13}, [sondern]{14} [die vo däm]{15}, wo [mich]{17} [gschickt hät]{16}.",
 "JHN.7.17": "[Wänn]{1} [öpper]{2} [sin]{6} [Wille]{4,5} [tue]{7} [wott]{3}, [wird er]{8} [a]{9} [de Lehr]{10,11} [merke]{8}, [öb]{12} si [vo]{13} [Gott]{14,15} [isch]{16} [oder]{17} öb [ich]{18} [vo]{19} [mir sälber]{20} [uus]{19} [rede]{21}.",
 "JHN.7.18": "[Wer]{1} [vo]{2} [sich sälber]{3} [uus]{2} [redt]{4}, [suecht]{9} [sini]{7} [eigeti]{8} [Ehr]{5,6}; [wer]{10} [aber]{11} [d Ehr]{13,14} [vo däm]{15} [suecht]{12}, wo [en]{17} [gschickt hät]{16}, [dä]{18} [isch]{20} [wahrhaftig]{19}, und{21} es [isch]{26} [kei]{25} [Unrächt]{22} [i]{23} [ihm]{24}.",
 "JHN.7.19": "[Hät]{3} [nöd]{1} [de Mose]{2} [eu]{4} [s Gsetz]{5,6} [gää]{3}? Und{7} [niemer]{8} [vo]{9} [eu]{10} [haltet]{11} [s Gsetz]{12,13}. [Werum]{14} [sueched ir]{16} [mich]{15} [umzbringe]{17}?»",
 "JHN.7.20": "[D Mängi]{2,3} [hät gantwortet]{1}: «[Du häsch]{5} [en Dämon]{4}! [Wer]{6} [suecht]{8} [dich]{7} [umzbringe]{9}?»",
 "JHN.7.21": "[De Jesus]{2} [hät gantwortet]{1} und{3} [zu ine]{5} [gseit]{4}: «[Es einzigs]{6} [Wärch]{7} [han ich gmacht]{8}, und{9} [ir alli]{10} [wundered eu]{11}.",
 "JHN.7.22": "[Drum]{1,2}: [De Mose]{3} [hät]{4} [eu]{5} [d Beschniidig]{6,7} [gää]{4} – [nöd]{8} [dass]{9} si [vom]{10,11} [Mose]{12} [chunnt]{13}, [sondern]{14} [vo]{15} [de Vätter]{16,17} –, und{18} [ir beschniided]{21} [en Mänsch]{22} [am]{19} [Sabbat]{20}.",
 "JHN.7.23": "[Wänn]{1} [en Mänsch]{4} [am]{5} [Sabbat]{6} [beschnitte wird]{2,3}, [demit]{7} [s Gsetz]{10,11} [vom Mose]{12} [nöd]{8} [broche wird]{9}, [sind ir]{14} [uf mich]{13} [wüetig]{14}, [wil]{15} [ich]{19} [en ganze]{16} [Mänsch]{17} [am]{20} [Sabbat]{21} [gsund]{18} [gmacht ha]{19}?",
 "JHN.7.24": "[Urteiled]{2} [nöd]{1} [nach]{3} [em Aaschii]{4}, [sondern]{5} [urteiled]{9} [mit eme grächte]{6,7} [Urteil]{8}!»",
 "JHN.7.25": "[Da]{2} [händ]{1} [es paar]{3} [vo]{4} [de Lüüt us Jerusalem]{5,6} [gseit]{1}: «[Isch]{9} [das]{8} [nöd]{7} dä, [wo]{10} [si]{11} [umbringe]{12} [wänd]{11}?",
 "JHN.7.26": "Und{1} [lueg]{2}, [er redt]{4} [offe]{3}, und{5} [si säged]{8} [ihm]{7} [nüüt]{6}. [Händ]{11} [öppe]{9} [d Obere]{12,13} [würkli]{10} [erchännt]{11}, [dass]{14} [dä]{15} [de Christus]{17,18} [isch]{16}?",
 "JHN.7.27": "[Aber]{1} [vo däm]{2} [wüssed mer]{3}, [wohär]{4} [er isch]{5}; [wänn]{9} [aber]{7} [de Christus]{6,8} [chunnt]{10}, [weiss]{12} [niemer]{11}, [wohär]{13} [er isch]{14}.»",
 "JHN.7.28": "[Da]{2} [hät]{1} [de Jesus]{7,8}, [wo er]{6} [im]{3,4} [Tämpel]{5} [glehrt hät]{6}, [luut grüeft]{1} [und gseit]{9,10}: «[Mich]{11} [känned ir]{12}, und{13} [ir wüssed]{14}, [wohär]{15} [ich bi]{16}! Und{17} [vo]{18} [mir sälber]{19} [uus]{18} [bin ich]{21} [nöd]{20} [choo]{21}, [sondern]{22} [dä]{25}, wo [mich]{27} [gschickt hät]{26}, [isch]{23} [wahrhaftig]{24}; [dä]{28} [känned]{31} [ir]{29} [nöd]{30}.",
 "JHN.7.29": "[Ich]{1} [känne]{2} [en]{3}, [dänn]{4} [ich bi]{7} [vo]{5} [ihm]{6}, [und er]{8} [hät]{10} [mich]{9} [gschickt]{10}.»",
 "JHN.7.30": "[Da]{2} [händ si probiert]{1}, [en]{3} [z verhafte]{4}, und{5} [niemer]{6} [hät]{7} [d Hand]{10,11} [a]{8} [en]{9} [gleit]{7}, [wil]{12} [sini]{15,17} [Stund]{16} [no nöd]{13} [choo isch]{14}.",
 "JHN.7.31": "[Vili]{5} [us]{1} [de Mängi]{2,3} [aber]{4} [händ]{6} [a]{7} [en]{8} [glaubt]{6} und{9} [händ gseit]{10}: «[Wird]{18} [de Christus]{11,12}, [wänn]{13} [er chunnt]{14}, [öppe]{15} [meh]{16} [Zeiche]{17} [mache]{18}, [als]{19} [dä]{20} [gmacht hät]{21}?»",
 "JHN.7.32": "[D Pharisäer]{2,3} [händ]{1} [d Mängi]{4,5} [das]{9} [über]{7} [en]{8} [murmle]{6} [ghört]{1}, und{10} [d Hoheprieschter]{12,13} und{14} [d Pharisäer]{15,16} [händ]{11} [Diener]{17} [gschickt]{11}, [zum]{18} [en]{20} [verhafte]{19}.",
 "JHN.7.33": "[Da]{2} [hät]{1} [de Jesus]{3,4} [gseit]{1}: «[No]{5} [es chliises]{7} [Wiili]{6} [bin ich]{10} [bi]{8} [eu]{9}, und{11} dänn [gang ich]{12} [zu]{13} [däm]{14}, wo [mich]{16} [gschickt hät]{15}.",
 "JHN.7.34": "[Ir wärded]{1} [mich]{2} [sueche]{1} und{3} [nöd]{4} [finde]{5}, und{6} [wo]{7} [ich]{9} [bi]{8}, dört [chönd]{12} [ir]{10} [nöd]{11} [häre choo]{13}.»",
 "JHN.7.35": "[Da]{2} [händ]{1} [d Jude]{3,4} [zunenand]{5,6} [gseit]{1}: «[Wo]{7} [wott]{9} [dä]{8} [hiigaa]{10}, [dass]{11} [mir]{12} [en]{15} [nöd]{13} [finde wärded]{14}? [Wott er]{22} [öppe]{16} [i]{17} [d Diaspora]{18,19} [under de Grieche]{20,21} [gaa]{23} und{24} [d Grieche]{26,27} [lehre]{25}?",
 "JHN.7.36": "[Was]{1} [isch]{2} [das]{5} [für es Wort]{3,4}, [wo]{6} [er gseit hät]{7}: ‹[Ir wärded]{8} [mich]{9} [sueche]{8} und{10} [nöd]{11} [finde]{12}, und{13} [wo]{14} [ich]{16} [bi]{15}, dört [chönd]{19} [ir]{17} [nöd]{18} [häre choo]{20}›?»",
 "JHN.7.37": "[Am]{1,3} [letschte]{4} [Tag]{5} [aber]{2}, [am grosse]{6,7} [vom Fäscht]{8,9}, [isch]{10} [de Jesus]{11,12} [dagstande]{10} und{13} [hät luut grüeft]{14} [und gseit]{15}: «[Wänn]{16} [öpper]{17} [Durscht hät]{18}, [söll er]{19} [zu]{20} [mir]{21} [choo]{19} und{22} [trinke]{23}!",
 "JHN.7.38": "[Wer]{1} [a]{3} [mich]{4} [glaubt]{2} – [wie]{5} [d Schrift]{7,8} [gseit hät]{6}: ‹[Ström]{9} [vo läbigem]{16} [Wasser]{15} [wärded]{14} [us]{10} [sim]{11,13} [Innere]{12} [flüüsse]{14}.›»",
 "JHN.7.39": "[Das]{1} [hät er]{3} [aber]{2} [über]{4} [de Geischt]{5,6} [gseit]{3}, [wo]{7} [die]{10} [übercho würded]{8,9}, wo [a]{12} [en]{13} [glaubt händ]{11}; [dänn]{15} [de Geischt]{17} [isch]{16} [no nöd]{14} [da gsii]{16}, [wil]{18} [de Jesus]{19} [no nöd]{20} [verherrlicht worde isch]{21}.",
 "JHN.7.40": "Es paar [us]{1} [de Mängi]{2,3} [also]{4}, wo [die]{8} [Wort]{6,7} [ghört händ]{5}, [händ gseit]{9}: «[Das]{10} [isch]{11} [würkli]{12} [de Prophet]{13,14}.»",
 "JHN.7.41": "[Anderi]{1} [händ gseit]{2}: «[Das]{3} [isch]{4} [de Christus]{5,6}.» [Wider anderi]{7} [aber]{8} [händ gseit]{9}: «[Chunnt]{17} [dänn]{11} [de Christus]{15,16} [öppe]{10} [us]{12} [Galiläa]{13,14}?",
 "JHN.7.42": "[Hät]{4} [nöd]{1} [d Schrift]{2,3} [gseit]{4}, [dass]{5} [de Christus]{19,20} [us]{6} [de Nachkomme]{7,8} [vom David]{9} und{10} [us]{11} [Betlehem]{12}, [em Dorf]{13,14}, [wo]{15} [de David]{17} [gsii isch]{16}, [chunnt]{18}?»",
 "JHN.7.43": "[So]{2} [isch]{3} [wäge ihm]{7,8} [e Spaltig]{1} [i]{4} [de Mängi]{5,6} [entstande]{3}.",
 "JHN.7.44": "[Es paar]{1} [vo]{4} [ine]{5} [aber]{2} [händ]{3} [en]{7} [verhafte]{6} [wele]{3}, [doch]{8} [niemer]{9} [hät]{10} [d Händ]{13,14} [a]{11} [en]{12} [gleit]{10}.",
 "JHN.7.45": "[D Diener]{3,4} [sind]{1} [also]{2} [zu]{5} [de Hoheprieschter]{6,7} und{8} [Pharisäer]{9} [zruggchoo]{1}, und{10} [die]{13} [händ]{11} [zu ine]{12} [gseit]{11}: «[Werum]{14,15} [händ ir]{17} [en]{18} [nöd]{16} [brocht]{17}?»",
 "JHN.7.46": "[D Diener]{2,3} [händ gantwortet]{1}: «[No nie]{4} [hät]{5} [en Mänsch]{7} [eso]{6} [gredt]{5}.»",
 "JHN.7.47": "[Da]{2} [händ]{1} [ine]{3} [d Pharisäer]{4,5} [gantwortet]{1}: «[Händ]{9} [öppe]{6} [au]{7} [ir]{8} [eu verfüere laa]{9}?",
 "JHN.7.48": "[Hät]{6} [öppe]{1} [eine]{2} [vo]{3} [de Obere]{4,5} [a]{7} [en]{8} [glaubt]{6} [oder]{9} [vo]{10} [de Pharisäer]{11,12}?",
 "JHN.7.49": "[Aber]{1} [das]{4} [Volk]{2,3} [da]{4}, [wo]{5} [s Gsetz]{8,9} [nöd]{6} [kännt]{7} – [verfluecht]{10} [sind si]{11}!»",
 "JHN.7.50": "[De Nikodemus]{2}, [wo]{5} [früener]{9} [zu]{7} [ihm]{8} [choo isch]{6} und [eine]{10} [vo]{12} [ine]{13} [gsii isch]{11}, [seit]{1} [zu]{3} [ine]{4}:",
 "JHN.7.51": "«[Richtet]{5} [öppe]{1} [üses]{4} [Gsetz]{2,3} [en Mänsch]{6,7}, [ohni]{8,9} [en]{12,13} [zerscht]{11} [aaghört]{10} [und]{14} [erchännt z ha]{15}, [was]{16} [er macht]{17}?»",
 "JHN.7.52": "[Si händ gantwortet]{1} und{2} [zu ihm]{4} [gseit]{3}: «[Bisch]{11} [du]{7} [öppe]{5} [au]{6} [us]{8} [Galiläa]{9,10}? [Forsch nache]{12} und{13} [lueg]{14}, [dass]{15} [us]{16} [Galiläa]{17,18} [kei]{20} [Prophet]{19} [ufstaat]{21}.»",
 "JHN.7.53": "⟦[Und]{1} [jede]{3} [isch]{2} [i]{4} [sis]{5,7} [Huus]{6} [gange]{2}.",
}

# (Stelle, Zieltext, Art, Griechisch, wörtlicher, andere Möglichkeiten, Hinweis)
PA_DE = ("Hier beginnt der Abschnitt von der Ehebrecherin ([[JHN.7.53]]–[[JHN.8.11]]). Der SBLGNT setzt ihn in "
         "Doppelklammern ⟦ ⟧; die Übersetzung übernimmt die Klammern (die schliessende steht in [[JHN.8.11]]). In der "
         "Textforschung wird der Abschnitt weithin als spätere Einfügung in das Johannesevangelium beurteilt; das ist ein "
         "verbreitetes Urteil, keine Tatsachenfeststellung. Befund der im Projekt erfassten CNTR-Transkriptionen: In 01, 03, "
         "029, 032, 𝔓66 und 𝔓75 steht für [[JHN.7.53]]–[[JHN.8.11]] kein Text, auf [[JHN.7.52]] folgt dort [[JHN.8.12]]. "
         "05 enthält den Abschnitt, in [[JHN.7.53]] mit ἐπορεύθησαν («sie gingen») statt ἐπορεύθη. 02 und 04 sind an "
         "dieser Stelle nicht erhalten (in den Transkriptionen fehlen bei 02 [[JHN.6.51]]–[[JHN.8.51]], bei 04 "
         "[[JHN.7.4]]–[[JHN.8.33]]); über ihren Wortlaut lässt sich deshalb nichts sagen. Nach Angaben der Forschungsliteratur "
         "steht der Abschnitt in einigen späteren Handschriften an anderer Stelle (etwa nach [[JHN.7.36]], nach [[JHN.21.25]] "
         "oder nach [[LUK.21.38]]); das ist im Projekt nicht anhand von Daten geprüft. Viele Kirchen lesen den Abschnitt als "
         "Teil der Heiligen Schrift; die Frage seiner Herkunft ist davon zu unterscheiden. [[JHN.7.53]] schliesst erzählerisch "
         "eher an eine Versammlung an als an die Sitzung in [[JHN.7.45]]–[[JHN.7.52]]; auch dieser Übergang wird verschieden erklärt.")
PA_GSW = ("Da faat de Abschnitt vo de Ehebrächerin aa ([[JHN.7.53]]–[[JHN.8.11]]). De SBLGNT setzt en i Doppelklammere ⟦ ⟧; "
          "d Übersetzig übernimmt d Klammere (di schliessend staat i [[JHN.8.11]]). I de Textforschig wird de Abschnitt "
          "wiitume als spööteri Iifüegig i s Johannesevangelium beurteilt; das isch es verbreitets Urteil, kei Tatsach. "
          "I de erfasste CNTR-Transkriptione vo 01, 03, 029, 032, 𝔓66 und 𝔓75 staat für [[JHN.7.53]]–[[JHN.8.11]] kei Text; "
          "uf [[JHN.7.52]] folgt dört [[JHN.8.12]]. 05 hät de Abschnitt. 02 und 04 sind a dere Stell nöd erhalte. Nach de "
          "Forschig staat de Abschnitt i es paar spöötere Handschrifte amene andere Ort (öppe nach [[JHN.21.25]] oder nach "
          "[[LUK.21.38]]); das isch im Projekt nöd mit Date prüeft. Vili Chile läsed en als Teil vo de Heilige Schrift; "
          "d Frag nach sinere Herkunft isch devo z underscheide.")

DEC_DE = [
 ("JHN.6.1", "des Sees", "adapted", "τῆς θαλάσσης", "des Meeres", None, "Johannes nennt den See Gennesaret wie Markus und Matthäus θάλασσα («Meer»). Den Namen «See von Tiberias» trägt er nach der unter Herodes Antipas gegründeten Stadt am Westufer; Johannes nennt beide Namen."),
 ("JHN.6.2", "die Zeichen", "literal", "τὰ σημεῖα", None, ["die Wunder", "die Wunderzeichen"], "σημεῖον ist durchgehend mit «Zeichen» wiedergegeben, nicht mit «Wunder»: Johannes nennt Jesu Taten Zeichen, die über sich hinausweisen ([[JHN.2.11]], [[JHN.20.30]]). Grundentscheid nach scripts/authoring/johannes_text_01_03.py."),
 ("JHN.6.4", "der Juden", "interpretive", "τῶν Ἰουδαίων", None, ["der Judäer"], "Siehe [[JHN.6.41]] und die translation_notes zur Wiedergabe von οἱ Ἰουδαῖοι."),
 ("JHN.6.7", "Denare", "literal", "δηναρίων", None, None, "Ein Denar war der übliche Tageslohn eines Arbeiters (vgl. [[MAT.20.2]]); zweihundert Denare entsprechen also etwa zweihundert Tagelöhnen."),
 ("JHN.6.9", "Gerstenbrote", "literal", "ἄρτους κριθίνους", None, None, "Gerstenbrot war billiger als Weizenbrot. Die Erzählung erinnert an Elischa, der mit zwanzig Gerstenbroten hundert Menschen sättigt ([[2KI.4.42]]–[[2KI.4.44]])."),
 ("JHN.6.10", "die Männer", "literal", "οἱ ἄνδρες", None, ["die Leute"], "Vorher steht ἀνθρώπους («Menschen»), bei der Zählung ἄνδρες («Männer»). Ob nur Männer gezählt wurden oder das Wort allgemein steht, lässt der Text offen."),
 ("JHN.6.11", "nachdem er gedankt hatte", "literal", "εὐχαριστήσας", None, ["sprach das Dankgebet"], "εὐχαριστέω entspricht dem jüdischen Tischgebet. Dasselbe Wort steht in [[JHN.6.23]]. Ob Johannes damit auf das Abendmahl anspielt, ist umstritten."),
 ("JHN.6.14", "der Prophet", "interpretive", "ὁ προφήτης", None, ["ein Prophet"], "Mit Artikel: der erwartete Prophet, wohl im Anschluss an [[DEU.18.15]] (ein Prophet wie Mose). Ebenso [[JHN.7.40]]."),
 ("JHN.6.14", "die Welt", "literal", "τὸν κόσμον", None, None, "κόσμος ist durchgehend mit «Welt» wiedergegeben (Grundentscheid)."),
 ("JHN.6.15", "mit Gewalt ergreifen", "literal", "ἁρπάζειν", None, ["an sich reissen", "entführen"], None),
 ("JHN.6.19", "Stadien", "literal", "σταδίους", None, ["Kilometer"], "Ein Stadion misst rund 185 Meter; 25 bis 30 Stadien sind etwa 4,5 bis 5,5 Kilometer."),
 ("JHN.6.20", "Ich bin es", "interpretive", "Ἐγώ εἰμι", None, ["Ich bin", "Ich bin’s"], "ἐγώ εἰμι ist durchgehend «Ich bin …» (Grundentscheid). Hier steht es ohne Ergänzung als Erkennungswort; als Antwort bzw. Identifikation gilt verbindlich «Ich bin es» (wie [[JHN.4.26]], [[JHN.9.9]], [[JHN.18.5]]–[[JHN.18.8]]), absolut gebraucht dagegen «ich bin» ([[JHN.8.24]], [[JHN.8.28]], [[JHN.8.58]], [[JHN.13.19]]). Dieselben Worte stehen in der griechischen Bibel für Gottes Selbstvorstellung (vgl. [[EXO.3.14]], [[ISA.43.10]]); ob Johannes diesen Anklang hier beabsichtigt (vgl. [[JHN.8.58]]), ist umstritten."),
 ("JHN.6.23", "jedoch", "interpretive", "ἀλλὰ", None, ["andere (Boote)"], "Die alten Handschriften schreiben ohne Akzente: ΑΛΛΑ kann ἀλλά («aber, jedoch») oder ἄλλα («andere») sein. Der SBLGNT akzentuiert ἀλλά; siehe Alternative."),
 ("JHN.6.23", "der Herr", "literal", "τοῦ κυρίου", None, None, "In den Erzählteilen nennt Johannes Jesus selten «den Herrn» (vgl. [[JHN.11.2]], [[JHN.20.20]]). In 05 fehlt die Wendung nach der Transkription."),
 ("JHN.6.26", "Amen, amen", "literal", "Ἀμὴν ἀμὴν", None, ["Wahrlich, wahrlich", "Ich versichere euch"], "Johannes verdoppelt das Amen, mit dem Jesus feierliche Worte einleitet (bei den anderen Evangelien einfach). Durchgehend «Amen, amen, ich sage euch» (Grundentscheid)."),
 ("JHN.6.27", "Arbeitet", "literal", "ἐργάζεσθε", None, ["Müht euch", "Wirkt"], "ἐργάζομαι «arbeiten, wirken» und ἔργον «Werk» verbinden [[JHN.6.27]]–[[JHN.6.30]]; die Übersetzung hält die Wortfamilie mit «arbeiten», «wirken» und «Werk» sichtbar."),
 ("JHN.6.27", "bleibt", "literal", "μένουσαν", None, ["vorhält"], "μένω ist durchgehend mit «bleiben» wiedergegeben (Grundentscheid; vgl. [[JHN.6.56]])."),
 ("JHN.6.27", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", None, "Selbstbezeichnung Jesu (vgl. [[DAN.7.13]]). Ebenso [[JHN.6.53]], [[JHN.6.62]]."),
 ("JHN.6.27", "beglaubigt", "adapted", "ἐσφράγισεν", "versiegelt", ["mit seinem Siegel bestätigt"], "Ein Siegel bestätigt Echtheit und Zugehörigkeit (vgl. [[JHN.3.33]])."),
 ("JHN.6.27", "ewigen", "literal", "αἰώνιον", None, None, "ζωὴ αἰώνιος ist durchgehend «ewiges Leben». Johannes spricht davon auch als gegenwärtigem Besitz ([[JHN.6.47]], [[JHN.6.54]])."),
 ("JHN.6.31", "Brot vom Himmel gab er ihnen zu essen", "literal", "Ἄρτον ἐκ τοῦ οὐρανοῦ ἔδωκεν αὐτοῖς φαγεῖν", None, None, "Schriftzitat; am nächsten steht [[PSA.78.24]] (vgl. [[EXO.16.4]], [[EXO.16.15]], [[NEH.9.15]]). Welche Stelle genau gemeint ist, ist umstritten."),
 ("JHN.6.33", "das, was", "interpretive", "ὁ καταβαίνων", None, ["der, der"], "ὁ καταβαίνων kann sich auf das Brot beziehen («das, was herabkommt») oder schon auf eine Person («der, der herabkommt»). Die Gesprächspartner verstehen es noch als Brot ([[JHN.6.34]]); [[JHN.6.35]] löst es auf Jesus hin auf."),
 ("JHN.6.34", "Herr", "interpretive", "Κύριε", None, ["mein Herr"], "κύριε ist auch eine höfliche Anrede. Was die Sprechenden damit meinen, lässt der Text offen. Ebenso [[JHN.6.68]]."),
 ("JHN.6.35", "Ich bin das Brot des Lebens", "literal", "Ἐγώ εἰμι ὁ ἄρτος τῆς ζωῆς", None, None, "Das erste der «Ich bin»-Worte mit Bildwort (weiter z. B. [[JHN.8.12]], [[JHN.10.11]], [[JHN.11.25]], [[JHN.14.6]], [[JHN.15.1]]). ἐγώ εἰμι ist durchgehend «Ich bin …» (Grundentscheid). «Brot des Lebens» kann heissen: Brot, das Leben gibt (vgl. [[JHN.6.33]]) und das selbst lebendig ist ([[JHN.6.51]])."),
 ("JHN.6.35", "wird gewiss nicht", "literal", "οὐ μὴ", None, None, "Doppelte Verneinung, verstärkend."),
 ("JHN.6.37", "hinausstossen", "literal", "ἐκβάλω ἔξω", "hinauswerfen nach draussen", ["abweisen"], None),
 ("JHN.6.41", "die Juden", "interpretive", "οἱ Ἰουδαῖοι", None, ["die Judäer", "die jüdischen Führer", "die Leute"], "Grundentscheid: οἱ Ἰουδαῖοι wörtlich «die Juden». Johannes gebraucht das Wort für das Volk, für die Bewohner Judäas und oft für die führenden Kreise in Jerusalem, die Jesus ablehnen; auch Jesus, seine Jünger und die Menge sind Juden. Hier sind es die Hörer in Galiläa ([[JHN.6.59]]). Eine kontextbezogene Wiedergabe würde eine Deutung festlegen, die wörtliche kann als Urteil über alle Juden missverstanden werden; siehe translation_notes."),
 ("JHN.6.41", "murrten", "literal", "Ἐγόγγυζον", None, ["murmelten"], "γογγύζω erinnert an das Murren Israels in der Wüste ([[EXO.16.2]], [[EXO.16.8]]), wo es ebenfalls um das Brot vom Himmel geht."),
 ("JHN.6.42", "Josefs", "literal", "Ἰωσήφ", None, None, "Die Sprechenden kennen Jesu Herkunft; Johannes setzt dem die Herkunft «vom Himmel» entgegen (vgl. [[JHN.7.27]]–[[JHN.7.28]])."),
 ("JHN.6.44", "zieht", "literal", "ἑλκύσῃ", None, ["heranzieht"], "Dasselbe Verb in [[JHN.12.32]] («ich werde alle zu mir ziehen»)."),
 ("JHN.6.45", "Und sie werden alle von Gott Belehrte sein", "literal", "Καὶ ἔσονται πάντες διδακτοὶ θεοῦ", None, ["Und sie werden alle von Gott gelehrt sein"], "Zitat aus [[ISA.54.13]] (vgl. [[JER.31.33]]–[[JER.31.34]])."),
 ("JHN.6.51", "Fleisch", "literal", "σάρξ", None, ["Leib"], "Vgl. [[JHN.1.14]] («das Wort wurde Fleisch»). Ob [[JHN.6.51]]–[[JHN.6.58]] auf das Abendmahl anspielen, wird verschieden beurteilt; die Übersetzung entscheidet das nicht."),
 ("JHN.6.51", "Ewigkeit", "literal", "τὸν αἰῶνα", None, ["für immer"], None),
 ("JHN.6.54", "isst", "interpretive", "τρώγων", "kaut", ["verzehrt"], "Ab hier steht τρώγω statt ἐσθίω/φαγεῖν. Ob das Wort verstärkt («kauen») oder in der Koine einfach «essen» bedeutet, ist umstritten. Ebenso [[JHN.6.56]]–[[JHN.6.58]]."),
 ("JHN.6.55", "wahre", "literal", "ἀληθής", None, ["wirklich"], "Siehe Alternative: einige Zeugen lesen das Adverb ἀληθῶς («wirklich»)."),
 ("JHN.6.56", "bleibt", "literal", "μένει", None, None, "μένω «bleiben» (Grundentscheid), hier für die gegenseitige Gemeinschaft (vgl. [[JHN.15.4]])."),
 ("JHN.6.57", "durch den Vater", "interpretive", "διὰ τὸν πατέρα", None, ["um des Vaters willen", "dank dem Vater"], "διά mit Akkusativ heisst meist «wegen»; hier wohl: der Vater ist Grund und Quelle des Lebens. Ebenso «durch mich»."),
 ("JHN.6.59", "in der Synagoge", "adapted", "ἐν συναγωγῇ", "in Synagoge", ["in einer Synagogenversammlung"], "Ohne Artikel; συναγωγή kann das Gebäude oder die Versammlung meinen."),
 ("JHN.6.60", "Wort", "literal", "λόγος", None, ["Rede"], "λόγος ist, wo möglich, mit «Wort» wiedergegeben (Grundentscheid; vgl. [[JHN.1.1]])."),
 ("JHN.6.60", "es", "interpretive", "αὐτοῦ", None, ["ihn"], "αὐτοῦ kann sich auf das Wort oder auf Jesus beziehen."),
 ("JHN.6.61", "zu Fall", "interpretive", "σκανδαλίζει", None, ["Nehmt ihr daran Anstoss"], "σκανδαλίζω: über ein Hindernis stolpern lassen, im Glauben zu Fall bringen."),
 ("JHN.6.62", "wo er vorher war", "adapted", "ὅπου ἦν τὸ πρότερον", None, None, "Der Satz bricht nach dem Wenn-Satz ab; der Nachsatz fehlt im Griechischen (etwa: «was dann?»). Ob der Aufstieg das Ärgernis noch vergrössert oder auflöst, wird verschieden gedeutet."),
 ("JHN.6.63", "Geist", "interpretive", "πνεῦμά", None, ["Gottes Geist"], "πνεῦμα heisst Geist, Wind, Atem. Ob hier Gottes Geist gemeint ist oder die geistliche Art der Worte, ist umstritten."),
 ("JHN.6.64", "ausliefern würde", "literal", "παραδώσων", None, ["verraten würde"], "παραδίδωμι ist wie bei Markus durchgehend «ausliefern»."),
 ("JHN.6.66", "Daraufhin", "interpretive", "Ἐκ τούτου", None, ["Aus diesem Grund", "Von da an"], "Ἐκ τούτου kann zeitlich oder begründend verstanden werden."),
 ("JHN.6.69", "der Heilige Gottes", "literal", "ὁ ἅγιος τοῦ θεοῦ", None, None, "Dieselbe Bezeichnung in [[MRK.1.24]]. Spätere Handschriften gleichen an [[MAT.16.16]] an; siehe Alternative."),
 ("JHN.6.70", "ein Teufel", "interpretive", "διάβολός", None, ["ein Verleumder", "ein Widersacher"], "διάβολος heisst «Verleumder» und bezeichnet sonst den Teufel (vgl. [[JHN.13.2]]). Ohne Artikel: «ein Teufel», wohl im Sinn von «einer, der auf der Seite des Teufels steht»."),
 ("JHN.6.71", "den Sohn des Simon Iskariot", "adapted", "Σίμωνος Ἰσκαριώτου", "des Simon Iskariot", ["Judas Iskariot, den Sohn Simons"], "Im SBLGNT steht Ἰσκαριώτου im Genitiv und bezieht sich damit auf den Vater Simon (so auch [[JHN.13.26]]); «Sohn» ist ergänzt. RP liest Ἰσκαριώτην und bezieht den Beinamen auf Judas."),
 ("JHN.7.1", "die Juden", "interpretive", "οἱ Ἰουδαῖοι", None, ["die Judäer", "die jüdischen Führer"], "Grundentscheid wie in [[JHN.6.41]]. Hier steht Ἰουδαῖοι unmittelbar neben Ἰουδαία («Judäa»); gemeint sind wohl die führenden Kreise in Judäa und Jerusalem (vgl. [[JHN.5.18]])."),
 ("JHN.7.2", "das Laubhüttenfest", "literal", "ἡ σκηνοπηγία", None, ["Sukkot"], "Das siebentägige Herbstfest ([[LEV.23.34]]–[[LEV.23.43]]), eines der drei Wallfahrtsfeste nach Jerusalem."),
 ("JHN.7.3", "Brüder", "literal", "ἀδελφοὶ", None, ["Geschwister", "Verwandte"], "Wie das Verhältnis zu verstehen ist (leibliche Brüder, Halbbrüder, Vettern), beantworten die kirchlichen Traditionen unterschiedlich; der Text sagt dazu nichts."),
 ("JHN.7.4", "offenbare", "literal", "φανέρωσον", None, ["zeige"], None),
 ("JHN.7.6", "Zeit", "interpretive", "καιρὸς", None, ["rechte Zeit", "Stunde"], "καιρός ist der passende, entscheidende Zeitpunkt; daneben steht bei Johannes ὥρα «Stunde» ([[JHN.7.30]])."),
 ("JHN.7.7", "Die Welt", "literal", "ὁ κόσμος", None, None, "Hier die Menschenwelt, die sich Gott verschliesst (vgl. [[JHN.15.18]])."),
 ("JHN.7.8", "Ich gehe nicht hinauf", "literal", "ἐγὼ οὐκ ἀναβαίνω", None, ["Ich gehe noch nicht hinauf"], "Jesus geht kurz darauf doch ([[JHN.7.10]]). Ausleger erklären das verschieden: nicht jetzt, nicht so wie die Brüder es wollen, oder mit einem Doppelsinn von ἀναβαίνω («hinaufgehen» auch zum Vater, vgl. [[JHN.20.17]]). Viele Handschriften lesen οὔπω «noch nicht»; siehe Alternative."),
 ("JHN.7.10", "gleichsam im Verborgenen", "literal", "ὡς ἐν κρυπτῷ", None, ["sozusagen heimlich"], None),
 ("JHN.7.12", "Gemurmel", "interpretive", "γογγυσμὸς", None, ["Murren", "Getuschel"], "Dieselbe Wortfamilie wie «murren» ([[JHN.6.41]]); hier ist es kein Klagen, sondern halblautes Reden in der Menge. Ebenso «murmeln» in [[JHN.7.32]]."),
 ("JHN.7.12", "das Volk", "literal", "τὸν ὄχλον", None, ["die Menge"], None),
 ("JHN.7.13", "vor den Juden", "interpretive", "τῶν Ἰουδαίων", None, ["vor den jüdischen Führern"], "Die Sprechenden sind selbst Juden; gemeint sind wohl die führenden Kreise (vgl. [[JHN.9.22]]). Grundentscheid: wörtlich."),
 ("JHN.7.14", "den Tempel", "literal", "τὸ ἱερὸν", None, ["den Tempelbezirk"], None),
 ("JHN.7.15", "die Schriften", "interpretive", "γράμματα", "Buchstaben", ["Gelehrsamkeit", "die Schrift"], "γράμματα heisst Buchstaben, Schriftkunde, Bildung. Gemeint ist wohl Kenntnis der Schriften, ohne bei einem Lehrer gelernt zu haben."),
 ("JHN.7.18", "Ehre", "interpretive", "δόξαν", None, ["Herrlichkeit", "Ansehen"], "δόξα ist Grundentscheid «Herrlichkeit» (vgl. [[JHN.1.14]]); hier geht es um Ansehen, das jemand sucht (wie [[JHN.5.41]], [[JHN.5.44]]), deshalb «Ehre». Der Zusammenhang mit der Herrlichkeit Gottes geht im Deutschen verloren."),
 ("JHN.7.19", "tut", "literal", "ποιεῖ", None, ["hält"], None),
 ("JHN.7.20", "einen Dämon", "literal", "Δαιμόνιον", None, ["Du bist besessen"], "Vorwurf der Besessenheit oder des Wahns (vgl. [[JHN.8.48]], [[JHN.10.20]])."),
 ("JHN.7.21", "Ein einziges Werk", "literal", "Ἓν ἔργον", None, None, "Gemeint ist wohl die Heilung am Sabbat in [[JHN.5.1]]–[[JHN.5.9]]."),
 ("JHN.7.22", "Darum", "interpretive", "διὰ τοῦτο", None, ["wundert euch darüber"], "Der SBLGNT zieht διὰ τοῦτο zu [[JHN.7.22]]. Man kann es auch an [[JHN.7.21]] anschliessen: «ihr alle wundert euch darüber»."),
 ("JHN.7.24", "nach dem Augenschein", "literal", "κατʼ ὄψιν", None, ["nach dem Äusseren"], None),
 ("JHN.7.26", "die Oberen", "interpretive", "οἱ ἄρχοντες", None, ["die Ratsherren", "die führenden Männer"], "Wohl die Mitglieder des Hohen Rates (vgl. [[JHN.3.1]])."),
 ("JHN.7.26", "der Christus", "traditional", "ὁ χριστός", None, ["der Messias", "der Gesalbte"], "χριστός übersetzt hebräisch māšîaḥ «Gesalbter»."),
 ("JHN.7.27", "woher er ist", "literal", "πόθεν ἐστίν", None, None, "Die Vorstellung, die Herkunft des Messias sei verborgen, ist auch in anderen jüdischen Schriften belegt; [[JHN.7.42]] hält ihr die Herkunft aus Betlehem entgegen."),
 ("JHN.7.28", "rief", "literal", "ἔκραξεν", None, ["schrie"], "κράζω: laut rufen, ausrufen (ebenso [[JHN.7.37]])."),
 ("JHN.7.30", "Stunde", "literal", "ὥρα", None, None, "Bei Johannes die Stunde seines Todes und seiner Verherrlichung (vgl. [[JHN.2.4]], [[JHN.12.23]], [[JHN.13.1]])."),
 ("JHN.7.32", "Diener", "interpretive", "ὑπηρέτας", None, ["Tempelwächter", "Gerichtsdiener"], "Wohl die Tempelpolizei, die dem Hohen Rat unterstand."),
 ("JHN.7.32", "murmeln", "interpretive", "γογγύζοντος", None, ["murren"], "Siehe [[JHN.7.12]]."),
 ("JHN.7.35", "die Diaspora unter den Griechen", "interpretive", "τὴν διασπορὰν τῶν Ἑλλήνων", None, ["die unter den Griechen Zerstreuten"], "Diaspora («Zerstreuung») bezeichnet die Juden ausserhalb des Landes Israel. «Die Griechen» kann griechisch sprechende Nichtjuden meinen; ob die Sprechenden an Juden oder an Nichtjuden denken, ist offen."),
 ("JHN.7.37", "rief laut", "literal", "ἔκραξεν", None, None, None),
 ("JHN.7.38", "Wer an mich glaubt", "interpretive", "ὁ πιστεύων εἰς ἐμέ", None, ["und es trinke, wer an mich glaubt"], "Die Übersetzung folgt der Zeichensetzung des SBLGNT: Der Satz beginnt neu, und «sein Inneres» ist das des Glaubenden. Andere ziehen «wer an mich glaubt» zu [[JHN.7.37]] («… komme zu mir, und es trinke, wer an mich glaubt») und beziehen die Ströme auf Jesus selbst (vgl. [[JHN.19.34]]). Beide Lesungen werden vertreten."),
 ("JHN.7.38", "wie die Schrift gesagt hat", "literal", "καθὼς εἶπεν ἡ γραφή", None, None, "Ein genau passendes Schriftwort gibt es nicht; vorgeschlagen werden u. a. [[ISA.58.11]], [[EZK.47.1]], [[ZEC.14.8]] und die Wasser aus dem Felsen ([[EXO.17.6]])."),
 ("JHN.7.38", "Inneren", "interpretive", "κοιλίας", "Leib", ["Bauch", "Herzen"], "κοιλία ist der Bauch, der Leib, dann das Innerste des Menschen."),
 ("JHN.7.38", "lebendigen Wassers", "literal", "ὕδατος ζῶντος", None, ["fliessenden Wassers"], "«Lebendiges Wasser» heisst zugleich fliessendes Quellwasser und Wasser, das Leben gibt (vgl. [[JHN.4.10]])."),
 ("JHN.7.39", "der Geist war noch nicht da", "adapted", "οὔπω γὰρ ἦν πνεῦμα", "noch nicht war Geist", ["der Geist war noch nicht gegeben"], "Wörtlich «noch nicht war Geist». Gemeint ist kaum, dass es den Geist nicht gab, sondern dass er noch nicht gegeben war (vgl. [[JHN.20.22]]). Einige Handschriften machen das ausdrücklich; siehe Alternative."),
 ("JHN.7.39", "verherrlicht worden war", "literal", "ἐδοξάσθη", None, None, "δοξάζω ist durchgehend «verherrlichen» (Grundentscheid); bei Johannes auf Jesu Tod und Erhöhung bezogen (vgl. [[JHN.12.16]], [[JHN.12.23]])."),
 ("JHN.7.42", "der Nachkommenschaft", "adapted", "τοῦ σπέρματος", "dem Samen", None, "Vgl. [[2SA.7.12]] und [[MIC.5.2]]. Johannes erzählt nicht, wo Jesus geboren wurde; ob die Sprechenden hier ironisch im Irrtum gezeigt werden, wird verschieden beurteilt."),
 ("JHN.7.49", "verflucht", "literal", "ἐπάρατοί", None, None, "Abschätziges Urteil über die Menge, die das Gesetz nicht kennt."),
 ("JHN.7.50", "früher", "literal", "πρότερον", None, None, "Vgl. [[JHN.3.1]]–[[JHN.3.2]]."),
 ("JHN.7.52", "kein Prophet", "literal", "προφήτης οὐκ", None, ["der Prophet nicht"], "Jona stammte nach [[2KI.14.25]] aus Gat-Hefer in Galiläa; der Satz ist deshalb oft als Übertreibung im Streit verstanden worden. In der Transkription von 𝔓66 steht in der Erstschrift ὁ προφήτης («der Prophet»), korrigiert ohne Artikel; das würde sich auf den erwarteten Propheten beziehen (vgl. [[JHN.7.40]]). Der SBLGNT-Apparat führt diese Lesart nicht."),
 ("JHN.7.53", "⟦Und jeder ging", "literal", "καὶ ἐπορεύθη ἕκαστος", None, None, PA_DE),
]

DEC_GSW = [
 ('JHN.6.7', 'Denar', 'literal', 'δηναρίων', None, None, 'En Denar isch de üblich Taglohn vomene Arbeiter gsii ([[MAT.20.2]]); zweihundert Denar sind öppe zweihundert Taglöhn. Damalige Münzname im Text, de Wärt i de Erkläärig (Entscheid Andi Neck 2026-10-26).'),
 ("JHN.6.1", "vom See", "adapted", "τῆς θαλάσσης", "vom Meer", None, "De Johannes säit em See Gennesaret wie de Markus und de Matthäus θάλασσα («Meer»)."),
 ("JHN.6.2", "d Zeiche", "literal", "τὰ σημεῖα", None, ["d Wunder"], "σημεῖον isch überall «Zeiche», nöd «Wunder»: De Johannes nännt d Tate vom Jesus Zeiche, wo über sich use zeiged ([[JHN.2.11]], [[JHN.20.30]]). Grundentscheid nach scripts/authoring/johannes_text_01_03.py."),
 ("JHN.6.9", "Gerschtebroot", "literal", "ἄρτους κριθίνους", None, None, "Gerschtebroot isch billiger gsii als Weizebroot (vgl. [[2KI.4.42]]–[[2KI.4.44]])."),
 ("JHN.6.10", "Lönd d Lüüt abhocke", "adapted", "Ποιήσατε τοὺς ἀνθρώπους ἀναπεσεῖν", "Mached, dass d Mänsche sich anelegged", None, "Mer hät bim Ässe glägen; d Mundart seit eifach «abhocke»."),
 ("JHN.6.20", "Ich bi s", "interpretive", "Ἐγώ εἰμι", None, ["Ich bi"], "ἐγώ εἰμι isch überall «Ich bi …» (Grundentscheid). Da ohni Ergänzig: «Ich bi s». Di gliiche Wort stönd i de griechische Bible für Gott, wo sich vorstellt ([[EXO.3.14]]); öb de Johannes das da aaklinge laat, isch umstritte."),
 ("JHN.6.23", "aber", "interpretive", "ἀλλὰ", None, ["anderi (Boot)"], "Di alte Handschrifte händ kei Akzänt: ΑΛΛΑ cha «aber» oder «anderi» heisse; lueg d Alternative."),
 ("JHN.6.26", "Amen, amen, ich säge eu", "literal", "Ἀμὴν ἀμὴν λέγω ὑμῖν", None, None, "De Johannes verdopplet s Amen. Überall «Amen, amen, ich säge eu» (Grundentscheid)."),
 ("JHN.6.27", "bliibt", "literal", "μένουσαν", None, None, "μένω isch überall «bliibe» (Grundentscheid)."),
 ("JHN.6.27", "de Mänschesohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None, "Bezeichnig, wo de Jesus für sich sälber bruucht (vgl. [[DAN.7.13]])."),
 ("JHN.6.27", "mit sim Siegel bestätiget", "adapted", "ἐσφράγισεν", "versiglet", None, None),
 ("JHN.6.33", "das, wo", "interpretive", "ὁ καταβαίνων", None, ["dä, wo"], "Cha sich ufs Broot bezie oder scho uf e Person; [[JHN.6.35]] löst s uf de Jesus hii uf."),
 ("JHN.6.35", "Ich bi s Broot vom Läbe", "literal", "Ἐγώ εἰμι ὁ ἄρτος τῆς ζωῆς", None, None, "S erscht vo de «Ich bi»-Wort mit eme Bild (wiiter [[JHN.8.12]], [[JHN.10.11]], [[JHN.11.25]], [[JHN.14.6]], [[JHN.15.1]])."),
 ("JHN.6.41", "d Jude", "interpretive", "οἱ Ἰουδαῖοι", None, ["d Judäer", "di jüdische Füerer"], "Grundentscheid: wörtlich «d Jude». De Johannes bruucht s Wort für s Volk, für d Lüüt us Judäa und oft für di füerende Chreis z Jerusalem; au de Jesus und sini Jünger sind Jude. Lueg translation_notes."),
 ("JHN.6.41", "gmuulet", "literal", "Ἐγόγγυζον", "gmurret", None, "Erinneret as Murre vo Israel i de Wüeschti ([[EXO.16.2]])."),
 ("JHN.6.45", "Und si wärded alli vo Gott glehrt sii", "literal", "Καὶ ἔσονται πάντες διδακτοὶ θεοῦ", None, None, "Zitat us [[ISA.54.13]]."),
 ("JHN.6.51", "Fleisch", "literal", "σάρξ", None, ["Liib"], "Vgl. [[JHN.1.14]]. Öb [[JHN.6.51]]–[[JHN.6.58]] uf s Aabigmaal aaspiled, wird verschide beurteilt."),
 ("JHN.6.54", "isst", "interpretive", "τρώγων", "chäut", None, "Ab da staat τρώγω; öb das «chäue» betont oder eifach «ässe» heisst, isch umstritte."),
 ("JHN.6.62", "wo er vorher gsii isch", "adapted", "ὅπου ἦν τὸ πρότερον", None, None, "De Satz bricht ab; de Nachsatz fäält im Griechische."),
 ("JHN.6.64", "wird uslifere", "literal", "παραδώσων", None, ["wird verrate"], "παραδίδωμι isch überall «uslifere»."),
 ("JHN.6.69", "de Heilig vo Gott", "literal", "ὁ ἅγιος τοῦ θεοῦ", None, None, "Lueg d Alternative."),
 ("JHN.6.70", "en Tüüfel", "interpretive", "διάβολός", None, ["en Verleumder"], None),
 ("JHN.7.1", "d Jude", "interpretive", "οἱ Ἰουδαῖοι", None, ["d Judäer", "di jüdische Füerer"], "Wie i [[JHN.6.41]]; da staat Ἰουδαῖοι grad näbe Ἰουδαία («Judäa»)."),
 ("JHN.7.2", "s Laubhüttefäscht", "literal", "ἡ σκηνοπηγία", None, ["Sukkot"], "S siebetägig Herbschtfäscht ([[LEV.23.34]]–[[LEV.23.43]])."),
 ("JHN.7.6", "Ziit", "interpretive", "καιρὸς", None, ["di richtig Ziit"], "καιρός isch de passend Momänt; daneb staat «Stund» ([[JHN.7.30]])."),
 ("JHN.7.8", "Ich gang nöd ufe", "literal", "ἐγὼ οὐκ ἀναβαίνω", None, ["Ich gang no nöd ufe"], "De Jesus gaat churz druf glich ([[JHN.7.10]]); lueg d Alternative."),
 ("JHN.7.12", "Gmurmel", "interpretive", "γογγυσμὸς", None, ["Gmuul"], "Di gliich Wortfamilie wie «muule» ([[JHN.6.41]]), da aber halbluuts Rede."),
 ("JHN.7.13", "vor de Jude", "interpretive", "τῶν Ἰουδαίων", None, ["vor de jüdische Füerer"], "Di, wo da redet, sind sälber Jude; gmeint sind wohl di füerende Chreis."),
 ("JHN.7.18", "Ehr", "interpretive", "δόξαν", None, ["Herrlichkeit"], "δόξα isch Grundentscheid «Herrlichkeit»; da gaat s um Aaseh, drum «Ehr»."),
 ("JHN.7.26", "de Christus", "traditional", "ὁ χριστός", None, ["de Messias", "de Gsalbet"], None),
 ("JHN.7.32", "Diener", "interpretive", "ὑπηρέτας", None, ["Tämpelwächter"], None),
 ("JHN.7.35", "d Diaspora under de Grieche", "interpretive", "τὴν διασπορὰν τῶν Ἑλλήνων", None, None, "D Jude usserhalb vom Land Israel; öb mit de «Grieche» Jude oder Nichtjude gmeint sind, isch offe."),
 ("JHN.7.38", "Wer a mich glaubt", "interpretive", "ὁ πιστεύων εἰς ἐμέ", None, ["und es trinki, wer a mich glaubt"], "D Übersetzig folgt de Zeichesetzig vom SBLGNT: «sis Innere» isch das vom Gläubige. Anderi ziend «wer a mich glaubt» zu [[JHN.7.37]] und beziend d Ström uf de Jesus sälber."),
 ("JHN.7.38", "Innere", "interpretive", "κοιλίας", "Liib", ["Buuch"], None),
 ("JHN.7.39", "de Geischt isch no nöd da gsii", "adapted", "οὔπω γὰρ ἦν πνεῦμα", "no nöd isch Geischt gsii", None, "Gmeint isch: er isch no nöd gää gsii (vgl. [[JHN.20.22]]); lueg d Alternative."),
 ("JHN.7.39", "verherrlicht worde isch", "literal", "ἐδοξάσθη", None, None, "δοξάζω isch überall «verherrliche» (Grundentscheid)."),
 ("JHN.7.53", "⟦Und jede isch", "literal", "καὶ ἐπορεύθη ἕκαστος", None, None, PA_GSW),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-JHN-006-011-02:R2", "JHN.6.11", "teilte er sie aus an die Lagernden", "teilte er sie den Jüngern aus, die Jünger aber den Lagernden",
  "hät er s verteilt a d Lüüt, wo da gläge sind", "hät er s de Jünger verteilt, und d Jünger de Lüüt, wo da gläge sind", "gering",
  "Mit Zusatz: Jesus gibt die Brote den Jüngern, diese verteilen sie.", "Mit Zuesatz: De Jesus git d Broot de Jünger, und die verteiled si.",
  {"R1": [("διέδωκεν τοῖς ἀνακειμένοις", "teilte aus an die Lagernden", None)], "R2": [("διέδωκεν τοῖς μαθηταῖς, οἱ δὲ μαθηταὶ τοῖς ἀνακειμένοις", "teilte den Jüngern aus, die Jünger aber den Lagernden", "RP")]},
  {"R1": [("διέδωκεν τοῖς ἀνακειμένοις", "hät verteilt a d Lüüt, wo da gläge sind", None)], "R2": [("διέδωκεν τοῖς μαθηταῖς, οἱ δὲ μαθηταὶ τοῖς ἀνακειμένοις", "hät s de Jünger verteilt, und d Jünger de Lüüt", "RP")]},
  ["Der Zusatz entspricht der Darstellung bei den anderen Evangelisten ([[MAT.14.19]], [[MRK.6.41]]); Abschreiber haben Parallelberichte oft angeglichen.",
   "Laut der automatischen Zuordnung und den Transkriptionen hat 05 den Zusatz (mit ἔδωκεν statt διέδωκεν); 02, 03, 032 und 𝔓75 lesen ohne ihn, 01, 𝔓28 und 𝔓66 ebenfalls ohne Zusatz, aber mit ἔδωκεν."],
  ["De Zuesatz entspricht em Bricht vo de andere Evangelischte ([[MAT.14.19]], [[MRK.6.41]]).",
   "Nach de automatische Zueornig und de Transkriptione hät 05 de Zuesatz; 01, 02, 03, 032, 𝔓28, 𝔓66 und 𝔓75 händ en nöd."]),
 ("VAR-SBLGNTAPP-JHN-006-014-01:R2", "JHN.6.14", "das Zeichen sahen, das er getan hatte", "die Zeichen sahen, die er getan hatte",
  "s Zeiche gseh händ, wo er gmacht hät", "d Zeiche gseh händ, wo er gmacht hät", "gering",
  "Mehrzahl statt Einzahl (WH).", "Mehrzahl statt Einzahl (WH).",
  {"R1": [("ὃ ἐποίησεν σημεῖον", "das Zeichen, das er getan hatte", "SBLGNT, Treg, NA28, RP")], "R2": [("ἃ ἐποίησεν σημεῖα", "die Zeichen, die er getan hatte", "WH")]},
  {"R1": [("ὃ ἐποίησεν σημεῖον", "s Zeiche, wo er gmacht hät", "SBLGNT, Treg, NA28, RP")], "R2": [("ἃ ἐποίησεν σημεῖα", "d Zeiche, wo er gmacht hät", "WH")]},
  ["Die Einzahl bezieht sich auf die Speisung; die Mehrzahl kann an [[JHN.6.2]] angleichen.",
   "Laut der automatischen Zuordnung lesen 01, 02, 05 und 032 die Einzahl, 03 und 𝔓75 die Mehrzahl."],
  ["D Einzahl bezieht sich uf d Spiisig; d Mehrzahl cha a [[JHN.6.2]] aagliche.",
   "Nach de automatische Zueornig läsed 01, 02, 05 und 032 d Einzahl, 03 und 𝔓75 d Mehrzahl."]),
 ("VAR-SBLGNTAPP-JHN-006-022-02:R2", "JHN.6.22", "ausser einem", "ausser jenem einen, in das seine Jünger eingestiegen waren",
  "usser eim", "usser säbem einte, wo sini Jünger iigstige sind", "gering",
  "Mit erklärendem Zusatz.", "Mit eme erkläärende Zuesatz.",
  {"R1": [("ἕν", "einem", None)], "R2": [("ἓν ἐκεῖνο εἰς ὃ ἐνέβησαν οἱ μαθηταὶ αὐτοῦ", "jenem einen, in das seine Jünger eingestiegen waren", "RP")]},
  {"R1": [("ἕν", "eim", None)], "R2": [("ἓν ἐκεῖνο εἰς ὃ ἐνέβησαν οἱ μαθηταὶ αὐτοῦ", "säbem einte, wo sini Jünger iigstige sind", "RP")]},
  ["Der Satz ist umständlich; der Zusatz verdeutlicht, um welches Boot es geht.",
   "Laut der automatischen Zuordnung haben 01 (Erstschrift und Korrektur) und 05 den Zusatz (01 mit «Jünger Jesu»), 02, 03, 032 und 𝔓75 nicht."],
  ["De Satz isch umständlich; de Zuesatz macht klar, um wele Boot s gaat.",
   "Nach de automatische Zueornig händ 01 und 05 de Zuesatz, 02, 03, 032 und 𝔓75 nöd."]),
 ("VAR-SBLGNTAPP-JHN-006-023-01:R2", "JHN.6.23", "Es kamen jedoch Boote", "Andere Boote kamen",
  "Es sind aber Boot", "Anderi Boot sind", "gering",
  "ἄλλα («andere») statt ἀλλά («jedoch»); RP liest ἄλλα δέ («andere aber»).", "ἄλλα («anderi») statt ἀλλά («aber»); RP lisst ἄλλα δέ.",
  {"R1": [("ἀλλὰ", "jedoch", "WH, Treg")], "R2": [("ἄλλα", "andere", "NA28")], "R3": [("ἄλλα δὲ", "andere aber", "RP")]},
  {"R1": [("ἀλλὰ", "aber", "WH, Treg")], "R2": [("ἄλλα", "anderi", "NA28")], "R3": [("ἄλλα δὲ", "anderi aber", "RP")]},
  ["Der Unterschied liegt zunächst in der Akzentsetzung: Die alten Majuskeln schreiben ΑΛΛΑ ohne Akzent, die Deutung ist eine Entscheidung der Herausgeber. Mit δέ ist nur «andere» möglich.",
   "Die automatische Zuordnung kann 03 und 𝔓75 (ΑΛΛΑ) deshalb keiner Lesart sicher zuordnen; 02 und 032 lesen αλλα δε. 01 und 05 bauen den Satz anders (Genitivus absolutus: 01 «als nun die Boote aus Tiberias herankamen», 05 «als andere Boote aus Tiberias kamen»)."],
  ["De Underschid liit z erscht im Akzänt: Di alte Handschrifte schriibed ΑΛΛΑ ohni Akzänt.",
   "D automatisch Zueornig cha 03 und 𝔓75 drum keinere Läsart sicher zueordne; 02 und 032 läsed αλλα δε; 01 und 05 bouet de Satz anders."]),
 ("VAR-SBLGNTAPP-JHN-006-040-02:R2", "JHN.6.40", "der Wille meines Vaters", "der Wille dessen, der mich gesandt hat",
  "de Wille vo mim Vatter", "de Wille vo däm, wo mich gschickt hät", "gering",
  "Gleicht an [[JHN.6.39]] an.", "Gliicht a [[JHN.6.39]] aa.",
  {"R1": [("πατρός μου", "meines Vaters", None)], "R2": [("πέμψαντός με", "dessen, der mich gesandt hat", "RP")]},
  {"R1": [("πατρός μου", "vo mim Vatter", None)], "R2": [("πέμψαντός με", "vo däm, wo mich gschickt hät", "RP")]},
  ["Die Wendung aus dem vorangehenden Vers kann beim Abschreiben übernommen worden sein.",
   "Nach den Transkriptionen lesen 01, 03, 04, 05, 029, 032, 𝔓66 und 𝔓75 «meines Vaters» (teils abgekürzt =πρσ, weshalb die automatische Zuordnung einige als «liest anders» führt), 02 «dessen, der mich gesandt hat»."],
  ["D Wändig us em Vers vorher cha bim Abschriibe übernoo worde sii.",
   "Nach de Transkriptione läsed 01, 03, 04, 05, 029, 032, 𝔓66 und 𝔓75 «vo mim Vatter», 02 «vo däm, wo mich gschickt hät»."]),
 ("VAR-SBLGNTAPP-JHN-006-047-01:R2", "JHN.6.47", "Wer glaubt", "Wer an mich glaubt",
  "Wer glaubt", "Wer a mich glaubt", "gering",
  "Mit «an mich» (Treg, RP).", "Mit «a mich» (Treg, RP).",
  {"R1": [("ὁ πιστεύων", "wer glaubt", "SBLGNT, WH, NA28")], "R2": [("ὁ πιστεύων εἰς ἐμέ", "wer an mich glaubt", "Treg, RP")]},
  {"R1": [("ὁ πιστεύων", "wer glaubt", "SBLGNT, WH, NA28")], "R2": [("ὁ πιστεύων εἰς ἐμέ", "wer a mich glaubt", "Treg, RP")]},
  ["Der Zusatz kann den Satz nach [[JHN.6.35]] vervollständigen; die kürzere Form kann aber auch eine Verkürzung sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 029, 032, 𝔓66 und 𝔓75 ohne, 02 und 05 mit «an mich»."],
  ["De Zuesatz cha de Satz nach [[JHN.6.35]] ergänze.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 029, 032, 𝔓66 und 𝔓75 ohni, 02 und 05 mit «a mich»."]),
 ("VAR-SBLGNTAPP-JHN-006-069-01:R2", "JHN.6.69", "der Heilige Gottes", "der Christus, der Sohn des lebendigen Gottes",
  "de Heilig vo Gott", "de Christus, de Sohn vom läbige Gott", "mittel",
  "Statt «der Heilige Gottes» liest RP «der Christus, der Sohn des lebendigen Gottes» (zusammen mit VAR-SBLGNTAPP-JHN-006-069-02).",
  "Statt «de Heilig vo Gott» lisst RP «de Christus, de Sohn vom läbige Gott».",
  {"R1": [("ὁ ἅγιος τοῦ θεοῦ", "der Heilige Gottes", "SBLGNT, WH, Treg, NA28")], "R2": [("ὁ χριστὸς ὁ υἱὸς τοῦ θεοῦ τοῦ ζῶντος", "der Christus, der Sohn des lebendigen Gottes", "RP")]},
  {"R1": [("ὁ ἅγιος τοῦ θεοῦ", "de Heilig vo Gott", "SBLGNT, WH, Treg, NA28")], "R2": [("ὁ χριστὸς ὁ υἱὸς τοῦ θεοῦ τοῦ ζῶντος", "de Christus, de Sohn vom läbige Gott", "RP")]},
  ["Die längere Form entspricht dem Petrusbekenntnis in [[MAT.16.16]]; Abschreiber haben bekannte Parallelen oft angeglichen.",
   "Nach den Transkriptionen lesen 01, 03, 04, 05, 032 und 𝔓75 «der Heilige Gottes»; 𝔓66 liest «der Christus, der Heilige Gottes». 02 und 029 sind hier nicht erhalten."],
  ["Di länger Form entspricht em Petrusbekänntnis i [[MAT.16.16]].",
   "Nach de Transkriptione läsed 01, 03, 04, 05, 032 und 𝔓75 «de Heilig vo Gott», 𝔓66 «de Christus, de Heilig vo Gott»."]),
 ("VAR-SBLGNTAPP-JHN-007-008-02:R2", "JHN.7.8", "Ich gehe nicht hinauf", "Ich gehe noch nicht hinauf",
  "Ich gang nöd ufe", "Ich gang no nöd ufe", "mittel",
  "οὔπω («noch nicht») statt οὐκ («nicht»); so WH und RP, der SBLGNT folgt hier Treg und NA28.",
  "οὔπω («no nöd») statt οὐκ («nöd»); so WH und RP.",
  {"R1": [("οὐκ", "nicht", "SBLGNT, Treg, NA28")], "R2": [("οὔπω", "noch nicht", "WH, NIV, RP")]},
  {"R1": [("οὐκ", "nöd", "SBLGNT, Treg, NA28")], "R2": [("οὔπω", "no nöd", "WH, NIV, RP")]},
  ["«Noch nicht» glättet den scheinbaren Widerspruch zu [[JHN.7.10]], wo Jesus doch geht; deshalb gilt «nicht» vielen als die schwierigere und ältere Lesart. Umgekehrt kann οὔπω auch durch das folgende οὔπω im selben Vers bedingt sein.",
   "Laut der automatischen Zuordnung lesen 01 und 05 οὐκ, 03, 029, 032, 0323, 𝔓66 und 𝔓75 οὔπω; 04 ist hier nicht erhalten."],
  ["«No nöd» glättet de schiinbaar Widerspruch zu [[JHN.7.10]], wo de Jesus glich gaat.",
   "Nach de automatische Zueornig läsed 01 und 05 οὐκ, 03, 029, 032, 0323, 𝔓66 und 𝔓75 οὔπω."]),
 ("VAR-SBLGNTAPP-JHN-007-009-02:R2", "JHN.7.9", "Nachdem er aber das gesagt hatte", "Nachdem er ihnen aber das gesagt hatte",
  "Nachdem er aber das gseit hät", "Nachdem er ine aber das gseit hät", "gering",
  "αὐτοῖς («ihnen») statt αὐτός («er selbst»); so WH und RP.", "αὐτοῖς («ine») statt αὐτός («er sälber»).",
  {"R1": [("αὐτὸς", "er (selbst)", "SBLGNT, Treg, NA28")], "R2": [("αὐτοῖς", "ihnen", "WH, RP")]},
  {"R1": [("αὐτὸς", "er (sälber)", "SBLGNT, Treg, NA28")], "R2": [("αὐτοῖς", "ine", "WH, RP")]},
  ["Die Wörter unterscheiden sich in der Schrift nur wenig; beide ergeben Sinn.",
   "Laut der automatischen Zuordnung lesen 01, 05, 032 und 𝔓66 αὐτός, 03, 029, 0323 und 𝔓75 αὐτοῖς."],
  ["D Wörter underscheided sich i de Schrift nume wenig.",
   "Nach de automatische Zueornig läsed 01, 05, 032 und 𝔓66 αὐτός, 03, 029, 0323 und 𝔓75 αὐτοῖς."]),
 ("VAR-SBLGNTAPP-JHN-007-039-03:R2", "JHN.7.39", "der Geist war noch nicht da", "der heilige Geist war noch nicht da",
  "de Geischt isch no nöd da gsii", "de heilig Geischt isch no nöd da gsii", "mittel",
  "Mit «heilig» (Treg, RP); NIV liest «gegeben» (R3). Die Zusätze erklären den knappen Ausdruck.",
  "Mit «heilig» (Treg, RP); NIV lisst «gää» (R3).",
  {"R1": [("πνεῦμα", "Geist", "SBLGNT, WH, NA28")], "R2": [("πνεῦμα ἅγιον", "heiliger Geist", "Treg, RP")], "R3": [("πνεῦμα δεδομένον", "Geist gegeben", "NIV")]},
  {"R1": [("πνεῦμα", "Geischt", "SBLGNT, WH, NA28")], "R2": [("πνεῦμα ἅγιον", "heilige Geischt", "Treg, RP")], "R3": [("πνεῦμα δεδομένον", "Geischt gää", "NIV")]},
  ["Der knappe Satz «noch nicht war Geist» konnte missverstanden werden; Zusätze wie «heilig», «gegeben» oder «auf ihnen» machen ihn eindeutig.",
   "Nach den Transkriptionen lesen 01, 029 und 𝔓75 nur πνεῦμα; 032 πνεῦμα ἅγιον; 03 πνεῦμα ἅγιον δεδομένον; 05 τὸ πνεῦμα ἅγιον ἐπʼ αὐτοῖς («der heilige Geist auf ihnen»); in 𝔓66 steht ἅγιον in der Erstschrift und ist durch Korrektur getilgt. Die automatische Zuordnung führt die meisten dieser Zeugen als «liest anders», weil ihr Wortlaut keiner Apparat-Lesart genau entspricht."],
  ["De churz Satz «no nöd isch Geischt gsii» hät chöne missverstande wärde; Zuesätz mached en eidüütig.",
   "Nach de Transkriptione läsed 01, 029 und 𝔓75 nume πνεῦμα; 032 πνεῦμα ἅγιον; 03 πνεῦμα ἅγιον δεδομένον; 05 τὸ πνεῦμα ἅγιον ἐπʼ αὐτοῖς; in 𝔓66 isch ἅγιον dur e Korrektur gstriche."]),
 ("VAR-SBLGNTAPP-JHN-007-046-02:R2", "JHN.7.46", "Noch nie hat ein Mensch so geredet", "Noch nie hat ein Mensch so geredet wie dieser Mensch",
  "No nie hät en Mänsch eso gredt", "No nie hät en Mänsch eso gredt wie dä Mänsch", "gering",
  "Mit Zusatz «wie dieser Mensch» (Treg, RP).", "Mit Zuesatz «wie dä Mänsch» (Treg, RP).",
  {"R1": [("ἄνθρωπος", "ein Mensch", "SBLGNT, WH, NA28")], "R2": [("ἄνθρωπος ὡς οὗτος ὁ ἄνθρωπος", "ein Mensch wie dieser Mensch", "Treg, RP")]},
  {"R1": [("ἄνθρωπος", "en Mänsch", "SBLGNT, WH, NA28")], "R2": [("ἄνθρωπος ὡς οὗτος ὁ ἄνθρωπος", "en Mänsch wie dä Mänsch", "Treg, RP")]},
  ["Der Vergleich kann zur Verdeutlichung ergänzt worden sein; die kürzere Form wirkt knapper und offener.",
   "Nach den Transkriptionen haben 01 («wie dieser redet, der Mensch»), 05 («wie dieser redet») und 𝔓66 in der Erstschrift einen Vergleich; 03, 029, 032, 𝔓75 und 𝔓66 nach Korrektur lesen ohne. Die automatische Zuordnung führt 01, 05 und 𝔓66 abweichend davon bei R1; die Angaben hier stützen sich auf die Transkriptionen."],
  ["De Vergliich cha zur Verdüütlichig ergänzt worde sii.",
   "Nach de Transkriptione händ 01, 05 und 𝔓66 (Erstschrift) en Vergliich; 03, 029, 032, 𝔓75 und 𝔓66 nach de Korrektur nöd."]),
 ("VAR-SBLGNTAPP-JHN-007-050-01:R2", "JHN.7.50", "der früher zu ihm gekommen war", "der früher bei Nacht zu ihm gekommen war",
  "wo früener zu ihm choo isch", "wo früener znacht zu ihm choo isch", "gering",
  "Mit «bei Nacht» (RP), nach [[JHN.3.2]].", "Mit «znacht» (RP), nach [[JHN.3.2]].",
  {"R1": [("ἐλθὼν", "gekommen", None)], "R2": [("ἐλθὼν νυκτὸς", "bei Nacht gekommen", "RP")]},
  {"R1": [("ἐλθὼν", "choo", None)], "R2": [("ἐλθὼν νυκτὸς", "znacht choo", "RP")]},
  ["Der Zusatz erinnert an [[JHN.3.2]] und [[JHN.19.39]].",
   "Laut der automatischen Zuordnung lesen 03, 029, 032, 05 und 𝔓75 ohne «bei Nacht»; nach der Transkription hat 05 aber νυκτὸς τὸ πρῶτον («bei Nacht, das erste Mal») an anderer Stelle im Satz. 01 hat die Wendung «der früher zu ihm gekommen war» nicht."],
  ["De Zuesatz erinneret a [[JHN.3.2]] und [[JHN.19.39]].",
   "Nach de Transkription hät 05 νυκτὸς τὸ πρῶτον amene andere Ort im Satz; 03, 029, 032 und 𝔓75 händ «znacht» nöd."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-006-001-071", "JHN.6.1-JHN.6.71", "section", "Das Brot des Lebens",
  ["TU-JHN-006-001-015", "TU-JHN-006-016-021", "TU-JHN-006-022-034", "TU-JHN-006-035-040", "TU-JHN-006-041-051",
   "TU-JHN-006-052-059", "TU-JHN-006-060-071"],
  "Kurz vor dem Passa sättigt Jesus am See von Galiläa mit fünf Gerstenbroten und zwei Fischen eine grosse Menge; die Leute halten ihn für den Propheten, der in die Welt kommt, und wollen ihn zum König machen, er aber zieht sich zurück. In der Nacht kommt er auf dem See zu den Jüngern: «Ich bin es; fürchtet euch nicht!» In Kafarnaum sucht ihn die Menge. Im Gespräch dort (nach [[JHN.6.59]] lehrt er in der Synagoge) nennt er sich das Brot des Lebens, das vom Himmel herabgekommen ist, und sagt, wer sein Fleisch esse und sein Blut trinke, habe ewiges Leben. Die Juden murren und streiten darüber; viele seiner Jünger finden das Wort hart und ziehen sich zurück. Simon Petrus antwortet für die Zwölf: «Du hast Worte ewigen Lebens.» Jesus sagt, einer von ihnen sei ein Teufel; der Erzähler bezieht das auf Judas, der ihn ausliefern sollte.", SEG),
 ("TU-JHN-006-001-015", "JHN.6.1-JHN.6.15", "narrative", "Die Speisung der Fünftausend", None,
  "Eine grosse Menge folgt Jesus wegen der Zeichen an den Kranken. Um Philippus zu prüfen, fragt Jesus, woher man Brot für sie kaufen solle; Andreas weist auf einen Jungen mit fünf Gerstenbroten und zwei Fischen. Jesus dankt und teilt aus; etwa fünftausend Männer werden satt, und zwölf Körbe mit Brocken bleiben übrig. Die Menschen sagen, er sei wahrhaftig der Prophet, der in die Welt kommt; weil er erkennt, dass sie ihn mit Gewalt zum König machen wollen, zieht er sich allein auf den Berg zurück.", None),
 ("TU-JHN-006-016-021", "JHN.6.16-JHN.6.21", "narrative", "Jesus kommt auf dem See zu den Jüngern", None,
  "Am Abend fahren die Jünger ohne Jesus über den See nach Kafarnaum; ein starker Wind wühlt das Wasser auf. Sie sehen Jesus auf dem See gehen und fürchten sich; er sagt: «Ich bin es; fürchtet euch nicht!» Als sie ihn ins Boot nehmen wollen, ist das Boot sogleich am Land.", None),
 ("TU-JHN-006-022-034", "JHN.6.22-JHN.6.34", "dialogue", "Die Menge sucht Jesus: Brot vom Himmel", None,
  "Am folgenden Tag fährt die Menge nach Kafarnaum und findet Jesus. Er sagt, sie suchten ihn nicht wegen der Zeichen, sondern weil sie satt geworden seien, und mahnt sie, für die Speise zu arbeiten, die zum ewigen Leben bleibt; Gottes Werk sei, an den zu glauben, den er gesandt hat. Sie verlangen ein Zeichen und berufen sich auf das Manna in der Wüste. Jesus antwortet, nicht Mose habe das Brot vom Himmel gegeben, sondern sein Vater gebe das wahre Brot vom Himmel, das der Welt Leben gibt. Sie bitten: «Herr, gib uns immer dieses Brot!»", None),
 ("TU-JHN-006-035-040", "JHN.6.35-JHN.6.40", "discourse", "«Ich bin das Brot des Lebens»", None,
  "Jesus sagt: «Ich bin das Brot des Lebens.» Wer zu ihm kommt, wird nicht hungern, wer an ihn glaubt, nicht dürsten; sie aber haben ihn gesehen und glauben nicht. Alles, was der Vater ihm gibt, wird zu ihm kommen, und wer kommt, den stösst er nicht hinaus. Er ist vom Himmel herabgekommen, um den Willen dessen zu tun, der ihn gesandt hat: nichts von dem zu verlieren, was der Vater ihm gegeben hat, sondern es am letzten Tag aufzuerwecken; jeder, der den Sohn sieht und an ihn glaubt, soll ewiges Leben haben.", None),
 ("TU-JHN-006-041-051", "JHN.6.41-JHN.6.51", "discourse", "Das lebendige Brot", None,
  "Die Juden murren, weil er sagt, er sei vom Himmel herabgekommen: Sie kennen doch seinen Vater und seine Mutter. Jesus antwortet, niemand könne zu ihm kommen, wenn der Vater ihn nicht zieht; wer vom Vater gehört und gelernt hat, kommt zu ihm. Wer glaubt, hat ewiges Leben. Die Väter assen in der Wüste das Manna und starben; er ist das lebendige Brot vom Himmel, und wer davon isst, wird in Ewigkeit leben. Das Brot, das er geben wird, ist sein Fleisch, für das Leben der Welt.", None),
 ("TU-JHN-006-052-059", "JHN.6.52-JHN.6.59", "discourse", "Fleisch essen und Blut trinken", None,
  "Die Juden streiten, wie er ihnen sein Fleisch zu essen geben könne. Jesus sagt: Wer das Fleisch des Menschensohnes nicht isst und sein Blut nicht trinkt, hat kein Leben in sich; wer es isst und trinkt, hat ewiges Leben und wird am letzten Tag auferweckt; er bleibt in Jesus und Jesus in ihm, und er wird durch Jesus leben, wie Jesus durch den Vater lebt. Das sagt er, als er in der Synagoge in Kafarnaum lehrt.", None),
 ("TU-JHN-006-060-071", "JHN.6.60-JHN.6.71", "narrative", "Viele gehen weg, Petrus antwortet", None,
  "Viele seiner Jünger finden das Wort hart und murren. Jesus fragt, ob es sie zu Fall bringe, und sagt: Der Geist macht lebendig, das Fleisch nützt nichts, seine Worte sind Geist und Leben; niemand kann zu ihm kommen, wenn es ihm nicht vom Vater gegeben ist. Er weiss von Anfang an, wer nicht glaubt und wer ihn ausliefern wird. Viele Jünger ziehen sich zurück. Jesus fragt die Zwölf, ob auch sie weggehen wollen; Simon Petrus antwortet: «Herr, zu wem sollen wir gehen? Du hast Worte ewigen Lebens», und bekennt ihn als den Heiligen Gottes. Jesus antwortet, einer von ihnen sei ein Teufel; der Erzähler bezieht das auf Judas, Sohn des Simon Iskariot, der ihn ausliefern sollte.", None),
 ("TU-JHN-007-001-053", "JHN.7.1-JHN.7.53", "section", "Jesus am Laubhüttenfest",
  ["TU-JHN-007-001-009", "TU-JHN-007-010-013", "TU-JHN-007-014-024", "TU-JHN-007-025-031", "TU-JHN-007-032-036",
   "TU-JHN-007-037-044", "TU-JHN-007-045-052", "TU-JHN-007-053-053"],
  "Jesus zieht in Galiläa umher, weil ihn die Juden in Judäa töten wollen. Seine Brüder, die nicht an ihn glauben, drängen ihn, zum Laubhüttenfest zu gehen und sich der Welt zu zeigen; er sagt, seine Zeit sei noch nicht da, geht dann aber im Verborgenen hinauf. Mitten im Fest lehrt er im Tempel: Seine Lehre stammt von dem, der ihn gesandt hat; die Heilung am Sabbat verteidigt er mit der Beschneidung am Sabbat. In der Menge wird gestritten, ob er der Christus sei und woher er komme. Die Hohepriester und Pharisäer senden Diener aus, ihn festzunehmen, doch niemand legt Hand an ihn. Am letzten Tag ruft er, wer Durst habe, solle zu ihm kommen und trinken; der Erzähler bezieht die Ströme lebendigen Wassers auf den Geist. Die Menge spaltet sich; die Diener kehren ohne ihn zurück, und Nikodemus erinnert die Pharisäer daran, dass das Gesetz niemanden richtet, ohne ihn anzuhören. Mit [[JHN.7.53]] beginnt im SBLGNT der in Doppelklammern ⟦ ⟧ gesetzte Abschnitt von der Ehebrecherin ([[JHN.7.53]]–[[JHN.8.11]]), den die Textforschung weithin als spätere Einfügung beurteilt.",
  SEG + " [[JHN.7.53]] bildet eine eigene Teileinheit, weil der Abschnitt von der Ehebrecherin dort beginnt und über die Kapitelgrenze reicht; die Fortsetzung [[JHN.8.1]]–[[JHN.8.11]] gehört zu Kapitel 8."),
 ("TU-JHN-007-001-009", "JHN.7.1-JHN.7.9", "narrative", "Jesus und seine Brüder", None,
  "Weil die Juden ihn töten wollen, zieht Jesus in Galiläa umher. Vor dem Laubhüttenfest drängen ihn seine Brüder, nach Judäa zu gehen und sich der Welt zu offenbaren, damit auch seine Jünger seine Werke sehen; der Erzähler bemerkt, dass auch sie nicht an ihn glaubten. Jesus antwortet, seine Zeit sei noch nicht da; die Welt hasse ihn, weil er bezeuge, dass ihre Werke böse sind. Er gehe nicht zu diesem Fest hinauf; und er bleibt in Galiläa.", None),
 ("TU-JHN-007-010-013", "JHN.7.10-JHN.7.13", "narrative", "Jesus geht im Verborgenen zum Fest", None,
  "Nachdem seine Brüder hinaufgegangen sind, geht auch Jesus zum Fest, nicht öffentlich, sondern gleichsam im Verborgenen. Die Juden suchen ihn am Fest. In der Menge wird über ihn gemurmelt: Die einen sagen, er sei gut, andere, er verführe das Volk. Aus Furcht vor den Juden redet niemand offen über ihn.", None),
 ("TU-JHN-007-014-024", "JHN.7.14-JHN.7.24", "dialogue", "Lehre im Tempel", None,
  "Mitten im Fest lehrt Jesus im Tempel. Die Juden wundern sich, dass er die Schriften kennt, ohne gelernt zu haben. Jesus sagt, seine Lehre sei die dessen, der ihn gesandt hat; wer Gottes Willen tun will, wird das erkennen. Er hält ihnen vor, keiner von ihnen tue das Gesetz, und fragt, warum sie ihn töten wollen; die Menge antwortet, er habe einen Dämon. Mit der Beschneidung am Sabbat begründet er, dass er einen ganzen Menschen am Sabbat gesund gemacht hat, und mahnt, nicht nach dem Augenschein zu urteilen.", None),
 ("TU-JHN-007-025-031", "JHN.7.25-JHN.7.31", "dialogue", "Ist er der Christus?", None,
  "Einige Leute aus Jerusalem wundern sich, dass der, den man töten will, offen redet, und fragen, ob die Oberen ihn als den Christus erkannt haben; aber von ihm wisse man, woher er sei, beim Christus wisse das niemand. Jesus ruft im Tempel, sie kennten ihn und wüssten, woher er sei; doch der ihn gesandt hat, ist wahrhaftig, und den kennen sie nicht, er aber kennt ihn. Man sucht ihn festzunehmen, doch niemand legt Hand an ihn, weil seine Stunde noch nicht gekommen ist. Viele aus der Menge glauben an ihn.", None),
 ("TU-JHN-007-032-036", "JHN.7.32-JHN.7.36", "dialogue", "«Ihr werdet mich suchen und nicht finden»", None,
  "Als die Pharisäer das Gemurmel der Menge hören, senden sie und die Hohepriester Diener, um ihn festzunehmen. Jesus sagt, er sei noch eine kleine Zeit bei ihnen und gehe dann zu dem, der ihn gesandt hat; sie würden ihn suchen und nicht finden, und wo er sei, dahin könnten sie nicht kommen. Die Juden fragen sich, ob er in die Diaspora zu den Griechen gehen wolle.", None),
 ("TU-JHN-007-037-044", "JHN.7.37-JHN.7.44", "narrative", "Ströme lebendigen Wassers", None,
  "Am letzten, grossen Tag des Festes ruft Jesus: Wer Durst hat, soll zu ihm kommen und trinken; mit einem Schriftwort spricht er von Strömen lebendigen Wassers, die aus dem Inneren fliessen werden (auf wen sich das bezieht, wird verschieden verstanden). Der Erzähler erklärt, er habe vom Geist gesprochen, den die Glaubenden empfangen sollten; der Geist war noch nicht da, weil Jesus noch nicht verherrlicht war. In der Menge halten ihn die einen für den Propheten, andere für den Christus; wieder andere wenden ein, nach der Schrift komme der Christus aus Betlehem, nicht aus Galiläa. Es entsteht eine Spaltung; einige wollen ihn festnehmen, doch niemand legt Hand an ihn.", None),
 ("TU-JHN-007-045-052", "JHN.7.45-JHN.7.52", "narrative", "Die Diener kehren zurück; Nikodemus", None,
  "Die Diener kehren ohne Jesus zu den Hohepriestern und Pharisäern zurück: Noch nie habe ein Mensch so geredet. Die Pharisäer fragen, ob auch sie sich hätten verführen lassen, ob etwa einer der Oberen oder Pharisäer an ihn geglaubt habe; das Volk, das das Gesetz nicht kenne, sei verflucht. Nikodemus, einer von ihnen, wendet ein, das Gesetz richte niemanden, ohne ihn zuerst anzuhören. Sie halten ihm entgegen, aus Galiläa stehe kein Prophet auf.", None),
 ("TU-JHN-007-053-053", "JHN.7.53", "narrative", "Beginn des Abschnitts von der Ehebrecherin", None,
  "«Und jeder ging in sein Haus.» Mit diesem Satz beginnt der Abschnitt von der Ehebrecherin ([[JHN.7.53]]–[[JHN.8.11]]), den der SBLGNT in Doppelklammern ⟦ ⟧ setzt; die Fortsetzung steht in Kapitel 8. In der Textforschung wird der Abschnitt weithin als spätere Einfügung in das Johannesevangelium beurteilt. In den im Projekt erfassten CNTR-Transkriptionen von 01, 03, 029, 032, 𝔓66 und 𝔓75 steht hier kein Text, auf [[JHN.7.52]] folgt [[JHN.8.12]]; 05 enthält den Abschnitt. 02 und 04 sind an dieser Stelle nicht erhalten. Nach Angaben der Forschung steht der Abschnitt in einigen späteren Handschriften an anderer Stelle (etwa nach [[JHN.21.25]] oder nach [[LUK.21.38]]); das ist im Projekt nicht anhand von Daten geprüft. Viele Kirchen lesen ihn als Teil der Heiligen Schrift; die Frage seiner Herkunft ist davon zu unterscheiden.", None),
]
UNITS_GSW = {
 "TU-JHN-006-001-071": ("S Broot vom Läbe", "Churz vor em Passa macht de Jesus am See vo Galiläa mit föif Gerschtebroot und zwei Fisch e grossi Mängi satt; d Lüüt halted en für de Prophet, wo i d Wält chunnt, und wänd en zum König mache, er aber zieht sich zrugg. I de Nacht chunnt er uf em See zu de Jünger: «Ich bi s; händ kei Angscht!» Z Kafarnaum suecht en d Mängi. Im Gspröch dört (nach [[JHN.6.59]] lehrt er i de Synagoge) seit er, er sig s Broot vom Läbe, wo vom Himmel abechoo isch, und wer sis Fleisch ässi und sis Bluet trinki, heig ewigs Läbe. D Jude muuled und strited drüber; vili vo sine Jünger finded s Wort hert und ziend sich zrugg. De Simon Petrus antwortet für d Zwölf: «Du häsch Wort vom ewige Läbe.» De Jesus seit, eine vo ine sig en Tüüfel; de Erzäler bezieht das uf de Judas, wo en sött uslifere."),
 "TU-JHN-006-001-015": ("D Spiisig vo de Föiftuusig", "E grossi Mängi lauft em Jesus nache wäge de Zeiche a de Chranke. Für de Philippus z prüefe, fröget de Jesus, vo wo mer Broot für si chönti chaufe; de Andreas zeigt uf en Bueb mit föif Gerschtebroot und zwei Fisch. De Jesus dankt und verteilt; öppe föiftuusig Manne wärded satt, und zwölf Chörb mit Brocke bliibed übrig. D Lüüt säged, er sig würkli de Prophet, wo i d Wält chunnt; wil er merkt, dass si en mit Gwalt zum König wänd mache, zieht er sich elei uf de Bärg zrugg."),
 "TU-JHN-006-016-021": ("De Jesus chunnt uf em See zu de Jünger", "Am Aabig faared d Jünger ohni de Jesus über de See uf Kafarnaum; en starche Wind wüelt s Wasser uf. Si gsehnd de Jesus uf em See laufe und händ Angscht; er seit: «Ich bi s; händ kei Angscht!» Wo s en is Boot wänd nää, isch s Boot sofort am Land."),
 "TU-JHN-006-022-034": ("D Mängi suecht de Jesus: Broot vom Himmel", "Am nächschte Tag faart d Mängi uf Kafarnaum und findt de Jesus. Er seit, si sueched en nöd wäge de Zeiche, sondern wil si satt worde sind, und mahnt si, für s Ässe z schaffe, wo bis is ewig Läbe bliibt; s Wärch vo Gott sig, a dä z glaube, wo er gschickt hät. Si verlanged es Zeiche und berüefed sich uf s Manna i de Wüeschti. De Jesus antwortet, nöd de Mose heig s Broot vom Himmel gää, sondern sin Vatter gäb s wahre Broot vom Himmel, wo de Wält Läbe git. Si bitted: «Herr, gib üs immer das Broot!»"),
 "TU-JHN-006-035-040": ("«Ich bi s Broot vom Läbe»", "De Jesus seit: «Ich bi s Broot vom Läbe.» Wer zu ihm chunnt, wird nie Hunger ha, wer a en glaubt, nie Durscht; si aber händ en gseh und glaubed nöd. Alles, wo em de Vatter git, wird zu ihm choo, und wer chunnt, dä rüert er nöd use. Er isch vom Himmel abechoo, für de Wille vo däm z tue, wo en gschickt hät: nüüt vo däm z verliere, won em de Vatter gää hät, sondern s am letschte Tag uferwecke; jede, wo de Sohn gseht und a en glaubt, söll ewigs Läbe ha."),
 "TU-JHN-006-041-051": ("S läbig Broot", "D Jude muuled, wil er seit, er sig vom Himmel abechoo: Si känned doch sin Vatter und sini Mueter. De Jesus antwortet, niemer chönn zu ihm choo, wänn en de Vatter nöd zieht; wer vom Vatter ghört und glernt hät, chunnt zu ihm. Wer glaubt, hät ewigs Läbe. D Vätter händ i de Wüeschti s Manna ggässe und sind gstorbe; er isch s läbig Broot vom Himmel, und wer devo isst, wird für immer läbe. S Broot, wo er wird gää, isch sis Fleisch, für s Läbe vo de Wält."),
 "TU-JHN-006-052-059": ("Fleisch ässe und Bluet trinke", "D Jude strited, wie dä ine sis Fleisch z ässe chönn gää. De Jesus seit: Wer s Fleisch vom Mänschesohn nöd isst und sis Bluet nöd trinkt, hät kei Läbe i sich; wer s isst und trinkt, hät ewigs Läbe und wird am letschte Tag uferweckt; er bliibt im Jesus und de Jesus i ihm, und er wird dur de Jesus läbe, wie de Jesus dur de Vatter läbt. Das seit er, wo er i de Synagoge z Kafarnaum lehrt."),
 "TU-JHN-006-060-071": ("Vili gönd, de Petrus antwortet", "Vili vo sine Jünger finded s Wort hert und muuled. De Jesus fröget, öb s si z Fall bringi, und seit: De Geischt macht läbig, s Fleisch nützt nüüt, sini Wort sind Geischt und Läbe; niemer cha zu ihm choo, wänn s em nöd vom Vatter gää isch. Er weiss vo Aafang aa, wer nöd glaubt und wer en wird uslifere. Vili Jünger ziend sich zrugg. De Jesus fröget d Zwölf, öb au si wänd gaa; de Simon Petrus antwortet: «Herr, zu wem söled mer gaa? Du häsch Wort vom ewige Läbe», und bekännt en als de Heilig vo Gott. De Jesus antwortet, eine vo ine sig en Tüüfel; de Erzäler bezieht das uf de Judas, de Sohn vom Simon Iskariot, wo en sött uslifere."),
 "TU-JHN-007-001-053": ("De Jesus am Laubhüttefäscht", "De Jesus zieht in Galiläa ume, wil en d Jude in Judäa wänd umbringe. Sini Brüedere, wo nöd a en glaubed, dränged en, as Laubhüttefäscht z gaa und sich de Wält z zeige; er seit, sini Ziit sig no nöd da, gaat dänn aber im Verborgne ufe. Mitts im Fäscht lehrt er im Tämpel: Sini Lehr chunnt vo däm, wo en gschickt hät; d Heilig am Sabbat verteidiget er mit de Beschniidig am Sabbat. I de Mängi strited d Lüüt, öb er de Christus sig und wohär er chöm. D Hoheprieschter und d Pharisäer schicked Diener, für en z verhafte, aber niemer leit d Hand a en. Am letschte Tag rüeft er, wer Durscht heig, söll zu ihm choo und trinke; de Erzäler bezieht d Ström vo läbigem Wasser uf de Geischt. D Mängi spaltet sich; d Diener chömed ohni en zrugg, und de Nikodemus erinneret d Pharisäer dra, dass s Gsetz niemer richtet, ohni en aazlose. Mit [[JHN.7.53]] faat im SBLGNT de Abschnitt vo de Ehebrächerin aa ([[JHN.7.53]]–[[JHN.8.11]]), i Doppelklammere ⟦ ⟧; d Textforschig beurteilt en wiitume als spööteri Iifüegig."),
 "TU-JHN-007-001-009": ("De Jesus und sini Brüedere", "Wil d Jude en wänd umbringe, zieht de Jesus in Galiläa ume. Vor em Laubhüttefäscht dränged en sini Brüedere, uf Judäa z gaa und sich de Wält z zeige, demit au sini Jünger sini Wärch gsehnd; de Erzäler merkt aa, dass au si nöd a en glaubt händ. De Jesus antwortet, sini Ziit sig no nöd da; d Wält hassi en, wil er bezüügi, dass iri Wärch bös sind. Er gang nöd a das Fäscht ufe; und er bliibt in Galiläa."),
 "TU-JHN-007-010-013": ("De Jesus gaat im Verborgne as Fäscht", "Nachdem sini Brüedere ufegange sind, gaat au de Jesus as Fäscht, nöd öffentlich, sondern wie im Verborgne. D Jude sueched en am Fäscht. I de Mängi wird über en gmurmlet: Di einte säged, er sig guet, anderi, er verfüeri s Volk. Us Angscht vor de Jude redt niemer offe über en."),
 "TU-JHN-007-014-024": ("Lehr im Tämpel", "Mitts im Fäscht lehrt de Jesus im Tämpel. D Jude wundered sich, dass er d Schrifte kännt, ohni dass er glernt hät. De Jesus seit, sini Lehr sig die vo däm, wo en gschickt hät; wer de Wille vo Gott wott tue, wird das merke. Er haltet ine vor, keine vo ine haltet s Gsetz, und fröget, werum s en wänd umbringe; d Mängi antwortet, er heig en Dämon. Mit de Beschniidig am Sabbat begründet er, dass er en ganze Mänsch am Sabbat gsund gmacht hät, und mahnt, nöd nach em Aaschii z urteile."),
 "TU-JHN-007-025-031": ("Isch er de Christus?", "Es paar Lüüt us Jerusalem wundered sich, dass dä, wo mer wott umbringe, offe redt, und fröged, öb d Obere en als de Christus erchännt heiged; aber vo ihm wüssi mer, wohär er sig, bim Christus wüssi das niemer. De Jesus rüeft im Tämpel, si kännted en und wüssted, wohär er sig; aber dä, wo en gschickt hät, isch wahrhaftig, und dä känned si nöd, er aber kännt en. Mer probiert en z verhafte, aber niemer leit d Hand a en, wil sini Stund no nöd choo isch. Vili us de Mängi glaubed a en."),
 "TU-JHN-007-032-036": ("«Ir wärded mich sueche und nöd finde»", "Wo d Pharisäer s Gmurmel vo de Mängi ghöred, schicked si und d Hoheprieschter Diener, für en z verhafte. De Jesus seit, er sig no es chliises Wiili bi ine und gang dänn zu däm, wo en gschickt hät; si würded en sueche und nöd finde, und wo er sig, chönted si nöd häre choo. D Jude fröged sich, öb er i d Diaspora zu de Grieche well gaa."),
 "TU-JHN-007-037-044": ("Ström vo läbigem Wasser", "Am letschte, grosse Tag vom Fäscht rüeft de Jesus: Wer Durscht hät, söll zu ihm choo und trinke; mit eme Schriftwort redt er vo Ström vo läbigem Wasser, wo us em Innere wärded flüüsse (uf wen sich das bezieht, wird verschide verstande). De Erzäler erklärt, er heig vom Geischt gredt, wo d Gläubige würded übercho; de Geischt isch no nöd da gsii, wil de Jesus no nöd verherrlicht worde isch. I de Mängi halted en di einte für de Prophet, anderi für de Christus; wider anderi wänded ii, nach de Schrift chöm de Christus us Betlehem, nöd us Galiläa. Es git e Spaltig; es paar wänd en verhafte, aber niemer leit d Hand a en."),
 "TU-JHN-007-045-052": ("D Diener chömed zrugg; de Nikodemus", "D Diener chömed ohni de Jesus zu de Hoheprieschter und Pharisäer zrugg: No nie heig en Mänsch eso gredt. D Pharisäer fröged, öb au si sich heiged la verfüere, öb öppe eine vo de Obere oder vo de Pharisäer a en glaubt heig; s Volk, wo s Gsetz nöd känni, sig verfluecht. De Nikodemus, eine vo ine, wändet ii, s Gsetz richti niemer, ohni en zerscht aazlose. Si halted em entgäge, us Galiläa staa kei Prophet uf."),
 "TU-JHN-007-053-053": ("Aafang vom Abschnitt vo de Ehebrächerin", "«Und jede isch i sis Huus gange.» Mit däm Satz faat de Abschnitt vo de Ehebrächerin aa ([[JHN.7.53]]–[[JHN.8.11]]), wo de SBLGNT i Doppelklammere ⟦ ⟧ setzt; d Fortsetzig staat im Kapitel 8. I de Textforschig wird de Abschnitt wiitume als spööteri Iifüegig i s Johannesevangelium beurteilt. I de erfasste CNTR-Transkriptione vo 01, 03, 029, 032, 𝔓66 und 𝔓75 staat da kei Text, uf [[JHN.7.52]] folgt [[JHN.8.12]]; 05 hät de Abschnitt. 02 und 04 sind a dere Stell nöd erhalte. Nach de Forschig staat de Abschnitt i es paar spöötere Handschrifte amene andere Ort (öppe nach [[JHN.21.25]] oder nach [[LUK.21.38]]); das isch im Projekt nöd mit Date prüeft. Vili Chile läsed en als Teil vo de Heilige Schrift; d Frag nach sinere Herkunft isch devo z underscheide."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "Wo Transkription und automatische Zuordnung auseinandergehen ([[JHN.6.40]], [[JHN.7.39]], [[JHN.7.46]]), ist das bei der "
  "Alternative vermerkt."),
 ("Die Grundentscheide für johanneische Schlüsselwörter sind in scripts/authoring/johannes_text_01_03.py begründet und hier "
  "übernommen: ἀμὴν ἀμήν «Amen, amen», ἐγώ εἰμι «Ich bin …» ([[JHN.6.35]], [[JHN.6.48]], [[JHN.6.51]]; ohne Ergänzung in "
  "[[JHN.6.20]] «Ich bin es»), σημεῖον «Zeichen», μένω «bleiben», κόσμος «Welt», λόγος «Wort», δοξάζω «verherrlichen» "
  "([[JHN.7.39]]), ζωὴ αἰώνιος «ewiges Leben». δόξα ist in [[JHN.7.18]] mit «Ehre» wiedergegeben (Begründung in decisions)."),
 ("οἱ Ἰουδαῖοι ist durchgehend wörtlich mit «die Juden» wiedergegeben ([[JHN.6.4]], [[JHN.6.41]], [[JHN.6.52]], [[JHN.7.1]], "
  "[[JHN.7.2]], [[JHN.7.11]], [[JHN.7.13]], [[JHN.7.15]], [[JHN.7.35]]). Das ist eine Deutungsentscheidung: Johannes meint je nach "
  "Stelle das Volk, die Bewohner Judäas oder die führenden Kreise in Jerusalem; auch Jesus, seine Jünger und die Menge sind "
  "Juden ([[JHN.7.13]]). Die Wiedergabe ist nicht als Urteil über das jüdische Volk zu lesen. Alternativen («die Judäer», "
  "«die jüdischen Führer») stehen in decisions."),
 ("[[JHN.7.53]] ist der erste Vers des Abschnitts von der Ehebrecherin ([[JHN.7.53]]–[[JHN.8.11]]), den der SBLGNT in "
  "Doppelklammern ⟦ ⟧ setzt. Er ist übersetzt, weil er im Ausgangstext steht; die öffnende Klammer steht im Text, die "
  "schliessende folgt in [[JHN.8.11]]. In der Textforschung gilt der Abschnitt weithin als spätere Einfügung; das ist ein "
  "verbreitetes Urteil. In den erfassten CNTR-Transkriptionen von 01, 03, 029, 032, 𝔓66 und 𝔓75 steht hier kein Text, 05 "
  "enthält ihn, 02 und 04 sind nicht erhalten. Der SBLGNT-Apparat und die automatische Kollation enthalten für [[JHN.7.53]] "
  "keine Variantenstelle; die Angaben stützen sich auf die Transkriptionen selbst. Viele Kirchen lesen den Abschnitt als "
  "kanonisch."),
 ("Johannes erzählt oft im Präsens («sagt er», «sehen sie»); das ist beibehalten. παραδίδωμι ist durchgehend mit "
  "«ausliefern» wiedergegeben. ὅτι vor direkter Rede ist nicht eigens übersetzt. Die Zeichensetzung folgt dem SBLGNT, "
  "auch in [[JHN.7.37]]–[[JHN.7.38]] (siehe decisions)."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("D Grundentscheid für d Schlüsselwörter vom Johannes sind in scripts/authoring/johannes_text_01_03.py begründet und da "
  "übernoo: «Amen, amen, ich säge eu», «Ich bi …», «Zeiche», «bliibe», «Wält», «Wort», «verherrliche», «ewigs Läbe»."),
 ("οἱ Ἰουδαῖοι isch überall wörtlich «d Jude». Das isch en Entscheid vo de Deutig: De Johannes meint je nach Stell s Volk, "
  "d Lüüt us Judäa oder di füerende Chreis z Jerusalem; au de Jesus und sini Jünger sind Jude. Es isch kei Urteil über s "
  "jüdisch Volk."),
 ("[[JHN.7.53]] isch de erscht Vers vom Abschnitt vo de Ehebrächerin ([[JHN.7.53]]–[[JHN.8.11]]), im SBLGNT i Doppelklammere "
  "⟦ ⟧. Er isch übersetzt, wil er im Text staat; d Klammere zeiged, dass de Abschnitt wiitume als spööteri Iifüegig gilt."),
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
            raise SystemExit(f"Kapitel {c}: Verse ohne Tokens – Behandlung prüfen")
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/johannes_text_06_07.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 6–7 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
