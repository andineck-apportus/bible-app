#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 10–11 (Aussendungsrede, Anfrage des Täufers, Jesu Zeugnis über Johannes, Weherufe,
Lobpreis und Einladung) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_10_11.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 10–11 fehlt im SBLGNT kein Vers (per Skript geprüft); alle Verse haben Tokens.
- [[MAT.11.1]] schliesst die Aussendungsrede mit der Formel ab, die alle fünf grossen Reden des Matthäus beendet;
  die Kapiteleinteilung zieht den Vers zu Kapitel 11, die Gliederung stellt ihn als Überleitung an den Anfang von
  [[MAT.11.1-MAT.11.6]].
- [[MAT.11.9]]: Der SBLGNT setzt (wie WH und SR) das Fragezeichen nach ἐξήλθατε; KJTR, Stephanus und RP lesen
  τί ἐξήλθετε ἰδεῖν; προφήτην; (nach den CNTR-Texten). Der importierte Apparat führt das nicht als eigene Variante;
  der Befund steht in decisions.

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
CHAPTERS = ((10, 42), (11, 30))
SCRIPT = "scripts/authoring/matthaeus_text_10_11.py"

DE = {
 # ------------------------------------------------------------ Kapitel 10
 "MAT.10.1": "Und{1} [er rief]{2} [seine]{6} [zwölf]{3,4} [Jünger]{5} [zu sich]{2} und [gab]{7} [ihnen]{8} [Vollmacht]{9} über [unreine]{11} [Geister]{10}, [um]{12} [sie]{14} [auszutreiben]{13} und{15} [jede]{17} [Krankheit]{18} und{19} [jedes]{20} [Gebrechen]{21} [zu heilen]{16}.",
 "MAT.10.2": "[Die Namen]{5,6} [der]{1} [zwölf]{3} [Apostel]{4} [aber]{2} [sind]{7} [diese]{8}: [zuerst]{9} [Simon]{10}, [der]{11} [Petrus]{13} [genannt wird]{12}, und{14} [Andreas]{15}, [sein]{18} [Bruder]{16,17}, [Jakobus]{19}, [der Sohn]{20} [des]{21} [Zebedäus]{22}, und{23} [Johannes]{24}, [sein]{27} [Bruder]{25,26},",
 "MAT.10.3": "[Philippus]{1} und{2} [Bartholomäus]{3}, [Thomas]{4} und{5} [Matthäus]{6}, [der]{7} [Zöllner]{8}, [Jakobus]{9}, [der Sohn]{10} [des]{11} [Alphäus]{12}, und{13} [Thaddäus]{14},",
 "MAT.10.4": "[Simon]{1}, [der]{2} [Kananäer]{3}, und{4} [Judas]{5} [Iskariot]{6,7}, [der]{8} [ihn]{11} [auch]{9} [auslieferte]{10}.",
 "MAT.10.5": "[Diese]{1} [Zwölf]{2,3} [sandte]{4} [Jesus]{5,6} [aus]{4} und [gebot]{7} [ihnen]{8}: «[Geht]{14} [nicht]{13} [auf]{10} [einen Weg]{11} [zu den Heiden]{12} [und]{15} [geht]{20} [in]{16} [keine]{19} [Stadt]{17} [der Samaritaner]{18} [hinein]{20}! ~9(λέγων «sagend» leitet die direkte Rede ein)",
 "MAT.10.6": "[Geht]{1} [vielmehr]{3} [zu]{4} [den]{5} [verlorenen]{7,8} [Schafen]{6} [des Hauses]{9} [Israel]{10}! ~2(δέ verbindet mit dem Vorigen; durch «vielmehr» mit ausgedrückt)",
 "MAT.10.7": "[Unterwegs]{1} [aber]{2} [verkündigt]{3} und [sagt]{4}: ‹[Das Reich]{7,8} [der Himmel]{9,10} [ist nahe gekommen]{6}.› ~5(ὅτι leitet die direkte Rede ein)",
 "MAT.10.8": "[Heilt]{2} [Kranke]{1}, [weckt]{4} [Tote]{3} [auf]{4}, [macht]{6} [Aussätzige]{5} [rein]{6}, [treibt]{8} [Dämonen]{7} [aus]{8}! [Umsonst]{9} [habt ihr empfangen]{10}, [umsonst]{11} [gebt]{12}!",
 "MAT.10.9": "[Verschafft euch]{2} [kein]{1} [Gold]{3}, [kein]{4} [Silber]{5} [und kein]{6} [Kupfergeld]{7} [für]{8} [eure]{11} [Gürtel]{9,10},",
 "MAT.10.10": "[keinen]{1} [Beutel]{2} [für]{3} [den Weg]{4}, [nicht]{5} [zwei]{6} [Untergewänder]{7}, [keine]{8} [Sandalen]{9} [und keinen]{10} [Stab]{11}; [denn]{13} [der]{14} [Arbeiter]{15} ist [seiner]{18} [Nahrung]{16,17} [wert]{12}.",
 "MAT.10.11": "[In]{1} [welche]{2} [Stadt]{5} [oder]{6} [welches Dorf]{7} [ihr]{8} [aber]{3} [auch]{4} [kommt]{8}, [erkundigt euch]{9}, [wer]{10} [in]{11} [ihr]{12} [würdig]{13} [ist]{14}; [und dort]{15} [bleibt]{16}, [bis]{17,18} [ihr weiterzieht]{19}.",
 "MAT.10.12": "[Wenn ihr]{1} [aber]{2} [in]{3} [das]{4} [Haus]{5} [hineingeht]{1}, [grüsst]{6} [es]{7}.",
 "MAT.10.13": "Und{1} [wenn]{2} [das Haus]{5,6} [würdig]{7} [ist]{4}, [soll]{8} [euer]{11} [Friede]{9,10} [darauf]{12,13} [kommen]{8}; [wenn]{14} es [aber]{15} [nicht]{16} [würdig]{18} [ist]{17}, [soll]{24} [euer]{21} [Friede]{19,20} [zu]{22} [euch]{23} [zurückkehren]{24}. ~3(μέν bildet mit δέ ein Gegensatzpaar; nicht eigens wiedergegeben)",
 "MAT.10.14": "Und{1} [wer]{2} [euch]{6} [nicht]{4} [aufnimmt]{5} [und]{7} [eure]{11} [Worte]{9,10} [nicht]{7} [hört]{8}, [verlasst]{12,13} [das Haus]{14,15} [oder]{16} [jene]{19} [Stadt]{17,18} und [schüttelt]{20} [den Staub]{21,22} von [euren]{25} [Füssen]{23,24} [ab]{20}. ~3(ἄν verallgemeinert «wer»; nicht eigens wiedergegeben)",
 "MAT.10.15": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Dem Land]{6} [Sodom]{7} und{8} [Gomorra]{9} [wird es]{5} [am]{10} [Tag]{11} [des Gerichts]{12} [erträglicher]{4} [ergehen]{5} [als]{13} [jener]{16} [Stadt]{14,15}.",
 "MAT.10.16": "[Siehe]{1}, [ich]{2} [sende]{3} [euch]{4} [wie]{5} [Schafe]{6} [mitten]{7,8} unter [Wölfe]{9}; [seid]{10} [also]{11} [klug]{12} [wie]{13} [die]{14} [Schlangen]{15} und{16} [ohne Falsch]{17} [wie]{18} [die]{19} [Tauben]{20}.",
 "MAT.10.17": "[Hütet euch]{1} [aber]{2} [vor]{3} [den]{4} [Menschen]{5}; [denn]{7} [sie werden]{6} [euch]{8} [an]{9} [Gerichte]{10} [ausliefern]{6}, und{11} [in]{12} [ihren]{15} [Synagogen]{13,14} [werden sie]{16} [euch]{17} [geisseln]{16},",
 "MAT.10.18": "[und]{1} [auch]{4} [vor]{2} [Statthalter]{3} und{5} [Könige]{6} [werdet ihr geführt werden]{7} [um meinetwillen]{8,9}, [ihnen]{12} [und]{13} [den Heiden]{14,15} [zum]{10} [Zeugnis]{11}.",
 "MAT.10.19": "[Wenn]{1} [sie]{3} [euch]{4} [aber]{2} [ausliefern]{3}, [sorgt euch]{6} [nicht]{5}, [wie]{7} [oder]{8} [was]{9} [ihr reden sollt]{10}; [denn]{12} [es wird]{11} [euch]{13} [in]{14} [jener]{15,16} [Stunde]{17} [gegeben]{11}, [was]{18} [ihr reden sollt]{19}.",
 "MAT.10.20": "[Denn]{2} [nicht]{1} [ihr]{3} [seid es]{4}, [die]{5} [reden]{6}, [sondern]{7} [der Geist]{8,9} [eures]{12} [Vaters]{10,11} ist es, [der]{13} [in]{15} [euch]{16} [redet]{14}.",
 "MAT.10.21": "[Es wird]{1} [aber]{2} [ein Bruder]{3} [den Bruder]{4} [in]{5} [den Tod]{6} [ausliefern]{1} und{7} [ein Vater]{8} [das Kind]{9}, und{10} [Kinder]{12} [werden sich]{11} [gegen]{13} [Eltern]{14} [erheben]{11} und{15} [sie]{17} [in den Tod bringen]{16}.",
 "MAT.10.22": "Und{1} [ihr werdet]{2} [von]{4} [allen]{5} [gehasst sein]{3} [wegen]{6} [meines]{9} [Namens]{7,8}. [Wer]{10} [aber]{11} [bis]{13} [ans Ende]{14} [standhält]{12}, [der]{15} [wird gerettet werden]{16}.",
 "MAT.10.23": "[Wenn]{1} [sie]{3} [euch]{4} [aber]{2} [in]{5} [dieser]{6,8} [Stadt]{7} [verfolgen]{3}, [flieht]{9} [in]{10} [die]{11} [andere]{12}. [Amen]{13}, [ich sage]{15} [euch]{16} [nämlich]{14}: [Ihr werdet]{19} mit [den Städten]{20,21} [Israels]{22,23} [gewiss nicht]{17,18} [zu Ende kommen]{19}, [bis]{24,25} [der Menschensohn]{27-30} [kommt]{26}.",
 "MAT.10.24": "[Ein Jünger]{3} [steht]{2} [nicht]{1} [über]{4} [dem]{5} [Lehrer]{6} [und kein]{7} [Knecht]{8} [über]{9} [seinem]{10,12} [Herrn]{11}.",
 "MAT.10.25": "[Es genügt]{1} [dem]{2} [Jünger]{3}, [dass]{4} er [wie]{6} [sein]{7,9} [Lehrer]{8} [wird]{5}, und{10} [der]{11} [Knecht]{12} [wie]{13} [sein]{14,16} [Herr]{15}. [Wenn]{17} sie [den]{18} [Hausherrn]{19} [Beelzebul]{20} [genannt haben]{21}, [wie viel mehr]{22,23} [seine]{26} [Hausgenossen]{24,25}!",
 "MAT.10.26": "[Fürchtet]{3} [sie]{4} [also]{2} [nicht]{1}! [Denn]{6} [nichts]{5} [ist]{7} [verhüllt]{8}, [das]{9} [nicht]{10} [enthüllt werden wird]{11}, und{12} nichts [verborgen]{13}, [das]{14} [nicht]{15} [bekannt werden wird]{16}.",
 "MAT.10.27": "[Was]{1} [ich]{2} [euch]{3} [in]{4} [der Finsternis]{5,6} [sage]{2}, [das sagt]{7} [im]{8,9} [Licht]{10}; und{11} [was]{12} [ihr]{16} [ins]{13,14} [Ohr]{15} geflüstert [hört]{16}, [das verkündigt]{17} [auf]{18} [den]{19} [Dächern]{20}.",
 "MAT.10.28": "Und{1} [fürchtet euch]{3} [nicht]{2} [vor]{4} [denen]{5}, [die]{6} [den Leib]{7,8} [töten]{6}, [die Seele]{9,11} [aber]{10} [nicht]{12} [töten]{14} [können]{13}; [fürchtet]{15} [aber]{16} [vielmehr]{17} [den]{18}, [der]{19} [sowohl]{20} [Seele]{21} [als auch]{22} [Leib]{23} [in]{25} [der Hölle]{26} [verderben]{24} [kann]{19}.",
 "MAT.10.29": "[Werden]{5} [nicht]{1} [zwei]{2} [Spatzen]{3} [für einen Groschen]{4} [verkauft]{5}? Und{6} [nicht]{10} [einer]{7} [von]{8} [ihnen]{9} [wird]{11} [auf]{12} [die Erde]{13,14} [fallen]{11} [ohne]{15} [euren]{18} [Vater]{16,17}.",
 "MAT.10.30": "[Bei euch]{1} [aber]{2} [sind]{10} [sogar]{3} [die]{4} [Haare]{5} [auf dem Kopf]{6,7} [alle]{8} [gezählt]{9}.",
 "MAT.10.31": "[Fürchtet euch]{3} [also]{2} [nicht]{1}! [Ihr]{7} [seid]{6} [mehr wert]{6} [als viele]{4} [Spatzen]{5}.",
 "MAT.10.32": "[Jeder]{1} [nun]{2}, [der]{3} sich [vor]{7} [den]{8} [Menschen]{9} [zu]{5} [mir]{6} [bekennt]{4}, [zu]{12} [dem]{13} [werde]{10} [auch ich]{11} mich [bekennen]{10} [vor]{14} [meinem]{15,17} [Vater]{16} [in]{18,19} [den Himmeln]{20};",
 "MAT.10.33": "[wer]{1,3} [mich]{5} [aber]{2} [vor]{6} [den]{7} [Menschen]{8} [verleugnet]{4}, [den]{11} [werde]{9} [auch ich]{10} [verleugnen]{9} [vor]{12} [meinem]{13,15} [Vater]{14} [in]{16,17} [den Himmeln]{18}.",
 "MAT.10.34": "[Meint]{2} [nicht]{1}, [dass]{3} [ich gekommen bin]{4}, [Frieden]{6} [auf]{7} [die Erde]{8,9} [zu bringen]{5}! [Ich bin]{11} [nicht]{10} [gekommen]{11}, [Frieden]{13} [zu bringen]{12}, [sondern]{14} [ein Schwert]{15}.",
 "MAT.10.35": "[Denn]{2} [ich bin gekommen]{1}, [einen Menschen]{4} [mit]{5} [seinem]{6,8} [Vater]{7} [zu entzweien]{3} und{9} [eine Tochter]{10} [mit]{11} [ihrer]{12,14} [Mutter]{13} und{15} [eine Schwiegertochter]{16} [mit]{17} [ihrer]{18,20} [Schwiegermutter]{19},",
 "MAT.10.36": "und{1} [die Feinde]{2} [des Menschen]{3,4} werden [seine]{7} [Hausgenossen]{5,6} sein.",
 "MAT.10.37": "[Wer]{1} [Vater]{3} [oder]{4} [Mutter]{5} [mehr]{6} [liebt]{2} [als mich]{7}, [ist]{9} [meiner]{10} [nicht]{8} [würdig]{11}; und{12} [wer]{13} [Sohn]{15} [oder]{16} [Tochter]{17} [mehr]{18} [liebt]{14} [als mich]{19}, [ist]{21} [meiner]{22} [nicht]{20} [würdig]{23};",
 "MAT.10.38": "und{1} [wer]{2} [sein]{5,7} [Kreuz]{6} [nicht]{3} [auf sich nimmt]{4} und{8} [mir]{11} [nachfolgt]{9,10}, [ist]{13} [meiner]{14} [nicht]{12} [würdig]{15}.",
 "MAT.10.39": "[Wer]{1} [sein]{3,5} [Leben]{4} [gefunden hat]{2}, [wird]{6} [es]{7} [verlieren]{6}, und{8} [wer]{9} [sein]{11,13} [Leben]{12} [um meinetwillen]{14,15} [verloren hat]{10}, [wird]{16} [es]{17} [finden]{16}.",
 "MAT.10.40": "[Wer]{1} [euch]{3} [aufnimmt]{2}, [nimmt]{5} [mich]{4} [auf]{5}; und{6} [wer]{7} [mich]{8} [aufnimmt]{9}, [nimmt]{10} [den]{11} [auf]{10}, [der]{12} [mich]{13} [gesandt hat]{12}.",
 "MAT.10.41": "[Wer]{1} [einen Propheten]{3} [aufnimmt]{2}, [weil er ein Prophet ist]{4-6:idiom}, [wird]{9} [den Lohn]{7} [eines Propheten]{8} [empfangen]{9}; und{10} [wer]{11} [einen Gerechten]{13} [aufnimmt]{12}, [weil er ein Gerechter ist]{14-16:idiom}, [wird]{19} [den Lohn]{17} [eines Gerechten]{18} [empfangen]{19}.",
 "MAT.10.42": "Und{1} [wer]{2,3} [einem]{5} [dieser]{6,8} [Kleinen]{7} auch [nur]{11} [einen Becher]{9} [kaltes Wasser]{10} [zu trinken gibt]{4}, [weil er ein Jünger ist]{12-14:idiom} – [amen]{15}, [ich sage]{16} [euch]{17}: [Er wird]{20} [seinen]{21,23} [Lohn]{22} [gewiss nicht]{18,19} [verlieren]{20}.»",
 # ------------------------------------------------------------ Kapitel 11
 "MAT.11.1": "Und{1} [es geschah]{2}: [Als]{3} [Jesus]{5,6} [die Anweisungen]{7} [an]{8} [seine]{11} [zwölf]{9} [Jünger]{10} [beendet hatte]{4}, [zog er]{12} [von dort]{13} [weiter]{12}, [um]{14} [in]{18} [ihren]{21} [Städten]{19,20} [zu lehren]{15} und{16} [zu verkündigen]{17}.",
 "MAT.11.2": "Als [Johannes]{1,3} [aber]{2} [im]{5,6} [Gefängnis]{7} [von den Werken]{8,9} [des Christus]{10,11} [hörte]{4}, [sandte er]{12} [durch]{13} [seine]{14,16} [Jünger]{15}",
 "MAT.11.3": "und liess [ihm]{2} [sagen]{1}: «[Bist]{4} [du]{3} [der]{5} [Kommende]{6}, [oder]{7} [sollen wir]{9} [auf einen anderen]{8} [warten]{9}?»",
 "MAT.11.4": "Und{1} [Jesus]{3,4} [antwortete]{2} und [sagte]{5} [zu ihnen]{6}: «[Geht hin]{7} und [berichtet]{8} [Johannes]{9}, [was]{10} [ihr hört]{11} und{12} [seht]{13}:",
 "MAT.11.5": "[Blinde]{1} [sehen wieder]{2}, und{3} [Lahme]{4} [gehen umher]{5}, [Aussätzige]{6} [werden rein]{7}, und{8} [Taube]{9} [hören]{10}, und{11} [Tote]{12} [werden auferweckt]{13}, und{14} [den Armen]{15} [wird das Evangelium verkündigt]{16};",
 "MAT.11.6": "und{1} [selig]{2} [ist]{3}, [wer]{4,5} [an]{8} [mir]{9} [keinen]{6} [Anstoss nimmt]{7}.»",
 "MAT.11.7": "Als [diese]{1} [aber]{2} [weggingen]{3}, [begann]{4} [Jesus]{5,6} [zur Menge]{8,9} [über]{10} [Johannes]{11} [zu reden]{7}: «[Was]{12} [seid ihr]{13} [in]{14} [die Wüste]{15,16} [hinausgegangen]{13} [anzuschauen]{17}? [Ein Schilfrohr]{18}, das [vom]{19} [Wind]{20} [hin und her bewegt wird]{21}?",
 "MAT.11.8": "[Oder]{1} [was]{2} [seid ihr hinausgegangen]{3} [zu sehen]{4}? [Einen Menschen]{5}, [in]{6} [weiche Kleider]{7} [gehüllt]{8}? [Siehe]{9}, [die]{10} [weiche Kleider]{11,12} [tragen]{13}, [sind]{19} [in]{14} [den]{15} [Häusern]{16} [der Könige]{17,18}.",
 "MAT.11.9": "[Oder]{1} [was]{2} [seid ihr hinausgegangen]{3}? [Einen Propheten]{4} [zu sehen]{5}? [Ja]{6}, [ich sage]{7} [euch]{8}: [sogar]{9} [mehr]{10} [als einen Propheten]{11}.",
 "MAT.11.10": "[Dieser]{1} [ist es]{2}, [über]{3} [den]{4} [geschrieben steht]{5}: ‹[Siehe]{6}, [ich]{7} [sende]{8} [meinen]{9,11} [Boten]{10} [vor]{12,13} [dir]{14} [her]{12,13}, [der]{15} [deinen]{17,19} [Weg]{18} [vor]{20} [dir]{21} [bereiten wird]{16}.›",
 "MAT.11.11": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Unter]{6} [denen, die von Frauen geboren sind]{7,8}, [ist]{5} [kein Grösserer]{4,9} [aufgetreten]{5} [als Johannes]{10} [der]{11} [Täufer]{12}; [der]{13} [Kleinste]{15} [aber]{14} [im]{16,17} [Reich]{18} [der Himmel]{19,20} [ist]{23} [grösser]{21} [als er]{22}.",
 "MAT.11.12": "[Seit]{1} [den Tagen]{3,4} [Johannes']{5} [des]{6} [Täufers]{7} [aber]{2} [bis]{8} [jetzt]{9} [leidet]{14} [das Reich]{10,11} [der Himmel]{12,13} [Gewalt]{14}, und{15} [Gewalttätige]{16} [reissen]{17} [es]{18} [an sich]{17}.",
 "MAT.11.13": "[Denn]{2} [alle]{1} [Propheten]{3,4} und{5} [das Gesetz]{6,7} [haben]{10} [bis]{8} [auf Johannes]{9} [prophezeit]{10};",
 "MAT.11.14": "und{1} [wenn]{2} ihr es [annehmen]{4} [wollt]{3}: [Er]{5} [ist]{6} [Elija]{7}, [der]{8} [kommen]{10} [soll]{9}.",
 "MAT.11.15": "[Wer]{1} [Ohren]{3} [hat]{2}, [der höre]{4}!",
 "MAT.11.16": "[Womit]{1} [aber]{2} [soll ich]{3} [dieses]{4,6} [Geschlecht]{5} [vergleichen]{3}? Es [ist]{8} [Kindern]{9} [gleich]{7}, [die]{10} [auf]{11} [den]{12} [Marktplätzen]{13} [sitzen]{10} und [den]{16} [anderen]{17} [zurufen]{15} ~14(ἅ «die» nimmt «Kindern» auf; durch «und» angeschlossen)",
 "MAT.11.17": "und [sagen]{1}: ‹[Wir haben]{2} [euch]{3} [auf der Flöte gespielt]{2}, und{4} [ihr habt]{6} [nicht]{5} [getanzt]{6}; [wir haben]{7} [Klagelieder gesungen]{7}, und{8} [ihr habt]{10} euch [nicht]{9} [an die Brust geschlagen]{10}.›",
 "MAT.11.18": "[Denn]{2} [Johannes]{3} [ist gekommen]{1}, [ohne]{4} [zu essen]{5} [und ohne]{6} [zu trinken]{7}, und{8} [sie sagen]{9}: ‹[Er hat]{11} [einen Dämon]{10}.›",
 "MAT.11.19": "[Der Menschensohn]{2-5} [ist gekommen]{1}, [er isst]{6} und{7} [trinkt]{8}, und{9} [sie sagen]{10}: ‹[Siehe]{11}, [was für ein Mensch]{12}: [ein Fresser]{13} und{14} [Weinsäufer]{15}, [ein Freund]{17} [von Zöllnern]{16} und{18} [Sündern]{19}!› Und{20} [die Weisheit]{22,23} [ist]{21} [durch]{24} [ihre]{27} [Werke]{25,26} [gerechtfertigt worden]{21}.»",
 "MAT.11.20": "[Da]{1} [begann er]{2}, [die Städte]{4,5} [zu schelten]{3}, [in]{6} [denen]{7} [die meisten]{9,10} [seiner]{12} [Machttaten]{11} [geschehen waren]{8}, [weil]{13} sie [nicht]{14} [umgekehrt waren]{15}:",
 "MAT.11.21": "«[Wehe]{1} [dir]{2}, [Chorazin]{3}! [Wehe]{4} [dir]{5}, [Betsaida]{6}! [Denn]{7} [wenn]{8} [in]{9} [Tyrus]{10} und{11} [Sidon]{12} [die]{14} [Machttaten]{15} [geschehen wären]{13}, [die]{16} [bei]{18} [euch]{19} [geschehen sind]{17}, [sie wären]{21,26} [längst]{20} [in]{22} [Sack]{23} und{24} [Asche]{25} [umgekehrt]{21,26}.",
 "MAT.11.22": "[Doch]{1} [ich sage]{2} [euch]{3}: [Tyrus]{4} und{5} [Sidon]{6} [wird es]{8} [am]{9} [Tag]{10} [des Gerichts]{11} [erträglicher]{7} [ergehen]{8} [als]{12} [euch]{13}.",
 "MAT.11.23": "Und{1} [du]{2}, [Kafarnaum]{3}, [wirst du]{7} [etwa]{4} [bis]{5} [zum Himmel]{6} [erhöht werden]{7}? [Bis]{8} [ins Totenreich]{9} [wirst du hinabsteigen]{10}. [Denn]{11} [wenn]{12} [in]{13} [Sodom]{14} [die]{16} [Machttaten]{17} [geschehen wären]{15}, [die]{18} [bei]{20} [dir]{21} [geschehen sind]{19}, [es wäre]{22,23} [bis]{24} [auf den heutigen Tag]{25,26} [stehen geblieben]{22,23}.",
 "MAT.11.24": "[Doch]{1} [ich sage]{2} [euch]{3}: [Dem Land]{5} [Sodom]{6} [wird es]{8} [am]{9} [Tag]{10} [des Gerichts]{11} [erträglicher]{7} [ergehen]{8} [als]{12} [dir]{13}.» ~4(ὅτι leitet die direkte Rede ein)",
 "MAT.11.25": "[Zu]{1} [jener]{2,3} [Zeit]{4} [ergriff]{5} [Jesus]{6,7} [das Wort]{5} und [sagte]{8}: «[Ich preise]{9} [dich]{10}, [Vater]{11}, [Herr]{12} [des Himmels]{13,14} und{15} [der Erde]{16,17}, [dass]{18} [du]{19} [dies]{20} [vor]{21} [Weisen]{22} und{23} [Verständigen]{24} [verborgen hast]{19} und{25} [es]{27} [Unmündigen]{28} [offenbart hast]{26}.",
 "MAT.11.26": "[Ja]{1}, [Vater]{2,3}, [denn]{4} [so]{5} [hat es]{7} [dir]{8,9} [gefallen]{6}.",
 "MAT.11.27": "[Alles]{1} [ist]{3} [mir]{2} [von]{4} [meinem]{5,7} [Vater]{6} [übergeben worden]{3}, und{8} [niemand]{9} [kennt]{10} [den Sohn]{11,12} [ausser]{13,14} [der Vater]{15,16}, [noch]{17} [kennt]{21} [jemand]{20} [den Vater]{18,19} [ausser]{22,23} [der Sohn]{24,25} und{26} [jeder, dem]{27,28} [der Sohn]{30,31} es [offenbaren]{32} [will]{29}.",
 "MAT.11.28": "[Kommt her]{1} [zu]{2} [mir]{3}, [alle]{4}, [die]{5} ihr [euch abmüht]{6} und{7} [beladen seid]{8}, [und ich]{9} [werde]{10} [euch]{11} [Ruhe geben]{10}.",
 "MAT.11.29": "[Nehmt]{1} [mein]{2,4} [Joch]{3} [auf]{5} [euch]{6} und{7} [lernt]{8} [von]{9} [mir]{10}, [denn]{11} [ich bin]{13} [sanftmütig]{12} und{14} [demütig]{15} [im Herzen]{16,17}, und{18} [ihr werdet]{19} [Ruhe]{20} [finden]{19} [für]{21} [eure]{23} [Seelen]{22}.",
 "MAT.11.30": "[Denn]{2} [mein]{1,4} [Joch]{3} ist [sanft]{5}, und{6} [meine]{7,9} [Last]{8} [ist]{11} [leicht]{10}.»",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 10
 "MAT.10.1": "Und{1} [er hät]{2} [sini]{6} [zwölf]{3,4} [Jünger]{5} [zu sich grüeft]{2} und [hät]{7} [ine]{8} [Vollmacht]{9} über [unreini]{11} [Geischter]{10} [ggää]{7}, [für]{12} [si]{14} [usztriibe]{13} und{15} [jedi]{17} [Chrankheit]{18} und{19} [jedes]{20} [Gebräche]{21} [z heile]{16}.",
 "MAT.10.2": "[D Näme]{5,6} [vo de]{1} [zwölf]{3} [Apostel]{4} [aber]{2} [sind]{7} [die]{8}: [zerscht]{9} [de Simon]{10}, [wo]{11} [Petrus]{13} [gnännt wird]{12}, und{14} [de Andreas]{15}, [sin]{18} [Brueder]{16,17}, [de Jakobus]{19}, [de Sohn]{20} [vom]{21} [Zebedäus]{22}, und{23} [de Johannes]{24}, [sin]{27} [Brueder]{25,26},",
 "MAT.10.3": "[de Philippus]{1} und{2} [de Bartholomäus]{3}, [de Thomas]{4} und{5} [de Matthäus]{6}, [de]{7} [Zöllner]{8}, [de Jakobus]{9}, [de Sohn]{10} [vom]{11} [Alphäus]{12}, und{13} [de Thaddäus]{14},",
 "MAT.10.4": "[de Simon]{1}, [de]{2} [Kananäer]{3}, und{4} [de Judas]{5} [Iskariot]{6,7}, [wo]{8} [en]{11} [au]{9} [usgliferet hät]{10}.",
 "MAT.10.5": "[Die]{1} [Zwölf]{2,3} [hät]{4} [de Jesus]{5,6} [usgschickt]{4} und [ine]{8} [befole]{7}: «[Gönd]{14} [nöd]{13} [uf]{10} [en Wäg]{11} [zu de Heide]{12}, [und]{15} [gönd]{20} [i]{16} [kei]{19} [Stadt]{17} [vo de Samaritaner]{18} [ine]{20}! ~9(λέγων «sägend» leitet di diräkt Red ii)",
 "MAT.10.6": "[Gönd]{1} [vilmeh]{3} [zu]{4} [de]{5} [verlorene]{7,8} [Schaf]{6} [vom Huus]{9} [Israel]{10}! ~2(δέ verbindet mit em Vorige; mit «vilmeh» usdrückt)",
 "MAT.10.7": "[Underwägs]{1} [aber]{2} [verchünded]{3} und [säged]{4}: ‹[S Riich]{7,8} [vo de Himel]{9,10} [isch nöch choo]{6}.› ~5(ὅτι leitet di diräkt Red ii)",
 "MAT.10.8": "[Heiled]{2} [Chranki]{1}, [wecked]{4} [Toti]{3} [uf]{4}, [mached]{6} [Ussätzigi]{5} [rein]{6}, [triibed]{8} [Dämone]{7} [us]{8}! [Umesuscht]{9} [händ ir übercho]{10}, [umesuscht]{11} [gänd]{12}!",
 "MAT.10.9": "[Schaffed eu]{2} [kei]{1} [Gold]{3}, [kei]{4} [Silber]{5} [und kei]{6} [Chupfergäld]{7} [für]{8} [eui]{11} [Gürtel]{9,10} [aa]{2},",
 "MAT.10.10": "[kei]{1} [Täsche]{2} [für]{3} [de Wäg]{4}, [nöd]{5} [zwei]{6} [Underchleider]{7}, [kei]{8} [Sandale]{9} [und kei]{10} [Stäcke]{11}; [de]{14} [Arbeiter]{15} isch [nämli]{13} [sis]{18} [Ässe]{16,17} [wärt]{12}.",
 "MAT.10.11": "[I]{1} [weli]{2} [Stadt]{5} [oder]{6} [weles Dorf]{7} [ir]{8} [aber]{3} [au]{4} [chömed]{8}, [fröged nache]{9}, [wer]{10} [i]{11} [ire]{12} [wärt]{13} [isch]{14}; [und dört]{15} [bliibed]{16}, [bis]{17,18} [ir wiiterziehnd]{19}.",
 "MAT.10.12": "[Wänn ir]{1} [aber]{2} [is]{3,4} [Huus]{5} [inegönd]{1}, [grüessed]{6} [d Lüüt drin]{7}.",
 "MAT.10.13": "Und{1} [wänn]{2} [s Huus]{5,6} es [wärt]{7} [isch]{4}, [söll]{8} [eue]{11} [Fride]{9,10} [druf]{12,13} [choo]{8}; [wänn]{14} s [aber]{15} [nöd]{16} [wärt]{18} [isch]{17}, [söll]{24} [eue]{21} [Fride]{19,20} [zu]{22} [eu]{23} [zruggchoo]{24}. ~3(μέν bildet mit δέ es Gägesatzpaar; nöd eigens widergää)",
 "MAT.10.14": "Und{1} [wer]{2,3} [eu]{6} [nöd]{4} [ufnimmt]{5} [und nöd]{7} uf [eui]{11} [Wort]{9,10} [lost]{8}, [gönd]{12} [use]{13} us [em Huus]{14,15} [oder]{16} us [dere]{19} [Stadt]{17,18} und [schüttled]{20} [de Staub]{21,22} vo [eune]{25} [Füess]{23,24} [ab]{20}.",
 "MAT.10.15": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Em Land]{6} [Sodom]{7} und{8} [Gomorra]{9} [wird s]{5} [am]{10} [Tag]{11} [vom Gricht]{12} [erträglicher]{4} [gaa]{5} [als]{13} [dere]{16} [Stadt]{14,15}.",
 "MAT.10.16": "[Lueg]{1}, [ich]{2} [schicke]{3} [eu]{4} [wie]{5} [Schaf]{6} [mitten]{7,8} under [Wölf]{9}; [sind]{10} [also]{11} [gschiid]{12} [wie]{13} [d]{14} [Schlange]{15} und{16} [ohni Falsch]{17} [wie]{18} [d]{19} [Tuube]{20}.",
 "MAT.10.17": "[Hüeted eu]{1} [aber]{2} [vor]{3} [de]{4} [Mänsche]{5}; [si wärded]{6} [eu]{8} [nämli]{7} [a]{9} [Gricht]{10} [uslifere]{6}, und{11} [i]{12} [ire]{15} [Synagoge]{13,14} [wärded si]{16} [eu]{17} [geissle]{16},",
 "MAT.10.18": "[und]{1} [au]{4} [vor]{2} [Statthalter]{3} und{5} [Könige]{6} [wärded ir gfüert]{7} [wäge mir]{8,9}, [ine]{12} [und]{13} [de Heide]{14,15} [zum]{10} [Züügnis]{11}.",
 "MAT.10.19": "[Wänn]{1} [si]{3} [eu]{4} [aber]{2} [uslifered]{3}, [mached eu]{6} [kei]{5} [Sorge]{6}, [wie]{7} [oder]{8} [was]{9} [ir rede söled]{10}; [es wird]{11} [eu]{13} [nämli]{12} [i]{14} [dere]{15,16} [Stund]{17} [ggää]{11}, [was]{18} [ir rede söled]{19}.",
 "MAT.10.20": "[Nöd]{1} [ir]{3} [sind s]{4} [nämli]{2}, [wo]{5} [reded]{6}, [sondern]{7} [de Geischt]{8,9} vo [eurem]{12} [Vatter]{10,11} isch es, [wo]{13} [i]{15} [eu]{16} [redt]{14}.",
 "MAT.10.21": "[Es wird]{1} [aber]{2} [en Brueder]{3} [de Brueder]{4} [in]{5} [Tod]{6} [uslifere]{1} und{7} [en Vatter]{8} [s Chind]{9}, und{10} [Chind]{12} [wärded sich]{11} [gäge]{13} [d Eltere]{14} [ufläne]{11} und{15} [si]{17} [in Tod bringe]{16}.",
 "MAT.10.22": "Und{1} [ir wärded]{2} [vo]{4} [allne]{5} [ghasst sii]{3} [wäge]{6} [mim]{9} [Name]{7,8}. [Wer]{10} [aber]{11} [bis]{13} [as Änd]{14} [durehebt]{12}, [dä]{15} [wird grettet]{16}.",
 "MAT.10.23": "[Wänn]{1} [si]{3} [eu]{4} [aber]{2} [i]{5} [dere]{6,8} [Stadt]{7} [verfolged]{3}, [flüchted]{9} [i]{10} [di]{11} [ander]{12}. [Amen]{13}, [ich säg]{15} [eu]{16} [nämli]{14}: [Ir wärded]{19} mit [de Stedt]{20,21} [vo Israel]{22,23} [sicher nöd]{17,18} [fertig]{19}, [bis]{24,25} [de Mänschesohn]{27-30} [chunnt]{26}.",
 "MAT.10.24": "[En Jünger]{3} [staat]{2} [nöd]{1} [über]{4} [em]{5} [Lehrer]{6} [und kei]{7} [Chnächt]{8} [über]{9} [sim]{10,12} [Herr]{11}.",
 "MAT.10.25": "[Es länget]{1} [em]{2} [Jünger]{3}, [dass]{4} er [wie]{6} [sin]{7,9} [Lehrer]{8} [wird]{5}, und{10} [de]{11} [Chnächt]{12} [wie]{13} [sin]{14,16} [Herr]{15}. [Wänn]{17} si [de]{18} [Huusherr]{19} [Beelzebul]{20} [gnännt händ]{21}, [wie vil meh]{22,23} [sini]{26} [Huusgnosse]{24,25}!",
 "MAT.10.26": "[Förchted]{3} [si]{4} [also]{2} [nöd]{1}! [Es isch]{7} [nämli]{6} [nüüt]{5} [verdeckt]{8}, [wo]{9} [nöd]{10} [ufdeckt wird]{11}, und{12} nüüt [verborge]{13}, [wo]{14} [nöd]{15} [bekannt wird]{16}.",
 "MAT.10.27": "[Was]{1} [ich]{2} [eu]{3} [i]{4} [de Fiischteri]{5,6} [säg]{2}, [das säged]{7} [im]{8,9} [Liecht]{10}; und{11} [was]{12} [ir]{16} [is]{13,14} [Ohr]{15} gflüschteret [ghöred]{16}, [das verchünded]{17} [uf]{18} [de]{19} [Dächer]{20}.",
 "MAT.10.28": "Und{1} [förchted eu]{3} [nöd]{2} [vor]{4} [dene]{5}, [wo]{6} [de Liib]{7,8} [töded]{6}, [d Seel]{9,11} [aber]{10} [nöd]{12} [töde]{14} [chönd]{13}; [förchted eu]{15} [aber]{16} [vilmeh]{17} vor [däm]{18}, [wo]{19} [d Seel]{21} [und]{22} [de Liib]{23} [i]{25} [de Höll]{26} [cha]{19} [zgrund richte]{24}. ~20(καί … καί «sowohl … als au»: s erscht καί nöd eigens widergää)",
 "MAT.10.29": "[Wärded]{5} [nöd]{1} [zwei]{2} [Spatze]{3} [für en Batze]{4} [verchauft]{5}? Und{6} [nöd]{10} [eine]{7} [vo]{8} [ine]{9} [gheit]{11} [uf]{12} [de Bode]{13,14} [ohni]{15} [eue]{18} [Vatter]{16,17}.",
 "MAT.10.30": "[Bi eu]{1} [aber]{2} [sind]{10} [sogar]{3} [d]{4} [Haar]{5} [uf em Chopf]{6,7} [alli]{8} [zellt]{9}.",
 "MAT.10.31": "[Förchted eu]{3} [also]{2} [nöd]{1}! [Ir]{7} [sind]{6} [meh wärt]{6} [als vil]{4} [Spatze]{5}.",
 "MAT.10.32": "[Jede]{1} [also]{2}, [wo]{3} sich [vor]{7} [de]{8} [Mänsche]{9} [zu]{5} [mir]{6} [bekännt]{4}, [zu]{12} [däm]{13} [wird]{10} [au ich]{11} mich [bekänne]{10} [vor]{14} [mim]{15,17} [Vatter]{16} [i]{18,19} [de Himel]{20};",
 "MAT.10.33": "[wer]{1,3} [mich]{5} [aber]{2} [vor]{6} [de]{7} [Mänsche]{8} [verleugnet]{4}, [dä]{11} [wird]{9} [au ich]{10} [verleugne]{9} [vor]{12} [mim]{13,15} [Vatter]{14} [i]{16,17} [de Himel]{18}.",
 "MAT.10.34": "[Meined]{2} [nöd]{1}, [dass]{3} [ich choo bi]{4}, für [Fride]{6} [uf]{7} [d Ärde]{8,9} [z bringe]{5}! [Ich bi]{11} [nöd]{10} [choo]{11}, für [Fride]{13} [z bringe]{12}, [sondern]{14} [es Schwärt]{15}.",
 "MAT.10.35": "[Ich bi]{1} [nämli]{2} [choo]{1}, für [en Mänsch]{4} [mit]{5} [sim]{6,8} [Vatter]{7} [z entzweie]{3} und{9} [e Tochter]{10} [mit]{11} [irer]{12,14} [Mueter]{13} und{15} [e Schwigertochter]{16} [mit]{17} [irer]{18,20} [Schwigermueter]{19},",
 "MAT.10.36": "und{1} [d Fiind]{2} [vom Mänsch]{3,4} wärded [sini]{7} [Huusgnosse]{5,6} sii.",
 "MAT.10.37": "[Wer]{1} [Vatter]{3} [oder]{4} [Mueter]{5} [meh]{6} [gärn hät]{2} [als mich]{7}, [isch]{9} [mich]{10} [nöd]{8} [wärt]{11}; und{12} [wer]{13} [Sohn]{15} [oder]{16} [Tochter]{17} [meh]{18} [gärn hät]{14} [als mich]{19}, [isch]{21} [mich]{22} [nöd]{20} [wärt]{23};",
 "MAT.10.38": "und{1} [wer]{2} [sis]{5,7} [Chrüüz]{6} [nöd]{3} [uf sich nimmt]{4} und{8} [mir]{11} [nachefolget]{9,10}, [isch]{13} [mich]{14} [nöd]{12} [wärt]{15}.",
 "MAT.10.39": "[Wer]{1} [sis]{3,5} [Läbe]{4} [gfunde hät]{2}, [wird]{6} [s]{7} [verlüüre]{6}, und{8} [wer]{9} [sis]{11,13} [Läbe]{12} [wäge mir]{14,15} [verloore hät]{10}, [wird]{16} [s]{17} [finde]{16}.",
 "MAT.10.40": "[Wer]{1} [eu]{3} [ufnimmt]{2}, [nimmt]{5} [mich]{4} [uf]{5}; und{6} [wer]{7} [mich]{8} [ufnimmt]{9}, [nimmt]{10} [dä]{11} [uf]{10}, [wo]{12} [mich]{13} [gschickt hät]{12}.",
 "MAT.10.41": "[Wer]{1} [en Prophet]{3} [ufnimmt]{2}, [wil er en Prophet isch]{4-6:idiom}, [wird]{9} [de Loon]{7} [vo me Prophet]{8} [übercho]{9}; und{10} [wer]{11} [en Grächte]{13} [ufnimmt]{12}, [wil er en Grächte isch]{14-16:idiom}, [wird]{19} [de Loon]{17} [vo me Grächte]{18} [übercho]{19}.",
 "MAT.10.42": "Und{1} [wer]{2,3} [eim]{5} [vo dene]{6,8} [Chliine]{7} au [nu]{11} [en Bächer]{9} [chalts Wasser]{10} [z trinke git]{4}, [wil er en Jünger isch]{12-14:idiom} – [Amen]{15}, [ich säg]{16} [eu]{17}: [Dä wird]{20} [sin]{21,23} [Loon]{22} [sicher nöd]{18,19} [verlüüre]{20}.»",
 # ------------------------------------------------------------ Kapitel 11
 "MAT.11.1": "Und{1} [wo]{3} [de Jesus]{5,6} [mit de Aawiisige]{7} [a]{8} [sini]{11} [zwölf]{9} [Jünger]{10} [fertig gsii isch]{4}, [isch er]{12} [vo dört]{13} [wiiterzoge]{12}, [für]{14} [i]{18} [ire]{21} [Stedt]{19,20} [z lehre]{15} und{16} [z verchünde]{17}. ~2(ἐγένετο «es isch gscheh» leitet d Erzählig ii; i de Mundart nöd eigens widergää)",
 "MAT.11.2": "Wo [de Johannes]{1,3} [aber]{2} [im]{5,6} [Gfängnis]{7} [vo de Wärch]{8,9} [vom Christus]{10,11} [ghört hät]{4}, [hät er]{12} [sini]{14,16} [Jünger]{15} [gschickt]{12} ~13(διά «dur»: d Jünger sind d Bote; mit «gschickt» usdrückt)",
 "MAT.11.3": "und hät [ihm]{2} [la säge]{1}: «[Bisch]{4} [du]{3} [dä]{5}, [wo chunnt]{6}, [oder]{7} [söled mir]{9} [uf en andere]{8} [warte]{9}?»",
 "MAT.11.4": "Und{1} [de Jesus]{3,4} [hät gantwortet]{2} und [zu ine]{6} [gseit]{5}: «[Gönd]{7} und [verzelled]{8} [em Johannes]{9}, [was]{10} [ir ghöred]{11} und{12} [gseend]{13}:",
 "MAT.11.5": "[Blindi]{1} [gseend wider]{2}, und{3} [Lahmi]{4} [laufed]{5}, [Ussätzigi]{6} [wärded rein]{7}, und{8} [Taubi]{9} [ghöred]{10}, und{11} [Toti]{12} [wärded uferweckt]{13}, und{14} [de Arme]{15} [wird s Evangelium verchündet]{16};",
 "MAT.11.6": "und{1} [sälig]{2} [isch]{3}, [wer]{4,5} [a]{8} [mir]{9} [kei]{6} [Aastoss nimmt]{7}.»",
 "MAT.11.7": "Wo [die]{1} [aber]{2} [furtgange sind]{3}, [hät]{4} [de Jesus]{5,6} [aagfange]{4}, [zu de Mängi]{8,9} [über]{10} [de Johannes]{11} [z rede]{7}: «[Was]{12} [sind ir]{13} [i]{14} [d Wüeschti]{15,16} [usegange]{13} [go luege]{17}? [Es Schilfrohr]{18}, wo [vom]{19} [Wind]{20} [hin und här gschüttlet wird]{21}?",
 "MAT.11.8": "[Oder]{1} [was]{2} [sind ir usegange]{3} [go luege]{4}? [En Mänsch]{5}, [i]{6} [weichi Chleider]{7} [aagleit]{8}? [Lueg]{9}, [die]{10}, wo [weichi Chleider]{11,12} [träged]{13}, [sind]{19} [i]{14} [de]{15} [Hüüser]{16} [vo de Könige]{17,18}.",
 "MAT.11.9": "[Oder]{1} [was]{2} [sind ir usegange]{3}? [En Prophet]{4} [go luege]{5}? [Ja]{6}, [ich säg]{7} [eu]{8}: [sogar]{9} [meh]{10} [als en Prophet]{11}.",
 "MAT.11.10": "[Dä]{1} [isch es]{2}, [vo]{3} [däm]{4} [gschribe staat]{5}: ‹[Lueg]{6}, [ich]{7} [schicke]{8} [min]{9,11} [Bote]{10} [vor]{12,13} [dir]{14} [här]{12,13}, [wo]{15} [din]{17,19} [Wäg]{18} [vor]{20} [dir]{21} [wird parat mache]{16}.›",
 "MAT.11.11": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Under]{6} [dene, wo vo Fraue gebore sind]{7,8}, [isch]{5} [kei Grössere]{4,9} [uftrete]{5} [als de Johannes]{10} [de]{11} [Täufer]{12}; [de]{13} [Chliinscht]{15} [aber]{14} [im]{16,17} [Riich]{18} [vo de Himel]{19,20} [isch]{23} [grösser]{21} [als er]{22}.",
 "MAT.11.12": "[Sit]{1} [de Täg]{3,4} [vom Johannes]{5}, [em]{6} [Täufer]{7}, [aber]{2} [bis]{8} [jetzt]{9} [tuet me]{14} [em Riich]{10,11} [vo de Himel]{12,13} [Gwalt aa]{14}, und{15} [Gwalttätigi]{16} [riissed]{17} [s]{18} [a sich]{17}.",
 "MAT.11.13": "[Alli]{1} [Prophete]{3,4} und{5} [s Gsetz]{6,7} [händ]{10} [nämli]{2} [bis]{8} [zum Johannes]{9} [prophezeit]{10};",
 "MAT.11.14": "und{1} [wänn]{2} ir s [wänd]{3} [aanää]{4}: [Er]{5} [isch]{6} [de Elija]{7}, [wo]{8} [söll]{9} [choo]{10}.",
 "MAT.11.15": "[Wer]{1} [Ohre]{3} [hät]{2}, [dä söll lose]{4}!",
 "MAT.11.16": "[Mit was]{1} [aber]{2} [söll ich]{3} [die]{4,6} [Generation]{5} [vergliiche]{3}? Si [isch]{8} [wie]{7} [Chind]{9}, [wo]{10} [uf]{11} [de]{12} [Märt]{13} [sitzed]{10} und [de]{16} [andere]{17} [zuerüefed]{15} ~14(ἅ «wo» nimmt «Chind» uf; mit «und» aagschlosse)",
 "MAT.11.17": "und [säged]{1}: ‹[Mir händ]{2} [eu]{3} [uf de Flöte gspilt]{2}, und{4} [ir händ]{6} [nöd]{5} [tanzet]{6}; [mir händ]{7} [Klaglieder gsunge]{7}, und{8} [ir händ]{10} eu [nöd]{9} [a d Bruscht gschlage]{10}.›",
 "MAT.11.18": "[De Johannes]{3} [isch]{1} [nämli]{2} [choo]{1}, [ohni]{4} [z ässe]{5} [und ohni]{6} [z trinke]{7}, und{8} [si säged]{9}: ‹[Er hät]{11} [en Dämon]{10}.›",
 "MAT.11.19": "[De Mänschesohn]{2-5} [isch choo]{1}, [er isst]{6} und{7} [trinkt]{8}, und{9} [si säged]{10}: ‹[Lueg]{11}, [was für en Mänsch]{12}: [en Frässer]{13} und{14} [Süffel]{15}, [en Fründ]{17} [vo Zöllner]{16} und{18} [Sünder]{19}!› Und{20} [d Wiisheit]{22,23} [isch]{21} [dur]{24} [iri]{27} [Wärch]{25,26} [is Rächt gsetzt worde]{21}.»",
 "MAT.11.20": "[Dänn]{1} [hät er aagfange]{2}, [d Stedt]{4,5} [uszschimpfe]{3}, [i]{6} [dene]{7} [di meischte]{9,10} [vo sine]{12} [Chrafttate]{11} [passiert sind]{8}, [wil]{13} si [nöd]{14} [umgchehrt sind]{15}:",
 "MAT.11.21": "«[Wee]{1} [dir]{2}, [Chorazin]{3}! [Wee]{4} [dir]{5}, [Betsaida]{6}! [Wänn]{8} [nämli]{7} [z]{9} [Tyrus]{10} und{11} [Sidon]{12} [d]{14} [Chrafttate]{15} [passiert wäred]{13}, [wo]{16} [bi]{18} [eu]{19} [passiert sind]{17}, [wäred si]{21,26} [scho lang]{20} [in]{22} [Sack]{23} und{24} [Äsche]{25} [umgchehrt]{21,26}.",
 "MAT.11.22": "[Aber]{1} [ich säg]{2} [eu]{3}: [Tyrus]{4} und{5} [Sidon]{6} [wird s]{8} [am]{9} [Tag]{10} [vom Gricht]{11} [erträglicher]{7} [gaa]{8} [als]{12} [eu]{13}.",
 "MAT.11.23": "Und{1} [du]{2}, [Kafarnaum]{3}, [wirsch]{7} [öppe]{4} [bis]{5} [in Himel]{6} [erhöcht wärde]{7}? [Bis]{8} [is Toterich]{9} [wirsch abestiige]{10}. [Wänn]{12} [nämli]{11} [z]{13} [Sodom]{14} [d]{16} [Chrafttate]{17} [passiert wäred]{15}, [wo]{18} [bi]{20} [dir]{21} [passiert sind]{19}, [wär s]{22,23} [bis]{24} [hüt]{25,26} [staa bliibe]{22,23}.",
 "MAT.11.24": "[Aber]{1} [ich säg]{2} [eu]{3}: [Em Land]{5} [Sodom]{6} [wird s]{8} [am]{9} [Tag]{10} [vom Gricht]{11} [erträglicher]{7} [gaa]{8} [als]{12} [dir]{13}.» ~4(ὅτι leitet di diräkt Red ii)",
 "MAT.11.25": "[I]{1} [dere]{2,3} [Ziit]{4} [hät]{8} [de Jesus]{6,7} [gseit]{8}: «[Ich priise]{9} [dich]{10}, [Vatter]{11}, [Herr]{12} [vom Himel]{13,14} und{15} [vo de Ärde]{16,17}, [dass]{18} [du]{19} [das]{20} [vor]{21} [Wiise]{22} und{23} [Verständige]{24} [verborge häsch]{19} und{25} [es]{27} [de Unmündige]{28} [offebart häsch]{26}. ~5(ἀποκριθείς «antwortend», obwohl kei Frag vorusgaat; nöd eigens widergää)",
 "MAT.11.26": "[Ja]{1}, [Vatter]{2,3}, [wil]{4} s [dir]{8,9} [eso]{5} [gfalle hät]{6,7}.",
 "MAT.11.27": "[Alles]{1} [isch]{3} [mir]{2} [vo]{4} [mim]{5,7} [Vatter]{6} [übergää worde]{3}, und{8} [niemer]{9} [kännt]{10} [de Sohn]{11,12} [usser]{13,14} [de Vatter]{15,16}, [und au]{17} [de Vatter]{18,19} [kännt]{21} [niemer]{20} [usser]{22,23} [de Sohn]{24,25} und{26} [jede, wo]{27,28} [de Sohn]{30,31} em s [wott]{29} [offebare]{32}.",
 "MAT.11.28": "[Chömed]{1} [zu]{2} [mir]{3}, [alli]{4}, [wo]{5} [sich abmüehed]{6} und{7} [schwär z träge händ]{8}, [und ich]{9} [gib]{10} [eu]{11} [Rue]{10}.",
 "MAT.11.29": "[Nämed]{1} [mis]{2,4} [Joch]{3} [uf]{5} [eu]{6} und{7} [lerned]{8} [vo]{9} [mir]{10}, [wil]{11} [ich]{13} [sanftmüetig]{12} und{14} [demüetig]{15} [im Härz]{16,17} [bi]{13}, und{18} [ir wärded]{19} [Rue]{20} [finde]{19} [für]{21} [eui]{23} [Seele]{22}.",
 "MAT.11.30": "[Mis]{1,4} [Joch]{3} isch [nämli]{2} [sanft]{5}, und{6} [mini]{7,9} [Lascht]{8} [isch]{11} [liecht]{10}.»",
}


# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MAT.10.1", "Vollmacht über unreine Geister", "literal", "ἐξουσίαν πνευμάτων ἀκαθάρτων", "Vollmacht unreiner Geister", ["Macht über unreine Geister"],
  "Der Genitiv bezeichnet, worüber die Vollmacht reicht; ebenso [[MRK.6.7]]. ἐξουσία durchgehend «Vollmacht» (vgl. [[MAT.7.29]], [[MAT.9.6]])."),
 ("MAT.10.1", "jede Krankheit und jedes Gebrechen", "literal", "πᾶσαν νόσον καὶ πᾶσαν μαλακίαν", None, ["jede Krankheit und jedes Leiden", "jede Krankheit und jede Schwäche"],
  "Feste Wendung des Matthäus ([[MAT.4.23]], [[MAT.9.35]], [[MAT.10.1]]); μαλακία heisst wörtlich «Schwäche, Schwachheit». Für alle drei Stellen wird «jede Krankheit und jedes Gebrechen» vorgeschlagen."),
 ("MAT.10.2", "Apostel", "traditional", "ἀποστόλων", None, ["Gesandten", "Abgesandten"],
  "Das Wort steht bei Matthäus nur hier. Es gehört zum Verb ἀποστέλλω «aussenden» ([[MAT.10.5]], [[MAT.10.16]], [[MAT.10.40]]): Die Zwölf sind Gesandte Jesu. Der eingebürgerte Titel ist beibehalten."),
 ("MAT.10.2", "zuerst", "interpretive", "πρῶτος", "als Erster", ["der Erste", "an erster Stelle"],
  "πρῶτος kann die Reihenfolge der Liste meinen oder einen Vorrang des Simon andeuten (vgl. [[MAT.16.18]]); «zuerst» lässt beides offen. Nur Matthäus setzt das Wort in die Liste."),
 ("MAT.10.3", "Matthäus, der Zöllner", "literal", "Μαθθαῖος ὁ τελώνης", None, ["Matthäus, der Zolleinnehmer"],
  "Nur Matthäus fügt der Liste den Beruf hinzu; vgl. die Berufung des Zöllners Matthäus [[MAT.9.9]]. «Zöllner» bezeichnet einen Pächter oder Angestellten der Zoll- und Abgabenerhebung."),
 ("MAT.10.4", "Kananäer", "interpretive", "Καναναῖος", None, ["Eiferer", "Zelot"],
  "Καναναῖος gibt wohl ein aramäisches Wort für «Eiferer» wieder; [[LUK.6.15]] nennt denselben Simon ζηλωτής («Zelot, Eiferer»). Mit dem Volk der Kanaaniter oder dem Ort Kana hat der Beiname nach verbreitetem Urteil nichts zu tun. Die Umschrift folgt [[MRK.3.18]]."),
 ("MAT.10.4", "der ihn auch auslieferte", "literal", "ὁ καὶ παραδοὺς αὐτόν", None, ["der ihn auch verriet"],
  "παραδίδωμι wird wie bei Markus mit «ausliefern» wiedergegeben, auch in [[MAT.10.17]], [[MAT.10.19]] und [[MAT.10.21]], wo es um die Auslieferung der Jünger geht; «verraten» engt auf den Treuebruch ein. In [[MAT.11.27]] steht dasselbe Verb für das Übergeben durch den Vater («übergeben»)."),
 ("MAT.10.5", "zu den Heiden", "interpretive", "ἐθνῶν", "der Völker", ["der Nichtjuden", "der Völker"],
  "τὰ ἔθνη meint hier die nichtjüdischen Völker im Gegensatz zu Israel ([[MAT.10.6]]); «Weg der Heiden» ist ein Weg in nichtjüdisches Gebiet. Ebenso [[MAT.10.18]]. «Heiden» hat im Deutschen keinen abwertenden Sinn beabsichtigt; im missionarischen Schluss des Evangeliums ([[MAT.28.19]]) ist dasselbe Wort mit «Völker» zu übersetzen."),
 ("MAT.10.6", "den verlorenen Schafen des Hauses Israel", "interpretive", "τὰ πρόβατα τὰ ἀπολωλότα οἴκου Ἰσραήλ", None, ["den verlorenen Schafen, nämlich dem Haus Israel", "den Verlorenen unter dem Haus Israel"],
  "Der Genitiv kann das ganze Volk als «verlorene Schafe» bezeichnen oder die Verlorenen innerhalb Israels hervorheben; beides wird vertreten. Vgl. [[MAT.15.24]] und [[MAT.9.36]] (Schafe ohne Hirten). Die Beschränkung auf Israel gilt für diese Aussendung; [[MAT.28.19]] weitet den Auftrag auf alle Völker aus."),
 ("MAT.10.7", "Das Reich der Himmel", "traditional", "ἡ βασιλεία τῶν οὐρανῶν", None, ["das Himmelreich", "die Herrschaft der Himmel"],
  "Einheitliche Wiedergabe für das Matthäusevangelium (siehe translation_notes). Matthäus sagt meist «Reich der Himmel», wo Markus «Reich Gottes» hat (vgl. [[MRK.1.15]]); «Himmel» umschreibt dabei ehrfürchtig Gott. βασιλεία meint die Königsherrschaft Gottes, nicht in erster Linie ein Gebiet. Der griechische Plural «Himmel» ist beibehalten."),
 ("MAT.10.7", "ist nahe gekommen", "literal", "Ἤγγικεν", None, ["ist nahe", "ist herbeigekommen"],
  "Perfekt: Das Reich ist herangekommen und nun nahe. Dieselbe Botschaft wie bei Johannes dem Täufer und Jesus ([[MAT.3.2]], [[MAT.4.17]])."),
 ("MAT.10.8", "Umsonst", "literal", "δωρεὰν", None, ["Als Geschenk", "Unentgeltlich"],
  "δωρεάν heisst «als Geschenk, ohne Bezahlung». Gemeint ist, dass die Jünger für Heilungen kein Entgelt nehmen sollen."),
 ("MAT.10.9", "Kupfergeld", "adapted", "χαλκὸν", "Kupfer", ["Kupfermünzen", "Kleingeld"],
  "Gold, Silber und Kupfer stehen für Münzen, die man im Gürtel trug; vgl. [[MRK.6.8]] («Geld im Gürtel»). κτάομαι heisst «erwerben, sich verschaffen»; ob damit auch das Mitnehmen gemeint ist oder nur das Anschaffen für die Reise, wird verschieden beurteilt."),
 ("MAT.10.10", "Beutel", "interpretive", "πήραν", None, ["Reisetasche", "Vorratssack", "Bettelsack"],
  "πήρα ist der Ranzen für Vorräte; manche denken an die Sammeltasche umherziehender Wanderprediger. Wiedergabe wie [[MRK.6.8]]."),
 ("MAT.10.10", "Untergewänder", "interpretive", "χιτῶνας", None, ["Hemden", "Leibröcke"],
  "χιτών ist das Gewand, das man unter dem Mantel auf dem Leib trug; wie [[MRK.6.9]]."),
 ("MAT.10.10", "keine Sandalen und keinen Stab", "literal", "μηδὲ ὑποδήματα μηδὲ ῥάβδον", None, ["keine Schuhe und keinen Stock"],
  "Nach [[MRK.6.8]]–[[MRK.6.9]] sollen die Jünger einen Stab mitnehmen und Sandalen tragen; bei Matthäus (wie [[LUK.9.3]] für den Stab) ist beides ausgeschlossen. Ob Matthäus eine noch strengere Ausrüstungsregel überliefert oder, vom Verb «verschafft euch» her, nur das zusätzliche Anschaffen verbietet, wird verschieden erklärt. Die Übersetzung gleicht nicht an."),
 ("MAT.10.10", "wert", "adapted", "ἄξιος", "würdig", ["verdient seine Nahrung"],
  "ἄξιος heisst «würdig, wert»; beim Lohn oder Unterhalt ist im Deutschen «wert» üblich. Sonst steht im Kapitel «würdig» ([[MAT.10.11]], [[MAT.10.13]], [[MAT.10.37]]–[[MAT.10.38]]). Vgl. [[LUK.10.7]] («Lohn»)."),
 ("MAT.10.11", "würdig", "literal", "ἄξιός", None, ["geeignet", "es wert"],
  "Gemeint ist ein Gastgeber, der die Boten und ihre Botschaft aufnimmt (vgl. [[MAT.10.13]]–[[MAT.10.14]])."),
 ("MAT.10.12", "grüsst es", "literal", "ἀσπάσασθε αὐτήν", None, ["grüsst die Bewohner", "wünscht ihm Frieden"],
  "«Es» ist das Haus, gemeint sind seine Bewohner. Der übliche Gruss war ein Friedenswunsch; darauf bezieht sich [[MAT.10.13]] («euer Friede»)."),
 ("MAT.10.13", "euer Friede", "literal", "ἡ εἰρήνη ὑμῶν", None, ["euer Friedensgruss"],
  "Der Friede wird fast wie eine Gabe vorgestellt, die auf das Haus kommt oder zu den Boten zurückkehrt."),
 ("MAT.10.14", "verlasst das Haus oder jene Stadt", "adapted", "ἐξερχόμενοι ἔξω τῆς οἰκίας ἢ τῆς πόλεως ἐκείνης", "hinausgehend aus jenem Haus oder jener Stadt", ["geht aus jenem Haus oder jener Stadt hinaus"],
  "Der Satz wechselt wie im Griechischen von «wer euch nicht aufnimmt» zur Anweisung an die Jünger; der Bruch ist nicht geglättet. ἐκείνης bezieht sich mindestens auf die Stadt, vielleicht auch auf das Haus."),
 ("MAT.10.14", "schüttelt den Staub von euren Füssen ab", "interpretive", "ἐκτινάξατε τὸν κονιορτὸν τῶν ποδῶν ὑμῶν", "schüttelt den Staub eurer Füsse ab", ["schüttelt den Staub von euren Füssen als Zeichen ab"],
  "Zeichenhandlung der Trennung: Man nimmt nichts von dem Ort mit. Ob sie als Warnung oder als Anklage gemeint ist, wird verschieden beurteilt (vgl. [[MRK.6.11]], [[ACT.13.51]])."),
 ("MAT.10.15", "Amen, ich sage euch", "traditional", "ἀμὴν λέγω ὑμῖν", None, ["Wahrlich, ich sage euch", "Ich versichere euch"],
  "Einheitliche Wiedergabe für das Matthäusevangelium. Das hebräische «Amen» (fest, zuverlässig) steht bei Jesus am Anfang, nicht am Schluss der Aussage. Ebenso [[MAT.10.23]], [[MAT.10.42]], [[MAT.11.11]]."),
 ("MAT.10.15", "erträglicher ergehen", "adapted", "ἀνεκτότερον ἔσται", "erträglicher wird es sein", None,
  "Sodom und Gomorra ([[GEN.19.24]]–[[GEN.19.25]]) gelten als Beispiel des schwersten Gerichts. «Land» (γῇ) meint die Bewohner. Ebenso [[MAT.11.22]] und [[MAT.11.24]]."),
 ("MAT.10.16", "Siehe", "traditional", "Ἰδοὺ", None, ["Seht", "Gebt acht"],
  "Einheitliche Wiedergabe für das Matthäusevangelium; Mundart «lueg»."),
 ("MAT.10.16", "ohne Falsch", "interpretive", "ἀκέραιοι", "unvermischt", ["arglos", "lauter", "aufrichtig"],
  "ἀκέραιος heisst «unvermischt, rein» und bezeichnet einen Menschen ohne Hintergedanken. «Arglos» könnte als «naiv» missverstanden werden; «ohne Falsch» betont die Aufrichtigkeit."),
 ("MAT.10.17", "an Gerichte", "interpretive", "εἰς συνέδρια", None, ["an Ratsversammlungen", "an die Synedrien"],
  "συνέδριον (Plural) bezeichnet hier örtliche Ratsgremien mit Gerichtsbarkeit, nicht nur den Hohen Rat in Jerusalem (vgl. [[MAT.5.22]], [[MAT.26.59]]). Wiedergabe wie [[MRK.13.9]]."),
 ("MAT.10.17", "in ihren Synagogen", "literal", "ἐν ταῖς συναγωγαῖς αὐτῶν", None, None,
  "Matthäus spricht öfter von «ihren Synagogen» ([[MAT.4.23]], [[MAT.9.35]], [[MAT.12.9]]); das zeigt Abstand zwischen den Adressaten des Evangeliums und bestimmten Synagogengemeinden seiner Zeit. Es ist keine Aussage über das Judentum insgesamt; die Übersetzung gibt die Wendung neutral wieder."),
 ("MAT.10.17", "geisseln", "literal", "μαστιγώσουσιν", None, ["auspeitschen", "schlagen"],
  "Gemeint ist die Prügelstrafe der Synagogengerichte (vgl. [[DEU.25.2]]–[[DEU.25.3]], [[2CO.11.24]])."),
 ("MAT.10.18", "ihnen und den Heiden zum Zeugnis", "interpretive", "εἰς μαρτύριον αὐτοῖς καὶ τοῖς ἔθνεσιν", None, ["als Zeugnis vor ihnen und den Heiden", "als Zeugnis gegen sie"],
  "Der Dativ kann «für sie» (Zeugnis, das sie hören) oder «gegen sie» (Belastung im Gericht) bedeuten. «Ihnen» bezieht sich wohl auf die Statthalter und Könige oder auf die Verfolger aus [[MAT.10.17]]."),
 ("MAT.10.19", "sorgt euch nicht", "literal", "μὴ μεριμνήσητε", None, ["macht euch keine Sorgen"],
  "Dasselbe Verb wie in [[MAT.6.25]]–[[MAT.6.34]]; einheitlich «sich sorgen»."),
 ("MAT.10.20", "der Geist eures Vaters", "literal", "τὸ πνεῦμα τοῦ πατρὸς ὑμῶν", None, None,
  "Nur Matthäus sagt «der Geist eures Vaters»; [[MRK.13.11]] hat «der heilige Geist». Die Bezeichnung Gottes als «euer Vater» prägt die Reden des Matthäus (vgl. [[MAT.10.29]])."),
 ("MAT.10.22", "standhält", "interpretive", "ὑπομείνας", None, ["ausharrt", "durchhält"],
  "Partizip Aorist: wer standgehalten hat. «Bis ans Ende» (εἰς τέλος) kann das Ende der Verfolgung, des Lebens oder der Weltzeit meinen (vgl. [[MAT.24.13]]); auch «bis zuletzt, völlig» ist möglich."),
 ("MAT.10.23", "gewiss nicht zu Ende kommen", "interpretive", "οὐ μὴ τελέσητε τὰς πόλεις", "ihr werdet die Städte gewiss nicht vollenden", ["nicht alle Städte durchziehen", "mit der Flucht durch die Städte nicht fertig werden"],
  "Gemeint ist, dass die Jünger nicht alle Städte Israels erreicht haben werden, sei es mit der Verkündigung oder auf der Flucht. Welches Kommen des Menschensohns gemeint ist, ist eine bekannte Streitfrage: das Kommen am Ende der Zeit, die Auferstehung, das Gericht über Jerusalem im Jahr 70 oder ein Kommen während der Aussendung selbst. Die Übersetzung lässt das offen; οὐ μή ist eine verstärkte Verneinung («gewiss nicht»)."),
 ("MAT.10.23", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", None,
  "Einheitliche Wiedergabe für das Matthäusevangelium und wie bei Markus; Selbstbezeichnung Jesu mit Anklang an [[DAN.7.13]]."),
 ("MAT.10.24", "Knecht", "interpretive", "δοῦλος", None, ["Sklave", "Diener"],
  "δοῦλος ist ein unfreier Diener, oft ein Sklave. Im Gegenüber zu «Herr» (κύριος) und in der Spruchform ist «Knecht» gewählt; wo die soziale Stellung im Vordergrund steht, ist «Sklave» genauer (vgl. [[MRK.10.44]])."),
 ("MAT.10.25", "Beelzebul", "literal", "Βεελζεβοὺλ", None, ["Beelzebub"],
  "Name eines Dämonenfürsten (vgl. [[MAT.12.24]], [[MAT.12.27]]). Die Form «Beelzebub» folgt der lateinischen Überlieferung und [[2KI.1.2]]. Die Bedeutung ist unsicher; viele hören «Herr der Wohnung», was zum Wortspiel mit «Hausherr» (οἰκοδεσπότης) passen würde."),
 ("MAT.10.26", "verhüllt", "literal", "κεκαλυμμένον", None, ["zugedeckt"],
  "κεκαλυμμένον («verhüllt») und ἀποκαλυφθήσεται («wird enthüllt») gehören zum selben Stamm; «verhüllt – enthüllt» hält den Gleichklang. Dieselbe Wurzel steht in [[MAT.11.25]] und [[MAT.11.27]] («offenbaren»)."),
 ("MAT.10.27", "ins Ohr geflüstert hört", "adapted", "εἰς τὸ οὖς ἀκούετε", "ins Ohr hört", ["im Vertrauen hört", "unter vier Augen hört"],
  "«Ins Ohr hören» meint das leise, vertrauliche Mitteilen; «geflüstert» macht das im Deutschen deutlich. «Auf den Dächern» (Flachdächer) heisst: in aller Öffentlichkeit."),
 ("MAT.10.28", "die Seele", "interpretive", "τὴν ψυχὴν", None, ["das Leben"],
  "ψυχή heisst «Leben, Seele, das Selbst». Hier steht es dem Leib (σῶμα) gegenüber, den Menschen töten können; deshalb «Seele». In [[MAT.10.39]] meint dasselbe Wort das Leben, das man findet oder verliert («Leben»), in [[MAT.11.29]] wieder «Seelen». Der Wechsel ist bewusst."),
 ("MAT.10.28", "in der Hölle", "traditional", "ἐν γεέννῃ", "in der Gehenna", ["im Feuer der Gehenna", "im Verderben"],
  "Γέεννα ist das Hinnomtal südlich von Jerusalem, das zum Bild für den Ort des endgültigen Gerichts wurde (vgl. [[MAT.5.22]], [[MAT.5.29]]–[[MAT.5.30]]). Wiedergabe wie bei Markus ([[MRK.9.43]])."),
 ("MAT.10.28", "verderben", "interpretive", "ἀπολέσαι", None, ["vernichten", "zugrunde richten"],
  "Dasselbe Verb wie «verlieren» in [[MAT.10.39]] und [[MAT.10.42]] und «verloren» in [[MAT.10.6]]. Gemeint ist, wer Gott fürchten soll; dass der Teufel gemeint sei, vertreten nur wenige."),
 ("MAT.10.29", "für einen Groschen", "adapted", "ἀσσαρίου", "für ein As", ["für einen Assarion", "für einen Rappen", "für ein paar Münzen"],
  "Das As (griechisch ἀσσάριον) war eine kleine römische Kupfermünze, etwa ein Sechzehntel eines Denars, des Tageslohns eines Arbeiters. «Groschen» gibt den geringen Wert wieder."),
 ("MAT.10.29", "ohne euren Vater", "interpretive", "ἄνευ τοῦ πατρὸς ὑμῶν", None, ["ohne den Willen eures Vaters", "ohne dass euer Vater es weiss"],
  "Der Text sagt knapp «ohne euren Vater». Ob Gottes Wissen, sein Wille oder seine Gegenwart gemeint ist, bleibt offen; Übersetzungen, die ein Wort ergänzen, legen sich fest."),
 ("MAT.10.32", "zu mir bekennt", "interpretive", "ὁμολογήσει ἐν ἐμοὶ", "in mir bekennen wird", ["sich offen zu mir stellt", "mich bekennt"],
  "Die Verbindung von ὁμολογέω mit ἐν ist ungewöhnlich und gilt als semitische Wendung («sich zu jemandem bekennen»)."),
 ("MAT.10.32", "Vater in den Himmeln", "traditional", "πατρός μου τοῦ ἐν οὐρανοῖς", None, ["Vater im Himmel"],
  "Einheitliche Wiedergabe für das Matthäusevangelium (wie [[MAT.6.9]]): «Vater in den Himmeln» gibt den griechischen Plural wieder. Ebenso [[MAT.10.33]]."),
 ("MAT.10.34", "Frieden auf die Erde zu bringen", "adapted", "βαλεῖν εἰρήνην ἐπὶ τὴν γῆν", "Frieden auf die Erde zu werfen", None,
  "βάλλω «werfen» steht hier in der abgeschwächten Bedeutung «bringen, setzen»."),
 ("MAT.10.34", "ein Schwert", "interpretive", "μάχαιραν", None, ["die Trennung", "die Entzweiung"],
  "Das Schwert ist Bild für die Scheidung, die [[MAT.10.35]]–[[MAT.10.36]] beschreiben; [[LUK.12.51]] sagt dafür «Spaltung». Es ist keine Aufforderung zur Gewalt (vgl. [[MAT.26.52]]). Das Bild ist stehen gelassen."),
 ("MAT.10.35", "zu entzweien", "literal", "διχάσαι", None, ["zu trennen", "zu entfremden"],
  "κατά mit Genitiv heisst «gegen»: der Mensch gegen seinen Vater usw. [[MAT.10.35]]–[[MAT.10.36]] nehmen [[MIC.7.6]] auf, ohne es als Zitat einzuführen."),
 ("MAT.10.37", "mehr liebt als mich", "literal", "φιλῶν πατέρα ἢ μητέρα ὑπὲρ ἐμὲ", "liebt über mich hinaus", ["lieber hat als mich"],
  "Das Verb ist φιλέω (bei Johannes «lieb haben»); hier ist «lieben» der natürliche Ausdruck. ὑπέρ heisst «über … hinaus, mehr als»."),
 ("MAT.10.37", "meiner nicht würdig", "literal", "οὐκ ἔστιν μου ἄξιος", None, ["gehört nicht zu mir", "verdient mich nicht"], None),
 ("MAT.10.38", "sein Kreuz nicht auf sich nimmt", "literal", "οὐ λαμβάνει τὸν σταυρὸν αὐτοῦ", None, None,
  "Erste Erwähnung des Kreuzes im Evangelium, noch vor den Leidensankündigungen (vgl. [[MAT.16.24]]). Das Bild stammt vom Verurteilten, der den Querbalken zur Hinrichtung trägt."),
 ("MAT.10.39", "Leben", "interpretive", "ψυχὴν", None, ["Seele", "sich selbst"],
  "Hier meint ψυχή das eigene Leben, das man sichern oder hingeben kann (vgl. [[MAT.16.25]]). Die Partizipien im Aorist («gefunden hat», «verloren hat») blicken vom Gericht aus zurück."),
 ("MAT.10.41", "weil er ein Prophet ist", "adapted", "εἰς ὄνομα προφήτου", "auf den Namen eines Propheten hin", ["als Propheten", "um seines Prophetseins willen"],
  "εἰς ὄνομα mit Genitiv ist eine semitisch geprägte Wendung für «als, in der Eigenschaft als». Ebenso «weil er ein Gerechter ist» und «weil er ein Jünger ist» ([[MAT.10.42]])."),
 ("MAT.10.42", "dieser Kleinen", "interpretive", "τῶν μικρῶν τούτων", None, ["dieser Geringen", "dieser Unbedeutenden"],
  "Im Zusammenhang sind die ausgesandten Jünger gemeint (vgl. [[MAT.18.6]], [[MAT.18.10]], [[MAT.25.40]])."),
 ("MAT.10.42", "kaltes Wasser", "adapted", "ψυχροῦ", "Kaltes", ["frisches Wasser"],
  "Das Griechische hat nur «(einen Becher) Kaltes»; «Wasser» ist ergänzt."),
 ("MAT.11.1", "Und es geschah", "traditional", "Καὶ ἐγένετο", None, ["Und als", "Als nun"],
  "Mit dieser Formel schliesst Matthäus jede seiner fünf grossen Reden ab ([[MAT.7.28]], [[MAT.11.1]], [[MAT.13.53]], [[MAT.19.1]], [[MAT.26.1]]); die Wiedergabe hält sie erkennbar. Der Vers beendet die Aussendungsrede und leitet zu Kapitel 11 über."),
 ("MAT.11.1", "in ihren Städten", "interpretive", "ἐν ταῖς πόλεσιν αὐτῶν", None, ["in den Städten dort", "in den Städten der Leute"],
  "Wessen Städte gemeint sind, sagt der Text nicht; wohl die der Menschen in Galiläa. Dass die Zwölf aufbrechen oder zurückkehren, erzählt Matthäus nicht."),
 ("MAT.11.2", "Gefängnis", "literal", "δεσμωτηρίῳ", None, None,
  "Vgl. [[MAT.4.12]]; der Grund der Gefangenschaft wird erst [[MAT.14.3]]–[[MAT.14.4]] erzählt."),
 ("MAT.11.2", "des Christus", "traditional", "τοῦ χριστοῦ", None, ["des Gesalbten", "des Messias"],
  "Einheitliche Wiedergabe χριστός «Christus». χριστός übersetzt hebräisch māšîaḥ «Gesalbter» (Messias). Hier spricht der Erzähler: Johannes fragt, ob Jesus der Erwartete ist; der Erzähler nennt ihn schon den Christus (vgl. [[MAT.1.1]]). «Werke» verbindet mit [[MAT.11.19]]."),
 ("MAT.11.3", "der Kommende", "interpretive", "ὁ ἐρχόμενος", None, ["der da kommen soll", "der, der kommen soll"],
  "Bezeichnung für den erwarteten Retter, im Anschluss an die Ankündigung des Täufers ([[MAT.3.11]]: «der nach mir kommt») und an [[PSA.118.26]] (vgl. [[MAT.21.9]])."),
 ("MAT.11.5", "den Armen wird das Evangelium verkündigt", "adapted", "πτωχοὶ εὐαγγελίζονται", "Arme werden evangelisiert", ["Armen wird die gute Nachricht gebracht", "Arme empfangen die frohe Botschaft"],
  "Die Aufzählung nimmt Verheissungen aus Jesaja auf ([[ISA.35.5]]–[[ISA.35.6]], [[ISA.26.19]], [[ISA.61.1]]). εὐαγγελίζομαι gehört zu εὐαγγέλιον «Evangelium» (vgl. [[MAT.4.23]]); die Wiedergabe hält diese Verbindung."),
 ("MAT.11.6", "selig", "traditional", "μακάριός", None, ["glücklich zu preisen", "wohl dem", "glücklich"],
  "Vorschlag für eine einheitliche Wiedergabe von μακάριος im Matthäusevangelium (13-mal, vor allem [[MAT.5.3]]–[[MAT.5.11]]): «selig» ist vertraut und meint das von Gott geschenkte Heil, nicht nur ein Glücksgefühl. «Glücklich zu preisen» trifft den Zuspruch ebenfalls und ist zeitgemässer."),
 ("MAT.11.6", "keinen Anstoss nimmt", "interpretive", "μὴ σκανδαλισθῇ", "nicht zu Fall gebracht wird", ["nicht irre wird", "sich nicht ärgert", "nicht zu Fall kommt"],
  "Vorschlag für eine einheitliche Wiedergabe von σκανδαλίζω im Matthäusevangelium (14-mal): passiv «Anstoss nehmen» (wie [[MRK.6.3]]), aktiv «zu Fall bringen» (wie [[MRK.9.42]]). Das Bild ist das Stellholz einer Falle oder der Stein, über den man stolpert. Hier wohl: wer an Jesus nicht irre wird, auch wenn er anders auftritt als erwartet."),
 ("MAT.11.7", "zur Menge", "adapted", "τοῖς ὄχλοις", "zu den Mengen", ["zu den Leuten", "zu den Volksscharen"],
  "Matthäus braucht den Plural οἱ ὄχλοι oft für die Menschen, die Jesus folgen; im Deutschen ist der Singular natürlicher."),
 ("MAT.11.7", "Ein Schilfrohr, das vom Wind hin und her bewegt wird", "interpretive", "κάλαμον ὑπὸ ἀνέμου σαλευόμενον", None, ["ein Rohr, das im Wind schwankt"],
  "Bild für einen schwankenden, angepassten Menschen; im Jordantal wuchs Schilf. Manche sehen eine Anspielung auf Herodes Antipas, auf dessen frühen Münzen ein Schilfrohr abgebildet war; das ist umstritten."),
 ("MAT.11.8", "in weiche Kleider gehüllt", "adapted", "ἐν μαλακοῖς ἠμφιεσμένον", "in Weiches gekleidet", ["in feine Gewänder gekleidet"],
  "μαλακά sind weiche, feine Stoffe; «Kleider» ist ergänzt. Die von RP gelesene Form ἐν μαλακοῖς ἱματίοις («in weichen Kleidern») ergibt dieselbe Übersetzung und steht deshalb nicht als Alternative."),
 ("MAT.11.9", "Oder was seid ihr hinausgegangen? Einen Propheten zu sehen?", "interpretive", "ἀλλὰ τί ἐξήλθατε; προφήτην ἰδεῖν;", None, ["Oder was seid ihr hinausgegangen zu sehen? Einen Propheten?"],
  "Der SBLGNT setzt (wie WH und SR) das Fragezeichen nach ἐξήλθατε und liest προφήτην ἰδεῖν; KJTR, Stephanus und RP lesen τί ἐξήλθετε ἰδεῖν; προφήτην; (nach den CNTR-Texten dieser Ausgaben). Der Sinn bleibt gleich. Der importierte Apparat führt die Stelle nicht als eigene Variante. ἀλλά ist in [[MAT.11.8]]–[[MAT.11.9]] mit «oder» wiedergegeben: Es leitet die nächste Möglichkeit ein."),
 ("MAT.11.10", "Boten", "interpretive", "ἄγγελόν", None, ["Engel"],
  "ἄγγελος heisst «Bote» und «Engel»; hier ist ein menschlicher Bote gemeint. Das Wort verbindet [[MAL.3.1]] mit [[EXO.23.20]] (in der Septuaginta fast gleichlautend). Wiedergabe wie [[MRK.1.2]]."),
 ("MAT.11.11", "der Kleinste", "interpretive", "ὁ μικρότερος", "der Kleinere", ["der Geringste", "der Geringere"],
  "Der Komparativ steht im neutestamentlichen Griechisch oft für den Superlativ: der Kleinste im Reich steht über Johannes. Seit der Alten Kirche wird auch vertreten, «der Kleinere» (Jüngere, Geringere) sei Jesus selbst, der grösser ist als Johannes. Die Übersetzung folgt der verbreiteten Deutung; redaktionelle Entscheidung."),
 ("MAT.11.11", "aufgetreten", "adapted", "ἐγήγερται", "ist erweckt worden", ["ist aufgestanden", "hat es gegeben"],
  "ἐγείρω im Passiv «auftreten, sich erheben» (vgl. [[MAT.24.11]]); dasselbe Verb steht in [[MAT.11.5]] für die Auferweckung der Toten."),
 ("MAT.11.12", "leidet das Reich der Himmel Gewalt", "interpretive", "ἡ βασιλεία τῶν οὐρανῶν βιάζεται", None, ["bricht sich das Reich der Himmel mit Macht Bahn", "dringt das Reich der Himmel mit Gewalt vor"],
  "Einer der umstrittensten Sätze des Evangeliums. βιάζεται kann passiv sein («erleidet Gewalt», so hier) oder medial («setzt sich mit Gewalt durch»). Die «Gewalttätigen» (βιασταί), die es «an sich reissen», können Gegner sein, die das Reich bekämpfen (vgl. das Schicksal des Täufers, [[MAT.11.2]], [[MAT.14.3]]–[[MAT.14.10]]), oder Menschen, die mit Entschlossenheit hineindrängen (vgl. [[LUK.16.16]]). Die Übersetzung bleibt wörtlich und negativ; die positive Deutung wird ebenfalls breit vertreten."),
 ("MAT.11.13", "prophezeit", "literal", "ἐπροφήτευσαν", None, ["geweissagt", "prophetisch geredet"],
  "Auffällig ist, dass auch «das Gesetz» prophezeit: Gesetz und Propheten weisen bis Johannes voraus."),
 ("MAT.11.14", "Elija, der kommen soll", "interpretive", "Ἠλίας ὁ μέλλων ἔρχεσθαι", None, ["Elija, der kommen wird"],
  "Nach [[MAL.4.5]] (im hebräischen Text 3,23) wurde die Rückkehr des Elija vor dem Tag JHWHs erwartet; vgl. [[MAT.17.10]]–[[MAT.17.13]]. «Wenn ihr es annehmen wollt» zeigt, dass die Gleichsetzung nicht selbstverständlich war."),
 ("MAT.11.15", "Wer Ohren hat, der höre!", "literal", "ὁ ἔχων ὦτα ἀκουέτω", None, None,
  "Weckruf; ebenso [[MAT.13.9]] und [[MAT.13.43]]. Die Form mit «um zu hören» (ἀκούειν, vgl. [[MRK.4.9]]) steht als Alternative."),
 ("MAT.11.16", "dieses Geschlecht", "traditional", "τὴν γενεὰν ταύτην", None, ["diese Generation"],
  "γενεά heisst «Generation, Zeitgenossenschaft»; Wiedergabe wie bei Markus im Hochdeutschen (vgl. [[MRK.8.12]]), in der Mundart «Generation». Gemeint sind die Zeitgenossen Jesu, die weder Johannes noch ihn annehmen."),
 ("MAT.11.17", "euch nicht an die Brust geschlagen", "adapted", "οὐκ ἐκόψασθε", "ihr habt euch nicht geschlagen", ["ihr habt nicht geklagt", "ihr habt nicht getrauert"],
  "κόπτομαι bezeichnet das Schlagen an die Brust als Trauergebärde. Die Kinder spielen Hochzeit (Flöte, Tanz) und Begräbnis (Klagelied, Trauergebärde); die anderen machen bei keinem Spiel mit."),
 ("MAT.11.19", "was für ein Mensch", "adapted", "ἄνθρωπος", "ein Mensch", ["dieser Mensch"],
  "ἄνθρωπος steht verächtlich vor den Schimpfwörtern; «was für ein Mensch» gibt den Ton wieder."),
 ("MAT.11.19", "ein Fresser und Weinsäufer", "literal", "φάγος καὶ οἰνοπότης", None, ["ein Schlemmer und Trinker"],
  "Die Verbindung erinnert an [[DEU.21.20]] (der widerspenstige Sohn)."),
 ("MAT.11.19", "gerechtfertigt worden", "interpretive", "ἐδικαιώθη", None, ["ins Recht gesetzt worden", "als gerecht erwiesen worden"],
  "Der Aorist kann eine allgemeine Wahrheit ausdrücken («wird ins Recht gesetzt»). Die «Weisheit» ist Gottes Weisheit, die in Johannes und Jesus wirkt; die «Werke» knüpfen an «die Werke des Christus» in [[MAT.11.2]] an. [[LUK.7.35]] hat «von allen ihren Kindern»; diese Lesart steht bei Matthäus in einem Teil der Überlieferung (siehe Alternative)."),
 ("MAT.11.20", "Da", "literal", "Τότε", None, ["Dann"],
  "τότε ist ein Lieblingswort des Matthäus (nach MACULA-Lemma 90-mal im SBLGNT-Text); erzählend einheitlich «da» oder «dann», in der Mundart «dänn»."),
 ("MAT.11.20", "Machttaten", "literal", "δυνάμεις", None, ["Wunder", "Krafttaten"],
  "δύναμις heisst «Kraft», im Plural die Taten, in denen sie sichtbar wird; Wiedergabe wie bei Markus ([[MRK.6.2]]). Ebenso [[MAT.11.21]] und [[MAT.11.23]]."),
 ("MAT.11.20", "umgekehrt waren", "literal", "μετενόησαν", None, ["Busse getan hatten", "sich bekehrt hatten"],
  "Einheitliche Wiedergabe μετανοέω «umkehren» (vgl. [[MAT.3.2]], [[MAT.4.17]])."),
 ("MAT.11.21", "in Sack und Asche", "literal", "ἐν σάκκῳ καὶ σποδῷ", None, ["im Bussgewand und in Asche"],
  "Sack (grobes Tuch) und Asche sind Zeichen der Busse und Trauer (vgl. [[JON.3.6]]). Tyrus und Sidon stehen für heidnische Städte, gegen die die Propheten Gericht ankündigten (vgl. [[ISA.23.1]])."),
 ("MAT.11.23", "wirst du etwa bis zum Himmel erhöht werden?", "literal", "μὴ ἕως οὐρανοῦ ὑψωθήσῃ;", None, ["Wirst du etwa bis zum Himmel erhoben?"],
  "Die Frage mit μή erwartet die Antwort «nein». Der Satz nimmt das Spottlied auf den König von Babel auf ([[ISA.14.13]]–[[ISA.14.15]])."),
 ("MAT.11.23", "Totenreich", "interpretive", "ᾅδου", None, ["Hades", "Unterwelt"],
  "ᾅδης gibt in der Septuaginta das hebräische šəʾôl wieder, den Ort der Toten; anders als Γέεννα ([[MAT.10.28]]) nicht in erster Linie Ort der Strafe. Mundart «Toterich»."),
 ("MAT.11.25", "ergriff Jesus das Wort", "adapted", "ἀποκριθεὶς ὁ Ἰησοῦς εἶπεν", "antwortete Jesus und sagte", ["nahm Jesus das Wort", "sprach Jesus"],
  "ἀποκρίνομαι steht hier ohne vorausgehende Frage und heisst «das Wort nehmen, anheben zu reden»."),
 ("MAT.11.25", "Ich preise dich", "interpretive", "Ἐξομολογοῦμαί σοι", "Ich bekenne dir", ["Ich danke dir", "Ich lobe dich"],
  "ἐξομολογέομαι heisst «bekennen», mit Dativ im Gebet «preisen, lobend bekennen» (wie in den Psalmen der Septuaginta)."),
 ("MAT.11.25", "Unmündigen", "traditional", "νηπίοις", None, ["kleinen Kindern", "Einfachen", "Ungebildeten"],
  "νήπιος ist das kleine Kind, übertragen der Unerfahrene; Gegensatz zu den «Weisen und Verständigen» (vgl. [[PSA.8.2]], zitiert in [[MAT.21.16]])."),
 ("MAT.11.26", "denn so hat es dir gefallen", "adapted", "ὅτι οὕτως εὐδοκία ἐγένετο ἔμπροσθέν σου", "denn so wurde es Wohlgefallen vor dir", ["denn so war es dein Wille", "denn so hast du es beschlossen"],
  "εὐδοκία ist Gottes Wohlgefallen, sein gnädiger Entschluss; «vor dir» ist eine ehrfürchtige Umschreibung. ὁ πατήρ steht als Anrede im Nominativ."),
 ("MAT.11.27", "übergeben worden", "literal", "παρεδόθη", None, ["anvertraut worden", "überlassen worden"],
  "Dasselbe Verb wie «ausliefern» in [[MAT.10.4]] und [[MAT.10.17]]–[[MAT.10.21]]; hier der Sinn «übergeben, anvertrauen». Was «alles» umfasst (Vollmacht, Erkenntnis, Offenbarung), sagt der Text nicht; vgl. [[MAT.28.18]]."),
 ("MAT.11.27", "kennt", "interpretive", "ἐπιγινώσκει", None, ["erkennt", "kennt genau"],
  "ἐπιγινώσκω betont das volle, persönliche Kennen."),
 ("MAT.11.28", "euch abmüht und beladen seid", "literal", "κοπιῶντες καὶ πεφορτισμένοι", None, ["mühselig und beladen seid"],
  "κοπιάω «sich abmühen, müde werden»; das Perfekt πεφορτισμένοι «mit Lasten beladen». Was die Last ist (Lebensnot, die Auslegung des Gesetzes, vgl. [[MAT.23.4]], dasselbe Wortfeld), sagt der Text nicht ausdrücklich."),
 ("MAT.11.28", "Ruhe geben", "literal", "ἀναπαύσω", None, ["erquicken", "Erholung verschaffen"],
  "ἀναπαύω «zur Ruhe bringen»; das Nomen ἀνάπαυσις folgt in [[MAT.11.29]] («Ruhe»)."),
 ("MAT.11.29", "Joch", "literal", "ζυγόν", None, None,
  "Das Joch ist in jüdischer Sprache ein Bild für die Bindung an Gottes Gebote und eine Lehre. Jesus stellt sein eigenes Joch dagegen."),
 ("MAT.11.29", "sanftmütig und demütig im Herzen", "literal", "πραΰς εἰμι καὶ ταπεινὸς τῇ καρδίᾳ", None, ["freundlich und von Herzen bescheiden", "sanft und von Herzen niedrig"],
  "πραΰς auch in [[MAT.5.5]] und [[MAT.21.5]] («sanftmütig»). ταπεινός «niedrig, demütig»."),
 ("MAT.11.29", "denn", "interpretive", "ὅτι", None, ["dass"],
  "ὅτι kann begründen («denn ich bin sanftmütig») oder den Inhalt des Lernens angeben («lernt von mir, dass ich sanftmütig bin»)."),
 ("MAT.11.29", "Ruhe finden für eure Seelen", "literal", "εὑρήσετε ἀνάπαυσιν ταῖς ψυχαῖς ὑμῶν", None, ["Ruhe für euch selbst finden"],
  "Fast wörtlich nach [[JER.6.16]]. ψυχή steht hier für das ganze Leben, das Selbst."),
 ("MAT.11.30", "sanft", "traditional", "χρηστὸς", None, ["angenehm", "gut zu tragen", "wohltuend"],
  "χρηστός heisst «brauchbar, gut, freundlich»; beim Joch: gut sitzend, nicht wund reibend. «Sanft» ist die vertraute Wiedergabe."),
]

DEC_GSW = [
 ("MAT.10.1", "jedi Chrankheit und jedes Gebräche", "literal", "πᾶσαν νόσον καὶ πᾶσαν μαλακίαν", None, ["jedi Chrankheit und jedi Schwächi"],
  "Feschti Wändig vom Matthäus ([[MAT.4.23]], [[MAT.9.35]], [[MAT.10.1]]); μαλακία heisst wörtli «Schwächi». Vorschlag für alli drüü Stelle."),
 ("MAT.10.2", "Apostel", "traditional", "ἀποστόλων", None, ["Gschickti"],
  "S Wort ghört zum Verb ἀποστέλλω «ussende» ([[MAT.10.5]], [[MAT.10.16]]): D Zwölf sind Gschickti vom Jesus."),
 ("MAT.10.4", "Kananäer", "interpretive", "Καναναῖος", None, ["Iiferer", "Zelot"],
  "Wohl es aramäisches Wort für «Iiferer»; [[LUK.6.15]] nännt dä Simon ζηλωτής. Mit de Kanaaniter hät de Name nüüt z tue."),
 ("MAT.10.5", "zu de Heide", "interpretive", "ἐθνῶν", "vo de Völker", ["vo de Nichtjude"],
  "τὰ ἔθνη sind d Völker, wo nöd zu Israel ghöred. Gliich i [[MAT.10.18]]."),
 ("MAT.10.7", "S Riich vo de Himel", "traditional", "ἡ βασιλεία τῶν οὐρανῶν", None, ["s Himelriich"],
  "Einheitlichi Widergaab fürs Matthäusevangelium. «Himel» umschriibt ehrfürchtig Gott; βασιλεία meint d Herrschaft vo Gott."),
 ("MAT.10.8", "Umesuscht", "literal", "δωρεὰν", None, ["gratis", "gschänkt"],
  "Züritüütsch «umesuscht» heisst «gratis» und «vergäbe»; da isch klar «gratis» gmeint."),
 ("MAT.10.9", "Chupfergäld", "adapted", "χαλκὸν", "Chupfer", ["Münz"],
  "Gold, Silber und Chupfer stönd für Münze, wo me im Gürtel treit hät."),
 ("MAT.10.10", "wärt", "literal", "ἄξιος", None, ["würdig"],
  "ἄξιος isch i de Mundart immer «wärt»: «sis Ässe wärt», «wer i ire wärt isch», «isch mich nöd wärt»."),
 ("MAT.10.12", "grüessed d Lüüt drin", "adapted", "ἀσπάσασθε αὐτήν", "grüessed s (s Huus)", ["grüessed s Huus"],
  "«Es» isch s Huus; gmeint sind d Lüüt, wo drin wohned. De Gruess isch en Fridenswunsch (lueg [[MAT.10.13]])."),
 ("MAT.10.16", "ohni Falsch", "interpretive", "ἀκέραιοι", "unvermischt", ["ehrlich", "ohni Hindergedanke"],
  "ἀκέραιος heisst «unvermischt, suber»: en Mänsch ohni Hindergedanke."),
 ("MAT.10.17", "a Gricht", "interpretive", "εἰς συνέδρια", None, ["a Rätsversammlige"],
  "Örtlichi Rät mit Grichtsbarkeit, nöd nu de Hoch Rat z Jerusalem; wie [[MRK.13.9]]."),
 ("MAT.10.23", "sicher nöd fertig", "interpretive", "οὐ μὴ τελέσητε τὰς πόλεις", "ir wärded d Stedt sicher nöd vollände", ["nöd dur alli Stedt choo"],
  "Gmeint isch, dass d Jünger nöd alli Stedt vo Israel erreicht händ. Weles Choo vom Mänschesohn gmeint isch, isch umstritte; d Übersetzig laat s offe."),
 ("MAT.10.24", "Chnächt", "interpretive", "δοῦλος", None, ["Sklav", "Diener"],
  "δοῦλος isch en unfreie Diener, oft en Sklav; im Gägenüber zum «Herr» staat «Chnächt»."),
 ("MAT.10.28", "d Seel", "interpretive", "τὴν ψυχὴν", None, ["s Läbe"],
  "Gägenüber em Liib staat «Seel»; i [[MAT.10.39]] meint s gliich Wort s Läbe («Läbe»)."),
 ("MAT.10.28", "de Höll", "traditional", "γεέννῃ", "de Gehenna", None,
  "Γέεννα isch s Hinnomtal bi Jerusalem, Bild für de Ort vom letschte Gricht; wie bi Markus «Höll»."),
 ("MAT.10.29", "für en Batze", "adapted", "ἀσσαρίου", "für es As", ["für en Rappe"],
  "S As (griechisch ἀσσάριον) isch e chliini römischi Chupfermünz gsii, öppe en Sächzähntel vom Tageslohn. «Batze» git de chlii Wärt wider."),
 ("MAT.10.29", "gheit", "adapted", "πεσεῖται", "wird gheie", None,
  "S Präsens staat für s Futur, wie s i de Mundart üblich isch."),
 ("MAT.10.37", "gärn hät", "literal", "φιλῶν", None, ["liebt"],
  "S Verb isch φιλέω; wie bi Johannes «gärn haa». I de Mundart isch das de natürlich Usdruck."),
 ("MAT.10.41", "wil er en Prophet isch", "adapted", "εἰς ὄνομα προφήτου", "uf de Name vo me Prophet", ["als Prophet"],
  "εἰς ὄνομα isch e semitischi Wändig für «als». Gliich «wil er en Grächte isch», «wil er en Jünger isch»."),
 ("MAT.11.6", "sälig", "traditional", "μακάριός", None, ["glücklich z priise", "wohl däm"],
  "Vorschlag für e einheitlichi Widergaab vo μακάριος im Matthäusevangelium ([[MAT.5.3]]–[[MAT.5.11]])."),
 ("MAT.11.6", "kei Aastoss nimmt", "interpretive", "μὴ σκανδαλισθῇ", "nöd z Fall bracht wird", ["nöd irr wird a mir"],
  "σκανδαλίζω: passiv «Aastoss nää» (wie [[MRK.6.3]]), aktiv «z Fall bringe» (wie [[MRK.9.42]])."),
 ("MAT.11.11", "de Chliinscht", "interpretive", "ὁ μικρότερος", "de Chliiner", ["de Gringscht"],
  "De Komparativ staat oft für de Superlativ. Sit de Alte Chile vertreted au einzelni, «de Chliiner» sig de Jesus sälber."),
 ("MAT.11.12", "tuet me em Riich vo de Himel Gwalt aa", "interpretive", "ἡ βασιλεία τῶν οὐρανῶν βιάζεται", "s Riich vo de Himel erliidet Gwalt", ["s Riich vo de Himel setzt sich mit Gwalt dure"],
  "Sehr umstritte. βιάζεται cha passiv sii (so da, i de Mundart mit «me» widergää) oder medial («setzt sich mit Macht dure»); d «Gwalttätige» chönd Gägner sii oder Lüüt, wo entschlosse inedrucked."),
 ("MAT.11.16", "Generation", "literal", "γενεὰν", None, ["Gschlächt"],
  "Wie bi Markus i de Mundart «Generation» ([[MRK.8.12]]); im Hochdüütsche «Geschlecht»."),
 ("MAT.11.19", "Süffel", "adapted", "οἰνοπότης", "Wiitrinker", ["Wiisüffer"],
  "οἰνοπότης isch eine, wo vil Wii trinkt; «Süffel» isch de gwöhnlich Schimpfname."),
 ("MAT.11.20", "Dänn", "literal", "Τότε", None, ["Da"],
  "τότε, es Lieblingswort vom Matthäus, isch erzählend immer «dänn». Für γάρ staat drum «nämli», nöd «dänn»."),
 ("MAT.11.20", "Chrafttate", "literal", "δυνάμεις", None, ["Wunder"],
  "Wie bi Markus ([[MRK.6.2]])."),
 ("MAT.11.21", "Wee", "literal", "Οὐαί", None, ["Wehe"],
  "Klagruef und Drohruef zgliich."),
 ("MAT.11.23", "Toterich", "interpretive", "ᾅδου", None, ["Hades", "Unterwält"],
  "ᾅδης isch de Ort vo de Tote (hebräisch šəʾôl), nöd in erschter Linie de Ort vo de Straf wie Γέεννα."),
 ("MAT.11.25", "Ich priise dich", "interpretive", "Ἐξομολογοῦμαί σοι", "Ich bekänne dir", ["Ich dank dir", "Ich lob dich"],
  "ἐξομολογέομαι heisst «bekänne», im Gebätt «lobend bekänne, priise»."),
 ("MAT.11.29", "sanftmüetig und demüetig im Härz", "literal", "πραΰς εἰμι καὶ ταπεινὸς τῇ καρδίᾳ", None, ["fründlich und bscheide vo Härze"], None),
 ("MAT.11.30", "liecht", "literal", "ἐλαφρόν", None, None,
  "«Liecht» heisst da «nöd schwär» (Gwicht) und isch gliich gschribe wie «s Liecht»."),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Lesarten de, Lesarten gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) bzw.
#  aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-MAT-010-003-01:R2", "MAT.10.3", "und Thaddäus,", "und Lebbäus, genannt Thaddäus,", "und de Thaddäus,", "und de Lebbäus, wo Thaddäus gnännt wird,", "gering",
  "Der zehnte Apostel trägt zwei Namen: Lebbäus mit dem Beinamen Thaddäus.", "De zäät Apostel hät zwei Näme: Lebbäus, mit em Zuename Thaddäus.",
  {"R1": [("Θαδδαῖος", "Thaddäus", "WH, Treg, NA28")], "R2": [("Λεββαῖος ὁ ἐπικληθεὶς Θαδδαῖος", "Lebbäus, genannt Thaddäus", "RP")]},
  {"R1": [("Θαδδαῖος", "de Thaddäus", "WH, Treg, NA28")], "R2": [("Λεββαῖος ὁ ἐπικληθεὶς Θαδδαῖος", "de Lebbäus, wo Thaddäus gnännt wird", "RP")]},
  ["Die Doppelform kann zwei überlieferte Namen derselben Person verbinden ([[MRK.3.18]] hat Thaddäus, ein Teil der Überlieferung Lebbäus); ebenso kann einer der Namen beim Abschreiben ergänzt oder ersetzt worden sein, um die Apostellisten anzugleichen.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 Θαδδαῖος, 032 Λεββαῖος ὁ ἐπικληθεὶς Θαδδαῖος. 05 hat die Zuordnung keiner der beiden Lesarten zugewiesen; nach der CNTR-Transkription steht dort λεββεος (Lebbäus) allein."],
  ["Di Doppelform cha zwei überliferet Näme vo de gliiche Person verbinde ([[MRK.3.18]] hät Thaddäus, en Teil vo de Überliferig Lebbäus); oder eine vo de Näme isch bim Abschriibe ergänzt oder ersetzt worde, für d Apostellischte aazgliiche.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 Θαδδαῖος, 032 Λεββαῖος ὁ ἐπικληθεὶς Θαδδαῖος; 05 hät nach de CNTR-Transkription λεββεος (Lebbäus) elei."]),
 ("VAR-SBLGNTAPP-MAT-010-004-01:R2", "MAT.10.4", "der Kananäer", "der Kananit", "de Kananäer", "de Kananit", "gering",
  "Andere Wortbildung derselben Bezeichnung; der Sinn ändert sich kaum.", "Anderi Wortbildig vo de gliiche Bezeichnig; de Sinn bliibt fascht gliich.",
  {"R1": [("Καναναῖος", "Kananäer", "WH, Treg, NA28")], "R2": [("Κανανίτης", "Kananit", "RP")]},
  {"R1": [("Καναναῖος", "Kananäer", "WH, Treg, NA28")], "R2": [("Κανανίτης", "Kananit", "RP")]},
  ["Κανανίτης kann an griechische Herkunftsnamen auf -ίτης angeglichen sein (als hiesse es «aus Kana»); ebenso kann Καναναῖος an [[MRK.3.18]] angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 03, 04 und 05 Καναναῖος, 01 (auch in der Korrektur) und 032 Κανανίτης."],
  ["Κανανίτης cha a griechischi Herkunftsnäme uf -ίτης aaglichen sii; oder Καναναῖος isch a [[MRK.3.18]] aaglichen worde.",
   "Nach de automatische Zueornig läsed 03, 04 und 05 Καναναῖος, 01 und 032 Κανανίτης."]),
 ("VAR-SBLGNTAPP-MAT-010-008-01:R2", "MAT.10.8", "Heilt Kranke, weckt Tote auf, macht Aussätzige rein,", "Heilt Kranke, macht Aussätzige rein,",
  "Heiled Chranki, wecked Toti uf, mached Ussätzigi rein,", "Heiled Chranki, mached Ussätzigi rein,", "mittel",
  "Der Auftrag, Tote aufzuwecken, fehlt.", "De Uftrag, Toti ufzwecke, fehlt.",
  {"R1": [("νεκροὺς ἐγείρετε", "weckt Tote auf", "WH, Treg, NA28")], "R2": [("–", "(fehlt)", "RP")]},
  {"R1": [("νεκροὺς ἐγείρετε", "wecked Toti uf", "WH, Treg, NA28")], "R2": [("–", "(fehlt)", "RP")]},
  ["Die Worte können zwischen gleich endenden Befehlsformen (-ετε) durch ein Abgleiten des Auges ausgefallen sein; ebenso können sie nach [[MAT.11.5]] (Tote werden auferweckt) ergänzt worden sein. Dafür kann sprechen, dass sie in einem Teil der Überlieferung an anderer Stelle der Reihe stehen.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 die Worte, 032 nicht. Die Zuordnung führt auch KJTR und Stephanus ohne die Worte; nach den CNTR-Texten haben diese Ausgaben sie aber an anderer Stelle (nach «macht Aussätzige rein»). Der Apparat nennt für die Auslassung nur RP."],
  ["D Wort chönd zwüsche gliich ändende Befählsforme (-ετε) usgfalle sii, wil s Aug abgrutscht isch; oder si sind nach [[MAT.11.5]] ergänzt worde. Defür cha spräche, dass si i eme Teil vo de Überliferig a ere andere Stell vo de Reie stönd.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 d Wort, 032 nöd. KJTR und Stephanus händ si nach de CNTR-Text a ere andere Stell (nach «mached Ussätzigi rein»)."]),
 ("VAR-SBLGNTAPP-MAT-010-010-01:R2", "MAT.10.10", "keinen Stab", "keine Stäbe", "kei Stäcke", "kei Stäcke (Mehrzahl)", "gering",
  "Plural: keine Stäbe; vielleicht als «keinen zusätzlichen Stab» verstanden.", "Mehrzahl: kei Stäcke; villicht als «kei zuesätzliche Stäcke» verstande.",
  {"R1": [("ῥάβδον", "keinen Stab", "WH, Treg, NA28")], "R2": [("ῥάβδους", "keine Stäbe", "RP")]},
  {"R1": [("ῥάβδον", "kei Stäcke", "WH, Treg, NA28")], "R2": [("ῥάβδους", "kei Stäcke (meh als eine)", "RP")]},
  ["Der Plural kann den Widerspruch zu [[MRK.6.8]] (ein Stab ist erlaubt) mildern: Verboten wären dann nur weitere Stäbe. Ebenso kann der Plural an die vorangehenden Plurale angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ῥάβδον, 04 und 032 ῥάβδους."],
  ["D Mehrzahl cha de Widerspruch zu [[MRK.6.8]] milte: Verbote wäred dänn nu wiiteri Stäcke. Oder si isch a di vorige Mehrzahle aaglichen.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ῥάβδον, 04 und 032 ῥάβδους."]),
 ("VAR-SBLGNTAPP-MAT-010-013-01:R2", "MAT.10.13", "zu euch zurückkehren", "auf euch zurückkehren", "zu eu zruggchoo", "uf eu zruggchoo", "gering",
  "Statt «zu euch» steht «auf euch»; der Friede kehrt auf die Boten zurück.", "Statt «zu eu» staat «uf eu».",
  {"R1": [("πρὸς ὑμᾶς", "zu euch", "Treg, NA28, RP")], "R2": [("ἐφʼ ὑμᾶς", "auf euch", "WH")]},
  {"R1": [("πρὸς ὑμᾶς", "zu eu", "Treg, NA28, RP")], "R2": [("ἐφʼ ὑμᾶς", "uf eu", "WH")]},
  ["ἐφʼ ὑμᾶς kann an ἐπʼ αὐτήν in der ersten Vershälfte angeglichen sein; ebenso kann πρὸς ὑμᾶς die geläufigere Verbindung mit «zurückkehren» sein, die eingesetzt wurde.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 032 ἐφʼ ὑμᾶς, 04 und 05 πρὸς ὑμᾶς."],
  ["ἐφʼ ὑμᾶς cha a ἐπʼ αὐτήν i de erschte Vershälfti aaglichen sii; oder πρὸς ὑμᾶς isch di gläufigeri Verbindig, wo iigsetzt worde isch.",
   "Nach de automatische Zueornig läsed 01, 03 und 032 ἐφʼ ὑμᾶς, 04 und 05 πρὸς ὑμᾶς."]),
 ("VAR-SBLGNTAPP-MAT-011-002-01:R2", "MAT.11.2", "sandte er durch seine Jünger", "sandte er zwei seiner Jünger", "hät er sini Jünger gschickt", "hät er zwei vo sine Jünger gschickt", "gering",
  "Johannes sendet zwei seiner Jünger.", "De Johannes schickt zwei vo sine Jünger.",
  {"R1": [("διά", "durch", "WH, Treg, NA28")], "R2": [("δύο", "zwei", "RP")]},
  {"R1": [("διά", "dur", "WH, Treg, NA28")], "R2": [("δύο", "zwei", "RP")]},
  ["δύο kann aus [[LUK.7.18]]–[[LUK.7.19]] (zwei Jünger) übernommen sein; die beiden Wörter sehen in Grossbuchstaben ähnlich aus (ΔΙΑ / ΔΥΟ), so dass auch ein Lesefehler in Frage kommt.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 032 und 05 διά; δύο führt sie nur für die Ausgaben KJTR, RP und Stephanus."],
  ["δύο cha us [[LUK.7.18]]–[[LUK.7.19]] übernoo sii; di zwei Wörter gsehnd i Grossbuechstabe ähnlich us (ΔΙΑ / ΔΥΟ), drum chunnt au en Läsfähler in Frag.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 032 und 05 διά; δύο nu d Usgabe KJTR, RP und Stephanus."]),
 ("VAR-SBLGNTAPP-MAT-011-008-02:R2", "MAT.11.8", "in den Häusern der Könige", "in den Königspalästen", "i de Hüüser vo de Könige", "i de Königspaläscht", "gering",
  "Statt «der Könige» steht «königlich»: in den Königshäusern, Palästen.", "Statt «vo de Könige» staat «königlich»: i de Paläscht.",
  {"R1": [("βασιλέων", "der Könige", "WH, Treg, NA28")], "R2": [("βασιλείων", "königlichen (Häusern)", "RP")]},
  {"R1": [("βασιλέων", "vo de Könige", "WH, Treg, NA28")], "R2": [("βασιλείων", "königliche (Hüüser)", "RP")]},
  ["Die beiden Formen unterscheiden sich in einem Buchstaben; die eine kann beim Abschreiben aus der anderen entstanden sein, βασιλείων vielleicht nach [[LUK.7.25]] (ἐν τοῖς βασιλείοις).",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 032 und 05 βασιλέων; βασιλείων führt sie nur für RP."],
  ["Di zwei Forme underscheided sich i eim Buechstabe; eini cha bim Abschriibe us de andere entstande sii, βασιλείων villicht nach [[LUK.7.25]].",
   "Nach de automatische Zueornig läsed 01, 03, 04, 032 und 05 βασιλέων; βασιλείων nu RP."]),
 ("VAR-SBLGNTAPP-MAT-011-010-01:R2", "MAT.11.10", "Dieser ist es", "Denn dieser ist es", "Dä isch es", "Dä isch es nämli", "gering",
  "Ein «denn» verbindet den Satz begründend mit [[MAT.11.9]].", "Es «nämli» verbindet de Satz mit [[MAT.11.9]].",
  {"R1": [("οὗτός", "Dieser", "WH, NA28")], "R2": [("οὗτος γάρ", "Denn dieser", "Treg, RP")]},
  {"R1": [("οὗτός", "Dä", "WH, NA28")], "R2": [("οὗτος γάρ", "Dä … nämli", "Treg, RP")]},
  ["γάρ kann zur Verdeutlichung des Zusammenhangs ergänzt sein; ebenso kann es ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne γάρ, 04 und 032 mit ihm."],
  ["γάρ cha ergänzt sii, für de Zämehang z verdütliche; oder es isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni γάρ, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-011-015-01:R2", "MAT.11.15", "Wer Ohren hat, der höre!", "Wer Ohren hat zu hören, der höre!", "Wer Ohre hät, dä söll lose!", "Wer Ohre hät zum ghööre, dä söll lose!", "gering",
  "Erweiterte Form des Weckrufs: Ohren, um zu hören.", "Erwiiterti Form: Ohre zum ghööre.",
  {"R1": [("ὦτα", "Ohren", "WH, NA28")], "R2": [("ὦτα ἀκούειν", "Ohren zu hören", "Treg, RP")]},
  {"R1": [("ὦτα", "Ohre", "WH, NA28")], "R2": [("ὦτα ἀκούειν", "Ohre zum ghööre", "Treg, RP")]},
  ["ἀκούειν kann nach der Form des Weckrufs bei Markus und Lukas ergänzt sein ([[MRK.4.9]], [[LUK.8.8]]); ebenso kann es weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 03 und 05 ohne ἀκούειν, 01, 04 und 032 mit ihm."],
  ["ἀκούειν cha nach de Form bi Markus und Lukas ergänzt sii ([[MRK.4.9]], [[LUK.8.8]]); oder es isch weggla worde.",
   "Nach de automatische Zueornig läsed 03 und 05 ohni ἀκούειν, 01, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-011-016-01:R2", "MAT.11.16", "die auf den Marktplätzen sitzen und den anderen zurufen", "die auf Marktplätzen sitzen und ihren Gefährten zurufen",
  "wo uf de Märt sitzed und de andere zuerüefed", "wo uf Märt sitzed und ire Kamerade zuerüefed", "gering",
  "Die Kinder rufen ihren Gefährten zu, nicht «den anderen».", "D Chind rüefed ire Kamerade zue, nöd «de andere».",
  {"R1": [("καθημένοις ἐν ταῖς ἀγοραῖς ἃ προσφωνοῦντα τοῖς ἑτέροις", "die auf den Marktplätzen sitzen und den anderen zurufen", "WH, Treg, NA28")],
   "R2": [("ἐν ἀγοραῖς καθημένοις καὶ προσφωνοῦσιν τοῖς ἑταίροις αὐτῶν", "die auf Marktplätzen sitzen und ihren Gefährten zurufen", "RP")]},
  {"R1": [("καθημένοις ἐν ταῖς ἀγοραῖς ἃ προσφωνοῦντα τοῖς ἑτέροις", "wo uf de Märt sitzed und de andere zuerüefed", "WH, Treg, NA28")],
   "R2": [("ἐν ἀγοραῖς καθημένοις καὶ προσφωνοῦσιν τοῖς ἑταίροις αὐτῶν", "wo uf Märt sitzed und ire Kamerade zuerüefed", "RP")]},
  ["ἑτέροις («anderen») und ἑταίροις («Gefährten») wurden in späterer Aussprache gleich gesprochen; die Verwechslung liegt nahe. Die Umstellung und das Verb im Indikativ glätten den Satz.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 032 und 05 die Form des SBLGNT; die andere führt sie nur für KJTR, RP und Stephanus. Nach der CNTR-Transkription hat 032 allerdings καὶ προσφωνουσιν τοις ετεροις αυτων, also Teile beider Formen."],
  ["ἑτέροις («andere») und ἑταίροις («Kamerade») händ spööter gliich tönt; e Verwächslig liit nooch. D Umstellig und s Verb im Indikativ mached de Satz glatter.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 032 und 05 d Form vom SBLGNT; 032 hät nach de CNTR-Transkription aber Teil vo beidne Forme."]),
 ("VAR-SBLGNTAPP-MAT-011-017-02:R2", "MAT.11.17", "wir haben Klagelieder gesungen", "wir haben euch Klagelieder gesungen", "mir händ Klaglieder gsunge", "mir händ eu Klaglieder gsunge", "gering",
  "Ein «euch» ergänzt den Parallelismus zum ersten Satzglied.", "Es «eu» ergänzt de Parallelismus zum erschte Satzglid.",
  {"R1": [("ἐθρηνήσαμεν", "wir haben Klagelieder gesungen", "WH, Treg, NA28")], "R2": [("ἐθρηνήσαμεν ὑμῖν", "wir haben euch Klagelieder gesungen", "RP")]},
  {"R1": [("ἐθρηνήσαμεν", "mir händ Klaglieder gsunge", "WH, Treg, NA28")], "R2": [("ἐθρηνήσαμεν ὑμῖν", "mir händ eu Klaglieder gsunge", "RP")]},
  ["ὑμῖν kann nach ηὐλήσαμεν ὑμῖν im ersten Satzglied ergänzt sein; ebenso kann es ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 05 ohne ὑμῖν, 04 und 032 mit ihm."],
  ["ὑμῖν cha nach em erschte Satzglid ergänzt sii; oder es isch usgfalle.",
   "Nach de automatische Zueornig läsed 01, 03 und 05 ohni ὑμῖν, 04 und 032 mit."]),
 ("VAR-SBLGNTAPP-MAT-011-019-01:R2", "MAT.11.19", "durch ihre Werke", "durch ihre Kinder", "dur iri Wärch", "dur iri Chind", "mittel",
  "Die Weisheit wird durch ihre Kinder ins Recht gesetzt, also durch die Menschen, die sie annehmen.", "D Wiisheit wird dur iri Chind is Rächt gsetzt, also dur d Mänsche, wo si aanämed.",
  {"R1": [("ἔργων", "Werke", "WH, Treg, NA28")], "R2": [("τέκνων", "Kinder", "RP")]},
  {"R1": [("ἔργων", "Wärch", "WH, Treg, NA28")], "R2": [("τέκνων", "Chind", "RP")]},
  ["τέκνων entspricht [[LUK.7.35]] und kann an Lukas angeglichen sein; ἔργων verbindet mit «den Werken des Christus» in [[MAT.11.2]]. Ebenso kann ἔργων eine bewusste Änderung sein, die den Satz an [[MAT.11.2]] anschliesst.",
   "Laut der automatischen Zuordnung lesen 01, 03 und 032 ἔργων, 04 und 05 τέκνων; in 03 setzt eine Korrektur τέκνων ein."],
  ["τέκνων entspricht [[LUK.7.35]] und cha a de Lukas aaglichen sii; ἔργων verbindet mit «de Wärch vom Christus» i [[MAT.11.2]]. Oder ἔργων isch e bewussti Änderig, wo de Satz a [[MAT.11.2]] aaschlüüsst.",
   "Nach de automatische Zueornig läsed 01, 03 und 032 ἔργων, 04 und 05 τέκνων; i 03 setzt e Korrektur τέκνων ii."]),
 ("VAR-SBLGNTAPP-MAT-011-020-01:R2", "MAT.11.20", "Da begann er", "Da begann Jesus", "Dänn hät er aagfange", "Dänn hät de Jesus aagfange", "gering",
  "Der Name Jesus steht ausdrücklich; der Sinn ändert sich nicht.", "De Name Jesus staat usdrücklich; de Sinn bliibt gliich.",
  {"R1": [("ἤρξατο", "begann er", "WH, Treg, RP, NA28")], "R2": [("ἤρξατο ὁ Ἰησοῦς", "begann Jesus", "NIV")]},
  {"R1": [("ἤρξατο", "hät er aagfange", "WH, Treg, RP, NA28")], "R2": [("ἤρξατο ὁ Ἰησοῦς", "hät de Jesus aagfange", "NIV")]},
  ["Der Name kann am Beginn eines neuen Abschnitts ergänzt worden sein, etwa für das Vorlesen im Gottesdienst.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 032 und 05 ohne den Namen; der Apparat nennt für den Zusatz nur NIV (den griechischen Text hinter der NIV)."],
  ["De Name cha am Aafang vo me neue Abschnitt ergänzt worde sii, öppe fürs Vorläse im Gottesdienscht.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 032 und 05 ohni de Name; de Apparat nännt für de Zuesatz nu NIV."]),
 ("VAR-SBLGNTAPP-MAT-011-023-01:R2", "MAT.11.23", "wirst du etwa bis zum Himmel erhöht werden?", "die du bis zum Himmel erhöht worden bist,",
  "wirsch öppe bis in Himel erhöcht wärde?", "wo du bis in Himel erhöcht worde bisch,", "mittel",
  "Statt einer Frage steht eine Aussage: Kafarnaum ist bis zum Himmel erhöht worden und wird hinabgestossen.", "Statt ere Frag staat e Ussag: Kafarnaum isch bis in Himel erhöcht worde.",
  {"R1": [("μὴ ἕως οὐρανοῦ ὑψωθήσῃ", "wirst du etwa bis zum Himmel erhöht werden?", "WH, Treg, NA28")], "R2": [("ἡ ἕως τοῦ οὐρανοῦ ὑψωθεῖσα", "die du bis zum Himmel erhöht worden bist", "RP")]},
  {"R1": [("μὴ ἕως οὐρανοῦ ὑψωθήσῃ", "wirsch öppe bis in Himel erhöcht wärde?", "WH, Treg, NA28")], "R2": [("ἡ ἕως τοῦ οὐρανοῦ ὑψωθεῖσα", "wo du bis in Himel erhöcht worde bisch", "RP")]},
  ["ΜΗ und Η unterscheiden sich in einem Buchstaben; wurde μή nach dem vorangehenden Καφαρναούμ (Endung -μ) übersehen, lag die Umdeutung zum Partizip nahe. Ebenso kann μή ergänzt worden sein, um den Anschluss an [[ISA.14.13]]–[[ISA.14.15]] als Frage zu gestalten.",
   "Laut der automatischen Zuordnung lesen 01, 03, 032 und 05 die Frage des SBLGNT. 04 hat sie als unklar eingestuft; nach der CNTR-Transkription steht dort μη εως του ουρανου υψωθηση, also die Frage mit Artikel."],
  ["ΜΗ und Η underscheided sich i eim Buechstabe; isch μή nach Καφαρναούμ (Ändig -μ) überseh worde, isch d Umdüütig zum Partizip nooch gläge. Oder μή isch ergänzt worde, für de Aaschluss a [[ISA.14.13]]–[[ISA.14.15]] als Frag z gstalte.",
   "Nach de automatische Zueornig läsed 01, 03, 032 und 05 d Frag; 04 hät nach de CNTR-Transkription d Frag mit Artikel."]),
 ("VAR-SBLGNTAPP-MAT-011-023-02:R2", "MAT.11.23", "wirst du hinabsteigen", "wirst du hinabgestossen werden", "wirsch abestiige", "wirsch abegstosse", "gering",
  "Passiv: Kafarnaum steigt nicht selbst hinab, sondern wird hinabgestossen.", "Passiv: Kafarnaum wird abegstosse.",
  {"R1": [("καταβήσῃ", "wirst du hinabsteigen", "WH, Treg, NA28")], "R2": [("καταβιβασθήσῃ", "wirst du hinabgestossen werden", "RP")]},
  {"R1": [("καταβήσῃ", "wirsch abestiige", "WH, Treg, NA28")], "R2": [("καταβιβασθήσῃ", "wirsch abegstosse", "RP")]},
  ["Das Passiv καταβιβασθήσῃ betont, dass Gott richtet, und kann als Verdeutlichung entstanden sein; ebenso kann καταβήσῃ die Form vereinfachen. Auch eine Angleichung an die Parallele [[LUK.10.15]] kommt in Frage.",
   "Laut der automatischen Zuordnung lesen 03, 032 und 05 καταβήσῃ, 01 und 04 καταβιβασθήσῃ."],
  ["S Passiv καταβιβασθήσῃ betont, dass Gott richtet, und cha als Verdüütlichung entstande sii; oder καταβήσῃ vereifacht d Form. Au e Aagliichig a [[LUK.10.15]] chunnt in Frag.",
   "Nach de automatische Zueornig läsed 03, 032 und 05 καταβήσῃ, 01 und 04 καταβιβασθήσῃ."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-010-001-042", "MAT.10.1-MAT.10.42", "section", "Die Aussendung der Zwölf",
  ["TU-MAT-010-001-004", "TU-MAT-010-005-015", "TU-MAT-010-016-025", "TU-MAT-010-026-033", "TU-MAT-010-034-042"],
  "Jesus gibt seinen zwölf Jüngern Vollmacht, unreine Geister auszutreiben und jede Krankheit zu heilen; ihre Namen werden aufgezählt. Er sendet sie zu den verlorenen Schafen des Hauses Israel, nicht zu den Heiden und Samaritanern: Sie sollen verkündigen, dass das Reich der Himmel nahe gekommen ist, Kranke heilen und Dämonen austreiben, umsonst und ohne Geld und Vorrat. Er kündigt ihnen Verfolgung an: Auslieferung an Gerichte, Geisselung in Synagogen, Entzweiung in den Familien und Hass um seines Namens willen; wer bis ans Ende standhält, wird gerettet. Sie sollen sich nicht vor Menschen fürchten; wer sich vor den Menschen zu ihm bekennt, zu dem wird er sich vor seinem Vater bekennen. Er sei nicht gekommen, Frieden zu bringen, sondern ein Schwert; wer Angehörige mehr liebt als ihn, ist seiner nicht würdig. Wer die Gesandten aufnimmt, nimmt ihn und den auf, der ihn gesandt hat. Dass die Zwölf aufbrechen, erzählt Matthäus nicht.", SEG),
 ("TU-MAT-010-001-004", "MAT.10.1-MAT.10.4", "narrative", "Die zwölf Apostel", None,
  "Jesus ruft seine zwölf Jünger zu sich und gibt ihnen Vollmacht über unreine Geister, sie auszutreiben und jede Krankheit und jedes Gebrechen zu heilen. Es folgen die Namen der zwölf Apostel, zuerst Simon, der Petrus genannt wird, zuletzt Judas Iskariot, der Jesus auch auslieferte.", None),
 ("TU-MAT-010-005-015", "MAT.10.5-MAT.10.15", "discourse", "Der Auftrag an die Zwölf", None,
  "Jesus sendet die Zwölf aus: Sie sollen nicht zu den Heiden und in keine Stadt der Samaritaner gehen, sondern zu den verlorenen Schafen des Hauses Israel. Unterwegs sollen sie verkündigen, dass das Reich der Himmel nahe gekommen ist, Kranke heilen, Tote aufwecken, Aussätzige rein machen und Dämonen austreiben, umsonst, wie sie es umsonst empfangen haben. Sie sollen sich kein Geld für den Gürtel verschaffen, keinen Beutel, keine zwei Untergewänder, keine Sandalen und keinen Stab, denn der Arbeiter ist seiner Nahrung wert. In jedem Ort sollen sie bei einem Würdigen bleiben und das Haus grüssen; wo man sie nicht aufnimmt und nicht hört, sollen sie den Staub von den Füssen schütteln. Jesus sagt, dem Land Sodom und Gomorra werde es am Tag des Gerichts erträglicher ergehen als einer solchen Stadt.", None),
 ("TU-MAT-010-016-025", "MAT.10.16-MAT.10.25", "discourse", "Verfolgung um Jesu willen", None,
  "Jesus sendet die Jünger wie Schafe mitten unter Wölfe; sie sollen klug sein wie die Schlangen und ohne Falsch wie die Tauben. Er kündigt an, man werde sie an Gerichte ausliefern, in den Synagogen geisseln und vor Statthalter und Könige führen; dann sollen sie sich nicht sorgen, was sie reden sollen, denn es werde ihnen gegeben, und der Geist ihres Vaters rede in ihnen. Bruder werde Bruder in den Tod ausliefern, Kinder würden sich gegen die Eltern erheben, und um seines Namens willen würden sie von allen gehasst; wer bis ans Ende standhält, wird gerettet. Werden sie in einer Stadt verfolgt, sollen sie in die andere fliehen; mit den Städten Israels würden sie nicht zu Ende kommen, bis der Menschensohn kommt. Der Jünger steht nicht über dem Lehrer: Wenn man den Hausherrn Beelzebul genannt hat, dann umso mehr seine Hausgenossen.", None),
 ("TU-MAT-010-026-033", "MAT.10.26-MAT.10.33", "discourse", "Fürchtet euch nicht", None,
  "Jesus sagt den Jüngern, sie sollen sich vor ihren Gegnern nicht fürchten: Nichts Verhülltes bleibt verborgen, und was er ihnen im Dunkeln sagt, sollen sie im Licht und auf den Dächern verkündigen. Sie sollen nicht die fürchten, die den Leib töten, aber die Seele nicht töten können, sondern den, der Seele und Leib in der Hölle verderben kann. Kein Spatz fällt ohne ihren Vater auf die Erde, und selbst ihre Haare sind gezählt; sie sind mehr wert als viele Spatzen. Wer sich vor den Menschen zu Jesus bekennt, zu dem wird er sich vor seinem Vater in den Himmeln bekennen; wer ihn verleugnet, den wird er auch verleugnen.", None),
 ("TU-MAT-010-034-042", "MAT.10.34-MAT.10.42", "discourse", "Nicht Frieden, sondern ein Schwert", None,
  "Jesus sagt, er sei nicht gekommen, Frieden auf die Erde zu bringen, sondern ein Schwert: Er sei gekommen, Menschen mit ihren nächsten Angehörigen zu entzweien, und die eigenen Hausgenossen würden zu Feinden. Wer Vater oder Mutter, Sohn oder Tochter mehr liebt als ihn oder sein Kreuz nicht auf sich nimmt und ihm nachfolgt, ist seiner nicht würdig; wer sein Leben gefunden hat, wird es verlieren, wer es um seinetwillen verloren hat, wird es finden. Wer die Jünger aufnimmt, nimmt ihn auf und den, der ihn gesandt hat. Wer einen Propheten oder Gerechten aufnimmt, empfängt dessen Lohn, und wer einem dieser Kleinen, weil er ein Jünger ist, auch nur einen Becher kaltes Wasser gibt, wird seinen Lohn gewiss nicht verlieren.", None),
 ("TU-MAT-011-001-030", "MAT.11.1-MAT.11.30", "section", "Johannes der Täufer, die unbussfertigen Städte und der Ruf Jesu",
  ["TU-MAT-011-001-006", "TU-MAT-011-007-015", "TU-MAT-011-016-019", "TU-MAT-011-020-024", "TU-MAT-011-025-030"],
  "Nach den Anweisungen an die Zwölf zieht Jesus weiter, um zu lehren und zu verkündigen. Der gefangene Johannes lässt fragen, ob Jesus der Kommende sei; Jesus verweist auf das, was die Boten hören und sehen. Vor der Menge nennt Jesus Johannes mehr als einen Propheten, den angekündigten Boten und Elija, der kommen soll, und vergleicht dieses Geschlecht mit Kindern auf dem Marktplatz, die den anderen vorwerfen, sie hätten weder getanzt noch geklagt: Johannes wie dem Menschensohn wirft man etwas vor. Er schilt Chorazin, Betsaida und Kafarnaum, weil sie trotz seiner Machttaten nicht umgekehrt sind. Dann preist er den Vater, der dies den Unmündigen offenbart hat, sagt, niemand kenne den Vater ausser dem Sohn und dem, dem der Sohn es offenbaren will, und lädt alle, die sich abmühen und beladen sind, ein, sein Joch auf sich zu nehmen und Ruhe zu finden.", SEG),
 ("TU-MAT-011-001-006", "MAT.11.1-MAT.11.6", "dialogue", "Die Anfrage des Täufers", None,
  "Als Jesus seine Anweisungen an die Zwölf beendet hat, zieht er weiter, um in ihren Städten zu lehren und zu verkündigen. Johannes hört im Gefängnis von den Werken des Christus und lässt Jesus durch seine Jünger fragen, ob er der Kommende sei oder ob sie auf einen anderen warten sollen. Jesus antwortet, sie sollen Johannes berichten, was sie hören und sehen: Blinde sehen wieder, Lahme gehen umher, Aussätzige werden rein, Taube hören, Tote werden auferweckt, und den Armen wird das Evangelium verkündigt; selig ist, wer an ihm keinen Anstoss nimmt.", "[[MAT.11.1]] schliesst die Aussendungsrede ab und steht hier als Überleitung."),
 ("TU-MAT-011-007-015", "MAT.11.7-MAT.11.15", "discourse", "Jesus über Johannes", None,
  "Als die Boten gehen, fragt Jesus die Menge, was sie in der Wüste sehen wollten: ein Schilfrohr im Wind oder einen Menschen in weichen Kleidern? Einen Propheten, ja mehr als einen Propheten. Johannes ist der Bote, von dem geschrieben steht, dass er den Weg bereiten wird ([[MAL.3.1]]). Unter den von Frauen Geborenen ist kein Grösserer aufgetreten als er, doch der Kleinste im Reich der Himmel ist grösser als er. Seit den Tagen des Johannes leidet das Reich der Himmel Gewalt; alle Propheten und das Gesetz haben bis zu Johannes prophezeit, und wenn sie es annehmen wollen, ist er Elija, der kommen soll. Wer Ohren hat, der höre.", None),
 ("TU-MAT-011-016-019", "MAT.11.16-MAT.11.19", "discourse", "Die Kinder auf dem Marktplatz", None,
  "Jesus vergleicht dieses Geschlecht mit Kindern auf den Marktplätzen, die den anderen vorwerfen, sie hätten nicht getanzt, als sie Flöte spielten, und sich nicht an die Brust geschlagen, als sie Klagelieder sangen. Von Johannes, der gekommen ist, ohne zu essen und zu trinken, sagt man, er habe einen Dämon; vom Menschensohn, der isst und trinkt, sagt man, er sei ein Fresser und Weinsäufer, ein Freund von Zöllnern und Sündern. Und doch ist die Weisheit durch ihre Werke gerechtfertigt worden.", None),
 ("TU-MAT-011-020-024", "MAT.11.20-MAT.11.24", "discourse", "Weherufe über die Städte", None,
  "Jesus schilt die Städte, in denen die meisten seiner Machttaten geschehen sind, weil sie nicht umgekehrt sind. Er ruft Wehe über Chorazin und Betsaida: Wären in Tyrus und Sidon solche Machttaten geschehen, wären sie längst in Sack und Asche umgekehrt; am Tag des Gerichts werde es Tyrus und Sidon erträglicher ergehen als ihnen. Kafarnaum fragt er, ob es etwa bis zum Himmel erhöht werde, und sagt, es werde ins Totenreich hinabsteigen; wären in Sodom solche Machttaten geschehen, stünde es noch heute, und dem Land Sodom werde es am Tag des Gerichts erträglicher ergehen als Kafarnaum.", None),
 ("TU-MAT-011-025-030", "MAT.11.25-MAT.11.30", "discourse", "Lobpreis des Vaters und Einladung zur Ruhe", None,
  "Jesus preist den Vater, den Herrn des Himmels und der Erde, dass er dies vor Weisen und Verständigen verborgen und Unmündigen offenbart hat, denn so hat es ihm gefallen. Alles ist ihm von seinem Vater übergeben; niemand kennt den Sohn ausser dem Vater, und niemand den Vater ausser dem Sohn und dem, dem der Sohn es offenbaren will. Er ruft alle, die sich abmühen und beladen sind, zu sich und sagt, er werde ihnen Ruhe geben: Sie sollen sein Joch auf sich nehmen und von ihm lernen, denn er ist sanftmütig und demütig im Herzen; sein Joch ist sanft und seine Last leicht.", None),
]
UNITS_GSW = {
 "TU-MAT-010-001-042": ("D Ussändig vo de Zwölf", "De Jesus git sine zwölf Jünger Vollmacht, unreini Geischter usztriibe und jedi Chrankheit z heile; ire Näme wärded ufzellt. Er schickt si zu de verlorene Schaf vom Huus Israel, nöd zu de Heide und Samaritaner: Si söled verchünde, dass s Riich vo de Himel nöch choo isch, Chranki heile und Dämone ustriibe, umesuscht und ohni Gäld und Vorrat. Er seit ine Verfolgig aa: Si wärded a Gricht usgliferet, i Synagoge geisslet, d Familie wärded entzweit, und wäge sim Name wärded si ghasst; wer bis as Änd durehebt, wird grettet. Si söled sich nöd vor Mänsche förchte; wer sich vor de Mänsche zu ihm bekännt, zu däm bekännt er sich vor sim Vatter. Er sig nöd choo, für Fride z bringe, sondern es Schwärt; wer sini Aaghörige meh gärn hät als ihn, isch ihn nöd wärt. Wer d Gschickte ufnimmt, nimmt ihn uf und dä, wo ihn gschickt hät. Dass d Zwölf ufbreched, verzellt de Matthäus nöd."),
 "TU-MAT-010-001-004": ("D Zwölf Apostel", "De Jesus rüeft sini zwölf Jünger zu sich und git ine Vollmacht über unreini Geischter, für si usztriibe und jedi Chrankheit und jedes Gebräche z heile. Dänn chömed d Näme vo de zwölf Apostel, zerscht de Simon, wo Petrus gnännt wird, zletscht de Judas Iskariot, wo de Jesus au usgliferet hät."),
 "TU-MAT-010-005-015": ("De Uftrag a d Zwölf", "De Jesus schickt d Zwölf us: Si söled nöd zu de Heide und i kei Stadt vo de Samaritaner gaa, sondern zu de verlorene Schaf vom Huus Israel. Underwägs söled si verchünde, dass s Riich vo de Himel nöch choo isch, Chranki heile, Toti ufwecke, Ussätzigi rein mache und Dämone ustriibe, umesuscht, wie si s umesuscht übercho händ. Si söled sich kei Gäld für de Gürtel aaschaffe, kei Täsche, nöd zwei Underchleider, kei Sandale und kei Stäcke, dänn de Arbeiter isch sis Ässe wärt. I jedem Ort söled si bi eim bliibe, wo s wärt isch, und s Huus grüesse; wo me si nöd ufnimmt und nöd uf si lost, söled si de Staub vo de Füess schüttle. De Jesus seit, em Land Sodom und Gomorra gang s am Tag vom Gricht erträglicher als ere settige Stadt."),
 "TU-MAT-010-016-025": ("Verfolgig wäge em Jesus", "De Jesus schickt d Jünger wie Schaf mitten under Wölf; si söled gschiid sii wie d Schlange und ohni Falsch wie d Tuube. Er seit aa, me wärd si a Gricht uslifere, i de Synagoge geissle und vor Statthalter und Könige füere; dänn söled si sich kei Sorge mache, was si söled rede, wil s ine ggää wärd, und de Geischt vo irem Vatter red i ine. En Brueder wärd de Brueder in Tod uslifere, Chind wärded sich gäge d Eltere ufläne, und wäge sim Name wärded si vo allne ghasst; wer bis as Änd durehebt, wird grettet. Wänn me si i ere Stadt verfolgt, söled si i di ander flüchte; mit de Stedt vo Israel wärded si nöd fertig, bis de Mänschesohn chunnt. De Jünger staat nöd über em Lehrer: Wänn me de Huusherr Beelzebul gnännt hät, dänn erscht rächt sini Huusgnosse."),
 "TU-MAT-010-026-033": ("Förchted eu nöd", "De Jesus seit de Jünger, si söled sich vor irne Gägner nöd förchte: Nüüt Verdeckts bliibt verborge, und was er ine i de Fiischteri seit, söled si im Liecht und uf de Dächer verchünde. Si söled nöd die förchte, wo de Liib töded, aber d Seel nöd töde chönd, sondern dä, wo d Seel und de Liib i de Höll cha zgrund richte. Kei Spatz gheit ohni ire Vatter uf de Bode, und sogar iri Haar sind zellt; si sind meh wärt als vil Spatze. Wer sich vor de Mänsche zum Jesus bekännt, zu däm bekännt er sich vor sim Vatter i de Himel; wer ihn verleugnet, dä verleugnet er au."),
 "TU-MAT-010-034-042": ("Nöd Fride, sondern es Schwärt", "De Jesus seit, er sig nöd choo, für Fride uf d Ärde z bringe, sondern es Schwärt: Er sig choo, für Mänsche mit irne nöchschte Aaghörige z entzweie, und di eigete Huusgnosse wärded zu Fiind. Wer Vatter oder Mueter, Sohn oder Tochter meh gärn hät als ihn oder sis Chrüüz nöd uf sich nimmt und ihm nachefolget, isch ihn nöd wärt; wer sis Läbe gfunde hät, wird s verlüüre, wer s wäge ihm verloore hät, wird s finde. Wer d Jünger ufnimmt, nimmt ihn uf und dä, wo ihn gschickt hät. Wer en Prophet oder en Grächte ufnimmt, überchunnt dä sin Loon, und wer eim vo dene Chliine, wil er en Jünger isch, au nu en Bächer chalts Wasser git, wird sin Loon sicher nöd verlüüre."),
 "TU-MAT-011-001-030": ("De Johannes de Täufer, d Stedt, wo nöd umchered, und de Ruef vom Jesus", "Nach de Aawiisige a d Zwölf zieht de Jesus wiiter, für z lehre und z verchünde. De Johannes im Gfängnis laat fröge, öb de Jesus dä sig, wo chunnt; de Jesus verwiist uf das, was d Bote ghöred und gseend. Vor de Mängi nännt de Jesus de Johannes meh als en Prophet, de aagchündet Bote und de Elija, wo söll choo, und vergliicht die Generation mit Chind uf em Märt, wo de andere vorwärfed, si heiged weder tanzet no klagt: Em Johannes wie em Mänschesohn wirft me öppis vor. Er schimpft Chorazin, Betsaida und Kafarnaum us, wil si trotz sine Chrafttate nöd umgchehrt sind. Dänn priist er de Vatter, wo das de Unmündige offebart hät, seit, niemer känn de Vatter usser de Sohn und dä, wo s de Sohn ihm wott offebare, und rüeft alli, wo sich abmüehed und schwär z träge händ, sis Joch uf sich z nää und Rue z finde."),
 "TU-MAT-011-001-006": ("D Aafrag vom Täufer", "Wo de Jesus mit de Aawiisige a d Zwölf fertig isch, zieht er wiiter, für i irne Stedt z lehre und z verchünde. De Johannes ghört im Gfängnis vo de Wärch vom Christus und laat de Jesus dur sini Jünger fröge, öb er dä sig, wo chunnt, oder öb si uf en andere söled warte. De Jesus antwortet, si söled em Johannes verzelle, was si ghöred und gseend: Blindi gseend wider, Lahmi laufed, Ussätzigi wärded rein, Taubi ghöred, Toti wärded uferweckt, und de Arme wird s Evangelium verchündet; sälig isch, wer a ihm kei Aastoss nimmt."),
 "TU-MAT-011-007-015": ("De Jesus über de Johannes", "Wo d Bote gönd, fröget de Jesus d Mängi, was si i de Wüeschti händ wele gseh: es Schilfrohr im Wind oder en Mänsch i weiche Chleider? En Prophet, ja meh als en Prophet. De Johannes isch de Bote, vo däm gschribe staat, dass er de Wäg parat macht ([[MAL.3.1]]). Under dene, wo vo Fraue gebore sind, isch kei Grössere uftrete als er, aber de Chliinscht im Riich vo de Himel isch grösser als er. Sit de Täg vom Johannes tuet me em Riich vo de Himel Gwalt aa; alli Prophete und s Gsetz händ bis zum Johannes prophezeit, und wänn si s wänd aanää, isch er de Elija, wo söll choo. Wer Ohre hät, söll lose."),
 "TU-MAT-011-016-019": ("D Chind uf em Märt", "De Jesus vergliicht die Generation mit Chind uf em Märt, wo de andere vorwärfed, si heiged nöd tanzet, wo si uf de Flöte gspilt händ, und sich nöd a d Bruscht gschlage, wo si Klaglieder gsunge händ. Vom Johannes, wo choo isch, ohni z ässe und z trinke, seit me, er heig en Dämon; vom Mänschesohn, wo isst und trinkt, seit me, er sig en Frässer und Süffel, en Fründ vo Zöllner und Sünder. Und doch isch d Wiisheit dur iri Wärch is Rächt gsetzt worde."),
 "TU-MAT-011-020-024": ("Wee über d Stedt", "De Jesus schimpft d Stedt us, wo di meischte vo sine Chrafttate passiert sind, wil si nöd umgchehrt sind. Er rüeft Wee über Chorazin und Betsaida: Wäred z Tyrus und Sidon settig Chrafttate passiert, wäred si scho lang in Sack und Äsche umgchehrt; am Tag vom Gricht gang s Tyrus und Sidon erträglicher als ine. Kafarnaum fröget er, öb s öppe bis in Himel erhöcht wärd, und seit, es wärd is Toterich abestiige; wäred z Sodom settig Chrafttate passiert, stünd s hüt no, und em Land Sodom gang s am Tag vom Gricht erträglicher als Kafarnaum."),
 "TU-MAT-011-025-030": ("De Vatter priise und zur Rue iilade", "De Jesus priist de Vatter, de Herr vom Himel und vo de Ärde, dass er das vor Wiise und Verständige verborge und de Unmündige offebart hät, wil s ihm eso gfalle hät. Alles isch ihm vo sim Vatter übergää; niemer kännt de Sohn usser de Vatter, und niemer de Vatter usser de Sohn und dä, wo s de Sohn ihm wott offebare. Er rüeft alli zu sich, wo sich abmüehed und schwär z träge händ, und seit, er gäb ine Rue: Si söled sis Joch uf sich nää und vo ihm lerne, wil er sanftmüetig und demüetig im Härz isch; sis Joch isch sanft und sini Lascht liecht."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "Widerspricht die automatische Zuordnung den Sigla des SBLGNT-Apparats, gilt der Apparat; die Abweichung ist bei der "
  "Alternative benannt (z. B. [[MAT.10.8]]: KJTR und Stephanus haben die Worte an anderer Stelle). Zahlen zu Wortvorkommen "
  "sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts gezählt."),
 ("Umfang: [[MAT.10.1-MAT.10.42]] (Aussendungsrede, die zweite der fünf grossen Reden des Matthäus) und [[MAT.11.1-MAT.11.30]]. "
  "[[MAT.11.1]] schliesst die Rede mit der Formel ab, die alle fünf Reden beendet ([[MAT.7.28]], [[MAT.13.53]], [[MAT.19.1]], "
  "[[MAT.26.1]]); die Gliederung stellt den Vers als Überleitung zu [[MAT.11.2-MAT.11.6]]. Im SBLGNT fehlt in Kapitel 10–11 kein Vers."),
 ("Gemeinsame Begriffe für das ganze Matthäusevangelium (verbindliche Liste für alle Kapitelbereiche): «das Reich der "
  "Himmel», «der Menschensohn», «Amen, ich sage euch», «Vater in den Himmeln», «siehe», «da/dann» für τότε, «kehrt um / "
  "Umkehr», «Dämon», «Christus», Schriftgelehrte, Pharisäer usw. Jede Wiedergabe ist eine redaktionelle Entscheidung, keine "
  "geprüfte Festlegung."),
 ("In diesem Bereich neu festgelegte Wiedergaben (Vorschlag für die übrigen Kapitel): μακάριος «selig» (Mundart «sälig»); "
  "σκανδαλίζω passiv «Anstoss nehmen», aktiv «zu Fall bringen» (wie Markus); ἄξιος «würdig», beim Lohn «wert» (Mundart "
  "durchgehend «wärt»); πᾶσα νόσος καὶ πᾶσα μαλακία «jede Krankheit und jedes Gebrechen»; δυνάμεις «Machttaten» (Mundart "
  "«Chrafttate», wie Markus); γενεά «Geschlecht» (Mundart «Generation», wie Markus); τὰ ἔθνη im Gegenüber zu Israel «die "
  "Heiden» (Mundart «d Heide»), sonst «die Völker»; παραδίδωμι «ausliefern» (beim Vater [[MAT.11.27]] «übergeben»); "
  "γέεννα «Hölle», ᾅδης «Totenreich» (Mundart «Höll», «Toterich»); ψυχή je nach Zusammenhang «Seele» oder «Leben», mit "
  "Entscheidung; οἱ ὄχλοι «die Menge» (Mundart «d Mängi»); δοῦλος im Gegenüber zu κύριος «Knecht» (Mundart «Chnächt»); "
  "εὐαγγελίζομαι «das Evangelium verkündigen»; μεριμνάω «sich sorgen»."),
 ("Erzählweise und Redegrenzen: Anführungszeichen sind eine Entscheidung der Übersetzung, denn das Griechische hat keine. "
  "Die Aussendungsrede läuft von [[MAT.10.5]] bis [[MAT.10.42]]; in Kapitel 11 stehen die Reden [[MAT.11.4]]–[[MAT.11.6]], "
  "[[MAT.11.7]]–[[MAT.11.19]], [[MAT.11.21]]–[[MAT.11.24]] und [[MAT.11.25]]–[[MAT.11.30]] in Anführungszeichen. "
  "Wörtliche Rede innerhalb der Rede steht in ‹ ›. ὅτι und λέγων vor direkter Rede sind nicht eigens übersetzt."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens. Abweichende Lesarten stehen als Alternativen, soweit sie die Übersetzung "
  "verändern; Lesarten, die nur Schreibung, Wortstellung, Artikel oder Zeitform ohne Wirkung auf die Übersetzung betreffen, "
  "sind nicht aufgenommen. In [[MAT.11.9]] folgt die Übersetzung der Zeichensetzung des SBLGNT (siehe decisions)."),
 "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Gmeinsami Begriff fürs Matthäusevangelium: «s Riich vo de Himel», «de Mänschesohn», «Amen, ich säg eu», «Vatter i de "
  "Himel», «lueg», «dänn» für τότε (für γάρ drum «nämli»), «chehred um / Umkehr», «Dämon», «Christus». Neu i dem Bereich: "
  "μακάριος «sälig», σκανδαλίζω «Aastoss nää» / «z Fall bringe», ἄξιος «wärt», δυνάμεις «Chrafttate», γενεά «Generation», "
  "ἔθνη «Heide», γέεννα «Höll», ᾅδης «Toterich», ὄχλοι «Mängi», δοῦλος «Chnächt», φιλέω «gärn haa»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Johannes»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«s Riich vo de Himel»); s Präsens staat oft für s Futur."),
 "Eigeti Formulierig; nöd us ere veröffentlichte Mundart-Bible übernoo.",
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Liecht, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Namen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; wiederkehrende Begriffe des Matthäus einheitlich (siehe translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": f"« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt ({SCRIPT}).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 10–11 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
