#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 10–11 (der gute Hirte, Tempelweihfest, Auferweckung des Lazarus, Todesbeschluss) –
Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen,
Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_10_11.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben. Die Grundentscheide zu den johanneischen
Schlüsselwörtern sind in scripts/authoring/johannes_text_01_03.py begründet; diese Datei folgt ihnen.

Besonderheiten:
- [[JHN.10.29]]: Der SBLGNT liest ὃ … μείζων (Holmes); die glatteren Lesarten stehen als Alternativen.
- [[JHN.11.25]]: «und das Leben» fehlt nach der CNTR-Transkription in 𝔓45. Der SBLGNT-Apparat hat dort keinen Eintrag;
  der Befund steht deshalb in decisions und translation_notes, nicht als Lesart-Alternative.

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
BOOK = "JHN"
CHAPTERS = ((10, 42), (11, 57))
SCRIPT = "scripts/authoring/johannes_text_10_11.py"

DE = {
 # ------------------------------------------------------------ Kapitel 10
 "JHN.10.1": "«[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Wer]{5} [nicht]{6} [durch]{8} [die Tür]{9,10} [in]{11} [den Hof]{12,13} [der Schafe]{14,15} [hineingeht]{7}, [sondern]{16} [anderswo]{18} [hinübersteigt]{17}, [der]{19} [ist]{21} [ein Dieb]{20} und{22} [ein Räuber]{23}.",
 "JHN.10.2": "[Wer]{1} [aber]{2} [durch]{4} [die Tür]{5,6} [hineingeht]{3}, [ist]{8} [Hirte]{7} [der Schafe]{9,10}.",
 "JHN.10.3": "[Ihm]{1} [öffnet]{4} [der Türhüter]{2,3}, und{5} [die Schafe]{6,7} [hören]{11} auf [seine]{10} [Stimme]{8,9}, und{12} [er ruft]{16} [die eigenen]{13,14} [Schafe]{15} [mit]{17} [Namen]{18} und{19} [führt]{20} [sie]{21} [hinaus]{20}.",
 "JHN.10.4": "[Wenn]{1} [er]{5} [alle]{4} [seine eigenen]{2,3} [hinausgetrieben hat]{5}, [geht er]{8} [vor]{6} [ihnen]{7} [her]{6}, und{9} [die Schafe]{10,11} [folgen]{13} [ihm]{12}, [denn]{14} [sie kennen]{15} [seine]{18} [Stimme]{16,17}.",
 "JHN.10.5": "[Einem Fremden]{1} [aber]{2} [werden sie]{5} [gewiss nicht]{3,4} [folgen]{5}, [sondern]{6} [sie werden]{7} [vor]{8} [ihm]{9} [fliehen]{7}, [denn]{10} [sie kennen]{12} [die Stimme]{15,16} [der Fremden]{13,14} [nicht]{11}.»",
 "JHN.10.6": "[Dieses]{1} [Bildwort]{2,3} [sagte]{4} [Jesus]{6,7} [zu ihnen]{5}; [jene]{8} [aber]{9} [verstanden]{11} [nicht]{10}, [was]{12} es [war]{13}, [das]{14} [er]{15} [zu ihnen]{16} [redete]{15}.",
 "JHN.10.7": "[Da]{2} [sagte]{1} [Jesus]{5,6} [wieder]{3} [zu ihnen]{4}: «[Amen]{7}, [amen]{8}, [ich sage]{9} [euch]{10}: [Ich]{12} [bin]{13} [die Tür]{14,15} [der Schafe]{16,17}. ~11(ὅτι leitet die direkte Rede ein)",
 "JHN.10.8": "[Alle]{1}, [die]{2} [vor]{4} [mir]{5} [gekommen sind]{3}, [sind]{7} [Diebe]{6} und{8} [Räuber]{9}; [aber]{10} [die Schafe]{14,15} [haben]{12} [nicht]{11} [auf sie]{13} [gehört]{12}.",
 "JHN.10.9": "[Ich]{1} [bin]{2} [die Tür]{3,4}. [Wenn]{7} [jemand]{8} [durch]{5} [mich]{6} [hineingeht]{9}, [wird er gerettet werden]{10}, und{11} [er wird hineingehen]{12} und{13} [hinausgehen]{14} und{15} [Weide]{16} [finden]{17}.",
 "JHN.10.10": "[Der Dieb]{1,2} [kommt]{4} [nur]{3,5,6}, [um]{7} [zu stehlen]{8} und{9} [zu schlachten]{10} und{11} [zu vernichten]{12}. [Ich]{13} [bin gekommen]{14}, [damit]{15} [sie]{17} [Leben]{16} [haben]{17} und{18} [Überfluss]{19} [haben]{20}.",
 "JHN.10.11": "[Ich]{1} [bin]{2} [der gute Hirte]{3-6}. [Der gute Hirte]{7-10} [gibt]{14} [sein]{13} [Leben]{11,12} [hin]{14} [für]{15} [die Schafe]{16,17}.",
 "JHN.10.12": "[Der Lohnarbeiter]{1,2}, [der]{5} [nicht]{4} [Hirte]{6} [ist]{5} und{3} [dem]{7} [die Schafe]{10,11} [nicht]{8} [gehören]{9,12}, [sieht]{13} [den Wolf]{14,15} [kommen]{16} und{17} [lässt]{18} [die Schafe]{19,20} [im Stich]{18} und{21} [flieht]{22} – und{23} [der Wolf]{24,25} [reisst]{26} und{28} [zerstreut]{29} [sie]{27} –,",
 "JHN.10.13": "[denn]{1} [er ist]{3} [ein Lohnarbeiter]{2}, und{4} [ihm]{7} [liegt]{6} [nichts]{5} [an]{8} [den Schafen]{9,10}.",
 "JHN.10.14": "[Ich]{1} [bin]{2} [der gute Hirte]{3-6}, und{7} [ich kenne]{8} [die Meinen]{9,10}, und{11} [die Meinen]{14,15} [kennen]{12} [mich]{13},",
 "JHN.10.15": "[wie]{1} [der Vater]{4,5} [mich]{3} [kennt]{2} [und ich]{6} [den Vater]{8,9} [kenne]{7}; und{10} [ich gebe]{14} [mein]{13} [Leben]{11,12} [hin]{14} [für]{15} [die Schafe]{16,17}.",
 "JHN.10.16": "Und{1} [ich habe]{4} [andere]{2} [Schafe]{3}, [die]{5} [nicht]{6} [aus]{8} [diesem]{11} [Hof]{9,10} [sind]{7}; [auch sie]{12} [muss]{13} [ich]{14} [führen]{15}, und{16} [sie werden]{20} auf [meine]{19} [Stimme]{17,18} [hören]{20}, und{21} [sie werden]{22} [eine]{23} [Herde]{24} [werden]{22}, [ein]{25} [Hirte]{26}.",
 "JHN.10.17": "[Darum]{1,2} [liebt]{6} [mich]{3} [der Vater]{4,5}, [weil]{7} [ich]{8} [mein]{12} [Leben]{10,11} [hingebe]{9}, [um]{13} [es]{16} [wieder]{14} [zu nehmen]{15}.",
 "JHN.10.18": "[Niemand]{1} [nimmt]{2} [es]{3} [mir]{4,5} [weg]{2}, [sondern]{6} [ich]{7} [gebe]{8} [es]{9} [von mir aus]{10,11} [hin]{8}. [Ich habe]{13} [Vollmacht]{12}, [es]{15} [hinzugeben]{14}, und{16} [ich habe]{18} [Vollmacht]{17}, [es]{21} [wieder]{19} [zu nehmen]{20}. [Diesen]{22} [Auftrag]{23,24} [habe ich]{25} [von]{26} [meinem]{29} [Vater]{27,28} [empfangen]{25}.»",
 "JHN.10.19": "[Wieder]{2} [entstand]{3} [eine Spaltung]{1} [unter]{4} [den Juden]{5,6} [wegen]{7} [dieser]{10} [Worte]{8,9}.",
 "JHN.10.20": "[Viele]{3} [von]{4} [ihnen]{5} [aber]{2} [sagten]{1}: «[Er hat]{7} [einen Dämon]{6} und{8} [ist von Sinnen]{9}. [Warum]{10} [hört ihr]{12} [auf ihn]{11}?»",
 "JHN.10.21": "[Andere]{1} [sagten]{2}: «[Das]{3} [sind]{7} [nicht]{6} [die Worte]{4,5} [eines Besessenen]{8}. [Kann]{11} [etwa]{9} [ein Dämon]{10} [Blinden]{12} [die Augen]{13} [öffnen]{14}?»",
 "JHN.10.22": "[Damals]{2} [fand]{1} [in]{5} [Jerusalem]{6,7} [das Fest der Tempelweihe]{3,4} [statt]{1}; [es war]{9} [Winter]{8}.",
 "JHN.10.23": "Und{1} [Jesus]{3,4} [ging]{2} [im]{5,6} [Tempel]{7} [umher]{2}, [in]{8} [der Säulenhalle]{9,10} [Salomos]{11,12}.",
 "JHN.10.24": "[Da]{2} [umringten]{1} [ihn]{3} [die Juden]{4,5} und{6} [sagten]{7} [zu ihm]{8}: «[Wie lange]{9,10} [hältst du uns hin]{11-14:idiom}? [Wenn]{15} [du]{16} [der Christus]{18,19} [bist]{17}, [sag es]{20} [uns]{21} [offen]{22}!»",
 "JHN.10.25": "[Jesus]{3,4} [antwortete]{1} [ihnen]{2}: «[Ich habe es]{5} [euch]{6} [gesagt]{5}, und{7} [ihr glaubt]{9} [nicht]{8}. [Die Werke]{10,11}, [die]{12} [ich]{13} [im]{15,16} [Namen]{17} [meines]{20} [Vaters]{18,19} [tue]{14}, [diese]{21} [zeugen]{22} [von]{23} [mir]{24}.",
 "JHN.10.26": "[Aber]{1} [ihr]{2} [glaubt]{4} [nicht]{3}, [weil]{5} [ihr]{7} [nicht]{6} [zu]{8} [meinen]{11,12} [Schafen]{9,10} [gehört]{7}.",
 "JHN.10.27": "[Meine]{3,4} [Schafe]{1,2} [hören]{8} auf [meine]{7} [Stimme]{5,6}, [und ich]{9} [kenne]{10} [sie]{11}, und{12} [sie folgen]{13} [mir]{14}.",
 "JHN.10.28": "[Und ich]{1} [gebe]{2} [ihnen]{3} [ewiges]{5} [Leben]{4}, und{6} [sie werden]{9} [in Ewigkeit]{10-12} [gewiss nicht]{7,8} [verloren gehen]{9}, und{13} [niemand]{14,16} [wird]{15} [sie]{17} [aus]{18} [meiner]{21} [Hand]{19,20} [reissen]{15}.",
 "JHN.10.29": "[Mein]{3} [Vater]{1,2} – [was]{4} er [mir]{6} [gegeben hat]{5} – [ist]{9} [grösser]{8} [als alle]{7}, und{10} [niemand]{11} [kann]{12} sie [aus]{14} [der Hand]{15,16} [des Vaters]{17,18} [reissen]{13}.",
 "JHN.10.30": "[Ich]{1} und{2} [der Vater]{3,4} [sind]{6} [eins]{5}.»",
 "JHN.10.31": "[Da]{2} [hoben]{1} [die Juden]{5,6} [wieder]{3} [Steine]{4} [auf]{1}, [um]{7} [ihn]{9} [zu steinigen]{8}.",
 "JHN.10.32": "[Jesus]{3,4} [antwortete]{1} [ihnen]{2}: «[Viele]{5} [gute]{7} [Werke]{6} [habe ich]{8} [euch]{9} [gezeigt]{8}, [vom]{10,11} [Vater]{12} her. [Für]{13} [welches]{14} [dieser]{15} [Werke]{16} [steinigt ihr]{18} [mich]{17}?»",
 "JHN.10.33": "[Die Juden]{3,4} [antworteten]{1} [ihm]{2}: «[Wegen]{5} [eines guten]{6} [Werkes]{7} [steinigen wir]{9} [dich]{10} [nicht]{8}, [sondern]{11} [wegen]{12} [Lästerung]{13}, und{14} [weil]{15} [du]{16}, [der du]{18} [ein Mensch]{17} [bist]{18}, [dich selbst]{20} [zu Gott]{21} [machst]{19}.»",
 "JHN.10.34": "[Jesus]{3,4} [antwortete]{1} [ihnen]{2}: «[Steht]{6} [nicht]{5} [in]{8} [eurem]{11} [Gesetz]{9,10} [geschrieben]{7}: ‹[Ich]{13} [habe gesagt]{14}: [Ihr seid]{16} [Götter]{15}›? ~12(ὅτι leitet das Zitat ein)",
 "JHN.10.35": "[Wenn]{1} [er]{3} [jene]{2} [Götter]{4} [genannt hat]{3}, [an]{5} [die]{6} [das Wort]{7,8} [Gottes]{9,10} [erging]{11} – und{12} [die Schrift]{16,17} [kann]{14} [nicht]{13} [aufgehoben werden]{15} –,",
 "JHN.10.36": "[sagt]{11} [ihr]{10} dann [von dem]{1}, den [der Vater]{2,3} [geheiligt]{4} und{5} [in]{7} [die Welt]{8,9} [gesandt hat]{6}: ‹[Du lästerst]{13}›, [weil]{14} [ich gesagt habe]{15}: ‹[Ich bin]{19} [Gottes]{17,18} [Sohn]{16}›? ~12(ὅτι leitet die direkte Rede ein)",
 "JHN.10.37": "[Wenn]{1} [ich]{3} [die Werke]{4,5} [meines]{8} [Vaters]{6,7} [nicht]{2} [tue]{3}, [dann glaubt]{10} [mir]{11} [nicht]{9}.",
 "JHN.10.38": "[Wenn]{1} [ich sie]{3} [aber]{2} [tue]{3}, [so glaubt]{10} [den Werken]{8,9}, [auch wenn]{4} [ihr]{7} [mir]{5} [nicht]{6} [glaubt]{7}, [damit]{11} [ihr erkennt]{12} und{13} [immer mehr erkennt]{14}, [dass]{15} [der Vater]{18,19} [in]{16} [mir]{17} ist [und ich]{20} [im]{21,22} [Vater]{23}.»",
 "JHN.10.39": "[Da]{2} [suchten sie]{1} [ihn]{4} [wieder]{3} [festzunehmen]{5}; und{6} [er entkam]{7} [aus]{8} [ihrer]{11} [Hand]{9,10}.",
 "JHN.10.40": "Und{1} [er ging]{2} [wieder]{3} [weg]{2}, [auf die andere Seite]{4} [des Jordan]{5,6}, [an]{7} [den Ort]{8,9}, [wo]{10} [Johannes]{12} [zuerst]{13,14} [getauft hatte]{11,15}, und{16} [er blieb]{17} [dort]{18}.",
 "JHN.10.41": "Und{1} [viele]{2} [kamen]{3} [zu]{4} [ihm]{5} und{6} [sagten]{7}: «[Johannes]{9} [hat]{12} [zwar]{10} [kein]{13} [Zeichen]{11} [getan]{12}, [aber]{15} [alles]{14}, [was]{16} [Johannes]{18} [über]{19} [diesen]{20} [gesagt hat]{17}, [war]{22} [wahr]{21}.» ~8(ὅτι leitet die direkte Rede ein)",
 "JHN.10.42": "Und{1} [viele]{2} [glaubten]{3} [dort]{6} [an]{4} [ihn]{5}.",
 # ------------------------------------------------------------ Kapitel 11
 "JHN.11.1": "[Es war]{1} [aber]{2} [einer]{3} [krank]{4}, [Lazarus]{5} [aus]{6} [Betanien]{7}, [aus]{8} [dem Dorf]{9,10} [Marias]{11} und{12} [ihrer]{16} [Schwester]{14,15} [Marta]{13}.",
 "JHN.11.2": "[Maria]{3} [aber]{2} [war]{1} [die]{4}, die [den Herrn]{6,7} [mit Salböl]{8} [gesalbt]{5} und{9} [seine]{13} [Füsse]{11,12} [mit ihren]{14,16} [Haaren]{15} [abgetrocknet hatte]{10}; [deren]{17} [Bruder]{18,19} [Lazarus]{20} [war krank]{21}.",
 "JHN.11.3": "[Da]{2} [sandten]{1} [die Schwestern]{3,4} [zu]{5} [ihm]{6} [und liessen sagen]{7}: «[Herr]{8}, [sieh]{9}, der, [den]{10} [du lieb hast]{11}, [ist krank]{12}.»",
 "JHN.11.4": "[Als]{1} [Jesus]{3,4} das [aber]{2} [hörte]{1}, [sagte er]{5}: «[Diese]{6} [Krankheit]{7,8} [führt]{10} [nicht]{9} [zum]{11} [Tod]{12}, [sondern]{13} [sie dient]{14} [der Herrlichkeit]{15,16} [Gottes]{17,18}, [damit]{19} [der Sohn]{21,22} [Gottes]{23,24} [durch]{25} [sie]{26} [verherrlicht wird]{20}.»",
 "JHN.11.5": "[Jesus]{3,4} [aber]{2} [liebte]{1} [Marta]{5,6} und{7} [ihre]{10} [Schwester]{8,9} und{11} [Lazarus]{12,13}.",
 "JHN.11.6": "[Als]{1} [er]{3} [nun]{2} [hörte]{3}, [dass]{4} [er krank sei]{5}, [blieb er]{8} [da]{6} [noch]{7} [zwei]{13} [Tage]{14} [an]{9} [dem Ort]{12}, [wo]{10} [er war]{11}.",
 "JHN.11.7": "[Erst]{1} [danach]{2,3} [sagt er]{4} [zu den Jüngern]{5,6}: «[Lasst uns]{7} [wieder]{11} [nach]{8} [Judäa]{9,10} [gehen]{7}!»",
 "JHN.11.8": "[Die Jünger]{3,4} [sagen]{1} [zu ihm]{2}: «[Rabbi]{5}, [eben noch]{6} [suchten]{7} [die Juden]{10,11} [dich]{8} [zu steinigen]{9}, und{12} [du gehst]{14} [wieder]{13} [dorthin]{15}?»",
 "JHN.11.9": "[Jesus]{2} [antwortete]{1}: «[Hat]{6} [der Tag]{7,8} [nicht]{3} [zwölf]{4} [Stunden]{5}? [Wenn]{9} [jemand]{10} [am]{12,13} [Tag]{14} [umhergeht]{11}, [stösst er]{16} [nicht]{15} [an]{16}, [denn]{17} [er sieht]{23} [das Licht]{18,19} [dieser]{22} [Welt]{20,21}.",
 "JHN.11.10": "[Wenn]{1} [aber]{2} [jemand]{3} [in]{5} [der Nacht]{6,7} [umhergeht]{4}, [stösst er an]{8}, [denn]{9} [das Licht]{10,11} [ist]{13} [nicht]{12} [in]{14} [ihm]{15}.»",
 "JHN.11.11": "[Das]{1} [sagte er]{2}, und{3} [danach]{4,5} [sagt er]{6} [zu ihnen]{7}: «[Lazarus]{8}, [unser]{11} [Freund]{9,10}, [ist eingeschlafen]{12}; [aber]{13} [ich gehe hin]{14}, [um]{15} [ihn]{17} [aufzuwecken]{16}.»",
 "JHN.11.12": "[Da]{2} [sagten]{1} [die Jünger]{3,4} [zu ihm]{5}: «[Herr]{6}, [wenn]{7} [er eingeschlafen ist]{8}, [wird er gesund werden]{9}.»",
 "JHN.11.13": "[Jesus]{3,4} [hatte]{1} [aber]{2} [von]{5} [seinem]{8} [Tod]{6,7} [gesprochen]{1}; [jene]{9} [aber]{10} [meinten]{11}, [dass]{12} [er]{18} [vom]{13,14} [Ruhen]{15} [im Schlaf]{16,17} [rede]{18}.",
 "JHN.11.14": "[Da]{1} [sagte]{3} [Jesus]{5,6} [ihnen]{4} [nun]{2} [offen]{7}: «[Lazarus]{8} [ist gestorben]{9},",
 "JHN.11.15": "und{1} [ich freue mich]{2} [euretwegen]{3,4}, [dass]{7} [ich]{9} [nicht]{8} [dort]{10} [war]{9}, [damit]{5} [ihr glaubt]{6}. [Aber]{11} [lasst uns]{12} [zu]{13} [ihm]{14} [gehen]{12}!»",
 "JHN.11.16": "[Da]{2} [sagte]{1} [Thomas]{3}, [der]{4} [Didymus]{6} [genannt wird]{5}, [zu den Mitjüngern]{7,8}: «[Lasst]{9} [auch]{10} [uns]{11} [gehen]{9}, [damit]{12} [wir]{13} [mit]{14} [ihm]{15} [sterben]{13}!»",
 "JHN.11.17": "[Als]{1} [Jesus]{3,4} [nun]{2} [ankam]{1}, [fand er]{5}, [dass er]{6} [schon]{8} [vier]{7} [Tage]{9} [im]{11,12} [Grab]{13} [lag]{10}.",
 "JHN.11.18": "[Betanien]{3,4} [lag]{1} [aber]{2} [nahe]{5} [bei Jerusalem]{6,7}, [etwa]{8} [fünfzehn]{11} [Stadien]{10} [entfernt]{9}.",
 "JHN.11.19": "[Viele]{1} [von]{3} [den Juden]{4,5} [aber]{2} [waren]{6} [zu]{7} [Marta]{8,9} und{10} [Maria]{11} [gekommen]{6}, [um]{12} [sie]{14} [wegen]{15} [des Bruders]{16,17} [zu trösten]{13}.",
 "JHN.11.20": "[Als]{4} [Marta]{1,3} [nun]{2} [hörte]{5}, [dass]{6} [Jesus]{7} [komme]{8}, [ging sie]{9} [ihm]{10} [entgegen]{9}; [Maria]{11} [aber]{12} [blieb]{16} [im]{13,14} [Haus]{15} [sitzen]{16}.",
 "JHN.11.21": "[Da]{2} [sagte]{1} [Marta]{3,4} [zu]{5} [Jesus]{6,7}: «[Herr]{8}, [wenn]{9} [du]{10} [hier]{11} [gewesen wärst]{10}, [wäre]{13} [mein]{17} [Bruder]{15,16} [nicht]{12} [gestorben]{14}.",
 "JHN.11.22": "Und{1} [auch jetzt]{2} [weiss ich]{3}, [dass]{4} [Gott]{12,13} [dir]{11} [geben wird]{10}, [was]{5} [immer]{6} [du]{7} [von Gott]{8,9} [erbittest]{7}.»",
 "JHN.11.23": "[Jesus]{3,4} [sagt]{1} [zu ihr]{2}: «[Dein]{8} [Bruder]{6,7} [wird auferstehen]{5}.»",
 "JHN.11.24": "[Marta]{3,4} [sagt]{1} [zu ihm]{2}: «[Ich weiss]{5}, [dass]{6} [er auferstehen wird]{7} [bei]{8} [der Auferstehung]{9,10} [am]{11,12} [letzten]{13} [Tag]{14}.»",
 "JHN.11.25": "[Jesus]{3,4} [sagte]{1} [zu ihr]{2}: «[Ich]{5} [bin]{6} [die Auferstehung]{7,8} und{9} [das Leben]{10,11}. [Wer]{12} [an]{14} [mich]{15} [glaubt]{13}, [wird leben]{18}, [auch wenn]{16} [er stirbt]{17};",
 "JHN.11.26": "und{1} [jeder]{2}, [der]{3} [lebt]{4} und{5} [an]{7} [mich]{8} [glaubt]{6}, [wird]{11} [in Ewigkeit]{12-14} [gewiss nicht]{9,10} [sterben]{11}. [Glaubst du]{15} [das]{16}?»",
 "JHN.11.27": "[Sie sagt]{1} [zu ihm]{2}: «[Ja]{3}, [Herr]{4}, [ich]{5} [glaube]{6}, [dass]{7} [du]{8} [der Christus]{10,11} [bist]{9}, [der Sohn]{12,13} [Gottes]{14,15}, [der]{16} [in]{17} [die Welt]{18,19} [kommt]{20}.»",
 "JHN.11.28": "Und{1} [als sie]{3} [das]{2} [gesagt hatte]{3}, [ging sie weg]{4} und{5} [rief]{6} [heimlich]{11} [ihre]{10} [Schwester]{8,9} [Maria]{7} [und sagte]{12}: «[Der Lehrer]{13,14} [ist da]{15} und{16} [ruft]{17} [dich]{18}.»",
 "JHN.11.29": "[Als]{3} [sie]{1} [aber]{2} [das hörte]{4}, [stand sie]{5} [schnell]{6} [auf]{5} und{7} [ging]{8} [zu]{9} [ihm]{10}.",
 "JHN.11.30": "[Jesus]{4,5} [war]{3} [aber]{2} [noch nicht]{1} [in]{6} [das Dorf]{7,8} [gekommen]{3}, [sondern]{9} [er war]{10} [noch]{11} [an]{12} [dem Ort]{13,14}, [wo]{15} [Marta]{18,19} [ihm]{17} [entgegengekommen war]{16}.",
 "JHN.11.31": "[Die Juden]{1,3} [nun]{2}, [die]{4} [bei]{6} [ihr]{7} [im]{8,9} [Haus]{10} [waren]{5} und{11} [sie]{13} [trösteten]{12}, [sahen]{14}, [dass]{17} [Maria]{15,16} [schnell]{18} [aufstand]{19} und{20} [hinausging]{21}; [sie folgten]{22} [ihr]{23}, [weil sie meinten]{24}, [dass]{25} [sie]{26} [zum]{27,28} [Grab]{29} [gehe]{26}, [um]{30} [dort]{32} [zu weinen]{31}.",
 "JHN.11.32": "[Als]{4} [Maria]{1,3} [nun]{2} [dorthin kam]{5}, [wo]{6} [Jesus]{8} [war]{7}, und [ihn]{10} [sah]{9}, [fiel sie]{11} [ihm]{12} [zu]{13} [Füssen]{14,15} [und sagte]{16} [zu ihm]{17}: «[Herr]{18}, [wenn]{19} [du]{20} [hier]{21} [gewesen wärst]{20}, [wäre]{23} [mein]{24} [Bruder]{26,27} [nicht]{22} [gestorben]{25}.»",
 "JHN.11.33": "[Als]{3} [Jesus]{1} [nun]{2} [sah]{4}, wie [sie]{5} [weinte]{6} und{7} wie [die Juden]{8,11} [weinten]{12}, die [mit ihr]{10} [gekommen waren]{9}, [wurde er]{13} [im]{14} [Geist]{15} [zornig erregt]{13} und{16} [erschütterte]{17} [sich]{18}",
 "JHN.11.34": "und{1} [sagte]{2}: «[Wo]{3} [habt ihr]{4} [ihn]{5} [hingelegt]{4}?» [Sie sagen]{6} [zu ihm]{7}: «[Herr]{8}, [komm]{9} und{10} [sieh]{11}!»",
 "JHN.11.35": "[Jesus]{2,3} [weinte]{1}.",
 "JHN.11.36": "[Da]{2} [sagten]{1} [die Juden]{3,4}: «[Seht]{5}, [wie]{6} [lieb er]{7} [ihn]{8} [hatte]{7}!»",
 "JHN.11.37": "[Einige]{1} [von]{3} [ihnen]{4} [aber]{2} [sagten]{5}: «[Konnte]{7} [dieser]{8}, [der]{9} [dem Blinden]{13,14} [die Augen]{11,12} [geöffnet hat]{10}, [nicht]{6} [bewirken]{15}, [dass]{16} [auch]{17} [dieser]{18} [nicht]{19} [stürbe]{20}?»",
 "JHN.11.38": "[Da]{2} [kommt]{7} [Jesus]{1}, [wieder]{3} [innerlich]{5,6} [zornig erregt]{4}, [zum]{8,9} [Grab]{10}. [Es war]{11} [aber]{12} [eine Höhle]{13}, und{14} [ein Stein]{15} [lag]{16} [darauf]{17,18}.",
 "JHN.11.39": "[Jesus]{2,3} [sagt]{1}: «[Nehmt]{4} [den Stein]{5,6} [weg]{4}!» [Marta]{13}, [die Schwester]{9,10} [des Verstorbenen]{11,12}, [sagt]{7} [zu ihm]{8}: «[Herr]{14}, [er riecht]{16} [schon]{15}; [denn]{18} [es ist]{19} [der vierte Tag]{17}.»",
 "JHN.11.40": "[Jesus]{3,4} [sagt]{1} [zu ihr]{2}: «[Habe ich]{6} [dir]{7} [nicht]{5} [gesagt]{6}: [Wenn]{9} [du glaubst]{10}, [wirst du]{11} [die Herrlichkeit]{12,13} [Gottes]{14,15} [sehen]{11}?» ~8(ὅτι leitet die direkte Rede ein)",
 "JHN.11.41": "[Da]{2} [nahmen sie]{1} [den Stein]{3,4} [weg]{1}. [Jesus]{5,7} [aber]{6} [hob]{8} [die Augen]{9,10} [empor]{11} und{12} [sagte]{13}: «[Vater]{14}, [ich danke]{15} [dir]{16}, [dass]{17} [du]{18} [mich]{19} [erhört hast]{18}.",
 "JHN.11.42": "[Ich]{1} [aber]{2} [wusste]{3}, [dass]{4} [du]{7} [mich]{6} [immer]{5} [erhörst]{7}; [aber]{8} [wegen]{9} [der Menge]{10,11}, [die]{12} [herumsteht]{13}, [habe ich es gesagt]{14}, [damit]{15} [sie glauben]{16}, [dass]{17} [du]{18} [mich]{19} [gesandt hast]{20}.»",
 "JHN.11.43": "Und{1} [als er]{3} [das]{2} [gesagt hatte]{3}, [rief er]{6} [mit lauter]{5} [Stimme]{4}: «[Lazarus]{7}, [komm]{8} [heraus]{9}!»",
 "JHN.11.44": "[Der Tote]{2,3} [kam heraus]{1}, [an]{5} [Füssen]{6} und{7} [Händen]{8,9} [mit Binden]{10} [umwickelt]{4}, und{11} [sein]{14} [Gesicht]{12,13} [war]{16} [mit einem Schweisstuch]{15} [umbunden]{16}. [Jesus]{19,20} [sagt]{17} [zu ihnen]{18}: «[Bindet]{21} [ihn]{22} [los]{21} und{23} [lasst]{24} [ihn]{25} [gehen]{26}!»",
 "JHN.11.45": "[Viele]{1} [nun]{2} [von]{3} [den Juden]{4,5}, [die]{6} [zu]{8} [Maria]{9,10} [gekommen waren]{7} und{11} [gesehen hatten]{12}, [was]{13} [er getan hatte]{14}, [glaubten]{15} [an]{16} [ihn]{17}.",
 "JHN.11.46": "[Einige]{1} [von]{3} [ihnen]{4} [aber]{2} [gingen]{5} [zu]{6} [den Pharisäern]{7,8} und{9} [sagten]{10} [ihnen]{11}, [was]{12} [Jesus]{14} [getan hatte]{13}.",
 "JHN.11.47": "[Da]{2} [beriefen]{1} [die Hohepriester]{3,4} und{5} [die Pharisäer]{6,7} [eine Sitzung des Hohen Rates]{8} [ein]{1} und{9} [sagten]{10}: «[Was]{11} [sollen wir tun]{12}? [Denn]{13} [dieser]{14} [Mensch]{15,16} [tut]{18} [viele]{17} [Zeichen]{19}.",
 "JHN.11.48": "[Wenn]{1} [wir]{2} [ihn]{3} [so]{4} [gewähren lassen]{2}, [werden]{6} [alle]{5} [an]{7} [ihn]{8} [glauben]{6}, und{9} [die Römer]{11,12} [werden kommen]{10} und{13} [uns]{15} [sowohl]{16} [den Ort]{17,18} [als auch]{19} [die Nation]{20,21} [wegnehmen]{14}.»",
 "JHN.11.49": "[Einer]{1,3} [von]{4} [ihnen]{5} [aber]{2}, [Kajafas]{6}, [der]{8} [in jenem]{9,11} [Jahr]{10} [Hohepriester]{7} [war]{8}, [sagte]{12} [zu ihnen]{13}: «[Ihr]{14} [wisst]{16} [gar nichts]{15,17}",
 "JHN.11.50": "[und bedenkt]{2} [auch nicht]{1}, [dass]{3} es [besser]{4} [für euch]{5} [ist]{4}, [dass]{6} [ein]{7} [Mensch]{8} [für]{10} [das Volk]{11,12} [stirbt]{9} und{13} [nicht]{14} [die ganze]{15,16} [Nation]{17} [zugrunde geht]{18}.»",
 "JHN.11.51": "[Das]{1} [sagte er]{6} [aber]{2} [nicht]{5} [von sich aus]{3,4}, [sondern]{7} [als]{9} [Hohepriester]{8} [jenes]{10,12} [Jahres]{11} [weissagte er]{13}, [dass]{14} [Jesus]{16} [für]{18} [die Nation]{19,20} [sterben]{17} [werde]{15},",
 "JHN.11.52": "und{1} [nicht]{2} [für]{3} [die Nation]{4,5} [allein]{6}, [sondern]{7} [um]{8} [auch]{9} [die zerstreuten]{14,15} [Kinder]{10,11} [Gottes]{12,13} [zu einer Einheit]{17,18} [zusammenzuführen]{16}.",
 "JHN.11.53": "[Von]{1} [jenem]{2,4} [Tag]{5} [an]{1} [nun]{3} [planten sie]{6}, [ihn]{9} [zu töten]{7,8}.",
 "JHN.11.54": "[Jesus]{1,3} [nun]{2} [ging]{6} [nicht mehr]{4} [offen]{5} [unter]{7} [den Juden]{8,9} [umher]{6}, [sondern]{10} [zog]{11} [von dort]{12} [weg]{11} [in]{13} [die Gegend]{14,15} [nahe]{16} [der Wüste]{17,18}, [in]{19} [eine Stadt]{22}, die [Efraim]{20} [heisst]{21}, [und dort]{23} [blieb er]{24} [mit]{25} [den Jüngern]{26,27}.",
 "JHN.11.55": "[Das Passa]{4,5} [der Juden]{6,7} [aber]{2} [war]{1} [nahe]{3}, und{8} [viele]{10} [zogen]{9} [vor]{16} [dem Passa]{17,18} [aus]{13} [dem Land]{14,15} [nach]{11} [Jerusalem]{12} [hinauf]{9}, [um]{19} [sich]{21} [zu reinigen]{20}.",
 "JHN.11.56": "[Sie suchten]{1} [nun]{2} [Jesus]{3,4} und{5} [sagten]{6} [zueinander]{7,8}, [während sie]{12} [im]{9,10} [Tempel]{11} [standen]{12}: «[Was]{13} [meint]{14} [ihr]{15}? [Dass]{16} [er]{19} [gewiss nicht]{17,18} [zum]{20,21} [Fest]{22} [kommt]{19}?»",
 "JHN.11.57": "[Die Hohepriester]{3,4} und{5} [die Pharisäer]{6,7} [hatten]{1} [aber]{2} [Anweisungen]{8} [gegeben]{1}, [dass]{9}, [wenn]{10} [jemand]{11} [erfahre]{12}, [wo]{13} [er sei]{14}, [er es melden solle]{15}, [damit]{16} [sie]{17} [ihn]{18} [festnehmen könnten]{17}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 10
 "JHN.10.1": "«[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Wer]{5} [nöd]{6} [dur]{8} [d Tüür]{9,10} [in]{11} [de Hof]{12,13} [vo de Schaaf]{14,15} [ine gaat]{7}, [sondern]{16} [anderswo]{18} [übere stiigt]{17}, [dä]{19} [isch]{21} [en Dieb]{20} und{22} [en Röiber]{23}.",
 "JHN.10.2": "[Wer]{1} [aber]{2} [dur]{4} [d Tüür]{5,6} [ine gaat]{3}, [isch]{8} [Hirt]{7} [vo de Schaaf]{9,10}.",
 "JHN.10.3": "[Ihm]{1} [macht]{4} [de Tüürhüeter]{2,3} [uf]{4}, und{5} [d Schaaf]{6,7} [losed]{11} uf [sini]{10} [Stimm]{8,9}, und{12} [er rüeft]{16} [sini eigete]{13,14} [Schaaf]{15} [bim]{17} [Name]{18} und{19} [füert]{20} [si]{21} [use]{20}.",
 "JHN.10.4": "[Wänn]{1} [er]{5} [all]{4} [sini eigete]{2,3} [usetribe hät]{5}, [gaat er]{8} [vor]{6} [ine]{7} [här]{6}, und{9} [d Schaaf]{10,11} [folged]{13} [ihm]{12}, [wil]{14} [si]{15} [sini]{18} [Stimm]{16,17} [känned]{15}.",
 "JHN.10.5": "[Eme Frömde]{1} [aber]{2} [wärded si]{5} [sicher nöd]{3,4} [folge]{5}, [sondern]{6} [si wärded]{7} [vor]{8} [ihm]{9} [flüchte]{7}, [wil]{10} [si]{12} [d Stimm]{15,16} [vo de Frömde]{13,14} [nöd]{11} [känned]{12}.»",
 "JHN.10.6": "[Das]{1} [Bildwort]{2,3} [hät]{4} [de Jesus]{6,7} [ine]{5} [gseit]{4}; [die]{8} [aber]{9} [händ]{11} [nöd]{10} [verstande]{11}, [was]{12} [das]{14} [gsii isch]{13}, wo n [er]{15} [zu ine]{16} [gredt hät]{15}.",
 "JHN.10.7": "[Dänn]{2} [hät]{1} [de Jesus]{5,6} [wider]{3} [zu ine]{4} [gseit]{1}: «[Amen]{7}, [amen]{8}, [ich säge]{9} [eu]{10}: [Ich]{12} [bin]{13} [d Tüür]{14,15} [vo de Schaaf]{16,17}. ~11(ὅτι leitet di diräkt Red ii)",
 "JHN.10.8": "[All]{1}, [wo]{2} [vor]{4} [mir]{5} [choo sind]{3}, [sind]{7} [Dieb]{6} und{8} [Röiber]{9}; [aber]{10} [d Schaaf]{14,15} [händ]{12} [nöd]{11} [uf si]{13} [glost]{12}.",
 "JHN.10.9": "[Ich]{1} [bin]{2} [d Tüür]{3,4}. [Wänn]{7} [öpper]{8} [dur]{5} [mich]{6} [ine gaat]{9}, [wird er grettet]{10}, und{11} [er wird ine gaa]{12} und{13} [use gaa]{14} und{15} [Weid]{16} [finde]{17}.",
 "JHN.10.10": "[De Dieb]{1,2} [chunnt]{4} [nu]{3,5,6}, [zum]{7} [stäle]{8} und{9} [metzge]{10} und{11} [zgrund richte]{12}. [Ich]{13} [bin choo]{14}, [demit]{15} [si]{17} [Läbe]{16} [händ]{17} und{18} [meh als gnueg]{19} [händ]{20}.",
 "JHN.10.11": "[Ich]{1} [bin]{2} [de guet Hirt]{3-6}. [De guet Hirt]{7-10} [git]{14} [sis]{13} [Läbe]{11,12} [häre]{14} [für]{15} [d Schaaf]{16,17}.",
 "JHN.10.12": "[De Taglöhner]{1,2}, [wo]{5} [nöd]{4} [Hirt]{6} [isch]{5} und{3} [däm]{7} [d Schaaf]{10,11} [nöd]{8} [ghööred]{9,12}, [gseht]{13} [de Wolf]{14,15} [choo]{16} und{17} [laat]{18} [d Schaaf]{19,20} [im Stich]{18} und{21} [flüchtet]{22} – und{23} [de Wolf]{24,25} [riisst]{26} und{28} [versprängt]{29} [si]{27} –,",
 "JHN.10.13": "[wil]{1} [er]{3} [en Taglöhner]{2} [isch]{3} und{4} [ihm]{7} [nüüt]{5} [a]{8} [de Schaaf]{9,10} [glääge isch]{6}.",
 "JHN.10.14": "[Ich]{1} [bin]{2} [de guet Hirt]{3-6}, und{7} [ich känne]{8} [di Mine]{9,10}, und{11} [di Mine]{14,15} [känned]{12} [mich]{13},",
 "JHN.10.15": "[wie]{1} [de Vatter]{4,5} [mich]{3} [kännt]{2} [und ich]{6} [de Vatter]{8,9} [känne]{7}; und{10} [ich gib]{14} [mis]{13} [Läbe]{11,12} [häre]{14} [für]{15} [d Schaaf]{16,17}.",
 "JHN.10.16": "Und{1} [ich han]{4} [anderi]{2} [Schaaf]{3}, [wo]{5} [nöd]{6} [us]{8} [däm]{11} [Hof]{9,10} [sind]{7}; [au die]{12} [mues]{13} [ich]{14} [füere]{15}, und{16} [si wärded]{20} uf [mini]{19} [Stimm]{17,18} [lose]{20}, und{21} [si wärded]{22} [ei]{23} [Herde]{24} [wärde]{22}, [ein]{25} [Hirt]{26}.",
 "JHN.10.17": "[Drum]{1,2} [hät]{6} [mich]{3} [de Vatter]{4,5} [gern]{6}, [wil]{7} [ich]{8} [mis]{12} [Läbe]{10,11} [häregib]{9}, [demit]{13} [ich]{15} [s]{16} [wider]{14} [nimm]{15}.",
 "JHN.10.18": "[Niemer]{1} [nimmt]{2} [mir]{4,5} [s]{3} [wäg]{2}, [sondern]{6} [ich]{7} [gib]{8} [s]{9} [vo mir uus]{10,11} [häre]{8}. [Ich han]{13} [d Vollmacht]{12}, [s]{15} [häre z gää]{14}, und{16} [ich han]{18} [d Vollmacht]{17}, [s]{21} [wider]{19} [z neh]{20}. [Dä]{22} [Uftrag]{23,24} [han ich]{25} [vo]{26} [mim]{29} [Vatter]{27,28} [übercho]{25}.»",
 "JHN.10.19": "[Wider]{2} [isch]{3} [e Spaltig]{1} [under]{4} [de Jude]{5,6} [entstande]{3} [wäge]{7} [dene]{10} [Wort]{8,9}.",
 "JHN.10.20": "[Vili]{3} [vo]{4} [ine]{5} [aber]{2} [händ gseit]{1}: «[Er hät]{7} [en Dämon]{6} und{8} [isch vo Sinne]{9}. [Werum]{10} [losed ir]{12} [uf en]{11}?»",
 "JHN.10.21": "[Anderi]{1} [händ gseit]{2}: «[Das]{3} [sind]{7} [nöd]{6} [d Wort]{4,5} [vo me Bsässne]{8}. [Cha]{11} [öppe]{9} [en Dämon]{10} [Blinde]{12} [d Auge]{13} [uftue]{14}?»",
 "JHN.10.22": "[Damals]{2} [isch]{1} [z]{5} [Jerusalem]{6,7} [s Fäscht vo de Tämpelwiiig]{3,4} [gsii]{1}; [es isch]{9} [Winter]{8} [gsii]{9}.",
 "JHN.10.23": "Und{1} [de Jesus]{3,4} [isch]{2} [im]{5,6} [Tämpel]{7} [umenand gloffe]{2}, [i]{8} [de Säulehalle]{9,10} [vom Salomo]{11,12}.",
 "JHN.10.24": "[Dänn]{2} [händ]{1} [d Jude]{4,5} [en]{3} [umringt]{1} und{6} [zu ihm]{8} [gseit]{7}: «[Wie lang]{9,10} [laasch üs no zable]{11-14:idiom}? [Wänn]{15} [du]{16} [de Christus]{18,19} [bisch]{17}, [säg s]{20} [üs]{21} [offe]{22}!»",
 "JHN.10.25": "[De Jesus]{3,4} [hät]{1} [ine]{2} [gantwortet]{1}: «[Ich han]{5} [s eu]{6} [gseit]{5}, und{7} [ir glaubed]{9} [nöd]{8}. [D Wärch]{10,11}, [won]{12} [ich]{13} [im]{15,16} [Name]{17} [vo mim]{20} [Vatter]{18,19} [tue]{14}, [die]{21} [züüged]{22} [vo]{23} [mir]{24}.",
 "JHN.10.26": "[Aber]{1} [ir]{2} [glaubed]{4} [nöd]{3}, [wil]{5} [ir]{7} [nöd]{6} [zu]{8} [mine]{11,12} [Schaaf]{9,10} [ghööred]{7}.",
 "JHN.10.27": "[Mini]{3,4} [Schaaf]{1,2} [losed]{8} uf [mini]{7} [Stimm]{5,6}, [und ich]{9} [känne]{10} [si]{11}, und{12} [si folged]{13} [mir]{14}.",
 "JHN.10.28": "[Und ich]{1} [gib]{2} [ine]{3} [ewigs]{5} [Läbe]{4}, und{6} [si wärded]{9} [i Ewigkeit]{10-12} [sicher nöd]{7,8} [verlore gaa]{9}, und{13} [niemer]{14,16} [wird]{15} [si]{17} [us]{18} [minere]{21} [Hand]{19,20} [riisse]{15}.",
 "JHN.10.29": "[Min]{3} [Vatter]{1,2} – [was]{4} er [mir]{6} [gää hät]{5} – [isch]{9} [grösser]{8} [als alli]{7}, und{10} [niemer]{11} [cha]{12} si [us]{14} [de Hand]{15,16} [vom Vatter]{17,18} [riisse]{13}.",
 "JHN.10.30": "[Ich]{1} und{2} [de Vatter]{3,4} [sind]{6} [eis]{5}.»",
 "JHN.10.31": "[Dänn]{2} [händ]{1} [d Jude]{5,6} [wider]{3} [Stei]{4} [ufgnoo]{1}, [zum]{7} [en]{9} [steinige]{8}.",
 "JHN.10.32": "[De Jesus]{3,4} [hät]{1} [ine]{2} [gantwortet]{1}: «[Vili]{5} [gueti]{7} [Wärch]{6} [han ich]{8} [eu]{9} [zeigt]{8}, [vom]{10,11} [Vatter]{12} här. [Für]{13} [weles]{14} [vo dene]{15} [Wärch]{16} [steiniged ir]{18} [mich]{17}?»",
 "JHN.10.33": "[D Jude]{3,4} [händ]{1} [em]{2} [gantwortet]{1}: «[Wäge]{5} [eme guete]{6} [Wärch]{7} [steiniged mir]{9} [dich]{10} [nöd]{8}, [sondern]{11} [wäge]{12} [Läschterig]{13}, und{14} [wil]{15} [du]{16} [als]{18} [Mänsch]{17} [dich sälber]{20} [zu Gott]{21} [machsch]{19}.»",
 "JHN.10.34": "[De Jesus]{3,4} [hät]{1} [ine]{2} [gantwortet]{1}: «[Staat]{6} [nöd]{5} [i]{8} [euem]{11} [Gsetz]{9,10} [gschribe]{7}: ‹[Ich]{13} [han gseit]{14}: [Ir sind]{16} [Götter]{15}›? ~12(ὅτι leitet s Zitat ii)",
 "JHN.10.35": "[Wänn]{1} [er]{3} [die]{2} [Götter]{4} [gnännt hät]{3}, [a]{5} [die]{6} [s Wort]{7,8} [vo Gott]{9,10} [ergange isch]{11} – und{12} [d Schrift]{16,17} [cha]{14} [nöd]{13} [ufghobe wärde]{15} –,",
 "JHN.10.36": "[säged]{11} [ir]{10} dänn [vo däm]{1}, wo [de Vatter]{2,3} [gheiliget]{4} und{5} [i]{7} [d Wält]{8,9} [gschickt hät]{6}: ‹[Du läschterisch]{13}›, [wil]{14} [ich gseit han]{15}: ‹[Ich bin]{19} [de Sohn]{16} [vo Gott]{17,18}›? ~12(ὅτι leitet di diräkt Red ii)",
 "JHN.10.37": "[Wänn]{1} [ich]{3} [d Wärch]{4,5} [vo mim]{8} [Vatter]{6,7} [nöd]{2} [tue]{3}, [dänn glaubed]{10} [mir]{11} [nöd]{9}.",
 "JHN.10.38": "[Wänn]{1} [ich si]{3} [aber]{2} [tue]{3}, [dänn glaubed]{10} [de Wärch]{8,9}, [au wänn]{4} [ir]{7} [mir]{5} [nöd]{6} [glaubed]{7}, [demit]{11} [ir erchänned]{12} und{13} [immer meh erchänned]{14}, [dass]{15} [de Vatter]{18,19} [i]{16} [mir]{17} isch [und ich]{20} [im]{21,22} [Vatter]{23}.»",
 "JHN.10.39": "[Dänn]{2} [händ si]{1} [wider]{3} [gsuecht]{1}, [en]{4} [z packe]{5}; und{6} [er isch]{7} [ine]{11} [us]{8} [de Händ]{9,10} [entwütscht]{7}.",
 "JHN.10.40": "Und{1} [er isch]{2} [wider]{3} [wäggange]{2}, [uf di ander Siite]{4} [vom Jordan]{5,6}, [a]{7} [de Ort]{8,9}, [wo]{10} [de Johannes]{12} [zerscht]{13,14} [tauft hät]{11,15}, und{16} [er isch]{17} [dört]{18} [bliibe]{17}.",
 "JHN.10.41": "Und{1} [vili]{2} [sind]{3} [zu]{4} [ihm]{5} [choo]{3} und{6} [händ gseit]{7}: «[De Johannes]{9} [hät]{12} [zwar]{10} [kei]{13} [Zeiche]{11} [gmacht]{12}, [aber]{15} [alles]{14}, [was]{16} [de Johannes]{18} [über]{19} [dä]{20} [gseit hät]{17}, [isch]{22} [wahr]{21} [gsii]{22}.» ~8(ὅτι leitet di diräkt Red ii)",
 "JHN.10.42": "Und{1} [vili]{2} [händ]{3} [dört]{6} [a]{4} [en]{5} [glaubt]{3}.",
 # ------------------------------------------------------------ Kapitel 11
 "JHN.11.1": "[Es isch]{1} [aber]{2} [eine]{3} [chrank]{4} [gsii]{1}, [de Lazarus]{5} [vo]{6} [Betanie]{7}, [us]{8} [em Dorf]{9,10} [vo de Maria]{11} und{12} [vo irere]{16} [Schwöschter]{14,15} [Marta]{13}.",
 "JHN.11.2": "[D Maria]{3} [aber]{2} [isch]{1} [di]{4} [gsii]{1}, wo [de Herr]{6,7} [mit Salböl]{8} [gsalbet]{5} und{9} [sini]{13} [Füess]{11,12} [mit irne]{14,16} [Haar]{15} [abtröchnet hät]{10}; [ire]{17} [Brueder]{18,19} [Lazarus]{20} [isch chrank gsii]{21}.",
 "JHN.11.3": "[Dänn]{2} [händ]{1} [d Schwöschtere]{3,4} [zu]{5} [ihm]{6} [gschickt]{1} [und händ laa säge]{7}: «[Herr]{8}, [lueg]{9}, dä, [won]{10} [du lieb häsch]{11}, [isch chrank]{12}.»",
 "JHN.11.4": "[Wo]{1} [de Jesus]{3,4} das [aber]{2} [ghört hät]{1}, [hät er gseit]{5}: «[Die]{6} [Chranket]{7,8} [füert]{10} [nöd]{9} [zum]{11} [Tod]{12}, [sondern]{13} [si dient]{14} [de Herrlichkeit]{15,16} [vo Gott]{17,18}, [demit]{19} [de Sohn]{21,22} [vo Gott]{23,24} [dur]{25} [si]{26} [verherrlicht wird]{20}.»",
 "JHN.11.5": "[De Jesus]{3,4} [aber]{2} [hät]{1} [d Marta]{5,6} und{7} [iri]{10} [Schwöschter]{8,9} und{11} [de Lazarus]{12,13} [gern gha]{1}.",
 "JHN.11.6": "[Wo]{1} [er]{3} [jetzt]{2} [ghört hät]{3}, [dass]{4} [er chrank seig]{5}, [isch er]{8} [dänn]{6} [no]{7} [zwei]{13} [Täg]{14} [a]{9} [däm Ort]{12} [bliibe]{8}, [won]{10} [er gsii isch]{11}.",
 "JHN.11.7": "[Ersch]{1} [nachane]{2,3} [seit er]{4} [zu de Jünger]{5,6}: «[Mir gönd]{7} [wider]{11} [uf]{8} [Judäa]{9,10}!»",
 "JHN.11.8": "[D Jünger]{3,4} [säged]{1} [zu ihm]{2}: «[Rabbi]{5}, [grad no]{6} [händ]{7} [d Jude]{10,11} [gsuecht]{7}, [dich]{8} [z steinige]{9}, und{12} [du gaasch]{14} [wider]{13} [det häre]{15}?»",
 "JHN.11.9": "[De Jesus]{2} [hät gantwortet]{1}: «[Hät]{6} [de Tag]{7,8} [nöd]{3} [zwölf]{4} [Stund]{5}? [Wänn]{9} [öpper]{10} [am]{12,13} [Tag]{14} [umelauft]{11}, [stolperet er]{16} [nöd]{15}, [wil]{17} [er]{23} [s Liecht]{18,19} [vo dere]{22} [Wält]{20,21} [gseht]{23}.",
 "JHN.11.10": "[Wänn]{1} [aber]{2} [öpper]{3} [i]{5} [de Nacht]{6,7} [umelauft]{4}, [stolperet er]{8}, [wil]{9} [s Liecht]{10,11} [nöd]{12} [i]{14} [ihm]{15} [isch]{13}.»",
 "JHN.11.11": "[Das]{1} [hät er gseit]{2}, und{3} [nachane]{4,5} [seit er]{6} [zu ine]{7}: «[De Lazarus]{8}, [üse]{11} [Fründ]{9,10}, [isch iigschlaafe]{12}; [aber]{13} [ich gaa]{14}, [zum]{15} [en]{17} [ufwecke]{16}.»",
 "JHN.11.12": "[Dänn]{2} [händ]{1} [d Jünger]{3,4} [zu ihm]{5} [gseit]{1}: «[Herr]{6}, [wänn]{7} [er iigschlaafe isch]{8}, [wird er gsund]{9}.»",
 "JHN.11.13": "[De Jesus]{3,4} [hät]{1} [aber]{2} [vo]{5} [sim]{8} [Tod]{6,7} [gredt]{1}; [die]{9} [aber]{10} [händ gmeint]{11}, [dass]{12} [er]{18} [vom]{13,14} [Uusrue]{15} [im Schlaaf]{16,17} [redi]{18}.",
 "JHN.11.14": "[Dänn]{1} [hät]{3} [de Jesus]{5,6} [ine]{4} [jetzt]{2} [offe]{7} [gseit]{3}: «[De Lazarus]{8} [isch gstorbe]{9},",
 "JHN.11.15": "und{1} [ich freu mich]{2} [wäge]{3} [eu]{4}, [dass]{7} [ich]{9} [nöd]{8} [dört]{10} [gsii bin]{9}, [demit]{5} [ir glaubed]{6}. [Aber]{11} [mir gönd]{12} [zu]{13} [ihm]{14}!»",
 "JHN.11.16": "[Dänn]{2} [hät]{1} [de Thomas]{3}, [wo]{4} [mer]{5} [Didymus]{6} [nännt]{5}, [zu de andere Jünger]{7,8} [gseit]{1}: «[Mir]{11} [gönd]{9} [au]{10}, [demit]{12} [mir]{13} [mit]{14} [ihm]{15} [stärbed]{13}!»",
 "JHN.11.17": "[Wo]{1} [de Jesus]{3,4} [jetzt]{2} [aachoo isch]{1}, [hät er gfunde]{5}, [dass er]{6} [scho]{8} [vier]{7} [Täg]{9} [im]{11,12} [Grab]{13} [liit]{10}.",
 "JHN.11.18": "[Betanie]{3,4} [isch]{1} [aber]{2} [nööch]{5} [bi Jerusalem]{6,7} [gsii]{1}, [öppe]{8} [füfzä]{11} [Stadie]{10} [devo]{9}.",
 "JHN.11.19": "[Vili]{1} [vo]{3} [de Jude]{4,5} [aber]{2} [sind]{6} [zu]{7} [de Marta]{8,9} und{10} [de Maria]{11} [choo]{6}, [zum]{12} [si]{14} [wäge]{15} [em Brueder]{16,17} [tröschte]{13}.",
 "JHN.11.20": "[Wo]{4} [d Marta]{1,3} [jetzt]{2} [ghört hät]{5}, [dass]{6} [de Jesus]{7} [chunnt]{8}, [isch si]{9} [ihm]{10} [entgäge gange]{9}; [d Maria]{11} [aber]{12} [isch]{16} [im]{13,14} [Huus]{15} [hocke bliibe]{16}.",
 "JHN.11.21": "[Dänn]{2} [hät]{1} [d Marta]{3,4} [zum]{5} [Jesus]{6,7} [gseit]{1}: «[Herr]{8}, [wänn]{9} [du]{10} [da]{11} [gsii wärsch]{10}, [wär]{13} [min]{17} [Brueder]{15,16} [nöd]{12} [gstorbe]{14}.",
 "JHN.11.22": "Und{1} [au jetzt]{2} [weiss ich]{3}, [dass]{4} [Gott]{12,13} [dir]{11} [wird gää]{10}, [was]{5} [immer]{6} [du]{7} [vo Gott]{8,9} [erbittisch]{7}.»",
 "JHN.11.23": "[De Jesus]{3,4} [seit]{1} [zu ere]{2}: «[Din]{8} [Brueder]{6,7} [wird uferstaa]{5}.»",
 "JHN.11.24": "[D Marta]{3,4} [seit]{1} [zu ihm]{2}: «[Ich weiss]{5}, [dass]{6} [er wird uferstaa]{7} [bi]{8} [de Uferstehig]{9,10} [am]{11,12} [letschte]{13} [Tag]{14}.»",
 "JHN.11.25": "[De Jesus]{3,4} [hät]{1} [zu ere]{2} [gseit]{1}: «[Ich]{5} [bin]{6} [d Uferstehig]{7,8} und{9} [s Läbe]{10,11}. [Wer]{12} [a]{14} [mich]{15} [glaubt]{13}, [wird läbe]{18}, [au wänn]{16} [er stirbt]{17};",
 "JHN.11.26": "und{1} [jede]{2}, [wo]{3} [läbt]{4} und{5} [a]{7} [mich]{8} [glaubt]{6}, [wird]{11} [i Ewigkeit]{12-14} [sicher nöd]{9,10} [stärbe]{11}. [Glaubsch]{15} [das]{16}?»",
 "JHN.11.27": "[Si seit]{1} [zu ihm]{2}: «[Ja]{3}, [Herr]{4}, [ich]{5} [glaub]{6}, [dass]{7} [du]{8} [de Christus]{10,11} [bisch]{9}, [de Sohn]{12,13} [vo Gott]{14,15}, [wo]{16} [i]{17} [d Wält]{18,19} [chunnt]{20}.»",
 "JHN.11.28": "Und{1} [wo si]{3} [das]{2} [gseit hät]{3}, [isch si gange]{4} und{5} [hät]{6} [heimli]{11} [iri]{10} [Schwöschter]{8,9} [Maria]{7} [grüeft]{6} [und gseit]{12}: «[De Lehrer]{13,14} [isch da]{15} und{16} [rüeft]{17} [dich]{18}.»",
 "JHN.11.29": "[Wo]{3} [si]{1} [aber]{2} [das ghört hät]{4}, [isch si]{5} [schnell]{6} [ufgstande]{5} und{7} [isch]{8} [zu]{9} [ihm]{10} [gange]{8}.",
 "JHN.11.30": "[De Jesus]{4,5} [isch]{3} [aber]{2} [no nöd]{1} [is]{6,7} [Dorf]{8} [choo]{3}, [sondern]{9} [er isch]{10} [no]{11} [a]{12} [däm Ort]{13,14} [gsii]{10}, [wo]{15} [d Marta]{18,19} [ihm]{17} [entgäge choo isch]{16}.",
 "JHN.11.31": "[D Jude]{1,3} [jetzt]{2}, [wo]{4} [bi]{6} [ere]{7} [im]{8,9} [Huus]{10} [gsii sind]{5} und{11} [si]{13} [tröschtet händ]{12}, [händ gseh]{14}, [dass]{17} [d Maria]{15,16} [schnell]{18} [ufgstande]{19} und{20} [usegange isch]{21}; [si sind]{22} [ere]{23} [nachegange]{22}, [wil si gmeint händ]{24}, [dass]{25} [si]{26} [zum]{27,28} [Grab]{29} [gaat]{26}, [zum]{30} [dört]{32} [briegge]{31}.",
 "JHN.11.32": "[Wo]{4} [d Maria]{1,3} [jetzt]{2} [det häre choo isch]{5}, [wo]{6} [de Jesus]{8} [gsii isch]{7}, und [en]{10} [gseh hät]{9}, [isch si]{11} [ihm]{12} [z]{13} [Füess]{14,15} [gfalle]{11} [und hät]{16} [zu ihm]{17} [gseit]{16}: «[Herr]{18}, [wänn]{19} [du]{20} [da]{21} [gsii wärsch]{20}, [wär]{23} [min]{24} [Brueder]{26,27} [nöd]{22} [gstorbe]{25}.»",
 "JHN.11.33": "[Wo]{3} [de Jesus]{1} [jetzt]{2} [gseh hät]{4}, wie [si]{5} [briegget]{6} und{7} wie [d Jude]{8,11}, wo [mit ere]{10} [choo sind]{9}, [briegged]{12}, [isch er]{13} [im]{14} [Geischt]{15} [zornig worde]{13} und{16} [hät]{17} [sich]{18} [ufgwüelt]{17}",
 "JHN.11.34": "und{1} [hät gseit]{2}: «[Wo]{3} [händ ir]{4} [en]{5} [anegleit]{4}?» [Si säged]{6} [zu ihm]{7}: «[Herr]{8}, [chumm]{9} und{10} [lueg]{11}!»",
 "JHN.11.35": "[Em Jesus]{2,3} [sind d Träne choo]{1}.",
 "JHN.11.36": "[Dänn]{2} [händ]{1} [d Jude]{3,4} [gseit]{1}: «[Lueged]{5}, [wie]{6} [lieb er]{7} [en]{8} [gha hät]{7}!»",
 "JHN.11.37": "[Es paar]{1} [vo]{3} [ine]{4} [aber]{2} [händ gseit]{5}: «[Hett]{7} [dä]{8}, [wo]{9} [em Blinde]{13,14} [d Auge]{11,12} [uftaa hät]{10}, [nöd]{6} [chöne]{7} [mache]{15}, [dass]{16} [au]{17} [dä]{18} [nöd]{19} [stirbt]{20}?»",
 "JHN.11.38": "[Dänn]{2} [chunnt]{7} [de Jesus]{1}, [wider]{3} [innerlich]{5,6} [zornig]{4}, [zum]{8,9} [Grab]{10}. [Es isch]{11} [aber]{12} [e Höhli]{13} [gsii]{11}, und{14} [en Stei]{15} [isch]{16} [druf]{17,18} [gläge]{16}.",
 "JHN.11.39": "[De Jesus]{2,3} [seit]{1}: «[Nämed]{4} [de Stei]{5,6} [wäg]{4}!» [D Marta]{13}, [d Schwöschter]{9,10} [vom Verstorbene]{11,12}, [seit]{7} [zu ihm]{8}: «[Herr]{14}, [er schmöckt]{16} [scho]{15}; [es isch]{19} [nämli]{18} [de viert Tag]{17}.»",
 "JHN.11.40": "[De Jesus]{3,4} [seit]{1} [zu ere]{2}: «[Han ich]{6} [dir]{7} [nöd]{5} [gseit]{6}: [Wänn]{9} [du glaubsch]{10}, [wirsch]{11} [d Herrlichkeit]{12,13} [vo Gott]{14,15} [gseh]{11}?» ~8(ὅτι leitet di diräkt Red ii)",
 "JHN.11.41": "[Dänn]{2} [händ si]{1} [de Stei]{3,4} [wäggnoo]{1}. [De Jesus]{5,7} [aber]{6} [hät]{8} [d Auge]{9,10} [ufe]{11} [ghobe]{8} und{12} [hät gseit]{13}: «[Vatter]{14}, [ich dank]{15} [dir]{16}, [dass]{17} [du]{18} [mich]{19} [erhört häsch]{18}.",
 "JHN.11.42": "[Ich]{1} [han]{3} [aber]{2} [gwüsst]{3}, [dass]{4} [du]{7} [mich]{6} [immer]{5} [erhörsch]{7}; [aber]{8} [wäge]{9} [de Mängi]{10,11}, [wo]{12} [umestaat]{13}, [han ich s gseit]{14}, [demit]{15} [si glaubed]{16}, [dass]{17} [du]{18} [mich]{19} [gschickt häsch]{20}.»",
 "JHN.11.43": "Und{1} [wo er]{3} [das]{2} [gseit hät]{3}, [hät er]{6} [mit luuter]{5} [Stimm]{4} [grüeft]{6}: «[Lazarus]{7}, [chumm]{8} [use]{9}!»",
 "JHN.11.44": "[De Tot]{2,3} [isch usechoo]{1}, [a]{5} [de Füess]{6} und{7} [a de Händ]{8,9} [mit Binde]{10} [iiwicklet]{4}, und{11} [sis]{14} [Gsicht]{12,13} [isch]{16} [mit eme Schweisstuech]{15} [umbunde gsii]{16}. [De Jesus]{19,20} [seit]{17} [zu ine]{18}: «[Bindet]{21} [en]{22} [los]{21} und{23} [lönd]{24} [en]{25} [gaa]{26}!»",
 "JHN.11.45": "[Vili]{1} [jetzt]{2} [vo]{3} [de Jude]{4,5}, [wo]{6} [zu]{8} [de Maria]{9,10} [choo sind]{7} und{11} [gseh händ]{12}, [was]{13} [er gmacht hät]{14}, [händ]{15} [a]{16} [en]{17} [glaubt]{15}.",
 "JHN.11.46": "[Es paar]{1} [vo]{3} [ine]{4} [aber]{2} [sind]{5} [zu]{6} [de Pharisäer]{7,8} [gange]{5} und{9} [händ]{10} [ine]{11} [verzellt]{10}, [was]{12} [de Jesus]{14} [gmacht hät]{13}.",
 "JHN.11.47": "[Dänn]{2} [händ]{1} [d Hoheprieschter]{3,4} und{5} [d Pharisäer]{6,7} [e Sitzig vom Hohe Raat]{8} [iiberüeft]{1} und{9} [händ gseit]{10}: «[Was]{11} [söled mir mache]{12}? [Dä]{14} [Mänsch]{15,16} [tuet]{18} [ja]{13} [vili]{17} [Zeiche]{19}.",
 "JHN.11.48": "[Wänn]{1} [mir]{2} [en]{3} [eso]{4} [mache lönd]{2}, [wärded]{6} [alli]{5} [a]{7} [en]{8} [glaube]{6}, und{9} [d Römer]{11,12} [wärded choo]{10} und{13} [wärded]{14} [üs]{15} [de Ort]{17,18} und{19} [d Nation]{20,21} [wägneh]{14}.» ~16(καί … καί «sowohl … als auch»; nöd eigens widergää)",
 "JHN.11.49": "[Eine]{1,3} [vo]{4} [ine]{5} [aber]{2}, [de Kajafas]{6}, [wo]{8} [i dem]{9,11} [Jahr]{10} [Hoheprieschter]{7} [gsii isch]{8}, [hät]{12} [zu ine]{13} [gseit]{12}: «[Ir]{14} [wüssed]{16} [überhaupt nüüt]{15,17}",
 "JHN.11.50": "[und überleged]{2} [au nöd]{1}, [dass]{3} es [besser]{4} [für eu]{5} [isch]{4}, [dass]{6} [ein]{7} [Mänsch]{8} [für]{10} [s Volk]{11,12} [stirbt]{9} und{13} [nöd]{14} [di ganz]{15,16} [Nation]{17} [zgrund gaat]{18}.»",
 "JHN.11.51": "[Das]{1} [hät er]{6} [aber]{2} [nöd]{5} [vo sich uus]{3,4} [gseit]{6}, [sondern]{7} [als]{9} [Hoheprieschter]{8} [vo dem]{10,12} [Jahr]{11} [hät er prophezeit]{13}, [dass]{14} [de Jesus]{16} [für]{18} [d Nation]{19,20} [stärbe]{17} [werdi]{15},",
 "JHN.11.52": "und{1} [nöd]{2} [für]{3} [d Nation]{4,5} [elei]{6}, [sondern]{7} [zum]{8} [au]{9} [di verstreute]{14,15} [Chind]{10,11} [vo Gott]{12,13} [zu ere Einheit]{17,18} [zämefüere]{16}.",
 "JHN.11.53": "[Vo]{1} [dem]{2,4} [Tag]{5} [aa]{1} [händ si]{6} [jetzt]{3} [plant]{6}, [en]{9} [z töte]{7,8}.",
 "JHN.11.54": "[De Jesus]{1,3} [isch]{6} [jetzt]{2} [nüme]{4} [offe]{5} [under]{7} [de Jude]{8,9} [umegloffe]{6}, [sondern]{10} [isch]{11} [vo dört]{12} [wäggange]{11} [i]{13} [d Gäged]{14,15} [nööch]{16} [bi de Wüeschti]{17,18}, [in]{19} [e Stadt]{22}, wo [Efraim]{20} [heisst]{21}, [und dört]{23} [isch er]{24} [mit]{25} [de Jünger]{26,27} [bliibe]{24}.",
 "JHN.11.55": "[S Passa]{4,5} [vo de Jude]{6,7} [aber]{2} [isch]{1} [nööch]{3} [gsii]{1}, und{8} [vili]{10} [sind]{9} [vor]{16} [em Passa]{17,18} [vom]{13,14} [Land]{15} [uf]{11} [Jerusalem]{12} [ufe gange]{9}, [zum]{19} [sich]{21} [reinige]{20}.",
 "JHN.11.56": "[Si händ]{1} [jetzt]{2} [de Jesus]{3,4} [gsuecht]{1} und{5} [händ]{6} [zunenand]{7,8} [gseit]{6}, [während si]{12} [im]{9,10} [Tämpel]{11} [gstande sind]{12}: «[Was]{13} [meined]{14} [ir]{15}? [Dass]{16} [er]{19} [sicher nöd]{17,18} [as]{20,21} [Fäscht]{22} [chunnt]{19}?»",
 "JHN.11.57": "[D Hoheprieschter]{3,4} und{5} [d Pharisäer]{6,7} [händ]{1} [aber]{2} [Aawiisige]{8} [gää]{1}, [dass]{9}, [wänn]{10} [öpper]{11} [erfahri]{12}, [wo]{13} [er seig]{14}, [er s mälde söll]{15}, [demit]{16} [si]{17} [en]{18} [chönted packe]{17}.",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
G = "Grundentscheid für das ganze Evangelium, begründet in scripts/authoring/johannes_text_01_03.py"
DEC_DE = [
 ("JHN.10.1", "Amen, amen, ich sage euch", "literal", "Ἀμὴν ἀμὴν λέγω ὑμῖν", None, ["Wahrlich, wahrlich, ich sage euch"], "ἀμήν wird nicht übersetzt, sondern als «Amen» beibehalten (" + G + "). Die verdoppelte Form steht nach der Zählung der SBLGNT-Tokens 25-mal im Johannesevangelium; hier wie in [[JHN.10.7]]."),
 ("JHN.10.1", "den Hof der Schafe", "literal", "τὴν αὐλὴν τῶν προβάτων", None, ["den Schafstall", "den Pferch"], "αὐλή ist ein ummauerter Hof; hier der umfriedete Platz, in dem die Schafe nachts bleiben. Dasselbe Wort in [[JHN.10.16]]."),
 ("JHN.10.6", "Bildwort", "interpretive", "παροιμίαν", None, ["Gleichnis", "Rätselrede", "Sinnbild"], "παροιμία ist bei Johannes eine verhüllte, bildhafte Rede, die erst aufgeschlüsselt werden muss (vgl. [[JHN.16.25]], [[JHN.16.29]]). Für die Gleichnisse der anderen Evangelien steht meist παραβολή."),
 ("JHN.10.7", "Ich bin die Tür", "literal", "ἐγώ εἰμι ἡ θύρα", None, None, "ἐγώ εἰμι mit Bildwort wird einheitlich «Ich bin …» wiedergegeben (" + G + "). In Johannes 10–11: «die Tür» ([[JHN.10.7]], [[JHN.10.9]]), «der gute Hirte» ([[JHN.10.11]], [[JHN.10.14]]), «die Auferstehung und das Leben» ([[JHN.11.25]])."),
 ("JHN.10.10", "Überfluss", "adapted", "περισσὸν", "Übermass", ["Leben in Fülle"], "περισσός «über das Mass hinaus, reichlich»."),
 ("JHN.10.11", "der gute Hirte", "traditional", "ὁ ποιμὴν ὁ καλός", "der Hirte, der gute", ["der schöne Hirte", "der rechte Hirte", "der vortreffliche Hirte"], "καλός heisst «schön, edel, tüchtig, gut». Gemeint ist der Hirte, wie er sein soll, im Gegensatz zum Lohnarbeiter ([[JHN.10.12]]). «Der gute Hirte» ist die vertraute Wiedergabe. Zum Hirtenbild vgl. [[PSA.23.1]] und [[EZK.34.11]]–[[EZK.34.16]]."),
 ("JHN.10.11", "gibt sein Leben hin", "interpretive", "τὴν ψυχὴν αὐτοῦ τίθησιν", "legt seine Seele hin", ["setzt sein Leben ein", "lässt sein Leben"], "ψυχή meint hier das Leben. τίθημι τὴν ψυχήν «das Leben hinlegen» ist eine johanneische Wendung (vgl. [[JHN.13.37]], [[JHN.15.13]], [[1JN.3.16]]); in [[JHN.10.15]], [[JHN.10.17]] und [[JHN.10.18]] gleich übersetzt."),
 ("JHN.10.12", "Der Lohnarbeiter", "adapted", "ὁ μισθωτὸς", "der um Lohn Angestellte", ["der Mietling", "der Tagelöhner"], "μισθωτός ist einer, der für Lohn arbeitet. «Mietling» (Luther 1912) ist die vertraute, heute ungebräuchliche Wiedergabe."),
 ("JHN.10.16", "eine Herde", "literal", "μία ποίμνη", None, None, "Wortspiel ποίμνη «Herde» – ποιμήν «Hirte». Die anderen Schafe kommen nicht in denselben Hof (αὐλή), sondern es entsteht eine Herde."),
 ("JHN.10.18", "Vollmacht", "literal", "ἐξουσίαν", None, ["Recht", "Macht"], "ἐξουσία ist die verliehene Berechtigung, etwas zu tun."),
 ("JHN.10.18", "Auftrag", "interpretive", "ἐντολὴν", None, ["Gebot", "Weisung"], "ἐντολή heisst «Gebot, Auftrag»; hier der Auftrag des Vaters, das Leben hinzugeben und wieder zu nehmen (vgl. [[JHN.12.49]], [[JHN.14.31]])."),
 ("JHN.10.19", "den Juden", "interpretive", "τοῖς Ἰουδαίοις", None, ["den jüdischen Führern", "den Judäern"], G + ": οἱ Ἰουδαῖοι wird wörtlich mit «die Juden» wiedergegeben. Das Wort bezeichnet in Kapitel 10–11 Gegner Jesu in Jerusalem ([[JHN.10.31]], [[JHN.11.8]]), eine gespaltene Menge ([[JHN.10.19]]) sowie Trauernde und Glaubende ([[JHN.11.19]], [[JHN.11.45]]). «Die jüdischen Führer» oder «die Judäer» wären Deutungsentscheidungen je nach Stelle. Jesus, seine Jünger, Marta, Maria und Lazarus sind selbst Juden."),
 ("JHN.10.22", "das Fest der Tempelweihe", "adapted", "τὰ ἐγκαίνια", "die Einweihung", ["Chanukka"], "ἐγκαίνια «Einweihung, Erneuerung» bezeichnet das Fest, das an die Wiedereinweihung des Tempels unter Judas Makkabäus erinnert ([[1MA.4.52]]–[[1MA.4.59]]); heute Chanukka. Es fällt in den Winter."),
 ("JHN.10.24", "hältst du uns hin", "interpretive", "τὴν ψυχὴν ἡμῶν αἴρεις", "hebst du unsere Seele", ["hältst du uns in Spannung", "quälst du uns"], "Die Wendung bezeichnet hier wohl Spannung und Ungewissheit; sie kann auch «aufregen, ärgern» heissen. Ob die Frage ungeduldig, feindselig oder ernsthaft gemeint ist, lässt der Text offen."),
 ("JHN.10.24", "der Christus", "traditional", "ὁ χριστός", "der Gesalbte", ["der Messias"], "χριστός übersetzt hebräisch «Gesalbter», Messias (vgl. [[JHN.1.41]])."),
 ("JHN.10.25", "Die Werke", "literal", "τὰ ἔργα", None, ["Die Taten"], "ἔργα sind bei Johannes die Taten Jesu, die er als Werke des Vaters bezeichnet; sie schliessen die Zeichen ein (vgl. [[JHN.5.36]], [[JHN.10.37]]–[[JHN.10.38]])."),
 ("JHN.10.28", "ewiges", "literal", "ζωὴν αἰώνιον", None, None, "ζωὴ αἰώνιος durchgehend «ewiges Leben». εἰς τὸν αἰῶνα mit doppelter Verneinung ist mit «in Ewigkeit gewiss nicht» wiedergegeben, ebenso [[JHN.11.26]]; sinngemäss auch «niemals»."),
 ("JHN.10.29", "grösser als alle", "interpretive", "ὃ δέδωκέν μοι πάντων μεῖζων ἐστίν", "was er mir gegeben hat, grösser als alle ist er", ["Was mein Vater mir gegeben hat, ist grösser als alles", "Mein Vater, der sie mir gegeben hat, ist grösser als alle"], "Der SBLGNT liest mit Holmes ὃ … μείζων: das Relativpronomen ist sächlich («was»), das Adjektiv männlich (auf den Vater bezogen). Die Verbindung ist grammatisch hart. Die Übersetzung hält sie als Einschub fest: Das Gegebene sind wohl die Schafe (vgl. [[JHN.6.37]], [[JHN.6.39]], [[JHN.17.2]]), «grösser als alle» sagt etwas über den Vater. Andere Ausgaben lesen glatter in die eine oder andere Richtung; siehe die Alternativen."),
 ("JHN.10.30", "eins", "literal", "ἕν", None, None, "ἕν ist sächlich: «eins», nicht «einer» (εἷς). Wie weit die ausgesagte Einheit reicht (Wille und Wirken oder Wesen), wird verschieden ausgelegt; die Gegner verstehen den Satz als Anspruch, Gott zu sein ([[JHN.10.33]])."),
 ("JHN.10.33", "zu Gott", "interpretive", "θεόν", None, ["zu einem Gott"], "θεόν steht ohne Artikel; im Zusammenhang mit [[JHN.10.34]]–[[JHN.10.36]] sind beide Wiedergaben möglich."),
 ("JHN.10.34", "Gesetz", "literal", "τῷ νόμῳ", None, ["Schrift"], "Zitiert wird [[PSA.82.6]]. «Gesetz» meint hier die Schrift insgesamt, nicht nur die fünf Bücher Mose (vgl. [[JHN.12.34]], [[JHN.15.25]])."),
 ("JHN.10.35", "das Wort", "literal", "ὁ λόγος", None, None, "λόγος durchgehend «Wort» (" + G + ", vgl. [[JHN.1.1]])."),
 ("JHN.10.36", "geheiligt", "literal", "ἡγίασεν", None, ["geweiht", "ausgesondert"], "ἁγιάζω «heiligen, weihen, für Gott aussondern». Am Fest der Tempelweihe ([[JHN.10.22]]) kann «geweiht» mitklingen."),
 ("JHN.10.36", "die Welt", "literal", "τὸν κόσμον", None, None, "κόσμος durchgehend «Welt» (" + G + ")."),
 ("JHN.10.38", "immer mehr erkennt", "adapted", "γνῶτε καὶ γινώσκητε", "erkennt und erkennt", ["erkennt und versteht"], "Dasselbe Verb steht zuerst im Aorist (zur Erkenntnis kommen), dann im Präsens (dauerndes Erkennen)."),
 ("JHN.10.40", "er blieb", "literal", "ἔμεινεν", None, ["hielt sich auf"], "μένω durchgehend «bleiben» (" + G + "), auch wo es den Aufenthalt meint (vgl. [[JHN.11.6]], [[JHN.11.54]])."),
 ("JHN.10.41", "Zeichen", "literal", "σημεῖον", None, ["Wunder"], "σημεῖον durchgehend «Zeichen», nicht «Wunder» (" + G + "): Johannes nennt die Taten Jesu Zeichen, weil sie auf ihn hinweisen (vgl. [[JHN.2.11]], [[JHN.20.30]]–[[JHN.20.31]]). Ebenso [[JHN.11.47]]."),
 ("JHN.11.3", "du lieb hast", "interpretive", "φιλεῖς", "du liebst", None, "Für die Liebe Jesu zu Lazarus und seinen Schwestern steht φιλέω ([[JHN.11.3]], [[JHN.11.36]]) und ἀγαπάω ([[JHN.11.5]]). Die Übersetzung macht den Wortwechsel mit «lieb haben» und «lieben» sichtbar; ob Johannes damit einen Unterschied in der Sache meint, ist umstritten (vgl. [[JHN.21.15]]–[[JHN.21.17]])."),
 ("JHN.11.4", "führt nicht zum Tod", "adapted", "οὐκ ἔστιν πρὸς θάνατον", "ist nicht zum Tod", ["endet nicht im Tod"], "Lazarus stirbt ([[JHN.11.14]]); gesagt ist, dass der Tod nicht das Ziel und Ende dieser Krankheit ist."),
 ("JHN.11.4", "der Herrlichkeit", "literal", "τῆς δόξης", None, ["der Ehre"], "δόξα und δοξάζω durchgehend «Herrlichkeit» und «verherrlichen» (" + G + "). Vgl. [[JHN.11.40]]."),
 ("JHN.11.11", "ist eingeschlafen", "literal", "κεκοίμηται", None, None, "κοιμάομαι «schlafen» ist auch Bild für den Tod (vgl. [[ACT.7.60]], [[1TH.4.13]]); die Jünger verstehen es wörtlich ([[JHN.11.13]])."),
 ("JHN.11.12", "wird er gesund werden", "interpretive", "σωθήσεται", "wird er gerettet werden", ["wird er genesen"], "σῴζω heisst «retten» und «heilen». Die Jünger meinen die Genesung; «gerettet werden» kann mitklingen (vgl. [[JHN.10.9]])."),
 ("JHN.11.16", "Didymus", "literal", "Δίδυμος", None, ["Zwilling"], "Δίδυμος heisst griechisch «Zwilling»; der Name Thomas hat im Aramäischen dieselbe Bedeutung."),
 ("JHN.11.18", "fünfzehn Stadien", "literal", "σταδίων δεκαπέντε", None, ["knapp drei Kilometer"], "Ein Stadion misst rund 185–192 m; fünfzehn Stadien sind knapp drei Kilometer."),
 ("JHN.11.19", "den Juden", "interpretive", "τῶν Ἰουδαίων", None, ["den Leuten aus Judäa"], "Hier sind Trauergäste gemeint, keine Gegner; die wörtliche Wiedergabe bleibt (Grundentscheid, siehe [[JHN.10.19]])."),
 ("JHN.11.25", "Ich bin die Auferstehung und das Leben", "literal", "Ἐγώ εἰμι ἡ ἀνάστασις καὶ ἡ ζωή", None, None, "ἐγώ εἰμι mit Prädikat einheitlich «Ich bin …» (" + G + "). In 𝔓45 fehlt nach der CNTR-Transkription «und das Leben»; die Transkriptionen von 01, 02, 03, 04, 05, 032, 𝔓66 und 𝔓75 haben es. Der SBLGNT-Apparat verzeichnet hier keine Variante; deshalb ist keine Lesart-Alternative erfasst."),
 ("JHN.11.26", "in Ewigkeit gewiss nicht sterben", "literal", "οὐ μὴ ἀποθάνῃ εἰς τὸν αἰῶνα", None, ["niemals sterben"], "οὐ μή ist die stärkste Verneinung. Weil [[JHN.11.25]] vom Sterben der Glaubenden spricht, beziehen die meisten Ausleger den Satz auf ein Leben, das der Tod nicht beendet, nicht auf das Ausbleiben des leiblichen Todes."),
 ("JHN.11.27", "glaube", "adapted", "πεπίστευκα", "habe geglaubt", ["bin zum Glauben gekommen"], "Perfekt: ein Glaube, der begonnen hat und besteht."),
 ("JHN.11.27", "der in die Welt kommt", "literal", "ὁ εἰς τὸν κόσμον ἐρχόμενος", None, ["der in die Welt kommen soll"], "Partizip Präsens, oft als Titel verstanden: «der Kommende» (vgl. [[JHN.1.9]], [[JHN.6.14]])."),
 ("JHN.11.33", "zornig erregt", "interpretive", "ἐνεβριμήσατο", "schnaubte", ["tief bewegt", "ergrimmte", "empört"], "ἐμβριμάομαι bezeichnet sonst heftigen Unmut oder scharfes Anfahren (vgl. [[MRK.1.43]], [[MRK.14.5]]). Viele Übersetzungen mildern es zu «tief bewegt». Worüber Jesus zornig ist (über den Tod, die Klage oder den Unglauben), sagt der Text nicht; die Auslegungen gehen auseinander. Ebenso [[JHN.11.38]]."),
 ("JHN.11.33", "erschütterte", "adapted", "ἐτάραξεν ἑαυτόν", "verwirrte sich selbst", ["wurde erschüttert", "war tief erschüttert"], "Aktiv mit Reflexivpronomen: Jesus ist selbst der Handelnde. Dasselbe Verb in [[JHN.12.27]] und [[JHN.13.21]]."),
 ("JHN.11.35", "weinte", "literal", "ἐδάκρυσεν", None, ["brach in Tränen aus"], "δακρύω heisst «Tränen vergiessen»; für Maria und die Juden steht κλαίω «weinen, laut klagen» ([[JHN.11.31]], [[JHN.11.33]]). Im Deutschen heissen beide «weinen»."),
 ("JHN.11.39", "der vierte Tag", "adapted", "τεταρταῖος", "ein Viertägiger", None, "Er ist «ein Viertägiger», d. h. seit vier Tagen tot (vgl. [[JHN.11.17]])."),
 ("JHN.11.44", "Schweisstuch", "literal", "σουδαρίῳ", None, ["Tuch"], "σουδάριον (lateinisch sudarium) ist ein Tuch zum Abwischen des Schweisses; dasselbe Wort in [[JHN.20.7]]."),
 ("JHN.11.47", "eine Sitzung des Hohen Rates", "adapted", "συνέδριον", "einen Rat", ["den Hohen Rat"], "συνέδριον ohne Artikel: eine Versammlung des Rates, nicht die Behörde als ganze."),
 ("JHN.11.48", "den Ort", "interpretive", "τὸν τόπον", None, ["die heilige Stätte", "den Tempel", "unser Land"], "τόπος «Ort» meint hier wahrscheinlich den Tempel (vgl. [[ACT.6.13]]–[[ACT.6.14]]), vielleicht auch Jerusalem oder das Land."),
 ("JHN.11.48", "die Nation", "literal", "τὸ ἔθνος", None, ["das Volk"], "Um ἔθνος und λαός ([[JHN.11.50]]) zu unterscheiden, steht für ἔθνος «Nation» und für λαός «Volk»; ebenso [[JHN.11.50]]–[[JHN.11.52]]."),
 ("JHN.11.51", "weissagte er", "literal", "ἐπροφήτευσεν", None, ["redete er prophetisch"], "Der Erzähler deutet das Wort des Kajafas als Weissagung, die dieser als amtierender Hohepriester ausspricht, ohne sie selbst so zu meinen."),
 ("JHN.11.52", "zu einer Einheit", "adapted", "εἰς ἕν", "in eins", None, "Vgl. [[JHN.10.16]] und [[JHN.10.30]]."),
 ("JHN.11.55", "zu reinigen", "literal", "ἁγνίσωσιν", None, ["zu heiligen"], "Wer kultisch unrein war, musste sich vor dem Passa reinigen (vgl. [[NUM.9.6]]–[[NUM.9.10]], [[2CH.30.17]]–[[2CH.30.18]])."),
]

DEC_GSW = [
 ("JHN.10.1", "Amen, amen, ich säge eu", "literal", "Ἀμὴν ἀμὴν λέγω ὑμῖν", None, None, "ἀμήν wird nöd übersetzt, sondern als «Amen» bhalte (Grundentscheid, lueg johannes_text_01_03.py). Bim Johannes 25-mal verdopplet (Zellig us de SBLGNT-Token)."),
 ("JHN.10.6", "Bildwort", "interpretive", "παροιμίαν", None, ["Glichnis", "Rätselred"], "παροιμία isch bim Johannes e verhüllti Red i Bilder, wo mer zerscht mues verstaa (vgl. [[JHN.16.25]])."),
 ("JHN.10.7", "Ich bin d Tüür", "literal", "ἐγώ εἰμι ἡ θύρα", None, None, "ἐγώ εἰμι mit eme Bild immer «Ich bin …» (Grundentscheid)."),
 ("JHN.10.11", "de guet Hirt", "traditional", "ὁ ποιμὴν ὁ καλός", "de Hirt, de guet", ["de rächt Hirt", "de schön Hirt"], "καλός heisst «schön, rächt, tüchtig, guet»: de Hirt, wie n er sött sii, im Gägesatz zum Taglöhner ([[JHN.10.12]])."),
 ("JHN.10.11", "git sis Läbe häre", "interpretive", "τὴν ψυχὴν αὐτοῦ τίθησιν", "leit sini Seel ane", ["setzt sis Läbe ii"], "ψυχή meint da s Läbe; gliich i [[JHN.10.15]], [[JHN.10.17]] und [[JHN.10.18]]."),
 ("JHN.10.12", "De Taglöhner", "adapted", "ὁ μισθωτὸς", "dä, wo um Lohn aagstellt isch", ["de Mietling"], "μισθωτός isch eine, wo für Lohn schaffet."),
 ("JHN.10.19", "de Jude", "interpretive", "τοῖς Ἰουδαίοις", None, ["de jüdische Füerer", "de Lüüt us Judäa"], "Grundentscheid: οἱ Ἰουδαῖοι wörtlich «d Jude». S Wort meint da Gägner vom Jesus z Jerusalem ([[JHN.10.31]]), e gspalteni Mängi ([[JHN.10.19]]) und Truurgäscht und Gläubigi ([[JHN.11.19]], [[JHN.11.45]]). De Jesus, sini Jünger, d Marta, d Maria und de Lazarus sind sälber Jude."),
 ("JHN.10.22", "s Fäscht vo de Tämpelwiiig", "adapted", "τὰ ἐγκαίνια", "d Iiwiiig", ["Chanukka"], "S Fäscht erinneret a d Wiiig vom Tämpel under em Judas Makkabäus ([[1MA.4.52]]–[[1MA.4.59]]); hüt Chanukka."),
 ("JHN.10.24", "laasch üs no zable", "interpretive", "τὴν ψυχὴν ἡμῶν αἴρεις", "hebsch üsi Seel", ["hebsch üs hii"], "D Wändig meint wahrschiinli Spannig und Unsicherheit; si cha au «ufrege» heisse."),
 ("JHN.10.29", "grösser als alli", "interpretive", "ὃ δέδωκέν μοι πάντων μεῖζων ἐστίν", None, ["Was min Vatter mir gää hät, isch grösser als alles", "Min Vatter, wo mir si gää hät, isch grösser als alli"], "De SBLGNT list ὃ («was», sächlich) mit μείζων («grösser», männlich, uf de Vatter bezoge). Das isch grammatisch hert; anderi Usgabe läsed glatter (lueg d Alternative)."),
 ("JHN.10.30", "eis", "literal", "ἕν", None, None, "ἕν isch sächlich: «eis», nöd «eine» (εἷς)."),
 ("JHN.10.40", "er isch dört bliibe", "literal", "ἔμεινεν", None, None, "μένω immer «bliibe» (Grundentscheid)."),
 ("JHN.10.41", "Zeiche", "literal", "σημεῖον", None, ["Wunder"], "σημεῖον immer «Zeiche», nöd «Wunder» (Grundentscheid): Si wiised uf de Jesus häre (vgl. [[JHN.20.30]]–[[JHN.20.31]])."),
 ("JHN.11.3", "du lieb häsch", "interpretive", "φιλεῖς", None, None, "Für d Liebi vom Jesus staat φιλέω ([[JHN.11.3]], [[JHN.11.36]], «lieb haa») und ἀγαπάω ([[JHN.11.5]], «gern haa»). Öb de Johannes en Underschid meint, isch umstritte."),
 ("JHN.11.4", "de Herrlichkeit", "literal", "τῆς δόξης", None, None, "δόξα und δοξάζω immer «Herrlichkeit» und «verherrliche» (Grundentscheid)."),
 ("JHN.11.12", "wird er gsund", "interpretive", "σωθήσεται", "wird er grettet", None, "σῴζω heisst «rette» und «heile»; d Jünger meined d Gnesig."),
 ("JHN.11.25", "Ich bin d Uferstehig und s Läbe", "literal", "Ἐγώ εἰμι ἡ ἀνάστασις καὶ ἡ ζωή", None, None, "Grundentscheid «Ich bin …». I 𝔓45 fäält nach de CNTR-Transkription «und s Läbe»; im SBLGNT-Apparat staat kei Variante, drum git s kei Alternative."),
 ("JHN.11.33", "zornig worde", "interpretive", "ἐνεβριμήσατο", "hät gschnaubt", ["isch tüüf bewegt gsii"], "ἐμβριμάομαι meint suscht heftige Unmuet (vgl. [[MRK.1.43]], [[MRK.14.5]]). Wäge was de Jesus zornig isch, seit de Text nöd. Gliich [[JHN.11.38]]."),
 ("JHN.11.33", "hät sich ufgwüelt", "adapted", "ἐτάραξεν ἑαυτόν", "hät sich sälber verwirrt", ["isch erschütteret gsii"], "Aktiv mit «sich»: De Jesus isch sälber de, wo handlet."),
 ("JHN.11.35", "sind d Träne choo", "adapted", "ἐδάκρυσεν", "hät Träne vergosse", ["hät briegget"], "δακρύω heisst «Träne vergüüsse»; für d Maria und d Jude staat κλαίω «briegge, luut chlage» ([[JHN.11.31]], [[JHN.11.33]])."),
 ("JHN.11.48", "de Ort", "interpretive", "τὸν τόπον", None, ["de Tämpel"], "τόπος meint da wahrschiinli de Tämpel."),
 ("JHN.11.48", "d Nation", "literal", "τὸ ἔθνος", None, ["s Volk"], "ἔθνος «Nation», λαός ([[JHN.11.50]]) «Volk»."),
]

# Lesarten-Alternativen: (Variante:Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw,
#  Wortlaute de, Wortlaute gsw, Entstehung de, Entstehung gsw[, verwandte Varianten]).
#  Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung, erste Hand).
ALTS = [
 ("VAR-SBLGNTAPP-JHN-010-008-01:R2", "JHN.10.8", "Alle, die vor mir gekommen sind", "Alle, die gekommen sind", "All, wo vor mir choo sind", "All, wo choo sind", "mittel",
  "Ohne «vor mir» gilt die Aussage allgemein allen, die gekommen sind.", "Ohni «vor mir» gilt d Uussag allgemein für all, wo choo sind.",
  {"R1": [("πρὸ ἐμοῦ", "vor mir", None)], "R2": [("–", "(fehlt)", None)]},
  {"R1": [("πρὸ ἐμοῦ", "vor mir", None)], "R2": [("–", "(fäält)", None)]},
  ["«Vor mir» kann weggelassen worden sein, weil es so klingt, als wären alle Früheren, auch die Propheten, Diebe und Räuber; es kann auch zur Verdeutlichung ergänzt worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 𝔓45 und 𝔓75 ohne «vor mir», 02, 03, 05, 032 und 𝔓66 mit."],
  ["«Vor mir» cha wäggloo worde sii, wil s tönt, wie wänn all Früehnere, au d Prophete, Dieb und Röiber wäred; es cha au zur Verdüütlichig ergänzt worde sii.",
   "Nach de automatische Zueornig läsed 01, 𝔓45 und 𝔓75 ohni «vor mir», 02, 03, 05, 032 und 𝔓66 mit."]),
 ("VAR-SBLGNTAPP-JHN-010-016-02:R2", "JHN.10.16", "sie werden eine Herde werden", "es wird eine Herde werden", "si wärded ei Herde wärde", "es wird ei Herde wärde", "gering",
  "Mit dem Singular wird die eine Herde selbst zum Subjekt.", "Mit em Singular wird di ei Herde sälber zum Subjekt.",
  {"R1": [("γενήσονται", "sie werden werden", None)], "R2": [("γενήσεται", "es wird werden", None)]},
  {"R1": [("γενήσονται", "si wärded wärde", None)], "R2": [("γενήσεται", "es wird wärde", None)]},
  ["Der Singular kann an «eine Herde» angeglichen sein; der Plural knüpft an «sie werden hören» an.",
   "Laut der automatischen Zuordnung lesen 01, 02, 𝔓66 und 𝔓75 den Singular, 03, 05, 032 und 𝔓45 den Plural."],
  ["De Singular cha a «ei Herde» aaglichen sii; de Plural chnüpft a «si wärded lose» aa.",
   "Nach de automatische Zueornig läsed 01, 02, 𝔓66 und 𝔓75 de Singular, 03, 05, 032 und 𝔓45 de Plural."]),
 ("VAR-SBLGNTAPP-JHN-010-018-01:R2", "JHN.10.18", "Niemand nimmt es mir weg", "Niemand hat es mir weggenommen", "Niemer nimmt mir s wäg", "Niemer hät mir s wäggnoo", "mittel",
  "Vergangenheitsform: Der Satz blickt zurück, als wäre das Hingeben schon geschehen.", "Vergangeheit: De Satz luegt zrugg, wie wänn s Häregää scho gscheh wär.",
  {"R1": [("αἴρει", "nimmt", "Treg, NA28, RP")], "R2": [("ἦρεν", "hat genommen", "WH")]},
  {"R1": [("αἴρει", "nimmt", "Treg, NA28, RP")], "R2": [("ἦρεν", "hät gnoo", "WH")]},
  ["Der Aorist kann aus der Rückschau nach Ostern stammen; er kann auch ursprünglich sein und später an das Präsens der Umgebung angeglichen worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 𝔓45 und 𝔓75 ἦρεν, 02, 05, 032 und 𝔓66 αἴρει."],
  ["De Aorist cha us em Rückblick nach Oschtere stamme; er cha au ursprünglich sii und spööter as Präsens drumume aaglichen worde sii.",
   "Nach de automatische Zueornig läsed 01, 03, 𝔓45 und 𝔓75 ἦρεν, 02, 05, 032 und 𝔓66 αἴρει."]),
 ("VAR-SBLGNTAPP-JHN-010-026-02:R2", "JHN.10.26", "zu meinen Schafen gehört", "zu meinen Schafen gehört, wie ich euch gesagt habe", "zu mine Schaaf ghööred", "zu mine Schaaf ghööred, wie n ich eu gseit han", "gering",
  "Mit dem Zusatz verweist Jesus auf früher Gesagtes.", "Mit em Zuesatz verwiist de Jesus uf öppis, won er früener gseit hät.",
  {"R1": [("ἐμῶν", "meinen", None)], "R2": [("ἐμῶν καθὼς εἶπον ὑμῖν", "meinen, wie ich euch gesagt habe", "mit Zusatz")]},
  {"R1": [("ἐμῶν", "mine", None)], "R2": [("ἐμῶν καθὼς εἶπον ὑμῖν", "mine, wie n ich eu gseit han", "mit Zuesatz")]},
  ["Der Zusatz kann an [[JHN.10.25]] («Ich habe es euch gesagt») anknüpfen; er kann auch weggelassen worden sein, weil Jesus das zuvor nicht wörtlich gesagt hat.",
   "Laut der automatischen Zuordnung lesen 02, 05 und 𝔓66 mit dem Zusatz, 01, 03, 032 und 𝔓75 ohne; 0258 hat einen abweichenden Wortlaut."],
  ["De Zuesatz cha a [[JHN.10.25]] aachnüpfe; er cha au wäggloo worde sii, wil de Jesus das vorher nöd wörtlich gseit hät.",
   "Nach de automatische Zueornig läsed 02, 05 und 𝔓66 mit Zuesatz, 01, 03, 032 und 𝔓75 ohni; 0258 hät en andere Wortlut."]),
 ("VAR-SBLGNTAPP-JHN-010-029-03:R2", "JHN.10.29", "Mein Vater – was er mir gegeben hat – ist grösser als alle", "Was mein Vater mir gegeben hat, ist grösser als alles",
  "Min Vatter – was er mir gää hät – isch grösser als alli", "Was min Vatter mir gää hät, isch grösser als alles", "bedeutsam",
  "Mit dem sächlichen μεῖζον ist nicht der Vater, sondern das, was er gegeben hat, «grösser als alles».", "Mit em sächliche μεῖζον isch nöd de Vatter, sondern das, won er gää hät, «grösser als alles».",
  {"R1": [("πάντων μεῖζων", "grösser als alle (männlich, auf den Vater bezogen)", "Holmes, SBLGNT")], "R2": [("πάντων μεῖζόν", "grösser als alles (sächlich, auf das Gegebene bezogen)", "WH, Treg, NA28")],
   "R3": [("μείζων πάντων", "grösser als alle (männlich; andere Wortfolge)", "RP")]},
  {"R1": [("πάντων μεῖζων", "grösser als alli (männlich, uf de Vatter bezoge)", "Holmes, SBLGNT")], "R2": [("πάντων μεῖζόν", "grösser als alles (sächlich, uf das, wo gää isch)", "WH, Treg, NA28")],
   "R3": [("μείζων πάντων", "grösser als alli (männlich; anderi Wortfolg)", "RP")]},
  ["Die sächliche Form ergibt mit ὃ einen glatten Satz über das Gegebene, die männliche mit ὅς einen glatten Satz über den Vater. Die gemischte Lesart ὃ … μείζων ist grammatisch hart; manche halten sie gerade deshalb für ursprünglich, andere für eine Vermischung der beiden glatten Formen.",
   "Laut der automatischen Zuordnung lesen 01, 05 und 032 πάντων μείζων (R1), 03 und 𝔓75 μεῖζον (R2), 02 und 𝔓66 μείζων πάντων (R3). Beim Relativpronomen (VAR-SBLGNTAPP-JHN-010-029-01) lesen nach derselben Zuordnung 01, 03, 05 und 032 ὃ, 02, 𝔓66 und 𝔓75 ὅς; für 03 verzeichnet die CNTR-Transkription an dieser Stelle eine Korrektur."],
  ["Di sächlich Form git mit ὃ en glatte Satz über das, wo gää isch, di männlich mit ὅς en glatte Satz über de Vatter. Di gmischt Läsart ὃ … μείζων isch grammatisch hert; für di einte isch si grad drum ursprünglich, für anderi e Vermischig vo de beide glatte Forme.",
   "Nach de automatische Zueornig läsed 01, 05 und 032 R1, 03 und 𝔓75 R2, 02 und 𝔓66 R3. Bim Relativpronomen läsed 01, 03, 05 und 032 ὃ, 02, 𝔓66 und 𝔓75 ὅς."],
  ["VAR-SBLGNTAPP-JHN-010-029-01"]),
 ("VAR-SBLGNTAPP-JHN-010-029-01:R2", "JHN.10.29", "Mein Vater – was er mir gegeben hat – ist grösser als alle", "Mein Vater, der sie mir gegeben hat, ist grösser als alle",
  "Min Vatter – was er mir gää hät – isch grösser als alli", "Min Vatter, wo mir si gää hät, isch grösser als alli", "bedeutsam",
  "Mit ὅς («der») ist der ganze Satz eine Aussage über den Vater; «sie» (die Schafe) ist sinngemäss ergänzt.", "Mit ὅς («wo») isch de ganz Satz e Uussag über de Vatter; «si» (d Schaaf) isch sinngemäss ergänzt.",
  {"R1": [("ὃ", "was", "WH, Treg, NA28, SBLGNT")], "R2": [("ὃς", "der", "RP")]},
  {"R1": [("ὃ", "was", "WH, Treg, NA28, SBLGNT")], "R2": [("ὃς", "wo", "RP")]},
  ["ὅς passt zum männlichen μείζων und glättet den Satz; ὃ passt zum sächlichen μεῖζον (siehe VAR-SBLGNTAPP-JHN-010-029-03).",
   "Laut der automatischen Zuordnung lesen 01, 03, 05 und 032 ὃ, 02, 𝔓66 und 𝔓75 ὅς; für 03 verzeichnet die CNTR-Transkription an dieser Stelle eine Korrektur."],
  ["ὅς passt zum männliche μείζων und macht de Satz glatt; ὃ passt zum sächliche μεῖζον.",
   "Nach de automatische Zueornig läsed 01, 03, 05 und 032 ὃ, 02, 𝔓66 und 𝔓75 ὅς."],
  ["VAR-SBLGNTAPP-JHN-010-029-03"]),
 ("VAR-SBLGNTAPP-JHN-010-038-02:R2", "JHN.10.38", "damit ihr erkennt und immer mehr erkennt", "damit ihr erkennt und glaubt",
  "demit ir erchänned und immer meh erchänned", "demit ir erchänned und glaubed", "gering",
  "Statt des wiederholten «erkennen» steht «glauben».", "Statt em widerholte «erchänne» staat «glaube».",
  {"R1": [("γινώσκητε", "erkennt (dauernd)", None)], "R2": [("πιστεύσητε", "glaubt", None)]},
  {"R1": [("γινώσκητε", "erchänned (dauernd)", None)], "R2": [("πιστεύσητε", "glaubed", None)]},
  ["Die Wiederholung desselben Verbs kann als ungewöhnlich empfunden und durch «glauben» ersetzt worden sein, das im Zusammenhang mehrfach vorkommt.",
   "Laut der automatischen Zuordnung lesen 01 und 02 «glaubt», 03, 032, 𝔓45, 𝔓66 und 𝔓75 «erkennt»; 05 hat einen abweichenden Wortlaut."],
  ["Di Widerholig vom gliiche Verb cha als ungwöhnlich empfunde und dur «glaube» ersetzt worde sii.",
   "Nach de automatische Zueornig läsed 01 und 02 «glaubed», 03, 032, 𝔓45, 𝔓66 und 𝔓75 «erchänned»; 05 hät en andere Wortlut."]),
 ("VAR-SBLGNTAPP-JHN-011-041-01:R2", "JHN.11.41", "Da nahmen sie den Stein weg.", "Da nahmen sie den Stein weg, wo der Tote lag.",
  "Dänn händ si de Stei wäggnoo.", "Dänn händ si de Stei wäggnoo, wo de Tot gläge isch.", "gering",
  "Mit erklärendem Zusatz.", "Mit erklärendem Zuesatz.",
  {"R1": [("λίθον", "Stein", None)], "R2": [("λίθον οὗ ἦν ὁ τεθνηκὼς κειμένος", "Stein, wo der Tote lag", "mit Zusatz")]},
  {"R1": [("λίθον", "Stei", None)], "R2": [("λίθον οὗ ἦν ὁ τεθνηκὼς κειμένος", "Stei, wo de Tot gläge isch", "mit Zuesatz")]},
  ["Der Zusatz verdeutlicht, welcher Stein gemeint ist.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 04, 05, 032, 𝔓66 und 𝔓75 ohne den Zusatz; ihn haben unter den erfassten Texten nur die gedruckten Ausgaben KJTR, RP und Stephanus."],
  ["De Zuesatz macht dütlich, weli Stei gmeint isch.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 04, 05, 032, 𝔓66 und 𝔓75 ohni Zuesatz; en händ under de erfasste Text nu di druckte Usgabe KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-JHN-011-050-02:R2", "JHN.11.50", "für euch", "für uns", "für eu", "für üs", "gering",
  "Mit «uns» schliesst Kajafas sich selbst ein.", "Mit «üs» zellt sich de Kajafas sälber derzue.",
  {"R1": [("ὑμῖν", "euch", None)], "R2": [("ἡμῖν", "uns", None)]},
  {"R1": [("ὑμῖν", "eu", None)], "R2": [("ἡμῖν", "üs", None)]},
  ["ὑμῖν und ἡμῖν wurden im späteren Griechisch gleich ausgesprochen und beim Abschreiben oft verwechselt.",
   "Laut der automatischen Zuordnung lesen 03, 05, 𝔓45, 𝔓66 und 𝔓75 «euch», 02 und 032 «uns»; 01 hat einen abweichenden Wortlaut."],
  ["ὑμῖν und ἡμῖν sind im spöötere Griechisch gliich usgsproche und bim Abschriibe oft verwächslet worde.",
   "Nach de automatische Zueornig läsed 03, 05, 𝔓45, 𝔓66 und 𝔓75 «eu», 02 und 032 «üs»; 01 hät en andere Wortlut."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-010-001-042", "JHN.10.1-JHN.10.42", "section", "Der gute Hirte; am Fest der Tempelweihe",
  ["TU-JHN-010-001-006", "TU-JHN-010-007-018", "TU-JHN-010-019-021", "TU-JHN-010-022-039", "TU-JHN-010-040-042"],
  "Jesus spricht in einem Bildwort vom Hirten, der durch die Tür in den Hof der Schafe geht, und vom Dieb, der anderswo einsteigt; die Zuhörer verstehen es nicht. Er sagt von sich: «Ich bin die Tür» und «Ich bin der gute Hirte», der sein Leben für die Schafe hingibt und es wieder nimmt; auch andere Schafe muss er führen. Unter den Juden entsteht eine Spaltung. Am Fest der Tempelweihe fordern die Juden ihn auf, offen zu sagen, ob er der Christus ist. Jesus verweist auf seine Werke und sagt, sie glaubten nicht, weil sie nicht zu seinen Schafen gehörten; niemand werde seine Schafe aus seiner und des Vaters Hand reissen: «Ich und der Vater sind eins.» Sie wollen ihn steinigen und festnehmen; er entkommt und bleibt jenseits des Jordan, wo viele an ihn glauben.", SEG),
 ("TU-JHN-010-001-006", "JHN.10.1-JHN.10.6", "discourse", "Das Bildwort von Tür und Hirte", None,
  "Wer nicht durch die Tür in den Hof der Schafe hineingeht, ist ein Dieb und Räuber. Dem Hirten öffnet der Türhüter; er ruft seine Schafe mit Namen, führt sie hinaus und geht vor ihnen her, und sie folgen ihm, weil sie seine Stimme kennen. Einem Fremden folgen sie nicht. Die Zuhörer verstehen nicht, was Jesus damit sagt.", None),
 ("TU-JHN-010-007-018", "JHN.10.7-JHN.10.18", "discourse", "Ich bin die Tür – ich bin der gute Hirte", None,
  "Jesus nennt sich die Tür der Schafe: Wer durch ihn hineingeht, wird gerettet und findet Weide; er ist gekommen, damit sie Leben und Überfluss haben. Er ist der gute Hirte, der sein Leben für die Schafe hingibt, anders als der Lohnarbeiter, der vor dem Wolf flieht. Er kennt die Seinen und sie kennen ihn, wie der Vater ihn kennt und er den Vater. Auch andere Schafe, die nicht aus diesem Hof sind, muss er führen, und sie werden eine Herde werden. Niemand nimmt ihm sein Leben; er gibt es von sich aus hin und hat Vollmacht, es wieder zu nehmen. Diesen Auftrag hat er vom Vater.", None),
 ("TU-JHN-010-019-021", "JHN.10.19-JHN.10.21", "narrative", "Spaltung unter den Juden", None,
  "Wegen dieser Worte sind die Juden gespalten: Viele sagen, er habe einen Dämon und sei von Sinnen; andere halten dagegen, so rede kein Besessener, und ein Dämon könne Blinden nicht die Augen öffnen.", None),
 ("TU-JHN-010-022-039", "JHN.10.22-JHN.10.39", "dialogue", "Am Fest der Tempelweihe", None,
  "Im Winter, am Fest der Tempelweihe, umringen die Juden Jesus in der Säulenhalle Salomos und verlangen, er solle offen sagen, ob er der Christus sei. Jesus verweist auf seine Werke im Namen des Vaters: Sie glauben nicht, weil sie nicht zu seinen Schafen gehören. Seinen Schafen gibt er ewiges Leben, und niemand reisst sie aus seiner und des Vaters Hand: «Ich und der Vater sind eins.» Die Juden heben Steine auf, weil er sich als Mensch zu Gott mache. Jesus antwortet mit [[PSA.82.6]] und verweist erneut auf die Werke, damit sie erkennen, dass der Vater in ihm ist und er im Vater. Sie suchen ihn festzunehmen, doch er entkommt.", None),
 ("TU-JHN-010-040-042", "JHN.10.40-JHN.10.42", "narrative", "Jenseits des Jordan", None,
  "Jesus geht an den Ort jenseits des Jordan, wo Johannes zuerst getauft hatte, und bleibt dort. Viele kommen zu ihm und sagen, Johannes habe kein Zeichen getan, aber alles, was er über ihn gesagt habe, sei wahr gewesen; viele glauben dort an ihn.", None),
 ("TU-JHN-011-001-057", "JHN.11.1-JHN.11.57", "section", "Die Auferweckung des Lazarus und der Todesbeschluss",
  ["TU-JHN-011-001-016", "TU-JHN-011-017-027", "TU-JHN-011-028-037", "TU-JHN-011-038-044", "TU-JHN-011-045-053", "TU-JHN-011-054-057"],
  "Lazarus aus Betanien, der Bruder von Marta und Maria, ist krank; die Schwestern lassen es Jesus ausrichten. Jesus sagt, die Krankheit diene der Herrlichkeit Gottes, bleibt noch zwei Tage und geht dann trotz der Gefahr nach Judäa; Lazarus ist inzwischen gestorben und liegt schon vier Tage im Grab, als Jesus ankommt. Zu Marta sagt Jesus: «Ich bin die Auferstehung und das Leben», und sie bekennt ihn als den Christus, den Sohn Gottes. Maria und die Trauernden weinen; Jesus wird zornig erregt und weint. Am Grab lässt er den Stein wegnehmen, dankt dem Vater und ruft Lazarus heraus; der Tote kommt heraus. Viele Juden glauben an Jesus, einige melden es den Pharisäern. Im Hohen Rat sagt Kajafas, es sei besser, dass ein Mensch für das Volk sterbe; der Erzähler deutet das als Weissagung über den Tod Jesu. Von da an planen sie, ihn zu töten. Jesus zieht sich nach Efraim zurück. Vor dem Passa fragen sich die Leute im Tempel, ob er zum Fest kommt; die Hohepriester und Pharisäer haben angeordnet, ihn zu melden.", SEG),
 ("TU-JHN-011-001-016", "JHN.11.1-JHN.11.16", "narrative", "Die Nachricht von der Krankheit des Lazarus", None,
  "Marta und Maria lassen Jesus ausrichten, dass Lazarus, den er lieb hat, krank ist. Jesus sagt, die Krankheit führe nicht zum Tod, sondern diene der Herrlichkeit Gottes, und bleibt noch zwei Tage, wo er ist. Dann will er wieder nach Judäa, obwohl die Juden ihn dort steinigen wollten; wer am Tag umhergeht, stösst nicht an. Er sagt, Lazarus sei eingeschlafen; als die Jünger das wörtlich verstehen, sagt er offen, Lazarus sei gestorben, und er freue sich ihretwegen, nicht dort gewesen zu sein, damit sie glauben. Thomas sagt: «Lasst auch uns gehen, damit wir mit ihm sterben!»", None),
 ("TU-JHN-011-017-027", "JHN.11.17-JHN.11.27", "dialogue", "Jesus und Marta: Ich bin die Auferstehung und das Leben", None,
  "Lazarus liegt schon vier Tage im Grab; viele Juden sind gekommen, um die Schwestern zu trösten. Marta geht Jesus entgegen: Wäre er hier gewesen, wäre ihr Bruder nicht gestorben; doch auch jetzt werde Gott ihm geben, worum er bitte. Jesus sagt, ihr Bruder werde auferstehen; Marta denkt an die Auferstehung am letzten Tag. Jesus antwortet: «Ich bin die Auferstehung und das Leben»; wer an ihn glaubt, wird leben, auch wenn er stirbt. Marta bekennt, dass er der Christus ist, der Sohn Gottes, der in die Welt kommt.", None),
 ("TU-JHN-011-028-037", "JHN.11.28-JHN.11.37", "narrative", "Jesus und Maria; Jesus weint", None,
  "Marta ruft Maria heimlich; Maria eilt zu Jesus, und die Juden folgen ihr in der Meinung, sie gehe zum Grab. Sie fällt ihm zu Füssen mit denselben Worten wie Marta. Als Jesus sie und die Juden weinen sieht, wird er im Geist zornig erregt und erschüttert; er fragt nach dem Grab, und er weint. Die einen sehen darin, wie lieb er Lazarus hatte; andere fragen, ob der, der dem Blinden die Augen öffnete, sein Sterben nicht hätte verhindern können.", None),
 ("TU-JHN-011-038-044", "JHN.11.38-JHN.11.44", "narrative", "Die Auferweckung des Lazarus", None,
  "Wieder zornig erregt kommt Jesus zur Grabhöhle und lässt den Stein wegnehmen, obwohl Marta einwendet, Lazarus rieche schon. Er erinnert sie, dass sie die Herrlichkeit Gottes sehen wird, wenn sie glaubt. Jesus dankt dem Vater, dass er ihn erhört hat, und sagt, er spreche es um der Menge willen, damit sie glaubt, dass der Vater ihn gesandt hat. Dann ruft er laut: «Lazarus, komm heraus!» Der Tote kommt heraus, mit Binden umwickelt, und Jesus lässt ihn losbinden.", None),
 ("TU-JHN-011-045-053", "JHN.11.45-JHN.11.53", "narrative", "Der Beschluss des Hohen Rates", None,
  "Viele Juden, die es gesehen haben, glauben an Jesus; einige berichten es den Pharisäern. Die Hohepriester und Pharisäer berufen eine Sitzung des Hohen Rates ein: Wenn alle an ihn glauben, werden die Römer kommen und ihnen Ort und Nation wegnehmen. Kajafas, Hohepriester in jenem Jahr, sagt, es sei besser, dass ein Mensch für das Volk sterbe. Der Erzähler deutet das als Weissagung, dass Jesus für die Nation sterben werde, und nicht nur für sie, sondern um auch die zerstreuten Kinder Gottes zu einer Einheit zusammenzuführen. Von diesem Tag an planen sie, ihn zu töten.", None),
 ("TU-JHN-011-054-057", "JHN.11.54-JHN.11.57", "narrative", "Rückzug nach Efraim; vor dem Passa", None,
  "Jesus geht nicht mehr offen unter den Juden umher, sondern bleibt mit den Jüngern in Efraim nahe der Wüste. Vor dem Passa ziehen viele nach Jerusalem hinauf, um sich zu reinigen; im Tempel suchen sie Jesus und fragen einander, ob er zum Fest kommen werde. Die Hohepriester und Pharisäer haben angeordnet, wer wisse, wo er sei, solle es melden, damit sie ihn festnehmen können.", None),
]
UNITS_GSW = {
 "TU-JHN-010-001-042": ("De guet Hirt; am Fäscht vo de Tämpelwiiig", "De Jesus redt imene Bildwort vom Hirt, wo dur d Tüür in Hof vo de Schaaf ine gaat, und vom Dieb, wo anderswo übere stiigt; d Zuehörer verstönd s nöd. Er seit vo sich: «Ich bin d Tüür» und «Ich bin de guet Hirt», wo sis Läbe für d Schaaf häregit und s wider nimmt; au anderi Schaaf mues er füere. Under de Jude git s e Spaltig. Am Fäscht vo de Tämpelwiiig verlanged d Jude, er söll offe säge, öb er de Christus seig. De Jesus verwiist uf sini Wärch und seit, si glaubed nöd, wil si nöd zu sine Schaaf ghööred; niemer werdi sini Schaaf us sinere und em Vatter sinere Hand riisse: «Ich und de Vatter sind eis.» Si wänd en steinige und packe; er entwütscht und bliibt änet em Jordan, wo vili a en glaubed."),
 "TU-JHN-010-001-006": ("S Bildwort vo de Tüür und em Hirt", "Wer nöd dur d Tüür in Hof vo de Schaaf ine gaat, isch en Dieb und en Röiber. Em Hirt macht de Tüürhüeter uf; er rüeft sini Schaaf bim Name, füert si use und gaat vor ine här, und si folged ihm, wil si sini Stimm känned. Eme Frömde folged si nöd. D Zuehörer verstönd nöd, was de Jesus demit seit."),
 "TU-JHN-010-007-018": ("Ich bin d Tüür – ich bin de guet Hirt", "De Jesus nännt sich d Tüür vo de Schaaf: Wer dur ihn ine gaat, wird grettet und findt Weid; er isch choo, demit si Läbe und meh als gnueg händ. Er isch de guet Hirt, wo sis Läbe für d Schaaf häregit, nöd wie de Taglöhner, wo vor em Wolf flüchtet. Er kännt di Sine und si känned ihn, wie de Vatter ihn kännt und er de Vatter. Au anderi Schaaf, wo nöd us däm Hof sind, mues er füere, und si wärded ei Herde wärde. Niemer nimmt ihm sis Läbe; er gits vo sich uus häre und hät d Vollmacht, s wider z neh. Dä Uftrag hät er vom Vatter."),
 "TU-JHN-010-019-021": ("Spaltig under de Jude", "Wäge dene Wort sind d Jude gspalte: Vili säged, er heig en Dämon und seig vo Sinne; anderi händ dergäge, so redi kein Bsässne, und en Dämon chön Blinde nöd d Auge uftue."),
 "TU-JHN-010-022-039": ("Am Fäscht vo de Tämpelwiiig", "Im Winter, am Fäscht vo de Tämpelwiiig, umringed d Jude de Jesus i de Säulehalle vom Salomo und verlanged, er söll offe säge, öb er de Christus seig. De Jesus verwiist uf sini Wärch im Name vom Vatter: Si glaubed nöd, wil si nöd zu sine Schaaf ghööred. Sine Schaaf git er ewigs Läbe, und niemer riisst si us sinere und em Vatter sinere Hand: «Ich und de Vatter sind eis.» D Jude nämed Stei uf, wil er sich als Mänsch zu Gott machi. De Jesus antwortet mit [[PSA.82.6]] und verwiist nomal uf d Wärch, demit si erchänned, dass de Vatter in ihm isch und er im Vatter. Si sueched en z packe, aber er entwütscht."),
 "TU-JHN-010-040-042": ("Änet em Jordan", "De Jesus gaat a de Ort änet em Jordan, wo de Johannes zerscht tauft hät, und bliibt dört. Vili chömed zu ihm und säged, de Johannes heig kei Zeiche gmacht, aber alles, won er über ihn gseit heig, seig wahr gsii; vili glaubed dört a en."),
 "TU-JHN-011-001-057": ("D Uferweckig vom Lazarus und de Todesbeschluss", "De Lazarus vo Betanie, de Brueder vo de Marta und de Maria, isch chrank; d Schwöschtere lönd s em Jesus usrichte. De Jesus seit, d Chranket dieni de Herrlichkeit vo Gott, bliibt no zwei Täg und gaat dänn trotz de Gfaar uf Judäa; de Lazarus isch underdesse gstorbe und liit scho vier Täg im Grab, wo de Jesus aachunnt. Zur Marta seit de Jesus: «Ich bin d Uferstehig und s Läbe», und si bekännt en als de Christus, de Sohn vo Gott. D Maria und d Truurgäscht briegged; de Jesus wird zornig, und em chömed d Träne. Bim Grab laat er de Stei wägneh, dankt em Vatter und rüeft de Lazarus use; de Tot chunnt use. Vili Jude glaubed a de Jesus, es paar mälded s de Pharisäer. Im Hohe Raat seit de Kajafas, es seig besser, dass ein Mänsch für s Volk stärbi; de Verzeller deutet das als Prophezeiig über de Tod vom Jesus. Vo dänn aa planed si, en z töte. De Jesus zieht sich uf Efraim zrugg. Vor em Passa fröged sich d Lüüt im Tämpel, öb er as Fäscht chömi; d Hoheprieschter und d Pharisäer händ aagordnet, mer söll en mälde."),
 "TU-JHN-011-001-016": ("D Nachricht vo de Chranket vom Lazarus", "D Marta und d Maria lönd em Jesus usrichte, dass de Lazarus, won er lieb hät, chrank isch. De Jesus seit, d Chranket füeri nöd zum Tod, sondern dieni de Herrlichkeit vo Gott, und bliibt no zwei Täg, won er isch. Dänn wott er wider uf Judäa, obwohl d Jude en dört händ wele steinige; wer am Tag umelauft, stolperet nöd. Er seit, de Lazarus seig iigschlaafe; wo d Jünger das wörtlich verstönd, seit er offe, de Lazarus seig gstorbe, und er freu sich wäge ine, dass er nöd dört gsii seig, demit si glaubed. De Thomas seit: «Mir gönd au, demit mir mit ihm stärbed!»"),
 "TU-JHN-011-017-027": ("De Jesus und d Marta: Ich bin d Uferstehig und s Läbe", "De Lazarus liit scho vier Täg im Grab; vili Jude sind choo, zum d Schwöschtere tröschte. D Marta gaat em Jesus entgäge: Wänn er da gsii wär, wär ire Brueder nöd gstorbe; aber au jetzt werdi Gott ihm gää, was er erbitti. De Jesus seit, ire Brueder werdi uferstaa; d Marta dänkt a d Uferstehig am letschte Tag. De Jesus antwortet: «Ich bin d Uferstehig und s Läbe»; wer a ihn glaubt, wird läbe, au wänn er stirbt. D Marta bekännt, dass er de Christus isch, de Sohn vo Gott, wo i d Wält chunnt."),
 "TU-JHN-011-028-037": ("De Jesus und d Maria; em Jesus chömed d Träne", "D Marta rüeft heimli d Maria; d Maria gaat schnell zum Jesus, und d Jude gönd ere nache, wil si meined, si gang zum Grab. Si fallt ihm z Füess mit de gliiche Wort wie d Marta. Wo de Jesus gseht, wie si und d Jude briegged, wird er im Geischt zornig und ufgwüelt; er fröget nach em Grab, und em chömed d Träne. Di einte gsehnd drin, wie lieb er de Lazarus gha hät; anderi fröged, öb dä, wo em Blinde d Auge uftaa hät, sis Stärbe nöd hett chöne verhindere."),
 "TU-JHN-011-038-044": ("D Uferweckig vom Lazarus", "Wider zornig chunnt de Jesus zur Grabhöhli und laat de Stei wägneh, obwohl d Marta iiwändt, de Lazarus schmöcki scho. Er erinneret si, dass si d Herrlichkeit vo Gott wird gseh, wänn si glaubt. De Jesus dankt em Vatter, dass er en erhört hät, und seit, er säg das wäge de Mängi, demit si glaubt, dass de Vatter en gschickt hät. Dänn rüeft er luut: «Lazarus, chumm use!» De Tot chunnt use, mit Binde iiwicklet, und de Jesus laat en losbinde."),
 "TU-JHN-011-045-053": ("De Beschluss vom Hohe Raat", "Vili Jude, wo s gseh händ, glaubed a de Jesus; es paar verzelled s de Pharisäer. D Hoheprieschter und d Pharisäer rüefed e Sitzig vom Hohe Raat ii: Wänn alli a ihn glaubed, chömed d Römer und nämed ine de Ort und d Nation wäg. De Kajafas, Hoheprieschter i dem Jahr, seit, es seig besser, dass ein Mänsch für s Volk stärbi. De Verzeller deutet das als Prophezeiig, dass de Jesus für d Nation werdi stärbe, und nöd nu für si, sondern zum au di verstreute Chind vo Gott zu ere Einheit zämezfüere. Vo dem Tag aa planed si, en z töte."),
 "TU-JHN-011-054-057": ("Rückzug uf Efraim; vor em Passa", "De Jesus gaat nüme offe under de Jude ume, sondern bliibt mit de Jünger z Efraim nööch bi de Wüeschti. Vor em Passa gönd vili uf Jerusalem ufe, zum sich reinige; im Tämpel sueched si de Jesus und fröged enand, öb er as Fäscht chömi. D Hoheprieschter und d Pharisäer händ aagordnet, wer wüssi, won er seig, söll s mälde, demit si en chönd packe."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("Die Grundentscheide zu den johanneischen Schlüsselwörtern (λόγος «Wort», ἐγώ εἰμι «Ich bin …», δόξα/δοξάζω «Herrlichkeit/"
  "verherrlichen», σημεῖον «Zeichen», μένω «bleiben», ἀμὴν ἀμήν «Amen, amen», κόσμος «Welt», οἱ Ἰουδαῖοι «die Juden») sind in "
  "scripts/authoring/johannes_text_01_03.py begründet; diese Übersetzung folgt ihnen."),
 ("οἱ Ἰουδαῖοι ist wörtlich mit «die Juden» wiedergegeben. In Kapitel 10–11 meint das Wort Gegner Jesu in Jerusalem "
  "([[JHN.10.31]], [[JHN.11.8]]), eine gespaltene Menge ([[JHN.10.19]]) sowie Trauernde und Glaubende ([[JHN.11.19]], "
  "[[JHN.11.45]]). «Die jüdischen Führer» oder «die Judäer» wären Deutungsentscheidungen je nach Stelle; sie sind in den "
  "decisions als Alternativen genannt. Jesus, seine Jünger, Marta, Maria und Lazarus sind selbst Juden."),
 ("[[JHN.10.29]]: Der SBLGNT liest ὃ … μείζων, eine grammatisch harte Verbindung; die Übersetzung hält sie fest, die "
  "glatteren Lesarten stehen als Alternativen."),
 ("[[JHN.11.25]]: In 𝔓45 fehlt nach der CNTR-Transkription «und das Leben» (καὶ ἡ ζωή); die Transkriptionen von 01, 02, 03, "
  "04, 05, 032, 𝔓66 und 𝔓75 haben die Worte. Der SBLGNT-Apparat verzeichnet an dieser Stelle keine Variante, deshalb gibt es "
  "dazu keine Lesart-Alternative; die Angabe stützt sich auf die Transkriptionen selbst."),
 ("Johannes erzählt oft im Präsens («er sagt», «sie sagen»); das ist beibehalten. ὅτι vor direkter Rede ist nicht eigens "
  "übersetzt. Für ἀγαπάω steht «lieben», für φιλέω «lieb haben» ([[JHN.11.3]], [[JHN.11.5]], [[JHN.11.36]]); für ἔθνος "
  "«Nation», für λαός «Volk» ([[JHN.11.48]]–[[JHN.11.52]])."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("D Grundentscheid zu de johanneische Schlüsselwört sind i scripts/authoring/johannes_text_01_03.py begründet. "
  "Mundart: «Amen, amen, ich säge eu», «de Vatter», «de Jesus»; οἱ Ἰουδαῖοι wörtlich «d Jude»."),
 ("[[JHN.11.25]]: I 𝔓45 fäält nach de CNTR-Transkription «und s Läbe»; im SBLGNT-Apparat staat da kei Variante."),
 ("Für ἀγαπάω staat «gern haa», für φιλέω «lieb haa»; für κλαίω «briegge», für δακρύω «d Träne chömed» ([[JHN.11.35]])."),
]


def run():
    import json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _lib import localize  # noqa: E402
    n = 0
    if not (D / "works" / f"WORK-{BOOK}.json").exists():
        raise SystemExit(f"WORK-{BOOK} fehlt")
    for uid, rng, kind, title, parts, summary, seg in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": f"WORK-{BOOK}", "range": rng, "kind": kind,
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
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-{BOOK}-{c:03d}.json")
        refs_c = [f"{BOOK}.{c}.{v}" for v in range(1, last + 1) if f"{BOOK}.{c}.{v}" in toks]
        if len(refs_c) != last or len(toks) != last:
            raise SystemExit(f"Kapitel {c}: Versbestand weicht ab ({len(refs_c)} von {last}, Tokens für {len(toks)} Verse)")
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-{BOOK}-{c:03d}-001-{last:03d}-{code}-WORKING"
            dec = [{"reference": r, "target": tg, "kind": kd, "grc": grc, **({"more_literal": ml} if ml else {}),
                    **({"other_options": oo} if oo else {}), **({"note": nt} if nt else {})}
                   for r, tg, kd, grc, ml, oo, nt in decs if r in refs_c]
            for d in dec:
                if d["target"] not in texts[d["reference"]]:
                    raise SystemExit(f"{tid}: Entscheidung {d['target']!r} nicht im Text {d['reference']}")
            alts = []
            for a in ALTS:
                vid, ref, f_de, t_de, f_g, t_g, eff, n_de, n_g, w_de, w_g, o_de, o_g = a[:13]
                related = a[13] if len(a) > 13 else None
                if ref not in refs_c:
                    continue
                if vid.split(":")[0] not in variants:
                    raise SystemExit(f"{tid}: Variante {vid} nicht im Apparat")
                f_, t_, nt, ws, og = (f_de, t_de, n_de, w_de, o_de) if lang == "de" else (f_g, t_g, n_g, w_g, o_g)
                if f_ not in texts[ref]:
                    raise SystemExit(f"{tid}: Alternative {f_!r} nicht im Text {ref}")
                alt = {"reading": vid, "reference": ref, "from_text": f_, "to_text": t_, "effect": eff, "note": nt,
                       "readings": {k: [{"grc": g, "text": x, **({"note": h} if h else {})} for g, x, h in v] for k, v in ws.items()},
                       "origin": og}
                if related:
                    for rv in related:
                        if rv not in variants:
                            raise SystemExit(f"{tid}: verwandte Variante {rv} nicht im Apparat")
                    alt["related_variants"] = related
                alts.append(alt)
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"{BOOK}.{c}.1-{BOOK}.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Schaaf, Tüür), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-{BOOK}-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; historisches Präsens beibehalten; johanneische Schlüsselwörter einheitlich nach den Grundentscheiden in scripts/authoring/johannes_text_01_03.py. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
            aid = f"ALIGN-{BOOK}-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"{BOOK}.{c}.1-{BOOK}.{c}.{last}",
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": f"« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt ({SCRIPT}).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 10–11 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
