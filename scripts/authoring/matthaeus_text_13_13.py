#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 13 (die Gleichnisrede und die Ablehnung in der Heimat) – Texteinheiten, Arbeitsübersetzungen
(Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_13_13.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 13 fehlt im SBLGNT kein Vers (per Skript geprüft); alle 58 Verse haben Tokens.
- Jesu Rede im Haus läuft ohne neue Redeeinleitung von [[MAT.13.37]] bis zur Frage in [[MAT.13.51]]; in [[MAT.13.30]]
  stehen drei Ebenen von Anführungszeichen (« ‹ « » › »).
- [[MAT.13.35]]: Nach der CNTR-Transkription las die Erstschrift von 01 «durch den Propheten Jesaja»; der SBLGNT-Apparat
  verzeichnet die Stelle nicht, deshalb steht der Befund in decisions und translation_notes, nicht als Alternative.
- [[MAT.13.45]]: Die automatische Zuordnung führt 032 und 04 bei der Lesart ohne ἀνθρώπῳ; nach den CNTR-Transkriptionen
  steht dort die Abkürzung ανω. Die Übersetzung («einem Kaufmann») ändert sich nicht; der Befund steht in decisions.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1,
WREAD-CNTR-MAT-013-001-058) bzw. aus den CNTR-Transkriptionen (Sekundärtranskription), nicht aus eigener Prüfung der
Handschriften. Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts (data/annotations) ermittelt.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, write  # noqa: E402

DATE = "2026-10-18"
AUTH = "KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-MATTHEW"]
CHAPTERS = ((13, 58),)

DE = {
 # ------------------------------------------------------------ Kapitel 13
 "MAT.13.1": "[An]{1} [jenem]{4} [Tag]{2,3} [ging]{5} [Jesus]{6,7} [aus dem]{8} [Haus]{9} [hinaus]{5} und [sass]{10} [am]{11,12} [See]{13}.",
 "MAT.13.2": "Und{1} [es versammelten sich]{2} [grosse]{6} [Menschenmengen]{5} [bei]{3} [ihm]{4}, [sodass]{7} [er]{8} [in]{9} [ein Boot]{10} [stieg]{11} und [sich setzte]{12}; und{13} [die ganze]{14,15} [Menge]{16} [stand]{20} [am]{17,18} [Ufer]{19}.",
 "MAT.13.3": "Und{1} [er redete]{2} [zu ihnen]{3} [vieles]{4} [in]{5} [Gleichnissen]{6} und [sagte]{7}: «[Siehe]{8}, [der Sämann]{10,11} [ging hinaus]{9}, [um]{12} [zu säen]{13}.",
 "MAT.13.4": "Und{1} [während]{2,3} [er]{5} [säte]{4}, [fiel]{8} [einiges]{6} [an]{9} [den]{10} [Weg]{11}, und{12} [die Vögel]{14,15} [kamen]{13} und [frassen]{16} [es]{17} [auf]{16}. ~7(μέν kündigt die folgende Aufzählung an «einiges … anderes»; nicht eigens wiedergegeben)",
 "MAT.13.5": "[Anderes]{1} [aber]{2} [fiel]{3} [auf]{4} [den]{5} [felsigen Boden]{6}, [wo]{7} [es]{9} [nicht]{8} [viel]{11} [Erde]{10} [hatte]{9}, und{12} [es ging]{14} [sogleich]{13} [auf]{14}, [weil]{15,16} [es]{18} [keine]{17} [tiefe]{19} [Erde]{20} [hatte]{18}.",
 "MAT.13.6": "[Als]{3} [aber]{2} [die Sonne]{1} [aufging]{3}, [wurde es versengt]{4}, und{5} [weil]{6,7} [es]{9} [keine]{8} [Wurzel]{10} [hatte]{9}, [verdorrte es]{11}.",
 "MAT.13.7": "[Anderes]{1} [aber]{2} [fiel]{3} [unter]{4} [die]{5} [Dornen]{6}, und{7} [die Dornen]{9,10} [wuchsen hoch]{8} und{11} [erstickten]{12} [es]{13}.",
 "MAT.13.8": "[Anderes]{1} [aber]{2} [fiel]{3} [auf]{4} [die]{5} [gute]{7,8} [Erde]{6} und{9} [brachte]{10} [Frucht]{11}: [teils]{12,13} [hundertfach]{14}, [teils]{15,16} [sechzigfach]{17}, [teils]{18,19} [dreissigfach]{20}.",
 "MAT.13.9": "[Wer]{1} [Ohren]{3} [hat]{2}, [der höre]{4}!»",
 "MAT.13.10": "Und{1} [die Jünger]{3,4} [traten herzu]{2} und [sagten]{5} [zu ihm]{6}: «[Warum]{7,8} [redest du]{11} [in]{9} [Gleichnissen]{10} [zu ihnen]{12}?»",
 "MAT.13.11": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4} [zu ihnen]{5}: «[Euch]{7} [ist es gegeben]{8}, [die Geheimnisse]{10,11} [des Reiches der Himmel]{12-15} [zu erkennen]{9}, [jenen]{16} [aber]{17} [ist es]{19} [nicht]{18} [gegeben]{19}. ~6(ὅτι leitet die direkte Rede ein)",
 "MAT.13.12": "[Denn]{2} [wer]{1} [hat]{3}, [dem]{5} [wird gegeben werden]{4}, und{6} [er wird Überfluss haben]{7}; [wer]{8} [aber]{9} [nicht]{10} [hat]{11}, [von dem]{16,17} [wird]{15} [auch]{12} [das, was]{13} [er hat]{14}, [weggenommen werden]{15}.",
 "MAT.13.13": "[Darum]{1,2} [rede ich]{6} [in]{3} [Gleichnissen]{4} [zu ihnen]{5}, [weil]{7} [sie]{10} [sehend]{8} [nicht]{9} [sehen]{10} und{11} [hörend]{12} [nicht]{13} [hören]{14} [und nicht]{15} [verstehen]{16}.",
 "MAT.13.14": "Und{1} [an ihnen]{3} [erfüllt sich]{2} [die Prophetie]{4,5} [des Jesaja]{6}, [die]{7} [sagt]{8}: ‹[Mit dem Gehör]{9} [werdet ihr hören]{10} und{11} [gewiss nicht]{12,13} [verstehen]{14}, und{15} [sehend]{16} [werdet ihr sehen]{17} und{18} [gewiss nicht]{19,20} [erkennen]{21}.",
 "MAT.13.15": "[Denn]{2} [das Herz]{3,4} [dieses]{7} [Volkes]{5,6} [ist abgestumpft]{1}, und{8} [mit den]{9} [Ohren]{10} [haben sie]{12} [schwer]{11} [gehört]{12}, und{13} [ihre]{16} [Augen]{14,15} [haben sie geschlossen]{17}, [damit sie nicht etwa]{18} [mit den]{20} [Augen]{21} [sehen]{19} und{22} [mit den]{23} [Ohren]{24} [hören]{25} und{26} [mit dem]{27} [Herzen]{28} [verstehen]{29} und{30} [umkehren]{31} und{32} [ich]{33} [sie]{34} [heilen werde]{33}.›",
 "MAT.13.16": "[Selig]{3} [aber]{2} sind [eure]{1} [Augen]{4,5}, [weil]{6} [sie sehen]{7}, und{8} [eure]{11} [Ohren]{9,10}, [weil]{12} [sie hören]{13}.",
 "MAT.13.17": "[Amen]{1}, [ich sage]{3} [euch]{4}: [Viele]{6} [Propheten]{7} und{8} [Gerechte]{9} [haben sich danach gesehnt]{10}, [zu sehen]{11}, [was]{12} [ihr seht]{13}, und{14} [haben es]{16} [nicht]{15} [gesehen]{16}, und{17} [zu hören]{18}, [was]{19} [ihr hört]{20}, und{21} [haben es]{23} [nicht]{22} [gehört]{23}. ~2(γάρ «denn» verbindet locker mit dem Vorigen; nicht eigens wiedergegeben) ~5(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.13.18": "[Ihr]{1} [also]{2}, [hört]{3} [das Gleichnis]{4,5} [vom Sämann]{6,7}!",
 "MAT.13.19": "[Bei jedem]{1}, der [das Wort]{3,4} [vom Reich]{5,6} [hört]{2} und{7} [nicht]{8} [versteht]{9}, [kommt]{10} [der Böse]{11,12} und{13} [raubt]{14}, [was]{15} [in]{17} [seinem]{20} [Herzen]{18,19} [gesät ist]{16}; [das]{21} [ist]{22} [der]{23}, der [an]{24} [den]{25} [Weg]{26} [gesät wurde]{27}.",
 "MAT.13.20": "[Der]{1} [aber]{2}, der [auf]{3} [den]{4} [felsigen Boden]{5} [gesät wurde]{6}, [das]{7} [ist]{8} [der]{9}, der [das Wort]{10,11} [hört]{12} und{13} [es]{18} [sogleich]{14} [mit]{15} [Freude]{16} [aufnimmt]{17};",
 "MAT.13.21": "[er hat]{2} [aber]{3} [keine]{1} [Wurzel]{4} [in]{5} [sich]{6}, [sondern]{7} [ist]{9} [unbeständig]{8}; [wenn]{10} [aber]{11} [Bedrängnis]{12} [oder]{13} [Verfolgung]{14} [kommt]{10} [um]{15} [des Wortes]{16,17} [willen]{15}, [kommt er]{19} [sogleich]{18} [zu Fall]{19}.",
 "MAT.13.22": "[Der]{1} [aber]{2}, der [unter]{3} [die]{4} [Dornen]{5} [gesät wurde]{6}, [das]{7} [ist]{8} [der]{9}, der [das Wort]{10,11} [hört]{12}, und{13} [die Sorge]{14,15} [dieser]{18} [Weltzeit]{16,17} und{19} [die Verführung]{20,21} [des Reichtums]{22,23} [ersticken]{24} [das Wort]{25,26}, und{27} [es wird]{29} [fruchtlos]{28}.",
 "MAT.13.23": "[Der]{1} [aber]{2}, der [auf]{3} [die]{4} [gute]{5} [Erde]{6} [gesät wurde]{7}, [das]{8} [ist]{9} [der]{10}, der [das Wort]{11,12} [hört]{13} und{14} [versteht]{15}; [der]{16} [bringt]{18} [dann auch]{17} [Frucht]{18} und{19} [trägt]{20}: [teils]{21,22} [hundertfach]{23}, [teils]{24,25} [sechzigfach]{26}, [teils]{27,28} [dreissigfach]{29}.»",
 "MAT.13.24": "[Ein anderes]{1} [Gleichnis]{2} [legte er]{3} [ihnen]{4} [vor]{3} und [sagte]{5}: «[Das Reich der Himmel]{7-10} [gleicht]{6} [einem Menschen]{11}, [der]{12} [guten]{13} [Samen]{14} [auf]{15} [sein]{18} [Feld]{16,17} [säte]{12}.",
 "MAT.13.25": "[Während]{1,3} [aber]{2} [die Leute]{5,6} [schliefen]{4}, [kam]{7} [sein]{8} [Feind]{9,10} und{11} [säte]{12} [Unkraut]{13} [mitten unter]{14,15} [den Weizen]{16,17} und{18} [ging weg]{19}.",
 "MAT.13.26": "[Als]{1} [aber]{2} [die Saat]{4,5} [aufging]{3} und{6} [Frucht]{7} [ansetzte]{8}, [da]{9} [zeigte sich]{10} [auch]{11} [das Unkraut]{12,13}.",
 "MAT.13.27": "[Die Knechte]{3,4} [des Hausherrn]{5,6} [aber]{2} [traten herzu]{1} und [sagten]{7} [zu ihm]{8}: ‹[Herr]{9}, [hast du]{13} [nicht]{10} [guten]{11} [Samen]{12} [auf]{14} [dein]{16} [Feld]{15,17} [gesät]{13}? [Woher]{18} [hat es]{20} [denn]{19} [Unkraut]{21}?›",
 "MAT.13.28": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: ‹[Das]{7} [hat]{8} [ein Feind]{5,6} [getan]{8}.› [Die Knechte]{9,11} [aber]{10} [sagen]{13} [zu ihm]{12}: ‹[Willst du]{14} [also]{15}, [dass wir]{17} [hingehen]{16} und [es]{18} [einsammeln]{17}?›",
 "MAT.13.29": "[Er]{1} [aber]{2} [sagt]{3}: ‹[Nein]{4}, [damit ihr nicht etwa]{5} [beim Einsammeln]{6} [des Unkrauts]{7,8} [zusammen mit]{10} [ihm]{11} [den Weizen]{12,13} [ausreisst]{9}.",
 "MAT.13.30": "[Lasst]{1} [beides]{3} [miteinander wachsen]{2} [bis]{4} [zur]{5} [Ernte]{6}; und{7} [zur]{8} [Zeit]{9} [der]{10} [Ernte]{11} [werde ich]{12} [den Schnittern]{13,14} [sagen]{12}: «[Sammelt]{15} [zuerst]{16} [das Unkraut]{17,18} [ein]{15} und{19} [bindet]{20} [es]{21} [in]{22} [Bündel]{23}, [um]{24,25} [es]{27} [zu verbrennen]{26}; [den Weizen]{28,30} [aber]{29} [bringt]{31} [in]{32} [meine]{35} [Scheune]{33,34}!»›»",
 "MAT.13.31": "[Ein anderes]{1} [Gleichnis]{2} [legte er]{3} [ihnen]{4} [vor]{3} und [sagte]{5}: «[Das Reich der Himmel]{8-11} [gleicht]{6,7} [einem Senfkorn]{12,13}, [das]{14} [ein Mensch]{16} [nahm]{15} und [auf]{18} [sein]{21} [Feld]{19,20} [säte]{17}.",
 "MAT.13.32": "[Es]{1} [ist]{4} [zwar]{3} [kleiner]{2} [als alle]{5} [Samen]{6,7}; [wenn es]{8} [aber]{9} [gewachsen ist]{10}, [ist es]{14} [grösser]{11} [als die]{12} [Gartenkräuter]{13} und{15} [wird]{16} [ein Baum]{17}, [sodass]{18} [die Vögel]{20,21} [des Himmels]{22,23} [kommen]{19} und{24} [in]{26} [seinen]{29} [Zweigen]{27,28} [nisten]{25}.»",
 "MAT.13.33": "[Ein anderes]{1} [Gleichnis]{2} [redete er]{3} [zu ihnen]{4}: «[Das Reich der Himmel]{7-10} [gleicht]{5,6} [dem Sauerteig]{11}, [den]{12} [eine Frau]{14} [nahm]{13} und [in]{16} [drei]{19} [Mass]{18} [Mehl]{17} [verbarg]{15}, [bis]{20,21} [das Ganze]{23} [durchsäuert war]{22}.»",
 "MAT.13.34": "[Das]{1} [alles]{2} [redete]{3} [Jesus]{4,5} [in]{6} [Gleichnissen]{7} [zu den]{8} [Menschenmengen]{9}, und{10} [ohne]{11} [Gleichnis]{12} [redete er]{14} [nichts]{13} [zu ihnen]{15},",
 "MAT.13.35": "[damit]{1} [erfüllt würde]{2}, [was]{3} [durch]{5} [den Propheten]{6,7} [gesagt ist]{4}: ‹[Ich will]{9} [meinen]{14} [Mund]{12,13} [in]{10} [Gleichnissen]{11} [auftun]{9}, [ich will aussprechen]{15}, [was verborgen ist]{16} [seit]{17} [der Grundlegung]{18}.› ~8(λέγοντος «der sagt» leitet das Zitat ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.13.36": "[Da]{1} [entliess er]{2} [die Menschenmengen]{3,4} und [ging]{5} [ins]{6,7} [Haus]{8}. Und{9} [seine]{14} [Jünger]{12,13} [traten]{10} [zu ihm]{11} und [sagten]{15}: «[Erkläre]{16} [uns]{17} [das Gleichnis]{18,19} [vom Unkraut]{20,21} [auf dem Feld]{22,23}!»",
 "MAT.13.37": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: «[Der]{5}, der [den guten]{7,8} [Samen]{9} [sät]{6}, [ist]{10} [der Menschensohn]{11-14};",
 "MAT.13.38": "[das Feld]{1,3} [aber]{2} [ist]{4} [die Welt]{5,6}; [der gute]{7,9} [Samen]{10} [aber]{8}, [das]{11} [sind]{12} [die Söhne]{13,14} [des Reiches]{15,16}; [das Unkraut]{17,19} [aber]{18} [sind]{20} [die Söhne]{21,22} [des Bösen]{23,24};",
 "MAT.13.39": "[der Feind]{1,3} [aber]{2}, [der]{4} [es]{6} [gesät hat]{5}, [ist]{7} [der Teufel]{8,9}; [die Ernte]{10,12} [aber]{11} [ist]{15} [die Vollendung]{13} [der Weltzeit]{14}; [die Schnitter]{16,18} [aber]{17} [sind]{20} [Engel]{19}.",
 "MAT.13.40": "[Wie]{1} [nun]{2} [das Unkraut]{4,5} [eingesammelt]{3} und{6} [im Feuer]{7} [verbrannt wird]{8}, [so]{9} [wird es sein]{10} [bei]{11} [der Vollendung]{12,13} [der Weltzeit]{14,15}:",
 "MAT.13.41": "[Der Menschensohn]{2-5} [wird]{1} [seine]{8} [Engel]{6,7} [aussenden]{1}, und{9} [sie werden]{10} [aus]{11} [seinem]{14} [Reich]{12,13} [alles]{15,16} [einsammeln]{10}, [was zu Fall bringt]{17}, und{18} [die]{19}, die [Gesetzlosigkeit]{21,22} [tun]{20},",
 "MAT.13.42": "und{1} [sie werden]{2} [sie]{3} [in]{4} [den]{5} [Feuerofen]{6-8} [werfen]{2}; [dort]{9} [wird]{10} [das Weinen]{11,12} und{13} [das Zähneknirschen]{14-17} [sein]{10}.",
 "MAT.13.43": "[Dann]{1} [werden]{4} [die Gerechten]{2,3} [leuchten]{4} [wie]{5} [die Sonne]{6,7} [im]{8,9} [Reich]{10} [ihres]{13} [Vaters]{11,12}. [Wer]{14} [Ohren]{16} [hat]{15}, [der höre]{17}!",
 "MAT.13.44": "[Das Reich der Himmel]{3-6} [gleicht]{1,2} [einem Schatz]{7}, der [im]{9,10} [Feld]{11} [verborgen ist]{8}. [Ein Mensch]{14} [fand]{13} [ihn]{12} und [verbarg]{15} ihn, und{16} [in]{17} [seiner]{20} [Freude]{18,19} [geht er hin]{21} und{22} [verkauft]{23} [alles]{24}, [was]{25} [er hat]{26}, und{27} [kauft]{28} [jenes]{31} [Feld]{29,30}.",
 "MAT.13.45": "[Wiederum]{1} [gleicht]{2,3} [das Reich der Himmel]{4-7} [einem Kaufmann]{8,9}, der [schöne]{11} [Perlen]{12} [sucht]{10}.",
 "MAT.13.46": "[Als er]{1} [aber]{2} [eine]{3} [kostbare]{4} [Perle]{5} [fand]{1}, [ging er hin]{6}, [verkaufte]{7} [alles]{8}, [was]{9} [er hatte]{10}, und{11} [kaufte]{12} [sie]{13}.",
 "MAT.13.47": "[Wiederum]{1} [gleicht]{2,3} [das Reich der Himmel]{4-7} [einem Schleppnetz]{8}, das [in]{10} [den]{11} [See]{12} [geworfen wurde]{9} und{13} Fische [aller]{14,15} [Art]{16} [einfing]{17}.",
 "MAT.13.48": "[Als]{2} [es]{1} [voll war]{3}, [zogen sie es]{4} [ans]{5,6} [Ufer]{7}, und{8} [sie setzten sich]{9} und [lasen]{10} [die guten]{11,12} [in]{13} [Gefässe]{14} [zusammen]{10}; [die unbrauchbaren]{15,17} [aber]{16} [warfen sie hinaus]{18,19}.",
 "MAT.13.49": "[So]{1} [wird es sein]{2} [bei]{3} [der Vollendung]{4,5} [der Weltzeit]{6,7}: [Die Engel]{9,10} [werden ausziehen]{8} und{11} [die Bösen]{13,14} [aus]{15} [der Mitte]{16} [der Gerechten]{17,18} [aussondern]{12},",
 "MAT.13.50": "und{1} [sie werden]{2} [sie]{3} [in]{4} [den]{5} [Feuerofen]{6-8} [werfen]{2}; [dort]{9} [wird]{10} [das Weinen]{11,12} und{13} [das Zähneknirschen]{14-17} [sein]{10}.",
 "MAT.13.51": "[Habt ihr]{1} [das]{2} [alles]{3} [verstanden]{1}?» [Sie sagen]{4} [zu ihm]{5}: «[Ja]{6}.»",
 "MAT.13.52": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: «[Darum]{5,6} [gleicht]{14,15} [jeder]{7} [Schriftgelehrte]{8}, der [für]{10} [das Reich der Himmel]{11-13} [zum Jünger geworden ist]{9}, [einem Hausherrn]{16,17}, [der]{18} [aus]{20} [seinem]{23} [Schatz]{21,22} [Neues]{24} und{25} [Altes]{26} [hervorholt]{19}.»",
 "MAT.13.53": "Und{1} [es geschah]{2}, [als]{3} [Jesus]{5,6} [diese]{9} [Gleichnisse]{7,8} [beendet hatte]{4}, [zog er]{10} [von dort]{11} [weg]{10}.",
 "MAT.13.54": "Und{1} [er kam]{2} [in]{3} [seine]{6} [Heimat]{4,5} und [lehrte]{7} [sie]{8} [in]{9} [ihrer]{12} [Synagoge]{10,11}, [sodass]{13} [sie]{15} [staunten]{14} und{16} [sagten]{17}: «[Woher]{18} [hat dieser]{19} [diese]{22} [Weisheit]{20,21} und{23} [die Machttaten]{24,25}?",
 "MAT.13.55": "[Ist]{3} [dieser]{2} [nicht]{1} [der]{4} [Sohn]{7} [des Zimmermanns]{5,6}? [Heisst]{12} [nicht]{8} [seine]{11} [Mutter]{9,10} [Maria]{13}, und{14} [seine]{17} [Brüder]{15,16} [Jakobus]{18} und{19} [Josef]{20} und{21} [Simon]{22} und{23} [Judas]{24}?",
 "MAT.13.56": "Und{1} [sind]{9} [nicht]{5} [seine]{4} [Schwestern]{2,3} [alle]{6} [bei]{7} [uns]{8}? [Woher]{10} [hat dieser]{12} [also]{11} [das]{13} [alles]{14}?»",
 "MAT.13.57": "Und{1} [sie nahmen Anstoss]{2} [an]{3} [ihm]{4}. [Jesus]{5,7} [aber]{6} [sagte]{8} [zu ihnen]{9}: «[Ein Prophet]{12} [ist]{11} [nicht]{10} [ohne Ehre]{13}, [ausser]{14,15} [in]{16} [der]{17} [Heimat]{18} und{19} [in]{20} [seinem]{23} [Haus]{21,22}.»",
 "MAT.13.58": "Und{1} [er tat]{3} [dort]{4} [nicht]{2} [viele]{6} [Machttaten]{5} [wegen]{7} [ihres]{10} [Unglaubens]{8,9}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 13
 "MAT.13.1": "[A]{1} [dem]{2,4} [Tag]{3} [isch]{5} [de Jesus]{6,7} [us em]{8} [Huus]{9} [usegange]{5} und [isch]{10} [am]{11,12} [See]{13} [gsässe]{10}.",
 "MAT.13.2": "Und{1} [es sind]{2} [vil]{6} [Lüüt]{5} [bi]{3} [ihm]{4} [zämechoo]{2}, [so dass]{7} [er]{8} [i]{9} [es Boot]{10} [gstige]{11} und [abgsässe isch]{12}; und{13} [di ganz]{14,15} [Mängi]{16} [isch]{20} [am]{17,18} [Ufer]{19} [gstande]{20}.",
 "MAT.13.3": "Und{1} [er hät]{2} [vil]{4} [i]{5} [Gliichnis]{6} [zu ine]{3} [gredt]{2} und [gseit]{7}: «[Lueg]{8}, [de Sämaa]{10,11} [isch usegange]{9}, [go]{12} [sääje]{13}.",
 "MAT.13.4": "Und{1} [won]{2,3} [er]{5} [gsäät hät]{4}, [isch]{8} [öppis]{6} [a de]{9,10} [Wäg]{11} [gheit]{8}, und{12} [d Vögel]{14,15} [sind choo]{13} und [händ]{16} [s]{17} [ufgfrässe]{16}. ~7(μέν chündet d Ufzellig aa «öppis … anders»; nöd eigens widerggää)",
 "MAT.13.5": "[Anders]{1} [aber]{2} [isch]{3} [uf]{4} [de]{5} [Felsbode]{6} [gheit]{3}, [wo]{7} [s]{9} [nöd]{8} [vil]{11} [Ärde]{10} [gha hät]{9}, und{12} [es isch]{14} [grad]{13} [ufgange]{14}, [wil]{15,16} [s]{18} [kei]{17} [tüüfi]{19} [Ärde]{20} [gha hät]{18}.",
 "MAT.13.6": "[Wo]{3} [aber]{2} [d Sunne]{1} [ufgange isch]{3}, [isch es verbrännt]{4}, und{5} [wil]{6,7} [s]{9} [kei]{8} [Wurzle]{10} [gha hät]{9}, [isch es verdorret]{11}.",
 "MAT.13.7": "[Anders]{1} [aber]{2} [isch]{3} [i]{4} [d]{5} [Dörn]{6} [gheit]{3}, und{7} [d Dörn]{9,10} [sind ufgschosse]{8} und{11} [händ]{12} [s]{13} [verstickt]{12}.",
 "MAT.13.8": "[Anders]{1} [aber]{2} [isch]{3} [uf]{4} [di]{5} [guet]{7,8} [Ärde]{6} [gheit]{3}, und{9} [es hät]{10} [Frucht]{11} [bracht]{10}: [teils]{12,13} [hundertfach]{14}, [teils]{15,16} [sächzgfach]{17}, [teils]{18,19} [drüssgfach]{20}.",
 "MAT.13.9": "[Wer]{1} [Ohre]{3} [hät]{2}, [dä söll lose]{4}!»",
 "MAT.13.10": "Und{1} [d Jünger]{3,4} [sind härechoo]{2} und [händ]{5} [zu ihm]{6} [gseit]{5}: «[Werum]{7,8} [redsch]{11} [i]{9} [Gliichnis]{10} [zu ine]{12}?»",
 "MAT.13.11": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [zu ine]{5} [gseit]{4}: «[Eu]{7} [isch es ggää]{8}, [d Gheimnis]{10,11} [vom Riich vo de Himel]{12-15} [z erchänne]{9}, [dene]{16} [aber]{17} [isch es]{19} [nöd]{18} [ggää]{19}. ~6(ὅτι leitet di diräkt Red ii)",
 "MAT.13.12": "[Dänn]{2} [wer]{1} [hät]{3}, [däm]{5} [wird ggää]{4}, und{6} [er wird meh als gnueg ha]{7}; [wer]{8} [aber]{9} [nöd]{10} [hät]{11}, [vo däm]{16,17} [wird]{15} [sogar]{12} [das, won]{13} [er hät]{14}, [wäggnoo]{15}.",
 "MAT.13.13": "[Drum]{1,2} [red ich]{6} [i]{3} [Gliichnis]{4} [zu ine]{5}, [wil]{7} [si]{10} [mit offne Auge]{8} [nöd]{9} [gsehnd]{10} und{11} [mit offne Ohre]{12} [nöd]{13} [ghöred]{14} [und nöd]{15} [verstönd]{16}.",
 "MAT.13.14": "Und{1} [a ine]{3} [erfüllt sich]{2} [d Prophezeiig]{4,5} [vom Jesaja]{6}, [wo]{7} [seit]{8}: ‹[Mit de Ohre]{9} [wärded ir ghööre]{10} und{11} [ganz sicher nöd]{12,13} [verstaa]{14}, und{15} [mit offne Auge]{16} [wärded ir luege]{17} und{18} [ganz sicher nöd]{19,20} [gseh]{21}.",
 "MAT.13.15": "[Dänn]{2} [s Härz]{3,4} [vo]{5} [däm]{7} [Volk]{6} [isch abgstumpft]{1}, und{8} [mit de]{9} [Ohre]{10} [händ si]{12} [schwer]{11} [ghört]{12}, und{13} [iri]{16} [Auge]{14,15} [händ si zuegmacht]{17}, [damit si nöd öppe]{18} [mit de]{20} [Auge]{21} [gsehnd]{19} und{22} [mit de]{23} [Ohre]{24} [ghöred]{25} und{26} [mit em]{27} [Härz]{28} [verstönd]{29} und{30} [umchered]{31} und{32} [ich]{33} [si]{34} [heile]{33}.›",
 "MAT.13.16": "[Sälig]{3} [aber]{2} sind [eui]{1} [Auge]{4,5}, [wil]{6} [si gsehnd]{7}, und{8} [eui]{11} [Ohre]{9,10}, [wil]{12} [si ghöred]{13}.",
 "MAT.13.17": "[Amen]{1}, [ich säg]{3} [eu]{4}: [Vil]{6} [Prophete]{7} und{8} [Grächti]{9} [händ sich danaa gsehnt]{10}, [z gseh]{11}, [was]{12} [ir gsehnd]{13}, und{14} [händ s]{16} [nöd]{15} [gseh]{16}, und{17} [z ghööre]{18}, [was]{19} [ir ghöred]{20}, und{21} [händ s]{23} [nöd]{22} [ghört]{23}. ~2(γάρ «dänn» verbindet locker mit em Vorige; nöd eigens widerggää) ~5(ὅτι leitet d Ussag ii; mit em Doppelpunkt widerggää)",
 "MAT.13.18": "[Ir]{1} [also]{2}, [losed]{3} uf [s Gliichnis]{4,5} [vom Sämaa]{6,7}!",
 "MAT.13.19": "[Bi jedem]{1}, wo [s Wort]{3,4} [vom Riich]{5,6} [ghört]{2} und{7} [nöd]{8} [verstaat]{9}, [chunnt]{10} [de Böös]{11,12} und{13} [riisst]{14} [wäg]{14}, [was]{15} [i]{17} [sim]{20} [Härz]{18,19} [gsäät isch]{16}; [das]{21} [isch]{22} [dä]{23}, wo [a de]{24,25} [Wäg]{26} [gsäät worde isch]{27}.",
 "MAT.13.20": "[Dä]{1} [aber]{2}, wo [uf]{3} [de]{4} [Felsbode]{5} [gsäät worde isch]{6}, [das]{7} [isch]{8} [dä]{9}, wo [s Wort]{10,11} [ghört]{12} und{13} [s]{18} [grad]{14} [mit]{15} [Fröid]{16} [aanimmt]{17};",
 "MAT.13.21": "[er hät]{2} [aber]{3} [kei]{1} [Wurzle]{4} [i]{5} [sich]{6}, [sondern]{7} [isch]{9} [unbständig]{8}; [wänn]{10} [aber]{11} [Not]{12} [oder]{13} [Verfolgig]{14} [chunnt]{10} [wäge]{15} [em Wort]{16,17}, [chunnt er]{19} [grad]{18} [z Fall]{19}.",
 "MAT.13.22": "[Dä]{1} [aber]{2}, wo [i]{3} [d]{4} [Dörn]{5} [gsäät worde isch]{6}, [das]{7} [isch]{8} [dä]{9}, wo [s Wort]{10,11} [ghört]{12}, und{13} [d Sorg]{14,15} [vo dere]{16,18} [Wältziit]{17} und{19} [d Verfüerig]{20,21} [vom Riichtum]{22,23} [verstickted]{24} [s Wort]{25,26}, und{27} [es wird]{29} [unfruchtbar]{28}.",
 "MAT.13.23": "[Dä]{1} [aber]{2}, wo [uf]{3} [di]{4} [guet]{5} [Ärde]{6} [gsäät worde isch]{7}, [das]{8} [isch]{9} [dä]{10}, wo [s Wort]{11,12} [ghört]{13} und{14} [verstaat]{15}; [dä]{16} [bringt]{18} [äbe]{17} [Frucht]{18} und{19} [treit]{20}: [teils]{21,22} [hundertfach]{23}, [teils]{24,25} [sächzgfach]{26}, [teils]{27,28} [drüssgfach]{29}.»",
 "MAT.13.24": "[Es anders]{1} [Gliichnis]{2} [hät er]{3} [ine]{4} [vorgleit]{3} und [gseit]{5}: «[S Riich vo de Himel]{7-10} [isch wie]{6} [en Mänsch]{11}, [wo]{12} [guete]{13} [Same]{14} [uf]{15} [sis]{18} [Fäld]{16,17} [gsäät hät]{12}.",
 "MAT.13.25": "[Während]{1,3} [aber]{2} [d Lüüt]{5,6} [gschlafe händ]{4}, [isch]{7} [sin]{8} [Feind]{9,10} [choo]{7} und{11} [hät]{12} [Uchruut]{13} [mitten under]{14,15} [de Weize]{16,17} [gsäät]{12} und{18} [isch furtgange]{19}.",
 "MAT.13.26": "[Wo]{1} [aber]{2} [d Saat]{4,5} [ufgange isch]{3} und{6} [Frucht]{7} [aagsetzt hät]{8}, [dänn]{9} [isch]{10} [au]{11} [s Uchruut]{12,13} [füürechoo]{10}.",
 "MAT.13.27": "[D Chnächt]{3,4} [vom Huusherr]{5,6} [aber]{2} [sind härechoo]{1} und [händ]{7} [zu ihm]{8} [gseit]{7}: ‹[Herr]{9}, [häsch]{13} [nöd]{10} [guete]{11} [Same]{12} [uf]{14} [dis]{16} [Fäld]{15,17} [gsäät]{13}? [Vo wo]{18} [hät s]{20} [dänn]{19} [Uchruut]{21}?›",
 "MAT.13.28": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: ‹[Das]{7} [hät]{8} [en Feind]{5,6} [gmacht]{8}.› [D Chnächt]{9,11} [aber]{10} [säged]{13} [zu ihm]{12}: ‹[Wottsch]{14} [also]{15}, [dass mer]{17} [gönd]{16} und [s]{18} [zämeläsed]{17}?›",
 "MAT.13.29": "[Er]{1} [aber]{2} [seit]{3}: ‹[Nei]{4}, [suscht]{5} [riissed ir]{9} [bim Zämeläse]{6} [vom Uchruut]{7,8} [zäme mit]{10} [ihm]{11} [de Weize]{12,13} [us]{9}.",
 "MAT.13.30": "[Lönd]{1} [beides]{3} [mitenand wachse]{2} [bis]{4} [zur]{5} [Ärn]{6}; und{7} [zur]{8} [Ziit]{9} [vo de]{10} [Ärn]{11} [wird ich]{12} [de Schnitter]{13,14} [säge]{12}: «[Läsed]{15} [zerscht]{16} [s Uchruut]{17,18} [zäme]{15} und{19} [binded]{20} [s]{21} [i]{22} [Büschel]{23}, [für]{24,25} [s]{27} [z verbränne]{26}; [de Weize]{28,30} [aber]{29} [bringed]{31} [i]{32} [mini]{35} [Schüür]{33,34}!»›»",
 "MAT.13.31": "[Es anders]{1} [Gliichnis]{2} [hät er]{3} [ine]{4} [vorgleit]{3} und [gseit]{5}: «[S Riich vo de Himel]{8-11} [isch wie]{6,7} [es Sänfchorn]{12,13}, [wo]{14} [en Mänsch]{16} [gnoo]{15} und [uf]{18} [sis]{21} [Fäld]{19,20} [gsäät hät]{17}.",
 "MAT.13.32": "[Es]{1} [isch]{4} [zwar]{3} [chliiner]{2} [als alli]{5} [Same]{6,7}; [wänn s]{8} [aber]{9} [gwachse isch]{10}, [isch es]{14} [grösser]{11} [als d]{12} [Gartechrüüter]{13} und{15} [wird]{16} [en Baum]{17}, [so dass]{18} [d Vögel]{20,21} [vom Himel]{22,23} [chömed]{19} und{24} [i]{26} [sine]{29} [Äscht]{27,28} [nischted]{25}.»",
 "MAT.13.33": "[Es anders]{1} [Gliichnis]{2} [hät er]{3} [ine]{4} [verzellt]{3}: «[S Riich vo de Himel]{7-10} [isch wie]{5,6} [Suurteig]{11}, [wo]{12} [e Frau]{14} [gnoo]{13} und [i]{16} [drüü]{19} [Mass]{18} [Mehl]{17} [versteckt hät]{15}, [bis]{20,21} [alles]{23} [durgsüüret gsii isch]{22}.»",
 "MAT.13.34": "[Das]{1} [alles]{2} [hät]{3} [de Jesus]{4,5} [i]{6} [Gliichnis]{7} [zu de]{8} [Lüüt]{9} [gredt]{3}, und{10} [ohni]{11} [Gliichnis]{12} [hät er]{14} [nüüt]{13} [zu ine]{15} [gredt]{14},",
 "MAT.13.35": "[damit]{1} [erfüllt wird]{2}, [was]{3} [dur]{5} [de Prophet]{6,7} [gseit worden isch]{4}: ‹[Ich will]{9} [mis]{14} [Muul]{12,13} [i]{10} [Gliichnis]{11} [uftue]{9}, [ich will usspräche]{15}, [was verborge isch]{16} [sit]{17} [de Grundlegig]{18}.› ~8(λέγοντος «wo seit» leitet s Zitat ii; mit em Doppelpunkt widerggää)",
 "MAT.13.36": "[Dänn]{1} [hät er]{2} [d Lüüt]{3,4} [la gaa]{2} und [isch]{5} [is]{6,7} [Huus]{8} [gange]{5}. Und{9} [sini]{14} [Jünger]{12,13} [sind]{10} [zu ihm]{11} [choo]{10} und [händ gseit]{15}: «[Erklär]{16} [üs]{17} [s Gliichnis]{18,19} [vom Uchruut]{20,21} [uf em Fäld]{22,23}!»",
 "MAT.13.37": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: «[Dä]{5}, wo [de guet]{7,8} [Same]{9} [sääit]{6}, [isch]{10} [de Mänschesohn]{11-14};",
 "MAT.13.38": "[s Fäld]{1,3} [aber]{2} [isch]{4} [d Wält]{5,6}; [de guet]{7,9} [Same]{10} [aber]{8}, [das]{11} [sind]{12} [d Söhn]{13,14} [vom Riich]{15,16}; [s Uchruut]{17,19} [aber]{18} [sind]{20} [d Söhn]{21,22} [vom Bööse]{23,24};",
 "MAT.13.39": "[de Feind]{1,3} [aber]{2}, [wo]{4} [s]{6} [gsäät hät]{5}, [isch]{7} [de Tüüfel]{8,9}; [d Ärn]{10,12} [aber]{11} [isch]{15} [d Vollendig]{13} [vo de Wältziit]{14}; [d Schnitter]{16,18} [aber]{17} [sind]{20} [Ängel]{19}.",
 "MAT.13.40": "[Wie]{1} [mer]{3} [also]{2} [s Uchruut]{4,5} [zämeliist]{3} und{6} [im Füür]{7} [verbrännt]{8}, [so]{9} [wird s sii]{10} [a]{11} [de Vollendig]{12,13} [vo de Wältziit]{14,15}:",
 "MAT.13.41": "[De Mänschesohn]{2-5} [wird]{1} [sini]{8} [Ängel]{6,7} [usschicke]{1}, und{9} [si wärded]{10} [us]{11} [sim]{14} [Riich]{12,13} [alles]{15,16} [zämeläse]{10}, [was z Fall bringt]{17}, und{18} [die]{19}, wo [d Gsetzlosigkeit]{21,22} [tüend]{20},",
 "MAT.13.42": "und{1} [si wärded]{2} [si]{3} [i]{4} [de]{5} [Füürofe]{6-8} [rüere]{2}; [dört]{9} [wird]{10} [s Brüele]{11,12} und{13} [s Zändchnirsche]{14-17} [sii]{10}.",
 "MAT.13.43": "[Dänn]{1} [wärded]{4} [d Grächte]{2,3} [lüüchte]{4} [wie]{5} [d Sunne]{6,7} [im]{8,9} [Riich]{10} [vo irem]{11,13} [Vatter]{12}. [Wer]{14} [Ohre]{16} [hät]{15}, [dä söll lose]{17}!",
 "MAT.13.44": "[S Riich vo de Himel]{3-6} [isch wie]{1,2} [en Schatz]{7}, wo [im]{9,10} [Fäld]{11} [versteckt isch]{8}. [En Mänsch]{14} [hät]{13} [en]{12} [gfunde]{13} und [hät]{15} en [versteckt]{15}, und{16} [i]{17} [sinere]{20} [Fröid]{18,19} [gaat er hii]{21} und{22} [verchauft]{23} [alles]{24}, [won]{25} [er hät]{26}, und{27} [chauft]{28} [das]{29,31} [Fäld]{30}.",
 "MAT.13.45": "[Wider]{1} [isch]{3} [s Riich vo de Himel]{4-7} [wie]{2} [en Chaufmaa]{8,9}, wo [schööni]{11} [Perle]{12} [suecht]{10}.",
 "MAT.13.46": "[Won er]{1} [aber]{2} [e]{3} [choschtbari]{4} [Perle]{5} [gfunde hät]{1}, [isch er hiigange]{6}, [hät]{7} [alles]{8} [verchauft]{7}, [won]{9} [er gha hät]{10}, und{11} [hät]{12} [si]{13} [gchauft]{12}.",
 "MAT.13.47": "[Wider]{1} [isch]{3} [s Riich vo de Himel]{4-7} [wie]{2} [es Schleppnetz]{8}, wo [i]{10} [de]{11} [See]{12} [gworfe worde isch]{9} und{13} Fisch [vo jeder]{14,15} [Art]{16} [gfange hät]{17}.",
 "MAT.13.48": "[Wo]{2} [s]{1} [voll gsii isch]{3}, [händ si s]{4} [as]{5,6} [Ufer]{7} [ufezoge]{4}, und{8} [si sind abgsässe]{9} und [händ]{10} [di guete]{11,12} [i]{13} [Gfäss]{14} [zämegläse]{10}; [di unbruuchbare]{15,17} [aber]{16} [händ si usegrüert]{18,19}.",
 "MAT.13.49": "[So]{1} [wird s sii]{2} [a]{3} [de Vollendig]{4,5} [vo de Wältziit]{6,7}: [D Ängel]{9,10} [wärded usegaa]{8} und{11} [d Bööse]{13,14} [us]{15} [de Mitti]{16} [vo de Grächte]{17,18} [ussondere]{12},",
 "MAT.13.50": "und{1} [si wärded]{2} [si]{3} [i]{4} [de]{5} [Füürofe]{6-8} [rüere]{2}; [dört]{9} [wird]{10} [s Brüele]{11,12} und{13} [s Zändchnirsche]{14-17} [sii]{10}.",
 "MAT.13.51": "[Händ er]{1} [das]{2} [alles]{3} [verstande]{1}?» [Si säged]{4} [zu ihm]{5}: «[Ja]{6}.»",
 "MAT.13.52": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: «[Drum]{5,6} [isch]{15} [jede]{7} [Schriftgelehrte]{8}, wo [fürs]{10} [Riich vo de Himel]{11-13} [en Jünger worde isch]{9}, [wie]{14} [en Huusherr]{16,17}, [wo]{18} [us]{20} [sim]{23} [Schatz]{21,22} [Neus]{24} und{25} [Alts]{26} [füürenimmt]{19}.»",
 "MAT.13.53": "Und{1} [es isch passiert]{2}: [Wo]{3} [de Jesus]{5,6} [mit]{4} [dene]{9} [Gliichnis]{7,8} [fertig gsii isch]{4}, [isch er]{10} [vo dört]{11} [wiitergzoge]{10}.",
 "MAT.13.54": "Und{1} [er isch]{2} [i]{3} [sini]{6} [Heimet]{4,5} [choo]{2} und [hät]{7} [si]{8} [i]{9} [irer]{12} [Synagoge]{10,11} [gleert]{7}, [so dass]{13} [si]{15} [gstuunt]{14} und{16} [gseit händ]{17}: «[Vo wo]{18} [hät dä]{19} [die]{22} [Wiisheit]{20,21} und{23} [d Chrafttate]{24,25}?",
 "MAT.13.55": "[Isch]{3} [dä]{2} [nöd]{1} [de]{4} [Sohn]{7} [vom Zimmermaa]{5,6}? [Heisst]{12} [nöd]{8} [sini]{11} [Mueter]{9,10} [Maria]{13}, und{14} [sini]{17} [Brüeder]{15,16} [Jakobus]{18} und{19} [Josef]{20} und{21} [Simon]{22} und{23} [Judas]{24}?",
 "MAT.13.56": "Und{1} [sind]{9} [nöd]{5} [sini]{4} [Schwöschtere]{2,3} [alli]{6} [da bi]{7} [üs]{8}? [Vo wo]{10} [hät dä]{12} [also]{11} [das]{13} [alles]{14}?»",
 "MAT.13.57": "Und{1} [si händ]{2} [a]{3} [ihm]{4} [Aastoss gnoo]{2}. [De Jesus]{5,7} [aber]{6} [hät]{8} [zu ine]{9} [gseit]{8}: «[En Prophet]{12} [isch]{11} [nöd]{10} [ohni Ehr]{13}, [usser]{14,15} [i]{16} [de]{17} [Heimet]{18} und{19} [i]{20} [sim]{23} [Huus]{21,22}.»",
 "MAT.13.58": "Und{1} [er hät]{3} [dört]{4} [nöd]{2} [vil]{6} [Chrafttate]{5} [gmacht]{3}, [wäge]{7} [irem]{10} [Unglaube]{8,9}.",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MAT.13.1", "An jenem Tag", "literal", "Ἐν τῇ ἡμέρᾳ ἐκείνῃ", None, ["Am selben Tag"],
  "Die Zeitangabe verbindet die Gleichnisrede mit den Auseinandersetzungen und dem Wort über Jesu wahre Verwandte am Ende von Kapitel 12 ([[MAT.12.46]]–[[MAT.12.50]]). Das Haus, aus dem Jesus hinausgeht, ist nicht näher bestimmt; in [[MAT.13.36]] kehrt er dorthin zurück."),
 ("MAT.13.1", "See", "adapted", "θάλασσαν", "Meer", ["Meer"],
  "Matthäus nennt den See Gennesaret wie Markus θάλασσα («Meer»). Im Deutschen ist das Gewässer ein See; ebenso [[MAT.13.47]]."),
 ("MAT.13.2", "Menschenmengen", "literal", "ὄχλοι", None, ["Volksmengen", "Scharen"],
  "ὄχλος (nach MACULA-Lemma 49-mal bei Matthäus) im Singular «Menge», im Plural «Menschenmengen»; ebenso [[MAT.13.34]] und [[MAT.13.36]]."),
 ("MAT.13.3", "Gleichnissen", "traditional", "παραβολαῖς", None, ["Bildreden", "Vergleichen", "Rätselworten"],
  "παραβολή ist ein Vergleich, ein Bildwort, auch ein rätselhaftes Wort (hebräisch māšāl). Das Wort steht in Kapitel 13 12-mal, bei Matthäus insgesamt 17-mal (nach MACULA-Lemma); einheitlich «Gleichnis» wie bei Markus ([[MRK.4.2]])."),
 ("MAT.13.3", "Siehe", "traditional", "Ἰδοὺ", None, ["Seht", "Schaut"],
  "Aufmerksamkeitssignal; einheitlich «siehe» im ganzen Evangelium."),
 ("MAT.13.3", "der Sämann", "literal", "ὁ σπείρων", "der Säende", None,
  "Das Partizip mit Artikel bezeichnet den, der sät; «Sämann» wie in [[MRK.4.3]]. Ebenso [[MAT.13.18]] (dort Partizip Aorist τοῦ σπείραντος) und [[MAT.13.37]]."),
 ("MAT.13.5", "sogleich", "literal", "εὐθέως", None, ["sofort", "gleich"],
  "Einheitliche Wiedergabe für εὐθέως und εὐθύς im Matthäusevangelium (nach MACULA-Lemma 13- bzw. 6-mal); ebenso [[MAT.13.20]] und [[MAT.13.21]] (εὐθύς)."),
 ("MAT.13.5", "keine tiefe Erde", "adapted", "μὴ ἔχειν βάθος γῆς", "keine Tiefe an Erde", None,
  "Gemeint ist eine dünne Erdschicht über dem Fels, nicht ein mit Steinen durchsetzter Acker."),
 ("MAT.13.6", "versengt", "literal", "ἐκαυματίσθη", None, ["verbrannt", "von der Hitze verdorrt"], None),
 ("MAT.13.8", "teils hundertfach, teils sechzigfach, teils dreissigfach", "adapted", "ὃ μὲν ἑκατὸν ὃ δὲ ἑξήκοντα ὃ δὲ τριάκοντα",
  "das eine hundert, das andere sechzig, das andere dreissig", None,
  "Matthäus zählt absteigend, Markus aufsteigend ([[MRK.4.8]]). Gemeint ist das Vielfache der Aussaat. Wie hoch übliche Erträge waren und ob die Zahlen als ungewöhnlich reiche Ernte gedacht sind, wird diskutiert. Ebenso [[MAT.13.23]]."),
 ("MAT.13.9", "Wer Ohren hat, der höre!", "literal", "ὁ ἔχων ὦτα ἀκουέτω", None, None,
  "Weckruf; ebenso [[MAT.11.15]] und [[MAT.13.43]]. Der SBLGNT liest ohne «zu hören» (siehe Alternative)."),
 ("MAT.13.10", "traten herzu", "literal", "προσελθόντες", "hinzugetreten", ["kamen zu ihm"],
  "προσέρχομαι ist ein Lieblingswort des Matthäus (nach MACULA-Lemma 51-mal); einheitlich «herzutreten» bzw. «zu ihm treten» (ebenso [[MAT.13.27]], [[MAT.13.36]])."),
 ("MAT.13.11", "die Geheimnisse", "interpretive", "τὰ μυστήρια", None, ["die Mysterien", "die verborgenen Pläne"],
  "μυστήριον meint im Neuen Testament keine Geheimlehre für Eingeweihte, sondern etwas Verborgenes, das Gott offenlegt. Matthäus hat den Plural und «zu erkennen» (γνῶναι), Markus den Singular ohne Verb ([[MRK.4.11]]). Das Passiv «ist gegeben» lässt Gott als Geber verstehen."),
 ("MAT.13.11", "des Reiches der Himmel", "traditional", "τῆς βασιλείας τῶν οὐρανῶν", "der Königsherrschaft der Himmel", ["des Himmelreichs", "der Herrschaft der Himmel"],
  "Matthäus sagt fast immer «Reich der Himmel» (nach MACULA-Lemmata 32-mal, «Reich Gottes» nur 4-mal), wo Markus und Lukas «Reich Gottes» haben. Der Plural entspricht dem hebräischen šāmayim; nach verbreiteter Deutung umschreibt «Himmel» ehrfürchtig den Gottesnamen. Einheitliche Wiedergabe «Reich der Himmel». βασιλεία meint zuerst Gottes Herrschen, nicht ein Gebiet."),
 ("MAT.13.12", "er wird Überfluss haben", "adapted", "περισσευθήσεται", "es wird ihm Überfluss gegeben werden", ["er wird im Überfluss haben"],
  "Passiv wie das vorangehende «wird gegeben werden»; der Satz steht wieder in [[MAT.25.29]]. Bei Markus steht das Wort in anderem Zusammenhang ([[MRK.4.25]])."),
 ("MAT.13.13", "weil", "interpretive", "ὅτι", None, ["dass", "denn"],
  "Matthäus schreibt ὅτι («weil»), wo [[MRK.4.12]] ἵνα («damit») hat: Die Gleichnisrede erscheint hier als Folge des Nichtverstehens, nicht als dessen Zweck. Ob Matthäus damit die Härte des Markus bewusst mildert, wird diskutiert; mit dem Zitat in [[MAT.13.14]]–[[MAT.13.15]] (μήποτε «damit nicht») bleibt die Spannung bestehen."),
 ("MAT.13.13", "sehend", "literal", "βλέποντες", None, ["obwohl sie sehen"],
  "Das Partizip nimmt das Jesajawort vorweg ([[ISA.6.9]]): Sie sehen und sehen doch nicht. συνίημι «verstehen» ist ein Leitwort des Kapitels (nach MACULA-Lemma 6-mal: [[MAT.13.13]]–[[MAT.13.15]], [[MAT.13.19]], [[MAT.13.23]], [[MAT.13.51]])."),
 ("MAT.13.14", "erfüllt sich", "literal", "ἀναπληροῦται", None, ["wird erfüllt", "geht in Erfüllung"],
  "Präsens und verstärktes Kompositum (ἀνα-πληρόω); sonst gebraucht Matthäus für die Schrifterfüllung πληρόω (vgl. [[MAT.13.35]]). Das Zitat folgt [[ISA.6.9-ISA.6.10]] im Wortlaut der Septuaginta. Anders als die meisten Erfüllungszitate des Evangeliums, die der Erzähler anführt, steht es in Jesu eigener Rede."),
 ("MAT.13.14", "Mit dem Gehör werdet ihr hören", "literal", "Ἀκοῇ ἀκούσετε", None, ["Hörend werdet ihr hören", "Ihr werdet hören und hören"],
  "Die Septuaginta gibt die hebräische Verdoppelung (Infinitiv und finites Verb) mit dem Dativ des Nomens wieder; gemeint ist eine Verstärkung."),
 ("MAT.13.14", "gewiss nicht", "literal", "οὐ μὴ", None, ["keinesfalls", "überhaupt nicht"],
  "οὐ μή mit Konjunktiv ist die stärkste Verneinung des Griechischen."),
 ("MAT.13.15", "ist abgestumpft", "adapted", "ἐπαχύνθη", "ist fett geworden", ["ist verhärtet", "ist unempfindlich geworden"],
  "Ein von Fett umschlossenes Herz ist Bild der Unempfänglichkeit; das Herz meint den Ort des Denkens und Wollens."),
 ("MAT.13.15", "damit sie nicht etwa", "interpretive", "μήποτε", None, ["sonst könnten sie", "ob sie nicht vielleicht doch"],
  "μήποτε heisst meist «damit nicht». Einige Auslegungen lesen es abgeschwächt als «ob sie nicht vielleicht doch umkehren». Die Fortsetzung steht im Indikativ Futur («und ich sie heilen werde»)."),
 ("MAT.13.15", "umkehren", "literal", "ἐπιστρέψωσιν", None, ["sich bekehren", "sich zuwenden"],
  "ἐπιστρέφω ist die Umkehr, die Hinwendung; das Wort ist von μετανοέω («umkehren, Umkehr» im Sinn der Sinnesänderung, z. B. [[MAT.4.17]]) zu unterscheiden, auch wenn beide im Deutschen «umkehren» heissen."),
 ("MAT.13.16", "Selig", "traditional", "μακάριοι", None, ["Glücklich", "Glücklich zu preisen", "Wohl"],
  "μακάριος preist jemanden als von Gott beschenkt glücklich. Vorschlag für eine einheitliche Wiedergabe im ganzen Evangelium (nach MACULA-Lemma 13-mal, darunter die Seligpreisungen [[MAT.5.3]]–[[MAT.5.11]]); ebenso bei Johannes ([[JHN.13.17]], [[JHN.20.29]])."),
 ("MAT.13.17", "Gerechte", "literal", "δίκαιοι", None, ["Fromme"],
  "δίκαιος meint den, der nach Gottes Willen lebt. In [[MAT.13.43]] und [[MAT.13.49]] stehen die Gerechten den Bösen im Gericht gegenüber."),
 ("MAT.13.17", "Amen, ich sage euch", "traditional", "ἀμὴν γὰρ λέγω ὑμῖν", None, ["Wahrlich, ich sage euch"],
  "Feste Wiedergabe im ganzen Evangelium; das γάρ («denn») davor ist nicht eigens übersetzt."),
 ("MAT.13.19", "der Böse", "interpretive", "ὁ πονηρὸς", None, ["das Böse", "der Satan"],
  "Männlich: der Böse, das heisst der Satan; [[MRK.4.15]] sagt hier «der Satan». Ebenso [[MAT.13.38]] («die Söhne des Bösen»), dort mit [[MAT.13.39]] («der Teufel»). Vgl. [[MAT.6.13]], wo die Wiedergabe offen ist."),
 ("MAT.13.19", "das Wort vom Reich", "literal", "τὸν λόγον τῆς βασιλείας", "das Wort des Reiches", ["die Botschaft vom Reich"], None),
 ("MAT.13.19", "das ist der, der an den Weg gesät wurde", "literal", "οὗτός ἐστιν ὁ παρὰ τὴν ὁδὸν σπαρείς", None, ["das ist das, was an den Weg gesät wurde", "bei ihm ist es wie mit dem, was an den Weg gesät wurde"],
  "Matthäus setzt den Hörenden mit dem Gesäten gleich, obwohl zuvor das Wort in sein Herz gesät wird; Same und Hörer gehen im Bild ineinander über. Die Übersetzung lässt das stehen. Ebenso [[MAT.13.20]], [[MAT.13.22]], [[MAT.13.23]]."),
 ("MAT.13.21", "unbeständig", "adapted", "πρόσκαιρός", "nur für eine Zeit", ["wankelmütig", "ein Mensch des Augenblicks"],
  "Wie [[MRK.4.17]]."),
 ("MAT.13.21", "Bedrängnis", "literal", "θλίψεως", None, ["Not", "Trübsal"], None),
 ("MAT.13.21", "kommt er sogleich zu Fall", "interpretive", "εὐθὺς σκανδαλίζεται", None, ["nimmt er sogleich Anstoss", "fällt er sogleich ab"],
  "Grundentscheid für σκανδαλίζω (nach MACULA-Lemma 14-mal bei Matthäus) und σκάνδαλον (5-mal): σκάνδαλον ist das Stellholz einer Falle oder ein Stolperstein. Absolut gebraucht «zu Fall kommen» bzw. «zu Fall bringen» (wie [[MRK.4.17]]); mit Bezug auf eine Person («an ihm») «Anstoss nehmen» ([[MAT.13.57]], wie [[MRK.6.3]]); das Nomen in [[MAT.13.41]] «was zu Fall bringt»."),
 ("MAT.13.22", "die Sorge dieser Weltzeit", "interpretive", "ἡ μέριμνα τοῦ αἰῶνος τούτου", "die Sorge dieses Äons", ["die Sorge dieser Welt", "die Sorgen des Alltags"],
  "αἰών meint die gegenwärtige Weltzeit im Gegensatz zur kommenden; im ganzen Kapitel «Weltzeit» (vgl. [[MAT.13.39]], [[MAT.13.40]], [[MAT.13.49]]). Der SBLGNT hat hier τούτου («dieser») mit RP gegen WH, Treg und NA28 (siehe Alternative)."),
 ("MAT.13.22", "die Verführung des Reichtums", "interpretive", "ἡ ἀπάτη τοῦ πλούτου", "die Täuschung des Reichtums", ["der trügerische Reiz des Reichtums"],
  "ἀπάτη ist Täuschung; gemeint ist, dass Reichtum mehr verspricht, als er hält. Wie [[MRK.4.19]]."),
 ("MAT.13.22", "ersticken", "adapted", "συμπνίγει", "erstickt", None,
  "Griechisch Singular bei zwei Subjekten; im Deutschen Plural."),
 ("MAT.13.22", "es wird fruchtlos", "interpretive", "ἄκαρπος γίνεται", None, ["er wird fruchtlos", "es bleibt ohne Frucht"],
  "Subjekt kann das Wort oder der Hörende sein; «es» bezieht sich auf das Wort."),
 ("MAT.13.23", "versteht", "literal", "συνιείς", None, ["begreift"],
  "Das Verstehen kennzeichnet den guten Boden; [[MRK.4.20]] hat «annehmen», [[LUK.8.15]] «festhalten»."),
 ("MAT.13.23", "dann auch", "adapted", "δὴ", None, ["gerade", "eben"],
  "Die Partikel hebt hervor, dass gerade dieser Frucht bringt."),
 ("MAT.13.24", "gleicht", "interpretive", "Ὡμοιώθη", "ist gleich geworden", ["ist zu vergleichen mit", "mit … verhält es sich wie mit"],
  "Aorist Passiv («ist gleich geworden, ist gleichgemacht worden»), in [[MAT.13.31]], [[MAT.13.33]], [[MAT.13.44]], [[MAT.13.45]] und [[MAT.13.47]] dagegen ὁμοία ἐστίν («ist gleich»), in [[MAT.13.52]] ὅμοιός ἐστιν. Alle sind mit «gleicht» wiedergegeben. Verglichen wird nicht das Reich mit dem Menschen (bzw. Senfkorn, Sauerteig, Schatz), sondern mit dem ganzen erzählten Vorgang. Ob der Aorist auf schon Geschehenes weist, ist umstritten."),
 ("MAT.13.25", "die Leute", "adapted", "τοὺς ἀνθρώπους", "die Menschen", None,
  "Gemeint sind die Menschen allgemein: während man schlief, also nachts. Ein Vorwurf der Nachlässigkeit liegt nicht im Wort."),
 ("MAT.13.25", "säte", "literal", "ἐπέσπειρεν", "säte darüber", ["säte nach", "säte dazu"],
  "ἐπισπείρω heisst «darüber, dazu säen», auf schon besätes Land; das «dazu» trägt im Deutschen das folgende «mitten unter den Weizen». RP liest das einfache ἔσπειρεν; die Übersetzung bleibt davon unberührt."),
 ("MAT.13.25", "Unkraut", "interpretive", "ζιζάνια", "Lolch", ["Taumellolch", "Lolch"],
  "ζιζάνιον bezeichnet nach verbreiteter Ansicht den Taumellolch (Lolium temulentum), ein Gras, das jung dem Weizen gleicht und dessen Körner, oft von einem Pilz befallen, giftig sind. «Unkraut» ist allgemeiner und in der Wendung vertraut. Das Wort steht im Neuen Testament nur in diesem Gleichnis und seiner Deutung (nach MACULA-Lemma 8-mal)."),
 ("MAT.13.26", "die Saat", "adapted", "ὁ χόρτος", "das Gras", ["das Grün", "die Halme"],
  "χόρτος ist alles, was grün aufwächst; hier die junge Saat."),
 ("MAT.13.27", "Knechte", "traditional", "δοῦλοι", None, ["Sklaven", "Diener"],
  "δοῦλος (nach MACULA-Lemma 30-mal bei Matthäus) ist der unfreie Diener; im Gleichnis die Hausleute des Hausherrn. «Knecht» wie bei Markus ([[MRK.12.2]]) und Johannes ([[JHN.4.51]]); «Sklave» nur, wo der Gegensatz zur Freiheit im Vordergrund steht."),
 ("MAT.13.27", "Hausherrn", "literal", "οἰκοδεσπότου", None, ["Gutsherrn", "Hausvaters"],
  "οἰκοδεσπότης ist der Herr eines Hauswesens samt Land und Gesinde; ebenso [[MAT.13.52]]."),
 ("MAT.13.27", "Herr", "literal", "Κύριε", None, None,
  "Höfliche Anrede an den Hausherrn."),
 ("MAT.13.28", "ein Feind", "adapted", "Ἐχθρὸς ἄνθρωπος", "ein feindlicher Mensch", ["ein Mensch, der mir feind ist"], None),
 ("MAT.13.30", "Schnittern", "literal", "θερισταῖς", None, ["Erntearbeitern"],
  "In der Deutung sind die Schnitter Engel ([[MAT.13.39]])."),
 ("MAT.13.30", "Bündel", "literal", "δέσμας", None, ["Garben", "Büschel"], None),
 ("MAT.13.31", "einem Senfkorn", "literal", "κόκκῳ σινάπεως", "einem Korn von Senf", None,
  "Senf hat sehr kleine Samen und wächst als Staude rasch in die Höhe; «kleiner als alle Samen» ist sprichwörtlich, «Baum» ([[MAT.13.32]]) übertreibt. Welche Senfart gemeint ist, wird diskutiert."),
 ("MAT.13.32", "Gartenkräuter", "literal", "λαχάνων", None, ["Gemüsepflanzen", "Stauden"], None),
 ("MAT.13.32", "nisten", "literal", "κατασκηνοῦν", None, ["wohnen", "sich niederlassen"],
  "Der Schluss klingt an Bilder vom grossen Baum an, in dem die Vögel des Himmels wohnen ([[DAN.4.12]], [[EZK.17.23]], [[EZK.31.6]]). Anders als [[MRK.4.32]] (im Schatten) nisten sie bei Matthäus in den Zweigen."),
 ("MAT.13.33", "dem Sauerteig", "literal", "ζύμῃ", None, ["Hefe"],
  "ζύμη ist gesäuerter Teig, mit dem man neuen Teig zum Gären bringt. Sonst ist er oft Bild für verderblichen Einfluss ([[MAT.16.6]], [[1CO.5.6]]); hier für das Reich der Himmel."),
 ("MAT.13.33", "drei Mass Mehl", "adapted", "ἀλεύρου σάτα τρία", "drei Sata Mehl", ["drei Sea Mehl", "drei Scheffel Mehl"],
  "σάτον entspricht dem hebräischen seʾāh, einem Hohlmass von nach üblichen Schätzungen etwa 12 bis 13 Litern; drei Sata sind eine sehr grosse Menge Mehl. Vgl. [[GEN.18.6]], wo Sara aus drei Mass Mehl backt."),
 ("MAT.13.33", "verbarg", "literal", "ἐνέκρυψεν", None, ["mengte unter", "mischte hinein"],
  "Wörtlich «verbarg darin». Das Verb verbindet das Gleichnis mit dem Verborgenen in [[MAT.13.35]] und [[MAT.13.44]]."),
 ("MAT.13.35", "durch den Propheten", "interpretive", "διὰ τοῦ προφήτου", None, None,
  "Das Zitat stammt aus [[PSA.78.2]], einem Psalm Asafs; [[2CH.29.30]] nennt Asaf einen Seher. Nach der CNTR-Transkription las die Erstschrift von 01 «durch den Propheten Jesaja», von einer Korrektur getilgt. Der SBLGNT-Apparat verzeichnet die Stelle nicht, deshalb steht der Befund hier und nicht als Alternative."),
 ("MAT.13.35", "damit erfüllt würde, was durch den Propheten gesagt ist", "traditional", "ὅπως πληρωθῇ τὸ ῥηθὲν διὰ τοῦ προφήτου λέγοντος", "damit erfüllt würde das durch den Propheten Gesagte, der sagt", None,
  "Einheitliche Wiedergabe der Erfüllungsformel im ganzen Evangelium (hier mit ὅπως statt ἵνα); λέγοντος ist durch den Doppelpunkt wiedergegeben."),
 ("MAT.13.35", "ich will aussprechen", "interpretive", "ἐρεύξομαι", "ich will hervorsprudeln lassen", ["ich will verkünden", "ich will kundtun"],
  "ἐρεύγομαι heisst eigentlich «ausstossen, hervorsprudeln». Die zweite Vershälfte weicht vom üblichen Septuagintatext von [[PSA.78.2]] ab und steht dem hebräischen Text näher; ob Matthäus eine andere griechische Fassung kannte oder selbst übersetzte, ist offen."),
 ("MAT.13.35", "seit der Grundlegung", "literal", "ἀπὸ καταβολῆς", None, ["seit Anbeginn", "seit der Grundlegung der Welt"],
  "Ohne «der Welt» (siehe Alternative); gemeint ist wohl dennoch die Grundlegung der Welt (vgl. [[MAT.25.34]])."),
 ("MAT.13.36", "Erkläre", "literal", "Διασάφησον", "Mach deutlich", ["Deute"], None),
 ("MAT.13.37", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", None,
  "Einheitlich «der Menschensohn» im ganzen Evangelium; Selbstbezeichnung Jesu mit Anklang an [[DAN.7.13]]. Ebenso [[MAT.13.41]]."),
 ("MAT.13.38", "die Söhne des Reiches", "literal", "οἱ υἱοὶ τῆς βασιλείας", None, ["die Kinder des Reiches", "die zum Reich gehören"],
  "Semitische Ausdrucksweise: «Sohn von» bezeichnet Zugehörigkeit. Dieselbe Wendung steht in [[MAT.8.12]] für die, die hinausgeworfen werden; ebenso «die Söhne des Bösen» hier."),
 ("MAT.13.39", "der Teufel", "literal", "ὁ διάβολος", "der Verleumder", None, None),
 ("MAT.13.39", "die Vollendung der Weltzeit", "literal", "συντέλεια αἰῶνός", None, ["das Ende der Welt", "das Ende des Zeitalters"],
  "Die Formel steht im Neuen Testament nur bei Matthäus ([[MAT.13.39]], [[MAT.13.40]], [[MAT.13.49]], [[MAT.24.3]], [[MAT.28.20]]; nach MACULA-Lemma συντέλεια 5-mal); einheitlich «Vollendung der Weltzeit»."),
 ("MAT.13.40", "eingesammelt", "literal", "συλλέγεται", None, ["gesammelt", "gejätet"],
  "Dasselbe Verb wie in [[MAT.13.28]]–[[MAT.13.30]] und [[MAT.13.41]] («einsammeln») und in [[MAT.13.48]] («zusammenlesen»)."),
 ("MAT.13.41", "was zu Fall bringt", "interpretive", "τὰ σκάνδαλα", "die Fallstricke", ["die Ärgernisse", "die Verführungen"],
  "Sächlicher Plural; gemeint sein können Dinge oder Menschen, die andere zu Fall bringen. Grundentscheid siehe [[MAT.13.21]]."),
 ("MAT.13.41", "Gesetzlosigkeit", "literal", "τὴν ἀνομίαν", None, ["Unrecht", "Bosheit"],
  "Einheitliche Wiedergabe von ἀνομία (nach MACULA-Lemma 4-mal bei Matthäus: [[MAT.7.23]], [[MAT.13.41]], [[MAT.23.28]], [[MAT.24.12]]): wörtlich «Gesetzlosigkeit», ein Leben gegen Gottes Weisung."),
 ("MAT.13.42", "Feuerofen", "literal", "τὴν κάμινον τοῦ πυρός", "den Ofen des Feuers", None,
  "Anklang an [[DAN.3.6]]. Ebenso [[MAT.13.50]]."),
 ("MAT.13.42", "das Weinen und das Zähneknirschen", "literal", "ὁ κλαυθμὸς καὶ ὁ βρυγμὸς τῶν ὀδόντων", None, ["das Heulen und Zähneklappern"],
  "Feste Wendung bei Matthäus ([[MAT.8.12]], [[MAT.13.42]], [[MAT.13.50]], [[MAT.22.13]], [[MAT.24.51]], [[MAT.25.30]]): Weinen aus Schmerz, Zähneknirschen aus Verzweiflung oder Wut; einheitlich so wiedergegeben."),
 ("MAT.13.43", "leuchten", "literal", "ἐκλάμψουσιν", None, ["aufstrahlen", "hervorleuchten"],
  "Anklang an [[DAN.12.3]]."),
 ("MAT.13.44", "Das Reich der Himmel gleicht einem Schatz", "interpretive", "Ὁμοία ἐστὶν ἡ βασιλεία τῶν οὐρανῶν θησαυρῷ", None, None,
  "Keine neue Redeeinleitung: Nach [[MAT.13.36]] spricht Jesus im Haus zu den Jüngern; die Übersetzung lässt die Rede von [[MAT.13.37]] bis zur Frage in [[MAT.13.51]] weiterlaufen. Ob die Gleichnisse [[MAT.13.44]]–[[MAT.13.50]] als Fortsetzung der Deutung oder als neue Reihe gedacht sind, gibt der Text nicht an."),
 ("MAT.13.44", "verborgen ist", "literal", "κεκρυμμένῳ", None, ["verborgen war"],
  "Perfekt Partizip: Der Schatz liegt verborgen. Die Erzählung wechselt danach ins Präsens («geht hin», «verkauft», «kauft»); die Übersetzung behält den Wechsel bei."),
 ("MAT.13.45", "einem Kaufmann", "adapted", "ἀνθρώπῳ ἐμπόρῳ", "einem Menschen, einem Kaufmann", ["einem Händler"],
  "ἄνθρωπος vor einer Berufsbezeichnung ist im Deutschen überflüssig. WH lässt ἀνθρώπῳ aus. Laut der automatischen Zuordnung lassen auch 01 (Erstschrift), 03, 032 und 04 das Wort aus; nach den CNTR-Transkriptionen steht in 032 und 04 jedoch die Abkürzung ανω (ἀνθρώπῳ), die die Zuordnung offenbar nicht erkannt hat. Die Korrektur von 01 und 05 haben das Wort. Die Übersetzung ändert sich nicht."),
 ("MAT.13.46", "verkaufte", "interpretive", "πέπρακεν", "hat verkauft", None,
  "Perfekt zwischen Aoristen; es kann das Verkaufen als abgeschlossen und endgültig hervorheben oder lebhaft erzählen."),
 ("MAT.13.47", "Fische aller Art", "adapted", "ἐκ παντὸς γένους", "aus jeder Art", None,
  "«Fische» ist ergänzt. γένος kann auch «Volk, Geschlecht» heissen; manche hören darin, dass Menschen aus allen Völkern gesammelt werden."),
 ("MAT.13.47", "Schleppnetz", "literal", "σαγήνῃ", None, ["Zugnetz"],
  "σαγήνη ist ein grosses Netz, das man vom Boot aus auslegt und an Land zieht."),
 ("MAT.13.48", "die unbrauchbaren", "adapted", "τὰ σαπρὰ", "die faulen", ["die schlechten", "die wertlosen"],
  "Gedacht ist an ungeniessbare oder nach [[LEV.11.9]]–[[LEV.11.12]] unreine Fische."),
 ("MAT.13.52", "Schriftgelehrte", "traditional", "γραμματεὺς", None, ["Schriftkundige", "Toralehrer"],
  "Einheitlich «Schriftgelehrte» im ganzen Evangelium. Viele Ausleger sehen in diesem Vers ein Selbstbild des Evangelisten oder seiner Gemeinde; das bleibt Deutung."),
 ("MAT.13.52", "zum Jünger geworden ist", "literal", "μαθητευθεὶς", None, ["unterwiesen ist", "geschult ist"],
  "Der Dativ τῇ βασιλείᾳ kann «für das Reich» oder «im Reich» heissen; RP liest εἰς τὴν βασιλείαν («in das Reich hinein»)."),
 ("MAT.13.52", "Schatz", "literal", "θησαυροῦ", None, ["Vorrat", "Schatzkammer"],
  "θησαυρός ist der Schatz und der Ort, wo man ihn aufbewahrt; das Wort nimmt [[MAT.13.44]] auf."),
 ("MAT.13.52", "Neues und Altes", "literal", "καινὰ καὶ παλαιά", None, None,
  "Das Neue steht voran. Was mit Neuem und Altem gemeint ist (etwa Jesu Lehre und die Schrift), sagt der Text nicht."),
 ("MAT.13.53", "Und es geschah, als Jesus", "literal", "καὶ ἐγένετο ὅτε ἐτέλεσεν ὁ Ἰησοῦς", None, None,
  "Schlussformel nach den grossen Reden ([[MAT.7.28]], [[MAT.11.1]], [[MAT.19.1]], [[MAT.26.1]]); einheitlich «Und es geschah, als Jesus … beendet hatte»."),
 ("MAT.13.54", "Heimat", "literal", "πατρίδα", None, ["Vaterstadt"],
  "Gemeint ist der Heimatort; Matthäus nennt Nazaret hier nicht (vgl. [[MAT.2.23]]). Ebenso [[MAT.13.57]]."),
 ("MAT.13.54", "hat dieser", "adapted", "τούτῳ", "diesem", None,
  "Dativ des Besitzes («woher [ist] diesem …»); das Fürwort kann abschätzig klingen («dieser da»)."),
 ("MAT.13.54", "Machttaten", "literal", "δυνάμεις", None, ["Wunder", "Krafttaten"],
  "δύναμις ist Kraft und die Tat, in der sie sich zeigt; wie bei Markus «Machttat» ([[MRK.6.2]]). Ebenso [[MAT.13.58]]."),
 ("MAT.13.55", "des Zimmermanns", "traditional", "τοῦ τέκτονος", None, ["des Bauhandwerkers", "des Handwerkers"],
  "τέκτων bezeichnet einen Handwerker, der vor allem mit Holz, aber auch mit Stein baut. Matthäus sagt «der Sohn des Zimmermanns», [[MRK.6.3]] «der Zimmermann, der Sohn der Maria»."),
 ("MAT.13.55", "Brüder", "literal", "ἀδελφοὶ", None, ["Verwandten"],
  "ἀδελφός heisst «Bruder». Ob leibliche Brüder, Halbbrüder oder Vettern gemeint sind, ist zwischen den Konfessionen umstritten; die Übersetzung bleibt beim Wortlaut. Ebenso «Schwestern» in [[MAT.13.56]]."),
 ("MAT.13.55", "Josef", "literal", "Ἰωσὴφ", None, ["Joses"],
  "[[MRK.6.3]] hat Joses, eine Kurzform von Josef; ebenso RP hier (siehe Alternative)."),
 ("MAT.13.57", "sie nahmen Anstoss", "interpretive", "ἐσκανδαλίζοντο", None, ["sie kamen zu Fall", "sie lehnten ihn ab"],
  "Imperfekt. Mit Bezug auf eine Person «Anstoss nehmen an»; Grundentscheid siehe [[MAT.13.21]]."),
 ("MAT.13.57", "ohne Ehre", "literal", "ἄτιμος", None, ["ungeehrt", "verachtet"], None),
 ("MAT.13.58", "er tat dort nicht viele Machttaten", "literal", "οὐκ ἐποίησεν ἐκεῖ δυνάμεις πολλὰς", None, None,
  "[[MRK.6.5]] sagt «er konnte dort keine Machttat tun»; Matthäus formuliert «tat nicht viele»."),
 ("MAT.13.58", "Unglaubens", "literal", "ἀπιστίαν", None, ["Misstrauens"], None),
]

DEC_GSW = [
 ("MAT.13.1", "See", "adapted", "θάλασσαν", "Meer", ["Meer"],
  "De Matthäus nännt de See Gennesaret wie de Markus θάλασσα («Meer»); uf Tüütsch isch es en See. Gliich i [[MAT.13.47]]."),
 ("MAT.13.2", "vil Lüüt", "adapted", "ὄχλοι πολλοί", "vil Mängine", ["e grossi Mängi"],
  "ὄχλος im Singular «Mängi», im Plural «Lüüt» (au [[MAT.13.34]], [[MAT.13.36]]), wil «Mängine» im Züritüütsch frömd tönt."),
 ("MAT.13.3", "Gliichnis", "traditional", "παραβολαῖς", None, ["Bildrede", "Vergliich"],
  "παραβολή isch en Vergliich, es Bildwort, au es Rätselwort. Im ganze Kapitel «Gliichnis» wie bim Markus."),
 ("MAT.13.3", "Lueg", "traditional", "Ἰδοὺ", "Lueg", ["Lueged"],
  "ἰδού isch e feschti Form zum Ufmerksammache; im ganze Evangelium «lueg», au wänn mehreri aagredt sind."),
 ("MAT.13.5", "grad", "literal", "εὐθέως", None, ["sofort"],
  "Einheitlich «grad» für εὐθέως und εὐθύς im Matthäusevangelium."),
 ("MAT.13.9", "dä söll lose", "adapted", "ἀκουέτω", "dä söll ghööre", None,
  "«Lose» heisst im Züritüütsch «zuelose, ufpasse»; das trifft de Wäckruef. Gliich i [[MAT.13.43]]."),
 ("MAT.13.10", "sind härechoo", "literal", "προσελθόντες", None, ["sind zue ihm choo"],
  "προσέρχομαι isch es Lieblingswort vom Matthäus; einheitlich «härechoo» oder «zu ihm choo»."),
 ("MAT.13.11", "vom Riich vo de Himel", "traditional", "τῆς βασιλείας τῶν οὐρανῶν", None, ["vom Himelriich", "vo de Herrschaft vo de Himel"],
  "De Matthäus seit fascht immer «Riich vo de Himel», wo de Markus und de Lukas «Riich vo Gott» händ; nach verbreiteter Düütig umschriibt «Himel» de Gottesname. Einheitlich im ganze Evangelium."),
 ("MAT.13.11", "d Gheimnis", "interpretive", "τὰ μυστήρια", None, ["d Myschterie"],
  "μυστήριον isch nöd e Gheimlehr, sondern öppis Verborgnigs, wo Gott sälber offeleit. De Matthäus hät de Plural."),
 ("MAT.13.13", "wil", "interpretive", "ὅτι", None, ["dass"],
  "De Matthäus schriibt ὅτι («wil»), wo [[MRK.4.12]] ἵνα («damit») hät: D Gliichnis sind da Folg vom Nöd-Verstaa, nöd de Zwäck. Öb de Matthäus d Härti vom Markus mildere wott, isch umstritte."),
 ("MAT.13.13", "mit offne Auge", "adapted", "βλέποντες", "luegend", ["obwohl si lueged"],
  "S Partizip «luegend» isch im Züritüütsch nöd gläufig; «mit offne Auge» und «mit offne Ohre» säged s glich (wie bim Markus)."),
 ("MAT.13.14", "Mit de Ohre wärded ir ghööre", "literal", "Ἀκοῇ ἀκούσετε", None, ["Ghööre wärded ir, ghööre"],
  "D Septuaginta git e hebräischi Verdopplig wider; gmeint isch e Verstärkig. S Zitat isch [[ISA.6.9-ISA.6.10]]."),
 ("MAT.13.15", "isch abgstumpft", "adapted", "ἐπαχύνθη", "isch fett worde", ["isch verhärtet"],
  "Es Härz, wo vo Fett umgää isch, isch es Bild für Unempfänglichkeit."),
 ("MAT.13.16", "Sälig", "traditional", "μακάριοι", None, ["Glücklich", "Wohl eu"],
  "μακάριος priist öpper als vo Gott bschänkt glücklich. Vorschlag für s ganz Evangelium, au für d Säligpriisige ([[MAT.5.3]]–[[MAT.5.11]])."),
 ("MAT.13.17", "Amen, ich säg eu", "traditional", "ἀμὴν γὰρ λέγω ὑμῖν", None, None,
  "Feschti Widergab im ganze Evangelium."),
 ("MAT.13.19", "de Böös", "interpretive", "ὁ πονηρὸς", None, ["s Bööse", "de Satan"],
  "Männlich: de Böös, also de Satan; [[MRK.4.15]] seit da «de Satan». Gliich [[MAT.13.38]]."),
 ("MAT.13.19", "das isch dä, wo a de Wäg gsäät worde isch", "literal", "οὗτός ἐστιν ὁ παρὰ τὴν ὁδὸν σπαρείς", None, None,
  "De Matthäus setzt de Hörer mit em Gsääte gliich, obwohl vorher s Wort is Härz gsäät wird; Same und Hörer gönd im Bild inenand über. Gliich i [[MAT.13.20]], [[MAT.13.22]], [[MAT.13.23]]."),
 ("MAT.13.21", "chunnt er grad z Fall", "interpretive", "εὐθὺς σκανδαλίζεται", None, ["nimmt er grad Aastoss"],
  "Grundentscheid für σκανδαλίζω und σκάνδαλον (s Stellholz vo ere Falle, en Stolperstei): eleige «z Fall choo / z Fall bringe»; mit Bezug uf e Person «Aastoss nää a» ([[MAT.13.57]]); s Nomen i [[MAT.13.41]] «was z Fall bringt»."),
 ("MAT.13.21", "Not", "adapted", "θλίψεως", "Bedrängnis", ["Trüebsal"], "Wie bim Markus ([[MRK.4.17]])."),
 ("MAT.13.22", "d Sorg vo dere Wältziit", "interpretive", "ἡ μέριμνα τοῦ αἰῶνος τούτου", None, ["d Sorg vo dere Wält", "d Alltagssorge"],
  "αἰών isch di jetzig Wältziit im Gägesatz zur chömende; im ganze Kapitel «Wältziit». De SBLGNT hät da τούτου mit RP gäge WH, Treg und NA28 (lueg d Alternative)."),
 ("MAT.13.22", "es wird unfruchtbar", "interpretive", "ἄκαρπος γίνεται", None, ["er wird unfruchtbar"],
  "S Subjekt cha s Wort oder de Hörer sii."),
 ("MAT.13.24", "isch wie", "adapted", "Ὡμοιώθη", "isch gliich worde", ["glicht"],
  "Aorist Passiv («isch gliich worde»), i [[MAT.13.31]], [[MAT.13.33]], [[MAT.13.44]], [[MAT.13.45]], [[MAT.13.47]] dagäge ὁμοία ἐστίν («isch gliich»), i [[MAT.13.52]] ὅμοιός ἐστιν. Im Züritüütsch seit mer eifach «isch wie». Vergliche wird nöd s Riich mit em Mänsch, sondern mit em ganze Vorgang."),
 ("MAT.13.25", "Uchruut", "interpretive", "ζιζάνια", "Lolch", ["Taumellolch"],
  "ζιζάνιον isch nach verbreiteter Aasicht de Taumellolch, es Gras, wo jung wie Weize uusgseht und giftigi Chörner hät. «Uchruut» isch allgemeiner und vertrout."),
 ("MAT.13.27", "D Chnächt", "traditional", "οἱ δοῦλοι", None, ["d Sklave", "d Diener"],
  "δοῦλος isch de unfrei Diener; «Chnächt» wie bim Markus und Johannes."),
 ("MAT.13.27", "Huusherr", "literal", "οἰκοδεσπότου", None, ["Guetsherr"], None),
 ("MAT.13.28", "en Feind", "adapted", "Ἐχθρὸς ἄνθρωπος", "en feindliche Mänsch", None, None),
 ("MAT.13.29", "suscht", "adapted", "μήποτε", "damit nöd öppe", None,
  "«Damit nöd öppe» wär wörtlicher; «suscht» seit s im Züritüütsch natürlicher."),
 ("MAT.13.30", "wird ich", "literal", "ἐρῶ", None, ["säg ich"],
  "Futur; im Züritüütsch gieng au s Präsens."),
 ("MAT.13.31", "es Sänfchorn", "literal", "κόκκῳ σινάπεως", None, None,
  "Sänf hät sehr chliini Same und wachst schnäll i d Höchi; «Baum» übertriibt."),
 ("MAT.13.33", "drüü Mass", "adapted", "σάτα τρία", "drüü Sata", ["drüü Sea"],
  "σάτον isch es Hohlmass vo öppe 12 bis 13 Liter; drüü Sata sind e riesigi Mängi Mehl (vgl. [[GEN.18.6]])."),
 ("MAT.13.33", "durgsüüret", "literal", "ἐζυμώθη", None, ["ufgange"], None),
 ("MAT.13.35", "dur de Prophet", "interpretive", "διὰ τοῦ προφήτου", None, None,
  "S Zitat chunnt us [[PSA.78.2]], eme Psalm vom Asaf, wo [[2CH.29.30]] en Seher nännt. Nach de CNTR-Transkription hät d Erschtschrift vo 01 «dur de Prophet Jesaja», vo ere Korrektur gstriche; de SBLGNT-Apparat füert d Stell nöd."),
 ("MAT.13.35", "Muul", "literal", "στόμα", None, ["Mund"],
  "Im Züritüütsch isch «Muul» s gwöhnlich Wort, nöd grob."),
 ("MAT.13.35", "ich will usspräche", "interpretive", "ἐρεύξομαι", "ich will usesprudle", ["ich will verchünde"],
  "ἐρεύγομαι heisst eigentlich «usstoosse, usesprudle»."),
 ("MAT.13.37", "de Mänschesohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", None, None,
  "Einheitlich im ganze Evangelium; Selbstbezeichnig vom Jesus mit Aaklang a [[DAN.7.13]]."),
 ("MAT.13.38", "d Söhn vom Riich", "literal", "οἱ υἱοὶ τῆς βασιλείας", None, ["d Chind vom Riich", "die, wo zum Riich ghöred"],
  "Semitischi Uusdrucksart: «Sohn vo» heisst «ghört zu»."),
 ("MAT.13.39", "d Vollendig vo de Wältziit", "literal", "συντέλεια αἰῶνός", None, ["s Änd vo de Wält"],
  "D Formel staat nu bim Matthäus ([[MAT.13.39]], [[MAT.13.40]], [[MAT.13.49]], [[MAT.24.3]], [[MAT.28.20]]); einheitlich «Vollendig vo de Wältziit»."),
 ("MAT.13.41", "d Gsetzlosigkeit", "literal", "τὴν ἀνομίαν", None, ["s Unrächt"],
  "Einheitlich für ἀνομία ([[MAT.7.23]], [[MAT.23.28]], [[MAT.24.12]])."),
 ("MAT.13.42", "s Brüele und s Zändchnirsche", "literal", "ὁ κλαυθμὸς καὶ ὁ βρυγμὸς τῶν ὀδόντων", None, None,
  "Feschti Wändig bim Matthäus ([[MAT.8.12]], [[MAT.22.13]], [[MAT.24.51]], [[MAT.25.30]]); «brüele» heisst im Züritüütsch «gränne, weine»."),
 ("MAT.13.44", "S Riich vo de Himel isch wie en Schatz", "interpretive", "Ὁμοία ἐστὶν ἡ βασιλεία τῶν οὐρανῶν θησαυρῷ", None, None,
  "Kei neui Redeiileitig: De Jesus redt im Huus wiiter zu de Jünger; d Übersetzig laat d Red vo [[MAT.13.37]] bis zur Frag i [[MAT.13.51]] laufe."),
 ("MAT.13.45", "en Chaufmaa", "adapted", "ἀνθρώπῳ ἐμπόρῳ", "eme Mänsch, eme Chaufmaa", None,
  "ἄνθρωπος vor ere Bruefsbezeichnig bruucht s im Tüütsche nöd. Zur automatische Zueornig vo de Handschrifte lueg d hochtüütschi Entscheidig."),
 ("MAT.13.47", "Fisch vo jeder Art", "adapted", "ἐκ παντὸς γένους", "us jeder Art", None,
  "«Fisch» isch ergänzt; γένος cha au «Volk» heisse."),
 ("MAT.13.48", "di unbruuchbare", "adapted", "τὰ σαπρὰ", "di fuule", ["di schlächte"],
  "Gmeint sind ungniessbari oder nach [[LEV.11.9]]–[[LEV.11.12]] unreini Fisch."),
 ("MAT.13.52", "Schriftgelehrte", "traditional", "γραμματεὺς", None, None,
  "Einheitlich «Schriftgelehrte», im Plural «Schriftgelehrti»."),
 ("MAT.13.53", "Und es isch passiert", "literal", "καὶ ἐγένετο", None, None,
  "Schlussformle nach de grosse Rede ([[MAT.7.28]], [[MAT.11.1]], [[MAT.19.1]], [[MAT.26.1]])."),
 ("MAT.13.54", "Heimet", "literal", "πατρίδα", None, ["Vatterstadt"],
  "Gmeint isch de Heimatort; de Matthäus nännt Nazaret da nöd."),
 ("MAT.13.54", "Chrafttate", "literal", "δυνάμεις", None, ["Wunder"],
  "δύναμις isch Chraft und d Tat, wo si sich drin zeigt; wie bim Markus."),
 ("MAT.13.55", "Brüeder", "literal", "ἀδελφοὶ", None, ["Verwandti"],
  "ἀδελφός heisst «Brüeder». Öb liiblichi Brüeder, Halbbrüeder oder Vettere gmeint sind, isch zwüsche de Konfessione umstritte."),
 ("MAT.13.57", "Aastoss gnoo", "interpretive", "ἐσκανδαλίζοντο", None, ["sind z Fall choo"],
  "Mit Bezug uf e Person «Aastoss nää a»; lueg [[MAT.13.21]]."),
 ("MAT.13.58", "er hät dört nöd vil Chrafttate gmacht", "literal", "οὐκ ἐποίησεν ἐκεῖ δυνάμεις πολλὰς", None, None,
  "[[MRK.6.5]] seit «er hät dört kei Chrafttat chöne tue»; de Matthäus seit «hät nöd vil gmacht»."),
]

# Lesarten-Alternativen: (Variante:Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw,
#  Lesarten de {Lesart: [(griechisch, Wiedergabe, Ausgaben)]}, Lesarten gsw, Entstehung de, Entstehung gsw).
# Handschriftenangaben nur aus WREAD-CNTR-MAT-013-001-058 (maschinelle Zuordnung) bzw. aus den CNTR-Transkriptionen.
ALTS = [
 ("VAR-SBLGNTAPP-MAT-013-009-01:R2", "MAT.13.9", "Wer Ohren hat,", "Wer Ohren hat, um zu hören,", "Wer Ohre hät,", "Wer Ohre hät zum ghööre,", "gering",
  "Mit ἀκούειν lautet der Weckruf wie in [[MRK.4.9]]: «Wer Ohren hat, um zu hören».", "Mit ἀκούειν luutet de Wäckruef wie i [[MRK.4.9]].",
  {"R1": [("ὦτα", "Ohren", "WH, NA28")], "R2": [("ὦτα ἀκούειν", "Ohren, um zu hören", "Treg, RP")]},
  {"R1": [("ὦτα", "Ohre", "WH, NA28")], "R2": [("ὦτα ἀκούειν", "Ohre zum ghööre", "Treg, RP")]},
  ["Der Zusatz kann an [[MRK.4.9]] und [[LUK.8.8]] angeglichen sein, wo er fest steht; ebenso kann er beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne Zusatz, 032, 04 und 05 mit ihm."],
  ["De Zuesatz cha a [[MRK.4.9]] und [[LUK.8.8]] aaglichen sii; er chönnt aber au bim Abschriibe usgfalle sii.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni Zuesatz, 032, 04 und 05 mit."]),
 ("VAR-SBLGNTAPP-MAT-013-011-01:R2", "MAT.13.11", "sagte zu ihnen:", "sagte:", "zu ine gseit:", "gseit:", "gering",
  "Ohne αὐτοῖς fehlt nur die Angabe der Angesprochenen.", "Ohni αὐτοῖς fählt nu, zu wem er redt.",
  {"R1": [("αὐτοῖς", "zu ihnen", "Treg, RP, NA28")], "R2": [("–", "(fehlt)", "WH, NIV")]},
  {"R1": [("αὐτοῖς", "zu ine", "Treg, RP, NA28")], "R2": [("–", "(fählt)", "WH, NIV")]},
  ["Das Fürwort kann als selbstverständlich ergänzt oder als überflüssig weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 03, 032 und 05 αὐτοῖς, 01 und 04 lassen es aus."],
  ["S Fürwort cha als sälbverständlich ergänzt oder als überflüssig wäggloo worde sii.",
   "Nach de automatische Zueornig läsed 03, 032 und 05 αὐτοῖς, 01 und 04 lönd s uus."]),
 ("VAR-SBLGNTAPP-MAT-013-022-01:R2", "MAT.13.22", "die Sorge dieser Weltzeit", "die Sorge der Weltzeit", "d Sorg vo dere Wältziit", "d Sorg vo de Wältziit", "gering",
  "Ohne τούτου («dieser») ist die Weltzeit nicht ausdrücklich als die gegenwärtige bezeichnet; der Sinn bleibt derselbe.",
  "Ohni τούτου isch d Wältziit nöd usdrücklich als di jetzig bezeichnet; de Sinn bliibt de gliich.",
  {"R1": [("τοῦ αἰῶνος τούτου", "dieser Weltzeit", "RP")], "R2": [("τοῦ αἰῶνος", "der Weltzeit", "WH, Treg, NA28")]},
  {"R1": [("τοῦ αἰῶνος τούτου", "vo dere Wältziit", "RP")], "R2": [("τοῦ αἰῶνος", "vo de Wältziit", "WH, Treg, NA28")]},
  ["τούτου kann als geläufige Verdeutlichung ergänzt worden sein (vgl. [[MAT.12.32]]); ebenso kann es ausgefallen sein. Der SBLGNT folgt hier RP gegen WH, Treg und NA28.",
   "Laut der automatischen Zuordnung lesen 032, 04 und die Korrektur von 01 τούτου, die Erstschrift von 01, 03 und 05 lassen es aus."],
  ["τούτου cha als gläufigi Verdüütlichung ergänzt worde sii (vgl. [[MAT.12.32]]); oder es isch usgfalle. De SBLGNT folgt da RP gäge WH, Treg und NA28.",
   "Nach de automatische Zueornig läsed 032, 04 und d Korrektur vo 01 τούτου, d Erschtschrift vo 01, 03 und 05 lönd s uus."]),
 ("VAR-SBLGNTAPP-MAT-013-028-01:R2", "MAT.13.28", "Die Knechte aber sagen zu ihm", "Sie aber sagen zu ihm", "D Chnächt aber säged zu ihm", "Si aber säged zu ihm", "gering",
  "Ohne δοῦλοι ist das Subjekt nur aus dem Zusammenhang klar; RP hat zudem die Vergangenheit («sagten»).",
  "Ohni δοῦλοι isch s Subjekt nu us em Zämehang klar; RP hät dezue d Vergangeheit («händ gseit»).",
  {"R1": [("οἱ δὲ δοῦλοι αὐτῷ λέγουσιν", "die Knechte aber sagen zu ihm", "Treg")], "R2": [("οἱ δὲ αὐτῷ λέγουσιν", "sie aber sagen zu ihm", "WH")],
   "R3": [("οἱ δὲ δοῦλοι λέγουσιν αὐτῷ", "die Knechte aber sagen zu ihm", "NA28")], "R4": [("οἱ δὲ δοῦλοι εἶπον αὐτῷ", "die Knechte aber sagten zu ihm", "RP")]},
  {"R1": [("οἱ δὲ δοῦλοι αὐτῷ λέγουσιν", "d Chnächt aber säged zu ihm", "Treg")], "R2": [("οἱ δὲ αὐτῷ λέγουσιν", "si aber säged zu ihm", "WH")],
   "R3": [("οἱ δὲ δοῦλοι λέγουσιν αὐτῷ", "d Chnächt aber säged zu ihm", "NA28")], "R4": [("οἱ δὲ δοῦλοι εἶπον αὐτῷ", "d Chnächt aber händ zu ihm gseit", "RP")]},
  ["δοῦλοι kann zur Verdeutlichung ergänzt worden sein; ebenso kann das Wort ausgefallen sein. Die schwankende Stellung von αὐτῷ deutet auf spätere Bearbeitung des Satzes.",
   "Laut der automatischen Zuordnung liest 03 ohne δοῦλοι, 04 wie der SBLGNT, 01 wie NA28, 032 wie RP; 05 hat die Zuordnung keiner Lesart zugewiesen."],
  ["δοῦλοι cha zur Verdüütlichung ergänzt worde sii; oder s Wort isch usgfalle.",
   "Nach de automatische Zueornig list 03 ohni δοῦλοι, 04 wie de SBLGNT, 01 wie NA28, 032 wie RP; 05 hät si keinere Läsart zuegordnet."]),
 ("VAR-SBLGNTAPP-MAT-013-034-01:R2", "MAT.13.34", "redete er nichts zu ihnen", "redete er nicht zu ihnen", "hät er nüüt zu ine gredt", "hät er nöd zu ine gredt", "gering",
  "Statt «nichts» heisst es «nicht»; der Sinn bleibt gleich.", "Statt «nüüt» heisst s «nöd»; de Sinn bliibt de gliich.",
  {"R1": [("οὐδέν", "nichts", "WH, Treg, NA28")], "R2": [("οὐκ", "nicht", "RP")]},
  {"R1": [("οὐδέν", "nüüt", "WH, Treg, NA28")], "R2": [("οὐκ", "nöd", "RP")]},
  ["οὐκ kann an [[MRK.4.34]] angeglichen sein, wo es steht.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 04 οὐδέν, 05 οὐκ."],
  ["οὐκ cha a [[MRK.4.34]] aaglichen sii, wo s staat.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 04 οὐδέν, 05 οὐκ."]),
 ("VAR-SBLGNTAPP-MAT-013-035-01:R2", "MAT.13.35", "seit der Grundlegung", "seit der Grundlegung der Welt", "sit de Grundlegig", "sit de Grundlegig vo de Wält", "gering",
  "Mit κόσμου ist ausdrücklich die Grundlegung der Welt genannt.", "Mit κόσμου isch usdrücklich d Grundlegig vo de Wält gnännt.",
  {"R1": [("καταβολῆς", "seit der Grundlegung", "WH, Treg")], "R2": [("καταβολῆς κόσμου", "seit der Grundlegung der Welt", "NA28, RP")]},
  {"R1": [("καταβολῆς", "sit de Grundlegig", "WH, Treg")], "R2": [("καταβολῆς κόσμου", "sit de Grundlegig vo de Wält", "NA28, RP")]},
  ["κόσμου kann nach der geläufigen Wendung «seit Grundlegung der Welt» ergänzt sein (vgl. [[MAT.25.34]], [[LUK.11.50]]); ebenso kann es früh ausgefallen sein. Der SBLGNT folgt hier WH und Treg gegen NA28 und RP.",
   "Laut der automatischen Zuordnung liest 03 ohne κόσμου, 01, 032, 04 und 05 mit ihm."],
  ["κόσμου cha nach de gläufige Wändig ergänzt sii (vgl. [[MAT.25.34]], [[LUK.11.50]]); oder es isch früe usgfalle. De SBLGNT folgt da WH und Treg gäge NA28 und RP.",
   "Nach de automatische Zueornig list 03 ohni κόσμου, 01, 032, 04 und 05 mit."]),
 ("VAR-SBLGNTAPP-MAT-013-036-01:R2", "MAT.13.36", "und ging ins Haus", "und Jesus ging ins Haus", "und isch is Huus gange", "und de Jesus isch is Huus gange", "gering",
  "Der Name verdeutlicht, wer ins Haus geht.", "De Name macht klar, wer is Huus gaat.",
  {"R1": [("οἰκίαν", "ins Haus", "WH, Treg, NA28")], "R2": [("οἰκίαν ὁ Ἰησοῦς", "Jesus … ins Haus", "RP")]},
  {"R1": [("οἰκίαν", "is Huus", "WH, Treg, NA28")], "R2": [("οἰκίαν ὁ Ἰησοῦς", "de Jesus … is Huus", "RP")]},
  ["Der Name kann am Beginn eines Leseabschnitts ergänzt worden sein; ebenso kann er ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 04 und 05 ohne den Namen."],
  ["De Name cha am Aafang vo me Läseabschnitt ergänzt worde sii; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 04 und 05 ohni de Name."]),
 ("VAR-SBLGNTAPP-MAT-013-037-01:R2", "MAT.13.37", "antwortete und sagte:", "antwortete und sagte zu ihnen:", "hät gantwortet und gseit:", "hät gantwortet und zu ine gseit:", "gering",
  "Der Zusatz nennt die Angesprochenen.", "De Zuesatz nännt, zu wem er redt.",
  {"R1": [("εἶπεν", "sagte", "WH, Treg, NA28")], "R2": [("εἶπεν αὐτοῖς", "sagte zu ihnen", "RP")]},
  {"R1": [("εἶπεν", "gseit", "WH, Treg, NA28")], "R2": [("εἶπεν αὐτοῖς", "zu ine gseit", "RP")]},
  ["Das Fürwort kann nach der häufigen Wendung ergänzt worden sein; ebenso kann es ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne Zusatz, 032 und 04 mit ihm."],
  ["S Fürwort cha nach de hüüfige Wändig ergänzt worde sii; oder es isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni Zuesatz, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-013-040-02:R2", "MAT.13.40", "der Vollendung der Weltzeit", "der Vollendung dieser Weltzeit", "de Vollendig vo de Wältziit", "de Vollendig vo dere Wältziit", "gering",
  "Mit τούτου ist die gegenwärtige Weltzeit ausdrücklich genannt.", "Mit τούτου isch di jetzig Wältziit usdrücklich gnännt.",
  {"R1": [("αἰῶνος", "der Weltzeit", "WH, Treg, NA28")], "R2": [("αἰῶνος τούτου", "dieser Weltzeit", "RP")]},
  {"R1": [("αἰῶνος", "vo de Wältziit", "WH, Treg, NA28")], "R2": [("αἰῶνος τούτου", "vo dere Wältziit", "RP")]},
  ["τούτου kann als Verdeutlichung ergänzt sein; in [[MAT.13.39]] und [[MAT.13.49]] steht die Formel ohne es.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne τούτου, 032 und 04 mit ihm."],
  ["τούτου cha als Verdüütlichung ergänzt sii; i [[MAT.13.39]] und [[MAT.13.49]] staat d Formle ohni.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni τούτου, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-013-043-01:R2", "MAT.13.43", "Wer Ohren hat,", "Wer Ohren hat, um zu hören,", "Wer Ohre hät,", "Wer Ohre hät zum ghööre,", "gering",
  "Wie in [[MAT.13.9]].", "Wie i [[MAT.13.9]].",
  {"R1": [("ὦτα", "Ohren", "WH, NA28")], "R2": [("ὦτα ἀκούειν", "Ohren, um zu hören", "Treg, RP")]},
  {"R1": [("ὦτα", "Ohre", "WH, NA28")], "R2": [("ὦτα ἀκούειν", "Ohre zum ghööre", "Treg, RP")]},
  ["Wie in [[MAT.13.9]]: Angleichung an [[MRK.4.9]] und [[LUK.8.8]] oder Ausfall.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne Zusatz, 032, 04 und 05 mit ihm."],
  ["Wie i [[MAT.13.9]]: Aagliichig a [[MRK.4.9]] und [[LUK.8.8]] oder Usfall.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni Zuesatz, 032, 04 und 05 mit."]),
 ("VAR-SBLGNTAPP-MAT-013-044-01:R2", "MAT.13.44", "Das Reich der Himmel gleicht einem Schatz", "Wiederum gleicht das Reich der Himmel einem Schatz",
  "S Riich vo de Himel isch wie en Schatz", "Wider isch s Riich vo de Himel wie en Schatz", "gering",
  "Mit πάλιν («wiederum») beginnt das Gleichnis wie die beiden folgenden.", "Mit πάλιν («wider») faat s Gliichnis wie di zwei nächschte aa.",
  {"R1": [("Ὁμοία", "gleicht", "WH, Treg, NA28")], "R2": [("Πάλιν ὁμοία", "Wiederum gleicht", "RP")]},
  {"R1": [("Ὁμοία", "isch wie", "WH, Treg, NA28")], "R2": [("Πάλιν ὁμοία", "Wider isch … wie", "RP")]},
  ["πάλιν kann an [[MAT.13.45]] und [[MAT.13.47]] angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01 (auch die Korrektur), 03 und 05 ohne πάλιν, 032 und 04 mit ihm."],
  ["πάλιν cha a [[MAT.13.45]] und [[MAT.13.47]] aaglichen sii.",
   "Nach de automatische Zueornig läsed 01 (au d Korrektur), 03 und 05 ohni πάλιν, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-013-044-02:R2", "MAT.13.44", "verkauft alles, was er hat", "verkauft, was er hat", "verchauft alles, won er hät", "verchauft, won er hät", "gering",
  "Ohne πάντα («alles») fehlt die Betonung, dass er alles verkauft; RP hat πάντα, nur in anderer Wortstellung.",
  "Ohni πάντα fählt d Betonig, dass er alles verchauft; RP hät πάντα, nu andersch gstellt.",
  {"R1": [("πωλεῖ πάντα ὅσα ἔχει", "verkauft alles, was er hat", "Treg, NA28")], "R2": [("πωλεῖ ὅσα ἔχει", "verkauft, was er hat", "WH")],
   "R3": [("πάντα ὅσα ἔχει πωλεῖ", "alles, was er hat, verkauft", "RP")]},
  {"R1": [("πωλεῖ πάντα ὅσα ἔχει", "verchauft alles, won er hät", "Treg, NA28")], "R2": [("πωλεῖ ὅσα ἔχει", "verchauft, won er hät", "WH")],
   "R3": [("πάντα ὅσα ἔχει πωλεῖ", "alles, won er hät, verchauft", "RP")]},
  ["πάντα kann nach [[MAT.13.46]] ergänzt sein («verkaufte alles, was er hatte»); ebenso kann es ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 05 wie der SBLGNT, 03 ohne πάντα, 032 und 04 wie RP."],
  ["πάντα cha nach [[MAT.13.46]] ergänzt sii; oder es isch usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 05 wie de SBLGNT, 03 ohni πάντα, 032 und 04 wie RP."]),
 ("VAR-SBLGNTAPP-MAT-013-051-01:R2", "MAT.13.51", "Habt ihr das alles verstanden?", "Jesus sagt zu ihnen: Habt ihr das alles verstanden?",
  "Händ er das alles verstande?", "De Jesus seit zu ine: Händ er das alles verstande?", "gering",
  "Die Redeeinleitung macht den Sprecher ausdrücklich.", "D Redeiileitig macht de Sprächer usdrücklich.",
  {"R1": [("Συνήκατε", "Habt ihr verstanden", "WH, Treg, NA28")], "R2": [("Λέγει αὐτοῖς ὁ Ἰησοῦς· Συνήκατε", "Jesus sagt zu ihnen: Habt ihr verstanden", "NIV, RP")]},
  {"R1": [("Συνήκατε", "Händ er verstande", "WH, Treg, NA28")], "R2": [("Λέγει αὐτοῖς ὁ Ἰησοῦς· Συνήκατε", "De Jesus seit zu ine: Händ er verstande", "NIV, RP")]},
  ["Die Einleitung kann ergänzt worden sein, weil die Frage ohne sie unvermittelt auf die Rede folgt; ebenso kann sie ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne Einleitung, 032 und 04 mit ihr."],
  ["D Iileitig cha ergänzt worde sii, wil d Frag ohni si unvermittlet uf d Red folgt; oder si isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni Iileitig, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-013-051-02:R2", "MAT.13.51", "«Ja.»", "«Ja, Herr.»", "«Ja.»", "«Ja, Herr.»", "gering",
  "Die Jünger reden Jesus mit «Herr» an.", "D Jünger redet de Jesus mit «Herr» aa.",
  {"R1": [("Ναί", "Ja", "WH, Treg, NA28")], "R2": [("Ναί κύριε", "Ja, Herr", "RP")]},
  {"R1": [("Ναί", "Ja", "WH, Treg, NA28")], "R2": [("Ναί κύριε", "Ja, Herr", "RP")]},
  ["Die Anrede kann als ehrerbietige Ergänzung hinzugekommen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 04 und 05 ohne κύριε."],
  ["D Aared cha als ehrerbietigi Ergänzig dezuecho sii.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 04 und 05 ohni κύριε."]),
 ("VAR-SBLGNTAPP-MAT-013-055-02:R2", "MAT.13.55", "Josef", "Joses", "Josef", "Joses", "gering",
  "Der zweite Bruder heisst Joses statt Josef, wie in [[MRK.6.3]].", "De zweit Brüeder heisst Joses statt Josef, wie i [[MRK.6.3]].",
  {"R1": [("Ἰωσήφ", "Josef", "WH, Treg, NA28")], "R2": [("Ἰωσῆς", "Joses", "RP")]},
  {"R1": [("Ἰωσήφ", "Josef", "WH, Treg, NA28")], "R2": [("Ἰωσῆς", "Joses", "RP")]},
  ["Ἰωσῆς kann an [[MRK.6.3]] angeglichen sein; es ist eine Kurzform von Josef. Ebenso kann Ἰωσήφ an den Namen des Vaters erinnern.",
   "Laut der automatischen Zuordnung lesen 03, 04 und die Korrektur von 01 Ἰωσήφ, 032 Ἰωσῆς. Die Erstschrift von 01 und 05 hat die Zuordnung keiner Lesart zugewiesen; nach den CNTR-Transkriptionen steht dort Ἰωάννης (Johannes)."],
  ["Ἰωσῆς cha a [[MRK.6.3]] aaglichen sii; es isch e Churzform vo Josef.",
   "Nach de automatische Zueornig läsed 03, 04 und d Korrektur vo 01 Ἰωσήφ, 032 Ἰωσῆς. D Erschtschrift vo 01 und 05 sind keinere Läsart zuegordnet; nach de CNTR-Transkriptione staat dört Ἰωάννης (Johannes)."]),
 ("VAR-SBLGNTAPP-MAT-013-057-01:R2", "MAT.13.57", "in der Heimat", "in seiner Heimat", "i de Heimet", "i sinere Heimet", "gering",
  "Mit αὐτοῦ ist ausdrücklich seine eigene Heimat genannt.", "Mit αὐτοῦ isch usdrücklich sini eiget Heimet gnännt.",
  {"R1": [("πατρίδι", "Heimat", "WH, Treg, NA28")], "R2": [("πατρίδι αὐτοῦ", "seiner Heimat", "RP")]},
  {"R1": [("πατρίδι", "Heimet", "WH, Treg, NA28")], "R2": [("πατρίδι αὐτοῦ", "sinere Heimet", "RP")]},
  ["Das Fürwort kann an [[MRK.6.4]] angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne αὐτοῦ, 032 und 04 mit ihm."],
  ["S Fürwort cha a [[MRK.6.4]] aaglichen sii.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni αὐτοῦ, 032 und 04 mit."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-013-001-058", "MAT.13.1-MAT.13.58", "section", "Gleichnisse vom Reich der Himmel und Ablehnung in der Heimat",
  ["TU-MAT-013-001-009", "TU-MAT-013-010-017", "TU-MAT-013-018-023", "TU-MAT-013-024-030", "TU-MAT-013-031-035",
   "TU-MAT-013-036-043", "TU-MAT-013-044-052", "TU-MAT-013-053-058"],
  "Jesus sitzt in einem Boot am See und redet zu den Menschenmengen am Ufer in Gleichnissen: vom Sämann, dessen Samen auf den Weg, auf felsigen Boden, unter die Dornen und auf gute Erde fällt. Den Jüngern, die fragen, warum er in Gleichnissen redet, sagt er, ihnen sei gegeben, die Geheimnisse des Reiches der Himmel zu erkennen, jenen nicht, und an jenen erfülle sich die Prophetie des Jesaja ([[ISA.6.9-ISA.6.10]]); dann deutet er ihnen das Gleichnis vom Sämann. Der Menge erzählt er weiter vom Unkraut, das ein Feind unter den Weizen sät und das bis zur Ernte mitwachsen soll, vom Senfkorn und vom Sauerteig; der Erzähler sieht darin ein Prophetenwort erfüllt ([[PSA.78.2]]). Im Haus deutet Jesus den Jüngern das Gleichnis vom Unkraut auf das Gericht bei der Vollendung der Weltzeit, vergleicht das Reich mit einem verborgenen Schatz, mit einem Kaufmann, der eine kostbare Perle findet, und mit einem Netz und spricht vom Schriftgelehrten, der wie ein Hausherr Neues und Altes hervorholt. In seiner Heimat lehrt er in der Synagoge; die Leute staunen, fragen aber, ob er nicht der Sohn des Zimmermanns sei, und nehmen Anstoss an ihm; wegen ihres Unglaubens tut er dort nicht viele Machttaten.", SEG),
 ("TU-MAT-013-001-009", "MAT.13.1-MAT.13.9", "parable", "Das Gleichnis vom Sämann", None,
  "An jenem Tag setzt sich Jesus an den See. Weil sich grosse Menschenmengen bei ihm versammeln, steigt er in ein Boot und setzt sich, während die Menge am Ufer steht, und redet vieles in Gleichnissen. Ein Sämann geht hinaus zu säen: Einiges fällt an den Weg, und die Vögel fressen es; anderes fällt auf felsigen Boden, geht sogleich auf und verdorrt in der Sonne, weil es keine Wurzel hat; anderes fällt unter die Dornen, die es ersticken; anderes fällt auf gute Erde und bringt Frucht, hundert-, sechzig- oder dreissigfach. «Wer Ohren hat, der höre!»", None),
 ("TU-MAT-013-010-017", "MAT.13.10-MAT.13.17", "dialogue", "Warum Jesus in Gleichnissen redet", None,
  "Die Jünger fragen Jesus, warum er in Gleichnissen zu den Leuten redet. Er antwortet, ihnen sei gegeben, die Geheimnisse des Reiches der Himmel zu erkennen, jenen nicht; wer hat, dem wird gegeben, wer nicht hat, dem wird auch genommen, was er hat. Er rede in Gleichnissen zu ihnen, weil sie sehend nicht sehen und hörend nicht hören und nicht verstehen; an ihnen erfülle sich die Prophetie des Jesaja ([[ISA.6.9-ISA.6.10]]). Die Jünger preist er selig, weil ihre Augen sehen und ihre Ohren hören; viele Propheten und Gerechte haben sich danach gesehnt, das zu sehen und zu hören, und haben es nicht gesehen und gehört.", None),
 ("TU-MAT-013-018-023", "MAT.13.18-MAT.13.23", "discourse", "Die Deutung des Gleichnisses vom Sämann", None,
  "Jesus deutet den Jüngern das Gleichnis: Wer das Wort vom Reich hört und nicht versteht, dem raubt der Böse, was in sein Herz gesät ist – das ist der Same am Weg. Wer es sogleich mit Freude aufnimmt, aber keine Wurzel hat, kommt bei Bedrängnis oder Verfolgung zu Fall – das ist der felsige Boden. Bei dem, der unter die Dornen gesät ist, ersticken die Sorge dieser Weltzeit und die Verführung des Reichtums das Wort. Wer das Wort hört und versteht, bringt Frucht, hundert-, sechzig- oder dreissigfach – das ist die gute Erde.", None),
 ("TU-MAT-013-024-030", "MAT.13.24-MAT.13.30", "parable", "Das Unkraut unter dem Weizen", None,
  "Jesus legt ein weiteres Gleichnis vor: Das Reich der Himmel gleicht einem Menschen, der guten Samen auf sein Feld sät; während die Leute schlafen, sät sein Feind Unkraut mitten unter den Weizen. Als sich das Unkraut zeigt, fragen die Knechte den Hausherrn, woher es komme; er antwortet, ein Feind habe das getan. Auf ihre Frage, ob sie es einsammeln sollen, sagt er Nein, damit sie nicht zugleich den Weizen ausreissen: Beides soll bis zur Ernte miteinander wachsen; dann werde er den Schnittern sagen, zuerst das Unkraut zu bündeln und zu verbrennen und den Weizen in seine Scheune zu bringen.", None),
 ("TU-MAT-013-031-035", "MAT.13.31-MAT.13.35", "parable", "Senfkorn und Sauerteig", None,
  "Das Reich der Himmel gleicht einem Senfkorn, das ein Mensch auf sein Feld sät: Es ist kleiner als alle Samen, wird aber grösser als die Gartenkräuter und zu einem Baum, in dessen Zweigen die Vögel des Himmels nisten. Es gleicht auch dem Sauerteig, den eine Frau in drei Mass Mehl verbirgt, bis alles durchsäuert ist. Der Erzähler hält fest, dass Jesus zu den Menschenmengen nur in Gleichnissen redete, damit erfüllt würde, was durch den Propheten gesagt ist ([[PSA.78.2]]).", None),
 ("TU-MAT-013-036-043", "MAT.13.36-MAT.13.43", "discourse", "Die Deutung des Gleichnisses vom Unkraut", None,
  "Jesus entlässt die Menschenmengen und geht ins Haus; die Jünger bitten ihn, ihnen das Gleichnis vom Unkraut zu erklären. Er deutet: Der Sämann ist der Menschensohn, das Feld die Welt, der gute Samen die Söhne des Reiches, das Unkraut die Söhne des Bösen, der Feind der Teufel, die Ernte die Vollendung der Weltzeit, die Schnitter Engel. Wie das Unkraut eingesammelt und verbrannt wird, so wird der Menschensohn bei der Vollendung der Weltzeit seine Engel aussenden; sie werden aus seinem Reich alles einsammeln, was zu Fall bringt, und die, die Gesetzlosigkeit tun, und sie in den Feuerofen werfen. Dann werden die Gerechten im Reich ihres Vaters leuchten wie die Sonne.", None),
 ("TU-MAT-013-044-052", "MAT.13.44-MAT.13.52", "parable", "Schatz, Perle und Netz", None,
  "Jesus redet weiter zu den Jüngern: Das Reich der Himmel gleicht einem im Feld verborgenen Schatz, den ein Mensch findet und verbirgt; in seiner Freude verkauft er alles, was er hat, und kauft das Feld. Es gleicht einem Kaufmann, der eine kostbare Perle findet, alles verkauft und sie kauft. Und es gleicht einem Netz, das Fische aller Art fängt; man liest die guten aus und wirft die unbrauchbaren weg. So werden bei der Vollendung der Weltzeit die Engel die Bösen von den Gerechten scheiden und in den Feuerofen werfen. Auf seine Frage, ob sie das alles verstanden haben, sagen die Jünger Ja. Darauf sagt er, jeder Schriftgelehrte, der für das Reich der Himmel zum Jünger geworden ist, gleiche einem Hausherrn, der aus seinem Schatz Neues und Altes hervorholt.", None),
 ("TU-MAT-013-053-058", "MAT.13.53-MAT.13.58", "narrative", "Ablehnung in der Heimat", None,
  "Nach diesen Gleichnissen zieht Jesus weiter und lehrt in der Synagoge seiner Heimat. Die Leute staunen und fragen, woher er diese Weisheit und die Machttaten habe: Er sei doch der Sohn des Zimmermanns, seine Mutter heisse Maria, seine Brüder Jakobus, Josef, Simon und Judas, und seine Schwestern seien alle bei ihnen. Sie nehmen Anstoss an ihm. Jesus sagt, ein Prophet sei nicht ohne Ehre, ausser in der Heimat und in seinem Haus; wegen ihres Unglaubens tut er dort nicht viele Machttaten.", None),
]
UNITS_GSW = {
 "TU-MAT-013-001-058": ("Gliichnis vom Riich vo de Himel und Ablehnig i de Heimet", "De Jesus sitzt am See i me Boot und redt zu de Lüüt am Ufer i Gliichnis: vom Sämaa, wo sin Same uf de Wäg, uf Felsbode, i d Dörn und uf guet Ärde gheit. De Jünger, wo fröged, werum er i Gliichnis redi, seit er, ine sig ggää, d Gheimnis vom Riich vo de Himel z erchänne, dene andere nöd, und a dene erfülli sich d Prophezeiig vom Jesaja ([[ISA.6.9-ISA.6.10]]); dänn erklärt er ine s Gliichnis vom Sämaa. De Lüüt verzellt er wiiter vom Uchruut, wo en Feind under de Weize sääit und wo bis zur Ärn mitwachse söll, vom Sänfchorn und vom Suurteig; de Erzäler gseht drin es Prophetewort erfüllt ([[PSA.78.2]]). Im Huus erklärt de Jesus de Jünger s Gliichnis vom Uchruut uf s Gricht a de Vollendig vo de Wältziit, vergliicht s Riich mit eme versteckte Schatz, mit eme Chaufmaa, wo e choschtbari Perle findt, und mit eme Netz und redt vom Schriftgelehrte, wo wie en Huusherr Neus und Alts füürenimmt. I sinere Heimet leert er i de Synagoge; d Lüüt stuuned, fröged aber, öb er nöd de Sohn vom Zimmermaa sig, und nämed Aastoss a ihm; wäge irem Unglaube macht er dört nöd vil Chrafttate."),
 "TU-MAT-013-001-009": ("S Gliichnis vom Sämaa", "A dem Tag sitzt de Jesus a de See. Wil sich vil Lüüt bi ihm versammled, stiigt er i es Boot und sitzt ab, während d Mängi am Ufer staat, und redt vil i Gliichnis. En Sämaa gaat go sääje: Öppis gheit a de Wäg, und d Vögel frässed s; anders gheit uf Felsbode, gaat grad uf und verdorret a de Sunne, wil s kei Wurzle hät; anders gheit i d Dörn, und die verstickted s; anders gheit uf guet Ärde und bringt Frucht, hundert-, sächzg- oder drüssgfach. «Wer Ohre hät, dä söll lose!»"),
 "TU-MAT-013-010-017": ("Werum de Jesus i Gliichnis redt", "D Jünger fröged de Jesus, werum er i Gliichnis zu de Lüüt redi. Er antwortet, ine sig ggää, d Gheimnis vom Riich vo de Himel z erchänne, dene nöd; wer hät, däm wird ggää, wer nöd hät, däm wird sogar wäggnoo, won er hät. Er redi i Gliichnis zu ine, wil si mit offne Auge nöd gsehnd und mit offne Ohre nöd ghöred und nöd verstönd; a ine erfülli sich d Prophezeiig vom Jesaja ([[ISA.6.9-ISA.6.10]]). D Jünger priist er sälig, wil iri Auge gsehnd und iri Ohre ghöred; vil Prophete und Grächti händ sich danaa gsehnt, das z gseh und z ghööre, und händ s nöd gseh und nöd ghört."),
 "TU-MAT-013-018-023": ("D Düütig vom Gliichnis vom Sämaa", "De Jesus erklärt de Jünger s Gliichnis: Wer s Wort vom Riich ghört und nöd verstaat, däm riisst de Böös wäg, was i sim Härz gsäät isch – das isch de Same am Wäg. Wer s grad mit Fröid aanimmt, aber kei Wurzle hät, chunnt bi Not oder Verfolgig z Fall – das isch de Felsbode. Bi däm, wo i d Dörn gsäät isch, verstickt d Sorg vo dere Wältziit und d Verfüerig vom Riichtum s Wort. Wer s Wort ghört und verstaat, bringt Frucht, hundert-, sächzg- oder drüssgfach – das isch di guet Ärde."),
 "TU-MAT-013-024-030": ("S Uchruut im Weize", "De Jesus leit es anders Gliichnis vor: S Riich vo de Himel isch wie en Mänsch, wo guete Same uf sis Fäld sääit; während d Lüüt schlafed, sääit sin Feind Uchruut mitten under de Weize. Wo s Uchruut füürechunnt, fröged d Chnächt de Huusherr, vo wo s chömi; er antwortet, en Feind heig das gmacht. Uf iri Frag, öb si s söled zämeläse, seit er Nei, damit si nöd zäme mit em Uchruut de Weize usriissed: Beides söll bis zur Ärn mitenand wachse; dänn wärdi er de Schnitter säge, zerscht s Uchruut z bündle und z verbränne und de Weize i sini Schüür z bringe."),
 "TU-MAT-013-031-035": ("Sänfchorn und Suurteig", "S Riich vo de Himel isch wie es Sänfchorn, wo en Mänsch uf sis Fäld sääit: Es isch chliiner als alli Same, wird aber grösser als d Gartechrüüter und en Baum, i dem sine Äscht d Vögel vom Himel nischted. Es isch au wie Suurteig, wo e Frau i drüü Mass Mehl versteckt, bis alles durgsüüret isch. De Erzäler haltet fescht, dass de Jesus zu de Lüüt nu i Gliichnis gredt hät, damit erfüllt wird, was dur de Prophet gseit worden isch ([[PSA.78.2]])."),
 "TU-MAT-013-036-043": ("D Düütig vom Gliichnis vom Uchruut", "De Jesus laat d Lüüt gaa und gaat is Huus; d Jünger bitted en, ine s Gliichnis vom Uchruut z erkläre. Er düütet: De Sämaa isch de Mänschesohn, s Fäld d Wält, de guet Same d Söhn vom Riich, s Uchruut d Söhn vom Bööse, de Feind de Tüüfel, d Ärn d Vollendig vo de Wältziit, d Schnitter Ängel. Wie mer s Uchruut zämeliist und verbrännt, so wird de Mänschesohn a de Vollendig vo de Wältziit sini Ängel usschicke; die wärded us sim Riich alles zämeläse, was z Fall bringt, und die, wo d Gsetzlosigkeit tüend, und si in Füürofe rüere. Dänn wärded d Grächte im Riich vo irem Vatter lüüchte wie d Sunne."),
 "TU-MAT-013-044-052": ("Schatz, Perle und Netz", "De Jesus redt wiiter zu de Jünger: S Riich vo de Himel isch wie en Schatz, wo im Fäld versteckt isch; en Mänsch findt en und versteckt en, und i sinere Fröid verchauft er alles, won er hät, und chauft s Fäld. Es isch wie en Chaufmaa, wo e choschtbari Perle findt, alles verchauft und si chauft. Und es isch wie es Netz, wo Fisch vo jeder Art fangt; mer liist di guete uus und rüert di unbruuchbare wäg. So wärded a de Vollendig vo de Wältziit d Ängel d Bööse vo de Grächte trenne und in Füürofe rüere. Uf sini Frag, öb si das alles verstande heigid, säged d Jünger Ja. Druf seit er, jede Schriftgelehrte, wo fürs Riich vo de Himel en Jünger worde isch, sig wie en Huusherr, wo us sim Schatz Neus und Alts füürenimmt."),
 "TU-MAT-013-053-058": ("Ablehnig i de Heimet", "Nach dene Gliichnis zieht de Jesus wiiter und leert i de Synagoge vo sinere Heimet. D Lüüt stuuned und fröged, vo wo er die Wiisheit und d Chrafttate heig: Er sig doch de Sohn vom Zimmermaa, sini Mueter heissi Maria, sini Brüeder Jakobus, Josef, Simon und Judas, und sini Schwöschtere sigid alli bi ine. Si nämed Aastoss a ihm. De Jesus seit, en Prophet sig nöd ohni Ehr, usser i de Heimet und i sim Huus; wäge irem Unglaube macht er dört nöd vil Chrafttate."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten in den Alternativen beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1, "
  "Datensatz WREAD-CNTR-MAT-013-001-058) bzw. auf den CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), "
  "nicht auf eigener Prüfung der Handschriften. Wo die automatische Zuordnung den Sigla des SBLGNT-Apparats widerspräche, gälte "
  "der Apparat; in Kapitel 13 stimmen die Ausgaben überein. Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des "
  "SBLGNT-Texts gezählt."),
 ("Einheitliche Begriffe: Die Wiedergabe der wiederkehrenden Matthäus-Begriffe folgt der gemeinsamen Liste für das ganze "
  "Evangelium (u. a. «Reich der Himmel», «Menschensohn», «Amen, ich sage euch», «siehe», «sogleich», «da/dann», «Schriftgelehrte», "
  "die Erfüllungsformel). In Kapitel 13 zusätzlich festgelegt und für die übrigen Kapitel vorgeschlagen: παραβολή «Gleichnis»; "
  "συνίημι «verstehen»; σκανδαλίζω absolut «zu Fall kommen/bringen», mit Bezug auf eine Person «Anstoss nehmen an», σκάνδαλον "
  "«was zu Fall bringt»; μακάριος «selig»; δίκαιος «gerecht»; ὁ πονηρός (Person) «der Böse»; δοῦλος «Knecht»; οἰκοδεσπότης "
  "«Hausherr»; αἰών «Weltzeit», συντέλεια (τοῦ) αἰῶνος «Vollendung der Weltzeit»; ἀνομία «Gesetzlosigkeit»; ὁ κλαυθμὸς καὶ ὁ "
  "βρυγμὸς τῶν ὀδόντων «das Weinen und das Zähneknirschen»; ἡ κάμινος τοῦ πυρός «Feuerofen»; προσέρχομαι «herzutreten, zu ihm "
  "treten»; ὄχλος «Menge», ὄχλοι «Menschenmengen»; θάλασσα (der See Gennesaret) «See»; δύναμις (Tat) «Machttat»; πατρίς «Heimat»; "
  "ὁ ἔχων ὦτα ἀκουέτω «Wer Ohren hat, der höre!»; ὁμοιόω/ὅμοιος in den Gleichnissen «gleicht»; die Schlussformel nach den Reden "
  "«Und es geschah, als Jesus … beendet hatte» ([[MAT.13.53]])."),
 ("Gliederung: Kapitel 13 enthält die Gleichnisrede, nach verbreiteter Gliederung die dritte der fünf grossen Reden des "
  "Evangeliums. Jesus spricht zuerst vom Boot aus zur Menge ([[MAT.13.1]]–[[MAT.13.35]]), dazwischen zu den Jüngern "
  "([[MAT.13.10]]–[[MAT.13.23]]), dann im Haus nur zu den Jüngern ([[MAT.13.36]]–[[MAT.13.52]]). Die Texteinheiten folgen den "
  "Gleichnissen und ihren Deutungen. [[MAT.13.53]]–[[MAT.13.58]] schliesst die Rede ab und eröffnet den folgenden Erzählteil; "
  "die Einheit ist dem Kapitel zugeordnet."),
 ("Redegrenzen: Das Griechische hat keine Anführungszeichen. Jesu Rede im Haus läuft ohne neue Einleitung von [[MAT.13.37]] bis zur "
  "Frage in [[MAT.13.51]]. In [[MAT.13.30]] stehen drei Ebenen (Jesus erzählt, der Hausherr spricht, er zitiert seinen Auftrag an "
  "die Schnitter): « ‹ « » › »."),
 ("Parallelen: [[MRK.4.1-MRK.4.34]] und [[MRK.6.1-MRK.6.6]]. Gleiche griechische Wendungen sind möglichst gleich übersetzt wie "
  "dort; wo Matthäus anders formuliert (z. B. ὅτι statt ἵνα in [[MAT.13.13]], «die Geheimnisse» im Plural, «tat nicht viele» statt "
  "«konnte nicht» in [[MAT.13.58]]), bleibt der Unterschied sichtbar."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT gegen andere Ausgaben liest: in [[MAT.13.22]] τούτου mit RP "
  "gegen WH, Treg und NA28, in [[MAT.13.35]] ohne κόσμου mit WH und Treg gegen NA28 und RP. Abweichende Lesarten stehen als "
  "Alternativen, soweit sie die Übersetzung verändern; Unterschiede in Wortstellung, Schreibweise oder Zeitform ohne Folgen für "
  "die Übersetzung sind nicht aufgenommen. In Kapitel 13 fehlt im SBLGNT kein Vers."),
 ("Befunde ausserhalb des Apparats: In [[MAT.13.35]] las die Erstschrift von 01 nach der CNTR-Transkription «durch den Propheten "
  "Jesaja» (korrigiert). In [[MAT.13.45]] führt die automatische Zuordnung 032 und 04 bei der Lesart ohne ἀνθρώπῳ, obwohl dort nach "
  "den Transkriptionen die Abkürzung ανω steht; die Unsicherheit ist in decisions benannt."),
 "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1, WREAD-CNTR-MAT-013-001-058) "
  "oder uf de CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Einheitlichi Begriff fürs ganz Matthäusevangelium (usfüerlich i de hochtüütsche translation_notes): «s Riich vo de Himel», "
  "«de Mänschesohn», «Amen, ich säg eu», «lueg», «grad», «dänn»; neu i Kapitel 13: παραβολή «Gliichnis»; συνίημι «verstaa»; "
  "σκανδαλίζω «z Fall choo / z Fall bringe», mit Bezug uf e Person «Aastoss nää a»; μακάριος «sälig»; δίκαιος «grächt»; "
  "ὁ πονηρός «de Böös»; δοῦλος «Chnächt»; οἰκοδεσπότης «Huusherr»; αἰών «Wältziit», συντέλεια αἰῶνος «Vollendig vo de Wältziit»; "
  "ἀνομία «Gsetzlosigkeit»; «s Brüele und s Zändchnirsche»; «Füürofe»; προσέρχομαι «härechoo»; ὄχλοι «Lüüt»; δύναμις «Chrafttat»; "
  "πατρίς «Heimet»; ὁ ἔχων ὦτα ἀκουέτω «Wer Ohre hät, dä söll lose!»; ὅμοιος/ὁμοιόω «isch wie»."),
 ("Mundart: Näme mit Artikel («de Jesus»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv («s Riich vo de Himel»). "
  "«Himel» wie im Vaterunser ([[MAT.6.9]]–[[MAT.6.10]])."),
 ("Redegränze: D Red vom Jesus im Huus lauft ohni neui Iileitig vo [[MAT.13.37]] bis zur Frag i [[MAT.13.51]]; i [[MAT.13.30]] "
  "drüü Ebene vo Aafüerigszeiche."),
 "Eigeti Formulierig; nöd us ere veröffentlichte Mundart-Bibel übernoo.",
]


def run():
    import json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _lib import localize  # noqa: E402
    n = 0
    if not (D / "works" / "WORK-MAT.json").exists():
        raise SystemExit("WORK-MAT fehlt")
    for uid, rng, kind, title, parts, summary, seg in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-MAT", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}), "segmentation_note_de": seg,
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        rec = {k: v for k, v in rec.items() if v is not None}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-18; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-mat").glob("*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-MAT-{c:03d}.json")
        refs_c = [f"MAT.{c}.{v}" for v in range(1, last + 1) if f"MAT.{c}.{v}" in toks]
        if len(refs_c) != last:
            raise SystemExit(f"MAT {c}: unerwartet fehlende Verse")
        follows = sorted(f"{vid}:{r['reading_id']}" for vid, v in variants.items() if v["reference"] in refs_c
                         for r in v["readings"] if r.get("is_sblgnt_text"))
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-MAT-{c:03d}-001-{last:03d}-{code}-WORKING"
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
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"MAT.{c}.1-MAT.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Liecht, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Namen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; wiederkehrende Matthäus-Begriffe einheitlich (siehe translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
            aid = f"ALIGN-MAT-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"MAT.{c}.1-MAT.{c}.{last}",
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_13_13.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 13 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
