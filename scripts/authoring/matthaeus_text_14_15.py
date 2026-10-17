#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 14–15 (Tod des Täufers, Speisung der Fünftausend, Gang auf dem Wasser, rein und unrein,
die kanaanäische Frau, Speisung der Viertausend) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus
dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_14_15.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 14–15 fehlt im SBLGNT kein Vers (per Skript geprüft); alle Verse haben Tokens.
- Parallelen bei Markus ([[MRK.6.14]]–[[MRK.6.56]], [[MRK.7.1]]–[[MRK.7.30]], [[MRK.8.1]]–[[MRK.8.10]]): gleiche griechische
  Wendungen sind möglichst gleich übersetzt wie in den Markus-Arbeitsübersetzungen; wo Matthäus anders formuliert, folgt die
  Übersetzung seinem Wortlaut.
- Einheitliche Begriffe für das ganze Matthäusevangelium laut Vorgabe (Schriftgelehrte, Heuchler, sogleich, siehe usw.);
  in diesem Bereich neu festgelegte Wiedergaben stehen in translation_notes.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1),
nicht aus eigener Prüfung der Handschriften. Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des
SBLGNT-Texts (data/annotations) ermittelt.
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
CHAPTERS = ((14, 36), (15, 39))

DE = {
 # ------------------------------------------------------------ Kapitel 14
 "MAT.14.1": "[In]{1} [jener]{2} [Zeit]{3,4} [hörte]{5} [Herodes]{6}, [der Tetrarch]{7,8}, [die Kunde]{9,10} [von Jesus]{11}",
 "MAT.14.2": "und{1} [sagte]{2} [zu]{3} [seinen]{5} [Dienern]{4}: «[Das]{6} [ist]{7} [Johannes]{8} [der Täufer]{9,10}; [er]{11} [ist]{12} [von]{13} [den Toten]{14,15} [auferweckt worden]{12}, und{16} [darum]{17,18} [wirken]{21} [die Kräfte]{19,20} [in]{22} [ihm]{23}.»",
 "MAT.14.3": "[Herodes]{1,3} [hatte]{4} [nämlich]{2} [Johannes]{5,6} [festgenommen]{4}, [ihn]{8} [gefesselt]{7} und{9} [ins]{10} [Gefängnis]{11} [gebracht]{12}, [wegen]{13} [Herodias]{14}, [der Frau]{15,16} [seines]{20} [Bruders]{18,19} [Philippus]{17}.",
 "MAT.14.4": "[Denn]{2} [Johannes]{4,5} [sagte]{1} [zu ihm]{3}: «[Es ist]{7} [dir]{8} [nicht]{6} [erlaubt]{7}, [sie]{10} [zu haben]{9}.»",
 "MAT.14.5": "Und{1} [obwohl er]{2} [ihn]{3} [töten]{4} [wollte]{2}, [fürchtete er]{5} [die Menge]{6,7}, [weil]{8} [sie]{12} [ihn]{11} [für]{9} [einen Propheten]{10} [hielten]{12}.",
 "MAT.14.6": "[Als]{3} [aber]{2} [der Geburtstag]{1} [des Herodes]{4,5} [gefeiert wurde]{3}, [tanzte]{6} [die Tochter]{7,8} [der Herodias]{9,10} [vor allen]{11-13} und{14} [gefiel]{15} [Herodes]{16,17}.",
 "MAT.14.7": "[Darum]{1} [versprach er]{4} [ihr]{5} [mit]{2} [einem Eid]{3}, ihr [zu geben]{6}, [was]{7} [immer]{8} [sie erbitten würde]{9}.",
 "MAT.14.8": "[Sie]{1} [aber]{2}, [von]{4} [ihrer]{7} [Mutter]{5,6} [angestiftet]{3}, [sagt]{10}: «[Gib]{8} [mir]{9} [hier]{11} [auf]{12} [einer Schale]{13} [den Kopf]{14,15} [des Johannes]{16} [des Täufers]{17,18}!»",
 "MAT.14.9": "Und{1} [obwohl]{2} [der König]{3,4} [betrübt war]{2}, [befahl er]{11} [wegen]{5} [der Eide]{6,7} und{8} [der Gäste]{9,10}, [dass man es ihr gebe]{12}.",
 "MAT.14.10": "Und{1} [er schickte hin]{2} und [liess]{3} [Johannes]{4,5} [im]{6,7} [Gefängnis]{8} [enthaupten]{3}.",
 "MAT.14.11": "Und{1} [sein]{5} [Kopf]{3,4} [wurde]{2} [auf]{6} [einer Schale]{7} [gebracht]{2} und{8} [dem Mädchen]{10,11} [gegeben]{9}, und{12} [es brachte]{13} ihn [seiner]{16} [Mutter]{14,15}.",
 "MAT.14.12": "Und{1} [seine]{5} [Jünger]{3,4} [kamen]{2}, [holten]{6} [den Leichnam]{7,8} und{9} [begruben]{10} [ihn]{11}; und{12} [sie gingen hin]{13} und [berichteten]{14} es [Jesus]{15,16}.",
 "MAT.14.13": "[Als]{1} [aber]{2} [Jesus]{3,4} das [hörte]{1}, [zog er sich]{5} [von dort]{6} [in]{7} [einem Boot]{8} [an]{9} [einen einsamen]{10} [Ort]{11} [zurück]{5}, [für sich allein]{12,13}; und{14} [als]{15} [die Leute]{16,17} [es hörten]{15}, [folgten sie]{18} [ihm]{19} [zu Fuss]{20} [aus]{21} [den Städten]{22,23}.",
 "MAT.14.14": "Und{1} [als er ausstieg]{2}, [sah er]{3} [eine grosse]{4} [Menge]{5}, und{6} [er hatte Erbarmen]{7} [mit]{8} [ihnen]{9} und{10} [heilte]{11} [ihre]{14} [Kranken]{12,13}.",
 "MAT.14.15": "[Als]{3} es [aber]{2} [Abend]{1} [geworden war]{3}, [traten]{4} [die Jünger]{6,7} [zu ihm]{5} und [sagten]{8}: «[Der Ort]{11,12} [ist]{10} [einsam]{9}, und{13} [die Stunde]{14,15} [ist]{17} [schon]{16} [vorgerückt]{17}; [schick]{18} [die Leute]{19,20} [weg]{18}, [damit]{21} sie [in]{23} [die Dörfer]{24,25} [gehen]{22} und [sich]{27} [etwas zu essen]{28} [kaufen]{26}.»",
 "MAT.14.16": "[Jesus]{1,3} [aber]{2} [sagte]{4} [zu ihnen]{5}: «[Sie haben]{8} es [nicht]{6} [nötig]{7}, [wegzugehen]{9}; [gebt]{10} [ihr]{12} [ihnen]{11} [zu essen]{13}!»",
 "MAT.14.17": "[Sie]{1} [aber]{2} [sagen]{3} [zu ihm]{4}: «[Wir haben]{6} [hier]{7} [nichts]{5} [ausser]{8,9} [fünf]{10} [Broten]{11} und{12} [zwei]{13} [Fischen]{14}.»",
 "MAT.14.18": "[Er]{1} [aber]{2} [sagte]{3}: «[Bringt]{4} [sie]{7} [mir]{5} [hierher]{6}!»",
 "MAT.14.19": "Und{1} [er befahl]{2} [den Leuten]{3,4}, sich [auf]{6} [dem Gras]{7,8} [zu lagern]{5}, [nahm]{9} [die fünf]{10,11} [Brote]{12} und{13} [die zwei]{14,15} [Fische]{16}, [blickte]{17} [zum]{18,19} [Himmel]{20} [auf]{17}, [sprach den Segen]{21} und{22} [brach]{23} [die Brote]{27,28} und [gab]{24} sie [den Jüngern]{25,26}, [die Jünger]{29,31} [aber]{30} [den Leuten]{32,33}.",
 "MAT.14.20": "Und{1} [alle]{3} [assen]{2} und{4} [wurden satt]{5}; und{6} [sie hoben auf]{7}, [was]{8} [an Brocken]{10,11} [übrig blieb]{9}: [zwölf]{12} [Körbe]{13} [voll]{14}.",
 "MAT.14.21": "[Die]{1} [aber]{2} [gegessen hatten]{3}, [waren]{4} [etwa]{6} [fünftausend]{7} [Männer]{5}, [ohne]{8} [Frauen]{9} und{10} [Kinder]{11}.",
 "MAT.14.22": "Und{1} [sogleich]{2} [nötigte er]{3} [die Jünger]{4,5}, [ins]{7} [Boot]{8} [zu steigen]{6} und{9} [ihm]{11} [ans]{12,13} [andere Ufer]{14} [vorauszufahren]{10}, [bis]{15,16} er [die Leute]{18,19} [entlassen hätte]{17}.",
 "MAT.14.23": "Und{1} [nachdem er]{2} [die Leute]{3,4} [entlassen hatte]{2}, [stieg er]{5} [auf]{6} [den Berg]{7,8} [hinauf]{5}, [für sich allein]{9,10}, [um zu beten]{11}. [Als]{14} es [aber]{13} [Abend]{12} [geworden war]{14}, [war er]{16} [dort]{17} [allein]{15}.",
 "MAT.14.24": "[Das Boot]{1,3} [aber]{2} [war]{10} [schon]{4} [viele]{6} [Stadien]{5} [vom]{7,8} [Land]{9} [entfernt]{10} und wurde [von]{12} [den Wellen]{13,14} [bedrängt]{11}; [denn]{16} [der Wind]{18,19} [stand]{15} ihnen [entgegen]{17}.",
 "MAT.14.25": "[In der vierten]{1} [Nachtwache]{3-5} [aber]{2} [kam er]{6} [zu]{7} [ihnen]{8} und [ging]{9} dabei [auf]{10} [dem See]{11,12}.",
 "MAT.14.26": "[Als]{4} [aber]{2} [die Jünger]{1,3} [ihn]{5} [auf]{6} [dem See]{7,8} [gehen]{9} [sahen]{4}, [erschraken sie]{10} und [sagten]{11}: «[Es ist]{14} [ein Gespenst]{13}!», und{15} [vor]{16} [Furcht]{17,18} [schrien sie auf]{19}. ~12(ὅτι leitet die direkte Rede ein)",
 "MAT.14.27": "[Sogleich]{1} [aber]{2} [redete]{3} [Jesus]{5,6} [mit ihnen]{4} und [sagte]{7}: «[Seid getrost]{8}, [ich]{9} [bin es]{10}; [fürchtet euch]{12} [nicht]{11}!»",
 "MAT.14.28": "[Petrus]{4,5} [aber]{2} [antwortete]{1} [ihm]{3} und [sagte]{6}: «[Herr]{7}, [wenn]{8} [du]{9} [es bist]{10}, [befiehl]{11} [mir]{12}, [auf]{16} [dem Wasser]{17,18} [zu]{14} [dir]{15} [zu kommen]{13}!»",
 "MAT.14.29": "[Er]{1} [aber]{2} [sagte]{3}: «[Komm]{4}!» Und{5} [Petrus]{10} [stieg]{6} [aus]{7} [dem Boot]{8,9}, [ging]{11} [auf]{12} [dem Wasser]{13,14} und{15} [kam]{16} [zu]{17} [Jesus]{18,19}.",
 "MAT.14.30": "[Als er]{1} [aber]{2} [den starken]{3,5} [Wind]{4} [sah]{1}, [fürchtete er sich]{6}, und{7} [als er]{8} [zu versinken]{9} [begann]{8}, [schrie er]{10}: «[Herr]{12}, [rette]{13} [mich]{14}!» ~11(λέγων «sagend» leitet die direkte Rede ein)",
 "MAT.14.31": "[Sogleich]{1} [aber]{2} [streckte]{5} [Jesus]{3,4} [die Hand]{6,7} [aus]{5}, [ergriff]{8} [ihn]{9} und{10} [sagt]{11} [zu ihm]{12}: «[Du Kleingläubiger]{13}, [warum]{14,15} [hast du gezweifelt]{16}?»",
 "MAT.14.32": "Und{1} [als]{2} [sie]{3} [ins]{4,5} [Boot]{6} [gestiegen waren]{2}, [legte sich]{7} [der Wind]{8,9}.",
 "MAT.14.33": "[Die]{1} [aber]{2} [im]{3,4} [Boot]{5} waren, [fielen vor]{6} [ihm]{7} [nieder]{6} und [sagten]{8}: «[Wahrhaftig]{9}, [du bist]{12} [Gottes]{10} [Sohn]{11}!»",
 "MAT.14.34": "Und{1} [als sie hinübergefahren waren]{2}, [kamen sie]{3} [in]{7} [Gennesaret]{8} [an]{4} [Land]{5,6}.",
 "MAT.14.35": "Und{1} [als]{2} [die Männer]{4,5} [jenes]{8} [Ortes]{6,7} [ihn]{3} [erkannten]{2}, [schickten sie]{9} Boten [in]{10} [jene]{14} [ganze]{11} [Umgebung]{12,13}, und{15} [sie brachten]{16} [ihm]{17} [alle]{18} [Kranken]{19-21}.",
 "MAT.14.36": "Und{1} [sie baten]{2} [ihn]{3}, [dass]{4} sie [nur]{5} [den Saum]{7,8} [seines]{11} [Mantels]{9,10} [berühren dürften]{6}; und{12} [alle, die]{13} [ihn berührten]{14}, [wurden gerettet]{15}.",
 # ------------------------------------------------------------ Kapitel 15
 "MAT.15.1": "[Da]{1} [kommen]{2} [Pharisäer]{7} und{8} [Schriftgelehrte]{9} [aus]{5} [Jerusalem]{6} [zu]{3} [Jesus]{4} und [sagen]{10}:",
 "MAT.15.2": "«[Warum]{1,2} [übertreten]{6} [deine]{5} [Jünger]{3,4} [die Überlieferung]{7,8} [der Ältesten]{9,10}? [Denn]{12} [sie waschen]{13} [ihre]{16} [Hände]{14,15} [nicht]{11}, [wenn]{17} sie [Brot]{18} [essen]{19}.»",
 "MAT.15.3": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4} [zu ihnen]{5}: «[Warum]{6,7} [übertretet]{10} [auch]{8} [ihr]{9} [das Gebot]{11,12} [Gottes]{13,14} [um]{15} [eurer]{18} [Überlieferung]{16,17} [willen]{15}?",
 "MAT.15.4": "[Denn]{2} [Gott]{1,3} [hat gesagt]{4}: ‹[Ehre]{5} [den Vater]{6,7} und{8} [die Mutter]{9,10}›, und{11}: ‹[Wer]{12} [Vater]{14} [oder]{15} [Mutter]{16} [verflucht]{13}, [soll]{18} [des Todes]{17} [sterben]{18}.›",
 "MAT.15.5": "[Ihr]{1} [aber]{2} [sagt]{3}: ‹[Wer]{4,5} [zum Vater]{7,8} [oder]{9} [zur Mutter]{10,11} [sagt]{6}: [Opfergabe]{12} sei, [was]{13,14} [du]{17} [von]{15} [mir]{16} [an Hilfe bekommen könntest]{17},",
 "MAT.15.6": "[der braucht]{3} [seinen]{6} [Vater]{4,5} [nicht]{1,2} [zu ehren]{3}.› Und{7} [ihr habt]{8} [das Wort]{9,10} [Gottes]{11,12} [um]{13} [eurer]{16} [Überlieferung]{14,15} [willen]{13} [ausser Kraft gesetzt]{8}.",
 "MAT.15.7": "[Ihr Heuchler]{1}! [Treffend]{2} [hat]{3} [Jesaja]{6} [über]{4} [euch]{5} [geweissagt]{3}, [als er sagte]{7}:",
 "MAT.15.8": "‹[Dieses]{3} [Volk]{1,2} [ehrt]{7} [mich]{6} [mit den Lippen]{4,5}, [ihr]{11} [Herz]{8,10} [aber]{9} [ist]{13} [weit]{12} [entfernt]{13} [von]{14} [mir]{15};",
 "MAT.15.9": "[vergeblich]{1} [aber]{2} [verehren sie]{3} [mich]{4}, [indem sie]{5} [als Lehren]{6} [Gebote]{7} [von Menschen]{8} [lehren]{5}.›»",
 "MAT.15.10": "Und{1} [er rief]{2} [die Menge]{3,4} [herbei]{2} und [sagte]{5} [zu ihnen]{6}: «[Hört]{7} und{8} [versteht]{9}!",
 "MAT.15.11": "[Nicht]{1} [was]{2} [in]{4} [den Mund]{5,6} [hineingeht]{3}, [macht]{7} [den Menschen]{8,9} [unrein]{7}, [sondern]{10} [was]{11} [aus]{13} [dem Mund]{14,15} [herauskommt]{12}, [das]{16} [macht]{17} [den Menschen]{18,19} [unrein]{17}.»",
 "MAT.15.12": "[Da]{1} [traten]{2} [die Jünger]{3,4} [hinzu]{2} und [sagen]{5} [zu ihm]{6}: «[Weisst du]{7}, [dass]{8} [die Pharisäer]{9,10} [Anstoss genommen haben]{14}, [als sie]{11} [das Wort]{12,13} [hörten]{11}?»",
 "MAT.15.13": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: «[Jede]{5} [Pflanze]{6}, [die]{7} [mein]{12} [himmlischer]{13,14} [Vater]{10,11} [nicht]{8} [gepflanzt hat]{9}, [wird ausgerissen werden]{15}.",
 "MAT.15.14": "[Lasst]{1} [sie]{2}! [Sie sind]{4} [Blinde]{3}, [Führer]{5} [von Blinden]{6}. [Wenn]{10} [aber]{8} [ein Blinder]{7} [einen Blinden]{9} [führt]{11}, [werden]{15} [beide]{12} [in]{13} [eine Grube]{14} [fallen]{15}.»",
 "MAT.15.15": "[Petrus]{3,4} [aber]{2} [antwortete]{1} und [sagte]{5} [zu ihm]{6}: «[Erkläre]{7} [uns]{8} [dieses]{11} [Gleichnis]{9,10}!»",
 "MAT.15.16": "[Er]{1} [aber]{2} [sagte]{3}: «[Seid]{8} [auch]{5} [ihr]{6} [noch immer]{4} [unverständig]{7}?",
 "MAT.15.17": "[Begreift ihr]{2} [nicht]{1}, [dass]{3} [alles]{4}, [was]{5} [in]{7} [den Mund]{8,9} [hineingeht]{6}, [in]{10} [den Bauch]{11,12} [gelangt]{13} und{14} [in]{15} [den Abort]{16} [ausgeschieden wird]{17}?",
 "MAT.15.18": "[Was]{1} [aber]{2} [aus]{4} [dem Mund]{5,6} [herauskommt]{3}, [kommt]{10} [aus]{7} [dem Herzen]{8,9} [hervor]{10}, [und das]{11} [macht]{12} [den Menschen]{13,14} [unrein]{12}.",
 "MAT.15.19": "[Denn]{2} [aus]{1} [dem Herzen]{3,4} [kommen]{5} [böse]{7} [Gedanken]{6} [hervor]{5}: [Morde]{8}, [Ehebrüche]{9}, [Unzucht]{10}, [Diebstähle]{11}, [falsche Zeugnisse]{12}, [Lästerungen]{13}.",
 "MAT.15.20": "[Das]{1} [ist es]{2}, [was]{3} [den Menschen]{5,6} [unrein macht]{4}; [aber]{8} [mit ungewaschenen]{9} [Händen]{10} [zu essen]{7,11} [macht]{13} [den Menschen]{14,15} [nicht]{12} [unrein]{13}.»",
 "MAT.15.21": "Und{1} [Jesus]{4,5} [ging]{2} [von dort]{3} [weg]{2} und [zog sich]{6} [in]{7} [die Gegend]{8,9} [von Tyros]{10} und{11} [Sidon]{12} [zurück]{6}.",
 "MAT.15.22": "Und{1} [siehe]{2}, [eine kanaanäische]{4} [Frau]{3} [kam]{9} [aus]{5} [jenem]{8} [Gebiet]{6,7} [heraus]{9} und [schrie]{10}: «[Hab Erbarmen]{12} [mit mir]{13}, [Herr]{14}, [Sohn]{15} [Davids]{16}! [Meine]{19} [Tochter]{17,18} [ist]{21} [schlimm]{20} [besessen]{21}.» ~11(λέγουσα «sagend» leitet die direkte Rede ein)",
 "MAT.15.23": "[Er]{1} [aber]{2} [antwortete]{4} [ihr]{5} [kein]{3} [Wort]{6}. Und{7} [seine]{11} [Jünger]{9,10} [traten hinzu]{8}, [baten]{12} [ihn]{13} und [sagten]{14}: «[Schick]{15} [sie]{16} [fort]{15}, [denn]{17} [sie schreit]{18} [hinter]{19} [uns]{20} [her]{19}!»",
 "MAT.15.24": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: «[Ich bin]{6} [nur]{5,7,8} [zu]{9} [den]{10} [verlorenen]{12,13} [Schafen]{11} [des Hauses]{14} [Israel]{15} [gesandt]{6}.»",
 "MAT.15.25": "[Sie]{1} [aber]{2} [kam]{3}, [fiel vor]{4} [ihm]{5} [nieder]{4} und [sagte]{6}: «[Herr]{7}, [hilf]{8} [mir]{9}!»",
 "MAT.15.26": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: «[Es ist]{6} [nicht]{5} [recht]{7}, [das Brot]{9,10} [der Kinder]{11,12} [zu nehmen]{8} und{13} [den Hündchen]{15,16} [hinzuwerfen]{14}.»",
 "MAT.15.27": "[Sie]{1} [aber]{2} [sagte]{3}: «[Ja]{4}, [Herr]{5}; [denn]{7} [auch]{6} [die Hündchen]{8,9} [essen]{10} [von]{11} [den Brotkrumen]{12,13}, [die]{14} [vom]{16,17} [Tisch]{18} [ihrer]{21} [Herren]{19,20} [fallen]{15}.»",
 "MAT.15.28": "[Da]{1} [antwortete]{2} [Jesus]{3,4} und [sagte]{5} [zu ihr]{6}: «[Frau]{8}, [dein]{10} [Glaube]{11,12} ist [gross]{9}! [Dir]{14} [geschehe]{13}, [wie]{15} [du willst]{16}.» Und{17} [ihre]{21} [Tochter]{19,20} [war]{18} [von]{22} [jener]{25} [Stunde]{23,24} [an]{22} [geheilt]{18}. ~7(Ὦ «o» verstärkt die Anrede; durch den Ausruf wiedergegeben)",
 "MAT.15.29": "Und{1} [Jesus]{4,5} [zog]{2} [von dort]{3} [weiter]{2} und [kam]{6} [an]{7} [den See]{8,9} [von Galiläa]{10,11}; und{12} [er stieg]{13} [auf]{14} [den Berg]{15,16} [hinauf]{13} und [sass]{17} [dort]{18}.",
 "MAT.15.30": "Und{1} [viele]{5} [Leute]{4} [kamen]{2} [zu ihm]{3} und [hatten]{6} [Stumme]{9}, [Blinde]{10}, [Lahme]{11}, [Verkrüppelte]{12} und{13} [viele]{15} [andere]{14} [bei]{7} [sich]{8}; und{16} [sie legten]{17} [sie]{18} [zu]{19} [seinen]{22} [Füssen]{20,21} [hin]{17}, und{23} [er heilte]{24} [sie]{25},",
 "MAT.15.31": "[sodass]{1} [die Menge]{2,3} [staunte]{4}, [als sie sah]{5}, wie [Stumme]{6} [redeten]{7}, [Verkrüppelte]{8} [gesund]{9} waren und{10} [Lahme]{11} [umhergingen]{12} und{13} [Blinde]{14} [sahen]{15}; und{16} [sie priesen]{17} [den Gott]{18,19} [Israels]{20}.",
 "MAT.15.32": "[Jesus]{1,3} [aber]{2} [rief]{4} [seine]{7} [Jünger]{5,6} [herbei]{4} und [sagte]{8}: «[Ich habe Erbarmen]{9} [mit]{10} [der Menge]{11,12}, [denn]{13} [schon]{14} [drei]{16} [Tage]{15} [bleiben sie]{17} [bei mir]{18} und{19} [haben]{21} [nichts]{20,22} [zu essen]{23}. Und{24} [ich will]{29} [sie]{26} [nicht]{28} [hungrig]{27} [wegschicken]{25}, [damit]{30} sie [nicht]{30} [unterwegs]{32-34} [zusammenbrechen]{31}.»",
 "MAT.15.33": "Und{1} [die Jünger]{4,5} [sagen]{2} [zu ihm]{3}: «[Woher]{6} [sollen wir]{7} [in]{8} [der Einöde]{9} [so viele]{11} [Brote]{10} nehmen, [um]{12} [eine so grosse]{15} [Menge]{14} [satt zu machen]{13}?»",
 "MAT.15.34": "Und{1} [Jesus]{4,5} [sagt]{2} [zu ihnen]{3}: «[Wie viele]{6} [Brote]{7} [habt ihr]{8}?» [Sie]{9} [aber]{10} [sagten]{11}: «[Sieben]{12}, und{13} [ein paar]{14} [Fischlein]{15}.»",
 "MAT.15.35": "Und{1} [er gebot]{2} [der Menge]{3,4}, sich [auf]{6} [den Boden]{7,8} [zu lagern]{5},",
 "MAT.15.36": "[nahm]{1} [die sieben]{2,3} [Brote]{4} und{5} [die Fische]{6,7} und{8} [sprach das Dankgebet]{9}, [brach]{10} sie und{11} [gab]{12} sie [den Jüngern]{13,14}, [die Jünger]{15,17} [aber]{16} [den Leuten]{18,19}.",
 "MAT.15.37": "Und{1} [alle]{3} [assen]{2} und{4} [wurden satt]{5}; und{6} [was]{7} [an Brocken]{9,10} [übrig blieb]{8}, [hoben sie auf]{11}: [sieben]{12} [Körbe]{13} [voll]{14}.",
 "MAT.15.38": "[Die]{1} [aber]{2} [gegessen hatten]{3}, [waren]{4} [viertausend]{5} [Männer]{6}, [ohne]{7} [Frauen]{8} und{9} [Kinder]{10}.",
 "MAT.15.39": "Und{1} [nachdem er]{2} [die Leute]{3,4} [entlassen hatte]{2}, [stieg er]{5} [ins]{6,7} [Boot]{8} und{9} [kam]{10} [in]{11} [das Gebiet]{12,13} [von Magadan]{14}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 14
 "MAT.14.1": "[I]{1} [dere]{2} [Ziit]{3,4} [hät]{5} [de Herodes]{6}, [de Tetrarch]{7,8}, [d Nachricht]{9,10} [vom Jesus]{11} [ghört]{5}",
 "MAT.14.2": "und{1} [hät]{2} [zu]{3} [sine]{5} [Diener]{4} [gseit]{2}: «[Das]{6} [isch]{7} [de Johannes]{8} [de Täufer]{9,10}; [er]{11} [isch]{12} [vo]{13} [de Tote]{14,15} [uferweckt worde]{12}, und{16} [drum]{17,18} [würked]{21} [d Chräft]{19,20} [i]{22} [ihm]{23}.»",
 "MAT.14.3": "[De Herodes]{1,3} [hät]{4} [nämli]{2} [de Johannes]{5,6} [feschtgnoo]{4}, [en]{8} [gfesslet]{7} und{9} [is]{10} [Gfängnis]{11} [brocht]{12}, [wäge]{13} [de Herodias]{14}, [de Frau]{15,16} [vo sim]{20} [Brüeder]{18,19} [Philippus]{17}.",
 "MAT.14.4": "[De Johannes]{4,5} [hät]{1} [ihm]{3} [nämli]{2} [gseit]{1}: «[Es isch]{7} [dir]{8} [nöd]{6} [erlaubt]{7}, [si]{10} [z haa]{9}.»",
 "MAT.14.5": "Und{1} [obwohl er]{2} [en]{3} [hät wele]{2} [umbringe]{4}, [hät er]{5} [d Mängi]{6,7} [gförchtet]{5}, [wil]{8} [si]{12} [en]{11} [für]{9} [en Prophet]{10} [ghalte händ]{12}.",
 "MAT.14.6": "[Wo]{3} [aber]{2} [de Geburtstag]{1} [vom Herodes]{4,5} [gfiiret worde isch]{3}, [hät]{6} [d Tochter]{7,8} [vo de Herodias]{9,10} [vor allne]{11-13} [tanzt]{6}, und{14} [si hät]{15} [em Herodes]{16,17} [gfalle]{15}.",
 "MAT.14.7": "[Drum]{1} [hät er]{4} [ere]{5} [mit]{2} [eme Eid]{3} [versproche]{4}, ere [z gää]{6}, [was]{7} [si]{9} [au]{8} [heusche würd]{9}.",
 "MAT.14.8": "[Si]{1} [aber]{2}, [vo]{4} [irer]{7} [Mueter]{5,6} [aagstiftet]{3}, [seit]{10}: «[Gib]{8} [mir]{9} [da]{11} [uf]{12} [ere Platte]{13} [de Chopf]{14,15} [vom Johannes]{16} [em Täufer]{17,18}!»",
 "MAT.14.9": "Und{1} [obwohl]{2} [de König]{3,4} [truurig gsii isch]{2}, [hät er]{11} [wäge]{5} [de Eid]{6,7} und{8} [wäge de Gäscht]{9,10} [befole]{11}, [me söll ere s gää]{12}.",
 "MAT.14.10": "Und{1} [er hät öpper gschickt]{2} und [hät]{3} [de Johannes]{4,5} [im]{6,7} [Gfängnis]{8} [la chöpfe]{3}.",
 "MAT.14.11": "Und{1} [sin]{5} [Chopf]{3,4} [isch]{2} [uf]{6} [ere Platte]{7} [brocht worde]{2} und{8} [em Meitli]{10,11} [gää worde]{9}, und{12} [es hät]{13} en [sinere]{16} [Mueter]{14,15} [brocht]{13}.",
 "MAT.14.12": "Und{1} [sini]{5} [Jünger]{3,4} [sind choo]{2}, [händ]{6} [d Liich]{7,8} [gholt]{6} und{9} [händ]{10} [si]{11} [begrabe]{10}; und{12} [si sind gange]{13} und [händ]{14} s [em Jesus]{15,16} [gmäldet]{14}.",
 "MAT.14.13": "[Wo]{1} [aber]{2} [de Jesus]{3,4} das [ghört hät]{1}, [hät er sich]{5} [vo dört]{6} [imene Boot]{7,8} [an]{9} [en einsame]{10} [Ort]{11} [zruggzoge]{5}, [für sich elei]{12,13}; und{14} [wo]{15} [d Lüüt]{16,17} [s ghört händ]{15}, [sind si]{18} [ihm]{19} [z Fuess]{20} [us]{21} [de Städt]{22,23} [nachegange]{18}.",
 "MAT.14.14": "Und{1} [wo er usgstige isch]{2}, [hät er]{3} [e grossi]{4} [Mängi]{5} [gseh]{3}, und{6} [er hät Erbarme]{7} [mit]{8} [ine]{9} [gha]{7} und{10} [hät]{11} [iri]{14} [Chranke]{12,13} [gheilt]{11}.",
 "MAT.14.15": "[Wo]{3} s [aber]{2} [Aabig]{1} [worde isch]{3}, [sind]{4} [d Jünger]{6,7} [zu ihm]{5} [choo]{4} und [händ gseit]{8}: «[De Ort]{11,12} [isch]{10} [einsam]{9}, und{13} [d Ziit]{14,15} [isch]{17} [scho]{16} [vorbii]{17}; [schick]{18} [d Lüüt]{19,20} [furt]{18}, [demit]{21} si [i]{23} [d Dörfer]{24,25} [gönd]{22} und [sich]{27} [öppis z ässe]{28} [chaufed]{26}.»",
 "MAT.14.16": "[De Jesus]{1,3} [aber]{2} [hät]{4} [zu ine]{5} [gseit]{4}: «[Si händ]{8} s [nöd]{6} [nötig]{7}, [furtzgaa]{9}; [gänd]{10} [ir]{12} [ine]{11} [z ässe]{13}!»",
 "MAT.14.17": "[Si]{1} [aber]{2} [säged]{3} [zu ihm]{4}: «[Mir händ]{6} [da]{7} [nüüt]{5} [als]{8,9} [föif]{10} [Broot]{11} und{12} [zwee]{13} [Fisch]{14}.»",
 "MAT.14.18": "[Er]{1} [aber]{2} [hät gseit]{3}: «[Bringed]{4} [si]{7} [mir]{5} [da here]{6}!»",
 "MAT.14.19": "Und{1} [er hät]{2} [de Lüüt]{3,4} [befole]{2}, [sich]{5} [ufs]{6,7} [Gras]{8} [z setze]{5}, [hät]{9} [di föif]{10,11} [Broot]{12} und{13} [di zwee]{14,15} [Fisch]{16} [gnoo]{9}, [hät]{17} [zum]{18,19} [Himel]{20} [ufegluegt]{17}, [de Säge gsproche]{21} und{22} [d Broot]{27,28} [broche]{23} und si [de Jünger]{25,26} [gää]{24}, [d Jünger]{29,31} [aber]{30} [de Lüüt]{32,33}.",
 "MAT.14.20": "Und{1} [alli]{3} [händ ggässe]{2} und{4} [sind satt worde]{5}; und{6} [si händ ufgläse]{7}, [was]{8} [a Brocke]{10,11} [übrig bliibe isch]{9}: [zwölf]{12} [Chörb]{13} [voll]{14}.",
 "MAT.14.21": "[Die]{1} [aber]{2}, wo [ggässe händ]{3}, [sind]{4} [öppe]{6} [föiftuusig]{7} [Manne]{5} [gsii]{4}, [ohni]{8} [Fraue]{9} und{10} [Chind]{11}.",
 "MAT.14.22": "Und{1} [grad]{2} [hät er]{3} [d Jünger]{4,5} [drängt]{3}, [is]{7} [Boot]{8} [z stiige]{6} und{9} [ihm]{11} [as]{12,13} [ander Ufer]{14} [voruszfahre]{10}, [bis]{15,16} er [d Lüüt]{18,19} [furtgschickt hät]{17}.",
 "MAT.14.23": "Und{1} [wo er]{2} [d Lüüt]{3,4} [furtgschickt gha hät]{2}, [isch er]{5} [uf]{6} [de Bärg]{7,8} [ufe]{5}, [für sich elei]{9,10}, [go bätte]{11}. [Wo]{14} s [aber]{13} [Aabig]{12} [worde isch]{14}, [isch er]{16} [dört]{17} [elei]{15} [gsii]{16}.",
 "MAT.14.24": "[S Boot]{1,3} [aber]{2} [isch]{10} [scho]{4} [vili]{6} [Stadie]{5} [vom]{7,8} [Land]{9} [ewägg gsii]{10} und [vo]{12} [de Wälle]{13,14} [plaget worde]{11}; [dänn]{16} [de Wind]{18,19} [isch]{15} ine [entgäge]{17} [gsii]{15}.",
 "MAT.14.25": "[I de vierte]{1} [Nachtwach]{3-5} [aber]{2} [isch er]{6} [zu]{7} [ine]{8} [choo]{6} und [isch]{9} debii [uf]{10} [em See]{11,12} [gloffe]{9}.",
 "MAT.14.26": "[Wo]{4} [aber]{2} [d Jünger]{1,3} [en]{5} [uf]{6} [em See]{7,8} [laufe]{9} [gseh händ]{4}, [sind si verschrocke]{10} und [händ gseit]{11}: «[Es isch]{14} [es Gspängscht]{13}!», und{15} [vor]{16} [Angscht]{17,18} [händ si ufgschroue]{19}. ~12(ὅτι leitet di diräkt Red ii)",
 "MAT.14.27": "[Grad]{1} [aber]{2} [hät]{3} [de Jesus]{5,6} [mit ine]{4} [gredt]{3} und [gseit]{7}: «[Nu Muet]{8}, [ich]{9} [bi s]{10}; [händ]{12} [kei]{11} [Angscht]{12}!»",
 "MAT.14.28": "[De Petrus]{4,5} [aber]{2} [hät]{1} [ihm]{3} [gantwortet]{1} und [gseit]{6}: «[Herr]{7}, [wänn]{8} [du]{9} [s bisch]{10}, [befiil]{11} [mir]{12}, [uf em Wasser]{16-18} [zu]{14} [dir]{15} [z choo]{13}!»",
 "MAT.14.29": "[Er]{1} [aber]{2} [hät gseit]{3}: «[Chumm]{4}!» Und{5} [de Petrus]{10} [isch]{6} [us]{7} [em Boot]{8,9} [gstige]{6}, [isch]{11} [uf]{12} [em Wasser]{13,14} [gloffe]{11} und{15} [isch]{16} [zum]{17,18} [Jesus]{19} [choo]{16}.",
 "MAT.14.30": "[Wo er]{1} [aber]{2} [de starch]{3,5} [Wind]{4} [gseh hät]{1}, [hät er Angscht übercho]{6}, und{7} [wo er aagfange hät]{8} [z versinke]{9}, [hät er gschroue]{10}: «[Herr]{12}, [rett]{13} [mich]{14}!» ~11(λέγων «sägend» leitet di diräkt Red ii)",
 "MAT.14.31": "[Grad]{1} [aber]{2} [hät]{5} [de Jesus]{3,4} [d Hand]{6,7} [usgstreckt]{5}, [hät]{8} [en]{9} [packt]{8} und{10} [seit]{11} [zu ihm]{12}: «[Du Chliigläubige]{13}, [werum]{14,15} [häsch zwiiflet]{16}?»",
 "MAT.14.32": "Und{1} [wo]{2} [si]{3} [is]{4,5} [Boot]{6} [gstige sind]{2}, [hät sich]{7} [de Wind]{8,9} [gleit]{7}.",
 "MAT.14.33": "[Die]{1} [aber]{2}, wo [im]{3,4} [Boot]{5} gsii sind, [sind vor]{6} [ihm]{7} [nidergfalle]{6} und [händ gseit]{8}: «[Würkli]{9}, [du bisch]{12} [de Sohn]{11} [vo Gott]{10}!»",
 "MAT.14.34": "Und{1} [wo si übere gfahre sind]{2}, [sind si]{3} [z]{7} [Gennesaret]{8} [a]{4} [Land]{5,6} [choo]{3}.",
 "MAT.14.35": "Und{1} [wo]{2} [d Manne]{4,5} [vo dem]{6,8} [Ort]{7} [en]{3} [erchännt händ]{2}, [händ si]{9} Bote [i]{10} [die]{14} [ganz]{11} [Gäged]{12,13} [gschickt]{9}, und{15} [si händ]{16} [ihm]{17} [alli]{18} [Chranke]{19-21} [brocht]{16}.",
 "MAT.14.36": "Und{1} [si händ]{2} [en]{3} [bätte]{2}, [dass]{4} si [nu]{5} [de Saum]{7,8} [vo sim]{11} [Mantel]{9,10} [dörfed aarüere]{6}; und{12} [alli, wo]{13} [en aagrüert händ]{14}, [sind grettet worde]{15}.",
 # ------------------------------------------------------------ Kapitel 15
 "MAT.15.1": "[Dänn]{1} [chömed]{2} [Pharisäer]{7} und{8} [Schriftgelehrti]{9} [vo]{5} [Jerusalem]{6} [zum]{3} [Jesus]{4} und [säged]{10}:",
 "MAT.15.2": "«[Werum]{1,2} [verstoossed]{6} [dini]{5} [Jünger]{3,4} [gäge d Überliferig]{7,8} [vo de Ältischte]{9,10}? [Si wäsched]{13} [nämli]{12} [iri]{16} [Händ]{14,15} [nöd]{11}, [wänn]{17} si [Broot]{18} [ässed]{19}.»",
 "MAT.15.3": "[Er]{1} [aber]{2} [hät]{3} [ine]{5} [gantwortet]{3} und [gseit]{4}: «[Werum]{6,7} [verstoossed]{10} [au]{8} [ir]{9} [gäge s Gebot]{11,12} [vo Gott]{13,14} [für]{15} [eui]{18} [Überliferig]{16,17}?",
 "MAT.15.4": "[Gott]{1,3} [hät]{4} [nämli]{2} [gseit]{4}: ‹[Ehr]{5} [de Vatter]{6,7} und{8} [d Mueter]{9,10}›, und{11}: ‹[Wer]{12} [Vatter]{14} [oder]{15} [Mueter]{16} [verfluecht]{13}, [dä söll]{18} [de Tod]{17} [stärbe]{18}.›",
 "MAT.15.5": "[Ir]{1} [aber]{2} [säged]{3}: ‹[Wer]{4,5} [zum Vatter]{7,8} [oder]{9} [zur Mueter]{10,11} [seit]{6}: [Opfergab]{12} sig, [was]{13,14} [du]{17} [vo]{15} [mir]{16} [a Hilf chöntsch übercho]{17},",
 "MAT.15.6": "[dä mues]{3} [sin]{6} [Vatter]{4,5} [nöd]{1,2} [ehre]{3}.› Und{7} [ir händ]{8} [s Wort]{9,10} [vo Gott]{11,12} [für]{13} [eui]{16} [Überliferig]{14,15} [usser Chraft gsetzt]{8}.",
 "MAT.15.7": "[Ir Heuchler]{1}! [Treffend]{2} [hät]{3} [de Jesaja]{6} [über]{4} [eu]{5} [profezeit]{3}, [wo er gseit hät]{7}:",
 "MAT.15.8": "‹[Das]{3} [Volch]{1,2} [ehrt]{7} [mich]{6} [mit de Lippe]{4,5}, [ires]{11} [Härz]{8,10} [aber]{9} [isch]{13} [wiit]{12} [ewägg]{13} [vo]{14} [mir]{15};",
 "MAT.15.9": "[vergäbe]{1} [aber]{2} [verehred si]{3} [mich]{4}; [si lehred]{5} [als Lehre]{6} [Gebot]{7} [vo Mänsche]{8}.›»",
 "MAT.15.10": "Und{1} [er hät]{2} [d Mängi]{3,4} [zu sich grüeft]{2} und [zu ine]{6} [gseit]{5}: «[Losed]{7} und{8} [verstönd]{9}!",
 "MAT.15.11": "[Nöd]{1} [was]{2} [is]{4,5} [Muul]{6} [ine gaat]{3}, [macht]{7} [de Mänsch]{8,9} [unrein]{7}, [sondern]{10} [was]{11} [us]{13} [em Muul]{14,15} [usechunnt]{12}, [das]{16} [macht]{17} [de Mänsch]{18,19} [unrein]{17}.»",
 "MAT.15.12": "[Dänn]{1} [sind]{2} [d Jünger]{3,4} [choo]{2} und [säged]{5} [zu ihm]{6}: «[Weisch]{7}, [dass]{8} [d Pharisäer]{9,10} [Aastoss gnoo händ]{14}, [wo si]{11} [das Wort]{12,13} [ghört händ]{11}?»",
 "MAT.15.13": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: «[Jedi]{5} [Pflanze]{6}, [wo]{7} [min]{12} [himmlisch]{13,14} [Vatter]{10,11} [nöd]{8} [pflanzt hät]{9}, [wird usgrisse wärde]{15}.",
 "MAT.15.14": "[Lönd]{1} [si]{2}! [Si sind]{4} [Blindi]{3}, [Füerer]{5} [vo Blinde]{6}. [Wänn]{10} [aber]{8} [en Blinde]{7} [en Blinde]{9} [füert]{11}, [wärded]{15} [beidi]{12} [i]{13} [e Grueb]{14} [gheie]{15}.»",
 "MAT.15.15": "[De Petrus]{3,4} [aber]{2} [hät gantwortet]{1} und [zu ihm]{6} [gseit]{5}: «[Erklär]{7} [üs]{8} [das]{11} [Gliichnis]{9,10}!»",
 "MAT.15.16": "[Er]{1} [aber]{2} [hät gseit]{3}: «[Sind]{8} [au]{5} [ir]{6} [immer no]{4} [unverständig]{7}?",
 "MAT.15.17": "[Begriifed ir]{2} [nöd]{1}, [dass]{3} [alles]{4}, [wo]{5} [is]{7,8} [Muul]{9} [ine gaat]{6}, [in]{10} [de Buuch]{11,12} [gaat]{13} und{14} [in]{15} de [Abtritt]{16} [usgschide wird]{17}?",
 "MAT.15.18": "[Was]{1} [aber]{2} [us]{4} [em Muul]{5,6} [usechunnt]{3}, [chunnt]{10} [us]{7} [em Härz]{8,9} [use]{10}, [und das]{11} [macht]{12} [de Mänsch]{13,14} [unrein]{12}.",
 "MAT.15.19": "[Us]{1} [em Härz]{3,4} [chömed]{5} [nämli]{2} [böösi]{7} [Gedanke]{6} [use]{5}: [Mord]{8}, [Ehebrüch]{9}, [Unzucht]{10}, [Diebstähl]{11}, [falschi Zügnis]{12}, [Läschterige]{13}.",
 "MAT.15.20": "[Das]{1} [isch es]{2}, [was]{3} [de Mänsch]{5,6} [unrein macht]{4}; [aber]{8} [mit ungwäschne]{9} [Händ]{10} [ässe]{7,11} [macht]{13} [de Mänsch]{14,15} [nöd]{12} [unrein]{13}.»",
 "MAT.15.21": "Und{1} [de Jesus]{4,5} [isch]{2} [vo dört]{3} [furtgange]{2} und [hät sich]{6} [i]{7} [d Gäged]{8,9} [vo Tyros]{10} und{11} [Sidon]{12} [zruggzoge]{6}.",
 "MAT.15.22": "Und{1} [lueg]{2}, [e kanaanäischi]{4} [Frau]{3} [isch]{9} [us]{5} [dem]{6} [Gebiet]{7} [dört]{8} [choo]{9} und [hät gschroue]{10}: «[Häb Erbarme]{12} [mit mir]{13}, [Herr]{14}, [Sohn]{15} [vom David]{16}! [Mini]{19} [Tochter]{17,18} [isch]{21} [schlimm]{20} [bsässe]{21}.» ~11(λέγουσα «sägend» leitet di diräkt Red ii)",
 "MAT.15.23": "[Er]{1} [aber]{2} [hät]{4} [ere]{5} [kei]{3} [Wort]{6} [gantwortet]{4}. Und{7} [sini]{11} [Jünger]{9,10} [sind choo]{8}, [händ]{12} [en]{13} [bätte]{12} und [gseit]{14}: «[Schick]{15} [si]{16} [furt]{15}, [dänn]{17} [si schreit]{18} [hinder]{19} [üs]{20} [här]{19}!»",
 "MAT.15.24": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: «[Ich bi]{6} [nu]{5,7,8} [zu]{9} [de]{10} [verlorne]{12,13} [Schaf]{11} [vom Huus]{14} [Israel]{15} [gschickt worde]{6}.»",
 "MAT.15.25": "[Si]{1} [aber]{2} [isch choo]{3}, [isch vor]{4} [ihm]{5} [nidergfalle]{4} und [hät gseit]{6}: «[Herr]{7}, [hilf]{8} [mir]{9}!»",
 "MAT.15.26": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: «[Es isch]{6} [nöd]{5} [rächt]{7}, [s Broot]{9,10} [vo de Chind]{11,12} [z nää]{8} und{13} [de Hündli]{15,16} [anezrüere]{14}.»",
 "MAT.15.27": "[Si]{1} [aber]{2} [hät gseit]{3}: «[Ja]{4}, [Herr]{5}; [dänn]{7} [au]{6} [d Hündli]{8,9} [ässed]{10} [vo]{11} [de Brösmeli]{12,13}, [wo]{14} [vom]{16,17} [Tisch]{18} [vo irne]{21} [Herre]{19,20} [abegheied]{15}.»",
 "MAT.15.28": "[Dänn]{1} [hät]{2} [de Jesus]{3,4} [gantwortet]{2} und [zu ire]{6} [gseit]{5}: «[Frau]{8}, [din]{10} [Glaube]{11,12} isch [gross]{9}! [Dir]{14} [söll gscheh]{13}, [wie]{15} [du wottsch]{16}.» Und{17} [iri]{21} [Tochter]{19,20} [isch]{18} [vo]{22} [dere]{25} [Stund]{23,24} [aa]{22} [gheilt gsii]{18}. ~7(Ὦ «o» verstärkt d Aared; mit em Usruef widergää)",
 "MAT.15.29": "Und{1} [de Jesus]{4,5} [isch]{2} [vo dört]{3} [wiitergange]{2} und [isch]{6} [an]{7} [de See]{8,9} [vo Galiläa]{10,11} [choo]{6}; und{12} [er isch]{13} [uf]{14} [de Bärg]{15,16} [ufegstige]{13} und [isch]{17} [dört]{18} [gsässe]{17}.",
 "MAT.15.30": "Und{1} [vil]{5} [Lüüt]{4} [sind]{2} [zu ihm]{3} [choo]{2} und [händ]{6} [Stummi]{9}, [Blindi]{10}, [Lahmi]{11}, [Verchrüppleti]{12} und{13} [vil]{15} [anderi]{14} [bi]{7} [sich]{8} [gha]{6}; und{16} [si händ]{17} [si]{18} [ihm]{22} [vor d]{19,20} [Füess]{21} [anegleit]{17}, und{23} [er hät]{24} [si]{25} [gheilt]{24},",
 "MAT.15.31": "[sodass]{1} [d Mängi]{2,3} [gstuunt hät]{4}, [wo si gseh hät]{5}, wie [Stummi]{6} [redt händ]{7}, [Verchrüppleti]{8} [gsund]{9} gsii sind und{10} [Lahmi]{11} [umegloffe sind]{12} und{13} [Blindi]{14} [gseh händ]{15}; und{16} [si händ]{17} [de Gott]{18,19} [vo Israel]{20} [globt]{17}.",
 "MAT.15.32": "[De Jesus]{1,3} [aber]{2} [hät]{4} [sini]{7} [Jünger]{5,6} [zu sich grüeft]{4} und [gseit]{8}: «[Ich ha Erbarme]{9} [mit]{10} [de Mängi]{11,12}, [dänn]{13} [si bliibed]{17} [scho]{14} [drüü]{16} [Täg]{15} [bi mir]{18} und{19} [händ]{21} [nüüt]{20,22} [z ässe]{23}. Und{24} [ich wott]{29} [si]{26} [nöd]{28} [hungrig]{27} [furtschicke]{25}, [demit]{30} si [nöd]{30} [understwägs]{32-34} [zämebräched]{31}.»",
 "MAT.15.33": "Und{1} [d Jünger]{4,5} [säged]{2} [zu ihm]{3}: «[Vo wo]{6} [söled mir]{7} [i]{8} [de Wüeschti]{9} [so vil]{11} [Broot]{10} nää, [für]{12} [e so grossi]{15} [Mängi]{14} [satt z mache]{13}?»",
 "MAT.15.34": "Und{1} [de Jesus]{4,5} [seit]{2} [zu ine]{3}: «[Wie vil]{6} [Broot]{7} [händ ir]{8}?» [Si]{9} [aber]{10} [händ gseit]{11}: «[Sibe]{12}, und{13} [es paar]{14} [Fischli]{15}.»",
 "MAT.15.35": "Und{1} [er hät]{2} [de Mängi]{3,4} [befole]{2}, [sich]{5} [uf]{6} [de Bode]{7,8} [z setze]{5},",
 "MAT.15.36": "[hät]{1} [di sibe]{2,3} [Broot]{4} und{5} [d Fisch]{6,7} [gnoo]{1} und{8} [hät dankt]{9}, si [broche]{10} und{11} si [de Jünger]{13,14} [gää]{12}, [d Jünger]{15,17} [aber]{16} [de Lüüt]{18,19}.",
 "MAT.15.37": "Und{1} [alli]{3} [händ ggässe]{2} und{4} [sind satt worde]{5}; und{6} [was]{7} [a Brocke]{9,10} [übrig bliibe isch]{8}, [händ si ufgläse]{11}: [sibe]{12} [Chörb]{13} [voll]{14}.",
 "MAT.15.38": "[Die]{1} [aber]{2}, wo [ggässe händ]{3}, [sind]{4} [viertuusig]{5} [Manne]{6} [gsii]{4}, [ohni]{7} [Fraue]{8} und{9} [Chind]{10}.",
 "MAT.15.39": "Und{1} [wo er]{2} [d Lüüt]{3,4} [furtgschickt gha hät]{2}, [isch er]{5} [is]{6,7} [Boot]{8} [gstige]{5} und{9} [isch]{10} [is]{11,12} [Gebiet]{13} [vo Magadan]{14} [choo]{10}.",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 # ------------------------------------------------------------ Kapitel 14
 ("MAT.14.1", "der Tetrarch", "literal", "ὁ τετραάρχης", "der Vierfürst", ["der Landesfürst"],
  "Herodes Antipas, Sohn von Herodes dem Grossen, herrschte von Roms Gnaden als Tetrarch («Herrscher über ein Viertel») über Galiläa und Peräa, nicht als König. In [[MAT.14.9]] nennt ihn Matthäus «der König», wie Markus durchgehend ([[MRK.6.14]]); der volkstümliche Titel ist dort beibehalten."),
 ("MAT.14.2", "Dienern", "literal", "παισὶν", None, ["Knechten", "Höflingen"],
  "παῖς heisst «Kind, Knabe» und «Diener»; hier sind die Bediensteten am Hof gemeint."),
 ("MAT.14.2", "die Kräfte", "literal", "αἱ δυνάμεις", None, ["die Wunderkräfte"],
  "Gemeint sind die Kräfte selbst, die in ihm wirken (wie [[MRK.6.14]]); dasselbe Wort bezeichnet sonst auch die Machttaten (z. B. [[MAT.13.58]])."),
 ("MAT.14.3", "Philippus", "literal", "Φιλίππου", None, None,
  "Nach dem jüdischen Geschichtsschreiber Josephus war Herodias vorher mit einem anderen Halbbruder des Antipas verheiratet, der dort nicht Philippus heisst. Ob die Evangelien ungenau sind oder jener Mann auch Philippus hiess, ist umstritten (vgl. [[MRK.6.17]])."),
 ("MAT.14.5", "fürchtete er die Menge", "literal", "ἐφοβήθη τὸν ὄχλον", None, None,
  "Bei Matthäus will Herodes selbst Johannes töten und fürchtet die Menge, die Johannes für einen Propheten hält; bei Markus will Herodias ihn töten, und Herodes fürchtet Johannes ([[MRK.6.19]]–[[MRK.6.20]]). Die Übersetzung folgt jeweils dem eigenen Wortlaut."),
 ("MAT.14.6", "der Geburtstag", "interpretive", "γενεσίοις", "Geburtstagsfeiern", ["die Geburtstagsfeier", "der Jahrestag seines Herrschaftsantritts"],
  "γενέσια (Plural) bezeichnet meist die Feier des Geburtstags; seltener wird es als Gedenktag des Regierungsantritts gedeutet. Zur Lesart Γενεσίων ἀγομένων («als der Geburtstag begangen wurde», RP) siehe den Apparat; sie ändert die Übersetzung kaum."),
 ("MAT.14.6", "vor allen", "adapted", "ἐν τῷ μέσῳ", "in der Mitte", ["mitten unter den Gästen"],
  "Gemeint ist der Tanz vor den versammelten Gästen; «vor allen» sagt das ohne Ergänzung."),
 ("MAT.14.8", "angestiftet", "interpretive", "προβιβασθεῖσα", "vorangebracht", ["angeleitet", "gedrängt"],
  "προβιβάζω heisst «vorwärtsbringen», übertragen «anleiten, antreiben». Der Text lässt offen, wie weit die Tochter selbst beteiligt ist; die Initiative liegt bei der Mutter."),
 ("MAT.14.8", "einer Schale", "literal", "πίνακι", None, ["einer Platte", "einem Teller"],
  "πίναξ ist eine flache Schüssel oder Platte; Wiedergabe wie [[MRK.6.25]]."),
 ("MAT.14.9", "der König", "literal", "ὁ βασιλεὺς", None, ["der Herrscher"],
  "Volkstümlicher Titel für Herodes Antipas; siehe [[MAT.14.1]]."),
 ("MAT.14.9", "wegen der Eide und der Gäste", "interpretive", "διὰ τοὺς ὅρκους καὶ τοὺς συνανακειμένους", "wegen der Eide und der mit (ihm) zu Tisch Liegenden", None,
  "Die Wendung kann zur Betrübnis gehören («betrübt wegen der Eide») oder zum Befehl; die Übersetzung bezieht sie auf den Befehl, wie es der Satzbau nahelegt. RP macht das mit διὰ δέ eindeutig (siehe Alternative). Plural «Eide»: wohl der eine, feierlich bekräftigte Schwur."),
 ("MAT.14.10", "liess Johannes im Gefängnis enthaupten", "adapted", "πέμψας ἀπεκεφάλισεν τὸν Ἰωάννην", "er schickte und enthauptete Johannes", None,
  "Herodes vollzieht die Hinrichtung nicht selbst; «schickte und enthauptete» meint, dass er sie durch einen Gesandten vollziehen lässt."),
 ("MAT.14.12", "den Leichnam", "literal", "τὸ πτῶμα", None, ["den Toten"],
  "πτῶμα (wörtlich «das Gefallene») ist das harte Wort für den toten Körper; RP liest σῶμα «Leib» (siehe Alternative)."),
 ("MAT.14.13", "zog er sich von dort in einem Boot an einen einsamen Ort zurück", "literal", "ἀνεχώρησεν ἐκεῖθεν ἐν πλοίῳ", None, ["entwich er", "ging er weg"],
  "Grundentscheid für diesen Bereich: ἀναχωρέω durchgehend «sich zurückziehen» (Mundart «sich zruggzieh»). Matthäus braucht das Wort (nach MACULA-Lemma 10-mal) oft für ein Ausweichen vor Bedrohung: [[MAT.2.14]], [[MAT.4.12]], [[MAT.12.15]], hier nach der Nachricht vom Tod des Täufers, ebenso [[MAT.15.21]]."),
 ("MAT.14.13", "einsamen", "interpretive", "ἔρημον", "öden", ["abgelegenen", "unbewohnten"],
  "ἔρημος ist unbewohntes Land, nicht unbedingt Wüste; Wiedergabe wie [[MRK.6.31]]."),
 ("MAT.14.13", "die Leute", "adapted", "οἱ ὄχλοι", "die Volksmengen", ["die Scharen"],
  "Grundentscheid für diesen Bereich: ὄχλος in der Einzahl «Menge», in der bei Matthäus häufigen Mehrzahl οἱ ὄχλοι «die Leute» (Mundart «d Mängi» bzw. «d Lüüt»), weil «die Mengen» im Deutschen nicht trägt. Ebenso [[MAT.14.15]], [[MAT.14.19]], [[MAT.14.22]]–[[MAT.14.23]], [[MAT.15.30]], [[MAT.15.36]], [[MAT.15.39]]."),
 ("MAT.14.14", "er hatte Erbarmen", "interpretive", "ἐσπλαγχνίσθη", "es bewegte ihn im Innersten", ["es jammerte ihn", "er hatte Mitleid"],
  "σπλάγχνα sind die Eingeweide als Sitz der Gefühle. Einheitlich «Erbarmen haben» wie [[MRK.6.34]]; ebenso [[MAT.15.32]]. Das Verb steht bei Matthäus nach MACULA-Lemma 5-mal."),
 ("MAT.14.19", "sprach den Segen", "adapted", "εὐλόγησεν", "segnete", ["dankte"],
  "Gemeint ist der jüdische Lobspruch über dem Brot, der Gott preist. In [[MAT.15.36]] steht εὐχαριστέω («danken»); die Übersetzung hält den Unterschied fest («Dankgebet»). Vgl. [[MAT.26.26]]–[[MAT.26.27]], wo beide Verben nebeneinander stehen."),
 ("MAT.14.20", "Körbe", "literal", "κοφίνους", None, ["Handkörbe"],
  "κόφινος (hier) und σπυρίς ([[MAT.15.37]]) sind zwei verschiedene Korbwörter; [[MAT.16.9]]–[[MAT.16.10]] hält die Unterscheidung fest. Beide sind wie bei Markus mit «Körbe» wiedergegeben."),
 ("MAT.14.21", "ohne Frauen und Kinder", "literal", "χωρὶς γυναικῶν καὶ παιδίων", None, ["Frauen und Kinder nicht mitgezählt"],
  "Matthäus ergänzt gegenüber [[MRK.6.44]] ausdrücklich, dass Frauen und Kinder nicht mitgezählt sind; ebenso [[MAT.15.38]]."),
 ("MAT.14.22", "nötigte er", "literal", "ἠνάγκασεν", None, ["drängte er", "zwang er"],
  "Dasselbe Verb wie [[MRK.6.45]]; warum Jesus die Jünger drängt, sagt der Text nicht."),
 ("MAT.14.24", "Stadien", "literal", "σταδίους", None, ["Stadion (rund 185 m)"],
  "Ein Stadion misst etwa 185 Meter; «viele Stadien» heisst also wohl mehrere Kilometer. Zur Lesart «mitten auf dem See» siehe die Alternative."),
 ("MAT.14.24", "bedrängt", "adapted", "βασανιζόμενον", "gequält", ["geplagt", "hin und her geworfen"],
  "βασανίζω heisst «prüfen, quälen»; von einem Boot gesagt: von den Wellen hart bedrängt."),
 ("MAT.14.25", "In der vierten", "literal", "τετάρτῃ", None, ["gegen Morgen"],
  "Nach römischer Einteilung die letzte von vier Nachtwachen, etwa von 3 bis 6 Uhr (vgl. [[MRK.6.48]])."),
 ("MAT.14.26", "ein Gespenst", "literal", "Φάντασμά", None, ["eine Erscheinung", "ein Geist"], None),
 ("MAT.14.27", "Seid getrost", "traditional", "Θαρσεῖτε", None, ["Habt Mut", "Nur Mut"],
  "θαρσέω «guten Mutes sein»; ebenso [[MAT.9.2]], [[MAT.9.22]]."),
 ("MAT.14.27", "ich bin es", "interpretive", "ἐγώ εἰμι", "ich bin", None,
  "Erkennungsformel wie [[MRK.6.50]]. Zugleich kann ein Anklang an die Selbstvorstellung Gottes ([[EXO.3.14]]; [[ISA.43.10]] in der Septuaginta) mitgehört werden, zumal Jesus auf dem Wasser geht (vgl. [[JOB.9.8]])."),
 ("MAT.14.28", "Herr", "interpretive", "Κύριε", None, ["Herr (als höfliche Anrede)"],
  "κύριε ist die übliche höfliche Anrede, kann aber im Erzählzusammenhang mehr anklingen lassen. Bei Matthäus reden Jünger und Hilfesuchende Jesus häufig so an ([[MAT.8.25]], [[MAT.14.30]], [[MAT.15.22]], [[MAT.15.25]], [[MAT.15.27]]); einheitlich «Herr»."),
 ("MAT.14.30", "rette", "literal", "σῶσόν", None, ["hilf"],
  "σῴζω «retten» wie im Notruf der Jünger [[MAT.8.25]]."),
 ("MAT.14.31", "Du Kleingläubiger", "literal", "Ὀλιγόπιστε", "Du Wenig-Glaubender", ["Du Kleinmütiger", "Du mit deinem kleinen Glauben"],
  "Grundentscheid: ὀλιγόπιστος durchgehend «kleingläubig» (Mundart «chliigläubig»), ὀλιγοπιστία «Kleinglaube» ([[MAT.17.20]]). Das Wort steht bei Matthäus nach MACULA-Lemma 4-mal ([[MAT.6.30]], [[MAT.8.26]], hier, [[MAT.16.8]]) und meint nicht Unglauben, sondern Vertrauen, das in der Bedrängnis nicht ausreicht. Gegenbild ist der «grosse Glaube» der kanaanäischen Frau ([[MAT.15.28]])."),
 ("MAT.14.31", "hast du gezweifelt", "literal", "ἐδίστασας", None, ["hast du geschwankt"],
  "διστάζω («zwiespältig sein, schwanken») steht im Neuen Testament nur hier und in [[MAT.28.17]]."),
 ("MAT.14.33", "fielen vor ihm nieder", "interpretive", "προσεκύνησαν", None, ["beteten ihn an", "huldigten ihm"],
  "Grundentscheid für diesen Bereich: προσκυνέω «niederfallen vor» (Mundart «nidergfalle vor»). Das Wort bezeichnet die Gebärde des Niederwerfens vor einem König oder vor Gott; ob Anbetung gemeint ist, ergibt der Zusammenhang. Matthäus braucht es häufig (nach MACULA-Lemma 13-mal, z. B. [[MAT.2.11]], [[MAT.8.2]], [[MAT.15.25]], [[MAT.28.9]], [[MAT.28.17]]); die einheitliche Wiedergabe hält die Stellen vergleichbar."),
 ("MAT.14.33", "du bist Gottes Sohn", "interpretive", "θεοῦ υἱὸς εἶ", None, ["du bist der Sohn Gottes", "du bist ein Sohn Gottes"],
  "θεοῦ υἱός steht ohne Artikel und vor dem Verb, wie oft bei einem vorangestellten Prädikatsnomen; das schliesst die Bedeutung «der Sohn Gottes» nicht aus (vgl. [[MAT.16.16]] mit Artikel, [[MAT.27.54]] ohne). Die Übersetzung behält die artikellose Form. Anders als bei Markus, wo die Jünger fassungslos bleiben ([[MRK.6.51]]–[[MRK.6.52]]), endet die Szene bei Matthäus mit einem Bekenntnis."),
 ("MAT.14.36", "den Saum", "interpretive", "κρασπέδου", None, ["die Quaste"],
  "κράσπεδον kann den Saum oder die Quasten am Gewand meinen, die nach [[NUM.15.38]] an den Zipfeln zu tragen waren; vgl. [[MAT.9.20]]."),
 ("MAT.14.36", "wurden gerettet", "interpretive", "διεσώθησαν", None, ["wurden geheilt", "wurden ganz gesund"],
  "διασῴζω heisst «durch und durch retten, unversehrt durchbringen»; hier die Heilung. Die Übersetzung behält das Wort «retten» (vgl. [[MRK.6.56]], σῴζω), weil es bei Matthäus Heilung und Rettung verbindet (vgl. [[MAT.9.21]]–[[MAT.9.22]])."),
 # ------------------------------------------------------------ Kapitel 15
 ("MAT.15.1", "Da", "literal", "Τότε", "Dann", None,
  "τότε ist das typische Verbindungswort des Matthäus (einheitlich «da», Mundart «dänn»). Die Gegenwartsform προσέρχονται («kommen») ist als erzählendes Präsens beibehalten."),
 ("MAT.15.1", "Schriftgelehrte", "traditional", "γραμματεῖς", "Schreiber", ["Gesetzeslehrer"],
  "Kundige der Schrift und ihrer Auslegung; einheitliche Wiedergabe für das Matthäusevangelium."),
 ("MAT.15.2", "die Überlieferung der Ältesten", "literal", "τὴν παράδοσιν τῶν πρεσβυτέρων", None, ["die Satzungen der Alten"],
  "Gemeint ist die mündlich weitergegebene Auslegung der Tora durch frühere Lehrer, die die Pharisäer hochhielten. «Älteste» heisst hier frühere Generationen von Lehrern, nicht die Ratsmitglieder."),
 ("MAT.15.2", "sie waschen ihre Hände nicht", "literal", "οὐ γὰρ νίπτονται τὰς χεῖρας αὐτῶν", None, None,
  "Es geht um rituelle Reinheit vor der Mahlzeit, nicht um Hygiene. Anders als [[MRK.7.3]]–[[MRK.7.4]] erklärt Matthäus den Brauch nicht. «Brot essen» heisst «eine Mahlzeit halten»."),
 ("MAT.15.4", "verflucht", "interpretive", "κακολογῶν", "schlecht redet über", ["schmäht", "beschimpft"],
  "Zitate aus [[EXO.20.12]] und [[EXO.21.17]] (vgl. [[DEU.5.16]]) nach der griechischen Übersetzung. Das hebräische Verb in [[EXO.21.17]] meint «verfluchen, verächtlich machen»; Wiedergabe wie [[MRK.7.10]]."),
 ("MAT.15.4", "soll des Todes sterben", "literal", "θανάτῳ τελευτάτω", "soll mit dem Tod enden", ["muss getötet werden"],
  "Wiedergabe der hebräischen Rechtsformel (vgl. [[LEV.20.9]]); sie bezeichnet die Todesstrafe. Wie [[MRK.7.10]]."),
 ("MAT.15.5", "Opfergabe", "interpretive", "Δῶρον", "Gabe", ["Weihgabe", "Geschenk (an Gott)"],
  "δῶρον allein heisst «Gabe»; im Zusammenhang die Gott geweihte Gabe. Gemeint ist ein Gelübde, durch das Besitz dem Tempel geweiht und dadurch den Eltern entzogen wird. Matthäus lässt das hebräische Wort «Korban» weg, das [[MRK.7.11]] nennt und übersetzt."),
 ("MAT.15.6", "der braucht seinen Vater nicht zu ehren", "interpretive", "οὐ μὴ τιμήσει τὸν πατέρα αὐτοῦ", "der wird seinen Vater gewiss nicht ehren", ["der soll seinen Vater nicht mehr ehren"],
  "οὐ μή mit Futur ist eine starke Verneinung. Die Übersetzung liest den Satz als Schluss der Lehre, die Jesus den Gegnern vorhält (darum innerhalb der Anführungszeichen); möglich ist auch, dass Jesus selbst die Folge feststellt: «der wird seinen Vater dann gewiss nicht ehren». Zum Zusatz «oder seine Mutter» siehe die Alternative."),
 ("MAT.15.6", "ausser Kraft gesetzt", "literal", "ἠκυρώσατε", "ungültig gemacht", ["aufgehoben"],
  "Rechtssprache: etwas für ungültig erklären; wie [[MRK.7.13]]. Zur Lesart «das Gebot» bzw. «das Gesetz» statt «das Wort» siehe die Alternative."),
 ("MAT.15.7", "Heuchler", "traditional", "ὑποκριταί", "Schauspieler", ["Scheinheilige"],
  "ὑποκριτής ist ursprünglich der Bühnendarsteller; im Neuen Testament jemand, dessen Auftreten und Inneres auseinanderfallen. Einheitliche Wiedergabe für das Matthäusevangelium; das Wort beschreibt hier die angesprochenen Pharisäer und Schriftgelehrten, kein Urteil über eine Gruppe als Ganzes."),
 ("MAT.15.7", "geweissagt", "literal", "ἐπροφήτευσεν", None, ["prophezeit"],
  "Die Weissagung ist auf die Gegenwart bezogen: «über euch»."),
 ("MAT.15.8", "Dieses Volk ehrt mich mit den Lippen", "literal", "Ὁ λαὸς οὗτος τοῖς χείλεσίν με τιμᾷ", None, None,
  "Zitat aus [[ISA.29.13]] in einer Form, die der Septuaginta nahesteht; [[MRK.7.6]]–[[MRK.7.7]] hat denselben Wortlaut. Zur längeren Form «naht sich mir mit seinem Mund» siehe die Alternative."),
 ("MAT.15.11", "unrein", "interpretive", "κοινοῖ", "gemein macht", ["entweiht"],
  "κοινόω «gemein machen» bezeichnet im jüdischen Sprachgebrauch der Zeit das rituelle Verunreinigen. Wie [[MRK.7.15]]; ebenso [[MAT.15.18]] und [[MAT.15.20]]."),
 ("MAT.15.12", "Anstoss genommen haben", "interpretive", "ἐσκανδαλίσθησαν", None, ["sich geärgert haben", "zu Fall gekommen sind"],
  "Grundentscheid für diesen Bereich: σκανδαλίζω (bei Matthäus nach MACULA-Lemma 14-mal) kommt von σκάνδαλον, dem Stellholz einer Falle oder einem Stolperstein. Wo Menschen an Jesus Anstoss nehmen und sich gegen ihn stellen (hier, [[MAT.13.57]]), steht «Anstoss nehmen»; wo jemand im Glauben zu Fall kommt oder gebracht wird (z. B. [[MAT.18.6]], [[MAT.26.31]]), «zu Fall kommen / bringen». So auch die Markus-Übersetzung ([[MRK.6.3]], [[MRK.9.42]])."),
 ("MAT.15.13", "Pflanze", "literal", "φυτεία", "Pflanzung", ["Gewächs"],
  "Bild für das, was Gott gepflanzt hat (vgl. [[ISA.60.21]]; [[ISA.61.3]]). Wen Jesus damit meint, sagt der folgende Vers: die Pharisäer als blinde Führer."),
 ("MAT.15.13", "himmlischer Vater", "literal", "ὁ πατήρ μου ὁ οὐράνιος", None, None,
  "Einheitliche Wiedergabe für das Matthäusevangelium («himmlisch»; Mundart «himmlisch»)."),
 ("MAT.15.14", "Führer von Blinden", "literal", "ὁδηγοὶ τυφλῶν", None, ["blinde Blindenführer"],
  "Zur Lesart «Sie sind blinde Führer» ohne «von Blinden» siehe die Alternative; vgl. [[MAT.23.16]], [[MAT.23.24]]."),
 ("MAT.15.15", "Gleichnis", "literal", "παραβολὴν", None, ["Bildwort", "Rätselwort"],
  "παραβολή meint hier nicht eine Erzählung, sondern das bildhafte Wort von [[MAT.15.11]]."),
 ("MAT.15.17", "den Abort", "literal", "ἀφεδρῶνα", None, ["die Grube", "den Abtritt"],
  "Derbes, sachliches Wort für den Ort der Ausscheidung; wie [[MRK.7.19]]. Den Satz «So erklärte er alle Speisen für rein» aus [[MRK.7.19]] hat Matthäus nicht."),
 ("MAT.15.19", "Unzucht", "literal", "πορνεῖαι", "Unzuchtstaten", ["sexuelle Vergehen", "Hurereien"],
  "πορνεία bezeichnet unerlaubte sexuelle Beziehungen allgemein. Die Liste folgt nach «bösen Gedanken» in den Gliedern Mord, Ehebruch, Diebstahl und falsches Zeugnis der Reihenfolge der Zehn Gebote ([[EXO.20.13]]–[[EXO.20.16]])."),
 ("MAT.15.19", "falsche Zeugnisse", "literal", "ψευδομαρτυρίαι", None, ["Falschaussagen"],
  "Vgl. das Gebot [[EXO.20.16]]."),
 ("MAT.15.19", "Lästerungen", "literal", "βλασφημίαι", None, ["Verleumdungen", "Schmähungen"],
  "βλασφημία meint verletzende Rede gegen Gott oder Menschen; hier wohl vor allem gegen Menschen."),
 ("MAT.15.21", "von Tyros und Sidon", "literal", "Τύρου καὶ Σιδῶνος", None, None,
  "Phönizische Hafenstädte nördlich von Galiläa, nichtjüdisches Gebiet. Ob Jesus das Gebiet betritt oder an seine Grenze kommt, lässt der Text offen; die Frau kommt «aus jenem Gebiet heraus» ([[MAT.15.22]])."),
 ("MAT.15.22", "eine kanaanäische", "literal", "Χαναναία", None, ["eine Kanaaniterin"],
  "Markus nennt die Frau eine Griechin und Syrophönizierin ([[MRK.7.26]]). Matthäus verwendet den alten biblischen Namen für die Bewohner des Landes vor Israel und hebt damit ihre nichtjüdische Herkunft hervor."),
 ("MAT.15.22", "Hab Erbarmen", "literal", "Ἐλέησόν", None, ["Erbarme dich"],
  "Bittruf wie in den Psalmen; vgl. [[MAT.9.27]], [[MAT.20.30]]."),
 ("MAT.15.22", "Sohn Davids", "literal", "υἱὸς Δαυίδ", None, None,
  "Messianischer Titel (vgl. [[MAT.1.1]], [[MAT.9.27]], [[MAT.12.23]]); hier aus dem Mund einer Nichtjüdin. Der SBLGNT hat den Nominativ υἱός als Anrede; RP liest den Vokativ υἱέ, ohne Unterschied für die Übersetzung."),
 ("MAT.15.22", "besessen", "literal", "δαιμονίζεται", "wird von einem Dämon beherrscht", ["wird von einem Dämon geplagt"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: δαιμονίζομαι «besessen sein»."),
 ("MAT.15.23", "Schick sie fort", "interpretive", "Ἀπόλυσον αὐτήν", "Entlasse sie", ["Erfüll ihre Bitte und lass sie gehen", "Fertige sie ab"],
  "ἀπολύω heisst «entlassen, wegschicken». Ob die Jünger verlangen, dass Jesus sie abweist, oder dass er ihr hilft, um sie loszuwerden, bleibt offen; seine Antwort in [[MAT.15.24]] passt eher zur zweiten Deutung."),
 ("MAT.15.24", "zu den verlorenen Schafen des Hauses Israel", "interpretive", "εἰς τὰ πρόβατα τὰ ἀπολωλότα οἴκου Ἰσραήλ", None, ["zu den verlorenen Schafen, nämlich dem Haus Israel", "zu den Verlorenen unter dem Haus Israel"],
  "Der Genitiv kann das ganze Volk als verlorene Schafe bezeichnen oder die Verlorenen innerhalb Israels. Vgl. [[MAT.10.6]] und das Bild der verlorenen Schafe in [[JER.50.6]] und [[EZK.34.4]]–[[EZK.34.16]]."),
 ("MAT.15.24", "nur", "adapted", "Οὐκ εἰ μὴ", "nicht … ausser", None,
  "Die Verneinung mit Ausnahme («nicht gesandt ausser zu …») ist im Deutschen mit «nur» wiedergegeben."),
 ("MAT.15.25", "fiel vor ihm nieder", "interpretive", "προσεκύνει", None, ["huldigte ihm", "warf sich vor ihm nieder"],
  "Wiedergabe von προσκυνέω wie in [[MAT.14.33]]. Das Imperfekt kann die andauernde Gebärde beschreiben."),
 ("MAT.15.26", "recht", "literal", "καλὸν", "gut", ["richtig", "schön"], None),
 ("MAT.15.26", "Hündchen", "literal", "κυναρίοις", None, ["Hunden", "Haushunden"],
  "Verkleinerungsform von κύων; gemeint sind wohl Hunde im Haus, nicht streunende. Ob die Verkleinerung das harte Bild abmildert, ist umstritten. «Hund» war als Schimpfwort für Nichtjuden belegt. Wie [[MRK.7.27]]."),
 ("MAT.15.27", "denn auch", "interpretive", "καὶ γὰρ", None, ["doch auch", "aber auch"],
  "καὶ γάρ heisst «denn auch, ja auch». Die Frau stimmt dem Bild zu («Ja, Herr») und begründet daraus ihre Bitte: Auch die Hündchen bekommen etwas. Viele Übersetzungen geben die Antwort als Einwand wieder («doch»)."),
 ("MAT.15.28", "dein Glaube ist gross", "literal", "μεγάλη σου ἡ πίστις", None, None,
  "Grundentscheid: πίστις «Glaube» (Mundart «Glaube»). Der «grosse Glaube» der Nichtjüdin steht dem «Kleinglauben» des Petrus gegenüber ([[MAT.14.31]]); vgl. den Hauptmann in [[MAT.8.10]]."),
 ("MAT.15.28", "von jener Stunde an", "literal", "ἀπὸ τῆς ὥρας ἐκείνης", None, ["von diesem Augenblick an"],
  "Wendung wie in [[MAT.9.22]] und [[MAT.17.18]]; ähnlich [[MAT.8.13]]."),
 ("MAT.15.29", "den Berg", "literal", "τὸ ὄρος", None, ["das Bergland"],
  "Mit Artikel, aber ohne Namen; vgl. [[MAT.5.1]]. Welcher Berg gemeint ist, sagt der Text nicht."),
 ("MAT.15.30", "Stumme", "interpretive", "κωφούς", None, ["Taube", "Taubstumme"],
  "κωφός heisst «stumpf» und bezeichnet Taube, Stumme oder Taubstumme. Weil es in [[MAT.15.31]] heisst, dass die κωφοί reden, ist «Stumme» gewählt (vgl. [[MAT.9.32]]–[[MAT.9.33]]). Nach der CNTR-Transkription liest 03 in [[MAT.15.31]] ἀκούοντας («hören») statt λαλοῦντας."),
 ("MAT.15.30", "Verkrüppelte", "interpretive", "κυλλούς", "Verkrümmte", ["Krüppel", "an Gliedern Verstümmelte"],
  "κυλλός heisst «krumm, verkrüppelt», auch «verstümmelt» (vgl. [[MAT.18.8]]). Die Reihenfolge der vier Gruppen ist in den Ausgaben verschieden; der SBLGNT folgt hier eigener Entscheidung (Holmes), WH, Treg, NA28 und RP stellen anders um. Das ändert nur die Reihenfolge der Wörter."),
 ("MAT.15.30", "sie legten sie zu seinen Füssen hin", "adapted", "ἔρριψαν αὐτοὺς παρὰ τοὺς πόδας αὐτοῦ", "sie warfen sie zu seinen Füssen", ["sie legten sie ihm zu Füssen"],
  "ῥίπτω «werfen» beschreibt hier ein eiliges Hinlegen, kein Werfen im wörtlichen Sinn."),
 ("MAT.15.31", "sie priesen den Gott Israels", "literal", "ἐδόξασαν τὸν θεὸν Ἰσραήλ", "sie verherrlichten den Gott Israels", ["sie lobten den Gott Israels"],
  "Grundentscheid für die Erzählung bei Matthäus: δοξάζω τὸν θεόν «Gott preisen» (Mundart «Gott lobe»), wie [[MAT.9.8]]. Die Wendung «Gott Israels» lässt manche an eine nichtjüdische Menge denken (vgl. [[MRK.7.31]]: Dekapolis); der Text sagt nicht, wer die Menge ist."),
 ("MAT.15.32", "Ich habe Erbarmen", "interpretive", "Σπλαγχνίζομαι", "Es bewegt mich im Innersten", ["Es jammert mich", "Ich habe Mitleid"],
  "Einheitlich wie [[MAT.14.14]]."),
 ("MAT.15.32", "hungrig", "literal", "νήστεις", "nüchtern", ["ohne Essen"],
  "νῆστις «nüchtern, ohne gegessen zu haben»."),
 ("MAT.15.33", "der Einöde", "literal", "ἐρημίᾳ", None, ["der Wüste", "einer unbewohnten Gegend"],
  "ἐρημία ist die unbewohnte Gegend; Anklang an Israels Speisung in der Wüste ([[EXO.16.32]])."),
 ("MAT.15.36", "sprach das Dankgebet", "adapted", "εὐχαριστήσας", "dankte", ["dankte (Gott)"],
  "εὐχαριστέω «danken», hier das Tischgebet; vgl. [[MAT.14.19]] (εὐλογέω, «sprach den Segen»)."),
 ("MAT.15.37", "Körbe", "literal", "σπυρίδας", None, ["Tragkörbe"],
  "σπυρίς ist ein anderes Korbwort als κόφινος ([[MAT.14.20]]); siehe dort."),
 ("MAT.15.39", "von Magadan", "literal", "Μαγαδάν", None, None,
  "Der Ort ist sonst unbekannt. [[MRK.8.10]] nennt Dalmanuta; zur Lesart «Magdala» siehe die Alternative."),
]

DEC_GSW = [
 # ------------------------------------------------------------ Kapitel 14
 ("MAT.14.1", "de Tetrarch", "literal", "ὁ τετραάρχης", "de Vierfürscht", ["de Landesfürscht"],
  "De Herodes Antipas isch vo Roms Gnade Tetrarch («Herrscher über es Viertel») vo Galiläa und Peräa gsii, nöd König. I [[MAT.14.9]] nännt en de Matthäus «de König», wie de Markus ([[MRK.6.14]])."),
 ("MAT.14.6", "vor allne", "adapted", "ἐν τῷ μέσῳ", "i de Mitti", None,
  "Gmeint isch de Tanz vor de versammlete Gäscht."),
 ("MAT.14.8", "aagstiftet", "interpretive", "προβιβασθεῖσα", "vorwärtsbrocht", ["aagleitet", "drängt"],
  "προβιβάζω heisst «vorwärtsbringe», übertreit «aaleite, aatriibe»; de Aastoss chunnt vo de Mueter."),
 ("MAT.14.8", "Platte", "literal", "πίνακι", None, ["Schale"], "πίναξ isch e flachi Schüssle oder Platte; wie [[MRK.6.25]]."),
 ("MAT.14.10", "la chöpfe", "adapted", "πέμψας ἀπεκεφάλισεν", "gschickt und gchöpft", None,
  "De Herodes macht d Hiirichtig nöd sälber; er laat si dur en Gschickte mache."),
 ("MAT.14.12", "d Liich", "literal", "τὸ πτῶμα", None, ["de Liichnam"],
  "πτῶμα isch s harte Wort für de tot Körper; RP list σῶμα «Liib» (lueg d Alternative)."),
 ("MAT.14.13", "zruggzoge", "literal", "ἀνεχώρησεν", None, ["usgwiche"],
  "Grundentscheid für dä Bereich: ἀναχωρέω immer «sich zruggzieh». De Matthäus bruucht s Wort vil für s Uswiiche vor ere Bedroohig ([[MAT.2.14]], [[MAT.4.12]], [[MAT.12.15]], [[MAT.15.21]])."),
 ("MAT.14.13", "d Lüüt", "adapted", "οἱ ὄχλοι", "d Volksmängine", None,
  "Grundentscheid für dä Bereich: ὄχλος i de Einzahl «d Mängi», i de Mehrzahl οἱ ὄχλοι «d Lüüt»."),
 ("MAT.14.14", "Erbarme", "interpretive", "ἐσπλαγχνίσθη", "s hät en im Innerschte bewegt", ["es hät en duuret"],
  "σπλάγχνα sind d Iigweid als Sitz vo de Gfüel; wie [[MRK.6.34]] und [[MAT.15.32]]."),
 ("MAT.14.19", "de Säge gsproche", "adapted", "εὐλόγησεν", "gsägnet", ["dankt"],
  "De jüdisch Lobspruch über em Broot; i [[MAT.15.36]] staat εὐχαριστέω («danke»)."),
 ("MAT.14.20", "Chörb", "literal", "κοφίνους", None, None,
  "κόφινος (da) und σπυρίς ([[MAT.15.37]]) sind zwei verschideni Wort für Chörb ([[MAT.16.9]]–[[MAT.16.10]])."),
 ("MAT.14.24", "Stadie", "literal", "σταδίους", None, None,
  "Es Stadion isch öppe 185 Meter lang. Zur Läsart «mitten uf em See» lueg d Alternative."),
 ("MAT.14.24", "plaget worde", "adapted", "βασανιζόμενον", "gquält worde", ["hin und her gworfe worde"], None),
 ("MAT.14.27", "Nu Muet", "adapted", "Θαρσεῖτε", "Sind guete Muets", ["Händ Muet"], "Wie [[MRK.6.50]]."),
 ("MAT.14.27", "ich bi s", "interpretive", "ἐγώ εἰμι", "ich bi", None,
  "Erkännigsformle. Mitghört wärde cha en Aaklang a d Selbschtvorstellig vo Gott ([[EXO.3.14]])."),
 ("MAT.14.31", "Du Chliigläubige", "literal", "Ὀλιγόπιστε", None, ["Du mit dim chliine Glaube"],
  "Grundentscheid: ὀλιγόπιστος immer «chliigläubig» ([[MAT.6.30]], [[MAT.8.26]], [[MAT.16.8]]). Gmeint isch nöd Unglaube, sondern Vertroue, wo i de Not nöd längt; s Gägebild isch de «gross Glaube» vo de kanaanäische Frau ([[MAT.15.28]])."),
 ("MAT.14.33", "nidergfalle", "interpretive", "προσεκύνησαν", None, ["händ en aabätet", "händ ihm ghuldiget"],
  "Grundentscheid für dä Bereich: προσκυνέω «vor öpperem nidergfalle»: d Gebärde vom Sich-Niderwerfe vor eme König oder vor Gott; öb Aabätig gmeint isch, seit de Zämehang."),
 ("MAT.14.33", "du bisch de Sohn vo Gott", "interpretive", "θεοῦ υἱὸς εἶ", "du bisch Gottes Sohn", ["du bisch en Sohn vo Gott"],
  "θεοῦ υἱός staat ohni Artikel. Will d Mundart kei Genitiv bruucht, bruucht s «vo Gott» de Artikel bim «Sohn»; das schliesst d Bedüütig «de Sohn vo Gott» nöd uus (vgl. [[MAT.16.16]])."),
 ("MAT.14.36", "grettet worde", "interpretive", "διεσώθησαν", None, ["gheilt worde", "ganz gsund worde"],
  "διασῴζω heisst «ganz rette»; da d Heilig. S Wort «rette» bliibt, wil s bim Matthäus Heilig und Rettig verbindet."),
 # ------------------------------------------------------------ Kapitel 15
 ("MAT.15.1", "Dänn", "literal", "Τότε", None, None,
  "τότε isch s typisch Verbindigswort vom Matthäus (einheitlich «dänn»)."),
 ("MAT.15.1", "Schriftgelehrti", "traditional", "γραμματεῖς", "Schriiber", None,
  "Einheitlichi Widergab fürs Matthäusevangelium."),
 ("MAT.15.2", "verstoossed", "adapted", "παραβαίνουσιν", "überträted", ["übertrete"],
  "παραβαίνω «drüberuusgaa, übertrete»; i de Mundart «gäge öppis verstoosse». Gliich i [[MAT.15.3]]."),
 ("MAT.15.2", "vo de Ältischte", "literal", "τῶν πρεσβυτέρων", None, None,
  "Gmeint sind früeneri Generatione vo Lehrer, wo d Uuslegig vo de Tora mündlich wiitergää händ."),
 ("MAT.15.5", "Opfergab", "interpretive", "Δῶρον", "Gab", ["Weihgab"],
  "Es Glübd, wo Bsitz em Tämpel gweiht und so de Eltere entzoge wird. De Matthäus laat s hebräisch Wort «Korban» ewägg ([[MRK.7.11]])."),
 ("MAT.15.6", "dä mues sin Vatter nöd ehre", "interpretive", "οὐ μὴ τιμήσει τὸν πατέρα αὐτοῦ", "dä wird sin Vatter sicher nöd ehre", None,
  "Starchi Verneinig. D Übersetzig list de Satz als Schluss vo de Lehr, wo de Jesus de Gägner vorhaltet; mögli isch au, dass de Jesus sälber d Folg feschtstellt."),
 ("MAT.15.7", "Heuchler", "traditional", "ὑποκριταί", "Schauspiiler", None,
  "Einheitlichi Widergab fürs Matthäusevangelium; s Wort beschriibt di aagredte Pharisäer und Schriftgelehrte, kei Urteil über e ganzi Gruppe."),
 ("MAT.15.11", "unrein", "interpretive", "κοινοῖ", "gwöhnlich macht", None,
  "κοινόω «gwöhnlich mache» heisst jüdisch: rituell unrein mache; wie [[MRK.7.15]]."),
 ("MAT.15.12", "Aastoss gnoo händ", "interpretive", "ἐσκανδαλίσθησαν", None, ["sich gärgeret händ", "z Fall choo sind"],
  "Grundentscheid für dä Bereich: σκανδαλίζω chunnt vo σκάνδαλον, em Stellhölzli vo nere Falle. Wo Mänsche a Jesus Aastoss nämed, staat «Aastoss nää» (da, [[MAT.13.57]]); wo öpper im Glaube z Fall chunnt, «z Fall choo / bringe»."),
 ("MAT.15.14", "gheie", "adapted", "πεσοῦνται", "falle", None, "Mundart «gheie» für «falle»."),
 ("MAT.15.22", "e kanaanäischi", "literal", "Χαναναία", None, None,
  "De Markus nännt d Frau e Syrophönizierin ([[MRK.7.26]]); de Matthäus bruucht de alt biblisch Name für d Bewohner vom Land vor Israel."),
 ("MAT.15.22", "bsässe", "literal", "δαιμονίζεται", None, ["vo me Dämon plaget"],
  "Einheitlichi Widergab: δαιμονίζομαι «bsässe sii»."),
 ("MAT.15.23", "Schick si furt", "interpretive", "Ἀπόλυσον αὐτήν", None, ["Erfüll ere d Bitt und la si gaa"],
  "Öb d Jünger wänd, dass de Jesus si abwiist oder dass er ere hilft, demit si s los sind, bliibt offe."),
 ("MAT.15.24", "zu de verlorne Schaf vom Huus Israel", "interpretive", "εἰς τὰ πρόβατα τὰ ἀπολωλότα οἴκου Ἰσραήλ", None, ["zu de Verlorne im Huus Israel"],
  "Es cha s ganz Volk als verlorni Schaf meine oder d Verlorne inerhalb vo Israel; vgl. [[MAT.10.6]] und [[JER.50.6]]."),
 ("MAT.15.26", "Hündli", "literal", "κυναρίοις", None, ["Hünd"], "Verchliinerigsform: Hünd im Huus; wie [[MRK.7.27]]."),
 ("MAT.15.27", "dänn au", "interpretive", "καὶ γὰρ", None, ["aber au", "doch au"],
  "D Frau stimmt em Bild zue und begründet drus iri Bitt."),
 ("MAT.15.27", "Brösmeli", "adapted", "ψιχίων", "Bröckli", None, None),
 ("MAT.15.28", "din Glaube isch gross", "literal", "μεγάλη σου ἡ πίστις", None, None,
  "Grundentscheid: πίστις «Glaube». De gross Glaube vo de Frau staat em Chliiglaube vom Petrus gägenüber ([[MAT.14.31]])."),
 ("MAT.15.30", "Stummi", "interpretive", "κωφούς", None, ["Taubi", "Taubstummi"],
  "κωφός cha taub oder stumm heisse; will si i [[MAT.15.31]] redt, staat «Stummi»."),
 ("MAT.15.30", "Verchrüppleti", "interpretive", "κυλλούς", "Chrummi", ["Verstümmleti"],
  "D Reihefolg vo de vier Gruppe isch i de Usgabe verschide; das ändert nu d Reihefolg."),
 ("MAT.15.31", "globt", "adapted", "ἐδόξασαν", "verherrlicht", ["prise"],
  "Grundentscheid für d Erzählig bim Matthäus: δοξάζω τὸν θεόν «Gott lobe» ([[MAT.9.8]])."),
 ("MAT.15.32", "Ich ha Erbarme", "interpretive", "Σπλαγχνίζομαι", "Es bewegt mich im Innerschte", None, "Wie [[MAT.14.14]]."),
 ("MAT.15.33", "Wüeschti", "adapted", "ἐρημίᾳ", "Einödi", None, "Wie [[MRK.8.4]]."),
 ("MAT.15.36", "hät dankt", "literal", "εὐχαριστήσας", None, None, "Vgl. [[MAT.14.19]] (εὐλογέω, «de Säge gsproche»)."),
 ("MAT.15.37", "Chörb", "literal", "σπυρίδας", None, None, "Es anders Wort als κόφινος ([[MAT.14.20]])."),
 ("MAT.15.39", "Magadan", "literal", "Μαγαδάν", None, None,
  "De Ort isch susch unbekannt; [[MRK.8.10]] nännt Dalmanuta. Zur Läsart «Magdala» lueg d Alternative."),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung).
ALTS = [
 ("VAR-SBLGNTAPP-MAT-014-009-01:R2", "MAT.14.9", "Und obwohl der König betrübt war, befahl er wegen der Eide und der Gäste",
  "Und der König wurde betrübt; wegen der Eide aber und der Gäste befahl er",
  "Und obwohl de König truurig gsii isch, hät er wäge de Eid und wäge de Gäscht befole",
  "Und de König isch truurig worde; wäge de Eid aber und wäge de Gäscht hät er befole", "gering",
  "R2 macht die Betrübnis zu einem eigenen Satz; Eide und Gäste sind dann eindeutig der Grund des Befehls.",
  "R2 macht us de Truurigkeit en eigete Satz; d Eid und d Gäscht sind dänn eidüütig de Grund für de Befehl.",
  {"R1": [("λυπηθεὶς ὁ βασιλεὺς διὰ", "obwohl der König betrübt war, … wegen", "WH, Treg, NA28")],
   "R2": [("ἐλυπήθη ὁ βασιλεύς διὰ δὲ", "der König wurde betrübt; wegen aber", "RP")]},
  {"R1": [("λυπηθεὶς ὁ βασιλεὺς διὰ", "obwohl de König truurig gsii isch, … wäge", "WH, Treg, NA28")],
   "R2": [("ἐλυπήθη ὁ βασιλεύς διὰ δὲ", "de König isch truurig worde; wäge aber", "RP")]},
  ["R2 kann den Satz geglättet haben (Hauptverb statt Partizip, δέ als deutlicher Neueinsatz, vgl. [[MRK.6.26]]); umgekehrt kann R1 eine stilistische Straffung sein.",
   "Laut der automatischen Zuordnung lesen 03 und 05 R1, 01, 04 und 032 R2."],
  ["R2 cha de Satz glättet ha (Hauptverb statt Partizip, δέ als düütliche Neuaasatz, vgl. [[MRK.6.26]]); umgekehrt cha R1 e stilistischi Straffig sii.",
   "Nach de automatische Zueornig läsed 03 und 05 R1, 01, 04 und 032 R2."]),
 ("VAR-SBLGNTAPP-MAT-014-012-01:R2", "MAT.14.12", "holten den Leichnam", "holten den Leib", "händ d Liich gholt", "händ de Liib gholt", "gering",
  "σῶμα «Leib» ist das allgemeinere, weniger harte Wort.", "σῶμα «Liib» isch s allgemeinere, weniger harte Wort.",
  {"R1": [("πτῶμα", "den Leichnam", "WH, Treg, NA28")], "R2": [("σῶμα", "den Leib", "RP")]},
  {"R1": [("πτῶμα", "d Liich", "WH, Treg, NA28")], "R2": [("σῶμα", "de Liib", "RP")]},
  ["σῶμα kann das harte πτῶμα ersetzt haben, vielleicht nach dem Sprachgebrauch von [[MAT.27.58]]–[[MAT.27.59]]; πτῶμα steht auch in [[MRK.6.29]].",
   "Laut der automatischen Zuordnung lesen 01 (auch die Korrektur), 03, 04 und 05 πτῶμα, 032 σῶμα. 04, 05 und 032 haben am Versende αὐτό statt αὐτόν; das ändert die Übersetzung nicht."],
  ["σῶμα cha s harte πτῶμα ersetzt ha, vilicht nach em Sprachgebruuch vo [[MAT.27.58]]–[[MAT.27.59]]; πτῶμα staat au i [[MRK.6.29]].",
   "Nach de automatische Zueornig läsed 01 (au d Korrektur), 03, 04 und 05 πτῶμα, 032 σῶμα."]),
 ("VAR-SBLGNTAPP-MAT-014-024-01:R2", "MAT.14.24", "war schon viele Stadien vom Land entfernt", "war schon mitten auf dem See",
  "isch scho vili Stadie vom Land ewägg gsii", "isch scho mitten uf em See gsii", "mittel",
  "Statt der Entfernung vom Land nennt R2 die Lage mitten auf dem See.", "Statt de Entfernig vom Land nännt R2 d Lag mitten uf em See.",
  {"R1": [("σταδίους πολλοὺς ἀπὸ τῆς γῆς ἀπεῖχεν", "war viele Stadien vom Land entfernt", "WH, Treg, NA28")],
   "R2": [("μέσον τῆς θαλάσσης ἦν", "war mitten auf dem See", "RP")]},
  {"R1": [("σταδίους πολλοὺς ἀπὸ τῆς γῆς ἀπεῖχεν", "isch vili Stadie vom Land ewägg gsii", "WH, Treg, NA28")],
   "R2": [("μέσον τῆς θαλάσσης ἦν", "isch mitten uf em See gsii", "RP")]},
  ["R2 entspricht [[MRK.6.47]] und kann daran angeglichen sein; umgekehrt kann R1 eine nachträgliche Präzisierung sein. Die Ausgaben sind geteilt.",
   "Laut der automatischen Zuordnung liest unter den erfassten Handschriften nur 03 R1; 01, 04, 032 (auch die Korrektur) und 05 lesen R2, 05 in der Form ἦν εἰς μέσον τῆς θαλάσσης."],
  ["R2 entspricht [[MRK.6.47]] und cha dra aaglichen sii; umgekehrt cha R1 e spööteri Präzisierig sii. D Usgabe sind teilt.",
   "Nach de automatische Zueornig list under de erfasste Handschrifte nu 03 R1; 01, 04, 032 und 05 läsed R2."]),
 ("VAR-SBLGNTAPP-MAT-014-025-01:R2", "MAT.14.25", "kam er zu ihnen", "ging er hin zu ihnen", "isch er zu ine choo", "isch er zu ine anegange", "gering",
  "ἀπῆλθεν betont den Weg von Jesus aus («ging hin»).", "ἀπῆλθεν betont de Wäg vom Jesus uus («isch anegange»).",
  {"R1": [("ἦλθεν", "kam", "WH, Treg, NA28")], "R2": [("ἀπῆλθεν", "ging hin", "NIV, RP")]},
  {"R1": [("ἦλθεν", "isch choo", "WH, Treg, NA28")], "R2": [("ἀπῆλθεν", "isch anegange", "NIV, RP")]},
  ["Die Vorsilbe ἀπ- kann stilistisch hinzugefügt oder als überflüssig weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ἦλθεν, 04, 032 und 05 ἀπῆλθεν (05 ohne πρὸς αὐτούς)."],
  ["D Vorsilbe ἀπ- cha stilistisch dezuecho oder als überflüssig ewägglaa worde sii.",
   "Nach de automatische Zueornig läsed 01 und 03 ἦλθεν, 04, 032 und 05 ἀπῆλθεν."]),
 ("VAR-SBLGNTAPP-MAT-014-029-02:R2", "MAT.14.29", "und kam zu Jesus", "um zu Jesus zu kommen", "und isch zum Jesus choo", "für zum Jesus z choo", "mittel",
  "Nach R2 ging Petrus auf dem Wasser, um zu Jesus zu kommen; ob er ihn erreichte, bleibt offen.",
  "Nach R2 isch de Petrus uf em Wasser gloffe, für zum Jesus z choo; öb er en erreicht hät, bliibt offe.",
  {"R1": [("καὶ ἦλθεν", "und kam", "WH, NA28")], "R2": [("ἐλθεῖν", "um zu kommen", "Treg, RP")]},
  {"R1": [("καὶ ἦλθεν", "und isch choo", "WH, NA28")], "R2": [("ἐλθεῖν", "für z choo", "Treg, RP")]},
  ["R2 vermeidet die Spannung, dass Petrus zu Jesus kommt und erst danach zu sinken beginnt; R1 gilt deshalb manchen als die schwierigere Lesart. Umgekehrt kann καὶ ἦλθεν aus dem Infinitiv entstanden sein.",
   "Laut der automatischen Zuordnung lesen 03 und 04 R1, 032 und 05 R2. 01 hat beides, ἐλθεῖν· ἦλθεν οὖν («zu kommen; er kam also»), und ist von der Zuordnung bei R2 geführt."],
  ["R2 vermiidet d Spannig, dass de Petrus zum Jesus chunnt und erscht dänn aafangt versinke; drum gilt R1 für mänggi als di schwiriger Läsart. Umgekehrt cha καὶ ἦλθεν us em Infinitiv entstande sii.",
   "Nach de automatische Zueornig läsed 03 und 04 R1, 032 und 05 R2. 01 hät beides (ἐλθεῖν· ἦλθεν οὖν) und isch bi R2 gfüert."]),
 ("VAR-SBLGNTAPP-MAT-014-030-01:R2", "MAT.14.30", "den starken Wind", "den Wind", "de starch Wind", "de Wind", "gering",
  "Ohne «stark» bleibt nur der Blick auf den Wind.", "Ohni «starch» bliibt nu de Blick uf de Wind.",
  {"R1": [("ἰσχυρὸν", "stark", "Treg, RP, NA28")], "R2": [("–", "(fehlt)", "WH, NIV")]},
  {"R1": [("ἰσχυρὸν", "starch", "Treg, RP, NA28")], "R2": [("–", "(fehlt)", "WH, NIV")]},
  ["ἰσχυρόν kann als Verdeutlichung hinzugekommen oder versehentlich ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und die Erstschrift von 03 ohne ἰσχυρόν; eine Korrektur in 03 sowie 04, 05 und 032 haben es, 032 dazu σφόδρα («sehr»)."],
  ["ἰσχυρόν cha als Verdüütlichung dezuecho oder us Versehe usgfalle sii.",
   "Nach de automatische Zueornig läsed 01 und d Erschtschrift vo 03 ohni ἰσχυρόν; e Korrektur i 03 und 04, 05 und 032 händ s."]),
 ("VAR-SBLGNTAPP-MAT-014-033-01:R2", "MAT.14.33", "Die aber im Boot waren, fielen vor ihm nieder",
  "Die aber im Boot waren, kamen und fielen vor ihm nieder",
  "Die aber, wo im Boot gsii sind, sind vor ihm nidergfalle", "Die aber, wo im Boot gsii sind, sind choo und sind vor ihm nidergfalle", "gering",
  "Der Zusatz malt die Szene aus: Die Jünger kommen zu Jesus und fallen vor ihm nieder.",
  "De Zuesatz malt d Szene uus: D Jünger chömed zum Jesus und falled vor ihm nider.",
  {"R1": [("πλοίῳ", "im Boot", "WH, NA28")], "R2": [("πλοίῳ ἐλθόντες", "im Boot kamen und", "Treg, RP")]},
  {"R1": [("πλοίῳ", "im Boot", "WH, NA28")], "R2": [("πλοίῳ ἐλθόντες", "im Boot sind choo und", "Treg, RP")]},
  ["ἐλθόντες kann als erzählerische Ausmalung hinzugefügt oder als überflüssig weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 ohne Zusatz, 032 und 05 mit ihm."],
  ["ἐλθόντες cha als erzählerischi Usmalig dezuecho oder als überflüssig ewägglaa worde sii.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 ohni Zuesatz, 032 und 05 mit."]),
 ("VAR-SBLGNTAPP-MAT-015-004-01:R2", "MAT.15.4", "Denn Gott hat gesagt", "Denn Gott hat geboten", "Gott hät nämli gseit", "Gott hät nämli gebote", "gering",
  "«Geboten» betont den Gebotscharakter.", "«Gebote» betont, dass es es Gebot isch.",
  {"R1": [("εἶπεν", "hat gesagt", "WH, Treg, NA28")], "R2": [("ἐνετείλατο λέγων", "hat geboten (und gesagt)", "RP")]},
  {"R1": [("εἶπεν", "hät gseit", "WH, Treg, NA28")], "R2": [("ἐνετείλατο λέγων", "hät gebote", "RP")]},
  ["ἐνετείλατο passt zu «das Gebot Gottes» in [[MAT.15.3]] und kann verdeutlichend eingesetzt sein; εἶπεν kann umgekehrt eine Vereinfachung sein.",
   "Laut der automatischen Zuordnung lesen 03 und 05 εἶπεν, 01, 04 und 032 ἐνετείλατο λέγων."],
  ["ἐνετείλατο passt zu «s Gebot vo Gott» i [[MAT.15.3]] und cha verdüütlichend iigsetzt sii; εἶπεν cha umgekehrt e Vereifachig sii.",
   "Nach de automatische Zueornig läsed 03 und 05 εἶπεν, 01, 04 und 032 ἐνετείλατο λέγων."]),
 ("VAR-SBLGNTAPP-MAT-015-006-03:R2", "MAT.15.6", "der braucht seinen Vater nicht zu ehren", "der braucht seinen Vater oder seine Mutter nicht zu ehren",
  "dä mues sin Vatter nöd ehre", "dä mues sin Vatter oder sini Mueter nöd ehre", "gering",
  "Der Zusatz nennt auch die Mutter.", "De Zuesatz nännt au d Mueter.",
  {"R1": [("αὐτοῦ", "seinen (Vater)", "WH, NA28")], "R2": [("αὐτοῦ ἢ τὴν μητέρα αὐτοῦ", "seinen (Vater) oder seine Mutter", "Treg, RP")]},
  {"R1": [("αὐτοῦ", "sin (Vatter)", "WH, NA28")], "R2": [("αὐτοῦ ἢ τὴν μητέρα αὐτοῦ", "sin (Vatter) oder sini Mueter", "Treg, RP")]},
  ["Der Zusatz gleicht an das Gebot ([[MAT.15.4]]) und an [[MAT.15.5]] («zum Vater oder zur Mutter») an; die kürzere Lesart kann ihn auch durch Überspringen verloren haben (zweimal αὐτοῦ).",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne Zusatz, 04 und 032 mit ihm."],
  ["De Zuesatz glicht a s Gebot ([[MAT.15.4]]) und a [[MAT.15.5]] aa; di chürzer Läsart cha en au dur Überspringe verlore ha (zweimal αὐτοῦ).",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni Zuesatz, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-015-006-04:R2", "MAT.15.6", "das Wort Gottes", "das Gebot Gottes", "s Wort vo Gott", "s Gebot vo Gott", "gering",
  "«Gebot» statt «Wort» nimmt [[MAT.15.3]] auf.", "«Gebot» statt «Wort» nimmt [[MAT.15.3]] uf.",
  {"R1": [("τὸν λόγον", "das Wort", "WH, Treg, NA28")], "R2": [("τὴν ἐντολὴν", "das Gebot", "RP")]},
  {"R1": [("τὸν λόγον", "s Wort", "WH, Treg, NA28")], "R2": [("τὴν ἐντολὴν", "s Gebot", "RP")]},
  ["ἐντολή gleicht an [[MAT.15.3]] an, νόμος («Gesetz») an den geläufigen Ausdruck «Gesetz Gottes»; λόγος entspricht [[MRK.7.13]]. Welche Form die älteste ist, ist umstritten.",
   "Laut der automatischen Zuordnung lesen 03 und 05 τὸν λόγον, 032 τὴν ἐντολήν; 01 und 04 haben τὸν νόμον («das Gesetz») und sind keiner Lesart zugeordnet."],
  ["ἐντολή glicht a [[MAT.15.3]] aa, νόμος («Gsetz») a de gwohnt Usdruck «Gsetz vo Gott»; λόγος entspricht [[MRK.7.13]]. Weli Form di eltischt isch, isch umstritte.",
   "Nach de automatische Zueornig läsed 03 und 05 τὸν λόγον, 032 τὴν ἐντολήν; 01 und 04 händ τὸν νόμον («s Gsetz») und sind keiner Läsart zueordnet."]),
 ("VAR-SBLGNTAPP-MAT-015-008-01:R2", "MAT.15.8", "Dieses Volk ehrt mich mit den Lippen", "Dieses Volk naht sich mir mit seinem Mund und ehrt mich mit den Lippen",
  "Das Volch ehrt mich mit de Lippe", "Das Volch chunnt mir nöch mit sim Muul und ehrt mich mit de Lippe", "mittel",
  "Das Zitat ist länger und folgt enger dem Jesajatext.", "S Zitat isch länger und folgt nöcher em Jesajatext.",
  {"R1": [("Ὁ λαὸς οὗτος", "Dieses Volk", "WH, Treg, NA28")],
   "R2": [("Ἐγγίζει μοι ὁ λαὸς οὗτος τῷ στόματι αὐτῶν καὶ", "Dieses Volk naht sich mir mit seinem Mund und", "RP")]},
  {"R1": [("Ὁ λαὸς οὗτος", "Das Volch", "WH, Treg, NA28")],
   "R2": [("Ἐγγίζει μοι ὁ λαὸς οὗτος τῷ στόματι αὐτῶν καὶ", "Das Volch chunnt mir nöch mit sim Muul und", "RP")]},
  ["Der längere Text gleicht das Zitat an den Wortlaut von [[ISA.29.13]] in der Septuaginta an; die kürzere Form entspricht [[MRK.7.6]].",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 die kürzere Form, 04 und 032 die längere."],
  ["De länger Text glicht s Zitat a de Wortlut vo [[ISA.29.13]] i de Septuaginta aa; di chürzer Form entspricht [[MRK.7.6]].",
   "Nach de automatische Zueornig läsed 01, 03 und 05 di chürzer Form, 04 und 032 di länger."]),
 ("VAR-SBLGNTAPP-MAT-015-014-01:R2", "MAT.15.14", "Sie sind Blinde, Führer von Blinden", "Sie sind blinde Führer",
  "Si sind Blindi, Füerer vo Blinde", "Si sind blindi Füerer", "gering",
  "Ohne «von Blinden» sind die Führer selbst blind; das Bild der Geführten folgt erst im nächsten Satz.",
  "Ohni «vo Blinde» sind d Füerer sälber blind; s Bild vo de Gfüerte chunnt erscht im nächschte Satz.",
  {"R1": [("τυφλοί εἰσιν ὁδηγοὶ τυφλῶν", "Sie sind Blinde, Führer von Blinden", "Treg, NA28")],
   "R2": [("τυφλοί εἰσιν ὁδηγοί", "Sie sind blinde Führer", "WH, NIV")],
   "R3": [("ὁδηγοί εἰσιν τυφλοὶ τυφλῶν", "Führer sind sie, blinde, von Blinden", "RP")]},
  {"R1": [("τυφλοί εἰσιν ὁδηγοὶ τυφλῶν", "Si sind Blindi, Füerer vo Blinde", "Treg, NA28")],
   "R2": [("τυφλοί εἰσιν ὁδηγοί", "Si sind blindi Füerer", "WH, NIV")],
   "R3": [("ὁδηγοί εἰσιν τυφλοὶ τυφλῶν", "Füerer sind si, blindi, vo Blinde", "RP")]},
  ["τυφλῶν kann ergänzt sein, um das Bild an den folgenden Satz anzugleichen, oder wegen der gleichen Endung (-ων) ausgefallen sein. R3 hat dieselben Wörter wie R1 in anderer Folge.",
   "Laut der automatischen Zuordnung lesen 03 und 05 R2, 01, 04 und 032 R3; den Wortlaut von R1 hat keine der erfassten Handschriften genau so."],
  ["τυφλῶν cha dezuecho sii, für s Bild em nächschte Satz aazgliiche, oder wäg de gliiche Endig (-ων) usgfalle sii. R3 hät di gliiche Wort wie R1 in anderer Reihefolg.",
   "Nach de automatische Zueornig läsed 03 und 05 R2, 01, 04 und 032 R3; de Wortlut vo R1 hät keini vo de erfasste Handschrifte gnau eso."]),
 ("VAR-SBLGNTAPP-MAT-015-017-01:R2", "MAT.15.17", "Begreift ihr nicht", "Begreift ihr noch nicht", "Begriifed ir nöd", "Begriifed ir no nöd", "gering",
  "«Noch nicht» verstärkt den Tadel.", "«No nöd» verstärcht de Tadel.",
  {"R1": [("οὐ", "nicht", "WH, Treg, NA28")], "R2": [("Οὔπω", "noch nicht", "RP")]},
  {"R1": [("οὐ", "nöd", "WH, Treg, NA28")], "R2": [("Οὔπω", "no nöd", "RP")]},
  ["οὔπω nimmt ἀκμήν («noch immer») aus [[MAT.15.16]] auf und entspricht [[MRK.8.17]]; es kann von dort beeinflusst sein.",
   "Laut der automatischen Zuordnung lesen 03 und 05 οὐ, 01, 04 und 032 οὔπω."],
  ["οὔπω nimmt ἀκμήν («immer no») us [[MAT.15.16]] uf und entspricht [[MRK.8.17]]; es cha vo dört beiiflusst sii.",
   "Nach de automatische Zueornig läsed 03 und 05 οὐ, 01, 04 und 032 οὔπω."]),
 ("VAR-SBLGNTAPP-MAT-015-022-01:R2", "MAT.15.22", "und schrie", "und schrie ihm zu", "und hät gschroue", "und hät ihm zuegschroue", "gering",
  "R2 nennt den Angerufenen ausdrücklich.", "R2 nännt de Aagrüefte usdrücklich.",
  {"R1": [("ἔκραζεν", "schrie (immer wieder)", "WH, Treg, NA28")], "R2": [("ἐκραύγασεν αὐτῷ", "schrie ihm zu", "RP")]},
  {"R1": [("ἔκραζεν", "hät (immer wider) gschroue", "WH, Treg, NA28")], "R2": [("ἐκραύγασεν αὐτῷ", "hät ihm zuegschroue", "RP")]},
  ["Die Formen wechseln zwischen Imperfekt (wiederholtes Schreien) und Aorist; αὐτῷ verdeutlicht den Adressaten.",
   "Laut der automatischen Zuordnung lesen 03 und 05 ἔκραζεν (05 mit dem Zusatz ὀπίσω αὐτοῦ, «hinter ihm her»), 032 ἐκραύγασεν αὐτῷ; 01 (ἔκραξεν) und 04 (ἐκραύγασεν ohne αὐτῷ) sind keiner Lesart zugeordnet."],
  ["D Forme wächsled zwüsche Imperfekt (s Schreie widerholt sich) und Aorist; αὐτῷ verdüütlicht, wem s gilt.",
   "Nach de automatische Zueornig läsed 03 und 05 ἔκραζεν, 032 ἐκραύγασεν αὐτῷ; 01 und 04 sind keiner Läsart zueordnet."]),
 ("VAR-SBLGNTAPP-MAT-015-031-02:R2", "MAT.15.31", "Stumme redeten, Verkrüppelte gesund waren und Lahme umhergingen",
  "Stumme redeten und Lahme umhergingen",
  "Stummi redt händ, Verchrüppleti gsund gsii sind und Lahmi umegloffe sind", "Stummi redt händ und Lahmi umegloffe sind", "gering",
  "Ohne die Verkrüppelten fehlt eine der Gruppen aus [[MAT.15.30]].", "Ohni d Verchrüppleti fehlt e Gruppe us [[MAT.15.30]].",
  {"R1": [("κυλλοὺς ὑγιεῖς", "Verkrüppelte gesund", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  {"R1": [("κυλλοὺς ὑγιεῖς", "Verchrüppleti gsund", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  ["Das Fehlen kann auf ein Überspringen zurückgehen (gleiche Endungen auf -ους); umgekehrt kann die Wendung ergänzt sein, damit alle in [[MAT.15.30]] genannten Gruppen vorkommen.",
   "Laut der automatischen Zuordnung lesen 03, 04, 05 und 032 mit κυλλοὺς ὑγιεῖς, 01 ohne."],
  ["S Fehle cha uf es Überspringe zruggaa (gliichi Endige uf -ους); umgekehrt cha d Wändig ergänzt sii, demit alli Gruppe us [[MAT.15.30]] vorchömed.",
   "Nach de automatische Zueornig läsed 03, 04, 05 und 032 mit κυλλοὺς ὑγιεῖς, 01 ohni."]),
 ("VAR-SBLGNTAPP-MAT-015-039-01:R2", "MAT.15.39", "von Magadan", "von Magdala", "vo Magadan", "vo Magdala", "gering",
  "Statt des unbekannten Magadan nennt R2 Magdala am See Gennesaret.", "Statt em unbekannte Magadan nännt R2 Magdala am See Gennesaret.",
  {"R1": [("Μαγαδάν", "Magadan", "WH, Treg, NA28")], "R2": [("Μαγδαλά", "Magdala", "RP")]},
  {"R1": [("Μαγαδάν", "Magadan", "WH, Treg, NA28")], "R2": [("Μαγδαλά", "Magdala", "RP")]},
  ["Abschreiber können den unbekannten Namen durch das bekannte Magdala ersetzt haben; [[MRK.8.10]] nennt an der Stelle Dalmanuta.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 Μαγαδάν (05 mit Artikel), 04 und 032 Μαγδαλάν."],
  ["Abschriiber chönd de unbekannt Name dur s bekannt Magdala ersetzt ha; [[MRK.8.10]] nännt a dere Stell Dalmanuta.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 Μαγαδάν, 04 und 032 Μαγδαλάν."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-014-001-036", "MAT.14.1-MAT.14.36", "section", "Der Tod des Täufers, Brot in der Einöde und Jesus auf dem Wasser",
  ["TU-MAT-014-001-012", "TU-MAT-014-013-021", "TU-MAT-014-022-033", "TU-MAT-014-034-036"],
  "Herodes, der Tetrarch, hält Jesus für den von den Toten auferweckten Johannes den Täufer. Rückblickend wird erzählt, wie Herodes Johannes wegen Herodias gefangen nahm und ihn auf Verlangen ihrer Tochter, der er unter Eid etwas versprochen hatte, im Gefängnis enthaupten liess. Als Jesus das hört, zieht er sich an einen einsamen Ort zurück; die Leute folgen ihm, er heilt ihre Kranken und sättigt mit fünf Broten und zwei Fischen etwa fünftausend Männer, ohne Frauen und Kinder. In der Nacht kommt er auf dem See zum Boot der Jünger; Petrus geht auf dem Wasser zu ihm, beginnt im Wind zu sinken, wird von Jesus ergriffen, der ihn kleingläubig nennt; die im Boot fallen vor Jesus nieder und bekennen ihn als Gottes Sohn. In Gennesaret werden alle gerettet, die den Saum seines Mantels berühren.", SEG),
 ("TU-MAT-014-001-012", "MAT.14.1-MAT.14.12", "narrative", "Herodes lässt Johannes den Täufer enthaupten", None,
  "Herodes, der Tetrarch, hört die Kunde von Jesus und sagt zu seinen Dienern, das sei Johannes der Täufer, von den Toten auferweckt; darum wirkten die Kräfte in ihm. Rückblickend erzählt der Text: Herodes hatte Johannes festgenommen und ins Gefängnis gebracht wegen Herodias, der Frau seines Bruders Philippus, denn Johannes hatte ihm gesagt, es sei ihm nicht erlaubt, sie zu haben. Herodes wollte ihn töten, fürchtete aber die Menge, die ihn für einen Propheten hielt. Bei der Feier seines Geburtstags tanzt die Tochter der Herodias, sie gefällt Herodes, und er verspricht ihr mit einem Eid, was immer sie erbittet. Von ihrer Mutter angestiftet, verlangt sie den Kopf des Johannes auf einer Schale; der König ist betrübt, lässt Johannes aber wegen der Eide und der Gäste im Gefängnis enthaupten. Der Kopf wird dem Mädchen gegeben, und es bringt ihn seiner Mutter. Die Jünger des Johannes begraben den Leichnam und berichten es Jesus.", None),
 ("TU-MAT-014-013-021", "MAT.14.13-MAT.14.21", "narrative", "Die Speisung der Fünftausend", None,
  "Als Jesus das hört, zieht er sich im Boot an einen einsamen Ort zurück; die Leute folgen ihm zu Fuss aus den Städten. Er hat Erbarmen mit ihnen und heilt ihre Kranken. Am Abend wollen die Jünger die Leute wegschicken, damit sie sich in den Dörfern zu essen kaufen; Jesus sagt: «Gebt ihr ihnen zu essen!» Sie haben nur fünf Brote und zwei Fische. Jesus lässt die Leute sich auf dem Gras lagern, blickt zum Himmel auf, spricht den Segen, bricht die Brote und gibt sie den Jüngern, die sie den Leuten geben. Alle essen und werden satt, und sie sammeln zwölf Körbe voll übrig gebliebener Brocken. Es sind etwa fünftausend Männer, ohne Frauen und Kinder.", None),
 ("TU-MAT-014-022-033", "MAT.14.22-MAT.14.33", "narrative", "Jesus und Petrus auf dem Wasser", None,
  "Jesus nötigt die Jünger, im Boot vorauszufahren, entlässt die Leute und steigt allein auf den Berg, um zu beten. Das Boot ist weit vom Land entfernt und wird von den Wellen bedrängt, denn der Wind steht entgegen. In der vierten Nachtwache kommt Jesus auf dem See zu ihnen; die Jünger halten ihn für ein Gespenst und schreien vor Furcht, er aber sagt: «Seid getrost, ich bin es; fürchtet euch nicht!» Petrus antwortet: «Herr, wenn du es bist, befiehl mir, auf dem Wasser zu dir zu kommen!» Auf Jesu «Komm!» steigt er aus dem Boot, geht auf dem Wasser und kommt zu Jesus. Als er den starken Wind sieht, fürchtet er sich, beginnt zu versinken und schreit: «Herr, rette mich!» Jesus ergreift ihn und sagt: «Du Kleingläubiger, warum hast du gezweifelt?» Als sie ins Boot steigen, legt sich der Wind; die im Boot fallen vor ihm nieder und sagen: «Wahrhaftig, du bist Gottes Sohn!»", None),
 ("TU-MAT-014-034-036", "MAT.14.34-MAT.14.36", "narrative", "Heilungen in Gennesaret", None,
  "Nach der Überfahrt kommen sie in Gennesaret an Land. Die Männer des Ortes erkennen Jesus, schicken Boten in die ganze Umgebung und bringen alle Kranken zu ihm. Sie bitten ihn, nur den Saum seines Mantels berühren zu dürfen, und alle, die ihn berühren, werden gerettet.", None),
 ("TU-MAT-015-001-039", "MAT.15.1-MAT.15.39", "section", "Rein und unrein, die kanaanäische Frau und die Speisung der Viertausend",
  ["TU-MAT-015-001-020", "TU-MAT-015-021-028", "TU-MAT-015-029-031", "TU-MAT-015-032-039"],
  "Pharisäer und Schriftgelehrte aus Jerusalem fragen, warum Jesu Jünger die Überlieferung der Ältesten übertreten und sich vor dem Essen die Hände nicht waschen. Jesus hält ihnen vor, dass sie um ihrer Überlieferung willen das Gebot Gottes übertreten, Vater und Mutter zu ehren, nennt sie Heuchler und wendet [[ISA.29.13]] auf sie an. Der Menge sagt er, nicht was in den Mund hineingeht, mache den Menschen unrein, sondern was aus dem Mund herauskommt; den Jüngern erklärt er, das komme aus dem Herzen. In der Gegend von Tyros und Sidon bittet eine kanaanäische Frau für ihre besessene Tochter; Jesus antwortet zunächst nicht und sagt, er sei nur zu den verlorenen Schafen des Hauses Israel gesandt, doch auf ihre Antwort hin nennt er ihren Glauben gross, und die Tochter ist geheilt. Am See von Galiläa heilt er auf dem Berg viele Kranke, und die Menge preist den Gott Israels. Mit sieben Broten und ein paar Fischen sättigt er viertausend Männer, ohne Frauen und Kinder, und fährt dann in das Gebiet von Magadan.", SEG),
 ("TU-MAT-015-001-020", "MAT.15.1-MAT.15.20", "dialogue", "Was den Menschen unrein macht", None,
  "Pharisäer und Schriftgelehrte aus Jerusalem fragen Jesus, warum seine Jünger die Überlieferung der Ältesten übertreten und sich vor dem Essen nicht die Hände waschen. Jesus fragt zurück, warum sie um ihrer Überlieferung willen das Gebot Gottes übertreten: Gott hat gesagt, man solle Vater und Mutter ehren; sie aber lehren, wer zu Vater oder Mutter sagt, was er ihnen an Hilfe geben könnte, sei eine Opfergabe, der brauche seinen Vater nicht zu ehren. Er nennt sie Heuchler und wendet [[ISA.29.13]] auf sie an. Dann ruft er die Menge herbei und sagt: Nicht was in den Mund hineingeht, macht den Menschen unrein, sondern was aus dem Mund herauskommt. Die Jünger berichten, die Pharisäer hätten daran Anstoss genommen; Jesus antwortet, jede Pflanze, die sein himmlischer Vater nicht gepflanzt hat, werde ausgerissen; sie seien Blinde, Führer von Blinden; wenn aber ein Blinder einen Blinden führe, fielen beide in eine Grube. Auf die Bitte des Petrus erklärt er das Gleichnis: Was in den Mund hineingeht, gelangt in den Bauch und wird ausgeschieden; aus dem Herzen aber kommen böse Gedanken, Morde, Ehebrüche, Unzucht, Diebstähle, falsche Zeugnisse und Lästerungen. Das macht den Menschen unrein, nicht das Essen mit ungewaschenen Händen.", None),
 ("TU-MAT-015-021-028", "MAT.15.21-MAT.15.28", "narrative", "Die kanaanäische Frau", None,
  "Jesus zieht sich in die Gegend von Tyros und Sidon zurück. Eine kanaanäische Frau aus jenem Gebiet schreit: «Hab Erbarmen mit mir, Herr, Sohn Davids! Meine Tochter ist schlimm besessen.» Jesus antwortet ihr kein Wort; die Jünger bitten ihn, sie fortzuschicken, weil sie hinter ihnen herschreit. Er sagt, er sei nur zu den verlorenen Schafen des Hauses Israel gesandt. Die Frau fällt vor ihm nieder und bittet: «Herr, hilf mir!» Er antwortet, es sei nicht recht, das Brot der Kinder zu nehmen und den Hündchen hinzuwerfen. Sie entgegnet: «Ja, Herr; denn auch die Hündchen essen von den Brotkrumen, die vom Tisch ihrer Herren fallen.» Da sagt Jesus: «Frau, dein Glaube ist gross! Dir geschehe, wie du willst.» Von jener Stunde an ist ihre Tochter geheilt.", None),
 ("TU-MAT-015-029-031", "MAT.15.29-MAT.15.31", "narrative", "Heilungen am See von Galiläa", None,
  "Jesus kommt an den See von Galiläa, steigt auf den Berg und sitzt dort. Viele Leute kommen mit Stummen, Blinden, Lahmen, Verkrüppelten und vielen anderen zu ihm und legen sie ihm zu Füssen, und er heilt sie. Die Menge staunt, als sie sieht, wie Stumme reden, Verkrüppelte gesund sind, Lahme umhergehen und Blinde sehen, und sie preisen den Gott Israels.", None),
 ("TU-MAT-015-032-039", "MAT.15.32-MAT.15.39", "narrative", "Die Speisung der Viertausend", None,
  "Jesus ruft seine Jünger und sagt, er habe Erbarmen mit der Menge, die schon drei Tage bei ihm bleibe und nichts zu essen habe; er wolle sie nicht hungrig wegschicken, damit sie unterwegs nicht zusammenbrechen. Die Jünger fragen, woher sie in der Einöde so viele Brote nehmen sollen. Sie haben sieben Brote und ein paar Fischlein. Jesus lässt die Menge sich auf den Boden lagern, nimmt die Brote und die Fische, spricht das Dankgebet, bricht sie und gibt sie den Jüngern, die sie den Leuten geben. Alle essen und werden satt, und sie sammeln sieben Körbe voll übrig gebliebener Brocken. Es sind viertausend Männer, ohne Frauen und Kinder. Dann entlässt Jesus die Leute, steigt ins Boot und kommt in das Gebiet von Magadan.", None),
]
UNITS_GSW = {
 "TU-MAT-014-001-036": ("De Tod vom Täufer, Broot i de Wüeschti und de Jesus uf em Wasser", "De Herodes, de Tetrarch, meint, de Jesus sig de Johannes de Täufer, vo de Tote uferweckt. Im Rückblick wird verzellt, wie de Herodes de Johannes wäge de Herodias gfange gnoo und en uf s Verlange vo irer Tochter, wo er mit eme Eid öppis versproche hät, im Gfängnis hät la chöpfe. Wo de Jesus das ghört, zieht er sich an en einsame Ort zrugg; d Lüüt gönd em nache, er heilt iri Chranke und macht mit föif Broot und zwee Fisch öppe föiftuusig Manne satt, ohni Fraue und Chind. I de Nacht chunnt er uf em See zum Boot vo de Jünger; de Petrus lauft uf em Wasser zu ihm, fangt im Wind aa versinke, wird vom Jesus packt, und dä nännt en chliigläubig; die im Boot falled vor em Jesus nider und bekännd en als Sohn vo Gott. Z Gennesaret wärded alli grettet, wo de Saum vo sim Mantel aarüered."),
 "TU-MAT-014-001-012": ("De Herodes laat de Johannes de Täufer chöpfe", "De Herodes, de Tetrarch, ghört d Nachricht vom Jesus und seit zu sine Diener, das sig de Johannes de Täufer, vo de Tote uferweckt; drum würkid d Chräft i ihm. Im Rückblick verzellt de Text: De Herodes hät de Johannes feschtgnoo und is Gfängnis brocht wäge de Herodias, de Frau vo sim Brüeder Philippus, wil de Johannes ihm gseit hät, es sig ihm nöd erlaubt, si z haa. De Herodes hät en wele umbringe, hät aber d Mängi gförchtet, wo en für en Prophet ghalte hät. Bim Fiire vo sim Geburtstag tanzt d Tochter vo de Herodias; si gfallt em Herodes, und er verspricht ere mit eme Eid, was si au heuscht. Vo irer Mueter aagstiftet, verlangt si de Chopf vom Johannes uf ere Platte; de König isch truurig, laat de Johannes aber wäge de Eid und de Gäscht im Gfängnis chöpfe. De Chopf wird em Meitli gää, und es bringt en sinere Mueter. D Jünger vom Johannes begrabed d Liich und melded s em Jesus."),
 "TU-MAT-014-013-021": ("D Spiisig vo de Föiftuusig", "Wo de Jesus das ghört, zieht er sich imene Boot an en einsame Ort zrugg; d Lüüt gönd em z Fuess us de Städt nache. Er hät Erbarme mit ine und heilt iri Chranke. Am Aabig wänd d Jünger d Lüüt furtschicke, demit si sich i de Dörfer öppis z ässe chaufed; de Jesus seit: «Gänd ir ine z ässe!» Si händ nu föif Broot und zwee Fisch. De Jesus laat d Lüüt sich ufs Gras setze, lueget zum Himel ufe, spricht de Säge, bricht d Broot und git si de Jünger, und die gänd si de Lüüt. Alli ässed und wärded satt, und si läsed zwölf Chörb voll übrigi Brocke uf. Es sind öppe föiftuusig Manne, ohni Fraue und Chind."),
 "TU-MAT-014-022-033": ("De Jesus und de Petrus uf em Wasser", "De Jesus drängt d Jünger, mit em Boot voruszfahre, schickt d Lüüt furt und gaat elei uf de Bärg go bätte. S Boot isch wiit vom Land ewägg und wird vo de Wälle plaget, dänn de Wind isch ine entgäge. I de vierte Nachtwach chunnt de Jesus uf em See zu ine; d Jünger meined, er sig es Gspängscht, und schreied vor Angscht, er aber seit: «Nu Muet, ich bi s; händ kei Angscht!» De Petrus antwortet: «Herr, wänn du s bisch, befiil mir, uf em Wasser zu dir z choo!» Uf s «Chumm!» vom Jesus stiigt er us em Boot, lauft uf em Wasser und chunnt zum Jesus. Wo er de starch Wind gseht, überchunnt er Angscht, fangt aa versinke und schreit: «Herr, rett mich!» De Jesus packt en und seit: «Du Chliigläubige, werum häsch zwiiflet?» Wo si is Boot stiiged, leit sich de Wind; die im Boot falled vor ihm nider und säged: «Würkli, du bisch de Sohn vo Gott!»"),
 "TU-MAT-014-034-036": ("Heilige z Gennesaret", "Nach de Überfahrt chömed si z Gennesaret a Land. D Manne vo dem Ort erchänned de Jesus, schicked Bote i die ganz Gäged und bringed alli Chranke zu ihm. Si bitted en, dass si nu de Saum vo sim Mantel dörfed aarüere, und alli, wo en aarüered, wärded grettet."),
 "TU-MAT-015-001-039": ("Rein und unrein, d kanaanäisch Frau und d Spiisig vo de Viertuusig", "Pharisäer und Schriftgelehrti us Jerusalem fröged, werum d Jünger vom Jesus gäge d Überliferig vo de Ältischte verstoossed und sich vor em Ässe d Händ nöd wäsched. De Jesus haltet ine vor, dass si für iri Überliferig gäge s Gebot vo Gott verstoossed, Vatter und Mueter z ehre, nännt si Heuchler und bezieht [[ISA.29.13]] uf si. De Mängi seit er, nöd was is Muul ine gaat, mach de Mänsch unrein, sondern was us em Muul usechunnt; de Jünger erklärt er, das chömm us em Härz. I de Gäged vo Tyros und Sidon bittet e kanaanäischi Frau für iri bsässni Tochter; de Jesus antwortet zerscht nöd und seit, er sig nu zu de verlorne Schaf vom Huus Israel gschickt, aber uf iri Antwort hii nännt er ire Glaube gross, und d Tochter isch gheilt. Am See vo Galiläa heilt er uf em Bärg vili Chranki, und d Mängi lobt de Gott vo Israel. Mit sibe Broot und es paar Fisch macht er viertuusig Manne satt, ohni Fraue und Chind, und fahrt dänn is Gebiet vo Magadan."),
 "TU-MAT-015-001-020": ("Was de Mänsch unrein macht", "Pharisäer und Schriftgelehrti us Jerusalem fröged de Jesus, werum sini Jünger gäge d Überliferig vo de Ältischte verstoossed und sich vor em Ässe d Händ nöd wäsched. De Jesus fröget zrugg, werum si für iri Überliferig gäge s Gebot vo Gott verstoossed: Gott hät gseit, me söll Vatter und Mueter ehre; si aber lehred, wer zum Vatter oder zur Mueter seit, was er ine a Hilf chönnt gää, sig e Opfergab, dä müess sin Vatter nöd ehre. Er nännt si Heuchler und bezieht [[ISA.29.13]] uf si. Dänn rüeft er d Mängi zu sich und seit: Nöd was is Muul ine gaat, macht de Mänsch unrein, sondern was us em Muul usechunnt. D Jünger verzelled, d Pharisäer heigid Aastoss gnoo; de Jesus antwortet, jedi Pflanze, wo sin himmlisch Vatter nöd pflanzt hät, wärdi usgrisse; si sigid Blindi, Füerer vo Blinde, und wänn en Blinde en Blinde füert, gheied beidi i e Grueb. Uf d Bitt vom Petrus erklärt er s Gliichnis: Was is Muul ine gaat, gaat in Buuch und wird usgschide; us em Härz aber chömed bösi Gedanke, Mord, Ehebrüch, Unzucht, Diebstähl, falschi Zügnis und Läschterige. Das macht de Mänsch unrein, nöd s Ässe mit ungwäschne Händ."),
 "TU-MAT-015-021-028": ("D kanaanäisch Frau", "De Jesus zieht sich i d Gäged vo Tyros und Sidon zrugg. E kanaanäischi Frau us dem Gebiet schreit: «Häb Erbarme mit mir, Herr, Sohn vom David! Mini Tochter isch schlimm bsässe.» De Jesus git ere kei Antwort; d Jünger bitted en, er söll si furtschicke, wil si hinder ine här schreit. Er seit, er sig nu zu de verlorne Schaf vom Huus Israel gschickt. D Frau fallt vor ihm nider und bittet: «Herr, hilf mir!» Er antwortet, es sig nöd rächt, s Broot vo de Chind z nää und de Hündli anezrüere. Si seit: «Ja, Herr; dänn au d Hündli ässed vo de Brösmeli, wo vom Tisch vo irne Herre abegheied.» Dänn seit de Jesus: «Frau, din Glaube isch gross! Dir söll gscheh, wie du wottsch.» Vo dere Stund aa isch iri Tochter gheilt."),
 "TU-MAT-015-029-031": ("Heilige am See vo Galiläa", "De Jesus chunnt an de See vo Galiläa, stiigt uf de Bärg und sitzt dört. Vil Lüüt chömed mit Stumme, Blinde, Lahme, Verchrüpplete und vilne andere zu ihm und leged si ihm vor d Füess, und er heilt si. D Mängi stuunt, wo si gseht, wie Stummi reded, Verchrüppleti gsund sind, Lahmi umelaufed und Blindi gsehnd, und si lobed de Gott vo Israel."),
 "TU-MAT-015-032-039": ("D Spiisig vo de Viertuusig", "De Jesus rüeft sini Jünger und seit, er heig Erbarme mit de Mängi, wo scho drüü Täg bi ihm bliibi und nüüt z ässe heig; er well si nöd hungrig furtschicke, demit si understwägs nöd zämebrächid. D Jünger fröged, vo wo si i de Wüeschti so vil Broot söled nää. Si händ sibe Broot und es paar Fischli. De Jesus laat d Mängi sich uf de Bode setze, nimmt d Broot und d Fisch, dankt, bricht si und git si de Jünger, und die gänd si de Lüüt. Alli ässed und wärded satt, und si läsed sibe Chörb voll übrigi Brocke uf. Es sind viertuusig Manne, ohni Fraue und Chind. Dänn schickt de Jesus d Lüüt furt, stiigt is Boot und chunnt is Gebiet vo Magadan."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) der "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "Erfasst sind für Matthäus 14–15 die Handschriften 01, 03, 04, 05 und 032; 02 ist hier nicht erhalten. Widerspricht die "
  "automatische Zuordnung den Sigla des SBLGNT-Apparats, gilt der Apparat: so bei VAR-SBLGNTAPP-MAT-015-031-03 (καί vor "
  "χωλούς), wo die Zuordnung WH bei der Lesart ohne καί führt, der Apparat aber bei R1; die Variante ändert die Übersetzung "
  "nicht und ist nicht als Alternative aufgenommen. Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des "
  "SBLGNT-Texts gezählt."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens. In Matthäus 14–15 fehlt im SBLGNT kein Vers. Als Alternativen stehen "
  "Lesarten des SBLGNT-Apparats, die die Übersetzung verändern; nicht aufgenommen sind reine Unterschiede der Wortfolge, des "
  "Artikels, der Rechtschreibung oder der Zeitform des Erzählens sowie Zusätze wie «seine (Jünger)» oder «Jesus» als "
  "ausdrückliches Subjekt (z. B. [[MAT.14.14]], [[MAT.14.22]], [[MAT.15.16]]), die den Sinn nicht ändern. In [[MAT.15.30]] "
  "stehen die vier Gruppen der Kranken in den Ausgaben in verschiedener Reihenfolge; die Übersetzung folgt dem SBLGNT."),
 ("Einheitliche Begriffe für das ganze Matthäusevangelium laut Vorgabe, in diesem Bereich verwendet: Schriftgelehrte, "
  "Pharisäer, Älteste (Mundart Schriftgelehrti, Pharisäer, Ältischti); Heuchler; «sogleich» für εὐθέως / εὐθύς (Mundart "
  "«grad»); «da» für erzählendes τότε (Mundart «dänn»); «siehe» für ἰδού (Mundart «lueg»); «besessen» für δαιμονίζομαι "
  "(Mundart «bsässe»); «himmlischer Vater» (Mundart «himmlisch Vatter»); Ortsnamen Galiläa, Jerusalem, Gennesaret."),
 ("Grundentscheide dieses Bereichs, für die übrigen Matthäus-Bereiche vorgeschlagen (jeweils mit Begründung in decisions): "
  "ὄχλος Einzahl «Menge», Mehrzahl οἱ ὄχλοι «die Leute» (Mundart «d Mängi» / «d Lüüt»); ἀναχωρέω «sich zurückziehen» "
  "(«sich zruggzieh»); σπλαγχνίζομαι «Erbarmen haben» («Erbarme haa»); προσκυνέω «niederfallen vor» («nidergfalle vor»), "
  "Alternativen «anbeten», «huldigen»; ὀλιγόπιστος «kleingläubig» («chliigläubig»), ὀλιγοπιστία «Kleinglaube»; πίστις "
  "«Glaube»; σκανδαλίζω je nach Zusammenhang «Anstoss nehmen» (gegen Jesus) bzw. «zu Fall kommen / bringen» (im Glauben); "
  "κοινόω «unrein machen»; παράδοσις «Überlieferung»; δοξάζω τὸν θεόν in der Erzählung «Gott preisen» (Mundart «Gott lobe»); "
  "κύριε als Anrede «Herr»; ἐγώ εἰμι als Erkennungswort «ich bin es» («ich bi s»); εὐλογέω über dem Brot «den Segen "
  "sprechen», εὐχαριστέω «das Dankgebet sprechen»; κόφινος und σπυρίς beide «Körbe»; κωφός je nach Zusammenhang «stumm» oder "
  "«taub»."),
 ("Parallelen: Für [[MAT.14.1]]–[[MAT.14.36]] und [[MAT.15.1]]–[[MAT.15.39]] sind die Markus-Arbeitsübersetzungen "
  "([[MRK.6.14]]–[[MRK.6.56]], [[MRK.7.1]]–[[MRK.7.30]], [[MRK.8.1]]–[[MRK.8.10]]) verglichen. Gleiche griechische Wendungen sind "
  "gleich übersetzt (z. B. «Seid getrost, ich bin es», das Jesajazitat, «Hündchen»); wo Matthäus anders erzählt, folgt die "
  "Übersetzung seinem Wortlaut (Herodes will Johannes töten, [[MAT.14.5]]; Petrus auf dem Wasser und das Bekenntnis "
  "[[MAT.14.28]]–[[MAT.14.33]]; kein «Korban» und keine Erklärung der Speisen; «kanaanäische Frau»; Frauen und Kinder nicht "
  "mitgezählt)."),
 ("Erzählweise und Redegrenzen: Matthäus erzählt meist im Aorist; seine wenigen Formen im erzählenden Präsens (λέγουσιν, "
  "λέγει, φησίν, προσέρχονται) sind als Präsens beibehalten. ὅτι vor direkter Rede und λέγων / λέγουσα als Redeeinleitung "
  "sind nicht eigens übersetzt, wo das Deutsche sie nicht braucht. Anführungszeichen sind eine Entscheidung der Übersetzung. "
  "In [[MAT.15.5]]–[[MAT.15.6]] steht die von Jesus wiedergegebene Lehre der Gegner in einfachen Anführungszeichen bis «nicht "
  "zu ehren»; die andere Abgrenzung nennt die decision zu [[MAT.15.6]]."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig. Eigeti Formulierig; nöd us ere veröffentlichte Mundart-Bible übernoo.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) vo de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte. Wo si de Sigla vom SBLGNT-Apparat widerspricht, gilt de "
  "Apparat."),
 ("Text: D Übersetzig folgt de SBLGNT-Token; i Matthäus 14–15 fehlt kei Vers. Als Alternative stönd Läsarte, wo d "
  "Übersetzig veränderet; reini Underschid i de Wortfolg, bim Artikel oder Zuesätz wie «sini (Jünger)» sind nöd ufgnoo."),
 ("Einheitlichi Begriff fürs ganz Matthäusevangelium: Schriftgelehrti, Pharisäer, Ältischti; Heuchler; «grad» für εὐθέως / "
  "εὐθύς; «dänn» für τότε; «lueg» für ἰδού; «bsässe»; «himmlisch Vatter»; «Himel»."),
 ("Grundentscheid vo dem Bereich (usfüerlich i de hochdütsche translation_notes): ὄχλος «d Mängi», οἱ ὄχλοι «d Lüüt»; "
  "ἀναχωρέω «sich zruggzieh»; σπλαγχνίζομαι «Erbarme haa»; προσκυνέω «vor öpperem nidergfalle»; ὀλιγόπιστος «chliigläubig»; "
  "πίστις «Glaube»; σκανδαλίζω «Aastoss nää» oder «z Fall choo»; κοινόω «unrein mache»; δοξάζω τὸν θεόν «Gott lobe»; "
  "ἐγώ εἰμι «ich bi s»; κύριε «Herr»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Petrus»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«s Gebot vo Gott», «de Sohn vo Gott»); Gägewartsforme vom Erzähle (seit, säged, chömed) bliibed."),
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
        if len(refs_c) != last or len(toks) != last:
            raise SystemExit(f"MAT {c}: unerwartete Versliste")
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Riich, Broot), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Namen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; Wiederholungswörter einheitlich (Grundentscheide in translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_14_15.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 14–15 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
