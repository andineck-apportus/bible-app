#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 26 (Salbung in Betanien, letztes Mahl, Getsemani, Gefangennahme, Verhör vor dem Hohen Rat,
Verleugnung des Petrus) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_26_26.py

Muster: scripts/authoring/johannes_text_01_03.py. Die Übersetzung steht als Auszeichnung je Vers (siehe _lib.py); Text
und Wortzuordnung entstehen daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins
revision_log. WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 26 fehlt im SBLGNT kein Vers (per Skript geprüft); alle 75 Verse haben Tokens.
- Parallele: Markus 14 (TRANS-MRK-014-001-072-*). Gleiche griechische Wendungen sind möglichst gleich übersetzt
  (z. B. «ausliefern», «Becher», «sprach den Lobpreis»); wo Matthäus anders formuliert, folgt die
  Übersetzung seinem Wortlaut.
- [[MAT.26.42]] «so geschehe dein Wille» nimmt den Wortlaut des Vaterunsers auf ([[MAT.6.10]], vaterunser.py); die
  Wiedergabe ist darauf abgestimmt (Mundart «söll diin Wile gschee»).

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben in den Lesarten stammen aus der maschinellen Zuordnung
(METHOD-AUTO-COLLATION-V1, data/witness-readings/WREAD-CNTR-MAT-026-001-075), nicht aus eigener Prüfung der
Handschriften.
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
CHAPTERS = ((26, 75),)

DE = {
 # ------------------------------------------------------------ Kapitel 26
 "MAT.26.1": "Und{1} [es geschah]{2}, [als]{3} [Jesus]{5,6} [alle]{7} [diese]{10} [Worte]{8,9} [beendet hatte]{4}, [da sagte er]{11} [zu]{12} [seinen]{14} [Jüngern]{13}:",
 "MAT.26.2": "«[Ihr wisst]{1}, [dass]{2} [in]{3} [zwei]{4} [Tagen]{5} [das Passa]{6,7} [ist]{8}, und{9} [der Menschensohn]{10-13} [wird ausgeliefert]{14}, [um]{15,16} [gekreuzigt zu werden]{17}.»",
 "MAT.26.3": "[Da]{1} [versammelten sich]{2} [die Hohepriester]{3,4} und{5} [die Ältesten]{6,7} [des Volkes]{8,9} [im]{10,11} [Hof]{12} [des Hohepriesters]{13,14}, [der]{15} [Kajafas]{17} [hiess]{16},",
 "MAT.26.4": "und{1} [berieten miteinander]{2}, [wie]{3} [sie]{7} [Jesus]{4,5} [mit List]{6} [ergreifen]{7} und{8} [töten könnten]{9}.",
 "MAT.26.5": "[Sie sagten]{1} [aber]{2}: «[Nicht]{3} [am]{4,5} [Fest]{6}, [damit]{7} [kein]{8} [Aufruhr]{9} [im]{11,12} [Volk]{13} [entsteht]{10}.»",
 "MAT.26.6": "[Als]{4} [Jesus]{1,3} [aber]{2} [in]{5} [Betanien]{6} [im]{7} [Haus]{8} [Simons]{9} [des Aussätzigen]{10,11} [war]{4},",
 "MAT.26.7": "[trat]{1} [eine Frau]{3} [mit]{4} [einem Alabastergefäss]{5} [voll]{6} [sehr kostbarem]{7} [Salböl]{6} [zu ihm]{2} [heran]{1} und{8} [goss]{9} es [ihm]{13} [über]{10} [den]{11} [Kopf]{12}, [während er zu Tisch lag]{14}.",
 "MAT.26.8": "[Als]{1} [die Jünger]{3,4} [das]{1} [aber]{2} [sahen]{1}, [empörten sie sich]{5} und [sagten]{6}: «[Wozu]{7,8} [diese]{11} [Verschwendung]{9,10}?",
 "MAT.26.9": "[Das]{3} [hätte]{1} [nämlich]{2} [für viel Geld]{5} [verkauft]{4} und{6} [den Armen]{8} [gegeben]{7} [werden können]{1}.»",
 "MAT.26.10": "[Jesus]{3,4} [aber]{2} [merkte es]{1} und [sagte]{5} [zu ihnen]{6}: «[Warum]{7} [bereitet ihr]{9} [der]{10} [Frau]{11} [Verdruss]{8}? [Sie hat]{15} [nämlich]{13} [ein gutes]{14} [Werk]{12} [an]{16} [mir]{17} [getan]{15}.",
 "MAT.26.11": "[Denn]{2} [die Armen]{3,4} [habt ihr]{5} [immer]{1} [bei]{6} [euch]{7}, [mich]{8} [aber]{9} [habt ihr]{12} [nicht]{10} [immer]{11}.",
 "MAT.26.12": "[Denn]{2} [indem]{1} [sie]{3} [dieses]{4,6} [Salböl]{5} [auf]{7} [meinen]{8,10} [Leib]{9} [gegossen hat]{1}, [hat sie]{15} es [für]{11,12} [mein]{14} [Begräbnis]{13} [getan]{15}.",
 "MAT.26.13": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Wo immer]{4,5} [dieses]{9} [Evangelium]{7,8} [verkündigt wird]{6} [in]{10} [der]{12} [ganzen]{11} [Welt]{13}, [wird]{14} [auch]{15} [erzählt werden]{14}, [was]{16} [sie]{18} [getan hat]{17}, [zu]{19} [ihrem]{21} [Gedächtnis]{20}.»",
 "MAT.26.14": "[Da]{1} [ging]{2} [einer]{3} [der]{4} [Zwölf]{5}, [der]{6} [Judas]{8} [Iskariot]{9} [hiess]{7}, [zu]{10} [den Hohepriestern]{11,12}",
 "MAT.26.15": "und [sagte]{1}: «[Was]{2} [wollt ihr]{3} [mir]{4} [geben]{5}? [Dann]{6} [werde]{8} [ich]{6} [ihn]{9} [euch]{7} [ausliefern]{8}.» [Sie]{10} [aber]{11} [wogen]{12} [ihm]{13} [dreissig]{14} [Silberstücke]{15} [ab]{12}.",
 "MAT.26.16": "Und{1} [von da an]{2,3} [suchte er]{4} [eine günstige Gelegenheit]{5}, [um]{6} [ihn]{7} [auszuliefern]{8}.",
 "MAT.26.17": "[Am]{1} [ersten Tag]{3} [der Ungesäuerten Brote]{4,5} [aber]{2} [traten]{6} [die Jünger]{7,8} [zu]{9} [Jesus]{10} [heran]{6} und [sagten]{11}: «[Wo]{12} [willst du]{13}, [dass wir]{14} [dir]{15} alles [vorbereiten]{14}, [damit du]{16} [das Passa]{17,18} [essen kannst]{16}?»",
 "MAT.26.18": "[Er]{1} [aber]{2} [sagte]{3}: «[Geht]{4} [in]{5} [die Stadt]{6,7} [zu]{8} [dem und dem]{9,10} und{11} [sagt]{12} [zu ihm]{13}: ‹[Der Lehrer]{14,15} [sagt]{16}: [Meine]{19} [Zeit]{17,18} [ist]{21} [nahe]{20}; [bei]{22} [dir]{23} [halte ich]{24} [das Passa]{25,26} [mit]{27} [meinen]{28,30} [Jüngern]{29}.›»",
 "MAT.26.19": "Und{1} [die Jünger]{3,4} [taten]{2}, [wie]{5} [Jesus]{8,9} es [ihnen]{7} [aufgetragen hatte]{6}, und{10} [bereiteten]{11} [das Passa]{12,13} [vor]{11}.",
 "MAT.26.20": "[Als]{3} es [aber]{2} [Abend]{1} [geworden war]{3}, [lag er]{4} [mit]{5} [den]{6} [zwölf]{7} [Jüngern]{8} [zu Tisch]{4}.",
 "MAT.26.21": "Und{1} [während]{2} [sie]{3} [assen]{2}, [sagte er]{4}: «[Amen]{5}, [ich sage]{6} [euch]{7}: [Einer]{9} [von]{10} [euch]{11} [wird]{12} [mich]{13} [ausliefern]{12}.» ~8(ὅτι leitet die direkte Rede ein)",
 "MAT.26.22": "Und{1} [sie wurden]{2} [sehr]{3} [traurig]{2} und [fingen an]{4}, [ihm]{6} [zu sagen]{5}, [jeder einzelne]{7,8}: «[Ich]{10} [bin es]{11} [doch nicht]{9}, [Herr]{12}?»",
 "MAT.26.23": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: «[Der]{5} [mit]{7} [mir]{8} [die Hand]{9,10} [in]{11} [die Schüssel]{12,13} [getaucht hat]{6}, [der]{14} [wird]{16} [mich]{15} [ausliefern]{16}.",
 "MAT.26.24": "[Der Menschensohn]{1,3,4,5} [geht]{6} [zwar]{2} [dahin]{6}, [wie]{7} [über]{9} [ihn]{10} [geschrieben steht]{8}; [weh]{11} [aber]{12} [jenem]{13,15} [Menschen]{14}, [durch]{16} [den]{17} [der Menschensohn]{18-21} [ausgeliefert wird]{22}! [Es wäre]{24} [gut]{23} [für ihn]{25}, [wenn]{26} [jener]{29,31} [Mensch]{30} [nicht]{27} [geboren wäre]{28}.»",
 "MAT.26.25": "[Judas]{3} [aber]{2}, [der]{4} [ihn]{6} [auslieferte]{5}, [antwortete]{1} und [sagte]{7}: «[Ich]{9} [bin es]{10} [doch nicht]{8}, [Rabbi]{11}?» [Er sagt]{12} [zu ihm]{13}: «[Du]{14} [hast es gesagt]{15}.»",
 "MAT.26.26": "[Während]{1} [sie]{3} [aber]{2} [assen]{1}, [nahm]{4} [Jesus]{5,6} [Brot]{7} und{8} [sprach den Lobpreis]{9}; er [brach]{10} es und{11} [gab es]{12} [den Jüngern]{13,14} und [sagte]{15}: «[Nehmt]{16}, [esst]{17}! [Das]{18} [ist]{19} [mein]{22} [Leib]{20,21}.»",
 "MAT.26.27": "Und{1} [er nahm]{2} [einen Becher]{3} und{4} [sprach das Dankgebet]{5}, [gab]{6} ihn [ihnen]{7} und [sagte]{8}: «[Trinkt]{9} [alle]{12} [daraus]{10,11}!",
 "MAT.26.28": "[Denn]{2} [das]{1} [ist]{3} [mein]{6} [Blut]{4,5} [des Bundes]{7,8}, [das]{9} [für]{10} [viele]{11} [vergossen wird]{12} [zur]{13} [Vergebung]{14} [der Sünden]{15}.",
 "MAT.26.29": "[Ich sage]{1} [euch]{3} [aber]{2}: [Ich werde]{6} [von nun an]{7,8} [gewiss nicht mehr]{4,5} [von]{9} [diesem]{10} [Gewächs]{11,12} [des Weinstocks]{13,14} [trinken]{6} [bis]{15} [zu jenem]{16,18} [Tag]{17}, [an dem]{19} [ich]{21} [es]{20} [mit]{22} [euch]{23} [neu]{24} [trinke]{21} [im]{25,26} [Reich]{27} [meines]{30} [Vaters]{28,29}.»",
 "MAT.26.30": "Und{1} [nachdem sie den Lobgesang gesungen hatten]{2}, [gingen sie hinaus]{3} [zum]{4,5} [Ölberg]{6-8}.",
 "MAT.26.31": "[Da]{1} [sagt]{2} [Jesus]{4,5} [zu ihnen]{3}: «[Ihr]{7} [alle]{6} [werdet]{8} [in]{11} [dieser]{12,14} [Nacht]{13} [an]{9} [mir]{10} [Anstoss nehmen]{8}; [denn]{16} [es steht geschrieben]{15}: ‹[Ich werde]{17} [den Hirten]{18,19} [schlagen]{17}, und{20} [die Schafe]{22,23} [der Herde]{24,25} [werden zerstreut werden]{21}.›",
 "MAT.26.32": "[Nachdem]{1,3} [ich]{5} [aber]{2} [auferweckt worden bin]{4}, [werde ich]{6} [euch]{7} [nach]{8,9} [Galiläa]{10} [vorausgehen]{6}.»",
 "MAT.26.33": "[Petrus]{3,4} [aber]{2} [antwortete]{1} und [sagte]{5} [zu ihm]{6}: «[Wenn]{7} [alle]{8} [an]{10} [dir]{11} [Anstoss nehmen]{9} – [ich]{12} [werde]{14} [niemals]{13} [Anstoss nehmen]{14}!»",
 "MAT.26.34": "[Jesus]{3,4} [sagte]{1} [zu ihm]{2}: «[Amen]{5}, [ich sage]{6} [dir]{7}: [In]{9} [dieser]{10,11} [Nacht]{12}, [bevor]{13} [ein Hahn]{14} [kräht]{15}, [wirst du]{17} [mich]{18} [dreimal]{16} [verleugnen]{17}.» ~8(ὅτι leitet die direkte Rede ein)",
 "MAT.26.35": "[Petrus]{3,4} [sagt]{1} [zu ihm]{2}: «[Selbst wenn]{5} [ich]{7} [mit]{8} [dir]{9} [sterben]{10} [müsste]{6}, [werde ich]{14} [dich]{13} [gewiss nicht]{11,12} [verleugnen]{14}!» [Ebenso]{15} [sprachen]{20} [auch]{16} [alle]{17} [Jünger]{18,19}.",
 "MAT.26.36": "[Da]{1} [kommt]{2} [Jesus]{5,6} [mit]{3} [ihnen]{4} [zu]{7} [einem Grundstück]{8}, [das]{9} [Getsemani]{10} [heisst]{9}, und{11} [sagt]{12} [zu den]{13} [Jüngern]{14}: «[Setzt euch]{15} [hier]{16} [hin]{15}, [während]{17,18} [ich]{21} [dorthin]{20} [gehe]{19} [und bete]{21}.»",
 "MAT.26.37": "Und{1} [er nahm]{2} [Petrus]{3,4} und{5} [die]{6} [beiden]{7} [Söhne]{8} [des Zebedäus]{9} [mit sich]{2} und [fing an]{10}, [traurig zu werden]{11} und{12} [sich zu ängstigen]{13}.",
 "MAT.26.38": "[Da]{1} [sagt er]{2} [zu ihnen]{3}: «[Tief betrübt]{4} [ist]{5} [meine]{8} [Seele]{6,7} [bis]{9} [zum Tod]{10}. [Bleibt]{11} [hier]{12} und{13} [wacht]{14} [mit]{15} [mir]{16}!»",
 "MAT.26.39": "Und{1} [er ging]{2} [ein wenig]{3} [weiter]{2}, [fiel]{4} [auf]{5} [sein]{7} [Gesicht]{6}, [betete]{8} und{9} [sagte]{10}: «[Mein]{12} [Vater]{11}, [wenn]{13} es [möglich]{14} [ist]{15}, so [gehe]{16} [dieser]{19,21} [Becher]{20} [an]{17} [mir]{18} [vorüber]{16}! [Doch]{22} [nicht]{23}, [wie]{24} [ich]{25} [will]{26}, [sondern]{27} [wie]{28} [du]{29} willst.»",
 "MAT.26.40": "Und{1} [er kommt]{2} [zu]{3} [den Jüngern]{4,5} und{6} [findet]{7} [sie]{8} [schlafend]{9}, und{10} [er sagt]{11} [zu]{12} [Petrus]{13}: «[So]{14} [wart ihr]{16} [nicht]{15} [imstande]{16}, [eine]{17} [Stunde]{18} [mit]{20} [mir]{21} [zu wachen]{19}?",
 "MAT.26.41": "[Wacht]{1} und{2} [betet]{3}, [damit]{4} [ihr]{6} [nicht]{5} [in]{7} [Versuchung]{8} [kommt]{6}! [Der Geist]{9,11} ist [zwar]{10} [willig]{12}, [das Fleisch]{13,15} [aber]{14} [schwach]{16}.»",
 "MAT.26.42": "[Wieder]{1} [ging er]{4} [zum zweiten Mal]{2,3} [weg]{4}, [betete]{5} und [sagte]{6}: «[Mein]{8} [Vater]{7}, [wenn]{9} [dies]{12} [nicht]{10} [vorübergehen]{13} [kann]{11}, [ohne dass]{14,15} [ich]{17} [es]{16} [trinke]{17}, [so geschehe]{18} [dein]{21} [Wille]{19,20}.»",
 "MAT.26.43": "Und{1} [als er]{2} [wieder]{3} [kam]{2}, [fand er]{4} [sie]{5} [schlafend]{6}; [denn]{8} [ihre]{9} [Augen]{10,11} [waren]{7} [schwer]{12}.",
 "MAT.26.44": "Und{1} [er liess]{2} [sie]{3}, [ging]{5} [wieder]{4} [weg]{5} und [betete]{6} [zum dritten Mal]{7,8} und [sprach]{12} [noch einmal]{13} [dieselben]{9,10} [Worte]{11}.",
 "MAT.26.45": "[Dann]{1} [kommt er]{2} [zu]{3} [den Jüngern]{4,5} und{6} [sagt]{7} [zu ihnen]{8}: «[Schlaft ihr]{9} [noch]{10,11} und{12} [ruht euch aus]{13}? [Siehe]{14}, [die Stunde]{16,17} [ist nahe gekommen]{15}, und{18} [der Menschensohn]{19-22} [wird]{23} [in]{24} [die Hände]{25} [von Sündern]{26} [ausgeliefert]{23}.",
 "MAT.26.46": "[Steht auf]{1}, [lasst uns gehen]{2}! [Siehe]{3}, [der]{5} [mich]{7} [ausliefert]{6}, [ist nahe gekommen]{4}.»",
 "MAT.26.47": "Und{1} [noch]{2} [während er]{3} [redete]{4}, [siehe]{5}, [da kam]{10} [Judas]{6}, [einer]{7} [der]{8} [Zwölf]{9}, und{11} [mit]{12} [ihm]{13} [eine grosse]{15} [Menge]{14} [mit]{16} [Schwertern]{17} und{18} [Knüppeln]{19}, [von]{20} [den Hohepriestern]{21,22} und{23} [Ältesten]{24} [des Volkes]{25,26}.",
 "MAT.26.48": "[Der]{1} [ihn]{4} [auslieferte]{3}, [hatte]{5} [ihnen]{6} [aber]{2} [ein Zeichen]{7} [gegeben]{5} und [gesagt]{8}: «[Wen]{9,10} [ich]{11} [küssen werde]{11}, [der]{12} [ist es]{13}; [ergreift]{14} [ihn]{15}!»",
 "MAT.26.49": "Und{1} [sogleich]{2} [trat er]{3} [zu]{4} [Jesus]{5} [heran]{3} und [sagte]{6}: «[Sei gegrüsst]{7}, [Rabbi]{8}!», und{9} [küsste]{10} [ihn]{11}.",
 "MAT.26.50": "[Jesus]{1,3} [aber]{2} [sagte]{4} [zu ihm]{5}: «[Freund]{6}, tu, [wozu]{7,8} [du da bist]{9}!» [Da]{10} [traten sie heran]{11}, [legten]{12} [die Hände]{13,14} [an]{15} [Jesus]{16,17} und{18} [ergriffen]{19} [ihn]{20}.",
 "MAT.26.51": "Und{1} [siehe]{2}, [einer]{3} [von denen]{4}, die [mit]{5} [Jesus]{6} waren, [streckte]{7} [die Hand]{8,9} [aus]{7}, [zog]{10} [sein]{13} [Schwert]{11,12} und{14} [schlug]{15} [den Knecht]{16,17} [des Hohepriesters]{18,19} und [hieb]{20} [ihm]{21} [das Ohr]{22,23} [ab]{20}.",
 "MAT.26.52": "[Da]{1} [sagt]{2} [Jesus]{4,5} [zu ihm]{3}: «[Steck]{6} [dein]{9} [Schwert]{7,8} [zurück]{6} [an]{10} [seinen]{11,13} [Platz]{12}! [Denn]{15} [alle]{14}, [die]{16} [zum Schwert]{18} [greifen]{17}, [werden]{21} [durch]{19} [das Schwert]{20} [umkommen]{21}.",
 "MAT.26.53": "[Oder]{1} [meinst du]{2}, [ich könnte]{5} [meinen]{7,9} [Vater]{8} [nicht]{4} [bitten]{6}, und{10} [er würde]{11} [mir]{12} [jetzt]{13} [mehr als]{14} [zwölf]{15} [Legionen]{16} [Engel]{17} [zur Seite stellen]{11}? ~3(ὅτι leitet den Inhalt ein; nicht eigens wiedergegeben)",
 "MAT.26.54": "[Wie]{1} [würden]{3} [dann]{2} [die Schriften]{4,5} [erfüllt]{3}, [nach denen]{6} es [so]{7} [geschehen]{9} [muss]{8}?»",
 "MAT.26.55": "[In]{1} [jener]{2,3} [Stunde]{4} [sagte]{5} [Jesus]{6,7} [zu den]{8} [Menschenmengen]{9}: «[Wie]{10} [gegen]{11} [einen Räuber]{12} [seid ihr ausgezogen]{13} [mit]{14} [Schwertern]{15} und{16} [Knüppeln]{17}, [um]{18} [mich]{19} [festzunehmen]{18}? [Täglich]{20,21} [sass ich]{25} [im]{22,23} [Tempel]{24} und [lehrte]{26}, und{27} [ihr habt]{29} [mich]{30} [nicht]{28} [ergriffen]{29}.",
 "MAT.26.56": "[Das]{1} [alles]{3} [aber]{2} [ist geschehen]{4}, [damit]{5} [die Schriften]{7,8} [der Propheten]{9,10} [erfüllt würden]{6}.» [Da]{11} [verliessen]{15} [ihn]{16} [alle]{14} [Jünger]{12,13} und [flohen]{17}.",
 "MAT.26.57": "[Die]{1} [aber]{2}, die [Jesus]{4,5} [ergriffen hatten]{3}, [führten]{6} ihn [ab]{6} [zu]{7} [Kajafas]{8}, [dem Hohepriester]{9,10}, [wo]{11} [die Schriftgelehrten]{12,13} und{14} [die Ältesten]{15,16} [sich versammelt hatten]{17}.",
 "MAT.26.58": "[Petrus]{1,3} [aber]{2} [folgte]{4} [ihm]{5} [von]{6} [ferne]{7} [bis]{8} [zum]{9} [Hof]{10} [des Hohepriesters]{11,12}, und{13} [er ging]{14} [hinein]{15} und [sass]{16} [bei]{17} [den Dienern]{18,19}, [um]{20} [den Ausgang]{21,22} [zu sehen]{20}.",
 "MAT.26.59": "[Die Hohepriester]{1,3} [aber]{2} und{4} [der]{5} [ganze]{7} [Hohe Rat]{6} [suchten]{8} [ein falsches Zeugnis]{9} [gegen]{10} [Jesus]{11,12}, [um]{13} [ihn]{14} [zu töten]{15},",
 "MAT.26.60": "und{1} [sie fanden]{3} [keines]{2}, [obwohl]{5} [viele]{4} [falsche Zeugen]{6} [herantraten]{5}. [Zuletzt]{7} [aber]{8} [traten]{9} [zwei]{10} [heran]{9}",
 "MAT.26.61": "und [sagten]{1}: «[Dieser]{2} [hat gesagt]{3}: ‹[Ich kann]{4} [den Tempel]{6,7} [Gottes]{8,9} [niederreissen]{5} und{10} [in]{11} [drei]{12} [Tagen]{13} [aufbauen]{14}.›»",
 "MAT.26.62": "Und{1} [der Hohepriester]{3,4} [stand auf]{2} und [sagte]{5} [zu ihm]{6}: «[Antwortest du]{8} [nichts]{7}? [Was]{9} [bezeugen]{12} [diese]{10} [gegen]{12} [dich]{11}?»",
 "MAT.26.63": "[Jesus]{1,3} [aber]{2} [schwieg]{4}. Und{5} [der Hohepriester]{6,7} [sagte]{8} [zu ihm]{9}: «[Ich beschwöre]{10} [dich]{11} [bei]{12} [dem]{13,15} [lebendigen]{16} [Gott]{14}, [dass]{17} [du]{19} [uns]{18} [sagst]{19}, [ob]{20} [du]{21} [der Christus]{23,24} [bist]{22}, [der Sohn]{25,26} [Gottes]{27,28}.»",
 "MAT.26.64": "[Jesus]{3,4} [sagt]{1} [zu ihm]{2}: «[Du]{5} [hast es gesagt]{6}. [Doch]{7} [ich sage]{8} [euch]{9}: [Von nun an]{10,11} [werdet ihr]{12} [den Menschensohn]{13-16} [zur]{18} [Rechten]{19} [der Macht]{20,21} [sitzen]{17} und{22} [auf]{24} [den Wolken]{25,26} [des Himmels]{27,28} [kommen]{23} [sehen]{12}.»",
 "MAT.26.65": "[Da]{1} [zerriss]{4} [der Hohepriester]{2,3} [seine]{7} [Gewänder]{5,6} und [sagte]{8}: «[Er hat gelästert]{9}! [Wozu]{10} [brauchen wir]{12,13} [noch]{11} [Zeugen]{14}? [Siehe]{15}, [jetzt]{16} [habt ihr]{17} [die Lästerung]{18,19} [gehört]{17}.",
 "MAT.26.66": "[Was]{1} [meint ihr]{2,3}?» [Sie]{4} [aber]{5} [antworteten]{6} und [sagten]{7}: «[Er hat]{10} [den Tod]{9} [verdient]{8}!»",
 "MAT.26.67": "[Da]{1} [spuckten sie]{2} [ihm]{6} [ins]{3,4} [Gesicht]{5} und{7} [schlugen]{8} [ihn]{9} [mit Fäusten]{8}; [andere]{10} [aber]{11} [ohrfeigten ihn]{12}",
 "MAT.26.68": "und [sagten]{1}: «[Weissage]{2} [uns]{3}, [Christus]{4}: [Wer]{5} [ist es]{6}, [der]{7} [dich]{9} [geschlagen hat]{8}?»",
 "MAT.26.69": "[Petrus]{1,3} [aber]{2} [sass]{4} [draussen]{5} [im]{6,7} [Hof]{8}. Und{9} [eine]{12} [Magd]{13} [trat]{10} [zu ihm]{11} [heran]{10} und [sagte]{14}: «[Auch]{15} [du]{16} [warst]{17} [mit]{18} [Jesus]{19}, [dem Galiläer]{20,21}!»",
 "MAT.26.70": "[Er]{1} [aber]{2} [leugnete]{3} [vor]{4} [allen]{5} und [sagte]{6}: «[Ich weiss]{8} [nicht]{7}, [was]{9} [du sagst]{10}.»",
 "MAT.26.71": "[Als er]{1} [aber]{2} [zum]{3,4} [Tor]{5} [hinausging]{1}, [sah]{6} [ihn]{7} [eine andere]{8} und{9} [sagt]{10} [zu denen]{11}, die [dort]{12} waren: «[Dieser]{13} [war]{14} [mit]{15} [Jesus]{16}, [dem Nazoräer]{17,18}!»",
 "MAT.26.72": "Und{1} [wieder]{2} [leugnete er]{3} [mit]{4} [einem Eid]{5}: «[Ich kenne]{8} [den]{9} [Menschen]{10} [nicht]{7}!» ~6(ὅτι leitet die direkte Rede ein)",
 "MAT.26.73": "[Nach]{1} [kurzer Zeit]{2} [aber]{3} [traten]{4} [die Umstehenden]{5,6} [heran]{4} und [sagten]{7} [zu]{8} [Petrus]{9}: «[Wirklich]{10}, [auch]{11} [du]{12} [bist]{15} einer [von]{13} [ihnen]{14}; [denn]{17} [auch]{16} [deine]{20} [Sprechweise]{18,19} [verrät]{21,23} [dich]{22}!»",
 "MAT.26.74": "[Da]{1} [fing er an]{2}, [sich zu verfluchen]{3} und{4} [zu schwören]{5}: «[Ich kenne]{8} [den]{9} [Menschen]{10} [nicht]{7}!» Und{11} [sogleich]{12} [krähte]{14} [ein Hahn]{13}. ~6(ὅτι leitet die direkte Rede ein)",
 "MAT.26.75": "Und{1} [Petrus]{3,4} [erinnerte sich]{2} [an das]{5} [Wort]{6}, das [Jesus]{7} [gesagt hatte]{8}: «[Bevor]{10} [ein Hahn]{11} [kräht]{12}, [wirst du]{14} [mich]{15} [dreimal]{13} [verleugnen]{14}.» Und{16} [er ging]{17} [hinaus]{18} und [weinte]{19} [bitterlich]{20}. ~9(ὅτι leitet die direkte Rede ein)",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 26
 "MAT.26.1": "Und{1} [es isch gscheh]{2}: [Wo]{3} [de Jesus]{5,6} [mit]{4} [all]{7} [dene]{8,10} [Wort]{9} [fertig gsii isch]{4}, [hät er]{11} [zu]{12} [sine]{14} [Jünger]{13} [gseit]{11}:",
 "MAT.26.2": "«[Ir wüssed]{1}, [dass]{2} [in]{3} [zwei]{4} [Täg]{5} [s Passa]{6,7} [isch]{8}, und{9} [de Mänschesohn]{10-13} [wird usgliferet]{14}, [zum]{15,16} [gchrüüziget wärde]{17}.»",
 "MAT.26.3": "[Dänn]{1} [sind]{2} [d Hoheprieschter]{3,4} und{5} [d Ältischte]{6,7} [vom Volk]{8,9} [im]{10,11} [Hof]{12} [vom Hoheprieschter]{13,14}, [wo]{15} [Kajafas]{17} [gheisse hät]{16}, [zämechoo]{2}",
 "MAT.26.4": "und{1} [händ mitenand beraate]{2}, [wie]{3} [si]{7} [de Jesus]{4,5} [mit Lischt]{6} [chönted packe]{7} und{8} [umbringe]{9}.",
 "MAT.26.5": "[Si händ]{1} [aber]{2} [gseit]{1}: «[Nöd]{3} [am]{4,5} [Fäscht]{6}, [suscht]{7,8} [git s]{10} no [en Ufruer]{9} [im]{11,12} [Volk]{13}.»",
 "MAT.26.6": "[Wo]{4} [de Jesus]{1,3} [aber]{2} [z]{5} [Betanie]{6} [im]{7} [Huus]{8} [vom Simon]{9} [em Ussätzige]{10,11} [gsii isch]{4},",
 "MAT.26.7": "[isch]{1} [e Frau]{3} [mit]{4} [eme Alabaschtergfäss]{5} [voll]{6} [sehr tüürem]{7} [Salböl]{6} [zu ihm]{2} [härechoo]{1}, und{8} [si hät]{9} s [ihm]{13} [über]{10} [de]{11} [Chopf]{12} [gschüttet]{9}, [wo er am Tisch gläge isch]{14}.",
 "MAT.26.8": "[Wo]{1} [aber]{2} [d Jünger]{3,4} [das gseh händ]{1}, [händ si sich ufgregt]{5} und [gseit]{6}: «[Für was]{7,8} [die]{11} [Verschwändig]{9,10}?",
 "MAT.26.9": "[Mer hett]{1} [das]{3} [nämli]{2} [für vil Gäld]{5} [verchaufe]{4} und{6} [de Arme]{8} [gää]{7} [chöne]{1}.»",
 "MAT.26.10": "[De Jesus]{3,4} [aber]{2} [hät das gmerkt]{1} und [zu ine]{6} [gseit]{5}: «[Werum]{7} [mached ir]{9} [de]{10} [Frau]{11} [Chummer]{8}? [Si hät]{15} [nämli]{13} [es guets]{14} [Wärch]{12} [a]{16} [mir]{17} [taa]{15}.",
 "MAT.26.11": "[Dänn]{2} [d Arme]{3,4} [händ ir]{5} [immer]{1} [bi]{6} [eu]{7}, [mich]{8} [aber]{9} [händ ir]{12} [nöd]{10} [immer]{11}.",
 "MAT.26.12": "[Dänn]{2} [wo]{1} [die]{3} [das]{4,6} [Salböl]{5} [uf]{7} [min]{8,10} [Liib]{9} [gschüttet hät]{1}, [hät si]{15} s [für]{11,12} [mini]{14} [Beerdigung]{13} [gmacht]{15}.",
 "MAT.26.13": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Wo immer]{4,5} [das]{9} [Evangelium]{7,8} [verchündet wird]{6} [i]{10} [de]{12} [ganze]{11} [Wält]{13}, [dört wird]{14} [au]{15} [verzellt]{14}, [was]{16} [die]{18} [gmacht hät]{17}, [zur]{19} [Erinnerig a si]{20,21}.»",
 "MAT.26.14": "[Dänn]{1} [isch]{2} [eine]{3} [vo de]{4} [Zwölf]{5}, [wo]{6} [Judas]{8} [Iskariot]{9} [gheisse hät]{7}, [zu]{10} [de Hoheprieschter]{11,12} [gange]{2}",
 "MAT.26.15": "und [hät gseit]{1}: «[Was]{2} [wänd ir]{3} [mir]{4} [gää]{5}? [Dänn]{6} [lifere]{8} [ich]{6} [en]{9} [eu]{7} [us]{8}.» [Si]{10} [aber]{11} [händ]{12} [ihm]{13} [driissg]{14} [Silberstück]{15} [abgwoge]{12}.",
 "MAT.26.16": "Und{1} [vo dänn aa]{2,3} [hät er]{4} [e günschtigi Glägeheit]{5} [gsuecht]{4}, [zum]{6} [en]{7} [uslifere]{8}.",
 "MAT.26.17": "[Am]{1} [erschte Tag]{3} [vo de ungsüürete Broot]{4,5} [aber]{2} [sind]{6} [d Jünger]{7,8} [zum]{9} [Jesus]{10} [härechoo]{6} und [händ gseit]{11}: «[Wo]{12} [wottsch]{13}, [dass mer]{14} [dir]{15} alles [vorbereited]{14}, [damit du]{16} [s Passa]{17,18} [chasch ässe]{16}?»",
 "MAT.26.18": "[Er]{1} [aber]{2} [hät gseit]{3}: «[Gönd]{4} [i]{5} [d Stadt]{6,7} [zum]{8,9} [Soundso]{10} und{11} [säged]{12} [zu ihm]{13}: ‹[De Lehrer]{14,15} [seit]{16}: [Mini]{19} [Ziit]{17,18} [isch]{21} [nöch]{20}; [bi]{22} [dir]{23} [fiir ich]{24} [s Passa]{25,26} [mit]{27} [mine]{28,30} [Jünger]{29}.›»",
 "MAT.26.19": "Und{1} [d Jünger]{3,4} [händ gmacht]{2}, [wie]{5} [de Jesus]{8,9} [ine]{7} [ufgtreit hät]{6}, und{10} [händ]{11} [s Passa]{12,13} [vorbereitet]{11}.",
 "MAT.26.20": "[Wo]{3} s [aber]{2} [Aabig]{1} [worde isch]{3}, [isch er]{4} [mit]{5} [de]{6} [zwölf]{7} [Jünger]{8} [am Tisch gläge]{4}.",
 "MAT.26.21": "Und{1} [während]{2} [si]{3} [ggässe händ]{2}, [hät er gseit]{4}: «[Amen]{5}, [ich säg]{6} [eu]{7}: [Eine]{9} [vo]{10} [eu]{11} [wird]{12} [mich]{13} [uslifere]{12}.» ~8(ὅτι leitet di diräkt Red ii)",
 "MAT.26.22": "Und{1} [si sind]{2} [fescht]{3} [truurig worde]{2} und [händ aagfange]{4}, [zu ihm]{6} [z säge]{5}, [jede einzelne]{7,8}: «[Ich]{10} [bi s]{11} [doch nöd]{9}, [Herr]{12}?»",
 "MAT.26.23": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: «[Dä, wo]{5} [mit]{7} [mir]{8} [d Hand]{9,10} [i]{11} [d Schüssle]{12,13} [tunkt hät]{6}, [dä]{14} [wird]{16} [mich]{15} [uslifere]{16}.",
 "MAT.26.24": "[De Mänschesohn]{1,3,4,5} [gaat]{6} [zwar]{2} [dethii]{6}, [wie]{7} s [über]{9} [en]{10} [gschribe staat]{8}; [weh]{11} [aber]{12} [säbem]{13,15} [Mänsch]{14}, [dur]{16} [dä]{17} [de Mänschesohn]{18-21} [usgliferet wird]{22}! [Es wär]{24} [guet]{23} [für en]{25}, [wänn]{26} [säbe]{29,31} [Mänsch]{30} [nöd]{27} [gebore worde wär]{28}.»",
 "MAT.26.25": "[De Judas]{3} [aber]{2}, [wo]{4} [en]{6} [usgliferet hät]{5}, [hät gantwortet]{1} und [gseit]{7}: «[Ich]{9} [bi s]{10} [doch nöd]{8}, [Rabbi]{11}?» [Er seit]{12} [zu ihm]{13}: «[Du]{14} [häsch es gseit]{15}.»",
 "MAT.26.26": "[Während]{1} [si]{3} [aber]{2} [ggässe händ]{1}, [hät]{4} [de Jesus]{5,6} [Broot]{7} [gnoo]{4} und{8} [de Lobpriis gsproche]{9}, [hät s broche]{10} und{11} [de Jünger]{13,14} [gää]{12} und [gseit]{15}: «[Nämed]{16}, [ässed]{17}! [Das]{18} [isch]{19} [min]{22} [Liib]{20,21}.»",
 "MAT.26.27": "Und{1} [er hät]{2} [en Bächer]{3} [gnoo]{2} und{4} [s Dankgebätt gsproche]{5}, [hät]{6} en [ine]{7} [gää]{6} und [gseit]{8}: «[Trinked]{9} [alli]{12} [drus]{10,11}!",
 "MAT.26.28": "[Dänn]{2} [das]{1} [isch]{3} [mis]{6} [Bluet]{4,5} [vom Bund]{7,8}, [wo]{9} [für]{10} [vili]{11} [vergosse wird]{12} [zur]{13} [Vergäbig]{14} [vo de Sünde]{15}.",
 "MAT.26.29": "[Ich säg]{1} [eu]{3} [aber]{2}: [Ich wirde]{6} [vo jetzt aa]{7,8} [sicher nümme]{4,5} [vo]{9} [dem]{10} [Gwächs]{11,12} [vom Wiistock]{13,14} [trinke]{6} [bis]{15} [zu säbem]{16,18} [Tag]{17}, [wo]{19} [ich]{21} [s]{20} [mit]{22} [eu]{23} [nöi]{24} [trinke]{21} [im]{25,26} [Riich]{27} [vo mim]{30} [Vatter]{28,29}.»",
 "MAT.26.30": "Und{1} [nachdem si de Lobgsang gsunge händ]{2}, [sind si usegange]{3} [uf de]{4,5} [Ölberg]{6-8}.",
 "MAT.26.31": "[Dänn]{1} [seit]{2} [de Jesus]{4,5} [zu ine]{3}: «[Ir]{7} [alli]{6} [wärded]{8} [i]{11} [dere]{12,14} [Nacht]{13} [a]{9} [mir]{10} [Aastoss nää]{8}; [es staat]{15} [nämli]{16} [gschribe]{15}: ‹[Ich wirde]{17} [de Hirt]{18,19} [schlaa]{17}, und{20} [d Schaf]{22,23} [vo de Herde]{24,25} [wärded verstreut]{21}.›",
 "MAT.26.32": "[Nachdem]{1,3} [ich]{5} [aber]{2} [uferweckt worde bi]{4}, [gang ich]{6} [eu]{7} [nach]{8,9} [Galiläa]{10} [voruus]{6}.»",
 "MAT.26.33": "[De Petrus]{3,4} [aber]{2} [hät gantwortet]{1} und [zu ihm]{6} [gseit]{5}: «[Wänn]{7} [alli]{8} [a]{10} [dir]{11} [Aastoss nämed]{9} – [ich]{12} [nimm]{14} [nie]{13} [Aastoss]{14}!»",
 "MAT.26.34": "[De Jesus]{3,4} [hät]{1} [zu ihm]{2} [gseit]{1}: «[Amen]{5}, [ich säg]{6} [dir]{7}: [I]{9} [dere]{10,11} [Nacht]{12}, [bevor]{13} [en Güggel]{14} [chräit]{15}, [wirsch du]{17} [mich]{18} [drüümal]{16} [verleugne]{17}.» ~8(ὅτι leitet di diräkt Red ii)",
 "MAT.26.35": "[De Petrus]{3,4} [seit]{1} [zu ihm]{2}: «[Au wänn]{5} [ich]{7} [mit]{8} [dir]{9} [sterbe]{10} [müesst]{6}, [ich wirde]{14} [dich]{13} [sicher nöd]{11,12} [verleugne]{14}!» [Gnau so]{15} [händ]{20} [au]{16} [alli]{17} [Jünger]{18,19} [gredt]{20}.",
 "MAT.26.36": "[Dänn]{1} [chunnt]{2} [de Jesus]{5,6} [mit]{3} [ine]{4} [zu]{7} [eme Grundstück]{8}, [wo]{9} [Getsemani]{10} [heisst]{9}, und{11} [seit]{12} [zu de]{13} [Jünger]{14}: «[Sitzed]{15} [da]{16} [ane]{15}, [solang]{17,18} [ich]{21} [dört äne]{20} [gang]{19} [go bätte]{21}.»",
 "MAT.26.37": "Und{1} [er hät]{2} [de Petrus]{3,4} und{5} [di]{6} [zwei]{7} [Söhn]{8} [vom Zebedäus]{9} [mitgnoo]{2} und [hät aagfange]{10}, [truurig z wärde]{11} und{12} [Angscht z ha]{13}.",
 "MAT.26.38": "[Dänn]{1} [seit er]{2} [zu ine]{3}: «[Ganz fescht truurig]{4} [isch]{5} [mini]{8} [Seel]{6,7}, [bis]{9} [zum Tod]{10}. [Bliibed]{11} [da]{12} und{13} [wached]{14} [mit]{15} [mir]{16}!»",
 "MAT.26.39": "Und{1} [er isch]{2} [es Stückli]{3} [wiitergange]{2}, [isch]{4} [uf]{5} [sis]{7} [Gsicht]{6} [gfalle]{4}, [hät bätet]{8} und{9} [gseit]{10}: «[Min]{12} [Vatter]{11}, [wänn]{13} s [möglich]{14} [isch]{15}, [söll]{16} [dä]{19,21} [Bächer]{20} [a]{17} [mir]{18} [verbiigaa]{16}! [Aber]{22} [nöd]{23}, [wie]{24} [ich]{25} [wott]{26}, [sondern]{27} [wie]{28} [du]{29} wottsch.»",
 "MAT.26.40": "Und{1} [er chunnt]{2} [zu]{3} [de Jünger]{4,5} und{6} [findt]{7} [si]{8} [am Schlaafe]{9}, und{10} [er seit]{11} [zum]{12} [Petrus]{13}: «[So]{14} [händ ir]{16} s [nöd]{15} [gschafft]{16}, [ei]{17} [Stund]{18} [mit]{20} [mir]{21} [wach z bliibe]{19}?",
 "MAT.26.41": "[Wached]{1} und{2} [bätted]{3}, [damit]{4} [ir]{6} [nöd]{5} [i]{7} [Versuechig]{8} [chömed]{6}! [De Geischt]{9,11} isch [zwar]{10} [willig]{12}, [s Fleisch]{13,15} [aber]{14} [schwach]{16}.»",
 "MAT.26.42": "[Wider]{1} [isch er]{4} [zum zweite Mal]{2,3} [wäggange]{4}, [hät bätet]{5} und [gseit]{6}: «[Min]{8} [Vatter]{7}, [wänn]{9} [das]{12} [nöd]{10} [cha]{11} [verbiigaa]{13}, [ohni dass]{14,15} [ich]{17} [s]{16} [trinke]{17}, dänn [söll]{18} [diin]{21} [Wile]{19,20} [gschee]{18}.»",
 "MAT.26.43": "Und{1} [wo er]{2} [wider]{3} [choo isch]{2}, [hät er]{4} [si]{5} [schlaafend]{6} [aatroffe]{4}; [iri]{9} [Auge]{10,11} [sind]{7} [nämli]{8} [schwär]{12} [gsii]{7}.",
 "MAT.26.44": "Und{1} [er hät]{2} [si]{3} [la sii]{2}, [isch]{5} [wider]{4} [wäggange]{5} und [hät]{6} [zum dritte Mal]{7,8} [bätet]{6} und [nomal]{13} [di gliiche]{9,10} [Wort]{11} [gseit]{12}.",
 "MAT.26.45": "[Dänn]{1} [chunnt er]{2} [zu]{3} [de Jünger]{4,5} und{6} [seit]{7} [zu ine]{8}: «[Schlaafed ir]{9} [no]{10,11} und{12} [ruehed eu us]{13}? [Lueg]{14}, [d Stund]{16,17} [isch nöch]{15}, und{18} [de Mänschesohn]{19-22} [wird]{23} [i]{24} [d Händ]{25} [vo Sünder]{26} [usgliferet]{23}.",
 "MAT.26.46": "[Stönd uf]{1}, [mir gönd]{2}! [Lueg]{3}, [dä, wo]{5} [mich]{7} [usliferet]{6}, [isch nöch]{4}.»",
 "MAT.26.47": "Und{1} [no]{2} [während er]{3} [gredt hät]{4}, [lueg]{5}, [da isch]{10} [de Judas]{6} [choo]{10}, [eine]{7} [vo de]{8} [Zwölf]{9}, und{11} [mit]{12} [ihm]{13} [e grossi]{15} [Mängi]{14} [mit]{16} [Schwärter]{17} und{18} [Chnüppel]{19}, [vo]{20} [de Hoheprieschter]{21,22} und{23} [Ältischte]{24} [vom Volk]{25,26}.",
 "MAT.26.48": "[Dä, wo]{1} [en]{4} [usgliferet hät]{3}, [hät]{5} [ine]{6} [aber]{2} [es Zeiche]{7} [gää]{5} und [gseit]{8}: «[Dä, wo]{9,10} [ich]{11} [küsse]{11}, [dä]{12} [isch es]{13}; [packed]{14} [en]{15}!»",
 "MAT.26.49": "Und{1} [grad]{2} [isch er]{3} [zum]{4} [Jesus]{5} [härechoo]{3} und [hät gseit]{6}: «[Grüess di]{7}, [Rabbi]{8}!», und{9} [hät]{10} [en]{11} [küsst]{10}.",
 "MAT.26.50": "[De Jesus]{1,3} [aber]{2} [hät]{4} [zu ihm]{5} [gseit]{4}: «[Fründ]{6}, mach, [für was]{7,8} [du da bisch]{9}!» [Dänn]{10} [sind si härechoo]{11}, [händ]{12} [d Händ]{13,14} [a]{15} [de Jesus]{16,17} [gleit]{12} und{18} [händ]{19} [en]{20} [packt]{19}.",
 "MAT.26.51": "Und{1} [lueg]{2}, [eine]{3} [vo dene]{4}, wo [mit]{5} [em Jesus]{6} gsii sind, [hät]{7} [d Hand]{8,9} [usgstreckt]{7}, [hät]{10} [sis]{13} [Schwärt]{11,12} [zoge]{10} und{14} [de Chnächt]{16,17} [vom Hoheprieschter]{18,19} [troffe]{15} und [ihm]{21} [s Oor]{22,23} [abghaue]{20}.",
 "MAT.26.52": "[Dänn]{1} [seit]{2} [de Jesus]{4,5} [zu ihm]{3}: «[Steck]{6} [dis]{9} [Schwärt]{7,8} [zrugg]{6} [a]{10} [sin]{11,13} [Platz]{12}! [Alli]{14}, [wo]{16} [zum Schwärt]{18} [griifed]{17}, [chömed]{21} [nämli]{15} [dur]{19} [s Schwärt]{20} [um]{21}.",
 "MAT.26.53": "[Oder]{1} [meinsch]{2}, [ich chönt]{5} [mim]{7,9} [Vatter]{8} [nöd]{4} [rüefe]{6}, und{10} [er würd]{11} [mir]{12} [jetzt]{13} [meh als]{14} [zwölf]{15} [Legione]{16} [Ängel]{17} [schicke]{11}? ~3(ὅτι leitet de Inhalt ii; nöd eigens widergää)",
 "MAT.26.54": "[Wie]{1} [würded]{3} [dänn]{2} [d Schrifte]{4,5} [erfüllt]{3}, [wo säged, dass]{6} s [eso]{7} [mues]{8} [gscheh]{9}?»",
 "MAT.26.55": "[I]{1} [säbere]{2,3} [Stund]{4} [hät]{5} [de Jesus]{6,7} [zu de]{8} [Lüüt]{9} [gseit]{5}: «[Wie]{10} [gäge]{11} [en Röiber]{12} [sind ir uuszoge]{13} [mit]{14} [Schwärter]{15} und{16} [Chnüppel]{17}, [zum]{18} [mich]{19} [feschtnää]{18}? [Jede Tag]{20,21} [bin ich]{25} [im]{22,23} [Tämpel]{24} [gsässe]{25} und [ha glehrt]{26}, und{27} [ir händ]{29} [mich]{30} [nöd]{28} [packt]{29}.",
 "MAT.26.56": "[Das]{1} [alles]{3} [aber]{2} [isch gscheh]{4}, [damit]{5} [d Schrifte]{7,8} [vo de Prophete]{9,10} [erfüllt wärded]{6}.» [Dänn]{11} [händ]{15} [en]{16} [alli]{14} [Jünger]{12,13} [verlaa]{15} und [sind gflüchtet]{17}.",
 "MAT.26.57": "[Die]{1} [aber]{2}, wo [de Jesus]{4,5} [packt händ]{3}, [händ]{6} en [zum]{7} [Kajafas]{8}, [em Hoheprieschter]{9,10}, [abgfüert]{6}, [wo]{11} [d Schriftgelehrte]{12,13} und{14} [d Ältischte]{15,16} [zämechoo sind]{17}.",
 "MAT.26.58": "[De Petrus]{1,3} [aber]{2} [isch]{4} [ihm]{5} [vo]{6} [wiitem]{7} [nachegange]{4} [bis]{8} [zum]{9} [Hof]{10} [vom Hoheprieschter]{11,12}, und{13} [er isch]{14} [ine]{15} [gange]{14} und [isch]{16} [bi]{17} [de Diener]{18,19} [gsässe]{16}, [zum luege]{20}, [wie s usgaat]{21,22}.",
 "MAT.26.59": "[D Hoheprieschter]{1,3} [aber]{2} und{4} [de]{5} [ganz]{7} [Hoch Raat]{6} [händ]{8} [es falschs Zügnis]{9} [gäge]{10} [de Jesus]{11,12} [gsuecht]{8}, [zum]{13} [en]{14} [töte]{15},",
 "MAT.26.60": "und{1} [händ]{3} [keis]{2} [gfunde]{3}, [obwohl]{5} [vili]{4} [falschi Züüge]{6} [härechoo sind]{5}. [Zletscht]{7} [aber]{8} [sind]{9} [zwei]{10} [härechoo]{9}",
 "MAT.26.61": "und [händ gseit]{1}: «[Dä]{2} [hät gseit]{3}: ‹[Ich cha]{4} [de Tämpel]{6,7} [vo Gott]{8,9} [abriisse]{5} und{10} [in]{11} [drüü]{12} [Täg]{13} [ufbaue]{14}.›»",
 "MAT.26.62": "Und{1} [de Hoheprieschter]{3,4} [isch ufgstande]{2} und [hät]{5} [zu ihm]{6} [gseit]{5}: «[Antwortisch]{8} [nüüt]{7}? [Was]{9} [säged]{12} [die]{10} [gäge]{12} [dich]{11} [uus]{12}?»",
 "MAT.26.63": "[De Jesus]{1,3} [aber]{2} [hät gschwige]{4}. Und{5} [de Hoheprieschter]{6,7} [hät]{8} [zu ihm]{9} [gseit]{8}: «[Ich beschwör]{10} [dich]{11} [bim]{12,13,15} [läbige]{16} [Gott]{14}, [dass]{17} [du]{19} [üs]{18} [seisch]{19}, [öb]{20} [du]{21} [de Christus]{23,24} [bisch]{22}, [de Sohn]{25,26} [vo Gott]{27,28}.»",
 "MAT.26.64": "[De Jesus]{3,4} [seit]{1} [zu ihm]{2}: «[Du]{5} [häsch es gseit]{6}. [Aber]{7} [ich säg]{8} [eu]{9}: [Vo jetzt aa]{10,11} [wärded ir]{12} [de Mänschesohn]{13-16} [zur]{18} [Rächte]{19} [vo de Macht]{20,21} [gseh]{12} [sitze]{17} und{22} [uf]{24} [de Wolche]{25,26} [vom Himel]{27,28} [choo]{23}.»",
 "MAT.26.65": "[Dänn]{1} [hät]{4} [de Hoheprieschter]{2,3} [sini]{7} [Chleider]{5,6} [verrisse]{4} und [gseit]{8}: «[Er hät gläschteret]{9}! [Für was]{10} [bruuched mer]{12,13} [no]{11} [Züüge]{14}? [Lueg]{15}, [jetzt]{16} [händ ir]{17} [d Läschterig]{18,19} [ghört]{17}.",
 "MAT.26.66": "[Was]{1} [meined ir]{2,3}?» [Si]{4} [aber]{5} [händ gantwortet]{6} und [gseit]{7}: «[Er hät]{10} [de Tod]{9} [verdient]{8}!»",
 "MAT.26.67": "[Dänn]{1} [händ si]{2} [ihm]{6} [is]{3,4} [Gsicht]{5} [gspöit]{2} und{7} [en]{9} [mit de Füüscht]{8} [gschlage]{8}; [anderi]{10} [aber]{11} [händ em Chläpf gää]{12}",
 "MAT.26.68": "und [händ gseit]{1}: «[Weissag]{2} [üs]{3}, [Christus]{4}: [Wer]{5} [isch es]{6}, [wo]{7} [dich]{9} [gschlage hät]{8}?»",
 "MAT.26.69": "[De Petrus]{1,3} [aber]{2} [isch]{4} [dusse]{5} [im]{6,7} [Hof]{8} [gsässe]{4}. Und{9} [e]{12} [Magd]{13} [isch]{10} [zu ihm]{11} [härechoo]{10} und [hät gseit]{14}: «[Au]{15} [du]{16} [bisch]{17} [mit]{18} [em Jesus]{19} [gsii]{17}, [em Galiläer]{20,21}!»",
 "MAT.26.70": "[Er]{1} [aber]{2} [hät s]{3} [vor]{4} [allne]{5} [abgstritte]{3} und [gseit]{6}: «[Ich weiss]{8} [nöd]{7}, [was]{9} [du seisch]{10}.»",
 "MAT.26.71": "[Wo er]{1} [aber]{2} [zum]{3,4} [Tor]{5} [usgange isch]{1}, [hät]{6} [en]{7} [e anderi]{8} [gseh]{6} und{9} [seit]{10} [zu dene]{11}, wo [dört]{12} gsii sind: «[Dä]{13} [isch]{14} [mit]{15} [em Jesus]{16} [gsii]{14}, [em Nazoräer]{17,18}!»",
 "MAT.26.72": "Und{1} [wider]{2} [hät er s]{3} [mit]{4} [eme Eid]{5} [abgstritte]{3}: «[Ich kenn]{8} [dä]{9} [Mänsch]{10} [nöd]{7}!» ~6(ὅτι leitet di diräkt Red ii)",
 "MAT.26.73": "[Nach]{1} [ere churze Ziit]{2} [aber]{3} [sind]{4} [d Umstehende]{5,6} [härechoo]{4} und [händ]{7} [zum]{8} [Petrus]{9} [gseit]{7}: «[Würkli]{10}, [au]{11} [du]{12} [bisch]{15} eine [vo]{13} [ine]{14}; [dini]{20} [Spraach]{18,19} [verratet]{21,23} [dich]{22} [nämli]{17} [au]{16}!»",
 "MAT.26.74": "[Dänn]{1} [hät er aagfange]{2}, [sich z verflueche]{3} und{4} [z schwööre]{5}: «[Ich kenn]{8} [dä]{9} [Mänsch]{10} [nöd]{7}!» Und{11} [grad]{12} [hät]{14} [en Güggel]{13} [gchräit]{14}. ~6(ὅτι leitet di diräkt Red ii)",
 "MAT.26.75": "Und{1} [de Petrus]{3,4} [hät sich]{2} [as]{5} [Wort]{6} [erinneret]{2}, wo [de Jesus]{7} [gseit hät]{8}: «[Bevor]{10} [en Güggel]{11} [chräit]{12}, [wirsch du]{14} [mich]{15} [drüümal]{13} [verleugne]{14}.» Und{16} [er isch usegange]{17,18} und [hät]{19} [bitter]{20} [briegget]{19}. ~9(ὅτι leitet di diräkt Red ii)",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MAT.26.1", "Und es geschah, als Jesus alle diese Worte beendet hatte", "literal", "Καὶ ἐγένετο ὅτε ἐτέλεσεν ὁ Ἰησοῦς πάντας τοὺς λόγους τούτους", None, ["Als Jesus alle diese Reden beendet hatte"],
  "Mit dieser Formel schliesst Matthäus seine fünf grossen Reden ab ([[MAT.7.28]], [[MAT.11.1]], [[MAT.13.53]], [[MAT.19.1]]). Nur hier steht «alle»: Die letzte Rede (Kapitel 24–25) ist zu Ende, die Leidensgeschichte beginnt. Die alttestamentlich klingende Einleitung «und es geschah» ist beibehalten."),
 ("MAT.26.2", "das Passa", "literal", "τὸ πάσχα", None, ["das Pessach", "das Passafest"],
  "πάσχα gibt das aramäische Wort für das Fest wieder, an dem Israel des Auszugs aus Ägypten gedenkt ([[EXO.12.1]]–[[EXO.12.14]]). Das Wort bezeichnet das Fest, das Mahl und das Lamm; hier das Fest, in [[MAT.26.17]]–[[MAT.26.19]] das Mahl."),
 ("MAT.26.2", "wird ausgeliefert", "literal", "παραδίδοται", None, ["wird verraten", "wird übergeben"],
  "Grundentscheid wie bei Markus: παραδίδωμι heisst «übergeben, ausliefern» und wird durchgehend so wiedergegeben, für Judas ([[MAT.26.15]], [[MAT.26.16]], [[MAT.26.21]]–[[MAT.26.25]], [[MAT.26.46]], [[MAT.26.48]]) ebenso wie in den Leidensansagen und später für die Hohepriester und Pilatus ([[MAT.27.2]], [[MAT.27.26]]). «Verraten» ist die vertraute Wiedergabe für Judas, lässt aber die Kette der Übergaben verschwinden. Das Präsens kündigt Kommendes als gewiss an."),
 ("MAT.26.2", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", None,
  "Einheitliche Wiedergabe für das ganze Matthäusevangelium. Die Wendung heisst hebräisch und aramäisch zunächst «Mensch»; bei Jesus ist sie Selbstbezeichnung, in [[MAT.26.64]] ausdrücklich mit Anklang an [[DAN.7.13]]."),
 ("MAT.26.3", "die Hohepriester", "traditional", "οἱ ἀρχιερεῖς", None, ["die Oberpriester", "die führenden Priester"],
  "Der Plural meint den amtierenden Hohepriester, frühere Amtsinhaber und die führenden Priesterfamilien. Einheitliche Wiedergabe für das ganze Buch."),
 ("MAT.26.3", "Hof", "literal", "αὐλὴν", None, ["Palast", "Amtssitz"],
  "αὐλή ist der Innenhof eines grossen Hauses, dann auch das ganze Anwesen. Die Übersetzung bleibt bei «Hof», damit der Ort in [[MAT.26.58]] und [[MAT.26.69]] (dasselbe Wort) wiedererkannt wird."),
 ("MAT.26.3", "Kajafas", "literal", "Καϊάφα", None, ["Kaiphas", "Kajaphas"],
  "Schreibung wie in den übrigen Arbeitsübersetzungen (z. B. Johannes). Nach Josephus war Kajafas etwa 18–36 n. Chr. Hohepriester."),
 ("MAT.26.4", "mit List", "literal", "δόλῳ", None, ["heimlich", "mit einer Hinterlist"], None),
 ("MAT.26.6", "Simons des Aussätzigen", "literal", "Σίμωνος τοῦ λεπροῦ", None, None,
  "Ob Simon noch krank oder (etwa von Jesus) geheilt war, sagt der Text nicht; der Beiname kann auch an eine frühere Krankheit erinnern."),
 ("MAT.26.7", "Alabastergefäss voll sehr kostbarem Salböl", "literal", "ἀλάβαστρον μύρου βαρυτίμου", "Alabaster von sehr kostbarem Salböl", ["Alabasterfläschchen mit teurem Parfüm"],
  "ἀλάβαστρον ist ein Fläschchen aus Alabaster für duftendes Öl. Anders als [[MRK.14.3]] nennt Matthäus weder Narde noch das Zerbrechen des Gefässes."),
 ("MAT.26.7", "während er zu Tisch lag", "adapted", "ἀνακειμένου", "liegend", ["während er bei Tisch sass"],
  "Bei festlichen Mahlzeiten lag man nach griechisch-römischer Sitte auf Polstern um den Tisch. Ebenso [[MAT.26.20]]."),
 ("MAT.26.7", "zu ihm heran", "literal", "προσῆλθεν αὐτῷ", None, ["kam zu ihm"],
  "Gemeinsame Wiedergabe für das Matthäusevangelium: προσέρχομαι «herantreten»; ebenso [[MAT.26.17]], [[MAT.26.49]], [[MAT.26.50]], [[MAT.26.60]], [[MAT.26.69]] und [[MAT.26.73]]. In [[MAT.26.60]] ist das Vortreten der Zeugen vor dem Rat gemeint."),
 ("MAT.26.10", "Verdruss", "adapted", "κόπους παρέχετε", "Mühen bereitet ihr", ["Warum macht ihr der Frau Schwierigkeiten?", "Warum kränkt ihr die Frau?"], None),
 ("MAT.26.10", "ein gutes Werk", "literal", "ἔργον καλὸν", None, ["eine schöne Tat"],
  "καλός heisst «schön» und «gut»; die Wendung wie in [[MAT.5.16]] («gute Werke»)."),
 ("MAT.26.12", "für mein Begräbnis", "adapted", "πρὸς τὸ ἐνταφιάσαι με", "um mich zu bestatten", ["zur Vorbereitung meines Begräbnisses"],
  "Jesus deutet die Salbung auf sein Begräbnis. In [[MAT.28.1]] gehen die Frauen nicht zum Salben, sondern um nach dem Grab zu sehen; die Salbung des Leichnams ist damit gleichsam vorweggenommen."),
 ("MAT.26.13", "Amen, ich sage euch", "literal", "ἀμὴν λέγω ὑμῖν", None, ["Wahrlich, ich sage euch"],
  "Einheitliche Wiedergabe für das ganze Matthäusevangelium; ebenso «Amen, ich sage dir» ([[MAT.26.34]]). ἀμήν ist ein hebräisches Wort der Bekräftigung; ungewöhnlich ist, dass Jesus es seinen eigenen Worten voranstellt."),
 ("MAT.26.13", "Evangelium", "traditional", "εὐαγγέλιον", None, ["gute Nachricht", "frohe Botschaft"], None),
 ("MAT.26.15", "Dann werde ich ihn euch ausliefern", "adapted", "κἀγὼ ὑμῖν παραδώσω αὐτόν", "und ich werde ihn euch ausliefern", None,
  "καί verbindet Angebot und Gegenleistung; «dann» macht das im Deutschen deutlich."),
 ("MAT.26.15", "wogen ihm dreissig Silberstücke ab", "interpretive", "ἔστησαν αὐτῷ τριάκοντα ἀργύρια", None, ["setzten ihm dreissig Silberstücke fest", "zahlten ihm dreissig Silberstücke aus"],
  "ἵστημι heisst hier entweder «abwägen» (Geld wurde gewogen) oder «festsetzen». Die Wendung entspricht der griechischen Fassung von [[ZEC.11.12]] (ἔστησαν … τριάκοντα ἀργυροῦς), auf die [[MAT.27.9]]–[[MAT.27.10]] ausdrücklich anspielt; deshalb «wogen ab». Dreissig Silberstücke nennt auch [[EXO.21.32]] als Ersatz für einen getöteten Sklaven."),
 ("MAT.26.17", "ersten Tag der Ungesäuerten Brote", "adapted", "Τῇ πρώτῃ τῶν ἀζύμων", "am ersten der Ungesäuerten", ["am ersten Tag des Festes der Ungesäuerten Brote"],
  "τὰ ἄζυμα («die ungesäuerten [Brote]») ist der Name des siebentägigen Festes, das an das Passa anschliesst ([[LEV.23.5]]–[[LEV.23.6]]); «Tag» und «Brote» sind ergänzt, wie bei [[MRK.14.12]]. Wie sich der Tag zum Passatermin genau verhält, wird diskutiert."),
 ("MAT.26.18", "zu dem und dem", "literal", "πρὸς τὸν δεῖνα", None, ["zu einem gewissen Mann"],
  "ὁ δεῖνα bezeichnet eine Person, deren Name nicht genannt wird. Matthäus erzählt knapper als [[MRK.14.13]]–[[MRK.14.15]] (ohne den Mann mit dem Wasserkrug)."),
 ("MAT.26.18", "Meine Zeit", "literal", "Ὁ καιρός μου", None, ["Meine Stunde"],
  "καιρός ist der bestimmte, entscheidende Zeitpunkt; gemeint ist das bevorstehende Leiden (vgl. [[MAT.26.45]]: «die Stunde»)."),
 ("MAT.26.18", "halte ich das Passa", "adapted", "ποιῶ τὸ πάσχα", "mache ich das Passa", ["feiere ich das Passa"],
  "Präsens mit Zukunftssinn."),
 ("MAT.26.20", "lag er mit den zwölf Jüngern zu Tisch", "literal", "ἀνέκειτο μετὰ τῶν δώδεκα μαθητῶν", None, ["lag er mit den Zwölf zu Tisch"],
  "Der SBLGNT liest mit WH μαθητῶν; Treg, NA28 und RP haben nur «mit den Zwölf» (siehe Alternative)."),
 ("MAT.26.22", "Ich bin es doch nicht, Herr?", "interpretive", "Μήτι ἐγώ εἰμι, κύριε", "Doch nicht ich bin es, Herr?", ["Bin ich es etwa, Herr?"],
  "Mit μήτι erwartet die Frage ein Nein. Die Jünger reden Jesus mit «Herr» an, Judas in [[MAT.26.25]] mit «Rabbi»; viele sehen darin eine bewusste Unterscheidung des Evangelisten."),
 ("MAT.26.23", "getaucht hat", "literal", "ἐμβάψας", None, ["eintaucht"],
  "Partizip Aorist: Der Satz kann auf ein schon geschehenes Eintauchen zurückblicken oder allgemein jeden Tischgenossen meinen, der aus derselben Schüssel isst."),
 ("MAT.26.25", "Du hast es gesagt", "interpretive", "Σὺ εἶπας", None, ["Du sagst es", "Ja, du sagst es selbst"],
  "Die Antwort bejaht, legt aber die Aussage dem Fragenden in den Mund: Er hat selbst ausgesprochen, was zutrifft. Wie stark die Bejahung ist, wird unterschiedlich beurteilt. Dieselbe Antwort gibt Jesus dem Hohepriester ([[MAT.26.64]]); vgl. [[MAT.27.11]]."),
 ("MAT.26.26", "sprach den Lobpreis", "interpretive", "εὐλογήσας", "segnete", ["sprach den Segen", "dankte"],
  "Wie bei [[MRK.14.22]]: εὐλογέω entspricht dem jüdischen Tischsegen, der Gott über dem Brot preist. Ein Objekt fehlt; ob Gott gepriesen oder das Brot gesegnet wird, sagt der Text nicht ausdrücklich. Beim Becher steht εὐχαριστέω ([[MAT.26.27]])."),
 ("MAT.26.26", "Das ist mein Leib", "literal", "τοῦτό ἐστιν τὸ σῶμά μου", None, None,
  "Wörtlich belassen. Wie das «ist» zu verstehen ist (Gleichsetzung, Zeichen, Vergegenwärtigung), beantworten die kirchlichen Lehrtraditionen unterschiedlich; die Übersetzung entscheidet das nicht."),
 ("MAT.26.27", "einen Becher", "literal", "ποτήριον", None, ["einen Kelch"],
  "Wie bei Markus «Becher». Im Gebet in Getsemani ([[MAT.26.39]]) wird der Becher zum Bild für das zugemessene Geschick (vgl. [[MAT.20.22]])."),
 ("MAT.26.27", "sprach das Dankgebet", "adapted", "εὐχαριστήσας", "dankte", None, None),
 ("MAT.26.28", "mein Blut des Bundes", "literal", "τὸ αἷμά μου τῆς διαθήκης", None, ["mein Bundesblut"],
  "Nimmt das «Blut des Bundes» vom Sinai auf ([[EXO.24.8]]). διαθήκη ist hier «Bund», nicht «Testament» im Sinn eines letzten Willens. Das Wort «neu» (vgl. [[JER.31.31]]) steht nicht im SBLGNT-Text (siehe Alternative)."),
 ("MAT.26.28", "für viele", "literal", "περὶ πολλῶν", None, ["für alle"],
  "«Viele» kann im semitischen Sprachgebrauch die unzählbar Vielen im Gegenüber zu dem Einen meinen (vgl. [[ISA.53.12]], [[MAT.20.28]]) und ist dann keine Einschränkung. Beide Deutungen werden vertreten."),
 ("MAT.26.28", "zur Vergebung der Sünden", "literal", "εἰς ἄφεσιν ἁμαρτιῶν", None, None,
  "Nur Matthäus hat diesen Zusatz im Becherwort. Bei der Taufe des Johannes, wo [[MRK.1.4]] «zur Vergebung der Sünden» sagt, fehlt die Wendung bei Matthäus ([[MAT.3.11]])."),
 ("MAT.26.29", "von nun an", "literal", "ἀπʼ ἄρτι", None, ["ab jetzt"], "Ebenso [[MAT.26.64]]."),
 ("MAT.26.29", "im Reich meines Vaters", "literal", "ἐν τῇ βασιλείᾳ τοῦ πατρός μου", None, None,
  "Sonst spricht Matthäus meist vom «Reich der Himmel»; hier vom Reich «meines Vaters» (vgl. [[MAT.13.43]])."),
 ("MAT.26.30", "nachdem sie den Lobgesang gesungen hatten", "interpretive", "ὑμνήσαντες", "nachdem sie gesungen hatten", None,
  "Nach späterer jüdischer Überlieferung wurden am Passamahl die Hallel-Psalmen ([[PSA.113.1]]–[[PSA.118.29]]) gesungen. Ob genau diese gemeint sind, sagt der Text nicht."),
 ("MAT.26.31", "Anstoss nehmen", "interpretive", "σκανδαλισθήσεσθε", "zu Fall gebracht werden", ["zu Fall kommen", "irrewerden", "abfallen", "Ärgernis nehmen"],
  "σκανδαλίζω gehört zu σκάνδαλον «Stellholz einer Falle, Fallstrick»: im Glauben zu Fall kommen, sich von jemandem abwenden. Gemeinsame Wiedergabe für das Matthäusevangelium: aktiv «zu Fall bringen», passiv gegenüber einer Person (hier ἐν ἐμοί «an mir») «Anstoss nehmen an», sonst «zu Fall kommen». Ebenso [[MAT.26.33]], wo die zweite Form ohne Person auf die erste zurückgreift. Markus hat an der Parallelstelle «zu Fall kommen» ([[MRK.14.27]]). Das Zitat ist [[ZEC.13.7]]."),
 ("MAT.26.32", "auferweckt worden bin", "literal", "ἐγερθῆναί", None, ["auferstanden bin"],
  "Passiv von ἐγείρω «aufwecken»: Gott ist der Handelnde (vgl. [[MAT.28.6]]–[[MAT.28.7]])."),
 ("MAT.26.34", "ein Hahn kräht", "literal", "ἀλέκτορα φωνῆσαι", None, None,
  "Matthäus nennt einen Hahnenschrei, Markus zwei ([[MRK.14.30]], [[MRK.14.72]])."),
 ("MAT.26.34", "verleugnen", "literal", "ἀπαρνήσῃ", None, ["verneinen", "nicht kennen wollen"],
  "ἀπαρνέομαι «verleugnen, sich lossagen» (vgl. [[MAT.16.24]]: «sich selbst verleugnen»); das einfache ἀρνέομαι in [[MAT.26.70]] und [[MAT.26.72]] ist mit «leugnen» wiedergegeben."),
 ("MAT.26.36", "Getsemani", "literal", "Γεθσημανί", None, ["Gethsemane"],
  "Ein Grundstück am Ölberg; der Name wird meist als «Ölpresse» gedeutet. Schreibung wie bei Markus."),
 ("MAT.26.37", "sich zu ängstigen", "literal", "ἀδημονεῖν", None, ["in Angst zu geraten", "bange zu werden"], None),
 ("MAT.26.38", "Tief betrübt ist meine Seele bis zum Tod", "literal", "Περίλυπός ἐστιν ἡ ψυχή μου ἕως θανάτου", None, ["Ich bin zu Tode betrübt"],
  "Klingt an die Klage in [[PSA.42.5]] an. ψυχή meint hier das Innere, das ganze Selbst."),
 ("MAT.26.38", "wacht", "literal", "γρηγορεῖτε", None, ["bleibt wach"],
  "Leitwort der vorangehenden Rede ([[MAT.24.42]], [[MAT.25.13]]); in Getsemani dreimal ([[MAT.26.38]], [[MAT.26.40]], [[MAT.26.41]]). Nur Matthäus hat «mit mir»."),
 ("MAT.26.39", "fiel auf sein Gesicht", "literal", "ἔπεσεν ἐπὶ πρόσωπον αὐτοῦ", None, ["warf sich nieder"], None),
 ("MAT.26.39", "Mein Vater", "literal", "Πάτερ μου", None, None,
  "Markus hat das aramäische «Abba» ([[MRK.14.36]]); Matthäus «mein Vater», ebenso [[MAT.26.42]]."),
 ("MAT.26.39", "so gehe dieser Becher an mir vorüber", "literal", "παρελθάτω ἀπʼ ἐμοῦ τὸ ποτήριον τοῦτο", "es gehe vorüber von mir dieser Becher", ["lass diesen Becher an mir vorübergehen"],
  "Der Becher ist ein Bild für das zugemessene Geschick, in der Schrift auch für Gottes Gericht (vgl. [[ISA.51.17]], [[MAT.20.22]])."),
 ("MAT.26.40", "So wart ihr nicht imstande", "literal", "Οὕτως οὐκ ἰσχύσατε", None, ["Konntet ihr also nicht"],
  "Jesus spricht Petrus an, redet aber in der Mehrzahl: Gemeint sind alle drei."),
 ("MAT.26.41", "Versuchung", "interpretive", "πειρασμόν", None, ["Prüfung", "Anfechtung"],
  "Dasselbe Wort wie in der Vaterunser-Bitte [[MAT.6.13]] («führe uns nicht in Versuchung»)."),
 ("MAT.26.41", "das Fleisch", "literal", "σὰρξ", None, ["der Mensch", "die menschliche Natur"],
  "σάρξ steht hier für den schwachen, sterblichen Menschen, nicht für Sünde."),
 ("MAT.26.42", "so geschehe dein Wille", "literal", "γενηθήτω τὸ θέλημά σου", None, ["dein Wille soll geschehen"],
  "Wörtlich dieselben Worte wie die Vaterunser-Bitte [[MAT.6.10]]; die Übersetzung hält den Wortlaut gleich, damit der Anklang hörbar bleibt."),
 ("MAT.26.42", "Wieder ging er zum zweiten Mal weg", "literal", "πάλιν ἐκ δευτέρου ἀπελθὼν", None, ["Zum zweiten Mal ging er weg"],
  "Die doppelte Angabe «wieder, zum zweiten Mal» steht so im Griechischen."),
 ("MAT.26.44", "dieselben Worte", "adapted", "τὸν αὐτὸν λόγον", "dasselbe Wort", None, None),
 ("MAT.26.45", "Schlaft ihr noch und ruht euch aus?", "interpretive", "Καθεύδετε τὸ λοιπὸν καὶ ἀναπαύεσθε", None, ["Schlaft nur weiter und ruht euch aus!", "Schlaft ihr weiter und ruht euch aus?"],
  "Die Form kann Aussage, Frage oder Aufforderung sein; τὸ λοιπόν heisst «noch, weiterhin» oder «nun also». Als Frage (so hier, wie bei [[MRK.14.41]]) ist es ein Vorwurf; als Aufforderung wäre es Ironie oder Resignation. Der folgende Vers («Steht auf!») spricht eher für die Frage."),
 ("MAT.26.45", "von Sündern", "literal", "ἁμαρτωλῶν", None, ["der Sünder"], None),
 ("MAT.26.47", "Knüppeln", "literal", "ξύλων", "Hölzern", ["Stöcken"], "Wie bei Markus."),
 ("MAT.26.48", "hatte ihnen aber ein Zeichen gegeben", "adapted", "ἔδωκεν αὐτοῖς σημεῖον", "gab ihnen ein Zeichen", None,
  "Aorist; die Verabredung liegt vor dem Erzählten, deshalb Plusquamperfekt."),
 ("MAT.26.49", "Sei gegrüsst", "literal", "Χαῖρε", "Freue dich", ["Grüss dich"],
  "Der übliche griechische Gruss. Dasselbe Wort sagen die Soldaten beim Spott ([[MAT.27.29]]) und der Auferstandene zu den Frauen ([[MAT.28.9]])."),
 ("MAT.26.49", "küsste", "literal", "κατεφίλησεν", None, ["küsste innig"],
  "Das zusammengesetzte Verb kann einen herzlichen Kuss bezeichnen; ob Matthäus das betonen will, ist unsicher. In [[MAT.26.48]] steht das einfache φιλέω."),
 ("MAT.26.50", "Freund, tu, wozu du da bist!", "interpretive", "Ἑταῖρε, ἐφʼ ὃ πάρει", "Freund, wozu du da bist", ["Freund, wozu bist du gekommen?", "Freund, dazu bist du also da!"],
  "Der Satz ist verkürzt; ἐφʼ ὅ ist eigentlich kein Fragewort. Die meisten ergänzen eine Aufforderung («tu, wozu du gekommen bist»), andere lesen eine Frage oder einen Ausruf. «tu» ist ergänzt. ἑταῖρε «Freund, Kamerad» ist bei Matthäus eine distanzierte Anrede an jemanden, der im Unrecht ist ([[MAT.20.13]], [[MAT.22.12]])."),
 ("MAT.26.51", "einer von denen, die mit Jesus waren", "literal", "εἷς τῶν μετὰ Ἰησοῦ", None, None,
  "Matthäus nennt keinen Namen; [[JHN.18.10]] nennt Petrus und den Knecht Malchus."),
 ("MAT.26.51", "den Knecht", "traditional", "τὸν δοῦλον", "den Sklaven", ["den Diener"], None),
 ("MAT.26.52", "zum Schwert greifen", "adapted", "λαβόντες μάχαιραν", "das Schwert genommen haben", ["das Schwert ziehen"], None),
 ("MAT.26.53", "Legionen", "literal", "λεγιῶνας", None, None,
  "Eine römische Legion umfasste mehrere tausend Soldaten; zwölf Legionen sind ein Bild für eine unermesslich grosse Schar."),
 ("MAT.26.53", "jetzt", "literal", "ἄρτι", None, ["sogleich", "auf der Stelle"], None),
 ("MAT.26.54", "nach denen", "adapted", "ὅτι", "dass", None,
  "ὅτι leitet den Inhalt der Schriften ein: Sie sagen, dass es so geschehen muss."),
 ("MAT.26.55", "Menschenmengen", "literal", "ὄχλοις", "Mengen", ["Scharen", "Leuten"],
  "Gemeinsame Wiedergabe für das Matthäusevangelium: ὄχλος «die Menge» (in [[MAT.26.47]] die bewaffnete Menge), der Plural οἱ ὄχλοι «die Menschenmengen»."),
 ("MAT.26.55", "einen Räuber", "interpretive", "λῃστὴν", None, ["einen Banditen", "einen Aufständischen"],
  "λῃστής bezeichnet im 1. Jahrhundert oft bewaffnete Banden und Aufständische, nicht nur Diebe. Dasselbe Wort steht für die beiden Mitgekreuzigten ([[MAT.27.38]])."),
 ("MAT.26.55", "Tempel", "literal", "ἱερῷ", None, ["Tempelbezirk"],
  "ἱερόν ist der ganze Tempelbezirk; in [[MAT.26.61]] steht ναός, das Tempelhaus."),
 ("MAT.26.56", "Das alles aber ist geschehen", "interpretive", "τοῦτο δὲ ὅλον γέγονεν", None, None,
  "Ob der Satz noch zur Rede Jesu gehört oder eine Bemerkung des Erzählers ist, sagt der Text nicht. Dieselben Worte stehen als Erzählerbemerkung in [[MAT.1.22]]; hier lässt die Übersetzung die Rede bis zu diesem Satz laufen (vgl. [[MAT.26.54]]). Redaktionelle Entscheidung."),
 ("MAT.26.57", "die Schriftgelehrten", "traditional", "οἱ γραμματεῖς", None, ["die Schriftkundigen", "die Toragelehrten"], None),
 ("MAT.26.58", "den Dienern", "literal", "τῶν ὑπηρετῶν", None, ["den Wächtern", "den Gerichtsdienern"], None),
 ("MAT.26.58", "den Ausgang", "literal", "τὸ τέλος", None, ["das Ende", "wie es ausgehen würde"], None),
 ("MAT.26.59", "Hohe Rat", "traditional", "συνέδριον", None, ["Synedrium", "Ratsversammlung"],
  "Das jüdische Ratsgremium in Jerusalem unter Vorsitz des Hohepriesters."),
 ("MAT.26.59", "ein falsches Zeugnis", "literal", "ψευδομαρτυρίαν", None, ["eine falsche Aussage"],
  "Matthäus sagt von Anfang an, dass falsche Zeugenaussagen gesucht wurden; [[MRK.14.55]] spricht von «Zeugnis»."),
 ("MAT.26.61", "Ich kann den Tempel Gottes niederreissen", "literal", "Δύναμαι καταλῦσαι τὸν ναὸν τοῦ θεοῦ", None, None,
  "ναός ist das Tempelhaus. Bei Matthäus behaupten die Zeugen, Jesus habe von seinem Können gesprochen («ich kann»); bei [[MRK.14.58]] von einem Vorhaben («ich werde»). Vgl. [[JHN.2.19]]."),
 ("MAT.26.63", "Ich beschwöre dich", "literal", "Ἐξορκίζω σε", None, ["Ich nehme dich unter Eid"],
  "Feierliche Aufforderung, unter Anrufung Gottes die Wahrheit zu sagen."),
 ("MAT.26.63", "der Christus", "traditional", "ὁ χριστὸς", None, ["der Gesalbte", "der Messias"],
  "Einheitliche Wiedergabe für das ganze Buch. χριστός übersetzt hebräisch māšîaḥ «Gesalbter». Ebenso [[MAT.26.68]] als spöttische Anrede."),
 ("MAT.26.64", "Du hast es gesagt", "interpretive", "Σὺ εἶπας", None, ["Du sagst es", "Ja, du sagst es selbst"],
  "Wie [[MAT.26.25]]. Das folgende πλήν («doch») kann die Antwort einschränken (die Worte des Hohepriesters treffen zu, aber anders, als er meint) oder fortführen. Markus hat hier «Ich bin es» ([[MRK.14.62]])."),
 ("MAT.26.64", "Von nun an", "interpretive", "ἀπʼ ἄρτι", None, ["Ab jetzt", "Künftig"],
  "Die Zeitangabe sagt, dass das Gesehene mit dem jetzigen Geschehen beginnt; wie sie sich zum «Kommen auf den Wolken» verhält, wird verschieden gedeutet. Jesus verbindet [[PSA.110.1]] und [[DAN.7.13]]."),
 ("MAT.26.64", "zur Rechten der Macht", "literal", "ἐκ δεξιῶν τῆς δυνάμεως", None, ["zur Rechten Gottes"], "«Die Macht» umschreibt Gott."),
 ("MAT.26.65", "zerriss der Hohepriester seine Gewänder", "literal", "ὁ ἀρχιερεὺς διέρρηξεν τὰ ἱμάτια αὐτοῦ", None, None,
  "Zeichen der Trauer und des Entsetzens, hier über eine als Gotteslästerung gehörte Aussage."),
 ("MAT.26.65", "Er hat gelästert", "literal", "Ἐβλασφήμησεν", None, ["Er hat Gott gelästert"], None),
 ("MAT.26.66", "Er hat den Tod verdient", "adapted", "Ἔνοχος θανάτου ἐστίν", "Er ist des Todes schuldig", ["Er muss sterben"],
  "Der Genitiv «des Todes schuldig» ist heute ungebräuchlich; der Sinn ist, dass er nach ihrem Urteil die Todesstrafe verdient."),
 ("MAT.26.67", "andere aber", "interpretive", "οἱ δὲ", "die aber", ["sie aber"],
  "οἱ δέ kann neue Personen einführen oder dieselben weiter beschreiben."),
 ("MAT.26.67", "ohrfeigten ihn", "interpretive", "ἐράπισαν", None, ["schlugen ihn mit Stöcken"],
  "ῥαπίζω heisst ursprünglich «mit dem Stock schlagen», dann auch «ins Gesicht schlagen»; dasselbe Verb in [[MAT.5.39]]."),
 ("MAT.26.68", "Weissage", "literal", "Προφήτευσον", None, ["Prophezeie"],
  "Spott: Als angeblicher Prophet und Christus soll er sagen, wer ihn geschlagen hat. Matthäus erwähnt nicht, dass ihm das Gesicht verhüllt wurde ([[MRK.14.65]])."),
 ("MAT.26.69", "Magd", "literal", "παιδίσκη", None, ["Dienerin", "Sklavin"], None),
 ("MAT.26.71", "dem Nazoräer", "literal", "τοῦ Ναζωραίου", None, ["dem Nazarener", "aus Nazaret"],
  "Ναζωραῖος ist ein anderes Wort als Markus' Ναζαρηνός «Nazarener»; vgl. [[MAT.2.23]]. Die Übersetzung behält die Form bei."),
 ("MAT.26.71", "Tor", "literal", "πυλῶνα", None, ["Torweg", "Vorhalle"], None),
 ("MAT.26.72", "Ich kenne den Menschen nicht", "adapted", "Οὐκ οἶδα τὸν ἄνθρωπον", "Ich weiss den Menschen nicht", None,
  "οἶδα mit Person heisst «kennen». Ebenso [[MAT.26.74]]."),
 ("MAT.26.73", "deine Sprechweise verrät dich", "adapted", "ἡ λαλιά σου δῆλόν σε ποιεῖ", "deine Sprechweise macht dich offenkundig", ["deine Aussprache verrät dich"],
  "Gemeint ist die galiläische Aussprache."),
 ("MAT.26.74", "sich zu verfluchen", "interpretive", "καταθεματίζειν", None, ["zu fluchen", "ihn (Jesus) zu verfluchen"],
  "Das Verb hat kein Objekt. Gemeint sein kann eine Selbstverfluchung für den Fall, dass er lügt, oder eine Verfluchung Jesu."),
 ("MAT.26.75", "bitterlich", "literal", "πικρῶς", None, ["bitter"], None),
]

DEC_GSW = [
 ("MAT.26.1", "Und es isch gscheh", "literal", "Καὶ ἐγένετο", None, None,
  "Mit dere Formle schlüüsst de Matthäus sini füüf grosse Rede ab ([[MAT.7.28]], [[MAT.11.1]], [[MAT.13.53]], [[MAT.19.1]]); nu da staat «all»."),
 ("MAT.26.2", "wird usgliferet", "literal", "παραδίδοται", None, ["wird verrate"],
  "παραδίδωμι heisst «übergää, uslifere»; drum überall «uslifere», für de Judas wie für d Hoheprieschter und de Pilatus ([[MAT.27.2]], [[MAT.27.26]]), wie bim Markus."),
 ("MAT.26.2", "de Mänschesohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None,
  "Einheitlich fürs ganz Matthäusevangelium; Aaklang a [[DAN.7.13]] (lueg [[MAT.26.64]])."),
 ("MAT.26.5", "suscht git s no en Ufruer", "adapted", "ἵνα μὴ θόρυβος γένηται", "damit kei Ufruer entstaat", None, None),
 ("MAT.26.7", "zu ihm härechoo", "literal", "προσῆλθεν αὐτῷ", None, ["zu ihm choo"],
  "Gmeinsami Widergab fürs Matthäusevangelium: προσέρχομαι «härechoo»; gliich i [[MAT.26.17]], [[MAT.26.49]], [[MAT.26.50]], [[MAT.26.60]], [[MAT.26.69]] und [[MAT.26.73]]."),
 ("MAT.26.9", "Mer hett", "adapted", "ἐδύνατο πραθῆναι", "Das hett chöne verchauft wärde", None,
  "S Passiv isch i de Mundart mit «mer» widergää."),
 ("MAT.26.13", "Amen, ich säg eu", "literal", "ἀμὴν λέγω ὑμῖν", None, ["Würkli, ich säg eu"],
  "Einheitlich fürs ganz Matthäusevangelium; gliich «Amen, ich säg dir» ([[MAT.26.34]])."),
 ("MAT.26.15", "abgwoge", "interpretive", "ἔστησαν", None, ["feschtgsetzt", "uszahlt"],
  "ἵστημι heisst da «abwääge» oder «feschtsetze». D Wändig entspricht de griechische Fassig vo [[ZEC.11.12]], wo [[MAT.27.9]]–[[MAT.27.10]] druf aaspilt."),
 ("MAT.26.18", "zum Soundso", "literal", "πρὸς τὸν δεῖνα", None, ["zu eme gwüsse Maa"], "De Name wird nöd gnännt."),
 ("MAT.26.18", "fiir ich s Passa", "adapted", "ποιῶ τὸ πάσχα", "mach ich s Passa", None, None),
 ("MAT.26.25", "Du häsch es gseit", "interpretive", "Σὺ εἶπας", None, ["Du seisch es"],
  "D Antwort bejaht, leit aber d Ussag em Frogende is Muul. Gliich [[MAT.26.64]]."),
 ("MAT.26.26", "de Lobpriis gsproche", "interpretive", "εὐλογήσας", "hät gsägnet", ["hät dankt"],
  "Wie bim jüdische Tischsäge: Gott wird über em Broot globt. Wie [[MRK.14.22]]."),
 ("MAT.26.26", "Das isch min Liib", "literal", "τοῦτό ἐστιν τὸ σῶμά μου", None, None,
  "Wörtlich bhalte. Wie s «isch» z verstaa isch, beantworted di kirchliche Lehrtraditione verschide; d Übersetzig entscheidet das nöd."),
 ("MAT.26.28", "mis Bluet vom Bund", "literal", "τὸ αἷμά μου τῆς διαθήκης", None, None,
  "Nimmt s «Bluet vom Bund» vom Sinai uf ([[EXO.24.8]]). «Nöi» staat im SBLGNT nöd; lueg d Alternative."),
 ("MAT.26.28", "zur Vergäbig vo de Sünde", "literal", "εἰς ἄφεσιν ἁμαρτιῶν", None, None, "De Zuesatz hät nu de Matthäus."),
 ("MAT.26.31", "Aastoss nää", "interpretive", "σκανδαλισθήσεσθε", None, ["z Fall choo", "abfalle"],
  "Gmeinsami Widergab fürs ganz Matthäusevangelium: aktiv «z Fall bringe», passiv gägenüber ere Person (da «a mir») «Aastoss nää», susch «z Fall choo». Gliich i [[MAT.26.33]]. S Zitat isch [[ZEC.13.7]]."),
 ("MAT.26.34", "en Güggel", "adapted", "ἀλέκτορα", "en Hahn", None, "Wie bim Markus."),
 ("MAT.26.39", "söll dä Bächer a mir verbiigaa", "literal", "παρελθάτω ἀπʼ ἐμοῦ τὸ ποτήριον τοῦτο", None, None,
  "De Bächer isch es Bild für s Gschick, wo eim zuegmässe isch (vgl. [[MAT.20.22]])."),
 ("MAT.26.42", "söll diin Wile gschee", "literal", "γενηθήτω τὸ θέλημά σου", None, None,
  "Im Griechische gnau di gliiche Wort wie im Vaterunser ([[MAT.6.10]], dört «diin Wile söll gschee»); d Mundart bruucht drum di gliiche Wörter."),
 ("MAT.26.45", "Schlaafed ir no und ruehed eu us?", "interpretive", "Καθεύδετε τὸ λοιπὸν καὶ ἀναπαύεσθε", None, ["Schlaafed nu wiiter und ruehed eu us!"],
  "Cha Frag, Ussag oder Ufforderig sii; de nächscht Vers («Stönd uf!») spricht ehner für d Frag."),
 ("MAT.26.49", "Grüess di", "adapted", "Χαῖρε", "Fröi di", ["Sei grüesst"], "De gwöhnlich griechisch Gruess."),
 ("MAT.26.50", "Fründ, mach, für was du da bisch!", "interpretive", "Ἑταῖρε, ἐφʼ ὃ πάρει", "Fründ, für was du da bisch", ["Fründ, für was bisch choo?"],
  "De Satz isch verchürzt; «mach» isch ergänzt. Anderi läsed e Frag."),
 ("MAT.26.53", "Legione", "literal", "λεγιῶνας", None, None, "E römischi Legion hät mehreri tuusig Soldate gha."),
 ("MAT.26.55", "Lüüt", "adapted", "ὄχλοις", "Mängine", None, "Gmeinsami Widergab: ὄχλος «d Mängi» ([[MAT.26.47]]), de Plural οἱ ὄχλοι «d Lüüt»."),
 ("MAT.26.56", "Das alles aber isch gscheh", "interpretive", "τοῦτο δὲ ὅλον γέγονεν", None, None,
  "Öb de Satz no zur Red vom Jesus ghört oder de Erzäler das aamerkt, seit de Text nöd (gliichi Wort wie i [[MAT.1.22]]). Redaktionelle Entscheid."),
 ("MAT.26.57", "d Schriftgelehrte", "traditional", "οἱ γραμματεῖς", None, None, "Einheitlich fürs ganz Matthäusevangelium: «Schriftgelehrti», mit Artikel «d Schriftgelehrte»; gliich «Ältischti», «d Ältischte»."),
 ("MAT.26.59", "Hoch Raat", "traditional", "συνέδριον", None, ["Synedrium"], "S jüdisch Ratsgremium z Jerusalem."),
 ("MAT.26.63", "de Christus", "traditional", "ὁ χριστὸς", None, ["de Gsalbet", "de Messias"], None),
 ("MAT.26.64", "Vo jetzt aa", "interpretive", "ἀπʼ ἄρτι", None, ["Ab jetzt"], "De Jesus verbindet [[PSA.110.1]] und [[DAN.7.13]]."),
 ("MAT.26.66", "Er hät de Tod verdient", "adapted", "Ἔνοχος θανάτου ἐστίν", "er isch schuldig vom Tod", None,
  "D Mundart hät kei Genitiv; de Sinn isch: er mües stärbe."),
 ("MAT.26.67", "händ em Chläpf gää", "interpretive", "ἐράπισαν", None, ["händ en mit Stöck gschlage"], None),
 ("MAT.26.71", "em Nazoräer", "literal", "τοῦ Ναζωραίου", None, ["em Nazarener"],
  "Ναζωραῖος isch es anders Wort als bim Markus (Ναζαρηνός); vgl. [[MAT.2.23]]."),
 ("MAT.26.73", "dini Spraach verratet dich", "adapted", "ἡ λαλιά σου δῆλόν σε ποιεῖ", "dini Red macht dich offesichtlich", None,
  "Gmeint isch di galiläisch Uussprach."),
 ("MAT.26.74", "sich z verflueche", "interpretive", "καταθεματίζειν", None, ["en (de Jesus) z verflueche"], "S Verb hät keis Objekt."),
 ("MAT.26.75", "briegget", "adapted", "ἔκλαυσεν", "gweint", None, None),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung).
LACUNA_P45 = "𝔓45 ist hier nicht erhalten."
LACUNA_P45_G = "𝔓45 isch da nöd erhalte."
ALTS = [
 ("VAR-SBLGNTAPP-MAT-026-003-01:R2", "MAT.26.3", "die Hohepriester und die Ältesten des Volkes", "die Hohepriester und die Schriftgelehrten und die Ältesten des Volkes",
  "d Hoheprieschter und d Ältischte vom Volk", "d Hoheprieschter und d Schriftgelehrte und d Ältischte vom Volk", "gering",
  "Zu den Versammelten zählen auch die Schriftgelehrten.", "Bi de Versammlete sind au d Schriftgelehrte.",
  {"R1": [("ἀρχιερεῖς", "die Hohepriester", "WH, Treg, NA28")], "R2": [("ἀρχιερεῖς καὶ οἱ γραμματεῖς", "die Hohepriester und die Schriftgelehrten", "RP")]},
  {"R1": [("ἀρχιερεῖς", "d Hoheprieschter", "WH, Treg, NA28")], "R2": [("ἀρχιερεῖς καὶ οἱ γραμματεῖς", "d Hoheprieschter und d Schriftgelehrte", "RP")]},
  ["Die Schriftgelehrten können aus [[MRK.14.1]] und [[LUK.22.2]] ergänzt sein, wo sie genannt sind. Umgekehrt kann das Auge eines Abschreibers vom einen καὶ οἱ zum nächsten gesprungen sein, sodass die Worte ausfielen.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 05, 032 und 𝔓45 ohne den Zusatz; keine der zugeordneten Handschriften hat ihn. 04 ist hier nicht erhalten."],
  ["D Schriftgelehrte chönted us [[MRK.14.1]] und [[LUK.22.2]] ergänzt sii. Oder s Aug vo me Abschriiber isch vom eine καὶ οἱ zum nächschte gsprunge, und d Wort sind usgfalle.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 05, 032 und 𝔓45 ohni Zuesatz; keini vo de zueordnete Handschrifte hät en. 04 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-026-008-01:R2", "MAT.26.8", "die Jünger das aber sahen", "seine Jünger das aber sahen",
  "d Jünger das gseh händ", "sini Jünger das gseh händ", "gering",
  "Das Fürwort «seine» ist ergänzt.", "S Fürwort «sini» isch ergänzt.",
  {"R1": [("μαθηταὶ", "die Jünger", "WH, Treg, NA28")], "R2": [("μαθηταὶ αὐτοῦ", "seine Jünger", "RP")]},
  {"R1": [("μαθηταὶ", "d Jünger", "WH, Treg, NA28")], "R2": [("μαθηταὶ αὐτοῦ", "sini Jünger", "RP")]},
  ["«Seine Jünger» ist eine geläufige Verbindung und kann verdeutlichend ergänzt worden sein; ebenso kann das kurze Wort beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 05 und 𝔓45 ohne αὐτοῦ, 02 und 032 mit ihm; 04 ist hier nicht erhalten."],
  ["«Sini Jünger» isch e gläufigi Verbindig und cha zur Verdüütlichung ergänzt sii; oder s churz Wort isch bim Abschriibe usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 05 und 𝔓45 ohni αὐτοῦ, 02 und 032 mit; 04 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-026-009-01:R2", "MAT.26.9", "Das hätte nämlich", "Dieses Salböl hätte nämlich",
  "Mer hett das nämli", "Mer hett das Salböl nämli", "gering",
  "Das Salböl wird ausdrücklich genannt.", "S Salböl wird usdrücklich gnännt.",
  {"R1": [("τοῦτο", "das", "WH, Treg, NA28")], "R2": [("τοῦτο τὸ μύρον", "dieses Salböl", "NIV, RP")]},
  {"R1": [("τοῦτο", "das", "WH, Treg, NA28")], "R2": [("τοῦτο τὸ μύρον", "das Salböl", "NIV, RP")]},
  ["Der Zusatz kann aus [[MRK.14.5]] stammen, wo τοῦτο τὸ μύρον steht; ebenso kann er bei Matthäus ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 05, 032 und 𝔓45 ohne den Zusatz; 04 ist hier nicht erhalten."],
  ["De Zuesatz cha us [[MRK.14.5]] stamme; oder er isch bim Matthäus usgfalle.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 05, 032 und 𝔓45 ohni Zuesatz; 04 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-026-020-01:R2", "MAT.26.20", "mit den zwölf Jüngern", "mit den Zwölf",
  "mit de zwölf Jünger", "mit de Zwölf", "gering",
  "Es heisst nur «die Zwölf»; der Sinn bleibt gleich.", "Es heisst nu «di Zwölf»; de Sinn bliibt gliich.",
  {"R1": [("μαθητῶν", "Jüngern", "WH")], "R2": [("–", "(fehlt)", "Treg, NA28, RP")]},
  {"R1": [("μαθητῶν", "Jünger", "WH")], "R2": [("–", "(fehlt)", "Treg, NA28, RP")]},
  ["«Jünger» kann nach [[MAT.10.1]] und [[MAT.11.1]] («die zwölf Jünger») ergänzt worden sein; ebenso kann das Wort in Angleichung an [[MRK.14.17]] («mit den Zwölf») weggefallen sein. Der SBLGNT folgt hier WH gegen Treg, NA28 und RP.",
   "Laut der automatischen Zuordnung lesen 01, 02 und 032 μαθητῶν, 03 und 𝔓45 nicht; 05 hat einen anderen Wortlaut, 04 ist hier nicht erhalten."],
  ["«Jünger» cha nach [[MAT.10.1]] und [[MAT.11.1]] ergänzt sii; oder s Wort isch in Aagliichig a [[MRK.14.17]] wäggfalle. De SBLGNT folgt da WH gäge Treg, NA28 und RP.",
   "Nach de automatische Zueornig läsed 01, 02 und 032 μαθητῶν, 03 und 𝔓45 nöd; 05 hät en andere Wortlaut, 04 isch da nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-026-022-01:R2", "MAT.26.22", "jeder einzelne", "jeder von ihnen", "jede einzelne", "jede vo ine", "gering",
  "Gleicher Sinn, andere Wendung.", "Gliiche Sinn, anderi Wändig.",
  {"R1": [("εἷς ἕκαστος", "jeder einzelne", "WH, Treg, NA28")], "R2": [("ἕκαστος αὐτῶν", "jeder von ihnen", "RP")]},
  {"R1": [("εἷς ἕκαστος", "jede einzelne", "WH, Treg, NA28")], "R2": [("ἕκαστος αὐτῶν", "jede vo ine", "RP")]},
  ["Beide Wendungen sind geläufig; eine Glättung in die eine oder andere Richtung ist denkbar.",
   "Laut der automatischen Zuordnung lesen 01 und 03 εἷς ἕκαστος, 02, 05, 032 und 𝔓45 ἕκαστος αὐτῶν; 04 hat einen anderen Wortlaut."],
  ["Beidi Wändige sind gläufig; es Glätte i di eint oder ander Richtig isch dänkbar.",
   "Nach de automatische Zueornig läsed 01 und 03 εἷς ἕκαστος, 02, 05, 032 und 𝔓45 ἕκαστος αὐτῶν; 04 hät en andere Wortlaut."]),
 ("VAR-SBLGNTAPP-MAT-026-026-02:R2", "MAT.26.26", "sprach den Lobpreis", "sprach das Dankgebet", "de Lobpriis gsproche", "s Dankgebätt gsproche", "gering",
  "Beim Brot steht dasselbe Verb wie beim Becher (εὐχαριστέω «danken»).", "Bim Broot staat s gliich Verb wie bim Bächer (εὐχαριστέω «danke»).",
  {"R1": [("εὐλογήσας", "sprach den Lobpreis", "WH, Treg, NA28")], "R2": [("εὐχαριστήσας", "sprach das Dankgebet", "RP")]},
  {"R1": [("εὐλογήσας", "de Lobpriis gsproche", "WH, Treg, NA28")], "R2": [("εὐχαριστήσας", "s Dankgebätt gsproche", "RP")]},
  ["εὐχαριστήσας entspricht [[LUK.22.19]] und [[1CO.11.24]] und kann von dort oder aus [[MAT.26.27]] übernommen sein; εὐλογήσας stimmt mit [[MRK.14.22]] überein, was umgekehrt eine Angleichung an Markus sein kann.",
   "Laut der automatischen Zuordnung lesen 01 (auch die Korrektur), 03, 04, 05 und 𝔓45 εὐλογήσας, 02 und 032 εὐχαριστήσας."],
  ["εὐχαριστήσας entspricht [[LUK.22.19]] und [[1CO.11.24]] und cha vo dört oder us [[MAT.26.27]] übernoo sii; εὐλογήσας stimmt mit [[MRK.14.22]] überii, was umgekehrt e Aagliichig a de Markus sii cha.",
   "Nach de automatische Zueornig läsed 01 (au d Korrektur), 03, 04, 05 und 𝔓45 εὐλογήσας, 02 und 032 εὐχαριστήσας."]),
 ("VAR-SBLGNTAPP-MAT-026-028-02:R2", "MAT.26.28", "mein Blut des Bundes", "mein Blut des neuen Bundes", "mis Bluet vom Bund", "mis Bluet vom nöie Bund", "mittel",
  "Der Bund wird ausdrücklich «neu» genannt (vgl. [[JER.31.31]]).", "De Bund wird usdrücklich «nöi» gnännt (vgl. [[JER.31.31]]).",
  {"R1": [("τῆς διαθήκης", "des Bundes", "WH, NA28")], "R2": [("τῆς καινῆς διαθήκης", "des neuen Bundes", "Treg, RP")]},
  {"R1": [("τῆς διαθήκης", "vom Bund", "WH, NA28")], "R2": [("τῆς καινῆς διαθήκης", "vom nöie Bund", "Treg, RP")]},
  ["«Neu» kann aus [[LUK.22.20]] und [[1CO.11.25]] übernommen sein, wo vom neuen Bund die Rede ist; ebenso kann das Wort beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 𝔓45 ohne καινῆς, 02, 04, 05 und 032 mit ihm."],
  ["«Nöi» cha us [[LUK.22.20]] und [[1CO.11.25]] übernoo sii; oder s Wort isch bim Abschriibe usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 𝔓45 ohni καινῆς, 02, 04, 05 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-026-038-01:R2", "MAT.26.38", "Da sagt er zu ihnen", "Da sagt Jesus zu ihnen", "Dänn seit er zu ine", "Dänn seit de Jesus zu ine", "gering",
  "Das Subjekt wird ausdrücklich genannt.", "S Subjekt wird usdrücklich gnännt.",
  {"R1": [("αὐτοῖς", "zu ihnen", "WH, Treg, NA28")], "R2": [("αὐτοῖς ὁ Ἰησοῦς", "Jesus zu ihnen", "RP")]},
  {"R1": [("αὐτοῖς", "zu ine", "WH, Treg, NA28")], "R2": [("αὐτοῖς ὁ Ἰησοῦς", "de Jesus zu ine", "RP")]},
  ["Der Name kann verdeutlichend ergänzt worden sein, etwa für die Lesung eines einzelnen Abschnitts; ebenso denkbar ist ein Ausfall.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 04, 05, 032 und 𝔓45 ohne den Zusatz; keine der zugeordneten Handschriften hat ihn."],
  ["De Name cha zur Verdüütlichung ergänzt worde sii, öppe für d Läsig vo me einzelne Abschnitt; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 04, 05, 032 und 𝔓45 ohni Zuesatz; keini vo de zueordnete Handschrifte hät en."]),
 ("VAR-SBLGNTAPP-MAT-026-039-01:R2", "MAT.26.39", "er ging ein wenig weiter", "er trat ein wenig heran", "er isch es Stückli wiitergange", "er isch es Stückli härechoo", "gering",
  "Kaum ein Unterschied im Sinn: «herantreten» statt «vorausgehen».", "Chuum en Underschid im Sinn: «härechoo» statt «voruusgaa».",
  {"R1": [("προελθὼν", "ging … weiter", "WH, NA28")], "R2": [("προσελθὼν", "trat … heran", "Treg, RP")]},
  {"R1": [("προελθὼν", "isch … wiitergange", "WH, NA28")], "R2": [("προσελθὼν", "isch … härechoo", "Treg, RP")]},
  ["Die Formen unterscheiden sich nur in einem Buchstaben und sind leicht zu verwechseln. προσέρχομαι ist bei Matthäus sehr häufig, was den Wechsel zu diesem Wort erklären kann; ebenso kann προελθών eine Angleichung an [[MRK.14.35]] sein.",
   "Laut der automatischen Zuordnung lesen 03 und 𝔓45 προελθών, 01, 02, 04, 05 und 032 προσελθών."],
  ["Di zwei Forme underscheided sich nu i eim Buechstabe und sind liecht z verwächsle. προσέρχομαι isch bim Matthäus sehr hüüfig; oder προελθών isch e Aagliichig a [[MRK.14.35]].",
   "Nach de automatische Zueornig läsed 03 und 𝔓45 προελθών, 01, 02, 04, 05 und 032 προσελθών."]),
 ("VAR-SBLGNTAPP-MAT-026-042-01:R2", "MAT.26.42", "wenn dies nicht vorübergehen kann", "wenn dieser Becher nicht vorübergehen kann",
  "wänn das nöd cha verbiigaa", "wänn dä Bächer nöd cha verbiigaa", "gering",
  "Der Becher wird ausdrücklich genannt.", "De Bächer wird usdrücklich gnännt.",
  {"R1": [("τοῦτο", "dies", "WH, Treg, NA28")], "R2": [("τοῦτο τὸ ποτήριον", "dieser Becher", "RP")]},
  {"R1": [("τοῦτο", "das", "WH, Treg, NA28")], "R2": [("τοῦτο τὸ ποτήριον", "dä Bächer", "RP")]},
  ["Der Zusatz verdeutlicht nach [[MAT.26.39]]; ebenso kann er ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 04, 05 und 032 ohne den Zusatz. " + LACUNA_P45],
  ["De Zuesatz verdüütlicht nach [[MAT.26.39]]; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 04, 05 und 032 ohni Zuesatz. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-042-02:R2", "MAT.26.42", "vorübergehen kann, ohne dass", "an mir vorübergehen kann, ohne dass",
  "cha verbiigaa, ohni dass", "cha a mir verbiigaa, ohni dass", "gering",
  "«an mir» ist ergänzt wie in [[MAT.26.39]].", "«a mir» isch ergänzt wie i [[MAT.26.39]].",
  {"R1": [("παρελθεῖν", "vorübergehen", "WH, Treg, NA28")], "R2": [("παρελθεῖν ἀπʼ ἐμοῦ", "an mir vorübergehen", "RP")]},
  {"R1": [("παρελθεῖν", "verbiigaa", "WH, Treg, NA28")], "R2": [("παρελθεῖν ἀπʼ ἐμοῦ", "a mir verbiigaa", "RP")]},
  ["Angleichung an [[MAT.26.39]] liegt nahe; ebenso kann ἀπʼ ἐμοῦ ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne ἀπʼ ἐμοῦ, 02, 04 und 032 mit ihm. " + LACUNA_P45],
  ["Aagliichig a [[MAT.26.39]] liit nöch; oder ἀπʼ ἐμοῦ isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni ἀπʼ ἐμοῦ, 02, 04 und 032 mit. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-044-02:R2", "MAT.26.44", "und sprach noch einmal dieselben Worte", "und sprach dieselben Worte",
  "und nomal di gliiche Wort gseit", "und di gliiche Wort gseit", "gering",
  "Das dritte «wieder» im Vers fehlt.", "S dritt «wider» im Vers fehlt.",
  {"R1": [("πάλιν", "noch einmal", "WH, NA28")], "R2": [("–", "(fehlt)", "Treg, RP")]},
  {"R1": [("πάλιν", "nomal", "WH, NA28")], "R2": [("–", "(fehlt)", "Treg, RP")]},
  ["Das dreifache πάλιν im Vers wirkt überladen und kann deshalb gestrichen worden sein; ebenso kann es nachträglich ergänzt worden sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 πάλιν, 02, 04, 05 und 032 nicht. " + LACUNA_P45],
  ["S drüüfach πάλιν wirkt überlade und isch drum villicht gstriche worde; oder es isch nachträglich ergänzt worde.",
   "Nach de automatische Zueornig läsed 01 und 03 πάλιν, 02, 04, 05 und 032 nöd. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-045-01:R2", "MAT.26.45", "zu den Jüngern und sagt", "zu seinen Jüngern und sagt", "zu de Jünger und seit", "zu sine Jünger und seit", "gering",
  "Das Fürwort «seinen» ist ergänzt.", "S Fürwort «sine» isch ergänzt.",
  {"R1": [("μαθητὰς", "den Jüngern", "WH, Treg, NA28")], "R2": [("μαθητὰς αὐτοῦ", "seinen Jüngern", "RP")]},
  {"R1": [("μαθητὰς", "de Jünger", "WH, Treg, NA28")], "R2": [("μαθητὰς αὐτοῦ", "sine Jünger", "RP")]},
  ["Verdeutlichende Ergänzung oder Ausfall des kurzen Wortes; beides ist denkbar.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03 und 04 ohne αὐτοῦ, 05 und 032 mit ihm. " + LACUNA_P45],
  ["Verdüütlichendi Ergänzig oder Usfall vom churze Wort; beides isch dänkbar.",
   "Nach de automatische Zueornig läsed 01, 02, 03 und 04 ohni αὐτοῦ, 05 und 032 mit. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-052-02:R2", "MAT.26.52", "durch das Schwert umkommen", "durch das Schwert sterben",
  "chömed nämli dur s Schwärt um", "stärbed nämli dur s Schwärt", "gering",
  "«sterben» statt «umkommen»; der Sinn bleibt gleich.", "«stärbe» statt «umchoo»; de Sinn bliibt gliich.",
  {"R1": [("ἀπολοῦνται", "werden umkommen", "WH, Treg, NA28")], "R2": [("ἀποθανοῦνται", "werden sterben", "RP")]},
  {"R1": [("ἀπολοῦνται", "chömed um", "WH, Treg, NA28")], "R2": [("ἀποθανοῦνται", "stärbed", "RP")]},
  ["Die beiden Verben sind sinnverwandt und ähnlich gebaut; ein Ersatz beim Abschreiben ist in beide Richtungen denkbar.",
   "Laut der automatischen Zuordnung lesen 01, 02, 03, 04 und 05 ἀπολοῦνται, 032 ἀποθανοῦνται. " + LACUNA_P45],
  ["Di zwei Verbe sind sinnverwandt und ähnlich bout; en Ersatz bim Abschriibe isch i beidi Richtige dänkbar.",
   "Nach de automatische Zueornig läsed 01, 02, 03, 04 und 05 ἀπολοῦνται, 032 ἀποθανοῦνται. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-055-01:R2", "MAT.26.55", "Täglich sass ich im Tempel", "Täglich sass ich bei euch im Tempel",
  "Jede Tag bin ich im Tämpel gsässe", "Jede Tag bin ich bi eu im Tämpel gsässe", "gering",
  "«bei euch» ist ergänzt.", "«bi eu» isch ergänzt.",
  {"R1": [("ἡμέραν", "täglich", "WH, NA28")], "R2": [("ἡμέραν πρὸς ὑμᾶς", "täglich bei euch", "Treg, RP")]},
  {"R1": [("ἡμέραν", "jede Tag", "WH, NA28")], "R2": [("ἡμέραν πρὸς ὑμᾶς", "jede Tag bi eu", "Treg, RP")]},
  ["Der Zusatz entspricht [[MRK.14.49]] und kann von dort übernommen sein; ebenso kann er bei Matthäus ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 02 und 03 ohne πρὸς ὑμᾶς, 04, 05 und 032 mit ihm. " + LACUNA_P45],
  ["De Zuesatz entspricht [[MRK.14.49]] und cha vo dört übernoo sii; oder er isch bim Matthäus usgfalle.",
   "Nach de automatische Zueornig läsed 01, 02 und 03 ohni πρὸς ὑμᾶς, 04, 05 und 032 mit. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-059-01:R2", "MAT.26.59", "Die Hohepriester aber und der ganze Hohe Rat", "Die Hohepriester aber und die Ältesten und der ganze Hohe Rat",
  "D Hoheprieschter aber und de ganz Hoch Raat", "D Hoheprieschter aber und d Ältischte und de ganz Hoch Raat", "gering",
  "Auch die Ältesten werden genannt.", "Au d Ältischte wärded gnännt.",
  {"R1": [("καὶ", "und", "WH, Treg, NA28")], "R2": [("καὶ οἱ πρεσβύτεροι καὶ", "und die Ältesten und", "RP")]},
  {"R1": [("καὶ", "und", "WH, Treg, NA28")], "R2": [("καὶ οἱ πρεσβύτεροι καὶ", "und d Ältischte und", "RP")]},
  ["Die Ältesten können nach [[MAT.26.3]], [[MAT.26.47]] und [[MAT.27.1]] ergänzt worden sein; ebenso kann das Auge eines Abschreibers vom einen καί zum nächsten gesprungen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne den Zusatz, 02, 04 und 032 mit ihm. " + LACUNA_P45],
  ["D Ältischte chönted nach [[MAT.26.3]], [[MAT.26.47]] und [[MAT.27.1]] ergänzt sii; oder s Aug vo me Abschriiber isch vom eine καί zum nächschte gsprunge.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni Zuesatz, 02, 04 und 032 mit. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-063-01:R2", "MAT.26.63", "Und der Hohepriester sagte zu ihm", "Und der Hohepriester antwortete und sagte zu ihm",
  "Und de Hoheprieschter hät zu ihm gseit", "Und de Hoheprieschter hät gantwortet und zu ihm gseit", "gering",
  "Die geläufige Redeeinleitung «antwortete und sagte».", "Di gläufig Redeiileitig «hät gantwortet und gseit».",
  {"R1": [("καὶ", "und", "WH, Treg, NA28")], "R2": [("καὶ ἀποκριθεὶς", "und … antwortete und", "RP")]},
  {"R1": [("καὶ", "und", "WH, Treg, NA28")], "R2": [("καὶ ἀποκριθεὶς", "und … hät gantwortet und", "RP")]},
  ["Die formelhafte Wendung wird oft ergänzt; dass ἀποκριθείς ausfiel, weil Jesus geschwiegen hatte und es nichts zu beantworten gab, ist ebenfalls denkbar.",
   "Laut der automatischen Zuordnung lesen 03 und die Korrektur in 01 ohne ἀποκριθείς, 02, 04, 05 und 032 mit ihm; die Erstschrift von 01 hat einen anderen Wortlaut. " + LACUNA_P45],
  ["Di formelhaft Wändig wird oft ergänzt; dänkbar isch au, dass ἀποκριθείς wäggfalle isch, wil de Jesus gschwige hät und s nüüt z beantworte gää hät.",
   "Nach de automatische Zueornig läsed 03 und d Korrektur i 01 ohni ἀποκριθείς, 02, 04, 05 und 032 mit; d Erschtschrift vo 01 hät en andere Wortlaut. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-065-02:R2", "MAT.26.65", "habt ihr die Lästerung gehört", "habt ihr seine Lästerung gehört",
  "händ ir d Läschterig ghört", "händ ir sini Läschterig ghört", "gering",
  "Das Fürwort «seine» ist ergänzt.", "S Fürwort «sini» isch ergänzt.",
  {"R1": [("βλασφημίαν", "die Lästerung", "WH, Treg, NA28")], "R2": [("βλασφημίαν αὐτοῦ", "seine Lästerung", "RP")]},
  {"R1": [("βλασφημίαν", "d Läschterig", "WH, Treg, NA28")], "R2": [("βλασφημίαν αὐτοῦ", "sini Läschterig", "RP")]},
  ["Verdeutlichende Ergänzung oder Ausfall des kurzen Wortes; beides ist denkbar.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne αὐτοῦ, 02, 04 und 032 mit ihm. " + LACUNA_P45],
  ["Verdüütlichendi Ergänzig oder Usfall vom churze Wort; beides isch dänkbar.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni αὐτοῦ, 02, 04 und 032 mit. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-070-01:R2", "MAT.26.70", "vor allen", "vor ihnen allen", "vor allne", "vor ine allne", "gering",
  "«ihnen» ist ergänzt.", "«ine» isch ergänzt.",
  {"R1": [("ἔμπροσθεν", "vor", "WH, Treg, NA28")], "R2": [("ἔμπροσθεν αὐτῶν", "vor ihnen", "RP")]},
  {"R1": [("ἔμπροσθεν", "vor", "WH, Treg, NA28")], "R2": [("ἔμπροσθεν αὐτῶν", "vor ine", "RP")]},
  ["Verdeutlichende Ergänzung oder Ausfall des kurzen Wortes; beides ist denkbar.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne αὐτῶν, 02, 04 und 032 mit ihm. " + LACUNA_P45],
  ["Verdüütlichendi Ergänzig oder Usfall vom churze Wort; beides isch dänkbar.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni αὐτῶν, 02, 04 und 032 mit. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-071-03:R2", "MAT.26.71", "«Dieser war mit Jesus", "«Auch dieser war mit Jesus", "«Dä isch mit em Jesus", "«Au dä isch mit em Jesus", "gering",
  "Mit «auch» knüpft die zweite Magd an die Aussage der ersten an ([[MAT.26.69]]).", "Mit «au» knüpft di zweit Magd a d Ussag vo de erschte aa ([[MAT.26.69]]).",
  {"R1": [("Οὗτος", "Dieser", "WH, NA28")], "R2": [("Καὶ οὗτος", "Auch dieser", "Treg, RP")]},
  {"R1": [("Οὗτος", "Dä", "WH, NA28")], "R2": [("Καὶ οὗτος", "Au dä", "Treg, RP")]},
  ["«Auch» kann nach [[MAT.26.69]] («Auch du») ergänzt worden sein; ebenso kann das kurze Wort ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 οὗτος, 02, 04 und 032 καὶ οὗτος. " + LACUNA_P45],
  ["«Au» cha nach [[MAT.26.69]] ergänzt worde sii; oder s churz Wort isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 οὗτος, 02, 04 und 032 καὶ οὗτος. " + LACUNA_P45_G]),
 ("VAR-SBLGNTAPP-MAT-026-075-02:R2", "MAT.26.75", "das Jesus gesagt hatte", "das Jesus zu ihm gesagt hatte", "wo de Jesus gseit hät", "wo de Jesus zu ihm gseit hät", "gering",
  "«zu ihm» ist ergänzt.", "«zu ihm» isch ergänzt.",
  {"R1": [("εἰρηκότος", "gesagt hatte", "WH, Treg, NA28")], "R2": [("εἰρηκότος αὐτῷ", "zu ihm gesagt hatte", "RP")]},
  {"R1": [("εἰρηκότος", "gseit hät", "WH, Treg, NA28")], "R2": [("εἰρηκότος αὐτῷ", "zu ihm gseit hät", "RP")]},
  ["Der Zusatz kann aus [[MRK.14.72]] stammen, wo αὐτῷ steht; ebenso kann er ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne αὐτῷ, 02, 04 und 032 mit ihm. " + LACUNA_P45],
  ["De Zuesatz cha us [[MRK.14.72]] stamme; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni αὐτῷ, 02, 04 und 032 mit. " + LACUNA_P45_G]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-026-001-075", "MAT.26.1-MAT.26.75", "section", "Salbung, letztes Mahl, Getsemani und Verhör",
  ["TU-MAT-026-001-005", "TU-MAT-026-006-013", "TU-MAT-026-014-016", "TU-MAT-026-017-025", "TU-MAT-026-026-030",
   "TU-MAT-026-031-035", "TU-MAT-026-036-046", "TU-MAT-026-047-056", "TU-MAT-026-057-068", "TU-MAT-026-069-075"],
  "Nach seinen Reden sagt Jesus den Jüngern, dass in zwei Tagen das Passa ist und der Menschensohn ausgeliefert wird, um gekreuzigt zu werden; die Hohepriester und Ältesten beraten im Hof des Kajafas, wie sie ihn mit List ergreifen und töten können. In Betanien giesst eine Frau Jesus kostbares Salböl über den Kopf; er verteidigt sie gegen die empörten Jünger und bezieht es auf sein Begräbnis. Judas lässt sich von den Hohepriestern dreissig Silberstücke abwiegen, um Jesus auszuliefern. Beim Passamahl kündigt Jesus an, dass einer der Zwölf ihn ausliefern wird; er gibt den Jüngern Brot und Becher mit den Worten, das sei sein Leib und sein Blut des Bundes. Auf dem Weg zum Ölberg sagt er voraus, dass alle an ihm Anstoss nehmen und Petrus ihn dreimal verleugnen wird. In Getsemani betet er dreimal, während die Jünger schlafen. Judas kommt mit einer bewaffneten Menge und küsst ihn; Jesus wird festgenommen und heisst einen Begleiter, der mit dem Schwert zugeschlagen hat, das Schwert zurückstecken; alle Jünger fliehen. Vor Kajafas und dem Hohen Rat antwortet Jesus auf die Frage, ob er der Christus sei: «Du hast es gesagt», und kündigt den Menschensohn zur Rechten der Macht an; die Versammelten erklären, er habe den Tod verdient, und misshandeln ihn. Im Hof leugnet Petrus dreimal, zu Jesus zu gehören; ein Hahn kräht, Petrus erinnert sich an das Wort Jesu und weint bitterlich.", SEG),
 ("TU-MAT-026-001-005", "MAT.26.1-MAT.26.5", "narrative", "Der Plan, Jesus zu töten", None,
  "Als Jesus alle diese Worte beendet hat, sagt er seinen Jüngern, dass in zwei Tagen das Passa ist und der Menschensohn ausgeliefert wird, um gekreuzigt zu werden. Die Hohepriester und die Ältesten des Volkes versammeln sich im Hof des Hohepriesters Kajafas und beraten, wie sie Jesus mit List ergreifen und töten können; nicht am Fest, sagen sie, damit kein Aufruhr im Volk entsteht.", None),
 ("TU-MAT-026-006-013", "MAT.26.6-MAT.26.13", "narrative", "Die Salbung in Betanien", None,
  "Im Haus Simons des Aussätzigen in Betanien giesst eine Frau Jesus, der zu Tisch liegt, sehr kostbares Salböl aus einem Alabastergefäss über den Kopf. Die Jünger empören sich über die Verschwendung: Man hätte das Öl teuer verkaufen und den Armen geben können. Jesus nimmt die Frau in Schutz: Sie habe ein gutes Werk an ihm getan; die Armen hätten sie immer bei sich, ihn nicht. Mit dem Salböl habe sie es für sein Begräbnis getan, und wo das Evangelium verkündigt werde, werde man zu ihrem Gedächtnis erzählen, was sie getan hat.", None),
 ("TU-MAT-026-014-016", "MAT.26.14-MAT.26.16", "narrative", "Judas und die Hohepriester", None,
  "Judas Iskariot, einer der Zwölf, geht zu den Hohepriestern und fragt, was sie ihm geben wollen; dann werde er ihnen Jesus ausliefern. Sie wiegen ihm dreissig Silberstücke ab, und von da an sucht er eine günstige Gelegenheit, ihn auszuliefern.", None),
 ("TU-MAT-026-017-025", "MAT.26.17-MAT.26.25", "dialogue", "Das Passamahl und die Ankündigung der Auslieferung", None,
  "Am ersten Tag der Ungesäuerten Brote fragen die Jünger, wo sie das Passa vorbereiten sollen. Jesus schickt sie in die Stadt zu einem Mann, dem sie ausrichten sollen: Die Zeit des Lehrers sei nahe, bei ihm halte er mit seinen Jüngern das Passa; sie tun es. Am Abend, beim Mahl mit den Zwölf, sagt Jesus, einer von ihnen werde ihn ausliefern. Tief betrübt fragt ihn einer nach dem anderen: «Ich bin es doch nicht, Herr?» Jesus antwortet, der mit ihm die Hand in die Schüssel getaucht hat, werde ihn ausliefern; der Menschensohn gehe dahin, wie geschrieben steht, doch weh dem Menschen, durch den er ausgeliefert wird. Auf die Frage des Judas: «Ich bin es doch nicht, Rabbi?» sagt Jesus: «Du hast es gesagt.»", None),
 ("TU-MAT-026-026-030", "MAT.26.26-MAT.26.30", "narrative", "Brot und Becher", None,
  "Während sie essen, nimmt Jesus Brot, spricht den Lobpreis, bricht es und gibt es den Jüngern mit den Worten: «Nehmt, esst! Das ist mein Leib.» Dann nimmt er einen Becher, spricht das Dankgebet und gibt ihn ihnen: Sie sollen alle daraus trinken, denn das sei sein Blut des Bundes, das für viele vergossen wird zur Vergebung der Sünden. Er werde von nun an nicht mehr vom Gewächs des Weinstocks trinken bis zu dem Tag, an dem er es mit ihnen neu trinkt im Reich seines Vaters. Nach dem Lobgesang gehen sie hinaus zum Ölberg.", None),
 ("TU-MAT-026-031-035", "MAT.26.31-MAT.26.35", "dialogue", "Die Ankündigung der Verleugnung", None,
  "Jesus sagt den Jüngern, sie alle würden in dieser Nacht an ihm Anstoss nehmen, denn es steht geschrieben: «Ich werde den Hirten schlagen, und die Schafe der Herde werden zerstreut werden» ([[ZEC.13.7]]); nach seiner Auferweckung werde er ihnen nach Galiläa vorausgehen. Petrus beteuert, er werde niemals Anstoss nehmen. Jesus kündigt ihm an, er werde ihn in dieser Nacht, bevor ein Hahn kräht, dreimal verleugnen. Petrus versichert, er werde ihn nicht verleugnen, selbst wenn er mit ihm sterben müsse; ebenso reden alle Jünger.", None),
 ("TU-MAT-026-036-046", "MAT.26.36-MAT.26.46", "narrative", "Getsemani", None,
  "Jesus kommt mit den Jüngern zu einem Grundstück namens Getsemani und nimmt Petrus und die beiden Söhne des Zebedäus mit; er wird traurig und ängstigt sich und bittet sie, hier zu bleiben und mit ihm zu wachen. Er fällt auf sein Gesicht und betet: «Mein Vater, wenn es möglich ist, so gehe dieser Becher an mir vorüber! Doch nicht, wie ich will, sondern wie du willst.» Er findet die Jünger schlafend und sagt zu Petrus, sie hätten nicht eine Stunde mit ihm wachen können; sie sollen wachen und beten, damit sie nicht in Versuchung kommen. Ein zweites Mal betet er: Wenn dies nicht vorübergehen könne, ohne dass er es trinkt, so geschehe der Wille des Vaters. Wieder findet er sie schlafend und betet ein drittes Mal mit denselben Worten. Dann fragt er sie, ob sie noch schlafen: Die Stunde ist nahe gekommen, der Menschensohn wird in die Hände von Sündern ausgeliefert; sie sollen aufstehen, denn der ihn ausliefert, ist nahe gekommen.", None),
 ("TU-MAT-026-047-056", "MAT.26.47-MAT.26.56", "narrative", "Die Gefangennahme", None,
  "Noch während Jesus redet, kommt Judas mit einer grossen Menge mit Schwertern und Knüppeln, von den Hohepriestern und Ältesten des Volkes. Er hat ihnen einen Kuss als Zeichen verabredet, tritt zu Jesus, grüsst ihn mit «Sei gegrüsst, Rabbi!» und küsst ihn; Jesus sagt: «Freund, tu, wozu du da bist!», und sie ergreifen ihn. Einer von denen, die bei Jesus sind, zieht das Schwert und schlägt dem Knecht des Hohepriesters das Ohr ab. Jesus heisst ihn das Schwert zurückstecken, denn alle, die zum Schwert greifen, werden durch das Schwert umkommen; er könnte seinen Vater um mehr als zwölf Legionen Engel bitten, doch wie würden dann die Schriften erfüllt? Den Menschenmengen hält er vor, dass sie wie gegen einen Räuber gegen ihn ausgezogen sind, obwohl er täglich im Tempel lehrte; das alles sei geschehen, damit die Schriften der Propheten erfüllt würden. Da verlassen ihn alle Jünger und fliehen.", None),
 ("TU-MAT-026-057-068", "MAT.26.57-MAT.26.68", "narrative", "Jesus vor dem Hohen Rat", None,
  "Jesus wird zum Hohepriester Kajafas geführt, wo die Schriftgelehrten und die Ältesten versammelt sind; Petrus folgt von ferne bis in den Hof und setzt sich zu den Dienern, um den Ausgang zu sehen. Die Hohepriester und der ganze Hohe Rat suchen falsches Zeugnis gegen Jesus, um ihn zu töten, und finden keines, obwohl viele falsche Zeugen herantreten; schliesslich sagen zwei aus, er habe gesagt, er könne den Tempel Gottes niederreissen und in drei Tagen aufbauen. Jesus schweigt. Der Hohepriester beschwört ihn beim lebendigen Gott, zu sagen, ob er der Christus, der Sohn Gottes, sei. Jesus antwortet: «Du hast es gesagt», und kündigt an, von nun an würden sie den Menschensohn zur Rechten der Macht sitzen und auf den Wolken des Himmels kommen sehen. Der Hohepriester zerreisst seine Gewänder und erklärt, Jesus habe gelästert; die Versammelten antworten, er habe den Tod verdient. Sie spucken ihm ins Gesicht, schlagen ihn und verlangen spottend, er solle weissagen, wer ihn geschlagen hat.", None),
 ("TU-MAT-026-069-075", "MAT.26.69-MAT.26.75", "narrative", "Petrus verleugnet Jesus", None,
  "Im Hof sagt eine Magd zu Petrus, auch er sei mit Jesus, dem Galiläer, gewesen; er leugnet vor allen. Am Tor sagt eine andere zu den Leuten dort, dieser sei mit Jesus, dem Nazoräer, gewesen; er leugnet mit einem Eid, den Menschen zu kennen. Kurz darauf sagen die Umstehenden, er sei wirklich einer von ihnen, seine Sprechweise verrate ihn; da beginnt er, sich zu verfluchen und zu schwören, er kenne den Menschen nicht. Sogleich kräht ein Hahn. Petrus erinnert sich an das Wort Jesu, er werde ihn dreimal verleugnen, bevor ein Hahn kräht, geht hinaus und weint bitterlich.", None),
]
UNITS_GSW = {
 "TU-MAT-026-001-075": ("Salbig, letschts Ässe, Getsemani und Verhör", "Nach sine Rede seit de Jesus de Jünger, dass in zwei Täg s Passa isch und de Mänschesohn usgliferet wird, zum gchrüüziget wärde; d Hoheprieschter und d Ältischte beraated im Hof vom Kajafas, wie si en mit Lischt chönted packe und umbringe. Z Betanie schüttet e Frau em Jesus tüürs Salböl über de Chopf; er nimmt si gäge di empörte Jünger in Schutz und bezieht s uf sini Beerdigung. De Judas laat sich vo de Hoheprieschter driissg Silberstück abwääge, zum de Jesus uslifere. Bim Passaässe seit de Jesus, dass eine vo de Zwölf en wird uslifere; er git de Jünger Broot und Bächer und seit, das sig sin Liib und sis Bluet vom Bund. Uf em Wäg zum Ölberg seit er voruus, dass alli a ihm Aastoss nämed und de Petrus en drüümal wird verleugne. Z Getsemani bättet er drüümal, während d Jünger schlaafed. De Judas chunnt mit ere bewaffnete Mängi und küsst en; de Jesus wird feschtgnoo und heisst eine vo sine Lüüt, wo mit em Schwärt zueghaue hät, s Schwärt zruggstecke; alli Jünger flüchted. Vor em Kajafas und em Hoche Raat antwortet de Jesus uf d Frag, öb er de Christus sig: «Du häsch es gseit», und seit de Mänschesohn zur Rächte vo de Macht aa; d Versammlete erkläred, er heig de Tod verdient, und plooged en. Im Hof strittet de Petrus drüümal ab, zum Jesus z ghöre; en Güggel chräit, de Petrus erinneret sich as Wort vom Jesus und briegget bitter."),
 "TU-MAT-026-001-005": ("De Plan, de Jesus z töte", "Wo de Jesus mit all dene Wort fertig isch, seit er sine Jünger, dass in zwei Täg s Passa isch und de Mänschesohn usgliferet wird, zum gchrüüziget wärde. D Hoheprieschter und d Ältischte vom Volk chömed im Hof vom Hoheprieschter Kajafas zäme und beraated, wie si de Jesus mit Lischt chönted packe und umbringe; nöd am Fäscht, säged si, suscht gäb s en Ufruer im Volk."),
 "TU-MAT-026-006-013": ("D Salbig z Betanie", "Im Huus vom Simon em Ussätzige z Betanie schüttet e Frau em Jesus, wo am Tisch liit, sehr tüürs Salböl us eme Alabaschtergfäss über de Chopf. D Jünger reged sich über d Verschwändig uf: Mer hett s Öl tüür chöne verchaufe und de Arme gää. De Jesus nimmt d Frau in Schutz: Si heig es guets Wärch a ihm taa; d Arme heigid si immer bi sich, ihn nöd. Mit em Salböl heig si s für sini Beerdigung gmacht, und wo s Evangelium verchündet wärdi, wärd mer zur Erinnerig a si verzelle, was si gmacht hät."),
 "TU-MAT-026-014-016": ("De Judas und d Hoheprieschter", "De Judas Iskariot, eine vo de Zwölf, gaat zu de Hoheprieschter und fröget, was si ihm wänd gää; dänn lifer er ene de Jesus us. Si wääged ihm driissg Silberstück ab, und vo dänn aa suecht er e günschtigi Glägeheit, zum en uslifere."),
 "TU-MAT-026-017-025": ("S Passaässe und d Aakündigung vo de Uslifrig", "Am erschte Tag vo de ungsüürete Broot fröged d Jünger, wo si s Passa söled vorbereite. De Jesus schickt si i d Stadt zu eme Maa, däm si söled usrichte: D Ziit vom Lehrer sig nöch, bi ihm fiir er mit sine Jünger s Passa; si mached s. Am Aabig, bim Ässe mit de Zwölf, seit de Jesus, eine vo ine wärd en uslifere. Ganz truurig fröget en eine nach em andere: «Ich bi s doch nöd, Herr?» De Jesus antwortet, dä, wo mit ihm d Hand i d Schüssle tunkt hät, wärd en uslifere; de Mänschesohn gang dethii, wie s gschribe staat, aber weh em Mänsch, dur dä er usgliferet wird. Uf d Frag vom Judas: «Ich bi s doch nöd, Rabbi?» seit de Jesus: «Du häsch es gseit.»"),
 "TU-MAT-026-026-030": ("Broot und Bächer", "Während si ässed, nimmt de Jesus Broot, spricht de Lobpriis, bricht s und git s de Jünger und seit: «Nämed, ässed! Das isch min Liib.» Dänn nimmt er en Bächer, spricht s Dankgebätt und git en ine: Si söled alli drus trinke, dänn das sig sis Bluet vom Bund, wo für vili vergosse wird zur Vergäbig vo de Sünde. Er wärd vo jetzt aa nümme vom Gwächs vom Wiistock trinke bis zu däm Tag, wo er s mit ine nöi trinkt im Riich vo sim Vatter. Nach em Lobgsang gönd si use uf de Ölberg."),
 "TU-MAT-026-031-035": ("D Aakündigung vo de Verleugnig", "De Jesus seit de Jünger, si wärdid alli i dere Nacht a ihm Aastoss nää, dänn es staat gschribe: «Ich wirde de Hirt schlaa, und d Schaf vo de Herde wärded verstreut» ([[ZEC.13.7]]); nach sinere Uferweckig gang er ine nach Galiläa voruus. De Petrus beteuret, er nämi nie Aastoss. De Jesus seit em, er wärd en i dere Nacht, bevor en Güggel chräit, drüümal verleugne. De Petrus versicheret, er wärd en nöd verleugne, au wänn er mit ihm müesst sterbe; gnau so reded alli Jünger."),
 "TU-MAT-026-036-046": ("Getsemani", "De Jesus chunnt mit de Jünger zu eme Grundstück, wo Getsemani heisst, und nimmt de Petrus und di zwei Söhn vom Zebedäus mit; er wird truurig und hät Angscht und bittet si, da z bliibe und mit ihm z wache. Er fallt uf sis Gsicht und bättet: «Min Vatter, wänn s möglich isch, söll dä Bächer a mir verbiigaa! Aber nöd, wie ich wott, sondern wie du wottsch.» Er findt d Jünger am Schlaafe und seit zum Petrus, si heigid s nöd gschafft, ei Stund mit ihm wach z bliibe; si söled wache und bätte, damit si nöd i Versuechig chömed. Es zweits Mal bättet er: Wänn das nöd chönn verbiigaa, ohni dass er s trinki, dänn söll de Wile vom Vatter gschee. Wider findt er si schlaafend und bättet es dritts Mal mit de gliiche Wort. Dänn fröget er si, öb si no schlaafed: D Stund isch nöch, de Mänschesohn wird i d Händ vo Sünder usgliferet; si söled ufstaa, dänn dä, wo en usliferet, isch nöch."),
 "TU-MAT-026-047-056": ("D Gfangenahm", "No während de Jesus redt, chunnt de Judas mit ere grosse Mängi mit Schwärter und Chnüppel, vo de Hoheprieschter und Ältischte vom Volk. Er hät ine en Kuss als Zeiche abgmacht, gaat zum Jesus, grüesst en mit «Grüess di, Rabbi!» und küsst en; de Jesus seit: «Fründ, mach, für was du da bisch!», und si packed en. Eine vo dene, wo bim Jesus sind, zieht s Schwärt und haut em Chnächt vom Hoheprieschter s Oor ab. De Jesus heisst en, s Schwärt zruggstecke, dänn alli, wo zum Schwärt griifed, chömed dur s Schwärt um; er chönnt sim Vatter rüefe für meh als zwölf Legione Ängel, aber wie würded dänn d Schrifte erfüllt? De Lüüt hebt er vor, dass si wie gäge en Röiber gäge ihn uuszoge sind, obwohl er jede Tag im Tämpel glehrt heig; das alles sig gscheh, damit d Schrifte vo de Prophete erfüllt wärded. Dänn verlönd en alli Jünger und flüchted."),
 "TU-MAT-026-057-068": ("De Jesus vor em Hoche Raat", "De Jesus wird zum Hoheprieschter Kajafas gfüert, wo d Schriftgelehrte und d Ältischte zämechoo sind; de Petrus gaat em vo wiitem nache bis in Hof und sitzt zu de Diener, zum luege, wie s usgaat. D Hoheprieschter und de ganz Hoch Raat sueched es falschs Zügnis gäge de Jesus, zum en töte, und finded keis, obwohl vili falschi Züüge härechömed; zletscht säged zwei us, er heig gseit, er chönn de Tämpel vo Gott abriisse und in drüü Täg ufbaue. De Jesus schwiigt. De Hoheprieschter beschwört en bim läbige Gott, z säge, öb er de Christus, de Sohn vo Gott, sig. De Jesus antwortet: «Du häsch es gseit», und seit, vo jetzt aa wärdid si de Mänschesohn zur Rächte vo de Macht gseh sitze und uf de Wolche vom Himel choo. De Hoheprieschter verriisst sini Chleider und seit, de Jesus heig gläschteret; d Versammlete antworted, er heig de Tod verdient. Si spöied ihm is Gsicht, schlönd en und verlanged zum Spott, er söll weissage, wer en gschlage hät."),
 "TU-MAT-026-069-075": ("De Petrus verleugnet de Jesus", "Im Hof seit e Magd zum Petrus, au er sig mit em Jesus, em Galiläer, gsii; er strittet s vor allne ab. Bim Tor seit e anderi zu de Lüüt dört, dä sig mit em Jesus, em Nazoräer, gsii; er strittet mit eme Eid ab, dä Mänsch z kenne. Churz druf säged d Umstehende, er sig würkli eine vo ine, sini Spraach verrati en; dänn faat er aa, sich z verflueche und z schwööre, er kenni dä Mänsch nöd. Grad chräit en Güggel. De Petrus erinneret sich as Wort vom Jesus, er wärd en drüümal verleugne, bevor en Güggel chräit, gaat use und briegget bitter."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1, "
  "data/witness-readings/WREAD-CNTR-MAT-026-001-075), nicht auf eigener Prüfung der Handschriften. Bei den hier "
  "verwendeten Varianten widerspricht die automatische Zuordnung der Editionen (ED-RP usw.) den Sigla des SBLGNT-Apparats "
  "nicht. Bei VAR-SBLGNTAPP-MAT-026-017-01 (λέγοντες / αὐτῷ, ohne Wirkung auf die Übersetzung und deshalb nicht als "
  "Alternative geführt) ordnet sie ED-RP der SBLGNT-Lesart zu, während der Apparat RP bei der anderen Lesart nennt; es gilt "
  "der Apparat, die Zuordnung ist dort unsicher."),
 ("Abgrenzung: Diese Datei übersetzt Matthäus 26 vollständig (75 Verse). Im SBLGNT fehlt in diesem Kapitel kein Vers. "
  "Einheitliche Begriffe für das ganze Matthäusevangelium (Menschensohn, Amen ich sage euch, Hohepriester, Älteste, "
  "Schriftgelehrte, Christus usw.) sind übernommen; in Kapitel 26 neu festgelegt und in decisions begründet sind: "
  "παραδίδωμι «ausliefern» (nicht «verraten»), ποτήριον «Becher», ἀπαρνέομαι «verleugnen» "
  "und ἀρνέομαι «leugnen», συνέδριον «Hoher Rat», ἀλέκτωρ «Hahn» (Mundart «Güggel»), Καϊάφας «Kajafas». Nach der "
  "gemeinsamen Festlegung: σκανδαλίζομαι gegenüber einer Person «Anstoss nehmen an» ([[MAT.26.31]], [[MAT.26.33]]), sonst «zu "
  "Fall kommen»; προσέρχομαι «herantreten»; ὄχλος «die Menge», οἱ ὄχλοι «die Menschenmengen»; δοῦλος «Knecht»."),
 ("Parallele zu Markus 14: Gleiche griechische Wendungen sind wie in der Markus-Übersetzung wiedergegeben (z. B. «sprach den "
  "Lobpreis», «Tief betrübt ist meine Seele», «Räuber», «Knüppel»). Wo Matthäus anders formuliert, folgt die Übersetzung "
  "seinem Wortlaut: «Mein Vater» statt «Abba» ([[MAT.26.39]]), «Du hast es gesagt» statt «Ich bin es» ([[MAT.26.64]]), "
  "ein Hahnenschrei statt zwei ([[MAT.26.34]], [[MAT.26.75]]), «Nazoräer» ([[MAT.26.71]]) statt «Nazarener»."),
 ("Bezug zum Vaterunser: Das zweite Gebet in Getsemani ([[MAT.26.42]]) hat wörtlich dieselbe Bitte wie [[MAT.6.10]] "
  "(γενηθήτω τὸ θέλημά σου); die Wiedergabe ist auf die bestehende Übersetzung von [[MAT.6.5]]–[[MAT.6.15]] abgestimmt "
  "(«dein Wille geschehe» bzw. Mundart «diin Wile söll gschee», hier «söll diin Wile gschee»), ebenso «Versuchung» in [[MAT.26.41]] (vgl. [[MAT.6.13]])."),
 ("Erzählweise und Redegrenzen: Das erzählende Präsens (λέγει «sagt») ist beibehalten. ὅτι vor direkter Rede ist nicht eigens "
  "übersetzt. Anführungszeichen sind eine Entscheidung der Übersetzung; in [[MAT.26.56]] lässt sie die Rede Jesu bis "
  "«erfüllt würden» laufen (die andere Möglichkeit steht in decisions)."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT gegen Treg, NA28 und RP liest ([[MAT.26.20]] "
  "μαθητῶν, mit WH). Abweichende Lesarten stehen als Alternativen, soweit sie die Übersetzung verändern; reine Wortstellungs- "
  "oder Formvarianten ohne Wirkung auf die Übersetzung sind nur in follows_readings erfasst."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig. Eigeti Formulierig; nöd us ere veröffentlichte Mundart-Bible übernoo.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1), nöd uf eigeter "
  "Prüefig vo de Handschrifte."),
 ("Begriff (wie im ganze Matthäusevangelium): s Riich vo de Himel; de Mänschesohn; Amen, ich säg eu / dir; Hoheprieschter, "
  "Ältischti, Schriftgelehrti (mit Artikel «d Ältischte», «d Schriftgelehrte»); lueg (ἰδού); grad (εὐθέως); dänn (τότε); "
  "σκανδαλίζομαι gägenüber ere Person «Aastoss nää» (susch «z Fall choo»); προσέρχομαι «härechoo»; ὄχλος «d Mängi», "
  "οἱ ὄχλοι «d Lüüt». Im Kapitel 26 neu: παραδίδωμι «uslifere», ποτήριον «Bächer», ἀπαρνέομαι «verleugne», ἀρνέομαι «abstriite», συνέδριον «Hoch Raat», "
  "ἀλέκτωρ «Güggel», Καϊάφας «Kajafas»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Petrus»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«de Tämpel vo Gott»). [[MAT.26.42]] «söll diin Wile gschee» mit de Wort vom Vaterunser ([[MAT.6.10]])."),
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
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; einheitliche Begriffe für das ganze Matthäusevangelium (siehe translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_26_26.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 26 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
