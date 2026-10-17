#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 20–21 (Arbeiter im Weinberg, dritte Leidensankündigung, Bitte der Zebedäusmutter, zwei Blinde
bei Jericho, Einzug in Jerusalem, Tempel, Feigenbaum, Vollmachtsfrage, zwei Söhne, Weinbauern) – Texteinheiten,
Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen, Lesarten-Alternativen und
vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_20_21.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 20–21 fehlt im SBLGNT kein Vers (per Skript geprüft); alle Verse haben Tokens.
- [[MAT.21.44]] steht im SBLGNT (mit Variantenzeichen); der Apparat verzeichnet die Auslassung (WH am Rand). Die
  Übersetzung folgt dem SBLGNT; die Auslassung steht als Alternative.
- [[MAT.21.29]]–[[MAT.21.31]]: Reihenfolge der beiden Söhne und Antwort «der erste» nach dem SBLGNT; die vertauschte
  Fassung (WH) steht in drei zusammengehörigen Alternativen.

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
CHAPTERS = ((20, 34), (21, 46))

DE = {
 # ------------------------------------------------------------ Kapitel 20
 "MAT.20.1": "«[Denn]{2} [das Reich]{4,5} [der Himmel]{6,7} [ist]{3} [gleich]{1} [einem Hausherrn]{8,9}, [der]{10} [frühmorgens]{12,13} [hinausging]{11}, [um]{14} [Arbeiter]{15} [für]{16} [seinen]{17,19} [Weinberg]{18} [anzuwerben]{14}.",
 "MAT.20.2": "[Nachdem er sich]{1} [aber]{2} [mit]{3} [den Arbeitern]{4,5} [auf]{6} [einen Denar]{7} [für den]{8} [Tag]{9} [geeinigt hatte]{1}, [schickte er]{10} [sie]{11} [in]{12} [seinen]{13,15} [Weinberg]{14}.",
 "MAT.20.3": "Und{1} [als er]{2} [um]{3} [die dritte]{4} [Stunde]{5} [hinausging]{2}, [sah er]{6} [andere]{7} [untätig]{12} [auf]{9} [dem]{10} [Markt]{11} [stehen]{8}.",
 "MAT.20.4": "Und{1} [zu jenen]{2} [sagte er]{3}: ‹[Geht]{4} [auch]{5} [ihr]{6} [in]{7} [den]{8} [Weinberg]{9}, und{10} [was]{11,12} [recht]{14} [ist]{13}, [werde ich]{15} [euch]{16} [geben]{15}.›",
 "MAT.20.5": "[Sie]{1} [aber]{2} [gingen hin]{3}. [Wieder]{4} [ging er hinaus]{5}, [um]{6} [die sechste]{7} und{8} [die neunte]{9} [Stunde]{10}, und [machte es]{11} [ebenso]{12}.",
 "MAT.20.6": "[Als er]{5} [aber]{2} [um]{1} [die elfte]{3,4} Stunde [hinausging]{5}, [fand er]{6} [andere]{7}, [die dastanden]{8}, und{9} [sagt]{10} [zu ihnen]{11}: ‹[Warum]{12} [steht ihr]{14} [den ganzen]{15,16} [Tag]{17} [untätig]{18} [hier]{13}?›",
 "MAT.20.7": "[Sie sagen]{1} [zu ihm]{2}: ‹[Weil]{3} [niemand]{4} [uns]{5} [angeworben hat]{6}.› [Er sagt]{7} [zu ihnen]{8}: ‹[Geht]{9} [auch]{10} [ihr]{11} [in]{12} [den]{13} [Weinberg]{14}!›",
 "MAT.20.8": "[Als es]{3} [aber]{2} [Abend]{1} [geworden war]{3}, [sagt]{4} [der Herr]{5,6} [des Weinbergs]{7,8} [zu seinem]{9,11} [Verwalter]{10}: ‹[Ruf]{12} [die Arbeiter]{13,14} und{15} [zahl]{16} [ihnen]{17} [den Lohn]{18,19} [aus]{16}, [angefangen]{20} [bei]{21} [den Letzten]{22,23} [bis]{24} [zu den Ersten]{25,26}!›",
 "MAT.20.9": "Und{1} [die]{3} [von]{4} [der elften]{5,6} [Stunde]{7} [kamen]{2} und [erhielten]{8} [je]{9} [einen Denar]{10}.",
 "MAT.20.10": "Und{1} [als]{2} [die Ersten]{3,4} [kamen]{2}, [meinten sie]{5}, [dass]{6} [sie]{8} [mehr]{7} [erhalten würden]{8}; und{9} [auch]{14} [sie]{15} [erhielten]{10} [je]{11,12} [einen Denar]{13}.",
 "MAT.20.11": "[Als sie ihn]{1} [aber]{2} [erhalten hatten]{1}, [murrten sie]{3} [gegen]{4} [den Hausherrn]{5,6}",
 "MAT.20.12": "und [sagten]{1}: ‹[Diese]{2} [Letzten]{3,4} [haben]{7} [eine]{5} [Stunde]{6} [gearbeitet]{7}, und{8} [du hast]{12} [sie]{10} [uns]{11} [gleichgestellt]{9}, [die wir]{13} [die Last]{15,16} [des Tages]{17,18} und{19} [die Hitze]{20,21} [getragen haben]{14}.›",
 "MAT.20.13": "[Er]{1} [aber]{2} [antwortete]{3} [einem]{4} [von ihnen]{5} und [sagte]{6}: ‹[Freund]{7}, [ich tue]{9} [dir]{10} [kein]{8} [Unrecht]{9}. [Hast du dich]{13} [nicht]{11} [mit mir]{14} [auf einen Denar]{12} [geeinigt]{13}?",
 "MAT.20.14": "[Nimm]{1} [das Deine]{2,3} und{4} [geh]{5}! [Ich will]{6} [aber]{7} [diesem]{8} [Letzten]{9,10} [geben]{11} [wie]{12} [auch]{13} [dir]{14}.",
 "MAT.20.15": "[Ist es]{2} [mir]{3} [nicht]{1} [erlaubt]{2}, [mit dem]{7,8} [Meinen]{9} [zu tun]{6}, [was]{4} [ich will]{5}? [Oder]{10} [ist]{15} [dein]{13} [Auge]{11,12} [böse]{14}, [weil]{16} [ich]{17} [gütig]{18} [bin]{19}?›",
 "MAT.20.16": "[So]{1} [werden]{2} [die Letzten]{3,4} [Erste]{5} [sein]{2} und{6} [die Ersten]{7,8} [Letzte]{9}.»",
 "MAT.20.17": "Und{1} [als]{2} [Jesus]{3,4} [nach]{5} [Jerusalem]{6} [hinaufzog]{2}, [nahm er]{7} [die]{8} [zwölf]{9} [Jünger]{10} [beiseite]{11,12} und{13} [sagte]{17} [auf]{14} [dem]{15} [Weg]{16} [zu ihnen]{18}:",
 "MAT.20.18": "«[Siehe]{1}, [wir ziehen]{2} [nach]{3} [Jerusalem]{4} [hinauf]{2}, und{5} [der Menschensohn]{6-9} [wird]{10} [den Hohepriestern]{11,12} und{13} [Schriftgelehrten]{14} [ausgeliefert werden]{10}, und{15} [sie werden]{16} [ihn]{17} [zum Tod]{18} [verurteilen]{16}",
 "MAT.20.19": "und{1} [sie werden]{2} [ihn]{3} [den Heiden]{4,5} [ausliefern]{2}, [damit sie ihn]{6,7} [verspotten]{8} und{9} [auspeitschen]{10} und{11} [kreuzigen]{12}; und{13} [am dritten]{14,15} [Tag]{16} [wird er auferweckt werden]{17}.»",
 "MAT.20.20": "[Da]{1} [trat]{2} [die Mutter]{4,5} [der Söhne]{6,7} [des Zebedäus]{8} [mit]{9} [ihren]{10,12} [Söhnen]{11} [an ihn]{3} [heran]{2}, [warf sich vor ihm nieder]{13} und{14} [bat]{15} [ihn]{17,18} [um etwas]{16}.",
 "MAT.20.21": "[Er]{1} [aber]{2} [sagte]{3} [zu ihr]{4}: «[Was]{5} [willst du]{6}?» [Sie sagt]{7} [zu ihm]{8}: «[Sag]{9}, [dass]{10} [diese]{12,13} [meine]{16} [zwei]{14} [Söhne]{15} [in]{26} [deinem]{27,29} [Reich]{28} [sitzen]{11} [dürfen]{10}, [einer]{17} [zu]{18} [deiner]{20} [Rechten]{19} und{21} [einer]{22} [zu]{23} [deiner]{25} [Linken]{24}!»",
 "MAT.20.22": "[Jesus]{3,4} [aber]{2} [antwortete]{1} und [sagte]{5}: «[Ihr wisst]{7} [nicht]{6}, [was]{8} [ihr bittet]{9}. [Könnt ihr]{10} [den Becher]{12,13} [trinken]{11}, [den]{14} [ich]{15} [trinken]{17} [werde]{16}?» [Sie sagen]{18} [zu ihm]{19}: «[Wir können es]{20}.»",
 "MAT.20.23": "[Er sagt]{1} [zu ihnen]{2}: «[Meinen]{6} [Becher]{3,5} [werdet ihr]{7} [zwar]{4} [trinken]{7}; [das Sitzen]{8,10} [aber]{9} [zu]{11} [meiner]{13} [Rechten]{12} und{14} [zur]{15} [Linken]{16} [zu vergeben]{20}, [steht]{18} [nicht]{17} [mir]{19} [zu]{18}, [sondern]{21} es gehört [denen, für die]{22} es [von]{24} [meinem]{25,27} [Vater]{26} [bereitet ist]{23}.»",
 "MAT.20.24": "Und{1} [als]{2} [die Zehn]{3,4} [das hörten]{2}, [empörten sie sich]{5} [über]{6} [die]{7} [zwei]{8} [Brüder]{9}.",
 "MAT.20.25": "[Jesus]{1,3} [aber]{2} [rief]{4} [sie]{5} [zu sich]{4} und [sagte]{6}: «[Ihr wisst]{7}, [dass]{8} [die Herrscher]{9,10} [der Völker]{11,12} [sie]{14} [unterdrücken]{13} und{15} [die Grossen]{16,17} [Gewalt über sie ausüben]{18,19}.",
 "MAT.20.26": "[So]{2} [soll es]{3} [nicht]{1} [sein]{3} [unter]{4} [euch]{5}; [sondern]{6} [wer]{7,8} [unter]{10} [euch]{11} [gross]{12} [werden]{13} [will]{9}, [der soll]{14} [euer]{15} [Diener]{16} [sein]{14},",
 "MAT.20.27": "und{1} [wer]{2,3} [unter]{5} [euch]{6} [der Erste]{8} [sein]{7} [will]{4}, [der soll]{9} [euer]{10} [Sklave]{11} [sein]{9},",
 "MAT.20.28": "[so wie]{1} [der Menschensohn]{2-5} [nicht]{6} [gekommen ist]{7}, [um sich dienen zu lassen]{8}, [sondern]{9} [um zu dienen]{10} und{11} [sein]{13,15} [Leben]{14} [zu geben]{12} [als Lösegeld]{16} [für]{17} [viele]{18}.»",
 "MAT.20.29": "Und{1} [als]{2} [sie]{3} [aus]{4} [Jericho]{5} [hinauszogen]{2}, [folgte]{6} [ihm]{7} [eine grosse]{9} [Menge]{8}.",
 "MAT.20.30": "Und{1} [siehe]{2}, [zwei]{3} [Blinde]{4} [sassen]{5} [am]{6,7} [Weg]{8}; [als sie hörten]{9}, [dass]{10} [Jesus]{11} [vorbeigeht]{12}, [schrien sie]{13}: «[Herr]{15}, [hab Erbarmen]{16} [mit uns]{17}, [Sohn]{18} [Davids]{19}!» ~14(λέγοντες «sagend» leitet die direkte Rede ein)",
 "MAT.20.31": "[Die Menge]{1,3} [aber]{2} [fuhr]{4} [sie]{5} [an]{4}, [sie sollten]{6} [schweigen]{7}; [sie]{8} [aber]{9} [schrien]{11} [noch lauter]{10}: «[Herr]{13}, [hab Erbarmen]{14} [mit uns]{15}, [Sohn]{16} [Davids]{17}!» ~12(λέγοντες «sagend» leitet die direkte Rede ein)",
 "MAT.20.32": "Und{1} [Jesus]{3,4} [blieb stehen]{2}, [rief]{5} [sie]{6} und{7} [sagte]{8}: «[Was]{9} [wollt ihr]{10}, [dass ich]{11} [euch]{12} [tue]{11}?»",
 "MAT.20.33": "[Sie sagen]{1} [zu ihm]{2}: «[Herr]{3}, [dass]{4} [unsere]{8} [Augen]{6,7} [geöffnet werden]{5}!»",
 "MAT.20.34": "[Jesus]{3,4} [aber]{2} [hatte Erbarmen]{1} und [berührte]{5} [ihre]{8} [Augen]{6,7}, und{9} [sogleich]{10} [sahen sie wieder]{11}, und{12} [sie folgten]{13} [ihm]{14} [nach]{13}.",
 # ------------------------------------------------------------ Kapitel 21
 "MAT.21.1": "Und{1} [als]{2} [sie sich]{3} [Jerusalem]{4,5} [näherten]{3} und{6} [nach]{8} [Betfage]{9} [kamen]{7}, [an]{10} [den Ölberg]{11-14}, [da]{15} [sandte]{17} [Jesus]{16} [zwei]{18} [Jünger]{19} [aus]{17}",
 "MAT.21.2": "und [sagte]{1} [zu ihnen]{2}: «[Geht]{3} [in]{4} [das]{5} [Dorf]{6}, [das]{7} [vor]{8} [euch]{9} [liegt]{8}, und{10} [sogleich]{11} [werdet ihr]{12} [eine Eselin]{13} [angebunden]{14} [finden]{12} und{15} [ein Fohlen]{16} [bei]{17} [ihr]{18}. [Bindet sie los]{19} und [bringt sie]{20} [zu mir]{21}!",
 "MAT.21.3": "Und{1} [wenn]{2} [jemand]{3} [euch]{4} [etwas]{6} [sagt]{5}, [dann sagt]{7}: ‹[Der Herr]{9,10} [braucht]{12,13} [sie]{11}.› [Er wird]{16} [sie]{17} [aber]{15} [sogleich]{14} [schicken]{16}.» ~8(ὅτι leitet die direkte Rede ein)",
 "MAT.21.4": "[Das]{1} [aber]{2} [ist geschehen]{3}, [damit]{4} [erfüllt würde]{5}, [was]{6} [durch]{8} [den Propheten]{9,10} [gesagt ist]{7}: ~11(λέγοντος «der sagt» leitet das Zitat ein)",
 "MAT.21.5": "«[Sagt]{1} [der Tochter]{2,3} [Zion]{4}: [Siehe]{5}, [dein]{8} [König]{6,7} [kommt]{9} [zu dir]{10}, [sanftmütig]{11} und{12} [reitend]{13} [auf]{14} [einer Eselin]{15} und{16} [auf]{17} [einem Fohlen]{18}, [dem Jungen]{19} [eines Lasttiers]{20}.»",
 "MAT.21.6": "[Die Jünger]{3,4} [aber]{2} [gingen hin]{1} und{5} [taten]{6}, [wie]{7} [Jesus]{10,11} [es ihnen]{9} [aufgetragen hatte]{8}.",
 "MAT.21.7": "[Sie brachten]{1} [die Eselin]{2,3} und{4} [das Fohlen]{5,6} und{7} [legten]{8} [die Mäntel]{11,12} [auf]{9} [sie]{10}, und{13} [er setzte sich]{14} [darauf]{15,16}.",
 "MAT.21.8": "[Die meisten]{1,3} [aus der Menge]{4} [aber]{2} [breiteten]{5} [ihre]{6} [Mäntel]{7,8} [auf]{9} [dem]{10} [Weg]{11} [aus]{5}; [andere]{12} [aber]{13} [schnitten]{14} [Zweige]{15} [von]{16} [den Bäumen]{17,18} und{19} [breiteten sie]{20} [auf]{21} [dem]{22} [Weg]{23} [aus]{20}.",
 "MAT.21.9": "[Die Menschenmengen]{1,3} [aber]{2}, [die]{4} [ihm]{6} [vorausgingen]{5} und{7} [die]{8} ihm [nachfolgten]{9}, [riefen]{10}: «[Hosanna]{12} [dem Sohn]{13,14} [Davids]{15}! [Gesegnet]{16} sei, [der]{17} [kommt]{18} [im]{19} [Namen]{20} [des Herrn]{21}! [Hosanna]{22} [in]{23} [den Höhen]{24,25}!» ~11(λέγοντες «sagend» leitet die direkte Rede ein)",
 "MAT.21.10": "Und{1} [als]{2} [er]{3} [in]{4} [Jerusalem]{5} [einzog]{2}, [geriet]{6} [die ganze]{7,8} [Stadt]{9} [in Aufruhr]{6} und [sagte]{10}: «[Wer]{11} [ist]{12} [dieser]{13}?»",
 "MAT.21.11": "[Die Menschenmengen]{1,3} [aber]{2} [sagten]{4}: «[Das]{5} [ist]{6} [der Prophet]{7,8} [Jesus]{9} [aus]{10,11} [Nazaret]{12} [in Galiläa]{13,14}.»",
 "MAT.21.12": "Und{1} [Jesus]{3} [ging]{2} [in]{4} [den]{5} [Tempel]{6} [hinein]{2} und{7} [trieb]{8} [alle]{9} [hinaus]{8}, [die]{10} [im]{14,15} [Tempel]{16} [verkauften]{11} und{12} [kauften]{13}; und{17} [die Tische]{18,19} [der Geldwechsler]{20,21} und{23} [die Sitze]{24,25} [der Taubenverkäufer]{26-29} [stiess er um]{22},",
 "MAT.21.13": "und{1} [sagt]{2} [zu ihnen]{3}: «[Es steht geschrieben]{4}: ‹[Mein]{7} [Haus]{5,6} [soll]{10} [ein Haus]{8} [des Gebets]{9} [heissen]{10}.› [Ihr]{11} [aber]{12} [macht]{14} [es]{13} [zu einer Räuberhöhle]{15,16}.»",
 "MAT.21.14": "Und{1} [es traten]{2} [Blinde]{4} und{5} [Lahme]{6} [im]{7,8} [Tempel]{9} [an ihn]{3} [heran]{2}, und{10} [er heilte]{11} [sie]{12}.",
 "MAT.21.15": "[Als]{1} [aber]{2} [die Hohepriester]{3,4} und{5} [die Schriftgelehrten]{6,7} [die erstaunlichen Dinge]{8,9} [sahen]{1}, [die]{10} [er getan hatte]{11}, und{12} [die Kinder]{13,14}, [die]{15} [im]{17,18} [Tempel]{19} [riefen]{16} und{20} [sagten]{21}: «[Hosanna]{22} [dem Sohn]{23,24} [Davids]{25}!», [empörten sie sich]{26}.",
 "MAT.21.16": "Und{1} [sie sagten]{2} [zu ihm]{3}: «[Hörst du]{4}, [was]{5} [diese]{6} [sagen]{7}?» [Jesus]{8,10} [aber]{9} [sagt]{11} [zu ihnen]{12}: «[Ja]{13}. [Habt ihr]{15} [nie]{14} [gelesen]{15}: ‹[Aus]{17} [dem Mund]{18} [von kleinen Kindern]{19} und{20} [Säuglingen]{21} [hast du dir]{22} [Lob]{23} [bereitet]{22}›?» ~16(ὅτι leitet das Zitat ein)",
 "MAT.21.17": "Und{1} [er verliess]{2} [sie]{3}, [ging]{4} [aus]{5} [der Stadt]{6,7} [hinaus]{4} [nach]{8} [Betanien]{9} und{10} [übernachtete]{11} [dort]{12}.",
 "MAT.21.18": "[Als er]{3} [aber]{2} [frühmorgens]{1} [in]{4} [die Stadt]{5,6} [zurückkehrte]{3}, [hatte er Hunger]{7}.",
 "MAT.21.19": "Und{1} [als er]{2} [einen]{4} [Feigenbaum]{3} [am]{5,6} [Weg]{7} [sah]{2}, [ging er]{8} [zu]{9} [ihm]{10} [hin]{8} und{11} [fand]{13} [nichts]{12} [an]{14} [ihm]{15} [als]{16,17} [nur]{19} [Blätter]{18}; und{20} [er sagt]{21} [zu ihm]{22}: «[Nie mehr]{23} [in]{28} [Ewigkeit]{29,30} [soll]{27} [aus]{24} [dir]{25} [Frucht]{26} [wachsen]{27}!» Und{31} [der Feigenbaum]{34,35} [verdorrte]{32} [auf der Stelle]{33}.",
 "MAT.21.20": "Und{1} [als]{2} [die Jünger]{3,4} [das sahen]{2}, [staunten sie]{5} und [sagten]{6}: «[Wie]{7} [ist]{9} [der Feigenbaum]{10,11} [auf der Stelle]{8} [verdorrt]{9}?»",
 "MAT.21.21": "[Jesus]{3,4} [aber]{2} [antwortete]{1} und [sagte]{5} [zu ihnen]{6}: «[Amen]{7}, [ich sage]{8} [euch]{9}: [Wenn]{10} [ihr]{11} [Glauben]{12} [habt]{11} und{13} [nicht]{14} [zweifelt]{15}, [werdet ihr]{21} [nicht]{16} [nur]{17} [das mit]{18,19} [dem Feigenbaum]{20} [tun]{21}, [sondern]{22} [auch wenn]{23} [ihr]{27} [zu diesem]{24,26} [Berg]{25} [sagt]{27}: ‹[Heb dich hoch]{28} und{29} [stürz dich]{30} [ins]{31,32} [Meer]{33}!›, [wird es geschehen]{34}.",
 "MAT.21.22": "Und{1} [alles]{2}, [worum]{3,4} [ihr]{5} [im]{6,7} [Gebet]{8} [bittet]{5}, [werdet ihr empfangen]{10}, [wenn ihr glaubt]{9}.»",
 "MAT.21.23": "Und{1} [als]{2} [er]{3} [in]{4} [den]{5} [Tempel]{6} [gegangen war]{2}, [traten]{7} [die Hohepriester]{10,11} und{12} [die Ältesten]{13,14} [des Volkes]{15,16} [an ihn]{8} [heran]{7}, [während er lehrte]{9}, und [sagten]{17}: «[In]{18} [welcher]{19} [Vollmacht]{20} [tust du]{22} [das]{21}? Und{23} [wer]{24} [hat]{26} [dir]{25} [diese]{27,29} [Vollmacht]{28} [gegeben]{26}?»",
 "MAT.21.24": "[Jesus]{3,4} [aber]{2} [antwortete]{1} und [sagte]{5} [zu ihnen]{6}: «[Auch ich]{9} [werde]{7} [euch]{8} [eine]{11} [Frage]{10} [stellen]{7}; [wenn]{13} [ihr]{14} [sie]{12} [mir]{15} [beantwortet]{14}, [werde]{18} [auch ich]{16} [euch]{17} [sagen]{18}, [in]{19} [welcher]{20} [Vollmacht]{21} [ich]{23} [das]{22} [tue]{23}.",
 "MAT.21.25": "[Die Taufe]{1,2} [des Johannes]{3,4} – [woher]{5} [war sie]{6}? [Vom]{7} [Himmel]{8} [oder]{9} [von]{10} [Menschen]{11}?» [Sie]{12} [aber]{13} [überlegten]{14} [untereinander]{15,16} und [sagten]{17}: «[Wenn]{18} [wir sagen]{19}: ‹[Vom]{20} [Himmel]{21}›, [wird er]{22} [zu uns]{23} [sagen]{22}: ‹[Warum]{24,25} [habt ihr]{28} [ihm]{29} [dann]{26} [nicht]{27} [geglaubt]{28}?›",
 "MAT.21.26": "[Wenn]{1} [wir]{3} [aber]{2} [sagen]{3}: ‹[Von]{4} [Menschen]{5}›, [fürchten wir]{6} [die Menge]{7,8}; [denn]{10} [alle]{9} [halten]{13} [Johannes]{14,15} [für]{11} [einen Propheten]{12}.»",
 "MAT.21.27": "Und{1} [sie antworteten]{2} [Jesus]{3,4} und [sagten]{5}: «[Wir wissen es]{7} [nicht]{6}.» [Und]{10} [er]{11} [sagte]{8} [zu ihnen]{9}: «[Auch ich]{13} [sage]{14} [euch]{15} [nicht]{12}, [in]{16} [welcher]{17} [Vollmacht]{18} [ich]{20} [das]{19} [tue]{20}.»",
 "MAT.21.28": "«[Was]{1} [aber]{2} [meint]{4} [ihr]{3}? [Ein Mensch]{5} [hatte]{6} [zwei]{8} [Kinder]{7}. [Er trat]{9} [an den]{10} [ersten]{11} [heran]{9} und [sagte]{12}: ‹[Kind]{13}, [geh]{14}, [arbeite]{16} [heute]{15} [im]{17,18} [Weinberg]{19}!›",
 "MAT.21.29": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: ‹[Ich will]{6} [nicht]{5}.› [Später]{7} [aber]{8} [bereute er es]{9}, und [er ging hin]{10}.",
 "MAT.21.30": "[Er trat]{1} [aber]{2} [an den]{3} [zweiten]{4} [heran]{1} und [sagte]{5} [dasselbe]{6}. [Der]{7} [aber]{8} [antwortete]{9} und [sagte]{10}: ‹[Ich]{11} gehe, [Herr]{12}!› Und{13} [er ging]{15} [nicht]{14} [hin]{15}.",
 "MAT.21.31": "[Wer]{1} [von]{2} [den]{3} [beiden]{4} [hat]{5} [den Willen]{6,7} [des Vaters]{8,9} [getan]{5}?» [Sie sagen]{10}: «[Der erste]{11,12}.» [Jesus]{15,16} [sagt]{13} [zu ihnen]{14}: «[Amen]{17}, [ich sage]{18} [euch]{19}: [Die Zöllner]{21,22} und{23} [die Prostituierten]{24,25} [gehen]{26} [euch]{27} [voran]{26} [in]{28} [das Reich]{29,30} [Gottes]{31,32}. ~20(ὅτι leitet die direkte Rede ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.21.32": "[Denn]{2} [Johannes]{3} [ist]{1} [zu]{4} [euch]{5} [gekommen]{1} [auf]{6} [dem Weg]{7} [der Gerechtigkeit]{8}, und{9} [ihr habt]{11} [ihm]{12} [nicht]{10} [geglaubt]{11}; [die Zöllner]{13,15} [aber]{14} und{16} [die Prostituierten]{17,18} [haben]{19} [ihm]{20} [geglaubt]{19}. [Ihr]{21} [aber]{22} [habt es gesehen]{23} und es [nicht einmal]{24} [danach]{26} [bereut]{25}, [sodass ihr]{27} [ihm]{29} [geglaubt hättet]{28}.",
 "MAT.21.33": "[Hört]{3} [ein anderes]{1} [Gleichnis]{2}: [Es war]{5} [ein Hausherr]{4,6}, [der]{7} [einen Weinberg]{9} [pflanzte]{8}; und{10} [er zog]{13} [einen Zaun]{11} [darum]{12} und{14} [grub]{15} [darin]{16,17} [eine Kelter]{18} und{19} [baute]{20} [einen Turm]{21} und{22} [verpachtete]{23} [ihn]{24} [an Weinbauern]{25} und{26} [reiste ausser Landes]{27}.",
 "MAT.21.34": "[Als]{1} [aber]{2} [die Zeit]{4,5} [der Früchte]{6,7} [nahe kam]{3}, [sandte er]{8} [seine]{9,11} [Knechte]{10} [zu]{12} [den Weinbauern]{13,14}, [um]{15} [seine]{16,18} [Früchte]{17} [abzuholen]{15}.",
 "MAT.21.35": "Und{1} [die Weinbauern]{3,4} [packten]{2} [seine]{5,7} [Knechte]{6}: [den einen]{8,9} [verprügelten sie]{10}, [einen anderen]{11,12} [töteten sie]{13}, [einen anderen]{14,15} [steinigten sie]{16}.",
 "MAT.21.36": "[Wieder]{1} [sandte er]{2} [andere]{3} [Knechte]{4}, [mehr]{5} [als]{6} [die ersten]{7}; und{8} [sie machten es]{9} [mit ihnen]{10} [ebenso]{11}.",
 "MAT.21.37": "[Zuletzt]{1} [aber]{2} [sandte er]{3} [seinen]{6,8} [Sohn]{7} [zu]{4} [ihnen]{5} und [sagte sich]{9}: ‹[Vor meinem]{11,13} [Sohn]{12} [werden sie Achtung haben]{10}.›",
 "MAT.21.38": "[Als]{4} [die Weinbauern]{1,3} [aber]{2} [den Sohn]{5,6} [sahen]{4}, [sagten sie]{7} [untereinander]{8,9}: ‹[Das]{10} [ist]{11} [der Erbe]{12,13}; [kommt]{14}, [lasst uns]{15} [ihn]{16} [töten]{15} und{17} [sein]{19,21} [Erbe]{20} [bekommen]{18}!›",
 "MAT.21.39": "Und{1} [sie packten]{2} [ihn]{3}, [warfen ihn]{4} [aus]{5} [dem Weinberg]{6,7} [hinaus]{4} und{8} [töteten ihn]{9}.",
 "MAT.21.40": "[Wenn]{1} [nun]{2} [der Herr]{4,5} [des Weinbergs]{6,7} [kommt]{3}, [was]{8} [wird er]{9} [mit]{10} [jenen]{12} [Weinbauern]{11} [tun]{9}?»",
 "MAT.21.41": "[Sie sagen]{1} [zu ihm]{2}: «[Er wird]{5} [die Übeltäter]{3,6} [übel]{4} [umbringen]{5}, und{7} [den Weinberg]{8,9} [wird er]{10} [an andere]{11} [Weinbauern]{12} [verpachten]{10}, [die]{13} [ihm]{15} [die Früchte]{16,17} [zu]{18} [ihrer]{19,21} [Zeit]{20} [abgeben werden]{14}.»",
 "MAT.21.42": "[Jesus]{3,4} [sagt]{1} [zu ihnen]{2}: «[Habt ihr]{6} [nie]{5} [in]{7} [den Schriften]{8,9} [gelesen]{6}: ‹[Der Stein]{10}, [den]{11} [die Bauleute]{13,14} [verworfen haben]{12}, [der]{15} [ist]{16} [zum Eckstein]{17-19} [geworden]{16}; [vom]{20} [Herrn]{21} [ist]{22} [das]{23} [geschehen]{22}, und{24} [es ist]{25} [wunderbar]{26} [in]{27} [unseren]{29} [Augen]{28}›?",
 "MAT.21.43": "[Darum]{1,2} [sage ich]{3} [euch]{4}: [Das Reich]{9,10} [Gottes]{11,12} [wird]{6} [von]{7} [euch]{8} [weggenommen]{6} und{13} [einem Volk]{15} [gegeben werden]{14}, [das]{16} [seine]{17,19} [Früchte]{18} [bringt]{16}. ~5(ὅτι leitet die Aussage ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.21.44": "Und{1} [wer]{2} [auf]{4} [diesen]{5,7} [Stein]{6} [fällt]{3}, [wird zerschellen]{8}; [auf wen]{9,10,12} [er]{13} [aber]{11} [fällt]{13}, [den]{15} [wird er zermalmen]{14}.»",
 "MAT.21.45": "Und{1} [als]{2} [die Hohepriester]{3,4} und{5} [die Pharisäer]{6,7} [seine]{8,10} [Gleichnisse]{9} [hörten]{2}, [erkannten sie]{11}, [dass]{12} [er]{15} [von]{13} [ihnen]{14} [redete]{15}.",
 "MAT.21.46": "Und{1} [sie suchten]{2} [ihn]{3} [festzunehmen]{4}, [fürchteten]{5} aber [die Menschenmengen]{6,7}, [weil]{8} [sie]{12} [ihn]{11} [für]{9} [einen Propheten]{10} [hielten]{12}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 20
 "MAT.20.1": "«[Dänn]{2} [mit em Riich]{4,5} [vo de Himel]{6,7} [isch es]{3} [wie]{1} [mit eme Huusherr]{8,9}, [wo]{10} [am Morge früe]{12,13} [use isch]{11} [go]{14} [Arbeiter]{15} [für]{16} [sin]{17,19} [Wiibärg]{18} [aastelle]{14}.",
 "MAT.20.2": "[Er isch sich]{1} [aber]{2} [mit]{3} [de Arbeiter]{4,5} [uf]{6} [en Denar]{7} [für de]{8} [Tag]{9} [einig worde]{1} und [hät]{10} [si]{11} [i]{12} [sin]{13,15} [Wiibärg]{14} [gschickt]{10}.",
 "MAT.20.3": "Und{1} [won er]{2} [um]{3} [di dritt]{4} [Stund]{5} [use isch]{2}, [hät er]{6} [anderi]{7} [ohni Arbet]{12} [uf]{9} [em]{10} [Märt]{11} [umestaa]{8} [gseh]{6}.",
 "MAT.20.4": "Und{1} [zu dene]{2} [hät er]{3} [gseit]{3}: ‹[Gönd]{4} [au]{5} [ir]{6} [in]{7,8} [Wiibärg]{9}, und{10} [was]{11,12} [rächt]{14} [isch]{13}, [gib ich]{15} [eu]{16}.›",
 "MAT.20.5": "[Si]{1} [aber]{2} [sind gange]{3}. [Wider]{4} [isch er]{5} [um]{6} [di sächst]{7} und{8} [di nüünt]{9} [Stund]{10} [use]{5} und [hät s]{11} [gliich]{12} [gmacht]{11}.",
 "MAT.20.6": "[Won er]{5} [aber]{2} [um]{1} [di elft]{3,4} Stund [use isch]{5}, [hät er]{6} [anderi]{7} [umestaa]{8} [gfunde]{6} und{9} [seit]{10} [zu ine]{11}: ‹[Werum]{12} [stönd ir]{14} [de ganz]{15,16} [Tag]{17} [ohni Arbet]{18} [da]{13} [ume]{14}?›",
 "MAT.20.7": "[Si säged]{1} [zu ihm]{2}: ‹[Wil]{3} [üs]{5} [niemer]{4} [aagstellt hät]{6}.› [Er seit]{7} [zu ine]{8}: ‹[Gönd]{9} [au]{10} [ir]{11} [in]{12,13} [Wiibärg]{14}!›",
 "MAT.20.8": "[Wo s]{3} [aber]{2} [Aabig]{1} [worde isch]{3}, [seit]{4} [de Herr]{5,6} [vom Wiibärg]{7,8} [zu sim]{9,11} [Verwalter]{10}: ‹[Rüef]{12} [d Arbeiter]{13,14} und{15} [zahl]{16} [ine]{17} [de Loon]{18,19} [us]{16}, [aagfange]{20} [bi]{21} [de Letschte]{22,23} [bis]{24} [zu de Erschte]{25,26}!›",
 "MAT.20.9": "Und{1} [die]{3} [vo]{4} [de elfte]{5,6} [Stund]{7} [sind choo]{2} und [händ]{8} [je]{9} [en Denar]{10} [übercho]{8}.",
 "MAT.20.10": "Und{1} [wo]{2} [di Erschte]{3,4} [choo sind]{2}, [händ si gmeint]{5}, [dass]{6} [si]{8} [meh]{7} [überchömed]{8}; und{9} [au]{14} [si]{15} [händ]{10} [je]{11,12} [en Denar]{13} [übercho]{10}.",
 "MAT.20.11": "[Wo si en]{1} [aber]{2} [übercho händ]{1}, [händ si]{3} [über]{4} [de Huusherr]{5,6} [gmuulet]{3}",
 "MAT.20.12": "und [gseit]{1}: ‹[Die]{2} [Letschte]{3,4} [händ]{7} [e]{5} [Stund]{6} [gschaffet]{7}, und{8} [du häsch]{12} [si]{10} [üs]{11} [gliichgstellt]{9}, [üs, wo]{13} [d Lascht]{15,16} [vom Tag]{17,18} und{19} [d Hitz]{20,21} [treit händ]{14}.›",
 "MAT.20.13": "[Er]{1} [aber]{2} [hät]{3} [eim]{4} [vo ine]{5} [gantwortet]{3} und [gseit]{6}: ‹[Fründ]{7}, [ich tue]{9} [dir]{10} [kei]{8} [Unrächt]{9}. [Bisch du]{13} [nöd]{11} [mit mir]{14} [uf en Denar]{12} [einig worde]{13}?",
 "MAT.20.14": "[Nimm]{1}, [was dir ghört]{2,3}, und{4} [gang]{5}! [Ich wott]{6} [aber]{7} [däm]{8} [Letschte]{9,10} [gää]{11} [wie]{12} [au]{13} [dir]{14}.",
 "MAT.20.15": "[Dörf]{2} [ich]{3} [mit]{7} [mim Eigete]{8,9} [nöd]{1} [mache]{6}, [was]{4} [ich wott]{5}? [Oder]{10} [isch]{15} [dis]{13} [Aug]{11,12} [böös]{14}, [wil]{16} [ich]{17} [guet]{18} [bi]{19}?›",
 "MAT.20.16": "[So]{1} [wärded]{2} [di Letschte]{3,4} [Erschti]{5} [sii]{2} und{6} [di Erschte]{7,8} [Letschti]{9}.»",
 "MAT.20.17": "Und{1} [wo]{2} [de Jesus]{3,4} [uf]{5} [Jerusalem]{6} [ufe gange isch]{2}, [hät er]{7} [di]{8} [zwölf]{9} [Jünger]{10} [uf d Siite]{11,12} [gnoo]{7} und{13} [uf]{14} [em]{15} [Wäg]{16} [zu ine]{18} [gseit]{17}:",
 "MAT.20.18": "«[Lueg]{1}, [mir gönd]{2} [uf]{3} [Jerusalem]{4} [ufe]{2}, und{5} [de Mänschesohn]{6-9} [wird]{10} [de Hoheprieschter]{11,12} und{13} [de Schriftgelehrte]{14} [usgliferet]{10}, und{15} [si wärded]{16} [en]{17} [zum Tod]{18} [verurteile]{16}",
 "MAT.20.19": "und{1} [si wärded]{2} [en]{3} [de Heide]{4,5} [usliefere]{2}, [damit si en]{6,7} [verspotted]{8} und{9} [uspeitsched]{10} und{11} [chrüziged]{12}; und{13} [am dritte]{14,15} [Tag]{16} [wird er uferweckt]{17}.»",
 "MAT.20.20": "[Dänn]{1} [isch]{2} [d Mueter]{4,5} [vo de Söhn]{6,7} [vom Zebedäus]{8} [mit]{9} [ire]{10,12} [Söhn]{11} [zu ihm]{3} [härechoo]{2}, [hät sich vor ihm nidergworfe]{13} und{14} [hät]{15} [en]{17,18} [um öppis]{16} [bätte]{15}.",
 "MAT.20.21": "[Er]{1} [aber]{2} [hät]{3} [zu ire]{4} [gseit]{3}: «[Was]{5} [wottsch]{6}?» [Si seit]{7} [zu ihm]{8}: «[Säg]{9}, [dass]{10} [mini]{16} [zwei]{14} [Söhn]{15} [da]{12,13} [i]{26} [dim]{27,29} [Riich]{28} [dörfed]{10} [sitze]{11}, [eine]{17} [a]{18} [dinere]{20} [Rächte]{19} und{21} [eine]{22} [a]{23} [dinere]{25} [Linke]{24}!»",
 "MAT.20.22": "[De Jesus]{3,4} [aber]{2} [hät gantwortet]{1} und [gseit]{5}: «[Ir wüssed]{7} [nöd]{6}, [was]{8} [ir verlanged]{9}. [Chönd ir]{10} [de Bächer]{12,13} [trinke]{11}, [wo]{14} [ich]{15} [jetzt dänn]{16} [trinke]{17}?» [Si säged]{18} [zu ihm]{19}: «[Mir chönd s]{20}.»",
 "MAT.20.23": "[Er seit]{1} [zu ine]{2}: «[Min]{6} [Bächer]{3,5} [wärded ir]{7} [scho]{4} [trinke]{7}; [s Sitze]{8,10} [aber]{9} [a]{11} [minere]{13} [Rächte]{12} und{14} [a]{15} [de Linke]{16} [z vergää]{20}, [staat]{18} [nöd]{17} [mir]{19} [zue]{18}, [sondern]{21} es ghört [dene, für die]{22} s [vo]{24} [mim]{25,27} [Vatter]{26} [parat gmacht isch]{23}.»",
 "MAT.20.24": "Und{1} [wo]{2} [di Zää]{3,4} [das ghört händ]{2}, [händ si sich]{5} [über]{6} [di]{7} [zwei]{8} [Brüedere]{9} [ergeret]{5}.",
 "MAT.20.25": "[De Jesus]{1,3} [aber]{2} [hät]{4} [si]{5} [zu sich]{4} [grüeft]{4} und [gseit]{6}: «[Ir wüssed]{7}, [dass]{8} [d Herrscher]{9,10} [vo de Völker]{11,12} [si]{14} [underdrucked]{13} und{15} [d Grosse]{16,17} [Gwalt über si bruuched]{18,19}.",
 "MAT.20.26": "[So]{2} [söll s]{3} [nöd]{1} [sii]{3} [under]{4} [eu]{5}; [sondern]{6} [wer]{7,8} [under]{10} [eu]{11} [gross]{12} [wärde]{13} [wott]{9}, [dä söll]{14} [eue]{15} [Diener]{16} [sii]{14},",
 "MAT.20.27": "und{1} [wer]{2,3} [under]{5} [eu]{6} [de Erscht]{8} [sii]{7} [wott]{4}, [dä söll]{9} [eue]{10} [Sklav]{11} [sii]{9},",
 "MAT.20.28": "[so wie]{1} [de Mänschesohn]{2-5} [nöd]{6} [choo isch]{7}, [zum sich la diene]{8}, [sondern]{9} [zum diene]{10} und{11} [zum]{12} [sis]{13,15} [Läbe]{14} [gää]{12} [als Lösgält]{16} [für]{17} [vili]{18}.»",
 "MAT.20.29": "Und{1} [wo]{2} [si]{3} [vo]{4} [Jericho]{5} [furtgange sind]{2}, [isch]{6} [ihm]{7} [e grossi]{9} [Mängi]{8} [nachegfolget]{6}.",
 "MAT.20.30": "Und{1} [lueg]{2}, [zwei]{3} [Blindi]{4} [sind]{5} [am]{6,7} [Wäg]{8} [gsässe]{5}; [wo si ghört händ]{9}, [dass]{10} [de Jesus]{11} [verbiigaat]{12}, [händ si gschroue]{13}: «[Herr]{15}, [häb Erbarme]{16} [mit üs]{17}, [Sohn]{18} [vom David]{19}!» ~14(λέγοντες «sägend» leitet di diräkt Red ii)",
 "MAT.20.31": "[D Mängi]{1,3} [aber]{2} [hät]{4} [si]{5} [aagfahre]{4}, [si söled]{6} [still sii]{7}; [si]{8} [aber]{9} [händ]{11} [no lüüter]{10} [gschroue]{11}: «[Herr]{13}, [häb Erbarme]{14} [mit üs]{15}, [Sohn]{16} [vom David]{17}!» ~12(λέγοντες «sägend» leitet di diräkt Red ii)",
 "MAT.20.32": "Und{1} [de Jesus]{3,4} [isch staa blibe]{2}, [hät]{5} [si]{6} [grüeft]{5} und{7} [gseit]{8}: «[Was]{9} [wänd ir]{10}, [dass ich]{11} [eu]{12} [mache]{11}?»",
 "MAT.20.33": "[Si säged]{1} [zu ihm]{2}: «[Herr]{3}, [dass]{4} [öisi]{8} [Auge]{6,7} [ufgönd]{5}!»",
 "MAT.20.34": "[De Jesus]{3,4} [aber]{2} [hät Erbarme gha]{1} und [hät]{5} [iri]{8} [Auge]{6,7} [aagrüert]{5}, und{9} [grad]{10} [händ si wider gseh]{11}, und{12} [si sind]{13} [ihm]{14} [nachegfolget]{13}.",
 # ------------------------------------------------------------ Kapitel 21
 "MAT.21.1": "Und{1} [wo]{2} [si]{3} [i d Nöchi]{3} [vo]{4} [Jerusalem]{5} [choo]{3} und{6} [z]{8} [Betfage]{9} [am]{10,11} [Ölberg]{12-14} [aachoo sind]{7}, [dänn]{15} [hät]{17} [de Jesus]{16} [zwei]{18} [Jünger]{19} [losgschickt]{17}",
 "MAT.21.2": "und [hät]{1} [zu ine]{2} [gseit]{1}: «[Gönd]{3} [i]{4} [das]{5} [Dorf]{6}, [wo]{7} [vor]{8} [eu]{9} [liit]{8}, und{10} [grad]{11} [wärded ir]{12} [e Eselin]{13} [aabunde]{14} [finde]{12} und{15} [es Füli]{16} [bi]{17} [ire]{18}. [Binded si los]{19} und [bringed si]{20} [zu mir]{21}!",
 "MAT.21.3": "Und{1} [wänn]{2} [öpper]{3} [eu]{4} [öppis]{6} [seit]{5}, [dänn säged]{7}: ‹[De Herr]{9,10} [bruucht]{12,13} [si]{11}.› [Er wird]{16} [si]{17} [aber]{15} [grad]{14} [schicke]{16}.» ~8(ὅτι leitet di diräkt Red ii)",
 "MAT.21.4": "[Das]{1} [isch]{3} [aber]{2} [gscheh]{3}, [damit]{4} [erfüllt wird]{5}, [was]{6} [dur]{8} [de Prophet]{9,10} [gseit worden isch]{7}: ~11(λέγοντος «wo seit» leitet s Zitat ii)",
 "MAT.21.5": "«[Säged]{1} [de Tochter]{2,3} [Zion]{4}: [Lueg]{5}, [din]{8} [König]{6,7} [chunnt]{9} [zu dir]{10}, [sanftmüetig]{11} und{12} [rittet]{13} [uf]{14} [ere Eselin]{15} und{16} [uf]{17} [eme Füli]{18}, [em Junge]{19} [vo me Lasttier]{20}.»",
 "MAT.21.6": "[D Jünger]{3,4} [aber]{2} [sind gange]{1} und{5} [händ gmacht]{6}, [wie]{7} [s ine]{9} [de Jesus]{10,11} [uftreit hät]{8}.",
 "MAT.21.7": "[Si händ]{1} [d Eselin]{2,3} und{4} [s Füli]{5,6} [brocht]{1} und{7} [händ]{8} [d Mäntel]{11,12} [uf]{9} [si]{10} [gleit]{8}, und{13} [er hät sich]{14} [druf]{15,16} [gsetzt]{14}.",
 "MAT.21.8": "[Di meischte]{1,3} [vo de Mängi]{4} [aber]{2} [händ]{5} [iri]{6} [Mäntel]{7,8} [uf]{9} [em]{10} [Wäg]{11} [usbreitet]{5}; [anderi]{12} [aber]{13} [händ]{14} [Zweig]{15} [vo]{16} [de Bäum]{17,18} [abghaue]{14} und{19} [händ si]{20} [uf]{21} [em]{22} [Wäg]{23} [usbreitet]{20}.",
 "MAT.21.9": "[D Lüüt]{1,3} [aber]{2}, [wo]{4} [ihm]{6} [voruusgange sind]{5}, und{7} [die]{8}, [wo nachechoo sind]{9}, [händ grüeft]{10}: «[Hosanna]{12} [em Sohn]{13,14} [vom David]{15}! [Gsägnet]{16} sig [dä, wo]{17} [chunnt]{18} [im]{19} [Name]{20} [vom Herr]{21}! [Hosanna]{22} [i]{23} [de Höchi]{24,25}!» ~11(λέγοντες «sägend» leitet di diräkt Red ii)",
 "MAT.21.10": "Und{1} [wo]{2} [er]{3} [uf]{4} [Jerusalem]{5} [ine choo isch]{2}, [isch]{6} [di ganz]{7,8} [Stadt]{9} [in Ufruer graate]{6} und [hät gseit]{10}: «[Wer]{11} [isch]{12} [dä]{13}?»",
 "MAT.21.11": "[D Lüüt]{1,3} [aber]{2} [händ gseit]{4}: «[Das]{5} [isch]{6} [de Prophet]{7,8} [Jesus]{9} [vo]{10,11} [Nazaret]{12} [in Galiläa]{13,14}.»",
 "MAT.21.12": "Und{1} [de Jesus]{3} [isch]{2} [in]{4,5} [Tämpel]{6} [ine gange]{2} und{7} [hät]{8} [alli]{9} [usegjagt]{8}, [wo]{10} [im]{14,15} [Tämpel]{16} [verchauft]{11} und{12} [gchauft händ]{13}; und{17} [d Tisch]{18,19} [vo de Gältwächsler]{20,21} und{23} [d Stüel]{24,25} [vo de Tuubeverchäufer]{26-29} [hät er umgschmisse]{22},",
 "MAT.21.13": "und{1} [seit]{2} [zu ine]{3}: «[Es staat gschribe]{4}: ‹[Mis]{7} [Huus]{5,6} [söll]{10} [es Huus]{8} [zum Bätte]{9} [heisse]{10}.› [Ir]{11} [aber]{12} [mached]{14} [e Röiberhöli]{15,16} [drus]{13}.»",
 "MAT.21.14": "Und{1} [es sind]{2} [Blindi]{4} und{5} [Lahmi]{6} [im]{7,8} [Tämpel]{9} [zu ihm]{3} [härechoo]{2}, und{10} [er hät]{11} [si]{12} [gheilt]{11}.",
 "MAT.21.15": "[Wo]{1} [aber]{2} [d Hoheprieschter]{3,4} und{5} [d Schriftgelehrte]{6,7} [di erstuunliche Sache]{8,9} [gseh händ]{1}, [wo]{10} [er gmacht hät]{11}, und{12} [d Chind]{13,14}, [wo]{15} [im]{17,18} [Tämpel]{19} [grüeft]{16} und{20} [gseit händ]{21}: «[Hosanna]{22} [em Sohn]{23,24} [vom David]{25}!», [händ si sich ergeret]{26}.",
 "MAT.21.16": "Und{1} [si händ]{2} [zu ihm]{3} [gseit]{2}: «[Ghörsch]{4}, [was]{5} [die]{6} [säged]{7}?» [De Jesus]{8,10} [aber]{9} [seit]{11} [zu ine]{12}: «[Ja]{13}. [Händ ir]{15} [nie]{14} [gläse]{15}: ‹[Us]{17} [em Muul]{18} [vo chliine Chind]{19} und{20} [Söiglinge]{21} [häsch du dir]{22} [Lob]{23} [parat gmacht]{22}›?» ~16(ὅτι leitet s Zitat ii)",
 "MAT.21.17": "Und{1} [er hät]{2} [si]{3} [verlaa]{2}, [isch]{4} [us]{5} [de Stadt]{6,7} [use]{4} [uf]{8} [Betanie]{9} [gange]{4} und{10} [hät]{11} [dört]{12} [übernachtet]{11}.",
 "MAT.21.18": "[Wo er]{3} [aber]{2} [am Morge früe]{1} [i]{4} [d Stadt]{5,6} [zrugg gange isch]{3}, [hät er Hunger gha]{7}.",
 "MAT.21.19": "Und{1} [wo er]{2} [en]{4} [Fiigebaum]{3} [am]{5,6} [Wäg]{7} [gseh hät]{2}, [isch er]{8} [zu]{9} [em]{10} [ane gange]{8} und{11} [hät]{13} [nüüt]{12} [dra]{14,15} [gfunde]{13} [als]{16,17} [nu]{19} [Bletter]{18}; und{20} [er seit]{21} [zu em]{22}: «[Nie meh]{23} [i]{28} [Ewigkeit]{29,30} [söll]{27} [us]{24} [dir]{25} [Frucht]{26} [wachse]{27}!» Und{31} [de Fiigebaum]{34,35} [isch]{32} [uf de Stell]{33} [verdorret]{32}.",
 "MAT.21.20": "Und{1} [wo]{2} [d Jünger]{3,4} [das gseh händ]{2}, [händ si gstuunt]{5} und [gseit]{6}: «[Wie]{7} [isch]{9} [de Fiigebaum]{10,11} [uf de Stell]{8} [verdorret]{9}?»",
 "MAT.21.21": "[De Jesus]{3,4} [aber]{2} [hät gantwortet]{1} und [zu ine]{6} [gseit]{5}: «[Amen]{7}, [ich säg]{8} [eu]{9}: [Wänn]{10} [ir]{11} [Glaube]{12} [händ]{11} und{13} [nöd]{14} [zwiifled]{15}, [wärded ir]{21} [nöd]{16} [nu]{17} [das mit]{18,19} [em Fiigebaum]{20} [mache]{21}, [sondern]{22} [au wänn]{23} [ir]{27} [zu dem]{24,26} [Bärg]{25} [säged]{27}: ‹[Heb di uf]{28} und{29} [stürz di]{30} [is]{31,32} [Meer]{33}!›, [wird s passiere]{34}.",
 "MAT.21.22": "Und{1} [alles]{2}, [wo]{3,4} [ir]{5} [im]{6,7} [Gebät]{8} [drum bitted]{5}, [wärded ir übercho]{10}, [wänn ir glaubed]{9}.»",
 "MAT.21.23": "Und{1} [wo]{2} [er]{3} [in]{4,5} [Tämpel]{6} [gange isch]{2}, [sind]{7} [d Hoheprieschter]{10,11} und{12} [d Ältischte]{13,14} [vom Volk]{15,16} [zu ihm]{8} [härechoo]{7}, [während er glehrt hät]{9}, und [händ gseit]{17}: «[Mit]{18} [was für ere]{19} [Vollmacht]{20} [machsch du]{22} [das]{21}? Und{23} [wer]{24} [hät]{26} [dir]{25} [die]{27,29} [Vollmacht]{28} [gää]{26}?»",
 "MAT.21.24": "[De Jesus]{3,4} [aber]{2} [hät gantwortet]{1} und [zu ine]{6} [gseit]{5}: «[Au ich]{9} [stell]{7} [eu]{8} [e]{11} [Frag]{10}; [wänn]{13} [ir]{14} [si]{12} [mir]{15} [beantworted]{14}, [säg]{18} [au ich]{16} [eu]{17}, [mit]{19} [was für ere]{20} [Vollmacht]{21} [ich]{23} [das]{22} [mache]{23}.",
 "MAT.21.25": "[D Taufi]{1,2} [vom Johannes]{3,4} – [vo wo]{5} [isch si gsii]{6}? [Vom]{7} [Himel]{8} [oder]{9} [vo]{10} [Mänsche]{11}?» [Si]{12} [aber]{13} [händ]{14} [under sich]{15,16} [überleit]{14} und [gseit]{17}: «[Wänn]{18} [mer säged]{19}: ‹[Vom]{20} [Himel]{21}›, [seit er]{22} [zu üs]{23}: ‹[Werum]{24,25} [händ ir]{28} [em]{29} [dänn]{26} [nöd]{27} [glaubt]{28}?›",
 "MAT.21.26": "[Wänn]{1} [mer]{3} [aber]{2} [säged]{3}: ‹[Vo]{4} [Mänsche]{5}›, [händ mer Angscht]{6} [vor de Mängi]{7,8}; [dänn]{10} [alli]{9} [halted]{13} [de Johannes]{14,15} [für]{11} [en Prophet]{12}.»",
 "MAT.21.27": "Und{1} [si händ]{2} [em Jesus]{3,4} [gantwortet]{2} und [gseit]{5}: «[Mir wüssed s]{7} [nöd]{6}.» [Und]{10} [er]{11} [hät]{8} [zu ine]{9} [gseit]{8}: «[Au ich]{13} [säg]{14} [eu]{15} [nöd]{12}, [mit]{16} [was für ere]{17} [Vollmacht]{18} [ich]{20} [das]{19} [mache]{20}.»",
 "MAT.21.28": "«[Was]{1} [meined]{4} [ir]{3} [aber]{2}? [En Mänsch]{5} [hät]{6} [zwei]{8} [Chind]{7} [gha]{6}. [Er isch]{9} [zum]{10} [erschte]{11} [härechoo]{9} und [hät gseit]{12}: ‹[Chind]{13}, [gang]{14} [hüt]{15} [go schaffe]{16} [im]{17,18} [Wiibärg]{19}!›",
 "MAT.21.29": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: ‹[Ich wott]{6} [nöd]{5}.› [Spöter]{7} [aber]{8} [hät s en groue]{9}, und [er isch gange]{10}.",
 "MAT.21.30": "[Er isch]{1} [aber]{2} [zum]{3} [zweite]{4} [härechoo]{1} und [hät]{5} [s gliich]{6} [gseit]{5}. [Dä]{7} [aber]{8} [hät gantwortet]{9} und [gseit]{10}: ‹[Ich]{11} gaa, [Herr]{12}!› Und{13} [er isch]{15} [nöd]{14} [gange]{15}.",
 "MAT.21.31": "[Wele]{1} [vo]{2} [de]{3} [beide]{4} [hät]{5} [de Wille]{6,7} [vom Vatter]{8,9} [gmacht]{5}?» [Si säged]{10}: «[De erscht]{11,12}.» [De Jesus]{15,16} [seit]{13} [zu ine]{14}: «[Amen]{17}, [ich säg]{18} [eu]{19}: [D Zöllner]{21,22} und{23} [d Prostituierte]{24,25} [gönd]{26} [eu]{27} [voraa]{26} [is]{28,29} [Riich]{30} [vo Gott]{31,32}. ~20(ὅτι leitet di diräkt Red ii; mit em Doppelpunkt widergää)",
 "MAT.21.32": "[Dänn]{2} [de Johannes]{3} [isch]{1} [zu]{4} [eu]{5} [choo]{1} [uf]{6} [em Wäg]{7} [vo de Grächtigkeit]{8}, und{9} [ir händ]{11} [em]{12} [nöd]{10} [glaubt]{11}; [d Zöllner]{13,15} [aber]{14} und{16} [d Prostituierte]{17,18} [händ]{19} [em]{20} [glaubt]{19}. [Ir]{21} [aber]{22} [händ s gseh]{23}, und [es hät eu]{25} [nöd emal]{24} [spöter]{26} [groue]{25}, [so dass ir]{27} [em]{29} [glaubt hetted]{28}.",
 "MAT.21.33": "[Losed]{3} [es anders]{1} [Gliichnis]{2}: [Es isch]{5} [en Huusherr]{4,6} [gsii]{5}, [wo]{7} [en Wiibärg]{9} [aapflanzt hät]{8}; und{10} [er hät]{13} [en Haag]{11} [drum ume]{12} [gmacht]{13} und{14} [hät]{15} [e Trotte]{18} [drin]{16,17} [usghobe]{15} und{19} [hät]{20} [en Turm]{21} [baut]{20} und{22} [hät]{23} [en]{24} [a Wiibuure]{25} [verpachtet]{23} und{26} [isch verreist]{27}.",
 "MAT.21.34": "[Wo]{1} [aber]{2} [d Ziit]{4,5} [vo de Frücht]{6,7} [nöch choo isch]{3}, [hät er]{8} [sini]{9,11} [Chnächt]{10} [zu]{12} [de Wiibuure]{13,14} [gschickt]{8}, [go]{15} [sini]{16,18} [Frücht]{17} [hole]{15}.",
 "MAT.21.35": "Und{1} [d Wiibuure]{3,4} [händ]{2} [sini]{5,7} [Chnächt]{6} [packt]{2}: [de eint]{8,9} [händ si verprüglet]{10}, [en andere]{11,12} [händ si umbracht]{13}, [en andere]{14,15} [händ si gsteiniget]{16}.",
 "MAT.21.36": "[Wider]{1} [hät er]{2} [anderi]{3} [Chnächt]{4} [gschickt]{2}, [meh]{5} [als]{6} [di erschte]{7}; und{8} [si händ s]{9} [mit ine]{10} [gliich]{11} [gmacht]{9}.",
 "MAT.21.37": "[Zletscht]{1} [aber]{2} [hät er]{3} [sin]{6,8} [Sohn]{7} [zu]{4} [ine]{5} [gschickt]{3} und [sich gseit]{9}: ‹[Vor mim]{11,13} [Sohn]{12} [händ si dänn Respekt]{10}.›",
 "MAT.21.38": "[Wo]{4} [d Wiibuure]{1,3} [aber]{2} [de Sohn]{5,6} [gseh händ]{4}, [händ si]{7} [zunenand]{8,9} [gseit]{7}: ‹[Das]{10} [isch]{11} [de Erb]{12,13}; [chömed]{14}, [mir bringed]{15} [en]{16} [um]{15} und{17} [überchömed]{18} [sis]{19,21} [Erb]{20}!›",
 "MAT.21.39": "Und{1} [si händ]{2} [en]{3} [packt]{2}, [us]{5} [em Wiibärg]{6,7} [usegworfe]{4} und{8} [umbracht]{9}.",
 "MAT.21.40": "[Wänn]{1} [jetzt]{2} [de Herr]{4,5} [vom Wiibärg]{6,7} [chunnt]{3}, [was]{8} [macht er]{9} [mit]{10} [dene]{12} [Wiibuure]{11}?»",
 "MAT.21.41": "[Si säged]{1} [zu ihm]{2}: «[Er wird]{5} [di Bööse]{3,6} [böös]{4} [umbringe]{5}, und{7} [de Wiibärg]{8,9} [wird er]{10} [a anderi]{11} [Wiibuure]{12} [verpachte]{10}, [wo]{13} [ihm]{15} [d Frücht]{16,17} [zu]{18} [irer]{19,21} [Ziit]{20} [abgänd]{14}.»",
 "MAT.21.42": "[De Jesus]{3,4} [seit]{1} [zu ine]{2}: «[Händ ir]{6} [nie]{5} [i]{7} [de Schrifte]{8,9} [gläse]{6}: ‹[De Stei]{10}, [wo]{11} [d Buulüüt]{13,14} [verworfe händ]{12}, [dä]{15} [isch]{16} [zum Eckstei]{17-19} [worde]{16}; [vom]{20} [Herr]{21} [isch]{22} [das]{23} [gscheh]{22}, und{24} [es isch]{25} [wunderbar]{26} [i]{27} [öisne]{29} [Auge]{28}›?",
 "MAT.21.43": "[Drum]{1,2} [säg ich]{3} [eu]{4}: [S Riich]{9,10} [vo Gott]{11,12} [wird]{6} [eu]{7,8} [wäggnoo]{6} und{13} [eme Volk]{15} [gää]{14}, [wo]{16} [sini]{17,19} [Frücht]{18} [bringt]{16}. ~5(ὅτι leitet d Ussag ii; mit em Doppelpunkt widergää)",
 "MAT.21.44": "Und{1} [wer]{2} [uf]{4} [dä]{5,7} [Stei]{6} [gheit]{3}, [wird verschmätteret]{8}; [uf wän]{9,10,12} [er]{13} [aber]{11} [gheit]{13}, [dä]{15} [zermalmt er]{14}.»",
 "MAT.21.45": "Und{1} [wo]{2} [d Hoheprieschter]{3,4} und{5} [d Pharisäer]{6,7} [sini]{8,10} [Gliichnis]{9} [ghört händ]{2}, [händ si gmerkt]{11}, [dass]{12} [er]{15} [vo]{13} [ine]{14} [redt]{15}.",
 "MAT.21.46": "Und{1} [si händ probiert]{2}, [en]{3} [feschtznää]{4}, [händ]{5} aber [Angscht gha]{5} [vor de Lüüt]{6,7}, [wil]{8} [die]{12} [en]{11} [für]{9} [en Prophet]{10} [ghalte händ]{12}.",
}

DEC_DE = [
 ("MAT.20.1", "das Reich der Himmel", "literal", "ἡ βασιλεία τῶν οὐρανῶν", None, ["das Himmelreich"],
  "Einheitliche Wiedergabe für das ganze Matthäusevangelium. Matthäus sagt meist «Reich der Himmel» (griechisch Plural), wo Markus und Lukas «Reich Gottes» haben; viele sehen darin die jüdische Scheu, den Gottesnamen auszusprechen, nicht einen anderen Inhalt. In diesem Bereich steht zweimal «Reich Gottes» ([[MAT.21.31]], [[MAT.21.43]])."),
 ("MAT.20.1", "einem Hausherrn", "adapted", "ἀνθρώπῳ οἰκοδεσπότῃ", "einem Menschen, einem Hausherrn", None,
  "Die Doppelung «Mensch, Hausherr» ist eine semitisch geprägte Ausdrucksweise; sie ist in eine Wendung zusammengezogen. Ebenso [[MAT.21.33]]. οἰκοδεσπότης ist der Herr eines Hauswesens mit Besitz und Gesinde."),
 ("MAT.20.2", "einen Denar", "literal", "δηναρίου", None, None,
  "Römische Silbermünze; verbreitet als üblicher Tageslohn eines Arbeiters verstanden. Die Lohnabsprache ist für den Fortgang wichtig ([[MAT.20.13]])."),
 ("MAT.20.3", "um die dritte Stunde", "literal", "περὶ τρίτην ὥραν", None, ["um neun Uhr"],
  "Die Stunden des Tages wurden ab Sonnenaufgang gezählt: die dritte etwa 9 Uhr, die sechste Mittag, die neunte etwa 15 Uhr, die elfte etwa 17 Uhr, kurz vor Arbeitsschluss. Die Übersetzung behält die antike Zählung."),
 ("MAT.20.3", "untätig", "literal", "ἀργούς", None, ["ohne Arbeit", "müssig"],
  "ἀργός heisst «ohne Arbeit, untätig»; hier eher arbeitslos als faul, wie [[MAT.20.7]] zeigt."),
 ("MAT.20.9", "die von der elften Stunde", "adapted", "οἱ περὶ τὴν ἑνδεκάτην ὥραν", "die um die elfte Stunde", None,
  "Gemeint sind die, die um die elfte Stunde angeworben wurden ([[MAT.20.6]])."),
 ("MAT.20.11", "murrten", "literal", "ἐγόγγυζον", None, ["beschwerten sich"],
  "Dasselbe Verb steht in der Septuaginta für das Murren Israels in der Wüste (z. B. [[NUM.14.27]]); ob Matthäus darauf anspielt, ist offen."),
 ("MAT.20.12", "gearbeitet", "adapted", "ἐποίησαν", "gemacht", None,
  "ποιέω «machen, tun» mit Zeitangabe meint hier die Arbeitszeit."),
 ("MAT.20.13", "Freund", "adapted", "Ἑταῖρε", None, ["Kamerad", "mein Lieber"],
  "ἑταῖρος ist eine freundliche, aber distanzierte Anrede an jemanden, der im Unrecht ist; bei Matthäus noch [[MAT.22.12]] und [[MAT.26.50]]."),
 ("MAT.20.15", "ist dein Auge böse", "literal", "ὁ ὀφθαλμός σου πονηρός ἐστιν", None, ["bist du neidisch", "bist du missgünstig"],
  "«Böses Auge» ist eine biblische Wendung für Neid und Missgunst (vgl. [[DEU.15.9]], [[MAT.6.23]]). Die wörtliche Wiedergabe erhält den Gegensatz zu «gütig»."),
 ("MAT.20.15", "gütig", "interpretive", "ἀγαθός", "gut", ["grosszügig"],
  "ἀγαθός heisst «gut»; im Gegenüber zum «bösen Auge» ist die Güte als Grosszügigkeit gemeint."),
 ("MAT.20.16", "So werden die Letzten Erste sein", "literal", "οὕτως ἔσονται οἱ ἔσχατοι πρῶτοι", None, None,
  "Der Satz nimmt [[MAT.19.30]] in umgekehrter Reihenfolge auf und rahmt so das Gleichnis."),
 ("MAT.20.18", "ausgeliefert werden", "literal", "παραδοθήσεται", None, ["übergeben werden", "verraten werden"],
  "παραδίδωμι «ausliefern» wird auch für die Tat des Judas gebraucht ([[MAT.26.15]]); die Übersetzung bleibt bei «ausliefern» wie bei Markus."),
 ("MAT.20.19", "den Heiden", "interpretive", "τοῖς ἔθνεσιν", "den Völkern", ["den Nichtjuden"],
  "ἔθνη heisst «Völker»; aus jüdischer Sicht die Nichtjuden, hier die römische Macht. Wo der Plural die Völker als Herrschaftsgebiete meint, steht «Völker» ([[MAT.20.25]]); in [[MAT.21.43]] steht der Singular «einem Volk»."),
 ("MAT.20.19", "wird er auferweckt werden", "literal", "ἐγερθήσεται", None, ["wird er auferstehen"],
  "Passiv: Gott ist als Handelnder mitzudenken. Die Ankündigungen [[MAT.16.21]] und [[MAT.17.23]] haben dasselbe Verb. Zur Lesart ἀναστήσεται («wird auferstehen») siehe Alternativen."),
 ("MAT.20.20", "die Mutter der Söhne des Zebedäus", "literal", "ἡ μήτηρ τῶν υἱῶν Ζεβεδαίου", None, None,
  "In [[MRK.10.35]] bitten Jakobus und Johannes selbst; bei Matthäus kommt die Mutter mit ihnen, Jesus antwortet aber in der Mehrzahl ([[MAT.20.22]]). Sie wird auch in [[MAT.27.56]] genannt."),
 ("MAT.20.20", "trat", "literal", "προσῆλθεν", "kam herzu", ["kam"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: προσέρχομαι «herantreten» (Mundart «härechoo»); ebenso [[MAT.21.14]], [[MAT.21.23]], [[MAT.21.28]], [[MAT.21.30]] (dort: an den Sohn herantreten)."),
 ("MAT.20.20", "warf sich vor ihm nieder", "interpretive", "προσκυνοῦσα", "sich niederwerfend", ["huldigte ihm", "betete ihn an", "fiel vor ihm nieder"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: προσκυνέω vor Menschen und vor Jesus «sich niederwerfen», mit Gott als Empfänger «anbeten». προσκυνέω bezeichnet das Niederfallen vor einer höhergestellten Person oder vor Gott. Matthäus braucht das Wort oft gegenüber Jesus (z. B. [[MAT.2.11]], [[MAT.14.33]], [[MAT.28.9]]). Ob Huldigung oder Anbetung gemeint ist, hängt vom Zusammenhang ab; die Übersetzung beschreibt die Gebärde und lässt die Deutung offen."),
 ("MAT.20.21", "sitzen dürfen", "adapted", "ἵνα καθίσωσιν", "dass … sitzen", None,
  "Der griechische Satz mit ἵνα drückt eine Bitte aus; «dürfen» macht das im Deutschen deutlich. Rechts und links vom König zu sitzen bedeutet die höchsten Ehrenplätze."),
 ("MAT.20.22", "den Becher", "literal", "τὸ ποτήριον", None, ["den Kelch"],
  "Der Becher ist in der Bibel ein Bild für das zugemessene Geschick, oft für Leid und Gericht ([[ISA.51.17]]); vgl. [[MAT.26.39]]. «Kelch» ist die vertraute kirchliche Wiedergabe."),
 ("MAT.20.25", "unterdrücken", "interpretive", "κατακυριεύουσιν", "herrschen über", ["unterjochen"],
  "κατακυριεύω und κατεξουσιάζω betonen die Herrschaft «von oben herab»; wie in [[MRK.10.42]] wiedergegeben."),
 ("MAT.20.26", "So soll es nicht sein", "interpretive", "οὐχ οὕτως ἔσται", "So wird es nicht sein", ["So ist es nicht"],
  "Das Futur ἔσται (ebenso in [[MAT.20.26]]–[[MAT.20.27]] «der soll … sein») ist als Weisung verstanden. Der SBLGNT folgt hier der Lesart, die unter den erfassten Ausgaben nur NA28 hat; zum Präsens ἐστίν («ist») siehe Alternativen."),
 ("MAT.20.27", "Sklave", "literal", "δοῦλος", None, ["Knecht", "Diener"],
  "δοῦλος ist der unfreie Diener, der einem Herrn gehört. Im Spruch steht wie in [[MRK.10.44]] «Sklave», um die Schärfe zu erhalten; im Gleichnis [[MAT.21.34]]–[[MAT.21.36]] steht «Knechte» (siehe dort)."),
 ("MAT.20.28", "Leben", "literal", "ψυχὴν", None, ["Seele"],
  "ψυχή meint hier das Leben der ganzen Person, nicht einen Teil des Menschen."),
 ("MAT.20.28", "als Lösegeld für viele", "literal", "λύτρον ἀντὶ πολλῶν", None, ["als Lösegeld anstelle von vielen"],
  "λύτρον ist der Preis für den Freikauf von Gefangenen oder Sklaven; ἀντί heisst «anstelle von, für». «Viele» kann nach semitischem Sprachgebrauch die Gesamtheit meinen (vgl. [[ISA.53.12]]); wie weit, wird verschieden beurteilt. Wortgleich [[MRK.10.45]]."),
 ("MAT.20.30", "zwei Blinde", "literal", "δύο τυφλοὶ", None, None,
  "[[MRK.10.46]] und [[LUK.18.35]] erzählen von einem Blinden; Matthäus nennt zwei (ebenso zwei Blinde in [[MAT.9.27]] und zwei Besessene in [[MAT.8.28]])."),
 ("MAT.20.30", "hab Erbarmen mit uns", "adapted", "ἐλέησον ἡμᾶς", "erbarme dich unser", None,
  "Die wörtliche Form «erbarme dich unser» ist im heutigen Deutsch veraltet. In [[MAT.20.34]] steht für σπλαγχνίζομαι ebenfalls «Erbarmen haben»; das Griechische unterscheidet die beiden Verben."),
 ("MAT.20.30", "Sohn Davids", "literal", "υἱὸς Δαυίδ", None, ["Sohn von David"],
  "Messianischer Titel, bei Matthäus häufig ([[MAT.1.1]], [[MAT.9.27]], [[MAT.21.9]], [[MAT.21.15]])."),
 ("MAT.20.34", "hatte Erbarmen", "interpretive", "σπλαγχνισθεὶς", "im Innersten bewegt", ["wurde von Mitgefühl ergriffen", "es jammerte ihn"],
  "Einheitliche Wiedergabe für das Matthäusevangelium: σπλαγχνίζομαι «Erbarmen haben (mit)», wie [[MAT.14.14]] und [[MRK.6.34]]. σπλάγχνα sind die Eingeweide als Sitz der Gefühle. Das Wort ist im Griechischen ein anderes als ἐλεέω in der Bitte «hab Erbarmen» ([[MAT.20.30]]); die gleiche deutsche Wiedergabe lässt Bitte und Antwort zusammenklingen."),
 ("MAT.21.2", "eine Eselin", "literal", "ὄνον", None, None,
  "ὄνος ist hier weiblich (δεδεμένην, «angebunden»). Markus, Lukas und Johannes nennen nur ein Tier; Matthäus nennt Eselin und Fohlen, entsprechend dem Wortlaut von [[ZEC.9.9]] ([[MAT.21.5]])."),
 ("MAT.21.3", "Der Herr", "interpretive", "Ὁ κύριος", None, ["Ihr Herr", "Der Meister"],
  "κύριος kann «Herr, Besitzer» oder als Würdetitel auf Jesus bezogen sein. αὐτῶν («ihrer») gehört zu χρείαν ἔχει: «braucht sie»."),
 ("MAT.21.3", "Er wird sie aber sogleich schicken", "interpretive", "εὐθὺς δὲ ἀποστελεῖ αὐτούς", None, ["Und er wird sie gleich zurückschicken"],
  "Meist wird der Satz als Zusage verstanden, der Besitzer werde die Tiere sogleich herausgeben; andere beziehen ihn auf Jesus, der sie zurückschicken werde (vgl. [[MRK.11.3]] mit πάλιν «wieder»). Die Übersetzung lässt das offen."),
 ("MAT.21.4", "damit erfüllt würde", "literal", "ἵνα πληρωθῇ", None, None,
  "Einheitliche Wiedergabe der matthäischen Erfüllungsformel (z. B. [[MAT.1.22]], [[MAT.2.15]])."),
 ("MAT.21.5", "Sagt der Tochter Zion", "literal", "Εἴπατε τῇ θυγατρὶ Σιών", None, None,
  "Mischzitat: Der Anfang stammt aus [[ISA.62.11]], das Folgende aus [[ZEC.9.9]]. Matthäus lässt die Worte «gerecht und ein Retter» aus [[ZEC.9.9]] weg. «Tochter Zion» ist eine bildhafte Bezeichnung für Jerusalem und seine Bewohner."),
 ("MAT.21.5", "sanftmütig", "literal", "πραῢς", None, ["demütig", "sanft", "gewaltlos"],
  "πραΰς heisst «sanft, freundlich, nicht gewalttätig»; das hebräische Wort in [[ZEC.9.9]] bedeutet eher «arm, gebeugt». Vgl. [[MAT.5.5]] und [[MAT.11.29]]."),
 ("MAT.21.5", "dem Jungen eines Lasttiers", "literal", "υἱὸν ὑποζυγίου", "dem Sohn eines Lasttiers", None,
  "υἱός «Sohn» bezeichnet hier das Jungtier. Im Hebräischen von [[ZEC.9.9]] ist dasselbe Tier in zwei parallelen Gliedern genannt; Matthäus' Erzählung spricht von zwei Tieren ([[MAT.21.7]])."),
 ("MAT.21.7", "er setzte sich darauf", "interpretive", "ἐπεκάθισεν ἐπάνω αὐτῶν", "er setzte sich auf sie", None,
  "αὐτῶν («auf sie») kann sich auf die Mäntel oder auf die Tiere beziehen; die Übersetzung lässt den Bezug wie das Griechische offen."),
 ("MAT.21.8", "Die meisten aus der Menge", "interpretive", "ὁ πλεῖστος ὄχλος", "die meiste Menge", ["eine sehr grosse Menge"],
  "πλεῖστος kann den grössten Teil oder eine sehr grosse Zahl meinen. Das Verb steht im Plural."),
 ("MAT.21.9", "Die Menschenmengen", "literal", "οἱ ὄχλοι", None, ["die Scharen", "die Leute"],
  "Matthäus gebraucht oft den Plural ὄχλοι; er ist mit «Menschenmengen» wiedergegeben, der Singular mit «Menge»."),
 ("MAT.21.9", "riefen", "adapted", "ἔκραζον", "schrien", None,
  "κράζω heisst «laut rufen, schreien»; bei den Hilferufen der Blinden steht «schreien» ([[MAT.20.30]]), bei den Huldigungsrufen «rufen» (ebenso [[MAT.21.15]])."),
 ("MAT.21.9", "Hosanna", "traditional", "Ὡσαννὰ", None, None,
  "Griechische Umschrift des hebräischen Rufs «hilf doch!» aus [[PSA.118.25]]; zur Zeit Jesu auch ein Jubel- und Huldigungsruf. Der folgende Ruf stammt aus [[PSA.118.26]]. «In den Höhen» meint Gott im Himmel."),
 ("MAT.21.10", "geriet die ganze Stadt in Aufruhr", "interpretive", "ἐσείσθη πᾶσα ἡ πόλις", "wurde die ganze Stadt erschüttert", ["geriet die ganze Stadt in Bewegung"],
  "σείω heisst «erschüttern, beben»; dasselbe Verb steht beim Erdbeben in [[MAT.27.51]] und [[MAT.28.4]]. Hier im übertragenen Sinn."),
 ("MAT.21.12", "trieb alle hinaus", "literal", "ἐξέβαλεν πάντας", None, None,
  "Bei Matthäus folgt die Tempelaktion unmittelbar auf den Einzug; in [[MRK.11.11]]–[[MRK.11.15]] erst am folgenden Tag."),
 ("MAT.21.13", "Räuberhöhle", "literal", "σπήλαιον λῃστῶν", None, None,
  "Verbindung von [[ISA.56.7]] und [[JER.7.11]]; anders als [[MRK.11.17]] ohne «für alle Völker»."),
 ("MAT.21.15", "die erstaunlichen Dinge", "adapted", "τὰ θαυμάσια", None, ["die Wunder", "die wunderbaren Taten"],
  "θαυμάσιος «erstaunlich, wunderbar» steht im Neuen Testament nur hier; gemeint sind die Heilungen ([[MAT.21.14]])."),
 ("MAT.21.15", "die Kinder", "interpretive", "τοὺς παῖδας", None, ["die Knaben", "die Jungen"],
  "παῖς ist ein Kind, oft ein Knabe; das Wort kann auch Diener bedeuten. Hier im Zusammenhang mit [[MAT.21.16]] Kinder."),
 ("MAT.21.16", "Lob", "literal", "αἶνον", None, None,
  "Wörtlich nach der Septuaginta von [[PSA.8.2]]; der hebräische Text hat dort «Macht, Bollwerk»."),
 ("MAT.21.19", "verdorrte auf der Stelle", "literal", "ἐξηράνθη παραχρῆμα", None, ["verdorrte sofort"],
  "Bei Matthäus verdorrt der Baum sofort; in [[MRK.11.20]] sehen die Jünger ihn erst am nächsten Morgen verdorrt."),
 ("MAT.21.21", "Glauben", "literal", "πίστιν", None, ["Vertrauen"],
  "Wiedergabe für den Bereich: πίστις «Glaube», πιστεύω «glauben». Die Wörter umfassen auch Vertrauen und Treue; die einheitliche Wiedergabe hält die Verbindung zu [[MAT.21.22]] und [[MAT.21.25]]–[[MAT.21.32]] (Johannes «glauben») sichtbar."),
 ("MAT.21.21", "zweifelt", "literal", "διακριθῆτε", None, ["schwankt", "unschlüssig seid"], None),
 ("MAT.21.21", "Heb dich hoch", "adapted", "Ἄρθητι καὶ βλήθητι", "Werde hochgehoben … werde geworfen", None,
  "Die griechischen Befehle stehen im Passiv; wie in [[MRK.11.23]] aktiv wiedergegeben."),
 ("MAT.21.23", "Vollmacht", "literal", "ἐξουσίᾳ", None, ["Recht", "Autorität"],
  "ἐξουσία ist die übertragene Befugnis; wie bei Markus «Vollmacht»."),
 ("MAT.21.23", "die Ältesten des Volkes", "literal", "οἱ πρεσβύτεροι τοῦ λαοῦ", None, None,
  "Die Ältesten sind Mitglieder der führenden Familien Jerusalems im Hohen Rat; die Bezeichnung ist neutral wiedergegeben."),
 ("MAT.21.25", "untereinander", "interpretive", "ἐν ἑαυτοῖς", "in sich", ["bei sich"],
  "ἐν ἑαυτοῖς kann «jeder bei sich» oder «untereinander» heissen; die Fortsetzung mit «wir» spricht für eine Beratung."),
 ("MAT.21.28", "zwei Kinder", "literal", "τέκνα δύο", None, ["zwei Söhne"],
  "τέκνον «Kind» ist hier beibehalten; die Antwort «der erste» ([[MAT.21.31]]) zeigt, dass Söhne gemeint sind."),
 ("MAT.21.29", "bereute er es", "interpretive", "μεταμεληθεὶς", "es reuend", ["besann er sich anders", "änderte er seine Meinung"],
  "μεταμέλομαι «bereuen, sich anders besinnen» ist hier wie in [[MAT.21.32]] mit «bereuen» übersetzt und so vom Leitwort μετανοέω «umkehren» ([[MAT.3.2]], [[MAT.4.17]]) unterschieden; ebenso [[MAT.27.3]]."),
 ("MAT.21.30", "Ich gehe, Herr", "adapted", "Ἐγώ, κύριε", "Ich, Herr", ["Ja, Herr"],
  "Die knappe Antwort «Ich, Herr» ist als Zusage zu verstehen; «gehe» ist ergänzt."),
 ("MAT.21.31", "das Reich Gottes", "literal", "τὴν βασιλείαν τοῦ θεοῦ", None, None,
  "Matthäus sagt sonst meist «Reich der Himmel»; «Reich Gottes» steht im SBLGNT-Text noch in [[MAT.12.28]], [[MAT.19.24]] und [[MAT.21.43]]."),
 ("MAT.21.31", "gehen euch voran", "interpretive", "προάγουσιν ὑμᾶς", None, ["kommen vor euch"],
  "Ob «vorangehen» die Angesprochenen ausschliesst oder ihnen den Weg noch offenlässt, wird verschieden verstanden; die Übersetzung bleibt wörtlich."),
 ("MAT.21.31", "die Prostituierten", "adapted", "αἱ πόρναι", None, ["die Huren", "die Dirnen"],
  "Sachliche heutige Bezeichnung; «Huren» ist im heutigen Deutsch abwertend, «Dirnen» veraltet."),
 ("MAT.21.32", "auf dem Weg der Gerechtigkeit", "literal", "ἐν ὁδῷ δικαιοσύνης", None, ["mit der Botschaft der Gerechtigkeit"],
  "Wiedergabe für den Bereich: δικαιοσύνη «Gerechtigkeit» (das Rechte vor Gott, vgl. [[MAT.3.15]]). Ob gemeint ist, dass Johannes den Weg der Gerechtigkeit lehrte oder selbst darauf ging, lässt der Text offen."),
 ("MAT.21.33", "eine Kelter", "literal", "ληνὸν", None, ["eine Weinpresse", "eine Keltergrube"],
  "ληνός ist die in den Fels gehauene Tretkelter. Die Schilderung des Weinbergs nimmt [[ISA.5.1]]–[[ISA.5.2]] auf, wo der Weinberg für Israel steht."),
 ("MAT.21.34", "Knechte", "interpretive", "δούλους", "Sklaven", ["Diener", "Boten"],
  "Im Gleichnis sind die δοῦλοι Beauftragte des Herrn; «Knechte» ist im Deutschen die eingeführte Wiedergabe und stimmt mit [[MRK.12.2]] überein. Im Spruch [[MAT.20.27]] steht «Sklave»."),
 ("MAT.21.34", "seine Früchte", "interpretive", "τοὺς καρποὺς αὐτοῦ", None, ["dessen Früchte", "ihren Ertrag"],
  "αὐτοῦ kann den Hausherrn («seine» Früchte) oder den Weinberg («dessen» Früchte) meinen."),
 ("MAT.21.37", "werden sie Achtung haben", "interpretive", "Ἐντραπήσονται", "werden sie sich scheuen", ["werden sie Respekt haben"],
  "ἐντρέπομαι heisst «sich scheuen, Respekt haben vor»; wie [[MRK.12.6]]."),
 ("MAT.21.41", "die Übeltäter übel umbringen", "adapted", "Κακοὺς κακῶς ἀπολέσει αὐτούς", "Böse wird er böse vernichten, sie", ["er wird den Bösen ein böses Ende bereiten"],
  "Wortspiel mit κακός «böse» und κακῶς «übel»; im Deutschen mit «Übeltäter … übel» nachgebildet. Bei Matthäus sprechen die Zuhörer das Urteil selbst, bei [[MRK.12.9]] Jesus."),
 ("MAT.21.42", "zum Eckstein", "interpretive", "εἰς κεφαλὴν γωνίας", "zum Haupt der Ecke", ["zum Schlussstein"],
  "Zitat aus [[PSA.118.22]]–[[PSA.118.23]] nach der Septuaginta. Gemeint ist der tragende Eckstein im Fundament oder der Schlussstein oben; «Eckstein» ist die verbreitete Wiedergabe."),
 ("MAT.21.43", "einem Volk", "interpretive", "ἔθνει", None, ["einer Nation", "einem anderen Volk"],
  "ἔθνος im Singular. Wer dieses Volk ist, sagt der Text nicht: Gedeutet wurde es auf die Gemeinde aus Juden und Nichtjuden, auf eine neue Führung für Israel oder allgemein auf alle, die die Früchte bringen. Angesprochen sind nach dem Zusammenhang die Hohepriester und Ältesten bzw. Pharisäer ([[MAT.21.23]], [[MAT.21.45]]). Eine Verwerfung des jüdischen Volkes als ganzem steht nicht im Text; die Wirkungsgeschichte solcher Deutungen ist mitzubedenken."),
 ("MAT.21.44", "wird zerschellen", "literal", "συνθλασθήσεται", None, ["wird zerschmettert werden"],
  "Das Bild erinnert an [[ISA.8.14]]–[[ISA.8.15]] und [[DAN.2.34]]–[[DAN.2.35]]; ähnlich [[LUK.20.18]]. Der Vers fehlt in einem Teil der Überlieferung (siehe Alternativen)."),
]

DEC_GSW = [
 ("MAT.20.1", "mit em Riich vo de Himel isch es wie mit eme Huusherr", "adapted", "Ὁμοία γάρ ἐστιν ἡ βασιλεία τῶν οὐρανῶν ἀνθρώπῳ οἰκοδεσπότῃ", "s Riich vo de Himel isch gliich wie en Mänsch, en Huusherr", None,
  "So seit mer s im Züritüütsch. «S Riich vo de Himel» isch di einheitlich Widergab fürs ganz Matthäusevangelium (griechisch Plural); «Mänsch, Huusherr» isch zu eim Wort zämegnoo, wie i [[MAT.21.33]]."),
 ("MAT.20.3", "ohni Arbet", "adapted", "ἀργούς", "untätig", ["wo nüüt z tue händ"],
  "ἀργός heisst «ohni Arbet, untätig»; da eher arbeitslos als fuul ([[MAT.20.7]])."),
 ("MAT.20.8", "Loon", "literal", "μισθὸν", None, None, "Schriibig wie im Vatterunser-Abschnitt ([[MAT.6.5]])."),
 ("MAT.20.11", "gmuulet", "adapted", "ἐγόγγυζον", "gmurret", ["gschumpfe", "sich beklagt"],
  "«Muule» isch s gwöhnlich Wort für lislig und unzfride reklamiere."),
 ("MAT.20.12", "gschaffet", "adapted", "ἐποίησαν", "gmacht", None, "ποιέω mit ere Ziitaagab meint d Arbetsziit."),
 ("MAT.20.13", "Fründ", "adapted", "Ἑταῖρε", None, ["Kolleg"],
  "Fründlichi, aber distanzierti Aared a öpper, wo im Unrächt isch; wie i [[MAT.22.12]] und [[MAT.26.50]]."),
 ("MAT.20.15", "isch dis Aug böös", "literal", "ὁ ὀφθαλμός σου πονηρός ἐστιν", None, ["bisch nidisch"],
  "S «böös Aug» isch e biblischi Wändig für Niid ([[DEU.15.9]], [[MAT.6.23]]); wörtlich bhalte wäg em Gägesatz zu «guet»."),
 ("MAT.20.15", "guet", "literal", "ἀγαθός", None, ["grosszügig"], "Im Gägesatz zum böös Aug: d Güeti als Grosszügigkeit."),
 ("MAT.20.19", "de Heide", "interpretive", "τοῖς ἔθνεσιν", "de Völker", ["de Nichtjude"],
  "ἔθνη heisst «Völker»; us jüdischer Sicht d Nichtjude, da d römisch Macht. I [[MAT.20.25]] «Völker»."),
 ("MAT.20.19", "wird er uferweckt", "literal", "ἐγερθήσεται", None, ["staat er uf"], "Passiv: Gott isch dä, wo handlet."),
 ("MAT.20.20", "härechoo", "literal", "προσῆλθεν", None, None, "Einheitlich fürs Matthäusevangelium: προσέρχομαι «härechoo»; ebenso [[MAT.21.14]], [[MAT.21.23]], [[MAT.21.28]], [[MAT.21.30]]."),
 ("MAT.20.20", "hät sich vor ihm nidergworfe", "interpretive", "προσκυνοῦσα", None, ["hät ihm ghuldiget", "hät en aabätet"],
  "Einheitlich fürs Matthäusevangelium: προσκυνέω vor Mänsche und vor em Jesus «sich niderwärfe», mit Gott als Empfänger «aabätte». S Wort bezeichnet s Niderfalle vor ere höchere Person oder vor Gott. D Übersetzig beschriibt d Gebärde und laat d Düütig offe."),
 ("MAT.20.22", "jetzt dänn", "adapted", "μέλλω", "bi im Begriff", ["bald"],
  "μέλλω mit Infinitiv: öppis staat unmittelbar bevor. D Mundart hät kei gwöhnlichs Futur; «jetzt dänn» seit, dass es bald passiert."),
 ("MAT.20.22", "de Bächer", "literal", "τὸ ποτήριον", None, ["de Kelch"], "Bild für s zuegmässe Gschick, oft für Liide ([[ISA.51.17]], [[MAT.26.39]])."),
 ("MAT.20.26", "So söll s nöd sii", "interpretive", "οὐχ οὕτως ἔσται", "So wird s nöd sii", ["So isch es nöd"],
  "S Futur isch als Wiisig verstande, ebenso «dä söll … sii». Zum Präsens ἐστίν lueg d Alternative."),
 ("MAT.20.27", "Sklav", "literal", "δοῦλος", None, ["Chnächt", "Diener"], "Im Spruch «Sklav» wie i [[MRK.10.44]]; im Gliichnis [[MAT.21.34]] «Chnächt»."),
 ("MAT.20.30", "häb Erbarme mit üs", "literal", "ἐλέησον ἡμᾶς", None, None, "Wie i [[MRK.10.47]]."),
 ("MAT.20.30", "Sohn vom David", "literal", "υἱὸς Δαυίδ", None, None, "Messianische Titel, bim Matthäus hüüfig ([[MAT.1.1]], [[MAT.21.9]])."),
 ("MAT.20.34", "hät Erbarme gha", "interpretive", "σπλαγχνισθεὶς", "voll Mitgfühl", ["es hät en duuret"],
  "Einheitlich fürs Matthäusevangelium: σπλαγχνίζομαι «Erbarme haa (mit)», wie [[MAT.14.14]]. σπλάγχνα sind d Iigweid als Sitz vo de Gfühl. Im Griechische isch s es anders Wort als ἐλεέω i de Bitt «häb Erbarme» ([[MAT.20.30]])."),
 ("MAT.21.4", "damit erfüllt wird", "literal", "ἵνα πληρωθῇ", None, None, "Einheitlichi Widergab vo de Erfüllungsformle bim Matthäus."),
 ("MAT.21.5", "sanftmüetig", "literal", "πραῢς", None, ["sanft", "demüetig"], "Zitat us [[ISA.62.11]] und [[ZEC.9.9]]."),
 ("MAT.21.5", "rittet", "adapted", "ἐπιβεβηκὼς", "ufgsässe", None, "S Partizip («ufgsässe uf») isch als Verb widergää."),
 ("MAT.21.9", "D Lüüt", "adapted", "οἱ ὄχλοι", "d Mängine", ["d Schare"],
  "De Plural vo «Mängi» isch ungwöhnlich; drum «d Lüüt» für οἱ ὄχλοι (ebenso [[MAT.21.11]], [[MAT.21.46]]), «d Mängi» für de Singular."),
 ("MAT.21.9", "Hosanna", "traditional", "Ὡσαννὰ", None, None, "Umschrift vom hebräische Ruef «hilf doch!» ([[PSA.118.25]]); zur Ziit vom Jesus au en Jubelruef."),
 ("MAT.21.10", "in Ufruer graate", "interpretive", "ἐσείσθη", "erschüttered worde", ["in Bewegig cho"], "σείω heisst «erschüttere, bebe»; da im übertreite Sinn."),
 ("MAT.21.16", "Muul", "literal", "στόματος", None, ["Mund"], "Im Züritüütsch s gwöhnlich Wort für de Mund."),
 ("MAT.21.21", "Glaube", "literal", "πίστιν", None, ["Vertroue"], "Widergab für de Bereich: πίστις «Glaube», πιστεύω «glaube»."),
 ("MAT.21.29", "hät s en groue", "interpretive", "μεταμεληθεὶς", None, ["hät er sich anders bsunne"],
  "μεταμέλομαι «bereue» isch mit «groue» widergää (ebenso [[MAT.21.32]]) und so vom Leitwort μετανοέω «umchehre» underscheide."),
 ("MAT.21.30", "Ich gaa, Herr", "adapted", "Ἐγώ, κύριε", "Ich, Herr", None, "Di churz Antwort isch e Zuesag; «gaa» isch ergänzt."),
 ("MAT.21.31", "d Prostituierte", "adapted", "αἱ πόρναι", None, ["d Hure"], "Sachlichi Bezeichnig; «Hure» tönt hüt abwärtend."),
 ("MAT.21.31", "Riich vo Gott", "literal", "τὴν βασιλείαν τοῦ θεοῦ", None, None, "Bim Matthäus selte statt «Riich vo de Himel»; ebenso [[MAT.21.43]]."),
 ("MAT.21.32", "Grächtigkeit", "literal", "δικαιοσύνης", None, None, "Widergab für de Bereich: δικαιοσύνη «Grächtigkeit»."),
 ("MAT.21.33", "Trotte", "literal", "ληνὸν", None, ["Weipress"], "D Trotte isch d Wiipress; da e i de Fels ghaueni Trättchälter. Aaklang a [[ISA.5.1]]–[[ISA.5.2]]."),
 ("MAT.21.34", "Chnächt", "interpretive", "δούλους", "Sklave", ["Diener"], "Im Gliichnis di iigfüert Widergab, wie i [[MRK.12.2]]."),
 ("MAT.21.41", "di Bööse böös umbringe", "adapted", "Κακοὺς κακῶς ἀπολέσει αὐτούς", None, None, "S Wortspiil vo κακός und κακῶς isch mit «böös» nachebildet."),
 ("MAT.21.42", "zum Eckstei", "interpretive", "εἰς κεφαλὴν γωνίας", "zum Chopf vo de Egge", ["zum Schlussstei"], "Zitat us [[PSA.118.22]]–[[PSA.118.23]]."),
 ("MAT.21.43", "eme Volk", "interpretive", "ἔθνει", None, ["ere Nation"],
  "Wer das Volk isch, seit de Text nöd; d Düütige gönd usenand (d Gmeind us Jude und Nichtjude, e neui Füerig für Israel, alli, wo Frücht bringed). E Verwerfig vom jüdische Volk als ganzem staat nöd im Text."),
 ("MAT.21.44", "verschmätteret", "adapted", "συνθλασθήσεται", "zerschlage", None, "Aaklang a [[ISA.8.14]]–[[ISA.8.15]] und [[DAN.2.34]]–[[DAN.2.35]]. De Vers fehlt i eme Teil vo de Überliferig (lueg d Alternative)."),
]

AUTO = "Laut der automatischen Zuordnung"
AUTO_G = "Nach de automatische Zueornig"
ALTS = [
 ("VAR-SBLGNTAPP-MAT-020-006-02:R2", "MAT.20.6", "andere, die dastanden", "andere, die untätig dastanden", "anderi umestaa", "anderi ohni Arbet umestaa", "gering",
  "Mit dem Zusatz steht «untätig» schon in der Erzählung, nicht erst in der Frage des Hausherrn.",
  "Mit em Zuesatz staat «ohni Arbet» scho i de Erzählig, nöd erscht i de Frag vom Huusherr.",
  {"R1": [("ἑστῶτας", "dastehen", "WH, Treg, NA28")], "R2": [("ἑστῶτας ἀργούς", "untätig dastehen", "RP")]},
  {"R1": [("ἑστῶτας", "umestaa", "WH, Treg, NA28")], "R2": [("ἑστῶτας ἀργούς", "ohni Arbet umestaa", "RP")]},
  ["Der Zusatz kann aus [[MAT.20.3]] übernommen sein; ebenso kann das Wort als überflüssig weggefallen sein, weil es in der Frage gleich folgt.",
   AUTO + " lesen 01, 03 und 05 ohne Zusatz, 032 und 04 mit ihm; 𝔓45 ist hier nicht erhalten."],
  ["De Zuesatz cha us [[MAT.20.3]] übernoo sii; s Wort cha aber au wäggfalle sii, wil s i de Frag grad nachechunnt.",
   AUTO_G + " läsed 01, 03 und 05 ohni Zuesatz, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-020-007-01:R2", "MAT.20.7", "in den Weinberg!", "in den Weinberg, und was recht ist, werdet ihr empfangen!",
  "in Wiibärg!", "in Wiibärg, und was rächt isch, überchömed ir!", "gering",
  "Mit dem Zusatz erhalten auch die Letzten eine Lohnzusage wie die in [[MAT.20.4]].",
  "Mit em Zuesatz überchömed au di Letschte e Loonzuesag wie die i [[MAT.20.4]].",
  {"R1": [("ἀμπελῶνα", "Weinberg", "WH, Treg, NA28")], "R2": [("ἀμπελῶνα καὶ ὃ ἐὰν ᾖ δίκαιον λήψεσθε", "Weinberg, und was recht ist, werdet ihr empfangen", "RP")]},
  {"R1": [("ἀμπελῶνα", "Wiibärg", "WH, Treg, NA28")], "R2": [("ἀμπελῶνα καὶ ὃ ἐὰν ᾖ δίκαιον λήψεσθε", "Wiibärg, und was rächt isch, überchömed ir", "RP")]},
  ["Der Zusatz gleicht an [[MAT.20.4]] an; umgekehrt kann er beim Abschreiben ausgefallen sein.",
   AUTO + " lesen 01, 03 und 05 ohne Zusatz, 032 und 04 mit ihm; 𝔓45 ist hier nicht erhalten."],
  ["De Zuesatz gliicht a [[MAT.20.4]] aa; umgekeert cha er bim Abschriibe usgfalle sii.",
   AUTO_G + " läsed 01, 03 und 05 ohni Zuesatz, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-020-016-01:R2", "MAT.20.16", "die Ersten Letzte.", "die Ersten Letzte. Denn viele sind berufen, wenige aber auserwählt.",
  "di Erschte Letschti.", "di Erschte Letschti. Dänn vili sind berüeft, aber wenig userwählt.", "mittel",
  "Der Zusatz gibt dem Gleichnis einen zweiten Schlusssatz, der wörtlich in [[MAT.22.14]] steht.",
  "De Zuesatz git em Gliichnis en zweite Schlusssatz, wo wörtlich i [[MAT.22.14]] staat.",
  {"R1": [("ἔσχατοι", "Letzte", "WH, NA28")], "R2": [("ἔσχατοι· πολλοὶ γάρ εἰσιν κλητοί, ὀλίγοι δὲ ἐκλεκτοί", "Letzte. Denn viele sind berufen, wenige aber auserwählt", "Treg, RP")]},
  {"R1": [("ἔσχατοι", "Letschti", "WH, NA28")], "R2": [("ἔσχατοι· πολλοὶ γάρ εἰσιν κλητοί, ὀλίγοι δὲ ἐκλεκτοί", "Letschti. Dänn vili sind berüeft, aber wenig userwählt", "Treg, RP")]},
  ["Der Satz kann aus [[MAT.22.14]] übernommen sein, als passender Abschluss. Ebenso kann er durch Augensprung ausgefallen sein, weil vorher und am Ende des Zusatzes ähnlich endende Wörter stehen (ἔσχατοι … ἐκλεκτοί).",
   AUTO + " lesen 01 und 03 ohne Zusatz, 032, 04 und 05 mit ihm; 𝔓45 ist hier nicht erhalten."],
  ["De Satz cha us [[MAT.22.14]] übernoo sii. Er cha aber au dur en Augesprung usgfalle sii, wil vorher und am Änd vom Zuesatz ähnlich ändendi Wort stönd.",
   AUTO_G + " läsed 01 und 03 ohni Zuesatz, 032, 04 und 05 mit."]),
 ("VAR-SBLGNTAPP-MAT-020-017-01:R2", "MAT.20.17", "Und als Jesus nach Jerusalem hinaufzog", "Als Jesus aber nach Jerusalem hinaufziehen wollte",
  "Und wo de Jesus uf Jerusalem ufe gange isch", "Wo de Jesus aber uf Jerusalem ufe hät wele", "gering",
  "Nach dieser Lesart spricht Jesus vor dem Aufbruch, nicht unterwegs.",
  "Nach dere Läsart redt de Jesus vor em Ufbruch, nöd underwägs.",
  {"R1": [("Καὶ ἀναβαίνων ὁ", "Und als (Jesus) hinaufzog", "Treg, NA28, RP")], "R2": [("Μέλλων δὲ ἀναβαίνειν", "Als (Jesus) aber hinaufziehen wollte", "WH")]},
  {"R1": [("Καὶ ἀναβαίνων ὁ", "Und wo (de Jesus) ufe gange isch", "Treg, NA28, RP")], "R2": [("Μέλλων δὲ ἀναβαίνειν", "Wo (de Jesus) aber ufe hät wele", "WH")]},
  ["μέλλων kann die ungewöhnlichere, ursprüngliche Form sein, die dem folgenden «auf dem Weg» zu widersprechen scheint; ebenso kann sie eine stilistische Abwandlung sein.",
   AUTO + " liest 03 μέλλων, 01, 032, 04 und 05 ἀναβαίνων; 𝔓45 ist hier nicht erhalten."],
  ["μέλλων cha di ungwöhnlicheri, ursprünglichi Form sii; si cha aber au e stilistischi Abwandlig sii.",
   AUTO_G + " list 03 μέλλων, 01, 032, 04 und 05 ἀναβαίνων."]),
 ("VAR-SBLGNTAPP-MAT-020-017-02:R2", "MAT.20.17", "die zwölf Jünger", "die Zwölf", "di zwölf Jünger", "di Zwölf", "gering",
  "Ohne μαθητάς steht «die Zwölf» als feste Bezeichnung des Kreises.",
  "Ohni μαθητάς staat «di Zwölf» als feschti Bezeichnig vom Chreis.",
  {"R1": [("τοὺς δώδεκα μαθητὰς", "die zwölf Jünger", "WH, NA28, RP")], "R2": [("τοὺς δώδεκα", "die Zwölf", "Treg")]},
  {"R1": [("τοὺς δώδεκα μαθητὰς", "di zwölf Jünger", "WH, NA28, RP")], "R2": [("τοὺς δώδεκα", "di Zwölf", "Treg")]},
  ["«Jünger» kann zur Verdeutlichung ergänzt oder als selbstverständlich weggelassen worden sein (vgl. [[MAT.26.20]]).",
   AUTO + " lesen 01 und 05 ohne μαθητάς (die Zahl dort als Zahlzeichen geschrieben), 03, 032 und 04 mit; 𝔓45 ist hier nicht erhalten."],
  ["«Jünger» cha zur Verdüütlichung ergänzt oder als sälbverständlich wäggloo worde sii.",
   AUTO_G + " läsed 01 und 05 ohni μαθητάς (d Zahl als Zahlzeiche gschribe), 03, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-020-019-01:R2", "MAT.20.19", "wird er auferweckt werden", "wird er auferstehen", "wird er uferweckt", "wird er uferstaa", "gering",
  "Statt des Passivs (Gott weckt ihn auf) steht das aktive «auferstehen» wie in [[MRK.10.34]].",
  "Statt em Passiv (Gott weckt en uf) staat s aktiv «uferstaa» wie i [[MRK.10.34]].",
  {"R1": [("ἐγερθήσεται", "wird auferweckt werden", "WH, Treg, NA28")], "R2": [("ἀναστήσεται", "wird auferstehen", "RP")]},
  {"R1": [("ἐγερθήσεται", "wird uferweckt", "WH, Treg, NA28")], "R2": [("ἀναστήσεται", "wird uferstaa", "RP")]},
  ["ἀναστήσεται kann an [[MRK.10.34]] und [[LUK.18.33]] angeglichen sein; ἐγερθήσεται kann umgekehrt an die früheren Ankündigungen bei Matthäus ([[MAT.16.21]], [[MAT.17.23]]) angeglichen sein.",
   AUTO + " lesen 01 und 04 ἐγερθήσεται, 03, 032 und 05 ἀναστήσεται; 𝔓45 ist hier nicht erhalten."],
  ["ἀναστήσεται cha a [[MRK.10.34]] und [[LUK.18.33]] aaglichen sii; ἐγερθήσεται umgekeert a di früenere Aakündige bim Matthäus ([[MAT.16.21]], [[MAT.17.23]]).",
   AUTO_G + " läsed 01 und 04 ἐγερθήσεται, 03, 032 und 05 ἀναστήσεται."]),
 ("VAR-SBLGNTAPP-MAT-020-022-01:R2", "MAT.20.22", "den ich trinken werde?", "den ich trinken werde, oder mit der Taufe getauft werden, mit der ich getauft werde?",
  "wo ich jetzt dänn trinke?", "wo ich jetzt dänn trinke, oder mit de Taufi tauft wärde, mit dere ich tauft wirde?", "mittel",
  "Der Zusatz stellt neben das Bild des Bechers das der Taufe, wie in [[MRK.10.38]].",
  "De Zuesatz stellt näbe s Bild vom Bächer das vo de Taufi, wie i [[MRK.10.38]].",
  {"R1": [("πίνειν", "trinken werde", "WH, Treg, NA28")], "R2": [("πίνειν ἢ τὸ βάπτισμα ὃ ἐγὼ βαπτίζομαι βαπτισθῆναι", "trinken werde, oder mit der Taufe getauft werden, mit der ich getauft werde", "RP")]},
  {"R1": [("πίνειν", "trinke", "WH, Treg, NA28")], "R2": [("πίνειν ἢ τὸ βάπτισμα ὃ ἐγὼ βαπτίζομαι βαπτισθῆναι", "trinke, oder mit de Taufi tauft wärde …", "RP")]},
  ["Der Zusatz kann aus [[MRK.10.38]] übernommen sein; ebenso kann Matthäus ihn gehabt und ein Abschreiber ihn ausgelassen haben.",
   AUTO + " lesen 01, 03 und 05 ohne Zusatz, 032 und 04 mit ihm; 𝔓45 ist hier nicht erhalten."],
  ["De Zuesatz cha us [[MRK.10.38]] übernoo sii; oder er isch bim Abschriibe usgfalle.",
   AUTO_G + " läsed 01, 03 und 05 ohni Zuesatz, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-020-023-02:R2", "MAT.20.23", "Meinen Becher werdet ihr zwar trinken;", "Meinen Becher werdet ihr zwar trinken, und mit der Taufe, mit der ich getauft werde, werdet ihr getauft werden;",
  "Min Bächer wärded ir scho trinke;", "Min Bächer wärded ir scho trinke, und mit de Taufi, mit dere ich tauft wirde, wärded ir tauft wärde;", "mittel",
  "Gehört mit dem Zusatz in [[MAT.20.22]] zusammen; vgl. [[MRK.10.39]].",
  "Ghört mit em Zuesatz i [[MAT.20.22]] zäme; vgl. [[MRK.10.39]].",
  {"R1": [("πίεσθε", "werdet ihr trinken", "WH, Treg, NA28")], "R2": [("πίεσθε καὶ τὸ βάπτισμα ὃ ἐγὼ βαπτίζομαι βαπτισθήσεσθε", "werdet ihr trinken, und mit der Taufe, mit der ich getauft werde, werdet ihr getauft werden", "RP")]},
  {"R1": [("πίεσθε", "wärded ir trinke", "WH, Treg, NA28")], "R2": [("πίεσθε καὶ τὸ βάπτισμα ὃ ἐγὼ βαπτίζομαι βαπτισθήσεσθε", "wärded ir trinke, und mit de Taufi … tauft wärde", "RP")]},
  ["Wie in [[MAT.20.22]]: Angleichung an Markus oder Auslassung.",
   AUTO + " lesen 01, 03 und 05 ohne Zusatz, 032 und 04 mit ihm; 𝔓45 ist hier nicht erhalten."],
  ["Wie i [[MAT.20.22]]: Aaglichig a de Markus oder Uslassig.",
   AUTO_G + " läsed 01, 03 und 05 ohni Zuesatz, 032 und 04 mit."]),
 ("VAR-SBLGNTAPP-MAT-020-026-01:R3", "MAT.20.26", "So soll es nicht sein unter euch", "So ist es nicht unter euch",
  "So söll s nöd sii under eu", "So isch es nöd under eu", "gering",
  "Mit dem Präsens beschreibt Jesus, wie es unter den Jüngern ist, statt eine Weisung zu geben; so auch [[MRK.10.43]].",
  "Mit em Präsens beschriibt de Jesus, wie s under de Jünger isch, statt e Wiisig z gää; so au [[MRK.10.43]].",
  {"R1": [("ἔσται", "soll sein (wörtlich: wird sein)", "NA28")], "R2": [("δέ ἔσται", "aber soll sein", "RP")], "R3": [("ἐστὶν", "ist", "WH, Treg")]},
  {"R1": [("ἔσται", "söll sii", "NA28")], "R2": [("δέ ἔσται", "aber söll sii", "RP")], "R3": [("ἐστὶν", "isch", "WH, Treg")]},
  ["Das Präsens kann an [[MRK.10.43]] angeglichen sein; das Futur kann umgekehrt an das folgende ἔσται («der soll … sein») angeglichen sein.",
   AUTO + " lesen 01 (Schreibung εστε), 032 und 𝔓45 ἔσται, 04 δὲ ἔσται, 03 und 05 ἐστίν."],
  ["S Präsens cha a [[MRK.10.43]] aaglichen sii; s Futur umgekeert as folgend ἔσται.",
   AUTO_G + " läsed 01, 032 und 𝔓45 ἔσται, 04 δὲ ἔσται, 03 und 05 ἐστίν."]),
 ("VAR-SBLGNTAPP-MAT-021-004-01:R2", "MAT.21.4", "Das aber ist geschehen", "Das alles aber ist geschehen", "Das isch aber gscheh", "Das alles isch aber gscheh", "gering",
  "Mit «alles» bezieht sich die Formel auf das ganze Geschehen.", "Mit «alles» bezieht sich d Formle uf s ganz Gscheh.",
  {"R1": [("Τοῦτο δὲ γέγονεν", "Das aber ist geschehen", "WH, Treg, NA28")], "R2": [("Τοῦτο δὲ ὅλον γέγονεν", "Das alles aber ist geschehen", "RP")]},
  {"R1": [("Τοῦτο δὲ γέγονεν", "Das isch aber gscheh", "WH, Treg, NA28")], "R2": [("Τοῦτο δὲ ὅλον γέγονεν", "Das alles isch aber gscheh", "RP")]},
  ["ὅλον kann an die gleichlautende Formel in [[MAT.1.22]] und [[MAT.26.56]] angeglichen sein; ebenso kann es ausgefallen sein.",
   AUTO + " lesen 01, 04 und 05 ohne ὅλον, 03 und 032 mit; 𝔓45 ist hier nicht erhalten."],
  ["ὅλον cha a di gliich Formle i [[MAT.1.22]] und [[MAT.26.56]] aaglichen sii; oder es isch usgfalle.",
   AUTO_G + " läsed 01, 04 und 05 ohni ὅλον, 03 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-021-012-02:R2", "MAT.21.12", "in den Tempel hinein", "in den Tempel Gottes hinein", "in Tämpel ine gange", "in Tämpel vo Gott ine gange", "gering",
  "Der Zusatz betont, wem der Tempel gehört.", "De Zuesatz betont, wäm de Tämpel ghört.",
  {"R1": [("ἱερόν", "Tempel", "WH, Treg, NA28")], "R2": [("ἱερὸν τοῦ θεοῦ", "Tempel Gottes", "RP")]},
  {"R1": [("ἱερόν", "Tämpel", "WH, Treg, NA28")], "R2": [("ἱερὸν τοῦ θεοῦ", "Tämpel vo Gott", "RP")]},
  ["Der Zusatz kann eine fromme Verdeutlichung sein; die Wendung ist im Neuen Testament sonst selten. Ebenso kann er beim Abschreiben ausgefallen sein.",
   AUTO + " lesen 01 und 03 ohne Zusatz, 032, 04 und 05 mit ihm; 𝔓45 ist hier nicht erhalten."],
  ["De Zuesatz cha e frommi Verdüütlichung sii; oder er isch bim Abschriibe usgfalle.",
   AUTO_G + " läsed 01 und 03 ohni Zuesatz, 032, 04 und 05 mit."]),
 ("VAR-SBLGNTAPP-MAT-021-013-01:R2", "MAT.21.13", "Ihr aber macht es zu einer Räuberhöhle.", "Ihr aber habt es zu einer Räuberhöhle gemacht.",
  "Ir aber mached e Röiberhöli drus.", "Ir aber händ e Röiberhöli drus gmacht.", "gering",
  "Statt des Präsens (was sie gerade tun) steht das Ergebnis.", "Statt em Präsens (was si grad mached) staat s Ergebnis.",
  {"R1": [("ποιεῖτε", "macht", "WH, Treg, NA28")], "R2": [("ἐποιήσατε", "habt gemacht", "RP")]},
  {"R1": [("ποιεῖτε", "mached", "WH, Treg, NA28")], "R2": [("ἐποιήσατε", "händ gmacht", "RP")]},
  ["Der Aorist kann an [[MRK.11.17]] und [[LUK.19.46]] angeglichen sein; ebenso kann das Präsens eine Angleichung an die Gegenwart der Szene sein.",
   AUTO + " lesen 01, 03 und 𝔓45 ποιεῖτε, 032, 04 und 05 ἐποιήσατε."],
  ["De Aorist cha a [[MRK.11.17]] und [[LUK.19.46]] aaglichen sii; s Präsens umgekeert a d Szene.",
   AUTO_G + " läsed 01, 03 und 𝔓45 ποιεῖτε, 032, 04 und 05 ἐποιήσατε."]),
 ("VAR-SBLGNTAPP-MAT-021-028-02:R2", "MAT.21.28", "im Weinberg!", "in meinem Weinberg!", "im Wiibärg!", "i mim Wiibärg!", "gering",
  "Mit «meinem» spricht der Vater ausdrücklich von seinem Weinberg.", "Mit «mim» redt de Vatter usdrücklich vo sim Wiibärg.",
  {"R1": [("ἀμπελῶνι", "Weinberg", "WH, Treg, NA28")], "R2": [("ἀμπελῶνί μου", "meinem Weinberg", "RP")]},
  {"R1": [("ἀμπελῶνι", "Wiibärg", "WH, Treg, NA28")], "R2": [("ἀμπελῶνί μου", "mim Wiibärg", "RP")]},
  ["μου kann zur Verdeutlichung ergänzt oder als selbstverständlich weggelassen worden sein.",
   AUTO + " lesen 01 und 04 ohne μου, 03 und 032 mit; 05 hat nach der CNTR-Transkription εἰς τὸν ἀμπελῶνα ohne μου (der Zuordnung nach bei R1); 𝔓45 ist hier nicht erhalten."],
  ["μου cha zur Verdüütlichung ergänzt oder wäggloo worde sii.",
   AUTO_G + " läsed 01 und 04 ohni μου, 03 und 032 mit; 05 hät nach de CNTR-Transkription εἰς τὸν ἀμπελῶνα ohni μου."]),
 ("VAR-SBLGNTAPP-MAT-021-029-01:R2", "MAT.21.29", "‹Ich will nicht.› Später aber bereute er es, und er ging hin.", "‹Ich gehe, Herr!› Und er ging nicht hin.",
  "‹Ich wott nöd.› Spöter aber hät s en groue, und er isch gange.", "‹Ich gaa, Herr!› Und er isch nöd gange.", "erheblich",
  "In dieser Fassung (WH) sagt der erste Sohn zu und geht nicht, der zweite lehnt ab und geht später ([[MAT.21.30]]); die Antwort lautet dann «der letzte» ([[MAT.21.31]]). Die Aussage des Gleichnisses bleibt gleich, nur die Reihenfolge der Söhne ist vertauscht. Die drei Alternativen zu [[MAT.21.29]]–[[MAT.21.31]] gehören zusammen.",
  "I dere Fassig (WH) seit de erscht Sohn zue und gaat nöd, de zweit seit nei und gaat spöter ([[MAT.21.30]]); d Antwort heisst dänn «de letscht» ([[MAT.21.31]]). D Ussag vom Gliichnis bliibt gliich, nu d Reihefolg vo de Söhn isch vertuuschet.",
  {"R1": [("Οὐ θέλω, ὕστερον δὲ μεταμεληθεὶς", "Ich will nicht. Später aber bereute er es", "Treg, NA28, RP")], "R2": [("Ἐγώ, κύριε, καὶ οὐκ", "Ich (gehe), Herr, und (ging) nicht", "WH")]},
  {"R1": [("Οὐ θέλω, ὕστερον δὲ μεταμεληθεὶς", "Ich wott nöd. Spöter aber hät s en groue", "Treg, NA28, RP")], "R2": [("Ἐγώ, κύριε, καὶ οὐκ", "Ich (gaa), Herr, und (isch) nöd", "WH")]},
  ["Die Reihenfolge kann vertauscht worden sein, weil man die Söhne heilsgeschichtlich deutete: Wer zuerst Ja sagt und nicht handelt, erschien manchen als Bild für die führenden Kreise, wer zuerst Nein sagt und dann geht, als Bild für Zöllner und Sünder oder die Völker; je nach Deutung lag die eine oder die andere Reihenfolge nahe. Andere halten die Fassung mit dem Ja-Sager an erster Stelle für ursprünglich und die verbreitete Fassung für eine Glättung.",
   AUTO + " lesen 01, 032, 04 und 05 wie der SBLGNT, 03 die vertauschte Fassung; 𝔓45 ist hier nicht erhalten."],
  ["D Reihefolg cha vertuuschet worde sii, wil mer d Söhn heilsgschichtlich düütet hät; je nach Düütig isch di eint oder di ander Reihefolg nöch gläge. Anderi halted d Fassig mit em Ja-Säger zerscht für ursprünglich.",
   AUTO_G + " läsed 01, 032, 04 und 05 wie de SBLGNT, 03 di vertuuschet Fassig."]),
 ("VAR-SBLGNTAPP-MAT-021-030-03:R2", "MAT.21.30", "‹Ich gehe, Herr!› Und er ging nicht hin.", "‹Ich will nicht.› Später bereute er es und ging hin.",
  "‹Ich gaa, Herr!› Und er isch nöd gange.", "‹Ich wott nöd.› Spöter hät s en groue, und er isch gange.", "erheblich",
  "Gegenstück zu [[MAT.21.29]] in der Fassung WH.", "Gägestuck zu [[MAT.21.29]] i de Fassig WH.",
  {"R1": [("Ἐγώ, κύριε, καὶ οὐκ", "Ich (gehe), Herr, und nicht", "Treg, NA28, RP")], "R2": [("Οὐ θέλω, ὕστερον μεταμεληθεὶς", "Ich will nicht; später bereute er es", "WH")]},
  {"R1": [("Ἐγώ, κύριε, καὶ οὐκ", "Ich (gaa), Herr, und nöd", "Treg, NA28, RP")], "R2": [("Οὐ θέλω, ὕστερον μεταμεληθεὶς", "Ich wott nöd; spöter hät s en groue", "WH")]},
  ["Siehe [[MAT.21.29]].",
   AUTO + " lesen 01, 032 und 04 wie der SBLGNT, 03 die vertauschte Fassung. 05 hat nach der CNTR-Transkription ἐγώ, κύριε, ὑπάγω («Ich gehe hin, Herr») und καὶ οὐκ ἀπῆλθεν, also den Sinn des SBLGNT mit einem zusätzlichen Verb (der Zuordnung nach «andere Lesart»); 𝔓45 ist hier nicht erhalten."],
  ["Lueg [[MAT.21.29]].",
   AUTO_G + " läsed 01, 032 und 04 wie de SBLGNT, 03 di vertuuschet Fassig; 05 hät nach de CNTR-Transkription zuesätzlich ὑπάγω («ich gaa»)."]),
 ("VAR-SBLGNTAPP-MAT-021-031-02:R2", "MAT.21.31", "«Der erste.»", "«Der letzte.»", "«De erscht.»", "«De letscht.»", "erheblich",
  "Zur vertauschten Reihenfolge ([[MAT.21.29]]–[[MAT.21.30]] nach WH) gehört die Antwort «der letzte», die dann denselben Sohn meint. Mit der Reihenfolge des SBLGNT nennt «der letzte» dagegen den Sohn, der zusagt und nicht geht.",
  "Zur vertuuschete Reihefolg ([[MAT.21.29]]–[[MAT.21.30]] nach WH) ghört d Antwort «de letscht», wo dänn de gliich Sohn meint. Mit de Reihefolg vom SBLGNT nännt «de letscht» dä, wo zueseit und nöd gaat.",
  {"R1": [("πρῶτος", "der erste", "NA28, RP")], "R2": [("ὕστερος", "der letzte", "WH, Treg")]},
  {"R1": [("πρῶτος", "de erscht", "NA28, RP")], "R2": [("ὕστερος", "de letscht", "WH, Treg")]},
  ["Die Antwort hängt an der Reihenfolge der Söhne (siehe [[MAT.21.29]]). Die Verbindung von SBLGNT-Reihenfolge und «der letzte», wie sie 05 nach der Transkription hat, wird teils als bewusst widersinnige Antwort der Gegner verstanden, teils als Mischung zweier Textformen.",
   AUTO + " lesen 01, 032 und 04 πρῶτος, 03 ὕστερος. 05 hat nach der CNTR-Transkription ὁ ἔσχατος («der letzte») bei der Reihenfolge des SBLGNT (der Zuordnung nach «andere Lesart»); 𝔓45 ist hier nicht erhalten."],
  ["D Antwort hanget a de Reihefolg vo de Söhn (lueg [[MAT.21.29]]). D Verbindig vo de SBLGNT-Reihefolg mit «de letscht», wie si 05 nach de Transkription hät, wird teils als absichtlich widersinnigi Antwort vo de Gägner verstande, teils als Mischig vo zwei Textforme.",
   AUTO_G + " läsed 01, 032 und 04 πρῶτος, 03 ὕστερος; 05 nach de CNTR-Transkription ὁ ἔσχατος bi de Reihefolg vom SBLGNT."]),
 ("VAR-SBLGNTAPP-MAT-021-032-02:R2", "MAT.21.32", "nicht einmal danach bereut", "danach nicht bereut",
  "nöd emal spöter groue", "spöter nöd groue", "gering",
  "Ohne «nicht einmal» fehlt die Steigerung gegenüber den Zöllnern und Prostituierten.",
  "Ohni «nöd emal» fehlt d Steigerig gägenüber de Zöllner und Prostituierte.",
  {"R1": [("οὐδὲ", "nicht einmal", "WH, Treg, NA28")], "R2": [("οὐ", "nicht", "RP")]},
  {"R1": [("οὐδὲ", "nöd emal", "WH, Treg, NA28")], "R2": [("οὐ", "nöd", "RP")]},
  ["οὐδέ kann zur Verstärkung gesetzt oder zu οὐ vereinfacht worden sein.",
   AUTO + " liest 03 οὐδέ, 01, 032 und 04 οὐ. 05 hat nach der CNTR-Transkription keine Verneinung («ihr habt es später bereut»; der Zuordnung nach «andere Lesart»); 𝔓45 ist hier nicht erhalten."],
  ["οὐδέ cha zur Verstärkig gsetzt oder zu οὐ vereifacht worde sii.",
   AUTO_G + " list 03 οὐδέ, 01, 032 und 04 οὐ; 05 hät nach de CNTR-Transkription kei Verneinig."]),
 ("VAR-SBLGNTAPP-MAT-021-038-01:R2", "MAT.21.38", "sein Erbe bekommen", "sein Erbe in Besitz nehmen", "überchömed sis Erb", "nämed sis Erb in Bsitz", "gering",
  "κατάσχωμεν betont die Besitzergreifung.", "κατάσχωμεν betont, dass si s Erb a sich riissed.",
  {"R1": [("σχῶμεν", "lasst uns bekommen", "WH, Treg, NA28")], "R2": [("κατάσχωμεν", "lasst uns in Besitz nehmen", "RP")]},
  {"R1": [("σχῶμεν", "überchömed", "WH, Treg, NA28")], "R2": [("κατάσχωμεν", "nämed in Bsitz", "RP")]},
  ["Das verstärkte Verb kann eine Verdeutlichung sein; ebenso kann die Vorsilbe ausgefallen sein.",
   AUTO + " lesen 01, 03 und 05 σχῶμεν, 032 und 04 κατάσχωμεν; 𝔓45 ist hier nicht erhalten."],
  ["S verstärkt Verb cha e Verdüütlichung sii; oder d Vorsilbe isch usgfalle.",
   AUTO_G + " läsed 01, 03 und 05 σχῶμεν, 032 und 04 κατάσχωμεν."]),
 ("VAR-SBLGNTAPP-MAT-021-044-01:R2", "MAT.21.44", "Und wer auf diesen Stein fällt, wird zerschellen; auf wen er aber fällt, den wird er zermalmen.", "(Vers fehlt)",
  "Und wer uf dä Stei gheit, wird verschmätteret; uf wän er aber gheit, dä zermalmt er.", "(Vers fehlt)", "mittel",
  "Ohne den Vers endet die Rede mit dem Wort vom Reich, das einem Volk gegeben wird ([[MAT.21.43]]). Die erfassten Ausgaben haben den Vers alle; nur WH am Rand verzeichnet die Auslassung, WH setzt ihn in Klammern. Der SBLGNT markiert ihn mit einem Variantenzeichen.",
  "Ohni de Vers hört d Red mit em Wort vom Riich uf, wo eme Volk gää wird ([[MAT.21.43]]). Alli erfasste Usgabe händ de Vers; nu WH am Rand verzeichnet d Uslassig.",
  {"R1": [("Καὶ ὁ πεσὼν … αὐτόν", "Und wer auf diesen Stein fällt … zermalmen", "WH, Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH am Rand")]},
  {"R1": [("Καὶ ὁ πεσὼν … αὐτόν", "Und wer uf dä Stei gheit … zermalmt er", "WH, Treg, NA28, RP")], "R2": [("–", "(fehlt)", "WH am Rand")]},
  ["Der Vers kann aus [[LUK.20.18]] übernommen sein, wo ein ähnliches Wort steht; dann wäre er spät eingefügt. Ebenso kann er durch Augensprung ausgefallen sein, weil [[MAT.21.43]] und [[MAT.21.44]] auf ähnliche Wörter enden (αὐτῆς … αὐτόν), oder weil er nach [[MAT.21.43]] fehl am Platz wirkte.",
   AUTO + " haben 01, 03, 032 und 04 den Vers (01 in der Erstschrift ohne einleitendes καί). Für 05 und 𝔓45 führt die Zuordnung «nicht erhalten», weil die Transkription für diesen Vers keinen Text enthält; ob der Vers in 05 fehlt oder die Stelle nicht erhalten ist, lässt sich daraus nicht entscheiden."],
  ["De Vers cha us [[LUK.20.18]] übernoo sii; oder er isch dur en Augesprung usgfalle, wil [[MAT.21.43]] und [[MAT.21.44]] uf ähnlichi Wort ändet, oder wil er nach [[MAT.21.43]] fehl am Platz gwürkt hät.",
   AUTO_G + " händ 01, 03, 032 und 04 de Vers. Für 05 und 𝔓45 füert d Zueornig «nöd erhalte», wil d Transkription für dä Vers kein Text hät; öb de Vers i 05 fehlt oder d Stell nöd erhalte isch, cha mer drus nöd entscheide."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-020-001-034", "MAT.20.1-MAT.20.34", "section", "Die Arbeiter im Weinberg, der Weg nach Jerusalem und zwei Blinde bei Jericho",
  ["TU-MAT-020-001-016", "TU-MAT-020-017-019", "TU-MAT-020-020-028", "TU-MAT-020-029-034"],
  "Jesus erzählt vom Hausherrn, der zu verschiedenen Stunden Arbeiter für seinen Weinberg anwirbt und am Abend allen denselben Lohn, einen Denar, auszahlen lässt; den Murrenden hält er seine Güte entgegen: So werden die Letzten Erste sein und die Ersten Letzte. Auf dem Weg nach Jerusalem kündigt Jesus den Zwölf an, der Menschensohn werde ausgeliefert, zum Tod verurteilt und gekreuzigt und am dritten Tag auferweckt werden. Die Mutter der Söhne des Zebedäus bittet, ihre Söhne möchten in seinem Reich zu seiner Rechten und Linken sitzen; Jesus antwortet, sie würden seinen Becher trinken, doch diese Plätze zu vergeben stehe nicht ihm zu. Den empörten Zehn sagt er, wer gross werden wolle, solle Diener sein, so wie der Menschensohn gekommen sei, zu dienen und sein Leben als Lösegeld für viele zu geben. Beim Auszug aus Jericho rufen zwei Blinde Jesus als Sohn Davids um Erbarmen an; er berührt ihre Augen, sie sehen wieder und folgen ihm nach.", SEG),
 ("TU-MAT-020-001-016", "MAT.20.1-MAT.20.16", "parable", "Die Arbeiter im Weinberg", None,
  "Jesus vergleicht das Reich der Himmel mit einem Hausherrn, der frühmorgens Arbeiter für einen Denar am Tag in seinen Weinberg schickt und um die dritte, sechste, neunte und elfte Stunde weitere hinschickt. Am Abend lässt er durch seinen Verwalter den Lohn auszahlen, bei den Letzten angefangen: Alle erhalten einen Denar. Die Ersten, die mehr erwartet hatten, murren, weil die Letzten nur eine Stunde gearbeitet haben und ihnen gleichgestellt sind. Der Hausherr antwortet einem von ihnen, er tue ihm kein Unrecht, sie hätten sich auf einen Denar geeinigt; er wolle dem Letzten geben wie ihm. Er fragt, ob er mit dem Seinen nicht tun dürfe, was er wolle, oder ob sein Auge böse sei, weil er gütig sei. So werden die Letzten Erste sein und die Ersten Letzte.", None),
 ("TU-MAT-020-017-019", "MAT.20.17-MAT.20.19", "narrative_with_saying", "Die dritte Ankündigung von Leiden und Auferweckung", None,
  "Auf dem Weg hinauf nach Jerusalem nimmt Jesus die zwölf Jünger beiseite und kündigt an: Der Menschensohn wird den Hohepriestern und Schriftgelehrten ausgeliefert werden; sie werden ihn zum Tod verurteilen und den Heiden ausliefern, damit er verspottet, ausgepeitscht und gekreuzigt wird; am dritten Tag wird er auferweckt werden.", None),
 ("TU-MAT-020-020-028", "MAT.20.20-MAT.20.28", "dialogue", "Herrschen und Dienen", None,
  "Die Mutter der Söhne des Zebedäus tritt mit ihren Söhnen an Jesus heran, wirft sich vor ihm nieder und bittet, ihre zwei Söhne möchten in seinem Reich zu seiner Rechten und zu seiner Linken sitzen. Jesus antwortet, sie wüssten nicht, was sie bitten, und fragt, ob sie den Becher trinken können, den er trinken werde; sie antworten, sie könnten es. Er sagt, seinen Becher würden sie trinken, die Plätze zu seiner Rechten und Linken zu vergeben stehe aber nicht ihm zu; sie gehörten denen, für die sein Vater sie bereitet habe. Die Zehn empören sich über die zwei Brüder. Jesus stellt ihnen die Herrscher der Völker gegenüber, die Gewalt ausüben: Unter ihnen soll es nicht so sein; wer gross werden will, soll Diener sein, und wer der Erste sein will, Sklave, so wie der Menschensohn nicht gekommen ist, sich dienen zu lassen, sondern zu dienen und sein Leben als Lösegeld für viele zu geben.", None),
 ("TU-MAT-020-029-034", "MAT.20.29-MAT.20.34", "narrative", "Zwei Blinde bei Jericho", None,
  "Beim Auszug aus Jericho folgt Jesus eine grosse Menge. Zwei Blinde am Weg hören, dass Jesus vorbeigeht, und schreien: «Herr, hab Erbarmen mit uns, Sohn Davids!» Die Menge fährt sie an, sie sollen schweigen, doch sie schreien noch lauter. Jesus bleibt stehen und fragt, was er für sie tun solle; sie bitten, dass ihre Augen geöffnet werden. Er hat Erbarmen und berührt ihre Augen; sogleich sehen sie wieder und folgen ihm nach.", None),
 ("TU-MAT-021-001-046", "MAT.21.1-MAT.21.46", "section", "Einzug in Jerusalem, Tempel und Streit um die Vollmacht",
  ["TU-MAT-021-001-011", "TU-MAT-021-012-017", "TU-MAT-021-018-022", "TU-MAT-021-023-027", "TU-MAT-021-028-032", "TU-MAT-021-033-046"],
  "Jesus lässt zwei Jünger eine Eselin und ein Fohlen holen und zieht nach Jerusalem ein; der Erzähler sieht darin [[ZEC.9.9]] erfüllt. Die Menschenmengen breiten Mäntel und Zweige auf den Weg und rufen «Hosanna dem Sohn Davids!», und die ganze Stadt fragt, wer er sei. Im Tempel treibt er Verkäufer und Käufer hinaus, stösst die Tische der Geldwechsler um und heilt Blinde und Lahme; den Hohepriestern und Schriftgelehrten, die sich über die rufenden Kinder empören, hält er [[PSA.8.2]] entgegen. Am Morgen darauf verdorrt ein Feigenbaum, an dem er nur Blätter findet, auf sein Wort hin; den staunenden Jüngern sagt er, was der Glaube ohne Zweifel vermag. Als die Hohepriester und Ältesten nach seiner Vollmacht fragen, stellt er die Gegenfrage nach der Taufe des Johannes; sie antworten, sie wüssten es nicht, und er sagt ihnen nicht, in welcher Vollmacht er handelt. Mit dem Gleichnis von den zwei Söhnen hält er ihnen vor, Johannes nicht geglaubt zu haben, während Zöllner und Prostituierte ihm glaubten. Im Gleichnis von den Weinbauern, die die Knechte und zuletzt den Sohn des Hausherrn töten, kündigt er an, das Reich Gottes werde ihnen weggenommen und einem Volk gegeben, das seine Früchte bringt. Die Hohepriester und Pharisäer erkennen, dass er von ihnen redet, und wollen ihn festnehmen, fürchten aber die Menschenmengen.", SEG),
 ("TU-MAT-021-001-011", "MAT.21.1-MAT.21.11", "narrative", "Der Einzug in Jerusalem", None,
  "Bei Betfage am Ölberg schickt Jesus zwei Jünger in das Dorf vor ihnen, eine angebundene Eselin und ein Fohlen zu holen; wer etwas sage, dem sollen sie antworten, der Herr brauche sie. Darin sieht der Erzähler das Prophetenwort erfüllt: «Siehe, dein König kommt zu dir, sanftmütig und reitend auf einer Eselin und auf einem Fohlen» ([[ISA.62.11]], [[ZEC.9.9]]). Die Jünger bringen die Tiere und legen die Mäntel auf sie, und Jesus setzt sich darauf. Die meisten aus der Menge breiten ihre Mäntel auf dem Weg aus, andere Zweige; die Menschenmengen vor und hinter ihm rufen: «Hosanna dem Sohn Davids! Gesegnet sei, der kommt im Namen des Herrn!» Als er in Jerusalem einzieht, gerät die ganze Stadt in Aufruhr und fragt, wer das sei; die Menschenmengen antworten: der Prophet Jesus aus Nazaret in Galiläa.", None),
 ("TU-MAT-021-012-017", "MAT.21.12-MAT.21.17", "narrative", "Jesus im Tempel", None,
  "Jesus treibt alle, die im Tempel verkaufen und kaufen, hinaus, stösst die Tische der Geldwechsler und die Sitze der Taubenverkäufer um und sagt, geschrieben stehe, sein Haus solle ein Haus des Gebets heissen, sie aber machten es zu einer Räuberhöhle ([[ISA.56.7]], [[JER.7.11]]). Blinde und Lahme kommen im Tempel zu ihm, und er heilt sie. Die Hohepriester und Schriftgelehrten sehen, was er tut, und hören die Kinder im Tempel «Hosanna dem Sohn Davids!» rufen und empören sich. Auf ihre Frage, ob er höre, was diese sagen, antwortet Jesus mit [[PSA.8.2]]: Aus dem Mund von kleinen Kindern und Säuglingen hast du dir Lob bereitet. Dann verlässt er sie und übernachtet in Betanien.", None),
 ("TU-MAT-021-018-022", "MAT.21.18-MAT.21.22", "narrative_with_saying", "Der verdorrte Feigenbaum", None,
  "Als Jesus frühmorgens in die Stadt zurückkehrt, hat er Hunger. An einem Feigenbaum am Weg findet er nur Blätter und sagt: «Nie mehr in Ewigkeit soll aus dir Frucht wachsen!» Der Feigenbaum verdorrt auf der Stelle. Die Jünger staunen. Jesus sagt ihnen: Wenn sie Glauben haben und nicht zweifeln, werden sie nicht nur das mit dem Feigenbaum tun, sondern auch wenn sie zu diesem Berg sagen, er solle sich ins Meer stürzen, wird es geschehen; alles, worum sie im Gebet bitten, werden sie empfangen, wenn sie glauben.", None),
 ("TU-MAT-021-023-027", "MAT.21.23-MAT.21.27", "dialogue", "Die Frage nach der Vollmacht", None,
  "Während Jesus im Tempel lehrt, fragen ihn die Hohepriester und die Ältesten des Volkes, in welcher Vollmacht er das tue und wer sie ihm gegeben habe. Jesus stellt eine Gegenfrage: Die Taufe des Johannes – war sie vom Himmel oder von Menschen? Sie überlegen: Sagen sie «vom Himmel», wird er fragen, warum sie Johannes nicht geglaubt haben; sagen sie «von Menschen», fürchten sie die Menge, die Johannes für einen Propheten hält. So antworten sie, sie wüssten es nicht, und Jesus sagt ihnen ebenfalls nicht, in welcher Vollmacht er das tut.", None),
 ("TU-MAT-021-028-032", "MAT.21.28-MAT.21.32", "parable", "Die zwei Söhne", None,
  "Jesus fragt die Hohepriester und Ältesten nach ihrer Meinung: Ein Mensch schickt nacheinander seine zwei Kinder zur Arbeit in den Weinberg. Der erste sagt «Ich will nicht», bereut es aber später und geht hin; der zweite sagt «Ich gehe, Herr» und geht nicht hin. Auf die Frage, wer von beiden den Willen des Vaters getan habe, antworten sie: der erste. Jesus sagt ihnen: Die Zöllner und die Prostituierten gehen ihnen voran in das Reich Gottes; denn Johannes kam zu ihnen auf dem Weg der Gerechtigkeit, und sie glaubten ihm nicht, die Zöllner und Prostituierten aber glaubten ihm; und obwohl sie es sahen, bereuten sie es nicht einmal danach und glaubten ihm nicht. Die Reihenfolge der beiden Söhne ist in den Handschriften und Ausgaben unterschiedlich überliefert.", None),
 ("TU-MAT-021-033-046", "MAT.21.33-MAT.21.46", "parable", "Die Weinbauern", None,
  "Ein Hausherr pflanzt einen Weinberg, verpachtet ihn an Weinbauern und reist ausser Landes. Zur Zeit der Früchte sendet er seine Knechte, um seine Früchte abzuholen; die Weinbauern verprügeln, töten und steinigen sie, und ebenso ergeht es einer zweiten, grösseren Gruppe von Knechten. Zuletzt sendet er seinen Sohn; die Weinbauern sehen in ihm den Erben, werfen ihn aus dem Weinberg und töten ihn. Auf Jesu Frage, was der Herr des Weinbergs mit ihnen tun wird, antworten die Zuhörer, er werde die Übeltäter übel umbringen und den Weinberg anderen Weinbauern verpachten, die ihm die Früchte abgeben. Jesus verweist auf das Wort vom verworfenen Stein, der zum Eckstein geworden ist ([[PSA.118.22]]–[[PSA.118.23]]), und sagt: Das Reich Gottes wird ihnen weggenommen und einem Volk gegeben werden, das seine Früchte bringt; wer auf diesen Stein fällt, wird zerschellen, und auf wen er fällt, den wird er zermalmen ([[MAT.21.44]] fehlt in einem Teil der Überlieferung). Die Hohepriester und Pharisäer erkennen, dass er von ihnen redet; sie wollen ihn festnehmen, fürchten aber die Menschenmengen, die ihn für einen Propheten halten.", None),
]
UNITS_GSW = {
 "TU-MAT-020-001-034": ("D Arbeiter im Wiibärg, de Wäg uf Jerusalem und zwei Blindi bi Jericho", "De Jesus verzellt vom Huusherr, wo zu verschidene Stunde Arbeiter für sin Wiibärg aastellt und am Aabig allne de gliich Loon, en Denar, uszahle laat; dene, wo muuled, hebt er sini Güeti entgäge: So wärded di Letschte Erschti sii und di Erschte Letschti. Uf em Wäg uf Jerusalem seit de Jesus de Zwölf aa, de Mänschesohn wärdi usgliferet, zum Tod verurteilt und gchrüziget und am dritte Tag uferweckt. D Mueter vo de Söhn vom Zebedäus bittet, iri Söhn söled i sim Riich a sinere Rächte und Linke sitze; de Jesus antwortet, si wärdid sin Bächer trinke, aber die Plätz z vergää stöng nöd ihm zue. De Zää, wo sich ergered, seit er, wer gross wärde well, söll Diener sii, so wie de Mänschesohn choo sig zum diene und zum sis Läbe als Lösgält für vili gää. Bim Furtgaa vo Jericho rüefed zwei Blindi de Jesus als Sohn vom David um Erbarme aa; er rüert iri Auge aa, si gsehnd wider und folged ihm nache."),
 "TU-MAT-020-001-016": ("D Arbeiter im Wiibärg", "De Jesus vergliicht s Riich vo de Himel mit eme Huusherr, wo am Morge früe Arbeiter für en Denar im Tag in sin Wiibärg schickt und um di dritt, di sächst, di nüünt und di elft Stund no meh ane schickt. Am Aabig laat er dur sin Verwalter de Loon uszahle, bi de Letschte aagfange: Alli überchömed en Denar. Di Erschte, wo meh erwartet händ, muuled, wil di Letschte nu e Stund gschaffet händ und ine gliichgstellt sind. De Huusherr antwortet eim vo ine, er tüeg ihm kei Unrächt, si seigid sich uf en Denar einig worde; er well em Letschte gää wie ihm. Er fröget, öb er mit sim Eigete nöd dörf mache, was er well, oder öb sis Aug böös sig, wil er guet sig. So wärded di Letschte Erschti sii und di Erschte Letschti."),
 "TU-MAT-020-017-019": ("Di dritt Aakündigung vom Liide und vo de Uferweckig", "Uf em Wäg ufe uf Jerusalem nimmt de Jesus di zwölf Jünger uf d Siite und seit aa: De Mänschesohn wird de Hoheprieschter und de Schriftgelehrte usgliferet; si wärded en zum Tod verurteile und de Heide usliefere, damit er verspottet, uspeitscht und gchrüziget wird; am dritte Tag wird er uferweckt."),
 "TU-MAT-020-020-028": ("Herrsche und diene", "D Mueter vo de Söhn vom Zebedäus chunnt mit ire Söhn zum Jesus häre, wirft sich vor ihm nider und bittet, iri zwei Söhn söled i sim Riich a sinere Rächte und a sinere Linke sitze. De Jesus antwortet, si wüssid nöd, was si verlanged, und fröget, öb si de Bächer chönd trinke, wo er jetzt dänn trinki; si säged, si chönid s. Er seit, sin Bächer wärdid si trinke, aber d Plätz a sinere Rächte und Linke z vergää stöng nöd ihm zue; si ghöred dene, für die sin Vatter si parat gmacht heig. D Zää ergered sich über di zwei Brüedere. De Jesus stellt ine d Herrscher vo de Völker gägenüber, wo Gwalt bruuched: Under ine söll s nöd so sii; wer gross wärde wott, söll Diener sii, und wer de Erscht sii wott, Sklav, so wie de Mänschesohn nöd choo isch zum sich la diene, sondern zum diene und zum sis Läbe als Lösgält für vili gää."),
 "TU-MAT-020-029-034": ("Zwei Blindi bi Jericho", "Bim Furtgaa vo Jericho folget em Jesus e grossi Mängi. Zwei Blindi am Wäg ghöred, dass de Jesus verbiigaat, und schreied: «Herr, häb Erbarme mit üs, Sohn vom David!» D Mängi fahrt si aa, si söled still sii, aber si schreied no lüüter. De Jesus bliibt staa und fröget, was er für si söll mache; si bitted, dass iri Auge ufgönd. Er hät Erbarme und rüert iri Auge aa; grad gsehnd si wider und folged ihm nache."),
 "TU-MAT-021-001-046": ("Iizug z Jerusalem, Tämpel und Striit um d Vollmacht", "De Jesus laat zwei Jünger e Eselin und es Füli hole und ziet uf Jerusalem ii; de Erzäler gseht drin [[ZEC.9.9]] erfüllt. D Lüüt breited Mäntel und Zweig uf de Wäg und rüefed «Hosanna em Sohn vom David!», und di ganz Stadt fröget, wer er sig. Im Tämpel jagt er d Verchäufer und d Chäufer use, schmeisst d Tisch vo de Gältwächsler um und heilt Blindi und Lahmi; de Hoheprieschter und de Schriftgelehrte, wo sich über di rüefende Chind ergered, hebt er [[PSA.8.2]] entgäge. Am Morge druf verdorret en Fiigebaum, wo er nu Bletter dra findt, uf sis Wort hi; de stuunende Jünger seit er, was de Glaube ohni Zwiifel vermag. Wo d Hoheprieschter und d Ältischte nach sinere Vollmacht fröged, stellt er d Gägefrag nach de Taufi vom Johannes; si antworted, si wüssid s nöd, und er seit ine nöd, mit was für ere Vollmacht er handlet. Mit em Gliichnis vo de zwei Söhn hebt er ine vor, si heigid em Johannes nöd glaubt, wo doch Zöllner und Prostituierti ihm glaubt händ. Im Gliichnis vo de Wiibuure, wo d Chnächt und zletscht de Sohn vom Huusherr umbringed, seit er aa, s Riich vo Gott wärdi ine wäggnoo und eme Volk gää, wo sini Frücht bringt. D Hoheprieschter und d Pharisäer merked, dass er vo ine redt, und wänd en feschtnää, händ aber Angscht vor de Lüüt."),
 "TU-MAT-021-001-011": ("De Iizug z Jerusalem", "Bi Betfage am Ölberg schickt de Jesus zwei Jünger i s Dorf vor ine, go e aabundeni Eselin und es Füli hole; wänn öpper öppis säg, söled si antworte, de Herr bruuchi si. Drin gseht de Erzäler s Prophetewort erfüllt: «Lueg, din König chunnt zu dir, sanftmüetig und rittet uf ere Eselin und uf eme Füli» ([[ISA.62.11]], [[ZEC.9.9]]). D Jünger bringed d Tier und leged d Mäntel druf, und de Jesus setzt sich druf. Di meischte vo de Mängi breited iri Mäntel uf em Wäg us, anderi Zweig; d Lüüt vor und hinder ihm rüefed: «Hosanna em Sohn vom David! Gsägnet sig dä, wo chunnt im Name vom Herr!» Wo er uf Jerusalem ine chunnt, gratet di ganz Stadt in Ufruer und fröget, wer das sig; d Lüüt antworted: de Prophet Jesus vo Nazaret in Galiläa."),
 "TU-MAT-021-012-017": ("De Jesus im Tämpel", "De Jesus jagt alli, wo im Tämpel verchaufed und chaufed, use, schmeisst d Tisch vo de Gältwächsler und d Stüel vo de Tuubeverchäufer um und seit, es stönd gschribe, sis Huus söll es Huus zum Bätte heisse, si aber mached e Röiberhöli drus ([[ISA.56.7]], [[JER.7.11]]). Blindi und Lahmi chömed im Tämpel zu ihm, und er heilt si. D Hoheprieschter und d Schriftgelehrte gsehnd, was er macht, und ghöred d Chind im Tämpel «Hosanna em Sohn vom David!» rüefe und ergered sich. Uf iri Frag, öb er ghör, was die säged, antwortet de Jesus mit [[PSA.8.2]]: Us em Muul vo chliine Chind und Söiglinge häsch du dir Lob parat gmacht. Dänn verlaat er si und übernachtet z Betanie."),
 "TU-MAT-021-018-022": ("De verdorret Fiigebaum", "Wo de Jesus am Morge früe i d Stadt zrugg gaat, hät er Hunger. A eme Fiigebaum am Wäg findt er nu Bletter und seit: «Nie meh i Ewigkeit söll us dir Frucht wachse!» De Fiigebaum verdorret uf de Stell. D Jünger stuuned. De Jesus seit ine: Wänn si Glaube händ und nöd zwiifled, wärded si nöd nu das mit em Fiigebaum mache, sondern au wänn si zu dem Bärg säged, er söll sich is Meer stürze, wird s passiere; alles, wo si im Gebät drum bitted, wärded si übercho, wänn si glaubed."),
 "TU-MAT-021-023-027": ("D Frag nach de Vollmacht", "Während de Jesus im Tämpel lehrt, fröged en d Hoheprieschter und d Ältischte vom Volk, mit was für ere Vollmacht er das mach und wer si ihm gää heig. De Jesus stellt e Gägefrag: D Taufi vom Johannes – isch si vom Himel gsii oder vo Mänsche? Si überleged: Säged si «vom Himel», fröget er, werum si em Johannes nöd glaubt händ; säged si «vo Mänsche», händ si Angscht vor de Mängi, wo de Johannes für en Prophet haltet. Drum antworted si, si wüssid s nöd, und de Jesus seit ine au nöd, mit was für ere Vollmacht er das macht."),
 "TU-MAT-021-028-032": ("Di zwei Söhn", "De Jesus fröget d Hoheprieschter und d Ältischte nach irer Meinig: En Mänsch schickt nachenand sini zwei Chind go schaffe in Wiibärg. De erscht seit «Ich wott nöd», aber spöter rout s en, und er gaat; de zweit seit «Ich gaa, Herr» und gaat nöd. Uf d Frag, wele vo beide de Wille vom Vatter gmacht heig, antworted si: de erscht. De Jesus seit ine: D Zöllner und d Prostituierte gönd ine voraa is Riich vo Gott; dänn de Johannes isch zu ine choo uf em Wäg vo de Grächtigkeit, und si händ ihm nöd glaubt, d Zöllner und d Prostituierte aber händ ihm glaubt; und obwohl si s gseh händ, hät s si nöd emal spöter groue, und si händ ihm nöd glaubt. D Reihefolg vo de zwei Söhn isch i de Handschrifte und Usgabe verschide überliferet."),
 "TU-MAT-021-033-046": ("D Wiibuure", "En Huusherr pflanzt en Wiibärg aa, verpachtet en a Wiibuure und verreist. Zur Ziit vo de Frücht schickt er sini Chnächt, go sini Frücht hole; d Wiibuure verprügled, töded und steiniged si, und eso gaat s au ere zweite, grössere Gruppe vo Chnächt. Zletscht schickt er sin Sohn; d Wiibuure gsehnd i ihm de Erb, rüered en us em Wiibärg und bringed en um. Uf d Frag vom Jesus, was de Herr vom Wiibärg mit ine macht, antworted d Zuehörer, er wärdi di Bööse böös umbringe und de Wiibärg a anderi Wiibuure verpachte, wo ihm d Frücht abgänd. De Jesus verwiist uf s Wort vom verworfne Stei, wo zum Eckstei worde isch ([[PSA.118.22]]–[[PSA.118.23]]), und seit: S Riich vo Gott wird ine wäggnoo und eme Volk gää, wo sini Frücht bringt; wer uf dä Stei gheit, wird verschmätteret, und uf wän er gheit, dä zermalmt er ([[MAT.21.44]] fehlt i eme Teil vo de Überliferig). D Hoheprieschter und d Pharisäer merked, dass er vo ine redt; si wänd en feschtnää, händ aber Angscht vor de Lüüt, wo en für en Prophet halted."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "Handschriften werden mit ihren Gregory-Aland-Nummern genannt (01 Sinaiticus, 03 Vaticanus, 04 Ephraemi, 05 Bezae, "
  "032 Washingtonianus, 𝔓45). Wo die automatische Zuordnung einer Handschrift «andere Lesart» oder «nicht erhalten» "
  "zuweist, ist der Wortlaut der Transkription genannt oder die Unsicherheit benannt."),
 ("Einheitliche Begriffe für das ganze Matthäusevangelium: «das Reich der Himmel» (Mundart «s Riich vo de Himel»), "
  "«das Reich Gottes» («s Riich vo Gott»), «der Menschensohn» («de Mänschesohn»), «Amen, ich sage euch» («Amen, ich säg eu»), "
  "ἰδού «siehe» («lueg»), εὐθέως/εὐθύς «sogleich» («grad»), τότε «da» («dänn»), Hohepriester, Schriftgelehrte, Älteste, "
  "Pharisäer, die Erfüllungsformel «damit erfüllt würde, was … durch den Propheten gesagt ist» («damit erfüllt wird, was … "
  "dur de Prophet gseit worden isch»). Gleiche griechische Wendungen sind möglichst wie in der Markus-Übersetzung "
  "([[MRK.10.32]]–[[MRK.12.12]]) wiedergegeben; wo Matthäus anders formuliert, folgt die Übersetzung seinem Wortlaut."),
 ("In diesem Bereich festgelegte bzw. verwendete Wiedergaben (die für das ganze Evangelium einheitlichen sind gekennzeichnet): πίστις «Glaube», πιστεύω "
  "«glauben»; δικαιοσύνη «Gerechtigkeit» («Grächtigkeit»); μεταμέλομαι «bereuen» (Mundart «groue»), unterschieden von "
  "μετανοέω «umkehren»; einheitlich: προσκυνέω «sich (vor jemandem) niederwerfen» (mit Gott als Empfänger «anbeten»), προσέρχομαι «herantreten»; "
  "δοῦλος «Sklave» im Spruch, «Knecht» im Gleichnis; οἱ ὄχλοι «die Menschenmengen» (Mundart «d Lüüt»), ὁ ὄχλος «die Menge» "
  "(«d Mängi»); ἔθνη «Heiden» bzw. «Völker» nach Zusammenhang, ἔθνος «Volk»; ἐλέησον «hab Erbarmen» («häb Erbarme»), "
  "einheitlich σπλαγχνίζομαι «Erbarmen haben» (Mundart «Erbarme haa»); κράζω «schreien», bei Huldigungsrufen «rufen»; "
  "ἀμπελών «Weinberg» («Wiibärg»), γεωργοί «Weinbauern» («Wiibuure»), οἰκοδεσπότης «Hausherr» («Huusherr»), μισθός «Lohn» "
  "(«Loon»); τέκνον «Kind»; ἐξουσία «Vollmacht»; ποτήριον «Becher»; παραδίδωμι «ausliefern»; ἐγείρω (passiv) «auferweckt "
  "werden»; Ὡσαννά «Hosanna»."),
 ("Redegrenzen: Das Gleichnis [[MAT.20.1]]–[[MAT.20.16]] setzt die Rede Jesu aus Kapitel 19 fort; es beginnt hier mit einem "
  "eigenen öffnenden Anführungszeichen. Reden innerhalb von Reden und Gleichnissen stehen in ‹ ›. Das Griechische hat keine "
  "Anführungszeichen; ὅτι und λέγων/λέγοντες vor direkter Rede sind nicht eigens übersetzt. Das erzählende Präsens "
  "(λέγει «sagt») ist beibehalten."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT nur mit einem Teil der Ausgaben geht (z. B. "
  "[[MAT.20.26]] ἔσται mit NA28 gegen WH, Treg und RP). Abweichende Lesarten stehen als Alternativen, soweit sie die "
  "Übersetzung verändern; reine Wortstellungs- und Schreibvarianten sind nicht aufgenommen. In Kapitel 20–21 fehlt im SBLGNT "
  "kein Vers (per Skript geprüft). [[MAT.21.44]] steht im SBLGNT; seine Auslassung (WH am Rand) ist als Alternative "
  "aufgenommen. In [[MAT.21.29]]–[[MAT.21.31]] folgt die Übersetzung der Reihenfolge der Söhne im SBLGNT; die vertauschte "
  "Fassung (WH) steht in drei zusammengehörigen Alternativen."),
 ("Abgrenzung: Dieses Werkzeug umfasst nur [[MAT.20.1]]–[[MAT.21.46]]. Die Kapitel 19 und 22 gehören zu anderen Bereichen; "
  "Querverweise darauf ([[MAT.19.30]], [[MAT.22.14]]) setzen deren Übersetzung nicht voraus."),
 "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Einheitlichi Begriff fürs ganz Matthäusevangelium: «s Riich vo de Himel», «s Riich vo Gott», «de Mänschesohn», «Amen, ich säg "
  "eu», «lueg», «grad», «dänn», Hoheprieschter, Schriftgelehrti, Ältischti; Erfüllungsformle «damit erfüllt wird, was … dur de "
  "Prophet gseit worden isch»."),
 ("I dem Bereich festgleit: πίστις «Glaube»; δικαιοσύνη «Grächtigkeit»; μεταμέλομαι «groue» (nöd «umchehre»); "
  "οἱ ὄχλοι «d Lüüt», ὁ ὄχλος «d Mängi»; σπλαγχνίζομαι «Erbarme haa»; προσέρχομαι «härechoo»; προσκυνέω «sich niderwärfe»; ἐλέησον «häb Erbarme»; δοῦλος «Sklav» im Spruch, "
  "«Chnächt» im Gliichnis; μισθός «Loon»; ἀμπελών «Wiibärg», γεωργοί «Wiibuure»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Johannes»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«s Riich vo Gott», «de Sohn vom David»)."),
 "Eigeti Formulierig; nöd us ere veröffentlichte Mundartbible übernoo.",
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
            raise SystemExit(f"MAT {c}: unerwartete Verszahl")
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Riich, Loon), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Namen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; wiederkehrende Begriffe einheitlich (translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_20_21.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 20–21 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
