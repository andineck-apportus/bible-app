#!/usr/bin/env python3
"""Autorenwerkzeug: Markus 14–16 (Passion, Grab, Markusschlüsse) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch,
Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/markus_text_14_16.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MRK besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- [[MRK.15.28]] fehlt im SBLGNT (keine Tokens); der Vers erhält keinen Text. Der Zusatz steht als Alternative bei
  [[MRK.15.27]].
- Der SBLGNT druckt beide späteren Markusschlüsse in Doppelklammern ⟦ ⟧: den kürzeren Schluss innerhalb der Tokens von
  [[MRK.16.8]] (Positionen 19–52) und den längeren Schluss [[MRK.16.9]]–[[MRK.16.20]]. Beide werden übersetzt, weil die
  Tokens sie enthalten, die Klammern bleiben im Übersetzungstext stehen, und Hinweise (decisions, translation_notes,
  Texteinheit TU-MRK-016-009-020) weisen sie als spätere Schlüsse aus.

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
TAGS = ["TAG-MARK"]
CHAPTERS = ((14, 72), (15, 47), (16, 20))

DE = {
 # ------------------------------------------------------------ Kapitel 14
 "MRK.14.1": "[Nach]{8} [zwei]{9} [Tagen]{10} [aber]{2} [war]{1} [das Passa]{3,4} und{5} [das Fest der Ungesäuerten Brote]{6,7}. Und{11} [die Hohepriester]{13,14} und{15} [die Schriftgelehrten]{16,17} [suchten]{12}, [wie]{18} [sie]{22} [ihn]{19} [mit]{20} [List]{21} [ergreifen]{22} und [töten könnten]{23}.",
 "MRK.14.2": "[Sie sagten]{1} [nämlich]{2}: «[Nicht]{3} [am]{4,5} [Fest]{6}, [damit nicht]{7} [ein Aufruhr]{9} [des Volkes]{10,11} [entsteht]{8}.»",
 "MRK.14.3": "Und{1} [als er]{3} [in]{4} [Betanien]{5} [im]{6,7} [Haus]{8} [Simons]{9} [des Aussätzigen]{10,11} [war]{2} und [zu Tisch lag]{12,13}, [kam]{14} [eine Frau]{15} [mit]{16} [einem Alabastergefäss]{17} voll [kostbarem]{21} [Salböl]{18} [aus reiner]{20} [Narde]{19}; [sie zerbrach]{22} [das]{23} [Gefäss]{24} [und goss es]{25} [ihm]{26} [über]{25} [den]{27} [Kopf]{28}.",
 "MRK.14.4": "[Einige]{3} [aber]{2} [waren]{1} [empört]{4} [und sagten zueinander]{5,6}: «[Wozu]{7,8} [ist]{14} [diese]{11} [Verschwendung]{9,10} [des Salböls]{12,13} [geschehen]{14}?",
 "MRK.14.5": "[Dieses]{3} [Salböl]{4,5} [hätte]{1} [nämlich]{2} [für mehr als]{7} [dreihundert]{9} [Denare]{8} [verkauft]{6} und{10} [den Armen]{12,13} [gegeben werden]{11} [können]{1}.» Und{14} [sie fuhren]{15} [sie]{16} [an]{15}.",
 "MRK.14.6": "[Jesus]{1,3} [aber]{2} [sagte]{4}: «[Lasst]{5} [sie]{6}! [Warum]{7} [bereitet ihr]{10} [ihr]{8} [Verdruss]{9}? [Ein gutes]{11} [Werk]{12} [hat sie]{13} [an]{14} [mir]{15} [getan]{13}.",
 "MRK.14.7": "Denn{2} [die Armen]{3,4} [habt ihr]{5} [allezeit]{1} [bei]{6} [euch]{7}, und{8} [wann]{9} [immer ihr wollt]{10}, [könnt ihr]{11} [ihnen]{12} [Gutes]{13} [tun]{14}; [mich]{15} [aber]{16} [habt ihr]{19} [nicht]{17} [allezeit]{18}.",
 "MRK.14.8": "[Was]{1} [sie konnte]{2}, [hat sie getan]{3}: [Sie hat]{4} [meinen]{8} [Leib]{6,7} [im Voraus]{4} [gesalbt]{5} [für]{9} [das]{10} [Begräbnis]{11}.",
 "MRK.14.9": "[Amen]{1}, [ich sage]{3} [euch]{4}: [Wo]{5} [immer]{6} [das]{8} [Evangelium]{9} [verkündigt wird]{7} [in]{10} [der ganzen]{11,12} [Welt]{13}, [wird]{18} [auch]{14} [erzählt werden]{18}, [was]{15} [diese]{17} [getan hat]{16}, [zu]{19} [ihrem]{21} [Gedächtnis]{20}.» ~2(δέ «aber» nach ἀμήν; nicht eigens wiedergegeben)",
 "MRK.14.10": "Und{1} [Judas]{2} [Iskariot]{3}, [der]{4} [eine]{5} [der Zwölf]{6,7}, [ging]{8} [zu]{9} [den Hohepriestern]{10,11}, [um]{12} [ihn]{13} [ihnen]{15} [auszuliefern]{14}.",
 "MRK.14.11": "[Sie]{1} [aber]{2} [freuten sich]{4}, [als sie es hörten]{3}, und{5} [versprachen]{6} [ihm]{7} [Geld]{8} [zu geben]{9}. Und{10} [er suchte]{11}, [wie]{12} [er]{15} [ihn]{13} [bei guter Gelegenheit]{14} [ausliefern könnte]{15}.",
 "MRK.14.12": "Und{1} [am]{2} [ersten]{3} [Tag]{4} [der Ungesäuerten Brote]{5,6}, [als]{7} [man]{10} [das Passalamm]{8,9} [schlachtete]{10}, [sagen]{11} [seine]{15} [Jünger]{13,14} [zu ihm]{12}: «[Wo]{16} [willst du]{17}, [dass wir]{19} [hingehen]{18} und [es vorbereiten]{19}, [damit]{20} [du]{21} [das Passa]{22,23} [essen kannst]{21}?»",
 "MRK.14.13": "Und{1} [er sendet]{2} [zwei]{3} [seiner]{4,6} [Jünger]{5} und{7} [sagt]{8} [zu ihnen]{9}: «[Geht]{10} [in]{11} [die]{12} [Stadt]{13}, und{14} [es wird]{15} [euch]{16} [ein Mensch]{17} [begegnen]{15}, [der]{20} [einen Wasserkrug]{18,19} [trägt]{20}; [folgt]{21} [ihm]{22},",
 "MRK.14.14": "und{1} [wo]{2} [immer]{3} [er hineingeht]{4}, [sagt]{5} [dem Hausherrn]{6,7}: ‹[Der Lehrer]{9,10} [sagt]{11}: Wo{12} [ist]{13} [mein]{16} [Gastraum]{14,15}, [wo]{17} [ich]{24} [mit]{20} [meinen]{21,23} [Jüngern]{22} [das Passa]{18,19} [essen kann]{24}?›  ~8(ὅτι leitet die direkte Rede ein)",
 "MRK.14.15": "Und{1} [er]{2} [wird]{4} [euch]{3} [einen grossen]{6} [Obersaal]{5} [zeigen]{4}, [mit Polstern ausgelegt]{7} [und bereit]{8}; und{9} [dort]{10} [bereitet]{11} [für uns]{12} [vor]{11}.»",
 "MRK.14.16": "Und{1} [die Jünger]{3,4} [gingen hinaus]{2} und{5} [kamen]{6} [in]{7} [die Stadt]{8,9} und{10} [fanden es]{11}, [wie]{12} [er]{13} [ihnen]{14} [gesagt hatte]{13}, und{15} [bereiteten]{16} [das Passa]{17,18} [vor]{16}.",
 "MRK.14.17": "Und{1} [als es Abend geworden war]{2,3}, [kommt er]{4} [mit]{5} [den Zwölf]{6,7}.",
 "MRK.14.18": "Und{1} [als sie]{3} [zu Tisch lagen]{2} und{4} [assen]{5}, [sagte]{8} [Jesus]{6,7}: «[Amen]{9}, [ich sage]{10} [euch]{11}: [Einer]{13} [von]{14} [euch]{15} [wird]{16} [mich]{17} [ausliefern]{16}, [der]{18} [mit]{20} [mir]{21} [isst]{19}.» ~12(ὅτι leitet die direkte Rede ein)",
 "MRK.14.19": "[Sie fingen an]{1}, [traurig zu werden]{2} und{3} [zu ihm]{5} [zu sagen]{4}, [einer]{6} [nach]{7} [dem anderen]{8}: «[Doch nicht]{9} [ich]{10}?»",
 "MRK.14.20": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: «[Einer]{5} [der Zwölf]{6,7}, [der]{8} [mit]{10} [mir]{11} [in]{12} [die]{13} [Schüssel]{14} [eintaucht]{9}.",
 "MRK.14.21": "Denn{1} [der Menschensohn]{2,4-6} [geht]{7} [zwar]{3} [dahin]{7}, [wie]{8} [über]{10} [ihn]{11} [geschrieben steht]{9}; [weh]{12} [aber]{13} [jenem]{16} [Menschen]{14,15}, [durch]{17} [den]{18} [der Menschensohn]{19-22} [ausgeliefert wird]{23}! Es wäre [gut]{24} [für ihn]{25}, [wenn]{26} [jener]{31} [Mensch]{29,30} [nicht]{27} [geboren wäre]{28}.»",
 "MRK.14.22": "Und{1} [während sie]{3} [assen]{2}, [nahm er]{4} [Brot]{5}, [sprach den Lobpreis]{6}, [brach es]{7} und{8} [gab es]{9} [ihnen]{10} und{11} [sagte]{12}: «[Nehmt]{13}! [Das]{14} [ist]{15} [mein]{18} [Leib]{16,17}.»",
 "MRK.14.23": "Und{1} [er nahm]{2} [einen Becher]{3}, [sprach das Dankgebet]{4} und [gab ihn]{5} [ihnen]{6}, und{7} [sie tranken]{8} [alle]{11} [daraus]{9,10}.",
 "MRK.14.24": "Und{1} [er sagte]{2} [zu ihnen]{3}: «[Das]{4} [ist]{5} [mein]{8} [Blut]{6,7} [des Bundes]{9,10}, [das]{11} [für]{13} [viele]{14} [vergossen wird]{12}.",
 "MRK.14.25": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Ich werde]{8} [nie mehr]{5-7} [vom]{9,10} [Gewächs]{11} [des Weinstocks]{12,13} [trinken]{8} [bis]{14} [zu jenem]{15,17} [Tag]{16}, [an dem]{18} [ich]{20} [es]{19} [neu]{21} [trinke]{20} [im]{22,23} [Reich]{24} [Gottes]{25,26}.» ~4(ὅτι leitet die direkte Rede ein)",
 "MRK.14.26": "Und{1} [nachdem sie den Lobgesang gesungen hatten]{2}, [gingen sie hinaus]{3} [zum]{4,5} [Ölberg]{6-8}.",
 "MRK.14.27": "Und{1} [Jesus]{4,5} [sagt]{2} [zu ihnen]{3}: «[Ihr werdet]{8} [alle]{7} [zu Fall kommen]{8}, denn{9} [es steht geschrieben]{10}: ‹[Ich werde]{11} [den Hirten]{12,13} [schlagen]{11}, und{14} [die Schafe]{15,16} [werden zerstreut werden]{17}.› ~6(ὅτι leitet die direkte Rede ein)",
 "MRK.14.28": "[Aber]{1} [nachdem]{2,3} [ich]{5} [auferweckt worden bin]{4}, [werde ich]{6} [euch]{7} [nach]{8} [Galiläa]{9,10} [vorausgehen]{6}.»",
 "MRK.14.29": "[Petrus]{1,3} [aber]{2} [sagte]{4} [zu ihm]{5}: «[Auch wenn]{6,7} [alle]{8} [zu Fall kommen]{9}, [so doch]{10} [nicht]{11} [ich]{12}!»",
 "MRK.14.30": "Und{1} [Jesus]{4,5} [sagt]{2} [zu ihm]{3}: «[Amen]{6}, [ich sage]{7} [dir]{8}: [Du]{10} [wirst]{22} [heute]{11}, [in dieser]{12,13} [Nacht]{14}, [bevor]{15,16} [ein Hahn]{18} [zweimal]{17} [kräht]{19}, [mich]{21} [dreimal]{20} [verleugnen]{22}.» ~9(ὅτι leitet die direkte Rede ein)",
 "MRK.14.31": "[Er]{1} [aber]{2} [beteuerte]{4} [umso heftiger]{3}: «[Wenn]{5} [ich]{7} [mit dir]{9} [sterben]{8} [müsste]{6}, [ich werde]{13} [dich]{12} [gewiss nicht]{10,11} [verleugnen]{13}!» [Ebenso]{14} [aber]{15} [redeten]{18} [auch]{16} [alle]{17}.",
 "MRK.14.32": "Und{1} [sie kommen]{2} [zu]{3} [einem Grundstück]{4}, [dessen]{5} [Name]{6,7} [Getsemani]{8} ist, und{9} [er sagt]{10} [zu seinen]{11,13} [Jüngern]{12}: «[Setzt euch]{14} [hier hin]{15}, [während]{16} [ich bete]{17}.»",
 "MRK.14.33": "Und{1} [er nimmt]{2} [Petrus]{3,4} und{5} [Jakobus]{6} und{7} [Johannes]{8} [mit sich]{9,10}, und{11} [er fing an]{12}, [sich zu entsetzen]{13} und{14} [sich zu ängstigen]{15},",
 "MRK.14.34": "und{1} [sagt]{2} [zu ihnen]{3}: «[Tief betrübt]{4} [ist]{5} [meine]{8} [Seele]{6,7} [bis]{9} [zum Tod]{10}. [Bleibt]{11} [hier]{12} und{13} [wacht]{14}!»",
 "MRK.14.35": "Und{1} [er ging]{2} [ein wenig]{3} [weiter]{2}, [fiel]{4} [auf]{5} [die Erde]{6,7} und{8} [betete]{9}, [dass]{10}, [wenn]{11} es [möglich]{12} [ist]{13}, [die Stunde]{17,18} [an]{15} [ihm]{16} [vorübergehe]{14};",
 "MRK.14.36": "und{1} [er sagte]{2}: «[Abba]{3}, [Vater]{4,5}, [alles]{6} ist [dir]{8} [möglich]{7}. [Nimm]{9} [diesen]{12} [Becher]{10,11} [von]{13} [mir]{14} [weg]{9}! [Doch]{15} [nicht]{16}, [was]{17} [ich]{18} [will]{19}, [sondern]{20} [was]{21} [du]{22} willst.»",
 "MRK.14.37": "Und{1} [er kommt]{2} und{3} [findet]{4} [sie]{5} [schlafend]{6}, und{7} [sagt]{8} [zu Petrus]{9,10}: «[Simon]{11}, [schläfst du]{12}? [Vermochtest du]{14} [nicht]{13}, [eine]{15} [Stunde]{16} [zu wachen]{17}?",
 "MRK.14.38": "[Wacht]{1} und{2} [betet]{3}, [damit]{4} [ihr]{6} [nicht]{5} [in]{7} [Versuchung]{8} [kommt]{6}! [Der]{9} [Geist]{11} ist [zwar]{10} [willig]{12}, [das]{13} [Fleisch]{15} [aber]{14} [schwach]{16}.»",
 "MRK.14.39": "Und{1} [er ging]{3} [wieder]{2} [weg]{3}, [betete]{4} und [sprach]{8} [dieselben]{5,6} [Worte]{7}.",
 "MRK.14.40": "Und{1} [als er]{3} [wieder]{2} [kam]{3}, [fand er]{4} [sie]{5} [schlafend]{6}; [ihre]{9} [Augen]{10,11} [waren]{7} [nämlich]{8} [ganz schwer]{12}, und{13} [sie wussten]{15} [nicht]{14}, [was]{16} [sie]{17} [ihm]{18} [antworten sollten]{17}.",
 "MRK.14.41": "Und{1} [er kommt]{2} [zum dritten Mal]{3,4} und{5} [sagt]{6} [zu ihnen]{7}: «[Schlaft ihr]{8} [noch]{9,10} und{11} [ruht euch aus]{12}? [Es ist genug]{13}. [Gekommen ist]{14} [die Stunde]{15,16}; [siehe]{17}, [der Menschensohn]{19-22} [wird]{18} [in]{23} [die Hände]{24,25} [der Sünder]{26,27} [ausgeliefert]{18}.",
 "MRK.14.42": "[Steht auf]{1}, [lasst uns gehen]{2}! [Siehe]{3}, [der]{4} [mich]{6} [ausliefert]{5}, [ist nahe gekommen]{7}.»",
 "MRK.14.43": "Und{1} [sogleich]{2}, [noch]{3} [während er]{4} [redete]{5}, [kommt]{6} [Judas]{7} [herbei]{6}, [einer]{8} [der Zwölf]{9,10}, und{11} [mit]{12} [ihm]{13} [eine Menge]{14} [mit]{15} [Schwertern]{16} und{17} [Knüppeln]{18}, [von]{19} [den Hohepriestern]{20,21} und{22} [den Schriftgelehrten]{23,24} und{25} [den Ältesten]{26,27}.",
 "MRK.14.44": "[Der]{3} [ihn]{5} [auslieferte]{4}, [hatte]{1} [ihnen]{7} [aber]{2} [ein Zeichen]{6} [gegeben]{1} [und gesagt]{8}: «[Wen]{9} [immer]{10} [ich küssen werde]{11}, [der]{12} [ist es]{13}. [Ergreift]{14} [ihn]{15} und{16} [führt ihn]{17} [sicher]{18} [ab]{17}!»",
 "MRK.14.45": "Und{1} [als er kam]{2}, [trat er]{4} [sogleich]{3} [zu ihm]{5} [heran]{4} und [sagt]{6}: «[Rabbi]{7}!», und{8} [küsste]{9} [ihn]{10}.",
 "MRK.14.46": "[Sie]{1} [aber]{2} [legten]{3} [die Hände]{4,5} [an ihn]{6} und{7} [ergriffen]{8} [ihn]{9}.",
 "MRK.14.47": "[Einer]{1,3} [der Umstehenden]{4,5} [aber]{2} [zog]{6} [das]{7} [Schwert]{8}, [schlug]{9} [den]{10} [Knecht]{11} [des Hohepriesters]{12,13} und{14} [hieb]{15} [ihm]{16} [das]{17} [Ohr]{18} [ab]{15}.",
 "MRK.14.48": "Und{1} [Jesus]{3,4} [ergriff das Wort]{2} und [sagte]{5} [zu ihnen]{6}: «[Wie]{7} [gegen]{8} [einen Räuber]{9} [seid ihr ausgezogen]{10} [mit]{11} [Schwertern]{12} und{13} [Knüppeln]{14}, um [mich]{16} [festzunehmen]{15}?",
 "MRK.14.49": "[Täglich]{1,2} [war ich]{3} [bei]{4} [euch]{5} [im]{6,7} [Tempel]{8} [und lehrte]{9}, und{10} [ihr habt]{12} [mich]{13} [nicht]{11} [ergriffen]{12}. [Aber]{14} es geschieht, [damit]{15} [die Schriften]{17,18} [erfüllt werden]{16}.»",
 "MRK.14.50": "Und{1} [sie verliessen]{2} [ihn]{3} und [flohen]{4} [alle]{5}.",
 "MRK.14.51": "Und{1} [ein junger Mann]{2,3} [folgte]{4} [ihm]{5} [nach]{4}, [bekleidet]{6} [mit einem Leinentuch]{7} [auf]{8} [dem nackten Leib]{9}; und{10} [sie packen]{11} [ihn]{12},",
 "MRK.14.52": "[er]{1} [aber]{2} [liess]{3} [das]{4} [Leinentuch]{5} [zurück]{3} und [floh]{7} [nackt]{6}.",
 "MRK.14.53": "Und{1} [sie führten]{2} [Jesus]{3,4} [ab]{2} [zum]{5,6} [Hohepriester]{7}, und{8} [es kommen]{9} [alle]{10} [Hohepriester]{11,12} und{13} [die Ältesten]{14,15} und{16} [die Schriftgelehrten]{17,18} [zusammen]{9}.",
 "MRK.14.54": "Und{1} [Petrus]{2,3} [folgte]{6} [ihm]{7} [von]{4} [ferne]{5} [bis]{8} [hinein]{9} [in]{10} [den]{11} [Hof]{12} [des Hohepriesters]{13,14}, und{15} [er sass]{16,17} [bei]{18} [den]{19} [Dienern]{20} und{21} [wärmte sich]{22} [am]{23,24} [Feuer]{25}.",
 "MRK.14.55": "[Die Hohepriester]{1,3} [aber]{2} und{4} [der ganze]{5,6} [Hohe Rat]{7} [suchten]{8} [ein Zeugnis]{12} [gegen]{9} [Jesus]{10,11}, [um]{13,14} [ihn]{16} [zu töten]{15}, und{17} [fanden]{19} [keines]{18}.",
 "MRK.14.56": "[Viele]{1} [legten]{3} [nämlich]{2} [falsches Zeugnis]{3} [gegen]{4} [ihn]{5} [ab]{3}, und{6} [die]{8} [Aussagen]{9} [stimmten]{11} [nicht]{10} [überein]{7}.",
 "MRK.14.57": "Und{1} [einige]{2} [standen auf]{3}, [legten]{4} [falsches Zeugnis]{4} [gegen]{5} [ihn]{6} [ab]{4} und [sagten]{7}:",
 "MRK.14.58": "«[Wir]{2} [haben]{3} [ihn]{4} [sagen]{5} [hören]{3}: ‹[Ich]{7} [werde]{8} [diesen]{11} [Tempel]{9,10}, [der]{12} [mit Händen gemacht ist]{13}, [niederreissen]{8} und{14} [in]{15} [drei]{16} [Tagen]{17} [einen anderen]{18} [bauen]{20}, [der nicht mit Händen gemacht ist]{19}.›» ~1(ὅτι leitet die direkte Rede ein) ~6(ὅτι leitet die direkte Rede ein)",
 "MRK.14.59": "Und{1} [auch]{2} [so]{3} [stimmte]{5} [ihre]{8} [Aussage]{6,7} [nicht]{2} [überein]{4}.",
 "MRK.14.60": "Und{1} [der Hohepriester]{3,4} [trat]{2} [in]{5} [die Mitte]{6}, [fragte]{7} [Jesus]{8,9} [und sagte]{10}: «[Antwortest du]{12} [nichts]{11,13}? [Was]{14} [bezeugen]{17} [diese]{15} [gegen dich]{16}?»",
 "MRK.14.61": "[Er]{1} [aber]{2} [schwieg]{3} und{4} [antwortete]{6} [nichts]{5,7}. [Wieder]{8} [fragte]{11} [ihn]{12} [der Hohepriester]{9,10} und{13} [sagt]{14} [zu ihm]{15}: «[Bist]{17} [du]{16} [der Christus]{18,19}, [der Sohn]{20,21} [des Hochgelobten]{22,23}?»",
 "MRK.14.62": "[Jesus]{1,3} [aber]{2} [sagte]{4}: «[Ich]{5} [bin es]{6}, und{7} [ihr werdet]{8} [den Menschensohn]{9-12} [zur]{13} [Rechten]{14} [der Macht]{16,17} [sitzen]{15} und{18} [mit]{20} [den Wolken]{21,22} [des Himmels]{23,24} [kommen]{19} [sehen]{8}.»",
 "MRK.14.63": "[Der Hohepriester]{1,3} [aber]{2} [zerriss]{4} [seine]{7} [Gewänder]{5,6} und [sagt]{8}: «[Wozu]{9} [brauchen wir]{11,12} [noch]{10} [Zeugen]{13}?",
 "MRK.14.64": "[Ihr habt]{1} [die]{2} [Lästerung]{3} [gehört]{1}. [Was]{4} [meint]{6} [ihr]{5}?» [Sie]{7} [aber]{8} [verurteilten]{10} [ihn]{11} [alle]{9} [als]{13} [des Todes]{14} [schuldig]{12}.",
 "MRK.14.65": "Und{1} [einige]{3} [fingen an]{2}, [ihn]{5} [anzuspucken]{4}, und{6} [sein]{8} [Gesicht]{9,10} [zu verhüllen]{7} und{11} [ihn]{13} [mit Fäusten zu schlagen]{12} und{14} [zu ihm]{16} [zu sagen]{15}: «[Weissage]{17}!» Und{18} [die Diener]{19,20} [nahmen]{23} [ihn]{22} [mit Schlägen]{21} [in Empfang]{23}.",
 "MRK.14.66": "Und{1} [als]{2} [Petrus]{3,4} [unten]{5} [im]{6,7} [Hof]{8} [war]{2}, [kommt]{9} [eine]{10} [der Mägde]{11,12} [des Hohepriesters]{13,14},",
 "MRK.14.67": "und{1} [als sie]{2} [Petrus]{3,4} [sah]{2}, [wie er sich wärmte]{5}, [blickte sie]{6} [ihn]{7} [an]{6} und [sagt]{8}: «[Auch]{9} [du]{10} [warst]{14} [mit]{11} [dem Nazarener]{12,13}, [Jesus]{15,16}!»",
 "MRK.14.68": "[Er]{1} [aber]{2} [leugnete]{3} und [sagte]{4}: «[Ich weiss]{6} [nicht]{5} [und verstehe]{8} [nicht]{7}, [was]{10} [du]{9} [sagst]{11}.» Und{12} [er ging]{13} [hinaus]{14} [in]{15} [den]{16} [Vorhof]{17}; und{18} [ein Hahn]{19} [krähte]{20}.",
 "MRK.14.69": "Und{1} [die Magd]{2,3} [sah]{4} [ihn]{5} und [fing]{6} [wieder]{7} [an]{6}, [zu den Umstehenden]{9,10} [zu sagen]{8}: «[Der]{12} [ist]{15} [einer von]{13} [ihnen]{14}!» ~11(ὅτι leitet die direkte Rede ein)",
 "MRK.14.70": "[Er]{1} [aber]{2} [leugnete]{4} [wieder]{3}. Und{5} [nach]{6} [kurzer Zeit]{7} [sagten]{11} [die Umstehenden]{9,10} [wieder]{8} [zu Petrus]{12,13}: «[Wirklich]{14}, [du bist]{17} [einer von]{15} [ihnen]{16}; [denn]{19} [du bist]{21} [auch]{18} [ein Galiläer]{20}, und{22} [deine]{25} [Sprechweise]{23,24} [passt dazu]{26}!»",
 "MRK.14.71": "[Er]{1} [aber]{2} [fing an]{3}, [sich zu verfluchen]{4} und{5} [zu schwören]{6}: «[Ich kenne]{9} [diesen]{12} [Menschen]{10,11} [nicht]{8}, [von dem]{13} [ihr redet]{14}!» ~7(ὅτι leitet die direkte Rede ein)",
 "MRK.14.72": "Und{1} [sogleich]{2} [krähte]{6} [ein Hahn]{5} [zum zweiten Mal]{3,4}. Und{7} [Petrus]{9,10} [erinnerte sich]{8} [an das]{11} [Wort]{12}, [wie]{13} [Jesus]{16,17} [zu ihm]{15} [gesagt hatte]{14}: «[Bevor]{19} [ein Hahn]{20} [zweimal]{22} [kräht]{21}, [wirst du]{25} [mich]{24} [dreimal]{23} [verleugnen]{25}.» Und{26} [er dachte daran]{27} und [weinte]{28}. ~18(ὅτι leitet die direkte Rede ein)",
 # ------------------------------------------------------------ Kapitel 15 (15,28 fehlt im SBLGNT)
 "MRK.15.1": "Und{1} [gleich]{2} [am frühen Morgen]{3} [fassten]{5} [die Hohepriester]{6,7} [mit]{8} [den Ältesten]{9,10} und{11} [Schriftgelehrten]{12} und{13} [der ganze]{14,15} [Hohe Rat]{16} [einen Beschluss]{4}; [sie fesselten]{17} [Jesus]{18,19}, [führten ihn ab]{20} und{21} [lieferten ihn]{22} [Pilatus]{23} [aus]{22}.",
 "MRK.15.2": "Und{1} [Pilatus]{4,5} [fragte]{2} [ihn]{3}: «[Bist]{7} [du]{6} [der König]{8,9} [der Juden]{10,11}?» [Er]{12} [aber]{13} [antwortet]{14} [ihm]{15} [und sagt]{16}: «[Du]{17} [sagst es]{18}.»",
 "MRK.15.3": "Und{1} [die Hohepriester]{4,5} [klagten]{2} [ihn]{3} [vieler Dinge]{6} [an]{2}.",
 "MRK.15.4": "[Pilatus]{1,3} [aber]{2} [fragte]{5} [ihn]{6} [wieder]{4} [und sagte]{7}: «[Antwortest du]{9} [nichts]{8,10}? [Sieh]{11}, [wie viel]{12} [sie]{14} [dir]{13} [vorwerfen]{14}!»",
 "MRK.15.5": "[Jesus]{1,3} [aber]{2} [antwortete]{6} [nichts mehr]{4,5}, [sodass]{7} [Pilatus]{9,10} [sich wunderte]{8}.",
 "MRK.15.6": "[Zum]{1} [Fest]{3} [aber]{2} [liess er]{4} [ihnen]{5} [jeweils einen]{6} [Gefangenen]{7} [frei]{4}, [den]{8} [sie sich erbaten]{9}.",
 "MRK.15.7": "[Es war]{1} [aber]{2} [der sogenannte]{3,4} [Barabbas]{5} [mit]{6} [den Aufständischen]{7,8} [gefangen]{9}, [die]{10} [beim]{11,12} [Aufstand]{13} [einen Mord]{14} [begangen hatten]{15}.",
 "MRK.15.8": "Und{1} [die Menge]{3,4} [zog hinauf]{2} und [fing an]{5} [zu bitten]{6}, [wie]{7} [er es]{8} [für sie]{9} [zu tun pflegte]{8}.",
 "MRK.15.9": "[Pilatus]{1,3} [aber]{2} [antwortete]{4} [ihnen]{5} [und sagte]{6}: «[Wollt ihr]{7}, [dass ich]{8} [euch]{9} [den König]{10,11} [der Juden]{12,13} [freilasse]{8}?»",
 "MRK.15.10": "[Er erkannte]{1} [nämlich]{2}, [dass]{3} [die Hohepriester]{8,9} [ihn]{7} [aus]{4} [Neid]{5} [ausgeliefert hatten]{6}.",
 "MRK.15.11": "[Die Hohepriester]{1,3} [aber]{2} [wiegelten]{4} [die Menge]{5,6} [auf]{4}, [dass er]{7} [ihnen]{12} [lieber]{8} [Barabbas]{9,10} [freilasse]{11}.",
 "MRK.15.12": "[Pilatus]{1,3} [aber]{2} [antwortete]{5} [wieder]{4} und [sagte]{6} [zu ihnen]{7}: «[Was]{8} [wollt ihr]{10} [nun]{9}, [dass ich]{11} [mit dem tue]{11}, [den]{12} [ihr]{13} [den König]{14,15} [der Juden]{16,17} [nennt]{13}?»",
 "MRK.15.13": "[Sie]{1} [aber]{2} [schrien]{4} [wieder]{3}: «[Kreuzige]{5} [ihn]{6}!»",
 "MRK.15.14": "[Pilatus]{1,3} [aber]{2} [sagte]{4} [zu ihnen]{5}: «[Was]{6} [hat er]{8} [denn]{7} [Böses]{9} [getan]{8}?» [Sie]{10} [aber]{11} [schrien]{13} [umso lauter]{12}: «[Kreuzige]{14} [ihn]{15}!»",
 "MRK.15.15": "[Pilatus]{1,3} [aber]{2} [wollte]{4} [die Menge]{5,6} [zufriedenstellen]{7-9} und [liess]{10} [ihnen]{11} [Barabbas]{12,13} [frei]{10}; und{14} [Jesus]{16,17} [liess er geisseln]{18} und [lieferte ihn aus]{15}, [damit er gekreuzigt würde]{19,20}.",
 "MRK.15.16": "[Die Soldaten]{1,3} [aber]{2} [führten]{4} [ihn]{5} [ab]{4}, [hinein]{6} [in den Palast]{7,8}, [das ist]{9,10} [das Prätorium]{11}, und{12} [rufen]{13} [die ganze]{14,15} [Kohorte]{16} [zusammen]{13}.",
 "MRK.15.17": "Und{1} [sie ziehen]{2} [ihm]{3} [einen Purpurmantel]{4} [an]{2} und{5} [flechten]{8} [einen Dornenkranz]{9,10} und [setzen]{6} ihn [ihm]{7} [auf]{6};",
 "MRK.15.18": "und{1} [sie fingen an]{2}, [ihn]{4} [zu grüssen]{3}: «[Sei gegrüsst]{5}, [König]{6} [der Juden]{7,8}!»",
 "MRK.15.19": "Und{1} [sie schlugen]{2} [ihn]{3} [mit einem Rohr]{6} [auf den]{4} [Kopf]{5} und{7} [spuckten]{8} [ihn]{9} [an]{8}, und{10} [sie beugten]{11} [die Knie]{12,13} und [warfen sich vor]{14} [ihm]{15} [nieder]{14}.",
 "MRK.15.20": "Und{1} [als]{2} [sie]{3} [ihn]{4} [verspottet hatten]{3}, [zogen sie]{5} [ihm]{6} [den Purpurmantel]{7,8} [aus]{5} und{9} [zogen]{10} [ihm]{11} [seine eigenen]{14,15} [Kleider]{12,13} [an]{10}. Und{16} [sie führen]{17} [ihn]{18} [hinaus]{17}, [um]{19} [ihn]{21} [zu kreuzigen]{20}.",
 "MRK.15.21": "Und{1} [sie zwingen]{2} [einen]{4} [Vorübergehenden]{3}, [Simon]{5} [von Kyrene]{6}, der [vom]{8} [Feld]{9} [kam]{7}, [den Vater]{10,11} [von Alexander]{12} und{13} [Rufus]{14}, [sein]{19} [Kreuz]{17,18} [zu tragen]{15,16}.",
 "MRK.15.22": "Und{1} [sie bringen]{2} [ihn]{3} [an]{4} [den]{5} [Ort]{7} [Golgota]{6}, [das]{8} [heisst]{9} [übersetzt]{10} «[Schädelstätte]{11,12}».",
 "MRK.15.23": "Und{1} [sie wollten]{2} [ihm]{3} [mit Myrrhe gewürzten]{4} [Wein]{5} [geben]{2}; [er]{6} [aber]{7} [nahm]{9} ihn [nicht]{8}.",
 "MRK.15.24": "Und{1} [sie kreuzigen]{2} [ihn]{3} und{4} [verteilen]{5} [seine]{8} [Kleider]{6,7} [und werfen]{9} [das Los]{10} [darüber]{11,12}, [wer]{13} [was]{14} [bekommen sollte]{15}.",
 "MRK.15.25": "[Es war]{1} [aber]{2} [die dritte]{4} [Stunde]{3}, und{5} [sie kreuzigten]{6} [ihn]{7}.",
 "MRK.15.26": "Und{1} [die Aufschrift]{3,4} mit [der Anklage]{5,6} [gegen ihn]{7} [lautete]{2,8}: «[Der König]{9,10} [der Juden]{11,12}.»",
 "MRK.15.27": "Und{1} [mit]{2} [ihm]{3} [kreuzigen sie]{4} [zwei]{5} [Räuber]{6}, [einen]{7} [zur]{8} [Rechten]{9} und{10} [einen]{11} [zu]{12} [seiner]{14} [Linken]{13}.",
 "MRK.15.29": "Und{1} [die Vorübergehenden]{2,3} [lästerten]{4} [ihn]{5}, [schüttelten]{6} [ihre]{9} [Köpfe]{7,8} und{10} [sagten]{11}: «[Ha]{12}, [der du]{13} [den Tempel]{15,16} [niederreisst]{14} und{17} [in]{19} [drei]{20} [Tagen]{21} [aufbaust]{18},",
 "MRK.15.30": "[rette]{1} [dich selbst]{2} [und steig herab]{3} [vom]{4,5} [Kreuz]{6}!»",
 "MRK.15.31": "[Ebenso]{1} [spotteten]{5} [auch]{2} [die Hohepriester]{3,4} [untereinander]{6,7} [mit]{8} [den Schriftgelehrten]{9,10} und [sagten]{11}: «[Andere]{12} [hat er gerettet]{13}, [sich selbst]{14} [kann er]{16} [nicht]{15} [retten]{17}.",
 "MRK.15.32": "[Der Christus]{1,2}, [der König]{3,4} [Israels]{5}, [steige]{6} [jetzt]{7} [vom]{8,9} [Kreuz]{10} [herab]{6}, [damit]{11} [wir]{12} [sehen]{12} und{13} [glauben]{14}!» Und{15} [die]{16} [mit]{18} [ihm]{19} [Gekreuzigten]{17} [beschimpften]{20} [ihn]{21}.",
 "MRK.15.33": "Und{1} [als]{2} [die sechste]{4} [Stunde]{3} [gekommen war]{2}, [kam]{6} [eine Finsternis]{5} [über]{7} [das ganze]{8,9} [Land]{10} [bis]{11} [zur neunten]{13} [Stunde]{12}.",
 "MRK.15.34": "Und{1} [zur]{2} [neunten]{3} [Stunde]{4} [schrie]{5} [Jesus]{6,7} [mit lauter]{9} [Stimme]{8}: «[Eloi]{10}, [Eloi]{11}, [lema]{12} [sabachthani]{13}?», [das]{14} [heisst]{15} [übersetzt]{16}: «[Mein]{19} [Gott]{17,18}, [mein]{22} [Gott]{20,21}, [wozu]{23,24} [hast du]{25} [mich]{26} [verlassen]{25}?»",
 "MRK.15.35": "Und{1} [einige]{2} [der Umstehenden]{3,4} [hörten es]{5} und [sagten]{6}: «[Seht]{7}, [er ruft]{9} [Elija]{8}!»",
 "MRK.15.36": "[Einer]{3} [aber]{2} [lief hin]{1}, [füllte]{5} [einen Schwamm]{6} [mit Essig]{7}, [steckte ihn]{8} [auf ein Rohr]{9} und [gab]{10} [ihm]{11} [zu trinken]{10} [und sagte]{12}: «[Lasst]{13}, [wir wollen sehen]{14}, [ob]{15} [Elija]{17} [kommt]{16}, um [ihn]{19} [herabzunehmen]{18}!» ~4(καί «und» bzw. «auch» nach τις; nicht eigens wiedergegeben)",
 "MRK.15.37": "[Jesus]{1,3} [aber]{2} [stiess]{4} [einen lauten]{6} [Schrei]{5} [aus]{4} und [verschied]{7}.",
 "MRK.15.38": "Und{1} [der Vorhang]{2,3} [des Tempels]{4,5} [riss]{6} [entzwei]{7,8}, [von]{9} [oben]{10} [bis]{11} [unten]{12}.",
 "MRK.15.39": "[Als]{1} [aber]{2} [der Hauptmann]{3,4}, [der]{5} [ihm]{9} [gegenüber]{7,8} [stand]{6}, [sah]{1}, [dass]{10} [er]{12} [so]{11} [verschied]{12}, [sagte er]{13}: «[Wahrhaftig]{14}, [dieser]{15} [Mensch]{16,17} [war]{20} [Gottes]{19} [Sohn]{18}!»",
 "MRK.15.40": "[Es waren]{1} [aber]{2} [auch]{3} [Frauen]{4} da, die [von]{5} [ferne]{6} [zuschauten]{7}; [unter]{8} [ihnen]{9} [auch]{10} [Maria]{11} [aus Magdala]{12,13} und{14} [Maria]{15}, [die Mutter]{16,22} [von Jakobus]{17} [dem Kleinen]{18,19} und{20} [Joses]{21}, und{23} [Salome]{24},",
 "MRK.15.41": "[die]{1} [ihm]{8}, [als]{2} [er]{3} [in]{4} [Galiläa]{5,6} [war]{3}, [gefolgt waren]{7} und{9} [ihm]{11} [gedient hatten]{10}, und{12} [viele]{14} [andere]{13}, [die]{15} [mit ihm]{17} [nach]{18} [Jerusalem]{19} [hinaufgezogen waren]{16}.",
 "MRK.15.42": "Und{1} [als es]{4} [schon]{2} [Abend]{3} [geworden war]{4} – [weil]{5} [es]{6} [Rüsttag]{7} [war]{6}, [das ist]{8,9} [der Tag vor dem Sabbat]{10} –,",
 "MRK.15.43": "[kam]{1} [Josef]{2} [von]{3,4} [Arimatäa]{5}, [ein angesehenes]{6} [Ratsmitglied]{7}, [der]{8} [auch]{9} [selbst]{10} auf [das Reich]{13,14} [Gottes]{15,16} [wartete]{11,12}; [er wagte es]{17}, [ging]{18} [zu]{19} [Pilatus]{20,21} [hinein]{18} und{22} [bat]{23} um [den Leib]{24,25} [Jesu]{26,27}.",
 "MRK.15.44": "[Pilatus]{1,3} [aber]{2} [wunderte sich]{4}, [ob]{5} [er]{7} [schon]{6} [tot sei]{7}, und{8} [er rief]{9} [den Hauptmann]{10,11} [herbei]{9} und [fragte]{12} [ihn]{13}, [ob]{14} [er]{16} [schon längst]{15} [gestorben sei]{16}.",
 "MRK.15.45": "Und{1} [als er es]{2} [vom]{3,4} [Hauptmann]{5} [erfahren hatte]{2}, [überliess er]{6} [den Leichnam]{7,8} [dem Josef]{9,10}.",
 "MRK.15.46": "Und{1} [er kaufte]{2} [ein Leinentuch]{3}, [nahm]{4} [ihn]{5} [herab]{4}, [wickelte]{6} ihn [in]{7} [das Leinentuch]{8} und{9} [legte]{10} [ihn]{11} [in]{12} [ein Grab]{13}, [das]{14} [aus]{17} [dem Felsen]{18} [gehauen]{16} [war]{15}, und{19} [wälzte]{20} [einen Stein]{21} [vor]{22} [den]{23} [Eingang]{24} [des Grabes]{25,26}.",
 "MRK.15.47": "[Maria]{1,3} [aus Magdala]{4,5} [aber]{2} und{6} [Maria]{7}, [die]{8} Mutter [des Joses]{9}, [sahen]{10}, [wo]{11} [er hingelegt worden war]{12}.",
 # ------------------------------------------------------------ Kapitel 16
 "MRK.16.1": "Und{1} [als]{2} [der Sabbat]{3,4} [vorüber war]{2}, [kauften]{15} [Maria]{5} [aus Magdala]{6,7} und{8} [Maria]{9}, [die]{10} Mutter [des Jakobus]{11,12}, und{13} [Salome]{14} [wohlriechende Öle]{16}, [um]{17} [hinzugehen]{18} und [ihn]{20} [zu salben]{19}.",
 "MRK.16.2": "Und{1} [sehr]{2} [früh]{3} [am]{4} [ersten Tag]{5} [der Woche]{6,7} [kommen sie]{8} [zum]{9,10} [Grab]{11}, [als]{12} [die Sonne]{13,14} [aufgegangen war]{12}.",
 "MRK.16.3": "Und{1} [sie sagten]{2} [zueinander]{3,4}: «[Wer]{5} [wird]{6} [uns]{7} [den Stein]{8,9} [vom]{10,11} [Eingang]{12} [des Grabes]{13,14} [wegwälzen]{6}?»",
 "MRK.16.4": "Und{1} [als sie aufblicken]{2}, [sehen sie]{3}, [dass]{4} [der Stein]{6,7} [weggewälzt ist]{5}; [er war]{8} [nämlich]{9} [sehr]{11} [gross]{10}.",
 "MRK.16.5": "Und{1} [sie gingen]{2} [in]{3} [das Grab]{4,5} [hinein]{2} und [sahen]{6} [einen jungen Mann]{7} [auf]{9} [der rechten Seite]{10,11} [sitzen]{8}, [bekleidet]{12} [mit einem weissen]{14} [Gewand]{13}; und{15} [sie entsetzten sich]{16}.",
 "MRK.16.6": "[Er]{1} [aber]{2} [sagt]{3} [zu ihnen]{4}: «[Entsetzt euch]{6} [nicht]{5}! [Ihr sucht]{8} [Jesus]{7}, [den Nazarener]{9,10}, [den Gekreuzigten]{11,12}. [Er ist auferweckt worden]{13}, [er ist]{15} [nicht]{14} [hier]{16}. [Seht]{17}, da ist [der Ort]{18,19}, [wo]{20} [sie]{21} [ihn]{22} [hingelegt haben]{21}.",
 "MRK.16.7": "[Aber]{1} [geht]{2}, [sagt]{3} [seinen]{4,6} [Jüngern]{5} und{7} [Petrus]{8,9}: ‹[Er geht]{11} [euch]{12} [voraus]{11} [nach]{13} [Galiläa]{14,15}; [dort]{16} [werdet ihr]{18} [ihn]{17} [sehen]{18}, [wie]{19} [er]{20} [euch]{21} [gesagt hat]{20}.›» ~10(ὅτι leitet die direkte Rede ein)",
 "MRK.16.8": "Und{1} [sie gingen hinaus]{2} und [flohen]{3} [vom]{4,5} [Grab]{6}; [denn]{8} [Zittern]{10} und{11} [Entsetzen]{12} [hatte]{7} [sie]{9} [ergriffen]{7}. Und{13} [sie sagten]{16} [niemandem]{14} [etwas]{15}; [sie fürchteten sich]{17} [nämlich]{18}. ⟦[Alles]{19} [aber]{20}, [was]{21} [aufgetragen worden war]{22}, [berichteten sie]{28} [kurz]{27} [denen]{23} [um]{24} [Petrus]{25,26}. [Danach]{29,31} [aber]{30} [sandte]{41} [auch]{32} [Jesus]{34,35} [selbst]{33} [durch]{42} [sie]{43} [vom]{36} [Osten]{37} [bis]{38,39} [zum Westen]{40} [die]{44} [heilige]{45} und{46} [unvergängliche]{47} [Botschaft]{48} [vom]{49} [ewigen]{50} [Heil]{51} [aus]{41}. [Amen]{52}.⟧",
 "MRK.16.9": "⟦[Nachdem er]{1} [aber]{2} [früh]{3} [am ersten Tag der Woche]{4,5} [auferstanden war]{1}, [erschien er]{6} [zuerst]{7} [Maria]{8} [aus Magdala]{9,10}, [aus]{11} [der]{12} [er]{13} [sieben]{14} [Dämonen]{15} [ausgetrieben hatte]{13}.",
 "MRK.16.10": "[Sie]{1} [ging hin]{2} und [berichtete]{3} es [denen]{4}, [die]{7} [mit]{5} [ihm]{6} [gewesen waren]{7} und nun [trauerten]{8} und{9} [weinten]{10}.",
 "MRK.16.11": "[Und als jene]{1} [hörten]{2}, [dass]{3} [er lebe]{4} und{5} [von]{7} [ihr]{8} [gesehen worden sei]{6}, [glaubten sie es nicht]{9}.",
 "MRK.16.12": "[Danach]{1,3} [aber]{2} [offenbarte er sich]{8} [zweien]{4} [von]{5} [ihnen]{6} [in]{9} [anderer]{10} [Gestalt]{11}, [als sie unterwegs waren]{7} und [aufs Land]{13,14} [gingen]{12}.",
 "MRK.16.13": "[Und jene]{1} [gingen hin]{2} und [berichteten]{3} es [den Übrigen]{4,5}; [auch]{6} [jenen]{7} [glaubten sie]{8} [nicht]{6}.",
 "MRK.16.14": "[Später]{1} [aber]{2} [offenbarte er sich]{7} [den Elf]{5,6} [selbst]{4}, [als sie zu Tisch lagen]{3}, und{8} [tadelte]{9} [ihren]{12} [Unglauben]{10,11} und{13} [ihre Herzenshärte]{14}, [weil]{15} [sie]{21} [denen]{16}, die [ihn]{18} [als Auferweckten]{19} [gesehen hatten]{17}, [nicht]{20} [geglaubt hatten]{21}.",
 "MRK.16.15": "Und{1} [er sagte]{2} [zu ihnen]{3}: «[Geht hin]{4} [in]{5} [die ganze]{6,8} [Welt]{7} und [verkündigt]{9} [das Evangelium]{10,11} [der ganzen]{12,13} [Schöpfung]{14}.",
 "MRK.16.16": "[Wer]{1} [glaubt]{2} und{3} [getauft wird]{4}, [wird gerettet werden]{5}; [wer]{6} [aber]{7} [nicht glaubt]{8}, [wird verurteilt werden]{9}.",
 "MRK.16.17": "[Diese]{5} [Zeichen]{1} [aber]{2} [werden]{6} [denen]{3} [folgen]{6}, [die glauben]{4}: [In]{7} [meinem]{10} [Namen]{8,9} [werden sie]{12} [Dämonen]{11} [austreiben]{12}, [in neuen]{15} [Sprachen]{13} [reden]{14},",
 "MRK.16.18": "[Schlangen]{1} [werden sie aufheben]{2}, [und wenn]{3} [sie]{6} [etwas]{5} [Tödliches]{4} [trinken]{6}, [wird es]{10} [ihnen]{9} [gewiss nicht]{7,8} [schaden]{10}; [Kranken]{11,12} [werden sie]{14} [die Hände]{13} [auflegen]{14}, und{15} [sie werden gesund werden]{16,17}.»",
 "MRK.16.19": "[Der Herr]{1,4} [Jesus]{5} [nun]{2,3}, [nachdem er]{6,7} [zu ihnen]{9} [geredet hatte]{8}, [wurde]{10} [in]{11} [den Himmel]{12,13} [aufgenommen]{10} und{14} [setzte sich]{15} [zur]{16} [Rechten]{17} [Gottes]{18,19}.",
 "MRK.16.20": "[Jene]{1} [aber]{2} [zogen aus]{3} und [verkündigten]{4} [überall]{5}; [der Herr]{6,7} [wirkte mit]{8} und{9} [bekräftigte]{12} [das Wort]{10,11} [durch]{13} [die]{14} [Zeichen]{16}, [die es begleiteten]{15}.⟧",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 14
 "MRK.14.1": "[In]{8} [zwei]{9} [Täg]{10} [aber]{2} [isch]{1} [s Passa]{3,4} und{5} [s Fäscht vo de ungsüürete Broot]{6,7} [gsii]{1}. Und{11} [d Hoheprieschter]{13,14} und{15} [d Schriftgleerte]{16,17} [händ gsuecht]{12}, [wie]{18} [si]{22} [en]{19} [mit]{20} [Lischt]{21} [chönted packe]{22} und [umbringe]{23}.",
 "MRK.14.2": "[Si händ]{1} [nämli]{2} [gseit]{1}: «[Nöd]{3} [am]{4,5} [Fäscht]{6}, [suscht]{7} [git s]{8} [no en Ufruer]{9} [im Volk]{10,11}.»",
 "MRK.14.3": "Und{1} [wo er]{3} [z]{4} [Betanie]{5} [im]{6,7} [Huus]{8} [vom Simon]{9} [em Ussätzige]{10,11} [gsii isch]{2} und [am Tisch gläge isch]{12,13}, [isch]{14} [e Frau]{15} [choo]{14} [mit]{16} [eme Alabaschtergfäss]{17} voll [tüürem]{21} [Salböl]{18} [us echter]{20} [Narde]{19}; [si hät]{22} [s]{23} [Gfäss]{24} [verbroche]{22} [und hät s]{25} [ihm]{26} [über]{25} [de]{27} [Chopf]{28} [gschüttet]{25}.",
 "MRK.14.4": "[Es paar]{3} [aber]{2} [sind]{1} [empört gsii]{4} [und händ zunenand gseit]{5,6}: «[Für was]{7,8} [hät s]{14} [die]{11} [Verschwändig]{9,10} [vom Salböl]{12,13} [gää]{14}?",
 "MRK.14.5": "[Mer hett]{1} [nämli]{2} [das]{3} [Salböl]{4,5} [für meh als]{7} [drüühundert]{9} [Denar]{8} [verchaufe]{6} und{10} [de Arme]{12,13} [gää]{11} [chöne]{1}.» Und{14} [si händ]{15} [si]{16} [aagschnauzt]{15}.",
 "MRK.14.6": "[De Jesus]{1,3} [aber]{2} [hät gseit]{4}: «[Lönd]{5} [si]{6} [in Rue]{5}! [Werum]{7} [mached ir]{10} [ere]{8} [Chummer]{9}? [Si hät]{13} [es guets]{11} [Wärch]{12} [a]{14} [mir]{15} [taa]{13}.",
 "MRK.14.7": "Dänn{2} [d Arme]{3,4} [händ ir]{5} [immer]{1} [bi]{6} [eu]{7}, und{8} [wänn]{9} [immer ir wänd]{10}, [chönd ir]{11} [ine]{12} [Guets]{13} [tue]{14}; [mich]{15} [aber]{16} [händ ir]{19} [nöd]{17} [immer]{18}.",
 "MRK.14.8": "[Was]{1} [si hät chöne]{2}, [hät si gmacht]{3}: [Si hät]{4} [min]{8} [Liib]{6,7} [zum voruus]{4} [gsalbet]{5} [für]{9} [d]{10} [Beerdigung]{11}.",
 "MRK.14.9": "[Amen]{1}, [ich säg s]{3} [eu]{4}: [Wo]{5} [immer]{6} [s]{8} [Evangelium]{9} [verchündet wird]{7} [i]{10} [de ganze]{11,12} [Wält]{13}, [dört wird]{18} [au]{14} [verzellt]{18}, [was]{15} [die]{17} [gmacht hät]{16}, [zur Erinnerig]{19,20} [a si]{21}.» ~2(δέ «aber» nach ἀμήν; nöd eigens widergää)",
 "MRK.14.10": "Und{1} [de Judas]{2} [Iskariot]{3}, [dä]{4} [eint]{5} [vo de Zwölf]{6,7}, [isch]{8} [zu]{9} [de Hoheprieschter]{10,11} [gange]{8}, [zum]{12} [en]{13} [ine]{15} [uslifere]{14}.",
 "MRK.14.11": "[Si]{1} [aber]{2} [händ sich gfröit]{4}, [wo si das ghört händ]{3}, und{5} [händ]{6} [em]{7} [Gält]{8} [z gää]{9} [versproche]{6}. Und{10} [er hät gsuecht]{11}, [wie]{12} [er]{15} [en]{13} [bi günschtiger Glägeheit]{14} [chönt uslifere]{15}.",
 "MRK.14.12": "Und{1} [am]{2} [erschte]{3} [Tag]{4} [vo de ungsüürete Broot]{5,6}, [wo]{7} [mer]{10} [s Passalamm]{8,9} [gschlachtet hät]{10}, [säged]{11} [sini]{15} [Jünger]{13,14} [zu ihm]{12}: «[Wo]{16} [wottsch]{17}, [dass mer]{19} [hiigönd]{18} und [s vorbereited]{19}, [demit]{20} [du]{21} [s Passa]{22,23} [chasch ässe]{21}?»",
 "MRK.14.13": "Und{1} [er schickt]{2} [zwei]{3} [vo sine]{4,6} [Jünger]{5} und{7} [seit]{8} [zu ine]{9}: «[Gönd]{10} [i]{11} [d]{12} [Stadt]{13}, und{14} [es wird]{15} [eu]{16} [en Mänsch]{17} [begägne]{15}, [wo]{20} [en Wasserchrueg]{18,19} [treit]{20}; [gönd]{21} [ihm]{22} [nache]{21},",
 "MRK.14.14": "und{1} [wo]{2} [er au]{3} [ine gaat]{4}, [säged]{5} [em Huusherr]{6,7}: ‹[De Lehrer]{9,10} [seit]{11}: Wo{12} [isch]{13} [mis]{16} [Gaschtzimmer]{14,15}, [wo]{17} [ich]{24} [mit]{20} [mine]{21,23} [Jünger]{22} [s Passa]{18,19} [chan ässe]{24}?› ~8(ὅτι leitet di diräkt Red ii)",
 "MRK.14.15": "Und{1} [er]{2} [wird]{4} [eu]{3} [en grosse]{6} [Saal im Obergschoss]{5} [zeige]{4}, [mit Polschter usgleit]{7} [und parat]{8}; und{9} [dört]{10} [mached]{11} [für üs]{12} [alles parat]{11}.»",
 "MRK.14.16": "Und{1} [d Jünger]{3,4} [sind usegange]{2} und{5} [sind]{6} [i]{7} [d Stadt]{8,9} [choo]{6} und{10} [händ s aatroffe]{11}, [wie]{12} [er]{13} [ine]{14} [gseit hät]{13}, und{15} [händ]{16} [s Passa]{17,18} [vorbereitet]{16}.",
 "MRK.14.17": "Und{1} [wo s Aabig worde isch]{2,3}, [chunnt er]{4} [mit]{5} [de Zwölf]{6,7}.",
 "MRK.14.18": "Und{1} [wo si]{3} [am Tisch gläge sind]{2} und{4} [ggässe händ]{5}, [hät]{8} [de Jesus]{6,7} [gseit]{8}: «[Amen]{9}, [ich säg s]{10} [eu]{11}: [Eine]{13} [vo]{14} [eu]{15} [wird]{16} [mich]{17} [uslifere]{16}, [eine, wo]{18} [mit]{20} [mir]{21} [isst]{19}.» ~12(ὅτι leitet di diräkt Red ii)",
 "MRK.14.19": "[Si händ aagfange]{1}, [truurig z wärde]{2} und{3} [zu ihm]{5} [z säge]{4}, [eine]{6} [nach]{7} [em andere]{8}: «[Doch nöd]{9} [ich]{10}?»",
 "MRK.14.20": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: «[Eine]{5} [vo de Zwölf]{6,7}, [eine, wo]{8} [mit]{10} [mir]{11} [i]{12} [d]{13} [Schüssle]{14} [iituuchet]{9}.",
 "MRK.14.21": "Dänn{1} [de Mänschesohn]{2,4-6} [gaat]{7} [zwar]{3} [dethii]{7}, [wie]{8} s [über]{10} [en]{11} [gschribe staat]{9}; [weh]{12} [aber]{13} [säbem]{16} [Mänsch]{14,15}, [dur]{17} [dä]{18} [de Mänschesohn]{19-22} [usgliferet wird]{23}! Es wär [besser]{24} [für en]{25}, [wänn]{26} [säbe]{31} [Mänsch]{29,30} [nie]{27} [gebore worde wär]{28}.»",
 "MRK.14.22": "Und{1} [wo si]{3} [ggässe händ]{2}, [hät er]{4} [Broot]{5} [gnoo]{4}, [hät de Lobpriis gsproche]{6}, [hät s broche]{7} und{8} [hät s]{9} [ine]{10} [gää]{9} und{11} [hät gseit]{12}: «[Nämed]{13}! [Das]{14} [isch]{15} [min]{18} [Liib]{16,17}.»",
 "MRK.14.23": "Und{1} [er hät]{2} [en Bächer]{3} [gnoo]{2}, [hät s Dankgebätt gsproche]{4} und [hät en]{5} [ine]{6} [gää]{5}, und{7} [si händ]{8} [alli]{11} [drus]{9,10} [trunke]{8}.",
 "MRK.14.24": "Und{1} [er hät]{2} [zu ine]{3} [gseit]{2}: «[Das]{4} [isch]{5} [mis]{8} [Bluet]{6,7} [vom Bund]{9,10}, [wo]{11} [für]{13} [vili]{14} [vergosse wird]{12}.",
 "MRK.14.25": "[Amen]{1}, [ich säg s]{2} [eu]{3}: [Ich wirde]{8} [nie meh]{5-7} [vom]{9,10} [Gwächs]{11} [vom Wiistock]{12,13} [trinke]{8} [bis]{14} [zu säbem]{15,17} [Tag]{16}, [wo]{18} [ich]{20} [s]{19} [nöi]{21} [trinke]{20} [im]{22,23} [Riich]{24} [vo Gott]{25,26}.» ~4(ὅτι leitet di diräkt Red ii)",
 "MRK.14.26": "Und{1} [nachdem si de Lobgsang gsunge händ]{2}, [sind si usegange]{3} [uf de]{4,5} [Ölberg]{6-8}.",
 "MRK.14.27": "Und{1} [de Jesus]{4,5} [seit]{2} [zu ine]{3}: «[Ir wärded]{8} [alli]{7} [z Fall choo]{8}, dänn{9} [es staat gschribe]{10}: ‹[Ich wirde]{11} [de Hirt]{12,13} [schlaa]{11}, und{14} [d Schaf]{15,16} [wärded verstreut]{17}.› ~6(ὅτι leitet di diräkt Red ii)",
 "MRK.14.28": "[Aber]{1} [nachdem]{2,3} [ich]{5} [uferweckt worde bi]{4}, [gang ich]{6} [eu]{7} [nach]{8} [Galiläa]{9,10} [voruus]{6}.»",
 "MRK.14.29": "[De Petrus]{1,3} [aber]{2} [hät]{4} [zu ihm]{5} [gseit]{4}: «[Au wänn]{6,7} [alli]{8} [z Fall chömed]{9}, [ich]{12} [aber]{10} [nöd]{11}!»",
 "MRK.14.30": "Und{1} [de Jesus]{4,5} [seit]{2} [zu ihm]{3}: «[Amen]{6}, [ich säg s]{7} [dir]{8}: [Du]{10} [wirsch]{22} [mich]{21} [hüt]{11}, [i dere]{12,13} [Nacht]{14}, [bevor]{15,16} [en Güggel]{18} [zweimal]{17} [chräit]{19}, [drüümal]{20} [verleugne]{22}.» ~9(ὅτι leitet di diräkt Red ii)",
 "MRK.14.31": "[Er]{1} [aber]{2} [hät]{4} [umso heftiger]{3} [beteuret]{4}: «[Wänn]{5} [ich]{7} [mit dir]{9} [sterbe]{8} [müesst]{6}, [ich wirde]{13} [dich]{12} [sicher nöd]{10,11} [verleugne]{13}!» [Gnau so]{14} [aber]{15} [händ]{18} [au]{16} [alli]{17} [gredt]{18}.",
 "MRK.14.32": "Und{1} [si chömed]{2} [zu]{3} [eme Grundstück]{4}, [wo]{5} [Getsemani]{8} [heisst]{6,7}, und{9} [er seit]{10} [zu sine]{11,13} [Jünger]{12}: «[Sitzed]{14} [da ane]{15}, [solang]{16} [ich bätte]{17}.»",
 "MRK.14.33": "Und{1} [er nimmt]{2} [de Petrus]{3,4} und{5} [de Jakobus]{6} und{7} [de Johannes]{8} [mit sich]{9,10}, und{11} [er hät aagfange]{12}, [sich z entsetze]{13} und{14} [Angscht z ha]{15},",
 "MRK.14.34": "und{1} [seit]{2} [zu ine]{3}: «[Ganz fescht truurig]{4} [isch]{5} [mini]{8} [Seel]{6,7}, [bis]{9} [zum Tod]{10}. [Bliibed]{11} [da]{12} und{13} [wached]{14}!»",
 "MRK.14.35": "Und{1} [er isch]{2} [es Stückli]{3} [wiitergange]{2}, [isch]{4} [uf]{5} [de Bode]{6,7} [gfalle]{4} und{8} [hät bätet]{9}, [dass]{10}, [wänn]{11} s [möglich]{12} [isch]{13}, [d Stund]{17,18} [a]{15} [ihm]{16} [verbii gaat]{14};",
 "MRK.14.36": "und{1} [er hät gseit]{2}: «[Abba]{3}, [Vatter]{4,5}, [alles]{6} isch [dir]{8} [möglich]{7}. [Nimm]{9} [dä]{12} [Bächer]{10,11} [vo]{13} [mir]{14} [weg]{9}! [Aber]{15} [nöd]{16}, [was]{17} [ich]{18} [wott]{19}, [sondern]{20} [was]{21} [du]{22} wottsch.»",
 "MRK.14.37": "Und{1} [er chunnt]{2} und{3} [findt]{4} [si]{5} [am Schlaafe]{6}, und{7} [seit]{8} [zum Petrus]{9,10}: «[Simon]{11}, [schlaafsch]{12}? [Häsch es]{14} [nöd]{13} [gschafft]{14}, [ei]{15} [Stund]{16} [wach z bliibe]{17}?",
 "MRK.14.38": "[Wached]{1} und{2} [bätted]{3}, [demit]{4} [ir]{6} [nöd]{5} [i]{7} [Versuechig]{8} [chömed]{6}! [De]{9} [Geischt]{11} isch [zwar]{10} [willig]{12}, [s]{13} [Fleisch]{15} [aber]{14} [schwach]{16}.»",
 "MRK.14.39": "Und{1} [er isch]{3} [wider]{2} [wäggange]{3}, [hät bätet]{4} und [di gliiche]{5,6} [Wort]{7} [gseit]{8}.",
 "MRK.14.40": "Und{1} [wo er]{3} [wider]{2} [choo isch]{3}, [hät er]{4} [si]{5} [schlaafend]{6} [aatroffe]{4}; [iri]{9} [Auge]{10,11} [sind]{7} [nämli]{8} [ganz schwär gsii]{12}, und{13} [si händ]{15} [nöd]{14} [gwüsst]{15}, [was]{16} [si]{17} [ihm]{18} [söled antworte]{17}.",
 "MRK.14.41": "Und{1} [er chunnt]{2} [zum dritte Mal]{3,4} und{5} [seit]{6} [zu ine]{7}: «[Schlaafed ir]{8} [no]{9,10} und{11} [ruehed eu us]{12}? [Es isch gnueg]{13}. [D Stund]{15,16} [isch choo]{14}; [lueg]{17}, [de Mänschesohn]{19-22} [wird]{18} [i]{23} [d Händ]{24,25} [vo de Sünder]{26,27} [usgliferet]{18}.",
 "MRK.14.42": "[Stönd uf]{1}, [mir gönd]{2}! [Lueg]{3}, [dä]{4}, wo [mich]{6} [usliferet]{5}, [isch nöch]{7}.»",
 "MRK.14.43": "Und{1} [grad]{2}, [no]{3} [während er]{4} [gredt hät]{5}, [chunnt]{6} [de Judas]{7}, [eine]{8} [vo de Zwölf]{9,10}, und{11} [mit]{12} [ihm]{13} [e Mängi]{14} [mit]{15} [Schwärter]{16} und{17} [Chnüppel]{18}, [vo]{19} [de Hoheprieschter]{20,21} und{22} [de Schriftgleerte]{23,24} und{25} [de Ältischte]{26,27}.",
 "MRK.14.44": "[Dä]{3}, wo [en]{5} [usgliferet hät]{4}, [hät]{1} [ine]{7} [aber]{2} [es Zeiche]{6} [gää]{1} [und gseit]{8}: «[Dä]{9}, [wo]{10} [ich küsse]{11}, [dä]{12} [isch es]{13}. [Packed]{14} [en]{15} und{16} [füered en]{17} [sicher]{18} [ab]{17}!»",
 "MRK.14.45": "Und{1} [wo er choo isch]{2}, [isch er]{4} [grad]{3} [zu ihm]{5} [ane]{4} und [seit]{6}: «[Rabbi]{7}!», und{8} [hät]{9} [en]{10} [küsst]{9}.",
 "MRK.14.46": "[Si]{1} [aber]{2} [händ]{3} [d Händ]{4,5} [a ihn]{6} [gleit]{3} und{7} [händ]{8} [en]{9} [feschtgnoo]{8}.",
 "MRK.14.47": "[Eine]{1,3} [vo de Umstehende]{4,5} [aber]{2} [hät]{6} [s]{7} [Schwärt]{8} [zoge]{6}, [hät]{9} [de]{10} [Chnächt]{11} [vom Hoheprieschter]{12,13} [troffe]{9} und{14} [hät]{15} [em]{16} [s]{17} [Oor]{18} [abghaue]{15}.",
 "MRK.14.48": "Und{1} [de Jesus]{3,4} [hät s Wort gnoo]{2} und [zu ine]{6} [gseit]{5}: «[Wie]{7} [gäge]{8} [en Röiber]{9} [sind ir uuszoge]{10} [mit]{11} [Schwärter]{12} und{13} [Chnüppel]{14}, zum [mich]{16} [feschtnää]{15}?",
 "MRK.14.49": "[Jede Tag]{1,2} [bin ich]{3} [bi]{4} [eu]{5} [im]{6,7} [Tämpel]{8} [gsii]{3} [und ha glehrt]{9}, und{10} [ir händ]{12} [mich]{13} [nöd]{11} [packt]{12}. [Aber]{14} das gschiet, [demit]{15} [d Schrifte]{17,18} [erfüllt wärded]{16}.»",
 "MRK.14.50": "Und{1} [si händ]{2} [en]{3} [verlaa]{2} und [sind]{4} [alli]{5} [gflüchtet]{4}.",
 "MRK.14.51": "Und{1} [en junge Maa]{2,3} [isch]{4} [ihm]{5} [nachegange]{4}, [aagleit]{6} [mit eme Liinetuech]{7} [uf]{8} [em blutte Liib]{9}; und{10} [si packed]{11} [en]{12},",
 "MRK.14.52": "[er]{1} [aber]{2} [hät]{3} [s]{4} [Liinetuech]{5} [zrugglaa]{3} und [isch]{7} [blutt]{6} [gflüchtet]{7}.",
 "MRK.14.53": "Und{1} [si händ]{2} [de Jesus]{3,4} [zum]{5,6} [Hoheprieschter]{7} [abgfüert]{2}, und{8} [es chömed]{9} [alli]{10} [Hoheprieschter]{11,12} und{13} [d Ältischte]{14,15} und{16} [d Schriftgleerte]{17,18} [zäme]{9}.",
 "MRK.14.54": "Und{1} [de Petrus]{2,3} [isch]{6} [ihm]{7} [vo]{4} [wiitem]{5} [nachegange]{6} [bis]{8} [ine]{9} [in]{10} [de]{11} [Hof]{12} [vom Hoheprieschter]{13,14}, und{15} [er isch]{16,17} [bi]{18} [de]{19} [Diener]{20} [gsässe]{16,17} und{21} [hät sich]{22} [am]{23,24} [Füür]{25} [gwärmt]{22}.",
 "MRK.14.55": "[D Hoheprieschter]{1,3} [aber]{2} und{4} [de ganz]{5,6} [Hoch Raat]{7} [händ]{8} [es Züügnis]{12} [gäge]{9} [de Jesus]{10,11} [gsuecht]{8}, [zum]{13,14} [en]{16} [töte]{15}, und{17} [händ]{19} [keis]{18} [gfunde]{19}.",
 "MRK.14.56": "[Vili]{1} [händ]{3} [nämli]{2} [falsch]{3} [gäge]{4} [ihn]{5} [usgseit]{3}, und{6} [d]{8} [Uussage]{9} [händ]{11} [nöd]{10} [zämegstimmt]{7}.",
 "MRK.14.57": "Und{1} [es paar]{2} [sind ufgstande]{3}, [händ]{4} [falsch]{4} [gäge]{5} [ihn]{6} [usgseit]{4} und [gseit]{7}:",
 "MRK.14.58": "«[Mir]{2} [händ]{3} [en]{4} [säge]{5} [ghört]{3}: ‹[Ich]{7} [wirde]{8} [dä]{11} [Tämpel]{9,10}, [wo]{12} [vo Händ gmacht isch]{13}, [abrisse]{8} und{14} [in]{15} [drüü]{16} [Täg]{17} [en andere]{18} [baue]{20}, [wo nöd vo Händ gmacht isch]{19}.›» ~1(ὅτι leitet di diräkt Red ii) ~6(ὅτι leitet di diräkt Red ii)",
 "MRK.14.59": "Und{1} [au]{2} [so]{3} [hät]{5} [iri]{8} [Uussag]{6,7} [nöd]{2} [zämegstimmt]{4}.",
 "MRK.14.60": "Und{1} [de Hoheprieschter]{3,4} [isch]{2} [i]{5} [d Mitti]{6} [gstande]{2}, [hät]{7} [de Jesus]{8,9} [gfröget]{7} [und gseit]{10}: «[Antwortisch]{12} [nüt]{11,13}? [Was]{14} [säged]{17} [die]{15} [gäge dich]{16} [uus]{17}?»",
 "MRK.14.61": "[Er]{1} [aber]{2} [hät gschwige]{3} und{4} [hät]{6} [nüt]{5,7} [gantwortet]{6}. [Wider]{8} [hät]{11} [en]{12} [de Hoheprieschter]{9,10} [gfröget]{11} und{13} [seit]{14} [zu ihm]{15}: «[Bisch]{17} [du]{16} [de Christus]{18,19}, [de Sohn]{20,21} [vom Hochgelobte]{22,23}?»",
 "MRK.14.62": "[De Jesus]{1,3} [aber]{2} [hät gseit]{4}: «[Ich]{5} [bi s]{6}, und{7} [ir wärded]{8} [de Mänschesohn]{9-12} [zur]{13} [Rächte]{14} [vo de Macht]{16,17} [gseh]{8} [sitze]{15} und{18} [mit]{20} [de Wolche]{21,22} [vom Himmel]{23,24} [choo]{19}.»",
 "MRK.14.63": "[De Hoheprieschter]{1,3} [aber]{2} [hät]{4} [sini]{7} [Chleider]{5,6} [verrisse]{4} und [seit]{8}: «[Für was]{9} [bruuched mer]{11,12} [no]{10} [Züüge]{13}?",
 "MRK.14.64": "[Ir händ]{1} [d]{2} [Läschterig]{3} [ghört]{1}. [Was]{4} [meined]{6} [ir]{5}?» [Si]{7} [aber]{8} [händ]{10} [en]{11} [alli]{9} [verurteilt]{10}: [Er häig de Tod verdient]{12-14}.",
 "MRK.14.65": "Und{1} [es paar]{3} [händ aagfange]{2}, [en]{5} [aazspöie]{4}, und{6} [sis]{8} [Gsicht]{9,10} [z verdecke]{7} und{11} [en]{13} [mit de Füüscht z schlaa]{12} und{14} [zu ihm]{16} [z säge]{15}: «[Weissag]{17}!» Und{18} [d Diener]{19,20} [händ]{23} [en]{22} [mit Schleeg]{21} [in Empfang gnoo]{23}.",
 "MRK.14.66": "Und{1} [wo]{2} [de Petrus]{3,4} [unde]{5} [im]{6,7} [Hof]{8} [gsii isch]{2}, [chunnt]{9} [eini]{10} [vo de Mägd]{11,12} [vom Hoheprieschter]{13,14},",
 "MRK.14.67": "und{1} [wo si]{2} [de Petrus]{3,4} [gseh hät]{2}, [wie er sich gwärmt hät]{5}, [hät si]{6} [en]{7} [aagluegt]{6} und [seit]{8}: «[Au]{9} [du]{10} [bisch]{14} [mit]{11} [em Nazarener]{12,13} [gsii]{14}, [em Jesus]{15,16}!»",
 "MRK.14.68": "[Er]{1} [aber]{2} [hät s]{3} [abgstritte]{3} und [gseit]{4}: «[Ich weiss]{6} [nöd]{5} [und verstaa]{8} [nöd]{7}, [was]{10} [du]{9} [seisch]{11}.» Und{12} [er isch]{13} [use]{14} [in]{15} [de]{16} [Vorhof]{17} [gange]{13}; und{18} [en Güggel]{19} [hät gchräit]{20}.",
 "MRK.14.69": "Und{1} [d Magd]{2,3} [hät]{4} [en]{5} [gseh]{4} und [hät]{6} [wider]{7} [aagfange]{6}, [zu de Umstehende]{9,10} [z säge]{8}: «[Dä]{12} [isch]{15} [eine vo]{13} [ine]{14}!» ~11(ὅτι leitet di diräkt Red ii)",
 "MRK.14.70": "[Er]{1} [aber]{2} [hät s]{4} [wider]{3} [abgstritte]{4}. Und{5} [nach]{6} [ere churze Ziit]{7} [händ]{11} [d Umstehende]{9,10} [wider]{8} [zum Petrus]{12,13} [gseit]{11}: «[Würkli]{14}, [du bisch]{17} [eine vo]{15} [ine]{16}; [dänn]{19} [du bisch]{21} [au]{18} [en Galiläer]{20}, und{22} [dini]{25} [Spraach]{23,24} [passt dezue]{26}!»",
 "MRK.14.71": "[Er]{1} [aber]{2} [hät aagfange]{3}, [sich z verflueche]{4} und{5} [z schwööre]{6}: «[Ich kenn]{9} [dä]{12} [Mänsch]{10,11} [nöd]{8}, [vo dem]{13} [ir redet]{14}!» ~7(ὅτι leitet di diräkt Red ii)",
 "MRK.14.72": "Und{1} [grad]{2} [hät]{6} [en Güggel]{5} [zum zweite Mal]{3,4} [gchräit]{6}. Und{7} [de Petrus]{9,10} [hät sich]{8} [as]{11} [Wort]{12} [erinneret]{8}, [wie]{13} [de Jesus]{16,17} [zu ihm]{15} [gseit hät]{14}: «[Bevor]{19} [en Güggel]{20} [zweimal]{22} [chräit]{21}, [wirsch du]{25} [mich]{24} [drüümal]{23} [verleugne]{25}.» Und{26} [er hät dra dänkt]{27} und [hät briegget]{28}. ~18(ὅτι leitet di diräkt Red ii)",
 # ------------------------------------------------------------ Kapitel 15 (15,28 fehlt im SBLGNT)
 "MRK.15.1": "Und{1} [grad]{2} [am früene Morge]{3} [händ]{5} [d Hoheprieschter]{6,7} [mit]{8} [de Ältischte]{9,10} und{11} [Schriftgleerte]{12} und{13} [de ganz]{14,15} [Hoch Raat]{16} [en Bschluss]{4} [gfasst]{5}; [si händ]{17} [de Jesus]{18,19} [gfesslet]{17}, [abgfüert]{20} und{21} [em Pilatus]{23} [usgliferet]{22}.",
 "MRK.15.2": "Und{1} [de Pilatus]{4,5} [hät]{2} [en]{3} [gfröget]{2}: «[Bisch]{7} [du]{6} [de König]{8,9} [vo de Jude]{10,11}?» [Er]{12} [aber]{13} [antwortet]{14} [ihm]{15} [und seit]{16}: «[Du]{17} [seisch es]{18}.»",
 "MRK.15.3": "Und{1} [d Hoheprieschter]{4,5} [händ]{2} [en]{3} [wäge vilne Sache]{6} [aaklagt]{2}.",
 "MRK.15.4": "[De Pilatus]{1,3} [aber]{2} [hät]{5} [en]{6} [wider]{4} [gfröget]{5} [und gseit]{7}: «[Antwortisch]{9} [nüt]{8,10}? [Lueg]{11}, [wie vil]{12} [si]{14} [dir]{13} [vorwärfed]{14}!»",
 "MRK.15.5": "[De Jesus]{1,3} [aber]{2} [hät]{6} [nüt meh]{4,5} [gantwortet]{6}, [sodass]{7} [de Pilatus]{9,10} [sich gwunderet hät]{8}.",
 "MRK.15.6": "[Zum]{1} [Fäscht]{3} [aber]{2} [hät er]{4} [ine]{5} [jewiils eine]{6} [Gfangne]{7} [freiglaa]{4}, [wo]{8} [si sich gwünscht händ]{9}.",
 "MRK.15.7": "Es [isch]{1} [aber]{2} [de sogenannt]{3,4} [Barabbas]{5} [mit]{6} [de Ufständische]{7,8} [gfange]{9} [gsii]{1}, [wo]{10} [bim]{11,12} [Ufstand]{13} [en Mord]{14} [begange gha händ]{15}.",
 "MRK.15.8": "Und{1} [d Mängi]{3,4} [isch ufezoge]{2} und [hät aagfange]{5} [z bitte]{6}, [wie]{7} [er s]{8} [für si]{9} [immer gmacht hät]{8}.",
 "MRK.15.9": "[De Pilatus]{1,3} [aber]{2} [hät]{4} [ine]{5} [gantwortet]{4} [und gseit]{6}: «[Wänd ir]{7}, [dass ich]{8} [eu]{9} [de König]{10,11} [vo de Jude]{12,13} [freilaa]{8}?»",
 "MRK.15.10": "[Er hät]{1} [nämli]{2} [gmerkt]{1}, [dass]{3} [d Hoheprieschter]{8,9} [en]{7} [us]{4} [Niid]{5} [usgliferet händ]{6}.",
 "MRK.15.11": "[D Hoheprieschter]{1,3} [aber]{2} [händ]{4} [d Mängi]{5,6} [ufgwieglet]{4}, [dass er]{7} [ine]{12} [lieber]{8} [de Barabbas]{9,10} [freilaat]{11}.",
 "MRK.15.12": "[De Pilatus]{1,3} [aber]{2} [hät]{5} [wider]{4} [gantwortet]{5} und [zu ine]{7} [gseit]{6}: «[Was]{8} [wänd ir]{10} [dänn]{9}, [dass ich]{11} [mit dem mach]{11}, [wo]{12} [ir]{13} [de König]{14,15} [vo de Jude]{16,17} [nänned]{13}?»",
 "MRK.15.13": "[Si]{1} [aber]{2} [händ]{4} [wider]{3} [brüelet]{4}: «[Chrüüzig]{5} [en]{6}!»",
 "MRK.15.14": "[De Pilatus]{1,3} [aber]{2} [hät]{4} [zu ine]{5} [gseit]{4}: «[Was]{6} [hät er]{8} [dänn]{7} [Böses]{9} [gmacht]{8}?» [Si]{10} [aber]{11} [händ]{13} [no lüüter]{12} [brüelet]{13}: «[Chrüüzig]{14} [en]{15}!»",
 "MRK.15.15": "[De Pilatus]{1,3} [aber]{2} [hät wele]{4} [d Mängi]{5,6} [zfride stelle]{7-9} und [hät]{10} [ine]{11} [de Barabbas]{12,13} [freiglaa]{10}; und{14} [de Jesus]{16,17} [hät er la gisle]{18} und [usgliferet]{15}, [demit er gchrüüziget wird]{19,20}.",
 "MRK.15.16": "[D Soldate]{1,3} [aber]{2} [händ]{4} [en]{5} [abgfüert]{4}, [ine]{6} [in Palascht]{7,8}, [das isch]{9,10} [s Prätorium]{11}, und{12} [rüefed]{13} [di ganz]{14,15} [Kohorte]{16} [zäme]{13}.",
 "MRK.15.17": "Und{1} [si leged]{2} [ihm]{3} [en Purpurmantel]{4} [aa]{2} und{5} [flächted]{8} [en Dornechranz]{9,10} und [setzed]{6} en [ihm]{7} [uf]{6};",
 "MRK.15.18": "und{1} [si händ aagfange]{2}, [en]{4} [z grüesse]{3}: «[Sig gegrüesst]{5}, [König]{6} [vo de Jude]{7,8}!»",
 "MRK.15.19": "Und{1} [si händ]{2} [en]{3} [mit eme Rohr]{6} [uf de]{4} [Chopf]{5} [gschlage]{2} und{7} [händ]{8} [en]{9} [aagspöit]{8}, und{10} [si sind]{11} [uf d Chnüü]{12,13} [gange]{11} und [händ sich]{14} [vor ihm]{15} [nidergworfe]{14}.",
 "MRK.15.20": "Und{1} [wo]{2} [si]{3} [en]{4} [verspottet händ]{3}, [händ si]{5} [ihm]{6} [de Purpurmantel]{7,8} [abzoge]{5} und{9} [händ]{10} [ihm]{11} [sini eigete]{14,15} [Chleider]{12,13} [aagleit]{10}. Und{16} [si füered]{17} [en]{18} [use]{17}, [zum]{19} [en]{21} [chrüüzige]{20}.",
 "MRK.15.21": "Und{1} [si zwinged]{2} [eine]{4}, [wo verbiichunnt]{3}, [de Simon]{5} [vo Kyrene]{6}, wo [vom]{8} [Fäld]{9} [chunnt]{7}, [de Vatter]{10,11} [vom Alexander]{12} und{13} [vom Rufus]{14}, [sis]{19} [Chrüüz]{17,18} [z träge]{15,16}.",
 "MRK.15.22": "Und{1} [si bringed]{2} [en]{3} [a]{4} [de]{5} [Ort]{7} [Golgota]{6}, [das]{8} [heisst]{9} [übersetzt]{10} «[Schädelplatz]{11,12}».",
 "MRK.15.23": "Und{1} [si händ]{2} [ihm]{3} [Wii]{5} [mit Myrrhe drin]{4} [wele gää]{2}; [er]{6} [aber]{7} [hät en]{9} [nöd]{8} [gnoo]{9}.",
 "MRK.15.24": "Und{1} [si chrüüziged]{2} [en]{3} und{4} [verteiled]{5} [sini]{8} [Chleider]{6,7} [und wärfed]{9} [s Los]{10} [drüber]{11,12}, [wär]{13} [was]{14} [söll übercho]{15}.",
 "MRK.15.25": "[Es isch]{1} [aber]{2} [di dritt]{4} [Stund]{3} [gsii]{1}, und{5} [si händ]{6} [en]{7} [gchrüüziget]{6}.",
 "MRK.15.26": "Und{1} [d Ufschrift]{3,4} mit [de Aaklag]{5,6} [gäge en]{7} [hät]{2,8} [gheisse]{2,8}: «[De König]{9,10} [vo de Jude]{11,12}.»",
 "MRK.15.27": "Und{1} [mit]{2} [ihm]{3} [chrüüziged si]{4} [zwei]{5} [Röiber]{6}, [eine]{7} [rächts]{8,9} und{10} [eine]{11} [linggs]{12,13} [vo ihm]{14}.",
 "MRK.15.29": "Und{1} [die, wo verbii gönd]{2,3}, [händ]{4} [en]{5} [verläschteret]{4}, [händ]{6} [iri]{9} [Chöpf]{7,8} [gschüttlet]{6} und{10} [gseit]{11}: «[Ha]{12}, [du, wo]{13} [de Tämpel]{15,16} [abrissisch]{14} und{17} [in]{19} [drüü]{20} [Täg]{21} [ufbausch]{18},",
 "MRK.15.30": "[rett]{1} [dich sälber]{2} [und chumm abe]{3} [vom]{4,5} [Chrüüz]{6}!»",
 "MRK.15.31": "[Gnau so]{1} [händ]{5} [au]{2} [d Hoheprieschter]{3,4} [undernand]{6,7} [mit]{8} [de Schriftgleerte]{9,10} [gspottet]{5} und [gseit]{11}: «[Anderi]{12} [hät er grettet]{13}, [sich sälber]{14} [chan er]{16} [nöd]{15} [rette]{17}.",
 "MRK.15.32": "[De Christus]{1,2}, [de König]{3,4} [vo Israel]{5}, [söll]{6} [jetzt]{7} [vom]{8,9} [Chrüüz]{10} [abecho]{6}, [demit]{11} [mir]{12} [s gsehnd]{12} und{13} [glaubed]{14}!» Und{15} [die]{16}, wo [mit]{18} [ihm]{19} [gchrüüziget worde sind]{17}, [händ]{20} [en]{21} [beschimpft]{20}.",
 "MRK.15.33": "Und{1} [wo]{2} [di sächst]{4} [Stund]{3} [choo isch]{2}, [isch]{6} [e Fischternis]{5} [über]{7} [s ganz]{8,9} [Land]{10} [choo]{6} [bis]{11} [zur nüünte]{13} [Stund]{12}.",
 "MRK.15.34": "Und{1} [zur]{2} [nüünte]{3} [Stund]{4} [hät]{5} [de Jesus]{6,7} [mit luuter]{9} [Stimm]{8} [gschroue]{5}: «[Eloi]{10}, [Eloi]{11}, [lema]{12} [sabachthani]{13}?», [das]{14} [heisst]{15} [übersetzt]{16}: «[Min]{19} [Gott]{17,18}, [min]{22} [Gott]{20,21}, [für was]{23,24} [häsch du]{25} [mich]{26} [verlaa]{25}?»",
 "MRK.15.35": "Und{1} [es paar]{2} [vo de Umstehende]{3,4} [händ das ghört]{5} und [gseit]{6}: «[Lueged]{7}, [er rüeft]{9} [em Elija]{8}!»",
 "MRK.15.36": "[Eine]{3} [aber]{2} [isch anegrännt]{1}, [hät]{5} [en Schwamm]{6} [mit Essig]{7} [gfüllt]{5}, [en]{8} [uf es Rohr]{9} [gsteckt]{8} und [ihm]{11} [z trinke gää]{10} [und gseit]{12}: «[Lönd]{13}, [mir wänd luege]{14}, [öb]{15} [de Elija]{17} [chunnt]{16}, zum [en]{19} [abenää]{18}!» ~4(καί «und» oder «au» nach τις; nöd eigens widergää)",
 "MRK.15.37": "[De Jesus]{1,3} [aber]{2} [hät]{4} [en luute]{6} [Schrei]{5} [usgstoosse]{4} und [isch gstorbe]{7}.",
 "MRK.15.38": "Und{1} [de Vorhang]{2,3} [vom Tämpel]{4,5} [isch]{6} [in zwei Stuck]{7,8} [verrisse]{6}, [vo]{9} [obe]{10} [bis]{11} [unde]{12}.",
 "MRK.15.39": "[Wo]{1} [aber]{2} [de Hauptmaa]{3,4}, [wo]{5} [ihm]{9} [vis-à-vis]{7,8} [gstande isch]{6}, [gseh hät]{1}, [dass]{10} [er]{12} [eso]{11} [gstorbe isch]{12}, [hät er gseit]{13}: «[Würkli]{14}, [dä]{15} [Mänsch]{16,17} [isch]{20} [Gottes Sohn]{18,19} [gsii]{20}!»",
 "MRK.15.40": "[Es sind]{1} [aber]{2} [au]{3} [Fraue]{4} [da gsii]{1}, wo [vo]{5} [wiitem]{6} [zuegluegt händ]{7}; [under]{8} [ine]{9} [au]{10} [d Maria]{11} [vo Magdala]{12,13} und{14} [d Maria]{15}, [d Mueter]{16,22} [vom Jakobus]{17} [em Chliine]{18,19} und{20} [vom Joses]{21}, und{23} [d Salome]{24},",
 "MRK.15.41": "[wo]{1} [ihm]{8}, [wo]{2} [er]{3} [z]{4} [Galiläa]{5,6} [gsii isch]{3}, [nachegange sind]{7} und{9} [ihm]{11} [dienet händ]{10}, und{12} [vili]{14} [anderi]{13}, [wo]{15} [mit ihm]{17} [uf]{18} [Jerusalem]{19} [ufegange sind]{16}.",
 "MRK.15.42": "Und{1} [wo s]{4} [scho]{2} [Aabig]{3} [worde isch]{4} – [wil]{5} [es]{6} [Rüschttag]{7} [gsii isch]{6}, [das isch]{8,9} [de Tag vor em Sabbat]{10} –,",
 "MRK.15.43": "[isch]{1} [de Josef]{2} [vo]{3,4} [Arimatäa]{5} [choo]{1}, [es aagsehnigs]{6} [Ratsmitglied]{7}, [wo]{8} [au]{9} [sälber]{10} uf [s Riich]{13,14} [vo Gott]{15,16} [gwartet hät]{11,12}; [er hät sich trout]{17}, [isch]{18} [zum]{19,20} [Pilatus]{21} [ine gange]{18} und{22} [hät]{23} [de Liib]{24,25} [vom Jesus]{26,27} [verlangt]{23}.",
 "MRK.15.44": "[De Pilatus]{1,3} [aber]{2} [hät sich gwunderet]{4}, [öb]{5} [er]{7} [scho]{6} [tot sig]{7}, und{8} [er hät]{9} [de Hauptmaa]{10,11} [zue sich grüeft]{9} und [hät]{12} [en]{13} [gfröget]{12}, [öb]{14} [er]{16} [scho lang]{15} [gstorbe sig]{16}.",
 "MRK.15.45": "Und{1} [wo er s]{2} [vom]{3,4} [Hauptmaa]{5} [erfahre hät]{2}, [hät er]{6} [de Liichnam]{7,8} [em Josef]{9,10} [überlaa]{6}.",
 "MRK.15.46": "Und{1} [er hät]{2} [es Liinetuech]{3} [gchauft]{2}, [hät]{4} [en]{5} [abegnoo]{4}, [hät]{6} en [is]{7} [Liinetuech]{8} [iigwicklet]{6} und{9} [hät]{10} [en]{11} [in]{12} [es Grab]{13} [gleit]{10}, [wo]{14} [us]{17} [em Fels]{18} [ghaue]{16} [gsii isch]{15}, und{19} [hät]{20} [en Stei]{21} [vor]{22} [de]{23} [Iigang]{24} [vom Grab]{25,26} [gwälzt]{20}.",
 "MRK.15.47": "[D Maria]{1,3} [vo Magdala]{4,5} [aber]{2} und{6} [d Maria]{7}, [d]{8} Mueter [vom Joses]{9}, [händ gseh]{10}, [wo]{11} [er anegleit worde isch]{12}.",
 # ------------------------------------------------------------ Kapitel 16
 "MRK.16.1": "Und{1} [wo]{2} [de Sabbat]{3,4} [verbii gsii isch]{2}, [händ]{15} [d Maria]{5} [vo Magdala]{6,7} und{8} [d Maria]{9}, [d]{10} Mueter [vom Jakobus]{11,12}, und{13} [d Salome]{14} [wohlschmöckendi Öl]{16} [gchauft]{15}, [zum]{17} [anegaa]{18} und [en]{20} [salbe]{19}.",
 "MRK.16.2": "Und{1} [ganz]{2} [früe]{3} [am]{4} [erschte Tag]{5} [vo de Wuche]{6,7} [chömed si]{8} [zum]{9,10} [Grab]{11}, [wo]{12} [d Sunne]{13,14} [ufgange gsii isch]{12}.",
 "MRK.16.3": "Und{1} [si händ]{2} [zunenand]{3,4} [gseit]{2}: «[Wär]{5} [wälzt]{6} [üs]{7} [de Stei]{8,9} [vom]{10,11} [Iigang]{12} [vom Grab]{13,14} [ewägg]{6}?»",
 "MRK.16.4": "Und{1} [wo si uflueged]{2}, [gsehnd si]{3}, [dass]{4} [de Stei]{6,7} [wäggwälzt isch]{5}; [er isch]{8} [nämli]{9} [sehr]{11} [gross]{10} [gsii]{8}.",
 "MRK.16.5": "Und{1} [si sind]{2} [is Grab]{3-5} [ine gange]{2} und [händ]{6} [en junge Maa]{7} [uf]{9} [de rächte Siite]{10,11} [sitze]{8} [gseh]{6}, [aagleit]{12} [mit eme wiisse]{14} [Gwand]{13}; und{15} [si händ sich entsetzt]{16}.",
 "MRK.16.6": "[Er]{1} [aber]{2} [seit]{3} [zu ine]{4}: «[Entsetzed eu]{6} [nöd]{5}! [Ir sueched]{8} [de Jesus]{7}, [de Nazarener]{9,10}, [de Gchrüüzigt]{11,12}. [Er isch uferweckt worde]{13}, [er isch]{15} [nöd]{14} [da]{16}. [Lueged]{17}, da isch [de Ort]{18,19}, [wo]{20} [si]{21} [en]{22} [anegleit händ]{21}.",
 "MRK.16.7": "[Aber]{1} [gönd]{2}, [säged]{3} [sine]{4,6} [Jünger]{5} und{7} [em Petrus]{8,9}: ‹[Er gaat]{11} [eu]{12} [voruus]{11} [nach]{13} [Galiläa]{14,15}; [dört]{16} [wärded ir]{18} [en]{17} [gseh]{18}, [wie]{19} [er]{20} [eu]{21} [gseit hät]{20}.›» ~10(ὅτι leitet di diräkt Red ii)",
 "MRK.16.8": "Und{1} [si sind usegange]{2} und [devogrännt]{3} [vom]{4,5} [Grab]{6}; [dänn]{8} [Zittere]{10} und{11} [Entsetze]{12} [hät]{7} [si]{9} [packt]{7}. Und{13} [si händ]{16} [niemertem]{14} [öppis]{15} [gseit]{16}; [si händ sich]{17} [nämli]{18} [gfürchtet]{17}. ⟦[Alles]{19} [aber]{20}, [wo]{21} [ine ufträge worde isch]{22}, [händ si]{28} [churz]{27} [dene]{23} [um]{24} [de Petrus]{25,26} [verzellt]{28}. [Dänn]{29,31} [aber]{30} [hät]{41} [au]{32} [de Jesus]{34,35} [sälber]{33} [dur]{42} [si]{43} [vom]{36} [Oschte]{37} [bis]{38,39} [zum Weschte]{40} [di heilig]{44,45} und{46} [unvergänglich]{47} [Botschaft]{48} [vom]{49} [ewige]{50} [Heil]{51} [usgschickt]{41}. [Amen]{52}.⟧",
 "MRK.16.9": "⟦[Nachdem er]{1} [aber]{2} [früe]{3} [am erschte Tag vo de Wuche]{4,5} [uferstande gsii isch]{1}, [isch er]{6} [zerscht]{7} [de Maria]{8} [vo Magdala]{9,10} [erschine]{6}, [us]{11} [dere]{12} [er]{13} [sibe]{14} [Dämone]{15} [ustribe gha hät]{13}.",
 "MRK.16.10": "[Si]{1} [isch gange]{2} und [hät]{3} es [dene]{4} [verzellt]{3}, [wo]{7} [mit]{5} [ihm]{6} [gsii sind]{7} und jetzt [truured]{8} und{9} [briegged]{10}.",
 "MRK.16.11": "[Und wo die]{1} [ghört händ]{2}, [dass]{3} [er läbi]{4} und{5} [vo]{7} [ere]{8} [gseh worde sig]{6}, [händ si s nöd glaubt]{9}.",
 "MRK.16.12": "[Dänn]{1,3} [aber]{2} [hät er sich]{8} [zweine]{4} [vo]{5} [ine]{6} [in ere]{9} [andere]{10} [Gstalt]{11} [zeigt]{8}, [wo si understwägs gsii sind]{7} und [ufs Land]{13,14} [gange sind]{12}.",
 "MRK.16.13": "[Und die]{1} [sind gange]{2} und [händ]{3} es [de Andere]{4,5} [verzellt]{3}; [au]{6} [dene]{7} [händ si]{8} [nöd]{6} [glaubt]{8}.",
 "MRK.16.14": "[Spöter]{1} [aber]{2} [hät er sich]{7} [de Elf]{5,6} [sälber]{4} [zeigt]{7}, [wo si am Tisch gläge sind]{3}, und{8} [hät]{9} [iren]{12} [Unglaube]{10,11} und{13} [iri Härzenshärti]{14} [tadlet]{9}, [wil]{15} [si]{21} [dene]{16}, wo [en]{18} [als Uferweckte]{19} [gseh händ]{17}, [nöd]{20} [glaubt händ]{21}.",
 "MRK.16.15": "Und{1} [er hät]{2} [zu ine]{3} [gseit]{2}: «[Gönd]{4} [i]{5} [di ganz]{6,8} [Wält]{7} und [verchünded]{9} [s Evangelium]{10,11} [de ganze]{12,13} [Schöpfig]{14}.",
 "MRK.16.16": "[Wär]{1} [glaubt]{2} und{3} [tauft wird]{4}, [wird grettet]{5}; [wär]{6} [aber]{7} [nöd glaubt]{8}, [wird verurteilt]{9}.",
 "MRK.16.17": "[Die]{5} [Zeiche]{1} [aber]{2} [wärded]{6} [dene]{3} [folge]{6}, [wo glaubed]{4}: [I]{7} [mim]{10} [Name]{8,9} [wärded si]{12} [Dämone]{11} [ustriibe]{12}, [i nöie]{15} [Spraache]{13} [rede]{14},",
 "MRK.16.18": "[Schlange]{1} [wärded si ufnää]{2}, [und wänn]{3} [si]{6} [öppis]{5} [Tödlichs]{4} [trinked]{6}, [wird s]{10} [ine]{9} [sicher nöd]{7,8} [schade]{10}; [Chranke]{11,12} [wärded si]{14} [d Händ]{13} [uflege]{14}, und{15} [die wärded gsund]{16,17}.»",
 "MRK.16.19": "[De Herr]{1,4} [Jesus]{5} [also]{2,3}, [nachdem er]{6,7} [zu ine]{9} [gredt hät]{8}, [isch]{10} [in]{11} [Himmel]{12,13} [ufgnoo worde]{10} und{14} [hät sich]{15} [zur]{16} [Rächte]{17} [vo Gott]{18,19} [gsetzt]{15}.",
 "MRK.16.20": "[Die]{1} [aber]{2} [sind uszoge]{3} und [händ]{4} [überall]{5} [verchündet]{4}; [de Herr]{6,7} [hät mitgschaffet]{8} und{9} [s Wort]{10,11} [bestätiget]{12} [dur]{13} [d]{14} [Zeiche]{16}, [wo dezue choo sind]{15}.⟧",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MRK.14.1", "das Fest der Ungesäuerten Brote", "adapted", "τὰ ἄζυμα", "die Ungesäuerten", ["die Mazzot"], "τὰ ἄζυμα («die ungesäuerten [Brote]») ist der Name des siebentägigen Festes, das an das Passa anschliesst ([[LEV.23.5]]–[[LEV.23.6]]); Markus nennt beides zusammen."),
 ("MRK.14.3", "aus reiner Narde", "interpretive", "νάρδου πιστικῆς", None, ["aus echter Narde", "aus Pistazien-Narde"], "πιστικός ist selten. Meist wird es als «echt, unverfälscht» verstanden (von πίστις); andere leiten es von einem Pflanzennamen ab. Die Bedeutung bleibt unsicher."),
 ("MRK.14.5", "Denare", "literal", "δηναρίων", None, None, "Ein Denar war der übliche Tageslohn eines Arbeiters (vgl. [[MAT.20.2]]); dreihundert Denare entsprechen also ungefähr dem Verdienst eines Jahres."),
 ("MRK.14.8", "Was sie konnte", "adapted", "ὃ ἔσχεν", "Was sie hatte", None, "ἔχω mit Infinitiv-Sinn: «was sie vermochte»."),
 ("MRK.14.10", "auszuliefern", "literal", "παραδοῖ", None, ["zu verraten"], "παραδίδωμι heisst «übergeben, ausliefern». Dasselbe Verb steht für Judas, für die Hohepriester ([[MRK.15.1]], [[MRK.15.10]]), für Pilatus ([[MRK.15.15]]) und in den Leidensansagen ([[MRK.9.31]], [[MRK.10.33]]). «Ausliefern» hält diese Kette sichtbar; «verraten» ist die vertraute Wiedergabe bei Judas."),
 ("MRK.14.12", "das Passalamm", "interpretive", "τὸ πάσχα ἔθυον", "das Passa opferten", ["das Passa schlachtete"], "πάσχα bezeichnet das Fest, das Mahl und das Lamm. Mit θύω («schlachten, opfern») ist das Lamm gemeint (vgl. [[EXO.12.6]])."),
 ("MRK.14.15", "Obersaal", "literal", "ἀνάγαιον", None, ["Raum im Obergeschoss"], "ἀνάγαιον ist ein Raum im oberen Stockwerk."),
 ("MRK.14.21", "der Menschensohn", "traditional", "υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", ["der Mensch"], "«Sohn eines Menschen» heisst hebräisch und aramäisch einfach «Mensch». Bei Jesus ist es eine Selbstbezeichnung, oft mit Anklang an [[DAN.7.13]] (ausdrücklich in [[MRK.14.62]]). Ob die Wendung schon als Titel verstanden wurde, ist umstritten. Ebenso [[MRK.14.41]] und [[MRK.14.62]]."),
 ("MRK.14.22", "sprach den Lobpreis", "interpretive", "εὐλογήσας", "segnete", ["sprach den Segen", "dankte"], "εὐλογέω entspricht dem jüdischen Tischsegen, der Gott über dem Brot preist. Ein Objekt fehlt; ob Gott gepriesen oder das Brot gesegnet wird, sagt der Text nicht ausdrücklich. Beim Becher steht εὐχαριστέω «danken» ([[MRK.14.23]])."),
 ("MRK.14.22", "Das ist mein Leib", "literal", "τοῦτό ἐστιν τὸ σῶμά μου", None, None, "Wörtlich belassen. Wie das «ist» zu verstehen ist (Gleichsetzung, Zeichen, Vergegenwärtigung), beantworten die kirchlichen Lehrtraditionen unterschiedlich; die Übersetzung entscheidet das nicht."),
 ("MRK.14.24", "mein Blut des Bundes", "literal", "αἷμά μου τῆς διαθήκης", None, ["mein Bundesblut"], "Nimmt das «Blut des Bundes» vom Sinai auf ([[EXO.24.8]]). διαθήκη ist hier «Bund», Gottes verbindliche Zusage und Ordnung, nicht «Testament» im Sinn eines letzten Willens, obwohl das Wort im Griechischen auch das heissen kann. Das Wort «neu» (vgl. [[JER.31.31]]) steht im SBLGNT nicht; siehe Alternative."),
 ("MRK.14.24", "für viele", "literal", "ὑπὲρ πολλῶν", None, ["für alle"], "«Viele» kann im semitischen Sprachgebrauch die unzählbar Vielen im Gegenüber zu dem Einen meinen (vgl. [[ISA.53.12]], [[MRK.10.45]]) und ist dann keine Einschränkung. Beide Deutungen werden vertreten."),
 ("MRK.14.24", "vergossen wird", "literal", "ἐκχυννόμενον", None, ["vergossen werden wird"], "Partizip Präsens; der Bezug auf den kommenden Tod ergibt sich aus dem Zusammenhang."),
 ("MRK.14.25", "Reich Gottes", "traditional", "βασιλείᾳ τοῦ θεοῦ", None, ["Herrschaft Gottes", "Königreich Gottes"], "βασιλεία meint zuerst die Königsherrschaft Gottes, dann auch den Bereich, in dem sie gilt."),
 ("MRK.14.26", "nachdem sie den Lobgesang gesungen hatten", "interpretive", "ὑμνήσαντες", "nachdem sie gesungen hatten", None, "Nach späterer jüdischer Überlieferung wurden am Passamahl die Hallel-Psalmen ([[PSA.113.1]]–[[PSA.118.29]]) gesungen. Ob genau diese gemeint sind, sagt der Text nicht."),
 ("MRK.14.27", "zu Fall kommen", "interpretive", "σκανδαλισθήσεσθε", None, ["Anstoss nehmen", "irrewerden", "abfallen"], "σκανδαλίζομαι: über ein Hindernis stolpern, im Glauben zu Fall kommen. Das Zitat ist [[ZEC.13.7]]."),
 ("MRK.14.28", "auferweckt worden bin", "literal", "ἐγερθῆναί", None, ["auferstanden bin"], "Passiv von ἐγείρω «aufwecken»: Gott ist der Handelnde. Ebenso [[MRK.16.6]]; im längeren Schluss steht dagegen ἀναστάς «auferstanden» ([[MRK.16.9]])."),
 ("MRK.14.30", "ein Hahn zweimal kräht", "literal", "δὶς ἀλέκτορα φωνῆσαι", None, None, "Nur Markus spricht von zweimaligem Krähen (vgl. [[MRK.14.72]]); [[MAT.26.34]] nennt einen Hahnenschrei."),
 ("MRK.14.33", "sich zu entsetzen", "literal", "ἐκθαμβεῖσθαι", None, ["zu erschrecken", "zu erschauern"], "Dasselbe Verb steht für die Frauen im Grab ([[MRK.16.5]], [[MRK.16.6]]) und ist dort ebenso wiedergegeben."),
 ("MRK.14.34", "Tief betrübt ist meine Seele", "literal", "Περίλυπός ἐστιν ἡ ψυχή μου", None, ["Ich bin zu Tode betrübt"], "Klingt an die Klage in [[PSA.42.5]] an. ψυχή meint hier das Innere, das ganze Selbst."),
 ("MRK.14.36", "Abba, Vater", "literal", "Αββα ὁ πατήρ", None, None, "Αββα gibt das aramäische ʾabbāʾ «Vater» wieder; Markus fügt die griechische Übersetzung an (so auch [[ROM.8.15]], [[GAL.4.6]]). Die verbreitete Deutung als kindliches «Papa» ist umstritten; die Form war auch unter Erwachsenen gebräuchlich. Der Nominativ ὁ πατήρ steht für die Anrede."),
 ("MRK.14.36", "Becher", "literal", "ποτήριον", None, ["Kelch"], "Der Becher ist ein Bild für das zugemessene Geschick, in der Schrift auch für Gottes Gericht (vgl. [[ISA.51.17]], [[MRK.10.38]])."),
 ("MRK.14.38", "Versuchung", "interpretive", "πειρασμόν", None, ["Prüfung", "Anfechtung"], "πειρασμός heisst «Versuchung» und «Prüfung» (vgl. das Vaterunser, [[MAT.6.13]])."),
 ("MRK.14.38", "Fleisch", "literal", "σὰρξ", None, ["der Mensch", "die Natur"], "σάρξ steht hier für den schwachen, sterblichen Menschen, nicht für Sünde."),
 ("MRK.14.41", "Es ist genug", "interpretive", "ἀπέχει", None, ["Es ist entschieden", "Er hat (den Lohn) erhalten", "Es ist so weit"], "Die Bedeutung von ἀπέχει ist hier unsicher. Vorgeschlagen werden «es ist genug», «es ist entschieden» und, auf Judas bezogen, «er hat (das Geld) erhalten»."),
 ("MRK.14.43", "Knüppeln", "literal", "ξύλων", "Hölzern", ["Stöcken"], None),
 ("MRK.14.47", "Knecht", "traditional", "δοῦλον", "Sklaven", ["Diener"], None),
 ("MRK.14.48", "Räuber", "interpretive", "λῃστὴν", None, ["Banditen", "Aufständischen"], "λῃστής bezeichnet im 1. Jahrhundert oft bewaffnete Banden und Aufständische, nicht nur Diebe. Dasselbe Wort steht für die beiden Mitgekreuzigten ([[MRK.15.27]])."),
 ("MRK.14.49", "Aber es geschieht, damit", "adapted", "ἀλλʼ ἵνα", "Aber damit", None, "Der griechische Satz ist verkürzt; «es geschieht» ist ergänzt."),
 ("MRK.14.51", "ein junger Mann", "literal", "νεανίσκος", None, None, "Dasselbe Wort steht für den Boten im Grab ([[MRK.16.5]]). Wer der junge Mann war, sagt der Text nicht; die Vermutung, es sei Markus selbst, lässt sich nicht belegen."),
 ("MRK.14.54", "Feuer", "adapted", "φῶς", "Licht", ["Feuerschein"], "Gemeint ist das Feuer, an dem man sich wärmt."),
 ("MRK.14.55", "Hohe Rat", "traditional", "συνέδριον", None, ["Synedrium", "Ratsversammlung"], "Das jüdische Ratsgremium in Jerusalem unter Vorsitz des Hohepriesters."),
 ("MRK.14.58", "Tempel", "literal", "ναὸν", None, ["Tempelhaus"], "ναός ist das Tempelhaus, das Heiligtum; ἱερόν ([[MRK.14.49]]) ist der ganze Tempelbezirk. ναός steht auch in [[MRK.15.29]] und [[MRK.15.38]]."),
 ("MRK.14.61", "der Christus", "traditional", "χριστὸς", None, ["der Messias", "der Gesalbte"], "χριστός übersetzt hebräisch māšîaḥ «Gesalbter». Ebenso [[MRK.15.32]]."),
 ("MRK.14.61", "des Hochgelobten", "literal", "εὐλογητοῦ", None, None, "Ehrfürchtige Umschreibung für Gott."),
 ("MRK.14.62", "Ich bin es", "interpretive", "Ἐγώ εἰμι", "Ich bin", ["Ja, ich bin es"], "Als Antwort auf die Frage heisst ἐγώ εἰμι «ich bin es», also «ja». Dieselben Worte stehen in der griechischen Bibel für Gottes Selbstvorstellung (vgl. [[EXO.3.14]], [[ISA.43.10]]); ob Markus diesen Anklang beabsichtigt (vgl. [[MRK.6.50]]), ist umstritten."),
 ("MRK.14.62", "zur Rechten der Macht", "literal", "δεξιῶν δυνάμεως", None, ["zur Rechten Gottes"], "«Die Macht» umschreibt Gott. Jesus verbindet [[PSA.110.1]] und [[DAN.7.13]]."),
 ("MRK.14.64", "Lästerung", "literal", "βλασφημίας", None, ["Gotteslästerung"], "Wie in [[MRK.3.28]]."),
 ("MRK.14.70", "deine Sprechweise passt dazu", "literal", "ἡ λαλιά σου ὁμοιάζει", "deine Rede ist ähnlich", ["deine Aussprache verrät dich"], "Steht im Token-Text des SBLGNT; laut SBLGNT-Apparat lassen WH, Treg und NA28 die Worte weg (siehe Alternative)."),
 ("MRK.14.71", "sich zu verfluchen", "interpretive", "ἀναθεματίζειν", None, ["zu fluchen", "ihn (Jesus) zu verfluchen"], "Das Verb hat kein Objekt. Gemeint sein kann eine Selbstverfluchung für den Fall, dass er lügt, oder eine Verfluchung Jesu."),
 ("MRK.14.72", "er dachte daran", "interpretive", "ἐπιβαλὼν", None, ["er brach in Tränen aus", "er stürzte hinaus", "er verhüllte sich"], "Die Bedeutung von ἐπιβαλών ist hier unsicher; die Vorschläge reichen von «darüber nachdenkend» bis «hinausstürzend»."),
 ("MRK.15.1", "lieferten ihn", "literal", "παρέδωκαν", None, ["übergaben ihn"], "Wie in [[MRK.14.10]]: παραδίδωμι durchgehend «ausliefern»."),
 ("MRK.15.2", "Du sagst es", "literal", "Σὺ λέγεις", None, ["Das sagst du"], "Eine zurückhaltende Antwort; ob sie eher Zustimmung oder Abstand ausdrückt, wird verschieden gedeutet."),
 ("MRK.15.15", "zufriedenstellen", "adapted", "τὸ ἱκανὸν ποιῆσαι", "das Genügende tun", None, "Entspricht der lateinischen Wendung satisfacere."),
 ("MRK.15.15", "liess er geisseln", "literal", "φραγελλώσας", None, None, "Lateinisches Lehnwort (flagellum «Geissel»). Die Geisselung ging der Kreuzigung voraus."),
 ("MRK.15.16", "Kohorte", "literal", "σπεῖραν", None, ["Truppe"], "Eine römische Einheit von mehreren hundert Mann (nominell ein Zehntel einer Legion); hier wohl die anwesende Truppe."),
 ("MRK.15.17", "Purpurmantel", "interpretive", "πορφύραν", "Purpur", ["Purpurgewand"], "Ein purpurfarbenes Kleidungsstück als Zeichen königlicher Würde, hier zum Spott."),
 ("MRK.15.21", "sie zwingen", "literal", "ἀγγαρεύουσιν", None, ["sie verpflichten"], "ἀγγαρεύω ist das Wort für die Dienstverpflichtung durch Soldaten oder Beamte (vgl. [[MAT.5.41]])."),
 ("MRK.15.22", "Golgota", "literal", "Γολγοθᾶν", None, None, "Griechische Umschrift des aramäischen gulgultāʾ «Schädel»; Markus übersetzt selbst."),
 ("MRK.15.23", "sie wollten", "interpretive", "ἐδίδουν", "sie gaben", ["sie boten an"], "Das Imperfekt beschreibt hier einen Versuch, weil er nicht trank."),
 ("MRK.15.24", "werfen das Los darüber", "literal", "βάλλοντες κλῆρον", None, None, "Klingt an [[PSA.22.18]] an."),
 ("MRK.15.25", "die dritte Stunde", "literal", "ὥρα τρίτη", None, ["neun Uhr"], "Die Stunden wurden ab Sonnenaufgang gezählt: etwa neun Uhr morgens. [[JHN.19.14]] nennt für die Verurteilung die sechste Stunde; der Unterschied wird verschieden erklärt."),
 ("MRK.15.29", "Ha", "adapted", "Οὐὰ", None, ["Pah", "Ei"], "Spöttischer Ausruf."),
 ("MRK.15.33", "Land", "interpretive", "γῆν", None, ["Erde"], "γῆ kann das Land (Judäa) oder die ganze Erde meinen."),
 ("MRK.15.34", "Eloi, Eloi, lema sabachthani", "literal", "Ἐλωῒ ἐλωῒ λεμὰ σαβαχθάνι", None, None, "Aramäisch, in griechischen Buchstaben: ʾelāhî ʾelāhî lǝmā šǝbaqtanî. Es ist der Anfang von [[PSA.22.1]] (hebräisch ʾēlî ʾēlî lāmâ ʿăzabtānî). Markus übersetzt selbst. Die Handschriften schreiben die Wörter unterschiedlich (siehe Alternative)."),
 ("MRK.15.34", "wozu", "literal", "εἰς τί", None, ["warum"], "εἰς τί fragt nach dem Zweck: «wozu, wofür»."),
 ("MRK.15.36", "Essig", "traditional", "ὄξους", None, ["sauren Wein"], "Billiger, saurer Wein, ein übliches Getränk von Soldaten; klingt an [[PSA.69.21]] an."),
 ("MRK.15.37", "verschied", "traditional", "ἐξέπνευσεν", "hauchte aus", ["starb"], None),
 ("MRK.15.38", "riss entzwei", "interpretive", "ἐσχίσθη", "wurde zerrissen", None, "Passiv. Dasselbe Verb steht bei der Taufe: die Himmel «reissen auf» ([[MRK.1.10]]). Welcher Vorhang gemeint ist (vor dem Allerheiligsten oder am Eingang des Tempelhauses), sagt Markus nicht."),
 ("MRK.15.39", "Hauptmann", "traditional", "κεντυρίων", None, ["Zenturio"], "Lateinisches Lehnwort (centurio): Offizier über eine Hundertschaft."),
 ("MRK.15.39", "Gottes Sohn", "interpretive", "υἱὸς θεοῦ", None, ["der Sohn Gottes", "ein Sohn Gottes", "ein Gottessohn"], "υἱὸς θεοῦ steht ohne Artikel. Grammatisch ist «ein Sohn Gottes» möglich (im Mund eines römischen Soldaten etwa: ein göttlicher Mensch) wie auch «der Sohn Gottes», weil ein vorangestelltes Prädikatsnomen oft ohne Artikel steht. Im Erzählganzen nimmt der Satz [[MRK.1.1]] und [[MRK.1.11]] auf. «Gottes Sohn» lässt beides offen; redaktionelle Entscheidung."),
 ("MRK.15.40", "Maria aus Magdala", "interpretive", "Μαρία ἡ Μαγδαληνὴ", "Maria, die Magdalenerin", ["Maria Magdalena"], "Herkunftsbezeichnung nach dem Ort Magdala am See Gennesaret. Ebenso [[MRK.15.47]], [[MRK.16.1]], [[MRK.16.9]]."),
 ("MRK.15.41", "gedient hatten", "literal", "διηκόνουν", None, ["für ihn gesorgt hatten", "ihn unterstützt hatten"], "διακονέω umfasst Bewirtung, Versorgung und Unterstützung."),
 ("MRK.15.42", "Rüsttag", "literal", "παρασκευή", "Vorbereitung", ["Freitag"], "Der Tag der Vorbereitung auf den Sabbat; Markus erklärt es selbst."),
 ("MRK.15.43", "Ratsmitglied", "interpretive", "βουλευτής", None, ["Ratsherr"], "Wohl Mitglied des Hohen Rates."),
 ("MRK.15.47", "die Mutter des Joses", "interpretive", "ἡ Ἰωσῆτος", "die des Joses", None, "«Mutter» ist ergänzt, nach [[MRK.15.40]]. Ebenso «Mutter des Jakobus» in [[MRK.16.1]]."),
 ("MRK.16.2", "am ersten Tag der Woche", "literal", "μιᾷ τῶν σαββάτων", "am ersten der Sabbate", None, "σάββατα heisst auch «Woche»; gemeint ist der Tag nach dem Sabbat."),
 ("MRK.16.5", "einen jungen Mann", "literal", "νεανίσκον", None, ["einen Engel"], "Der Text nennt ihn nicht Engel; das weisse Gewand deutet auf einen himmlischen Boten (vgl. [[MAT.28.2]]). Dasselbe Wort wie in [[MRK.14.51]]."),
 ("MRK.16.6", "Er ist auferweckt worden", "literal", "ἠγέρθη", None, ["Er ist auferstanden"], "Passiv wie in [[MRK.14.28]]."),
 ("MRK.16.8", "sie fürchteten sich nämlich", "literal", "ἐφοβοῦντο γάρ", None, ["denn sie fürchteten sich"], "In den CNTR-Transkriptionen der Handschriften 01 und 03 endet das Evangelium mit diesem Satz. Ein Text, der mit γάρ («nämlich, denn») schliesst, ist ungewöhnlich, kommt aber vor. Ob Markus so schliessen wollte, ob ein ursprünglicher Schluss verloren ging oder ob das Werk unvollendet blieb, ist umstritten. φοβέομαι kann Angst wie Ehrfurcht vor Gott bezeichnen. Die Übersetzung lässt den Satz offen stehen."),
 ("MRK.16.8", "⟦Alles aber", "literal", "Πάντα δὲ", None, None, "Hier beginnt der sogenannte kürzere Markusschluss (Tokens 19–52 von [[MRK.16.8]]). Der SBLGNT setzt ihn in Doppelklammern ⟦ ⟧ und weist ihn damit als spätere Ergänzung aus; die Übersetzung übernimmt die Klammern. In keiner der im Projekt erfassten CNTR-Transkriptionen (01, 02, 03, 04, 05, 032) steht er. Wortschatz und Stil («die heilige und unvergängliche Botschaft vom ewigen Heil») unterscheiden sich deutlich vom übrigen Markus."),
 ("MRK.16.9", "⟦Nachdem er aber", "literal", "Ἀναστὰς δὲ", None, None, "Hier beginnt der längere Markusschluss ([[MRK.16.9]]–[[MRK.16.20]]), im SBLGNT in Doppelklammern ⟦ ⟧ als spätere Ergänzung ausgewiesen; die Übersetzung übernimmt die Klammern. In den CNTR-Transkriptionen von 01 (Codex Sinaiticus) und 03 (Codex Vaticanus) endet der Text mit [[MRK.16.8]]; für 16,9–20 ist dort kein Text erfasst. In 02, 04 und 032 steht der Abschnitt, in 05 nach der Transkription bis 16,15. Im Text selbst fällt auf: Maria aus Magdala wird neu vorgestellt, obwohl sie in [[MRK.16.1]] schon genannt ist, und statt ἠγέρθη ([[MRK.16.6]]) steht ἀναστάς. Der Abschnitt fasst Erscheinungen zusammen, die andere Evangelien ausführlicher erzählen (vgl. [[LUK.24.13]]–[[LUK.24.35]], [[JHN.20.11]]–[[JHN.20.18]]). Viele Kirchen haben ihn als Teil der Heiligen Schrift überliefert und anerkannt; die Frage seiner Herkunft ist davon zu unterscheiden."),
 ("MRK.16.12", "offenbarte er sich", "literal", "ἐφανερώθη", "wurde er offenbart", ["erschien er"], None),
 ("MRK.16.14", "Herzenshärte", "literal", "σκληροκαρδίαν", None, ["Verstocktheit"], None),
 ("MRK.16.17", "in neuen Sprachen", "interpretive", "γλώσσαις καιναῖς", "in neuen Zungen", ["in fremden Sprachen"], "γλῶσσα heisst «Zunge» und «Sprache» (vgl. [[ACT.2.4]], [[1CO.14.2]])."),
]

DEC_GSW = [
 ("MRK.14.1", "s Fäscht vo de ungsüürete Broot", "adapted", "τὰ ἄζυμα", "di Ungsüürete", None, "Name vom siebetägige Fäscht, wo as Passa aaschlüsst ([[LEV.23.5]]–[[LEV.23.6]])."),
 ("MRK.14.10", "uslifere", "literal", "παραδοῖ", None, ["verrate"], "παραδίδωμι heisst «übergää, uslifere». Es staat für de Judas, für d Hoheprieschter ([[MRK.15.1]]) und für de Pilatus ([[MRK.15.15]]); drum überall «uslifere»."),
 ("MRK.14.21", "de Mänschesohn", "traditional", "υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", ["de Mänsch"], "«Sohn vo me Mänsch» heisst hebräisch und aramäisch eifach «Mänsch»; bim Jesus e Bezeichnig für sich sälber, mit Aaklang a [[DAN.7.13]]."),
 ("MRK.14.22", "hät de Lobpriis gsproche", "interpretive", "εὐλογήσας", "hät gsägnet", ["hät dankt"], "Wie bim jüdische Tischsäge: Gott wird über em Broot globt."),
 ("MRK.14.22", "Das isch min Liib", "literal", "τοῦτό ἐστιν τὸ σῶμά μου", None, None, "Wörtlich bhalte. Wie s «isch» z verstaa isch, beantwortet di kirchliche Lehrtraditione verschide; d Übersetzig entscheidet das nöd."),
 ("MRK.14.24", "mis Bluet vom Bund", "literal", "αἷμά μου τῆς διαθήκης", None, None, "Nimmt s «Bluet vom Bund» vom Sinai uf ([[EXO.24.8]]). διαθήκη isch da «Bund», nöd «Teschtament». «Nöi» staat im SBLGNT nöd; lueg d Alternative."),
 ("MRK.14.24", "für vili", "literal", "ὑπὲρ πολλῶν", None, ["für alli"], "«Vili» cha di unzellbar Vile meine (vgl. [[ISA.53.12]], [[MRK.10.45]]) und isch dänn kei Iischränkig."),
 ("MRK.14.25", "Riich vo Gott", "traditional", "βασιλείᾳ τοῦ θεοῦ", None, ["Herrschaft vo Gott"], None),
 ("MRK.14.27", "z Fall choo", "interpretive", "σκανδαλισθήσεσθε", None, ["Aastoss nää"], "Zitat us [[ZEC.13.7]]."),
 ("MRK.14.28", "uferweckt worde bi", "literal", "ἐγερθῆναί", None, ["uferstande bi"], "Passiv: Gott weckt uf. Gliich i [[MRK.16.6]]."),
 ("MRK.14.30", "en Güggel", "adapted", "ἀλέκτορα", "en Hahn", None, None),
 ("MRK.14.36", "Abba, Vatter", "literal", "Αββα ὁ πατήρ", None, None, "Αββα isch aramäisch ʾabbāʾ «Vatter»; de Markus setzt d griechisch Übersetzig dezue (vgl. [[ROM.8.15]], [[GAL.4.6]]). Dass es es chindlichs «Papi» sig, isch umstritte."),
 ("MRK.14.38", "Versuechig", "interpretive", "πειρασμόν", None, ["Prüefig"], None),
 ("MRK.14.41", "Es isch gnueg", "interpretive", "ἀπέχει", None, ["Es isch entschide", "Er hät de Lohn übercho"], "D Bedüütig vo ἀπέχει isch da unsicher."),
 ("MRK.14.48", "en Röiber", "interpretive", "λῃστὴν", None, ["en Bandit", "en Ufständische"], "λῃστής sind oft bewaffneti Bande oder Ufständischi gsii; s gliich Wort staat für di zwei Mitgchrüüzigte ([[MRK.15.27]])."),
 ("MRK.14.61", "de Christus", "traditional", "χριστὸς", None, ["de Messias", "de Gsalbet"], None),
 ("MRK.14.62", "Ich bi s", "interpretive", "Ἐγώ εἰμι", "Ich bi", None, "Als Antwort heisst ἐγώ εἰμι «ich bi s», also «ja». Di gliiche Wort stönd i de griechische Bible für Gott, wo sich vorstellt ([[EXO.3.14]]); öb de Markus das aaklinge laat, isch umstritte."),
 ("MRK.14.64", "Er häig de Tod verdient", "adapted", "ἔνοχον εἶναι θανάτου", "er sig schuldig vom Tod", None, "D Mundart hät kei Genitiv; de Sinn isch: er mües stärbe."),
 ("MRK.14.70", "dini Spraach passt dezue", "literal", "ἡ λαλιά σου ὁμοιάζει", None, None, "Staat im Token-Text vom SBLGNT; WH, Treg und NA28 lönd s wäg (lueg d Alternative)."),
 ("MRK.14.71", "sich z verflueche", "interpretive", "ἀναθεματίζειν", None, ["en (de Jesus) z verflueche"], "S Verb hät keis Objekt."),
 ("MRK.14.72", "er hät dra dänkt", "interpretive", "ἐπιβαλὼν", None, ["er isch in Träne usbroche"], "D Bedüütig vo ἐπιβαλών isch unsicher."),
 ("MRK.15.2", "Du seisch es", "literal", "Σὺ λέγεις", None, None, None),
 ("MRK.15.34", "Eloi, Eloi, lema sabachthani", "literal", "Ἐλωῒ ἐλωῒ λεμὰ σαβαχθάνι", None, None, "Aramäisch: ʾelāhî ʾelāhî lǝmā šǝbaqtanî, de Aafang vo [[PSA.22.1]]. De Markus übersetzt sälber."),
 ("MRK.15.34", "für was", "literal", "εἰς τί", "wozue", ["werum"], "εἰς τί fröget nach em Zwäck."),
 ("MRK.15.39", "Gottes Sohn", "interpretive", "υἱὸς θεοῦ", None, ["de Sohn vo Gott", "en Sohn vo Gott"], "Ohni Artikel: «en Sohn vo Gott» und «de Sohn vo Gott» sind beidi möglich. Im Ganze nimmt de Satz [[MRK.1.1]] und [[MRK.1.11]] uf. «Gottes Sohn» laat beides offe; redaktionelle Entscheid."),
 ("MRK.15.40", "d Maria vo Magdala", "interpretive", "Μαρία ἡ Μαγδαληνὴ", "d Maria, d Magdalenerin", ["d Maria Magdalena"], None),
 ("MRK.16.2", "am erschte Tag", "literal", "μιᾷ", None, None, "σάββατα heisst au «Wuche»."),
 ("MRK.16.8", "si händ sich nämli gfürchtet", "literal", "ἐφοβοῦντο γάρ", None, None, "I de CNTR-Transkriptione vo de Handschrifte 01 und 03 hört s Evangelium mit dem Satz uf. Öb de Markus so hät wele schlüüsse, öb en ursprüngliche Schluss verlore gange isch oder öb s Wärch nöd fertig worde isch, isch umstritte."),
 ("MRK.16.8", "⟦Alles aber", "literal", "Πάντα δὲ", None, None, "Da faat de sogenannt chürzer Markusschluss aa. De SBLGNT setzt en i Doppelklammere ⟦ ⟧ als spööteri Ergänzig; d Übersetzig übernimmt d Klammere. I keinere vo de erfasste CNTR-Transkriptione (01, 02, 03, 04, 05, 032) staat er."),
 ("MRK.16.9", "⟦Nachdem er aber", "literal", "Ἀναστὰς δὲ", None, None, "Da faat de länger Markusschluss aa ([[MRK.16.9]]–[[MRK.16.20]]), im SBLGNT i Doppelklammere ⟦ ⟧ als spööteri Ergänzig. I de CNTR-Transkriptione vo 01 und 03 hört de Text mit [[MRK.16.8]] uf; in 02, 04 und 032 staat de Abschnitt, in 05 bis 16,15. Vili Chile händ en als Teil vo de Heilige Schrift überliferet; d Frag nach sinere Herkunft isch devo z underscheide."),
 ("MRK.16.17", "i nöie Spraache", "interpretive", "γλώσσαις καιναῖς", "i nöie Zunge", None, None),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-MRK-014-019-02:R2", "MRK.14.19", "«Doch nicht ich?»", "«Doch nicht ich?» Und ein anderer: «Doch nicht ich?»",
  "«Doch nöd ich?»", "«Doch nöd ich?» Und en andere: «Doch nöd ich?»", "gering",
  "Die Frage wird wiederholt und einem zweiten Jünger in den Mund gelegt.", "D Frag wird widerholt und eme zweite Jünger in Mund gleit.",
  {"R1": [("Μήτι ἐγώ", "Doch nicht ich?", None)], "R2": [("Μήτι ἐγώ; Καὶ ἄλλος· Μήτι ἐγώ", "Doch nicht ich? Und ein anderer: Doch nicht ich?", "mit Wiederholung")]},
  {"R1": [("Μήτι ἐγώ", "Doch nöd ich?", None)], "R2": [("Μήτι ἐγώ; Καὶ ἄλλος· Μήτι ἐγώ", "Doch nöd ich? Und en andere: Doch nöd ich?", "mit Widerholig")]},
  ["Die Wiederholung kann die Szene ausmalen; sie kann aber auch beim Abschreiben ausgefallen sein, weil zweimal dieselben Worte stehen.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 032 ohne die Wiederholung, 02 und 05 mit ihr; 04 hat hier ἕκαστος statt καθʼ εἷς und ebenfalls keine Wiederholung."],
  ["D Widerholig cha d Szene usmale; si cha aber au bim Abschriibe usgfalle sii, wil zweimal di gliiche Wort stönd.",
   "Nach de automatische Zueornig läsed 01, 03 und 032 ohni Widerholig, 02 und 05 mit; 04 hät da ἕκαστος statt καθʼ εἷς und au kei Widerholig."]),
 ("VAR-SBLGNTAPP-MRK-014-022-02:R2", "MRK.14.22", "«Nehmt!", "«Nehmt, esst!", "«Nämed!", "«Nämed, ässed!", "gering",
  "Mit «esst» wird die Aufforderung ausdrücklich.", "Mit «ässed» wird d Ufforderig usdrücklich.",
  {"R1": [("Λάβετε", "Nehmt", None)], "R2": [("Λάβετε φάγετε", "Nehmt, esst", "mit Zusatz")]},
  {"R1": [("Λάβετε", "Nämed", None)], "R2": [("Λάβετε φάγετε", "Nämed, ässed", "mit Zuesatz")]},
  ["Der Zusatz entspricht dem Wortlaut in [[MAT.26.26]]; Abschreiber haben Paralleltexte oft angeglichen.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 04, 05 und 032 ohne «esst»; den Zusatz haben unter den erfassten Texten nur die gedruckten Ausgaben KJTR, RP und Stephanus."],
  ["De Zuesatz entspricht em Wortlut i [[MAT.26.26]]; Abschriiber händ Paralleltext oft aaglichen.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 04, 05 und 032 ohni «ässed»; de Zuesatz händ under de erfasste Text nu di druckte Usgabe KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-MRK-014-024-01:R3", "MRK.14.24", "mein Blut des Bundes", "mein Blut, das des neuen Bundes", "mis Bluet vom Bund", "mis Bluet vom nöie Bund", "mittel",
  "Der Becher wird ausdrücklich mit dem «neuen Bund» verbunden.", "De Bächer wird usdrücklich mit em «nöie Bund» verbunde.",
  {"R1": [("τῆς διαθήκης", "des Bundes", None)], "R2": [("τὸ τῆς διαθήκης", "das des Bundes", "mit Artikel")], "R3": [("τὸ τῆς καινῆς διαθήκης", "das des neuen Bundes", "mit «neu»")]},
  {"R1": [("τῆς διαθήκης", "vom Bund", None)], "R2": [("τὸ τῆς διαθήκης", "das vom Bund", "mit Artikel")], "R3": [("τὸ τῆς καινῆς διαθήκης", "das vom nöie Bund", "mit «nöi»")]},
  ["«Neu» kann aus [[LUK.22.20]] und [[1CO.11.25]] übernommen sein, wo der «neue Bund» ([[JER.31.31]]) steht; die Abschreiber haben die Abendmahlsworte einander angeglichen.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 «des Bundes»; 05 und 032 haben den Artikel (R2), 02 «des neuen Bundes» (R3)."],
  ["«Nöi» cha us [[LUK.22.20]] und [[1CO.11.25]] übernoo sii, wo de «nöi Bund» ([[JER.31.31]]) staat.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 «vom Bund»; 05 und 032 händ de Artikel (R2), 02 «vom nöie Bund» (R3)."]),
 ("VAR-SBLGNTAPP-MRK-014-027-01:R2", "MRK.14.27", "Ihr werdet alle zu Fall kommen", "Ihr werdet alle an mir zu Fall kommen in dieser Nacht",
  "Ir wärded alli z Fall choo", "Ir wärded alli wäge mir z Fall choo i dere Nacht", "gering",
  "Der Zusatz nennt Anlass und Zeitpunkt.", "De Zuesatz nännt Aalass und Ziitpunkt.",
  {"R1": [("σκανδαλισθήσεσθε", "ihr werdet zu Fall kommen", None)], "R2": [("σκανδαλισθήσεσθε ἐν ἐμοὶ ἐν τῇ νυκτὶ ταύτῃ", "ihr werdet an mir zu Fall kommen in dieser Nacht", "mit Zusatz")]},
  {"R1": [("σκανδαλισθήσεσθε", "ir wärded z Fall choo", None)], "R2": [("σκανδαλισθήσεσθε ἐν ἐμοὶ ἐν τῇ νυκτὶ ταύτῃ", "ir wärded wäge mir z Fall choo i dere Nacht", "mit Zuesatz")]},
  ["Der Zusatz entspricht [[MAT.26.31]] und kann von dort übernommen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 ohne Zusatz, 02 und 032 (Erstschrift und Korrektur) mit ihm; 05 weicht anders ab."],
  ["De Zuesatz entspricht [[MAT.26.31]] und cha vo det übernoo sii.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 ohni Zuesatz, 02 und 032 mit; 05 weicht anders ab."]),
 ("VAR-SBLGNTAPP-MRK-014-065-02:R2", "MRK.14.65", "nahmen ihn mit Schlägen in Empfang", "schlugen mit Schlägen auf ihn ein",
  "händ en mit Schleeg in Empfang gnoo", "händ mit Schleeg uf en ii gschlage", "gering",
  "ἔβαλλον («sie warfen, schlugen») statt ἔλαβον («sie nahmen»).", "ἔβαλλον («si händ gschlage») statt ἔλαβον («si händ gnoo»).",
  {"R1": [("ἔλαβον", "nahmen", None)], "R2": [("ἔβαλλον", "schlugen", None)]},
  {"R1": [("ἔλαβον", "händ gnoo", None)], "R2": [("ἔβαλλον", "händ gschlage", None)]},
  ["Die beiden Wörter sehen sich im Schriftbild ähnlich; «schlugen» glättet die ungewöhnliche Wendung «mit Schlägen nehmen».",
   "Laut der automatischen Zuordnung lesen 01, 02, 03 und 04 ἔλαβον (in 03 und 04 ist die Stelle teils beschädigt); 05 und 032 haben ἐλάμβανον, eine andere Form desselben Verbs. ἔβαλλον haben unter den erfassten Texten die Ausgaben KJTR, RP und Stephanus."],
  ["Di beide Wörter gseend sich im Schriftbild ähnlich; «händ gschlage» glättet di ungwöhnlich Wändig.",
   "Nach de automatische Zueornig läsed 01, 02, 03 und 04 ἔλαβον; 05 und 032 händ ἐλάμβανον, en anderi Form vom gliiche Verb. ἔβαλλον händ di druckte Usgabe KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-MRK-014-068-02:R2", "MRK.14.68", "Vorhof; und ein Hahn krähte.", "Vorhof.", "Vorhof gange; und en Güggel hät gchräit.", "Vorhof gange.", "mittel",
  "Ohne den ersten Hahnenschrei hat das «zum zweiten Mal» in [[MRK.14.72]] keinen Bezug im Text.", "Ohni de erscht Güggelschrei hät s «zum zweite Mal» i [[MRK.14.72]] kei Bezug im Text.",
  {"R1": [("καὶ ἀλέκτωρ ἐφώνησεν", "und ein Hahn krähte", None)], "R2": [("–", "(fehlt)", "ohne Hahnenschrei")]},
  {"R1": [("καὶ ἀλέκτωρ ἐφώνησεν", "und en Güggel hät gchräit", None)], "R2": [("–", "(fehlt)", "ohni Güggelschrei")]},
  ["Der Satz kann ergänzt worden sein, damit das «zum zweiten Mal» ([[MRK.14.72]]) einen ersten Hahnenschrei hat; er kann auch weggelassen worden sein, um an die anderen Evangelien anzugleichen, die nur einen Hahnenschrei kennen.",
   "Laut der automatischen Zuordnung fehlt der Satz in 01 und 03; 02, 04 (beschädigt) und 05 haben ihn; 032 liest an dieser Stelle anders (εἰς τὴν ἔξω αὐλήν)."],
  ["De Satz cha ergänzt worde sii, demit s «zum zweite Mal» ([[MRK.14.72]]) en erschte Güggelschrei hät; er cha au wäggloo worde sii, zum a di andere Evangelie aazgliiche.",
   "Nach de automatische Zueornig fäält de Satz in 01 und 03; 02, 04 und 05 händ en; 032 lisst a dere Stell anders."]),
 ("VAR-SBLGNTAPP-MRK-014-070-01:R2", "MRK.14.70", "ein Galiläer, und deine Sprechweise passt dazu!", "ein Galiläer!", "en Galiläer, und dini Spraach passt dezue!", "en Galiläer!", "gering",
  "Ohne den Hinweis auf die Aussprache.", "Ohni de Hiiwiis uf d Uussprach.",
  {"R1": [("καὶ ἡ λαλιά σου ὁμοιάζει", "und deine Sprechweise passt dazu", "SBLGNT-Text; laut Apparat sonst nur RP")], "R2": [("–", "(fehlt)", "WH, Treg, NA28")]},
  {"R1": [("καὶ ἡ λαλιά σου ὁμοιάζει", "und dini Spraach passt dezue", "SBLGNT-Text")], "R2": [("–", "(fehlt)", "WH, Treg, NA28")]},
  ["Der Satz kann aus [[MAT.26.73]] («deine Sprache verrät dich») übernommen und angepasst sein; er kann auch ursprünglich sein und begründen, woran man Petrus als Galiläer erkennt.",
   "Laut der automatischen Zuordnung fehlt der Satz in 01, 03, 04 und 05; 02 hat ihn; 032 liest an dieser Stelle anders."],
  ["De Satz cha us [[MAT.26.73]] übernoo sii; er cha au ursprünglich sii und begründe, wora mer de Petrus als Galiläer erchännt.",
   "Nach de automatische Zueornig fäält de Satz in 01, 03, 04 und 05; 02 hät en."]),
 ("VAR-SBLGNTAPP-MRK-015-008-01:R2", "MRK.15.8", "zog hinauf", "schrie auf", "isch ufezoge", "hät ufbrüelet", "gering",
  "ἀναβοήσας («aufschreiend») statt ἀναβάς («hinaufsteigend»).", "ἀναβοήσας («ufbrüelend») statt ἀναβάς («ufestiigend»).",
  {"R1": [("ἀναβὰς", "hinaufgezogen", None)], "R2": [("ἀναβοήσας", "aufschreiend", None)]},
  {"R1": [("ἀναβὰς", "ufezoge", None)], "R2": [("ἀναβοήσας", "ufbrüelet", None)]},
  ["Die beiden Wörter sehen sich ähnlich; «aufschreien» passt zur lauten Menge in [[MRK.15.13]]–[[MRK.15.14]], «hinaufziehen» zum Palast des Statthalters.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ἀναβάς, 02, 04 und 032 ἀναβοήσας; 059 ist hier nicht erhalten."],
  ["Di beide Wörter gseend sich ähnlich; «ufbrüele» passt zur luute Mängi, «ufezie» zum Palascht.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ἀναβάς, 02, 04 und 032 ἀναβοήσας."]),
 ("VAR-SBLGNTAPP-MRK-015-027-01:R2", "MRK.15.27", "zu seiner Linken.", "zu seiner Linken. [28] Und die Schrift wurde erfüllt, die sagt: «Und er wurde zu den Gesetzlosen gerechnet.»",
  "linggs vo ihm.", "linggs vo ihm. [28] Und d Schrift isch erfüllt worde, wo seit: «Und er isch zu de Gsetzlose zellt worde.»", "bedeutsam",
  "Mit dem Zusatz steht ein eigener Vers 15,28, der die Kreuzigung zwischen zwei Räubern als Erfüllung von [[ISA.53.12]] deutet. Im SBLGNT fehlt der Vers; deshalb hat [[MRK.15.28]] hier keinen Text.",
  "Mit em Zuesatz staat en eigete Vers 15,28, wo d Chrüüzigung zwüsche zwei Röiber als Erfüllig vo [[ISA.53.12]] deutet. Im SBLGNT fäält de Vers; drum hät [[MRK.15.28]] da kein Text.",
  {"R1": [("αὐτοῦ", "(ohne Vers 28)", None)], "R2": [("Καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα, Καὶ μετὰ ἀνόμων ἐλογίσθη", "Und die Schrift wurde erfüllt, die sagt: Und er wurde zu den Gesetzlosen gerechnet.", "Vers 28")]},
  {"R1": [("αὐτοῦ", "(ohni Vers 28)", None)], "R2": [("Καὶ ἐπληρώθη ἡ γραφὴ ἡ λέγουσα, Καὶ μετὰ ἀνόμων ἐλογίσθη", "Und d Schrift isch erfüllt worde, wo seit: Und er isch zu de Gsetzlose zellt worde.", "Vers 28")]},
  ["Dasselbe Jesajawort zitiert Jesus in [[LUK.22.37]]; von dort kann es als Deutung hierher gelangt sein.",
   "In den CNTR-Transkriptionen von 01, 02, 03, 04 und 05 fehlt Vers 28 (die automatische Zuordnung führt diese Handschriften bei R1); bei 032 ist die Stelle nicht erhalten, 059 hat hier R1 mit teils beschädigtem bzw. ergänztem Wortlaut. Die gedruckten Ausgaben, die den Vers enthalten, führen ihn als eigenen Vers; die Kollation zu 15,27 erfasst ihn deshalb nicht."],
  ["S gliich Jesajawort zitiert de Jesus i [[LUK.22.37]]; vo det cha s als Deutig da ane choo sii.",
   "I de CNTR-Transkriptione vo 01, 02, 03, 04 und 05 fäält de Vers 28; bi 032 isch d Stell nöd erhalte. Di druckte Usgabe mit em Vers füered en als eigete Vers; d Kollation zu 15,27 erfasst en drum nöd."]),
 ("VAR-SBLGNTAPP-MRK-015-034-03:R2", "MRK.15.34", "lema", "lama", "lema", "lama", "gering",
  "Andere Umschrift des Fragewortes «wozu».", "En anderi Umschrift vom Fragewort «für was».",
  {"R1": [("λεμὰ", "lema", "aramäische Form")], "R2": [("λαμὰ", "lama", None)], "R3": [("λιμὰ", "lima", None)]},
  {"R1": [("λεμὰ", "lema", "aramäischi Form")], "R2": [("λαμὰ", "lama", None)], "R3": [("λιμὰ", "lima", None)]},
  ["λεμά entspricht dem Aramäischen, λαμά eher dem Hebräischen von [[PSA.22.1]]; die Abschreiber haben die fremden Wörter unterschiedlich umschrieben und teils an [[MAT.27.46]] angeglichen.",
   "Laut der automatischen Zuordnung lesen 01 und 04 λεμα, 03, 05 und 059 λαμα (059 teils beschädigt), 02 λιμα; 032 ist hier nicht erhalten. Im erfassten Wortlaut von 05 und 059 steht ausserdem ηλει statt ελωι (wie in Matthäus)."],
  ["λεμά entspricht em Aramäische, λαμά ehner em Hebräische vo [[PSA.22.1]].",
   "Nach de automatische Zueornig läsed 01 und 04 λεμα, 03, 05 und 059 λαμα, 02 λιμα. Im erfasste Wortlut vo 05 und 059 staat ussertem ηλει statt ελωι."]),
 ("VAR-SBLGNTAPP-MRK-015-039-01:R2", "MRK.15.39", "dass er so verschied", "dass er so schrie und verschied", "dass er eso gstorbe isch", "dass er eso gschroue hät und gstorbe isch", "gering",
  "Der Zusatz κράξας («schreiend») verbindet die Beobachtung des Hauptmanns mit dem Schrei in [[MRK.15.37]].", "De Zuesatz κράξας («schreiend») verbindet das, was de Hauptmaa gseht, mit em Schrei i [[MRK.15.37]].",
  {"R1": [("οὕτως", "so", None)], "R2": [("οὕτως κράξας", "so schreiend", "mit Zusatz")]},
  {"R1": [("οὕτως", "eso", None)], "R2": [("οὕτως κράξας", "eso schreiend", "mit Zuesatz")]},
  ["Der Zusatz macht ausdrücklich, was der Hauptmann sah; ohne ihn bleibt offen, was an der Art des Sterbens ihn bewegte.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne Zusatz, 02 und 04 mit ihm. 032 wird bei R1 geführt, hat aber im erfassten Wortlaut κράξας ohne οὕτως; 05 liest anders (mit κράξαντα)."],
  ["De Zuesatz macht usdrücklich, was de Hauptmaa gseh hät.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni Zuesatz, 02 und 04 mit; 032 hät im erfasste Wortlut κράξας ohni οὕτως, 05 lisst anders."]),
 ("VAR-SBLGNTAPP-MRK-015-045-01:R2", "MRK.15.45", "den Leichnam", "den Leib", "de Liichnam", "de Liib", "gering",
  "σῶμα («Leib») statt πτῶμα («Leichnam»).", "σῶμα («Liib») statt πτῶμα («Liichnam»).",
  {"R1": [("πτῶμα", "Leichnam", None)], "R2": [("σῶμα", "Leib", None)]},
  {"R1": [("πτῶμα", "Liichnam", None)], "R2": [("σῶμα", "Liib", None)]},
  ["«Leib» ist ehrfürchtiger und greift [[MRK.15.43]] auf; das härtere «Leichnam» kann deshalb ersetzt worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 πτῶμα, 02 (Erstschrift und Korrektur), 04 und 032 σῶμα; 059 ist hier nicht erhalten."],
  ["«Liib» isch ehrfürchtiger und nimmt [[MRK.15.43]] uf.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 πτῶμα, 02, 04 und 032 σῶμα."]),
 ("VAR-SBLGNTAPP-MRK-016-017-02:R2", "MRK.16.17", "in neuen Sprachen", "in Sprachen", "i nöie Spraache", "i Spraache", "gering",
  "Ohne «neu».", "Ohni «nöi».",
  {"R1": [("καιναῖς", "neuen", None)], "R2": [("–", "(fehlt)", None)]},
  {"R1": [("καιναῖς", "nöie", None)], "R2": [("–", "(fäält)", None)]},
  ["Das Wort kann als Verdeutlichung ergänzt oder als überflüssig weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 02 und 032 mit «neu», 04 ohne; 01 und 03 enthalten den längeren Schluss nicht, 05 hat hier keinen erfassten Text."],
  ["S Wort cha als Verdüütlichig ergänzt oder als überflüssig wäggloo worde sii.",
   "Nach de automatische Zueornig läsed 02 und 032 mit «nöi», 04 ohni; 01 und 03 händ de länger Schluss nöd."]),
 ("VAR-SBLGNTAPP-MRK-016-018-01:R2", "MRK.16.18", "Schlangen werden sie aufheben", "und mit den Händen werden sie Schlangen aufheben",
  "Schlange wärded si ufnää", "und mit de Händ wärded si Schlange ufnää", "gering",
  "Mit Zusatz «und mit den Händen». Hier folgt der SBLGNT-Text dem Mehrheitstext (RP); WH (in Doppelklammern), Treg und NA28 haben den Zusatz.",
  "Mit Zuesatz «und mit de Händ». Da folgt de SBLGNT-Text em Mehrheitstext (RP); WH, Treg und NA28 händ de Zuesatz.",
  {"R1": [("ὄφεις", "Schlangen", "SBLGNT, RP")], "R2": [("καὶ ἐν ταῖς χερσὶν ὄφεις", "und mit den Händen Schlangen", "WH, Treg, NA28")]},
  {"R1": [("ὄφεις", "Schlange", "SBLGNT, RP")], "R2": [("καὶ ἐν ταῖς χερσὶν ὄφεις", "und mit de Händ Schlange", "WH, Treg, NA28")]},
  ["Der Zusatz kann verdeutlichen oder beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 02 und 032 ohne Zusatz, 04 (beschädigt) mit ihm; 01 und 03 enthalten den längeren Schluss nicht."],
  ["De Zuesatz cha verdüütliche oder bim Abschriibe usgfalle sii.",
   "Nach de automatische Zueornig läsed 02 und 032 ohni Zuesatz, 04 mit; 01 und 03 händ de länger Schluss nöd."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MRK-014-001-072", "MRK.14.1-MRK.14.72", "section", "Salbung, Abendmahl, Getsemani und Verhör",
  ["TU-MRK-014-001-011", "TU-MRK-014-012-021", "TU-MRK-014-022-025", "TU-MRK-014-026-031", "TU-MRK-014-032-042",
   "TU-MRK-014-043-052", "TU-MRK-014-053-065", "TU-MRK-014-066-072"],
  "Zwei Tage vor dem Passa suchen die Hohepriester und Schriftgelehrten nach einer List, Jesus zu töten. Eine Frau salbt ihn in Betanien, Judas bietet die Auslieferung an. Beim Passamahl kündigt Jesus an, dass einer der Zwölf ihn ausliefert, und deutet Brot und Becher auf seinen Leib und sein Blut. In Getsemani ringt er im Gebet, während die Jünger schlafen; er wird gefangen genommen, alle fliehen. Vor dem Hohen Rat bekennt er sich als Christus und wird zum Tod verurteilt, während Petrus ihn im Hof dreimal verleugnet.", SEG),
 ("TU-MRK-014-001-011", "MRK.14.1-MRK.14.11", "narrative", "Die Salbung in Betanien", None,
  "Gerahmt vom Todesplan der Hohepriester und dem Angebot des Judas salbt eine namenlose Frau Jesus mit kostbarem Öl. Gegen den Vorwurf der Verschwendung deutet Jesus ihre Tat als Salbung für sein Begräbnis, die überall erzählt werden soll.", None),
 ("TU-MRK-014-012-021", "MRK.14.12-MRK.14.21", "narrative", "Vorbereitung des Passamahls und Ansage der Auslieferung", None,
  "Zwei Jünger finden den Raum, wie Jesus es gesagt hat. Beim Mahl kündigt Jesus an, dass einer, der mit ihm isst, ihn ausliefern wird; der Weg des Menschensohns entspricht der Schrift, doch wehe dem Menschen, der ihn ausliefert.", None),
 ("TU-MRK-014-022-025", "MRK.14.22-MRK.14.25", "narrative", "Brot und Becher", None,
  "Jesus gibt das Brot als seinen Leib und den Becher als sein Blut des Bundes, vergossen für viele, und blickt auf das neue Trinken im Reich Gottes voraus.", None),
 ("TU-MRK-014-026-031", "MRK.14.26-MRK.14.31", "narrative", "Ansage der Flucht und der Verleugnung", None,
  "Auf dem Weg zum Ölberg sagt Jesus mit [[ZEC.13.7]] voraus, dass alle zu Fall kommen, und verheisst, ihnen nach der Auferweckung nach Galiläa vorauszugehen. Petrus beteuert seine Treue; Jesus kündigt seine dreifache Verleugnung an.", None),
 ("TU-MRK-014-032-042", "MRK.14.32-MRK.14.42", "narrative", "Getsemani", None,
  "Jesus betet in Todesangst, der Becher möge an ihm vorübergehen, und unterstellt sich doch dem Willen des Vaters. Dreimal findet er die Jünger schlafend; dann ist die Stunde der Auslieferung da.", None),
 ("TU-MRK-014-043-052", "MRK.14.43-MRK.14.52", "narrative", "Die Gefangennahme", None,
  "Judas kommt mit einer bewaffneten Menge und gibt das vereinbarte Zeichen, einen Kuss. Jesus wird ergriffen und sieht darin die Schriften erfüllt; alle Jünger fliehen, ein junger Mann sogar nackt.", None),
 ("TU-MRK-014-053-065", "MRK.14.53-MRK.14.65", "narrative", "Vor dem Hohen Rat", None,
  "Falsche Zeugen widersprechen einander. Auf die Frage des Hohepriesters bekennt Jesus, der Christus zu sein, und spricht vom Menschensohn zur Rechten der Macht. Der Rat verurteilt ihn wegen Lästerung zum Tod; man verspottet und schlägt ihn.", None),
 ("TU-MRK-014-066-072", "MRK.14.66-MRK.14.72", "narrative", "Petrus verleugnet Jesus", None,
  "Im Hof wird Petrus dreimal als Anhänger Jesu erkannt und streitet es immer heftiger ab. Als der Hahn zum zweiten Mal kräht, erinnert er sich an Jesu Wort und weint.", None),
 ("TU-MRK-015-001-047", "MRK.15.1-MRK.15.47", "section", "Verurteilung, Kreuzigung und Begräbnis",
  ["TU-MRK-015-001-015", "TU-MRK-015-016-020", "TU-MRK-015-021-032", "TU-MRK-015-033-041", "TU-MRK-015-042-047"],
  "Der Hohe Rat liefert Jesus an Pilatus aus. Die Menge verlangt die Freilassung des Barabbas und die Kreuzigung Jesu; Pilatus gibt nach. Soldaten verspotten ihn als König, er wird gekreuzigt und von allen Seiten verhöhnt. Nach drei Stunden Finsternis schreit er die Klage aus [[PSA.22.1]] und stirbt mit einem lauten Schrei; der Tempelvorhang reisst, und der Hauptmann bekennt ihn als Gottes Sohn. Frauen sehen zu; Josef von Arimatäa begräbt ihn. [[MRK.15.28]] steht nicht im SBLGNT.",
  SEG + " [[MRK.15.28]] fehlt im SBLGNT und hat keinen Text; der Bereich der Kapiteleinheit schliesst die Versnummer trotzdem ein."),
 ("TU-MRK-015-001-015", "MRK.15.1-MRK.15.15", "narrative", "Vor Pilatus", None,
  "Pilatus fragt Jesus, ob er der König der Juden sei; Jesus antwortet knapp und schweigt dann. Die von den Hohepriestern aufgewiegelte Menge fordert Barabbas und schreit nach der Kreuzigung; Pilatus lässt Jesus geisseln und liefert ihn aus.", None),
 ("TU-MRK-015-016-020", "MRK.15.16-MRK.15.20", "narrative", "Die Verspottung durch die Soldaten", None,
  "Die Kohorte kleidet Jesus in Purpur, setzt ihm einen Dornenkranz auf, grüsst ihn als König der Juden, schlägt und bespuckt ihn und führt ihn zur Kreuzigung hinaus.", None),
 ("TU-MRK-015-021-032", "MRK.15.21-MRK.15.32", "narrative", "Die Kreuzigung", None,
  "Simon von Kyrene muss das Kreuz tragen. In Golgota wird Jesus gekreuzigt, seine Kleider werden verlost, die Aufschrift nennt ihn König der Juden. Zwischen zwei Räubern wird er von Vorübergehenden, Hohepriestern und Mitgekreuzigten verspottet.", None),
 ("TU-MRK-015-033-041", "MRK.15.33-MRK.15.41", "narrative", "Der Tod Jesu", None,
  "Finsternis liegt über dem Land. Jesus schreit die Klage aus [[PSA.22.1]] und stirbt mit einem lauten Schrei. Der Tempelvorhang reisst, der Hauptmann nennt ihn Gottes Sohn; Frauen, die ihm seit Galiläa gefolgt sind, schauen von ferne zu.", None),
 ("TU-MRK-015-042-047", "MRK.15.42-MRK.15.47", "narrative", "Das Begräbnis", None,
  "Josef von Arimatäa erbittet von Pilatus den Leichnam, wickelt ihn in Leinen und legt ihn in ein Felsengrab. Zwei der Frauen sehen, wo er liegt.", None),
 ("TU-MRK-016-001-020", "MRK.16.1-MRK.16.20", "section", "Das leere Grab und die weiteren Markusschlüsse",
  ["TU-MRK-016-001-008", "TU-MRK-016-009-020"],
  "Die Frauen finden das Grab offen; ein junger Mann verkündet ihnen, Jesus sei auferweckt worden und gehe den Jüngern nach Galiläa voraus. Sie fliehen und sagen aus Furcht niemandem etwas. Mit [[MRK.16.8]] enden die Handschriften 01 und 03 nach der CNTR-Transkription. Der SBLGNT druckt danach in Doppelklammern ⟦ ⟧ zwei weitere Schlüsse, die in der Textforschung weithin als spätere Ergänzungen gelten: den kürzeren Schluss (innerhalb von 16,8) und den längeren Schluss [[MRK.16.9]]–[[MRK.16.20]].",
  SEG + " Der kürzere Schluss steht im SBLGNT innerhalb von [[MRK.16.8]] (Tokens 19–52) und bildet deshalb keine eigene Texteinheit; er gehört zu TU-MRK-016-001-008 und ist dort beschrieben."),
 ("TU-MRK-016-001-008", "MRK.16.1-MRK.16.8", "narrative", "Das leere Grab", None,
  "Am Morgen nach dem Sabbat kommen drei Frauen mit Salben zum Grab. Der Stein ist weggewälzt; ein junger Mann in weissem Gewand sagt ihnen, der Gekreuzigte sei auferweckt worden, und schickt sie mit einer Botschaft zu den Jüngern und Petrus. Sie fliehen zitternd und sagen niemandem etwas, «denn sie fürchteten sich». Im SBLGNT folgt in Doppelklammern ⟦ ⟧ der kürzere Markusschluss: Die Frauen berichten alles den Leuten um Petrus, und Jesus sendet durch sie die Botschaft vom ewigen Heil von Osten bis Westen aus. Dieser Schluss gilt in der Textforschung weithin als spätere Ergänzung; in keiner der im Projekt erfassten CNTR-Transkriptionen (01, 02, 03, 04, 05, 032) steht er.", None),
 ("TU-MRK-016-009-020", "MRK.16.9-MRK.16.20", "narrative", "Der längere Markusschluss", None,
  "Der Auferstandene erscheint Maria aus Magdala, dann zwei Jüngern unterwegs; man glaubt ihnen nicht. Schliesslich erscheint er den Elf, tadelt ihren Unglauben und sendet sie in alle Welt, das Evangelium zu verkündigen; Zeichen sollen die Glaubenden begleiten. Er wird in den Himmel aufgenommen, die Jünger verkündigen überall. Der SBLGNT setzt den Abschnitt in Doppelklammern ⟦ ⟧ und kennzeichnet ihn damit als spätere Ergänzung; so urteilt die Textforschung weithin, eine Minderheit hält ihn für ursprünglich, viele Kirchen anerkennen ihn als kanonisch. In den CNTR-Transkriptionen von 01 und 03 endet der Text mit [[MRK.16.8]]; 02, 04 und 032 enthalten den Abschnitt (032 mit einem zusätzlichen Einschub nach [[MRK.16.14]]).", None),
]
UNITS_GSW = {
 "TU-MRK-014-001-072": ("Salbig, Aabigmaal, Getsemani und Verhör", "Zwei Täg vor em Passa sueched d Hoheprieschter und d Schriftgleerte e Lischt, zum de Jesus töte. E Frau salbt en z Betanie, de Judas bietet aa, en uszliefere. Bim Passamaal seit de Jesus, dass eine vo de Zwölf en usliferet, und deutet s Broot und de Bächer uf sin Liib und sis Bluet. Z Getsemani ringt er im Gebätt, während d Jünger schlaafed; er wird gfange gnoo, alli flüchted. Vor em Hohe Raat bekännt er sich als Christus und wird zum Tod verurteilt, während de Petrus en im Hof drüümal verleugnet."),
 "TU-MRK-014-001-011": ("D Salbig z Betanie", "Zwüsche em Plan vo de Hoheprieschter und em Aagebot vom Judas salbt e Frau ohni Name de Jesus mit tüürem Öl. Gäge de Vorwurf vo Verschwändig seit de Jesus, si heig en für sis Begräbnis gsalbet, und das wärdi überall verzellt."),
 "TU-MRK-014-012-021": ("Vorbereitig vom Passamaal und Aasag vo de Uslieferig", "Zwei Jünger finded de Ruum, wie s de Jesus gseit hät. Bim Ässe seit de Jesus, dass eine, wo mit ihm isst, en wird uslifere; de Wäg vom Mänschesohn entspricht de Schrift, aber wehe däm Mänsch, wo en usliferet."),
 "TU-MRK-014-022-025": ("Broot und Bächer", "De Jesus git s Broot als sin Liib und de Bächer als sis Bluet vom Bund, wo für vili vergosse wird, und luegt voruus uf s nöi Trinke im Riich vo Gott."),
 "TU-MRK-014-026-031": ("Aasag vo de Flucht und de Verleugnig", "Uf em Wäg zum Ölberg seit de Jesus mit [[ZEC.13.7]] voruus, dass alli z Fall chömed, und verspricht, ine nach de Uferweckig uf Galiläa voruszgaa. De Petrus beteuret sini Tröii; de Jesus seit em sini drüüfach Verleugnig aa."),
 "TU-MRK-014-032-042": ("Getsemani", "De Jesus bättet i Todesangscht, de Bächer söll a ihm verbii gaa, und git sich doch em Wille vom Vatter häre. Drüümal findt er d Jünger am Schlaafe; dänn isch d Stund vo de Uslieferig da."),
 "TU-MRK-014-043-052": ("D Gfangenaam", "De Judas chunnt mit ere bewaffnete Mängi und git s abgmacht Zeiche, en Kuss. De Jesus wird packt und gseht drin d Schrifte erfüllt; alli Jünger flüchted, en junge Maa sogar blutt."),
 "TU-MRK-014-053-065": ("Vor em Hohe Raat", "Falschi Züüge widerspräched enand. Uf d Frag vom Hoheprieschter bekännt de Jesus, er sig de Christus, und redt vom Mänschesohn zur Rächte vo de Macht. De Raat verurteilt en wäge Läschterig zum Tod; mer verspottet und schlaat en."),
 "TU-MRK-014-066-072": ("De Petrus verleugnet de Jesus", "Im Hof wird de Petrus drüümal als Aahänger vom Jesus erchännt und strittet s immer heftiger ab. Wo de Güggel zum zweite Mal chräit, erinneret er sich as Wort vom Jesus und briegget."),
 "TU-MRK-015-001-047": ("Verurteilig, Chrüüzigung und Begräbnis", "De Hoch Raat liferet de Jesus em Pilatus us. D Mängi verlangt de Barabbas frei und de Jesus am Chrüüz; de Pilatus git naa. Soldate verspotted en als König, er wird gchrüüziget und vo allne Siite verhöhnt. Nach drüü Stund Fischternis schreit er d Klag us [[PSA.22.1]] und stirbt mit eme luute Schrei; de Vorhang im Tämpel verriisst, und de Hauptmaa bekännt en als Gottes Sohn. Fraue lueged zue; de Josef vo Arimatäa begrabt en. [[MRK.15.28]] staat nöd im SBLGNT."),
 "TU-MRK-015-001-015": ("Vor em Pilatus", "De Pilatus fröget de Jesus, öb er de König vo de Jude sig; de Jesus antwortet churz und schwiigt dänn. D Mängi, vo de Hoheprieschter ufgwieglet, verlangt de Barabbas und brüelet nach de Chrüüzigung; de Pilatus laat de Jesus gisle und liferet en us."),
 "TU-MRK-015-016-020": ("D Soldate verspotted de Jesus", "D Kohorte leit em Purpur aa, setzt em en Dornechranz uf, grüesst en als König vo de Jude, schlaat und bespöit en und füert en zur Chrüüzigung use."),
 "TU-MRK-015-021-032": ("D Chrüüzigung", "De Simon vo Kyrene mues s Chrüüz träge. Uf Golgota wird de Jesus gchrüüziget, sini Chleider wärded verlost, d Ufschrift nännt en König vo de Jude. Zwüsche zwei Röiber wird er vo Lüüt, wo verbii gönd, vo de Hoheprieschter und vo de Mitgchrüüzigte verspottet."),
 "TU-MRK-015-033-041": ("De Tod vom Jesus", "Fischternis liit über em Land. De Jesus schreit d Klag us [[PSA.22.1]] und stirbt mit eme luute Schrei. De Vorhang im Tämpel verriisst, de Hauptmaa nännt en Gottes Sohn; Fraue, wo ihm sit Galiläa gfolgt sind, lueged vo wiitem zue."),
 "TU-MRK-015-042-047": ("S Begräbnis", "De Josef vo Arimatäa bittet de Pilatus um de Liichnam, wicklet en in es Liinetuech und leit en in es Felsegrab. Zwei vo de Fraue gsehnd, wo er liit."),
 "TU-MRK-016-001-020": ("S läär Grab und di wiitere Markusschlüss", "D Fraue finded s Grab offe; en junge Maa seit ine, de Jesus sig uferweckt worde und gang de Jünger voruus uf Galiläa. Si flüchted und säged us Angscht niemertem öppis. Mit [[MRK.16.8]] hört de Text i de Handschrifte 01 und 03 uf (CNTR-Transkription). De SBLGNT druckt nachher i Doppelklammere ⟦ ⟧ zwei wiiteri Schlüss, wo i de Textforschig wiitume als spööteri Ergänzige gälted: de chürzer Schluss (in 16,8) und de länger Schluss [[MRK.16.9]]–[[MRK.16.20]]."),
 "TU-MRK-016-001-008": ("S läär Grab", "Am Morge nach em Sabbat chömed drei Fraue mit Salbe zum Grab. De Stei isch wäggwälzt; en junge Maa im wiisse Gwand seit ine, de Gchrüüzigt sig uferweckt worde, und schickt si mit ere Botschaft zu de Jünger und zum Petrus. Si flüchted zitterig und säged niemertem öppis, «si händ sich nämli gfürchtet». Im SBLGNT folgt i Doppelklammere ⟦ ⟧ de chürzer Markusschluss: D Fraue verzelled alles de Lüüt um de Petrus, und de Jesus schickt dur si d Botschaft vom ewige Heil vo Oschte bis Weschte us. Dä Schluss gilt i de Textforschig wiitume als spööteri Ergänzig; i keinere vo de erfasste CNTR-Transkriptione (01, 02, 03, 04, 05, 032) staat er."),
 "TU-MRK-016-009-020": ("De länger Markusschluss", "De Uferstande erschiint de Maria vo Magdala, dänn zwei Jünger understwägs; mer glaubt ine nöd. Zletscht erschiint er de Elf, tadlet iren Unglaube und schickt si i di ganz Wält, zum s Evangelium verchünde; Zeiche söled d Gläubige begleite. Er wird in Himmel ufgnoo, d Jünger verchünded überall. De SBLGNT setzt de Abschnitt i Doppelklammere ⟦ ⟧ und zeichnet en demit als spööteri Ergänzig us; so urteilt d Textforschig wiitume, e Minderheit hebt en für ursprünglich, vili Chile anerchänned en als kanonisch. I de CNTR-Transkriptione vo 01 und 03 hört de Text mit [[MRK.16.8]] uf; 02, 04 und 032 händ de Abschnitt (032 mit eme zuesätzliche Iischub nach [[MRK.16.14]])."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("[[MRK.15.28]] steht nicht im SBLGNT und hat deshalb hier keinen Text. Laut SBLGNT-Apparat haben Treg und RP den Vers "
  "(«Und die Schrift wurde erfüllt, die sagt: Und er wurde zu den Gesetzlosen gerechnet», vgl. [[ISA.53.12]]); in den "
  "CNTR-Transkriptionen von 01, 02, 03, 04 und 05 fehlt er. Er ist als Alternative bei [[MRK.15.27]] aufgeführt."),
 ("Markusschlüsse: Der SBLGNT druckt nach ἐφοβοῦντο γάρ ([[MRK.16.8]]) in Doppelklammern ⟦ ⟧ zuerst den kürzeren Schluss "
  "(innerhalb der Tokens von 16,8) und dann den längeren Schluss [[MRK.16.9]]–[[MRK.16.20]]. Beide sind übersetzt, weil sie im "
  "Ausgangstext stehen; die Klammern sind beibehalten und weisen sie als spätere Ergänzungen aus. In den CNTR-Transkriptionen "
  "von 01 (Codex Sinaiticus) und 03 (Codex Vaticanus) endet das Evangelium mit 16,8; für 16,9–20 ist dort kein Text erfasst "
  "(die automatische Kollation führt diese Verse dort als «nicht erhalten», unterscheidet also nicht zwischen Auslassung und "
  "Verlust). 02, 04 und 032 enthalten den längeren Schluss, 05 nach der Transkription bis 16,15; 032 hat nach 16,14 einen "
  "weiteren Einschub (sogenanntes Freer-Logion). Den kürzeren Schluss enthält keine der erfassten Transkriptionen. Die "
  "Kollation zu VAR-SBLGNTAPP-MRK-016-008-02 konnte die Zeugen keiner Lesart zuordnen; die Angaben hier stützen sich deshalb "
  "auf die Transkriptionen selbst."),
 ("In [[MRK.14.70]] und [[MRK.16.18]] folgt die Übersetzung dem Token-Text des SBLGNT, der dort mit RP gegen WH, Treg und NA28 "
  "liest; die anderen Wortlaute stehen als Alternativen."),
 ("Markus erzählt oft im Präsens («er kommt», «sie sagen»); das ist beibehalten. παραδίδωμι ist durchgehend mit «ausliefern» "
  "wiedergegeben. ὅτι vor direkter Rede ist nicht eigens übersetzt."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("[[MRK.15.28]] staat nöd im SBLGNT und hät drum da kein Text; de Vers staat als Alternative bi [[MRK.15.27]]."),
 ("Markusschlüss: De SBLGNT druckt nach [[MRK.16.8]] i Doppelklammere ⟦ ⟧ de chürzer Schluss (in 16,8) und de länger Schluss "
  "[[MRK.16.9]]–[[MRK.16.20]]. Beidi sind übersetzt, wil si im Text stönd; d Klammere zeiged, dass es spööteri Ergänzige sind. "
  "I de CNTR-Transkriptione vo 01 und 03 hört s Evangelium mit 16,8 uf."),
]


def run():
    import json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _lib import localize  # noqa: E402
    n = 0
    if not (D / "works" / "WORK-MRK.json").exists():
        raise SystemExit("WORK-MRK fehlt")
    for uid, rng, kind, title, parts, summary, seg in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-MRK", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}), "segmentation_note_de": seg,
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        rec = {k: v for k, v in rec.items() if v is not None}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-14; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-mrk").glob("*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-MRK-{c:03d}.json")
        refs_c = [f"MRK.{c}.{v}" for v in range(1, last + 1) if f"MRK.{c}.{v}" in toks]  # 15,28 fehlt im SBLGNT
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-MRK-{c:03d}-001-{last:03d}-{code}-WORKING"
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
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"MRK.{c}.1-MRK.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MRK-{c:03d}-001-{last:03d}-DE-WORKING",
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
            aid = f"ALIGN-MRK-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"MRK.{c}.1-MRK.{c}.{last}",
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/markus_text_14_16.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Markus 14–16 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
