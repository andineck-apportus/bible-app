#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 16–17 (Zeichenforderung, Sauerteig, Bekenntnis des Petrus, erste Leidensankündigung und
Nachfolge, Verwandlung auf dem Berg, Frage nach Elija, Heilung des mondsüchtigen Jungen, zweite Leidensankündigung,
Doppeldrachme) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_16_17.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- [[MAT.17.21]] fehlt im SBLGNT (keine Tokens). Der Wortlaut steht als Alternative zu [[MAT.17.20]]
  (VAR-SBLGNTAPP-MAT-017-020-04); die automatische Zuordnung sieht den zusätzlichen Vers nicht, die Angaben zu den
  Handschriften stammen deshalb aus den CNTR-Transkriptionen.
- [[MAT.16.2]]b–3 steht im SBLGNT im Text (Apparatzeichen ⸂ … ⸃). Der SBLGNT-Apparat führt dazu zwei Einträge (WH setzt
  die Worte in doppelte eckige Klammern; RP ergänzt «Heuchler»), die in data/variants/sblgntapp-mat nicht importiert sind.
  Deshalb stehen sie in decisions und translation_notes, nicht als Alternativen (Vorgehen wie bei [[JHN.3.31]]).

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1)
bzw. aus den CNTR-Transkriptionen (Sekundärtranskription), nicht aus eigener Prüfung der Handschriften. Zahlen zu
Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts (data/annotations) ermittelt.
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
CHAPTERS = ((16, 28), (17, 27))
NO_TOKENS = {"MAT.17.21"}  # im SBLGNT nicht enthalten; andere Ausgaben führen den Vers

DE = {
 # ------------------------------------------------------------ Kapitel 16
 "MAT.16.1": "Und{1} [die Pharisäer]{3,4} und{5} [Sadduzäer]{6} [traten heran]{2}; [um ihn auf die Probe zu stellen]{7}, [forderten sie]{8} [ihn]{9} [auf]{8}, [ihnen]{15} [ein Zeichen]{10} [vom]{11,12} [Himmel]{13} [zu zeigen]{14}.",
 "MAT.16.2": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4} [zu ihnen]{5}: «[Wenn es Abend]{6} [wird]{7}, [sagt ihr]{8}: ‹[Schönes Wetter]{9}! [Denn]{11} [der Himmel]{12,13} [ist rot]{10}.›",
 "MAT.16.3": "[Und]{1} [am Morgen]{2}: ‹[Heute]{3} [kommt ein Unwetter]{4}, [denn]{6} [der Himmel]{8,9} [ist rot]{5} [und düster]{7}.› [Das Aussehen]{10,12} [des Himmels]{13,14} [wisst ihr]{15} [zwar]{11} [zu beurteilen]{16}, [die Zeichen]{17,19} [der Zeiten]{20,21} [aber]{18} [könnt ihr]{23} [nicht]{22} beurteilen.",
 "MAT.16.4": "[Ein böses]{2} und{3} [ehebrecherisches]{4} [Geschlecht]{1} [verlangt]{6} [ein Zeichen]{5}, und{7} [ein Zeichen]{8} [wird]{10} [ihm]{11} [nicht]{9} [gegeben werden]{10} [ausser]{12,13} [dem Zeichen]{14,15} [des Jona]{16}.» Und{17} [er verliess]{18} [sie]{19} und [ging weg]{20}.",
 "MAT.16.5": "Und{1} [die Jünger]{3,4} [kamen]{2} [ans]{5,6} [andere Ufer]{7} und [hatten vergessen]{8}, [Brote]{9} [mitzunehmen]{10}.",
 "MAT.16.6": "[Jesus]{1,3} [aber]{2} [sagte]{4} [zu ihnen]{5}: «[Seht zu]{6} und{7} [hütet euch]{8} [vor]{9} [dem Sauerteig]{10,11} [der Pharisäer]{12,13} und{14} [Sadduzäer]{15}!»",
 "MAT.16.7": "[Sie]{1} [aber]{2} [überlegten]{3} [untereinander]{4,5} und [sagten]{6}: «[Wir haben]{10} [keine]{9} [Brote]{8} [mitgenommen]{10}.» ~7(ὅτι leitet die direkte Rede ein)",
 "MAT.16.8": "[Jesus]{3,4} [aber]{2} [merkte es]{1} und [sagte]{5}: «[Was]{6} [überlegt ihr]{7} [untereinander]{8,9}, [ihr Kleingläubigen]{10}, [dass]{11} [ihr]{14} [keine]{13} [Brote]{12} [mitgenommen habt]{14}?",
 "MAT.16.9": "[Begreift ihr]{2} [noch nicht]{1}? [Erinnert ihr euch]{4} [auch nicht]{3} [an die]{5} [fünf]{6} [Brote]{7} [für die]{8} [Fünftausend]{9} und{10} [wie viele]{11} [Körbe]{12} [ihr aufgehoben habt]{13}?",
 "MAT.16.10": "[Auch nicht]{1} [an die]{2} [sieben]{3} [Brote]{4} [für die]{5} [Viertausend]{6} und{7} [wie viele]{8} [Körbe]{9} [ihr aufgehoben habt]{10}?",
 "MAT.16.11": "[Wieso]{1} [begreift ihr]{3} [nicht]{2}, [dass]{4} [ich]{8} [nicht]{5} [von]{6} [Broten]{7} [zu euch]{9} [gesprochen habe]{8}? [Hütet euch]{10} [aber]{11} [vor]{12} [dem Sauerteig]{13,14} [der Pharisäer]{15,16} und{17} [Sadduzäer]{18}!»",
 "MAT.16.12": "[Da]{1} [verstanden sie]{2}, [dass]{3} [er]{5} [nicht]{4} [gesagt hatte]{5}, [sie sollten sich]{6} [vor]{7} [dem Sauerteig]{8,9} [der Brote]{10,11} [hüten]{6}, [sondern]{12} [vor]{13} [der Lehre]{14,15} [der Pharisäer]{16,17} und{18} [Sadduzäer]{19}.",
 "MAT.16.13": "[Als]{1} [Jesus]{3,4} [aber]{2} [in]{5} [die Gegend]{6,7} [von Cäsarea]{8} [Philippi]{9,10} [kam]{1}, [fragte er]{11} [seine]{14} [Jünger]{12,13}: «[Wer]{16}, [sagen]{17} [die Leute]{18,19}, [sei]{20} [der Menschensohn]{21-24}?» ~15(λέγων «sagend» leitet die direkte Rede ein)",
 "MAT.16.14": "[Sie]{1} [aber]{2} [sagten]{3}: «[Die einen]{4,5}: [Johannes]{6} [der Täufer]{7,8}, [andere]{9} [aber]{10}: [Elija]{11}, [wieder andere]{12} [aber]{13}: [Jeremia]{14} [oder]{15} [einer]{16} [der]{17} [Propheten]{18}.»",
 "MAT.16.15": "[Er sagt]{1} [zu ihnen]{2}: «[Ihr]{3} [aber]{4}, [wer]{5}, [sagt ihr]{7}, [sei]{8} [ich]{6}?»",
 "MAT.16.16": "[Simon]{3} [Petrus]{4} [aber]{2} [antwortete]{1} und [sagte]{5}: «[Du]{6} [bist]{7} [der Christus]{8,9}, [der Sohn]{10,11} [des lebendigen]{14,15} [Gottes]{12,13}!»",
 "MAT.16.17": "[Jesus]{3,4} [aber]{2} [antwortete]{1} und [sagte]{5} [zu ihm]{6}: «[Selig]{7} [bist du]{8}, [Simon]{9} [Barjona]{10}, [denn]{11} [nicht]{15} [Fleisch]{12} und{13} [Blut]{14} [hat]{16} [dir]{17} [das offenbart]{16}, [sondern]{18} [mein]{21} [Vater]{19,20} [in]{22,23} [den Himmeln]{24,25}.",
 "MAT.16.18": "[Ich]{1} [aber]{2} [sage]{4} [dir]{3} [auch]{1}: [Du]{6} [bist]{7} [Petrus]{8}, und{9} [auf]{10} [diesen]{11} [Felsen]{12,13} [werde ich]{14} [meine]{15} [Gemeinde]{16,17} [bauen]{14}, und{18} [die Tore]{19} [des Totenreichs]{20} [werden]{22} [sie]{23} [nicht]{21} [überwältigen]{22}. ~5(ὅτι leitet die direkte Rede ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.16.19": "[Ich werde]{1} [dir]{2} [die Schlüssel]{3,4} [des Reichs]{5,6} [der Himmel]{7,8} [geben]{1}, und{9} [was]{10} [du]{12} [auch]{11} [auf]{13} [der Erde]{14,15} [bindest]{12}, [wird]{16} [in]{18} [den Himmeln]{19,20} [gebunden]{17} [sein]{16}, und{21} [was]{22} [du]{24} [auch]{23} [auf]{25} [der Erde]{26,27} [löst]{24}, [wird]{28} [in]{30} [den Himmeln]{31,32} [gelöst]{29} [sein]{28}.»",
 "MAT.16.20": "[Dann]{1} [schärfte er]{2} [den Jüngern]{3,4} [ein]{2}, [dass]{5} [sie]{7} [niemandem]{6} [sagen sollten]{7}, [dass]{8} [er]{9} [der Christus]{11,12} [sei]{10}.",
 "MAT.16.21": "[Von da an]{1,2} [begann]{3} [Jesus]{4,5} [seinen]{9} [Jüngern]{7,8} [zu zeigen]{6}, [dass]{10} [er]{12} [nach]{13} [Jerusalem]{14} [gehen]{15} und{16} [von]{19} [den Ältesten]{20,21} und{22} [Hohepriestern]{23} und{24} [Schriftgelehrten]{25} [vieles]{17} [erleiden]{18} und{26} [getötet werden]{27} und{28} [am]{29} [dritten]{30} [Tag]{31} [auferweckt werden]{32} [muss]{11}.",
 "MAT.16.22": "Und{1} [Petrus]{4,5} [nahm]{2} [ihn]{3} [beiseite]{2} und [fing an]{6}, [ihn]{8} [zurechtzuweisen]{7}: «[Gott bewahre dich]{10,11:idiom}, [Herr]{12}! [Das]{17} [wird]{15} [dir]{16} [niemals]{13,14} [widerfahren]{15}!» ~9(λέγων «sagend» leitet die direkte Rede ein)",
 "MAT.16.23": "[Er]{1} [aber]{2} [wandte sich um]{3} und [sagte]{4} [zu Petrus]{5,6}: «[Geh]{7} [hinter]{8} [mich]{9}, [Satan]{10}! [Du bist]{12} [mir]{13} [ein Fallstrick]{11}; [denn]{14} [du hast]{16} [nicht]{15} [im Sinn]{16}, [was]{17} [Gottes]{18,19} ist, [sondern]{20} [was]{21} [der Menschen]{22,23} ist.»",
 "MAT.16.24": "[Da]{1} [sagte]{4} [Jesus]{2,3} [zu]{5} [seinen]{7} [Jüngern]{6}: «[Wenn]{8} [jemand]{9} [hinter]{11} [mir]{12} [herkommen]{13} [will]{10}, [der verleugne]{14} [sich selbst]{15} und{16} [nehme]{17} [sein]{20} [Kreuz]{18,19} [auf sich]{17} und{21} [folge]{22} [mir]{23} [nach]{22}.",
 "MAT.16.25": "[Denn]{2} [wer]{1} [sein]{7} [Leben]{5,6} [retten]{8} [will]{4}, [wird]{9} [es]{10} [verlieren]{9}; [wer]{11} [aber]{12} [sein]{17} [Leben]{15,16} [verliert]{14} [um meinetwillen]{18,19}, [wird]{20} [es]{21} [finden]{20}. ~3(ἐάν macht «wer» allgemein; nicht eigens wiedergegeben) ~13(ἄν macht «wer» allgemein; nicht eigens wiedergegeben)",
 "MAT.16.26": "[Denn]{2} [was]{1} [wird es]{3} [einem Menschen]{4} [nützen]{3}, [wenn]{5} [er]{9} [die]{6} [ganze]{8} [Welt]{7} [gewinnt]{9}, [sein]{13} [Leben]{10,12} [aber]{11} [einbüsst]{14}? [Oder]{15} [was]{16} [wird]{17} [ein Mensch]{18} [als Gegenwert]{19} [für]{20} [sein]{22} [Leben]{21} [geben]{17}?",
 "MAT.16.27": "[Denn]{2} [der Menschensohn]{3-6} [wird]{1} [in]{8} [der Herrlichkeit]{9,10} [seines]{13} [Vaters]{11,12} [mit]{14} [seinen]{17} [Engeln]{15,16} [kommen]{7}, und{18} [dann]{19} [wird er]{20} [jedem]{21} [nach]{22} [seinem]{25} [Tun]{23,24} [vergelten]{20}.",
 "MAT.16.28": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Es sind]{5} [einige]{6} [von denen, die]{7} [hier]{8} [stehen]{9}, [die]{10} [den Tod]{14} [nicht]{11,12} [schmecken werden]{13}, [bis]{15} [sie]{17} [den Menschensohn]{18-21} [in]{23} [seinem]{26} [Reich]{24,25} [kommen]{22} [sehen]{17}.» ~4(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben) ~16(ἄν macht «bis» offen; nicht eigens wiedergegeben)",
 # ------------------------------------------------------------ Kapitel 17
 "MAT.17.1": "Und{1} [nach]{2} [sechs]{4} [Tagen]{3} [nimmt]{5} [Jesus]{6,7} [Petrus]{8,9} und{10} [Jakobus]{11} und{12} [Johannes]{13}, [dessen]{16} [Bruder]{14,15}, [mit]{5} und{17} [führt]{18} [sie]{19} [auf]{20} [einen hohen]{22} [Berg]{21} [hinauf]{18}, [für sich allein]{23,24}.",
 "MAT.17.2": "Und{1} [er wurde]{2} [vor]{3} [ihnen]{4} [verwandelt]{2}, und{5} [sein]{9} [Gesicht]{7,8} [leuchtete]{6} [wie]{10} [die Sonne]{11,12}, [seine]{16} [Kleider]{13,15} [aber]{14} [wurden]{17} [weiss]{18} [wie]{19} [das Licht]{20,21}.",
 "MAT.17.3": "Und{1} [siehe]{2}, [es erschienen]{3} [ihnen]{4} [Mose]{5} und{6} [Elija]{7} und [redeten]{8} [mit]{9} [ihm]{10}.",
 "MAT.17.4": "[Petrus]{3,4} [aber]{2} [ergriff das Wort]{1} und [sagte]{5} [zu Jesus]{6,7}: «[Herr]{8}, [es ist]{10} [gut]{9}, [dass wir]{11} [hier]{12} [sind]{13}. [Wenn]{14} [du willst]{15}, [werde ich]{16} [hier]{17} [drei]{18} [Hütten]{19} [machen]{16}: [dir]{20} [eine]{21} und{22} [Mose]{23} [eine]{24} und{25} [Elija]{26} [eine]{27}.»",
 "MAT.17.5": "[Während]{3} [er]{2} [noch]{1} [redete]{3}, [siehe]{4}, [eine lichte]{6} [Wolke]{5} [überschattete]{7} [sie]{8}, und{9} [siehe]{10}, [eine Stimme]{11} [aus]{12} [der Wolke]{13,14} [sagte]{15}: «[Dieser]{16} [ist]{17} [mein]{20} [Sohn]{18,19}, [der Geliebte]{21,22}, [an]{23} [dem]{24} [ich Gefallen gefunden habe]{25}; [hört auf]{26} [ihn]{27}!»",
 "MAT.17.6": "Und{1} [als]{2} [die Jünger]{3,4} [das hörten]{2}, [fielen sie]{5} [auf]{6} [ihr]{8} [Gesicht]{7} und{9} [fürchteten sich]{10} [sehr]{11}.",
 "MAT.17.7": "Und{1} [Jesus]{3,4} [trat heran]{2}, [berührte]{6} [sie]{7} und{5} [sagte]{8}: «[Steht auf]{9} und{10} [fürchtet euch]{12} [nicht]{11}!»",
 "MAT.17.8": "[Als sie]{1} [aber]{2} [ihre]{5} [Augen]{3,4} [erhoben]{1}, [sahen sie]{7} [niemanden]{6} [ausser]{8,9} [Jesus]{11} [allein]{12}. ~10(αὐτόν «ihn selbst» hebt Jesus hervor; nicht eigens wiedergegeben)",
 "MAT.17.9": "Und{1} [als]{2} [sie]{3} [vom]{4,5} [Berg]{6} [herabstiegen]{2}, [gebot]{7} [ihnen]{8} [Jesus]{9,10}: «[Erzählt]{13} [niemandem]{12} [von der Erscheinung]{14,15}, [bis]{16,17} [der Menschensohn]{18-21} [von]{22} [den Toten]{23} [auferweckt ist]{24}!» ~11(λέγων «sagend» leitet die direkte Rede ein)",
 "MAT.17.10": "Und{1} [die Jünger]{4,5} [fragten]{2} [ihn]{3}: «[Warum]{7} [sagen]{11} [dann]{8} [die Schriftgelehrten]{9,10}, [dass]{12} [Elija]{13} [zuerst]{16} [kommen]{15} [muss]{14}?» ~6(λέγοντες «sagend» leitet die direkte Rede ein)",
 "MAT.17.11": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: «[Elija]{5} [kommt]{7} [zwar]{6} und{8} [wird]{9} [alles]{10} [wiederherstellen]{9}.",
 "MAT.17.12": "[Ich sage]{1} [euch]{3} [aber]{2}: [Elija]{5} [ist]{7} [schon]{6} [gekommen]{7}, und{8} [sie haben]{10} [ihn]{11} [nicht]{9} [erkannt]{10}, [sondern]{12} [haben]{13} [mit]{14} [ihm]{15} [gemacht]{13}, [was]{16} [sie wollten]{17}. [So]{18} [wird]{24} [auch]{19} [der Menschensohn]{20-23} [durch]{26} [sie]{27} [leiden]{25}.» ~4(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.17.13": "[Da]{1} [verstanden]{2} [die Jünger]{3,4}, [dass]{5} [er]{10} [zu ihnen]{11} [von]{6} [Johannes]{7} [dem Täufer]{8,9} [gesprochen hatte]{10}.",
 "MAT.17.14": "Und{1} [als sie]{2} [zu]{3} [der Menge]{4,5} [kamen]{2}, [trat]{6} [ein Mensch]{8} [zu ihm]{7} [heran]{6}, [fiel]{9} [vor ihm]{10} [auf die Knie]{9}",
 "MAT.17.15": "und{1} [sagte]{2}: «[Herr]{3}, [erbarme dich]{4} [meines]{5} [Sohnes]{6,7}, [denn]{8} [er ist mondsüchtig]{9} und{10} [leidet]{12} [schwer]{11}; [oft]{13} [fällt er]{15} [nämlich]{14} [ins]{16,17} [Feuer]{18} und{19} [oft]{20} [ins]{21,22} [Wasser]{23}.",
 "MAT.17.16": "Und{1} [ich habe]{2} [ihn]{3} [zu]{4} [deinen]{6} [Jüngern]{5} [gebracht]{2}, und{7} [sie konnten]{9} [ihn]{10} [nicht]{8} [heilen]{11}.»",
 "MAT.17.17": "[Jesus]{3,4} [aber]{2} [antwortete]{1} und [sagte]{5}: «[O]{6} [ungläubiges]{8} und{9} [verkehrtes]{10} [Geschlecht]{7}, [wie lange]{11,12} [werde ich]{15} [bei]{13} [euch]{14} [sein]{15}? [Wie lange]{16,17} [werde ich]{18} [euch]{19} [ertragen]{18}? [Bringt]{20} [ihn]{22} [mir]{21} [hierher]{23}!»",
 "MAT.17.18": "Und{1} [Jesus]{4,5} [drohte]{2} [ihm]{3}, und{6} [der Dämon]{10,11} [fuhr]{7} [von]{8} [ihm]{9} [aus]{7}, und{12} [der Junge]{14,15} [wurde]{13} [von]{16} [jener]{19} [Stunde]{17,18} [an]{16} [geheilt]{13}.",
 "MAT.17.19": "[Da]{1} [traten]{2} [die Jünger]{3,4} [für sich allein]{7,8} [zu Jesus]{5,6} [heran]{2} und [sagten]{9}: «[Warum]{10,11} [konnten]{14} [wir]{12} [ihn]{16} [nicht]{13} [austreiben]{15}?»",
 "MAT.17.20": "[Er]{1} [aber]{2} [sagt]{3} [zu ihnen]{4}: «[Wegen]{5} [eures]{8} [Kleinglaubens]{6,7}. [Denn]{10} [amen]{9}, [ich sage]{11} [euch]{12}: [Wenn]{13} [ihr]{14} [Glauben]{15} [habt]{14} [wie]{16} [ein Senfkorn]{17,18}, [werdet ihr]{19} [zu]{20} [diesem]{22} [Berg]{21} [sagen]{19}: ‹[Geh]{23} [von hier]{24} [nach dort]{25}!›, und{26} [er wird hinübergehen]{27}; und{28} [nichts]{29} [wird]{30} [euch]{31} [unmöglich sein]{30}.»",
 "MAT.17.22": "[Als]{1} [sie]{3} [sich]{1} [aber]{2} [in]{4} [Galiläa]{5,6} [sammelten]{1}, [sagte]{7} [Jesus]{9,10} [zu ihnen]{8}: «[Der Menschensohn]{12-15} [wird]{11} [in]{17} [die Hände]{18} [von Menschen]{19} [ausgeliefert werden]{16},",
 "MAT.17.23": "und{1} [sie werden]{2} [ihn]{3} [töten]{2}, und{4} [am]{5} [dritten]{6} [Tag]{7} [wird er auferweckt werden]{8}.» Und{9} [sie wurden]{10} [sehr]{11} [traurig]{10}.",
 "MAT.17.24": "[Als]{1} [sie]{3} [aber]{2} [nach]{4} [Kafarnaum]{5} [kamen]{1}, [traten]{6} [die]{7} [Einnehmer]{10} [der]{8} [Doppeldrachme]{9} [an Petrus]{11,12} [heran]{6} und{13} [sagten]{14}: «[Zahlt]{19} [euer]{17} [Lehrer]{15,16} [die]{20} [Doppeldrachme]{21} [nicht]{18}?»",
 "MAT.17.25": "[Er sagt]{1}: «[Doch]{2}.» Und{3} [als er]{4} [ins]{5,6} [Haus]{7} [kam]{4}, [kam]{8} [Jesus]{10,11} [ihm]{9} [zuvor]{8} und [sagte]{12}: «[Was]{13} [meinst]{15} [du]{14}, [Simon]{16}? [Von]{21} [wem]{22} [nehmen]{23} [die Könige]{17,18} [der Erde]{19,20} [Zoll]{24} [oder]{25} [Steuer]{26}? [Von]{27} [ihren]{30} [Söhnen]{28,29} [oder]{31} [von]{32} [den Fremden]{33,34}?»",
 "MAT.17.26": "[Als er]{1} [aber]{2} [sagte]{1}: «[Von]{3} [den Fremden]{4,5}», [sagte]{6} [Jesus]{8,9} [zu ihm]{7}: «[Also]{10} [sind]{13} [die Söhne]{14,15} [doch]{11} [frei]{12}.",
 "MAT.17.27": "[Damit]{1} [wir]{4} [sie]{5} [aber]{2} [nicht]{3} [zu Fall bringen]{4}, [geh]{6} [an]{7} [den See]{8}, [wirf]{9} [eine Angel]{10} [aus]{9}, und{11} [den]{12} [ersten]{14} [Fisch]{15}, [der heraufkommt]{13}, [zieh heraus]{16}; und{17} [wenn du]{18} [sein]{21} [Maul]{19,20} [öffnest]{18}, [wirst du]{22} [einen Stater]{23} [finden]{22}. [Den]{24} [nimm]{25} und [gib]{26} [ihnen]{27} [für]{28} [mich]{29} und{30} [dich]{31}.»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 16
 "MAT.16.1": "Und{1} [d Pharisäer]{3,4} und{5} [Sadduzäer]{6} [sind härechoo]{2}; [zum en uf d Prob stelle]{7}, [händ si]{8} [en]{9} [ufgforderet]{8}, [ine]{15} [es Zeiche]{10} [vom]{11,12} [Himel]{13} [z zeige]{14}.",
 "MAT.16.2": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [zu ine]{5} [gseit]{4}: «[Wänn s Aabig]{6} [wird]{7}, [säged ir]{8}: ‹[Schöns Wätter]{9}! [De Himel]{12,13} [isch]{10} [nämli]{11} [rot]{10}.›",
 "MAT.16.3": "[Und]{1} [am Morge]{2}: ‹[Hüt]{3} [chunnt es Unwätter]{4}; [de Himel]{8,9} [isch]{5} [nämli]{6} [rot]{5} [und trüeb]{7}.› [S Uusgseh]{10,12} [vom Himel]{13,14} [chönd ir]{15} [zwar]{11} [beurteile]{16}, [d Zeiche]{17,19} [vo de Ziite]{20,21} [aber]{18} [chönd ir]{23} [nöd]{22} beurteile.",
 "MAT.16.4": "[E bösi]{2} und{3} [ehebrecherischi]{4} [Generation]{1} [verlangt]{6} [es Zeiche]{5}, und{7} [ere]{11} [wird]{10} [kei]{9} [Zeiche]{8} [ggää]{10} [usser]{12,13} [em Zeiche]{14,15} [vom Jona]{16}.» Und{17} [er hät]{18} [si]{19} [la staa]{18} und [isch furtgange]{20}.",
 "MAT.16.5": "Und{1} [d Jünger]{3,4} [sind]{2} [as]{5,6} [ander Ufer]{7} [choo]{2} und [händ vergässe]{8}, [Broot]{9} [mitznää]{10}.",
 "MAT.16.6": "[De Jesus]{1,3} [aber]{2} [hät]{4} [zu ine]{5} [gseit]{4}: «[Lueged]{6} und{7} [hüeted eu]{8} [vor]{9} [em Suurteig]{10,11} [vo de Pharisäer]{12,13} und{14} [Sadduzäer]{15}!»",
 "MAT.16.7": "[Si]{1} [aber]{2} [händ]{3} [mitenand]{4,5} [überleit]{3} und [gseit]{6}: «[Mir händ]{10} [kei]{9} [Broot]{8} [mitgnoo]{10}.» ~7(ὅτι leitet di diräkt Red ii)",
 "MAT.16.8": "[De Jesus]{3,4} [aber]{2} [hät s gmerkt]{1} und [gseit]{5}: «[Was]{6} [überleged ir]{7} [mitenand]{8,9}, [ir Chliigläubige]{10}, [dass]{11} [ir]{14} [kei]{13} [Broot]{12} [mitgnoo händ]{14}?",
 "MAT.16.9": "[Begriifed ir]{2} [immer no nöd]{1}? [Erinnered ir eu]{4} [au nöd]{3} [a di]{5} [föif]{6} [Broot]{7} [für di]{8} [Föiftuusig]{9} und{10} [wie vil]{11} [Chörb]{12} [ir ufgläse händ]{13}?",
 "MAT.16.10": "[Au nöd]{1} [a di]{2} [sibe]{3} [Broot]{4} [für di]{5} [Viertuusig]{6} und{7} [wie vil]{8} [Chörb]{9} [ir ufgläse händ]{10}?",
 "MAT.16.11": "[Wieso]{1} [begriifed ir]{3} [nöd]{2}, [dass]{4} [ich]{8} [nöd]{5} [vo]{6} [Broot]{7} [zu eu]{9} [gredt han]{8}? [Hüeted eu]{10} [aber]{11} [vor]{12} [em Suurteig]{13,14} [vo de Pharisäer]{15,16} und{17} [Sadduzäer]{18}!»",
 "MAT.16.12": "[Dänn]{1} [händ si]{2} [verstande]{2}, [dass]{3} [er]{5} [nöd]{4} [gseit hät]{5}, [si söled sich]{6} [vor]{7} [em Suurteig]{8,9} [vo de Broot]{10,11} [hüete]{6}, [sondern]{12} [vor]{13} [de Lehr]{14,15} [vo de Pharisäer]{16,17} und{18} [Sadduzäer]{19}.",
 "MAT.16.13": "[Wo]{1} [de Jesus]{3,4} [aber]{2} [i]{5} [d Gäged]{6,7} [vo Cäsarea]{8} [Philippi]{9,10} [choo isch]{1}, [hät er]{11} [sini]{14} [Jünger]{12,13} [gfröget]{11}: «[Wer]{16}, [säged]{17} [d Lüüt]{18,19}, [sig]{20} [de Mänschesohn]{21-24}?» ~15(λέγων «sägend» leitet di diräkt Red ii)",
 "MAT.16.14": "[Si]{1} [aber]{2} [händ gseit]{3}: «[Di einte]{4,5}: [de Johannes]{6} [de Täufer]{7,8}, [anderi]{9} [aber]{10}: [de Elija]{11}, [wider anderi]{12} [aber]{13}: [de Jeremia]{14} [oder]{15} [eine]{16} [vo de]{17} [Prophete]{18}.»",
 "MAT.16.15": "[Er seit]{1} [zu ine]{2}: «[Ir]{3} [aber]{4}, [wer]{5}, [säged ir]{7}, [sig]{8} [ich]{6}?»",
 "MAT.16.16": "[De Simon]{3} [Petrus]{4} [aber]{2} [hät gantwortet]{1} und [gseit]{5}: «[Du]{6} [bisch]{7} [de Christus]{8,9}, [de Sohn]{10,11} [vom läbige]{14,15} [Gott]{12,13}!»",
 "MAT.16.17": "[De Jesus]{3,4} [aber]{2} [hät gantwortet]{1} und [zu ihm]{6} [gseit]{5}: «[Sälig]{7} [bisch du]{8}, [Simon]{9} [Barjona]{10}, [wil]{11} [dir]{17} [nöd]{15} [Fleisch]{12} und{13} [Bluet]{14} [das offebaret hät]{16}, [sondern]{18} [min]{21} [Vatter]{19,20} [i]{22,23} [de Himel]{24,25}.",
 "MAT.16.18": "[Ich]{1} [aber]{2} [säg]{4} [dir]{3} [au]{1}: [Du]{6} [bisch]{7} [de Petrus]{8}, und{9} [uf]{10} [dä]{11} [Felse]{12,13} [wird ich]{14} [mini]{15} [Gmeind]{16,17} [buue]{14}, und{18} [d Tor]{19} [vom Totereich]{20} [wärded]{22} [si]{23} [nöd]{21} [überwältige]{22}. ~5(ὅτι leitet di diräkt Red ii; mit em Doppelpunkt widergää)",
 "MAT.16.19": "[Ich wird]{1} [dir]{2} [d Schlüssel]{3,4} [vom Riich]{5,6} [vo de Himel]{7,8} [gää]{1}, und{9} [was]{10} [du]{12} [au]{11} [uf]{13} [de Ärde]{14,15} [bindsch]{12}, [wird]{16} [i]{18} [de Himel]{19,20} [bunde]{17} [sii]{16}, und{21} [was]{22} [du]{24} [au]{23} [uf]{25} [de Ärde]{26,27} [lösisch]{24}, [wird]{28} [i]{30} [de Himel]{31,32} [glöst]{29} [sii]{28}.»",
 "MAT.16.20": "[Dänn]{1} [hät er]{2} [de Jünger]{3,4} [iigschärft]{2}, [dass]{5} [si]{7} [niemertem]{6} [söled säge]{7}, [dass]{8} [er]{9} [de Christus]{11,12} [sig]{10}.",
 "MAT.16.21": "[Vo dänn aa]{1,2} [hät]{3} [de Jesus]{4,5} [aagfange]{3}, [sine]{9} [Jünger]{7,8} [z zeige]{6}, [dass]{10} [er]{12} [mues]{11} [uf]{13} [Jerusalem]{14} [gaa]{15} und{16} [vo]{19} [de Ältischte]{20,21} und{22} [Hoheprieschter]{23} und{24} [Schriftgelehrte]{25} [vil]{17} [liide]{18} und{26} [umbracht wärde]{27} und{28} [am]{29} [dritte]{30} [Tag]{31} [uferweckt wärde]{32}.",
 "MAT.16.22": "Und{1} [de Petrus]{4,5} [hät]{2} [en]{3} [uf d Siite gnoo]{2} und [hät aagfange]{6}, [en]{8} [zrächtzwiise]{7}: «[Gott bhüet di]{10,11:idiom}, [Herr]{12}! [Das]{17} [passiert]{15} [dir]{16} [sicher nie]{13,14}!» ~9(λέγων «sägend» leitet di diräkt Red ii)",
 "MAT.16.23": "[Er]{1} [aber]{2} [hät sich umdräit]{3} und [zum Petrus]{5,6} [gseit]{4}: «[Gang]{7} [hinder]{8} [mich]{9}, [Satan]{10}! [Du bisch]{12} [mir]{13} [en Fallstrick]{11}, [wil]{14} [du]{16} [nöd]{15} [im Sinn häsch]{16}, [was]{17} [vo Gott]{18,19} isch, [sondern]{20} [was]{21} [vo de Mänsche]{22,23} isch.»",
 "MAT.16.24": "[Dänn]{1} [hät]{4} [de Jesus]{2,3} [zu]{5} [sine]{7} [Jünger]{6} [gseit]{4}: «[Wänn]{8} [öpper]{9} [hinder]{11} [mir]{12} [härchoo]{13} [wott]{10}, [dä söll]{14} [sich sälber]{15} [verleugne]{14} und{16} [sis]{20} [Chrüüz]{18,19} [uf sich nää]{17} und{21} [mir]{23} [nachefolge]{22}.",
 "MAT.16.25": "[Wer]{1} [nämli]{2} [sis]{7} [Läbe]{5,6} [rette]{8} [wott]{4}, [dä wird]{9} [s]{10} [verlüüre]{9}; [wer]{11} [aber]{12} [sis]{17} [Läbe]{15,16} [verlüürt]{14} [wäge]{18} [mir]{19}, [dä wird]{20} [s]{21} [finde]{20}. ~3(ἐάν macht «wer» allgemein; nöd eigens widergää) ~13(ἄν macht «wer» allgemein; nöd eigens widergää)",
 "MAT.16.26": "[Was]{1} [wird s]{3} [emne Mänsch]{4} [nämli]{2} [nütze]{3}, [wänn]{5} [er]{9} [di]{6} [ganz]{8} [Wält]{7} [gwünnt]{9}, [sis]{13} [Läbe]{10,12} [aber]{11} [verlüürt]{14}? [Oder]{15} [was]{16} [wird]{17} [en Mänsch]{18} [als Gägewärt]{19} [für]{20} [sis]{22} [Läbe]{21} [gää]{17}?",
 "MAT.16.27": "[De Mänschesohn]{3-6} [wird]{1} [nämli]{2} [i]{8} [de Herrlichkeit]{9,10} [vo sim]{13} [Vatter]{11,12} [mit]{14} [sine]{17} [Ängel]{15,16} [choo]{7}, und{18} [dänn]{19} [wird er]{20} [jedem]{21} [nach]{22} [sim]{25} [Tue]{23,24} [vergälte]{20}.",
 "MAT.16.28": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Es git]{5} [es paar]{6} [vo dene, wo]{7} [da]{8} [stönd]{9}, [wo]{10} [de Tod]{14} [nöd]{11,12} [wärded schmöcke]{13}, [bis]{15} [si]{17} [de Mänschesohn]{18-21} [gsehnd]{17} [i]{23} [sim]{26} [Riich]{24,25} [choo]{22}.» ~4(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää) ~16(ἄν macht «bis» offe; nöd eigens widergää)",
 # ------------------------------------------------------------ Kapitel 17
 "MAT.17.1": "Und{1} [nach]{2} [sächs]{4} [Täg]{3} [nimmt]{5} [de Jesus]{6,7} [de Petrus]{8,9} und{10} [de Jakobus]{11} und{12} [de Johannes]{13}, [sin]{16} [Brüeder]{14,15}, [mit]{5} und{17} [füert]{18} [si]{19} [uf]{20} [en hööche]{22} [Bärg]{21} [ufe]{18}, [für sich elei]{23,24}.",
 "MAT.17.2": "Und{1} [er isch]{2} [vor]{3} [ine]{4} [verwandlet worde]{2}, und{5} [sis]{9} [Gsicht]{7,8} [hät glüüchtet]{6} [wie]{10} [d Sunne]{11,12}, [sini]{16} [Chleider]{13,15} [aber]{14} [sind]{17} [wiiss]{18} [worde]{17} [wie]{19} [s Liecht]{20,21}.",
 "MAT.17.3": "Und{1} [lueg]{2}, [es sind]{3} [ine]{4} [de Mose]{5} und{6} [de Elija]{7} [erschine]{3} und [händ]{8} [mit]{9} [ihm]{10} [gredt]{8}.",
 "MAT.17.4": "[De Petrus]{3,4} [aber]{2} [hät s Wort gnoo]{1} und [zum Jesus]{6,7} [gseit]{5}: «[Herr]{8}, [es isch]{10} [guet]{9}, [dass mir]{11} [da]{12} [sind]{13}. [Wänn]{14} [du wottsch]{15}, [mach ich]{16} [da]{17} [drüü]{18} [Hütte]{19}: [dir]{20} [eini]{21} und{22} [em Mose]{23} [eini]{24} und{25} [em Elija]{26} [eini]{27}.»",
 "MAT.17.5": "[Wo]{3} [er]{2} [no]{1} [gredt hät]{3}, [lueg]{4}, [e hälli]{6} [Wolche]{5} [hät]{7} [si]{8} [überschattet]{7}, und{9} [lueg]{10}, [e Stimm]{11} [us]{12} [de Wolche]{13,14} [hät gseit]{15}: «[Das]{16} [isch]{17} [min]{20} [Sohn]{18,19}, [de Gliebt]{21,22}, [a]{23} [däm]{24} [ich Freud ha]{25}; [losed uf]{26} [en]{27}!»",
 "MAT.17.6": "Und{1} [wo]{2} [d Jünger]{3,4} [das ghört händ]{2}, [sind si]{5} [uf]{6} [ires]{8} [Gsicht]{7} [gfalle]{5} und{9} [händ sich]{10} [fescht]{11} [gförchtet]{10}.",
 "MAT.17.7": "Und{1} [de Jesus]{3,4} [isch härechoo]{2}, [hät]{6} [si]{7} [aagrüert]{6} und{5} [gseit]{8}: «[Stönd uf]{9} und{10} [förchted eu]{12} [nöd]{11}!»",
 "MAT.17.8": "[Wo si]{1} [aber]{2} [iri]{5} [Auge]{3,4} [ufghebt händ]{1}, [händ si]{7} [niemer]{6} [gseh]{7} [usser]{8,9} [de Jesus]{11} [elei]{12}. ~10(αὐτόν «ihn sälber» hebt de Jesus hervor; nöd eigens widergää)",
 "MAT.17.9": "Und{1} [wo]{2} [si]{3} [vom]{4,5} [Bärg]{6} [abegstige sind]{2}, [hät]{7} [ine]{8} [de Jesus]{9,10} [befole]{7}: «[Verzelled]{13} [niemertem]{12} [vo de Erschiinig]{14,15}, [bis]{16,17} [de Mänschesohn]{18-21} [vo]{22} [de Tote]{23} [uferweckt isch]{24}!» ~11(λέγων «sägend» leitet di diräkt Red ii)",
 "MAT.17.10": "Und{1} [d Jünger]{4,5} [händ]{2} [en]{3} [gfröget]{2}: «[Werum]{7} [säged]{11} [dänn]{8} [d Schriftgelehrti]{9,10}, [dass]{12} [de Elija]{13} [zerscht]{16} [mües]{14} [choo]{15}?» ~6(λέγοντες «sägend» leitet di diräkt Red ii)",
 "MAT.17.11": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: «[De Elija]{5} [chunnt]{7} [scho]{6} und{8} [wird]{9} [alles]{10} [wider in Ornig bringe]{9}.",
 "MAT.17.12": "[Ich säg]{1} [eu]{3} [aber]{2}: [De Elija]{5} [isch]{7} [scho]{6} [choo]{7}, und{8} [si händ]{10} [en]{11} [nöd]{9} [erchännt]{10}, [sondern]{12} [händ]{13} [mit]{14} [ihm]{15} [gmacht]{13}, [was]{16} [si händ wele]{17}. [Eso]{18} [wird]{24} [au]{19} [de Mänschesohn]{20-23} [dur]{26} [si]{27} [liide]{25}.» ~4(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.17.13": "[Dänn]{1} [händ]{2} [d Jünger]{3,4} [verstande]{2}, [dass]{5} [er]{10} [zu ine]{11} [vom]{6} [Johannes]{7}, [em Täufer]{8,9}, [gredt hät]{10}.",
 "MAT.17.14": "Und{1} [wo si]{2} [zu]{3} [de Mängi]{4,5} [choo sind]{2}, [isch]{6} [en Mänsch]{8} [zu ihm]{7} [härechoo]{6}, [isch]{9} [vor ihm]{10} [uf d Chnü gfalle]{9}",
 "MAT.17.15": "und{1} [hät gseit]{2}: «[Herr]{3}, [häb Erbarme]{4} [mit mim]{5} [Sohn]{6,7}, [wil]{8} [er mondsüchtig isch]{9} und{10} [schlimm]{11} [liidet]{12}; [er gheit]{15} [nämli]{14} [vil Mal]{13} [is]{16,17} [Füür]{18} und{19} [vil Mal]{20} [is]{21,22} [Wasser]{23}.",
 "MAT.17.16": "Und{1} [ich ha]{2} [en]{3} [zu]{4} [dine]{6} [Jünger]{5} [brocht]{2}, und{7} [si händ]{9} [en]{10} [nöd]{8} [chöne]{9} [heile]{11}.»",
 "MAT.17.17": "[De Jesus]{3,4} [aber]{2} [hät gantwortet]{1} und [gseit]{5}: «[O]{6} [du ungläubigi]{8} und{9} [verdrähti]{10} [Generation]{7}, [wie lang]{11,12} [söll ich]{15} [bi]{13} [eu]{14} [sii]{15}? [Wie lang]{16,17} [söll ich]{18} [eu]{19} [uushalte]{18}? [Bringed]{20} [en]{22} [mir]{21} [da häre]{23}!»",
 "MAT.17.18": "Und{1} [de Jesus]{4,5} [hät]{2} [en]{3} [aagfahre]{2}, und{6} [de Dämon]{10,11} [isch]{7} [us]{8} [ihm]{9} [usgfahre]{7}, und{12} [de Bueb]{14,15} [isch]{13} [vo]{16} [dere]{19} [Stund]{17,18} [aa]{16} [gheilt worde]{13}.",
 "MAT.17.19": "[Dänn]{1} [sind]{2} [d Jünger]{3,4} [für sich elei]{7,8} [zum Jesus]{5,6} [härechoo]{2} und [händ gseit]{9}: «[Werum]{10,11} [händ]{14} [mir]{12} [en]{16} [nöd]{13} [chöne]{14} [ustriibe]{15}?»",
 "MAT.17.20": "[Er]{1} [aber]{2} [seit]{3} [zu ine]{4}: «[Wäge]{5} [eurem]{8} [Chliiglaube]{6,7}. [Amen]{9}, [ich säg]{11} [eu]{12} [nämli]{10}: [Wänn]{13} [ir]{14} [Glaube]{15} [händ]{14} [wie]{16} [es Senfchorn]{17,18}, [wärded ir]{19} [zu]{20} [dem]{22} [Bärg]{21} [säge]{19}: ‹[Gang]{23} [vo da]{24} [dört äne]{25}!›, und{26} [er wird änegaa]{27}; und{28} [nüüt]{29} [wird]{30} [eu]{31} [unmöglich sii]{30}.»",
 "MAT.17.22": "[Wo]{1} [si]{3} [sich]{1} [aber]{2} [in]{4} [Galiläa]{5,6} [gsammlet händ]{1}, [hät]{7} [de Jesus]{9,10} [zu ine]{8} [gseit]{7}: «[De Mänschesohn]{12-15} [wird]{11} [i]{17} [d Händ]{18} [vo Mänsche]{19} [usgliferet wärde]{16},",
 "MAT.17.23": "und{1} [si wärded]{2} [en]{3} [umbringe]{2}, und{4} [am]{5} [dritte]{6} [Tag]{7} [wird er uferweckt wärde]{8}.» Und{9} [si sind]{10} [fescht]{11} [truurig worde]{10}.",
 "MAT.17.24": "[Wo]{1} [si]{3} [aber]{2} [uf]{4} [Kafarnaum]{5} [choo sind]{1}, [sind]{6} [di]{7} [Iizüger]{10} [vo de]{8} [Doppeldrachme]{9} [zum Petrus]{11,12} [härechoo]{6} und{13} [händ gseit]{14}: «[Zahlt]{19} [eue]{17} [Lehrer]{15,16} [d]{20} [Doppeldrachme]{21} [nöd]{18}?»",
 "MAT.17.25": "[Er seit]{1}: «[Momoll]{2}.» Und{3} [wo er]{4} [is]{5,6} [Huus]{7} [choo isch]{4}, [isch]{8} [ihm]{9} [de Jesus]{10,11} [zvorchoo]{8} und [hät gseit]{12}: «[Was]{13} [meinsch]{15} [du]{14}, [Simon]{16}? [Vo]{21} [wem]{22} [nämed]{23} [d Chünige]{17,18} [vo de Ärde]{19,20} [Zoll]{24} [oder]{25} [Stüür]{26}? [Vo]{27} [ire]{30} [Söön]{28,29} [oder]{31} [vo]{32} [de Frömde]{33,34}?»",
 "MAT.17.26": "[Wo er]{1} [aber]{2} [gseit hät]{1}: «[Vo]{3} [de Frömde]{4,5}», [hät]{6} [de Jesus]{8,9} [zu ihm]{7} [gseit]{6}: «[Also]{10} [sind]{13} [d Söön]{14,15} [doch]{11} [frei]{12}.",
 "MAT.17.27": "[Damit]{1} [mir]{4} [si]{5} [aber]{2} [nöd]{3} [z Fall bringed]{4}, [gang]{6} [a]{7} [de See]{8}, [wirf]{9} [en Angel]{10} [us]{9}, und{11} [de]{12} [erscht]{14} [Fisch]{15}, [wo ufechunnt]{13}, [zieh use]{16}; und{17} [wänn du]{18} [sis]{21} [Muul]{19,20} [ufmachsch]{18}, [findsch]{22} [en Stater]{23}. [Dä]{24} [nimm]{25} und [gib]{26} [ine]{27} [für]{28} [mich]{29} und{30} [dich]{31}.»",
}

# ------------------------------------------------------------------------------------------------ Entscheidungen
DEC_DE = [
 ("MAT.16.1", "traten heran", "literal", "προσελθόντες", None, ["kamen herzu", "traten hinzu"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: προσέρχομαι (bei Matthäus nach MACULA-Lemma 51-mal, oft als Auftakt einer Begegnung) heisst «herantreten, hinzukommen». Die Übersetzung sagt «herantreten» ([[MAT.17.7]], [[MAT.17.14]], [[MAT.17.19]], [[MAT.17.24]]). Mundart «härechoo»."),
 ("MAT.16.1", "um ihn auf die Probe zu stellen", "interpretive", "πειράζοντες", "versuchend", ["um ihn zu versuchen"],
  "πειράζω heisst «prüfen, auf die Probe stellen» und «versuchen»; dasselbe Verb steht für den Versucher in [[MAT.4.1]]–[[MAT.4.3]]. Hier geht es um eine Prüfung mit dem Ziel, Jesus blosszustellen."),
 ("MAT.16.1", "ein Zeichen vom Himmel", "literal", "σημεῖον ἐκ τοῦ οὐρανοῦ", None, ["ein Zeichen von Gott"],
  "«Himmel» kann hier den Ort meinen (ein Zeichen am Himmel) oder umschreibend für Gott stehen (ein von Gott beglaubigendes Zeichen). Die Antwort Jesu spielt mit dem sichtbaren Himmel ([[MAT.16.2]]–[[MAT.16.3]]). Vgl. die Zeichenforderung in [[MAT.12.38]]–[[MAT.12.39]]."),
 ("MAT.16.2", "Wenn es Abend wird", "literal", "Ὀψίας γενομένης", "Als es Abend geworden war", None,
  "Textbefund: [[MAT.16.2]]b–3 («Wenn es Abend wird … nicht beurteilen») steht im SBLGNT im Text. Der SBLGNT-Apparat vermerkt, dass Treg, NA28 und RP die Worte haben und WH sie in doppelte eckige Klammern setzt (in den importierten Variantendatensätzen fehlt dieser Eintrag; deshalb keine Alternative). Nach den CNTR-Transkriptionen fehlen die Worte in 01 und 03; 04, 05 und 032 haben sie. Die einen halten sie für einen späteren Zusatz nach dem Muster von [[LUK.12.54]]–[[LUK.12.56]], andere für ursprünglich und in Gegenden ausgefallen, wo Abendrot kein gutes Wetter ankündigt. Die Übersetzung folgt den SBLGNT-Tokens."),
 ("MAT.16.2", "Schönes Wetter", "literal", "Εὐδία", None, ["Heiteres Wetter"], None),
 ("MAT.16.3", "kommt ein Unwetter", "adapted", "χειμών", "Unwetter", ["Sturm", "schlechtes Wetter"],
  "Der griechische Satz hat kein Verb («Heute Unwetter»); «kommt» ist ergänzt."),
 ("MAT.16.3", "Das Aussehen des Himmels", "literal", "τὸ πρόσωπον τοῦ οὐρανοῦ", "das Angesicht des Himmels", ["den Himmel"],
  "Laut SBLGNT-Apparat ergänzt RP davor «Ihr Heuchler» (ὑποκριταί); der Eintrag fehlt in den importierten Variantendatensätzen. Nach den CNTR-Transkriptionen steht das Wort in keiner der hier transkribierten Handschriften (04, 05, 032), wohl aber in den Ausgaben RP, KJTR und Stephanus."),
 ("MAT.16.3", "könnt ihr nicht beurteilen", "adapted", "οὐ δύνασθε", "könnt ihr nicht", None,
  "Das Verb ist aus dem ersten Satzteil ergänzt. Welche «Zeichen der Zeiten» gemeint sind, sagt der Text nicht; viele denken an das Wirken Jesu (vgl. [[MAT.11.4]]–[[MAT.11.5]])."),
 ("MAT.16.4", "Geschlecht", "traditional", "Γενεὰ", None, ["Generation"],
  "Grundentscheid wie bei Markus: γενεά (bei Matthäus nach MACULA-Lemma 13-mal) «Geschlecht», die Zeitgenossen, oft mit kritischem Unterton (vgl. [[MAT.12.39]], [[MAT.17.17]]). Mundart «Generation»."),
 ("MAT.16.4", "ehebrecherisches", "literal", "μοιχαλὶς", None, ["treuloses"],
  "Prophetisches Bild: Untreue gegen Gott heisst Ehebruch (vgl. [[HOS.2.2]] in KJV-Zählung). Gemeint ist nicht ein Urteil über das Eheleben."),
 ("MAT.16.4", "dem Zeichen des Jona", "interpretive", "τὸ σημεῖον Ἰωνᾶ", None, None,
  "Hier ohne Erklärung. In [[MAT.12.40]]–[[MAT.12.41]] deutet Matthäus das Zeichen auf die drei Tage Jonas im Fisch und auf die Umkehr Ninives; ob hier dasselbe gemeint ist, lässt der Text offen."),
 ("MAT.16.5", "Brote", "literal", "ἄρτους", None, ["Brot"], "Plural: Brotfladen, wie bei den Speisungen ([[MAT.14.17]], [[MAT.15.34]])."),
 ("MAT.16.6", "Sauerteig", "literal", "ζύμης", None, ["Hefe"],
  "Bild für eine unscheinbare, aber alles durchdringende Wirkung. Matthäus deutet es selbst: gemeint ist die Lehre ([[MAT.16.12]]). Markus nennt Pharisäer und Herodes ([[MRK.8.15]]), Matthäus Pharisäer und Sadduzäer."),
 ("MAT.16.7", "Wir haben keine Brote mitgenommen", "interpretive", "ὅτι Ἄρτους οὐκ ἐλάβομεν", None, ["(Das sagt er,) weil wir keine Brote mitgenommen haben"],
  "ὅτι kann die direkte Rede einleiten (so hier) oder begründen: Die Jünger beziehen die Warnung auf das vergessene Brot. Der Sinn bleibt derselbe."),
 ("MAT.16.8", "ihr Kleingläubigen", "literal", "ὀλιγόπιστοι", "ihr Wenig-Glaubenden", ["ihr Glaubensschwachen", "ihr mit eurem kleinen Glauben"],
  "Grundentscheid, vorgeschlagen für das ganze Evangelium: ὀλιγόπιστος (nach MACULA-Lemma bei Matthäus 4-mal: [[MAT.6.30]], [[MAT.8.26]], [[MAT.14.31]], [[MAT.16.8]]) «kleingläubig, ihr Kleingläubigen», ὀλιγοπιστία ([[MAT.17.20]]) «Kleinglaube», πίστις «Glaube». Das Wort ist fast nur bei Matthäus belegt und meint nicht Unglauben, sondern zu wenig Vertrauen bei denen, die Jesus folgen."),
 ("MAT.16.9", "Begreift ihr", "literal", "νοεῖτε", None, ["Versteht ihr"],
  "Unterscheidung wie bei Markus: νοέω «begreifen» ([[MAT.16.9]], [[MAT.16.11]]), συνίημι «verstehen» ([[MAT.16.12]], [[MAT.17.13]])."),
 ("MAT.16.9", "Körbe", "literal", "κοφίνους", None, ["Handkörbe"],
  "Das Griechische unterscheidet wie in den Speisungsberichten κόφινος ([[MAT.14.20]]) und σπυρίς ([[MAT.15.37]], hier [[MAT.16.10]]); beide sind mit «Körbe» übersetzt, der Unterschied der Korbarten wird im Deutschen nicht sichtbar."),
 ("MAT.16.12", "der Lehre", "literal", "τῆς διδαχῆς", None, ["der Unterweisung"],
  "Matthäus löst das Bildwort ausdrücklich auf; Markus lässt es offen ([[MRK.8.21]]). Pharisäer und Sadduzäer vertraten in vielem gegensätzliche Lehren; der Text nennt sie hier als Gegner gemeinsam."),
 ("MAT.16.13", "Cäsarea Philippi", "literal", "Καισαρείας τῆς Φιλίππου", "Cäsarea des Philippus", None,
  "Stadt an den Jordanquellen, vom Tetrarchen Philippus ausgebaut; der Zusatz unterscheidet sie von Cäsarea am Meer. Schreibung wie bei Markus ([[MRK.8.27]])."),
 ("MAT.16.13", "der Menschensohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "der Sohn des Menschen", ["der Mensch"],
  "Einheitliche Wiedergabe für Matthäus. Wo Markus Jesus fragen lässt «Wer, sagen die Leute, sei ich?» ([[MRK.8.27]]), steht bei Matthäus «der Menschensohn»; in [[MAT.16.15]] folgt «ich». Damit zeigt der Text, dass Jesus mit «Menschensohn» von sich selbst spricht."),
 ("MAT.16.14", "Jeremia", "literal", "Ἰερεμίαν", None, None, "Nur Matthäus nennt Jeremia (vgl. [[MAT.2.17]], [[MAT.27.9]])."),
 ("MAT.16.16", "der Christus", "traditional", "ὁ χριστὸς", "der Gesalbte", ["der Messias"],
  "Einheitliche Wiedergabe für Matthäus: χριστός übersetzt hebräisch māšîaḥ «Gesalbter»; mit Artikel ist es hier Titel, kein Name. Ebenso [[MAT.16.20]]."),
 ("MAT.16.16", "der Sohn des lebendigen Gottes", "literal", "ὁ υἱὸς τοῦ θεοῦ τοῦ ζῶντος", None, None,
  "Matthäus erweitert das Bekenntnis gegenüber [[MRK.8.29]]. «Der lebendige Gott» ist eine alttestamentliche Gottesbezeichnung (z. B. [[PSA.42.2]])."),
 ("MAT.16.17", "Selig", "traditional", "Μακάριος", None, ["Glücklich zu preisen", "Wohl dir", "Glückselig"],
  "Grundentscheid, vorgeschlagen für das ganze Evangelium: μακάριος (bei Matthäus nach MACULA-Lemma 13-mal, vor allem in den Seligpreisungen [[MAT.5.3]]–[[MAT.5.11]]) «selig». Das Wort preist jemanden glücklich, weil Gott an ihm handelt; «selig» ist die vertraute Wiedergabe, auch wenn es im heutigen Deutsch oft nach Jenseits oder Gefühl klingt. Mundart «sälig»."),
 ("MAT.16.17", "Barjona", "literal", "Βαριωνᾶ", None, ["Sohn des Jona"],
  "Aramäisch bar Yônâ «Sohn des Jona». In [[JHN.1.42]] heisst der Vater des Simon Johannes; ob «Jona» eine Kurzform davon ist, ist offen."),
 ("MAT.16.17", "Fleisch und Blut", "literal", "σὰρξ καὶ αἷμα", None, ["ein Mensch", "menschliche Einsicht"],
  "Semitische Wendung für den Menschen in seiner Begrenztheit."),
 ("MAT.16.17", "in den Himmeln", "literal", "ἐν τοῖς οὐρανοῖς", None, ["im Himmel"],
  "Plural wie im Griechischen und wie im Vaterunser ([[MAT.6.9]]). Ebenso «in den Himmeln» in [[MAT.16.19]]; das Reich heisst einheitlich «das Reich der Himmel»."),
 ("MAT.16.18", "Petrus", "interpretive", "Πέτρος", "Stein", ["Fels"],
  "Wortspiel: Πέτρος (männlich, «Stein, Fels») und πέτρα (weiblich, «Fels»), aramäisch beides kêp̄āʾ (vgl. Kephas, [[JHN.1.42]]). Im Deutschen geht das Wortspiel verloren, weil der Name als «Petrus» stehen bleibt. Worauf «dieser Felsen» zielt, ist seit alters umstritten: auf Petrus selbst, auf sein Bekenntnis, auf Jesus oder auf Petrus als Bekennenden. Die Übersetzung entscheidet das nicht."),
 ("MAT.16.18", "Gemeinde", "interpretive", "ἐκκλησίαν", "Versammlung", ["Kirche"],
  "Einheitliche Wiedergabe für Matthäus. ἐκκλησία steht in den Evangelien nur bei Matthäus (nach MACULA-Lemma 3-mal: hier und [[MAT.18.17]]). In der griechischen Bibel gibt es das hebräische qāhāl «Versammlung (Israels)» wieder. «Kirche» würde spätere Gestalten der Kirche eintragen."),
 ("MAT.16.18", "die Tore des Totenreichs", "literal", "πύλαι ᾅδου", None, ["die Pforten der Hölle", "die Macht des Todes"],
  "ᾅδης ist das Totenreich (hebräisch šᵉʾôl), nicht der Strafort γέεννα («Hölle», [[MAT.5.22]]). «Tore des Totenreichs» ist ein biblisches Bild für die Macht des Todes ([[ISA.38.10]])."),
 ("MAT.16.18", "überwältigen", "interpretive", "κατισχύσουσιν", "stärker sein als", ["standhalten", "besiegen"],
  "κατισχύω mit Genitiv heisst «die Oberhand gewinnen über». Ob die Tore die Gemeinde angreifen und nicht besiegen oder ob sie dem Ansturm der Gemeinde nicht standhalten, wird verschieden gedeutet."),
 ("MAT.16.19", "die Schlüssel", "literal", "τὰς κλεῖδας", None, None,
  "Bild des Hausverwalters, der öffnet und schliesst (vgl. [[ISA.22.22]]); vgl. auch [[MAT.23.13]]."),
 ("MAT.16.19", "bindest", "interpretive", "δήσῃς", None, ["verbietest"],
  "«Binden» und «lösen» sind in der jüdischen Lehrsprache Begriffe für «verbieten» und «erlauben» (verbindliche Auslegung); andere denken an das Behalten und Vergeben von Sünden (vgl. [[MAT.18.18]], [[JHN.20.23]]) oder an das Binden dämonischer Mächte. Die Übersetzung bleibt beim Bild."),
 ("MAT.16.19", "gebunden", "interpretive", "ἔσται δεδεμένον", "wird gebunden worden sein", ["wird gebunden werden"],
  "Umschreibendes Futur mit Perfektpartizip: Entweder bestätigt der Himmel, was auf der Erde entschieden wird, oder die Entscheidung auf der Erde entspricht dem, was im Himmel schon entschieden ist. «Wird gebunden sein» lässt beides offen. Ebenso «gelöst sein»."),
 ("MAT.16.20", "schärfte er", "interpretive", "διεστείλατο", "gab er Anweisung", ["gebot er streng"],
  "Der SBLGNT liest mit Treg, RP und NA28 διεστείλατο; WH liest ἐπετίμησεν (siehe Alternative)."),
 ("MAT.16.21", "Von da an", "literal", "Ἀπὸ τότε", None, None,
  "Dieselbe Wendung markiert in [[MAT.4.17]] den Beginn der Verkündigung; hier beginnt die Ankündigung des Leidens. Viele sehen darin einen Gliederungseinschnitt des Evangeliums."),
 ("MAT.16.21", "muss", "interpretive", "δεῖ", "es ist nötig", ["es ist bestimmt"],
  "Wie bei Markus ([[MRK.8.31]]): δεῖ drückt eine Notwendigkeit aus, die viele im Willen Gottes und in der Schrift begründet sehen (vgl. [[MAT.26.54]])."),
 ("MAT.16.21", "auferweckt werden", "literal", "ἐγερθῆναι", None, ["auferstehen"],
  "Passiv von ἐγείρω «aufwecken»; Matthäus schreibt so, wo Markus ἀναστῆναι «auferstehen» hat ([[MRK.8.31]]), und sagt «am dritten Tag» statt «nach drei Tagen». Das Passiv nennt keinen Handelnden; viele verstehen es als Handeln Gottes. Einheitlich «auferweckt werden» ([[MAT.17.9]], [[MAT.17.23]]). Nach der CNTR-Transkription liest 05 hier «nach drei Tagen auferstehen» wie Markus; der SBLGNT-Apparat verzeichnet das nicht."),
 ("MAT.16.22", "zurechtzuweisen", "literal", "ἐπιτιμᾶν", "anzufahren", ["Vorwürfe zu machen"],
  "Dasselbe Verb steht für Jesus gegenüber dem Dämon in [[MAT.17.18]] («drohte»). Die Wiedergaben wechseln mit dem Zusammenhang wie bei Markus."),
 ("MAT.16.22", "Gott bewahre dich", "adapted", "Ἵλεώς σοι", "Gnädig dir", ["Das sei fern von dir", "Gott behüte"],
  "Feste Wendung, verkürzt aus «(Gott sei) dir gnädig»: eine abwehrende Beteuerung. Wörtlich übersetzt wäre sie unverständlich."),
 ("MAT.16.22", "niemals", "literal", "οὐ μὴ", None, ["gewiss nicht"], "Doppelte Verneinung mit Konjunktiv bzw. Futur: nachdrückliches Nein."),
 ("MAT.16.23", "Geh hinter mich", "literal", "Ὕπαγε ὀπίσω μου", None, ["Weg mit dir", "Tritt hinter mich"],
  "Wie bei Markus ([[MRK.8.33]]): ὀπίσω μου «hinter mich» steht auch im folgenden Vers («hinter mir herkommen»); Petrus wird an den Platz des Nachfolgenden gewiesen. Mit «Geh weg, Satan» weist Jesus in [[MAT.4.10]] den Versucher ab (dort ohne ὀπίσω μου)."),
 ("MAT.16.23", "ein Fallstrick", "interpretive", "σκάνδαλον", None, ["ein Stolperstein", "ein Anstoss", "ein Ärgernis"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: σκάνδαλον «Fallstrick». Das Wort ist ursprünglich das Stellholz einer Falle, dann das, woran man zu Fall kommt. Petrus will Jesus vom Weg ins Leiden abhalten und wird ihm so zur Falle. «Stolperstein» liesse den Gegensatz zum Felsen von [[MAT.16.18]] hörbar werden (der eben noch Fels genannt wurde, wird zum Stein, über den man stolpert); der Text betont aber das Bild der Falle nicht eigens. Zum Wortfeld σκανδαλίζω siehe [[MAT.17.27]]."),
 ("MAT.16.23", "im Sinn", "literal", "φρονεῖς", "denkst", ["trachtest nach"], None),
 ("MAT.16.24", "hinter mir herkommen", "literal", "ὀπίσω μου ἐλθεῖν", None, ["mir nachfolgen"], None),
 ("MAT.16.24", "der verleugne sich selbst", "literal", "ἀπαρνησάσθω ἑαυτὸν", None, ["der sage sich los von sich selbst"],
  "Dasselbe Verb steht für die Verleugnung des Petrus ([[MAT.26.34]], [[MAT.26.75]]). Gemeint ist, nicht mehr sich selbst zum Massstab zu machen."),
 ("MAT.16.25", "Leben", "interpretive", "ψυχὴν", "Seele", ["sich selbst", "das Selbst"],
  "Wie bei Markus ([[MRK.8.35]]): ψυχή umfasst das natürliche Leben und das Selbst; in [[MAT.16.25]]–[[MAT.16.26]] durchgehend «Leben», damit das Wortspiel retten/verlieren/finden erhalten bleibt."),
 ("MAT.16.26", "einbüsst", "literal", "ζημιωθῇ", "Schaden nimmt an", ["verliert"], "Kaufmannssprache: Gewinn (κερδήσῃ) und Verlust."),
 ("MAT.16.27", "der Menschensohn wird", "interpretive", "μέλλει", "ist im Begriff", ["soll"],
  "μέλλω mit Infinitiv bezeichnet etwas Bevorstehendes, oft mit dem Ton der Gewissheit. Ebenso [[MAT.17.12]] und [[MAT.17.22]]."),
 ("MAT.16.27", "nach seinem Tun vergelten", "literal", "ἀποδώσει ἑκάστῳ κατὰ τὴν πρᾶξιν αὐτοῦ", None, None,
  "Anklang an [[PSA.62.12]] und [[PRO.24.12]]."),
 ("MAT.16.28", "den Tod nicht schmecken werden", "literal", "οὐ μὴ γεύσωνται θανάτου", None, ["nicht sterben werden"],
  "Semitische Wendung für «sterben»; wie bei Markus ([[MRK.9.1]])."),
 ("MAT.16.28", "in seinem Reich kommen", "interpretive", "ἐρχόμενον ἐν τῇ βασιλείᾳ αὐτοῦ", None, ["mit seiner Königsherrschaft kommen"],
  "Worauf sich das Wort bezieht, ist umstritten: auf die unmittelbar folgende Verwandlung ([[MAT.17.1]]–[[MAT.17.8]]), auf Auferstehung und Sendung ([[MAT.28.18]]), auf das Gericht über Jerusalem oder auf das Kommen am Ende. Markus sagt «das Reich Gottes in Kraft» ([[MRK.9.1]]), Matthäus spricht vom Menschensohn und seinem Reich. Die Übersetzung legt sich nicht fest."),
 ("MAT.17.1", "nimmt", "literal", "παραλαμβάνει", None, None,
  "Erzählendes Präsens (auch «führt»), wie im Griechischen beibehalten."),
 ("MAT.17.1", "für sich allein", "literal", "κατʼ ἰδίαν", None, ["abseits"], "Ebenso [[MAT.17.19]]."),
 ("MAT.17.2", "verwandelt", "literal", "μετεμορφώθη", None, ["verklärt"],
  "Wie bei Markus ([[MRK.9.2]]): μεταμορφόω «umgestalten»; das Passiv nennt keinen Handelnden. «Verklärung» ist die traditionelle Bezeichnung des Ereignisses."),
 ("MAT.17.2", "leuchtete wie die Sonne", "literal", "ἔλαμψεν τὸ πρόσωπον αὐτοῦ ὡς ὁ ἥλιος", None, None,
  "Nur Matthäus erwähnt das leuchtende Gesicht; viele erinnern an Mose ([[EXO.34.29]]) und an [[MAT.13.43]]."),
 ("MAT.17.3", "siehe", "literal", "ἰδοὺ", None, ["sieh", "da"],
  "Einheitliche Wiedergabe für Matthäus: ἰδού «siehe», Mundart «lueg». Matthäus braucht das Wort oft, um etwas Unerwartetes einzuführen ([[MAT.17.5]] zweimal)."),
 ("MAT.17.3", "es erschienen", "adapted", "ὤφθη", "wurde gesehen", ["zeigten sich"],
  "Verb im Singular vor zwei Subjekten, im Griechischen möglich; im Deutschen Plural. RP liest den Plural ὤφθησαν; die Übersetzung ändert sich dadurch nicht."),
 ("MAT.17.4", "ergriff das Wort", "adapted", "ἀποκριθεὶς", "antwortend", ["hob an"],
  "ἀποκρίνομαι heisst auch ohne vorangehende Frage «das Wort ergreifen»; wie bei Markus ([[MRK.9.5]])."),
 ("MAT.17.4", "Herr", "literal", "Κύριε", None, ["Meister"],
  "Markus hat «Rabbi» ([[MRK.9.5]]). κύριε kann höfliche Anrede («Herr») oder Bekenntnis sein; bei Matthäus reden die Jünger Jesus so an (z. B. [[MAT.8.25]], [[MAT.14.28]])."),
 ("MAT.17.4", "werde ich", "literal", "ποιήσω", None, ["will ich"],
  "Der SBLGNT liest die erste Person Singular; Treg und RP lesen «wollen wir machen» (siehe Alternative)."),
 ("MAT.17.4", "Hütten", "literal", "σκηνάς", None, ["Zelte", "Laubhütten"],
  "σκηνή «Zelt, Hütte»; manche hören einen Anklang an das Laubhüttenfest oder an das Zelt der Begegnung."),
 ("MAT.17.5", "eine lichte Wolke", "literal", "νεφέλη φωτεινὴ", None, ["eine leuchtende Wolke"],
  "Die Wolke ist in der Bibel Zeichen der Gegenwart Gottes ([[EXO.24.15]]–[[EXO.24.16]], [[EXO.40.34]])."),
 ("MAT.17.5", "der Geliebte", "literal", "ὁ ἀγαπητός", None, ["der Einzige"], "Wie bei der Taufe ([[MAT.3.17]])."),
 ("MAT.17.5", "an dem ich Gefallen gefunden habe", "adapted", "εὐδόκησα", "an dem ich Gefallen fand", ["an dem ich Freude habe", "den ich erwählt habe"],
  "Aorist, wohl im Sinn einer gültigen Entscheidung; mit Perfekt wiedergegeben. Gleicher Wortlaut wie bei der Taufe ([[MAT.3.17]]); Anklang an [[ISA.42.1]]."),
 ("MAT.17.5", "hört auf ihn", "literal", "ἀκούετε αὐτοῦ", None, ["gehorcht ihm"], "Anklang an [[DEU.18.15]] (der Prophet wie Mose)."),
 ("MAT.17.6", "fielen sie auf ihr Gesicht", "literal", "ἔπεσαν ἐπὶ πρόσωπον αὐτῶν", None, ["warfen sich nieder"],
  "Nur Matthäus erzählt Niederfallen und Furcht nach der Stimme; Gebärde der Ehrfurcht und des Erschreckens."),
 ("MAT.17.7", "Steht auf", "literal", "Ἐγέρθητε", None, None,
  "Dasselbe Verb ἐγείρω steht für die Auferweckung ([[MAT.17.9]], [[MAT.17.23]]); im Deutschen nicht nachzuahmen."),
 ("MAT.17.8", "ausser Jesus allein", "adapted", "εἰ μὴ αὐτὸν Ἰησοῦν μόνον", "ausser ihn selbst, Jesus, allein", ["ausser Jesus selbst"],
  "αὐτόν («ihn selbst») hebt Jesus hervor und ist der Lesbarkeit halber nicht eigens übersetzt. Treg und RP lesen τόν statt αὐτόν; die Übersetzung ändert sich dadurch nicht."),
 ("MAT.17.9", "von der Erscheinung", "interpretive", "τὸ ὅραμα", "das Geschaute", ["von der Vision", "von dem, was ihr gesehen habt"],
  "ὅραμα ist «was man sieht», auch die von Gott gewährte Schau ([[ACT.10.17]]). «Erscheinung» lässt offen, ob es ein äusseres oder inneres Sehen war."),
 ("MAT.17.9", "auferweckt ist", "literal", "ἐγερθῇ", None, ["auferstanden ist"], "RP liest ἀναστῇ «auferstanden ist» (siehe Alternative)."),
 ("MAT.17.10", "die Schriftgelehrten", "traditional", "οἱ γραμματεῖς", None, ["die Schriftkundigen", "die Gesetzeslehrer"],
  "Einheitliche Wiedergabe für Matthäus: γραμματεῖς sind Kenner und Ausleger der Schrift."),
 ("MAT.17.11", "wird alles wiederherstellen", "literal", "ἀποκαταστήσει πάντα", None, ["wird alles in Ordnung bringen"],
  "Anklang an die Erwartung des wiederkommenden Elija ([[MAL.4.5]]–[[MAL.4.6]] in KJV-Zählung). Futur, wo Markus Präsens hat ([[MRK.9.12]])."),
 ("MAT.17.12", "mit ihm gemacht, was sie wollten", "literal", "ἐποίησαν ἐν αὐτῷ ὅσα ἠθέλησαν", "an ihm getan, so viel sie wollten", None,
  "Anspielung auf die Hinrichtung Johannes des Täufers ([[MAT.14.3]]–[[MAT.14.12]]); der folgende Vers sagt das ausdrücklich."),
 ("MAT.17.12", "wird auch der Menschensohn durch sie leiden", "interpretive", "μέλλει πάσχειν ὑπʼ αὐτῶν", "ist im Begriff, von ihnen zu leiden", ["wird von ihnen leiden müssen"],
  "ὑπό nennt die Urheber des Leidens; «durch sie» hält fest, dass es dieselben sind, die mit Elija machten, was sie wollten."),
 ("MAT.17.13", "von Johannes dem Täufer", "literal", "περὶ Ἰωάννου τοῦ βαπτιστοῦ", None, None,
  "Matthäus sagt ausdrücklich, was Markus nur andeutet (vgl. [[MAT.11.14]]). Der Satz ist Erzählerkommentar über das Verstehen der Jünger."),
 ("MAT.17.14", "fiel vor ihm auf die Knie", "literal", "γονυπετῶν αὐτὸν", "ihm kniefallend", None, None),
 ("MAT.17.15", "erbarme dich", "literal", "ἐλέησόν", None, ["hab Erbarmen mit"],
  "Bitte, wie sie in [[MAT.9.27]], [[MAT.15.22]] und [[MAT.20.30]] an Jesus gerichtet wird (liturgisch «Kyrie eleison»)."),
 ("MAT.17.15", "er ist mondsüchtig", "interpretive", "σεληνιάζεται", "er ist vom Mond getroffen", ["er ist epileptisch", "er hat Anfälle"],
  "σεληνιάζομαι (von σελήνη «Mond») gibt die antike Vorstellung wieder, der Mond verursache Anfälle. Die geschilderten Zeichen erinnern viele an Epilepsie; der Text spricht anschliessend von einem Dämon ([[MAT.17.18]]). Die Übersetzung bleibt beim antiken Wort und stellt keine heutige Diagnose; ebenso in [[MAT.4.24]]."),
 ("MAT.17.15", "leidet schwer", "literal", "κακῶς πάσχει", None, ["ist übel dran"],
  "Der SBLGNT liest mit NA28 und RP πάσχει; WH und Treg lesen ἔχει «hat es schlimm» (siehe Alternative)."),
 ("MAT.17.17", "ungläubiges", "literal", "ἄπιστος", None, ["treuloses"],
  "ἄπιστος «ohne Glauben, ohne Vertrauen»; wie bei Markus ([[MRK.9.19]]). Vgl. ὀλιγοπιστία in [[MAT.17.20]]."),
 ("MAT.17.17", "verkehrtes", "literal", "διεστραμμένη", "verdrehtes", ["irregeleitetes"], "Anklang an [[DEU.32.5]] in der griechischen Übersetzung."),
 ("MAT.17.17", "werde ich bei euch sein", "literal", "μεθʼ ὑμῶν ἔσομαι", None, ["soll ich bei euch sein"],
  "Futur wie im Griechischen; Markus hat dieselben Verben ([[MRK.9.19]]), dort mit «soll ich» wiedergegeben."),
 ("MAT.17.18", "drohte", "interpretive", "ἐπετίμησεν", "fuhr an", ["gebot", "wies zurecht"],
  "Bei Austreibungen der machtvolle Befehl (wie [[MRK.9.25]]). αὐτῷ («ihm») ist nach MACULA sächlich bestimmt und meint den Dämon, nicht den Jungen; im Deutschen ist «ihm» beides möglich."),
 ("MAT.17.18", "der Dämon", "literal", "τὸ δαιμόνιον", None, ["der böse Geist"], "Einheitliche Wiedergabe für Matthäus: δαιμόνιον «Dämon»."),
 ("MAT.17.18", "der Junge", "literal", "ὁ παῖς", None, ["der Knabe", "das Kind"], "παῖς «Kind, Junge», auch «Diener»; hier der Sohn ([[MAT.17.15]])."),
 ("MAT.17.20", "Kleinglaubens", "literal", "ὀλιγοπιστίαν", None, ["kleinen Glaubens"],
  "Siehe [[MAT.16.8]]. RP liest ἀπιστίαν «Unglaubens» (siehe Alternative)."),
 ("MAT.17.20", "ein Senfkorn", "literal", "κόκκον σινάπεως", "ein Korn von Senf", None,
  "Sprichwörtlich kleinstes Samenkorn (vgl. [[MAT.13.31]]–[[MAT.13.32]]). Der Vergleich zielt auf die Kleinheit: schon ein winziger Glaube genügt."),
 ("MAT.17.20", "Geh von hier nach dort", "literal", "Μετάβα ἔνθεν ἐκεῖ", None, ["Rück von hier dorthin"], "Bildwort für das unmöglich Scheinende (vgl. [[MAT.21.21]])."),
 ("MAT.17.22", "sammelten", "interpretive", "Συστρεφομένων", "sich zusammendrängten", ["zusammen unterwegs waren", "sich aufhielten"],
  "συστρέφομαι «sich zusammenschliessen, sich sammeln». RP liest Ἀναστρεφομένων «als sie sich aufhielten» (siehe Alternative)."),
 ("MAT.17.22", "ausgeliefert werden", "interpretive", "παραδίδοσθαι", "übergeben werden", ["verraten werden", "preisgegeben werden"],
  "Wie bei Markus ([[MRK.9.31]]): παραδίδωμι steht für das Ausliefern durch Judas ([[MAT.26.15]]), durch die Führer an Pilatus ([[MAT.27.2]]) und kann zugleich an Gottes Handeln denken lassen."),
 ("MAT.17.23", "sehr traurig", "literal", "ἐλυπήθησαν σφόδρα", None, None,
  "Matthäus erzählt Trauer, wo Markus Unverständnis und Furcht nennt ([[MRK.9.32]])."),
 ("MAT.17.24", "Doppeldrachme", "interpretive", "τὰ δίδραχμα", "die Doppeldrachmen", ["die Tempelsteuer", "die Steuer"],
  "Die Doppeldrachme entsprach dem halben Schekel, den jüdische Männer jährlich für den Tempel entrichteten ([[EXO.30.13]]); die meisten Ausleger verstehen die Abgabe deshalb als Tempelsteuer. Der Text sagt «Tempel» nicht; die Übersetzung behält den Münznamen, im Singular, weil eine Person je eine Doppeldrachme schuldete."),
 ("MAT.17.24", "Lehrer", "literal", "διδάσκαλος", None, ["Meister"], None),
 ("MAT.17.25", "Doch", "adapted", "Ναί", "Ja", None,
  "Auf eine verneinte Frage («Zahlt … nicht?») antwortet das Deutsche zustimmend mit «doch»."),
 ("MAT.17.25", "kam Jesus ihm zuvor", "literal", "προέφθασεν αὐτὸν ὁ Ἰησοῦς", None, ["sprach Jesus ihn zuerst an"],
  "Jesus spricht an, bevor Petrus etwas sagen kann; der Text lässt erkennen, dass Jesus von dem Gespräch weiss."),
 ("MAT.17.25", "Zoll oder Steuer", "literal", "τέλη ἢ κῆνσον", None, ["Abgaben oder Kopfsteuer"],
  "τέλη sind Zölle und indirekte Abgaben, κῆνσος (lateinisch census) die Kopfsteuer."),
 ("MAT.17.25", "Söhnen", "literal", "υἱῶν", None, ["Kindern", "eigenen Leuten"],
  "Gemeint sind die Angehörigen des Königshauses, im Gegensatz zu den Fremden (den Untertanen); «Söhne» bleibt wegen [[MAT.17.26]]."),
 ("MAT.17.26", "Also sind die Söhne doch frei", "interpretive", "Ἄρα γε ἐλεύθεροί εἰσιν οἱ υἱοί", None, ["Dann sind ja die Söhne frei"],
  "Die Folgerung überträgt das Bild: Wenn die Abgabe Gott gilt, sind die Söhne des Königs, Jesus und wohl auch die Seinen, davon frei. Wie weit das auf die Jünger zielt, wird verschieden gedeutet. RP lässt hier Petrus ausdrücklich antworten (siehe Alternative)."),
 ("MAT.17.27", "zu Fall bringen", "literal", "σκανδαλίσωμεν", None, ["ihnen keinen Anstoss geben", "sie nicht vor den Kopf stossen", "ihnen kein Ärgernis geben"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: σκανδαλίζω (nach MACULA-Lemma bei Matthäus 14-mal) aktiv «zu Fall bringen», passiv gegenüber einer Person «Anstoss nehmen an», sonst «zu Fall kommen»; σκάνδαλον «Fallstrick» ([[MAT.16.23]]). Hier geht es wohl darum, die Einnehmer nicht zu verärgern und ihnen keinen Grund zur Ablehnung zu geben; deutsch läge «keinen Anstoss geben» näher. Die einheitliche Wiedergabe hält die Verbindung zu den übrigen Stellen sichtbar."),
 ("MAT.17.27", "den See", "adapted", "θάλασσαν", "das Meer", None, "Gemeint ist der See Gennesaret bei Kafarnaum."),
 ("MAT.17.27", "einen Stater", "literal", "στατῆρα", None, ["ein Vierdrachmenstück", "eine Silbermünze"],
  "Silbermünze im Wert von vier Drachmen, also die Abgabe für zwei Personen."),
 ("MAT.17.27", "für mich und dich", "literal", "ἀντὶ ἐμοῦ καὶ σοῦ", "anstelle von mir und dir", None,
  "Die Erzählung endet mit dem Auftrag; dass Petrus ihn ausführt, wird nicht erzählt."),
]

DEC_GSW = [
 ("MAT.16.1", "sind härechoo", "literal", "προσελθόντες", None, ["sind zue choo"],
  "Einheitlich fürs Matthäusevangelium: προσέρχομαι «härechoo» (bim Matthäus 51-mal)."),
 ("MAT.16.1", "zum en uf d Prob stelle", "interpretive", "πειράζοντες", "versuechend", ["zum en versueche"],
  "Gliich Verb wie bim Versuecher ([[MAT.4.1]])."),
 ("MAT.16.2", "Wänn s Aabig", "literal", "Ὀψίας γενομένης", None, None,
  "Textbefund: [[MAT.16.2]]b–3 staat im SBLGNT im Text. Im SBLGNT-Apparat staat, dass WH d Wort i doppleti eckigi Chlammere setzt (i de importierte Variante-Datesätz fehlt dä Iitrag, drum kei Alternative). Nach de CNTR-Transkriptione fehled d Wort i 01 und 03; 04, 05 und 032 händ si. D Übersetzig folgt em SBLGNT."),
 ("MAT.16.3", "S Uusgseh", "literal", "τὸ πρόσωπον", "S Gsicht", None,
  "Nach em SBLGNT-Apparat setzt RP «Ir Hüüchler» devor; dä Iitrag fehlt i de importierte Datesätz."),
 ("MAT.16.3", "chönd ir nöd beurteile", "adapted", "οὐ δύνασθε", "chönd ir nöd", None, "S Verb isch us em erschte Satzteil ergänzt."),
 ("MAT.16.4", "Generation", "adapted", "Γενεὰ", None, ["Gschlächt"],
  "Wie bim Markus: γενεά «Generation», d Ziitgenosse; «Gschlächt» tönt i de Mundart altmodisch."),
 ("MAT.16.4", "ehebrecherischi", "literal", "μοιχαλὶς", None, ["untreui"], "Prophetischs Bild: Untreui gäge Gott heisst Ehebruch."),
 ("MAT.16.4", "la staa", "adapted", "καταλιπὼν", "verlaa", None, "«verlaa» isch i de Mundart unüblich; «la staa» wie bim Markus ([[MRK.8.13]])."),
 ("MAT.16.6", "Suurteig", "literal", "ζύμης", None, ["Hefe"], "De Matthäus düütet s Bild sälber: gmeint isch d Lehr ([[MAT.16.12]])."),
 ("MAT.16.8", "ir Chliigläubige", "literal", "ὀλιγόπιστοι", None, ["ir mit eurem chliine Glaube"],
  "Grundentscheid, vorgschlage fürs ganz Evangelium: ὀλιγόπιστος «chliigläubig», ὀλιγοπιστία «Chliiglaube», πίστις «Glaube». Nöd Unglaube, sondern z wenig Vertroue."),
 ("MAT.16.9", "Chörb", "literal", "κοφίνους", None, None, "S Griechisch underscheidet zwei Chorbarte (κόφινος, σπυρίς); beidi sind «Chörb»."),
 ("MAT.16.13", "de Mänschesohn", "traditional", "τὸν υἱὸν τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None,
  "Iiheitlichi Widergaab fürs Matthäusevangelium. Wo s bim Markus «ich» heisst ([[MRK.8.27]]), staat da «de Mänschesohn»."),
 ("MAT.16.16", "de Christus", "traditional", "ὁ χριστὸς", "de Gsalbt", ["de Messias"], "Titel, nöd Name."),
 ("MAT.16.16", "vom läbige Gott", "literal", "τοῦ θεοῦ τοῦ ζῶντος", None, None, "Kei Genitiv i de Mundart: «vo» mit Dativ."),
 ("MAT.16.17", "Sälig", "traditional", "Μακάριος", None, ["Glücklich", "Wohl dir"],
  "Grundentscheid, vorgschlage fürs ganz Evangelium: μακάριος «sälig». S Wort prieset öpper glücklich, wil Gott a ihm handlet."),
 ("MAT.16.17", "Barjona", "literal", "Βαριωνᾶ", None, ["Sohn vom Jona"], "Aramäisch bar Yônâ «Sohn vom Jona»."),
 ("MAT.16.17", "i de Himel", "literal", "ἐν τοῖς οὐρανοῖς", None, None, "Mehrzahl wie im Griechische und wie im Unservatter ([[MAT.6.9]])."),
 ("MAT.16.18", "de Petrus", "interpretive", "Πέτρος", "Stei", ["Fels"],
  "Wortspiil: Πέτρος «Stei, Fels» und πέτρα «Felse», aramäisch beides kêp̄āʾ. Wohii «dä Felse» zielt (de Petrus sälber, sis Bekänntnis, de Jesus), isch umstritte; d Übersetzig entscheidet das nöd."),
 ("MAT.16.18", "Gmeind", "interpretive", "ἐκκλησίαν", "Versammlig", ["Chile"],
  "Iiheitlichi Widergaab fürs Matthäusevangelium. «Chile» würd spööteri Forme vo de Chile iiträge."),
 ("MAT.16.18", "d Tor vom Totereich", "literal", "πύλαι ᾅδου", None, ["d Macht vom Tod"],
  "ᾅδης isch s Totereich, nöd d Höll (γέεννα)."),
 ("MAT.16.18", "wird ich", "literal", "οἰκοδομήσω", None, ["buu ich"], "Futur; i de Mundart wär au s Präsens müglich."),
 ("MAT.16.19", "bindsch", "interpretive", "δήσῃς", None, ["verbüütsch"],
  "«Binde» und «löse» sind i de jüdische Lehrsprach Wort für «verbüüte» und «erlaube»; anderi tänked as Vergää vo Sünde ([[MAT.18.18]], [[JHN.20.23]])."),
 ("MAT.16.19", "bunde", "interpretive", "ἔσται δεδεμένον", None, None,
  "Futur mit Perfektpartizip: Entweder bestätiget de Himel, was uf de Ärde entschide wird, oder s entspricht dem, wo im Himel scho entschide isch."),
 ("MAT.16.21", "uferweckt wärde", "literal", "ἐγερθῆναι", None, ["uferstaa"],
  "Passiv, wo de Markus «uferstaa» hät ([[MRK.8.31]]); iiheitlich «uferweckt wärde»."),
 ("MAT.16.21", "umbracht wärde", "adapted", "ἀποκτανθῆναι", "tötet wärde", None, "Wie bim Markus «umbringe» für ἀποκτείνω ([[MRK.9.31]])."),
 ("MAT.16.22", "Gott bhüet di", "adapted", "Ἵλεώς σοι", "Gnädig dir", ["Das söll nöd sii"],
  "Feschti Wändig, abwehrend; «Gott bhüet di» isch i de Mundart s natürlichi Gägestück."),
 ("MAT.16.23", "Gang hinder mich", "literal", "Ὕπαγε ὀπίσω μου", None, ["Gang mer us de Auge"], "Wie bim Markus ([[MRK.8.33]])."),
 ("MAT.16.23", "en Fallstrick", "interpretive", "σκάνδαλον", None, ["en Stolperstei", "en Aastoss"],
  "Einheitlich fürs Matthäusevangelium: σκάνδαλον «Fallstrick», ursprünglich s Stellhölzli vo nere Falle. De Petrus wott de Jesus vom Wäg is Liide abhalte und wird ihm so zur Falle. «Stolperstei» liess de Gägesatz zum Felse vo [[MAT.16.18]] ghööre."),
 ("MAT.16.25", "Läbe", "interpretive", "ψυχὴν", "Seel", ["sich sälber"], "Wie bim Markus: ψυχή isch s Läbe und s Sälbscht; überall «Läbe»."),
 ("MAT.16.27", "vergälte", "literal", "ἀποδώσει", None, None, "Aaklang a [[PSA.62.12]] und [[PRO.24.12]]."),
 ("MAT.16.28", "de Tod nöd wärded schmöcke", "literal", "οὐ μὴ γεύσωνται θανάτου", None, ["nöd stärbe"], "Semitischi Wändig für «stärbe»."),
 ("MAT.16.28", "i sim Riich choo", "interpretive", "ἐρχόμενον ἐν τῇ βασιλείᾳ αὐτοῦ", None, None,
  "Worum s gaat (Verwandlig, Uferstehig, Gricht, Wiederkunft), isch umstritte; d Übersetzig leit sich nöd fescht."),
 ("MAT.17.2", "verwandlet worde", "literal", "μετεμορφώθη", None, ["verklärt worde"], "S Passiv seit nöd, wer handlet."),
 ("MAT.17.3", "lueg", "literal", "ἰδοὺ", "lueg emal", None, "Iiheitlichi Widergaab fürs Matthäusevangelium: ἰδού «lueg»."),
 ("MAT.17.4", "hät s Wort gnoo", "adapted", "ἀποκριθεὶς", "hät gantwortet", None, "ἀποκρίνομαι au ohni Frag: «s Wort nää»."),
 ("MAT.17.4", "mach ich", "adapted", "ποιήσω", "wird ich mache", None, "Futur mit Präsens widergää, wie s i de Mundart üblich isch."),
 ("MAT.17.5", "e hälli Wolche", "literal", "νεφέλη φωτεινὴ", None, ["e lüüchtigi Wolche"], "D Wolche isch Zeiche vo de Gägewart vo Gott ([[EXO.40.34]])."),
 ("MAT.17.5", "a däm ich Freud ha", "adapted", "εὐδόκησα", "a däm ich Gfalle gfunde ha", None,
  "Aorist, i de Mundart mit Präsens widergää; gliich wie bi de Taufi ([[MAT.3.17]])."),
 ("MAT.17.5", "losed uf en", "literal", "ἀκούετε αὐτοῦ", None, None, "«lose» isch s Mundartwort für «zuehöre»; Aaklang a [[DEU.18.15]]."),
 ("MAT.17.8", "usser de Jesus elei", "adapted", "εἰ μὴ αὐτὸν Ἰησοῦν μόνον", "usser ihn sälber, de Jesus, elei", None, "αὐτόν isch nöd eigens übersetzt."),
 ("MAT.17.9", "vo de Erschiinig", "interpretive", "τὸ ὅραμα", None, ["vo dem, wo ir gseh händ"], None),
 ("MAT.17.15", "er mondsüchtig isch", "interpretive", "σεληνιάζεται", None, ["er hät Aafäll"],
  "Antiki Vorstellig, de Mond verursachi Aafäll; d Übersetzig stellt kei hüütigi Diagnose."),
 ("MAT.17.15", "gheit", "adapted", "πίπτει", "fallt", None, "«ghei» isch i de Züri Mundart s gwöhnlich Wort für «falle»."),
 ("MAT.17.17", "söll ich", "adapted", "ἔσομαι", "wird ich", None, "Futur, wie bim Markus mit «söll» widergää ([[MRK.9.19]])."),
 ("MAT.17.18", "aagfahre", "interpretive", "ἐπετίμησεν", None, ["befole"], "Wie bim Markus ([[MRK.9.25]]); «en» meint de Dämon."),
 ("MAT.17.18", "de Bueb", "literal", "ὁ παῖς", None, ["s Chind"], None),
 ("MAT.17.20", "Chliiglaube", "literal", "ὀλιγοπιστίαν", None, None, "Lueg [[MAT.16.8]]."),
 ("MAT.17.20", "es Senfchorn", "literal", "κόκκον σινάπεως", None, None, "S sprichwörtlich chliinscht Chorn ([[MAT.13.31]])."),
 ("MAT.17.24", "Doppeldrachme", "interpretive", "τὰ δίδραχμα", None, ["Tämpelstüür"],
  "Entspricht em halbe Schekel für de Tämpel ([[EXO.30.13]]); de Text seit «Tämpel» aber nöd."),
 ("MAT.17.24", "Iizüger", "literal", "λαμβάνοντες", "die, wo iizieh", None, None),
 ("MAT.17.25", "Momoll", "adapted", "Ναί", "Ja", ["Doch"], "Uf e verneinti Frag seit me i de Mundart «momoll» oder «doch»."),
 ("MAT.17.25", "Chünige", "literal", "βασιλεῖς", None, None, None),
 ("MAT.17.27", "z Fall bringed", "literal", "σκανδαλίσωμεν", None, ["vor de Chopf stossed", "Aastoss gänd"],
  "Einheitlich fürs Matthäusevangelium: σκανδαλίζω aktiv «z Fall bringe», passiv «Aastoss nää» oder «z Fall choo»; σκάνδαλον «Fallstrick». Da isch wohl gmeint, d Iizüger nöd z verärgere («vor de Chopf stosse»)."),
 ("MAT.17.27", "findsch", "adapted", "εὑρήσεις", "wirsch finde", None, "Futur mit Präsens widergää."),
]

# ------------------------------------------------------------------------------------------------ Alternativen
ALTS = [
 ("VAR-SBLGNTAPP-MAT-016-004-01:R2", "MAT.16.4", "dem Zeichen des Jona", "dem Zeichen des Propheten Jona",
  "em Zeiche vom Jona", "em Zeiche vom Prophet Jona", "gering",
  "Jona wird ausdrücklich als Prophet bezeichnet.", "De Jona wird usdrücklich Prophet gnännt.",
  {"R1": [("Ἰωνᾶ", "des Jona", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ τοῦ προφήτου", "des Propheten Jona", "RP")]},
  {"R1": [("Ἰωνᾶ", "vom Jona", "WH, Treg, NA28")], "R2": [("Ἰωνᾶ τοῦ προφήτου", "vom Prophet Jona", "RP")]},
  ["Der Zusatz kann aus [[MAT.12.39]] übernommen sein, wo «des Propheten Jona» unbestritten steht; ebenso kann er hier ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne Zusatz, 04 und 032 mit ihm."],
  ["De Zuesatz cha us [[MAT.12.39]] übernoo sii, wo «vom Prophet Jona» unbestritte staat; oder er isch da usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni Zuesatz, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-016-005-01:R2", "MAT.16.5", "die Jünger", "seine Jünger", "d Jünger", "sini Jünger", "gering",
  "Nur ein verdeutlichendes Fürwort.", "Nu es verdüütlichends Fürwort.",
  {"R1": [("μαθηταὶ", "die Jünger", "WH, Treg, NA28")], "R2": [("μαθηταὶ αὐτοῦ", "seine Jünger", "RP")]},
  {"R1": [("μαθηταὶ", "d Jünger", "WH, Treg, NA28")], "R2": [("μαθηταὶ αὐτοῦ", "sini Jünger", "RP")]},
  ["Solche Fürwörter wurden beim Abschreiben oft ergänzt; ebenso können sie ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 ohne Fürwort, 032 mit ihm."],
  ["Söttigi Fürwörter sind bim Abschriibe oft ergänzt worde; oder si sind usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 ohni Fürwort, 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-016-008-01:R2", "MAT.16.8", "und sagte:", "und sagte zu ihnen:", "und gseit:", "und zu ine gseit:", "gering",
  "Die Angeredeten werden genannt.", "Di Aagredte wärded gnännt.",
  {"R1": [("εἶπεν", "sagte", "WH, Treg, NA28")], "R2": [("εἶπεν αὐτοῖς", "sagte zu ihnen", "RP")]},
  {"R1": [("εἶπεν", "hät gseit", "WH, Treg, NA28")], "R2": [("εἶπεν αὐτοῖς", "hät zu ine gseit", "RP")]},
  ["Verdeutlichender Zusatz, wie er beim Abschreiben häufig ist; ebenso kann das Wort ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 05 ohne Zusatz, 04 mit ihm."],
  ["Verdüütlichende Zuesatz, wie s bim Abschriibe hüüfig isch; oder s Wort isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 05 ohni Zuesatz, 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-016-008-02:R2", "MAT.16.8", "dass ihr keine Brote mitgenommen habt", "dass ihr keine Brote habt",
  "dass ir kei Broot mitgnoo händ", "dass ir kei Broot händ", "gering",
  "Jesus greift nicht das Vergessen auf, sondern den Mangel: «dass ihr keine Brote habt» (wie [[MRK.8.17]]).",
  "De Jesus nimmt nöd s Vergässe uf, sondern de Mangel: «dass ir kei Broot händ» (wie [[MRK.8.17]]).",
  {"R1": [("ἐλάβετε", "mitgenommen habt", "Treg, RP")], "R2": [("ἔχετε", "habt", "WH, NA28")]},
  {"R1": [("ἐλάβετε", "mitgnoo händ", "Treg, RP")], "R2": [("ἔχετε", "händ", "WH, NA28")]},
  ["ἐλάβετε nimmt das Verb aus [[MAT.16.7]] auf und kann daran angeglichen sein; ἔχετε kann aus [[MRK.8.17]] stammen. Der SBLGNT folgt hier Treg und RP, gegen WH und NA28.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ἔχετε, 04 und 032 ἐλάβετε."],
  ["ἐλάβετε nimmt s Verb us [[MAT.16.7]] uf und cha dra aaglichne sii; ἔχετε cha us [[MRK.8.17]] stamme. De SBLGNT folgt da em Treg und em RP, gäge WH und NA28.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ἔχετε, 04 und 032 ἐλάβετε."]),
 ("VAR-SBLGNTAPP-MAT-016-011-01:R2", "MAT.16.11", "von Broten", "von Brot", "vo Broot", "vom Broot", "gering",
  "Singular statt Plural; im Sinn gleich.", "Einzahl statt Mehrzahl; de Sinn bliibt gliich.",
  {"R1": [("ἄρτων", "von Broten", "WH, Treg, NA28")], "R2": [("ἄρτου", "von Brot", "RP")]},
  {"R1": [("ἄρτων", "vo Broot (Mehrzahl)", "WH, Treg, NA28")], "R2": [("ἄρτου", "vom Broot", "RP")]},
  ["Der Singular kann an den allgemeinen Sprachgebrauch («Brot») angeglichen sein; der Plural entspricht [[MAT.16.5]]–[[MAT.16.10]].",
   "Laut der automatischen Zuordnung lesen 01 und 03 den Plural, 04, 032 und 05 den Singular."],
  ["D Einzahl cha a de allgemein Sprachgebruuch aaglichne sii; d Mehrzahl entspricht [[MAT.16.5]]–[[MAT.16.10]].",
   "Nach de automatische Zueornig läsed 01 und 03 d Mehrzahl, 04, 032 und 05 d Einzahl."]),
 ("VAR-SBLGNTAPP-MAT-016-011-02:R2", "MAT.16.11", "gesprochen habe? Hütet euch aber vor dem Sauerteig", "gesprochen habe, ihr solltet euch vor dem Sauerteig hüten",
  "gredt han? Hüeted eu aber vor em Suurteig", "gredt han, ir söled eu vor em Suurteig hüete", "gering",
  "Statt einer neuen Mahnung steht ein abhängiger Satz: Jesus habe nicht von Brot gesprochen, als er sagte, sie sollten sich hüten.",
  "Statt ere neue Mahnig staat en abhängige Satz: De Jesus heig nöd vom Broot gredt, won er gseit hät, si söled sich hüete.",
  {"R1": [("προσέχετε δὲ", "hütet euch aber", "WH, Treg, NA28")], "R2": [("προσέχειν", "(dass ihr) euch hüten (solltet)", "RP")]},
  {"R1": [("προσέχετε δὲ", "hüeted eu aber", "WH, Treg, NA28")], "R2": [("προσέχειν", "(dass ir) eu söled hüete", "RP")]},
  ["Der Infinitiv glättet den Satz und entspricht [[MAT.16.12]] (προσέχειν); der Imperativ ist die schwierigere Lesart.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 den Imperativ, 032 den Infinitiv."],
  ["De Infinitiv macht de Satz glatter und entspricht [[MAT.16.12]]; de Imperativ isch di schwierigeri Läsart.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 de Imperativ, 032 de Infinitiv."]),
 ("VAR-SBLGNTAPP-MAT-016-012-01:R2", "MAT.16.12", "vor dem Sauerteig der Brote", "vor dem Sauerteig des Brotes",
  "vor em Suurteig vo de Broot", "vor em Suurteig vom Broot", "gering",
  "Singular statt Plural; im Sinn gleich.", "Einzahl statt Mehrzahl; de Sinn bliibt gliich.",
  {"R1": [("τῶν ἄρτων", "der Brote", "WH, Treg, NA28")], "R2": [("τοῦ ἄρτου", "des Brotes", "RP")]},
  {"R1": [("τῶν ἄρτων", "vo de Broot", "WH, Treg, NA28")], "R2": [("τοῦ ἄρτου", "vom Broot", "RP")]},
  ["Wie in [[MAT.16.11]]: Angleichung an den Singular oder an den Plural der vorangehenden Verse.",
   "Laut der automatischen Zuordnung liest 03 den Plural, 04 und 032 den Singular. 01 und 05 hat die Zuordnung keiner Lesart zugewiesen: Nach der CNTR-Transkription steht in 05 «vor dem Sauerteig» ohne Zusatz, in der korrigierten Fassung von 01 «vor dem Sauerteig der Pharisäer und Sadduzäer»."],
  ["Wie i [[MAT.16.11]]: aaglichne a d Einzahl oder a d Mehrzahl vo de Vers vorher.",
   "Nach de automatische Zueornig list 03 d Mehrzahl, 04 und 032 d Einzahl; 01 und 05 läsed andersch (nach de CNTR-Transkription 05 ohni Zuesatz, 01 korrigiert «vo de Pharisäer und Sadduzäer»)."]),
 ("VAR-SBLGNTAPP-MAT-016-013-01:R2", "MAT.16.13", "Wer, sagen die Leute, sei der Menschensohn?", "Wer, sagen die Leute, sei ich, der Menschensohn?",
  "Wer, säged d Lüüt, sig de Mänschesohn?", "Wer, säged d Lüüt, sig ich, de Mänschesohn?", "mittel",
  "Mit «mich» spricht Jesus ausdrücklich von sich; «Menschensohn» wird zur Beifügung.",
  "Mit «mich» redt de Jesus usdrücklich vo sich; «Mänschesohn» wird zur Biifüegig.",
  {"R1": [("Τίνα", "Wer", "WH, Treg, NA28")], "R2": [("Τίνα με", "Wer … ich", "RP")]},
  {"R1": [("Τίνα", "Wer", "WH, Treg, NA28")], "R2": [("Τίνα με", "Wer … ich", "RP")]},
  ["Das Fürwort kann aus [[MRK.8.27]] und [[LUK.9.18]] stammen oder die ungewöhnliche Frage nach dem Menschensohn verdeutlichen; ebenso kann es ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 04 ohne Fürwort; für 05 ergab sie keine eindeutige Zuordnung."],
  ["S Fürwort cha us [[MRK.8.27]] und [[LUK.9.18]] stamme oder di ungwöhnlich Frag nach em Mänschesohn verdüütliche; oder s isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 04 ohni Fürwort; bi 05 isch d Zueornig nöd eidüütig."]),
 ("VAR-SBLGNTAPP-MAT-016-020-01:R2", "MAT.16.20", "schärfte er den Jüngern ein", "gebot er den Jüngern streng",
  "hät er de Jünger iigschärft", "hät er de Jünger streng befole", "gering",
  "Mit ἐπετίμησεν steht dasselbe Verb wie bei der Zurechtweisung durch Petrus ([[MAT.16.22]]) und beim Schweigegebot in [[MRK.8.30]].",
  "Mit ἐπετίμησεν staat s gliich Verb wie bim Petrus ([[MAT.16.22]]) und i [[MRK.8.30]].",
  {"R1": [("διεστείλατο", "schärfte ein", "Treg, RP, NA28")], "R2": [("ἐπετίμησεν", "gebot streng", "WH, NIV")]},
  {"R1": [("διεστείλατο", "hät iigschärft", "Treg, RP, NA28")], "R2": [("ἐπετίμησεν", "hät streng befole", "WH, NIV")]},
  ["ἐπετίμησεν kann aus [[MRK.8.30]] übernommen sein; umgekehrt kann διεστείλατο das schroffe Verb ersetzt haben.",
   "Laut der automatischen Zuordnung lesen 01, 032 und 04 διεστείλατο, 03 und 05 ἐπετίμησεν."],
  ["ἐπετίμησεν cha us [[MRK.8.30]] übernoo sii; oder διεστείλατο hät s schroffi Verb ersetzt.",
   "Nach de automatische Zueornig läsed 01, 032 und 04 διεστείλατο, 03 und 05 ἐπετίμησεν."]),
 ("VAR-SBLGNTAPP-MAT-016-020-02:R2", "MAT.16.20", "den Jüngern", "seinen Jüngern", "de Jünger", "sine Jünger", "gering",
  "Nur ein verdeutlichendes Fürwort.", "Nu es verdüütlichends Fürwort.",
  {"R1": [("μαθηταῖς", "den Jüngern", "WH, Treg, NA28")], "R2": [("μαθηταῖς αὐτοῦ", "seinen Jüngern", "RP")]},
  {"R1": [("μαθηταῖς", "de Jünger", "WH, Treg, NA28")], "R2": [("μαθηταῖς αὐτοῦ", "sine Jünger", "RP")]},
  ["Solche Fürwörter wurden oft ergänzt; ebenso können sie ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 ohne Fürwort, 032 mit ihm."],
  ["Söttigi Fürwörter sind oft ergänzt worde; oder si sind usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 ohni Fürwort, 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-016-020-03:R2", "MAT.16.20", "dass er der Christus sei", "dass er, Jesus, der Christus sei",
  "dass er de Christus sig", "dass er, de Jesus, de Christus sig", "gering",
  "Der Name wird hinzugefügt; Inhalt des Bekenntnisses wird «Jesus ist der Christus».",
  "De Name chunnt dezue; s Bekänntnis heisst dänn «de Jesus isch de Christus».",
  {"R1": [("ἐστιν", "sei", "WH, Treg, NA28")], "R2": [("ἐστιν Ἰησοῦς", "sei, Jesus,", "RP")]},
  {"R1": [("ἐστιν", "sig", "WH, Treg, NA28")], "R2": [("ἐστιν Ἰησοῦς", "sig, de Jesus,", "RP")]},
  ["Der Name kann aus der Bekenntnisformel «Jesus ist der Christus» eingedrungen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032, 04 und 05 ohne den Namen; unter den erfassten Ausgaben haben ihn RP, KJTR und Stephanus."],
  ["De Name cha us de Bekänntnisformle «de Jesus isch de Christus» iidrunge sii.",
   "Nach de automatische Zueornig läsed 01, 03, 032, 04 und 05 ohni de Name."]),
 ("VAR-SBLGNTAPP-MAT-016-021-01:R2", "MAT.16.21", "begann Jesus", "begann Jesus Christus", "hät de Jesus aagfange", "hät de Jesus Christus aagfange", "gering",
  "Der Doppelname «Jesus Christus» steht im Matthäusevangelium sonst nur am Anfang ([[MAT.1.1]], [[MAT.1.18]]).",
  "De Doppelname «Jesus Christus» staat im Matthäusevangelium susch nu am Aafang ([[MAT.1.1]], [[MAT.1.18]]).",
  {"R1": [("ὁ Ἰησοῦς", "Jesus", "Treg, NA28, RP")], "R2": [("Ἰησοῦς Χριστὸς", "Jesus Christus", "WH")]},
  {"R1": [("ὁ Ἰησοῦς", "de Jesus", "Treg, NA28, RP")], "R2": [("Ἰησοῦς Χριστὸς", "de Jesus Christus", "WH")]},
  ["«Christus» kann nach dem Bekenntnis von [[MAT.16.16]] ergänzt sein; ebenso kann es als ungewöhnlich gestrichen worden sein.",
   "Die automatische Zuordnung hat keine Handschrift eindeutig zugewiesen. Nach den CNTR-Transkriptionen lesen 01 (ohne Artikel) und 03 (mit Artikel) «Jesus Christus», 04 und 032 ὁ Ἰησοῦς, 05 Ἰησοῦς ohne Artikel."],
  ["«Christus» cha nach em Bekänntnis vo [[MAT.16.16]] ergänzt sii; oder s isch als ungwöhnlich gstriche worde.",
   "D automatisch Zueornig hät kei Handschrift eidüütig zuegwise. Nach de CNTR-Transkriptione läsed 01 und 03 «Jesus Christus», 04 und 032 ὁ Ἰησοῦς, 05 Ἰησοῦς."]),
 ("VAR-SBLGNTAPP-MAT-016-026-01:R2", "MAT.16.26", "was wird es einem Menschen nützen", "was nützt es einem Menschen",
  "Was wird s emne Mänsch nämli nütze", "Was nützt s emne Mänsch nämli", "gering",
  "Präsens statt Futur; die Frage wird allgemein statt im Blick auf das kommende Gericht ([[MAT.16.27]]).",
  "Präsens statt Futur; d Frag wird allgemein statt im Blick uf s chömed Gricht ([[MAT.16.27]]).",
  {"R1": [("ὠφεληθήσεται", "wird es nützen", "WH, Treg, NA28")], "R2": [("ὠφελεῖται", "nützt es", "RP")]},
  {"R1": [("ὠφεληθήσεται", "wird s nütze", "WH, Treg, NA28")], "R2": [("ὠφελεῖται", "nützt s", "RP")]},
  ["Das Präsens kann an [[MRK.8.36]] angeglichen sein; ebenso kann das Futur an den folgenden Vers angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 das Futur, 04, 032 und 05 das Präsens."],
  ["S Präsens cha a [[MRK.8.36]] aaglichne sii; oder s Futur a de nächscht Vers.",
   "Nach de automatische Zueornig läsed 01 und 03 s Futur, 04, 032 und 05 s Präsens."]),
 ("VAR-SBLGNTAPP-MAT-017-004-01:R2", "MAT.17.4", "werde ich hier drei Hütten machen", "wollen wir hier drei Hütten machen",
  "mach ich da drüü Hütte", "mached mir da drüü Hütte", "gering",
  "Petrus schlägt vor, die Hütten gemeinsam zu bauen, statt es selbst zu übernehmen.",
  "De Petrus schlaat vor, d Hütte zäme z mache, statt es sälber z übernää.",
  {"R1": [("ποιήσω", "werde ich machen", "WH, NA28")], "R2": [("ποιήσωμεν", "wollen wir machen", "Treg, RP")]},
  {"R1": [("ποιήσω", "mach ich", "WH, NA28")], "R2": [("ποιήσωμεν", "mached mir", "Treg, RP")]},
  ["Der Plural kann an [[MRK.9.5]] und [[LUK.9.33]] angeglichen sein; der Singular entspricht dem Eifer des Petrus bei Matthäus.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 den Singular, 032 und 05 den Plural."],
  ["D Mehrzahl cha a [[MRK.9.5]] und [[LUK.9.33]] aaglichne sii; d Einzahl passt zum Iifer vom Petrus bim Matthäus.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 d Einzahl, 032 und 05 d Mehrzahl."]),
 ("VAR-SBLGNTAPP-MAT-017-009-01:R2", "MAT.17.9", "auferweckt ist", "auferstanden ist", "uferweckt isch", "uferstande isch", "gering",
  "Aktiv «auferstehen» statt Passiv «auferweckt werden».", "Aktiv «uferstaa» statt Passiv «uferweckt wärde».",
  {"R1": [("ἐγερθῇ", "auferweckt ist", "WH, Treg, NA28")], "R2": [("ἀναστῇ", "auferstanden ist", "RP")]},
  {"R1": [("ἐγερθῇ", "uferweckt isch", "WH, Treg, NA28")], "R2": [("ἀναστῇ", "uferstande isch", "RP")]},
  ["ἀναστῇ kann aus [[MRK.9.9]] stammen; umgekehrt kann ἐγερθῇ an den Sprachgebrauch des Matthäus ([[MAT.16.21]], [[MAT.17.23]]) angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 03 und 05 ἐγερθῇ, 01 und 04 ἀναστῇ; 032 liest nach der CNTR-Transkription ebenfalls ἀναστῇ, in anderer Wortfolge."],
  ["ἀναστῇ cha us [[MRK.9.9]] stamme; oder ἐγερθῇ isch a de Sprachgebruuch vom Matthäus aaglichne.",
   "Nach de automatische Zueornig läsed 03 und 05 ἐγερθῇ, 01 und 04 ἀναστῇ; 032 au ἀναστῇ, i andere Wortfolg."]),
 ("VAR-SBLGNTAPP-MAT-017-010-01:R2", "MAT.17.10", "die Jünger", "seine Jünger", "d Jünger", "sini Jünger", "gering",
  "Nur ein verdeutlichendes Fürwort.", "Nu es verdüütlichends Fürwort.",
  {"R1": [("μαθηταὶ", "die Jünger", "WH, Treg, NA28")], "R2": [("μαθηταὶ αὐτοῦ", "seine Jünger", "RP")]},
  {"R1": [("μαθηταὶ", "d Jünger", "WH, Treg, NA28")], "R2": [("μαθηταὶ αὐτοῦ", "sini Jünger", "RP")]},
  ["Solche Fürwörter wurden oft ergänzt; ebenso können sie ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 (auch in der Korrektur) und 032 ohne Fürwort, 03, 04 und 05 mit ihm."],
  ["Söttigi Fürwörter sind oft ergänzt worde; oder si sind usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 032 ohni Fürwort, 03, 04 und 05 mit."]),
 ("VAR-SBLGNTAPP-MAT-017-011-03:R2", "MAT.17.11", "Elija kommt zwar", "Elija kommt zwar zuerst", "De Elija chunnt scho", "De Elija chunnt scho zerscht", "gering",
  "Der Zusatz nimmt «zuerst» aus der Frage der Jünger auf ([[MAT.17.10]]).", "De Zuesatz nimmt «zerscht» us de Frag vo de Jünger uf ([[MAT.17.10]]).",
  {"R1": [("ἔρχεται", "kommt", "WH, Treg, NA28")], "R2": [("ἔρχεται πρῶτον", "kommt zuerst", "RP")]},
  {"R1": [("ἔρχεται", "chunnt", "WH, Treg, NA28")], "R2": [("ἔρχεται πρῶτον", "chunnt zerscht", "RP")]},
  ["«Zuerst» kann aus [[MAT.17.10]] und [[MRK.9.12]] ergänzt sein; ebenso kann es ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 05 ohne Zusatz, 04 mit ihm."],
  ["«Zerscht» cha us [[MAT.17.10]] und [[MRK.9.12]] ergänzt sii; oder s isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 05 ohni Zuesatz, 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-017-015-01:R2", "MAT.17.15", "leidet schwer", "hat es schlimm", "schlimm liidet", "s schlimm hät", "gering",
  "«Es schlimm haben» (κακῶς ἔχειν) ist die geläufige Wendung für Kranke ([[MAT.4.24]]); der Sinn ist ähnlich.",
  "«S schlimm ha» isch di gläufig Wändig für Chranki ([[MAT.4.24]]); de Sinn isch ähnlich.",
  {"R1": [("πάσχει", "leidet", "NA28, RP")], "R2": [("ἔχει", "hat es (schlimm)", "WH, Treg")]},
  {"R1": [("πάσχει", "liidet", "NA28, RP")], "R2": [("ἔχει", "hät s (schlimm)", "WH, Treg")]},
  ["ἔχει kann an die geläufige Wendung κακῶς ἔχειν angeglichen sein; πάσχει kann das Leiden verstärken. Der SBLGNT folgt hier NA28 und RP, gegen WH und Treg.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ἔχει, 032, 04 und 05 πάσχει."],
  ["ἔχει cha a di gläufig Wändig aaglichne sii; πάσχει cha s Liide verstärche. De SBLGNT folgt da em NA28 und em RP.",
   "Nach de automatische Zueornig läsed 01 und 03 ἔχει, 032, 04 und 05 πάσχει."]),
 ("VAR-SBLGNTAPP-MAT-017-020-02:R2", "MAT.17.20", "Wegen eures Kleinglaubens", "Wegen eures Unglaubens", "Wäge eurem Chliiglaube", "Wäge eurem Unglaube", "mittel",
  "Statt zu wenig Glauben wird den Jüngern Unglaube vorgeworfen.", "Statt z wenig Glaube wirft er de Jünger Unglaube vor.",
  {"R1": [("ὀλιγοπιστίαν", "Kleinglaubens", "WH, Treg, NA28")], "R2": [("ἀπιστίαν", "Unglaubens", "RP")]},
  {"R1": [("ὀλιγοπιστίαν", "Chliiglaube", "WH, Treg, NA28")], "R2": [("ἀπιστίαν", "Unglaube", "RP")]},
  ["ἀπιστίαν kann an [[MAT.17.17]] («ungläubig») oder an [[MRK.9.24]] angeglichen sein; ὀλιγοπιστίαν entspricht dem Lieblingswort des Matthäus (vgl. [[MAT.16.8]]) und kann deshalb auch eingetragen sein. Die Senfkorn-Aussage passt eher zu «Kleinglaube».",
   "Laut der automatischen Zuordnung lesen 01 und 03 ὀλιγοπιστίαν, 032, 04 und 05 ἀπιστίαν."],
  ["ἀπιστίαν cha a [[MAT.17.17]] oder [[MRK.9.24]] aaglichne sii; ὀλιγοπιστίαν isch es Lieblingswort vom Matthäus und cha drum au iitreit sii.",
   "Nach de automatische Zueornig läsed 01 und 03 ὀλιγοπιστίαν, 032, 04 und 05 ἀπιστίαν."]),
 ("VAR-SBLGNTAPP-MAT-017-020-04:R2", "MAT.17.20", "und nichts wird euch unmöglich sein.»",
  "und nichts wird euch unmöglich sein. (21) Diese Art aber fährt nur durch Gebet und Fasten aus.»",
  "und nüüt wird eu unmöglich sii.»", "und nüüt wird eu unmöglich sii. (21) Die Art aber fahrt nu dur Bätte und Faschte us.»", "mittel",
  "Der Zusatz bildet den Vers [[MAT.17.21]]; im SBLGNT fehlt er, deshalb hat [[MAT.17.21]] hier keinen Übersetzungstext. Er nennt Gebet und Fasten als Weg, diese Art von Dämonen auszutreiben.",
  "De Zuesatz isch de Vers [[MAT.17.21]]; im SBLGNT fehlt er, drum hät [[MAT.17.21]] da kei Text. Er nännt Bätte und Faschte als Wäg, die Art vo Dämone uszträibe.",
  {"R1": [("ὑμῖν", "(ohne Vers 21)", "WH, NA28")], "R2": [("ὑμῖν. Τοῦτο δὲ τὸ γένος οὐκ ἐκπορεύεται εἰ μὴ ἐν προσευχῇ καὶ νηστείᾳ.", "Diese Art aber fährt nur durch Gebet und Fasten aus", "Treg, RP")]},
  {"R1": [("ὑμῖν", "(ohni Vers 21)", "WH, NA28")], "R2": [("… Τοῦτο δὲ τὸ γένος οὐκ ἐκπορεύεται εἰ μὴ ἐν προσευχῇ καὶ νηστείᾳ.", "Die Art aber fahrt nu dur Bätte und Faschte us", "Treg, RP")]},
  ["Der Satz kann aus der Parallele [[MRK.9.29]] übernommen sein (dort in einem Teil der Überlieferung ebenfalls mit «und Fasten»); umgekehrt kann er ausgefallen sein. Die Erweiterung «und Fasten» kann die wachsende Bedeutung des Fastens in der frühen Kirche spiegeln.",
   "Die automatische Zuordnung ordnet alle Zeugen dem kurzen Text zu, auch die Ausgabe RP, die den Vers laut SBLGNT-Apparat hat; sie vergleicht nur den Wortlaut bis zum Ende von [[MAT.17.20]] und sieht den zusätzlichen Vers nicht. Es gilt der Apparat. Nach den CNTR-Transkriptionen steht der Vers in 04, 05 und 032 sowie in den Ausgaben RP, KJTR und Stephanus; in 01 und 03 sowie bei WH und SR fehlt er."],
  ["De Satz cha us de Parallele [[MRK.9.29]] übernoo sii; oder er isch usgfalle. «Und Faschte» cha zeige, wie wichtig s Faschte i de früene Chile worde isch.",
   "D automatisch Zueornig ordnet alli Züüge em churze Text zue, au de RP, wo de Vers nach em Apparat hät; si vergliicht nu bis as Änd vo [[MAT.17.20]]. Es gilt de Apparat. Nach de CNTR-Transkriptione staat de Vers i 04, 05 und 032, nöd aber i 01 und 03."]),
 ("VAR-SBLGNTAPP-MAT-017-022-01:R2", "MAT.17.22", "sich aber in Galiläa sammelten", "sich aber in Galiläa aufhielten",
  "sich aber in Galiläa gsammlet händ", "sich aber in Galiläa ufghalte händ", "gering",
  "Statt vom Sich-Sammeln ist vom Aufenthalt in Galiläa die Rede.", "Statt vom Sich-Sammle isch vom Ufenthalt in Galiläa d Red.",
  {"R1": [("Συστρεφομένων", "als sie sich sammelten", "WH, Treg, NA28")], "R2": [("Ἀναστρεφομένων", "als sie sich aufhielten", "RP")]},
  {"R1": [("Συστρεφομένων", "wo si sich gsammlet händ", "WH, Treg, NA28")], "R2": [("Ἀναστρεφομένων", "wo si sich ufghalte händ", "RP")]},
  ["Das seltene συστρέφομαι kann durch das geläufigere ἀναστρέφομαι ersetzt worden sein; die beiden Wörter unterscheiden sich im Schriftbild nur in der Vorsilbe.",
   "Laut der automatischen Zuordnung lesen 01 und 03 Συστρεφομένων, 032, 04 und 05 Ἀναστρεφομένων."],
  ["S selte συστρέφομαι cha dur s gläufiger ἀναστρέφομαι ersetzt worde sii; di zwei Wort underscheided sich nu i de Vorsilbe.",
   "Nach de automatische Zueornig läsed 01 und 03 Συστρεφομένων, 032, 04 und 05 Ἀναστρεφομένων."]),
 ("VAR-SBLGNTAPP-MAT-017-026-01:R2", "MAT.17.26", "Als er aber sagte: «Von den Fremden»", "Petrus sagt zu ihm: «Von den Fremden»",
  "Wo er aber gseit hät: «Vo de Frömde»", "De Petrus seit zu ihm: «Vo de Frömde»", "gering",
  "Petrus wird ausdrücklich als Antwortender genannt.", "De Petrus wird usdrücklich als dä gnännt, wo antwortet.",
  {"R1": [("εἰπόντος δέ", "als er aber sagte", "WH, Treg, NA28")], "R2": [("Λέγει αὐτῷ ὁ Πέτρος", "Petrus sagt zu ihm", "RP")]},
  {"R1": [("εἰπόντος δέ", "wo er aber gseit hät", "WH, Treg, NA28")], "R2": [("Λέγει αὐτῷ ὁ Πέτρος", "de Petrus seit zu ihm", "RP")]},
  ["Die Nennung des Petrus verdeutlicht den Sprecherwechsel; die knappe Genitivkonstruktion ist die schwierigere Lesart.",
   "Laut der automatischen Zuordnung lesen 01 und 03 εἰπόντος δέ, 032 die Form mit Petrus. 04 und 05 hat sie keiner Lesart zugewiesen: Nach den CNTR-Transkriptionen hat 04 beide Wendungen nacheinander, 05 «er sagt zu ihm» ohne Namen; auch die Erstschrift von 01 verbindet nach der CNTR-Transkription zwei Wendungen."],
  ["D Nännig vom Petrus verdüütlicht de Sprächerwächsel; di churz Genitivkonstruktion isch di schwierigeri Läsart.",
   "Nach de automatische Zueornig läsed 01 und 03 εἰπόντος δέ, 032 d Form mit em Petrus; 04 hät nach de CNTR-Transkription beidi Wändige, 05 «er seit zu ihm» ohni Name."]),
]

# ------------------------------------------------------------------------------------------------ Texteinheiten
SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-016-001-028", "MAT.16.1-MAT.16.28", "section", "Zeichenforderung, Bekenntnis des Petrus und der Weg der Nachfolge",
  ["TU-MAT-016-001-004", "TU-MAT-016-005-012", "TU-MAT-016-013-020", "TU-MAT-016-021-028"],
  "Pharisäer und Sadduzäer verlangen von Jesus ein Zeichen vom Himmel, um ihn auf die Probe zu stellen; er verweist sie auf das Zeichen des Jona und geht weg. Die Jünger haben vergessen, Brote mitzunehmen, und beziehen Jesu Warnung vor dem Sauerteig der Pharisäer und Sadduzäer auf das Brot, bis sie verstehen, dass er deren Lehre meint. In der Gegend von Cäsarea Philippi bekennt Simon Petrus Jesus als den Christus, den Sohn des lebendigen Gottes; Jesus nennt ihn selig, sagt, auf diesen Felsen werde er seine Gemeinde bauen, verspricht ihm die Schlüssel des Reichs der Himmel und verbietet den Jüngern, zu sagen, dass er der Christus sei. Von da an beginnt Jesus seinen Jüngern zu zeigen, dass er in Jerusalem leiden, getötet und am dritten Tag auferweckt werden muss. Petrus widerspricht und wird mit «Geh hinter mich, Satan!» zurückgewiesen. Jesus ruft dazu auf, sich selbst zu verleugnen und das Kreuz auf sich zu nehmen, und kündigt an, dass der Menschensohn in der Herrlichkeit seines Vaters kommen und jedem nach seinem Tun vergelten wird.", SEG),
 ("TU-MAT-016-001-004", "MAT.16.1-MAT.16.4", "dialogue", "Die Forderung nach einem Zeichen", None,
  "Pharisäer und Sadduzäer treten an Jesus heran und fordern ihn auf, ihnen ein Zeichen vom Himmel zu zeigen, um ihn auf die Probe zu stellen. Er hält ihnen vor, dass sie am Abendrot und am Morgenhimmel das Wetter zu beurteilen wissen, die Zeichen der Zeiten aber nicht beurteilen können. Einem bösen und ehebrecherischen Geschlecht werde kein Zeichen gegeben ausser dem Zeichen des Jona. Dann verlässt er sie. Die Worte über Abend- und Morgenhimmel ([[MAT.16.2]]b–3) fehlen in einem Teil der Überlieferung.", None),
 ("TU-MAT-016-005-012", "MAT.16.5-MAT.16.12", "dialogue", "Der Sauerteig der Pharisäer und Sadduzäer", None,
  "Am anderen Ufer zeigt sich, dass die Jünger vergessen haben, Brote mitzunehmen. Als Jesus sie vor dem Sauerteig der Pharisäer und Sadduzäer warnt, überlegen sie untereinander, dass sie keine Brote mitgenommen haben. Jesus nennt sie Kleingläubige, erinnert sie an die Brote für die Fünftausend und die Viertausend und an die Körbe, die sie aufgehoben haben, und fragt, wie sie nicht begreifen können, dass er nicht von Broten gesprochen hat. Da verstehen sie, dass er vor der Lehre der Pharisäer und Sadduzäer gewarnt hat.", None),
 ("TU-MAT-016-013-020", "MAT.16.13-MAT.16.20", "dialogue", "Das Bekenntnis des Petrus", None,
  "In der Gegend von Cäsarea Philippi fragt Jesus seine Jünger, wer nach der Meinung der Leute der Menschensohn sei; sie nennen Johannes den Täufer, Elija, Jeremia oder einen der Propheten. Auf die Frage, wer er nach ihrer eigenen Meinung sei, antwortet Simon Petrus: «Du bist der Christus, der Sohn des lebendigen Gottes!» Jesus nennt ihn selig, weil nicht Fleisch und Blut, sondern sein Vater in den Himmeln ihm das offenbart hat. Er sagt: Du bist Petrus, und auf diesen Felsen werde ich meine Gemeinde bauen, und die Tore des Totenreichs werden sie nicht überwältigen. Er werde ihm die Schlüssel des Reichs der Himmel geben; was er auf der Erde binde oder löse, werde in den Himmeln gebunden oder gelöst sein. Dann schärft er den Jüngern ein, niemandem zu sagen, dass er der Christus sei.", None),
 ("TU-MAT-016-021-028", "MAT.16.21-MAT.16.28", "dialogue", "Erste Leidensankündigung und der Weg der Nachfolge", None,
  "Von da an beginnt Jesus seinen Jüngern zu zeigen, dass er nach Jerusalem gehen, von den Ältesten, Hohepriestern und Schriftgelehrten vieles erleiden, getötet und am dritten Tag auferweckt werden muss. Petrus nimmt ihn beiseite und weist ihn zurecht: Das werde ihm niemals widerfahren. Jesus wendet sich um und sagt zu Petrus: «Geh hinter mich, Satan!» Er sei ihm ein Fallstrick, denn er habe nicht im Sinn, was Gottes ist, sondern was der Menschen ist. Zu seinen Jüngern sagt er: Wer hinter ihm herkommen will, soll sich selbst verleugnen, sein Kreuz auf sich nehmen und ihm folgen; wer sein Leben retten will, wird es verlieren, wer es um seinetwillen verliert, wird es finden. Der Menschensohn wird in der Herrlichkeit seines Vaters mit seinen Engeln kommen und jedem nach seinem Tun vergelten; einige der hier Stehenden werden den Tod nicht schmecken, bis sie den Menschensohn in seinem Reich kommen sehen.", None),
 ("TU-MAT-017-001-027", "MAT.17.1-MAT.17.27", "section", "Verwandlung auf dem Berg, Heilung eines Jungen und die Doppeldrachme",
  ["TU-MAT-017-001-008", "TU-MAT-017-009-013", "TU-MAT-017-014-021", "TU-MAT-017-022-023", "TU-MAT-017-024-027"],
  "Auf einem hohen Berg wird Jesus vor Petrus, Jakobus und Johannes verwandelt; Mose und Elija erscheinen und reden mit ihm, und eine Stimme aus einer lichten Wolke nennt ihn den geliebten Sohn, auf den sie hören sollen. Beim Abstieg verbietet Jesus, von der Erscheinung zu erzählen, bis der Menschensohn von den Toten auferweckt ist, und sagt, Elija sei schon gekommen; die Jünger verstehen, dass er von Johannes dem Täufer spricht. Einen mondsüchtigen Jungen, den die Jünger nicht heilen konnten, heilt Jesus, indem er dem Dämon droht; den Jüngern nennt er ihren Kleinglauben als Grund und spricht vom Glauben wie ein Senfkorn. In Galiläa sagt er erneut, der Menschensohn werde ausgeliefert, getötet und am dritten Tag auferweckt werden; die Jünger werden sehr traurig. In Kafarnaum fragen die Einnehmer der Doppeldrachme Petrus, ob sein Lehrer sie zahle; Jesus sagt, die Söhne seien frei, weist Petrus aber an, um sie nicht zu Fall zu bringen, den Stater, den er im Maul des ersten Fisches finden werde, für beide zu geben. [[MAT.17.21]] fehlt im SBLGNT.", SEG),
 ("TU-MAT-017-001-008", "MAT.17.1-MAT.17.8", "narrative", "Die Verwandlung auf dem Berg", None,
  "Nach sechs Tagen nimmt Jesus Petrus, Jakobus und dessen Bruder Johannes mit auf einen hohen Berg. Dort wird er vor ihnen verwandelt: Sein Gesicht leuchtet wie die Sonne, seine Kleider werden weiss wie das Licht. Mose und Elija erscheinen ihnen und reden mit ihm. Petrus sagt, es sei gut, dass sie hier sind, und bietet an, drei Hütten zu machen. Während er noch redet, überschattet sie eine lichte Wolke, und eine Stimme aus der Wolke sagt: «Dieser ist mein Sohn, der Geliebte, an dem ich Gefallen gefunden habe; hört auf ihn!» Die Jünger fallen auf ihr Gesicht und fürchten sich sehr; Jesus tritt heran, berührt sie und sagt, sie sollen aufstehen und sich nicht fürchten. Als sie aufblicken, sehen sie niemanden ausser Jesus allein.", None),
 ("TU-MAT-017-009-013", "MAT.17.9-MAT.17.13", "dialogue", "Die Frage nach Elija", None,
  "Beim Abstieg vom Berg gebietet Jesus den drei Jüngern, niemandem von der Erscheinung zu erzählen, bis der Menschensohn von den Toten auferweckt ist. Sie fragen, warum die Schriftgelehrten sagen, Elija müsse zuerst kommen. Jesus antwortet, Elija komme zwar und werde alles wiederherstellen; doch Elija sei schon gekommen, man habe ihn nicht erkannt, sondern mit ihm gemacht, was man wollte; so werde auch der Menschensohn durch sie leiden. Da verstehen die Jünger, dass er von Johannes dem Täufer gesprochen hat.", None),
 ("TU-MAT-017-014-021", "MAT.17.14-MAT.17.21", "narrative", "Die Heilung eines mondsüchtigen Jungen", None,
  "Als sie zur Menge kommen, fällt ein Mann vor Jesus auf die Knie und bittet um Erbarmen für seinen Sohn: Er sei mondsüchtig und leide schwer, oft falle er ins Feuer und ins Wasser, und die Jünger hätten ihn nicht heilen können. Jesus klagt über das ungläubige und verkehrte Geschlecht und verlangt, dass man ihm den Jungen bringt. Er droht dem Dämon, der Dämon fährt aus, und der Junge ist von jener Stunde an geheilt. Als die Jünger ihn allein fragen, warum sie ihn nicht austreiben konnten, nennt Jesus ihren Kleinglauben: Hätten sie Glauben wie ein Senfkorn, würden sie zu diesem Berg sagen, er solle von hier nach dort gehen, und er würde hinübergehen; nichts wäre ihnen unmöglich. [[MAT.17.21]] fehlt im SBLGNT; andere Ausgaben haben dort ein Wort über Gebet und Fasten.", None),
 ("TU-MAT-017-022-023", "MAT.17.22-MAT.17.23", "narrative_with_saying", "Zweite Leidensankündigung", None,
  "Als sie sich in Galiläa sammeln, sagt Jesus, der Menschensohn werde in die Hände von Menschen ausgeliefert werden; sie würden ihn töten, und am dritten Tag werde er auferweckt werden. Die Jünger werden sehr traurig.", None),
 ("TU-MAT-017-024-027", "MAT.17.24-MAT.17.27", "dialogue", "Die Doppeldrachme", None,
  "In Kafarnaum fragen die Einnehmer der Doppeldrachme Petrus, ob sein Lehrer sie nicht zahle; Petrus bejaht. Im Haus kommt Jesus ihm zuvor und fragt, von wem die Könige der Erde Zoll oder Steuer nehmen, von ihren Söhnen oder von den Fremden. Auf die Antwort «Von den Fremden» folgert Jesus, die Söhne seien also frei. Um sie aber nicht zu Fall zu bringen, weist er Petrus an, am See eine Angel auszuwerfen; im Maul des ersten Fisches werde er einen Stater finden, den solle er ihnen für Jesus und sich geben. Dass Petrus den Auftrag ausführt, wird nicht erzählt.", None),
]
UNITS_GSW = {
 "TU-MAT-016-001-028": ("Zeichefoderig, s Bekänntnis vom Petrus und de Wäg vo de Nachfolg",
  "D Pharisäer und Sadduzäer verlanged vom Jesus es Zeiche vom Himel, zum en uf d Prob stelle; er verwiist si ufs Zeiche vom Jona und gaat furt. D Jünger händ vergässe, Broot mitznää, und beziehnd d Warnig vom Jesus vor em Suurteig vo de Pharisäer und Sadduzäer uf s Broot, bis si verstönd, dass er iri Lehr meint. I de Gäged vo Cäsarea Philippi bekännt de Simon Petrus de Jesus als de Christus, de Sohn vom läbige Gott; de Jesus priist en sälig, seit, uf dä Felse wärdi er sini Gmeind buue, verspricht em d Schlüssel vom Riich vo de Himel und verbüütet de Jünger z säge, dass er de Christus sig. Vo dänn aa faat de Jesus aa, sine Jünger z zeige, dass er z Jerusalem mües liide, umbracht und am dritte Tag uferweckt wärde. De Petrus widerspricht und wird mit «Gang hinder mich, Satan!» zruggwise. De Jesus rüeft uf, sich sälber z verleugne und s Chrüüz uf sich z nää, und seit aa, dass de Mänschesohn i de Herrlichkeit vo sim Vatter chunnt und jedem nach sim Tue vergältet."),
 "TU-MAT-016-001-004": ("D Foderig nach eme Zeiche",
  "D Pharisäer und Sadduzäer chömed zum Jesus häre und fordered en uf, ine es Zeiche vom Himel z zeige, zum en uf d Prob stelle. Er haltet ine vor, dass si am Aabigrot und am Morgehimel s Wätter chönd beurteile, d Zeiche vo de Ziite aber nöd. Ere bööse und ehebrecherische Generation wärdi kei Zeiche ggää usser em Zeiche vom Jona. Dänn laat er si staa. D Wort über de Aabig- und Morgehimel ([[MAT.16.2]]b–3) fehled i eme Teil vo de Überlieferig."),
 "TU-MAT-016-005-012": ("De Suurteig vo de Pharisäer und Sadduzäer",
  "Am andere Ufer zeigt sich, dass d Jünger vergässe händ, Broot mitznää. Wo de Jesus si vor em Suurteig vo de Pharisäer und Sadduzäer warnt, überleged si mitenand, dass si kei Broot mitgnoo händ. De Jesus nännt si Chliigläubigi, erinneret si a d Broot für di Föiftuusig und di Viertuusig und a d Chörb, wo si ufgläse händ, und fröget, wie si nöd chönd begriife, dass er nöd vo Broot gredt hät. Dänn verstönd si, dass er vor de Lehr vo de Pharisäer und Sadduzäer gwarnt hät."),
 "TU-MAT-016-013-020": ("S Bekänntnis vom Petrus",
  "I de Gäged vo Cäsarea Philippi fröget de Jesus sini Jünger, wer nach de Lüüt de Mänschesohn sig; si nänned de Johannes de Täufer, de Elija, de Jeremia oder eine vo de Prophete. Uf d Frag, wer er nach irer eigete Meinig sig, antwortet de Simon Petrus: «Du bisch de Christus, de Sohn vom läbige Gott!» De Jesus priist en sälig, wil nöd Fleisch und Bluet, sondern sin Vatter i de Himel ihm das offebaret hät. Er seit: Du bisch de Petrus, und uf dä Felse wird ich mini Gmeind buue, und d Tor vom Totereich wärded si nöd überwältige. Er wärdi ihm d Schlüssel vom Riich vo de Himel gää; was er uf de Ärde bindi oder lösi, sig i de Himel bunde oder glöst. Dänn schärft er de Jünger ii, niemertem z säge, dass er de Christus sig."),
 "TU-MAT-016-021-028": ("Erschti Liidesaakündigung und de Wäg vo de Nachfolg",
  "Vo dänn aa faat de Jesus aa, sine Jünger z zeige, dass er mues uf Jerusalem gaa, vo de Ältischte, Hoheprieschter und Schriftgelehrte vil liide, umbracht und am dritte Tag uferweckt wärde. De Petrus nimmt en uf d Siite und wiist en zrächt: Das passier em sicher nie. De Jesus dräit sich um und seit zum Petrus: «Gang hinder mich, Satan!» Er sig em en Fallstrick, wil er nöd im Sinn heig, was vo Gott isch, sondern was vo de Mänsche isch. Zu sine Jünger seit er: Wer hinder ihm härchoo well, söll sich sälber verleugne, sis Chrüüz uf sich nää und ihm nachefolge; wer sis Läbe rette well, verlüüri s, wer s wäge ihm verlüüri, findi s. De Mänschesohn wärdi i de Herrlichkeit vo sim Vatter mit sine Ängel choo und jedem nach sim Tue vergälte; es paar vo dene, wo da stönd, wärdid de Tod nöd schmöcke, bis si de Mänschesohn i sim Riich gsehnd choo."),
 "TU-MAT-017-001-027": ("Verwandlig uf em Bärg, d Heilig vo me Bueb und d Doppeldrachme",
  "Uf eme hööche Bärg wird de Jesus vor em Petrus, em Jakobus und em Johannes verwandlet; de Mose und de Elija erschiined und reded mit ihm, und e Stimm us ere hälle Wolche nännt en de gliebt Sohn, uf dä si söled lose. Bim Abestiige verbüütet de Jesus, vo de Erschiinig z verzelle, bis de Mänschesohn vo de Tote uferweckt isch, und seit, de Elija sig scho choo; d Jünger verstönd, dass er vom Johannes em Täufer redt. En mondsüchtige Bueb, wo d Jünger nöd händ chöne heile, heilt de Jesus, indem er de Dämon aafahrt; de Jünger nännt er ire Chliiglaube als Grund und redt vom Glaube wie es Senfchorn. In Galiläa seit er wider, de Mänschesohn wärdi usgliferet, umbracht und am dritte Tag uferweckt; d Jünger wärded fescht truurig. Z Kafarnaum fröged d Iizüger vo de Doppeldrachme de Petrus, öb sin Lehrer si zahli; de Jesus seit, d Söön sigid frei, wiist de Petrus aber aa, für si nöd z Fall z bringe, de Stater, won er im Muul vom erschte Fisch wärdi finde, für beid z gää. [[MAT.17.21]] fehlt im SBLGNT."),
 "TU-MAT-017-001-008": ("D Verwandlig uf em Bärg",
  "Nach sächs Täg nimmt de Jesus de Petrus, de Jakobus und dä sin Brüeder Johannes mit uf en hööche Bärg. Det wird er vor ine verwandlet: Sis Gsicht lüüchtet wie d Sunne, sini Chleider wärded wiiss wie s Liecht. De Mose und de Elija erschiined ine und reded mit ihm. De Petrus seit, es sig guet, dass si da sind, und biitet aa, drüü Hütte z mache. Won er no redt, überschattet si e hälli Wolche, und e Stimm us de Wolche seit: «Das isch min Sohn, de Gliebt, a däm ich Freud ha; losed uf en!» D Jünger gheied uf ires Gsicht und förchted sich fescht; de Jesus chunnt häre, rüert si aa und seit, si söled ufstaa und kei Angscht ha. Wo si ufelueged, gsehnd si niemer meh usser de Jesus elei."),
 "TU-MAT-017-009-013": ("D Frag nach em Elija",
  "Bim Abestiige vom Bärg befilt de Jesus de drüü Jünger, niemertem vo de Erschiinig z verzelle, bis de Mänschesohn vo de Tote uferweckt isch. Si fröged, werum d Schriftgelehrti säged, de Elija mües zerscht choo. De Jesus antwortet, de Elija chömi scho und bringi alles wider in Ornig; aber de Elija sig scho choo, me heig en nöd erchännt, sondern mit ihm gmacht, was me wele heig; eso wärdi au de Mänschesohn dur si liide. Dänn verstönd d Jünger, dass er vom Johannes em Täufer gredt hät."),
 "TU-MAT-017-014-021": ("D Heilig vo me mondsüchtige Bueb",
  "Wo si zu de Mängi chömed, gheit en Maa vor em Jesus uf d Chnü und bittet um Erbarme für sin Sohn: Er sig mondsüchtig und liidi schlimm, vil Mal gheii er is Füür und is Wasser, und d Jünger heigid en nöd chöne heile. De Jesus chlagt über di ungläubig und verdrähti Generation und verlangt, dass me ihm de Bueb bringt. Er fahrt de Dämon aa, de Dämon fahrt us, und de Bueb isch vo dere Stund aa gheilt. Wo d Jünger en elei fröged, werum si en nöd händ chöne ustriibe, nännt de Jesus ire Chliiglaube: Wänn si Glaube hettid wie es Senfchorn, würdid si zu dem Bärg säge, er söll vo da dört äne gaa, und er gieng dört äne; nüüt wär ine unmöglich. [[MAT.17.21]] fehlt im SBLGNT; anderi Usgabe händ det es Wort über Bätte und Faschte."),
 "TU-MAT-017-022-023": ("Zweiti Liidesaakündigung",
  "Wo si sich in Galiläa sammled, seit de Jesus, de Mänschesohn wärdi i d Händ vo Mänsche usgliferet; si wärdid en umbringe, und am dritte Tag wärdi er uferweckt. D Jünger wärded fescht truurig."),
 "TU-MAT-017-024-027": ("D Doppeldrachme",
  "Z Kafarnaum fröged d Iizüger vo de Doppeldrachme de Petrus, öb sin Lehrer si nöd zahli; de Petrus seit ja. Im Huus chunnt em de Jesus zvor und fröget, vo wem d Chünige vo de Ärde Zoll oder Stüür nämed, vo ire Söön oder vo de Frömde. Uf d Antwort «Vo de Frömde» folgeret de Jesus, d Söön sigid also frei. Für si aber nöd z Fall z bringe, wiist er de Petrus aa, am See en Angel uszwärfe; im Muul vom erschte Fisch wärdi er en Stater finde, dä söll er ine für de Jesus und für sich gää. Öb de Petrus das macht, wird nöd verzellt."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung. Eigene Formulierung; nicht aus einer veröffentlichten Bibel übernommen.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts gezählt."),
 ("Bereich und Abgrenzung: Diese Datei umfasst [[MAT.16.1-MAT.16.28]] und [[MAT.17.1-MAT.17.27]]. Die einheitlichen "
  "Begriffe für Matthäus gelten: «das Reich der Himmel», «der Menschensohn», «Amen, ich sage euch», «Vater in den Himmeln», "
  "«siehe», «Schriftgelehrte», «Pharisäer», «Sadduzäer», «Hohepriester», «Älteste», «Dämon», «Gemeinde» für ἐκκλησία "
  "([[MAT.16.18]]), «Christus», «Kafarnaum», «Galiläa». τότε ist erzählend mit «da», sonst mit «dann» wiedergegeben."),
 ("Abstimmung mit Markus: Die Parallelen in [[MRK.8.11-MRK.8.38]] und [[MRK.9.1-MRK.9.32]] sind, wo der griechische Wortlaut "
  "gleich ist, gleich übersetzt (z. B. «Geh hinter mich, Satan», «Leben» für ψυχή, «den Tod nicht schmecken», «ausgeliefert», "
  "«Geschlecht» für γενεά, «verwandelt»). Wo Matthäus anders formuliert, folgt die Übersetzung ihm: «auferweckt werden» "
  "(ἐγερθῆναι) statt «auferstehen», «am dritten Tag» statt «nach drei Tagen», «Herr» statt «Rabbi» ([[MAT.17.4]]), Futur in "
  "[[MAT.17.11]] und [[MAT.17.17]]."),
 ("Wiedergaben, die für das ganze Evangelium einheitlich gelten (jeweils in decisions begründet): μακάριος «selig» "
  "([[MAT.16.17]]); ὀλιγόπιστος / ὀλιγοπιστία «kleingläubig, ihr Kleingläubigen» / «Kleinglaube», πίστις «Glaube» "
  "([[MAT.16.8]], [[MAT.17.20]]); σκανδαλίζω «zu Fall bringen», passiv «Anstoss nehmen an» (Person) bzw. «zu Fall kommen», "
  "auch [[MAT.17.27]], σκάνδαλον «Fallstrick» ([[MAT.16.23]]); προσέρχομαι "
  "«herantreten» ([[MAT.16.1]]); ᾅδης «Totenreich» ([[MAT.16.18]]); ἐγείρω im Passiv «auferweckt werden»; ἐπιτιμάω je nach "
  "Zusammenhang «zurechtweisen» bzw. bei Austreibungen «drohen» wie bei Markus; νοέω «begreifen», συνίημι «verstehen»."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT gegen WH und NA28 liest ([[MAT.16.8]] ἐλάβετε) oder "
  "gegen WH und Treg ([[MAT.17.15]] πάσχει). Abweichende Lesarten des SBLGNT-Apparats stehen als Alternativen, soweit sie die "
  "Übersetzung verändern; reine Wortstellungs- und Schreibvarianten ohne Folgen für die Übersetzung sind nicht aufgenommen."),
 ("[[MAT.16.2]]b–3 («Wenn es Abend wird … nicht beurteilen») steht im SBLGNT im Text. Der SBLGNT-Apparat vermerkt, dass WH "
  "die Worte in doppelte eckige Klammern setzt und dass RP in [[MAT.16.3]] «Heuchler» ergänzt. Diese beiden Apparateinträge "
  "fehlen in den importierten Variantendatensätzen (data/variants/sblgntapp-mat); deshalb stehen sie in decisions und hier, "
  "nicht als Alternativen. Nach den CNTR-Transkriptionen fehlen die Worte in 01 und 03 (und in den CNTR-Texten von WH und SR); "
  "04, 05 und 032 haben sie."),
 ("Verse ohne SBLGNT-Text: [[MAT.17.21]] («Diese Art aber fährt nur durch Gebet und Fasten aus») steht nicht im SBLGNT und hat "
  "deshalb keinen Übersetzungstext; sein Wortlaut nach Treg und RP steht als Alternative zu [[MAT.17.20]]. Die automatische "
  "Zuordnung ordnet dort alle Zeugen dem kurzen Text zu, weil sie nur bis zum Ende von [[MAT.17.20]] vergleicht; es gilt der "
  "Apparat. Nach den CNTR-Transkriptionen haben 04, 05 und 032 den Vers, 01 und 03 nicht. Die Texteinheit "
  "TU-MAT-017-014-021 schliesst die Versnummer ein, damit die Gliederung lückenlos bleibt."),
 ("Erzählweise und Redegrenzen: Das erzählende Präsens ist beibehalten, wo Matthäus es hat ([[MAT.16.15]], [[MAT.17.1]], "
  "[[MAT.17.20]], [[MAT.17.25]]). ὅτι vor direkter Rede und einleitendes λέγων sind nicht eigens übersetzt. Anführungszeichen "
  "sind eine Entscheidung der Übersetzung, denn das Griechische hat keine."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig. Eigeti Formulierig; nöd us ere veröffentlichte Mundart-Bible übernoo.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Iiheitlichi Begriff fürs Matthäusevangelium: «s Riich vo de Himel», «de Mänschesohn», «Amen, ich säg eu», «Vatter i de "
  "Himel», «lueg» für ἰδού, «grad» für εὐθέως, «dänn» für τότε, «Schriftgelehrti», «Hoheprieschter», «Ältischti», «Dämon», "
  "«Gmeind», «Christus»."),
 ("Iiheitlich fürs ganz Evangelium: μακάριος «sälig»; ὀλιγόπιστος «chliigläubig», ὀλιγοπιστία "
  "«Chliiglaube»; σκανδαλίζω «z Fall bringe», passiv «Aastoss nää» oder «z Fall choo», σκάνδαλον «Fallstrick»; προσέρχομαι «härechoo»; "
  "ᾅδης «Totereich»; ἐγείρω im Passiv «uferweckt wärde»; γενεά «Generation»; ἀποκτείνω «umbringe»; γάρ meischt «nämli»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Petrus»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«de Sohn vom läbige Gott»); Futur oft mit Präsens («mach ich», «findsch»), wie s i de Mundart üblich isch."),
 ("Textbefund: [[MAT.16.2]]b–3 staat im SBLGNT; i 01 und 03 fehled d Wort nach de CNTR-Transkriptione. [[MAT.17.21]] fehlt "
  "im SBLGNT und hät kein Text; de Wortlut staat als Alternative bi [[MAT.17.20]]."),
]


def run():
    import json
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
            raise SystemExit(f"Kapitel {c}: unerwartete Verse ohne Tokens {sorted(missing)}")
        refs_c = [r for r in all_refs if r in toks]
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
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
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; Begriffe einheitlich für das Matthäusevangelium und abgestimmt auf die Markus-Parallelen. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_16_17.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 16–17 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
