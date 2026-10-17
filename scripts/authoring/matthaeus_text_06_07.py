#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 6,1–4; 6,16–34 und 7,1–29 (zweiter Teil der Bergpredigt) – Texteinheiten,
Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und
vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_06_07.py

Muster: scripts/authoring/johannes_text_01_03.py und scripts/authoring/markus_text_01_03.py. Die Übersetzung steht als
Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen daraus und stimmen deshalb
überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log. WORK-MAT besteht und wird nur
referenziert, nicht geschrieben.

Abgrenzung: [[MAT.6.5-MAT.6.15]] ist bereits übersetzt (scripts/authoring/vaterunser.py: TRANS-MAT-006-005-015-DE-WORKING,
TRANS-MAT-006-005-015-GSW-ZH-WORKING, Texteinheiten TU-MAT-006-005-015 mit Teilen). Dieses Werkzeug berührt jene
Datensätze nicht; es schreibt für Kapitel 6 zwei Übersetzungen (6,1–4 und 6,16–34) und die Kapiteleinheit
TU-MAT-006-001-034, deren Teile TU-MAT-006-005-015 einschliessen. Wortlaut und Begriffe sind auf das Vaterunser-Stück
abgestimmt.

In Matthäus 6–7 fehlt im SBLGNT kein Vers (per Skript geprüft: alle Verse haben Tokens).

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben in den Lesarten stammen aus der maschinellen Zuordnung
(METHOD-AUTO-COLLATION-V1, data/witness-readings/WREAD-CNTR-MAT-*) bzw. aus dem dort erfassten Wortlaut der
CNTR-Transkriptionen (Sekundärtranskription), nicht aus eigener Prüfung der Handschriften.
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
# (Kapitel, erster Vers, letzter Vers); 6,5–15 besteht schon (vaterunser.py)
SEGMENTS = ((6, 1, 4), (6, 16, 34), (7, 1, 29))
CHAPTER_LAST = {6: 34, 7: 29}

DE = {
 # ------------------------------------------------------------ Kapitel 6,1–4
 "MAT.6.1": "Achtet{1} darauf, [eure]{5} [Gerechtigkeit]{3,4} nicht{6} [vor]{8} [den Menschen]{9,10} [zu üben]{7}, [um]{11,12} [von ihnen]{14} [gesehen zu werden]{13}; [sonst]{15-18:idiom} [habt ihr]{21} keinen{20} [Lohn]{19} [bei]{22} [eurem]{25} [Vater]{23,24} [in den Himmeln]{26-29}. ~2(«aber»; überleitend, nicht eigens wiedergegeben)",
 "MAT.6.2": "Wenn{1} [du]{3} nun{2} [Almosen]{4} [gibst]{3}, [blas]{6} nicht{5} [die Posaune]{6} [vor]{7} [dir]{8} [her]{7}, wie{9} [die Heuchler]{10,11} [es]{12} [in]{13} [den Synagogen]{14,15} und{16} [in]{17} [den Gassen]{18,19} [tun]{12}, damit{20} [sie]{21} [von]{22} [den Menschen]{23,24} [gerühmt werden]{21}. Amen{25}, [ich sage]{26} [euch]{27}: [Sie haben]{28} [ihren]{31} [Lohn]{29,30} [schon erhalten]{28}.",
 "MAT.6.3": "Wenn{3} du{1} aber{2} [Almosen]{4} [gibst]{3}, [soll]{6} [deine]{9} [linke Hand]{7,8} nicht{5} [wissen]{6}, [was]{10} [deine]{14} [rechte]{12,13} [tut]{11},",
 "MAT.6.4": "damit{1} [dein]{3} [Almosen]{4,5} [im Verborgenen]{6-8} [bleibt]{2}; und{9} [dein]{12} [Vater]{10,11}, [der]{13} [ins Verborgene]{15-17} [sieht]{14}, [wird es]{18} [dir]{19} [vergelten]{18}.",
 # ------------------------------------------------------------ Kapitel 6,16–34
 "MAT.6.16": "Wenn{1} [ihr]{3} aber{2} [fastet]{3}, [macht]{5} kein{4} [düsteres Gesicht]{9} wie{6} [die Heuchler]{7,8}; denn{11} [sie machen]{10} [ihr]{14} [Gesicht]{12,13} [unkenntlich]{10}, damit{15} [die Menschen]{17,18} [sehen]{16}, dass sie [fasten]{19}. Amen{20}, [ich sage]{21} [euch]{22}: [Sie haben]{23} [ihren]{26} [Lohn]{24,25} [schon erhalten]{23}.",
 "MAT.6.17": "Du{1} aber{2}, [wenn du fastest]{3}, [salbe]{4} [deinen]{5} [Kopf]{6,7} und{8} [wasche]{12} [dein]{11} [Gesicht]{9,10},",
 "MAT.6.18": "damit{1} nicht{2} [die Menschen]{4,5} [sehen]{3}, dass du [fastest]{6}, sondern{7} [dein]{10} [Vater]{8,9}, [der]{11} [im Verborgenen]{12-14} ist; und{15} [dein]{18} [Vater]{16,17}, [der]{19} [ins Verborgene]{21-23} [sieht]{20}, [wird es]{24} [dir]{25} [vergelten]{24}.",
 "MAT.6.19": "[Sammelt]{2} [euch]{3} keine{1} [Schätze]{4} [auf]{5} [der Erde]{6,7}, wo{8} [Motte]{9} und{10} [Frass]{11} [zerstören]{12} und{13} wo{14} [Diebe]{15} [einbrechen]{16} und{17} [stehlen]{18}.",
 "MAT.6.20": "[Sammelt]{1} [euch]{3} aber{2} [Schätze]{4} [im]{5} [Himmel]{6}, wo{7} weder{8} [Motte]{9} noch{10} [Frass]{11} [zerstören]{12} und{13} wo{14} [Diebe]{15} nicht{16} [einbrechen]{17} [und nicht]{18} [stehlen]{19}.",
 "MAT.6.21": "Denn{2} wo{1} [dein]{6} [Schatz]{4,5} [ist]{3}, dort{7} [wird]{8} auch{9} [dein]{12} [Herz]{10,11} [sein]{8}.",
 "MAT.6.22": "[Die Lampe]{1,2} [des Leibes]{3,4} [ist]{5} [das Auge]{6,7}. Wenn{8} nun{9} [dein]{13} [Auge]{11,12} [klar]{14} [ist]{10}, [wird]{20} [dein]{18} [ganzer]{15} [Leib]{16,17} [hell]{19} [sein]{20}.",
 "MAT.6.23": "Wenn{1} aber{2} [dein]{5} [Auge]{3,4} [schlecht]{6} [ist]{7}, [wird]{13} [dein]{11} [ganzer]{8} [Leib]{9,10} [finster]{12} [sein]{13}. Wenn{14} nun{15} [das Licht]{16,17} [in dir]{18-20} [Finsternis]{21} [ist]{22}, [wie gross]{25} ist dann [die Finsternis]{23,24}!",
 "MAT.6.24": "Niemand{1} kann{2} [zwei]{3} [Herren]{4} [dienen]{5}; denn{7} entweder{6} [wird er]{10} [den einen]{8,9} [hassen]{10} und{11} [den anderen]{12,13} [lieben]{14}, oder{15} [er wird]{17} [dem einen]{16} [anhängen]{17} und{18} [den anderen]{19,20} [verachten]{21}. [Ihr könnt]{23} nicht{22} [Gott]{24} [dienen]{25} und{26} [dem Mammon]{27}.",
 "MAT.6.25": "[Darum]{1,2} [sage ich]{3} [euch]{4}: [Sorgt euch]{6} nicht{5} [um]{7} [euer]{9} [Leben]{8}, was{10} [ihr essen sollt]{11}, [und auch nicht]{12} [um]{13} [euren]{15} [Leib]{14}, was{16} [ihr anziehen sollt]{17}. [Ist]{22} nicht{18} [das Leben]{19,20} [mehr]{21} [als]{23} [die Nahrung]{24} und{25} [der Leib]{26,27} mehr [als die Kleidung]{28,29}?",
 "MAT.6.26": "[Schaut]{1} [auf]{2} [die Vögel]{3,4} [des Himmels]{5,6}: [Sie säen]{9} nicht{8}, [sie ernten]{11} nicht{10} und [sammeln]{13} [auch nicht]{12} [in]{14} [Scheunen]{15}, und{16} [euer]{19} [himmlischer]{20,21} [Vater]{17,18} [ernährt]{22} [sie]{23}. [Seid]{27} [ihr]{25} nicht{24} [viel mehr]{26} [wert]{27} [als sie]{28}? ~7(«dass»; im Doppelpunkt aufgegangen)",
 "MAT.6.27": "Wer{1} aber{2} [von]{3} [euch]{4} kann{6} [durch sein Sorgen]{5} [seiner]{11} [Lebenszeit]{9,10} [eine einzige]{13} [Elle]{12} [hinzufügen]{7,8}?",
 "MAT.6.28": "Und{1} [warum]{4} [sorgt ihr euch]{5} [um]{2} [Kleidung]{3}? [Seht euch]{6} [die Lilien]{7,8} [des Feldes]{9,10} [genau an]{6}, wie{11} [sie wachsen]{12}: [Sie mühen sich]{14} nicht{13} [ab]{14} und [spinnen]{16} [auch nicht]{15}.",
 "MAT.6.29": "[Ich sage]{1} [euch]{3} aber{2}: [Nicht einmal]{5} Salomo{6} [in]{7} [all]{8} [seiner]{11} [Pracht]{9,10} [war gekleidet]{12} wie{13} [eine]{14} [von diesen]{15}. ~4(leitet die Rede ein)",
 "MAT.6.30": "Wenn{1} aber{2} Gott{14,15} [das Gras]{3,4} [des Feldes]{5,6}, [das]{8} heute{7} [steht]{8} und{9} morgen{10} [in]{11} [den Ofen]{12} [geworfen wird]{13}, so{16} [kleidet]{17}, wird er dann nicht{18} [viel]{19} [mehr]{20} [euch]{21} kleiden, [ihr Kleingläubigen]{22}?",
 "MAT.6.31": "[Sorgt euch]{3} also{2} nicht{1} [und sagt]{4}: «Was{5} [sollen wir essen]{6}?», oder{7}: «Was{8} [sollen wir trinken]{9}?», oder{10}: «Was{11} [sollen wir anziehen]{12}?»",
 "MAT.6.32": "Denn{2} [nach all dem]{1,3} [trachten]{6} [die Heiden]{4,5}; [euer]{11} [himmlischer]{12,13} [Vater]{9,10} [weiss]{7} ja{8}, dass{14} [ihr]{15} [das alles]{16,17} [braucht]{15}.",
 "MAT.6.33": "[Sucht]{1} aber{2} zuerst{3} [das Reich]{4,5} und{6} [seine]{9} [Gerechtigkeit]{7,8}, und{10} [dies alles]{11,12} [wird]{13} [euch]{14} [dazugegeben]{13}.",
 "MAT.6.34": "[Sorgt euch]{3} also{2} nicht{1} [um]{4} [den morgigen Tag]{5,6}; denn{8} [der morgige Tag]{7,9} [wird]{10} [für sich selbst]{11} [sorgen]{10}. [Es genügt]{12} [dem]{13} [Tag]{14} [seine]{17} [eigene Plage]{15,16}.",
 # ------------------------------------------------------------ Kapitel 7
 "MAT.7.1": "[Richtet]{2} nicht{1}, damit{3} [ihr]{5} nicht{4} [gerichtet werdet]{5}.",
 "MAT.7.2": "Denn{3} [mit welchem]{1,2} [Urteil]{4} [ihr richtet]{5}, [werdet ihr gerichtet werden]{6}, und{7} [mit welchem]{8,9} [Mass]{10} [ihr messt]{11}, [wird]{12} [euch]{13} [gemessen werden]{12}.",
 "MAT.7.3": "Warum{1} aber{2} [siehst du]{3} [den Splitter]{4,5} [im]{6-8} [Auge]{9} [deines]{12} [Bruders]{10,11}, [den Balken]{13,19} aber{14} [in]{15,16} [deinem eigenen]{17} [Auge]{18} [bemerkst du]{21} nicht{20}?",
 "MAT.7.4": "Oder{1} wie{2} [kannst du]{3} [zu]{4} [deinem]{6} [Bruder]{5} [sagen]{3}: «[Lass mich]{7} [den Splitter]{9,10} [aus]{11} [deinem]{14} [Auge]{12,13} [herausziehen]{8}», und{15} siehe{16}, [in]{19,20} [deinem]{22} [Auge]{21} ist [der Balken]{17,18}?",
 "MAT.7.5": "[Du Heuchler]{1}! [Zieh]{2} zuerst{3} [den Balken]{8,9} [aus]{4} [deinem]{7} [Auge]{5,6} [heraus]{2}, und{10} dann{11} [wirst du klar sehen]{12}, um [den Splitter]{14,15} [aus]{16} [dem Auge]{17,18} [deines]{21} [Bruders]{19,20} [herauszuziehen]{13}.",
 "MAT.7.6": "[Gebt]{2} [das Heilige]{3,4} nicht{1} [den Hunden]{5,6}, [und werft]{8} [eure]{11} [Perlen]{9,10} [auch nicht]{7} [vor]{12} [die Schweine]{13,14}, damit{15} [sie]{16} [diese]{17} nicht{15} [mit]{18} [ihren]{21} [Füssen]{19,20} [zertreten]{16} und{22} [sich umdrehen]{23} und [euch]{25} [zerreissen]{24}.",
 "MAT.7.7": "Bittet{1}, und{2} [es wird]{3} [euch]{4} [gegeben werden]{3}; sucht{5}, und{6} [ihr werdet finden]{7}; [klopft an]{8}, und{9} [es wird]{10} [euch]{11} [geöffnet werden]{10}.",
 "MAT.7.8": "Denn{2} [jeder]{1}, [der bittet]{3,4}, [empfängt]{5}, und{6} [wer sucht]{7,8}, [findet]{9}, und{10} [wer anklopft]{11,12}, [dem wird geöffnet werden]{13}.",
 "MAT.7.9": "Oder{1} wer{2} [ist]{3} [unter]{4} [euch]{5} [ein Mensch]{6}, [den]{7} [sein]{11} [Sohn]{9,10} [um Brot]{12} [bittet]{8} – [wird er]{15} [ihm]{16} [etwa]{13} [einen Stein]{14} [geben]{15}?",
 "MAT.7.10": "Oder{1} [er bittet]{4} auch{2} [um einen Fisch]{3} – [wird er]{7} [ihm]{8} [etwa]{5} [eine Schlange]{6} [geben]{7}?",
 "MAT.7.11": "Wenn{1} nun{2} ihr{3}, [die ihr]{5} [böse]{4} [seid]{5}, [euren]{12} [Kindern]{10,11} [gute]{8} [Gaben]{7} [zu geben]{9} [wisst]{6}, [wie viel]{13} [mehr]{14} [wird]{22} [euer]{17} [Vater]{15,16} [in den Himmeln]{18-21} [denen]{24} [Gutes]{23} [geben]{22}, die [ihn]{26} [bitten]{25}!",
 "MAT.7.12": "[Alles]{1} nun{2}, [was]{3,4} [ihr wollt]{5}, dass{6} [euch]{8} [die Menschen]{9,10} [tun]{7}, so{11} [tut]{14} auch{12} ihr{13} [ihnen]{15}; denn{17} das{16} [ist]{18} [das Gesetz]{19,20} und{21} [die Propheten]{22,23}.",
 "MAT.7.13": "[Geht hinein]{1} [durch]{2} [das enge]{3,4} [Tor]{5}! Denn{6} [weit]{7} ist [das Tor]{8,9} und{10} [breit]{11} [der Weg]{12,13}, [der]{14} [ins]{16,17} [Verderben]{18} [führt]{15}, und{19} viele{20} [sind es]{21}, [die]{22} [dort]{24,25} [hineingehen]{23}.",
 "MAT.7.14": "Denn{1} [eng]{2} ist [das Tor]{3,4} und{5} [schmal]{6} [der Weg]{7,8}, [der]{9} [ins]{11,12} [Leben]{13} [führt]{10}, und{14} wenige{15} [sind es]{16}, [die]{17} [ihn]{19} [finden]{18}.",
 "MAT.7.15": "[Hütet euch]{1} [vor]{2} [den falschen Propheten]{3,4}, [die]{5} [in]{9} [Schafskleidern]{10,11} [zu]{7} [euch]{8} [kommen]{6}; [innen]{12} aber{13} [sind sie]{14} [reissende]{16} [Wölfe]{15}.",
 "MAT.7.16": "[An]{1} [ihren]{4} [Früchten]{2,3} [werdet ihr]{5} [sie]{6} [erkennen]{5}. [Sammelt man]{8} [etwa]{7} [Trauben]{11} [von]{9} [Dornen]{10} oder{12} [Feigen]{15} [von]{13} [Disteln]{14}?",
 "MAT.7.17": "So{1} [bringt]{7} [jeder]{2} [gute]{4} [Baum]{3} [gute]{6} [Früchte]{5}, [der faule]{8,10} [Baum]{11} aber{9} [bringt]{14} [schlechte]{13} [Früchte]{12}.",
 "MAT.7.18": "[Ein guter]{4} [Baum]{3} kann{2} nicht{1} [schlechte]{6} [Früchte]{5} [bringen]{7}, [und ebenso wenig]{8} kann [ein fauler]{10} [Baum]{9} [gute]{12} [Früchte]{11} [bringen]{13}.",
 "MAT.7.19": "[Jeder]{1} [Baum]{2}, [der]{4} [keine]{3} [gute]{6} [Frucht]{5} [bringt]{4}, [wird umgehauen]{7} und{8} [ins]{9} [Feuer]{10} [geworfen]{11}.",
 "MAT.7.20": "[Also]{1,2} [an]{3} [ihren]{6} [Früchten]{4,5} [werdet ihr]{7} [sie]{8} [erkennen]{7}.",
 "MAT.7.21": "[Nicht]{1} [jeder]{2}, [der]{3} [zu mir]{5} [sagt]{4}: «Herr{6}, Herr{7}!», [wird]{8} [in]{9} [das Reich]{10,11} [der Himmel]{12,13} [hineinkommen]{8}, sondern{14} [wer]{15} [den Willen]{17,18} [meines]{21} [Vaters]{19,20} [in den Himmeln]{22-25} [tut]{16}.",
 "MAT.7.22": "Viele{1} [werden]{2} [an]{4} [jenem]{5} [Tag]{6,7} [zu mir]{3} [sagen]{2}: «Herr{8}, Herr{9}, [haben wir]{14} nicht{10} [in deinem]{11,12} [Namen]{13} [prophezeit]{14} und{15} [in deinem]{16,17} [Namen]{18} [Dämonen]{19} [ausgetrieben]{20} und{21} [in deinem]{22,23} [Namen]{24} [viele]{26} [Machttaten]{25} [getan]{27}?»",
 "MAT.7.23": "Und{1} dann{2} [werde ich]{3} [ihnen]{4} [offen erklären]{3}: «[Nie]{6} [habe ich]{7} [euch]{8} [gekannt]{7}. [Weicht]{9} [von]{10} [mir]{11}, [die ihr]{12,13} [Gesetzlosigkeit]{14,15} [übt]{12,13}!» ~5(leitet die direkte Rede ein)",
 "MAT.7.24": "[Jeder]{1} nun{2}, [der]{3} [diese]{8} [meine]{5} [Worte]{6,7} [hört]{4} und{9} [sie]{11} [tut]{10}, [wird]{12} [einem klugen]{14} [Mann]{13} [gleichen]{12}, [der]{15} [sein]{17} [Haus]{18,19} [auf]{20} [den Felsen]{21,22} [gebaut hat]{16}.",
 "MAT.7.25": "Und{1} [der Regen]{3,4} [fiel]{2}, und{5} [die Fluten]{7,8} [kamen]{6}, und{9} [die Winde]{11,12} [wehten]{10} und{13} [prallten]{14} [gegen]{15} [jenes]{17} [Haus]{16}, und{18} [es stürzte]{20} nicht{19} [ein]{20}; denn{22} [es war]{21} [auf]{23} [den Felsen]{24,25} [gegründet]{21}.",
 "MAT.7.26": "Und{1} [jeder]{2}, [der]{3} [diese]{8} [meine]{5} [Worte]{6,7} [hört]{4} und{9} [sie]{12} nicht{10} [tut]{11}, [wird]{13} [einem törichten]{15} [Mann]{14} [gleichen]{13}, [der]{16} [sein]{18} [Haus]{19,20} [auf]{21} [den Sand]{22,23} [gebaut hat]{17}.",
 "MAT.7.27": "Und{1} [der Regen]{3,4} [fiel]{2}, und{5} [die Fluten]{7,8} [kamen]{6}, und{9} [die Winde]{11,12} [wehten]{10} und{13} [schlugen]{14} [an]{15} [jenes]{17} [Haus]{16}, und{18} [es stürzte ein]{19}, und{20} [sein]{24} [Einsturz]{22,23} [war]{21} [gewaltig]{25}.",
 "MAT.7.28": "Und{1} [es geschah]{2}, als{3} Jesus{5,6} [diese]{9} [Worte]{7,8} [beendet hatte]{4}, [da war]{10} [die Menge]{11,12} [überwältigt]{10} [von]{13} [seiner]{16} [Lehre]{14,15};",
 "MAT.7.29": "denn{2} [er lehrte]{1,3} [sie]{4} [wie]{5} einer, der [Vollmacht]{6} [hat]{7}, und{8} nicht{9} [wie]{10} [ihre]{13} [Schriftgelehrten]{11,12}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 6,1–4
 "MAT.6.1": "[Passed uf]{1}, dass [ir]{7} [eui]{5} [Grächtigkeit]{3,4} nöd{6} [vor]{8} [de Lüüt]{9,10} [üebed]{7}, [demit]{11,12} [si]{14} [eu gseend]{13}; [suscht]{15-18:idiom} [händ ir]{21} kei{20} [Loon]{19} [bi]{22} [euem]{25} [Vatter]{23,24} [i de Himel]{26-29}. ~2(«aber»; überleitend, nöd extra wiedergää)",
 "MAT.6.2": "Wänn{1} [du]{3} also{2} [Almose]{4} [gisch]{3}, [blaas]{6} nöd{5} [d Posuune]{6} [vor]{7} [dir]{8} [här]{7}, wie{9} [s]{12} [d Hüüchler]{10,11} [i]{13} [de Synagoge]{14,15} und{16} [i]{17} [de Gasse]{18,19} [mached]{12}, demit{20} [si]{21} [vo]{22} [de Lüüt]{23,24} [grüemt wärded]{21}. Amen{25}, [ich säg]{26} [eu]{27}: [Si händ]{28} [ire]{31} [Loon]{29,30} [scho übercho]{28}.",
 "MAT.6.3": "Wänn{3} du{1} aber{2} [Almose]{4} [gisch]{3}, [söll]{6} [dini]{9} [linggi Hand]{7,8} nöd{5} [wüsse]{6}, [was]{10} [dini]{14} [rächti]{12,13} [macht]{11},",
 "MAT.6.4": "demit{1} [diis]{3} [Almose]{4,5} [im Verborgne]{6-8} [bliibt]{2}; und{9} [diin]{12} [Vatter]{10,11}, [wo]{13} [is Verborgne]{15-17} [gseet]{14}, [wird s]{18} [dir]{19} [vergälte]{18}.",
 # ------------------------------------------------------------ Kapitel 6,16–34
 "MAT.6.16": "Wänn{1} [ir]{3} aber{2} [faschted]{3}, [mached]{5} kei{4} [finschters Gsicht]{9} wie{6} [d Hüüchler]{7,8}; [si mached]{10} nämli{11} [ires]{14} [Gsicht]{12,13} [unkänntlich]{10}, demit{15} [d Lüüt]{17,18} [gseend]{16}, dass si [faschted]{19}. Amen{20}, [ich säg]{21} [eu]{22}: [Si händ]{23} [ire]{26} [Loon]{24,25} [scho übercho]{23}.",
 "MAT.6.17": "Du{1} aber{2}, [wänn du faschtisch]{3}, [salb]{4} [diin]{5} [Chopf]{6,7} und{8} [wäsch]{12} [diis]{11} [Gsicht]{9,10},",
 "MAT.6.18": "demit{1} nöd{2} [d Lüüt]{4,5} [gseend]{3}, dass du [faschtisch]{6}, sondern{7} [diin]{10} [Vatter]{8,9}, [wo]{11} [im Verborgne]{12-14} isch; und{15} [diin]{18} [Vatter]{16,17}, [wo]{19} [is Verborgne]{21-23} [gseet]{20}, [wird s]{24} [dir]{25} [vergälte]{24}.",
 "MAT.6.19": "[Sammled]{2} [eu]{3} kei{1} [Schätz]{4} [uf]{5} [de Ärde]{6,7}, wo{8} [Schabe]{9} und{10} [Frass]{11} [alles kaputt mached]{12} und{13} wo{14} [Dieb]{15} [iibräched]{16} und{17} [stääled]{18}.",
 "MAT.6.20": "[Sammled]{1} [eu]{3} aber{2} [Schätz]{4} [im]{5} [Himel]{6}, wo{7} weder{8} [Schabe]{9} no{10} [Frass]{11} [öppis kaputt mached]{12} und{13} wo{14} [Dieb]{15} nöd{16} [iibräched]{17} [und nöd]{18} [stääled]{19}.",
 "MAT.6.21": "Dänn{2} wo{1} [diin]{6} [Schatz]{4,5} [isch]{3}, dört{7} [wird]{8} au{9} [diis]{12} [Härz]{10,11} [sii]{8}.",
 "MAT.6.22": "[D Lampe]{1,2} [vom Liib]{3,4} [isch]{5} [s Aug]{6,7}. Wänn{8} also{9} [diis]{13} [Aug]{11,12} [klar]{14} [isch]{10}, [wird]{20} [diin]{18} [ganz]{15} [Liib]{16,17} [hell]{19} [sii]{20}.",
 "MAT.6.23": "Wänn{1} aber{2} [diis]{5} [Aug]{3,4} [schlächt]{6} [isch]{7}, [wird]{13} [diin]{11} [ganz]{8} [Liib]{9,10} [fiischter]{12} [sii]{13}. Wänn{14} also{15} [s Liecht]{16,17} [i dir]{18-20} [Fiischteri]{21} [isch]{22}, [wie gross]{25} isch dänn [d Fiischteri]{23,24}!",
 "MAT.6.24": "Niemer{1} [cha]{2} [zwei]{3} [Herre]{4} [diene]{5}; dänn{7} entweder{6} [hasst er]{10} [de eint]{8,9} und{11} [liebt]{14} [de ander]{12,13}, oder{15} [er hanget]{17} [am eint]{16} [aa]{17} und{18} [verachtet]{21} [de ander]{19,20}. [Ir chönd]{23} nöd{22} [Gott]{24} [diene]{25} und{26} [em Mammon]{27}.",
 "MAT.6.25": "[Drum]{1,2} [säg ich]{3} [eu]{4}: [Mached eu]{6} kei{5} [Sorge]{6} [um]{7} [eues]{9} [Läbe]{8}, was{10} [ir ässed]{11}, [und au nöd]{12} [um]{13} [eue]{15} [Liib]{14}, was{16} [ir aalegged]{17}. [Isch]{22} nöd{18} [s Läbe]{19,20} [meh]{21} [als]{23} [s Ässe]{24} und{25} [de Liib]{26,27} meh [als d Chleider]{28,29}?",
 "MAT.6.26": "[Lueged]{1} [d Vögel]{3,4} [am Himel]{5,6} [aa]{2}: [Si säied]{9} nöd{8}, [si ärnted]{11} nöd{10} und [sammled]{13} [au nüüt]{12} [i]{14} [Schüüre]{15} [ii]{13}, und{16} [eue]{19} [himmlisch]{20,21} [Vatter]{17,18} [git]{22} [ene]{23} [z ässe]{22}. [Sind]{27} [ir]{25} nöd{24} [vil meh]{26} [wärt]{27} [als si]{28}? ~7(«dass»; im Doppelpunkt ufgange)",
 "MAT.6.27": "Wer{1} aber{2} [vo]{3} [eu]{4} [cha]{6}, [wänn er sich Sorge macht]{5}, [sinere]{11} [Läbesziit]{9,10} [e einzigi]{13} [Elle]{12} [dezuetue]{7,8}?",
 "MAT.6.28": "Und{1} [wieso]{4} [mached ir eu Sorge]{5} [um]{2} [d Chleider]{3}? [Lueged]{6} [d Lilie]{7,8} [uf em Fäld]{9,10} [gnau aa]{6}, wie{11} [si wachsed]{12}: [Si chrampfed]{14} nöd{13} und [spinned]{16} [au nöd]{15}.",
 "MAT.6.29": "[Ich säg]{1} [eu]{3} aber{2}: [Nöd emal]{5} [de Salomo]{6} [i]{7} [all]{8} [sinere]{11} [Pracht]{9,10} [isch aagleit gsii]{12} wie{13} [eini]{14} [vo dene]{15}. ~4(leitet di direkt Red ii)",
 "MAT.6.30": "Wänn{1} aber{2} [Gott]{14,15} [s Gras]{3,4} [uf em Fäld]{5,6}, [wo]{8} hüt{7} [staat]{8} und{9} morn{10} [in]{11} [Ofe]{12} [gworfe wird]{13}, eso{16} [aaleit]{17}, wird er dänn nöd{18} [vil]{19} [meh]{20} [eu]{21} aalegge, [ir Chliigläubige]{22}?",
 "MAT.6.31": "[Mached eu]{3} also{2} kei{1} [Sorge]{3} [und säged]{4}: «Was{5} [söled mir ässe]{6}?», oder{7}: «Was{8} [söled mir trinke]{9}?», oder{10}: «Was{11} [söled mir aalegge]{12}?»",
 "MAT.6.32": "[All das]{1,3} [sueched]{6} nämli{2} [d Heide]{4,5}; [eue]{11} [himmlisch]{12,13} [Vatter]{9,10} [weiss]{7} ja{8}, dass{14} [ir]{15} [das alles]{16,17} [bruuched]{15}.",
 "MAT.6.33": "[Sueched]{1} aber{2} zerscht{3} [s Riich]{4,5} und{6} [sini]{9} [Grächtigkeit]{7,8}, und{10} [das alles]{11,12} [wird]{13} [eu]{14} [dezue ggää]{13}.",
 "MAT.6.34": "[Mached eu]{3} also{2} kei{1} [Sorge]{3} [um]{4} [de morgig Tag]{5,6}; dänn{8} [de morgig Tag]{7,9} [wird]{10} [für sich sälber]{11} [sorge]{10}. [Jedem]{13} [Tag]{14} [längt]{12} [sini]{17} [eiget Plaag]{15,16}.",
 # ------------------------------------------------------------ Kapitel 7
 "MAT.7.1": "[Richted]{2} nöd{1}, demit{3} [ir]{5} nöd{4} [grichtet wärded]{5}.",
 "MAT.7.2": "Dänn{3} [mit em]{1} [Urteil]{4}, [wo]{2} [ir richted]{5}, [wärded ir grichtet]{6}, und{7} [mit em]{8} [Mass]{10}, [wo]{9} [ir mässed]{11}, [wird]{12} [eu]{13} [gmässe]{12}.",
 "MAT.7.3": "Wieso{1} aber{2} [gseesch du]{3} [de Splitter]{4,5} [im]{6-8} [Aug]{9} [vo dim]{12} [Brueder]{10,11}, [de Balke]{13,19} aber{14} [i]{15,16} [dim eigete]{17} [Aug]{18} [merksch du]{21} nöd{20}?",
 "MAT.7.4": "Oder{1} wie{2} [chasch du]{3} [zu]{4} [dim]{6} [Brueder]{5} [säge]{3}: «[La mich]{7} [de Splitter]{9,10} [us]{11} [dim]{14} [Aug]{12,13} [usezie]{8}», und{15} lueg{16}, [i]{19,20} [dim]{22} [Aug]{21} isch [de Balke]{17,18}?",
 "MAT.7.5": "[Du Hüüchler]{1}! [Zie]{2} zerscht{3} [de Balke]{8,9} [us]{4} [dim]{7} [Aug]{5,6} [use]{2}, und{10} dänn{11} [gseesch du klar]{12}, zum [de Splitter]{14,15} [us]{16} [em Aug]{17,18} [vo dim]{21} [Brueder]{19,20} [usezie]{13}.",
 "MAT.7.6": "[Gänd]{2} [s Heilig]{3,4} nöd{1} [de Hünd]{5,6}, [und rüered]{8} [eui]{11} [Perle]{9,10} [au nöd]{7} [vor]{12} [d Säu]{13,14}, demit{15} [si]{16} [die]{17} nöd{15} [mit]{18} [irne]{21} [Füess]{19,20} [vertrampled]{16} und{22} [sich umdrääied]{23} und [eu]{25} [verriissed]{24}.",
 "MAT.7.7": "Bitted{1}, und{2} [es wird]{3} [eu]{4} [ggää]{3}; sueched{5}, und{6} [ir wärded finde]{7}; [chlopfed aa]{8}, und{9} [es wird]{10} [eu]{11} [uftaa]{10}.",
 "MAT.7.8": "Dänn{2} [jede]{1}, [wo bittet]{3,4}, [überchunnt]{5}, und{6} [wer suecht]{7,8}, [findet]{9}, und{10} [wer aachlopft]{11,12}, [däm wird uftaa]{13}.",
 "MAT.7.9": "Oder{1} wer{2} [vo]{4} [eu]{5} [isch]{3} [en Mänsch]{6}, [wo]{7} [sin]{11} [Sohn]{9,10} [en]{7} [um Broot]{12} [bittet]{8} – [git er]{15} [em]{16} [öppe]{13} [en Stei]{14}?",
 "MAT.7.10": "Oder{1} [er bittet]{4} au{2} [um en Fisch]{3} – [git er]{7} [em]{8} [öppe]{5} [e Schlange]{6}?",
 "MAT.7.11": "Wänn{1} also{2} ir{3}, [wo]{5} [bös]{4} [sind]{5}, [eune]{12} [Chind]{10,11} [gueti]{8} [Gabe]{7} [chönd]{6} [gää]{9}, [wie vil]{13} [meh]{14} [wird]{22} [eue]{17} [Vatter]{15,16} [i de Himel]{18-21} [dene]{24} [Guets]{23} [gää]{22}, wo [en]{26} [drum bitted]{25}!",
 "MAT.7.12": "[Alles]{1} also{2}, [wo]{3,4} [ir wänd]{5}, dass{6} [eu]{8} [d Lüüt]{9,10} [tüend]{7}, eso{11} [tüend]{14} au{12} ir{13} [ine]{15}; dänn{17} das{16} [isch]{18} [s Gsetz]{19,20} und{21} [d Prophete]{22,23}.",
 "MAT.7.13": "[Gönd]{1} [dur]{2} [s äng]{3,4} [Tor]{5} [ine]{1}! Dänn{6} [wiit]{7} isch [s Tor]{8,9} und{10} [breit]{11} [de Wäg]{12,13}, [wo]{14} [is]{16,17} [Verderbe]{18} [füert]{15}, und{19} vil{20} [sind s]{21}, [wo]{22} [dört]{24,25} [inegönd]{23}.",
 "MAT.7.14": "Dänn{1} [äng]{2} isch [s Tor]{3,4} und{5} [schmaal]{6} [de Wäg]{7,8}, [wo]{9} [is]{11,12} [Läbe]{13} [füert]{10}, und{14} wenig{15} [sind s]{16}, [wo]{17} [en]{19} [finded]{18}.",
 "MAT.7.15": "[Hüeted eu]{1} [vor]{2} [de falsche Prophete]{3,4}, [wo]{5} [i]{9} [Schaafchleider]{10,11} [zu]{7} [eu]{8} [chömed]{6}; [inne]{12} aber{13} [sind s]{14} [riissendi]{16} [Wölf]{15}.",
 "MAT.7.16": "[A]{1} [irne]{4} [Frücht]{2,3} [wärded ir]{5} [si]{6} [erchänne]{5}. [List me]{8} [öppe]{7} [Truube]{11} [vo]{9} [Dörn]{10} oder{12} [Fiige]{15} [vo]{13} [Dischtle]{14}?",
 "MAT.7.17": "Eso{1} [bringt]{7} [jede]{2} [guet]{4} [Baum]{3} [gueti]{6} [Frücht]{5}, [de fuul]{8,10} [Baum]{11} aber{9} [bringt]{14} [schlächti]{13} [Frücht]{12}.",
 "MAT.7.18": "[En guete]{4} [Baum]{3} [cha]{2} kei{1} [schlächti]{6} [Frücht]{5} [bringe]{7}, [und au]{8} [en fuule]{10} [Baum]{9} cha [kei]{8} [gueti]{12} [Frücht]{11} [bringe]{13}.",
 "MAT.7.19": "[Jede]{1} [Baum]{2}, [wo]{4} [kei]{3} [gueti]{6} [Frucht]{5} [bringt]{4}, [wird umghaue]{7} und{8} [is]{9} [Füür]{10} [gworfe]{11}.",
 "MAT.7.20": "[Also]{1,2} [a]{3} [irne]{6} [Frücht]{4,5} [wärded ir]{7} [si]{8} [erchänne]{7}.",
 "MAT.7.21": "[Nöd]{1} [jede]{2}, [wo]{3} [zu mir]{5} [seit]{4}: «Herr{6}, Herr{7}!», [chunnt]{8} [is]{9,10} [Riich]{11} [vo de Himel]{12,13} [ine]{8}, sondern{14} [wer]{15} [de Wile]{17,18} [vo mim]{21} [Vatter]{19,20} [i de Himel]{22-25} [tuet]{16}.",
 "MAT.7.22": "Vil{1} [wärded]{2} [a]{4} [dem]{5} [Tag]{6,7} [zu mir]{3} [säge]{2}: «Herr{8}, Herr{9}, [händ mir]{14} nöd{10} [i dim]{11,12} [Name]{13} [profezeit]{14} und{15} [i dim]{16,17} [Name]{18} [Dämone]{19} [ustribe]{20} und{21} [i dim]{22,23} [Name]{24} [vil]{26} [Machttate]{25} [tue]{27}?»",
 "MAT.7.23": "Und{1} dänn{2} [wird ich]{3} [ine]{4} [offe säge]{3}: «[Nie]{6} [han ich]{7} [eu]{8} [kännt]{7}. [Gönd weg]{9} [vo]{10} [mir]{11}, [ir, wo]{12,13} [Gsetzlosigkeit]{14,15} [tüend]{12,13}!» ~5(leitet di direkt Red ii)",
 "MAT.7.24": "[Jede]{1} also{2}, [wo]{3} [die]{8} [Wort]{6,7} [vo mir]{5} [ghört]{4} und{9} [si]{11} [tuet]{10}, [isch wie]{12} [en gschiide]{14} [Maa]{13}, [wo]{15} [sis]{17} [Huus]{18,19} [uf]{20} [de Fels]{21,22} [buut hät]{16}.",
 "MAT.7.25": "Und{1} [de Räge]{3,4} [isch abecho]{2}, und{5} [s Hochwasser]{7,8} [isch choo]{6}, und{9} [d Wind]{11,12} [händ bloose]{10} und{13} [sind]{14} [gäge]{15} [das]{17} [Huus]{16} [prallt]{14}, und{18} [es isch]{20} nöd{19} [iigstürzt]{20}; [es isch]{21} nämli{22} [uf]{23} [em Fels]{24,25} [gründet gsii]{21}.",
 "MAT.7.26": "Und{1} [jede]{2}, [wo]{3} [die]{8} [Wort]{6,7} [vo mir]{5} [ghört]{4} und{9} [si]{12} nöd{10} [tuet]{11}, [isch wie]{13} [en tumme]{15} [Maa]{14}, [wo]{16} [sis]{18} [Huus]{19,20} [uf]{21} [de Sand]{22,23} [buut hät]{17}.",
 "MAT.7.27": "Und{1} [de Räge]{3,4} [isch abecho]{2}, und{5} [s Hochwasser]{7,8} [isch choo]{6}, und{9} [d Wind]{11,12} [händ bloose]{10} und{13} [händ]{14} [a]{15} [das]{17} [Huus]{16} [gschlage]{14}, und{18} [es isch iigstürzt]{19}, und{20} [sin]{24} [Iisturz]{22,23} [isch]{21} [gwaltig]{25} [gsii]{21}.",
 "MAT.7.28": "Und{1} [es isch gscheh]{2}: [Wo]{3} [de Jesus]{5,6} mit [dene]{9} [Wort]{7,8} [fertig gsii isch]{4}, [isch]{10} [d Mängi]{11,12} [überwältiget gsii]{10} [vo]{13} [sinere]{16} [Lehr]{14,15};",
 "MAT.7.29": "[er hät]{1,3} [si]{4} nämli{2} [gleert]{1,3} [wie]{5} eine, wo [Vollmacht]{6} [hät]{7}, und{8} nöd{9} [wie]{10} [iri]{13} [Schriftgelehrte]{11,12}.",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, andere Möglichkeiten, Hinweis)
DEC_DE = [
 ("MAT.6.1", "Gerechtigkeit", "interpretive", "δικαιοσύνην", None, ["Frömmigkeit", "fromme Werke"],
  "δικαιοσύνη ist ein Leitwort des Matthäus ([[MAT.3.15]], [[MAT.5.6]], [[MAT.5.10]], [[MAT.5.20]], [[MAT.6.33]], [[MAT.21.32]]): das Tun, das Gottes Willen entspricht. Hier steht es als Überschrift über Almosen, Beten und Fasten ([[MAT.6.2-MAT.6.18]]). Die Wiedergabe bleibt in ganz Matthäus «Gerechtigkeit», damit die Verbindungen sichtbar bleiben. Zur Lesart «Almosen» siehe die Alternativen."),
 ("MAT.6.1", "zu üben", "adapted", "ποιεῖν", "zu tun", None, "«Gerechtigkeit tun» ist im Deutschen ungewohnt."),
 ("MAT.6.1", "sonst", "adapted", "εἰ δὲ μή γε", "wenn aber nicht", None, "Feste Wendung."),
 ("MAT.6.1", "Lohn", "literal", "μισθὸν", None, ["Belohnung"], "μισθός ist der Lohn eines Arbeiters; ebenso in [[MAT.6.2]], [[MAT.6.5]] und [[MAT.6.16]]."),
 ("MAT.6.1", "in den Himmeln", "literal", "τῷ ἐν τοῖς οὐρανοῖς", None, ["im Himmel"], "Plural wie in [[MAT.6.9]]."),
 ("MAT.6.2", "Almosen", "traditional", "ἐλεημοσύνην", "Barmherzigkeit", ["Spende", "Gabe für die Armen"],
  "ἐλεημοσύνη (von ἔλεος, «Erbarmen») ist die Gabe für Arme; neben Gebet und Fasten eine der grundlegenden Übungen jüdischer Frömmigkeit. «Almosen» folgt der vertrauten Wiedergabe, ebenso in [[MAT.6.3-MAT.6.4]]."),
 ("MAT.6.2", "blas nicht die Posaune vor dir her", "interpretive", "μὴ σαλπίσῃς ἔμπροσθέν σου", "trompete nicht vor dir her", ["posaune es nicht aus"],
  "Ob ein tatsächlicher Brauch gemeint ist (vermutet werden Trompetensignale bei öffentlichen Spenden oder die trompetenförmigen Opferkästen im Tempel) oder ein Bild für Selbstdarstellung, ist unsicher; ein solcher Brauch ist nicht sicher belegt."),
 ("MAT.6.2", "Heuchler", "traditional", "ὑποκριταὶ", "Schauspieler", None,
  "ὑποκριτής hiess ursprünglich «Schauspieler», der unter einer Maske spielt; das Bild passt zum Auftreten «vor den Menschen». Gemeint ist eine Haltung, nicht eine bestimmte Gruppe. Wie in [[MAT.6.5]], [[MAT.6.16]] und [[MAT.7.5]]."),
 ("MAT.6.2", "Gassen", "literal", "ῥύμαις", None, ["Strassen"], "ῥύμη ist die enge Gasse; in [[MAT.6.5]] stehen die breiten Strassen (πλατεῖαι)."),
 ("MAT.6.2", "gerühmt werden", "adapted", "δοξασθῶσιν", "verherrlicht werden", ["geehrt werden"], "δοξάζω heisst «Ansehen geben, rühmen»; in [[MAT.5.16]] von Gott gesagt."),
 ("MAT.6.2", "Amen, ich sage euch", "traditional", "ἀμὴν λέγω ὑμῖν", None, ["Wahrlich, ich sage euch"],
  "Das hebräische Wort «amen» («gewiss, fest») steht hier vor der Aussage und bekräftigt sie; in den Evangelien so nur im Mund Jesu. Einheitlich in ganz Matthäus."),
 ("MAT.6.2", "Sie haben ihren Lohn schon erhalten", "literal", "ἀπέχουσιν τὸν μισθὸν αὐτῶν", "Sie haben ihren Lohn empfangen", None,
  "ἀπέχω ist der Ausdruck der Quittung: «vollständig erhalten»; mehr ist nicht zu erwarten. Wie in [[MAT.6.5]] und [[MAT.6.16]]."),
 ("MAT.6.3", "soll deine linke Hand nicht wissen, was deine rechte tut", "literal", "μὴ γνώτω ἡ ἀριστερά σου τί ποιεῖ ἡ δεξιά σου", None, None,
  "Bildhafte Zuspitzung: Das Geben soll so unauffällig geschehen, dass man nicht einmal selbst Aufhebens davon macht."),
 ("MAT.6.4", "im Verborgenen bleibt", "adapted", "ᾖ σου ἡ ἐλεημοσύνη ἐν τῷ κρυπτῷ", "im Verborgenen sei", None, None),
 ("MAT.6.4", "ins Verborgene sieht", "literal", "βλέπων ἐν τῷ κρυπτῷ", "im Verborgenen sieht", None, "Wie in [[MAT.6.6]]: Gott sieht, was Menschen nicht sehen."),
 ("MAT.6.4", "vergelten", "literal", "ἀποδώσει", None, ["belohnen", "erstatten"],
  "ἀποδίδωμι heisst «zurückgeben, erstatten»; womit, sagt der Text nicht. Zu den Lesarten «er selbst» und «öffentlich» siehe die Alternativen."),
 ("MAT.6.16", "macht kein düsteres Gesicht", "adapted", "μὴ γίνεσθε ὡς οἱ ὑποκριταὶ σκυθρωποί", "werdet nicht düster blickend", None, None),
 ("MAT.6.16", "machen ihr Gesicht unkenntlich", "interpretive", "ἀφανίζουσιν τὰ πρόσωπα αὐτῶν", "lassen ihr Gesicht verschwinden", ["entstellen ihr Gesicht", "verhüllen ihr Gesicht"],
  "ἀφανίζω heisst «unsichtbar machen, verschwinden lassen», in [[MAT.6.19]] «zerstören». Gedacht ist wohl an Ungepflegtsein, Asche auf dem Kopf oder Verhüllen als Zeichen von Trauer und Busse. Wortspiel mit φανῶσιν («damit sie erscheinen»): Sie machen ihr Gesicht unsichtbar, um gesehen zu werden."),
 ("MAT.6.16", "damit die Menschen sehen, dass sie fasten", "adapted", "ὅπως φανῶσιν τοῖς ἀνθρώποις νηστεύοντες", "damit sie den Menschen als Fastende erscheinen", None, "Ebenso in [[MAT.6.18]]."),
 ("MAT.6.17", "salbe deinen Kopf", "literal", "ἄλειψαί σου τὴν κεφαλὴν", None, ["öle dein Haar"],
  "Öl auf Kopf und Haar gehörte zur täglichen Körperpflege und zur Festfreude; in der Trauer liess man es weg (vgl. [[2SA.14.2]]). Wer fastet, soll aussehen wie an einem gewöhnlichen Tag."),
 ("MAT.6.18", "im Verborgenen", "literal", "ἐν τῷ κρυφαίῳ", None, None,
  "κρυφαῖος ist sinngleich mit κρυπτός in [[MAT.6.4]] und [[MAT.6.6]]; die Wiedergabe ist dieselbe. Manche Editionen lesen hier κρυπτῷ; die Übersetzung ändert sich dadurch nicht."),
 ("MAT.6.19", "Sammelt euch keine Schätze", "literal", "Μὴ θησαυρίζετε ὑμῖν θησαυροὺς", "Häuft euch keine Schätze auf", None, "Verb und Objekt haben im Griechischen denselben Stamm (θησαυρίζω, θησαυρός)."),
 ("MAT.6.19", "Frass", "interpretive", "βρῶσις", "Essen", ["Rost", "Wurm"],
  "βρῶσις heisst «Essen, Fressen»; neben der Motte (σής) wohl ein Schädling, der Vorräte oder Stoffe frisst. Die Deutung «Rost» ist verbreitet (vgl. [[JAS.5.2-JAS.5.3]]), vom Wort her aber nicht zwingend."),
 ("MAT.6.19", "einbrechen", "literal", "διορύσσουσιν", "durchgraben", None, "Wörtlich «durchgraben»: Wände aus Lehmziegeln wurden durchbrochen."),
 ("MAT.6.20", "im Himmel", "literal", "ἐν οὐρανῷ", None, None, "Hier steht die Einzahl, anders als in der Wendung «Vater in den Himmeln» ([[MAT.6.1]]); die Übersetzung folgt dem Wechsel."),
 ("MAT.6.22", "Lampe", "literal", "λύχνος", None, ["Leuchte"], "Die Öllampe; vgl. [[MAT.5.15]]."),
 ("MAT.6.22", "Leib", "traditional", "σώματός", None, ["Körper"], "σῶμα ist der Mensch in seiner Leiblichkeit; «Leib» folgt der vertrauten Wiedergabe, ebenso in [[MAT.6.23]] und [[MAT.6.25]]."),
 ("MAT.6.22", "klar", "interpretive", "ἁπλοῦς", "einfach", ["gesund", "lauter", "ungeteilt", "grosszügig"],
  "ἁπλοῦς heisst «einfach, ungeteilt», vom Auge gesagt «gesund, klar». Wegen des Gegenstücks «schlechtes Auge» ([[MAT.6.23]]) und des Zusammenhangs mit dem Besitz ([[MAT.6.19-MAT.6.24]]) wird auch «grosszügig» vertreten, denn das «böse Auge» bezeichnet in der jüdischen Sprache Neid und Geiz (vgl. [[DEU.15.9]], [[MAT.20.15]]). «Klar» hält das Bild und lässt die übertragenen Bedeutungen offen."),
 ("MAT.6.23", "schlecht", "interpretive", "πονηρὸς", "böse", ["krank", "neidisch"], "Gegenstück zu ἁπλοῦς ([[MAT.6.22]]); «böses Auge» ist eine Wendung für Missgunst (vgl. [[MAT.20.15]])."),
 ("MAT.6.23", "wie gross ist dann die Finsternis", "adapted", "τὸ σκότος πόσον", "die Finsternis – wie gross!", None, "Der griechische Satz hat kein Verb; «ist dann» ist ergänzt."),
 ("MAT.6.24", "Herren", "literal", "κυρίοις", None, ["Besitzern"], "Gedacht ist an Sklavenhalter: Ein Sklave konnte nicht zwei Eigentümern zugleich ganz gehören."),
 ("MAT.6.24", "hassen", "interpretive", "μισήσει", None, ["zurücksetzen"],
  "«Hassen» und «lieben» drücken in semitischer Redeweise auch Zurücksetzen und Vorziehen aus (vgl. [[GEN.29.30-GEN.29.31]], [[LUK.14.26]])."),
 ("MAT.6.24", "dem Mammon", "traditional", "μαμωνᾷ", "dem Besitz", ["dem Geld", "dem Reichtum"],
  "μαμωνᾶς ist ein aramäisches Wort für Besitz, Vermögen; seine Herkunft ist unsicher. Hier steht er als Gegenmacht zu Gott, wie ein Herr, dem man dient; deshalb bleibt das Fremdwort stehen."),
 ("MAT.6.25", "Sorgt euch nicht", "interpretive", "μὴ μεριμνᾶτε", None, ["Seid nicht ängstlich besorgt", "Macht euch keine Sorgen"],
  "μεριμνάω meint das angespannte, ängstliche Sorgen. Leitwort von [[MAT.6.25-MAT.6.34]] (sechsmal: [[MAT.6.25]], [[MAT.6.27]], [[MAT.6.28]], [[MAT.6.31]], zweimal [[MAT.6.34]]); einheitlich «sich sorgen»."),
 ("MAT.6.25", "Leben", "interpretive", "ψυχῇ", "Seele", None,
  "ψυχή meint hier das Leben, das durch Nahrung erhalten wird, wie der Leib durch Kleidung; ebenso im zweiten Teil des Verses. Zur Lesart «was ihr essen oder was ihr trinken sollt» siehe die Alternativen."),
 ("MAT.6.26", "die Vögel des Himmels", "literal", "τὰ πετεινὰ τοῦ οὐρανοῦ", None, ["die Vögel unter dem Himmel"], "Hebräisch geprägte Wendung für die frei lebenden Vögel."),
 ("MAT.6.26", "Seid ihr nicht viel mehr wert als sie", "adapted", "οὐχ ὑμεῖς μᾶλλον διαφέρετε αὐτῶν", "Unterscheidet ihr euch nicht mehr als sie", None, "διαφέρω heisst «sich unterscheiden, überlegen sein»."),
 ("MAT.6.27", "seiner Lebenszeit eine einzige Elle hinzufügen", "interpretive", "προσθεῖναι ἐπὶ τὴν ἡλικίαν αὐτοῦ πῆχυν ἕνα", None, ["seiner Körpergrösse eine Elle hinzufügen"],
  "ἡλικία heisst «Lebenszeit» und «Körpergrösse»; die Elle (etwa 45 cm) ist ein Längenmass. Weil ein Zuwachs der Grösse um eine Elle kein Geringes wäre (vgl. [[LUK.12.26]]), wird meist bildlich an die Lebenszeit gedacht."),
 ("MAT.6.28", "Lilien", "traditional", "κρίνα", None, ["Blumen", "Anemonen"], "Welche Blume κρίνον bezeichnet, ist unsicher; gemeint sind wohl die wild wachsenden Blumen des Feldes."),
 ("MAT.6.28", "Sie mühen sich nicht ab und spinnen auch nicht", "literal", "οὐ κοπιῶσιν οὐδὲ νήθουσιν", None, None,
  "Säen und Ernten ([[MAT.6.26]]) waren vor allem Arbeit der Männer, Spinnen Arbeit der Frauen; beide Bilder zusammen umfassen die Arbeit für Nahrung und Kleidung."),
 ("MAT.6.29", "Pracht", "adapted", "δόξῃ", "Herrlichkeit", None, "δόξα meint hier den sichtbaren Glanz des Königs (vgl. [[1KI.10.4-1KI.10.7]])."),
 ("MAT.6.30", "in den Ofen geworfen wird", "literal", "εἰς κλίβανον βαλλόμενον", None, None, "Getrocknetes Gras diente als Brennstoff für den Backofen."),
 ("MAT.6.30", "ihr Kleingläubigen", "literal", "ὀλιγόπιστοι", "ihr Wenig-Glaubenden", ["ihr Glaubensschwachen"],
  "ὀλιγόπιστος ist ein Wort des Matthäus ([[MAT.8.26]], [[MAT.14.31]], [[MAT.16.8]]; vgl. ὀλιγοπιστία in [[MAT.17.20]]). Es spricht Jüngern den Glauben nicht ab, sondern rügt ein zu kleines Vertrauen. Einheitlich «Kleingläubige»."),
 ("MAT.6.31", "Sorgt euch also nicht und sagt", "adapted", "μὴ οὖν μεριμνήσητε λέγοντες", "Sorgt euch also nicht, indem ihr sagt", None, None),
 ("MAT.6.32", "trachten", "literal", "ἐπιζητοῦσιν", "suchen", None, "Verstärktes «suchen»; vgl. «sucht» in [[MAT.6.33]]."),
 ("MAT.6.32", "die Heiden", "interpretive", "τὰ ἔθνη", "die Völker", ["die Nichtjuden"],
  "ἔθνη sind die Völker ausser Israel; wie ἐθνικοί in [[MAT.6.7]] mit «Heiden» wiedergegeben. Gemeint ist eine Lebensweise ohne Vertrauen auf den Gott Israels, kein Urteil über Menschen anderer Herkunft."),
 ("MAT.6.33", "das Reich", "literal", "τὴν βασιλείαν", None, ["sein Reich", "das Reich Gottes"],
  "Im SBLGNT steht «das Reich» ohne Zusatz. αὐτοῦ («sein») kann sich auf beide Glieder beziehen, also auf das Reich und die Gerechtigkeit Gottes, des Vaters von [[MAT.6.32]]. Zur Lesart «das Reich Gottes» siehe die Alternativen."),
 ("MAT.6.33", "seine Gerechtigkeit", "interpretive", "τὴν δικαιοσύνην αὐτοῦ", None, ["die Gerechtigkeit, die er schenkt", "das gerechte Tun, das er will"],
  "Vgl. [[MAT.6.1]]: bei Matthäus meist das Tun, das Gottes Willen entspricht; manche verstehen «seine Gerechtigkeit» als Gottes eigenes, rettendes Handeln."),
 ("MAT.6.33", "dazugegeben", "literal", "προστεθήσεται", "hinzugefügt werden", None, "Das Passiv wird meist als Umschreibung für Gottes Handeln verstanden."),
 ("MAT.6.34", "wird für sich selbst sorgen", "literal", "μεριμνήσει αὑτῆς", None, None,
  "Der morgige Tag wird wie eine Person vorgestellt, die ihre eigenen Sorgen hat. Zur Lesart «wird für das Seine sorgen» siehe die Alternativen."),
 ("MAT.6.34", "Es genügt dem Tag seine eigene Plage", "adapted", "ἀρκετὸν τῇ ἡμέρᾳ ἡ κακία αὐτῆς", "Genug für den Tag ist sein Übel", ["Jeder Tag hat genug an seiner eigenen Last"],
  "κακία heisst hier nicht «Bosheit», sondern Not, Mühsal; «eigene» ist ergänzt."),
 ("MAT.7.1", "Richtet nicht", "interpretive", "Μὴ κρίνετε", None, ["Verurteilt nicht"],
  "κρίνω heisst «urteilen, richten, verurteilen». Gemeint ist das verurteilende Urteilen über andere ([[MAT.7.3-MAT.7.5]]), nicht jedes Unterscheiden: [[MAT.7.6]] und [[MAT.7.15-MAT.7.20]] verlangen gerade Unterscheidung. Das Passiv «gerichtet werdet» wird meist auf Gottes Gericht bezogen."),
 ("MAT.7.2", "Mass", "literal", "μέτρῳ", None, None, "Bild vom Getreidemass. Der Satz steht auch in [[MRK.4.24]] (dort zum Hören) und [[LUK.6.38]]."),
 ("MAT.7.3", "Splitter", "literal", "κάρφος", None, ["Holzspan", "Halm"], "κάρφος ist ein trockener Halm oder Span, δοκός ein Dachbalken: ein absichtlich übertriebenes Bild."),
 ("MAT.7.3", "Bruders", "literal", "ἀδελφοῦ", None, ["Mitmenschen", "Glaubensgeschwisters"], "Gemeint ist der Mitmensch in der Gemeinschaft, nicht nur der leibliche Bruder; Frauen sind mitgemeint. Wie in [[MAT.5.22-MAT.5.24]]."),
 ("MAT.7.4", "wie kannst du zu deinem Bruder sagen", "adapted", "πῶς ἐρεῖς τῷ ἀδελφῷ σου", "wie wirst du zu deinem Bruder sagen", None, "Das Futur drückt hier aus, was man sich herausnimmt."),
 ("MAT.7.4", "siehe", "traditional", "ἰδοὺ", None, ["schau"], "ἰδού lenkt die Aufmerksamkeit; in ganz Matthäus «siehe»."),
 ("MAT.7.5", "Du Heuchler", "traditional", "ὑποκριτά", "Schauspieler", None, "Wie [[MAT.6.2]]; hier ist der Einzelne angeredet, der den anderen beurteilt und sich selbst nicht sieht."),
 ("MAT.7.5", "wirst du klar sehen", "literal", "διαβλέψεις", "wirst du hindurchblicken", None, None),
 ("MAT.7.6", "das Heilige", "interpretive", "τὸ ἅγιον", None, ["das Opferfleisch"],
  "Wahrscheinlich ist an geweihtes Opferfleisch gedacht, das man nicht den Hunden vorwerfen durfte (vgl. [[EXO.22.31]]). Hunde und Schweine galten als unrein. Was das Bild meint, sagt der Text nicht; die Deutungen reichen von der Verkündigung an Menschen, die sie verächtlich zurückweisen, bis zu heiligen Handlungen der Gemeinde."),
 ("MAT.7.6", "sich umdrehen und euch zerreissen", "literal", "στραφέντες ῥήξωσιν ὑμᾶς", None, None,
  "Das Subjekt wechselt nicht ausdrücklich: Zertreten passt zu den Schweinen, Zerreissen eher zu den Hunden; beides kann aber auch von den Schweinen gesagt sein."),
 ("MAT.7.7", "Bittet", "literal", "Αἰτεῖτε", None, None, "Präsens-Imperative: anhaltend bitten, suchen, anklopfen. Die Passive («wird gegeben», «wird geöffnet») werden meist als Umschreibung für Gottes Handeln verstanden."),
 ("MAT.7.9", "wird er ihm etwa einen Stein geben", "adapted", "μὴ λίθον ἐπιδώσει αὐτῷ", "nicht einen Stein wird er ihm geben", None,
  "Die Frage mit μή erwartet die Antwort «nein»; «etwa» gibt das wieder. Der griechische Satz ist unterbrochen gebaut; der Gedankenstrich zeigt das. Ebenso in [[MAT.7.10]]."),
 ("MAT.7.11", "die ihr böse seid", "literal", "πονηροὶ ὄντες", None, ["obwohl ihr böse seid"], "Die Aussage setzt voraus, dass Menschen nicht gut sind, ohne es auszuführen."),
 ("MAT.7.11", "Gutes", "literal", "ἀγαθὰ", None, None, "In [[LUK.11.13]] steht an dieser Stelle «heiligen Geist»."),
 ("MAT.7.12", "Alles nun, was ihr wollt, dass euch die Menschen tun, so tut auch ihr ihnen", "literal", "Πάντα οὖν ὅσα ἐὰν θέλητε ἵνα ποιῶσιν ὑμῖν οἱ ἄνθρωποι, οὕτως καὶ ὑμεῖς ποιεῖτε αὐτοῖς", None, None,
  "Die sogenannte Goldene Regel. In verneinter Form ist sie im Judentum und darüber hinaus verbreitet (etwa im Buch Tobit und in einem Wort, das der Babylonische Talmud Rabbi Hillel zuschreibt); hier steht sie in bejahter Form."),
 ("MAT.7.12", "das Gesetz und die Propheten", "literal", "ὁ νόμος καὶ οἱ προφῆται", None, None,
  "Die Schrift Israels; wie in [[MAT.5.17]] und [[MAT.22.40]]. Manche sehen in der Wiederaufnahme von [[MAT.5.17]] eine Klammer um den Hauptteil der Bergpredigt."),
 ("MAT.7.13", "Tor", "literal", "πύλης", None, ["Pforte"], "πύλη ist das (Stadt-)Tor. Das Bild der zwei Wege ist in der Schrift vertraut ([[DEU.30.15-DEU.30.19]], [[PSA.1.6]], [[JER.21.8]])."),
 ("MAT.7.13", "breit", "literal", "εὐρύχωρος", "geräumig", None, None),
 ("MAT.7.13", "Verderben", "literal", "ἀπώλειαν", None, ["Untergang"], "ἀπώλεια: Untergang, Verlorensein; Gegenbegriff zum «Leben» in [[MAT.7.14]]."),
 ("MAT.7.13", "dort", "adapted", "διʼ αὐτῆς", "durch es", ["durch ihn"], "αὐτῆς kann auf das Tor oder auf den Weg zurückweisen (beide im Griechischen weiblich); «dort» lässt das offen. Zur Lesart ohne «das Tor» siehe die Alternativen."),
 ("MAT.7.14", "Denn eng", "interpretive", "ὅτι στενὴ", None, ["Wie eng"],
  "Der SBLGNT liest ὅτι («denn»), parallel zu [[MAT.7.13]]. Viele Editionen lesen τί («wie!»), einen Ausruf; siehe die Alternativen."),
 ("MAT.7.14", "schmal", "adapted", "τεθλιμμένη", "bedrängt", ["eingeengt"], "θλίβω heisst «bedrängen, einengen»; Anklang an θλῖψις, «Bedrängnis» (vgl. [[MAT.24.21]])."),
 ("MAT.7.14", "Leben", "literal", "ζωήν", None, None, "Das Leben im vollen Sinn, das Leben bei Gott (vgl. [[MAT.19.16-MAT.19.17]])."),
 ("MAT.7.15", "den falschen Propheten", "literal", "τῶν ψευδοπροφητῶν", "den Falschpropheten", None, "Vgl. [[MAT.24.11]] und [[MAT.24.24]]. Wer gemeint ist, sagt der Text nicht; erkennbar sind sie an ihren Früchten ([[MAT.7.16]])."),
 ("MAT.7.15", "Schafskleidern", "literal", "ἐνδύμασι προβάτων", "Kleidern von Schafen", ["Schafspelz"], "Bild der Tarnung: Sie geben sich harmlos wie Schafe der Herde (vgl. [[MAT.10.16]])."),
 ("MAT.7.16", "An ihren Früchten werdet ihr sie erkennen", "literal", "ἀπὸ τῶν καρπῶν αὐτῶν ἐπιγνώσεσθε αὐτούς", None, None, "«Früchte» steht bildlich für Taten und ihre Wirkung; vgl. [[MAT.3.8]] und [[MAT.12.33]]. Der Satz rahmt [[MAT.7.16-MAT.7.20]]."),
 ("MAT.7.16", "Sammelt man etwa", "adapted", "μήτι συλλέγουσιν", "sammeln sie etwa", None, "Unpersönliches «sie»; μήτι erwartet die Antwort «nein»."),
 ("MAT.7.17", "gute Früchte", "literal", "καρποὺς καλοὺς", "schöne Früchte", None,
  "Vom Baum steht ἀγαθός, von den Früchten καλός; beides ist mit «gut» wiedergegeben. πονηρός, sonst «böse», heisst von Früchten «schlecht»."),
 ("MAT.7.17", "faule", "interpretive", "σαπρὸν", None, ["morsche", "kranke", "unbrauchbare"], "σαπρός heisst «faul, verdorben»; von einem Baum gesagt «krank, unbrauchbar»."),
 ("MAT.7.19", "wird umgehauen und ins Feuer geworfen", "literal", "ἐκκόπτεται καὶ εἰς πῦρ βάλλεται", None, None, "Wörtlich wie das Wort des Täufers in [[MAT.3.10]]."),
 ("MAT.7.21", "Herr, Herr", "literal", "Κύριε κύριε", None, None,
  "κύριε ist die Anrede «Herr»; die Verdoppelung zeigt Eindringlichkeit. [[MAT.7.22]] verlegt die Szene auf den Tag des Gerichts."),
 ("MAT.7.21", "das Reich der Himmel", "traditional", "τὴν βασιλείαν τῶν οὐρανῶν", "die Königsherrschaft der Himmel", ["das Himmelreich", "das Reich Gottes"],
  "Matthäus sagt meist «Reich der Himmel»; «Himmel» steht wohl aus Scheu vor dem Gottesnamen für Gott. Sachlich gleich mit «Reich Gottes» bei Markus und Lukas. Einheitlich «Reich der Himmel», mit dem griechischen Plural."),
 ("MAT.7.22", "an jenem Tag", "literal", "ἐν ἐκείνῃ τῇ ἡμέρᾳ", None, None, "Prophetische Wendung für den Tag des Gerichts (vgl. [[ISA.2.11]], [[MAL.3.17]])."),
 ("MAT.7.22", "prophezeit", "literal", "ἐπροφητεύσαμεν", None, ["als Propheten geredet"], "προφητεύω heisst im Auftrag Gottes reden, nicht nur Künftiges voraussagen."),
 ("MAT.7.22", "in deinem", "literal", "τῷ σῷ ὀνόματι", None, ["unter Berufung auf deinen Namen"], "Dativ des Mittels; dreimal betont vorangestellt."),
 ("MAT.7.22", "Machttaten", "literal", "δυνάμεις", "Kräfte", ["Wunder"], "δύναμις heisst «Kraft»; im Plural die Machterweise."),
 ("MAT.7.23", "offen erklären", "interpretive", "ὁμολογήσω", "bekennen", ["öffentlich erklären"], "ὁμολογέω heisst «bekennen, zugestehen, öffentlich erklären»; hier eine feierliche Erklärung wie vor Gericht."),
 ("MAT.7.23", "Nie habe ich euch gekannt", "literal", "Οὐδέποτε ἔγνων ὑμᾶς", None, None, "«Kennen» im biblischen Sinn: in Beziehung stehen, anerkennen (vgl. [[AMO.3.2]])."),
 ("MAT.7.23", "Weicht von mir", "literal", "ἀποχωρεῖτε ἀπʼ ἐμοῦ", None, None, "Anklang an [[PSA.6.8]]."),
 ("MAT.7.23", "Gesetzlosigkeit", "literal", "τὴν ἀνομίαν", None, ["Unrecht", "Bosheit"],
  "ἀνομία, wörtlich «Gesetzlosigkeit», kehrt bei Matthäus wieder ([[MAT.13.41]], [[MAT.23.28]], [[MAT.24.12]]): Handeln gegen Gottes Willen, wie ihn das Gesetz ausdrückt; Gegenstück zum Tun des Willens des Vaters ([[MAT.7.21]])."),
 ("MAT.7.24", "diese meine Worte", "literal", "μου τοὺς λόγους τούτους", None, None, "Bezieht sich auf die ganze Rede ab [[MAT.5.3]]."),
 ("MAT.7.24", "wird einem klugen Mann gleichen", "literal", "ὁμοιωθήσεται ἀνδρὶ φρονίμῳ", "wird einem klugen Mann gleichgemacht werden", ["gleicht einem klugen Mann"],
  "Futur Passiv, wohl mit Blick auf das Gericht. Zur Lesart «den werde ich vergleichen» siehe die Alternativen."),
 ("MAT.7.24", "gebaut hat", "adapted", "ᾠκοδόμησεν", "baute", None, "Im Deutschen ist hier das Perfekt natürlicher; ebenso in [[MAT.7.26]]. Das Gleichnis selbst ([[MAT.7.25]], [[MAT.7.27]]) erzählt im Präteritum."),
 ("MAT.7.25", "die Fluten", "adapted", "οἱ ποταμοὶ", "die Flüsse", ["die Ströme", "die Sturzbäche"], "Gemeint sind die Wassermassen, die nach heftigem Regen in den Trockentälern plötzlich anschwellen."),
 ("MAT.7.25", "gegründet", "literal", "τεθεμελίωτο", None, None, "Plusquamperfekt: Das Fundament war schon gelegt."),
 ("MAT.7.26", "törichten", "literal", "μωρῷ", None, ["dummen"], "μωρός: töricht, ohne Einsicht; Gegenwort zu φρόνιμος, «klug» ([[MAT.7.24]]), wie in [[MAT.25.2]]."),
 ("MAT.7.27", "sein Einsturz war gewaltig", "literal", "ἦν ἡ πτῶσις αὐτῆς μεγάλη", "sein Fall war gross", None, None),
 ("MAT.7.28", "Und es geschah, als", "literal", "Καὶ ἐγένετο ὅτε", None, None,
  "Mit dieser Formel schliesst Matthäus jede seiner fünf grossen Reden ab ([[MAT.11.1]], [[MAT.13.53]], [[MAT.19.1]], [[MAT.26.1]])."),
 ("MAT.7.28", "die Menge", "adapted", "οἱ ὄχλοι", "die Mengen", ["die Volksscharen", "die Leute"], "Matthäus hat oft den Plural ὄχλοι; im Deutschen ist die Einzahl natürlicher."),
 ("MAT.7.28", "überwältigt", "literal", "ἐξεπλήσσοντο", None, ["erstaunt", "betroffen"], "ἐκπλήσσομαι: ausser sich geraten, tief beeindruckt sein; wie in [[MRK.1.22]]. Imperfekt: ein anhaltender Eindruck."),
 ("MAT.7.29", "Vollmacht", "interpretive", "ἐξουσίαν", "Befugnis", ["Autorität"], "ἐξουσία ist rechtmässige Befugnis; wie in [[MRK.1.22]]. Vgl. das «Ich aber sage euch» der Rede ([[MAT.5.22]])."),
 ("MAT.7.29", "ihre Schriftgelehrten", "literal", "οἱ γραμματεῖς αὐτῶν", None, ["die Schriftgelehrten"],
  "«ihre» bezieht sich auf die Menge. Manche lesen darin eine Abgrenzung der Gemeinde des Matthäus von der Synagoge; der Text sagt nur, dass es die Schriftgelehrten der Menge sind. Zur Lesart ohne «ihre» siehe die Alternativen."),
]

DEC_GSW = [
 ("MAT.6.1", "Grächtigkeit", "interpretive", "δικαιοσύνην", None, ["Frömmigkeit"],
  "δικαιοσύνη isch bim Matthäus es Leitwort ([[MAT.5.6]], [[MAT.5.20]], [[MAT.6.33]]): s Tue, wo em Wile vo Gott entspricht. Da staat s als Überschrift über Almose, Bätte und Faschte. Zur Läsart «Almose» lueg d Alternative."),
 ("MAT.6.1", "üebed", "adapted", "ποιεῖν", "tüend", None, "«Grächtigkeit tue» isch ungwöhnlich."),
 ("MAT.6.1", "demit si eu gseend", "adapted", "πρὸς τὸ θεαθῆναι αὐτοῖς", "zum vo ine gsee wärde", None, "S Passiv isch i de Mundart umständlich; umgstellt."),
 ("MAT.6.1", "suscht", "adapted", "εἰ δὲ μή γε", "wänn aber nöd", None, "Feschti Wändig."),
 ("MAT.6.1", "Loon", "literal", "μισθὸν", None, None, "Wie i [[MAT.6.5]]."),
 ("MAT.6.2", "Almose", "traditional", "ἐλεημοσύνην", "Barmhärzigkeit", ["Spänd"], "D Gab für Armi; näbe Bätte und Faschte e Grundüebig vo de jüdische Frömmigkeit."),
 ("MAT.6.2", "blaas nöd d Posuune vor dir här", "interpretive", "μὴ σαλπίσῃς ἔμπροσθέν σου", "trumpeet nöd vor dir här", None,
  "Öb en würkliche Bruuch gmeint isch oder es Bild für Sälbschtdarstellig, isch unsicher."),
 ("MAT.6.2", "Hüüchler", "traditional", "ὑποκριταὶ", "Schauspiler", None,
  "ὑποκριτής hät ursprünglich «Schauspiler» gheisse. «Hüüchler» wie i [[MAT.6.5]] und [[MRK.7.6]]."),
 ("MAT.6.2", "grüemt wärded", "adapted", "δοξασθῶσιν", "verherrlicht wärded", None, None),
 ("MAT.6.2", "Amen, ich säg eu", "traditional", "ἀμὴν λέγω ὑμῖν", None, None, "«Amen» (hebräisch «gwüss») bekräftiget, was chunnt; i ganz Matthäus gliich."),
 ("MAT.6.2", "Si händ ire Loon scho übercho", "literal", "ἀπέχουσιν τὸν μισθὸν αὐτῶν", None, None, "ἀπέχω isch s Wort vo de Quittig: «vollständig übercho». Wie i [[MAT.6.5]]."),
 ("MAT.6.4", "im Verborgne bliibt", "adapted", "ᾖ σου ἡ ἐλεημοσύνη ἐν τῷ κρυπτῷ", "im Verborgne isch", None, None),
 ("MAT.6.4", "vergälte", "literal", "ἀποδώσει", None, ["belohne"], "Zu de Läsarte «er sälber» und «öffentlich» lueg d Alternative."),
 ("MAT.6.16", "mached kei finschters Gsicht", "adapted", "μὴ γίνεσθε ὡς οἱ ὑποκριταὶ σκυθρωποί", "wärded nöd finschter dreiluegend", None, None),
 ("MAT.6.16", "ires Gsicht unkänntlich", "interpretive", "ἀφανίζουσιν τὰ πρόσωπα αὐτῶν", "lönd ires Gsicht verschwinde", ["verstelled ires Gsicht"],
  "ἀφανίζω heisst «unsichtbar mache»; Wortspiil mit φανῶσιν («demit si gsee wärded»). Gmeint isch wohl Ungflegt-Sii, Äsche uf em Chopf oder Verhülle als Zeiche vo Truur."),
 ("MAT.6.17", "salb diin Chopf", "literal", "ἄλειψαί σου τὴν κεφαλὴν", None, None, "Öl uf Chopf und Haar hät zur tägliche Pfleg ghört; i de Truur hät me s weggla."),
 ("MAT.6.19", "Schabe", "adapted", "σὴς", "Motte", None, "«Schabe» isch s Mundartwort für d Chleidermotte."),
 ("MAT.6.19", "Frass", "interpretive", "βρῶσις", "Ässe", ["Rost"], "Wohl en Schädling, wo Vorrät oder Stoff frisst; d Düütig «Rost» isch vom Wort här nöd zwingend."),
 ("MAT.6.19", "iibräched", "literal", "διορύσσουσιν", "dureggrabed", None, "Wänd us Lehmziegel sind durebroche worde."),
 ("MAT.6.20", "im Himel", "literal", "ἐν οὐρανῷ", None, None, "Da Einzahl, andersch als «Vatter i de Himel»."),
 ("MAT.6.22", "Liib", "traditional", "σώματός", None, ["Körper"], None),
 ("MAT.6.22", "klar", "interpretive", "ἁπλοῦς", "eifach", ["gsund", "luuter", "grosszügig"],
  "Vom Aug gseit «gsund, klar». Im Zämehang vom Bsitz wird au «grosszügig» vertrete, will «es bööses Aug» Niid und Giiz bedüütet (vgl. [[MAT.20.15]])."),
 ("MAT.6.23", "schlächt", "interpretive", "πονηρὸς", "bös", ["neidisch"], None),
 ("MAT.6.24", "hasst er", "interpretive", "μισήσει", None, ["setzt er hinde"], "«Hasse» und «liebe» chönd semitisch au «hindesetze» und «vorzie» heisse (vgl. [[LUK.14.26]])."),
 ("MAT.6.24", "er hanget am eint aa", "adapted", "ἑνὸς ἀνθέξεται", "er wird am eint aahange", ["er haltet zum eint"], "S griechisch Futur isch i de Mundart mit em Präsens wiedergää, wie me s seit."),
 ("MAT.6.24", "em Mammon", "traditional", "μαμωνᾷ", "em Bsitz", ["em Gält"], "Aramäischs Wort für Bsitz, Vermöge; da wie en Herr, wo me em dient."),
 ("MAT.6.25", "Mached eu kei Sorge", "interpretive", "μὴ μεριμνᾶτε", "Sorged eu nöd", None,
  "μεριμνάω isch s ängschtlich, aagspannt Sorge; Leitwort vo [[MAT.6.25-MAT.6.34]]. Zur Läsart «oder was ir trinked» lueg d Alternative."),
 ("MAT.6.25", "Läbe", "interpretive", "ψυχῇ", "Seel", None, None),
 ("MAT.6.26", "d Vögel am Himel", "literal", "τὰ πετεινὰ τοῦ οὐρανοῦ", "d Vögel vom Himel", None, None),
 ("MAT.6.27", "sinere Läbesziit e einzigi Elle dezuetue", "interpretive", "προσθεῖναι ἐπὶ τὴν ἡλικίαν αὐτοῦ πῆχυν ἕνα", None, ["sinere Grössi e Elle dezuetue"],
  "ἡλικία heisst «Läbesziit» und «Grössi»; d Elle (öppe 45 cm) isch es Längemass."),
 ("MAT.6.28", "Lilie", "traditional", "κρίνα", None, ["Blueme"], "Welli Blueme gmeint isch, isch unsicher."),
 ("MAT.6.28", "chrampfed", "adapted", "κοπιῶσιν", "müeied sich ab", None, "«Chrampfe» = hert schaffe."),
 ("MAT.6.29", "Pracht", "adapted", "δόξῃ", "Herrlichkeit", None, None),
 ("MAT.6.30", "ir Chliigläubige", "literal", "ὀλιγόπιστοι", None, None, "Es Wort vom Matthäus ([[MAT.8.26]], [[MAT.14.31]], [[MAT.16.8]]); einheitlich «Chliigläubigi»."),
 ("MAT.6.32", "d Heide", "interpretive", "τὰ ἔθνη", "d Völker", ["d Nichtjude"], "Wie [[MAT.6.7]]. Gmeint isch e Läbeswiis ohni Vertroue uf de Gott vo Israel, kei Urteil über Mänsche vo andere Herkunft."),
 ("MAT.6.33", "s Riich", "literal", "τὴν βασιλείαν", None, ["sis Riich", "s Riich vo Gott"], "Im SBLGNT ohni Zuesatz; «sini» cha sich uf beides bezieh. Lueg d Alternative."),
 ("MAT.6.34", "Jedem Tag längt sini eiget Plaag", "adapted", "ἀρκετὸν τῇ ἡμέρᾳ ἡ κακία αὐτῆς", "Gnueg für de Tag isch sis Übel", None, "κακία heisst da Not, Müe; «eiget» isch ergänzt."),
 ("MAT.6.34", "wird für sich sälber sorge", "literal", "μεριμνήσει αὑτῆς", None, None, "Zur Läsart «für s Sine» lueg d Alternative."),
 ("MAT.7.1", "Richted nöd", "interpretive", "Μὴ κρίνετε", None, ["Verurteiled nöd"], "Gmeint isch s Verurteile vo andere ([[MAT.7.3-MAT.7.5]]), nöd jedes Underscheide."),
 ("MAT.7.2", "mit em Mass, wo ir mässed", "literal", "ἐν ᾧ μέτρῳ μετρεῖτε", None, None, "Gliich wie [[MRK.4.24]]."),
 ("MAT.7.3", "Brueder", "literal", "ἀδελφοῦ", None, ["Mitmänsch"], "Gmeint isch de Mitmänsch; Fraue sind mitgmeint."),
 ("MAT.7.4", "lueg", "traditional", "ἰδοὺ", None, None, "Einheitlich «lueg» für ἰδού."),
 ("MAT.7.5", "Du Hüüchler", "traditional", "ὑποκριτά", None, None, "Wie [[MAT.6.2]]."),
 ("MAT.7.6", "s Heilig", "interpretive", "τὸ ἅγιον", None, ["s Opferfleisch"], "Wahrschiinli isch gweihts Opferfleisch gmeint (vgl. [[EXO.22.31]]); was s Bild meint, seit de Text nöd."),
 ("MAT.7.6", "rüered", "adapted", "βάλητε", "wärfed", None, "«Rüere» = wärfe."),
 ("MAT.7.11", "chönd", "adapted", "οἴδατε", "wüssed", None, "«Wüsse, wie me git» isch i de Mundart «chöne gää»."),
 ("MAT.7.12", "s Gsetz und d Prophete", "literal", "ὁ νόμος καὶ οἱ προφῆται", None, None, "D Schrift vo Israel; wie [[MAT.5.17]]."),
 ("MAT.7.13", "dört", "adapted", "διʼ αὐτῆς", "dur es", ["dur en"], "Es cha s Tor oder de Wäg gmeint sii. Zur Läsart ohni «s Tor» lueg d Alternative."),
 ("MAT.7.14", "Dänn äng", "interpretive", "ὅτι στενὴ", None, ["Wie äng"], "Lueg d Alternative."),
 ("MAT.7.14", "schmaal", "adapted", "τεθλιμμένη", "bedrängt", None, None),
 ("MAT.7.16", "List me", "adapted", "συλλέγουσιν", "Sammled si", None, "«Truube läse» isch s Mundartwort für s Ärnte vo Truube."),
 ("MAT.7.17", "fuul", "interpretive", "σαπρὸν", None, ["chrank"], None),
 ("MAT.7.21", "is Riich vo de Himel", "traditional", "εἰς τὴν βασιλείαν τῶν οὐρανῶν", "i d Chönigsherrschaft vo de Himel", ["is Himelriich"],
  "De Matthäus seit meischt «Riich vo de Himel» («Himel» staat für Gott); sachlich gliich wie «Riich vo Gott»."),
 ("MAT.7.22", "Machttate", "literal", "δυνάμεις", "Chräft", ["Wunder"], None),
 ("MAT.7.23", "offe säge", "interpretive", "ὁμολογήσω", "bekänne", None, None),
 ("MAT.7.23", "Gsetzlosigkeit", "literal", "τὴν ἀνομίαν", None, ["Unrächt"], "Handle gäge de Wile vo Gott; Gägestuck zu [[MAT.7.21]]."),
 ("MAT.7.24", "isch wie en gschiide Maa", "adapted", "ὁμοιωθήσεται ἀνδρὶ φρονίμῳ", "wird eme gschiide Maa gliich gmacht", ["wird eme gschiide Maa gliiche"],
  "Futur Passiv; i de Mundart eifacher «isch wie». Zur Läsart «dä vergliich ich» lueg d Alternative."),
 ("MAT.7.25", "s Hochwasser", "adapted", "οἱ ποταμοὶ", "d Flüss", None, "Gmeint sind d Wassermasse, wo nach starchem Räge plötzlich aaschwelled."),
 ("MAT.7.26", "tumme", "literal", "μωρῷ", None, ["törichte"], None),
 ("MAT.7.28", "Und es isch gscheh", "literal", "Καὶ ἐγένετο", None, None,
  "Mit dere Formle schlüüsst de Matthäus jedi vo sine füüf grosse Rede ab ([[MAT.11.1]], [[MAT.13.53]], [[MAT.19.1]], [[MAT.26.1]])."),
 ("MAT.7.28", "d Mängi", "adapted", "οἱ ὄχλοι", "d Mängene", None, None),
 ("MAT.7.29", "iri Schriftgelehrte", "literal", "οἱ γραμματεῖς αὐτῶν", None, None, "Lueg d Alternative."),
]

# Lesarten, die die Übersetzung verändern: (Lesart, Stelle, de von, de zu, gsw von, gsw zu, Wirkung, Hinweis de, Hinweis gsw,
#  Wörter {Lesart: [(griechisch, de, Hinweis)]}, Wörter gsw, Entstehung de, Entstehung gsw)
AUTO = "Laut der automatischen Zuordnung (WREAD-CNTR-MAT-…)"
AUTO_G = "Nach de automatische Zueornig"
ALTS = [
 ("VAR-SBLGNTAPP-MAT-006-001-02:R2", "MAT.6.1", "eure Gerechtigkeit", "eure Almosen", "eui Grächtigkeit", "eues Almose", "mittel",
  "Mit «Almosen» bezieht sich der Satz nur auf das Geben ([[MAT.6.2-MAT.6.4]]) und ist nicht mehr Überschrift auch über Beten und Fasten.",
  "Mit «Almose» bezieht sich de Satz nu ufs Gää ([[MAT.6.2-MAT.6.4]]) und isch nüme d Überschrift au über Bätte und Faschte.",
  {"R1": [("δικαιοσύνην", "Gerechtigkeit", "SBLGNT, WH, Treg, NA28")], "R2": [("ἐλεημοσύνην", "Almosen", "RP")]},
  {"R1": [("δικαιοσύνην", "Grächtigkeit", "SBLGNT, WH, Treg, NA28")], "R2": [("ἐλεημοσύνην", "Almose", "RP")]},
  ["Ein Schreiber konnte das allgemeine Wort an das folgende Stichwort «Almosen» ([[MAT.6.2]]) angleichen; im späteren Sprachgebrauch konnte δικαιοσύνη selbst «Wohltätigkeit» bedeuten, was den Austausch erleichterte.",
   "Umgekehrt kann δικαιοσύνη als Leitwort des Matthäus ([[MAT.5.20]]) eingesetzt worden sein, um den Satz zur Überschrift über alle drei Übungen zu machen.",
   AUTO + " lesen Sinaiticus (Erstschrift), Vaticanus und Bezae «Gerechtigkeit», Washingtonianus «Almosen». Eine Korrektur im Sinaiticus liest nach dem erfassten Wortlaut ein drittes Wort (δοσειν, wohl δόσιν, «Gabe»); die automatische Zuordnung führt sie als «liest anders»."],
  ["En Schriiber hät s allgemein Wort as nächscht Stichwort «Almose» ([[MAT.6.2]]) chöne aagliiche; spöter hät δικαιοσύνη sälber «Wohltätigkeit» chöne heisse.",
   "Umgekeert cha δικαιοσύνη als Leitwort vom Matthäus ([[MAT.5.20]]) iigsetzt worde sii, demit de Satz d Überschrift über alli drüü Üebige wird.",
   AUTO_G + " läsed de Sinaiticus (Erschtschrift), de Vaticanus und de Bezae «Grächtigkeit», de Washingtonianus «Almose». E Korrektur im Sinaiticus list nach em erfasste Wortlut es drittes Wort (δοσειν, wohl δόσιν, «Gab»)."]),
 ("VAR-SBLGNTAPP-MAT-006-004-01:R2", "MAT.6.4", "wird es dir vergelten", "wird er selbst es dir vergelten", "wird s dir vergälte", "wird er sälber s dir vergälte", "gering",
  "Der Zusatz betont, dass Gott selbst vergilt.", "De Zuesatz betont, dass Gott sälber vergiltet.",
  {"R1": [("κρυπτῷ", "im Verborgenen", "ohne Zusatz; SBLGNT, WH, Treg, NA28")], "R2": [("κρυπτῷ αὐτὸς", "im Verborgenen, er selbst", "RP")]},
  {"R1": [("κρυπτῷ", "im Verborgne", "ohni Zuesatz; SBLGNT, WH, Treg, NA28")], "R2": [("κρυπτῷ αὐτὸς", "im Verborgne, er sälber", "RP")]},
  ["Der Zusatz kann zur Verdeutlichung ergänzt worden sein; ein Grund für eine Streichung ist weniger erkennbar.",
   AUTO + " haben Sinaiticus und Vaticanus den kurzen Text, Washingtonianus und Bezae den Zusatz."],
  ["De Zuesatz cha zur Verdüütlichung ergänzt worde sii.",
   AUTO_G + " händ de Sinaiticus und de Vaticanus de churz Text, de Washingtonianus und de Bezae de Zuesatz."]),
 ("VAR-SBLGNTAPP-MAT-006-004-02:R2", "MAT.6.4", "wird es dir vergelten", "wird es dir öffentlich vergelten", "wird s dir vergälte", "wird s dir öffentlich vergälte", "mittel",
  "Der Zusatz stellt dem Verborgenen ein öffentliches Vergelten gegenüber; dieselbe Lesart steht in [[MAT.6.6]].",
  "De Zuesatz stellt em Verborgne es öffentlichs Vergälte gägenüber; di gliich Läsart staat i [[MAT.6.6]].",
  {"R1": [("σοι", "dir", "SBLGNT, WH, Treg, NA28")], "R2": [("σοι ἐν τῷ φανερῷ", "dir öffentlich", "RP")]},
  {"R1": [("σοι", "dir", "SBLGNT, WH, Treg, NA28")], "R2": [("σοι ἐν τῷ φανερῷ", "dir öffentlich", "RP")]},
  ["Der Gegensatz «im Verborgenen – öffentlich» lag nahe und kann als Erläuterung ergänzt worden sein; dieselbe Erweiterung steht in [[MAT.6.6]].",
   "Umgekehrt könnte die Wendung gestrichen worden sein, weil ein öffentlicher Lohn dem Gedanken der Stelle zu widersprechen schien.",
   AUTO + " haben Sinaiticus, Vaticanus und Bezae den kurzen Text, nur Washingtonianus den Zusatz."],
  ["De Gägesatz «im Verborgne – öffentlich» isch nöch gläge und cha als Erklärig ergänzt worde sii; di gliich Erwiiterig staat i [[MAT.6.6]].",
   "Umgekeert chönnt d Wändig gstriche worde sii, will en öffentliche Loon em Gedanke vo de Stell schiinbar widersproche hät.",
   AUTO_G + " händ de Sinaiticus, de Vaticanus und de Bezae de churz Text, nu de Washingtonianus de Zuesatz."]),
 ("VAR-SBLGNTAPP-MAT-006-021-01:R2", "MAT.6.21", "wo dein Schatz ist", "wo euer Schatz ist", "wo diin Schatz isch", "wo eue Schatz isch", "gering",
  "Mit «euer» passt der Vers zur Anrede in der Mehrzahl in [[MAT.6.19-MAT.6.20]].",
  "Mit «eue» passt de Vers zur Aared i de Mehrzahl i [[MAT.6.19-MAT.6.20]].",
  {"R1": [("σου", "dein", "SBLGNT, WH, Treg, NA28")], "R2": [("ὑμῶν", "euer", "RP")]},
  {"R1": [("σου", "diin", "SBLGNT, WH, Treg, NA28")], "R2": [("ὑμῶν", "eue", "RP")]},
  ["Die Einzahl nach der Mehrzahl von [[MAT.6.19-MAT.6.20]] ist auffällig; ein Schreiber konnte angleichen, auch an die Parallele [[LUK.12.34]], die die Mehrzahl hat.",
   AUTO + " lesen Sinaiticus und Vaticanus «dein», Washingtonianus «euer». Bezae ist an dieser Stelle nicht erhalten."],
  ["D Einzahl nach de Mehrzahl vo [[MAT.6.19-MAT.6.20]] fallt uf; en Schriiber hät chöne aagliiche, au a d Parallele [[LUK.12.34]] mit de Mehrzahl.",
   AUTO_G + " läsed de Sinaiticus und de Vaticanus «diin», de Washingtonianus «eue». De Bezae isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-006-021-02:R2", "MAT.6.21", "dort wird auch dein Herz sein", "dort wird auch euer Herz sein", "dört wird au diis Härz sii", "dört wird au eues Härz sii", "gering",
  "Wie beim ersten «dein» des Verses.", "Wie bim erschte «diin» vom Vers.",
  {"R1": [("σου", "dein", "SBLGNT, WH, Treg, NA28")], "R2": [("ὑμῶν", "euer", "RP")]},
  {"R1": [("σου", "diis", "SBLGNT, WH, Treg, NA28")], "R2": [("ὑμῶν", "eues", "RP")]},
  ["Siehe die Erklärung zum ersten «dein»; beide Stellen wechseln in denselben Zeugen gemeinsam.",
   AUTO + " lesen Sinaiticus und Vaticanus «dein», Washingtonianus «euer». Bezae ist an dieser Stelle nicht erhalten."],
  ["Lueg d Erklärig zum erschte «diin»; beidi Stelle wächsled i de gliiche Züüge mitenand.",
   AUTO_G + " läsed de Sinaiticus und de Vaticanus «diis», de Washingtonianus «eues». De Bezae isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-006-025-01:R2", "MAT.6.25", "was ihr essen sollt", "was ihr essen oder was ihr trinken sollt", "was ir ässed", "was ir ässed oder was ir trinked", "gering",
  "Mit dem Zusatz nennt der Vers Essen und Trinken wie [[MAT.6.31]]. Hier folgt der SBLGNT dem Rand von Westcott/Hort und weicht von deren Haupttext, von Treg und von NA28 ab.",
  "Mit em Zuesatz nännt de Vers Ässe und Trinke wie [[MAT.6.31]]. Da folgt de SBLGNT em Rand vo Westcott/Hort und wiicht vo dere Haupttext, vo Treg und vo NA28 ab.",
  {"R1": [("φάγητε", "essen", "SBLGNT, WH am Rand")], "R2": [("φάγητε ἢ τί πίητε", "essen oder was ihr trinken", "WH, Treg, NA28")], "R3": [("φάγητε καὶ τί πίητε", "essen und was ihr trinken", "RP")]},
  {"R1": [("φάγητε", "ässed", "SBLGNT, WH am Rand")], "R2": [("φάγητε ἢ τί πίητε", "ässed oder was ir trinked", "WH, Treg, NA28")], "R3": [("φάγητε καὶ τί πίητε", "ässed und was ir trinked", "RP")]},
  ["Der Zusatz kann aus [[MAT.6.31]] («Was sollen wir essen? oder: Was sollen wir trinken?») übernommen sein; die Parallele [[LUK.12.22]] hat ihn nicht.",
   "Umgekehrt konnte das Glied beim Abschreiben ausfallen, weil τί φάγητε und τί πίητε ähnlich klingen und enden (Augensprung).",
   AUTO + " hat Sinaiticus den kurzen Text, Vaticanus und Washingtonianus die Lesart mit «oder». Bezae ist an dieser Stelle nicht erhalten."],
  ["De Zuesatz cha us [[MAT.6.31]] übernoo sii; d Parallele [[LUK.12.22]] hät en nöd.",
   "Umgekeert hät s Glid bim Abschriibe chöne usfalle, will τί φάγητε und τί πίητε ähnlich tönd und ändet (Augesprung).",
   AUTO_G + " hät de Sinaiticus de churz Text, de Vaticanus und de Washingtonianus d Läsart mit «oder». De Bezae isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-006-033-01:R2", "MAT.6.33", "das Reich", "das Reich Gottes", "s Riich", "s Riich vo Gott", "mittel",
  "Mit dem Zusatz ist ausdrücklich gesagt, wessen Reich gemeint ist; ohne ihn bezieht sich «seine» auf den Vater aus [[MAT.6.32]]. Matthäus sagt sonst meist «Reich der Himmel», «Reich Gottes» nur selten ([[MAT.12.28]], [[MAT.19.24]], [[MAT.21.31]], [[MAT.21.43]]). Der SBLGNT folgt hier Westcott/Hort.",
  "Mit em Zuesatz isch usdrücklich gseit, wem sis Riich gmeint isch; ohni en bezieht sich «sini» uf de Vatter us [[MAT.6.32]]. De Matthäus seit suscht meischt «Riich vo de Himel». De SBLGNT folgt da Westcott/Hort.",
  {"R1": [("τὴν βασιλείαν", "das Reich", "SBLGNT, WH")], "R2": [("τὴν βασιλείαν τοῦ θεοῦ", "das Reich Gottes", "Treg, NA28, RP")]},
  {"R1": [("τὴν βασιλείαν", "s Riich", "SBLGNT, WH")], "R2": [("τὴν βασιλείαν τοῦ θεοῦ", "s Riich vo Gott", "Treg, NA28, RP")]},
  ["«Gottes» kann zur Verdeutlichung ergänzt worden sein; dass ein Schreiber es gestrichen hätte, ist weniger naheliegend.",
   "Umgekehrt ist «Reich Gottes» für Matthäus ungewöhnlich, was für diese Lesart als die schwierigere sprechen kann.",
   AUTO + " liest Sinaiticus (Erstschrift und Korrektur) «das Reich», Washingtonianus «das Reich Gottes». Vaticanus liest anders als beide: Nach dem erfassten Wortlaut steht bei ihm die Gerechtigkeit vor dem Reich. Bezae ist an dieser Stelle nicht erhalten."],
  ["«vo Gott» cha zur Verdüütlichung ergänzt worde sii.",
   "Umgekeert isch «Riich vo Gott» für de Matthäus ungwöhnlich; das cha für die Läsart als di schwierigeri rede.",
   AUTO_G + " list de Sinaiticus (Erschtschrift und Korrektur) «s Riich», de Washingtonianus «s Riich vo Gott». De Vaticanus list andersch: Nach em erfasste Wortlut staat bi ihm d Grächtigkeit vor em Riich. De Bezae isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-006-034-01:R3", "MAT.6.34", "wird für sich selbst sorgen", "wird für das Seine sorgen", "wird für sich sälber sorge", "wird für sini eigete Sache sorge", "gering",
  "Mit dem Artikel (τὰ ἑαυτῆς) heisst es «das Seine», die eigenen Angelegenheiten; der Sinn bleibt nahezu gleich. R1 und R2 sind zwei Schreibungen desselben Wortes.",
  "Mit em Artikel (τὰ ἑαυτῆς) heisst s «s Sine», di eigete Sache; de Sinn bliibt fasch gliich.",
  {"R1": [("αὑτῆς", "für sich", "SBLGNT, WH")], "R2": [("ἑαυτῆς", "für sich selbst", "Treg, NA28")], "R3": [("τὰ ἑαυτῆς", "für das Seine", "RP")]},
  {"R1": [("αὑτῆς", "für sich", "SBLGNT, WH")], "R2": [("ἑαυτῆς", "für sich sälber", "Treg, NA28")], "R3": [("τὰ ἑαυτῆς", "für sini eigete Sache", "RP")]},
  ["Der Artikel kann ergänzt worden sein, um die ungewöhnliche Verbindung von μεριμνάω mit dem Genitiv zu glätten.",
   AUTO + " liest Vaticanus αυτης (ohne Akzente), Sinaiticus und Washingtonianus ἑαυτῆς; keine der erfassten Handschriften hat den Artikel. Bezae ist an dieser Stelle nicht erhalten."],
  ["De Artikel cha ergänzt worde sii, zum di ungwöhnlich Verbindig vo μεριμνάω mit em Genitiv z glätte.",
   AUTO_G + " list de Vaticanus αυτης (ohni Akzänt), de Sinaiticus und de Washingtonianus ἑαυτῆς; keini vo de erfasste Handschrifte hät de Artikel. De Bezae isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-007-013-01:R2", "MAT.7.13", "weit ist das Tor und breit der Weg", "weit und breit ist der Weg", "wiit isch s Tor und breit de Wäg", "wiit und breit isch de Wäg", "mittel",
  "Ohne «das Tor» spricht der zweite Satz nur vom Weg; das Tor steht dann nur am Anfang. So lesen Westcott/Hort; der SBLGNT folgt hier den anderen Editionen.",
  "Ohni «s Tor» redt de zweit Satz nu vom Wäg. So läsed Westcott/Hort; de SBLGNT folgt da de andere Usgabe.",
  {"R1": [("πλατεῖα ἡ πύλη καὶ εὐρύχωρος", "weit ist das Tor und breit", "SBLGNT, Treg, NA28, RP")], "R2": [("πλατεῖα καὶ εὐρύχωρος", "weit und breit", "WH")]},
  {"R1": [("πλατεῖα ἡ πύλη καὶ εὐρύχωρος", "wiit isch s Tor und breit", "SBLGNT, Treg, NA28, RP")], "R2": [("πλατεῖα καὶ εὐρύχωρος", "wiit und breit", "WH")]},
  ["Das Wort kann ergänzt worden sein, damit [[MAT.7.13]] dem Aufbau von [[MAT.7.14]] («eng ist das Tor und schmal der Weg») entspricht.",
   "Umgekehrt konnte ἡ πύλη nach dem vorangehenden πύλης beim Abschreiben ausfallen.",
   AUTO + " fehlt «das Tor» im Sinaiticus in der Erstschrift; eine Korrektur ergänzt es. Vaticanus, Washingtonianus und Ephraemi haben es."],
  ["S Wort cha ergänzt worde sii, demit [[MAT.7.13]] glich bout isch wie [[MAT.7.14]].",
   "Umgekeert hät ἡ πύλη nach em vorhärige πύλης bim Abschriibe chöne usfalle.",
   AUTO_G + " fehlt «s Tor» im Sinaiticus i de Erschtschrift; e Korrektur ergänzt s. De Vaticanus, de Washingtonianus und de Ephraemi händ s."]),
 ("VAR-SBLGNTAPP-MAT-007-014-01:R3", "MAT.7.14", "Denn eng ist das Tor", "Wie eng ist das Tor", "Dänn äng isch s Tor", "Wie äng isch s Tor", "mittel",
  "Mit τί wird der Satz zum Ausruf («Wie eng ist das Tor und wie schmal der Weg …!») und begründet nicht mehr die Aufforderung von [[MAT.7.13]]. Der SBLGNT folgt hier Westcott/Hort.",
  "Mit τί wird de Satz zumene Uusruef («Wie äng isch s Tor …!») und begründet d Uffordrig vo [[MAT.7.13]] nüme. De SBLGNT folgt da Westcott/Hort.",
  {"R1": [("ὅτι", "denn", "SBLGNT, WH")], "R2": [("ὅτι δὲ", "denn aber", "NIV")], "R3": [("τί", "wie (eng)!", "Treg, NA28, RP")]},
  {"R1": [("ὅτι", "dänn", "SBLGNT, WH")], "R2": [("ὅτι δὲ", "dänn aber", "NIV")], "R3": [("τί", "wie (äng)!", "Treg, NA28, RP")]},
  ["τί als Ausruf («wie!») ist ungewöhnlich und wird als semitisch gefärbt angesehen; ein Schreiber konnte es an das ὅτι von [[MAT.7.13]] angleichen.",
   "Umgekehrt kann τί aus ὅτι entstanden sein: In Grossbuchstaben ohne Worttrennung unterscheiden sich ΟΤΙ und ΤΙ nur durch einen Buchstaben, der leicht verloren geht.",
   AUTO + " liest Sinaiticus in der Erstschrift ὅτι, eine Korrektur τί; Vaticanus ὅτι δέ. Eine Korrektur im Vaticanus hat nach dem erfassten Wortlaut τι δε; die automatische Zuordnung rechnet sie zu ὅτι δέ, was unsicher ist. Washingtonianus und Ephraemi lesen τί."],
  ["τί als Uusruef isch ungwöhnlich; en Schriiber hät s as ὅτι vo [[MAT.7.13]] chöne aagliiche.",
   "Umgekeert cha τί us ὅτι entstande sii: I Grossbuechstabe ohni Worttränig underscheided sich ΟΤΙ und ΤΙ nu dur en Buechstabe.",
   AUTO_G + " list de Sinaiticus i de Erschtschrift ὅτι, e Korrektur τί; de Vaticanus ὅτι δέ. E Korrektur im Vaticanus hät nach em erfasste Wortlut τι δε; d automatisch Zueornig rächnet si zu ὅτι δέ, was unsicher isch. De Washingtonianus und de Ephraemi läsed τί."]),
 ("VAR-SBLGNTAPP-MAT-007-024-01:R2", "MAT.7.24", "wird einem klugen Mann gleichen", "den werde ich einem klugen Mann vergleichen", "isch wie en gschiide Maa", "dä vergliich ich mit eme gschiide Maa", "gering",
  "Mit ὁμοιώσω αὐτόν spricht Jesus in der Ich-Form, wie in [[MAT.7.23]]; der Sinn bleibt fast gleich.",
  "Mit ὁμοιώσω αὐτόν redt de Jesus i de Ich-Form, wie i [[MAT.7.23]]; de Sinn bliibt fasch gliich.",
  {"R1": [("ὁμοιωθήσεται", "wird gleichen", "SBLGNT, WH, Treg, NA28")], "R2": [("ὁμοιώσω αὐτὸν", "werde ich ihn vergleichen", "RP")]},
  {"R1": [("ὁμοιωθήσεται", "isch wie", "SBLGNT, WH, Treg, NA28")], "R2": [("ὁμοιώσω αὐτὸν", "vergliich ich en", "RP")]},
  ["Die Parallele [[LUK.6.47]] ist in der Ich-Form gehalten («ich will euch zeigen, wem er gleich ist»), und Vergleiche Jesu beginnen auch sonst mit ὁμοιώσω (vgl. [[MAT.11.16]]); die Lesart kann davon beeinflusst sein. In [[MAT.7.26]] steht in allen erfassten Editionen ὁμοιωθήσεται.",
   AUTO + " lesen Sinaiticus und Vaticanus ὁμοιωθήσεται, Washingtonianus und Ephraemi ὁμοιώσω αὐτόν."],
  ["D Parallele [[LUK.6.47]] isch i de Ich-Form, und Vergliich vom Jesus fanged au suscht mit ὁμοιώσω aa (vgl. [[MAT.11.16]]); d Läsart cha devo beiflusst sii.",
   AUTO_G + " läsed de Sinaiticus und de Vaticanus ὁμοιωθήσεται, de Washingtonianus und de Ephraemi ὁμοιώσω αὐτόν."]),
 ("VAR-SBLGNTAPP-MAT-007-029-01:R2", "MAT.7.29", "wie ihre Schriftgelehrten", "wie die Schriftgelehrten", "wie iri Schriftgelehrte", "wie d Schriftgelehrte", "gering",
  "Ohne «ihre» fehlt die Zuordnung der Schriftgelehrten zur Menge.", "Ohni «iri» fehlt d Zueornig vo de Schriftgelehrte zur Mängi.",
  {"R1": [("οἱ γραμματεῖς αὐτῶν", "ihre Schriftgelehrten", "SBLGNT, WH, Treg, NA28")], "R2": [("οἱ γραμματεῖς", "die Schriftgelehrten", "RP")]},
  {"R1": [("οἱ γραμματεῖς αὐτῶν", "iri Schriftgelehrte", "SBLGNT, WH, Treg, NA28")], "R2": [("οἱ γραμματεῖς", "d Schriftgelehrte", "RP")]},
  ["Die Parallele [[MRK.1.22]] hat «die Schriftgelehrten» ohne «ihre»; die kürzere Lesart kann an Markus angeglichen sein. Umgekehrt kann «ihre» ergänzt worden sein (vgl. «ihre Synagogen» in [[MAT.4.23]]).",
   AUTO + " haben Sinaiticus, Vaticanus und Washingtonianus «ihre», Ephraemi lässt es weg."],
  ["D Parallele [[MRK.1.22]] hät «d Schriftgleerte» ohni «iri»; di chürzer Läsart cha am Markus aagliche sii. Umgekeert cha «iri» ergänzt worde sii (vgl. [[MAT.4.23]]).",
   AUTO_G + " händ de Sinaiticus, de Vaticanus und de Washingtonianus «iri», de Ephraemi laat s weg."]),
]

UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-006-001-034", "MAT.6.1-MAT.6.34", "section", "Almosen, Gebet und Fasten; Schätze und Sorgen",
  ["TU-MAT-006-001-004", "TU-MAT-006-005-015", "TU-MAT-006-016-018", "TU-MAT-006-019-024", "TU-MAT-006-025-034"],
  "Jesus warnt davor, die Gerechtigkeit vor den Menschen zu üben, um gesehen zu werden: Almosen, Gebet und Fasten sollen im Verborgenen geschehen, dann wird der Vater, der ins Verborgene sieht, es vergelten; zum Beten gibt er das Vaterunser und sagt, dass der Vater nur denen vergibt, die selbst den Menschen vergeben. Dann fordert er auf, Schätze im Himmel statt auf der Erde zu sammeln, nennt das Auge die Lampe des Leibes und sagt, dass niemand Gott und dem Mammon dienen kann. Sie sollen sich nicht um Essen und Kleidung sorgen, denn der himmlische Vater weiss, was sie brauchen; sie sollen zuerst das Reich und seine Gerechtigkeit suchen.",
  "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung. Teil der Bergpredigt ([[MAT.5.1-MAT.7.29]]). [[MAT.6.1]] kann als Überschrift über [[MAT.6.1-MAT.6.18]] gelesen werden. [[MAT.6.5-MAT.6.15]] ist die bestehende Einheit TU-MAT-006-005-015 mit eigenen Teilen. [[MAT.6.22-MAT.6.23]] und [[MAT.6.24]] können auch als eigene Einheiten gelten."),
 ("TU-MAT-006-001-004", "MAT.6.1-MAT.6.4", "discourse", "Vom Almosengeben", None,
  "Jesus warnt, die Gerechtigkeit nicht vor den Menschen zu üben, um von ihnen gesehen zu werden; sonst gibt es keinen Lohn beim Vater in den Himmeln. Wer Almosen gibt, soll nicht die Posaune vor sich her blasen, wie es die Heuchler in Synagogen und Gassen tun, um von den Menschen gerühmt zu werden; sie haben ihren Lohn schon erhalten. Die linke Hand soll nicht wissen, was die rechte tut; der Vater, der ins Verborgene sieht, wird es vergelten.", None),
 ("TU-MAT-006-016-018", "MAT.6.16-MAT.6.18", "discourse", "Vom Fasten", None,
  "Wer fastet, soll kein düsteres Gesicht machen wie die Heuchler, die ihr Gesicht unkenntlich machen, damit die Menschen ihr Fasten sehen; sie haben ihren Lohn schon erhalten. Wer fastet, soll den Kopf salben und das Gesicht waschen, damit nicht die Menschen es sehen, sondern der Vater im Verborgenen; er wird es vergelten.", None),
 ("TU-MAT-006-019-024", "MAT.6.19-MAT.6.24", "discourse", "Schätze im Himmel", None,
  "Jesus fordert auf, keine Schätze auf der Erde zu sammeln, wo Motte und Frass zerstören und Diebe stehlen, sondern im Himmel; denn wo der Schatz ist, dort wird auch das Herz sein. Das Auge ist die Lampe des Leibes: Ist es klar, wird der ganze Leib hell sein, ist es schlecht, finster. Niemand kann zwei Herren dienen; man kann nicht Gott dienen und dem Mammon.", None),
 ("TU-MAT-006-025-034", "MAT.6.25-MAT.6.34", "discourse", "Sorgt euch nicht", None,
  "Jesus sagt, sie sollen sich nicht um Essen und Kleidung sorgen. Der himmlische Vater ernährt die Vögel, und nicht einmal Salomo war gekleidet wie eine Lilie; wenn Gott schon das Gras so kleidet, wie viel mehr wird er sie kleiden, die Kleingläubigen. Durch Sorgen kann niemand seiner Lebenszeit etwas hinzufügen. Nach all dem trachten die Heiden; der Vater aber weiss, dass sie es brauchen. Sie sollen zuerst das Reich und seine Gerechtigkeit suchen, dann wird ihnen das alles dazugegeben, und sich nicht um den morgigen Tag sorgen: Jeder Tag hat genug an seiner eigenen Plage.", None),
 ("TU-MAT-007-001-029", "MAT.7.1-MAT.7.29", "section", "Richten, Bitten, die zwei Wege und der Schluss der Bergpredigt",
  ["TU-MAT-007-001-006", "TU-MAT-007-007-012", "TU-MAT-007-013-014", "TU-MAT-007-015-023", "TU-MAT-007-024-027", "TU-MAT-007-028-029"],
  "Jesus sagt: Richtet nicht; wer den Splitter im Auge des Bruders sieht, soll zuerst den Balken aus dem eigenen Auge ziehen; das Heilige soll man nicht den Hunden geben. Er ermutigt zum Bitten, denn der Vater in den Himmeln wird denen Gutes geben, die ihn bitten, und fasst zusammen: Was ihr wollt, dass euch die Menschen tun, das tut auch ihnen; das ist das Gesetz und die Propheten. Er ruft dazu auf, durch das enge Tor hineinzugehen, warnt vor falschen Propheten, die man an ihren Früchten erkennt, und sagt, dass nicht jeder, der «Herr, Herr» sagt, ins Reich der Himmel kommt, sondern wer den Willen des Vaters tut. Wer seine Worte hört und tut, wird einem klugen Mann gleichen, der auf den Felsen gebaut hat; wer sie nicht tut, einem törichten, der auf Sand gebaut hat. Als Jesus die Rede beendet hat, ist die Menge überwältigt, denn er lehrt mit Vollmacht.",
  "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung. Schluss der Bergpredigt ([[MAT.5.1-MAT.7.29]]). [[MAT.7.12]] kann auch als Abschluss des Hauptteils der Rede für sich stehen; [[MAT.7.28-MAT.7.29]] ist der erzählende Abschluss mit der Formel, die alle fünf grossen Reden des Matthäus beendet."),
 ("TU-MAT-007-001-006", "MAT.7.1-MAT.7.6", "discourse", "Vom Richten", None,
  "Jesus sagt: Richtet nicht, damit ihr nicht gerichtet werdet; mit dem Mass, mit dem ihr messt, wird euch gemessen werden. Wer den Splitter im Auge des Bruders sieht, soll zuerst den Balken aus dem eigenen Auge ziehen. Das Heilige soll man nicht den Hunden geben und die Perlen nicht vor die Schweine werfen.", None),
 ("TU-MAT-007-007-012", "MAT.7.7-MAT.7.12", "discourse", "Bittet, sucht, klopft an", None,
  "Jesus fordert auf zu bitten, zu suchen und anzuklopfen, denn wer bittet, empfängt. Wenn schon Menschen, die böse sind, ihrem Sohn keinen Stein statt Brot geben, sondern ihren Kindern gute Gaben, wie viel mehr wird der Vater in den Himmeln denen Gutes geben, die ihn bitten. Was ihr wollt, dass euch die Menschen tun, das sollt ihr ihnen tun; das ist das Gesetz und die Propheten.", None),
 ("TU-MAT-007-013-014", "MAT.7.13-MAT.7.14", "discourse", "Das enge Tor", None,
  "Jesus ruft dazu auf, durch das enge Tor hineinzugehen: Weit ist das Tor und breit der Weg ins Verderben, und viele gehen dort hinein; eng ist das Tor und schmal der Weg ins Leben, und wenige finden ihn.", None),
 ("TU-MAT-007-015-023", "MAT.7.15-MAT.7.23", "discourse", "An den Früchten erkennen", None,
  "Jesus warnt vor falschen Propheten, die in Schafskleidern kommen und innen reissende Wölfe sind: An ihren Früchten wird man sie erkennen, wie einen Baum an seinen Früchten; jeder Baum ohne gute Frucht wird umgehauen und ins Feuer geworfen. Nicht jeder, der «Herr, Herr» sagt, wird ins Reich der Himmel hineinkommen, sondern wer den Willen des Vaters tut. Vielen, die sich an jenem Tag auf Prophezeien, Dämonenaustreibungen und Machttaten in seinem Namen berufen, wird er erklären: «Nie habe ich euch gekannt», und sie von sich weisen.", None),
 ("TU-MAT-007-024-027", "MAT.7.24-MAT.7.27", "discourse", "Das Haus auf dem Felsen", None,
  "Jesus sagt: Wer seine Worte hört und tut, wird einem klugen Mann gleichen, der sein Haus auf den Felsen gebaut hat; Regen, Fluten und Winde bringen es nicht zum Einsturz. Wer sie hört und nicht tut, wird einem törichten Mann gleichen, der auf Sand gebaut hat; sein Haus stürzt ein, und der Einsturz ist gewaltig.", None),
 ("TU-MAT-007-028-029", "MAT.7.28-MAT.7.29", "narrative", "Die Menge ist überwältigt", None,
  "Als Jesus diese Worte beendet hat, ist die Menge überwältigt von seiner Lehre, denn er lehrt sie wie einer, der Vollmacht hat, und nicht wie ihre Schriftgelehrten.", None),
]
UNITS_GSW = {
 "TU-MAT-006-001-034": ("Almose, Gebät und Faschte; Schätz und Sorge",
  "De Jesus warnt devor, d Grächtigkeit vor de Lüüt z üebe, zum gsee z wärde: Almose, Gebät und Faschte söled im Verborgne gschee, dänn wird de Vatter, wo is Verborgne gseet, s vergälte; zum Bätte git er s Vatterunser und seit, dass de Vatter nu dene vergit, wo sälber de Lüüt vergänd. Dänn fordered er uf, Schätz im Himel statt uf de Ärde z sammle, nännt s Aug d Lampe vom Liib und seit, dass niemer Gott und em Mammon cha diene. Si söled sich kei Sorge mache um Ässe und Chleider, dänn de himmlisch Vatter weiss, was si bruuched; si söled zerscht s Riich und sini Grächtigkeit sueche."),
 "TU-MAT-006-001-004": ("Vom Almosegää",
  "De Jesus warnt, d Grächtigkeit nöd vor de Lüüt z üebe, zum vo ine gsee z wärde; suscht gits kei Loon bim Vatter i de Himel. Wer Almose git, söll nöd d Posuune vor sich här blaase, wie s d Hüüchler i de Synagoge und i de Gasse mached, zum vo de Lüüt grüemt z wärde; die händ ire Loon scho übercho. Di lingg Hand söll nöd wüsse, was di rächt macht; de Vatter, wo is Verborgne gseet, wird s vergälte."),
 "TU-MAT-006-016-018": ("Vom Faschte",
  "Wer faschtet, söll kei finschters Gsicht mache wie d Hüüchler, wo ires Gsicht unkänntlich mached, demit d Lüüt gseend, dass si faschted; die händ ire Loon scho übercho. Wer faschtet, söll de Chopf salbe und s Gsicht wäsche, demit nöd d Lüüt s gseend, sondern de Vatter im Verborgne; er wird s vergälte."),
 "TU-MAT-006-019-024": ("Schätz im Himel",
  "De Jesus fordered uf, kei Schätz uf de Ärde z sammle, wo Schabe und Frass alles kaputt mached und Dieb stääled, sondern im Himel; dänn wo de Schatz isch, dört wird au s Härz sii. S Aug isch d Lampe vom Liib: Isch s klar, wird de ganz Liib hell sii, isch s schlächt, fiischter. Niemer cha zwei Herre diene; me cha nöd Gott diene und em Mammon."),
 "TU-MAT-006-025-034": ("Mached eu kei Sorge",
  "De Jesus seit, si söled sich kei Sorge mache um Ässe und Chleider. De himmlisch Vatter git de Vögel z ässe, und nöd emal de Salomo isch aagleit gsii wie e Lilie; wänn Gott scho s Gras eso aaleit, wie vil meh wird er si aalegge, di Chliigläubige. Mit Sorge mache cha niemer sinere Läbesziit öppis dezuetue. All das sueched d Heide; de Vatter aber weiss, dass si s bruuched. Si söled zerscht s Riich und sini Grächtigkeit sueche, dänn wird ene das alles dezue ggää, und sich kei Sorge um de morgig Tag mache: Jedem Tag längt sini eiget Plaag."),
 "TU-MAT-007-001-029": ("Richte, Bitte, di zwee Wäg und de Schluss vo de Bärgpredig",
  "De Jesus seit: Richted nöd; wer de Splitter im Aug vo sim Brueder gseet, söll zerscht de Balke us em eigete Aug usezie; s Heilig söll me nöd de Hünd gää. Er macht Muet zum Bitte, dänn de Vatter i de Himel wird dene Guets gää, wo en drum bitted, und fasst zäme: Was ir wänd, dass eu d Lüüt tüend, das tüend au ine; das isch s Gsetz und d Prophete. Er rüeft uf, dur s äng Tor ine z gaa, warnt vor falsche Prophete, wo me a irne Frücht erchännt, und seit, dass nöd jede, wo «Herr, Herr» seit, is Riich vo de Himel chunnt, sondern wer de Wile vom Vatter tuet. Wer sini Wort ghört und tuet, isch wie en gschiide Maa, wo uf de Fels buut hät; wer si nöd tuet, wie en tumme, wo uf Sand buut hät. Wo de Jesus mit de Red fertig isch, isch d Mängi überwältiget, dänn er leert mit Vollmacht."),
 "TU-MAT-007-001-006": ("Vom Richte",
  "De Jesus seit: Richted nöd, demit ir nöd grichtet wärded; mit em Mass, wo ir mässed, wird eu gmässe. Wer de Splitter im Aug vo sim Brueder gseet, söll zerscht de Balke us em eigete Aug usezie. S Heilig söll me nöd de Hünd gää und d Perle nöd vor d Säu rüere."),
 "TU-MAT-007-007-012": ("Bitted, sueched, chlopfed aa",
  "De Jesus fordered uf z bitte, z sueche und aazchlopfe, dänn wer bittet, überchunnt. Wänn scho Mänsche, wo bös sind, irem Sohn kei Stei statt Broot gänd, sondern irne Chind gueti Gabe, wie vil meh wird de Vatter i de Himel dene Guets gää, wo en drum bitted. Was ir wänd, dass eu d Lüüt tüend, das söled ir ine tue; das isch s Gsetz und d Prophete."),
 "TU-MAT-007-013-014": ("S äng Tor",
  "De Jesus rüeft uf, dur s äng Tor ine z gaa: Wiit isch s Tor und breit de Wäg is Verderbe, und vil gönd dört ine; äng isch s Tor und schmaal de Wäg is Läbe, und wenig finded en."),
 "TU-MAT-007-015-023": ("A de Frücht erchänne",
  "De Jesus warnt vor falsche Prophete, wo i Schaafchleider chömed und inne riissendi Wölf sind: A irne Frücht wird me si erchänne, wie en Baum a sine Frücht; jede Baum ohni gueti Frucht wird umghaue und is Füür gworfe. Nöd jede, wo «Herr, Herr» seit, chunnt is Riich vo de Himel ine, sondern wer de Wile vom Vatter tuet. Vilne, wo sich a dem Tag uf Profezeie, Dämone-Ustriibe und Machttate i sim Name berüefed, wird er offe säge: «Nie han ich eu kännt», und si vo sich wegschicke."),
 "TU-MAT-007-024-027": ("S Huus uf em Fels",
  "De Jesus seit: Wer sini Wort ghört und tuet, isch wie en gschiide Maa, wo sis Huus uf de Fels buut hät; Räge, Hochwasser und Wind bringed s nöd zum Iistürze. Wer si ghört und nöd tuet, isch wie en tumme Maa, wo uf Sand buut hät; sis Huus stürzt ii, und de Iisturz isch gwaltig."),
 "TU-MAT-007-028-029": ("D Mängi isch überwältiget",
  "Wo de Jesus mit dene Wort fertig isch, isch d Mängi überwältiget vo sinere Lehr, dänn er leert si wie eine, wo Vollmacht hät, und nöd wie iri Schriftgelehrte."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten in den Alternativen beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1, "
  "WREAD-CNTR-MAT-006-001-004, WREAD-CNTR-MAT-006-016-034, WREAD-CNTR-MAT-007-001-029) bzw. auf dem dort erfassten Wortlaut der "
  "CNTR-Transkriptionen (Sekundärtranskription), nicht auf eigener Prüfung der Handschriften. Wo die automatische Zuordnung unsicher "
  "ist (z. B. eine Korrektur im Vaticanus zu [[MAT.7.14]]), ist das bei der Alternative gesagt."),
 ("Abgrenzung: [[MAT.6.5-MAT.6.15]] ist in eigenen Arbeitsübersetzungen erfasst (TRANS-MAT-006-005-015-DE-WORKING, "
  "scripts/authoring/vaterunser.py) und wird hier nicht berührt. Kapitel 6 hat deshalb zwei Übersetzungen dieses Werkzeugs "
  "([[MAT.6.1-MAT.6.4]] und [[MAT.6.16-MAT.6.34]]). Wortlaut und Begriffe sind auf das Vaterunser-Stück abgestimmt: «Heuchler», "
  "«Synagogen», «Amen, ich sage euch», «Sie haben ihren Lohn schon erhalten», «dein Vater, der ins Verborgene sieht, wird es dir "
  "vergelten», «in den Himmeln», «himmlischer Vater», «Heiden», «Menschen»."),
 ("Einheitliche Begriffe für Matthäus (gemeinsame Festlegung für alle Bereiche): «Reich der Himmel», «Amen, ich sage euch», «Vater in den "
  "Himmeln», «himmlisch», «siehe», «Heuchler», «Schriftgelehrte», «Dämon». In diesem Bereich zusätzlich festgelegt: δικαιοσύνη "
  "«Gerechtigkeit» (auch [[MAT.6.1]], wo sie Almosen, Beten und Fasten überschreibt); μισθός «Lohn»; ἐλεημοσύνη «Almosen»; μεριμνάω «sich "
  "sorgen»; ὀλιγόπιστοι «Kleingläubige»; ἔθνη «Heiden» (wie ἐθνικοί in [[MAT.6.7]]); μαμωνᾶς «Mammon»; κρίνω «richten»; καρπός «Frucht»; "
  "ψευδοπροφῆται «falsche Propheten»; ἀνομία «Gesetzlosigkeit»; δυνάμεις «Machttaten»; ὄχλοι «die Menge» (Einzahl)."),
 ("Redegrenzen: Die Bergpredigt ([[MAT.5.3-MAT.7.27]]) ist eine durchgehende Rede Jesu. Wie in [[MAT.6.5-MAT.6.15]] steht sie ohne "
  "äussere Anführungszeichen; Zitate innerhalb der Rede ([[MAT.6.31]], [[MAT.7.4]], [[MAT.7.21-MAT.7.23]]) stehen in «»."),
 ("Zeitformen: Futur bleibt Futur, wo das Deutsche es trägt («wird es dir vergelten», «werdet ihr sie erkennen»); das Gleichnis vom "
  "Hausbau erzählt im Präteritum. ὅτι vor direkter Rede ist nicht eigens übersetzt."),
 ("Text: Die Übersetzung folgt an allen Apparatstellen dem SBLGNT (follows_readings), auch wo er gegen die meisten erfassten Editionen "
  "liest: [[MAT.6.25]] (ohne «oder was ihr trinken sollt», mit dem Rand von WH), [[MAT.6.33]] («das Reich» ohne «Gottes», mit WH) und "
  "[[MAT.7.14]] («denn» statt «wie», mit WH). Abweichende Lesarten stehen als Alternativen, soweit sie die Übersetzung verändern; "
  "reine Wortstellungs- und Schreibvarianten (z. B. [[MAT.6.18]] κρυφαίῳ/κρυπτῷ, [[MAT.7.5]]) sind nicht aufgenommen."),
 "In Matthäus 6–7 fehlt im SBLGNT kein Vers (per Skript geprüft); alle Verse sind übersetzt.",
 "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf em erfasste Wortlut vo de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Abgränzig: [[MAT.6.5-MAT.6.15]] staat i TRANS-MAT-006-005-015-GSW-ZH-WORKING (scripts/authoring/vaterunser.py) und wird da nöd aagrüert. "
  "Wörter sind druf abgstimmt: «Hüüchler», «Synagoge», «Si händ ire Loon scho übercho», «diin Vatter, wo is Verborgne gseet, wird s dir "
  "vergälte», «i de Himel», «himmlisch Vatter», «d Heide», «d Lüüt», «ir»."),
 ("Einheitlichi Wörter: «s Riich vo de Himel», «Amen, ich säg eu», «Vatter i de Himel», «lueg», «Schriftgelehrti», «Dämon»; neu i dem Bereich: "
  "δικαιοσύνη «Grächtigkeit», μισθός «Loon», ἐλεημοσύνη «Almose», μεριμνάω «sich Sorge mache», ὀλιγόπιστοι «Chliigläubigi», ἔθνη «d Heide», "
  "μαμωνᾶς «Mammon», κρίνω «richte», ἀνομία «Gsetzlosigkeit», δυνάμεις «Machttate», ὄχλοι «d Mängi». ὑποκριταί heisst wie im Vaterunser-Stuck "
  "und bim Markus «Hüüchler»."),
 ("Mundart: Näme mit Artikel («de Salomo», «de Jesus»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv («s Riich vo de Himel»); "
  "s griechisch Futur oft mit em Präsens («er hanget am eint aa»)."),
 "D Bärgpredig staat wie i [[MAT.6.5-MAT.6.15]] ohni üsseri Aafüerigszeiche; Zitat i de Red staat i «».",
 "D Übersetzig folgt a allne Apparatstelle em SBLGNT, au i [[MAT.6.25]], [[MAT.6.33]] und [[MAT.7.14]]. I Matthäus 6–7 fehlt im SBLGNT kei Vers.",
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
    toks_by_ch = {}
    for c, last in CHAPTER_LAST.items():
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-MAT-{c:03d}.json")
        if [f"MAT.{c}.{v}" for v in range(1, last + 1) if f"MAT.{c}.{v}" not in toks]:
            raise SystemExit(f"MAT {c}: unerwartet fehlende Verse")
        toks_by_ch[c] = (ts_id, toks)
    for c, first, last in SEGMENTS:
        ts_id, toks = toks_by_ch[c]
        refs_c = [f"MAT.{c}.{v}" for v in range(first, last + 1)]
        follows = sorted(f"{vid}:{r['reading_id']}" for vid, v in variants.items() if v["reference"] in refs_c
                         for r in v["readings"] if r.get("is_sblgnt_text"))
        span = f"{c:03d}-{first:03d}-{last:03d}"
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-MAT-{span}-{code}-WORKING"
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
                rid = vid.split(":")[1]
                if rid not in [r["reading_id"] for r in variants[vid.split(":")[0]]["readings"]]:
                    raise SystemExit(f"{tid}: Lesart {vid} nicht im Apparat")
                f_, t_, nt, ws, og = (f_de, t_de, n_de, w_de, o_de) if lang == "de" else (f_g, t_g, n_g, w_g, o_g)
                if f_ not in texts[ref]:
                    raise SystemExit(f"{tid}: Alternative {f_!r} nicht im Text {ref}")
                alts.append({"reading": vid, "reference": ref, "from_text": f_, "to_text": t_, "effect": eff, "note": nt,
                             "readings": {k: [{"grc": g, "text": x, **({"note": h} if h else {})} for g, x, h in v] for k, v in ws.items()},
                             "origin": og})
            ref_rng = f"MAT.{c}.{first}-MAT.{c}.{last}"
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": ref_rng,
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich, Loon), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Artikel vor Personennamen. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{span}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; Begriffe einheitlich für ganz Matthäus und abgestimmt auf [[MAT.6.5-MAT.6.15]]. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
            aid = f"ALIGN-MAT-{span}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": ref_rng,
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_06_07.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 6,1–4; 6,16–34; 7,1–29 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
