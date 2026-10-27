#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 22–23 (Gleichnis vom Hochzeitsmahl, Streitgespräche, Rede gegen die Schriftgelehrten
und Pharisäer, Klage über Jerusalem) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_22_23.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- [[MAT.23.14]] (verbreitete Zählung) fehlt im SBLGNT und hat keine Tokens; der Vers wird nicht übersetzt. Sein
  Wortlaut steht als Alternative bei [[MAT.23.12]] (Stellung bei RP) und [[MAT.23.13]] (Stellung im TR).
- Begriffe nach der gemeinsamen Matthäus-Tabelle; für diesen Bereich neu festgelegte Wiedergaben stehen in
  translation_notes.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1),
nicht aus eigener Prüfung der Handschriften.
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
CHAPTERS = ((22, 46), (23, 39))
MISSING = {"MAT.23.14"}

DE = {
 # ------------------------------------------------------------ Kapitel 22
 "MAT.22.1": "Und{1} [Jesus]{3,4} [antwortete]{2} und [redete]{6} [wieder]{5} [in]{7} [Gleichnissen]{8} [zu ihnen]{9}: ~10(λέγων «sagend» leitet die direkte Rede ein)",
 "MAT.22.2": "«[Das Reich]{2,3} [der Himmel]{4,5} [ist]{1} [einem König]{6,7} [gleich geworden]{1}, [der]{8} [für]{11} [seinen]{13} [Sohn]{12} [ein Hochzeitsfest]{10} [ausrichtete]{9}.",
 "MAT.22.3": "Und{1} [er sandte]{2} [seine]{5} [Knechte]{3,4} [aus]{2}, [um]{6} [die]{7} [Geladenen]{8} [zum]{9,10} [Hochzeitsfest]{11} [zu rufen]{6}; und{12} [sie wollten]{14} [nicht]{13} [kommen]{15}.",
 "MAT.22.4": "[Wieder]{1} [sandte er]{2} [andere]{3} [Knechte]{4} [aus]{2} und [sagte]{5}: ‹[Sagt]{6} [den]{7} [Geladenen]{8}: [Siehe]{9}, [ich habe]{13} [mein]{12} [Mahl]{10,11} [bereitet]{13}, [meine]{16} [Ochsen]{14,15} und{17} [das]{18} [Mastvieh]{19} [sind geschlachtet]{20}, und{21} [alles]{22} [ist bereit]{23}. [Kommt]{24} [zum]{25,26} [Hochzeitsfest]{27}!›",
 "MAT.22.5": "[Sie]{1} [aber]{2} [kümmerten sich nicht darum]{3} und [gingen weg]{4}, [der eine]{5,6} [auf]{7} [seinen eigenen]{8,9} [Acker]{10}, [der andere]{11,12} [zu]{13} [seinem]{14,16} [Geschäft]{15}.",
 "MAT.22.6": "[Die]{1} [übrigen]{3} [aber]{2} [ergriffen]{4} [seine]{7} [Knechte]{5,6}, [misshandelten]{8} und{9} [töteten]{10} sie.",
 "MAT.22.7": "[Der König]{1,3} [aber]{2} [wurde zornig]{4}, und{5} [er schickte]{6} [seine]{9} [Truppen]{7,8}, [brachte]{10} [jene]{13} [Mörder]{11,12} [um]{10} und{14} [zündete]{18} [ihre]{17} [Stadt]{15,16} [an]{18}.",
 "MAT.22.8": "[Dann]{1} [sagt er]{2} [zu seinen]{3,5} [Knechten]{4}: ‹[Das Hochzeitsfest]{6,8} [ist]{10} [zwar]{7} [bereit]{9}, [die]{11} [Geladenen]{13} [aber]{12} [waren]{15} es [nicht]{14} [wert]{16}.",
 "MAT.22.9": "[Geht]{1} [also]{2} [an]{3} [die]{4} [Ausgänge]{5} [der Strassen]{6,7}, und{8} [ladet]{12} [alle, die]{9} [ihr findet]{11}, [zum]{13,14} [Hochzeitsfest]{15} [ein]{12}!› ~10(ἐάν verallgemeinert «alle, die»; nicht eigens wiedergegeben)",
 "MAT.22.10": "Und{1} [jene]{5} [Knechte]{3,4} [gingen hinaus]{2} [auf]{6} [die]{7} [Strassen]{8} und [brachten]{9} [alle]{10} [zusammen]{9}, [die]{11} [sie fanden]{12}, [Böse]{13} [und]{14,15} [Gute]{16}; und{17} [das Hochzeitsfest]{19,20} [füllte sich]{18} [mit Gästen]{21}.",
 "MAT.22.11": "[Als]{1} [aber]{2} [der König]{3,4} [hereinkam]{1}, [um]{5} [die Gäste]{6,7} [anzusehen]{5}, [sah er]{8} [dort]{9} [einen Menschen]{10}, [der]{12} [kein]{11} [Hochzeitskleid]{13,14} [anhatte]{12}.",
 "MAT.22.12": "Und{1} [er sagt]{2} [zu ihm]{3}: ‹[Freund]{4}, [wie]{5} [bist du]{6} [hier]{7} [hereingekommen]{6}, [ohne]{8} [ein Hochzeitskleid]{10,11} [zu haben]{9}?› [Er]{12} [aber]{13} [verstummte]{14}.",
 "MAT.22.13": "[Da]{1} [sagte]{4} [der König]{2,3} [zu den]{5} [Dienern]{6}: ‹[Bindet]{7} [ihm]{8} [Füsse]{9} und{10} [Hände]{11} und [werft]{12} [ihn]{13} [hinaus]{12} [in]{14} [die]{15} [Finsternis]{16} [draussen]{17,18}! [Dort]{19} [wird]{20} [das Weinen]{21,22} und{23} [das Zähneknirschen]{24-27} [sein]{20}.›",
 "MAT.22.14": "[Denn]{2} [viele]{1} [sind]{3} [eingeladen]{4}, [wenige]{5} [aber]{6} [auserwählt]{7}.»",
 "MAT.22.15": "[Da]{1} [gingen]{2} [die Pharisäer]{3,4} [hin]{2} und [berieten sich]{5,6}, [wie]{7} [sie]{9} [ihn]{8} [mit]{10} [einer Aussage]{11} [in eine Falle locken könnten]{9}.",
 "MAT.22.16": "Und{1} [sie schicken]{2} [ihre]{6} [Jünger]{4,5} [mit]{7} [den Herodianern]{8,9} [zu ihm]{3}, [die sagen]{10}: «[Lehrer]{11}, [wir wissen]{12}, [dass]{13} [du]{15} [wahrhaftig]{14} [bist]{15} und{16} [den Weg]{17,18} [Gottes]{19,20} [in]{21} [Wahrheit]{22} [lehrst]{23}, und{24} [du]{27} [kümmerst dich]{26} [um]{28} [niemanden]{25,29}; [denn]{31} [du siehst]{32} [nicht]{30} [auf]{33} [das Ansehen]{34} [der Menschen]{35}.",
 "MAT.22.17": "[Sag]{1} [uns]{3} [also]{2}: [Was]{4} [meinst]{6} [du]{5}? [Ist es erlaubt]{7}, [dem Kaiser]{10} [Steuer]{9} [zu zahlen]{8}, [oder]{11} [nicht]{12}?»",
 "MAT.22.18": "[Jesus]{3,4} [aber]{2} [erkannte]{1} [ihre]{7} [Bosheit]{5,6} und [sagte]{8}: «[Warum]{9} [stellt ihr]{11} [mich]{10} [auf die Probe]{11}, [ihr Heuchler]{12}?",
 "MAT.22.19": "[Zeigt]{1} [mir]{2} [die]{3} [Münze]{4} [für die Steuer]{5,6}!» [Sie]{7} [aber]{8} [brachten]{9} [ihm]{10} [einen Denar]{11}.",
 "MAT.22.20": "Und{1} [er sagt]{2} [zu ihnen]{3}: «[Wessen]{4} [Bild]{5,6} und{8} [Aufschrift]{9,10} [ist das]{7}?»",
 "MAT.22.21": "[Sie sagen]{1} [zu ihm]{2}: «[Des Kaisers]{3}.» [Da]{4} [sagt er]{5} [zu ihnen]{6}: «[Gebt]{7} [also]{8}, [was]{9} [des Kaisers]{10} ist, [dem Kaiser]{11}, und{12} [was]{13} [Gottes]{14,15} ist, [Gott]{16,17}!»",
 "MAT.22.22": "Und{1} [als sie das hörten]{2}, [staunten sie]{3}; und{4} [sie liessen]{5} [ihn]{6} [stehen]{5} und [gingen weg]{7}.",
 "MAT.22.23": "[An]{1} [jenem]{2} [Tag]{3,4} [traten]{5} [Sadduzäer]{7} [zu ihm]{6} [heran]{5}, [die sagen]{8}, [es gebe]{10} [keine]{9} [Auferstehung]{11}, und{12} [sie fragten]{13} [ihn]{14}",
 "MAT.22.24": "[und sagten]{1}: «[Lehrer]{2}, [Mose]{3} [hat gesagt]{4}: ‹[Wenn]{5} [jemand]{6} [stirbt]{7}, [ohne]{8} [Kinder]{10} [zu haben]{9}, [soll]{11} [sein]{14} [Bruder]{12,13} [seine]{17} [Frau]{15,16} [heiraten]{11} und{18} [seinem]{23} [Bruder]{21,22} [Nachkommen]{20} [erwecken]{19}.›",
 "MAT.22.25": "[Es waren]{1} [aber]{2} [bei]{3} [uns]{4} [sieben]{5} [Brüder]{6}. Und{7} [der erste]{8,9} [heiratete]{10} und [starb]{11}, und{12} [weil er]{14} [keine]{13} [Nachkommen]{15} [hatte]{14}, [hinterliess er]{16} [seine]{19} [Frau]{17,18} [seinem]{22} [Bruder]{20,21}.",
 "MAT.22.26": "[Ebenso]{1} [auch]{2} [der zweite]{3,4} und{5} [der dritte]{6,7}, [bis]{8} [zum]{9} [siebten]{10}.",
 "MAT.22.27": "[Zuletzt]{1} [aber]{2}, [nach allen]{3}, [starb]{4} [die Frau]{5,6}.",
 "MAT.22.28": "[In]{1} [der Auferstehung]{2,3} [nun]{4}: [Wessen]{5} [Frau]{9} [von den]{6} [sieben]{7} [wird sie sein]{8}? [Denn]{11} [alle]{10} [haben]{12} [sie]{13} zur Frau [gehabt]{12}.»",
 "MAT.22.29": "[Jesus]{3,4} [aber]{2} [antwortete]{1} und [sagte]{5} [zu ihnen]{6}: «[Ihr irrt]{7}, [weil ihr]{9} [weder]{8} [die Schriften]{10,11} [kennt]{9} [noch]{12} [die Kraft]{13,14} [Gottes]{15,16}.",
 "MAT.22.30": "[Denn]{2} [in]{1} [der Auferstehung]{3,4} [heiraten sie]{6} [weder]{5}, [noch]{7} [werden sie verheiratet]{8}, [sondern]{9} [sie sind]{16} [wie]{10} [Engel]{11} [Gottes]{12} [im]{13,14} [Himmel]{15}.",
 "MAT.22.31": "[Was]{1} [aber]{2} [die Auferstehung]{3,4} [der Toten]{5,6} [betrifft]{1}: [Habt ihr]{8} [nicht]{7} [gelesen]{8}, [was]{9} [euch]{11} [von]{12} [Gott]{13,14} [gesagt worden ist]{10}, [der spricht]{15}:",
 "MAT.22.32": "‹[Ich]{1} [bin]{2} [der Gott]{3,4} [Abrahams]{5} und{6} [der Gott]{7,8} [Isaaks]{9} und{10} [der Gott]{11,12} [Jakobs]{13}›? [Er ist]{15} [nicht]{14} [der Gott]{16,17} [von Toten]{18}, [sondern]{19} [von Lebenden]{20}.»",
 "MAT.22.33": "Und{1} [als]{2} [die Menschenmengen]{3,4} [das hörten]{2}, [waren sie überwältigt]{5} [von]{6} [seiner]{9} [Lehre]{7,8}.",
 "MAT.22.34": "[Als]{4} [aber]{2} [die Pharisäer]{1,3} [hörten]{4}, [dass]{5} [er]{6} [die Sadduzäer]{7,8} [zum Schweigen gebracht hatte]{6}, [versammelten sie sich]{9} [am selben Ort]{10-12}.",
 "MAT.22.35": "Und{1} [einer]{3} [von]{4} [ihnen]{5}, [ein Gesetzeslehrer]{6}, [fragte]{2}, [um]{7} [ihn]{8} [auf die Probe zu stellen]{7}:",
 "MAT.22.36": "«[Lehrer]{1}, [welches]{2} [Gebot]{3} [ist das grösste]{4} [im]{5,6} [Gesetz]{7}?»",
 "MAT.22.37": "[Er]{1} [aber]{2} [sagte]{3} [zu ihm]{4}: «‹[Du sollst]{5} [den Herrn]{6}, [deinen]{9} [Gott]{7,8}, [lieben]{5} [mit]{10} [deinem]{14} [ganzen]{11} [Herzen]{12,13} und{15} [mit]{16} [deiner]{20} [ganzen]{17} [Seele]{18,19} und{21} [mit]{22} [deinem]{26} [ganzen]{23} [Denken]{24,25}.›",
 "MAT.22.38": "[Das]{1} [ist]{2} [das]{3} [grösste]{4} und{5} [erste]{6} [Gebot]{7}.",
 "MAT.22.39": "[Das zweite]{1} [aber]{2} [ist]{3} [ihm]{4} [gleich]{3}: ‹[Du sollst]{5} [deinen]{6,8} [Nächsten]{7} [lieben]{5} [wie]{9} [dich selbst]{10}.›",
 "MAT.22.40": "[An]{1} [diesen]{2,3} [zwei]{4} [Geboten]{5} [hängen]{9} [das ganze]{6,7} [Gesetz]{8} und{10} [die Propheten]{11,12}.»",
 "MAT.22.41": "[Als]{1} [aber]{2} [die Pharisäer]{3,4} [versammelt waren]{1}, [fragte]{5} [Jesus]{7,8} [sie]{6}",
 "MAT.22.42": "[und sagte]{1}: «[Was]{2} [meint]{4} [ihr]{3} [über]{5} [den Christus]{6,7}? [Wessen]{8} [Sohn]{9} [ist er]{10}?» [Sie sagen]{11} [zu ihm]{12}: «[Davids]{13,14}.»",
 "MAT.22.43": "[Er sagt]{1} [zu ihnen]{2}: «[Wie]{3} [nennt]{8} [ihn]{9} [dann]{4} [David]{5} [im]{6} [Geist]{7} ‹[Herr]{10}›, [wenn er sagt]{11}:",
 "MAT.22.44": "‹[Der Herr]{2} [sprach]{1} [zu meinem]{3,5} [Herrn]{4}: [Setze dich]{6} [zu]{7} [meiner]{9} [Rechten]{8}, [bis]{10,11} [ich]{12} [deine]{15} [Feinde]{13,14} [unter]{16} [deine]{19} [Füsse]{17,18} [lege]{12}›?",
 "MAT.22.45": "[Wenn]{1} [nun]{2} [David]{3} [ihn]{5} ‹[Herr]{6}› [nennt]{4}, [wie]{7} [ist er]{10} dann [sein]{9} [Sohn]{8}?»",
 "MAT.22.46": "Und{1} [niemand]{2} [konnte]{3} [ihm]{5} [ein Wort]{6} [antworten]{4}, und [von]{10} [jenem]{11} [Tag]{12,13} [an]{10} [wagte]{8} es [auch]{7} [keiner]{9} [mehr]{16}, [ihn]{15} [zu fragen]{14}.",
 # ------------------------------------------------------------ Kapitel 23
 "MAT.23.1": "[Da]{1} [redete]{4} [Jesus]{2,3} [zu den]{5} [Menschenmengen]{6} und{7} [zu seinen]{8,10} [Jüngern]{9}",
 "MAT.23.2": "[und sagte]{1}: [Auf]{2} [den]{3} [Stuhl]{5} [des Mose]{4} [haben sich]{6} [die Schriftgelehrten]{7,8} und{9} [die Pharisäer]{10,11} [gesetzt]{6}.",
 "MAT.23.3": "[Alles]{1} [nun]{2}, [was]{3} [sie]{5} [euch]{6} [sagen]{5}, [das tut]{7} und{8} [haltet]{9}; [nach]{10} [ihren]{14} [Werken]{12,13} [aber]{11} [handelt]{16} [nicht]{15}; [denn]{18} [sie reden]{17} und{19} [tun es]{21} [nicht]{20}. ~4(ἐάν verallgemeinert «alles, was»; nicht eigens wiedergegeben)",
 "MAT.23.4": "[Sie schnüren]{1} [aber]{2} [schwere]{4} [Lasten]{3} [zusammen]{1} und{5} [legen]{6} sie [den Menschen]{10,11} [auf]{7} [die Schultern]{8,9}; [sie selbst]{12} [aber]{13} [wollen]{18} [sie]{20} [mit]{14} [ihrem]{16} [Finger]{15} [nicht]{17} [bewegen]{19}.",
 "MAT.23.5": "[Alle]{1} [ihre]{5} [Werke]{3,4} [aber]{2} [tun sie]{6}, [um]{7,8} [von den Menschen]{10,11} [gesehen zu werden]{9}; [denn]{13} [sie machen]{12} [ihre]{16} [Gebetsriemen]{14,15} [breit]{12} und{17} [die Quasten]{19,20} [lang]{18}.",
 "MAT.23.6": "[Sie lieben]{1} [aber]{2} [den]{3} [Ehrenplatz]{4} [bei]{5} [den]{6} [Gastmählern]{7} und{8} [die]{9} [Ehrensitze]{10} [in]{11} [den]{12} [Synagogen]{13}",
 "MAT.23.7": "und{1} [die]{2} [Begrüssungen]{3} [auf]{4} [den]{5} [Marktplätzen]{6} und{7} [von]{9} [den Menschen]{10,11} «[Rabbi]{12}» [genannt zu werden]{8}.",
 "MAT.23.8": "[Ihr]{1} [aber]{2} [sollt euch]{4} [nicht]{3} «[Rabbi]{5}» [nennen lassen]{4}; [denn]{7} [einer]{6} [ist]{8} [euer]{9} [Lehrer]{10,11}, [ihr]{14} [alle]{12} [aber]{13} [seid]{16} [Brüder]{15}.",
 "MAT.23.9": "Und{1} [nennt]{4} [keinen]{3} [auf]{6} [der Erde]{7,8} [euren]{5} [Vater]{2}; [denn]{10} [einer]{9} [ist]{11} [euer]{12} [Vater]{13,14}, [der himmlische]{15,16}.",
 "MAT.23.10": "[Lasst euch]{2} [auch nicht]{1} «[Lehrmeister]{3}» [nennen]{2}; [denn]{4} [einer]{8} [ist]{7} [euer]{6} [Lehrmeister]{5}, [der Christus]{9,10}.",
 "MAT.23.11": "[Der Grösste]{1,3} [unter euch]{4} [aber]{2} [soll]{5} [euer]{6} [Diener]{7} [sein]{5}.",
 "MAT.23.12": "[Wer]{1} [sich]{4} [aber]{2} [selbst]{4} [erhöht]{3}, [wird erniedrigt werden]{5}, und{6} [wer]{7} [sich selbst]{9} [erniedrigt]{8}, [wird erhöht werden]{10}.",
 "MAT.23.13": "[Wehe]{1} [aber]{2} [euch]{3}, [Schriftgelehrte]{4} und{5} [Pharisäer]{6}, [ihr Heuchler]{7}, [denn]{8} [ihr verschliesst]{9} [das Reich]{10,11} [der Himmel]{12,13} [vor]{14} [den Menschen]{15,16}! [Ihr]{17} selbst [geht]{20} [ja]{18} [nicht]{19} [hinein]{20}, [und]{21} [die, die]{22} [hineinwollen]{23}, [lasst ihr]{24} [nicht]{21} [hineingehen]{25}.",
 "MAT.23.15": "[Wehe]{1} [euch]{2}, [Schriftgelehrte]{3} und{4} [Pharisäer]{5}, [ihr Heuchler]{6}, [denn]{7} [ihr durchzieht]{8} [das Meer]{9,10} und{11} [das trockene Land]{12,13}, [um]{14} [einen einzigen]{15} [Proselyten]{16} [zu gewinnen]{14}, und{17} [wenn]{18} [er es geworden ist]{19}, [macht ihr]{20} [ihn]{21} [zu einem Sohn]{22} [der Hölle]{23}, [doppelt so schlimm]{24} [wie ihr]{25}!",
 "MAT.23.16": "[Wehe]{1} [euch]{2}, [ihr blinden]{4} [Führer]{3}, [die ihr sagt]{5,6}: «[Wer]{7,8} [beim]{10,11} [Tempel]{12} [schwört]{9}, [das gilt]{14} [nichts]{13}; [wer]{15,17} [aber]{16} [beim]{19,20} [Gold]{21} [des Tempels]{22,23} [schwört]{18}, [ist gebunden]{24}.»",
 "MAT.23.17": "[Ihr Narren]{1} und{2} [Blinden]{3}! [Was]{4} [ist]{7} [denn]{5} [grösser]{6}: [das Gold]{8,9} [oder]{10} [der Tempel]{11,12}, [der]{13} [das Gold]{15,16} [geheiligt hat]{14}?",
 "MAT.23.18": "Und{1}: «[Wer]{2,3} [beim]{5,6} [Altar]{7} [schwört]{4}, [das gilt]{9} [nichts]{8}; [wer]{10,12} [aber]{11} [bei]{14} [der Gabe]{15,16} [schwört]{13}, [die]{17} [darauf]{18,19} liegt, [ist gebunden]{20}.»",
 "MAT.23.19": "[Ihr Blinden]{1}! [Was]{2} ist [denn]{3} [grösser]{4}: [die Gabe]{5,6} [oder]{7} [der Altar]{8,9}, [der]{10} [die Gabe]{12,13} [heiligt]{11}?",
 "MAT.23.20": "[Wer]{1} [also]{2} [beim]{4,5} [Altar]{6} [schwört]{3}, [schwört]{7} [bei]{8} [ihm]{9} und{10} [bei]{11} [allem]{12}, [was]{13} [darauf]{14,15} liegt.",
 "MAT.23.21": "Und{1} [wer]{2} [beim]{4,5} [Tempel]{6} [schwört]{3}, [schwört]{7} [bei]{8} [ihm]{9} und{10} [bei]{11} [dem, der]{12} [ihn]{14} [bewohnt]{13}.",
 "MAT.23.22": "Und{1} [wer]{2} [beim]{4,5} [Himmel]{6} [schwört]{3}, [schwört]{7} [beim]{8,9} [Thron]{10} [Gottes]{11,12} und{13} [bei]{14} [dem, der]{15} [darauf]{17,18} [sitzt]{16}.",
 "MAT.23.23": "[Wehe]{1} [euch]{2}, [Schriftgelehrte]{3} und{4} [Pharisäer]{5}, [ihr Heuchler]{6}, [denn]{7} [ihr gebt den Zehnten]{8} [von der]{9} [Minze]{10} und{11} [dem]{12} [Dill]{13} und{14} [dem]{15} [Kümmel]{16} und{17} [habt]{18} [das Gewichtigere]{19,20} [des Gesetzes]{21,22} [beiseitegelassen]{18}: [das Recht]{23,24} und{25} [die Barmherzigkeit]{26,27} und{28} [die Treue]{29,30}! [Dies]{31} [hätte man]{32} [tun]{33} [und jenes]{34} [nicht]{35} [beiseitelassen]{36} [sollen]{32}.",
 "MAT.23.24": "[Ihr blinden]{2} [Führer]{1}, [die ihr]{3} [die Mücke]{5,6} [aussiebt]{4}, [das Kamel]{7,9} [aber]{8} [verschluckt]{10}!",
 "MAT.23.25": "[Wehe]{1} [euch]{2}, [Schriftgelehrte]{3} und{4} [Pharisäer]{5}, [ihr Heuchler]{6}, [denn]{7} [ihr reinigt]{8} [das Äussere]{9,10} [des Bechers]{11,12} und{13} [der Schüssel]{14,15}, [innen]{16} [aber]{17} [sind sie voll]{18} [von]{19} [Raub]{20} und{21} [Masslosigkeit]{22}!",
 "MAT.23.26": "[Du blinder]{2} [Pharisäer]{1}! [Reinige]{3} [zuerst]{4} [das Innere]{5,6} [des Bechers]{7,8} und{9} [der Schüssel]{10,11}, [damit]{12} [auch]{14} [sein]{17} [Äusseres]{15,16} [rein]{18} [wird]{13}.",
 "MAT.23.27": "[Wehe]{1} [euch]{2}, [Schriftgelehrte]{3} und{4} [Pharisäer]{5}, [ihr Heuchler]{6}, [denn]{7} [ihr gleicht]{8} [weiss getünchten]{10} [Gräbern]{9}, [die]{11} [aussen]{12} [zwar]{13} [schön]{15} [aussehen]{14}, [innen]{16} [aber]{17} [voll sind]{18} [von Totengebeinen]{19,20} und{21} [von aller]{22} [Unreinheit]{23}!",
 "MAT.23.28": "[So]{1} [erscheint]{6} [auch]{2} [ihr]{3} [aussen]{4} [zwar]{5} [den Menschen]{7,8} [gerecht]{9}, [innen]{10} [aber]{11} [seid ihr]{12} [voll]{13} [Heuchelei]{14} und{15} [Gesetzlosigkeit]{16}.",
 "MAT.23.29": "[Wehe]{1} [euch]{2}, [Schriftgelehrte]{3} und{4} [Pharisäer]{5}, [ihr Heuchler]{6}, [denn]{7} [ihr baut]{8} [die Gräber]{9,10} [der Propheten]{11,12} und{13} [schmückt]{14} [die Grabmäler]{15,16} [der Gerechten]{17,18}",
 "MAT.23.30": "und{1} [sagt]{2}: «[Wenn]{3} [wir]{4} [in]{5} [den Tagen]{6,7} [unserer]{10} [Väter]{8,9} [gelebt hätten]{4}, [wären wir]{12,13} [nicht]{11} [mit ihnen]{14} [am]{16,17} [Blut]{18} [der Propheten]{19,20} [beteiligt]{15} [gewesen]{12,13}.»",
 "MAT.23.31": "[Damit]{1} [bezeugt ihr]{2} [euch selbst]{3}, [dass]{4} [ihr]{6} [Söhne]{5} [derer]{7} [seid]{6}, die [die Propheten]{9,10} [ermordet haben]{8}.",
 "MAT.23.32": "Und{1} [ihr]{2}: [Macht]{3} [das Mass]{4,5} [eurer]{8} [Väter]{6,7} [voll]{3}!",
 "MAT.23.33": "[Ihr Schlangen]{1}, [ihr Vipernbrut]{2,3}! [Wie]{4} [wollt ihr]{5} [dem]{6,7} [Gericht]{8} [der Hölle]{9,10} [entkommen]{5}?",
 "MAT.23.34": "[Darum]{1,2}, [siehe]{3}, [ich]{4} [sende]{5} [zu]{6} [euch]{7} [Propheten]{8} und{9} [Weise]{10} und{11} [Schriftgelehrte]{12}. [Einige von]{13} [ihnen]{14} [werdet ihr töten]{15} und{16} [kreuzigen]{17}, und{18} [einige von]{19} [ihnen]{20} [werdet ihr]{21} [in]{22} [euren]{23,25} [Synagogen]{24} [auspeitschen]{21} und{26} [von]{28} [Stadt]{29} [zu]{30} [Stadt]{31} [verfolgen]{27},",
 "MAT.23.35": "[damit]{1} [über]{3} [euch]{4} [alles]{5} [gerechte]{7} [Blut]{6} [kommt]{2}, [das]{8} [auf]{9} [der Erde]{10,11} [vergossen wird]{8}, [vom]{12,13} [Blut]{14} [Abels]{15}, [des Gerechten]{16,17}, [bis zum]{18,19} [Blut]{20} [Secharjas]{21}, [des Sohnes]{22} [Berechjas]{23}, [den]{24} [ihr]{25} [zwischen]{26} [dem Tempel]{27,28} und{29} [dem Altar]{30,31} [ermordet habt]{25}.",
 "MAT.23.36": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Das]{5} [alles]{6} [wird]{4} [über]{7} [dieses]{8,10} [Geschlecht]{9} [kommen]{4}.",
 "MAT.23.37": "[Jerusalem]{1}, [Jerusalem]{2}, [die]{3} [die Propheten]{5,6} [tötet]{4} und{7} die [steinigt]{8}, [die]{9} [zu]{11} [ihr]{12} [gesandt sind]{10}! [Wie oft]{13} [habe ich]{14} [deine]{18} [Kinder]{16,17} [sammeln]{15} [wollen]{14}, [wie]{19,20} [eine Henne]{21} [ihre]{25} [Küken]{23,24} [unter]{26} [die Flügel]{27,28} [sammelt]{22}, und{29} [ihr habt]{31} [nicht]{30} [gewollt]{31}!",
 "MAT.23.38": "[Siehe]{1}, [euer]{6} [Haus]{4,5} [wird]{2} [euch]{3} [verödet]{7} [überlassen]{2}.",
 "MAT.23.39": "[Denn]{2} [ich sage]{1} [euch]{3}: [Ihr werdet]{7} [mich]{6} [von jetzt an]{8,9} [nicht mehr]{4,5} [sehen]{7}, [bis]{10,11} [ihr sagt]{12}: «[Gesegnet sei]{13} [der, der]{14} [kommt]{15} [im]{16} [Namen]{17} [des Herrn]{18}!»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 22
 "MAT.22.1": "Und{1} [de Jesus]{3,4} [hät gantwortet]{2} und [wider]{5} [i]{7} [Gliichnis]{8} [zu ine]{9} [gredt]{6}: ~10(λέγων «sägend» leitet di diräkt Red ii)",
 "MAT.22.2": "«[S Riich]{2,3} [vo de Himel]{4,5} [isch]{1} [eme König]{6,7} [gliich worde]{1}, [wo]{8} [für]{11} [sin]{13} [Sohn]{12} [es Hochziitfäscht]{10} [gmacht hät]{9}.",
 "MAT.22.3": "Und{1} [er hät]{2} [sini]{5} [Chnächt]{3,4} [gschickt]{2}, [für]{6} [di]{7} [Iigladne]{8} [as]{9,10} [Hochziitfäscht]{11} [z rüefe]{6}; und{12} [si händ]{14} [nöd]{13} [wele]{14} [choo]{15}.",
 "MAT.22.4": "[Wider]{1} [hät er]{2} [anderi]{3} [Chnächt]{4} [gschickt]{2} und [gseit]{5}: ‹[Säged]{6} [de]{7} [Iigladne]{8}: [Lueg]{9}, [ich han]{13} [mis]{12} [Ässe]{10,11} [parat gmacht]{13}, [mini]{16} [Ochse]{14,15} und{17} [s]{18} [Mastvieh]{19} [sind gmetzget]{20}, und{21} [alles]{22} [isch parat]{23}. [Chömed]{24} [as]{25,26} [Hochziitfäscht]{27}!›",
 "MAT.22.5": "[Si]{1} [aber]{2} [händ sich nüüt drus gmacht]{3} und [sind wäggange]{4}, [de eint]{5,6} [uf]{7} [sin]{8} [eigete]{9} [Acher]{10}, [de ander]{11,12} [zu]{13} [sim]{14,16} [Gschäft]{15}.",
 "MAT.22.6": "[Di]{1} [andere]{3} [aber]{2} [händ]{4} [sini]{7} [Chnächt]{5,6} [packt]{4}, [misshandlet]{8} und{9} [umbrocht]{10}.",
 "MAT.22.7": "[De König]{1,3} [aber]{2} [isch toube worde]{4}, und{5} [er hät]{6} [sini]{9} [Truppe]{7,8} [gschickt]{6}, [hät]{10} [säbi]{13} [Mörder]{11,12} [umbrocht]{10} und{14} [hät]{18} [iri]{17} [Stadt]{15,16} [aazündt]{18}.",
 "MAT.22.8": "[Dänn]{1} [seit er]{2} [zu sine]{3,5} [Chnächt]{4}: ‹[S Hochziitfäscht]{6,8} [isch]{10} [zwar]{7} [parat]{9}, [di]{11} [Iigladne]{13} [aber]{12} [sind]{15} s [nöd]{14} [wärt]{16} [gsii]{15}.",
 "MAT.22.9": "[Gönd]{1} [also]{2} [a]{3} [d]{4} [Usgäng]{5} [vo de Strasse]{6,7}, und{8} [laded]{12} [alli, wo]{9} [ir finded]{11}, [as]{13,14} [Hochziitfäscht]{15} [ii]{12}!› ~10(ἐάν verallgemeineret «alli, wo»; nöd eigens widergää)",
 "MAT.22.10": "Und{1} [säbi]{5} [Chnächt]{3,4} [sind]{2} [uf]{6} [d]{7} [Strasse]{8} [usegange]{2} und [händ]{9} [alli]{10} [zämegholt]{9}, [wo]{11} [si gfunde händ]{12}, [Bösi]{13} [und]{14,15} [Gueti]{16}; und{17} [s Hochziitfäscht]{19,20} [isch voll]{18} [Gäscht]{21} [worde]{18}.",
 "MAT.22.11": "[Wo]{1} [aber]{2} [de König]{3,4} [inechoo isch]{1}, [für]{5} [d Gäscht]{6,7} [aazluege]{5}, [hät er]{8} [dört]{9} [en Mänsch]{10} [gseh]{8}, [wo]{12} [kei]{11} [Hochziitgwand]{13,14} [aaghaa hät]{12}.",
 "MAT.22.12": "Und{1} [er seit]{2} [zu ihm]{3}: ‹[Fründ]{4}, [wie]{5} [bisch du]{6} [da]{7} [inechoo]{6}, [ohni]{8} [es Hochziitgwand]{10,11} [z haa]{9}?› [Er]{12} [aber]{13} [isch verstummt]{14}.",
 "MAT.22.13": "[Dänn]{1} [hät]{4} [de König]{2,3} [zu de]{5} [Diener]{6} [gseit]{4}: ‹[Binded]{7} [ihm]{8} [d Füess]{9} und{10} [d Händ]{11} und [rüered]{12} [en]{13} [use]{12} [i]{14} [d]{15} [Fiischteri]{16} [dusse]{17,18}! [Dört]{19} [wird]{20} [s Hüüle]{21,22} und{23} [s Zändchnirsche]{24-27} [sii]{20}.›",
 "MAT.22.14": "[Dänn]{2} [vili]{1} [sind]{3} [iiglade]{4}, [aber]{6} [wenig]{5} [userwählt]{7}.»",
 "MAT.22.15": "[Dänn]{1} [sind]{2} [d Pharisäer]{3,4} [gange]{2} und [händ sich beraate]{5,6}, [wie]{7} [si]{9} [en]{8} [mit]{10} [ere Ussag]{11} [i d Falle locke chönnted]{9}.",
 "MAT.22.16": "Und{1} [si schicked]{2} [iri]{6} [Jünger]{4,5} [mit]{7} [de Herodianer]{8,9} [zu ihm]{3}, [wo säged]{10}: «[Lehrer]{11}, [mir wüssed]{12}, [dass]{13} [du]{15} [ufrichtig]{14} [bisch]{15} und{16} [de Wäg]{17,18} [vo Gott]{19,20} [i]{21} [Wahrheit]{22} [lehrsch]{23}, und{24} [du]{27} [kümmersch di]{26} [um]{28} [niemer]{25,29}; [dänn]{31} [du luegsch]{32} [nöd]{30} [uf]{33} [s Aaseh]{34} [vo de Mänsche]{35}.",
 "MAT.22.17": "[Säg]{1} [üs]{3} [also]{2}: [Was]{4} [meinsch]{6} [du]{5}? [Isch es erlaubt]{7}, [em Kaiser]{10} [Stüür]{9} [z zale]{8}, [oder]{11} [nöd]{12}?»",
 "MAT.22.18": "[De Jesus]{3,4} [aber]{2} [hät]{1} [iri]{7} [Bosheit]{5,6} [gmerkt]{1} und [gseit]{8}: «[Werum]{9} [stelled ir]{11} [mi]{10} [uf d Prob]{11}, [ir Hüüchler]{12}?",
 "MAT.22.19": "[Zeiged]{1} [mir]{2} [d]{3} [Münz]{4} [für d Stüür]{5,6}!» [Si]{7} [aber]{8} [händ]{9} [ihm]{10} [en Denar]{11} [brocht]{9}.",
 "MAT.22.20": "Und{1} [er seit]{2} [zu ine]{3}: «[Wäm sis]{4} [Bild]{5,6} und{8} [Ufschrift]{9,10} [isch das]{7}?»",
 "MAT.22.21": "[Si säged]{1} [zu ihm]{2}: «[Vom Kaiser]{3}.» [Dänn]{4} [seit er]{5} [zu ine]{6}: «[Gänd]{7} [also]{8}, [was]{9} [em Kaiser]{10} ghört, [em Kaiser]{11}, und{12} [was]{13} [Gott]{14,15} ghört, [Gott]{16,17}!»",
 "MAT.22.22": "Und{1} [wo si das ghört händ]{2}, [händ si gstuunt]{3}; und{4} [si händ]{5} [en]{6} [la staa]{5} und [sind wäggange]{7}.",
 "MAT.22.23": "[A]{1} [säbem]{2} [Tag]{3,4} [sind]{5} [Sadduzäer]{7} [zu ihm]{6} [härechoo]{5}, [wo säged]{8}, [es geb]{10} [kei]{9} [Uferstehig]{11}, und{12} [si händ]{13} [en]{14} [gfröget]{13}",
 "MAT.22.24": "[und gseit]{1}: «[Lehrer]{2}, [de Mose]{3} [hät gseit]{4}: ‹[Wänn]{5} [öpper]{6} [stirbt]{7}, [ohni]{8} [Chind]{10} [z haa]{9}, [söll]{11} [sin]{14} [Brüeder]{12,13} [sini]{17} [Frau]{15,16} [hürate]{11} und{18} [sim]{23} [Brüeder]{21,22} [Nachkomme]{20} [verschaffe]{19}.›",
 "MAT.22.25": "[Es sind]{1} [aber]{2} [bi]{3} [üs]{4} [sibe]{5} [Brüedere]{6} [gsii]{1}. Und{7} [de erscht]{8,9} [hät ghürate]{10} und [isch gstorbe]{11}, und{12} [wil er]{14} [kei]{13} [Nachkomme]{15} [gha hät]{14}, [hät er]{16} [sini]{19} [Frau]{17,18} [sim]{22} [Brüeder]{20,21} [hinderlaa]{16}.",
 "MAT.22.26": "[Gnau gliich]{1} [au]{2} [de zweit]{3,4} und{5} [de dritt]{6,7}, [bis]{8} [zum]{9} [sibete]{10}.",
 "MAT.22.27": "[Zletscht]{1} [aber]{2}, [nach allne]{3}, [isch]{4} [d Frau]{5,6} [gstorbe]{4}.",
 "MAT.22.28": "[I]{1} [de Uferstehig]{2,3} [also]{4}: [Wäm vo]{5} [de]{6} [sibe]{7} [sini Frau]{9} [wird si sii]{8}? [Dänn]{11} [alli]{10} [händ]{12} [si]{13} zur Frau [gha]{12}.»",
 "MAT.22.29": "[De Jesus]{3,4} [aber]{2} [hät gantwortet]{1} und [zu ine]{6} [gseit]{5}: «[Ir irred]{7}, [wil ir]{9} [weder]{8} [d Schrifte]{10,11} [känned]{9} [no]{12} [d Chraft]{13,14} [vo Gott]{15,16}.",
 "MAT.22.30": "[Dänn]{2} [i]{1} [de Uferstehig]{3,4} [hürated si]{6} [weder]{5}, [no]{7} [wärded si verhüratet]{8}, [sondern]{9} [si sind]{16} [wie]{10} [Ängel]{11} [vo Gott]{12} [im]{13,14} [Himel]{15}.",
 "MAT.22.31": "[Was]{1} [aber]{2} [d Uferstehig]{3,4} [vo de Tote]{5,6} [betrifft]{1}: [Händ ir]{8} [nöd]{7} [gläse]{8}, [was]{9} [eu]{11} [vo]{12} [Gott]{13,14} [gseit worde isch]{10}, [wo seit]{15}:",
 "MAT.22.32": "‹[Ich]{1} [bi]{2} [de Gott]{3,4} [vom Abraham]{5} und{6} [de Gott]{7,8} [vom Isaak]{9} und{10} [de Gott]{11,12} [vom Jakob]{13}›? [Er isch]{15} [nöd]{14} [de Gott]{16,17} [vo Tote]{18}, [sondern]{19} [vo Läbige]{20}.»",
 "MAT.22.33": "Und{1} [wo]{2} [d Lüüt]{3,4} [das ghört händ]{2}, [sind si]{5} [vo]{6} [sinere]{9} [Lehr]{7,8} [überwältiget gsii]{5}.",
 "MAT.22.34": "[Wo]{4} [aber]{2} [d Pharisäer]{1,3} [ghört händ]{4}, [dass]{5} [er]{6} [d Sadduzäer]{7,8} [zum Schwiige brocht hät]{6}, [händ si sich]{9} [am gliiche Ort]{10-12} [versammlet]{9}.",
 "MAT.22.35": "Und{1} [eine]{3} [vo]{4} [ine]{5}, [en Gsetzeslehrer]{6}, [hät gfröget]{2}, [für]{7} [en]{8} [uf d Prob z stelle]{7}:",
 "MAT.22.36": "«[Lehrer]{1}, [weles]{2} [Gebot]{3} [isch s gröscht]{4} [im]{5,6} [Gsetz]{7}?»",
 "MAT.22.37": "[Er]{1} [aber]{2} [hät]{3} [zu ihm]{4} [gseit]{3}: «‹[Du söllsch]{5} [de Herr]{6}, [din]{9} [Gott]{7,8}, [liebe]{5} [mit]{10} [dim]{14} [ganze]{11} [Härz]{12,13} und{15} [mit]{16} [dinere]{20} [ganze]{17} [Seel]{18,19} und{21} [mit]{22} [dim]{26} [ganze]{23} [Dänke]{24,25}.›",
 "MAT.22.38": "[Das]{1} [isch]{2} [s]{3} [gröscht]{4} und{5} [erscht]{6} [Gebot]{7}.",
 "MAT.22.39": "[S zweit]{1} [aber]{2} [isch]{3} [ihm]{4} [gliich]{3}: ‹[Du söllsch]{5} [din]{6,8} [Nächschte]{7} [liebe]{5} [wie]{9} [di sälber]{10}.›",
 "MAT.22.40": "[A]{1} [dene]{2,3} [zwei]{4} [Gebot]{5} [hanged]{9} [s ganz]{6,7} [Gsetz]{8} und{10} [d Prophete]{11,12}.»",
 "MAT.22.41": "[Wo]{1} [aber]{2} [d Pharisäer]{3,4} [versammlet gsii sind]{1}, [hät]{5} [de Jesus]{7,8} [si]{6} [gfröget]{5}",
 "MAT.22.42": "[und gseit]{1}: «[Was]{2} [meined]{4} [ir]{3} [über]{5} [de Christus]{6,7}? [Wäm sin]{8} [Sohn]{9} [isch er]{10}?» [Si säged]{11} [zu ihm]{12}: «[Vom David]{13,14}.»",
 "MAT.22.43": "[Er seit]{1} [zu ine]{2}: «[Wie]{3} [nännt]{8} [en]{9} [dänn]{4} [de David]{5} [im]{6} [Geischt]{7} ‹[Herr]{10}›, [wänn er seit]{11}:",
 "MAT.22.44": "‹[De Herr]{2} [hät]{1} [zu mim]{3,5} [Herr]{4} [gseit]{1}: [Sitz]{6} [rächts]{8} [vo]{7} [mir]{9}, [bis]{10,11} [ich]{12} [dini]{15} [Find]{13,14} [under]{16} [dini]{19} [Füess]{17,18} [lege]{12}›?",
 "MAT.22.45": "[Wänn]{1} [also]{2} [de David]{3} [en]{5} ‹[Herr]{6}› [nännt]{4}, [wie]{7} [isch er]{10} dänn [sin]{9} [Sohn]{8}?»",
 "MAT.22.46": "Und{1} [niemer]{2} [hät]{3} [ihm]{5} [es Wort]{6} [chöne]{3} [antworte]{4}, und [vo]{10} [säbem]{11} [Tag]{12,13} [aa]{10} [hät sich]{8} [au]{7} [keine]{9} [meh]{16} [traut]{8}, [en]{15} [z fröge]{14}.",
 # ------------------------------------------------------------ Kapitel 23
 "MAT.23.1": "[Dänn]{1} [hät]{4} [de Jesus]{2,3} [zu de]{5} [Lüüt]{6} und{7} [zu sine]{8,10} [Jünger]{9} [gredt]{4}",
 "MAT.23.2": "[und gseit]{1}: [Uf]{2} [de]{3} [Stuel]{5} [vom Mose]{4} [händ sich]{6} [d Schriftgelehrte]{7,8} und{9} [d Pharisäer]{10,11} [gsetzt]{6}.",
 "MAT.23.3": "[Alles]{1} [also]{2}, [was]{3} [si]{5} [eu]{6} [säged]{5}, [das mached]{7} und{8} [halted]{9}; [aber]{11} [richted eu]{16} [nöd]{15} [nach]{10} [irne]{14} [Wärch]{12,13}; [dänn]{18} [si reded]{17} und{19} [tüend s]{21} [nöd]{20}. ~4(ἐάν verallgemeineret «alles, was»; nöd eigens widergää)",
 "MAT.23.4": "[Si binded]{1} [aber]{2} [schwääri]{4} [Laschte]{3} [zäme]{1} und{5} [leged]{6} si [de Mänsche]{10,11} [uf]{7} [d Schultere]{8,9}; [si sälber]{12} [aber]{13} [wänd]{18} [si]{20} [mit]{14} [irem]{16} [Finger]{15} [nöd]{17} [bewege]{19}.",
 "MAT.23.5": "[Alli]{1} [iri]{5} [Wärch]{3,4} [aber]{2} [tüend si]{6}, [damit]{7,8} [d Mänsche]{10,11} [si gsehnd]{9}; [dänn]{13} [si mached]{12} [iri]{16} [Gebetsrieme]{14,15} [breit]{12} und{17} [d Quaste]{19,20} [lang]{18}.",
 "MAT.23.6": "[Si händ]{1} [aber]{2} [gärn]{1} [de]{3} [Ehreplatz]{4} [a]{5} [de]{6} [Fäschtässe]{7} und{8} [d]{9} [Ehreplätz]{10} [i]{11} [de]{12} [Synagoge]{13}",
 "MAT.23.7": "und{1} [d]{2} [Grüess]{3} [uf]{4} [de]{5} [Märtplätz]{6} und{7} [dass si]{8} [vo]{9} [de Mänsche]{10,11} «[Rabbi]{12}» [gnännt wärded]{8}.",
 "MAT.23.8": "[Ir]{1} [aber]{2} [söled eu]{4} [nöd]{3} «[Rabbi]{5}» [nänne laa]{4}; [dänn]{7} [eine]{6} [isch]{8} [eue]{9} [Lehrer]{10,11}, [ir]{14} [alli]{12} [aber]{13} [sind]{16} [Brüedere]{15}.",
 "MAT.23.9": "Und{1} [nänned]{4} [keine]{3} [uf]{6} [de Ärde]{7,8} [eue]{5} [Vatter]{2}; [dänn]{10} [eine]{9} [isch]{11} [eue]{12} [Vatter]{13,14}, [de himmlisch]{15,16}.",
 "MAT.23.10": "[Lönd eu]{2} [au nöd]{1} «[Lehrmeischter]{3}» [nänne]{2}; [dänn]{4} [eine]{8} [isch]{7} [eue]{6} [Lehrmeischter]{5}, [de Christus]{9,10}.",
 "MAT.23.11": "[De Gröscht]{1,3} [under eu]{4} [aber]{2} [söll]{5} [eue]{6} [Diener]{7} [sii]{5}.",
 "MAT.23.12": "[Wer]{1} [sich]{4} [aber]{2} [sälber]{4} [erhöcht]{3}, [wird erniedriget]{5}, und{6} [wer]{7} [sich sälber]{9} [erniedriget]{8}, [wird erhöcht]{10}.",
 "MAT.23.13": "[Weh]{1} [aber]{2} [eu]{3}, [Schriftgelehrti]{4} und{5} [Pharisäer]{6}, [ir Hüüchler]{7}, [dänn]{8} [ir schlüssed]{9} [s Riich]{10,11} [vo de Himel]{12,13} [vor]{14} [de Mänsche]{15,16} [zue]{9}! [Ir]{17} sälber [gönd]{20} [ja]{18} [nöd]{19} [ine]{20}, [und]{21} [die, wo]{22} [inewänd]{23}, [lönd ir]{24} [nöd]{21} [inegaa]{25}.",
 "MAT.23.15": "[Weh]{1} [eu]{2}, [Schriftgelehrti]{3} und{4} [Pharisäer]{5}, [ir Hüüchler]{6}, [dänn]{7} [ir zieched]{8} [übers Meer]{9,10} und{11} [übers troche Land]{12,13}, [für]{14} [en einzige]{15} [Proselyt]{16} [z gwünne]{14}, und{17} [wänn]{18} [er s worde isch]{19}, [mached ir]{20} [en]{21} [zumene Sohn]{22} [vo de Höll]{23}, [doppelt so schlimm]{24} [wie ir]{25}!",
 "MAT.23.16": "[Weh]{1} [eu]{2}, [ir blinde]{4} [Füerer]{3}, [wo säged]{5,6}: «[Wer]{7,8} [bim]{10,11} [Tämpel]{12} [schwört]{9}, [das gilt]{14} [nüüt]{13}; [wer]{15,17} [aber]{16} [bim]{19,20} [Gold]{21} [vom Tämpel]{22,23} [schwört]{18}, [isch draa bunde]{24}.»",
 "MAT.23.17": "[Ir Narre]{1} und{2} [Blinde]{3}! [Was]{4} [isch]{7} [dänn]{5} [grösser]{6}: [s Gold]{8,9} [oder]{10} [de Tämpel]{11,12}, [wo]{13} [s Gold]{15,16} [heilig gmacht hät]{14}?",
 "MAT.23.18": "Und{1}: «[Wer]{2,3} [bim]{5,6} [Altar]{7} [schwört]{4}, [das gilt]{9} [nüüt]{8}; [wer]{10,12} [aber]{11} [bi]{14} [de Gab]{15,16} [schwört]{13}, [wo]{17} [druf]{18,19} liit, [isch draa bunde]{20}.»",
 "MAT.23.19": "[Ir Blinde]{1}! [Was]{2} isch [dänn]{3} [grösser]{4}: [d Gab]{5,6} [oder]{7} [de Altar]{8,9}, [wo]{10} [d Gab]{12,13} [heilig macht]{11}?",
 "MAT.23.20": "[Wer]{1} [also]{2} [bim]{4,5} [Altar]{6} [schwört]{3}, [schwört]{7} [bi]{8} [ihm]{9} und{10} [bi]{11} [allem]{12}, [wo]{13} [druf]{14,15} liit.",
 "MAT.23.21": "Und{1} [wer]{2} [bim]{4,5} [Tämpel]{6} [schwört]{3}, [schwört]{7} [bi]{8} [ihm]{9} und{10} [bi]{11} [däm, wo]{12} [drin]{14} [wohnt]{13}.",
 "MAT.23.22": "Und{1} [wer]{2} [bim]{4,5} [Himel]{6} [schwört]{3}, [schwört]{7} [bim]{8,9} [Thron]{10} [vo Gott]{11,12} und{13} [bi]{14} [däm, wo]{15} [druf]{17,18} [sitzt]{16}.",
 "MAT.23.23": "[Weh]{1} [eu]{2}, [Schriftgelehrti]{3} und{4} [Pharisäer]{5}, [ir Hüüchler]{6}, [dänn]{7} [ir gänd de Zäänte]{8} [vo de]{9} [Minze]{10} und{11} [vom]{12} [Dill]{13} und{14} [vom]{15} [Chümi]{16} und{17} [händ]{18} [s Gwichtiger]{19,20} [vom Gsetz]{21,22} [uf d Siite gstellt]{18}: [s Rächt]{23,24} und{25} [d Barmherzigkeit]{26,27} und{28} [d Treui]{29,30}! [Das]{31} [hett mer sölle]{32} [tue]{33} [und säbs]{34} [nöd]{35} [uf d Siite stelle]{36}.",
 "MAT.23.24": "[Ir blinde]{2} [Füerer]{1}, [wo]{3} [d Mugge]{5,6} [ussiebed]{4}, [aber]{8} [s Kamel]{7,9} [abeschlucked]{10}!",
 "MAT.23.25": "[Weh]{1} [eu]{2}, [Schriftgelehrti]{3} und{4} [Pharisäer]{5}, [ir Hüüchler]{6}, [dänn]{7} [ir mached]{8} [s Üsser]{9,10} [vom Becher]{11,12} und{13} [vo de Schüssle]{14,15} [suuber]{8}, [inne]{16} [aber]{17} [sind si voll]{18} [vo]{19} [Raub]{20} und{21} [Masslosigkeit]{22}!",
 "MAT.23.26": "[Du blinde]{2} [Pharisäer]{1}! [Mach]{3} [zerscht]{4} [s Inner]{5,6} [vom Becher]{7,8} und{9} [vo de Schüssle]{10,11} [suuber]{3}, [damit]{12} [au]{14} [sis]{17} [Üsser]{15,16} [suuber]{18} [wird]{13}.",
 "MAT.23.27": "[Weh]{1} [eu]{2}, [Schriftgelehrti]{3} und{4} [Pharisäer]{5}, [ir Hüüchler]{6}, [dänn]{7} [ir sind wie]{8} [wiissgstricheni]{10} [Greber]{9}, [wo]{11} [usse]{12} [zwar]{13} [schöön]{15} [usgsehnd]{14}, [inne]{16} [aber]{17} [voll sind]{18} [vo Totechnoche]{19,20} und{21} [vo allerlei]{22} [Unreinheit]{23}!",
 "MAT.23.28": "[So]{1} [gsehnd]{6} [au]{2} [ir]{3} [usse]{4} [zwar]{5} [für d Mänsche]{7,8} [grächt]{9} [us]{6}, [inne]{10} [aber]{11} [sind ir]{12} [voll]{13} [Hüüchelei]{14} und{15} [Gsetzlosigkeit]{16}.",
 "MAT.23.29": "[Weh]{1} [eu]{2}, [Schriftgelehrti]{3} und{4} [Pharisäer]{5}, [ir Hüüchler]{6}, [dänn]{7} [ir bued]{8} [d Greber]{9,10} [vo de Prophete]{11,12} und{13} [schmücked]{14} [d Grabmäler]{15,16} [vo de Grächte]{17,18}",
 "MAT.23.30": "und{1} [säged]{2}: «[Wänn]{3} [mir]{4} [i]{5} [de Täg]{6,7} [vo öisne]{8,10} [Vätere]{9} [gläbt hettid]{4}, [wäred mir]{12,13} [nöd]{11} [mit ine]{14} [am]{16,17} [Bluet]{18} [vo de Prophete]{19,20} [beteiligt]{15} [gsii]{12,13}.»",
 "MAT.23.31": "[Damit]{1} [bezüüged ir]{2} [eu sälber]{3}, [dass]{4} [ir]{6} [Söhn]{5} [vo dene]{7} [sind]{6}, [wo]{8} [d Prophete]{9,10} [umbrocht händ]{8}.",
 "MAT.23.32": "Und{1} [ir]{2}: [Mached]{3} [s Mass]{4,5} [vo eune]{6,8} [Vätere]{7} [voll]{3}!",
 "MAT.23.33": "[Ir Schlange]{1}, [ir Viperebruet]{2,3}! [Wie]{4} [wänd ir]{5} [em]{6,7} [Gricht]{8} [vo de Höll]{9,10} [entchoo]{5}?",
 "MAT.23.34": "[Drum]{1,2}, [lueg]{3}, [ich]{4} [schick]{5} [zu]{6} [eu]{7} [Prophete]{8} und{9} [Wiisi]{10} und{11} [Schriftgelehrti]{12}. [Es paar vo]{13} [ine]{14} [wärded ir umbringe]{15} und{16} [chrüüzige]{17}, und{18} [es paar vo]{19} [ine]{20} [wärded ir]{21} [i]{22} [eune]{23,25} [Synagoge]{24} [uspeitsche]{21} und{26} [vo]{28} [Stadt]{29} [zu]{30} [Stadt]{31} [verfolge]{27},",
 "MAT.23.35": "[damit]{1} [über]{3} [eu]{4} [alles]{5} [grächte]{7} [Bluet]{6} [chunnt]{2}, [wo]{8} [uf]{9} [de Ärde]{10,11} [vergosse wird]{8}, [vom]{12,13} [Bluet]{14} [vom Abel]{15}, [em Grächte]{16,17}, [bis zum]{18,19} [Bluet]{20} [vom Secharja]{21}, [em Sohn]{22} [vom Berechja]{23}, [wo]{24} [ir]{25} [zwüsche]{26} [em Tämpel]{27,28} und{29} [em Altar]{30,31} [ermordet händ]{25}.",
 "MAT.23.36": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Das]{5} [alles]{6} [chunnt]{4} [über]{7} [die]{8,10} [Generation]{9}.",
 "MAT.23.37": "[Jerusalem]{1}, [Jerusalem]{2}, [wo]{3} [d Prophete]{5,6} [umbringt]{4} und{7} die [steiniget]{8}, [wo]{9} [zu]{11} [ire]{12} [gschickt worde sind]{10}! [Wie mängisch]{13} [han ich]{14} [dini]{18} [Chind]{16,17} [wele]{14} [sammle]{15}, [wie]{19,20} [e Huen]{21} [iri]{25} [Bibeli]{23,24} [under]{26} [d Flügel]{27,28} [sammlet]{22}, und{29} [ir händ]{31} [nöd]{30} [wele]{31}!",
 "MAT.23.38": "[Lueg]{1}, [eues]{6} [Huus]{4,5} [wird]{2} [eu]{3} [läär und öd]{7} [überlaa]{2}.",
 "MAT.23.39": "[Dänn]{2} [ich säg]{1} [eu]{3}: [Ir wärded]{7} [mich]{6} [vo jetzt aa]{8,9} [nümme]{4,5} [gseh]{7}, [bis]{10,11} [ir säged]{12}: «[Gsägnet sig]{13} [dä, wo]{14} [chunnt]{15} [im]{16} [Name]{17} [vom Herr]{18}!»",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MAT.22.1", "antwortete", "literal", "ἀποκριθεὶς", None, ["ergriff das Wort", "fuhr fort"],
  "Eine Frage geht nicht voraus; ἀποκρίνομαι steht hier wie oft in den Evangelien für das Aufnehmen einer Situation. Das Gleichnis antwortet auf die Lage von [[MAT.21.45]]–[[MAT.21.46]], wo die Hohepriester und Pharisäer Jesus festnehmen wollen. Die wörtliche Wiedergabe lässt diesen Bezug sichtbar."),
 ("MAT.22.2", "Das Reich der Himmel", "literal", "ἡ βασιλεία τῶν οὐρανῶν", None, ["das Himmelreich", "die Herrschaft der Himmel", "das Reich Gottes"],
  "Gemeinsame Wiedergabe für das ganze Matthäusevangelium. Matthäus sagt meist «Reich der Himmel», wo Markus und Lukas «Reich Gottes» haben; «Himmel» (im Griechischen Plural, nach hebräisch šāmayim) gilt vielen als ehrfürchtige Umschreibung für Gott. βασιλεία meint sowohl das Herrschaftsgebiet als auch das Herrschen selbst."),
 ("MAT.22.2", "ist einem König gleich geworden", "adapted", "Ὡμοιώθη ἀνθρώπῳ βασιλεῖ", "ist gleich geworden einem Menschen, einem König", ["Mit dem Reich der Himmel ist es wie mit einem König", "gleicht einem König"],
  "ὡμοιώθη (Aorist Passiv) heisst «wurde gleich gemacht, ist gleich geworden»; Matthäus leitet so auch [[MAT.13.24]] und [[MAT.18.23]] ein. Ob der Aorist sagt, dass das Gleichnis schon Wirklichkeit geworden ist, oder einfach eine feste Einleitungsformel ist, wird verschieden beurteilt. Der Vergleichspunkt ist nicht der König allein, sondern die ganze erzählte Begebenheit. ἄνθρωπος βασιλεύς («ein Mensch, ein König») ist eine semitisch geprägte Doppelung; sie ist mit «einem König» wiedergegeben."),
 ("MAT.22.2", "ein Hochzeitsfest", "literal", "γάμους", "Hochzeiten", ["eine Hochzeit", "ein Hochzeitsmahl"],
  "Plural γάμοι für das (oft mehrtägige) Fest; ebenso in [[MAT.22.3]], [[MAT.22.4]] und [[MAT.22.9]]. In [[MAT.22.8]] und [[MAT.22.10]] steht der Singular γάμος, ebenfalls «Hochzeitsfest»."),
 ("MAT.22.3", "Knechte", "literal", "δούλους", None, ["Sklaven", "Diener"],
  "δοῦλος ist der unfreie Diener, oft ein Sklave; im Gleichnis sind es die Boten des Königs. «Knecht» wie in der Markus-Übersetzung ([[MRK.12.2]]); die διάκονοι in [[MAT.22.13]] heissen zur Unterscheidung «Diener»."),
 ("MAT.22.3", "Geladenen", "literal", "κεκλημένους", "die Gerufenen", ["die Eingeladenen"],
  "Perfekt Partizip: Die Gäste sind schon früher eingeladen worden; nun werden sie gerufen, weil das Fest beginnt. Eine doppelte Einladung kennt auch die Schrift (vgl. [[EST.5.8]] und [[EST.6.14]]). καλέω durchzieht das Gleichnis bis zu κλητοί in [[MAT.22.14]]."),
 ("MAT.22.4", "Mahl", "adapted", "ἄριστόν", "Frühmahl", ["Mittagsmahl", "Festessen"],
  "ἄριστον ist die erste Mahlzeit des Tages bzw. ein Mittagsmahl; hier das Mahl, mit dem das Fest beginnt."),
 ("MAT.22.7", "zündete ihre Stadt an", "literal", "τὴν πόλιν αὐτῶν ἐνέπρησεν", None, None,
  "Der Zug gegen eine Stadt sprengt das Bild eines Hochzeitsfests. Viele sehen darin einen Rückblick auf die Zerstörung Jerusalems im Jahr 70; andere verweisen darauf, dass Strafzüge gegen aufrührerische Städte ein verbreitetes Motiv in Erzählungen über Könige sind. Der Text nennt keine Stadt; die Übersetzung trägt keinen Namen ein."),
 ("MAT.22.9", "an die Ausgänge der Strassen", "interpretive", "ἐπὶ τὰς διεξόδους τῶν ὁδῶν", None, ["an die Kreuzungen", "an die Wegscheiden", "dorthin, wo die Strassen aus der Stadt führen"],
  "διέξοδος ist der Ausgang, die Stelle, an der eine Strasse in offenes Land hinausführt, oder eine Weggabelung. Gemeint sind Orte, wo viele Leute vorbeikommen, auch solche von ausserhalb."),
 ("MAT.22.10", "mit Gästen", "adapted", "ἀνακειμένων", "mit zu Tisch Liegenden", ["mit Tischgästen"],
  "Bei Festmählern lag man zu Tisch. Ebenso [[MAT.22.11]] «die Gäste»."),
 ("MAT.22.11", "Hochzeitskleid", "literal", "ἔνδυμα γάμου", "Gewand der Hochzeit", ["Festkleid"],
  "Ob vorausgesetzt ist, dass der Gastgeber Festkleider stellte, sagt der Text nicht; antike Belege dafür sind umstritten. Was das Kleid bedeutet (etwa ein der Einladung entsprechendes Leben, vgl. [[MAT.7.21]]), ist Deutung; die Übersetzung bleibt beim Bild."),
 ("MAT.22.12", "Freund", "literal", "Ἑταῖρε", None, ["Kamerad", "Mein Lieber"],
  "ἑταῖρος ist eine freundliche, aber distanzierte Anrede (nicht φίλος); bei Matthäus jeweils vor einem Vorwurf: [[MAT.20.13]], [[MAT.26.50]]."),
 ("MAT.22.13", "in die Finsternis draussen", "literal", "εἰς τὸ σκότος τὸ ἐξώτερον", None, ["in die äusserste Finsternis"],
  "ἐξώτερος «weiter draussen»: die Finsternis ausserhalb des erleuchteten Festsaals. Dieselbe Wendung samt «Weinen und Zähneknirschen» in [[MAT.8.12]] und [[MAT.25.30]]."),
 ("MAT.22.13", "das Weinen", "literal", "ὁ κλαυθμὸς", None, ["das Heulen"],
  "κλαυθμός heisst «Weinen, Wehklagen». Die vertraute Wendung «Heulen und Zähneknirschen» ist hier zugunsten des Wörtlichen nicht übernommen."),
 ("MAT.22.14", "eingeladen", "interpretive", "κλητοὶ", "Gerufene", ["berufen"],
  "κλητός gehört zu καλέω, dem Leitwort des Gleichnisses (die «Geladenen», [[MAT.22.3]]–[[MAT.22.9]]). «Eingeladen» hält diesen Zusammenhang sichtbar; «berufen» ist die vertraute Wiedergabe. ἐκλεκτοί ist mit «auserwählt» wiedergegeben. «Viele» ist eine semitische Ausdrucksweise für eine grosse Zahl, nicht notwendig im Gegensatz zu «alle»."),
 ("MAT.22.15", "berieten sich", "adapted", "συμβούλιον ἔλαβον", "nahmen einen Ratschluss", ["fassten einen Beschluss", "hielten Rat"],
  "Dieselbe Wendung in [[MAT.12.14]] und [[MAT.27.1]]."),
 ("MAT.22.16", "den Herodianern", "literal", "τῶν Ἡρῳδιανῶν", None, ["den Anhängern des Herodes"],
  "Gemeint sind Anhänger der Herrscherfamilie des Herodes (in Galiläa regierte Herodes Antipas). Wer genau dazu gehörte, ist unklar; die Bezeichnung kommt nur hier und bei Markus ([[MRK.3.6]], [[MRK.12.13]]) vor."),
 ("MAT.22.16", "du siehst nicht auf das Ansehen der Menschen", "literal", "οὐ γὰρ βλέπεις εἰς πρόσωπον ἀνθρώπων", "du siehst nicht auf das Gesicht von Menschen", ["du bist nicht parteiisch", "du richtest dich nicht nach dem Rang eines Menschen"],
  "Hebräisch geprägte Wendung für Unparteilichkeit; wörtlich wie in der Markus-Übersetzung ([[MRK.12.14]])."),
 ("MAT.22.17", "Steuer", "literal", "κῆνσον", None, ["Kopfsteuer", "Zensus"],
  "κῆνσος ist das lateinische census: die Kopfsteuer, die die römische Verwaltung von der Bevölkerung Judäas erhob. «Kaiser» (Καῖσαρ, ursprünglich der Name Caesar) ist hier der regierende Kaiser, zur Zeit Jesu Tiberius."),
 ("MAT.22.18", "ihr Heuchler", "literal", "ὑποκριταί", None, ["ihr Scheinheiligen", "ihr Schauspieler"],
  "Gemeinsame Wiedergabe für das ganze Matthäusevangelium. ὑποκριτής heisst ursprünglich «Schauspieler». Bei Matthäus meint das Wort Menschen, deren Tun nicht mit dem übereinstimmt, was sie zeigen oder sagen (vgl. [[MAT.6.2]], [[MAT.23.28]]). Ebenso in den Weherufen von [[MAT.23]]."),
 ("MAT.22.19", "einen Denar", "literal", "δηνάριον", None, None,
  "Römische Silbermünze, etwa ein Tageslohn ([[MAT.20.2]]). Die Denare des Tiberius trugen sein Bild und eine Aufschrift, die ihn als Sohn des vergöttlichten Augustus bezeichnete."),
 ("MAT.22.21", "Gebt", "interpretive", "Ἀπόδοτε", "Gebt zurück", ["Zahlt", "Gebt, was ihr schuldet"],
  "ἀποδίδωμι heisst «zurückgeben, abgeben, was man schuldet». Die Frage in [[MAT.22.17]] hatte δοῦναι «geben» gebraucht. Manche hören darin, dass die Münze mit dem Bild des Kaisers ohnehin ihm gehört; die Übersetzung bleibt bei «geben» wie in [[MRK.12.17]]."),
 ("MAT.22.23", "die sagen, es gebe keine Auferstehung", "literal", "λέγοντες μὴ εἶναι ἀνάστασιν", None, None,
  "Kennzeichen der Sadduzäer, die nach Josephus und Apostelgeschichte ([[ACT.23.8]]) die Auferstehung ablehnten. Gemeinsame Wiedergabe der Gruppenbezeichnungen: Sadduzäer, Pharisäer, Schriftgelehrte."),
 ("MAT.22.24", "soll sein Bruder seine Frau heiraten", "adapted", "ἐπιγαμβρεύσει ὁ ἀδελφὸς αὐτοῦ τὴν γυναῖκα αὐτοῦ", "wird sein Bruder seine Frau als Schwager heiraten", ["soll … die Schwagerehe eingehen"],
  "Das Futur steht für ein Gebot. ἐπιγαμβρεύω ist das Fachwort für die Schwagerehe (Leviratsehe) nach [[DEU.25.5]]–[[DEU.25.6]] (vgl. [[GEN.38.8]]); die Sadduzäer geben das Gebot frei wieder."),
 ("MAT.22.24", "Nachkommen erwecken", "literal", "ἀναστήσει σπέρμα", "wird Samen aufstehen lassen", ["Nachkommen verschaffen"],
  "ἀνίστημι ist dasselbe Verb, zu dem ἀνάστασις «Auferstehung» gehört; die Wiedergabe «erwecken» lässt das Wortspiel anklingen."),
 ("MAT.22.26", "bis zum siebten", "adapted", "ἕως τῶν ἑπτά", "bis zu den sieben", ["bis hin zu allen sieben"],
  "Gemeint ist: bis alle sieben die Frau geheiratet hatten und gestorben waren."),
 ("MAT.22.29", "Ihr irrt", "literal", "Πλανᾶσθε", None, ["Ihr täuscht euch", "Ihr seid im Irrtum"],
  "Bei Markus als Frage ([[MRK.12.24]]); bei Matthäus als Feststellung."),
 ("MAT.22.30", "werden sie verheiratet", "literal", "γαμίζονται", None, ["werden sie zur Ehe gegeben"],
  "γαμίζω ist das Verheiraten durch den Vater oder Vormund, meist von Töchtern; γαμέω (heiraten) und γαμίζω zusammen umfassen also beide Seiten der Eheschliessung."),
 ("MAT.22.30", "wie Engel Gottes im Himmel", "literal", "ὡς ἄγγελοι θεοῦ ἐν τῷ οὐρανῷ", None, ["wie Engel im Himmel"],
  "Der SBLGNT liest θεοῦ mit Holmes; WH, Treg und NA28 haben das Wort nicht (siehe Alternative). Der Vergleich betrifft das Heiraten, nicht die Frage, ob die Auferstandenen Engel werden."),
 ("MAT.22.31", "der spricht", "literal", "λέγοντος", "sagend", None,
  "Das Präsens-Partizip stellt das Schriftwort als gegenwärtige Rede Gottes an die Hörer dar («was euch … gesagt worden ist»)."),
 ("MAT.22.32", "Er ist nicht der Gott von Toten", "interpretive", "οὐκ ἔστιν ὁ θεὸς νεκρῶν", "nicht ist (er) der Gott von Toten", ["Gott ist nicht ein Gott der Toten"],
  "Das Zitat stammt aus [[EXO.3.6]]. Ein Subjekt fehlt im Griechischen; es kann «er» (der redende Gott) oder «Gott» ergänzt werden."),
 ("MAT.22.33", "die Menschenmengen", "literal", "οἱ ὄχλοι", "die Volksmengen", ["die Scharen", "die Leute", "die Menge"],
  "Gemeinsame Wiedergabe für das ganze Matthäusevangelium: ὄχλος «die Menge», der Plural οἱ ὄχλοι «die Menschenmengen». Matthäus braucht oft den Plural; die Wiedergabe hält ihn fest. Ebenso [[MAT.23.1]]."),
 ("MAT.22.33", "waren sie überwältigt", "literal", "ἐξεπλήσσοντο", None, ["gerieten sie ausser sich", "staunten sie"],
  "Wie in der Markus-Übersetzung ([[MRK.1.22]]); vgl. [[MAT.7.28]]."),
 ("MAT.22.34", "versammelten sie sich am selben Ort", "literal", "συνήχθησαν ἐπὶ τὸ αὐτό", None, ["kamen sie zusammen"],
  "Manche hören einen Anklang an [[PSA.2.2]] in der Septuaginta (συνήχθησαν ἐπὶ τὸ αὐτό: Herrscher «versammeln sich» gegen den Herrn und seinen Gesalbten)."),
 ("MAT.22.35", "ein Gesetzeslehrer", "literal", "νομικὸς", None, ["ein Gesetzeskundiger", "ein Schriftgelehrter"],
  "νομικός, ein Kenner des Gesetzes (der Tora), steht bei Matthäus nur hier; Markus nennt den Fragenden einen Schriftgelehrten ([[MRK.12.28]])."),
 ("MAT.22.36", "ist das grösste", "adapted", "μεγάλη", "(ist) gross", ["ist gross"],
  "Der Positiv μεγάλη steht für den Superlativ, wie es im semitisch geprägten Griechisch häufig ist. Ebenso [[MAT.22.38]]."),
 ("MAT.22.37", "Denken", "literal", "διανοίᾳ", None, ["Verstand", "Gesinnung"],
  "Das Zitat folgt [[DEU.6.5]]; dort stehen «Herz», «Seele» und «Kraft» (hebräisch məʾōḏ). Matthäus nennt drei Glieder und hat statt «Kraft» διάνοια «Denken»; Markus hat vier ([[MRK.12.30]]). «Denken» wie in der Markus-Übersetzung."),
 ("MAT.22.39", "ist ihm gleich", "interpretive", "ὁμοία αὐτῇ", None, ["ist ihm ähnlich", "ist ebenso wichtig"],
  "ὅμοιος heisst «gleich, ähnlich». Ob gemeint ist, dass das zweite Gebot gleich gewichtig ist, oder dass es in der Form ähnlich ist (beide beginnen mit «Du sollst lieben»), ist offen. Zitat aus [[LEV.19.18]]."),
 ("MAT.22.40", "hängen", "adapted", "κρέμαται", "hängt", ["beruhen"],
  "Im Griechischen Singular (nach «das ganze Gesetz»); im Deutschen nach den beiden Subjekten Plural. «Das Gesetz und die Propheten» steht für die Schrift insgesamt (vgl. [[MAT.5.17]], [[MAT.7.12]])."),
 ("MAT.22.42", "den Christus", "traditional", "τοῦ χριστοῦ", None, ["den Gesalbten", "den Messias"],
  "Gemeinsame Wiedergabe für das ganze Matthäusevangelium: Χριστός «Christus». Das Wort übersetzt hebräisch māšîaḥ «Gesalbter»; mit Artikel ist es hier deutlich ein Titel, der erwartete Messias. Ebenso [[MAT.23.10]]."),
 ("MAT.22.42", "Davids", "literal", "Τοῦ Δαυίδ", "Der des David", ["Davids Sohn"],
  "Die Antwort setzt die verbreitete Erwartung voraus, der Messias stamme aus Davids Familie (vgl. [[2SA.7.12]]–[[2SA.7.16]]). Matthäus nennt Jesus selbst «Sohn Davids» ([[MAT.1.1]]; vgl. [[MAT.21.9]])."),
 ("MAT.22.43", "im Geist", "interpretive", "ἐν πνεύματι", None, ["durch den Geist", "vom Geist erfüllt", "im heiligen Geist"],
  "Gemeint ist: vom Geist Gottes geleitet, also als inspirierte Rede. Markus hat ἐν τῷ πνεύματι τῷ ἁγίῳ ([[MRK.12.36]])."),
 ("MAT.22.44", "Der Herr sprach zu meinem Herrn", "literal", "Εἶπεν κύριος τῷ κυρίῳ μου", None, None,
  "Zitat aus [[PSA.110.1]]. Im hebräischen Text spricht JHWH zu ʾăḏōnî «meinem Herrn»; die Septuaginta hat beide Male κύριος. Das Argument setzt voraus, dass David der Sprecher des Psalms ist. ὑποκάτω «unter» (in [[PSA.110.1]] und bei RP «Schemel», siehe Alternative)."),
 ("MAT.22.46", "wagte es auch keiner mehr", "literal", "οὐδὲ ἐτόλμησέν τις οὐκέτι", None, None,
  "Abschluss der Streitgespräche seit [[MAT.21.23]]; Matthäus stellt den Satz ans Ende der letzten Frage (bei Markus nach dem Gespräch über das grösste Gebot, [[MRK.12.34]])."),
 ("MAT.23.2", "Auf den Stuhl des Mose haben sich", "interpretive", "Ἐπὶ τῆς Μωϋσέως καθέδρας ἐκάθισαν", None, ["Auf dem Stuhl des Mose sitzen", "Den Lehrstuhl des Mose haben eingenommen"],
  "καθέδρα ist der Sitz des Lehrenden; der «Stuhl des Mose» steht für die Lehrautorität in der Auslegung der Tora. Ob auch ein wirklicher Sitz in Synagogen gemeint ist, wie ihn spätere Funde und Quellen bezeugen, ist umstritten. Der Aorist ἐκάθισαν kann sagen, dass sie diese Stellung eingenommen haben, oder zeitlos «sie sitzen»; die Übersetzung wählt das Erste."),
 ("MAT.23.2", "die Schriftgelehrten", "literal", "οἱ γραμματεῖς", None, ["die Gesetzeslehrer", "die Schreiber"],
  "Gemeinsame Wiedergabe für das ganze Matthäusevangelium. γραμματεύς bezeichnet die Kundigen der Schrift und ihrer Auslegung; sie gehörten verschiedenen Gruppen an, viele den Pharisäern. Die Rede nennt beide Gruppen meist zusammen."),
 ("MAT.23.3", "das tut und haltet", "literal", "ποιήσατε καὶ τηρεῖτε", None, None,
  "Die Aufforderung steht in Spannung zur Warnung vor der Lehre der Pharisäer und Sadduzäer ([[MAT.16.12]]) und zur Kritik an ihren Überlieferungen ([[MAT.15.1]]–[[MAT.15.20]]). Gedeutet wird etwa: soweit sie aus Mose lesen; als zugespitzte, ironische Aussage; als ältere Überlieferung, die Matthäus aufnimmt. Die Übersetzung gibt den Satz uneingeschränkt wieder, wie er dasteht."),
 ("MAT.23.4", "schwere Lasten", "literal", "φορτία βαρέα", None, None,
  "Bild für Auslegungen und Vorschriften, die das Leben belasten; vgl. Jesu «leichte Last» ([[MAT.11.30]], dasselbe Wort φορτίον). Der SBLGNT liest mit WH ohne καὶ δυσβάστακτα «und schwer zu tragende» (siehe Alternative)."),
 ("MAT.23.4", "mit ihrem Finger nicht bewegen", "literal", "τῷ δακτύλῳ αὐτῶν οὐ θέλουσιν κινῆσαι αὐτά", None, ["keinen Finger rühren, um sie zu tragen"],
  "Gemeint ist wohl: Sie helfen nicht, die Lasten zu tragen oder zu erleichtern. Manche verstehen: Sie halten sich selbst nicht daran."),
 ("MAT.23.5", "Gebetsriemen", "interpretive", "φυλακτήρια", "Schutzmittel", ["Gebetskapseln", "Phylakterien", "Tefillin"],
  "Gemeint sind die Kapseln mit Schriftworten, die nach [[DEU.6.8]] und [[DEU.11.18]] beim Gebet an Stirn und Arm getragen werden (hebräisch təp̄illîn). Das griechische Wort heisst sonst «Amulett, Schutzmittel»; ob Matthäus damit eine Wertung verbindet, ist offen. Breit gemacht werden die Riemen bzw. Kapseln."),
 ("MAT.23.5", "die Quasten", "literal", "τὰ κράσπεδα", None, ["die Fransen", "die Schaufäden"],
  "Die Quasten an den Ecken des Obergewands nach [[NUM.15.38]]–[[NUM.15.39]] (hebräisch ṣîṣiṯ). Auch Jesus trug sie ([[MAT.9.20]], [[MAT.14.36]]). Kritisiert wird nicht der Brauch, sondern das Zur-Schau-Stellen."),
 ("MAT.23.6", "Ehrenplatz", "literal", "πρωτοκλισίαν", "ersten Liegeplatz", ["obersten Platz"],
  "Der Platz neben dem Gastgeber beim Liegen zu Tisch. πρωτοκαθεδρίαι «Ehrensitze» sind die vorderen Sitze in der Synagoge. Wortwahl wie in der Markus-Übersetzung ([[MRK.12.39]])."),
 ("MAT.23.7", "Rabbi", "literal", "Ῥαββί", None, ["Meister", "Lehrer"],
  "Hebräisch-aramäisch «mein Grosser», respektvolle Anrede eines Lehrers. Die Umschrift ist beibehalten, weil [[MAT.23.8]] gerade dieses Wort aufnimmt."),
 ("MAT.23.8", "sollt euch nicht «Rabbi» nennen lassen", "adapted", "μὴ κληθῆτε", "sollt nicht gerufen werden", ["lasst euch nicht nennen"],
  "Aorist Konjunktiv mit μή als Verbot. Angesprochen sind die Menschenmengen und die Jünger ([[MAT.23.1]]); in [[MAT.23.13]] wechselt die Anrede zu den Schriftgelehrten und Pharisäern."),
 ("MAT.23.8", "Brüder", "literal", "ἀδελφοί", None, ["Geschwister"],
  "Der Plural schliesst nach antikem Sprachgebrauch Frauen nicht aus; die Übersetzung bleibt beim Wortlaut."),
 ("MAT.23.9", "nennt keinen auf der Erde euren Vater", "interpretive", "πατέρα μὴ καλέσητε ὑμῶν ἐπὶ τῆς γῆς", "Vater nennt nicht von euch auf der Erde", ["nennt niemanden unter euch auf der Erde Vater"],
  "ὑμῶν kann zu «Vater» gehören («euren Vater») oder partitiv sein («keinen von euch»). «Vater» war auch Ehrentitel verehrter Lehrer. Zu «der himmlische» (ὁ οὐράνιος) vgl. die gemeinsame Wiedergabe «himmlischer Vater» ([[MAT.6.14]])."),
 ("MAT.23.10", "Lehrmeister", "interpretive", "καθηγηταί", None, ["Führer", "Lehrer", "Wegweiser"],
  "καθηγητής kommt im Neuen Testament nur in diesem Vers vor (zweimal) und meint einen Lehrer und Leiter. «Lehrmeister» unterscheidet das Wort von διδάσκαλος «Lehrer» in [[MAT.23.8]]."),
 ("MAT.23.11", "soll euer Diener sein", "adapted", "ἔσται", "wird … sein", None,
  "Das Futur hat hier den Sinn einer Weisung. Vgl. [[MAT.20.26]]–[[MAT.20.27]]."),
 ("MAT.23.12", "wird erniedrigt werden", "interpretive", "ταπεινωθήσεται", None, ["wird gedemütigt werden"],
  "Das Passiv lässt den Handelnden offen; viele verstehen es als Umschreibung für Gottes Handeln. Ebenso «wird erhöht werden». Vgl. [[MAT.18.4]], [[LUK.14.11]]."),
 ("MAT.23.13", "Wehe", "literal", "Οὐαὶ", None, ["Weh euch", "Ach, ihr"],
  "οὐαί ist Klage und Drohung zugleich, wie die Weherufe der Propheten (z. B. [[ISA.5.8]]–[[ISA.5.22]]). Die Rede enthält im SBLGNT-Text sieben Weherufe ([[MAT.23.13]], [[MAT.23.15]], [[MAT.23.16]], [[MAT.23.23]], [[MAT.23.25]], [[MAT.23.27]], [[MAT.23.29]]). ὅτι danach ist jeweils mit «denn» wiedergegeben."),
 ("MAT.23.13", "die hineinwollen", "adapted", "τοὺς εἰσερχομένους", "die Hineingehenden", ["die hineingehen wollen"],
  "Präsens mit dem Sinn des Versuchs: die im Begriff sind hineinzugehen."),
 ("MAT.23.15", "Proselyten", "literal", "προσήλυτον", None, ["einen Übergetretenen", "einen Anhänger"],
  "προσήλυτος ist ein Nichtjude, der zum Judentum übergetreten ist. Wie verbreitet eine gezielte Werbung von Proselyten war, ist in der Forschung umstritten."),
 ("MAT.23.15", "zu gewinnen", "adapted", "ποιῆσαι", "zu machen", None, None),
 ("MAT.23.15", "der Hölle", "interpretive", "γεέννης", "der Gehenna", ["des Gehinnom"],
  "γέεννα ist das Tal Hinnom bei Jerusalem (hebräisch gê hinnōm), Ort früherer Kinderopfer ([[JER.7.31]]), später Bild für den Ort des endzeitlichen Gerichts. «Hölle» wie in der Markus-Übersetzung ([[MRK.9.43]]); ebenso [[MAT.23.33]]. «Sohn der Hölle» ist eine semitische Wendung: einer, der der Hölle gehört."),
 ("MAT.23.15", "doppelt so schlimm wie ihr", "adapted", "διπλότερον ὑμῶν", "doppelt mehr als ihr", None, None),
 ("MAT.23.16", "das gilt nichts", "adapted", "οὐδέν ἐστιν", "ist nichts", ["ist nicht verbindlich"],
  "Gemeint ist: Ein solcher Schwur verpflichtet nicht. Ebenso [[MAT.23.18]]. Vgl. Jesu grundsätzliches Wort zum Schwören in [[MAT.5.33]]–[[MAT.5.37]]."),
 ("MAT.23.16", "ist gebunden", "adapted", "ὀφείλει", "schuldet", ["ist verpflichtet"],
  "ὀφείλω heisst «schulden»: Wer so schwört, schuldet die Erfüllung seines Schwurs. Ebenso [[MAT.23.18]]."),
 ("MAT.23.16", "ihr blinden Führer", "literal", "ὁδηγοὶ τυφλοὶ", None, ["ihr blinden Wegführer"],
  "Vgl. [[MAT.15.14]]. Ebenso [[MAT.23.24]]."),
 ("MAT.23.17", "Ihr Narren", "literal", "μωροὶ", None, ["Ihr Toren", "Ihr Dummen"],
  "In [[MAT.5.22]] verbietet Jesus, jemanden μωρέ zu nennen; die Spannung wird verschieden erklärt (prophetische Anklage gegenüber persönlicher Beschimpfung u. a.). Die Übersetzung mildert nicht."),
 ("MAT.23.18", "Und:", "adapted", "καί", "Und", ["Und ihr sagt:"],
  "καί führt ein zweites Beispiel derselben Lehre ein; «ihr sagt» ist aus [[MAT.23.16]] zu ergänzen."),
 ("MAT.23.21", "dem, der ihn bewohnt", "literal", "τῷ κατοικοῦντι αὐτόν", None, None,
  "Gemeint ist Gott, der im Tempel wohnt (vgl. [[1KI.8.13]], [[PSA.135.21]]). Ebenso ist in [[MAT.23.22]] mit dem, der auf dem Thron sitzt, Gott gemeint."),
 ("MAT.23.23", "ihr gebt den Zehnten", "literal", "ἀποδεκατοῦτε", None, ["ihr verzehntet"],
  "Zum Zehnten von den Erträgen des Landes vgl. [[LEV.27.30]] und [[DEU.14.22]]. Minze, Dill und Kümmel sind Gartenkräuter; ob sie zehntpflichtig waren, wurde damals diskutiert. κύμινον ist der Kreuzkümmel."),
 ("MAT.23.23", "das Recht", "interpretive", "τὴν κρίσιν", "das Gericht", ["die Gerechtigkeit", "das gerechte Urteil"],
  "κρίσις heisst «Gericht, Urteil, Recht». Zusammen mit «Barmherzigkeit» und «Treue» erinnert die Reihe an prophetische Weisung wie [[MIC.6.8]] (Recht und Güte) und [[HOS.12.6]] (Güte und Recht). In [[MAT.23.33]] ist κρίσις mit «Gericht» wiedergegeben."),
 ("MAT.23.23", "die Barmherzigkeit", "literal", "τὸ ἔλεος", None, ["das Erbarmen"],
  "Vgl. [[MAT.9.13]] und [[MAT.12.7]] (Zitat aus [[HOS.6.6]])."),
 ("MAT.23.23", "die Treue", "interpretive", "τὴν πίστιν", None, ["den Glauben", "die Zuverlässigkeit"],
  "πίστις ist im Matthäusevangelium sonst mit «Glaube» wiedergegeben (z. B. [[MAT.8.10]], [[MAT.9.2]], [[MAT.17.20]]). Hier steht das Wort in einer Reihe mit Recht und Barmherzigkeit, die an prophetische Weisung anknüpft; dort meint es die Treue, die Verlässlichkeit im Verhalten gegenüber Gott und Menschen (hebräisch ʾĕmûnāh). Bewusste Ausnahme von der einheitlichen Wiedergabe; redaktionelle Entscheidung."),
 ("MAT.23.23", "Dies hätte man tun und jenes nicht beiseitelassen sollen", "adapted", "ταῦτα ἔδει ποιῆσαι κἀκεῖνα μὴ ἀφιέναι", "dies war nötig zu tun und jenes nicht zu lassen", ["Dies sollte man tun und jenes nicht lassen"],
  "«Dies» meint das Gewichtigere (Recht, Barmherzigkeit, Treue), «jenes» den Zehnten: Jesus verwirft den Zehnten nicht. ἀφίημι ist im ganzen Vers mit «beiseitelassen» wiedergegeben."),
 ("MAT.23.24", "die ihr die Mücke aussiebt", "literal", "οἱ διϋλίζοντες τὸν κώνωπα", None, ["die ihr die Mücke aussieht", "die ihr die Mücke herausfiltert"],
  "Man seihte Wein durch ein Tuch, um kleine Tiere zu entfernen, die als unrein galten ([[LEV.11.20]]–[[LEV.11.23]], [[LEV.11.41]]); auch das Kamel ist unrein ([[LEV.11.4]]). Bildhafte Übertreibung. Ein Wortspiel im Aramäischen (qalmāʾ «Mücke», gamlāʾ «Kamel») wird vermutet."),
 ("MAT.23.25", "Masslosigkeit", "literal", "ἀκρασίας", None, ["Unbeherrschtheit", "Gier"],
  "ἀκρασία ist der Mangel an Selbstbeherrschung. Ob der Inhalt der Gefässe (durch Raub erworben) oder das Innere der Menschen gemeint ist, verschwimmt im Bild; [[MAT.23.26]] und [[MAT.23.28]] beziehen es auf die Menschen. RP liest ἀδικίας «Ungerechtigkeit» (siehe Alternative)."),
 ("MAT.23.26", "Du blinder Pharisäer", "literal", "Φαρισαῖε τυφλέ", None, None,
  "Einzige Anrede in der Einzahl in den Weherufen."),
 ("MAT.23.27", "weiss getünchten Gräbern", "literal", "τάφοις κεκονιαμένοις", None, ["geweisselten Gräbern"],
  "Gräber machen unrein ([[NUM.19.16]]). Nach späteren rabbinischen Quellen wurden Gräber mit Kalk gekennzeichnet, damit niemand sich unwissentlich verunreinigte; ob Matthäus daran oder an verzierende Tünche denkt, ist offen."),
 ("MAT.23.28", "Gesetzlosigkeit", "literal", "ἀνομίας", None, ["Unrecht", "Gottlosigkeit"],
  "ἀνομία heisst wörtlich das Fehlen bzw. Missachten des Gesetzes; bei Matthäus auch [[MAT.7.23]], [[MAT.13.41]] und [[MAT.24.12]]. Gerade Gesetzeskundigen wird hier Gesetzlosigkeit vorgeworfen."),
 ("MAT.23.29", "die Grabmäler der Gerechten", "literal", "τὰ μνημεῖα τῶν δικαίων", None, ["die Denkmäler der Gerechten"],
  "δίκαιος «gerecht» bezeichnet hier Menschen, die nach Gottes Willen lebten, wie die Propheten; vgl. [[MAT.23.35]]."),
 ("MAT.23.30", "gelebt hätten", "adapted", "ἤμεθα", "gewesen wären", None,
  "Dasselbe Verb steht zweimal im Satz («gewesen wären», «wären … gewesen»); das erste ist mit «gelebt hätten» wiedergegeben."),
 ("MAT.23.32", "Macht das Mass eurer Väter voll", "interpretive", "πληρώσατε τὸ μέτρον τῶν πατέρων ὑμῶν", None, ["Füllt nur das Mass eurer Väter auf", "So macht doch das Mass voll"],
  "Imperativ mit ironischem oder herausforderndem Sinn: Sie sollen vollenden, was die Väter begonnen haben. Vorgestellt ist ein Mass von Schuld, das voll werden muss, bevor das Gericht kommt."),
 ("MAT.23.33", "ihr Vipernbrut", "literal", "γεννήματα ἐχιδνῶν", "Erzeugnisse von Vipern", ["ihr Natternbrut", "ihr Schlangenbrut", "ihr Otterngezücht"],
  "Gemeinsame Wiedergabe für das ganze Matthäusevangelium. Dieselbe Anrede bei Johannes dem Täufer ([[MAT.3.7]]) und bei Jesus ([[MAT.12.34]])."),
 ("MAT.23.33", "dem Gericht der Hölle", "interpretive", "τῆς κρίσεως τῆς γεέννης", None, ["der Verurteilung zur Hölle"],
  "Gemeint ist das Urteil, das zur Hölle verurteilt. φύγητε (Konjunktiv) in einer Frage der Überlegung: «Wie wollt ihr entkommen?»"),
 ("MAT.23.34", "Weise", "literal", "σοφοὺς", None, ["Weisheitslehrer"],
  "Propheten, Weise und Schriftgelehrte: Gesandte, wie sie Matthäus wohl auch in der Gemeinde seiner Zeit kennt. Lukas leitet das Wort mit «die Weisheit Gottes sagt» ein ([[LUK.11.49]]); bei Matthäus spricht Jesus selbst («ich sende»)."),
 ("MAT.23.35", "Secharjas, des Sohnes Berechjas", "interpretive", "Ζαχαρίου υἱοῦ Βαραχίου", None, ["des Zacharias, des Sohnes des Barachias"],
  "Abel ist das erste Opfer eines Mordes in der Schrift ([[GEN.4.8]]). Im Tempelvorhof gesteinigt wurde nach [[2CH.24.20]]–[[2CH.24.22]] Secharja, der Sohn Jojadas; Chronik steht in der hebräischen Bibel am Ende, sodass «von Abel bis Secharja» die ganze Schrift umspannen würde. Secharja, der Sohn Berechjas, ist der Prophet von [[ZEC.1.1]]. Als Erklärungen werden genannt: eine Verwechslung oder Verschmelzung der beiden Gestalten; eine andere Person (Josephus berichtet von einem Zacharias, Sohn des Baris, der im Tempel getötet wurde). Lukas hat den Vaternamen nicht ([[LUK.11.51]]). Die Übersetzung gibt den Text wieder, ohne zu harmonisieren; Namensformen nach dem Hebräischen."),
 ("MAT.23.36", "dieses Geschlecht", "literal", "τὴν γενεὰν ταύτην", None, ["diese Generation"],
  "γενεά meint die Menschen einer Zeit, die Zeitgenossen. «Geschlecht» wie in der Markus-Übersetzung ([[MRK.13.30]]); vgl. [[MAT.24.34]]."),
 ("MAT.23.37", "die die Propheten tötet und die steinigt, die zu ihr gesandt sind", "literal", "ἡ ἀποκτείνουσα τοὺς προφήτας καὶ λιθοβολοῦσα τοὺς ἀπεσταλμένους πρὸς αὐτήν", None, ["die du die Propheten tötest und die steinigst, die zu dir gesandt sind"],
  "Die Anrede an Jerusalem steht mit Partizipien in der dritten Person («zu ihr»), dann wechselt sie zu «deine Kinder» und «ihr». Die Übersetzung behält den Wechsel bei, statt ihn zu glätten."),
 ("MAT.23.37", "wie eine Henne ihre Küken", "literal", "ὃν τρόπον ὄρνις ἐπισυνάγει τὰ νοσσία αὐτῆς", None, None,
  "ὄρνις ist allgemein ein Vogel, meist die Henne. Das Bild vom Schutz unter Flügeln kennt die Schrift auch für Gott (z. B. [[PSA.91.4]], [[DEU.32.11]])."),
 ("MAT.23.38", "euer Haus", "interpretive", "ὁ οἶκος ὑμῶν", None, ["euer Tempel", "eure Stadt"],
  "«Haus» kann den Tempel, die Stadt oder das Volk meinen; vgl. [[JER.22.5]] und [[JER.12.7]]. Die Übersetzung bleibt beim offenen Wort."),
 ("MAT.23.38", "verödet", "literal", "ἔρημος", None, ["verlassen", "wüst"],
  "ἔρημος heisst «öde, verlassen» (vgl. ἔρημος «Wüste»). WH haben das Wort nicht (siehe Alternative)."),
 ("MAT.23.39", "Gesegnet sei der, der kommt im Namen des Herrn", "literal", "Εὐλογημένος ὁ ἐρχόμενος ἐν ὀνόματι κυρίου", None, ["Gesegnet ist, der kommt im Namen des Herrn"],
  "Zitat aus [[PSA.118.26]], wie beim Einzug in Jerusalem ([[MAT.21.9]]). Ohne Verb im Griechischen; «sei» als Segenswunsch wie in der Markus-Übersetzung ([[MRK.11.9]]). οὐ μή mit Konjunktiv ist eine verstärkte Verneinung («gewiss nicht»), hier mit «von jetzt an nicht mehr» wiedergegeben."),
]

DEC_GSW = [
 ('MAT.22.19', 'en Denar', 'literal', 'δηνάριον', None, None, 'Römischi Silbermünz mit Bild und Ufschrift vom Kaiser, öppe en Taglohn ([[MAT.20.2]]). Damalige Münzname im Text, de Wärt i de Erkläärig (Entscheid Andi Neck 2026-10-26).'),
 ("MAT.22.1", "hät gantwortet", "literal", "ἀποκριθεὶς", None, ["hät s Wort gnoo"],
  "Es Frag gaat nöd voruus; s Gliichnis gaat uf d Laag vo [[MAT.21.45]]–[[MAT.21.46]] ii."),
 ("MAT.22.2", "S Riich vo de Himel", "literal", "ἡ βασιλεία τῶν οὐρανῶν", None, ["s Himelriich", "s Riich vo Gott"],
  "Gmeinsami Widergab fürs ganz Matthäusevangelium. De Matthäus seit meischtens «Riich vo de Himel», wo de Markus und de Lukas «Riich vo Gott» händ; «Himel» gilt vilne als ehrfürchtigi Umschriibig für Gott."),
 ("MAT.22.2", "isch eme König gliich worde", "adapted", "Ὡμοιώθη ἀνθρώπῳ βασιλεῖ", "isch gliich worde eme Mänsch, eme König", ["Mit em Riich vo de Himel isch es wie mit eme König"],
  "ὡμοιώθη (Aorist Passiv) heisst «isch gliich worde»; so faat de Matthäus au [[MAT.13.24]] und [[MAT.18.23]] aa. Vergliche wird di ganz Gschicht, nöd nu de König."),
 ("MAT.22.3", "Chnächt", "literal", "δούλους", None, ["Sklave", "Diener"],
  "δοῦλος isch en unfreie Diener; «Chnächt» wie i de Markus-Übersetzig. D διάκονοι i [[MAT.22.13]] heissed «Diener»."),
 ("MAT.22.3", "Iigladne", "literal", "κεκλημένους", None, None,
  "Perfekt: D Gäscht sind scho früener iiglade worde; jetzt wärded si grüeft, wil s Fäscht aafaat."),
 ("MAT.22.7", "hät iri Stadt aazündt", "literal", "τὴν πόλιν αὐτῶν ἐνέπρησεν", None, None,
  "Vili gsehnd drin en Rückblick uf d Zerstörig vo Jerusalem im Jahr 70; anderi säged, Strafzüüg gäge Stedt seigid es verbreitets Motiv i Gschichte über König. De Text nännt kei Stadt."),
 ("MAT.22.9", "a d Usgäng vo de Strasse", "interpretive", "ἐπὶ τὰς διεξόδους τῶν ὁδῶν", None, ["a d Chrüüzige"],
  "διέξοδος isch de Ort, wo e Strass is offe Land usegaat, oder e Wägchrüüzig: wo vil Lüüt verbiichömed."),
 ("MAT.22.13", "i d Fiischteri dusse", "literal", "εἰς τὸ σκότος τὸ ἐξώτερον", None, ["i di üsserscht Fiischteri"],
  "Gliichi Wändig i [[MAT.8.12]] und [[MAT.25.30]]. Gmeinsami Widergab: «s Hüüle und s Zändchnirsche»; κλαυθμός heisst «Hüüle, Wehklage»."),
 ("MAT.22.14", "iiglade", "interpretive", "κλητοὶ", "grüeft", ["berüeft"],
  "κλητός ghört zu καλέω, em Leitwort vom Gliichnis («Iigladni»). ἐκλεκτοί isch «userwählt»."),
 ("MAT.22.16", "de Herodianer", "literal", "τῶν Ἡρῳδιανῶν", None, ["de Aahänger vom Herodes"],
  "Aahänger vo de Herrscherfamilie vom Herodes; wer gnau dezue ghört hät, isch unklar."),
 ("MAT.22.17", "Stüür", "literal", "κῆνσον", None, ["Chopfstüür"],
  "κῆνσος isch s latiinisch census, d Chopfstüür für Rom. «Kaiser» isch de regierend Kaiser, zur Ziit vom Jesus de Tiberius."),
 ("MAT.22.18", "ir Hüüchler", "literal", "ὑποκριταί", None, ["ir Schiiheilige", "ir Schauspiler"],
  "Gmeinsami Widergab fürs ganz Matthäusevangelium. ὑποκριτής heisst ursprünglich «Schauspiler»: öpper, wo sis Tue nöd zu däm passt, was er zeigt oder seit."),
 ("MAT.22.21", "Gänd", "interpretive", "Ἀπόδοτε", "Gänd zrugg", ["Zaled"],
  "ἀποδίδωμι heisst «zruggää, abgää, was mer schuldig isch»; d Übersetzig bliibt bi «gää» wie i [[MRK.12.17]]."),
 ("MAT.22.24", "söll sin Brüeder sini Frau hürate", "adapted", "ἐπιγαμβρεύσει ὁ ἀδελφὸς αὐτοῦ τὴν γυναῖκα αὐτοῦ", "wird sin Brüeder sini Frau als Schwager hürate", None,
  "Futur als Gebot. Schwagerehe (Leviratsehe) nach [[DEU.25.5]]–[[DEU.25.6]]."),
 ("MAT.22.24", "Nachkomme verschaffe", "adapted", "ἀναστήσει σπέρμα", "wird Same ufstaa laa", ["Nachkomme erwecke"],
  "ἀνίστημι isch s gliich Verb wie bi ἀνάστασις «Uferstehig»; s Wortspiel gaat i de Mundart verlore."),
 ("MAT.22.30", "wie Ängel vo Gott im Himel", "literal", "ὡς ἄγγελοι θεοῦ ἐν τῷ οὐρανῷ", None, ["wie Ängel im Himel"],
  "De SBLGNT list θεοῦ mit Holmes; WH, Treg und NA28 händ s Wort nöd (lueg d Alternative)."),
 ("MAT.22.32", "Er isch nöd de Gott vo Tote", "interpretive", "οὐκ ἔστιν ὁ θεὸς νεκρῶν", None, ["Gott isch nöd en Gott vo Tote"],
  "Zitat us [[EXO.3.6]]. Es Subjekt fehlt im Griechische."),
 ("MAT.22.33", "d Lüüt", "adapted", "οἱ ὄχλοι", "d Mängene", ["d Mängi"],
  "Gmeinsami Widergab fürs ganz Matthäusevangelium: ὄχλος «d Mängi», de Plural οἱ ὄχλοι «d Lüüt». Gliich i [[MAT.23.1]]."),
 ("MAT.22.35", "en Gsetzeslehrer", "literal", "νομικὸς", None, ["en Schriftgelehrte"],
  "νομικός, en Kenner vom Gsetz, staat bim Matthäus nu da; de Markus seit «Schriftgleerte» ([[MRK.12.28]])."),
 ("MAT.22.36", "isch s gröscht", "adapted", "μεγάλη", "isch gross", None,
  "De Positiv staat für de Superlativ. Gliich i [[MAT.22.38]]."),
 ("MAT.22.37", "Dänke", "literal", "διανοίᾳ", None, ["Verstand"],
  "Zitat us [[DEU.6.5]]; dört staat statt «Dänke» «Chraft». De Markus nännt vier Glider ([[MRK.12.30]])."),
 ("MAT.22.42", "de Christus", "traditional", "τοῦ χριστοῦ", None, ["de Gsalbt", "de Messias"],
  "Gmeinsami Widergab: Χριστός «Christus»; s Wort übersetzt hebräisch māšîaḥ «Gsalbte». Gliich i [[MAT.23.10]]."),
 ("MAT.22.43", "im Geischt", "interpretive", "ἐν πνεύματι", None, ["dur de Geischt"],
  "Vom Geischt vo Gott gleitet. De Markus seit «im Heilige Geischt» ([[MRK.12.36]])."),
 ("MAT.22.44", "De Herr hät zu mim Herr gseit", "literal", "Εἶπεν κύριος τῷ κυρίῳ μου", None, None,
  "Zitat us [[PSA.110.1]]; im hebräische Text redt JHWH zu «mim Herr»."),
 ("MAT.23.2", "Uf de Stuel vom Mose händ sich", "interpretive", "Ἐπὶ τῆς Μωϋσέως καθέδρας ἐκάθισαν", None, ["Uf em Stuel vom Mose sitzed"],
  "De «Stuel vom Mose» staat für d Lehrautorität bi de Uslegig vo de Tora. Öb au en würkliche Sitz i de Synagoge gmeint isch, isch umstritte."),
 ("MAT.23.2", "d Schriftgelehrte", "literal", "οἱ γραμματεῖς", None, ["d Gsetzeslehrer"],
  "Gmeinsami Widergab: Schriftgelehrti (mit Artikel «d Schriftgelehrte»)."),
 ("MAT.23.3", "das mached und halted", "literal", "ποιήσατε καὶ τηρεῖτε", None, None,
  "De Satz staat in Spannig zu [[MAT.16.12]] und [[MAT.15.1]]–[[MAT.15.20]]. Me düütet en verschide (soviel si us em Mose läsed; ironisch; elteri Überlieferig); d Übersetzig git en wider, wie n er staat."),
 ("MAT.23.3", "richted eu nöd", "adapted", "μὴ ποιεῖτε", "mached nöd", None, None),
 ("MAT.23.5", "Gebetsrieme", "interpretive", "φυλακτήρια", "Schutzmittel", ["Gebetschapsle", "Tefillin"],
  "D Chapsle mit Schriftwort, wo nach [[DEU.6.8]] bim Bätte a de Stirn und am Arm treit wärded (hebräisch təp̄illîn)."),
 ("MAT.23.5", "d Quaste", "literal", "τὰ κράσπεδα", None, ["d Franse"],
  "D Quaste a de Egge vom Obergwand nach [[NUM.15.38]]–[[NUM.15.39]]; au de Jesus hät si treit ([[MAT.9.20]])."),
 ("MAT.23.10", "Lehrmeischter", "interpretive", "καθηγηταί", None, ["Füerer", "Lehrer"],
  "καθηγητής chunnt im Neue Teschtament nu i dem Vers vor; «Lehrmeischter» underscheidet s vo διδάσκαλος «Lehrer»."),
 ("MAT.23.12", "wird erniedriget", "interpretive", "ταπεινωθήσεται", None, ["wird chlii gmacht"],
  "S Passiv laat offe, wer handlet; vili verstönd s als Umschriibig für s Handle vo Gott."),
 ("MAT.23.13", "Weh", "literal", "Οὐαὶ", None, None,
  "οὐαί isch Klag und Drohig zäme, wie bi de Prophete. Sibe Weherüef im SBLGNT-Text; ὅτι isch jedesmal «dänn»."),
 ("MAT.23.15", "Proselyt", "literal", "προσήλυτον", None, ["Übergetrettene"],
  "En Nichtjud, wo zum Judetum übertrette isch."),
 ("MAT.23.15", "vo de Höll", "interpretive", "γεέννης", "vo de Gehenna", None,
  "γέεννα isch s Tal Hinnom bi Jerusalem, spöter es Bild für de Ort vom Gricht. «Höll» wie i de Markus-Übersetzig."),
 ("MAT.23.16", "isch draa bunde", "adapted", "ὀφείλει", "schuldet", ["isch verpflichtet"],
  "Wer so schwört, schuldet, was er gschwore hät. Gliich i [[MAT.23.18]]."),
 ("MAT.23.17", "Ir Narre", "literal", "μωροὶ", None, ["Ir Dummchöpf"],
  "I [[MAT.5.22]] verbütet de Jesus, öpperem μωρέ z säge; d Übersetzig milderet nöd."),
 ("MAT.23.23", "d Treui", "interpretive", "τὴν πίστιν", None, ["de Glaube"],
  "πίστις isch im Matthäusevangelium susch «Glaube». Da staat s Wort näbe Rächt und Barmherzigkeit (vgl. [[MIC.6.8]]) und meint d Treui, d Verlässlichkeit. Bewussti Usnahm; redaktionelle Entscheid."),
 ("MAT.23.23", "s Rächt", "interpretive", "τὴν κρίσιν", "s Gricht", ["d Grächtigkeit"],
  "κρίσις heisst «Gricht, Urteil, Rächt»; i [[MAT.23.33]] «Gricht»."),
 ("MAT.23.23", "Chümi", "adapted", "κύμινον", None, ["Chrüüzchümi"],
  "Gmeint isch de Chrüüzchümi."),
 ("MAT.23.24", "d Mugge ussiebed", "literal", "διϋλίζοντες τὸν κώνωπα", None, None,
  "Mer hät de Wii dur es Tuech gsiebt, wil chliini Tierli als unrein gulte händ ([[LEV.11.41]]); au s Kamel isch unrein ([[LEV.11.4]]). Bildhafti Übertriibig."),
 ("MAT.23.27", "wiissgstricheni Greber", "literal", "τάφοις κεκονιαμένοις", None, None,
  "Greber mached unrein ([[NUM.19.16]]); nach spööteren rabbinische Quälle hät mer s mit Chalch zeichnet."),
 ("MAT.23.32", "Mached s Mass vo eune Vätere voll", "interpretive", "πληρώσατε τὸ μέτρον τῶν πατέρων ὑμῶν", None, None,
  "Imperativ mit ironischem Sinn: Si söled fertig mache, was d Väter aagfange händ."),
 ("MAT.23.33", "ir Viperebruet", "literal", "γεννήματα ἐχιδνῶν", "Bruet vo Vipere", ["ir Schlangebruet", "ir Natterebruet"],
  "Gmeinsami Widergab fürs ganz Matthäusevangelium; di gliich Aared bim Johannes em Täufer ([[MAT.3.7]]) und bim Jesus ([[MAT.12.34]])."),
 ("MAT.23.35", "vom Secharja, em Sohn vom Berechja", "interpretive", "Ζαχαρίου υἱοῦ Βαραχίου", None, ["vom Zacharias, em Sohn vom Barachias"],
  "Im Tämpelvorhof gsteiniget worde isch nach [[2CH.24.20]]–[[2CH.24.22]] de Secharja, de Sohn vom Jojada; de Secharja, de Sohn vom Berechja, isch de Prophet vo [[ZEC.1.1]]. Erkläärige: e Verwächslig oder Verschmelzig; en anderi Person (de Josephus verzellt vo me Zacharias, Sohn vom Baris). D Übersetzig harmonisiert nöd."),
 ("MAT.23.36", "die Generation", "literal", "τὴν γενεὰν ταύτην", None, ["das Gschlächt"],
  "γενεά meint d Mänsche vo ere Ziit; «Generation» wie i de Markus-Übersetzig ([[MRK.13.30]])."),
 ("MAT.23.37", "wo d Prophete umbringt", "literal", "ἡ ἀποκτείνουσα τοὺς προφήτας", None, ["wo du d Prophete umbringsch"],
  "D Aared a Jerusalem staat zerscht i de dritte Person («zu ire»), dänn wächslet si zu «dini Chind» und «ir». D Übersetzig laat de Wächsel staa."),
 ("MAT.23.38", "eues Huus", "interpretive", "ὁ οἶκος ὑμῶν", None, ["eue Tämpel", "eui Stadt"],
  "«Huus» cha de Tämpel, d Stadt oder s Volch meine; vgl. [[JER.22.5]]."),
 ("MAT.23.39", "Gsägnet sig dä, wo chunnt im Name vom Herr", "literal", "Εὐλογημένος ὁ ἐρχόμενος ἐν ὀνόματι κυρίου", None, None,
  "Zitat us [[PSA.118.26]], wie bim Iizug z Jerusalem ([[MAT.21.9]])."),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung).
V14_DE = ("Wehe euch, Schriftgelehrte und Pharisäer, ihr Heuchler, denn ihr fresst die Häuser der Witwen auf und betet "
          "zum Schein lange; darum werdet ihr ein umso härteres Urteil empfangen.")
V14_GSW = ("Weh eu, Schriftgelehrti und Pharisäer, ir Hüüchler, dänn ir frässed d Hüüser vo de Witwe uf und bätted zum "
           "Schii lang; drum wärded ir es umso härters Urteil überchoo.")
V14_ORIGIN_DE = ("Der Weheruf entspricht wörtlich weitgehend [[MRK.12.40]] und [[LUK.20.47]]; er kann von dort in Matthäus "
                 "übernommen worden sein, was auch erklären würde, dass er an zwei verschiedenen Stellen (vor oder nach "
                 "[[MAT.23.13]]) eingefügt ist. Ebenso denkbar ist, dass er beim Abschreiben wegen der gleich beginnenden "
                 "Weherufe ausgefallen ist.")
V14_ORIGIN_GSW = ("De Weheruef entspricht wiitgehend [[MRK.12.40]] und [[LUK.20.47]] und cha vo dört übernoo sii; das würd "
                  "au erkläre, werum er a zwei verschidne Stelle staat. Oder er isch bim Abschriibe usgfalle, wil d "
                  "Weherüef gliich aafanged.")
V14_COLL_DE = ("Die automatische Zuordnung hat nur den Wortlaut am Ende von [[MAT.23.12]] bzw. [[MAT.23.13]] verglichen und "
               "01, 03, 032 und 05 der Lesart ohne Zusatz zugeordnet (04 ist hier nicht erhalten); ob in ihnen der "
               "zusätzliche Vers steht, lässt sich daraus nicht ablesen. Sie ordnet auch die Ausgaben RP und KJTR der "
               "Lesart ohne Zusatz zu; nach dem Apparat hat RP den Vers. Es gilt der Apparat; die Zuordnung ist an dieser "
               "Stelle unzuverlässig.")
V14_COLL_GSW = ("D automatisch Zueornig hät nu de Wortlut am Änd vo [[MAT.23.12]] bzw. [[MAT.23.13]] vergliche und 01, 03, 032 "
                "und 05 de Läsart ohni Zuesatz zueteilt; öb bi ine de zuesätzlich Vers staat, cha mer drus nöd abläse. Si "
                "teilt au d Usgabe RP und KJTR ohni Zuesatz ii; nach em Apparat hät RP de Vers. Es gilt de Apparat.")

ALTS = [
 ("VAR-SBLGNTAPP-MAT-022-007-01:R2", "MAT.22.7", "Der König aber wurde zornig", "Als jener König das hörte, wurde er zornig",
  "De König aber isch toube worde", "Wo säbe König das ghört hät, isch er toube worde", "gering",
  "Mit καὶ ἀκούσας («und als er hörte») reagiert der König ausdrücklich auf die Nachricht vom Mord an seinen Knechten.",
  "Mit καὶ ἀκούσας («und wo er ghört hät») reagiert de König usdrücklich uf d Nachricht vom Mord a sine Chnächt.",
  {"R1": [("ὁ δὲ βασιλεὺς", "Der König aber", "WH, Treg, NA28")], "R2": [("Καὶ ἀκούσας ὁ βασιλεὺς ἐκεῖνος", "Und als jener König das hörte", "RP")]},
  {"R1": [("ὁ δὲ βασιλεὺς", "De König aber", "WH, Treg, NA28")], "R2": [("Καὶ ἀκούσας ὁ βασιλεὺς ἐκεῖνος", "Und wo säbe König das ghört hät", "RP")]},
  ["Die längere Lesart verdeutlicht den Erzählablauf und kann ergänzt worden sein; ebenso kann die kürzere eine Straffung sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 die kürzere Lesart, 032 und 04 die längere."],
  ["Di länger Läsart macht de Ablauf düütlicher und cha ergänzt worde sii; oder di chürzer isch e Straffig.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 di chürzer Läsart, 032 und 04 di länger."]),
 ("VAR-SBLGNTAPP-MAT-022-010-02:R2", "MAT.22.10", "das Hochzeitsfest füllte sich", "der Hochzeitssaal füllte sich",
  "s Hochziitfäscht isch voll", "de Hochziitsaal isch voll", "gering",
  "Mit νυμφών ist der Raum genannt, in dem gefeiert wird, statt des Festes.",
  "Mit νυμφών isch de Ruum gmeint, wo mer fiiret, statt s Fäscht.",
  {"R1": [("γάμος", "das Hochzeitsfest", "Treg, NA28, RP")], "R2": [("νυμφὼν", "der Hochzeitssaal", "WH")]},
  {"R1": [("γάμος", "s Hochziitfäscht", "Treg, NA28, RP")], "R2": [("νυμφὼν", "de Hochziitsaal", "WH")]},
  ["νυμφών passt besser zu «füllte sich» und kann deshalb eingesetzt worden sein; ebenso kann γάμος aus dem Zusammenhang (γάμος in [[MAT.22.8]]) stammen und das seltenere Wort verdrängt haben.",
   "Laut der automatischen Zuordnung lesen 01 und 03 νυμφών (03 von einer Korrektur zu γάμος geändert), 032, 04 und 05 γάμος."],
  ["νυμφών passt besser zu «voll worde» und cha drum iigsetzt worde sii; oder γάμος chunnt us em Zämehang ([[MAT.22.8]]) und hät s sältener Wort verdrängt.",
   "Nach de automatische Zueornig läsed 01 und 03 νυμφών (03 vo ere Korrektur zu γάμος gänderet), 032, 04 und 05 γάμος."]),
 ("VAR-SBLGNTAPP-MAT-022-013-02:R2", "MAT.22.13", "Bindet ihm Füsse und Hände und werft ihn hinaus", "Bindet ihm Füsse und Hände, nehmt ihn weg und werft ihn hinaus",
  "Binded ihm d Füess und d Händ und rüered en use", "Binded ihm d Füess und d Händ, nämed en wäg und rüered en use", "gering",
  "Mit ἄρατε αὐτόν («nehmt ihn weg») wird ein weiterer Schritt des Hinausschaffens genannt.",
  "Mit ἄρατε αὐτόν («nämed en wäg») chunnt en wiitere Schritt dezue.",
  {"R1": [("ἐκβάλετε αὐτὸν", "werft ihn hinaus", "WH, Treg, NA28")], "R2": [("ἄρατε αὐτὸν καὶ ἐκβάλετε", "nehmt ihn weg und werft ihn hinaus", "RP")]},
  {"R1": [("ἐκβάλετε αὐτὸν", "rüered en use", "WH, Treg, NA28")], "R2": [("ἄρατε αὐτὸν καὶ ἐκβάλετε", "nämed en wäg und rüered en use", "RP")]},
  ["Die längere Lesart malt die Szene aus und kann erweitert worden sein; ebenso kann der Zusatz als überflüssig weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 die kürzere Lesart, 032 und 04 die längere."],
  ["Di länger Läsart malt d Szene us und cha erwiitered worde sii; oder de Zuesatz isch als überflüssig wäggfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 di chürzer Läsart, 032 und 04 di länger."]),
 ("VAR-SBLGNTAPP-MAT-022-030-02:R3", "MAT.22.30", "wie Engel Gottes im Himmel", "wie Engel im Himmel",
  "wie Ängel vo Gott im Himel", "wie Ängel im Himel", "gering",
  "Ohne θεοῦ heisst es nur «wie Engel im Himmel», wie in [[MRK.12.25]].",
  "Ohni θεοῦ heisst s nu «wie Ängel im Himel», wie i [[MRK.12.25]].",
  {"R1": [("θεοῦ", "Gottes", "Holmes")], "R2": [("τοῦ θεοῦ", "Gottes", "RP")], "R3": [("–", "(fehlt)", "WH, Treg, NA28")]},
  {"R1": [("θεοῦ", "vo Gott", "Holmes")], "R2": [("τοῦ θεοῦ", "vo Gott", "RP")], "R3": [("–", "(fehlt)", "WH, Treg, NA28")]},
  ["«Engel Gottes» ist eine geläufige Verbindung und kann ergänzt worden sein; ebenso kann das Wort neben «im Himmel» als überflüssig weggelassen oder an [[MRK.12.25]] angeglichen worden sein. Der SBLGNT folgt hier Holmes gegen WH, Treg und NA28.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne θεοῦ, 032 τοῦ θεοῦ (04 ist hier nicht erhalten). Der von der Zuordnung erfasste Wortlaut von 01 enthält jedoch das Kürzel für θεοῦ (αγγελοι θυ); die Zuordnung von 01 zur Lesart ohne θεοῦ ist deshalb fraglich."],
  ["«Ängel vo Gott» isch e gläufigi Verbindig und cha ergänzt worde sii; oder s Wort isch näbe «im Himel» als überflüssig wäggloo oder a [[MRK.12.25]] aaglichen worde. De SBLGNT folgt da em Holmes gäge WH, Treg und NA28.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni θεοῦ, 032 τοῦ θεοῦ. De erfasst Wortlut vo 01 hät aber s Chürzel für θεοῦ; d Zueornig vo 01 isch drum fraglich."]),
 ("VAR-SBLGNTAPP-MAT-022-044-02:R2", "MAT.22.44", "unter deine Füsse lege", "zum Schemel deiner Füsse mache",
  "under dini Füess lege", "zum Schämel vo dine Füess mache", "gering",
  "ὑποπόδιον («Schemel») entspricht dem Wortlaut von [[PSA.110.1]] in der Septuaginta.",
  "ὑποπόδιον («Schämel») entspricht em Wortlut vo [[PSA.110.1]] i de Septuaginta.",
  {"R1": [("ὑποκάτω", "unter", "WH, Treg, NA28")], "R2": [("ὑποπόδιον", "zum Schemel", "RP")]},
  {"R1": [("ὑποκάτω", "under", "WH, Treg, NA28")], "R2": [("ὑποπόδιον", "zum Schämel", "RP")]},
  ["Abschreiber haben Zitate oft an den bekannten Wortlaut der Septuaginta angeglichen; ὑποκάτω kann aus [[MRK.12.36]] stammen.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ὑποκάτω, 032 ὑποπόδιον (04 ist hier nicht erhalten)."],
  ["Abschriiber händ Zitat oft a de bekannt Wortlut vo de Septuaginta aaglichen; ὑποκάτω cha us [[MRK.12.36]] stamme.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ὑποκάτω, 032 ὑποπόδιον."]),
 ("VAR-SBLGNTAPP-MAT-023-003-02:R2", "MAT.23.3", "was sie euch sagen, das tut und haltet", "was sie euch zu halten sagen, das haltet und tut",
  "was si eu säged, das mached und halted", "was si eu säged z halte, das halted und mached", "gering",
  "Mit τηρεῖν («zu halten») bezieht sich die Aufforderung ausdrücklich auf das, was sie zu halten gebieten.",
  "Mit τηρεῖν («z halte») bezieht sich d Ufforderig usdrücklich uf das, wo si z halte gebiited.",
  {"R1": [("ποιήσατε καὶ τηρεῖτε", "tut und haltet", "WH, Treg, NA28")], "R2": [("τηρεῖν τηρεῖτε καὶ ποιεῖτε", "zu halten, das haltet und tut", "RP")]},
  {"R1": [("ποιήσατε καὶ τηρεῖτε", "mached und halted", "WH, Treg, NA28")], "R2": [("τηρεῖν τηρεῖτε καὶ ποιεῖτε", "z halte, das halted und mached", "RP")]},
  ["Die längere Lesart kann die Aufforderung einschränken oder verdeutlichen; ebenso kann sie aus einer Verdoppelung beim Abschreiben entstanden sein.",
   "Laut der automatischen Zuordnung lesen 03 und 05 die Lesart des SBLGNT, 032 die längere. Die Erstschrift von 01 hat die Zuordnung keiner Lesart zugewiesen (ihr erfasster Wortlaut hat nur ποιήσατε); eine Korrektur in 01 liest wie der SBLGNT."],
  ["Di länger Läsart cha d Ufforderig iischränke oder verdüütliche; oder si isch us ere Verdopplig bim Abschriibe entstande.",
   "Nach de automatische Zueornig läsed 03 und 05 wie de SBLGNT, 032 di länger Läsart. D Erschtschrift vo 01 isch keiner Läsart zueteilt; e Korrektur in 01 list wie de SBLGNT."]),
 ("VAR-SBLGNTAPP-MAT-023-004-02:R2", "MAT.23.4", "schwere Lasten", "schwere und schwer zu tragende Lasten",
  "schwääri Laschte", "schwääri und schwär z träägendi Laschte", "gering",
  "Der Zusatz verstärkt das Bild der Last.", "De Zuesatz verstärkt s Bild vo de Lascht.",
  {"R1": [("βαρέα", "schwere", "WH, NIV")], "R2": [("βαρέα καὶ δυσβάστακτα", "schwere und schwer zu tragende", "Treg, RP, NA28")]},
  {"R1": [("βαρέα", "schwääri", "WH, NIV")], "R2": [("βαρέα καὶ δυσβάστακτα", "schwääri und schwär z träägendi", "Treg, RP, NA28")]},
  ["Der Zusatz kann aus [[LUK.11.46]] (φορτία δυσβάστακτα) übernommen sein; ebenso kann er beim Abschreiben wegen des ähnlichen Ausgangs ausgefallen sein. Der SBLGNT folgt hier WH gegen Treg, NA28 und RP.",
   "Laut der automatischen Zuordnung liest 01 ohne Zusatz, 03, 032 und 05 mit ihm (04 ist hier nicht erhalten)."],
  ["De Zuesatz cha us [[LUK.11.46]] übernoo sii; oder er isch bim Abschriibe usgfalle. De SBLGNT folgt da WH gäge Treg, NA28 und RP.",
   "Nach de automatische Zueornig list 01 ohni Zuesatz, 03, 032 und 05 mit."]),
 ("VAR-SBLGNTAPP-MAT-023-005-02:R2", "MAT.23.5", "die Quasten lang", "die Quasten an ihren Gewändern lang",
  "d Quaste lang", "d Quaste a irne Gwänder lang", "gering",
  "Der Zusatz sagt, woran die Quasten sind.", "De Zuesatz seit, wo d Quaste dra sind.",
  {"R1": [("κράσπεδα", "die Quasten", "WH, Treg, NA28")], "R2": [("κράσπεδα τῶν ἱματίων αὐτῶν", "die Quasten ihrer Gewänder", "NIV, RP")]},
  {"R1": [("κράσπεδα", "d Quaste", "WH, Treg, NA28")], "R2": [("κράσπεδα τῶν ἱματίων αὐτῶν", "d Quaste a irne Gwänder", "NIV, RP")]},
  ["Erklärende Ergänzung (vgl. [[MAT.9.20]], [[MAT.14.36]]) liegt nahe; ebenso kann der Zusatz als selbstverständlich weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne Zusatz, 032 mit ihm."],
  ["E erklärendi Ergänzig liit nöch; oder de Zuesatz isch als sälbverständlich wäggfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni Zuesatz, 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-023-008-01:R2", "MAT.23.8", "denn einer ist euer Lehrer", "denn einer ist euer Lehrmeister, der Christus",
  "dänn eine isch eue Lehrer", "dänn eine isch eue Lehrmeischter, de Christus", "mittel",
  "Der Lehrer wird schon hier als der Christus benannt und mit dem Wort aus [[MAT.23.10]] bezeichnet.",
  "De Lehrer wird scho da als de Christus gnännt, mit em Wort us [[MAT.23.10]].",
  {"R1": [("διδάσκαλος", "Lehrer", "WH, Treg, NA28")], "R2": [("καθηγητής ὁ χριστός", "Lehrmeister, der Christus", "RP")]},
  {"R1": [("διδάσκαλος", "Lehrer", "WH, Treg, NA28")], "R2": [("καθηγητής ὁ χριστός", "Lehrmeischter, de Christus", "RP")]},
  ["Angleichung an [[MAT.23.10]] liegt nahe; ebenso kann διδάσκαλος eingesetzt worden sein, um den Bezug auf «Rabbi» (Lehrer) zu verdeutlichen.",
   "Laut der automatischen Zuordnung liest 03 διδάσκαλος (04 ist hier nicht erhalten). 01, 032 und 05 hat die Zuordnung einer anderen Lesart zugewiesen; ihr erfasster Wortlaut hat καθηγητής ohne ὁ χριστός."],
  ["Aagliichig a [[MAT.23.10]] liit nöch; oder διδάσκαλος isch iigsetzt worde, damit de Bezug uf «Rabbi» klar isch.",
   "Nach de automatische Zueornig list 03 διδάσκαλος. 01, 032 und 05 sind ere andere Läsart zueteilt; ire erfasst Wortlut hät καθηγητής ohni ὁ χριστός."]),
 ("VAR-SBLGNTAPP-MAT-023-009-02:R2", "MAT.23.9", "euer Vater, der himmlische", "euer Vater, der in den Himmeln",
  "eue Vatter, de himmlisch", "eue Vatter, wo i de Himel isch", "gering",
  "Statt des Adjektivs steht die Wendung «in den Himmeln»; der Sinn bleibt gleich.",
  "Statt em Adjektiv staat «i de Himel»; de Sinn bliibt gliich.",
  {"R1": [("οὐράνιος", "der himmlische", "WH, Treg, NA28")], "R2": [("ἐν τοῖς οὐρανοῖς", "der in den Himmeln", "RP")]},
  {"R1": [("οὐράνιος", "de himmlisch", "WH, Treg, NA28")], "R2": [("ἐν τοῖς οὐρανοῖς", "wo i de Himel isch", "RP")]},
  ["Matthäus braucht beide Wendungen ([[MAT.6.9]], [[MAT.6.14]]); die eine kann an die häufigere angeglichen worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 05 οὐράνιος (04 ist hier nicht erhalten)."],
  ["De Matthäus bruucht beidi Wändige ([[MAT.6.9]], [[MAT.6.14]]); di eint cha a di hüüfiger aaglichen worde sii.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 05 οὐράνιος."]),
 ("VAR-SBLGNTAPP-MAT-023-012-01:R2", "MAT.23.12", "wird erhöht werden.", "wird erhöht werden. " + V14_DE,
  "wird erhöcht.", "wird erhöcht. " + V14_GSW, "mittel",
  "RP hat nach [[MAT.23.12]] einen zusätzlichen Weheruf (dort als Vers 13 gezählt; der SBLGNT-Vers 13 wird dort zu Vers 14). In der verbreiteten Zählung ist es [[MAT.23.14]].",
  "RP hät nach [[MAT.23.12]] en zuesätzliche Weheruef (dört Vers 13; de SBLGNT-Vers 13 wird dört zu Vers 14). I de verbreitete Zellig isch das [[MAT.23.14]].",
  {"R1": [("ὑψωθήσεται", "wird erhöht werden.", "WH, Treg, NA28")],
   "R2": [("ὑψωθήσεται. Οὐαὶ δέ ὑμῖν, γραμματεῖς καὶ Φαρισαῖοι, ὑποκριταί, ὅτι κατεσθίετε τὰς οἰκίας τῶν χηρῶν, καὶ προφάσει μακρὰ προσευχόμενοι· διὰ τοῦτο λήψεσθε περισσότερον κρίμα", "wird erhöht werden. " + V14_DE, "RP")]},
  {"R1": [("ὑψωθήσεται", "wird erhöcht.", "WH, Treg, NA28")],
   "R2": [("ὑψωθήσεται. Οὐαὶ δέ ὑμῖν, γραμματεῖς καὶ Φαρισαῖοι, ὑποκριταί, ὅτι κατεσθίετε τὰς οἰκίας τῶν χηρῶν, καὶ προφάσει μακρὰ προσευχόμενοι· διὰ τοῦτο λήψεσθε περισσότερον κρίμα", "wird erhöcht. " + V14_GSW, "RP")]},
  [V14_ORIGIN_DE, V14_COLL_DE], [V14_ORIGIN_GSW, V14_COLL_GSW]),
 ("VAR-SBLGNTAPP-MAT-023-013-02:R2", "MAT.23.13", "lasst ihr nicht hineingehen.", "lasst ihr nicht hineingehen. [[MAT.23.14]] " + V14_DE,
  "lönd ir nöd inegaa.", "lönd ir nöd inegaa. [[MAT.23.14]] " + V14_GSW, "mittel",
  "Der Textus Receptus hat denselben Weheruf nach [[MAT.23.13]] als Vers 14.",
  "De Textus Receptus hät dä gliich Weheruef nach [[MAT.23.13]] als Vers 14.",
  {"R1": [("εἰσελθεῖν", "hineingehen.", "WH, Treg, NA28, RP")],
   "R2": [("εἰσελθεῖν. Οὐαὶ ὑμῖν, γραμματεῖς καὶ Φαρισαῖοι ὑποκριταί, ὅτι κατεσθίετε τὰς οἰκίας τῶν χηρῶν καὶ προφάσει μακρὰ προσευχόμενοι· διὰ τοῦτο λήψεσθε περισσότερον κρίμα", "hineingehen. " + V14_DE, "TR")]},
  {"R1": [("εἰσελθεῖν", "inegaa.", "WH, Treg, NA28, RP")],
   "R2": [("εἰσελθεῖν. Οὐαὶ ὑμῖν, γραμματεῖς καὶ Φαρισαῖοι ὑποκριταί, ὅτι κατεσθίετε τὰς οἰκίας τῶν χηρῶν καὶ προφάσει μακρὰ προσευχόμενοι· διὰ τοῦτο λήψεσθε περισσότερον κρίμα", "inegaa. " + V14_GSW, "TR")]},
  [V14_ORIGIN_DE, V14_COLL_DE], [V14_ORIGIN_GSW, V14_COLL_GSW]),
 ("VAR-SBLGNTAPP-MAT-023-019-01:R2", "MAT.23.19", "Ihr Blinden!", "Ihr Narren und Blinden!",
  "Ir Blinde!", "Ir Narre und Blinde!", "gering",
  "Die Anrede lautet wie in [[MAT.23.17]].", "D Aared luutet wie i [[MAT.23.17]].",
  {"R1": [("τυφλοί", "Ihr Blinden", "WH, Treg, NA28")], "R2": [("Μωροὶ καὶ τυφλοί", "Ihr Narren und Blinden", "RP")]},
  {"R1": [("τυφλοί", "Ir Blinde", "WH, Treg, NA28")], "R2": [("Μωροὶ καὶ τυφλοί", "Ir Narre und Blinde", "RP")]},
  ["Angleichung an [[MAT.23.17]] liegt nahe; ebenso kann μωροὶ καί beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 05 τυφλοί, 03, 032 und 04 Μωροὶ καὶ τυφλοί."],
  ["Aagliichig a [[MAT.23.17]] liit nöch; oder μωροὶ καί isch bim Abschriibe usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 05 τυφλοί, 03, 032 und 04 Μωροὶ καὶ τυφλοί."]),
 ("VAR-SBLGNTAPP-MAT-023-025-01:R2", "MAT.23.25", "Raub und Masslosigkeit", "Raub und Ungerechtigkeit",
  "Raub und Masslosigkeit", "Raub und Ungrächtigkeit", "gering",
  "Statt des Mangels an Selbstbeherrschung ist Unrecht genannt.", "Statt em Mangel a Sälbschtbeherrschig isch Unrächt gnännt.",
  {"R1": [("ἀκρασίας", "Masslosigkeit", "WH, Treg, NA28")], "R2": [("ἀδικίας", "Ungerechtigkeit", "RP")]},
  {"R1": [("ἀκρασίας", "Masslosigkeit", "WH, Treg, NA28")], "R2": [("ἀδικίας", "Ungrächtigkeit", "RP")]},
  ["Das seltenere ἀκρασία kann durch das geläufigere ἀδικία ersetzt worden sein, das auch besser zu «Raub» passt; ebenso ist eine Verwechslung ähnlicher Wörter denkbar.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 05 ἀκρασίας, 04 ἀδικίας."],
  ["S sältener ἀκρασία cha dur s gläufiger ἀδικία ersetzt worde sii; oder ähnlichi Wort sind verwächslet worde.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 05 ἀκρασίας, 04 ἀδικίας."]),
 ("VAR-SBLGNTAPP-MAT-023-026-01:R2", "MAT.23.26", "des Bechers und der Schüssel", "des Bechers",
  "vom Becher und vo de Schüssle", "vom Becher", "gering",
  "Ohne die Worte ist nur vom Becher die Rede.", "Ohni d Wort isch nu vom Becher d Red.",
  {"R1": [("καὶ τῆς παροψίδος", "und der Schüssel", "WH, Treg, NIV, RP")], "R2": [("–", "(fehlt)", "WHmarg, NA28")]},
  {"R1": [("καὶ τῆς παροψίδος", "und vo de Schüssle", "WH, Treg, NIV, RP")], "R2": [("–", "(fehlt)", "WHmarg, NA28")]},
  ["Die Worte können aus [[MAT.23.25]] ergänzt worden sein; ebenso können sie beim Abschreiben ausgefallen sein. Der SBLGNT folgt WH, Treg und RP gegen NA28.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 04 καὶ τῆς παροψίδος, 05 ohne die Worte."],
  ["D Wort chönd us [[MAT.23.25]] ergänzt worde sii; oder si sind bim Abschriibe usgfalle. De SBLGNT folgt WH, Treg und RP gäge NA28.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 04 καὶ τῆς παροψίδος, 05 ohni."]),
 ("VAR-SBLGNTAPP-MAT-023-038-01:R2", "MAT.23.38", "euer Haus wird euch verödet überlassen", "euer Haus wird euch überlassen",
  "eues Huus wird eu läär und öd überlaa", "eues Huus wird eu überlaa", "mittel",
  "Ohne ἔρημος heisst der Satz: «euer Haus wird euch überlassen», also aufgegeben, ihnen allein gelassen.",
  "Ohni ἔρημος heisst de Satz: «eues Huus wird eu überlaa», also ufgää, eu elei überlaa.",
  {"R1": [("ἔρημος", "verödet", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  {"R1": [("ἔρημος", "läär und öd", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  ["ἔρημος kann aus [[JER.22.5]] oder zur Verdeutlichung ergänzt worden sein; ebenso kann es weggefallen sein (vgl. [[LUK.13.35]], wo das Wort in den Ausgaben fehlt).",
   "Laut der automatischen Zuordnung lesen 01, 032, 04 und 05 ἔρημος, 03 ohne das Wort."],
  ["ἔρημος cha us [[JER.22.5]] oder zur Verdüütlichung ergänzt worde sii; oder s Wort isch wäggfalle (vgl. [[LUK.13.35]]).",
   "Nach de automatische Zueornig läsed 01, 032, 04 und 05 ἔρημος, 03 ohni."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-022-001-046", "MAT.22.1-MAT.22.46", "section", "Das Gleichnis vom Hochzeitsmahl und vier Streitfragen",
  ["TU-MAT-022-001-014", "TU-MAT-022-015-022", "TU-MAT-022-023-033", "TU-MAT-022-034-040", "TU-MAT-022-041-046"],
  "Jesus erzählt das Gleichnis von einem König, dessen Geladene nicht zum Hochzeitsfest seines Sohnes kommen wollen; einige von ihnen misshandeln und töten seine Knechte. Der König lässt die Mörder umbringen und ihre Stadt anzünden, lässt Böse und Gute von den Strassen holen und befiehlt, einen Gast ohne Hochzeitskleid hinauszuwerfen. Danach schicken die Pharisäer ihre Jünger mit den Herodianern, die Jesus mit der Frage nach der Steuer für den Kaiser in eine Falle locken wollen; er antwortet, man solle dem Kaiser geben, was des Kaisers ist, und Gott, was Gottes ist. Sadduzäer fragen, wessen Frau in der Auferstehung eine Frau sein wird, die nacheinander sieben Brüder geheiratet hat; Jesus wirft ihnen vor, weder die Schriften noch die Kraft Gottes zu kennen. Ein Gesetzeslehrer fragt nach dem grössten Gebot; Jesus nennt die Liebe zu Gott und die Liebe zum Nächsten. Zuletzt fragt Jesus die Pharisäer, wie der Christus Davids Sohn sein kann, wenn David ihn Herr nennt; niemand kann antworten, und keiner wagt mehr, ihn zu fragen.", SEG),
 ("TU-MAT-022-001-014", "MAT.22.1-MAT.22.14", "parable", "Das Gleichnis vom königlichen Hochzeitsfest", None,
  "Jesus sagt, das Reich der Himmel sei einem König gleich geworden, der für seinen Sohn ein Hochzeitsfest ausrichtet. Die Geladenen wollen nicht kommen; auf eine zweite Einladung hin gehen die einen auf ihren Acker oder zu ihrem Geschäft, die übrigen misshandeln und töten die Knechte. Der König schickt seine Truppen, bringt die Mörder um und zündet ihre Stadt an. Die Knechte holen auf seinen Befehl alle von den Strassen, Böse und Gute, und das Fest füllt sich mit Gästen. Über einen Gast ohne Hochzeitskleid, der auf die Frage des Königs verstummt, befiehlt der König, ihn gebunden in die Finsternis hinauszuwerfen. Das Gleichnis schliesst: Viele sind eingeladen, wenige aber auserwählt.", SEG),
 ("TU-MAT-022-015-022", "MAT.22.15-MAT.22.22", "dialogue", "Die Frage nach der Steuer für den Kaiser", None,
  "Die Pharisäer beraten, wie sie Jesus mit einer Aussage in eine Falle locken können, und schicken ihre Jünger mit den Herodianern zu ihm. Diese nennen ihn wahrhaftig und unparteiisch und fragen, ob es erlaubt sei, dem Kaiser Steuer zu zahlen. Jesus erkennt ihre Bosheit, nennt sie Heuchler und lässt sich die Steuermünze zeigen, einen Denar. Auf seine Frage, wessen Bild und Aufschrift das sei, antworten sie: «Des Kaisers.» Er sagt: «Gebt also, was des Kaisers ist, dem Kaiser, und was Gottes ist, Gott!» Sie staunen, lassen ihn stehen und gehen weg.", SEG),
 ("TU-MAT-022-023-033", "MAT.22.23-MAT.22.33", "dialogue", "Die Sadduzäer und die Auferstehung", None,
  "Am selben Tag kommen Sadduzäer, die sagen, es gebe keine Auferstehung. Sie führen das Gebot des Mose an, dass der Bruder eines kinderlos Verstorbenen dessen Frau heiraten soll, und erzählen von sieben Brüdern, die nacheinander dieselbe Frau geheiratet haben und gestorben sind: Wessen Frau wird sie in der Auferstehung sein? Jesus antwortet, sie irrten, weil sie weder die Schriften noch die Kraft Gottes kennen; in der Auferstehung heiraten sie nicht, sondern sind wie Engel Gottes im Himmel. Zur Auferstehung der Toten verweist er auf Gottes Wort: «Ich bin der Gott Abrahams und der Gott Isaaks und der Gott Jakobs» ([[EXO.3.6]]); er sei nicht der Gott von Toten, sondern von Lebenden. Die Menschenmengen sind überwältigt von seiner Lehre.", SEG),
 ("TU-MAT-022-034-040", "MAT.22.34-MAT.22.40", "dialogue", "Das grösste Gebot", None,
  "Als die Pharisäer hören, dass Jesus die Sadduzäer zum Schweigen gebracht hat, versammeln sie sich. Einer von ihnen, ein Gesetzeslehrer, fragt ihn, um ihn auf die Probe zu stellen, welches Gebot das grösste im Gesetz sei. Jesus antwortet mit dem Gebot aus [[DEU.6.5]]: Du sollst den Herrn, deinen Gott, lieben mit deinem ganzen Herzen, deiner ganzen Seele und deinem ganzen Denken; das sei das grösste und erste Gebot. Das zweite sei ihm gleich: Du sollst deinen Nächsten lieben wie dich selbst ([[LEV.19.18]]). An diesen zwei Geboten hängen das ganze Gesetz und die Propheten.", SEG),
 ("TU-MAT-022-041-046", "MAT.22.41-MAT.22.46", "dialogue", "Wessen Sohn ist der Christus?", None,
  "Jesus fragt die versammelten Pharisäer, was sie über den Christus meinen: Wessen Sohn ist er? Sie antworten: «Davids.» Er fragt zurück, wie David ihn dann im Geist «Herr» nennt, wenn er sagt: «Der Herr sprach zu meinem Herrn: Setze dich zu meiner Rechten, bis ich deine Feinde unter deine Füsse lege» ([[PSA.110.1]]). Wenn David ihn Herr nennt, wie ist er dann sein Sohn? Niemand kann ihm antworten, und von jenem Tag an wagt keiner mehr, ihn zu fragen.", SEG),
 ("TU-MAT-023-001-039", "MAT.23.1-MAT.23.39", "section", "Die Rede gegen die Schriftgelehrten und Pharisäer und die Klage über Jerusalem",
  ["TU-MAT-023-001-012", "TU-MAT-023-013-022", "TU-MAT-023-023-028", "TU-MAT-023-029-036", "TU-MAT-023-037-039"],
  "Jesus spricht zu den Menschenmengen und seinen Jüngern: Die Schriftgelehrten und Pharisäer sitzen auf dem Stuhl des Mose; was sie sagen, sollen sie tun und halten, nach ihren Werken aber nicht handeln, denn sie reden und tun es nicht. Er wirft ihnen vor, anderen schwere Lasten aufzulegen und ihre Werke zu tun, um gesehen zu werden; seine Hörer sollen sich nicht Rabbi oder Lehrmeister nennen lassen und keinen auf der Erde ihren Vater nennen, und der Grösste unter ihnen soll ihr Diener sein. In sieben Weherufen nennt er die Schriftgelehrten und Pharisäer Heuchler und blinde Führer: Sie verschliessen das Reich der Himmel, machen ihren Proselyten zu einem Sohn der Hölle, lehren, manche Schwüre gälten nichts, geben den Zehnten von Gewürzen und lassen Recht, Barmherzigkeit und Treue beiseite, reinigen das Äussere von Becher und Schüssel, gleichen getünchten Gräbern und bauen die Gräber der Propheten, womit sie bezeugen, dass sie Söhne der Prophetenmörder sind. Er kündigt an, dass alles gerechte Blut von Abel bis Secharja über dieses Geschlecht kommen wird, und klagt über Jerusalem, das die Propheten tötet: Ihr Haus werde ihnen verödet überlassen, und sie würden ihn nicht mehr sehen, bis sie sagen: «Gesegnet sei, der kommt im Namen des Herrn!» Der Vers [[MAT.23.14]] der verbreiteten Zählung fehlt im zugrunde gelegten Text.", SEG),
 ("TU-MAT-023-001-012", "MAT.23.1-MAT.23.12", "discourse", "Nicht nach ihren Werken handeln", None,
  "Jesus sagt zu den Menschenmengen und seinen Jüngern: Die Schriftgelehrten und Pharisäer haben sich auf den Stuhl des Mose gesetzt; alles, was sie sagen, sollen die Hörer tun und halten, nach ihren Werken aber nicht handeln, denn sie reden und tun es nicht. Sie legen den Menschen schwere Lasten auf, wollen sie selbst aber nicht mit dem Finger bewegen; sie tun ihre Werke, um gesehen zu werden, machen ihre Gebetsriemen breit und die Quasten lang und lieben Ehrenplätze, Begrüssungen und die Anrede Rabbi. Die Hörer aber sollen sich nicht Rabbi nennen lassen, denn einer ist ihr Lehrer, und sie alle sind Brüder; keinen auf der Erde sollen sie ihren Vater nennen, denn einer ist ihr Vater, der himmlische; auch nicht Lehrmeister, denn ihr Lehrmeister ist einer, der Christus. Der Grösste unter ihnen soll ihr Diener sein: Wer sich selbst erhöht, wird erniedrigt werden, und wer sich selbst erniedrigt, wird erhöht werden.", SEG),
 ("TU-MAT-023-013-022", "MAT.23.13-MAT.23.22", "discourse", "Weherufe: das verschlossene Reich, die Proselyten und die Schwüre", None,
  "Jesus ruft Wehe über die Schriftgelehrten und Pharisäer, die er Heuchler nennt: Sie verschliessen das Reich der Himmel vor den Menschen, gehen selbst nicht hinein und lassen die nicht hinein, die hineinwollen. Sie ziehen über Meer und Land, um einen einzigen Proselyten zu gewinnen, und machen ihn zu einem Sohn der Hölle, doppelt so schlimm wie sie. Als blinde Führer sagen sie, ein Schwur beim Tempel oder beim Altar gelte nichts, wer aber beim Gold des Tempels oder bei der Gabe auf dem Altar schwöre, sei gebunden. Jesus fragt, was grösser sei, das Gold oder der Tempel, der es geheiligt hat, die Gabe oder der Altar, der sie heiligt: Wer beim Altar schwört, schwört auch bei allem, was darauf liegt; wer beim Tempel schwört, auch bei dem, der ihn bewohnt; wer beim Himmel schwört, beim Thron Gottes und bei dem, der darauf sitzt. Der Vers [[MAT.23.14]] der verbreiteten Zählung fehlt im zugrunde gelegten Text.", SEG),
 ("TU-MAT-023-023-028", "MAT.23.23-MAT.23.28", "discourse", "Weherufe: der Zehnte, Becher und Schüssel, die getünchten Gräber", None,
  "Jesus ruft weiter Wehe über die Schriftgelehrten und Pharisäer: Sie geben den Zehnten von Minze, Dill und Kümmel und haben das Gewichtigere des Gesetzes beiseitegelassen, das Recht, die Barmherzigkeit und die Treue; dies hätte man tun und jenes nicht beiseitelassen sollen. Als blinde Führer sieben sie die Mücke aus und verschlucken das Kamel. Sie reinigen das Äussere von Becher und Schüssel, innen aber sind diese voll von Raub und Masslosigkeit; den blinden Pharisäer fordert Jesus auf, zuerst das Innere zu reinigen, damit auch das Äussere rein wird. Sie gleichen weiss getünchten Gräbern, die aussen schön aussehen, innen aber voll Totengebeine und Unreinheit sind: Aussen erscheinen sie den Menschen gerecht, innen sind sie voll Heuchelei und Gesetzlosigkeit.", SEG),
 ("TU-MAT-023-029-036", "MAT.23.29-MAT.23.36", "discourse", "Der letzte Weheruf: die Gräber der Propheten und das kommende Gericht", None,
  "Jesus ruft Wehe über die Schriftgelehrten und Pharisäer, weil sie die Gräber der Propheten bauen, die Grabmäler der Gerechten schmücken und sagen, in den Tagen ihrer Väter hätten sie sich nicht am Blut der Propheten beteiligt. Damit bezeugen sie, sagt Jesus, dass sie Söhne derer sind, die die Propheten ermordet haben; sie sollen das Mass ihrer Väter vollmachen. Er nennt sie Schlangen und Vipernbrut und fragt, wie sie dem Gericht der Hölle entkommen wollen. Er sendet zu ihnen Propheten, Weise und Schriftgelehrte; einige werden sie töten und kreuzigen, andere in ihren Synagogen auspeitschen und von Stadt zu Stadt verfolgen, damit alles gerechte Blut von Abel bis Secharja, dem Sohn Berechjas, über sie kommt. Amen, das alles wird über dieses Geschlecht kommen.", SEG),
 ("TU-MAT-023-037-039", "MAT.23.37-MAT.23.39", "discourse", "Klage über Jerusalem", None,
  "Jesus klagt über Jerusalem, das die Propheten tötet und die steinigt, die zu ihr gesandt sind: Wie oft hat er ihre Kinder sammeln wollen, wie eine Henne ihre Küken unter die Flügel sammelt, und sie haben nicht gewollt. Ihr Haus wird ihnen verödet überlassen; sie werden ihn von jetzt an nicht mehr sehen, bis sie sagen: «Gesegnet sei, der kommt im Namen des Herrn!» ([[PSA.118.26]]).", SEG),
]
UNITS_GSW = {
 "TU-MAT-022-001-046": ("S Gliichnis vom Hochziitfäscht und vier Striitfroge",
  "De Jesus verzellt s Gliichnis vo me König, wo sini Iigladne nöd as Hochziitfäscht vo sim Sohn wänd choo; es paar vo ine misshandled sini Chnächt und bringed si um. De König laat d Mörder umbringe und iri Stadt aazünde, laat Bösi und Gueti vo de Strasse hole und befiehlt, en Gascht ohni Hochziitgwand usezrüere. Dänn schicked d Pharisäer iri Jünger mit de Herodianer, wo de Jesus mit de Frag nach de Stüür für de Kaiser i d Falle wänd locke; er antwortet, mer söll em Kaiser gää, was em Kaiser ghört, und Gott, was Gott ghört. Sadduzäer fröged, wäm sini Frau i de Uferstehig e Frau sig, wo nachenand vo sibe Brüedere ghürate worde isch; de Jesus wirft ine vor, si kännid weder d Schrifte no d Chraft vo Gott. En Gsetzeslehrer fröget nach em gröschte Gebot; de Jesus nännt d Liebi zu Gott und d Liebi zum Nächschte. Zletscht fröget de Jesus d Pharisäer, wie de Christus de Sohn vom David chönn sii, wänn en de David Herr nännt; niemer cha antworte, und keine traut sich meh, en z fröge."),
 "TU-MAT-022-001-014": ("S Gliichnis vom königliche Hochziitfäscht",
  "De Jesus seit, s Riich vo de Himel sig eme König gliich worde, wo für sin Sohn es Hochziitfäscht macht. D Iigladne wänd nöd choo; uf e zweiti Iiladig gönd di eint uf iren Acher oder zu irem Gschäft, di andere misshandled d Chnächt und bringed si um. De König schickt sini Truppe, bringt d Mörder um und zündt iri Stadt aa. D Chnächt holed uf sin Befähl alli vo de Strasse, Bösi und Gueti, und s Fäscht wird voll Gäscht. Bi me Gascht ohni Hochziitgwand, wo uf d Frag vom König verstummt, befiehlt de König, en bunde i d Fiischteri usezrüere. S Gliichnis schlüsst: Vili sind iiglade, aber wenig userwählt."),
 "TU-MAT-022-015-022": ("D Frag nach de Stüür für de Kaiser",
  "D Pharisäer beraated, wie si de Jesus mit ere Ussag i d Falle chönd locke, und schicked iri Jünger mit de Herodianer zu ihm. Die nänned en ufrichtig und unparteiisch und fröged, öb s erlaubt sig, em Kaiser Stüür z zale. De Jesus merkt iri Bosheit, nännt si Hüüchler und laat sich d Stüürmünz zeige, en Denar. Uf sini Frag, wäm sis Bild und Ufschrift das sig, antworted si: «Vom Kaiser.» Er seit: «Gänd also, was em Kaiser ghört, em Kaiser, und was Gott ghört, Gott!» Si stuuned, lönd en staa und gönd wäg."),
 "TU-MAT-022-023-033": ("D Sadduzäer und d Uferstehig",
  "Am gliiche Tag chömed Sadduzäer, wo säged, es geb kei Uferstehig. Si zitiered s Gebot vom Mose, dass de Brüeder vo eim, wo ohni Chind stirbt, sini Frau söll hürate, und verzelled vo sibe Brüedere, wo nachenand di gliich Frau ghürate händ und gstorbe sind: Wäm sini Frau wird si i de Uferstehig sii? De Jesus antwortet, si irred, wil si weder d Schrifte no d Chraft vo Gott kännid; i de Uferstehig hürated si nöd, sondern sind wie Ängel vo Gott im Himel. Zur Uferstehig vo de Tote verwiist er uf s Wort vo Gott: «Ich bi de Gott vom Abraham und de Gott vom Isaak und de Gott vom Jakob» ([[EXO.3.6]]); er sig nöd de Gott vo Tote, sondern vo Läbige. D Lüüt sind vo sinere Lehr überwältiget."),
 "TU-MAT-022-034-040": ("S gröscht Gebot",
  "Wo d Pharisäer ghöred, dass de Jesus d Sadduzäer zum Schwiige brocht hät, versammled si sich. Eine vo ine, en Gsetzeslehrer, fröget en, für en uf d Prob z stelle, weles Gebot s gröscht im Gsetz sig. De Jesus antwortet mit em Gebot us [[DEU.6.5]]: Du söllsch de Herr, din Gott, liebe mit dim ganze Härz, dinere ganze Seel und dim ganze Dänke; das sig s gröscht und erscht Gebot. S zweit sig ihm gliich: Du söllsch din Nächschte liebe wie di sälber ([[LEV.19.18]]). A dene zwei Gebot hanged s ganz Gsetz und d Prophete."),
 "TU-MAT-022-041-046": ("Wäm sin Sohn isch de Christus?",
  "De Jesus fröget di versammlete Pharisäer, was si über de Christus meined: Wäm sin Sohn isch er? Si antworted: «Vom David.» Er fröget zrugg, wie de David en dänn im Geischt «Herr» nännt, wänn er seit: «De Herr hät zu mim Herr gseit: Sitz rächts vo mir, bis ich dini Find under dini Füess lege» ([[PSA.110.1]]). Wänn de David en Herr nännt, wie isch er dänn sin Sohn? Niemer cha ihm antworte, und vo säbem Tag aa traut sich keine meh, en z fröge."),
 "TU-MAT-023-001-039": ("D Red gäge d Schriftgelehrte und Pharisäer und d Klag über Jerusalem",
  "De Jesus redt zu de Lüüt und zu sine Jünger: D Schriftgelehrte und Pharisäer sitzed uf em Stuel vom Mose; was si säged, söled si mache und halte, aber sich nöd nach irne Wärch richte, dänn si reded und tüend s nöd. Er wirft ine vor, dass si andere schwääri Laschte ufleged und iri Wärch tüend, damit me si gseht; sini Zuehörer söled sich nöd Rabbi oder Lehrmeischter nänne laa und keine uf de Ärde ire Vatter nänne, und de Gröscht under ine söll ire Diener sii. I sibe Weherüef nännt er d Schriftgelehrte und Pharisäer Hüüchler und blindi Füerer: Si schlüssed s Riich vo de Himel zue, mached ire Proselyt zumene Sohn vo de Höll, lehred, mängi Schwüer gältid nüüt, gänd de Zäänte vo Gwürz und stelled Rächt, Barmherzigkeit und Treui uf d Siite, mached s Üsser vo Becher und Schüssle suuber, sind wie wiissgstricheni Greber und bued d Greber vo de Prophete; damit bezüüged si, dass si Söhn vo dene sind, wo d Prophete umbrocht händ. Er seit aa, dass alles grächte Bluet vom Abel bis zum Secharja über die Generation chunnt, und klagt über Jerusalem, wo d Prophete umbringt: Ires Huus wärdi ine läär und öd überlaa, und si wärdid en nümme gseh, bis si säged: «Gsägnet sig dä, wo chunnt im Name vom Herr!» De Vers [[MAT.23.14]] vo de verbreitete Zellig fehlt im Grundtext."),
 "TU-MAT-023-001-012": ("Nöd nach irne Wärch handle",
  "De Jesus seit zu de Lüüt und zu sine Jünger: D Schriftgelehrte und Pharisäer händ sich uf de Stuel vom Mose gsetzt; alles, was si säged, söled d Zuehörer mache und halte, aber sich nöd nach irne Wärch richte, dänn si reded und tüend s nöd. Si leged de Mänsche schwääri Laschte uf, wänd si aber sälber nöd mit em Finger bewege; si tüend iri Wärch, damit d Mänsche si gsehnd, mached iri Gebetsrieme breit und d Quaste lang und händ gärn Ehreplätz, Grüess und d Aared Rabbi. D Zuehörer aber söled sich nöd Rabbi nänne laa, dänn eine isch ire Lehrer, und si alli sind Brüedere; keine uf de Ärde söled si ire Vatter nänne, dänn eine isch ire Vatter, de himmlisch; au nöd Lehrmeischter, dänn ire Lehrmeischter isch eine, de Christus. De Gröscht under ine söll ire Diener sii: Wer sich sälber erhöcht, wird erniedriget, und wer sich sälber erniedriget, wird erhöcht."),
 "TU-MAT-023-013-022": ("Weherüef: s verschlosse Riich, d Proselyte und d Schwüer",
  "De Jesus rüeft Weh über d Schriftgelehrte und Pharisäer, wo n er Hüüchler nännt: Si schlüssed s Riich vo de Himel vor de Mänsche zue, gönd sälber nöd ine und lönd die nöd ine, wo inewänd. Si zieched übers Meer und übers Land, für en einzige Proselyt z gwünne, und mached en zumene Sohn vo de Höll, doppelt so schlimm wie si. Als blindi Füerer säged si, en Schwur bim Tämpel oder bim Altar gälti nüüt, wer aber bim Gold vom Tämpel oder bi de Gab uf em Altar schwöri, sig draa bunde. De Jesus fröget, was grösser sig, s Gold oder de Tämpel, wo s heilig gmacht hät, d Gab oder de Altar, wo si heilig macht: Wer bim Altar schwört, schwört au bi allem, wo druf liit; wer bim Tämpel schwört, au bi däm, wo drin wohnt; wer bim Himel schwört, bim Thron vo Gott und bi däm, wo druf sitzt. De Vers [[MAT.23.14]] vo de verbreitete Zellig fehlt im Grundtext."),
 "TU-MAT-023-023-028": ("Weherüef: de Zäänte, Becher und Schüssle, d wiissgstrichne Greber",
  "De Jesus rüeft wiiter Weh über d Schriftgelehrte und Pharisäer: Si gänd de Zäänte vo Minze, Dill und Chümi und händ s Gwichtiger vom Gsetz uf d Siite gstellt, s Rächt, d Barmherzigkeit und d Treui; das hett mer sölle tue und säbs nöd uf d Siite stelle. Als blindi Füerer siebed si d Mugge us und schlucked s Kamel abe. Si mached s Üsser vo Becher und Schüssle suuber, inne aber sind die voll vo Raub und Masslosigkeit; de blind Pharisäer fordert de Jesus uf, zerscht s Inner suuber z mache, damit au s Üsser suuber wird. Si sind wie wiissgstricheni Greber, wo usse schöön usgsehnd, inne aber voll Totechnoche und Unreinheit sind: Usse gsehnd si für d Mänsche grächt us, inne sind si voll Hüüchelei und Gsetzlosigkeit."),
 "TU-MAT-023-029-036": ("De letscht Weheruef: d Greber vo de Prophete und s chömend Gricht",
  "De Jesus rüeft Weh über d Schriftgelehrte und Pharisäer, wil si d Greber vo de Prophete bued, d Grabmäler vo de Grächte schmücked und säged, i de Täg vo irne Vätere hettid si sich nöd am Bluet vo de Prophete beteiligt. Damit bezüüged si, seit de Jesus, dass si Söhn vo dene sind, wo d Prophete umbrocht händ; si söled s Mass vo irne Vätere voll mache. Er nännt si Schlange und Viperebruet und fröget, wie si em Gricht vo de Höll wänd entchoo. Er schickt ine Prophete, Wiisi und Schriftgelehrti; es paar wärded si umbringe und chrüüzige, anderi i irne Synagoge uspeitsche und vo Stadt zu Stadt verfolge, damit alles grächte Bluet vom Abel bis zum Secharja, em Sohn vom Berechja, über si chunnt. Amen, das alles chunnt über die Generation."),
 "TU-MAT-023-037-039": ("Klag über Jerusalem",
  "De Jesus klagt über Jerusalem, wo d Prophete umbringt und die steiniget, wo zu ire gschickt worde sind: Wie mängisch hät er iri Chind wele sammle, wie e Huen iri Bibeli under d Flügel sammlet, und si händ nöd wele. Ires Huus wird ine läär und öd überlaa; si wärded en vo jetzt aa nümme gseh, bis si säged: «Gsägnet sig dä, wo chunnt im Name vom Herr!» ([[PSA.118.26]])."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1), nicht auf "
  "eigener Prüfung der Handschriften. Wo sie den Sigla des SBLGNT-Apparats widerspricht oder ihr erfasster Wortlaut der "
  "Zuordnung nicht entspricht (z. B. [[MAT.22.30]], [[MAT.23.12]]), ist das bei der Alternative vermerkt; es gilt der Apparat."),
 ("Begriffe: Die Übersetzung folgt den für das ganze Matthäusevangelium vereinbarten Wiedergaben: ἡ βασιλεία τῶν οὐρανῶν "
  "«das Reich der Himmel», ὁ πατὴρ ὁ οὐράνιος «der himmlische Vater», ἀμὴν λέγω ὑμῖν «Amen, ich sage euch», ἰδού «siehe», "
  "τότε «da/dann», γραμματεῖς «Schriftgelehrte», Φαρισαῖοι «Pharisäer», Σαδδουκαῖοι «Sadduzäer», ὑποκριταί «Heuchler», "
  "Χριστός «Christus» (in decisions: «Gesalbter/Messias»), ὄχλος «die Menge» und οἱ ὄχλοι «die Menschenmengen», "
  "προσέρχομαι «herantreten», γεννήματα ἐχιδνῶν «Vipernbrut», ὁ κλαυθμὸς καὶ ὁ βρυγμὸς τῶν ὀδόντων «das Weinen und das "
  "Zähneknirschen», δοῦλος «Knecht». Gleiche griechische Wendungen sind, wo es passt, wie in der "
  "Markus-Übersetzung wiedergegeben (Parallelen [[MRK.12.13-MRK.12.40]])."),
 ("In Kapitel 22–23 neu festgelegt und für die übrigen Matthäus-Bereiche vorgeschlagen: οὐαί «Wehe» (Mundart «Weh»); ὅτι "
  "nach dem Weheruf «denn»; γέεννα «Hölle» wie bei Markus (Alternative «Gehenna» in decisions); γενεά «Geschlecht» (Mundart "
  "«Generation», wie bei Markus); διάκονος «Diener» (neben δοῦλος «Knecht»); ὁδηγοὶ τυφλοί "
  "«blinde Führer»; δίκαιος «gerecht»; ἀνομία «Gesetzlosigkeit»; ὀμνύω «schwören»; ναός «Tempel»; νομικός "
  "«Gesetzeslehrer»; καθηγητής «Lehrmeister»; Gleichniseinleitung ὡμοιώθη «ist … gleich geworden»; κλητοί «eingeladen». "
  "πίστις steht in [[MAT.23.23]] ausnahmsweise als «Treue» (sonst «Glaube»; Begründung in decisions)."),
 ("Die Rede in Kapitel 23 ist scharfe Polemik. Die Übersetzung gibt sie wörtlich wieder, ohne sie abzuschwächen oder "
  "zuzuspitzen; Schriftgelehrte und Pharisäer werden mit den gewöhnlichen Bezeichnungen genannt. Matthäus schreibt aus "
  "einem innerjüdischen Konflikt seiner Zeit; Jesus und seine Jünger sind selbst Juden, und die Rede beginnt mit der "
  "Weisung, zu tun und zu halten, was die Schriftgelehrten und Pharisäer sagen ([[MAT.23.3]]). Pauschale Urteile über das "
  "Judentum oder über Pharisäer aller Zeiten sind damit nicht gedeckt; die Wirkungsgeschichte der Weherufe im christlichen "
  "Judenhass ist mitzubedenken."),
 ("Erzählweise: Das erzählende Präsens (λέγει «sagt») ist beibehalten. λέγων vor direkter Rede ist teils nicht eigens "
  "übersetzt. Anführungszeichen sind eine Entscheidung der Übersetzung, denn das Griechische hat keine; die Rede Jesu "
  "reicht in Kapitel 23 von [[MAT.23.2]] bis [[MAT.23.39]]. Wie die übrigen grossen Reden (vgl. [[MAT.6.5-MAT.6.15]]) steht "
  "sie ohne äussere Anführungszeichen; wörtliche Rede innerhalb der Rede steht in «…»."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT gegen andere Ausgaben liest (z. B. [[MAT.22.30]] "
  "θεοῦ mit Holmes gegen WH, Treg und NA28; [[MAT.23.4]] ohne καὶ δυσβάστακτα mit WH gegen Treg, NA28 und RP). Abweichende "
  "Lesarten stehen als Alternativen, soweit sie die Übersetzung verändern; Unterschiede nur der Wortstellung oder der "
  "Form ohne Folgen für die Übersetzung sind nicht aufgenommen."),
 ("[[MAT.23.14]] (verbreitete Zählung) fehlt im SBLGNT wie bei Westcott/Hort, Tregelles und NA28. Robinson/Pierpont haben "
  "den Weheruf über das Auffressen der Häuser der Witwen vor [[MAT.23.13]] (dort als Vers 13 gezählt), der Textus Receptus "
  "nach [[MAT.23.13]] als Vers 14. Weil es dafür keine SBLGNT-Tokens gibt, enthält diese Übersetzung für [[MAT.23.14]] "
  "keinen Text; der Wortlaut steht als Alternative bei [[MAT.23.12]] und [[MAT.23.13]]. Der Weheruf entspricht weitgehend "
  "[[MRK.12.40]] und [[LUK.20.47]]."),
 "Eigene Formulierung; nicht aus einer veröffentlichten Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1), nöd uf eigeter "
  "Prüefig vo de Handschrifte. Wo si em SBLGNT-Apparat widerspricht, gilt de Apparat."),
 ("Gmeinsami Begriff fürs ganz Matthäusevangelium: «s Riich vo de Himel», «öise/eue Vatter i de Himel», «himmlisch», «Amen, "
  "ich säg eu», «lueg», «dänn», «Schriftgelehrti» (mit Artikel «d Schriftgelehrte»), «Pharisäer», «Sadduzäer», "
  "«Hüüchler», «Christus», ὄχλος «d Mängi» und οἱ ὄχλοι «d Lüüt», προσέρχομαι «härechoo», γεννήματα ἐχιδνῶν «Viperebruet», "
  "«s Hüüle und s Zändchnirsche», δοῦλος «Chnächt». Nöi für Kapitel 22–23: οὐαί «Weh»; γέεννα «Höll»; γενεά «Generation»; "
  "διάκονος «Diener»; καθηγητής «Lehrmeischter»; πίστις i [[MAT.23.23]] usnahmswiis «Treui»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de David»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«s Riich vo de Himel»). D Red vom Jesus i Kapitel 23 staat wie di andere grosse Rede ohni üsseri "
  "Aafüerigszeiche; wörtlichi Red drin staat in «…»."),
 ("D Red i Kapitel 23 isch schaarfi Polemik. D Übersetzig git si wörtlich wider, ohni abzschwäche oder zuezspitze; "
  "de Matthäus schriibt us eme innerjüdische Konflikt vo sinere Ziit. Pauschali Urteil über s Judetum oder über "
  "Pharisäer vo allne Ziite sind damit nöd deckt."),
 ("[[MAT.23.14]] (verbreiteti Zellig) fehlt im SBLGNT wie bi WH, Tregelles und NA28; RP hät de Weheruef vor [[MAT.23.13]], "
  "de Textus Receptus nach [[MAT.23.13]]. Wil s kei SBLGNT-Tokens git, hät die Übersetzig für [[MAT.23.14]] kein Text; de "
  "Wortlut staat als Alternative bi [[MAT.23.12]] und [[MAT.23.13]]."),
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
                      f"KI-Entwurf (Claude) vom {DATE}; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-mat").glob("VAR-SBLGNTAPP-MAT-02[23]-*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-MAT-{c:03d}.json")
        # Verse ohne SBLGNT-Tokens (MAT.23.14) erhalten keinen Text
        refs_c = [f"MAT.{c}.{v}" for v in range(1, last + 1) if f"MAT.{c}.{v}" in toks]
        missing = {f"MAT.{c}.{v}" for v in range(1, last + 1)} - set(refs_c)
        if missing != {m for m in MISSING if m.startswith(f"MAT.{c}.")}:
            raise SystemExit(f"MAT {c}: unerwartet fehlende Verse {sorted(missing)}")
        follows = []
        for vid, v in variants.items():
            if v["reference"] not in refs_c:
                continue
            r1 = [r for r in v["readings"] if r.get("reading_id") == "R1"]
            if r1 and r1[0].get("is_sblgnt_text") is False:
                raise SystemExit(f"{vid}: R1 ist nicht der SBLGNT-Text")
            follows.append(f"{vid}:R1")
        follows.sort()
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Riich, Huus), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Namen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; Begriffe nach den gemeinsamen Wiedergaben für das Matthäusevangelium (abgestimmt auf [[MAT.6.5-MAT.6.15]]) und, bei gleichem Wortlaut, auf die Markus-Übersetzung. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
                                       if lang == "de" else "Direkt aus dem SBLGNT übersetzt, mit Wortzuordnung zu den Token; die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle. Begriffe nach den gemeinsamen Wiedergaben für das Matthäusevangelium. Nicht aus einer veröffentlichten Mundart-Bibel übernommen."),
                        "based_on_edition": "ED-SBLGNT", "based_on_tokens": ts_id, "follows_readings": follows,
                        "text_by_reference": texts, "authorship_de": AUTH if lang == "de" else AUTH_GSW,
                        "translation_notes": NOTES_DE if lang == "de" else NOTES_GSW,
                        "knowledge": {"asserted_at": DATE, "supersedes": None}, "decisions": dec,
                        "decisions_note_de": "Übersetzungsentscheidungen: wörtlich (literal), sprachlich angepasst (adapted), Deutungsentscheidung (interpretive) oder der vertrauten Wiedergabe folgend (traditional). " + (AUTH if lang == "de" else AUTH_GSW)})
            if c != 23:
                rec["translation_notes"] = [x for x in rec["translation_notes"] if "MAT.23.14" not in x]
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_22_23.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 22–23 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
