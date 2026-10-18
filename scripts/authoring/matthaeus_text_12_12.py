#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 12 (Sabbatstreit, der erwählte Knecht, Beelzebul, das Zeichen des Jona, die Verwandten
Jesu) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen,
Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_12_12.py

Muster: scripts/authoring/johannes_text_01_03.py und scripts/authoring/markus_text_01_03.py. Die Übersetzung steht als
Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen daraus und stimmen deshalb
überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log. WORK-MAT besteht bereits und wird hier
nur referenziert, nicht geschrieben.

Abgrenzung: Dieses Werkzeug schreibt nur Kapitel 12 (TRANS-MAT-012-001-050-…, ALIGN-MAT-012-001-050-…, Texteinheiten
TU-MAT-012-…). Das bestehende Stück [[MAT.6.5-MAT.6.15]] (scripts/authoring/vaterunser.py) und andere Kapitel werden
nicht berührt. Die einheitlichen Begriffe für alle Matthäus-Bereiche (Reich der Himmel, Menschensohn, «siehe»/«lueg»,
Erfüllungsformel usw.) sind übernommen.

Besonderheiten:
- In Matthäus 12 fehlt im SBLGNT kein Vers (per Skript geprüft); alle 50 Verse haben Tokens.
- [[MAT.12.47]] steht im SBLGNT-Text; WH lässt den Vers aus. Das steht als Alternative.
- Parallelen: [[MRK.2.23-MRK.3.12]], [[MRK.3.22-MRK.3.35]], [[MRK.8.11-MRK.8.12]]. Gleiche griechische Wendungen sind
  möglichst gleich wiedergegeben wie in der Markus-Übersetzung (z. B. γενεά «Geschlecht»/«Generation»), eigene
  Wendungen des Matthäus eigens.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben in den Lesarten stammen aus der maschinellen Zuordnung
(METHOD-AUTO-COLLATION-V1, data/witness-readings/WREAD-CNTR-MAT-012-001-050) bzw. aus dem dort erfassten Wortlaut der
CNTR-Transkription, nicht aus eigener Prüfung der Handschriften. Zahlen zu Wortvorkommen sind per Skript aus den
SBLGNT-Tokens ermittelt.
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
CHAPTERS = ((12, 50),)

DE = {
 # ------------------------------------------------------------ Ähren am Sabbat
 "MAT.12.1": "[Zu]{1} [jener]{2} [Zeit]{3,4} [ging]{5} [Jesus]{6,7} [am Sabbat]{8,9} [durch]{10} [die Kornfelder]{11,12}. [Seine]{16} [Jünger]{13,15} [aber]{14} [hatten Hunger]{17} und{18} [fingen an]{19}, [Ähren]{21} [abzurupfen]{20} und{22} [zu essen]{23}.",
 "MAT.12.2": "[Die Pharisäer]{1,3} [aber]{2} [sahen es]{4} und [sagten]{5} [zu ihm]{6}: «[Siehe]{7}, [deine]{10} [Jünger]{8,9} [tun]{11}, [was]{12} [am Sabbat]{16,17} [zu tun]{15} [nicht]{13} [erlaubt ist]{14}.»",
 "MAT.12.3": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: «[Habt ihr]{6} [nicht]{5} [gelesen]{6}, [was]{7} [David]{9} [getan hat]{8}, [als]{10} [er]{11} und{12} [seine Begleiter]{13-15} [Hunger hatten]{11},",
 "MAT.12.4": "[wie]{1} [er]{2} [in]{3} [das Haus]{4,5} [Gottes]{6,7} [hineinging]{2} und{8} [sie]{13} [die Schaubrote]{9-12} [assen]{13}, [was]{14} [ihm]{18} [nicht]{15} [zu essen]{19} [erlaubt]{16} [war]{17}, [auch nicht]{20} [denen, die]{21} [bei]{22} [ihm]{23} waren, [sondern]{24,25} [allein]{28} [den Priestern]{26,27}?",
 "MAT.12.5": "[Oder]{1} [habt ihr]{3} [nicht]{2} [im]{4,5} [Gesetz]{6} [gelesen]{3}, [dass]{7} [die Priester]{10,11} [am Sabbat]{8,9} [im]{12,13} [Tempel]{14} [den Sabbat]{15,16} [entweihen]{17} und{18} [schuldlos]{19} [sind]{20}?",
 "MAT.12.6": "[Ich sage]{1} [euch]{3} [aber]{2}: [Hier]{9} [ist]{8} [Grösseres]{7} [als der]{5} [Tempel]{6}. ~4(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.12.7": "[Wenn]{1} [ihr]{3} [aber]{2} [erkannt hättet]{3}, [was]{4} [das heisst]{5}: ‹[Barmherzigkeit]{6} [will ich]{7} und{8} [nicht]{9} [Opfer]{10}›, [hättet ihr]{13} [die Schuldlosen]{14,15} [nicht]{11} [verurteilt]{13}. ~12(ἄν kennzeichnet die nicht eingetretene Folge; im Konjunktiv «hättet» enthalten)",
 "MAT.12.8": "[Denn]{2} [der Menschensohn]{6-9} [ist]{3} [Herr]{1} [über den Sabbat]{4,5}.»",
 # ------------------------------------------------------------ Die verdorrte Hand
 "MAT.12.9": "Und{1} [er ging]{2} [von dort]{3} [weiter]{2} und [kam]{4} [in]{5} [ihre]{8} [Synagoge]{6,7}.",
 "MAT.12.10": "Und{1} [siehe]{2}, da war [ein Mensch]{3}, [der]{5} [eine verdorrte]{6} [Hand]{4} [hatte]{5}. Und{7} [sie fragten]{8} [ihn]{9}: «[Ist es erlaubt]{11,12}, [am Sabbat]{13,14} [zu heilen]{15}?», [damit]{16} [sie]{17} [ihn]{18} [anklagen könnten]{17}. ~10(λέγοντες «sagend» leitet die direkte Rede ein)",
 "MAT.12.11": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: «[Wer]{5} [unter]{7} [euch]{8} [wäre]{6} [ein Mensch]{9}, [der]{10} [ein einziges]{13} [Schaf]{12} [hat]{11} und{14} [es]{24} [nicht]{22} [packen]{23} und{25} [herausziehen würde]{26}, [wenn]{15} [es]{17} [am Sabbat]{18,19} [in]{20} [eine Grube]{21} [fällt]{16}?",
 "MAT.12.12": "[Wie viel]{1} [ist]{3} [nun]{2} [ein Mensch]{4} [mehr wert]{3} [als ein Schaf]{5}! [Also]{6} [ist es]{7} [am Sabbat]{8,9} [erlaubt]{7}, [Gutes]{10} [zu tun]{11}.»",
 "MAT.12.13": "[Da]{1} [sagt er]{2} [zu dem Menschen]{3,4}: «[Streck]{5} [deine]{6} [Hand]{7,8} [aus]{5}!» Und{9} [er streckte sie aus]{10}, und{11} [sie wurde wieder]{12} [gesund]{13} [wie]{14} [die]{15} [andere]{16}.",
 "MAT.12.14": "[Die Pharisäer]{3,4} [aber]{2} [gingen hinaus]{1} [und hielten]{6} [Rat]{5} [gegen]{7} [ihn]{8}, [wie]{9} [sie]{11} [ihn]{10} [umbringen könnten]{11}.",
 # ------------------------------------------------------------ Der erwählte Knecht
 "MAT.12.15": "[Jesus]{1,3} [aber]{2} [merkte es]{4} und [zog sich]{5} [von dort]{6} [zurück]{5}. Und{7} [viele]{10} [folgten]{8} [ihm]{9}, und{11} [er heilte]{12} [sie]{13} [alle]{14}.",
 "MAT.12.16": "Und{1} [er gebot]{2} [ihnen]{3} [streng]{2}, [dass]{4} [sie]{8} [ihn]{7} [nicht]{5} [bekannt]{6} [machen sollten]{8},",
 "MAT.12.17": "[damit]{1} [erfüllt würde]{2}, [was]{3} [durch]{5} [Jesaja]{6}, [den Propheten]{7,8}, [gesagt ist]{4}: ~9(λέγοντος «der sagt» leitet das Zitat ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.12.18": "«[Siehe]{1}, [mein]{4} [Knecht]{2,3}, [den]{5} [ich erwählt habe]{6}, [mein]{9} [Geliebter]{7,8}, [an]{10} [dem]{11} [meine]{15} [Seele]{13,14} [Gefallen gefunden hat]{12}. [Ich werde]{16} [meinen]{19} [Geist]{17,18} [auf]{20} [ihn]{21} [legen]{16}, und{22} [er wird]{26} [den Völkern]{24,25} [das Recht]{23} [verkünden]{26}.",
 "MAT.12.19": "[Er wird]{2} [nicht]{1} [streiten]{2} [noch]{3} [schreien]{4}, [noch]{5} [wird]{6} [jemand]{7} [auf]{8} [den Strassen]{9,10} [seine]{13} [Stimme]{11,12} [hören]{6}.",
 "MAT.12.20": "[Ein geknicktes]{2} [Rohr]{1} [wird er]{4} [nicht]{3} [zerbrechen]{4}, und{5} [einen glimmenden]{7} [Docht]{6} [wird er]{9} [nicht]{8} [auslöschen]{9}, [bis]{10} [er]{12} [das Recht]{15,16} [zum]{13} [Sieg]{14} [geführt hat]{12}. ~11(ἄν lässt den Zeitpunkt offen; nicht eigens wiedergegeben)",
 "MAT.12.21": "Und{1} [auf seinen]{2,4} [Namen]{3} [werden]{6} [Völker]{5} [hoffen]{6}.»",
 # ------------------------------------------------------------ Beelzebul
 "MAT.12.22": "[Da]{1} [wurde]{2} [ein Besessener]{4} [zu ihm]{3} [gebracht]{2}, [der blind]{5} und{6} [stumm war]{7}; und{8} [er heilte]{9} [ihn]{10}, [sodass]{11} [der Stumme]{12,13} [redete]{14} und{15} [sah]{16}.",
 "MAT.12.23": "Und{1} [alle]{3} [Menschenmengen]{4,5} [gerieten ausser sich]{2} und{6} [sagten]{7}: «[Ist]{10} [das]{9} [vielleicht]{8} [der Sohn]{11,12} [Davids]{13}?»",
 "MAT.12.24": "[Als]{4} [aber]{2} [die Pharisäer]{1,3} [das hörten]{4}, [sagten sie]{5}: «[Der]{6} [treibt]{8} [die Dämonen]{9,10} [nicht]{7} [aus]{8}, [ausser]{11,12} [durch]{13} [Beelzebul]{14,15}, [den Herrscher]{16} [der Dämonen]{17,18}.»",
 "MAT.12.25": "[Er kannte]{1} [aber]{2} [ihre]{5} [Gedanken]{3,4} und [sagte]{6} [zu ihnen]{7}: «[Jedes]{8} [Reich]{9}, [das]{10} [gegen sich selbst]{11,12} [gespalten ist]{10}, [wird verwüstet]{13}, und{14} [jede]{15} [Stadt]{16} [oder]{17} [jedes Haus]{18}, [das]{19} [gegen sich selbst]{20,21} [gespalten ist]{19}, [wird]{23} [nicht]{22} [bestehen]{23}.",
 "MAT.12.26": "Und{1} [wenn]{2} [der Satan]{3,4} [den Satan]{5,6} [austreibt]{7}, [ist er]{10} [gegen sich selbst]{8,9} [gespalten]{10}. [Wie]{11} [wird]{13} [dann]{12} [sein]{16} [Reich]{14,15} [bestehen]{13}?",
 "MAT.12.27": "Und{1} [wenn]{2} [ich]{3} [durch]{4} [Beelzebul]{5} [die Dämonen]{7,8} [austreibe]{6}, [durch]{12} [wen]{13} [treiben]{14} [eure]{11} [Söhne]{9,10} sie [aus]{14}? [Darum]{15,16} [werden]{19} [sie]{17} [eure]{20} [Richter]{18} [sein]{19}.",
 "MAT.12.28": "[Wenn]{1} [ich]{6} [aber]{2} [durch]{3} [den Geist]{4} [Gottes]{5} [die Dämonen]{8,9} [austreibe]{7}, [dann]{10} [ist]{11} [das Reich Gottes]{14-17} [zu]{12} [euch]{13} [gekommen]{11}.",
 "MAT.12.29": "[Oder]{1} [wie]{2} [kann]{3} [jemand]{4} [in]{6} [das Haus]{7,8} [des Starken]{9,10} [hineingehen]{5} und{11} [seinen]{14} [Hausrat]{12,13} [rauben]{15}, [wenn]{16} [er]{19} [nicht]{17} [zuerst]{18} [den Starken]{20,21} [bindet]{19}? Und{22} [dann]{23} [wird er]{27} [sein]{26} [Haus]{24,25} [plündern]{27}.",
 "MAT.12.30": "[Wer]{1} [nicht]{2} [mit]{4} [mir]{5} [ist]{3}, [ist]{8} [gegen]{6} [mich]{7}, und{9} [wer]{10} [nicht]{11} [mit]{13} [mir]{14} [sammelt]{12}, [zerstreut]{15}.",
 "MAT.12.31": "[Darum]{1,2} [sage ich]{3} [euch]{4}: [Jede]{5} [Sünde]{6} und{7} [Lästerung]{8} [wird]{9} [den Menschen]{10,11} [vergeben werden]{9}, [die Lästerung]{12,16} [gegen den]{14} [Geist]{15} [aber]{13} [wird]{18} [nicht]{17} [vergeben werden]{18}.",
 "MAT.12.32": "Und{1} [wer]{2,3} [ein Wort]{5} [gegen]{6} [den Menschensohn]{7-10} [sagt]{4}, [dem]{12} [wird]{11} [vergeben werden]{11}; [wer]{13,15} [aber]{14} [gegen]{17} [den heiligen]{20,21} [Geist]{18,19} [redet]{16}, [dem]{24} [wird]{23} [nicht]{22} [vergeben werden]{23}, [weder]{25} [in]{26} [dieser]{27} [Weltzeit]{28,29} [noch]{30} [in]{31} [der]{32} [kommenden]{33}.",
 # ------------------------------------------------------------ Baum und Frucht
 "MAT.12.33": "[Entweder]{1} [macht]{2} [den Baum]{3,4} [gut]{5} und{6} [seine]{9} [Frucht]{7,8} [gut]{10}, [oder]{11} [macht]{12} [den Baum]{13,14} [faul]{15} und{16} [seine]{19} [Frucht]{17,18} [faul]{20}; [denn]{22} [an]{21} [der Frucht]{23,24} [wird]{27} [der Baum]{25,26} [erkannt]{27}.",
 "MAT.12.34": "[Ihr Vipernbrut]{1,2}! [Wie]{3} [könnt ihr]{4} [Gutes]{5} [reden]{6}, [da ihr]{8} [böse]{7} [seid]{8}? [Denn]{10} [aus]{9} [dem Überfluss]{11,12} [des Herzens]{13,14} [redet]{17} [der Mund]{15,16}.",
 "MAT.12.35": "[Der gute]{1,2} [Mensch]{3} [bringt]{8} [aus]{4} [dem guten]{5,6} [Schatz]{7} [Gutes]{9} [hervor]{8}, und{10} [der böse]{11,12} [Mensch]{13} [bringt]{18} [aus]{14} [dem bösen]{15,16} [Schatz]{17} [Böses]{19} [hervor]{18}.",
 "MAT.12.36": "[Ich sage]{1} [euch]{3} [aber]{2}: [Jedes]{5} [unnütze]{7} [Wort]{6}, [das]{8} [die Menschen]{10,11} [reden werden]{9} – [darüber]{13,14} [werden sie]{12} [am]{16} [Tag]{17} [des Gerichts]{18} [Rechenschaft]{15} [ablegen]{12}. ~4(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.12.37": "[Denn]{2} [aufgrund]{1} [deiner]{5} [Worte]{3,4} [wirst du]{6} [gerecht gesprochen werden]{6}, und{7} [aufgrund]{8} [deiner]{11} [Worte]{9,10} [wirst du]{12} [verurteilt werden]{12}.»",
 # ------------------------------------------------------------ Das Zeichen des Jona
 "MAT.12.38": "[Da]{1} [antworteten]{2} [ihm]{3} [einige]{4} [der]{5} [Schriftgelehrten]{6} und{7} [Pharisäer]{8}: «[Lehrer]{10}, [wir wollen]{11} [von]{12} [dir]{13} [ein Zeichen]{14} [sehen]{15}.» ~9(λέγοντες «sagend» leitet die direkte Rede ein)",
 "MAT.12.39": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4} [zu ihnen]{5}: «[Ein böses]{7} und{8} [ehebrecherisches]{9} [Geschlecht]{6} [verlangt]{11} [ein Zeichen]{10}, und{12} [kein]{14} [Zeichen]{13} [wird]{15} [ihm]{16} [gegeben werden]{15} [ausser]{17,18} [dem Zeichen]{19,20} [des Propheten]{22,23} [Jona]{21}.",
 "MAT.12.40": "[Denn]{2} [wie]{1} [Jona]{4} [drei]{10} [Tage]{11} und{12} [drei]{13} [Nächte]{14} [im]{5,6} [Bauch]{7} [des grossen Fisches]{8,9} [war]{3}, [so]{15} [wird]{16} [der Menschensohn]{17-20} [drei]{26} [Tage]{27} und{28} [drei]{29} [Nächte]{30} [im]{21,22} [Herzen]{23} [der Erde]{24,25} [sein]{16}.",
 "MAT.12.41": "[Die Männer]{1} [von Ninive]{2} [werden]{3} [beim]{4,5} [Gericht]{6} [mit]{7} [diesem]{10} [Geschlecht]{8,9} [aufstehen]{3} und{11} [es]{13} [verurteilen]{12}; [denn]{14} [sie sind]{15} [auf]{16} [die Verkündigung]{17,18} [des Jona]{19} [hin]{16} [umgekehrt]{15}, und{20} [siehe]{21}, [hier]{24} ist [mehr]{22} [als Jona]{23}.",
 "MAT.12.42": "[Die Königin]{1} [des Südens]{2} [wird sich]{3} [beim]{4,5} [Gericht]{6} [mit]{7} [diesem]{10} [Geschlecht]{8,9} [erheben]{3} und{11} [es]{13} [verurteilen]{12}; [denn]{14} [sie kam]{15} [von]{16} [den Enden]{17,18} [der Erde]{19,20}, um [die Weisheit]{22,23} [Salomos]{24} [zu hören]{21}, und{25} [siehe]{26}, [hier]{29} ist [mehr]{27} [als Salomo]{28}.",
 "MAT.12.43": "[Wenn]{1} [aber]{2} [der unreine]{3,4} [Geist]{5} [von]{7} [dem Menschen]{8,9} [ausgegangen ist]{6}, [zieht er]{10} [durch]{11} [wasserlose]{12} [Gegenden]{13} [und sucht]{14} [Ruhe]{15} und{16} [findet]{18} [keine]{17}.",
 "MAT.12.44": "[Dann]{1} [sagt er]{2}: ‹[Ich werde]{7} [in]{3} [mein]{6} [Haus]{4,5} [zurückkehren]{7}, [aus dem]{8} [ich]{9} [weggegangen bin]{9}.› Und{10} [wenn er kommt]{11}, [findet er]{12} es [leer]{13}, [gefegt]{14} und{15} [geschmückt]{16}.",
 "MAT.12.45": "[Dann]{1} [geht er hin]{2} und{3} [nimmt]{4} [sieben]{7} [andere]{8} [Geister]{9} [mit sich]{5,6}, [die böser sind]{10} [als er selbst]{11}; und{12} [sie gehen hinein]{13} [und wohnen]{14} [dort]{15}, und{16} [am Ende]{18,19} [steht es]{17} [um jenen]{20,22} [Menschen]{21} [schlimmer]{23} [als am Anfang]{24,25}. [So]{26} [wird es]{27} [auch]{28} [diesem]{31} [bösen]{32,33} [Geschlecht]{29,30} [ergehen]{27}.»",
 # ------------------------------------------------------------ Die Verwandten Jesu
 "MAT.12.46": "[Während]{1} [er]{3} [aber]{2} [noch]{1} [zu den Menschenmengen]{5,6} [redete]{4}, [siehe]{7}, [da standen]{14} [seine]{13} [Mutter]{8,9} und{10} seine [Brüder]{11,12} [draussen]{15} [und suchten]{16} [ihn]{17} [zu sprechen]{18}.",
 "MAT.12.47": "[Jemand]{3} [aber]{2} [sagte]{1} [zu ihm]{4}: «[Siehe]{5}, [deine]{8} [Mutter]{6,7} und{9} [deine]{12} [Brüder]{10,11} [stehen]{14} [draussen]{13} [und suchen]{15} [dich]{16} [zu sprechen]{17}.»",
 "MAT.12.48": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4} [zu dem]{5}, [der]{6} es [ihm]{7} [sagte]{6}: «[Wer]{8} [ist]{9} [meine]{12} [Mutter]{10,11}, und{13} [wer]{14} [sind]{15} [meine]{18} [Brüder]{16,17}?»",
 "MAT.12.49": "Und{1} [er streckte]{2} [seine]{5} [Hand]{3,4} [über]{6} [seine]{9} [Jünger]{7,8} [aus]{2} und [sagte]{10}: «[Siehe]{11}, [meine]{14} [Mutter]{12,13} und{15} [meine]{18} [Brüder]{16,17}!",
 "MAT.12.50": "[Denn]{2} [wer]{1,3} [den Willen]{5,6} [meines]{9} [Vaters]{7,8} [in]{10,11} [den Himmeln]{12} [tut]{4}, [der]{13} [ist]{20} [mein]{14} [Bruder]{15} und{16} meine [Schwester]{17} und{18} meine [Mutter]{19}.»",
}

GSW = {
 # ------------------------------------------------------------ Ähren am Sabbat
 "MAT.12.1": "[I]{1} [dere]{2} [Ziit]{3,4} [isch]{5} [de Jesus]{6,7} [am Sabbat]{8,9} [dur]{10} [d Chornfälder]{11,12} [gange]{5}. [Sini]{16} [Jünger]{13,15} [aber]{14} [händ Hunger gha]{17} und{18} [händ aagfange]{19}, [Ähre]{21} [abzrupfe]{20} und{22} [z ässe]{23}.",
 "MAT.12.2": "[D Pharisäer]{1,3} [aber]{2} [händ das gseh]{4} und [händ]{5} [zu ihm]{6} [gseit]{5}: «[Lueg]{7}, [dini]{10} [Jünger]{8,9} [mached]{11}, [was]{12} [am Sabbat]{16,17} [z mache]{15} [nöd]{13} [erlaubt isch]{14}.»",
 "MAT.12.3": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: «[Händ er]{6} [nöd]{5} [gläse]{6}, [was]{7} [de David]{9} [gmacht hät]{8}, [wo]{10} [er]{11} und{12} [sini Begleiter]{13-15} [Hunger gha händ]{11},",
 "MAT.12.4": "[wie]{1} [er]{2} [is]{3,4} [Huus]{5} [vo Gott]{6,7} [inegange isch]{2} und{8} [si]{13} [d Schaubrot]{9-12} [gässe händ]{13}, [was]{14} [ihm]{18} [nöd]{15} [erlaubt]{16} [gsii isch]{17} [z ässe]{19}, [au nöd]{20} [dene, wo]{21} [bi]{22} [ihm]{23} gsii sind, [sondern]{24,25} [nu]{28} [de Prieschter]{26,27}?",
 "MAT.12.5": "[Oder]{1} [händ er]{3} [nöd]{2} [im]{4,5} [Gsetz]{6} [gläse]{3}, [dass]{7} [d Prieschter]{10,11} [am Sabbat]{8,9} [im]{12,13} [Tämpel]{14} [de Sabbat]{15,16} [entheiliged]{17} und{18} [ohni Schuld]{19} [sind]{20}?",
 "MAT.12.6": "[Ich säg]{1} [eu]{3} [aber]{2}: [Da]{9} [isch]{8} [öppis Grössers]{7} [als de]{5} [Tämpel]{6}. ~4(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.12.7": "[Wänn]{1} [ir]{3} [aber]{2} [begriffe hetted]{3}, [was]{4} [das heisst]{5}: ‹[Barmhärzigkeit]{6} [wott ich]{7} und{8} [nöd]{9} [Opfer]{10}›, [dänn hetted ir]{13} [di Schuldlose]{14,15} [nöd]{11} [verurteilt]{13}. ~12(ἄν zeigt, dass d Folg nöd iitroffe isch; im «hetted» enthalte)",
 "MAT.12.8": "[Dänn]{2} [de Mänschesohn]{6-9} [isch]{3} [Herr]{1} [über de Sabbat]{4,5}.»",
 # ------------------------------------------------------------ Die verdorrte Hand
 "MAT.12.9": "Und{1} [er isch]{2} [vo dört]{3} [wiitergange]{2} und [isch]{4} [i]{5} [iri]{8} [Synagoge]{6,7} [choo]{4}.",
 "MAT.12.10": "Und{1} [lueg]{2}, da isch [en Mänsch]{3} gsii, [wo]{5} [e verdorreti]{6} [Hand]{4} [gha hät]{5}. Und{7} [si händ]{8} [en]{9} [gfröget]{8}: «[Isch es erlaubt]{11,12}, [am Sabbat]{13,14} [z heile]{15}?», [damit]{16} [si]{17} [en]{18} [chönted aachlage]{17}. ~10(λέγοντες «sägend» leitet di diräkt Red ii)",
 "MAT.12.11": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: «[Wer]{5} [under]{7} [eu]{8} [isch]{6} [en Mänsch]{9}, [wo]{10} [es einzigs]{13} [Schaf]{12} [hät]{11} und{14} [s]{24} [nöd]{22} [würd packe]{23} und{25} [usezie]{26}, [wänn]{15} [es]{17} [am Sabbat]{18,19} [in]{20} [e Gruebe]{21} [gheit]{16}?",
 "MAT.12.12": "[Wie vil]{1} [isch]{3} [en Mänsch]{4} [also]{2} [meh wärt]{3} [als es Schaf]{5}! [Drum]{6} [isch es]{7} [am Sabbat]{8,9} [erlaubt]{7}, [Guets]{10} [z tue]{11}.»",
 "MAT.12.13": "[Dänn]{1} [seit er]{2} [zum Mänsch]{3,4}: «[Streck]{5} [dini]{6} [Hand]{7,8} [us]{5}!» Und{9} [er hät si usgstreckt]{10}, und{11} [si isch wider]{12} [gsund]{13} [worde]{12} [wie]{14} [di]{15} [ander]{16}.",
 "MAT.12.14": "[D Pharisäer]{3,4} [aber]{2} [sind usegange]{1} [und händ]{6} [gäge]{7} [ihn]{8} [Raat]{5} [ghalte]{6}, [wie]{9} [si]{11} [en]{10} [chönted umbringe]{11}.",
 # ------------------------------------------------------------ Der erwählte Knecht
 "MAT.12.15": "[De Jesus]{1,3} [aber]{2} [hät das gmerkt]{4} und [hät sich]{5} [vo dört]{6} [zruggzoge]{5}. Und{7} [vili]{10} [sind]{8} [ihm]{9} [nachegange]{8}, und{11} [er hät]{12} [si]{13} [alli]{14} [gheilt]{12}.",
 "MAT.12.16": "Und{1} [er hät]{2} [ine]{3} [streng befole]{2}, [dass]{4} [si]{8} [en]{7} [nöd]{5} [bekannt]{6} [mache söled]{8},",
 "MAT.12.17": "[damit]{1} [erfüllt wird]{2}, [was]{3} [dur]{5} [de Jesaja]{6}, [de Prophet]{7,8}, [gseit worden isch]{4}: ~9(λέγοντος «wo seit» leitet s Zitat ii; mit em Doppelpunkt widergää)",
 "MAT.12.18": "«[Lueg]{1}, [min]{4} [Chnächt]{2,3}, [wo]{5} [ich userwählt han]{6}, [min]{9} [Gliebte]{7,8}, [a]{10} [däm]{11} [mini]{15} [Seel]{13,14} [Gfalle gfunde hät]{12}. [Ich wird]{16} [min]{19} [Geischt]{17,18} [uf]{20} [ihn]{21} [lege]{16}, und{22} [er wird]{26} [de Völker]{24,25} [s Rächt]{23} [verchünde]{26}.",
 "MAT.12.19": "[Er wird]{2} [nöd]{1} [strite]{2} [und nöd]{3} [schreie]{4}, [und niemer]{5,7} [wird]{6} [uf]{8} [de Straasse]{9,10} [sini]{13} [Stimm]{11,12} [ghöre]{6}.",
 "MAT.12.20": "[Es gchnickts]{2} [Rohr]{1} [wird er]{4} [nöd]{3} [verbreche]{4}, und{5} [en glimmende]{7} [Docht]{6} [wird er]{9} [nöd]{8} [uslösche]{9}, [bis]{10} [er]{12} [s Rächt]{15,16} [zum]{13} [Sieg]{14} [gfüert hät]{12}. ~11(ἄν laat de Ziitpunkt offe; nöd eigens widergää)",
 "MAT.12.21": "Und{1} [uf sin]{2,4} [Name]{3} [wärded]{6} [Völker]{5} [hoffe]{6}.»",
 # ------------------------------------------------------------ Beelzebul
 "MAT.12.22": "[Dänn]{1} [isch]{2} [en Bsässne]{4} [zu ihm]{3} [bracht worde]{2}, [wo blind]{5} und{6} [stumm gsii isch]{7}; und{8} [er hät]{9} [en]{10} [gheilt]{9}, [so dass]{11} [de Stumm]{12,13} [gredt]{14} und{15} [gseh hät]{16}.",
 "MAT.12.23": "Und{1} [alli]{3} [Lüüt]{4,5} [sind usser sich gsii]{2} und{6} [händ gseit]{7}: «[Isch]{10} [dä]{9} [ächt]{8} [de Sohn]{11,12} [vom David]{13}?»",
 "MAT.12.24": "[Wo]{4} [aber]{2} [d Pharisäer]{1,3} [das ghört händ]{4}, [händ si gseit]{5}: «[Dä]{6} [tribt]{8} [d Dämone]{9,10} [nu]{7,11,12} [dur]{13} [de Beelzebul]{14,15} [us]{8}, [de Herrscher]{16} [vo de Dämone]{17,18}.»",
 "MAT.12.25": "[Er hät]{1} [aber]{2} [iri]{5} [Gedanke]{3,4} [kännt]{1} und [hät]{6} [zu ine]{7} [gseit]{6}: «[Jedes]{8} [Riich]{9}, [wo]{10} [gäge sich sälber]{11,12} [gspalte isch]{10}, [wird verwüeschtet]{13}, und{14} [jedi]{15} [Stadt]{16} [oder]{17} [jedes Huus]{18}, [wo]{19} [gäge sich sälber]{20,21} [gspalte isch]{19}, [wird]{23} [nöd]{22} [bestaa]{23}.",
 "MAT.12.26": "Und{1} [wänn]{2} [de Satan]{3,4} [de Satan]{5,6} [ustribt]{7}, [isch er]{10} [gäge sich sälber]{8,9} [gspalte]{10}. [Wie]{11} [wird]{13} [also]{12} [sis]{16} [Riich]{14,15} [bestaa]{13}?",
 "MAT.12.27": "Und{1} [wänn]{2} [ich]{3} [dur]{4} [de Beelzebul]{5} [d Dämone]{7,8} [ustriibe]{6}, [dur]{12} [wän]{13} [triibed]{14} [eui]{11} [Söhn]{9,10} si [us]{14}? [Drum]{15,16} [wärded]{19} [si]{17} [eui]{20} [Richter]{18} [sii]{19}.",
 "MAT.12.28": "[Wänn]{1} [ich]{6} [aber]{2} [dur]{3} [de Geischt]{4} [vo Gott]{5} [d Dämone]{8,9} [ustriibe]{7}, [dänn]{10} [isch]{11} [s Riich vo Gott]{14-17} [zu]{12} [eu]{13} [choo]{11}.",
 "MAT.12.29": "[Oder]{1} [wie]{2} [cha]{3} [öpper]{4} [is]{6,7} [Huus]{8} [vom Starche]{9,10} [inegaa]{5} und{11} [sin]{14} [Huusraat]{12,13} [raube]{15}, [wänn]{16} [er]{19} [nöd]{17} [zerscht]{18} [de Starch]{20,21} [bindt]{19}? Und{22} [dänn]{23} [wird er]{27} [sis]{26} [Huus]{24,25} [plündere]{27}.",
 "MAT.12.30": "[Wer]{1} [nöd]{2} [mit]{4} [mir]{5} [isch]{3}, [isch]{8} [gäge]{6} [mich]{7}, und{9} [wer]{10} [nöd]{11} [mit]{13} [mir]{14} [sammlet]{12}, [verströit]{15}.",
 "MAT.12.31": "[Drum]{1,2} [säg ich]{3} [eu]{4}: [Jedi]{5} [Sünd]{6} und{7} [Läschterig]{8} [wird]{9} [de Mänsche]{10,11} [vergää]{9}, [d Läschterig]{12,16} [gäge de]{14} [Geischt]{15} [aber]{13} [wird]{18} [nöd]{17} [vergää]{18}.",
 "MAT.12.32": "Und{1} [wer]{2,3} [es Wort]{5} [gäge]{6} [de Mänschesohn]{7-10} [seit]{4}, [däm]{12} [wird]{11} [vergää]{11}; [wer]{13,15} [aber]{14} [gäge]{17} [de heilig]{18,20,21} [Geischt]{19} [redt]{16}, [däm]{24} [wird]{23} [nöd]{22} [vergää]{23}, [wäder]{25} [i]{26} [dere]{27} [Wältziit]{28,29} [no]{30} [i]{31} [de]{32} [chomende]{33}.",
 # ------------------------------------------------------------ Baum und Frucht
 "MAT.12.33": "[Entwäder]{1} [mached]{2} [de Baum]{3,4} [guet]{5} und{6} [sini]{9} [Frucht]{7,8} [guet]{10}, [oder]{11} [mached]{12} [de Baum]{13,14} [fuul]{15} und{16} [sini]{19} [Frucht]{17,18} [fuul]{20}; [dänn]{22} [a]{21} [de Frucht]{23,24} [erchännt me]{27} [de Baum]{25,26}.",
 "MAT.12.34": "[Ir Viperebruet]{1,2}! [Wie]{3} [chönd ir]{4} [Guets]{5} [rede]{6}, [wo ir]{8} [bös]{7} [sind]{8}? [Dänn]{10} [us]{9} [em Überfluss]{11,12} [vom Härz]{13,14} [redt]{17} [de Mund]{15,16}.",
 "MAT.12.35": "[De guet]{1,2} [Mänsch]{3} [holt]{8} [us]{4} [em guete]{5,6} [Schatz]{7} [Guets]{9} [füre]{8}, und{10} [de bös]{11,12} [Mänsch]{13} [holt]{18} [us]{14} [em böse]{15,16} [Schatz]{17} [Bös]{19} [füre]{18}.",
 "MAT.12.36": "[Ich säg]{1} [eu]{3} [aber]{2}: [Jedes]{5} [unnütze]{7} [Wort]{6}, [wo]{8} [d Mänsche]{10,11} [rede wärded]{9} – [drüber]{13,14} [wärded si]{12} [am]{16} [Tag]{17} [vom Gricht]{18} [Rächeschaft]{15} [ablege]{12}. ~4(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.12.37": "[Dänn]{2} [uf Grund vo]{1} [dine]{5} [Wort]{3,4} [wirsch]{6} [grächt gsproche]{6}, und{7} [uf Grund vo]{8} [dine]{11} [Wort]{9,10} [wirsch]{12} [verurteilt]{12}.»",
 # ------------------------------------------------------------ Das Zeichen des Jona
 "MAT.12.38": "[Dänn]{1} [händ]{2} [ihm]{3} [es paar]{4} [vo de]{5} [Schriftgelehrte]{6} und{7} [Pharisäer]{8} [gantwortet]{2}: «[Lehrer]{10}, [mir wänd]{11} [vo]{12} [dir]{13} [es Zeiche]{14} [gseh]{15}.» ~9(λέγοντες «sägend» leitet di diräkt Red ii)",
 "MAT.12.39": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [zu ine]{5} [gseit]{4}: «[E bösi]{7} und{8} [ehebrecherischi]{9} [Generation]{6} [verlangt]{11} [es Zeiche]{10}, und{12} [kei]{14} [Zeiche]{13} [wird]{15} [ere]{16} [gää]{15} [usser]{17,18} [s Zeiche]{19,20} [vom Prophet]{22,23} [Jona]{21}.",
 "MAT.12.40": "[Dänn]{2} [wie]{1} [de Jona]{4} [drüü]{10} [Täg]{11} und{12} [drüü]{13} [Nächt]{14} [im]{5,6} [Buuch]{7} [vom grosse Fisch]{8,9} [gsii isch]{3}, [eso]{15} [wird]{16} [de Mänschesohn]{17-20} [drüü]{26} [Täg]{27} und{28} [drüü]{29} [Nächt]{30} [im]{21,22} [Härz]{23} [vo de Ärde]{24,25} [sii]{16}.",
 "MAT.12.41": "[D Manne]{1} [vo Ninive]{2} [wärded]{3} [im]{4,5} [Gricht]{6} [mit]{7} [dere]{10} [Generation]{8,9} [ufstaa]{3} und{11} [si]{13} [verurteile]{12}; [dänn]{14} [si sind]{15} [uf]{16} [d Verchündigung]{17,18} [vom Jona]{19} [hii]{16} [umgchehrt]{15}, und{20} [lueg]{21}, [da]{24} isch [meh]{22} [als de Jona]{23}.",
 "MAT.12.42": "[D Königin]{1} [vom Süde]{2} [wird sich]{3} [im]{4,5} [Gricht]{6} [mit]{7} [dere]{10} [Generation]{8,9} [erhebe]{3} und{11} [si]{13} [verurteile]{12}; [dänn]{14} [si isch]{15} [vo]{16} [de Änd]{17,18} [vo de Ärde]{19,20} [choo]{15}, [zum]{21} [d Wiisheit]{22,23} [vom Salomo]{24} [ghöre]{21}, und{25} [lueg]{26}, [da]{29} isch [meh]{27} [als de Salomo]{28}.",
 "MAT.12.43": "[Wänn]{1} [aber]{2} [de unrein]{3,4} [Geischt]{5} [vom]{7,8} [Mänsch]{9} [usegange isch]{6}, [zieht er]{10} [dur]{11} [wasserlosi]{12} [Gägede]{13} [und suecht]{14} [Rue]{15} und{16} [findt]{18} [kei]{17}.",
 "MAT.12.44": "[Dänn]{1} [seit er]{2}: ‹[Ich gang]{7} [i]{3} [mis]{6} [Huus]{4,5} [zrugg]{7}, [vo wo]{8} [ich]{9} [usegange bin]{9}.› Und{10} [wänn er chunnt]{11}, [findt er]{12} s [leer]{13}, [gwüscht]{14} und{15} [gschmückt]{16}.",
 "MAT.12.45": "[Dänn]{1} [gaat er]{2} und{3} [nimmt]{4} [sibe]{7} [anderi]{8} [Geischter]{9} [mit sich]{5,6}, [wo böser sind]{10} [als er sälber]{11}; und{12} [si gönd ine]{13} [und wohned]{14} [dört]{15}, und{16} [am Schluss]{18,19} [isch es]{17} [mit däm]{20,22} [Mänsch]{21} [schlimmer]{23} [als am Aafang]{24,25}. [Eso]{26} [wirds]{27} [au]{28} [dere]{31} [böse]{32,33} [Generation]{29,30} [gaa]{27}.»",
 # ------------------------------------------------------------ Die Verwandten Jesu
 "MAT.12.46": "[Wo]{1} [er]{3} [aber]{2} [no]{1} [zu de Lüüt]{5,6} [gredt hät]{4}, [lueg]{7}, [da sind]{14} [sini]{13} [Mueter]{8,9} und{10} sini [Brüeder]{11,12} [dusse]{15} [gstande]{14} [und händ]{16} [mit ihm]{17} [rede]{18} [welle]{16}.",
 "MAT.12.47": "[Öpper]{3} [aber]{2} [hät]{1} [zu ihm]{4} [gseit]{1}: «[Lueg]{5}, [dini]{8} [Mueter]{6,7} und{9} [dini]{12} [Brüeder]{10,11} [stönd]{14} [dusse]{13} [und wänd]{15} [mit dir]{16} [rede]{17}.»",
 "MAT.12.48": "[Er]{1} [aber]{2} [hät]{3,4} [däm]{5}, [wo]{6} [ihm]{7} [das gseit hät]{6}, [gantwortet]{3,4}: «[Wer]{8} [isch]{9} [mini]{12} [Mueter]{10,11}, und{13} [wer]{14} [sind]{15} [mini]{18} [Brüeder]{16,17}?»",
 "MAT.12.49": "Und{1} [er hät]{2} [sini]{5} [Hand]{3,4} [gäge]{6} [sini]{9} [Jünger]{7,8} [usgstreckt]{2} und [gseit]{10}: «[Lueg]{11}, [mini]{14} [Mueter]{12,13} und{15} [mini]{18} [Brüeder]{16,17}!",
 "MAT.12.50": "[Dänn]{2} [wer]{1,3} [de Wile]{5,6} [vo mim]{7,9} [Vatter]{8} [i]{10,11} [de Himel]{12} [tuet]{4}, [dä]{13} [isch]{20} [min]{14} [Brueder]{15} und{16} mini [Schwöschter]{17} und{18} mini [Mueter]{19}.»",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MAT.12.1", "Zu jener Zeit", "literal", "Ἐν ἐκείνῳ τῷ καιρῷ", "In jener Zeit", None,
  "Lose Überleitungsformel des Matthäus (ebenso [[MAT.11.25]], [[MAT.14.1]]); sie verbindet mit dem Vorigen, ohne einen genauen Zeitpunkt zu nennen."),
 ("MAT.12.1", "am Sabbat", "adapted", "τοῖς σάββασιν", "an den Sabbaten", None,
  "Der Plural τὰ σάββατα bezeichnet oft einen einzelnen Sabbat (wohl nach der aramäischen Form des Wortes). Ebenso in [[MAT.12.5]], [[MAT.12.10]], [[MAT.12.11]] und [[MAT.12.12]]."),
 ("MAT.12.1", "hatten Hunger", "literal", "ἐπείνασαν", None, ["hungerten"],
  "Nur Matthäus nennt den Hunger der Jünger (vgl. [[MRK.2.23]]); er verbindet die Szene mit David, der Hunger hatte ([[MAT.12.3]]). Ähren auf einem fremden Feld mit der Hand abzurupfen, erlaubt [[DEU.23.25]]; der Vorwurf betrifft den Sabbat."),
 ("MAT.12.2", "Siehe", "literal", "Ἰδοὺ", None, ["Schau", "Sieh doch"],
  "Einheitliche Wiedergabe von ἰδού für alle Matthäus-Bereiche: «siehe» (Mundart «lueg»). Ebenso [[MAT.12.10]], [[MAT.12.18]], [[MAT.12.41]], [[MAT.12.42]], [[MAT.12.46]], [[MAT.12.47]], [[MAT.12.49]]."),
 ("MAT.12.4", "sie die Schaubrote assen", "literal", "τοὺς ἄρτους τῆς προθέσεως ἔφαγον", "die Brote der Auslegung assen sie", ["er die Schaubrote ass"],
  "«Schaubrote» folgt der vertrauten Wiedergabe für die zwölf Brote, die im Heiligtum vor Gott ausgelegt wurden ([[LEV.24.5-LEV.24.9]]; zur Begebenheit [[1SA.21.1-1SA.21.6]]). Der SBLGNT liest den Plural ἔφαγον («sie assen»), obwohl der Satz von David spricht; das Relativ ὃ («was») bezieht sich auf das Essen, nicht auf die Brote. Andere Lesarten siehe Alternativen."),
 ("MAT.12.5", "entweihen", "literal", "βεβηλοῦσιν", None, ["brechen", "entheiligen"],
  "Die Priester verrichten am Sabbat den vorgeschriebenen Opferdienst ([[NUM.28.9-NUM.28.10]]) und tun damit Arbeit, die sonst verboten ist. Nur Matthäus bringt dieses zweite Beispiel."),
 ("MAT.12.6", "Grösseres", "interpretive", "μεῖζόν", "ein Grösseres", ["einer, der grösser ist", "Grösseres als der Tempel"],
  "Das Wort ist sächlich. Gemeint sein kann Jesus selbst, das mit ihm anbrechende Reich oder die Barmherzigkeit, von der [[MAT.12.7]] spricht; die sächliche Form lässt das offen. Ebenso πλεῖον in [[MAT.12.41]] und [[MAT.12.42]]."),
 ("MAT.12.7", "Barmherzigkeit will ich und nicht Opfer", "literal", "Ἔλεος θέλω καὶ οὐ θυσίαν", None, ["Erbarmen will ich, nicht Opfer", "An Güte habe ich Gefallen, nicht am Opfer"],
  "Zitat aus [[HOS.6.6]] nach der Septuaginta; Matthäus führt es schon in [[MAT.9.13]] an. Gemeint ist nach verbreitetem Verständnis kein Verbot des Opfers, sondern ein Vorrang: Gott will zuerst Barmherzigkeit."),
 ("MAT.12.8", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", ["der Mensch"],
  "Einheitliche Wiedergabe für alle Matthäus-Bereiche, wie bei Markus. Bei Matthäus fehlt der Satz von [[MRK.2.27]] («Der Sabbat wurde für den Menschen geschaffen»); die Aussage begründet hier den Anspruch Jesu, der grösser ist als der Tempel ([[MAT.12.6]])."),
 ("MAT.12.8", "Herr über den Sabbat", "literal", "κύριος γάρ ἐστιν τοῦ σαββάτου", "Herr des Sabbats", None,
  "κύριος steht betont am Satzanfang."),
 ("MAT.12.10", "verdorrte", "literal", "ξηράν", "trockene", ["gelähmte", "abgestorbene"],
  "Wohl eine Lähmung oder ein Muskelschwund; wie in [[MRK.3.1]]."),
 ("MAT.12.10", "Ist es erlaubt", "literal", "Εἰ ἔξεστι", "Ob es erlaubt ist", None,
  "εἰ leitet hier, wie oft im neutestamentlichen Griechisch, eine direkte Frage ein. Bei Matthäus stellen die Gegner die Frage; bei Markus fragt Jesus ([[MRK.3.4]])."),
 ("MAT.12.11", "wäre", "adapted", "ἔσται", "wird sein", ["ist"],
  "Die Frage erwartet die Antwort «niemand». Das Futur ist mit der Möglichkeitsform wiedergegeben, damit die lange Frage im Deutschen trägt. Das Bildwort vom Schaf hat bei Markus keine Parallele (vgl. [[LUK.14.5]])."),
 ("MAT.12.12", "Gutes zu tun", "adapted", "καλῶς ποιεῖν", "gut zu handeln", ["wohlzutun"],
  "καλῶς ist ein Adverb («gut, recht»); «Gutes tun» gibt den Sinn natürlicher wieder."),
 ("MAT.12.14", "hielten Rat gegen ihn", "literal", "συμβούλιον ἔλαβον κατʼ αὐτοῦ", "nahmen einen Beschluss gegen ihn", ["fassten den Beschluss gegen ihn"],
  "συμβούλιον λαμβάνειν heisst «beraten» oder «beschliessen»; die Wiedergabe folgt [[MRK.3.6]]. ἀπολέσωσιν («vernichten, umbringen») wie dort mit «umbringen»."),
 ("MAT.12.16", "gebot ihnen streng", "interpretive", "ἐπετίμησεν αὐτοῖς", "fuhr sie an", ["schärfte ihnen ein", "verbot ihnen"],
  "ἐπιτιμάω heisst «zurechtweisen, anfahren», auch «nachdrücklich gebieten». Bei Markus richtet sich das Verb an die unreinen Geister ([[MRK.3.12]], dort «fuhr an»); bei Matthäus an die Geheilten, darum hier die Bedeutung «streng gebieten»."),
 ("MAT.12.17", "damit erfüllt würde, was durch Jesaja, den Propheten, gesagt ist", "traditional", "ἵνα πληρωθῇ τὸ ῥηθὲν διὰ Ἠσαΐου τοῦ προφήτου", None, ["sodass erfüllt wurde"],
  "Einheitliche Wiedergabe der Erfüllungsformel für alle Matthäus-Bereiche. ἵνα bezeichnet einen Zweck; manche lesen es hier als Folge («sodass»)."),
 ("MAT.12.18", "Knecht", "interpretive", "παῖς", "Kind", ["Diener", "Knabe"],
  "Zitat aus [[ISA.42.1-ISA.42.4]], im Wortlaut weder genau nach der Septuaginta noch nach dem hebräischen Text; die Septuaginta deutet den Knecht dort auf Jakob/Israel. παῖς heisst «Kind» und «Diener»; im Jesajatext ist der Knecht Gottes gemeint, darum «Knecht». «Mein Geliebter» und «Gefallen gefunden» klingen an die Himmelsstimme bei der Taufe an ([[MAT.3.17]]; vgl. [[MAT.17.5]])."),
 ("MAT.12.18", "meine Seele", "literal", "ἡ ψυχή μου", None, ["ich"],
  "ψυχή steht hier semitisch für die Person selbst: «an dem ich Gefallen gefunden habe»."),
 ("MAT.12.18", "das Recht", "interpretive", "κρίσιν", None, ["das Gericht", "die Gerechtigkeit", "das Urteil"],
  "κρίσις gibt im Jesajazitat das hebräische Wort für Recht und Rechtsordnung wieder; darum hier und in [[MAT.12.20]] «Recht». Wo κρίσις das Gericht Gottes meint ([[MAT.12.36]], [[MAT.12.41]], [[MAT.12.42]]), steht «Gericht»."),
 ("MAT.12.18", "den Völkern", "interpretive", "τοῖς ἔθνεσιν", None, ["den Heiden", "den Nationen"],
  "ἔθνη meint die Völker im Unterschied zu Israel. «Völker» hält offen, ob die Nichtjuden als Völker oder als einzelne Menschen gemeint sind. Ebenso [[MAT.12.21]]."),
 ("MAT.12.20", "das Recht zum Sieg geführt hat", "interpretive", "ἐκβάλῃ εἰς νῖκος τὴν κρίσιν", "das Recht hinausgeführt hat zum Sieg", ["dem Recht zum Sieg verholfen hat", "das Recht durchgesetzt hat"],
  "ἐκβάλλω heisst «hinauswerfen, hinausführen». Die Wendung «zum Sieg» weicht vom Jesajatext ab, der vom Hervorbringen des Rechts «in Treue» spricht."),
 ("MAT.12.21", "auf seinen Namen werden Völker hoffen", "literal", "τῷ ὀνόματι αὐτοῦ ἔθνη ἐλπιοῦσιν", None, None,
  "So auch die Septuaginta; der hebräische Text spricht von den Inseln (Küstenländern), die auf seine Weisung warten."),
 ("MAT.12.22", "ein Besessener", "literal", "δαιμονιζόμενος", "einer, der von einem Dämon beherrscht wird", None,
  "Einheitliche Wiedergabe für alle Matthäus-Bereiche: δαιμονιζόμενος «Besessener», δαιμόνιον «Dämon»."),
 ("MAT.12.22", "stumm", "interpretive", "κωφός", None, ["taub", "taubstumm"],
  "κωφός heisst «stumpf» und meint stumm oder taub; hier zeigt «redete», dass Stummheit gemeint ist (vgl. [[MAT.9.32-MAT.9.33]])."),
 ("MAT.12.23", "alle Menschenmengen", "literal", "πάντες οἱ ὄχλοι", None, ["alle Leute", "die ganze Menge"],
  "Gemeinsame Matthäus-Wiedergabe: ὄχλος «die Menge», οἱ ὄχλοι «die Menschenmengen». Matthäus braucht den Plural oft; die Übersetzung hält ihn sichtbar. Ebenso [[MAT.12.46]]."),
 ("MAT.12.23", "gerieten ausser sich", "literal", "ἐξίσταντο", None, ["staunten", "waren fassungslos"], None),
 ("MAT.12.23", "Ist das vielleicht der Sohn Davids", "interpretive", "Μήτι οὗτός ἐστιν ὁ υἱὸς Δαυίδ", None, ["Ist das etwa der Sohn Davids?", "Ist das nicht der Sohn Davids?"],
  "μήτι leitet eine Frage ein, die eher eine verneinende Antwort erwartet, oft aber auch zögernde Vermutung ausdrückt. «Vielleicht» gibt das Zögern wieder; «etwa» betonte den Zweifel, «nicht» machte daraus eine Behauptung. «Sohn Davids» ist bei Matthäus ein Messiastitel ([[MAT.1.1]], [[MAT.9.27]])."),
 ("MAT.12.24", "Beelzebul", "literal", "Βεελζεβοὺλ", None, ["Beelzebub"],
  "Name eines Dämonenherrschers; die Herkunft ist unsicher (Anklang an den Gott Baal-Sebub von Ekron, [[2KI.1.2]], oder Deutung als «Herr der Wohnung»; vgl. [[MAT.10.25]]). Die Form «Beelzebub» folgt der Vulgata. ἄρχων «Herrscher» wie in [[MRK.3.22]]."),
 ("MAT.12.25", "wird verwüstet", "literal", "ἐρημοῦται", "wird zur Wüste gemacht", ["zerfällt", "geht zugrunde"], None),
 ("MAT.12.25", "gegen sich selbst gespalten", "literal", "μερισθεῖσα καθʼ ἑαυτῆς", "geteilt gegen sich selbst", ["in sich uneins"],
  "Wie in [[MRK.3.24-MRK.3.25]]."),
 ("MAT.12.27", "eure Söhne", "literal", "οἱ υἱοὶ ὑμῶν", None, ["eure Leute", "eure Schüler"],
  "Gemeint sind wohl Angehörige oder Schüler der Angesprochenen, die selbst Dämonen austreiben."),
 ("MAT.12.28", "das Reich Gottes", "literal", "ἡ βασιλεία τοῦ θεοῦ", None, ["die Herrschaft Gottes"],
  "Einheitliche Wiedergabe für alle Matthäus-Bereiche. Matthäus sagt sonst meist «Reich der Himmel» (nach den SBLGNT-Tokens 32-mal); «Reich Gottes» nur hier und in [[MAT.19.24]], [[MAT.21.31]], [[MAT.21.43]]. Weshalb hier, ist offen (Übernahme aus einer Quelle, vgl. [[LUK.11.20]], oder Anklang an «Geist Gottes»)."),
 ("MAT.12.28", "zu euch gekommen", "interpretive", "ἔφθασεν ἐφʼ ὑμᾶς", "ist auf euch gekommen", ["hat euch erreicht", "ist über euch gekommen", "ist schon bei euch angekommen"],
  "φθάνω heisst «zuvorkommen, gelangen». Ob gemeint ist, das Reich sei schon da oder stehe unmittelbar bevor, wird verschieden beurteilt; der Aorist spricht eher für das Erste."),
 ("MAT.12.29", "plündern", "literal", "διαρπάσει", "ausrauben", None,
  "ἁρπάζω «rauben», διαρπάζω «ausplündern»; zweites wie in [[MRK.3.27]]. σκεύη (Geräte, Habe) «Hausrat»."),
 ("MAT.12.30", "zerstreut", "literal", "σκορπίζει", None, None,
  "Bild vom Sammeln der Herde oder der Ernte."),
 ("MAT.12.31", "Lästerung", "literal", "βλασφημία", None, ["Schmähung", "Verleumdung"],
  "βλασφημία meint verletzende Rede, gegen Menschen oder gegen Gott."),
 ("MAT.12.31", "die Lästerung gegen den Geist", "interpretive", "ἡ δὲ τοῦ πνεύματος βλασφημία", "die Lästerung des Geistes", None,
  "Der Genitiv bezeichnet den, gegen den sich die Lästerung richtet (vgl. [[MAT.12.32]]: «gegen den heiligen Geist»). Im Zusammenhang geht es darum, das Wirken des Geistes Gottes ([[MAT.12.28]]) dem Beelzebul zuzuschreiben ([[MAT.12.24]])."),
 ("MAT.12.32", "heiligen Geist", "literal", "πνεύματος τοῦ ἁγίου", None, ["Heiligen Geist"],
  "Einheitliche Wiedergabe für alle Matthäus-Bereiche: «heiliger Geist», klein geschrieben, weil das Griechische keine Grossschreibung kennt."),
 ("MAT.12.32", "Weltzeit", "interpretive", "αἰῶνι", None, ["Zeitalter", "Welt"],
  "Jüdische Unterscheidung von dieser und der kommenden Weltzeit. Die Wendung «weder … noch» unterstreicht, dass keine Vergebung erfolgt; über eine Vergebung nach dem Tod sagt der Satz nach verbreitetem Verständnis nichts aus."),
 ("MAT.12.33", "macht", "interpretive", "ποιήσατε", None, ["nehmt an", "setzt voraus"],
  "Der Imperativ fordert, Baum und Frucht als Einheit zu beurteilen. Viele verstehen ihn im Sinn von «nehmt an»; die Übersetzung bleibt beim Wortlaut. Vgl. [[MAT.7.17-MAT.7.18]]."),
 ("MAT.12.33", "faul", "interpretive", "σαπρὸν", None, ["schlecht", "verdorben", "morsch"],
  "σαπρός heisst «faul, verdorben», übertragen «schlecht, unbrauchbar». Ebenso [[MAT.7.17-MAT.7.18]]."),
 ("MAT.12.34", "Ihr Vipernbrut", "literal", "γεννήματα ἐχιδνῶν", "Erzeugnisse von Vipern", ["Schlangenbrut", "Otterngezücht"],
  "Ebenso [[MAT.3.7]] und [[MAT.23.33]]. «Otterngezücht» (Luther) ist veraltet."),
 ("MAT.12.34", "Überfluss", "literal", "περισσεύματος", None, ["Fülle"],
  "Was das Herz füllt, kommt aus dem Mund. Das Herz steht für das Innere, Denken und Wollen."),
 ("MAT.12.36", "unnütze", "interpretive", "ἀργὸν", "untätige", ["nichtige", "leere", "gedankenlose"],
  "ἀργός (aus ἀ- und ἔργον) heisst «untätig, nutzlos»: ein Wort, das nichts Gutes bewirkt."),
 ("MAT.12.36", "darüber werden sie", "literal", "ἀποδώσουσιν περὶ αὐτοῦ", "werden sie über es", None,
  "Der Satz beginnt mit «jedes unnütze Wort» und nimmt es mit «über es» wieder auf; der Gedankenstrich bildet diesen Bruch nach."),
 ("MAT.12.37", "gerecht gesprochen werden", "interpretive", "δικαιωθήσῃ", None, ["freigesprochen werden", "gerechtfertigt werden"],
  "Gerichtssprache als Gegenbegriff zu «verurteilt werden». Der Wechsel zur Anrede «du» macht den Satz zur allgemeinen Regel."),
 ("MAT.12.39", "Geschlecht", "traditional", "Γενεὰ", None, ["Generation"],
  "γενεά «Geschlecht, Generation» bezeichnet die Zeitgenossen, mit kritischem Unterton; wie in der Markus-Übersetzung ([[MRK.8.12]], [[MRK.8.38]]). Ebenso [[MAT.12.41]], [[MAT.12.42]], [[MAT.12.45]]."),
 ("MAT.12.39", "ehebrecherisches", "literal", "μοιχαλὶς", None, ["treuloses"],
  "Prophetisches Bild für Untreue gegen Gott (vgl. [[HOS.2.2]], [[JER.3.8-JER.3.9]]), nicht in erster Linie Vorwurf sexueller Verfehlung."),
 ("MAT.12.39", "ausser dem Zeichen des Propheten Jona", "literal", "εἰ μὴ τὸ σημεῖον Ἰωνᾶ τοῦ προφήτου", None, None,
  "Bei Markus fehlt die Ausnahme ([[MRK.8.12]]). Matthäus deutet das Zeichen in [[MAT.12.40]] auf die drei Tage, [[LUK.11.30]] auf Jona selbst als Zeichen für Ninive."),
 ("MAT.12.40", "des grossen Fisches", "interpretive", "τοῦ κήτους", "des Seeungeheuers", ["des Walfisches"],
  "κῆτος ist ein grosses Meerestier; so die Septuaginta in [[JON.1.17]], dessen Wortlaut der Vers aufnimmt. «Walfisch» (Luther) legt die Tierart fest, die der Text offen lässt."),
 ("MAT.12.40", "drei Tage und drei Nächte", "literal", "τρεῖς ἡμέρας καὶ τρεῖς νύκτας", None, None,
  "Wörtlich aus [[JON.1.17]]. Wie sich die Angabe zu «am dritten Tag» ([[MAT.16.21]]) verhält, wird verschieden erklärt, etwa mit jüdischer Zählweise, die angebrochene Tage mitrechnet."),
 ("MAT.12.40", "im Herzen der Erde", "interpretive", "ἐν τῇ καρδίᾳ τῆς γῆς", None, ["im Inneren der Erde"],
  "Meist auf das Grab bzw. das Totenreich bezogen."),
 ("MAT.12.41", "aufstehen", "interpretive", "ἀναστήσονται", None, ["auftreten", "auferstehen"],
  "Gerichtsbild: Sie treten als Zeugen gegen dieses Geschlecht auf. ἀνίστημι und ἐγείρω ([[MAT.12.42]], «sich erheben») sind auch Verben der Auferstehung; der Anklang ist möglich."),
 ("MAT.12.41", "umgekehrt", "literal", "μετενόησαν", "sinneswandelten", ["Busse getan", "haben ihre Gesinnung geändert"],
  "Einheitliche Wiedergabe für alle Matthäus-Bereiche: μετανοέω «umkehren», μετάνοια «Umkehr». Zu Ninive [[JON.3.5-JON.3.10]]."),
 ("MAT.12.41", "mehr als Jona", "interpretive", "πλεῖον Ἰωνᾶ", "Grösseres als Jona", ["einer, der mehr ist als Jona"],
  "πλεῖον ist sächlich wie μεῖζον in [[MAT.12.6]]; ebenso [[MAT.12.42]]."),
 ("MAT.12.42", "Die Königin des Südens", "literal", "βασίλισσα νότου", None, ["die Königin von Saba"],
  "Die Königin von Saba ([[1KI.10.1-1KI.10.10]]); «Süden» bezeichnet das ferne Südarabien."),
 ("MAT.12.43", "der unreine Geist", "literal", "τὸ ἀκάθαρτον πνεῦμα", None, None,
  "Wie bei Markus «unreiner Geist»; im Zusammenhang gleichbedeutend mit Dämon."),
 ("MAT.12.43", "wasserlose Gegenden", "literal", "ἀνύδρων τόπων", None, ["die Wüste"],
  "Die Wüste galt als Aufenthaltsort von Dämonen (vgl. [[ISA.13.21]], [[ISA.34.14]])."),
 ("MAT.12.44", "leer", "interpretive", "σχολάζοντα", "unbeschäftigt", ["unbewohnt", "frei"],
  "Das Haus steht leer: niemand hat den Platz eingenommen. Das Bildwort lässt offen, wer das Haus hätte füllen sollen."),
 ("MAT.12.45", "am Ende steht es um jenen Menschen schlimmer als am Anfang", "adapted", "γίνεται τὰ ἔσχατα τοῦ ἀνθρώπου ἐκείνου χείρονα τῶν πρώτων", "es werden die letzten Dinge jenes Menschen schlimmer als die ersten", None,
  "Die wörtliche Wendung ist im Deutschen schwer verständlich; Sinn und Zeitform (Präsens) sind erhalten."),
 ("MAT.12.45", "So wird es auch diesem bösen Geschlecht ergehen", "literal", "οὕτως ἔσται καὶ τῇ γενεᾷ ταύτῃ τῇ πονηρᾷ", "So wird es sein auch diesem bösen Geschlecht", None,
  "Nur Matthäus wendet das Bildwort ausdrücklich auf «dieses Geschlecht» an (vgl. [[LUK.11.24-LUK.11.26]])."),
 ("MAT.12.46", "Brüder", "literal", "ἀδελφοὶ", None, ["Halbbrüder", "Verwandte"],
  "ἀδελφός heisst «Bruder». Ob leibliche Brüder, Halbbrüder oder Vettern gemeint sind, ist zwischen den Konfessionen umstritten; die Übersetzung bleibt beim Wortlaut, wie bei Markus ([[MRK.6.3]]). Vgl. [[MAT.13.55]]."),
 ("MAT.12.46", "suchten ihn zu sprechen", "literal", "ζητοῦντες αὐτῷ λαλῆσαι", "suchend, mit ihm zu reden", ["wollten mit ihm reden"], None),
 ("MAT.12.50", "meines Vaters in den Himmeln", "literal", "τοῦ πατρός μου τοῦ ἐν οὐρανοῖς", None, ["meines Vaters im Himmel"],
  "Einheitliche Wiedergabe für alle Matthäus-Bereiche (Plural wie in [[MAT.6.9]]). Markus sagt «den Willen Gottes» ([[MRK.3.35]]); Matthäus spricht vom Vater, wie oft in seinem Evangelium."),
]

DEC_GSW = [
 ("MAT.12.1", "I dere Ziit", "literal", "Ἐν ἐκείνῳ τῷ καιρῷ", None, None,
  "Lockeri Überleitig vom Matthäus; si nännt kein gnaue Ziitpunkt."),
 ("MAT.12.1", "am Sabbat", "adapted", "τοῖς σάββασιν", "a de Sabbate", None,
  "De Plural meint oft en einzelne Sabbat. Gliich i [[MAT.12.5]], [[MAT.12.10]], [[MAT.12.11]] und [[MAT.12.12]]."),
 ("MAT.12.1", "händ Hunger gha", "literal", "ἐπείνασαν", None, None,
  "Nu de Matthäus nännt de Hunger vo de Jünger (vgl. [[MRK.2.23]]); das verbindet d Szene mit em David ([[MAT.12.3]]). Ähre abrupfe erlaubt [[DEU.23.25]]; de Vorwurf gaat um de Sabbat."),
 ("MAT.12.2", "Lueg", "literal", "Ἰδοὺ", "Lueg", None,
  "Iiheitlichi Widergaab vo ἰδού für alli Matthäus-Teil: «lueg»."),
 ("MAT.12.4", "d Schaubrot", "traditional", "τοὺς ἄρτους τῆς προθέσεως", "d Brot vo de Uuslegig", None,
  "Di zwölf Brot, wo im Heiligtum vor Gott uusgleit worde sind ([[LEV.24.5-LEV.24.9]]). De SBLGNT hät «si händ gässe» (Plural)."),
 ("MAT.12.6", "öppis Grössers", "interpretive", "μεῖζόν", "Grössers", ["eine, wo grösser isch"],
  "S Wort isch sächlich. Gmeint cha de Jesus sälber sii, s Riich, wo mit ihm chunnt, oder d Barmhärzigkeit vo [[MAT.12.7]]. Gliich πλεῖον i [[MAT.12.41]] und [[MAT.12.42]]."),
 ("MAT.12.7", "Barmhärzigkeit wott ich und nöd Opfer", "literal", "Ἔλεος θέλω καὶ οὐ θυσίαν", None, ["Erbarme wott ich, nöd Opfer"],
  "Zitat us [[HOS.6.6]]; scho i [[MAT.9.13]]."),
 ("MAT.12.8", "de Mänschesohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", None,
  "Iiheitlichi Widergaab für alli Matthäus-Teil, wie bim Markus."),
 ("MAT.12.11", "isch", "adapted", "ἔσται", "wird sii", None,
  "D Frag erwartet d Antwort «niemer». S Futur isch im Züritüütsch mit em Präsens widergää."),
 ("MAT.12.11", "gheit", "adapted", "ἐμπέσῃ", "inegheit", ["fallt"],
  "«Gheie» isch s gwöönlich Mundartwort für «falle»."),
 ("MAT.12.14", "Raat", "literal", "συμβούλιον", "en Beschluss", None,
  "Wie i [[MRK.3.6]]: «Raat ghalte»."),
 ("MAT.12.16", "streng befole", "interpretive", "ἐπετίμησεν", "aagfahre", ["iigschärft"],
  "ἐπιτιμάω heisst «zrächtwiise, aafahre», au «nachdrücklich befele». Bim Matthäus richtet sich s Verb a d Gheilte."),
 ("MAT.12.17", "damit erfüllt wird, was dur de Jesaja, de Prophet, gseit worden isch", "traditional", "ἵνα πληρωθῇ τὸ ῥηθὲν διὰ Ἠσαΐου τοῦ προφήτου", None, None,
  "Iiheitlichi Widergaab vo de Erfüllungsformle für alli Matthäus-Teil."),
 ("MAT.12.18", "Chnächt", "interpretive", "παῖς", "Chind", ["Diener"],
  "Zitat us [[ISA.42.1-ISA.42.4]]. παῖς heisst «Chind» und «Diener»; im Jesajatext isch de Chnächt vo Gott gmeint. «Min Gliebte» klingt a d Stimm bi de Taufi aa ([[MAT.3.17]])."),
 ("MAT.12.18", "s Rächt", "interpretive", "κρίσιν", None, ["s Gricht", "d Grächtigkeit"],
  "Im Jesajazitat meint κρίσις s Rächt; wo s Gricht vo Gott gmeint isch ([[MAT.12.36]], [[MAT.12.41]], [[MAT.12.42]]), staat «Gricht»."),
 ("MAT.12.18", "de Völker", "interpretive", "τοῖς ἔθνεσιν", None, ["de Heide"],
  "ἔθνη meint d Völker im Underschid zu Israel. Gliich [[MAT.12.21]]."),
 ("MAT.12.20", "s Rächt zum Sieg gfüert hät", "interpretive", "ἐκβάλῃ εἰς νῖκος τὴν κρίσιν", "s Rächt usegfüert hät zum Sieg", ["em Rächt zum Sieg verholfe hät"], None),
 ("MAT.12.22", "en Bsässne", "literal", "δαιμονιζόμενος", None, None,
  "Iiheitlichi Widergaab für alli Matthäus-Teil: δαιμονιζόμενος «Bsässne», δαιμόνιον «Dämon». κωφός heisst stumm oder taub; da zeigt «gredt», dass stumm gmeint isch."),
 ("MAT.12.23", "Lüüt", "adapted", "ὄχλοι", "Mängene", ["d Mängi"],
  "Gmeinsami Matthäus-Wiedergab: ὄχλος «d Mängi», οἱ ὄχλοι «d Lüüt», wil «Mängene» i de Mundart ungwohnt isch. Gliich [[MAT.12.46]]."),
 ("MAT.12.23", "ächt", "interpretive", "Μήτι", None, ["öppe", "nöd"],
  "μήτι leitet e Frag ii, wo eher e verneinendi Antwort erwartet, aber au zögerlichi Vermuetig usdrückt. S Mundartwort «ächt» trifft das Zögere. «Sohn vom David» isch bim Matthäus en Messiastitel ([[MAT.1.1]])."),
 ("MAT.12.24", "de Beelzebul", "literal", "Βεελζεβοὺλ", None, ["de Beelzebub"],
  "Name vo eme Dämoneherrscher; d Herkunft isch unsicher (vgl. [[2KI.1.2]], [[MAT.10.25]])."),
 ("MAT.12.28", "s Riich vo Gott", "literal", "ἡ βασιλεία τοῦ θεοῦ", None, None,
  "Iiheitlichi Widergaab. Susch seit de Matthäus meischtens «s Riich vo de Himel»; «s Riich vo Gott» nu da und i [[MAT.19.24]], [[MAT.21.31]], [[MAT.21.43]]."),
 ("MAT.12.31", "Läschterig", "literal", "βλασφημία", None, ["Schmähig"],
  "Verletzendi Red gäge Mänsche oder gäge Gott. «Gäge de Geischt»: De Genitiv nännt dä, wo d Läschterig gilt."),
 ("MAT.12.32", "de heilig Geischt", "literal", "τοῦ πνεύματος τοῦ ἁγίου", None, None,
  "Iiheitlichi Widergaab für alli Matthäus-Teil: «heilige Geischt», mit em Artikel «de heilig Geischt»."),
 ("MAT.12.32", "Wältziit", "interpretive", "αἰῶνι", None, ["Ziitalter", "Wält"],
  "Jüdischi Underscheidig vo dere und de chomende Wältziit."),
 ("MAT.12.33", "fuul", "interpretive", "σαπρὸν", None, ["schlächt", "verdorbe"],
  "σαπρός heisst «fuul, verdorbe», übertreit «schlächt». «Mached» bliibt bim Wortlut; vili verstönd s als «nämed aa»."),
 ("MAT.12.34", "Ir Viperebruet", "literal", "γεννήματα ἐχιδνῶν", None, ["Schlangebruet"],
  "Gliich [[MAT.3.7]] und [[MAT.23.33]]."),
 ("MAT.12.36", "unnütze", "interpretive", "ἀργὸν", "untätig", ["läär", "gedankelos"],
  "ἀργός heisst «untätig, nutzlos»: es Wort, wo nüüt Guets bewürkt."),
 ("MAT.12.37", "grächt gsproche", "interpretive", "δικαιωθήσῃ", None, ["freigsproche"],
  "Grichtssprooch als Gägebegriff zu «verurteilt»."),
 ("MAT.12.39", "Generation", "traditional", "Γενεὰ", None, ["Gschlächt"],
  "Wie i de Markus-Übersetzig ([[MRK.8.12]]). «Ehebrecherisch» isch es Prophetebild für Untröii gäge Gott."),
 ("MAT.12.40", "vom grosse Fisch", "interpretive", "τοῦ κήτους", "vom Meeruugheuer", ["vom Walfisch"],
  "κῆτος isch es grosses Meertier; so d Septuaginta i [[JON.1.17]]."),
 ("MAT.12.41", "umgchehrt", "literal", "μετενόησαν", None, None,
  "Iiheitlichi Widergaab für alli Matthäus-Teil: μετανοέω «umchehre»."),
 ("MAT.12.43", "usegange", "adapted", "ἐξέλθῃ", "usegange", ["usgfahre"],
  "Für unreini Geischter seit mer i de Mundart au «usfahre»; «usegange» bliibt nööch bim griechische Verb."),
 ("MAT.12.45", "am Schluss isch es mit däm Mänsch schlimmer als am Aafang", "adapted", "γίνεται τὰ ἔσχατα τοῦ ἀνθρώπου ἐκείνου χείρονα τῶν πρώτων", "es wärded di letschte Sache vo däm Mänsch schlimmer als di erschte", None, None),
 ("MAT.12.46", "Brüeder", "literal", "ἀδελφοὶ", None, ["Halbbrüeder", "Verwandti"],
  "Öb liiblichi Brüeder, Halbbrüeder oder Vettere gmeint sind, isch zwüsche de Konfessione umstritte; d Übersetzig bliibt bim Wortlut, wie bim Markus ([[MRK.6.3]])."),
 ("MAT.12.50", "vo mim Vatter i de Himel", "literal", "τοῦ πατρός μου τοῦ ἐν οὐρανοῖς", None, ["vo mim Vatter im Himel"],
  "Iiheitlichi Widergaab für alli Matthäus-Teil (wie [[MAT.6.9]])."),
]

# Lesarten-Alternativen (Variante:Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw,
#  Lesarten de, Lesarten gsw, Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings
#  (maschinelle Zuordnung) bzw. aus dem dort erfassten Wortlaut der CNTR-Transkription.
ALTS = [
 ("VAR-SBLGNTAPP-MAT-012-003-01:R2", "MAT.12.3", "als er und seine Begleiter Hunger hatten", "als er selbst und seine Begleiter Hunger hatten",
  "wo er und sini Begleiter Hunger gha händ", "wo er sälber und sini Begleiter Hunger gha händ", "gering",
  "Mit αὐτός liegt der Ton auf David selbst.", "Mit αὐτός liit de Ton uf em David sälber.",
  {"R1": [("ἐπείνασεν", "als er Hunger hatte", "WH, Treg, NA28")], "R2": [("ἐπείνασεν αὐτός", "als er selbst Hunger hatte", "RP")]},
  {"R1": [("ἐπείνασεν", "wo er Hunger gha hät", "WH, Treg, NA28")], "R2": [("ἐπείνασεν αὐτός", "wo er sälber Hunger gha hät", "RP")]},
  ["αὐτός kann aus der Parallele [[MRK.2.25]] (αὐτὸς καὶ οἱ μετʼ αὐτοῦ) übernommen sein; ebenso kann es als entbehrlich weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 05 und 032 ohne αὐτός."],
  ["αὐτός cha us de Parallele [[MRK.2.25]] übernoo sii; oder es isch wäggfalle, wil s nöd nötig isch.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 05 und 032 ohni αὐτός."]),
 ("VAR-SBLGNTAPP-MAT-012-004-01:R3", "MAT.12.4", "und sie die Schaubrote assen, was", "und er die Schaubrote ass, die",
  "und si d Schaubrot gässe händ, was", "und er d Schaubrot gässe hät, wo", "gering",
  "David isst allein, und der Relativsatz bezieht sich auf die Brote statt auf das Essen.",
  "De David isst elei, und de Relativsatz bezieht sich uf d Brot statt ufs Ässe.",
  {"R1": [("ἔφαγον, ὃ", "sie assen, was", "WH, NA28")], "R2": [("ἔφαγεν, ὃ", "er ass, was", "Treg")], "R3": [("ἔφαγεν οὓς", "er ass, die", "RP")]},
  {"R1": [("ἔφαγον, ὃ", "si händ gässe, was", "WH, NA28")], "R2": [("ἔφαγεν, ὃ", "er hät gässe, was", "Treg")], "R3": [("ἔφαγεν οὓς", "er hät gässe, wo", "RP")]},
  ["Der Plural ἔφαγον ist die schwierigere Lesart, weil der Satz von David spricht; der Singular kann an [[MRK.2.26]] (ἔφαγεν, οὓς) und [[LUK.6.4]] angeglichen sein, οὓς passt das Relativ grammatisch an die Brote an. Ebenso kann der Plural durch Angleichung an «die bei ihm waren» entstanden sein.",
   "Laut der automatischen Zuordnung liest 03 ἔφαγον ὃ, 05 und 032 ἔφαγεν ὃ, 04 ἔφαγεν οὕς. Für 01 ist die Zuordnung unklar; der erfasste Wortlaut lautet εφαγο¯ ουσ, also ἔφαγον mit οὕς."],
  ["De Plural ἔφαγον isch di schwierigeri Läsart, wil de Satz vom David redt; de Singular cha a [[MRK.2.26]] und [[LUK.6.4]] aagliche sii. Oder de Plural isch dur Aagliichig a «die, wo bi ihm gsii sind» entstande.",
   "Nach de automatische Zueornig liist 03 ἔφαγον ὃ, 05 und 032 ἔφαγεν ὃ, 04 ἔφαγεν οὕς. Bi 01 isch d Zueornig unklar; de erfasst Wortlut isch εφαγο¯ ουσ."]),
 ("VAR-SBLGNTAPP-MAT-012-010-01:R2", "MAT.12.10", "siehe, da war ein Mensch, der eine verdorrte Hand hatte", "siehe, da war ein Mensch, der die Hand verdorrt hatte",
  "en Mänsch gsii, wo e verdorreti Hand gha hät", "en Mänsch gsii, wo d Hand verdorret gha hät", "gering",
  "Der griechische Satz erhält ein Verb («war») und den Artikel vor «Hand»; der Sinn bleibt gleich.", "De griechisch Satz überchunnt es Verb («isch gsii») und de Artikel vor «Hand»; de Sinn bliibt gliich.",
  {"R1": [("ἄνθρωπος χεῖρα ἔχων ξηράν", "ein Mensch, der eine verdorrte Hand hatte", "WH, Treg, NA28")], "R2": [("ἄνθρωπος ἦν τὴν χεῖρα ἔχων ξηράν", "da war ein Mensch, der die Hand verdorrt hatte", "RP")]},
  {"R1": [("ἄνθρωπος χεῖρα ἔχων ξηράν", "en Mänsch, wo e verdorreti Hand gha hät", "WH, Treg, NA28")], "R2": [("ἄνθρωπος ἦν τὴν χεῖρα ἔχων ξηράν", "da isch en Mänsch gsii, wo d Hand verdorret gha hät", "RP")]},
  ["Der Zusatz glättet den Satz ohne Verb, vielleicht nach [[MRK.3.1]] (ἦν ἐκεῖ ἄνθρωπος); ebenso kann ἦν beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung liest 03 ohne Zusatz; 05 hat ἦν ἐκεῖ τὴν («war dort, die …») und wird R2 zugeordnet. 01, 04 und 032 führt die Zuordnung als «anders»; nach dem dort erfassten Wortlaut steht ἄνθρωπος als Kürzel ohne Zusatz, also wie im SBLGNT-Text."],
  ["De Zuesatz macht de Satz ohni Verb glatter, vilicht nach [[MRK.3.1]]; oder ἦν isch bim Abschriibe usgfalle.",
   "Nach de automatische Zueornig liist 03 ohni Zuesatz; 05 hät ἦν ἐκεῖ τὴν. 01, 04 und 032 füert d Zueornig als «andersch»; nach em erfasste Wortlut staat ἄνθρωπος als Chürzel ohni Zuesatz."]),
 ("VAR-SBLGNTAPP-MAT-012-015-01:R2", "MAT.12.15", "Und viele folgten ihm", "Und grosse Menschenmengen folgten ihm",
  "Und vili sind ihm nachegange", "Und vili Lüüt sind ihm nachegange", "gering",
  "«Viele» wird zu «grosse Menschenmengen» (ὄχλοι πολλοί, wie [[MAT.8.1]]); der Sinn bleibt nahezu gleich. Der SBLGNT folgt hier WH gegen Treg, RP und NA28.",
  "«Vili» wird zu «vili Lüüt»; de Sinn bliibt fascht gliich. De SBLGNT folgt da WH gäge Treg, RP und NA28.",
  {"R1": [("αὐτῷ πολλοί", "viele folgten ihm", "WH, NIV")], "R2": [("αὐτῷ ὄχλοι πολλοί", "grosse Menschenmengen folgten ihm", "Treg, RP, NA28")]},
  {"R1": [("αὐτῷ πολλοί", "vili sind ihm nachegange", "WH, NIV")], "R2": [("αὐτῷ ὄχλοι πολλοί", "vili Lüüt sind ihm nachegange", "Treg, RP, NA28")]},
  ["ὄχλοι kann nach der Wendung ὄχλοι πολλοί ergänzt sein, die Matthäus öfter braucht ([[MAT.4.25]], [[MAT.8.1]]); ebenso kann das Wort wegen der ähnlichen Endung (ΟΧΛΟΙ ΠΟΛΛΟΙ) beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne ὄχλοι, 04, 05 und 032 mit ihm."],
  ["ὄχλοι cha nach de Wändig ὄχλοι πολλοί ergänzt sii, wo de Matthäus öfter bruucht ([[MAT.4.25]], [[MAT.8.1]]); oder s Wort isch wäge de ähnliche Ändig usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni ὄχλοι, 04, 05 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-012-022-01:R2", "MAT.12.22", "Da wurde ein Besessener zu ihm gebracht", "Da brachte man einen Besessenen zu ihm",
  "Dänn isch en Bsässne zu ihm bracht worde", "Dänn händ si en Bsässne zu ihm bracht", "gering",
  "Aktiv statt Passiv; der Sinn bleibt gleich.", "Aktiv statt Passiv; de Sinn bliibt gliich.",
  {"R1": [("προσηνέχθη αὐτῷ δαιμονιζόμενος τυφλὸς καὶ κωφός", "wurde ein Besessener zu ihm gebracht, blind und stumm", "Treg, RP, NA28")],
   "R2": [("προσήνεγκαν αὐτῷ δαιμονιζόμενον τυφλὸν καὶ κωφόν", "brachte man einen Besessenen zu ihm, blind und stumm", "WH, NIV")]},
  {"R1": [("προσηνέχθη …", "isch en Bsässne zu ihm bracht worde", "Treg, RP, NA28")], "R2": [("προσήνεγκαν …", "händ si en Bsässne zu ihm bracht", "WH, NIV")]},
  ["Das Aktiv entspricht [[MAT.9.32]] (προσήνεγκαν αὐτῷ … δαιμονιζόμενον) und kann daran angeglichen sein; ebenso kann das Passiv eine stilistische Änderung sein.",
   "Laut der automatischen Zuordnung liest 03 das Aktiv, 01, 04, 05 und 032 das Passiv. 04 hat nach dem erfassten Wortlaut nur κωφός, ohne τυφλὸς καί."],
  ["S Aktiv entspricht [[MAT.9.32]] und cha dra aagliche sii; oder s Passiv isch e stilistischi Änderig.",
   "Nach de automatische Zueornig liist 03 s Aktiv, 01, 04, 05 und 032 s Passiv."]),
 ("VAR-SBLGNTAPP-MAT-012-022-02:R2", "MAT.12.22", "sodass der Stumme redete und sah", "sodass der Blinde und Stumme redete und sah",
  "so dass de Stumm gredt und gseh hät", "so dass de Blind und Stumm gredt und gseh hät", "gering",
  "Der Satz nennt beide Leiden wie am Versanfang.", "De Satz nännt beidi Leide wie am Versaafang.",
  {"R1": [("κωφὸν", "der Stumme", "WH, Treg, NA28")], "R2": [("τυφλὸν καὶ κωφὸν καὶ", "der Blinde und Stumme sowohl (redete als auch sah)", "RP")]},
  {"R1": [("κωφὸν", "de Stumm", "WH, Treg, NA28")], "R2": [("τυφλὸν καὶ κωφὸν καὶ", "de Blind und Stumm", "RP")]},
  ["Der Zusatz gleicht an den Versanfang an («blind und stumm»); ebenso kann «blind» ausgefallen sein, weil das Sehen ohnehin folgt.",
   "Laut der automatischen Zuordnung lesen 01, 03, 05 und 032 κωφόν allein, 04 mit Zusatz. Nach dem erfassten Wortlaut hat 032 allerdings κωφὸν καὶ τυφλόν (in umgekehrter Reihenfolge), was die Zuordnung dennoch R1 zuweist."],
  ["De Zuesatz glicht a de Versaafang aa; oder «blind» isch usgfalle, wil s Gseh sowiso folgt.",
   "Nach de automatische Zueornig läsed 01, 03, 05 und 032 κωφόν elei, 04 mit Zuesatz. Nach em erfasste Wortlut hät 032 aber κωφὸν καὶ τυφλόν (umgekehrti Reihefolg), wo d Zueornig glich R1 zuewiist."]),
 ("VAR-SBLGNTAPP-MAT-012-025-01:R2", "MAT.12.25", "Er kannte aber ihre Gedanken", "Jesus aber kannte ihre Gedanken",
  "Er hät aber iri Gedanke kännt", "De Jesus aber hät iri Gedanke kännt", "gering",
  "Jesus wird ausdrücklich genannt.", "De Jesus wird usdrücklich gnännt.",
  {"R1": [("δὲ", "er aber", "WH, Treg, NA28")], "R2": [("δὲ ὁ Ἰησοῦς", "Jesus aber", "RP")]},
  {"R1": [("δὲ", "er aber", "WH, Treg, NA28")], "R2": [("δὲ ὁ Ἰησοῦς", "de Jesus aber", "RP")]},
  ["Der Name verdeutlicht das Subjekt, wie häufig am Beginn eines Leseabschnitts; ebenso kann er ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 (auch korrigiert), 03, 04, 05 und 032 ohne den Namen."],
  ["De Name macht s Subjekt düütlich, wie oft am Aafang vo eme Läseabschnitt; oder er isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 05 und 032 ohni de Name."]),
 ("VAR-SBLGNTAPP-MAT-012-029-01:R2", "MAT.12.29", "seinen Hausrat rauben", "seinen Hausrat plündern",
  "sin Huusraat raube", "sin Huusraat plündere", "gering",
  "Beide Male steht dasselbe Verb («plündern»).", "Beidi Mal staat s gliich Verb («plündere»).",
  {"R1": [("ἁρπάσαι", "rauben", "WH, Treg, NA28")], "R2": [("διαρπάσαι", "plündern", "RP")]},
  {"R1": [("ἁρπάσαι", "raube", "WH, Treg, NA28")], "R2": [("διαρπάσαι", "plündere", "RP")]},
  ["διαρπάσαι gleicht an διαρπάσει am Versende und an [[MRK.3.27]] an; ebenso kann das einfache Verb eine Vereinfachung sein.",
   "Laut der automatischen Zuordnung lesen 01 und 05 διαρπάσαι, 03, 04 und 032 ἁρπάσαι."],
  ["διαρπάσαι glicht a s Verb am Versänd und a [[MRK.3.27]] aa; oder s eifach Verb isch e Vereifachig.",
   "Nach de automatische Zueornig läsed 01 und 05 διαρπάσαι, 03, 04 und 032 ἁρπάσαι."]),
 ("VAR-SBLGNTAPP-MAT-012-031-01:R2", "MAT.12.31", "wird nicht vergeben werden.", "wird den Menschen nicht vergeben werden.",
  "wird nöd vergää.", "wird de Mänsche nöd vergää.", "gering",
  "Der Zusatz wiederholt «den Menschen» aus der ersten Vershälfte.", "De Zuesatz widerholt «de Mänsche» us de erschte Vershälfti.",
  {"R1": [("ἀφεθήσεται", "wird nicht vergeben werden", "WH, Treg, NA28")], "R2": [("ἀφεθήσεται τοῖς ἀνθρώποις", "wird den Menschen nicht vergeben werden", "RP")]},
  {"R1": [("ἀφεθήσεται", "wird nöd vergää", "WH, Treg, NA28")], "R2": [("ἀφεθήσεται τοῖς ἀνθρώποις", "wird de Mänsche nöd vergää", "RP")]},
  ["Der Zusatz gleicht an die erste Vershälfte an; ebenso kann er als überflüssig weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 03 ohne Zusatz, 04, 05 und 032 mit ihm. 01 führt sie als «anders»; der erfasste Wortlaut endet mit ουκ αφεθησετε. Auch für die Ausgaben WH und SR meldet sie «anders»; der Apparat führt WH bei R1, das gilt, die Abweichung der Zuordnung ist ungeklärt."],
  ["De Zuesatz glicht a di erscht Vershälfti aa; oder er isch wäggloo worde, wil er überflüssig isch.",
   "Nach de automatische Zueornig liist 03 ohni Zuesatz, 04, 05 und 032 mit. 01 füert si als «andersch». Au für d Usgabe WH und SR meldet si «andersch»; de Apparat füert WH bi R1, das gilt."]),
 ("VAR-SBLGNTAPP-MAT-012-032-01:R2", "MAT.12.32", "in dieser Weltzeit", "in der jetzigen Weltzeit",
  "i dere Wältziit", "i de jetzige Wältziit", "gering",
  "«Die jetzige» statt «diese» Weltzeit; der Sinn bleibt gleich.", "«Di jetzig» statt «die» Wältziit; de Sinn bliibt gliich.",
  {"R1": [("τούτῳ τῷ αἰῶνι", "dieser Weltzeit", "WH, Treg, NA28")], "R2": [("τῷ νῦν αἰῶνι", "der jetzigen Weltzeit", "RP")]},
  {"R1": [("τούτῳ τῷ αἰῶνι", "dere Wältziit", "WH, Treg, NA28")], "R2": [("τῷ νῦν αἰῶνι", "de jetzige Wältziit", "RP")]},
  ["τῷ νῦν αἰῶνι ist eine geläufige Wendung (vgl. [[1TI.6.17]], [[TIT.2.12]]) und kann die andere ersetzt haben; ebenso umgekehrt.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 05 und 032 τούτῳ τῷ. Sie ordnet auch den Text von RP (ED-RP) R1 zu, gegen den Apparat; es gilt der Apparat, die Unsicherheit bleibt (möglicherweise liegen verschiedene Fassungen von RP zugrunde)."],
  ["τῷ νῦν αἰῶνι isch e gläufigi Wändig (vgl. [[1TI.6.17]], [[TIT.2.12]]) und cha di ander ersetzt ha; oder umgekehrt.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 05 und 032 τούτῳ τῷ. Si ordnet au de Text vo RP R1 zue, gäge de Apparat; es gilt de Apparat, d Unsicherheit bliibt."]),
 ("VAR-SBLGNTAPP-MAT-012-036-01:R2", "MAT.12.36", "das die Menschen reden werden", "das die Menschen etwa reden",
  "wo d Mänsche rede wärded", "wo d Mänsche öppe redid", "gering",
  "Allgemeiner Fall statt Zukunft; der Sinn bleibt nahezu gleich.", "Allgemeine Fall statt Zuekunft; de Sinn bliibt fascht gliich.",
  {"R1": [("λαλήσουσιν", "reden werden", "WH, Treg, NA28")], "R2": [("ἐὰν λαλήσωσιν", "etwa reden", "RP")]},
  {"R1": [("λαλήσουσιν", "rede wärded", "WH, Treg, NA28")], "R2": [("ἐὰν λαλήσωσιν", "öppe redid", "RP")]},
  ["ἐάν mit Konjunktiv ist die übliche verallgemeinernde Form nach einem Relativ und kann das Futur glätten; ebenso kann das Futur an ἀποδώσουσιν angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01 (auch korrigiert), 03 und 05 ohne ἐάν (05 nach dem erfassten Wortlaut im Präsens λαλοῦσιν), 032 ἐὰν λαλήσωσιν; 04 hat ἐὰν λαλήσουσιν und wird R2 zugeordnet."],
  ["ἐάν mit Konjunktiv isch di üblich verallgemeinerndi Form und cha s Futur glätte; oder s Futur isch a ἀποδώσουσιν aagliche.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni ἐάν, 032 ἐὰν λαλήσωσιν; 04 hät ἐὰν λαλήσουσιν."]),
 ("VAR-SBLGNTAPP-MAT-012-038-01:R2", "MAT.12.38", "Da antworteten ihm einige", "Da antworteten einige",
  "Dänn händ ihm es paar", "Dänn händ es paar", "gering",
  "Ohne «ihm»; der Sinn bleibt gleich.", "Ohni «ihm»; de Sinn bliibt gliich.",
  {"R1": [("αὐτῷ", "ihm", "WH, Treg, NA28")], "R2": [("–", "(fehlt)", "RP")]},
  {"R1": [("αὐτῷ", "ihm", "WH, Treg, NA28")], "R2": [("–", "(fehlt)", "RP")]},
  ["αὐτῷ kann als selbstverständlich weggefallen oder zur Verdeutlichung ergänzt worden sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 mit αὐτῷ, 032 ohne."],
  ["αὐτῷ cha wäggfalle sii, wil s sälbverständlich isch, oder zur Verdüütlichung ergänzt.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 mit αὐτῷ, 032 ohni."]),
 ("VAR-SBLGNTAPP-MAT-012-044-02:R2", "MAT.12.44", "findet er es leer", "findet er das Haus leer",
  "findt er s leer", "findt er s Huus leer", "gering",
  "Das Haus wird ausdrücklich genannt.", "S Huus wird usdrücklich gnännt.",
  {"R1": [("εὑρίσκει", "findet er (es)", "WH, Treg, RP, NA28")], "R2": [("εὑρίσκει τὸν οἶκον", "findet er das Haus", "NIV")]},
  {"R1": [("εὑρίσκει", "findt er s", "WH, Treg, RP, NA28")], "R2": [("εὑρίσκει τὸν οἶκον", "findt er s Huus", "NIV")]},
  ["Der Zusatz macht das im Griechischen fehlende Objekt ausdrücklich; dass er ausgefallen wäre, ist ebenso denkbar.",
   "Laut der automatischen Zuordnung liest 05 τὸν οἶκον, 01 (auch korrigiert), 03, 04 und 032 lesen ohne."],
  ["De Zuesatz macht s Objekt usdrücklich, wo im Griechische fehlt; dass er usgfalle wär, isch gliich denkbar.",
   "Nach de automatische Zueornig liist 05 τὸν οἶκον, 01, 03, 04 und 032 läsed ohni."]),
 ("VAR-SBLGNTAPP-MAT-012-047-01:R2", "MAT.12.47",
  "Jemand aber sagte zu ihm: «Siehe, deine Mutter und deine Brüder stehen draussen und suchen dich zu sprechen.»", "(Vers fehlt)",
  "Öpper aber hät zu ihm gseit: «Lueg, dini Mueter und dini Brüeder stönd dusse und wänd mit dir rede.»", "(Vers fehlt)", "mittel",
  "Ohne den Vers antwortet Jesus in [[MAT.12.48]] «dem, der es ihm sagte», ohne dass zuvor jemand gesprochen hat. WH lässt den Vers aus; der SBLGNT hat ihn mit Treg, NA28 und RP.",
  "Ohni de Vers antwortet de Jesus i [[MAT.12.48]] «däm, wo ihm das gseit hät», ohni dass vorher öpper gredt hät. WH laat de Vers wäg.",
  {"R1": [("εἶπεν δέ τις αὐτῷ … λαλῆσαι", "Jemand aber sagte zu ihm: … zu sprechen.", "Treg, NA28, RP")], "R2": [("–", "(Vers fehlt)", "WH")]},
  {"R1": [("εἶπεν δέ τις αὐτῷ … λαλῆσαι", "Öpper aber hät zu ihm gseit: … rede.", "Treg, NA28, RP")], "R2": [("–", "(Vers fehlt)", "WH")]},
  ["Der Vers kann durch Augensprung ausgefallen sein: [[MAT.12.46]] und [[MAT.12.47]] enden beide mit λαλῆσαι. Ebenso kann er nach [[MRK.3.32]] und [[LUK.8.20]] ergänzt worden sein, um den Bezug von [[MAT.12.48]] herzustellen.",
   "Laut der automatischen Zuordnung fehlt der Vers in 01 (Erstschrift); 04, 05 und 032 haben ihn (05 nach dem erfassten Wortlaut mit εἱστήκεισαν ἔξω und ohne σοι). Für 03 meldet die Zuordnung die Stelle als nicht erhalten (lacuna); ob das eine Auslassung des Verses wiedergibt oder auf die Zuordnung zurückgeht, ist hier nicht geprüft."],
  ["De Vers cha dur en Augesprung usgfalle sii: [[MAT.12.46]] und [[MAT.12.47]] händ beid am Schluss λαλῆσαι. Oder er isch nach [[MRK.3.32]] und [[LUK.8.20]] ergänzt worde, damit [[MAT.12.48]] en Bezug hät.",
   "Nach de automatische Zueornig fehlt de Vers i 01 (Erschtschrift); 04, 05 und 032 händ en. Für 03 meldet d Zueornig d Stell als nöd erhalte (lacuna); öb das e Uslassig vom Vers widergit oder vo de Zueornig chunnt, isch da nöd prüeft."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-012-001-050", "MAT.12.1-MAT.12.50", "section", "Streit um den Sabbat, Beelzebul und das Zeichen des Jona",
  ["TU-MAT-012-001-008", "TU-MAT-012-009-014", "TU-MAT-012-015-021", "TU-MAT-012-022-032", "TU-MAT-012-033-037",
   "TU-MAT-012-038-045", "TU-MAT-012-046-050"],
  "Als seine Jünger am Sabbat Ähren abrupfen, sagen die Pharisäer zu Jesus, sie täten, was am Sabbat nicht erlaubt sei; Jesus verweist auf David und die Priester, sagt, hier sei Grösseres als der Tempel, und nennt den Menschensohn Herrn über den Sabbat. In der Synagoge heilt er am Sabbat eine verdorrte Hand, und die Pharisäer beraten, wie sie ihn umbringen könnten. Jesus zieht sich zurück, heilt alle, die ihm folgen, und gebietet ihnen streng, ihn nicht bekannt zu machen; der Evangelist sieht darin das Wort Jesajas vom erwählten Knecht erfüllt. Als Jesus einen blinden und stummen Besessenen heilt, sagen die Pharisäer, er treibe die Dämonen durch Beelzebul aus; Jesus antwortet, ein gespaltenes Reich könne nicht bestehen, treibe er durch den Geist Gottes aus, sei das Reich Gottes zu ihnen gekommen, und die Lästerung gegen den Geist werde nicht vergeben. An der Frucht werde der Baum erkannt; aus dem Überfluss des Herzens rede der Mund, und aufgrund seiner Worte werde man gerecht gesprochen oder verurteilt. Schriftgelehrten und Pharisäern, die ein Zeichen verlangen, sagt er, diesem Geschlecht werde kein Zeichen gegeben werden ausser dem Zeichen des Jona, und wendet das Bildwort vom zurückkehrenden unreinen Geist auf dieses Geschlecht an. Als seine Mutter und seine Brüder ihn sprechen wollen, nennt er jeden, der den Willen seines Vaters in den Himmeln tut, seinen Bruder, seine Schwester und seine Mutter.", SEG),
 ("TU-MAT-012-001-008", "MAT.12.1-MAT.12.8", "dialogue", "Ährenrupfen am Sabbat", None,
  "Zu jener Zeit geht Jesus am Sabbat durch die Kornfelder; seine Jünger haben Hunger, rupfen Ähren ab und essen. Die Pharisäer sagen zu Jesus, seine Jünger täten, was am Sabbat nicht erlaubt sei. Jesus erinnert an David, der mit seinen Begleitern im Haus Gottes die Schaubrote ass, die allein den Priestern erlaubt waren, und an die Priester, die am Sabbat im Tempel den Sabbat entweihen und doch schuldlos sind. Hier sei Grösseres als der Tempel; hätten sie verstanden, was «Barmherzigkeit will ich und nicht Opfer» ([[HOS.6.6]]) heisst, hätten sie die Schuldlosen nicht verurteilt. Denn der Menschensohn ist Herr über den Sabbat.", None),
 ("TU-MAT-012-009-014", "MAT.12.9-MAT.12.14", "narrative", "Die Heilung der verdorrten Hand", None,
  "In ihrer Synagoge ist ein Mensch mit einer verdorrten Hand. Jesus wird gefragt, ob es erlaubt sei, am Sabbat zu heilen, damit man ihn anklagen könne. Er fragt zurück, wer von ihnen ein Schaf, das am Sabbat in eine Grube fällt, nicht herausziehen würde; ein Mensch sei viel mehr wert als ein Schaf, also sei es erlaubt, am Sabbat Gutes zu tun. Er sagt zu dem Menschen, er solle die Hand ausstrecken; der streckt sie aus, und sie wird gesund wie die andere. Die Pharisäer gehen hinaus und halten Rat, wie sie ihn umbringen könnten.", None),
 ("TU-MAT-012-015-021", "MAT.12.15-MAT.12.21", "narrative", "Der erwählte Knecht", None,
  "Jesus merkt es und zieht sich zurück; viele folgen ihm, und er heilt sie alle, gebietet ihnen aber streng, ihn nicht bekannt zu machen. Der Evangelist sieht darin erfüllt, was Jesaja gesagt hat ([[ISA.42.1-ISA.42.4]]): Im Zitat heisst der Knecht erwählt und geliebt; der Sprecher wird seinen Geist auf ihn legen, und er wird den Völkern das Recht verkünden. Er wird nicht streiten noch schreien, das geknickte Rohr nicht zerbrechen und den glimmenden Docht nicht auslöschen, bis er das Recht zum Sieg geführt hat, und auf seinen Namen werden Völker hoffen.", None),
 ("TU-MAT-012-022-032", "MAT.12.22-MAT.12.32", "dialogue", "Beelzebul und die Lästerung gegen den Geist", None,
  "Jesus heilt einen Besessenen, der blind und stumm ist, sodass er redet und sieht. Die Menschenmengen geraten ausser sich und fragen, ob das vielleicht der Sohn Davids sei. Die Pharisäer sagen, er treibe die Dämonen nur durch Beelzebul, den Herrscher der Dämonen, aus. Jesus kennt ihre Gedanken: Ein gegen sich selbst gespaltenes Reich wird verwüstet; treibt der Satan den Satan aus, kann sein Reich nicht bestehen; und durch wen treiben ihre Söhne aus? Treibt er die Dämonen durch den Geist Gottes aus, ist das Reich Gottes zu ihnen gekommen; niemand kann das Haus des Starken plündern, ohne ihn zuerst zu binden. Wer nicht mit ihm ist, ist gegen ihn. Jede Sünde und Lästerung, auch ein Wort gegen den Menschensohn, wird vergeben werden, die Lästerung gegen den heiligen Geist aber nicht, weder in dieser Weltzeit noch in der kommenden.", None),
 ("TU-MAT-012-033-037", "MAT.12.33-MAT.12.37", "discourse", "Baum und Frucht, Herz und Wort", None,
  "Jesus fährt fort, man solle Baum und Frucht entweder beide gut oder beide faul machen, denn an der Frucht wird der Baum erkannt. Er nennt die Angesprochenen eine Vipernbrut und fragt, wie sie Gutes reden könnten, da sie böse seien; denn aus dem Überfluss des Herzens redet der Mund, und der gute Mensch bringt aus dem guten Schatz Gutes hervor, der böse Böses. Über jedes unnütze Wort werden die Menschen am Tag des Gerichts Rechenschaft ablegen; aufgrund seiner Worte wird man gerecht gesprochen oder verurteilt werden.", None),
 ("TU-MAT-012-038-045", "MAT.12.38-MAT.12.45", "dialogue", "Das Zeichen des Jona", None,
  "Einige Schriftgelehrte und Pharisäer wollen von Jesus ein Zeichen sehen. Er antwortet, diesem bösen und ehebrecherischen Geschlecht werde kein Zeichen gegeben werden ausser dem Zeichen des Propheten Jona: Wie Jona drei Tage und drei Nächte im Bauch des grossen Fisches war, so werde der Menschensohn drei Tage und drei Nächte im Herzen der Erde sein. Die Männer von Ninive, die auf die Verkündigung des Jona hin umkehrten, und die Königin des Südens, die kam, um die Weisheit Salomos zu hören, werden beim Gericht dieses Geschlecht verurteilen; hier ist mehr als Jona und mehr als Salomo. Dann spricht er von einem unreinen Geist, der von einem Menschen ausgeht, keine Ruhe findet, sein früheres Haus leer, gefegt und geschmückt antrifft und mit sieben noch böseren Geistern dort wohnt, sodass es um den Menschen am Ende schlimmer steht als am Anfang; so werde es auch diesem bösen Geschlecht ergehen.", None),
 ("TU-MAT-012-046-050", "MAT.12.46-MAT.12.50", "narrative", "Mutter und Brüder Jesu", None,
  "Während Jesus noch zu den Menschenmengen redet, stehen seine Mutter und seine Brüder draussen und suchen ihn zu sprechen; jemand sagt es ihm. Jesus fragt, wer seine Mutter und wer seine Brüder seien, streckt die Hand über seine Jünger aus und sagt: «Siehe, meine Mutter und meine Brüder!» Denn wer den Willen seines Vaters in den Himmeln tut, ist sein Bruder, seine Schwester und seine Mutter.", None),
]
UNITS_GSW = {
 "TU-MAT-012-001-050": ("Striit um de Sabbat, de Beelzebul und s Zeiche vom Jona",
  "Wo sini Jünger am Sabbat Ähre abrupfed, säged d Pharisäer zum Jesus, si machid, was am Sabbat nöd erlaubt sig; de Jesus verwiist uf de David und d Prieschter, seit, da sig öppis Grössers als de Tämpel, und nännt de Mänschesohn Herr über de Sabbat. I de Synagoge heilt er am Sabbat e verdorreti Hand, und d Pharisäer haltet Raat, wie si en chönted umbringe. De Jesus zieht sich zrugg, heilt alli, wo ihm nachegönd, und befiehlt ine streng, en nöd bekannt z mache; de Evangelischt gseht drin s Wort vom Jesaja vom userwählte Chnächt erfüllt. Wo de Jesus en blinde und stumme Bsässne heilt, säged d Pharisäer, er tribi d Dämone dur de Beelzebul us; de Jesus antwortet, es gspaltes Riich chönn nöd bestaa, wänn er dur de Geischt vo Gott ustribi, sig s Riich vo Gott zu ine choo, und d Läschterig gäge de Geischt wärdi nöd vergää. A de Frucht erchänn me de Baum; us em Überfluss vom Härz redi de Mund, und uf Grund vo sine Wort wärdi me grächt gsproche oder verurteilt. De Schriftgelehrte und Pharisäer, wo es Zeiche verlanged, seit er, dere Generation wärdi kei Zeiche gää usser s Zeiche vom Jona, und wändet s Bildwort vom unreine Geischt, wo zruggchunnt, uf die Generation aa. Wo sini Mueter und sini Brüeder mit ihm wänd rede, nännt er jede, wo de Wile vo sim Vatter i de Himel tuet, sin Brueder, sini Schwöschter und sini Mueter."),
 "TU-MAT-012-001-008": ("Ährerupfe am Sabbat",
  "I dere Ziit gaat de Jesus am Sabbat dur d Chornfälder; sini Jünger händ Hunger, rupfed Ähre ab und ässed. D Pharisäer säged zum Jesus, sini Jünger machid, was am Sabbat nöd erlaubt sig. De Jesus erinneret a de David, wo mit sine Begleiter im Huus vo Gott d Schaubrot gässe hät, wo nu de Prieschter erlaubt gsii sind, und a d Prieschter, wo am Sabbat im Tämpel de Sabbat entheiliged und glich ohni Schuld sind. Da sig öppis Grössers als de Tämpel; wänn si begriffe hetted, was «Barmhärzigkeit wott ich und nöd Opfer» ([[HOS.6.6]]) heisst, hetted si di Schuldlose nöd verurteilt. Dänn de Mänschesohn isch Herr über de Sabbat."),
 "TU-MAT-012-009-014": ("D Heilig vo de verdorrete Hand",
  "I irer Synagoge isch en Mänsch mit ere verdorrete Hand. De Jesus wird gfröget, öb s erlaubt sig, am Sabbat z heile, damit me en chönn aachlage. Er fröget zrugg, wer vo ine es Schaf, wo am Sabbat in e Gruebe gheit, nöd würd usezie; en Mänsch sig vil meh wärt als es Schaf, also sig s erlaubt, am Sabbat Guets z tue. Er seit zum Mänsch, er söll d Hand usstrecke; dä streckt si us, und si wird gsund wie di ander. D Pharisäer gönd use und haltet Raat, wie si en chönted umbringe."),
 "TU-MAT-012-015-021": ("De userwählt Chnächt",
  "De Jesus merkt s und zieht sich zrugg; vili gönd ihm nache, und er heilt si alli, befiehlt ine aber streng, en nöd bekannt z mache. De Evangelischt gseht drin erfüllt, was de Jesaja gseit hät ([[ISA.42.1-ISA.42.4]]): Im Zitat heisst de Chnächt userwählt und gliebt; dä, wo redt, wird sin Geischt uf ihn lege, und er wird de Völker s Rächt verchünde. Er wird nöd strite und nöd schreie, s gchnickt Rohr nöd verbreche und de glimmend Docht nöd uslösche, bis er s Rächt zum Sieg gfüert hät, und uf sin Name wärded Völker hoffe."),
 "TU-MAT-012-022-032": ("De Beelzebul und d Läschterig gäge de Geischt",
  "De Jesus heilt en Bsässne, wo blind und stumm isch, so dass er redt und gseht. D Lüüt sind usser sich und fröged, öb das ächt de Sohn vom David sig. D Pharisäer säged, er tribi d Dämone nu dur de Beelzebul, de Herrscher vo de Dämone, us. De Jesus kännt iri Gedanke: Es Riich, wo gäge sich sälber gspalte isch, wird verwüeschtet; wänn de Satan de Satan ustribt, cha sis Riich nöd bestaa; und dur wän triibed iri Söhn us? Wänn er d Dämone dur de Geischt vo Gott ustribt, isch s Riich vo Gott zu ine choo; niemer cha s Huus vom Starche plündere, ohni en zerscht z binde. Wer nöd mit ihm isch, isch gäge ihn. Jedi Sünd und Läschterig, au es Wort gäge de Mänschesohn, wird vergää, d Läschterig gäge de heilig Geischt aber nöd, wäder i dere Wältziit no i de chomende."),
 "TU-MAT-012-033-037": ("Baum und Frucht, Härz und Wort",
  "De Jesus redt wiiter, me söll Baum und Frucht entwäder beid guet oder beid fuul mache, dänn a de Frucht erchännt me de Baum. Er nännt die, wo zueloosed, e Viperebruet und fröget, wie si Guets chönted rede, wo si doch bös sigid; dänn us em Überfluss vom Härz redt de Mund, und de guet Mänsch holt us em guete Schatz Guets füre, de bös Bös. Über jedes unnütze Wort wärded d Mänsche am Tag vom Gricht Rächeschaft ablege; uf Grund vo sine Wort wird me grächt gsproche oder verurteilt."),
 "TU-MAT-012-038-045": ("S Zeiche vom Jona",
  "Es paar Schriftgelehrti und Pharisäer wänd vom Jesus es Zeiche gseh. Er antwortet, dere böse und ehebrecherische Generation wärdi kei Zeiche gää usser s Zeiche vom Prophet Jona: Wie de Jona drüü Täg und drüü Nächt im Buuch vom grosse Fisch gsii isch, eso wärdi de Mänschesohn drüü Täg und drüü Nächt im Härz vo de Ärde sii. D Manne vo Ninive, wo uf d Verchündigung vom Jona hii umgchehrt sind, und d Königin vom Süde, wo choo isch, zum d Wiisheit vom Salomo ghöre, wärded im Gricht die Generation verurteile; da isch meh als de Jona und meh als de Salomo. Dänn redt er vo eme unreine Geischt, wo vo eme Mänsch usegaat, kei Rue findt, sis früener Huus leer, gwüscht und gschmückt aatrifft und mit sibe no bösere Geischter dört wohnt, so dass es am Schluss mit däm Mänsch schlimmer isch als am Aafang; eso wärds au dere böse Generation gaa."),
 "TU-MAT-012-046-050": ("D Mueter und d Brüeder vom Jesus",
  "Wo de Jesus no zu de Lüüt redt, stönd sini Mueter und sini Brüeder dusse und wänd mit ihm rede; öpper seit s ihm. De Jesus fröget, wer sini Mueter und wer sini Brüeder sigid, streckt d Hand gäge sini Jünger us und seit: «Lueg, mini Mueter und mini Brüeder!» Dänn wer de Wile vo sim Vatter i de Himel tuet, isch sin Brueder, sini Schwöschter und sini Mueter."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1, "
  "WREAD-CNTR-MAT-012-001-050) bzw. auf dem dort erfassten Wortlaut der CNTR-Transkriptionen (Sekundärtranskription, nicht "
  "am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. Widerspricht die Zuordnung den Sigla des "
  "SBLGNT-Apparats (in Kapitel 12 bei RP in [[MAT.12.32]], bei WH in [[MAT.12.31]]), gilt der Apparat; die Unsicherheit ist "
  "bei der Alternative genannt. Zahlen zu Wortvorkommen sind per Skript aus den SBLGNT-Tokens gezählt."),
 ("Einheitliche Begriffe für alle Matthäus-Bereiche, in Kapitel 12 verwendet: ἰδού «siehe»; τότε «da/dann»; ὁ υἱὸς τοῦ "
  "ἀνθρώπου «der Menschensohn»; ἡ βασιλεία τοῦ θεοῦ «das Reich Gottes» ([[MAT.12.28]], sonst bei Matthäus meist «Reich der "
  "Himmel»); ὁ πατήρ μου ὁ ἐν οὐρανοῖς «mein Vater in den Himmeln»; Erfüllungsformel «damit erfüllt würde, was … gesagt "
  "ist»; γραμματεῖς «Schriftgelehrte»; Φαρισαῖοι «Pharisäer»; δαιμόνιον «Dämon», δαιμονιζόμενος «Besessener»; πνεῦμα "
  "ἅγιον «heiliger Geist»; μετανοέω «umkehren»."),
 ("Weitere Wiedergaben in Kapitel 12: γενεά «Geschlecht» (wie in der Markus-Übersetzung; Mundart «Generation»); "
  "ὄχλος «die Menge», ὄχλοι (Plural) «die Menschenmengen»; σημεῖον «Zeichen»; κρίσις «Gericht», im Jesajazitat [[MAT.12.18]] und [[MAT.12.20]] «Recht»; "
  "ἔθνη «Völker»; παῖς (Gottesknecht) «Knecht»; βλασφημία «Lästerung»; αἰών «Weltzeit»; γεννήματα ἐχιδνῶν «Vipernbrut» "
  "(auch [[MAT.3.7]], [[MAT.23.33]]); σαπρός «faul»; δικαιόω «gerecht sprechen»; ἀδελφοί «Brüder»."),
 ("Parallelen: [[MRK.2.23-MRK.3.12]], [[MRK.3.22-MRK.3.35]], [[MRK.8.11-MRK.8.12]]. Wo Matthäus dieselbe griechische "
  "Wendung hat, ist sie möglichst gleich übersetzt wie bei Markus (z. B. «hielten Rat gegen ihn», «plündern», «gegen sich "
  "selbst gespalten»); wo er anders formuliert (Hunger der Jünger, Beispiel der Priester, Bildwort vom Schaf, «Reich "
  "Gottes», «Vater in den Himmeln»), folgt die Übersetzung seinem Wortlaut."),
 ("Erzählweise und Redegrenzen: Das erzählende Präsens (λέγει «sagt», [[MAT.12.13]], [[MAT.12.44]]) ist beibehalten. ὅτι vor "
  "direkter Rede und λέγων/λέγοντες «sagend» sind nicht eigens übersetzt. Anführungszeichen sind eine Entscheidung der "
  "Übersetzung; Zitate in einer Rede ([[MAT.12.7]], [[MAT.12.44]]) stehen in einfachen Anführungszeichen. Das Jesajazitat "
  "[[MAT.12.18-MAT.12.21]] steht in Anführungszeichen, weil die Erfüllungsformel es ausdrücklich einleitet."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT mit WH gegen Treg, RP und NA28 liest ([[MAT.12.15]] "
  "ohne ὄχλοι). Abweichende Lesarten stehen als Alternativen, soweit sie die Übersetzung verändern; reine "
  "Wortstellungsvarianten und Formvarianten ohne Wirkung auf die Übersetzung ([[MAT.12.10]] θεραπεῦσαι, [[MAT.12.13]], "
  "[[MAT.12.14]], [[MAT.12.17]], [[MAT.12.18]], [[MAT.12.27]], [[MAT.12.29]] διαρπάσῃ, [[MAT.12.44]] Wortstellung und καί, "
  "[[MAT.12.46]] δέ, [[MAT.12.48]] εἰπόντι) sind nur in follows_readings geführt; ebenso [[MAT.12.11]] (Treg ohne ἔσται), "
  "weil «wäre» davon nicht berührt wird."),
 ("In Kapitel 12 fehlt im SBLGNT kein Vers. [[MAT.12.47]] steht im SBLGNT-Text (mit Treg, NA28 und RP); WH lässt ihn aus. "
  "Das steht als Alternative."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig. Eigeti Formulierig; nöd us ere veröffentlichte Mundart-Bible übernoo.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte. Wo d Zueornig em Apparat widerspricht, gilt de Apparat."),
 ("Iiheitlichi Begriff für alli Matthäus-Teil: ἰδού «lueg»; τότε «dänn»; «de Mänschesohn»; «s Riich vo Gott» (da, susch "
  "meischtens «s Riich vo de Himel»); «min Vatter i de Himel»; Erfüllungsformle «damit erfüllt wird, was … gseit worden "
  "isch»; «Schriftgelehrti», «Pharisäer»; «Dämon», «Bsässne»; «heilige Geischt»; μετανοέω «umchehre»."),
 ("Wiiteri Widergaabe i Kapitel 12: γενεά «Generation» (wie bim Markus); ὄχλος «d Mängi», ὄχλοι «d Lüüt»; σημεῖον «Zeiche»; κρίσις «Gricht», "
  "im Jesajazitat «Rächt»; ἔθνη «Völker»; παῖς «Chnächt»; βλασφημία «Läschterig»; αἰών «Wältziit»; γεννήματα ἐχιδνῶν "
  "«Viperebruet»; σαπρός «fuul»; δικαιόω «grächt spräche»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de David»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«s Huus vo Gott»); Futur oft mit «wird/wärded», wo s griechisch Futur betont isch."),
 ("Text: D Übersetzig folgt de SBLGNT-Token. I Kapitel 12 fehlt kei Vers; [[MAT.12.47]] staat im SBLGNT, WH laat en wäg "
  "(lueg Alternative)."),
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Huus, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Artikel vor Personennamen. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; einheitliche Begriffe für das ganze Matthäusevangelium (translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_12_12.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 12 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
