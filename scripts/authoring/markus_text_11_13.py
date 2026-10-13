#!/usr/bin/env python3
"""Autorenwerkzeug: Markus 11–13 – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/markus_text_11_13.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MRK besteht schon und wird hier nur referenziert, nicht geschrieben.
KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben in den Lesarten stammen aus der maschinellen Zuordnung
(METHOD-AUTO-COLLATION-V1, Datensätze WREAD-CNTR-MRK-011..013), nicht aus eigener Prüfung der Handschriften.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, write  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-MARK"]
CHAPTERS = ((11, 33), (12, 44), (13, 37))

DE = {
 # ------------------------------------------------------------ Kapitel 11
 "MRK.11.1": "Und{1} [als]{2} [sie]{3} [in die Nähe von]{4} [Jerusalem]{5} [kommen]{3}, [nach]{6} Betfage{7} und{8} Betanien{9} [am]{10,11} [Ölberg]{12-14}, [sendet]{15} er [zwei]{16} [seiner]{17,19} [Jünger]{18} [aus]{15}",
 "MRK.11.2": "und{1} [sagt]{2} [zu ihnen]{3}: «[Geht]{4} [in]{5} [das]{6} [Dorf]{7}, [das]{8} [vor]{9} [euch]{10} liegt; und{11} [gleich]{12}, [wenn ihr]{13} [dort]{14,15} [hineinkommt]{13}, [werdet ihr]{16} [ein Fohlen]{17} [angebunden]{18} [finden]{16}, [auf]{19} [dem]{20} [noch]{22} [kein]{21} [Mensch]{23} [gesessen hat]{24}. [Bindet]{25} [es]{26} [los]{25} und{27} [bringt]{28} es!",
 "MRK.11.3": "Und{1} [wenn]{2} [jemand]{3} [zu euch]{4} [sagt]{5}: ‹[Was]{6} [tut ihr]{7} [da]{8}?›, [dann sagt]{9}: ‹[Der]{11} [Herr]{12} [braucht]{14,15} [es]{13}, und{16} [er schickt]{19} [es]{18} [sofort]{17} [wieder]{20} [hierher]{21}.›» ~10(ὅτι leitet die Rede ein)",
 "MRK.11.4": "Und{1} [sie gingen hin]{2} und{3} [fanden]{4} [ein Fohlen]{5}, [angebunden]{6} [an]{7} [einer Tür]{8} [draussen]{9} [an]{10} [der]{11} [Strasse]{12}, und{13} [sie binden]{14} [es]{15} [los]{14}.",
 "MRK.11.5": "Und{1} [einige]{2}, [die]{3} [dort]{4} [standen]{5}, [sagten]{6} [zu ihnen]{7}: «[Was]{8} [tut ihr]{9} da? [Ihr bindet]{10} [das]{11} [Fohlen]{12} [los]{10}?»",
 "MRK.11.6": "[Sie]{1} [aber]{2} [sagten]{3} [zu ihnen]{4}, [wie]{5} [Jesus]{7,8} [gesagt hatte]{6}; und{9} [man liess]{10} [sie]{11} [gewähren]{10}.",
 "MRK.11.7": "Und{1} [sie bringen]{2} [das]{3} [Fohlen]{4} [zu]{5} [Jesus]{6,7} und{8} [legen]{9} [ihm]{10} [ihre]{13} [Mäntel]{11,12} [auf]{9}, und{14} [er setzte sich]{15} [darauf]{16,17}.",
 "MRK.11.8": "Und{1} [viele]{2} [breiteten]{6} [ihre]{5} [Mäntel]{3,4} [auf]{7} [den]{8} [Weg]{9} [aus]{6}, [andere]{10} [aber]{11} [Zweige]{12}, [die sie]{13} [auf]{14} [den]{15} [Feldern]{16} [abgeschnitten hatten]{13}.",
 "MRK.11.9": "Und{1} [die]{2} [vorausgingen]{3} und{4} [die]{5} [nachfolgten]{6}, [riefen]{7}: «[Hosanna]{8}! [Gesegnet sei]{9} [der]{10}, der [kommt]{11} [im]{12} [Namen]{13} [des Herrn]{14}!",
 "MRK.11.10": "[Gesegnet sei]{1} [das]{2} [kommende]{3} [Reich]{4} [unseres]{5,7} [Vaters]{6} [David]{8}! [Hosanna]{9} [in]{10} [den]{11} [Höhen]{12}!»",
 "MRK.11.11": "Und{1} [er zog]{2} [in]{3} [Jerusalem]{4} [ein]{2}, [in]{5} [den]{6} [Tempel]{7}; und{8} [nachdem er]{9} [alles]{10} [ringsum angeschaut hatte]{9}, [ging er]{16}, [da]{13} [es]{14,15} [schon]{12} [spät]{11} [war]{13}, [mit]{19} [den]{20} [Zwölf]{21} [hinaus]{16} [nach]{17} [Betanien]{18}.",
 "MRK.11.12": "Und{1} [am]{2} [nächsten Tag]{3}, [als]{4} [sie]{5} [von]{6} [Betanien]{7} [weggingen]{4}, [hatte er Hunger]{8}.",
 "MRK.11.13": "Und{1} [als er]{2} [von]{4} [weitem]{5} [einen Feigenbaum]{3} [sah]{2}, [der]{6} [Blätter]{7} [hatte]{6}, [ging er hin]{8}, [ob]{9} [er]{12} [vielleicht]{10} [etwas]{11} [an]{13} [ihm]{14} [finden würde]{12}. Und{15} [als er]{16} [zu]{17} [ihm]{18} [kam]{16}, [fand er]{20} [nichts]{19} [ausser]{21,22} [Blättern]{23}; [denn]{25} [es war]{28} [nicht]{27} [die]{24} [Zeit]{26} [der Feigen]{29}.",
 "MRK.11.14": "Und{1} [er ergriff das Wort]{2} [und sagte]{3} [zu ihm]{4}: «[Nie mehr]{5} [in]{6} [Ewigkeit]{7,8} [soll]{13} [jemand]{11} [von]{9} [dir]{10} [Frucht]{12} [essen]{13}!» Und{14} [seine]{18} [Jünger]{16,17} [hörten es]{15}.",
 "MRK.11.15": "Und{1} [sie kommen]{2} [nach]{3} [Jerusalem]{4}. Und{5} [er ging]{6} [in]{7} [den]{8} [Tempel]{9} [hinein]{6} und [fing an]{10}, [die]{12} [Verkäufer]{13} und{14} [die]{15} [Käufer]{16} [im]{17,18} [Tempel]{19} [hinauszutreiben]{11}; und{20} [die]{21} [Tische]{22} [der]{23} [Geldwechsler]{24} und{25} [die]{26} [Sitze]{27} [der]{28} [Taubenverkäufer]{29-31} [stiess er um]{32},",
 "MRK.11.16": "und{1} [er liess]{3} [nicht]{2} [zu]{3}, [dass]{4} [jemand]{5} [ein Gerät]{7} [durch]{8} [den]{9} [Tempel]{10} [trug]{6}.",
 "MRK.11.17": "Und{1} [er lehrte]{2} und{3} [sagte]{4} [zu ihnen]{5}: «[Steht]{7} [nicht]{6} [geschrieben]{7}: ‹[Mein]{11} [Haus]{9,10} [soll]{14} [ein Haus]{12} [des Gebets]{13} [heissen]{14} [für alle]{15} [Völker]{16,17}›? [Ihr]{18} [aber]{19} [habt]{20} [es]{21} [zu einer Räuberhöhle]{22,23} [gemacht]{20}!» ~8(ὅτι leitet das Zitat ein)",
 "MRK.11.18": "Und{1} [die]{3} [Hohepriester]{4} und{5} [die]{6} [Schriftgelehrten]{7} [hörten es]{2} und{8} [suchten]{9}, [wie]{10} [sie]{12} [ihn]{11} [umbringen könnten]{12}; [denn]{14} [sie fürchteten]{13} [ihn]{15}, [denn]{17} [die]{18} [ganze]{16} [Menge]{19} [war überwältigt]{20} [von]{21} [seiner]{22,24} [Lehre]{23}.",
 "MRK.11.19": "Und{1} [wenn]{2} [es]{4} [Abend]{3} [wurde]{4}, [gingen sie]{5} [aus]{6} [der]{7} [Stadt]{8} [hinaus]{5}.",
 "MRK.11.20": "Und{1} [als sie]{2} [am frühen Morgen]{3} [vorbeigingen]{2}, [sahen sie]{4} [den]{5} [Feigenbaum]{6} [von]{8} [den Wurzeln]{9} [her]{8} [verdorrt]{7}.",
 "MRK.11.21": "Und{1} [Petrus]{3,4} [erinnert sich]{2} und [sagt]{5} [zu ihm]{6}: «[Rabbi]{7}, [sieh]{8}, [der]{9} [Feigenbaum]{10}, [den]{11} [du verflucht hast]{12}, [ist verdorrt]{13}!»",
 "MRK.11.22": "Und{1} [Jesus]{3,4} [antwortet]{2} und [sagt]{5} [zu ihnen]{6}: «[Habt]{7} [Glauben]{8} [an Gott]{9}!",
 "MRK.11.23": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Wer]{5,6} [zu]{8} [diesem]{10} [Berg]{9} [sagt]{7}: ‹[Heb dich hoch]{11} und{12} [stürz dich]{13} [ins]{14,15} [Meer]{16}!›, und{17} [nicht]{18} [zweifelt]{19} [in]{20} [seinem]{21,23} [Herzen]{22}, [sondern]{24} [glaubt]{25}, [dass]{26} [geschieht]{29}, [was]{27} [er sagt]{28}, [dem]{31} [wird es zuteil]{30}. ~4(ὅτι leitet die Rede ein)",
 "MRK.11.24": "[Darum]{1,2} [sage ich]{3} [euch]{4}: [Alles]{5}, [worum]{6} [ihr betet]{7} und{8} [bittet]{9} – [glaubt]{10}, [dass]{11} [ihr es empfangen habt]{12}, und{13} [es wird]{14} [euch]{15} [zuteil]{14}.",
 "MRK.11.25": "Und{1} [wenn]{2} [ihr dasteht]{3} [und betet]{4}, [dann vergebt]{5}, [wenn]{6} [ihr]{8} [etwas]{7} [gegen]{9} [jemanden]{10} [habt]{8}, [damit]{11} [auch]{12} [euer]{13,15} [Vater]{14} [im]{16-18} [Himmel]{19} [euch]{21} [eure]{22,24} [Verfehlungen]{23} [vergibt]{20}.»",
 "MRK.11.27": "Und{1} [sie kommen]{2} [wieder]{3} [nach]{4} [Jerusalem]{5}. Und{6} [während]{10} [er]{11} [im]{7,8} [Tempel]{9} [umhergeht]{10}, [kommen]{12} [die]{15} [Hohepriester]{16} und{17} [die]{18} [Schriftgelehrten]{19} und{20} [die]{21} [Ältesten]{22} [zu]{13} [ihm]{14}",
 "MRK.11.28": "und{1} [sagten]{2} [zu ihm]{3}: «[In]{4} [welcher]{5} [Vollmacht]{6} [tust du]{8} [das]{7}? [Oder]{9} [wer]{10} [hat]{12} [dir]{11} [diese]{13,15} [Vollmacht]{14} [gegeben]{12}, [dass]{16} [du]{18} [das]{17} [tust]{18}?»",
 "MRK.11.29": "[Jesus]{1,3} [aber]{2} [sagte]{4} [zu ihnen]{5}: «[Ich will]{6} [euch]{7} [eine]{8} [Frage]{9} [stellen]{6}, und{10} [antwortet]{11} [mir]{12}, und{13} [ich werde]{14} [euch]{15} [sagen]{14}, [in]{16} [welcher]{17} [Vollmacht]{18} [ich]{20} [das]{19} [tue]{20}.",
 "MRK.11.30": "[Die]{1} [Taufe]{2} [des]{3} [Johannes]{4}: [War]{7} sie [vom]{5} [Himmel]{6} [oder]{8} [von]{9} [Menschen]{10}? [Antwortet]{11} [mir]{12}!»",
 "MRK.11.31": "Und{1} [sie überlegten]{2} [miteinander]{3,4} [und sagten]{5}: «[Was]{6} [sollen wir sagen]{7}? [Wenn]{8} [wir sagen]{9}: ‹[Vom]{10} [Himmel]{11}›, [wird er sagen]{12}: ‹[Warum]{13,14} [habt ihr]{17} [ihm]{18} [dann]{15} [nicht]{16} [geglaubt]{17}?›",
 "MRK.11.32": "[Sollen wir]{2} [aber]{1} [sagen]{2}: ‹[Von]{3} [Menschen]{4}›?» – [Sie fürchteten]{5} [die]{6} [Menge]{7}; [denn]{9} [alle]{8} [meinten]{10} [von Johannes]{11,12}, [dass]{14} [er]{16} [wirklich]{13} [ein Prophet]{15} [war]{16}.",
 "MRK.11.33": "Und{1} [sie antworten]{2} [Jesus]{3,4} [und sagen]{5}: «[Wir wissen es]{7} [nicht]{6}.» Und{8} [Jesus]{9,10} [sagt]{11} [zu ihnen]{12}: «[Auch]{13} [ich]{14} [sage]{15} [euch]{16} [nicht]{13}, [in]{17} [welcher]{18} [Vollmacht]{19} [ich]{21} [das]{20} [tue]{21}.»",
 # ------------------------------------------------------------ Kapitel 12
 "MRK.12.1": "Und{1} [er fing an]{2}, [in]{4} [Gleichnissen]{5} [zu ihnen]{3} [zu reden]{6}: «[Einen Weinberg]{7} [pflanzte]{9} [ein Mensch]{8}, und{10} [er zog]{11} [einen Zaun]{12} [darum]{11}, und{13} [hob]{14} [eine Keltergrube]{15} [aus]{14}, und{16} [baute]{17} [einen Turm]{18}, und{19} [verpachtete]{20} [ihn]{21} [an Weinbauern]{22}, und{23} [reiste ausser Landes]{24}.",
 "MRK.12.2": "Und{1} [er sandte]{2} [zur]{6} [gegebenen Zeit]{7} [einen Knecht]{8} [zu]{3} [den]{4} [Weinbauern]{5}, [um]{9} [von]{10} [den]{11} [Weinbauern]{12} [seinen Anteil an]{14} [den]{15} [Früchten]{16} [des]{17} [Weinbergs]{18} [zu holen]{13}.",
 "MRK.12.3": "Und{1} [sie packten]{2} [ihn]{3}, [schlugen ihn]{4} und{5} [schickten ihn]{6} [mit leeren Händen]{7} [fort]{6}.",
 "MRK.12.4": "Und{1} [wieder]{2} [sandte er]{3} [einen anderen]{6} [Knecht]{7} [zu]{4} [ihnen]{5}; [auch den]{8} [schlugen sie auf den Kopf]{9} und{10} [beschimpften ihn]{11}.",
 "MRK.12.5": "Und{1} [einen anderen]{2} [sandte er]{3}; [auch den]{4} [töteten sie]{5}; und{6} so [viele]{7} [andere]{8}: [die einen]{9,10} [schlugen sie]{11}, [die anderen]{12,13} [töteten sie]{14}.",
 "MRK.12.6": "[Noch]{1} [einen]{2} [hatte er]{3}, [einen geliebten]{5} [Sohn]{4}. [Den]{7} [sandte er]{6} [als Letzten]{8} [zu]{9} [ihnen]{10} [und sagte sich]{11}: ‹[Vor meinem]{14,16} [Sohn]{15} [werden sie Achtung haben]{13}.› ~12(ὅτι leitet die Rede ein)",
 "MRK.12.7": "[Jene]{1} [Weinbauern]{3,4} [aber]{2} [sagten]{7} [zueinander]{5,6}: ‹[Das]{9} [ist]{10} [der]{11} [Erbe]{12}; [kommt]{13}, [lasst uns]{14} [ihn]{15} [töten]{14}, und{16} [das]{19} [Erbe]{20} [wird]{18} [uns]{17} [gehören]{18}!› ~8(ὅτι leitet die Rede ein)",
 "MRK.12.8": "Und{1} [sie packten]{2} und [töteten]{3} [ihn]{4} und{5} [warfen]{6} [ihn]{7} [aus]{8} [dem]{9} [Weinberg]{10} [hinaus]{6}.",
 "MRK.12.9": "[Was]{1} [wird]{2} [der]{3} [Herr]{4} [des]{5} [Weinbergs]{6} [tun]{2}? [Er wird kommen]{7} und{8} [die]{10} [Weinbauern]{11} [umbringen]{9} und{12} [den]{14} [Weinberg]{15} [anderen]{16} [geben]{13}.",
 "MRK.12.10": "[Habt ihr]{5} [nicht einmal]{1} [diese]{2,4} [Schriftstelle]{3} [gelesen]{5}: ‹[Der Stein]{6}, [den]{7} [die]{9} [Bauleute]{10} [verworfen haben]{8}, [der]{11} [ist]{12} [zum]{13} [Eckstein]{14,15} [geworden]{12};",
 "MRK.12.11": "[vom]{1} [Herrn]{2} [ist]{3} [das]{4} [geschehen]{3}, und{5} [es ist]{6} [wunderbar]{7} [in]{8} [unseren]{10} [Augen]{9}›?»",
 "MRK.12.12": "Und{1} [sie suchten]{2} [ihn]{3} [festzunehmen]{4}, und{5} [sie fürchteten]{6} [die]{7} [Menge]{8}; [denn]{10} [sie merkten]{9}, [dass]{11} [er]{16} [das]{14} [Gleichnis]{15} [auf]{12} [sie]{13} [hin]{12} [erzählt hatte]{16}. Und{17} [sie liessen]{18} [ihn]{19} [stehen]{18} [und gingen weg]{20}.",
 "MRK.12.13": "Und{1} [sie schicken]{2} [einige]{5} [von den]{6} [Pharisäern]{7} und{8} [von den]{9} [Herodianern]{10} [zu]{3} [ihm]{4}, [um]{11} [ihn]{12} [mit einer Aussage]{14} [zu fangen]{13}.",
 "MRK.12.14": "Und{1} [sie kommen]{2} [und sagen]{3} [zu ihm]{4}: «[Lehrer]{5}, [wir wissen]{6}, [dass]{7} [du]{9} [wahrhaftig]{8} [bist]{9} und{10} [dich]{13} [um niemanden]{11,14,15} [kümmerst]{12}; [denn]{17} [du siehst nicht auf das Ansehen]{16,18,19,20:idiom} [der Menschen]{21}, [sondern]{22} [lehrst]{29} [den]{25} [Weg]{26} [Gottes]{27,28} [in]{23} [Wahrheit]{24}. [Ist es erlaubt]{30}, [dem Kaiser]{33} [Steuer]{32} [zu zahlen]{31}, [oder]{34} [nicht]{35}? [Sollen wir zahlen]{36} [oder]{37} [nicht]{38} [zahlen]{39}?»",
 "MRK.12.15": "[Er]{1} [aber]{2} [durchschaute]{3} [ihre]{4,5} [Heuchelei]{6} [und sagte]{7} [zu ihnen]{8}: «[Was]{9} [stellt ihr]{11} [mich]{10} [auf die Probe]{11}? [Bringt]{12} [mir]{13} [einen Denar]{14}, [damit]{15} [ich ihn sehe]{16}.»",
 "MRK.12.16": "[Sie]{1} [aber]{2} [brachten einen]{3}. Und{4} [er sagt]{5} [zu ihnen]{6}: «[Wessen]{7} [Bild]{8,9} und{11} [Aufschrift]{12,13} [ist das]{10}?» [Sie]{14} [aber]{15} [sagten]{16} [zu ihm]{17}: «[Des Kaisers]{18}.»",
 "MRK.12.17": "[Jesus]{1,3} [aber]{2} [sagte]{4} [zu ihnen]{5}: «[Was]{6} [des Kaisers]{7} ist, [gebt]{8} [dem Kaiser]{9}, und{10} [was]{11} [Gottes]{12,13} ist, [Gott]{14,15}!» Und{16} [sie staunten sehr]{17} [über]{18} [ihn]{19}.",
 "MRK.12.18": "Und{1} [es kommen]{2} [Sadduzäer]{3} [zu]{4} [ihm]{5}, [die]{6} [sagen]{7}, [es gebe]{10} [keine]{9} [Auferstehung]{8}, und{11} [sie fragten]{12} [ihn]{13} [und sagten]{14}:",
 "MRK.12.19": "«[Lehrer]{1}, [Mose]{2} [hat]{3} [uns]{4} [geschrieben]{3}: [Wenn]{6} [jemandes]{7} [Bruder]{8} [stirbt]{9} und{10} [eine Frau]{12} [hinterlässt]{11} und{13} [kein]{14} [Kind]{16} [zurücklässt]{15}, [dann soll]{17} [sein]{21} [Bruder]{19,20} [die]{22} [Frau]{23} [nehmen]{18} und{24} [seinem]{27,29} [Bruder]{28} [Nachkommen]{26} [erwecken]{25}. ~5(ὅτι leitet das Zitat ein)",
 "MRK.12.20": "[Es waren]{3} [sieben]{1} [Brüder]{2}. Und{4} [der]{5} [erste]{6} [nahm]{7} [eine Frau]{8}, und{9} [als er starb]{10}, [hinterliess er]{12} [keine]{11} [Nachkommen]{13}.",
 "MRK.12.21": "Und{1} [der]{2} [zweite]{3} [nahm]{4} [sie]{5} und{6} [starb]{7}, [ohne]{8} [Nachkommen]{10} [zu hinterlassen]{9}; und{11} [der]{12} [dritte]{13} [ebenso]{14}.",
 "MRK.12.22": "Und{1} [die]{2} [sieben]{3} [hinterliessen]{5} [keine]{4} [Nachkommen]{6}. [Zuletzt]{7} [von allen]{8} [starb]{12} [auch]{9} [die]{10} [Frau]{11}.",
 "MRK.12.23": "[In]{1} [der]{2} [Auferstehung]{3}, [wenn]{4} [sie auferstehen]{5}: [Wem]{6} [von ihnen]{7} [wird sie]{8} [als Frau]{9} [gehören]{8}? [Denn]{11} [die]{10} [sieben]{12} [haben]{13} [sie]{14} [zur Frau]{15} [gehabt]{13}.»",
 "MRK.12.24": "[Jesus]{3,4} [sagte]{1} [zu ihnen]{2}: «[Irrt ihr]{8} [nicht]{5} [deshalb]{6,7}, [weil ihr]{10} [weder]{9} [die]{11} [Schriften]{12} [kennt]{10} [noch]{13} [die]{14} [Kraft]{15} [Gottes]{16,17}?",
 "MRK.12.25": "[Denn]{2} [wenn]{1} [sie]{5} [von]{3} [den Toten]{4} [auferstehen]{5}, [heiraten sie]{7} [weder]{6}, [noch]{8} [werden sie verheiratet]{9}, [sondern]{10} [sie sind]{11} [wie]{12} [Engel]{13} [im]{14,15} [Himmel]{16}.",
 "MRK.12.26": "[Was]{1} [aber]{2} [die]{3} [Toten]{4} [betrifft]{1}, [dass]{5} [sie auferweckt werden]{6}: [Habt ihr]{8} [nicht]{7} [im]{9,10} [Buch]{11} [des Mose]{12} [gelesen]{8}, [beim]{13,14} [Dornbusch]{15}, [wie]{16} [Gott]{19,20} [zu ihm]{18} [sprach]{17}: ‹[Ich]{22} bin [der]{23} [Gott]{24} [Abrahams]{25} und{26} [der]{27} [Gott]{28} [Isaaks]{29} und{30} [der]{31} [Gott]{32} [Jakobs]{33}›? ~21(λέγων leitet das Zitat ein)",
 "MRK.12.27": "[Er ist]{2} [nicht]{1} [ein Gott]{3} [von Toten]{4}, [sondern]{5} [von Lebenden]{6}. [Ihr irrt]{8} [sehr]{7}.»",
 "MRK.12.28": "Und{1} [einer]{3} [der]{4} [Schriftgelehrten]{5} [trat hinzu]{2}; [er hatte]{6} [sie]{7} [miteinander streiten]{8} [hören]{6} [und sah]{9}, [dass]{10} [er]{12} [ihnen]{13} [gut]{11} [geantwortet hatte]{12}. [Er fragte]{14} [ihn]{15}: «[Welches]{16} [Gebot]{18} [ist]{17} [das erste]{19} [von allen]{20}?»",
 "MRK.12.29": "[Jesus]{2,3} [antwortete]{1}: «[Das erste]{5} [ist]{6}: ‹[Höre]{7}, [Israel]{8}: [Der Herr]{9}, [unser]{12} [Gott]{10,11}, [der Herr]{13} [ist]{15} [einer]{14}; ~4(ὅτι leitet die Rede ein)",
 "MRK.12.30": "und{1} [du sollst]{2} [den Herrn]{3}, [deinen]{6} [Gott]{4,5}, [lieben]{2} [mit]{7} [deinem]{9,11} [ganzen]{8} [Herzen]{10} und{12} [mit]{13} [deiner]{15,17} [ganzen]{14} [Seele]{16} und{18} [mit]{19} [deinem]{21,23} [ganzen]{20} [Denken]{22} und{24} [mit]{25} [deiner]{27,29} [ganzen]{26} [Kraft]{28}.›",
 "MRK.12.31": "[Das zweite]{1} [ist dieses]{2}: ‹[Du sollst]{3} [deinen]{4,6} [Nächsten]{5} [lieben]{3} [wie]{7} [dich selbst]{8}.› [Grösser]{9} [als diese]{10} [ist]{14} [kein]{13} [anderes]{11} [Gebot]{12}.»",
 "MRK.12.32": "Und{1} [der]{4} [Schriftgelehrte]{5} [sagte]{2} [zu ihm]{3}: «[Gut]{6}, [Lehrer]{7}! [Mit Recht]{8,9} [hast du gesagt]{10}: [Einer]{12} [ist er]{13}, und{14} [es gibt]{16} [keinen]{15} [anderen]{17} [ausser]{18} [ihm]{19}. ~11(ὅτι leitet die Rede ein)",
 "MRK.12.33": "Und{1} [ihn]{4} [zu lieben]{2,3} [mit]{5} [ganzem]{6} [Herzen]{7,8} und{9} [mit]{10} [ganzem]{11} [Verstand]{12,13} und{14} [mit]{15} [ganzer]{16} [Kraft]{17,18} und{19} [den]{22} [Nächsten]{23} [zu lieben]{20,21} [wie]{24} [sich selbst]{25}, [das ist]{27} [mehr]{26} [als alle]{28} [Brandopfer]{29,30} und{31} [Schlachtopfer]{32}.»",
 "MRK.12.34": "Und{1} [als]{4} [Jesus]{2,3} [sah]{4}, [dass]{6} [er]{5} [verständig]{7} [geantwortet hatte]{8}, [sagte er]{9} [zu ihm]{10}: «[Du bist]{13} [nicht]{11} [fern]{12} [vom]{14,15} [Reich]{16} [Gottes]{17,18}.» Und{19} [niemand]{20} [wagte]{22} [mehr]{21}, [ihn]{23} [zu fragen]{24}.",
 "MRK.12.35": "Und{1} [Jesus]{3,4} [nahm das Wort]{2} [und sagte]{5}, [als er]{6} [im]{7,8} [Tempel]{9} [lehrte]{6}: «[Wie]{10} [können]{11} [die]{12} [Schriftgelehrten]{13} [sagen]{11}, [dass]{14} [der]{15} [Christus]{16} [Davids]{18} [Sohn]{17} [ist]{19}?",
 "MRK.12.36": "[David]{2} [selbst]{1} [hat]{3} [im]{4,5} [Heiligen]{7,8} [Geist]{6} [gesagt]{3}: ‹[Der Herr]{10} [sprach]{9} [zu]{11} [meinem]{13} [Herrn]{12}: [Setze dich]{14} [zu]{15} [meiner]{17} [Rechten]{16}, [bis]{18,19} [ich]{20} [deine]{21,23} [Feinde]{22} [unter]{24} [deine]{25,27} [Füsse]{26} [lege]{20}.›",
 "MRK.12.37": "[David]{2} [selbst]{1} [nennt]{3} [ihn]{4} [Herr]{5}; und{6} [woher]{7} kommt es, [dass er]{9} [sein]{8} [Sohn]{10} [ist]{9}?» Und{11} [die]{12} [grosse]{13} [Menge]{14} [hörte]{15} [ihm]{16} [gern]{17} [zu]{15}.",
 "MRK.12.38": "Und{1} [in]{2} [seiner]{3,5} [Lehre]{4} [sagte er]{6}: «[Hütet euch]{7} [vor]{8} [den]{9} [Schriftgelehrten]{10}, [die]{11} [es lieben]{12}, [in]{13} [langen Gewändern]{14} [umherzugehen]{15}, und{16} [die Begrüssungen]{17} [auf]{18} [den]{19} [Marktplätzen]{20}",
 "MRK.12.39": "und{1} [die Ehrensitze]{2} [in]{3} [den]{4} [Synagogen]{5} und{6} [die Ehrenplätze]{7} [bei]{8} [den]{9} [Gastmählern]{10};",
 "MRK.12.40": "[die]{1} [die Häuser]{3,4} [der]{5} [Witwen]{6} [auffressen]{2} und{7} [zum Schein]{8} [lange]{9} [beten]{10}: [Die]{11} [werden]{12} [ein umso härteres]{13} [Urteil]{14} [empfangen]{12}.»",
 "MRK.12.41": "Und{1} [er setzte sich]{2} [gegenüber]{3} [dem]{4} [Opferkasten]{5} [und sah zu]{6}, [wie]{7} [die]{8} [Menge]{9} [Kupfergeld]{11} [in]{12} [den]{13} [Opferkasten]{14} [warf]{10}; und{15} [viele]{16} [Reiche]{17} [warfen]{18} [viel]{19} [ein]{18}.",
 "MRK.12.42": "Und{1} [es kam]{2} [eine]{3} [arme]{5} [Witwe]{4} [und warf]{6} [zwei]{8} [Lepta]{7} [ein]{6}, [das]{9} [ist]{10} [ein Quadrans]{11}.",
 "MRK.12.43": "Und{1} [er rief]{2} [seine]{3,5} [Jünger]{4} [herbei]{2} [und sagte]{6} [zu ihnen]{7}: «[Amen]{8}, [ich sage]{9} [euch]{10}: [Diese]{14} [arme]{15,16} [Witwe]{12,13} [hat]{19} [mehr]{17} [eingeworfen]{19} [als alle]{18}, [die]{20} [in]{22} [den]{23} [Opferkasten]{24} [einwerfen]{21}. ~11(ὅτι leitet die Rede ein)",
 "MRK.12.44": "[Denn]{2} [alle]{1} [haben]{7} [von]{3} [ihrem]{4,6} [Überfluss]{5} [eingeworfen]{7}; [sie]{8} [aber]{9} [hat]{17} [aus]{10} [ihrem]{11,13} [Mangel]{12} [alles]{14} [eingeworfen]{17}, [was]{15} [sie hatte]{16}, [ihren]{19,21} [ganzen]{18} [Lebensunterhalt]{20}.»",
 # ------------------------------------------------------------ Kapitel 13
 "MRK.13.1": "Und{1} [als er]{3} [aus]{4} [dem]{5} [Tempel]{6} [hinausging]{2}, [sagt]{7} [einer]{9} [seiner]{10,12} [Jünger]{11} [zu ihm]{8}: «[Lehrer]{13}, [sieh]{14}, [was für]{15} [Steine]{16} und{17} [was für]{18} [Bauten]{19}!»",
 "MRK.13.2": "Und{1} [Jesus]{2,3} [sagte]{4} [zu ihm]{5}: «[Siehst du]{6} [diese]{7,8} [grossen]{9} [Bauten]{10}? [Hier]{14} [wird]{13} [kein]{11,12} [Stein]{15} [auf]{16} [dem anderen]{17} [gelassen]{13}, [der]{18} [nicht]{19,20} [abgebrochen wird]{21}.»",
 "MRK.13.3": "Und{1} [als er]{3} [auf]{4} [dem]{5} [Ölberg]{6-8} [sass]{2}, [gegenüber]{9} [dem]{10} [Tempel]{11}, [fragten]{12} [ihn]{13} [Petrus]{16} und{17} [Jakobus]{18} und{19} [Johannes]{20} und{21} [Andreas]{22} [für sich allein]{14,15}:",
 "MRK.13.4": "«[Sag]{1} [uns]{2}: [Wann]{3} [wird]{5} [das]{4} [geschehen]{5}, und{6} [was]{7} ist [das]{8} [Zeichen]{9}, [wenn]{10} [das]{12} [alles]{14} [sich vollenden]{13} [soll]{11}?»",
 "MRK.13.5": "[Jesus]{1,3} [aber]{2} [fing an]{4}, [zu ihnen]{6} [zu sagen]{5}: «[Seht zu]{7}, [dass niemand]{8,9} [euch]{10} [irreführt]{11}!",
 "MRK.13.6": "[Viele]{1} [werden]{2} [unter]{3} [meinem]{4,6} [Namen]{5} [kommen]{2} [und sagen]{7}: ‹[Ich]{9} [bin es]{10}›, und{11} [sie werden]{13} [viele]{12} [irreführen]{13}. ~8(ὅτι leitet die Rede ein)",
 "MRK.13.7": "[Wenn]{1} [ihr]{3} [aber]{2} [von Kriegen]{4} und{5} [Kriegsgerüchten]{6,7} [hört]{3}, [lasst euch]{9} [nicht]{8} [erschrecken]{9}. [Es muss]{10} [geschehen]{11}, [aber]{12} [das]{14} [Ende]{15} ist [noch nicht]{13} da.",
 "MRK.13.8": "[Denn]{2} [es wird sich]{1} [Volk]{3} [gegen]{4} [Volk]{5} [erheben]{1} und{6} [Reich]{7} [gegen]{8} [Reich]{9}; [es wird]{10} [Erdbeben]{11} [geben]{10} [an]{12} [vielen Orten]{13}, [es wird]{14} [Hungersnöte]{15} [geben]{14}. [Das]{18} ist [der Anfang]{16} [der Wehen]{17}.",
 "MRK.13.9": "[Ihr]{3} [aber]{2}, [gebt acht]{1} [auf euch selbst]{4}! [Man wird]{5} [euch]{6} [an]{7} [Gerichte]{8} [ausliefern]{5}, und{9} [in]{10} [Synagogen]{11} [werdet ihr geschlagen werden]{12}, und{13} [vor]{14} [Statthalter]{15} und{16} [Könige]{17} [werdet ihr gestellt werden]{18} [um meinetwillen]{19,20}, [ihnen]{23} [zum]{21} [Zeugnis]{22}.",
 "MRK.13.10": "Und{1} [unter]{2} [allen]{3} [Völkern]{4,5} [muss]{7} [zuerst]{6} [das]{9} [Evangelium]{10} [verkündigt werden]{8}.",
 "MRK.13.11": "Und{1} [wenn]{2} [man]{3} [euch]{4} [abführt]{3} [und ausliefert]{5}, [sorgt euch]{7} [nicht]{6} [im Voraus]{7} [darum, was]{8} [ihr reden sollt]{9}; [sondern]{10} [was]{11,12} [euch]{14} [in]{15} [jener]{16,17} [Stunde]{18} [gegeben wird]{13}, [das]{19} [redet]{20}. [Denn]{22} [nicht]{21} [ihr]{24} [seid]{23} [es]{25}, [die reden]{26}, [sondern]{27} [der]{28} [Heilige]{30,31} [Geist]{29}.",
 "MRK.13.12": "Und{1} [es wird]{2} [ein Bruder]{3} [den Bruder]{4} [in den]{5} [Tod]{6} [ausliefern]{2} und{7} [ein Vater]{8} [das Kind]{9}, und{10} [Kinder]{12} [werden sich]{11} [gegen]{13} [Eltern]{14} [erheben]{11} und{15} [sie]{17} [in den Tod schicken]{16}.",
 "MRK.13.13": "Und{1} [ihr werdet]{2} [von]{4} [allen]{5} [gehasst]{3} [sein]{2} [wegen]{6} [meines]{7,9} [Namens]{8}. [Wer]{10} [aber]{11} [bis]{13} [ans Ende]{14} [standhält]{12}, [der]{15} [wird gerettet werden]{16}.",
 "MRK.13.14": "[Wenn]{1} [ihr]{3} [aber]{2} [den]{4} [Gräuel]{5} [der]{6} [Verwüstung]{7} [dort stehen]{8} [seht]{3}, [wo]{9} er [nicht]{10} [darf]{11} – [wer es liest]{12,13}, [der merke auf]{14}! –, [dann]{15} [sollen]{20} [die]{16} [in]{17} [Judäa]{18,19} [in]{21} [die]{22} [Berge]{23} [fliehen]{20}.",
 "MRK.13.15": "[Wer]{1} [auf]{2} [dem]{3} [Dach]{4} ist, [steige]{6} [nicht]{5} [hinab]{6} [und gehe]{8} [nicht]{7} [hinein]{8}, um [etwas]{9} [aus]{11} [seinem]{12,14} [Haus]{13} [zu holen]{10};",
 "MRK.13.16": "und{1} [wer]{2} [auf]{3} [dem]{4} [Feld]{5} ist, [kehre]{7} [nicht]{6} [zurück]{8-10}, um [seinen]{12,14} [Mantel]{13} [zu holen]{11}.",
 "MRK.13.17": "[Wehe]{1} [aber]{2} [den]{3} [Schwangeren]{4-6} und{7} [den]{8} [Stillenden]{9} [in]{10} [jenen]{11,12} [Tagen]{13}!",
 "MRK.13.18": "[Betet]{1} [aber]{2}, [dass]{3} [es]{5} [nicht]{4} [im Winter]{6} [geschieht]{5}.",
 "MRK.13.19": "[Denn]{2} [jene]{3,5} [Tage]{4} [werden]{1} [eine Bedrängnis]{6} [sein]{1}, [wie]{7} [es]{9} [keine]{8} [solche]{10} [gegeben hat]{9} [vom]{11} [Anfang]{12} [der Schöpfung]{13}, [die]{14} [Gott]{16,17} [geschaffen hat]{15}, [bis]{18} [jetzt]{19,20}, und{21} [auch nie]{22,23} [geben wird]{24}.",
 "MRK.13.20": "Und{1} [wenn]{2} [der Herr]{5} [die]{6} [Tage]{7} [nicht]{3} [verkürzt hätte]{4}, [würde]{9} [kein]{8} [Mensch]{11,12} [gerettet]{10} werden; [aber]{13} [um]{14} [der]{15} [Auserwählten]{16} [willen]{14}, [die]{17} [er erwählt hat]{18}, [hat er]{19} [die]{20} [Tage]{21} [verkürzt]{19}.",
 "MRK.13.21": "Und{1} [wenn]{3} [dann]{2} [jemand]{4} [zu euch]{5} [sagt]{6}: ‹[Sieh]{7}, [hier]{8} ist [der]{9} [Christus]{10}! [Sieh]{11}, [dort]{12}!›, [glaubt es]{14} [nicht]{13}!",
 "MRK.13.22": "[Denn]{2} [es werden]{1} [falsche Christusse]{3} und{4} [falsche Propheten]{5} [auftreten]{1} und{6} [Zeichen]{8} und{9} [Wunder]{10} [tun]{7}, [um]{11,12} [wenn]{14} [möglich]{15} [die]{16} [Auserwählten]{17} [irrezuführen]{13}.",
 "MRK.13.23": "[Ihr]{1} [aber]{2}, [seht euch vor]{3}! [Ich habe]{4} [euch]{5} [alles]{6} [vorausgesagt]{4}.",
 "MRK.13.24": "[Aber]{1} [in]{2} [jenen]{3,4} [Tagen]{5}, [nach]{6} [jener]{7,9} [Bedrängnis]{8}, [wird]{12} [die]{10} [Sonne]{11} [verfinstert werden]{12}, und{13} [der]{14} [Mond]{15} [wird]{17} [seinen]{18,20} [Schein]{19} [nicht]{16} [geben]{17},",
 "MRK.13.25": "und{1} [die]{2} [Sterne]{3} [werden]{4} [vom]{5,6} [Himmel]{7} [fallen]{8}, und{9} [die]{10} [Mächte]{11} [im]{12-14} [Himmel]{15} [werden erschüttert werden]{16}.",
 "MRK.13.26": "Und{1} [dann]{2} [werden sie]{3} [den]{4} [Menschensohn]{5-7} [kommen]{8} [sehen]{3} [in]{9} [Wolken]{10} [mit]{11} [grosser]{13} [Macht]{12} und{14} [Herrlichkeit]{15}.",
 "MRK.13.27": "Und{1} [dann]{2} [wird er]{3} [die]{4} [Engel]{5} [aussenden]{3} und{6} [die]{8} [Auserwählten]{9} [sammeln]{7} [aus]{10} [den]{11} [vier]{12} [Winden]{13}, [vom]{14} [Ende]{15} [der Erde]{16} [bis]{17} [zum Ende]{18} [des Himmels]{19}.",
 "MRK.13.28": "[Vom]{1,3} [Feigenbaum]{4} [aber]{2} [lernt]{5} [das]{6} [Gleichnis]{7}: [Sobald]{8} [sein]{10,12} [Zweig]{11} [schon]{9} [zart]{13} [wird]{14} und{15} [die]{17} [Blätter]{18} [treibt]{16}, [erkennt ihr]{19}, [dass]{20} [der]{22} [Sommer]{23} [nahe]{21} [ist]{24}.",
 "MRK.13.29": "[So]{1} [auch]{2} [ihr]{3}: [Wenn]{4} [ihr]{5} [das]{6} [geschehen]{7} [seht]{5}, [erkennt]{8}, [dass]{9} [es]{11} [nahe]{10} [vor]{12} [der Tür]{13} [ist]{11}.",
 "MRK.13.30": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Dieses]{8,10} [Geschlecht]{9} [wird]{7} [nicht]{5,6} [vergehen]{7}, [bis]{11,12} [das]{13} [alles]{14} [geschieht]{15}. ~4(ὅτι leitet die Rede ein)",
 "MRK.13.31": "[Der]{1} [Himmel]{2} und{3} [die]{4} [Erde]{5} [werden vergehen]{6}, [meine]{7,10} [Worte]{9} [aber]{8} [werden]{13} [nicht]{11,12} [vergehen]{13}.",
 "MRK.13.32": "[Von]{1} [jenem]{3,5} [Tag]{4} [aber]{2} [oder]{6} [der]{7} [Stunde]{8} [weiss]{10} [niemand]{9}, [auch nicht]{11} [die]{12} [Engel]{13} [im]{14} [Himmel]{15}, [auch nicht]{16} [der]{17} [Sohn]{18}, [nur]{19,20} [der]{21} [Vater]{22}.",
 "MRK.13.33": "[Seht euch vor]{1}, [bleibt wach]{2}! [Denn]{5} [ihr wisst]{4} [nicht]{3}, [wann]{6} [die]{7} [Zeit]{8} [da ist]{9}.",
 "MRK.13.34": "[Es ist wie]{1} [bei einem Menschen]{2}, [der verreist ist]{3}: [Er hat]{4} [sein]{5,7} [Haus]{6} [verlassen]{4} und{8} [seinen]{10,12} [Knechten]{11} [die]{13} [Vollmacht]{14} [gegeben]{9}, [jedem]{15} [seine]{16,18} [Arbeit]{17}, und{19} [dem]{20} [Türhüter]{21} [hat er befohlen]{22}, [dass]{23} [er wachen soll]{24}.",
 "MRK.13.35": "[Wacht]{1} [also]{2}! [Denn]{5} [ihr wisst]{4} [nicht]{3}, [wann]{6} [der]{7} [Herr]{8} [des]{9} [Hauses]{10} [kommt]{11}: [ob]{12} [am Abend]{13} [oder]{14} [um Mitternacht]{15} [oder]{16} [beim Hahnenschrei]{17} [oder]{18} [am frühen Morgen]{19},",
 "MRK.13.36": "[damit]{1} [er]{4}, [wenn er]{2} [plötzlich]{3} [kommt]{2}, [euch]{5} [nicht]{1} [schlafend]{6} [findet]{4}.",
 "MRK.13.37": "[Was]{1} [ich]{4} [aber]{2} [euch]{3} [sage]{4}, [das sage ich]{6} [allen]{5}: [Wacht]{7}!»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 11
 "MRK.11.1": "Und{1} [wo]{2} [si]{3} [i d Nöchi vo]{4} [Jerusalem]{5} [chömed]{3}, [uf]{6} Betfage{7} und{8} Betanie{9} [am]{10,11} [Ölberg]{12-14}, [schickt]{15} er [zwei]{16} [vo sine]{17,19} [Jünger]{18} [los]{15}",
 "MRK.11.2": "und{1} [seit]{2} [zu ine]{3}: «[Gönd]{4} [i]{5} [das]{6} [Dorf]{7}, [wo]{8} [vor]{9} [eu]{10} liit; und{11} [grad]{12}, [wänn ir]{13} [ine]{14,15} [chömed]{13}, [wärded ir]{16} [es Füli]{17} [aabunde]{18} [finde]{16}, [wo]{19,20} [no]{22} [nie]{21} [en Mänsch]{23} [druf]{19,20} [gsässe isch]{24}. [Binded]{25} [s]{26} [los]{25} und{27} [bringed]{28} s!",
 "MRK.11.3": "Und{1} [wänn]{2} [öpper]{3} [zu eu]{4} [seit]{5}: ‹[Was]{6} [mached ir]{7} [da]{8}?›, [dänn säged]{9}: ‹[De]{11} [Herr]{12} [bruucht]{14,15} [s]{13}, und{16} [er schickt]{19} [s]{18} [grad]{17} [wider]{20} [da häre]{21}.›» ~10(ὅτι leitet die Rede ein)",
 "MRK.11.4": "Und{1} [si sind ane gange]{2} und{3} [händ]{4} [es Füli]{5} [gfunde]{4}, [aabunde]{6} [a]{7} [ere Tür]{8} [dusse]{9} [a]{10} [de]{11} [Strass]{12}, und{13} [si binded]{14} [s]{15} [los]{14}.",
 "MRK.11.5": "Und{1} [es paar]{2}, [wo]{3} [det]{4} [gstande sind]{5}, [händ]{6} [zu ine]{7} [gseit]{6}: «[Was]{8} [mached ir]{9} da? [Ir binded]{10} [s]{11} [Füli]{12} [los]{10}?»",
 "MRK.11.6": "[Si]{1} [aber]{2} [händ]{3} [zu ine]{4} [gseit]{3}, [wie s]{5} [de Jesus]{7,8} [gseit hät]{6}; und{9} [mer hät]{10} [si]{11} [la mache]{10}.",
 "MRK.11.7": "Und{1} [si bringed]{2} [s]{3} [Füli]{4} [zum]{5,6} [Jesus]{7} und{8} [leged]{9} [em]{10} [iri]{13} [Mäntel]{11,12} [uf]{9}, und{14} [er hät sich]{15} [druf]{16,17} [gsetzt]{15}.",
 "MRK.11.8": "Und{1} [vil]{2} [händ]{6} [iri]{5} [Mäntel]{3,4} [uf]{7} [de]{8} [Wäg]{9} [usbreitet]{6}, [anderi]{10} [aber]{11} [Zweig]{12}, [wo si]{13} [uf]{14} [de]{15} [Fälder]{16} [abghaue händ]{13}.",
 "MRK.11.9": "Und{1} [die, wo]{2} [voruusgange sind]{3}, und{4} [die, wo]{5} [nachecho sind]{6}, [händ]{7} [grüeft]{7}: «[Hosanna]{8}! [Gsägnet sig]{9} [dä]{10}, wo [chunnt]{11} [im]{12} [Name]{13} [vom Herr]{14}!",
 "MRK.11.10": "[Gsägnet sig]{1} [s]{2} [Riich]{4} [vo üsem]{5,7} [Vatter]{6} [David]{8}, [wo chunnt]{3}! [Hosanna]{9} [i]{10} [de]{11} [Höchi]{12}!»",
 "MRK.11.11": "Und{1} [er isch]{2} [uf]{3} [Jerusalem]{4} [choo]{2}, [in]{5,6} [Tämpel]{7}; und{8} [nachdem er]{9} [alles]{10} [rundum aagluegt hät]{9}, [isch er]{16}, [wil]{13} [s]{14,15} [scho]{12} [spaat]{11} [gsii isch]{13}, [mit]{19} [de]{20} [Zwölf]{21} [use]{16} [uf]{17} [Betanie]{18} [gange]{16}.",
 "MRK.11.12": "Und{1} [am]{2} [nächschte Tag]{3}, [wo]{4} [si]{5} [vo]{6} [Betanie]{7} [furt sind]{4}, [hät er Hunger gha]{8}.",
 "MRK.11.13": "Und{1} [wo er]{2} [vo]{4} [wiitem]{5} [en Fiigebaum]{3} [gseh hät]{2}, [wo]{6} [Bletter]{7} [gha hät]{6}, [isch er ane gange]{8}, [öb]{9} [er]{12} [villicht]{10} [öppis]{11} [dra]{13,14} [findi]{12}. Und{15} [wo er]{16} [zu]{17} [em]{18} [choo isch]{16}, [hät er]{20} [nüt]{19} [gfunde]{20} [usser]{21,22} [Bletter]{23}; [dänn]{25} [es isch]{28} [nöd]{27} [d]{24} [Ziit]{26} [für Fiige]{29} [gsii]{28}.",
 "MRK.11.14": "Und{1} [druf abe]{2} [hät er]{3} [zu em]{4} [gseit]{3}: «[Nie meh]{5} [i]{6} [Ewigkeit]{7,8} [söll]{13} [öpper]{11} [vo]{9} [dir]{10} [Frucht]{12} [ässe]{13}!» Und{14} [sini]{18} [Jünger]{16,17} [händ das ghört]{15}.",
 "MRK.11.15": "Und{1} [si chömed]{2} [uf]{3} [Jerusalem]{4}. Und{5} [er isch]{6} [in]{7,8} [Tämpel]{9} [ine gange]{6} und [hät aagfange]{10}, [d]{12} [Verchäufer]{13} und{14} [d]{15} [Chäufer]{16} [im]{17,18} [Tämpel]{19} [usezjage]{11}; und{20} [d]{21} [Tisch]{22} [vo de]{23} [Gältwächsler]{24} und{25} [d]{26} [Stüel]{27} [vo de]{28} [Tuubeverchäufer]{29-31} [hät er umgschmisse]{32},",
 "MRK.11.16": "und{1} [er hät]{3} [nöd]{2} [zueglaa]{3}, [dass]{4} [öpper]{5} [es Grät]{7} [dur]{8} [de]{9} [Tämpel]{10} [treit]{6}.",
 "MRK.11.17": "Und{1} [er hät glehrt]{2} und{3} [zu ine]{5} [gseit]{4}: «[Staat]{7} [nöd]{6} [gschribe]{7}: ‹[Mis]{11} [Huus]{9,10} [söll]{14} [es Huus]{12} [zum Bätte]{13} [heisse]{14} [für alli]{15} [Völker]{16,17}›? [Ir]{18} [aber]{19} [händ]{20} [e Röiberhöli]{22,23} [drus]{21} [gmacht]{20}!» ~8(ὅτι leitet das Zitat ein)",
 "MRK.11.18": "Und{1} [d]{3} [Hoheprieschter]{4} und{5} [d]{6} [Schriftgleerte]{7} [händ das ghört]{2} und{8} [händ gsuecht]{9}, [wie]{10} [si]{12} [en]{11} [chönnted umbringe]{12}; [dänn]{14} [si händ Angscht gha]{13} [vor ihm]{15}, [dänn]{17} [di]{18} [ganz]{16} [Mängi]{19} [isch überwältiget gsii]{20} [vo]{21} [sinere]{22,24} [Lehr]{23}.",
 "MRK.11.19": "Und{1} [wänn]{2} [s]{4} [Aabig]{3} [worde isch]{4}, [sind si]{5} [zur]{6,7} [Stadt]{8} [us gange]{5}.",
 "MRK.11.20": "Und{1} [wo si]{2} [am Morge früe]{3} [verbii choo sind]{2}, [händ si]{4} [de]{5} [Fiigebaum]{6} [gseh]{4}, [vo]{8} [de Wurzle]{9} [här]{8} [verdorret]{7}.",
 "MRK.11.21": "Und{1} [de Petrus]{3,4} [bsinnt sich]{2} und [seit]{5} [zu ihm]{6}: «[Rabbi]{7}, [lueg]{8}, [de]{9} [Fiigebaum]{10}, [wo]{11} [du verfluecht häsch]{12}, [isch verdorret]{13}!»",
 "MRK.11.22": "Und{1} [de Jesus]{3,4} [antwortet]{2} und [seit]{5} [zu ine]{6}: «[Händ]{7} [Glaube]{8} [a Gott]{9}!",
 "MRK.11.23": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Wär]{5,6} [zu]{8} [dem]{10} [Bärg]{9} [seit]{7}: ‹[Heb di uf]{11} und{12} [stürz di]{13} [is]{14,15} [Meer]{16}!›, und{17} [nöd]{18} [zwiiflet]{19} [i]{20} [sim]{21,23} [Härz]{22}, [sondern]{24} [glaubt]{25}, [dass]{26} [passiert]{29}, [was]{27} [er seit]{28}, [dem]{31} [wird s zueteil]{30}. ~4(ὅτι leitet die Rede ein)",
 "MRK.11.24": "[Drum]{1,2} [säg ich]{3} [eu]{4}: [Alles]{5}, [wo]{6} [ir drum bättet]{7} und{8} [bittet]{9} – [glaubed]{10}, [dass]{11} [ir s übercho händ]{12}, und{13} [es wird]{14} [eu]{15} [zueteil]{14}.",
 "MRK.11.25": "Und{1} [wänn]{2} [ir dastönd]{3} [und bättet]{4}, [dänn vergänd]{5}, [wänn]{6} [ir]{8} [öppis]{7} [gäge]{9} [öpper]{10} [händ]{8}, [demit]{11} [au]{12} [eue]{13,15} [Vatter]{14} [im]{16-18} [Himmel]{19} [eu]{21} [eui]{22,24} [Verfehlige]{23} [vergit]{20}.»",
 "MRK.11.27": "Und{1} [si chömed]{2} [wider]{3} [uf]{4} [Jerusalem]{5}. Und{6} [während]{10} [er]{11} [im]{7,8} [Tämpel]{9} [umelauft]{10}, [chömed]{12} [d]{15} [Hoheprieschter]{16} und{17} [d]{18} [Schriftgleerte]{19} und{20} [d]{21} [Ältischte]{22} [zu]{13} [ihm]{14}",
 "MRK.11.28": "und{1} [händ]{2} [zu ihm]{3} [gseit]{2}: «[Mit]{4} [was für ere]{5} [Vollmacht]{6} [machsch du]{8} [das]{7}? [Oder]{9} [wär]{10} [hät]{12} [dir]{11} [die]{13,15} [Vollmacht]{14} [gää]{12}, [dass]{16} [du]{18} [das]{17} [machsch]{18}?»",
 "MRK.11.29": "[De Jesus]{1,3} [aber]{2} [hät]{4} [zu ine]{5} [gseit]{4}: «[Ich frög]{6} [eu]{7} [öppis]{8,9}, und{10} [gänd]{11} [mir]{12} [Antwort]{11}, und{13} [dänn säg ich]{14} [eu]{15}, [mit]{16} [was für ere]{17} [Vollmacht]{18} [ich]{20} [das]{19} [mache]{20}.",
 "MRK.11.30": "[D]{1} [Taufi]{2} [vom]{3} [Johannes]{4}: [Isch]{7} si [vom]{5} [Himmel]{6} [gsii]{7} [oder]{8} [vo]{9} [Mänsche]{10}? [Gänd]{11} [mir]{12} [Antwort]{11}!»",
 "MRK.11.31": "Und{1} [si händ]{2} [mitenand]{3,4} [hin und här überleit]{2} [und gseit]{5}: «[Was]{6} [söled mer säge]{7}? [Wänn]{8} [mer säged]{9}: ‹[Vom]{10} [Himmel]{11}›, [dänn seit er]{12}: ‹[Werum]{13,14} [händ ir]{17} [em]{18} [dänn]{15} [nöd]{16} [glaubt]{17}?›",
 "MRK.11.32": "[Söled mer]{2} [aber]{1} [säge]{2}: ‹[Vo]{3} [Mänsche]{4}›?» – [Si händ Angscht gha]{5} [vor de]{6} [Mängi]{7}; [dänn]{9} [alli]{8} [händ]{10} [vom Johannes]{11,12} [gmeint]{10}, [dass]{14} [er]{16} [würkli]{13} [en Prophet]{15} [gsii sig]{16}.",
 "MRK.11.33": "Und{1} [si gänd]{2} [em Jesus]{3,4} [zur Antwort]{2} [und säged]{5}: «[Mir wüssed s]{7} [nöd]{6}.» Und{8} [de Jesus]{9,10} [seit]{11} [zu ine]{12}: «[Dänn säg]{15} [au]{13} [ich]{14} [eu]{16} [nöd]{13}, [mit]{17} [was für ere]{18} [Vollmacht]{19} [ich]{21} [das]{20} [mache]{21}.»",
 # ------------------------------------------------------------ Kapitel 12
 "MRK.12.1": "Und{1} [er hät aagfange]{2}, [i]{4} [Gliichnis]{5} [zu ine]{3} [z rede]{6}: «[En Wiibärg]{7} [hät]{9} [en Mänsch]{8} [aapflanzt]{9}, und{10} [er hät]{11} [en Haag]{12} [drum ume gmacht]{11}, und{13} [hät]{14} [e Trottegrueb]{15} [usghobe]{14}, und{16} [hät]{17} [en Turm]{18} [baut]{17}, und{19} [hät]{20} [en]{21} [a Wiibuure]{22} [verpachtet]{20}, und{23} [isch verreist]{24}.",
 "MRK.12.2": "Und{1} [er hät]{2} [zur]{6} [richtige Ziit]{7} [en Chnächt]{8} [zu]{3} [de]{4} [Wiibuure]{5} [gschickt]{2}, [demit er]{9} [vo]{10} [de]{11} [Wiibuure]{12} [sin Teil a]{14} [de]{15} [Frücht]{16} [vom]{17} [Wiibärg]{18} [chönn hole]{13}.",
 "MRK.12.3": "Und{1} [si händ]{2} [en]{3} [packt]{2}, [verprüglet]{4} und{5} [mit lääre Händ]{7} [furtgschickt]{6}.",
 "MRK.12.4": "Und{1} [wider]{2} [hät er]{3} [en andere]{6} [Chnächt]{7} [zu]{4} [ine]{5} [gschickt]{3}; [au dä]{8} [händ si uf de Chopf gschlage]{9} und{10} [beschimpft]{11}.",
 "MRK.12.5": "Und{1} [en andere]{2} [hät er gschickt]{3}; [au dä]{4} [händ si umbracht]{5}; und{6} so [vil]{7} [anderi]{8}: [di einte]{9,10} [händ si verprüglet]{11}, [di andere]{12,13} [umbracht]{14}.",
 "MRK.12.6": "[No]{1} [eine]{2} [hät er gha]{3}, [en gliebte]{5} [Sohn]{4}. [Dä]{7} [hät er]{6} [als Letschte]{8} [zu]{9} [ine]{10} [gschickt]{6} [und sich gseit]{11}: ‹[Vor mim]{14,16} [Sohn]{15} [händ si dänn Respekt]{13}.› ~12(ὅτι leitet die Rede ein)",
 "MRK.12.7": "[Die]{1} [Wiibuure]{3,4} [aber]{2} [händ]{7} [zunenand]{5,6} [gseit]{7}: ‹[Das]{9} [isch]{10} [de]{11} [Erb]{12}; [chömed]{13}, [mir bringed]{14} [en]{15} [um]{14}, und{16} [s]{19} [Erb]{20} [ghört]{18} [üs]{17}!› ~8(ὅτι leitet die Rede ein)",
 "MRK.12.8": "Und{1} [si händ]{3} [en]{4} [packt]{2} [und umbracht]{3} und{5} [en]{7} [us]{8} [em]{9} [Wiibärg]{10} [usegworfe]{6}.",
 "MRK.12.9": "[Was]{1} [wird]{2} [de]{3} [Herr]{4} [vom]{5} [Wiibärg]{6} [mache]{2}? [Er wird choo]{7} und{8} [d]{10} [Wiibuure]{11} [umbringe]{9} und{12} [de]{14} [Wiibärg]{15} [andere]{16} [gää]{13}.",
 "MRK.12.10": "[Händ ir]{5} [nöd emal]{1} [die]{2,4} [Schriftstell]{3} [gläse]{5}: ‹[De Stei]{6}, [wo]{7} [d]{9} [Buulüüt]{10} [verworfe händ]{8}, [dä]{11} [isch]{12} [zum]{13} [Eckstei]{14,15} [worde]{12};",
 "MRK.12.11": "[vom]{1} [Herr]{2} [isch]{3} [das]{4} [gscheh]{3}, und{5} [es isch]{6} [wunderbar]{7} [i]{8} [üsne]{10} [Auge]{9}›?»",
 "MRK.12.12": "Und{1} [si händ probiert]{2}, [en]{3} [feschtznää]{4}, und{5} [händ Angscht gha vor]{6} [de]{7} [Mängi]{8}; [dänn]{10} [si händ gmerkt]{9}, [dass]{11} [er]{16} [s]{14} [Gliichnis]{15} [gäge]{12} [si]{13} [verzellt hät]{16}. Und{17} [si händ]{18} [en]{19} [la staa]{18} [und sind gange]{20}.",
 "MRK.12.13": "Und{1} [si schicked]{2} [es paar]{5} [vo de]{6} [Pharisäer]{7} und{8} [vo de]{9} [Herodianer]{10} [zu]{3} [ihm]{4}, [demit si]{11} [en]{12} [mit ere Ussag]{14} [chönd fange]{13}.",
 "MRK.12.14": "Und{1} [si chömed]{2} [und säged]{3} [zu ihm]{4}: «[Lehrer]{5}, [mir wüssed]{6}, [dass]{7} [du]{9} [ufrichtig]{8} [bisch]{9} und{10} [di]{13} [um niemer]{11,14,15} [kümmersch]{12}; [dänn]{17} [du luegsch nöd uf s Aaseh]{16,18,19,20:idiom} [vo de Mänsche]{21}, [sondern]{22} [lehrsch]{29} [de]{25} [Wäg]{26} [vo Gott]{27,28} [i]{23} [Wahrheit]{24}. [Isch es erlaubt]{30}, [em Kaiser]{33} [Stüür]{32} [z zale]{31}, [oder]{34} [nöd]{35}? [Söled mer zale]{36} [oder]{37} [nöd]{38} [zale]{39}?»",
 "MRK.12.15": "[Er]{1} [aber]{2} [hät]{3} [iri]{4,5} [Heuchlerei]{6} [duureschaut]{3} [und]{7} [zu ine]{8} [gseit]{7}: «[Was]{9} [stelled ir]{11} [mich]{10} [uf d Prob]{11}? [Bringed]{12} [mir]{13} [en Denar]{14}, [demit]{15} [ich en gseh]{16}.»",
 "MRK.12.16": "[Si]{1} [aber]{2} [händ eine bracht]{3}. Und{4} [er seit]{5} [zu ine]{6}: «[Wäm sis]{7} [Bild]{8,9} und{11} [Ufschrift]{12,13} [isch das]{10}?» [Si]{14} [aber]{15} [händ]{16} [zu ihm]{17} [gseit]{16}: «[Vom Kaiser]{18}.»",
 "MRK.12.17": "[De Jesus]{1,3} [aber]{2} [hät]{4} [zu ine]{5} [gseit]{4}: «[Was]{6} [em Kaiser]{7} ghört, [gänd]{8} [em Kaiser]{9}, und{10} [was]{11} [Gott]{12,13} ghört, [Gott]{14,15}!» Und{16} [si händ]{17} [über]{18} [ihn]{19} [nu gstuunt]{17}.",
 "MRK.12.18": "Und{1} [es chömed]{2} [Sadduzäer]{3} [zu]{4} [ihm]{5}, [wo]{6} [säged]{7}, [es geb]{10} [kei]{9} [Uferstehig]{8}, und{11} [si händ]{12} [en]{13} [gfröget]{12} [und gseit]{14}:",
 "MRK.12.19": "«[Lehrer]{1}, [de Mose]{2} [hät]{3} [üs]{4} [gschribe]{3}: [Wänn]{6} [öpperem sin]{7} [Brueder]{8} [stirbt]{9} und{10} [e Frau]{12} [hinderlaat]{11} und{13} [kei]{14} [Chind]{16} [hinderlaat]{15}, [dänn söll]{17} [sin]{21} [Brueder]{19,20} [d]{22} [Frau]{23} [nää]{18} und{24} [sim]{27,29} [Brueder]{28} [Nachkomme]{26} [verschaffe]{25}. ~5(ὅτι leitet das Zitat ein)",
 "MRK.12.20": "[Es sind]{3} [sibe]{1} [Brüeder]{2} [gsii]{3}. Und{4} [de]{5} [erscht]{6} [hät]{7} [e Frau]{8} [gnoo]{7}, und{9} [wo er gstorbe isch]{10}, [hät er]{12} [kei]{11} [Nachkomme]{13} [hinderlaa]{12}.",
 "MRK.12.21": "Und{1} [de]{2} [zweit]{3} [hät]{4} [si]{5} [gnoo]{4} und{6} [isch gstorbe]{7}, [ohni]{8} [Nachkomme]{10} [z hinderlaa]{9}; und{11} [de]{12} [dritt]{13} [gnau gliich]{14}.",
 "MRK.12.22": "Und{1} [alli]{2} [sibe]{3} [händ]{5} [kei]{4} [Nachkomme]{6} [hinderlaa]{5}. [Als Letschti]{7} [vo allne]{8} [isch]{12} [au]{9} [d]{10} [Frau]{11} [gstorbe]{12}.",
 "MRK.12.23": "[I]{1} [de]{2} [Uferstehig]{3}, [wänn]{4} [si uferstönd]{5}: [Wäm]{6} [vo ine]{7} [ghört si]{8} [als Frau]{9}? [Dänn]{11} [alli]{10} [sibe]{12} [händ]{13} [si]{14} [zur Frau]{15} [gha]{13}.»",
 "MRK.12.24": "[De Jesus]{3,4} [hät]{1} [zu ine]{2} [gseit]{1}: «[Irred ir]{8} [nöd]{5} [drum]{6,7}, [wil ir]{10} [weder]{9} [d]{11} [Schrifte]{12} [kenned]{10} [no]{13} [d]{14} [Chraft]{15} [vo Gott]{16,17}?",
 "MRK.12.25": "[Dänn]{2} [wänn]{1} [si]{5} [vo]{3} [de Tote]{4} [uferstönd]{5}, [hürated si]{7} [weder]{6}, [no]{8} [wärded si verhüratet]{9}, [sondern]{10} [si sind]{11} [wie]{12} [Ängel]{13} [im]{14,15} [Himmel]{16}.",
 "MRK.12.26": "[Was]{1} [aber]{2} [d]{3} [Tote]{4} [betrifft]{1}, [dass]{5} [si uferweckt wärded]{6}: [Händ ir]{8} [nöd]{7} [im]{9,10} [Buech]{11} [vom Mose]{12} [gläse]{8}, [bim]{13,14} [Dornbusch]{15}, [wie]{16} [Gott]{19,20} [zu ihm]{18} [gseit hät]{17}: ‹[Ich]{22} bi [de]{23} [Gott]{24} [vom Abraham]{25} und{26} [de]{27} [Gott]{28} [vom Isaak]{29} und{30} [de]{31} [Gott]{32} [vom Jakob]{33}›? ~21(λέγων leitet das Zitat ein)",
 "MRK.12.27": "[Er isch]{2} [nöd]{1} [en Gott]{3} [vo Tote]{4}, [sondern]{5} [vo Läbige]{6}. [Ir irred]{8} [gwaltig]{7}.»",
 "MRK.12.28": "Und{1} [eine]{3} [vo de]{4} [Schriftgleerte]{5} [isch dezuecho]{2}; [er hät]{6} [si]{7} [mitenand striite]{8} [ghöre]{6} [und gseh]{9}, [dass]{10} [er]{12} [ine]{13} [guet]{11} [Antwort gää hät]{12}. [Er hät]{14} [en]{15} [gfröget]{14}: «[Weles]{16} [Gebot]{18} [isch]{17} [s erscht]{19} [vo allne]{20}?»",
 "MRK.12.29": "[De Jesus]{2,3} [hät gantwortet]{1}: «[S erscht]{5} [isch]{6}: ‹[Los]{7}, [Israel]{8}: [De Herr]{9}, [üse]{12} [Gott]{10,11}, [de Herr]{13} [isch]{15} [eine]{14}; ~4(ὅτι leitet die Rede ein)",
 "MRK.12.30": "und{1} [du söllsch]{2} [de Herr]{3}, [din]{6} [Gott]{4,5}, [liebe]{2} [mit]{7} [dim]{9,11} [ganze]{8} [Härz]{10} und{12} [mit]{13} [dinere]{15,17} [ganze]{14} [Seel]{16} und{18} [mit]{19} [dim]{21,23} [ganze]{20} [Dänke]{22} und{24} [mit]{25} [dinere]{27,29} [ganze]{26} [Chraft]{28}.›",
 "MRK.12.31": "[S zweit]{1} [isch das]{2}: ‹[Du söllsch]{3} [din]{4,6} [Nächschte]{5} [liebe]{3} [wie]{7} [di sälber]{8}.› [Grösser]{9} [als die]{10} [isch]{14} [kei]{13} [anders]{11} [Gebot]{12}.»",
 "MRK.12.32": "Und{1} [de]{4} [Schriftgleert]{5} [hät]{2} [zu ihm]{3} [gseit]{2}: «[Guet]{6}, [Lehrer]{7}! [Mit Rächt]{8,9} [häsch gseit]{10}: [Eine]{12} [isch er]{13}, und{14} [es git]{16} [kein]{15} [andere]{17} [usser]{18} [ihm]{19}. ~11(ὅτι leitet die Rede ein)",
 "MRK.12.33": "Und{1} [ihn]{4} [z liebe]{2,3} [vo]{5} [ganzem]{6} [Härze]{7,8} und{9} [mit]{10} [ganzem]{11} [Verstand]{12,13} und{14} [mit]{15} [ganzer]{16} [Chraft]{17,18} und{19} [de]{22} [Nächscht]{23} [z liebe]{20,21} [wie]{24} [sich sälber]{25}, [das isch]{27} [meh]{26} [als alli]{28} [Brandopfer]{29,30} und{31} [Schlachtopfer]{32}.»",
 "MRK.12.34": "Und{1} [wo]{4} [de Jesus]{2,3} [gseh hät]{4}, [dass]{6} [er]{5} [gschiid]{7} [gantwortet hät]{8}, [hät er]{9} [zu ihm]{10} [gseit]{9}: «[Du bisch]{13} [nöd]{11} [wiit]{12} [vom]{14,15} [Riich]{16} [vo Gott]{17,18}.» Und{19} [niemer]{20} [hät sich]{22} [meh]{21} [traut]{22}, [en]{23} [z fröge]{24}.",
 "MRK.12.35": "Und{1} [de Jesus]{3,4} [hät s Wort ergriffe]{2} [und gseit]{5}, [wo er]{6} [im]{7,8} [Tämpel]{9} [glehrt hät]{6}: «[Wie]{10} [chönd]{11} [d]{12} [Schriftgleerte]{13} [säge]{11}, [dass]{14} [de]{15} [Christus]{16} [de Sohn]{17} [vom David]{18} [isch]{19}?",
 "MRK.12.36": "[De David]{2} [sälber]{1} [hät]{3} [im]{4,5} [Heilige]{7,8} [Geischt]{6} [gseit]{3}: ‹[De Herr]{10} [hät]{9} [zu]{11} [mim]{13} [Herr]{12} [gseit]{9}: [Sitz]{14} [rächts]{15,16} [vo mir]{17}, [bis]{18,19} [ich]{20} [dini]{21,23} [Find]{22} [under]{24} [dini]{25,27} [Füess]{26} [lege]{20}.›",
 "MRK.12.37": "[De David]{2} [sälber]{1} [nännt]{3} [en]{4} [Herr]{5}; und{6} [wie]{7} chunnt s, [dass er]{9} [sin]{8} [Sohn]{10} [isch]{9}?» Und{11} [di]{12} [gross]{13} [Mängi]{14} [hät]{15} [ihm]{16} [gern]{17} [zueglost]{15}.",
 "MRK.12.38": "Und{1} [i]{2} [sinere]{3,5} [Lehr]{4} [hät er gseit]{6}: «[Nämed eu in Acht]{7} [vor]{8} [de]{9} [Schriftgleerte]{10}, [wo s gern händ]{11,12}, [i]{13} [lange Gwänder]{14} [umezlaufe]{15}, und{16} [d Grüess]{17} [uf]{18} [de]{19} [Märtplätz]{20}",
 "MRK.12.39": "und{1} [d Ehreplätz]{2} [i]{3} [de]{4} [Synagoge]{5} und{6} [di beschte Plätz]{7} [a]{8} [de]{9} [Fäschtässe]{10};",
 "MRK.12.40": "[wo]{1} [d Hüüser]{3,4} [vo de]{5} [Witwe]{6} [uffrässed]{2} und{7} [zum Schii]{8} [lang]{9} [bätted]{10}: [Die]{11} [wärded]{12} [es umso härters]{13} [Urteil]{14} [überchoo]{12}.»",
 "MRK.12.41": "Und{1} [er isch]{2} [gägenüber]{3} [vom]{4} [Opferstock]{5} [abgsässe]{2} [und hät zuegluegt]{6}, [wie]{7} [d]{8} [Mängi]{9} [Chupfergält]{11} [i]{12} [de]{13} [Opferstock]{14} [iiwirft]{10}; und{15} [vil]{16} [Riichi]{17} [händ]{18} [vil]{19} [iigworfe]{18}.",
 "MRK.12.42": "Und{1} [es isch]{2} [e]{3} [armi]{5} [Witwe]{4} [choo]{2} [und hät]{6} [zwei]{8} [Lepta]{7} [iigworfe]{6}, [das]{9} [isch]{10} [en Quadrans]{11}.",
 "MRK.12.43": "Und{1} [er hät]{2} [sini]{3,5} [Jünger]{4} [zue sich grüeft]{2} [und]{6} [zu ine]{7} [gseit]{6}: «[Amen]{8}, [ich säg]{9} [eu]{10}: [Die]{14} [armi]{15,16} [Witwe]{12,13} [hät]{19} [meh]{17} [iigworfe]{19} [als alli]{18}, [wo]{20} [i]{22} [de]{23} [Opferstock]{24} [iiwärfed]{21}. ~11(ὅτι leitet die Rede ein)",
 "MRK.12.44": "[Dänn]{2} [alli]{1} [händ]{7} [vo]{3} [irem]{4,6} [Überfluss]{5} [iigworfe]{7}; [si]{8} [aber]{9} [hät]{17} [us]{10} [irem]{11,13} [Mangel]{12} [alles]{14} [iigworfe]{17}, [was]{15} [si gha hät]{16}, [ire]{19,21} [ganz]{18} [Läbesunderhalt]{20}.»",
 # ------------------------------------------------------------ Kapitel 13
 "MRK.13.1": "Und{1} [wo er]{3} [us]{4} [em]{5} [Tämpel]{6} [use gaat]{2}, [seit]{7} [eine]{9} [vo sine]{10,12} [Jünger]{11} [zu ihm]{8}: «[Lehrer]{13}, [lueg]{14}, [was für]{15} [Stei]{16} und{17} [was für]{18} [Bauwärch]{19}!»",
 "MRK.13.2": "Und{1} [de Jesus]{2,3} [hät]{4} [zu ihm]{5} [gseit]{4}: «[Gsehsch]{6} [die]{7,8} [grosse]{9} [Bauwärch]{10}? [Da]{14} [bliibt]{13} [kei]{11,12} [Stei]{15} [uf]{16} [em andere]{17}, [wo]{18} [nöd]{19,20} [abbroche wird]{21}.»",
 "MRK.13.3": "Und{1} [wo er]{3} [uf]{4} [em]{5} [Ölberg]{6-8} [gsässe isch]{2}, [gägenüber]{9} [vom]{10} [Tämpel]{11}, [händ]{12} [en]{13} [de Petrus]{16} und{17} [de Jakobus]{18} und{19} [de Johannes]{20} und{21} [de Andreas]{22} [für sich elei]{14,15} [gfröget]{12}:",
 "MRK.13.4": "«[Säg]{1} [üs]{2}: [Wänn]{3} [passiert]{5} [das]{4}, und{6} [was]{7} isch [s]{8} [Zeiche]{9}, [wänn]{10} [das]{12} [alles]{14} [sich erfülle]{13} [söll]{11}?»",
 "MRK.13.5": "[De Jesus]{1,3} [aber]{2} [hät aagfange]{4}, [zu ine]{6} [z säge]{5}: «[Passed uf]{7}, [dass niemer]{8,9} [eu]{10} [in d Irri füert]{11}!",
 "MRK.13.6": "[Vil]{1} [wärded]{2} [i]{3} [mim]{4,6} [Name]{5} [choo]{2} [und säge]{7}: ‹[Ich]{9} [bins]{10}›, und{11} [si wärded]{13} [vil]{12} [in d Irri füere]{13}. ~8(ὅτι leitet die Rede ein)",
 "MRK.13.7": "[Wänn]{1} [ir]{3} [aber]{2} [vo Chrieg]{4} und{5} [Chriegsgrücht]{6,7} [ghöred]{3}, [lönd eu]{9} [nöd]{8} [verschrecke]{9}. [Es mues]{10} [passiere]{11}, [aber]{12} [s]{14} [Änd]{15} isch [no nöd]{13} da.",
 "MRK.13.8": "[Dänn]{2} [es wird sich]{1} [Volk]{3} [gäge]{4} [Volk]{5} [erhebe]{1} und{6} [Riich]{7} [gäge]{8} [Riich]{9}; [es wird]{10} [a vilne Orte]{12,13} [Ärdbebe]{11} [gää]{10}, [es wird]{14} [Hungersnöt]{15} [gää]{14}. [Das]{18} isch [de Aafang]{16} [vo de Wehe]{17}.",
 "MRK.13.9": "[Ir]{3} [aber]{2}, [lueged]{1} [uf eu sälber]{4}! [Mer wird]{5} [eu]{6} [a]{7} [Gricht]{8} [uslifere]{5}, und{9} [i]{10} [Synagoge]{11} [wärded ir gschlage]{12}, und{13} [vor]{14} [Statthalter]{15} und{16} [Könige]{17} [wärded ir gstellt]{18} [wäge mir]{19,20}, [ine]{23} [zum]{21} [Züügnis]{22}.",
 "MRK.13.10": "Und{1} [under]{2} [allne]{3} [Völker]{4,5} [mues]{7} [zerscht]{6} [s]{9} [Evangelium]{10} [verchündet wärde]{8}.",
 "MRK.13.11": "Und{1} [wänn]{2} [mer]{3} [eu]{4} [abfüert]{3} [und uslieferet]{5}, [mached eu]{7} [nöd]{6} [zum voruus Sorge]{7}, [was]{8} [ir säge söled]{9}; [sondern]{10} [was]{11,12} [eu]{14} [i]{15} [dere]{16,17} [Stund]{18} [gää wird]{13}, [das]{19} [säged]{20}. [Dänn]{22} [nöd]{21} [ir]{24} [sind]{23} [s]{25}, [wo reded]{26}, [sondern]{27} [de]{28} [Heilig]{30,31} [Geischt]{29}.",
 "MRK.13.12": "Und{1} [es wird]{2} [en Brueder]{3} [de Brueder]{4} [in]{5} [de Tod]{6} [uslifere]{2} und{7} [en Vatter]{8} [s Chind]{9}, und{10} [Chind]{12} [wärded sich]{11} [gäge]{13} [d Eltere]{14} [ufläne]{11} und{15} [si]{17} [in Tod schicke]{16}.",
 "MRK.13.13": "Und{1} [ir wärded]{2} [vo]{4} [allne]{5} [ghasst]{3} [sii]{2} [wäge]{6} [mim]{7,9} [Name]{8}. [Wär]{10} [aber]{11} [bis]{13} [as Änd]{14} [durehebt]{12}, [dä]{15} [wird grettet]{16}.",
 "MRK.13.14": "[Wänn]{1} [ir]{3} [aber]{2} [de]{4} [Gröiel]{5} [vo de]{6} [Verwüeschtig]{7} [det staa]{8} [gsehnd]{3}, [wo]{9} er [nöd]{10} [darf]{11} – [wär s list]{12,13}, [dä söll ufpasse]{14}! –, [dänn]{15} [söled]{20} [die]{16} [z]{17,18} [Judäa]{19} [i]{21} [d]{22} [Bärge]{23} [flüchte]{20}.",
 "MRK.13.15": "[Wär]{1} [uf]{2} [em]{3} [Dach]{4} isch, [söll]{6} [nöd]{5} [abe choo]{6} [und nöd]{7} [ine gaa]{8}, zum [öppis]{9} [us]{11} [sim]{12,14} [Huus]{13} [z hole]{10};",
 "MRK.13.16": "und{1} [wär]{2} [uf]{3} [em]{4} [Fäld]{5} isch, [söll]{7} [nöd]{6} [zrugg]{8-10} [choo]{7}, zum [sin]{12,14} [Mantel]{13} [z hole]{11}.",
 "MRK.13.17": "[Wehe]{1} [aber]{2} [de]{3} [Schwangere]{4-6} und{7} [dene]{8}, [wo stilled]{9}, [i]{10} [dene]{11,12} [Täg]{13}!",
 "MRK.13.18": "[Bätted]{1} [aber]{2}, [dass]{3} [s]{5} [nöd]{4} [im Winter]{6} [passiert]{5}.",
 "MRK.13.19": "[Dänn]{2} [die]{3,5} [Täg]{4} [wärded]{1} [e Bedrängnis]{6} [sii]{1}, [wie]{7} [s]{9} [kei]{8} [settigi]{10} [gää hät]{9} [vom]{11} [Aafang]{12} [vo de Schöpfig]{13}, [wo]{14} [Gott]{16,17} [gschaffe hät]{15}, [bis]{18} [hüt]{19,20}, und{21} [au nie]{22,23} [gää wird]{24}.",
 "MRK.13.20": "Und{1} [wänn]{2} [de Herr]{5} [d]{6} [Täg]{7} [nöd]{3} [verchürzt hett]{4}, [wür]{9} [kei]{8} [Mänsch]{11,12} [grettet]{10} wärde; [aber]{13} [wäge]{14} [de]{15} [Uuserwäälte]{16}, [wo]{17} [er uuserwäält hät]{18}, [hät er]{19} [d]{20} [Täg]{21} [verchürzt]{19}.",
 "MRK.13.21": "Und{1} [wänn]{3} [dänn]{2} [öpper]{4} [zu eu]{5} [seit]{6}: ‹[Lueg]{7}, [da]{8} isch [de]{9} [Christus]{10}! [Lueg]{11}, [det]{12}!›, [glaubed s]{14} [nöd]{13}!",
 "MRK.13.22": "[Dänn]{2} [es wärded]{1} [falschi Christusse]{3} und{4} [falschi Prophete]{5} [uftrete]{1} und{6} [Zeiche]{8} und{9} [Wunder]{10} [tue]{7}, [zum]{11,12} [wänn]{14} [mögli]{15} [d]{16} [Uuserwäälte]{17} [in d Irri z füere]{13}.",
 "MRK.13.23": "[Ir]{1} [aber]{2}, [passed uf]{3}! [Ich ha]{4} [eu]{5} [alles]{6} [voruus gseit]{4}.",
 "MRK.13.24": "[Aber]{1} [i]{2} [dene]{3,4} [Täg]{5}, [nach]{6} [dere]{7,9} [Bedrängnis]{8}, [wird]{12} [d]{10} [Sunne]{11} [dunkel wärde]{12}, und{13} [de]{14} [Mond]{15} [wird]{17} [sis]{18,20} [Liecht]{19} [nöd]{16} [gää]{17},",
 "MRK.13.25": "und{1} [d]{2} [Stärne]{3} [wärded]{4} [vom]{5,6} [Himmel]{7} [abegheie]{8}, und{9} [d]{10} [Mächt]{11} [im]{12-14} [Himmel]{15} [wärded erschütteret]{16}.",
 "MRK.13.26": "Und{1} [dänn]{2} [wärded si]{3} [de Mänschesohn]{4-7} [gseh]{3} [choo]{8} [i]{9} [Wolche]{10} [mit]{11} [grosser]{13} [Macht]{12} und{14} [Herrlichkeit]{15}.",
 "MRK.13.27": "Und{1} [dänn]{2} [wird er]{3} [d]{4} [Ängel]{5} [usschicke]{3} und{6} [d]{8} [Uuserwäälte]{9} [zämehole]{7} [us]{10} [de]{11} [vier]{12} [Wind]{13}, [vom]{14} [Änd]{15} [vo de Ärde]{16} [bis]{17} [as Änd]{18} [vom Himmel]{19}.",
 "MRK.13.28": "[Vom]{1,3} [Fiigebaum]{4} [aber]{2} [lehred]{5} [s]{6} [Gliichnis]{7}: [Sobald]{8} [sin]{10,12} [Zweig]{11} [scho]{9} [weich]{13} [wird]{14} und{15} [d]{17} [Bletter]{18} [tribt]{16}, [merked ir]{19}, [dass]{20} [de]{22} [Summer]{23} [nöch]{21} [isch]{24}.",
 "MRK.13.29": "[So]{1} [au]{2} [ir]{3}: [Wänn]{4} [ir]{5} [das]{6} [gsehnd]{5} [passiere]{7}, [merked]{8}, [dass]{9} [s]{11} [nöch]{10} [vor]{12} [de Tür]{13} [isch]{11}.",
 "MRK.13.30": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Die]{8,10} [Generation]{9} [vergaat]{7} [nöd]{5,6}, [bis]{11,12} [das]{13} [alles]{14} [passiert]{15}. ~4(ὅτι leitet die Rede ein)",
 "MRK.13.31": "[De]{1} [Himmel]{2} und{3} [d]{4} [Ärde]{5} [vergönd]{6}, [mini]{7,10} [Wort]{9} [aber]{8} [vergönd]{13} [nöd]{11,12}.",
 "MRK.13.32": "[Vo]{1} [dem]{3,5} [Tag]{4} [aber]{2} [oder]{6} [dere]{7} [Stund]{8} [weiss]{10} [niemer]{9} öppis, [au nöd]{11} [d]{12} [Ängel]{13} [im]{14} [Himmel]{15}, [au nöd]{16} [de]{17} [Sohn]{18}, [nu]{19,20} [de]{21} [Vatter]{22}.",
 "MRK.13.33": "[Passed uf]{1}, [bliibed wach]{2}! [Dänn]{5} [ir wüssed]{4} [nöd]{3}, [wänn]{6} [d]{7} [Ziit]{8} [da isch]{9}.",
 "MRK.13.34": "[Es isch wie]{1} [bi me Mänsch]{2}, [wo verreist isch]{3}: [Er hät]{4} [sis]{5,7} [Huus]{6} [verlaa]{4} und{8} [sine]{10,12} [Chnächt]{11} [d]{13} [Vollmacht]{14} [gää]{9}, [jedem]{15} [sini]{16,18} [Arbet]{17}, und{19} [em]{20} [Türhüeter]{21} [hät er befole]{22}, [dass]{23} [er wach bliibt]{24}.",
 "MRK.13.35": "[Bliibed]{1} [also]{2} [wach]{1}! [Dänn]{5} [ir wüssed]{4} [nöd]{3}, [wänn]{6} [de]{7} [Herr]{8} [vom]{9} [Huus]{10} [chunnt]{11}: [öb]{12} [am Aabig]{13} [oder]{14} [z Mitternacht]{15} [oder]{16} [wänn de Güggel chräit]{17} [oder]{18} [am Morge früe]{19},",
 "MRK.13.36": "[demit]{1} [er]{4}, [wänn er]{2} [plötzlich]{3} [chunnt]{2}, [eu]{5} [nöd]{1} [am Schlafe]{6} [aatrifft]{4}.",
 "MRK.13.37": "[Was]{1} [ich]{4} [aber]{2} [eu]{3} [säg]{4}, [das säg ich]{6} [allne]{5}: [Bliibed wach]{7}!»",
}

# Übersetzungsentscheidungen: (Stelle, Zieltext, Art, griechisch, wörtlicher, andere Möglichkeiten, Begründung)
DEC_DE = [
 ("MRK.11.2", "ein Fohlen", "interpretive", "πῶλον", "ein Jungtier", ["einen jungen Esel", "ein Eselsfüllen"], "πῶλος ist ein junges Tier; Markus sagt nicht, welches. Meist wird an einen jungen Esel gedacht (vgl. [[ZEC.9.9]], [[MAT.21.2]], [[JHN.12.14]]); ohne nähere Angabe kann das Wort im Griechischen auch ein Pferdefohlen bezeichnen."),
 ("MRK.11.3", "Der Herr braucht es", "interpretive", "Ὁ κύριος αὐτοῦ χρείαν ἔχει", "Der Herr hat seiner Bedarf", ["Sein Besitzer braucht es", "Der Meister braucht es"], "κύριος kann Jesus, Gott oder einen Besitzer meinen; αὐτοῦ gehört zu χρείαν («hat es nötig»), nicht zu κύριος. Meist wird der Satz als Selbstbezeichnung Jesu gelesen; die Wiedergabe lässt die Doppeldeutigkeit stehen. Wer «es sofort wieder hierher» schickt, ist ebenfalls offen: Jesus (Rückgabe) oder der Besitzer."),
 ("MRK.11.7", "Mäntel", "interpretive", "ἱμάτια", "Gewänder", ["Kleider", "Obergewänder"], "ἱμάτιον ist das Obergewand, ein Umhang; ebenso in [[MRK.11.8]] und [[MRK.13.16]]."),
 ("MRK.11.8", "Zweige", "interpretive", "στιβάδας", "Streu", ["Laubbüschel", "Palmzweige"], "στιβάς ist eine Streu aus Laub, Halmen oder Zweigen. Von Palmzweigen spricht nur [[JHN.12.13]]."),
 ("MRK.11.9", "Hosanna", "traditional", "Ὡσαννά", "Hilf doch!", ["Rette doch!", "Heil!"], "Ὡσαννά ist die griechische Umschrift eines hebräisch-aramäischen Rufs «Hilf doch!» ([[PSA.118.25]]). Zur Zeit Jesu war er wohl schon ein Jubelruf; ob die Bitte noch mitgehört wurde, ist offen. Die Umschrift bleibt stehen, wie im Griechischen."),
 ("MRK.11.9", "Gesegnet sei der, der kommt im Namen des Herrn", "literal", "Εὐλογημένος ὁ ἐρχόμενος ἐν ὀνόματι κυρίου", None, ["Gepriesen sei, der da kommt im Namen des Herrn"], "Zitat aus [[PSA.118.26]], einem Wallfahrtspsalm. «Der Kommende» konnte messianisch verstanden werden; [[MRK.11.10]] spricht ausdrücklich vom Reich Davids."),
 ("MRK.11.11", "Tempel", "literal", "ἱερόν", None, ["Tempelbezirk", "Heiligtum"], "ἱερόν bezeichnet den ganzen Tempelbezirk mit Höfen und Hallen, nicht nur das Tempelhaus (ναός). Ebenso in [[MRK.11.15-MRK.11.16]], [[MRK.11.27]], [[MRK.12.35]] und [[MRK.13.1]]."),
 ("MRK.11.13", "denn es war nicht die Zeit der Feigen", "literal", "ὁ γὰρ καιρὸς οὐκ ἦν σύκων", None, None, "Die Bemerkung macht die Verfluchung in [[MRK.11.14]] auffällig. Markus rahmt mit der Feigenbaum-Geschichte ([[MRK.11.12-MRK.11.14]], [[MRK.11.20-MRK.11.21]]) Jesu Auftreten im Tempel; viele lesen sie deshalb als Zeichenhandlung. Die Übersetzung glättet die Spannung nicht."),
 ("MRK.11.14", "er ergriff das Wort", "adapted", "ἀποκριθεὶς", "antwortend", ["er sprach ihn an", "darauf"], "ἀποκρίνομαι heisst «antworten», steht bei Markus aber auch, wenn niemand gefragt hat: Jesus reagiert auf den Befund."),
 ("MRK.11.15", "Geldwechsler", "literal", "κολλυβιστῶν", None, ["Wechsler"], "Für die Tempelsteuer wurde eine bestimmte Silbermünze verlangt; Wechsler tauschten anderes Geld gegen Gebühr. Tauben waren das Opfer der Armen ([[LEV.12.8]])."),
 ("MRK.11.17", "ein Haus des Gebets heissen für alle Völker", "literal", "οἶκος προσευχῆς κληθήσεται πᾶσιν τοῖς ἔθνεσιν", None, ["Bethaus für alle Völker", "für alle Heiden"], "Zitat aus [[ISA.56.7]]. ἔθνη sind die Völker, im jüdischen Sprachgebrauch die Nichtjuden. Nur Markus führt «für alle Völker» mit an (vgl. [[MAT.21.13]], [[LUK.19.46]])."),
 ("MRK.11.17", "zu einer Räuberhöhle", "traditional", "σπήλαιον λῃστῶν", "zu einer Höhle von Räubern", ["zu einem Räubernest", "zu einem Versteck von Banditen", "zu einem Schlupfwinkel von Aufrührern"], "Die Wendung ist aus [[JER.7.11]] übernommen (in der griechischen Fassung wörtlich gleich). Eine Räuberhöhle ist nicht der Ort, an dem geraubt wird, sondern der Unterschlupf, in dem Räuber sich sicher fühlen; bei Jeremia steht das Bild gegen ein Vertrauen auf den Tempel trotz Unrecht. λῃστής kann auch bewaffnete Aufständische bezeichnen. Ob Jesus den Handel, die Ausbeutung der Armen oder falsche Sicherheit anprangert, wird unterschiedlich gedeutet."),
 ("MRK.11.18", "Hohepriester", "literal", "ἀρχιερεῖς", None, ["Oberpriester", "führende Priester"], "Der Plural meint den amtierenden Hohepriester, seine Vorgänger und die Spitzen der Priesterschaft."),
 ("MRK.11.18", "war überwältigt", "interpretive", "ἐξεπλήσσετο", "geriet ausser sich", ["staunte", "war erschüttert"], "ἐκπλήσσομαι bezeichnet ein starkes Ergriffensein, nicht nur Verwunderung."),
 ("MRK.11.22", "Glauben an Gott", "interpretive", "πίστιν θεοῦ", "Glauben Gottes", ["Vertrauen auf Gott", "Glauben, der von Gott kommt"], "Der Genitiv wird meist objektiv verstanden (Glauben an Gott). Seltener wird er als Glaube gelesen, den Gott schenkt, oder als Gottes Treue."),
 ("MRK.11.23", "Heb dich hoch und stürz dich ins Meer", "adapted", "Ἄρθητι καὶ βλήθητι", "Werde hochgehoben und geworfen", ["Heb dich empor und wirf dich ins Meer"], "Die passiven Befehlsformen sind deutsch kaum nachzubilden; manche sehen darin ein verhülltes Handeln Gottes. Ob «dieser Berg» bildlich jeden Berg meint oder im Zusammenhang auf den Tempelberg anspielt, ist umstritten."),
 ("MRK.11.24", "dass ihr es empfangen habt", "literal", "ἐλάβετε", None, ["dass ihr es empfangt", "dass ihr es erhalten werdet"], "Der Aorist (Vergangenheitsform) ist auffällig: Der Glaube rechnet mit der Erhörung, als sei sie schon geschehen. Ein Teil der Überlieferung hat die Gegenwartsform (siehe Alternativen)."),
 ("MRK.11.25", "Verfehlungen", "interpretive", "παραπτώματα", "Fehltritte", ["Übertretungen", "Sünden"], "παράπτωμα ist der Fehltritt, das Danebentreten; das einzige Vorkommen bei Markus."),
 ("MRK.11.28", "Vollmacht", "interpretive", "ἐξουσίᾳ", None, ["Autorität", "Befugnis", "Recht"], "ἐξουσία ist die verliehene Befugnis zu handeln. Die Frage zielt darauf, wer Jesus dazu ermächtigt hat (vgl. [[MRK.1.22]], [[MRK.1.27]])."),
 ("MRK.11.30", "vom Himmel", "literal", "ἐξ οὐρανοῦ", None, ["von Gott"], "«Himmel» umschreibt in jüdischer Redeweise Gott."),
 ("MRK.11.32", "Sollen wir aber sagen", "interpretive", "ἀλλὰ εἴπωμεν", "Aber sagen wir", None, "Der Satz bricht ab; der Erzähler setzt die Begründung fort. Die Übersetzung macht den Abbruch mit einem Gedankenstrich sichtbar."),
 ("MRK.12.1", "Weinbauern", "interpretive", "γεωργοῖς", "Landbauern", ["Pächtern", "Winzern"], "γεωργός ist der Landbauer; hier Pächter, die dem abwesenden Besitzer einen Teil des Ertrags schulden. Das Bild nimmt [[ISA.5.1-ISA.5.7]] auf (Weinberg, Zaun, Kelter, Turm)."),
 ("MRK.12.1", "eine Keltergrube", "literal", "ὑπολήνιον", None, ["eine Kelter", "einen Keltertrog"], "ὑπολήνιον ist das Becken unter der Kelter, in das der Most läuft."),
 ("MRK.12.2", "Knecht", "traditional", "δοῦλον", "Sklaven", ["Diener", "Boten"], "δοῦλος ist der Sklave; im Gleichnis ein Beauftragter des Besitzers. Viele hören darin die Propheten, die zu Israel gesandt wurden."),
 ("MRK.12.4", "schlugen sie auf den Kopf", "interpretive", "ἐκεφαλίωσαν", None, ["verwundeten sie am Kopf", "misshandelten sie"], "Das Verb ist sonst kaum belegt; es ist von κεφαλή «Kopf» abgeleitet. Die Bedeutung wird aus dem Zusammenhang erschlossen."),
 ("MRK.12.6", "einen geliebten Sohn", "literal", "υἱὸν ἀγαπητόν", None, ["seinen einzigen Sohn", "seinen lieben Sohn"], "ἀγαπητός steht in der griechischen Bibel auch für den «einzigen» Sohn ([[GEN.22.2]]). Anklang an die Himmelsstimme in [[MRK.1.11]] und [[MRK.9.7]]."),
 ("MRK.12.10", "zum Eckstein", "interpretive", "κεφαλὴν γωνίας", "zum Haupt der Ecke", ["zum Schlussstein", "zum Grundstein"], "Zitat aus [[PSA.118.22-PSA.118.23]]. Gemeint ist ein Stein an hervorgehobener Stelle: ein Eckstein im Fundament oder ein Schlussstein oben; beides wird vertreten."),
 ("MRK.12.13", "Herodianern", "literal", "Ἡρῳδιανῶν", None, ["Anhängern des Herodes"], "Anhänger der Herodes-Dynastie, in Galiläa des Herodes Antipas (vgl. [[MRK.3.6]]). Wer genau dazugehörte, ist nicht bekannt."),
 ("MRK.12.14", "du siehst nicht auf das Ansehen", "adapted", "οὐ βλέπεις εἰς πρόσωπον", "du blickst nicht auf das Gesicht", ["du bist nicht parteiisch", "du richtest dich nicht nach dem Rang"], "Biblische Redewendung: das «Gesicht» ist die Stellung eines Menschen. Gemeint ist Unparteilichkeit."),
 ("MRK.12.14", "Steuer", "interpretive", "κῆνσον", "Census", ["Kopfsteuer", "Zensus"], "Lehnwort aus dem Lateinischen (census): die direkte Steuer an Rom, in Judäa seit der Eingliederung als Provinz (6 n. Chr.) erhoben und umstritten."),
 ("MRK.12.15", "Denar", "literal", "δηνάριον", None, None, "Römische Silbermünze, etwa ein Tageslohn (vgl. [[MAT.20.2]]), mit Bild und Inschrift des Kaisers."),
 ("MRK.12.17", "gebt dem Kaiser", "interpretive", "ἀπόδοτε Καίσαρι", "gebt zurück dem Kaiser", ["erstattet dem Kaiser", "zahlt dem Kaiser"], "ἀποδίδωμι heisst «zurückgeben, Geschuldetes geben»; in der Frage stand δοῦναι «geben» ([[MRK.12.14]]). Ob der Satz zwei Bereiche nebeneinanderstellt oder den Kaiser Gott unterordnet, ist umstritten. Manche verbinden das Bild auf der Münze mit dem Menschen als Bild Gottes ([[GEN.1.27]]); das sagt der Text nicht ausdrücklich."),
 ("MRK.12.19", "Nachkommen erwecken", "literal", "ἐξαναστήσῃ σπέρμα", "Samen erstehen lassen", ["einen Erben zeugen"], "Gemeint ist die Schwagerehe nach [[DEU.25.5-DEU.25.6]] (vgl. [[GEN.38.8]]): Der Name des Verstorbenen soll weiterleben."),
 ("MRK.12.26", "beim Dornbusch", "literal", "ἐπὶ τοῦ βάτου", None, ["in der Geschichte vom Dornbusch"], "So wurde der Abschnitt [[EXO.3.1-EXO.3.6]] bezeichnet; Kapitel- und Verszählung gab es noch nicht. Das Zitat ist [[EXO.3.6]]."),
 ("MRK.12.29", "Höre, Israel: Der Herr, unser Gott, der Herr ist einer", "literal", "Ἄκουε Ἰσραήλ κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν", None, ["Der Herr ist unser Gott, der Herr allein", "Der Herr, unser Gott, ist der einzige Herr", "Der Herr, unser Gott, ist ein Herr"], "Das «Schma Israel» ([[DEU.6.4-DEU.6.5]]) nach der griechischen Fassung. κύριος steht dort für den Gottesnamen JHWH. Der Satz lässt sich als Aussage über die Einzigkeit Gottes (nur er ist Gott), über seine Einheit oder als Bekenntnis zur alleinigen Bindung Israels an ihn lesen; die Wiedergabe bleibt beim Wortlaut."),
 ("MRK.12.30", "du sollst den Herrn, deinen Gott, lieben", "adapted", "ἀγαπήσεις κύριον τὸν θεόν σου", "du wirst den Herrn, deinen Gott, lieben", None, "Das Futur hat, wie in der griechischen Fassung von [[DEU.6.5]], die Kraft eines Gebots."),
 ("MRK.12.30", "Denken", "interpretive", "διανοίας", None, ["Verstand", "Gesinnung", "Gemüt"], "[[DEU.6.5]] nennt im Hebräischen drei Glieder (Herz, Seele, Kraft); Markus hat vier, dazu διάνοια «Denken, Verstand». Der Schriftgelehrte nennt in [[MRK.12.33]] drei, mit σύνεσις «Einsicht»."),
 ("MRK.12.31", "deinen Nächsten lieben wie dich selbst", "literal", "Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν", None, None, "Zitat aus [[LEV.19.18]]. Die Verbindung der beiden Gebote ist auch aus jüdischer Überlieferung bekannt; neu ist hier die ausdrückliche Rangfolge «das erste – das zweite»."),
 ("MRK.12.33", "Brandopfer und Schlachtopfer", "literal", "ὁλοκαυτωμάτων καὶ θυσιῶν", None, ["Opfer und Gaben"], "Brandopfer wurden ganz verbrannt, bei Schlachtopfern ass man einen Teil. Der Satz nimmt prophetische Kritik auf (vgl. [[HOS.6.6]], [[1SA.15.22]])."),
 ("MRK.12.35", "der Christus", "literal", "ὁ χριστὸς", None, ["der Messias", "der Gesalbte"], "χριστός heisst «Gesalbter», griechisch für hebräisch Maschiach. Hier ein Titel, nicht der Name Jesu; ebenso in [[MRK.13.21]]."),
 ("MRK.12.36", "Der Herr sprach zu meinem Herrn", "literal", "Εἶπεν κύριος τῷ κυρίῳ μου", None, None, "Zitat aus [[PSA.110.1]]. Im Hebräischen spricht JHWH zu «meinem Herrn» (einem menschlichen Herrn); im Griechischen steht zweimal κύριος. Das Argument setzt voraus, dass David selbst spricht."),
 ("MRK.12.38", "die es lieben", "interpretive", "θελόντων", "die wollen", ["die gern"], "θέλω «wollen» regiert hier auch die folgenden Glieder (Begrüssungen, Ehrenplätze); «lieben» macht das deutsch lesbar."),
 ("MRK.12.40", "die Häuser der Witwen auffressen", "literal", "κατεσθίοντες τὰς οἰκίας τῶν χηρῶν", None, ["die Witwen um ihr Vermögen bringen"], "«Häuser» meint Besitz und Lebensgrundlage. Wie das geschah (Vermögensverwaltung, Gebühren, Ausnützen von Gastfreundschaft), sagt der Text nicht."),
 ("MRK.12.41", "Opferkasten", "interpretive", "γαζοφυλακίου", "Schatzkammer", ["Opferstock", "Tempelschatz"], "γαζοφυλάκιον ist die Schatzkammer; hier wohl die Behälter für Spenden im Tempelbezirk."),
 ("MRK.12.42", "zwei Lepta", "literal", "λεπτὰ δύο ὅ ἐστιν κοδράντης", None, ["zwei kleine Münzen, das ist ein Viertelgroschen"], "Das Lepton war die kleinste Kupfermünze; Markus erklärt sie mit der römischen Münze quadrans (ein Viertel As). Die Erklärung mit einer römischen Münze wird oft als Hinweis auf eine Leserschaft im römischen Westen gelesen."),
 ("MRK.12.44", "ihren ganzen Lebensunterhalt", "interpretive", "ὅλον τὸν βίον αὐτῆς", "ihr ganzes Leben", ["alles, wovon sie lebte"], "βίος ist das Leben und das, wovon man lebt. Ob die Witwe gelobt oder (nach [[MRK.12.40]]) als Opfer eines Systems gezeigt wird, wird unterschiedlich gedeutet."),
 ("MRK.13.6", "bin es", "interpretive", "εἰμι", "bin", ["bin der Christus"], "Ἐγώ εἰμι kann heissen «Ich bin es (der Erwartete)». Die Wendung klingt an die Selbstvorstellung Gottes an ([[EXO.3.14]], [[ISA.43.10]]) und an [[MRK.6.50]] und [[MRK.14.62]]."),
 ("MRK.13.8", "der Anfang der Wehen", "literal", "ἀρχὴ ὠδίνων", None, ["der Anfang der Geburtswehen"], "Bild aus der Geburt: Die Nöte sind schmerzhaft, aber kein Ende, sondern Beginn von etwas Neuem (vgl. [[ISA.26.17]])."),
 ("MRK.13.9", "Gerichte", "interpretive", "συνέδρια", "Synedrien", ["Ratsversammlungen", "Hohe Räte"], "Der Plural meint örtliche jüdische Gerichtsräte, nicht nur den Hohen Rat in Jerusalem."),
 ("MRK.13.14", "den Gräuel der Verwüstung", "traditional", "τὸ βδέλυγμα τῆς ἐρημώσεως", "den Abscheu der Verödung", ["das verwüstende Scheusal", "die entweihende Abscheulichkeit"], "Ausdruck aus dem Danielbuch ([[DAN.9.27]], [[DAN.11.31]], [[DAN.12.11]]); dort für den heidnischen Altar im Tempel unter Antiochus IV. (vgl. [[1MA.1.54]]). βδέλυγμα ist, was Gott ein Gräuel ist, oft Götzendienst. Markus setzt das Partizip ἑστηκότα männlich, obwohl βδέλυγμα sächlich ist; vielleicht ist eine Person gemeint. Die Übersetzung gibt das mit «wo er nicht darf» wieder. Worauf die Stelle zielt (Entweihung des Tempels im Jüdischen Krieg 66–70, Caligulas Plan einer Statue im Tempel um 40 n. Chr., eine Gestalt der Endzeit), ist umstritten."),
 ("MRK.13.14", "wer es liest, der merke auf", "literal", "ὁ ἀναγινώσκων νοείτω", None, ["wer es vorliest, soll es verstehen"], "Ein Einschub an den Leser bzw. Vorleser des Textes; er deutet einen verschlüsselten Hinweis an."),
 ("MRK.13.20", "kein Mensch", "adapted", "πᾶσα σάρξ", "alles Fleisch", None, "«Fleisch» steht hebräischer Redeweise folgend für den Menschen in seiner Vergänglichkeit; mit οὐκ: «kein Mensch»."),
 ("MRK.13.22", "falsche Christusse", "literal", "ψευδόχριστοι", None, ["falsche Messiasse", "falsche Gesalbte"], "Zu «Christus» als Titel vgl. [[MRK.12.35]]."),
 ("MRK.13.26", "den Menschensohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "den Sohn des Menschen", ["den Menschen"], "Anspielung auf [[DAN.7.13]]: einer «wie ein Menschensohn» kommt mit den Wolken des Himmels. Bei Markus Selbstbezeichnung Jesu (vgl. [[MRK.14.62]])."),
 ("MRK.13.29", "dass es nahe vor der Tür ist", "interpretive", "ὅτι ἐγγύς ἐστιν ἐπὶ θύραις", "dass nahe ist an den Türen", ["dass er nahe vor der Tür ist"], "Das Subjekt fehlt: gemeint sein kann «er» (der Menschensohn, [[MRK.13.26]]) oder «es» (das Ende, das angekündigte Geschehen)."),
 ("MRK.13.30", "Dieses Geschlecht", "traditional", "ἡ γενεὰ αὕτη", "diese Generation", ["Diese Generation", "Diese Art von Menschen", "Dieses Volk"], "γενεά meint meist die Menschen einer Zeit, eine Generation (vgl. [[MRK.8.12]], [[MRK.8.38]], [[MRK.9.19]]). Dann bezieht sich «das alles» entweder auf die Ereignisse bis zur Zerstörung des Tempels (70 n. Chr.), oder es stellt sich die Frage nach der ausgebliebenen Wiederkunft. Andere verstehen γενεά weiter (die Menschheit, das jüdische Volk, die Art ungläubiger Menschen). «Geschlecht» hält die Mehrdeutigkeit offen; viele neuere Übersetzungen sagen «Generation»."),
 ("MRK.13.32", "auch nicht der Sohn, nur der Vater", "literal", "οὐδὲ ὁ υἱός εἰ μὴ ὁ πατήρ", None, None, "Die einzige Stelle bei Markus, an der Jesus sich absolut «der Sohn» nennt. Dass der Sohn Tag und Stunde nicht kennt, beschäftigte die späteren Debatten über die Person Christi; Markus sagt es ohne Abschwächung."),
 ("MRK.13.33", "Zeit", "interpretive", "καιρός", None, ["der entscheidende Zeitpunkt", "die Stunde"], "καιρός ist die bestimmte, entscheidende Zeit, nicht die Dauer (χρόνος)."),
 ("MRK.13.35", "am Abend oder um Mitternacht oder beim Hahnenschrei oder am frühen Morgen", "literal", "ὀψὲ μεσονύκτιον ἀλεκτοροφωνίας πρωΐ", None, None, "Die vier Nachtwachen nach römischer Zählung. Der Hahnenschrei weist auf [[MRK.14.72]] voraus."),
]
DEC_GSW = [
 ("MRK.11.2", "es Füli", "interpretive", "πῶλον", "es Jungtier", ["en junge Esel"], "πῶλος isch es junges Tier; de Markus seit nöd, was für eis. Meischt dänkt mer a en junge Esel (vgl. [[ZEC.9.9]], [[MAT.21.2]], [[JHN.12.14]]); ohni nöcheri Aagab cha s Wort au es Rossfüli meine."),
 ("MRK.11.3", "De Herr bruucht s", "interpretive", "Ὁ κύριος αὐτοῦ χρείαν ἔχει", "De Herr hät sin Bedarf", ["Sin Bsitzer bruucht s", "De Meischter bruucht s"], "κύριος cha de Jesus, Gott oder en Bsitzer meine. Meischt list mer de Satz so, dass de Jesus vo sich sälber redt; d Widergab laat d Doppeldüütigkeit staa. Wär s «grad wider da häre» schickt, isch au offe: de Jesus (Rückgab) oder de Bsitzer."),
 ("MRK.11.8", "Zweig", "interpretive", "στιβάδας", "Streui", ["Loubbüschel", "Palmzweig"], "στιβάς isch e Streui us Loub, Halme oder Zweig. Vo Palmzweig redt nu [[JHN.12.13]]."),
 ("MRK.11.9", "Hosanna", "traditional", "Ὡσαννά", "Hilf doch!", ["Rette doch!"], "Ὡσαννά isch di griechisch Umschrift vo me hebräisch-aramäische Ruef «Hilf doch!» ([[PSA.118.25]]). Zur Ziit vo Jesus isch er wahrschiinli scho en Jubelruef gsii; öb mer d Bitt no mitghört hät, isch offe."),
 ("MRK.11.11", "Tämpel", "literal", "ἱερόν", None, ["Tämpelbezirk"], "ἱερόν meint de ganz Tämpelbezirk mit Höf und Halle, nöd nu s Tämpelhuus (ναός)."),
 ("MRK.11.13", "dänn es isch nöd d Ziit für Fiige gsii", "literal", "ὁ γὰρ καιρὸς οὐκ ἦν σύκων", None, None, "D Bemerkig macht de Fluech i [[MRK.11.14]] uffällig. De Markus rahmt mit de Fiigebaum-Gschicht ([[MRK.11.12-MRK.11.14]], [[MRK.11.20-MRK.11.21]]) s Uftrete vo Jesus im Tämpel; vil läsed si drum als Zeichehandlig."),
 ("MRK.11.14", "druf abe", "adapted", "ἀποκριθεὶς", "antwortend", None, "ἀποκρίνομαι heisst «antworte», staat bim Markus aber au, wänn niemer gfröget hät: De Jesus reagiert uf das, won er gfunde hät."),
 ("MRK.11.17", "e Röiberhöli", "traditional", "σπήλαιον λῃστῶν", "e Höli vo Röiber", ["es Röibernäscht", "es Versteck vo Bandite"], "D Wändig isch us [[JER.7.11]] übernoo (i de griechische Fassig wörtlich gliich). E Röiberhöli isch nöd de Ort, wo grobt wird, sondern de Unterschlupf, wo sich d Röiber sicher füeled; bim Jeremia staat s Bild gäge s Vertroue uf de Tämpel trotz Unrächt. λῃστής cha au bewaffneti Ufständischi meine. Öb de Jesus de Handel, d Usbüütig vo de Arme oder e falschi Sicherheit aaprangeret, wird verschide düütet."),
 ("MRK.11.22", "Glaube a Gott", "interpretive", "πίστιν θεοῦ", "Glaube vo Gott", ["Vertroue uf Gott"], "De Genitiv wird meischt objektiv verstande (Glaube a Gott); sältener als Glaube, wo Gott schänkt, oder als Tröii vo Gott."),
 ("MRK.11.24", "dass ir s übercho händ", "literal", "ἐλάβετε", None, ["dass ir s überchömed"], "D Vergangeheitsform (Aorist) isch uffällig: De Glaube rächnet mit de Erhörig, wie wänn si scho gscheh wär. En Teil vo de Überlieferig hät d Gägewartsform (lueg Alternative)."),
 ("MRK.11.28", "Vollmacht", "interpretive", "ἐξουσίᾳ", None, ["Autorität", "Befuegnis"], "ἐξουσία isch d Befuegnis, wo mer überchunnt, zum handle. D Frag zielt druf, wär de Jesus dezue ermächtiget hät (vgl. [[MRK.1.22]])."),
 ("MRK.12.1", "Wiibuure", "interpretive", "γεωργοῖς", "Buure", ["Pächter"], "γεωργός isch de Buur; da Pächter, wo em Bsitzer en Teil vom Ertrag schuldig sind. S Bild nimmt [[ISA.5.1-ISA.5.7]] uf (Wiibärg, Haag, Trotte, Turm)."),
 ("MRK.12.6", "en gliebte", "literal", "ἀγαπητόν", None, ["sin einzig"], "ἀγαπητός staat i de griechische Bibel au für de «einzig» Sohn ([[GEN.22.2]]). Aaklang a d Stimm us em Himmel i [[MRK.1.11]] und [[MRK.9.7]]."),
 ("MRK.12.10", "zum Eckstei", "interpretive", "κεφαλὴν γωνίας", "zum Chopf vo de Egge", ["zum Schlussstei"], "Zitat us [[PSA.118.22-PSA.118.23]]. Gmeint isch en Stei a ere bsundere Stell: en Eckstei im Fundament oder en Schlussstei obe; beides wird vertrette."),
 ("MRK.12.14", "Stüür", "interpretive", "κῆνσον", "Census", ["Chopfstüür"], "Lehnwort us em Latiinische (census): di direkt Stüür a Rom, z Judäa sit de Iigliederig als Provinz (6 n. Chr.) iizoge und umstritte."),
 ("MRK.12.17", "gänd em Kaiser", "interpretive", "ἀπόδοτε Καίσαρι", "gänd em Kaiser zrugg", ["zaled em Kaiser"], "ἀποδίδωμι heisst «zruggää, gää, was mer schuldig isch»; i de Frag isch δοῦναι «gää» gstande ([[MRK.12.14]]). Öb de Satz zwei Bereich näbenand stellt oder de Kaiser under Gott stellt, isch umstritte."),
 ("MRK.12.29", "Los, Israel: De Herr, üse Gott, de Herr isch eine", "literal", "Ἄκουε Ἰσραήλ κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν", None, ["De Herr isch üse Gott, de Herr elei", "De Herr, üse Gott, isch de einzig Herr"], "S «Schma Israel» ([[DEU.6.4-DEU.6.5]]) nach de griechische Fassig. κύριος staat det für de Gottesname JHWH. Mer cha de Satz als Ussag über d Einzigkeit vo Gott, über sini Einheit oder als Bekänntnis läse, dass Israel nu a ihn bunde isch; d Widergab bliibt bim Wortlut. «Los» isch s züritüütsche Wort für «hör zue»."),
 ("MRK.12.30", "Dänke", "interpretive", "διανοίας", None, ["Verstand", "Gmüet"], "[[DEU.6.5]] nännt im Hebräische drü Glider (Härz, Seel, Chraft); de Markus hät vier, mit διάνοια «Dänke, Verstand»."),
 ("MRK.12.35", "Christus", "literal", "χριστὸς", None, ["Messias", "Gsalbte"], "χριστός heisst «Gsalbte», griechisch für hebräisch Maschiach. Da en Titel, nöd de Name vo Jesus."),
 ("MRK.12.36", "De Herr hät zu mim Herr gseit", "literal", "Εἶπεν κύριος τῷ κυρίῳ μου", None, None, "Zitat us [[PSA.110.1]]. Im Hebräische redt JHWH zu «mim Herr»; im Griechische staat zweimal κύριος."),
 ("MRK.12.41", "Opferstock", "interpretive", "γαζοφυλακίου", "Schatzchammere", None, "γαζοφυλάκιον isch d Schatzchammere; da wahrschiinli d Behälter für Spände im Tämpelbezirk."),
 ("MRK.12.44", "Läbesunderhalt", "interpretive", "βίον", "Läbe", ["alles, wo si devo gläbt hät"], "βίος isch s Läbe und das, wo mer devo läbt."),
 ("MRK.13.6", "bins", "interpretive", "εἰμι", "bi", None, "Ἐγώ εἰμι cha heisse «Ich bin s (de Erwartet)». D Wändig tönt a d Sälbschtvorstellig vo Gott aa ([[EXO.3.14]], [[ISA.43.10]])."),
 ("MRK.13.14", "de Gröiel vo de Verwüeschtig", "traditional", "τὸ βδέλυγμα τῆς ἐρημώσεως", "de Abscheu vo de Verödig", ["s verwüeschtend Schüüsal"], "Usdruck us em Danielbuech ([[DAN.9.27]], [[DAN.11.31]], [[DAN.12.11]]); det für de heidnisch Altar im Tämpel under em Antiochus IV. (vgl. [[1MA.1.54]]). De Markus setzt s Partizip ἑστηκότα männlich, obwohl βδέλυγμα sächlich isch; villicht isch e Person gmeint, drum «wo er nöd darf». Wo d Stell druf zielt (Entweihig vom Tämpel im Jüdische Chrieg 66–70, de Plan vom Caligula, um 40 n. Chr. e Statue im Tämpel ufzstelle, e Gstalt vo de Ändziit), isch umstritte."),
 ("MRK.13.26", "de Mänschesohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None, "Aaspilig uf [[DAN.7.13]]: eine «wie en Mänschesohn» chunnt mit de Wolche vom Himmel. Bim Markus nännt sich de Jesus sälber so."),
 ("MRK.13.29", "dass s nöch vor de Tür isch", "interpretive", "ὅτι ἐγγύς ἐστιν ἐπὶ θύραις", "dass nöch isch a de Türe", ["dass er nöch vor de Tür isch"], "S Subjekt fäält: Gmeint cha «er» sii (de Mänschesohn, [[MRK.13.26]]) oder «es» (s Änd, das, wo aagchündet isch)."),
 ("MRK.13.30", "Die Generation", "interpretive", "ἡ γενεὰ αὕτη", None, ["Die Art vo Mänsche", "Das Volk"], "γενεά meint meischt d Mänsche vo ere Ziit, e Generation (vgl. [[MRK.8.12]], [[MRK.8.38]], [[MRK.9.19]]). Dänn bezieht sich «das alles» entweder uf das, wo bis zur Zerstörig vom Tämpel (70 n. Chr.) passiert isch, oder es stellt sich d Frag, werum d Widerchunft uusbliibe isch. Anderi verstönd γενεά wiiter (d Mänschheit, s jüdisch Volk). «Gschlächt» seit mer i de Mundart chuum; drum «Generation». D hochdüütschi Fassig hät «Geschlecht»."),
 ("MRK.13.32", "au nöd de Sohn, nu de Vatter", "literal", "οὐδὲ ὁ υἱός εἰ μὴ ὁ πατήρ", None, None, "Di einzig Stell bim Markus, wo sich de Jesus eifach «de Sohn» nännt. Dass de Sohn Tag und Stund nöd kännt, hät di spötere Debatte über d Person vo Christus beschäftiget; de Markus seit s ohni Abschwächig."),
 ("MRK.13.35", "wänn de Güggel chräit", "adapted", "ἀλεκτοροφωνίας", "Haneschrei", None, "Di vier Nachtwache nach römischer Zellig. De Haneschrei wiist uf [[MRK.14.72]] voruus."),
]

# Lesarten, die die Übersetzung verändern: (Lesart, Stelle, de von, de zu, gsw von, gsw zu, Wirkung, Hinweis de, Hinweis gsw,
#  Wörter {Lesart: [(griechisch, de, Hinweis)]}, Wörter gsw, Entstehung de, Entstehung gsw)
ALTS = [
 ("VAR-SBLGNTAPP-MRK-011-003-03:R2", "MRK.11.3", "er schickt es sofort wieder hierher", "er schickt es sofort hierher", "er schickt s grad wider da häre", "er schickt s grad da häre", "mittel",
  "Ohne «wieder» spricht der Satz eher vom Besitzer, der das Tier sofort hergibt; mit «wieder» verspricht Jesus, es zurückzuschicken.", "Ohni «wider» redt de Satz ehner vom Bsitzer, wo s Tier grad häregit; mit «wider» verspricht de Jesus, s zruggzschicke.",
  {"R1": [("πάλιν", "wieder", "SBLGNT")], "R2": [("–", "ohne «wieder»", "")]},
  {"R1": [("πάλιν", "wider", "SBLGNT")], "R2": [("–", "ohni «wider»", "")]},
  ["«Wieder» kann ausgefallen sein, weil man den Satz als Zusage des Besitzers verstand; es kann auch ergänzt worden sein, um die Rückgabe ausdrücklich zu machen.",
   "Laut der automatischen Zuordnung haben Sinaiticus, Vaticanus (mit anderer Wortfolge) und Bezae «wieder», Alexandrinus und Washingtonianus nicht. Ephraemi wird knapp der Lesart ohne «wieder» zugeordnet, obwohl der erfasste Wortlaut πάλιν (teilweise unsicher gelesen) enthält; die Zuordnung ist dort unsicher."],
  ["«Wider» cha usgfalle sii, wil mer de Satz als Zuesag vom Bsitzer verstande hät; es cha au ergänzt worde sii, demit d Rückgab usdrücklich wird.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Vaticanus (mit andere Wortfolg) und de Bezae «wider», de Alexandrinus und de Washingtonianus nöd. De Ephraemi wird knapp de Läsart ohni «wider» zueteilt, obwohl im erfasste Wortlut πάλιν staat (zum Teil unsicher gläse); d Zueornig isch det unsicher."]),
 ("VAR-SBLGNTAPP-MRK-011-008-02:R2", "MRK.11.8", "andere aber Zweige, die sie auf den Feldern abgeschnitten hatten", "andere aber hieben Zweige von den Bäumen und streuten sie auf den Weg", "anderi aber Zweig, wo si uf de Fälder abghaue händ", "anderi aber händ Zweig vo de Bäum abghaue und uf de Wäg gstreut", "gering",
  "Die Zweige kommen von den Bäumen statt von den Feldern und werden ausdrücklich auf den Weg gestreut.", "D Zweig chömed vo de Bäum statt vo de Fälder und wärded usdrücklich uf de Wäg gstreut.",
  {"R1": [("κόψαντες ἐκ τῶν ἀγρῶν", "die sie auf den Feldern abgeschnitten hatten", "SBLGNT")], "R2": [("ἔκοπτον ἐκ τῶν δένδρων καὶ ἐστρώννυον εἰς τὴν ὁδόν", "hieben von den Bäumen und streuten auf den Weg", "")]},
  {"R1": [("κόψαντες ἐκ τῶν ἀγρῶν", "wo si uf de Fälder abghaue händ", "SBLGNT")], "R2": [("ἔκοπτον ἐκ τῶν δένδρων καὶ ἐστρώννυον εἰς τὴν ὁδόν", "händ vo de Bäum abghaue und uf de Wäg gstreut", "")]},
  ["Die längere Fassung entspricht fast wörtlich [[MAT.21.8]]; Angleichung an Matthäus liegt nahe.",
   "Laut der automatischen Zuordnung lesen Sinaiticus und Vaticanus «von den Feldern», Alexandrinus und Bezae «von den Bäumen … auf den Weg». Washingtonianus und Ephraemi lesen anders als beide Lesarten."],
  ["Di länger Fassig entspricht fascht wörtlich [[MAT.21.8]]; e Aagliichig a de Matthäus liit nooch.",
   "Nach de automatische Zueornig läsed de Sinaiticus und de Vaticanus «vo de Fälder», de Alexandrinus und de Bezae «vo de Bäum … uf de Wäg». De Washingtonianus und de Ephraemi läsed anders als beidi Läsarte."]),
 ("VAR-SBLGNTAPP-MRK-011-010-01:R2", "MRK.11.10", "Gesegnet sei das kommende Reich unseres Vaters David", "Gesegnet sei das kommende Reich im Namen des Herrn, unseres Vaters David", "Gsägnet sig s Riich vo üsem Vatter David, wo chunnt", "Gsägnet sig s Riich im Name vom Herr, vo üsem Vatter David, wo chunnt", "gering",
  "Der Zusatz wiederholt die Wendung aus dem vorangehenden Vers.", "De Zuesatz widerholt d Wändig us em Vers vorhär.",
  {"R1": [("βασιλεία", "Reich", "SBLGNT")], "R2": [("βασιλεία ἐν ὀνόματι κυρίου", "Reich im Namen des Herrn", "")]},
  {"R1": [("βασιλεία", "Riich", "SBLGNT")], "R2": [("βασιλεία ἐν ὀνόματι κυρίου", "Riich im Name vom Herr", "")]},
  ["Angleichung an [[MRK.11.9]] («im Namen des Herrn») liegt nahe.",
   "Laut der automatischen Zuordnung hat Alexandrinus den Zusatz; Sinaiticus, Vaticanus, Washingtonianus, Ephraemi und Bezae haben ihn nicht."],
  ["E Aagliichig a [[MRK.11.9]] («im Name vom Herr») liit nooch.",
   "Nach de automatische Zueornig hät de Alexandrinus de Zuesatz; de Sinaiticus, de Vaticanus, de Washingtonianus, de Ephraemi und de Bezae händ en nöd."]),
 ("VAR-SBLGNTAPP-MRK-011-024-02:R2", "MRK.11.24", "dass ihr es empfangen habt", "dass ihr es empfangt", "dass ir s übercho händ", "dass ir s überchömed", "mittel",
  "Statt der Vergangenheit (schon empfangen) steht die Gegenwart.", "Statt de Vergangeheit (scho übercho) staat d Gägewart.",
  {"R1": [("ἐλάβετε", "ihr habt empfangen", "SBLGNT, Aorist")], "R2": [("λαμβάνετε", "ihr empfangt", "Präsens")]},
  {"R1": [("ἐλάβετε", "ir händ übercho", "SBLGNT, Aorist")], "R2": [("λαμβάνετε", "ir überchömed", "Präsens")]},
  ["Die Vergangenheitsform ist die schwierigere Lesart; Abschreiber haben sie eher geglättet als eingeführt.",
   "Laut der automatischen Zuordnung lesen Sinaiticus, Vaticanus, Washingtonianus und Ephraemi die Vergangenheit, Alexandrinus die Gegenwart; Bezae liest anders (im erfassten Wortlaut eine Zukunftsform)."],
  ["D Vergangeheitsform isch di schwirigeri Läsart; Abschriiber händ si ehner glättet als iigfüert.",
   "Nach de automatische Zueornig läsed de Sinaiticus, de Vaticanus, de Washingtonianus und de Ephraemi d Vergangeheit, de Alexandrinus d Gägewart; de Bezae list anders (im erfasste Wortlut e Zuekunftsform)."]),
 ("VAR-SBLGNTAPP-MRK-011-025-02:R2", "MRK.11.25", "eure Verfehlungen vergibt.»", "eure Verfehlungen vergibt. [[MRK.11.26]] Wenn ihr aber nicht vergebt, wird auch euer Vater im Himmel eure Verfehlungen nicht vergeben.»", "eui Verfehlige vergit.»", "eui Verfehlige vergit. [[MRK.11.26]] Wänn ir aber nöd vergänd, wird au eue Vatter im Himmel eui Verfehlige nöd vergää.»", "mittel",
  "Mit dem Zusatz folgt ein ganzer Vers ([[MRK.11.26]] in der KJV-Zählung), der die Vergebung unter Bedingung stellt.", "Mit em Zuesatz chunnt en ganze Vers ([[MRK.11.26]] i de KJV-Zellig) dezue, wo d Vergäbig a e Bedingig chnüpft.",
  {"R1": [("ὑμῶν", "eure (Verfehlungen)", "SBLGNT, ohne Vers 26")], "R2": [("ὑμῶν Εἰ δὲ ὑμεῖς οὖκ ἀφίετε, οὐδὲ ὁ πατὴρ ὑμῶν ὁ ἐν τοῖς οὐρανοῖς ἀφήσει τὰ παραπτώματα ὑμῶν", "eure (Verfehlungen). Wenn ihr aber nicht vergebt, wird auch euer Vater im Himmel eure Verfehlungen nicht vergeben", "Wortlaut wie im SBLGNT-Apparat")]},
  {"R1": [("ὑμῶν", "eui (Verfehlige)", "SBLGNT, ohni Vers 26")], "R2": [("ὑμῶν Εἰ δὲ ὑμεῖς οὖκ ἀφίετε, οὐδὲ ὁ πατὴρ ὑμῶν ὁ ἐν τοῖς οὐρανοῖς ἀφήσει τὰ παραπτώματα ὑμῶν", "eui (Verfehlige). Wänn ir aber nöd vergänd, wird au eue Vatter im Himmel eui Verfehlige nöd vergää", "Wortlut wie im SBLGNT-Apparat")]},
  ["Der Vers entspricht fast wörtlich [[MAT.6.15]] und kann von dort ergänzt worden sein; ein Ausfall durch das Auge eines Abschreibers, das vom einen «eure Verfehlungen» zum anderen sprang, wird ebenfalls erwogen.",
   "Die automatische Zuordnung hat nur den Wortlaut bis zum Ende von [[MRK.11.25]] verglichen und alle erfassten Handschriften der Lesart ohne Zusatz zugeordnet. Ob in ihnen [[MRK.11.26]] folgt, lässt sich daraus nicht ablesen."],
  ["De Vers entspricht fascht wörtlich [[MAT.6.15]] und cha vo det ergänzt worde sii; mer überleit au, öb er usgfalle isch, wil s Aug vo me Abschriiber vom eint «eui Verfehlige» zum andere gumpet isch.",
   "D automatisch Zueornig hät nu de Wortlut bis as Änd vo [[MRK.11.25]] vergliche und alli erfasste Handschrifte de Läsart ohni Zuesatz zueteilt. Öb bi ine [[MRK.11.26]] folgt, cha mer drus nöd abläse."]),
 ("VAR-SBLGNTAPP-MRK-011-031-02:R2", "MRK.11.31", "«Was sollen wir sagen? Wenn wir sagen", "«Wenn wir sagen", "«Was söled mer säge? Wänn mer säged", "«Wänn mer säged", "gering",
  "Die Frage «Was sollen wir sagen?» steht nur im SBLGNT; die übrigen verglichenen Editionen haben sie nicht.", "D Frag «Was söled mer säge?» staat nu im SBLGNT; di andere verglichne Usgabe händ si nöd.",
  {"R1": [("Τί εἴπωμεν", "Was sollen wir sagen?", "SBLGNT (Holmes)")], "R2": [("–", "ohne diese Frage", "WH, Treg, NA28, RP")]},
  {"R1": [("Τί εἴπωμεν", "Was söled mer säge?", "SBLGNT (Holmes)")], "R2": [("–", "ohni die Frag", "WH, Treg, NA28, RP")]},
  ["Die Frage kann als lebhafte Einleitung der Überlegung ergänzt worden sein; sie kann auch ausgefallen sein, weil das folgende «wenn wir sagen» gleich anfängt (εἴπωμεν … εἴπωμεν).",
   "Laut der automatischen Zuordnung hat nur Bezae die Frage; Papyrus 45, Sinaiticus, Alexandrinus, Vaticanus, Washingtonianus und Ephraemi haben sie nicht. Unter den hier erfassten Handschriften stützt also nur Bezae den Text des SBLGNT, der an dieser Stelle der Ausgabe von Holmes folgt; über die übrige Überlieferung sagen diese Daten nichts."],
  ["D Frag cha als läbhafti Iileitig vo de Überlegig ergänzt worde sii; si cha au usgfalle sii, wil s nächscht «wänn mer säged» gliich aafangt (εἴπωμεν … εἴπωμεν).",
   "Nach de automatische Zueornig hät nu de Bezae d Frag; de Papyrus 45, de Sinaiticus, de Alexandrinus, de Vaticanus, de Washingtonianus und de Ephraemi händ si nöd. Under de erfasste Handschrifte stützt also nu de Bezae de Text vom SBLGNT, wo da de Usgab vom Holmes folgt; über di übrig Überlieferig säged die Date nüt."]),
 ("VAR-SBLGNTAPP-MRK-012-004-01:R2", "MRK.12.4", "auch den schlugen sie auf den Kopf", "auch den steinigten sie und schlugen ihn auf den Kopf", "au dä händ si uf de Chopf gschlage", "au dä händ si gsteiniget und uf de Chopf gschlage", "gering",
  "Der Zusatz steigert die Gewalt gegen den zweiten Knecht.", "De Zuesatz steigeret d Gwalt gäge de zweit Chnächt.",
  {"R1": [("κἀκεῖνον", "auch den", "SBLGNT")], "R2": [("κἀκεῖνον λιθοβολήσαντες", "auch den steinigten sie", "")]},
  {"R1": [("κἀκεῖνον", "au dä", "SBLGNT")], "R2": [("κἀκεῖνον λιθοβολήσαντες", "au dä händ si gsteiniget", "")]},
  ["Angleichung an [[MAT.21.35]], wo von Steinigung die Rede ist, liegt nahe.",
   "Laut der automatischen Zuordnung haben Alexandrinus und Ephraemi den Zusatz, Sinaiticus, Vaticanus und Washingtonianus (dieser mit abweichender Form) nicht; Bezae liest anders, im erfassten Wortlaut ohne Steinigung."],
  ["E Aagliichig a [[MAT.21.35]], wo vo Steinige d Red isch, liit nooch.",
   "Nach de automatische Zueornig händ de Alexandrinus und de Ephraemi de Zuesatz, de Sinaiticus, de Vaticanus und de Washingtonianus (dä mit ere andere Form) nöd; de Bezae list anders, im erfasste Wortlut ohni Steinige."]),
 ("VAR-SBLGNTAPP-MRK-012-023-01:R2", "MRK.12.23", "In der Auferstehung, wenn sie auferstehen:", "In der Auferstehung:", "I de Uferstehig, wänn si uferstönd:", "I de Uferstehig:", "gering",
  "Ohne den Nebensatz fehlt nur die Verdoppelung «Auferstehung – auferstehen».", "Ohni de Nebesatz fäält nu d Verdopplig «Uferstehig – uferstaa».",
  {"R1": [("ὅταν ἀναστῶσιν", "wenn sie auferstehen", "SBLGNT, NA28, RP")], "R2": [("–", "ohne Nebensatz", "WH, Treg")]},
  {"R1": [("ὅταν ἀναστῶσιν", "wänn si uferstönd", "SBLGNT, NA28, RP")], "R2": [("–", "ohni Nebesatz", "WH, Treg")]},
  ["Die Doppelung passt zum Stil des Markus und kann als überflüssig gestrichen worden sein; sie kann auch als Verdeutlichung hinzugekommen sein.",
   "Laut der automatischen Zuordnung hat Alexandrinus den Nebensatz; Sinaiticus, Vaticanus, Washingtonianus, Ephraemi und Bezae haben ihn nicht."],
  ["D Doppelig passt zum Stil vom Markus und cha als überflüssig gstriche worde sii; si cha au als Verdüütlichig dezuecho sii.",
   "Nach de automatische Zueornig hät de Alexandrinus de Nebesatz; de Sinaiticus, de Vaticanus, de Washingtonianus, de Ephraemi und de Bezae händ en nöd."]),
 ("VAR-SBLGNTAPP-MRK-012-030-02:R2", "MRK.12.30", "mit deiner ganzen Kraft.›", "mit deiner ganzen Kraft.› Das ist das erste Gebot.", "mit dinere ganze Chraft.›", "mit dinere ganze Chraft.› Das isch s erscht Gebot.", "gering",
  "Der Zusatz schliesst die Antwort auf die Frage nach dem ersten Gebot ausdrücklich ab.", "De Zuesatz schlüüsst d Antwort uf d Frag nach em erschte Gebot usdrücklich ab.",
  {"R1": [("σου", "dein(er Kraft)", "SBLGNT")], "R2": [("σου αὕτη πρώτη ἐντολή", "dein(er Kraft). Das ist das erste Gebot", "")]},
  {"R1": [("σου", "din(ere Chraft)", "SBLGNT")], "R2": [("σου αὕτη πρώτη ἐντολή", "din(ere Chraft). Das isch s erscht Gebot", "")]},
  ["Der Satz kann ergänzt worden sein, um die Antwort mit «das zweite» ([[MRK.12.31]]) zu verklammern (vgl. [[MAT.22.38]]).",
   "Laut der automatischen Zuordnung haben Alexandrinus und Bezae den Zusatz, Sinaiticus, Vaticanus und Washingtonianus nicht."],
  ["De Satz cha ergänzt worde sii, demit d Antwort mit «s zweit» ([[MRK.12.31]]) zämeghebt wird (vgl. [[MAT.22.38]]).",
   "Nach de automatische Zueornig händ de Alexandrinus und de Bezae de Zuesatz, de Sinaiticus, de Vaticanus und de Washingtonianus nöd."]),
 ("VAR-SBLGNTAPP-MRK-012-033-02:R2", "MRK.12.33", "mit ganzem Verstand", "mit ganzem Verstand und mit ganzer Seele", "mit ganzem Verstand", "mit ganzem Verstand und mit ganzer Seel", "gering",
  "Mit dem Zusatz nennt der Schriftgelehrte vier statt drei Glieder.", "Mit em Zuesatz nännt de Schriftgleert vier statt drü Glider.",
  {"R1": [("συνέσεως", "Verstand", "SBLGNT")], "R2": [("συνέσεως καὶ ἐξ ὅλης τῆς ψυχῆς", "Verstand und mit ganzer Seele", "")]},
  {"R1": [("συνέσεως", "Verstand", "SBLGNT")], "R2": [("συνέσεως καὶ ἐξ ὅλης τῆς ψυχῆς", "Verstand und mit ganzer Seel", "")]},
  ["Angleichung an die vollständigere Aufzählung in [[MRK.12.30]] liegt nahe.",
   "Die automatische Zuordnung ordnet hier alle erfassten Handschriften der Lesart mit Zusatz zu, aber mit sehr knappem Abstand und ebenso die Ausgabe von Westcott/Hort, deren Text den Zusatz nicht hat; die Zuordnung ist an dieser Stelle unzuverlässig. Im erfassten Wortlaut steht «Seele» bei Alexandrinus und Bezae (Bezae auch sonst abweichend), nicht bei Sinaiticus, Vaticanus und Washingtonianus."],
  ["E Aagliichig a di vollständiger Uufzellig i [[MRK.12.30]] liit nooch.",
   "D automatisch Zueornig teilt da alli erfasste Handschrifte de Läsart mit Zuesatz zue, aber mit sehr knappem Abstand und gliich au d Usgab vo Westcott/Hort, wo de Zuesatz nöd hät; d Zueornig isch a dere Stell unzueverlässig. Im erfasste Wortlut staat «Seel» bim Alexandrinus und bim Bezae (dä au suscht abwiichend), nöd bim Sinaiticus, bim Vaticanus und bim Washingtonianus."]),
 ("VAR-SBLGNTAPP-MRK-012-036-06:R2", "MRK.12.36", "unter deine Füsse lege", "zum Schemel deiner Füsse mache", "under dini Füess lege", "zum Schämel vo dine Füess mache", "gering",
  "Das Bild bleibt gleich: die Feinde werden unterworfen.", "S Bild bliibt gliich: d Find wärded underworfe.",
  {"R1": [("ὑποκάτω", "unter", "SBLGNT")], "R2": [("ὑποπόδιον", "(zum) Schemel", "")]},
  {"R1": [("ὑποκάτω", "under", "SBLGNT")], "R2": [("ὑποπόδιον", "(zum) Schämel", "")]},
  ["ὑποπόδιον ist der Wortlaut der griechischen Fassung von [[PSA.110.1]]; Abschreiber können an das bekannte Psalmwort angeglichen haben. Umgekehrt kann ὑποκάτω aus [[MAT.22.44]] stammen.",
   "Laut der automatischen Zuordnung lesen Sinaiticus und Alexandrinus «Schemel», Vaticanus, Washingtonianus und Bezae «unter». Ephraemi ist hier nicht erhalten."],
  ["ὑποπόδιον isch de Wortlut vo de griechische Fassig vo [[PSA.110.1]]; Abschriiber chönd sich a s bekannt Psalmwort aaglehnt ha. Umgekeert cha ὑποκάτω us [[MAT.22.44]] stamme.",
   "Nach de automatische Zueornig läsed de Sinaiticus und de Alexandrinus «Schämel», de Vaticanus, de Washingtonianus und de Bezae «under». De Ephraemi isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-013-008-03:R2", "MRK.13.8", "es wird Hungersnöte geben", "es wird Hungersnöte und Unruhen geben", "es wird Hungersnöt gää", "es wird Hungersnöt und Unrue gää", "gering",
  "Die Aufzählung der Nöte wird um «Unruhen» erweitert.", "D Uufzellig vo de Nöt wird um «Unrue» erwiitert.",
  {"R1": [("λιμοί", "Hungersnöte", "SBLGNT")], "R2": [("λιμοί καὶ ταραχαί", "Hungersnöte und Unruhen", "")]},
  {"R1": [("λιμοί", "Hungersnöt", "SBLGNT")], "R2": [("λιμοί καὶ ταραχαί", "Hungersnöt und Unrue", "")]},
  ["Erweiterungen solcher Aufzählungen sind beim Abschreiben häufig; ein Ausfall des Wortes ist ebenfalls möglich.",
   "Laut der automatischen Zuordnung hat Alexandrinus (Erstschrift und Korrektur) den Zusatz, Vaticanus und Bezae nicht. Sinaiticus liest anders (im erfassten Wortlaut ohne «Hungersnöte»); Washingtonianus liest ebenfalls anders, im erfassten Wortlaut stehen dort «Hungersnöte» und «Unruhen» in anderer Anordnung. Ephraemi ist hier nicht erhalten."],
  ["Erwiiterige vo settige Uufzellige sind bim Abschriibe hüüfig; dass s Wort usgfalle isch, isch au mögli.",
   "Nach de automatische Zueornig hät de Alexandrinus (Erschtschrift und Korrektur) de Zuesatz, de Vaticanus und de Bezae nöd. De Sinaiticus list anders (im erfasste Wortlut ohni «Hungersnöt»); de Washingtonianus list au anders, im erfasste Wortlut stönd det «Hungersnöt» und «Unrue» i andere Aaornig. De Ephraemi isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-013-014-01:R2", "MRK.13.14", "den Gräuel der Verwüstung dort stehen seht, wo er nicht darf", "den Gräuel der Verwüstung, von dem der Prophet Daniel gesprochen hat, dort stehen seht, wo er nicht darf", "de Gröiel vo de Verwüeschtig det staa gsehnd, wo er nöd darf", "de Gröiel vo de Verwüeschtig, vo dem de Prophet Daniel gredt hät, det staa gsehnd, wo er nöd darf", "mittel",
  "Der Zusatz nennt die Quelle des Ausdrucks; ausserdem steht das Partizip sächlich (ἑστώς), sodass der Hinweis auf eine Person entfällt.", "De Zuesatz nännt d Quelle vom Usdruck; usserdem staat s Partizip sächlich (ἑστώς), so dass de Hiiwiis uf e Person wägfallt.",
  {"R1": [("ἑστηκότα", "stehend (männlich)", "SBLGNT")], "R2": [("τὸ ῥηθὲν ὑπὸ Δανιὴλ τοῦ προφήτου ἑστὼς", "von dem der Prophet Daniel gesprochen hat, stehend (sächlich)", "")]},
  {"R1": [("ἑστηκότα", "stönd (männlich)", "SBLGNT")], "R2": [("τὸ ῥηθὲν ὑπὸ Δανιὴλ τοῦ προφήτου ἑστὼς", "vo dem de Prophet Daniel gredt hät, stönd (sächlich)", "")]},
  ["Der Zusatz entspricht [[MAT.24.15]]; Angleichung an Matthäus und grammatische Glättung des männlichen Partizips liegen nahe.",
   "Laut der automatischen Zuordnung hat Alexandrinus den Zusatz, Sinaiticus und Vaticanus nicht. Washingtonianus und Bezae lesen anders: im erfassten Wortlaut ohne Daniel-Zusatz, aber mit einer sächlichen Partizipform. Ephraemi ist hier nicht erhalten."],
  ["De Zuesatz entspricht [[MAT.24.15]]; e Aagliichig a de Matthäus und e grammatischi Glättig vom männliche Partizip liged nooch.",
   "Nach de automatische Zueornig hät de Alexandrinus de Zuesatz, de Sinaiticus und de Vaticanus nöd. De Washingtonianus und de Bezae läsed anders: im erfasste Wortlut ohni Daniel-Zuesatz, aber mit ere sächliche Partizipform. De Ephraemi isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-013-018-01:R2", "MRK.13.18", "dass es nicht im Winter geschieht", "dass eure Flucht nicht im Winter geschieht", "dass s nöd im Winter passiert", "dass eui Flucht nöd im Winter passiert", "gering",
  "Der Zusatz nennt ausdrücklich, was nicht im Winter geschehen soll.", "De Zuesatz seit usdrücklich, was nöd im Winter söll passiere.",
  {"R1": [("γένηται", "es geschieht", "SBLGNT")], "R2": [("γένηται ἡ φυγὴ ὑμῶν", "eure Flucht geschieht", "")]},
  {"R1": [("γένηται", "es passiert", "SBLGNT")], "R2": [("γένηται ἡ φυγὴ ὑμῶν", "eui Flucht passiert", "")]},
  ["Angleichung an [[MAT.24.20]] liegt nahe.",
   "Laut der automatischen Zuordnung hat Alexandrinus den Zusatz, Sinaiticus, Vaticanus und Washingtonianus nicht; Bezae liest anders. Ephraemi ist hier nicht erhalten."],
  ["E Aagliichig a [[MAT.24.20]] liit nooch.",
   "Nach de automatische Zueornig hät de Alexandrinus de Zuesatz, de Sinaiticus, de Vaticanus und de Washingtonianus nöd; de Bezae list anders. De Ephraemi isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-013-033-01:R2", "MRK.13.33", "bleibt wach!", "bleibt wach und betet!", "bliibed wach!", "bliibed wach und bätted!", "gering",
  "Zur Wachsamkeit kommt das Gebet.", "Zum Wach-Bliibe chunnt s Bätte dezue.",
  {"R1": [("ἀγρυπνεῖτε", "bleibt wach", "SBLGNT")], "R2": [("ἀγρυπνεῖτε καὶ προσεύχεσθε", "bleibt wach und betet", "")]},
  {"R1": [("ἀγρυπνεῖτε", "bliibed wach", "SBLGNT")], "R2": [("ἀγρυπνεῖτε καὶ προσεύχεσθε", "bliibed wach und bätted", "")]},
  ["Der Zusatz kann aus [[MRK.14.38]] («Wacht und betet») stammen; er kann auch beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung haben Sinaiticus, Alexandrinus, Washingtonianus und Ephraemi den Zusatz, Vaticanus und Bezae nicht. Hier stehen frühe Handschriften auf beiden Seiten."],
  ["De Zuesatz cha us [[MRK.14.38]] («Bliibed wach und bätted») stamme; er cha au bim Abschriibe usgfalle sii.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Alexandrinus, de Washingtonianus und de Ephraemi de Zuesatz, de Vaticanus und de Bezae nöd. Da stönd früeni Handschrifte uf beidne Siite."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung)
 ("TU-MRK-011-001-033", "MRK.11.1-MRK.11.33", "section", "Jesus kommt nach Jerusalem",
  ["TU-MRK-011-001-011", "TU-MRK-011-012-014", "TU-MRK-011-015-019", "TU-MRK-011-020-025", "TU-MRK-011-027-033"],
  "Jesus zieht auf einem Fohlen in Jerusalem ein, begleitet von Hosanna-Rufen. Er verflucht einen Feigenbaum ohne Frucht, vertreibt Händler aus dem Tempel und spricht vom Glauben, vom Gebet und von der Vergebung. Die Führenden in Jerusalem stellen seine Vollmacht in Frage. Der Vers [[MRK.11.26]] der KJV-Zählung fehlt im zugrunde gelegten Text."),
 ("TU-MRK-011-001-011", "MRK.11.1-MRK.11.11", "narrative", "Einzug in Jerusalem", None,
  "Zwei Jünger holen ein Fohlen, wie Jesus es angesagt hat. Jesus reitet nach Jerusalem; die Menge breitet Mäntel und Zweige aus und ruft: «Hosanna! Gesegnet sei, der kommt im Namen des Herrn!» Am Abend schaut er sich im Tempel um und kehrt nach Betanien zurück."),
 ("TU-MRK-011-012-014", "MRK.11.12-MRK.11.14", "narrative", "Der Feigenbaum ohne Frucht", None,
  "Jesus hat Hunger, findet an einem Feigenbaum nur Blätter, obwohl nicht die Zeit der Feigen ist, und sagt, niemand solle je wieder Frucht von ihm essen."),
 ("TU-MRK-011-015-019", "MRK.11.15-MRK.11.19", "narrative", "Jesus im Tempel", None,
  "Jesus treibt Verkäufer und Käufer aus dem Tempel, stösst die Tische der Geldwechsler um und lehrt mit Jesaja und Jeremia: Das Haus Gottes soll ein Haus des Gebets für alle Völker sein, ist aber eine Räuberhöhle geworden. Die Hohepriester und Schriftgelehrten suchen ihn zu töten, fürchten aber die Menge."),
 ("TU-MRK-011-020-025", "MRK.11.20-MRK.11.25", "narrative", "Der verdorrte Feigenbaum: Glaube, Gebet, Vergebung", None,
  "Am Morgen ist der Feigenbaum verdorrt. Jesus ruft zum Glauben an Gott auf: Wer nicht zweifelt, kann Berge versetzen; wer betet, soll mit der Erhörung rechnen und denen vergeben, gegen die er etwas hat."),
 ("TU-MRK-011-027-033", "MRK.11.27-MRK.11.33", "dialogue", "Die Frage nach der Vollmacht", None,
  "Hohepriester, Schriftgelehrte und Älteste fragen Jesus, in welcher Vollmacht er handelt. Er stellt die Gegenfrage nach der Taufe des Johannes. Weil sie aus Furcht vor der Menge nicht antworten, gibt auch er keine Antwort."),
 ("TU-MRK-012-001-044", "MRK.12.1-MRK.12.44", "section", "Streitgespräche im Tempel",
  ["TU-MRK-012-001-012", "TU-MRK-012-013-017", "TU-MRK-012-018-027", "TU-MRK-012-028-034", "TU-MRK-012-035-037", "TU-MRK-012-038-040", "TU-MRK-012-041-044"],
  "Im Tempel erzählt Jesus das Gleichnis von den Weinbauern, die den Sohn des Besitzers töten. Verschiedene Gruppen stellen ihm Fangfragen: zur Steuer an den Kaiser, zur Auferstehung, zum ersten Gebot. Jesus fragt selbst, wie der Christus Davids Sohn sein kann, warnt vor geltungssüchtigen Schriftgelehrten und lobt die Gabe einer armen Witwe."),
 ("TU-MRK-012-001-012", "MRK.12.1-MRK.12.12", "discourse", "Das Gleichnis von den Weinbauern", None,
  "Ein Mensch verpachtet einen Weinberg. Die Weinbauern misshandeln und töten die Knechte, die den Ertrag holen sollen, und schliesslich den geliebten Sohn. Jesus schliesst mit dem Psalmwort vom verworfenen Stein, der zum Eckstein wurde. Die Führenden merken, dass das Gleichnis ihnen gilt."),
 ("TU-MRK-012-013-017", "MRK.12.13-MRK.12.17", "dialogue", "Die Frage nach der Steuer", None,
  "Pharisäer und Herodianer fragen, ob man dem Kaiser Steuer zahlen darf. Jesus lässt sich einen Denar zeigen und antwortet: «Was des Kaisers ist, gebt dem Kaiser, und was Gottes ist, Gott.»"),
 ("TU-MRK-012-018-027", "MRK.12.18-MRK.12.27", "dialogue", "Die Frage nach der Auferstehung", None,
  "Sadduzäer, die die Auferstehung bestreiten, erzählen von einer Frau, die nacheinander sieben Brüder geheiratet hat. Jesus antwortet, die Auferstandenen heirateten nicht, und begründet die Auferstehung mit dem Gott Abrahams, Isaaks und Jakobs, der ein Gott der Lebenden ist."),
 ("TU-MRK-012-028-034", "MRK.12.28-MRK.12.34", "dialogue", "Das erste Gebot", None,
  "Ein Schriftgelehrter fragt nach dem ersten Gebot. Jesus nennt das «Höre, Israel» und die Liebe zu Gott mit ganzem Herzen, dazu die Liebe zum Nächsten. Der Schriftgelehrte stimmt zu; Jesus sagt, er sei nicht fern vom Reich Gottes."),
 ("TU-MRK-012-035-037", "MRK.12.35-MRK.12.37", "discourse", "Davids Sohn und Herr", None,
  "Jesus fragt, wie der Christus Davids Sohn sein kann, wenn David ihn im Psalm «meinen Herrn» nennt. Die Menge hört ihm gern zu."),
 ("TU-MRK-012-038-040", "MRK.12.38-MRK.12.40", "discourse", "Warnung vor den Schriftgelehrten", None,
  "Jesus warnt vor Schriftgelehrten, die Ehre suchen, die Häuser der Witwen auffressen und zum Schein lange beten; sie werden ein härteres Urteil empfangen."),
 ("TU-MRK-012-041-044", "MRK.12.41-MRK.12.44", "narrative", "Die Gabe der Witwe", None,
  "Jesus sieht, wie Reiche viel in den Opferkasten werfen und eine arme Witwe zwei kleine Münzen. Er sagt den Jüngern, sie habe mehr gegeben als alle, denn sie gab ihren ganzen Lebensunterhalt."),
 ("TU-MRK-013-001-037", "MRK.13.1-MRK.13.37", "section", "Rede über die Zukunft",
  ["TU-MRK-013-001-002", "TU-MRK-013-003-013", "TU-MRK-013-014-023", "TU-MRK-013-024-027", "TU-MRK-013-028-031", "TU-MRK-013-032-037"],
  "Jesus kündigt die Zerstörung des Tempels an. Auf dem Ölberg spricht er zu vier Jüngern über Kriege, Verfolgung und Verführung, über den Gräuel der Verwüstung und die grosse Bedrängnis, über das Kommen des Menschensohns und darüber, dass niemand Tag und Stunde kennt. Die Rede endet mit dem Ruf: Wacht!"),
 ("TU-MRK-013-001-002", "MRK.13.1-MRK.13.2", "dialogue", "Kein Stein auf dem anderen", None,
  "Ein Jünger bewundert die Bauten des Tempels. Jesus sagt, kein Stein werde auf dem anderen bleiben."),
 ("TU-MRK-013-003-013", "MRK.13.3-MRK.13.13", "discourse", "Der Anfang der Wehen", None,
  "Petrus, Jakobus, Johannes und Andreas fragen nach Zeitpunkt und Zeichen. Jesus warnt vor Verführern, nennt Kriege, Erdbeben und Hungersnöte einen Anfang der Wehen und kündigt Verfolgung an; zuerst muss das Evangelium allen Völkern verkündigt werden, und wer bis zum Ende standhält, wird gerettet."),
 ("TU-MRK-013-014-023", "MRK.13.14-MRK.13.23", "discourse", "Die grosse Bedrängnis", None,
  "Wenn der Gräuel der Verwüstung steht, wo er nicht darf, sollen die in Judäa in die Berge fliehen. Eine Bedrängnis ohnegleichen kommt, doch Gott verkürzt die Tage um der Auserwählten willen. Jesus warnt vor falschen Christussen und Propheten."),
 ("TU-MRK-013-024-027", "MRK.13.24-MRK.13.27", "discourse", "Das Kommen des Menschensohns", None,
  "Nach der Bedrängnis verfinstern sich Sonne und Mond, die Sterne fallen; man wird den Menschensohn in den Wolken kommen sehen, und er wird die Auserwählten von überall sammeln."),
 ("TU-MRK-013-028-031", "MRK.13.28-MRK.13.31", "discourse", "Das Gleichnis vom Feigenbaum", None,
  "Wie die Blätter des Feigenbaums den Sommer ankündigen, so zeigt das Geschehene, dass es nahe ist. Dieses Geschlecht werde nicht vergehen, bis alles geschieht; Himmel und Erde vergehen, Jesu Worte nicht."),
 ("TU-MRK-013-032-037", "MRK.13.32-MRK.13.37", "discourse", "Wacht!", None,
  "Tag und Stunde kennt niemand, nicht einmal der Sohn, nur der Vater. Wie Knechte und Türhüter eines verreisten Herrn sollen alle wach bleiben, denn er kann zu jeder Nachtwache kommen."),
]
UNITS_GSW = {
 "TU-MRK-011-001-033": ("De Jesus chunnt uf Jerusalem", "De Jesus riitet uf eme Füli in Jerusalem ii, und d Lüüt rüefed Hosanna. Er verflueched en Fiigebaum ohni Frucht, jagt d Händler us em Tämpel und redt vom Glaube, vom Bätte und vom Vergää. D Füerende z Jerusalem stelled sini Vollmacht in Frag. De Vers [[MRK.11.26]] vo de KJV-Zellig fäält im Grundtext."),
 "TU-MRK-011-001-011": ("Iizug in Jerusalem", "Zwei Jünger holed es Füli, wie s de Jesus aagseit hät. De Jesus riitet uf Jerusalem; d Mängi breitet Mäntel und Zweig uus und rüeft: «Hosanna! Gsägnet sig dä, wo chunnt im Name vom Herr!» Am Aabig luegt er sich im Tämpel um und gaat zrugg uf Betanie."),
 "TU-MRK-011-012-014": ("De Fiigebaum ohni Frucht", "De Jesus hät Hunger, findet a me Fiigebaum nu Bletter, obwohl s nöd d Ziit für Fiige isch, und seit, niemer söll je wider Frucht vo ihm ässe."),
 "TU-MRK-011-015-019": ("De Jesus im Tämpel", "De Jesus jagt Verchäufer und Chäufer us em Tämpel, schmeisst d Tisch vo de Gältwächsler um und lehrt mit em Jesaja und em Jeremia: S Huus vo Gott söll es Huus zum Bätte für alli Völker sii, isch aber e Röiberhöli worde. D Hoheprieschter und d Schriftgleerte sueched en umzbringe, händ aber Angscht vor de Mängi."),
 "TU-MRK-011-020-025": ("De verdorret Fiigebaum: Glaube, Bätte, Vergää", "Am Morge isch de Fiigebaum verdorret. De Jesus rüeft zum Glaube a Gott uf: Wär nöd zwiiflet, cha Bärge versetze; wär bättet, söll mit de Erhörig rächne und dene vergää, won er öppis gäge si hät."),
 "TU-MRK-011-027-033": ("D Frag nach de Vollmacht", "Hoheprieschter, Schriftgleerti und Ältischti fröged de Jesus, mit was für ere Vollmacht er handlet. Er stellt d Gägefrag nach de Taufi vom Johannes. Wil si us Angscht vor de Mängi kei Antwort gänd, git au er kei Antwort."),
 "TU-MRK-012-001-044": ("Striitgspröch im Tämpel", "Im Tämpel verzellt de Jesus s Gliichnis vo de Wiibuure, wo de Sohn vom Bsitzer umbringed. Verschideni Gruppe stelled em Fangfrage: zur Stüür a de Kaiser, zur Uferstehig, zum erschte Gebot. De Jesus fröget sälber, wie de Christus de Sohn vom David sii cha, warnt vor Schriftgleerte, wo nu Ehr sueched, und lobt d Gab vo ere arme Witwe."),
 "TU-MRK-012-001-012": ("S Gliichnis vo de Wiibuure", "En Mänsch verpachtet en Wiibärg. D Wiibuure verprügled und töded d Chnächt, wo de Ertrag sölled hole, und z letscht de gliebt Sohn. De Jesus schlüüsst mit em Psalmwort vom verworfne Stei, wo zum Eckstei worde isch. D Füerende merked, dass s Gliichnis ine gilt."),
 "TU-MRK-012-013-017": ("D Frag nach de Stüür", "Pharisäer und Herodianer fröged, öb mer em Kaiser Stüür zale dörf. De Jesus laat sich en Denar zeige und seit: «Was em Kaiser ghört, gänd em Kaiser, und was Gott ghört, Gott.»"),
 "TU-MRK-012-018-027": ("D Frag nach de Uferstehig", "Sadduzäer, wo d Uferstehig bestriited, verzelled vo ere Frau, wo nachenand sibe Brüeder ghüratet hät. De Jesus seit, d Uferstandne hüratid nöd, und begründet d Uferstehig mit em Gott vom Abraham, vom Isaak und vom Jakob, wo en Gott vo de Läbige isch."),
 "TU-MRK-012-028-034": ("S erscht Gebot", "En Schriftgleerte fröget nach em erschte Gebot. De Jesus nännt s «Los, Israel» und d Liebi zu Gott vo ganzem Härze, dezue d Liebi zum Nächschte. De Schriftgleert stimmt zue; de Jesus seit, er sig nöd wiit vom Riich vo Gott."),
 "TU-MRK-012-035-037": ("Em David sin Sohn und Herr", "De Jesus fröget, wie de Christus de Sohn vom David sii cha, wänn de David en im Psalm «min Herr» nännt. D Mängi lost em gern zue."),
 "TU-MRK-012-038-040": ("Warnig vor de Schriftgleerte", "De Jesus warnt vor Schriftgleerte, wo Ehr sueched, d Hüüser vo de Witwe uffrässed und zum Schii lang bätted; si wärded es härters Urteil überchoo."),
 "TU-MRK-012-041-044": ("D Gab vo de Witwe", "De Jesus gseht, wie Riichi vil in Opferstock wärfed und e armi Witwe zwei chliini Münze. Er seit de Jünger, si heig meh gää als alli, dänn si hät ire ganz Läbesunderhalt gää."),
 "TU-MRK-013-001-037": ("Red über d Zuekunft", "De Jesus chündet aa, dass de Tämpel zerstört wird. Uf em Ölberg redt er mit vier Jünger über Chrieg, Verfolgig und Verfüerig, über de Gröiel vo de Verwüeschtig und di gross Bedrängnis, über s Cho vom Mänschesohn und devo, dass niemer Tag und Stund kännt. D Red hört mit em Ruef uf: Bliibed wach!"),
 "TU-MRK-013-001-002": ("Kei Stei uf em andere", "En Jünger bewunderet d Bauwärch vom Tämpel. De Jesus seit, kei Stei bliib uf em andere."),
 "TU-MRK-013-003-013": ("De Aafang vo de Wehe", "De Petrus, de Jakobus, de Johannes und de Andreas fröged nach Ziitpunkt und Zeiche. De Jesus warnt vor Verfüerer, nännt Chrieg, Ärdbebe und Hungersnöt en Aafang vo de Wehe und chündet Verfolgig aa; zerscht mues s Evangelium allne Völker verchündet wärde, und wär bis as Änd durehebt, wird grettet."),
 "TU-MRK-013-014-023": ("Di gross Bedrängnis", "Wänn de Gröiel vo de Verwüeschtig staat, wo er nöd darf, söled die z Judäa i d Bärge flüchte. E Bedrängnis chunnt, wie s no nie eini gää hät, aber Gott verchürzt d Täg wäge de Uuserwäälte. De Jesus warnt vor falsche Christusse und Prophete."),
 "TU-MRK-013-024-027": ("S Cho vom Mänschesohn", "Nach de Bedrängnis wärded d Sunne und de Mond dunkel, d Stärne gheied abe; mer wird de Mänschesohn i de Wolche gseh choo, und er wird d Uuserwäälte vo überall zämehole."),
 "TU-MRK-013-028-031": ("S Gliichnis vom Fiigebaum", "Wie d Bletter vom Fiigebaum de Summer aachündet, so zeigt das, wo passiert, dass es nöch isch. Die Generation vergang nöd, bis alles passiert isch; Himmel und Ärde vergönd, d Wort vo Jesus nöd."),
 "TU-MRK-013-032-037": ("Bliibed wach!", "Tag und Stund kännt niemer, au nöd de Sohn, nu de Vatter. Wie d Chnächt und de Türhüeter vo me verreiste Herr söled alli wach bliibe, dänn er cha i jeder Nachtwach choo."),
}

NOTES_DE = ["KI-Entwurf ohne fachliche Prüfung.",
            ("Die Zuordnung von Handschriften zu Lesarten in den Alternativen beruht auf maschineller Kollation "
             "(METHOD-AUTO-COLLATION-V1, WREAD-CNTR-MRK-011..013), nicht auf eigener Prüfung der Handschriften; wo die Zuordnung "
             "erkennbar unsicher ist, ist das bei der Alternative vermerkt."),
            ("[[MRK.11.26]] (KJV-Zählung) fehlt im SBLGNT wie in den Ausgaben von Westcott/Hort, Tregelles und NA28; er steht im "
             "Text von Robinson/Pierpont. Weil es dafür keine SBLGNT-Tokens gibt, enthält diese Übersetzung für [[MRK.11.26]] keinen "
             "Text; der Wortlaut ist bei den Alternativen zu [[MRK.11.25]] wiedergegeben."),
            "Markus erzählt oft im Präsens; die Übersetzung behält dieses historische Präsens bei.",
            "Die grosse Rede Jesu reicht von [[MRK.13.5]] bis [[MRK.13.37]]; die Anführungszeichen markieren das.",
            "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."]
NOTES_GSW = ["KI-Entwurf ohni fachlichi Prüefig.", "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
             ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1, "
              "WREAD-CNTR-MRK-011..013), nöd uf eigeter Prüefig vo de Handschrifte."),
             ("[[MRK.11.26]] (KJV-Zellig) fäält im SBLGNT wie i de Usgabe vo Westcott/Hort, Tregelles und NA28; er staat im Text "
              "vo Robinson/Pierpont. Wil s defür kei SBLGNT-Tokens git, hät die Übersetzig für [[MRK.11.26]] kein Text; de Wortlut "
              "staat bi de Alternative zu [[MRK.11.25]]."),
             "Di gross Red vo Jesus gaat vo [[MRK.13.5]] bis [[MRK.13.37]]; d Aafüerigszeiche zeiged das."]


def run():
    import json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _lib import localize  # noqa: E402
    n = 0
    if not (D / "works" / "WORK-MRK.json").exists():
        raise SystemExit("WORK-MRK fehlt")
    for uid, rng, kind, title, parts, summary in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-MRK", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}),
               "segmentation_note_de": SEG if parts else None,
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        rec = {k: v for k, v in rec.items() if v is not None}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-14; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-mrk").glob("VAR-SBLGNTAPP-MRK-01[123]-*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-MRK-{c:03d}.json")
        # Verse ohne SBLGNT-Tokens (MRK.11.26) erhalten keinen Text
        refs_c = [f"MRK.{c}.{v}" for v in range(1, last + 1) if f"MRK.{c}.{v}" in toks]
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-MRK-{c:03d}-001-{last:03d}-{code}-WORKING"
            dec = [{"reference": r, "target": tg, "kind": kd, "grc": grc, **({"more_literal": ml} if ml else {}),
                    **({"other_options": oo} if oo else {}), "note": nt}
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
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"MRK.{c}.1-MRK.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MRK-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch. Schweizer Rechtschreibung. Begriffe abgestimmt auf die Arbeitsübersetzung von [[MRK.3.20-MRK.3.35]]. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
                                       if lang == "de" else "Direkt aus dem SBLGNT übersetzt, mit Wortzuordnung zu den Token; die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle. Begriffe abgestimmt auf die Mundartfassung von [[MRK.3.20-MRK.3.35]]. Nicht aus einer veröffentlichten Mundart-Bibel übernommen."),
                        "based_on_edition": "ED-SBLGNT", "based_on_tokens": ts_id, "follows_readings": follows,
                        "text_by_reference": texts, "authorship_de": AUTH if lang == "de" else AUTH_GSW,
                        "translation_notes": NOTES_DE if lang == "de" else NOTES_GSW,
                        "knowledge": {"asserted_at": DATE, "supersedes": None}, "decisions": dec,
                        "decisions_note_de": "Übersetzungsentscheidungen: wörtlich (literal), sprachlich angepasst (adapted), Deutungsentscheidung (interpretive) oder der vertrauten Wiedergabe folgend (traditional). " + (AUTH if lang == "de" else AUTH_GSW)})
            if c != 11:
                rec["translation_notes"] = [x for x in rec["translation_notes"] if "MRK.11.26" not in x]
            if c != 13:
                rec["translation_notes"] = [x for x in rec["translation_notes"] if "MRK.13.5" not in x]
            if alts:
                rec["alternatives"] = alts
                rec["alternatives_note_de"] = "Wiedergabe abweichender Lesarten, soweit sie die Übersetzung verändern. " + (AUTH if lang == "de" else AUTH_GSW)
                rec["alternatives_origin_note"] = ("Mögliche Erklärungen, wie die Unterschiede entstanden sein könnten. Sie stehen nebeneinander; keine ist als richtig entschieden."
                                                   if lang == "de" else "Möglichi Erkläärige, wie d Underschid entstande sii chönnted. Si stönd näbenand; keini isch als richtig entschide.")
            n += write(D / "translations" / f"{tid}.json", rec)
            aid = f"ALIGN-MRK-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"MRK.{c}.1-MRK.{c}.{last}",
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/markus_text_11_13.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Markus 11–13 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
