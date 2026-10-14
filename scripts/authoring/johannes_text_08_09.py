#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 8–9 (die Frau vor Jesus, das Licht der Welt, der Streit um Abraham, der Blindgeborene) –
Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen,
Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_08_09.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- [[JHN.8.1]]–[[JHN.8.11]] setzt den Abschnitt von der Frau, die beim Ehebruch ergriffen wurde, fort. Er beginnt im
  SBLGNT mit [[JHN.7.53]] (Teileinheit TU-JHN-007-053-053, eigenes Werkzeug) und steht dort in Doppelklammern ⟦ ⟧.
  Die öffnende Klammer steht bei 7,53, die schliessende in den Tokens von [[JHN.8.11]]; sie bleibt im Übersetzungstext.
  Die Angaben zu den Handschriften stammen aus den CNTR-Transkriptionen in data/witness-texts (siehe WITNESS_PA unten).
- Die johanneischen Schlüsselwörter sind einheitlich wiedergegeben wie in den Grundentscheiden zu Johannes 1–3
  (scripts/authoring/johannes_text_01_03.py): ἐγώ εἰμι «Ich bin …», δόξα/δοξάζω «Herrlichkeit/verherrlichen»,
  σημεῖον «Zeichen», μένω «bleiben», ἀμὴν ἀμήν «Amen, amen», κόσμος «Welt», ὑψόω «erhöhen», οἱ Ἰουδαῖοι «die Juden»
  (Deutungsentscheidung, siehe decisions und translation_notes).

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
CHAPTERS = ((8, 59), (9, 41))

DE = {
 # ------------------------------------------------------------ Kapitel 8
 "JHN.8.1": "[Jesus]{1} [aber]{2} [ging]{3} [zum]{4,5} [Ölberg]{6-8}.",
 "JHN.8.2": "[Früh am Morgen]{1} [aber]{2} [kam er]{4} [wieder]{3} [in]{5} [den]{6} [Tempel]{7}, und{8} [das ganze]{9,10} [Volk]{11} [kam herbei]{12}; und{13} [er setzte sich]{14} [und lehrte]{15} [sie]{16}.",
 "JHN.8.3": "[Da]{2} [bringen]{1} [die Schriftgelehrten]{3,4} und{5} [die Pharisäer]{6,7} [eine Frau]{10} [zu]{8} [ihm]{9}, [die]{13} [beim]{11} [Ehebruch]{12} [ergriffen worden war]{13}; und{14} [sie stellten]{15} [sie]{16} [in]{17} [die Mitte]{18}",
 "JHN.8.4": "und [sagen]{1} [zu ihm]{2}, [um]{3} ihn [auf die Probe zu stellen]{3}: «[Lehrer]{4}, [diese]{5} [Frau]{6,7} [ist]{8} [auf frischer Tat]{9,10} [beim Ehebruch]{11} [ergriffen worden]{8}.",
 "JHN.8.5": "[Im]{1,3} [Gesetz]{4} [aber]{2} [hat]{7} [uns]{6} [Mose]{5} [geboten]{7}, [solche]{8,9} [zu steinigen]{10}. [Was]{13} [sagst]{14} [nun]{12} [du]{11}?»",
 "JHN.8.6": "[Das]{1} [sagten sie]{3} [aber]{2}, [um]{4} [ihn]{5} [auf die Probe zu stellen]{4}, [damit]{6} [sie]{7} [ihn]{9} [anklagen]{8} [könnten]{7}. [Jesus]{10,12} [aber]{11} [bückte sich nieder]{13,14} [und schrieb]{17} [mit dem]{15} [Finger]{16} [auf]{18} [die]{19} [Erde]{20}, [ohne auf sie einzugehen]{21,22}.",
 "JHN.8.7": "[Als]{1} [sie]{3} [ihn]{5} [aber]{2} [immer weiter]{3} [fragten]{4}, [richtete er sich auf]{6} [und sagte]{7} [zu]{8} [ihnen]{9}: «[Wer]{10} [von euch]{12} [ohne Sünde ist]{11}, [werfe]{18} [als Erster]{13} [den]{16} [Stein]{17} [auf]{14} [sie]{15}.»",
 "JHN.8.8": "Und{1} [wieder]{2} [bückte er sich nieder]{3,4} [und schrieb]{5} [auf]{6} [die]{7} [Erde]{8}.",
 "JHN.8.9": "[Sie]{1} [aber]{2} [hörten es]{3}, und{4} [vom]{5,6} [Gewissen]{7} [überführt]{8} [gingen sie hinaus]{9}, [einer]{10} [nach]{11} [dem anderen]{12}, [angefangen]{13} [bei]{14} [den]{15} [Ältesten]{16}; und{17} [Jesus]{20,21} [blieb]{18} [allein]{19} [zurück]{18}, und{22} [die]{23} [Frau]{24}, [die]{27} [in]{25} [der Mitte]{26} [stand]{27}.",
 "JHN.8.10": "[Jesus]{3,4} [aber]{2} [richtete sich auf]{1}, und{5} [als er]{7} [niemanden]{6} [sah]{7} [ausser]{8} [der]{9} [Frau]{10}, [sagte er]{11} [zu ihr]{12}: «[Wo]{13} [sind]{14} [jene]{15}, [deine]{18} [Ankläger]{16,17}? [Hat]{21} [niemand]{19} [dich]{20} [verurteilt]{21}?»",
 "JHN.8.11": "[Sie]{1} [aber]{2} [sagte]{3}: «[Niemand]{4}, [Herr]{5}.» [Jesus]{8,9} [aber]{7} [sagte]{6}: «[Auch]{10} [ich]{11} [verurteile]{13} [dich]{12} [nicht]{10}. [Geh]{14}, und{15} [sündige]{17} [nicht mehr]{16}!»⟧",
 "JHN.8.12": "[Wieder]{1} [nun]{2} [redete]{4} [Jesus]{5,6} [zu ihnen]{3} [und sagte]{7}: «[Ich]{8} [bin]{9} [das Licht]{10,11} [der Welt]{12,13}. [Wer]{14} [mir]{16} [nachfolgt]{15}, [wird]{19} [gewiss nicht]{17,18} [in]{20} [der Finsternis]{21,22} [gehen]{19}, [sondern]{23} [wird]{24} [das Licht]{25,26} [des Lebens]{27,28} [haben]{24}.»",
 "JHN.8.13": "[Da]{2} [sagten]{1} [die Pharisäer]{4,5} [zu ihm]{3}: «[Du]{6} [legst]{9} [über]{7} [dich selbst]{8} [Zeugnis ab]{9}; [dein]{12} [Zeugnis]{10,11} [ist]{14} [nicht]{13} [wahr]{15}.»",
 "JHN.8.14": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihnen]{5}: «[Auch wenn]{6} [ich]{7} [über]{9} [mich selbst]{10} [Zeugnis ablege]{8}, [ist]{12} [mein]{15} [Zeugnis]{13,14} [wahr]{11}, [denn]{16} [ich weiss]{17}, [woher]{18} [ich gekommen bin]{19} und{20} [wohin]{21} [ich gehe]{22}; [ihr]{23} [aber]{24} [wisst]{26} [nicht]{25}, [woher]{27} [ich komme]{28} [oder]{29} [wohin]{30} [ich gehe]{31}.",
 "JHN.8.15": "[Ihr]{1} [richtet]{5} [nach]{2} [dem]{3} [Fleisch]{4}, [ich]{6} [richte]{8} [niemanden]{7,9}.",
 "JHN.8.16": "[Wenn]{2} [ich]{5} [aber]{4} [auch]{1} [richte]{3}, [ist]{11} [mein]{8,9} [Urteil]{6,7} [wahr]{10}, [denn]{12} [ich bin]{15} [nicht]{14} [allein]{13}, [sondern]{16} [ich]{17} und{18} [der Vater]{22}, [der]{19} [mich]{21} [gesandt hat]{20}.",
 "JHN.8.17": "[Auch]{1,5} [in]{2} [eurem]{6,7} [Gesetz]{3,4} [steht geschrieben]{8}, [dass]{9} [das Zeugnis]{12,13} [zweier]{10} [Menschen]{11} [wahr]{14} [ist]{15}.",
 "JHN.8.18": "[Ich]{1} [bin]{2} [der]{3}, [der]{4} [über]{5} [mich selbst]{6} [Zeugnis ablegt]{4}, und{7} [über]{9} [mich]{10} [legt]{8} [der Vater]{14} [Zeugnis ab]{8}, [der]{11} [mich]{13} [gesandt hat]{12}.»",
 "JHN.8.19": "[Da]{2} [sagten sie]{1} [zu ihm]{3}: «[Wo]{4} [ist]{5} [dein]{8} [Vater]{6,7}?» [Jesus]{10} [antwortete]{9}: «[Ihr kennt]{13} [weder]{11} [mich]{12} [noch]{14} [meinen]{17} [Vater]{15,16}; [wenn]{18} [ihr]{20} [mich]{19} [kennen würdet]{20}, [würdet ihr]{25} [auch]{21} [meinen]{24} [Vater]{22,23} [kennen]{26}.»",
 "JHN.8.20": "[Diese]{1} [Worte]{2,3} [redete er]{4} [bei]{5} [der]{6} [Schatzkammer]{7}, [als er]{8} [im]{9,10} [Tempel]{11} [lehrte]{8}; und{12} [niemand]{13} [nahm]{14} [ihn]{15} [fest]{14}, [denn]{16} [seine]{21} [Stunde]{19,20} [war]{18} [noch nicht]{17} [gekommen]{18}.",
 "JHN.8.21": "[Nun]{2} [sagte er]{1} [wieder]{3} [zu ihnen]{4}: «[Ich]{5} [gehe weg]{6}, und{7} [ihr werdet]{8} [mich]{9} [suchen]{8}, und{10} [ihr werdet]{15} [in]{11} [eurer]{12,14} [Sünde]{13} [sterben]{15}. [Wohin]{16} [ich]{17} [gehe]{18}, [könnt]{21} [ihr]{19} [nicht]{20} [kommen]{22}.»",
 "JHN.8.22": "[Da]{2} [sagten]{1} [die Juden]{3,4}: «[Er wird]{6} [sich]{7} [doch nicht]{5} [selbst]{7} [töten]{6}, [weil]{8} [er sagt]{9}: ‹[Wohin]{10} [ich]{11} [gehe]{12}, [könnt]{15} [ihr]{13} [nicht]{14} [kommen]{16}›?»",
 "JHN.8.23": "Und{1} [er sagte]{2} [zu ihnen]{3}: «[Ihr]{4} [seid]{8} [von]{5} [unten]{6,7}, [ich]{9} [bin]{13} [von]{10} [oben]{11,12}; [ihr]{14} [seid]{19} [aus]{15} [dieser]{16} [Welt]{17,18}, [ich]{20} [bin]{22} [nicht]{21} [aus]{23} [dieser]{26} [Welt]{24,25}.",
 "JHN.8.24": "[Darum]{2} [habe ich]{1} [euch]{3} [gesagt]{1}, [dass]{4} [ihr]{5} [in]{6} [euren]{7,9} [Sünden]{8} [sterben werdet]{5}; [denn]{11} [wenn]{10} [ihr]{13} [nicht]{12} [glaubt]{13}, [dass]{14} [ich]{15} [bin]{16}, [werdet ihr]{17} [in]{18} [euren]{19,21} [Sünden]{20} [sterben]{17}.»",
 "JHN.8.25": "[Da]{2} [sagten sie]{1} [zu ihm]{3}: «[Wer]{5} [bist]{6} [du]{4}?» [Jesus]{9,10} [sagte]{7} [zu ihnen]{8}: «[Wozu]{13,14} [rede ich]{16} [überhaupt]{11,12} [noch]{15} [zu euch]{17}?",
 "JHN.8.26": "[Vieles]{1} [habe ich]{2} [über]{3} [euch]{4} [zu reden]{5} und{6} [zu richten]{7}; [aber]{8} [der]{9} [mich]{11} [gesandt hat]{10}, [ist]{13} [wahrhaftig]{12}, [und ich]{14} [rede]{20} [zur]{21,22} [Welt]{23} [das]{19}, [was]{15} [ich]{16} [von]{17} [ihm]{18} [gehört habe]{16}.»",
 "JHN.8.27": "[Sie erkannten]{2} [nicht]{1}, [dass]{3} [er]{7} [zu ihnen]{6} [vom]{4} [Vater]{5} [sprach]{7}.",
 "JHN.8.28": "[Da]{2} [sagte]{1} [Jesus]{3,4}: «[Wenn]{5} [ihr]{6} [den Menschensohn]{7-10} [erhöht habt]{6}, [dann]{11} [werdet ihr erkennen]{12}, [dass]{13} [ich]{14} [bin]{15} und{16} [nichts]{20} [von]{17} [mir selbst aus]{18} [tue]{19}, [sondern]{21} [so]{27} [rede]{28}, [wie]{22} [mich]{24} [der Vater]{25,26} [gelehrt hat]{23}.",
 "JHN.8.29": "Und{1} [der]{2} [mich]{4} [gesandt hat]{3}, [ist]{7} [mit]{5} [mir]{6}; [er hat]{9} [mich]{10} [nicht]{8} [allein]{11} [gelassen]{9}, [denn]{12} [ich]{13} [tue]{17} [allezeit]{18}, [was]{14} [ihm]{16} [gefällt]{15}.»",
 "JHN.8.30": "[Als er]{2} [das]{1} [redete]{3}, [glaubten]{5} [viele]{4} [an]{6} [ihn]{7}.",
 "JHN.8.31": "[Da]{2} [sagte]{1} [Jesus]{3,4} [zu]{5} [den]{6} [Juden]{9}, [die]{7} [ihm]{8} [geglaubt hatten]{7}: «[Wenn]{10} [ihr]{11} [in]{13} [meinem]{16,17} [Wort]{14,15} [bleibt]{12}, [seid ihr]{21} [wahrhaft]{18} [meine]{20} [Jünger]{19},",
 "JHN.8.32": "und{1} [ihr werdet]{2} [die Wahrheit]{3,4} [erkennen]{2}, und{5} [die Wahrheit]{6,7} [wird]{8} [euch]{9} [frei machen]{8}.»",
 "JHN.8.33": "[Sie antworteten]{1} [ihm]{2,3}: «[Wir sind]{6} [Nachkommen]{4} [Abrahams]{5} und{7} [haben]{9} [niemandem]{8} [jemals]{10} [als Sklaven gedient]{9}. [Wie]{11} [sagst]{13} [du]{12} da: ‹[Ihr werdet]{16} [frei]{15} [werden]{16}›?» ~14(ὅτι leitet die direkte Rede ein)",
 "JHN.8.34": "[Jesus]{3,4} [antwortete]{1} [ihnen]{2}: «[Amen]{5}, [amen]{6}, [ich sage]{7} [euch]{8}: [Jeder]{10}, [der]{11} [die Sünde]{13,14} [tut]{12}, [ist]{16} [ein Sklave]{15} [der Sünde]{17,18}. ~9(ὅτι leitet die direkte Rede ein)",
 "JHN.8.35": "[Der]{1} [Sklave]{3} [aber]{2} [bleibt]{5} [nicht]{4} [in Ewigkeit]{9-11} [im]{6,7} [Haus]{8}; [der]{12} [Sohn]{13} [bleibt]{14} [in Ewigkeit]{15-17}.",
 "JHN.8.36": "[Wenn]{1} [nun]{2} [der Sohn]{3,4} [euch]{5} [frei macht]{6}, [werdet ihr]{9} [wirklich]{7} [frei]{8} [sein]{9}.",
 "JHN.8.37": "[Ich weiss]{1}, [dass]{2} [ihr]{5} [Nachkommen]{3} [Abrahams]{4} [seid]{5}; [aber]{6} [ihr sucht]{7} [mich]{8} [zu töten]{9}, [weil]{10} [mein]{13,14} [Wort]{11,12} [in]{17} [euch]{18} [keinen Raum findet]{15,16}.",
 "JHN.8.38": "[Was]{1} [ich]{2} [beim]{4,5} [Vater]{6} [gesehen habe]{3}, [rede ich]{7}; und{8} [ihr]{9} [tut]{16} [also]{10}, [was]{11} [ihr]{12} [vom]{13,14} [Vater]{15} [gehört habt]{12}.»",
 "JHN.8.39": "[Sie antworteten]{1} und{2} [sagten]{3} [zu ihm]{4}: «[Unser]{7} [Vater]{5,6} [ist]{9} [Abraham]{8}.» [Jesus]{12,13} [sagt]{10} [zu ihnen]{11}: «[Wenn]{14} [ihr]{18} [Kinder]{15} [Abrahams]{16,17} [seid]{18}, [würdet ihr]{23} [die Werke]{19,20} [Abrahams]{21,22} [tun]{23};",
 "JHN.8.40": "[nun]{1} [aber]{2} [sucht ihr]{3} [mich]{4} [zu töten]{5}, [einen Menschen]{6}, [der]{7} [euch]{10} [die Wahrheit]{8,9} [gesagt hat]{11}, [die]{12} [ich]{13} [bei]{14} [Gott]{15,16} [gehört habe]{13}. [Das]{17} [hat]{20} [Abraham]{18} [nicht]{19} [getan]{20}.",
 "JHN.8.41": "[Ihr]{1} [tut]{2} [die Werke]{3,4} [eures]{7} [Vaters]{5,6}.» [Sie sagten]{8} [zu ihm]{9}: «[Wir]{10} [sind]{14} [nicht]{13} [aus]{11} [Unzucht]{12} [geboren]{14}; [einen]{15} [Vater]{16} [haben wir]{17}: [Gott]{18,19}.»",
 "JHN.8.42": "[Jesus]{3,4} [sagte]{1} [zu ihnen]{2}: «[Wenn]{5} [Gott]{6,7} [euer]{9} [Vater]{8} [wäre]{10}, [würdet]{12} [ihr]{11} [mich]{13} [lieben]{11}; [denn]{15} [ich]{14} [bin]{19} [von]{16} [Gott]{17,18} [ausgegangen]{19} und{20} [bin hier]{21}. [Denn]{23} [ich bin]{26} [auch nicht]{22} [von]{24} [mir selbst aus]{25} [gekommen]{26}, [sondern]{27} [jener]{28} [hat]{30} [mich]{29} [gesandt]{30}.",
 "JHN.8.43": "[Warum]{1,2} [versteht ihr]{8} [meine]{5,6} [Rede]{3,4} [nicht]{7}? [Weil]{9} [ihr]{11} [mein]{15,16} [Wort]{13,14} [nicht]{10} [hören]{12} [könnt]{11}.",
 "JHN.8.44": "[Ihr]{1} [stammt]{7} [vom]{2,3} [Vater]{4}, [dem Teufel]{5,6}, und{8} [die Begierden]{9,10} [eures]{13} [Vaters]{11,12} [wollt ihr]{14} [tun]{15}. [Jener]{16} [war]{18} [ein Menschenmörder]{17} [von]{19} [Anfang an]{20}, und{21} [er steht]{26} [nicht]{25} [in]{22} [der Wahrheit]{23,24}, [denn]{27} [Wahrheit]{30} [ist]{29} [nicht]{28} [in]{31} [ihm]{32}. [Wenn]{33} [er]{34} [die Lüge]{35,36} [redet]{34}, [redet er]{40} [aus]{37} [dem Eigenen]{38,39}, [denn]{41} [er ist]{43} [ein Lügner]{42} und{44} [der Vater]{45,46} [davon]{47}.",
 "JHN.8.45": "[Mir]{9} [aber]{2} [glaubt ihr]{8} [nicht]{7}, [weil]{3} [ich]{1} [die Wahrheit]{4,5} [sage]{6}.",
 "JHN.8.46": "[Wer]{1} [von]{2} [euch]{3} [überführt]{4} [mich]{5} [einer Sünde]{6,7}? [Wenn]{8} [ich]{10} [die Wahrheit]{9} [sage]{10}, [warum]{11,12} [glaubt]{15} [ihr]{13} [mir]{16} [nicht]{14}?",
 "JHN.8.47": "[Wer]{1} [aus]{3} [Gott]{4,5} [ist]{2}, [hört]{10} [die Worte]{6,7} [Gottes]{8,9}; [darum]{11,12} [hört]{15} [ihr]{13} [nicht]{14}, [weil]{16} [ihr]{21} [nicht]{20} [aus]{17} [Gott]{18,19} [seid]{21}.»",
 "JHN.8.48": "[Die Juden]{2,3} [antworteten]{1} und{4} [sagten]{5} [zu ihm]{6}: «[Sagen]{9} [wir]{10} [nicht]{7} [mit Recht]{8}, [dass]{11} [du]{14} [ein Samaritaner]{12} [bist]{13} und{15} [einen Dämon]{16} [hast]{17}?»",
 "JHN.8.49": "[Jesus]{2} [antwortete]{1}: «[Ich]{3} [habe]{6} [keinen]{5} [Dämon]{4}, [sondern]{7} [ich ehre]{8} [meinen]{11} [Vater]{9,10}, und{12} [ihr]{13} [entehrt]{14} [mich]{15}.",
 "JHN.8.50": "[Ich]{1} [aber]{2} [suche]{4} [nicht]{3} [meine]{7} [Ehre]{5,6}; [es gibt]{8} [einen]{9}, [der sie sucht]{10} und{11} [richtet]{12}.",
 "JHN.8.51": "[Amen]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Wenn]{5} [jemand]{6} [mein]{7,8} [Wort]{9} [bewahrt]{10}, [wird er]{14} [den Tod]{11} [in Ewigkeit]{15-17} [gewiss nicht]{12,13} [sehen]{14}.»",
 "JHN.8.52": "[Die Juden]{3,4} [sagten]{1} [zu ihm]{2}: «[Jetzt]{5} [haben wir erkannt]{6}, [dass]{7} [du]{9} [einen Dämon]{8} [hast]{9}. [Abraham]{10} [ist gestorben]{11} und{12} [die Propheten]{13,14}, und{15} [du]{16} [sagst]{17}: ‹[Wenn]{18} [jemand]{19} [mein]{22} [Wort]{20,21} [bewahrt]{23}, [wird er]{26} [den Tod]{27} [in Ewigkeit]{28-30} [gewiss nicht]{24,25} [schmecken]{26}.›",
 "JHN.8.53": "[Bist]{4} [du]{2} [etwa]{1} [grösser]{3} [als]{5} [unser]{7} [Vater]{6} [Abraham]{8}, [der]{9} [gestorben ist]{10}? [Auch]{11} [die Propheten]{12,13} [sind gestorben]{14}. [Zu wem]{15} [machst du]{17} [dich selbst]{16}?»",
 "JHN.8.54": "[Jesus]{2} [antwortete]{1}: «[Wenn]{3} [ich]{4} [mich selbst]{6} [verherrliche]{5}, [ist]{11} [meine]{9} [Ehre]{7,8} [nichts]{10}. [Es ist]{12} [mein]{15} [Vater]{13,14}, [der]{16} [mich]{18} [verherrlicht]{17}, [von dem]{19} [ihr]{20} [sagt]{21}: ‹[Er ist]{25} [unser]{24} [Gott]{23}›, ~22(ὅτι leitet die direkte Rede ein)",
 "JHN.8.55": "und{1} [ihr habt]{3} [ihn]{4} [nicht]{2} [erkannt]{3}; [ich]{5} [aber]{6} [kenne]{7} [ihn]{8}. [Und wenn]{9} [ich sagte]{10}: ‹[Ich kenne]{13} [ihn]{14} [nicht]{12}›, [wäre ich]{15} [ein Lügner]{18} [gleich]{16} [euch]{17}. [Aber]{19} [ich kenne]{20} [ihn]{21} und{22} [bewahre]{26} [sein]{25} [Wort]{23,24}. ~11(ὅτι leitet die direkte Rede ein)",
 "JHN.8.56": "[Abraham]{1}, [euer]{4} [Vater]{2,3}, [jubelte]{5}, [dass]{6} [er]{7} [meinen]{10,11} [Tag]{8,9} [sehen sollte]{7}, und{12} [er sah ihn]{13} und{14} [freute sich]{15}.»",
 "JHN.8.57": "[Da]{2} [sagten]{1} [die Juden]{3,4} [zu]{5} [ihm]{6}: «[Du bist]{10} [noch nicht]{9} [fünfzig]{7} [Jahre]{8} [alt]{10} und{11} [hast]{13} [Abraham]{12} [gesehen]{13}?»",
 "JHN.8.58": "[Jesus]{3} [sagte]{1} [zu ihnen]{2}: «[Amen]{4}, [amen]{5}, [ich sage]{6} [euch]{7}: [Bevor]{8} [Abraham]{9} [wurde]{10}, [bin]{12} [ich]{11}.»",
 "JHN.8.59": "[Da]{2} [hoben sie]{1} [Steine]{3} [auf]{1}, [um]{4} sie [auf]{6} [ihn]{7} [zu werfen]{5}. [Jesus]{8} [aber]{9} [verbarg sich]{10} und{11} [ging]{12} [aus]{13} [dem]{14} [Tempel]{15} [hinaus]{12}.",
 # ------------------------------------------------------------ Kapitel 9
 "JHN.9.1": "Und{1} [im Vorübergehen]{2} [sah er]{3} [einen Menschen]{4}, [blind]{5} [von]{6} [Geburt an]{7}.",
 "JHN.9.2": "Und{1} [seine]{6} [Jünger]{4,5} [fragten]{2} [ihn]{3} [und sagten]{7}: «[Rabbi]{8}, [wer]{9} [hat gesündigt]{10}, [dieser]{11} [oder]{12} [seine]{15} [Eltern]{13,14}, [sodass]{16} [er]{18} [blind]{17} [geboren wurde]{18}?»",
 "JHN.9.3": "[Jesus]{2} [antwortete]{1}: «[Weder]{3} [dieser]{4} [hat gesündigt]{5} [noch]{6} [seine]{9} [Eltern]{7,8}, [sondern]{10} es geschah, [damit]{11} [die Werke]{13,14} [Gottes]{15,16} [an]{17} [ihm]{18} [offenbar werden]{12}.",
 "JHN.9.4": "[Wir]{1} [müssen]{2} [die Werke]{4,5} [dessen]{6} [wirken]{3}, [der]{7} [mich]{8} [gesandt hat]{7}, [solange]{9} [es Tag]{10} [ist]{11}; [es kommt]{12} [die Nacht]{13}, [in der]{14} [niemand]{15} [wirken]{17} [kann]{16}.",
 "JHN.9.5": "[Solange]{1} [ich]{5} [in]{2} [der Welt]{3,4} [bin]{5}, [bin ich]{7} [das Licht]{6} [der Welt]{8,9}.»",
 "JHN.9.6": "[Als er]{2} [das]{1} [gesagt hatte]{2}, [spuckte er]{3} [auf die Erde]{4} und{5} [machte]{6} [einen Brei]{7} [aus]{8} [dem]{9} [Speichel]{10} und{11} [strich]{12} [ihm]{13} [den]{14} [Brei]{15} [auf]{16} [die]{17} [Augen]{18}",
 "JHN.9.7": "und{1} [sagte]{2} [zu ihm]{3}: «[Geh]{4}, [wasch dich]{5} [im]{6,7} [Teich]{8} [Siloam]{9,10}» ([das]{11} [heisst übersetzt]{12}: «[Gesandter]{13}»). [Da]{15} [ging er hin]{14} und{16} [wusch sich]{17} und{18} [kam]{19} [sehend]{20} zurück.",
 "JHN.9.8": "[Die Nachbarn]{1,3} [nun]{2} und{4} [die]{5}, [die]{6} [ihn]{7} [früher]{8,9} [als]{10} [Bettler]{11,12} [gesehen hatten]{6}, [sagten]{13}: «[Ist]{16} [das]{15} [nicht]{14} [der]{17}, der [dasass]{18} und{19} [bettelte]{20}?»",
 "JHN.9.9": "[Andere]{1} [sagten]{2}: «[Er]{4} [ist es]{5}.» [Andere]{6} [sagten]{7}: «[Nein]{8}, [aber]{9} [er ist]{12} [ihm]{11} [ähnlich]{10}.» [Er selbst]{13} [sagte]{14}: «[Ich]{16} [bin es]{17}.» ~3(ὅτι leitet die direkte Rede ein) ~15(ὅτι leitet die direkte Rede ein)",
 "JHN.9.10": "[Da]{2} [sagten sie]{1} [zu ihm]{3}: «[Wie]{4} [sind]{5} [dir]{6} [die Augen]{7,8} [geöffnet worden]{5}?»",
 "JHN.9.11": "[Er]{2} [antwortete]{1}: «[Der Mensch]{3,4}, [der]{5} [Jesus]{7} [heisst]{6}, [machte]{9} [einen Brei]{8} und{10} [strich ihn]{11} [auf]{11} [meine]{12} [Augen]{13,14} und{15} [sagte]{16} [zu mir]{17}: ‹[Geh]{19} [zum]{20,21} [Siloam]{22} und{23} [wasch dich]{24}!› [Da]{26} [ging ich hin]{25}, und{27} [als ich mich gewaschen hatte]{28}, [wurde ich sehend]{29}.» ~18(ὅτι leitet die direkte Rede ein)",
 "JHN.9.12": "Und{1} [sie sagten]{2} [zu ihm]{3}: «[Wo]{4} [ist]{5} [er]{6}?» [Er sagt]{7}: «[Ich weiss]{9} [es nicht]{8}.»",
 "JHN.9.13": "[Sie bringen]{1} [ihn]{2}, [den]{6} [früher]{7} [Blinden]{8}, [zu]{3} [den Pharisäern]{4,5}.",
 "JHN.9.14": "[Es war]{1} [aber]{2} [Sabbat]{3}, [als]{4-6} [Jesus]{10,11} [den]{7} [Brei]{8} [machte]{9} und{12} [ihm]{14} [die Augen]{15,16} [öffnete]{13}.",
 "JHN.9.15": "[Nun]{2} [fragten]{3} [ihn]{4} [wieder]{1} [auch]{5} [die Pharisäer]{6,7}, [wie]{8} [er sehend geworden sei]{9}. [Er]{10} [aber]{11} [sagte]{12} [zu ihnen]{13}: «[Einen Brei]{14} [hat er]{15} [mir]{16} [auf]{17} [die Augen]{18,19} [gelegt]{15}, und{20} [ich wusch mich]{21}, und{22} [ich sehe]{23}.»",
 "JHN.9.16": "[Da]{2} [sagten]{1} [einige]{6} [von]{3} [den Pharisäern]{4,5}: «[Dieser]{9} [Mensch]{12,13} [ist]{8} [nicht]{7} [von]{10} [Gott]{11}, [denn]{14} [er hält]{18} [den Sabbat]{15,16} [nicht]{17}.» [Andere]{19} [sagten]{20}: «[Wie]{21} [kann]{22} [ein sündiger]{24} [Mensch]{23} [solche]{25} [Zeichen]{26} [tun]{27}?» Und{28} [es gab]{30} [eine Spaltung]{29} [unter]{31} [ihnen]{32}.",
 "JHN.9.17": "[Da]{2} [sagen sie]{1} [wieder]{5} [zu dem]{3} [Blinden]{4}: «[Was]{6} [sagst]{8} [du]{7} [über]{9} [ihn]{10}, [da]{11} [er]{12} [dir]{13} [die Augen]{14,15} [geöffnet hat]{12}?» [Er]{16} [aber]{17} [sagte]{18}: «[Er ist]{21} [ein Prophet]{20}.» ~19(ὅτι leitet die direkte Rede ein)",
 "JHN.9.18": "[Die Juden]{4,5} [glaubten]{2} [nun]{3} [nicht]{1} [von]{6} [ihm]{7}, [dass]{8} [er]{9} [blind]{10} [gewesen]{9} und{11} [sehend geworden war]{12}, [bis]{13,14} [sie]{15} [die Eltern]{16,17} [dessen]{18,19} [riefen]{15}, [der sehend geworden war]{20},",
 "JHN.9.19": "und{1} [fragten]{2} [sie]{3}: «[Ist]{6} [das]{5} [euer]{9} [Sohn]{7,8}, [von dem]{10} [ihr]{11} [sagt]{12}, [er sei]{15} [blind]{14} [geboren]{15}? [Wie]{16} [sieht er]{18} [denn]{17} [jetzt]{19}?» ~4(λέγοντες «sagend» vor der direkten Rede nicht eigens wiedergegeben) ~13(ὅτι leitet die indirekte Rede ein)",
 "JHN.9.20": "[Da]{2} [antworteten]{1} [seine]{5} [Eltern]{3,4} und{6} [sagten]{7}: «[Wir wissen]{8}, [dass]{9} [das]{10} [unser]{14} [Sohn]{12,13} [ist]{11} und{15} [dass]{16} [er]{18} [blind]{17} [geboren wurde]{18};",
 "JHN.9.21": "[wie]{1} [er]{4} [aber]{2} [jetzt]{3} [sieht]{4}, [wissen wir]{6} [nicht]{5}, [oder]{7} [wer]{8} [ihm]{10} [die Augen]{11,12} [geöffnet hat]{9}, [wissen]{15} [wir]{13} [nicht]{14}. [Fragt]{17} [ihn]{16}, [er ist alt genug]{18,19}, [er selbst]{20} [wird]{23} [für]{21} [sich]{22} [reden]{23}.»",
 "JHN.9.22": "[Das]{1} [sagten]{2} [seine]{5} [Eltern]{3,4}, [weil]{6} [sie]{7} [die Juden]{8,9} [fürchteten]{7}; [denn]{11} [die Juden]{13,14} [hatten]{12} [schon]{10} [beschlossen]{12}, [dass]{15}, [wenn]{16} [jemand]{17} [ihn]{18} [als Christus]{20} [bekenne]{19}, er [aus der Synagoge ausgeschlossen]{21} [werde]{22}.",
 "JHN.9.23": "[Darum]{1,2} [sagten]{6} [seine]{5} [Eltern]{3,4}: «[Er ist alt genug]{8,9}, [fragt]{11} [ihn]{10}!» ~7(ὅτι leitet die direkte Rede ein)",
 "JHN.9.24": "[Da]{2} [riefen sie]{1} [den Menschen]{3,4}, [der]{7} [blind]{9} [gewesen war]{8}, [zum zweiten Mal]{5,6} und{10} [sagten]{11} [zu ihm]{12}: «[Gib]{13} [Gott]{15,16} [die Ehre]{14}! [Wir]{17} [wissen]{18}, [dass]{19} [dieser]{20} [Mensch]{21,22} [ein Sünder]{23} [ist]{24}.»",
 "JHN.9.25": "[Da]{2} [antwortete]{1} [er]{3}: «[Ob]{4} [er]{6} [ein Sünder]{5} [ist]{6}, [weiss ich]{8} [nicht]{7}; [eines]{9} [weiss ich]{10}: [dass]{11} [ich]{13} [blind]{12} [war]{13} und [jetzt]{14} [sehe]{15}.»",
 "JHN.9.26": "[Da]{2} [sagten sie]{1} [zu ihm]{3}: «[Was]{4} [hat er]{5} [mit dir]{6} [gemacht]{5}? [Wie]{7} [hat er]{8} [dir]{9} [die Augen]{10,11} [geöffnet]{8}?»",
 "JHN.9.27": "[Er antwortete]{1} [ihnen]{2}: «[Ich habe]{3} [es euch]{4} [schon]{5} [gesagt]{3}, und{6} [ihr habt]{8} [nicht]{7} [zugehört]{8}. [Warum]{9} [wollt ihr]{11} es [noch einmal]{10} [hören]{12}? [Wollt]{16} [etwa]{13} [auch]{14} [ihr]{15} [seine]{17} [Jünger]{18} [werden]{19}?»",
 "JHN.9.28": "[Sie beschimpften]{1} [ihn]{2} und{3} [sagten]{4}: «[Du]{5} [bist]{7} [ein Jünger]{6} [von jenem]{8}, [wir]{9} [aber]{10} [sind]{13} [Jünger]{14} [des Mose]{11,12}.",
 "JHN.9.29": "[Wir]{1} [wissen]{2}, [dass]{3} [Gott]{6,7} [zu Mose]{4} [geredet hat]{5}; [von diesem]{8} [aber]{9} [wissen wir]{11} [nicht]{10}, [woher]{12} [er ist]{13}.»",
 "JHN.9.30": "[Der Mensch]{2,3} [antwortete]{1} und{4} [sagte]{5} [zu ihnen]{6}: «[Darin]{7,8} [liegt]{12} [ja]{9} [das]{10} [Erstaunliche]{11}, [dass]{13} [ihr]{14} [nicht]{15} [wisst]{16}, [woher]{17} [er ist]{18}, und{19} [er hat]{20} [mir]{21} [die Augen]{22,23} [geöffnet]{20}!",
 "JHN.9.31": "[Wir wissen]{1}, [dass]{2} [Gott]{4,5} [nicht]{6} [auf Sünder]{3} [hört]{7}; [sondern]{8} [wenn]{9} [jemand]{10} [gottesfürchtig]{11} [ist]{12} und{13} [seinen]{16} [Willen]{14,15} [tut]{17}, [auf den]{18} [hört er]{19}.",
 "JHN.9.32": "[Seit Menschengedenken]{1-3} [hat man]{5} [nicht]{4} [gehört]{5}, [dass]{6} [jemand]{8} [die Augen]{9} [eines von Geburt]{11} [Blinden]{10} [geöffnet hat]{7}.",
 "JHN.9.33": "[Wenn]{1} [dieser]{4} [nicht]{2} [von]{5} [Gott]{6} [wäre]{3}, [könnte er]{8} [nichts]{7,10} [tun]{9}.»",
 "JHN.9.34": "[Sie antworteten]{1} und{2} [sagten]{3} [zu ihm]{4}: «[Du]{7} [bist]{8} [ganz]{9} [in]{5} [Sünden]{6} [geboren]{8}, und{10} [du]{11} [belehrst]{12} [uns]{13}?» Und{14} [sie warfen]{15} [ihn]{16} [hinaus]{17}.",
 "JHN.9.35": "[Jesus]{2} [hörte]{1}, [dass]{3} [sie]{4} [ihn]{5} [hinaus]{6}[geworfen hatten]{4}, und{7} [als er]{8} [ihn]{9} [fand]{8}, [sagte er]{10}: «[Glaubst]{12} [du]{11} [an]{13} [den Menschensohn]{14-17}?»",
 "JHN.9.36": "[Er]{2} [antwortete]{1} und{3} [sagte]{4}: «[Und]{5} [wer]{6} [ist]{7} es, [Herr]{8}, [damit]{9} [ich]{10} [an]{11} [ihn]{12} [glauben kann]{10}?»",
 "JHN.9.37": "[Jesus]{3,4} [sagte]{1} [zu ihm]{2}: «[Du hast]{6} [ihn]{7} [ja]{5} [gesehen]{6}, und{8} [der]{9} [mit]{11} [dir]{12} [redet]{10}, [der]{13} [ist es]{14}.»",
 "JHN.9.38": "[Er]{1} [aber]{2} [sagte]{3}: «[Ich glaube]{4}, [Herr]{5}!» Und{6} [er fiel]{7} [vor ihm]{8} [nieder]{7}.",
 "JHN.9.39": "Und{1} [Jesus]{3,4} [sagte]{2}: «[Zum]{5} [Gericht]{6} [bin]{12} [ich]{7} [in]{8} [diese]{11} [Welt]{9,10} [gekommen]{12}, [damit]{13} [die]{14} [nicht]{15} [Sehenden]{16} [sehen]{17} und{18} [die]{19} [Sehenden]{20} [blind]{21} [werden]{22}.»",
 "JHN.9.40": "[Das]{5} [hörten]{1} [von]{2} [den Pharisäern]{3,4} [die]{6}, [die]{9} [bei]{7} [ihm]{8} [waren]{9}, und{10} [sagten]{11} [zu ihm]{12}: «[Sind]{17} [etwa]{13} [auch]{14} [wir]{15} [blind]{16}?»",
 "JHN.9.41": "[Jesus]{3,4} [sagte]{1} [zu ihnen]{2}: «[Wenn]{5} [ihr]{7} [blind]{6} [wärt]{7}, [hättet ihr]{9,10} [keine]{8} [Sünde]{11}; [nun]{12} [aber]{13} [sagt ihr]{14}: ‹[Wir sehen]{16}.› [Eure]{19} [Sünde]{17,18} [bleibt]{20}.» ~15(ὅτι leitet die direkte Rede ein)",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 8
 "JHN.8.1": "[De Jesus]{1} [aber]{2} [isch]{3} [uf]{4} [de]{5} [Ölberg]{6-8} [gange]{3}.",
 "JHN.8.2": "[Früe am Morge]{1} [aber]{2} [isch er]{4} [wider]{3} [in]{5} [de]{6} [Tämpel]{7} [choo]{4}, und{8} [s ganz]{9,10} [Volk]{11} [isch]{12} [dezue choo]{12}; und{13} [er isch abgsässe]{14} [und hät]{15} [si]{16} [glehrt]{15}.",
 "JHN.8.3": "[Da]{2} [bringed]{1} [d Schriftgleerte]{3,4} und{5} [d Pharisäer]{6,7} [e Frau]{10} [zu]{8} [ihm]{9}, [wo mer]{13} [bim]{11} [Ehebruch]{12} [verwütscht hät]{13}; und{14} [si stelled]{15} [si]{16} [i]{17} [d Mitti]{18}",
 "JHN.8.4": "und [säged]{1} [zu ihm]{2}, [zum]{3} en [uf d Prob z stele]{3}: «[Lehrer]{4}, [die]{5} [Frau]{6,7} [isch]{8} [uf früscher Tat]{9,10} [bim Ehebruch]{11} [verwütscht worde]{8}.",
 "JHN.8.5": "[Im]{1,3} [Gsetz]{4} [aber]{2} [hät]{7} [üs]{6} [de Mose]{5} [befole]{7}, [settigi]{8,9} [z steinige]{10}. [Was]{13} [seisch]{14} [jetzt]{12} [du]{11}?»",
 "JHN.8.6": "[Das]{1} [händ si]{3} [aber]{2} [gseit]{3}, [zum]{4} [en]{5} [uf d Prob z stele]{4}, [demit]{6} [si]{7} [en]{9} [chönted]{7} [aachlage]{8}. [De Jesus]{10,12} [aber]{11} [hät sich abebückt]{13,14} [und hät]{17} [mit em]{15} [Finger]{16} [uf]{18} [de]{19} [Bode]{20} [gschribe]{17}, [ohni uf si iizgaa]{21,22}.",
 "JHN.8.7": "[Wo]{1} [si]{3} [en]{5} [aber]{2} [immer wiiter]{3} [gfröget händ]{4}, [hät er sich ufgrichtet]{6} [und hät]{7} [zu]{8} [ine]{9} [gseit]{7}: «[Wer]{10} [vo eu]{12} [ohni Sünd isch]{11}, [söll]{18} [als Erschte]{13} [de]{16} [Stei]{17} [uf]{14} [si]{15} [rüere]{18}.»",
 "JHN.8.8": "Und{1} [wider]{2} [hät er sich abebückt]{3,4} [und hät]{5} [uf]{6} [de]{7} [Bode]{8} [gschribe]{5}.",
 "JHN.8.9": "[Si]{1} [aber]{2} [händ das ghört]{3}, und{4} [vom]{5,6} [Gwüsse]{7} [überfüert]{8} [sind si]{9} [eine]{10} [nach]{11} [em andere]{12} [usegange]{9}, [aagfange]{13} [bi]{14} [de]{15} [Ältischte]{16}; und{17} [de Jesus]{20,21} [isch]{18} [elei]{19} [zruggblibe]{18}, und{22} [d]{23} [Frau]{24}, [wo]{27} [i]{25} [de Mitti]{26} [gstande isch]{27}.",
 "JHN.8.10": "[De Jesus]{3,4} [aber]{2} [hät sich ufgrichtet]{1}, und{5} [won er]{7} [niemer]{6} [gseh hät]{7} [usser]{8} [de]{9} [Frau]{10}, [hät er]{11} [zu ere]{12} [gseit]{11}: «[Wo]{13} [sind]{14} [di säbe]{15}, [dini]{18} [Aachläger]{16,17}? [Hät]{21} [di]{20} [niemer]{19} [verurteilt]{21}?»",
 "JHN.8.11": "[Si]{1} [aber]{2} [hät gseit]{3}: «[Niemer]{4}, [Herr]{5}.» [De Jesus]{8,9} [aber]{7} [hät gseit]{6}: «[Au]{10} [ich]{11} [verurteile]{13} [di]{12} [nöd]{10}. [Gang]{14}, und{15} [sündig]{17} [nüme]{16}!»⟧",
 "JHN.8.12": "[Wider]{1} [hät]{4} [de Jesus]{5,6} [dänn]{2} [zu ine]{3} [gredt]{4} [und gseit]{7}: «[Ich]{8} [bi]{9} [s Liecht]{10,11} [vo de Wält]{12,13}. [Wer]{14} [mir]{16} [nachegaat]{15}, [wird]{19} [sicher nöd]{17,18} [i]{20} [de Fiischteri]{21,22} [laufe]{19}, [sondern]{23} [wird]{24} [s Liecht]{25,26} [vom Läbe]{27,28} [ha]{24}.»",
 "JHN.8.13": "[Dänn]{2} [händ]{1} [d Pharisäer]{4,5} [zu ihm]{3} [gseit]{1}: «[Du]{6} [leisch]{9} [über]{7} [dich sälber]{8} [Zügnis ab]{9}; [dis]{12} [Zügnis]{10,11} [isch]{14} [nöd]{13} [wahr]{15}.»",
 "JHN.8.14": "[De Jesus]{2} [hät]{1} [ine]{5} [gantwortet]{1} und{3} [gseit]{4}: «[Au wänn]{6} [ich]{7} [über]{9} [mich sälber]{10} [Zügnis ablegge]{8}, [isch]{12} [mis]{15} [Zügnis]{13,14} [wahr]{11}, [wil]{16} [ich weiss]{17}, [vo wo]{18} [ich choo bi]{19} und{20} [wohi]{21} [ich gaa]{22}; [ir]{23} [aber]{24} [wüssed]{26} [nöd]{25}, [vo wo]{27} [ich chume]{28} [oder]{29} [wohi]{30} [ich gaa]{31}.",
 "JHN.8.15": "[Ir]{1} [richted]{5} [nach]{2} [em]{3} [Fleisch]{4}, [ich]{6} [richte]{8} [niemer]{7,9}.",
 "JHN.8.16": "[Wänn]{2} [ich]{5} [aber]{4} [au]{1} [richte]{3}, [isch]{11} [mis]{8,9} [Urteil]{6,7} [wahr]{10}, [wil]{12} [ich]{15} [nöd]{14} [elei]{13} [bi]{15}, [sondern]{16} [ich]{17} und{18} [de Vatter]{22}, [wo]{19} [mich]{21} [gschickt hät]{20}.",
 "JHN.8.17": "[Au]{1,5} [i]{2} [eurem]{6,7} [Gsetz]{3,4} [staat gschribe]{8}, [dass]{9} [s Zügnis]{12,13} [vo zwei]{10} [Mänsche]{11} [wahr]{14} [isch]{15}.",
 "JHN.8.18": "[Ich]{1} [bi]{2} [dä]{3}, [wo]{4} [über]{5} [mich sälber]{6} [Zügnis ablegt]{4}, und{7} [über]{9} [mich]{10} [leit]{8} [de Vatter]{14} [Zügnis ab]{8}, [wo]{11} [mich]{13} [gschickt hät]{12}.»",
 "JHN.8.19": "[Dänn]{2} [händ si]{1} [zu ihm]{3} [gseit]{1}: «[Wo]{4} [isch]{5} [din]{8} [Vatter]{6,7}?» [De Jesus]{10} [hät gantwortet]{9}: «[Ir känned]{13} [weder]{11} [mich]{12} [no]{14} [min]{17} [Vatter]{15,16}; [wänn]{18} [ir]{20} [mich]{19} [känne würded]{20}, [würded ir]{25} [au]{21} [min]{24} [Vatter]{22,23} [känne]{26}.»",
 "JHN.8.20": "[Die]{1} [Wort]{2,3} [hät er]{4} [bi]{5} [de]{6} [Schatzchammer]{7} [gredt]{4}, [won er]{8} [im]{9,10} [Tämpel]{11} [glehrt hät]{8}; und{12} [niemer]{13} [hät]{14} [en]{15} [gfange gnoo]{14}, [wil]{16} [sini]{21} [Stund]{19,20} [no nöd]{17} [choo gsii isch]{18}.",
 "JHN.8.21": "[Dänn]{2} [hät er]{1} [wider]{3} [zu ine]{4} [gseit]{1}: «[Ich]{5} [gaa wäg]{6}, und{7} [ir wärded]{8} [mich]{9} [sueche]{8}, und{10} [ir wärded]{15} [i]{11} [eurer]{12,14} [Sünd]{13} [stärbe]{15}. [Wo]{16} [ich]{17} [hiigaa]{18}, [chönd]{21} [ir]{19} [nöd]{20} [härecho]{22}.»",
 "JHN.8.22": "[Dänn]{2} [händ]{1} [d Jude]{3,4} [gseit]{1}: «[Er wird]{6} [sich]{7} [doch nöd]{5} [sälber]{7} [umbringe]{6}, [wil]{8} [er seit]{9}: ‹[Wo]{10} [ich]{11} [hiigaa]{12}, [chönd]{15} [ir]{13} [nöd]{14} [härecho]{16}›?»",
 "JHN.8.23": "Und{1} [er hät]{2} [zu ine]{3} [gseit]{2}: «[Ir]{4} [sind]{8} [vo]{5} [unde]{6,7}, [ich]{9} [bi]{13} [vo]{10} [obe]{11,12}; [ir]{14} [sind]{19} [us]{15} [dere]{16} [Wält]{17,18}, [ich]{20} [bi]{22} [nöd]{21} [us]{23} [dere]{26} [Wält]{24,25}.",
 "JHN.8.24": "[Drum]{2} [han ich]{1} [eu]{3} [gseit]{1}, [dass]{4} [ir]{5} [i]{6} [eui]{7,9} [Sünde]{8} [wärded stärbe]{5}; [dänn]{11} [wänn]{10} [ir]{13} [nöd]{12} [glaubed]{13}, [dass]{14} [ich]{15} [bi]{16}, [wärded ir]{17} [i]{18} [eui]{19,21} [Sünde]{20} [stärbe]{17}.»",
 "JHN.8.25": "[Dänn]{2} [händ si]{1} [zu ihm]{3} [gseit]{1}: «[Wer]{5} [bisch]{6} [du]{4}?» [De Jesus]{9,10} [hät]{7} [zu ine]{8} [gseit]{7}: «[Für was]{13,14} [red ich]{16} [überhaupt]{11,12} [no]{15} [mit eu]{17}?",
 "JHN.8.26": "[Vil]{1} [han ich]{2} [über]{3} [eu]{4} [z säge]{5} und{6} [z richte]{7}; [aber]{8} [dä]{9}, [wo]{10} [mich]{11} [gschickt hät]{10}, [isch]{13} [wahrhaftig]{12}, [und ich]{14} [säg]{20} [de Wält]{21-23} [das]{19}, [was]{15} [ich]{16} [vo]{17} [ihm]{18} [ghört han]{16}.»",
 "JHN.8.27": "[Si händ]{2} [nöd]{1} [verstande]{2}, [dass]{3} [er]{7} [zu ine]{6} [vom]{4} [Vatter]{5} [gredt hät]{7}.",
 "JHN.8.28": "[Dänn]{2} [hät]{1} [de Jesus]{3,4} [gseit]{1}: «[Wänn]{5} [ir]{6} [de Mänschesohn]{7-10} [erhöcht händ]{6}, [dänn]{11} [wärded ir erchänne]{12}, [dass]{13} [ich]{14} [bi]{15} und{16} [nüüt]{20} [vo]{17} [mir sälber us]{18} [mache]{19}, [sondern]{21} [eso]{27} [rede]{28}, [wie]{22} [mich]{24} [de Vatter]{25,26} [glehrt hät]{23}.",
 "JHN.8.29": "Und{1} [dä]{2}, [wo]{3} [mich]{4} [gschickt hät]{3}, [isch]{7} [mit]{5} [mir]{6}; [er hät]{9} [mich]{10} [nöd]{8} [elei]{11} [gloo]{9}, [wil]{12} [ich]{13} [immer]{18} [tue]{17}, [was]{14} [ihm]{16} [gfallt]{15}.»",
 "JHN.8.30": "[Won er]{2} [das]{1} [gredt hät]{3}, [händ]{5} [vili]{4} [a]{6} [en]{7} [glaubt]{5}.",
 "JHN.8.31": "[Dänn]{2} [hät]{1} [de Jesus]{3,4} [zu]{5} [de]{6} [Jude]{9}, [wo]{7} [ihm]{8} [glaubt händ]{7}, [gseit]{1}: «[Wänn]{10} [ir]{11} [i]{13} [mim]{16,17} [Wort]{14,15} [bliibed]{12}, [sind ir]{21} [würkli]{18} [mini]{20} [Jünger]{19},",
 "JHN.8.32": "und{1} [ir wärded]{2} [d Wahrheit]{3,4} [erchänne]{2}, und{5} [d Wahrheit]{6,7} [wird]{8} [eu]{9} [frei mache]{8}.»",
 "JHN.8.33": "[Si händ]{1} [ihm]{2,3} [gantwortet]{1}: «[Mir sind]{6} [Nachkomme]{4} [vom Abraham]{5} und{7} [händ]{9} [niemertem]{8} [je]{10} [als Sklave dient]{9}. [Wie]{11} [seisch]{13} [du]{12} dänn: ‹[Ir wärded]{16} [frei]{15} [wärde]{16}›?» ~14(ὅτι leitet di diräkt Red ii)",
 "JHN.8.34": "[De Jesus]{3,4} [hät]{1} [ine]{2} [gantwortet]{1}: «[Amen]{5}, [amen]{6}, [ich säge]{7} [eu]{8}: [Jede]{10}, [wo]{11} [d Sünd]{13,14} [tuet]{12}, [isch]{16} [en Sklav]{15} [vo de Sünd]{17,18}. ~9(ὅτι leitet di diräkt Red ii)",
 "JHN.8.35": "[De]{1} [Sklav]{3} [aber]{2} [bliibt]{5} [nöd]{4} [i Ewigkeit]{9-11} [im]{6,7} [Huus]{8}; [de]{12} [Sohn]{13} [bliibt]{14} [i Ewigkeit]{15-17}.",
 "JHN.8.36": "[Wänn]{1} [also]{2} [de Sohn]{3,4} [eu]{5} [frei macht]{6}, [wärded ir]{9} [würkli]{7} [frei]{8} [sii]{9}.",
 "JHN.8.37": "[Ich weiss]{1}, [dass]{2} [ir]{5} [Nachkomme]{3} [vom Abraham]{4} [sind]{5}; [aber]{6} [ir sueched]{7} [mich]{8} [z töte]{9}, [wil]{10} [mis]{13,14} [Wort]{11,12} [in]{17} [eu]{18} [kei Platz findt]{15,16}.",
 "JHN.8.38": "[Was]{1} [ich]{2} [bim]{4,5} [Vatter]{6} [gseh han]{3}, [das red ich]{7}; und{8} [ir]{9} [tüend]{16} [also]{10}, [was]{11} [ir]{12} [vom]{13,14} [Vatter]{15} [ghört händ]{12}.»",
 "JHN.8.39": "[Si händ gantwortet]{1} und{2} [zu ihm]{4} [gseit]{3}: «[Üse]{7} [Vatter]{5,6} [isch]{9} [de Abraham]{8}.» [De Jesus]{12,13} [seit]{10} [zu ine]{11}: «[Wänn]{14} [ir]{18} [Chind]{15} [vom Abraham]{16,17} [sind]{18}, [würded ir]{23} [d Wärch]{19,20} [vom Abraham]{21,22} [tue]{23};",
 "JHN.8.40": "[jetzt]{1} [aber]{2} [sueched ir]{3} [mich]{4} [z töte]{5}, [en Mänsch]{6}, [wo]{7} [eu]{10} [d Wahrheit]{8,9} [gseit hät]{11}, [wo]{12} [ich]{13} [bi]{14} [Gott]{15,16} [ghört han]{13}. [Das]{17} [hät]{20} [de Abraham]{18} [nöd]{19} [gmacht]{20}.",
 "JHN.8.41": "[Ir]{1} [tüend]{2} [d Wärch]{3,4} [vo eurem]{7} [Vatter]{5,6}.» [Si händ]{8} [zu ihm]{9} [gseit]{8}: «[Mir]{10} [sind]{14} [nöd]{13} [us]{11} [Unzucht]{12} [gebore]{14}; [ein]{15} [Vatter]{16} [händ mir]{17}: [Gott]{18,19}.»",
 "JHN.8.42": "[De Jesus]{3,4} [hät]{1} [zu ine]{2} [gseit]{1}: «[Wänn]{5} [Gott]{6,7} [eue]{9} [Vatter]{8} [wär]{10}, [würded]{12} [ir]{11} [mich]{13} [liebe]{11}; [dänn]{15} [ich]{14} [bi]{19} [vo]{16} [Gott]{17,18} [usgange]{19} und{20} [bi da]{21}. [Ich bi]{26} [ja]{23} [au nöd]{22} [vo]{24} [mir sälber us]{25} [choo]{26}, [sondern]{27} [dä]{28} [hät]{30} [mich]{29} [gschickt]{30}.",
 "JHN.8.43": "[Werum]{1,2} [verstönd ir]{8} [mini]{5,6} [Red]{3,4} [nöd]{7}? [Wil]{9} [ir]{11} [mis]{15,16} [Wort]{13,14} [nöd]{10} [chönd]{11} [ghöre]{12}.",
 "JHN.8.44": "[Ir]{1} [stammed]{7} [vom]{2,3} [Vatter]{4}, [em Tüüfel]{5,6}, und{8} [d Glüscht]{9,10} [vo eurem]{13} [Vatter]{11,12} [wänd ir]{14} [tue]{15}. [Dä]{16} [isch]{18} [vo]{19} [Aafang aa]{20} [en Mänschemörder]{17} [gsii]{18}, und{21} [er staat]{26} [nöd]{25} [i]{22} [de Wahrheit]{23,24}, [wil]{27} [kei]{28} [Wahrheit]{30} [in]{31} [ihm]{32} [isch]{29}. [Wänn]{33} [er]{34} [d Lüüg]{35,36} [redt]{34}, [redt er]{40} [us]{37} [sim Eigete]{38,39}, [dänn]{41} [er isch]{43} [en Lüügner]{42} und{44} [de Vatter]{45,46} [devo]{47}.",
 "JHN.8.45": "[Mir]{9} [aber]{2} [glaubed ir]{8} [nöd]{7}, [wil]{3} [ich]{1} [d Wahrheit]{4,5} [säg]{6}.",
 "JHN.8.46": "[Wer]{1} [vo]{2} [eu]{3} [überfüert]{4} [mich]{5} [vo ere Sünd]{6,7}? [Wänn]{8} [ich]{10} [d Wahrheit]{9} [säg]{10}, [werum]{11,12} [glaubed]{15} [ir]{13} [mir]{16} [nöd]{14}?",
 "JHN.8.47": "[Wer]{1} [us]{3} [Gott]{4,5} [isch]{2}, [ghört]{10} [d Wort]{6,7} [vo Gott]{8,9}; [drum]{11,12} [ghöred]{15} [ir]{13} [nöd]{14}, [wil]{16} [ir]{21} [nöd]{20} [us]{17} [Gott]{18,19} [sind]{21}.»",
 "JHN.8.48": "[D Jude]{2,3} [händ gantwortet]{1} und{4} [zu ihm]{6} [gseit]{5}: «[Säged]{9} [mir]{10} [nöd]{7} [z Rächt]{8}, [dass]{11} [du]{14} [en Samaritaner]{12} [bisch]{13} und{15} [en Dämon]{16} [häsch]{17}?»",
 "JHN.8.49": "[De Jesus]{2} [hät gantwortet]{1}: «[Ich]{3} [han]{6} [kei]{5} [Dämon]{4}, [sondern]{7} [ich ehre]{8} [min]{11} [Vatter]{9,10}, und{12} [ir]{13} [entehred]{14} [mich]{15}.",
 "JHN.8.50": "[Ich]{1} [aber]{2} [suech]{4} [nöd]{3} [mini]{7} [Ehr]{5,6}; [es git]{8} [eine]{9}, [wo si suecht]{10} und{11} [richtet]{12}.",
 "JHN.8.51": "[Amen]{1}, [amen]{2}, [ich säge]{3} [eu]{4}: [Wänn]{5} [öpper]{6} [mis]{7,8} [Wort]{9} [bhaltet]{10}, [wird er]{14} [de Tod]{11} [i Ewigkeit]{15-17} [sicher nöd]{12,13} [gseh]{14}.»",
 "JHN.8.52": "[D Jude]{3,4} [händ]{1} [zu ihm]{2} [gseit]{1}: «[Jetzt]{5} [wüssed mir]{6}, [dass]{7} [du]{9} [en Dämon]{8} [häsch]{9}. [De Abraham]{10} [isch gstorbe]{11} und{12} [d Prophete]{13,14}, und{15} [du]{16} [seisch]{17}: ‹[Wänn]{18} [öpper]{19} [mis]{22} [Wort]{20,21} [bhaltet]{23}, [wird er]{26} [de Tod]{27} [i Ewigkeit]{28-30} [sicher nöd]{24,25} [versueche]{26}.›",
 "JHN.8.53": "[Bisch]{4} [du]{2} [öppe]{1} [grösser]{3} [als]{5} [üse]{7} [Vatter]{6} [Abraham]{8}, [wo]{9} [gstorbe isch]{10}? [Au]{11} [d Prophete]{12,13} [sind gstorbe]{14}. [Für wer]{15} [hältsch]{17} [dich sälber]{16}?»",
 "JHN.8.54": "[De Jesus]{2} [hät gantwortet]{1}: «[Wänn]{3} [ich]{4} [mich sälber]{6} [verherrliche]{5}, [isch]{11} [mini]{9} [Ehr]{7,8} [nüüt]{10}. [Es isch]{12} [min]{15} [Vatter]{13,14}, [wo]{16} [mich]{18} [verherrlicht]{17}, [vo däm]{19} [ir]{20} [säged]{21}: ‹[Er isch]{25} [üse]{24} [Gott]{23}›, ~22(ὅτι leitet di diräkt Red ii)",
 "JHN.8.55": "und{1} [ir händ]{3} [en]{4} [nöd]{2} [erchännt]{3}; [ich]{5} [aber]{6} [känne]{7} [en]{8}. [Und wänn]{9} [ich würd säge]{10}: ‹[Ich känne]{13} [en]{14} [nöd]{12}›, [wär ich]{15} [en Lüügner]{18} [gliich wie]{16} [ir]{17}. [Aber]{19} [ich känne]{20} [en]{21} und{22} [bhalte]{26} [sis]{25} [Wort]{23,24}. ~11(ὅτι leitet di diräkt Red ii)",
 "JHN.8.56": "[De Abraham]{1}, [eue]{4} [Vatter]{2,3}, [hät gjublet]{5}, [dass]{6} [er]{7} [min]{10,11} [Tag]{8,9} [söll gseh]{7}, und{12} [er hät en gseh]{13} und{14} [hät sich gfröit]{15}.»",
 "JHN.8.57": "[Dänn]{2} [händ]{1} [d Jude]{3,4} [zu]{5} [ihm]{6} [gseit]{1}: «[Du bisch]{10} [no nöd]{9} [füfzg]{7} [Jahr]{8} [alt]{10} und{11} [häsch]{13} [de Abraham]{12} [gseh]{13}?»",
 "JHN.8.58": "[De Jesus]{3} [hät]{1} [zu ine]{2} [gseit]{1}: «[Amen]{4}, [amen]{5}, [ich säge]{6} [eu]{7}: [Bevor]{8} [de Abraham]{9} [worde isch]{10}, [bin]{12} [ich]{11}.»",
 "JHN.8.59": "[Dänn]{2} [händ si]{1} [Stei]{3} [ufghebt]{1}, [zum]{4} [uf]{6} [en]{7} [z rüere]{5}. [De Jesus]{8} [aber]{9} [hät sich versteckt]{10} und{11} [isch]{12} [us]{13} [em]{14} [Tämpel]{15} [usegange]{12}.",
 # ------------------------------------------------------------ Kapitel 9
 "JHN.9.1": "Und{1} [im Verbiigaa]{2} [hät er]{3} [en Mänsch]{4} [gseh]{3}, [blind]{5} [vo]{6} [Geburt aa]{7}.",
 "JHN.9.2": "Und{1} [sini]{6} [Jünger]{4,5} [händ]{2} [en]{3} [gfröget]{2} [und gseit]{7}: «[Rabbi]{8}, [wer]{9} [hät gsündiget]{10}, [dä]{11} [oder]{12} [sini]{15} [Eltere]{13,14}, [dass]{16} [er]{18} [blind]{17} [gebore worde isch]{18}?»",
 "JHN.9.3": "[De Jesus]{2} [hät gantwortet]{1}: «[Weder]{3} [dä]{4} [hät gsündiget]{5} [no]{6} [sini]{9} [Eltere]{7,8}, [sondern]{10} es isch gscheh, [demit]{11} [d Wärch]{13,14} [vo Gott]{15,16} [a]{17} [ihm]{18} [offebar wärded]{12}.",
 "JHN.9.4": "[Mir]{1} [müend]{2} [d Wärch]{4,5} [vo däm]{6} [wirke]{3}, [wo]{7} [mich]{8} [gschickt hät]{7}, [solang]{9} [es Tag]{10} [isch]{11}; [es chunnt]{12} [d Nacht]{13}, [wo]{14} [niemer]{15} [cha]{16} [wirke]{17}.",
 "JHN.9.5": "[Solang]{1} [ich]{5} [i]{2} [de Wält]{3,4} [bi]{5}, [bin ich]{7} [s Liecht]{6} [vo de Wält]{8,9}.»",
 "JHN.9.6": "[Won er]{2} [das]{1} [gseit hät]{2}, [hät er]{3} [uf de Bode]{4} [gspöit]{3} und{5} [hät]{6} [us]{8} [em]{9} [Spöiz]{10} [en Brei]{7} [gmacht]{6} und{11} [hät]{12} [ihm]{13} [de]{14} [Brei]{15} [uf]{16} [d]{17} [Auge]{18} [gstriche]{12}",
 "JHN.9.7": "und{1} [hät]{2} [zu ihm]{3} [gseit]{2}: «[Gang]{4}, [wäsch di]{5} [im]{6,7} [Teich]{8} [Siloam]{9,10}» ([das]{11} [heisst übersetzt]{12}: «[Gschickte]{13}»). [Dänn]{15} [isch er hiigange]{14} und{16} [hät sich gwäsche]{17} und{18} [isch]{19} [sehend]{20} [zruggchoo]{19}.",
 "JHN.9.8": "[D Nachbere]{1,3} [dänn]{2} und{4} [die]{5}, [wo]{6} [en]{7} [früener]{8,9} [als]{10} [Bettler]{11,12} [gseh händ]{6}, [händ gseit]{13}: «[Isch]{16} [das]{15} [nöd]{14} [dä]{17}, wo [dört ghocket isch]{18} und{19} [bettlet hät]{20}?»",
 "JHN.9.9": "[Anderi]{1} [händ gseit]{2}: «[Er]{4} [isch es]{5}.» [Anderi]{6} [händ gseit]{7}: «[Nei]{8}, [aber]{9} [er isch]{12} [ihm]{11} [ähnlich]{10}.» [Er sälber]{13} [hät gseit]{14}: «[Ich]{16} [bi s]{17}.» ~3(ὅτι leitet di diräkt Red ii) ~15(ὅτι leitet di diräkt Red ii)",
 "JHN.9.10": "[Dänn]{2} [händ si]{1} [zu ihm]{3} [gseit]{1}: «[Wie]{4} [sind]{5} [dir]{6} [d Auge]{7,8} [ufgmacht worde]{5}?»",
 "JHN.9.11": "[Er]{2} [hät gantwortet]{1}: «[De Mänsch]{3,4}, [wo]{5} [Jesus]{7} [heisst]{6}, [hät]{9} [en Brei]{8} [gmacht]{9} und{10} [hät en]{11} [uf]{11} [mini]{12} [Auge]{13,14} [gstriche]{11} und{15} [hät]{16} [zu mir]{17} [gseit]{16}: ‹[Gang]{19} [zum]{20,21} [Siloam]{22} und{23} [wäsch di]{24}!› [Dänn]{26} [bin ich hiigange]{25}, und{27} [won ich mich gwäsche han]{28}, [bin ich sehend worde]{29}.» ~18(ὅτι leitet di diräkt Red ii)",
 "JHN.9.12": "Und{1} [si händ]{2} [zu ihm]{3} [gseit]{2}: «[Wo]{4} [isch]{5} [dä]{6}?» [Er seit]{7}: «[Ich weiss]{9} [es nöd]{8}.»",
 "JHN.9.13": "[Si bringed]{1} [en]{2}, [dä]{6} [wo früener]{7} [blind gsii isch]{8}, [zu]{3} [de Pharisäer]{4,5}.",
 "JHN.9.14": "[Es isch]{1} [aber]{2} [Sabbat]{3} [gsii]{1}, [wo]{4-6} [de Jesus]{10,11} [de]{7} [Brei]{8} [gmacht]{9} und{12} [ihm]{14} [d Auge]{15,16} [ufgmacht hät]{13}.",
 "JHN.9.15": "[Dänn]{2} [händ]{3} [en]{4} [wider]{1} [au]{5} [d Pharisäer]{6,7} [gfröget]{3}, [wie]{8} [er sehend worde sig]{9}. [Er]{10} [aber]{11} [hät]{12} [zu ine]{13} [gseit]{12}: «[En Brei]{14} [hät er]{15} [mir]{16} [uf]{17} [d Auge]{18,19} [gleit]{15}, und{20} [ich han mich gwäsche]{21}, und{22} [ich gsehne]{23}.»",
 "JHN.9.16": "[Dänn]{2} [händ]{1} [es paar]{6} [vo]{3} [de Pharisäer]{4,5} [gseit]{1}: «[Dä]{9} [Mänsch]{12,13} [isch]{8} [nöd]{7} [vo]{10} [Gott]{11}, [wil]{14} [er]{18} [de Sabbat]{15,16} [nöd]{17} [haltet]{18}.» [Anderi]{19} [händ gseit]{20}: «[Wie]{21} [cha]{22} [en sündige]{24} [Mänsch]{23} [settigi]{25} [Zeiche]{26} [tue]{27}?» Und{28} [es hät]{30} [e Spaltig]{29} [under]{31} [ine]{32} [gää]{30}.",
 "JHN.9.17": "[Dänn]{2} [säged si]{1} [wider]{5} [zum]{3} [Blinde]{4}: «[Was]{6} [seisch]{8} [du]{7} [über]{9} [en]{10}, [wil]{11} [er]{12} [dir]{13} [d Auge]{14,15} [ufgmacht hät]{12}?» [Er]{16} [aber]{17} [hät gseit]{18}: «[Er isch]{21} [en Prophet]{20}.» ~19(ὅτι leitet di diräkt Red ii)",
 "JHN.9.18": "[D Jude]{4,5} [händ]{2} [dänn]{3} [nöd]{1} [glaubt]{2} [über]{6} [en]{7}, [dass]{8} [er]{9} [blind]{10} [gsii]{9} und{11} [sehend worde sig]{12}, [bis]{13,14} [si]{15} [d Eltere]{16,17} [vo däm]{18,19} [grüeft händ]{15}, [wo sehend worde isch]{20},",
 "JHN.9.19": "und{1} [händ]{2} [si]{3} [gfröget]{2}: «[Isch]{6} [das]{5} [eue]{9} [Sohn]{7,8}, [vo däm]{10} [ir]{11} [säged]{12}, [er sig]{15} [blind]{14} [gebore]{15}? [Wie]{16} [gseht er]{18} [dänn]{17} [jetzt]{19}?» ~4(λέγοντες «sägend» vor de diräkte Red nöd eigens widergää) ~13(ὅτι leitet di indiräkt Red ii)",
 "JHN.9.20": "[Dänn]{2} [händ]{1} [sini]{5} [Eltere]{3,4} [gantwortet]{1} und{6} [gseit]{7}: «[Mir wüssed]{8}, [dass]{9} [das]{10} [üse]{14} [Sohn]{12,13} [isch]{11} und{15} [dass]{16} [er]{18} [blind]{17} [gebore worde isch]{18};",
 "JHN.9.21": "[wie]{1} [er]{4} [aber]{2} [jetzt]{3} [gseht]{4}, [wüssed mir]{6} [nöd]{5}, [oder]{7} [wer]{8} [ihm]{10} [d Auge]{11,12} [ufgmacht hät]{9}, [wüssed]{15} [mir]{13} [nöd]{14}. [Fröged]{17} [en]{16}, [er isch alt gnueg]{18,19}, [er sälber]{20} [wird]{23} [für]{21} [sich]{22} [rede]{23}.»",
 "JHN.9.22": "[Das]{1} [händ]{2} [sini]{5} [Eltere]{3,4} [gseit]{2}, [wil]{6} [si]{7} [vor de Jude]{8,9} [Angscht gha händ]{7}; [dänn]{11} [d Jude]{13,14} [händ]{12} [scho]{10} [beschlosse]{12}, [dass]{15}, [wänn]{16} [öpper]{17} [en]{18} [als Christus]{20} [bekänni]{19}, er [us de Synagoge usgschlosse]{21} [wärdi]{22}.",
 "JHN.9.23": "[Drum]{1,2} [händ]{6} [sini]{5} [Eltere]{3,4} [gseit]{6}: «[Er isch alt gnueg]{8,9}, [fröged]{11} [en]{10}!» ~7(ὅτι leitet di diräkt Red ii)",
 "JHN.9.24": "[Dänn]{2} [händ si]{1} [de Mänsch]{3,4}, [wo]{7} [blind]{9} [gsii isch]{8}, [zum zweite Mal]{5,6} [grüeft]{1} und{10} [zu ihm]{12} [gseit]{11}: «[Gib]{13} [Gott]{15,16} [d Ehr]{14}! [Mir]{17} [wüssed]{18}, [dass]{19} [dä]{20} [Mänsch]{21,22} [en Sünder]{23} [isch]{24}.»",
 "JHN.9.25": "[Dänn]{2} [hät]{1} [dä]{3} [gantwortet]{1}: «[Öb]{4} [er]{6} [en Sünder]{5} [isch]{6}, [weiss ich]{8} [nöd]{7}; [eis]{9} [weiss ich]{10}: [dass]{11} [ich]{13} [blind]{12} [gsii bi]{13} und [jetzt]{14} [gsehne]{15}.»",
 "JHN.9.26": "[Dänn]{2} [händ si]{1} [zu ihm]{3} [gseit]{1}: «[Was]{4} [hät er]{5} [mit dir]{6} [gmacht]{5}? [Wie]{7} [hät er]{8} [dir]{9} [d Auge]{10,11} [ufgmacht]{8}?»",
 "JHN.9.27": "[Er hät]{1} [ine]{2} [gantwortet]{1}: «[Ich han]{3} [s eu]{4} [scho]{5} [gseit]{3}, und{6} [ir händ]{8} [nöd]{7} [zueglost]{8}. [Werum]{9} [wänd ir]{11} s [nomal]{10} [ghöre]{12}? [Wänd]{16} [öppe]{13} [au]{14} [ir]{15} [sini]{17} [Jünger]{18} [wärde]{19}?»",
 "JHN.9.28": "[Si händ]{1} [en]{2} [beschimpft]{1} und{3} [gseit]{4}: «[Du]{5} [bisch]{7} [en Jünger]{6} [vo däm]{8}, [mir]{9} [aber]{10} [sind]{13} [Jünger]{14} [vom Mose]{11,12}.",
 "JHN.9.29": "[Mir]{1} [wüssed]{2}, [dass]{3} [Gott]{6,7} [mit em Mose]{4} [gredt hät]{5}; [vo däm]{8} [aber]{9} [wüssed mir]{11} [nöd]{10}, [vo wo]{12} [er isch]{13}.»",
 "JHN.9.30": "[De Mänsch]{2,3} [hät gantwortet]{1} und{4} [zu ine]{6} [gseit]{5}: «[Da]{7,8} [isch]{12} [doch]{9} [s]{10} [Erstuunliche]{11}, [dass]{13} [ir]{14} [nöd]{15} [wüssed]{16}, [vo wo]{17} [er isch]{18}, und{19} [er hät]{20} [mir]{21} [d Auge]{22,23} [ufgmacht]{20}!",
 "JHN.9.31": "[Mir wüssed]{1}, [dass]{2} [Gott]{4,5} [nöd]{6} [uf Sünder]{3} [lost]{7}; [sondern]{8} [wänn]{9} [öpper]{10} [gottesfürchtig]{11} [isch]{12} und{13} [sin]{16} [Wille]{14,15} [tuet]{17}, [uf dä]{18} [lost er]{19}.",
 "JHN.9.32": "[Sit Mänschegedänke]{1-3} [hät mer]{5} [nöd]{4} [ghört]{5}, [dass]{6} [öpper]{8} [d Auge]{9} [vo eme vo Geburt aa]{11} [Blinde]{10} [ufgmacht hät]{7}.",
 "JHN.9.33": "[Wänn]{1} [dä]{4} [nöd]{2} [vo]{5} [Gott]{6} [wär]{3}, [chönt er]{8} [nüüt]{7,10} [mache]{9}.»",
 "JHN.9.34": "[Si händ gantwortet]{1} und{2} [zu ihm]{4} [gseit]{3}: «[Du]{7} [bisch]{8} [ganz]{9} [i]{5} [Sünde]{6} [gebore]{8}, und{10} [du]{11} [lehrsch]{12} [üs]{13}?» Und{14} [si händ]{15} [en]{16} [use]{17}[gworfe]{15}.",
 "JHN.9.35": "[De Jesus]{2} [hät ghört]{1}, [dass]{3} [si]{4} [en]{5} [use]{6}[gworfe händ]{4}, und{7} [won er]{8} [en]{9} [gfunde hät]{8}, [hät er gseit]{10}: «[Glaubsch]{12} [du]{11} [a]{13} [de Mänschesohn]{14-17}?»",
 "JHN.9.36": "[Dä]{2} [hät gantwortet]{1} und{3} [gseit]{4}: «[Und]{5} [wer]{6} [isch]{7} es, [Herr]{8}, [demit]{9} [ich]{10} [a]{11} [en]{12} [chan glaube]{10}?»",
 "JHN.9.37": "[De Jesus]{3,4} [hät]{1} [zu ihm]{2} [gseit]{1}: «[Du häsch]{6} [en]{7} [ja]{5} [gseh]{6}, und{8} [dä]{9}, [wo]{10} [mit]{11} [dir]{12} [redt]{10}, [dä]{13} [isch es]{14}.»",
 "JHN.9.38": "[Er]{1} [aber]{2} [hät gseit]{3}: «[Ich glaube]{4}, [Herr]{5}!» Und{6} [er isch]{7} [vor ihm]{8} [uf d Chnü gfalle]{7}.",
 "JHN.9.39": "Und{1} [de Jesus]{3,4} [hät gseit]{2}: «[Zum]{5} [Gricht]{6} [bin]{12} [ich]{7} [i]{8} [die]{11} [Wält]{9,10} [choo]{12}, [demit]{13} [die]{14}, [wo nöd]{15} [gsehnd]{16}, [gsehnd]{17} und{18} [die]{19}, [wo gsehnd]{20}, [blind]{21} [wärded]{22}.»",
 "JHN.9.40": "[Das]{5} [händ]{1} [die]{6} [vo]{2} [de Pharisäer]{3,4}, [wo]{9} [bi]{7} [ihm]{8} [gsii sind]{9}, [ghört]{1}, und{10} [händ]{11} [zu ihm]{12} [gseit]{11}: «[Sind]{17} [öppe]{13} [au]{14} [mir]{15} [blind]{16}?»",
 "JHN.9.41": "[De Jesus]{3,4} [hät]{1} [zu ine]{2} [gseit]{1}: «[Wänn]{5} [ir]{7} [blind]{6} [wäred]{7}, [hetted ir]{9,10} [kei]{8} [Sünd]{11}; [jetzt]{12} [aber]{13} [säged ir]{14}: ‹[Mir gsehnd]{16}.› [Eui]{19} [Sünd]{17,18} [bliibt]{20}.» ~15(ὅτι leitet di diräkt Red ii)",
}

# Was die CNTR-Transkriptionen zu [[JHN.7.53]]–[[JHN.8.11]] zeigen (per Skript aus data/witness-texts ermittelt,
# Stand 2026-10-14; «-» = für den Vers kein Text, der Text geht von 7,52 zu 8,12 über):
#   kein Text («-»): 01, 03, 029, 032, 𝔓66, 𝔓75   – Text vorhanden: 05
#   nicht erfasst (Lücke): 02 (6,51–8,51), 04 (7,4–8,33); 𝔓45: Eintrag «-~», kein Text
PA_DE = ("In den im Projekt erfassten CNTR-Transkriptionen (Sekundärtranskription) steht für [[JHN.7.53]]–[[JHN.8.11]] bei 01 "
         "(Codex Sinaiticus), 03 (Codex Vaticanus), 029, 032, 𝔓66 und 𝔓75 kein Text; dort folgt auf [[JHN.7.52]] unmittelbar "
         "[[JHN.8.12]]. 05 (Codex Bezae) enthält den Abschnitt, mit eigenem Wortlaut. 02 und 04 sind an dieser Stelle nicht "
         "erhalten (Lücken in 6,51–8,51 bzw. 7,4–8,33), sie geben also keine Auskunft; auch die Transkription von 𝔓45 enthält "
         "hier keinen Text.")
PA_GSW = ("I de erfasste CNTR-Transkriptione staat für [[JHN.7.53]]–[[JHN.8.11]] bi 01 (Codex Sinaiticus), 03 (Codex Vaticanus), "
          "029, 032, 𝔓66 und 𝔓75 kei Text; dört chunnt nach [[JHN.7.52]] grad [[JHN.8.12]]. 05 (Codex Bezae) hät de Abschnitt, "
          "mit eigetem Wortlut. 02 und 04 sind a dere Stell nöd erhalte und säged drum nüüt; au d Transkription vo 𝔓45 hät da "
          "kei Text.")

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("JHN.8.1", "Jesus aber ging", "literal", "Ἰησοῦς δὲ ἐπορεύθη", None, None,
  "[[JHN.8.1]]–[[JHN.8.11]] setzt den Abschnitt von der Frau fort, die beim Ehebruch ergriffen wurde; er beginnt mit [[JHN.7.53]]. "
  "Der SBLGNT setzt [[JHN.7.53]]–[[JHN.8.11]] in Doppelklammern ⟦ ⟧; die Übersetzung übernimmt sie (die öffnende Klammer steht bei 7,53, "
  "die schliessende am Ende von 8,11). In der Textforschung wird der Abschnitt weithin als spätere Einfügung in das Johannesevangelium "
  "beurteilt, auch wegen Wortschatz und Stil; das ist ein verbreitetes Urteil, keine gesicherte Tatsache, und über Herkunft und Alter "
  "der Erzählung selbst wird verschieden geurteilt. " + PA_DE + " Nach Angaben der Forschung steht der Abschnitt in einigen späteren "
  "Handschriften an anderer Stelle (etwa nach [[JHN.7.36]], nach [[JHN.21.25]] oder nach [[LUK.21.38]]); diese Handschriften sind im "
  "Projekt nicht erfasst. Viele Kirchen lesen den Abschnitt als Teil der Heiligen Schrift; die Frage seiner Herkunft ist davon zu "
  "unterscheiden."),
 ("JHN.8.6", "ohne auf sie einzugehen", "interpretive", "μὴ προσποιούμενος", "nicht so tuend", ["als hörte er sie nicht", "ohne sich etwas anmerken zu lassen"],
  "Die Wendung steht im Token-Text des SBLGNT. προσποιέομαι heisst «sich stellen, so tun als ob»; verneint etwa «ohne darauf einzugehen». Was Jesus auf die Erde schrieb, sagt der Text nicht."),
 ("JHN.8.5", "zu steinigen", "literal", "λιθοβολεῖσθαι", None, None,
  "Das Gesetz sieht für Ehebruch den Tod beider Beteiligten vor ([[LEV.20.10]]; [[DEU.22.22]]); die Steinigung ist für bestimmte Fälle ausdrücklich genannt ([[DEU.22.23]]–[[DEU.22.24]]). Dass hier nur die Frau gebracht wird, sagt der Text, ohne es zu erklären."),
 ("JHN.8.11", "Herr", "interpretive", "κύριε", None, ["Meister"],
  "κύριε ist auch die höfliche Anrede an einen Mann («Herr»). Ob die Frau mehr meint, lässt der Text offen. Ebenso [[JHN.9.36]] und [[JHN.9.38]]."),
 ("JHN.8.11", "verurteile", "interpretive", "κρίνω", "richte", ["urteile … ab"],
  "Der Token-Text hat κρίνω «richten»; im Zusammenhang mit κατέκρινεν «hat verurteilt» ([[JHN.8.10]]) ist das Verurteilen gemeint."),
 ("JHN.8.11", "nicht mehr!»⟧", "literal", "μηκέτι ἁμάρτανε", None, None,
  "Hier schliesst die Doppelklammer ⟦ ⟧ des Abschnitts [[JHN.7.53]]–[[JHN.8.11]] (siehe [[JHN.8.1]]). Mit [[JHN.8.12]] geht die Rede Jesu weiter, die in [[JHN.7.52]] unterbrochen ist."),
 ("JHN.8.12", "Ich bin das Licht der Welt", "literal", "Ἐγώ εἰμι τὸ φῶς τοῦ κόσμου", None, None,
  "Grundentscheid für Johannes: ἐγώ εἰμι mit einem Bildwort wird durchgehend «Ich bin …» wiedergegeben (vgl. [[JHN.6.35]], [[JHN.10.11]]); κόσμος durchgehend «Welt». Das Licht nimmt [[JHN.1.4]]–[[JHN.1.9]] auf und kehrt in [[JHN.9.5]] wieder."),
 ("JHN.8.12", "gewiss nicht", "literal", "οὐ μὴ", None, ["keinesfalls"], "Die doppelte Verneinung οὐ μή mit Konjunktiv ist eine starke Verneinung. Ebenso [[JHN.8.51]]–[[JHN.8.52]]."),
 ("JHN.8.13", "Zeugnis ab", "literal", "μαρτυρεῖς", None, ["zeugst"], "μαρτυρέω/μαρτυρία «Zeugnis ablegen/Zeugnis» ist ein Leitwort bei Johannes (vgl. [[JHN.5.31]]–[[JHN.5.32]]) und durchgehend so wiedergegeben."),
 ("JHN.8.15", "nach dem Fleisch", "literal", "κατὰ τὴν σάρκα", None, ["nach menschlichem Massstab", "nach dem Augenschein"], "σάρξ steht hier für das bloss menschliche Urteil (vgl. [[JHN.7.24]])."),
 ("JHN.8.17", "das Zeugnis zweier Menschen", "literal", "δύο ἀνθρώπων ἡ μαρτυρία", None, None, "Vgl. [[DEU.17.6]] und [[DEU.19.15]]: Eine Sache gilt erst auf die Aussage von zwei oder drei Zeugen."),
 ("JHN.8.20", "Schatzkammer", "interpretive", "γαζοφυλακίῳ", None, ["Opferkasten", "Schatzhaus"],
  "γαζοφυλάκιον bezeichnet die Tempelkasse: die Räume, in denen Gaben verwahrt wurden, oder die Opferstöcke (vgl. [[MRK.12.41]]). ἐν kann hier auch «bei» heissen."),
 ("JHN.8.20", "seine Stunde", "literal", "ἡ ὥρα αὐτοῦ", None, None, "Die «Stunde» Jesu ist bei Johannes die Stunde seines Todes und seiner Verherrlichung (vgl. [[JHN.7.30]], [[JHN.12.23]], [[JHN.13.1]])."),
 ("JHN.8.22", "die Juden", "interpretive", "οἱ Ἰουδαῖοι", None, ["die jüdischen Führer", "die Judäer", "die führenden Männer"],
  "Grundentscheid für Johannes: οἱ Ἰουδαῖοι wird wörtlich «die Juden» wiedergegeben. Das ist eine Deutungsentscheidung. Johannes gebraucht das Wort "
  "in mehreren Bedeutungen: für das jüdische Volk und seine Bräuche (vgl. [[JHN.2.6]], [[JHN.4.22]]), für Menschen aus Judäa und Jerusalem, oft aber für "
  "die Gegner Jesu, besonders die führenden Kreise in Jerusalem (vgl. [[JHN.9.22]], wo jüdische Eltern sich vor «den Juden» fürchten). Jesus, seine "
  "Jünger und die meisten Personen der Erzählung sind selbst Juden. Viele Übersetzungen schreiben deshalb je nach Stelle «die jüdischen Führer» oder "
  "«die Judäer»; dagegen spricht, dass damit eine Deutung in den Text gelegt wird und die Unschärfe des Originals verloren geht. Die Wiedergabe «die "
  "Juden» behält den Wortlaut bei; sie ist nicht als Aussage über das jüdische Volk insgesamt zu lesen. Redaktionelle Entscheidung; ebenso [[JHN.8.31]], "
  "[[JHN.8.48]], [[JHN.8.52]], [[JHN.8.57]], [[JHN.9.18]] und [[JHN.9.22]]."),
 ("JHN.8.24", "dass ich bin", "interpretive", "ἐγώ εἰμι", None, ["dass ich es bin", "dass ich der bin, der ich bin"],
  "ἐγώ εἰμι steht hier ohne Ergänzung. Grundentscheid für Johannes: «Ich bin» wird auch in dieser absoluten Form sichtbar gehalten, wie in [[JHN.8.28]] "
  "und [[JHN.8.58]]. Viele Ausleger hören darin die Selbstvorstellung Gottes in der griechischen Bibel (vgl. [[ISA.43.10]], wo ebenfalls «damit ihr glaubt, "
  "dass ich bin» steht, und [[DEU.32.39]]); andere verstehen es als «dass ich es bin», das heisst der, als den Jesus sich zuvor bezeichnet hat. Die "
  "Rückfrage «Wer bist du?» ([[JHN.8.25]]) zeigt, dass der Satz offen klingt."),
 ("JHN.8.25", "Wozu rede ich überhaupt noch zu euch?", "interpretive", "Τὴν ἀρχὴν ὅ τι καὶ λαλῶ ὑμῖν", "Den Anfang, was ich auch zu euch rede",
  ["Was ich euch von Anfang an gesagt habe", "Vor allem das, was ich euch sage", "Dass ich überhaupt noch zu euch rede!"],
  "Einer der schwierigsten Sätze des Evangeliums. τὴν ἀρχήν kann adverbial «überhaupt» heissen oder «am Anfang»; ὅ τι (bzw. ὅτι) kann «was», «warum» oder «dass» sein. "
  "Der SBLGNT setzt ein Fragezeichen; die Übersetzung folgt dem. Die alten Handschriften sind ohne Worttrennung geschrieben; ob ὅ τι oder ὅτι gemeint ist, "
  "entscheiden die Ausgaben (WH liest ὅτι)."),
 ("JHN.8.28", "erhöht habt", "literal", "ὑψώσητε", None, ["erhoben habt"],
  "Grundentscheid für Johannes: ὑψόω «erhöhen». Das Wort meint bei Johannes zugleich das Aufrichten am Kreuz und die Erhöhung zu Gott (vgl. [[JHN.3.14]], [[JHN.12.32]]–[[JHN.12.33]]). Die Angeredeten sind hier selbst die, die ihn erhöhen."),
 ("JHN.8.28", "den Menschensohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "den Sohn des Menschen", None,
  "«Sohn eines Menschen» heisst hebräisch und aramäisch einfach «Mensch»; bei Jesus eine Selbstbezeichnung, oft mit Anklang an [[DAN.7.13]]. Ebenso [[JHN.9.35]]."),
 ("JHN.8.28", "dass ich bin", "interpretive", "ἐγώ εἰμι", None, ["dass ich es bin"], "Wie in [[JHN.8.24]]."),
 ("JHN.8.28", "so rede", "adapted", "ταῦτα λαλῶ", "dies rede", None, "ταῦτα «dies» ist mit «so» wiedergegeben, weil es auf «wie mich der Vater gelehrt hat» zurückweist."),
 ("JHN.8.31", "den Juden, die ihm geglaubt hatten", "interpretive", "τοὺς πεπιστευκότας αὐτῷ Ἰουδαίους", None, ["den Juden, die ihm Glauben geschenkt hatten"],
  "Zu «die Juden» siehe [[JHN.8.22]]. Auffällig ist, dass dieselben Angeredeten in [[JHN.8.37]] und [[JHN.8.40]] Jesus töten wollen. Manche sehen darin einen Glauben, "
  "der nicht bleibt (vgl. [[JHN.8.31]] «wenn ihr bleibt»), andere einen Wechsel der Angeredeten im Lauf des Gesprächs oder eine Naht in der Überlieferung."),
 ("JHN.8.31", "bleibt", "literal", "μείνητε", None, ["festhaltet"], "Grundentscheid für Johannes: μένω durchgehend «bleiben», auch [[JHN.8.35]] und [[JHN.9.41]]."),
 ("JHN.8.33", "Nachkommen", "adapted", "Σπέρμα", "Same", ["Nachkommenschaft"], "σπέρμα «Same» steht bildlich für die Nachkommenschaft. Ebenso [[JHN.8.37]]."),
 ("JHN.8.34", "Amen, amen, ich sage euch", "literal", "Ἀμὴν ἀμὴν λέγω ὑμῖν", None, ["Wahrlich, wahrlich, ich sage euch"],
  "Grundentscheid für Johannes: Das doppelte ἀμήν (hebräisch ʾāmēn «gewiss, so ist es») vor einem Wort Jesu steht nur bei Johannes und wird als «Amen, amen» belassen. Ebenso [[JHN.8.51]] und [[JHN.8.58]]."),
 ("JHN.8.34", "ein Sklave", "literal", "δοῦλός", None, ["ein Knecht"], "δοῦλος ist hier «Sklave», weil das Gespräch Sklaverei und Freiheit gegenüberstellt ([[JHN.8.33]]–[[JHN.8.36]])."),
 ("JHN.8.35", "in Ewigkeit", "literal", "εἰς τὸν αἰῶνα", None, ["für immer"], "Ebenso [[JHN.8.51]] und [[JHN.8.52]]."),
 ("JHN.8.38", "ihr tut also", "interpretive", "ὑμεῖς οὖν ποιεῖτε", None, ["so tut auch ihr"],
  "ποιεῖτε kann Indikativ («ihr tut») oder Imperativ («tut!») sein; «der Vater» steht ohne «euer». Als Imperativ hiesse der Satz: «Tut also auch ihr, was ihr vom Vater gehört habt», gemeint wäre dann Gott. Die Übersetzung liest den Indikativ, weil im Folgenden zwei Väter einander gegenübergestellt werden ([[JHN.8.41]], [[JHN.8.44]]). Redaktionelle Entscheidung. Zu Lesarten mit «euer Vater» siehe die Alternativen."),
 ("JHN.8.40", "der euch die Wahrheit gesagt hat", "adapted", "ὃς τὴν ἀλήθειαν ὑμῖν λελάληκα", "der ich euch die Wahrheit gesagt habe", None,
  "Im Griechischen spricht Jesus im Relativsatz in der ersten Person; im Deutschen ist die dritte Person gewählt."),
 ("JHN.8.41", "Unzucht", "interpretive", "πορνείας", "Hurerei", ["Ehebruch"],
  "Der Satz kann allgemein gemeint sein (Israel als treues Volk im Gegensatz zum Götzendienst, der in der Schrift Hurerei heisst, vgl. [[HOS.2.4]]) oder als Anspielung auf Gerüchte über Jesu Herkunft. Der Text entscheidet das nicht."),
 ("JHN.8.44", "vom Vater, dem Teufel", "interpretive", "ἐκ τοῦ πατρὸς τοῦ διαβόλου", None, ["vom Vater des Teufels"],
  "Grammatisch ist auch «vom Vater des Teufels» möglich; diese Lesart vertraten in der alten Kirche einzelne Gruppen. Die Übersetzung folgt der verbreiteten Auffassung. "
  "Der Vers richtet sich in der Erzählung an bestimmte Gesprächspartner Jesu in einem innerjüdischen Streit. In der Geschichte des christlichen Antijudaismus wurde er gegen "
  "Juden insgesamt gewendet; das gibt der Text nicht her."),
 ("JHN.8.44", "der Vater davon", "interpretive", "ὁ πατὴρ αὐτοῦ", "sein Vater", ["der Vater der Lüge", "der Vater des Lügners"],
  "αὐτοῦ kann sich auf «die Lüge» oder auf «den Lügner» beziehen; beides läuft auf den Teufel als Ursprung der Lüge hinaus."),
 ("JHN.8.48", "Samaritaner", "literal", "Σαμαρίτης", None, None, "Ein Schimpfwort im Mund der Gegner: Samaritaner galten den Jerusalemern als abtrünnig (vgl. [[JHN.4.9]])."),
 ("JHN.8.50", "Ehre", "adapted", "δόξαν", "Herrlichkeit", ["Herrlichkeit", "Ansehen"],
  "Ausnahme vom Grundentscheid δόξα/δοξάζω «Herrlichkeit/verherrlichen»: Wo δόξα das Ansehen bei Menschen meint, steht «Ehre» "
  "(einheitlich in [[JHN.5.41]], [[JHN.5.44]], [[JHN.7.18]], [[JHN.8.50]], [[JHN.8.54]], [[JHN.9.24]] und [[JHN.12.43]]). Hier steht das Wort "
  "neben «ehren» und «entehren» ([[JHN.8.49]]): Jesus sucht nicht sein eigenes Ansehen. Dass im selben Wort die «Herrlichkeit» mitklingt, "
  "geht in der deutschen Wiedergabe verloren. Redaktionelle Entscheidung."),
 ("JHN.8.54", "meine Ehre", "adapted", "ἡ δόξα μου", "meine Herrlichkeit", ["meine Herrlichkeit"],
  "Wie [[JHN.8.50]]: δόξα meint hier das Ansehen, das man sich selbst verschafft, deshalb «Ehre». Das Verb δοξάζω bleibt nach dem "
  "Grundentscheid «verherrlichen»; im Griechischen gehören Verb und Nomen zum selben Stamm (wörtlich: «Wenn ich mich selbst "
  "verherrliche, ist meine Herrlichkeit nichts»)."),
 ("JHN.8.51", "bewahrt", "literal", "τηρήσῃ", None, ["hält", "befolgt"], "Ebenso [[JHN.8.52]] und [[JHN.8.55]]."),
 ("JHN.8.52", "schmecken", "literal", "γεύσηται", None, ["erleiden", "erfahren"], "«Den Tod schmecken» ist eine Redewendung für «sterben»; die Gegner nehmen Jesu Wort «den Tod sehen» ([[JHN.8.51]]) so auf."),
 ("JHN.8.56", "dass er meinen Tag sehen sollte", "interpretive", "ἵνα ἴδῃ τὴν ἡμέραν τὴν ἐμήν", None, ["dass er meinen Tag sehen würde", "in der Erwartung, meinen Tag zu sehen"],
  "Woran Johannes denkt, ist offen: an die Verheissung an Abraham ([[GEN.12.3]]), an Abrahams Lachen ([[GEN.17.17]]) oder an spätere jüdische Überlieferungen, nach denen Abraham die Zukunft gezeigt wurde."),
 ("JHN.8.57", "noch nicht fünfzig Jahre", "literal", "Πεντήκοντα ἔτη οὔπω", None, None, "Die Zahl ist eine runde Grenze, keine Altersangabe zu Jesus."),
 ("JHN.8.58", "bin ich", "interpretive", "ἐγὼ εἰμί", "ich bin", ["war ich schon", "bin ich da"],
  "Der Satz stellt γενέσθαι («werden, entstehen») bei Abraham dem Präsens εἰμί («ich bin») bei Jesus gegenüber; deshalb ist das Präsens beibehalten, auch wenn es im Deutschen "
  "ungewohnt klingt. Viele Ausleger hören darin die Selbstvorstellung Gottes (vgl. [[EXO.3.14]] in der griechischen Bibel, [[ISA.43.10]]); andere verstehen es als Aussage über "
  "Jesu Dasein vor Abraham, ohne direkten Bezug auf diese Stellen. Dass die Hörer danach Steine aufheben ([[JHN.8.59]]), deuten viele als Reaktion auf eine empfundene "
  "Gotteslästerung. Wie [[JHN.8.24]] und [[JHN.8.28]]."),
 ("JHN.8.59", "verbarg sich", "interpretive", "ἐκρύβη", "wurde verborgen", None, "Passivform; sie kann reflexiv («verbarg sich») oder als Handeln Gottes («wurde verborgen») verstanden werden."),
 ("JHN.9.2", "Rabbi", "literal", "Ῥαββί", None, ["Meister", "Lehrer"], "Aramäisch-hebräische Anrede für einen Lehrer (vgl. [[JHN.1.38]])."),
 ("JHN.9.3", "es geschah, damit", "adapted", "ἀλλʼ ἵνα", "sondern damit", None,
  "Der griechische Satz ist verkürzt; «es geschah» ist ergänzt. Manche ziehen ἀλλʼ ἵνα … zum folgenden Vers: «Damit die Werke Gottes an ihm offenbar werden, müssen wir wirken …». Die Satzgrenze ist eine redaktionelle Entscheidung."),
 ("JHN.9.4", "Wir müssen", "literal", "ἡμᾶς δεῖ", None, ["Ich muss"], "Das «wir» bezieht die Jünger ein, während das «mich» Jesus allein meint. Zur Lesart «ich» siehe die Alternativen."),
 ("JHN.9.5", "bin ich das Licht der Welt", "literal", "φῶς εἰμι τοῦ κόσμου", None, None, "Nimmt [[JHN.8.12]] auf; hier ohne betontes ἐγώ."),
 ("JHN.9.6", "einen Brei", "literal", "πηλὸν", None, ["Lehm", "Teig"], "πηλός ist feuchte Erde, Lehm; hier mit Speichel angerührt."),
 ("JHN.9.6", "ihm", "interpretive", "αὐτοῦ", None, ["seinen Brei"], "αὐτοῦ kann zu «Augen» gehören («ihm auf die Augen») oder zu «Brei» («seinen Brei»)."),
 ("JHN.9.7", "Siloam", "literal", "Σιλωάμ", None, ["Schiloach", "Siloah"],
  "Griechische Form des hebräischen šilōaḥ (vgl. [[ISA.8.6]]). Johannes deutet den Namen als «Gesandter» und verbindet ihn so mit Jesus, dem Gesandten des Vaters ([[JHN.9.4]])."),
 ("JHN.9.9", "Ich bin es", "interpretive", "Ἐγώ εἰμι", "Ich bin", ["Ich bin's", "Ich bin der"],
  "Grundentscheid für Johannes: ἐγώ εἰμι als Antwort oder Selbstidentifikation heisst «Ich bin es» (ebenso [[JHN.4.26]], [[JHN.6.20]], "
  "[[JHN.18.5]]–[[JHN.18.8]]); die absolute Form ohne Bezug auf eine Frage ([[JHN.8.24]], [[JHN.8.28]], [[JHN.8.58]], [[JHN.13.19]]) heisst "
  "«ich bin». Hier antwortet der Geheilte auf den Streit, ob er der frühere Bettler sei; im Mund eines Menschen ist das eine gewöhnliche "
  "Identifikation. Manche Ausleger hören einen bewussten Anklang an die Ich-bin-Worte Jesu; das ist eine Deutung."),
 ("JHN.9.11", "wurde ich sehend", "interpretive", "ἀνέβλεψα", "blickte ich auf", ["sah ich wieder", "konnte ich sehen"],
  "ἀναβλέπω heisst «aufblicken» und «wieder sehen»; bei einem von Geburt an Blinden ist das Sehendwerden gemeint. Ebenso [[JHN.9.15]] und [[JHN.9.18]]."),
 ("JHN.9.16", "Zeichen", "literal", "σημεῖα", None, ["Wunder"], "Grundentscheid für Johannes: σημεῖον durchgehend «Zeichen», nicht «Wunder»; die Taten Jesu weisen über sich hinaus (vgl. [[JHN.2.11]], [[JHN.20.30]])."),
 ("JHN.9.18", "Die Juden", "interpretive", "οἱ Ἰουδαῖοι", None, ["Die jüdischen Führer"],
  "Zum Grundentscheid siehe [[JHN.8.22]]. Hier heissen dieselben Leute, die eben «die Pharisäer» genannt wurden ([[JHN.9.13]]–[[JHN.9.16]]), «die Juden»: gemeint sind die Befragenden."),
 ("JHN.9.22", "die Juden", "interpretive", "τοὺς Ἰουδαίους", None, ["die jüdischen Behörden", "die jüdischen Führer"],
  "Zum Grundentscheid siehe [[JHN.8.22]]. Die Eltern sind selbst Juden; «die Juden» meint hier die Instanz, die über den Ausschluss aus der Synagoge entscheidet. Das zeigt deutlich, dass das Wort bei Johannes oft eine Gruppe und nicht das ganze Volk bezeichnet. Ebenso das zweite Vorkommen im Vers."),
 ("JHN.9.22", "als Christus", "traditional", "χριστόν", None, ["als Messias", "als Gesalbten"], "χριστός übersetzt hebräisch māšîaḥ «Gesalbter» (vgl. [[JHN.1.41]])."),
 ("JHN.9.22", "aus der Synagoge ausgeschlossen", "literal", "ἀποσυνάγωγος", None, None,
  "ἀποσυνάγωγος steht nur bei Johannes (auch [[JHN.12.42]], [[JHN.16.2]]). Ob es zur Zeit Jesu einen solchen Beschluss gab oder ob sich darin Erfahrungen der johanneischen Gemeinde zur Zeit der Abfassung spiegeln, ist in der Forschung umstritten (vgl. BG-JHN-BOOK-0001)."),
 ("JHN.9.24", "Gib Gott die Ehre", "adapted", "Δὸς δόξαν τῷ θεῷ", "Gib Gott Herrlichkeit", ["Gib Gott die Herrlichkeit", "Sag vor Gott die Wahrheit"],
  "Feste Redewendung, mit der jemand aufgefordert wird, vor Gott die Wahrheit zu sagen (vgl. [[JOS.7.19]]). Deshalb hier «Ehre» statt «Herrlichkeit» (Ausnahme vom Grundentscheid, siehe [[JHN.8.50]])."),
 ("JHN.9.32", "Seit Menschengedenken", "adapted", "ἐκ τοῦ αἰῶνος", "Von Ewigkeit her", ["seit jeher"], None),
 ("JHN.9.34", "sie warfen ihn hinaus", "interpretive", "ἐξέβαλον αὐτὸν ἔξω", None, ["sie stiessen ihn aus"],
  "Ob nur ein Hinauswerfen aus dem Raum gemeint ist oder der in [[JHN.9.22]] genannte Ausschluss aus der Synagoge, sagt der Text nicht ausdrücklich."),
 ("JHN.9.35", "den Menschensohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "den Sohn des Menschen", None, "Wie [[JHN.8.28]]. Zur Lesart «Sohn Gottes» siehe die Alternativen."),
 ("JHN.9.38", "er fiel vor ihm nieder", "interpretive", "προσεκύνησεν αὐτῷ", None, ["er betete ihn an", "er huldigte ihm"],
  "προσκυνέω bezeichnet das Niederfallen vor einem Menschen wie die Anbetung Gottes (vgl. [[JHN.4.20]]–[[JHN.4.24]]). Welche Bedeutung hier gemeint ist, wird verschieden beurteilt. "
  "In den CNTR-Transkriptionen von 01, 032 und 𝔓75 steht für [[JHN.9.38]] kein Text, und [[JHN.9.39]] beginnt dort mit «Zum Gericht …» ohne «Und Jesus sagte»; 02, 03, 05 und 𝔓66 haben den Vers. Der SBLGNT-Apparat verzeichnet dazu keine Variante."),
 ("JHN.9.39", "Gericht", "literal", "κρίμα", None, ["Urteil", "Scheidung"], "κρίμα ist das Urteil, das scheidet; vgl. [[JHN.3.19]]."),
 ("JHN.9.41", "bleibt", "literal", "μένει", None, None, "μένω «bleiben», wie [[JHN.8.31]] und [[JHN.8.35]]."),
]

DEC_GSW = [
 ("JHN.8.1", "De Jesus aber isch", "literal", "Ἰησοῦς δὲ ἐπορεύθη", None, None,
  "[[JHN.8.1]]–[[JHN.8.11]] füert de Abschnitt vo de Frau wiiter, wo bim Ehebruch verwütscht worde isch; er faat mit [[JHN.7.53]] aa. De SBLGNT setzt "
  "[[JHN.7.53]]–[[JHN.8.11]] i Doppelklammere ⟦ ⟧; d Übersetzig übernimmt si. I de Textforschig wird de Abschnitt wiitume als spööteri Iifüegig is "
  "Johannesevangelium beurteilt; das isch es verbreitets Urteil, kei gsichereti Tatsach. " + PA_GSW + " Nach Aagabe vo de Forschig staat de Abschnitt i "
  "es paar spöötere Handschrifte a anderer Stell (öppe nach [[JHN.7.36]], [[JHN.21.25]] oder [[LUK.21.38]]); die Handschrifte sind im Projekt nöd erfasst. "
  "Vili Chile läsed de Abschnitt als Teil vo de Heilige Schrift; d Frag nach sinere Herkunft isch devo z underscheide."),
 ("JHN.8.6", "ohni uf si iizgaa", "interpretive", "μὴ προσποιούμενος", None, ["wie wänn er si nöd ghöri"], "Was de Jesus uf de Bode gschribe hät, seit de Text nöd."),
 ("JHN.8.11", "nüme!»⟧", "literal", "μηκέτι ἁμάρτανε", None, None, "Da schlüüsst d Doppelklammere vom Abschnitt [[JHN.7.53]]–[[JHN.8.11]] (lueg [[JHN.8.1]])."),
 ("JHN.8.12", "Ich bi s Liecht vo de Wält", "literal", "Ἐγώ εἰμι τὸ φῶς τοῦ κόσμου", None, None,
  "Grundentscheid für Johannes: ἐγώ εἰμι mit eme Bildwort heisst überall «Ich bi …»; κόσμος überall «Wält»."),
 ("JHN.8.22", "d Jude", "interpretive", "οἱ Ἰουδαῖοι", None, ["di jüdische Füerer", "d Judäer"],
  "Grundentscheid für Johannes: οἱ Ἰουδαῖοι heisst wörtlich «d Jude». Das isch en Düütigsentscheid. De Johannes bruucht s Wort für s jüdisch Volk, für Lüüt us "
  "Judäa und Jerusalem, mängisch aber für d Gägner vom Jesus, bsunders di füerende Chreis z Jerusalem (vgl. [[JHN.9.22]]). De Jesus, sini Jünger und di meischte "
  "Persone i de Gschicht sind sälber Jude. «D Jude» bhaltet de Wortlut; es isch nöd als Uussag über s jüdisch Volk im Ganze z läse. Redaktionelle Entscheid; "
  "gliich [[JHN.8.31]], [[JHN.8.48]], [[JHN.8.52]], [[JHN.8.57]], [[JHN.9.18]], [[JHN.9.22]]."),
 ("JHN.8.24", "dass ich bi", "interpretive", "ἐγώ εἰμι", None, ["dass ich s bi"],
  "ἐγώ εἰμι staat da ohni Ergänzig; «ich bi» bliibt sichtbar wie i [[JHN.8.28]] und [[JHN.8.58]]. Vili ghöred drin, wie Gott sich i de griechische Bible vorstellt "
  "(vgl. [[ISA.43.10]]); anderi verstönd «dass ich s bi»."),
 ("JHN.8.25", "Für was red ich überhaupt no mit eu?", "interpretive", "Τὴν ἀρχὴν ὅ τι καὶ λαλῶ ὑμῖν", None, ["Was ich eu vo Aafang aa gseit han"],
  "En sehr schwirige Satz; d Übersetzig folgt em Fragezeiche vom SBLGNT."),
 ("JHN.8.28", "erhöcht händ", "literal", "ὑψώσητε", None, None, "ὑψόω «erhöche»: bim Johannes s Ufrichte am Chrüüz und d Erhöchig zu Gott zgliich (vgl. [[JHN.3.14]], [[JHN.12.32]]–[[JHN.12.33]])."),
 ("JHN.8.28", "de Mänschesohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None, None),
 ("JHN.8.31", "bliibed", "literal", "μείνητε", None, None, "μένω überall «bliibe»."),
 ("JHN.8.34", "Amen, amen, ich säge eu", "literal", "Ἀμὴν ἀμὴν λέγω ὑμῖν", None, None, "S doppelt ἀμήν staat nu bim Johannes und bliibt «Amen, amen»."),
 ("JHN.8.34", "en Sklav", "literal", "δοῦλός", None, ["en Chnächt"], "S Gspröch stellt Sklaverei und Freiheit gägenand."),
 ("JHN.8.38", "ir tüend also", "interpretive", "ὑμεῖς οὖν ποιεῖτε", None, ["tüend au ir"], "ποιεῖτε cha «ir tüend» oder «tüend!» heisse; redaktionelle Entscheid."),
 ("JHN.8.44", "vom Vatter, em Tüüfel", "interpretive", "ἐκ τοῦ πατρὸς τοῦ διαβόλου", None, ["vom Vatter vom Tüüfel"],
  "De Vers richtet sich i de Gschicht a bestimmti Gsprächspartner vom Jesus i me innerjüdische Striit. I de Gschicht vom chrischtliche Antijudaismus isch er gäge alli Jude "
  "gwändet worde; das git de Text nöd här."),
 ("JHN.8.50", "Ehr", "adapted", "δόξαν", "Herrlichkeit", ["Herrlichkeit", "Aasee"],
  "Usnaam vom Grundentscheid δόξα/δοξάζω «Herrlichkeit/verherrliche»: Wo δόξα s Aasee bi de Mänsche meint, staat «Ehr» "
  "([[JHN.5.41]], [[JHN.5.44]], [[JHN.7.18]], [[JHN.8.50]], [[JHN.8.54]], [[JHN.9.24]], [[JHN.12.43]]). Da staat s Wort näbe «ehre» und «entehre» ([[JHN.8.49]])."),
 ("JHN.8.54", "mini Ehr", "adapted", "ἡ δόξα μου", "mini Herrlichkeit", ["mini Herrlichkeit"],
  "Wie [[JHN.8.50]]; s Verb δοξάζω bliibt «verherrliche». Im Griechische ghöred Verb und Nomen zum gliiche Stamm."),
 ("JHN.9.9", "Ich bi s", "interpretive", "Ἐγώ εἰμι", "Ich bi", ["Ich bi dä"],
  "Grundentscheid: ἐγώ εἰμι als Antwort oder Sälbervorstellig heisst «Ich bi s» (gliich [[JHN.4.26]], [[JHN.6.20]], [[JHN.18.5]]–[[JHN.18.8]]); "
  "di absolut Form ([[JHN.8.24]], [[JHN.8.28]], [[JHN.8.58]], [[JHN.13.19]]) «ich bi». Im Mund vom Gheilte isch das e gwöhnlichi Identifikation; "
  "es paar Uusleger ghöred en Aaklang a d Ich-bi-Wort vom Jesus, das isch e Düütig."),
 ("JHN.8.58", "bin ich", "interpretive", "ἐγὼ εἰμί", None, ["bin ich scho gsii"],
  "S Präsens «ich bi» staat gäge s «worde isch» bim Abraham; drum isch es bhalte. Vili ghöred drin, wie Gott sich vorstellt (vgl. [[EXO.3.14]], [[ISA.43.10]]); anderi läsed e Uussag über s Dasii vom Jesus vor em Abraham."),
 ("JHN.9.11", "bin ich sehend worde", "interpretive", "ἀνέβλεψα", "han ich ufgluegt", ["han ich wider gseh"], None),
 ("JHN.9.16", "Zeiche", "literal", "σημεῖα", None, ["Wunder"], "σημεῖον überall «Zeiche»."),
 ("JHN.9.22", "d Jude", "interpretive", "οἱ Ἰουδαῖοι", None, ["di jüdische Behörde"],
  "D Eltere sind sälber Jude; «d Jude» meint da di Instanz, wo über de Uusschluss us de Synagoge entscheidet. Lueg [[JHN.8.22]]."),
 ("JHN.9.24", "Gib Gott d Ehr", "adapted", "Δὸς δόξαν τῷ θεῷ", "Gib Gott Herrlichkeit", None, "Redewändig: vor Gott d Wahrheit säge (vgl. [[JOS.7.19]])."),
 ("JHN.9.38", "er isch vor ihm uf d Chnü gfalle", "interpretive", "προσεκύνησεν αὐτῷ", None, ["er hät en aabättet"],
  "I de CNTR-Transkriptione vo 01, 032 und 𝔓75 staat für [[JHN.9.38]] kei Text; 02, 03, 05 und 𝔓66 händ de Vers."),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-JHN-008-029-01:R2", "JHN.8.29", "er hat mich nicht allein gelassen", "der Vater hat mich nicht allein gelassen",
  "er hät mich nöd elei gloo", "de Vatter hät mich nöd elei gloo", "gering",
  "Mit «der Vater» als ausdrücklichem Subjekt.", "Mit «de Vatter» als usdrücklichem Subjekt.",
  {"R1": [("μόνον", "allein", None)], "R2": [("μόνον ὁ πατήρ", "allein, der Vater", "mit Zusatz")]},
  {"R1": [("μόνον", "elei", None)], "R2": [("μόνον ὁ πατήρ", "elei, de Vatter", "mit Zuesatz")]},
  ["Der Zusatz macht ausdrücklich, was sich aus «der mich gesandt hat» ergibt.",
   "Laut der automatischen Zuordnung lesen 01, 03, 05, 029, 032, 𝔓66 und 𝔓75 ohne Zusatz; 02 und 04 sind hier nicht erhalten. «Der Vater» haben unter den erfassten Texten die Ausgaben KJTR, RP und Stephanus."],
  ["De Zuesatz macht usdrücklich, was sich us «wo mich gschickt hät» ergit.",
   "Nach de automatische Zueornig läsed 01, 03, 05, 029, 032, 𝔓66 und 𝔓75 ohni Zuesatz; 02 und 04 sind da nöd erhalte."]),
 ("VAR-SBLGNTAPP-JHN-008-038-03:R2", "JHN.8.38", "gehört habt", "gesehen habt", "ghört händ", "gseh händ", "gering",
  "«Gesehen» statt «gehört»: Der zweite Satzteil wird dem ersten («was ich beim Vater gesehen habe») angeglichen.",
  "«Gseh» statt «ghört»: De zweit Satzteil wird em erschte aaglichen.",
  {"R1": [("ἃ ἠκούσατε", "was ihr gehört habt", None)], "R2": [("ὃ ἑωράκατε", "was ihr gesehen habt", None)]},
  {"R1": [("ἃ ἠκούσατε", "was ir ghört händ", None)], "R2": [("ὃ ἑωράκατε", "was ir gseh händ", None)]},
  ["Die Angleichung an «gesehen» im ersten Satzteil kann beim Abschreiben entstanden sein; umgekehrt kann «gehört» die Unterscheidung zwischen Jesus und den Angeredeten betonen.",
   "Laut der automatischen Zuordnung lesen 03, 04, 032 und 𝔓75 «gehört», 01, 05 und 𝔓66 «gesehen» (im erfassten Wortlaut mit ἅ statt ὅ); 02 und 029 sind hier nicht erhalten."],
  ["D Aagliichig a «gseh» cha bim Abschriibe entstande sii; umgekehrt cha «ghört» de Underschid zwüsche em Jesus und de Aagredte betone.",
   "Nach de automatische Zueornig läsed 03, 04, 032 und 𝔓75 «ghört», 01, 05 und 𝔓66 «gseh»."]),
 ("VAR-SBLGNTAPP-JHN-008-038-04:R2", "JHN.8.38", "vom Vater", "von eurem Vater", "vom Vatter", "vo eurem Vatter", "mittel",
  "Mit «euer» ist klar, dass ein anderer Vater gemeint ist als in der ersten Satzhälfte (vgl. [[JHN.8.41]], [[JHN.8.44]]).",
  "Mit «eue» isch klar, dass en andere Vatter gmeint isch als i de erschte Satzhälfti.",
  {"R1": [("τοῦ πατρὸς", "vom Vater", None)], "R2": [("τοῦ πατρὸς ὑμῶν", "von eurem Vater", None)], "R3": [("τῷ πατρὶ ὑμῶν", "bei eurem Vater", "RP")]},
  {"R1": [("τοῦ πατρὸς", "vom Vatter", None)], "R2": [("τοῦ πατρὸς ὑμῶν", "vo eurem Vatter", None)], "R3": [("τῷ πατρὶ ὑμῶν", "bi eurem Vatter", "RP")]},
  ["«Euer» kann als Verdeutlichung ergänzt worden sein; ohne «euer» bleibt offen, welcher Vater gemeint ist (siehe die Entscheidung zu «ihr tut also»).",
   "Laut der automatischen Zuordnung lesen 03 und 𝔓75 ohne «euer», 01 und 04 mit «euer» (R2), 05 «bei eurem Vater» (R3); 032 und 𝔓66 sind als «liest anders» geführt, haben im erfassten Wortlaut aber τοῦ πατρός ohne ὑμῶν. 𝔓75 hat nach der Transkription statt ποιεῖτε «ihr tut» λαλεῖτε «ihr redet» (Buchstaben teils als unsicher markiert)."],
  ["«Eue» cha als Verdüütlichig ergänzt worde sii.",
   "Nach de automatische Zueornig läsed 03 und 𝔓75 ohni «eue», 01 und 04 mit (R2), 05 «bi eurem Vatter» (R3); 032 und 𝔓66 händ im erfasste Wortlut τοῦ πατρός ohni ὑμῶν."]),
 ("VAR-SBLGNTAPP-JHN-008-039-01:R2", "JHN.8.39", "ihr Kinder Abrahams seid", "ihr Kinder Abrahams wärt", "ir Chind vom Abraham sind", "ir Chind vom Abraham wäred", "gering",
  "ἦτε («wärt») statt ἐστε («seid»): ein durchgehend irrealer Bedingungssatz.", "ἦτε («wäred») statt ἐστε («sind»).",
  {"R1": [("ἐστε", "seid", None)], "R2": [("ἦτε", "wärt", None)]},
  {"R1": [("ἐστε", "sind", None)], "R2": [("ἦτε", "wäred", None)]},
  ["Der Wechsel von «seid» zu «würdet tun» ist grammatisch ungewöhnlich; ἦτε glättet ihn.",
   "Laut der automatischen Zuordnung lesen 01, 03, 05, 𝔓66 und 𝔓75 ἐστε, 04 und 032 ἦτε; 02 und 029 sind hier nicht erhalten."],
  ["ἦτε glättet de ungwöhnlich Satz.",
   "Nach de automatische Zueornig läsed 01, 03, 05, 𝔓66 und 𝔓75 ἐστε, 04 und 032 ἦτε."]),
 ("VAR-SBLGNTAPP-JHN-008-039-02:R2", "JHN.8.39", "würdet ihr die Werke Abrahams tun", "so tut die Werke Abrahams",
  "würded ir d Wärch vom Abraham tue", "dänn tüend d Wärch vom Abraham", "mittel",
  "ποιεῖτε statt ἐποιεῖτε: als Imperativ eine Aufforderung («so tut …»), als Indikativ eine Feststellung («so tut ihr …»).",
  "ποιεῖτε statt ἐποιεῖτε: als Befähl «dänn tüend …», als Feststellig «dänn tüend ir …».",
  {"R1": [("ἐποιεῖτε", "würdet ihr tun", None)], "R2": [("ποιεῖτε", "tut (ihr)", None)]},
  {"R1": [("ἐποιεῖτε", "würded ir tue", None)], "R2": [("ποιεῖτε", "tüend (ir)", None)]},
  ["Die Formen unterscheiden sich nur durch einen Buchstaben am Wortanfang; das kann beim Abschreiben ausgefallen oder ergänzt worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 04, 05, 032 und 𝔓75 ἐποιεῖτε, 03 und 𝔓66 ποιεῖτε; 02 und 029 sind hier nicht erhalten."],
  ["D Forme underscheided sich nu dur en Buechstabe.",
   "Nach de automatische Zueornig läsed 01, 04, 05, 032 und 𝔓75 ἐποιεῖτε, 03 und 𝔓66 ποιεῖτε."]),
 ("VAR-SBLGNTAPP-JHN-008-054-02:R2", "JHN.8.54", "Er ist unser Gott", "Er ist euer Gott", "Er isch üse Gott", "Er isch eue Gott", "gering",
  "Mit ὑμῶν wird der Satz zur indirekten Rede: «von dem ihr sagt, er sei euer Gott».", "Mit ὑμῶν wird de Satz zur indiräkte Red: «er sig eue Gott».",
  {"R1": [("ἡμῶν", "unser", None)], "R2": [("ὑμῶν", "euer", None)]},
  {"R1": [("ἡμῶν", "üse", None)], "R2": [("ὑμῶν", "eue", None)]},
  ["ἡμῶν und ὑμῶν wurden in der Aussprache der Zeit kaum unterschieden und werden in Handschriften oft verwechselt.",
   "Laut der automatischen Zuordnung lesen 02, 04, 032 und 𝔓75 ἡμῶν, ebenso die Korrekturen in 03 und 𝔓66; 01, 05 und die Erstschrift von 03 und 𝔓66 lesen ὑμῶν."],
  ["ἡμῶν und ὑμῶν hät mer dazmal fascht gliich usgsproche.",
   "Nach de automatische Zueornig läsed 02, 04, 032 und 𝔓75 ἡμῶν, au d Korrekture in 03 und 𝔓66; 01, 05 und d Erschtschrift vo 03 und 𝔓66 läsed ὑμῶν."]),
 ("VAR-SBLGNTAPP-JHN-008-059-01:R2", "JHN.8.59", "aus dem Tempel hinaus.", "aus dem Tempel hinaus, mitten durch sie hindurch, und ging so vorüber.",
  "us em Tämpel usegange.", "us em Tämpel usegange, mitte dur si dure, und isch eso verbiigange.", "mittel",
  "Der Zusatz erzählt, wie Jesus mitten durch die Gegner hindurchgeht.", "De Zuesatz verzellt, wie de Jesus mitte dur d Gägner dure gaat.",
  {"R1": [("ἱεροῦ", "Tempel", None)], "R2": [("ἱεροῦ διελθὼν διὰ μέσου αὐτῶν καὶ παρῆγεν οὕτως", "Tempel, mitten durch sie hindurchgehend, und ging so vorüber", "mit Zusatz")]},
  {"R1": [("ἱεροῦ", "Tämpel", None)], "R2": [("ἱεροῦ διελθὼν διὰ μέσου αὐτῶν καὶ παρῆγεν οὕτως", "Tämpel, mitte dur si dure, und isch eso verbiigange", "mit Zuesatz")]},
  ["Die Worte erinnern an [[LUK.4.30]] («er aber schritt mitten durch sie hindurch und ging weg»), und παράγων steht in [[JHN.9.1]]; der Zusatz kann daraus gebildet sein und den Übergang zu Kapitel 9 herstellen.",
   "Laut der automatischen Zuordnung lesen 01, 03, 05, 032, 𝔓66 und 𝔓75 ohne Zusatz, 02 und 04 mit ihm (04 im erfassten Wortlaut mit zusätzlichem ἐπορεύετο)."],
  ["D Wort erinnered a [[LUK.4.30]], und παράγων staat i [[JHN.9.1]]; de Zuesatz cha drus bildet sii.",
   "Nach de automatische Zueornig läsed 01, 03, 05, 032, 𝔓66 und 𝔓75 ohni Zuesatz, 02 und 04 mit."]),
 ("VAR-SBLGNTAPP-JHN-009-004-01:R2", "JHN.9.4", "Wir müssen", "Ich muss", "Mir müend", "Ich mues", "mittel",
  "Mit ἐμέ sagt Jesus es nur von sich; mit ἡμᾶς bezieht er die Jünger ein.", "Mit ἐμέ seit de Jesus s nu vo sich; mit ἡμᾶς nimmt er d Jünger dezue.",
  {"R1": [("ἡμᾶς", "wir", None)], "R2": [("Ἐμὲ", "ich", None)]},
  {"R1": [("ἡμᾶς", "mir", None)], "R2": [("Ἐμὲ", "ich", None)]},
  ["«Ich» passt zu «der mich gesandt hat» und kann daran angeglichen sein; umgekehrt kann «wir» die Jünger in den Auftrag einbeziehen wollen.",
   "Laut der automatischen Zuordnung lesen 01 (Erstschrift), 03, 05, 032, 𝔓66 und 𝔓75 ἡμᾶς, 01 (Korrektur), 02 und 04 ἐμέ."],
  ["«Ich» passt zu «wo mich gschickt hät»; «mir» cha d Jünger in Uftrag iibezie.",
   "Nach de automatische Zueornig läsed 01 (Erschtschrift), 03, 05, 032, 𝔓66 und 𝔓75 ἡμᾶς, 01 (Korrektur), 02 und 04 ἐμέ."]),
 ("VAR-SBLGNTAPP-JHN-009-006-01:R2", "JHN.9.6", "strich", "legte", "gstriche", "gleit", "gering",
  "ἐπέθηκεν («legte») statt ἐπέχρισεν («strich»).", "ἐπέθηκεν («hät gleit») statt ἐπέχρισεν («hät gstriche»).",
  {"R1": [("ἐπέχρισεν", "strich", None)], "R2": [("ἐπέθηκεν", "legte", None)]},
  {"R1": [("ἐπέχρισεν", "hät gstriche", None)], "R2": [("ἐπέθηκεν", "hät gleit", None)]},
  ["ἐπέθηκεν steht in der Erzählung des Geheilten ([[JHN.9.15]]); der Wortlaut kann daran angeglichen sein.",
   "Laut der automatischen Zuordnung liest 03 ἐπέθηκεν; 01, 02, 04, 05, 032, 𝔓66 und 𝔓75 lesen ἐπέχρισεν."],
  ["ἐπέθηκεν staat i [[JHN.9.15]]; de Wortlut cha dra aaglichen sii.",
   "Nach de automatische Zueornig lisst 03 ἐπέθηκεν; 01, 02, 04, 05, 032, 𝔓66 und 𝔓75 läsed ἐπέχρισεν."]),
 ("VAR-SBLGNTAPP-JHN-009-008-01:R2", "JHN.9.8", "als Bettler", "als Blinden", "als Bettler", "als Blinde", "gering",
  "τυφλός («blind») statt προσαίτης («Bettler»).", "τυφλός («blind») statt προσαίτης («Bettler»).",
  {"R1": [("προσαίτης", "Bettler", None)], "R2": [("τυφλὸς", "blind", None)]},
  {"R1": [("προσαίτης", "Bettler", None)], "R2": [("τυφλὸς", "blind", None)]},
  ["«Blind» kann aus der übrigen Erzählung eingetragen sein.",
   "Laut der automatischen Zuordnung lesen alle erfassten Handschriften (01, 02, 03, 04, 05, 032, 𝔓66, 𝔓75) προσαίτης; τυφλός haben unter den erfassten Texten die Ausgaben KJTR, RP und Stephanus."],
  ["«Blind» cha us de übrige Gschicht iitreit sii.",
   "Nach de automatische Zueornig läsed alli erfasste Handschrifte προσαίτης; τυφλός händ di druckte Usgabe KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-JHN-009-035-03:R2", "JHN.9.35", "an den Menschensohn", "an den Sohn Gottes", "a de Mänschesohn", "a de Sohn vo Gott", "bedeutsam",
  "Die Frage richtet sich auf den «Sohn Gottes» statt auf den «Menschensohn».", "D Frag gaat uf de «Sohn vo Gott» statt uf de «Mänschesohn».",
  {"R1": [("ἀνθρώπου", "Menschensohn", None)], "R2": [("θεοῦ", "Sohn Gottes", None)]},
  {"R1": [("ἀνθρώπου", "Mänschesohn", None)], "R2": [("θεοῦ", "Sohn vo Gott", None)]},
  ["«Sohn Gottes» ist die geläufigere Glaubensformel (vgl. [[JHN.1.34]], [[JHN.20.31]]) und kann die ungewöhnliche Frage nach dem Glauben an den «Menschensohn» ersetzt haben. In den Handschriften stehen beide Wörter oft als Kurzformen (θυ, ανου), die sich ähneln.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ἀνθρώπου. 032, 𝔓66 und 𝔓75 sind als «liest anders» geführt; im erfassten Wortlaut steht dort die Kurzform ανου (für ἀνθρώπου). 02 ist ebenfalls als «liest anders» geführt und hat die Kurzform θυ (für θεοῦ). 04 ist hier nicht erhalten. θεοῦ haben ausserdem die Ausgaben KJTR, RP und Stephanus."],
  ["«Sohn vo Gott» isch di gläufiger Glaubensformle (vgl. [[JHN.1.34]], [[JHN.20.31]]). I de Handschrifte stönd beidi Wörter oft als Churzforme (θυ, ανου).",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ἀνθρώπου; 032, 𝔓66 und 𝔓75 händ d Churzform ανου (für ἀνθρώπου), 02 d Churzform θυ (für θεοῦ)."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-008-001-059", "JHN.8.1-JHN.8.59", "section", "Die Frau vor Jesus, das Licht der Welt und der Streit um Abraham",
  ["TU-JHN-008-001-011", "TU-JHN-008-012-020", "TU-JHN-008-021-030", "TU-JHN-008-031-047", "TU-JHN-008-048-059"],
  "Im Tempel bringen Schriftgelehrte und Pharisäer eine beim Ehebruch ergriffene Frau zu Jesus; er verurteilt sie nicht (dieser Abschnitt, [[JHN.7.53]]–[[JHN.8.11]], "
  "steht im SBLGNT in Doppelklammern ⟦ ⟧). Dann nennt sich Jesus das Licht der Welt und beruft sich gegenüber den Pharisäern auf das Zeugnis des Vaters. Er kündigt an, "
  "dass er weggeht und sie in ihrer Sünde sterben werden, wenn sie nicht glauben, «dass ich bin»; wenn sie den Menschensohn erhöht haben, werden sie es erkennen. "
  "Zu Juden, die ihm geglaubt hatten, sagt er, wenn sie in seinem Wort blieben, werde die Wahrheit sie frei machen; im Streit darüber, wer ihr Vater sei – Abraham, Gott oder der Teufel –, wirft er ihnen "
  "vor, ihn töten zu wollen. Sie halten ihn für einen Samaritaner mit einem Dämon. Auf sein Wort «Bevor Abraham wurde, bin ich» heben sie Steine auf; Jesus verbirgt sich "
  "und geht aus dem Tempel hinaus.",
  SEG + " Der Abschnitt von der Frau beginnt im SBLGNT mit [[JHN.7.53]] (Teileinheit TU-JHN-007-053-053 in der Einheit zu Kapitel 7); TU-JHN-008-001-011 setzt ihn fort."),
 ("TU-JHN-008-001-011", "JHN.8.1-JHN.8.11", "narrative", "Jesus und die Frau, die beim Ehebruch ergriffen wurde", None,
  "Jesus geht zum Ölberg und lehrt frühmorgens im Tempel. Die Schriftgelehrten und Pharisäer bringen eine Frau, die beim Ehebruch ergriffen worden ist, stellen sie in die "
  "Mitte und fragen ihn, um ihn auf die Probe zu stellen, was er zum Gebot des Mose sage, solche zu steinigen. Jesus bückt sich und schreibt auf die Erde; dann sagt er, wer "
  "von ihnen ohne Sünde sei, solle als Erster einen Stein auf sie werfen. Einer nach dem anderen geht hinaus, angefangen bei den Ältesten. Jesus fragt die Frau, ob niemand "
  "sie verurteilt habe, sagt, auch er verurteile sie nicht, und schickt sie weg: Sie solle nicht mehr sündigen. Der SBLGNT setzt den Abschnitt ([[JHN.7.53]]–[[JHN.8.11]]) in "
  "Doppelklammern ⟦ ⟧; in der Textforschung wird er weithin als spätere Einfügung in das Johannesevangelium beurteilt. " + PA_DE + " Nach Angaben der Forschung steht er in "
  "einigen späteren Handschriften an anderer Stelle. Viele Kirchen lesen ihn als Teil der Heiligen Schrift.", None),
 ("TU-JHN-008-012-020", "JHN.8.12-JHN.8.20", "dialogue", "Das Licht der Welt und das Zeugnis des Vaters", None,
  "Jesus sagt: «Ich bin das Licht der Welt.» Die Pharisäer halten ihm vor, sein Zeugnis über sich selbst sei nicht wahr. Jesus antwortet, er wisse, woher er komme und wohin "
  "er gehe; nach ihrem Gesetz gelte das Zeugnis zweier, und neben ihm lege der Vater, der ihn gesandt hat, Zeugnis ab. Sie kennten weder ihn noch seinen Vater. Er "
  "redet dies bei der Schatzkammer im Tempel, und niemand nimmt ihn fest, denn seine Stunde ist noch nicht gekommen.", None),
 ("TU-JHN-008-021-030", "JHN.8.21-JHN.8.30", "dialogue", "«Wohin ich gehe, könnt ihr nicht kommen»", None,
  "Jesus sagt, er gehe weg, sie würden ihn suchen und in ihrer Sünde sterben. Die Juden fragen sich, ob er sich selbst töten wolle. Er sagt, sie seien von unten, er von oben; wenn sie "
  "nicht glauben, «dass ich bin», würden sie in ihren Sünden sterben. Auf die Frage «Wer bist du?» antwortet er mit einem schwer zu deutenden Satz und verweist auf den, der ihn gesandt hat; sie verstehen nicht, dass er vom "
  "Vater spricht. Wenn sie den Menschensohn erhöht haben, würden sie erkennen, «dass ich bin» und dass er redet, wie der Vater ihn gelehrt hat. Viele glauben an ihn.", None),
 ("TU-JHN-008-031-047", "JHN.8.31-JHN.8.47", "dialogue", "Wahrheit, Freiheit und die Frage nach dem Vater", None,
  "Zu den Juden, die ihm geglaubt hatten, sagt Jesus: Wenn sie in seinem Wort bleiben, werden sie die Wahrheit erkennen, und die Wahrheit wird sie frei machen. Sie berufen "
  "sich darauf, Nachkommen Abrahams zu sein und niemandem je als Sklaven gedient zu haben. Jesus antwortet, wer die Sünde tut, sei ein Sklave der Sünde; wenn der Sohn sie "
  "frei mache, seien sie wirklich frei. Weil sie ihn töten wollen, täten sie nicht die Werke Abrahams; sie berufen sich auf Gott als ihren einzigen Vater. Jesus sagt, wäre Gott ihr Vater, würden sie ihn lieben; "
  "sie stammten vom Vater, dem Teufel, dem Lügner und Menschenmörder von Anfang an, und hörten nicht, weil sie nicht aus Gott seien.", None),
 ("TU-JHN-008-048-059", "JHN.8.48-JHN.8.59", "dialogue", "«Bevor Abraham wurde, bin ich»", None,
  "Die Juden nennen Jesus einen Samaritaner, der einen Dämon habe. Jesus sagt, er ehre seinen Vater, und wer sein Wort bewahre, werde den Tod in Ewigkeit nicht sehen. "
  "Sie halten ihm entgegen, Abraham und die Propheten seien gestorben, und fragen, ob er grösser sei als Abraham. Jesus sagt, sein Vater verherrliche ihn; Abraham habe "
  "gejubelt, seinen Tag zu sehen. Auf den Einwand, er sei noch nicht fünfzig Jahre alt, antwortet er: «Bevor Abraham wurde, bin ich.» Sie heben Steine auf, um sie auf ihn "
  "zu werfen; Jesus verbirgt sich und geht aus dem Tempel hinaus.", None),
 ("TU-JHN-009-001-041", "JHN.9.1-JHN.9.41", "section", "Der Blindgeborene wird sehend",
  ["TU-JHN-009-001-012", "TU-JHN-009-013-023", "TU-JHN-009-024-034", "TU-JHN-009-035-041"],
  "Jesus sieht einen von Geburt an blinden Menschen. Auf die Frage der Jünger, wer gesündigt habe, antwortet er: weder er noch seine Eltern; an ihm sollten die Werke Gottes "
  "offenbar werden. Er streicht ihm einen Brei auf die Augen und schickt ihn zum Teich Siloam; der Mann kommt sehend zurück. Die Heilung geschah an einem Sabbat; die Pharisäer befragen ihn, die Juden "
  "seine Eltern, und diese weichen aus Furcht vor dem Ausschluss aus der Synagoge aus. Beim zweiten Verhör hält der Geheilte daran fest, dass Jesus von Gott sein müsse, und wird "
  "hinausgeworfen. Jesus findet ihn; der Mann glaubt an den Menschensohn. Jesus sagt, er sei zum Gericht gekommen, damit die Nichtsehenden sehen und die Sehenden blind werden; "
  "den Pharisäern, die fragen, ob auch sie blind seien, sagt er, ihre Sünde bleibe.", SEG),
 ("TU-JHN-009-001-012", "JHN.9.1-JHN.9.12", "narrative", "Die Heilung des Blindgeborenen", None,
  "Die Jünger fragen, ob der Mann oder seine Eltern gesündigt hätten, dass er blind geboren wurde. Jesus verneint beides: An ihm sollen die Werke Gottes offenbar werden; "
  "solange er in der Welt ist, ist er das Licht der Welt. Er macht aus Speichel einen Brei, streicht ihn dem Blinden auf die Augen und schickt ihn zum Teich Siloam; der Mann "
  "wäscht sich und kommt sehend zurück. Die Nachbarn streiten, ob er es sei; er sagt «Ich bin es» und erzählt, wie Jesus ihn geheilt hat, weiss aber nicht, wo Jesus ist.", None),
 ("TU-JHN-009-013-023", "JHN.9.13-JHN.9.23", "narrative", "Der Geheilte und seine Eltern werden befragt", None,
  "Man bringt den Geheilten zu den Pharisäern; es war Sabbat, als Jesus ihn heilte. Einige sagen, Jesus sei nicht von Gott, weil er den Sabbat nicht hält; andere fragen, "
  "wie ein Sünder solche Zeichen tun könne. Der Geheilte nennt Jesus einen Propheten. Die Juden glauben nicht, dass er blind war, und befragen seine Eltern; diese bestätigen, "
  "dass er ihr blind geborener Sohn ist, verweisen aber für alles Weitere auf ihn selbst, weil sie die Juden fürchten: Diese haben beschlossen, jeden aus der Synagoge "
  "auszuschliessen, der Jesus als Christus bekennt.", None),
 ("TU-JHN-009-024-034", "JHN.9.24-JHN.9.34", "dialogue", "Das zweite Verhör und der Ausschluss", None,
  "Zum zweiten Mal gerufen, wird der Geheilte aufgefordert, Gott die Ehre zu geben; die Befragenden erklären, Jesus sei ein Sünder. Er sagt, das wisse er nicht, er wisse nur, dass er blind war und "
  "jetzt sieht, und fragt, ob auch sie Jesu Jünger werden wollten. Sie beschimpfen ihn und berufen sich auf Mose. Er hält ihnen entgegen, Gott höre nicht auf "
  "Sünder, und noch nie habe man gehört, dass einem Blindgeborenen die Augen geöffnet wurden; wäre dieser nicht von Gott, könnte er nichts tun. Sie sagen, er sei ganz in Sünden geboren, und werfen ihn hinaus.", None),
 ("TU-JHN-009-035-041", "JHN.9.35-JHN.9.41", "dialogue", "Sehen und Blindsein", None,
  "Jesus findet den Hinausgeworfenen und fragt ihn, ob er an den Menschensohn glaube. Als Jesus sich als der zu erkennen gibt, der mit ihm redet, sagt der Mann «Ich glaube, "
  "Herr» und fällt vor ihm nieder. Jesus sagt, er sei zum Gericht in diese Welt gekommen, damit die Nichtsehenden sehen und die Sehenden blind werden. Pharisäer, die bei ihm sind, fragen, ob "
  "auch sie blind seien; Jesus antwortet: Wären sie blind, hätten sie keine Sünde; nun aber sagten sie «Wir sehen», ihre Sünde bleibe.", None),
]
UNITS_GSW = {
 "TU-JHN-008-001-059": ("D Frau vor em Jesus, s Liecht vo de Wält und de Striit um de Abraham",
  "Im Tämpel bringed Schriftgleerti und Pharisäer e Frau zum Jesus, wo bim Ehebruch verwütscht worde isch; er verurteilt si nöd (dä Abschnitt, [[JHN.7.53]]–[[JHN.8.11]], staat "
  "im SBLGNT i Doppelklammere ⟦ ⟧). Dänn nännt sich de Jesus s Liecht vo de Wält und beruefft sich gägenüber de Pharisäer uf s Zügnis vom Vatter. Er seit, dass er wäggaat und "
  "dass si i irer Sünd stärbed, wänn si nöd glaubed, «dass ich bi»; wänn si de Mänschesohn erhöcht händ, wärded si s erchänne. Zu Jude, wo ihm glaubt händ, seit er, wänn si i sim Wort bliibid, wärdi d Wahrheit "
  "si frei mache; im Striit, wer ire Vatter sig – de Abraham, Gott oder de Tüüfel –, wirft er ine vor, si welled en töte. Si heissed en en Samaritaner mit eme Dämon. Uf sis "
  "Wort «Bevor de Abraham worde isch, bin ich» nämed si Stei uf; de Jesus versteckt sich und gaat us em Tämpel use."),
 "TU-JHN-008-001-011": ("De Jesus und d Frau, wo bim Ehebruch verwütscht worde isch",
  "De Jesus gaat uf de Ölberg und lehrt am Morge früe im Tämpel. D Schriftgleerte und d Pharisäer bringed e Frau, wo bim Ehebruch verwütscht worde isch, stelled si i d Mitti "
  "und fröged en, zum en uf d Prob z stele, was er zum Gebot vom Mose säg, settigi z steinige. De Jesus bückt sich und schriibt uf de Bode; dänn seit er, wer vo ine ohni Sünd "
  "sig, söll als Erschte en Stei uf si rüere. Eine nach em andere gaat use, aagfange bi de Ältischte. De Jesus fröget d Frau, öb si niemer verurteilt heig, seit, au er verurteili "
  "si nöd, und schickt si furt: Si söll nüme sündige. De SBLGNT setzt de Abschnitt ([[JHN.7.53]]–[[JHN.8.11]]) i Doppelklammere ⟦ ⟧; i de Textforschig wird er wiitume als "
  "spööteri Iifüegig is Johannesevangelium beurteilt. " + PA_GSW + " Nach Aagabe vo de Forschig staat er i es paar spöötere Handschrifte a anderer Stell. Vili Chile läsed en "
  "als Teil vo de Heilige Schrift."),
 "TU-JHN-008-012-020": ("S Liecht vo de Wält und s Zügnis vom Vatter",
  "De Jesus seit: «Ich bi s Liecht vo de Wält.» D Pharisäer händ em vor, sis Zügnis über sich sälber sig nöd wahr. De Jesus antwortet, er wüssi, vo wo er chömi und wohi er "
  "gang; nach irem Gsetz gälti s Zügnis vo zwei, und näbe ihm legi de Vatter, wo en gschickt hät, Zügnis ab. Si känned weder ihn no sin Vatter. Er redt das bi de "
  "Schatzchammer im Tämpel, und niemer nimmt en gfange, wil sini Stund no nöd choo isch."),
 "TU-JHN-008-021-030": ("«Wo ich hiigaa, chönd ir nöd härecho»",
  "De Jesus seit, er gang wäg, si wärdid en sueche und i irer Sünd stärbe. D Jude fröged sich, öb er sich sälber well umbringe. Er seit, si sigid vo unde, er vo obe; wänn si nöd glaubid, "
  "«dass ich bi», wärdid si i irne Sünde stärbe. Uf d Frag «Wer bisch du?» antwortet er mit eme schwär verständliche Satz und verwiist uf dä, wo en gschickt hät; si verstönd nöd, dass er vom Vatter redt. Wänn si de "
  "Mänschesohn erhöcht händ, wärdid si erchänne, «dass ich bi» und dass er redt, wie de Vatter en glehrt hät. Vili glaubed a en."),
 "TU-JHN-008-031-047": ("Wahrheit, Freiheit und d Frag nach em Vatter",
  "Zu de Jude, wo ihm glaubt händ, seit de Jesus: Wänn si i sim Wort bliibed, wärded si d Wahrheit erchänne, und d Wahrheit wird si frei mache. Si beruefed sich druf, dass si "
  "Nachkomme vom Abraham sigid und niemertem je als Sklave dient heigid. De Jesus antwortet, wer d Sünd tuet, sig en Sklav vo de Sünd; wänn de Sohn si frei machi, sigid si würkli frei. Wil si en "
  "welled töte, tüegid si nöd d Wärch vom Abraham; si beruefed sich uf Gott als irn einzige Vatter. De Jesus seit, wänn Gott ire Vatter wär, würdid si en liebe; si stammid vom Vatter, em Tüüfel, "
  "em Lüügner und Mänschemörder vo Aafang aa, und ghörid nöd, wil si nöd us Gott sigid."),
 "TU-JHN-008-048-059": ("«Bevor de Abraham worde isch, bin ich»",
  "D Jude säged em Jesus, er sig en Samaritaner und heig en Dämon. De Jesus seit, er ehri sin Vatter, und wer sis Wort bhalti, wärdi de Tod i Ewigkeit nöd gseh. Si händ em "
  "entgäge, de Abraham und d Prophete sigid gstorbe, und fröged, öb er grösser sig als de Abraham. De Jesus seit, sin Vatter verherrlichi en; de Abraham heig gjublet, dass er "
  "sin Tag söll gseh. Uf de Iiwand, er sig no nöd füfzg Jahr alt, antwortet er: «Bevor de Abraham worde isch, bin ich.» Si nämed Stei uf, zum uf en z rüere; de Jesus versteckt "
  "sich und gaat us em Tämpel use."),
 "TU-JHN-009-001-041": ("De Blindgeboreni wird sehend",
  "De Jesus gseht en Mänsch, wo vo Geburt aa blind isch. Uf d Frag vo de Jünger, wer gsündiget heig, antwortet er: weder er no sini Eltere; a ihm söled d Wärch vo Gott offebar "
  "wärde. Er striicht em en Brei uf d Auge und schickt en zum Teich Siloam; de Maa chunnt sehend zrugg. D Heilig isch amene Sabbat gscheh; d Pharisäer fröged en uus, d Jude sini Eltere, und die wiiched "
  "us Angscht vor em Uusschluss us de Synagoge uus. Bim zweite Verhör bliibt de Gheilt debii, dass de Jesus vo Gott sii müesi, und wird usegworfe. De Jesus findt en; de Maa "
  "glaubt a de Mänschesohn. De Jesus seit, er sig zum Gricht choo, demit die, wo nöd gsehnd, gsehnd und die, wo gsehnd, blind wärded; de Pharisäer, wo fröged, öb au si blind "
  "sigid, seit er, iri Sünd bliibi."),
 "TU-JHN-009-001-012": ("D Heilig vom Blindgeborne",
  "D Jünger fröged, öb de Maa oder sini Eltere gsündiget heigid, dass er blind gebore worde isch. De Jesus seit zu beidem nei: A ihm söled d Wärch vo Gott offebar wärde; solang "
  "er i de Wält isch, isch er s Liecht vo de Wält. Er macht us Spöiz en Brei, striicht en em Blinde uf d Auge und schickt en zum Teich Siloam; de Maa wäscht sich und chunnt "
  "sehend zrugg. D Nachbere strited, öb er s sig; er seit «Ich bi s» und verzellt, wie de Jesus en gheilt hät, weiss aber nöd, wo de Jesus isch."),
 "TU-JHN-009-013-023": ("De Gheilt und sini Eltere wärded befröget",
  "Mer bringt de Gheilt zu de Pharisäer; es isch Sabbat gsii, won en de Jesus gheilt hät. Es paar säged, de Jesus sig nöd vo Gott, wil er de Sabbat nöd haltet; anderi "
  "fröged, wie en Sünder settigi Zeiche chönn tue. De Gheilt nännt de Jesus en Prophet. D Jude glaubed nöd, dass er blind gsii isch, und fröged sini Eltere; die bestätiged, "
  "dass er ire blind gebore Sohn isch, verwiised aber für alles Wiitere uf en sälber, wil si vor de Jude Angscht händ: Die händ beschlosse, jede us de Synagoge uszschlüüsse, "
  "wo de Jesus als Christus bekännt."),
 "TU-JHN-009-024-034": ("S zweit Verhör und de Uusschluss",
  "Zum zweite Mal grüeft, wird de Gheilt ufgforderet, Gott d Ehr z gää; di Befrögende säged, de Jesus sig en Sünder. Er seit, das wüssi er nöd, er wüssi nu, dass er blind gsii isch und jetzt gseht, "
  "und fröget, öb au si sini Jünger welled wärde. Si beschimpfed en und beruefed sich uf de Mose. Er hebt ine entgäge, Gott losi nöd uf Sünder, und no nie heig mer ghört, dass eim, wo blind gebore isch, d Auge ufgmacht worde sigid; wär dä nöd vo Gott, "
  "chönnt er nüüt mache. Si säged, er sig ganz i Sünde gebore, und rüered en use."),
 "TU-JHN-009-035-041": ("Gseh und blind sii",
  "De Jesus findt de Usegworfnig und fröget en, öb er a de Mänschesohn glaubi. Wo sich de Jesus als dä z erchänne git, wo mit ihm redt, seit de Maa «Ich glaube, Herr» und "
  "fallt vor ihm uf d Chnü. De Jesus seit, er sig zum Gricht i die Wält choo, demit die, wo nöd gsehnd, gsehnd und die, wo gsehnd, blind wärded. Pharisäer, wo bi ihm sind, fröged, öb au si "
  "blind sigid; de Jesus antwortet: Wäred si blind, hetted si kei Sünd; jetzt aber säged si «Mir gsehnd», iri Sünd bliibi."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("Johanneische Schlüsselwörter sind nach den Grundentscheiden zu Johannes 1–3 (scripts/authoring/johannes_text_01_03.py) einheitlich "
  "wiedergegeben: ἐγώ εἰμι «Ich bin …» (auch absolut «ich bin»: [[JHN.8.24]], [[JHN.8.28]], [[JHN.8.58]]; als Selbstidentifikation «Ich bin es»: "
  "[[JHN.9.9]]), δόξα/δοξάζω «Herrlichkeit/verherrlichen» (Ausnahme «Ehre», wo das Ansehen bei Menschen gemeint ist: [[JHN.8.50]], "
  "[[JHN.8.54]], [[JHN.9.24]]), σημεῖον «Zeichen», μένω «bleiben», ἀμὴν ἀμήν «Amen, amen», κόσμος «Welt», ὑψόω «erhöhen»."),
 ("οἱ Ἰουδαῖοι ist wörtlich mit «die Juden» wiedergegeben. Das ist eine Deutungsentscheidung (Alternative: kontextbezogen «die jüdischen "
  "Führer» o. Ä.; Begründung in den decisions zu [[JHN.8.22]]). In Kapitel 8 und 9 bezeichnet das Wort die Gesprächspartner und Gegner Jesu "
  "in einem Streit, an dem auf allen Seiten Juden beteiligt sind; in [[JHN.9.22]] fürchten jüdische Eltern «die Juden». Die Wiedergabe ist "
  "nicht als Aussage über das jüdische Volk zu lesen; zur Wirkungsgeschichte von [[JHN.8.44]] siehe die Entscheidung dort."),
 ("[[JHN.8.1]]–[[JHN.8.11]] gehört zum Abschnitt [[JHN.7.53]]–[[JHN.8.11]], den der SBLGNT in Doppelklammern ⟦ ⟧ setzt. Er ist übersetzt, "
  "weil er im Ausgangstext steht; die schliessende Klammer steht am Ende von 8,11. In der Textforschung wird der Abschnitt weithin als "
  "spätere Einfügung beurteilt; viele Kirchen lesen ihn als Teil der Heiligen Schrift. " + PA_DE),
 ("In den CNTR-Transkriptionen von 01, 032 und 𝔓75 fehlen [[JHN.9.38]] und der Anfang von [[JHN.9.39]] («Und Jesus sagte»); der SBLGNT-Apparat "
  "verzeichnet das nicht, deshalb steht es nur als Hinweis bei der Entscheidung zu 9,38."),
 ("Historisches Präsens («sie bringen», «sagt») ist beibehalten. ὅτι vor direkter Rede ist nicht eigens übersetzt; οὖν ist meist mit «da» "
  "oder «nun» wiedergegeben."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Johanneischi Schlüsselwörter wie i de Grundentscheid zu Johannes 1–3 (scripts/authoring/johannes_text_01_03.py): ἐγώ εἰμι «Ich bi …», "
  "δόξα «Herrlichkeit» («Ehr», wo s Aasee bi Mänsche meint: [[JHN.8.50]], [[JHN.8.54]], [[JHN.9.24]]), absolut ἐγώ εἰμι «ich bi», als Antwort «Ich bi s» ([[JHN.9.9]]), σημεῖον «Zeiche», μένω «bliibe», ἀμὴν ἀμήν «Amen, amen, ich säge eu», κόσμος «Wält», ὑψόω «erhöche»."),
 ("οἱ Ἰουδαῖοι heisst wörtlich «d Jude»; das isch en Düütigsentscheid (Alternative: «di jüdische Füerer»), lueg [[JHN.8.22]]. Es isch nöd als "
  "Uussag über s jüdisch Volk z läse."),
 ("[[JHN.8.1]]–[[JHN.8.11]] ghört zum Abschnitt [[JHN.7.53]]–[[JHN.8.11]], wo de SBLGNT i Doppelklammere ⟦ ⟧ setzt. " + PA_GSW),
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
            raise SystemExit(f"Kapitel {c}: Verse ohne Tokens")
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Liecht, Wält), ä für offenes e.",
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/johannes_text_08_09.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 8–9 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
