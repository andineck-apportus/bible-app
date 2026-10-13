#!/usr/bin/env python3
"""Autorenwerkzeug: Markus 1,1–3,19 – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/markus_text_01_03.py

Muster: scripts/authoring/philipper_text.py. Die Übersetzung steht als Auszeichnung je Vers (siehe _lib.py); Text und
Wortzuordnung entstehen daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins
revision_log.

Abgrenzung: Mk 3,20–35 ist bereits übersetzt (TRANS-MRK-003-020-021-DE-WORKING, TRANS-MRK-003-022-030-DE-WORKING,
TRANS-MRK-003-031-035-DE-WORKING, TRANS-MRK-003-020-035-GSW-ZH-WORKING; Texteinheiten TU-MRK-003-020-035 usw.). Dieses
Werkzeug schreibt für Kapitel 3 nur 3,1–19 und berührt jene Datensätze nicht. WORK-MRK besteht und wird nur referenziert.

KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben in den Lesarten stammen aus der maschinellen Zuordnung
(METHOD-AUTO-COLLATION-V1, data/witness-readings/WREAD-CNTR-MRK-*) bzw. aus dem dort erfassten Wortlaut der
CNTR-Transkription, nicht aus eigener Prüfung der Handschriften.
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
CHAPTERS = ((1, 45), (2, 28), (3, 19))  # Kapitel 3 nur bis Vers 19; 3,20–35 besteht schon

DE = {
 # ------------------------------------------------------------ Kapitel 1
 "MRK.1.1": "Anfang{1} [des Evangeliums]{2,3} [von Jesus]{4} Christus{5}.",
 "MRK.1.2": "Wie{1} [geschrieben steht]{2} [bei]{3} Jesaja{4,5}, [dem Propheten]{6,7}: «Siehe{8}, [ich sende]{9} [meinen]{12} [Boten]{10,11} [vor dir her]{13-15:idiom}, [der]{16} [deinen]{20} [Weg]{18,19} [bereiten wird]{17};",
 "MRK.1.3": "[Stimme]{1} [eines Rufenden]{2} [in]{3} [der Wüste]{4,5}: ‹[Bereitet]{6} [den Weg]{7,8} [des Herrn]{9}, [macht]{11} [seine]{14} [Pfade]{12,13} gerade{10}!›»",
 "MRK.1.4": "So [trat]{1} Johannes{2} [der Täufer]{3,4} [in]{5} [der Wüste]{6,7} [auf]{1} [und verkündigte]{8} [eine Taufe]{9} [der Umkehr]{10} [zur]{11} [Vergebung]{12} [der Sünden]{13}.",
 "MRK.1.5": "Und{1} [es zog]{2} [das ganze]{5,6} Land{8} Judäa{7} und{9} [alle]{12} [Jerusalemer]{10,11} [zu]{3} [ihm]{4} [hinaus]{2}, und{13} [sie liessen sich]{14} [von]{15} [ihm]{16} [im]{17,18} [Fluss]{20} Jordan{19} [taufen]{14} [und bekannten]{21} [ihre]{24} [Sünden]{22,23}.",
 "MRK.1.6": "Und{1} Johannes{3,4} [war]{2} [bekleidet mit]{5} [Kamelhaaren]{6,7} und{8} [einem ledernen]{10} [Gurt]{9} [um]{11} [seine]{14} [Hüften]{12,13}, und{15} [er ass]{16} [Heuschrecken]{17} und{18} [wilden]{20} [Honig]{19}.",
 "MRK.1.7": "Und{1} [er verkündigte]{2} [und sagte]{3}: «[Nach]{8} [mir]{9} [kommt]{4} [der]{5}, [der stärker ist]{6} [als ich]{7}; [ich bin]{12} nicht{11} [wert]{13}, [mich zu bücken]{14} und [ihm]{10} [den Riemen]{16,17} [seiner]{20} [Sandalen]{18,19} [zu lösen]{15}.",
 "MRK.1.8": "Ich{1} [habe]{2} [euch]{3} [mit Wasser]{4} [getauft]{2}, er{5} aber{6} [wird]{7} [euch]{8} [mit]{9} [heiligem]{11} [Geist]{10} [taufen]{7}.»",
 "MRK.1.9": "Und{1} [es geschah]{2} [in]{3} [jenen]{4} [Tagen]{5,6}, [da kam]{7} Jesus{8} [von]{9} Nazaret{10} [in Galiläa]{11,12} und{13} [liess sich]{14} [von]{18} Johannes{19} [im]{15,16} Jordan{17} [taufen]{14}.",
 "MRK.1.10": "Und{1} sogleich{2}, [als er]{3} [aus]{4} [dem Wasser]{5,6} [heraufstieg]{3}, [sah er]{7} [die Himmel]{9,10} [aufreissen]{8} und{11} [den Geist]{12,13} [wie]{14} [eine Taube]{15} [auf]{17} [ihn]{18} [herabkommen]{16}.",
 "MRK.1.11": "Und{1} [eine Stimme]{2} [kam]{3} [aus]{4} [den Himmeln]{5,6}: «Du{7} bist{8} [mein]{11} [geliebter]{12,13} [Sohn]{9,10}; [an]{14} [dir]{15} [habe ich Gefallen gefunden]{16}.»",
 "MRK.1.12": "Und{1} sogleich{2} [treibt]{6} [ihn]{5} [der Geist]{3,4} [hinaus]{6} [in]{7} [die Wüste]{8,9}.",
 "MRK.1.13": "Und{1} [er war]{2} [in]{3} [der Wüste]{4,5} [vierzig]{6} Tage{7} [und wurde]{8} [vom]{9,10} Satan{11} [versucht]{8}, und{12} [er war]{13} [bei]{14} [den wilden Tieren]{15,16}, und{17} [die Engel]{18,19} [dienten]{20} [ihm]{21}.",
 "MRK.1.14": "Und{1} [nachdem]{2,3} Johannes{5,6} [ausgeliefert worden war]{4}, [kam]{7} Jesus{8,9} [nach]{10} Galiläa{11,12} [und verkündigte]{13} [das Evangelium]{14,15} [Gottes]{16,17}",
 "MRK.1.15": "und{1} [sagte]{2}: «[Die Zeit]{5,6} [ist erfüllt]{4}, und{7} [das Reich]{9,10} [Gottes]{11,12} [ist nahe gekommen]{8}. [Kehrt um]{13} und{14} [glaubt]{15} [an]{16} [das Evangelium]{17,18}!» ~3(leitet die direkte Rede ein)",
 "MRK.1.16": "Und{1} [als er]{2} [am]{3,4} [See]{5} [von Galiläa]{6,7} [entlangging]{2}, [sah er]{8} Simon{9} und{10} Andreas{11}, [den Bruder]{12,13} [Simons]{14}, [wie sie]{15} [im]{16,17} [See]{18} [ihre Netze auswarfen]{15}; [sie waren]{19} nämlich{20} Fischer{21}.",
 "MRK.1.17": "Und{1} Jesus{4,5} [sagte]{2} [zu ihnen]{3}: «[Kommt]{6} [mir]{8} [nach]{7}, und{9} [ich werde]{10} [euch]{11} [zu]{12} [Menschenfischern]{13,14} [machen]{10}.»",
 "MRK.1.18": "Und{1} sogleich{2} [liessen sie]{3} [die Netze]{4,5} [liegen]{3} [und folgten]{6} [ihm]{7}.",
 "MRK.1.19": "Und{1} [als er]{2} [ein wenig]{3} [weiterging]{2}, [sah er]{4} Jakobus{5}, [den Sohn]{6,7} [des Zebedäus]{8}, und{9} Johannes{10}, [seinen]{13} [Bruder]{11,12}; und{14} sie{15} waren [im]{16,17} [Boot]{18} [und richteten]{19} [die Netze]{20,21} [her]{19}.",
 "MRK.1.20": "Und{1} sogleich{2} [rief er]{3} sie{4}. Und{5} [sie liessen]{6} [ihren]{9} [Vater]{7,8} Zebedäus{10} [mit]{14} [den Tagelöhnern]{15,16} [im]{11,12} [Boot]{13} [zurück]{6} [und gingen]{17} [ihm]{19} [nach]{18}.",
 "MRK.1.21": "Und{1} [sie kommen]{2} [nach]{3} Kafarnaum{4}. Und{5} sogleich{6} [am Sabbat]{7,8} [lehrte er]{9} [in]{10} [der Synagoge]{11,12}.",
 "MRK.1.22": "Und{1} [sie waren überwältigt]{2} [von]{3} [seiner]{6} [Lehre]{4,5}; denn{8} [er lehrte]{7,9} [sie]{10} [wie]{11} einer, der [Vollmacht]{12} [hat]{13}, und{14} nicht{15} [wie]{16} [die Schriftgelehrten]{17,18}.",
 "MRK.1.23": "Und{1} [gerade da]{2} [war]{3} [in]{4} [ihrer]{7} [Synagoge]{5,6} [ein Mensch]{8} [mit]{9} [einem unreinen]{11} [Geist]{10}, und{12} [er schrie auf]{13}",
 "MRK.1.24": "[und sagte]{1}: «[Was haben wir mit dir zu schaffen]{2-5:idiom}, Jesus{6} [von Nazaret]{7}? [Bist du gekommen]{8}, [uns]{10} [zu verderben]{9}? [Ich weiss]{11}, [wer]{13} du{12} [bist]{14}: [der Heilige]{15,16} [Gottes]{17,18}!»",
 "MRK.1.25": "Und{1} Jesus{4,5} [fuhr]{2} [ihn]{3} [an]{2} [und sagte]{6}: «[Verstumme]{7} und{8} [geh]{9} [aus]{10} [ihm]{11} [heraus]{9}!»",
 "MRK.1.26": "Und{1} [der unreine Geist]{4-7} [riss]{2} [ihn]{3} [hin und her]{2}, [schrie]{9} [mit lauter]{11} [Stimme]{10} und{8} [fuhr]{12} [aus]{13} [ihm]{14} [heraus]{12}.",
 "MRK.1.27": "Und{1} alle{3} [erschraken]{2}, sodass{4} sie [untereinander]{6,7} [diskutierten]{5} [und sagten]{8}: «Was{9} [ist]{10} das{11}? [Eine neue]{13} [Lehre]{12} [mit]{14} [Vollmacht]{15}! [Sogar]{16} [den unreinen Geistern]{17-20} [gebietet er]{21}, und{22} [sie gehorchen]{23} [ihm]{24}!»",
 "MRK.1.28": "Und{1} [die Kunde]{3,4} [von ihm]{5} [verbreitete sich]{2} sogleich{6} überall{7} [in]{8} [der ganzen]{9,10} [Gegend]{11} [von Galiläa]{12,13}.",
 "MRK.1.29": "Und{1} sogleich{2}, [als sie]{6} [aus]{3} [der Synagoge]{4,5} [hinausgegangen waren]{6}, [kamen sie]{7} [in]{8} [das Haus]{9,10} [von Simon]{11} und{12} Andreas{13}, [mit]{14} Jakobus{15} und{16} Johannes{17}.",
 "MRK.1.30": "[Simons]{4} [Schwiegermutter]{1,3} aber{2} [lag]{5} [mit Fieber]{6} [im Bett]{5}, und{7} sogleich{8} [sagen sie]{9} [ihm]{10} [von]{11} [ihr]{12}.",
 "MRK.1.31": "Und{1} [er trat hinzu]{2}, [fasste]{5} [ihre Hand]{6,7} [und richtete]{3} [sie]{4} [auf]{3}. Und{8} [das Fieber]{11,12} [verliess]{9} [sie]{10}, und{13} [sie diente]{14} [ihnen]{15}.",
 "MRK.1.32": "[Am Abend]{1,3} aber{2}, [als]{4} [die Sonne]{6,7} [untergegangen war]{5}, [brachten sie]{8} alle{11} [Kranken]{12-14} und{15} [Besessenen]{16,17} [zu]{9} [ihm]{10};",
 "MRK.1.33": "und{1} [die ganze]{3,4} [Stadt]{5} [war]{2} [vor]{7} [der Tür]{8,9} [versammelt]{6}.",
 "MRK.1.34": "Und{1} [er heilte]{2} viele{3} [Kranke]{4,5} [mit mancherlei]{6} [Leiden]{7} und{8} [trieb]{11} viele{10} Dämonen{9} [aus]{11}; und{12} [er liess]{14} [die Dämonen]{16,17} nicht{13} [reden]{15}, weil{18} [sie]{19} [ihn]{20} [kannten]{19}.",
 "MRK.1.35": "Und{1} früh{2}, [tief]{4} [in der Nacht]{3}, [stand er auf]{5}, [ging hinaus]{6} und{7} [zog sich]{8} [an]{9} [einen einsamen]{10} [Ort]{11} [zurück]{8}, [und dort]{12} [betete er]{13}.",
 "MRK.1.36": "Und{1} Simon{4} und{5} [seine Begleiter]{6-8} [jagten]{2} [ihm]{3} [nach]{2}.",
 "MRK.1.37": "Und{1} [sie fanden]{2} [ihn]{3} und{4} [sagen]{5} [zu ihm]{6}: «Alle{8} [suchen]{9} dich{10}!» ~7(leitet die direkte Rede ein)",
 "MRK.1.38": "Und{1} [er sagt]{2} [zu ihnen]{3}: «[Lasst uns]{4} anderswohin{5} [gehen]{4}, [in]{6} [die nächsten]{7,8} [Kleinstädte]{9}, damit{10} [ich]{13} auch{11} dort{12} [verkündige]{13}; [denn]{16} [dazu]{14,15} [bin ich hinausgegangen]{17}.»",
 "MRK.1.39": "Und{1} [er kam]{2} [und verkündigte]{3} [in]{4} [ihren]{7} [Synagogen]{5,6} [in]{8} [ganz]{9,10} Galiläa{11} und{12} [trieb]{15} [die Dämonen]{13,14} [aus]{15}.",
 "MRK.1.40": "Und{1} [es kommt]{2} [zu]{3} [ihm]{4} [ein Aussätziger]{5}, [bittet]{6} [ihn]{7} und{8} [fällt auf die Knie]{9} [und sagt]{10} [zu ihm]{11}: «Wenn{13} [du willst]{14}, [kannst du]{15} mich{16} [rein machen]{17}.» ~12(leitet die direkte Rede ein)",
 "MRK.1.41": "Und{1} [von Zorn ergriffen]{2} [streckte er]{3} [seine]{6} [Hand]{4,5} [aus]{3}, [berührte]{7} ihn und{8} [sagt]{9} [zu ihm]{10}: «[Ich will]{11}; [werde rein]{12}!»",
 "MRK.1.42": "Und{1} sogleich{2} [wich]{3} [der Aussatz]{6,7} [von]{4} [ihm]{5}, und{8} [er wurde rein]{9}.",
 "MRK.1.43": "Und{1} [er fuhr]{2} [ihn]{3} [hart an]{2} [und trieb]{5} [ihn]{6} sogleich{4} [hinaus]{5}",
 "MRK.1.44": "und{1} [sagt]{2} [zu ihm]{3}: «[Sieh zu]{4}, [dass du]{7} [niemandem]{5} [etwas]{6} [sagst]{7}! Vielmehr{8}: [Geh]{9}, [zeig]{11} [dich]{10} [dem Priester]{12,13} und{14} [bring]{15} [für]{16} [deine]{19} [Reinigung]{17,18} [dar]{15}, [was]{20} Mose{22} [angeordnet hat]{21}, [ihnen]{25} [zum]{23} [Zeugnis]{24}.»",
 "MRK.1.45": "[Der]{1} aber{2} [ging hinaus]{3} und [fing an]{4}, [viel]{6} [zu verkünden]{5} und{7} [die Sache]{9,10} [bekannt zu machen]{8}, sodass{11} [er]{13} [nicht mehr]{12} [öffentlich]{15} [in]{16} [eine Stadt]{17} [gehen]{18} [konnte]{14}; sondern{19} [er hielt sich]{24} draussen{20} [an]{21} [einsamen]{22} [Orten]{23} [auf]{24}. Und{25} [sie kamen]{26} [von überall her]{29} [zu]{27} [ihm]{28}.",
 # ------------------------------------------------------------ Kapitel 2
 "MRK.2.1": "Und{1} [als er]{2} [nach einigen]{6} [Tagen]{7} wieder{3} [nach]{4} Kafarnaum{5} [hineinkam]{2}, [wurde bekannt]{8}, dass{9} [er]{12} [zu Hause]{10,11} [sei]{12}.",
 "MRK.2.2": "Und{1} viele{3} [versammelten sich]{2}, sodass{4} [kein Platz]{6} [mehr]{5} war, [nicht einmal]{7} [vor]{8,9} [der Tür]{10,11}; und{12} [er sprach]{13} [zu ihnen]{14} [das Wort]{15,16}.",
 "MRK.2.3": "Und{1} [sie kommen]{2} [und bringen]{3} [zu]{4} [ihm]{5} [einen Gelähmten]{6}, [der]{7} [von]{8} [vier Männern]{9} [getragen wurde]{7}.",
 "MRK.2.4": "Und{1} [weil sie]{3} ihn [wegen]{6} [der Menge]{7,8} nicht{2} [zu ihm]{5} [bringen]{4} [konnten]{3}, [deckten sie]{9} [das Dach]{10,11} [ab]{9}, [wo]{12} [er war]{13}, und{14} [nachdem sie es aufgebrochen hatten]{15}, [lassen sie]{16} [die Matte]{17,18} [hinunter]{16}, [auf der]{19} [der Gelähmte]{20,21} [lag]{22}.",
 "MRK.2.5": "Und{1} [als]{2} Jesus{3,4} [ihren]{7} [Glauben]{5,6} [sah]{2}, [sagt er]{8} [zum Gelähmten]{9,10}: «Kind{11}, [deine]{13} [Sünden]{14,15} [sind vergeben]{12}.»",
 "MRK.2.6": "[Es sassen]{1,7} aber{2} dort{6} [einige]{3} [von den Schriftgelehrten]{4,5} und{8} [überlegten]{9} [in]{10} [ihren]{13} [Herzen]{11,12}:",
 "MRK.2.7": "«Warum{1} [redet]{4} [der]{2} so{3}? [Er lästert]{5}! Wer{6} kann{7} [Sünden]{9} [vergeben]{8} [ausser]{10,11} [Gott]{13,14} [allein]{12}?»",
 "MRK.2.8": "Und{1} sogleich{2} [erkannte]{3} Jesus{4,5} [in seinem Geist]{6-8}, dass{9} [sie]{11} [bei]{12} [sich]{13} so{10} [überlegten]{11}, und [sagt]{14} [zu ihnen]{15}: «Warum{16} [überlegt ihr]{18} [das]{17} [in]{19} [euren]{22} [Herzen]{20,21}?",
 "MRK.2.9": "Was{1} [ist]{2} leichter{3}: [zum Gelähmten]{5,6} [zu sagen]{4}: ‹[Deine]{8} [Sünden]{9,10} [sind vergeben]{7}›, oder{11} [zu sagen]{12}: ‹[Steh auf]{13} und{14} [nimm]{15} [deine]{18} [Matte]{16,17} und{19} [geh umher]{20}›?",
 "MRK.2.10": "[Damit]{1} [ihr]{3} aber{2} [wisst]{3}, dass{4} [der Menschensohn]{7-10} [Vollmacht]{5} [hat]{6}, [auf]{11} [der Erde]{12,13} [Sünden]{15} [zu vergeben]{14}» – [sagt er]{16} [zum Gelähmten]{17,18}:",
 "MRK.2.11": "«Dir{1} [sage ich]{2}: [Steh auf]{3}, [nimm]{4} [deine]{7} [Matte]{5,6} und{8} [geh]{9} [nach Hause]{10-13}!»",
 "MRK.2.12": "Und{1} [er stand auf]{2}, und{3} sogleich{4} [nahm er]{5} [die Matte]{6,7} [und ging hinaus]{8} [vor]{9} [aller Augen]{10}, sodass{11} alle{13} [ausser sich gerieten]{12} und{14} [Gott]{16,17} [priesen]{15} [und sagten]{18}: «[So etwas]{20} [haben wir]{22} [noch nie]{21} [gesehen]{22}!» ~19(leitet die direkte Rede ein)",
 "MRK.2.13": "Und{1} [er ging]{2} wieder{3} [hinaus]{2} [an]{4} [den See]{5,6}; und{7} [die ganze]{8,9} [Menge]{10} [kam]{11} [zu]{12} [ihm]{13}, und{14} [er lehrte]{15} [sie]{16}.",
 "MRK.2.14": "Und{1} [im Vorbeigehen]{2} [sah er]{3} Levi{4}, [den Sohn]{5,6} [des Alphäus]{7}, [an]{9} [der Zollstelle]{10,11} [sitzen]{8}, und{12} [er sagt]{13} [zu ihm]{14}: «[Folge]{15} [mir]{16}!» Und{17} [er stand auf]{18} [und folgte]{19} [ihm]{20}.",
 "MRK.2.15": "Und{1} [es geschieht]{2}, [dass er]{4} [in]{5} [seinem]{8} [Haus]{6,7} [zu Tisch liegt]{3}, und{9} viele{10} Zöllner{11} und{12} Sünder{13} [lagen mit]{14} Jesus{15,16} und{17} [seinen]{20} [Jüngern]{18,19} [zu Tisch]{14}; [denn]{22} [es waren]{21} viele{23}, und{24} [sie folgten]{25} [ihm]{26}.",
 "MRK.2.16": "Und{1} [als]{6} [die Schriftgelehrten]{2,3} [der Pharisäer]{4,5} [sahen]{6}, dass{7} [er]{8} [mit]{9} [den Sündern]{10,11} und{12} [Zöllnern]{13} [isst]{8}, [sagten sie]{14} [zu]{15} [seinen]{17} [Jüngern]{16}: «Wieso{18} [isst er]{24} [mit]{19} [den Zöllnern]{20,21} und{22} [Sündern]{23}?»",
 "MRK.2.17": "Und{1} [als]{2} Jesus{3,4} [das hörte]{2}, [sagt er]{5} [zu ihnen]{6}: «[Nicht]{8} [die Gesunden]{11,12} [brauchen]{9,10} [einen Arzt]{13}, sondern{14} [die Kranken]{15-17}. [Ich bin]{19} nicht{18} [gekommen]{19}, [Gerechte]{21} [zu rufen]{20}, sondern{22} Sünder{23}.» ~7(leitet die direkte Rede ein)",
 "MRK.2.18": "Und{1} [die Jünger]{3,4} [des Johannes]{5} und{6} [die Pharisäer]{7,8} [fasteten]{2,9}. Und{10} [sie kommen]{11} und{12} [sagen]{13} [zu ihm]{14}: «[Warum]{15,16} [fasten]{25} [die Jünger]{17,18} [des Johannes]{19} und{20} [die Jünger]{21,22} [der Pharisäer]{23,24}, [deine]{28} [Jünger]{26,29} aber{27} [fasten]{31} nicht{30}?»",
 "MRK.2.19": "Und{1} Jesus{4,5} [sagte]{2} [zu ihnen]{3}: «[Können]{7} [etwa]{6} [die Hochzeitsgäste]{8-11} fasten{19}, [während]{12,13} [der Bräutigam]{14,15} [bei]{16} [ihnen]{17} [ist]{18}? [Solange]{20,21} [sie]{22} [den Bräutigam]{23,24} [bei]{25} [sich]{26} [haben]{22}, [können sie]{28} nicht{27} fasten{29}.",
 "MRK.2.20": "[Es werden]{1} aber{2} Tage{3} [kommen]{1}, [wenn]{4} [der Bräutigam]{8,9} [von]{6} [ihnen]{7} [weggenommen wird]{5}; und{10} dann{11} [werden sie]{12} [an]{13} [jenem]{14} [Tag]{15,16} [fasten]{12}.",
 "MRK.2.21": "Niemand{1} [näht]{5} [einen Flicken]{2} [aus ungewalktem]{4} [Stoff]{3} [auf]{6} [ein altes]{8} [Kleid]{7}; [sonst]{9-11} [reisst]{12} [das Flickstück]{13,14} [von]{15} [ihm]{16} [ab]{12}, [das neue]{17,18} [vom alten]{19,20}, und{21} [der Riss]{23} [wird]{24} [schlimmer]{22}.",
 "MRK.2.22": "Und{1} niemand{2} [füllt]{3} [jungen]{5} Wein{4} [in]{6} [alte]{8} Schläuche{7}; [sonst]{9-11} [wird]{12} [der Wein]{13,14} [die Schläuche]{15,16} [zerreissen]{12}, und{17} [der Wein]{18,19} [ist verloren]{20} und{21} [die Schläuche]{22,23} ebenso. Sondern{24}: [jungen]{26} Wein{25} [in]{27} [neue]{29} Schläuche{28}!»",
 "MRK.2.23": "Und{1} [es geschah]{2}, [dass er]{3} [am Sabbat]{4-6} [durch]{8} [die Kornfelder]{9,10} [ging]{7}, und{11} [seine]{14} [Jünger]{12,13} [fingen an]{15}, [unterwegs]{16,17:idiom} [die Ähren]{19,20} [abzurupfen]{18}.",
 "MRK.2.24": "Und{1} [die Pharisäer]{2,3} [sagten]{4} [zu ihm]{5}: «Sieh{6}, warum{7} [tun sie]{8} [am Sabbat]{9,10}, [was]{11} nicht{12} [erlaubt ist]{13}?»",
 "MRK.2.25": "Und{1} [er sagt]{2} [zu ihnen]{3}: «[Habt ihr]{5} nie{4} [gelesen]{5}, was{6} David{8} [getan hat]{7}, als{9} [er in Not war]{10,11} und{12} [hungerte]{13}, er{14} und{15} [seine Begleiter]{16-18},",
 "MRK.2.26": "wie{1} [er]{2} [zur Zeit]{8} [des Hohenpriesters]{10} Abjatar{9} [in]{3} [das Haus]{4,5} [Gottes]{6,7} [hineinging]{2} und{11} [die Schaubrote]{12-15} [ass]{16}, [die]{17} [ausser]{21,22} [den Priestern]{23,24} [niemand]{18} [essen]{20} [darf]{19}, und{25} sie auch{27} [denen]{28} [gab]{26}, die [bei]{29} [ihm]{30} [waren]{31}?»",
 "MRK.2.27": "Und{1} [er sagte]{2} [zu ihnen]{3}: «[Der Sabbat]{4,5} [wurde]{9} [für]{6} [den Menschen]{7,8} [geschaffen]{9}, und{10} nicht{11} [der Mensch]{12,13} [für]{14} [den Sabbat]{15,16}.",
 "MRK.2.28": "Darum{1} [ist]{3} [der Menschensohn]{4-7} [Herr]{2} auch{8} [über den Sabbat]{9,10}.»",
 # ------------------------------------------------------------ Kapitel 3,1–19
 "MRK.3.1": "Und{1} [er ging]{2} wieder{3} [in]{4} [eine Synagoge]{5}, und{6} dort{8} [war]{7} [ein Mensch]{9}, [der]{11} [eine verdorrte]{10} [Hand]{12,13} [hatte]{11}.",
 "MRK.3.2": "Und{1} [sie beobachteten]{2} [ihn]{3} [genau]{2}, ob{4} [er]{7} [ihn]{8} [am Sabbat]{5,6} [heilen würde]{7}, damit{9} [sie]{10} [ihn]{11} [anklagen könnten]{10}.",
 "MRK.3.3": "Und{1} [er sagt]{2} [zu dem Menschen]{3,4}, [der]{5} [die]{6} [verdorrte]{9} [Hand]{7} [hatte]{8}: «[Steh auf]{10} [und tritt in]{11} [die Mitte]{12,13}!»",
 "MRK.3.4": "Und{1} [er sagt]{2} [zu ihnen]{3}: «[Ist es erlaubt]{4}, [am Sabbat]{5,6} [Gutes zu tun]{7} oder{8} [Böses zu tun]{9}, [ein Leben]{10} [zu retten]{11} oder{12} [zu töten]{13}?» [Sie]{14} aber{15} [schwiegen]{16}.",
 "MRK.3.5": "Und{1} [er blickte]{2} [sie]{3} [ringsum an]{2} [mit]{4} [Zorn]{5}, [betrübt]{6} [über]{7} [die Verhärtung]{8,9} [ihres]{12} [Herzens]{10,11}, [und sagt]{13} [zu dem Menschen]{14,15}: «[Streck]{16} [die Hand]{17,18} [aus]{16}!» Und{19} [er streckte sie aus]{20}, und{21} [seine]{25} [Hand]{23,24} [wurde wiederhergestellt]{22}.",
 "MRK.3.6": "Und{1} [die Pharisäer]{3,4} [gingen hinaus]{2} [und hielten]{10} sogleich{5} [mit]{6} [den Herodianern]{7,8} [Rat]{9} [gegen]{11} [ihn]{12}, [wie]{13} [sie]{15} [ihn]{14} [umbringen könnten]{15}.",
 "MRK.3.7": "Und{1} Jesus{2,3} [zog sich]{8} [mit]{4} [seinen]{7} [Jüngern]{5,6} [an]{9} [den See]{10,11} [zurück]{8}, und{12} [eine grosse]{13} [Schar]{14} [aus]{15} Galiläa{16,17} [folgte]{18}. Auch{19} [aus]{20} Judäa{21,22}",
 "MRK.3.8": "und{1} [aus]{2} Jerusalem{3} und{4} [aus]{5} Idumäa{6,7} und{8} [von jenseits]{9} [des Jordan]{10,11} und{12} [aus der Gegend um]{13} Tyros{14} und{15} Sidon{16} [kam]{22} [eine grosse]{18} [Schar]{17} [zu]{23} [ihm]{24}, [weil sie hörten]{19}, [was er alles]{20} [tat]{21}.",
 "MRK.3.9": "Und{1} [er sagte]{2} [seinen]{5} [Jüngern]{3,4}, dass{6} [ein Boot]{7} [für ihn]{9} [bereitliegen solle]{8} [wegen]{10} [der Menge]{11,12}, damit{13} [sie]{15} [ihn]{16} nicht{14} [erdrückten]{15}.",
 "MRK.3.10": "Denn{2} [er hatte]{3} viele{1} [geheilt]{3}, sodass{4} [alle, die]{10} [Plagen]{12} [hatten]{11}, [sich auf]{5} [ihn]{6} [stürzten]{5}, [um]{7} [ihn]{8} [zu berühren]{9}.",
 "MRK.3.11": "Und{1} [wenn]{6} [die unreinen Geister]{2-5} [ihn]{7} [sahen]{8}, [fielen sie]{9} [vor ihm]{10} [nieder]{9} und{11} [schrien]{12}: «Du{15} bist{16} [der Sohn]{17,18} [Gottes]{19,20}!» ~13(«sagend»; im Doppelpunkt aufgegangen) ~14(leitet die direkte Rede ein)",
 "MRK.3.12": "Und{1} [er fuhr]{3} [sie]{4} [heftig]{2} [an]{3}, damit{5} [sie]{9} [ihn]{7} nicht{6} [bekannt]{8} [machten]{9}.",
 "MRK.3.13": "Und{1} [er steigt]{2} [auf]{3} [den Berg]{4,5} und{6} [ruft zu sich]{7}, [die]{8} [er selbst]{10} [wollte]{9}; und{11} [sie kamen]{12} [zu]{13} [ihm]{14}.",
 "MRK.3.14": "Und{1} [er setzte]{2} [zwölf]{3} [ein]{2}, damit{4} [sie]{5} [bei]{6} [ihm]{7} [seien]{5} und{8} damit{9} [er]{10} [sie]{11} [aussende]{10}, [zu verkündigen]{12}",
 "MRK.3.15": "und{1} [Vollmacht]{3} [zu haben]{2}, [die Dämonen]{5,6} [auszutreiben]{4}.",
 "MRK.3.16": "Und{1} [er setzte]{2} [die Zwölf]{3,4} [ein]{2}; und{5} [dem Simon]{8,9} [gab er]{6} [den Namen]{7} Petrus{10};",
 "MRK.3.17": "und{1} Jakobus{2}, [den Sohn]{3,4} [des Zebedäus]{5}, und{6} Johannes{7}, [den Bruder]{8,9} [des Jakobus]{10,11} – und{12} [er gab]{13} [ihnen]{14} [den Namen]{15} Boanerges{16}, [das heisst]{17,18} «[Söhne]{19} [des Donners]{20}» –,",
 "MRK.3.18": "und{1} Andreas{2} und{3} Philippus{4} und{5} Bartholomäus{6} und{7} Matthäus{8} und{9} Thomas{10} und{11} Jakobus{12}, [den Sohn]{13,14} [des Alphäus]{15}, und{16} Thaddäus{17} und{18} Simon{19}, [den Kananäer]{20,21},",
 "MRK.3.19": "und{1} Judas{2} Iskariot{3}, [der]{4} [ihn]{7} auch{5} [auslieferte]{6}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 1
 "MRK.1.1": "[De Aafang]{1} [vom Evangelium]{2,3} [vo Jesus]{4} Christus{5}.",
 "MRK.1.2": "Wie{1} [es gschribe staat]{2} [bim]{3} Jesaja{4,5}, [em Prophet]{6,7}: «Lueg{8}, [ich schicke]{9} [min]{12} [Bote]{10,11} [vor dir här]{13-15:idiom}, [wo]{16} [din]{20} [Wäg]{18,19} [wird parat mache]{17};",
 "MRK.1.3": "[e Stimm]{1} [vo eim, wo rüeft]{2} [i]{3} [de Wüeschti]{4,5}: ‹[Mached]{6} [de Wäg]{7,8} [vom Herr]{9} [parat]{6}, [mached]{11} [sini]{14} [Pfäd]{12,13} grad{10}!›»",
 "MRK.1.4": "So [isch]{1} [de Johannes]{2} [de Täufer]{3,4} [i]{5} [de Wüeschti]{6,7} [uftrete]{1} [und hät]{8} [e Taufi]{9} [vo de Umkehr]{10} [zur]{11} [Vergäbig]{12} [vo de Sünde]{13} [verchündet]{8}.",
 "MRK.1.5": "Und{1} [s ganz]{5,6} Land{8} Judäa{7} und{9} [alli]{12} [Jerusalemer]{10,11} [sind]{2} [zu]{3} [ihm]{4} [usegange]{2}, und{13} [si händ sich]{14} [vo]{15} [ihm]{16} [im]{17,18} [Fluss]{20} Jordan{19} [la taufe]{14} [und händ]{21} [iri]{24} [Sünde]{22,23} [bekännt]{21}.",
 "MRK.1.6": "Und{1} [de Johannes]{3,4} [isch]{2} [in]{5} [Kamelhaar]{6,7} [aagleit gsii]{5} und{8} [mit eme lädrige]{10} [Gurt]{9} [um]{11} [sini]{14} [Hüfte]{12,13}, und{15} [er hät]{16} [Heuschrecke]{17} und{18} [wilde]{20} [Hung]{19} [ggässe]{16}.",
 "MRK.1.7": "Und{1} [er hät verchündet]{2} [und gseit]{3}: «[Nach]{8} [mir]{9} [chunnt]{4} [dä]{5}, [wo stärcher isch]{6} [als ich]{7}; [ich bi]{12} nöd{11} [wärt]{13}, [mich z bücke]{14} und [ihm]{10} [de Rieme]{16,17} [vo sine]{20} [Sandale]{18,19} [ufzmache]{15}.",
 "MRK.1.8": "Ich{1} [han]{2} [eu]{3} [mit Wasser]{4} [tauft]{2}, er{5} aber{6} [wird]{7} [eu]{8} [mit]{9} [heilige]{11} [Geischt]{10} [taufe]{7}.»",
 "MRK.1.9": "Und{1} [es isch gscheh]{2} [i]{3} [dene]{4} [Täg]{5,6}: [Da isch]{7} [de Jesus]{8} [vo]{9} Nazaret{10} [z Galiläa]{11,12} [choo]{7} und{13} [hät sich]{14} [vom Johannes]{18,19} [im]{15,16} Jordan{17} [la taufe]{14}.",
 "MRK.1.10": "Und{1} grad{2}, [wo er]{3} [us]{4} [em Wasser]{5,6} [ufecho isch]{3}, [hät er]{7} [d Himmel]{9,10} [gseh]{7} [ufriisse]{8} und{11} [de Geischt]{12,13} [wie]{14} [e Tuube]{15} [uf]{17} [ihn]{18} [abecho]{16}.",
 "MRK.1.11": "Und{1} [e Stimm]{2} [isch]{3} [us]{4} [de Himmel]{5,6} [choo]{3}: «Du{7} bisch{8} [min]{11} [liebe]{12,13} [Sohn]{9,10}; [a dir]{14,15} [han ich Gfalle gfunde]{16}.»",
 "MRK.1.12": "Und{1} grad{2} [tribt]{6} [en]{5} [de Geischt]{3,4} [use]{6} [i]{7} [d Wüeschti]{8,9}.",
 "MRK.1.13": "Und{1} [er isch]{2} [vierzg]{6} Täg{7} [i]{3} [de Wüeschti]{4,5} [gsii]{2} [und isch]{8} [vom]{9,10} Satan{11} [versuecht worde]{8}, und{12} [er isch]{13} [bi]{14} [de wilde Tier]{15,16} [gsii]{13}, und{17} [d Ängel]{18,19} [händ]{20} [ihm]{21} [dienet]{20}.",
 "MRK.1.14": "Und{1} [nachdem]{2,3} [de Johannes]{5,6} [usgliferet worde isch]{4}, [isch]{7} [de Jesus]{8,9} [uf]{10} Galiläa{11,12} [choo]{7} [und hät]{13} [s Evangelium]{14,15} [vo Gott]{16,17} [verchündet]{13}",
 "MRK.1.15": "und{1} [hät gseit]{2}: «[D Ziit]{5,6} [isch erfüllt]{4}, und{7} [s Riich]{9,10} [vo Gott]{11,12} [isch nöch choo]{8}. [Chehred um]{13} und{14} [glaubed]{15} [as]{16,17} Evangelium{18}!» ~3(leitet di direkt Red ii)",
 "MRK.1.16": "Und{1} [wo er]{2} [am]{3,4} [See]{5} [vo Galiläa]{6,7} [entlang gange isch]{2}, [hät er]{8} [de Simon]{9} und{10} [de Andreas]{11} [gseh]{8}, [de Brueder]{12,13} [vom Simon]{14}, [wie si]{15} [im]{16,17} [See]{18} [iri Netz uusgworfe händ]{15}; [si sind]{19} nämli{20} Fischer{21} [gsii]{19}.",
 "MRK.1.17": "Und{1} [de Jesus]{4,5} [hät]{2} [zu ine]{3} [gseit]{2}: «[Chömed]{6} [mir]{8} [nache]{7}, und{9} [ich mache]{10} [eu]{11} [zu]{12} [Mänschefischer]{13,14}.»",
 "MRK.1.18": "Und{1} grad{2} [händ si]{3} [d Netz]{4,5} [la ligge]{3} [und sind]{6} [ihm]{7} [nachegange]{6}.",
 "MRK.1.19": "Und{1} [wo er]{2} [es Stuck]{3} [wiiter gange isch]{2}, [hät er]{4} [de Jakobus]{5} [gseh]{4}, [de Sohn]{6,7} [vom Zebedäus]{8}, und{9} [de Johannes]{10}, [sin]{13} [Brueder]{11,12}; und{14} si{15} sind [im]{16,17} [Boot]{18} gsii [und händ]{19} [d Netz]{20,21} [parat gmacht]{19}.",
 "MRK.1.20": "Und{1} grad{2} [hät er]{3} si{4} [grüeft]{3}. Und{5} [si händ]{6} [ire]{9} [Vatter]{7,8} [de Zebedäus]{10} [mit]{14} [de Taglöhner]{15,16} [im]{11,12} [Boot]{13} [zrugglaa]{6} [und sind]{17} [ihm]{19} [nache]{18} [gange]{17}.",
 "MRK.1.21": "Und{1} [si chömed]{2} [uf]{3} Kafarnaum{4}. Und{5} grad{6} [am Sabbat]{7,8} [hät er]{9} [i]{10} [de Synagoge]{11,12} [gleert]{9}.",
 "MRK.1.22": "Und{1} [si sind überwältiget gsii]{2} [vo]{3} [sinere]{6} [Lehr]{4,5}; [er hät]{7,9} [si]{10} nämli{8} [gleert]{7,9} [wie]{11} eine, wo [Vollmacht]{12} [hät]{13}, und{14} nöd{15} [wie]{16} [d Schriftgleerte]{17,18}.",
 "MRK.1.23": "Und{1} [grad dänn]{2} [isch]{3} [i]{4} [irer]{7} [Synagoge]{5,6} [en Mänsch]{8} [mit]{9} [eme unreine]{11} [Geischt]{10} [gsii]{3}, und{12} [er hät ufgschroue]{13}",
 "MRK.1.24": "[und gseit]{1}: «[Was händ mir mit dir z tue]{2-5:idiom}, Jesus{6} [vo Nazaret]{7}? [Bisch du choo]{8}, [zum]{9} [eus]{10} [z verderbe]{9}? [Ich weiss]{11}, [wer]{13} du{12} [bisch]{14}: [de Heilig]{15,16} [vo Gott]{17,18}!»",
 "MRK.1.25": "Und{1} [de Jesus]{4,5} [hät]{2} [en]{3} [aagfahre]{2} [und gseit]{6}: «[Bis still]{7} und{8} [gang]{9} [us]{10} [ihm]{11} [use]{9}!»",
 "MRK.1.26": "Und{1} [de unrein Geischt]{4-7} [hät]{2} [en]{3} [hin und her grisse]{2}, [hät]{9} [mit luter]{11} [Stimm]{10} [gschroue]{9} und{8} [isch]{12} [us]{13} [ihm]{14} [usegfahre]{12}.",
 "MRK.1.27": "Und{1} alli{3} [sind erschrocke]{2}, so dass{4} si [undereinand]{6,7} [diskutiert]{5} [und gseit]{8} händ: «Was{9} [isch]{10} das{11}? [E nöii]{13} [Lehr]{12} [mit]{14} [Vollmacht]{15}! [Sogar]{16} [de unreine Geischter]{17-20} [befiehlt er]{21}, und{22} [si folged]{23} [ihm]{24}!»",
 "MRK.1.28": "Und{1} [de Ruef]{3,4} [vo ihm]{5} [hät sich]{2} grad{6} überall{7} [i]{8} [de ganze]{9,10} [Gäged]{11} [vo Galiläa]{12,13} [verbreitet]{2}.",
 "MRK.1.29": "Und{1} grad{2}, [wo si]{6} [us]{3} [de Synagoge]{4,5} [use gange sind]{6}, [sind si]{7} [is]{8,9} [Huus]{10} [vom Simon]{11} und{12} [vom Andreas]{13} [choo]{7}, [mit]{14} [em Jakobus]{15} und{16} [em Johannes]{17}.",
 "MRK.1.30": "[D Schwigermueter]{1,3} [vom Simon]{4} aber{2} [isch]{5} [mit Fieber]{6} [im Bett gläge]{5}, und{7} grad{8} [verzelled si]{9} [ihm]{10} [vo]{11} [ere]{12}.",
 "MRK.1.31": "Und{1} [er isch zue ere gange]{2}, [hät]{5} [ire d Hand]{6,7} [packt]{5} [und hät]{3} [si]{4} [ufgrichtet]{3}. Und{8} [s Fieber]{11,12} [hät]{9} [si]{10} [verlaa]{9}, und{13} [si hät]{14} [ine]{15} [dienet]{14}.",
 "MRK.1.32": "[Am Abig]{1,3} aber{2}, [wo]{4} [d Sunne]{6,7} [undergange isch]{5}, [händ si]{8} alli{11} [Chranke]{12-14} und{15} [Bsässne]{16,17} [zu]{9} [ihm]{10} [bracht]{8};",
 "MRK.1.33": "und{1} [di ganz]{3,4} [Stadt]{5} [isch]{2} [vor]{7} [de Tür]{8,9} [versammlet gsii]{6}.",
 "MRK.1.34": "Und{1} [er hät]{2} vil{3} [Chranki]{4,5} [mit allerlei]{6} [Liide]{7} [gheilt]{2} und{8} [er hät]{11} vil{10} Dämone{9} [ustribe]{11}; und{12} [er hät]{14} [d Dämone]{16,17} nöd{13} [la]{14} [rede]{15}, wil{18} [si]{19} [en]{20} [kännt händ]{19}.",
 "MRK.1.35": "Und{1} früe{2}, [no tüüf]{4} [i de Nacht]{3}, [isch er ufgstande]{5}, [isch usegange]{6} und{7} [hät sich]{8} [an]{9} [en einsame]{10} [Ort]{11} [zruggzoge]{8}, [und dört]{12} [hät er bättet]{13}.",
 "MRK.1.36": "Und{1} [de Simon]{4} und{5} [sini Begleiter]{6-8} [sind]{2} [ihm]{3} [nachegrännt]{2}.",
 "MRK.1.37": "Und{1} [si händ]{2} [en]{3} [gfunde]{2} und{4} [säged]{5} [zu ihm]{6}: «Alli{8} [sueched]{9} dich{10}!» ~7(leitet di direkt Red ii)",
 "MRK.1.38": "Und{1} [er seit]{2} [zu ine]{3}: «[Gömmer]{4} anderswohii{5}, [i]{6} [di nöchschte]{7,8} [Städtli]{9}, demit{10} [ich]{13} au{11} dört{12} [verchünde]{13}; [dänn]{16} [dewäge]{14,15} [bin ich usegange]{17}.»",
 "MRK.1.39": "Und{1} [er isch]{2} [dur]{8} [ganz]{9,10} Galiläa{11} [zoge]{2} [und hät]{3} [i]{4} [irne]{7} [Synagoge]{5,6} [verchündet]{3} und{12} [hät]{15} [d Dämone]{13,14} [ustribe]{15}.",
 "MRK.1.40": "Und{1} [es chunnt]{2} [en Ussätzige]{5} [zu]{3} [ihm]{4}, [bittet]{6} [en]{7} und{8} [gaat uf d Chnüü]{9} [und seit]{10} [zu ihm]{11}: «Wänn{13} [du wottsch]{14}, [chasch du]{15} mich{16} [rein mache]{17}.» ~12(leitet di direkt Red ii)",
 "MRK.1.41": "Und{1} [voll Zorn]{2} [hät er]{3} [sini]{6} [Hand]{4,5} [usgstreckt]{3}, [hät]{7} en [aagrüert]{7} und{8} [seit]{9} [zu ihm]{10}: «[Ich wott]{11}; [wird rein]{12}!»",
 "MRK.1.42": "Und{1} grad{2} [isch]{3} [de Ussatz]{6,7} [vo]{4} [ihm]{5} [gwiche]{3}, und{8} [er isch rein worde]{9}.",
 "MRK.1.43": "Und{1} [er hät]{2} [en]{3} [hert aagschnauzt]{2} [und hät]{5} [en]{6} grad{4} [usegjagt]{5}",
 "MRK.1.44": "und{1} [seit]{2} [zu ihm]{3}: «[Lueg]{4}, [dass du]{7} [niemertem]{5} [öppis]{6} [verzellsch]{7}! Sondern{8}: [Gang]{9}, [zeig]{11} [dich]{10} [em Prieschter]{12,13} und{14} [bring]{15} [für]{16} [dini]{19} [Reinigung]{17,18}, [was]{20} [de Mose]{22} [aagordnet hät]{21}, [ine]{25} [zum]{23} [Zügnis]{24}.»",
 "MRK.1.45": "[Dä]{1} aber{2} [isch usegange]{3} und [hät aagfange]{4}, [vil]{6} [z verchünde]{5} und{7} [d Sach]{9,10} [bekannt z mache]{8}, so dass{11} [er]{13} [nüme]{12} [öffentlich]{15} [in]{16} [e Stadt]{17} [hät chöne]{14} [gaa]{18}; sondern{19} [er isch]{24} dusse{20} [a]{21} [einsame]{22} [Ort]{23} [blibe]{24}. Und{25} [si sind]{26} [vo überall här]{29} [zu]{27} [ihm]{28} [choo]{26}.",
 # ------------------------------------------------------------ Kapitel 2
 "MRK.2.1": "Und{1} [wo er]{2} [nach es paar]{6} [Täg]{7} wider{3} [uf]{4} Kafarnaum{5} [choo isch]{2}, [hät me ghört]{8}, dass{9} [er]{12} [dihei]{10,11} [isch]{12}.",
 "MRK.2.2": "Und{1} vil{3} [sind zämecho]{2}, so dass{4} es [kei Platz]{6} [meh]{5} gha hät, [nöd emal]{7} [vor]{8,9} [de Tür]{10,11}; und{12} [er hät]{13} [ine]{14} [s Wort]{15,16} [gseit]{13}.",
 "MRK.2.3": "Und{1} [si chömed]{2} [und bringed]{3} [en Glähmte]{6} [zu]{4} [ihm]{5}, [wo]{7} [vo]{8} [vier Manne]{9} [treit wird]{7}.",
 "MRK.2.4": "Und{1} [wil si]{3} en [wäge]{6} [de Mängi]{7,8} nöd{2} [zu ihm]{5} [händ chöne]{3} [bringe]{4}, [händ si]{9} [s Dach]{10,11} [abteckt]{9}, [wo]{12} [er gsii isch]{13}, und{14} [wo si es Loch gmacht händ]{15}, [lönd si]{16} [d Matte]{17,18} [abe]{16}, [uf dere]{19} [de Glähmt]{20,21} [gläge isch]{22}.",
 "MRK.2.5": "Und{1} [wo]{2} [de Jesus]{3,4} [ire]{7} [Glaube]{5,6} [gseh hät]{2}, [seit er]{8} [zum Glähmte]{9,10}: «Chind{11}, [dini]{13} [Sünde]{14,15} [sind vergää]{12}.»",
 "MRK.2.6": "[Es sind]{1} aber{2} [es paar]{3} [vo de Schriftgleerte]{4,5} dört{6} [gsässe]{7} und{8} [händ]{9} [i]{10} [irne]{13} [Härze]{11,12} [überleit]{9}:",
 "MRK.2.7": "«Wieso{1} [redt]{4} [dä]{2} so{3}? [Er läschteret]{5}! Wär{6} [cha]{7} [Sünde]{9} [vergää]{8} [ussert]{10,11} [Gott]{13,14} [elei]{12}?»",
 "MRK.2.8": "Und{1} grad{2} [hät]{3} [de Jesus]{4,5} [i sim Geischt]{6-8} [gmerkt]{3}, dass{9} [si]{11} [bi]{12} [sich]{13} so{10} [überleged]{11}, und [seit]{14} [zu ine]{15}: «Wieso{16} [überleged er]{18} [das]{17} [i]{19} [eune]{22} [Härze]{20,21}?",
 "MRK.2.9": "Was{1} [isch]{2} liechter{3}: [zum Glähmte]{5,6} [z säge]{4}: ‹[Dini]{8} [Sünde]{9,10} [sind vergää]{7}›, oder{11} [z säge]{12}: ‹[Stand uf]{13} und{14} [nimm]{15} [dini]{18} [Matte]{16,17} und{19} [lauf umenand]{20}›?",
 "MRK.2.10": "[Demit]{1} [er]{3} aber{2} [wüssed]{3}, dass{4} [de Mänschesohn]{7-10} [Vollmacht]{5} [hät]{6}, [uf]{11} [de Ärde]{12,13} [Sünde]{15} [z vergää]{14}» – [seit er]{16} [zum Glähmte]{17,18}:",
 "MRK.2.11": "«Dir{1} [säg ich]{2}: [Stand uf]{3}, [nimm]{4} [dini]{7} [Matte]{5,6} und{8} [gang]{9} [hei]{10-13}!»",
 "MRK.2.12": "Und{1} [er isch ufgstande]{2}, und{3} grad{4} [hät er]{5} [d Matte]{6,7} [gnoo]{5} [und isch]{8} [vor]{9} [allne]{10} [usegange]{8}, so dass{11} alli{13} [usser sich gsii sind]{12} und{14} [Gott]{16,17} [prise]{15} [und gseit]{18} händ: «[Eso öppis]{20} [händ mir]{22} [no nie]{21} [gseh]{22}!» ~19(leitet di direkt Red ii)",
 "MRK.2.13": "Und{1} [er isch]{2} wider{3} [use]{2} [an]{4} [See]{5,6} [gange]{2}; und{7} [di ganz]{8,9} [Mängi]{10} [isch]{11} [zu]{12} [ihm]{13} [choo]{11}, und{14} [er hät]{15} [si]{16} [gleert]{15}.",
 "MRK.2.14": "Und{1} [im Verbiigaa]{2} [hät er]{3} [de Levi]{4}, [de Sohn]{5,6} [vom Alphäus]{7}, [a]{9} [de Zollstell]{10,11} [gseh]{3} [hocke]{8}, und{12} [seit]{13} [zu ihm]{14}: «[Chumm]{15} [mir]{16} [nache]{15}!» Und{17} [er isch ufgstande]{18} [und isch]{19} [ihm]{20} [nachegange]{19}.",
 "MRK.2.15": "Und{1} [es isch eso]{2}, [dass er]{4} [i]{5} [sim]{8} [Huus]{6,7} [am Tisch liit]{3}, und{9} vil{10} Zöllner{11} und{12} Sünder{13} [sind mit]{14} [em Jesus]{15,16} und{17} [sine]{20} [Jünger]{18,19} [am Tisch gläge]{14}; [dänn]{22} [es sind]{21} vil{23} [gsii]{21}, und{24} [si sind]{25} [ihm]{26} [nachegange]{25}.",
 "MRK.2.16": "Und{1} [wo]{6} [d Schriftgleerte]{2,3} [vo de Pharisäer]{4,5} [gseh händ]{6}, dass{7} [er]{8} [mit]{9} [de Sünder]{10,11} und{12} [Zöllner]{13} [isst]{8}, [händ si]{14} [zu]{15} [sine]{17} [Jünger]{16} [gseit]{14}: «Wieso{18} [isst er]{24} [mit]{19} [de Zöllner]{20,21} und{22} [Sünder]{23}?»",
 "MRK.2.17": "Und{1} [wo]{2} [de Jesus]{3,4} [das ghört hät]{2}, [seit er]{5} [zu ine]{6}: «[Nöd]{8} [di Gsunde]{11,12} [bruuched]{9,10} [en Dokter]{13}, sondern{14} [di Chranke]{15-17}. [Ich bi]{19} nöd{18} [choo]{19}, [zum]{20} [Grächti]{21} [rüefe]{20}, sondern{22} Sünder{23}.» ~7(leitet di direkt Red ii)",
 "MRK.2.18": "Und{1} [d Jünger]{3,4} [vom Johannes]{5} und{6} [d Pharisäer]{7,8} [händ gfaschtet]{2,9}. Und{10} [si chömed]{11} und{12} [säged]{13} [zu ihm]{14}: «[Wieso]{15,16} [faschted]{25} [d Jünger]{17,18} [vom Johannes]{19} und{20} [d Jünger]{21,22} [vo de Pharisäer]{23,24}, [dini]{28} [Jünger]{26,29} aber{27} [faschted]{31} nöd{30}?»",
 "MRK.2.19": "Und{1} [de Jesus]{4,5} [hät]{2} [zu ine]{3} [gseit]{2}: «[Chönd]{7} [d Hochziitsgäscht]{8-11} [öppe]{6} faschte{19}, [solang]{12,13} [de Brüütigam]{14,15} [bi]{16} [ine]{17} [isch]{18}? [So lang]{20,21} [si]{22} [de Brüütigam]{23,24} [bi]{25} [sich]{26} [händ]{22}, [chönd si]{28} nöd{27} faschte{29}.",
 "MRK.2.20": "[Es chömed]{1} aber{2} Täg{3}, [wo]{4} [de Brüütigam]{8,9} [vo]{6} [ine]{7} [weggnoo wird]{5}; und{10} dänn{11} [wärded si]{12} [a]{13} [dem]{14} [Tag]{15,16} [faschte]{12}.",
 "MRK.2.21": "Niemert{1} [näht]{5} [en Blätz]{2} [vo nöd iiglaufnem]{4} [Tuech]{3} [uf]{6} [es alts]{8} [Chleid]{7}; [suscht]{9-11} [riisst]{12} [de Blätz]{13,14} [vo]{15} [ihm]{16} [ab]{12}, [de nöi]{17,18} [vom alte]{19,20}, und{21} [de Riss]{23} [wird]{24} [schlimmer]{22}.",
 "MRK.2.22": "Und{1} niemert{2} [tuet]{3} [nöie]{5} Wii{4} [i]{6} [alti]{8} Schlüüch{7}; [suscht]{9-11} [verriisst]{12} [de Wii]{13,14} [d Schlüüch]{15,16}, und{17} [de Wii]{18,19} [isch verlore]{20} und{21} [d Schlüüch]{22,23} au. Sondern{24}: [nöie]{26} Wii{25} [i]{27} [nöii]{29} Schlüüch{28}!»",
 "MRK.2.23": "Und{1} [es isch gscheh]{2}, [dass er]{3} [am Sabbat]{4-6} [dur]{8} [d Chornfälder]{9,10} [gange isch]{7}, und{11} [sini]{14} [Jünger]{12,13} [händ aagfange]{15}, [underwägs]{16,17:idiom} [d Ähre]{19,20} [abzrupfe]{18}.",
 "MRK.2.24": "Und{1} [d Pharisäer]{2,3} [händ]{4} [zu ihm]{5} [gseit]{4}: «Lueg{6}, wieso{7} [mached si]{8} [am Sabbat]{9,10}, [was]{11} nöd{12} [erlaubt isch]{13}?»",
 "MRK.2.25": "Und{1} [er seit]{2} [zu ine]{3}: «[Händ er]{5} nie{4} [gläse]{5}, was{6} [de David]{8} [gmacht hät]{7}, wo{9} [er in Not gsii isch]{10,11} und{12} [Hunger gha hät]{13}, er{14} und{15} [sini Begleiter]{16-18},",
 "MRK.2.26": "wie{1} [er]{2} [zur Ziit]{8} [vom Hoheprieschter]{10} Abjatar{9} [is]{3,4} [Huus]{5} [vo Gott]{6,7} [ine gange isch]{2} und{11} [d Schaubrot]{12-15} [ggässe hät]{16}, [wo]{17} [ussert]{21,22} [de Prieschter]{23,24} [niemert]{18} [ässe]{20} [därf]{19}, und{25} si au{27} [dene]{28} [ggää hät]{26}, wo [bi]{29} [ihm]{30} [gsii sind]{31}?»",
 "MRK.2.27": "Und{1} [er hät]{2} [zu ine]{3} [gseit]{2}: «[De Sabbat]{4,5} [isch]{9} [für]{6} [de Mänsch]{7,8} [gschaffe worde]{9}, und{10} nöd{11} [de Mänsch]{12,13} [für]{14} [de Sabbat]{15,16}.",
 "MRK.2.28": "Drum{1} [isch]{3} [de Mänschesohn]{4-7} au{8} [Herr]{2} [über de Sabbat]{9,10}.»",
 # ------------------------------------------------------------ Kapitel 3,1–19
 "MRK.3.1": "Und{1} [er isch]{2} wider{3} [in]{4} [e Synagoge]{5} [gange]{2}, und{6} dört{8} [isch]{7} [en Mänsch]{9} [gsii]{7}, [wo]{11} [e verdorreti]{10} [Hand]{12,13} [gha hät]{11}.",
 "MRK.3.2": "Und{1} [si händ]{2} [en]{3} [gnau beobachtet]{2}, öb{4} [er]{7} [en]{8} [am Sabbat]{5,6} [heile wird]{7}, demit{9} [si]{10} [en]{11} [chönd aachlage]{10}.",
 "MRK.3.3": "Und{1} [er seit]{2} [zum Mänsch]{3,4}, [wo]{5} [di]{6} [verdorret]{9} [Hand]{7} [hät]{8}: «[Stand uf]{10} [und chumm i]{11} [d Mitti]{12,13}!»",
 "MRK.3.4": "Und{1} [er seit]{2} [zu ine]{3}: «[Isch es erlaubt]{4}, [am Sabbat]{5,6} [Guets z tue]{7} oder{8} [Bös z tue]{9}, [es Läbe]{10} [z rette]{11} oder{12} [z töte]{13}?» [Si]{14} aber{15} [händ gschwige]{16}.",
 "MRK.3.5": "Und{1} [er hät]{2} [si]{3} [mit]{4} [Zorn]{5} [ringsum aagluegt]{2}, [truurig]{6} [über]{7} [d Verhärtig]{8,9} [vo irem]{12} [Härz]{10,11}, [und seit]{13} [zum Mänsch]{14,15}: «[Streck]{16} [d Hand]{17,18} [us]{16}!» Und{19} [er hät si usgstreckt]{20}, und{21} [sini]{25} [Hand]{23,24} [isch wider gsund worde]{22}.",
 "MRK.3.6": "Und{1} [d Pharisäer]{3,4} [sind usegange]{2} [und händ]{10} grad{5} [mit]{6} [de Herodianer]{7,8} [Root]{9} [ghalte]{10} [gäge]{11} [ihn]{12}, [wie]{13} [si]{15} [en]{14} [chönted umbringe]{15}.",
 "MRK.3.7": "Und{1} [de Jesus]{2,3} [hät sich]{8} [mit]{4} [sine]{7} [Jünger]{5,6} [an]{9} [See]{10,11} [zruggzoge]{8}, und{12} [e grossi]{13} [Schar]{14} [us]{15} Galiläa{16,17} [isch nachecho]{18}. Au{19} [us]{20} Judäa{21,22}",
 "MRK.3.8": "und{1} [us]{2} Jerusalem{3} und{4} [us]{5} Idumäa{6,7} und{8} [vo änet]{9} [em Jordan]{10,11} und{12} [us de Gäged um]{13} Tyros{14} und{15} Sidon{16} [isch]{22} [e grossi]{18} [Schar]{17} [zu]{23} [ihm]{24} [choo]{22}, [wil si ghört händ]{19}, [was er alles]{20} [gmacht hät]{21}.",
 "MRK.3.9": "Und{1} [er hät]{2} [sine]{5} [Jünger]{3,4} [gseit]{2}, dass{6} [es Böötli]{7} [für ihn]{9} [parat sii söll]{8} [wäge]{10} [de Mängi]{11,12}, demit{13} [si]{15} [en]{16} nöd{14} [verdrucked]{15}.",
 "MRK.3.10": "Dänn{2} [er hät]{3} vil{1} [gheilt]{3}, so dass{4} [alli, wo]{10} [Plage]{12} [gha händ]{11}, [sich uf]{5} [en]{6} [gstürzt händ]{5}, [zum]{7} [en]{8} [aazrüere]{9}.",
 "MRK.3.11": "Und{1} [wänn]{6} [di unreine Geischter]{2-5} [en]{7} [gseh händ]{8}, [sind si]{9} [vor ihm]{10} [nidergfalle]{9} und{11} [händ gschroue]{12}: «Du{15} bisch{16} [de Sohn]{17,18} [vo Gott]{19,20}!» ~13(«sägend»; im Doppelpunkt ufgange) ~14(leitet di direkt Red ii)",
 "MRK.3.12": "Und{1} [er hät]{3} [si]{4} [schaarf]{2} [aagfahre]{3}, demit{5} [si]{9} [en]{7} nöd{6} [bekannt]{8} [mached]{9}.",
 "MRK.3.13": "Und{1} [er gaat]{2} [uf]{3} [de Bärg]{4,5} [ufe]{2} und{6} [rüeft]{7} [die]{8} [zu sich]{7}, [wo er sälber]{10} [hät welle]{9}; und{11} [si sind]{12} [zu]{13} [ihm]{14} [choo]{12}.",
 "MRK.3.14": "Und{1} [er hät]{2} [zwölf]{3} [iigsetzt]{2}, demit{4} [si]{5} [bi]{6} [ihm]{7} [sind]{5} und{8} demit{9} [er]{10} [si]{11} [cha uussände]{10}, [zum Verchünde]{12}",
 "MRK.3.15": "und{1} [Vollmacht]{3} [z ha]{2}, [d Dämone]{5,6} [uszriibe]{4}.",
 "MRK.3.16": "Und{1} [er hät]{2} [di Zwölf]{3,4} [iigsetzt]{2}; und{5} [em Simon]{8,9} [hät er]{6} [de Name]{7} Petrus{10} [ggää]{6};",
 "MRK.3.17": "und{1} [de Jakobus]{2}, [de Sohn]{3,4} [vom Zebedäus]{5}, und{6} [de Johannes]{7}, [de Brueder]{8,9} [vom Jakobus]{10,11} – und{12} [ine]{14} [hät er]{13} [de Name]{15} Boanerges{16} [ggää]{13}, [das heisst]{17,18} «[Söhn]{19} [vom Donner]{20}» –,",
 "MRK.3.18": "und{1} [de Andreas]{2} und{3} [de Philippus]{4} und{5} [de Bartholomäus]{6} und{7} [de Matthäus]{8} und{9} [de Thomas]{10} und{11} [de Jakobus]{12}, [de Sohn]{13,14} [vom Alphäus]{15}, und{16} [de Thaddäus]{17} und{18} [de Simon]{19}, [de Kananäer]{20,21},",
 "MRK.3.19": "und{1} [de Judas]{2} Iskariot{3}, [wo]{4} [en]{7} au{5} [usgliferet hät]{6}.",
}

# Übersetzungsentscheidungen: (Stelle, Zieltext, Art, griechisch, wörtlicher, andere Möglichkeiten, Begründung)
DEC_DE = [
 ("MRK.1.1", "Anfang", "literal", "Ἀρχὴ", None, ["Beginn", "Ursprung"], "Der Vers hat kein Verb. Er kann als Überschrift des ganzen Buches gelesen werden oder als Einleitung zu [[MRK.1.2-MRK.1.8]]: Dann ist das Auftreten des Täufers der «Anfang» des Evangeliums. ἀρχή kann auch «Ursprung, Grundlage» heissen."),
 ("MRK.1.1", "Evangeliums", "traditional", "εὐαγγελίου", "der guten Nachricht", ["der Freudenbotschaft"], "εὐαγγέλιον ist die gute Nachricht; im griechischen Sprachgebrauch auch die Siegesmeldung oder die Kunde von Ereignissen im Herrscherhaus. Bei Markus ist es noch keine Buchgattung, sondern die verkündigte Botschaft (vgl. [[MRK.1.14-MRK.1.15]]). «Evangelium» folgt der vertrauten Wiedergabe."),
 ("MRK.1.1", "von Jesus", "interpretive", "Ἰησοῦ", None, ["über Jesus", "Jesu"], "Der Genitiv kann die Nachricht über Jesus meinen oder die Nachricht, die Jesus selbst verkündet (vgl. [[MRK.1.14]]). «von» lässt beides offen."),
 ("MRK.1.1", "Christus", "traditional", "χριστοῦ", "des Gesalbten", ["Messias"], "χριστός gibt das hebräische Wort für «Gesalbter» (Messias) wieder. Bei Markus ist es noch als Titel hörbar (vgl. [[MRK.8.29]]); «Christus» folgt der vertrauten Wiedergabe. Zur Lesart «Sohn Gottes» siehe die Alternativen."),
 ("MRK.1.2", "bei Jesaja, dem Propheten", "literal", "ἐν τῷ Ἠσαΐᾳ τῷ προφήτῃ", None, None, "Das folgende Zitat verbindet [[EXO.23.20]] bzw. [[MAL.3.1]] mit [[ISA.40.3]]; genannt wird nur Jesaja. Zur Lesart «bei den Propheten» siehe die Alternativen."),
 ("MRK.1.2", "Boten", "literal", "ἄγγελόν", None, ["Engel"], "ἄγγελος heisst «Bote»; erst der Zusammenhang zeigt, ob ein Mensch oder ein Engel gemeint ist. Hier ist Johannes gemeint, in [[MRK.1.13]] sind es Engel."),
 ("MRK.1.2", "vor dir her", "adapted", "πρὸ προσώπου σου", "vor deinem Angesicht", None, "Semitische Wendung für «vor dir»."),
 ("MRK.1.3", "des Herrn", "literal", "κυρίου", None, ["JHWHs"], "In [[ISA.40.3]] steht im hebräischen Text der Gottesname, in der griechischen Bibel κύριος. Markus bezieht den «Weg des Herrn» auf Jesus, dem Johannes vorausgeht."),
 ("MRK.1.4", "Umkehr", "interpretive", "μετανοίας", "Sinnesänderung", ["Busse"], "μετάνοια ist wörtlich ein Umdenken. Im biblischen Zusammenhang schwingt die prophetische Aufforderung zur Rückkehr zu Gott mit; «Umkehr» trifft das besser als «Busse», das an Strafe oder Wiedergutmachung denken lässt. Ebenso in [[MRK.1.15]]."),
 ("MRK.1.4", "der Täufer", "literal", "ὁ βαπτίζων", "der Taufende", None, "Partizip mit Artikel, als Beiname gebraucht."),
 ("MRK.1.8", "mit heiligem Geist", "literal", "ἐν πνεύματι ἁγίῳ", None, ["mit dem Heiligen Geist", "im Heiligen Geist"], "Ohne Artikel und im Gegenüber zu «mit Wasser». ἐν kann «mit» oder «in» heissen. In [[MRK.3.29]] steht der Ausdruck mit Artikel («den Heiligen Geist»)."),
 ("MRK.1.10", "aufreissen", "literal", "σχιζομένους", "zerrissen werden", ["sich öffnen", "sich spalten"], "σχίζω heisst spalten, zerreissen; ein gewaltsames Bild, anders als das ruhigere «sich öffnen» bei [[MAT.3.16]] und [[LUK.3.21]]. Dasselbe Verb steht in [[MRK.15.38]] für den Tempelvorhang. Möglicher Anklang an [[ISA.64.1]] («dass du die Himmel zerrissest»)."),
 ("MRK.1.10", "die Himmel", "literal", "τοὺς οὐρανοὺς", None, ["den Himmel"], "Plural wie im Hebräischen; ebenso in [[MRK.1.11]]."),
 ("MRK.1.10", "auf ihn", "interpretive", "εἰς αὐτόν", "in ihn hinein", ["zu ihm"], "εἰς bezeichnet die Richtung «hinein»; manche lesen, dass der Geist in Jesus hineinkommt. Die Parallelen haben «auf» (ἐπί)."),
 ("MRK.1.11", "an dir habe ich Gefallen gefunden", "interpretive", "ἐν σοὶ εὐδόκησα", None, ["an dir habe ich Freude", "dich habe ich erwählt"], "Der Aorist kann zeitlos verstanden werden. Die Himmelsstimme nimmt wohl [[PSA.2.7]] und [[ISA.42.1]] auf."),
 ("MRK.1.12", "treibt", "literal", "ἐκβάλλει", None, ["führt"], "Dasselbe Verb steht für das Austreiben von Dämonen ([[MRK.1.34]]); Markus erzählt drastisch. Präsens wie im Griechischen."),
 ("MRK.1.13", "versucht", "literal", "πειραζόμενος", None, ["auf die Probe gestellt"], "πειράζω heisst prüfen, auf die Probe stellen, auch zur Sünde verleiten. Markus erzählt keinen Inhalt der Versuchung."),
 ("MRK.1.14", "ausgeliefert worden war", "literal", "παραδοθῆναι", None, ["gefangen genommen worden war", "verhaftet worden war"], "παραδίδωμι («ausliefern») verwendet Markus auch für Jesus ([[MRK.3.19]], [[MRK.9.31]]). Die wörtliche Wiedergabe hält diese Verbindung sichtbar."),
 ("MRK.1.15", "Die Zeit ist erfüllt", "literal", "Πεπλήρωται ὁ καιρὸς", None, ["Die Zeit ist gekommen", "Die Frist ist abgelaufen"], "καιρός ist der bestimmte, entscheidende Zeitpunkt, nicht die fortlaufende Zeit. Das Perfekt sagt: Dieser Zeitpunkt ist jetzt da."),
 ("MRK.1.15", "ist nahe gekommen", "literal", "ἤγγικεν", None, ["ist nahe", "ist da", "ist herbeigekommen"], "Das Perfekt von ἐγγίζω beschreibt einen erreichten Zustand. Ob das Reich als schon angebrochen oder als unmittelbar bevorstehend gedacht ist, ist umstritten; «nahe gekommen» lässt beides offen."),
 ("MRK.1.15", "Reich", "traditional", "βασιλεία", "Königsherrschaft", ["Herrschaft", "Königreich"], "βασιλεία meint zuerst die Herrschaft Gottes als Geschehen, nicht ein Gebiet. «Reich Gottes» folgt der vertrauten Wiedergabe und stimmt mit [[MRK.3.24]] überein."),
 ("MRK.1.15", "Kehrt um", "interpretive", "μετανοεῖτε", "Ändert euren Sinn", ["Tut Busse"], "Vgl. [[MRK.1.4]]. Das Präsens fordert eine andauernde Haltung."),
 ("MRK.1.15", "glaubt an das Evangelium", "adapted", "πιστεύετε ἐν τῷ εὐαγγελίῳ", "glaubt im Evangelium", ["vertraut auf das Evangelium"], "Die Verbindung von πιστεύω mit ἐν ist ungewöhnlich; gemeint ist wohl ein Glauben, das sich auf das Evangelium richtet."),
 ("MRK.1.16", "See", "adapted", "θάλασσαν", "Meer", None, "θάλασσα heisst «Meer»; gemeint ist der See Gennesaret. Markus folgt dem semitischen Sprachgebrauch, der auch Binnenseen «Meer» nennt. Ebenso in [[MRK.2.13]] und [[MRK.3.7]]."),
 ("MRK.1.17", "Menschenfischern", "literal", "ἁλιεῖς ἀνθρώπων", "Fischern von Menschen", None, "Wortspiel mit dem Beruf der Angesprochenen. In [[JER.16.16]] ist das Bild des Fischens mit Gericht verbunden; hier steht es für das Sammeln von Menschen."),
 ("MRK.1.22", "Vollmacht", "interpretive", "ἐξουσίαν", "Befugnis", ["Autorität", "Macht"], "ἐξουσία ist übertragene, rechtmässige Befugnis. Das Wort kehrt in [[MRK.1.27]], [[MRK.2.10]] und [[MRK.3.15]] wieder."),
 ("MRK.1.22", "Schriftgelehrten", "traditional", "γραμματεῖς", "Schreiber", ["Gesetzeslehrer"], "γραμματεύς bezeichnet Schreiber und Ausleger des Gesetzes; wie in [[MRK.3.22]]."),
 ("MRK.1.23", "mit einem unreinen", "adapted", "ἐν πνεύματι ἀκαθάρτῳ", "in einem unreinen Geist", ["von einem unreinen Geist besessen"], "ἐν drückt aus, dass der Mensch in der Gewalt des Geistes ist. «Unrein» ist eine kultische Kategorie: was von Gott trennt."),
 ("MRK.1.24", "Was haben wir mit dir zu schaffen", "adapted", "Τί ἡμῖν καὶ σοί", "Was uns und dir?", ["Was willst du von uns?", "Lass uns in Ruhe!"], "Semitische Wendung der Abgrenzung (vgl. [[1KI.17.18]])."),
 ("MRK.1.24", "der Heilige Gottes", "literal", "ὁ ἅγιος τοῦ θεοῦ", None, None, "Der Dämon nennt Jesus beim Namen und Titel; nach antiker Vorstellung verschafft das Kennen des Namens Macht über das Gegenüber."),
 ("MRK.1.25", "fuhr ihn an", "interpretive", "ἐπετίμησεν", "bedrohte ihn", ["gebot ihm", "wies ihn zurecht"], "ἐπιτιμάω heisst scharf zurechtweisen. Markus verwendet das Wort auch für Jesu Wort an Wind und Wellen ([[MRK.4.39]]) und in [[MRK.3.12]]."),
 ("MRK.1.32", "Besessenen", "adapted", "δαιμονιζομένους", "von Dämonen Geplagten", None, "δαιμονίζομαι: unter der Macht eines Dämons stehen."),
 ("MRK.1.31", "sie diente", "literal", "διηκόνει", None, ["sie bewirtete", "sie sorgte für"], "Dasselbe Verb wie bei den Engeln in [[MRK.1.13]]; im Haus meint es zunächst das Bewirten."),
 ("MRK.1.35", "einsamen", "literal", "ἔρημον", "öden", ["verlassenen"], "Dasselbe Wort wie «Wüste» in [[MRK.1.4]] und [[MRK.1.12]]; Markus verbindet so die Orte."),
 ("MRK.1.38", "Kleinstädte", "adapted", "κωμοπόλεις", "Dorfstädte", ["Marktflecken", "Ortschaften"], "κωμόπολις bezeichnet grössere Dörfer ohne Stadtrecht."),
 ("MRK.1.38", "bin ich hinausgegangen", "literal", "ἐξῆλθον", None, ["bin ich gekommen", "bin ich gesandt"], "Gemeint sein kann das Verlassen von Kafarnaum ([[MRK.1.35]]) oder grundsätzlicher die Sendung Jesu (so deutet [[LUK.4.43]]). Wörtlich belassen."),
 ("MRK.1.40", "Aussätziger", "traditional", "λεπρὸς", None, ["Hautkranker"], "λέπρα bezeichnet verschiedene Hautkrankheiten, nicht nur die heutige Lepra. Sie machten nach [[LEV.13.45-LEV.13.46]] kultisch unrein und schlossen aus der Gemeinschaft aus; deshalb «rein machen»."),
 ("MRK.1.41", "von Zorn ergriffen", "literal", "ὀργισθεὶς", "zornig geworden", ["entrüstet", "empört"], "Der SBLGNT liest ὀργισθείς; die anderen erfassten Editionen σπλαγχνισθείς («von Erbarmen ergriffen», siehe Alternativen). Worüber Jesus zornig ist, sagt der Text nicht: über die Krankheit, die Ausgrenzung des Mannes, das «wenn du willst» oder anderes. Vgl. [[MRK.3.5]] und das harte Wort in [[MRK.1.43]]."),
 ("MRK.1.41", "berührte", "adapted", "ἥψατο", None, None, "Das Objekt «ihn» ist ergänzt. αὐτοῦ gehört nach der MACULA-Analyse zu «Hand» («seine Hand»); man kann es auch zu «berührte» ziehen («berührte ihn»)."),
 ("MRK.1.41", "werde rein", "literal", "καθαρίσθητι", None, ["sei rein"], "Passiv: Jesus spricht die Reinigung zu."),
 ("MRK.1.43", "fuhr ihn hart an", "interpretive", "ἐμβριμησάμενος αὐτῷ", "schnaubte ihn an", ["ermahnte ihn streng"], "ἐμβριμάομαι bezeichnet heftige Erregung, ursprünglich das Schnauben. Zusammen mit [[MRK.1.41]] zeigt Markus Jesus mit starken Gefühlen."),
 ("MRK.1.43", "trieb ihn sogleich hinaus", "literal", "εὐθὺς ἐξέβαλεν αὐτόν", None, ["schickte ihn sogleich weg"], "Dasselbe Verb wie beim Austreiben der Dämonen; gemeint ist wohl «wegschicken», aber auffällig hart."),
 ("MRK.1.44", "ihnen zum Zeugnis", "interpretive", "εἰς μαρτύριον αὐτοῖς", None, ["als Beweis für sie", "als Zeugnis gegen sie"], "Wer «sie» sind, bleibt offen (die Priester, das Volk). Das Zeugnis kann die Heilung bestätigen oder als Belastung gemeint sein (vgl. [[MRK.6.11]])."),
 ("MRK.1.45", "Der", "interpretive", "ὁ", None, ["Jesus"], "Meist auf den Geheilten bezogen; einige Ausleger beziehen es auf Jesus, der «das Wort» verkündete. Der Text sagt nur «der aber»."),
 ("MRK.1.45", "die Sache", "interpretive", "τὸν λόγον", "das Wort", ["die Geschichte", "die Botschaft"], "λόγος kann die Geschichte der Heilung meinen oder, wie in [[MRK.2.2]], die Botschaft."),
 ("MRK.2.1", "zu Hause", "interpretive", "ἐν οἴκῳ", "in einem Haus", ["daheim"], "Gemeint ist wohl das Haus von Simon und Andreas ([[MRK.1.29]]) oder ein anderes Haus, in dem Jesus wohnte."),
 ("MRK.2.4", "Matte", "interpretive", "κράβαττον", None, ["Bahre", "Liege", "Pritsche"], "κράβαττος ist die einfache Liege armer Leute."),
 ("MRK.2.4", "nachdem sie es aufgebrochen hatten", "adapted", "ἐξορύξαντες", "nachdem sie es aufgegraben hatten", None, "Dächer einfacher Häuser bestanden aus Balken, Zweigen und Lehm; man konnte sie aufgraben."),
 ("MRK.2.5", "Kind", "literal", "Τέκνον", None, ["mein Sohn"], "Freundliche Anrede; über das Alter sagt sie nichts."),
 ("MRK.2.5", "sind vergeben", "interpretive", "ἀφίενταί", "werden vergeben", None, "Das Präsens kann den Zuspruch im Moment des Sprechens ausdrücken. Das Passiv lässt offen, wer vergibt; die Schriftgelehrten verstehen, dass Jesus beansprucht, was Gott zusteht ([[MRK.2.7]])."),
 ("MRK.2.7", "ausser Gott allein", "adapted", "εἰ μὴ εἷς ὁ θεός", "ausser einer, Gott", ["ausser dem einen Gott"], "εἷς («einer») klingt an das Bekenntnis von [[DEU.6.4]] an."),
 ("MRK.2.7", "Er lästert", "literal", "βλασφημεῖ", None, None, "Lästerung ist hier das Beanspruchen dessen, was Gott vorbehalten ist; vgl. [[MRK.3.28-MRK.3.29]] und [[MRK.14.64]]."),
 ("MRK.2.10", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", ["der Mensch", "dieser Mensch"], "Hier zum ersten Mal bei Markus. Die Wendung kann im Aramäischen einfach «ein Mensch» oder umschreibend «ich» bedeuten; in [[DAN.7.13-DAN.7.14]] ist «einer wie ein Menschensohn» eine Gestalt, der Herrschaft gegeben wird. Markus verwendet sie als Selbstbezeichnung Jesu. Anders [[MRK.3.28]], wo der Plural «die Söhne der Menschen» einfach Menschen meint."),
 ("MRK.2.10", "auf der Erde", "literal", "ἐπὶ τῆς γῆς", None, None, "Betont: Vergebung, die man von Gott im Himmel erwartet, wird hier auf der Erde zugesprochen."),
 ("MRK.2.10", "sagt er zum Gelähmten", "adapted", "λέγει τῷ παραλυτικῷ", None, None, "Der Satz bricht ab; Markus wechselt mitten in der Rede vom Gespräch mit den Schriftgelehrten zur Anrede an den Gelähmten. Der Gedankenstrich macht den Bruch sichtbar."),
 ("MRK.2.12", "ausser sich gerieten", "literal", "ἐξίστασθαι", None, ["staunten", "fassungslos waren"], "Dasselbe Verb steht in [[MRK.3.21]] («Er ist von Sinnen»)."),
 ("MRK.2.14", "Zollstelle", "literal", "τελώνιον", None, ["Zollhaus"], "Kafarnaum lag an einer Grenze und Handelsstrasse."),
 ("MRK.2.15", "in seinem Haus", "interpretive", "ἐν τῇ οἰκίᾳ αὐτοῦ", None, ["in Levis Haus", "in Jesu Haus"], "Unklar, ob das Haus des Levi oder Jesu gemeint ist; [[LUK.5.29]] versteht es als Haus des Levi."),
 ("MRK.2.15", "Zöllner", "traditional", "τελῶναι", "Zollpächter", ["Zolleinnehmer"], "Zöllner galten als Kollaborateure und Betrüger; «Sünder» bezeichnet Menschen, die das Gesetz offenkundig nicht hielten."),
 ("MRK.2.15", "lagen mit", "adapted", "συνανέκειντο", None, ["sassen mit … zu Tisch"], "Bei Festmählern lag man auf Polstern."),
 ("MRK.2.16", "Schriftgelehrten der Pharisäer", "literal", "οἱ γραμματεῖς τῶν Φαρισαίων", None, ["Schriftgelehrten, die zu den Pharisäern gehörten"], "Schriftgelehrte, die der pharisäischen Richtung angehörten."),
 ("MRK.2.16", "Wieso", "interpretive", "Ὅτι", None, ["Er isst ja"], "ὅτι kann als Fragewort («warum?») gelesen werden oder die Rede einleiten: «Er isst mit Zöllnern und Sündern!»"),
 ("MRK.2.17", "rufen", "literal", "καλέσαι", None, ["berufen", "einladen"], "καλέω heisst rufen, berufen, auch zum Mahl einladen; im Zusammenhang des Gastmahls klingt die Einladung mit."),
 ("MRK.2.18", "fasteten", "interpretive", "ἦσαν νηστεύοντες", "waren fastend", ["pflegten zu fasten", "hielten gerade einen Fasttag"], "Die Umschreibung mit «sein» kann einen andauernden Brauch oder eine gerade laufende Fastenzeit meinen."),
 ("MRK.2.19", "die Hochzeitsgäste", "adapted", "οἱ υἱοὶ τοῦ νυμφῶνος", "die Söhne des Brautgemachs", ["die Freunde des Bräutigams"], "Semitische Wendung für die Gäste oder Freunde des Bräutigams."),
 ("MRK.2.21", "ungewalktem", "literal", "ἀγνάφου", None, ["neuem", "noch nicht eingelaufenem"], "Ungewalktes Tuch läuft beim Waschen ein und reisst das alte Gewebe auf."),
 ("MRK.2.22", "jungen Wein", "literal", "οἶνον νέον", None, ["neuen Wein"], "Junger Wein gärt noch; alte Lederschläuche sind spröde und reissen."),
 ("MRK.2.23", "unterwegs", "interpretive", "ὁδὸν ποιεῖν", "einen Weg zu machen", ["sich einen Weg zu bahnen"], "Wörtlich «einen Weg machen». Kann einfach «unterwegs sein» bedeuten oder dass sie sich durch das Feld einen Weg bahnten. Das Abreissen von Ähren auf einem fremden Feld erlaubt [[DEU.23.25]]; der Vorwurf betrifft den Sabbat."),
 ("MRK.2.26", "zur Zeit des Hohenpriesters Abjatar", "interpretive", "ἐπὶ Ἀβιαθὰρ ἀρχιερέως", "unter Abjatar, dem Hohenpriester", ["im Abschnitt über Abjatar"], "Nach [[1SA.21.1-1SA.21.6]] war Ahimelech Priester; sein Sohn Abjatar wurde später bekannter ([[1SA.22.20]]). Erklärungsversuche: ein Versehen; ἐπί bezeichne den Schriftabschnitt; Abjatar sei als der bekanntere genannt. [[MAT.12.4]] und [[LUK.6.4]] lassen den Namen weg."),
 ("MRK.2.26", "Schaubrote", "traditional", "τοὺς ἄρτους τῆς προθέσεως", "Brote der Auslegung", ["Brote der Darbringung"], "Die zwölf Brote, die im Heiligtum vor Gott ausgelegt wurden ([[LEV.24.5-LEV.24.9]])."),
 ("MRK.2.27", "wurde für den Menschen geschaffen", "interpretive", "διὰ τὸν ἄνθρωπον ἐγένετο", "ist um des Menschen willen geworden", ["ist für den Menschen da"], "ἐγένετο («wurde, entstand») kann an die Schöpfung erinnern ([[GEN.2.2-GEN.2.3]]). Der Satz ordnet den Sabbat dem Wohl des Menschen zu; ἄνθρωπος steht für den Menschen allgemein."),
 ("MRK.2.28", "Darum", "interpretive", "ὥστε", "sodass", ["also"], "ὥστε zieht eine Folgerung. Ob sie an [[MRK.2.27]] anschliesst oder an den Anspruch Jesu ([[MRK.2.10]]), wird verschieden gesehen."),
 ("MRK.2.28", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", ["der Mensch"], "Vgl. [[MRK.2.10]]. Wegen [[MRK.2.27]] fragen manche, ob hier der Mensch allgemein gemeint ist; im Zusammenhang bei Markus ist es eher Selbstbezeichnung Jesu."),
 ("MRK.3.1", "verdorrte", "literal", "ἐξηραμμένην", None, ["gelähmte", "abgestorbene"], "Wohl eine Lähmung oder ein Muskelschwund."),
 ("MRK.3.4", "ein Leben", "interpretive", "ψυχὴν", "eine Seele", None, "ψυχή meint hier das Leben."),
 ("MRK.3.5", "Zorn", "literal", "ὀργῆς", None, ["Unwillen"], "Markus nennt Jesu Zorn ausdrücklich; [[MAT.12.13]] und [[LUK.6.10]] haben das nicht. Vgl. [[MRK.1.41]]."),
 ("MRK.3.5", "betrübt", "interpretive", "συλλυπούμενος", "mitbetrübt", ["tief traurig"], "Das zusammengesetzte Verb kann Mitgefühl oder tiefe Trauer ausdrücken."),
 ("MRK.3.5", "die Verhärtung", "literal", "τῇ πωρώσει", None, ["die Verstocktheit", "die Gefühllosigkeit"], "πώρωσις ist eigentlich Verhärtung (wie bei einer Schwiele); das Herz steht für Verstand und Willen."),
 ("MRK.3.6", "Herodianern", "literal", "Ἡρῳδιανῶν", None, ["Anhängern des Herodes"], "Anhänger der Herrscherfamilie des Herodes; ihre genaue Rolle ist unbekannt."),
 ("MRK.3.10", "Plagen", "literal", "μάστιγας", "Geisseln", ["Leiden", "Krankheiten"], "μάστιξ ist die Peitsche; übertragen für schwere Leiden."),
 ("MRK.3.13", "den Berg", "literal", "τὸ ὄρος", None, ["das Bergland"], "Mit Artikel, aber ohne Ortsangabe; der Berg ist in der Bibel oft Ort der Begegnung mit Gott (vgl. [[EXO.19.3]])."),
 ("MRK.3.14", "setzte", "interpretive", "ἐποίησεν", "machte", ["schuf", "bestimmte"], "ποιέω («machen») steht in der griechischen Fassung von [[1SA.12.6]] für das Einsetzen von Mose und Aaron. Die Zwölfzahl erinnert an die zwölf Stämme Israels. Zur Lesart «die er auch Apostel nannte» siehe die Alternativen."),
 ("MRK.3.14", "damit sie bei ihm seien", "literal", "ἵνα ὦσιν μετʼ αὐτοῦ", None, None, "Die erste Bestimmung der Zwölf ist die Gemeinschaft mit Jesus, erst danach die Sendung."),
 ("MRK.3.16", "die Zwölf", "literal", "τοὺς δώδεκα", None, None, "Jetzt mit Artikel: Die Zwölf sind eine feste Gruppe; so bei Markus mehrfach ([[MRK.4.10]], [[MRK.6.7]])."),
 ("MRK.3.16", "Petrus", "literal", "Πέτρον", None, ["Fels"], "Griechisch «Stein, Fels». Markus nennt Simon von da an meist Petrus."),
 ("MRK.3.17", "Söhne des Donners", "literal", "Υἱοὶ Βροντῆς", None, ["Donnersöhne"], "Markus übersetzt den Beinamen Boanerges selbst. Was er bedeutet (Temperament? vgl. [[LUK.9.54]]), ist offen."),
 ("MRK.3.18", "den Kananäer", "literal", "τὸν Καναναῖον", None, ["den Eiferer", "den Zeloten"], "Wohl vom aramäischen Wort für «Eiferer» abgeleitet, nicht von «Kanaan»; [[LUK.6.15]] übersetzt «Zelot»."),
 ("MRK.3.19", "auslieferte", "literal", "παρέδωκεν", None, ["verriet"], "Dasselbe Verb wie in [[MRK.1.14]] für Johannes; «ausliefern» hält die Verbindung sichtbar, «verraten» betont den Vertrauensbruch."),
]

DEC_GSW = [
 ("MRK.1.1", "De Aafang", "literal", "Ἀρχὴ", None, ["De Beginn", "De Ursprung"], "De Vers hät kei Verb. Me cha en als Überschrift vom ganze Buech läse oder als Iileitig zu [[MRK.1.2-MRK.1.8]]: Dänn isch s Uftrete vom Täufer de «Aafang» vom Evangelium."),
 ("MRK.1.1", "Evangelium", "traditional", "εὐαγγελίου", "vo de guete Nachricht", ["vo de Fröidebotschaft"], "εὐαγγέλιον isch di guet Nachricht; bim Markus no kei Buechgattig, sondern d Botschaft, wo verchündet wird (vgl. [[MRK.1.14-MRK.1.15]])."),
 ("MRK.1.1", "vo Jesus", "interpretive", "Ἰησοῦ", None, ["über de Jesus"], "Es cha d Nachricht über de Jesus gmeint sii oder d Nachricht, wo de Jesus sälber verchündet (vgl. [[MRK.1.14]]). «vo» laat beides offe."),
 ("MRK.1.1", "Christus", "traditional", "χριστοῦ", "vom Gsalbte", ["Messias"], "χριστός git s hebräisch Wort für «Gsalbte» (Messias) wider. Zur Läsart «Sohn vo Gott» lueg d Alternative."),
 ("MRK.1.2", "bim Jesaja, em Prophet", "literal", "ἐν τῷ Ἠσαΐᾳ τῷ προφήτῃ", None, None, "S Zitat verbindet [[EXO.23.20]] bzw. [[MAL.3.1]] mit [[ISA.40.3]]; gnännt wird nu de Jesaja. Zur Läsart «bi de Prophete» lueg d Alternative."),
 ("MRK.1.2", "Bote", "literal", "ἄγγελόν", None, ["Ängel"], "ἄγγελος heisst «Bote»; da isch de Johannes gmeint, i [[MRK.1.13]] sinds Ängel."),
 ("MRK.1.3", "vom Herr", "literal", "κυρίου", None, ["vo JHWH"], "I [[ISA.40.3]] staat im hebräische Text de Gottesname, i de griechische Bible κύριος. De Markus bezieht de «Wäg vom Herr» uf de Jesus."),
 ("MRK.1.4", "Umkehr", "interpretive", "μετανοίας", "Umdänke", ["Buess"], "μετάνοια isch wörtlich es Umdänke; mitgmeint isch d Rückkehr zu Gott. «Buess» tönt nach Straf. Gliich i [[MRK.1.15]]."),
 ("MRK.1.8", "mit heilige Geischt", "literal", "ἐν πνεύματι ἁγίῳ", None, ["mit em Heilige Geischt"], "Ohni Artikel, im Gägesatz zu «mit Wasser». I [[MRK.3.29]] mit Artikel."),
 ("MRK.1.10", "ufriisse", "literal", "σχιζομένους", None, ["sich uftue"], "σχίζω heisst spalte, verriisse; es gwaltsams Bild. S gliich Verb staat i [[MRK.15.38]] für de Vorhang im Tempel. Villicht Aaklang a [[ISA.64.1]]."),
 ("MRK.1.11", "a dir han ich Gfalle gfunde", "interpretive", "ἐν σοὶ εὐδόκησα", None, ["a dir han ich Fröid"], "D Stimm us em Himmel nimmt wahrschiinli [[PSA.2.7]] und [[ISA.42.1]] uf."),
 ("MRK.1.12", "tribt", "literal", "ἐκβάλλει", None, ["füert"], "S gliich Verb wie bim Dämone-Ustriibe ([[MRK.1.34]])."),
 ("MRK.1.14", "usgliferet worde isch", "literal", "παραδοθῆναι", None, ["verhaftet worde isch"], "παραδίδωμι («usliefere») bruucht de Markus au für de Jesus ([[MRK.3.19]], [[MRK.9.31]])."),
 ("MRK.1.15", "D Ziit isch erfüllt", "literal", "Πεπλήρωται ὁ καιρὸς", None, ["D Ziit isch choo"], "καιρός isch de bestimmt, entscheidend Ziitpunkt; dä isch jetzt da."),
 ("MRK.1.15", "isch nöch choo", "literal", "ἤγγικεν", None, ["isch da"], "Öb s Riich scho aagfange hät oder grad bevorstaat, isch umstritte; «nöch choo» laat beides offe."),
 ("MRK.1.15", "s Riich", "traditional", "ἡ βασιλεία", "d Chönigsherrschaft", ["d Herrschaft"], "βασιλεία meint zersch d Herrschaft vo Gott als Gscheh, nöd es Gebiet. Gliich wie i [[MRK.3.24]] («Riich»)."),
 ("MRK.1.15", "Chehred um", "interpretive", "μετανοεῖτε", "Dänked um", ["Tüend Buess"], "Vgl. [[MRK.1.4]]."),
 ("MRK.1.16", "See", "adapted", "θάλασσαν", "Meer", None, "Gmeint isch de See Gennesaret; semitisch heisst au en See «Meer»."),
 ("MRK.1.17", "Mänschefischer", "literal", "ἁλιεῖς ἀνθρώπων", None, None, "Es Wortspiil mit em Bruef vo de Aagredte."),
 ("MRK.1.22", "Vollmacht", "interpretive", "ἐξουσίαν", "Befuegnis", ["Autorität"], "ἐξουσία isch rächtmässigi, übertreiti Befuegnis; s Wort chunnt i [[MRK.1.27]], [[MRK.2.10]] und [[MRK.3.15]] wider."),
 ("MRK.1.24", "Was händ mir mit dir z tue", "adapted", "Τί ἡμῖν καὶ σοί", "Was eus und dir?", ["Was wottsch vo eus?"], "Semitischi Wändig, wo Abgränzig uusdruckt (vgl. [[1KI.17.18]])."),
 ("MRK.1.25", "aagfahre", "interpretive", "ἐπετίμησεν", "bedroht", ["zrächtgwise"], "ἐπιτιμάω heisst schaarf zrächtwiise; au i [[MRK.4.39]] und [[MRK.3.12]]."),
 ("MRK.1.40", "Ussätzige", "traditional", "λεπρὸς", None, ["Hautchranke"], "λέπρα sind verschideni Hautchranket, nöd nu di hütig Lepra; si händ nach [[LEV.13.45-LEV.13.46]] unrein gmacht und us de Gmeinschaft uusgschlosse."),
 ("MRK.1.41", "voll Zorn", "literal", "ὀργισθεὶς", "zornig worde", ["empört"], "De SBLGNT list ὀργισθείς, di andere erfasste Usgabe σπλαγχνισθείς («voll Erbarme», lueg d Alternative). Über was de Jesus zornig isch, seit de Text nöd. Vgl. [[MRK.3.5]] und [[MRK.1.43]]."),
 ("MRK.1.41", "aagrüert", "adapted", "ἥψατο", None, None, "S Objekt «en» isch ergänzt; αὐτοῦ ghört nach de MACULA-Analyse zu «Hand»."),
 ("MRK.1.43", "hert aagschnauzt", "interpretive", "ἐμβριμησάμενος", "aagschnaubt", ["sträng ermahnt"], "ἐμβριμάομαι isch heftigi Erregig, ursprünglich s Schnaube."),
 ("MRK.1.45", "Dä", "interpretive", "ὁ", None, ["de Jesus"], "Meischt uf de Gheilt bezoge; es paar Usleger beziehnd s uf de Jesus."),
 ("MRK.2.4", "Matte", "interpretive", "κράβαττον", None, ["Bahre", "Liegi"], "κράβαττος isch di eifach Liegi vo arme Lüüt."),
 ("MRK.2.5", "Chind", "literal", "Τέκνον", None, ["min Sohn"], "Fründlichi Aared; über s Alter seit si nüüt."),
 ("MRK.2.7", "ussert Gott elei", "adapted", "εἰ μὴ εἷς ὁ θεός", "ussert eine, Gott", None, "εἷς («eine») klingt as Bekänntnis vo [[DEU.6.4]] aa."),
 ("MRK.2.10", "de Mänschesohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", ["de Mänsch"], "Da zum erschte Mal bim Markus. Aramäisch cha d Wändig eifach «en Mänsch» oder umschriibend «ich» heisse; i [[DAN.7.13-DAN.7.14]] isch es e Gstalt, wo Herrschaft übercho hät. Bim Markus e Sälbschtbezeichnig vom Jesus. Andersch [[MRK.3.28]]: «d Söhn vo de Mänsche» = d Mänsche."),
 ("MRK.2.10", "seit er zum Glähmte", "adapted", "λέγει τῷ παραλυτικῷ", None, None, "De Satz bricht ab; de Gedankestrich macht de Wächsel vo de Schriftgleerte zum Glähmte sichtbar."),
 ("MRK.2.12", "usser sich gsii sind", "literal", "ἐξίστασθαι", None, ["gstuunet händ"], "S gliich Verb staat i [[MRK.3.21]] («Er isch nüme bi Troscht»)."),
 ("MRK.2.15", "Zöllner", "traditional", "τελῶναι", "Zollpächter", None, "Zöllner händ als Kollaborateure und Betrüger gulte."),
 ("MRK.2.16", "Wieso", "interpretive", "Ὅτι", None, ["Er isst ja"], "ὅτι cha Frogwort sii («wieso?») oder d Red iileite."),
 ("MRK.2.19", "d Hochziitsgäscht", "adapted", "οἱ υἱοὶ τοῦ νυμφῶνος", "d Söhn vom Brutgmach", None, "Semitischi Wändig für d Gäscht oder Fründ vom Brüütigam."),
 ("MRK.2.21", "Blätz", "adapted", "ἐπίβλημα", "Ufsatz", ["Flick"], "Schwiizerdüütsch «Blätz» = Flickstuck."),
 ("MRK.2.23", "underwägs", "interpretive", "ὁδὸν ποιεῖν", "en Wäg z mache", ["sich en Wäg z bahne"], "Wörtlich «en Wäg mache». S Ährerupfe uf eme fremde Fäld erlaubt [[DEU.23.25]]; de Vorwurf gaat um de Sabbat."),
 ("MRK.2.26", "zur Ziit vom Hoheprieschter Abjatar", "interpretive", "ἐπὶ Ἀβιαθὰρ ἀρχιερέως", "under em Abjatar, em Hoheprieschter", ["im Abschnitt über de Abjatar"], "Nach [[1SA.21.1-1SA.21.6]] isch de Ahimelech Prieschter gsii, sin Sohn Abjatar spöter bekannter. Erklärigsversüech: es Versehe; ἐπί meini de Schriftabschnitt; de bekannter Name sig gnännt. [[MAT.12.4]] und [[LUK.6.4]] lönd de Name weg."),
 ("MRK.2.26", "d Schaubrot", "traditional", "τοὺς ἄρτους τῆς προθέσεως", "d Brot vo de Uuslegig", None, "Di zwölf Brot, wo im Heiligtum vor Gott uusgleit worde sind ([[LEV.24.5-LEV.24.9]])."),
 ("MRK.2.27", "isch für de Mänsch gschaffe worde", "interpretive", "διὰ τὸν ἄνθρωπον ἐγένετο", "isch wäge em Mänsch worde", ["isch für de Mänsch da"], "ἐγένετο cha a d Schöpfig erinnere ([[GEN.2.2-GEN.2.3]]). De Sabbat isch em Wohl vom Mänsch zueordnet."),
 ("MRK.2.28", "de Mänschesohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", ["de Mänsch"], "Vgl. [[MRK.2.10]]; wäge [[MRK.2.27]] fröged es paar, öb da de Mänsch allgemein gmeint isch."),
 ("MRK.3.4", "es Läbe", "interpretive", "ψυχὴν", "e Seel", None, "ψυχή meint da s Läbe."),
 ("MRK.3.5", "Zorn", "literal", "ὀργῆς", None, None, "De Markus nännt de Zorn vom Jesus usdrücklich; [[MAT.12.13]] und [[LUK.6.10]] nöd."),
 ("MRK.3.5", "d Verhärtig", "literal", "τῇ πωρώσει", None, ["d Verstocktheit"], "πώρωσις isch Verhärtig wie bi nere Schwiele; s Härz staat für Verstand und Wille."),
 ("MRK.3.14", "iigsetzt", "interpretive", "ἐποίησεν", "gmacht", ["bestimmt"], "D Zwölfzahl erinneret a di zwölf Stämm vo Israel. Zur Läsart «wo-n-er au Apostel gnännt hät» lueg d Alternative."),
 ("MRK.3.16", "di Zwölf", "literal", "τοὺς δώδεκα", None, None, "Jetzt mit Artikel: e feschti Gruppe ([[MRK.4.10]], [[MRK.6.7]])."),
 ("MRK.3.17", "Söhn vom Donner", "literal", "Υἱοὶ Βροντῆς", None, ["Donnersöhn"], "De Markus übersetzt de Bii-Name Boanerges sälber; was er bedüütet, isch offe (vgl. [[LUK.9.54]])."),
 ("MRK.3.18", "de Kananäer", "literal", "τὸν Καναναῖον", None, ["de Iiferer", "de Zelot"], "Wahrschiinli vom aramäische Wort für «Iiferer», nöd vo «Kanaan»; [[LUK.6.15]] seit «Zelot»."),
 ("MRK.3.19", "usgliferet hät", "literal", "παρέδωκεν", None, ["verrate hät"], "S gliich Verb wie i [[MRK.1.14]] für de Johannes."),
]

# Lesarten, die die Übersetzung verändern: (Lesart, Stelle, de von, de zu, gsw von, gsw zu, Wirkung, Hinweis de, Hinweis gsw,
#  Wörter {Lesart: [(griechisch, de, Hinweis)]}, Wörter gsw, Entstehung de, Entstehung gsw)
AUTO = "Laut der automatischen Zuordnung (WREAD-CNTR-MRK-…)"
ALTS = [
 ("VAR-SBLGNTAPP-MRK-001-001-01:R2", "MRK.1.1", "von Jesus Christus.", "von Jesus Christus, dem Sohn Gottes.", "vo Jesus Christus.", "vo Jesus Christus, em Sohn vo Gott.", "bedeutsam",
  "Mit dem Zusatz nennt schon die Überschrift Jesus «Sohn Gottes», wie später die Himmelsstimme ([[MRK.1.11]]) und der Hauptmann ([[MRK.15.39]]). Die Editionen sind geteilt.",
  "Mit em Zuesatz nännt scho d Überschrift de Jesus «Sohn vo Gott», wie spöter d Stimm us em Himmel ([[MRK.1.11]]) und de Hauptme ([[MRK.15.39]]). D Usgabe sind teilt.",
  {"R1": [("χριστοῦ", "Christus", "ohne Zusatz; SBLGNT, WH")], "R2": [("χριστοῦ υἱοῦ θεοῦ", "Christus, Sohn Gottes", "Treg, NA28")], "R3": [("χριστοῦ υἱοῦ τοῦ θεοῦ", "Christus, des Sohnes Gottes", "mit Artikel; RP")]},
  {"R1": [("χριστοῦ", "Christus", "ohni Zuesatz; SBLGNT, WH")], "R2": [("χριστοῦ υἱοῦ θεοῦ", "Christus, Sohn vo Gott", "Treg, NA28")], "R3": [("χριστοῦ υἱοῦ τοῦ θεοῦ", "Christus, em Sohn vo Gott", "mit Artikel; RP")]},
  ["Die Namen wurden als Kürzel geschrieben (ΙΥ ΧΥ ΥΥ ΘΥ). Bei einer solchen Reihe gleich endender Kürzel konnte ein Schreiber leicht zwei davon überspringen; der kurze Text wäre dann ein Versehen.",
   "Umgekehrt kann der Titel als feierliche Erweiterung am Buchanfang ergänzt worden sein; der kürzere Text ist bei Anfängen besonders gut sichtbar und weniger leicht übersehen.",
   "Die automatische Zuordnung konnte die Handschriften hier wegen der Kürzel keiner Lesart zuweisen. Im erfassten Wortlaut der CNTR-Transkription fehlt der Zusatz beim Sinaiticus in der Erstschrift; eine Korrektur ergänzt ihn. Alexandrinus hat ihn mit Artikel, Vaticanus, Washingtonianus und Bezae ohne Artikel. Ephraemi und 𝔓137 sind an dieser Stelle nicht erhalten. Ein Amulett des 6. Jh. (PSI 6.719) wird dem Zusatz zugeordnet. Sekundärtranskription, keine eigene Prüfung."],
  ["D Näme sind als Chürzel gschribe worde (ΙΥ ΧΥ ΥΥ ΘΥ). Bi so nere Reihe vo gliich ändende Chürzel hät en Schriiber liecht zwei überspringe chöne; dänn wär de churz Text es Versehe.",
   "Umgekeert cha de Titel als feierlichi Erwiiterig am Buechaafang ergänzt worde sii.",
   "D automatisch Zueornig hät d Handschrifte da wäge de Chürzel keinere Läsart chöne zueteile. Im erfasste Wortlut vo de CNTR-Transkription fehlt de Zuesatz bim Sinaiticus i de Erschtschrift; e Korrektur ergänzt en. De Alexandrinus hät en mit Artikel, de Vaticanus, de Washingtonianus und de Bezae ohni. De Ephraemi und 𝔓137 sind a dere Stell nöd erhalte. Es Amulett usem 6. Jh. (PSI 6.719) wird em Zuesatz zueteilt. Sekundärtranskription, kei eigeti Prüefig."]),
 ("VAR-SBLGNTAPP-MRK-001-002-02:R2", "MRK.1.2", "bei Jesaja, dem Propheten", "bei den Propheten", "bim Jesaja, em Prophet", "bi de Prophete", "mittel",
  "Mit «bei den Propheten» passt die Quellenangabe zum Mischzitat aus [[MAL.3.1]] und [[ISA.40.3]].",
  "Mit «bi de Prophete» passt d Quelleaagab zum gmischte Zitat us [[MAL.3.1]] und [[ISA.40.3]].",
  {"R1": [("ἐν τῷ Ἠσαΐᾳ τῷ προφήτῃ", "bei Jesaja, dem Propheten", "SBLGNT, WH, Treg, NA28")], "R2": [("ἐν τοῖς προφήταις", "bei den Propheten", "RP")]},
  {"R1": [("ἐν τῷ Ἠσαΐᾳ τῷ προφήτῃ", "bim Jesaja, em Prophet", "SBLGNT, WH, Treg, NA28")], "R2": [("ἐν τοῖς προφήταις", "bi de Prophete", "RP")]},
  ["Da das Zitat nicht nur aus Jesaja stammt, konnte ein Schreiber die Angabe zu «den Propheten» berichtigen; die Nennung Jesajas wäre dann die schwierigere, ursprünglichere Lesart.",
   "Umgekehrt kann «Jesaja» eingesetzt worden sein, weil der bekannteste Teil des Zitats ([[ISA.40.3]]) aus Jesaja stammt.",
   AUTO + " lesen Sinaiticus, Vaticanus und Bezae «Jesaja» (Bezae ohne Artikel), Alexandrinus und Washingtonianus «die Propheten». Ephraemi und 𝔓137 sind an dieser Stelle nicht erhalten."],
  ["Wil s Zitat nöd nu us em Jesaja stammt, hät en Schriiber d Aagab zu «de Prophete» chöne verbessere; dänn wär «Jesaja» di schwierigeri, ursprünglicheri Läsart.",
   "Umgekeert cha «Jesaja» iigsetzt worde sii, wil de bekanntischt Teil vom Zitat ([[ISA.40.3]]) us em Jesaja chunnt.",
   "Nach de automatische Zueornig läsed de Sinaiticus, de Vaticanus und de Bezae «Jesaja» (de Bezae ohni Artikel), de Alexandrinus und de Washingtonianus «d Prophete». De Ephraemi und 𝔓137 sind a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-001-014-02:R2", "MRK.1.14", "das Evangelium Gottes", "das Evangelium vom Reich Gottes", "s Evangelium vo Gott", "s Evangelium vom Riich vo Gott", "gering",
  "Der Zusatz nimmt das Stichwort «Reich Gottes» aus [[MRK.1.15]] vorweg.",
  "De Zuesatz nimmt s Stichwort «Riich vo Gott» us [[MRK.1.15]] vorwäg.",
  {"R1": [("τὸ εὐαγγέλιον τοῦ θεοῦ", "das Evangelium Gottes", "SBLGNT, WH, Treg, NA28")], "R2": [("τὸ εὐαγγέλιον τῆς βασιλείας τοῦ θεοῦ", "das Evangelium vom Reich Gottes", "RP")]},
  {"R1": [("τὸ εὐαγγέλιον τοῦ θεοῦ", "s Evangelium vo Gott", "SBLGNT, WH, Treg, NA28")], "R2": [("τὸ εὐαγγέλιον τῆς βασιλείας τοῦ θεοῦ", "s Evangelium vom Riich vo Gott", "RP")]},
  ["Der Zusatz kann aus dem folgenden Vers oder aus der geläufigen Wendung «Evangelium vom Reich» ([[MAT.4.23]]) stammen; dass er absichtlich gestrichen wurde, ist weniger naheliegend.",
   AUTO + " haben Sinaiticus und Vaticanus den kurzen Text, Alexandrinus, Washingtonianus und Bezae den Zusatz. Ephraemi und 𝔓137 sind an dieser Stelle nicht erhalten."],
  ["De Zuesatz cha us em nächschte Vers oder us de gläufige Wändig «Evangelium vom Riich» ([[MAT.4.23]]) stamme.",
   "Nach de automatische Zueornig händ de Sinaiticus und de Vaticanus de churz Text, de Alexandrinus, de Washingtonianus und de Bezae de Zuesatz. De Ephraemi und 𝔓137 sind a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-001-021-02:R2", "MRK.1.21", "lehrte er in der Synagoge", "ging er in die Synagoge und lehrte", "hät er i de Synagoge gleert", "isch er i d Synagoge gange und hät gleert", "gering",
  "Der Sinn bleibt gleich; die Lesart sagt ausdrücklich, dass Jesus hineinging. Hier weicht der SBLGNT von allen anderen erfassten Editionen ab.",
  "De Sinn bliibt gliich; d Läsart seit usdrücklich, dass de Jesus inegange isch. Da wiicht de SBLGNT vo allne andere erfasste Usgabe ab.",
  {"R1": [("ἐδίδασκεν εἰς τὴν συναγωγήν", "lehrte in (hinein in) die Synagoge", "SBLGNT, WH am Rand")], "R2": [("εἰσελθὼν εἰς τὴν συναγωγὴν ἐδίδασκεν", "ging in die Synagoge und lehrte", "WH, Treg, NA28, RP")]},
  {"R1": [("ἐδίδασκεν εἰς τὴν συναγωγήν", "hät i (ine i) d Synagoge gleert", "SBLGNT, WH am Rand")], "R2": [("εἰσελθὼν εἰς τὴν συναγωγὴν ἐδίδασκεν", "isch i d Synagoge gange und hät gleert", "WH, Treg, NA28, RP")]},
  ["«Lehren» mit εἰς («hinein») ist ungewöhnlich; ein Schreiber konnte das mit «hineingehen» glätten. Umgekehrt kann das Partizip beim Abschreiben ausgefallen sein.",
   AUTO + " liest Sinaiticus den kurzen Text (mit der Form ἐδίδαξεν), Alexandrinus, Vaticanus, Washingtonianus und Bezae den langen; Ephraemi liest anders als beide. 𝔓137 ist nicht erhalten."],
  ["«Leere» mit εἰς («ine») isch ungwöhnlich; en Schriiber hät das mit «inegaa» chöne glätte. Umgekeert cha s Partizip bim Abschriibe usgfalle sii.",
   "Nach de automatische Zueornig list de Sinaiticus de churz Text (mit de Form ἐδίδαξεν), de Alexandrinus, de Vaticanus, de Washingtonianus und de Bezae de lang; de Ephraemi list andersch. 𝔓137 isch nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-001-041-02:R2", "MRK.1.41", "von Zorn ergriffen", "von Erbarmen ergriffen", "voll Zorn", "voll Erbarme", "bedeutsam",
  "Die Lesarten zeichnen Jesus gegensätzlich: zornig oder voll Mitgefühl. Der SBLGNT folgt hier dem Rand von Westcott/Hort; die übrigen erfassten Editionen lesen «von Erbarmen ergriffen».",
  "D Läsarte zeichned de Jesus gägesätzlich: zornig oder voll Mitgfühl. De SBLGNT folgt da em Rand vo Westcott/Hort; di andere erfasste Usgabe läsed «voll Erbarme».",
  {"R1": [("ὀργισθεὶς", "von Zorn ergriffen", "SBLGNT, WH am Rand")], "R2": [("σπλαγχνισθεὶς", "von Erbarmen ergriffen", "WH, Treg, NA28, RP")]},
  {"R1": [("ὀργισθεὶς", "voll Zorn", "SBLGNT, WH am Rand")], "R2": [("σπλαγχνισθεὶς", "voll Erbarme", "WH, Treg, NA28, RP")]},
  ["Zorn als Regung Jesu konnte anstössig wirken; ein Schreiber hätte ihn eher durch Erbarmen ersetzt als umgekehrt. Matthäus und Lukas nennen an dieser Stelle gar kein Gefühl. Das spricht für «Zorn» als schwierigere Lesart.",
   "Für «Erbarmen» sprechen die breite Bezeugung und der Zusammenhang einer Heilungsbitte; es wird auch vermutet, dass zwei ähnliche Wörter in einer aramäischen Vorlage verwechselt wurden (Hypothese).",
   AUTO + " hat nur Bezae «von Zorn ergriffen»; Sinaiticus, Alexandrinus, Vaticanus, Washingtonianus und Ephraemi lesen «von Erbarmen ergriffen». 𝔓137 ist nicht erhalten."],
  ["Zorn als Regig vom Jesus hät chöne aastössig wirke; en Schriiber hät en ehner dur Erbarme ersetzt als umgekeert. De Matthäus und de Lukas nänned da gar kei Gfüel. Das redt für «Zorn» als schwierigeri Läsart.",
   "Für «Erbarme» reded di breit Bezüügig und de Zämehang vo nere Bitt um Heilig; mänggi vermueted au, dass zwei ähnlichi Wörter imene aramäische Vorbild verwächslet worde sind (Hypothese).",
   "Nach de automatische Zueornig hät nu de Bezae «voll Zorn»; de Sinaiticus, de Alexandrinus, de Vaticanus, de Washingtonianus und de Ephraemi läsed «voll Erbarme». 𝔓137 isch nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-002-016-07:R2", "MRK.2.16", "Sündern?»", "Sündern und trinkt?»", "Sünder?»", "Sünder und trinkt?»", "gering",
  "Der Zusatz vervollständigt das Bild des Mahls.", "De Zuesatz macht s Bild vom Ässe vollständig.",
  {"R1": [("ἐσθίει", "isst er", "SBLGNT, WH, NA28")], "R2": [("ἐσθίει καὶ πίνει", "isst und trinkt er", "Treg, RP")]},
  {"R1": [("ἐσθίει", "isst er", "SBLGNT, WH, NA28")], "R2": [("ἐσθίει καὶ πίνει", "isst und trinkt er", "Treg, RP")]},
  ["«Essen und trinken» ist eine geläufige Doppelwendung und steht in der Parallele [[LUK.5.30]]; der Zusatz kann von dort stammen.",
   AUTO + " haben Sinaiticus, Vaticanus und Washingtonianus den kurzen Text, Alexandrinus und 𝔓88 (4. Jh.) den Zusatz; Ephraemi und Bezae lesen anders als beide."],
  ["«Ässe und trinke» isch e gläufigi Doppelwändig und staat i de Parallele [[LUK.5.30]]; de Zuesatz cha vo dört stamme.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Vaticanus und de Washingtonianus de churz Text, de Alexandrinus und 𝔓88 (4. Jh.) de Zuesatz; de Ephraemi und de Bezae läsed andersch."]),
 ("VAR-SBLGNTAPP-MRK-002-017-02:R2", "MRK.2.17", "sondern Sünder.»", "sondern Sünder zur Umkehr.»", "sondern Sünder.»", "sondern Sünder zur Umkehr.»", "gering",
  "Der Zusatz nennt ausdrücklich das Ziel des Rufens.", "De Zuesatz seit usdrücklich, wozue grüeft wird.",
  {"R1": [("ἁμαρτωλούς", "Sünder", "SBLGNT, WH, Treg, NA28")], "R2": [("ἁμαρτωλοὺς εἰς μετάνοιαν", "Sünder zur Umkehr", "RP")]},
  {"R1": [("ἁμαρτωλούς", "Sünder", "SBLGNT, WH, Treg, NA28")], "R2": [("ἁμαρτωλοὺς εἰς μετάνοιαν", "Sünder zur Umkehr", "RP")]},
  ["Die Parallele [[LUK.5.32]] hat «zur Umkehr»; der Zusatz kann von dort übernommen sein.",
   AUTO + " hat nur Ephraemi den Zusatz; Sinaiticus, Alexandrinus, Vaticanus, Washingtonianus, Bezae und 𝔓88 haben den kurzen Text."],
  ["D Parallele [[LUK.5.32]] hät «zur Umkehr»; de Zuesatz cha vo dört übernoo sii.",
   "Nach de automatische Zueornig hät nu de Ephraemi de Zuesatz; de Sinaiticus, de Alexandrinus, de Vaticanus, de Washingtonianus, de Bezae und 𝔓88 händ de churz Text."]),
 ("VAR-SBLGNTAPP-MRK-003-014-01:R2", "MRK.3.14", "Und er setzte zwölf ein,", "Und er setzte zwölf ein, die er auch Apostel nannte,", "Und er hät zwölf iigsetzt,", "Und er hät zwölf iigsetzt, wo-n-er au Apostel gnännt hät,", "mittel",
  "Mit dem Zusatz erhalten die Zwölf schon hier den Titel «Apostel» (vgl. [[MRK.6.30]]). Die Editionen sind geteilt.",
  "Mit em Zuesatz überchömed d Zwölf scho da de Titel «Apostel» (vgl. [[MRK.6.30]]). D Usgabe sind teilt.",
  {"R1": [("δώδεκα", "zwölf", "SBLGNT, Treg, RP")], "R2": [("δώδεκα οὓς καὶ ἀποστόλους ὠνόμασεν", "zwölf, die er auch Apostel nannte", "WH, NA28")]},
  {"R1": [("δώδεκα", "zwölf", "SBLGNT, Treg, RP")], "R2": [("δώδεκα οὓς καὶ ἀποστόλους ὠνόμασεν", "zwölf, wo-n-er au Apostel gnännt hät", "WH, NA28")]},
  ["Der Satz steht wörtlich in [[LUK.6.13]]; er kann von dort in Markus eingedrungen sein.",
   "Umgekehrt kann er beim Abschreiben ausgefallen sein; die Wiederholung «er setzte die Zwölf ein» in [[MRK.3.16]] wirkt wie eine Wiederaufnahme nach einem Einschub.",
   AUTO + " haben Sinaiticus, Vaticanus, Washingtonianus und Ephraemi den Zusatz, Alexandrinus nicht; Bezae liest anders als beide. 0315 ist nicht erhalten."],
  ["De Satz staat wörtlich i [[LUK.6.13]]; er cha vo dört in Markus iidrunge sii.",
   "Umgekeert cha-n-er bim Abschriibe usgfalle sii; d Widerholig «er hät di Zwölf iigsetzt» i [[MRK.3.16]] würkt wie-n-e Wideraanaa nach eme Iischub.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Vaticanus, de Washingtonianus und de Ephraemi de Zuesatz, de Alexandrinus nöd; de Bezae list andersch. 0315 isch nöd erhalte."]),
 ("VAR-SBLGNTAPP-MRK-003-015-01:R2", "MRK.3.15", "die Dämonen auszutreiben", "die Krankheiten zu heilen und die Dämonen auszutreiben", "d Dämone uszriibe", "d Chrankete z heile und d Dämone uszriibe", "gering",
  "Der Zusatz erweitert den Auftrag um das Heilen.", "De Zuesatz erwiiteret de Uftrag um s Heile.",
  {"R1": [("ἐξουσίαν ἐκβάλλειν", "Vollmacht, auszutreiben", "SBLGNT, WH, Treg, NA28")], "R2": [("ἐξουσίαν θεραπεύειν τὰς νόσους καὶ ἐκβάλλειν", "Vollmacht, die Krankheiten zu heilen und auszutreiben", "RP")]},
  {"R1": [("ἐξουσίαν ἐκβάλλειν", "Vollmacht, uszriibe", "SBLGNT, WH, Treg, NA28")], "R2": [("ἐξουσίαν θεραπεύειν τὰς νόσους καὶ ἐκβάλλειν", "Vollmacht, d Chrankete z heile und uszriibe", "RP")]},
  ["Die Parallele [[MAT.10.1]] nennt Heilen und Austreiben zusammen; der Zusatz kann von dort stammen.",
   AUTO + " haben Sinaiticus, Vaticanus und Ephraemi den kurzen Text, Alexandrinus, Washingtonianus und Bezae den Zusatz."],
  ["D Parallele [[MAT.10.1]] nännt Heile und Ustriibe zäme; de Zuesatz cha vo dört stamme.",
   "Nach de automatische Zueornig händ de Sinaiticus, de Vaticanus und de Ephraemi de churz Text, de Alexandrinus, de Washingtonianus und de Bezae de Zuesatz."]),
 ("VAR-SBLGNTAPP-MRK-003-016-01:R2", "MRK.3.16", "Und er setzte die Zwölf ein; und dem Simon", "Und dem Simon", "Und er hät di Zwölf iigsetzt; und em Simon", "Und em Simon", "gering",
  "Ohne den Satz schliesst die Namensliste direkt an [[MRK.3.15]] an.", "Ohni de Satz schliesst d Nämeliischte diräkt a [[MRK.3.15]] aa.",
  {"R1": [("καὶ ἐποίησεν τοὺς δώδεκα καὶ ἐπέθηκεν", "und er setzte die Zwölf ein, und er gab", "SBLGNT, WH, NA28")], "R2": [("καὶ ἐπέθηκεν", "und er gab", "Treg, RP")]},
  {"R1": [("καὶ ἐποίησεν τοὺς δώδεκα καὶ ἐπέθηκεν", "und er hät di Zwölf iigsetzt, und er hät ggää", "SBLGNT, WH, NA28")], "R2": [("καὶ ἐπέθηκεν", "und er hät ggää", "Treg, RP")]},
  ["Nach [[MRK.3.14]] wirkt der Satz überflüssig und kann deshalb weggelassen worden sein; er kann auch als Wiederaufnahme nach dem Einschub in [[MRK.3.14]] ergänzt worden sein.",
   AUTO + " haben Vaticanus und Ephraemi den Satz, Sinaiticus, Alexandrinus, Washingtonianus und Bezae nicht. 0315 ist nicht erhalten."],
  ["Nach [[MRK.3.14]] würkt de Satz überflüssig und cha drum weggloo worde sii; er cha aber au als Wideraanaa nach em Iischub i [[MRK.3.14]] ergänzt worde sii.",
   "Nach de automatische Zueornig händ de Vaticanus und de Ephraemi de Satz, de Sinaiticus, de Alexandrinus, de Washingtonianus und de Bezae nöd. 0315 isch nöd erhalte."]),
]

UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung)
 ("TU-MRK-001-001-045", "MRK.1.1-MRK.1.45", "section", "Der Anfang des Evangeliums",
  ["TU-MRK-001-001-008", "TU-MRK-001-009-011", "TU-MRK-001-012-013", "TU-MRK-001-014-015", "TU-MRK-001-016-020",
   "TU-MRK-001-021-028", "TU-MRK-001-029-034", "TU-MRK-001-035-039", "TU-MRK-001-040-045"],
  "Johannes der Täufer kündigt einen Stärkeren an. Jesus wird getauft, vom Geist in die Wüste getrieben und verkündet in Galiläa das nahe Reich Gottes. Er beruft die ersten Jünger, lehrt mit Vollmacht, treibt Dämonen aus, heilt Kranke und macht einen Aussätzigen rein; sein Ruf verbreitet sich so, dass er sich nicht mehr offen zeigen kann."),
 ("TU-MRK-001-001-008", "MRK.1.1-MRK.1.8", "narrative", "Johannes der Täufer", None,
  "Nach der Überschrift beginnt das Buch mit einem Schriftwort und dem Auftreten des Johannes in der Wüste. Er tauft zur Vergebung der Sünden und kündigt einen Stärkeren an, der mit heiligem Geist taufen wird."),
 ("TU-MRK-001-009-011", "MRK.1.9-MRK.1.11", "narrative", "Die Taufe Jesu", None,
  "Jesus kommt aus Nazaret und lässt sich von Johannes taufen. Er sieht die Himmel aufreissen und den Geist herabkommen; eine Stimme nennt ihn den geliebten Sohn."),
 ("TU-MRK-001-012-013", "MRK.1.12-MRK.1.13", "narrative", "In der Wüste", None,
  "Der Geist treibt Jesus in die Wüste; dort wird er vierzig Tage vom Satan versucht, ist bei den wilden Tieren, und Engel dienen ihm."),
 ("TU-MRK-001-014-015", "MRK.1.14-MRK.1.15", "narrative_with_saying", "Das Reich Gottes ist nahe", None,
  "Nach der Auslieferung des Johannes verkündet Jesus in Galiläa: Die Zeit ist erfüllt, das Reich Gottes ist nahe gekommen; kehrt um und glaubt an das Evangelium."),
 ("TU-MRK-001-016-020", "MRK.1.16-MRK.1.20", "narrative", "Die ersten Jünger", None,
  "Am See ruft Jesus die Fischer Simon und Andreas, dann Jakobus und Johannes. Sie lassen Netze, Boot und Vater zurück und folgen ihm."),
 ("TU-MRK-001-021-028", "MRK.1.21-MRK.1.28", "narrative", "Vollmacht in der Synagoge von Kafarnaum", None,
  "Jesus lehrt am Sabbat mit Vollmacht, anders als die Schriftgelehrten. Ein unreiner Geist erkennt ihn als den Heiligen Gottes; Jesus bringt ihn zum Schweigen und treibt ihn aus. Die Kunde verbreitet sich in ganz Galiläa."),
 ("TU-MRK-001-029-034", "MRK.1.29-MRK.1.34", "narrative", "Heilungen am Abend", None,
  "Im Haus von Simon und Andreas richtet Jesus die fiebernde Schwiegermutter auf. Am Abend bringt man alle Kranken und Besessenen; er heilt viele und verbietet den Dämonen zu reden."),
 ("TU-MRK-001-035-039", "MRK.1.35-MRK.1.39", "narrative", "Aufbruch in andere Orte", None,
  "Jesus betet früh an einem einsamen Ort. Als die Jünger ihn suchen, will er weiterziehen, um auch anderswo zu verkünden, und zieht durch ganz Galiläa."),
 ("TU-MRK-001-040-045", "MRK.1.40-MRK.1.45", "narrative", "Ein Aussätziger wird rein", None,
  "Ein Aussätziger bittet Jesus: «Wenn du willst, kannst du mich rein machen.» Jesus berührt ihn und macht ihn rein, schickt ihn zum Priester und gebietet Schweigen. Der Mann erzählt es überall, sodass Jesus nicht mehr offen in eine Stadt gehen kann."),
 ("TU-MRK-002-001-028", "MRK.2.1-MRK.2.28", "section", "Streitgespräche in Galiläa",
  ["TU-MRK-002-001-012", "TU-MRK-002-013-017", "TU-MRK-002-018-022", "TU-MRK-002-023-028"],
  "In vier Szenen gerät Jesus mit Schriftgelehrten und Pharisäern in Streit: über die Vergebung von Sünden, das Essen mit Zöllnern und Sündern, das Fasten und den Sabbat. Mit [[MRK.3.1-MRK.3.6]] bilden sie eine Reihe von Streitgesprächen, die mit dem Beschluss endet, Jesus umzubringen."),
 ("TU-MRK-002-001-012", "MRK.2.1-MRK.2.12", "narrative", "Der Gelähmte und die Vergebung der Sünden", None,
  "Vier Männer bringen einen Gelähmten durch das Dach zu Jesus. Er spricht ihm die Vergebung der Sünden zu; die Schriftgelehrten nennen das Lästerung. Jesus heilt den Mann, damit sie erkennen, dass der Menschensohn auf der Erde Vollmacht hat, Sünden zu vergeben."),
 ("TU-MRK-002-013-017", "MRK.2.13-MRK.2.17", "narrative", "Levi und das Mahl mit Zöllnern", None,
  "Jesus ruft den Zöllner Levi und isst mit vielen Zöllnern und Sündern. Auf den Einwand der Schriftgelehrten antwortet er: Nicht die Gesunden brauchen den Arzt; er ist gekommen, Sünder zu rufen."),
 ("TU-MRK-002-018-022", "MRK.2.18-MRK.2.22", "dialogue", "Die Frage nach dem Fasten", None,
  "Man fragt, warum Jesu Jünger nicht fasten. Er antwortet mit dem Bild der Hochzeitsgäste, die nicht fasten, solange der Bräutigam da ist, und mit den Bildern vom neuen Flicken und vom jungen Wein."),
 ("TU-MRK-002-023-028", "MRK.2.23-MRK.2.28", "dialogue", "Ähren am Sabbat", None,
  "Die Jünger rupfen am Sabbat Ähren. Jesus verweist auf David, der die Schaubrote ass, und sagt: Der Sabbat wurde für den Menschen geschaffen, nicht der Mensch für den Sabbat; der Menschensohn ist Herr auch über den Sabbat."),
 ("TU-MRK-003-001-019", "MRK.3.1-MRK.3.19", "section", "Heilung am Sabbat, Andrang und die Zwölf",
  ["TU-MRK-003-001-006", "TU-MRK-003-007-012", "TU-MRK-003-013-019"],
  "Jesus heilt am Sabbat eine verdorrte Hand; daraufhin beraten Pharisäer und Herodianer, wie sie ihn umbringen können. Eine grosse Menge aus allen Gegenden strömt zu ihm. Auf dem Berg setzt er die Zwölf ein."),
 ("TU-MRK-003-001-006", "MRK.3.1-MRK.3.6", "narrative", "Die verdorrte Hand", None,
  "In der Synagoge fragt Jesus, ob man am Sabbat Leben retten oder töten dürfe. Zornig und betrübt über die Verhärtung der Herzen heilt er die Hand. Die Pharisäer beschliessen mit den Herodianern, ihn umzubringen."),
 ("TU-MRK-003-007-012", "MRK.3.7-MRK.3.12", "narrative", "Andrang am See", None,
  "Menschen aus Galiläa, Judäa, Jerusalem, Idumäa, Transjordanien und der Gegend von Tyros und Sidon kommen zu Jesus. Kranke drängen sich, ihn zu berühren; die unreinen Geister rufen ihn als Sohn Gottes aus, und er verbietet es ihnen."),
 ("TU-MRK-003-013-019", "MRK.3.13-MRK.3.19", "narrative", "Die Einsetzung der Zwölf", None,
  "Auf dem Berg ruft Jesus, die er will, und setzt zwölf ein: Sie sollen bei ihm sein, verkündigen und Dämonen austreiben. Die Liste nennt ihre Namen und Beinamen, zuletzt Judas Iskariot, der ihn auslieferte."),
]
UNITS_GSW = {
 "TU-MRK-001-001-045": ("De Aafang vom Evangelium", "De Johannes de Täufer chündet en Stärchere aa. De Jesus wird tauft, vom Geischt i d Wüeschti tribe und verchündet z Galiläa, dass s Riich vo Gott nöch isch. Er rüeft di erschte Jünger, leert mit Vollmacht, tribt Dämone us, heilt Chranki und macht en Ussätzige rein; sin Ruef verbreitet sich eso, dass er sich nüme offe cha zeige."),
 "TU-MRK-001-001-008": ("De Johannes de Täufer", "Nach de Überschrift fangt s Buech mit eme Schriftwort und em Uftrete vom Johannes i de Wüeschti aa. Er tauft zur Vergäbig vo de Sünde und chündet en Stärchere aa, wo mit heilige Geischt wird taufe."),
 "TU-MRK-001-009-011": ("D Taufi vom Jesus", "De Jesus chunnt vo Nazaret und laat sich vom Johannes taufe. Er gseht d Himmel ufriisse und de Geischt abecho; e Stimm nännt en de liebi Sohn."),
 "TU-MRK-001-012-013": ("I de Wüeschti", "De Geischt tribt de Jesus i d Wüeschti; dört wird er vierzg Täg vom Satan versuecht, isch bi de wilde Tier, und Ängel dieneds em."),
 "TU-MRK-001-014-015": ("S Riich vo Gott isch nöch", "Nachdem de Johannes usgliferet worde isch, verchündet de Jesus z Galiläa: D Ziit isch erfüllt, s Riich vo Gott isch nöch choo; chehred um und glaubed as Evangelium."),
 "TU-MRK-001-016-020": ("Di erschte Jünger", "Am See rüeft de Jesus d Fischer Simon und Andreas, dänn de Jakobus und de Johannes. Si lönd Netz, Boot und Vatter zrugg und gönd em nache."),
 "TU-MRK-001-021-028": ("Vollmacht i de Synagoge vo Kafarnaum", "De Jesus leert am Sabbat mit Vollmacht, andersch als d Schriftgleerte. En unreine Geischt kännt en als de Heilig vo Gott; de Jesus bringt en zum Schwiige und tribt en us. De Ruef verbreitet sich i ganz Galiläa."),
 "TU-MRK-001-029-034": ("Heilige am Abig", "Im Huus vom Simon und vom Andreas richtet de Jesus d Schwigermueter mit Fieber uf. Am Abig bringt me alli Chranke und Bsässne; er heilt vil und verbüütet de Dämone z rede."),
 "TU-MRK-001-035-039": ("Ufbruch i anderi Ort", "De Jesus bättet am früene Morge amene einsame Ort. Wo d Jünger en sueched, wott er wiiterzie, zum au anderswo verchünde, und zieht dur ganz Galiläa."),
 "TU-MRK-001-040-045": ("En Ussätzige wird rein", "En Ussätzige bittet de Jesus: «Wänn du wottsch, chasch du mich rein mache.» De Jesus rüert en aa und macht en rein, schickt en zum Prieschter und verbüütet em, öppis z säge. De Maa verzellt s überall, so dass de Jesus nüme offe in e Stadt cha."),
 "TU-MRK-002-001-028": ("Striitgspröch z Galiläa", "I vier Szene chunnt de Jesus mit Schriftgleerte und Pharisäer in Striit: über s Vergää vo Sünde, s Ässe mit Zöllner und Sünder, s Faschte und de Sabbat. Mit [[MRK.3.1-MRK.3.6]] bildeds e Reihe vo Striitgspröch, wo mit em Beschluss ändet, de Jesus umzbringe."),
 "TU-MRK-002-001-012": ("De Glähmt und s Vergää vo de Sünde", "Vier Manne bringed en Glähmte dur s Dach zum Jesus. Er seit em zue, dass sini Sünde vergää sind; d Schriftgleerte nänned das Läschterig. De Jesus heilt de Maa, demit si gsehnd, dass de Mänschesohn uf de Ärde Vollmacht hät, Sünde z vergää."),
 "TU-MRK-002-013-017": ("De Levi und s Ässe mit Zöllner", "De Jesus rüeft de Zöllner Levi und isst mit vilne Zöllner und Sünder. Uf de Iiwand vo de Schriftgleerte seit er: Nöd di Gsunde bruuched en Dokter; er isch choo, zum Sünder rüefe."),
 "TU-MRK-002-018-022": ("D Frog nach em Faschte", "Me fröget, wieso d Jünger vom Jesus nöd faschted. Er antwortet mit em Bild vo de Hochziitsgäscht, wo nöd faschted, solang de Brüütigam da isch, und mit de Bilder vom nöie Blätz und vom nöie Wii."),
 "TU-MRK-002-023-028": ("Ähre am Sabbat", "D Jünger rupfed am Sabbat Ähre ab. De Jesus verwiist uf de David, wo d Schaubrot ggässe hät, und seit: De Sabbat isch für de Mänsch gschaffe worde, nöd de Mänsch für de Sabbat; de Mänschesohn isch au Herr über de Sabbat."),
 "TU-MRK-003-001-019": ("Heilig am Sabbat, Aadrang und di Zwölf", "De Jesus heilt am Sabbat e verdorreti Hand; drufabe beroted Pharisäer und Herodianer, wie si en chönted umbringe. E grossi Mängi us allne Gägede chunnt zu ihm. Uf em Bärg setzt er di Zwölf ii."),
 "TU-MRK-003-001-006": ("Di verdorret Hand", "I de Synagoge fröget de Jesus, öb me am Sabbat Läbe rette oder töte törf. Zornig und truurig über di verhärtete Härz heilt er d Hand. D Pharisäer beschliessed mit de Herodianer, en umzbringe."),
 "TU-MRK-003-007-012": ("Aadrang am See", "Lüüt us Galiläa, Judäa, Jerusalem, Idumäa, vo änet em Jordan und us de Gäged vo Tyros und Sidon chömed zum Jesus. Chranki drängled sich, zum en aazrüere; di unreine Geischter rüefed en als Sohn vo Gott us, und er verbüütet ene das."),
 "TU-MRK-003-013-019": ("D Iisetzig vo de Zwölf", "Uf em Bärg rüeft de Jesus die, wo-n-er wott, und setzt zwölf ii: Si söled bi ihm sii, verchünde und Dämone ustriibe. D Liischte nännt iri Näme und Bii-Näme, zletscht de Judas Iskariot, wo-n-en usgliferet hät."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten in den Alternativen beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1, "
  "WREAD-CNTR-MRK-001-001-045, WREAD-CNTR-MRK-002-001-028, WREAD-CNTR-MRK-003-001-019) bzw. auf dem dort erfassten Wortlaut der "
  "CNTR-Transkription, nicht auf eigener Prüfung der Handschriften."),
 ("Die Übersetzung folgt an allen Apparatstellen dem SBLGNT (follows_readings), auch wo er von den anderen erfassten Editionen abweicht: "
  "[[MRK.1.21]] (lehrte «in die Synagoge») und [[MRK.1.41]] («von Zorn ergriffen»)."),
 ("Markus reiht Sätze mit καί («und») und erzählt oft im Präsens (historisches Präsens: «er sagt», «sie kommen»). Beides ist "
  "weitgehend beibehalten, damit der Erzählstil hörbar bleibt; εὐθύς ist meist mit «sogleich» wiedergegeben."),
 ("Abgrenzung: [[MRK.3.20-MRK.3.35]] ist in eigenen Arbeitsübersetzungen erfasst (TRANS-MRK-003-020-021-DE-WORKING, "
  "TRANS-MRK-003-022-030-DE-WORKING, TRANS-MRK-003-031-035-DE-WORKING); Begriffe wie «Reich», «Geist», «Schriftgelehrte», «Menge» "
  "sind darauf abgestimmt."),
 "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf em erfasste Wortlut vo de "
  "CNTR-Transkription, nöd uf eigeter Prüefig vo de Handschrifte."),
 "D Übersetzig folgt a allne Apparatstelle em SBLGNT, au i [[MRK.1.21]] und [[MRK.1.41]] («voll Zorn»).",
 ("Abgränzig: [[MRK.3.20-MRK.3.35]] staat i TRANS-MRK-003-020-035-GSW-ZH-WORKING; Wörter wie «Riich», «Geischt», «Schriftgleerte», "
  "«Mängi» sind druf abgstimmt."),
]


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
               "segmentation_note_de": ("Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
                                        + (" [[MRK.1.1]] kann auch als Überschrift des ganzen Buches für sich stehen." if uid == "TU-MRK-001-001-045" else "")
                                        + (" [[MRK.3.20-MRK.3.35]] bildet die eigene Einheit TU-MRK-003-020-035." if uid == "TU-MRK-003-001-019" else ""))
               if parts else None,
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
        refs_c = [f"MRK.{c}.{v}" for v in range(1, last + 1)]
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
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Artikel vor Personennamen. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MRK-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/markus_text_01_03.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Markus 1,1–3,19 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
