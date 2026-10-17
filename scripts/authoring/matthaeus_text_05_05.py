#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 5 (Beginn der Bergpredigt: Seligpreisungen, Salz und Licht, Gesetz und Propheten, die sechs
Gegenüberstellungen «Ich aber sage euch») – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_05_05.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 5 fehlt im SBLGNT kein Vers (per Skript geprüft); alle 48 Verse haben Tokens.
- Die Rede ([[MAT.5.3]]–[[MAT.7.27]]) steht ohne Anführungszeichen, wie in TRANS-MAT-006-005-015; Zitate innerhalb der
  Rede («Du sollst nicht töten», «Raka», «Ja, ja») stehen in «».
- [[MAT.5.39]]: Der SBLGNT liest σιαγόνα ohne σου (mit RP, gegen WH, Treg, NA28); die Übersetzung folgt ihm.
- [[MAT.6.5-MAT.6.15]] (Vaterunser) besteht schon; Begriffe («Vater in den Himmeln», «himmlischer Vater», «Lohn», «Heiden»,
  «vom Bösen») sind darauf abgestimmt.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1,
WREAD-CNTR-MAT-005-001-048) bzw. aus dem dort erfassten Wortlaut der CNTR-Transkriptionen (Sekundärtranskription), nicht
aus eigener Prüfung der Handschriften. Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts
(data/annotations) ermittelt.
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
CHAPTERS = ((5, 48),)

DE = {
 "MAT.5.1": "[Als er]{1} [aber]{2} [die Menge]{3,4} [sah]{1}, [stieg er]{5} [auf]{6} [den Berg]{7,8}; und{9} [als]{10} [er]{11} [sich gesetzt hatte]{10}, [traten]{12} [seine]{16} [Jünger]{14,15} [zu ihm]{13} [heran]{12}.",
 "MAT.5.2": "Und{1} [er öffnete]{2} [seinen]{5} [Mund]{3,4}, [lehrte]{6} [sie]{7} und [sagte]{8}:",
 "MAT.5.3": "[Selig]{1} sind [die]{2} [Armen]{3} [im]{4} [Geist]{5}, [denn]{6} [ihnen]{7} [gehört]{8} [das Reich]{9,10} [der Himmel]{11,12}.",
 "MAT.5.4": "[Selig]{1} sind [die]{2} [Trauernden]{3}, [denn]{4} [sie]{5} [werden getröstet werden]{6}.",
 "MAT.5.5": "[Selig]{1} sind [die]{2} [Sanftmütigen]{3}, [denn]{4} [sie]{5} [werden]{6} [die Erde]{7,8} [erben]{6}.",
 "MAT.5.6": "[Selig]{1} sind [die, die]{2} [nach der Gerechtigkeit]{6,7} [hungern]{3} und{4} [dürsten]{5}, [denn]{8} [sie]{9} [werden satt werden]{10}.",
 "MAT.5.7": "[Selig]{1} sind [die]{2} [Barmherzigen]{3}, [denn]{4} [sie]{5} [werden Barmherzigkeit erfahren]{6}.",
 "MAT.5.8": "[Selig]{1} sind [die, die]{2} [ein reines]{3} [Herz]{4,5} haben, [denn]{6} [sie]{7} [werden]{10} [Gott]{8,9} [sehen]{10}.",
 "MAT.5.9": "[Selig]{1} sind [die, die]{2} [Frieden stiften]{3}, [denn]{4} [sie]{5} [werden]{8} [Söhne]{6} [Gottes]{7} [genannt werden]{8}.",
 "MAT.5.10": "[Selig]{1} sind [die, die]{2} [wegen]{4} [der Gerechtigkeit]{5} [verfolgt worden sind]{3}, [denn]{6} [ihnen]{7} [gehört]{8} [das Reich]{9,10} [der Himmel]{11,12}.",
 "MAT.5.11": "[Selig]{1} [seid ihr]{2}, [wenn]{3} [sie]{4} [euch]{5} [beschimpfen]{4} und{6} [verfolgen]{7} und{8} [euch]{13} [meinetwegen]{15,16} [fälschlich]{14} [alles]{10} [Böse]{11} [nachsagen]{9,12}.",
 "MAT.5.12": "[Freut euch]{1} und{2} [jubelt]{3}, [denn]{4} [euer]{7} [Lohn]{5,6} ist [gross]{8} [in]{9} [den Himmeln]{10,11}; [so]{12} [haben sie]{14} [nämlich]{13} [die Propheten]{15,16} [verfolgt]{14}, [die]{17} [vor]{18} [euch]{19} waren.",
 "MAT.5.13": "[Ihr]{1} [seid]{2} [das Salz]{3,4} [der Erde]{5,6}. [Wenn]{7} [aber]{8} [das Salz]{9,10} [fad wird]{11}, [womit]{12,13} [soll es wieder salzig werden]{14}? [Es taugt]{17} [zu]{15} [nichts]{16} [mehr]{18}, [ausser]{19,20} [hinausgeworfen]{21,22} und [von]{24} [den Menschen]{25,26} [zertreten zu werden]{23}.",
 "MAT.5.14": "[Ihr]{1} [seid]{2} [das Licht]{3,4} [der Welt]{5,6}. [Eine Stadt]{9}, [die]{13} [auf]{11} [einem Berg]{12} [liegt]{13}, [kann]{8} [nicht]{7} [verborgen bleiben]{10}.",
 "MAT.5.15": "[Man zündet]{2} [auch keine]{1} [Lampe]{3} [an]{2} und{4} [stellt]{5} [sie]{6} [unter]{7} [den Scheffel]{8,9}, [sondern]{10} [auf]{11} [den Leuchter]{12,13}; und{14} [sie leuchtet]{15} [allen]{16}, [die]{17} [im]{18,19} [Haus]{20} sind.",
 "MAT.5.16": "[So]{1} [soll]{2} [euer]{5} [Licht]{3,4} [vor]{6} [den Menschen]{7,8} [leuchten]{2}, [damit]{9} [sie]{10} [eure]{11} [guten]{12,13} [Werke]{14} [sehen]{10} und{15} [euren]{19} [Vater]{17,18} [in]{20,21} [den Himmeln]{22,23} [preisen]{16}.",
 "MAT.5.17": "[Meint]{2} [nicht]{1}, [dass]{3} [ich gekommen sei]{4}, [das Gesetz]{6,7} [oder]{8} [die Propheten]{9,10} [aufzuheben]{5}. [Ich bin]{12} [nicht]{11} [gekommen]{12}, [um aufzuheben]{13}, [sondern]{14} [um zu erfüllen]{15}.",
 "MAT.5.18": "[Denn]{2} [amen]{1}, [ich sage]{3} [euch]{4}: [Bis]{5} [der Himmel]{8,9} und{10} [die Erde]{11,12} [vergehen]{7}, [wird]{20} [gewiss nicht]{18,19} [ein einziges]{14} [Jota]{13} [oder]{15} [ein einziges]{16} [Häkchen]{17} [vom]{21,22} [Gesetz]{23} [vergehen]{20}, [bis]{24} [alles]{26} [geschieht]{27}. ~6(ἄν macht den Nebensatz unbestimmt; nicht eigens wiedergegeben) ~25(ἄν macht den Nebensatz unbestimmt; nicht eigens wiedergegeben)",
 "MAT.5.19": "[Wer]{1,2} [also]{3} [eines]{5} [dieser]{8} [kleinsten]{9,10} [Gebote]{6,7} [auflöst]{4} und{11} [die Menschen]{14,15} [so]{13} [lehrt]{12}, [wird]{17} [im]{18,19} [Reich]{20} [der Himmel]{21,22} [der Kleinste]{16} [genannt werden]{17}; [wer]{23,25} sie [aber]{24} [tut]{26} und{27} [lehrt]{28}, [der]{29} [wird]{31} [im]{32,33} [Reich]{34} [der Himmel]{35,36} [gross]{30} [genannt werden]{31}.",
 "MAT.5.20": "[Denn]{2} [ich sage]{1} [euch]{3}: [Wenn]{5} [eure]{8} [Gerechtigkeit]{9,10} [nicht]{6} [weit über]{11} [die der Schriftgelehrten]{12,13} und{14} [Pharisäer]{15} [hinausgeht]{7}, [werdet ihr]{18} [gewiss nicht]{16,17} [in]{19} [das Reich]{20,21} [der Himmel]{22,23} [hineinkommen]{18}. ~4(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.5.21": "[Ihr habt gehört]{1}, [dass]{2} [zu den Alten]{4,5} [gesagt worden ist]{3}: «[Du sollst]{7} [nicht]{6} [töten]{7}; [wer]{8,10} [aber]{9} [tötet]{11}, [wird]{13} [dem Gericht]{14,15} [verfallen]{12}.»",
 "MAT.5.22": "[Ich]{1} [aber]{2} [sage]{3} [euch]{4}: [Jeder, der]{6,7} [seinem]{11} [Bruder]{9,10} [zürnt]{8}, [wird]{13} [dem Gericht]{14,15} [verfallen]{12}; [wer]{16,18} [aber]{17} zu [seinem]{22} [Bruder]{20,21} [sagt]{19}: «[Raka]{23}!», [wird]{25} [dem Hohen Rat]{26,27} [verfallen]{24}; [wer]{28,30} [aber]{29} [sagt]{31}: «[Du Narr]{32}!», [wird]{34} [dem Feuer]{38,39} [der Hölle]{35-37} [verfallen]{33}. ~5(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.5.23": "[Wenn]{1} [du]{3} [nun]{2} [deine]{6} [Gabe]{4,5} [zum]{7,8} [Altar]{9} [bringst]{3} [und]{10} [dich]{11} [dort]{10} [erinnerst]{11}, [dass]{12} [dein]{15} [Bruder]{13,14} [etwas]{17} [gegen]{18} [dich]{19} [hat]{16},",
 "MAT.5.24": "so [lass]{1} [deine]{5} [Gabe]{3,4} [dort]{2} [vor]{6} [dem Altar]{7,8} und{9} [geh]{10}; [versöhne dich]{12} [zuerst]{11} [mit]{13} [deinem]{15} [Bruder]{14}, und{16} [dann]{17} [komm]{18} und [bring]{19} [deine]{22} [Gabe]{20,21} [dar]{19}.",
 "MAT.5.25": "[Einige dich]{1,2} [schnell]{6} [mit]{3} [deinem]{5} [Gegner]{4}, [solange]{7,8} [du]{9} [mit]{10} [ihm]{11} [unterwegs]{12-14} [bist]{9}, [damit]{15} [dich]{16} [der Gegner]{18,19} [nicht]{15} [dem Richter]{20,21} [übergibt]{17} und{22} [der Richter]{23,24} [dem Gerichtsdiener]{25,26} und{27} [du]{30} [ins]{28} [Gefängnis]{29} [geworfen wirst]{30}.",
 "MAT.5.26": "[Amen]{1}, [ich sage]{2} [dir]{3}: [Du wirst]{6} [gewiss nicht]{4,5} [von dort]{7} [herauskommen]{6}, [bis]{8} [du]{10} [den letzten]{11,12} [Rappen]{13} [bezahlt hast]{10}. ~9(ἄν macht den Nebensatz unbestimmt; nicht eigens wiedergegeben)",
 "MAT.5.27": "[Ihr habt gehört]{1}, [dass]{2} [gesagt worden ist]{3}: «[Du sollst]{5} [nicht]{4} [ehebrechen]{5}.»",
 "MAT.5.28": "[Ich]{1} [aber]{2} [sage]{3} [euch]{4}: [Jeder, der]{6,7} [eine Frau]{9} [ansieht]{8}, [um]{10,11} [sie]{13} [zu begehren]{12}, [hat]{15} [in]{17} [seinem]{20} [Herzen]{18,19} [schon]{14} [mit ihr]{16} [die Ehe gebrochen]{15}. ~5(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.5.29": "[Wenn]{1} [aber]{2} [dein]{5} [rechtes]{6,7} [Auge]{3,4} [dich]{9} [zu Fall bringt]{8}, [reiss]{10} [es]{11} [heraus]{10} und{12} [wirf]{13} es [von]{14} [dir]{15} [weg]{13}! [Denn]{17} [es ist besser]{16} [für dich]{18}, [dass]{19} [eines]{21} [deiner]{24} [Glieder]{22,23} [verloren geht]{20} und{25} [nicht]{26} [dein]{30} [ganzer]{27} [Leib]{28,29} [in]{32} [die Hölle]{33} [geworfen wird]{31}.",
 "MAT.5.30": "Und{1} [wenn]{2} [deine]{5} [rechte]{3,4} [Hand]{6} [dich]{8} [zu Fall bringt]{7}, [hau]{9} [sie]{10} [ab]{9} und{11} [wirf]{12} sie [von]{13} [dir]{14} [weg]{12}! [Denn]{16} [es ist besser]{15} [für dich]{17}, [dass]{18} [eines]{20} [deiner]{23} [Glieder]{21,22} [verloren geht]{19} und{24} [nicht]{25} [dein]{29} [ganzer]{26} [Leib]{27,28} [in]{30} [die Hölle]{31} [kommt]{32}.",
 "MAT.5.31": "[Es ist]{1} [aber]{2} [gesagt worden]{1}: «[Wer]{3,4} [seine]{8} [Frau]{6,7} [entlässt]{5}, [soll]{9} [ihr]{10} [einen Scheidebrief]{11} [geben]{9}.»",
 "MAT.5.32": "[Ich]{1} [aber]{2} [sage]{3} [euch]{4}: [Jeder, der]{6,7} [seine]{11} [Frau]{9,10} [entlässt]{8} – [ausser]{12} [wegen]{13} [Unzucht]{14} –, [macht]{15}, [dass]{15} [mit ihr]{16} [die Ehe gebrochen wird]{17}; und{18} [wer]{19,20} [eine Entlassene]{21} [heiratet]{22}, [bricht die Ehe]{23}. ~5(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.5.33": "[Ihr habt]{2} [weiter]{1} [gehört]{2}, [dass]{3} [zu den Alten]{5,6} [gesagt worden ist]{4}: «[Du sollst]{8} [keinen]{7} [Meineid schwören]{8}; [du sollst]{9} [aber]{10} [dem Herrn]{11,12} [deine]{15} [Eide]{13,14} [halten]{9}.»",
 "MAT.5.34": "[Ich]{1} [aber]{2} [sage]{3} [euch]{4}: [Ihr sollt]{6} [überhaupt]{7} [nicht]{5} [schwören]{6}, [weder]{8} [beim]{9,10} [Himmel]{11}, [denn]{12} [er ist]{14} [der Thron]{13} [Gottes]{15,16},",
 "MAT.5.35": "[noch]{1} [bei]{2} [der Erde]{3,4}, [denn]{5} [sie ist]{7} [der Schemel]{6} [seiner]{10} [Füsse]{8,9}, [noch]{11} [bei]{12} [Jerusalem]{13}, [denn]{14} [es ist]{16} [die Stadt]{15} [des grossen]{17,18} [Königs]{19}.",
 "MAT.5.36": "[Schwöre]{6} [auch nicht]{1} [bei]{2} [deinem]{5} [Kopf]{3,4}, [denn]{7} [du kannst]{9} [nicht]{8} [ein einziges]{10} [Haar]{11} [weiss]{12} [oder]{14} [schwarz]{15} [machen]{13}.",
 "MAT.5.37": "[Eure]{5} [Rede]{3,4} [aber]{2} [sei]{1}: «[Ja]{6}, [ja]{7}», «[nein]{8}, [nein]{9}»; [was]{10} [aber]{11} [darüber hinausgeht]{12,13}, [ist]{17} [vom]{14,15} [Bösen]{16}.",
 "MAT.5.38": "[Ihr habt gehört]{1}, [dass]{2} [gesagt worden ist]{3}: «[Auge]{4} [um]{5} [Auge]{6} und{7} [Zahn]{8} [um]{9} [Zahn]{10}.»",
 "MAT.5.39": "[Ich]{1} [aber]{2} [sage]{3} [euch]{4}: [Ihr sollt]{6} [dem Bösen]{7,8} [nicht]{5} [widerstehen]{6}; [sondern]{9}: [Wer]{10} [dich]{11} [auf]{13} [die rechte]{14,15} [Wange]{16} [schlägt]{12}, [dem]{18} [halte]{17} [auch]{19} [die andere]{20,21} [hin]{17}.",
 "MAT.5.40": "Und{1} [wer]{2} [mit dir]{4} [vor Gericht gehen]{5} und{6} [dein]{9} [Hemd]{7,8} [nehmen]{10} [will]{3}, [dem]{12} [lass]{11} [auch]{13} [den Mantel]{14,15}.",
 "MAT.5.41": "Und{1} [wer]{2} [dich]{3} [zwingt]{4}, [eine]{6} [Meile]{5} [mitzugehen]{4}, [mit]{8} [dem]{9} [geh]{7} [zwei]{10}.",
 "MAT.5.42": "[Gib]{4} [dem, der]{1} [dich]{3} [bittet]{2}, und{5} [wende dich]{12} [nicht]{11} [ab]{12} [von dem, der]{6} [von]{8} [dir]{9} [borgen]{10} [will]{7}.",
 "MAT.5.43": "[Ihr habt gehört]{1}, [dass]{2} [gesagt worden ist]{3}: «[Du sollst]{4} [deinen]{7} [Nächsten]{5,6} [lieben]{4} und{8} [deinen]{12} [Feind]{10,11} [hassen]{9}.»",
 "MAT.5.44": "[Ich]{1} [aber]{2} [sage]{3} [euch]{4}: [Liebt]{5} [eure]{8} [Feinde]{6,7} und{9} [betet]{10} [für]{11} [die, die]{12} [euch]{14} [verfolgen]{13},",
 "MAT.5.45": "[damit]{1} [ihr]{2} [Söhne]{3} [eures]{6} [Vaters]{4,5} [in]{7,8} [den Himmeln]{9} [werdet]{2}; [denn]{10} [er lässt]{14} [seine]{13} [Sonne]{11,12} [aufgehen]{14} [über]{15} [Böse]{16} und{17} [Gute]{18} und{19} [lässt regnen]{20} [über]{21} [Gerechte]{22} und{23} [Ungerechte]{24}.",
 "MAT.5.46": "[Denn]{2} [wenn]{1} [ihr]{3} [die]{4} [liebt]{3}, [die]{4} [euch]{6} [lieben]{5}, [welchen]{7} [Lohn]{8} [habt ihr]{9}? [Tun]{16} [nicht]{10} [auch]{11} [die Zöllner]{12,13} [dasselbe]{14,15}?",
 "MAT.5.47": "Und{1} [wenn]{2} [ihr]{3} [nur]{7} [eure]{6} [Brüder]{4,5} [grüsst]{3}, [was]{8} [tut ihr]{10} [Besonderes]{9}? [Tun]{17} [nicht]{11} [auch]{12} [die Heiden]{13,14} [dasselbe]{15,16}?",
 "MAT.5.48": "[Ihr]{3} [sollt]{1} [also]{2} [vollkommen]{4} [sein]{1}, [wie]{5} [euer]{8} [himmlischer]{9,10} [Vater]{6,7} [vollkommen]{11} [ist]{12}.",
}

GSW = {
 "MAT.5.1": "[Wo er]{1} [aber]{2} [d Mängi]{3,4} [gsee hät]{1}, [isch er]{5} [uf]{6} [de Bärg]{7,8} [ufegstige]{5}; und{9} [wo]{10} [er]{11} [abgsässe isch]{10}, [sind]{12} [sini]{16} [Jünger]{14,15} [zu ihm]{13} [choo]{12}.",
 "MAT.5.2": "Und{1} [er hät]{2} [sin]{5} [Mund]{3,4} [uftaa]{2}, [hät]{6} [si]{7} [gleert]{6} und [gseit]{8}:",
 "MAT.5.3": "[Sälig]{1} sind [di]{2} [Arme]{3} [im]{4} [Geischt]{5}, [dänn]{6} [ine]{7} [ghört]{8} [s Riich]{9,10} [vo de Himel]{11,12}.",
 "MAT.5.4": "[Sälig]{1} sind [die]{2}, [wo truured]{3}, [dänn]{4} [si]{5} [wärded tröschtet]{6}.",
 "MAT.5.5": "[Sälig]{1} sind [di]{2} [Sanftmüetige]{3}, [dänn]{4} [si]{5} [wärded]{6} [d Ärde]{7,8} [erbe]{6}.",
 "MAT.5.6": "[Sälig]{1} sind [die, wo]{2} [nach de Grächtigkeit]{6,7} [hungered]{3} und{4} [dürschted]{5}, [dänn]{8} [si]{9} [wärded satt]{10}.",
 "MAT.5.7": "[Sälig]{1} sind [di]{2} [Barmhärzige]{3}, [dänn]{4} [si]{5} [wärded Barmhärzigkeit erfaare]{6}.",
 "MAT.5.8": "[Sälig]{1} sind [die, wo]{2} [es reins]{3} [Härz]{4,5} händ, [dänn]{6} [si]{7} [wärded]{10} [Gott]{8,9} [gsee]{10}.",
 "MAT.5.9": "[Sälig]{1} sind [die, wo]{2} [Fride stifted]{3}, [dänn]{4} [si]{5} [wärded]{8} [Söhn]{6} [vo Gott]{7} [gnännt]{8}.",
 "MAT.5.10": "[Sälig]{1} sind [die, wo]{2} [wäge]{4} [de Grächtigkeit]{5} [verfolgt worde sind]{3}, [dänn]{6} [ine]{7} [ghört]{8} [s Riich]{9,10} [vo de Himel]{11,12}.",
 "MAT.5.11": "[Sälig]{1} [sind ir]{2}, [wänn]{3} [si]{4} [eu]{5} [beschimpfed]{4} und{6} [verfolged]{7} und{8} [wäge mir]{15,16} [alles]{10} [Bööse]{11} [gäge]{12} [eu]{13} [säged]{9} [und debii lüüged]{14}.",
 "MAT.5.12": "[Fröied eu]{1} und{2} [jubled]{3}, [dänn]{4} [eue]{7} [Loon]{5,6} isch [gross]{8} [i]{9} [de Himel]{10,11}; [eso]{12} [händ si]{14} [nämli]{13} [d Prophete]{15,16} [verfolgt]{14}, [wo]{17} [vor]{18} [eu]{19} gsii sind.",
 "MAT.5.13": "[Ir]{1} [sind]{2} [s Salz]{3,4} [vo de Ärde]{5,6}. [Wänn]{7} [aber]{8} [s Salz]{9,10} [fad wird]{11}, [mit was]{12,13} [söll s wider salzig wärde]{14}? [Es isch]{17} [für]{15} [nüüt]{16} [mee]{18} [guet]{17}, [als dass es]{19,20} [usegworfe]{21,22} und [vo]{24} [de Lüüt]{25,26} [vertrampet wird]{23}.",
 "MAT.5.14": "[Ir]{1} [sind]{2} [s Liecht]{3,4} [vo de Wält]{5,6}. [E Stadt]{9}, [wo]{13} [uf]{11} [eme Bärg]{12} [liit]{13}, [cha]{8} [nöd]{7} [versteckt bliibe]{10}.",
 "MAT.5.15": "[Me zündt]{2} [au kei]{1} [Lampe]{3} [aa]{2} und{4} [stellt]{5} [si]{6} [under]{7} [de Schäffel]{8,9}, [sondern]{10} [uf]{11} [de Lüüchter]{12,13}; und{14} [si lüüchtet]{15} [allne]{16}, [wo]{17} [im]{18,19} [Huus]{20} sind.",
 "MAT.5.16": "[Eso]{1} [söll]{2} [eues]{5} [Liecht]{3,4} [vor]{6} [de Lüüt]{7,8} [lüüchte]{2}, [demit]{9} [si]{10} [eui]{11} [guete]{12,13} [Wärch]{14} [gseend]{10} und{15} [eue]{19} [Vatter]{17,18} [i]{20,21} [de Himel]{22,23} [priised]{16}.",
 "MAT.5.17": "[Meined]{2} [nöd]{1}, [dass]{3} [ich choo bi]{4}, [für]{5} [s Gsetz]{6,7} [oder]{8} [d Prophete]{9,10} [ufzhebe]{5}. [Ich bi]{12} [nöd]{11} [choo]{12} [zum Ufhebe]{13}, [sondern]{14} [zum Erfülle]{15}.",
 "MAT.5.18": "[Dänn]{2} [amen]{1}, [ich säg]{3} [eu]{4}: [Bis]{5} [de Himel]{8,9} und{10} [d Ärde]{11,12} [vergönd]{7}, [vergaat]{20} [vom]{21,22} [Gsetz]{23} [sicher nöd]{18,19} [es einzigs]{14} [Jota]{13} [oder]{15} [es einzigs]{16} [Hääggli]{17}, [bis]{24} [alles]{26} [gschee isch]{27}. ~6(ἄν macht de Nebesatz unbestimmt; nöd eigens widergää) ~25(ἄν macht de Nebesatz unbestimmt; nöd eigens widergää)",
 "MAT.5.19": "[Wer]{1,2} [also]{3} [eis]{5} [vo dene]{8} [chliinschte]{9,10} [Gebot]{6,7} [uflööst]{4} und{11} [d Lüüt]{14,15} [eso]{13} [leert]{12}, [wird]{17} [im]{18,19} [Riich]{20} [vo de Himel]{21,22} [de Chliinscht]{16} [gnännt]{17}; [wer]{23,25} si [aber]{24} [tuet]{26} und{27} [leert]{28}, [dä]{29} [wird]{31} [im]{32,33} [Riich]{34} [vo de Himel]{35,36} [gross]{30} [gnännt]{31}.",
 "MAT.5.20": "[Ich säg]{1} [eu]{3} [nämli]{2}: [Wänn]{5} [eui]{8} [Grächtigkeit]{9,10} [nöd]{6} [wiit über]{11} [die vo de Schriftgelehrti]{12,13} und{14} [Pharisäer]{15} [usegaat]{7}, [chömed ir]{18} [sicher nöd]{16,17} [i]{19} [s Riich]{20,21} [vo de Himel]{22,23} [ine]{18}. ~4(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.5.21": "[Ir händ ghört]{1}, [dass]{2} [zu de Alte]{4,5} [gseit worde isch]{3}: «[Du söllsch]{7} [nöd]{6} [töte]{7}; [wer]{8,10} [aber]{9} [tötet]{11}, [wird]{13} [em Gricht]{14,15} [verfalle]{12} [sii]{13}.»",
 "MAT.5.22": "[Ich]{1} [aber]{2} [säg]{3} [eu]{4}: [Jede, wo]{6,7} [uf sin]{11} [Brüeder]{9,10} [wüetig isch]{8}, [wird]{13} [em Gricht]{14,15} [verfalle]{12} [sii]{13}; [wer]{16,18} [aber]{17} zu [sim]{22} [Brüeder]{20,21} [seit]{19}: «[Raka]{23}!», [wird]{25} [em Hoche Raat]{26,27} [verfalle]{24} [sii]{25}; [wer]{28,30} [aber]{29} [seit]{31}: «[Du Tubel]{32}!», [wird]{34} [em Füür]{38,39} [vo de Höll]{35-37} [verfalle]{33} [sii]{34}. ~5(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.5.23": "[Wänn]{1} [du]{3} [also]{2} [dis]{6} [Gschänk]{4,5} [zum]{7,8} [Altar]{9} [bringsch]{3} [und]{10} [dich]{11} [dört]{10} [erinnerisch]{11}, [dass]{12} [din]{15} [Brüeder]{13,14} [öppis]{17} [gäge]{18} [dich]{19} [hät]{16},",
 "MAT.5.24": "dänn [la]{1} [dis]{5} [Gschänk]{3,4} [dört]{2} [vor]{6} [em Altar]{7,8} staa und{9} [gang]{10}; [versöön di]{12} [zerscht]{11} [mit]{13} [dim]{15} [Brüeder]{14}, und{16} [dänn]{17} [chumm]{18} und [bring]{19} [dis]{22} [Gschänk]{20,21} [dar]{19}.",
 "MAT.5.25": "[Einig di]{1,2} [schnäll]{6} [mit]{3} [dim]{5} [Gägner]{4}, [solang]{7,8} [du]{9} [mit]{10} [ihm]{11} [underwägs]{12-14} [bisch]{9}, [demit]{15} [di]{16} [de Gägner]{18,19} [nöd]{15} [em Richter]{20,21} [übergit]{17} und{22} [de Richter]{23,24} [em Gerichtsdiener]{25,26} und{27} [du]{30} [is]{28} [Gfängnis]{29} [gworfe wirsch]{30}.",
 "MAT.5.26": "[Amen]{1}, [ich säg]{2} [dir]{3}: [Du chunnsch]{6} [sicher nöd]{4,5} [vo dört]{7} [use]{6}, [bis]{8} [du]{10} [de letscht]{11,12} [Rappe]{13} [zaalt häsch]{10}. ~9(ἄν macht de Nebesatz unbestimmt; nöd eigens widergää)",
 "MAT.5.27": "[Ir händ ghört]{1}, [dass]{2} [gseit worde isch]{3}: «[Du söllsch]{5} [nöd]{4} [d Ee breche]{5}.»",
 "MAT.5.28": "[Ich]{1} [aber]{2} [säg]{3} [eu]{4}: [Jede, wo]{6,7} [e Frau]{9} [aaluegt]{8}, [für]{10,11} [si]{13} [z begääre]{12}, [hät]{15} [i]{17} [sim]{20} [Härz]{18,19} [scho]{14} [mit ire]{16} [d Ee broche]{15}. ~5(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.5.29": "[Wänn]{1} [aber]{2} [dis]{5} [rächt]{6,7} [Aug]{3,4} [dich]{9} [zu Fall bringt]{8}, [riiss]{10} [s]{11} [use]{10} und{12} [wirf]{13} s [vo]{14} [dir]{15} [wäg]{13}! [Es isch]{16} [nämli]{17} [besser]{16} [für dich]{18}, [dass]{19} [eis]{21} [vo dine]{24} [Glider]{22,23} [verlore gaat]{20} und{25} [nöd]{26} [din]{30} [ganz]{27} [Liib]{28,29} [i]{32} [d Höll]{33} [gworfe wird]{31}.",
 "MAT.5.30": "Und{1} [wänn]{2} [dini]{5} [rächt]{3,4} [Hand]{6} [dich]{8} [zu Fall bringt]{7}, [hau]{9} [si]{10} [ab]{9} und{11} [wirf]{12} si [vo]{13} [dir]{14} [wäg]{12}! [Es isch]{15} [nämli]{16} [besser]{15} [für dich]{17}, [dass]{18} [eis]{20} [vo dine]{23} [Glider]{21,22} [verlore gaat]{19} und{24} [nöd]{25} [din]{29} [ganz]{26} [Liib]{27,28} [i]{30} [d Höll]{31} [chunnt]{32}.",
 "MAT.5.31": "[Es isch]{1} [aber]{2} [gseit worde]{1}: «[Wer]{3,4} [sini]{8} [Frau]{6,7} [entlaat]{5}, [söll]{9} [ire]{10} [en Scheidigsbrief]{11} [gää]{9}.»",
 "MAT.5.32": "[Ich]{1} [aber]{2} [säg]{3} [eu]{4}: [Jede, wo]{6,7} [sini]{11} [Frau]{9,10} [entlaat]{8} – [ussert]{12} [wäge]{13} [Unzucht]{14} –, [macht]{15}, [dass]{15} [mit ire]{16} [d Ee broche wird]{17}; und{18} [wer]{19,20} [e Entlasseni]{21} [hüratet]{22}, [bricht d Ee]{23}. ~5(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.5.33": "[Ir händ]{2} [wiiter]{1} [ghört]{2}, [dass]{3} [zu de Alte]{5,6} [gseit worde isch]{4}: «[Du söllsch]{8} [kei]{7} [Meineid schwöre]{8}; [du söllsch]{9} [aber]{10} [em Herr]{11,12} [dini]{15} [Eid]{13,14} [halte]{9}.»",
 "MAT.5.34": "[Ich]{1} [aber]{2} [säg]{3} [eu]{4}: [Ir söled]{6} [überhaupt]{7} [nöd]{5} [schwöre]{6}, [weder]{8} [bim]{9,10} [Himel]{11}, [dänn]{12} [er isch]{14} [de Troon]{13} [vo Gott]{15,16},",
 "MAT.5.35": "[no]{1} [bi]{2} [de Ärde]{3,4}, [dänn]{5} [si isch]{7} [de Schämel]{6} [für sini]{10} [Füess]{8,9}, [no]{11} [bi]{12} [Jerusalem]{13}, [dänn]{14} [es isch]{16} [d Stadt]{15} [vom grosse]{17,18} [König]{19}.",
 "MAT.5.36": "[Schwör]{6} [au nöd]{1} [bi]{2} [dim]{5} [Chopf]{3,4}, [dänn]{7} [du chasch]{9} [nöd]{8} [es einzigs]{10} [Haar]{11} [wiiss]{12} [oder]{14} [schwarz]{15} [mache]{13}.",
 "MAT.5.37": "[Eui]{5} [Red]{3,4} [aber]{2} [söll sii]{1}: «[Ja]{6}, [ja]{7}», «[nei]{8}, [nei]{9}»; [was]{10} [aber]{11} [mee isch als das]{12,13}, [isch]{17} [vom]{14,15} [Bööse]{16}.",
 "MAT.5.38": "[Ir händ ghört]{1}, [dass]{2} [gseit worde isch]{3}: «[Aug]{4} [um]{5} [Aug]{6} und{7} [Zaa]{8} [um]{9} [Zaa]{10}.»",
 "MAT.5.39": "[Ich]{1} [aber]{2} [säg]{3} [eu]{4}: [Ir söled]{6} [em Bööse]{7,8} [nöd]{5} [widerstaa]{6}; [sondern]{9}: [Wer]{10} [dich]{11} [uf]{13} [de rächt]{14,15} [Bagge]{16} [schlaat]{12}, [däm]{18} [heb]{17} [au]{19} [de ander]{20,21} [ane]{17}.",
 "MAT.5.40": "Und{1} [wer]{2} [mit dir]{4} [vor Gricht gaa]{5} und{6} [dis]{9} [Hemd]{7,8} [nää]{10} [will]{3}, [däm]{12} [la]{11} [au]{13} [de Mantel]{14,15}.",
 "MAT.5.41": "Und{1} [wer]{2} [dich]{3} [zwingt]{4}, [ei]{6} [Meile]{5} [mitzgaa]{4}, [mit]{8} [däm]{9} [gang]{7} [zwei]{10}.",
 "MAT.5.42": "[Gib]{4} [däm, wo]{1} [dich]{3} [bittet]{2}, und{5} [cheer di]{12} [nöd]{11} [ab]{12} [vo däm, wo]{6} [vo]{8} [dir]{9} [öppis entlehne]{10} [will]{7}.",
 "MAT.5.43": "[Ir händ ghört]{1}, [dass]{2} [gseit worde isch]{3}: «[Du söllsch]{4} [din]{7} [Nächschte]{5,6} [liebe]{4} und{8} [din]{12} [Find]{10,11} [hasse]{9}.»",
 "MAT.5.44": "[Ich]{1} [aber]{2} [säg]{3} [eu]{4}: [Liebed]{5} [eui]{8} [Find]{6,7} und{9} [bätted]{10} [für]{11} [die, wo]{12} [eu]{14} [verfolged]{13},",
 "MAT.5.45": "[demit]{1} [ir]{2} [Söhn]{3} [vo eurem]{4,6} [Vatter]{5} [i]{7,8} [de Himel]{9} [wärded]{2}; [dänn]{10} [er laat]{14} [sini]{13} [Sunne]{11,12} [ufgaa]{14} [über]{15} [Bööse]{16} und{17} [Gueti]{18} und{19} [laat s rägne]{20} [über]{21} [Grächti]{22} und{23} [Ungrächti]{24}.",
 "MAT.5.46": "[Dänn]{2} [wänn]{1} [ir]{3} [die]{4} [liebed]{3}, [wo]{4} [eu]{6} [liebed]{5}, [was für en]{7} [Loon]{8} [händ ir]{9}? [Mached]{16} [nöd]{10} [au]{11} [d Zöllner]{12,13} [s Gliiche]{14,15}?",
 "MAT.5.47": "Und{1} [wänn]{2} [ir]{3} [nu]{7} [eui]{6} [Brüeder]{4,5} [grüessed]{3}, [was]{8} [mached ir]{10} [Bsunders]{9}? [Mached]{17} [nöd]{11} [au]{12} [d Heide]{13,14} [s Gliiche]{15,16}?",
 "MAT.5.48": "[Ir]{3} [söled]{1} [also]{2} [vollkomme]{4} [sii]{1}, [wie]{5} [eue]{8} [himmlisch]{9,10} [Vatter]{6,7} [vollkomme]{11} [isch]{12}.",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, andere Möglichkeiten, Hinweis)
DEC_DE = [
 ("MAT.5.1", "die Menge", "adapted", "τοὺς ὄχλους", "die Mengen", ["die Volksmengen", "die Scharen"],
  "Matthäus setzt ὄχλος oft in den Plural (nach MACULA-Lemma 49-mal im Buch). Im Deutschen steht die Einzahl; gemeint sind die Menschenmengen aus [[MAT.4.25]]. Dass sie mithören, setzt [[MAT.7.28]] voraus. Mundart «d Mängi»."),
 ("MAT.5.1", "auf den Berg", "literal", "εἰς τὸ ὄρος", None, ["auf einen Berg", "ins Bergland"],
  "Mit Artikel, aber ohne Namen. Daher der übliche Name «Bergpredigt». Viele sehen einen Anklang an Mose, der auf den Berg Sinai steigt ([[EXO.19.3]], [[EXO.24.12]]–[[EXO.24.18]]); [[LUK.6.17]] verlegt die verwandte Rede auf einen ebenen Platz."),
 ("MAT.5.1", "als er sich gesetzt hatte", "literal", "καθίσαντος αὐτοῦ", None, None,
  "Sitzend lehrte ein jüdischer Lehrer (vgl. [[MAT.23.2]], [[MAT.26.55]]). Wörtlich ist es eine Genitivkonstruktion («als er sich gesetzt hatte»)."),
 ("MAT.5.2", "er öffnete seinen Mund", "literal", "ἀνοίξας τὸ στόμα αὐτοῦ", None, ["er begann zu reden", "er tat seinen Mund auf"],
  "Feierliche biblische Redeeinleitung (vgl. [[JOB.3.1]], [[ACT.8.35]]). Sie ist wörtlich beibehalten."),
 ("MAT.5.3", "Selig", "traditional", "Μακάριοι", None, ["Glücklich", "Glücklich zu preisen", "Wohl denen", "Beglückwünschen kann man"],
  "Grundentscheid für Matthäus: μακάριος immer «selig» (nach MACULA-Lemma 13-mal im Buch, davon 9-mal in [[MAT.5.3]]–[[MAT.5.11]]), wie in der Johannes-Übersetzung. Die Form der Seligpreisung (Makarismus) beglückwünscht. Sie ist kein Auftrag. Das Griechische hat kein Verb; «sind» ist ergänzt. «Selig» meint hier nicht erst das Jenseits. Das Wort bezeichnet ein Glück, das von Gott zugesprochen wird. «Glücklich» wäre alltagsnäher, klingt aber nach Gefühl oder Zufall."),
 ("MAT.5.3", "die Armen im Geist", "interpretive", "οἱ πτωχοὶ τῷ πνεύματι", "die Armen dem Geist nach", ["die geistlich Armen", "die vor Gott arm sind", "die Armen"],
  "Der Dativ gibt an, worin sie arm sind. Gedeutet wird auf Menschen, die sich vor Gott arm und bedürftig wissen, oder auf die wirtschaftlich Armen und Gedemütigten, die auf Gott hoffen (vgl. die «Elenden» in [[ISA.61.1]], [[PSA.34.19]]). [[LUK.6.20]] sagt nur «die Armen». Nicht gemeint ist geistige Beschränktheit. Die wörtliche Wendung lässt die Deutungen offen. Der Ausdruck kommt sinngemäss auch in den Qumranschriften vor."),
 ("MAT.5.3", "denn ihnen gehört", "adapted", "ὅτι αὐτῶν ἐστιν", "denn ihrer ist", None,
  "Der Genitiv bezeichnet den Besitz. Präsens wie in [[MAT.5.10]], das den Abschnitt rahmt; die Verheissungen dazwischen ([[MAT.5.4]]–[[MAT.5.9]]) stehen im Futur."),
 ("MAT.5.3", "das Reich der Himmel", "literal", "ἡ βασιλεία τῶν οὐρανῶν", "die Königsherrschaft der Himmel", ["das Himmelreich", "die Herrschaft Gottes", "das Reich Gottes"],
  "Grundentscheid für Matthäus (für alle Kapitel gleich): ἡ βασιλεία τῶν οὐρανῶν «das Reich der Himmel», ἡ βασιλεία τοῦ θεοῦ «das Reich Gottes». Matthäus sagt meist «Reich der Himmel», wo Markus und Lukas «Reich Gottes» haben; «Himmel» umschreibt nach jüdischem Sprachgebrauch ehrfürchtig Gott. Der Plural spiegelt das hebräische šāmayim. βασιλεία meint die Königsherrschaft Gottes, nicht in erster Linie ein Gebiet. «Himmelreich» (Luther) würde den Bezug zum «Reich Gottes» verdecken."),
 ("MAT.5.4", "Trauernden", "literal", "οἱ πενθοῦντες", None, ["die Leid tragen", "die Weinenden"],
  "Anklang an [[ISA.61.2]]–[[ISA.61.3]], wo der Gesalbte gesandt ist, «alle Trauernden zu trösten»."),
 ("MAT.5.4", "werden getröstet werden", "literal", "παρακληθήσονται", None, None,
  "Passiv ohne Urheber. In den Seligpreisungen versteht man es meist als Umschreibung für Gottes Handeln (passivum divinum). Ebenso [[MAT.5.6]], [[MAT.5.7]] und [[MAT.5.9]]."),
 ("MAT.5.5", "Sanftmütigen", "literal", "οἱ πραεῖς", None, ["die Sanften", "die Demütigen", "die Gewaltlosen", "die keine Gewalt anwenden"],
  "πραΰς bezeichnet Menschen, die nicht gewaltsam für sich selbst eintreten. Matthäus nennt auch Jesus so ([[MAT.11.29]], [[MAT.21.5]]). Der Vers greift fast wörtlich [[PSA.37.11]] auf (griechische Bibel)."),
 ("MAT.5.5", "die Erde", "interpretive", "τὴν γῆν", None, ["das Land"],
  "In [[PSA.37.11]] ist das verheissene Land gemeint, und γῆ kann «Land» heissen. Bei Matthäus wird die Verheissung meist weiter verstanden. γῆ ist in Kapitel 5 einheitlich «Erde» ([[MAT.5.13]], [[MAT.5.18]], [[MAT.5.35]])."),
 ("MAT.5.6", "nach der Gerechtigkeit hungern und dürsten", "literal", "οἱ πεινῶντες καὶ διψῶντες τὴν δικαιοσύνην", None, ["nach Gerechtigkeit hungern und dürsten", "sich nach Gerechtigkeit sehnen"],
  "Grundentscheid für Matthäus: δικαιοσύνη immer «Gerechtigkeit» (7-mal im Buch: [[MAT.3.15]], [[MAT.5.6]], [[MAT.5.10]], [[MAT.5.20]], [[MAT.6.1]], [[MAT.6.33]], [[MAT.21.32]]). Gedeutet wird das Wort als rechtes Tun nach Gottes Willen (so klar in [[MAT.5.20]] und [[MAT.6.1]]) oder als Gottes rettendes Rechtschaffen, nach dem man sich sehnt. Beides wird vertreten. Die gleichbleibende Wiedergabe lässt die Verbindung der Stellen sichtbar. Das Objekt steht im Akkusativ: Sie verlangen nach der Gerechtigkeit selbst."),
 ("MAT.5.7", "werden Barmherzigkeit erfahren", "adapted", "ἐλεηθήσονται", "werden erbarmt werden", ["werden Erbarmen finden", "Gott wird sich ihrer erbarmen"],
  "Das deutsche Passiv von «sich erbarmen» gibt es nicht; die Umschreibung behält das Wortspiel ἐλεήμονες – ἐλεηθήσονται («Barmherzige – Barmherzigkeit»)."),
 ("MAT.5.8", "die ein reines Herz haben", "adapted", "οἱ καθαροὶ τῇ καρδίᾳ", "die Reinen im Herzen", ["die reinen Herzens sind"],
  "Das Herz steht biblisch für das Innere, Denken und Wollen. Anklang an [[PSA.24.3]]–[[PSA.24.4]]: Wer reinen Herzens ist, darf auf den Berg Gottes steigen."),
 ("MAT.5.9", "die Frieden stiften", "literal", "οἱ εἰρηνοποιοί", "die Friedensmacher", ["die Friedfertigen", "die Friedensstifter"],
  "Gemeint ist das aktive Herstellen von Frieden, nicht nur eine friedliche Gesinnung."),
 ("MAT.5.9", "Söhne Gottes", "literal", "υἱοὶ θεοῦ", None, ["Kinder Gottes"],
  "υἱοί schliesst nach antikem Sprachgebrauch Frauen ein. «Söhne» ist beibehalten, weil Matthäus den Gedanken in [[MAT.5.45]] aufnimmt («Söhne eures Vaters») und die Sohnschaft im Buch ein Leitgedanke ist. «Kinder Gottes» wäre inklusiver."),
 ("MAT.5.11", "meinetwegen", "literal", "ἕνεκεν ἐμοῦ", None, ["um meinetwillen", "weil ihr zu mir gehört"],
  "Hier wechselt die Rede in die zweite Person. Die Verfolgung «wegen der Gerechtigkeit» ([[MAT.5.10]]) wird zur Verfolgung «wegen Jesus»."),
 ("MAT.5.11", "fälschlich", "adapted", "ψευδόμενοι", "lügend", ["lügnerisch", "und dabei lügen", "zu Unrecht"],
  "Das Partizip bestimmt, dass die Vorwürfe falsch sind. «Nachsagen» gibt εἴπωσιν … καθʼ ὑμῶν («sagen gegen euch») wieder."),
 ("MAT.5.12", "jubelt", "literal", "ἀγαλλιᾶσθε", None, ["frohlockt", "jauchzt"], None),
 ("MAT.5.12", "Lohn", "literal", "ὁ μισθὸς", None, ["Belohnung"],
  "Grundentscheid: μισθός «Lohn» (nach MACULA-Lemma 10-mal im Buch). Dieselbe Wiedergabe steht in [[MAT.5.46]] und in [[MAT.6.5]] (TRANS-MAT-006-005-015). Gemeint ist Gottes Zuwendung, nicht ein einklagbarer Anspruch."),
 ("MAT.5.12", "in den Himmeln", "literal", "ἐν τοῖς οὐρανοῖς", None, ["im Himmel"],
  "Der Plural ist beibehalten, wie in «Vater in den Himmeln» ([[MAT.5.16]], [[MAT.6.9]]). Der Singular steht, wo das Griechische ihn hat ([[MAT.5.18]], [[MAT.5.34]])."),
 ("MAT.5.13", "fad wird", "adapted", "μωρανθῇ", "töricht wird", ["salzlos wird", "kraftlos wird", "seinen Geschmack verliert"],
  "μωραίνω heisst eigentlich «töricht werden»; vom Salz gesagt: «fad werden». Viele hören ein Wortspiel: Jünger, die «töricht» werden, verlieren ihre Wirkung. Reines Kochsalz verliert seinen Geschmack nicht; salzhaltige Gemische, wie man sie etwa am Toten Meer gewann, konnten aber unbrauchbar werden. [[MRK.9.50]] sagt ἄναλον («salzlos»)."),
 ("MAT.5.13", "soll es wieder salzig werden", "adapted", "ἁλισθήσεται", "wird es gesalzen werden", ["soll man es salzen", "soll man salzen"],
  "Das Passiv hat kein ausdrückliches Subjekt. Meist bezieht man es auf das Salz selbst; möglich ist auch «womit soll man (die Erde) salzen»."),
 ("MAT.5.13", "den Menschen", "literal", "τῶν ἀνθρώπων", None, ["den Leuten"],
  "Grundentscheid: ἄνθρωποι im Hochdeutschen «die Menschen», wie in TRANS-MAT-006-005-015; in der Mundart meist «d Lüüt»."),
 ("MAT.5.15", "den Scheffel", "traditional", "τὸν μόδιον", None, ["das Gefäss", "den Eimer", "das Kornmass"],
  "μόδιος ist ein Getreidemass von knapp 9 Litern. Der vertraute Ausdruck «Scheffel» ist beibehalten, wie in [[MRK.4.21]]."),
 ("MAT.5.15", "Lampe", "literal", "λύχνον", None, ["Licht", "Leuchte"], "Eine kleine Öllampe aus Ton; «Leuchter» (λυχνία) ist ihr Ständer."),
 ("MAT.5.16", "preisen", "adapted", "δοξάσωσιν", "verherrlichen", ["ehren", "rühmen", "loben"],
  "δοξάζω steht bei Matthäus für den Lobpreis Gottes durch Menschen ([[MAT.9.8]], [[MAT.15.31]]); hier deshalb «preisen». In [[MAT.6.2]] meint das Verb menschliches Ansehen. In der Johannes-Übersetzung ist δοξάζω einheitlich «verherrlichen», weil es dort meist um die Herrlichkeit Gottes und Jesu selbst geht."),
 ("MAT.5.16", "euren Vater in den Himmeln", "literal", "τὸν πατέρα ὑμῶν τὸν ἐν τοῖς οὐρανοῖς", "euren Vater, den in den Himmeln", ["euren Vater im Himmel", "euren himmlischen Vater"],
  "Grundentscheid für Matthäus: ὁ πατὴρ ὁ ἐν (τοῖς) οὐρανοῖς «Vater in den Himmeln» (wie [[MAT.6.9]]), ὁ πατὴρ ὁ οὐράνιος «himmlischer Vater» ([[MAT.5.48]], wie [[MAT.6.14]]). Hier zum ersten Mal im Buch."),
 ("MAT.5.17", "aufzuheben", "literal", "καταλῦσαι", None, ["aufzulösen", "abzuschaffen", "ausser Kraft zu setzen"],
  "καταλύω heisst «auflösen, niederreissen» (vom Tempel in [[MAT.24.2]], [[MAT.26.61]]), vom Gesetz «ausser Kraft setzen»."),
 ("MAT.5.17", "um zu erfüllen", "interpretive", "πληρῶσαι", None, ["um zu vollenden", "um zur vollen Geltung zu bringen", "um ganz zu verwirklichen"],
  "πληρόω ist bei Matthäus das Verb der Erfüllungszitate ([[MAT.1.22]], [[MAT.2.15]] u. ö.; nach MACULA-Lemma 16-mal im Buch). Ob Jesus das Gesetz durch sein Tun erfüllt, es in seiner Lehre zu seinem eigentlichen Sinn führt oder ob gemeint ist, dass sich Gesetz und Propheten in ihm erfüllen, ist umstritten. «Erfüllen» lässt das offen."),
 ("MAT.5.17", "das Gesetz oder die Propheten", "literal", "τὸν νόμον ἢ τοὺς προφήτας", None, ["die Tora oder die Propheten"],
  "Bezeichnung der heiligen Schriften Israels (vgl. [[MAT.7.12]], [[MAT.22.40]]). νόμος ist «Gesetz» wie bei Markus und Johannes; die hebräische tôrā meint mehr: «Weisung»."),
 ("MAT.5.18", "amen", "literal", "ἀμὴν λέγω ὑμῖν", None, ["wahrlich", "ganz gewiss"],
  "Grundentscheid für Matthäus: ἀμὴν λέγω ὑμῖν / σοι «Amen, ich sage euch / dir». Das hebräische Bekräftigungswort steht vor der eigenen Aussage. Diese Redeweise ist in den Evangelien auf Jesus beschränkt. Hier steht γάρ dazwischen («Denn amen …»)."),
 ("MAT.5.18", "Jota", "literal", "ἰῶτα", None, ["Buchstabe"],
  "Der kleinste griechische Buchstabe; er steht wohl für das hebräische Jod, den kleinsten Buchstaben des hebräischen Alphabets."),
 ("MAT.5.18", "Häkchen", "interpretive", "κεραία", "Hörnchen", ["Strichlein", "Tüpfelchen", "Pünktchen"],
  "κεραία ist ein kleiner Strich oder Haken, der hebräische Buchstaben voneinander unterscheidet."),
 ("MAT.5.18", "gewiss nicht", "literal", "οὐ μὴ", "nicht nicht", ["keinesfalls", "niemals"],
  "Die doppelte Verneinung verstärkt. Grundentscheid: οὐ μή «gewiss nicht» (wie in [[MRK.10.15]]); ebenso [[MAT.5.20]] und [[MAT.5.26]]."),
 ("MAT.5.18", "bis alles geschieht", "interpretive", "ἕως ἂν πάντα γένηται", None, ["bis alles erfüllt ist", "bis alles eingetroffen ist"],
  "Gemeint sein kann das Ende der Welt (parallel zu «bis Himmel und Erde vergehen») oder die Erfüllung dessen, was Gesetz und Propheten ankündigen, in Jesu Weg. Die Wiedergabe lässt beides offen."),
 ("MAT.5.19", "auflöst", "literal", "λύσῃ", None, ["aufhebt", "ausser Kraft setzt", "übertritt"],
  "λύω gehört zum Stamm von καταλύω in [[MAT.5.17]]. Gemeint ist, ein Gebot für ungültig zu erklären oder es nicht zu halten."),
 ("MAT.5.19", "der Kleinste genannt werden", "literal", "ἐλάχιστος κληθήσεται", "wird als Kleinster gerufen werden", ["wird der Geringste heissen"],
  "Auch der Kleinste steht noch «im Reich der Himmel». Ausgeschlossen wird er nach dem Wortlaut nicht."),
 ("MAT.5.20", "weit über die der Schriftgelehrten und Pharisäer hinausgeht", "adapted", "περισσεύσῃ πλεῖον τῶν γραμματέων καὶ Φαρισαίων", "überreichlich mehr ist als die der Schriftgelehrten und Pharisäer", ["viel grösser ist als die der Schriftgelehrten und Pharisäer", "die der Schriftgelehrten und Pharisäer übertrifft"],
  "Schriftgelehrte und Pharisäer galten als besonders genau im Halten des Gesetzes. Matthäus setzt sich mit ihnen aus einer innerjüdischen Auseinandersetzung seiner Zeit heraus auseinander. Die Wiedergabe ist neutral und spitzt nicht abwertend zu. Ein Urteil über das Judentum ist damit nicht ausgesprochen. περισσεύω kehrt in [[MAT.5.47]] wieder (περισσόν, «Besonderes»)."),
 ("MAT.5.21", "zu den Alten", "interpretive", "τοῖς ἀρχαίοις", None, ["von den Alten", "den Vorfahren"],
  "Der Dativ meint meist die Empfänger: die Generation am Sinai. «Von den Alten» (Dativ des Urhebers) ist seltener. Das Passiv «gesagt worden ist» nennt keinen Sprecher; gemeint ist die überlieferte Weisung der Schrift."),
 ("MAT.5.21", "Du sollst nicht töten", "literal", "Οὐ φονεύσεις", None, ["Du sollst nicht morden"],
  "[[EXO.20.13]], [[DEU.5.17]]; Wortlaut wie in [[MRK.10.19]]. φονεύω meint das widerrechtliche Töten eines Menschen. Der Zusatz «wer aber tötet, wird dem Gericht verfallen» steht so nicht im Alten Testament und fasst Bestimmungen wie [[EXO.21.12]] zusammen."),
 ("MAT.5.21", "dem Gericht verfallen", "adapted", "ἔνοχος ἔσται τῇ κρίσει", "schuldig sein wird dem Gericht", ["sich vor Gericht verantworten müssen", "dem Urteil verfallen"],
  "ἔνοχος ist ein Rechtsbegriff: «haftbar, verfallen». κρίσις kann hier das örtliche Gericht meinen; in der Steigerung von [[MAT.5.22]] (Gericht – Hoher Rat – Hölle) klingt auch Gottes Gericht an."),
 ("MAT.5.22", "Ich aber sage euch", "literal", "ἐγὼ δὲ λέγω ὑμῖν", None, None,
  "Mit betontem ἐγώ stellt Jesus sechsmal dem Überlieferten sein eigenes Wort gegenüber ([[MAT.5.21]]–[[MAT.5.48]]; «Antithesen»). Ob er damit die Tora überbietet, sie gegen bestimmte Auslegungen auslegt oder ihren Sinn verschärft, ist umstritten. [[MAT.5.17]] schliesst die Aufhebung aus."),
 ("MAT.5.22", "Bruder", "literal", "τῷ ἀδελφῷ", None, ["Mitmenschen", "Bruder oder Schwester"],
  "ἀδελφός meint hier den Mitmenschen in der Glaubensgemeinschaft, Frauen eingeschlossen. Die wörtliche Wiedergabe ist beibehalten; ebenso [[MAT.5.23]]–[[MAT.5.24]] und [[MAT.5.47]]."),
 ("MAT.5.22", "Raka", "literal", "Ῥακά", None, ["Hohlkopf", "Dummkopf"],
  "Aramäisches Schimpfwort (wohl rēqā, «Leerer, Hohlkopf»), im Griechischen umschrieben. Die Übersetzung behält das Fremdwort wie der griechische Text."),
 ("MAT.5.22", "dem Hohen Rat", "adapted", "τῷ συνεδρίῳ", "dem Synedrium", ["dem Synedrium", "dem Sanhedrin", "dem Rat"],
  "συνέδριον ist der oberste jüdische Gerichtshof in Jerusalem (so [[MAT.26.59]]), kann aber auch ein örtliches Ratsgericht meinen (vgl. [[MAT.10.17]])."),
 ("MAT.5.22", "Du Narr", "literal", "Μωρέ", None, ["Du Dummkopf", "Du Idiot"],
  "Griechischer Vokativ von μωρός «töricht». Vermutet wird zudem ein Anklang an hebräisch môreh («widerspenstig», vgl. [[NUM.20.10]])."),
 ("MAT.5.22", "dem Feuer der Hölle", "traditional", "εἰς τὴν γέενναν τοῦ πυρός", "in die Gehenna des Feuers", ["dem Höllenfeuer", "der Feuer-Gehenna", "dem Gehenna-Feuer"],
  "Grundentscheid: γέεννα «Hölle» (nach MACULA-Lemma 7-mal im Buch), wie in [[MRK.9.43]]. Das Wort kommt von hebräisch gê hinnōm, dem Tal Hinnom bei Jerusalem, das als Ort von Kinderopfern verflucht war ([[JER.7.31]]–[[JER.7.32]]) und zum Bild für den Ort des endgültigen Gerichts wurde. Es ist nicht dasselbe wie ᾅδης, das Totenreich ([[MAT.11.23]]). εἰς («bis in, in») ist in «verfallen» aufgenommen."),
 ("MAT.5.23", "Gabe", "literal", "τὸ δῶρόν", None, ["Opfergabe", "Opfer"],
  "Gemeint ist ein Opfer im Tempel in Jerusalem; der Text setzt voraus, dass der Tempel noch besteht."),
 ("MAT.5.25", "Einige dich schnell", "adapted", "ἴσθι εὐνοῶν ταχὺ", "sei wohlgesinnt schnell", ["Komm deinem Gegner rasch entgegen", "Vertrag dich bald"],
  "εὐνοέω heisst «wohlgesinnt sein»; im Zusammenhang eines Rechtsstreits ist die gütliche Einigung gemeint."),
 ("MAT.5.25", "Gegner", "literal", "τῷ ἀντιδίκῳ", None, ["Prozessgegner", "Ankläger", "Gläubiger"],
  "ἀντίδικος ist die Gegenpartei vor Gericht; das Gefängnis bis zur Bezahlung ([[MAT.5.26]]) lässt an Schuldhaft denken."),
 ("MAT.5.25", "Gerichtsdiener", "literal", "τῷ ὑπηρέτῃ", None, ["Amtsdiener", "Gerichtsvollzieher", "Wächter"], None),
 ("MAT.5.26", "Rappen", "adapted", "κοδράντην", "Quadrans", ["Quadrans", "Groschen", "Pfennig", "Cent"],
  "Der quadrans war die kleinste römische Münze (ein Viertel As, vgl. [[MRK.12.42]]). «Rappen», die kleinste Schweizer Münzeinheit, gibt den Sinn «bis auf den letzten Rest» für die Zielgruppe (de-CH) wieder; redaktionelle Entscheidung."),
 ("MAT.5.27", "Du sollst nicht ehebrechen", "literal", "Οὐ μοιχεύσεις", None, ["Du sollst nicht die Ehe brechen"],
  "[[EXO.20.14]], [[DEU.5.18]]; Wortlaut wie in [[MRK.10.19]]. Sonst steht in Kapitel 5 «die Ehe brechen»."),
 ("MAT.5.28", "eine Frau", "interpretive", "γυναῖκα", None, ["eine verheiratete Frau", "die Frau eines anderen"],
  "γυνή heisst «Frau» und «Ehefrau». Im Zusammenhang mit dem Ehebruchgebot und dem Verbot, die Frau des Nächsten zu begehren ([[EXO.20.17]]), denken viele an eine verheiratete Frau."),
 ("MAT.5.28", "um sie zu begehren", "interpretive", "πρὸς τὸ ἐπιθυμῆσαι αὐτὴν", None, ["und sie begehrt", "so dass er sie begehrt"],
  "πρὸς τό mit Infinitiv bezeichnet meist den Zweck: ein absichtliches, begehrliches Ansehen, nicht das blosse Sehen. ἐπιθυμέω ist das Verb von [[EXO.20.17]] in der griechischen Bibel (οὐκ ἐπιθυμήσεις)."),
 ("MAT.5.29", "zu Fall bringt", "adapted", "σκανδαλίζει", "zum Anstoss wird", ["zur Sünde verführt", "ärgert", "zum Stolperstein wird"],
  "Grundentscheid für Matthäus: σκανδαλίζω «zu Fall bringen» (nach MACULA-Lemma 14-mal im Buch), wie in [[MRK.9.43]]–[[MRK.9.47]]; wo es um innere Abwendung geht (z. B. [[MAT.11.6]], [[MAT.26.31]]), mit eigener Entscheidung. σκάνδαλον ist ursprünglich das Stellholz einer Falle, dann ein Stolperstein. «Ärgern» (Luther) ist heute missverständlich."),
 ("MAT.5.29", "reiss es heraus", "literal", "ἔξελε αὐτὸν", None, None,
  "Die harte Bildrede ist wörtlich wiedergegeben. Meist wird sie als bewusste Übertreibung verstanden, die zur radikalen Abkehr vom Bösen ruft, nicht als Anweisung zur Selbstverstümmelung."),
 ("MAT.5.29", "Leib", "literal", "σῶμά", None, ["Körper"], None),
 ("MAT.5.31", "einen Scheidebrief", "literal", "ἀποστάσιον", None, ["eine Scheidungsurkunde"],
  "Nach [[DEU.24.1]] gibt der Mann der Frau eine Urkunde, die sie frei macht, wieder zu heiraten. Wortlaut wie in [[MRK.10.4]]."),
 ("MAT.5.31", "entlässt", "literal", "ἀπολύσῃ", None, ["sich scheiden lässt von", "verstösst", "wegschickt"],
  "Nach damaligem jüdischem Recht konnte in der Regel nur der Mann die Scheidung aussprechen. «Entlassen» gibt das Wort wieder wie in [[MRK.10.11]]."),
 ("MAT.5.32", "ausser wegen Unzucht", "interpretive", "παρεκτὸς λόγου πορνείας", "ausser aufgrund einer Sache von Unzucht", ["ausser bei Ehebruch", "ausser bei sexueller Untreue", "ausser bei einer unerlaubten Ehe"],
  "Die Ausnahme steht nur bei Matthäus (vgl. [[MAT.19.9]]); [[MRK.10.11]] und [[LUK.16.18]] haben sie nicht. πορνεία ist weiter als «Ehebruch» (μοιχεία) und meint unerlaubte sexuelle Beziehungen allgemein; manche beziehen es auf Ehen in verbotenem Verwandtschaftsgrad (vgl. [[LEV.18.6]]–[[LEV.18.18]], [[ACT.15.20]]). λόγος πορνείας erinnert an die umstrittene Wendung «etwas Schändliches» in [[DEU.24.1]], über die die Schulen Schammais und Hillels stritten. «Unzucht» ist die vertraute, etwas altertümliche Wiedergabe, die die Weite des Begriffs erhält."),
 ("MAT.5.32", "macht, dass mit ihr die Ehe gebrochen wird", "literal", "ποιεῖ αὐτὴν μοιχευθῆναι", None, ["macht sie zur Ehebrecherin", "treibt sie in den Ehebruch"],
  "Der Infinitiv ist passiv. Der Satz setzt voraus, dass die entlassene Frau wieder heiratet; die Verantwortung liegt beim Mann, der sie entlässt."),
 ("MAT.5.33", "keinen Meineid schwören", "literal", "Οὐκ ἐπιορκήσεις", None, ["nicht falsch schwören", "deinen Eid nicht brechen"],
  "Zusammenfassung von Weisungen wie [[LEV.19.12]], [[NUM.30.3]] und [[DEU.23.22]]; ἐπιορκέω kann den falschen Eid und den gebrochenen Eid meinen."),
 ("MAT.5.33", "dem Herrn", "traditional", "τῷ κυρίῳ", None, None,
  "κύριος gibt in der griechischen Bibel den Gottesnamen JHWH wieder; die Übersetzung folgt dem vertrauten «Herr»."),
 ("MAT.5.34", "Ihr sollt überhaupt nicht schwören", "literal", "μὴ ὀμόσαι ὅλως", "nicht zu schwören überhaupt", ["Schwört überhaupt nicht"],
  "Der Infinitiv hängt von «ich sage euch» ab; die Übersetzung gibt ihn als Gebot wieder. Ebenso [[MAT.5.39]]."),
 ("MAT.5.35", "der Schemel seiner Füsse", "literal", "ὑποπόδιόν τῶν ποδῶν αὐτοῦ", None, ["sein Fussschemel"],
  "Nach [[ISA.66.1]]; «die Stadt des grossen Königs» nach [[PSA.48.3]] (in manchen Bibeln 48,2)."),
 ("MAT.5.37", "«Ja, ja», «nein, nein»", "interpretive", "ναὶ ναί, οὒ οὔ", None, ["Euer Ja sei ein Ja, euer Nein ein Nein", "Ja sei Ja, Nein sei Nein"],
  "Die Verdoppelung kann bekräftigen («ja, gewiss») oder bedeuten, dass ein Ja ein Ja bleibt (so [[JAS.5.12]]). Die wörtliche Wiedergabe lässt beides offen."),
 ("MAT.5.37", "vom Bösen", "interpretive", "ἐκ τοῦ πονηροῦ", None, ["vom Bösen (dem Teufel)", "aus dem Bösen", "vom Übel"],
  "τοῦ πονηροῦ kann männlich («vom Bösen», dem Teufel, vgl. [[MAT.13.19]]) oder sächlich («vom Bösen, vom Übel») sein. Die deutsche Wendung lässt beides offen, wie «vor dem Bösen» in [[MAT.6.13]] (TRANS-MAT-006-005-015)."),
 ("MAT.5.38", "Auge um Auge", "literal", "Ὀφθαλμὸν ἀντὶ ὀφθαλμοῦ", "Auge anstelle von Auge", ["Auge für Auge"],
  "Rechtssatz aus [[EXO.21.24]], [[LEV.24.20]], [[DEU.19.21]]. Er begrenzte die Vergeltung auf das Mass des Schadens und wurde zur Zeit Jesu meist in Geldersatz umgesetzt."),
 ("MAT.5.39", "dem Bösen nicht widerstehen", "interpretive", "μὴ ἀντιστῆναι τῷ πονηρῷ", None, ["dem, der euch Böses tut, nicht Widerstand leisten", "euch dem Bösen nicht entgegenstellen", "nicht Böses mit Bösem vergelten"],
  "τῷ πονηρῷ kann «dem Bösen» (dem bösen Menschen) oder «dem Bösen» (dem Übel) heissen; die Beispiele danach sprechen von Menschen, die einem Unrecht tun. ἀνθίστημι kann auch den Widerstand vor Gericht meinen (vgl. [[MAT.5.40]]). Ob gewaltloser Widerstand mitgemeint oder ausgeschlossen ist, ist umstritten; die wörtliche Wiedergabe entscheidet es nicht."),
 ("MAT.5.39", "schlägt", "literal", "ῥαπίζει", None, ["ohrfeigt"],
  "Ein Schlag auf die rechte Wange ist für Rechtshänder ein Schlag mit dem Handrücken, eine Beleidigung mehr als eine Verletzung."),
 ("MAT.5.40", "vor Gericht gehen", "adapted", "κριθῆναι", "gerichtet werden, prozessieren", ["prozessieren", "einen Rechtsstreit führen"], None),
 ("MAT.5.40", "Hemd", "adapted", "τὸν χιτῶνά", "Untergewand", ["Untergewand", "Rock", "Leibrock"],
  "χιτών ist das Untergewand, ἱμάτιον («Mantel») das Obergewand, das nach [[EXO.22.25]]–[[EXO.22.26]] nicht über Nacht gepfändet werden durfte, weil es Armen als Decke diente."),
 ("MAT.5.41", "zwingt, eine Meile mitzugehen", "interpretive", "ἀγγαρεύσει μίλιον ἕν", None, ["zu einer Meile Frondienst zwingt"],
  "ἀγγαρεύω bezeichnet das Recht von Soldaten und Beamten, Einheimische zu Trägerdiensten heranzuziehen (vgl. [[MAT.27.32]], Simon von Kyrene). Die römische Meile (μίλιον) mass knapp 1,5 Kilometer."),
 ("MAT.5.42", "borgen", "literal", "δανίσασθαι", None, ["leihen"], None),
 ("MAT.5.43", "deinen Feind hassen", "literal", "μισήσεις τὸν ἐχθρόν σου", None, None,
  "«Du sollst deinen Nächsten lieben» ist [[LEV.19.18]]; der zweite Teil steht so nicht im Alten Testament. Ob er eine verbreitete Folgerung aufnimmt (vgl. die Gemeinderegel von Qumran, die zum Hass auf die «Söhne der Finsternis» auffordert) oder zugespitzt formuliert ist, wird diskutiert."),
 ("MAT.5.43", "Nächsten", "literal", "τὸν πλησίον", None, None, "Wortlaut wie in [[MRK.12.31]]."),
 ("MAT.5.45", "werdet", "literal", "γένησθε", None, ["euch erweist als", "seid"],
  "Gotteskindschaft erscheint hier als etwas, das im Handeln Gestalt gewinnt; vgl. [[MAT.5.9]]."),
 ("MAT.5.46", "Zöllner", "traditional", "οἱ τελῶναι", None, ["Zolleinnehmer", "Steuereintreiber"],
  "Pächter oder Angestellte, die Zölle eintrieben; sie galten als unehrlich und als Mitarbeiter der Fremdherrschaft. Matthäus selbst ist nach [[MAT.10.3]] ein Zöllner."),
 ("MAT.5.47", "grüsst", "literal", "ἀσπάσησθε", None, None,
  "Grüssen meint mehr als eine Höflichkeitsformel: den Friedenswunsch und die Anerkennung als Zugehörige."),
 ("MAT.5.47", "Besonderes", "adapted", "περισσὸν", "Überschüssiges", ["Aussergewöhnliches", "mehr als die anderen"],
  "Das Wort nimmt περισσεύω aus [[MAT.5.20]] auf: die Gerechtigkeit, die «weit hinausgeht»."),
 ("MAT.5.47", "die Heiden", "traditional", "οἱ ἐθνικοὶ", None, ["die Nichtjuden", "die Leute aus den Völkern"],
  "ἐθνικός «zu den Völkern gehörig»: aus jüdischer Sicht die Nichtjuden. Wiedergabe wie in [[MAT.6.7]] (TRANS-MAT-006-005-015) und [[MAT.18.17]]."),
 ("MAT.5.48", "Ihr sollt also vollkommen sein", "interpretive", "Ἔσεσθε οὖν ὑμεῖς τέλειοι", "Ihr werdet also vollkommen sein", ["Ihr werdet vollkommen sein", "Seid ganz", "Seid ungeteilt"],
  "Das Futur steht wie in den Geboten der griechischen Bibel für einen Auftrag (vgl. [[MAT.5.43]]); als Verheissung («ihr werdet») kann es auch gelesen werden. τέλειος heisst «ganz, vollständig, reif» und gibt in der griechischen Bibel hebräisch tāmîm wieder ([[DEU.18.13]]: «ganz sollst du sein mit dem HERRN»). Gemeint ist im Zusammenhang die ungeteilte Liebe, die auch den Feind einschliesst; [[LUK.6.36]] sagt «barmherzig». Vgl. [[LEV.19.2]]."),
 ("MAT.5.48", "himmlischer Vater", "literal", "ὁ πατὴρ ὁ οὐράνιος", None, ["Vater im Himmel"],
  "οὐράνιος nach MACULA-Lemma 7-mal im Buch, immer vom Vater. Siehe [[MAT.5.16]]."),
]

DEC_GSW = [
 ("MAT.5.1", "d Mängi", "adapted", "τοὺς ὄχλους", "d Mängine", None, "Griechisch Plural; i de Mundart Einzahl."),
 ("MAT.5.1", "abgsässe", "literal", "καθίσαντος", None, None, "En jüdische Lehrer hät im Sitze gleert."),
 ("MAT.5.3", "Sälig", "traditional", "Μακάριοι", None, ["Glücklich", "Wohl dene"],
  "Grundentscheid für Matthäus: μακάριος immer «sälig» (wie bi de Johannes-Übersetzig). D Säligpriisig wünscht Glück und spricht s zue; si isch kei Uftrag. «sind» isch ergänzt."),
 ("MAT.5.3", "di Arme im Geischt", "interpretive", "οἱ πτωχοὶ τῷ πνεύματι", None, ["die, wo vor Gott arm sind", "di Arme"],
  "Gmeint sind Mänsche, wo sich vor Gott arm und bedürftig wüssed, oder di Arme und Plaagete, wo uf Gott hoffed ([[ISA.61.1]]); [[LUK.6.20]] seit nu «di Arme»."),
 ("MAT.5.3", "s Riich vo de Himel", "literal", "ἡ βασιλεία τῶν οὐρανῶν", None, ["s Himmelriich", "s Riich vo Gott"],
  "Grundentscheid für Matthäus: «s Riich vo de Himel»; ἡ βασιλεία τοῦ θεοῦ «s Riich vo Gott». «Himel» umschriibt ehrfürchtig Gott."),
 ("MAT.5.4", "wo truured", "literal", "οἱ πενθοῦντες", None, None, "Aaklang a [[ISA.61.2]]."),
 ("MAT.5.5", "d Ärde", "interpretive", "τὴν γῆν", None, ["s Land"], "I [[PSA.37.11]] isch s verheisse Land gmeint; bi Matthäus wird s meist wiiter verstande."),
 ("MAT.5.6", "Grächtigkeit", "literal", "δικαιοσύνην", None, None,
  "Grundentscheid für Matthäus: δικαιοσύνη immer «Grächtigkeit» (7-mal im Buech): rächts Tue nach Gottes Wille oder Gottes rettendi Grächtigkeit; beides wird vertrette."),
 ("MAT.5.9", "Söhn vo Gott", "literal", "υἱοὶ θεοῦ", None, ["Chind vo Gott"], "Wie [[MAT.5.45]]; Fraue sind mitgmeint."),
 ("MAT.5.11", "wäge mir", "literal", "ἕνεκεν ἐμοῦ", None, None, None),
 ("MAT.5.12", "Loon", "literal", "ὁ μισθὸς", None, None, "Wie i [[MAT.6.5]] (TRANS-MAT-006-005-015-GSW-ZH-WORKING)."),
 ("MAT.5.13", "fad wird", "adapted", "μωρανθῇ", "dumm wird", None,
  "μωραίνω heisst eigentli «tumm wärde»; vom Salz gseit: «fad wärde». Vili ghöred es Wortspiil."),
 ("MAT.5.13", "de Lüüt", "literal", "τῶν ἀνθρώπων", "de Mänsche", None, "Grundentscheid: ἄνθρωποι i de Mundart meist «d Lüüt», wie i TRANS-MAT-006-005-015-GSW-ZH-WORKING."),
 ("MAT.5.15", "de Schäffel", "traditional", "τὸν μόδιον", None, ["s Gfäss"], "Es Getreidemass vo chnapp 9 Liter; wie [[MRK.4.21]]."),
 ("MAT.5.16", "priised", "adapted", "δοξάσωσιν", "verherrliched", ["ehred", "lobed"], "Bi Matthäus s Verb fürs Lob vo Gott ([[MAT.9.8]], [[MAT.15.31]])."),
 ("MAT.5.16", "eue Vatter i de Himel", "literal", "τὸν πατέρα ὑμῶν τὸν ἐν τοῖς οὐρανοῖς", None, None,
  "Grundentscheid für Matthäus: «Vatter i de Himel», ὁ οὐράνιος «himmlisch» ([[MAT.5.48]]), wie im Vaterunser ([[MAT.6.9]], [[MAT.6.14]])."),
 ("MAT.5.17", "zum Erfülle", "interpretive", "πληρῶσαι", None, ["zum Vollände", "zum ganz Verwürkliche"],
  "Öb de Jesus s Gsetz mit sim Tue erfüllt, es i sinere Lehr zu sim eigetliche Sinn füert oder öb sich Gsetz und Prophete in ihm erfülled, isch umstritte."),
 ("MAT.5.18", "Hääggli", "interpretive", "κεραία", "Hörnli", ["Strichli", "Tüpfli"], "En chliine Strich, wo hebräischi Buechstabe vonenand underscheidet. S Jota isch de chliinscht griechisch Buechstabe."),
 ("MAT.5.18", "sicher nöd", "literal", "οὐ μὴ", "nöd nöd", None, "Doppleti Verneinig als Verstärchig; wie [[MRK.10.15]]."),
 ("MAT.5.20", "die vo de Schriftgelehrti und Pharisäer", "literal", "τῶν γραμματέων καὶ Φαρισαίων", None, None,
  "Neutral widergää; Matthäus redt us ere innerjüdische Uusenandersetzig vo sinere Ziit."),
 ("MAT.5.21", "em Gricht verfalle sii", "adapted", "ἔνοχος ἔσται τῇ κρίσει", "schuldig sii em Gricht", None, "ἔνοχος isch en Rächtsbegriff: «haftbar, verfalle»."),
 ("MAT.5.22", "Raka", "literal", "Ῥακά", None, ["Hohlchopf"], "Aramäischs Schimpfwort (wahrschiinli «Läärchopf»), im Griechische umschribe."),
 ("MAT.5.22", "em Hoche Raat", "adapted", "τῷ συνεδρίῳ", None, ["em Synedrium"], "De oberscht jüdisch Grichtshof z Jerusalem oder es örtlichs Ratsgricht."),
 ("MAT.5.22", "Du Tubel", "adapted", "Μωρέ", "Du Tumme", ["Du Narr", "Du Löli"],
  "μωρέ isch es grobs Schimpfwort («Tumme»); «Tubel» isch s gläufig züritüütsch Wort für so öppis."),
 ("MAT.5.22", "em Füür vo de Höll", "traditional", "εἰς τὴν γέενναν τοῦ πυρός", "i d Gehenna vom Füür", None,
  "Grundentscheid: γέεννα «Höll», wie [[MRK.9.43]]. S Wort chunnt vom Tal Hinnom bi Jerusalem ([[JER.7.31]]); es isch zum Bild für de Ort vom letschte Gricht worde."),
 ("MAT.5.23", "Gschänk", "literal", "τὸ δῶρόν", None, ["Opfergab"], "Es Opfer im Tämpel."),
 ("MAT.5.25", "Einig di", "adapted", "ἴσθι εὐνοῶν", "sig guet gsinnt", None, None),
 ("MAT.5.26", "Rappe", "adapted", "κοδράντην", "Quadrans", None, "Di chliinscht römisch Münz; «Rappe» seit, was gmeint isch: bis ufs Letscht."),
 ("MAT.5.29", "zu Fall bringt", "adapted", "σκανδαλίζει", "zum Aastoss wird", None,
  "Grundentscheid für Matthäus: σκανδαλίζω «zu Fall bringe», wie [[MRK.9.43]]–[[MRK.9.47]]."),
 ("MAT.5.32", "ussert wäge Unzucht", "interpretive", "παρεκτὸς λόγου πορνείας", None, ["ussert bi Ebruch", "ussert bi sexueller Untreui"],
  "D Usnaam staat nu bi Matthäus (vgl. [[MAT.19.9]]); πορνεία isch wiiter als «Ebruch» und meint uverlaubti sexuelli Beziehige allgemein."),
 ("MAT.5.32", "macht, dass mit ire d Ee broche wird", "literal", "ποιεῖ αὐτὴν μοιχευθῆναι", None, ["macht si zur Ebrächerin"],
  "Passiv; de Satz setzt voruus, dass di entlasse Frau wider hüratet."),
 ("MAT.5.33", "Meineid schwöre", "literal", "ἐπιορκήσεις", None, ["falsch schwöre"], None),
 ("MAT.5.37", "vom Bööse", "interpretive", "ἐκ τοῦ πονηροῦ", None, None, "Männlich (de Bös, de Tüüfel) oder sächlich (s Bös) möglich; wie im Vaterunser ([[MAT.6.13]])."),
 ("MAT.5.39", "em Bööse nöd widerstaa", "interpretive", "μὴ ἀντιστῆναι τῷ πονηρῷ", None, ["däm, wo eu Bööses tuet, kei Widerstand leischte"],
  "τῷ πονηρῷ cha de bös Mänsch oder s Bös meine; d Biispil drnaa redet vo Mänsche, wo eim Urächt tüend."),
 ("MAT.5.39", "Bagge", "literal", "σιαγόνα", None, None, "En Schlag uf de rächt Bagge isch für Rächtshänder en Schlag mit em Handrugge, e Beleidigung."),
 ("MAT.5.40", "Hemd", "adapted", "τὸν χιτῶνά", "Undergwand", None, "χιτών isch s Undergwand, ἱμάτιον de Mantel (s Obergwand)."),
 ("MAT.5.41", "zwingt", "interpretive", "ἀγγαρεύσει", None, None, "Soldate händ Iiheimischi zu Trägerdienscht chöne zwinge (vgl. [[MAT.27.32]]); e römischi Meile isch öppe 1,5 Kilometer."),
 ("MAT.5.43", "din Find hasse", "literal", "μισήσεις τὸν ἐχθρόν σου", None, None, "De zweit Teil staat so nöd im Alte Teschtament ([[LEV.19.18]])."),
 ("MAT.5.46", "d Zöllner", "traditional", "οἱ τελῶναι", None, None, None),
 ("MAT.5.47", "d Heide", "traditional", "οἱ ἐθνικοὶ", None, ["d Nichtjude"], "Wie [[MAT.6.7]]."),
 ("MAT.5.48", "Ir söled also vollkomme sii", "interpretive", "Ἔσεσθε οὖν ὑμεῖς τέλειοι", "Ir wärded also vollkomme sii", ["Sind ganz"],
  "S Futur staat wie i de Gebot für en Uftrag; τέλειος heisst «ganz, vollständig» ([[DEU.18.13]]). [[LUK.6.36]] seit «barmhärzig»."),
]

# Lesarten, die die Übersetzung verändern: (Lesart, Stelle, de von, de zu, gsw von, gsw zu, Wirkung, Hinweis de, Hinweis gsw,
#  Wörter {Lesart: [(griechisch, de, Hinweis)]}, Wörter gsw, Entstehung de, Entstehung gsw)
AUTO = "Laut der automatischen Zuordnung (WREAD-CNTR-MAT-005-001-048)"
AUTO_G = "Nach de automatische Zueornig"
ALTS = [
 ("VAR-SBLGNTAPP-MAT-005-011-01:R2", "MAT.5.11", "alles Böse", "jedes böse Wort", "alles Bööse", "jedes bööse Wort", "gering",
  "Mit ῥῆμα («Wort») ist ausdrücklich von böser Nachrede die Rede.", "Mit ῥῆμα («Wort») isch usdrücklich vo bööser Nachred d Red.",
  {"R1": [("πονηρὸν", "Böses", "SBLGNT, WH, Treg, NA28")], "R2": [("πονηρὸν ῥῆμα", "böses Wort", "RP")]},
  {"R1": [("πονηρὸν", "Bööses", "SBLGNT, WH, Treg, NA28")], "R2": [("πονηρὸν ῥῆμα", "bööses Wort", "RP")]},
  ["Der Zusatz kann verdeutlichen, dass es um Worte geht (εἴπωσιν «sagen»); ebenso kann ῥῆμα beim Abschreiben ausgefallen sein.",
   AUTO + " lesen 01 und 03 ohne Zusatz, 04 und 032 mit ῥῆμα. 05 hat die Zuordnung keiner der beiden Lesarten zugewiesen; der dort erfasste Wortlaut weicht in der Wortfolge ab."],
  ["De Zuesatz cha verdüütliche, dass es um Wort gaat; gliich guet cha ῥῆμα bim Abschriibe usgfalle sii.",
   AUTO_G + " läsed 01 und 03 ohni Zuesatz, 04 und 032 mit ῥῆμα; 05 hät si keinere Läsart zueteilt."]),
 ("VAR-SBLGNTAPP-MAT-005-022-01:R2", "MAT.5.22", "Jeder, der seinem Bruder zürnt", "Jeder, der seinem Bruder ohne Grund zürnt",
  "Jede, wo uf sin Brüeder wüetig isch", "Jede, wo ohni Grund uf sin Brüeder wüetig isch", "bedeutsam",
  "Mit εἰκῇ («ohne Grund») ist nicht jeder Zorn verurteilt, sondern nur grundloser Zorn.",
  "Mit εἰκῇ («ohni Grund») isch nöd jede Zorn verurteilt, sondern nu de grundlos.",
  {"R1": [("αὐτοῦ", "seinem Bruder (ohne Zusatz)", "SBLGNT, WH, NA28")], "R2": [("αὐτοῦ εἰκῇ", "seinem Bruder ohne Grund", "Treg, RP")]},
  {"R1": [("αὐτοῦ", "sim Brüeder (ohni Zuesatz)", "SBLGNT, WH, NA28")], "R2": [("αὐτοῦ εἰκῇ", "sim Brüeder ohni Grund", "Treg, RP")]},
  ["Der Zusatz kann die harte Forderung abgemildert haben, damit sie zu berechtigtem Zorn passt (vgl. Jesu Zorn in [[MRK.3.5]], [[EPH.4.26]]).",
   "Umgekehrt könnte das Wort gestrichen worden sein, um die Forderung zu verschärfen oder weil es überflüssig schien.",
   AUTO + " lesen 01 und 03 ohne Zusatz, 05 und 032 mit εἰκῇ. 04 ist an dieser Stelle nicht erhalten."],
  ["De Zuesatz cha di hert Forderig abgschwächt ha, demit si zu berächtigtem Zorn passt (vgl. [[MRK.3.5]], [[EPH.4.26]]).",
   "Umgekeert chönnt s Wort gstriche worde sii, zum d Forderig verschärfe.",
   AUTO_G + " läsed 01 und 03 ohni Zuesatz, 05 und 032 mit εἰκῇ. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-025-02:R2", "MAT.5.25", "und der Richter dem Gerichtsdiener", "und der Richter dich dem Gerichtsdiener übergibt",
  "und de Richter em Gerichtsdiener", "und de Richter dich em Gerichtsdiener übergit", "gering",
  "Der Zusatz wiederholt das Verb des ersten Satzteils; am Sinn ändert sich nichts.",
  "De Zuesatz widerholt s Verb vom erschte Satzteil; am Sinn änderet sich nüüt.",
  {"R1": [("κριτὴς", "der Richter", "SBLGNT, WH, NA28")], "R2": [("κριτὴς σε παραδῷ", "der Richter dich übergibt", "Treg, RP")]},
  {"R1": [("κριτὴς", "de Richter", "SBLGNT, WH, NA28")], "R2": [("κριτὴς σε παραδῷ", "de Richter dich übergit", "Treg, RP")]},
  ["Der Zusatz kann die knappe Ausdrucksweise geglättet haben; ebenso kann er wegen der Wiederholung desselben Verbs ausgefallen sein.",
   AUTO + " lesen 01 und 03 ohne Zusatz, 05 und 032 mit ihm. 04 ist an dieser Stelle nicht erhalten."],
  ["De Zuesatz cha di chnapp Usdrucksiis glättet ha; oder er isch wäge de Widerholig usgfalle.",
   AUTO_G + " läsed 01 und 03 ohni Zuesatz, 05 und 032 mit. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-030-01:R2", "MAT.5.30", "in die Hölle kommt", "in die Hölle geworfen wird", "i d Höll chunnt", "i d Höll gworfe wird", "gering",
  "Statt «kommt» steht wie in [[MAT.5.29]] «geworfen wird».", "Statt «chunnt» staat wie i [[MAT.5.29]] «gworfe wird».",
  {"R1": [("εἰς γέενναν ἀπέλθῃ", "in die Hölle kommt", "SBLGNT, WH, Treg, NA28")], "R2": [("βληθῇ εἰς γέενναν", "in die Hölle geworfen wird", "RP")]},
  {"R1": [("εἰς γέενναν ἀπέλθῃ", "i d Höll chunnt", "SBLGNT, WH, Treg, NA28")], "R2": [("βληθῇ εἰς γέενναν", "i d Höll gworfe wird", "RP")]},
  ["Die Lesart mit βληθῇ gleicht den Vers an [[MAT.5.29]] an; dass umgekehrt ein Schreiber bewusst abwechselte, ist weniger naheliegend.",
   AUTO + " lesen 01 und 03 ἀπέλθῃ, 032 βληθῇ. 04 und 05 sind an dieser Stelle nicht erhalten."],
  ["D Läsart mit βληθῇ gliicht de Vers a [[MAT.5.29]] aa.",
   AUTO_G + " läsed 01 und 03 ἀπέλθῃ, 032 βληθῇ. 04 und 05 sind a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-032-01:R2", "MAT.5.32", "Jeder, der seine Frau entlässt", "Wer seine Frau entlässt", "Jede, wo sini Frau entlaat", "Wer sini Frau entlaat", "gering",
  "Die Aussage bleibt dieselbe; nur die Satzform wechselt.", "D Ussag bliibt di gliich; nu d Satzform wächslet.",
  {"R1": [("πᾶς ὁ ἀπολύων", "jeder, der entlässt", "SBLGNT, WH, Treg, NA28")], "R2": [("ὃς ἂν ἀπολύσῃ", "wer entlässt", "RP")]},
  {"R1": [("πᾶς ὁ ἀπολύων", "jede, wo entlaat", "SBLGNT, WH, Treg, NA28")], "R2": [("ὃς ἂν ἀπολύσῃ", "wer entlaat", "RP")]},
  ["ὃς ἂν ἀπολύσῃ entspricht [[MAT.5.31]] und [[MAT.19.9]] und kann daran angeglichen sein; umgekehrt kann πᾶς ὁ an die Reihe in [[MAT.5.22]] und [[MAT.5.28]] angeglichen sein.",
   AUTO + " lesen 01, 03 und 032 πᾶς ὁ ἀπολύων, 05 ὃς ἂν ἀπολύσῃ. 04 ist an dieser Stelle nicht erhalten."],
  ["ὃς ἂν ἀπολύσῃ entspricht [[MAT.5.31]] und [[MAT.19.9]]; umgekeert cha πᾶς ὁ a [[MAT.5.22]] und [[MAT.5.28]] aaglichen sii.",
   AUTO_G + " läsed 01, 03 und 032 πᾶς ὁ ἀπολύων, 05 ὃς ἂν ἀπολύσῃ. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-032-02:R2", "MAT.5.32", "macht, dass mit ihr die Ehe gebrochen wird", "macht, dass sie die Ehe bricht",
  "macht, dass mit ire d Ee broche wird", "macht, dass si d Ee bricht", "mittel",
  "Mit der Medialform ist die Frau Handelnde des Ehebruchs, nicht Betroffene.",
  "Mit de Medialform isch d Frau die, wo d Ee bricht, nöd die, wo s betrifft.",
  {"R1": [("μοιχευθῆναι", "dass mit ihr die Ehe gebrochen wird (Passiv)", "SBLGNT, WH, Treg, NA28")], "R2": [("μοιχᾶσθαι", "dass sie die Ehe bricht", "RP")]},
  {"R1": [("μοιχευθῆναι", "dass mit ire d Ee broche wird (Passiv)", "SBLGNT, WH, Treg, NA28")], "R2": [("μοιχᾶσθαι", "dass si d Ee bricht", "RP")]},
  ["μοιχᾶσθαι entspricht dem Verb am Versende (μοιχᾶται) und kann daran angeglichen sein; das Passiv ist die ungewöhnlichere Form.",
   "Umgekehrt kann das Passiv aus dem Bestreben entstanden sein, die Verantwortung beim Mann zu betonen.",
   AUTO + " lesen 01, 03, 05 und 032 μοιχευθῆναι. 04 ist an dieser Stelle nicht erhalten."],
  ["μοιχᾶσθαι entspricht em Verb am Versänd (μοιχᾶται) und cha dra aaglichen sii; s Passiv isch di ungwöhnlicher Form.",
   "Umgekeert cha s Passiv entstande sii, zum d Verantwortig vom Maa betone.",
   AUTO_G + " läsed 01, 03, 05 und 032 μοιχευθῆναι. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-039-03:R2", "MAT.5.39", "auf die rechte Wange", "auf deine rechte Wange", "uf de rächt Bagge", "uf din rächte Bagge", "gering",
  "Mit σου ist die Wange ausdrücklich die des Angesprochenen; am Sinn ändert sich nichts. Hier folgt der SBLGNT RP gegen WH, Treg und NA28.",
  "Mit σου isch de Bagge usdrücklich dä vom Aagredete; am Sinn änderet sich nüüt. Da folgt de SBLGNT em RP gäge WH, Treg und NA28.",
  {"R1": [("σιαγόνα", "Wange", "SBLGNT, RP; NIV")], "R2": [("σιαγόνα σου", "deine Wange", "WH, Treg, NA28")]},
  {"R1": [("σιαγόνα", "Bagge", "SBLGNT, RP; NIV")], "R2": [("σιαγόνα σου", "din Bagge", "WH, Treg, NA28")]},
  ["σου kann als Verdeutlichung ergänzt oder als selbstverständlich weggelassen worden sein.",
   AUTO + " lesen 01 und 032 ohne σου, 03 und 05 mit σου. 04 ist an dieser Stelle nicht erhalten."],
  ["σου cha als Verdüütlichung ergänzt oder als sälbverständlich weggloo worde sii.",
   AUTO_G + " läsed 01 und 032 ohni σου, 03 und 05 mit. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-044-01:R2", "MAT.5.44", "Liebt eure Feinde", "Liebt eure Feinde, segnet, die euch verfluchen, tut Gutes denen, die euch hassen",
  "Liebed eui Find", "Liebed eui Find, sägned die, wo eu verfluechet, tüend dene Guets, wo eu hassed", "erheblich",
  "Zwei weitere Weisungen kommen hinzu; sie stehen ähnlich in [[LUK.6.27]]–[[LUK.6.28]].",
  "Zwei wiiteri Wiisige chömed dezue; si stönd ähnlich i [[LUK.6.27]]–[[LUK.6.28]].",
  {"R1": [("ὑμῶν", "(ohne Zusatz)", "SBLGNT, WH, Treg, NA28")],
   "R2": [("ὑμῶν, εὐλογεῖτε τοὺς καταρωμένους ὑμᾶς, καλῶς ποιεῖτε τοῖς μισοῦσιν ὑμᾶς", "segnet, die euch verfluchen, tut Gutes denen, die euch hassen", "RP")]},
  {"R1": [("ὑμῶν", "(ohni Zuesatz)", "SBLGNT, WH, Treg, NA28")],
   "R2": [("ὑμῶν, εὐλογεῖτε τοὺς καταρωμένους ὑμᾶς, καλῶς ποιεῖτε τοῖς μισοῦσιν ὑμᾶς", "sägned die, wo eu verfluechet, tüend dene Guets, wo eu hassed", "RP")]},
  ["Die Zusätze entsprechen weitgehend [[LUK.6.27]]–[[LUK.6.28]]; Abschreiber können Matthäus an Lukas angeglichen haben.",
   "Umgekehrt wird vertreten, die Wendungen seien bei Matthäus wegen der mehrfach gleichen Endung ὑμᾶς beim Abschreiben übersprungen worden.",
   AUTO + " lesen 01 und 03 ohne Zusatz, 05 und 032 mit ihm. 04 ist an dieser Stelle nicht erhalten."],
  ["D Zuesätz entspräched wiitgehend [[LUK.6.27]]–[[LUK.6.28]]; Abschriiber chönnted de Matthäus am Lukas aaglichen ha.",
   "Umgekeert wird vertrette, d Wändige seiged wäge de mehrfach gliiche Ändig ὑμᾶς bim Abschriibe übersprunge worde.",
   AUTO_G + " läsed 01 und 03 ohni Zuesatz, 05 und 032 mit. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-044-02:R2", "MAT.5.44", "betet für die, die euch verfolgen", "betet für die, die euch beleidigen und verfolgen",
  "bätted für die, wo eu verfolged", "bätted für die, wo eu beleidiged und verfolged", "gering",
  "Zu den Verfolgern kommen die hinzu, die beleidigen (vgl. [[LUK.6.28]]).", "Zu de Verfolger chömed die dezue, wo beleidiged (vgl. [[LUK.6.28]]).",
  {"R1": [("τῶν", "(ohne Zusatz)", "SBLGNT, WH, Treg, NA28")], "R2": [("τῶν ἐπηρεαζόντων ὑμᾶς καὶ", "die euch beleidigen und", "RP")]},
  {"R1": [("τῶν", "(ohni Zuesatz)", "SBLGNT, WH, Treg, NA28")], "R2": [("τῶν ἐπηρεαζόντων ὑμᾶς καὶ", "die, wo eu beleidiged und", "RP")]},
  ["Der Zusatz entspricht [[LUK.6.28]] (περὶ τῶν ἐπηρεαζόντων ὑμᾶς) und kann daraus übernommen sein; ebenso kann er zusammen mit dem Zusatz davor ausgefallen sein.",
   AUTO + " lesen 01, 03 und 05 ohne Zusatz, 032 mit ihm. 04 ist an dieser Stelle nicht erhalten."],
  ["De Zuesatz entspricht [[LUK.6.28]] und cha vo dört übernoo sii; oder er isch zäme mit em Zuesatz vorher usgfalle.",
   AUTO_G + " läsed 01, 03 und 05 ohni Zuesatz, 032 mit. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-046-01:R2", "MAT.5.46", "Tun nicht auch die Zöllner dasselbe?", "Tun es nicht auch die Zöllner so?",
  "Mached nöd au d Zöllner s Gliiche?", "Mached s nöd au d Zöllner eso?", "gering",
  "οὕτως («so») statt τὸ αὐτό («dasselbe»); am Sinn ändert sich nichts.", "οὕτως («eso») statt τὸ αὐτό («s Gliiche»); am Sinn änderet sich nüüt.",
  {"R1": [("τὸ αὐτὸ", "dasselbe", "SBLGNT, WH, NA28, RP")], "R2": [("οὕτως", "so", "Treg")]},
  {"R1": [("τὸ αὐτὸ", "s Gliiche", "SBLGNT, WH, NA28, RP")], "R2": [("οὕτως", "eso", "Treg")]},
  ["Die gleichbedeutenden Ausdrücke wechseln leicht; οὕτως kann aus der Lesart von [[MAT.5.47]] stammen, die RP dort hat.",
   AUTO + " lesen 01, 03 und 032 τὸ αὐτό, 05 οὕτως. 04 ist an dieser Stelle nicht erhalten."],
  ["Di gliichbedüütende Usdrück wächsled liecht; οὕτως cha us de Läsart vo [[MAT.5.47]] stamme.",
   AUTO_G + " läsed 01, 03 und 032 τὸ αὐτό, 05 οὕτως. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-047-01:R2", "MAT.5.47", "nur eure Brüder", "nur eure Freunde", "nu eui Brüeder", "nu eui Fründ", "gering",
  "Statt der «Brüder» sind die «Freunde» genannt.", "Statt de «Brüeder» sind d «Fründ» gnännt.",
  {"R1": [("ἀδελφοὺς", "Brüder", "SBLGNT, WH, Treg, NA28")], "R2": [("φίλους", "Freunde", "RP")]},
  {"R1": [("ἀδελφοὺς", "Brüeder", "SBLGNT, WH, Treg, NA28")], "R2": [("φίλους", "Fründ", "RP")]},
  ["«Freunde» kann das gemeindliche «Brüder» verallgemeinern oder verdeutlichen, dass nicht nur leibliche Brüder gemeint sind.",
   AUTO + " lesen 01, 03 und 05 ἀδελφούς, 032 φίλους. 04 ist an dieser Stelle nicht erhalten."],
  ["«Fründ» cha s gmeindlich «Brüeder» verallgemeinere.",
   AUTO_G + " läsed 01, 03 und 05 ἀδελφούς, 032 φίλους. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-047-02:R2", "MAT.5.47", "die Heiden", "die Zöllner", "d Heide", "d Zöllner", "gering",
  "Wie in [[MAT.5.46]] sind die Zöllner genannt.", "Wie i [[MAT.5.46]] sind d Zöllner gnännt.",
  {"R1": [("ἐθνικοὶ", "Heiden", "SBLGNT, WH, Treg, NA28")], "R2": [("τελῶναι", "Zöllner", "RP")]},
  {"R1": [("ἐθνικοὶ", "Heide", "SBLGNT, WH, Treg, NA28")], "R2": [("τελῶναι", "Zöllner", "RP")]},
  ["τελῶναι gleicht an [[MAT.5.46]] an; umgekehrt bildet ἐθνικοί eine Steigerung, die ein Schreiber kaum eingeführt hätte, wenn er Zöllner vorfand.",
   AUTO + " lesen 01, 03 und 05 ἐθνικοί, 032 τελῶναι. 04 ist an dieser Stelle nicht erhalten."],
  ["τελῶναι gliicht a [[MAT.5.46]] aa.",
   AUTO_G + " läsed 01, 03 und 05 ἐθνικοί, 032 τελῶναι. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-047-03:R2", "MAT.5.47", "Tun nicht auch die Heiden dasselbe?", "Tun es nicht auch die Heiden so?",
  "Mached nöd au d Heide s Gliiche?", "Mached s nöd au d Heide eso?", "gering",
  "οὕτως («so») statt τὸ αὐτό («dasselbe»); am Sinn ändert sich nichts.", "οὕτως («eso») statt τὸ αὐτό («s Gliiche»); am Sinn änderet sich nüüt.",
  {"R1": [("τὸ αὐτὸ", "dasselbe", "SBLGNT, WH, Treg, NA28")], "R2": [("οὕτως", "so", "RP")]},
  {"R1": [("τὸ αὐτὸ", "s Gliiche", "SBLGNT, WH, Treg, NA28")], "R2": [("οὕτως", "eso", "RP")]},
  ["Die gleichbedeutenden Ausdrücke wechseln leicht; τὸ αὐτό kann an [[MAT.5.46]] angeglichen sein, οὕτως eine stilistische Abwechslung.",
   AUTO + " lesen 01, 03, 05 und 032 τὸ αὐτό. 04 ist an dieser Stelle nicht erhalten."],
  ["Di gliichbedüütende Usdrück wächsled liecht.",
   AUTO_G + " läsed 01, 03, 05 und 032 τὸ αὐτό. 04 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-005-048-02:R2", "MAT.5.48", "euer himmlischer Vater", "euer Vater in den Himmeln", "eue himmlisch Vatter", "eue Vatter i de Himel", "gering",
  "Statt «himmlisch» steht die Wendung «in den Himmeln»; am Sinn ändert sich nichts.", "Statt «himmlisch» staat «i de Himel»; am Sinn änderet sich nüüt.",
  {"R1": [("ὁ οὐράνιος", "himmlisch", "SBLGNT, WH, Treg, NA28")], "R2": [("ὁ ἐν τοῖς οὐρανοῖς", "in den Himmeln", "RP")]},
  {"R1": [("ὁ οὐράνιος", "himmlisch", "SBLGNT, WH, Treg, NA28")], "R2": [("ὁ ἐν τοῖς οὐρανοῖς", "i de Himel", "RP")]},
  ["Die Lesart mit ἐν τοῖς οὐρανοῖς gleicht an die häufigere Wendung an (vgl. [[MAT.5.16]], [[MAT.5.45]]).",
   AUTO + " lesen 01, 03, 05 und 032 ὁ οὐράνιος. 04 ist an dieser Stelle nicht erhalten."],
  ["D Läsart mit ἐν τοῖς οὐρανοῖς gliicht a di hüüfiger Wändig aa (vgl. [[MAT.5.16]], [[MAT.5.45]]).",
   AUTO_G + " läsed 01, 03, 05 und 032 ὁ οὐράνιος. 04 isch a dere Stell nöd erhalte."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-005-001-048", "MAT.5.1-MAT.5.48", "section", "Die Bergpredigt beginnt: Seligpreisungen, Salz und Licht, Gesetz und «Ich aber sage euch»",
  ["TU-MAT-005-001-012", "TU-MAT-005-013-016", "TU-MAT-005-017-020", "TU-MAT-005-021-026", "TU-MAT-005-027-032",
   "TU-MAT-005-033-037", "TU-MAT-005-038-042", "TU-MAT-005-043-048"],
  "Als Jesus die Menge sieht, steigt er auf den Berg, setzt sich und lehrt seine Jünger. Er preist Arme im Geist, Trauernde, Sanftmütige, nach Gerechtigkeit Hungernde, Barmherzige, Menschen mit reinem Herzen, Friedensstifter und Verfolgte selig, auch seine Hörer, wenn man sie seinetwegen schmäht. Er nennt sie das Salz der Erde und das Licht der Welt. Er sei nicht gekommen, das Gesetz oder die Propheten aufzuheben, sondern zu erfüllen; ihre Gerechtigkeit müsse weit über die der Schriftgelehrten und Pharisäer hinausgehen. Sechsmal stellt er dem, was gesagt worden ist, sein «Ich aber sage euch» gegenüber: zum Töten, zum Ehebruch, zur Scheidung, zum Schwören, zur Vergeltung und zur Liebe zum Nächsten und zum Feind. Er schliesst: Liebt eure Feinde; ihr sollt vollkommen sein, wie euer himmlischer Vater vollkommen ist. Die Rede geht in Kapitel 6 und 7 weiter.", SEG),
 ("TU-MAT-005-001-012", "MAT.5.1-MAT.5.12", "discourse", "Die Seligpreisungen", None,
  "Als Jesus die Menge sieht, steigt er auf den Berg und setzt sich; seine Jünger treten zu ihm, und er lehrt sie. Er nennt selig die Armen im Geist, die Trauernden, die Sanftmütigen, die nach der Gerechtigkeit hungern und dürsten, die Barmherzigen, die ein reines Herz haben, die Frieden stiften und die wegen der Gerechtigkeit verfolgt worden sind. Den Armen im Geist und den Verfolgten gehöre das Reich der Himmel; die anderen würden getröstet, die Erde erben, satt werden, Barmherzigkeit erfahren, Gott sehen und Söhne Gottes genannt werden. Selig nennt er auch seine Hörer, wenn man sie seinetwegen beschimpft, verfolgt und verleumdet: Sie sollen sich freuen, denn ihr Lohn in den Himmeln ist gross; so hat man schon die Propheten vor ihnen verfolgt.", None),
 ("TU-MAT-005-013-016", "MAT.5.13-MAT.5.16", "discourse", "Salz der Erde und Licht der Welt", None,
  "Jesus sagt seinen Hörern: Ihr seid das Salz der Erde; fad gewordenes Salz taugt zu nichts mehr, als hinausgeworfen und zertreten zu werden. Ihr seid das Licht der Welt; eine Stadt auf einem Berg kann nicht verborgen bleiben, und eine Lampe stellt man nicht unter den Scheffel, sondern auf den Leuchter. So soll ihr Licht vor den Menschen leuchten, damit diese ihre guten Werke sehen und ihren Vater in den Himmeln preisen.", None),
 ("TU-MAT-005-017-020", "MAT.5.17-MAT.5.20", "discourse", "Gesetz und Propheten erfüllen", None,
  "Jesus sagt, er sei nicht gekommen, das Gesetz oder die Propheten aufzuheben, sondern zu erfüllen. Bis Himmel und Erde vergehen, werde vom Gesetz nicht ein einziges Jota oder Häkchen vergehen, bis alles geschieht. Wer eines der kleinsten Gebote auflöst und so lehrt, werde der Kleinste im Reich der Himmel genannt, wer sie tut und lehrt, gross. Wenn die Gerechtigkeit seiner Hörer nicht weit über die der Schriftgelehrten und Pharisäer hinausgeht, kommen sie gewiss nicht in das Reich der Himmel.", None),
 ("TU-MAT-005-021-026", "MAT.5.21-MAT.5.26", "discourse", "Vom Töten und vom Zorn", None,
  "Zum Gebot «Du sollst nicht töten» sagt Jesus: Schon wer seinem Bruder zürnt, ist dem Gericht verfallen; wer zu ihm «Raka» sagt, dem Hohen Rat, wer «Du Narr» sagt, dem Feuer der Hölle. Wer seine Gabe zum Altar bringt und sich dort erinnert, dass sein Bruder etwas gegen ihn hat, soll die Gabe liegen lassen, sich zuerst mit dem Bruder versöhnen und sie dann darbringen. Mit dem Gegner soll man sich unterwegs schnell einigen, damit er einen nicht dem Richter übergibt und man ins Gefängnis geworfen wird, aus dem man erst herauskommt, wenn man den letzten Rappen bezahlt hat.", None),
 ("TU-MAT-005-027-032", "MAT.5.27-MAT.5.32", "discourse", "Vom Ehebruch und von der Scheidung", None,
  "Zum Gebot «Du sollst nicht ehebrechen» sagt Jesus: Wer eine Frau ansieht, um sie zu begehren, hat in seinem Herzen schon mit ihr die Ehe gebrochen. Bringt das rechte Auge oder die rechte Hand zu Fall, soll man das Auge herausreissen und die Hand abhauen; besser ein Glied verlieren, als dass der ganze Leib in die Hölle kommt. Zur Weisung, wer seine Frau entlasse, solle ihr einen Scheidebrief geben, sagt er: Wer seine Frau entlässt, ausser wegen Unzucht, macht, dass mit ihr die Ehe gebrochen wird, und wer eine Entlassene heiratet, bricht die Ehe.", None),
 ("TU-MAT-005-033-037", "MAT.5.33-MAT.5.37", "discourse", "Vom Schwören", None,
  "Zu den Alten wurde gesagt, sie sollten keinen Meineid schwören und dem Herrn ihre Eide halten. Jesus sagt, man solle überhaupt nicht schwören: nicht beim Himmel, dem Thron Gottes, nicht bei der Erde, dem Schemel seiner Füsse, nicht bei Jerusalem, der Stadt des grossen Königs, und nicht beim eigenen Kopf, denn man kann kein einziges Haar weiss oder schwarz machen. Die Rede soll «Ja, ja» und «nein, nein» sein; was darüber hinausgeht, ist vom Bösen.", None),
 ("TU-MAT-005-038-042", "MAT.5.38-MAT.5.42", "discourse", "Von der Vergeltung", None,
  "Dem Satz «Auge um Auge und Zahn um Zahn» stellt Jesus gegenüber: Man soll dem Bösen nicht widerstehen. Wer einen auf die rechte Wange schlägt, dem soll man auch die andere hinhalten; wer vor Gericht das Hemd nehmen will, dem auch den Mantel lassen; wer einen zwingt, eine Meile mitzugehen, mit dem soll man zwei gehen. Wer bittet, dem soll man geben, und wer borgen will, von dem soll man sich nicht abwenden.", None),
 ("TU-MAT-005-043-048", "MAT.5.43-MAT.5.48", "discourse", "Von der Feindesliebe", None,
  "Zum Wort «Du sollst deinen Nächsten lieben und deinen Feind hassen» sagt Jesus: Liebt eure Feinde und betet für die, die euch verfolgen, damit ihr Söhne eures Vaters in den Himmeln werdet; denn er lässt seine Sonne über Böse und Gute aufgehen und regnen über Gerechte und Ungerechte. Wer nur die liebt, die ihn lieben, und nur seine Brüder grüsst, tut nichts Besonderes; das tun auch die Zöllner und die Heiden. Ihr sollt also vollkommen sein, wie euer himmlischer Vater vollkommen ist.", None),
]
UNITS_GSW = {
 "TU-MAT-005-001-048": ("D Bärgpredig faat aa: Säligpriisige, Salz und Liecht, s Gsetz und «Ich aber säg eu»",
  "Wo de Jesus d Mängi gseet, staat er uf de Bärg ufe, sitzt ab und leert sini Jünger. Er priist di Arme im Geischt, die, wo truured, di Sanftmüetige, die, wo nach Grächtigkeit hungered, di Barmhärzige, die mit eme reine Härz, die, wo Fride stifted, und di Verfolgte sälig, au sini Zuehörer, wänn me si wäge ihm schlächt macht. Er nännt si s Salz vo de Ärde und s Liecht vo de Wält. Er sig nöd choo, zum s Gsetz oder d Prophete ufhebe, sondern zum erfülle; iri Grächtigkeit müess wiit über die vo de Schriftgelehrti und Pharisäer usegaa. Sächs Mal stellt er däm, was gseit worde isch, sis «Ich aber säg eu» gägenüber: zum Töte, zum Ebruch, zur Scheidig, zum Schwöre, zur Vergältig und zur Liebi zum Nächschte und zum Find. Er schlüüsst: Liebed eui Find; ir söled vollkomme sii, wie eue himmlisch Vatter vollkomme isch. D Red gaat im Kapitel 6 und 7 wiiter."),
 "TU-MAT-005-001-012": ("D Säligpriisige",
  "Wo de Jesus d Mängi gseet, staat er uf de Bärg ufe und sitzt ab; sini Jünger chömed zu ihm, und er leert si. Er nännt sälig di Arme im Geischt, die, wo truured, di Sanftmüetige, die, wo nach de Grächtigkeit hungered und dürschted, di Barmhärzige, die, wo es reins Härz händ, die, wo Fride stifted, und die, wo wäge de Grächtigkeit verfolgt worde sind. De Arme im Geischt und de Verfolgte ghöri s Riich vo de Himel; di andere wärdid tröschtet, wärdid d Ärde erbe, satt wärde, Barmhärzigkeit erfaare, Gott gsee und Söhn vo Gott gnännt. Sälig nännt er au sini Zuehörer, wänn me si wäge ihm beschimpft, verfolgt und Lüüge über si verzellt: Si söled sich fröie, dänn ire Loon i de Himel isch gross; so hät me scho d Prophete vor ine verfolgt."),
 "TU-MAT-005-013-016": ("S Salz vo de Ärde und s Liecht vo de Wält",
  "De Jesus seit sine Zuehörer: Ir sind s Salz vo de Ärde; Salz, wo fad worde isch, isch für nüüt mee guet, als dass me s usewirft und vertrampet. Ir sind s Liecht vo de Wält; e Stadt uf eme Bärg cha nöd versteckt bliibe, und e Lampe stellt me nöd under de Schäffel, sondern uf de Lüüchter. Eso söll ires Liecht vor de Lüüt lüüchte, demit die iri guete Wärch gseend und ire Vatter i de Himel priised."),
 "TU-MAT-005-017-020": ("S Gsetz und d Prophete erfülle",
  "De Jesus seit, er sig nöd choo, zum s Gsetz oder d Prophete ufhebe, sondern zum erfülle. Bis de Himel und d Ärde vergönd, vergöng vom Gsetz nöd es einzigs Jota oder es einzigs Hääggli, bis alles gschee isch. Wer eis vo de chliinschte Gebot uflööst und eso leert, wärdi de Chliinscht im Riich vo de Himel gnännt, wer si tuet und leert, gross. Wänn d Grächtigkeit vo sine Zuehörer nöd wiit über die vo de Schriftgelehrti und Pharisäer usegaat, chömed si sicher nöd is Riich vo de Himel ine."),
 "TU-MAT-005-021-026": ("Vom Töte und vom Zorn",
  "Zum Gebot «Du söllsch nöd töte» seit de Jesus: Scho wer uf sin Brüeder wüetig isch, isch em Gricht verfalle; wer zu ihm «Raka» seit, em Hoche Raat, wer «Du Tubel» seit, em Füür vo de Höll. Wer sis Gschänk zum Altar bringt und sich dört erinneret, dass sin Brüeder öppis gäge ihn hät, söll s Gschänk la staa, sich zerscht mit em Brüeder versööne und s dänn darbringe. Mit em Gägner söll me sich underwägs schnäll einige, demit er eim nöd em Richter übergit und me is Gfängnis gworfe wird, wo me erscht wider usechunnt, wänn me de letscht Rappe zaalt hät."),
 "TU-MAT-005-027-032": ("Vom Ebruch und vo de Scheidig",
  "Zum Gebot «Du söllsch nöd d Ee breche» seit de Jesus: Wer e Frau aaluegt, zum si begääre, hät i sim Härz scho mit ire d Ee broche. Wänn s rächt Aug oder di rächt Hand eim zu Fall bringt, söll me s Aug usriisse und d Hand abhaue; s isch besser, es Glid z verliere, als dass de ganz Liib i d Höll chunnt. Zur Wiisig, wer sini Frau entlaat, söll ire en Scheidigsbrief gää, seit er: Wer sini Frau entlaat, ussert wäge Unzucht, macht, dass mit ire d Ee broche wird, und wer e Entlasseni hüratet, bricht d Ee."),
 "TU-MAT-005-033-037": ("Vom Schwöre",
  "Zu de Alte isch gseit worde, si söled kei Meineid schwöre und em Herr iri Eid halte. De Jesus seit, me söll überhaupt nöd schwöre: nöd bim Himel, em Troon vo Gott, nöd bi de Ärde, em Schämel für sini Füess, nöd bi Jerusalem, de Stadt vom grosse König, und nöd bim eigete Chopf, dänn me chan kei einzigs Haar wiiss oder schwarz mache. D Red söll «Ja, ja» und «nei, nei» sii; was mee isch, isch vom Bööse."),
 "TU-MAT-005-038-042": ("Vo de Vergältig",
  "Em Satz «Aug um Aug und Zaa um Zaa» stellt de Jesus gägenüber: Me söll em Bööse nöd widerstaa. Wer eim uf de rächt Bagge schlaat, däm söll me au de ander anehebe; wer vor Gricht s Hemd will nää, däm au de Mantel laa; wer eim zwingt, ei Meile mitzgaa, mit däm söll me zwei gaa. Wer bittet, däm söll me gää, und vo däm, wo öppis entlehne will, söll me sich nöd abcheere."),
 "TU-MAT-005-043-048": ("Vo de Findesliebi",
  "Zum Wort «Du söllsch din Nächschte liebe und din Find hasse» seit de Jesus: Liebed eui Find und bätted für die, wo eu verfolged, demit ir Söhn vo eurem Vatter i de Himel wärded; dänn er laat sini Sunne über Bööse und Gueti ufgaa und laat s rägne über Grächti und Ungrächti. Wer nu die liebt, wo ihn liebed, und nu sini Brüeder grüesst, macht nüüt Bsunders; das mached au d Zöllner und d Heide. Ir söled also vollkomme sii, wie eue himmlisch Vatter vollkomme isch."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten in den Alternativen beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1, "
  "WREAD-CNTR-MAT-005-001-048) bzw. auf dem dort erfassten Wortlaut der CNTR-Transkriptionen (Sekundärtranskription, nicht am "
  "Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. Handschriften: 01 Sinaiticus, 03 Vaticanus, 04 Ephraemi (an den "
  "Variantenstellen ab [[MAT.5.20]] nicht erhalten), 05 Bezae, 032 Washingtonianus. Zahlen zu Wortvorkommen sind per Skript aus den "
  "MACULA-Lemmata des SBLGNT-Texts gezählt."),
 ("Abgrenzung: Diese Datei umfasst [[MAT.5.1-MAT.5.48]], den Anfang der Bergpredigt (Kapitel 5–7). [[MAT.6.5-MAT.6.15]] ist in "
  "TRANS-MAT-006-005-015-DE-WORKING erfasst; Wiedergaben wie «Vater in den Himmeln», «himmlischer Vater», «Lohn», «Heiden», "
  "«vom Bösen» und «die Menschen» sind darauf abgestimmt. Gleiche griechische Wendungen wie bei Markus sind möglichst gleich "
  "übersetzt (z. B. «Scheffel», «Scheidebrief», «entlassen», «zu Fall bringen», «Hölle», «Du sollst nicht töten»)."),
 ("Einheitliche Matthäus-Begriffe (für alle Kapitel abgestimmt): «das Reich der Himmel» / «das Reich Gottes»; «Amen, ich sage "
  "euch / dir»; «Vater in den Himmeln», «himmlischer Vater»; «Schriftgelehrte», «Pharisäer»; «Gesetz». Hier neu festgelegt "
  "und in decisions begründet: μακάριος «selig» (13-mal im Buch); δικαιοσύνη «Gerechtigkeit» (7-mal); σκανδαλίζω «zu Fall "
  "bringen» (14-mal, wie Markus); γέεννα «Hölle» (7-mal); μισθός «Lohn» (10-mal); οὐ μή «gewiss nicht»; ὄχλοι «die Menge»; "
  "ἄνθρωποι «die Menschen» (Mundart «d Lüüt»); ἐθνικοί «Heiden»; τελῶναι «Zöllner»; τέλειος «vollkommen»; δοξάζω (von Menschen "
  "gegenüber Gott) «preisen»; ἀδελφός «Bruder»."),
 ("Die Rede ([[MAT.5.3]]–[[MAT.7.27]]) steht ohne Anführungszeichen, wie in TRANS-MAT-006-005-015; Zitate in der Rede stehen in «». "
  "Anführungszeichen sind eine Entscheidung der Übersetzung, das Griechische hat keine. Die sechs Gegenüberstellungen "
  "([[MAT.5.21]]–[[MAT.5.48]]) sind durchgehend mit «Ihr habt gehört, dass … gesagt worden ist» und «Ich aber sage euch» "
  "wiedergegeben, damit ihre Form sichtbar bleibt. ὅτι vor einer Aussage ist nicht eigens übersetzt."),
 ("Text: In Kapitel 5 fehlt im SBLGNT kein Vers. Die Übersetzung folgt an allen Apparatstellen dem SBLGNT (follows_readings), "
  "auch in [[MAT.5.39]] (σιαγόνα ohne σου, mit RP gegen WH, Treg und NA28). Als Alternativen stehen die Lesarten, die die "
  "Übersetzung verändern. Ohne Alternative bleiben Varianten, die im Deutschen gleich lauten: Wortfolge ([[MAT.5.20]], "
  "[[MAT.5.25]], [[MAT.5.36]]), βληθῆναι statt βληθέν ([[MAT.5.13]]), ὅτι vor dem Zitat ([[MAT.5.31]]), ῥαπίσει statt "
  "ῥαπίζει und ἐπί statt εἰς ([[MAT.5.39]]), δίδου statt δός ([[MAT.5.42]]), Artikel vor οὐρανοῖς ([[MAT.5.45]]) und ὥσπερ "
  "statt ὡς ([[MAT.5.48]])."),
 "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1, WREAD-CNTR-MAT-005-001-048) "
  "oder uf em erfasste Wortlut vo de CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Abgränzig: [[MAT.6.5-MAT.6.15]] staat i TRANS-MAT-006-005-015-GSW-ZH-WORKING; Wörter wie «Vatter i de Himel», «himmlisch "
  "Vatter», «Loon», «Heide», «vom Bööse» und «d Lüüt» sind druf abgstimmt."),
 ("Grundentscheid für Matthäus (usfüerlich i de hochdütsche translation_notes): «s Riich vo de Himel», «s Riich vo Gott»; «Amen, "
  "ich säg eu»; «Vatter i de Himel», «himmlisch»; «Schriftgelehrti», «Pharisäer»; μακάριος «sälig»; δικαιοσύνη «Grächtigkeit»; "
  "σκανδαλίζω «zu Fall bringe»; γέεννα «Höll»; μισθός «Loon»; οὐ μή «sicher nöd»; ἄνθρωποι «d Lüüt»."),
 ("Mundart: Näme mit Artikel; Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv («s Riich vo de Himel»). D Red staat "
  "ohni Aafüerigszeiche wie im Vaterunser; Zitat i de Red stönd i «»."),
 "Eigeti Formulierig; nöd us ere veröffentlichte Mundart-Bible übernoo.",
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
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; Wiederholungswörter einheitlich (Grundentscheide in translation_notes und decisions). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_05_05.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 5 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
