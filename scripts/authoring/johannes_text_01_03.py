#!/usr/bin/env python3
"""Autorenwerkzeug: Johannes 1–3 (Prolog, Täuferzeugnis, erste Jünger, Kana, Tempel, Nikodemus) – Texteinheiten,
Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und
vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/johannes_text_01_03.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-JHN besteht bereits und wird hier nur referenziert, nicht geschrieben.

Diese Datei ist die erste der Johannes-Reihe. Ihre translation_notes legen die Grundentscheide für das ganze
Evangelium dar (Schlüsselwörter, «die Juden», Redegrenzen, Mundart); die Dateien der weiteren Kapitel verweisen darauf.

Besonderheiten:
- In Johannes 1–3 fehlt im SBLGNT kein Vers (per Skript geprüft); alle Verse haben Tokens.
- [[JHN.1.3]]/[[JHN.1.4]]: Der SBLGNT setzt den Punkt vor ὃ γέγονεν und zieht die Worte zum folgenden Satz. Die
  Übersetzung folgt dieser Zeichensetzung; die andere steht in decisions.
- [[JHN.1.15]] steht im SBLGNT in runden Klammern; die Übersetzung übernimmt sie.
- [[JHN.3.31]]: Der SBLGNT-Apparat verzeichnet keine Variante; nach den CNTR-Transkriptionen fehlt die zweite Wendung
  «ist über allen» in 01, 05 und 𝔓75. Das steht in decisions und translation_notes, nicht als Alternative.

KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1)
bzw. aus den CNTR-Transkriptionen (Sekundärtranskription), nicht aus eigener Prüfung der Handschriften. Zahlen zu
Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts (data/annotations) ermittelt.
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
CHAPTERS = ((1, 51), (2, 25), (3, 36))

DE = {
 # ------------------------------------------------------------ Kapitel 1
 "JHN.1.1": "[Im]{1} [Anfang]{2} [war]{3} [das Wort]{4,5}, und{6} [das Wort]{7,8} [war]{9} [bei]{10} [Gott]{11,12}, und{13} [das Wort]{16,17} [war]{15} [Gott]{14}.",
 "JHN.1.2": "[Dieses]{1} [war]{2} [im]{3} [Anfang]{4} [bei]{5} [Gott]{6,7}.",
 "JHN.1.3": "[Alles]{1} [ist]{4} [durch]{2} [es]{3} [geworden]{4}, und{5} [ohne]{6} [es]{7} [ist]{8} [auch nicht]{9} [eines]{10} [geworden]{8}. [Was]{11} [geworden ist]{12} –",
 "JHN.1.4": "[in]{1} [ihm]{2} [war]{4} [Leben]{3}, und{5} [das Leben]{6,7} [war]{8} [das Licht]{9,10} [der Menschen]{11,12}.",
 "JHN.1.5": "Und{1} [das Licht]{2,3} [scheint]{7} [in]{4} [der Finsternis]{5,6}, und{8} [die Finsternis]{9,10} [hat]{13} [es]{11} [nicht]{12} [erfasst]{13}.",
 "JHN.1.6": "[Es trat]{1} [ein Mensch]{2} [auf]{1}, [gesandt]{3} [von]{4} [Gott]{5}; [sein]{7} [Name]{6} war [Johannes]{8}.",
 "JHN.1.7": "[Dieser]{1} [kam]{2} [zum]{3} [Zeugnis]{4}, [um]{5} [vom]{7,8} [Licht]{9} [Zeugnis abzulegen]{6}, [damit]{10} [alle]{11} [durch]{13} [ihn]{14} [zum Glauben kämen]{12}.",
 "JHN.1.8": "[Er]{3} [war]{2} [nicht]{1} [das Licht]{4,5}, [sondern]{6} [er sollte]{7} [vom]{9,10} [Licht]{11} [Zeugnis ablegen]{8}.",
 "JHN.1.9": "[Das]{2,4} [wahre]{5} [Licht]{3}, [das]{6} [jeden]{8} [Menschen]{9} [erleuchtet]{7}, [kam]{1,10} [in]{11} [die Welt]{12,13}.",
 "JHN.1.10": "[Er war]{4} [in]{1} [der Welt]{2,3}, und{5} [die Welt]{6,7} [ist]{10} [durch]{8} [ihn]{9} [geworden]{10}, und{11} [die Welt]{12,13} [hat]{16} [ihn]{14} [nicht]{15} [erkannt]{16}.",
 "JHN.1.11": "[Er kam]{4} [in]{1} [sein Eigentum]{2,3}, und{5} [die Seinen]{6,7} [nahmen]{10} [ihn]{8} [nicht]{9} [auf]{10}.",
 "JHN.1.12": "[Allen]{1} [aber]{2}, [die]{1} [ihn]{4} [aufnahmen]{3}, [gab er]{5} [die Vollmacht]{7}, [Kinder]{8} [Gottes]{9} [zu werden]{10}, [denen, die]{11} [an]{13} [seinen]{16} [Namen]{14,15} [glauben]{12}, ~6(αὐτοῖς «ihnen» nimmt «allen, die» auf; nicht eigens wiedergegeben)",
 "JHN.1.13": "[die]{1} [nicht]{2} [aus]{3} [Blut]{4} [noch]{5} [aus]{6} [dem Willen]{7} [des Fleisches]{8} [noch]{9} [aus]{10} [dem Willen]{11} [eines Mannes]{12}, [sondern]{13} [aus]{14} [Gott]{15} [geboren sind]{16}.",
 "JHN.1.14": "Und{1} [das Wort]{2,3} [wurde]{5} [Fleisch]{4} und{6} [wohnte]{7} [unter]{8} [uns]{9}, und{10} [wir haben]{11} [seine]{14} [Herrlichkeit]{12,13} [geschaut]{11}, [eine Herrlichkeit]{15} [wie]{16} [die des Einzigen]{17} [vom]{18} [Vater]{19}, [voller]{20} [Gnade]{21} und{22} [Wahrheit]{23}.",
 "JHN.1.15": "([Johannes]{1} [legt]{2} [über]{3} [ihn]{4} [Zeugnis ab]{2} und{5} [ruft]{6}: «[Dieser]{8} [war es]{9}, [von dem]{10} [ich sagte]{11}: ‹[Der]{12} [nach]{13} [mir]{14} [kommt]{15}, [ist]{18} [mir]{17} [voraus]{16}, [denn]{19} [er war]{22} [vor]{20} [mir]{21}.›») ~7(λέγων «sagend» leitet die direkte Rede ein)",
 "JHN.1.16": "[Denn]{1} [aus]{2} [seiner]{5} [Fülle]{3,4} [haben]{8} [wir]{6} [alle]{7} [empfangen]{8}, und{9} [Gnade]{10} [um]{11} [Gnade]{12}.",
 "JHN.1.17": "[Denn]{1} [das Gesetz]{2,3} [wurde]{6} [durch]{4} [Mose]{5} [gegeben]{6}, [die Gnade]{7,8} und{9} [die Wahrheit]{10,11} [sind]{15} [durch]{12} Jesus{13} Christus{14} [gekommen]{15}.",
 "JHN.1.18": "[Gott]{1} [hat]{3} [niemand]{2} [je]{4} [gesehen]{3}; [der Einzige]{5}, [Gott]{6}, [der]{7} [an]{9} [der Brust]{10,11} [des Vaters]{12,13} [ist]{8}, [er]{14} [hat Kunde gebracht]{15}.",
 "JHN.1.19": "Und{1} [dies]{2} [ist]{3} [das Zeugnis]{4,5} [des Johannes]{6,7}, [als]{8} [die Juden]{10,11} [aus]{12} [Jerusalem]{13} [Priester]{14} und{15} [Leviten]{16} [sandten]{9}, [um]{17} [ihn]{19} [zu fragen]{18}: «[Wer]{21} [bist]{22} [du]{20}?»",
 "JHN.1.20": "Und{1} [er bekannte]{2} und{3} [leugnete]{5} [nicht]{4}, und{6} [er bekannte]{7}: «[Ich]{9} [bin]{11} [nicht]{10} [der Christus]{12,13}.» ~8(ὅτι leitet die direkte Rede ein)",
 "JHN.1.21": "Und{1} [sie fragten]{2} [ihn]{3}: «[Was]{4} [dann]{5}? [Bist]{8} [du]{6} [Elija]{7}?» Und{9} [er sagt]{10}: «[Ich bin es]{12} [nicht]{11}.» «[Bist]{15} [du]{16} [der Prophet]{13,14}?» Und{17} [er antwortete]{18}: «[Nein]{19}.»",
 "JHN.1.22": "[Da]{2} [sagten sie]{1} [zu ihm]{3}: «[Wer]{4} [bist du]{5}? [Damit]{6} [wir]{8} [denen, die]{9} [uns]{11} [gesandt haben]{10}, [eine Antwort]{7} [geben können]{8}: [Was]{12} [sagst du]{13} [über]{14} [dich selbst]{15}?»",
 "JHN.1.23": "[Er sagte]{1}: «[Ich]{2} bin [die Stimme]{3} [eines Rufenden]{4} [in]{5} [der Wüste]{6,7}: ‹[Macht]{8} [den Weg]{9,10} [des Herrn]{11} [gerade]{8}!›, [wie]{12} [Jesaja]{14}, [der Prophet]{15,16}, [gesagt hat]{13}.»",
 "JHN.1.24": "Und{1} [sie waren]{3} [von]{4} [den Pharisäern]{5,6} [gesandt]{2}.",
 "JHN.1.25": "Und{1} [sie fragten]{2} [ihn]{3} und{4} [sagten]{5} [zu ihm]{6}: «[Warum]{7} [taufst du]{9} [dann]{8}, [wenn]{10} [du]{11} [nicht]{12} [der Christus]{14,15} [bist]{13}, [nicht]{16} [Elija]{17} [und nicht]{18} [der Prophet]{19,20}?»",
 "JHN.1.26": "[Johannes]{3,4} [antwortete]{1} [ihnen]{2}: «[Ich]{6} [taufe]{7} [mit]{8} [Wasser]{9}; [mitten]{10} [unter euch]{11} [steht]{12} einer, [den]{13} [ihr]{14} [nicht]{15} [kennt]{16}, ~5(λέγων «sagend» leitet die direkte Rede ein)",
 "JHN.1.27": "[der]{1} [nach]{2} [mir]{3} [kommt]{4}; [dessen]{5} [bin ich]{7} [nicht]{6} [würdig]{8}, [dass]{9} [ich]{10} [ihm]{11} [den Riemen]{12,13} [seiner Sandale]{14,15} [löse]{10}.»",
 "JHN.1.28": "[Dies]{1} [geschah]{4} [in]{2} [Betanien]{3} [jenseits]{5} [des Jordan]{6,7}, [wo]{8} [Johannes]{10,11} [taufte]{9,12}.",
 "JHN.1.29": "[Am folgenden Tag]{1,2} [sieht er]{3} [Jesus]{4,5} [zu]{7} [sich]{8} [kommen]{6} und{9} [sagt]{10}: «[Siehe]{11}, [das Lamm]{12,13} [Gottes]{14,15}, [das]{16} [die Sünde]{18,19} [der Welt]{20,21} [wegnimmt]{17}!",
 "JHN.1.30": "[Dieser]{1} [ist es]{2}, [von]{3} [dem]{4} [ich]{5} [gesagt habe]{6}: ‹[Nach]{7} [mir]{8} [kommt]{9} [ein Mann]{10}, [der]{11} [mir]{13} [voraus]{12} [ist]{14}, [denn]{15} [er war]{18} [vor]{16} [mir]{17}.›",
 "JHN.1.31": "[Und ich]{1} [kannte]{3} [ihn]{4} [nicht]{2}; [aber]{5} [damit]{6} [er]{7} [Israel]{8,9} [offenbart werde]{7}, [deshalb]{10,11} [bin]{12} [ich]{13} [gekommen]{12} [und taufe]{16} [mit]{14} [Wasser]{15}.»",
 "JHN.1.32": "Und{1} [Johannes]{3} [bezeugte]{2}: «[Ich habe]{6} [den Geist]{7,8} [wie]{10} [eine Taube]{11} [vom]{12} [Himmel]{13} [herabkommen]{9} [sehen]{6}, und{14} [er blieb]{15} [auf]{16} [ihm]{17}. ~4(λέγων «sagend» leitet die direkte Rede ein) ~5(ὅτι leitet die direkte Rede ein)",
 "JHN.1.33": "[Und ich]{1} [kannte]{3} [ihn]{4} [nicht]{2}; [aber]{5} [der]{6} [mich]{8} [gesandt hat]{7}, [mit]{10} [Wasser]{11} [zu taufen]{9}, [der]{12} [hat]{14} [mir]{13} [gesagt]{14}: ‹[Auf wen]{15,16} [du]{18} [auch]{17} [den Geist]{19,20} [herabkommen]{21} und{22} [auf]{24} [ihm]{25} [bleiben]{23} [siehst]{18}, [der]{26} [ist es]{27}, [der]{28} [mit]{30} [heiligem]{32} [Geist]{31} [tauft]{29}.›",
 "JHN.1.34": "[Und ich]{1} [habe es gesehen]{2} und{3} [habe bezeugt]{4}: [Dieser]{6} [ist]{7} [der Erwählte]{8,9} [Gottes]{10,11}.» ~5(ὅτι leitet den Inhalt des Zeugnisses ein; durch den Doppelpunkt wiedergegeben)",
 "JHN.1.35": "[Am folgenden Tag]{1,2} [stand]{4} [Johannes]{5,6} [wieder]{3} da und{7} [zwei]{12} [von]{8} [seinen]{9,11} [Jüngern]{10},",
 "JHN.1.36": "und{1} [er blickte]{2} [auf Jesus]{3,4}, [der vorüberging]{5}, und [sagt]{6}: «[Siehe]{7}, [das Lamm]{8,9} [Gottes]{10,11}!»",
 "JHN.1.37": "Und{1} [die]{3} [zwei]{4} [Jünger]{5} [hörten]{2} [ihn]{6} [reden]{7} und{8} [folgten]{9} [Jesus]{10,11}.",
 "JHN.1.38": "[Jesus]{3,4} [aber]{2} [wandte sich um]{1}, und{5} [als er]{6} [sie]{7} [folgen]{8} [sah]{6}, [sagt er]{9} [zu ihnen]{10}: «[Was]{11} [sucht ihr]{12}?» [Sie]{13} [aber]{14} [sagten]{15} [zu ihm]{16}: «[Rabbi]{17} ([das]{18} [heisst]{19} [übersetzt]{20}: [Lehrer]{21}), [wo]{22} [ist deine Bleibe]{23}?»",
 "JHN.1.39": "[Er sagt]{1} [zu ihnen]{2}: «[Kommt]{3}, und{4} [ihr werdet sehen]{5}!» [Da]{7} [kamen sie]{6} und{8} [sahen]{9}, [wo]{10} [seine Bleibe war]{11}, und{12} [sie blieben]{15} [jenen]{18} [Tag]{16,17} [bei]{13} [ihm]{14}; [es war]{20} [ungefähr]{21} [die zehnte]{22} [Stunde]{19}.",
 "JHN.1.40": "[Andreas]{2}, [der Bruder]{3,4} [des Simon]{5} [Petrus]{6}, [war]{1} [einer]{7} [von]{8} [den]{9} [zweien]{10}, [die]{11} es [von]{13} [Johannes]{14} [gehört hatten]{12} und{15} [ihm]{17} [gefolgt waren]{16}.",
 "JHN.1.41": "[Er]{2} [findet]{1} [zuerst]{3} [seinen eigenen]{6,7} [Bruder]{4,5} [Simon]{8} und{9} [sagt]{10} [zu ihm]{11}: «[Wir haben]{12} [den Messias]{13,14} [gefunden]{12}» ([das]{15} [heisst]{16} [übersetzt]{17}: [Christus]{18}).",
 "JHN.1.42": "[Er führte]{1} [ihn]{2} [zu]{3} [Jesus]{4,5}. [Jesus]{8,9} [blickte]{6} [ihn]{7} [an]{6} und [sagte]{10}: «[Du]{11} [bist]{12} [Simon]{13}, [der Sohn]{14,15} [des Johannes]{16}; [du]{17} [wirst]{18} [Kephas]{19} [heissen]{18}» ([das]{20} [wird übersetzt]{21}: [Petrus]{22}).",
 "JHN.1.43": "[Am folgenden Tag]{1,2} [wollte er]{3} [nach]{5} [Galiläa]{6,7} [aufbrechen]{4}. Und{8} [er findet]{9} [Philippus]{10}, und{11} [Jesus]{14,15} [sagt]{12} [zu ihm]{13}: «[Folge]{16} [mir]{17}!»",
 "JHN.1.44": "[Philippus]{3,4} [aber]{2} [war]{1} [aus]{5} [Betsaida]{6}, [aus]{7} [der]{8} [Stadt]{9} [des Andreas]{10} und{11} [des Petrus]{12}.",
 "JHN.1.45": "[Philippus]{2} [findet]{1} [Natanaël]{3,4} und{5} [sagt]{6} [zu ihm]{7}: «[Von dem]{8} [Mose]{10} [im]{11,12} [Gesetz]{13} [geschrieben hat]{9} und{14} [die Propheten]{15,16}, [den haben wir gefunden]{17}: [Jesus]{18}, [den Sohn]{19} [Josefs]{20,21}, [den]{22} [aus]{23} [Nazaret]{24}.»",
 "JHN.1.46": "Und{1} [Natanaël]{4} [sagte]{2} [zu ihm]{3}: «[Kann]{7} [aus]{5} [Nazaret]{6} [etwas]{8} [Gutes]{9} [kommen]{10}?» [Philippus]{13,14} [sagt]{11} [zu ihm]{12}: «[Komm]{15} und{16} [sieh]{17}!»",
 "JHN.1.47": "[Jesus]{2,3} [sah]{1} [Natanaël]{4,5} [zu]{7} [sich]{8} [kommen]{6} und{9} [sagt]{10} [über]{11} [ihn]{12}: «[Siehe]{13}, [wahrhaftig]{14} [ein Israelit]{15}, [in]{16} [dem]{17} [keine]{19} [Falschheit]{18} [ist]{20}!»",
 "JHN.1.48": "[Natanaël]{3} [sagt]{1} [zu ihm]{2}: «[Woher]{4} [kennst du]{6} [mich]{5}?» [Jesus]{8} [antwortete]{7} und{9} [sagte]{10} [zu ihm]{11}: «[Bevor]{12,13} [Philippus]{15} [dich]{14} [rief]{16}, [als du]{17} [unter]{18} [dem]{19} [Feigenbaum]{20} [warst]{17}, [habe ich]{21} [dich]{22} [gesehen]{21}.»",
 "JHN.1.49": "[Natanaël]{3} [antwortete]{1} [ihm]{2}: «[Rabbi]{4}, [du]{5} [bist]{6} [der Sohn]{7,8} [Gottes]{9,10}, [du]{11} [bist]{13} der [König]{12} [Israels]{14,15}!»",
 "JHN.1.50": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihm]{5}: «[Weil]{6} [ich]{7} [dir]{8} [gesagt habe]{7}, [dass]{9} [ich]{10} [dich]{11} [unter]{12} [dem]{13} [Feigenbaum]{14} [gesehen habe]{10}, [glaubst du]{15}? [Grösseres]{16} [als dies]{17} [wirst du sehen]{18}.»",
 "JHN.1.51": "Und{1} [er sagt]{2} [zu ihm]{3}: «[Amen]{4}, [amen]{5}, [ich sage]{6} [euch]{7}: [Ihr werdet]{8} [den Himmel]{9,10} [geöffnet]{11} [sehen]{8} und{12} [die Engel]{13,14} [Gottes]{15,16} [hinaufsteigen]{17} und{18} [herabsteigen]{19} [auf]{20} [den Menschensohn]{21-24}.»",
 # ------------------------------------------------------------ Kapitel 2
 "JHN.2.1": "Und{1} [am]{2} [dritten]{4,5} [Tag]{3} [fand]{7} [eine Hochzeit]{6} [statt]{7} [in]{8} [Kana]{9} [in Galiläa]{10,11}, und{12} [die Mutter]{14,15} [Jesu]{16,17} [war]{13} [dort]{18}.",
 "JHN.2.2": "[Auch]{3} [Jesus]{4,5} und{6} [seine]{9} [Jünger]{7,8} [waren]{1} [zur]{10,11} [Hochzeit]{12} [eingeladen]{1}. ~2(δέ «aber» verbindet nur locker mit dem Vorigen; nicht eigens wiedergegeben)",
 "JHN.2.3": "Und{1} [als]{2} [der Wein]{3} [ausging]{2}, [sagt]{4} [die Mutter]{5,6} [Jesu]{7,8} [zu]{9} [ihm]{10}: «[Sie haben]{13} [keinen]{12} [Wein]{11} mehr.»",
 "JHN.2.4": "Und{1} [Jesus]{4,5} [sagt]{2} [zu ihr]{3}: «[Was]{6} [habe ich]{7} [mit]{8} [dir]{9} [zu tun]{6}, [Frau]{10}? [Meine]{15} [Stunde]{13,14} [ist]{12} [noch nicht]{11} [gekommen]{12}.»",
 "JHN.2.5": "[Seine]{4} [Mutter]{2,3} [sagt]{1} [zu den]{5} [Dienern]{6}: «[Was]{7,8} [er]{10} [euch]{11} [auch]{9} [sagt]{10}, [das tut]{12}!»",
 "JHN.2.6": "[Es standen]{1,12} [aber]{2} [dort]{3} [sechs]{6} [steinerne]{4} [Wasserkrüge]{5} [für]{7} [die]{8} [Reinigung]{9} [der Juden]{10,11}; [sie fassten]{13} [je]{14} [zwei]{16} [oder]{17} [drei]{18} [Metreten]{15}.",
 "JHN.2.7": "[Jesus]{3,4} [sagt]{1} [zu ihnen]{2}: «[Füllt]{5} [die Krüge]{6,7} [mit Wasser]{8}!» Und{9} [sie füllten]{10} [sie]{11} [bis]{12} [oben]{13}.",
 "JHN.2.8": "Und{1} [er sagt]{2} [zu ihnen]{3}: «[Schöpft]{4} [jetzt]{5} und{6} [bringt]{7} es [dem Speisemeister]{8,9}!» [Sie]{10} [aber]{11} [brachten]{12} es.",
 "JHN.2.9": "[Als]{1} [aber]{2} [der Speisemeister]{4,5} [das Wasser]{6,7} [kostete]{3}, das [zu Wein]{8} [geworden war]{9} – und{10} [er wusste]{12} [nicht]{11}, [woher]{13} [er stammte]{14}, [die Diener]{15,17} [aber]{16} [wussten es]{18}, [die]{19} [das Wasser]{21,22} [geschöpft hatten]{20} –, [ruft]{23} [der Speisemeister]{26,27} [den Bräutigam]{24,25}",
 "JHN.2.10": "und{1} [sagt]{2} [zu ihm]{3}: «[Jeder]{4} [Mensch]{5} [setzt]{10} [zuerst]{6} [den guten]{7,8} [Wein]{9} [vor]{10}, und{11} [wenn]{12} [sie betrunken sind]{13}, [den geringeren]{14,15}; [du]{16} [hast]{17} [den guten]{18,19} [Wein]{20} [bis]{21} [jetzt]{22} [aufbewahrt]{17}.»",
 "JHN.2.11": "[Diesen]{1} [Anfang]{3} [der Zeichen]{4,5} [machte]{2} [Jesus]{6,7} [in]{8} [Kana]{9} [in Galiläa]{10,11} und{12} [offenbarte]{13} [seine]{16} [Herrlichkeit]{14,15}, und{17} [seine]{23} [Jünger]{21,22} [glaubten]{18} [an]{19} [ihn]{20}.",
 "JHN.2.12": "[Danach]{1,2} [ging]{3} [er]{6} [mit]{7} [seiner]{10} [Mutter]{8,9}, [den Brüdern]{12,13} und{14} [seinen]{17} [Jüngern]{15,16} [nach]{4} [Kafarnaum]{5} [hinab]{3}, und{18} [sie blieben]{20} [dort]{19} [nicht]{21} [viele]{22} [Tage]{23}. ~11(καί «und» zwischen den Aufgezählten; durch das Komma wiedergegeben)",
 "JHN.2.13": "Und{1} [das Passa]{4,5} [der Juden]{6,7} [war]{3} [nahe]{2}, und{8} [Jesus]{12,13} [zog]{9} [nach]{10} [Jerusalem]{11} [hinauf]{9}.",
 "JHN.2.14": "Und{1} [er fand]{2} [im]{3,4} [Tempel]{5} [die]{6} [Verkäufer]{7} [von Rindern]{8} und{9} [Schafen]{10} und{11} [Tauben]{12} und{13} [die]{14} [Geldwechsler]{15}, [die dort sassen]{16}.",
 "JHN.2.15": "Und{1} [er machte]{2} [eine Geissel]{3} [aus]{4} [Stricken]{5} und [trieb]{7} [alle]{6} [aus]{8} [dem]{9} [Tempel]{10} [hinaus]{7}, [sowohl]{12} [die]{11} [Schafe]{13} [als auch]{14} [die]{15} [Rinder]{16}; und{17} [den Geldwechslern]{18,19} [schüttete er]{20} [die Münzen]{21,22} [aus]{20} und{23} [stiess]{26} [die Tische]{24,25} [um]{26},",
 "JHN.2.16": "und{1} [zu denen, die]{2} [Tauben]{3,4} [verkauften]{5}, [sagte er]{6}: «[Schafft]{7} [das]{8} [von hier]{9} [weg]{7}! [Macht]{11} [das Haus]{12,13} [meines]{16} [Vaters]{14,15} [nicht]{10} [zu einem Haus]{17} [des Handels]{18}!»",
 "JHN.2.17": "[Seine]{4} [Jünger]{2,3} [erinnerten sich]{1}, [dass]{5} [geschrieben]{6} [steht]{7}: «[Der Eifer]{8,9} [um]{10} [dein]{12} [Haus]{11} [wird]{13} [mich]{14} [verzehren]{13}.»",
 "JHN.2.18": "[Da]{2} [antworteten]{1} [die Juden]{3,4} und{5} [sagten]{6} [zu ihm]{7}: «[Was für ein]{8} [Zeichen]{9} [zeigst du]{10} [uns]{11}, [dass]{12} [du]{14} [das]{13} [tust]{14}?»",
 "JHN.2.19": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihnen]{5}: «[Reisst]{6} [diesen]{9} [Tempel]{7,8} [nieder]{6}, und{10} [in]{11} [drei]{12} [Tagen]{13} [werde ich]{14} [ihn]{15} [aufrichten]{14}.»",
 "JHN.2.20": "[Da]{2} [sagten]{1} [die Juden]{3,4}: «[Sechsundvierzig]{5-7} [Jahre]{8} [ist]{9} [an diesem]{10,12} [Tempel]{11} [gebaut worden]{9}, und{13} [du]{14} [wirst]{18} [ihn]{19} [in]{15} [drei]{16} [Tagen]{17} [aufrichten]{18}?»",
 "JHN.2.21": "[Er]{1} [aber]{2} [sprach]{3} [vom]{4,5} [Tempel]{6} [seines]{9} [Leibes]{7,8}.",
 "JHN.2.22": "[Als]{1} [er]{3} [nun]{2} [von]{4} [den Toten]{5} [auferweckt worden war]{3}, [erinnerten sich]{6} [seine]{9} [Jünger]{7,8}, [dass]{10} [er]{12} [das]{11} [gesagt hatte]{12}, und{13} [sie glaubten]{14} [der Schrift]{15,16} und{17} [dem Wort]{18,19}, [das]{20} [Jesus]{22,23} [gesagt hatte]{21}.",
 "JHN.2.23": "[Als]{1} [er]{3} [aber]{2} [am]{7,8} [Passa]{9}, [beim]{10,11} [Fest]{12}, [in]{4,5} [Jerusalem]{6} [war]{3}, [glaubten]{14} [viele]{13} [an]{15} [seinen]{18} [Namen]{16,17}, [da sie]{19} [seine]{20} [Zeichen]{21,22} [sahen]{19}, [die]{23} [er tat]{24}.",
 "JHN.2.24": "[Jesus]{3} [selbst]{1} [aber]{2} [vertraute]{5} [sich]{6} [ihnen]{7} [nicht]{4} [an]{5}, [weil]{8,9} [er]{10} [alle]{12} [kannte]{11}",
 "JHN.2.25": "und{1} [weil]{2} [er]{5} [nicht]{3} [nötig]{4} [hatte]{5}, [dass]{6} [jemand]{7} [über]{9} [den Menschen]{10,11} [Zeugnis ablegte]{8}; [er selbst]{12} [erkannte]{14} [nämlich]{13}, [was]{15} [im]{17,18} [Menschen]{19} [war]{16}.",
 # ------------------------------------------------------------ Kapitel 3
 "JHN.3.1": "[Es war]{1} [aber]{2} [ein Mensch]{3} [unter]{4} [den Pharisäern]{5,6}, [sein]{9} [Name]{8} war [Nikodemus]{7}, [ein Oberster]{10} [der Juden]{11,12}.",
 "JHN.3.2": "[Dieser]{1} [kam]{2} [bei Nacht]{5} [zu]{3} [ihm]{4} und{6} [sagte]{7} [zu ihm]{8}: «[Rabbi]{9}, [wir wissen]{10}, [dass]{11} [du]{14} [als Lehrer]{15} [von]{12} [Gott]{13} [gekommen bist]{14}; [denn]{17} [niemand]{16} [kann]{18} [diese]{19,20} [Zeichen]{21} [tun]{22}, [die]{23} [du]{24} [tust]{25}, [wenn]{26} [Gott]{29,30} [nicht]{27} [mit]{31} [ihm]{32} [ist]{28}.»",
 "JHN.3.3": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihm]{5}: «[Amen]{6}, [amen]{7}, [ich sage]{8} [dir]{9}: [Wenn]{10} [jemand]{12} [nicht]{11} [von oben]{14} [geboren wird]{13}, [kann er]{16} [das Reich]{18,19} [Gottes]{20,21} [nicht]{15} [sehen]{17}.»",
 "JHN.3.4": "[Nikodemus]{4,5} [sagt]{1} [zu]{2} [ihm]{3}: «[Wie]{6} [kann]{7} [ein Mensch]{8} [geboren werden]{9}, [wenn er]{11} [alt]{10} [ist]{11}? [Kann er]{13} [etwa]{12} [ein zweites Mal]{20} [in]{14} [den]{15} [Leib]{16} [seiner]{19} [Mutter]{17,18} [hineingehen]{21} und{22} [geboren werden]{23}?»",
 "JHN.3.5": "[Jesus]{2} [antwortete]{1}: «[Amen]{3}, [amen]{4}, [ich sage]{5} [dir]{6}: [Wenn]{7} [jemand]{9} [nicht]{8} [aus]{11} [Wasser]{12} und{13} [Geist]{14} [geboren wird]{10}, [kann er]{16} [nicht]{15} [in]{18} [das Reich]{19,20} [Gottes]{21,22} [hineinkommen]{17}.",
 "JHN.3.6": "[Was]{1} [aus]{3} [dem Fleisch]{4,5} [geboren ist]{2}, [ist]{7} [Fleisch]{6}, und{8} [was]{9} [aus]{11} [dem Geist]{12,13} [geboren ist]{10}, [ist]{15} [Geist]{14}.",
 "JHN.3.7": "[Wundere dich]{2} [nicht]{1}, [dass]{3} [ich]{4} [dir]{5} [gesagt habe]{4}: ‹[Ihr]{7} [müsst]{6} [von oben]{9} [geboren werden]{8}.›",
 "JHN.3.8": "[Der Wind]{1,2} [weht]{5}, [wo]{3} [er will]{4}, und{6} [du hörst]{10} [sein]{9} [Rauschen]{7,8}, [aber]{11} [du weisst]{13} [nicht]{12}, [woher]{14} [er kommt]{15} und{16} [wohin]{17} [er geht]{18}. [So]{19} [ist es]{20} [mit jedem]{21}, [der]{22} [aus]{24} [dem Geist]{25,26} [geboren ist]{23}.»",
 "JHN.3.9": "[Nikodemus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihm]{5}: «[Wie]{6} [kann]{7} [das]{8} [geschehen]{9}?»",
 "JHN.3.10": "[Jesus]{2} [antwortete]{1} und{3} [sagte]{4} [zu ihm]{5}: «[Du]{6} [bist]{7} [der Lehrer]{8,9} [Israels]{10,11} und{12} [verstehst]{15} [das]{13} [nicht]{14}?",
 "JHN.3.11": "[Amen]{1}, [amen]{2}, [ich sage]{3} [dir]{4}: [Was]{6} [wir wissen]{7}, [davon reden wir]{8}, und{9} [was]{10} [wir gesehen haben]{11}, [das bezeugen wir]{12}; und{13} [unser]{16} [Zeugnis]{14,15} [nehmt ihr]{18} [nicht]{17} [an]{18}. ~5(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "JHN.3.12": "[Wenn]{1} [ich]{4} [euch]{5} [Irdisches]{2,3} [gesagt habe]{4} und{6} [ihr]{8} [nicht]{7} [glaubt]{8}, [wie]{9} [werdet ihr glauben]{15}, [wenn]{10} [ich]{11} [euch]{12} [Himmlisches]{13,14} [sage]{11}?",
 "JHN.3.13": "Und{1} [niemand]{2} [ist]{3} [in]{4} [den Himmel]{5,6} [hinaufgestiegen]{3} [ausser]{7,8} [dem]{9}, [der]{9} [aus]{10} [dem Himmel]{11,12} [herabgestiegen ist]{13}, [dem Menschensohn]{14-17}.",
 "JHN.3.14": "Und{1} [wie]{2} [Mose]{3} [die Schlange]{5,6} [in]{7} [der Wüste]{8,9} [erhöht hat]{4}, [so]{10} [muss]{12} [der Menschensohn]{13-16} [erhöht werden]{11},",
 "JHN.3.15": "[damit]{1} [jeder]{2}, [der]{3} [glaubt]{4}, [in]{5} [ihm]{6} [ewiges]{9} [Leben]{8} [hat]{7}.",
 "JHN.3.16": "[Denn]{2} [so]{1} [hat]{3} [Gott]{4,5} [die Welt]{6,7} [geliebt]{3}, [dass]{8} [er]{13} [den einzigen]{11,12} [Sohn]{9,10} [gab]{13}, [damit]{14} [jeder]{15}, [der]{16} [an]{18} [ihn]{19} [glaubt]{17}, [nicht]{20} [verloren geht]{21}, [sondern]{22} [ewiges]{25} [Leben]{24} [hat]{23}.",
 "JHN.3.17": "[Denn]{2} [Gott]{4,5} [hat]{3} [den Sohn]{6,7} [nicht]{1} [in]{8} [die Welt]{9,10} [gesandt]{3}, [damit]{11} [er]{12} [die Welt]{13,14} [richtet]{12}, [sondern]{15} [damit]{16} [die Welt]{18,19} [durch]{20} [ihn]{21} [gerettet wird]{17}.",
 "JHN.3.18": "[Wer]{1} [an]{3} [ihn]{4} [glaubt]{2}, [wird]{6} [nicht]{5} [gerichtet]{6}; [wer]{7} [aber]{8} [nicht]{9} [glaubt]{10}, [ist]{12} [schon]{11} [gerichtet]{12}, [weil]{13} [er]{15} [nicht]{14} [an]{16} [den Namen]{17,18} [des einzigen]{19,20} [Sohnes]{21} [Gottes]{22,23} [geglaubt hat]{15}.",
 "JHN.3.19": "[Das]{1} [aber]{2} [ist]{3} [das Gericht]{4,5}: [Das Licht]{7,8} [ist]{9} [in]{10} [die Welt]{11,12} [gekommen]{9}, und{13} [die Menschen]{15,16} [liebten]{14} [die Finsternis]{18,19} [mehr]{17} [als]{20} [das Licht]{21,22}; [denn]{24} [ihre]{25} [Werke]{27,28} [waren]{23} [böse]{26}. ~6(ὅτι leitet den Inhalt ein; durch den Doppelpunkt wiedergegeben)",
 "JHN.3.20": "[Denn]{2} [jeder]{1}, [der]{3} [Schlechtes]{4} [tut]{5}, [hasst]{6} [das Licht]{7,8} und{9} [kommt]{11} [nicht]{10} [zum]{12,13} [Licht]{14}, [damit]{15} [seine]{20} [Werke]{18,19} [nicht]{16} [aufgedeckt werden]{17}.",
 "JHN.3.21": "[Wer]{1} [aber]{2} [die Wahrheit]{4,5} [tut]{3}, [kommt]{6} [zum]{7,8} [Licht]{9}, [damit]{10} [offenbar wird]{11}, [dass]{15} [seine]{12} [Werke]{13,14} [in]{16} [Gott]{17} [getan]{19} [sind]{18}.»",
 "JHN.3.22": "[Danach]{1,2} [kamen]{3} [Jesus]{4,5} und{6} [seine]{9} [Jünger]{7,8} [in]{10} [das]{11} [judäische]{12} [Land]{13}, und{14} [er hielt sich]{16} [dort]{15} [mit]{17} [ihnen]{18} [auf]{16} und{19} [taufte]{20}.",
 "JHN.3.23": "[Aber]{2} [auch]{3} [Johannes]{4,5} [taufte]{1,6} [in]{7} [Änon]{8} [nahe]{9} [bei Salim]{10,11}, [weil]{12} [dort]{16} [viel]{14} [Wasser]{13} [war]{15}; und{17} [die Leute kamen]{18} und{19} [liessen sich taufen]{20}.",
 "JHN.3.24": "[Johannes]{8,9} [war]{3} [nämlich]{2} [noch nicht]{1} [ins]{5,6} [Gefängnis]{7} [geworfen worden]{4}.",
 "JHN.3.25": "[Da]{2} [kam es]{1} [zu einem Streit]{3} [zwischen]{4} [den Jüngern]{5,6} [des Johannes]{7} [und]{8} [einem Juden]{9} [über]{10} [die Reinigung]{11}.",
 "JHN.3.26": "Und{1} [sie kamen]{2} [zu]{3} [Johannes]{4,5} und{6} [sagten]{7} [zu ihm]{8}: «[Rabbi]{9}, [der]{10} [bei]{12} [dir]{13} [war]{11} [jenseits]{14} [des Jordan]{15,16}, [für den]{17} [du]{18} [Zeugnis abgelegt hast]{19} – [siehe]{20}, [der]{21} [tauft]{22}, und{23} [alle]{24} [kommen]{25} [zu]{26} [ihm]{27}!»",
 "JHN.3.27": "[Johannes]{2} [antwortete]{1} und{3} [sagte]{4}: «[Ein Mensch]{7} [kann]{6} [nichts]{5,9,10} [empfangen]{8}, [wenn]{11} es [ihm]{15} [nicht]{12} [vom]{16,17} [Himmel]{18} [gegeben]{14} [ist]{13}.",
 "JHN.3.28": "[Ihr]{2} [selbst]{1} [bezeugt]{4} [mir]{3}, [dass]{5} [ich gesagt habe]{6}: ‹[Ich]{9} [bin]{8} [nicht]{7} [der Christus]{10,11}›, [sondern]{12}: ‹[Ich bin]{15} [vor]{16} [ihm]{17} [her]{16} [gesandt]{14}.› ~13(ὅτι leitet die direkte Rede ein)",
 "JHN.3.29": "[Wer]{1} [die Braut]{3,4} [hat]{2}, [ist]{6} [der Bräutigam]{5}; [der Freund]{7,9} [des Bräutigams]{10,11} [aber]{8}, [der]{12} [dabeisteht]{13} und{14} [ihn]{16} [hört]{15}, [freut sich]{18} [von Herzen]{17} [über]{19} [die]{20} [Stimme]{21} [des Bräutigams]{22,23}. [Diese]{24} [meine]{28,29} [Freude]{26,27} [ist]{30} [nun]{25} [erfüllt]{30}.",
 "JHN.3.30": "[Er]{1} [muss]{2} [wachsen]{3}, [ich]{4} [aber]{5} [kleiner werden]{6}.",
 "JHN.3.31": "[Der]{1} [von oben]{2} [kommt]{3}, [ist]{6} [über]{4} [allen]{5}. [Wer]{7} [von]{9} [der Erde]{10,11} [ist]{8}, [ist]{15} [von]{12} [der Erde]{13,14} und{16} [redet]{20} [von]{17} [der Erde]{18,19} [her]{17}. [Der]{21} [vom]{22,23} [Himmel]{24} [kommt]{25}, [ist]{28} [über]{26} [allen]{27}.",
 "JHN.3.32": "[Was]{1} [er gesehen]{2} und{3} [gehört hat]{4}, [das]{5} [bezeugt er]{6}, und{7} [sein]{10} [Zeugnis]{8,9} [nimmt]{12} [niemand]{11} [an]{12}.",
 "JHN.3.33": "[Wer]{1} [sein]{3} [Zeugnis]{4,5} [angenommen hat]{2}, [hat besiegelt]{6}, [dass]{7} [Gott]{8,9} [wahrhaftig]{10} [ist]{11}.",
 "JHN.3.34": "[Denn]{2} [der]{1}, [den]{1} [Gott]{4,5} [gesandt hat]{3}, [redet]{10} [die Worte]{6,7} [Gottes]{8,9}; [denn]{12} [er gibt]{15} [den Geist]{16,17} [nicht]{11} [nach]{13} [Mass]{14}.",
 "JHN.3.35": "[Der Vater]{1,2} [liebt]{3} [den Sohn]{4,5} und{6} [hat]{8} [alles]{7} [in]{9} [seine]{12} [Hand]{10,11} [gegeben]{8}.",
 "JHN.3.36": "[Wer]{1} [an]{3} [den Sohn]{4,5} [glaubt]{2}, [hat]{6} [ewiges]{8} [Leben]{7}; [wer]{9} [aber]{10} [dem Sohn]{12,13} [nicht gehorcht]{11}, [wird]{15} [das Leben]{16} [nicht]{14} [sehen]{15}, [sondern]{17} [der Zorn]{18,19} [Gottes]{20,21} [bleibt]{22} [auf]{23} [ihm]{24}.»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 1
 "JHN.1.1": "[Im]{1} [Aafang]{2} [isch]{3} [s Wort]{4,5} [gsii]{3}, und{6} [s Wort]{7,8} [isch]{9} [bi]{10} [Gott]{11,12} [gsii]{9}, und{13} [s Wort]{16,17} [isch]{15} [Gott]{14} [gsii]{15}.",
 "JHN.1.2": "[Das]{1} [isch]{2} [im]{3} [Aafang]{4} [bi]{5} [Gott]{6,7} [gsii]{2}.",
 "JHN.1.3": "[Alles]{1} [isch]{4} [dur]{2} [es]{3} [worde]{4}, und{5} [ohni]{6} [es]{7} [isch]{8} [nöd emal]{9} [eis]{10} [worde]{8}. [Was]{11} [worde isch]{12} –",
 "JHN.1.4": "[in]{1} [ihm]{2} [isch]{4} [Läbe]{3} [gsii]{4}, und{5} [s Läbe]{6,7} [isch]{8} [s Liecht]{9,10} [vo de Mänsche]{11,12} [gsii]{8}.",
 "JHN.1.5": "Und{1} [s Liecht]{2,3} [schiint]{7} [i]{4} [de Fiischteri]{5,6}, und{8} [d Fiischteri]{9,10} [hät]{13} [es]{11} [nöd]{12} [packt]{13}.",
 "JHN.1.6": "[Es isch]{1} [en Mänsch]{2} [uftrete]{1}, [gschickt]{3} [vo]{4} [Gott]{5}; [sin]{7} [Name]{6} isch [Johannes]{8} gsii.",
 "JHN.1.7": "[Dä]{1} [isch]{2} [zum]{3} [Zügnis]{4} [choo]{2}, [demit]{5} [er]{6} [vom]{7,8} [Liecht]{9} [Zügnis gäb]{6}, [demit]{10} [alli]{11} [dur]{13} [ihn]{14} [zum Glaube chömed]{12}.",
 "JHN.1.8": "[Er]{3} [isch]{2} [nöd]{1} [s Liecht]{4,5} [gsii]{2}, [sondern]{6} [er hät söle]{7} [vom]{9,10} [Liecht]{11} [Zügnis gää]{8}.",
 "JHN.1.9": "[S]{2,4} [wahr]{5} [Liecht]{3}, [wo]{6} [jede]{8} [Mänsch]{9} [erlüüchtet]{7}, [isch]{1} [i]{11} [d Wält]{12,13} [choo]{10}.",
 "JHN.1.10": "[Er isch]{4} [i]{1} [de Wält]{2,3} [gsii]{4}, und{5} [d Wält]{6,7} [isch]{10} [dur]{8} [ihn]{9} [worde]{10}, und{11} [d Wält]{12,13} [hät]{16} [ihn]{14} [nöd]{15} [erchännt]{16}.",
 "JHN.1.11": "[Er isch]{4} [zu]{1} [sim Eigete]{2,3} [choo]{4}, und{5} [di Sine]{6,7} [händ]{10} [ihn]{8} [nöd]{9} [ufgnoo]{10}.",
 "JHN.1.12": "[Allne]{1} [aber]{2}, [wo]{1} [ihn]{4} [ufgnoo händ]{3}, [hät er]{5} [ine]{6} [d Vollmacht]{7} [gää]{5}, [Chind]{8} [vo Gott]{9} [z wärde]{10}, [dene, wo]{11} [a]{13} [sin]{16} [Name]{14,15} [glaubed]{12},",
 "JHN.1.13": "[wo]{1} [nöd]{2} [us]{3} [Bluet]{4} [und nöd]{5} [us]{6} [em Wille]{7} [vom Fleisch]{8} [und nöd]{9} [us]{10} [em Wille]{11} [vo me Maa]{12}, [sondern]{13} [us]{14} [Gott]{15} [gebore sind]{16}.",
 "JHN.1.14": "Und{1} [s Wort]{2,3} [isch]{5} [Fleisch]{4} [worde]{5} und{6} [hät]{7} [under]{8} [üs]{9} [gwohnt]{7}, und{10} [mir händ]{11} [sini]{14} [Herrlichkeit]{12,13} [aagluegt]{11}, [e Herrlichkeit]{15} [wie]{16} [die vom Einzige]{17} [vom]{18} [Vatter]{19}, [voll]{20} [Gnad]{21} und{22} [Wahrheit]{23}.",
 "JHN.1.15": "([De Johannes]{1} [git]{2} [über]{3} [ihn]{4} [Zügnis]{2} und{5} [rüeft]{6}: «[Dä]{8} [isch es]{9} [gsii]{9}, [vo däm]{10} [ich gseit han]{11}: ‹[Dä, wo]{12} [nach]{13} [mir]{14} [chunnt]{15}, [isch]{18} [mir]{17} [voraus]{16}, [dänn]{19} [er isch]{22} [vor]{20} [mir]{21} [gsii]{22}.›») ~7(λέγων «sägend» leitet di diräkt Red ii)",
 "JHN.1.16": "[Dänn]{1} [us]{2} [sinere]{5} [Füli]{3,4} [händ]{8} [mir]{6} [alli]{7} [übercho]{8}, und{9} [Gnad]{10} [um]{11} [Gnad]{12}.",
 "JHN.1.17": "[Dänn]{1} [s Gsetz]{2,3} [isch]{6} [dur]{4} [de Mose]{5} [gää worde]{6}, [d Gnad]{7,8} und{9} [d Wahrheit]{10,11} [sind]{15} [dur]{12} Jesus{13} Christus{14} [choo]{15}.",
 "JHN.1.18": "[Gott]{1} [hät]{3} [nie]{4} [öpper]{2} [gseh]{3}; [de Einzig]{5}, [Gott]{6}, [wo]{7} [a]{9} [de Bruscht]{10,11} [vom Vatter]{12,13} [isch]{8}, [dä]{14} [hät Bricht gää]{15}.",
 "JHN.1.19": "Und{1} [das]{2} [isch]{3} [s Zügnis]{4,5} [vom Johannes]{6,7}, [wo]{8} [d Jude]{10,11} [vo]{12} [Jerusalem]{13} [Prieschter]{14} und{15} [Levite]{16} [gschickt händ]{9}, [zum]{17} [en]{19} [fröge]{18}: «[Wer]{21} [bisch]{22} [du]{20}?»",
 "JHN.1.20": "Und{1} [er hät bekännt]{2} und{3} [hät]{5} [nöd]{4} [abgstritte]{5}, und{6} [er hät bekännt]{7}: «[Ich]{9} [bi]{11} [nöd]{10} [de Christus]{12,13}.» ~8(ὅτι leitet di diräkt Red ii)",
 "JHN.1.21": "Und{1} [si händ]{2} [en]{3} [gfröget]{2}: «[Was]{4} [dänn]{5}? [Bisch]{8} [du]{6} [de Elija]{7}?» Und{9} [er seit]{10}: «[Ich bi s]{12} [nöd]{11}.» «[Bisch]{15} [du]{16} [de Prophet]{13,14}?» Und{17} [er hät gantwortet]{18}: «[Nei]{19}.»",
 "JHN.1.22": "[Da]{2} [händ si]{1} [zu ihm]{3} [gseit]{1}: «[Wer]{4} [bisch]{5}? [Demit]{6} [mir]{8} [dene, wo]{9} [üs]{11} [gschickt händ]{10}, [e Antwort]{7} [chönd gää]{8}: [Was]{12} [seisch]{13} [über]{14} [dich sälber]{15}?»",
 "JHN.1.23": "[Er hät gseit]{1}: «[Ich]{2} bi [d Stimm]{3} [vo eim, wo rüeft]{4} [i]{5} [de Wüeschti]{6,7}: ‹[Mached]{8} [de Wäg]{9,10} [vom Herr]{11} [grad]{8}!›, [wie]{12} [de Jesaja]{14}, [de Prophet]{15,16}, [gseit hät]{13}.»",
 "JHN.1.24": "Und{1} [si sind]{3} [vo]{4} [de Pharisäer]{5,6} [gschickt worde]{2}.",
 "JHN.1.25": "Und{1} [si händ]{2} [en]{3} [gfröget]{2} und{4} [zu ihm]{6} [gseit]{5}: «[Werum]{7} [tauftsch]{9} [dänn]{8}, [wänn]{10} [du]{11} [nöd]{12} [de Christus]{14,15} [bisch]{13}, [nöd]{16} [de Elija]{17} [und nöd]{18} [de Prophet]{19,20}?»",
 "JHN.1.26": "[De Johannes]{3,4} [hät]{1} [ine]{2} [gantwortet]{1}: «[Ich]{6} [taufe]{7} [mit]{8} [Wasser]{9}; [mitte]{10} [under eu]{11} [staat]{12} eine, [wo]{13} [ir]{14} [nöd]{15} [känned]{16}, ~5(λέγων «sägend» leitet di diräkt Red ii)",
 "JHN.1.27": "[dä, wo]{1} [nach]{2} [mir]{3} [chunnt]{4}; [ich bi]{7} [nöd]{6} [wärt]{8}, [dass]{9} [ich]{10} [ihm]{5,11} [de Rieme]{12,13} [vo de Sandale]{14,15} [ufmach]{10}.»",
 "JHN.1.28": "[Das]{1} [isch]{4} [z]{2} [Betanie]{3} [ännet]{5} [em Jordan]{6,7} [gscheh]{4}, [wo]{8} [de Johannes]{10,11} [tauft hät]{9,12}.",
 "JHN.1.29": "[Am nächschte Tag]{1,2} [gseht er]{3} [de Jesus]{4,5} [zu]{7} [sich]{8} [choo]{6} und{9} [seit]{10}: «[Lueg]{11}, [s Lamm]{12,13} [vo Gott]{14,15}, [wo]{16} [d Sünd]{18,19} [vo de Wält]{20,21} [wägnimmt]{17}!",
 "JHN.1.30": "[Dä]{1} [isch es]{2}, [vo]{3} [däm]{4} [ich]{5} [gseit han]{6}: ‹[Nach]{7} [mir]{8} [chunnt]{9} [en Maa]{10}, [wo]{11} [mir]{13} [voraus]{12} [isch]{14}, [dänn]{15} [er isch]{18} [vor]{16} [mir]{17} [gsii]{18}.›",
 "JHN.1.31": "[Und ich]{1} [han]{3} [en]{4} [nöd]{2} [kännt]{3}; [aber]{5} [demit]{6} [er]{7} [Israel]{8,9} [offebaret wird]{7}, [drum]{10,11} [bin]{12} [ich]{13} [choo]{12} [und taufe]{16} [mit]{14} [Wasser]{15}.»",
 "JHN.1.32": "Und{1} [de Johannes]{3} [hät bezüügt]{2}: «[Ich han]{6} [de Geischt]{7,8} [wie]{10} [e Tuube]{11} [vom]{12} [Himmel]{13} [abechoo]{9} [gseh]{6}, und{14} [er isch]{15} [uf]{16} [ihm]{17} [bliibe]{15}. ~4(λέγων «sägend» leitet di diräkt Red ii) ~5(ὅτι leitet di diräkt Red ii)",
 "JHN.1.33": "[Und ich]{1} [han]{3} [en]{4} [nöd]{2} [kännt]{3}; [aber]{5} [dä, wo]{6} [mich]{8} [gschickt hät]{7}, [mit]{10} [Wasser]{11} [z taufe]{9}, [dä]{12} [hät]{14} [mir]{13} [gseit]{14}: ‹[Uf wän]{15,16} [du]{18} [au]{17} [de Geischt]{19,20} [abechoo]{21} und{22} [uf]{24} [ihm]{25} [bliibe]{23} [gsehsch]{18}, [dä]{26} [isch es]{27}, [wo]{28} [mit]{30} [heilige]{32} [Geischt]{31} [tauft]{29}.›",
 "JHN.1.34": "[Und ich]{1} [han s gseh]{2} und{3} [han bezüügt]{4}: [Dä]{6} [isch]{7} [de Userwählt]{8,9} [vo Gott]{10,11}.» ~5(ὅτι leitet de Inhalt vom Zügnis ii; mit em Doppelpunkt widergää)",
 "JHN.1.35": "[Am nächschte Tag]{1,2} [isch]{4} [de Johannes]{5,6} [wider]{3} [daagstande]{4} und{7} [zwei]{12} [vo]{8} [sine]{9,11} [Jünger]{10},",
 "JHN.1.36": "und{1} [er hät]{2} [uf de Jesus]{3,4} [gluegt]{2}, [wo verbiigloffe isch]{5}, und [seit]{6}: «[Lueg]{7}, [s Lamm]{8,9} [vo Gott]{10,11}!»",
 "JHN.1.37": "Und{1} [di]{3} [zwei]{4} [Jünger]{5} [händ ghört]{2}, [was er gseit hät]{6,7}, und{8} [sind]{9} [em Jesus]{10,11} [nachegange]{9}.",
 "JHN.1.38": "[De Jesus]{3,4} [aber]{2} [hät sich umdräit]{1}, und{5} [wo er]{6} [gseh hät]{6}, [dass si]{7} [em nachegönd]{8}, [seit er]{9} [zu ine]{10}: «[Was]{11} [sueched ir]{12}?» [Si]{13} [aber]{14} [händ]{15} [zu ihm]{16} [gseit]{15}: «[Rabbi]{17} ([das]{18} [heisst]{19} [übersetzt]{20}: [Lehrer]{21}), [wo]{22} [isch dini Bliibi]{23}?»",
 "JHN.1.39": "[Er seit]{1} [zu ine]{2}: «[Chömed]{3}, und{4} [ir wärded s gseh]{5}!» [Da]{7} [sind si]{6} [choo]{6} und{8} [händ gseh]{9}, [wo]{10} [sini Bliibi isch]{11}, und{12} [si sind]{15} [dä]{16,18} [Tag]{17} [bi]{13} [ihm]{14} [bliibe]{15}; [es isch]{20} [öppe]{21} [di zäät]{22} [Stund]{19} [gsii]{20}.",
 "JHN.1.40": "[De Andreas]{2}, [de Brüeder]{3,4} [vom Simon]{5} [Petrus]{6}, [isch]{1} [eine]{7} [vo]{8} [dene]{9} [zwei]{10} [gsii]{1}, [wo]{11} s [vom]{13} [Johannes]{14} [ghört händ]{12} und{15} [ihm]{17} [nachegange sind]{16}.",
 "JHN.1.41": "[Dä]{2} [findt]{1} [zerscht]{3} [sin eigete]{6,7} [Brüeder]{4,5}, [de Simon]{8}, und{9} [seit]{10} [zu ihm]{11}: «[Mir händ]{12} [de Messias]{13,14} [gfunde]{12}» ([das]{15} [heisst]{16} [übersetzt]{17}: [Christus]{18}).",
 "JHN.1.42": "[Er hät]{1} [en]{2} [zum]{3,4} [Jesus]{5} [brocht]{1}. [De Jesus]{8,9} [hät]{6} [en]{7} [aagluegt]{6} und [gseit]{10}: «[Du]{11} [bisch]{12} [de Simon]{13}, [de Sohn]{14,15} [vom Johannes]{16}; [du]{17} [wirsch]{18} [Kephas]{19} [heisse]{18}» ([das]{20} [heisst übersetzt]{21}: [Petrus]{22}).",
 "JHN.1.43": "[Am nächschte Tag]{1,2} [hät er]{3} [uf]{5} [Galiläa]{6,7} [wele]{3} [ufbreche]{4}. Und{8} [er findt]{9} [de Philippus]{10}, und{11} [de Jesus]{14,15} [seit]{12} [zu ihm]{13}: «[Chumm]{16} [mir]{17} [nache]{16}!»",
 "JHN.1.44": "[De Philippus]{3,4} [aber]{2} [isch]{1} [vo]{5} [Betsaida]{6} [gsii]{1}, [us]{7} [de]{8} [Stadt]{9} [vom Andreas]{10} und{11} [vom Petrus]{12}.",
 "JHN.1.45": "[De Philippus]{2} [findt]{1} [de Natanaël]{3,4} und{5} [seit]{6} [zu ihm]{7}: «[Dä, wo]{8} [de Mose]{10} [im]{11,12} [Gsetz]{13} [devo gschribe hät]{9} und{14} [d Prophete]{15,16} au, [dä händ mir gfunde]{17}: [de Jesus]{18}, [de Sohn]{19} [vom Josef]{20,21}, [dä]{22} [vo]{23} [Nazaret]{24}.»",
 "JHN.1.46": "Und{1} [de Natanaël]{4} [hät]{2} [zu ihm]{3} [gseit]{2}: «[Cha]{7} [us]{5} [Nazaret]{6} [öppis]{8} [Guets]{9} [choo]{10}?» [De Philippus]{13,14} [seit]{11} [zu ihm]{12}: «[Chumm]{15} und{16} [lueg]{17}!»",
 "JHN.1.47": "[De Jesus]{2,3} [hät]{1} [de Natanaël]{4,5} [zu]{7} [sich]{8} [choo]{6} [gseh]{1} und{9} [seit]{10} [über]{11} [ihn]{12}: «[Lueg]{13}, [würkli]{14} [en Israelit]{15}, [a däm]{16,17} [nüüt]{19} [Falschs]{18} [isch]{20}!»",
 "JHN.1.48": "[De Natanaël]{3} [seit]{1} [zu ihm]{2}: «[Vo wo]{4} [kännsch]{6} [mich]{5}?» [De Jesus]{8} [hät gantwortet]{7} und{9} [zu ihm]{11} [gseit]{10}: «[Bevor]{12,13} [de Philippus]{15} [dich]{14} [grüeft hät]{16}, [wo du]{17} [under]{18} [em]{19} [Fiigebaum]{20} [gsii bisch]{17}, [han ich]{21} [dich]{22} [gseh]{21}.»",
 "JHN.1.49": "[De Natanaël]{3} [hät]{1} [ihm]{2} [gantwortet]{1}: «[Rabbi]{4}, [du]{5} [bisch]{6} [de Sohn]{7,8} [vo Gott]{9,10}, [du]{11} [bisch]{13} de [König]{12} [vo Israel]{14,15}!»",
 "JHN.1.50": "[De Jesus]{2} [hät gantwortet]{1} und{3} [zu ihm]{5} [gseit]{4}: «[Wil]{6} [ich]{7} [dir]{8} [gseit han]{7}, [dass]{9} [ich]{10} [dich]{11} [under]{12} [em]{13} [Fiigebaum]{14} [gseh han]{10}, [glaubsch]{15}? [Grössers]{16} [als das]{17} [wirsch gseh]{18}.»",
 "JHN.1.51": "Und{1} [er seit]{2} [zu ihm]{3}: «[Amen]{4}, [amen]{5}, [ich säge]{6} [eu]{7}: [Ir wärded]{8} [de Himmel]{9,10} [offe]{11} [gseh]{8} und{12} [d Ängel]{13,14} [vo Gott]{15,16} [ufestiige]{17} und{18} [abestiige]{19} [uf]{20} [de Mänschesohn]{21-24}.»",
 # ------------------------------------------------------------ Kapitel 2
 "JHN.2.1": "Und{1} [am]{2} [dritte]{4,5} [Tag]{3} [isch]{7} [z]{8} [Kana]{9} [in Galiläa]{10,11} [e Hochziit]{6} [gsii]{7}, und{12} [d Mueter]{14,15} [vom Jesus]{16,17} [isch]{13} [dört]{18} [gsii]{13}.",
 "JHN.2.2": "[Au]{3} [de Jesus]{4,5} und{6} [sini]{9} [Jünger]{7,8} [sind]{1} [a d]{10,11} [Hochziit]{12} [iiglade gsii]{1}. ~2(δέ «aber» verbindet nu locker mit em Vorige; nöd eigens widergää)",
 "JHN.2.3": "Und{1} [wo]{2} [de Wii]{3} [usgange isch]{2}, [seit]{4} [d Mueter]{5,6} [vom Jesus]{7,8} [zu]{9} [ihm]{10}: «[Si händ]{13} [kei]{12} [Wii]{11} meh.»",
 "JHN.2.4": "Und{1} [de Jesus]{4,5} [seit]{2} [zu ire]{3}: «[Was]{6} [han ich]{7} [mit]{8} [dir]{9} [z tue]{6}, [Frau]{10}? [Mini]{15} [Stund]{13,14} [isch]{12} [no nöd]{11} [choo]{12}.»",
 "JHN.2.5": "[Sini]{4} [Mueter]{2,3} [seit]{1} [zu de]{5} [Diener]{6}: «[Was]{7,8} [er]{10} [eu]{11} [au]{9} [seit]{10}, [das mached]{12}!»",
 "JHN.2.6": "[Es sind]{1} [aber]{2} [dört]{3} [sächs]{6} [steinigi]{4} [Wasserchrüeg]{5} [gstande]{12} [für]{7} [d]{8} [Reinigung]{9} [vo de Jude]{10,11}; [si händ]{13} [je]{14} [zwei]{16} [oder]{17} [drüü]{18} [Metrete]{15} [gfasst]{13}.",
 "JHN.2.7": "[De Jesus]{3,4} [seit]{1} [zu ine]{2}: «[Füllet]{5} [d Chrüeg]{6,7} [mit Wasser]{8}!» Und{9} [si händ]{10} [si]{11} [bis]{12} [obe]{13} [gfüllt]{10}.",
 "JHN.2.8": "Und{1} [er seit]{2} [zu ine]{3}: «[Schöpfed]{4} [jetzt]{5} und{6} [bringed]{7} s [em Spiismeischter]{8,9}!» [Si]{10} [aber]{11} [händ s]{12} [brocht]{12}.",
 "JHN.2.9": "[Wo]{1} [aber]{2} [de Spiismeischter]{4,5} [s Wasser]{6,7} [probiert hät]{3}, wo [zu Wii]{8} [worde isch]{9} – und{10} [er hät]{12} [nöd]{11} [gwüsst]{12}, [vo wo]{13} [er chunnt]{14}, [d Diener]{15,17} [aber]{16} [händ s gwüsst]{18}, [wo]{19} [s Wasser]{21,22} [gschöpft händ]{20} –, [rüeft]{23} [de Spiismeischter]{26,27} [de Brüütigam]{24,25}",
 "JHN.2.10": "und{1} [seit]{2} [zu ihm]{3}: «[Jede]{4} [Mänsch]{5} [stellt]{10} [zerscht]{6} [de guet]{7,8} [Wii]{9} [uf]{10}, und{11} [wänn]{12} [si betrunke sind]{13}, [de schlächter]{14,15}; [du]{16} [häsch]{17} [de guet]{18,19} [Wii]{20} [bis]{21} [jetzt]{22} [ufbhalte]{17}.»",
 "JHN.2.11": "[Das]{1} [hät]{2} [de Jesus]{6,7} [z]{8} [Kana]{9} [in Galiläa]{10,11} [als Aafang]{3} [vo de Zeiche]{4,5} [gmacht]{2} und{12} [hät]{13} [sini]{16} [Herrlichkeit]{14,15} [offebaret]{13}, und{17} [sini]{23} [Jünger]{21,22} [händ]{18} [a]{19} [ihn]{20} [glaubt]{18}.",
 "JHN.2.12": "[Dänn]{1,2} [isch]{3} [er]{6} [mit]{7} [sinere]{10} [Mueter]{8,9}, [de Brüedere]{12,13} und{14} [sine]{17} [Jünger]{15,16} [uf]{4} [Kafarnaum]{5} [abegange]{3}, und{18} [si sind]{20} [dört]{19} [nöd]{21} [vil]{22} [Täg]{23} [bliibe]{20}. ~11(καί «und» zwüsche de Ufzellte; mit em Komma widergää)",
 "JHN.2.13": "Und{1} [s Passa]{4,5} [vo de Jude]{6,7} [isch]{3} [nöch]{2} [gsii]{3}, und{8} [de Jesus]{12,13} [isch]{9} [uf]{10} [Jerusalem]{11} [ufegange]{9}.",
 "JHN.2.14": "Und{1} [er hät]{2} [im]{3,4} [Tämpel]{5} [d]{6} [Händler]{7} [mit Rinder]{8} und{9} [Schaf]{10} und{11} [Tuube]{12} [aatroffe]{2} und{13} [d]{14} [Gäldwächsler]{15}, [wo dört ghocket sind]{16}.",
 "JHN.2.15": "Und{1} [er hät]{2} [us]{4} [Strick]{5} [e Geissle]{3} [gmacht]{2} und [hät]{7} [alli]{6} [us]{8} [em]{9} [Tämpel]{10} [usetribe]{7}, [sowohl]{12} [d]{11} [Schaf]{13} [als au]{14} [d]{15} [Rinder]{16}; und{17} [de Gäldwächsler]{18,19} [hät er]{20} [s Münz]{21,22} [usgschüttet]{20} und{23} [d Tisch]{24,25} [umgheit]{26},",
 "JHN.2.16": "und{1} [zu dene, wo]{2} [Tuube]{3,4} [verchauft händ]{5}, [hät er gseit]{6}: «[Nämed]{7} [das]{8} [da]{9} [wäg]{7}! [Mached]{11} [s Huus]{12,13} [vo mim]{16} [Vatter]{14,15} [nöd]{10} [zu me Handelshuus]{17,18}!»",
 "JHN.2.17": "[Sini]{4} [Jünger]{2,3} [händ sich erinneret]{1}, [dass]{5} [gschribe]{6} [staat]{7}: «[De Iifer]{8,9} [für]{10} [dis]{12} [Huus]{11} [wird]{13} [mich]{14} [uffrässe]{13}.»",
 "JHN.2.18": "[Da]{2} [händ]{1} [d Jude]{3,4} [gantwortet]{1} und{5} [zu ihm]{7} [gseit]{6}: «[Was für es]{8} [Zeiche]{9} [zeigsch]{10} [üs]{11}, [dass]{12} [du]{14} [das]{13} [machsch]{14}?»",
 "JHN.2.19": "[De Jesus]{2} [hät gantwortet]{1} und{3} [zu ine]{5} [gseit]{4}: «[Riissed]{6} [dä]{9} [Tämpel]{7,8} [ab]{6}, und{10} [i]{11} [drüü]{12} [Täg]{13} [stell ich]{14} [en]{15} [uf]{14}.»",
 "JHN.2.20": "[Da]{2} [händ]{1} [d Jude]{3,4} [gseit]{1}: «[Sächsevierzg]{5-7} [Jahr]{8} [isch]{9} [a däm]{10,12} [Tämpel]{11} [buut worde]{9}, und{13} [du]{14} [wottsch]{18} [en]{19} [i]{15} [drüü]{16} [Täg]{17} [ufstelle]{18}?»",
 "JHN.2.21": "[Er]{1} [aber]{2} [hät]{3} [vom]{4,5} [Tämpel]{6} [vo sim]{9} [Liib]{7,8} [gredt]{3}.",
 "JHN.2.22": "[Wo]{1} [er]{3} [dänn]{2} [vo]{4} [de Tote]{5} [uferweckt worde isch]{3}, [händ sich]{6} [sini]{9} [Jünger]{7,8} [erinneret]{6}, [dass]{10} [er]{12} [das]{11} [gseit hät]{12}, und{13} [si händ]{14} [de Schrift]{15,16} und{17} [em Wort]{18,19} [glaubt]{14}, [wo]{20} [de Jesus]{22,23} [gseit hät]{21}.",
 "JHN.2.23": "[Wo]{1} [er]{3} [aber]{2} [am]{7,8} [Passa]{9}, [bim]{10,11} [Fäscht]{12}, [z]{4,5} [Jerusalem]{6} [gsii isch]{3}, [händ]{14} [vili]{13} [a]{15} [sin]{18} [Name]{16,17} [glaubt]{14}, [wil si]{19} [sini]{20} [Zeiche]{21,22} [gseh händ]{19}, [wo]{23} [er gmacht hät]{24}.",
 "JHN.2.24": "[De Jesus]{3} [sälber]{1} [aber]{2} [hät]{5} [sich]{6} [ine]{7} [nöd]{4} [aavertrout]{5}, [wil]{8,9} [er]{10} [alli]{12} [kännt hät]{11}",
 "JHN.2.25": "und{1} [wil]{2} [er]{5} [nöd]{3} [nötig]{4} [gha hät]{5}, [dass]{6} [öpper]{7} [über]{9} [de Mänsch]{10,11} [Zügnis git]{8}; [er sälber]{12} [hät]{14} [nämli]{13} [erchännt]{14}, [was]{15} [im]{17,18} [Mänsch]{19} [isch]{16}.",
 # ------------------------------------------------------------ Kapitel 3
 "JHN.3.1": "[Es isch]{1} [aber]{2} [en Mänsch]{3} [under]{4} [de Pharisäer]{5,6} [gsii]{1}, [sin]{9} [Name]{8} isch [Nikodemus]{7} gsii, [en Oberschte]{10} [vo de Jude]{11,12}.",
 "JHN.3.2": "[Dä]{1} [isch]{2} [znacht]{5} [zu]{3} [ihm]{4} [choo]{2} und{6} [hät]{7} [zu ihm]{8} [gseit]{7}: «[Rabbi]{9}, [mir wüssed]{10}, [dass]{11} [du]{14} [als Lehrer]{15} [vo]{12} [Gott]{13} [choo bisch]{14}; [dänn]{17} [niemer]{16} [cha]{18} [die]{19,20} [Zeiche]{21} [mache]{22}, [wo]{23} [du]{24} [machsch]{25}, [wänn]{26} [Gott]{29,30} [nöd]{27} [mit]{31} [ihm]{32} [isch]{28}.»",
 "JHN.3.3": "[De Jesus]{2} [hät gantwortet]{1} und{3} [zu ihm]{5} [gseit]{4}: «[Amen]{6}, [amen]{7}, [ich säge]{8} [dir]{9}: [Wänn]{10} [öpper]{12} [nöd]{11} [vo obe]{14} [gebore wird]{13}, [cha er]{16} [s Riich]{18,19} [vo Gott]{20,21} [nöd]{15} [gseh]{17}.»",
 "JHN.3.4": "[De Nikodemus]{4,5} [seit]{1} [zu]{2} [ihm]{3}: «[Wie]{6} [cha]{7} [en Mänsch]{8} [gebore wärde]{9}, [wänn er]{11} [alt]{10} [isch]{11}? [Cha er]{13} [öppe]{12} [es zweits Mal]{20} [i]{14} [de]{15} [Buuch]{16} [vo sinere]{19} [Mueter]{17,18} [inegaa]{21} und{22} [gebore wärde]{23}?»",
 "JHN.3.5": "[De Jesus]{2} [hät gantwortet]{1}: «[Amen]{3}, [amen]{4}, [ich säge]{5} [dir]{6}: [Wänn]{7} [öpper]{9} [nöd]{8} [us]{11} [Wasser]{12} und{13} [Geischt]{14} [gebore wird]{10}, [cha er]{16} [nöd]{15} [i]{18} [s Riich]{19,20} [vo Gott]{21,22} [inechoo]{17}.",
 "JHN.3.6": "[Was]{1} [us]{3} [em Fleisch]{4,5} [gebore isch]{2}, [isch]{7} [Fleisch]{6}, und{8} [was]{9} [us]{11} [em Geischt]{12,13} [gebore isch]{10}, [isch]{15} [Geischt]{14}.",
 "JHN.3.7": "[Wunder dich]{2} [nöd]{1}, [dass]{3} [ich]{4} [dir]{5} [gseit han]{4}: ‹[Ir]{7} [müend]{6} [vo obe]{9} [gebore wärde]{8}.›",
 "JHN.3.8": "[De Wind]{1,2} [wäiht]{5}, [wo]{3} [er wott]{4}, und{6} [du ghörsch]{10} [sis]{9} [Ruusche]{7,8}, [aber]{11} [du weisch]{13} [nöd]{12}, [vo wo]{14} [er chunnt]{15} und{16} [wohi]{17} [er gaat]{18}. [So]{19} [isch es]{20} [mit jedem]{21}, [wo]{22} [us]{24} [em Geischt]{25,26} [gebore isch]{23}.»",
 "JHN.3.9": "[De Nikodemus]{2} [hät gantwortet]{1} und{3} [zu ihm]{5} [gseit]{4}: «[Wie]{6} [cha]{7} [das]{8} [gscheh]{9}?»",
 "JHN.3.10": "[De Jesus]{2} [hät gantwortet]{1} und{3} [zu ihm]{5} [gseit]{4}: «[Du]{6} [bisch]{7} [de Lehrer]{8,9} [vo Israel]{10,11} und{12} [verstaasch]{15} [das]{13} [nöd]{14}?",
 "JHN.3.11": "[Amen]{1}, [amen]{2}, [ich säge]{3} [dir]{4}: [Was]{6} [mir wüssed]{7}, [devo reded mir]{8}, und{9} [was]{10} [mir gseh händ]{11}, [das bezüüged mir]{12}; und{13} [üses]{16} [Zügnis]{14,15} [nämed ir]{18} [nöd]{17} [aa]{18}. ~5(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "JHN.3.12": "[Wänn]{1} [ich]{4} [eu]{5} [Irdischs]{2,3} [gseit han]{4} und{6} [ir]{8} [nöd]{7} [glaubed]{8}, [wie]{9} [wärded ir glaube]{15}, [wänn]{10} [ich]{11} [eu]{12} [Himmlischs]{13,14} [säge]{11}?",
 "JHN.3.13": "Und{1} [niemer]{2} [isch]{3} [i]{4} [de Himmel]{5,6} [ufegstige]{3} [usser]{7,8} [dä, wo]{9} [us]{10} [em Himmel]{11,12} [abegstige isch]{13}, [de Mänschesohn]{14-17}.",
 "JHN.3.14": "Und{1} [wie]{2} [de Mose]{3} [d Schlange]{5,6} [i]{7} [de Wüeschti]{8,9} [erhöcht hät]{4}, [so]{10} [mues]{12} [de Mänschesohn]{13-16} [erhöcht wärde]{11},",
 "JHN.3.15": "[demit]{1} [jede]{2}, [wo]{3} [glaubt]{4}, [in]{5} [ihm]{6} [ewigs]{9} [Läbe]{8} [hät]{7}.",
 "JHN.3.16": "[Dänn]{2} [so]{1} [hät]{3} [Gott]{4,5} [d Wält]{6,7} [gliebt]{3}, [dass]{8} [er]{13} [de einzig]{11,12} [Sohn]{9,10} [gää hät]{13}, [demit]{14} [jede]{15}, [wo]{16} [a]{18} [ihn]{19} [glaubt]{17}, [nöd]{20} [verlore gaat]{21}, [sondern]{22} [ewigs]{25} [Läbe]{24} [hät]{23}.",
 "JHN.3.17": "[Dänn]{2} [Gott]{4,5} [hät]{3} [de Sohn]{6,7} [nöd]{1} [i]{8} [d Wält]{9,10} [gschickt]{3}, [demit]{11} [er]{12} [d Wält]{13,14} [richtet]{12}, [sondern]{15} [demit]{16} [d Wält]{18,19} [dur]{20} [ihn]{21} [grettet wird]{17}.",
 "JHN.3.18": "[Wer]{1} [a]{3} [ihn]{4} [glaubt]{2}, [wird]{6} [nöd]{5} [grichtet]{6}; [wer]{7} [aber]{8} [nöd]{9} [glaubt]{10}, [isch]{12} [scho]{11} [grichtet]{12}, [wil]{13} [er]{15} [nöd]{14} [a]{16} [de Name]{17,18} [vom einzige]{19,20} [Sohn]{21} [vo Gott]{22,23} [glaubt hät]{15}.",
 "JHN.3.19": "[Das]{1} [aber]{2} [isch]{3} [s Gricht]{4,5}: [S Liecht]{7,8} [isch]{9} [i]{10} [d Wält]{11,12} [choo]{9}, und{13} [d Mänsche]{15,16} [händ]{14} [d Fiischteri]{18,19} [meh]{17} [gliebt]{14} [als]{20} [s Liecht]{21,22}; [dänn]{24} [iri]{25} [Wärch]{27,28} [sind]{23} [bös]{26} [gsii]{23}. ~6(ὅτι leitet de Inhalt ii; mit em Doppelpunkt widergää)",
 "JHN.3.20": "[Dänn]{2} [jede]{1}, [wo]{3} [Schlächts]{4} [tuet]{5}, [hasst]{6} [s Liecht]{7,8} und{9} [chunnt]{11} [nöd]{10} [zum]{12,13} [Liecht]{14}, [demit]{15} [sini]{20} [Wärch]{18,19} [nöd]{16} [ufdeckt wärded]{17}.",
 "JHN.3.21": "[Wer]{1} [aber]{2} [d Wahrheit]{4,5} [tuet]{3}, [chunnt]{6} [zum]{7,8} [Liecht]{9}, [demit]{10} [sichtbar wird]{11}, [dass]{15} [sini]{12} [Wärch]{13,14} [in]{16} [Gott]{17} [taa]{19} [sind]{18}.»",
 "JHN.3.22": "[Dänn]{1,2} [sind]{3} [de Jesus]{4,5} und{6} [sini]{9} [Jünger]{7,8} [is]{10,11} [judäisch]{12} [Land]{13} [choo]{3}, und{14} [er hät sich]{16} [dört]{15} [mit]{17} [ine]{18} [ufghalte]{16} und{19} [hät tauft]{20}.",
 "JHN.3.23": "[Aber]{2} [au]{3} [de Johannes]{4,5} [hät]{1} [z]{7} [Änon]{8} [nöch]{9} [bi Salim]{10,11} [tauft]{6}, [wil]{12} [dört]{16} [vil]{14} [Wasser]{13} [gsii isch]{15}; und{17} [d Lüüt sind choo]{18} und{19} [händ sich la taufe]{20}.",
 "JHN.3.24": "[De Johannes]{8,9} [isch]{3} [nämli]{2} [no nöd]{1} [is]{5,6} [Gfängnis]{7} [gworfe worde]{4}.",
 "JHN.3.25": "[Da]{2} [isch es]{1} [zumene Striit]{3} [choo]{1} [zwüsche]{4} [de Jünger]{5,6} [vom Johannes]{7} [und]{8} [eme Jud]{9} [über]{10} [d Reinigung]{11}.",
 "JHN.3.26": "Und{1} [si sind]{2} [zum]{3,4} [Johannes]{5} [choo]{2} und{6} [händ]{7} [zu ihm]{8} [gseit]{7}: «[Rabbi]{9}, [dä, wo]{10} [bi]{12} [dir]{13} [gsii isch]{11} [ännet]{14} [em Jordan]{15,16}, [für dä]{17} [du]{18} [Zügnis gää häsch]{19} – [lueg]{20}, [dä]{21} [tauft]{22}, und{23} [alli]{24} [chömed]{25} [zu]{26} [ihm]{27}!»",
 "JHN.3.27": "[De Johannes]{2} [hät gantwortet]{1} und{3} [gseit]{4}: «[En Mänsch]{7} [cha]{6} [nüüt]{5,9,10} [übercho]{8}, [wänn]{11} s [ihm]{15} [nöd]{12} [vom]{16,17} [Himmel]{18} [gää]{14} [isch]{13}.",
 "JHN.3.28": "[Ir]{2} [sälber]{1} [bezüüged]{4} [mir]{3}, [dass]{5} [ich gseit han]{6}: ‹[Ich]{9} [bi]{8} [nöd]{7} [de Christus]{10,11}›, [sondern]{12}: ‹[Ich bi]{15} [vor]{16} [ihm]{17} [här]{16} [gschickt]{14}.› ~13(ὅτι leitet di diräkt Red ii)",
 "JHN.3.29": "[Wer]{1} [d Bruut]{3,4} [hät]{2}, [isch]{6} [de Brüütigam]{5}; [de Fründ]{7,9} [vom Brüütigam]{10,11} [aber]{8}, [wo]{12} [debii staat]{13} und{14} [ihn]{16} [ghört]{15}, [fröit sich]{18} [vo Herze]{17} [über]{19} [d]{20} [Stimm]{21} [vom Brüütigam]{22,23}. [Die]{24} [Fröid]{26,27} [vo mir]{28,29} [isch]{30} [also]{25} [erfüllt]{30}.",
 "JHN.3.30": "[Er]{1} [mues]{2} [wachse]{3}, [ich]{4} [aber]{5} [chliiner wärde]{6}.",
 "JHN.3.31": "[Dä, wo]{1} [vo obe]{2} [chunnt]{3}, [isch]{6} [über]{4} [allne]{5}. [Wer]{7} [vo]{9} [de Ärde]{10,11} [isch]{8}, [isch]{15} [vo]{12} [de Ärde]{13,14} und{16} [redt]{20} [vo]{17} [de Ärde]{18,19} [här]{17}. [Dä, wo]{21} [vom]{22,23} [Himmel]{24} [chunnt]{25}, [isch]{28} [über]{26} [allne]{27}.",
 "JHN.3.32": "[Was]{1} [er gseh]{2} und{3} [ghört hät]{4}, [das]{5} [bezüügt er]{6}, und{7} [sis]{10} [Zügnis]{8,9} [nimmt]{12} [niemer]{11} [aa]{12}.",
 "JHN.3.33": "[Wer]{1} [sis]{3} [Zügnis]{4,5} [aagnoo hät]{2}, [hät bsiglet]{6}, [dass]{7} [Gott]{8,9} [wahrhaftig]{10} [isch]{11}.",
 "JHN.3.34": "[Dänn]{2} [dä, wo]{1} [Gott]{4,5} [gschickt hät]{3}, [redt]{10} [d Wort]{6,7} [vo Gott]{8,9}; [dänn]{12} [er git]{15} [de Geischt]{16,17} [nöd]{11} [nach]{13} [Mass]{14}.",
 "JHN.3.35": "[De Vatter]{1,2} [liebt]{3} [de Sohn]{4,5}, und{6} [er hät]{8} [alles]{7} [i]{9} [sini]{12} [Hand]{10,11} [gää]{8}.",
 "JHN.3.36": "[Wer]{1} [a]{3} [de Sohn]{4,5} [glaubt]{2}, [hät]{6} [ewigs]{8} [Läbe]{7}; [wer]{9} [aber]{10} [em Sohn]{12,13} [nöd folget]{11}, [wird]{15} [s Läbe]{16} [nöd]{14} [gseh]{15}, [sondern]{17} [de Zorn]{18,19} [vo Gott]{20,21} [bliibt]{22} [uf]{23} [ihm]{24}.»",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("JHN.1.1", "das Wort", "literal", "λόγος", None, ["der Logos", "die Rede", "der Sinn"],
  "Grundentscheid für das ganze Evangelium: λόγος heisst «Wort, Rede, Aussage», in der griechischen Philosophie auch «Vernunft, Weltordnung». Der Prolog knüpft an [[GEN.1.1]] an («Im Anfang», griechisch ἐν ἀρχῇ wie in der Septuaginta) und an Gottes schaffendes Wort ([[PSA.33.6]]); viele sehen auch Anklänge an die Weisheit, die bei Gott war ([[PRO.8.22]]–[[PRO.8.30]]). Was genau den Hintergrund bildet (biblisch-jüdische Weisheit, griechische Philosophie oder beides), ist umstritten. Als Titel steht das Wort nur im Prolog ([[JHN.1.1]], [[JHN.1.14]]); sonst heisst λόγος im Evangelium die gesprochene Rede (z. B. [[JHN.2.22]]) und ist ebenfalls mit «Wort» wiedergegeben. Fürwörter für das Wort sind bis [[JHN.1.5]] sächlich («es»), ab [[JHN.1.10]] männlich («er, ihn»), weil der Text dort von einer Person spricht."),
 ("JHN.1.1", "bei Gott", "literal", "πρὸς τὸν θεόν", "zu Gott hin", ["mit Gott", "Gott zugewandt"],
  "πρός mit Akkusativ heisst meist «zu … hin», bei «sein» auch «bei». Manche lesen darin eine Zuwendung des Wortes zu Gott; die Übersetzung bleibt bei der verbreiteten Bedeutung «bei». Ebenso [[JHN.1.2]]."),
 ("JHN.1.1", "das Wort war Gott", "interpretive", "θεὸς ἦν ὁ λόγος", "Gott war das Wort", ["das Wort war göttlich", "das Wort war von Gottes Art", "ein Gott war das Wort"],
  "θεός steht voran und ohne Artikel, ὁ λόγος mit Artikel ist das Subjekt. Damit ist das Wort nicht einfach mit «dem Gott» gleichgesetzt, bei dem es ist, aber ihm wird zugesprochen, was Gott ist. «Das Wort war Gott» macht das Subjekt im Deutschen eindeutig. «Göttlich» schwächt nach verbreitetem Urteil ab (dafür gäbe es griechisch θεῖος); «ein Gott» wird von einzelnen Übersetzungen vertreten, von den meisten abgelehnt, weil ein vorangestelltes Prädikatsnomen im Griechischen oft ohne Artikel steht und [[JHN.1.18]] den Einzigen ebenfalls θεός nennt. Redaktionelle Entscheidung."),
 ("JHN.1.3", "Was geworden ist", "interpretive", "ὃ γέγονεν", None, ["… und ohne es ist nichts geworden, was geworden ist. In ihm war Leben", "Was in ihm geworden ist, war Leben"],
  "Die ältesten Handschriften haben kaum Satzzeichen; wohin ὃ γέγονεν gehört, ist eine Entscheidung der Ausgaben. Der SBLGNT setzt (wie WH) den Punkt davor und zieht die Worte zum Folgenden; RP, KJTR, Stephanus und SR ziehen sie zum Vorigen (nach den CNTR-Texten dieser Ausgaben). Die Übersetzung folgt dem SBLGNT und lässt den Satzbruch sichtbar stehen. Nach den CNTR-Transkriptionen lesen 01 und 05 in [[JHN.1.4]] ἐστιν («in ihm ist Leben») statt ἦν."),
 ("JHN.1.4", "das Licht der Menschen", "literal", "τὸ φῶς τῶν ἀνθρώπων", None, None,
  "Grundentscheid: φῶς durchgehend «Licht», σκοτία (und das seltenere σκότος, [[JHN.3.19]]) durchgehend «Finsternis». Der Gegensatz trägt das ganze Evangelium (z. B. [[JHN.8.12]], [[JHN.12.35]]–[[JHN.12.36]]). Ob er eher an [[GEN.1.3]]–[[GEN.1.4]] anknüpft oder an zeitgenössische jüdische Sprache (etwa in den Qumranschriften), wird diskutiert."),
 ("JHN.1.5", "scheint", "literal", "φαίνει", None, None,
  "Präsens zwischen lauter Vergangenheitsformen: Das Licht scheint fortdauernd."),
 ("JHN.1.5", "erfasst", "interpretive", "κατέλαβεν", None, ["ergriffen", "überwältigt", "begriffen", "aufgenommen"],
  "καταλαμβάνω heisst «packen, in Besitz nehmen, überwältigen», im Medium auch «begreifen». Gemeint sein kann, dass die Finsternis das Licht nicht verstanden oder dass sie es nicht besiegt hat (vgl. [[JHN.12.35]]: «damit die Finsternis euch nicht überfällt», dasselbe Verb). «Erfasst» hält im Deutschen beides offen."),
 ("JHN.1.7", "Zeugnis abzulegen", "literal", "μαρτυρήσῃ", None, ["zu bezeugen"],
  "Grundentscheid: μαρτυρέω «bezeugen, Zeugnis ablegen», μαρτυρία «Zeugnis». Das Wortfeld ist ein Leitwort des Evangeliums (μαρτυρέω nach MACULA-Lemma 33-mal, μαρτυρία 14-mal im SBLGNT-Text)."),
 ("JHN.1.7", "zum Glauben kämen", "adapted", "πιστεύσωσιν", "glauben", None,
  "Der Aorist bezeichnet hier den Beginn des Glaubens. πιστεύω ist eines der häufigsten Verben des Evangeliums (nach MACULA-Lemma 98-mal); das Nomen πίστις kommt im Evangelium nicht vor."),
 ("JHN.1.9", "kam in die Welt", "interpretive", "ἦν ἐρχόμενον εἰς τὸν κόσμον", "war kommend in die Welt", ["Das wahre Licht, das jeden Menschen erleuchtet, der in die Welt kommt, war da"],
  "Das Partizip ἐρχόμενον kann zum Licht gehören (mit ἦν: «war im Kommen», so hier) oder zu «jeden Menschen» («der in die Welt kommt», so Luther 1912). Für den Bezug auf das Licht spricht, dass Johannes das Kommen in die Welt sonst von Jesus sagt ([[JHN.3.19]], [[JHN.6.14]])."),
 ("JHN.1.9", "wahre", "literal", "ἀληθινὸν", None, ["echte", "wirkliche"],
  "ἀληθινός meint bei Johannes das Echte gegenüber dem Vorläufigen (vgl. [[JHN.6.32]], [[JHN.15.1]])."),
 ("JHN.1.10", "Welt", "literal", "κόσμῳ", None, None,
  "Grundentscheid: κόσμος durchgehend «Welt» (nach MACULA-Lemma 78-mal im SBLGNT-Text). Das Wort meint je nach Stelle die Schöpfung (hier: «durch ihn geworden»), die Menschheit, die Gott liebt ([[JHN.3.16]]), oder die Menschenwelt, die sich Gott verschliesst (hier: «hat ihn nicht erkannt»). Die einheitliche Wiedergabe lässt diese Spannweite sichtbar."),
 ("JHN.1.11", "sein Eigentum", "interpretive", "τὰ ἴδια", "das Eigene", ["zu dem, was ihm gehört", "nach Hause"],
  "Sächlich τὰ ἴδια («das Eigene»), dann männlich οἱ ἴδιοι («die Eigenen»). Meist auf Israel bezogen, von manchen auf die ganze Menschenwelt, die ihm als Schöpfer gehört."),
 ("JHN.1.12", "die Vollmacht", "literal", "ἐξουσίαν", None, ["das Recht", "die Macht"], None),
 ("JHN.1.13", "Blut", "adapted", "αἱμάτων", "Blüten", ["Blutsverwandtschaft"],
  "Griechisch Plural («aus Blüten»), wohl nach antiker Vorstellung von der Zeugung aus dem Blut der Eltern. Die drei Verneinungen schliessen jede natürliche Abstammung als Grund der Gotteskindschaft aus."),
 ("JHN.1.14", "wurde Fleisch", "literal", "σὰρξ ἐγένετο", None, ["wurde Mensch"],
  "σάρξ meint den ganzen Menschen in seiner Vergänglichkeit und Verletzlichkeit, nicht einen Teil des Menschen. Die harte wörtliche Wendung ist beibehalten."),
 ("JHN.1.14", "wohnte", "adapted", "ἐσκήνωσεν", "zeltete", ["schlug sein Zelt auf", "nahm Wohnung"],
  "σκηνόω kommt von σκηνή «Zelt». Viele hören einen Anklang an das Zelt der Begegnung, das Gottes Herrlichkeit erfüllte ([[EXO.40.34]]); im selben Vers folgt «Herrlichkeit»."),
 ("JHN.1.14", "Herrlichkeit", "literal", "δόξαν", None, ["Glanz", "Ehre"],
  "Grundentscheid: δόξα durchgehend «Herrlichkeit», δοξάζω «verherrlichen». In der griechischen Bibel gibt δόξα das hebräische kāḇôd wieder: Gewicht, Ehre, sichtbarer Glanz von Gottes Gegenwart ([[EXO.33.18]]). Bei Johannes zeigt sie sich in den Zeichen ([[JHN.2.11]]) und gerade in der «Stunde» von Tod und Erhöhung ([[JHN.12.23]], [[JHN.17.1]]). Verbindlich steht «Ehre» nur, wo δόξα das Ansehen bei Menschen meint ([[JHN.5.41]], [[JHN.5.44]], [[JHN.7.18]], [[JHN.8.50]], [[JHN.8.54]], [[JHN.9.24]], [[JHN.12.43]]), jeweils mit eigener Entscheidung."),
 ("JHN.1.14", "des Einzigen", "interpretive", "μονογενοῦς", "eines Einziggeborenen", ["des eingeborenen Sohnes", "des einzigen Sohnes"],
  "μονογενής (aus μόνος «allein» und γένος «Art, Herkunft») heisst «einzig in seiner Art, einziges Kind» (vgl. [[LUK.7.12]]). Die vertraute Wiedergabe «eingeboren» folgt dem lateinischen unigenitus. «Sohn» steht hier nicht im Text; der Vergleich «wie die eines Einzigen vom Vater» legt ihn nahe. Ebenso [[JHN.1.18]], [[JHN.3.16]], [[JHN.3.18]] und [[1JN.4.9]] («einzigen»)."),
 ("JHN.1.14", "voller Gnade und Wahrheit", "literal", "πλήρης χάριτος καὶ ἀληθείας", None, ["voll Gnade und Treue"],
  "Viele hören einen Anklang an Gottes Selbstbeschreibung in [[EXO.34.6]] (hebräisch raḇ-ḥeseḏ weʾĕmeṯ, «reich an Güte und Treue»). πλήρης kann sich auf das Wort, auf «ihn» oder auf die Herrlichkeit beziehen."),
 ("JHN.1.15", "ist mir voraus", "interpretive", "ἔμπροσθέν μου γέγονεν", "ist vor mir geworden", ["steht über mir", "hat den Vorrang vor mir"],
  "Der Satz spielt mit Zeit und Rang: Der nach Johannes kommt, steht im Rang vor ihm, weil er schon vor ihm war (πρῶτός μου ἦν). Johannes steht im SBLGNT in runden Klammern; der Satz unterbricht den Prolog. Ebenso [[JHN.1.30]]."),
 ("JHN.1.16", "Gnade um Gnade", "interpretive", "χάριν ἀντὶ χάριτος", "Gnade anstelle von Gnade", ["Gnade über Gnade", "eine Gnade anstelle der anderen"],
  "ἀντί heisst meist «anstelle von». Gedeutet wird auf immer neue Gnade, die auf die vorige folgt, oder auf die Gnade in Christus anstelle der Gabe des Gesetzes (vgl. [[JHN.1.17]]). «Gnade um Gnade» lässt beides offen."),
 ("JHN.1.17", "das Gesetz", "traditional", "νόμος", None, ["die Tora", "die Weisung"],
  "Zwischen den beiden Satzhälften steht kein «aber». Ob Gesetz und Gnade als Gegensatz oder als Steigerung gedacht sind, ist umstritten; die Übersetzung setzt kein Bindewort hinzu."),
 ("JHN.1.18", "der Einzige, Gott,", "interpretive", "μονογενὴς θεὸς", "einziggeborener Gott", ["der einzige Sohn, der Gott ist", "der einzige Gott", "der Einzige, selbst Gott"],
  "Der SBLGNT liest μονογενὴς θεός (siehe Alternative zur Lesart «der einzige Sohn»). Die beiden Wörter können als Einheit («der einzige Gott») oder als Nebeneinander («der Einzige, Gott») gelesen werden. Die Übersetzung trennt sie durch Kommas, damit nicht der Eindruck eines zweiten Gottes neben dem Vater entsteht und doch beide Wörter stehen bleiben; redaktionelle Entscheidung. Der Satz schliesst den Bogen zu [[JHN.1.1]]."),
 ("JHN.1.18", "an der Brust", "interpretive", "εἰς τὸν κόλπον", "in den Schoss", ["im Schoss", "an der Seite", "in enger Gemeinschaft mit"],
  "Bild der nächsten Nähe, wie beim Liegen zu Tisch; vgl. den Lieblingsjünger «an der Brust Jesu» ([[JHN.13.23]], dort ἐν τῷ κόλπῳ)."),
 ("JHN.1.18", "hat Kunde gebracht", "interpretive", "ἐξηγήσατο", None, ["hat ihn ausgelegt", "hat ihn erklärt", "hat von ihm erzählt"],
  "ἐξηγέομαι heisst «erzählen, auslegen, erklären» (davon «Exegese»). Ein Objekt fehlt; gemeint ist der Gott, den niemand gesehen hat."),
 ("JHN.1.19", "die Juden", "interpretive", "οἱ Ἰουδαῖοι", None, ["die jüdischen Behörden", "die jüdischen Führer", "die Judäer"],
  "Grundentscheid (siehe translation_notes): οἱ Ἰουδαῖοι wird durchgehend wörtlich mit «die Juden» wiedergegeben. Hier sind offensichtlich die Jerusalemer Autoritäten gemeint: Sie senden Priester und Leviten aus Jerusalem (vgl. [[JHN.1.24]]: Pharisäer). Die Wiedergabe «die jüdischen Führer» würde das verdeutlichen, legt aber eine Deutung in den Text."),
 ("JHN.1.20", "der Christus", "traditional", "ὁ χριστός", None, ["der Messias", "der Gesalbte"],
  "χριστός übersetzt hebräisch māšîaḥ «Gesalbter» (vgl. [[JHN.1.41]]). Ebenso [[JHN.1.25]] und [[JHN.3.28]]."),
 ("JHN.1.21", "Elija", "literal", "Ἠλίας", None, None,
  "Nach [[MAL.4.5]] (im hebräischen Text 3,23) wurde die Rückkehr des Elija vor dem Tag JHWHs erwartet."),
 ("JHN.1.21", "der Prophet", "literal", "Ὁ προφήτης", None, None,
  "Wohl der Prophet wie Mose, den [[DEU.18.15]]–[[DEU.18.18]] ankündigt (vgl. [[JHN.6.14]], [[JHN.7.40]])."),
 ("JHN.1.23", "des Herrn", "literal", "κυρίου", None, None,
  "Zitat aus [[ISA.40.3]]. Im hebräischen Text steht dort der Gottesname JHWH, in der Septuaginta κύριος. Johannes zitiert frei und knapp (εὐθύνατε «macht gerade» fasst die zwei Glieder der Septuaginta zusammen)."),
 ("JHN.1.24", "sie waren von den Pharisäern gesandt", "interpretive", "ἀπεσταλμένοι ἦσαν ἐκ τῶν Φαρισαίων", None, ["es waren auch Pharisäer unter den Gesandten"],
  "ἐκ τῶν Φαρισαίων kann die Absender nennen oder (partitiv) sagen, dass die Gesandten zu den Pharisäern gehörten."),
 ("JHN.1.28", "Betanien jenseits des Jordan", "literal", "Βηθανίᾳ πέραν τοῦ Ἰορδάνου", None, ["Betabara"],
  "Nicht das Betanien bei Jerusalem ([[JHN.11.18]]); die Lage ist unbekannt. Nach den CNTR-Texten lesen 029, KJTR und Stephanus Βηθαβαρά («Betabara»), so auch Luther 1912; die übrigen erfassten Zeugen Βηθανία."),
 ("JHN.1.29", "das Lamm Gottes", "literal", "ὁ ἀμνὸς τοῦ θεοῦ", None, None,
  "Erwogen werden Bezüge auf das Passalamm ([[EXO.12.3]]–[[EXO.12.13]]; vgl. [[JHN.19.36]]), auf den Gottesknecht, der wie ein Lamm zur Schlachtung geführt wird ([[ISA.53.7]]), auf das tägliche Opfer und auf das Lamm als Siegergestalt (vgl. [[REV.5.6]]). Der Text legt sich nicht fest."),
 ("JHN.1.29", "wegnimmt", "interpretive", "αἴρων", None, ["trägt", "hinwegträgt"],
  "αἴρω heisst «aufheben, tragen, wegnehmen». Beides ist möglich: die Sünde stellvertretend tragen oder sie beseitigen. Singular: «die Sünde der Welt»."),
 ("JHN.1.32", "er blieb", "literal", "ἔμεινεν", None, None,
  "Grundentscheid: μένω durchgehend «bleiben» (nach MACULA-Lemma 40-mal im SBLGNT-Text). Das Wort verbindet das alltägliche Verweilen ([[JHN.1.39]], [[JHN.2.12]]) mit der bleibenden Gemeinschaft ([[JHN.15.4]]–[[JHN.15.10]]). Ebenso [[JHN.1.33]] und [[JHN.3.36]]."),
 ("JHN.1.33", "mit heiligem Geist", "literal", "ἐν πνεύματι ἁγίῳ", None, ["mit dem Heiligen Geist"],
  "Ohne Artikel wie in [[MRK.1.8]]."),
 ("JHN.1.34", "der Erwählte Gottes", "literal", "ὁ ἐκλεκτὸς τοῦ θεοῦ", None, ["der Sohn Gottes"],
  "Der SBLGNT liest hier ἐκλεκτός (mit Holmes und der Randlesart von WH), WH, Treg, NA28 und RP lesen υἱός «Sohn»; siehe Alternative. Anklang an [[ISA.42.1]]."),
 ("JHN.1.38", "ist deine Bleibe", "adapted", "μένεις", "bleibst du", ["wohnst du", "hältst du dich auf"],
  "μένω heisst hier «sich aufhalten, wohnen». «Wo bleibst du?» würde im Deutschen nach Ungeduld klingen; das Nomen «Bleibe» hält den Wortstamm fest, der im Evangelium Gewicht bekommt (Grundentscheid zu [[JHN.1.32]]). Ebenso [[JHN.1.39]] («wo seine Bleibe war … sie blieben»)."),
 ("JHN.1.38", "Rabbi", "literal", "Ῥαββί", None, None,
  "Hebräisch-aramäisch «mein Grosser, mein Meister»; Johannes übersetzt selbst mit διδάσκαλε «Lehrer»."),
 ("JHN.1.39", "die zehnte Stunde", "literal", "ὥρα δεκάτη", None, ["vier Uhr nachmittags"],
  "Bei Zählung ab Sonnenaufgang etwa 16 Uhr; manche nehmen eine Zählung ab Mitternacht an (10 Uhr vormittags). Umstritten."),
 ("JHN.1.41", "den Messias", "literal", "τὸν Μεσσίαν", None, ["den Gesalbten"],
  "Griechische Umschrift des aramäischen məšîḥāʾ «Gesalbter»; im Neuen Testament nur hier und [[JHN.4.25]]. Johannes übersetzt selbst mit χριστός."),
 ("JHN.1.41", "zuerst", "interpretive", "πρῶτον", None, ["als Erster"],
  "Adverb: Andreas findet zuerst, vor allem anderen, seinen Bruder. Zur Lesart πρῶτος («als Erster») siehe Alternative."),
 ("JHN.1.42", "Kephas", "literal", "Κηφᾶς", None, None,
  "Griechische Umschrift des aramäischen kêp̄āʾ «Fels, Stein»; Πέτρος ist das griechische Wort dafür. Johannes übersetzt selbst."),
 ("JHN.1.45", "im Gesetz geschrieben hat und die Propheten", "literal", "ἔγραψεν ἐν τῷ νόμῳ καὶ οἱ προφῆται", None, None,
  "«Gesetz und Propheten» steht für die Schrift als Ganze."),
 ("JHN.1.46", "kommen", "adapted", "εἶναι", "sein", None, None),
 ("JHN.1.47", "Falschheit", "interpretive", "δόλος", None, ["List", "Betrug", "Hinterlist"],
  "Viele sehen ein Wortspiel mit Jakob-Israel, der seinem Vater «mit List» (Septuaginta μετὰ δόλου) den Segen nahm ([[GEN.27.35]]); vgl. die Jakobsleiter in [[JHN.1.51]]."),
 ("JHN.1.51", "Amen, amen, ich sage euch", "literal", "Ἀμὴν ἀμὴν λέγω ὑμῖν", None, ["Wahrlich, wahrlich, ich sage euch", "Ganz gewiss, ich sage euch"],
  "Grundentscheid: Das doppelte ἀμήν bleibt «Amen, amen» (im SBLGNT-Text 25-mal, per Skript aus den MACULA-Lemmata gezählt; in den Evangelien nur bei Johannes verdoppelt). Es bekräftigt das folgende Wort Jesu im Voraus. Der Plural «euch» richtet sich nach dem Satz an Natanaël an alle Jünger."),
 ("JHN.1.51", "den Menschensohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "den Sohn des Menschen", ["den Menschen"],
  "Wie bei Markus «Menschensohn». Das Bild nimmt Jakobs Traum auf ([[GEN.28.12]]): Die Engel steigen nun auf und ab «auf den Menschensohn»."),
 ("JHN.2.4", "Was habe ich mit dir zu tun, Frau?", "interpretive", "Τί ἐμοὶ καὶ σοί, γύναι", "Was mir und dir, Frau?", ["Was geht das dich und mich an, Frau?", "Was willst du von mir, Frau?"],
  "Hebräisch geprägte Wendung (vgl. [[JDG.11.12]], [[1KI.17.18]]), die Abstand oder Abwehr ausdrückt; wie scharf sie hier klingt, wird verschieden beurteilt. γύναι («Frau») ist keine unhöfliche Anrede; so redet Jesus auch am Kreuz seine Mutter an ([[JHN.19.26]])."),
 ("JHN.2.4", "Meine Stunde", "literal", "ἡ ὥρα μου", None, None,
  "Die «Stunde» Jesu ist im Evangelium die Zeit seines Todes und seiner Verherrlichung (vgl. [[JHN.7.30]], [[JHN.12.23]], [[JHN.13.1]])."),
 ("JHN.2.6", "Metreten", "literal", "μετρητὰς", None, ["Mass"],
  "Ein Metretes fasste nach gängiger Umrechnung etwa 39 Liter; sechs Krüge zu je zwei oder drei Metreten ergeben rund 470 bis 700 Liter."),
 ("JHN.2.9", "Speisemeister", "traditional", "ἀρχιτρίκλινος", None, ["Tafelmeister", "Festleiter"],
  "Der Verantwortliche für Mahl und Getränke beim Fest."),
 ("JHN.2.10", "betrunken sind", "interpretive", "μεθυσθῶσιν", None, ["reichlich getrunken haben"],
  "μεθύσκομαι heisst «betrunken werden»; hier als allgemeine Regel des Festbetriebs gesagt."),
 ("JHN.2.11", "Anfang der Zeichen", "literal", "ἀρχὴν τῶν σημείων", None, ["das erste der Zeichen"],
  "Grundentscheid: σημεῖον durchgehend «Zeichen», nicht «Wunder». Die Taten Jesu verweisen über sich hinaus auf seine Herrlichkeit und rufen zum Glauben ([[JHN.20.30]]–[[JHN.20.31]]). Das bei den anderen Evangelien übliche δύναμις («Machttat») kommt im Johannesevangelium nicht vor (nach MACULA-Lemma 0-mal)."),
 ("JHN.2.12", "den Brüdern", "literal", "οἱ ἀδελφοὶ", None, ["seinen Brüdern"],
  "Der SBLGNT hat kein αὐτοῦ («seinen»); NA28 und RP lesen es (SBLGNT-Apparat). Wer mit den Brüdern Jesu gemeint ist (leibliche Brüder, Halbbrüder oder Verwandte), ist zwischen den Kirchen umstritten."),
 ("JHN.2.14", "Tempel", "literal", "ἱερῷ", None, ["Tempelbezirk"],
  "ἱερόν ist der ganze Tempelbezirk mit den Vorhöfen; ναός ([[JHN.2.19]]–[[JHN.2.21]]) ist das Tempelhaus. Beides heisst hier «Tempel»."),
 ("JHN.2.16", "das Haus meines Vaters", "literal", "τὸν οἶκον τοῦ πατρός μου", None, None,
  "Zum ersten Mal nennt Jesus Gott «meinen Vater»."),
 ("JHN.2.17", "Der Eifer um dein Haus wird mich verzehren", "literal", "Ὁ ζῆλος τοῦ οἴκου σου καταφάγεταί με", None, None,
  "Zitat aus [[PSA.69.9]] (in der Septuaginta mit Vergangenheitsform, hier Futur). Das Futur kann auf den Tod Jesu vorausweisen."),
 ("JHN.2.18", "die Juden", "interpretive", "οἱ Ἰουδαῖοι", None, ["die Tempelbehörden", "die jüdischen Führer"],
  "Grundentscheid zu [[JHN.1.19]]; gemeint sind wohl die für den Tempel Verantwortlichen."),
 ("JHN.2.19", "Reisst diesen Tempel nieder", "interpretive", "Λύσατε τὸν ναὸν τοῦτον", "Löst diesen Tempel auf", ["Wenn ihr diesen Tempel niederreisst"],
  "Imperativ mit bedingendem Sinn: kein Auftrag, sondern «wenn ihr …». ναός ist das Tempelhaus; Johannes deutet es in [[JHN.2.21]] auf den Leib Jesu."),
 ("JHN.2.19", "aufrichten", "interpretive", "ἐγερῶ", None, ["auferwecken", "wieder aufbauen"],
  "ἐγείρω heisst «aufrichten, errichten» bei Gebäuden und «auferwecken» bei Toten (vgl. ἠγέρθη in [[JHN.2.22]]). Das Missverständnis lebt von diesem Doppelsinn. Ebenso [[JHN.2.20]]."),
 ("JHN.2.20", "Sechsundvierzig Jahre", "literal", "Τεσσεράκοντα καὶ ἓξ ἔτεσιν", None, None,
  "Gemeint ist der Ausbau des Tempels unter Herodes, den Josephus (Jüdische Altertümer 15,380) ins 18. Regierungsjahr des Herodes setzt (etwa 20/19 v. Chr.)."),
 ("JHN.2.22", "auferweckt worden war", "literal", "ἠγέρθη", None, ["auferstanden war"],
  "Passiv von ἐγείρω: Gott ist der Handelnde."),
 ("JHN.2.24", "vertraute sich ihnen nicht an", "literal", "οὐκ ἐπίστευεν αὑτὸν αὐτοῖς", None, None,
  "Wortspiel mit [[JHN.2.23]]: Viele «glaubten» (ἐπίστευσαν) an ihn, er aber «glaubte» sich ihnen nicht an (dasselbe Verb)."),
 ("JHN.3.1", "ein Oberster der Juden", "traditional", "ἄρχων τῶν Ἰουδαίων", None, ["ein führendes Mitglied des Hohen Rates", "ein Ratsherr"],
  "ἄρχων ist ein führender Mann, wohl ein Mitglied des Hohen Rates (vgl. [[JHN.7.50]])."),
 ("JHN.3.2", "bei Nacht", "literal", "νυκτὸς", None, None,
  "Ob die Nacht nur die Zeit angibt oder auch an Licht und Finsternis ([[JHN.3.19]]–[[JHN.3.21]]) erinnern soll, ist offen."),
 ("JHN.3.3", "von oben", "interpretive", "ἄνωθεν", None, ["von neuem", "noch einmal", "neu"],
  "ἄνωθεν heisst «von oben» und «von neuem». Nikodemus versteht «ein zweites Mal» ([[JHN.3.4]]); bei Johannes heisst das Wort sonst «von oben» ([[JHN.3.31]], [[JHN.19.11]], [[JHN.19.23]]), und die Geburt «aus dem Geist» ([[JHN.3.5]]–[[JHN.3.8]]) passt dazu. Das Deutsche hat kein Wort mit beiden Bedeutungen; die Übersetzung wählt «von oben» (Luther 1912: «von neuem»), redaktionelle Entscheidung. Ebenso [[JHN.3.7]]."),
 ("JHN.3.3", "das Reich Gottes", "traditional", "τὴν βασιλείαν τοῦ θεοῦ", None, ["die Herrschaft Gottes"],
  "Bei Johannes nur hier und in [[JHN.3.5]]; sonst spricht das Evangelium vom «ewigen Leben» (vgl. [[JHN.3.15]]–[[JHN.3.16]]). In [[JHN.18.36]] spricht Jesus von «meinem Reich»."),
 ("JHN.3.5", "aus Wasser und Geist", "literal", "ἐξ ὕδατος καὶ πνεύματος", None, None,
  "Gedeutet wird auf die Taufe, auf die natürliche Geburt (Wasser) und die geistliche, oder auf ein einziges Geschehen von Reinigung und Geistgabe wie in [[EZK.36.25]]–[[EZK.36.27]]. Die wörtliche Wiedergabe legt sich nicht fest."),
 ("JHN.3.8", "Der Wind", "interpretive", "τὸ πνεῦμα", None, ["Der Geist"],
  "πνεῦμα heisst «Wind, Hauch, Geist» (wie hebräisch rûaḥ). Der Vers spielt damit: Am Anfang passt «Wind» (er «weht», man hört ihn), am Schluss steht dasselbe Wort für den Geist. Das Deutsche muss sich entscheiden."),
 ("JHN.3.8", "Rauschen", "adapted", "φωνὴν", "Stimme", ["Sausen"],
  "φωνή heisst «Stimme, Laut»; beim Wind das Geräusch."),
 ("JHN.3.11", "Was wir wissen", "literal", "ὃ οἴδαμεν", None, None,
  "Mitten in der Rede an Nikodemus («ich sage dir») wechselt Jesus in die Mehrzahl («wir», «ihr»). Ob er sich mit seinen Jüngern zusammenschliesst, ob die Sprache der späteren Gemeinde durchscheint oder ob er das «wir wissen» des Nikodemus ([[JHN.3.2]]) aufnimmt, ist offen."),
 ("JHN.3.13", "hinaufgestiegen", "literal", "ἀναβέβηκεν", "ist hinaufgestiegen", None,
  "Perfekt. Der Satz kann aus dem Rückblick nach Ostern gesprochen sein oder allgemein sagen, dass niemand himmlisches Wissen von oben geholt hat ausser dem, der von dort kam."),
 ("JHN.3.14", "erhöht werden", "literal", "ὑψωθῆναι", None, ["emporgehoben werden"],
  "Grundentscheid: ὑψόω durchgehend «erhöhen» (nach MACULA-Lemma 5-mal im SBLGNT-Text). Das Wort hat bei Johannes einen Doppelsinn: das Aufrichten am Kreuz (vgl. [[JHN.12.32]]–[[JHN.12.33]]) und die Erhöhung zu Gott (vgl. [[ISA.52.13]], wo die Septuaginta dasselbe Verb hat). Das Bild nimmt [[NUM.21.8]]–[[NUM.21.9]] auf."),
 ("JHN.3.15", "in ihm ewiges Leben hat", "interpretive", "ἐν αὐτῷ ἔχῃ ζωὴν αἰώνιον", None, ["jeder, der an ihn glaubt, ewiges Leben hat"],
  "ἐν αὐτῷ kann zu «glaubt» gehören («an ihn glaubt») oder zu «hat» («in ihm Leben hat»). Weil Johannes «glauben an» sonst mit εἰς ausdrückt (so [[JHN.3.16]]), ist es hier zu «hat» gezogen; redaktionelle Entscheidung. «Ewiges Leben» ist das Leben der kommenden Weltzeit (vgl. [[DAN.12.2]]), bei Johannes schon jetzt geschenkt ([[JHN.3.36]]: «hat»)."),
 ("JHN.3.16", "Denn so hat Gott die Welt geliebt", "interpretive", "Οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον ὥστε", None, ["Denn so sehr hat Gott die Welt geliebt", "Denn auf diese Weise hat Gott die Welt geliebt"],
  "οὕτως kann das Mass («so sehr») oder die Art («auf diese Weise», nämlich durch das Geben des Sohnes, vgl. [[JHN.3.14]]) bezeichnen; das deutsche «so … dass» hält beides offen. Ob [[JHN.3.16]]–[[JHN.3.21]] noch Worte Jesu an Nikodemus sind oder eine Erläuterung des Evangelisten, sagt der Text nicht (das Griechische hat keine Anführungszeichen). Die Übersetzung lässt die Rede Jesu bis [[JHN.3.21]] laufen, weil kein Sprecherwechsel angezeigt ist; redaktionelle Entscheidung."),
 ("JHN.3.16", "gab", "literal", "ἔδωκεν", None, ["hingab", "gegeben hat"],
  "Gemeint sein kann die Sendung in die Welt ([[JHN.3.17]]) und die Hingabe in den Tod; der Text sagt einfach «gab»."),
 ("JHN.3.16", "verloren geht", "literal", "ἀπόληται", None, ["zugrunde geht"], None),
 ("JHN.3.17", "richtet", "interpretive", "κρίνῃ", None, ["verurteilt"],
  "κρίνω heisst «urteilen, richten», oft im Sinn von «verurteilen»; κρίσις ([[JHN.3.19]]) entsprechend «Gericht». Das Gericht ist bei Johannes schon gegenwärtig ([[JHN.3.18]])."),
 ("JHN.3.19", "die Finsternis", "literal", "τὸ σκότος", None, None,
  "Hier steht σκότος statt σκοτία ([[JHN.1.5]]); beides ist mit «Finsternis» wiedergegeben."),
 ("JHN.3.20", "Schlechtes", "interpretive", "φαῦλα", None, ["Böses", "Nichtiges"], None),
 ("JHN.3.20", "aufgedeckt werden", "interpretive", "ἐλεγχθῇ", None, ["überführt werden", "ans Licht kommen", "gerügt werden"], None),
 ("JHN.3.21", "die Wahrheit tut", "literal", "ποιῶν τὴν ἀλήθειαν", None, ["nach der Wahrheit handelt"],
  "Wahrheit ist hier etwas, das man tut (vgl. [[1JN.1.6]])."),
 ("JHN.3.25", "einem Juden", "literal", "Ἰουδαίου", None, ["den Juden"],
  "Einzahl im SBLGNT. Nach den CNTR-Transkriptionen lesen 01 und 𝔓66 (sowie KJTR und Stephanus) die Mehrzahl Ἰουδαίων; der SBLGNT-Apparat verzeichnet hier keine Variante."),
 ("JHN.3.29", "der Freund des Bräutigams", "literal", "ὁ φίλος τοῦ νυμφίου", None, ["der Brautführer", "der Trauzeuge"],
  "Der Freund des Bräutigams hatte bei der Hochzeit eine Aufgabe für den Bräutigam; Johannes vergleicht sich mit ihm."),
 ("JHN.3.29", "von Herzen", "adapted", "χαρᾷ χαίρει", "freut sich mit Freude", ["freut sich sehr"],
  "Verstärkende Doppelung nach hebräischem Sprachgebrauch."),
 ("JHN.3.30", "kleiner werden", "interpretive", "ἐλαττοῦσθαι", None, ["abnehmen", "geringer werden"], None),
 ("JHN.3.31", "Der von oben kommt", "interpretive", "Ὁ ἄνωθεν ἐρχόμενος", None, None,
  "ἄνωθεν wie in [[JHN.3.3]], hier eindeutig «von oben». Ob [[JHN.3.31]]–[[JHN.3.36]] noch Worte des Täufers sind oder eine Erläuterung des Evangelisten, sagt der Text nicht; die Übersetzung lässt die Rede des Täufers bis [[JHN.3.36]] laufen, weil kein Sprecherwechsel angezeigt ist (vgl. [[JHN.3.16]]); redaktionelle Entscheidung."),
 ("JHN.3.31", "Der vom Himmel kommt, ist über allen", "literal", "ὁ ἐκ τοῦ οὐρανοῦ ἐρχόμενος ἐπάνω πάντων ἐστίν", None, ["Der vom Himmel kommt"],
  "Nach den CNTR-Transkriptionen fehlt die zweite Wendung «ist über allen» in 01, 05 und 𝔓75; dort endet der Vers mit «Der vom Himmel kommt» und der Satz läuft in [[JHN.3.32]] weiter («… bezeugt, was er gesehen und gehört hat»). Der SBLGNT-Apparat verzeichnet keine Variante; der Text folgt den SBLGNT-Tokens. πάντων kann «allen» oder «allem» heissen."),
 ("JHN.3.33", "hat besiegelt", "interpretive", "ἐσφράγισεν", None, ["hat bestätigt", "hat bekräftigt"],
  "Wie mit einem Siegel bestätigt: Wer das Zeugnis annimmt, bestätigt damit Gottes Wahrhaftigkeit."),
 ("JHN.3.34", "er gibt den Geist nicht nach Mass", "interpretive", "οὐ ἐκ μέτρου δίδωσιν τὸ πνεῦμα", None, ["Gott gibt ihm den Geist ohne Mass", "er (der Gesandte) gibt den Geist ohne Mass"],
  "Das Subjekt ist offen: Gott gibt dem Gesandten den Geist ohne Mass, oder der Gesandte gibt ihn anderen. Zur Lesart mit ὁ θεός siehe Alternative."),
 ("JHN.3.36", "nicht gehorcht", "interpretive", "ἀπειθῶν", None, ["nicht glaubt", "sich widersetzt"],
  "ἀπειθέω heisst «nicht gehorchen, sich nicht überzeugen lassen». Als Gegenstück zu «glauben» zeigt es, dass Glauben hier auch Gehorsam einschliesst."),
 ("JHN.3.36", "der Zorn Gottes", "literal", "ἡ ὀργὴ τοῦ θεοῦ", None, None,
  "ὀργή kommt im Johannesevangelium nur hier vor (nach MACULA-Lemma). Der Zorn «bleibt» (μένει): Er ist nicht erst künftig, sondern liegt schon auf dem, der sich verweigert."),
]

DEC_GSW = [
 ("JHN.1.1", "s Wort", "literal", "λόγος", None, ["de Logos", "d Red"],
  "Grundentscheid fürs ganz Evangelium: λόγος heisst «Wort, Red», i de griechische Philosophie au «Vernunft». De Prolog knüpft a [[GEN.1.1]] aa («Im Aafang») und as Wort, wo Gott dur s erschafft ([[PSA.33.6]]). Als Titel staat s Wort nu im Prolog; susch heisst λόγος s gredt Wort und isch au «Wort» widergää. Bis [[JHN.1.5]] «es», ab [[JHN.1.10]] «er, ihn», wil de Text dört vo ere Person redt."),
 ("JHN.1.1", "s Wort isch Gott gsii", "interpretive", "θεὸς ἦν ὁ λόγος", "Gott isch s Wort gsii", ["s Wort isch göttlich gsii", "en Gott isch s Wort gsii"],
  "θεός staat voraa und ohni Artikel, ὁ λόγος mit Artikel isch s Subjekt. S Wort isch nöd eifach mit «em Gott» gliichgsetzt, bi däm es isch, aber es wird ihm zuegsproche, was Gott isch. «Göttlich» schwächt nach verbreitetem Urteil ab; «en Gott» vertreted nu einzelni Übersetzige. Redaktionelle Entscheid."),
 ("JHN.1.3", "Was worde isch", "interpretive", "ὃ γέγονεν", None, ["… und ohni es isch nüüt worde, was worde isch. In ihm isch Läbe gsii"],
  "Wo ὃ γέγονεν dezue ghört, isch e Frag vo de Satzzeiche. De SBLGNT setzt de Punkt devor und zieht d Wort zum Nächschte; RP, KJTR, Stephanus und SR zum Vorige. D Übersetzig folgt em SBLGNT."),
 ("JHN.1.4", "s Liecht vo de Mänsche", "literal", "τὸ φῶς τῶν ἀνθρώπων", None, None,
  "Grundentscheid: φῶς immer «Liecht», σκοτία und σκότος immer «Fiischteri» (wie i de Johannesbrief)."),
 ("JHN.1.5", "packt", "interpretive", "κατέλαβεν", None, ["überwältiget", "begriffe", "ufgnoo"],
  "καταλαμβάνω heisst «packe, überwältige», au «begriife». Im Züritüütsch cha «packe» beides heisse: öppis feschthebe und öppis kapiere («ich packs nöd»)."),
 ("JHN.1.7", "Zügnis gäb", "literal", "μαρτυρήσῃ", None, ["bezüüge"],
  "Grundentscheid: μαρτυρέω «Zügnis gää, bezüüge», μαρτυρία «Zügnis»."),
 ("JHN.1.9", "isch i d Wält choo", "interpretive", "ἦν ἐρχόμενον εἰς τὸν κόσμον", None, ["… wo jede Mänsch erlüüchtet, wo i d Wält chunnt"],
  "S Partizip ἐρχόμενον cha zum Liecht ghöre (so da) oder zu «jede Mänsch» (so Luther 1912)."),
 ("JHN.1.10", "Wält", "literal", "κόσμῳ", None, None,
  "Grundentscheid: κόσμος immer «Wält»: d Schöpfig, d Mänschheit, wo Gott liebt ([[JHN.3.16]]), oder d Mänschewält, wo sich Gott verschlüüsst."),
 ("JHN.1.14", "gwohnt", "adapted", "ἐσκήνωσεν", "zeltet", ["sis Zält ufgstellt"],
  "σκηνόω chunnt vo σκηνή «Zält»; vili ghöred en Aaklang as Zält vo de Begägnig ([[EXO.40.34]])."),
 ("JHN.1.14", "Herrlichkeit", "literal", "δόξαν", None, ["Glanz", "Ehr"],
  "Grundentscheid: δόξα immer «Herrlichkeit», δοξάζω «verherrliche». Nu wo s s Aasee bi de Mänsche meint ([[JHN.5.41]], [[JHN.5.44]], [[JHN.7.18]], [[JHN.8.50]], [[JHN.8.54]], [[JHN.9.24]], [[JHN.12.43]]), staat «Ehr», jedesmal mit eme eigete Entscheid."),
 ("JHN.1.14", "vom Einzige", "interpretive", "μονογενοῦς", "vo me einzig Gebore", ["vom iigebore Sohn"],
  "μονογενής heisst «einzig i sinere Art, einzigs Chind». «Sohn» staat da nöd im Text. Gliich i [[JHN.1.18]], [[JHN.3.16]], [[JHN.3.18]]."),
 ("JHN.1.16", "Gnad um Gnad", "interpretive", "χάριν ἀντὶ χάριτος", "Gnad statt Gnad", ["Gnad über Gnad"], None),
 ("JHN.1.18", "de Einzig, Gott,", "interpretive", "μονογενὴς θεὸς", "einzig gebore Gott", ["de einzig Sohn, wo Gott isch"],
  "De SBLGNT list μονογενὴς θεός (lueg d Alternative zur Läsart «de einzig Sohn»). D Kommas trenned di zwei Wort, demit nöd de Iidruck vo me zweite Gott näbem Vatter entstaat; redaktionelle Entscheid."),
 ("JHN.1.18", "hät Bricht gää", "interpretive", "ἐξηγήσατο", None, ["hät en uusgleit", "hät vo ihm verzellt"],
  "ἐξηγέομαι heisst «verzelle, uusleggä». Es Objekt fehlt; gmeint isch Gott, wo niemer gseh hät."),
 ("JHN.1.19", "d Jude", "interpretive", "οἱ Ἰουδαῖοι", None, ["di jüdische Behörde", "di jüdische Füerer"],
  "Grundentscheid (lueg translation_notes): οἱ Ἰουδαῖοι immer wörtlich «d Jude». Da sind offesichtlich d Behörde z Jerusalem gmeint; si schicked Prieschter und Levite."),
 ("JHN.1.23", "vom Herr", "literal", "κυρίου", None, None,
  "Zitat us [[ISA.40.3]]; im hebräische Text staat dört de Gottesname JHWH."),
 ("JHN.1.29", "s Lamm vo Gott", "literal", "ὁ ἀμνὸς τοῦ θεοῦ", None, None,
  "Mer dänkt as Passalamm ([[EXO.12.3]]; vgl. [[JHN.19.36]]), a de Gottesknächt wie es Lamm ([[ISA.53.7]]) oder as Lamm als Sieger ([[REV.5.6]]). De Text leit sich nöd fescht."),
 ("JHN.1.29", "wägnimmt", "interpretive", "αἴρων", None, ["treit"],
  "αἴρω heisst «ufhebe, träge, wägnää»; beides isch möglich."),
 ("JHN.1.32", "bliibe", "literal", "ἔμεινεν", None, None,
  "Grundentscheid: μένω immer «bliibe» (im SBLGNT-Text 40-mal)."),
 ("JHN.1.34", "de Userwählt vo Gott", "literal", "ὁ ἐκλεκτὸς τοῦ θεοῦ", None, ["de Sohn vo Gott"],
  "De SBLGNT list ἐκλεκτός; WH, Treg, NA28 und RP läsed υἱός «Sohn» (lueg d Alternative)."),
 ("JHN.1.38", "isch dini Bliibi", "adapted", "μένεις", "bliibsch", ["wohnsch"],
  "μένω heisst da «sich ufhalte, wohne». «Bliibi» bhaltet de Wortstamm vo «bliibe»."),
 ("JHN.1.39", "di zäät Stund", "literal", "ὥρα δεκάτη", None, ["vieri am Namittag"],
  "Vom Sunneufgang aa zellt öppe am vieri am Namittag; anderi zelled ab Mitternacht. Umstritte."),
 ("JHN.1.47", "nüüt Falschs", "interpretive", "δόλος οὐκ", "kei List", ["kei Betrug"],
  "Vili gsehnd es Wortspiel mit em Jakob-Israel, wo sim Vatter «mit List» de Säge gnoo hät ([[GEN.27.35]])."),
 ("JHN.1.51", "Amen, amen, ich säge eu", "literal", "Ἀμὴν ἀμὴν λέγω ὑμῖν", None, ["Würkli, würkli, ich säge eu"],
  "Grundentscheid: S doppelt ἀμήν bliibt «Amen, amen» (im SBLGNT-Text 25-mal; i de Evangelie nu bim Johannes doppelt)."),
 ("JHN.1.51", "de Mänschesohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None,
  "S Bild nimmt de Traum vom Jakob uf ([[GEN.28.12]])."),
 ("JHN.2.4", "Was han ich mit dir z tue, Frau?", "interpretive", "Τί ἐμοὶ καὶ σοί, γύναι", "Was mir und dir, Frau?", ["Was gaat das di und mich aa, Frau?"],
  "Hebräisch prägti Wändig (vgl. [[JDG.11.12]]) für Abstand oder Abwehr. «Frau» isch kei unhöflichi Aared; so redt de Jesus au am Chrüüz sini Mueter aa ([[JHN.19.26]])."),
 ("JHN.2.4", "Mini Stund", "literal", "ἡ ὥρα μου", None, None,
  "D «Stund» vom Jesus isch d Ziit vo sim Tod und sinere Verherrlichung ([[JHN.12.23]])."),
 ("JHN.2.6", "Metrete", "literal", "μετρητὰς", None, None,
  "En Metretes isch öppe 39 Liter gsii; zäme also rund 470 bis 700 Liter."),
 ("JHN.2.11", "Aafang vo de Zeiche", "literal", "ἀρχὴν τῶν σημείων", None, ["s erscht vo de Zeiche"],
  "Grundentscheid: σημεῖον immer «Zeiche», nöd «Wunder». D Tate vom Jesus wiised über sich use uf sini Herrlichkeit."),
 ("JHN.2.19", "Riissed dä Tämpel ab", "interpretive", "Λύσατε τὸν ναὸν τοῦτον", None, ["Wänn ir dä Tämpel abriissed"],
  "Imperativ mit Bedingigs-Sinn: kei Uftrag, sondern «wänn ir …»."),
 ("JHN.2.19", "stell ich en uf", "interpretive", "ἐγερῶ αὐτόν", None, ["weck ich en uf"],
  "ἐγείρω heisst «ufstelle, ufrichte» bi Hüüser und «uferwecke» bi Tote ([[JHN.2.22]]). S Missverständnis läbt vo dem Doppelsinn."),
 ("JHN.2.20", "wottsch", "adapted", "ἐγερεῖς", "wirsch … ufstelle", None,
  "Futur; i de Mundart als ungläubigi Frag mit «wotte»."),
 ("JHN.3.3", "vo obe", "interpretive", "ἄνωθεν", None, ["vo neuem", "nomal"],
  "ἄνωθεν heisst «vo obe» und «vo neuem». De Nikodemus verstaat «es zweits Mal» ([[JHN.3.4]]); bim Johannes heisst s Wort susch «vo obe» ([[JHN.3.31]], [[JHN.19.11]]). Redaktionelle Entscheid. Gliich i [[JHN.3.7]]."),
 ("JHN.3.8", "De Wind", "interpretive", "τὸ πνεῦμα", None, ["De Geischt"],
  "πνεῦμα heisst «Wind, Hauch, Geischt». De Vers spilt demit: am Aafang «Wind», am Schluss «Geischt»."),
 ("JHN.3.14", "erhöcht wärde", "literal", "ὑψωθῆναι", None, ["ufeghebt wärde"],
  "Grundentscheid: ὑψόω immer «erhöche». Doppelsinn: am Chrüüz ufgrichtet und zu Gott erhöcht ([[JHN.12.32]]–[[JHN.12.33]]). S Bild nimmt [[NUM.21.8]]–[[NUM.21.9]] uf."),
 ("JHN.3.16", "Dänn so hät Gott d Wält gliebt", "interpretive", "Οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον ὥστε", None, ["Dänn so fescht hät Gott d Wält gliebt"],
  "οὕτως cha s Mass («so fescht») oder d Art («uf die Wiis») meine. Öb [[JHN.3.16]]–[[JHN.3.21]] no de Jesus redt oder de Evangelischt erklärt, seit de Text nöd; d Übersetzig laat d Red vom Jesus bis [[JHN.3.21]] laufe. Redaktionelle Entscheid."),
 ("JHN.3.31", "Dä, wo vo obe chunnt", "interpretive", "Ὁ ἄνωθεν ἐρχόμενος", None, None,
  "Öb [[JHN.3.31]]–[[JHN.3.36]] no de Täufer redt oder de Evangelischt, seit de Text nöd; d Übersetzig laat d Red vom Täufer bis [[JHN.3.36]] laufe. Nach de CNTR-Transkriptione fehlt s zweit «isch über allne» in 01, 05 und 𝔓75."),
 ("JHN.3.33", "hät bsiglet", "interpretive", "ἐσφράγισεν", None, ["hät bestätiget"], None),
 ("JHN.3.34", "er git de Geischt nöd nach Mass", "interpretive", "οὐ ἐκ μέτρου δίδωσιν τὸ πνεῦμα", None, ["Gott git ihm de Geischt ohni Mass"],
  "S Subjekt isch offe: Gott git em Gschickte de Geischt, oder de Gschickt git en andere. Lueg d Alternative."),
 ("JHN.3.36", "nöd folget", "interpretive", "ἀπειθῶν", None, ["nöd glaubt"],
  "ἀπειθέω heisst «nöd folge, sich nöd überzüüge laa»."),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-JHN-001-015-01:R2", "JHN.1.15", "Dieser war es, von dem ich sagte", "Dieser war es, der sagte",
  "Dä isch es gsii, vo däm ich gseit han", "Dä isch es gsii, wo gseit hät", "gering",
  "Mit ὁ εἰπών («der sagte») meint «dieser» Johannes selbst: Er ist es, der das Wort gesprochen hat.",
  "Mit ὁ εἰπών («wo gseit hät») meint «dä» de Johannes sälber: Er hät das Wort gseit.",
  {"R1": [("ὃν εἶπον", "von dem ich sagte", "Treg, NA28, RP")], "R2": [("ὁ εἰπών", "der (es) sagte", "WH")]},
  {"R1": [("ὃν εἶπον", "vo däm ich gseit han", "Treg, NA28, RP")], "R2": [("ὁ εἰπών", "wo s gseit hät", "WH")]},
  ["ὁ εἰπών ist die schwierigere Lesart; ὃν εἶπον glättet den Satz und entspricht [[JHN.1.30]]. Ebenso kann ὁ εἰπών aus einem Schreibversehen entstanden sein.",
   "Laut der automatischen Zuordnung lesen 02, 05, 032, 𝔓66 und 𝔓75 ὃν εἶπον, 03 und 04 ὁ εἰπών. Die Erstschrift von 01 hat die Worte nicht; nach der CNTR-Transkription ergänzen Korrekturen ὁ εἰπών bzw. ον ειπων (von der Zuordnung bei ὃν εἶπον geführt)."],
  ["ὁ εἰπών isch di schwierigeri Läsart; ὃν εἶπον macht de Satz glatter und entspricht [[JHN.1.30]]. ὁ εἰπών cha aber au us eme Schriibfähler entstande sii.",
   "Nach de automatische Zueornig läsed 02, 05, 032, 𝔓66 und 𝔓75 ὃν εἶπον, 03 und 04 ὁ εἰπών. D Erschtschrift vo 01 hät d Wort nöd; nach de CNTR-Transkription ergänzed Korrekture ὁ εἰπών oder ον ειπων."]),
 ("VAR-SBLGNTAPP-JHN-001-018-01:R2", "JHN.1.18", "der Einzige, Gott,", "der einzige Sohn,", "de Einzig, Gott,", "de einzig Sohn,", "erheblich",
  "Statt «Gott» steht «Sohn»; der Satz nennt den Einzigen dann nicht ausdrücklich Gott.",
  "Statt «Gott» staat «Sohn»; de Satz nännt de Einzig dänn nöd usdrücklich Gott.",
  {"R1": [("μονογενὴς θεός", "der Einzige, Gott", "WH, Treg, NA28")], "R2": [("ὁ μονογενὴς υἱός", "der einzige Sohn", "RP")]},
  {"R1": [("μονογενὴς θεός", "de Einzig, Gott", "WH, Treg, NA28")], "R2": [("ὁ μονογενὴς υἱός", "de einzig Sohn", "RP")]},
  ["«Sohn» entspricht der geläufigen Verbindung «der einzige Sohn» ([[JHN.3.16]], [[JHN.3.18]], [[1JN.4.9]]); Abschreiber könnten die ungewöhnliche Wendung daran angeglichen haben. Andere halten «Gott» für eine spätere Verdeutlichung im Sinn der Lehre von der Gottheit Christi. In den Handschriften stehen θεός und υἱός als Kürzel (ΘΣ, ΥΣ), die sich in einem Buchstaben unterscheiden.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 𝔓66 und 𝔓75 θεός (𝔓75 mit Artikel: ὁ μονογενὴς θεός), 02 und 032 υἱός; 032 hat nach der CNTR-Transkription ausserdem εἰ μή («ausser») davor und ἡμῖν («uns») am Schluss."],
  ["«Sohn» entspricht de gwohnte Verbindig «de einzig Sohn» ([[JHN.3.16]], [[JHN.3.18]], [[1JN.4.9]]); Abschriiber chönnted di ungwöhnlich Wändig dra aaglichen ha. Anderi halted «Gott» für e spööteri Verdüütlichung im Sinn vo de Lehr vo de Gottheit vo Christus. I de Handschrifte stönd θεός und υἱός als Chürzel (ΘΣ, ΥΣ), wo sich i eim Buechstabe underscheided.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 𝔓66 und 𝔓75 θεός (𝔓75 mit Artikel), 02 und 032 υἱός."]),
 ("VAR-SBLGNTAPP-JHN-001-027-02:R2", "JHN.1.27", "der nach mir kommt;", "der nach mir kommt, der mir voraus ist;",
  "dä, wo nach mir chunnt;", "dä, wo nach mir chunnt, wo mir voraus isch;", "gering",
  "Der Zusatz wiederholt die Aussage von [[JHN.1.15]] und [[JHN.1.30]].", "De Zuesatz widerholt d Ussag vo [[JHN.1.15]] und [[JHN.1.30]].",
  {"R1": [("ἐρχόμενος", "kommt", "WH, Treg, NA28")], "R2": [("ἐρχόμενος, ὃς ἔμπροσθέν μου γέγονεν", "kommt, der mir voraus ist", "RP")]},
  {"R1": [("ἐρχόμενος", "chunnt", "WH, Treg, NA28")], "R2": [("ἐρχόμενος, ὃς ἔμπροσθέν μου γέγονεν", "chunnt, wo mir voraus isch", "RP")]},
  ["Der Zusatz kann aus [[JHN.1.15]] und [[JHN.1.30]] übernommen sein; ebenso könnte er beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 029, 032, 𝔓5, 𝔓66, 𝔓75, 𝔓119 und 𝔓120 ohne Zusatz, 02 mit ihm."],
  ["De Zuesatz cha us [[JHN.1.15]] und [[JHN.1.30]] übernoo sii; er chönnt aber au bim Abschriibe usgfalle sii.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 029, 032, 𝔓5, 𝔓66, 𝔓75, 𝔓119 und 𝔓120 ohni Zuesatz, 02 mit."]),
 ("VAR-SBLGNTAPP-JHN-001-034-01:R2", "JHN.1.34", "der Erwählte Gottes", "der Sohn Gottes", "de Userwählt vo Gott", "de Sohn vo Gott", "mittel",
  "Johannes bezeugt Jesus als «Sohn Gottes» statt als «Erwählten Gottes».", "De Johannes bezüügt de Jesus als «Sohn vo Gott» statt als «Userwählte vo Gott».",
  {"R1": [("ἐκλεκτός", "der Erwählte", "Holmes, WHmarg")], "R2": [("υἱός", "der Sohn", "WH, Treg, NA28, RP")]},
  {"R1": [("ἐκλεκτός", "de Userwählt", "Holmes, WHmarg")], "R2": [("υἱός", "de Sohn", "WH, Treg, NA28, RP")]},
  ["«Der Erwählte» klingt an den Gottesknecht in [[ISA.42.1]] an; «Sohn Gottes» ist im Evangelium geläufig (vgl. [[JHN.1.49]]) und kann an seine Stelle getreten sein. Ebenso kann «der Erwählte» eine Angleichung an [[ISA.42.1]] oder [[LUK.23.35]] sein. Der SBLGNT folgt hier Holmes und der Randlesart von WH, gegen den Text von WH, Treg, NA28 und RP.",
   "Laut der automatischen Zuordnung lesen 01, 𝔓5 und 𝔓106 ἐκλεκτός, 02, 03 und 𝔓120 υἱός. 04, 032, 𝔓66 und 𝔓75 hat die Zuordnung keiner Lesart zugewiesen; nach den CNTR-Transkriptionen steht dort ebenfalls υἱός (als Kürzel)."],
  ["«De Userwählt» klingt a de Gottesknächt i [[ISA.42.1]] aa; «Sohn vo Gott» isch im Evangelium gläufig (vgl. [[JHN.1.49]]) und cha a sini Stell trätte sii. Gliich guet cha «de Userwählt» e Aagliichig a [[ISA.42.1]] oder [[LUK.23.35]] sii.",
   "Nach de automatische Zueornig läsed 01, 𝔓5 und 𝔓106 ἐκλεκτός, 02, 03 und 𝔓120 υἱός; nach de CNTR-Transkriptione au 04, 032, 𝔓66 und 𝔓75."]),
 ("VAR-SBLGNTAPP-JHN-001-041-01:R2", "JHN.1.41", "Er findet zuerst", "Er findet als Erster", "Dä findt zerscht", "Dä findt als Erschte", "gering",
  "Mit πρῶτος ist Andreas der Erste, der seinen Bruder findet; das kann andeuten, dass auch der andere Jünger danach jemanden fand.",
  "Mit πρῶτος isch de Andreas de Erscht, wo sin Brüeder findt; das cha aadüüte, dass au de ander Jünger nachher öpper gfunde hät.",
  {"R1": [("πρῶτον", "zuerst", "WH, Treg, NA28")], "R2": [("πρῶτος", "als Erster", "RP")]},
  {"R1": [("πρῶτον", "zerscht", "WH, Treg, NA28")], "R2": [("πρῶτος", "als Erschte", "RP")]},
  ["Die Formen unterscheiden sich nur im letzten Buchstaben und können beim Abschreiben leicht verwechselt werden.",
   "Laut der automatischen Zuordnung lesen 02, 03, 𝔓66, 𝔓75, 𝔓106 und 𝔓119 πρῶτον, 01 und 032 πρῶτος."],
  ["Di zwei Forme underscheided sich nu im letschte Buechstabe und sind bim Abschriibe liecht z verwächsle.",
   "Nach de automatische Zueornig läsed 02, 03, 𝔓66, 𝔓75, 𝔓106 und 𝔓119 πρῶτον, 01 und 032 πρῶτος."]),
 ("VAR-SBLGNTAPP-JHN-001-042-02:R2", "JHN.1.42", "der Sohn des Johannes", "der Sohn des Jona", "de Sohn vom Johannes", "de Sohn vom Jona", "gering",
  "Der Vater des Simon heisst Jona statt Johannes.", "De Vatter vom Simon heisst Jona statt Johannes.",
  {"R1": [("Ἰωάννου", "des Johannes", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ", "des Jona", "RP")]},
  {"R1": [("Ἰωάννου", "vom Johannes", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ", "vom Jona", "RP")]},
  ["«Jona» entspricht [[MAT.16.17]] (Simon Bar-Jona); Abschreiber haben Paralleltexte oft angeglichen. Ob «Jona» eine Kurzform von «Johannes» sein kann, wird diskutiert.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 𝔓66, 𝔓75, 𝔓106 und 𝔓119 Ἰωάννου, 02 Ἰωνᾶ."],
  ["«Jona» entspricht [[MAT.16.17]] (Simon Bar-Jona); Abschriiber händ Paralleltext oft aaglichen.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 𝔓66, 𝔓75, 𝔓106 und 𝔓119 Ἰωάννου, 02 Ἰωνᾶ."]),
 ("VAR-SBLGNTAPP-JHN-001-051-01:R2", "JHN.1.51", "Ihr werdet den Himmel", "Von nun an werdet ihr den Himmel", "Ir wärded de Himmel", "Vo jetzt aa wärded ir de Himmel", "gering",
  "Mit ἀπʼ ἄρτι («von nun an») beginnt das Sehen schon jetzt.", "Mit ἀπʼ ἄρτι («vo jetzt aa») faat s Gseh scho jetzt aa.",
  {"R1": [("ὑμῖν", "euch", "WH, Treg, NA28")], "R2": [("ὑμῖν ἀπʼ ἄρτι", "euch: Von nun an", "RP")]},
  {"R1": [("ὑμῖν", "eu", "WH, Treg, NA28")], "R2": [("ὑμῖν ἀπʼ ἄρτι", "eu: Vo jetzt aa", "RP")]},
  ["Die Wendung steht in [[MAT.26.64]] und kann von dort übernommen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 𝔓66, 𝔓75 und 𝔓134 ohne Zusatz, 02 mit ihm."],
  ["D Wändig staat i [[MAT.26.64]] und cha vo dört übernoo sii.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 𝔓66, 𝔓75 und 𝔓134 ohni Zuesatz, 02 mit."]),
 ("VAR-SBLGNTAPP-JHN-003-013-01:R2", "JHN.3.13", "dem Menschensohn.", "dem Menschensohn, der im Himmel ist.", "de Mänschesohn.", "de Mänschesohn, wo im Himmel isch.", "mittel",
  "Der Zusatz sagt, dass der Menschensohn zugleich im Himmel ist.", "De Zuesatz seit, dass de Mänschesohn gliichziitig im Himmel isch.",
  {"R1": [("ἀνθρώπου", "Menschensohn", "WH, NA28")], "R2": [("ἀνθρώπου ὁ ὢν ἐν τῷ οὐρανῷ", "Menschensohn, der im Himmel ist", "Treg, RP")]},
  {"R1": [("ἀνθρώπου", "Mänschesohn", "WH, NA28")], "R2": [("ἀνθρώπου ὁ ὢν ἐν τῷ οὐρανῷ", "Mänschesohn, wo im Himmel isch", "Treg, RP")]},
  ["Der Zusatz kann eine erklärende Ergänzung aus späterer Glaubenssicht sein; ebenso kann die schwierige Aussage (der Sprechende ist zugleich im Himmel) beim Abschreiben weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 𝔓66 ohne Zusatz. Nach den CNTR-Transkriptionen fehlt er auch in 029, 032 und 𝔓75; 02 hat ὁ ἐν τῷ οὐρανῷ, von einer Korrektur zu ὁ ὢν ἐν τῷ οὐρανῷ ergänzt."],
  ["De Zuesatz cha e erklärendi Ergänzig us spööterer Glaubessicht sii; oder di schwirig Ussag isch bim Abschriibe wäggloo worde.",
   "Nach de automatische Zueornig läsed 01, 03 und 𝔓66 ohni Zuesatz; nach de CNTR-Transkriptione au 029, 032 und 𝔓75. 02 hät ὁ ἐν τῷ οὐρανῷ, vo ere Korrektur ergänzt."]),
 ("VAR-SBLGNTAPP-JHN-003-015-01:R2", "JHN.3.15", "jeder, der glaubt, in ihm ewiges Leben hat", "jeder, der an ihn glaubt, nicht verloren geht, sondern ewiges Leben hat",
  "jede, wo glaubt, in ihm ewigs Läbe hät", "jede, wo a ihn glaubt, nöd verlore gaat, sondern ewigs Läbe hät", "gering",
  "Der Vers lautet dann wie die zweite Hälfte von [[JHN.3.16]].", "De Vers luutet dänn wie di zweit Hälfti vo [[JHN.3.16]].",
  {"R1": [("ἐν αὐτῷ", "in ihm", "WH, Treg, NA28")], "R2": [("εἰς αὐτὸν μὴ ἀπόληται ἀλλʼ", "an ihn … nicht verloren geht, sondern", "RP")]},
  {"R1": [("ἐν αὐτῷ", "in ihm", "WH, Treg, NA28")], "R2": [("εἰς αὐτὸν μὴ ἀπόληται ἀλλʼ", "a ihn … nöd verlore gaat, sondern", "RP")]},
  ["Angleichung an [[JHN.3.16]] liegt nahe; auch εἰς αὐτόν entspricht dem üblichen johanneischen «glauben an».",
   "Laut der automatischen Zuordnung lesen 03, 029, 032 und 𝔓75 ἐν αὐτῷ. Nach den CNTR-Transkriptionen hat 01 εἰς αὐτόν (ohne «nicht verloren geht»), 02 ἐπʼ αὐτόν μὴ ἀπόληται ἀλλʼ, 𝔓66 ἐπʼ αὐτῷ."],
  ["Aagliichig a [[JHN.3.16]] liit nöch.",
   "Nach de automatische Zueornig läsed 03, 029, 032 und 𝔓75 ἐν αὐτῷ; nach de CNTR-Transkriptione hät 01 εἰς αὐτόν, 02 ἐπʼ αὐτόν μὴ ἀπόληται ἀλλʼ, 𝔓66 ἐπʼ αὐτῷ."]),
 ("VAR-SBLGNTAPP-JHN-003-016-01:R2", "JHN.3.16", "den einzigen Sohn", "seinen einzigen Sohn", "de einzig Sohn", "sin einzige Sohn", "gering",
  "Mit αὐτοῦ heisst es ausdrücklich «seinen» Sohn.", "Mit αὐτοῦ heisst s usdrücklich «sin» Sohn.",
  {"R1": [("υἱόν", "den Sohn", "WH, NA28")], "R2": [("υἱὸν αὐτοῦ", "seinen Sohn", "Treg, RP")]},
  {"R1": [("υἱόν", "de Sohn", "WH, NA28")], "R2": [("υἱὸν αὐτοῦ", "sin Sohn", "Treg, RP")]},
  ["Das Fürwort kann verdeutlichend ergänzt worden sein, wie es in [[1JN.4.9]] steht («seinen einzigen Sohn»).",
   "Laut der automatischen Zuordnung lesen 03 und 𝔓75 ohne αὐτοῦ, 02 und 029 mit ihm. 01, 032 und 𝔓66 hat die Zuordnung keiner Lesart zugewiesen; nach den CNTR-Transkriptionen steht dort kein αὐτοῦ."],
  ["S Fürwort cha zur Verdüütlichung ergänzt worde sii, wie s i [[1JN.4.9]] staat.",
   "Nach de automatische Zueornig läsed 03 und 𝔓75 ohni αὐτοῦ, 02 und 029 mit; nach de CNTR-Transkriptione au 01, 032 und 𝔓66 ohni."]),
 ("VAR-SBLGNTAPP-JHN-003-034-01:R2", "JHN.3.34", "denn er gibt den Geist", "denn Gott gibt den Geist", "dänn er git de Geischt", "dänn Gott git de Geischt", "mittel",
  "Der Zusatz legt fest, dass Gott der Gebende ist; ohne ihn kann auch der Gesandte gemeint sein.",
  "De Zuesatz leit fescht, dass Gott de Gäber isch; ohni en cha au de Gschickt gmeint sii.",
  {"R1": [("δίδωσιν", "er gibt", "WH, NA28")], "R2": [("δίδωσιν ὁ θεός", "Gott gibt", "Treg, RP")]},
  {"R1": [("δίδωσιν", "er git", "WH, NA28")], "R2": [("δίδωσιν ὁ θεός", "Gott git", "Treg, RP")]},
  ["Der Zusatz kann den offenen Bezug klären; ebenso denkbar ist, dass ὁ θεός wegfiel, weil es kurz zuvor schon steht.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 032, 𝔓66 und 𝔓75 ohne Zusatz (bei 03 und 𝔓66 auch die Korrekturen), 02 und 05 mit ihm."],
  ["De Zuesatz cha de offe Bezug kläre; oder ὁ θεός isch usgfalle, wil s churz vorher scho staat.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 032, 𝔓66 und 𝔓75 ohni Zuesatz, 02 und 05 mit."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-JHN-001-001-051", "JHN.1.1-JHN.1.51", "section", "Das Wort, das Zeugnis des Johannes und die ersten Jünger",
  ["TU-JHN-001-001-018", "TU-JHN-001-019-028", "TU-JHN-001-029-034", "TU-JHN-001-035-042", "TU-JHN-001-043-051"],
  "Der Prolog spricht vom Wort, das im Anfang bei Gott war und Gott war, durch das alles geworden ist und das Fleisch wurde; Johannes ist gesandt, vom Licht Zeugnis abzulegen. Vor Priestern und Leviten aus Jerusalem bestreitet Johannes, der Christus, Elija oder der Prophet zu sein, und nennt sich die Stimme aus [[ISA.40.3]]. Er bezeichnet Jesus als das Lamm Gottes und bezeugt, den Geist auf ihn herabkommen gesehen zu haben. Zwei seiner Jünger folgen Jesus; Andreas bringt seinen Bruder Simon, und Jesus sagt ihm, er werde Kephas heissen. Jesus ruft Philippus; Natanaël bekennt ihn als Sohn Gottes und König Israels, und Jesus kündigt an, sie würden den Himmel geöffnet sehen.", SEG),
 ("TU-JHN-001-001-018", "JHN.1.1-JHN.1.18", "discourse", "Der Prolog: Das Wort wurde Fleisch", None,
  "Im Anfang war das Wort bei Gott, und das Wort war Gott; durch es ist alles geworden, in ihm war Leben, das Licht der Menschen, das in der Finsternis scheint. Johannes ist gesandt, um vom Licht Zeugnis abzulegen. Das wahre Licht kommt in die Welt; er kommt in sein Eigentum, doch die Seinen nehmen ihn nicht auf; allen, die ihn aufnehmen, gibt er Vollmacht, Kinder Gottes zu werden. Das Wort wurde Fleisch und wohnte unter uns, voller Gnade und Wahrheit. Niemand hat Gott je gesehen; der Einzige, Gott, der an der Brust des Vaters ist, hat Kunde gebracht.", None),
 ("TU-JHN-001-019-028", "JHN.1.19-JHN.1.28", "dialogue", "Das Zeugnis des Johannes vor den Abgesandten", None,
  "Priester und Leviten, von den Juden aus Jerusalem gesandt, fragen Johannes, wer er sei. Er bekennt, nicht der Christus zu sein, auch nicht Elija oder der Prophet, sondern die Stimme eines Rufenden in der Wüste ([[ISA.40.3]]). Auf die Frage, warum er dann taufe, verweist er auf einen, den sie nicht kennen, der mitten unter ihnen steht und nach ihm kommt. Das geschieht in Betanien jenseits des Jordan.", None),
 ("TU-JHN-001-029-034", "JHN.1.29-JHN.1.34", "narrative_with_saying", "Das Lamm Gottes", None,
  "Am folgenden Tag sieht Johannes Jesus kommen und nennt ihn das Lamm Gottes, das die Sünde der Welt wegnimmt. Er bezeugt, den Geist wie eine Taube herabkommen und auf ihm bleiben gesehen zu haben; daran sollte er, wie ihm der sagte, der ihn zu taufen gesandt hat, den erkennen, der mit heiligem Geist tauft. Er bezeugt: Dieser ist der Erwählte Gottes.", None),
 ("TU-JHN-001-035-042", "JHN.1.35-JHN.1.42", "narrative", "Die ersten Jünger", None,
  "Zwei Jünger des Johannes hören ihn Jesus das Lamm Gottes nennen und folgen Jesus. Auf seine Frage, was sie suchen, fragen sie nach seiner Bleibe und bleiben jenen Tag bei ihm. Einer von ihnen, Andreas, sagt seinem Bruder Simon, sie hätten den Messias gefunden, und führt ihn zu Jesus; Jesus sagt ihm, er werde Kephas heissen.", None),
 ("TU-JHN-001-043-051", "JHN.1.43-JHN.1.51", "dialogue", "Philippus und Natanaël", None,
  "Jesus ruft Philippus in die Nachfolge. Philippus sagt Natanaël, sie hätten den gefunden, von dem Mose und die Propheten geschrieben haben, Jesus aus Nazaret. Natanaël zweifelt, kommt aber mit; Jesus nennt ihn einen wahrhaftigen Israeliten ohne Falschheit und sagt, er habe ihn unter dem Feigenbaum gesehen; Natanaël bekennt ihn als Sohn Gottes und König Israels. Jesus kündigt Grösseres an: Sie werden den Himmel geöffnet sehen und die Engel Gottes auf- und absteigen auf den Menschensohn.", None),
 ("TU-JHN-002-001-025", "JHN.2.1-JHN.2.25", "section", "Kana und der Tempel in Jerusalem",
  ["TU-JHN-002-001-012", "TU-JHN-002-013-022", "TU-JHN-002-023-025"],
  "Auf einer Hochzeit in Kana wird das Wasser, das die Diener auf Jesu Anweisung schöpfen, zu Wein; das ist der Anfang der Zeichen, Jesus offenbart seine Herrlichkeit, und seine Jünger glauben an ihn. Vor dem Passa treibt Jesus die Händler und Geldwechsler aus dem Tempel in Jerusalem. Nach einem Zeichen gefragt, spricht er vom Niederreissen und Aufrichten des Tempels in drei Tagen; der Evangelist erklärt, er habe vom Tempel seines Leibes gesprochen. Viele glauben wegen der Zeichen an ihn, doch Jesus vertraut sich ihnen nicht an, weil er erkennt, was im Menschen ist.", SEG),
 ("TU-JHN-002-001-012", "JHN.2.1-JHN.2.12", "narrative", "Die Hochzeit in Kana", None,
  "Auf einer Hochzeit in Kana geht der Wein aus. Jesu Mutter sagt es ihm; er antwortet, seine Stunde sei noch nicht gekommen, doch sie weist die Diener an, zu tun, was er sagt. Auf Jesu Anweisung füllen die Diener sechs steinerne Krüge mit Wasser und bringen davon dem Speisemeister; das Wasser ist zu Wein geworden, und der Speisemeister sagt zum Bräutigam, er habe den guten Wein bis jetzt aufbewahrt. Damit macht Jesus den Anfang der Zeichen und offenbart seine Herrlichkeit; seine Jünger glauben an ihn. Danach zieht er mit Mutter, Brüdern und Jüngern für wenige Tage nach Kafarnaum.", None),
 ("TU-JHN-002-013-022", "JHN.2.13-JHN.2.22", "narrative", "Die Tempelreinigung", None,
  "Vor dem Passa treibt Jesus im Tempel in Jerusalem mit einer Geissel alle samt Schafen und Rindern hinaus, schüttet das Geld der Wechsler aus und verbietet, das Haus seines Vaters zu einem Haus des Handels zu machen; die Jünger erinnern sich an [[PSA.69.9]]. Die Juden fragen nach einem Zeichen. Jesus antwortet: «Reisst diesen Tempel nieder, und in drei Tagen werde ich ihn aufrichten.» Sie wenden ein, an diesem Tempel sei sechsundvierzig Jahre gebaut worden; er aber spricht, so der Erzähler, vom Tempel seines Leibes, und nach seiner Auferweckung erinnern sich die Jünger an dieses Wort.", None),
 ("TU-JHN-002-023-025", "JHN.2.23-JHN.2.25", "narrative", "Glaube wegen der Zeichen", None,
  "Am Passafest in Jerusalem glauben viele an seinen Namen, weil sie seine Zeichen sehen. Jesus aber vertraut sich ihnen nicht an, denn er kennt alle und erkennt selbst, was im Menschen ist.", None),
 ("TU-JHN-003-001-036", "JHN.3.1-JHN.3.36", "section", "Nikodemus und das letzte Zeugnis des Täufers",
  ["TU-JHN-003-001-015", "TU-JHN-003-016-021", "TU-JHN-003-022-030", "TU-JHN-003-031-036"],
  "Nikodemus, ein Pharisäer und Oberster der Juden, kommt bei Nacht zu Jesus. Jesus sagt ihm, wer nicht von oben, aus Wasser und Geist geboren werde, könne das Reich Gottes nicht sehen und nicht hineinkommen; Nikodemus versteht es nicht. Jesus spricht vom Menschensohn, der erhöht werden muss wie die Schlange in der Wüste, und davon, dass Gott die Welt so geliebt hat, dass er den einzigen Sohn gab; das Gericht besteht darin, dass Menschen die Finsternis mehr liebten als das Licht. Jesus tauft in Judäa, Johannes in Änon. Als seine Jünger ihm melden, dass alle zu Jesus kommen, vergleicht sich Johannes mit dem Freund des Bräutigams: Jener muss wachsen, er selbst kleiner werden. Wer vom Himmel kommt, ist über allen; wer an den Sohn glaubt, hat ewiges Leben. Ob [[JHN.3.16]]–[[JHN.3.21]] und [[JHN.3.31]]–[[JHN.3.36]] noch zu den Reden Jesu bzw. des Täufers gehören oder Erläuterung des Evangelisten sind, lässt der Text offen.", SEG),
 ("TU-JHN-003-001-015", "JHN.3.1-JHN.3.15", "dialogue", "Jesus und Nikodemus", None,
  "Nikodemus kommt bei Nacht und erkennt Jesus als einen von Gott gekommenen Lehrer an, weil niemand seine Zeichen tun könne, wenn Gott nicht mit ihm sei. Jesus antwortet, wer nicht von oben geboren werde, könne das Reich Gottes nicht sehen. Nikodemus fragt, ob ein Mensch ein zweites Mal in den Leib seiner Mutter gehen könne; Jesus spricht von der Geburt aus Wasser und Geist und vergleicht den Geist mit dem Wind. Er fragt, ob der Lehrer Israels das nicht verstehe, und spricht vom Menschensohn, der vom Himmel herabgestiegen ist und erhöht werden muss wie die Schlange in der Wüste, damit jeder, der glaubt, in ihm ewiges Leben hat.", None),
 ("TU-JHN-003-016-021", "JHN.3.16-JHN.3.21", "discourse", "So hat Gott die Welt geliebt", None,
  "Gott hat die Welt so geliebt, dass er den einzigen Sohn gab, damit jeder, der an ihn glaubt, nicht verloren geht, sondern ewiges Leben hat; er hat ihn nicht gesandt, die Welt zu richten, sondern damit sie gerettet wird. Wer nicht glaubt, ist schon gerichtet. Das Gericht besteht darin, dass das Licht in die Welt gekommen ist und die Menschen die Finsternis mehr liebten als das Licht: Wer Schlechtes tut, kommt nicht zum Licht, wer die Wahrheit tut, kommt zum Licht. Ob die Verse noch zur Rede Jesu an Nikodemus gehören oder Erläuterung des Evangelisten sind, lässt der Text offen.", None),
 ("TU-JHN-003-022-030", "JHN.3.22-JHN.3.30", "dialogue", "Der Freund des Bräutigams", None,
  "Jesus hält sich mit seinen Jüngern in Judäa auf und tauft; auch Johannes tauft noch, in Änon bei Salim. Nach einem Streit über die Reinigung melden die Jünger des Johannes, dass der, für den er Zeugnis abgelegt hat, tauft und alle zu ihm kommen. Johannes antwortet, niemand könne etwas empfangen, wenn es ihm nicht vom Himmel gegeben sei; er sei nicht der Christus, sondern vor ihm her gesandt. Wie der Freund des Bräutigams freut er sich über dessen Stimme: Jener muss wachsen, er selbst kleiner werden.", None),
 ("TU-JHN-003-031-036", "JHN.3.31-JHN.3.36", "discourse", "Der von oben kommt", None,
  "Wer von oben, vom Himmel kommt, ist über allen; wer von der Erde ist, redet von der Erde her. Er bezeugt, was er gesehen und gehört hat, doch niemand nimmt sein Zeugnis an; wer es annimmt, besiegelt, dass Gott wahrhaftig ist. Der Gesandte redet die Worte Gottes; der Vater liebt den Sohn und hat alles in seine Hand gegeben. Wer an den Sohn glaubt, hat ewiges Leben; auf dem, der dem Sohn nicht gehorcht, bleibt der Zorn Gottes. Ob hier der Täufer weiterspricht oder der Evangelist, lässt der Text offen.", None),
]
UNITS_GSW = {
 "TU-JHN-001-001-051": ("S Wort, s Zügnis vom Johannes und di erschte Jünger", "De Prolog redt vom Wort, wo im Aafang bi Gott gsii isch und Gott gsii isch, dur das alles worde isch und wo Fleisch worde isch; de Johannes isch gschickt, zum vom Liecht Zügnis gää. Vor Prieschter und Levite us Jerusalem strittet de Johannes ab, er sig de Christus, de Elija oder de Prophet, und nännt sich d Stimm us [[ISA.40.3]]. Er bezeichnet de Jesus als s Lamm vo Gott und bezüügt, er heig de Geischt uf ihn abecho gseh. Zwei vo sine Jünger gönd em Jesus nache; de Andreas bringt sin Brüeder Simon, und de Jesus seit em, er wärdi Kephas heisse. De Jesus rüeft de Philippus; de Natanaël bekännt en als Sohn vo Gott und König vo Israel, und de Jesus seit, si wärdid de Himmel offe gseh."),
 "TU-JHN-001-001-018": ("De Prolog: S Wort isch Fleisch worde", "Im Aafang isch s Wort bi Gott gsii, und s Wort isch Gott gsii; dur es isch alles worde, in ihm isch Läbe gsii, s Liecht vo de Mänsche, wo i de Fiischteri schiint. De Johannes isch gschickt, zum vom Liecht Zügnis gää. S wahr Liecht chunnt i d Wält; er chunnt zu sim Eigete, aber di Sine nämed en nöd uf; allne, wo en ufnämed, git er d Vollmacht, Chind vo Gott z wärde. S Wort isch Fleisch worde und hät under üs gwohnt, voll Gnad und Wahrheit. Niemer hät Gott je gseh; de Einzig, Gott, wo a de Bruscht vom Vatter isch, hät Bricht gää."),
 "TU-JHN-001-019-028": ("S Zügnis vom Johannes vor de Gschickte", "Prieschter und Levite, wo d Jude vo Jerusalem gschickt händ, fröged de Johannes, wer er sig. Er bekännt, er sig nöd de Christus, au nöd de Elija oder de Prophet, sondern d Stimm vo eim, wo i de Wüeschti rüeft ([[ISA.40.3]]). Uf d Frag, werum er dänn taufi, wiist er uf eine, wo si nöd känned, wo mitte under ine staat und nach ihm chunnt. Das gschiet z Betanie ännet em Jordan."),
 "TU-JHN-001-029-034": ("S Lamm vo Gott", "Am nächschte Tag gseht de Johannes de Jesus choo und nännt en s Lamm vo Gott, wo d Sünd vo de Wält wägnimmt. Er bezüügt, er heig de Geischt wie e Tuube abecho und uf ihm bliibe gseh; dra hät er, wie s ihm dä gseit hät, wo en zum Taufe gschickt hät, dä söle erchänne, wo mit heilige Geischt tauft. Er bezüügt: Dä isch de Userwählt vo Gott."),
 "TU-JHN-001-035-042": ("Di erschte Jünger", "Zwei Jünger vom Johannes ghöred, wie er de Jesus s Lamm vo Gott nännt, und gönd em Jesus nache. Uf sini Frag, was si sueched, fröged si nach sinere Bliibi und bliibed dä Tag bi ihm. Eine vo ine, de Andreas, seit sim Brüeder Simon, si heigid de Messias gfunde, und bringt en zum Jesus; de Jesus seit em, er wärdi Kephas heisse."),
 "TU-JHN-001-043-051": ("De Philippus und de Natanaël", "De Jesus rüeft de Philippus, ihm nachezgaa. De Philippus seit em Natanaël, si heigid dä gfunde, vo däm de Mose und d Prophete gschribe händ, de Jesus vo Nazaret. De Natanaël zwiiflet, chunnt aber mit; de Jesus nännt en en würkliche Israelit ohni Falschs und seit, er heig en under em Fiigebaum gseh; de Natanaël bekännt en als Sohn vo Gott und König vo Israel. De Jesus seit Grössers aa: Si wärded de Himmel offe gseh und d Ängel vo Gott ufe- und abestiige uf de Mänschesohn."),
 "TU-JHN-002-001-025": ("Kana und de Tämpel z Jerusalem", "A ere Hochziit z Kana wird s Wasser, wo d Diener uf d Aawiisig vom Jesus schöpfed, zu Wii; das isch de Aafang vo de Zeiche, de Jesus offebaret sini Herrlichkeit, und sini Jünger glaubed a ihn. Vor em Passa tribt de Jesus d Händler und d Gäldwächsler us em Tämpel z Jerusalem. Wo s en nach eme Zeiche fröged, redt er devo, de Tämpel abzriisse und i drüü Täg ufzstelle; de Evangelischt erklärt, er heig vom Tämpel vo sim Liib gredt. Vili glaubed wäge de Zeiche a ihn, aber de Jesus vertrout sich ine nöd aa, wil er erchännt, was im Mänsch isch."),
 "TU-JHN-002-001-012": ("D Hochziit z Kana", "A ere Hochziit z Kana gaat de Wii us. D Mueter vom Jesus seit s em; er antwortet, sini Stund sig no nöd choo, aber si seit de Diener, si söled mache, was er säg. Uf d Aawiisig vom Jesus füüled d Diener sächs steinigi Chrüeg mit Wasser und bringed devo em Spiismeischter; s Wasser isch zu Wii worde, und de Spiismeischter seit zum Brüütigam, er heig de guet Wii bis jetzt ufbhalte. Demit macht de Jesus de Aafang vo de Zeiche und offebaret sini Herrlichkeit; sini Jünger glaubed a ihn. Dänn gaat er mit de Mueter, de Brüedere und de Jünger für es paar Täg uf Kafarnaum."),
 "TU-JHN-002-013-022": ("D Tämpelreinigung", "Vor em Passa tribt de Jesus im Tämpel z Jerusalem mit ere Geissle alli mitsamt de Schaf und Rinder use, schüttet s Gält vo de Wächsler us und verbietet, s Huus vo sim Vatter zumene Handelshuus z mache; d Jünger erinnered sich a [[PSA.69.9]]. D Jude fröged nach eme Zeiche. De Jesus antwortet: «Riissed dä Tämpel ab, und i drüü Täg stell ich en uf.» Si wänded ii, a däm Tämpel sig sächsevierzg Jahr buut worde; er aber redt, seit de Erzäler, vom Tämpel vo sim Liib, und nach sinere Uferweckig erinnered sich d Jünger a das Wort."),
 "TU-JHN-002-023-025": ("Glaube wäge de Zeiche", "Am Passafäscht z Jerusalem glaubed vili a sin Name, wil si sini Zeiche gsehnd. De Jesus aber vertrout sich ine nöd aa, dänn er kännt alli und erchännt sälber, was im Mänsch isch."),
 "TU-JHN-003-001-036": ("De Nikodemus und s letscht Zügnis vom Täufer", "De Nikodemus, en Pharisäer und en Oberschte vo de Jude, chunnt znacht zum Jesus. De Jesus seit em, wer nöd vo obe, us Wasser und Geischt gebore wärdi, chönn s Riich vo Gott nöd gseh und nöd inechoo; de Nikodemus verstaat s nöd. De Jesus redt vom Mänschesohn, wo mues erhöcht wärde wie d Schlange i de Wüeschti, und devo, dass Gott d Wält so gliebt hät, dass er de einzig Sohn gää hät; s Gricht isch, dass d Mänsche d Fiischteri meh gliebt händ als s Liecht. De Jesus tauft in Judäa, de Johannes z Änon. Wo sini Jünger em melded, dass alli zum Jesus gönd, vergliicht sich de Johannes mit em Fründ vom Brüütigam: Dä mues wachse, er sälber chliiner wärde. Wer vom Himmel chunnt, isch über allne; wer a de Sohn glaubt, hät ewigs Läbe. Öb [[JHN.3.16]]–[[JHN.3.21]] und [[JHN.3.31]]–[[JHN.3.36]] no zu de Rede vom Jesus und vom Täufer ghöred oder de Evangelischt erklärt, laat de Text offe."),
 "TU-JHN-003-001-015": ("De Jesus und de Nikodemus", "De Nikodemus chunnt znacht und anerchännt de Jesus als Lehrer, wo vo Gott choo isch, wil niemer sini Zeiche chönn mache, wänn Gott nöd mit ihm sig. De Jesus antwortet, wer nöd vo obe gebore wärdi, chönn s Riich vo Gott nöd gseh. De Nikodemus fröget, öb en Mänsch es zweits Mal i de Buuch vo sinere Mueter chönn inegaa; de Jesus redt vo de Geburt us Wasser und Geischt und vergliicht de Geischt mit em Wind. Er fröget, öb de Lehrer vo Israel das nöd verstaa, und redt vom Mänschesohn, wo vom Himmel abegstige isch und mues erhöcht wärde wie d Schlange i de Wüeschti, demit jede, wo glaubt, in ihm ewigs Läbe hät."),
 "TU-JHN-003-016-021": ("So hät Gott d Wält gliebt", "Gott hät d Wält so gliebt, dass er de einzig Sohn gää hät, demit jede, wo a ihn glaubt, nöd verlore gaat, sondern ewigs Läbe hät; er hät en nöd gschickt, zum d Wält richte, sondern demit si grettet wird. Wer nöd glaubt, isch scho grichtet. S Gricht isch, dass s Liecht i d Wält choo isch und d Mänsche d Fiischteri meh gliebt händ als s Liecht: Wer Schlächts tuet, chunnt nöd zum Liecht, wer d Wahrheit tuet, chunnt zum Liecht. Öb d Vers no zur Red vom Jesus a de Nikodemus ghöred oder de Evangelischt erklärt, laat de Text offe."),
 "TU-JHN-003-022-030": ("De Fründ vom Brüütigam", "De Jesus haltet sich mit sine Jünger in Judäa uf und tauft; au de Johannes tauft no, z Änon bi Salim. Nach eme Striit über d Reinigung melded d Jünger vom Johannes, dass dä, für dä er Zügnis gää hät, tauft und alli zu ihm chömed. De Johannes antwortet, niemer chönn öppis übercho, wänn s ihm nöd vom Himmel gää sig; er sig nöd de Christus, sondern vor ihm här gschickt. Wie de Fründ vom Brüütigam fröit er sich über dä sini Stimm: Dä mues wachse, er sälber chliiner wärde."),
 "TU-JHN-003-031-036": ("Dä, wo vo obe chunnt", "Wer vo obe, vom Himmel chunnt, isch über allne; wer vo de Ärde isch, redt vo de Ärde här. Er bezüügt, was er gseh und ghört hät, aber niemer nimmt sis Zügnis aa; wer s aanimmt, bsiglet, dass Gott wahrhaftig isch. De Gschickt redt d Wort vo Gott; de Vatter liebt de Sohn und hät alles i sini Hand gää. Wer a de Sohn glaubt, hät ewigs Läbe; uf däm, wo em Sohn nöd folget, bliibt de Zorn vo Gott. Öb da de Täufer wiiterredt oder de Evangelischt, laat de Text offe."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts gezählt (einschliesslich der Abschnitte, "
  "die der SBLGNT in Doppelklammern setzt)."),
 ("Grundentscheide für das ganze Johannesevangelium. Diese Datei (Kapitel 1–3) legt sie fest; die Übersetzungen der weiteren "
  "Kapitel verweisen darauf und weichen nur mit eigener Begründung in decisions ab. Jede Wiedergabe ist eine redaktionelle "
  "Entscheidung, keine geprüfte Festlegung."),
 ("1. λόγος: «das Wort» ([[JHN.1.1]], [[JHN.1.14]]). Johannes erklärt den Begriff nicht; Anklänge an [[GEN.1.1]], an Gottes "
  "schaffendes Wort und an die Weisheit (vgl. [[PRO.8.22]]–[[PRO.8.30]]) werden vertreten, ebenso an die griechische "
  "Philosophie. «Wort» bleibt nah am Griechischen und verbindet den Titel mit dem gewöhnlichen Gebrauch von λόγος im "
  "Evangelium (nach MACULA-Lemma 40-mal im SBLGNT-Text). Fürwörter: sächlich bis [[JHN.1.5]], ab [[JHN.1.10]] männlich."),
 ("2. Licht und Finsternis: φῶς «Licht», σκοτία und σκότος «Finsternis», durchgehend; ebenso «erleuchten» (φωτίζω). In der "
  "Mundart «Liecht» und «Fiischteri» wie in den Johannesbriefen."),
 ("3. κόσμος: «Welt» (78-mal), durchgehend, auch wo die Menschenwelt gemeint ist, die sich Gott verschliesst; die Spannweite "
  "(Schöpfung, geliebte Menschheit, widerstrebende Welt) wird in decisions erläutert, nicht durch wechselnde Wörter."),
 ("4. δόξα / δοξάζω: «Herrlichkeit» / «verherrlichen» (19- bzw. 23-mal). «Ehre» steht nur, wo δόξα das Ansehen bei "
  "Menschen meint: [[JHN.5.41]], [[JHN.5.44]], [[JHN.7.18]], [[JHN.8.50]], [[JHN.8.54]], [[JHN.9.24]], [[JHN.12.43]], jeweils "
  "mit eigener Entscheidung in decisions."),
 ("5. σημεῖον: «Zeichen» (17-mal), nie «Wunder». Johannes braucht für Jesu Taten nie δύναμις («Machttat»); die Taten "
  "verweisen auf seine Herrlichkeit und rufen zum Glauben ([[JHN.2.11]], [[JHN.20.30]]–[[JHN.20.31]]). Ebenso ἔργα «Werke»."),
 ("6. μένω: «bleiben» (40-mal), auch im alltäglichen Sinn; wo das Deutsche «bleiben» nicht trägt, wird ein Wort vom selben "
  "Stamm gewählt («Bleibe», [[JHN.1.38]]–[[JHN.1.39]]). Mundart «bliibe», «Bliibi»."),
 ("7. ἀμὴν ἀμὴν λέγω ὑμῖν / σοι: «Amen, amen, ich sage euch / dir» (25-mal doppelt; in den Evangelien nur bei Johannes). "
  "Mundart: «Amen, amen, ich säge eu / dir»."),
 ("8. ἐγώ εἰμι: «Ich bin …»; mit Prädikat («Ich bin das Brot des Lebens», [[JHN.6.35]]) wörtlich. Ohne Prädikat gilt: "
  "absolut gebraucht ([[JHN.8.24]], [[JHN.8.28]], [[JHN.8.58]], [[JHN.13.19]]) «ich bin»; als Antwort oder Identifikation "
  "([[JHN.4.26]], [[JHN.6.20]], [[JHN.9.9]], [[JHN.18.5]]–[[JHN.18.8]]) «Ich bin es», jeweils mit der anderen Wiedergabe als "
  "Alternative in decisions und mit Hinweis auf den Anklang an Gottes Selbstvorstellung ([[EXO.3.14]], [[ISA.43.10]] in der "
  "Septuaginta). In Kapitel 1–3 steht nur die "
  "verneinte Form des Täufers «Ich bin nicht der Christus» ([[JHN.1.20]], [[JHN.3.28]])."),
 ("9. οἱ Ἰουδαῖοι (nach MACULA-Lemma Ἰουδαῖος 71-mal): Grundentscheid wörtlich «die Juden», durchgehend gleich, in "
  "decisions als Deutungsentscheidung (interpretive) markiert. Das Wort meint bei Johannes Verschiedenes: das jüdische Volk "
  "und seine Bräuche ([[JHN.2.6]], [[JHN.2.13]]), die Bewohner Judäas, die Jerusalemer Autoritäten ([[JHN.1.19]]), eine "
  "Gruppe, die Jesus ablehnt, aber auch Menschen, die an ihn glauben ([[JHN.8.31]], [[JHN.11.45]]). Jesus und seine Jünger "
  "sind selbst Juden ([[JHN.4.9]], [[JHN.4.22]]). Alternativen wie «die jüdischen Führer», «die Behörden» oder «die Judäer» "
  "verdeutlichen einzelne Stellen, legen aber eine Deutung in den Text und machen die Stellen untereinander unvergleichbar. "
  "Die wörtliche Wiedergabe zeigt, was dasteht, und verlangt die Erklärung: Johannes spricht aus einem innerjüdischen Konflikt "
  "seiner Zeit (vgl. den Ausschluss aus der Synagoge, [[JHN.9.22]]; Hintergrund BG-JHN-BOOK-0001). Pauschale Urteile über "
  "«die Juden» aller Zeiten sind damit nicht gedeckt; die Wirkungsgeschichte des Evangeliums im christlichen Judenhass ist "
  "mitzubedenken. Wo der Zusammenhang klar die Behörden meint, sagt das die decision zur Stelle. Mundart «d Jude»."),
 ("10. παράκλητος (erst ab [[JHN.14.16]]): «Beistand». Alternativen: «Tröster» (Luther), «Fürsprecher», «Anwalt», «Helfer», "
  "die Umschrift «Paraklet». In [[1JN.2.1]] ist dasselbe Wort für Jesus beim Vater mit «Fürsprecher» übersetzt; im Evangelium "
  "steht es für den Geist, der den Jüngern beisteht."),
 ("11. ὑψόω: «erhöhen» (5-mal: [[JHN.3.14]], [[JHN.8.28]], [[JHN.12.32]], [[JHN.12.34]]) mit dem Doppelsinn von Kreuz und "
  "Erhöhung zu Gott. ἄνωθεν: «von oben» ([[JHN.3.3]], [[JHN.3.7]], [[JHN.3.31]], [[JHN.19.11]], [[JHN.19.23]]); in [[JHN.3.3]] und [[JHN.3.7]] "
  "mit dem Doppelsinn «von neuem», den Nikodemus missversteht."),
 ("12. Weitere einheitliche Wiedergaben: μονογενής «einzig» (4-mal); πιστεύω εἰς «glauben an» (πιστεύω 98-mal; das Nomen "
  "πίστις fehlt); μαρτυρέω / μαρτυρία «bezeugen, Zeugnis ablegen» / «Zeugnis»; ἀλήθεια «Wahrheit»; ζωὴ αἰώνιος «ewiges "
  "Leben»; ὥρα «Stunde»; υἱὸς τοῦ ἀνθρώπου «Menschensohn» und χριστός «Christus» wie bei Markus; παραδίδωμι «ausliefern»; "
  "κρίνω / κρίσις «richten» / «Gericht». ἀγαπάω «lieben», φιλέω «lieb haben» (Mundart «liebe», «gärn haa»), damit der Wechsel der Verben sichtbar bleibt; ob "
  "Johannes damit einen Bedeutungsunterschied verbindet, ist umstritten (vgl. [[JHN.21.15]]–[[JHN.21.17]]). "
  "Gottesbezeichnungen: θεός «Gott», πατήρ «Vater» (Mundart «Gott», «de Vatter»)."),
 ("13. Erzählweise und Redegrenzen: Das erzählende Präsens (λέγει «sagt») ist beibehalten. ὅτι vor direkter Rede ist nicht "
  "eigens übersetzt. Anführungszeichen sind eine Entscheidung der Übersetzung, denn das Griechische hat keine. Johannes lässt "
  "Reden oft ohne Markierung in Erläuterung übergehen; die Übersetzung lässt eine Rede weiterlaufen, solange kein "
  "Sprecherwechsel angezeigt ist, und nennt die andere Möglichkeit in decisions (in Kapitel 3: [[JHN.3.16]]–[[JHN.3.21]] und "
  "[[JHN.3.31]]–[[JHN.3.36]])."),
 ("14. Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT gegen WH, Treg, NA28 und RP liest (z. B. "
  "[[JHN.1.34]] ἐκλεκτός). Abweichende Lesarten stehen als Alternativen, soweit sie die Übersetzung verändern. Verse ohne "
  "SBLGNT-Text erhalten keine Übersetzung; ihr Wortlaut steht als Alternative beim Nachbarvers. In Kapitel 1–3 fehlt kein Vers."),
 ("Kapitel 1–3 im Einzelnen: In [[JHN.1.3]]–[[JHN.1.4]] folgt die Übersetzung der Zeichensetzung des SBLGNT («Was geworden "
  "ist – in ihm war Leben»); [[JHN.1.15]] steht wie im SBLGNT in runden Klammern. In [[JHN.3.31]] fehlt nach den "
  "CNTR-Transkriptionen die zweite Wendung «ist über allen» in 01, 05 und 𝔓75; der SBLGNT-Apparat verzeichnet dort keine "
  "Variante, deshalb steht der Befund in decisions und nicht als Alternative."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Grundentscheid fürs ganz Johannesevangelium (usfüerlich i de hochdütsche translation_notes): λόγος «s Wort»; φῶς «Liecht», "
  "σκοτία «Fiischteri»; κόσμος «Wält»; δόξα «Herrlichkeit»; σημεῖον «Zeiche», nöd «Wunder»; μένω «bliibe»; ἀμὴν ἀμήν "
  "«Amen, amen, ich säge eu / dir»; ἐγώ εἰμι «Ich bi …» (als Antwort «Ich bi s», absolut «ich bi»); ἀγαπάω «liebe», φιλέω «gärn haa»; δόξα nu bi Aasee vo Mänsche «Ehr»; ὑψόω «erhöche»; ἄνωθεν «vo obe»; παράκλητος «Biistand»; "
  "οἱ Ἰουδαῖοι wörtlich «d Jude» (Düütigsentscheid, lueg decisions)."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Johannes»); Gott heisst «Gott», de Vatter «de Vatter»; Perfekt statt "
  "Präteritum; «wo» als Relativwort; kei Genitiv («s Lamm vo Gott»)."),
 ("Redegränze: S Griechisch hät kei Aafüerigszeiche. D Übersetzig laat d Red vom Jesus bis [[JHN.3.21]] und die vom Täufer bis "
  "[[JHN.3.36]] laufe; öb dört de Evangelischt erklärt, isch offe."),
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
            raise SystemExit(f"JHN {c}: unerwartet fehlende Verse")
        follows = sorted(f"{vid}:{r['reading_id']}" for vid, v in variants.items() if v["reference"] in refs_c
                         for r in v["readings"] if r.get("is_sblgnt_text"))
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Liecht, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Namen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-JHN-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; johanneische Schlüsselwörter einheitlich (Grundentscheide in translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/johannes_text_01_03.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Johannes 1–3 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
