#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 14–17 (Abschiedsreden und Gebet Jesu) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch,
Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_14_17.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben.

Die Grundentscheide zur Wiedergabe der johanneischen Schlüsselwörter (λόγος, ἐγώ εἰμι, δόξα/δοξάζω, σημεῖον, μένω,
ἀμὴν ἀμήν, κόσμος, οἱ Ἰουδαῖοι, παράκλητος, ὑψόω, ἄνωθεν) stehen in scripts/authoring/johannes_text_01_03.py; diese
Datei wendet sie an und begründet nur, was in Kapitel 14–17 neu hinzukommt.

Besonderheiten:
- In Kapitel 14–17 fehlt im SBLGNT kein Vers; alle Verse haben Tokens.
- Die Rede Jesu von [[JHN.15.1]] bis [[JHN.16.16]] schliesst ohne neue Redeeinleitung an [[JHN.14.31]] an und steht
  ohne Anführungszeichen, ebenso [[JHN.14.1]]–[[JHN.14.4]] als Fortsetzung der in Kapitel 13 begonnenen Rede.

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
CHAPTERS = ((14, 31), (15, 27), (16, 33), (17, 26))

DE = {
 # ------------------------------------------------------------ Kapitel 14
 "JHN.14.1": "[Euer]{3} [Herz]{4,5} [sei]{2} [nicht]{1} [erschüttert]{2}. [Glaubt]{6} [an]{7} [Gott]{8,9}, und{10} [glaubt]{13} [an]{11} [mich]{12}!",
 "JHN.14.2": "[Im]{1,2} [Haus]{3} [meines]{6} [Vaters]{4,5} [gibt es]{9} [viele]{8} [Wohnungen]{7}. [Wenn]{10} [es aber]{11} [nicht]{12} so wäre, [hätte]{14} [ich]{13} [euch]{15} dann [gesagt]{13}, [dass]{16} [ich hingehe]{17}, [um]{18} [euch]{20} [einen Ort]{19} [zu bereiten]{18}?",
 "JHN.14.3": "Und{1} [wenn]{2} [ich hingegangen bin]{3} und{4} [euch]{7} [einen Ort]{6} [bereitet habe]{5}, [komme ich]{9} [wieder]{8} und{10} [werde]{11} [euch]{12} [zu]{13} [mir]{14} [nehmen]{11}, [damit]{15} [auch]{19} [ihr]{20} [dort seid]{21}, [wo]{16} [ich]{18} [bin]{17}.",
 "JHN.14.4": "Und{1} [wohin]{2} [ich]{3} [gehe]{4}, [dahin kennt ihr]{5} [den]{6} [Weg]{7}.",
 "JHN.14.5": "[Thomas]{3} [sagt]{1} [zu ihm]{2}: «[Herr]{4}, [wir wissen]{6} [nicht]{5}, [wohin]{7} [du gehst]{8}. [Wie]{9} [können wir]{10} [den]{11} [Weg]{12} [kennen]{13}?»",
 "JHN.14.6": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: «[Ich]{5} [bin]{6} [der]{7} [Weg]{8} und{9} [die]{10} [Wahrheit]{11} und{12} [das]{13} [Leben]{14}. [Niemand]{15} [kommt]{16} [zum]{17,18} [Vater]{19} [ausser]{20,21} [durch]{22} [mich]{23}.",
 "JHN.14.7": "[Wenn]{1} [ihr]{2} [mich]{3} [erkannt hättet]{2}, [würdet ihr]{8} [auch]{4} [meinen]{7} [Vater]{5,6} [kennen]{9}. [Von]{10} [jetzt an]{11} [kennt ihr]{12} [ihn]{13} und{14} [habt]{15} [ihn]{16} [gesehen]{15}.»",
 "JHN.14.8": "[Philippus]{3} [sagt]{1} [zu ihm]{2}: «[Herr]{4}, [zeig]{5} [uns]{6} [den]{7} [Vater]{8}, und{9} [das genügt]{10} [uns]{11}.»",
 "JHN.14.9": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: «[So lange]{5} [Zeit]{6} [bin ich]{9} [bei]{7} [euch]{8}, und{10} [du hast]{12} [mich]{13} [nicht]{11} [erkannt]{12}, [Philippus]{14}? [Wer]{15} [mich]{17} [gesehen hat]{16}, [hat]{18} [den]{19} [Vater]{20} [gesehen]{18}. [Wie]{21} [sagst]{23} [du]{22} dann: ‹[Zeig]{24} [uns]{25} [den]{26} [Vater]{27}›?",
 "JHN.14.10": "[Glaubst du]{2} [nicht]{1}, [dass]{3} [ich]{4} [im]{5,6} [Vater]{7} [bin]{13} und{8} [der]{9} [Vater]{10} [in]{11} [mir]{12} [ist]{13}? [Die]{14} [Worte]{15}, [die]{16} [ich]{17} [euch]{19} [sage]{18}, [rede ich]{23} [nicht]{22} [von]{20} [mir selbst]{21} aus; [der Vater]{24,26} [aber]{25}, [der]{29} [in]{27} [mir]{28} [bleibt]{29}, [tut]{30} [seine]{33} [Werke]{31,32}.",
 "JHN.14.11": "[Glaubt]{1} [mir]{2}, [dass]{3} [ich]{4} [im]{5,6} [Vater]{7} bin und{8} [der]{9} [Vater]{10} [in]{11} [mir]{12} ist; [wenn]{13} [aber]{14} [nicht]{15}, [dann glaubt]{20} [um]{16} [der]{17} [Werke]{18} [selbst]{19} [willen]{16}.",
 "JHN.14.12": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Wer]{5} [an]{7} [mich]{8} [glaubt]{6}, [der]{14} [wird]{15} [die]{9} [Werke]{10}, [die]{11} [ich]{12} [tue]{13}, [auch]{14} [tun]{15}, und{16} [er wird]{19} [grössere]{17} [als diese]{18} [tun]{19}, [weil]{20} [ich]{21} [zum]{22,23} [Vater]{24} [gehe]{25}.",
 "JHN.14.13": "Und{1} [was]{2,3} [immer]{4} [ihr]{5} [in]{6} [meinem]{9} [Namen]{7,8} [erbittet]{5}, [das]{10} [werde ich tun]{11}, [damit]{12} [der]{14} [Vater]{15} [im]{16,17} [Sohn]{18} [verherrlicht wird]{13}.",
 "JHN.14.14": "[Wenn]{1} [ihr]{3} [mich]{4} [um etwas]{2} [bittet]{3} [in]{5} [meinem]{8} [Namen]{6,7}, [werde]{10} [ich]{9} [es tun]{10}.",
 "JHN.14.15": "[Wenn]{1} [ihr]{2} [mich]{3} [liebt]{2}, [werdet ihr]{8} [meine]{6,7} [Gebote]{4,5} [halten]{8}.",
 "JHN.14.16": "[Und ich]{1} [werde]{2} [den]{3} [Vater]{4} [bitten]{2}, und{5} [er wird]{8} [euch]{9} [einen anderen]{6} [Beistand]{7} [geben]{8}, [damit]{10} [er]{11} [bei]{12} [euch]{13} [sei]{11} [in]{14} [Ewigkeit]{15,16}:",
 "JHN.14.17": "[den Geist]{1,2} [der]{3} [Wahrheit]{4}, [den]{5} [die]{6} [Welt]{7} [nicht]{8} [empfangen]{10} [kann]{9}, [weil]{11} [sie]{13} [ihn]{14} [nicht]{12} [sieht]{13} [und auch nicht]{15} [kennt]{16}. [Ihr]{17} [kennt]{18} [ihn]{19}, [weil]{20} [er]{23} [bei]{21} [euch]{22} [bleibt]{23} und{24} [in]{25} [euch]{26} [sein wird]{27}.",
 "JHN.14.18": "[Ich werde]{2} [euch]{3} [nicht]{1} [als Waisen]{4} [zurücklassen]{2}; [ich komme]{5} [zu]{6} [euch]{7}.",
 "JHN.14.19": "[Noch]{1} [eine kleine Weile]{2}, und{3} [die]{4} [Welt]{5} [sieht]{8} [mich]{6} [nicht mehr]{7}; [ihr]{9} [aber]{10} [seht]{11} [mich]{12}, [weil]{13} [ich]{14} [lebe]{15} und{16} [auch ihr]{17} [leben werdet]{18}.",
 "JHN.14.20": "[An]{1} [jenem]{2} [Tag]{3,4} [werdet]{5} [ihr]{6} [erkennen]{5}, [dass]{7} [ich]{8} [in]{9} [meinem]{12} [Vater]{10,11} bin und{13} [ihr]{14} [in]{15} [mir]{16} [und ich]{17} [in]{18} [euch]{19}.",
 "JHN.14.21": "[Wer]{1} [meine]{5} [Gebote]{3,4} [hat]{2} und{6} [sie]{8} [hält]{7}, [der]{9} [ist]{10} [es, der]{11} [mich]{13} [liebt]{12}. [Wer]{14} [mich]{17} [aber]{15} [liebt]{16}, [wird]{18} [von]{19} [meinem]{22} [Vater]{20,21} [geliebt werden]{18}, [und ich]{23} [werde]{24} [ihn]{25} [lieben]{24} und{26} [mich]{29} [ihm]{28} [offenbaren]{27}.»",
 "JHN.14.22": "[Judas]{3} – [nicht]{4} [der]{5} [Iskariot]{6} – [sagt]{1} [zu ihm]{2}: «[Herr]{7}, [was]{8} [ist geschehen]{9}, [dass]{10} [du]{12} [dich]{14} [uns]{11} [offenbaren]{13} [wirst]{12} und{15} [nicht]{16} [der]{17} [Welt]{18}?»",
 "JHN.14.23": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihm]{5}: «[Wenn]{6} [jemand]{7} [mich]{9} [liebt]{8}, [wird er]{13} [mein]{12} [Wort]{10,11} [halten]{13}, und{14} [mein]{17} [Vater]{15,16} [wird]{18} [ihn]{19} [lieben]{18}, und{20} [wir werden]{23} [zu]{21} [ihm]{22} [kommen]{23} und{24} [bei]{26} [ihm]{27} [Wohnung]{25} [nehmen]{28}.",
 "JHN.14.24": "[Wer]{1} [mich]{4} [nicht]{2} [liebt]{3}, [hält]{9} [meine]{7} [Worte]{5,6} [nicht]{8}. Und{10} [das]{11} [Wort]{12}, [das]{13} [ihr hört]{14}, [ist]{16} [nicht]{15} [meines]{17}, [sondern]{18} [das des]{19} [Vaters]{22}, [der]{20} [mich]{21} [gesandt hat]{20}.",
 "JHN.14.25": "[Das]{1} [habe ich]{2} [zu euch]{3} [gesagt]{2}, [während ich]{6} [bei]{4} [euch]{5} [bleibe]{6}.",
 "JHN.14.26": "[Der]{1} [Beistand]{3} [aber]{2}, [der]{4} [heilige]{6,7} [Geist]{5}, [den]{8} [der]{10} [Vater]{11} [in]{12} [meinem]{15} [Namen]{13,14} [senden wird]{9}, [der]{16} [wird]{18} [euch]{17} [alles]{19} [lehren]{18} und{20} [euch]{22} [an]{21} [alles]{23} [erinnern]{21}, [was]{24} [ich]{25} [euch]{26} [gesagt habe]{25}.",
 "JHN.14.27": "[Frieden]{1} [hinterlasse ich]{2} [euch]{3}, [meinen]{5,6} [Frieden]{4} [gebe ich]{7} [euch]{8}. [Nicht]{9} [wie]{10} [die]{11} [Welt]{12} [gibt]{13}, [gebe]{15} [ich]{14} [euch]{16}. [Euer]{19} [Herz]{20,21} [sei]{18} [nicht]{17} [erschüttert]{18} [und verzage nicht]{22,23}.",
 "JHN.14.28": "[Ihr habt gehört]{1}, [dass]{2} [ich]{3} [euch]{5} [gesagt habe]{4}: ‹[Ich gehe]{6} und{7} [komme]{8} [zu]{9} [euch]{10}.› [Wenn]{11} [ihr]{12} [mich]{13} [lieben würdet]{12}, [würdet ihr]{15} [euch freuen]{14}, [dass]{16} [ich]{17} [zum]{18,19} [Vater]{20} [gehe]{17}, [denn]{21} [der]{22} [Vater]{23} [ist]{26} [grösser]{24} [als ich]{25}.",
 "JHN.14.29": "Und{1} [jetzt]{2} [habe ich es]{3} [euch]{4} [gesagt]{3}, [bevor]{5} [es geschieht]{6}, [damit]{7} [ihr]{10}, [wenn]{8} [es geschieht]{9}, [glaubt]{10}.",
 "JHN.14.30": "[Ich werde]{3} [nicht mehr]{1} [viel]{2} [mit]{4} [euch]{5} [reden]{3}, [denn]{7} [der]{8} [Herrscher]{11} [der]{9} [Welt]{10} [kommt]{6}. Und{12} [an]{13} [mir]{14} [hat er]{16} [nichts]{15,17};",
 "JHN.14.31": "[aber]{1} [die]{4} [Welt]{5} [soll]{2} [erkennen]{3}, [dass]{6} [ich]{7} [den]{8} [Vater]{9} [liebe]{7} und{10} [so]{16} [handle]{17}, [wie]{11} [der]{14} [Vater]{15} [mir]{13} [geboten hat]{12}. [Steht auf]{18}, [lasst uns]{19} [von hier]{20} [gehen]{19}!»",
 # ------------------------------------------------------------ Kapitel 15
 "JHN.15.1": "[Ich]{1} [bin]{2} [der]{3,5} [wahre]{6} [Weinstock]{4}, und{7} [mein]{10} [Vater]{8,9} [ist]{13} [der]{11} [Weingärtner]{12}.",
 "JHN.15.2": "[Jede]{1} [Rebe]{2} [an]{3} [mir]{4}, [die]{6} [keine]{5} [Frucht]{7} [bringt]{6}, [nimmt er]{8} [weg]{8}, und{10} [jede]{11}, [die]{12} [Frucht]{13} [bringt]{14}, [reinigt er]{15}, [damit]{17} sie [mehr]{19} [Frucht]{18} [bringt]{20}. ~9(αὐτό nimmt «jede Rebe» wieder auf; im Deutschen nicht eigens wiedergegeben) ~16(αὐτό als Objekt von καθαίρει; im Deutschen im Relativsatz mitgemeint)",
 "JHN.15.3": "[Ihr]{2} [seid]{4} [schon]{1} [rein]{3} [durch]{5} [das]{6} [Wort]{7}, [das]{8} [ich]{9} [zu euch]{10} [geredet habe]{9}.",
 "JHN.15.4": "[Bleibt]{1} [in]{2} [mir]{3}, [und ich]{4} [in]{5} [euch]{6}. [Wie]{7} [die]{8} [Rebe]{9} [nicht]{10} [von]{14} [sich aus]{15} [Frucht]{12} [bringen]{13} [kann]{11}, [wenn]{16} [sie]{18} [nicht]{17} [am]{19,20} [Weinstock]{21} [bleibt]{18}, [so]{22} [auch]{23} [ihr]{24} [nicht]{23}, [wenn]{25} [ihr]{29} [nicht]{26} [in]{27} [mir]{28} [bleibt]{29}.",
 "JHN.15.5": "[Ich]{1} [bin]{2} [der]{3} [Weinstock]{4}, [ihr]{5} seid [die]{6} [Reben]{7}. [Wer]{8} [in]{10} [mir]{11} [bleibt]{9} [und ich]{12} [in]{13} [ihm]{14}, [der]{15} [bringt]{16} [viel]{18} [Frucht]{17}; [denn]{19} [ohne]{20} [mich]{21} [könnt ihr]{23} [nichts]{22,25} [tun]{24}.",
 "JHN.15.6": "[Wenn]{1} [jemand]{3} [nicht]{2} [in]{5} [mir]{6} [bleibt]{4}, [wird er]{7} [hinaus]{8}[geworfen]{7} [wie]{9} [die]{10} [Rebe]{11} und{12} [verdorrt]{13}; und{14} [man sammelt]{15} [sie]{16} und{17} [wirft]{21} sie [ins]{18,19} [Feuer]{20}, und{22} [sie verbrennen]{23}.",
 "JHN.15.7": "[Wenn]{1} [ihr]{2} [in]{3} [mir]{4} [bleibt]{2} und{5} [meine]{8} [Worte]{6,7} [in]{9} [euch]{10} [bleiben]{11}, [was]{12} [immer]{13} [ihr wollt]{14}, [darum bittet]{15}, und{16} [es wird]{17} [euch]{18} [geschehen]{17}.",
 "JHN.15.8": "[Darin]{1,2} [wird]{3} [mein]{6} [Vater]{4,5} [verherrlicht]{3}, [dass]{7} [ihr]{10} [viel]{9} [Frucht]{8} [bringt]{10} und{11} [meine]{13} [Jünger]{14} [werdet]{12}.",
 "JHN.15.9": "[Wie]{1} [mich]{3} [der]{4} [Vater]{5} [geliebt hat]{2}, [so habe]{8} [auch ich]{6} [euch]{7} [geliebt]{8}. [Bleibt]{9} [in]{10} [meiner]{13,14} [Liebe]{11,12}!",
 "JHN.15.10": "[Wenn]{1} [ihr]{5} [meine]{4} [Gebote]{2,3} [haltet]{5}, [werdet ihr]{6} [in]{7} [meiner]{10} [Liebe]{8,9} [bleiben]{6}, [wie]{11} [ich]{12} [die]{13} [Gebote]{14} [meines]{17} [Vaters]{15,16} [gehalten habe]{18} und{19} [in]{22} [seiner]{21} [Liebe]{23,24} [bleibe]{20}.",
 "JHN.15.11": "[Das]{1} [habe ich]{2} [zu euch]{3} [gesagt]{2}, [damit]{4} [meine]{7,8} [Freude]{5,6} [in]{9} [euch]{10} [ist]{11} und{12} [eure]{15} [Freude]{13,14} [vollkommen wird]{16}.",
 "JHN.15.12": "[Das]{1} [ist]{2} [mein]{5,6} [Gebot]{3,4}: [dass]{7} [ihr]{8} [einander]{9} [liebt]{8}, [wie]{10} [ich]{11} [euch]{12} [geliebt habe]{11}.",
 "JHN.15.13": "[Grössere]{1} [Liebe]{3} [als diese]{2} [hat]{5} [niemand]{4}: [dass]{6} [einer]{7} [sein]{8,10} [Leben]{9} [hingibt]{11} [für]{12} [seine]{13,15} [Freunde]{14}.",
 "JHN.15.14": "[Ihr]{1} [seid]{4} [meine]{3} [Freunde]{2}, [wenn]{5} [ihr tut]{6}, [was]{7} [ich]{8} [euch]{10} [gebiete]{9}.",
 "JHN.15.15": "[Ich nenne]{2} [euch]{3} [nicht mehr]{1} [Knechte]{4}, [denn]{5} [der]{6} [Knecht]{7} [weiss]{9} [nicht]{8}, [was]{10} [sein]{12} [Herr]{13,14} [tut]{11}. [Euch]{15} [aber]{16} [habe ich]{17} [Freunde]{18} [genannt]{17}, [denn]{19} [alles]{20}, [was]{21} [ich]{22} [von]{23} [meinem]{26} [Vater]{24,25} [gehört habe]{22}, [habe ich]{27} [euch]{28} [kundgetan]{27}.",
 "JHN.15.16": "[Nicht]{1} [ihr]{2} [habt]{4} [mich]{3} [erwählt]{4}, [sondern]{5} [ich]{6} [habe]{7} [euch]{8} [erwählt]{7}, und{9} [ich habe]{10} [euch]{11} [dazu eingesetzt]{10}, [dass]{12} [ihr]{13} [hingeht]{14} und{15} [Frucht]{16} [bringt]{17} und{18} [eure]{21} [Frucht]{19,20} [bleibt]{22}, [damit]{23} [er]{34} [euch]{35} [gibt]{34}, [was]{24,25} [immer]{26} [ihr]{27} [den]{28} [Vater]{29} [in]{30} [meinem]{33} [Namen]{31,32} [bittet]{27}.",
 "JHN.15.17": "[Das]{1} [gebiete ich]{2} [euch]{3}: [dass]{4} [ihr]{5} [einander]{6} [liebt]{5}.",
 "JHN.15.18": "[Wenn]{1} [die]{2} [Welt]{3} [euch]{4} [hasst]{5}, [so wisst]{6}, [dass]{7} [sie]{11} [mich]{8} [vor]{9} [euch]{10} [gehasst hat]{11}.",
 "JHN.15.19": "[Wenn]{1} [ihr]{5} [aus]{2} [der]{3} [Welt]{4} [wärt]{5}, [würde]{8} [die]{6} [Welt]{7} [ihr]{9} [Eigenes]{10} [lieb haben]{11}. [Weil]{12} [ihr]{18} [aber]{13} [nicht]{17} [aus]{14} [der]{15} [Welt]{16} [seid]{18}, [sondern]{19} [ich]{20} [euch]{22} [aus]{23} [der]{24} [Welt]{25} [erwählt habe]{21}, [darum]{26,27} [hasst]{28} [euch]{29} [die]{30} [Welt]{31}.",
 "JHN.15.20": "[Erinnert euch]{1} [an das]{2} [Wort]{3}, [das]{4} [ich]{5} [euch]{7} [gesagt habe]{6}: «[Ein Knecht]{10} [ist]{9} [nicht]{8} [grösser]{11} [als]{12} [sein]{14} [Herr]{13}.» [Wenn]{15} [sie]{17} [mich]{16} [verfolgt haben]{17}, [werden sie]{20} [auch]{18} [euch]{19} [verfolgen]{20}; [wenn]{21} [sie]{25} [mein]{24} [Wort]{22,23} [gehalten haben]{25}, [werden sie]{29} [auch]{26} [das eure]{27,28} [halten]{29}.",
 "JHN.15.21": "[Aber]{1} [das]{2} [alles]{3} [werden sie]{4} [euch]{5,6} [antun]{4} [um]{7} [meines]{10} [Namens]{8,9} [willen]{7}, [weil]{11} [sie]{13} [den]{14} [nicht]{12} [kennen]{13}, [der]{15} [mich]{16} [gesandt hat]{15}.",
 "JHN.15.22": "[Wenn]{1} [ich]{3} [nicht]{2} [gekommen wäre]{3} und{4} [zu ihnen]{6} [geredet hätte]{5}, [hätten sie]{9} [keine]{8} [Sünde]{7}; [jetzt]{10} [aber]{11} [haben sie]{14} [keine]{13} [Ausrede]{12} [für]{15} [ihre]{16,18} [Sünde]{17}.",
 "JHN.15.23": "[Wer]{1} [mich]{2} [hasst]{3}, [hasst]{8} [auch]{4} [meinen]{7} [Vater]{5,6}.",
 "JHN.15.24": "[Wenn]{1} [ich]{5} [nicht]{4} [die]{2} [Werke]{3} [unter]{6} [ihnen]{7} [getan hätte]{5}, [die]{8} [kein]{9} [anderer]{10} [getan hat]{11}, [hätten sie]{14} [keine]{13} [Sünde]{12}; [jetzt]{15} [aber]{16} [haben sie]{18} sie [gesehen]{18} [und]{19} [gehasst]{20} – [sowohl]{21} [mich]{22} [als auch]{23} [meinen]{26} [Vater]{24,25}. ~17(καί vor ἑωράκασιν, «sowohl … als auch», im Deutschen nicht eigens wiedergegeben)",
 "JHN.15.25": "[Aber]{1} das geschieht, [damit]{2} [das]{4} [Wort]{5} [erfüllt wird]{3}, [das]{6} [in]{7} [ihrem]{8,10} [Gesetz]{9} [geschrieben steht]{11}: «[Sie haben]{13} [mich]{14} [ohne Grund]{15} [gehasst]{13}.» ~12(ὅτι leitet das Zitat ein)",
 "JHN.15.26": "[Wenn]{1} [der]{3} [Beistand]{4} [kommt]{2}, [den]{5} [ich]{6} [euch]{8} [vom]{9,10} [Vater]{11} [senden werde]{7}, [der Geist]{12,13} [der]{14} [Wahrheit]{15}, [der]{16} [vom]{17,18} [Vater]{19} [ausgeht]{20}, [der]{21} [wird]{22} [über]{23} [mich]{24} [Zeugnis ablegen]{22}.",
 "JHN.15.27": "[Und]{3} [auch]{1} [ihr]{2} [legt Zeugnis ab]{4}, [weil]{5} [ihr]{10} [von]{6} [Anfang]{7} [an]{6} [bei]{8} [mir]{9} [seid]{10}.",
 # ------------------------------------------------------------ Kapitel 16
 "JHN.16.1": "[Das]{1} [habe ich]{2} [zu euch]{3} [gesagt]{2}, [damit]{4} [ihr]{6} [nicht]{5} [zu Fall kommt]{6}.",
 "JHN.16.2": "[Aus der Synagoge]{1} [werden sie]{2} [euch]{3} [ausschliessen]{2}; [ja]{4}, [es kommt]{5} [die Stunde]{6}, [in der]{7} [jeder]{8}, [der]{9} [euch]{11} [tötet]{10}, [meinen wird]{12}, [Gott]{15,16} [einen heiligen Dienst]{13} [darzubringen]{14}.",
 "JHN.16.3": "Und{1} [das]{2} [werden sie tun]{3}, [weil]{4} [sie]{6} [weder]{5} [den]{7} [Vater]{8} [noch]{9} [mich]{10} [erkannt haben]{6}.",
 "JHN.16.4": "[Aber]{1} [das]{2} [habe ich]{3} [zu euch]{4} [gesagt]{3}, [damit]{5} [ihr]{11}, [wenn]{6} [ihre]{10} [Stunde]{8,9} [kommt]{7}, [euch]{11} [daran]{12} [erinnert]{11}, [dass]{13} [ich]{14} [es euch]{16} [gesagt habe]{15}. [Das]{17} [aber]{18} [habe ich]{23} [euch]{19} [nicht]{22} [von]{20} [Anfang]{21} [an]{20} [gesagt]{23}, [weil]{24} [ich]{27} [bei]{25} [euch]{26} [war]{27}.",
 "JHN.16.5": "[Jetzt]{1} [aber]{2} [gehe ich]{3} [zu]{4} [dem]{5}, [der]{6} [mich]{7} [gesandt hat]{6}, und{8} [keiner]{9} [von]{10} [euch]{11} [fragt]{12} [mich]{13}: «[Wohin]{14} [gehst du]{15}?»",
 "JHN.16.6": "[Sondern]{1} [weil]{2} [ich]{4} [das]{3} [zu euch]{5} [gesagt habe]{4}, [hat]{8} [die]{6} [Trauer]{7} [euer]{9} [Herz]{10,11} [erfüllt]{8}.",
 "JHN.16.7": "[Aber]{1} [ich]{2} [sage]{5} [euch]{6} [die]{3} [Wahrheit]{4}: [Es ist gut]{7} [für euch]{8}, [dass]{9} [ich]{10} [weggehe]{11}. [Denn]{13} [wenn]{12} [ich]{15} [nicht]{14} [weggehe]{15}, [wird]{20} [der]{16} [Beistand]{17} [gewiss nicht]{18,19} [zu]{21} [euch]{22} [kommen]{20}; [wenn]{23} [ich]{25} [aber]{24} [gehe]{25}, [werde ich]{26} [ihn]{27} [zu]{28} [euch]{29} [senden]{26}.",
 "JHN.16.8": "Und{1} [wenn]{2} [jener]{3} [kommt]{2}, [wird er]{4} [die]{5} [Welt]{6} [überführen]{4}: [hinsichtlich]{7} [der Sünde]{8} und{9} [hinsichtlich]{10} [der Gerechtigkeit]{11} und{12} [hinsichtlich]{13} [des Gerichts]{14};",
 "JHN.16.9": "[hinsichtlich]{1} [der Sünde]{2}, [weil]{4} [sie]{6} [nicht]{5} [an]{7} [mich]{8} [glauben]{6}; ~3(μέν … δέ gliedert die Aufzählung; nicht eigens wiedergegeben)",
 "JHN.16.10": "[hinsichtlich]{1} [der Gerechtigkeit]{2}, [weil]{4} [ich]{8} [zum]{5,6} [Vater]{7} [gehe]{8} und{9} [ihr]{11} [mich]{12} [nicht mehr]{10} [seht]{11}; ~3(μέν … δέ gliedert die Aufzählung; nicht eigens wiedergegeben)",
 "JHN.16.11": "[hinsichtlich]{1} [des Gerichts]{3}, [weil]{4} [der]{5} [Herrscher]{6} [dieser]{7,9} [Welt]{8} [gerichtet ist]{10}. ~2(μέν … δέ gliedert die Aufzählung; nicht eigens wiedergegeben)",
 "JHN.16.12": "[Noch]{1} [vieles]{2} [habe ich]{3} [euch]{4} [zu sagen]{5}, [aber]{6} [ihr könnt]{8} es [jetzt]{10} [nicht]{7} [tragen]{9}.",
 "JHN.16.13": "[Wenn]{1} [aber]{2} [jener]{4} [kommt]{3}, [der Geist]{5,6} [der]{7} [Wahrheit]{8}, [wird er]{9} [euch]{10} [in]{11} [der]{12} [ganzen]{14} [Wahrheit]{13} [leiten]{9}; [denn]{16} [er wird]{17} [nicht]{15} [von]{18} [sich aus]{19} [reden]{17}, [sondern]{20} [was]{21} [er hören wird]{22}, [wird er]{23} [reden]{23}, und{24} [das]{25} [Kommende]{26} [wird er]{27} [euch]{28} [verkünden]{27}.",
 "JHN.16.14": "[Er]{1} [wird]{3} [mich]{2} [verherrlichen]{3}, [denn]{4} [er wird]{8} [von]{5} [dem]{6} [Meinen]{7} [nehmen]{8} und{9} es [euch]{11} [verkünden]{10}.",
 "JHN.16.15": "[Alles]{1}, [was]{2} [der]{4} [Vater]{5} [hat]{3}, [ist]{7} [mein]{6}. [Darum]{8,9} [habe ich gesagt]{10}, [dass]{11} [er]{15} [von]{12} [dem]{13} [Meinen]{14} [nimmt]{15} und{16} es [euch]{18} [verkünden wird]{17}.",
 "JHN.16.16": "[Eine kleine Weile]{1}, und{2} [ihr seht]{4} [mich]{5} [nicht mehr]{3}, und{6} [wieder]{7} [eine kleine Weile]{8}, und{9} [ihr werdet]{10} [mich]{11} [sehen]{10}.",
 "JHN.16.17": "[Da]{2} [sagten]{1} [einige von]{3} [seinen]{4,6} [Jüngern]{5} [zueinander]{7,8}: «[Was]{9} [ist]{10} [das]{11}, [was]{12} [er]{13} [zu uns]{14} [sagt]{13}: ‹[Eine kleine Weile]{15}, und{16} [ihr seht]{18} [mich]{19} [nicht]{17}, und{20} [wieder]{21} [eine kleine Weile]{22}, und{23} [ihr werdet]{24} [mich]{25} [sehen]{24}›, und{26}: ‹[Ich gehe]{28} [zum]{29,30} [Vater]{31}›?» ~27(ὅτι leitet das Zitat ein)",
 "JHN.16.18": "[Sie sagten]{1} [nun]{2}: «[Was]{3} [ist]{4} [das]{5}, [was]{6} [er sagt]{7}: ‹[Eine kleine Weile]{8}›? [Wir wissen]{10} [nicht]{9}, [wovon]{11} [er redet]{12}.»",
 "JHN.16.19": "[Jesus]{2} [merkte]{1}, [dass]{3} [sie]{4} [ihn]{5} [fragen]{6} [wollten]{4}, und{7} [sagte]{8} [zu ihnen]{9}: «[Darüber]{10,11} [fragt ihr euch]{12} [untereinander]{13,14}, [dass]{15} [ich gesagt habe]{16}: ‹[Eine kleine Weile]{17}, und{18} [ihr seht]{20} [mich]{21} [nicht]{19}, und{22} [wieder]{23} [eine kleine Weile]{24}, und{25} [ihr werdet]{26} [mich]{27} [sehen]{26}›?",
 "JHN.16.20": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Ihr]{9} [werdet weinen]{6} und{7} [klagen]{8}, [die]{10} [Welt]{12} [aber]{11} [wird sich freuen]{13}. [Ihr]{14} [werdet traurig sein]{15}, [aber]{16} [eure]{19} [Trauer]{17,18} [wird]{22} [zur]{20} [Freude]{21} [werden]{22}. ~5(ὅτι leitet die Rede ein)",
 "JHN.16.21": "[Wenn]{3} [eine]{1} [Frau]{2} [gebiert]{4}, [hat sie]{6} [Schmerz]{5}, [weil]{7} [ihre]{11} [Stunde]{9,10} [gekommen ist]{8}; [wenn]{12} [sie]{14} [aber]{13} [das]{15} [Kind]{16} [geboren hat]{14}, [denkt sie]{18} [nicht mehr]{17} [an die]{19} [Bedrängnis]{20} [vor]{21} [Freude]{22,23}, [dass]{24} [ein Mensch]{26} [in]{27} [die]{28} [Welt]{29} [geboren ist]{25}.",
 "JHN.16.22": "[So]{3} [habt]{7} [auch]{1} [ihr]{2} [jetzt]{4} [Trauer]{6}; [aber]{9} [ich werde]{10} [euch]{11} [wieder]{8} [sehen]{10}, und{12} [euer]{14} [Herz]{15,16} [wird sich freuen]{13}, und{17} [eure]{18,20} [Freude]{19} [nimmt]{22} [niemand]{21} [von]{23} [euch]{24}. ~5(μέν … δέ; nicht eigens wiedergegeben)",
 "JHN.16.23": "Und{1} [an]{2} [jenem]{3} [Tag]{4,5} [werdet ihr]{8} [mich]{6} [nichts]{7,9} [fragen]{8}. [Amen]{10}, [amen]{11}, [ich sage]{12} [euch]{13}: [Wenn]{14} [ihr]{16} [den]{17} [Vater]{18} [um etwas]{15} [bittet]{16}, [wird er]{19} [es euch]{20} [in]{21} [meinem]{24} [Namen]{22,23} [geben]{19}.",
 "JHN.16.24": "[Bis]{1} [jetzt]{2} [habt ihr]{4} [um nichts]{3,5} [gebeten]{4} [in]{6} [meinem]{9} [Namen]{7,8}. [Bittet]{10}, und{11} [ihr werdet empfangen]{12}, [damit]{13} [eure]{16} [Freude]{14,15} [vollkommen]{18} [ist]{17}.",
 "JHN.16.25": "[Das]{1} [habe ich]{4} [in]{2} [Bildworten]{3} [zu euch]{5} [geredet]{4}. [Es kommt]{6} [die Stunde]{7}, [da]{8} [ich]{12} [nicht mehr]{9} [in]{10} [Bildworten]{11} [zu euch]{13} [reden werde]{12}, [sondern]{14} [euch]{20} [offen]{15} [vom]{16,17} [Vater]{18} [berichten werde]{19}.",
 "JHN.16.26": "[An]{1} [jenem]{2} [Tag]{3,4} [werdet ihr]{9} [in]{5} [meinem]{8} [Namen]{6,7} [bitten]{9}, und{10} [ich sage]{12} [euch]{13} [nicht]{11}, [dass]{14} [ich]{15} [den]{17} [Vater]{18} [für]{19} [euch]{20} [bitten werde]{16}.",
 "JHN.16.27": "[Denn]{2} [der]{3} [Vater]{4} [selbst]{1} [hat]{5} [euch]{6} [lieb]{5}, [weil]{7} [ihr]{8} [mich]{9} [lieb gehabt habt]{10} und{11} [geglaubt habt]{12}, [dass]{13} [ich]{14} [von]{15} [Gott]{16,17} [ausgegangen bin]{18}.",
 "JHN.16.28": "[Ich bin]{1} [vom]{2,3} [Vater]{4} [ausgegangen]{1} und{5} [bin]{6} [in]{7} [die]{8} [Welt]{9} [gekommen]{6}; [wieder]{10} [verlasse ich]{11} [die]{12} [Welt]{13} und{14} [gehe]{15} [zum]{16,17} [Vater]{18}.»",
 "JHN.16.29": "[Seine]{2,4} [Jünger]{3} [sagen]{1}: «[Sieh]{5}, [jetzt]{6} [redest du]{9} [offen]{7,8} und{10} [sagst]{13} [kein]{12} [Bildwort]{11}.",
 "JHN.16.30": "[Jetzt]{1} [wissen wir]{2}, [dass]{3} [du]{4} [alles]{5} [weisst]{4} und{6} es [nicht]{7} [nötig]{8} [hast]{9}, [dass]{10} [dich]{12} [jemand]{11} [fragt]{13}. [Darum]{14,15} [glauben wir]{16}, [dass]{17} [du]{20} [von]{18} [Gott]{19} [ausgegangen bist]{20}.»",
 "JHN.16.31": "[Jesus]{3} [antwortete]{1} [ihnen]{2}: «[Jetzt]{4} [glaubt ihr]{5}?",
 "JHN.16.32": "[Siehe]{1}, [es kommt]{2} [die Stunde]{3}, und{4} [sie ist gekommen]{5}, [dass]{6} [ihr zerstreut werdet]{7}, [jeder]{8} [zu]{9} [dem Seinen]{10,11}, [und mich]{12} [allein]{13} [lasst]{14}. Und{15} [ich bin]{17} [nicht]{16} [allein]{18}, [denn]{19} [der]{20} [Vater]{21} [ist]{24} [bei]{22} [mir]{23}.",
 "JHN.16.33": "[Das]{1} [habe ich]{2} [zu euch]{3} [gesagt]{2}, [damit]{4} [ihr]{8} [in]{5} [mir]{6} [Frieden]{7} [habt]{8}. [In]{9} [der]{10} [Welt]{11} [habt ihr]{13} [Bedrängnis]{12}; [aber]{14} [seid getrost]{15}: [Ich]{16} [habe]{17} [die]{18} [Welt]{19} [überwunden]{17}.»",
 # ------------------------------------------------------------ Kapitel 17
 "JHN.17.1": "[Das]{1} [redete]{2} [Jesus]{3}, und{4} [er erhob]{5} [seine]{6,8} [Augen]{7} [zum]{9,10} [Himmel]{11} und [sprach]{12}: «[Vater]{13}, [die]{15} [Stunde]{16} [ist gekommen]{14}. [Verherrliche]{17} [deinen]{18,19} [Sohn]{20}, [damit]{21} [der]{22} [Sohn]{23} [dich]{25} [verherrlicht]{24},",
 "JHN.17.2": "[wie]{1} [du]{2} [ihm]{3} [Vollmacht]{4} [über alles]{5} [Fleisch]{6} [gegeben hast]{2}, [damit]{7} [er]{12} [allen]{8}, [die]{9} [du]{10} [ihm]{11} [gegeben hast]{10}, [ewiges]{15} [Leben]{14} [gibt]{12}. ~13(αὐτοῖς «ihnen» nimmt πᾶν ὅ «alles, was» als Personen wieder auf; im Deutschen in «allen, die» enthalten)",
 "JHN.17.3": "[Das]{1} [aber]{2} [ist]{3} [das]{4} [ewige]{5} [Leben]{6}: [dass]{7} [sie]{8} [dich]{9}, [den]{10} [einzigen]{11} [wahren]{12} [Gott]{13}, [erkennen]{8} und{14} [den, den]{15} [du gesandt hast]{16}, [Jesus]{17} [Christus]{18}.",
 "JHN.17.4": "[Ich]{1} [habe]{3} [dich]{2} [auf]{4} [der]{5} [Erde]{6} [verherrlicht]{3}, [indem ich]{9} [das]{7} [Werk]{8} [vollendet habe]{9}, [das]{10} [du]{11} [mir]{12} [gegeben hast]{11}, [damit]{13} [ich es tue]{14}.",
 "JHN.17.5": "Und{1} [jetzt]{2} [verherrliche]{3} [du]{5} [mich]{4}, [Vater]{6}, [bei]{7} [dir]{8} [mit der]{9} [Herrlichkeit]{10}, [die]{11} [ich]{12} [bei]{18} [dir]{19} [hatte]{12}, [bevor]{13,14} [die]{15} [Welt]{16} [war]{17}.",
 "JHN.17.6": "[Ich habe]{1} [deinen]{2,3} [Namen]{4} [den]{5} [Menschen]{6} [offenbart]{1}, [die]{7} [du]{8} [mir]{9} [aus]{10} [der]{11} [Welt]{12} [gegeben hast]{8}. [Dein]{13} [waren sie]{14}, [und mir]{15} [hast du]{17} [sie]{16} [gegeben]{17}, und{18} [sie haben]{22} [dein]{21} [Wort]{19,20} [gehalten]{22}.",
 "JHN.17.7": "[Jetzt]{1} [haben sie erkannt]{2}, [dass]{3} [alles]{4}, [was]{5} [du]{6} [mir]{7} [gegeben hast]{6}, [von]{8} [dir]{9} [stammt]{10}.",
 "JHN.17.8": "[Denn]{1} [die]{2} [Worte]{3}, [die]{4} [du]{5} [mir]{6} [gegeben hast]{5}, [habe ich]{7} [ihnen]{8} [gegeben]{7}, und{9} [sie]{10} [haben sie angenommen]{11} und{12} [wahrhaftig]{14} [erkannt]{13}, [dass]{15} [ich]{18} [von]{16} [dir]{17} [ausgegangen bin]{18}, und{19} [sie haben geglaubt]{20}, [dass]{21} [du]{22} [mich]{23} [gesandt hast]{24}.",
 "JHN.17.9": "[Ich]{1} [bitte]{4} [für]{2} [sie]{3}; [nicht]{5} [für]{6} [die]{7} [Welt]{8} [bitte ich]{9}, [sondern]{10} [für]{11} [die, die]{12} [du]{13} [mir]{14} [gegeben hast]{13}, [denn]{15} [sie sind]{17} [dein]{16},",
 "JHN.17.10": "und{1} [alles]{4} [Meine]{2,3} [ist]{6} [dein]{5}, und{7} [das]{8} [Deine]{9} [ist mein]{10}, und{11} [ich bin]{12} [in]{13} [ihnen]{14} [verherrlicht]{12}.",
 "JHN.17.11": "Und{1} [ich bin]{3} [nicht mehr]{2} [in]{4} [der]{5} [Welt]{6}, und{7} [sie]{8} [sind]{12} [in]{9} [der]{10} [Welt]{11}, [und ich]{13} [komme]{16} [zu]{14} [dir]{15}. [Heiliger]{18} [Vater]{17}, [bewahre]{19} [sie]{20} [in]{21} [deinem]{22,24} [Namen]{23}, [den]{25} [du]{26} [mir]{27} [gegeben hast]{26}, [damit]{28} [sie]{29} [eins]{30} [sind]{29}, [wie]{31} [wir]{32}.",
 "JHN.17.12": "[Als]{1} [ich]{2} [bei]{3} [ihnen]{4} [war]{2}, [bewahrte]{6} [ich]{5} [sie]{7} [in]{8} [deinem]{9,11} [Namen]{10}, [den]{12} [du]{13} [mir]{14} [gegeben hast]{13}, und{15} [ich habe sie behütet]{16}, und{17} [keiner]{18} [von]{19} [ihnen]{20} [ist verloren gegangen]{21} [ausser]{22,23} [dem]{24} [Sohn]{25} [des]{26} [Verderbens]{27}, [damit]{28} [die]{29} [Schrift]{30} [erfüllt wird]{31}.",
 "JHN.17.13": "[Jetzt]{1} [aber]{2} [komme ich]{5} [zu]{3} [dir]{4}, und{6} [das]{7} [rede ich]{8} [in]{9} [der]{10} [Welt]{11}, [damit]{12} [sie]{13} [meine]{16,17} [Freude]{14,15} [vollkommen]{18} [in]{19} [sich]{20} [haben]{13}.",
 "JHN.17.14": "[Ich]{1} [habe]{2} [ihnen]{3} [dein]{4,6} [Wort]{5} [gegeben]{2}, und{7} [die]{8} [Welt]{9} [hat]{10} [sie]{11} [gehasst]{10}, [weil]{12} [sie]{14} [nicht]{13} [aus]{15} [der]{16} [Welt]{17} [sind]{14}, [wie]{18} [ich]{19} [nicht]{20} [aus]{22} [der]{23} [Welt]{24} [bin]{21}.",
 "JHN.17.15": "[Ich bitte]{2} [nicht]{1}, [dass]{3} [du]{4} [sie]{5} [aus]{6} [der]{7} [Welt]{8} [wegnimmst]{4}, [sondern]{9} [dass]{10} [du]{11} [sie]{12} [vor]{13} [dem]{14} [Bösen]{15} [bewahrst]{11}.",
 "JHN.17.16": "[Sie sind]{5} [nicht]{4} [aus]{1} [der]{2} [Welt]{3}, [wie]{6} [ich]{7} [nicht]{8} [aus]{10} [der]{11} [Welt]{12} [bin]{9}.",
 "JHN.17.17": "[Heilige]{1} [sie]{2} [in]{3} [der]{4} [Wahrheit]{5}; [dein]{8,9} [Wort]{6,7} [ist]{11} [Wahrheit]{10}.",
 "JHN.17.18": "[Wie]{1} [du]{3} [mich]{2} [in]{4} [die]{5} [Welt]{6} [gesandt hast]{3}, [so habe]{8} [auch ich]{7} [sie]{9} [in]{10} [die]{11} [Welt]{12} [gesandt]{8}.",
 "JHN.17.19": "Und{1} [für]{2} [sie]{3} [heilige]{5} [ich]{4} [mich selbst]{6}, [damit]{7} [auch]{9} [sie]{10} [in]{12} [Wahrheit]{13} [geheiligt]{11} [sind]{8}.",
 "JHN.17.20": "[Ich bitte]{5} [aber]{4} [nicht]{1} [nur]{6} [für]{2} [diese]{3}, [sondern]{7} [auch]{8} [für]{9} [die, die]{10} [durch]{12} [ihr]{13,15} [Wort]{14} [an]{16} [mich]{17} [glauben]{11},",
 "JHN.17.21": "[damit]{1} [alle]{2} [eins]{3} [sind]{4}, [wie]{5} [du]{6}, [Vater]{7}, [in]{8} [mir]{9} bist [und ich]{10} [in]{11} [dir]{12}, [damit]{13} [auch]{14} [sie]{15} [in]{16} [uns]{17} [sind]{18}, [damit]{19} [die]{20} [Welt]{21} [glaubt]{22}, [dass]{23} [du]{24} [mich]{25} [gesandt hast]{26}.",
 "JHN.17.22": "[Und ich]{1} [habe]{7} [ihnen]{8} [die]{2} [Herrlichkeit]{3} [gegeben]{7}, [die]{4} [du]{5} [mir]{6} [gegeben hast]{5}, [damit]{9} [sie]{10} [eins]{11} [sind]{10}, [wie]{12} [wir]{13} [eins]{14} sind,",
 "JHN.17.23": "[ich]{1} [in]{2} [ihnen]{3} und{4} [du]{5} [in]{6} [mir]{7}, [damit]{8} [sie]{9} [vollendet]{10} [sind]{9} [zur]{11} [Einheit]{12}, [damit]{13} [die]{15} [Welt]{16} [erkennt]{14}, [dass]{17} [du]{18} [mich]{19} [gesandt hast]{20} und{21} [sie]{23} [geliebt hast]{22}, [wie]{24} [du]{26} [mich]{25} [geliebt hast]{26}.",
 "JHN.17.24": "[Vater]{1}, [was]{2} [du]{3} [mir]{4} [gegeben hast]{3} – [ich will]{5}, [dass]{6} [auch jene]{10} [bei]{12} [mir]{13} [sind]{11}, [wo]{7} [ich]{9} [bin]{8}, [damit]{14} [sie]{15} [meine]{18,19} [Herrlichkeit]{16,17} [sehen]{15}, [die]{20} [du]{21} [mir]{22} [gegeben hast]{21}, [weil]{23} [du]{24} [mich]{25} [geliebt hast]{24} [vor]{26} [der Grundlegung]{27} [der Welt]{28}.",
 "JHN.17.25": "[Gerechter]{2} [Vater]{1}, [die]{4} [Welt]{5} [hat]{8} [dich]{6} [zwar]{3} [nicht]{7} [erkannt]{8}, [ich]{9} [aber]{10} [habe]{12} [dich]{11} [erkannt]{12}, und{13} [diese]{14} [haben erkannt]{15}, [dass]{16} [du]{17} [mich]{18} [gesandt hast]{19},",
 "JHN.17.26": "und{1} [ich habe]{2} [ihnen]{3} [deinen]{4,6} [Namen]{5} [bekannt gemacht]{2} und{7} [werde ihn bekannt machen]{8}, [damit]{9} [die]{10} [Liebe]{11}, [mit der]{12} [du]{13} [mich]{14} [geliebt hast]{13}, [in]{15} [ihnen]{16} [ist]{17} [und ich]{18} [in]{19} [ihnen]{20}.»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 14
 "JHN.14.1": "[Eues]{3} [Härz]{4,5} [söll]{2} [nöd]{1} [erschüttert sii]{2}. [Glaubed]{6} [a]{7} [Gott]{8,9}, und{10} [glaubed]{13} [a]{11} [mich]{12}!",
 "JHN.14.2": "[Im]{1,2} [Huus]{3} [vo mim]{6} [Vatter]{4,5} [hät s]{9} [vil]{8} [Wonige]{7}. [Wänn]{10} [s aber]{11} [nöd]{12} so wär, [hett]{14} [ich]{13} [eu]{15} dänn [gseit]{13}, [dass]{16} [ich gang]{17}, [zum]{18} [eu]{20} [en Platz]{19} [parat mache]{18}?",
 "JHN.14.3": "Und{1} [wänn]{2} [ich gange bin]{3} und{4} [eu]{7} [en Platz]{6} [parat gmacht han]{5}, [chumm ich]{9} [wider]{8} und{10} [nime]{11} [eu]{12} [zu]{13} [mir]{14}, [demit]{15} [au]{19} [ir]{20} [dört sind]{21}, [wo]{16} [ich]{18} [bin]{17}.",
 "JHN.14.4": "Und{1} [wo]{2} [ich]{3} [hiigang]{4}, [de]{6} [Wäg]{7} dörthii [kännt ir]{5}.",
 "JHN.14.5": "[De Thomas]{3} [seit]{1} [zu ihm]{2}: «[Herr]{4}, [mir wüssed]{6} [nöd]{5}, [wo]{7} [du hiigaasch]{8}. [Wie]{9} [chönd mir]{10} [de]{11} [Wäg]{12} [kenne]{13}?»",
 "JHN.14.6": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: «[Ich]{5} [bin]{6} [de]{7} [Wäg]{8} und{9} [d]{10} [Wahrheit]{11} und{12} [s]{13} [Läbe]{14}. [Niemer]{15} [chunnt]{16} [zum]{17,18} [Vatter]{19} [usser]{20,21} [dur]{22} [mich]{23}.",
 "JHN.14.7": "[Wänn]{1} [ir]{2} [mich]{3} [erchännt hetted]{2}, [würded ir]{8} [au]{4} [min]{7} [Vatter]{5,6} [kenne]{9}. [Vo]{10} [jetzt aa]{11} [kännt ir]{12} [en]{13} und{14} [händ]{15} [en]{16} [gseh]{15}.»",
 "JHN.14.8": "[De Philippus]{3} [seit]{1} [zu ihm]{2}: «[Herr]{4}, [zeig]{5} [üs]{6} [de]{7} [Vatter]{8}, und{9} [das längt]{10} [üs]{11}.»",
 "JHN.14.9": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: «[So lang]{5} [Ziit]{6} [bin ich]{9} [bi]{7} [eu]{8}, und{10} [du häsch]{12} [mich]{13} [nöd]{11} [erchännt]{12}, [Philippus]{14}? [Wär]{15} [mich]{17} [gseh hät]{16}, [hät]{18} [de]{19} [Vatter]{20} [gseh]{18}. [Wie]{21} [seisch]{23} [du]{22} dänn: ‹[Zeig]{24} [üs]{25} [de]{26} [Vatter]{27}›?",
 "JHN.14.10": "[Glaubsch]{2} [nöd]{1}, [dass]{3} [ich]{4} [im]{5,6} [Vatter]{7} [bin]{13} und{8} [de]{9} [Vatter]{10} [in]{11} [mir]{12} [isch]{13}? [D]{14} [Wort]{15}, [wo]{16} [ich]{17} [eu]{19} [säge]{18}, [red ich]{23} [nöd]{22} [vo]{20} [mir uus]{21}; [de Vatter]{24,26} [aber]{25}, [wo]{29} [in]{27} [mir]{28} [bliibt]{29}, [tuet]{30} [sini]{33} [Wärch]{31,32}.",
 "JHN.14.11": "[Glaubed]{1} [mir]{2}, [dass]{3} [ich]{4} [im]{5,6} [Vatter]{7} bin und{8} [de]{9} [Vatter]{10} [in]{11} [mir]{12} isch; [wänn]{13} [aber]{14} [nöd]{15}, [dänn glaubed]{20} [wäge]{16} [de]{17} [Wärch]{18} [sälber]{19}.",
 "JHN.14.12": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Wär]{5} [a]{7} [mich]{8} [glaubt]{6}, [dä]{14} [tuet]{15} [au]{14} [d]{9} [Wärch]{10}, [wo]{11} [ich]{12} [tue]{13}, und{16} [er wird]{19} [grösseri]{17} [als die]{18} [tue]{19}, [wil]{20} [ich]{21} [zum]{22,23} [Vatter]{24} [gang]{25}.",
 "JHN.14.13": "Und{1} [was]{2,3} [immer]{4} [ir]{5} [i]{6} [mim]{9} [Name]{7,8} [bittet]{5}, [das]{10} [tue ich]{11}, [demit]{12} [de]{14} [Vatter]{15} [im]{16,17} [Sohn]{18} [verherrlicht wird]{13}.",
 "JHN.14.14": "[Wänn]{1} [ir]{3} [mich]{4} [um öppis]{2} [bittet]{3} [i]{5} [mim]{8} [Name]{6,7}, [tue]{10} [ich]{9} [s]{10}.",
 "JHN.14.15": "[Wänn]{1} [ir]{2} [mich]{3} [liebed]{2}, [wärded ir]{8} [mini]{6,7} [Gebot]{4,5} [halte]{8}.",
 "JHN.14.16": "[Und ich]{1} [wirde]{2} [de]{3} [Vatter]{4} [bitte]{2}, und{5} [er wird]{8} [eu]{9} [en andere]{6} [Biistand]{7} [gää]{8}, [demit]{10} [er]{11} [bi]{12} [eu]{13} [isch]{11} [in]{14} [Ewigkeit]{15,16}:",
 "JHN.14.17": "[de Geischt]{1,2} [vo de]{3} [Wahrheit]{4}, [wo]{5} [d]{6} [Wält]{7} [nöd]{8} [cha]{9} [empfange]{10}, [wil]{11} [si]{13} [en]{14} [nöd]{12} [gseht]{13} [und au nöd]{15} [kännt]{16}. [Ir]{17} [kännt]{18} [en]{19}, [wil]{20} [er]{23} [bi]{21} [eu]{22} [bliibt]{23} und{24} [in]{25} [eu]{26} [sii wird]{27}.",
 "JHN.14.18": "[Ich laa]{2} [eu]{3} [nöd]{1} [als Waise]{4} [zrugg]{2}; [ich chume]{5} [zu]{6} [eu]{7}.",
 "JHN.14.19": "[No]{1} [es Wiili]{2}, und{3} [d]{4} [Wält]{5} [gseht]{8} [mich]{6} [nüme]{7}; [ir]{9} [aber]{10} [gsehnd]{11} [mich]{12}, [wil]{13} [ich]{14} [läbe]{15} und{16} [au ir]{17} [wärded läbe]{18}.",
 "JHN.14.20": "[A]{1} [säbem]{2} [Tag]{3,4} [wärded]{5} [ir]{6} [erchänne]{5}, [dass]{7} [ich]{8} [in]{9} [mim]{12} [Vatter]{10,11} bin und{13} [ir]{14} [in]{15} [mir]{16} [und ich]{17} [in]{18} [eu]{19}.",
 "JHN.14.21": "[Wär]{1} [mini]{5} [Gebot]{3,4} [hät]{2} und{6} [si]{8} [haltet]{7}, [dä]{9} [isch]{10} [s, wo]{11} [mich]{13} [liebt]{12}. [Wär]{14} [mich]{17} [aber]{15} [liebt]{16}, [wird]{18} [vo]{19} [mim]{22} [Vatter]{20,21} [gliebt wärde]{18}, [und ich]{23} [wirde]{24} [en]{25} [liebe]{24} und{26} [mich]{29} [ihm]{28} [offebare]{27}.»",
 "JHN.14.22": "[De Judas]{3} – [nöd]{4} [de]{5} [Iskariot]{6} – [seit]{1} [zu ihm]{2}: «[Herr]{7}, [was]{8} [isch passiert]{9}, [dass]{10} [du]{12} [dich]{14} [üs]{11} [wirsch]{12} [offebare]{13} und{15} [nöd]{16} [de]{17} [Wält]{18}?»",
 "JHN.14.23": "[De Jesus]{2} [hät gantwortet]{1} und{3} [zu ihm]{5} [gseit]{4}: «[Wänn]{6} [öpper]{7} [mich]{9} [liebt]{8}, [wird er]{13} [mis]{12} [Wort]{10,11} [halte]{13}, und{14} [min]{17} [Vatter]{15,16} [wird]{18} [en]{19} [liebe]{18}, und{20} [mir chömed]{23} [zu]{21} [ihm]{22} und{24} [nämed]{28} [bi]{26} [ihm]{27} [Wonig]{25}.",
 "JHN.14.24": "[Wär]{1} [mich]{4} [nöd]{2} [liebt]{3}, [haltet]{9} [mini]{7} [Wort]{5,6} [nöd]{8}. Und{10} [s]{11} [Wort]{12}, [wo]{13} [ir ghöred]{14}, [isch]{16} [nöd]{15} [mis]{17}, [sondern]{18} [s Wort vom]{19} [Vatter]{22}, [wo]{20} [mich]{21} [gschickt hät]{20}.",
 "JHN.14.25": "[Das]{1} [han ich]{2} [eu]{3} [gseit]{2}, [während ich]{6} [bi]{4} [eu]{5} [bliibe]{6}.",
 "JHN.14.26": "[De]{1} [Biistand]{3} [aber]{2}, [de]{4} [Heilig]{6,7} [Geischt]{5}, [wo]{8} [de]{10} [Vatter]{11} [i]{12} [mim]{15} [Name]{13,14} [schicke wird]{9}, [dä]{16} [wird]{18} [eu]{17} [alles]{19} [leere]{18} und{20} [eu]{22} [a]{21} [alles]{23} [erinnere]{21}, [wo]{24} [ich]{25} [eu]{26} [gseit han]{25}.",
 "JHN.14.27": "[Fride]{1} [loo ich]{2} [eu]{3} [zrugg]{2}, [min]{5,6} [Fride]{4} [gib ich]{7} [eu]{8}. [Nöd]{9} [wie]{10} [d]{11} [Wält]{12} [git]{13}, [gib]{15} [ich]{14} [eu]{16}. [Eues]{19} [Härz]{20,21} [söll]{18} [nöd]{17} [erschüttert sii]{18} [und nöd]{22} [verzaage]{23}.",
 "JHN.14.28": "[Ir händ ghört]{1}, [dass]{2} [ich]{3} [eu]{5} [gseit han]{4}: ‹[Ich gang]{6} und{7} [chume]{8} [zu]{9} [eu]{10}.› [Wänn]{11} [ir]{12} [mich]{13} [liebe würded]{12}, [würded ir]{15} [eu fröie]{14}, [dass]{16} [ich]{17} [zum]{18,19} [Vatter]{20} [gang]{17}, [wil]{21} [de]{22} [Vatter]{23} [grösser]{24} [isch]{26} [als ich]{25}.",
 "JHN.14.29": "Und{1} [jetzt]{2} [han ich s]{3} [eu]{4} [gseit]{3}, [bevor]{5} [s passiert]{6}, [demit]{7} [ir]{10}, [wänn]{8} [s passiert]{9}, [glaubed]{10}.",
 "JHN.14.30": "[Ich wirde]{3} [nüme]{1} [vil]{2} [mit]{4} [eu]{5} [rede]{3}, [dänn]{7} [de]{8} [Herrscher]{11} [vo de]{9} [Wält]{10} [chunnt]{6}. Und{12} [a]{13} [mir]{14} [hät er]{16} [nüüt]{15,17};",
 "JHN.14.31": "[aber]{1} [d]{4} [Wält]{5} [söll]{2} [erchänne]{3}, [dass]{6} [ich]{7} [de]{8} [Vatter]{9} [liebe]{7} und{10} [so]{16} [handle]{17}, [wie]{11} [de]{14} [Vatter]{15} [mir]{13} [befole hät]{12}. [Stönd uf]{18}, [mir gönd]{19} [vo da]{20} [furt]{19}!»",
 # ------------------------------------------------------------ Kapitel 15
 "JHN.15.1": "[Ich]{1} [bin]{2} [de]{3,5} [wahr]{6} [Wiistock]{4}, und{7} [min]{10} [Vatter]{8,9} [isch]{13} [de]{11} [Wiibuur]{12}.",
 "JHN.15.2": "[Jede]{1} [Schoss]{2} [a]{3} [mir]{4}, [wo]{6} [kei]{5} [Frucht]{7} [bringt]{6}, [nimmt er]{8} [wäg]{8}, und{10} [jede]{11}, [wo]{12} [Frucht]{13} [bringt]{14}, [macht er suuber]{15}, [demit]{17} er [meh]{19} [Frucht]{18} [bringt]{20}. ~9(αὐτό nimmt «jede Schoss» wider uf; nöd eigens widergää) ~16(αὐτό als Objekt vo καθαίρει; im Relativsatz mitgmeint)",
 "JHN.15.3": "[Ir]{2} [sind]{4} [scho]{1} [suuber]{3} [dur]{5} [s]{6} [Wort]{7}, [wo]{8} [ich]{9} [zu eu]{10} [gredt han]{9}.",
 "JHN.15.4": "[Bliibed]{1} [in]{2} [mir]{3}, [und ich]{4} [in]{5} [eu]{6}. [Wie]{7} [de]{8} [Schoss]{9} [nöd]{10} [vo]{14} [sich uus]{15} [Frucht]{12} [bringe]{13} [cha]{11}, [wänn]{16} [er]{18} [nöd]{17} [am]{19,20} [Wiistock]{21} [bliibt]{18}, [so]{22} [au]{23} [ir]{24} [nöd]{23}, [wänn]{25} [ir]{29} [nöd]{26} [in]{27} [mir]{28} [bliibed]{29}.",
 "JHN.15.5": "[Ich]{1} [bin]{2} [de]{3} [Wiistock]{4}, [ir]{5} sind [d]{6} [Schoss]{7}. [Wär]{8} [in]{10} [mir]{11} [bliibt]{9} [und ich]{12} [in]{13} [ihm]{14}, [dä]{15} [bringt]{16} [vil]{18} [Frucht]{17}; [dänn]{19} [ohni]{20} [mich]{21} [chönd ir]{23} [nüüt]{22,25} [mache]{24}.",
 "JHN.15.6": "[Wänn]{1} [öpper]{3} [nöd]{2} [in]{5} [mir]{6} [bliibt]{4}, [wird er]{7} [use]{8}[gworfe]{7} [wie]{9} [de]{10} [Schoss]{11} und{12} [verdoret]{13}; und{14} [mer sammlet]{15} [si]{16} und{17} [rüert]{21} si [is]{18,19} [Füür]{20}, und{22} [si verbränned]{23}.",
 "JHN.15.7": "[Wänn]{1} [ir]{2} [in]{3} [mir]{4} [bliibed]{2} und{5} [mini]{8} [Wort]{6,7} [in]{9} [eu]{10} [bliibed]{11}, [was]{12} [immer]{13} [ir wänd]{14}, [bitted drum]{15}, und{16} [es wird]{17} [eu]{18} [gscheh]{17}.",
 "JHN.15.8": "[Dadur]{1,2} [wird]{3} [min]{6} [Vatter]{4,5} [verherrlicht]{3}, [dass]{7} [ir]{10} [vil]{9} [Frucht]{8} [bringed]{10} und{11} [mini]{13} [Jünger]{14} [wärded]{12}.",
 "JHN.15.9": "[Wie]{1} [mich]{3} [de]{4} [Vatter]{5} [gliebt hät]{2}, [so han]{8} [au ich]{6} [eu]{7} [gliebt]{8}. [Bliibed]{9} [i]{10} [minere]{13,14} [Liebi]{11,12}!",
 "JHN.15.10": "[Wänn]{1} [ir]{5} [mini]{4} [Gebot]{2,3} [halted]{5}, [wärded ir]{6} [i]{7} [minere]{10} [Liebi]{8,9} [bliibe]{6}, [wie]{11} [ich]{12} [d]{13} [Gebot]{14} [vo mim]{15,17} [Vatter]{16} [ghalte han]{18} und{19} [i]{22} [sinere]{21} [Liebi]{23,24} [bliibe]{20}.",
 "JHN.15.11": "[Das]{1} [han ich]{2} [eu]{3} [gseit]{2}, [demit]{4} [mini]{7,8} [Fröid]{5,6} [in]{9} [eu]{10} [isch]{11} und{12} [eui]{15} [Fröid]{13,14} [vollkomme wird]{16}.",
 "JHN.15.12": "[Das]{1} [isch]{2} [mis]{5,6} [Gebot]{3,4}: [dass]{7} [ir]{8} [enand]{9} [liebed]{8}, [wie]{10} [ich]{11} [eu]{12} [gliebt han]{11}.",
 "JHN.15.13": "[Grösseri]{1} [Liebi]{3} [als die]{2} [hät]{5} [niemer]{4}: [dass]{6} [eine]{7} [sis]{8,10} [Läbe]{9} [hergit]{11} [für]{12} [sini]{13,15} [Fründe]{14}.",
 "JHN.15.14": "[Ir]{1} [sind]{4} [mini]{3} [Fründe]{2}, [wänn]{5} [ir tüend]{6}, [was]{7} [ich]{8} [eu]{10} [befile]{9}.",
 "JHN.15.15": "[Ich säg]{2} [eu]{3} [nüme]{1} [Chnächt]{4}, [dänn]{5} [de]{6} [Chnächt]{7} [weiss]{9} [nöd]{8}, [was]{10} [sin]{12} [Herr]{13,14} [macht]{11}. [Eu]{15} [aber]{16} [han ich]{17} [Fründe]{18} [gseit]{17}, [dänn]{19} [alles]{20}, [wo]{21} [ich]{22} [vo]{23} [mim]{26} [Vatter]{24,25} [ghört han]{22}, [han ich]{27} [eu]{28} [z wüsse taa]{27}.",
 "JHN.15.16": "[Nöd]{1} [ir]{2} [händ]{4} [mich]{3} [usgwählt]{4}, [sondern]{5} [ich]{6} [han]{7} [eu]{8} [usgwählt]{7}, und{9} [ich han]{10} [eu]{11} [defür iigsetzt]{10}, [dass]{12} [ir]{13} [gönd]{14} und{15} [Frucht]{16} [bringed]{17} und{18} [eui]{21} [Frucht]{19,20} [bliibt]{22}, [demit]{23} [er]{34} [eu]{35} [git]{34}, [was]{24,25} [immer]{26} [ir]{27} [de]{28} [Vatter]{29} [i]{30} [mim]{33} [Name]{31,32} [bittet]{27}.",
 "JHN.15.17": "[Das]{1} [befil ich]{2} [eu]{3}: [dass]{4} [ir]{5} [enand]{6} [liebed]{5}.",
 "JHN.15.18": "[Wänn]{1} [d]{2} [Wält]{3} [eu]{4} [hasst]{5}, [dänn wüssed]{6}, [dass]{7} [si]{11} [mich]{8} [vor]{9} [eu]{10} [ghasst hät]{11}.",
 "JHN.15.19": "[Wänn]{1} [ir]{5} [vo]{2} [de]{3} [Wält]{4} [wäred]{5}, [würd]{8} [d]{6} [Wält]{7} [ires]{9} [Eigete]{10} [gern ha]{11}. [Wil]{12} [ir]{18} [aber]{13} [nöd]{17} [vo]{14} [de]{15} [Wält]{16} [sind]{18}, [sondern]{19} [ich]{20} [eu]{22} [us]{23} [de]{24} [Wält]{25} [usgwählt han]{21}, [drum]{26,27} [hasst]{28} [eu]{29} [d]{30} [Wält]{31}.",
 "JHN.15.20": "[Dänked]{1} [as]{2} [Wort]{3}, [wo]{4} [ich]{5} [eu]{7} [gseit han]{6}: «[En Chnächt]{10} [isch]{9} [nöd]{8} [grösser]{11} [als]{12} [sin]{14} [Herr]{13}.» [Wänn]{15} [si]{17} [mich]{16} [verfolgt händ]{17}, [wärded si]{20} [au]{18} [eu]{19} [verfolge]{20}; [wänn]{21} [si]{25} [mis]{24} [Wort]{22,23} [ghalte händ]{25}, [wärded si]{29} [au]{26} [eues]{27,28} [halte]{29}.",
 "JHN.15.21": "[Aber]{1} [das]{2} [alles]{3} [wärded si]{4} [eu]{5,6} [aatue]{4} [wäge]{7} [mim]{10} [Name]{8,9}, [wil]{11} [si]{13} [dä]{14} [nöd]{12} [känned]{13}, [wo]{15} [mich]{16} [gschickt hät]{15}.",
 "JHN.15.22": "[Wänn]{1} [ich]{3} [nöd]{2} [choo wär]{3} und{4} [zu ine]{6} [gredt hett]{5}, [hetted si]{9} [kei]{8} [Sünd]{7}; [jetzt]{10} [aber]{11} [händ si]{14} [kei]{13} [Usred]{12} [für]{15} [iri]{16,18} [Sünd]{17}.",
 "JHN.15.23": "[Wär]{1} [mich]{2} [hasst]{3}, [hasst]{8} [au]{4} [min]{7} [Vatter]{5,6}.",
 "JHN.15.24": "[Wänn]{1} [ich]{5} [nöd]{4} [d]{2} [Wärch]{3} [under]{6} [ine]{7} [taa hett]{5}, [wo]{8} [kein]{9} [andere]{10} [taa hät]{11}, [hetted si]{14} [kei]{13} [Sünd]{12}; [jetzt]{15} [aber]{16} [händ si]{18} si [gseh]{18} [und]{19} [ghasst]{20} – [mich]{22} [und au]{23} [min]{26} [Vatter]{24,25}. ~17(καί … καί «sowohl … als auch» bi ἑωράκασιν nöd eigens widergää) ~21(καί … καί «sowohl … als auch» vor ἐμέ nöd eigens widergää)",
 "JHN.15.25": "[Aber]{1} das passiert, [demit]{2} [s]{4} [Wort]{5} [erfüllt wird]{3}, [wo]{6} [i]{7} [irem]{8,10} [Gsetz]{9} [gschribe staat]{11}: «[Si händ]{13} [mich]{14} [ohni Grund]{15} [ghasst]{13}.» ~12(ὅτι leitet s Zitat ii)",
 "JHN.15.26": "[Wänn]{1} [de]{3} [Biistand]{4} [chunnt]{2}, [wo]{5} [ich]{6} [eu]{8} [vom]{9,10} [Vatter]{11} [schicke wirde]{7}, [de Geischt]{12,13} [vo de]{14} [Wahrheit]{15}, [wo]{16} [vom]{17,18} [Vatter]{19} [usgaat]{20}, [dä]{21} [wird]{22} [über]{23} [mich]{24} [Züügnis ablegge]{22}.",
 "JHN.15.27": "[Und]{3} [au]{1} [ir]{2} [legged Züügnis ab]{4}, [wil]{5} [ir]{10} [vo]{6} [Aafang]{7} [aa]{6} [bi]{8} [mir]{9} [sind]{10}.",
 # ------------------------------------------------------------ Kapitel 16
 "JHN.16.1": "[Das]{1} [han ich]{2} [eu]{3} [gseit]{2}, [demit]{4} [ir]{6} [nöd]{5} [z Fall chömed]{6}.",
 "JHN.16.2": "[Us de Synagoge]{1} [wärded si]{2} [eu]{3} [usschlüüsse]{2}; [ja]{4}, [es chunnt]{5} [d Stund]{6}, [wo]{7} [jede]{8}, [wo]{9} [eu]{11} [tötet]{10}, [meint]{12}, [er bringi]{14} [Gott]{15,16} [en heilige Dienscht]{13} [dar]{14}.",
 "JHN.16.3": "Und{1} [das]{2} [wärded si mache]{3}, [wil]{4} [si]{6} [weder]{5} [de]{7} [Vatter]{8} [no]{9} [mich]{10} [erchännt händ]{6}.",
 "JHN.16.4": "[Aber]{1} [das]{2} [han ich]{3} [eu]{4} [gseit]{3}, [demit]{5} [ir]{11}, [wänn]{6} [iri]{10} [Stund]{8,9} [chunnt]{7}, [dra]{12} [dänked]{11}, [dass]{13} [ich]{14} [s eu]{16} [gseit han]{15}. [Das]{17} [aber]{18} [han ich]{23} [eu]{19} [nöd]{22} [vo]{20} [Aafang]{21} [aa]{20} [gseit]{23}, [wil]{24} [ich]{27} [bi]{25} [eu]{26} [gsii bin]{27}.",
 "JHN.16.5": "[Jetzt]{1} [aber]{2} [gang ich]{3} [zu]{4} [dem]{5}, [wo]{6} [mich]{7} [gschickt hät]{6}, und{8} [kein]{9} [vo]{10} [eu]{11} [fröget]{12} [mich]{13}: «[Wohii]{14} [gaasch]{15}?»",
 "JHN.16.6": "[Sondern]{1} [wil]{2} [ich]{4} [eu]{5} [das]{3} [gseit han]{4}, [hät]{8} [d]{6} [Truurigkeit]{7} [eues]{9} [Härz]{10,11} [gfüllt]{8}.",
 "JHN.16.7": "[Aber]{1} [ich]{2} [säge]{5} [eu]{6} [d]{3} [Wahrheit]{4}: [Es isch guet]{7} [für eu]{8}, [dass]{9} [ich]{10} [wäggang]{11}. [Dänn]{13} [wänn]{12} [ich]{15} [nöd]{14} [wäggang]{15}, [chunnt]{20} [de]{16} [Biistand]{17} [sicher nöd]{18,19} [zu]{21} [eu]{22}; [wänn]{23} [ich]{25} [aber]{24} [gang]{25}, [schick ich]{26} [en]{27} [zu]{28} [eu]{29}.",
 "JHN.16.8": "Und{1} [wänn]{2} [dä]{3} [chunnt]{2}, [wird er]{4} [d]{5} [Wält]{6} [überfüere]{4}: [wäge]{7} [de Sünd]{8} und{9} [wäge]{10} [de Grächtigkeit]{11} und{12} [wäge]{13} [em Gricht]{14};",
 "JHN.16.9": "[wäge]{1} [de Sünd]{2}, [wil]{4} [si]{6} [nöd]{5} [a]{7} [mich]{8} [glaubed]{6}; ~3(μέν … δέ gliederet d Ufzellig; nöd eigens widergää)",
 "JHN.16.10": "[wäge]{1} [de Grächtigkeit]{2}, [wil]{4} [ich]{8} [zum]{5,6} [Vatter]{7} [gang]{8} und{9} [ir]{11} [mich]{12} [nüme]{10} [gsehnd]{11}; ~3(μέν … δέ gliederet d Ufzellig; nöd eigens widergää)",
 "JHN.16.11": "[wäge]{1} [em Gricht]{3}, [wil]{4} [de]{5} [Herrscher]{6} [vo dere]{7,9} [Wält]{8} [grichtet isch]{10}. ~2(μέν … δέ gliederet d Ufzellig; nöd eigens widergää)",
 "JHN.16.12": "[No]{1} [vil]{2} [han ich]{3} [eu]{4} [z säge]{5}, [aber]{6} [ir chönd]{8} s [jetzt]{10} [nöd]{7} [träge]{9}.",
 "JHN.16.13": "[Wänn]{1} [aber]{2} [dä]{4} [chunnt]{3}, [de Geischt]{5,6} [vo de]{7} [Wahrheit]{8}, [wird er]{9} [eu]{10} [i]{11} [de]{12} [ganze]{14} [Wahrheit]{13} [füere]{9}; [dänn]{16} [er wird]{17} [nöd]{15} [vo]{18} [sich uus]{19} [rede]{17}, [sondern]{20} [was]{21} [er ghöre wird]{22}, [das wird er]{23} [rede]{23}, und{24} [was chunnt]{25,26}, [wird er]{27} [eu]{28} [verchünde]{27}.",
 "JHN.16.14": "[Dä]{1} [wird]{3} [mich]{2} [verherrliche]{3}, [dänn]{4} [er wird]{8} [vo]{5} [dem]{6}, [wo mir ghört]{7}, [nää]{8} und{9} s [eu]{11} [verchünde]{10}.",
 "JHN.16.15": "[Alles]{1}, [wo]{2} [de]{4} [Vatter]{5} [hät]{3}, [isch]{7} [mis]{6}. [Drum]{8,9} [han ich gseit]{10}, [dass]{11} [er]{15} [vo]{12} [dem]{13}, [wo mir ghört]{14}, [nimmt]{15} und{16} s [eu]{18} [verchünde wird]{17}.",
 "JHN.16.16": "[Es Wiili]{1}, und{2} [ir gsehnd]{4} [mich]{5} [nüme]{3}, und{6} [wider]{7} [es Wiili]{8}, und{9} [ir wärded]{10} [mich]{11} [gseh]{10}.",
 "JHN.16.17": "[Da]{2} [händ]{1} [es paar vo]{3} [sine]{4,6} [Jünger]{5} [zunenand]{7,8} [gseit]{1}: «[Was]{9} [isch]{10} [das]{11}, [wo]{12} [er]{13} [zu üs]{14} [seit]{13}: ‹[Es Wiili]{15}, und{16} [ir gsehnd]{18} [mich]{19} [nöd]{17}, und{20} [wider]{21} [es Wiili]{22}, und{23} [ir wärded]{24} [mich]{25} [gseh]{24}›, und{26}: ‹[Ich gang]{28} [zum]{29,30} [Vatter]{31}›?» ~27(ὅτι leitet s Zitat ii)",
 "JHN.16.18": "[Si händ]{1} [also]{2} [gseit]{1}: «[Was]{3} [isch]{4} [das]{5}, [wo]{6} [er seit]{7}: ‹[Es Wiili]{8}›? [Mir wüssed]{10} [nöd]{9}, [vo was]{11} [er redt]{12}.»",
 "JHN.16.19": "[De Jesus]{2} [hät gmerkt]{1}, [dass]{3} [si]{4} [en]{5} [wänd]{4} [fröge]{6}, und{7} [hät]{8} [zu ine]{9} [gseit]{8}: «[Drüber]{10,11} [fröged ir eu]{12} [undereinand]{13,14}, [dass]{15} [ich gseit han]{16}: ‹[Es Wiili]{17}, und{18} [ir gsehnd]{20} [mich]{21} [nöd]{19}, und{22} [wider]{23} [es Wiili]{24}, und{25} [ir wärded]{26} [mich]{27} [gseh]{26}›?",
 "JHN.16.20": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Ir]{9} [wärded briegge]{6} und{7} [chlage]{8}, [d]{10} [Wält]{12} [aber]{11} [wird sich fröie]{13}. [Ir]{14} [wärded truurig sii]{15}, [aber]{16} [eui]{19} [Truurigkeit]{17,18} [wird]{22} [zur]{20} [Fröid]{21} [wärde]{22}. ~5(ὅτι leitet d Red ii)",
 "JHN.16.21": "[Wänn]{3} [e]{1} [Frau]{2} [am Gebäre isch]{4}, [hät si]{6} [Schmerz]{5}, [wil]{7} [iri]{11} [Stund]{9,10} [choo isch]{8}; [wänn]{12} [si]{14} [aber]{13} [s]{15} [Chind]{16} [übercho hät]{14}, [dänkt si]{18} [nüme]{17} [a d]{19} [Not]{20} [vor]{21} [Fröid]{22,23}, [dass]{24} [en Mänsch]{26} [i]{27} [d]{28} [Wält]{29} [gebore worde isch]{25}.",
 "JHN.16.22": "[So]{3} [händ]{7} [au]{1} [ir]{2} [jetzt]{4} [Truurigkeit]{6}; [aber]{9} [ich wirde]{10} [eu]{11} [wider]{8} [gseh]{10}, und{12} [eues]{14} [Härz]{15,16} [wird sich fröie]{13}, und{17} [eui]{18,20} [Fröid]{19} [nimmt]{22} [niemer]{21} [vo]{23} [eu]{24} [wäg]{22}. ~5(μέν … δέ; nöd eigens widergää)",
 "JHN.16.23": "Und{1} [a]{2} [säbem]{3} [Tag]{4,5} [wärded ir]{8} [mich]{6} [nüüt]{7,9} [fröge]{8}. [Amen]{10}, [amen]{11}, [ich säge]{12} [eu]{13}: [Wänn]{14} [ir]{16} [de]{17} [Vatter]{18} [um öppis]{15} [bittet]{16}, [wird er]{19} [s eu]{20} [i]{21} [mim]{24} [Name]{22,23} [gää]{19}.",
 "JHN.16.24": "[Bis]{1} [jetzt]{2} [händ ir]{4} [um nüüt]{3,5} [bätte]{4} [i]{6} [mim]{9} [Name]{7,8}. [Bitted]{10}, und{11} [ir wärded s überchoo]{12}, [demit]{13} [eui]{16} [Fröid]{14,15} [vollkomme]{18} [isch]{17}.",
 "JHN.16.25": "[Das]{1} [han ich]{4} [i]{2} [Bildwort]{3} [zu eu]{5} [gredt]{4}. [Es chunnt]{6} [d Stund]{7}, [wo]{8} [ich]{12} [nüme]{9} [i]{10} [Bildwort]{11} [zu eu]{13} [rede]{12}, [sondern]{14} [eu]{20} [offe]{15} [vom]{16,17} [Vatter]{18} [verzelle]{19}.",
 "JHN.16.26": "[A]{1} [säbem]{2} [Tag]{3,4} [wärded ir]{9} [i]{5} [mim]{8} [Name]{6,7} [bitte]{9}, und{10} [ich säge]{12} [eu]{13} [nöd]{11}, [dass]{14} [ich]{15} [de]{17} [Vatter]{18} [für]{19} [eu]{20} [wirde bitte]{16}.",
 "JHN.16.27": "[Dänn]{2} [de]{3} [Vatter]{4} [sälber]{1} [hät]{5} [eu]{6} [gern]{5}, [wil]{7} [ir]{8} [mich]{9} [gern gha händ]{10} und{11} [glaubt händ]{12}, [dass]{13} [ich]{14} [vo]{15} [Gott]{16,17} [usgange bin]{18}.",
 "JHN.16.28": "[Ich bin]{1} [vom]{2,3} [Vatter]{4} [usgange]{1} und{5} [bin]{6} [i]{7} [d]{8} [Wält]{9} [choo]{6}; [wider]{10} [verlaa ich]{11} [d]{12} [Wält]{13} und{14} [gang]{15} [zum]{16,17} [Vatter]{18}.»",
 "JHN.16.29": "[Sini]{2,4} [Jünger]{3} [säged]{1}: «[Lueg]{5}, [jetzt]{6} [redsch du]{9} [offe]{7,8} und{10} [seisch]{13} [kei]{12} [Bildwort]{11}.",
 "JHN.16.30": "[Jetzt]{1} [wüssed mir]{2}, [dass]{3} [du]{4} [alles]{5} [weisch]{4} und{6} s [nöd]{7} [nötig]{8} [häsch]{9}, [dass]{10} [di]{12} [öpper]{11} [fröget]{13}. [Drum]{14,15} [glaubed mir]{16}, [dass]{17} [du]{20} [vo]{18} [Gott]{19} [usgange bisch]{20}.»",
 "JHN.16.31": "[De Jesus]{3} [hät]{1} [ine]{2} [gantwortet]{1}: «[Jetzt]{4} [glaubed ir]{5}?",
 "JHN.16.32": "[Lueg]{1}, [es chunnt]{2} [d Stund]{3}, und{4} [si isch choo]{5}, [wo]{6} [ir verstreut wärded]{7}, [jede]{8} [zu]{9} [sich hei]{10,11}, [und mich]{12} [elei]{13} [lönd]{14}. Und{15} [ich bin]{17} [nöd]{16} [elei]{18}, [wil]{19} [de]{20} [Vatter]{21} [bi]{22} [mir]{23} [isch]{24}.",
 "JHN.16.33": "[Das]{1} [han ich]{2} [eu]{3} [gseit]{2}, [demit]{4} [ir]{8} [in]{5} [mir]{6} [Fride]{7} [händ]{8}. [I]{9} [de]{10} [Wält]{11} [händ ir]{13} [Not]{12}; [aber]{14} [händ Muet]{15}: [Ich]{16} [han]{17} [d]{18} [Wält]{19} [überwunde]{17}.»",
 # ------------------------------------------------------------ Kapitel 17
 "JHN.17.1": "[Das]{1} [hät]{2} [de Jesus]{3} [gseit]{2}, und{4} [er hät]{5} [sini]{6,8} [Auge]{7} [zum]{9,10} [Himmel]{11} [ufghebt]{5} und [gseit]{12}: «[Vatter]{13}, [d]{15} [Stund]{16} [isch choo]{14}. [Verherrlich]{17} [din]{18,19} [Sohn]{20}, [demit]{21} [de]{22} [Sohn]{23} [dich]{25} [verherrlicht]{24},",
 "JHN.17.2": "[wie]{1} [du]{2} [ihm]{3} [Vollmacht]{4} [über alles]{5} [Fleisch]{6} [gää häsch]{2}, [demit]{7} [er]{12} [allne]{8}, [wo]{9} [du]{10} [ihm]{11} [gää häsch]{10}, [ewigs]{15} [Läbe]{14} [git]{12}. ~13(αὐτοῖς «ine» nimmt πᾶν ὅ «alles, wo» als Persone wider uf; in «allne, wo» enthalte)",
 "JHN.17.3": "[Das]{1} [aber]{2} [isch]{3} [s]{4} [ewig]{5} [Läbe]{6}: [dass]{7} [si]{8} [dich]{9}, [de]{10} [einzig]{11} [wahr]{12} [Gott]{13}, [erchänned]{8} und{14} [dä, wo]{15} [du gschickt häsch]{16}, [Jesus]{17} [Christus]{18}.",
 "JHN.17.4": "[Ich]{1} [han]{3} [dich]{2} [uf]{4} [de]{5} [Ärde]{6} [verherrlicht]{3}, [indem ich]{9} [s]{7} [Wärch]{8} [volländet han]{9}, [wo]{10} [du]{11} [mir]{12} [gää häsch]{11}, [demit]{13} [ich s tue]{14}.",
 "JHN.17.5": "Und{1} [jetzt]{2} [verherrlich]{3} [du]{5} [mich]{4}, [Vatter]{6}, [bi]{7} [dir]{8} [mit de]{9} [Herrlichkeit]{10}, [wo]{11} [ich]{12} [bi]{18} [dir]{19} [gha han]{12}, [bevor]{13,14} [d]{15} [Wält]{16} [gsii isch]{17}.",
 "JHN.17.6": "[Ich han]{1} [din]{2,3} [Name]{4} [de]{5} [Mänsche]{6} [offebart]{1}, [wo]{7} [du]{8} [mir]{9} [us]{10} [de]{11} [Wält]{12} [gää häsch]{8}. [Dir]{13} [händ si ghört]{14}, [und mir]{15} [häsch du]{17} [si]{16} [gää]{17}, und{18} [si händ]{22} [dis]{21} [Wort]{19,20} [ghalte]{22}.",
 "JHN.17.7": "[Jetzt]{1} [händ si erchännt]{2}, [dass]{3} [alles]{4}, [wo]{5} [du]{6} [mir]{7} [gää häsch]{6}, [vo]{8} [dir]{9} [chunnt]{10}.",
 "JHN.17.8": "[Dänn]{1} [d]{2} [Wort]{3}, [wo]{4} [du]{5} [mir]{6} [gää häsch]{5}, [han ich]{7} [ine]{8} [gää]{7}, und{9} [si]{10} [händ si aagnoo]{11} und{12} [würkli]{14} [erchännt]{13}, [dass]{15} [ich]{18} [vo]{16} [dir]{17} [usgange bin]{18}, und{19} [si händ glaubt]{20}, [dass]{21} [du]{22} [mich]{23} [gschickt häsch]{24}.",
 "JHN.17.9": "[Ich]{1} [bitte]{4} [für]{2} [si]{3}; [nöd]{5} [für]{6} [d]{7} [Wält]{8} [bitt ich]{9}, [sondern]{10} [für]{11} [die, wo]{12} [du]{13} [mir]{14} [gää häsch]{13}, [dänn]{15} [si ghöred]{17} [dir]{16},",
 "JHN.17.10": "und{1} [alles]{4}, [wo mir ghört]{2,3}, [isch]{6} [dis]{5}, und{7} [was]{8} [dir ghört]{9}, [isch mis]{10}, und{11} [ich bin]{12} [in]{13} [ine]{14} [verherrlicht]{12}.",
 "JHN.17.11": "Und{1} [ich bin]{3} [nüme]{2} [i]{4} [de]{5} [Wält]{6}, und{7} [si]{8} [sind]{12} [i]{9} [de]{10} [Wält]{11}, [und ich]{13} [chume]{16} [zu]{14} [dir]{15}. [Heilige]{18} [Vatter]{17}, [bhüet]{19} [si]{20} [i]{21} [dim]{22,24} [Name]{23}, [wo]{25} [du]{26} [mir]{27} [gää häsch]{26}, [demit]{28} [si]{29} [eis]{30} [sind]{29}, [wie]{31} [mir]{32}.",
 "JHN.17.12": "[Wo]{1} [ich]{2} [bi]{3} [ine]{4} [gsii bin]{2}, [han]{6} [ich]{5} [si]{7} [i]{8} [dim]{9,11} [Name]{10}, [wo]{12} [du]{13} [mir]{14} [gää häsch]{13}, [bhüetet]{6}, und{15} [ich han uf si ufpasst]{16}, und{17} [kein]{18} [vo]{19} [ine]{20} [isch verlore gange]{21} [usser]{22,23} [em]{24} [Sohn]{25} [vom]{26} [Verderbe]{27}, [demit]{28} [d]{29} [Schrift]{30} [erfüllt wird]{31}.",
 "JHN.17.13": "[Jetzt]{1} [aber]{2} [chumm ich]{5} [zu]{3} [dir]{4}, und{6} [das]{7} [säg ich]{8} [i]{9} [de]{10} [Wält]{11}, [demit]{12} [si]{13} [mini]{16,17} [Fröid]{14,15} [vollkomme]{18} [in]{19} [sich]{20} [händ]{13}.",
 "JHN.17.14": "[Ich]{1} [han]{2} [ine]{3} [dis]{4,6} [Wort]{5} [gää]{2}, und{7} [d]{8} [Wält]{9} [hät]{10} [si]{11} [ghasst]{10}, [wil]{12} [si]{14} [nöd]{13} [vo]{15} [de]{16} [Wält]{17} [sind]{14}, [wie]{18} [ich]{19} [nöd]{20} [vo]{22} [de]{23} [Wält]{24} [bin]{21}.",
 "JHN.17.15": "[Ich bitte]{2} [nöd]{1}, [dass]{3} [du]{4} [si]{5} [us]{6} [de]{7} [Wält]{8} [wägnimmsch]{4}, [sondern]{9} [dass]{10} [du]{11} [si]{12} [vor]{13} [em]{14} [Böse]{15} [bhüetisch]{11}.",
 "JHN.17.16": "[Si sind]{5} [nöd]{4} [vo]{1} [de]{2} [Wält]{3}, [wie]{6} [ich]{7} [nöd]{8} [vo]{10} [de]{11} [Wält]{12} [bin]{9}.",
 "JHN.17.17": "[Heilig]{1} [si]{2} [i]{3} [de]{4} [Wahrheit]{5}; [dis]{8,9} [Wort]{6,7} [isch]{11} [Wahrheit]{10}.",
 "JHN.17.18": "[Wie]{1} [du]{3} [mich]{2} [i]{4} [d]{5} [Wält]{6} [gschickt häsch]{3}, [so han]{8} [au ich]{7} [si]{9} [i]{10} [d]{11} [Wält]{12} [gschickt]{8}.",
 "JHN.17.19": "Und{1} [für]{2} [si]{3} [heilige]{5} [ich]{4} [mich sälber]{6}, [demit]{7} [au]{9} [si]{10} [i]{12} [Wahrheit]{13} [gheiliget]{11} [sind]{8}.",
 "JHN.17.20": "[Ich bitte]{5} [aber]{4} [nöd]{1} [nu]{6} [für]{2} [die]{3}, [sondern]{7} [au]{8} [für]{9} [die, wo]{10} [dur]{12} [ires]{13,15} [Wort]{14} [a]{16} [mich]{17} [glaubed]{11},",
 "JHN.17.21": "[demit]{1} [alli]{2} [eis]{3} [sind]{4}, [wie]{5} [du]{6}, [Vatter]{7}, [in]{8} [mir]{9} bisch [und ich]{10} [in]{11} [dir]{12}, [demit]{13} [au]{14} [si]{15} [in]{16} [üs]{17} [sind]{18}, [demit]{19} [d]{20} [Wält]{21} [glaubt]{22}, [dass]{23} [du]{24} [mich]{25} [gschickt häsch]{26}.",
 "JHN.17.22": "[Und ich]{1} [han]{7} [ine]{8} [d]{2} [Herrlichkeit]{3} [gää]{7}, [wo]{4} [du]{5} [mir]{6} [gää häsch]{5}, [demit]{9} [si]{10} [eis]{11} [sind]{10}, [wie]{12} [mir]{13} [eis]{14} sind,",
 "JHN.17.23": "[ich]{1} [in]{2} [ine]{3} und{4} [du]{5} [in]{6} [mir]{7}, [demit]{8} [si]{9} [volländet]{10} [sind]{9} [zur]{11} [Einheit]{12}, [demit]{13} [d]{15} [Wält]{16} [erchännt]{14}, [dass]{17} [du]{18} [mich]{19} [gschickt häsch]{20} und{21} [si]{23} [gliebt häsch]{22}, [wie]{24} [du]{26} [mich]{25} [gliebt häsch]{26}.",
 "JHN.17.24": "[Vatter]{1}, [was]{2} [du]{3} [mir]{4} [gää häsch]{3} – [ich wott]{5}, [dass]{6} [au die]{10} [bi]{12} [mir]{13} [sind]{11}, [wo]{7} [ich]{9} [bin]{8}, [demit]{14} [si]{15} [mini]{18,19} [Herrlichkeit]{16,17} [gsehnd]{15}, [wo]{20} [du]{21} [mir]{22} [gää häsch]{21}, [wil]{23} [du]{24} [mich]{25} [gliebt häsch]{24} [vor]{26} [de Grundlegig]{27} [vo de Wält]{28}.",
 "JHN.17.25": "[Grächte]{2} [Vatter]{1}, [d]{4} [Wält]{5} [hät]{8} [dich]{6} [zwar]{3} [nöd]{7} [erchännt]{8}, [ich]{9} [aber]{10} [han]{12} [dich]{11} [erchännt]{12}, und{13} [die da]{14} [händ erchännt]{15}, [dass]{16} [du]{17} [mich]{18} [gschickt häsch]{19},",
 "JHN.17.26": "und{1} [ich han]{2} [ine]{3} [din]{4,6} [Name]{5} [bekannt gmacht]{2} und{7} [wirde en bekannt mache]{8}, [demit]{9} [d]{10} [Liebi]{11}, [wo]{12} [du]{13} [mich]{14} [demit gliebt häsch]{13}, [in]{15} [ine]{16} [isch]{17} [und ich]{18} [in]{19} [ine]{20}.»",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
G01 = "Grundentscheid siehe scripts/authoring/johannes_text_01_03.py."
DEC_DE = [
 ("JHN.14.1", "Glaubt an Gott", "interpretive", "πιστεύετε εἰς τὸν θεόν", None, ["Ihr glaubt an Gott"], "πιστεύετε kann Imperativ («glaubt!») oder Indikativ («ihr glaubt») sein, beide Male. Möglich sind deshalb mehrere Verbindungen, z. B. «Ihr glaubt an Gott, glaubt auch an mich». Die Übersetzung liest zweimal den Imperativ, weil der Vers mit einer Aufforderung beginnt (μὴ ταρασσέσθω)."),
 ("JHN.14.2", "Wohnungen", "literal", "μοναὶ", "Bleiben", ["Bleiben", "Räume"], "μονή ist das Hauptwort zu μένω «bleiben»: ein Ort, an dem man bleibt. Dasselbe Wort steht in [[JHN.14.23]] («Wohnung nehmen»). An Zimmer in einem Gebäude denkt das Wort nicht ausdrücklich."),
 ("JHN.14.2", "hätte ich euch dann gesagt", "interpretive", "εἶπον ἂν ὑμῖν ὅτι", "hätte ich euch gesagt, dass", ["hätte ich es euch gesagt; denn ich gehe hin", "hätte ich euch gesagt: Ich gehe hin"], "Der Satz ist mehrdeutig. ὅτι kann «dass» (dann am besten als Frage), «denn» oder ein Doppelpunkt vor direkter Rede sein. Der SBLGNT setzt kein Fragezeichen; die Frage ist eine redaktionelle Entscheidung. Zur Lesart ohne ὅτι siehe die Alternative."),
 ("JHN.14.6", "Ich bin der Weg", "literal", "Ἐγώ εἰμι ἡ ὁδὸς", None, None, "Eines der Ich-bin-Worte mit Bildwort (vgl. [[JHN.6.35]], [[JHN.8.12]], [[JHN.10.11]], [[JHN.11.25]], [[JHN.15.1]]). ἐγώ εἰμι wird durchgehend «Ich bin …» wiedergegeben. " + G01),
 ("JHN.14.12", "Amen, amen, ich sage euch", "literal", "ἀμὴν ἀμὴν λέγω ὑμῖν", None, ["Wahrlich, wahrlich, ich sage euch"], "Das verdoppelte Amen steht nur im Johannesevangelium; es leitet eine feierliche Aussage ein. " + G01),
 ("JHN.14.13", "verherrlicht wird", "literal", "δοξασθῇ", None, ["geehrt wird"], "δοξάζω wird durchgehend «verherrlichen», δόξα «Herrlichkeit» wiedergegeben ([[JHN.15.8]], [[JHN.16.14]], [[JHN.17.1]]–[[JHN.17.5]], [[JHN.17.10]], [[JHN.17.22]], [[JHN.17.24]]). " + G01),
 ("JHN.14.16", "Beistand", "interpretive", "παράκλητον", "Herbeigerufenen", ["Fürsprecher", "Anwalt", "Tröster", "Helfer", "Paraklet"], "παράκλητος heisst wörtlich «der Herbeigerufene», besonders der Beistand vor Gericht. In [[1JN.2.1]] ist Jesus der Fürsprecher beim Vater; hier ist es der Geist, «ein anderer» Beistand. «Tröster» (seit Luther) betont eine Seite (παρακαλέω «ermutigen, trösten»), «Anwalt» die gerichtliche. «Beistand» gilt durchgehend ([[JHN.14.26]], [[JHN.15.26]], [[JHN.16.7]]). " + G01),
 ("JHN.14.16", "in Ewigkeit", "literal", "εἰς τὸν αἰῶνα", None, ["für immer"], None),
 ("JHN.14.17", "den Geist der Wahrheit", "adapted", "τὸ πνεῦμα τῆς ἀληθείας", None, None, "πνεῦμα ist im Griechischen sächlich (Pronomen αὐτό); im Deutschen steht wegen «der Geist» das männliche «ihn». Johannes selbst setzt in [[JHN.14.26]], [[JHN.15.26]] und [[JHN.16.13]] das männliche ἐκεῖνος («jener»)."),
 ("JHN.14.17", "Welt", "literal", "κόσμος", None, None, "κόσμος wird durchgehend «Welt» wiedergegeben; das Wort steht in Kapitel 14–17 38-mal (Zählung nach den MACULA-Lemmata), davon 18-mal im Gebet (Kapitel 17). Gemeint ist oft die Menschenwelt, die sich Gott verschliesst ([[JHN.15.18]]–[[JHN.15.19]]), aber auch die Welt, in die die Jünger gesandt sind ([[JHN.17.18]]). " + G01),
 ("JHN.14.17", "bleibt", "literal", "μένει", None, ["wohnt"], "μένω wird durchgehend «bleiben» wiedergegeben, auch wo «wohnen» oder «verbunden sein» flüssiger wäre; so bleibt das Leitwort sichtbar. In Kapitel 14–17 steht μένω 14-mal (nach MACULA-Lemma), elfmal davon in [[JHN.15.4]]–[[JHN.15.16]]. " + G01),
 ("JHN.14.21", "offenbaren", "literal", "ἐμφανίσω", None, ["zeigen", "sichtbar machen"], "ἐμφανίζω heisst «sichtbar machen, offenbaren». Judas greift das Wort in [[JHN.14.22]] auf."),
 ("JHN.14.23", "Wohnung nehmen", "adapted", "μονὴν ποιησόμεθα", "eine Bleibe machen", ["Wohnung machen", "bei ihm bleiben"], "μονή wie in [[JHN.14.2]]: Was dort für das Haus des Vaters verheissen ist, wird hier für den Menschen gesagt, der Jesus liebt."),
 ("JHN.14.27", "Frieden hinterlasse ich euch", "literal", "εἰρήνην ἀφίημι ὑμῖν", None, ["Frieden lasse ich euch"], "Wie ein Abschiedsgruss formuliert; ἀφίημι heisst hier «zurücklassen, hinterlassen» (vgl. [[JHN.14.18]])."),
 ("JHN.14.28", "grösser als ich", "literal", "μείζων μού", None, None, "Wörtlich belassen. Wie das Wort zu Aussagen wie [[JHN.10.30]] passt, ist seit der Alten Kirche verschieden erklärt worden (etwa auf die Sendung oder auf das Menschsein Jesu bezogen); die Übersetzung entscheidet das nicht."),
 ("JHN.14.30", "der Herrscher der Welt", "literal", "ὁ τοῦ κόσμου ἄρχων", None, ["der Fürst der Welt"], "Gemeint ist der Widersacher Gottes (vgl. [[JHN.12.31]], [[JHN.16.11]]). Der Text nennt ihn hier nicht mit Namen."),
 ("JHN.14.30", "an mir hat er nichts", "literal", "ἐν ἐμοὶ οὐκ ἔχει οὐδέν", "in mir hat er nichts", ["über mich hat er keine Macht", "an mir hat er keinen Anspruch"], "Die Wendung ist knapp; sie kann bedeuten, dass er keinen Anhaltspunkt oder keinen Anspruch an Jesus hat. Die wörtliche Wiedergabe lässt das offen."),
 ("JHN.14.31", "aber die Welt soll erkennen", "interpretive", "ἀλλʼ ἵνα γνῷ ὁ κόσμος", "aber damit die Welt erkennt", ["aber damit die Welt erkennt …, steht auf"], "Der ἵνα-Satz hat keinen Hauptsatz. Er kann für sich als Absicht stehen (so hier) oder mit dem folgenden «Steht auf» verbunden werden."),
 ("JHN.14.31", "Steht auf, lasst uns von hier gehen", "literal", "Ἐγείρεσθε, ἄγωμεν ἐντεῦθεν", None, None, "Erst in [[JHN.18.1]] wird erzählt, dass Jesus mit den Jüngern hinausgeht; dazwischen stehen Kapitel 15–17. Ob die Reden in mehreren Stufen gewachsen sind oder ob die Abfolge bewusst so gestaltet ist, wird in der Forschung unterschiedlich beurteilt."),
 ("JHN.15.1", "der wahre Weinstock", "literal", "ἡ ἄμπελος ἡ ἀληθινή", None, ["der wahre Rebstock"], "ἄμπελος ist die ganze Weinpflanze, κλῆμα der einzelne Trieb («Rebe»). In den Schriften Israels ist der Weinstock bzw. Weinberg ein Bild für Israel ([[PSA.80.8]]–[[PSA.80.16]], [[ISA.5.1]]–[[ISA.5.7]], [[JER.2.21]]). ἀληθινός heisst «wahr, echt». Ein Ich-bin-Wort wie [[JHN.14.6]]."),
 ("JHN.15.1", "Weingärtner", "adapted", "γεωργός", "Bauer", ["Winzer", "Landwirt"], "γεωργός ist allgemein der Landarbeiter; im Bild ist der Weinbauer gemeint."),
 ("JHN.15.2", "nimmt er weg", "literal", "αἴρει", None, ["hebt er auf"], "αἴρω heisst «wegnehmen» und «hochheben». Gewöhnlich wird es hier als Entfernen der fruchtlosen Rebe verstanden (vgl. [[JHN.15.6]]); vereinzelt wird an das Hochbinden am Boden liegender Reben gedacht."),
 ("JHN.15.2", "reinigt er", "literal", "καθαίρει", None, ["beschneidet er"], "Im Weinbau ist das Zurückschneiden gemeint. Das Wort ist gewählt wegen des Wortspiels mit καθαροί «rein» in [[JHN.15.3]] (vgl. [[JHN.13.10]]); «reinigt» hält es sichtbar."),
 ("JHN.15.3", "rein durch das Wort", "adapted", "καθαροί διὰ τὸν λόγον", "rein wegen des Wortes", ["rein um des Wortes willen"], "διά mit Akkusativ heisst eigentlich «wegen»; gemeint ist, dass das Wort Jesu sie rein gemacht hat."),
 ("JHN.15.6", "wird er hinausgeworfen", "adapted", "ἐβλήθη ἔξω ἐξηράνθη", "wurde er hinausgeworfen … und verdorrte", ["ist er hinausgeworfen"], "Die Aoriste beschreiben, was in einem solchen Fall geschieht (zeitlos), nicht ein vergangenes Ereignis; deshalb Präsens."),
 ("JHN.15.8", "wird mein Vater verherrlicht", "adapted", "ἐδοξάσθη", "wurde verherrlicht", ["ist verherrlicht worden"], "Aorist; wie in [[JHN.15.6]] als allgemein gültige Aussage wiedergegeben."),
 ("JHN.15.11", "vollkommen wird", "adapted", "πληρωθῇ", "erfüllt wird", ["voll wird"], "πληρόω «füllen, erfüllen»; ebenso [[JHN.16.24]] und [[JHN.17.13]] («vollkommen»)."),
 ("JHN.15.13", "sein Leben hingibt", "adapted", "τὴν ψυχὴν αὐτοῦ θῇ", "seine Seele hinlegt", ["sein Leben einsetzt"], "Dieselbe Wendung wie beim guten Hirten ([[JHN.10.11]], [[JHN.10.15]]); ψυχή steht hier für das Leben."),
 ("JHN.15.15", "Knechte", "traditional", "δούλους", None, ["Sklaven", "Diener"], "δοῦλος ist der unfreie Diener, oft ein Sklave. «Knecht» ist die vertraute Wiedergabe und nimmt das Wort aus [[JHN.13.16]] auf, das in [[JHN.15.20]] zitiert wird."),
 ("JHN.15.19", "lieb haben", "literal", "ἐφίλει", None, ["lieben"], "φιλέω (verwandt mit φίλος «Freund», [[JHN.15.13]]–[[JHN.15.15]]) steht in Kapitel 14–17 dreimal ([[JHN.15.19]], zweimal in [[JHN.16.27]]); sonst steht ἀγαπάω «lieben». Um die Wortwahl sichtbar zu halten, steht für φιλέω «lieb haben». Ob Johannes die beiden Verben bedeutungsmässig unterscheidet, ist umstritten; viele halten sie bei ihm für weitgehend gleichbedeutend."),
 ("JHN.15.25", "in ihrem Gesetz", "literal", "ἐν τῷ νόμῳ αὐτῶν", None, ["in ihrer Schrift"], "Das Zitat steht in den Psalmen ([[PSA.35.19]], [[PSA.69.4]]); «Gesetz» bezeichnet hier die Schrift insgesamt (vgl. [[JHN.10.34]])."),
 ("JHN.15.26", "vom Vater ausgeht", "literal", "παρὰ τοῦ πατρὸς ἐκπορεύεται", None, None, "Der Vers spricht vom Senden durch Jesus und vom Ausgehen vom Vater. Auf ihn beziehen sich später die kirchlichen Lehrstreitigkeiten über den Ausgang des Geistes (Filioque); der Text selbst führt diese Frage nicht aus."),
 ("JHN.15.27", "legt Zeugnis ab", "interpretive", "μαρτυρεῖτε", None, ["legt Zeugnis ab!", "werdet Zeugnis ablegen"], "μαρτυρεῖτε kann Indikativ oder Imperativ sein; hier als Feststellung gelesen."),
 ("JHN.16.1", "zu Fall kommt", "interpretive", "σκανδαλισθῆτε", None, ["Anstoss nehmt", "irre werdet", "vom Glauben abfallt"], "σκανδαλίζω: zu Fall bringen, am Glauben irre werden lassen."),
 ("JHN.16.2", "Aus der Synagoge werden sie euch ausschliessen", "adapted", "ἀποσυναγώγους ποιήσουσιν", "zu Aus-der-Synagoge-Ausgeschlossenen machen", None, "ἀποσυνάγωγος findet sich nur bei Johannes ([[JHN.9.22]], [[JHN.12.42]]). Welche geschichtlichen Vorgänge dahinterstehen und wann sie stattfanden, wird in der Forschung unterschiedlich beurteilt."),
 ("JHN.16.2", "einen heiligen Dienst darzubringen", "interpretive", "λατρείαν προσφέρειν", "einen Dienst darzubringen", ["einen Gottesdienst zu tun", "ein Opfer darzubringen"], "λατρεία ist der kultische Dienst für Gott; προσφέρω ist das Wort für das Darbringen von Opfern."),
 ("JHN.16.8", "überführen", "interpretive", "ἐλέγξει", None, ["aufdecken", "zurechtweisen", "der Welt zeigen, was … ist"], "ἐλέγχω heisst «überführen, aufdecken, zurechtweisen». Mit περί («hinsichtlich») ist offen, ob der Geist die Welt ihrer Sünde überführt oder ihr zeigt, was Sünde, Gerechtigkeit und Gericht wirklich sind. Die Begründungen in [[JHN.16.9]]–[[JHN.16.11]] (ὅτι, hier «weil», auch «dass» möglich) werden verschieden verbunden."),
 ("JHN.16.9", "weil", "interpretive", "ὅτι", None, ["dass", "insofern"], "ὅτι kann begründen («weil») oder den Inhalt angeben («dass»); ebenso [[JHN.16.10]] und [[JHN.16.11]]."),
 ("JHN.16.13", "in der ganzen Wahrheit leiten", "literal", "ὁδηγήσει ἐν τῇ ἀληθείᾳ πάσῃ", None, ["in die ganze Wahrheit führen"], "ὁδηγέω «auf dem Weg führen». Der SBLGNT liest hier mit NA28 ἐν («in»), WH und Treg εἰς («hinein in»); siehe Alternative."),
 ("JHN.16.21", "Schmerz", "adapted", "λύπην", "Trauer", ["Kummer"], "Dasselbe Wort λύπη ist in [[JHN.16.6]], [[JHN.16.20]] und [[JHN.16.22]] mit «Trauer» übersetzt; bei der Geburt passt im Deutschen «Schmerz». Das Bild verbindet beides."),
 ("JHN.16.23", "fragen", "interpretive", "ἐρωτήσετε", None, ["bitten"], "ἐρωτάω heisst «fragen» und «bitten». Hier wird «fragen» gelesen, weil die Jünger in [[JHN.16.19]] Jesus fragen wollten; im zweiten Satzteil steht αἰτέω «bitten». In [[JHN.14.16]], [[JHN.16.26]] und [[JHN.17.9]] ist ἐρωτάω mit «bitten» übersetzt."),
 ("JHN.16.25", "Bildworten", "interpretive", "παροιμίαις", None, ["Rätselworten", "Gleichnissen", "verhüllter Rede"], "παροιμία ist ein Bildwort oder Sprichwort, auch eine verschlüsselte Rede (vgl. [[JHN.10.6]]). Gegenbegriff ist παρρησία, die offene Rede."),
 ("JHN.16.27", "hat euch lieb", "literal", "φιλεῖ ὑμᾶς", None, ["liebt euch"], "φιλέω wie in [[JHN.15.19]]; siehe dort."),
 ("JHN.16.31", "Jetzt glaubt ihr?", "interpretive", "Ἄρτι πιστεύετε;", None, ["Jetzt glaubt ihr!", "Glaubt ihr jetzt?"], "Der SBLGNT setzt ein Fragezeichen. Ohne Satzzeichen kann es auch eine Feststellung sein. [[JHN.16.32]] spricht von der bevorstehenden Zerstreuung."),
 ("JHN.16.32", "jeder zu dem Seinen", "literal", "ἕκαστος εἰς τὰ ἴδια", None, ["jeder nach Hause"], "τὰ ἴδια «das Eigene» kann das eigene Zuhause oder die eigenen Angelegenheiten meinen."),
 ("JHN.16.33", "überwunden", "literal", "νενίκηκα", None, ["besiegt"], "Perfekt: der Sieg ist erreicht und gilt fort."),
 ("JHN.17.1", "die Stunde ist gekommen", "literal", "ἐλήλυθεν ἡ ὥρα", None, None, "«Die Stunde» Jesu durchzieht das Evangelium (vgl. [[JHN.2.4]], [[JHN.12.23]], [[JHN.13.1]])."),
 ("JHN.17.2", "über alles Fleisch", "literal", "πάσης σαρκός", None, ["über alle Menschen"], "«Alles Fleisch» ist eine biblische Wendung für alle Menschen bzw. alles Lebendige."),
 ("JHN.17.2", "allen, die", "adapted", "πᾶν ὃ", "allem, was", None, "Johannes spricht von den Jüngern als sächlicher Gesamtheit (πᾶν ὅ «alles, was»; ebenso ὅ in [[JHN.17.24]]) und nimmt sie dann mit dem männlichen αὐτοῖς auf."),
 ("JHN.17.3", "erkennen", "literal", "γινώσκωσι", None, ["kennen"], "γινώσκω meint hier nicht blosses Wissen, sondern eine lebendige Beziehung."),
 ("JHN.17.11", "Heiliger Vater", "literal", "πάτερ ἅγιε", None, None, "Die Anrede steht nur hier im Neuen Testament; vgl. «Gerechter Vater» [[JHN.17.25]]."),
 ("JHN.17.11", "bewahre", "literal", "τήρησον", None, ["behüte"], "τηρέω ist mit Geboten und Wort als «halten» übersetzt ([[JHN.14.15]], [[JHN.15.10]], [[JHN.17.6]]), mit Personen als «bewahren» ([[JHN.17.12]], [[JHN.17.15]]). φυλάσσω in [[JHN.17.12]] heisst «behüten»."),
 ("JHN.17.12", "Sohn des Verderbens", "literal", "ὁ υἱὸς τῆς ἀπωλείας", None, ["der Verlorene", "der zum Verderben Bestimmte"], "Semitische Wendung: einer, der zum Verderben gehört. Im Griechischen klingt ἀπώλετο «ist verloren gegangen» an (gleicher Stamm); das Deutsche kann das Wortspiel nicht nachbilden. Gemeint ist nach dem Zusammenhang Judas (vgl. [[JHN.13.18]]); der Text nennt ihn nicht. Dieselbe Wendung in [[2TH.2.3]]."),
 ("JHN.17.15", "vor dem Bösen", "interpretive", "ἐκ τοῦ πονηροῦ", None, ["vor dem Übel", "vor dem Bösen (dem Teufel)"], "τοῦ πονηροῦ kann männlich («der Böse») oder sächlich («das Böse») sein. Im johanneischen Schrifttum ist meist der Böse gemeint (vgl. [[1JN.2.13]]–[[1JN.2.14]], [[1JN.5.18]]–[[1JN.5.19]]); «dem Bösen» lässt beides offen."),
 ("JHN.17.17", "Heilige sie", "literal", "ἁγίασον αὐτοὺς", None, ["Weihe sie", "Sondere sie aus"], "ἁγιάζω heisst «heilig machen, für Gott aussondern»; in [[JHN.17.19]] heiligt Jesus sich selbst. Das Wort gehört auch zur Sprache des Opfers und der Priesterweihe (vgl. [[EXO.28.41]]); ob es hier so gemeint ist, wird verschieden beurteilt."),
 ("JHN.17.21", "eins", "literal", "ἓν", None, ["eine Einheit"], "ἕν ist sächlich: «eins», nicht «einer». So auch [[JHN.17.11]], [[JHN.17.22]] und [[JHN.17.23]] («zur Einheit», εἰς ἕν)."),
 ("JHN.17.23", "vollendet sind zur Einheit", "literal", "ὦσιν τετελειωμένοι εἰς ἕν", None, ["vollkommen eins sind"], "τελειόω «vollenden, zum Ziel bringen»; dasselbe Verb wie in [[JHN.17.4]] («das Werk vollendet»)."),
 ("JHN.17.24", "Vater, was du mir gegeben hast", "literal", "πάτερ, ὃ δέδωκάς μοι", None, ["Vater, die du mir gegeben hast"], "Sächlich wie in [[JHN.17.2]]; danach geht der Satz mit «jene» weiter. Zur Lesart οὕς «die» siehe die Alternative."),
]

DEC_GSW = [
 ("JHN.14.1", "Glaubed a Gott", "interpretive", "πιστεύετε εἰς τὸν θεόν", None, ["Ir glaubed a Gott"], "πιστεύετε cha Befähl oder Feschtstellig sii, beidi Mal. Übersetzt isch zweimal als Befähl, wil de Vers mit ere Ufforderig aafangt."),
 ("JHN.14.2", "Wonige", "literal", "μοναὶ", "Bliibine", ["Rüüm"], "μονή isch s Hauptwort zu μένω «bliibe»: en Ort, wo me bliibt. S gliich Wort staat i [[JHN.14.23]]."),
 ("JHN.14.2", "hett ich eu dänn gseit", "interpretive", "εἶπον ἂν ὑμῖν ὅτι", "hett ich eu gseit, dass", ["hett ich s eu gseit; dänn ich gang", "hett ich eu gseit: Ich gang"], "De Satz isch mehrdüütig. De SBLGNT setzt keis Fragezeiche; d Frag isch e redaktionelli Entscheidig."),
 ("JHN.14.6", "Ich bin de Wäg", "literal", "Ἐγώ εἰμι ἡ ὁδὸς", None, None, "Eis vo de Ich-bin-Wort (vgl. [[JHN.6.35]], [[JHN.8.12]], [[JHN.10.11]], [[JHN.11.25]], [[JHN.15.1]]). Grundentscheid: lueg scripts/authoring/johannes_text_01_03.py."),
 ("JHN.14.12", "Amen, amen, ich säge eu", "literal", "ἀμὴν ἀμὴν λέγω ὑμῖν", None, None, "S doppelt Amen staat nu bim Johannes; es leitet e fiirlichi Uussag ii."),
 ("JHN.14.16", "Biistand", "interpretive", "παράκλητον", "dä, wo me härerüeft", ["Fürspräch", "Aawalt", "Tröschter", "Hälfer", "Paraklet"], "παράκλητος isch dä, wo me herrüeft, bsunders de Biistand vor Gricht. I [[1JN.2.1]] isch Jesus de Fürspräch bim Vatter; da isch es de Geischt, «en andere» Biistand. Überall «Biistand» ([[JHN.14.26]], [[JHN.15.26]], [[JHN.16.7]])."),
 ("JHN.14.17", "bliibt", "literal", "μένει", None, ["wohnt"], "μένω isch überall mit «bliibe» widergää, demit s Leitwort sichtbar bliibt (i Kapitel 14–17 14-mal nach MACULA-Lemma, elfmal i [[JHN.15.4]]–[[JHN.15.16]])."),
 ("JHN.14.17", "Wält", "literal", "κόσμος", None, None, "κόσμος isch überall «Wält»; oft isch d Mänschewält gmeint, wo sich Gott verschlüüsst."),
 ("JHN.14.23", "nämed bi ihm Wonig", "adapted", "μονὴν ποιησόμεθα", "mached e Bliibi", None, "μονή wie i [[JHN.14.2]]."),
 ("JHN.14.27", "Fride loo ich eu zrugg", "literal", "εἰρήνην ἀφίημι ὑμῖν", None, None, "Wie en Abschiedsgruess."),
 ("JHN.14.30", "de Herrscher vo de Wält", "literal", "ὁ τοῦ κόσμου ἄρχων", None, ["de Fürscht vo de Wält"], "Gmeint isch de Gägespiler vo Gott (vgl. [[JHN.12.31]], [[JHN.16.11]])."),
 ("JHN.14.30", "a mir hät er nüüt", "literal", "ἐν ἐμοὶ οὐκ ἔχει οὐδέν", "in mir hät er nüüt", ["über mich hät er kei Macht"], "Churz und offe: kei Aahaltspunkt oder kei Aaspruch a Jesus."),
 ("JHN.15.1", "de wahr Wiistock", "literal", "ἡ ἄμπελος ἡ ἀληθινή", None, ["d wahr Räbe"], "ἄμπελος isch di ganz Wiipflanze, κλῆμα de einzel Trieb («Schoss»). Uf Züritüütsch meint «Räbe» oft di ganz Pflanze; drum «Wiistock» und «Schoss». Wiistock oder Wiiberg sind i de Schrifte vo Israel es Bild für Israel ([[PSA.80.8]]–[[PSA.80.16]], [[ISA.5.1]]–[[ISA.5.7]], [[JER.2.21]])."),
 ("JHN.15.1", "Wiibuur", "adapted", "γεωργός", "Buur", ["Winzer"], None),
 ("JHN.15.2", "nimmt er wäg", "literal", "αἴρει", None, ["hebt er uf"], "αἴρω heisst «wägnää» und «ufhebe»; meistens verstande als Wägnää vom Schoss ohni Frucht (vgl. [[JHN.15.6]])."),
 ("JHN.15.2", "macht er suuber", "literal", "καθαίρει", None, ["schniidt er zrugg"], "Im Wiibau isch s Zruggschniide gmeint. S Wort spilt mit καθαροί «suuber» i [[JHN.15.3]]."),
 ("JHN.15.13", "sis Läbe hergit", "adapted", "τὴν ψυχὴν αὐτοῦ θῇ", "sini Seel aneleit", None, "Gliich wie bim guete Hirt ([[JHN.10.11]])."),
 ("JHN.15.15", "Chnächt", "traditional", "δούλους", None, ["Sklave", "Diener"], "δοῦλος isch de unfrei Diener; «Chnächt» nimmt s Wort us [[JHN.13.16]] uf."),
 ("JHN.15.19", "gern ha", "literal", "ἐφίλει", None, ["liebe"], "Für φιλέω staat «gern ha», für ἀγαπάω «liebe» (au [[JHN.16.27]]). Öb de Johannes di zwei Verbe unterscheidet, isch umstritte."),
 ("JHN.16.2", "Us de Synagoge wärded si eu usschlüüsse", "adapted", "ἀποσυναγώγους ποιήσουσιν", None, None, "ἀποσυνάγωγος staat nu bim Johannes ([[JHN.9.22]], [[JHN.12.42]]). Was gschichtlich dehinder staat, wird i de Forschig verschide beurteilt."),
 ("JHN.16.8", "überfüere", "interpretive", "ἐλέγξει", None, ["ufdecke", "zrächtwiise"], "ἐλέγχω heisst «überfüere, ufdecke, zrächtwiise». Mit περί («wäge») isch offe, öb de Geischt d Wält überfüert oder ere zeigt, was Sünd, Grächtigkeit und Gricht würkli sind."),
 ("JHN.16.13", "i de ganze Wahrheit füere", "literal", "ὁδηγήσει ἐν τῇ ἀληθείᾳ πάσῃ", None, ["i di ganz Wahrheit füere"], "Lueg d Alternative."),
 ("JHN.16.23", "fröge", "interpretive", "ἐρωτήσετε", None, ["bitte"], "ἐρωτάω heisst «fröge» und «bitte»; da «fröge» wäge [[JHN.16.19]]."),
 ("JHN.16.25", "Bildwort", "interpretive", "παροιμίαις", None, ["Rätselwort", "Glichnis"], "παροιμία isch es Bildwort oder e verschlüsseleti Red (vgl. [[JHN.10.6]]); s Gägeteil isch di offe Red (παρρησία)."),
 ("JHN.16.27", "hät eu gern", "literal", "φιλεῖ ὑμᾶς", None, ["liebt eu"], "φιλέω wie i [[JHN.15.19]]."),
 ("JHN.17.2", "über alles Fleisch", "literal", "πάσης σαρκός", None, ["über alli Mänsche"], "Biblischi Wändig für alli Mänsche."),
 ("JHN.17.11", "bhüet", "literal", "τήρησον", None, ["bewahr"], "τηρέω isch mit Gebot und Wort «halte», mit Persone «bhüete»; φυλάσσω i [[JHN.17.12]] «ufpasse»."),
 ("JHN.17.12", "Sohn vom Verderbe", "literal", "ὁ υἱὸς τῆς ἀπωλείας", None, ["de Verloreni"], "Semitischi Wändig: eine, wo zum Verderbe ghört. Im Griechische tönt ἀπώλετο «isch verlore gange» aa. Nach em Zämehang isch de Judas gmeint (vgl. [[JHN.13.18]]); de Text nännt en nöd."),
 ("JHN.17.15", "vor em Böse", "interpretive", "ἐκ τοῦ πονηροῦ", None, ["vor em Übel"], "Männlich («de Bös») oder sächlich («s Bös»); «em Böse» laat beides offe."),
]

AZ = "Laut der automatischen Zuordnung"
AZ_G = "Nach de automatische Zueornig"
# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts; nur Erstschrift, Korrekturen eigens genannt.
ALTS = [
 ("VAR-SBLGNTAPP-JHN-014-002-01:R2", "JHN.14.2", "hätte ich euch dann gesagt, dass ich hingehe", "hätte ich es euch gesagt. Ich gehe hin",
  "hett ich eu dänn gseit, dass ich gang", "hett ich s eu gseit. Ich gang", "mittel",
  "Ohne ὅτι liegt die Lesung als Frage fern: «Wenn nicht, hätte ich es euch gesagt.» Danach beginnt ein neuer Satz.",
  "Ohni ὅτι isch e Frag unwahrschiinlich: «Wänn nöd, hett ich s eu gseit.» Dänn fangt en nöie Satz aa.",
  {"R1": [("ὅτι", "dass", "SBLGNT, WH, Treg, NA28")], "R2": [("–", "(fehlt)", "RP")]},
  {"R1": [("ὅτι", "dass", "SBLGNT, WH, Treg, NA28")], "R2": [("–", "(fäält)", "RP")]},
  ["ὅτι kann weggelassen worden sein, weil der Satz mit ihm schwer verständlich ist.",
   AZ + " lesen 01, 02, 03, 04, 05, 032 und 𝔓66 mit ὅτι; 𝔓75 hat hier keinen erhaltenen Text."],
  ["ὅτι cha wäggloo worde sii, wil de Satz mit ihm schwär z verstaa isch.",
   AZ_G + " läsed 01, 02, 03, 04, 05, 032 und 𝔓66 mit ὅτι; 𝔓75 hät da kein erhaltene Text."]),
 ("VAR-SBLGNTAPP-JHN-014-004-01:R2", "JHN.14.4", "dahin kennt ihr den Weg", "wisst ihr, und den Weg kennt ihr",
  "de Wäg dörthii kännt ir", "wüssed ir, und de Wäg kännt ir", "gering",
  "Ziel und Weg werden getrennt genannt.", "Ziil und Wäg wärded tränt gnännt.",
  {"R1": [("τὴν ὁδόν", "den Weg", None)], "R2": [("καὶ τὴν ὁδὸν οἴδατε", "und den Weg kennt ihr", "RP")]},
  {"R1": [("τὴν ὁδόν", "de Wäg", None)], "R2": [("καὶ τὴν ὁδὸν οἴδατε", "und de Wäg kännt ir", "RP")]},
  ["Die längere Form glättet den knappen Satz und bereitet die Frage des Thomas vor, die zwischen Ziel und Weg unterscheidet ([[JHN.14.5]]).",
   AZ + " lesen 01, 03, 04, 032 und die Korrektur in 𝔓66 die kürzere Form, 02, 05 und 𝔓66 (Erstschrift) die längere; 𝔓75 hat hier keinen erhaltenen Text."],
  ["Di länger Form glättet de churz Satz und bereitet d Frag vom Thomas vor ([[JHN.14.5]]).",
   AZ_G + " läsed 01, 03, 04, 032 und d Korrektur in 𝔓66 di chürzer Form, 02, 05 und 𝔓66 (Erstschrift) di länger."]),
 ("VAR-SBLGNTAPP-JHN-014-005-02:R2", "JHN.14.5", "Wie können wir den Weg kennen?", "Wie kennen wir den Weg?",
  "Wie chönd mir de Wäg kenne?", "Wie kenned mir de Wäg?", "gering",
  "Ohne «können».", "Ohni «chönne».",
  {"R1": [("δυνάμεθα τὴν ὁδὸν εἰδέναι", "können wir den Weg kennen", "SBLGNT, NA28, RP")], "R2": [("οἴδαμεν τὴν ὁδόν", "kennen wir den Weg", "WH, Treg")]},
  {"R1": [("δυνάμεθα τὴν ὁδὸν εἰδέναι", "chönd mir de Wäg kenne", "SBLGNT, NA28, RP")], "R2": [("οἴδαμεν τὴν ὁδόν", "kenned mir de Wäg", "WH, Treg")]},
  ["Die kürzere Form wiederholt οἴδαμεν aus dem ersten Satzteil; «können» kann ergänzt oder gestrichen worden sein.",
   AZ + " lesen 02, 032 und 𝔓66 mit «können», 03 und 04 ohne. 01 und 05 lassen sich keiner Lesart zuordnen: nach der CNTR-Transkription hat 01 καὶ πῶς τὴν ὁδὸν εἰδέναι, 05 καὶ πῶς τὴν ὁδὸν οἴδαμεν. 𝔓75 hat hier keinen erhaltenen Text."],
  ["Di chürzer Form widerholt οἴδαμεν; «chönne» cha ergänzt oder gstriche worde sii.",
   AZ_G + " läsed 02, 032 und 𝔓66 mit «chönne», 03 und 04 ohni; 01 und 05 läsed nach de CNTR-Transkription no anders."]),
 ("VAR-SBLGNTAPP-JHN-014-007-02:R3", "JHN.14.7", "würdet ihr auch meinen Vater kennen", "werdet ihr auch meinen Vater erkennen",
  "würded ir au min Vatter kenne", "wärded ir au min Vatter erchänne", "mittel",
  "Mit γνώσεσθε (und ἐγνώκατε im Vordersatz, VAR-SBLGNTAPP-JHN-014-007-01) wird aus dem Vorwurf eine Verheissung: «Wenn ihr mich erkannt habt, werdet ihr auch meinen Vater erkennen.»",
  "Mit γνώσεσθε (und ἐγνώκατε im Vordersatz) wird us em Vorwurf es Verspräche: «Wänn ir mich erchännt händ, wärded ir au min Vatter erchänne.»",
  {"R1": [("ἂν ᾔδειτε", "würdet ihr kennen", "SBLGNT, WH, Treg")], "R2": [("ἐγνώκειτε ἄν", "hättet ihr erkannt", "RP")], "R3": [("γνώσεσθε", "werdet ihr erkennen", "NA28")]},
  {"R1": [("ἂν ᾔδειτε", "würded ir kenne", "SBLGNT, WH, Treg")], "R2": [("ἐγνώκειτε ἄν", "hetted ir erchännt", "RP")], "R3": [("γνώσεσθε", "wärded ir erchänne", "NA28")]},
  ["Der irreale Satz passt zum Vorwurf an Philippus ([[JHN.14.9]]); die Verheissung passt zum folgenden «von jetzt an kennt ihr ihn». Beide Richtungen der Angleichung sind denkbar.",
   AZ + " lesen 03 und 04 ἂν ᾔδειτε, 02 ἐγνώκειτε ἄν, 01, 05, 032 und 𝔓66 γνώσεσθε; 01, 05 und 𝔓66 haben zudem im Vordersatz ἐγνώκατε. 𝔓75 hat hier keinen erhaltenen Text."],
  ["De irreal Satz passt zum Vorwurf a de Philippus ([[JHN.14.9]]), s Verspräche zum «vo jetzt aa kännt ir en». Beides cha aaglichen worde sii.",
   AZ_G + " läsed 03 und 04 ἂν ᾔδειτε, 02 ἐγνώκειτε ἄν, 01, 05, 032 und 𝔓66 γνώσεσθε."]),
 ("VAR-SBLGNTAPP-JHN-014-014-01:R2", "JHN.14.14", "Wenn ihr mich um etwas bittet", "Wenn ihr um etwas bittet",
  "Wänn ir mich um öppis bittet", "Wänn ir um öppis bittet", "gering",
  "Ohne «mich» ist die Bitte nicht ausdrücklich an Jesus gerichtet.", "Ohni «mich» gaat d Bitt nöd usdrücklich a Jesus.",
  {"R1": [("με", "mich", "SBLGNT, WH, NA28, RP")], "R2": [("–", "(fehlt)", "Treg")]},
  {"R1": [("με", "mich", "SBLGNT, WH, NA28, RP")], "R2": [("–", "(fäält)", "Treg")]},
  ["«mich» kann gestrichen worden sein, weil sonst der Vater gebeten wird ([[JHN.15.16]], [[JHN.16.23]]); es kann auch ergänzt worden sein.",
   AZ + " lesen 01, 03, 032, 𝔓66 und 𝔓75 mit «mich», 02 und 05 ohne; 04 hat hier keinen erhaltenen Text."],
  ["«mich» cha gstriche worde sii, wil suscht de Vatter bätte wird ([[JHN.15.16]], [[JHN.16.23]]).",
   AZ_G + " läsed 01, 03, 032, 𝔓66 und 𝔓75 mit «mich», 02 und 05 ohni."]),
 ("VAR-SBLGNTAPP-JHN-014-015-01:R2", "JHN.14.15", "werdet ihr meine Gebote halten", "so haltet meine Gebote",
  "wärded ir mini Gebot halte", "dänn halted mini Gebot", "gering",
  "Imperativ statt Futur.", "Befähl statt Zuekunft.",
  {"R1": [("τηρήσετε", "werdet halten", None)], "R2": [("τηρήσατε", "haltet", "RP")]},
  {"R1": [("τηρήσετε", "wärded halte", None)], "R2": [("τηρήσατε", "halted", "RP")]},
  ["Die Formen unterscheiden sich nur in einem Vokal und wurden leicht verwechselt.",
   AZ + " lesen 03 und 𝔓75 das Futur, 02, 05 und 032 den Imperativ; bei 01 und 𝔓66 ist die Zuordnung unklar, 04 hat hier keinen erhaltenen Text."],
  ["D Forme underscheided sich nu i eim Vokal.",
   AZ_G + " läsed 03 und 𝔓75 d Zuekunft, 02, 05 und 032 de Befähl; bi 01 und 𝔓66 isch d Zueornig unklar."]),
 ("VAR-SBLGNTAPP-JHN-014-016-01:R3", "JHN.14.16", "damit er bei euch sei in Ewigkeit", "damit er bei euch bleibe in Ewigkeit",
  "demit er bi eu isch in Ewigkeit", "demit er bi eu bliibt in Ewigkeit", "gering",
  "Mit dem Leitwort «bleiben» (vgl. [[JHN.14.17]]).", "Mit em Leitwort «bliibe» (vgl. [[JHN.14.17]]).",
  {"R1": [("ᾖ μεθʼ ὑμῶν", "bei euch sei", "SBLGNT, WH, Treg")], "R2": [("μεθʼ ὑμῶν … ᾖ", "bei euch … sei (ᾖ am Satzende)", "NA28")], "R3": [("μένῃ μεθʼ ὑμῶν", "bei euch bleibe", "RP")]},
  {"R1": [("ᾖ μεθʼ ὑμῶν", "bi eu isch", "SBLGNT, WH, Treg")], "R2": [("μεθʼ ὑμῶν … ᾖ", "bi eu … isch (am Satzänd)", "NA28")], "R3": [("μένῃ μεθʼ ὑμῶν", "bi eu bliibt", "RP")]},
  ["μένῃ kann aus dem folgenden μένει eingetragen sein; die schwankende Stellung von ᾖ spricht dafür, dass das Verb früh unsicher war.",
   AZ + " lesen 02, 05, 032 und 𝔓66 μένῃ. 01, 03 und 𝔓75 haben ᾖ nicht an der SBLGNT-Stelle: nach der CNTR-Transkription steht es in 01 nach μεθʼ ὑμῶν, in 03 und 𝔓75 am Satzende (VAR-SBLGNTAPP-JHN-014-016-02). 04 hat hier keinen erhaltenen Text."],
  ["μένῃ cha us em folgende μένει iitreit sii.",
   AZ_G + " läsed 02, 05, 032 und 𝔓66 μένῃ; 01, 03 und 𝔓75 händ ᾖ a andere Stelle."]),
 ("VAR-SBLGNTAPP-JHN-014-017-03:R2", "JHN.14.17", "in euch sein wird", "in euch ist",
  "in eu sii wird", "in eu isch", "gering",
  "Präsens statt Futur.", "Gägewart statt Zuekunft.",
  {"R1": [("ἔσται", "wird sein", "SBLGNT, NA28, RP")], "R2": [("ἐστίν", "ist", "WH, Treg")]},
  {"R1": [("ἔσται", "wird sii", "SBLGNT, NA28, RP")], "R2": [("ἐστίν", "isch", "WH, Treg")]},
  ["Das Präsens kann an μένει angeglichen sein, das Futur an die Verheissung des Kommens.",
   AZ + " lesen 01, 02 und die Korrektur in 𝔓66 das Futur, 03, 05, 032, 𝔓66 (Erstschrift) und 𝔓75 das Präsens; 04 hat hier keinen erhaltenen Text."],
  ["D Gägewart cha a μένει aaglichen sii, d Zuekunft as Verspräche.",
   AZ_G + " läsed 01, 02 und d Korrektur in 𝔓66 d Zuekunft, 03, 05, 032, 𝔓66 und 𝔓75 d Gägewart."]),
 ("VAR-SBLGNTAPP-JHN-015-007-01:R2", "JHN.15.7", "darum bittet", "darum werdet ihr bitten",
  "bitted drum", "wärded ir drum bitte", "gering",
  "Futur statt Imperativ.", "Zuekunft statt Befähl.",
  {"R1": [("αἰτήσασθε", "bittet", None)], "R2": [("αἰτήσεσθε", "werdet ihr bitten", "RP")]},
  {"R1": [("αἰτήσασθε", "bitted", None)], "R2": [("αἰτήσεσθε", "wärded ir bitte", "RP")]},
  ["Die beiden Formen klangen in der Aussprache der Zeit gleich und wurden leicht verwechselt.",
   AZ + " lesen 02, 03, 05, 𝔓66 und 𝔓75 den Imperativ, 01 das Futur; 𝔓22 hat hier keinen erhaltenen Text."],
  ["Di beide Forme händ dazmal gliich tönt.", AZ_G + " läsed 02, 03, 05, 𝔓66 und 𝔓75 de Befähl, 01 d Zuekunft."]),
 ("VAR-SBLGNTAPP-JHN-015-008-01:R2", "JHN.15.8", "und meine Jünger werdet", "– und ihr werdet meine Jünger werden",
  "und mini Jünger wärded", "– und ir wärded mini Jünger wärde", "gering",
  "Das Jüngerwerden wird zur Folge statt zum Inhalt der Verherrlichung.", "S Jüngerwärde isch d Folg statt de Inhalt.",
  {"R1": [("γένησθε", "werdet (dass ihr … werdet)", None)], "R2": [("γενήσεσθε", "ihr werdet werden", "RP")]},
  {"R1": [("γένησθε", "(dass ir …) wärded", None)], "R2": [("γενήσεσθε", "ir wärded wärde", "RP")]},
  ["Konjunktiv und Futur unterscheiden sich wenig und wurden leicht verwechselt.",
   AZ + " lesen 03, 05, 𝔓66 und 𝔓75 den Konjunktiv, 01 und 02 das Futur; 𝔓22 hat hier keinen erhaltenen Text."],
  ["D Forme underscheided sich wenig.", AZ_G + " läsed 03, 05, 𝔓66 und 𝔓75 γένησθε, 01 und 02 γενήσεσθε."]),
 ("VAR-SBLGNTAPP-JHN-015-011-01:R2", "JHN.15.11", "in euch ist", "in euch bleibt",
  "in eu isch", "in eu bliibt", "gering",
  "Mit dem Leitwort «bleiben».", "Mit em Leitwort «bliibe».",
  {"R1": [("ᾖ", "ist", None)], "R2": [("μείνῃ", "bleibt", "RP")]},
  {"R1": [("ᾖ", "isch", None)], "R2": [("μείνῃ", "bliibt", "RP")]},
  ["μείνῃ kann aus der Umgebung ([[JHN.15.4]]–[[JHN.15.10]]) eingetragen sein.",
   AZ + " lesen 02, 03, 05 und 𝔓66 ᾖ, 01 μείνῃ; 𝔓22 und 𝔓75 haben hier keinen erhaltenen Text."],
  ["μείνῃ cha us de Umgäbig iitreit sii.", AZ_G + " läsed 02, 03, 05 und 𝔓66 ᾖ, 01 μείνῃ."]),
 ("VAR-SBLGNTAPP-JHN-015-018-01:R2", "JHN.15.18", "mich vor euch gehasst", "mich zuerst gehasst",
  "mich vor eu ghasst", "mich zerscht ghasst", "gering",
  "Ohne «euch»: πρῶτον heisst dann einfach «zuerst».", "Ohni «eu» heisst πρῶτον eifach «zerscht».",
  {"R1": [("πρῶτον ὑμῶν", "vor euch", "SBLGNT, WH, Treg, NA28, RP")], "R2": [("πρῶτον", "zuerst", "NIV")]},
  {"R1": [("πρῶτον ὑμῶν", "vor eu", "SBLGNT, WH, Treg, NA28, RP")], "R2": [("πρῶτον", "zerscht", "NIV")]},
  ["ὑμῶν kann wegen der ungewohnten Verbindung mit πρῶτον ausgefallen oder gestrichen worden sein.",
   AZ + " lesen 02, 03 und 𝔓66 mit ὑμῶν, 01 und 05 ohne; 𝔓22 und 𝔓75 haben hier keinen erhaltenen Text."],
  ["ὑμῶν cha wäg de ungwonte Verbindig mit πρῶτον usgfalle sii.", AZ_G + " läsed 02, 03 und 𝔓66 mit ὑμῶν, 01 und 05 ohni."]),
 ("VAR-SBLGNTAPP-JHN-016-013-01:R2", "JHN.16.13", "in der ganzen Wahrheit leiten", "in die ganze Wahrheit leiten",
  "i de ganze Wahrheit füere", "i di ganz Wahrheit füere", "gering",
  "Mit εἰς führt der Geist in die Wahrheit hinein; mit ἐν leitet er innerhalb der Wahrheit. Hier folgt der SBLGNT NA28 gegen WH und Treg.",
  "Mit εἰς füert de Geischt i d Wahrheit ine; mit ἐν füert er i de Wahrheit. Da folgt de SBLGNT em NA28.",
  {"R1": [("ἐν τῇ ἀληθείᾳ πάσῃ", "in der ganzen Wahrheit", "SBLGNT, NA28")], "R2": [("εἰς τὴν ἀλήθειαν πᾶσαν", "in die ganze Wahrheit", "WH, Treg")], "R3": [("εἰς πᾶσαν τὴν ἀλήθειαν", "in alle Wahrheit", "RP")]},
  {"R1": [("ἐν τῇ ἀληθείᾳ πάσῃ", "i de ganze Wahrheit", "SBLGNT, NA28")], "R2": [("εἰς τὴν ἀλήθειαν πᾶσαν", "i di ganz Wahrheit", "WH, Treg")], "R3": [("εἰς πᾶσαν τὴν ἀλήθειαν", "i alli Wahrheit", "RP")]},
  ["ἐν und εἰς gehen in der Koine ineinander über; nach ὁδηγέω erwartet man eher εἰς, was die Änderung in beide Richtungen erklären kann.",
   AZ + " lesen 01, 05, 032 und 𝔓66 ἐν τῇ ἀληθείᾳ πάσῃ, 02 und 03 εἰς τὴν ἀλήθειαν πᾶσαν; 04, 𝔓5 und 𝔓22 haben hier keinen erhaltenen Text."],
  ["ἐν und εἰς gönd i de Koine inenand über.", AZ_G + " läsed 01, 05, 032 und 𝔓66 ἐν, 02 und 03 εἰς."]),
 ("VAR-SBLGNTAPP-JHN-016-013-02:R2", "JHN.16.13", "was er hören wird", "was er hört",
  "was er ghöre wird", "was er ghört", "gering",
  "Präsens statt Futur; RP: «was immer er hört».", "Gägewart statt Zuekunft; RP: «was er immer ghört».",
  {"R1": [("ἀκούσει", "er wird hören", "SBLGNT, Treg, NA28")], "R2": [("ἀκούει", "er hört", "WH")], "R3": [("ἂν ἀκούσῃ", "er (immer) hört", "RP")]},
  {"R1": [("ἀκούσει", "er wird ghöre", "SBLGNT, Treg, NA28")], "R2": [("ἀκούει", "er ghört", "WH")], "R3": [("ἂν ἀκούσῃ", "er (immer) ghört", "RP")]},
  ["Die Formen sind leicht anzugleichen, an das Futur der Umgebung oder an ein zeitloses Präsens.",
   AZ + " lesen 03, 05, 032 und 𝔓66 das Futur, 01 das Präsens, 02 ἂν ἀκούσῃ; 04, 𝔓5 und 𝔓22 haben hier keinen erhaltenen Text."],
  ["D Forme sind liecht aazglieche.", AZ_G + " läsed 03, 05, 032 und 𝔓66 d Zuekunft, 01 d Gägewart, 02 ἂν ἀκούσῃ."]),
 ("VAR-SBLGNTAPP-JHN-016-016-02:R2", "JHN.16.16", "und ihr werdet mich sehen", "und ihr werdet mich sehen, denn ich gehe zum Vater",
  "und ir wärded mich gseh", "und ir wärded mich gseh, dänn ich gang zum Vatter", "gering",
  "Mit Zusatz am Versende.", "Mit Zuesatz am Versänd.",
  {"R1": [("με", "mich", None)], "R2": [("με ὅτι ὑπάγω πρὸς τὸν πατέρα", "mich, denn ich gehe zum Vater", "RP")]},
  {"R1": [("με", "mich", None)], "R2": [("με ὅτι ὑπάγω πρὸς τὸν πατέρα", "mich, dänn ich gang zum Vatter", "RP")]},
  ["Der Zusatz kann aus [[JHN.16.17]] stammen, wo die Jünger die Worte «ich gehe zum Vater» zitieren (gesagt in [[JHN.16.10]]).",
   AZ + " lesen 01, 03, 05, 032, 𝔓5 und 𝔓66 ohne den Zusatz, 02 mit ihm; 04 und 𝔓22 haben hier keinen erhaltenen Text."],
  ["De Zuesatz cha us [[JHN.16.17]] stamme.", AZ_G + " läsed 01, 03, 05, 032, 𝔓5 und 𝔓66 ohni Zuesatz, 02 mit."]),
 ("VAR-SBLGNTAPP-JHN-016-022-02:R2", "JHN.16.22", "nimmt niemand von euch", "wird niemand von euch nehmen",
  "nimmt niemer vo eu wäg", "wird niemer vo eu wägnää", "gering",
  "Futur statt Präsens.", "Zuekunft statt Gägewart.",
  {"R1": [("αἴρει", "nimmt", "SBLGNT, NA28, RP")], "R2": [("ἀρεῖ", "wird nehmen", "WH, Treg")]},
  {"R1": [("αἴρει", "nimmt wäg", "SBLGNT, NA28, RP")], "R2": [("ἀρεῖ", "wird wägnää", "WH, Treg")]},
  ["Die Formen unterscheiden sich nur in der Betonung bzw. einem Buchstaben; das Futur passt zu den Futurformen der Umgebung.",
   AZ + " lesen 01, 02, 04, 𝔓22, 𝔓66 und die Korrektur in 05 das Präsens, 03, 05 (Erstschrift) und 𝔓5 das Futur; 032 lässt sich keiner Lesart zuordnen."],
  ["D Forme underscheided sich chuum.", AZ_G + " läsed 01, 02, 04, 𝔓22 und 𝔓66 d Gägewart, 03, 05 (Erstschrift) und 𝔓5 d Zuekunft."]),
 ("VAR-SBLGNTAPP-JHN-016-023-02:R2", "JHN.16.23", "Wenn ihr den Vater um etwas bittet, wird er es euch in meinem Namen geben", "Wenn ihr den Vater in meinem Namen um etwas bittet, wird er es euch geben",
  "Wänn ir de Vatter um öppis bittet, wird er s eu i mim Name gää", "Wänn ir de Vatter i mim Name um öppis bittet, wird er s eu gää", "mittel",
  "Die Wortstellung entscheidet, ob «in meinem Namen» zum Geben oder zum Bitten gehört. Der SBLGNT folgt hier WH und Treg gegen NA28 und RP.",
  "D Wortstellig entscheidet, öb «i mim Name» zum Gää oder zum Bitte ghört. De SBLGNT folgt da WH und Treg.",
  {"R1": [("δώσει ὑμῖν ἐν τῷ ὀνόματί μου", "wird er euch in meinem Namen geben", "SBLGNT, WH, Treg")], "R2": [("ἐν τῷ ὀνόματί μου δώσει ὑμῖν", "in meinem Namen … wird er euch geben", "NA28, RP")]},
  {"R1": [("δώσει ὑμῖν ἐν τῷ ὀνόματί μου", "wird er eu i mim Name gää", "SBLGNT, WH, Treg")], "R2": [("ἐν τῷ ὀνόματί μου δώσει ὑμῖν", "i mim Name … wird er eu gää", "NA28, RP")]},
  ["Sonst steht «in meinem Namen» beim Bitten ([[JHN.14.13]], [[JHN.15.16]], [[JHN.16.24]], [[JHN.16.26]]); Abschreiber können die Stellung daran angeglichen haben, oder die ungewöhnliche Stellung ist durch Umstellung entstanden.",
   AZ + " lesen 01, 03, 04 und 𝔓5 wie der SBLGNT, 02, 05, 032, 𝔓22 und 𝔓66 die andere Stellung."],
  ["Suscht staat «i mim Name» bim Bitte ([[JHN.14.13]], [[JHN.15.16]], [[JHN.16.24]]).", AZ_G + " läsed 01, 03, 04 und 𝔓5 wie de SBLGNT, 02, 05, 032, 𝔓22 und 𝔓66 di ander Stellig."]),
 ("VAR-SBLGNTAPP-JHN-016-027-01:R2", "JHN.16.27", "von Gott ausgegangen", "vom Vater ausgegangen",
  "vo Gott usgange", "vom Vatter usgange", "gering",
  "«Vater» statt «Gott»; im folgenden Vers steht «vom Vater».", "«Vatter» statt «Gott»; im nächschte Vers staat «vom Vatter».",
  {"R1": [("θεοῦ", "Gott", "SBLGNT, NA28, RP")], "R2": [("πατρὸς", "Vater", "WH, Treg")]},
  {"R1": [("θεοῦ", "Gott", "SBLGNT, NA28, RP")], "R2": [("πατρὸς", "Vatter", "WH, Treg")]},
  ["«Vater» kann an [[JHN.16.28]] angeglichen sein, «Gott» an [[JHN.16.30]].",
   AZ + " lesen 03 und 05 πατρός. Die übrigen Zeugen schreiben die Wörter abgekürzt (Nomina sacra), die die Zuordnung nicht erkennt; nach der CNTR-Transkription steht in 01, 02, 032, 𝔓5, 𝔓22 und 𝔓66 die Kurzform für θεοῦ, in 04 die Kurzform für πατρός."],
  ["«Vatter» cha a [[JHN.16.28]] aaglichen sii, «Gott» a [[JHN.16.30]].",
   AZ_G + " läsed 03 und 05 πατρός; nach de CNTR-Transkription händ 01, 02, 032, 𝔓5, 𝔓22 und 𝔓66 d Churzform für θεοῦ, 04 die für πατρός."]),
 ("VAR-SBLGNTAPP-JHN-017-012-01:R2", "JHN.17.12", "Als ich bei ihnen war", "Als ich bei ihnen in der Welt war",
  "Wo ich bi ine gsii bin", "Wo ich bi ine i de Wält gsii bin", "gering",
  "Mit «in der Welt».", "Mit «i de Wält».",
  {"R1": [("αὐτῶν", "ihnen", None)], "R2": [("αὐτῶν ἐν τῷ κόσμῳ", "ihnen in der Welt", "RP")]},
  {"R1": [("αὐτῶν", "ine", None)], "R2": [("αὐτῶν ἐν τῷ κόσμῳ", "ine i de Wält", "RP")]},
  ["Der Zusatz kann aus [[JHN.17.11]] stammen.", AZ + " lesen 01, 03, 04, 05, 032 und 𝔓66 ohne den Zusatz, 02 mit ihm."],
  ["De Zuesatz cha us [[JHN.17.11]] stamme.", AZ_G + " läsed 01, 03, 04, 05, 032 und 𝔓66 ohni, 02 mit."]),
 ("VAR-SBLGNTAPP-JHN-017-012-02:R2", "JHN.17.12", "in deinem Namen, den du mir gegeben hast, und ich habe sie behütet", "in deinem Namen; die du mir gegeben hast, habe ich behütet",
  "i dim Name, wo du mir gää häsch, bhüetet, und ich han uf si ufpasst", "i dim Name bhüetet; uf die, wo du mir gää häsch, han ich ufpasst", "mittel",
  "Mit οὕς sind nicht der Name, sondern die Jünger «gegeben»; in RP fehlt zudem καί vor ἐφύλαξα (VAR-SBLGNTAPP-JHN-017-012-03).",
  "Mit οὕς sind nöd de Name, sondern d Jünger «gää»; in RP fäält zuedem καί vor ἐφύλαξα.",
  {"R1": [("ᾧ", "den (Namen)", None)], "R2": [("οὕς", "die (Jünger)", "RP")]},
  {"R1": [("ᾧ", "wo (de Name)", None)], "R2": [("οὕς", "die (Jünger)", "RP")]},
  ["Dass der Vater Jesus seinen Namen gegeben hat, ist ungewöhnlich; οὕς nimmt die geläufige Aussage auf, dass der Vater Jesus die Jünger gegeben hat ([[JHN.17.6]], [[JHN.17.9]]). Umgekehrt kann ᾧ an [[JHN.17.11]] angeglichen sein.",
   AZ + " lesen 01, 03, 04, 032 und die Korrektur in 𝔓66 ᾧ, 02 und 05 οὕς; 𝔓66 (Erstschrift) lässt sich keiner Lesart zuordnen."],
  ["Dass de Vatter em Jesus sin Name gää hät, isch ungwont; οὕς nimmt uf, dass er em d Jünger gää hät ([[JHN.17.6]]).",
   AZ_G + " läsed 01, 03, 04, 032 und d Korrektur in 𝔓66 ᾧ, 02 und 05 οὕς."]),
 ("VAR-SBLGNTAPP-JHN-017-021-02:R2", "JHN.17.21", "in uns sind", "in uns eins sind",
  "in üs sind", "in üs eis sind", "gering",
  "Mit «eins».", "Mit «eis».",
  {"R1": [("ἡμῖν", "in uns", None)], "R2": [("ἡμῖν ἕν", "in uns eins", "RP")]},
  {"R1": [("ἡμῖν", "in üs", None)], "R2": [("ἡμῖν ἕν", "in üs eis", "RP")]},
  ["«eins» kann aus dem ersten Satzteil oder aus [[JHN.17.22]] ergänzt sein.", AZ + " lesen 03, 04, 05, 032 und 𝔓66 ohne «eins», 01 und 02 mit ihm."],
  ["«Eis» cha ergänzt sii.", AZ_G + " läsed 03, 04, 05, 032 und 𝔓66 ohni «eis», 01 und 02 mit."]),
 ("VAR-SBLGNTAPP-JHN-017-024-02:R2", "JHN.17.24", "Vater, was du mir gegeben hast", "Vater, die du mir gegeben hast",
  "Vatter, was du mir gää häsch", "Vatter, die, wo du mir gää häsch", "gering",
  "Männlich-plural statt sächlich; die Jünger als Personen.", "Persone statt sächlich.",
  {"R1": [("ὅ", "was", None)], "R2": [("οὕς", "die", "RP")]},
  {"R1": [("ὅ", "was", None)], "R2": [("οὕς", "die, wo", "RP")]},
  ["Das sächliche ὅ ist die schwierigere Form (vgl. [[JHN.17.2]]) und kann an das folgende κἀκεῖνοι angeglichen worden sein.",
   AZ + " lesen 01, 03, 05, 032, 𝔓66 und 𝔓108 ὅ, 02 und 04 οὕς; 𝔓107 hat hier keinen erhaltenen Text."],
  ["S sächlich ὅ isch di schwärer Form.", AZ_G + " läsed 01, 03, 05, 032, 𝔓66 und 𝔓108 ὅ, 02 und 04 οὕς."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-014-001-031", "JHN.14.1-JHN.14.31", "section", "Der Weg zum Vater und die Verheissung des Beistands",
  ["TU-JHN-014-001-014", "TU-JHN-014-015-026", "TU-JHN-014-027-031"],
  "Jesus spricht zu seinen Jüngern: Im Haus seines Vaters gibt es viele Wohnungen; er geht, um ihnen einen Ort zu bereiten, und wird wiederkommen. Auf die Fragen von Thomas und Philippus sagt er: «Ich bin der Weg und die Wahrheit und das Leben»; wer ihn gesehen hat, hat den Vater gesehen. Wer ihn liebt, hält seine Gebote. Er wird den Vater bitten, und dieser wird ihnen einen anderen Beistand geben, den Geist der Wahrheit, der sie alles lehren und an alles erinnern wird, was er gesagt hat. Er hinterlässt ihnen seinen Frieden, kündigt das Kommen des Herrschers der Welt an und fordert zum Aufbruch auf.",
  SEG + " Die Rede setzt die in Kapitel 13 begonnene Rede fort."),
 ("TU-JHN-014-001-014", "JHN.14.1-JHN.14.14", "discourse", "Der Weg zum Vater", None,
  "Jesus sagt den Jüngern, ihr Herz solle nicht erschüttert sein: Im Haus seines Vaters gibt es viele Wohnungen; er geht, um ihnen einen Ort zu bereiten, und wird wiederkommen und sie zu sich nehmen. Thomas fragt nach dem Weg; Jesus antwortet: «Ich bin der Weg und die Wahrheit und das Leben.» Philippus bittet, den Vater zu sehen; Jesus antwortet, wer ihn gesehen habe, habe den Vater gesehen, er sei im Vater und der Vater in ihm. Wer an ihn glaubt, wird die Werke tun, die er tut, und grössere; was sie in seinem Namen erbitten, wird er tun.", None),
 ("TU-JHN-014-015-026", "JHN.14.15-JHN.14.26", "discourse", "Die Verheissung des Beistands", None,
  "Wer Jesus liebt, wird seine Gebote halten. Jesus wird den Vater bitten, und der Vater wird ihnen einen anderen Beistand geben, den Geist der Wahrheit, den die Welt nicht empfangen kann. Er lässt sie nicht als Waisen zurück; die Welt wird ihn nicht mehr sehen, sie aber sehen ihn. Judas (nicht der Iskariot) fragt, warum er sich nur ihnen offenbaren wird; Jesus antwortet, wer ihn liebe, werde sein Wort halten, und er und der Vater würden bei ihm Wohnung nehmen. Der Beistand, der heilige Geist, den der Vater in Jesu Namen senden wird, wird sie alles lehren und an alles erinnern, was Jesus gesagt hat.", None),
 ("TU-JHN-014-027-031", "JHN.14.27-JHN.14.31", "discourse", "Frieden und Aufbruch", None,
  "Jesus hinterlässt den Jüngern seinen Frieden, nicht wie die Welt gibt. Wenn sie ihn liebten, würden sie sich freuen, dass er zum Vater geht, denn der Vater ist grösser als er. Er sagt es voraus, damit sie glauben, wenn es geschieht. Der Herrscher der Welt kommt, hat aber an ihm nichts; die Welt soll erkennen, dass Jesus den Vater liebt und tut, was der Vater ihm geboten hat. Er schliesst: «Steht auf, lasst uns von hier gehen!»", None),
 ("TU-JHN-015-001-027", "JHN.15.1-JHN.15.27", "section", "Weinstock und Reben, Liebe und Hass der Welt",
  ["TU-JHN-015-001-008", "TU-JHN-015-009-017", "TU-JHN-015-018-027"],
  "Jesus nennt sich den wahren Weinstock, den Vater den Weingärtner und die Jünger die Reben: Nur wer in ihm bleibt, bringt Frucht; wer nicht in ihm bleibt, wird hinausgeworfen und verbrannt. Wie der Vater ihn geliebt hat, so hat er sie geliebt; sie sollen in seiner Liebe bleiben und einander lieben, wie er sie geliebt hat. Er nennt sie nicht mehr Knechte, sondern Freunde; er hat sie erwählt, damit sie Frucht bringen. Die Welt wird sie hassen, wie sie ihn gehasst hat; doch der Beistand, den er vom Vater senden wird, wird über ihn Zeugnis ablegen, und auch die Jünger legen Zeugnis ab.",
  SEG + " Die Rede schliesst ohne neue Redeeinleitung an [[JHN.14.31]] an."),
 ("TU-JHN-015-001-008", "JHN.15.1-JHN.15.8", "discourse", "Der wahre Weinstock", None,
  "Jesus ist der wahre Weinstock, sein Vater der Weingärtner. Reben ohne Frucht nimmt der Vater weg, fruchttragende reinigt er. Die Jünger sind schon rein durch das Wort, das Jesus zu ihnen geredet hat. Wie eine Rebe nur am Weinstock Frucht bringt, so bringen sie nur Frucht, wenn sie in ihm bleiben; wer nicht in ihm bleibt, wird hinausgeworfen, verdorrt und wird verbrannt. Bleiben sie in ihm und seine Worte in ihnen, wird ihnen geschehen, worum sie bitten. Der Vater wird verherrlicht, wenn sie viel Frucht bringen und seine Jünger werden.", None),
 ("TU-JHN-015-009-017", "JHN.15.9-JHN.15.17", "discourse", "Bleiben in der Liebe", None,
  "Wie der Vater Jesus geliebt hat, so hat er die Jünger geliebt; sie bleiben in seiner Liebe, wenn sie seine Gebote halten, wie er die Gebote des Vaters gehalten hat. Sein Gebot ist, dass sie einander lieben, wie er sie geliebt hat; keine Liebe ist grösser, als das Leben für die Freunde hinzugeben. Er nennt sie Freunde, nicht mehr Knechte, weil er ihnen alles kundgetan hat, was er vom Vater gehört hat. Nicht sie haben ihn erwählt, sondern er sie, damit sie hingehen, Frucht bringen und ihre Frucht bleibt.", None),
 ("TU-JHN-015-018-027", "JHN.15.18-JHN.15.27", "discourse", "Der Hass der Welt und das Zeugnis", None,
  "Wenn die Welt die Jünger hasst, hat sie Jesus vor ihnen gehasst; weil er sie aus der Welt erwählt hat, sind sie nicht aus der Welt. Wie man ihn verfolgt hat, wird man auch sie verfolgen, um seines Namens willen, weil man den nicht kennt, der ihn gesandt hat. Weil er gekommen ist, geredet und Werke getan hat, haben die Hassenden keine Ausrede für ihre Sünde; so erfüllt sich das Wort: «Sie haben mich ohne Grund gehasst.» Der Beistand, der Geist der Wahrheit, den Jesus vom Vater senden wird, wird über ihn Zeugnis ablegen, und auch die Jünger, die von Anfang an bei ihm sind.", None),
 ("TU-JHN-016-001-033", "JHN.16.1-JHN.16.33", "section", "Verfolgung, Beistand und kommende Freude",
  ["TU-JHN-016-001-004", "TU-JHN-016-005-015", "TU-JHN-016-016-024", "TU-JHN-016-025-033"],
  "Jesus kündigt an, dass man die Jünger aus der Synagoge ausschliessen wird und dass, wer sie tötet, meinen wird, Gott damit einen Dienst darzubringen. Er geht zu dem, der ihn gesandt hat; das ist gut für sie, denn sonst kommt der Beistand nicht. Dieser wird die Welt überführen hinsichtlich der Sünde, der Gerechtigkeit und des Gerichts und die Jünger in der ganzen Wahrheit leiten. Den ratlosen Jüngern sagt er: Eine kleine Weile, und sie sehen ihn nicht mehr, und wieder eine kleine Weile, und sie werden ihn sehen; ihre Trauer wird zur Freude werden wie bei einer Frau nach der Geburt. Die Jünger bekennen, dass er von Gott ausgegangen ist; Jesus sagt voraus, dass sie sich zerstreuen und ihn allein lassen werden, und schliesst: «Ich habe die Welt überwunden.»",
  SEG),
 ("TU-JHN-016-001-004", "JHN.16.1-JHN.16.4", "discourse", "Ankündigung der Verfolgung", None,
  "Jesus sagt den Jüngern, damit sie nicht zu Fall kommen: Man wird sie aus der Synagoge ausschliessen, und es kommt die Stunde, in der jeder, der sie tötet, meinen wird, Gott einen Dienst darzubringen. Das wird geschehen, weil man weder den Vater noch ihn erkannt hat. Er sagt es ihnen, damit sie sich daran erinnern, wenn es eintritt; am Anfang hat er es nicht gesagt, weil er bei ihnen war.", None),
 ("TU-JHN-016-005-015", "JHN.16.5-JHN.16.15", "discourse", "Das Wirken des Beistands", None,
  "Jesus geht zu dem, der ihn gesandt hat; keiner fragt ihn, wohin er geht, die Trauer hat ihr Herz erfüllt. Es ist gut für sie, dass er weggeht, denn sonst kommt der Beistand nicht zu ihnen. Wenn er kommt, wird er die Welt überführen hinsichtlich der Sünde, der Gerechtigkeit und des Gerichts. Als Geist der Wahrheit wird er die Jünger in der ganzen Wahrheit leiten, reden, was er hören wird, ihnen das Kommende verkünden und Jesus verherrlichen, weil er von dem Seinen nimmt.", None),
 ("TU-JHN-016-016-024", "JHN.16.16-JHN.16.24", "discourse", "Trauer wird zu Freude", None,
  "Jesus sagt: «Eine kleine Weile, und ihr seht mich nicht mehr, und wieder eine kleine Weile, und ihr werdet mich sehen.» Die Jünger verstehen es nicht. Jesus kündigt an: Sie werden weinen, während die Welt sich freut, aber ihre Trauer wird zur Freude werden, wie eine Frau nach der Geburt die Bedrängnis vergisst. Er wird sie wiedersehen, und ihre Freude nimmt niemand von ihnen. Was sie den Vater bitten, wird er ihnen in Jesu Namen geben; sie sollen bitten, damit ihre Freude vollkommen ist.", None),
 ("TU-JHN-016-025-033", "JHN.16.25-JHN.16.33", "discourse", "Offene Rede und Überwindung der Welt", None,
  "Jesus kündigt an, er werde nicht mehr in Bildworten, sondern offen vom Vater reden; der Vater selbst hat sie lieb, weil sie Jesus lieb haben und glauben, dass er von Gott ausgegangen ist. Er ist vom Vater ausgegangen und geht zum Vater. Die Jünger sagen, jetzt rede er offen, und sie glauben, dass er von Gott ausgegangen ist. Jesus fragt, ob sie jetzt glauben, und sagt voraus, dass sie sich zerstreuen und ihn allein lassen werden; doch er ist nicht allein, der Vater ist bei ihm. In der Welt haben sie Bedrängnis, aber er hat die Welt überwunden.", None),
 ("TU-JHN-017-001-026", "JHN.17.1-JHN.17.26", "section", "Das Gebet Jesu",
  ["TU-JHN-017-001-005", "TU-JHN-017-006-019", "TU-JHN-017-020-026"],
  "Jesus erhebt die Augen zum Himmel und betet: Die Stunde ist gekommen; der Vater möge den Sohn verherrlichen, damit der Sohn ihn verherrliche. Ewiges Leben ist, den einzigen wahren Gott und den von ihm gesandten Jesus Christus zu erkennen. Er bittet für die Jünger, die der Vater ihm aus der Welt gegeben hat: dass der Vater sie in seinem Namen und vor dem Bösen bewahre und in der Wahrheit heilige; wie der Vater ihn in die Welt gesandt hat, hat er sie in die Welt gesandt. Dann bittet er für alle, die durch ihr Wort glauben: dass alle eins seien, damit die Welt glaube, dass der Vater ihn gesandt hat, und dass sie bei ihm seien und seine Herrlichkeit sehen.",
  SEG),
 ("TU-JHN-017-001-005", "JHN.17.1-JHN.17.5", "prayer", "Bitte um Verherrlichung", None,
  "Jesus betet: Die Stunde ist gekommen. Der Vater möge den Sohn verherrlichen, dem er Vollmacht über alles Fleisch gegeben hat, damit er allen, die der Vater ihm gegeben hat, ewiges Leben gebe; das ewige Leben ist, den einzigen wahren Gott und den von ihm gesandten Jesus Christus zu erkennen. Jesus hat den Vater auf der Erde verherrlicht und das Werk vollendet, das der Vater ihm gegeben hat; nun bittet er um die Herrlichkeit, die er beim Vater hatte, bevor die Welt war.", None),
 ("TU-JHN-017-006-019", "JHN.17.6-JHN.17.19", "prayer", "Fürbitte für die Jünger", None,
  "Jesus hat den Namen des Vaters den Menschen offenbart, die der Vater ihm aus der Welt gegeben hat; sie haben sein Wort gehalten, die Worte Jesu angenommen und glauben, dass der Vater ihn gesandt hat. Für sie bittet er, nicht für die Welt. Er ist nicht mehr in der Welt, sie aber sind in der Welt; der heilige Vater möge sie in seinem Namen bewahren, damit sie eins sind. Solange er bei ihnen war, hat er sie bewahrt, und keiner ist verloren gegangen ausser dem Sohn des Verderbens. Die Welt hat sie gehasst, weil sie nicht aus der Welt sind; er bittet nicht, sie aus der Welt wegzunehmen, sondern sie vor dem Bösen zu bewahren und in der Wahrheit zu heiligen. Wie der Vater ihn gesandt hat, hat er sie in die Welt gesandt, und für sie heiligt er sich selbst.", None),
 ("TU-JHN-017-020-026", "JHN.17.20-JHN.17.26", "prayer", "Fürbitte für die, die durch ihr Wort glauben", None,
  "Jesus bittet auch für die, die durch das Wort der Jünger an ihn glauben: dass alle eins seien, wie der Vater in ihm und er im Vater ist, damit die Welt glaube und erkenne, dass der Vater ihn gesandt und sie geliebt hat, wie er ihn geliebt hat. Er will, dass sie bei ihm sind, wo er ist, und seine Herrlichkeit sehen, die der Vater ihm gegeben hat, weil er ihn vor der Grundlegung der Welt geliebt hat. Die Welt hat den gerechten Vater nicht erkannt, Jesus aber hat ihn erkannt; er hat den Jüngern den Namen des Vaters bekannt gemacht und wird ihn bekannt machen, damit die Liebe des Vaters in ihnen sei und er in ihnen.", None),
]
UNITS_GSW = {
 "TU-JHN-014-001-031": ("De Wäg zum Vatter und s Verspräche vom Biistand", "De Jesus redt zu sine Jünger: Im Huus vo sim Vatter hät s vil Wonige; er gaat, zum ine en Platz parat mache, und chunnt wider. Uf d Frage vom Thomas und vom Philippus seit er: «Ich bin de Wäg und d Wahrheit und s Läbe»; wär ihn gseh hät, hät de Vatter gseh. Wär ihn liebt, haltet sini Gebot. Er wird de Vatter bitte, und dä wird ine en andere Biistand gää, de Geischt vo de Wahrheit, wo si alles leert und si a alles erinneret, won er gseit hät. Er laat ine sin Fride zrugg, seit, dass de Herrscher vo de Wält chunnt, und rüeft zum Ufbruch uf."),
 "TU-JHN-014-001-014": ("De Wäg zum Vatter", "De Jesus seit de Jünger, ires Härz söll nöd erschüttert sii: Im Huus vo sim Vatter hät s vil Wonige; er gaat, zum ine en Platz parat mache, und chunnt wider und nimmt si zu sich. De Thomas fröget nach em Wäg; de Jesus antwortet: «Ich bin de Wäg und d Wahrheit und s Läbe.» De Philippus bittet, de Vatter z gseh; de Jesus antwortet, wär ihn gseh heg, heg de Vatter gseh, er sig im Vatter und de Vatter in ihm. Wär a ihn glaubt, tuet d Wärch, won er tuet, und no grösseri; was si i sim Name bitted, tuet er."),
 "TU-JHN-014-015-026": ("S Verspräche vom Biistand", "Wär de Jesus liebt, wird sini Gebot halte. De Jesus wird de Vatter bitte, und de Vatter wird ine en andere Biistand gää, de Geischt vo de Wahrheit, wo d Wält nöd cha empfange. Er laat si nöd als Waise zrugg; d Wält gseht en nüme, si aber gsehnd en. De Judas (nöd de Iskariot) fröget, werum er sich nu ine offebare wärdi; de Jesus antwortet, wär ihn liebi, haltet sis Wort, und er und de Vatter nämed bi ihm Wonig. De Biistand, de Heilig Geischt, wo de Vatter i sim Name schickt, wird si alles leere und a alles erinnere, wo de Jesus gseit hät."),
 "TU-JHN-014-027-031": ("Fride und Ufbruch", "De Jesus laat de Jünger sin Fride zrugg, nöd wie d Wält git. Wänn si en liebe würded, würded si sich fröie, dass er zum Vatter gaat, wil de Vatter grösser isch als er. Er seit s voruus, demit si glaubed, wänn s passiert. De Herrscher vo de Wält chunnt, hät aber a ihm nüüt; d Wält söll erchänne, dass de Jesus de Vatter liebt und tuet, was ihm de Vatter befole hät. Er schlüüsst: «Stönd uf, mir gönd vo da furt!»"),
 "TU-JHN-015-001-027": ("Wiistock und Schoss, Liebi und Hass vo de Wält", "De Jesus nännt sich de wahr Wiistock, de Vatter de Wiibuur und d Jünger d Schoss: Nu wär in ihm bliibt, bringt Frucht; wär nöd in ihm bliibt, wird usegworfe und verbrännt. Wie de Vatter ihn gliebt hät, so hät er si gliebt; si söled i sinere Liebi bliibe und enand liebe, wie er si gliebt hät. Er nännt si nüme Chnächt, sondern Fründe; er hät si usgwählt, demit si Frucht bringed. D Wält wird si hasse, wie si ihn ghasst hät; aber de Biistand, won er vom Vatter schickt, wird über ihn Züügnis ablegge, und au d Jünger legged Züügnis ab."),
 "TU-JHN-015-001-008": ("De wahr Wiistock", "De Jesus isch de wahr Wiistock, sin Vatter de Wiibuur. Schoss ohni Frucht nimmt de Vatter wäg, die mit Frucht macht er suuber. D Jünger sind scho suuber dur s Wort, wo de Jesus zu ine gredt hät. Wie en Schoss nu am Wiistock Frucht bringt, so bringed si nu Frucht, wänn si in ihm bliibed; wär nöd in ihm bliibt, wird usegworfe, verdoret und wird verbrännt. Bliibed si in ihm und sini Wort in ine, gschiet ine, um was si bitted. De Vatter wird verherrlicht, wänn si vil Frucht bringed und sini Jünger wärded."),
 "TU-JHN-015-009-017": ("Bliibe i de Liebi", "Wie de Vatter de Jesus gliebt hät, so hät er d Jünger gliebt; si bliibed i sinere Liebi, wänn si sini Gebot halted, wie er d Gebot vom Vatter ghalte hät. Sis Gebot isch, dass si enand liebed, wie er si gliebt hät; kei Liebi isch grösser, als sis Läbe für d Fründe herzgää. Er nännt si Fründe, nüme Chnächt, wil er ine alles z wüsse taa hät, won er vom Vatter ghört hät. Nöd si händ ihn usgwählt, sondern er si, demit si gönd, Frucht bringed und iri Frucht bliibt."),
 "TU-JHN-015-018-027": ("De Hass vo de Wält und s Züügnis", "Wänn d Wält d Jünger hasst, hät si de Jesus vor ine ghasst; wil er si us de Wält usgwählt hät, sind si nöd vo de Wält. Wie me ihn verfolgt hät, wird me au si verfolge, wäge sim Name, wil me dä nöd kännt, wo ihn gschickt hät. Wil er choo isch, gredt und Wärch taa hät, händ die, wo hassed, kei Usred für iri Sünd; so erfüllt sich s Wort: «Si händ mich ohni Grund ghasst.» De Biistand, de Geischt vo de Wahrheit, wo de Jesus vom Vatter schickt, wird über ihn Züügnis ablegge, und au d Jünger, wo vo Aafang aa bi ihm sind."),
 "TU-JHN-016-001-033": ("Verfolgig, Biistand und di chömftig Fröid", "De Jesus seit voruus, dass me d Jünger us de Synagoge usschlüüsse wird und dass dä, wo si tötet, meint, er bringi Gott en Dienscht dar. Er gaat zu dem, wo ihn gschickt hät; das isch guet für si, suscht chunnt de Biistand nöd. De wird d Wält überfüere wäge de Sünd, de Grächtigkeit und em Gricht und d Jünger i de ganze Wahrheit füere. De ratlose Jünger seit er: Es Wiili, und si gsehnd en nüme, und wider es Wiili, und si wärded en gseh; iri Truurigkeit wird zur Fröid wie bi ere Frau nach de Geburt. D Jünger bekänned, dass er vo Gott usgange isch; de Jesus seit voruus, dass si sich verstreued und en elei lönd, und schlüüsst: «Ich han d Wält überwunde.»"),
 "TU-JHN-016-001-004": ("D Aakündigung vo de Verfolgig", "De Jesus seit de Jünger, demit si nöd z Fall chömed: Me wird si us de Synagoge usschlüüsse, und es chunnt d Stund, wo jede, wo si tötet, meint, er bringi Gott en Dienscht dar. Das wird passiere, wil me weder de Vatter no ihn erchännt hät. Er seit ine s, demit si dra dänked, wänn s iitrifft; am Aafang hät er s nöd gseit, wil er bi ine gsii isch."),
 "TU-JHN-016-005-015": ("Was de Biistand tuet", "De Jesus gaat zu dem, wo ihn gschickt hät; kein fröget, wohii er gaat, d Truurigkeit hät ires Härz gfüllt. Es isch guet für si, dass er wägg gaat, suscht chunnt de Biistand nöd zu ine. Wänn er chunnt, wird er d Wält überfüere wäge de Sünd, de Grächtigkeit und em Gricht. Als Geischt vo de Wahrheit wird er d Jünger i de ganze Wahrheit füere, rede, won er ghöre wird, ine verchünde, was chunnt, und de Jesus verherrliche, wil er vo dem nimmt, wo ihm ghört."),
 "TU-JHN-016-016-024": ("Truurigkeit wird zur Fröid", "De Jesus seit: «Es Wiili, und ir gsehnd mich nüme, und wider es Wiili, und ir wärded mich gseh.» D Jünger verstönd s nöd. De Jesus seit voruus: Si wärded briegge, während d Wält sich fröit, aber iri Truurigkeit wird zur Fröid, wie e Frau nach de Geburt d Not vergisst. Er wird si wider gseh, und iri Fröid nimmt ine niemer. Was si de Vatter bitted, git er ine i sim Name; si söled bitte, demit iri Fröid vollkomme isch."),
 "TU-JHN-016-025-033": ("Offeni Red und d Wält überwunde", "De Jesus seit, er redi nüme i Bildwort, sondern verzelli offe vom Vatter; de Vatter sälber hät si gern, wil si de Jesus gern händ und glaubed, dass er vo Gott usgange isch. Er isch vom Vatter usgange und gaat zum Vatter. D Jünger säged, jetzt redi er offe, und si glaubed, dass er vo Gott usgange isch. De Jesus fröget, öb si jetzt glaubed, und seit voruus, dass si sich verstreued und en elei lönd; aber er isch nöd elei, de Vatter isch bi ihm. I de Wält händ si Not, aber er hät d Wält überwunde."),
 "TU-JHN-017-001-026": ("S Gebätt vom Jesus", "De Jesus hebt d Auge zum Himmel uf und bättet: D Stund isch choo; de Vatter söll de Sohn verherrliche, demit de Sohn ihn verherrlichi. Ewigs Läbe isch, de einzig wahr Gott und dä, won er gschickt hät, Jesus Christus, z erchänne. Er bittet für d Jünger, wo ihm de Vatter us de Wält gää hät: dass de Vatter si i sim Name und vor em Böse bhüeti und i de Wahrheit heiligi; wie de Vatter ihn i d Wält gschickt hät, hät er si i d Wält gschickt. Dänn bittet er für alli, wo dur ires Wort glaubed: dass alli eis sigid, demit d Wält glaubt, dass de Vatter ihn gschickt hät, und dass si bi ihm sigid und sini Herrlichkeit gsehnd."),
 "TU-JHN-017-001-005": ("Bitt um Verherrlichung", "De Jesus bättet: D Stund isch choo. De Vatter söll de Sohn verherrliche, wo er ihm Vollmacht über alles Fleisch gää hät, demit er allne, wo ihm de Vatter gää hät, ewigs Läbe git; s ewig Läbe isch, de einzig wahr Gott und dä, won er gschickt hät, Jesus Christus, z erchänne. De Jesus hät de Vatter uf de Ärde verherrlicht und s Wärch volländet, wo ihm de Vatter gää hät; jetzt bittet er um d Herrlichkeit, won er bim Vatter gha hät, bevor d Wält gsii isch."),
 "TU-JHN-017-006-019": ("Fürbitt für d Jünger", "De Jesus hät de Name vom Vatter de Mänsche offebart, wo ihm de Vatter us de Wält gää hät; si händ sis Wort ghalte, d Wort vom Jesus aagnoo und glaubed, dass de Vatter ihn gschickt hät. Für si bittet er, nöd für d Wält. Er isch nüme i de Wält, si aber sind i de Wält; de heilig Vatter söll si i sim Name bhüete, demit si eis sind. Solang er bi ine gsii isch, hät er si bhüetet, und kein isch verlore gange usser em Sohn vom Verderbe. D Wält hät si ghasst, wil si nöd vo de Wält sind; er bittet nöd, si us de Wält wägznää, sondern si vor em Böse z bhüete und i de Wahrheit z heilige. Wie de Vatter ihn gschickt hät, hät er si i d Wält gschickt, und für si heiliget er sich sälber."),
 "TU-JHN-017-020-026": ("Fürbitt für die, wo dur ires Wort glaubed", "De Jesus bittet au für die, wo dur s Wort vo de Jünger a ihn glaubed: dass alli eis sigid, wie de Vatter in ihm und er im Vatter isch, demit d Wält glaubt und erchännt, dass de Vatter ihn gschickt und si gliebt hät, wie er ihn gliebt hät. Er wott, dass si bi ihm sind, won er isch, und sini Herrlichkeit gsehnd, wo ihm de Vatter gää hät, wil er ihn vor de Grundlegig vo de Wält gliebt hät. D Wält hät de grächt Vatter nöd erchännt, de Jesus aber hät ihn erchännt; er hät de Jünger de Name vom Vatter bekannt gmacht und wird en bekannt mache, demit d Liebi vom Vatter in ine isch und er in ine."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("Die Grundentscheide zu den johanneischen Schlüsselwörtern sind in scripts/authoring/johannes_text_01_03.py begründet und gelten "
  "hier unverändert: ἐγώ εἰμι «Ich bin …» ([[JHN.14.6]], [[JHN.15.1]], [[JHN.15.5]]), δόξα/δοξάζω «Herrlichkeit/verherrlichen», "
  "μένω «bleiben», ἀμὴν ἀμήν «Amen, amen», κόσμος «Welt», παράκλητος «Beistand» ([[JHN.14.16]], [[JHN.14.26]], [[JHN.15.26]], "
  "[[JHN.16.7]]). οἱ Ἰουδαῖοι kommt in Kapitel 14–17 nicht vor; für die Grundentscheidung «die Juden» und ihre Alternative siehe dort."),
 ("Weitere Wortwahl in Kapitel 14–17: τηρέω mit Geboten und Wort «halten», mit Personen «bewahren»; φυλάσσω «behüten»; "
  "ἀγαπάω «lieben», φιλέω «lieb haben» ([[JHN.15.19]], [[JHN.16.27]]); ἐρωτάω je nach Zusammenhang «fragen» oder «bitten»; "
  "λύπη «Trauer» (in [[JHN.16.21]] «Schmerz»); θλῖψις «Bedrängnis». ὅτι vor direkter Rede oder Zitat ist nicht eigens übersetzt."),
 ("Anführungszeichen: [[JHN.14.1]]–[[JHN.14.4]] setzen die in Kapitel 13 begonnene Rede fort, [[JHN.15.1]]–[[JHN.16.16]] schliessen "
  "ohne neue Redeeinleitung an [[JHN.14.31]] an; diese Redeteile stehen ohne äussere Anführungszeichen, Zitate darin in «». "
  "Wo Erzählung und Rede wechseln (Fragen der Jünger, [[JHN.16.17]]–[[JHN.16.33]], Gebet in Kapitel 17), steht die Rede in «»."),
 ("Auf [[JHN.14.31]] («Steht auf, lasst uns von hier gehen!») folgen Kapitel 15–17 ohne Ortswechsel bis [[JHN.18.1]]. Wie diese "
  "Abfolge entstanden ist, wird in der Forschung unterschiedlich beurteilt; die Übersetzung gibt den Text in der vorliegenden Reihenfolge wieder."),
 "In Kapitel 14–17 fehlt im SBLGNT kein Vers.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("D Grundentscheid zu de johanneische Schlüsselwört sind i scripts/authoring/johannes_text_01_03.py begründet und gälted da "
  "unveränderet: ἐγώ εἰμι «Ich bin …», δόξα/δοξάζω «Herrlichkeit/verherrliche», μένω «bliibe», ἀμὴν ἀμήν «Amen, amen, ich säge eu», "
  "κόσμος «Wält», παράκλητος «Biistand»; Gott heisst «Gott», de Vatter «de Vatter». οἱ Ἰουδαῖοι chunnt i Kapitel 14–17 nöd vor."),
 ("Wiiteri Wortwahl: τηρέω mit Gebot und Wort «halte», mit Persone «bhüete»; ἀγαπάω «liebe», φιλέω «gern ha»; "
  "κλῆμα «Schoss», ἄμπελος «Wiistock»."),
 ("Aafüerigszeiche: [[JHN.14.1]]–[[JHN.14.4]] und [[JHN.15.1]]–[[JHN.16.16]] sind Fortsetzige vo de Red ohni nöii Iileitig und "
  "stönd ohni üsseri Aafüerigszeiche; Zitat drin stönd in «»."),
]


def run():
    import json
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
            raise SystemExit(f"JHN {c}: Verse ohne Tokens – Bereich prüfen")
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Wiistock, Liebi), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-JHN-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; johanneische Leitwörter einheitlich wiedergegeben. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/johannes_text_14_17.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 14–17 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
