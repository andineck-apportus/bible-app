#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 18–19 (Rede vom Leben in der Gemeinde; Ehe und Scheidung, Kinder, der junge Mann mit
vielen Gütern, Lohn der Nachfolge) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_18_19.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- [[MAT.18.11]] steht nicht im SBLGNT (keine Tokens) und erhält keinen Übersetzungstext; der Wortlaut steht als
  Alternative bei [[MAT.18.10]] (VAR-SBLGNTAPP-MAT-018-010-01).
- [[MAT.19.17]]: Der SBLGNT-Apparat verzeichnet die Lesart von RP («Was nennst du mich gut? Niemand ist gut ausser
  einem: Gott»); sie fehlt in den importierten Variantendaten (kein Datensatz VAR-SBLGNTAPP-MAT-019-017-01) und steht
  deshalb in decisions und translation_notes, nicht als Alternative.
- Die Rede Jesu in Kapitel 18 läuft von [[MAT.18.3]] bis [[MAT.18.20]] und, nach der Frage des Petrus, von
  [[MAT.18.22]] bis [[MAT.18.35]]; Reden innerhalb des Gleichnisses stehen in ‹ ›.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1)
bzw. aus den CNTR-Transkriptionen (Sekundärtranskription), nicht aus eigener Prüfung der Handschriften. Zahlen zu
Wortvorkommen sind per Skript aus den SBLGNT-Tokens (Wortformen) ermittelt.
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
CHAPTERS = ((18, 35), (19, 30))
NO_TOKENS = {"MAT.18.11"}  # im SBLGNT nicht enthalten; KJV-Zählung führt den Vers

DE = {
 # ------------------------------------------------------------ Kapitel 18
 "MAT.18.1": "[In]{1} [jener]{2} [Stunde]{3,4} [traten]{5} [die Jünger]{6,7} [an Jesus]{8,9} [heran]{5} und [sagten]{10}: «[Wer]{11} [ist]{14} [denn]{12} [der Grösste]{13} [im]{15,16} [Reich]{17} [der Himmel]{18,19}?»",
 "MAT.18.2": "Und{1} [er rief]{2} [ein Kind]{3} [herbei]{2}, [stellte]{4} [es]{5} [in]{6} [ihre]{8} [Mitte]{7}",
 "MAT.18.3": "und{1} [sagte]{2}: [Amen]{3}, [ich sage]{4} [euch]{5}: [Wenn]{6} [ihr euch]{8} [nicht]{7} [umwendet]{8} und{9} [wie]{11} [die Kinder]{12,13} [werdet]{10}, [werdet ihr]{16} [gewiss nicht]{14,15} [in]{17} [das Reich]{18,19} [der Himmel]{20,21} [hineinkommen]{16}.",
 "MAT.18.4": "[Wer]{1} [sich]{4} [nun]{2} [klein macht]{3} [wie]{5} [dieses]{8} [Kind]{6,7}, [der]{9} [ist]{10} [der Grösste]{11,12} [im]{13,14} [Reich]{15} [der Himmel]{16,17}.",
 "MAT.18.5": "Und{1} [wer]{2,3} [ein]{5} [solches]{7} [Kind]{6} [in]{8} [meinem]{11} [Namen]{9,10} [aufnimmt]{4}, [nimmt]{13} [mich]{12} [auf]{13}.",
 "MAT.18.6": "[Wer]{1,3} [aber]{2} [einen]{5} [dieser]{8} [Kleinen]{6,7}, [die]{9} [an]{11} [mich]{12} [glauben]{10}, [zu Fall bringt]{4}, [für den]{14} [wäre es besser]{13}, [dass]{15} [ihm]{22} [ein grosser Mühlstein]{17,18} [um]{19} [den Hals]{20,21} [gehängt würde]{16} und{23} [er]{24} [in]{25} [der Tiefe]{26,27} [des Meeres]{28,29} [versenkt würde]{24}.",
 "MAT.18.7": "[Wehe]{1} [der Welt]{2,3} [wegen]{4} [der Fallstricke]{5,6}! [Denn]{8} [es ist unvermeidlich]{7}, dass [die Fallstricke]{10,11} [kommen]{9}; [doch]{12} [wehe]{13} [dem Menschen]{14,15}, [durch]{16} [den]{17} [der Fallstrick]{18,19} [kommt]{20}!",
 "MAT.18.8": "[Wenn]{1} [aber]{2} [deine]{5} [Hand]{3,4} [oder]{6} [dein]{9} [Fuss]{7,8} [dich]{11} [zu Fall bringt]{10}, [hau]{12} [ihn]{13} [ab]{12} und{14} [wirf]{15} ihn [von]{16} [dir]{17} [weg]{15}! [Es ist besser]{18,20} [für dich]{19}, [verstümmelt]{25} [oder]{26} [lahm]{27} [in]{22} [das Leben]{23,24} [hineinzugehen]{21}, [als]{28} [mit]{34} [zwei]{29} [Händen]{30} [oder]{31} [zwei]{32} [Füssen]{33} [in]{36} [das]{37} [ewige]{39,40} [Feuer]{38} [geworfen zu werden]{35}.",
 "MAT.18.9": "Und{1} [wenn]{2} [dein]{5} [Auge]{3,4} [dich]{7} [zu Fall bringt]{6}, [reiss]{8} [es]{9} [heraus]{8} und{10} [wirf]{11} es [von]{12} [dir]{13} [weg]{11}! [Es ist besser]{14,16} [für dich]{15}, [einäugig]{17} [in]{18} [das Leben]{19,20} [hineinzugehen]{21}, [als]{22} [mit]{25} [zwei]{23} [Augen]{24} [in]{27} [die Hölle]{28,29} [des Feuers]{30,31} [geworfen zu werden]{26}.",
 "MAT.18.10": "[Seht zu]{1}, [dass ihr]{3} [nicht]{2} [einen]{4} [dieser]{7} [Kleinen]{5,6} [verachtet]{3}! [Denn]{9} [ich sage]{8} [euch]{10}: [Ihre]{14} [Engel]{12,13} [in den Himmeln]{15,16} [sehen]{19} [allezeit]{17,18} [das Angesicht]{20,21} [meines]{24} [Vaters]{22,23} [in den Himmeln]{25-27}. ~11(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.18.12": "[Was]{1} [meint]{3} [ihr]{2}? [Wenn]{4} [ein]{6} [Mensch]{7} [hundert]{8} [Schafe]{9} [hat]{5} und{10} [eines]{12} [von]{13} [ihnen]{14} [sich verirrt]{11}, [wird er]{16} [nicht]{15} [die]{17} [neunundneunzig]{18,19} [auf]{20} [den Bergen]{21,22} [lassen]{16} und{23} [hingehen]{24} und [das]{26} [verirrte]{27} [suchen]{25}?",
 "MAT.18.13": "Und{1} [wenn]{2} [es ihm gelingt]{3}, [es]{5} [zu finden]{4} – [amen]{6}, [ich sage]{7} [euch]{8}: [Er freut sich]{10} [über]{11} [dieses]{12} [mehr]{13} [als]{14} [über]{15} [die]{16} [neunundneunzig]{17,18}, [die]{19} [sich]{21} [nicht]{20} [verirrt haben]{21}. ~9(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.18.14": "[So]{1} [ist es]{3} [nicht]{2} [der Wille]{4} [eures]{8} [Vaters]{6,7} [in den Himmeln]{9-11}, [dass]{12} [eines]{14} [dieser]{17} [Kleinen]{15,16} [verloren geht]{13}. ~5(ἔμπροσθεν «vor» umschreibt ehrfürchtig den Genitiv; in «der Wille eures Vaters» enthalten)",
 "MAT.18.15": "[Wenn]{1} [aber]{2} [dein]{8} [Bruder]{6,7} [gegen]{4} [dich]{5} [sündigt]{3}, [geh hin]{9} und [weise]{10} [ihn]{11} [zurecht]{10}, [zwischen]{12} [dir]{13} [und]{14} [ihm]{15} [allein]{16}. [Wenn]{17} [er]{19} auf [dich]{18} [hört]{19}, [hast du]{20} [deinen]{23} [Bruder]{21,22} [gewonnen]{20}.",
 "MAT.18.16": "[Wenn]{1} [er]{4} [aber]{2} [nicht]{3} [hört]{4}, [nimm]{5} [noch]{8} [einen]{9} [oder]{10} [zwei]{11} [mit]{6} [dir]{7} [dazu]{5}, [damit]{12} [jede]{20} [Sache]{21} [auf]{13} [die Aussage]{14} [von zwei]{15} [oder]{17} [drei]{18} [Zeugen]{16} [hin]{13} [festgestellt wird]{19}.",
 "MAT.18.17": "[Wenn]{1} [er]{3} [aber]{2} [nicht]{3} auf [sie]{4} [hört]{3}, [sag es]{5} [der Gemeinde]{6,7}; [wenn]{8} [er]{13} [aber]{9} [auch]{10} auf [die Gemeinde]{11,12} [nicht]{13} [hört]{13}, [soll er]{14} [für dich]{15} [sein]{14} [wie]{16} [der Heide]{17,18} und{19} [der Zöllner]{20,21}.",
 "MAT.18.18": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Alles, was]{4,5} [ihr]{6} [auf]{7} [der Erde]{8,9} [bindet]{6}, [wird]{10} [im]{12} [Himmel]{13} [gebunden sein]{11}, und{14} [alles, was]{15,16} [ihr]{17} [auf]{18} [der Erde]{19,20} [löst]{17}, [wird]{21} [im]{23} [Himmel]{24} [gelöst sein]{22}.",
 "MAT.18.19": "[Wiederum]{1}, [amen]{2}, [ich sage]{3} [euch]{4}: [Wenn]{6} [zwei]{7} [von]{9} [euch]{10} [auf]{11} [der Erde]{12,13} [einig werden]{8} [über]{14} [irgendeine]{15} [Sache]{16}, [um die]{17,18} [sie bitten]{19}, [wird sie]{20} [ihnen]{21} [von]{22} [meinem]{25} [Vater]{23,24} [in den Himmeln]{26-28} [zuteilwerden]{20}. ~5(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.18.20": "[Denn]{2} [wo]{1} [zwei]{4} [oder]{5} [drei]{6} [in]{8} [meinem]{9,10} [Namen]{11} [versammelt]{7} [sind]{3}, [da]{12} [bin ich]{13} [mitten]{14,15} [unter ihnen]{16}.",
 "MAT.18.21": "[Da]{1} [trat]{2} [Petrus]{4,5} [an ihn]{3} [heran]{2} und [sagte]{6}: «[Herr]{7}, [wie oft]{8} [wird]{9} [mein]{14} [Bruder]{12,13} [gegen]{10} [mich]{11} [sündigen]{9} und{15} [ich]{16} [ihm]{17} [vergeben]{16}? [Bis zu]{18} [siebenmal]{19}?»",
 "MAT.18.22": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: [Ich sage]{6} [dir]{7} [nicht]{5}: [bis zu]{8} [siebenmal]{9}, [sondern]{10} [bis zu]{11} [siebenundsiebzigmal]{12,13}.",
 "MAT.18.23": "[Darum]{1,2} [gleicht]{3} [das Reich]{4,5} [der Himmel]{6,7} [einem König]{9}, [der]{10} [mit]{14} [seinen]{17} [Knechten]{15,16} [abrechnen]{12,13} [wollte]{11}. ~8(ἀνθρώπῳ «einem Menschen» vor βασιλεῖ «König» ist semitisierende Ausdrucksweise; in «einem König» enthalten)",
 "MAT.18.24": "[Als]{1} [er]{3} [aber]{2} [anfing]{1} [abzurechnen]{4}, [wurde]{5} [einer]{7} [zu ihm]{6} [gebracht]{5}, [der]{8} [zehntausend]{9} [Talente]{10} [schuldete]{8}.",
 "MAT.18.25": "Da [er]{4} [aber]{3} [nicht]{1} [zahlen]{5} [konnte]{2}, [befahl]{6} [der Herr]{8,9}, [ihn]{7} [zu verkaufen]{10}, [samt]{11} [seiner Frau]{12,13} und{14} [den Kindern]{15,16} und{17} [allem]{18}, [was]{19} [er hat]{20}, und{21} [so die Schuld zu bezahlen]{22}.",
 "MAT.18.26": "[Da]{2} [fiel]{1} [der Knecht]{3,4} [zu Boden]{1}, [warf sich]{5} [vor ihm]{6} [nieder]{5} und [sagte]{7}: «[Hab Geduld]{8} [mit]{9} [mir]{10}, und{11} [ich werde]{13} [dir]{14} [alles]{12} [zurückzahlen]{13}!»",
 "MAT.18.27": "[Der Herr]{3,4} [jenes]{7} [Knechtes]{5,6} [aber]{2} [hatte Erbarmen]{1}, [liess]{8} [ihn]{9} [frei]{8} und{10} [erliess]{13} [ihm]{14} [das Darlehen]{11,12}.",
 "MAT.18.28": "[Jener]{5} [Knecht]{3,4} [aber]{2} [ging hinaus]{1} und [fand]{6} [einen]{7} [seiner]{10} [Mitknechte]{8,9}, [der]{11} [ihm]{13} [hundert]{14} [Denare]{15} [schuldete]{12}; und{16} [er packte]{17} [ihn]{18}, [würgte ihn]{19} und [sagte]{20}: «[Bezahl]{21}, [wenn]{22} [du]{24} [etwas]{23} [schuldest]{24}!»",
 "MAT.18.29": "[Da]{2} [fiel]{1} [sein]{5} [Mitknecht]{3,4} [nieder]{1}, [bat]{6} [ihn]{7} und [sagte]{8}: «[Hab Geduld]{9} [mit]{10} [mir]{11}, und{12} [ich werde]{13} es [dir]{14} [zurückzahlen]{13}!»",
 "MAT.18.30": "[Er]{1} [aber]{2} [wollte]{4} [nicht]{3}, [sondern]{5} [ging hin]{6} und [warf]{7} [ihn]{8} [ins]{9} [Gefängnis]{10}, [bis]{11,12} [er]{13} [die Schuld]{14,15} [bezahlt hätte]{13}.",
 "MAT.18.31": "[Als]{1} [nun]{2} [seine]{5} [Mitknechte]{3,4} [sahen]{1}, [was]{6} [geschehen war]{7}, [wurden sie]{8} [sehr]{9} [traurig]{8}, und{10} [sie gingen]{11} und [berichteten]{12} [ihrem]{15} [Herrn]{13,14} [alles]{16}, [was]{17} [geschehen war]{18}.",
 "MAT.18.32": "[Da]{1} [rief]{2} [ihn]{3} [sein]{6} [Herr]{4,5} [zu sich]{2} und [sagt]{7} [zu ihm]{8}: «Du [böser]{10} [Knecht]{9}! [Jene]{14} [ganze]{11} [Schuld]{12,13} [habe ich]{15} [dir]{16} [erlassen]{15}, [weil]{17} [du]{18} [mich]{19} [gebeten hast]{18}.",
 "MAT.18.33": "[Hättest]{2} [nicht]{1} [auch]{3} [du]{4} dich über [deinen]{8} [Mitknecht]{6,7} [erbarmen]{5} [müssen]{2}, [wie]{9} [auch ich]{10} mich über [dich]{11} [erbarmt habe]{12}?»",
 "MAT.18.34": "Und{1} [sein]{5} [Herr]{3,4} [wurde zornig]{2} und [lieferte]{6} [ihn]{7} [den]{8} [Folterknechten]{9} [aus]{6}, [bis]{10,11} [er]{12} [die]{14} [ganze]{13} [Schuld]{15} [bezahlt hätte]{12}.",
 "MAT.18.35": "[So]{1} [wird]{8} [auch]{2} [mein]{5} [himmlischer]{6,7} [Vater]{3,4} [mit euch]{9} [verfahren]{8}, [wenn]{10} [ihr]{12} [nicht]{11} [von]{17} [Herzen]{18-20} [vergebt]{12}, [jeder]{13} [seinem]{16} [Bruder]{14,15}.",
 # ------------------------------------------------------------ Kapitel 19
 "MAT.19.1": "Und{1} [es geschah]{2}, [als]{3} [Jesus]{5,6} [diese]{9} [Worte]{7,8} [beendet hatte]{4}, da [brach er]{10} [von]{11} [Galiläa]{12,13} [auf]{10} und{14} [kam]{15} [in]{16} [das Gebiet]{17,18} [von Judäa]{19,20} [jenseits]{21} [des Jordan]{22,23}.",
 "MAT.19.2": "Und{1} [grosse]{5} [Menschenmengen]{4} [folgten]{2} [ihm]{3}, und{6} [er heilte]{7} [sie]{8} [dort]{9}.",
 "MAT.19.3": "Und{1} [Pharisäer]{4} [traten]{2} [an ihn]{3} [heran]{2}, um [ihn]{6} [auf die Probe zu stellen]{5}, und{7} [sagten]{8}: «[Ist es]{10} [einem Mann]{11} [erlaubt]{10}, [seine]{15} [Frau]{13,14} [aus]{16} [jedem]{17} [Grund]{18} [zu entlassen]{12}?» ~9(εἰ leitet die direkte Frage ein; nicht eigens wiedergegeben)",
 "MAT.19.4": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: «[Habt ihr]{6} [nicht]{5} [gelesen]{6}, [dass]{7} [der Schöpfer]{8,9} [sie]{16} [von Anfang an]{10,11} ‹[männlich]{12} und{13} [weiblich]{14} [geschaffen hat]{15}›",
 "MAT.19.5": "und{1} [gesagt hat]{2}: ‹[Darum]{3,4} [wird]{5} [ein Mensch]{6} [Vater]{7,8} und{9} [Mutter]{10,11} [verlassen]{5} und{12} [an]{14} [seiner]{16} [Frau]{15} [hängen]{13}, und{17} [die zwei]{19,20} [werden]{18} [ein]{21,23} [Fleisch]{22} [sein]{18}›?",
 "MAT.19.6": "[So]{1} [sind sie]{3} [nicht mehr]{2} [zwei]{4}, [sondern]{5} [ein]{7} [Fleisch]{6}. [Was]{8} [nun]{9} [Gott]{10,11} [zusammengefügt hat]{12}, [soll]{15} [der Mensch]{13} [nicht]{14} [trennen]{15}.»",
 "MAT.19.7": "[Sie sagen]{1} [zu ihm]{2}: «[Warum]{3} [hat]{6} [Mose]{5} [dann]{4} [geboten]{6}, [einen Scheidebrief]{8,9} [zu geben]{7} und{10} [sie]{12} [zu entlassen]{11}?»",
 "MAT.19.8": "[Er sagt]{1} [zu ihnen]{2}: «[Mose]{4} [hat]{9} [euch]{10} [wegen]{5} [eurer]{8} [Herzenshärte]{6,7} [erlaubt]{9}, [eure]{14} [Frauen]{12,13} [zu entlassen]{11}; [von Anfang an]{15,16} [aber]{17} [ist es]{19} [nicht]{18} [so]{20} [gewesen]{19}. ~3(ὅτι leitet die direkte Rede ein)",
 "MAT.19.9": "[Ich sage]{1} [euch]{3} [aber]{2}: [Wer]{5,6} [seine]{10} [Frau]{8,9} [entlässt]{7} – [ausser]{11} [wegen]{12} [Unzucht]{13} – und{14} [eine andere]{16} [heiratet]{15}, [bricht die Ehe]{17}; und{18} [wer]{19} [eine Entlassene]{20} [heiratet]{21}, [bricht die Ehe]{22}.» ~4(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.19.10": "[Die Jünger]{3,4} [sagen]{1} [zu ihm]{2}: «[Wenn]{5} [die Sache]{8,9} [des Mannes]{10,11} [mit]{12} [der Frau]{13,14} [so]{6} [steht]{7}, [ist es]{16} [nicht]{15} [ratsam]{16}, [zu heiraten]{17}.»",
 "MAT.19.11": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: «[Nicht]{5} [alle]{6} [fassen]{7} [dieses]{10} [Wort]{8,9}, [sondern nur]{11} [die, denen]{12} [es gegeben ist]{13}.",
 "MAT.19.12": "[Denn]{2} [es gibt]{1} [Eunuchen]{3}, [die]{4} [vom]{5} [Mutterleib]{6,7} [an]{5} [so]{9} [geboren sind]{8}, und{10} [es gibt]{11} [Eunuchen]{12}, [die]{13} [von]{15} [den Menschen]{16,17} [zu Eunuchen gemacht worden sind]{14}, und{18} [es gibt]{19} [Eunuchen]{20}, [die]{21} [sich selbst]{23} [zu Eunuchen gemacht haben]{22} [um]{24} [des Reiches]{25,26} [der Himmel]{27,28} [willen]{24}. [Wer]{29} [es fassen]{31} [kann]{30}, [der fasse es]{32}!»",
 "MAT.19.13": "[Da]{1} [wurden]{2} [Kinder]{4} [zu ihm]{3} [gebracht]{2}, [damit]{5} [er]{8} [ihnen]{9} [die Hände]{6,7} [auflege]{8} und{10} [bete]{11}; [die Jünger]{12,14} [aber]{13} [fuhren]{15} [sie]{16} [an]{15}.",
 "MAT.19.14": "[Jesus]{1,3} [aber]{2} [sagte]{4}: «[Lasst]{5} [die Kinder]{6,7}, und{8} [hindert]{10} [sie]{11} [nicht]{9}, [zu]{13} [mir]{14} [zu kommen]{12}! [Denn]{16} [solchen]{15,17} [gehört]{18} [das Reich]{19,20} [der Himmel]{21,22}.»",
 "MAT.19.15": "Und{1} [er legte]{2} [ihnen]{5} [die Hände]{3,4} [auf]{2} und [zog]{6} [von dort]{7} [weiter]{6}.",
 "MAT.19.16": "Und{1} [siehe]{2}, [einer]{3} [trat]{4} [an ihn]{5} [heran]{4} und [sagte]{6}: «[Lehrer]{7}, [was]{8} [Gutes]{9} [soll ich tun]{10}, [damit]{11} [ich]{12} [ewiges]{14} [Leben]{13} [erlange]{12}?»",
 "MAT.19.17": "[Er]{1} [aber]{2} [sagte]{3} [zu ihm]{4}: «[Was]{5} [fragst du]{7} [mich]{6} [nach]{8} [dem Guten]{9,10}? [Einer]{11} [ist]{12} [der Gute]{13,14}. [Wenn]{15} [du]{17} [aber]{16} [in]{18} [das Leben]{19,20} [hineingehen]{21} [willst]{17}, [halte]{22} [die Gebote]{23,24}!»",
 "MAT.19.18": "[Er sagt]{1} [zu ihm]{2}: «[Welche]{3}?» [Jesus]{4,6} [aber]{5} [sagte]{7}: «‹[Du sollst]{10} [nicht]{9} [töten]{10}; [du sollst]{12} [nicht]{11} [ehebrechen]{12}; [du sollst]{14} [nicht]{13} [stehlen]{14}; [du sollst]{16} [nicht]{15} [falsch aussagen]{16}; ~8(Der Artikel τό kennzeichnet das Folgende als Zitat; durch die Anführungszeichen wiedergegeben)",
 "MAT.19.19": "[ehre]{1} [Vater]{2,3} und{4} [Mutter]{5,6}; und{7}: [du sollst]{8} [deinen]{11} [Nächsten]{9,10} [lieben]{8} [wie]{12} [dich selbst]{13}›.»",
 "MAT.19.20": "[Der junge Mann]{3,4} [sagt]{1} [zu ihm]{2}: «[Das alles]{5,6} [habe ich gehalten]{7}. [Was]{8} [fehlt mir]{10} [noch]{9}?»",
 "MAT.19.21": "[Jesus]{3,4} [sagte]{1} [zu ihm]{2}: «[Wenn]{5} [du]{6} [vollkommen]{7} [sein]{8} [willst]{6}, [geh]{9}, [verkaufe]{10} [deinen]{11} [Besitz]{12,13} und{14} [gib]{15} es [den Armen]{16}, und{17} [du wirst]{18} [einen Schatz]{19} [in]{20} [den Himmeln]{21} [haben]{18}; und{22} [komm]{23}, [folge]{24} [mir]{25} [nach]{24}!»",
 "MAT.19.22": "[Als]{1} [der junge Mann]{3,4} [aber]{2} [das Wort]{5,6} [hörte]{1}, [ging er]{7} [traurig]{8} [davon]{7}; [denn]{10} [er hatte]{9,11} [viele]{13} [Güter]{12}.",
 "MAT.19.23": "[Jesus]{1,3} [aber]{2} [sagte]{4} zu [seinen]{7} [Jüngern]{5,6}: «[Amen]{8}, [ich sage]{9} [euch]{10}: [Ein Reicher]{12} [wird]{14} [schwer]{13} [in]{15} [das Reich]{16,17} [der Himmel]{18,19} [hineinkommen]{14}. ~11(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.19.24": "[Wiederum]{1} [aber]{2} [sage ich]{3} [euch]{4}: [Es ist]{6} [leichter]{5}, dass [ein Kamel]{7} [durch]{8} [ein Nadelöhr]{9,10} [geht]{11}, [als]{12} dass [ein Reicher]{13} [in]{14} [das Reich]{15,16} [Gottes]{17,18} [hineinkommt]{11}.»",
 "MAT.19.25": "[Als]{1} [die Jünger]{3,4} das [aber]{2} [hörten]{1}, [gerieten sie]{5} [ganz]{6} [ausser sich]{5} und [sagten]{7}: «[Wer]{8} [kann]{10} [dann]{9} [gerettet werden]{11}?»",
 "MAT.19.26": "[Jesus]{3,4} [aber]{2} [sah sie an]{1} und [sagte]{5} [zu ihnen]{6}: «[Bei]{7} [Menschen]{8} [ist]{11} [das]{9} [unmöglich]{10}, [bei]{12} [Gott]{14} [aber]{13} ist [alles]{15} [möglich]{16}.»",
 "MAT.19.27": "[Da]{1} [antwortete]{2} [Petrus]{3,4} und [sagte]{5} [zu ihm]{6}: «[Siehe]{7}, [wir]{8} [haben]{9} [alles]{10} [verlassen]{9} und{11} [sind]{12} [dir]{13} [nachgefolgt]{12}. [Was]{14} [wird]{16} [uns]{17} [also]{15} [zuteil]{16}?»",
 "MAT.19.28": "[Jesus]{1,3} [aber]{2} [sagte]{4} [zu ihnen]{5}: «[Amen]{6}, [ich sage]{7} [euch]{8}: [Ihr]{10}, [die]{11} ihr [mir]{13} [nachgefolgt seid]{12} – [in]{14} [der Neuschöpfung]{15,16}, [wenn]{17} [der Menschensohn]{19-22} sich [auf]{23} [den Thron]{24} [seiner]{26} [Herrlichkeit]{25} [setzt]{18}, [werdet]{27} [auch]{28} [ihr]{29} [auf]{30} [zwölf]{31} [Thronen]{32} [sitzen]{27} und [die zwölf]{34,35} [Stämme]{36} [Israels]{37,38} [richten]{33}. ~9(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.19.29": "Und{1} [jeder]{2}, [der]{3} [Häuser]{5} [oder]{6} [Brüder]{7} [oder]{8} [Schwestern]{9} [oder]{10} [Vater]{11} [oder]{12} [Mutter]{13} [oder]{14} [Frau]{15} [oder]{16} [Kinder]{17} [oder]{18} [Äcker]{19} [um]{20} [meines]{23} [Namens]{21,22} [willen]{20} [verlassen hat]{4}, [wird]{25} [Hundertfaches]{24} [empfangen]{25} und{26} [ewiges]{28} [Leben]{27} [erben]{29}.",
 "MAT.19.30": "[Viele]{1} [Erste]{4} [aber]{2} [werden]{3} [Letzte]{5} [sein]{3}, und{6} [Letzte]{7} [Erste]{8}.»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 18
 "MAT.18.1": "[I]{1} [dere]{2} [Stund]{3,4} [sind]{5} [d Jünger]{6,7} [zum Jesus]{8,9} [härechoo]{5} und [händ gseit]{10}: «[Wer]{11} [isch]{14} [dänn]{12} [de Gröscht]{13} [im]{15,16} [Riich]{17} [vo de Himel]{18,19}?»",
 "MAT.18.2": "Und{1} [er hät]{2} [es Chind]{3} [zu sich grüeft]{2}, [hät]{4} [s]{5} [i]{6} [iri]{8} [Mitti]{7} [gstellt]{4}",
 "MAT.18.3": "und{1} [hät gseit]{2}: [Amen]{3}, [ich säg]{4} [eu]{5}: [Wänn]{6} [ir eu]{8} [nöd]{7} [umwänded]{8} und{9} [wie]{11} [d Chind]{12,13} [wärded]{10}, [chömed ir]{16} [sicher nöd]{14,15} [is]{17,18} [Riich]{19} [vo de Himel]{20,21} [ine]{16}.",
 "MAT.18.4": "[Wer]{1} [sich]{4} [also]{2} [chlii macht]{3} [wie]{5} [das]{8} [Chind]{6,7} [da]{8}, [dä]{9} [isch]{10} [de Gröscht]{11,12} [im]{13,14} [Riich]{15} [vo de Himel]{16,17}.",
 "MAT.18.5": "Und{1} [wer]{2,3} [es]{5} [settigs]{7} [Chind]{6} [i]{8} [mim]{11} [Name]{9,10} [ufnimmt]{4}, [nimmt]{13} [mich]{12} [uf]{13}.",
 "MAT.18.6": "[Wer]{1,3} [aber]{2} [eine]{5} [vo dene]{6,8} [Chliine]{7}, [wo]{9} [a]{11} [mich]{12} [glaubed]{10}, [z Fall bringt]{4}, [für dä]{14} [wär s besser]{13}, [wänn]{15} [ihm]{22} [en grosse Mülistei]{17,18} [um]{19} [de Hals]{20,21} [ghänkt würd]{16} und{23} [er]{24} [i]{25} [de Tüüfi]{26,27} [vom Meer]{28,29} [versänkt würd]{24}.",
 "MAT.18.7": "[Wehe]{1} [de Wält]{2,3} [wäge]{4} [de Fallstrick]{5,6}! [Es isch]{7} [nämli]{8} [unvermeidlich]{7}, dass [d Fallstrick]{10,11} [chömed]{9}; [aber]{12} [wehe]{13} [em Mänsch]{14,15}, wo [de Fallstrick]{18,19} [dur]{16} [ihn]{17} [chunnt]{20}!",
 "MAT.18.8": "[Wänn]{1} [aber]{2} [dini]{5} [Hand]{3,4} [oder]{6} [din]{9} [Fuess]{7,8} [dich]{11} [z Fall bringt]{10}, [hau]{12} [en]{13} [ab]{12} und{14} [rüer]{15} en [vo]{16} [dir]{17} [wäg]{15}! [Es isch besser]{18,20} [für dich]{19}, [verchrüpplet]{25} [oder]{26} [lahm]{27} [is]{22,23} [Läbe]{24} [ine z choo]{21}, [als]{28} [mit]{34} [zwei]{29} [Händ]{30} [oder]{31} [zwei]{32} [Füess]{33} [is]{36,37} [ewig]{39,40} [Füür]{38} [gworfe z wärde]{35}.",
 "MAT.18.9": "Und{1} [wänn]{2} [dis]{5} [Aug]{3,4} [dich]{7} [z Fall bringt]{6}, [riiss]{8} [s]{9} [use]{8} und{10} [rüer]{11} s [vo]{12} [dir]{13} [wäg]{11}! [Es isch besser]{14,16} [für dich]{15}, [mit eim Aug]{17} [is]{18,19} [Läbe]{20} [ine z choo]{21}, [als]{22} [mit]{25} [zwei]{23} [Auge]{24} [i]{27} [d Höll]{28,29} [vom Füür]{30,31} [gworfe z wärde]{26}.",
 "MAT.18.10": "[Passed uf]{1}, [dass ir]{3} [nöd]{2} [eine]{4} [vo dene]{5,7} [Chliine]{6} [verachted]{3}! [Ich säg]{8} [eu]{10} [nämli]{9}: [Iri]{14} [Ängel]{12,13} [i de Himel]{15,16} [gsehnd]{19} [immer]{17,18} [s Gsicht]{20,21} [vo mim Vatter]{22-24} [i de Himel]{25-27}. ~11(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.18.12": "[Was]{1} [meined]{3} [ir]{2}? [Wänn]{4} [en]{6} [Mänsch]{7} [hundert]{8} [Schaf]{9} [hät]{5} und{10} [eis]{12} [vo]{13} [ine]{14} [sich verlauft]{11}, [laat er]{16} [nöd]{15} [d]{17} [nüünenüünzg]{18,19} [uf]{20} [de Bärge]{21,22} [staa]{16} und{23} [gaat]{24} und [suecht]{25} [das]{26}, [wo sich verloffe hät]{27}?",
 "MAT.18.13": "Und{1} [wänn]{2} [er]{4} [s]{5} [würkli]{3} [findt]{4} – [amen]{6}, [ich säg]{7} [eu]{8}: [Er fröit sich]{10} [über]{11} [das]{12} [meh]{13} [als]{14} [über]{15} [di]{16} [nüünenüünzg]{17,18}, [wo]{19} [sich]{21} [nöd]{20} [verloffe händ]{21}. ~9(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.18.14": "[Eso]{1} [isch es]{3} [nöd]{2} [de Wile]{4} [vo]{5} [euem]{8} [Vatter]{6,7} [i de Himel]{9-11}, [dass]{12} [eis]{14} [vo dene]{15,17} [Chliine]{16} [verlore gaat]{13}.",
 "MAT.18.15": "[Wänn]{1} [aber]{2} [din]{8} [Brueder]{6,7} [gäge]{4} [dich]{5} [sündiget]{3}, [gang]{9} und [stell]{10} [en]{11} [zur Red]{10}, [nu]{16} [zwüsche]{12} [dir]{13} [und]{14} [ihm]{15}. [Wänn]{17} [er]{19} uf [dich]{18} [lost]{19}, [häsch]{20} [din]{23} [Brueder]{21,22} [gwunne]{20}.",
 "MAT.18.16": "[Wänn]{1} [er]{4} [aber]{2} [nöd]{3} [lost]{4}, [nimm]{5} [no]{8} [eine]{9} [oder]{10} [zwei]{11} [mit]{6,7}, [damit]{12} [jedi]{20} [Sach]{21} [uf]{13} [d Ussag]{14} [vo zwei]{15} [oder]{17} [drüü]{18} [Züge]{16} [hii]{13} [feschtgstellt wird]{19}.",
 "MAT.18.17": "[Wänn]{1} [er]{3} [aber]{2} [nöd]{3} uf [si]{4} [lost]{3}, [säg s]{5} [de Gmeind]{6,7}; [wänn]{8} [er]{13} [aber]{9} [au]{10} uf [d Gmeind]{11,12} [nöd]{13} [lost]{13}, [söll er]{14} [für dich]{15} [sii]{14} [wie]{16} [de Heid]{17,18} und{19} [de Zöllner]{20,21}.",
 "MAT.18.18": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Alles, wo]{4,5} [ir]{6} [uf]{7} [de Ärde]{8,9} [binded]{6}, [wird]{10} [im]{12} [Himel]{13} [bunde sii]{11}, und{14} [alles, wo]{15,16} [ir]{17} [uf]{18} [de Ärde]{19,20} [löösed]{17}, [wird]{21} [im]{23} [Himel]{24} [glööst sii]{22}.",
 "MAT.18.19": "[Wider]{1}, [amen]{2}, [ich säg]{3} [eu]{4}: [Wänn]{6} [zwei]{7} [vo]{9} [eu]{10} [uf]{11} [de Ärde]{12,13} [sich einig wärded]{8} [über]{14} [irgend e]{15} [Sach]{16}, [wo]{17,18} [si]{19} [drum bitted]{19}, so [wird]{20} [ine]{21} das [vo]{22} [mim Vatter]{23-25} [i de Himel]{26-28} [gää]{20}. ~5(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.18.20": "[Wo]{1} [nämli]{2} [zwei]{4} [oder]{5} [drüü]{6} [i]{8} [mim]{9,10} [Name]{11} [versammlet]{7} [sind]{3}, [dört]{12} [bin ich]{13} [mitten]{14,15} [under ine]{16}.",
 "MAT.18.21": "[Dänn]{1} [isch]{2} [de Petrus]{4,5} [zu ihm]{3} [härechoo]{2} und [hät gseit]{6}: «[Herr]{7}, [wie mängisch]{8} [sündiget]{9} [min]{14} [Brueder]{12,13} [gäge]{10} [mich]{11}, und{15} [ich]{16} [vergib]{16} [em]{17}? [Bis]{18} [sibe Mal]{19}?»",
 "MAT.18.22": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: [Ich säg]{6} [dir]{7} [nöd]{5}: [bis]{8} [sibe Mal]{9}, [sondern]{10} [bis]{11} [sibenesibezg Mal]{12,13}.",
 "MAT.18.23": "[Drum]{1,2} [isch]{3} [s Riich]{4,5} [vo de Himel]{6,7} [wie]{3} [en König]{9}, [wo]{10} [mit]{14} [sine]{17} [Chnächt]{15,16} [hät wele]{11} [abrächne]{12,13}. ~8(ἀνθρώπῳ «emne Mänsch» vor βασιλεῖ «König» isch semitischi Uusdrucksart; i «en König» enthalte)",
 "MAT.18.24": "[Wo]{1} [er]{3} [aber]{2} [aagfange hät]{1}, [abzrächne]{4}, [isch]{5} [eine]{7} [zu ihm]{6} [brocht worde]{5}, [wo]{8} [zäätuusig]{9} [Talänt]{10} [gschuldet hät]{8}.",
 "MAT.18.25": "Wil [er]{4} [aber]{3} [nöd]{1} [hät chöne]{2} [zale]{5}, [hät]{6} [de Herr]{8,9} [befole]{6}, [en]{7} [z verchaufe]{10}, [mitsamt]{11} [sinere Frau]{12,13} und{14} [de Chind]{15,16} und{17} [allem]{18}, [wo]{19} [er hät]{20}, und{21} [eso d Schuld z zale]{22}.",
 "MAT.18.26": "[De Chnächt]{3,4} [isch]{1} [drum]{2} [uf de Bode gfalle]{1}, [hät sich]{5} [vor ihm]{6} [nidergworfe]{5} und [hät gseit]{7}: «[Häb Geduld]{8} [mit]{9} [mir]{10}, und{11} [ich zal]{13} [dir]{14} [alles]{12} [zrugg]{13}!»",
 "MAT.18.27": "[De Herr]{3,4} [vo däm]{5,7} [Chnächt]{6} [aber]{2} [hät Erbarme gha]{1}, [hät]{8} [en]{9} [freiglaa]{8} und{10} [hät]{13} [ihm]{14} [s Darlehe]{11,12} [erlaa]{13}.",
 "MAT.18.28": "[Dä]{3,5} [Chnächt]{4} [aber]{2} [isch usegange]{1} und [hät]{6} [eine]{7} [vo sine]{8,10} [Mitchnächt]{9} [gfunde]{6}, [wo]{11} [ihm]{13} [hundert]{14} [Denar]{15} [gschuldet hät]{12}; und{16} [er hät]{17} [en]{18} [packt]{17}, [hät en gwürgt]{19} und [gseit]{20}: «[Zal]{21}, [wänn]{22} [du]{24} [öppis]{23} [schuldisch]{24}!»",
 "MAT.18.29": "[Sin]{5} [Mitchnächt]{3,4} [isch]{1} [drum]{2} [nidergfalle]{1}, [hät]{6} [en]{7} [aagfleht]{6} und [gseit]{8}: «[Häb Geduld]{9} [mit]{10} [mir]{11}, und{12} [ich zal]{13} [dir]{14} s [zrugg]{13}!»",
 "MAT.18.30": "[Er]{1} [aber]{2} [hät]{4} [nöd]{3} [wele]{4}, [sondern]{5} [isch hiigange]{6} und [hät]{7} [en]{8} [is]{9} [Gfängnis]{10} [gworfe]{7}, [bis]{11,12} [er]{13} [d Schuld]{14,15} [zalt hät]{13}.",
 "MAT.18.31": "[Wo]{1} [sini]{5} [Mitchnächt]{3,4} [also]{2} [gseh händ]{1}, [was]{6} [passiert isch]{7}, [sind si]{8} [arg]{9} [truurig worde]{8}, und{10} [si sind gange]{11} und [händ]{12} [irem]{15} [Herr]{13,14} [alles]{16} [verzellt]{12}, [was]{17} [passiert isch]{18}.",
 "MAT.18.32": "[Dänn]{1} [hät]{2} [en]{3} [sin]{6} [Herr]{4,5} [zu sich grüeft]{2} und [seit]{7} [zu ihm]{8}: «Du [böse]{10} [Chnächt]{9}! [Die]{12,14} [ganz]{11} [Schuld]{13} [han ich]{15} [dir]{16} [erlaa]{15}, [wil]{17} [du]{18} [mich]{19} [aagfleht häsch]{18}.",
 "MAT.18.33": "[Hettsch]{2} [du]{4} [nöd]{1} [au]{3} mit [dim]{8} [Mitchnächt]{6,7} [müese]{2} [Erbarme ha]{5}, [wie]{9} [au ich]{10} mit [dir]{11} [Erbarme gha han]{12}?»",
 "MAT.18.34": "Und{1} [sin]{5} [Herr]{3,4} [isch zornig worde]{2} und [hät]{6} [en]{7} [de]{8} [Folterchnächt]{9} [usgliferet]{6}, [bis]{10,11} [er]{12} [di]{14} [ganz]{13} [Schuld]{15} [zalt hät]{12}.",
 "MAT.18.35": "[Eso]{1} [macht s]{8} [au]{2} [min]{5} [himmlisch]{6,7} [Vatter]{3,4} [mit eu]{9}, [wänn]{10} [ir]{12} [nöd]{11} [vo]{17} [Härze]{18-20} [vergänd]{12}, [jede]{13} [sim]{16} [Brueder]{14,15}.",
 # ------------------------------------------------------------ Kapitel 19
 "MAT.19.1": "Und{1} [es isch gscheh]{2}: [Wo]{3} [de Jesus]{5,6} [mit]{4} [dene]{9} [Wort]{7,8} [fertig gsii isch]{4}, [isch er]{10} [vo]{11} [Galiläa]{12,13} [ufbroche]{10} und{14} [is]{16,17} [Gebiet]{18} [vo Judäa]{19,20} [änet]{21} [em Jordan]{22,23} [choo]{15}.",
 "MAT.19.2": "Und{1} [vil]{5} [Lüüt]{4} [sind]{2} [ihm]{3} [nachegfolget]{2}, und{6} [er hät]{7} [si]{8} [dört]{9} [gheilt]{7}.",
 "MAT.19.3": "Und{1} [Pharisäer]{4} [sind]{2} [zu ihm]{3} [härechoo]{2}, [für]{5} [en]{6} [uf d Prob z stelle]{5}, und{7} [händ gseit]{8}: «[Dörf]{10} [en Maa]{11} [sini]{15} [Frau]{13,14} [us]{16} [jedem]{17} [Grund]{18} [entlaa]{12}?» ~9(εἰ leitet di diräkt Frag ii; nöd eigens widergää)",
 "MAT.19.4": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: «[Händ ir]{6} [nöd]{5} [gläse]{6}, [dass]{7} [de Schöpfer]{8,9} [si]{16} [vo Aafang aa]{10,11} ‹[männlich]{12} und{13} [wiiblich]{14} [gmacht hät]{15}›",
 "MAT.19.5": "und{1} [gseit hät]{2}: ‹[Drum]{3,4} [wird]{5} [en Mänsch]{6} [Vatter]{7,8} und{9} [Mueter]{10,11} [verlaa]{5} und{12} [a]{14} [sinere]{16} [Frau]{15} [hange]{13}, und{17} [di zwei]{19,20} [wärded]{18} [ei]{21,23} [Fleisch]{22} [sii]{18}›?",
 "MAT.19.6": "[So]{1} [sind si]{3} [nüme]{2} [zwei]{4}, [sondern]{5} [ei]{7} [Fleisch]{6}. [Was]{8} [also]{9} [Gott]{10,11} [zämegfüegt hät]{12}, [söll]{15} [de Mänsch]{13} [nöd]{14} [trenne]{15}.»",
 "MAT.19.7": "[Si säged]{1} [zu ihm]{2}: «[Werum]{3} [hät]{6} [de Mose]{5} [dänn]{4} [befole]{6}, [en Scheidigsbrief]{8,9} [z gää]{7} und{10} [si]{12} [z entlaa]{11}?»",
 "MAT.19.8": "[Er seit]{1} [zu ine]{2}: «[De Mose]{4} [hät]{9} [eu]{10} [wäge]{5} [euem]{8} [härte Härz]{6,7} [erlaubt]{9}, [eui]{14} [Fraue]{12,13} [z entlaa]{11}; [vo Aafang aa]{15,16} [aber]{17} [isch es]{19} [nöd]{18} [eso]{20} [gsii]{19}. ~3(ὅτι leitet di diräkt Red ii)",
 "MAT.19.9": "[Ich säg]{1} [eu]{3} [aber]{2}: [Wer]{5,6} [sini]{10} [Frau]{8,9} [entlaat]{7} – [usser]{11} [wäge]{12} [Unzucht]{13} – und{14} [en anderi]{16} [hüratet]{15}, [bricht d Ee]{17}; und{18} [wer]{19} [eini]{20} [hüratet]{21}, [wo entlaa worde isch]{20}, [bricht d Ee]{22}.» ~4(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.19.10": "[D Jünger]{3,4} [säged]{1} [zu ihm]{2}: «[Wänn]{5} [d Sach]{8,9} [vom Maa]{10,11} [mit]{12} [de Frau]{13,14} [eso]{6} [staat]{7}, [isch es]{16} [nöd]{15} [ratsam]{16}, [z hürate]{17}.»",
 "MAT.19.11": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: «[Nöd]{5} [alli]{6} [chönd]{7} [das]{10} [Wort]{8,9} [fasse]{7}, [sondern nu]{11} [die, wo]{12} s [ene gää isch]{13}.",
 "MAT.19.12": "[Es git]{1} [nämli]{2} [Eunuche]{3}, [wo]{4} [vo]{5} [Muetterliib]{6,7} [aa]{5} [eso]{9} [gebore sind]{8}, und{10} [es git]{11} [Eunuche]{12}, [wo]{13} [vo]{15} [de Mänsche]{16,17} [zu Eunuche gmacht worde sind]{14}, und{18} [es git]{19} [Eunuche]{20}, [wo]{21} [sich sälber]{23} [zu Eunuche gmacht händ]{22} [wäge]{24} [em Riich]{25,26} [vo de Himel]{27,28}. [Wer]{29} [s fasse]{31} [cha]{30}, [dä söll s fasse]{32}!»",
 "MAT.19.13": "[Dänn]{1} [sind]{2} [Chind]{4} [zu ihm]{3} [brocht worde]{2}, [damit]{5} [er]{8} [ine]{9} [d Händ]{6,7} [uflegi]{8} und{10} [bäti]{11}; [d Jünger]{12,14} [aber]{13} [händ]{15} [si]{16} [aagfahre]{15}.",
 "MAT.19.14": "[De Jesus]{1,3} [aber]{2} [hät gseit]{4}: «[Lönd]{5} [d Chind]{6,7}, und{8} [hindered]{10} [si]{11} [nöd]{9} dra, [zu]{13} [mir]{14} [z choo]{12}! [Settige]{15,17} [ghört]{18} [nämli]{16} [s Riich]{19,20} [vo de Himel]{21,22}.»",
 "MAT.19.15": "Und{1} [er hät]{2} [ine]{5} [d Händ]{3,4} [ufgleit]{2} und [isch]{6} [vo dört]{7} [wiitergange]{6}.",
 "MAT.19.16": "Und{1} [lueg]{2}, [eine]{3} [isch]{4} [zu ihm]{5} [härechoo]{4} und [hät gseit]{6}: «[Lehrer]{7}, [was]{8} [Guets]{9} [söll ich mache]{10}, [damit]{11} [ich]{12} [ewigs]{14} [Läbe]{13} [überchume]{12}?»",
 "MAT.19.17": "[Er]{1} [aber]{2} [hät]{3} [zu ihm]{4} [gseit]{3}: «[Werum]{5} [frögsch du]{7} [mich]{6} [nach]{8} [em Guete]{9,10}? [Eine]{11} [isch]{12} [de Guet]{13,14}. [Wänn]{15} [du]{17} [aber]{16} [is]{18,19} [Läbe]{20} [ine choo]{21} [wottsch]{17}, [halt]{22} [d Gebot]{23,24}!»",
 "MAT.19.18": "[Er seit]{1} [zu ihm]{2}: «[Weli]{3}?» [De Jesus]{4,6} [aber]{5} [hät gseit]{7}: «‹[Du söllsch]{10} [nöd]{9} [töte]{10}; [du söllsch]{12} [nöd]{11} [d Ee breche]{12}; [du söllsch]{14} [nöd]{13} [stäle]{14}; [du söllsch]{16} [nöd]{15} [falsch uussäge]{16}; ~8(De Artikel τό kännzeichnet das, wo folgt, als Zitat; mit de Aafüerigszeiche widergää)",
 "MAT.19.19": "[ehr]{1} [Vatter]{2,3} und{4} [Mueter]{5,6}; und{7}: [du söllsch]{8} [din]{11} [Nächschte]{9,10} [liebe]{8} [wie]{12} [di sälber]{13}›.»",
 "MAT.19.20": "[De jung Maa]{3,4} [seit]{1} [zu ihm]{2}: «[Das alles]{5,6} [han ich ghalte]{7}. [Was]{8} [fehlt mer]{10} [no]{9}?»",
 "MAT.19.21": "[De Jesus]{3,4} [hät]{1} [zu ihm]{2} [gseit]{1}: «[Wänn]{5} [du]{6} [vollkomme]{7} [sii]{8} [wottsch]{6}, [gang]{9}, [verchauf]{10}, [was]{12} [du]{11} [häsch]{13}, und{14} [gib s]{15} [de Arme]{16}, und{17} [du wirsch]{18} [en Schatz]{19} [i]{20} [de Himel]{21} [ha]{18}; und{22} [chumm]{23}, [folg]{24} [mir]{25} [nache]{24}!»",
 "MAT.19.22": "[Wo]{1} [de jung Maa]{3,4} [aber]{2} [das Wort]{5,6} [ghört hät]{1}, [isch er]{7} [truurig]{8} [devo gange]{7}; [er hät]{9,11} [nämli]{10} [vil]{13} [Bsitz]{12} [gha]{9,11}.",
 "MAT.19.23": "[De Jesus]{1,3} [aber]{2} [hät]{4} zu [sine]{7} [Jünger]{5,6} [gseit]{4}: «[Amen]{8}, [ich säg]{9} [eu]{10}: [En Riiche]{12} [chunnt]{14} [schwär]{13} [is]{15,16} [Riich]{17} [vo de Himel]{18,19} [ine]{14}. ~11(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.19.24": "[Wider]{1} [aber]{2} [säg ich]{3} [eu]{4}: [Es isch]{6} [liechter]{5}, dass [es Kamel]{7} [dur]{8} [es Nadelööhr]{9,10} [gaat]{11}, [als]{12} dass [en Riiche]{13} [is]{14,15} [Riich]{16} [vo Gott]{17,18} [ine chunnt]{11}.»",
 "MAT.19.25": "[Wo]{1} [d Jünger]{3,4} das [aber]{2} [ghört händ]{1}, [sind si]{5} [ganz]{6} [usser sich gsii]{5} und [händ gseit]{7}: «[Wer]{8} [cha]{10} [dänn]{9} [grettet wärde]{11}?»",
 "MAT.19.26": "[De Jesus]{3,4} [aber]{2} [hät si aagluegt]{1} und [hät]{5} [zu ine]{6} [gseit]{5}: «[Bi]{7} [Mänsche]{8} [isch]{11} [das]{9} [unmöglich]{10}, [bi]{12} [Gott]{14} [aber]{13} isch [alles]{15} [möglich]{16}.»",
 "MAT.19.27": "[Dänn]{1} [hät]{2} [de Petrus]{3,4} [gantwortet]{2} und [zu ihm]{6} [gseit]{5}: «[Lueg]{7}, [mir]{8} [händ]{9} [alles]{10} [verlaa]{9} und{11} [sind]{12} [dir]{13} [nachegfolget]{12}. [Was]{14} [überchömed mir]{16,17} [also]{15} defür?»",
 "MAT.19.28": "[De Jesus]{1,3} [aber]{2} [hät]{4} [zu ine]{5} [gseit]{4}: «[Amen]{6}, [ich säg]{7} [eu]{8}: [Ir]{10}, [wo]{11} [mir]{13} [nachegfolget sind]{12} – [i]{14} [de Neuschöpfig]{15,16}, [wänn]{17} [de Mänschesohn]{19-22} sich [uf]{23} [de Throon]{24} [vo sinere]{26} [Herrlichkeit]{25} [setzt]{18}, [wärded]{27} [au]{28} [ir]{29} [uf]{30} [zwölf]{31} [Throon]{32} [sitze]{27} und [di zwölf]{34,35} [Stämm]{36} [vo Israel]{37,38} [richte]{33}. ~9(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.19.29": "Und{1} [jede]{2}, [wo]{3} [Hüüser]{5} [oder]{6} [Brüeder]{7} [oder]{8} [Schwöschtere]{9} [oder]{10} [Vatter]{11} [oder]{12} [Mueter]{13} [oder]{14} [Frau]{15} [oder]{16} [Chind]{17} [oder]{18} [Äcker]{19} [wäge]{20} [mim]{23} [Name]{21,22} [verlaa hät]{4}, [wird]{25} [hundertfach]{24} [übercho]{25} und{26} [ewigs]{28} [Läbe]{27} [erbe]{29}.",
 "MAT.19.30": "[Vil]{1} [Erschti]{4} [aber]{2} [wärded]{3} [Letschti]{5} [sii]{3}, und{6} [Letschti]{7} [Erschti]{8}.»",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 # ------------------------------------------------------------ Kapitel 18
 ("MAT.18.1", "traten", "literal", "προσῆλθον", "kamen herzu", ["kamen"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: προσέρχομαι «herantreten» (Mundart «härechoo»); ebenso [[MAT.18.21]], [[MAT.19.3]], [[MAT.19.16]]."),
 ("MAT.18.1", "der Grösste", "interpretive", "μείζων", "der Grössere", None,
  "Die Steigerungsform steht im Griechischen des Neuen Testaments oft für den Superlativ. Ebenso [[MAT.18.4]]."),
 ("MAT.18.1", "im Reich der Himmel", "literal", "ἐν τῇ βασιλείᾳ τῶν οὐρανῶν", None, ["im Himmelreich", "in der Königsherrschaft der Himmel"],
  "Grundentscheid für das ganze Matthäusevangelium: ἡ βασιλεία τῶν οὐρανῶν «das Reich der Himmel», mit der Mehrzahl des Griechischen. Matthäus gebraucht die Wendung nach den SBLGNT-Tokens 32-mal, «Reich Gottes» nur 4-mal ([[MAT.12.28]], [[MAT.19.24]], [[MAT.21.31]], [[MAT.21.43]]). Viele sehen darin jüdische Scheu, den Gottesnamen auszusprechen; der Sache nach meinen beide Wendungen dasselbe. βασιλεία heisst auch «Königsherrschaft»: Gemeint ist Gottes Herrschen, nicht in erster Linie ein Gebiet."),
 ("MAT.18.3", "ihr euch nicht umwendet", "literal", "μὴ στραφῆτε", None, ["umkehrt", "euch ändert"],
  "στρέφω «sich umwenden». «Umkehren» ist in dieser Übersetzung für μετανοέω reserviert ([[MAT.3.2]], [[MAT.4.17]]); damit die Wörter unterscheidbar bleiben, steht hier «sich umwenden». Gemeint ist eine Änderung der Richtung."),
 ("MAT.18.3", "gewiss nicht", "literal", "οὐ μὴ", None, ["auf keinen Fall"],
  "Doppelte Verneinung mit Konjunktiv: die stärkste Form der Verneinung."),
 ("MAT.18.4", "klein macht", "adapted", "ταπεινώσει ἑαυτὸν", "sich erniedrigen wird", ["sich erniedrigt", "sich demütigt"],
  "ταπεινόω heisst «niedrig machen». Das Futur steht im verallgemeinernden Relativsatz. Das Kind ist Bild für eine niedrige Stellung; ob zugleich an eine kindliche Haltung gedacht ist, ist umstritten. «Klein machen» hält die Verbindung zu «diese Kleinen» ([[MAT.18.6]]) sichtbar."),
 ("MAT.18.5", "aufnimmt", "literal", "δέξηται", None, ["empfängt"], None),
 ("MAT.18.6", "Kleinen", "interpretive", "τῶν μικρῶν τούτων", None, ["Geringen"],
  "Ob mit «diesen Kleinen» Kinder gemeint sind oder Jünger, die gering geachtet werden, ist offen; der Zusatz «die an mich glauben» spricht für Glaubende allgemein. Ebenso [[MAT.18.10]], [[MAT.18.14]]."),
 ("MAT.18.6", "zu Fall bringt", "interpretive", "σκανδαλίσῃ", None, ["zum Straucheln bringt", "vom Glauben abbringt", "Anstoss gibt"],
  "Einheitliche Wiedergabe für das Matthäusevangelium, wie bei Markus ([[MRK.9.42]]): σκανδαλίζω aktiv «zu Fall bringen», hier im Glauben (passiv gegenüber einer Person «Anstoss nehmen an», sonst «zu Fall kommen»); σκάνδαλον «Fallstrick» ([[MAT.18.7]]). Ebenso [[MAT.18.8]]–[[MAT.18.9]]."),
 ("MAT.18.6", "für den wäre es besser", "adapted", "συμφέρει αὐτῷ", "es nützt ihm", ["es ist besser für ihn"],
  "Präsens im Griechischen; der Vergleich ist im Deutschen mit dem Konjunktiv deutlicher."),
 ("MAT.18.6", "ein grosser Mühlstein", "interpretive", "μύλος ὀνικὸς", "ein Esels-Mühlstein", ["ein Mühlstein"],
  "Wie bei Markus ([[MRK.9.42]]): der schwere Läuferstein einer von einem Esel gedrehten Mühle, im Unterschied zur kleinen Handmühle."),
 ("MAT.18.7", "der Fallstricke", "interpretive", "τῶν σκανδάλων", None, ["der Ärgernisse", "der Verführungen", "der Anlässe zum Fall"],
  "σκάνδαλον ist ursprünglich das Stellholz einer Falle, dann alles, was zu Fall bringt. «Fallstrick» hält das Bild und die Verbindung zu «zu Fall bringen» fest."),
 ("MAT.18.8", "hau ihn ab", "literal", "ἔκκοψον αὐτὸν", None, ["hau sie ab"],
  "αὐτόν ist männliche Einzahl und bezieht sich grammatisch auf den zuletzt genannten Fuss, sachlich auf jedes der beiden Glieder. RP liest die Mehrzahl (siehe Alternativen)."),
 ("MAT.18.8", "verstümmelt", "literal", "κυλλὸν", None, ["verkrüppelt"], None),
 ("MAT.18.8", "das ewige Feuer", "literal", "τὸ πῦρ τὸ αἰώνιον", None, None,
  "αἰώνιος gehört zu αἰών «Weltzeit»; vgl. [[MAT.25.41]]."),
 ("MAT.18.9", "die Hölle des Feuers", "traditional", "τὴν γέενναν τοῦ πυρός", None, ["die Feuerhölle", "den Ort des Gerichts"],
  "Wie bei Markus ([[MRK.9.43]]): γέεννα gibt hebräisch gê hinnōm wieder, das Hinnomtal bei Jerusalem, das zum Bild für den Ort des endzeitlichen Gerichts wurde. «Hölle» folgt der vertrauten Wiedergabe, trägt aber spätere Vorstellungen mit."),
 ("MAT.18.10", "Ihre Engel", "literal", "οἱ ἄγγελοι αὐτῶν", None, None,
  "Die Vorstellung, dass Menschen Engel bei Gott haben, ist im Judentum der Zeit belegt (vgl. [[PSA.91.11]]). «Das Angesicht sehen» heisst, unmittelbar vor Gott zu stehen, wie Diener vor dem König."),
 ("MAT.18.10", "in den Himmeln", "literal", "ἐν οὐρανοῖς", None, ["im Himmel"],
  "Grundentscheid: Die Mehrzahl ἐν οὐρανοῖς ist mit «in den Himmeln» wiedergegeben, wie im Vaterunser ([[MAT.6.9]]); die Einzahl ἐν οὐρανῷ mit «im Himmel» ([[MAT.18.18]])."),
 ("MAT.18.12", "auf den Bergen lassen", "interpretive", "ἐπὶ τὰ ὄρη", None, ["… lassen und auf die Berge gehen"],
  "ἐπὶ τὰ ὄρη kann zu «lassen» gehören (so hier) oder zu «hingehen». Der Satz ist eine Frage, die Zustimmung erwartet (οὐχί)."),
 ("MAT.18.12", "das verirrte", "literal", "τὸ πλανώμενον", "das sich verirrende", None,
  "πλανάω «sich verirren», auch «in die Irre gehen»; dasselbe Wort steht für Verführung ([[MAT.24.4]]). Lukas erzählt das Gleichnis vom «verlorenen» Schaf ([[LUK.15.4]])."),
 ("MAT.18.13", "es ihm gelingt", "adapted", "γένηται", "es geschieht", None,
  "Das «wenn» lässt offen, ob der Mensch das Schaf findet."),
 ("MAT.18.14", "der Wille eures Vaters", "adapted", "θέλημα ἔμπροσθεν τοῦ πατρὸς ὑμῶν", "Wille vor eurem Vater", None,
  "ἔμπροσθεν «vor» ist eine ehrfürchtige Umschreibung, die Gott nicht direkt zum Subjekt macht."),
 ("MAT.18.15", "Bruder", "interpretive", "ὁ ἀδελφός σου", None, ["Mitchrist", "Bruder oder Schwester"],
  "ἀδελφός meint hier das Glied der Gemeinschaft ([[MAT.23.8]]); die Regel gilt der Sache nach auch für Schwestern. Die Übersetzung bleibt beim Wortlaut. Ebenso [[MAT.18.21]], [[MAT.18.35]]."),
 ("MAT.18.15", "weise ihn zurecht", "literal", "ἔλεγξον αὐτὸν", None, ["stell ihn zur Rede", "überführe ihn"],
  "ἐλέγχω heisst «aufdecken, überführen, zurechtweisen»; vgl. [[LEV.19.17]]."),
 ("MAT.18.15", "gewonnen", "literal", "ἐκέρδησας", None, ["zurückgewonnen"], None),
 ("MAT.18.16", "auf die Aussage von zwei oder drei Zeugen hin", "adapted", "ἐπὶ στόματος δύο μαρτύρων ἢ τριῶν", "auf den Mund von zwei Zeugen oder drei", None,
  "Aufnahme von [[DEU.19.15]]. «Mund» steht für die Aussage."),
 ("MAT.18.16", "jede Sache", "literal", "πᾶν ῥῆμα", "jedes Wort", None,
  "ῥῆμα «Wort» steht nach hebräischem Sprachgebrauch auch für «Sache, Angelegenheit»."),
 ("MAT.18.17", "der Gemeinde", "interpretive", "τῇ ἐκκλησίᾳ", None, ["der Versammlung", "der Kirche"],
  "Grundentscheid: ἐκκλησία «Gemeinde». In den Evangelien steht das Wort nur bei Matthäus ([[MAT.16.18]], [[MAT.18.17]]). Hier ist die versammelte örtliche Gemeinschaft gemeint; «Kirche» würde spätere Strukturen eintragen."),
 ("MAT.18.17", "wie der Heide und der Zöllner", "literal", "ὥσπερ ὁ ἐθνικὸς καὶ ὁ τελώνης", None, ["wie jemand aus den Völkern und ein Zöllner"],
  "ἐθνικός ist, wer nicht zum jüdischen Volk gehört; τελώνης, wer Zölle für die Herrschenden einzog. Beide galten vielen als Aussenstehende. Ob der Satz den Ausschluss aus der Gemeinschaft meint oder daran erinnert, dass Jesus sich gerade Zöllnern zuwendet ([[MAT.9.10]]–[[MAT.9.11]], [[MAT.11.19]]), wird verschieden gedeutet."),
 ("MAT.18.18", "gebunden sein", "interpretive", "ἔσται δεδεμένα", None, ["gebunden werden"],
  "Die Verbindung von Futur und Perfekt kann heissen: Was die Gemeinde entscheidet, wird im Himmel bestätigt, oder: sie entscheidet, was im Himmel schon entschieden ist. «Binden» und «lösen» sind Ausdrücke der jüdischen Lehrentscheidung (verbieten, erlauben) und der Disziplin (ausschliessen, wieder aufnehmen). Vgl. [[MAT.16.19]], dort an Petrus gerichtet. Ebenso «gelöst sein»."),
 ("MAT.18.19", "einig werden", "literal", "συμφωνήσωσιν", None, ["übereinstimmen"], None),
 ("MAT.18.20", "in meinem Namen", "adapted", "εἰς τὸ ἐμὸν ὄνομα", "auf meinen Namen hin", None,
  "εἰς mit «Namen» bezeichnet die Zugehörigkeit oder den Bezug: versammelt im Blick auf Jesus."),
 ("MAT.18.20", "mitten unter ihnen", "literal", "ἐν μέσῳ αὐτῶν", None, None,
  "Vgl. die Zusage «Gott mit uns» ([[MAT.1.23]]) und [[MAT.28.20]]."),
 ("MAT.18.21", "Herr", "interpretive", "Κύριε", None, ["Meister"],
  "κύριε ist eine respektvolle Anrede, kann aber auch die Anrede an Gott anklingen lassen. Im Gleichnis heisst derselbe Ausdruck der Herr der Knechte."),
 ("MAT.18.21", "vergeben", "literal", "ἀφήσω", None, ["erlassen"],
  "Grundentscheid: ἀφίημι im Sinn der Schuld «vergeben», wie im Vaterunser ([[MAT.6.12]], [[MAT.6.14]]–[[MAT.6.15]]). Im Gleichnis geht es um Geldschuld; dort steht «erlassen» ([[MAT.18.27]], [[MAT.18.32]]), das griechische Wort ist dasselbe."),
 ("MAT.18.22", "siebenundsiebzigmal", "interpretive", "ἑβδομηκοντάκις ἑπτά", None, ["siebzigmal siebenmal"],
  "Die Form kann «77-mal» oder «70-mal 7» heissen. In der griechischen Fassung von [[GEN.4.24]] (Lamech) steht dieselbe Form für 77. Gemeint ist in beiden Fällen eine Zahl, die das Zählen aufhebt."),
 ("MAT.18.23", "gleicht", "adapted", "ὡμοιώθη", "ist gleich geworden", ["ist zu vergleichen mit"],
  "Aorist Passiv; die Einleitungsformel der Gleichnisse bei Matthäus ([[MAT.13.24]], [[MAT.22.2]]). Ein Gleichnis vergleicht mit dem ganzen Vorgang, nicht nur mit der genannten Person."),
 ("MAT.18.23", "einem König", "adapted", "ἀνθρώπῳ βασιλεῖ", "einem Menschen, einem König", None,
  "Semitisierende Ausdrucksweise; «Mensch» wird nicht eigens wiedergegeben."),
 ("MAT.18.23", "Knechten", "interpretive", "δούλων", None, ["Sklaven", "Dienern", "Beamten"],
  "δοῦλος ist der unfreie Diener, wie bei Markus «Knecht». Bei einem König können hohe Beamte gemeint sein, die über grosse Summen verfügen."),
 ("MAT.18.23", "abrechnen", "adapted", "συνᾶραι λόγον", "Rechnung zusammenstellen", None, None),
 ("MAT.18.24", "zehntausend Talente", "literal", "μυρίων ταλάντων", None, ["unzählige Talente"],
  "Ein Talent entsprach etwa 6000 Denaren, ein Denar dem Tageslohn eines Arbeiters ([[MAT.20.2]]). μύριοι «zehntausend» ist zugleich die höchste griechische Zahlbezeichnung; die Summe ist bewusst unvorstellbar."),
 ("MAT.18.25", "was er hat", "literal", "ὅσα ἔχει", None, ["was er hatte"],
  "Präsens wie im SBLGNT; RP liest die Vergangenheit."),
 ("MAT.18.26", "warf sich vor ihm nieder", "interpretive", "προσεκύνει αὐτῷ", None, ["huldigte ihm", "betete ihn an"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: προσκυνέω vor Menschen und vor Jesus «sich niederwerfen», mit Gott als Empfänger «anbeten». Hier die Geste der Unterwerfung vor einem Herrscher; dasselbe Wort steht für die Anbetung. Das vorangehende πεσών ist mit «fiel zu Boden» wiedergegeben, damit «nieder» nicht doppelt steht."),
 ("MAT.18.26", "Hab Geduld", "literal", "Μακροθύμησον", None, ["Sei langmütig"], None),
 ("MAT.18.27", "hatte Erbarmen", "literal", "σπλαγχνισθεὶς", None, ["wurde von Mitleid ergriffen"],
  "σπλαγχνίζομαι, von σπλάγχνα «Eingeweide»: ein Erbarmen, das im Innersten bewegt. ἐλεέω in [[MAT.18.33]] ist mit «sich erbarmen» wiedergegeben."),
 ("MAT.18.27", "erliess", "adapted", "ἀφῆκεν", None, ["vergab"],
  "Dasselbe Verb wie «vergeben» in [[MAT.18.21]] und [[MAT.18.35]]; bei Geldschuld ist im Deutschen «erlassen» üblich."),
 ("MAT.18.27", "das Darlehen", "literal", "τὸ δάνειον", None, ["die Schuld"],
  "Der Herr behandelt die Schuld wie ein Darlehen."),
 ("MAT.18.28", "hundert Denare", "literal", "ἑκατὸν δηνάρια", None, None,
  "Etwa hundert Tageslöhne ([[MAT.20.2]]), ein Bruchteil der zehntausend Talente."),
 ("MAT.18.28", "Mitknechte", "literal", "τῶν συνδούλων", None, ["Mitsklaven"], None),
 ("MAT.18.32", "böser", "literal", "πονηρέ", None, ["schlechter"], None),
 ("MAT.18.34", "Folterknechten", "literal", "τοῖς βασανισταῖς", None, ["Peinigern", "Kerkermeistern"],
  "βασανιστής ist, wer peinlich befragt oder quält; im Schuldgefängnis sollte so die Zahlung durch Angehörige erzwungen werden."),
 ("MAT.18.34", "lieferte", "literal", "παρέδωκεν", None, ["übergab"],
  "παραδίδωμι «ausliefern» wie bei Markus; dasselbe Verb steht für die Auslieferung Jesu ([[MAT.17.22]])."),
 ("MAT.18.35", "himmlischer Vater", "literal", "ὁ πατήρ μου ὁ οὐράνιος", None, None,
  "Grundentscheid: ὁ οὐράνιος «himmlisch», wie in [[MAT.6.14]]."),
 ("MAT.18.35", "von Herzen", "adapted", "ἀπὸ τῶν καρδιῶν ὑμῶν", "von euren Herzen", None, None),
 # ------------------------------------------------------------ Kapitel 19
 ("MAT.19.1", "Und es geschah", "literal", "Καὶ ἐγένετο ὅτε ἐτέλεσεν", None, None,
  "Diese Formel schliesst bei Matthäus die fünf grossen Reden ab ([[MAT.7.28]], [[MAT.11.1]], [[MAT.13.53]], [[MAT.19.1]], [[MAT.26.1]]); hier die Rede von Kapitel 18."),
 ("MAT.19.1", "in das Gebiet von Judäa jenseits des Jordan", "interpretive", "εἰς τὰ ὅρια τῆς Ἰουδαίας πέραν τοῦ Ἰορδάνου", None, ["in das Gebiet von Judäa, und zwar jenseits des Jordan"],
  "Die Wendung ist geographisch ungenau: Judäa liegt westlich des Jordan. Gemeint ist wohl der Weg nach Judäa über das Ostjordanland (Peräa); [[MRK.10.1]] nennt Judäa und das Ostjordanland nebeneinander."),
 ("MAT.19.3", "auf die Probe zu stellen", "literal", "πειράζοντες", None, ["versuchen"], None),
 ("MAT.19.3", "einem Mann", "adapted", "ἀνθρώπῳ", "einem Menschen", None,
  "Im Zusammenhang ist der Ehemann gemeint; nach jüdischem Recht der Zeit konnte nur er die Ehe auflösen."),
 ("MAT.19.3", "zu entlassen", "literal", "ἀπολῦσαι", None, ["sich scheiden zu lassen von"],
  "Wie bei Markus ([[MRK.10.2]]): Rechtssprache nach [[DEU.24.1]]; «entlassen» lässt die einseitige Rechtslage sichtbar."),
 ("MAT.19.3", "aus jedem Grund", "interpretive", "κατὰ πᾶσαν αἰτίαν", None, ["aus jedem beliebigen Grund"],
  "Die Frage entspricht einer Streitfrage der Zeit über [[DEU.24.1]]: Nach der Schule Hillels genügte fast jeder Anlass, nach der Schule Schammais nur sexuelles Fehlverhalten."),
 ("MAT.19.4", "der Schöpfer", "adapted", "ὁ κτίσας", "der (sie) erschaffen hat", None, None),
 ("MAT.19.4", "männlich", "literal", "ἄρσεν καὶ θῆλυ ἐποίησεν αὐτοὺς", None, ["als Mann und Frau"],
  "Zitat aus [[GEN.1.27]] (griechische Fassung), wie [[MRK.10.6]]."),
 ("MAT.19.5", "und gesagt hat", "interpretive", "καὶ εἶπεν", None, ["und er sagte"],
  "Subjekt ist nach dem Satzbau der Schöpfer; in [[GEN.2.24]] ist der Satz eine Bemerkung des Erzählers. Matthäus versteht ihn als Wort Gottes."),
 ("MAT.19.5", "ein Fleisch", "literal", "εἰς σάρκα μίαν", "zu einem Fleisch", ["eine Einheit", "ein Leib"],
  "Zitat aus [[GEN.2.24]]; «Fleisch» meint den ganzen Menschen in seiner Leiblichkeit."),
 ("MAT.19.7", "einen Scheidebrief", "literal", "βιβλίον ἀποστασίου", None, ["eine Scheidungsurkunde"], "Vgl. [[DEU.24.1]]."),
 ("MAT.19.8", "Herzenshärte", "literal", "σκληροκαρδίαν", None, ["Hartherzigkeit"], None),
 ("MAT.19.9", "ausser wegen Unzucht", "interpretive", "μὴ ἐπὶ πορνείᾳ", None, ["ausser wegen Ehebruch", "ausser bei sexuellem Fehlverhalten", "ausser bei unerlaubter Ehe"],
  "πορνεία ist ein weiter Begriff für sexuelles Fehlverhalten. Die Ausnahme steht nur bei Matthäus (auch [[MAT.5.32]]), nicht bei Markus ([[MRK.10.11]]) und Lukas. Gedeutet wird sie als Ehebruch der Frau, als Ehe in verbotenen Verwandtschaftsgraden ([[LEV.18.6]]–[[LEV.18.18]]) oder als Unzucht vor der Ehe. «Unzucht» folgt der vertrauten Wiedergabe und lässt die Deutung offen."),
 ("MAT.19.9", "bricht die Ehe", "literal", "μοιχᾶται", None, None, None),
 ("MAT.19.10", "die Sache des Mannes mit der Frau", "interpretive", "ἡ αἰτία τοῦ ἀνθρώπου μετὰ τῆς γυναικός", None, ["das Verhältnis des Mannes zur Frau"],
  "αἰτία ist dasselbe Wort wie «Grund» in [[MAT.19.3]]; hier bezeichnet es die Sachlage."),
 ("MAT.19.10", "ratsam", "literal", "οὐ συμφέρει", None, ["gut", "vorteilhaft"], None),
 ("MAT.19.11", "dieses Wort", "interpretive", "τὸν λόγον τοῦτον", None, None,
  "Offen ist, worauf sich «dieses Wort» bezieht: auf die Bemerkung der Jünger ([[MAT.19.10]]), auf Jesu Weisung ([[MAT.19.9]]) oder auf das folgende Wort von den Eunuchen ([[MAT.19.12]])."),
 ("MAT.19.11", "fassen", "literal", "χωροῦσι", None, ["annehmen", "verstehen"],
  "χωρέω «Raum haben für, fassen»; ebenso [[MAT.19.12]]."),
 ("MAT.19.12", "Eunuchen", "literal", "εὐνοῦχοι", None, ["Verschnittene", "Entmannte"],
  "Eunuchen waren zeugungsunfähige Männer, von Geburt an oder durch Kastration, oft im Dienst von Höfen. Die dritte Gruppe wird meist bildlich verstanden: Menschen, die um des Reiches willen ehelos leben. Wörtlich verstanden hat sie in der Alten Kirche eine Minderheit."),
 ("MAT.19.13", "auflege", "literal", "ἐπιθῇ", None, None, "Handauflegung als Segensgeste (vgl. [[GEN.48.14]])."),
 ("MAT.19.14", "solchen gehört", "literal", "τῶν τοιούτων ἐστὶν", None, None,
  "Mehrdeutig: Kindern und Menschen wie ihnen. Vgl. [[MAT.18.3]]–[[MAT.18.4]]."),
 ("MAT.19.16", "einer", "literal", "εἷς", None, None,
  "Matthäus nennt ihn später «junger Mann» ([[MAT.19.20]], [[MAT.19.22]]); bei Lukas ist er ein Vorsteher ([[LUK.18.18]])."),
 ("MAT.19.16", "Lehrer", "literal", "Διδάσκαλε", None, ["Meister"],
  "Ohne «guter» (anders [[MRK.10.17]] und RP; siehe Alternativen)."),
 ("MAT.19.16", "erlange", "literal", "σχῶ", "habe", ["bekomme"], None),
 ("MAT.19.17", "Was fragst du mich nach dem Guten?", "literal", "Τί με ἐρωτᾷς περὶ τοῦ ἀγαθοῦ;", "Warum fragst du mich über das Gute?", None,
  "Bei Markus ([[MRK.10.18]]) lautet die Antwort: «Was nennst du mich gut? Niemand ist gut ausser einer: Gott.» Der SBLGNT-Apparat verzeichnet diese Fassung auch für Matthäus als Lesart von RP (gegen WH, Treg und NA28: λέγεις ἀγαθόν; Οὐδεὶς ἀγαθός εἰ μὴ εἷς ὁ θεός). Sie fehlt in den importierten Variantendaten und steht deshalb nicht bei den Alternativen."),
 ("MAT.19.17", "Einer ist der Gute", "interpretive", "εἷς ἐστιν ὁ ἀγαθός", None, ["Nur einer ist gut"],
  "Gemeint ist Gott; der Satz nennt ihn nicht ausdrücklich."),
 ("MAT.19.17", "in das Leben hineingehen", "literal", "εἰς τὴν ζωὴν εἰσελθεῖν", None, None,
  "«Das Leben» steht hier für das ewige Leben ([[MAT.19.16]]), wie in [[MAT.18.8]]–[[MAT.18.9]]."),
 ("MAT.19.18", "Du sollst", "literal", "Οὐ φονεύσεις", "Du wirst nicht töten", None,
  "Gebote aus [[EXO.20.12]]–[[EXO.20.16]] (vgl. [[DEU.5.16]]–[[DEU.5.20]]), das Futur als Gebot."),
 ("MAT.19.19", "du sollst deinen Nächsten lieben wie dich selbst", "literal", "Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν", None, None,
  "Zitat aus [[LEV.19.18]]; nur Matthäus fügt es der Reihe der Gebote an (vgl. [[MAT.22.39]])."),
 ("MAT.19.20", "Der junge Mann", "literal", "ὁ νεανίσκος", None, ["Der Jüngling"], None),
 ("MAT.19.21", "vollkommen", "interpretive", "τέλειος", None, ["ganz", "ungeteilt"],
  "τέλειος heisst «ganz, am Ziel». Vgl. [[MAT.5.48]]. Ob damit eine besondere Stufe gemeint ist oder das Ganze dessen, was zum Leben führt, wird verschieden gedeutet."),
 ("MAT.19.21", "in den Himmeln", "literal", "ἐν οὐρανοῖς", None, ["im Himmel"], "Mehrzahl wie im SBLGNT (siehe Alternativen)."),
 ("MAT.19.22", "Güter", "literal", "κτήματα", None, ["Besitzungen", "Grundbesitz"], None),
 ("MAT.19.23", "schwer", "literal", "δυσκόλως", None, ["nur mit Mühe"], None),
 ("MAT.19.24", "Reich Gottes", "literal", "τὴν βασιλείαν τοῦ θεοῦ", None, None,
  "Eine der vier Stellen, an denen Matthäus «Reich Gottes» statt «Reich der Himmel» sagt (siehe [[MAT.18.1]]); Treg liest auch hier «Reich der Himmel» (siehe Alternativen)."),
 ("MAT.19.24", "Nadelöhr", "literal", "τρυπήματος ῥαφίδος", "Loch einer Nadel", None,
  "Bildhafte Übertreibung wie [[MRK.10.25]]. Spätere Deutungen auf ein enges Stadttor oder auf ein «Seil» (κάμιλος statt κάμηλος) haben keinen Anhalt am hier übersetzten Text."),
 ("MAT.19.25", "gerettet werden", "literal", "σωθῆναι", None, None, None),
 ("MAT.19.28", "der Neuschöpfung", "interpretive", "τῇ παλιγγενεσίᾳ", "der Wiedergeburt", ["der Erneuerung der Welt", "der Wiederherstellung"],
  "παλιγγενεσία «neue Entstehung» bezeichnet hier die Erneuerung der Welt am Ende der Zeit; im Neuen Testament sonst nur [[TIT.3.5]] für die Neugeburt des Menschen."),
 ("MAT.19.28", "richten", "interpretive", "κρίνοντες", None, ["regieren", "Recht schaffen für"],
  "κρίνω kann wie hebräisch šāpaṭ auch «regieren» heissen (vgl. die Richter Israels). Ob Gericht über Israel oder Herrschaft gemeint ist, ist umstritten."),
 ("MAT.19.28", "Menschensohn", "literal", "ὁ υἱὸς τοῦ ἀνθρώπου", None, None,
  "Grundentscheid wie bei Markus: «Menschensohn». Zum Thron der Herrlichkeit vgl. [[MAT.25.31]] und [[DAN.7.13]]–[[DAN.7.14]]."),
 ("MAT.19.29", "Hundertfaches", "literal", "ἑκατονταπλασίονα", None, ["Vielfaches"], "WH und Treg lesen «Vielfaches» (siehe Alternativen)."),
 ("MAT.19.29", "ewiges Leben erben", "literal", "ζωὴν αἰώνιον κληρονομήσει", None, None, None),
 ("MAT.19.30", "Viele Erste aber werden Letzte sein", "interpretive", "πολλοὶ δὲ ἔσονται πρῶτοι ἔσχατοι", None, ["Viele aber werden als Erste Letzte sein"],
  "Der Satz leitet zum Gleichnis von den Arbeitern im Weinberg über ([[MAT.20.1]]–[[MAT.20.16]]), das mit dem umgekehrten Satz schliesst ([[MAT.20.16]])."),
]

DEC_GSW = [
 ("MAT.18.1", "de Gröscht", "interpretive", "μείζων", "de Grösser", None, "D Steigerigsform staat oft für de Superlativ."),
 ("MAT.18.1", "im Riich vo de Himel", "literal", "ἐν τῇ βασιλείᾳ τῶν οὐρανῶν", None, ["im Himmelriich"],
  "Grundentscheid fürs ganz Matthäusevangelium: «s Riich vo de Himel», mit de Mehrzahl vom Griechische. De Matthäus brucht d Wändig 32-mal, «Riich vo Gott» nu 4-mal; vili gsehnd drin e jüdischi Schüüchi, de Gottesname uuszspräche."),
 ("MAT.18.3", "umwänded", "literal", "στραφῆτε", None, ["umchered", "eu ändered"],
  "«Umchere» isch für μετανοέω reserviert; drum da «sich umwände»."),
 ("MAT.18.4", "chlii macht", "adapted", "ταπεινώσει ἑαυτὸν", "sich erniedrige wird", None,
  "S Chind isch es Bild für e nidrigi Stellig; d Verbindig zu «dene Chliine» ([[MAT.18.6]]) bliibt sichtbar."),
 ("MAT.18.6", "z Fall bringt", "interpretive", "σκανδαλίσῃ", None, ["vom Glaube abbringt"],
  "Einheitlich fürs Matthäusevangelium: σκανδαλίζω aktiv «z Fall bringe», passiv «Aastoss nää» oder «z Fall choo». σκάνδαλον isch s Stellhölzli vo nere Falle; drum σκάνδαλον «Fallstrick» ([[MAT.18.7]])."),
 ("MAT.18.6", "en grosse Mülistei", "interpretive", "μύλος ὀνικὸς", "en Esels-Mülistei", None, "De schwär Stei vo nere Müli, wo en Esel dräit."),
 ("MAT.18.8", "rüer", "adapted", "βάλε", "wirf", None, "«Rüere» isch s Mundartwort für «wärfe»."),
 ("MAT.18.8", "hau en ab", "literal", "ἔκκοψον αὐτὸν", None, ["hau si ab"], "αὐτόν isch männlich und Einzahl und bezieht sich uf de Fuess, wo zletscht gnännt isch."),
 ("MAT.18.9", "d Höll vom Füür", "traditional", "τὴν γέενναν τοῦ πυρός", None, None, "γέεννα: s Hinnomtal bi Jerusalem, Bild für de Ort vom Gricht."),
 ("MAT.18.10", "i de Himel", "literal", "ἐν οὐρανοῖς", None, ["im Himel"],
  "Mehrzahl wie im Griechische und im Vaterunser ([[MAT.6.9]]); d Einzahl ἐν οὐρανῷ heisst «im Himel» ([[MAT.18.18]])."),
 ("MAT.18.12", "staa", "adapted", "ἀφήσει", "laat … laa", None, "«Staa laa» isch i de Mundart s gwöhnlich Wort für «zrugglaa»."),
 ("MAT.18.12", "verlauft", "literal", "πλανηθῇ", None, ["verirrt"], None),
 ("MAT.18.13", "würkli", "adapted", "γένηται", "es gschiet", None, "D Mundart chunnt ohni «es gschiet, dass» uus; «würkli» haltet fescht, dass es offe isch."),
 ("MAT.18.15", "Brueder", "interpretive", "ἀδελφός", None, ["Brueder oder Schwöschter"], "Gmeint isch es Mitglid vo de Gmeinschaft."),
 ("MAT.18.15", "stell en zur Red", "literal", "ἔλεγξον αὐτὸν", None, ["wiis en zrächt"], None),
 ("MAT.18.16", "d Ussag", "adapted", "στόματος", "de Mund", None, "Uufnaam vo [[DEU.19.15]]."),
 ("MAT.18.17", "Gmeind", "interpretive", "ἐκκλησίᾳ", None, ["Chile", "Versammlig"],
  "Grundentscheid: ἐκκλησία «Gmeind»; «Chile» würd spööteri Strukture iiträge."),
 ("MAT.18.17", "de Heid und de Zöllner", "literal", "ὁ ἐθνικὸς καὶ ὁ τελώνης", None, None,
  "Beidi händ für vili als Ussestehendi gulte. Öb de Satz en Uusschluss meint oder dra erinneret, dass sich de Jesus grad de Zöllner zuewändet ([[MAT.9.10]]), wird verschide düütet."),
 ("MAT.18.18", "bunde sii", "interpretive", "ἔσται δεδεμένα", None, ["bunde wärde"], "Futur mit Perfekt; vgl. [[MAT.16.19]]."),
 ("MAT.18.19", "gää", "adapted", "γενήσεται", "gscheh", None, "«Es wird ine gscheh» isch i de Mundart unüblich; umschribe."),
 ("MAT.18.21", "vergib", "adapted", "ἀφήσω", "ich wird vergää", None,
  "D Mundart hät kei Futur; Präsens. Grundentscheid: ἀφίημι «vergää» wie im Vaterunser; im Gliichnis bi Gäldschuld «erlaa»."),
 ("MAT.18.22", "sibenesibezg Mal", "interpretive", "ἑβδομηκοντάκις ἑπτά", None, ["sibezg Mal sibe Mal"], "Wie i [[GEN.4.24]] (griechischi Fassig)."),
 ("MAT.18.23", "Chnächt", "interpretive", "δούλων", None, ["Sklave", "Diener"], "Wie bim Markus."),
 ("MAT.18.24", "zäätuusig Talänt", "literal", "μυρίων ταλάντων", None, None,
  "Es Talänt isch öppe 6000 Denar gsii, en Denar en Taglohn; d Summe isch bewusst unvorstellbar."),
 ("MAT.18.26", "nidergworfe", "interpretive", "προσεκύνει", None, ["ghuldiget", "aabätet"], "Einheitlich fürs Matthäusevangelium: προσκυνέω vor Mänsche und vor em Jesus «sich niderwärfe», mit Gott als Empfänger «aabätte». Da d Gebärde vo de Unterwärfig vor emne Herrscher; s gliich Wort staat für s Aabätte."),
 ("MAT.18.27", "erlaa", "adapted", "ἀφῆκεν", None, ["vergää"], "S gliich Verb wie «vergää» i [[MAT.18.21]] und [[MAT.18.35]]."),
 ("MAT.18.29", "aagfleht", "adapted", "παρεκάλει", "bätte", None, "«Bätte» chönnt mer mit «bätte» (bete) verwächsle; drum «aafleh». Ebeso [[MAT.18.32]]."),
 ("MAT.18.34", "Folterchnächt", "literal", "βασανισταῖς", None, None, None),
 ("MAT.18.35", "macht s", "adapted", "ποιήσει", "wird mache", None, "D Mundart hät kei Futur; Präsens."),
 ("MAT.18.35", "himmlisch Vatter", "literal", "ὁ πατήρ μου ὁ οὐράνιος", None, None, "Grundentscheid wie im Vaterunser ([[MAT.6.14]])."),
 ("MAT.19.1", "es isch gscheh", "literal", "ἐγένετο", None, None,
  "D Formle schlüüsst bim Matthäus di füf grosse Rede ab ([[MAT.7.28]], [[MAT.11.1]], [[MAT.13.53]], [[MAT.26.1]])."),
 ("MAT.19.3", "entlaa", "literal", "ἀπολῦσαι", None, ["sich la scheide vo"], "Rächtsspraach: De Maa hät d Frau mit emne Scheidigsbrief entlaa ([[DEU.24.1]])."),
 ("MAT.19.3", "Dörf en Maa", "adapted", "ἔξεστιν ἀνθρώπῳ", "Isch es emne Mänsch erlaubt", None, None),
 ("MAT.19.9", "usser wäge Unzucht", "interpretive", "μὴ ἐπὶ πορνείᾳ", None, ["usser wäge Eebruch"],
  "πορνεία isch en wiite Begriff für sexuells Fehlverhalte; d Uusnaam staat nu bim Matthäus ([[MAT.5.32]]). Si wird verschide düütet: Eebruch, verboteni Verwandteee, Unzucht vor de Ee."),
 ("MAT.19.12", "Eunuche", "literal", "εὐνοῦχοι", None, ["Verschnitteni"], "Di dritt Gruppe wird meischt bildlich verstande: Lüüt, wo wäge em Riich nöd hürated."),
 ("MAT.19.17", "Werum frögsch du mich nach em Guete?", "literal", "Τί με ἐρωτᾷς περὶ τοῦ ἀγαθοῦ;", None, None,
  "Bim Markus ([[MRK.10.18]]) und nach em SBLGNT-Apparat bi RP heisst s: «Werum seisch du mir guet? Niemer isch guet usser eine: Gott.» Die Läsart fehlt i de importierte Variantedate."),
 ("MAT.19.17", "Eine isch de Guet", "interpretive", "εἷς ἐστιν ὁ ἀγαθός", None, None, "Gmeint isch Gott."),
 ("MAT.19.21", "vollkomme", "interpretive", "τέλειος", None, ["ganz"], "Vgl. [[MAT.5.48]]."),
 ("MAT.19.24", "Riich vo Gott", "literal", "τὴν βασιλείαν τοῦ θεοῦ", None, None, "Eini vo de vier Stelle, wo de Matthäus «Riich vo Gott» seit."),
 ("MAT.19.27", "überchömed mir", "adapted", "ἔσται ἡμῖν", "wird üs sii", None, None),
 ("MAT.19.28", "Neuschöpfig", "interpretive", "παλιγγενεσίᾳ", "Widergeburt", ["Ernüürig vo de Wält"], "D Ernüürig vo de Wält am Änd vo de Ziit."),
 ("MAT.19.28", "richte", "interpretive", "κρίνοντες", None, ["regiere"], None),
]

# (Variante:Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Lesarten de, Lesarten gsw,
#  Entstehung de, Entstehung gsw)
ALTS = [
 ("VAR-SBLGNTAPP-MAT-018-002-01:R2", "MAT.18.2", "Und er rief ein Kind herbei", "Und Jesus rief ein Kind herbei",
  "Und er hät es Chind zu sich grüeft", "Und de Jesus hät es Chind zu sich grüeft", "gering",
  "Der Name Jesu wird ausdrücklich genannt.", "De Name vom Jesus wird usdrücklich gnännt.",
  {"R1": [("προσκαλεσάμενος", "er rief herbei", "WH, Treg, NA28")], "R2": [("προσκαλεσάμενος ὁ Ἰησοῦς", "Jesus rief herbei", "RP")]},
  {"R1": [("προσκαλεσάμενος", "er hät grüeft", "WH, Treg, NA28")], "R2": [("προσκαλεσάμενος ὁ Ἰησοῦς", "de Jesus hät grüeft", "RP")]},
  ["Der Name kann zur Verdeutlichung ergänzt sein, wie oft am Anfang eines Abschnitts; ebenso kann er ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne den Namen, 05 und 032 mit ihm; 04 ist hier nicht erhalten."],
  ["De Name cha zur Verdüütlichung ergänzt sii, wie oft am Aafang vo eme Abschnitt; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni de Name, 05 und 032 mit; 04 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-018-007-02:R2", "MAT.18.7", "wehe dem Menschen", "wehe jenem Menschen",
  "wehe em Mänsch", "wehe däm Mänsch", "gering",
  "Das hinweisende «jenem» verstärkt die Warnung.", "S «däm» verstärkt d Warnig.",
  {"R1": [("ἀνθρώπῳ", "dem Menschen", "WH, Treg, NA28")], "R2": [("ἀνθρώπῳ ἐκείνῳ", "jenem Menschen", "RP")]},
  {"R1": [("ἀνθρώπῳ", "em Mänsch", "WH, Treg, NA28")], "R2": [("ἀνθρώπῳ ἐκείνῳ", "däm Mänsch", "RP")]},
  ["«Jenem» kann an [[MAT.26.24]] angeglichen sein, wo die Wendung steht; ebenso kann das Wort ausgefallen sein.",
   "Laut der automatischen Zuordnung liest 03 mit ἐκείνῳ, 05 ohne. 01 und 032 hat die Zuordnung keiner Lesart zugewiesen; nach den CNTR-Transkriptionen steht in 01 kein ἐκείνῳ, in 032 steht es an anderer Stelle (vor «wehe»)."],
  ["«Däm» cha a [[MAT.26.24]] aaglichen sii; oder s Wort isch usgfalle.",
   "Nach de automatische Zueornig liest 03 mit ἐκείνῳ, 05 ohni; nach de CNTR-Transkriptione staat s i 01 nöd und i 032 a andere Stell."]),
 ("VAR-SBLGNTAPP-MAT-018-008-01:R2", "MAT.18.8", "hau ihn ab", "hau sie ab",
  "hau en ab", "hau si ab", "gering",
  "Die Mehrzahl bezieht sich auf beide Glieder, Hand und Fuss.", "D Mehrzahl bezieht sich uf beidi, Hand und Fuess.",
  {"R1": [("αὐτόν", "ihn", "WH, Treg, NA28")], "R2": [("αὐτά", "sie (beide)", "RP")]},
  {"R1": [("αὐτόν", "en", "WH, Treg, NA28")], "R2": [("αὐτά", "si (beidi)", "RP")]},
  ["Die Mehrzahl passt grammatisch zu den beiden Gliedern und kann eine Glättung sein; ebenso kann die Einzahl an [[MAT.18.9]] angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 αὐτόν, 032 αὐτά; 04 ist hier nicht erhalten."],
  ["D Mehrzahl passt zu beidne Glider und cha e Glättig sii; oder d Einzahl isch a [[MAT.18.9]] aaglichen.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 αὐτόν, 032 αὐτά."]),
 ("VAR-SBLGNTAPP-MAT-018-010-01:R2", "MAT.18.10", "meines Vaters in den Himmeln.", "meines Vaters in den Himmeln. Denn der Menschensohn ist gekommen, das Verlorene zu retten.",
  "vo mim Vatter i de Himel.", "vo mim Vatter i de Himel. De Mänschesohn isch nämli choo, für das z rette, wo verlore isch.", "mittel",
  "Der Zusatz bildet den Vers [[MAT.18.11]] der KJV-Zählung; im SBLGNT fehlt er, deshalb hat [[MAT.18.11]] hier keinen Übersetzungstext. Er gleicht [[LUK.19.10]].",
  "De Zuesatz isch de Vers [[MAT.18.11]] (KJV-Zellig); im SBLGNT fehlt er, drum hät [[MAT.18.11]] da kein Text. Er gliicht [[LUK.19.10]].",
  {"R1": [("οὐρανοῖς", "(ohne Vers 11)", "WH, Treg, NA28")], "R2": [("οὐρανοῖς. Ἦλθεν γὰρ ὁ υἱὸς τοῦ ἀνθρώπου σῶσαι τὸ ἀπολωλός", "Denn der Menschensohn ist gekommen, das Verlorene zu retten", "RP")]},
  {"R1": [("οὐρανοῖς", "(ohni Vers 11)", "WH, Treg, NA28")], "R2": [("… Ἦλθεν γὰρ ὁ υἱὸς τοῦ ἀνθρώπου σῶσαι τὸ ἀπολωλός", "De Mänschesohn isch nämli choo, für das z rette, wo verlore isch", "RP")]},
  ["Der Satz kann aus [[LUK.19.10]] übernommen worden sein, als Überleitung zum Gleichnis vom verirrten Schaf; ebenso kann er beim Abschreiben ausgefallen sein.",
   "Die automatische Zuordnung ordnet alle erfassten Handschriften und auch RP dem kurzen Text zu; das widerspricht dem Apparat, der RP für den Zusatz nennt. Sie vergleicht nur den Wortlaut bis zum Ende von [[MAT.18.10]] und kann einen zusätzlichen Vers nicht sehen. Über die Handschriften lässt sich hier aus den Daten nichts sagen; es gilt die Angabe des Apparats."],
  ["De Satz cha us [[LUK.19.10]] übernoo sii, as Überleitig zum Gliichnis vom Schaf, wo sich verloffe hät; oder er isch bim Abschriibe usgfalle.",
   "D automatisch Zueornig ordnet alli Handschrifte und au RP em churze Text zue; das widerspricht em Apparat. Si vergliicht nu bis as Änd vo [[MAT.18.10]] und gseet de zuesätzlich Vers nöd. Über d Handschrifte laat sich us de Date nüüt säge."]),
 ("VAR-SBLGNTAPP-MAT-018-014-02:R2", "MAT.18.14", "eures Vaters", "meines Vaters",
  "vo euem Vatter", "vo mim Vatter", "gering",
  "Mit «meines» spricht Jesus wie in [[MAT.18.10]] und [[MAT.18.19]] von seinem Vater. Der SBLGNT folgt hier NA28 und RP gegen WH und Treg.",
  "Mit «mim» redt de Jesus wie i [[MAT.18.10]] und [[MAT.18.19]] vo sim Vatter.",
  {"R1": [("ὑμῶν", "eures", "NA28, RP")], "R2": [("μου", "meines", "WH, Treg")]},
  {"R1": [("ὑμῶν", "euem", "NA28, RP")], "R2": [("μου", "mim", "WH, Treg")]},
  ["«Meines» kann an [[MAT.18.10]] und [[MAT.18.19]] angeglichen sein; ebenso kann «eures» an [[MAT.6.14]] und ähnliche Stellen angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01, 05 und 032 ὑμῶν, 03 μου."],
  ["«Mim» cha a [[MAT.18.10]] und [[MAT.18.19]] aaglichen sii; oder «euem» a [[MAT.6.14]].",
   "Nach de automatische Zueornig läsed 01, 05 und 032 ὑμῶν, 03 μου."]),
 ("VAR-SBLGNTAPP-MAT-018-015-01:R2", "MAT.18.15", "dein Bruder gegen dich sündigt", "dein Bruder sündigt",
  "din Brueder gäge dich sündiget", "din Brueder sündiget", "mittel",
  "Ohne «gegen dich» spricht der Satz von jeder Sünde des Bruders, nicht nur von einer, die dich selbst trifft.",
  "Ohni «gäge dich» redt de Satz vo jeder Sünd vom Brueder, nöd nu vo eire, wo dich sälber trifft.",
  {"R1": [("εἰς σέ", "gegen dich", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  {"R1": [("εἰς σέ", "gäge dich", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  ["«Gegen dich» kann aus [[MAT.18.21]] («gegen mich») ergänzt sein; ebenso kann es beim Abschreiben ausgefallen sein, zumal εἰς σέ ähnlich klingt wie die Endung des vorangehenden ἁμαρτήσῃ.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne «gegen dich», 05 und 032 mit."],
  ["«Gäge dich» cha us [[MAT.18.21]] ergänzt sii; oder s isch usgfalle, wil εἰς σέ ähnlich tönt wie s Änd vo ἁμαρτήσῃ.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni «gäge dich», 05 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-018-019-01:R2", "MAT.18.19", "Wiederum, amen, ich sage euch", "Wiederum sage ich euch",
  "Wider, amen, ich säg eu", "Wider säg ich eu", "gering",
  "Ohne das zweite «Amen» fehlt die feierliche Bekräftigung.", "Ohni s zweit «Amen» fehlt d feierlich Bekräftigung.",
  {"R1": [("ἀμήν", "amen", "WH, Treg, RP, NA28")], "R2": [("–", "(fehlt)", "NIV")]},
  {"R1": [("ἀμήν", "amen", "WH, Treg, RP, NA28")], "R2": [("–", "(fehlt)", "NIV")]},
  ["Das Wort kann kurz nach [[MAT.18.18]] ergänzt worden sein; ebenso kann es ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 05 ohne «Amen», 03 mit; 032 liest anders (nach der CNTR-Transkription «wiederum aber euch»)."],
  ["S Wort cha churz nach [[MAT.18.18]] ergänzt worde sii; oder s isch usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 05 ohni «Amen», 03 mit; 032 liest anders."]),
 ("VAR-SBLGNTAPP-MAT-018-026-01:R2", "MAT.18.26", "«Hab Geduld mit mir", "«Herr, hab Geduld mit mir",
  "«Häb Geduld mit mir", "«Herr, häb Geduld mit mir", "gering",
  "Der Knecht redet seinen Herrn ausdrücklich an.", "De Chnächt redt sin Herr usdrücklich aa.",
  {"R1": [("Μακροθύμησον", "Hab Geduld", "WH, Treg, NA28")], "R2": [("Κύριε, μακροθύμησον", "Herr, hab Geduld", "RP")]},
  {"R1": [("Μακροθύμησον", "Häb Geduld", "WH, Treg, NA28")], "R2": [("Κύριε, μακροθύμησον", "Herr, häb Geduld", "RP")]},
  ["Die Anrede kann aus dem Zusammenhang ergänzt sein; ebenso kann sie ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 03 und 05 ohne Anrede; bei 01 und 032 ist die Zuordnung unklar, nach den CNTR-Transkriptionen steht dort die Anrede als abgekürztes Kürzel (ΚΕ)."],
  ["D Aared cha us em Zämehang ergänzt sii; oder si isch usgfalle.",
   "Nach de automatische Zueornig läsed 03 und 05 ohni Aared; i 01 und 032 staat si nach de CNTR-Transkriptione als Chürzel."]),
 ("VAR-SBLGNTAPP-MAT-018-029-01:R2", "MAT.18.29", "Da fiel sein Mitknecht nieder", "Da fiel sein Mitknecht ihm zu Füssen nieder",
  "Sin Mitchnächt isch drum nidergfalle", "Sin Mitchnächt isch drum vor sine Füess nidergfalle", "gering",
  "Der Zusatz malt die Szene aus.", "De Zuesatz malt d Szene us.",
  {"R1": [("αὐτοῦ", "(ohne Zusatz)", "WH, Treg, NA28")], "R2": [("αὐτοῦ εἰς τοὺς πόδας αὐτοῦ", "ihm zu Füssen", "RP")]},
  {"R1": [("αὐτοῦ", "(ohni Zuesatz)", "WH, Treg, NA28")], "R2": [("… εἰς τοὺς πόδας αὐτοῦ", "vor sine Füess", "RP")]},
  ["Der Zusatz kann die Szene ausmalen und an [[MAT.18.26]] angleichen; ebenso kann er ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 ohne Zusatz, 032 mit."],
  ["De Zuesatz cha d Szene usmale; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 ohni Zuesatz, 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-018-035-02:R2", "MAT.18.35", "jeder seinem Bruder.", "jeder seinem Bruder seine Verfehlungen.",
  "jede sim Brueder.", "jede sim Brueder sini Fääler.", "gering",
  "Der Zusatz nennt, was zu vergeben ist.", "De Zuesatz nännt, was z vergää isch.",
  {"R1": [("ὑμῶν", "(ohne Zusatz)", "WH, Treg, NA28")], "R2": [("ὑμῶν τὰ παραπτώματα αὐτῶν", "ihre Verfehlungen", "RP")]},
  {"R1": [("ὑμῶν", "(ohni Zuesatz)", "WH, Treg, NA28")], "R2": [("… τὰ παραπτώματα αὐτῶν", "iri Fääler", "RP")]},
  ["Der Zusatz kann aus [[MAT.6.14]]–[[MAT.6.15]] oder [[MRK.11.25]] übernommen sein; ebenso kann er ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne Zusatz, 04 und 032 mit."],
  ["De Zuesatz cha us [[MAT.6.14]]–[[MAT.6.15]] oder [[MRK.11.25]] übernoo sii; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni Zuesatz, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-019-004-02:R2", "MAT.19.4", "der Schöpfer", "der, der sie gemacht hat,",
  "de Schöpfer", "dä, wo si gmacht hät,", "gering",
  "ποιήσας nimmt das Verb des Zitats auf («gemacht»).", "ποιήσας nimmt s Verb vom Zitat uf.",
  {"R1": [("κτίσας", "der Schöpfer", "WH, Treg, NA28")], "R2": [("ποιήσας", "der (sie) gemacht hat", "RP")]},
  {"R1": [("κτίσας", "de Schöpfer", "WH, Treg, NA28")], "R2": [("ποιήσας", "dä, wo si gmacht hät", "RP")]},
  ["ποιήσας kann an das folgende ἐποίησεν und an [[GEN.1.27]] angeglichen sein; κτίσας kann eine Verdeutlichung sein.",
   "Laut der automatischen Zuordnung liest 03 κτίσας, 01, 04, 05 und 032 ποιήσας."],
  ["ποιήσας cha as folgend ἐποίησεν aaglichen sii; κτίσας cha e Verdüütlichung sii.",
   "Nach de automatische Zueornig liest 03 κτίσας, 01, 04, 05 und 032 ποιήσας."]),
 ("VAR-SBLGNTAPP-MAT-019-009-02:R2", "MAT.19.9", "bricht die Ehe; und wer eine Entlassene heiratet, bricht die Ehe.»", "bricht die Ehe.»",
  "bricht d Ee; und wer eini hüratet, wo entlaa worde isch, bricht d Ee.»", "bricht d Ee.»", "mittel",
  "Ohne den Satz fehlt die Aussage über den Mann, der eine Entlassene heiratet; sie steht auch in [[MAT.5.32]]. Der SBLGNT folgt hier Treg und RP gegen WH und NA28.",
  "Ohni de Satz fehlt d Ussag über de Maa, wo eini hüratet, wo entlaa worde isch; si staat au i [[MAT.5.32]].",
  {"R1": [("καὶ ὁ ἀπολελυμένην γαμήσας μοιχᾶται", "und wer eine Entlassene heiratet, bricht die Ehe", "Treg, RP")], "R2": [("–", "(fehlt)", "WH, NA28")]},
  {"R1": [("καὶ ὁ ἀπολελυμένην γαμήσας μοιχᾶται", "und wer eini hüratet, wo entlaa worde isch, bricht d Ee", "Treg, RP")], "R2": [("–", "(fehlt)", "WH, NA28")]},
  ["Der Satz kann aus [[MAT.5.32]] ergänzt sein; ebenso kann er durch Augensprung von μοιχᾶται zu μοιχᾶται ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 03, 04 und 032 mit dem Satz, 01 und 05 ohne. Nach den CNTR-Transkriptionen haben 03 und 04 vorher ausserdem die Wendung «macht, dass sie die Ehe bricht» (wie [[MAT.5.32]])."],
  ["De Satz cha us [[MAT.5.32]] ergänzt sii; oder er isch dur en Augesprung vo μοιχᾶται zu μοιχᾶται usgfalle.",
   "Nach de automatische Zueornig läsed 03, 04 und 032 mit em Satz, 01 und 05 ohni."]),
 ("VAR-SBLGNTAPP-MAT-019-010-01:R2", "MAT.19.10", "Die Jünger sagen", "Seine Jünger sagen",
  "D Jünger säged", "Sini Jünger säged", "gering",
  "Das Possessiv ändert den Sinn nicht. Der SBLGNT folgt hier WH gegen Treg, NA28 und RP.", "S «sini» änderet de Sinn nöd.",
  {"R1": [("μαθηταί", "die Jünger", "WH, NIV")], "R2": [("μαθηταὶ αὐτοῦ", "seine Jünger", "Treg, RP, NA28")]},
  {"R1": [("μαθηταί", "d Jünger", "WH, NIV")], "R2": [("μαθηταὶ αὐτοῦ", "sini Jünger", "Treg, RP, NA28")]},
  ["αὐτοῦ ist eine naheliegende Ergänzung (vgl. [[MAT.19.23]]); ebenso kann es ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne αὐτοῦ, 04, 05 und 032 mit."],
  ["αὐτοῦ isch e naheliegendi Ergänzig; oder s isch usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni αὐτοῦ, 04, 05 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-019-016-02:R2", "MAT.19.16", "«Lehrer,", "«Guter Lehrer,",
  "«Lehrer,", "«Guete Lehrer,", "mittel",
  "Mit «guter Lehrer» lautet die Anrede wie in [[MRK.10.17]]; Jesu Antwort bezieht sich dann auf die Anrede (so RP auch in [[MAT.19.17]]).",
  "Mit «guete Lehrer» heisst d Aared wie i [[MRK.10.17]]; d Antwort vom Jesus bezieht sich dänn uf d Aared.",
  {"R1": [("Διδάσκαλε", "Lehrer", "WH, Treg, NA28")], "R2": [("Διδάσκαλε ἀγαθέ", "Guter Lehrer", "RP")]},
  {"R1": [("Διδάσκαλε", "Lehrer", "WH, Treg, NA28")], "R2": [("Διδάσκαλε ἀγαθέ", "Guete Lehrer", "RP")]},
  ["Die Anrede kann aus [[MRK.10.17]] und [[LUK.18.18]] übernommen sein; ebenso kann sie weggelassen worden sein, als die Frage in [[MAT.19.17]] auf «das Gute» bezogen wurde. Beides hängt mit der Lesart von [[MAT.19.17]] zusammen, die der SBLGNT-Apparat ebenfalls verzeichnet.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 «Lehrer», 04 und 032 «guter Lehrer»."],
  ["D Aared cha us [[MRK.10.17]] und [[LUK.18.18]] übernoo sii; oder si isch wägglaa worde, wo d Frag i [[MAT.19.17]] uf «s Guet» bezoge worde isch.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 «Lehrer», 04 und 032 «guete Lehrer»."]),
 ("VAR-SBLGNTAPP-MAT-019-020-02:R2", "MAT.19.20", "Das alles habe ich gehalten.", "Das alles habe ich gehalten von meiner Jugend an.",
  "Das alles han ich ghalte.", "Das alles han ich ghalte vo minere Jugend aa.", "gering",
  "Der Zusatz gleicht die Antwort an [[MRK.10.20]] an.", "De Zuesatz gliicht d Antwort a [[MRK.10.20]] aa.",
  {"R1": [("ἐφύλαξα", "habe ich gehalten", "WH, Treg, NA28")], "R2": [("ἐφυλαξάμην ἐκ νεότητός μου", "habe ich gehalten von meiner Jugend an", "RP")]},
  {"R1": [("ἐφύλαξα", "han ich ghalte", "WH, Treg, NA28")], "R2": [("ἐφυλαξάμην ἐκ νεότητός μου", "han ich ghalte vo minere Jugend aa", "RP")]},
  ["Der Zusatz kann aus [[MRK.10.20]] und [[LUK.18.21]] übernommen sein; ebenso kann er ausgefallen sein, vielleicht weil er schlecht zu «der junge Mann» passt.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne Zusatz, 04, 05 und 032 mit."],
  ["De Zuesatz cha us [[MRK.10.20]] und [[LUK.18.21]] übernoo sii; oder er isch usgfalle, will er schlächt zu «de jung Maa» passt.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni Zuesatz, 04, 05 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-019-021-02:R2", "MAT.19.21", "einen Schatz in den Himmeln", "einen Schatz im Himmel",
  "en Schatz i de Himel", "en Schatz im Himel", "gering",
  "Einzahl statt Mehrzahl; der Sinn bleibt gleich.", "Einzahl statt Mehrzahl; de Sinn bliibt gliich.",
  {"R1": [("οὐρανοῖς", "in den Himmeln", "WH, Treg, NA28")], "R2": [("οὐρανῷ", "im Himmel", "RP")]},
  {"R1": [("οὐρανοῖς", "i de Himel", "WH, Treg, NA28")], "R2": [("οὐρανῷ", "im Himel", "RP")]},
  ["Die Einzahl kann an [[MRK.10.21]] und [[LUK.18.22]] angeglichen sein; ebenso kann die Mehrzahl an den Sprachgebrauch des Matthäus angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 03, 04 und 05 οὐρανοῖς, 032 οὐρανῷ; 01 hat die Zuordnung keiner Lesart zugewiesen, nach der CNTR-Transkription steht dort ein abgekürztes οὐρανῷ."],
  ["D Einzahl cha a [[MRK.10.21]] aaglichen sii; oder d Mehrzahl a de Spraachgebruuch vom Matthäus.",
   "Nach de automatische Zueornig läsed 03, 04 und 05 οὐρανοῖς, 032 οὐρανῷ."]),
 ("VAR-SBLGNTAPP-MAT-019-024-02:R2", "MAT.19.24", "durch ein Nadelöhr geht", "durch ein Nadelöhr hindurchgeht",
  "dur es Nadelööhr gaat", "dur es Nadelööhr dure gaat", "gering",
  "διελθεῖν «hindurchgehen» statt εἰσελθεῖν «hineingehen»; der Sinn bleibt gleich.", "διελθεῖν «dure gaa» statt εἰσελθεῖν «ine gaa».",
  {"R1": [("εἰσελθεῖν", "(hinein)gehen", "WH, Treg")], "R2": [("διελθεῖν", "hindurchgehen", "NA28, RP")]},
  {"R1": [("εἰσελθεῖν", "(ine) gaa", "WH, Treg")], "R2": [("διελθεῖν", "dure gaa", "NA28, RP")]},
  ["διελθεῖν kann an [[MRK.10.25]] und [[LUK.18.25]] angeglichen sein; εἰσελθεῖν kann an das folgende «hineinkommen» angeglichen sein. Der SBLGNT folgt hier WH und Treg gegen NA28 und RP.",
   "Laut der automatischen Zuordnung lesen 01, 04 und 032 εἰσελθεῖν, 03 und 05 διελθεῖν."],
  ["διελθεῖν cha a [[MRK.10.25]] aaglichen sii; εἰσελθεῖν as folgend «inechoo».",
   "Nach de automatische Zueornig läsed 01, 04 und 032 εἰσελθεῖν, 03 und 05 διελθεῖν."]),
 ("VAR-SBLGNTAPP-MAT-019-024-03:R4", "MAT.19.24", "in das Reich Gottes", "in das Reich der Himmel",
  "is Riich vo Gott", "is Riich vo de Himel", "gering",
  "Treg liest die bei Matthäus übliche Wendung «Reich der Himmel»; NA28 und RP unterscheiden sich vom SBLGNT nur in der Wortstellung.",
  "Treg liest di gwöhnlich Wändig vom Matthäus «Riich vo de Himel».",
  {"R1": [("εἰς τὴν βασιλείαν τοῦ θεοῦ", "in das Reich Gottes", "WH")], "R2": [("εἰσελθεῖν εἰς τὴν βασιλείαν τοῦ θεοῦ", "in das Reich Gottes hineinkommen", "NA28")],
   "R3": [("εἰς τὴν βασιλείαν τοῦ θεοῦ εἰσελθεῖν", "in das Reich Gottes hineinkommen", "RP")], "R4": [("εἰσελθεῖν εἰς τὴν βασιλείαν τῶν οὐρανῶν", "in das Reich der Himmel hineinkommen", "Treg")]},
  {"R1": [("εἰς τὴν βασιλείαν τοῦ θεοῦ", "is Riich vo Gott", "WH")], "R2": [("εἰσελθεῖν εἰς …", "is Riich vo Gott inechoo", "NA28")],
   "R3": [("… εἰσελθεῖν", "is Riich vo Gott inechoo", "RP")], "R4": [("εἰσελθεῖν εἰς τὴν βασιλείαν τῶν οὐρανῶν", "is Riich vo de Himel inechoo", "Treg")]},
  ["«Reich der Himmel» kann an den gewöhnlichen Sprachgebrauch des Matthäus und an [[MAT.19.23]] angeglichen sein; «Reich Gottes» kann aus [[MRK.10.25]] stammen.",
   "Laut der automatischen Zuordnung hat 01 den Wortlaut von R1, 03 und 05 den von R2, 04 und 032 den von R3; keine der erfassten Handschriften wird R4 zugeordnet."],
  ["«Riich vo de Himel» cha a de gwöhnlich Spraachgebruuch vom Matthäus aaglichen sii; «Riich vo Gott» cha us [[MRK.10.25]] stamme.",
   "Nach de automatische Zueornig wird kei erfassti Handschrift R4 zueornet."]),
 ("VAR-SBLGNTAPP-MAT-019-029-03:R2", "MAT.19.29", "oder Mutter oder Frau oder Kinder", "oder Mutter oder Kinder",
  "oder Mueter oder Frau oder Chind", "oder Mueter oder Chind", "mittel",
  "Ohne «Frau» fehlt die Ehefrau in der Aufzählung, wie in [[MRK.10.29]]. Der SBLGNT folgt hier RP gegen WH, Treg und NA28.",
  "Ohni «Frau» fehlt d Eefrau i de Ufzellig, wie i [[MRK.10.29]].",
  {"R1": [("γυναῖκα ἢ", "oder Frau", "RP")], "R2": [("–", "(fehlt)", "WH, Treg, NA28")]},
  {"R1": [("γυναῖκα ἢ", "oder Frau", "RP")], "R2": [("–", "(fehlt)", "WH, Treg, NA28")]},
  ["«Frau» kann aus [[LUK.18.29]] ergänzt sein; ebenso kann das Wort ausgefallen sein, vielleicht mit Blick auf [[MAT.19.3]]–[[MAT.19.9]].",
   "Laut der automatischen Zuordnung lesen 01, 04 und 032 mit «Frau», 03 und 05 ohne."],
  ["«Frau» cha us [[LUK.18.29]] ergänzt sii; oder s Wort isch usgfalle, vilicht wäge [[MAT.19.3]]–[[MAT.19.9]].",
   "Nach de automatische Zueornig läsed 01, 04 und 032 mit «Frau», 03 und 05 ohni."]),
 ("VAR-SBLGNTAPP-MAT-019-029-06:R2", "MAT.19.29", "Hundertfaches", "Vielfaches",
  "hundertfach", "vilfach", "gering",
  "Statt einer bestimmten Zahl ein unbestimmtes «Vielfaches». Der SBLGNT folgt hier NA28 und RP gegen WH und Treg.",
  "Statt hundertfach es unbestimmts «vilfach».",
  {"R1": [("ἑκατονταπλασίονα", "Hundertfaches", "NA28, RP")], "R2": [("πολλαπλασίονα", "Vielfaches", "WH, Treg")]},
  {"R1": [("ἑκατονταπλασίονα", "hundertfach", "NA28, RP")], "R2": [("πολλαπλασίονα", "vilfach", "WH, Treg")]},
  ["πολλαπλασίονα kann aus [[LUK.18.30]] stammen; ἑκατονταπλασίονα kann an [[MRK.10.30]] angeglichen sein.",
   "Laut der automatischen Zuordnung liest 03 πολλαπλασίονα, 01, 04, 05 und 032 ἑκατονταπλασίονα."],
  ["πολλαπλασίονα cha us [[LUK.18.30]] stamme; ἑκατονταπλασίονα cha a [[MRK.10.30]] aaglichen sii.",
   "Nach de automatische Zueornig liest 03 πολλαπλασίονα, 01, 04, 05 und 032 ἑκατονταπλασίονα."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-018-001-035", "MAT.18.1-MAT.18.35", "section", "Die Rede vom Leben in der Gemeinde",
  ["TU-MAT-018-001-005", "TU-MAT-018-006-009", "TU-MAT-018-010-014", "TU-MAT-018-015-020", "TU-MAT-018-021-035"],
  "Die Jünger fragen, wer im Reich der Himmel der Grösste sei. Jesus stellt ein Kind in ihre Mitte: Wer sich nicht umwendet und wie die Kinder wird, kommt nicht hinein; wer sich klein macht wie dieses Kind, ist der Grösste. Er warnt davor, einen dieser Kleinen zu Fall zu bringen oder zu verachten: Wie ein Mensch das eine verirrte Schaf sucht, so will der Vater in den Himmeln nicht, dass eines von ihnen verloren geht. Sündigt ein Bruder, soll man ihn zuerst allein zurechtweisen, dann mit Zeugen, dann vor der Gemeinde; was die Jünger auf der Erde binden und lösen, wird im Himmel gebunden und gelöst sein, und wo zwei oder drei in seinem Namen versammelt sind, ist er mitten unter ihnen. Auf die Frage des Petrus, ob er bis zu siebenmal vergeben solle, antwortet Jesus: bis zu siebenundsiebzigmal, und erzählt vom Knecht, dem sein Herr eine riesige Schuld erlässt, der selbst aber seinem Mitknecht eine kleine nicht erlässt und darum den Folterknechten ausgeliefert wird: So wird auch der himmlische Vater mit denen verfahren, die nicht von Herzen vergeben. [[MAT.18.11]] fehlt im SBLGNT.",
  SEG + " Kapitel 18 ist die vierte der fünf grossen Reden bei Matthäus; [[MAT.19.1]] schliesst sie mit der Formel ab, die auch die anderen Reden beendet."),
 ("TU-MAT-018-001-005", "MAT.18.1-MAT.18.5", "narrative_with_saying", "Wer ist der Grösste?", None,
  "Die Jünger fragen Jesus, wer im Reich der Himmel der Grösste sei. Er ruft ein Kind herbei, stellt es in ihre Mitte und sagt: Wenn sie sich nicht umwenden und wie die Kinder werden, werden sie nicht in das Reich der Himmel hineinkommen; wer sich klein macht wie dieses Kind, ist dort der Grösste, und wer ein solches Kind in seinem Namen aufnimmt, nimmt ihn auf.", None),
 ("TU-MAT-018-006-009", "MAT.18.6-MAT.18.9", "discourse", "Wehe dem, durch den der Fallstrick kommt", None,
  "Wer einen dieser Kleinen, die an Jesus glauben, zu Fall bringt, für den wäre es besser, mit einem Mühlstein um den Hals im Meer versenkt zu werden. Jesus ruft das Wehe über die Welt wegen der Fallstricke, die unvermeidlich kommen, und über den Menschen, durch den sie kommen. Wenn Hand, Fuss oder Auge zu Fall bringen, soll man sie abhauen oder herausreissen: Es ist besser, verstümmelt oder einäugig in das Leben hineinzugehen, als mit beiden Händen, Füssen oder Augen in das ewige Feuer, die Hölle des Feuers, geworfen zu werden.", None),
 ("TU-MAT-018-010-014", "MAT.18.10-MAT.18.14", "discourse", "Das verirrte Schaf", None,
  "Jesus warnt, keinen dieser Kleinen zu verachten, denn ihre Engel sehen allezeit das Angesicht seines Vaters in den Himmeln. Er fragt: Wird ein Mensch, dem von hundert Schafen eines sich verirrt hat, nicht die neunundneunzig lassen und das verirrte suchen? Gelingt es ihm, es zu finden, freut er sich über dieses mehr als über die neunundneunzig. So ist es nicht der Wille des Vaters in den Himmeln, dass eines dieser Kleinen verloren geht. [[MAT.18.11]] fehlt im SBLGNT.", None),
 ("TU-MAT-018-015-020", "MAT.18.15-MAT.18.20", "discourse", "Wenn dein Bruder sündigt", None,
  "Sündigt ein Bruder gegen jemanden, soll dieser ihn zuerst unter vier Augen zurechtweisen; hört er nicht, soll er einen oder zwei dazunehmen, damit jede Sache durch zwei oder drei Zeugen festgestellt wird; hört er auch auf sie nicht, soll er es der Gemeinde sagen; hört er auch auf die Gemeinde nicht, soll der Bruder für ihn wie der Heide und der Zöllner sein. Was die Jünger auf der Erde binden und lösen, wird im Himmel gebunden und gelöst sein. Werden zwei von ihnen auf der Erde über eine Sache einig, um die sie bitten, wird sie ihnen vom Vater zuteilwerden; denn wo zwei oder drei in seinem Namen versammelt sind, ist Jesus mitten unter ihnen.", None),
 ("TU-MAT-018-021-035", "MAT.18.21-MAT.18.35", "discourse", "Wie oft vergeben? Der Knecht und sein Mitknecht", None,
  "Petrus fragt, wie oft er seinem Bruder vergeben solle, ob bis zu siebenmal; Jesus antwortet: bis zu siebenundsiebzigmal. Dann vergleicht er das Reich der Himmel mit einem König, der mit seinen Knechten abrechnet: Einem, der zehntausend Talente schuldet und sich vor ihm niederwirft und um Geduld bittet, erlässt er aus Erbarmen die ganze Schuld. Dieser Knecht aber packt und würgt einen Mitknecht, der ihm hundert Denare schuldet, und wirft ihn trotz seiner Bitte ins Gefängnis. Als die Mitknechte es dem Herrn berichten, nennt er ihn einen bösen Knecht, der sich hätte erbarmen müssen, wie er sich über ihn erbarmt habe, und liefert ihn den Folterknechten aus, bis er die ganze Schuld bezahlt hätte. So, sagt Jesus, wird auch sein himmlischer Vater mit ihnen verfahren, wenn sie nicht jeder seinem Bruder von Herzen vergeben.", None),
 ("TU-MAT-019-001-030", "MAT.19.1-MAT.19.30", "section", "Ehe, Kinder, Reichtum und Lohn der Nachfolge",
  ["TU-MAT-019-001-012", "TU-MAT-019-013-015", "TU-MAT-019-016-022", "TU-MAT-019-023-030"],
  "Nach dem Ende der Rede zieht Jesus von Galiläa in das Gebiet von Judäa jenseits des Jordan; grosse Menschenmengen folgen ihm, und er heilt sie. Pharisäer fragen ihn, ob ein Mann seine Frau aus jedem Grund entlassen dürfe; er verweist auf die Schöpfung: Was Gott zusammengefügt hat, soll der Mensch nicht trennen; Mose habe das Entlassen wegen ihrer Herzenshärte erlaubt. Wer seine Frau entlässt, ausser wegen Unzucht, und eine andere heiratet, bricht die Ehe. Auf den Einwand der Jünger spricht er von Eunuchen um des Reiches der Himmel willen. Er legt Kindern die Hände auf, denn solchen gehört das Reich der Himmel. Einem jungen Mann, der fragt, was er Gutes tun solle, um ewiges Leben zu erlangen, nennt er die Gebote und sagt ihm, wenn er vollkommen sein wolle, solle er seinen Besitz verkaufen, den Armen geben und ihm nachfolgen; der geht traurig weg. Jesus sagt, ein Reicher komme schwer in das Reich der Himmel, bei Gott aber sei alles möglich. Den Jüngern, die ihm nachgefolgt sind, kündigt er an, sie würden auf zwölf Thronen sitzen, und jedem, der um seines Namens willen Häuser, Angehörige oder Äcker verlassen hat, Hundertfaches und ewiges Leben; viele Erste werden Letzte sein.",
  SEG + " [[MAT.19.30]] leitet zum Gleichnis von den Arbeitern im Weinberg über ([[MAT.20.1]]–[[MAT.20.16]]); die Kapitelgrenze trennt diesen Zusammenhang."),
 ("TU-MAT-019-001-012", "MAT.19.1-MAT.19.12", "dialogue", "Ehe und Scheidung", None,
  "Jesus zieht von Galiläa in das Gebiet von Judäa jenseits des Jordan; grosse Menschenmengen folgen ihm, und er heilt sie dort. Pharisäer fragen ihn, um ihn auf die Probe zu stellen, ob ein Mann seine Frau aus jedem Grund entlassen dürfe. Jesus verweist auf [[GEN.1.27]] und [[GEN.2.24]]: Die zwei sind ein Fleisch; was Gott zusammengefügt hat, soll der Mensch nicht trennen. Auf ihren Einwand mit dem Scheidebrief antwortet er, Mose habe es wegen ihrer Herzenshärte erlaubt, von Anfang an sei es nicht so gewesen; wer seine Frau entlässt, ausser wegen Unzucht, und eine andere heiratet, bricht die Ehe, ebenso wer eine Entlassene heiratet. Die Jünger meinen, dann sei es nicht ratsam zu heiraten; Jesus antwortet, nicht alle fassen dieses Wort, und spricht von Eunuchen von Geburt an, durch Menschen und um des Reiches der Himmel willen.", None),
 ("TU-MAT-019-013-015", "MAT.19.13-MAT.19.15", "narrative", "Jesus und die Kinder", None,
  "Man bringt Kinder zu Jesus, damit er ihnen die Hände auflege und bete; die Jünger fahren sie an. Jesus sagt, sie sollen die Kinder zu ihm kommen lassen und sie nicht hindern, denn solchen gehöre das Reich der Himmel. Er legt ihnen die Hände auf und zieht weiter.", None),
 ("TU-MAT-019-016-022", "MAT.19.16-MAT.19.22", "dialogue", "Der junge Mann mit vielen Gütern", None,
  "Einer fragt Jesus, was er Gutes tun solle, um ewiges Leben zu erlangen. Jesus fragt zurück, was er ihn nach dem Guten frage: Einer ist der Gute; wer in das Leben hineingehen wolle, solle die Gebote halten. Auf die Frage, welche, nennt er Gebote aus den Zehn Geboten und das Gebot der Nächstenliebe. Der junge Mann sagt, er habe das alles gehalten, und fragt, was ihm noch fehle. Jesus sagt: Wenn er vollkommen sein wolle, solle er seinen Besitz verkaufen, ihn den Armen geben und ihm nachfolgen; dann werde er einen Schatz in den Himmeln haben. Der junge Mann geht traurig davon, denn er hat viele Güter.", None),
 ("TU-MAT-019-023-030", "MAT.19.23-MAT.19.30", "dialogue", "Reichtum und der Lohn der Nachfolge", None,
  "Jesus sagt seinen Jüngern, ein Reicher werde schwer in das Reich der Himmel hineinkommen; eher gehe ein Kamel durch ein Nadelöhr als ein Reicher in das Reich Gottes. Die Jünger geraten ausser sich und fragen, wer dann gerettet werden könne; Jesus antwortet, bei Menschen sei das unmöglich, bei Gott aber sei alles möglich. Petrus sagt, sie hätten alles verlassen und seien ihm nachgefolgt, und fragt, was ihnen zuteilwerde. Jesus kündigt an, in der Neuschöpfung, wenn der Menschensohn auf dem Thron seiner Herrlichkeit sitzt, würden sie auf zwölf Thronen sitzen und die zwölf Stämme Israels richten; jeder, der um seines Namens willen Häuser, Angehörige oder Äcker verlassen hat, werde Hundertfaches empfangen und ewiges Leben erben. Viele Erste werden Letzte sein und Letzte Erste.", None),
]
UNITS_GSW = {
 "TU-MAT-018-001-035": ("D Red vom Läbe i de Gmeind", "D Jünger fröged, wer im Riich vo de Himel de Gröscht sig. De Jesus stellt es Chind i iri Mitti: Wer sich nöd umwändet und nöd wie d Chind wird, chunnt nöd ine; wer sich chlii macht wie das Chind, isch de Gröscht. Er warnt devor, eine vo dene Chliine z Fall z bringe oder z verachte: Wie en Mänsch s eint Schaf suecht, wo sich verloffe hät, eso wott de Vatter i de Himel nöd, dass eis vo ine verlore gaat. Wänn en Brueder sündiget, söll me en zerscht elei zur Red stelle, dänn mit Züge, dänn vor de Gmeind; was d Jünger uf de Ärde binded und löösed, wird im Himel bunde und glööst sii, und wo zwei oder drüü i sim Name versammlet sind, isch er mitten under ine. Uf d Frag vom Petrus, öb er bis sibe Mal söll vergää, antwortet de Jesus: bis sibenesibezg Mal, und verzellt vom Chnächt, wo sin Herr ihm e riisigi Schuld erlaat, wo aber sälber sim Mitchnächt e chliini nöd erlaat und drum de Folterchnächt usgliferet wird: Eso macht s au de himmlisch Vatter mit dene, wo nöd vo Härze vergänd. [[MAT.18.11]] fehlt im SBLGNT."),
 "TU-MAT-018-001-005": ("Wer isch de Gröscht?", "D Jünger fröged de Jesus, wer im Riich vo de Himel de Gröscht sig. Er rüeft es Chind zu sich, stellt s i iri Mitti und seit: Wänn si sich nöd umwänded und wie d Chind wärded, chömed si nöd is Riich vo de Himel ine; wer sich chlii macht wie das Chind, isch det de Gröscht, und wer es settigs Chind i sim Name ufnimmt, nimmt ihn uf."),
 "TU-MAT-018-006-009": ("Wehe däm, wo de Fallstrick dur ihn chunnt", "Wer eine vo dene Chliine, wo a de Jesus glaubed, z Fall bringt, für dä wär s besser, mit eme Mülistei um de Hals im Meer versänkt z wärde. De Jesus rüeft s Wehe über d Wält wäge de Fallstrick, wo unvermeidlich chömed, und über de Mänsch, wo si dur ihn chömed. Wänn Hand, Fuess oder Aug z Fall bringed, söll me si abhaue oder useriisse: Es isch besser, verchrüpplet oder mit eim Aug is Läbe ine z choo, als mit beidne Händ, Füess oder Auge is ewig Füür, i d Höll vom Füür, gworfe z wärde."),
 "TU-MAT-018-010-014": ("S Schaf, wo sich verloffe hät", "De Jesus warnt, keis vo dene Chliine z verachte, dänn iri Ängel gsehnd immer s Gsicht vo sim Vatter i de Himel. Er fröget: Laat en Mänsch, wo vo hundert Schaf eis sich verloffe hät, nöd d nüünenüünzg staa und suecht das eint? Wänn er s findt, fröit er sich über das meh als über di nüünenüünzg. Eso isch es nöd de Wile vom Vatter i de Himel, dass eis vo dene Chliine verlore gaat. [[MAT.18.11]] fehlt im SBLGNT."),
 "TU-MAT-018-015-020": ("Wänn din Brueder sündiget", "Wänn en Brueder gäge öpper sündiget, söll dä en zerscht under vier Auge zur Red stelle; wänn er nöd lost, söll er eine oder zwei mitnää, damit jedi Sach dur zwei oder drüü Züge feschtgstellt wird; wänn er au uf die nöd lost, söll er s de Gmeind säge; wänn er au uf d Gmeind nöd lost, söll de Brueder für ihn sii wie de Heid und de Zöllner. Was d Jünger uf de Ärde binded und löösed, wird im Himel bunde und glööst sii. Wänn zwei vo ine uf de Ärde sich über e Sach einig wärded, wo si drum bitted, wird ine das vom Vatter gää; dänn wo zwei oder drüü i sim Name versammlet sind, isch de Jesus mitten under ine."),
 "TU-MAT-018-021-035": ("Wie mängisch vergää? De Chnächt und sin Mitchnächt", "De Petrus fröget, wie mängisch er sim Brueder söll vergää, öb bis sibe Mal; de Jesus antwortet: bis sibenesibezg Mal. Dänn vergliicht er s Riich vo de Himel mit eme König, wo mit sine Chnächt abrächnet: Eim, wo zäätuusig Talänt schuldet und sich vor ihm niderwirft und um Geduld bittet, erlaat er us Erbarme di ganz Schuld. Dä Chnächt aber packt und würgt en Mitchnächt, wo ihm hundert Denar schuldet, und rüert en trotz sim Flehe is Gfängnis. Wo d Mitchnächt das em Herr verzelled, nännt er en en böse Chnächt, wo hett müese Erbarme ha, wie er sälber mit ihm Erbarme gha heig, und lieferet en de Folterchnächt us, bis er di ganz Schuld zalt heig. Eso, seit de Jesus, macht s au sin himmlisch Vatter mit ine, wänn si nöd jede sim Brueder vo Härze vergänd."),
 "TU-MAT-019-001-030": ("Ee, Chind, Riichtum und de Loon vo de Nachfolg", "Nach em Änd vo de Red gaat de Jesus vo Galiläa is Gebiet vo Judäa änet em Jordan; vil Lüüt folged ihm, und er heilt si. Pharisäer fröged en, öb en Maa sini Frau us jedem Grund dörf entlaa; er verwiist uf d Schöpfig: Was Gott zämegfüegt hät, söll de Mänsch nöd trenne; de Mose heig s Entlaa wäge irem härte Härz erlaubt. Wer sini Frau entlaat, usser wäge Unzucht, und en anderi hüratet, bricht d Ee. Uf de Iiwand vo de Jünger redt er vo Eunuche wäge em Riich vo de Himel. Er leit Chind d Händ uf, dänn settige ghört s Riich vo de Himel. Eme junge Maa, wo fröget, was er Guets söll mache, damit er ewigs Läbe überchunnt, nännt er d Gebot und seit em, wänn er vollkomme sii well, söll er sin Bsitz verchaufe, s de Arme gää und ihm nachefolge; dä gaat truurig wäg. De Jesus seit, en Riiche chömm schwär is Riich vo de Himel, bi Gott aber sig alles möglich. De Jünger, wo ihm nachegfolget sind, seit er aa, si wärdid uf zwölf Throon sitze, und jedem, wo wäge sim Name Hüüser, Aaghörigi oder Äcker verlaa hät, hundertfach und ewigs Läbe; vil Erschti wärded Letschti sii."),
 "TU-MAT-019-001-012": ("Ee und Scheidig", "De Jesus gaat vo Galiläa is Gebiet vo Judäa änet em Jordan; vil Lüüt folged ihm, und er heilt si det. Pharisäer fröged en, für en uf d Prob z stelle, öb en Maa sini Frau us jedem Grund dörf entlaa. De Jesus verwiist uf [[GEN.1.27]] und [[GEN.2.24]]: Di zwei sind ei Fleisch; was Gott zämegfüegt hät, söll de Mänsch nöd trenne. Uf iren Iiwand mit em Scheidigsbrief antwortet er, de Mose heig s wäge irem härte Härz erlaubt, vo Aafang aa sig s nöd eso gsii; wer sini Frau entlaat, usser wäge Unzucht, und en anderi hüratet, bricht d Ee, und au wer eini hüratet, wo entlaa worde isch. D Jünger meined, dänn sig s nöd ratsam z hürate; de Jesus antwortet, nöd alli chönd das Wort fasse, und redt vo Eunuche vo Geburt aa, dur Mänsche und wäge em Riich vo de Himel."),
 "TU-MAT-019-013-015": ("De Jesus und d Chind", "Me bringt Chind zum Jesus, damit er ine d Händ uflegi und bäti; d Jünger fahred si aa. De Jesus seit, si söled d Chind zu ihm choo laa und si nöd hindere, dänn settige ghör s Riich vo de Himel. Er leit ine d Händ uf und gaat wiiter."),
 "TU-MAT-019-016-022": ("De jung Maa mit vil Bsitz", "Eine fröget de Jesus, was er Guets söll mache, damit er ewigs Läbe überchunnt. De Jesus fröget zrugg, werum er en nach em Guete fröget: Eine isch de Guet; wer is Läbe ine choo well, söll d Gebot halte. Uf d Frag, weli, nännt er Gebot us de Zäh Gebot und s Gebot vo de Nächschteliebi. De jung Maa seit, er heig das alles ghalte, und fröget, was em no fehli. De Jesus seit: Wänn er vollkomme sii well, söll er sin Bsitz verchaufe, s de Arme gää und ihm nachefolge; dänn heig er en Schatz i de Himel. De jung Maa gaat truurig devo, dänn er hät vil Bsitz."),
 "TU-MAT-019-023-030": ("Riichtum und de Loon vo de Nachfolg", "De Jesus seit sine Jünger, en Riiche chömm schwär is Riich vo de Himel ine; ender gieng es Kamel dur es Nadelööhr als en Riiche is Riich vo Gott. D Jünger sind usser sich und fröged, wer dänn chönn grettet wärde; de Jesus antwortet, bi Mänsche sig das unmöglich, bi Gott aber sig alles möglich. De Petrus seit, si heigid alles verlaa und sigid ihm nachegfolget, und fröget, was si defür überchömed. De Jesus seit aa, i de Neuschöpfig, wänn de Mänschesohn uf em Throon vo sinere Herrlichkeit sitzt, wärdid si uf zwölf Throon sitze und di zwölf Stämm vo Israel richte; jede, wo wäge sim Name Hüüser, Aaghörigi oder Äcker verlaa hät, wärdi hundertfach übercho und ewigs Läbe erbe. Vil Erschti wärded Letschti sii und Letschti Erschti."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "Widerspricht die automatische Zuordnung den Sigla des Apparats, gilt der Apparat (so bei [[MAT.18.11]]). "
  "Zahlen zu Wortvorkommen sind per Skript aus den SBLGNT-Tokens (Wortformen) gezählt."),
 ("Einheitliche Begriffe für das ganze Matthäusevangelium (gemeinsame Festlegung aller Matthäus-Bereiche): ἡ βασιλεία τῶν "
  "οὐρανῶν «das Reich der Himmel», ἡ βασιλεία τοῦ θεοῦ «das Reich Gottes» ([[MAT.19.24]]); ὁ υἱὸς τοῦ ἀνθρώπου «der "
  "Menschensohn»; ἀμὴν λέγω ὑμῖν «Amen, ich sage euch»; ὁ πατὴρ ὁ ἐν οὐρανοῖς «der Vater in den Himmeln», ὁ οὐράνιος "
  "«himmlisch»; ἰδού «siehe»; τότε «da»; Pharisäer; ἐκκλησία «Gemeinde»; Ortsnamen Galiläa, Judäa, Jordan."),
 ("Einheitlich für das ganze Evangelium, in diesem Bereich verwendet: σκανδαλίζω aktiv «zu Fall bringen», σκάνδαλον «Fallstrick»; "
  "προσέρχομαι «herantreten»; προσκυνέω «sich niederwerfen»; σπλαγχνίζομαι «Erbarmen haben»; οἱ ὄχλοι «die Menschenmengen»; "
  "δοῦλος «Knecht». Weitere Entscheide dieses Bereichs (begründet in decisions): ἀφίημι bei Schuld «vergeben» (wie im Vaterunser, [[MAT.6.12]]), bei Geldschuld "
  "«erlassen»; ἀδελφός als Glied der Gemeinschaft «Bruder»; δοῦλος «Knecht», σύνδουλος «Mitknecht», κύριος im Gleichnis "
  "«Herr»; ἐν οὐρανοῖς (Mehrzahl) «in den Himmeln», ἐν οὐρανῷ (Einzahl) «im Himmel»; γέεννα «Hölle» (wie Markus); "
  "ἀπολύω τὴν γυναῖκα «die Frau entlassen» (wie Markus); πορνεία «Unzucht»; στρέφομαι «sich umwenden» (zur Unterscheidung "
  "von μετανοέω «umkehren»); οἱ μικροὶ οὗτοι «diese Kleinen»; ζωὴ αἰώνιος «ewiges Leben»; εἰσέρχομαι εἰς τὴν βασιλείαν "
  "«in das Reich hineinkommen»."),
 ("Abgrenzung: Kapitel 18 ist die vierte der fünf grossen Reden; die Rede Jesu läuft von [[MAT.18.3]] bis [[MAT.18.20]] "
  "und nach der Frage des Petrus von [[MAT.18.22]] bis [[MAT.18.35]]. Wie alle grossen Reden steht sie ohne äussere "
  "Anführungszeichen (vgl. [[MAT.6.5-MAT.6.15]]); Reden innerhalb des Gleichnisses stehen in « ». "
  "[[MAT.19.1]] schliesst die Rede mit der Formel «Und es geschah, als Jesus diese Worte beendet hatte». [[MAT.19.30]] "
  "gehört sachlich zum folgenden Gleichnis ([[MAT.20.1]]–[[MAT.20.16]])."),
 ("Parallelen: [[MAT.18.1]]–[[MAT.18.9]] entspricht [[MRK.9.33]]–[[MRK.9.48]], [[MAT.19.1]]–[[MAT.19.30]] entspricht "
  "[[MRK.10.1]]–[[MRK.10.31]]. Gleiche griechische Wendungen sind möglichst gleich übersetzt wie dort (z. B. «ein grosser "
  "Mühlstein», «entlassen», «Herzenshärte», «ein Fleisch»); wo Matthäus anders formuliert, folgt die Übersetzung seinem "
  "Wortlaut (z. B. [[MAT.19.17]] «Was fragst du mich nach dem Guten?»)."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT gegen WH, Treg und NA28 liest (z. B. [[MAT.19.29]] "
  "«oder Frau»). Abweichende Lesarten stehen als Alternativen, soweit sie die Übersetzung verändern. [[MAT.18.11]] steht "
  "nicht im SBLGNT und hat keinen Übersetzungstext; der Wortlaut steht als Alternative bei [[MAT.18.10]]. Die Lesart von "
  "RP in [[MAT.19.17]] («Was nennst du mich gut? Niemand ist gut ausser einem: Gott») verzeichnet der SBLGNT-Apparat, sie "
  "fehlt aber in den importierten Variantendaten; sie ist deshalb in decisions genannt, nicht als Alternative geführt."),
 ("Erzählweise: Das erzählende Präsens (λέγει «sagt») ist beibehalten. ὅτι vor direkter Rede ist nicht eigens übersetzt. "
  "Anführungszeichen sind eine Entscheidung der Übersetzung, denn das Griechische hat keine."),
 "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte. Wo si em Apparat widerspricht, gilt de Apparat."),
 ("Iiheitlichi Begriff fürs ganz Matthäusevangelium: «s Riich vo de Himel», «s Riich vo Gott»; «de Mänschesohn»; «Amen, "
  "ich säg eu»; «de Vatter i de Himel», «himmlisch»; «lueg»; «dänn»; «Gmeind». Au: σκανδαλίζω «z Fall "
  "bringe», σκάνδαλον «Fallstrick»; προσέρχομαι «härechoo»; προσκυνέω «sich niderwärfe»; οἱ ὄχλοι «d Lüüt»; ἀφίημι «vergää», bi Gäldschuld «erlaa»; ἀδελφός «Brueder»; δοῦλος «Chnächt», "
  "σύνδουλος «Mitchnächt»; ἐν οὐρανοῖς «i de Himel», ἐν οὐρανῷ «im Himel»; γέεννα «Höll»; ἀπολύω «entlaa»; πορνεία "
  "«Unzucht»; στρέφομαι «sich umwände»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Petrus»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«s Riich vo de Himel»); kei Futur, wo s d Mundart nöd brucht. D Red i Kapitel 18 staat ohni ussereri Aafüerigszeiche; "
  "Rede im Gliichnis stönd i « »."),
 ("[[MAT.18.11]] staat nöd im SBLGNT und hät kein Text; de Wortlut staat als Alternative bi [[MAT.18.10]]. D Läsart vo RP "
  "i [[MAT.19.17]] staat i de decisions."),
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
        all_refs = [f"MAT.{c}.{v}" for v in range(1, last + 1)]
        missing = {r for r in all_refs if r not in toks}
        if missing != {r for r in NO_TOKENS if r.startswith(f"MAT.{c}.")}:
            raise SystemExit(f"MAT {c}: unerwartet fehlende Verse {sorted(missing)}")
        refs_c = [r for r in all_refs if r in toks]
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Riich, Lüüt), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Namen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; Begriffe einheitlich für das ganze Matthäusevangelium (translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_18_19.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 18–19 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
