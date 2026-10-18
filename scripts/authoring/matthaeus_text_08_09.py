#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 8–9 (Heilungen, Nachfolge, Sturm, Gadarener, Gelähmter, Matthäus, Fastenfrage, Tochter des
Vorstehers, Blinde, stummer Besessener, Ernte) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem
SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_08_09.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits (scripts/authoring/vaterunser.py) und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 8–9 fehlt im SBLGNT kein Vers (per Skript geprüft); alle Verse haben Tokens.
- [[MAT.9.34]]: Der SBLGNT-Apparat verzeichnet keine Variante; nach der CNTR-Transkription fehlt der Vers in 05. Das steht
  in decisions und translation_notes, nicht als Alternative.
- Die Begriffe folgen der gemeinsamen Matthäus-Tabelle (Reich der Himmel, Menschensohn, Amen ich sage euch, siehe/lueg,
  sogleich/grad, da/dänn, Erfüllungsformel); Parallelen bei Markus (TRANS-MRK-*) sind im Wortlaut abgestimmt, soweit das
  Griechische gleich ist.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1)
bzw. aus den CNTR-Transkriptionen (Sekundärtranskription), nicht aus eigener Prüfung der Handschriften.
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
CHAPTERS = ((8, 34), (9, 38))
TOOL = "scripts/authoring/matthaeus_text_08_09.py"

DE = {
 # ------------------------------------------------------------ Kapitel 8
 "MAT.8.1": "[Als er]{3} [aber]{2} [vom]{4,5} [Berg]{6} [herabgestiegen war]{1}, [folgten]{7} [ihm]{8} [grosse]{10} [Menschenmengen]{9}.",
 "MAT.8.2": "Und{1} [siehe]{2}, [ein Aussätziger]{3} [trat heran]{4}, [warf sich]{5} [vor ihm]{6} [nieder]{5} und [sagte]{7}: «[Herr]{8}, [wenn]{9} [du willst]{10}, [kannst du]{11} [mich]{12} [rein machen]{13}.»",
 "MAT.8.3": "Und{1} [er streckte]{2} [die Hand]{3,4} [aus]{2}, [berührte]{5} [ihn]{6} und [sagte]{7}: «[Ich will]{8}; [werde rein]{9}!» Und{10} [sogleich]{11} [wurde]{12} [er]{13} [von seinem Aussatz]{14,15} [rein]{12}.",
 "MAT.8.4": "Und{1} [Jesus]{4,5} [sagt]{2} [zu ihm]{3}: «[Sieh zu]{6}, [dass du]{8} es [niemandem]{7} [sagst]{8}; [sondern]{9} [geh]{10}, [zeig]{12} [dich]{11} [dem Priester]{13,14} und{15} [bring]{16} [die Gabe]{17,18} [dar]{16}, [die]{19} [Mose]{21} [angeordnet hat]{20}, [ihnen]{24} [zum]{22} [Zeugnis]{23}.»",
 "MAT.8.5": "[Als er]{3} [aber]{2} [nach]{4} [Kafarnaum]{5} [hineinkam]{1}, [trat]{6} [ein Hauptmann]{8} [zu ihm]{7} [heran]{6} und [bat]{9} [ihn]{10}",
 "MAT.8.6": "und{1} [sagte]{2}: «[Herr]{3}, [mein]{6} [Diener]{4,5} [liegt]{7} [gelähmt]{11} [im]{8,9} [Haus]{10} und [wird]{13} [schrecklich]{12} [gequält]{13}.»",
 "MAT.8.7": "Und{1} [er sagt]{2} [zu ihm]{3}: «[Ich]{4} [werde]{6} [kommen]{5} und [ihn]{7} [heilen]{6}.»",
 "MAT.8.8": "Und{1} [der Hauptmann]{3,4} [antwortete]{2} und [sagte]{5}: «[Herr]{6}, [ich bin]{8} [nicht]{7} [wert]{9}, [dass]{10} [du]{15} [unter]{12} [mein]{11} [Dach]{13,14} [kommst]{15}; [sondern]{16} [sprich]{18} [nur]{17} [ein Wort]{19}, und{20} [mein]{24} [Diener]{22,23} [wird gesund werden]{21}.",
 "MAT.8.9": "[Denn]{2} [auch]{1} [ich]{3} [bin]{5} [ein Mensch]{4} [unter]{6} [Befehlsgewalt]{7} und [habe]{8} [Soldaten]{11} [unter]{9} [mir]{10}; und{12} [ich sage]{13} [zu diesem]{14}: ‹[Geh]{15}!›, und{16} [er geht]{17}; und{18} [zu einem anderen]{19}: ‹[Komm]{20}!›, und{21} [er kommt]{22}; und{23} [zu meinem]{24,26} [Knecht]{25}: ‹[Tu]{27} [das]{28}!›, und{29} [er tut es]{30}.»",
 "MAT.8.10": "[Als]{1} [aber]{2} [Jesus]{3,4} das [hörte]{1}, [staunte er]{5} und{6} [sagte]{7} [zu denen, die]{8} [ihm folgten]{9}: «[Amen]{10}, [ich sage]{11} [euch]{12}: [Bei]{13} [niemandem]{14} [in]{17} [Israel]{18,19} [habe ich]{20} [einen so grossen]{15} [Glauben]{16} [gefunden]{20}.",
 "MAT.8.11": "[Ich sage]{1} [euch]{3} [aber]{2}: [Viele]{5} [werden]{10} [von]{6} [Osten]{7} und{8} [Westen]{9} [kommen]{10} und{11} [mit]{13} [Abraham]{14} und{15} [Isaak]{16} und{17} [Jakob]{18} [im]{19,20} [Reich]{21} [der Himmel]{22,23} [zu Tisch liegen]{12}; ~4(ὅτι leitet die Rede ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.8.12": "[die Söhne]{1,3} [des Reiches]{4,5} [aber]{2} [werden]{6} [in]{7} [die]{8,10} [äussere]{11} [Finsternis]{9} [hinausgeworfen werden]{6}; [dort]{12} [wird]{13} [das Weinen]{14,15} und{16} [das Zähneknirschen]{17-20} [sein]{13}.»",
 "MAT.8.13": "Und{1} [Jesus]{3,4} [sagte]{2} [zum Hauptmann]{5,6}: «[Geh]{7}! [Wie]{8} [du geglaubt hast]{9}, [soll]{10} [dir]{11} [geschehen]{10}.» Und{12} [in]{16} [jener]{17,19} [Stunde]{18} [wurde]{13} [der Diener]{14,15} [gesund]{13}.",
 "MAT.8.14": "Und{1} [als]{2} [Jesus]{3,4} [in]{5} [das]{6} [Haus]{7} [des Petrus]{8} [kam]{2}, [sah er]{9} [dessen]{12} [Schwiegermutter]{10,11} [mit Fieber]{15} [im Bett liegen]{13}. ~14(καί verbindet die beiden Partizipien; durch «mit» wiedergegeben)",
 "MAT.8.15": "Und{1} [er berührte]{2} [ihre]{5} [Hand]{3,4}, und{6} [das Fieber]{9,10} [verliess]{7} [sie]{8}; und{11} [sie stand auf]{12} und{13} [diente]{14} [ihm]{15}.",
 "MAT.8.16": "[Als]{3} [es aber]{2} [Abend]{1} [geworden war]{3}, [brachten sie]{4} [viele]{7} [Besessene]{6} [zu ihm]{5}; und{8} [er trieb]{9} [die Geister]{10,11} [mit einem Wort]{12} [aus]{9} und{13} [heilte]{18} [alle]{14}, [die]{15} [krank waren]{16,17},",
 "MAT.8.17": "[damit]{1} [erfüllt würde]{2}, [was]{3} [durch]{5} [den Propheten]{7,8} [Jesaja]{6} [gesagt ist]{4}: «[Er selbst]{10} [hat]{14} [unsere]{13} [Schwächen]{11,12} [genommen]{14} und{15} [die Krankheiten]{16,17} [getragen]{18}.» ~9(λέγοντος «sagend» leitet das Zitat ein)",
 "MAT.8.18": "[Als]{1} [aber]{2} [Jesus]{3,4} [die vielen]{5} [Menschenmengen]{6} [um]{7} [sich]{8} [sah]{1}, [befahl er]{9}, [ans]{11,12} [andere Ufer]{13} [aufzubrechen]{10}.",
 "MAT.8.19": "Und{1} [ein]{3} [Schriftgelehrter]{4} [trat heran]{2} und [sagte]{5} [zu ihm]{6}: «[Lehrer]{7}, [ich werde]{8} [dir]{9} [folgen]{8}, [wohin]{10} [du]{12} [auch]{11} [gehst]{12}.»",
 "MAT.8.20": "Und{1} [Jesus]{4,5} [sagt]{2} [zu ihm]{3}: «[Die Füchse]{6,7} [haben]{9} [Höhlen]{8}, und{10} [die Vögel]{11,12} [des Himmels]{13,14} [Nester]{15}; [der Menschensohn]{16,18-20} [aber]{17} [hat]{22} [keinen]{21} Ort, [wo]{23} [er]{26} [den Kopf]{24,25} [hinlegen kann]{26}.»",
 "MAT.8.21": "[Ein anderer]{1} [von den]{3} [Jüngern]{4} [aber]{2} [sagte]{5} [zu ihm]{6}: «[Herr]{7}, [erlaube]{8} [mir]{9}, [zuerst]{10} [wegzugehen]{11} und{12} [meinen]{16} [Vater]{14,15} [zu begraben]{13}.»",
 "MAT.8.22": "[Jesus]{1,3} [aber]{2} [sagt]{4} [zu ihm]{5}: «[Folge]{6} [mir]{7}, und{8} [lass]{9} [die Toten]{10,11} [ihre]{13,14} [Toten]{15} [begraben]{12}!»",
 "MAT.8.23": "Und{1} [als er]{3} [in]{4} [ein Boot]{5} [stieg]{2}, [folgten]{6} [ihm]{7} [seine]{10} [Jünger]{8,9}.",
 "MAT.8.24": "Und{1} [siehe]{2}, [es entstand]{5} [ein grosses]{4} [Beben]{3} [auf]{6} [dem See]{7,8}, [sodass]{9} [das Boot]{10,11} [von]{13} [den Wellen]{14,15} [bedeckt wurde]{12}; [er]{16} [aber]{17} [schlief]{18}.",
 "MAT.8.25": "Und{1} [sie traten heran]{2}, [weckten]{3} [ihn]{4} und [sagten]{5}: «[Herr]{6}, [rette]{7}! [Wir gehen zugrunde]{8}!»",
 "MAT.8.26": "Und{1} [er sagt]{2} [zu ihnen]{3}: «[Warum]{4} [seid ihr]{6} [so furchtsam]{5}, [ihr Kleingläubigen]{7}?» [Da]{8} [stand er auf]{9}, [fuhr]{10} [die Winde]{11,12} und{13} [den See]{14,15} [an]{10}, und{16} [es wurde]{17} [eine grosse]{19} [Stille]{18}.",
 "MAT.8.27": "[Die Menschen]{1,3} [aber]{2} [staunten]{4} und [sagten]{5}: «[Was für einer]{6} [ist]{7} [dieser]{8}, [dass]{9} [ihm]{16} [sogar]{10} [die Winde]{11,12} und{13} [der See]{14,15} [gehorchen]{17}?»",
 "MAT.8.28": "Und{1} [als er]{3} [ans]{4,5} [andere Ufer]{6} [in]{7} [das]{8} [Gebiet]{9} [der Gadarener]{10,11} [kam]{2}, [begegneten]{12} [ihm]{13} [zwei]{14} [Besessene]{15}, die [aus]{16} [den Grabstätten]{17,18} [herauskamen]{19}; sie waren [sehr]{21} [gefährlich]{20}, [sodass]{22} [niemand]{23,25} [auf]{27} [jenem]{28,30} [Weg]{29} [vorbeigehen]{26} [konnte]{24}.",
 "MAT.8.29": "Und{1} [siehe]{2}, [sie schrien]{3} und [sagten]{4}: «[Was haben wir mit dir zu tun]{5-8:idiom}, [Sohn]{9} [Gottes]{10,11}? [Bist du]{12} [hierher]{13} [gekommen]{12}, [um]{16} [uns]{17} [vor]{14} [der Zeit]{15} [zu quälen]{16}?»",
 "MAT.8.30": "[Es war]{1} [aber]{2} [weit weg]{3} [von]{4} [ihnen]{5} [eine Herde]{6} [vieler]{8} [Schweine]{7} [auf der Weide]{9}.",
 "MAT.8.31": "[Die Dämonen]{1,3} [aber]{2} [baten]{4} [ihn]{5} und [sagten]{6}: «[Wenn]{7} [du]{8} [uns]{9} [austreibst]{8}, [schick]{10} [uns]{11} [in]{12} [die Herde]{13,14} [der Schweine]{15,16}!»",
 "MAT.8.32": "Und{1} [er sagte]{2} [zu ihnen]{3}: «[Geht]{4}!» [Sie]{5} [aber]{6} [kamen heraus]{7} und [fuhren]{8} [in]{9} [die Schweine]{10,11}. Und{12} [siehe]{13}, [die ganze]{15,16} [Herde]{17} [stürmte]{14} [den Abhang]{19,20} [hinunter]{18} [in]{21} [den See]{22,23}, und{24} [sie starben]{25} [im]{26,27} [Wasser]{28}.",
 "MAT.8.33": "[Die Hirten]{1,3} [aber]{2} [flohen]{4}, und{5} [sie gingen]{6} [in]{7} [die Stadt]{8,9} und [berichteten]{10} [alles]{11}, [auch]{12} [das]{13} [mit den Besessenen]{14,15}.",
 "MAT.8.34": "Und{1} [siehe]{2}, [die ganze]{3,4} [Stadt]{5} [kam heraus]{6}, [Jesus]{9,10} [entgegen]{7,8}; und{11} [als sie]{12} [ihn]{13} [sahen]{12}, [baten sie]{14}, [dass]{15} [er]{16} [aus]{17} [ihrem]{20} [Gebiet]{18,19} [weggehe]{16}.",
 # ------------------------------------------------------------ Kapitel 9
 "MAT.9.1": "Und{1} [er stieg]{2} [in]{3} [ein Boot]{4}, [fuhr hinüber]{5} und{6} [kam]{7} [in]{8} [seine eigene]{9,10} [Stadt]{11}.",
 "MAT.9.2": "Und{1} [siehe]{2}, [sie brachten]{3} [zu ihm]{4} [einen Gelähmten]{5}, der [auf]{6} [einem Bett]{7} [lag]{8}. Und{9} [als]{10} [Jesus]{11,12} [ihren]{15} [Glauben]{13,14} [sah]{10}, [sagte er]{16} [zum Gelähmten]{17,18}: «[Sei getrost]{19}, [Kind]{20}! [Deine]{22} [Sünden]{23,24} [sind vergeben]{21}.»",
 "MAT.9.3": "Und{1} [siehe]{2}, [einige]{3} [von den]{4} [Schriftgelehrten]{5} [sagten]{6} [bei]{7} [sich]{8}: «[Der]{9} [lästert]{10}!»",
 "MAT.9.4": "Und{1} [Jesus]{3,4} [kannte]{2} [ihre]{7} [Gedanken]{5,6} und [sagte]{8}: «[Warum]{9} [denkt ihr]{10} [Böses]{11} [in]{12} [euren]{13,15} [Herzen]{14}?",
 "MAT.9.5": "[Was]{1} [ist]{3} [denn]{2} [leichter]{4}, [zu sagen]{5}: ‹[Deine]{7} [Sünden]{8,9} [sind vergeben]{6}›, [oder]{10} [zu sagen]{11}: ‹[Steh auf]{12} und{13} [geh umher]{14}›?",
 "MAT.9.6": "[Damit]{1} [ihr]{3} [aber]{2} [wisst]{3}, [dass]{4} [der Menschensohn]{7-10} [Vollmacht]{5} [hat]{6}, [auf]{11} [der Erde]{12,13} [Sünden]{15} [zu vergeben]{14}» – [da]{16} [sagt er]{17} [zum Gelähmten]{18,19}: «[Steh auf]{20}, [nimm]{21} [dein]{22} [Bett]{23,24} und{25} [geh]{26} [in]{27} [dein]{30} [Haus]{28,29}!»",
 "MAT.9.7": "Und{1} [er stand auf]{2} und [ging]{3} [in]{4} [sein]{7} [Haus]{5,6}.",
 "MAT.9.8": "[Als]{1} [aber]{2} [die Menschenmengen]{3,4} das [sahen]{1}, [fürchteten sie sich]{5} und{6} [priesen]{7} [Gott]{8,9}, [der]{10} [den Menschen]{14,15} [solche]{13} [Vollmacht]{12} [gegeben hat]{11}.",
 "MAT.9.9": "Und{1} [als]{2} [Jesus]{3,4} [von dort]{5} [weiterging]{2}, [sah er]{6} [einen Menschen]{7} [an]{9} [der]{10} [Zollstelle]{11} [sitzen]{8}, der [Matthäus]{12} [hiess]{13}, und{14} [er sagt]{15} [zu ihm]{16}: «[Folge]{17} [mir]{18}!» Und{19} [er stand auf]{20} und [folgte]{21} [ihm]{22}.",
 "MAT.9.10": "Und{1} [es geschah]{2}, [als er]{3} [im]{5,6} [Haus]{7} [zu Tisch lag]{4}, und{8} [siehe]{9}, [viele]{10} [Zöllner]{11} und{12} [Sünder]{13} [kamen]{14} und [lagen]{15} [mit Jesus]{16,17} und{18} [seinen]{19,21} [Jüngern]{20} [zu Tisch]{15}.",
 "MAT.9.11": "Und{1} [als]{2} [die Pharisäer]{3,4} das [sahen]{2}, [sagten sie]{5} [zu seinen]{6,8} [Jüngern]{7}: «[Warum]{9,10} [isst]{16} [euer]{19} [Lehrer]{17,18} [mit]{11} [den Zöllnern]{12,13} und{14} [Sündern]{15}?»",
 "MAT.9.12": "[Er]{1} [aber]{2} [hörte es]{3} und [sagte]{4}: «[Nicht]{5} [die Gesunden]{8,9} [brauchen]{6,7} [einen Arzt]{10}, [sondern]{11} [die Kranken]{12-14}.",
 "MAT.9.13": "[Geht]{1} [aber]{2} und [lernt]{3}, [was]{4} [das heisst]{5}: ‹[Barmherzigkeit]{6} [will ich]{7} und{8} [nicht]{9} [Opfer]{10}.› [Denn]{12} [ich bin]{13} [nicht]{11} [gekommen]{13}, [Gerechte]{15} [zu rufen]{14}, [sondern]{16} [Sünder]{17}.»",
 "MAT.9.14": "[Da]{1} [treten]{2} [die Jünger]{4,5} [des Johannes]{6} [zu ihm]{3} [heran]{2} und [sagen]{7}: «[Warum]{8,9} [fasten]{14} [wir]{10} und{11} [die Pharisäer]{12,13} [oft]{15}, [deine]{19} [Jünger]{16,18} [aber]{17} [fasten]{21} [nicht]{20}?»",
 "MAT.9.15": "Und{1} [Jesus]{4,5} [sagte]{2} [zu ihnen]{3}: «[Können]{7} [etwa]{6} [die Hochzeitsgäste]{8-11} [trauern]{12}, [solange]{13,14} [der Bräutigam]{18,19} [bei]{15} [ihnen]{16} [ist]{17}? [Es werden]{20} [aber]{21} [Tage]{22} [kommen]{20}, [wenn]{23} [der Bräutigam]{27,28} [von]{25} [ihnen]{26} [weggenommen wird]{24}, und{29} [dann]{30} [werden sie fasten]{31}.",
 "MAT.9.16": "[Niemand]{1} [aber]{2} [setzt]{3} [einen Flicken]{4} aus [ungewalktem]{6} [Stoff]{5} [auf]{7} [ein altes]{9} [Kleid]{8}; [denn]{11} [das Flickstück]{12-14} [reisst]{10} [vom]{15,16} [Kleid]{17} [ab]{10}, und{18} [der Riss]{20} [wird]{21} [schlimmer]{19}.",
 "MAT.9.17": "[Man füllt]{2} [auch nicht]{1} [jungen]{4} [Wein]{3} [in]{5} [alte]{7} [Schläuche]{6}; [sonst]{8-11} [reissen]{12} [die Schläuche]{13,14}, und{15} [der Wein]{16,17} [läuft aus]{18}, und{19} [die Schläuche]{20,21} [gehen verloren]{22}; [sondern]{23} [man füllt]{24} [jungen]{26} [Wein]{25} [in]{27} [neue]{29} [Schläuche]{28}, und{30} [beide]{31} [bleiben erhalten]{32}.»",
 "MAT.9.18": "[Während]{3} [er]{2} [das]{1} [zu ihnen]{4} [redete]{3}, [siehe]{5}, [da kam]{8} [ein]{7} [Vorsteher]{6}, [warf sich]{9} [vor ihm]{10} [nieder]{9} und [sagte]{11}: «[Meine]{15} [Tochter]{13,14} [ist]{17} [eben]{16} [gestorben]{17}; [aber]{18} [komm]{19}, [leg]{20} [deine]{23} [Hand]{21,22} [auf]{24} [sie]{25}, und{26} [sie wird leben]{27}.» ~12(ὅτι leitet die direkte Rede ein)",
 "MAT.9.19": "Und{1} [Jesus]{3,4} [stand auf]{2} und [folgte]{5} [ihm]{6}, und{7} auch [seine]{10} [Jünger]{8,9}.",
 "MAT.9.20": "Und{1} [siehe]{2}, [eine Frau]{3}, die [seit zwölf]{5} [Jahren]{6} [an Blutfluss litt]{4}, [trat]{7} [von hinten]{8} [heran]{7} und [berührte]{9} [den Saum]{10,11} [seines]{14} [Mantels]{12,13}.",
 "MAT.9.21": "[Denn]{2} [sie sagte]{1} [sich]{3,4}: «[Wenn]{5} [ich]{7} [nur]{6} [seinen]{10} [Mantel]{8,9} [berühre]{7}, [werde ich gerettet]{11}.»",
 "MAT.9.22": "[Jesus]{1,3} [aber]{2} [wandte sich um]{4}, und{5} [als er]{6} [sie]{7} [sah]{6}, [sagte er]{8}: «[Sei getrost]{9}, [Tochter]{10}! [Dein]{13} [Glaube]{11,12} [hat]{14} [dich]{15} [gerettet]{14}.» Und{16} [von]{20} [jener]{21,23} [Stunde]{22} [an]{20} [war]{17} [die Frau]{18,19} [gerettet]{17}.",
 "MAT.9.23": "Und{1} [als]{2} [Jesus]{3,4} [in]{5} [das]{6} [Haus]{7} [des Vorstehers]{8,9} [kam]{2} und{10} [die Flötenspieler]{12,13} und{14} [die]{15} [lärmende]{17} [Menge]{16} [sah]{11},",
 "MAT.9.24": "[sagte er]{1}: «[Geht weg]{2}! [Denn]{4} [das Mädchen]{6,7} [ist]{5} [nicht]{3} [gestorben]{5}, [sondern]{8} [es schläft]{9}.» Und{10} [sie lachten]{11} [ihn]{12} [aus]{11}.",
 "MAT.9.25": "[Als]{1} [aber]{2} [die Menge]{4,5} [hinausgetrieben war]{3}, [ging er hinein]{6}, [ergriff]{7} [ihre]{10} [Hand]{8,9}, und{11} [das Mädchen]{13,14} [stand auf]{12}.",
 "MAT.9.26": "Und{1} [diese]{5} [Kunde]{3,4} [verbreitete sich]{2} [in]{6} [jener]{8,10} [ganzen]{7} [Gegend]{9}.",
 "MAT.9.27": "Und{1} [als]{2} [Jesus]{4,5} [von dort]{3} [weiterging]{2}, [folgten]{6} [ihm]{7} [zwei]{8} [Blinde]{9}, [die schrien]{10} und{11} [sagten]{12}: «[Erbarme dich]{13} [unser]{14}, [Sohn]{15} [Davids]{16}!»",
 "MAT.9.28": "[Als er]{1} [aber]{2} [in]{3} [das]{4} [Haus]{5} [gekommen war]{1}, [traten]{6} [die Blinden]{8,9} [zu ihm]{7} [heran]{6}, und{10} [Jesus]{13,14} [sagt]{11} [zu ihnen]{12}: «[Glaubt ihr]{15}, [dass]{16} [ich]{17} [das]{18} [tun]{19} [kann]{17}?» [Sie sagen]{20} [zu ihm]{21}: «[Ja]{22}, [Herr]{23}.»",
 "MAT.9.29": "[Da]{1} [berührte er]{2} [ihre]{5} [Augen]{3,4} und [sagte]{6}: «[Nach]{7} [eurem]{8,10} [Glauben]{9} [soll]{11} [euch]{12} [geschehen]{11}.»",
 "MAT.9.30": "Und{1} [ihre]{3} [Augen]{4,5} [wurden geöffnet]{2}. Und{6} [Jesus]{9,10} [fuhr]{7} [sie]{8} [hart an]{7} und [sagte]{11}: «[Seht zu]{12}, dass [niemand]{13} [es erfährt]{14}!»",
 "MAT.9.31": "[Sie]{1} [aber]{2} [gingen hinaus]{3} und [machten]{4} [ihn]{5} [in]{6} [jener]{8,10} [ganzen]{7} [Gegend]{9} [bekannt]{4}.",
 "MAT.9.32": "[Als]{3} [sie]{1} [aber]{2} [hinausgingen]{3}, [siehe]{4}, [da brachte man]{5} [einen stummen]{8} [Menschen]{7} [zu ihm]{6}, [der besessen war]{9}.",
 "MAT.9.33": "Und{1} [als]{2} [der Dämon]{3,4} [ausgetrieben war]{2}, [redete]{5} [der Stumme]{6,7}. Und{8} [die Menschenmengen]{10,11} [staunten]{9} und [sagten]{12}: «[Noch nie]{13} [hat sich]{14} [so etwas]{15} [in]{16} [Israel]{17,18} [gezeigt]{14}!»",
 "MAT.9.34": "[Die Pharisäer]{1,3} [aber]{2} [sagten]{4}: «[Durch]{5} [den Herrscher]{6,7} [der Dämonen]{8,9} [treibt er]{10} [die Dämonen]{11,12} [aus]{10}.»",
 "MAT.9.35": "Und{1} [Jesus]{3,4} [zog]{2} [durch]{2} [alle]{7} [Städte]{5,6} und{8} [Dörfer]{9,10} [umher]{2}, [lehrte]{11} [in]{12} [ihren]{13,15} [Synagogen]{14} und{16} [verkündigte]{17} [das Evangelium]{18,19} [vom Reich]{20,21} und{22} [heilte]{23} [jede]{24} [Krankheit]{25} und{26} [jedes]{27} [Leiden]{28}.",
 "MAT.9.36": "[Als er]{1} [aber]{2} [die Menschenmengen]{3,4} [sah]{1}, [hatte er Erbarmen]{5} [mit]{6} [ihnen]{7}, [denn]{8} [sie waren]{9} [geschunden]{10} und{11} [hilflos]{12} [wie]{13} [Schafe]{14}, die [keinen]{15} [Hirten]{17} [haben]{16}.",
 "MAT.9.37": "[Da]{1} [sagt er]{2} [zu seinen]{3,5} [Jüngern]{4}: «[Die Ernte]{6,8} ist [zwar]{7} [gross]{9}, [die Arbeiter]{10,12} [aber]{11} sind [wenige]{13}.",
 "MAT.9.38": "[Bittet]{1} [also]{2} [den Herrn]{3,4} [der Ernte]{5,6}, [dass]{7} [er]{8} [Arbeiter]{9} [in]{10} [seine]{11,13} [Ernte]{12} [aussende]{8}.»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 8
 "MAT.8.1": "[Won er]{3} [aber]{2} [vom]{4,5} [Bärg]{6} [abegstige isch]{1}, [sind]{7} [ihm]{8} [vil]{10} [Lüüt]{9} [nachegange]{7}.",
 "MAT.8.2": "Und{1} [lueg]{2}, [en Ussätzige]{3} [isch härechoo]{4}, [hät sich]{5} [vor ihm]{6} [nidergworfe]{5} und [gseit]{7}: «[Herr]{8}, [wänn]{9} [du wottsch]{10}, [chasch du]{11} [mich]{12} [rein mache]{13}.»",
 "MAT.8.3": "Und{1} [er hät]{2} [d Hand]{3,4} [usgstreckt]{2}, [hät]{5} [en]{6} [aagrüert]{5} und [gseit]{7}: «[Ich wott]{8}; [wird rein]{9}!» Und{10} [grad]{11} [isch]{12} [er]{13} [vo sim Ussatz]{14,15} [rein worde]{12}.",
 "MAT.8.4": "Und{1} [de Jesus]{4,5} [seit]{2} [zu ihm]{3}: «[Pass uf]{6}, [dass du]{8} s [niemertem]{7} [seisch]{8}; [sondern]{9} [gang]{10}, [zeig]{12} [dich]{11} [em Prieschter]{13,14} und{15} [bring]{16} [d Gaab]{17,18} [dar]{16}, [wo]{19} [de Mose]{21} [aagordnet hät]{20}, [ine]{24} [zum]{22} [Zügnis]{23}.»",
 "MAT.8.5": "[Won er]{3} [aber]{2} [uf]{4} [Kafarnaum]{5} [inecho isch]{1}, [isch]{6} [en Hauptmaa]{8} [zu ihm]{7} [härechoo]{6} und [hät]{9} [en]{10} [bätte]{9}",
 "MAT.8.6": "und{1} [hät gseit]{2}: «[Herr]{3}, [min]{6} [Diener]{4,5} [liit]{7} [glähmt]{11} [im]{8,9} [Huus]{10} und [wird]{13} [schrecklich]{12} [plaget]{13}.»",
 "MAT.8.7": "Und{1} [er seit]{2} [zu ihm]{3}: «[Ich]{4} [chume]{5} und [heil]{6} [en]{7}.»",
 "MAT.8.8": "Und{1} [de Hauptmaa]{3,4} [hät gantwortet]{2} und [gseit]{5}: «[Herr]{6}, [ich bi]{8} [nöd]{7} [wärt]{9}, [dass]{10} [du]{15} [under]{12} [mis]{11} [Dach]{13,14} [chunnsch]{15}; [sondern]{16} [säg]{18} [nu]{17} [es Wort]{19}, und{20} [min]{24} [Diener]{22,23} [wird gsund]{21}.",
 "MAT.8.9": "[Dänn]{2} [au]{1} [ich]{3} [bi]{5} [en Mänsch]{4} [under]{6} [Befehlsgwalt]{7} und [han]{8} [Soldate]{11} [under]{9} [mir]{10}; und{12} [ich säg]{13} [zu däm]{14}: ‹[Gang]{15}!›, und{16} [er gaat]{17}; und{18} [zumene andere]{19}: ‹[Chumm]{20}!›, und{21} [er chunnt]{22}; und{23} [zu mim]{24,26} [Chnächt]{25}: ‹[Mach]{27} [das]{28}!›, und{29} [er machts]{30}.»",
 "MAT.8.10": "[Wo]{1} [aber]{2} [de Jesus]{3,4} das [ghört hät]{1}, [hät er gstuunt]{5} und{6} [zu dene, wo]{8} [ihm nachegange sind]{9}, [gseit]{7}: «[Amen]{10}, [ich säg]{11} [eu]{12}: [Bi]{13} [niemertem]{14} [in]{17} [Israel]{18,19} [han ich]{20} [eso en grosse]{15} [Glaube]{16} [gfunde]{20}.",
 "MAT.8.11": "[Ich säg]{1} [eu]{3} [aber]{2}: [Vili]{5} [wärded]{10} [vo]{6} [Oschte]{7} und{8} [Weschte]{9} [choo]{10} und{11} [mit]{13} [em Abraham]{14} und{15} [em Isaak]{16} und{17} [em Jakob]{18} [im]{19,20} [Riich]{21} [vo de Himel]{22,23} [am Tisch ligge]{12}; ~4(ὅτι leitet d Red ii; mit em Doppelpunkt widergää)",
 "MAT.8.12": "[d Söhn]{1,3} [vom Riich]{4,5} [aber]{2} [wärded]{6} [i]{7} [di]{8,10} [üsser]{11} [Fiischteri]{9} [usegworfe]{6}; [dört]{12} [wird]{13} [s Hüüle]{14,15} und{16} [s Zändchnirsche]{17-20} [sii]{13}.»",
 "MAT.8.13": "Und{1} [de Jesus]{3,4} [hät]{2} [zum Hauptmaa]{5,6} [gseit]{2}: «[Gang]{7}! [Wie]{8} [du glaubt häsch]{9}, [söll]{10} [dir]{11} [gscheh]{10}.» Und{12} [de Diener]{14,15} [isch]{13} [i]{16} [dere]{17,19} [Stund]{18} [gsund worde]{13}.",
 "MAT.8.14": "Und{1} [wo]{2} [de Jesus]{3,4} [is]{5,6} [Huus]{7} [vom Petrus]{8} [choo isch]{2}, [hät er]{9} [däm sini]{12} [Schwigermueter]{10,11} [mit Fieber]{15} [im Bett ligge]{13} [gseh]{9}. ~14(καί verbindet di beide Partizip; mit «mit» widergää)",
 "MAT.8.15": "Und{1} [er hät]{2} [ire]{5} [Hand]{3,4} [aagrüert]{2}, und{6} [s Fieber]{9,10} [hät]{7} [si]{8} [verlaa]{7}; und{11} [si isch ufgstande]{12} und{13} [hät]{14} [ihm]{15} [dienet]{14}.",
 "MAT.8.16": "[Won es]{3} [aber]{2} [Aabig]{1} [worde isch]{3}, [händ si]{4} [vil]{7} [Bsässne]{6} [zu ihm]{5} [bracht]{4}; und{8} [er hät]{9} [d Geischter]{10,11} [mit eme Wort]{12} [ustribe]{9} und{13} [hät]{18} [alli]{14} [gheilt]{18}, [wo]{15} [chrank gsii sind]{16,17},",
 "MAT.8.17": "[damit]{1} [erfüllt wird]{2}, [was]{3} [dur]{5} [de Prophet]{7,8} [Jesaja]{6} [gseit worden isch]{4}: «[Er sälber]{10} [hät]{14} [öisi]{13} [Schwäche]{11,12} [gnoo]{14} und{15} [d Chrankete]{16,17} [treit]{18}.» ~9(λέγοντος «sägend» leitet s Zitat ii)",
 "MAT.8.18": "[Wo]{1} [aber]{2} [de Jesus]{3,4} [di vile]{5} [Lüüt]{6} [um]{7} [sich]{8} [gseh hät]{1}, [hät er befole]{9}, [as]{11,12} [ander Ufer]{13} [ufzbreche]{10}.",
 "MAT.8.19": "Und{1} [en]{3} [Schriftgelehrte]{4} [isch härechoo]{2} und [hät]{5} [zu ihm]{6} [gseit]{5}: «[Lehrer]{7}, [ich gang]{8} [dir]{9} [nache]{8}, [wo]{10} [du]{12} [au]{11} [hiigaasch]{12}.»",
 "MAT.8.20": "Und{1} [de Jesus]{4,5} [seit]{2} [zu ihm]{3}: «[D Füchs]{6,7} [händ]{9} [Hööline]{8}, und{10} [d Vögel]{11,12} [vom Himel]{13,14} [Näschter]{15}; [de Mänschesohn]{16,18-20} [aber]{17} [hät]{22} [kein]{21} Ort, [wo]{23} [er]{26} [de Chopf]{24,25} [chan anelegge]{26}.»",
 "MAT.8.21": "[En andere]{1} [vo de]{3} [Jünger]{4} [aber]{2} [hät]{5} [zu ihm]{6} [gseit]{5}: «[Herr]{7}, [erlaub]{8} [mir]{9}, [zerscht]{10} [wägzgaa]{11} und{12} [min]{16} [Vatter]{14,15} [z beerdige]{13}.»",
 "MAT.8.22": "[De Jesus]{1,3} [aber]{2} [seit]{4} [zu ihm]{5}: «[Chumm]{6} [mir]{7} [nache]{6}, und{8} [la]{9} [d Tote]{10,11} [iri]{13,14} [Tote]{15} [beerdige]{12}!»",
 "MAT.8.23": "Und{1} [won er]{3} [in]{4} [es Boot]{5} [gstige isch]{2}, [sind]{6} [ihm]{7} [sini]{10} [Jünger]{8,9} [nachegange]{6}.",
 "MAT.8.24": "Und{1} [lueg]{2}, [es isch]{5} [es grosses]{4} [Bebe]{3} [uf]{6} [em See]{7,8} [choo]{5}, [so dass]{9} [s Boot]{10,11} [vo]{13} [de Wälle]{14,15} [zuedeckt worde isch]{12}; [er]{16} [aber]{17} [hät gschlafe]{18}.",
 "MAT.8.25": "Und{1} [si sind härechoo]{2}, [händ]{3} [en]{4} [gweckt]{3} und [gseit]{5}: «[Herr]{6}, [rett]{7}! [Mir gönd under]{8}!»",
 "MAT.8.26": "Und{1} [er seit]{2} [zu ine]{3}: «[Werum]{4} [sind er]{6} [so ängschtlich]{5}, [ir Chliigläubige]{7}?» [Dänn]{8} [isch er ufgstande]{9}, [hät]{10} [d Wind]{11,12} und{13} [de See]{14,15} [aagfahre]{10}, und{16} [es isch]{17} [ganz]{19} [still]{18} [worde]{17}.",
 "MAT.8.27": "[D Mänsche]{1,3} [aber]{2} [händ gstuunt]{4} und [gseit]{5}: «[Was]{6} [isch]{7} [dä]{8} [für eine]{6}, [dass]{9} [ihm]{16} [sogar]{10} [d Wind]{11,12} und{13} [de See]{14,15} [folged]{17}?»",
 "MAT.8.28": "Und{1} [won er]{3} [as]{4,5} [ander Ufer]{6} [is]{7,8} [Gebiet]{9} [vo de Gadarener]{10,11} [choo isch]{2}, [sind]{12} [ihm]{13} [zwei]{14} [Bsässne]{15} [entgägecho]{12}, wo [us]{16} [de Greber]{17,18} [usechoo sind]{19}; si sind [sehr]{21} [gföörlich]{20} gsii, [so dass]{22} [niemert]{23,25} [uf]{27} [däm]{28,30} [Wäg]{29} [hät chöne]{24} [verbiigaa]{26}.",
 "MAT.8.29": "Und{1} [lueg]{2}, [si händ gschroue]{3} und [gseit]{4}: «[Was händ mir mit dir z tue]{5-8:idiom}, [Sohn]{9} [vo Gott]{10,11}? [Bisch]{12} [da ane]{13} [choo]{12}, [für]{16} [üs]{17} [vor]{14} [de Ziit]{15} [z quäle]{16}?»",
 "MAT.8.30": "[Es isch]{1} [aber]{2} [wiit wäg]{3} [vo]{4} [ine]{5} [e Herde]{6} [vo vile]{8} [Söi]{7} [am Weide]{9} [gsii]{1}.",
 "MAT.8.31": "[D Dämone]{1,3} [aber]{2} [händ]{4} [en]{5} [bätte]{4} und [gseit]{6}: «[Wänn]{7} [du]{8} [üs]{9} [ustriibsch]{8}, [schick]{10} [üs]{11} [i]{12} [d Herde]{13,14} [vo de Söi]{15,16}!»",
 "MAT.8.32": "Und{1} [er hät]{2} [zu ine]{3} [gseit]{2}: «[Gönd]{4}!» [Si]{5} [aber]{6} [sind usecho]{7} und [sind]{8} [i]{9} [d Söi]{10,11} [gfahre]{8}. Und{12} [lueg]{13}, [di ganz]{15,16} [Herde]{17} [isch]{14} [de Abhang]{19,20} [abe]{18} [i]{21} [de See]{22,23} [gstürmt]{14}, und{24} [si sind]{25} [im]{26,27} [Wasser]{28} [gstorbe]{25}.",
 "MAT.8.33": "[D Hirte]{1,3} [aber]{2} [sind devogrännt]{4}, und{5} [si sind]{6} [i]{7} [d Stadt]{8,9} [gange]{6} und [händ]{10} [alles]{11} [verzellt]{10}, [au]{12} [das]{13} [mit de Bsässne]{14,15}.",
 "MAT.8.34": "Und{1} [lueg]{2}, [di ganz]{3,4} [Stadt]{5} [isch]{6} [em Jesus]{9,10} [entgäge]{7,8} [usecho]{6}; und{11} [wo si]{12} [en]{13} [gseh händ]{12}, [händ si bätte]{14}, [dass]{15} [er]{16} [us]{17} [irem]{20} [Gebiet]{18,19} [wäggang]{16}.",
 # ------------------------------------------------------------ Kapitel 9
 "MAT.9.1": "Und{1} [er isch]{2} [in]{3} [es Boot]{4} [gstige]{2}, [isch übere gfahre]{5} und{6} [isch]{7} [i]{8} [sini eiget]{9,10} [Stadt]{11} [choo]{7}.",
 "MAT.9.2": "Und{1} [lueg]{2}, [si händ]{3} [en Glähmte]{5} [zu ihm]{4} [bracht]{3}, wo [uf]{6} [eme Bett]{7} [gläge isch]{8}. Und{9} [wo]{10} [de Jesus]{11,12} [ire]{15} [Glaube]{13,14} [gseh hät]{10}, [hät er]{16} [zum Glähmte]{17,18} [gseit]{16}: «[Häb Muet]{19}, [Chind]{20}! [Dini]{22} [Sünde]{23,24} [sind vergää]{21}.»",
 "MAT.9.3": "Und{1} [lueg]{2}, [es paar]{3} [vo de]{4} [Schriftgelehrte]{5} [händ]{6} [bi]{7} [sich]{8} [gseit]{6}: «[Dä]{9} [läschteret]{10}!»",
 "MAT.9.4": "Und{1} [de Jesus]{3,4} [hät]{2} [iri]{7} [Gedanke]{5,6} [kännt]{2} und [gseit]{8}: «[Werum]{9} [dänked ir]{10} [Bööses]{11} [i]{12} [eune]{13,15} [Härze]{14}?",
 "MAT.9.5": "[Was]{1} [isch]{3} [dänn]{2} [liechter]{4}, [z säge]{5}: ‹[Dini]{7} [Sünde]{8,9} [sind vergää]{6}›, [oder]{10} [z säge]{11}: ‹[Stand uf]{12} und{13} [lauf umenand]{14}›?",
 "MAT.9.6": "[Damit]{1} [ir]{3} [aber]{2} [wüssed]{3}, [dass]{4} [de Mänschesohn]{7-10} [Vollmacht]{5} [hät]{6}, [uf]{11} [de Ärde]{12,13} [Sünde]{15} [z vergää]{14}» – [dänn]{16} [seit er]{17} [zum Glähmte]{18,19}: «[Stand uf]{20}, [nimm]{21} [dis]{22} [Bett]{23,24} und{25} [gang]{26} [hei]{27-30}!»",
 "MAT.9.7": "Und{1} [er isch ufgstande]{2} und [isch]{3} [hei]{4-7} [gange]{3}.",
 "MAT.9.8": "[Wo]{1} [aber]{2} [d Lüüt]{3,4} das [gseh händ]{1}, [händ si Angscht übercho]{5} und{6} [händ]{7} [Gott]{8,9} [priise]{7}, [wo]{10} [de Mänsche]{14,15} [so e]{13} [Vollmacht]{12} [gää hät]{11}.",
 "MAT.9.9": "Und{1} [wo]{2} [de Jesus]{3,4} [vo dört]{5} [wiitergange isch]{2}, [hät er]{6} [en Mänsch]{7} [a]{9} [de]{10} [Zollstell]{11} [hocke]{8} [gseh]{6}, wo [Matthäus]{12} [gheisse hät]{13}, und{14} [er seit]{15} [zu ihm]{16}: «[Chumm]{17} [mir]{18} [nache]{17}!» Und{19} [er isch ufgstande]{20} und [isch]{21} [ihm]{22} [nachegange]{21}.",
 "MAT.9.10": "Und{1} [es isch passiert]{2}, [won er]{3} [im]{5,6} [Huus]{7} [am Tisch gläge isch]{4}, und{8} [lueg]{9}, [vil]{10} [Zöllner]{11} und{12} [Sünder]{13} [sind choo]{14} und [sind]{15} [mit em Jesus]{16,17} und{18} [sine]{19,21} [Jünger]{20} [am Tisch gläge]{15}.",
 "MAT.9.11": "Und{1} [wo]{2} [d Pharisäer]{3,4} das [gseh händ]{2}, [händ si]{5} [zu sine]{6,8} [Jünger]{7} [gseit]{5}: «[Werum]{9,10} [isst]{16} [eue]{19} [Lehrer]{17,18} [mit]{11} [de Zöllner]{12,13} und{14} [Sünder]{15}?»",
 "MAT.9.12": "[Er]{1} [aber]{2} [hät s ghört]{3} und [gseit]{4}: «[Nöd]{5} [di Gsunde]{8,9} [bruuched]{6,7} [en Dokter]{10}, [sondern]{11} [di Chranke]{12-14}.",
 "MAT.9.13": "[Gönd]{1} [aber]{2} und [lerned]{3}, [was]{4} [das heisst]{5}: ‹[Barmhärzigkeit]{6} [wott ich]{7} und{8} [nöd]{9} [Opfer]{10}.› [Dänn]{12} [ich bi]{13} [nöd]{11} [choo]{13}, [für]{14} [Grächti]{15} [z rüefe]{14}, [sondern]{16} [Sünder]{17}.»",
 "MAT.9.14": "[Dänn]{1} [chömed]{2} [d Jünger]{4,5} [vom Johannes]{6} [zu ihm]{3} [häre]{2} und [säged]{7}: «[Werum]{8,9} [faschted]{14} [mir]{10} und{11} [d Pharisäer]{12,13} [vil]{15}, [dini]{19} [Jünger]{16,18} [aber]{17} [faschted]{21} [nöd]{20}?»",
 "MAT.9.15": "Und{1} [de Jesus]{4,5} [hät]{2} [zu ine]{3} [gseit]{2}: «[Chönd]{7} [d Hochziitsgäscht]{8-11} [öppe]{6} [truure]{12}, [solang]{13,14} [de Brüütigam]{18,19} [bi]{15} [ine]{16} [isch]{17}? [Es chömed]{20} [aber]{21} [Täg]{22}, [wo]{23} [de Brüütigam]{27,28} [vo]{25} [ine]{26} [weggnoo wird]{24}, und{29} [dänn]{30} [wärded si faschte]{31}.",
 "MAT.9.16": "[Niemert]{1} [aber]{2} [setzt]{3} [en Blätz]{4} vo [nöd iiglaufnem]{6} [Tuech]{5} [uf]{7} [es alts]{9} [Chleid]{8}; [dänn]{11} [de Blätz]{12-14} [riisst]{10} [vom]{15,16} [Chleid]{17} [ab]{10}, und{18} [de Riss]{20} [wird]{21} [schlimmer]{19}.",
 "MAT.9.17": "[Me tuet]{2} [au nöd]{1} [nöie]{4} [Wii]{3} [i]{5} [alti]{7} [Schlüüch]{6}; [suscht]{8-11} [platzed]{12} [d Schlüüch]{13,14}, und{15} [de Wii]{16,17} [lauft us]{18}, und{19} [d Schlüüch]{20,21} [sind verlore]{22}; [sondern]{23} [me tuet]{24} [nöie]{26} [Wii]{25} [i]{27} [nöii]{29} [Schlüüch]{28}, und{30} [beidi]{31} [bliibed erhalte]{32}.»",
 "MAT.9.18": "[Wäred er]{2} [das]{1} [zu ine]{4} [gredt hät]{3}, [lueg]{5}, [da isch]{8} [en]{7} [Vorsteher]{6} [choo]{8}, [hät sich]{9} [vor ihm]{10} [nidergworfe]{9} und [gseit]{11}: «[Mini]{15} [Tochter]{13,14} [isch]{17} [äbe]{16} [gstorbe]{17}; [aber]{18} [chumm]{19}, [leg]{20} [dini]{23} [Hand]{21,22} [uf]{24} [si]{25}, und{26} [si wird läbe]{27}.» ~12(ὅτι leitet di diräkt Red ii)",
 "MAT.9.19": "Und{1} [de Jesus]{3,4} [isch ufgstande]{2} und [isch]{5} [ihm]{6} [nachegange]{5}, und{7} [sini]{10} [Jünger]{8,9} au.",
 "MAT.9.20": "Und{1} [lueg]{2}, [e Frau]{3}, wo [sit zwölf]{5} [Jahr]{6} [a Bluetfluss liidet]{4}, [isch]{7} [vo hine]{8} [härechoo]{7} und [hät]{9} [de Saum]{10,11} [vo sim]{14} [Mantel]{12,13} [aagrüert]{9}.",
 "MAT.9.21": "[Si hät]{1} [nämli]{2} [bi sich]{3,4} [gseit]{1}: «[Wänn]{5} [ich]{7} [nu]{6} [sin]{10} [Mantel]{8,9} [aarüere]{7}, [wird ich grettet]{11}.»",
 "MAT.9.22": "[De Jesus]{1,3} [aber]{2} [hät sich umdräit]{4}, und{5} [won er]{6} [si]{7} [gseh hät]{6}, [hät er gseit]{8}: «[Häb Muet]{9}, [Tochter]{10}! [Din]{13} [Glaube]{11,12} [hät]{14} [dich]{15} [grettet]{14}.» Und{16} [vo]{20} [dere]{21,23} [Stund]{22} [aa]{20} [isch]{17} [d Frau]{18,19} [grettet gsii]{17}.",
 "MAT.9.23": "Und{1} [wo]{2} [de Jesus]{3,4} [is]{5,6} [Huus]{7} [vom Vorsteher]{8,9} [choo isch]{2} und{10} [d Flöötespiler]{12,13} und{14} [d]{15} [Mängi]{16}, [wo Lärm gmacht hät]{17}, [gseh hät]{11},",
 "MAT.9.24": "[hät er gseit]{1}: «[Gönd wäg]{2}! [S Meitli]{6,7} [isch]{5} [nämli]{4} [nöd]{3} [gstorbe]{5}, [sondern]{8} [es schlaft]{9}.» Und{10} [si händ]{11} [en]{12} [usglachet]{11}.",
 "MAT.9.25": "[Wo]{1} [aber]{2} [d Mängi]{4,5} [usegschickt gsii isch]{3}, [isch er inegange]{6}, [hät]{7} [ire]{10} [Hand]{8,9} [packt]{7}, und{11} [s Meitli]{13,14} [isch ufgstande]{12}.",
 "MAT.9.26": "Und{1} [die]{5} [Nachricht]{3,4} [hät sich]{2} [i]{6} [dere]{8,10} [ganze]{7} [Gegend]{9} [verbreitet]{2}.",
 "MAT.9.27": "Und{1} [wo]{2} [de Jesus]{4,5} [vo dört]{3} [wiitergange isch]{2}, [sind]{6} [ihm]{7} [zwei]{8} [Blindi]{9} [nachegange]{6}, [wo gschroue]{10} und{11} [gseit händ]{12}: «[Häb Erbarme]{13} [mit üs]{14}, [Sohn]{15} [vo David]{16}!»",
 "MAT.9.28": "[Won er]{1} [aber]{2} [is]{3,4} [Huus]{5} [choo isch]{1}, [sind]{6} [d Blinde]{8,9} [zu ihm]{7} [härechoo]{6}, und{10} [de Jesus]{13,14} [seit]{11} [zu ine]{12}: «[Glaubed ir]{15}, [dass]{16} [ich]{17} [das]{18} [cha]{17} [mache]{19}?» [Si säged]{20} [zu ihm]{21}: «[Ja]{22}, [Herr]{23}.»",
 "MAT.9.29": "[Dänn]{1} [hät er]{2} [iri]{5} [Auge]{3,4} [aagrüert]{2} und [gseit]{6}: «[Nach]{7} [eurem]{8,10} [Glaube]{9} [söll]{11} [eu]{12} [gscheh]{11}.»",
 "MAT.9.30": "Und{1} [iri]{3} [Auge]{4,5} [sind ufgange]{2}. Und{6} [de Jesus]{9,10} [hät]{7} [si]{8} [hert aagschnauzt]{7} und [gseit]{11}: «[Passed uf]{12}, dass [niemert]{13} [s erfahrt]{14}!»",
 "MAT.9.31": "[Si]{1} [aber]{2} [sind usegange]{3} und [händ]{4} [en]{5} [i]{6} [dere]{8,10} [ganze]{7} [Gegend]{9} [bekannt gmacht]{4}.",
 "MAT.9.32": "[Wo]{3} [si]{1} [aber]{2} [usegange sind]{3}, [lueg]{4}, [hät me]{5} [en stumme]{8} [Mänsch]{7} [zu ihm]{6} [bracht]{5}, [wo bsässe gsii isch]{9}.",
 "MAT.9.33": "Und{1} [wo]{2} [de Dämon]{3,4} [ustribe gsii isch]{2}, [hät]{5} [de Stumm]{6,7} [gredt]{5}. Und{8} [d Lüüt]{10,11} [händ gstuunt]{9} und [gseit]{12}: «[No nie]{13} [hät me]{14} [so öppis]{15} [in]{16} [Israel]{17,18} [gseh]{14}!»",
 "MAT.9.34": "[D Pharisäer]{1,3} [aber]{2} [händ gseit]{4}: «[Dur]{5} [de Herrscher]{6,7} [vo de Dämone]{8,9} [tribt er]{10} [d Dämone]{11,12} [us]{10}.»",
 "MAT.9.35": "Und{1} [de Jesus]{3,4} [isch]{2} [dur]{2} [alli]{7} [Stedt]{5,6} und{8} [Dörfer]{9,10} [zoge]{2}, [hät]{11} [i]{12} [irne]{13,15} [Synagoge]{14} [glehrt]{11} und{16} [hät]{17} [s Evangelium]{18,19} [vom Riich]{20,21} [verchündet]{17} und{22} [hät]{23} [jedi]{24} [Chranket]{25} und{26} [jedes]{27} [Liide]{28} [gheilt]{23}.",
 "MAT.9.36": "[Won er]{1} [aber]{2} [d Lüüt]{3,4} [gseh hät]{1}, [hät er Erbarme]{5} [mit]{6} [ine]{7} [gha]{5}, [wil]{8} [si]{9} [gschunde]{10} und{11} [hilflos]{12} [gsii sind]{9} [wie]{13} [Schaf]{14}, wo [kein]{15} [Hirt]{17} [händ]{16}.",
 "MAT.9.37": "[Dänn]{1} [seit er]{2} [zu sine]{3,5} [Jünger]{4}: «[D Ärn]{6,8} isch [zwar]{7} [gross]{9}, [d Arbeiter]{10,12} [aber]{11} sind [wenig]{13}.",
 "MAT.9.38": "[Bitted]{1} [also]{2} [de Herr]{3,4} [vo de Ärn]{5,6}, [dass]{7} [er]{8} [Arbeiter]{9} [i]{10} [sini]{11,13} [Ärn]{12} [usschickt]{8}.»",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MAT.8.1", "grosse Menschenmengen", "adapted", "ὄχλοι πολλοί", "viele Mengen", ["viele Leute", "grosse Scharen"],
  "Gemeinsame Matthäus-Wiedergabe: ὄχλος in der Einzahl «die Menge» ([[MAT.9.23]], [[MAT.9.25]]), in der Mehrzahl ὄχλοι «die Menschenmengen» ([[MAT.8.18]], [[MAT.9.8]], [[MAT.9.33]], [[MAT.9.36]]). Matthäus braucht die Mehrzahl auffallend oft. πολλοί ist hier mit «grosse» wiedergegeben, weil «viele Menschenmengen» im Deutschen ungewohnt klingt."),
 ("MAT.8.2", "Aussätziger", "traditional", "λεπρὸς", None, ["Hautkranker", "an Aussatz Leidender"],
  "λέπρα bezeichnet in der Bibel verschiedene Hautkrankheiten, die nach [[LEV.13.1]]–[[LEV.13.46]] unrein machten und vom Zusammenleben ausschlossen; gemeint ist nicht nur die heutige Lepra. Darum «rein machen» (καθαρίζω) statt «heilen», und der Geheilte soll sich nach [[LEV.14.2]]–[[LEV.14.32]] dem Priester zeigen ([[MAT.8.4]]). Wortlaut wie bei Markus ([[MRK.1.40]])."),
 ("MAT.8.2", "warf sich", "literal", "προσεκύνει", None, ["huldigte ihm", "betete ihn an", "fiel vor ihm nieder"],
  "Gemeinsame Matthäus-Wiedergabe: προσκυνέω vor Menschen und vor Jesus «sich (vor ihm) niederwerfen», mit Gott als Empfänger «anbeten»; so auch [[MAT.9.18]]. Die Gebärde kann einem König, einem Höhergestellten oder Gott gelten; ob die Bittenden hier Jesus anbeten oder ihm Ehrerbietung erweisen, sagt der Text nicht. Die Übersetzung beschreibt die Gebärde und lässt die Deutung offen."),
 ("MAT.8.2", "Herr", "literal", "Κύριε", None, ["Meister"],
  "κύριε ist als Anrede höflich («Herr») und kann zugleich mehr bedeuten, weil κύριος in der griechischen Bibel für den Gottesnamen steht. Durchgehend «Herr», ohne zu entscheiden, wie viel die Sprechenden meinen ([[MAT.8.6]], [[MAT.8.8]], [[MAT.8.21]], [[MAT.8.25]], [[MAT.9.28]]). Anrede διδάσκαλε dagegen «Lehrer» ([[MAT.8.19]])."),
 ("MAT.8.3", "wurde er von seinem Aussatz rein", "adapted", "ἐκαθαρίσθη αὐτοῦ ἡ λέπρα", "wurde sein Aussatz gereinigt", ["wich der Aussatz von ihm"],
  "Griechisch wird der Aussatz «gereinigt»; das Deutsche sagt vom Menschen, dass er rein wird. Die Wiederaufnahme von «rein» aus der Bitte bleibt erhalten."),
 ("MAT.8.4", "ihnen zum Zeugnis", "interpretive", "εἰς μαρτύριον αὐτοῖς", None, ["als Beweis für sie", "als Zeugnis gegen sie"],
  "Wer «ihnen» ist, bleibt offen: die Priester, das Volk oder allgemein die Leute. Ebenso kann gemeint sein, dass die Gabe die Heilung bestätigt, oder dass sie ein Zeugnis über Jesus ist. Gleiche Wendung in [[MRK.1.44]] und [[MAT.10.18]]."),
 ("MAT.8.5", "Hauptmann", "traditional", "ἑκατόνταρχος", "Befehlshaber über hundert", ["Zenturio", "Offizier"],
  "Ein Offizier mit rund hundert Mann, in Kafarnaum wohl im Dienst des Herodes Antipas; dass er Nichtjude ist, ergibt sich aus [[MAT.8.10]]–[[MAT.8.11]]. «Hauptmann» ist die vertraute Wiedergabe (vgl. [[MRK.15.39]] für κεντυρίων)."),
 ("MAT.8.6", "Diener", "interpretive", "παῖς", "Knabe", ["Junge", "Kind", "Sohn", "Bursche"],
  "παῖς heisst «Kind, Junge» und ebenso «Diener». Die Parallele [[LUK.7.2]] nennt ihn δοῦλος («Knecht»), [[JHN.4.46]] erzählt von einem Sohn. In [[MAT.8.9]] spricht der Hauptmann von seinem δοῦλος; ob dieser derselbe ist, bleibt offen. «Diener» folgt dem Lukas-Bericht; «Sohn» ist ebenfalls vertretbar."),
 ("MAT.8.7", "Ich werde kommen und ihn heilen", "interpretive", "Ἐγὼ ἐλθὼν θεραπεύσω αὐτόν", None, ["Soll ich etwa kommen und ihn heilen?", "Ich will kommen und ihn heilen."],
  "Ohne Satzzeichen kann der Satz Zusage oder (mit betontem ἐγώ) erstaunte Frage sein: Soll ich, ein Jude, in das Haus eines Nichtjuden kommen? Die Frage würde die Antwort des Hauptmanns ([[MAT.8.8]]) gut vorbereiten. Die Übersetzung wählt die Aussage wie die meisten Ausgaben; die Frage ist eine ernsthafte Alternative."),
 ("MAT.8.7", "heilen", "literal", "θεραπεύσω", None, ["gesund machen"],
  "Wiedergabe für Matthäus: θεραπεύω «heilen» ([[MAT.8.16]], [[MAT.9.35]]), ἰάομαι «gesund werden» ([[MAT.8.8]], [[MAT.8.13]]), damit die beiden Verben unterscheidbar bleiben. σῴζω ist «retten» ([[MAT.8.25]], [[MAT.9.21]]–[[MAT.9.22]])."),
 ("MAT.8.8", "wert", "literal", "ἱκανὸς", "genügend, tauglich", ["würdig"], None),
 ("MAT.8.9", "Befehlsgewalt", "adapted", "ἐξουσίαν", "Vollmacht", ["Autorität", "Befehl"],
  "ἐξουσία ist sonst «Vollmacht» ([[MAT.7.29]], [[MAT.9.6]], [[MAT.9.8]]). Hier spricht der Hauptmann von der militärischen Befehlskette, in der er selbst steht; «unter Befehlsgewalt» macht das deutlich. Er vergleicht damit Jesu Wort mit einem Befehl, der ausgeführt wird."),
 ("MAT.8.10", "Glauben", "literal", "πίστιν", None, ["Vertrauen"],
  "Wiedergabe für Matthäus: πίστις «Glaube», πιστεύω «glauben» ([[MAT.8.13]], [[MAT.9.2]], [[MAT.9.22]], [[MAT.9.28]]–[[MAT.9.29]]). In den Heilungsgeschichten meint das Wort vor allem das Vertrauen, dass Jesus helfen kann; «Vertrauen» wäre an diesen Stellen ebenfalls treffend, würde aber den Zusammenhang mit dem übrigen Gebrauch verdecken."),
 ("MAT.8.11", "zu Tisch liegen", "literal", "ἀνακλιθήσονται", None, ["zu Tisch sitzen", "am Festmahl teilnehmen"],
  "Beim festlichen Mahl lag man auf Polstern zu Tisch. Das Bild vom Mahl mit den Erzvätern greift die Erwartung eines endzeitlichen Festmahls auf (vgl. [[ISA.25.6]]). Ebenso ἀνάκειμαι in [[MAT.9.10]]."),
 ("MAT.8.11", "Reich der Himmel", "literal", "βασιλείᾳ τῶν οὐρανῶν", None, ["Himmelreich", "Reich Gottes"],
  "Gemeinsame Matthäus-Wiedergabe: «das Reich der Himmel». Matthäus sagt meist «der Himmel» (Mehrzahl, nach hebräischem Sprachgebrauch), wo Markus «Gottes» hat; viele sehen darin eine jüdische Umschreibung des Gottesnamens."),
 ("MAT.8.12", "die Söhne des Reiches", "literal", "υἱοὶ τῆς βασιλείας", None, ["die Erben des Reiches", "die für das Reich Bestimmten"],
  "Die semitische Wendung «Söhne von» bezeichnet Zugehörigkeit. Gemeint sind im Zusammenhang die, die nach ihrer Herkunft als Erben gelten; die Wendung steht der Aussage über die Vielen aus Osten und Westen gegenüber. Sie ist nicht pauschal auf ein Volk zu übertragen; in [[MAT.13.38]] bezeichnet dieselbe Wendung die Gerechten."),
 ("MAT.8.12", "das Zähneknirschen", "literal", "ὁ βρυγμὸς τῶν ὀδόντων", "das Knirschen der Zähne", ["das Zähneklappern"],
  "Gebärde der Wut oder Verzweiflung (vgl. [[PSA.112.10]]). Die Wendung «das Weinen und das Zähneknirschen» kehrt bei Matthäus mehrfach wieder ([[MAT.13.42]], [[MAT.13.50]], [[MAT.22.13]], [[MAT.24.51]], [[MAT.25.30]]) und ist überall gleich übersetzt (gemeinsame Matthäus-Wiedergabe)."),
 ("MAT.8.13", "wurde der Diener gesund", "literal", "ἰάθη", None, ["wurde der Diener geheilt"], None),
 ("MAT.8.15", "diente ihm", "literal", "διηκόνει αὐτῷ", None, ["bewirtete ihn", "sorgte für ihn"],
  "διακονέω meint hier das Bewirten und Versorgen der Gäste. Bei Matthäus steht die Einzahl «ihm» (Jesus), in [[MRK.1.31]] «ihnen»."),
 ("MAT.8.16", "die Geister", "literal", "τὰ πνεύματα", None, ["die bösen Geister"],
  "Matthäus sagt hier nur «die Geister»; aus dem Zusammenhang (Besessene, austreiben) sind böse Geister gemeint, vgl. [[MAT.10.1]] «unreine Geister». Die Übersetzung ergänzt nichts."),
 ("MAT.8.17", "damit erfüllt würde", "literal", "ὅπως πληρωθῇ", None, ["so sollte sich erfüllen"],
  "Erste Erfüllungsformel dieses Bereichs, gemeinsam für Matthäus «damit erfüllt würde, was … durch den Propheten gesagt ist». Das Zitat ist [[ISA.53.4]]; sein Wortlaut entspricht dem hebräischen Text («unsere Krankheiten trug er, unsere Schmerzen lud er auf sich»), nicht der Septuaginta, die von Sünden spricht. Matthäus bezieht den Vers auf die Heilungen."),
 ("MAT.8.17", "Schwächen", "literal", "ἀσθενείας", None, ["Gebrechen", "Krankheiten"],
  "ἀσθένεια heisst «Schwäche», oft im Sinn von Krankheit; neben νόσος «Krankheit» ist «Schwächen» gewählt, damit die beiden Wörter verschieden bleiben."),
 ("MAT.8.18", "ans andere Ufer", "adapted", "εἰς τὸ πέραν", "auf die andere Seite", None,
  "τὸ πέραν «das Jenseitige» meint das Ostufer des Sees; wie [[MRK.4.35]] «ans andere Ufer»."),
 ("MAT.8.19", "ich werde dir folgen", "literal", "ἀκολουθήσω σοι", None, ["ich will dir folgen", "ich will dir nachfolgen"],
  "Wiedergabe für Matthäus: ἀκολουθέω «folgen». Das Wort meint sowohl das Hinterhergehen der Menge ([[MAT.8.1]]) als auch die Jüngerschaft ([[MAT.8.22]], [[MAT.9.9]]); «nachfolgen» würde den zweiten Sinn festlegen."),
 ("MAT.8.20", "der Menschensohn", "literal", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", ["der Mensch"],
  "Erstes Vorkommen bei Matthäus; gemeinsame Wiedergabe «der Menschensohn» wie bei Markus und Johannes. Jesus spricht so von sich. Die Wendung kann im Aramäischen einfach «der Mensch» oder «einer» bedeuten und klingt zugleich an [[DAN.7.13]] an. Hier steht sie für Jesu heimatloses Unterwegssein."),
 ("MAT.8.20", "Nester", "adapted", "κατασκηνώσεις", "Wohnstätten, Lagerplätze", ["Nistplätze", "Unterschlupf"], None),
 ("MAT.8.22", "lass die Toten ihre Toten begraben", "literal", "ἄφες τοὺς νεκροὺς θάψαι τοὺς ἑαυτῶν νεκρούς", None, None,
  "Das harte Wort ist wörtlich belassen. Gedeutet wird es verschieden: Die ersten «Toten» seien geistlich Tote, die Jesus nicht folgen; oder es sei eine zugespitzte Redeweise, die den Vorrang der Nachfolge vor der heiligen Pflicht der Bestattung betont. Die Übersetzung entscheidet nicht."),
 ("MAT.8.24", "Beben", "literal", "σεισμὸς", "Erschütterung", ["Sturm", "Unwetter", "Seebeben"],
  "σεισμός heisst «Erschütterung, Beben» und steht bei Matthäus sonst für Erdbeben ([[MAT.24.7]], [[MAT.27.54]], [[MAT.28.2]]). [[MRK.4.37]] hat λαῖλαψ «Sturmwind». Gemeint ist wohl ein heftiges Unwetter auf dem See; das ungewöhnliche Wort ist erhalten, weil es einen Zusammenhang zu den Endzeit- und Osterberichten herstellen kann."),
 ("MAT.8.24", "See", "adapted", "θαλάσσῃ", "Meer", None,
  "θάλασσα heisst «Meer»; gemeint ist der See Gennesaret (See von Galiläa). Wie bei Markus «See»."),
 ("MAT.8.25", "rette", "literal", "σῶσον", None, ["hilf", "rette uns"],
  "Wiedergabe für Matthäus: σῴζω «retten». Der Ruf hat kein Objekt; die Übersetzung ergänzt «uns» nicht (eine Lesart hat es, siehe Alternativen). In [[MAT.9.21]]–[[MAT.9.22]] schliesst «retten» die Heilung ein."),
 ("MAT.8.26", "ihr Kleingläubigen", "literal", "ὀλιγόπιστοι", "ihr Wenig-Glaubenden", ["ihr mit eurem kleinen Glauben", "ihr Zaghaften"],
  "Wiedergabe für Matthäus: ὀλιγόπιστος «kleingläubig» (auch [[MAT.6.30]], [[MAT.14.31]], [[MAT.16.8]]; ὀλιγοπιστία [[MAT.17.20]]). Das Wort spricht den Jüngern nicht jeden Glauben ab, sondern nennt ihn zu klein. Bei Markus fragt Jesus: «Habt ihr noch keinen Glauben?» ([[MRK.4.40]])."),
 ("MAT.8.26", "fuhr", "literal", "ἐπετίμησεν", None, ["bedrohte", "gebot", "schalt"],
  "ἐπιτιμάω «anherrschen, scharf zurechtweisen»; dasselbe Verb steht beim Austreiben von Dämonen ([[MAT.17.18]]). Wie [[MRK.4.39]] «fuhr … an»."),
 ("MAT.8.28", "der Gadarener", "literal", "τῶν Γαδαρηνῶν", None, ["der Gerasener", "der Gergesener"],
  "Gadara lag einige Kilometer südöstlich des Sees; [[MRK.5.1]] und [[LUK.8.26]] nennen die Gerasener. Bei Matthäus sind es zwei Besessene, bei Markus und Lukas einer. Zu den Lesarten siehe Alternativen."),
 ("MAT.8.28", "Grabstätten", "literal", "μνημείων", None, ["Gräbern", "Grabhöhlen"],
  "Gemeint sind Grabhöhlen ausserhalb der Siedlung; Gräber machten nach [[NUM.19.16]] unrein. Wie [[MRK.5.2]]."),
 ("MAT.8.29", "Was haben wir mit dir zu tun", "adapted", "Τί ἡμῖν καὶ σοί", "Was uns und dir?", ["Was willst du von uns?", "Lass uns in Ruhe!"],
  "Semitische Abwehrformel (vgl. [[1KI.17.18]]; [[MRK.5.7]]; [[JHN.2.4]]), als Redewendung zugeordnet."),
 ("MAT.8.29", "vor der Zeit", "interpretive", "πρὸ καιροῦ", None, ["vor der festgesetzten Zeit"],
  "καιρός ist der bestimmte Zeitpunkt; gemeint ist wohl die erwartete Zeit des Gerichts über die bösen Mächte. Nur Matthäus hat diese Wendung."),
 ("MAT.8.31", "Die Dämonen", "literal", "δαίμονες", None, ["die bösen Geister"],
  "Einziges Vorkommen von δαίμων bei Matthäus; sonst δαιμόνιον ([[MAT.9.33]]–[[MAT.9.34]]). Beide Wörter sind «Dämon» übersetzt; δαιμονιζόμενος «Besessener» (gemeinsame Matthäus-Wiedergabe)."),
 ("MAT.8.33", "Die Hirten", "adapted", "βόσκοντες", "die Weidenden", ["die Schweinehirten"], None),
 ("MAT.8.34", "weggehe", "literal", "μεταβῇ", "hinübergehe", ["fortgehe"], None),
 ("MAT.9.1", "seine eigene Stadt", "interpretive", "τὴν ἰδίαν πόλιν", None, ["seine Heimatstadt"],
  "Gemeint ist Kafarnaum, wo Jesus nach [[MAT.4.13]] wohnte, nicht Nazaret. Der Name fällt hier nicht; die Übersetzung ergänzt ihn nicht."),
 ("MAT.9.2", "Bett", "literal", "κλίνης", None, ["Liege", "Trage", "Matte"],
  "κλίνη ist ein Bett oder eine Liege, auf der man den Gelähmten trägt; [[MRK.2.4]] hat κράβαττος «Matte». Matthäus erzählt nicht vom abgedeckten Dach."),
 ("MAT.9.2", "Sei getrost", "adapted", "Θάρσει", "Fasse Mut", ["Hab Mut", "Nur Mut"], "Ebenso [[MAT.9.22]]."),
 ("MAT.9.2", "Kind", "literal", "τέκνον", None, ["mein Sohn"],
  "Liebevolle Anrede, nicht Altersangabe; wie [[MRK.2.5]]."),
 ("MAT.9.2", "sind vergeben", "interpretive", "ἀφίενταί", "werden vergeben", ["sind dir vergeben", "werden dir vergeben"],
  "Das Präsens spricht die Vergebung in diesem Augenblick zu; «sind vergeben» gibt das im Deutschen wieder (wie [[MRK.2.5]]). Die Lesart ἀφέωνταί (Perfekt, RP) ergäbe dasselbe Deutsch und steht deshalb nicht bei den Alternativen; ebenso in [[MAT.9.5]]."),
 ("MAT.9.3", "lästert", "literal", "βλασφημεῖ", None, ["lästert Gott"],
  "Der Vorwurf der Gotteslästerung ergibt sich daraus, dass nach jüdischem Verständnis Gott allein Sünden vergibt (ausdrücklich in [[MRK.2.7]]). Die Übersetzung ergänzt «Gott» nicht."),
 ("MAT.9.4", "kannte", "literal", "εἰδὼς", "wissend", ["erkannte", "durchschaute"],
  "Der SBLGNT liest mit WH, Treg und NIV εἰδώς; NA28 und RP lesen ἰδών «sah». Siehe Alternativen."),
 ("MAT.9.6", "Steh auf", "adapted", "Ἐγερθεὶς", "Aufgestanden", ["Erhebe dich"],
  "Das Partizip ἐγερθείς ist vor dem Imperativ als Aufforderung wiedergegeben. Die Lesart Ἔγειρε (WH, Treg) ergäbe dasselbe Deutsch und steht deshalb nicht bei den Alternativen."),
 ("MAT.9.6", "– da sagt er zum Gelähmten", "literal", "τότε λέγει τῷ παραλυτικῷ", None, ["… vergeben, sagt er zum Gelähmten:"],
  "Der Satz bricht ab: Jesus wendet sich mitten im Satz dem Gelähmten zu. Gedankenstrich und neue Anführungszeichen machen den Bruch sichtbar (wie [[MRK.2.10]])."),
 ("MAT.9.8", "fürchteten sie sich", "literal", "ἐφοβήθησαν", None, ["erschraken", "wurden von Ehrfurcht ergriffen"],
  "φοβέομαι meint hier die Furcht vor dem Unerwarteten, aus dem Gott spricht; die Menschen preisen zugleich Gott."),
 ("MAT.9.8", "den Menschen", "interpretive", "τοῖς ἀνθρώποις", None, None,
  "Die Mehrzahl «den Menschen» fällt auf: Gott hat solche Vollmacht nicht nur einem gegeben. Manche beziehen das auf den Menschensohn als Menschen, andere auf die Vollmacht, die später die Gemeinde erhält (vgl. [[MAT.18.18]]). Der Text lässt es offen."),
 ("MAT.9.9", "Zollstelle", "literal", "τελώνιον", None, ["Zollhaus", "Zolltisch"],
  "Ort, an dem Zoll auf Waren erhoben wurde. Der Mann heisst hier Matthäus, in [[MRK.2.14]] und [[LUK.5.27]] Levi; ob es dieselbe Person mit zwei Namen ist, wird verschieden beurteilt. Vgl. «Matthäus, der Zöllner» in [[MAT.10.3]]."),
 ("MAT.9.10", "im Haus", "interpretive", "ἐν τῇ οἰκίᾳ", None, ["in seinem Haus", "im Haus des Matthäus"],
  "Wessen Haus gemeint ist, sagt Matthäus nicht; nach [[LUK.5.29]] ist es das Haus Levis, [[MRK.2.15]] lässt es ebenfalls offen."),
 ("MAT.9.10", "Zöllner", "literal", "τελῶναι", None, ["Zolleinnehmer"],
  "Einnehmer von Zöllen und Abgaben, oft im Auftrag von Zollpächtern; sie galten als unehrlich und unrein und werden mit den «Sündern» zusammen genannt. «Sünder» meint Menschen, die sich nicht an die Tora hielten oder als solche galten."),
 ("MAT.9.12", "die Gesunden", "adapted", "οἱ ἰσχύοντες", "die Starken", ["die Kräftigen"],
  "ἰσχύω heisst «stark sein, bei Kräften sein»; im Gegensatz zu den Kranken sind die Gesunden gemeint. [[MRK.2.17]] hat dasselbe Wort."),
 ("MAT.9.13", "Barmherzigkeit will ich und nicht Opfer", "literal", "Ἔλεος θέλω καὶ οὐ θυσίαν", None, ["Erbarmen will ich, nicht Opfer", "Ich will Barmherzigkeit mehr als Opfer"],
  "Zitat aus [[HOS.6.6]], nur bei Matthäus (auch [[MAT.12.7]]). Hebräisch steht ḥesed (Treue, Güte), griechisch ἔλεος. Das «nicht» ist nach verbreiteter Auslegung im hebräischen Sinn vergleichend zu verstehen («mehr als»); wörtlich übersetzt bleibt die Schärfe erhalten."),
 ("MAT.9.13", "Gerechte", "literal", "δικαίους", None, ["Fromme"],
  "Wiedergabe für Matthäus: δίκαιος «gerecht», δικαιοσύνη «Gerechtigkeit». Ob die «Gerechten» hier ironisch die gemeint sind, die sich dafür halten, oder ob das Wort ernst gemeint ist, wird verschieden gedeutet."),
 ("MAT.9.15", "die Hochzeitsgäste", "adapted", "οἱ υἱοὶ τοῦ νυμφῶνος", "die Söhne des Brautgemachs", ["die Freunde des Bräutigams"],
  "Semitische Wendung für die engsten Gäste und Begleiter des Bräutigams; wie [[MRK.2.19]]."),
 ("MAT.9.15", "trauern", "literal", "πενθεῖν", None, ["klagen"],
  "[[MRK.2.19]] hat «fasten»; Matthäus setzt «trauern» und stellt so Fasten und Trauer nebeneinander."),
 ("MAT.9.16", "ungewalktem", "literal", "ἀγνάφου", None, ["neuem", "ungewaschenem"],
  "Gewalkt wird Wollstoff, damit er verfilzt und nicht mehr einläuft; ein Flicken aus ungewalktem Stoff schrumpft beim ersten Waschen und reisst das alte Gewebe auf."),
 ("MAT.9.17", "jungen", "literal", "νέον", "neuen", ["neuen"],
  "Junger Wein gärt noch und dehnt sich aus; alte, schon gedehnte Schläuche aus Tierhaut reissen dabei. νέος (jung, frisch) ist mit «jung», καινός (neu) mit «neu» wiedergegeben."),
 ("MAT.9.18", "Vorsteher", "interpretive", "ἄρχων", "Herrscher, Oberster", ["Oberster", "Ratsherr", "Synagogenvorsteher"],
  "ἄρχων bezeichnet einen Mann in leitender Stellung. [[MRK.5.22]] nennt ihn Synagogenvorsteher mit Namen Jairus; Matthäus nennt weder Amt noch Namen. εἷς («einer») steht hier wie ein unbestimmter Artikel."),
 ("MAT.9.18", "ist eben gestorben", "literal", "ἄρτι ἐτελεύτησεν", None, ["ist soeben gestorben", "liegt im Sterben"],
  "Bei Matthäus ist das Mädchen schon tot, als der Vater kommt; bei Markus liegt es im Sterben ([[MRK.5.23]]), die Todesnachricht kommt später."),
 ("MAT.9.20", "an Blutfluss litt", "literal", "αἱμορροοῦσα", "blutflüssig", ["an Blutungen litt"],
  "Gemeint ist wohl eine andauernde Blutung, die nach [[LEV.15.25]]–[[LEV.15.27]] unrein machte; auch wer sie berührte, wurde unrein."),
 ("MAT.9.20", "den Saum", "traditional", "τοῦ κρασπέδου", None, ["die Quaste", "den Rand", "die Troddel"],
  "κράσπεδον kann den Rand eines Gewands meinen oder die Quasten, die nach [[NUM.15.38]]–[[NUM.15.39]] und [[DEU.22.12]] an den Ecken des Obergewands getragen wurden (vgl. [[MAT.23.5]]). «Saum» ist die vertraute Wiedergabe und lässt beides zu; wie [[MRK.6.56]]."),
 ("MAT.9.21", "werde ich gerettet", "literal", "σωθήσομαι", None, ["werde ich gesund", "werde ich geheilt"],
  "σῴζω schliesst hier die Heilung ein, sagt aber mehr; «retten» erhält den Anklang (so auch [[MAT.9.22]])."),
 ("MAT.9.23", "die Flötenspieler", "literal", "τοὺς αὐλητὰς", None, ["die Klageflötner"],
  "Zur Totenklage gehörten Flötenspieler und Klagefrauen; der Lärm zeigt, dass die Trauer schon begonnen hat."),
 ("MAT.9.24", "es schläft", "literal", "καθεύδει", None, None,
  "Ob Jesus sagt, das Mädchen sei nur scheintot, oder ob er den Tod im Blick auf die Auferweckung «Schlaf» nennt, lässt der Text offen; die Lachenden halten es für tot."),
 ("MAT.9.27", "Sohn Davids", "literal", "υἱὲ Δαυίδ", None, ["Nachkomme Davids"],
  "Messianischer Titel; Matthäus stellt Jesus von [[MAT.1.1]] an als Sohn Davids vor. Hier rufen ihn Blinde so an, wie später in [[MAT.20.30]]."),
 ("MAT.9.30", "fuhr", "adapted", "ἐνεβριμήθη", "schnaubte an", ["gebot streng", "drohte"],
  "ἐμβριμάομαι bezeichnet heftige Erregung oder scharfes Anfahren. Wie [[MRK.1.43]] «fuhr … hart an»."),
 ("MAT.9.32", "stummen", "interpretive", "κωφὸν", None, ["tauben", "taubstummen"],
  "κωφός heisst «stumpf» und bezeichnet Stumme wie Taube. Der Fortgang («redete der Stumme», [[MAT.9.33]]) zeigt, dass hier Stummheit im Vordergrund steht."),
 ("MAT.9.33", "so etwas", "adapted", "οὕτως", "so", ["Derartiges"], None),
 ("MAT.9.34", "den Herrscher der Dämonen", "literal", "τῷ ἄρχοντι τῶν δαιμονίων", None, ["den Obersten der Dämonen", "den Fürsten der Dämonen"],
  "Wie [[MRK.3.22]] «Herrscher der Dämonen». Matthäus nimmt den Vorwurf in [[MAT.12.24]] wieder auf. Der SBLGNT-Apparat verzeichnet zu diesem Vers keine Variante; nach der CNTR-Transkription fehlt der ganze Vers in 05 (Codex Bezae)."),
 ("MAT.9.35", "das Evangelium vom Reich", "literal", "τὸ εὐαγγέλιον τῆς βασιλείας", "die gute Nachricht des Reiches", ["die frohe Botschaft vom Reich"],
  "Matthäische Wendung (auch [[MAT.4.23]], [[MAT.24.14]]). «Das Reich» allein meint das Reich der Himmel. Der Vers nimmt [[MAT.4.23]] fast wörtlich auf."),
 ("MAT.9.36", "hatte er Erbarmen", "literal", "ἐσπλαγχνίσθη", "es ging ihm an die Eingeweide", ["es jammerte ihn", "er hatte Mitleid"],
  "σπλαγχνίζομαι kommt von σπλάγχνα «Eingeweide», dem Sitz der Gefühle; wie [[MRK.6.34]]. Das Bild der Schafe ohne Hirten stammt aus [[NUM.27.17]] und [[EZK.34.5]]."),
 ("MAT.9.36", "geschunden und hilflos", "adapted", "ἐσκυλμένοι καὶ ἐρριμμένοι", "geschunden und hingeworfen", ["erschöpft und verwahrlost", "abgehetzt und zerstreut"],
  "σκύλλω «schinden, plagen», ῥίπτω «hinwerfen»: Die Menschen sind wie Schafe, die erschöpft daliegen und sich nicht helfen können."),
 ("MAT.9.38", "aussende", "adapted", "ἐκβάλῃ", "hinaustreibe", ["hinausschicke"],
  "ἐκβάλλω ist dasselbe Verb wie beim Austreiben der Dämonen ([[MAT.9.33]]–[[MAT.9.34]]); hier meint es ein dringliches Aussenden. Kapitel 10 erzählt anschliessend von der Aussendung der Zwölf."),
]

DEC_GSW = [
 ("MAT.8.1", "vil Lüüt", "adapted", "ὄχλοι πολλοί", "vil Mängene", ["vil Volk"],
  "ὄχλος i de Einzahl «d Mängi», i de Mehrzahl «d Lüüt», wil «Mängene» i de Mundart ungwohnt isch ([[MAT.8.18]], [[MAT.9.8]], [[MAT.9.33]], [[MAT.9.36]])."),
 ("MAT.8.2", "Ussätzige", "traditional", "λεπρὸς", None, ["Hutchranke"],
  "λέπρα meint verschideni Hutchrankete, wo nach [[LEV.13.1]]–[[LEV.13.46]] unrein gmacht händ; drum «rein mache». Wie bim Markus ([[MRK.1.40]])."),
 ("MAT.8.2", "hät sich vor ihm nidergworfe", "literal", "προσεκύνει", None, ["hät em ghuldiget", "hät en aabättet"],
  "Gmeinsami Matthäus-Wiedergab: προσκυνέω vor Mänsche und vor em Jesus «sich niderwärfe», mit Gott als Empfänger «aabätte». S Wort beschriibt d Gebärde; öb s Aabätte oder Ehrerbietig isch, laat de Text offe. Gliich [[MAT.9.18]]."),
 ("MAT.8.4", "Pass uf", "adapted", "Ὅρα", "Lueg", ["Lueg, dass"],
  "«Lueg» isch für ἰδού reserviert (gmeinsami Matthäus-Wiedergab); drum für ὅρα «Pass uf». Gliich [[MAT.9.30]] «Passed uf»."),
 ("MAT.8.5", "Hauptmaa", "traditional", "ἑκατόνταρχος", "Befählshaber über hundert", ["Offizier"], "Wie [[MRK.15.39]]."),
 ("MAT.8.6", "Diener", "interpretive", "παῖς", "Bueb", ["Chind", "Sohn"],
  "παῖς heisst «Chind, Bueb» und «Diener»; [[LUK.7.2]] seit δοῦλος, [[JHN.4.46]] verzellt vo eme Sohn."),
 ("MAT.8.7", "Ich chume und heil en", "interpretive", "Ἐγὼ ἐλθὼν θεραπεύσω αὐτόν", "Ich wirde choo und en heile", ["Söll ich öppe choo und en heile?"],
  "D Mundart seit s Futur mit em Präsens. De Satz cha au e verwunderti Frag sii (söll ich als Jud is Huus vo eme Nichtjud choo?)."),
 ("MAT.8.8", "wird gsund", "literal", "ἰαθήσεται", None, ["wird gheilt"],
  "θεραπεύω «heile», ἰάομαι «gsund wärde», σῴζω «rette», damit d Verbe underscheidbar bliibed."),
 ("MAT.8.10", "Glaube", "literal", "πίστιν", None, ["Vertroue"],
  "πίστις «Glaube», πιστεύω «glaube», dur s ganz Matthäusevangelium."),
 ("MAT.8.11", "Riich vo de Himel", "literal", "βασιλείᾳ τῶν οὐρανῶν", None, ["Himmelriich"],
  "Gmeinsami Matthäus-Wiedergab «s Riich vo de Himel», Schriibig «Himel» wie im Unservatter ([[MAT.6.9]])."),
 ("MAT.8.11", "am Tisch ligge", "literal", "ἀνακλιθήσονται", None, ["am Tisch hocke"],
  "Bim Feschtmähli isch me uf Polschter am Tisch gläge; wie bim Markus «am Tisch gläge»."),
 ("MAT.8.12", "s Hüüle und s Zändchnirsche", "adapted", "ὁ κλαυθμὸς καὶ ὁ βρυγμὸς τῶν ὀδόντων", "s Weine und s Chnirsche vo de Zää", ["s Briegge und s Zändchnirsche"],
  "Gmeinsami Matthäus-Wiedergab ([[MAT.13.42]], [[MAT.13.50]], [[MAT.22.13]], [[MAT.24.51]], [[MAT.25.30]]); «Hüüle» isch s Mundartwort für luuts Weine."),
 ("MAT.8.17", "damit erfüllt wird", "literal", "ὅπως πληρωθῇ", None, None,
  "Gmeinsami Matthäus-Formle «damit erfüllt wird, was … dur de Prophet gseit worden isch»; Zitat us [[ISA.53.4]] nach em hebräische Text."),
 ("MAT.8.20", "de Mänschesohn", "literal", "ὁ υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None,
  "Gmeinsami Wiedergab wie bim Markus und Johannes; de Jesus redt eso vo sich ([[DAN.7.13]])."),
 ("MAT.8.24", "Bebe", "literal", "σεισμὸς", "Erschütterig", ["Sturm", "Unwätter"],
  "σεισμός isch bim Matthäus susch s Ärdbebe ([[MAT.24.7]], [[MAT.27.54]], [[MAT.28.2]]); s ungwöhnlich Wort isch bhalte."),
 ("MAT.8.26", "ir Chliigläubige", "literal", "ὀλιγόπιστοι", "ir Wenig-Glaubende", ["ir mit eurem chliine Glaube"],
  "Gmeinsami Matthäus-Wiedergab für ὀλιγόπιστος ([[MAT.6.30]], [[MAT.14.31]], [[MAT.16.8]])."),
 ("MAT.8.26", "ganz still", "adapted", "γαλήνη μεγάλη", "e grossi Stilli", None,
  "«Es isch ganz still worde» seit me eso i de Mundart; wie [[MRK.4.39]]."),
 ("MAT.8.29", "Was händ mir mit dir z tue", "adapted", "Τί ἡμῖν καὶ σοί", "Was üs und dir?", ["Was wottsch vo üs?"],
  "Semitischi Abwehrformle (vgl. [[1KI.17.18]], [[JHN.2.4]]), als Redewändig zueornet."),
 ("MAT.8.33", "D Hirte", "adapted", "βόσκοντες", "die, wo gweidet händ", ["d Söihirte"], None),
 ("MAT.9.2", "Häb Muet", "adapted", "Θάρσει", "Fass Muet", ["Nu Muet"], "Gliich [[MAT.9.22]]."),
 ("MAT.9.2", "sind vergää", "interpretive", "ἀφίενταί", "wärded vergää", None,
  "S Präsens sprecht d Vergäbig i dem Moment zue; wie [[MRK.2.5]]."),
 ("MAT.9.6", "gang hei", "adapted", "ὕπαγε εἰς τὸν οἶκόν σου", "gang i dis Huus", None,
  "«Gang hei» isch d gwohnti Mundartwändig (wie [[MRK.2.11]]); gliich [[MAT.9.7]] «isch hei gange»."),
 ("MAT.9.13", "Barmhärzigkeit wott ich und nöd Opfer", "literal", "Ἔλεος θέλω καὶ οὐ θυσίαν", None, ["Erbarme wott ich meh als Opfer"],
  "Zitat us [[HOS.6.6]]; s «nöd» isch im hebräische Sinn vergliichend («meh als»), wörtlich bhalte."),
 ("MAT.9.15", "d Hochziitsgäscht", "adapted", "οἱ υἱοὶ τοῦ νυμφῶνος", "d Söhn vom Brutgmach", None, "Wie [[MRK.2.19]]."),
 ("MAT.9.18", "Vorsteher", "interpretive", "ἄρχων", "Oberschte", ["Synagogevorsteher"],
  "Bim Markus heisst er Jairus und isch Synagogevorsteher ([[MRK.5.22]]); de Matthäus nännt weder Amt no Name."),
 ("MAT.9.18", "äbe", "literal", "ἄρτι", None, ["grad"],
  "«Grad» isch für εὐθέως/εὐθύς reserviert (gmeinsami Matthäus-Wiedergab); drum für ἄρτι «äbe»."),
 ("MAT.9.20", "de Saum", "traditional", "τοῦ κρασπέδου", None, ["d Quaste"],
  "κράσπεδον cha de Rand oder d Quaste a de Egge vom Obergwand meine ([[NUM.15.38]]); wie [[MRK.6.56]] «Saum»."),
 ("MAT.9.22", "grettet", "literal", "σέσωκέν", None, ["gheilt", "gsund gmacht"],
  "σῴζω schlüüsst d Heilig ii, seit aber meh; drum «rette»."),
 ("MAT.9.30", "hert aagschnauzt", "adapted", "ἐνεβριμήθη", None, ["streng befole"], "Wie [[MRK.1.43]]."),
 ("MAT.9.33", "hät me", "adapted", "ἐφάνη", "isch erschine", None,
  "«Hät me so öppis gseh» seit natürlicher, was d Lüüt meined; s Griechisch seit «isch so öppis erschine»."),
 ("MAT.9.35", "s Evangelium vom Riich", "literal", "τὸ εὐαγγέλιον τῆς βασιλείας", None, ["di guet Nachricht vom Riich"],
  "Matthäus-Wändig ([[MAT.4.23]], [[MAT.24.14]])."),
 ("MAT.9.36", "Erbarme", "literal", "ἐσπλαγχνίσθη", None, ["Mitleid"], "Wie [[MRK.6.34]]."),
 ("MAT.9.37", "Ärn", "literal", "θερισμὸς", None, None, None),
]

# (Variante, Stelle, von de, zu de, von gsw, zu gsw, Auswirkung, Hinweis de, Hinweis gsw, Lesarten de, Lesarten gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw. aus
#  den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-MAT-008-002-01:R2", "MAT.8.2", "ein Aussätziger trat heran", "ein Aussätziger kam", "en Ussätzige isch härechoo", "en Ussätzige isch choo", "gering",
  "Statt «trat heran» (προσελθών) steht «kam» (ἐλθών).", "Statt «isch härechoo» (προσελθών) staat «isch choo» (ἐλθών).",
  {"R1": [("προσελθὼν", "trat heran", "WH, Treg, NA28")], "R2": [("ἐλθὼν", "kam", "RP")]},
  {"R1": [("προσελθὼν", "isch härechoo", "WH, Treg, NA28")], "R2": [("ἐλθὼν", "isch choo", "RP")]},
  ["προσέρχομαι ist ein Lieblingswort des Matthäus (vgl. [[MAT.8.5]], [[MAT.8.19]]); Abschreiber könnten das einfache Verb gesetzt oder umgekehrt an den Sprachgebrauch des Evangeliums angeglichen haben.",
   "Laut der automatischen Zuordnung lesen 01 und 03 προσελθών, 04 und 032 ἐλθών."],
  ["προσέρχομαι bruucht de Matthäus gärn; Abschriiber chönnted s eifach Verb gsetzt oder umgekehrt aaglichen ha.",
   "Nach de automatische Zueornig läsed 01 und 03 προσελθών, 04 und 032 ἐλθών."]),
 ("VAR-SBLGNTAPP-MAT-008-003-01:R2", "MAT.8.3", "Und er streckte die Hand aus", "Und Jesus streckte die Hand aus", "Und er hät d Hand usgstreckt", "Und de Jesus hät d Hand usgstreckt", "gering",
  "Der Name Jesus ist ausdrücklich genannt.", "De Name Jesus isch usdrücklich gnännt.",
  {"R1": [("αὐτοῦ", "ihn", "WH, Treg, NA28")], "R2": [("αὐτοῦ ὁ Ἰησοῦς", "ihn Jesus", "RP")]},
  {"R1": [("αὐτοῦ", "en", "WH, Treg, NA28")], "R2": [("αὐτοῦ ὁ Ἰησοῦς", "en de Jesus", "RP")]},
  ["Namen werden beim Abschreiben oft verdeutlichend ergänzt, besonders wo ein Abschnitt für die Lesung beginnt; ebenso kann der Name als überflüssig weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 (auch die Korrektur), 03, 04 und 032 ohne den Namen."],
  ["Näme sind bim Abschriibe oft zur Verdüütlichung ergänzt worde; oder de Name isch als überflüssig usgfalle.",
   "Nach de automatische Zueornig läsed 01 (au d Korrektur), 03, 04 und 032 ohni Name."]),
 ("VAR-SBLGNTAPP-MAT-008-007-02:R2", "MAT.8.7", "Und er sagt zu ihm", "Und Jesus sagt zu ihm", "Und er seit zu ihm", "Und de Jesus seit zu ihm", "gering",
  "Der Name Jesus ist ausdrücklich genannt.", "De Name Jesus isch usdrücklich gnännt.",
  {"R1": [("αὐτῷ", "zu ihm", "WH, NA28")], "R2": [("αὐτῷ ὁ Ἰησοῦς", "zu ihm Jesus", "Treg, RP")]},
  {"R1": [("αὐτῷ", "zu ihm", "WH, NA28")], "R2": [("αὐτῷ ὁ Ἰησοῦς", "zu ihm de Jesus", "Treg, RP")]},
  ["Verdeutlichende Ergänzung des Namens bei Sprecherwechsel liegt nahe; ebenso kann er beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 032 ohne den Namen."],
  ["Ergänzig vom Name bim Sprächerwächsel liit nöch; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 032 ohni Name."]),
 ("VAR-SBLGNTAPP-MAT-008-009-01:R2", "MAT.8.9", "unter Befehlsgewalt", "unter Befehlsgewalt gestellt", "under Befehlsgwalt", "under Befehlsgwalt gstellt", "gering",
  "Mit τασσόμενος betont der Hauptmann, dass er selbst unter Befehl gestellt ist.", "Mit τασσόμενος betont de Hauptmaa, dass er sälber under Befehl gstellt isch.",
  {"R1": [("ἐξουσίαν", "unter Befehlsgewalt", "Treg, NA28, RP")], "R2": [("ἐξουσίαν τασσόμενος", "unter Befehlsgewalt gestellt", "WH")]},
  {"R1": [("ἐξουσίαν", "under Befehlsgwalt", "Treg, NA28, RP")], "R2": [("ἐξουσίαν τασσόμενος", "under Befehlsgwalt gstellt", "WH")]},
  ["τασσόμενος steht in der Parallele [[LUK.7.8]] und kann von dort übernommen sein; ebenso kann es in Matthäus ursprünglich sein und ausgefallen. Der SBLGNT folgt hier Treg, NA28 und RP gegen WH.",
   "Laut der automatischen Zuordnung lesen 01 und 03 mit τασσόμενος, 04 und 032 ohne."],
  ["τασσόμενος staat i de Parallele [[LUK.7.8]] und cha vo dört übernoo sii; oder s isch im Matthäus ursprünglich und usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 03 mit τασσόμενος, 04 und 032 ohni."]),
 ("VAR-SBLGNTAPP-MAT-008-010-01:R2", "MAT.8.10", "Bei niemandem in Israel habe ich einen so grossen Glauben gefunden", "Nicht einmal in Israel habe ich einen so grossen Glauben gefunden",
  "Bi niemertem in Israel han ich eso en grosse Glaube gfunde", "Nöd emal in Israel han ich eso en grosse Glaube gfunde", "mittel",
  "«Nicht einmal in Israel» stellt den Hauptmann über Israel; «bei niemandem in Israel» vergleicht ihn mit einzelnen Menschen.",
  "«Nöd emal in Israel» stellt de Hauptmaa über Israel; «bi niemertem in Israel» vergliicht en mit einzelne Mänsche.",
  {"R1": [("παρʼ οὐδενὶ τοσαύτην πίστιν ἐν τῷ Ἰσραὴλ", "bei niemandem in Israel einen so grossen Glauben", "WH, Treg, NA28")], "R2": [("οὐδὲ ἐν τῷ Ἰσραὴλ τοσαύτην πίστιν", "nicht einmal in Israel einen so grossen Glauben", "RP")]},
  {"R1": [("παρʼ οὐδενὶ τοσαύτην πίστιν ἐν τῷ Ἰσραὴλ", "bi niemertem in Israel eso en grosse Glaube", "WH, Treg, NA28")], "R2": [("οὐδὲ ἐν τῷ Ἰσραὴλ τοσαύτην πίστιν", "nöd emal in Israel eso en grosse Glaube", "RP")]},
  ["Die Lesart οὐδὲ ἐν τῷ Ἰσραήλ entspricht der Parallele [[LUK.7.9]] und kann daran angeglichen sein; ebenso kann παρʼ οὐδενί eine Abschwächung des schärferen Vergleichs sein.",
   "Laut der automatischen Zuordnung lesen 03 und 032 παρʼ οὐδενί, 01 und 04 οὐδὲ ἐν τῷ Ἰσραήλ."],
  ["οὐδὲ ἐν τῷ Ἰσραήλ entspricht de Parallele [[LUK.7.9]] und cha dra aaglichen sii; oder παρʼ οὐδενί schwächt de schärferi Vergliich ab.",
   "Nach de automatische Zueornig läsed 03 und 032 παρʼ οὐδενί, 01 und 04 οὐδὲ ἐν τῷ Ἰσραήλ."]),
 ("VAR-SBLGNTAPP-MAT-008-013-02:R2", "MAT.8.13", "wurde der Diener gesund", "wurde sein Diener gesund", "de Diener isch", "sin Diener isch", "gering",
  "Das Fürwort «sein» ist ergänzt.", "S Fürwort «sin» isch ergänzt.",
  {"R1": [("παῖς", "der Diener", "WH, Treg")], "R2": [("παῖς αὐτοῦ", "sein Diener", "NA28, RP")]},
  {"R1": [("παῖς", "de Diener", "WH, Treg")], "R2": [("παῖς αὐτοῦ", "sin Diener", "NA28, RP")]},
  ["Das Fürwort kann verdeutlichend ergänzt oder als selbstverständlich weggelassen worden sein. Der SBLGNT folgt hier WH und Treg gegen NA28 und RP.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne αὐτοῦ, 04 und 032 mit ihm."],
  ["S Fürwort cha zur Verdüütlichung ergänzt oder als sälbverständlich wäggloo worde sii.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni αὐτοῦ, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-008-018-01:R2", "MAT.8.18", "die vielen Menschenmengen um sich", "die Menge um sich", "di vile Lüüt um sich", "d Mängi um sich", "gering",
  "Statt «viele Menschenmengen» steht «die Menge» in der Einzahl.", "Statt «vil Lüüt» staat «d Mängi» i de Einzahl.",
  {"R1": [("πολλοὺς ὄχλους", "die vielen Menschenmengen", "Treg, RP")], "R2": [("ὄχλον", "die Menge", "WH, NA28")]},
  {"R1": [("πολλοὺς ὄχλους", "di vile Lüüt", "Treg, RP")], "R2": [("ὄχλον", "d Mängi", "WH, NA28")]},
  ["Die Mehrzahl kann an [[MAT.8.1]] angeglichen sein; ebenso kann die kurze Lesart eine Vereinfachung sein. Daneben gibt es weitere Formen (z. B. πολὺν ὄχλον). Der SBLGNT folgt hier Treg und RP gegen WH und NA28.",
   "Laut der automatischen Zuordnung liest 04 πολλοὺς ὄχλους, 03 und 032 ὄχλον; 01 hat einen anderen Wortlaut, den die Zuordnung keiner der beiden Lesarten zuweist."],
  ["D Mehrzahl cha a [[MAT.8.1]] aaglichen sii; oder di churz Läsart vereifacht. Es git au no anderi Forme.",
   "Nach de automatische Zueornig liest 04 πολλοὺς ὄχλους, 03 und 032 ὄχλον; 01 hät en andere Wortlut."]),
 ("VAR-SBLGNTAPP-MAT-008-021-01:R2", "MAT.8.21", "von den Jüngern", "von seinen Jüngern", "vo de Jünger", "vo sine Jünger", "gering",
  "Das Fürwort «seinen» ist ergänzt.", "S Fürwort «sine» isch ergänzt.",
  {"R1": [("μαθητῶν", "von den Jüngern", "WH, Treg")], "R2": [("μαθητῶν αὐτοῦ", "von seinen Jüngern", "NA28, RP")]},
  {"R1": [("μαθητῶν", "vo de Jünger", "WH, Treg")], "R2": [("μαθητῶν αὐτοῦ", "vo sine Jünger", "NA28, RP")]},
  ["Verdeutlichende Ergänzung oder Wegfall als selbstverständlich. Der SBLGNT folgt hier WH und Treg gegen NA28 und RP.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne αὐτοῦ, 04 und 032 mit ihm."],
  ["Ergänzig zur Verdüütlichung oder Wägfall als sälbverständlich.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni αὐτοῦ, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-008-022-01:R2", "MAT.8.22", "Jesus aber sagt zu ihm", "Jesus aber sagte zu ihm", "De Jesus aber seit zu ihm", "De Jesus aber hät zu ihm gseit", "gering",
  "Vergangenheit statt erzählendem Präsens.", "Vergangeheit statt erzählendem Präsens.",
  {"R1": [("λέγει", "sagt", "WH, Treg, NA28")], "R2": [("εἶπεν", "sagte", "RP")]},
  {"R1": [("λέγει", "seit", "WH, Treg, NA28")], "R2": [("εἶπεν", "hät gseit", "RP")]},
  ["Das erzählende Präsens wurde beim Abschreiben oft durch die geläufigere Vergangenheitsform ersetzt; der umgekehrte Weg ist seltener, aber möglich.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 λέγει, 032 εἶπεν."],
  ["S erzählend Präsens isch bim Abschriibe oft dur d gwohnter Vergangeheit ersetzt worde.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 λέγει, 032 εἶπεν."]),
 ("VAR-SBLGNTAPP-MAT-008-023-01:R2", "MAT.8.23", "in ein Boot", "in das Boot", "in es Boot", "is Boot", "gering",
  "Mit Artikel ist ein bestimmtes, schon bekanntes Boot gemeint.", "Mit Artikel isch es bestimmts, scho bekannts Boot gmeint.",
  {"R1": [("εἰς", "in ein", "WH, Treg")], "R2": [("εἰς τὸ", "in das", "NA28, RP")]},
  {"R1": [("εἰς", "in es", "WH, Treg")], "R2": [("εἰς τὸ", "is", "NA28, RP")]},
  ["Der Artikel kann ergänzt sein, weil das Boot nach [[MAT.8.18]] als bekannt gilt, oder als unnötig weggefallen sein. Der SBLGNT folgt hier WH und Treg gegen NA28 und RP.",
   "Laut der automatischen Zuordnung lesen 03 und 04 ohne Artikel, 032 mit ihm; die Erstschrift von 01 hat ihn, die Korrektur nicht."],
  ["De Artikel cha ergänzt sii, wil s Boot nach [[MAT.8.18]] als bekannt gilt, oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 03 und 04 ohni Artikel, 032 mit; d Erschtschrift vo 01 hät en, d Korrektur nöd."]),
 ("VAR-SBLGNTAPP-MAT-008-025-01:R2", "MAT.8.25", "Und sie traten heran", "Und die Jünger traten heran", "Und si sind härechoo", "Und d Jünger sind härechoo", "gering",
  "Die Jünger sind ausdrücklich genannt.", "D Jünger sind usdrücklich gnännt.",
  {"R1": [("προσελθόντες", "sie traten heran", "WH, Treg, NA28")], "R2": [("προσελθόντες οἱ μαθηταὶ", "die Jünger traten heran", "RP")]},
  {"R1": [("προσελθόντες", "si sind härechoo", "WH, Treg, NA28")], "R2": [("προσελθόντες οἱ μαθηταὶ", "d Jünger sind härechoo", "RP")]},
  ["Verdeutlichende Ergänzung des Subjekts (vgl. [[MAT.8.23]]); ebenso möglich ist ein Wegfall.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne Zusatz, 04 und 032 mit ihm."],
  ["Ergänzig vom Subjekt zur Verdüütlichung (vgl. [[MAT.8.23]]); oder es isch usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni Zuesatz, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-008-025-02:R2", "MAT.8.25", "Herr, rette!", "Herr, rette uns!", "Herr, rett!", "Herr, rett üs!", "gering",
  "Der Ruf hat ein ausdrückliches Objekt «uns».", "De Ruef hät es usdrücklichs Objekt «üs».",
  {"R1": [("σῶσον", "rette", "WH, Treg, NA28")], "R2": [("σῶσον ἡμᾶς", "rette uns", "NIV, RP")]},
  {"R1": [("σῶσον", "rett", "WH, Treg, NA28")], "R2": [("σῶσον ἡμᾶς", "rett üs", "NIV, RP")]},
  ["Das Objekt ist eine naheliegende Ergänzung; ebenso kann es weggefallen sein. NIV steht für den griechischen Text, der der New International Version zugrunde liegt.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 ohne ἡμᾶς, 032 mit ihm."],
  ["S Objekt isch e nöchliegendi Ergänzig; oder es isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 ohni ἡμᾶς, 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-008-028-02:R2", "MAT.8.28", "der Gadarener", "der Gergesener", "vo de Gadarener", "vo de Gergesener", "mittel",
  "Der Ort heisst Gergesa statt Gadara.", "De Ort heisst Gergesa statt Gadara.",
  {"R1": [("Γαδαρηνῶν", "der Gadarener", "WH, Treg, NA28")], "R2": [("Γεργεσηνῶν", "der Gergesener", "RP")]},
  {"R1": [("Γαδαρηνῶν", "vo de Gadarener", "WH, Treg, NA28")], "R2": [("Γεργεσηνῶν", "vo de Gergesener", "RP")]},
  ["Die Evangelien nennen den Ort verschieden: [[MRK.5.1]] und [[LUK.8.26]] haben im SBLGNT «Gerasener», Matthäus «Gadarener». Gerasa und Gadara lagen beide nicht direkt am See; «Gergesa» wurde schon in der alten Kirche (Origenes) am Seeufer gesucht. Abschreiber können den Namen deshalb geographisch angepasst oder an andere Überlieferungen angeglichen haben; ebenso kann «Gergesener» eine alte Ortsüberlieferung bewahren. In der Überlieferung kommen alle drei Namen vor.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 Γαδαρηνῶν, 032 Γεργεσηνῶν."],
  ["D Evangelie nänned de Ort verschide: [[MRK.5.1]] und [[LUK.8.26]] händ «Gerasener», de Matthäus «Gadarener». Gerasa und Gadara sind beidi nöd diräkt am See gläge; «Gergesa» hät me scho i de alte Chile (Origenes) am Seeufer gsuecht. Abschriiber chönnted de Name drum aapasst ha; oder «Gergesener» bewahrt e alti Ortsüberliferig.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 Γαδαρηνῶν, 032 Γεργεσηνῶν."]),
 ("VAR-SBLGNTAPP-MAT-008-029-01:R2", "MAT.8.29", "mit dir zu tun, Sohn Gottes", "mit dir zu tun, Jesus, Sohn Gottes", "mit dir z tue, Sohn vo Gott", "mit dir z tue, Jesus, Sohn vo Gott", "gering",
  "Die Dämonen nennen Jesus auch beim Namen.", "D Dämone nänned de Jesus au bim Name.",
  {"R1": [("σοί", "dir", "WH, Treg, NA28")], "R2": [("σοί Ἰησοῦ", "dir, Jesus", "RP")]},
  {"R1": [("σοί", "dir", "WH, Treg, NA28")], "R2": [("σοί Ἰησοῦ", "dir, Jesus", "RP")]},
  ["Die Anrede mit Namen steht in den Parallelen [[MRK.5.7]] und [[LUK.8.28]] und kann daran angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01 (auch die Korrektur), 03, 04 und 032 ohne den Namen."],
  ["D Aared mit em Name staat i de Parallele [[MRK.5.7]] und [[LUK.8.28]] und cha dra aaglichen sii.",
   "Nach de automatische Zueornig läsed 01 (au d Korrektur), 03, 04 und 032 ohni Name."]),
 ("VAR-SBLGNTAPP-MAT-008-031-01:R2", "MAT.8.31", "schick uns in die Herde der Schweine", "erlaube uns, in die Herde der Schweine zu fahren",
  "schick üs i d Herde vo de Söi", "erlaub üs, i d Herde vo de Söi z fahre", "mittel",
  "Die Dämonen bitten um Erlaubnis statt darum, geschickt zu werden.", "D Dämone bitted um Erlaubnis statt drum, gschickt z wärde.",
  {"R1": [("ἀπόστειλον ἡμᾶς", "schick uns", "WH, Treg, NA28")], "R2": [("ἐπίτρεψον ἡμῖν ἀπελθεῖν", "erlaube uns, zu fahren", "RP")]},
  {"R1": [("ἀπόστειλον ἡμᾶς", "schick üs", "WH, Treg, NA28")], "R2": [("ἐπίτρεψον ἡμῖν ἀπελθεῖν", "erlaub üs z fahre", "RP")]},
  ["«Erlauben» steht in [[LUK.8.32]] und [[MRK.5.13]] und kann von dort eingedrungen sein; ebenso kann ἀπόστειλον an [[MRK.5.12]] («schick uns») angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ἀπόστειλον ἡμᾶς, 04 und 032 ἐπίτρεψον ἡμῖν ἀπελθεῖν."],
  ["«Erlaube» staat i [[LUK.8.32]] und [[MRK.5.13]] und cha vo dört cho sii; oder ἀπόστειλον isch a [[MRK.5.12]] aaglichen.",
   "Nach de automatische Zueornig läsed 01 und 03 ἀπόστειλον ἡμᾶς, 04 und 032 ἐπίτρεψον ἡμῖν ἀπελθεῖν."]),
 ("VAR-SBLGNTAPP-MAT-008-032-01:R2", "MAT.8.32", "in die Schweine", "in die Herde der Schweine", "i d Söi", "i d Herde vo de Söi", "gering",
  "Statt «in die Schweine» steht «in die Herde der Schweine».", "Statt «i d Söi» staat «i d Herde vo de Söi».",
  {"R1": [("τοὺς χοίρους", "die Schweine", "WH, Treg, NA28")], "R2": [("τὴν ἀγέλην τῶν χοίρων", "die Herde der Schweine", "RP")]},
  {"R1": [("τοὺς χοίρους", "d Söi", "WH, Treg, NA28")], "R2": [("τὴν ἀγέλην τῶν χοίρων", "d Herde vo de Söi", "RP")]},
  ["Angleichung an die Bitte in [[MAT.8.31]] liegt nahe; ebenso kann die längere Wendung verkürzt worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 τοὺς χοίρους, 032 τὴν ἀγέλην τῶν χοίρων."],
  ["Aagliichig a d Bitt i [[MAT.8.31]] liit nöch; oder di lenger Wändig isch kürzt worde.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 τοὺς χοίρους, 032 τὴν ἀγέλην τῶν χοίρων."]),
 ("VAR-SBLGNTAPP-MAT-008-032-02:R2", "MAT.8.32", "die ganze Herde stürmte", "die ganze Herde der Schweine stürmte", "di ganz Herde isch", "di ganz Herde vo de Söi isch", "gering",
  "«Der Schweine» ist ergänzt.", "«Vo de Söi» isch ergänzt.",
  {"R1": [("ἀγέλη", "Herde", "WH, Treg, NA28")], "R2": [("ἀγέλη τῶν χοίρων", "Herde der Schweine", "RP")]},
  {"R1": [("ἀγέλη", "Herde", "WH, Treg, NA28")], "R2": [("ἀγέλη τῶν χοίρων", "Herde vo de Söi", "RP")]},
  ["Verdeutlichende Ergänzung; ebenso möglich ist Wegfall als überflüssig.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 032 ohne Zusatz."],
  ["Ergänzig zur Verdüütlichung; oder Wägfall als überflüssig.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 032 ohni Zuesatz."]),
 ("VAR-SBLGNTAPP-MAT-009-001-01:R2", "MAT.9.1", "Und er stieg in ein Boot", "Und Jesus stieg in ein Boot", "Und er isch in es Boot gstige", "Und de Jesus isch in es Boot gstige", "gering",
  "Der Name Jesus ist ausdrücklich genannt.", "De Name Jesus isch usdrücklich gnännt.",
  {"R1": [("ἐμβὰς", "er stieg", "WH, Treg, RP, NA28")], "R2": [("ἐμβὰς ὁ Ἰησοῦς", "Jesus stieg", "NIV")]},
  {"R1": [("ἐμβὰς", "er isch gstige", "WH, Treg, RP, NA28")], "R2": [("ἐμβὰς ὁ Ἰησοῦς", "de Jesus isch gstige", "NIV")]},
  ["Am Beginn eines Abschnitts wird der Name oft ergänzt, damit der Leseabschnitt für sich verständlich ist; ebenso kann er weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 ohne den Namen; 032 hat einen anderen Wortlaut, 05 hat hier eine Lücke."],
  ["Am Aafang vo eme Abschnitt wird de Name oft ergänzt, damit de Läseabschnitt für sich verständlich isch; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 ohni Name; 032 hät en andere Wortlut, 05 hät da e Lugge."]),
 ("VAR-SBLGNTAPP-MAT-009-001-02:R2", "MAT.9.1", "in ein Boot", "in das Boot", "in es Boot", "is Boot", "gering",
  "Mit Artikel ist ein bestimmtes, schon bekanntes Boot gemeint.", "Mit Artikel isch es bestimmts, scho bekannts Boot gmeint.",
  {"R1": [("εἰς", "in ein", "WH, Treg, NA28")], "R2": [("εἰς τὸ", "in das", "RP")]},
  {"R1": [("εἰς", "in es", "WH, Treg, NA28")], "R2": [("εἰς τὸ", "is", "RP")]},
  ["Der Artikel kann auf das Boot aus [[MAT.8.23]] zurückverweisen und ergänzt sein, oder als unnötig weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne Artikel, 04 und 032 mit ihm; 05 hat hier eine Lücke."],
  ["De Artikel cha uf s Boot us [[MAT.8.23]] zruggwiise und ergänzt sii, oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni Artikel, 04 und 032 mit; 05 hät da e Lugge."]),
 ("VAR-SBLGNTAPP-MAT-009-004-01:R2", "MAT.9.4", "Jesus kannte ihre Gedanken", "Jesus sah ihre Gedanken", "de Jesus hät iri Gedanke kännt", "de Jesus hät iri Gedanke gseh", "mittel",
  "Statt «kannte» (εἰδώς) steht «sah» (ἰδών).", "Statt «kännt» (εἰδώς) staat «gseh» (ἰδών).",
  {"R1": [("εἰδὼς", "kannte", "WH, Treg, NIV")], "R2": [("ἰδὼν", "sah", "RP, NA28")]},
  {"R1": [("εἰδὼς", "hät kännt", "WH, Treg, NIV")], "R2": [("ἰδὼν", "hät gseh", "RP, NA28")]},
  ["Die beiden Formen klangen in der Aussprache der Zeit gleich (ει und ι) und unterscheiden sich in der Schrift nur durch einen Buchstaben. ἰδών kann an [[MAT.9.2]] («als Jesus … sah») angeglichen sein; ebenso kann εἰδώς eine Glättung sein, weil man Gedanken nicht «sieht». Der SBLGNT folgt hier WH, Treg und NIV gegen NA28 und RP.",
   "Laut der automatischen Zuordnung liest 03 εἰδώς, 01, 04, 032 und 05 lesen ἰδών."],
  ["Di beide Forme händ i de Ussprach vo dere Ziit gliich tönt und underscheided sich i de Schrift nu i eim Buechstabe. ἰδών cha a [[MAT.9.2]] aaglichen sii; oder εἰδώς glättet, wil me Gedanke nöd «gseht».",
   "Nach de automatische Zueornig liest 03 εἰδώς, 01, 04, 032 und 05 läsed ἰδών."]),
 ("VAR-SBLGNTAPP-MAT-009-008-01:R2", "MAT.9.8", "fürchteten sie sich", "staunten sie", "händ si Angscht übercho", "händ si gstuunt", "mittel",
  "Die Menge staunt, statt sich zu fürchten.", "D Lüüt stuuned, statt Angscht z übercho.",
  {"R1": [("ἐφοβήθησαν", "fürchteten sich", "WH, Treg, NA28")], "R2": [("ἐθαύμασαν", "staunten", "RP")]},
  {"R1": [("ἐφοβήθησαν", "händ Angscht übercho", "WH, Treg, NA28")], "R2": [("ἐθαύμασαν", "händ gstuunt", "RP")]},
  ["«Staunen» ist nach Heilungen geläufiger (vgl. [[MAT.9.33]]) und kann die ungewöhnlichere «Furcht» ersetzt haben; ebenso kann «fürchten» aus [[LUK.5.26]] stammen.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 05 ἐφοβήθησαν, 04 ἐθαύμασαν."],
  ["«Stuune» isch nach Heiligsgschichte gläufiger (vgl. [[MAT.9.33]]) und cha di ungwöhnlicheri «Angscht» ersetzt ha; oder «fürchte» chunnt us [[LUK.5.26]].",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 05 ἐφοβήθησαν, 04 ἐθαύμασαν."]),
 ("VAR-SBLGNTAPP-MAT-009-012-01:R2", "MAT.9.12", "Er aber hörte es", "Jesus aber hörte es", "Er aber hät s ghört", "De Jesus aber hät s ghört", "gering",
  "Der Name Jesus ist ausdrücklich genannt.", "De Name Jesus isch usdrücklich gnännt.",
  {"R1": [("δὲ", "aber", "WH, NA28")], "R2": [("δὲ Ἰησοῦς", "aber Jesus", "Treg, RP")]},
  {"R1": [("δὲ", "aber", "WH, NA28")], "R2": [("δὲ Ἰησοῦς", "aber de Jesus", "Treg, RP")]},
  ["Verdeutlichende Ergänzung des Namens bei Sprecherwechsel; ebenso möglich ist Wegfall.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 032 und 05 ohne den Namen."],
  ["Ergänzig vom Name bim Sprächerwächsel; oder Wägfall.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 032 und 05 ohni Name."]),
 ("VAR-SBLGNTAPP-MAT-009-012-02:R2", "MAT.9.12", "und sagte:", "und sagte zu ihnen:", "und gseit:", "und zu ine gseit:", "gering",
  "«Zu ihnen» ist ergänzt.", "«Zu ine» isch ergänzt.",
  {"R1": [("εἶπεν", "sagte", "WH, Treg, NA28")], "R2": [("εἶπεν αὐτοῖς", "sagte zu ihnen", "RP")]},
  {"R1": [("εἶπεν", "gseit", "WH, Treg, NA28")], "R2": [("εἶπεν αὐτοῖς", "zu ine gseit", "RP")]},
  ["Häufige verdeutlichende Ergänzung (vgl. [[MRK.2.17]] λέγει αὐτοῖς).",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 ohne αὐτοῖς, 032 mit ihm."],
  ["Hüüfigi Ergänzig zur Verdüütlichung (vgl. [[MRK.2.17]]).",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 ohni αὐτοῖς, 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-009-013-01:R2", "MAT.9.13", "sondern Sünder.", "sondern Sünder zur Umkehr.", "sondern Sünder.", "sondern Sünder zur Umkehr.", "mittel",
  "Der Zusatz nennt das Ziel des Rufens: die Umkehr.", "De Zuesatz nännt s Ziel vom Rüefe: d Umkehr.",
  {"R1": [("ἁμαρτωλούς", "Sünder", "WH, Treg, NA28")], "R2": [("ἁμαρτωλοὺς εἰς μετάνοιαν", "Sünder zur Umkehr", "RP")]},
  {"R1": [("ἁμαρτωλούς", "Sünder", "WH, Treg, NA28")], "R2": [("ἁμαρτωλοὺς εἰς μετάνοιαν", "Sünder zur Umkehr", "RP")]},
  ["«Zur Umkehr» steht in der Parallele [[LUK.5.32]] und kann daraus übernommen sein; ebenso könnte die Wendung in Matthäus weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 05 ohne Zusatz, 04 mit ihm."],
  ["«Zur Umkehr» staat i de Parallele [[LUK.5.32]] und cha drus übernoo sii; oder d Wändig isch im Matthäus usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 05 ohni Zuesatz, 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-009-014-01:R2", "MAT.9.14", "die Pharisäer oft", "die Pharisäer", "d Pharisäer vil", "d Pharisäer", "gering",
  "Ohne «oft» ist nur vom Fasten überhaupt die Rede.", "Ohni «vil» isch nu vom Faschte überhaupt d Red.",
  {"R1": [("πολλά", "oft", "Treg, RP, NA28")], "R2": [("–", "(fehlt)", "WH, NIV")]},
  {"R1": [("πολλά", "vil", "Treg, RP, NA28")], "R2": [("–", "(fehlt)", "WH, NIV")]},
  ["πολλά kann verstärkend ergänzt (vgl. πυκνά «oft» in [[LUK.5.33]]) oder beim Abschreiben übersprungen worden sein. Der SBLGNT folgt hier Treg, RP und NA28 gegen WH und NIV.",
   "Laut der automatischen Zuordnung lesen 04, 032 und 05 πολλά, 01 (auch die Korrektur) und 03 ohne."],
  ["πολλά cha verstärkend ergänzt (vgl. [[LUK.5.33]]) oder bim Abschriibe überspringe worde sii.",
   "Nach de automatische Zueornig läsed 04, 032 und 05 πολλά, 01 (au d Korrektur) und 03 ohni."]),
 ("VAR-SBLGNTAPP-MAT-009-017-01:R2", "MAT.9.17", "gehen verloren", "werden verloren gehen", "sind verlore", "wärded verlore gaa", "gering",
  "Futur statt Präsens.", "Futur statt Präsens.",
  {"R1": [("ἀπόλλυνται", "gehen verloren", "WH, Treg, NA28")], "R2": [("ἀπολοῦνται", "werden verloren gehen", "RP")]},
  {"R1": [("ἀπόλλυνται", "sind verlore", "WH, Treg, NA28")], "R2": [("ἀπολοῦνται", "wärded verlore gaa", "RP")]},
  ["Das Futur entspricht [[MRK.2.22]] in einem Teil der Überlieferung und [[LUK.5.37]]; ebenso kann das Präsens an die übrigen Präsensformen des Verses angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ἀπόλλυνται, 04 und 032 ἀπολοῦνται."],
  ["S Futur entspricht [[LUK.5.37]]; oder s Präsens isch a di andere Präsensforme vom Vers aaglichen.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ἀπόλλυνται, 04 und 032 ἀπολοῦνται."]),
 ("VAR-SBLGNTAPP-MAT-009-018-01:R2", "MAT.9.18", "da kam ein Vorsteher", "da trat ein Vorsteher heran", "da isch en Vorsteher choo", "da isch en Vorsteher härechoo", "gering",
  "Statt «kam» (ἐλθών) steht «trat heran» (προσελθών).", "Statt «isch choo» (ἐλθών) staat «isch härechoo» (προσελθών).",
  {"R1": [("ἐλθὼν", "kam", "Treg, NA28, RP")], "R2": [("προσελθὼν", "trat heran", "WH")]},
  {"R1": [("ἐλθὼν", "isch choo", "Treg, NA28, RP")], "R2": [("προσελθὼν", "isch härechoo", "WH")]},
  ["προσέρχομαι ist bei Matthäus häufig (vgl. [[MAT.8.2]]); die Formen können ineinander übergegangen sein. Der SBLGNT folgt hier Treg, NA28 und RP gegen WH.",
   "Laut der automatischen Zuordnung lesen 04, 032 und 05 ἐλθών, 01 (auch die Korrektur) und 03 προσελθών."],
  ["προσέρχομαι isch bim Matthäus hüüfig (vgl. [[MAT.8.2]]); d Forme chönd inenand übergange sii.",
   "Nach de automatische Zueornig läsed 04, 032 und 05 ἐλθών, 01 (au d Korrektur) und 03 προσελθών."]),
 ("VAR-SBLGNTAPP-MAT-009-024-01:R2", "MAT.9.24", "sagte er:", "sagt er zu ihnen:", "hät er gseit:", "seit er zu ine:", "gering",
  "Erzählendes Präsens mit «zu ihnen».", "Erzählends Präsens mit «zu ine».",
  {"R1": [("ἔλεγεν", "sagte er", "WH, Treg, NA28")], "R2": [("λέγει αὐτοῖς", "sagt er zu ihnen", "RP")]},
  {"R1": [("ἔλεγεν", "hät er gseit", "WH, Treg, NA28")], "R2": [("λέγει αὐτοῖς", "seit er zu ine", "RP")]},
  ["Das Imperfekt ohne Angabe der Angeredeten ist knapper; die längere Form kann verdeutlichen. Ebenso kann die kürzere Form eine Glättung sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ἔλεγεν, 04 und 032 λέγει αὐτοῖς."],
  ["S Imperfekt ohni Aagab, zu wem, isch chnapper; di lenger Form cha verdüütliche. Oder di chürzer Form glättet.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ἔλεγεν, 04 und 032 λέγει αὐτοῖς."]),
 ("VAR-SBLGNTAPP-MAT-009-032-01:R2", "MAT.9.32", "einen stummen Menschen", "einen Stummen", "en stumme Mänsch", "en Stumme", "gering",
  "Ohne ἄνθρωπον ist nur von einem Stummen die Rede.", "Ohni ἄνθρωπον isch nu vo eme Stumme d Red.",
  {"R1": [("ἄνθρωπον", "Menschen", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  {"R1": [("ἄνθρωπον", "Mänsch", "Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH")]},
  ["ἄνθρωπον kann verdeutlichend ergänzt oder als entbehrlich weggelassen worden sein. Der SBLGNT folgt hier Treg, NA28 und RP gegen WH.",
   "Laut der automatischen Zuordnung liest 05 ἄνθρωπον, 01, 03, 04 und 032 lesen ohne."],
  ["ἄνθρωπον cha zur Verdüütlichung ergänzt oder als unnötig wäggloo worde sii.",
   "Nach de automatische Zueornig liest 05 ἄνθρωπον, 01, 03, 04 und 032 läsed ohni."]),
 ("VAR-SBLGNTAPP-MAT-009-035-01:R2", "MAT.9.35", "jedes Leiden.", "jedes Leiden im Volk.", "jedes Liide gheilt.", "jedes Liide im Volk gheilt.", "gering",
  "«Im Volk» ist ergänzt.", "«Im Volk» isch ergänzt.",
  {"R1": [("μαλακίαν", "Leiden", "WH, Treg, NA28")], "R2": [("μαλακίαν ἐν τῷ λαῷ", "Leiden im Volk", "RP")]},
  {"R1": [("μαλακίαν", "Liide", "WH, Treg, NA28")], "R2": [("μαλακίαν ἐν τῷ λαῷ", "Liide im Volk", "RP")]},
  ["Der Zusatz gleicht an [[MAT.4.23]] an, wo der Satz mit «im Volk» endet.",
   "Laut der automatischen Zuordnung lesen 03, 04, 032 und 05 ohne Zusatz; die Erstschrift von 01 hat ihn, die Korrektur streicht ihn."],
  ["De Zuesatz glicht a [[MAT.4.23]] aa, wo de Satz mit «im Volk» ufhört.",
   "Nach de automatische Zueornig läsed 03, 04, 032 und 05 ohni Zuesatz; d Erschtschrift vo 01 hät en, d Korrektur striicht en."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
SEG9 = (SEG + " [[MAT.9.35]] nimmt [[MAT.4.23]] fast wörtlich auf; zusammen rahmen die beiden Verse die Bergpredigt und die "
        "Taten in Kapitel 8–9. [[MAT.9.35]]–[[MAT.9.38]] leiten zugleich zur Aussendungsrede in Kapitel 10 über.")
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-008-001-034", "MAT.8.1-MAT.8.34", "section", "Heilungen, Ruf in die Nachfolge und der Sturm auf dem See",
  ["TU-MAT-008-001-004", "TU-MAT-008-005-013", "TU-MAT-008-014-017", "TU-MAT-008-018-022", "TU-MAT-008-023-027", "TU-MAT-008-028-034"],
  "Als Jesus vom Berg herabsteigt, macht er einen Aussätzigen rein und schickt ihn zum Priester. In Kafarnaum bittet ein Hauptmann für seinen gelähmten Diener und sagt, ein Wort Jesu genüge; Jesus sagt, er habe bei niemandem in Israel einen so grossen Glauben gefunden, kündigt an, viele von Osten und Westen würden mit Abraham, Isaak und Jakob im Reich der Himmel zu Tisch liegen, und der Diener wird gesund. Im Haus des Petrus heilt Jesus dessen Schwiegermutter, am Abend treibt er Geister aus und heilt alle Kranken; der Erzähler sieht darin [[ISA.53.4]] erfüllt. Einem Schriftgelehrten und einem Jünger, die ihm folgen wollen, antwortet Jesus mit harten Worten über die Nachfolge. Auf dem See nennt er die verängstigten Jünger kleingläubig und fährt Winde und See an, und es wird still. Im Gebiet der Gadarener fahren die Dämonen zweier Besessener auf sein Wort in eine Schweineherde, die im See umkommt; die Stadt bittet ihn, ihr Gebiet zu verlassen.", SEG),
 ("TU-MAT-008-001-004", "MAT.8.1-MAT.8.4", "narrative", "Die Heilung eines Aussätzigen", None,
  "Als Jesus vom Berg herabsteigt, folgen ihm grosse Menschenmengen. Ein Aussätziger wirft sich vor ihm nieder und sagt, Jesus könne ihn rein machen, wenn er wolle. Jesus berührt ihn und sagt: «Ich will; werde rein!», und sogleich wird er rein. Jesus sagt ihm, er solle es niemandem sagen, sondern sich dem Priester zeigen und die Gabe darbringen, die Mose angeordnet hat, ihnen zum Zeugnis.", None),
 ("TU-MAT-008-005-013", "MAT.8.5-MAT.8.13", "narrative_with_saying", "Der Hauptmann von Kafarnaum", None,
  "In Kafarnaum bittet ein Hauptmann Jesus für seinen Diener, der gelähmt im Haus liegt und schrecklich gequält wird. Jesus antwortet, er werde kommen und ihn heilen. Der Hauptmann sagt, er sei nicht wert, dass Jesus unter sein Dach komme; Jesus solle nur ein Wort sprechen, denn auch er selbst stehe unter Befehlsgewalt, und seine Soldaten und sein Knecht täten, was er ihnen sage. Jesus staunt und sagt zu denen, die ihm folgen, er habe bei niemandem in Israel einen so grossen Glauben gefunden: Viele werden von Osten und Westen kommen und mit Abraham, Isaak und Jakob im Reich der Himmel zu Tisch liegen, die Söhne des Reiches aber werden in die äussere Finsternis hinausgeworfen. Zum Hauptmann sagt er: «Wie du geglaubt hast, soll dir geschehen», und in jener Stunde wird der Diener gesund.", None),
 ("TU-MAT-008-014-017", "MAT.8.14-MAT.8.17", "narrative", "Die Schwiegermutter des Petrus und viele Heilungen", None,
  "Im Haus des Petrus sieht Jesus dessen Schwiegermutter mit Fieber im Bett liegen; er berührt ihre Hand, das Fieber verlässt sie, und sie steht auf und dient ihm. Am Abend bringt man viele Besessene zu ihm; er treibt die Geister mit einem Wort aus und heilt alle Kranken. Der Erzähler sieht darin erfüllt, was durch den Propheten Jesaja gesagt ist: «Er selbst hat unsere Schwächen genommen und die Krankheiten getragen» ([[ISA.53.4]]).", None),
 ("TU-MAT-008-018-022", "MAT.8.18-MAT.8.22", "dialogue", "Vom Ernst der Nachfolge", None,
  "Als Jesus die vielen Menschenmengen um sich sieht, befiehlt er, ans andere Ufer aufzubrechen. Ein Schriftgelehrter sagt, er werde ihm folgen, wohin er auch gehe; Jesus antwortet, die Füchse hätten Höhlen und die Vögel Nester, der Menschensohn aber habe keinen Ort, wo er den Kopf hinlegen kann. Ein anderer Jünger bittet, zuerst seinen Vater begraben zu dürfen; Jesus sagt zu ihm: «Folge mir, und lass die Toten ihre Toten begraben!»", None),
 ("TU-MAT-008-023-027", "MAT.8.23-MAT.8.27", "narrative", "Die Stillung des Sturms", None,
  "Jesus steigt in ein Boot, und seine Jünger folgen ihm. Auf dem See entsteht ein grosses Beben, sodass die Wellen das Boot bedecken; er aber schläft. Die Jünger wecken ihn: «Herr, rette! Wir gehen zugrunde!» Er fragt sie, warum sie so furchtsam seien, und nennt sie Kleingläubige; dann steht er auf und fährt die Winde und den See an, und es wird eine grosse Stille. Die Menschen staunen und fragen, was für einer das sei, dass ihm sogar die Winde und der See gehorchen.", None),
 ("TU-MAT-008-028-034", "MAT.8.28-MAT.8.34", "narrative", "Die zwei Besessenen im Gebiet der Gadarener", None,
  "Am anderen Ufer, im Gebiet der Gadarener, kommen Jesus aus den Grabstätten zwei Besessene entgegen, so gefährlich, dass niemand den Weg dort benutzen kann. Sie schreien, was sie mit ihm zu tun hätten, dem Sohn Gottes, und ob er gekommen sei, sie vor der Zeit zu quälen. Weit weg von ihnen weidet eine Herde vieler Schweine; die Dämonen bitten, wenn er sie austreibe, solle er sie in die Herde schicken. Jesus sagt: «Geht!» Sie fahren in die Schweine, und die ganze Herde stürmt den Abhang hinunter in den See und kommt im Wasser um. Die Hirten fliehen und berichten in der Stadt alles, auch das von den Besessenen; die ganze Stadt kommt Jesus entgegen und bittet ihn, aus ihrem Gebiet wegzugehen.", None),
 ("TU-MAT-009-001-038", "MAT.9.1-MAT.9.38", "section", "Vollmacht zu vergeben, Mahl mit Sündern und weitere Heilungen",
  ["TU-MAT-009-001-008", "TU-MAT-009-009-013", "TU-MAT-009-014-017", "TU-MAT-009-018-026", "TU-MAT-009-027-031", "TU-MAT-009-032-034", "TU-MAT-009-035-038"],
  "Zurück in seiner Stadt sagt Jesus einem Gelähmten, seine Sünden seien vergeben; gegen den Vorwurf der Lästerung heilt er ihn, damit man wisse, dass der Menschensohn Vollmacht hat, auf der Erde Sünden zu vergeben, und die Menschenmengen preisen Gott. Er ruft Matthäus von der Zollstelle in die Nachfolge, liegt mit Zöllnern und Sündern zu Tisch und antwortet den Pharisäern mit [[HOS.6.6]]: Er sei nicht gekommen, Gerechte zu rufen, sondern Sünder. Den Jüngern des Johannes sagt er, die Hochzeitsgäste könnten nicht trauern, solange der Bräutigam bei ihnen ist, und spricht von Flicken und Weinschläuchen. Ein Vorsteher bittet für seine eben gestorbene Tochter; unterwegs wird eine Frau, die seit zwölf Jahren an Blutfluss leidet, durch die Berührung seines Mantels gerettet, und im Haus ergreift Jesus die Hand des Mädchens, und es steht auf. Er öffnet zwei Blinden die Augen und befreit einen Stummen von einem Dämon; die Pharisäer sagen, er treibe die Dämonen durch den Herrscher der Dämonen aus. Jesus zieht lehrend, verkündigend und heilend durch Städte und Dörfer; er hat Erbarmen mit den Menschenmengen und sagt den Jüngern, sie sollen den Herrn der Ernte um Arbeiter bitten.", SEG9),
 ("TU-MAT-009-001-008", "MAT.9.1-MAT.9.8", "narrative_with_saying", "Die Heilung eines Gelähmten", None,
  "Jesus fährt hinüber in seine Stadt. Man bringt einen Gelähmten auf einem Bett zu ihm; als Jesus ihren Glauben sieht, sagt er: «Sei getrost, Kind! Deine Sünden sind vergeben.» Einige Schriftgelehrte sagen bei sich, er lästere. Jesus kennt ihre Gedanken und fragt, was leichter sei zu sagen: «Deine Sünden sind vergeben» oder «Steh auf und geh umher». Damit sie wissen, dass der Menschensohn Vollmacht hat, auf der Erde Sünden zu vergeben, sagt er zum Gelähmten, er solle aufstehen, sein Bett nehmen und in sein Haus gehen; der steht auf und geht. Die Menschenmengen fürchten sich und preisen Gott, der den Menschen solche Vollmacht gegeben hat.", None),
 ("TU-MAT-009-009-013", "MAT.9.9-MAT.9.13", "narrative_with_saying", "Die Berufung des Matthäus und das Mahl mit Zöllnern", None,
  "Jesus sieht einen Menschen namens Matthäus an der Zollstelle sitzen und sagt zu ihm: «Folge mir!»; der steht auf und folgt ihm. Als Jesus im Haus zu Tisch liegt, kommen viele Zöllner und Sünder und liegen mit ihm und seinen Jüngern zu Tisch. Die Pharisäer fragen seine Jünger, warum ihr Lehrer mit den Zöllnern und Sündern esse. Jesus hört es und antwortet: Nicht die Gesunden brauchen einen Arzt, sondern die Kranken; sie sollen lernen, was es heisst: «Barmherzigkeit will ich und nicht Opfer» ([[HOS.6.6]]); er sei nicht gekommen, Gerechte zu rufen, sondern Sünder.", None),
 ("TU-MAT-009-014-017", "MAT.9.14-MAT.9.17", "dialogue", "Die Frage nach dem Fasten", None,
  "Die Jünger des Johannes fragen Jesus, warum sie und die Pharisäer oft fasten, seine Jünger aber nicht. Jesus antwortet, die Hochzeitsgäste könnten nicht trauern, solange der Bräutigam bei ihnen ist; es werden aber Tage kommen, wenn der Bräutigam von ihnen weggenommen wird, und dann werden sie fasten. Niemand setze einen Flicken aus ungewalktem Stoff auf ein altes Kleid, und niemand fülle jungen Wein in alte Schläuche; jungen Wein fülle man in neue Schläuche, und beide bleiben erhalten.", None),
 ("TU-MAT-009-018-026", "MAT.9.18-MAT.9.26", "narrative", "Die Tochter des Vorstehers und die Frau mit dem Blutfluss", None,
  "Während Jesus redet, wirft sich ein Vorsteher vor ihm nieder: Seine Tochter sei eben gestorben, aber wenn Jesus ihr die Hand auflege, werde sie leben. Jesus steht auf und folgt ihm mit seinen Jüngern. Eine Frau, die seit zwölf Jahren an Blutfluss leidet, berührt von hinten den Saum seines Mantels, denn sie sagt sich, sie werde gerettet, wenn sie nur seinen Mantel berühre. Jesus wendet sich um und sagt: «Sei getrost, Tochter! Dein Glaube hat dich gerettet»; von jener Stunde an ist die Frau gerettet. Im Haus des Vorstehers schickt Jesus die Flötenspieler und die lärmende Menge weg, denn das Mädchen sei nicht gestorben, sondern schlafe; sie lachen ihn aus. Als die Menge hinausgetrieben ist, geht er hinein, ergreift die Hand des Mädchens, und es steht auf. Die Kunde davon verbreitet sich in jener ganzen Gegend.", None),
 ("TU-MAT-009-027-031", "MAT.9.27-MAT.9.31", "narrative", "Die Heilung zweier Blinder", None,
  "Zwei Blinde folgen Jesus und schreien: «Erbarme dich unser, Sohn Davids!» Im Haus fragt er sie, ob sie glauben, dass er das tun kann; sie antworten: «Ja, Herr.» Er berührt ihre Augen und sagt: «Nach eurem Glauben soll euch geschehen», und ihre Augen werden geöffnet. Jesus fährt sie hart an, niemand dürfe es erfahren; sie aber gehen hinaus und machen ihn in jener ganzen Gegend bekannt.", None),
 ("TU-MAT-009-032-034", "MAT.9.32-MAT.9.34", "narrative", "Ein stummer Besessener", None,
  "Man bringt einen stummen Menschen zu Jesus, der besessen ist. Als der Dämon ausgetrieben ist, redet der Stumme; die Menschenmengen staunen und sagen, so etwas habe sich in Israel noch nie gezeigt. Die Pharisäer aber sagen, er treibe die Dämonen durch den Herrscher der Dämonen aus.", None),
 ("TU-MAT-009-035-038", "MAT.9.35-MAT.9.38", "narrative_with_saying", "Die Ernte ist gross", None,
  "Jesus zieht durch alle Städte und Dörfer, lehrt in ihren Synagogen, verkündigt das Evangelium vom Reich und heilt jede Krankheit und jedes Leiden. Als er die Menschenmengen sieht, hat er Erbarmen mit ihnen, denn sie sind geschunden und hilflos wie Schafe, die keinen Hirten haben. Er sagt zu seinen Jüngern, die Ernte sei gross, die Arbeiter aber wenige; sie sollen den Herrn der Ernte bitten, Arbeiter in seine Ernte auszusenden.", None),
]
UNITS_GSW = {
 "TU-MAT-008-001-034": ("Heilige, Ruef zum Nachegaa und de Sturm uf em See", "Won de Jesus vom Bärg abestiigt, macht er en Ussätzige rein und schickt en zum Prieschter. Z Kafarnaum bittet en Hauptmaa für sin glähmte Diener und seit, es Wort vom Jesus längi; de Jesus seit, er heig bi niemertem in Israel eso en grosse Glaube gfunde, seit aa, vili vo Oschte und Weschte wärdid mit em Abraham, em Isaak und em Jakob im Riich vo de Himel am Tisch ligge, und de Diener wird gsund. Im Huus vom Petrus heilt de Jesus däm sini Schwigermueter, am Aabig tribt er Geischter us und heilt alli Chranke; de Erzäler gseht drin [[ISA.53.4]] erfüllt. Eme Schriftgelehrte und eme Jünger, wo ihm wänd nachegaa, antwortet de Jesus mit herte Wort übers Nachegaa. Uf em See nännt er di verängschtete Jünger chliigläubig und faart d Wind und de See aa, und es wird still. Im Gebiet vo de Gadarener fahred d Dämone vo zwei Bsässne uf sis Wort i e Söiherde, wo im See umchunnt; d Stadt bittet en, us irem Gebiet wägzgaa."),
 "TU-MAT-008-001-004": ("D Heilig vo eme Ussätzige", "Won de Jesus vom Bärg abestiigt, gönd ihm vil Lüüt nache. En Ussätzige wirft sich vor ihm nider und seit, de Jesus chönn en rein mache, wänn er well. De Jesus rüert en aa und seit: «Ich wott; wird rein!», und grad wird er rein. De Jesus seit em, er söll s niemertem säge, sondern sich em Prieschter zeige und d Gaab darbringe, wo de Mose aagordnet hät, ine zum Zügnis."),
 "TU-MAT-008-005-013": ("De Hauptmaa vo Kafarnaum", "Z Kafarnaum bittet en Hauptmaa de Jesus für sin Diener, wo glähmt im Huus liit und schrecklich plaget wird. De Jesus antwortet, er chömm und heil en. De Hauptmaa seit, er sig nöd wärt, dass de Jesus under sis Dach chömm; er söll nu es Wort säge, dänn au er sälber stöng under Befehlsgwalt, und sini Soldate und sin Chnächt mached, was er ine säg. De Jesus stuunt und seit zu dene, wo ihm nachegönd, er heig bi niemertem in Israel eso en grosse Glaube gfunde: Vili wärded vo Oschte und Weschte choo und mit em Abraham, em Isaak und em Jakob im Riich vo de Himel am Tisch ligge, d Söhn vom Riich aber wärded i di üsser Fiischteri usegworfe. Zum Hauptmaa seit er: «Wie du glaubt häsch, söll dir gscheh», und i dere Stund wird de Diener gsund."),
 "TU-MAT-008-014-017": ("D Schwigermueter vom Petrus und vil Heilige", "Im Huus vom Petrus gseht de Jesus däm sini Schwigermueter mit Fieber im Bett ligge; er rüert ire Hand aa, s Fieber verlaat si, und si staat uf und dienet ihm. Am Aabig bringed s vil Bsässne zu ihm; er tribt d Geischter mit eme Wort us und heilt alli Chranke. De Erzäler gseht drin erfüllt, was dur de Prophet Jesaja gseit worden isch: «Er sälber hät öisi Schwäche gnoo und d Chrankete treit» ([[ISA.53.4]])."),
 "TU-MAT-008-018-022": ("Vom Ärnscht vom Nachegaa", "Won de Jesus di vile Lüüt um sich gseht, befiehlt er, as ander Ufer ufzbreche. En Schriftgelehrte seit, er gangi ihm nache, wo er au hiigangi; de Jesus antwortet, d Füchs heigid Hööline und d Vögel Näschter, de Mänschesohn aber heig kein Ort, wo er de Chopf chönn anelegge. En andere Jünger bittet, zerscht sin Vatter dörfe z beerdige; de Jesus seit zu ihm: «Chumm mir nache, und la d Tote iri Tote beerdige!»"),
 "TU-MAT-008-023-027": ("De Sturm wird still", "De Jesus stiigt in es Boot, und sini Jünger gönd ihm nache. Uf em See chunnt es grosses Bebe, so dass d Wälle s Boot zuedecked; er aber schlaft. D Jünger wecked en: «Herr, rett! Mir gönd under!» Er fröget si, werum si so ängschtlich sigid, und nännt si Chliigläubigi; dänn staat er uf und faart d Wind und de See aa, und es wird ganz still. D Mänsche stuuned und fröged, was dä für eine sig, dass ihm sogar d Wind und de See folged."),
 "TU-MAT-008-028-034": ("Di zwei Bsässne im Gebiet vo de Gadarener", "Am andere Ufer, im Gebiet vo de Gadarener, chömed em Jesus us de Greber zwei Bsässni entgäge, so gföörlich, dass niemert dört de Wäg cha bruuche. Si schreied, was si mit ihm z tue heigid, em Sohn vo Gott, und öb er choo sig, für si vor de Ziit z quäle. Wiit wäg vo ine weidet e Herde vo vile Söi; d Dämone bitted, wänn er si ustriibi, söll er si i d Herde schicke. De Jesus seit: «Gönd!» Si fahred i d Söi, und di ganz Herde stürmt de Abhang abe i de See und stirbt im Wasser. D Hirte fliehed und verzelled i de Stadt alles, au das mit de Bsässne; di ganz Stadt chunnt em Jesus entgäge und bittet en, us irem Gebiet wägzgaa."),
 "TU-MAT-009-001-038": ("Vollmacht zum Vergää, Ässe mit Sünder und wiiteri Heilige", "Wider i sinere Stadt seit de Jesus eme Glähmte, sini Sünde sigid vergää; gäge de Vorwurf vo de Läschterig heilt er en, damit me weiss, dass de Mänschesohn Vollmacht hät, uf de Ärde Sünde z vergää, und d Lüüt priised Gott. Er rüeft de Matthäus vo de Zollstell, ihm nachezgaa, liit mit Zöllner und Sünder am Tisch und antwortet de Pharisäer mit [[HOS.6.6]]: Er sig nöd choo, für Grächti z rüefe, sondern Sünder. De Jünger vom Johannes seit er, d Hochziitsgäscht chönned nöd truure, solang de Brüütigam bi ine isch, und redt vo Blätz und Wiischlüüch. En Vorsteher bittet für sini Tochter, wo äbe gstorbe isch; underwägs wird e Frau, wo sit zwölf Jahr a Bluetfluss liidet, dur s Aarüere vo sim Mantel grettet, und im Huus nimmt de Jesus s Meitli a de Hand, und es staat uf. Er macht zwei Blinde d Auge uf und befreit en Stumme vo eme Dämon; d Pharisäer säged, er triibi d Dämone dur de Herrscher vo de Dämone us. De Jesus ziet lehrend, verchündend und heilend dur Stedt und Dörfer; er hät Erbarme mit de Lüüt und seit de Jünger, si söled de Herr vo de Ärn um Arbeiter bitte."),
 "TU-MAT-009-001-008": ("D Heilig vo eme Glähmte", "De Jesus faart übere i sini Stadt. Si bringed en Glähmte uf eme Bett zu ihm; won de Jesus ire Glaube gseht, seit er: «Häb Muet, Chind! Dini Sünde sind vergää.» Es paar Schriftgelehrti säged bi sich, er läschteri. De Jesus kännt iri Gedanke und fröget, was liechter sig z säge: «Dini Sünde sind vergää» oder «Stand uf und lauf umenand». Damit si wüssed, dass de Mänschesohn Vollmacht hät, uf de Ärde Sünde z vergää, seit er zum Glähmte, er söll ufstaa, sis Bett neh und heigaa; dä staat uf und gaat. D Lüüt händ Angscht und priised Gott, wo de Mänsche so e Vollmacht gää hät."),
 "TU-MAT-009-009-013": ("De Matthäus wird grüeft, und s Ässe mit de Zöllner", "De Jesus gseht en Mänsch, wo Matthäus heisst, a de Zollstell hocke und seit zu ihm: «Chumm mir nache!»; dä staat uf und gaat ihm nache. Won de Jesus im Huus am Tisch liit, chömed vil Zöllner und Sünder und ligged mit ihm und sine Jünger am Tisch. D Pharisäer fröged sini Jünger, werum ire Lehrer mit de Zöllner und Sünder ässi. De Jesus ghört s und antwortet: Nöd di Gsunde bruuched en Dokter, sondern di Chranke; si söled lerne, was das heisst: «Barmhärzigkeit wott ich und nöd Opfer» ([[HOS.6.6]]); er sig nöd choo, für Grächti z rüefe, sondern Sünder."),
 "TU-MAT-009-014-017": ("D Frag nach em Faschte", "D Jünger vom Johannes fröged de Jesus, werum si und d Pharisäer vil faschted, sini Jünger aber nöd. De Jesus antwortet, d Hochziitsgäscht chönned nöd truure, solang de Brüütigam bi ine isch; es chömed aber Täg, wo de Brüütigam vo ine weggnoo wird, und dänn wärded si faschte. Niemert setz en Blätz vo nöd iiglaufnem Tuech uf es alts Chleid, und niemert tüeg nöie Wii i alti Schlüüch; nöie Wii tuet me i nöii Schlüüch, und beidi bliibed erhalte."),
 "TU-MAT-009-018-026": ("D Tochter vom Vorsteher und d Frau mit em Bluetfluss", "Wäred de Jesus redt, wirft sich en Vorsteher vor ihm nider: Sini Tochter sig äbe gstorbe, aber wänn de Jesus ere d Hand ufleg, wärdi si läbe. De Jesus staat uf und gaat mit sine Jünger mit ihm. E Frau, wo sit zwölf Jahr a Bluetfluss liidet, rüert vo hine de Saum vo sim Mantel aa, dänn si seit bi sich, si wärdi grettet, wänn si nu sin Mantel aarüeri. De Jesus dräit sich um und seit: «Häb Muet, Tochter! Din Glaube hät dich grettet»; vo dere Stund aa isch d Frau grettet. Im Huus vom Vorsteher schickt de Jesus d Flöötespiler und d Mängi, wo Lärm macht, wäg, dänn s Meitli sig nöd gstorbe, sondern schlafi; si lached en us. Wo d Mängi usegschickt isch, gaat er ine, nimmt s Meitli a de Hand, und es staat uf. D Nachricht verbreitet sich i dere ganze Gegend."),
 "TU-MAT-009-027-031": ("Zwei Blindi wärded gheilt", "Zwei Blindi gönd em Jesus nache und schreied: «Häb Erbarme mit üs, Sohn vo David!» Im Huus fröget er si, öb si glaubed, dass er das cha mache; si antworted: «Ja, Herr.» Er rüert iri Auge aa und seit: «Nach eurem Glaube söll eu gscheh», und iri Auge gönd uf. De Jesus schnauzt si hert aa, niemert dörf s erfahre; si aber gönd use und mached en i dere ganze Gegend bekannt."),
 "TU-MAT-009-032-034": ("En stumme Bsässne", "Si bringed en stumme Mänsch zum Jesus, wo bsässe isch. Wo de Dämon ustribe isch, redt de Stumm; d Lüüt stuuned und säged, so öppis heig me in Israel no nie gseh. D Pharisäer aber säged, er triibi d Dämone dur de Herrscher vo de Dämone us."),
 "TU-MAT-009-035-038": ("D Ärn isch gross", "De Jesus ziet dur alli Stedt und Dörfer, lehrt i irne Synagoge, verchündet s Evangelium vom Riich und heilt jedi Chranket und jedes Liide. Won er d Lüüt gseht, hät er Erbarme mit ine, wil si gschunde und hilflos sind wie Schaf, wo kein Hirt händ. Er seit zu sine Jünger, d Ärn sig zwar gross, d Arbeiter aber wenig; si söled de Herr vo de Ärn bitte, dass er Arbeiter i sini Ärn usschickt."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "In Kapitel 8–9 stimmen die Zuordnungen der Ausgaben (ED-RP, ED-WH) mit den Sigla des Apparats überein."),
 ("Grundlage sind die gemeinsamen Matthäus-Wiedergaben (Reich der Himmel, Menschensohn, «Amen, ich sage euch», «siehe», "
  "«sogleich», «da» für τότε, Schriftgelehrte, Pharisäer, Besessener, Dämon, Erfüllungsformel). Wo Matthäus dieselbe "
  "griechische Wendung hat wie Markus (Parallelen [[MRK.1.29]]–[[MRK.1.45]], [[MRK.2.1]]–[[MRK.2.22]], "
  "[[MRK.4.35]]–[[MRK.5.43]]), ist der Wortlaut der Markus-Übersetzung angeglichen; wo er anders formuliert, folgt die "
  "Übersetzung seinem Text (z. B. «Beben» statt «Sturmwind», «trauern» statt «fasten», «Kleingläubige»)."),
 ("In diesem Bereich festgelegte Wiedergaben (für die übrigen Matthäus-Kapitel vorgeschlagen): πίστις / πιστεύω «Glaube» / "
  "«glauben»; ὀλιγόπιστοι «ihr Kleingläubigen»; θεραπεύω «heilen», ἰάομαι «gesund werden», σῴζω «retten»; "
  "προσκυνέω «sich niederwerfen» (mit Gott als Empfänger «anbeten»); προσέρχομαι «herantreten»; ἀκολουθέω «folgen»; κύριε «Herr», διδάσκαλε «Lehrer»; "
  "ὄχλος «die Menge», ὄχλοι «die Menschenmengen»; ἐξουσία «Vollmacht»; λεπρός «Aussätziger», καθαρίζω «rein machen»; "
  "θάλασσα (See Gennesaret) «See»; τελῶναι «Zöllner», ἁμαρτωλοί «Sünder»; ἀνάκειμαι «zu Tisch liegen»; δίκαιος «gerecht»; "
  "ἔλεος «Barmherzigkeit»; τὸ εὐαγγέλιον τῆς βασιλείας «das Evangelium vom Reich»; σπλαγχνίζομαι «Erbarmen haben»; "
  "ἐμβριμάομαι «hart anfahren»; ἐπιτιμάω «anfahren»; ὁ ἄρχων τῶν δαιμονίων «der Herrscher der Dämonen»; Θάρσει «Sei getrost»; "
  "ὅρα «sieh zu» (nicht «siehe», das ἰδού vorbehalten ist); ὁ κλαυθμὸς καὶ ὁ βρυγμὸς τῶν ὀδόντων «das Weinen und das "
  "Zähneknirschen»."),
 ("Erzählweise und Redegrenzen: Das erzählende Präsens (λέγει «sagt») ist beibehalten. ὅτι vor direkter Rede ist nicht "
  "eigens übersetzt. Anführungszeichen sind eine Entscheidung der Übersetzung, denn das Griechische hat keine. Reden, die über "
  "mehrere Verse laufen, bleiben in einem Anführungszeichen ([[MAT.8.8]]–[[MAT.8.9]], [[MAT.8.10]]–[[MAT.8.12]], "
  "[[MAT.9.4]]–[[MAT.9.6]], [[MAT.9.12]]–[[MAT.9.13]], [[MAT.9.15]]–[[MAT.9.17]], [[MAT.9.37]]–[[MAT.9.38]])."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT gegen einzelne Ausgaben liest (z. B. [[MAT.8.18]] "
  "πολλοὺς ὄχλους mit Treg und RP gegen WH und NA28; [[MAT.9.4]] εἰδώς mit WH, Treg und NIV gegen NA28 und RP; "
  "[[MAT.9.14]] πολλά). Abweichende Lesarten stehen als Alternativen, soweit sie die Übersetzung verändern. Nicht aufgeführt "
  "sind Varianten, die im Deutschen gleich lauten (Kasus beim Partizip, Wortstellung, Aussprache- und Formvarianten, "
  "Präsens/Perfekt bei «sind vergeben», Imperfekt/Aorist bei «folgte»): [[MAT.8.1]], [[MAT.8.5]], [[MAT.8.7]] (καί), "
  "[[MAT.8.8]], [[MAT.8.13]] (καί), [[MAT.8.27]], [[MAT.8.28]] (Kasus), [[MAT.8.34]], [[MAT.9.2]], [[MAT.9.4]] (ὑμεῖς), "
  "[[MAT.9.5]], [[MAT.9.6]], [[MAT.9.10]], [[MAT.9.11]], [[MAT.9.19]], [[MAT.9.22]], [[MAT.9.27]], [[MAT.9.30]], [[MAT.9.36]]."),
 ("Im SBLGNT fehlt in Kapitel 8–9 kein Vers. [[MAT.9.34]] fehlt nach der CNTR-Transkription in 05 (Codex Bezae); der "
  "SBLGNT-Apparat verzeichnet dort keine Variante, deshalb steht der Befund in decisions und nicht als Alternative."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig. Eigeti Formulierig; nöd us ere veröffentlichte Mundart-Bible übernoo.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Gmeinsami Matthäus-Wiedergabe: «s Riich vo de Himel», «de Mänschesohn», «Amen, ich säg eu», «lueg» (ἰδού), «grad» "
  "(εὐθέως), «dänn» (τότε), «Schriftgelehrti», «Bsässne», «Dämon», «damit erfüllt wird, was … dur de Prophet gseit worden "
  "isch». Im Bereich 8–9 neu: πίστις «Glaube»; ὀλιγόπιστοι «ir Chliigläubige»; θεραπεύω «heile», ἰάομαι «gsund wärde», "
  "σῴζω «rette»; προσκυνέω «sich niderwärfe» (mit Gott als Empfänger «aabätte»); προσέρχομαι «härechoo»; ἀκολουθέω «nachegaa»; ὄχλος «d Mängi», ὄχλοι «d Lüüt»; ὅρα «pass uf»; "
  "ἄρτι «äbe» (nöd «grad», das ghört εὐθέως); ὁ κλαυθμὸς καὶ ὁ βρυγμὸς τῶν ὀδόντων «s Hüüle und s Zändchnirsche»; θάλασσα «See»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Petrus»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«d Herde vo de Söi»); «damit» (wie i de gmeinsame Matthäus-Formle) statt «demit»; Schriibig «Himel» wie im Unservatter."),
 ("Text: D Übersetzig folgt de SBLGNT-Token. Im SBLGNT fählt i Kapitel 8–9 kein Vers; [[MAT.9.34]] fählt nach de "
  "CNTR-Transkription i 05, de Apparat hät aber kei Variante."),
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
        if len(refs_c) != last or max(int(r.split(".")[2]) for r in toks) != last:
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
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; Leitwörter einheitlich (gemeinsame Matthäus-Wiedergaben, Grundentscheide in translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": f"« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt ({TOOL}).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 8–9 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
