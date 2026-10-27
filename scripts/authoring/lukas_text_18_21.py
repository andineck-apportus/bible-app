#!/usr/bin/env python3
"""Autorenwerkzeug: Lukas 18–21 (Gleichnisse vom Beten, Weg nach Jerusalem, Zachäus, Einzug, Streitgespräche im Tempel,
Endzeitrede) – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT,
Übersetzungsentscheidungen, Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/lukas_text_18_21.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-LUK besteht bereits (scripts/authoring/vaterunser.py) und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Lukas 18–21 fehlt im SBLGNT kein Vers; alle Verse haben Tokens.
- Die Erzählformel ἐγένετο «es geschah» ist am Abschnittsbeginn wiedergegeben ([[LUK.18.35]], [[LUK.20.1]]), innerhalb
  eines Abschnitts nicht eigens ([[LUK.19.15]], [[LUK.19.29]]); gemeinsame Regel für ganz Lukas, siehe decisions.
- παραδίδωμι ist wie bei Markus durchgehend «ausliefern»; ὅτι vor direkter Rede ist nicht eigens übersetzt.
- Die Mundart folgt der Dieth-Schreibung und der Wortwahl der bisherigen Züridüütsch-Fassungen (Markus, Johannes);
  Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv.

KI-Entwurf (Claude) vom 2026-10-26 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1,
data/witness-readings/WREAD-CNTR-LUK-018-…–021-…) bzw. aus der CNTR-Transkription (Sekundärtranskription), nicht aus
eigener Prüfung der Handschriften.

Vereinheitlichung 2026-10-26 (gemeinsam für alle sechs Lukas-Werkzeuge; Texte und Begründungen in
scripts/authoring/lukas_einheitlich.py, Zählung dort):
- ἐγένετο als Erzählformel am Abschnittsbeginn wiedergegeben (καὶ ἐγένετο «Und es geschah» / «Und es isch gsii»,
  ἐγένετο δέ «Es geschah aber» / «Es isch aber gsii», wie [[LUK.11.1]]), innerhalb eines Abschnitts nicht eigens (~n).
- ἰδού: Erzählung «siehe» / «lueg»; direkte Rede «sieh» / «seht» bzw. «lueg» / «lueged» nach Zahl der Angesprochenen.
- μὴ φοβοῦ / μὴ φοβεῖσθε: Mundart «Häb kei Angscht» / «Händ kei Angscht».
- οἱ ὄχλοι «die Menschenmengen» / «d Lüüt»; ὄχλος «die Menge» / «d Mängi»; νομικός «Gesetzeslehrer» / «Gsetzeslehrer».
- οὐαί «Weh»; ἀληθῶς «Wahrhaftig»; ἀποκριθεὶς ohne Frage «ergriff das Wort» / «hät s Wort gnoo»; εὐθέως «sofort» /
  «grad», παραχρῆμα «sofort» / «sofort»; πλήν Mundart «aber».
- Mundart-Schreibung nach der Mehrheit in Markus und Johannes (run() prüft sie mit pruefe_mundart):
  userwählt (statt uuserwäält/uuserwählt) · userwählte (statt uuserwäälte) · lehrt (statt leert) · glehrt (statt
  gleert) · lehre (statt leere) · lehr (statt leer) · dört (statt det) · chnü (statt chnüü) · usggää (statt usgää) ·
  gscheh (statt gschee) · mueterliib (statt muetterliib) · wiitergange (statt witergange) · fürchte (statt förchte) ·
  fürchted (statt förchted) · fürcht (statt förcht) · gfürchtet (statt gförchtet) · elei (statt ellei) · frömde (statt
  fremde) · ggässe (statt gässe) · ghöre (statt ghööre) · ghöred (statt ghööred) · ghüratet (statt ghüraatet) ·
  hüratet (statt hüraatet) · verhüratet (statt verhüraatet) · glöst (statt glööst) · gmäldet (statt gmeldet) · mäldet
  (statt meldet) · höchi (statt hööchi) · gröscht (statt grööscht) · grössi (statt gröössi) · herde (statt härde) ·
  iigschlaafe (statt iigschlafe) · chöm (statt chömm) · chömende (statt chömmende) · chönt (statt chönnt) · chönted
  (statt chönnted) · fälder (statt felder) · riitet (statt rittet) · schaf (statt schaaf) · städt (statt stedt) ·
  stärbe (statt sterbe) · strited (statt striited) · tüüre (statt türe) · ufgläse (statt ufglääse) · uftrete (statt
  ufträte) · umkehr (statt umchehr) · ungläubig (statt unglöubig) · ussendig (statt uussändig) · usfüerlich (statt
  uusfüerlich) · usgaat (statt uusgaat) · usrichte (statt uusrichte) · ustriibed (statt uustriibed) · verdorret (statt
  verdoret) · verdorreti (statt verdoreti) · verdorrete (statt verdorete) · verrisse (statt verriisse) · villicht
  (statt vilicht) · wäggange (statt weggange) · wäg (statt wägg) · wem (statt wäm) · wän (statt wen) · wärdi (statt
  werdi) · wärfed (statt werfed) · zrugggange (statt zruggange) · zruggchoo (statt zruggcho) · anechoo (statt anecho)
  · choo (statt cho) · zügnis (statt züügnis) · böse (statt bööse) · böses (statt bööses) · greber (statt gräber) ·
  schnell (statt schnäll) · jahr (statt jaar) · ohre (statt oore) · lohn (statt loon) · söhn (statt söön) · glähmt
  (statt gläämt) · glähmte (statt gläämte) · zie (statt zieh) · ziend (statt ziehnd) · zieht (statt ziet) · wonige
  (statt wohnige) · fahr (statt faar) · fahred (statt faared) · fahrt (statt faart) · gfahre (statt gfaare) · befole
  (statt befohle) · fäält (statt fehlt) · nöi (statt nöii) · da (statt daa) · häre (statt here) · liide (statt lide) ·
  legged (statt leged) · söle (statt sölle) · nöch (statt nööch) · nöchi (statt nööchi) · fäschtässe (statt
  feschtässe)
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, write  # noqa: E402
from lukas_einheitlich import (EGEN_DE, EGEN_GSW, EGEN_SKIP_DE, EGEN_SKIP_GSW, IDOU_DE, IDOU_GSW, FURCHT_GSW,  # noqa: E402,F401
                              OCHLOI_DE, pruefe_mundart)

DATE = "2026-10-26"
AUTH = "KI-Entwurf (Claude) vom 2026-10-26 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-26 auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-LUKE"]
CHAPTERS = ((18, 43), (19, 48), (20, 47), (21, 38))
RIGHT = "ὅτι leitet die direkte Rede ein"
RIGHT_G = "ὅτι leitet di diräkt Red ii"
EGEN = EGEN_SKIP_DE
EGEN_G = EGEN_SKIP_GSW

DE = {
 # ------------------------------------------------------------ Kapitel 18
 "LUK.18.1": "[Er erzählte]{1} [ihnen]{4} [aber]{2} [ein Gleichnis]{3} [darüber, dass]{5,6} [sie]{10} [allezeit]{8} [beten]{9} und{11} [nicht]{12} [den Mut verlieren]{13} [sollten]{7}.",
 "LUK.18.2": "[Er sagte]{1}: «[In]{5} [einer]{6} [Stadt]{7} [war]{4} [ein]{3} [Richter]{2}, der [Gott]{8,9} [nicht]{10} [fürchtete]{11} und{12} [auf keinen]{14} [Menschen]{13} [Rücksicht nahm]{15}.",
 "LUK.18.3": "[In]{4} [jener]{7} [Stadt]{5,6} [war]{3} [aber]{2} [eine Witwe]{1}, und{8} [sie kam immer wieder]{9} [zu]{10} [ihm]{11} [und sagte]{12}: ‹[Verschaffe]{13} [mir]{14} [Recht]{13} [gegen]{15} [meinen]{18} [Gegner]{16,17}!›",
 "LUK.18.4": "Und{1} [eine Zeit lang]{4,5} [wollte er]{3} [nicht]{2}. [Danach]{6,7} [aber]{8} [sagte er]{9} [sich]{10,11}: ‹[Auch wenn]{12,13} [ich]{17} [Gott]{14,15} [nicht]{16} [fürchte]{17} [und auf keinen]{18} [Menschen]{19} [Rücksicht nehme]{20},",
 "LUK.18.5": "[weil]{1,3} [mir]{5} [diese]{9} [Witwe]{7,8} [nun einmal]{2} [Mühe]{6} [macht]{4}, [werde ich]{10} [ihr]{11} [Recht verschaffen]{10}, [damit]{12} [sie]{16} [nicht]{13} [ohne Ende]{14,15} [kommt]{16} und [mich]{18} [zermürbt]{17}.›»",
 "LUK.18.6": "[Der Herr]{3,4} [aber]{2} [sagte]{1}: «[Hört]{5}, [was]{6} [der]{7} [ungerechte]{9,10} [Richter]{8} [sagt]{11}!",
 "LUK.18.7": "[Sollte]{6} [Gott]{1,3} [aber]{2} [seinen]{11} [Auserwählten]{9,10} [nicht]{4,5} [Recht]{7,8} [verschaffen]{6}, [die]{12} [Tag]{15} und{16} [Nacht]{17} [zu ihm]{14} [schreien]{13}? Und{18} [lässt er]{19} [sie]{20,21} [warten]{19}?",
 "LUK.18.8": "[Ich sage]{1} [euch]{2}: [Er wird]{4} [ihnen]{7} [Recht]{5,6} [verschaffen]{4}, und zwar [schnell]{8,9}. [Doch]{10} [wird]{17} [der Menschensohn]{11-14}, [wenn er kommt]{15}, [wohl]{16} [den Glauben]{18,19} [auf]{20} [der Erde]{21,22} [finden]{17}?» ~3(" + RIGHT + ")",
 "LUK.18.9": "[Er erzählte]{1} [aber]{2} [auch]{3} [einigen]{4,5}, [die]{6} [von sich]{8,9} [überzeugt waren]{7}, [dass]{10} [sie]{11} [gerecht]{12} [seien]{11}, und{13} [die anderen]{15,16} [verachteten]{14}, [dieses]{19} [Gleichnis]{17,18}:",
 "LUK.18.10": "«[Zwei]{2} [Menschen]{1} [gingen]{3} [in]{4} [den Tempel]{5,6} [hinauf]{3}, [um zu beten]{7}, [der]{8} [eine]{9} [ein Pharisäer]{10} und{11} [der]{12} [andere]{13} [ein Zöllner]{14}.",
 "LUK.18.11": "[Der Pharisäer]{1,2} [stellte sich hin]{3} [und betete]{7} [bei sich]{4,5} [so]{6}: ‹[Gott]{8,9}, [ich danke]{10} [dir]{11}, [dass]{12} [ich]{14} [nicht]{13} [bin]{14} [wie]{15} [die übrigen]{16,17} [Menschen]{18,19}: [Räuber]{20}, [Ungerechte]{21}, [Ehebrecher]{22}, [oder]{23} [auch]{24} [wie]{25} [dieser]{26} [Zöllner]{27,28} da.",
 "LUK.18.12": "[Ich faste]{1} [zweimal]{2} [in der Woche]{3,4}, [ich gebe den Zehnten]{5} [von allem]{6}, [was]{7} [ich einnehme]{8}.›",
 "LUK.18.13": "[Der Zöllner]{1,3} [aber]{2} [stand]{5} [weit entfernt]{4} [und wollte]{7} [nicht einmal]{6,8} [die Augen]{9,10} [zum]{12,13} [Himmel]{14} [erheben]{11}, [sondern]{15} [schlug]{16} [an]{17} [seine]{19} [Brust]{18} [und sagte]{20}: ‹[Gott]{21,22}, [sei]{23} [mir]{24} [Sünder]{25,26} [gnädig]{23}!›",
 "LUK.18.14": "[Ich sage]{1} [euch]{2}: [Dieser]{4} [ging]{3} [gerechtfertigt]{5} [nach Hause]{6-9} [hinab]{3}, [und nicht]{10} [jener]{11}. [Denn]{12} [jeder]{13}, [der]{14} [sich selbst]{16} [erhöht]{15}, [wird erniedrigt werden]{17}; [wer]{18} [aber]{19} [sich selbst]{21} [erniedrigt]{20}, [wird erhöht werden]{22}.»",
 "LUK.18.15": "[Man brachte]{1} [aber]{2} [auch]{4} [die kleinen Kinder]{5,6} [zu ihm]{3}, [damit]{7} [er]{9} [sie]{8} [berühre]{9}. [Doch]{11} [als]{10} [die Jünger]{12,13} das [sahen]{10}, [wiesen sie]{14} [die Leute]{15} [zurecht]{14}.",
 "LUK.18.16": "[Jesus]{1,3} [aber]{2} [rief]{4} [sie]{5} [zu sich]{4} [und sagte]{6}: «[Lasst]{7} [die Kinder]{8,9} [zu]{11} [mir]{12} [kommen]{10} und{13} [hindert]{15} [sie]{16} [nicht]{14}; [denn]{18} [solchen]{17,19} [gehört]{20} [das Reich]{21,22} [Gottes]{23,24}.",
 "LUK.18.17": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Wer]{4,5} [das Reich]{8,9} [Gottes]{10,11} [nicht]{6} [annimmt]{7} [wie]{12} [ein Kind]{13}, [der wird]{16} [ganz gewiss nicht]{14,15} [hinein]{17,18}[kommen]{16}.»",
 "LUK.18.18": "Und{1} [ein]{3} [führender Mann]{5} [fragte]{2} [ihn]{4}: «[Guter]{8} [Lehrer]{7}, [was]{9} [muss ich tun]{10}, um [ewiges]{12} [Leben]{11} [zu erben]{13}?» ~6(λέγων «sagend» leitet die Rede ein)",
 "LUK.18.19": "[Jesus]{4,5} [aber]{2} [sagte]{1} [zu ihm]{3}: «[Warum]{6} [nennst du]{8} [mich]{7} [gut]{9}? [Niemand]{10} ist [gut]{11} [ausser]{12,13} [Gott]{15,16} [allein]{14}.",
 "LUK.18.20": "[Die Gebote]{1,2} [kennst du]{3}: ‹[Du sollst nicht]{4} [die Ehe brechen]{5}, [du sollst nicht]{6} [töten]{7}, [du sollst nicht]{8} [stehlen]{9}, [du sollst nicht]{10} [falsch aussagen]{11}, [ehre]{12} [deinen]{15} [Vater]{13,14} und{16} deine [Mutter]{17,18}.›»",
 "LUK.18.21": "[Er]{1} [aber]{2} [sagte]{3}: «[Das]{4} [alles]{5} [habe ich gehalten]{6} [von]{7} [meiner]{9} [Jugend]{8} [an]{7}.»",
 "LUK.18.22": "[Als]{1} [Jesus]{3,4} das [hörte]{1}, [sagte er]{5} [zu ihm]{6}: «[Eines]{8} [fehlt]{10} [dir]{9} [noch]{7}: [Verkaufe]{14} [alles]{11}, [was]{12} [du hast]{13}, und{15} [verteile es]{16} [an Arme]{17}, und{18} [du wirst]{19} [einen Schatz]{20} [im]{21} [Himmel]{22} [haben]{19}; und{23} [komm]{24}, [folge]{25} [mir]{26} [nach]{25}!» ~2",
 "LUK.18.23": "[Als]{3} [er]{1} [das]{4} [aber]{2} [hörte]{3}, [wurde er]{6} [sehr traurig]{5}; [denn]{8} [er war]{7} [sehr]{10} [reich]{9}.",
 "LUK.18.24": "[Jesus]{4,5} [aber]{2} [sah]{1} [ihn]{3} [an]{1} [und sagte]{6}: «[Wie]{7} [schwer]{8} [kommen]{18} [die]{9}, die [Vermögen]{10,11} [haben]{12}, [in]{13} [das Reich]{14,15} [Gottes]{16,17} [hinein]{18}!",
 "LUK.18.25": "[Es ist]{3} [nämlich]{2} [leichter]{1}, dass [ein Kamel]{4} [durch]{5} [ein Nadelöhr]{6,7} [geht]{8}, [als]{9} dass [ein Reicher]{10} [in]{11} [das Reich]{12,13} [Gottes]{14,15} [kommt]{16}.»",
 "LUK.18.26": "[Die Zuhörer]{3,4} [aber]{2} [sagten]{1}: «[Wer]{6} [kann]{7} [dann]{5} [gerettet werden]{8}?»",
 "LUK.18.27": "[Er]{1} [aber]{2} [sagte]{3}: «[Was]{4} [bei]{6} [Menschen]{7} [unmöglich]{5} ist, [ist]{12} [bei]{9} [Gott]{10,11} [möglich]{8}.»",
 "LUK.18.28": "[Da]{2} [sagte]{1} [Petrus]{3,4}: «[Sieh]{5}, [wir]{6} [haben]{7} [alles, was uns gehörte]{8,9}, [verlassen]{7} und [sind]{10} [dir]{11} [gefolgt]{10}.»",
 "LUK.18.29": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4}: «[Amen]{5}, [ich sage]{6} [euch]{7}: [Es gibt]{10} [niemanden]{9}, [der]{11} [Haus]{13} [oder]{14} [Frau]{15} [oder]{16} [Brüder]{17} [oder]{18} [Eltern]{19} [oder]{20} [Kinder]{21} [um]{22} [des Reiches]{23,24} [Gottes]{25,26} [willen]{22} [verlassen hat]{12}, ~8(" + RIGHT + ")",
 "LUK.18.30": "[der]{1} [nicht]{2,3} [ein Vielfaches]{5} [zurückbekommt]{4} [in]{6} [dieser]{9} [Zeit]{7,8} und{10} [in]{11} [der kommenden]{14,15} [Weltzeit]{12,13} [ewiges]{17} [Leben]{16}.»",
 "LUK.18.31": "[Er nahm]{1} [aber]{2} [die Zwölf]{3,4} [zu sich]{1} [und sagte]{5} [zu ihnen]{6,7}: «[Seht]{8}, [wir gehen]{9} [nach]{10} [Jerusalem]{11} [hinauf]{9}, und{12} [alles]{14}, [was]{15} [durch]{17} [die Propheten]{18,19} [geschrieben ist]{16}, [wird]{13} [am Menschensohn]{20-23} [vollendet werden]{13}.",
 "LUK.18.32": "[Er wird]{1} [nämlich]{2} [den Heiden]{3,4} [ausgeliefert]{1} und{5} [verspottet]{6} und{7} [misshandelt]{8} und{9} [angespuckt werden]{10},",
 "LUK.18.33": "und{1} [sie werden]{3} [ihn]{4} [auspeitschen]{2} und [töten]{3}; und{5} [am]{6} [dritten]{8,9} [Tag]{7} [wird er auferstehen]{10}.»",
 "LUK.18.34": "Und{1} [sie]{2} [verstanden]{5} [nichts]{3} [davon]{4}; und{6} [dieses]{10} [Wort]{8,9} [war]{7} [vor]{12} [ihnen]{13} [verborgen]{11}, und{14} [sie begriffen]{16} [nicht]{15}, [was gesagt wurde]{17,18}.",
 "LUK.18.35": "[Es geschah]{1} [aber]{2}, [als]{3,4} [er]{6} [in die Nähe]{5} [von]{7} [Jericho]{8} [kam]{5}: [Ein]{10} [Blinder]{9} [sass]{11} [am]{12,13} [Weg]{14} [und bettelte]{15}.",
 "LUK.18.36": "[Als er]{1} [eine Menge]{3} [vorbeiziehen]{4} [hörte]{1}, [fragte er]{5}, [was]{6} [das]{8} [sei]{7}. ~2",
 "LUK.18.37": "[Man berichtete]{1} [ihm]{3} [aber]{2}, [dass]{4} [Jesus]{5} [von Nazaret]{6,7} [vorbeikomme]{8}.",
 "LUK.18.38": "Und{1} [er rief]{2}: «[Jesus]{4}, [Sohn]{5} [Davids]{6}, [hab Erbarmen]{7} [mit mir]{8}!» ~3(λέγων «sagend» leitet die Rede ein)",
 "LUK.18.39": "Und{1} [die Leute, die]{2} [vorausgingen]{3}, [fuhren]{4} [ihn]{5} [an]{4}, [er solle]{6} [schweigen]{7}. [Er]{8} [aber]{9} [schrie]{12} [noch viel]{10} [lauter]{11}: «[Sohn]{13} [Davids]{14}, [hab Erbarmen]{15} [mit mir]{16}!»",
 "LUK.18.40": "[Jesus]{3,4} [aber]{2} [blieb stehen]{1} [und befahl]{5}, [ihn]{6} [zu]{8} [sich]{9} [zu führen]{7}. [Als]{10} [er]{12} [dann]{11} [näher kam]{10}, [fragte er]{13} [ihn]{14}:",
 "LUK.18.41": "«[Was]{1} [willst du]{3}, [dass ich]{4} [dir]{2} [tun soll]{4}?» [Er]{5} [aber]{6} [sagte]{7}: «[Herr]{8}, [dass]{9} [ich wieder sehen kann]{10}!»",
 "LUK.18.42": "Und{1} [Jesus]{2,3} [sagte]{4} [zu ihm]{5}: «[Sieh wieder]{6}! [Dein]{9} [Glaube]{7,8} [hat]{10} [dich]{11} [gerettet]{10}.»",
 "LUK.18.43": "Und{1} [sofort]{2} [konnte er wieder sehen]{3}, und{4} [er folgte]{5} [ihm]{6} [und pries]{7} [Gott]{8,9}. Und{10} [als]{14} [das ganze]{11,12} [Volk]{13} das [sah]{14}, [lobte es]{15,16} [Gott]{17,18}.",
 # ------------------------------------------------------------ Kapitel 19
 "LUK.19.1": "Und{1} [er kam]{2} [nach Jericho]{4,5} und [zog durch die Stadt]{3}.",
 "LUK.19.2": "Und{1} [siehe]{2}, da war [ein Mann]{3} [mit Namen]{4,5} [Zachäus]{6}; und{7} [er]{8} [war]{9} [Oberzöllner]{10} und{11} [reich]{13}. ~12(αὐτός «er» wiederholt das Subjekt; nicht eigens wiedergegeben)",
 "LUK.19.3": "Und{1} [er versuchte]{2} [zu sehen]{3}, [wer]{6} [Jesus]{4,5} [sei]{7}, und{8} [konnte es]{10} [nicht]{9} [wegen]{11} [der Menge]{12,13}; [denn]{14} [er war]{18} [klein]{17} [von Gestalt]{15,16}.",
 "LUK.19.4": "Und{1} [er lief]{2} [voraus]{3-5} [und stieg]{6} [auf]{7} [einen Maulbeerfeigenbaum]{8}, [um]{9} [ihn]{11} [zu sehen]{10}; [denn]{12} [dort]{13} [sollte er]{14} [vorbeikommen]{15}.",
 "LUK.19.5": "Und{1} [als]{2} [Jesus]{8,9} [an]{4} [die Stelle]{5,6} [kam]{3}, [schaute er auf]{7} [und sagte]{10} [zu ihm]{11,12}: «[Zachäus]{13}, [komm]{15} [schnell]{14} [herunter]{15}! [Denn]{17} [heute]{16} [muss ich]{22,23} [in]{18} [deinem]{21} [Haus]{19,20} [bleiben]{24}.»",
 "LUK.19.6": "Und{1} [er stieg]{3} [schnell]{2} [herunter]{3} und{4} [nahm]{5} [ihn]{6} [mit Freude]{7} [auf]{5}.",
 "LUK.19.7": "Und{1} [alle]{3}, [die es sahen]{2}, [murrten]{4} [und sagten]{5}: «[Bei]{7} [einem sündigen]{8} [Mann]{9} [ist er eingekehrt]{10}, [um dort Gast zu sein]{11}!» ~6(" + RIGHT + ")",
 "LUK.19.8": "[Zachäus]{3} [aber]{2} [trat hin]{1} [und sagte]{4} [zum]{5,6} [Herrn]{7}: «[Sieh]{8}, [Herr]{14}, [die Hälfte]{9,10} [meines]{11} [Besitzes]{12,13} [gebe ich]{17} [den Armen]{15,16}, und{18} [wenn]{19} [ich]{22} [von jemandem]{20} [etwas]{21} [erpresst habe]{22}, [gebe ich]{23} [es vierfach]{24} [zurück]{23}.»",
 "LUK.19.9": "[Jesus]{5,6} [aber]{2} [sagte]{1} [zu ihm]{3,4}: «[Heute]{8} [ist]{13} [diesem]{12} [Haus]{10,11} [Rettung]{9} [widerfahren]{13}, [denn]{14} [auch]{15} [er]{16} [ist]{19} [ein Sohn]{17} [Abrahams]{18}. ~7(" + RIGHT + ")",
 "LUK.19.10": "[Denn]{2} [der Menschensohn]{3-6} [ist gekommen]{1}, um [zu suchen]{7} und{8} [zu retten]{9}, [was]{10} [verloren ist]{11}.»",
 "LUK.19.11": "[Während]{1} [sie]{3} [das]{4} [aber]{2} [hörten]{1}, [erzählte er]{6} [noch]{5} [ein Gleichnis]{7}, [weil]{8,9} [er]{13} [nahe]{10} [bei Jerusalem]{12} [war]{11} und{14} [sie]{16} [meinten]{15}, [dass]{17} [das Reich]{20,21} [Gottes]{22,23} [sofort]{18} [erscheinen]{24} [werde]{19}.",
 "LUK.19.12": "[Er sagte]{1} [also]{2}: «[Ein]{4} [Mann]{3} [von vornehmer Herkunft]{5} [reiste]{6} [in]{7} [ein fernes]{9} [Land]{8}, um [sich]{11} [die Königswürde]{12} [zu holen]{10} und{13} [zurückzukehren]{14}.",
 "LUK.19.13": "[Er rief]{1} [aber]{2} [zehn]{3} [seiner]{5} [Knechte]{4} [zu sich]{1}, [gab]{6} [ihnen]{7} [zehn]{8} [Minen]{9} und{10} [sagte]{11} [zu ihnen]{12,13}: ‹[Macht Geschäfte damit]{14}, [bis]{15,16} [ich komme]{17}!›",
 "LUK.19.14": "[Seine]{4} [Mitbürger]{1,3} [aber]{2} [hassten]{5} [ihn]{6} und{7} [schickten]{8} [eine Gesandtschaft]{9} [hinter]{10} [ihm]{11} [her]{10} [und liessen sagen]{12}: ‹[Wir wollen]{14} [nicht]{13}, dass [dieser]{15} [über]{17} [uns]{18} [König wird]{16}!›",
 "LUK.19.15": "Und{1} [als]{3,4} [er]{6} [zurückkam]{5}, nachdem er [die Königswürde]{8,9} [empfangen hatte]{7}, [da]{10} [liess er]{11} [diese]{16} [Knechte]{14,15}, [denen]{17} er [das Silber]{19,20} [gegeben hatte]{18}, [zu sich]{13} [rufen]{12}, [um]{21} [zu erfahren]{22}, [was]{23} [sie erwirtschaftet hatten]{24}. ~2(" + EGEN + ")",
 "LUK.19.16": "[Da]{2} [kam]{1} [der]{3} [erste]{4} [und sagte]{5}: ‹[Herr]{6}, [deine]{9} [Mine]{7,8} [hat]{11} [zehn]{10} [Minen]{12} [dazugewonnen]{11}.›",
 "LUK.19.17": "Und{1} [er sagte]{2} [zu ihm]{3}: ‹[Gut gemacht]{4}, [du guter]{5} [Knecht]{6}! [Weil]{7} [du]{11} [im]{8} [Kleinsten]{9} [treu]{10} [gewesen bist]{11}, [sollst du]{12} [Macht]{13} [haben]{14} [über]{15} [zehn]{16} [Städte]{17}.›",
 "LUK.19.18": "Und{1} [der]{3} [zweite]{4} [kam]{2} [und sagte]{5}: ‹[Deine]{8} [Mine]{6,7}, [Herr]{9}, [hat]{10} [fünf]{11} [Minen]{12} [eingebracht]{10}.›",
 "LUK.19.19": "[Zu diesem]{4} [aber]{2} [sagte er]{1} [ebenso]{3}: ‹[Auch]{5} [du]{6} [sollst]{8} [über]{7} [fünf]{9} [Städte]{10} [herrschen]{8}.›",
 "LUK.19.20": "Und{1} [der]{2} [andere]{3} [kam]{4} [und sagte]{5}: ‹[Herr]{6}, [sieh]{7}, hier ist [deine]{10} [Mine]{8,9}, [die]{11} [ich]{12} [in]{14} [einem Tuch]{15} [verwahrt]{13} [hatte]{12}.",
 "LUK.19.21": "[Ich fürchtete mich]{1} [nämlich]{2} [vor dir]{3}, [weil]{4} [du]{7} [ein strenger]{6} [Mann]{5} [bist]{7}: [Du nimmst]{8}, [was]{9} du [nicht]{10} [hingelegt hast]{11}, und{12} [erntest]{13}, [was]{14} du [nicht]{15} [gesät hast]{16}.›",
 "LUK.19.22": "[Er sagt]{1} [zu ihm]{2}: ‹[Nach]{3} [deinen eigenen Worten]{4-6} [richte ich]{7} [dich]{8}, [du böser]{9} [Knecht]{10}! [Du wusstest]{11}, [dass]{12} [ich]{13} [ein strenger]{15} [Mann]{14} [bin]{16}: [Ich nehme]{17}, [was]{18} ich [nicht]{19} [hingelegt habe]{20}, und{21} [ernte]{22}, [was]{23} ich [nicht]{24} [gesät habe]{25}?",
 "LUK.19.23": "Und{1} [warum]{2,3} [hast du]{5} [mein]{6} [Silber]{7,8} [nicht]{4} [auf]{9} [die Bank]{10} [gebracht]{5}? [Dann]{11} [hätte]{15} [ich]{11} [es]{16} [bei meiner Rückkehr]{12} [mit]{13} [Zinsen]{14} [eingefordert]{17}.›",
 "LUK.19.24": "Und{1} [zu den Umstehenden]{2,3} [sagte er]{4}: ‹[Nehmt]{5} [ihm]{6,7} [die Mine]{8,9} [weg]{5} und{10} [gebt sie]{11} [dem]{12}, [der]{16} [die zehn]{13,14} [Minen]{15} [hat]{16}!› –",
 "LUK.19.25": "– und{1} [sie sagten]{2} [zu ihm]{3}: ‹[Herr]{4}, [er hat]{5} [zehn]{6} [Minen]{7}!› –",
 "LUK.19.26": "‹[Ich sage]{1} [euch]{2}: [Jedem]{4,5}, [der hat]{6}, [wird gegeben werden]{7}; [von]{8} [dem]{10} [aber]{9}, der [nicht]{11} [hat]{12}, [wird]{16} [auch]{13} [das, was]{14} [er hat]{15}, [weggenommen werden]{16}. ~3(" + RIGHT + ")",
 "LUK.19.27": "[Doch]{1} [diese]{5} [meine]{4} [Feinde]{2,3}, [die]{6} [nicht]{7} [wollten]{8}, [dass ich]{9} [über]{11} [sie]{12} [König werde]{10}, [bringt]{13} [hierher]{14} und{15} [macht]{16} [sie]{17} [vor]{18} [meinen Augen]{19} [nieder]{16}!›»",
 "LUK.19.28": "Und{1} [nachdem er]{2} [das]{3} [gesagt hatte]{2}, [zog er]{4} [voran]{5} [und ging hinauf]{6} [nach]{7} [Jerusalem]{8}.",
 "LUK.19.29": "Und{1} [als]{3} [er in die Nähe]{4} [von]{5} [Betfage]{6} und{7} [Betanien]{8} [kam]{4}, [an]{9,10} [den sogenannten]{12,13} [Ölberg]{11,14}, [sandte er]{15} [zwei]{16} [der]{17} [Jünger]{18} [aus]{15} ~2(" + EGEN + ")",
 "LUK.19.30": "[und sagte]{1}: «[Geht]{2} [in]{3} [das]{4} [Dorf]{6} [gegenüber]{5}! [Wenn ihr]{9} [dort]{7,8} [hineinkommt]{9}, [werdet ihr]{10} [ein Fohlen]{11} [angebunden]{12} [finden]{10}, [auf]{13} [dem]{14} [noch nie]{16} [jemand]{15,17} [gesessen hat]{18}. [Bindet]{20} [es]{21} [los]{20} und{19} [bringt es her]{22}!",
 "LUK.19.31": "Und{1} [wenn]{2} [euch]{4} [jemand]{3} [fragt]{5}: ‹[Warum]{6,7} [bindet ihr es los]{8}?›, [so]{9} [sollt ihr sagen]{10}: ‹[Der Herr]{12,13} [braucht]{15,16} [es]{14}.›» ~11(" + RIGHT + ")",
 "LUK.19.32": "[Die]{3} [Ausgesandten]{4} [gingen hin]{1} [und fanden es]{5}, [wie]{6} er [es ihnen]{8} [gesagt hatte]{7}. ~2",
 "LUK.19.33": "[Als]{1} [sie]{3} [aber]{2} [das Fohlen]{4,5} [losbanden]{1}, [sagten]{6} [seine]{9} [Besitzer]{7,8} [zu ihnen]{10,11}: «[Warum]{12} [bindet ihr]{13} [das Fohlen]{14,15} [los]{13}?»",
 "LUK.19.34": "[Sie]{1} [aber]{2} [sagten]{3}: «[Der Herr]{5,6} [braucht]{8,9} [es]{7}.» ~4(" + RIGHT + ")",
 "LUK.19.35": "Und{1} [sie brachten]{2} [es]{3} [zu]{4,5} [Jesus]{6}, und{7} [sie warfen]{8} [ihre]{9} [Mäntel]{10,11} [auf]{12} [das Fohlen]{13,14} [und setzten]{15} [Jesus]{16,17} [darauf]{15}.",
 "LUK.19.36": "[Während]{1} [er]{3} [aber]{2} [weiterzog]{1}, [breiteten sie]{4} [ihre]{7} [Mäntel]{5,6} [auf]{8} [dem]{9} [Weg]{10} [aus]{4}.",
 "LUK.19.37": "[Als]{1} [er]{3} [aber]{2} [schon]{4} [nahe]{1} [am]{5,6} [Abhang]{7} [des Ölbergs]{8-11} [war]{1}, [fing]{12} [die ganze]{13,14} [Schar]{15} [der Jünger]{16,17} [an]{12}, [voll Freude]{18} [Gott]{20,21} [mit lauter]{23} [Stimme]{22} [zu loben]{19} [für]{24} [alle]{25} [Machttaten]{28}, [die]{26} [sie gesehen hatten]{27},",
 "LUK.19.38": "[und riefen]{1}: «[Gesegnet]{2} sei [der König]{3,5}, [der kommt]{4} [im]{6} [Namen]{7} [des Herrn]{8}! [Im]{9} [Himmel]{10} [Friede]{11} und{12} [Ehre]{13} [in]{14} [den Höhen]{15}!»",
 "LUK.19.39": "Und{1} [einige]{2} [der Pharisäer]{3,4} [aus]{5} [der Menge]{6,7} [sagten]{8} [zu ihm]{9,10}: «[Lehrer]{11}, [weise]{12} [deine]{15} [Jünger]{13,14} [zurecht]{12}!»",
 "LUK.19.40": "Und{1} [er antwortete]{2} [und sagte]{3}: «[Ich sage]{4} [euch]{5}: [Wenn]{7} [diese]{8} [schweigen]{9}, [werden]{12} [die Steine]{10,11} [schreien]{12}.» ~6(" + RIGHT + ")",
 "LUK.19.41": "Und{1} [als]{2} [er näher kam]{3} und [die Stadt]{5,6} [sah]{4}, [weinte er]{7} [über]{8} [sie]{9}",
 "LUK.19.42": "[und sagte]{1}: «[Wenn]{3} doch [auch]{9} [du]{10} [an]{5} [diesem]{8} [Tag]{6,7} [erkannt hättest]{4}, [was]{11} [zum Frieden dient]{12,13}! – [Jetzt]{14} [aber]{15} [ist es]{16} [vor]{17} [deinen]{19} [Augen]{18} [verborgen]{16}. ~2(" + RIGHT + ")",
 "LUK.19.43": "[Denn]{1} [es werden]{2} [Tage]{3} [über]{4} [dich]{5} [kommen]{2}, und{6} [deine]{10} [Feinde]{8,9} [werden]{7} [einen Wall]{11} [um dich]{12} [aufwerfen]{7} und{13} [dich]{15} [einschliessen]{14} und{16} [dich]{18} [von allen Seiten]{19} [bedrängen]{17},",
 "LUK.19.44": "und{1} [sie werden]{2} [dich]{3} und{4} [deine]{7} [Kinder]{5,6} [in]{8} [dir]{9} [dem Erdboden gleichmachen]{2}, und{10} [sie werden]{12} [in]{16} [dir]{17} [keinen]{11} [Stein]{13} [auf]{14} [dem anderen]{15} [lassen]{12}, [weil]{18,19} du [die Zeit]{22,23} [deiner]{26} [Heimsuchung]{24,25} [nicht]{20} [erkannt hast]{21}.»",
 "LUK.19.45": "Und{1} [er ging]{2} [in]{3} [den Tempel]{4,5} [hinein]{2} [und fing an]{6}, [die Händler]{8,9} [hinauszutreiben]{7},",
 "LUK.19.46": "[und sagte]{1} [zu ihnen]{2}: «[Es steht geschrieben]{3}: ‹[Mein]{8} [Haus]{6,7} [wird]{5} [ein Haus]{9} [des Gebets]{10} [sein]{5}.› [Ihr]{11} [aber]{12} [habt]{14} [es]{13} [zu einer Räuberhöhle]{15,16} [gemacht]{14}.» ~4(καί «und» leitet das Zitat ein; nicht eigens wiedergegeben)",
 "LUK.19.47": "Und{1} [er lehrte]{2,3} [täglich]{4-6} [im]{7,8} [Tempel]{9}. [Die Hohepriester]{10,12} [aber]{11} und{13} [die Schriftgelehrten]{14,15} [suchten]{16}, [ihn]{17} [umzubringen]{18}, [ebenso]{19} [die Führenden]{20,21} [des Volkes]{22,23},",
 "LUK.19.48": "und{1} [sie fanden]{3} [nicht]{2}, [was]{4,5} [sie tun sollten]{6}; [denn]{9} [das ganze]{10} [Volk]{7,8} [hing]{11} [an seinen Lippen]{12,13:idiom}.",
 # ------------------------------------------------------------ Kapitel 20
 "LUK.20.1": "[Und es geschah]{1,2} [an]{3} [einem]{4} [der Tage]{5,6}, [als]{7} [er]{8} [das Volk]{9,10} [im]{11,12} [Tempel]{13} [lehrte]{7} und{14} [das Evangelium verkündigte]{15}: [Die Hohepriester]{17,18} und{19} [die Schriftgelehrten]{20,21} [traten]{16} [mit]{22} [den Ältesten]{23,24} [heran]{16}",
 "LUK.20.2": "und{1} [sagten]{2} [zu ihm]{4,5}: «[Sag]{6} [uns]{7}: [Mit]{8} [welcher]{9} [Vollmacht]{10} [tust du]{12} [das]{11}? [Oder]{13} [wer]{14} [ist es]{15}, [der]{16} [dir]{18} [diese]{21} [Vollmacht]{19,20} [gegeben hat]{17}?» ~3(λέγοντες «sagend»; nicht eigens wiedergegeben)",
 "LUK.20.3": "Er [antwortete]{1} [aber]{2} [und sagte]{3} [zu ihnen]{4,5}: «[Auch ich]{8} [will]{6} [euch]{7} [etwas]{9} [fragen]{6}; und{10} [sagt]{11} [mir]{12}:",
 "LUK.20.4": "[Die]{1} [Taufe]{2} [des Johannes]{3}, [war sie]{6} [vom]{4} [Himmel]{5} [oder]{7} [von]{8} [Menschen]{9}?»",
 "LUK.20.5": "[Sie]{1} [aber]{2} [überlegten]{3} [miteinander]{4,5} [und sagten]{6}: «[Wenn]{8} [wir sagen]{9}: ‹[Vom]{10} [Himmel]{11}›, [wird er sagen]{12}: ‹[Warum]{13,14} [habt ihr]{16} [ihm]{17} [nicht]{15} [geglaubt]{16}?›  ~7(" + RIGHT + ")",
 "LUK.20.6": "[Wenn]{1} [wir]{3} [aber]{2} [sagen]{3}: ‹[Von]{4} [Menschen]{5}›, [wird]{9} [das ganze]{8} [Volk]{6,7} [uns]{10} [steinigen]{9}; [denn]{12} [es ist]{13} [überzeugt]{11}, dass [Johannes]{14} [ein Prophet]{15} [war]{16}.»",
 "LUK.20.7": "Und{1} [sie antworteten]{2}, [sie wüssten]{4} [nicht]{3}, [woher]{5} sie stamme.",
 "LUK.20.8": "Und{1} [Jesus]{2,3} [sagte]{4} [zu ihnen]{5}: «Dann [sage]{8} [auch]{6} [ich]{7} [euch]{9} [nicht]{6}, [mit]{10} [welcher]{11} [Vollmacht]{12} ich [das]{13} [tue]{14}.»",
 "LUK.20.9": "[Er fing]{1} [aber]{2} [an]{1}, [dem Volk]{3-5} [dieses]{9} [Gleichnis]{7,8} [zu erzählen]{6}: «[Ein Mensch]{10} [pflanzte]{11} [einen Weinberg]{12} und{13} [verpachtete]{14} [ihn]{15} [an Weinbauern]{16} und{17} [reiste]{18} [für lange Zeit]{19,20} [ausser Landes]{18}.",
 "LUK.20.10": "Und{1} [zur rechten Zeit]{2} [sandte er]{3} [einen Knecht]{7} [zu]{4} [den Weinbauern]{5,6}, [damit]{8} [sie]{14} [ihm]{15} [seinen Anteil]{9,10} [am Ertrag]{11} [des Weinbergs]{12,13} [geben]{14}. [Die Weinbauern]{16,18} [aber]{17} [schlugen]{21} [ihn]{20} [und schickten ihn]{19} [mit leeren Händen]{22} [fort]{19}.",
 "LUK.20.11": "Und{1} [er sandte]{4} [noch]{2} [einen anderen]{3} [Knecht]{5}. [Sie]{6} [aber]{7} [schlugen]{9} [auch diesen]{8} und{10} [beschimpften ihn]{11} und [schickten ihn]{12} [mit leeren Händen]{13} [fort]{12}.",
 "LUK.20.12": "Und{1} [er sandte]{4} [noch]{2} [einen dritten]{3}. [Sie]{5} [aber]{6} [verwundeten]{9} [auch]{7} [diesen]{8} [und warfen ihn hinaus]{10}.",
 "LUK.20.13": "[Da]{2} [sagte]{1} [der Herr]{3,4} [des Weinbergs]{5,6}: ‹[Was]{7} [soll ich tun]{8}? [Ich will]{9} [meinen]{12} [geliebten]{13,14} [Sohn]{10,11} [senden]{9}; [vielleicht]{15} [werden sie]{17} [vor ihm]{16} [Achtung haben]{17}.›",
 "LUK.20.14": "[Als]{1} [die Weinbauern]{4,5} [ihn]{3} [aber]{2} [sahen]{1}, [überlegten sie]{6} [miteinander]{7,8} [und sagten]{9}: ‹[Das]{10} [ist]{11} [der Erbe]{12,13}; [lasst]{14} [ihn]{15} [uns töten]{14}, [damit]{16} [das Erbe]{19,20} [uns]{17} [gehört]{18}!›",
 "LUK.20.15": "Und{1} [sie warfen]{2} [ihn]{3} [aus]{4} [dem Weinberg]{5,6} [hinaus]{2} [und töteten ihn]{7}. [Was]{8} [wird]{10} [nun]{9} [der Herr]{12,13} [des Weinbergs]{14,15} [mit ihnen]{11} [tun]{10}?",
 "LUK.20.16": "[Er wird kommen]{1} und{2} [diese]{6} [Weinbauern]{4,5} [umbringen]{3} und{7} [den Weinberg]{9,10} [anderen]{11} [geben]{8}.» [Die Zuhörer]{12} [aber]{13} [sagten]{14}: «[Das darf nicht]{15} [geschehen]{16}!»",
 "LUK.20.17": "[Er]{1} [aber]{2} [sah]{3} [sie]{4} [an]{3} [und sagte]{5}: «[Was]{6} [bedeutet]{8} [denn]{7} [dieses]{11} [Schriftwort]{9,10}: ‹[Der Stein]{12}, [den]{13} [die Bauleute]{15,16} [verworfen haben]{14}, [der]{17} [ist]{18} [zum]{19} [Eckstein]{20,21} [geworden]{18}›?",
 "LUK.20.18": "[Jeder]{1}, [der]{2} [auf]{4} [jenen]{5} [Stein]{6,7} [fällt]{3}, [wird zerschmettert werden]{8}; [auf wen]{9,10} er [aber]{11} [fällt]{12,13}, [den]{15} [wird er zermalmen]{14}.»",
 "LUK.20.19": "Und{1} [die Schriftgelehrten]{3,4} und{5} [die Hohepriester]{6,7} [suchten]{2}, [noch in]{13} [derselben]{14} [Stunde]{15,16} [die Hände]{11,12} [an]{9} [ihn]{10} [zu legen]{8}, [doch]{17} [sie fürchteten]{18} [das Volk]{19,20}; [denn]{22} [sie hatten erkannt]{21}, [dass]{23} er [dieses]{29} [Gleichnis]{27,28} [im Blick auf]{24} [sie]{25} [erzählt hatte]{26}.",
 "LUK.20.20": "Und{1} [sie lauerten ihm auf]{2} [und schickten]{3} [Spitzel]{4}, die [sich]{6} [als Gerechte]{7} [ausgaben]{5,8}, [um]{9} [ihn]{11} [bei einem Wort]{12} [zu fassen]{10}, [damit sie]{13} [ihn]{15} [der Macht]{16,17} und{18} [der Gewalt]{19,20} [des Statthalters]{21,22} [ausliefern könnten]{14}.",
 "LUK.20.21": "Und{1} [sie fragten]{2} [ihn]{3}: «[Lehrer]{5}, [wir wissen]{6}, [dass]{7} du [richtig]{8} [redest]{9} und{10} [lehrst]{11} und{12} [nicht]{13} [auf das Ansehen der Person siehst]{14,15:idiom}, [sondern]{16} [den Weg]{19,20} [Gottes]{21,22} [in]{17} [Wahrheit]{18} [lehrst]{23}. ~4(λέγοντες «sagend»; nicht eigens wiedergegeben)",
 "LUK.20.22": "[Ist es]{1} [uns]{2} [erlaubt]{1}, [dem Kaiser]{3} [Steuer]{4} [zu zahlen]{5}, [oder]{6} [nicht]{7}?»",
 "LUK.20.23": "Er [durchschaute]{1} [aber]{2} [ihre]{3} [Verschlagenheit]{4,5} [und sagte]{6} [zu ihnen]{7,8}:",
 "LUK.20.24": "«[Zeigt]{1} [mir]{2} [einen Denar]{3}! [Wessen]{4} [Bild]{6} und{7} [Aufschrift]{8} [trägt er]{5}?» [Sie antworteten]{9} [aber]{10} [und sagten]{11}: «[Des Kaisers]{12}.»",
 "LUK.20.25": "[Er]{1} [aber]{2} [sagte]{3} [zu ihnen]{4,5}: «[Dann]{6} [gebt]{7} [dem Kaiser]{10} [zurück]{7}, [was des Kaisers ist]{8,9}, und{11} [Gott]{15,16}, [was Gottes ist]{12-14}!»",
 "LUK.20.26": "Und{1} [sie konnten]{3} ihn [vor]{7} [dem Volk]{8,9} [nicht]{2} [bei seiner Rede]{5,6} [fassen]{4}, und{10} [sie staunten]{11} [über]{12} [seine]{15} [Antwort]{13,14} [und schwiegen]{16}.",
 "LUK.20.27": "[Es kamen]{1} [aber]{2} [einige]{3} [der Sadduzäer]{4,5} [herbei]{1}, [die]{6} [bestreiten]{7}, dass [es eine Auferstehung]{8} [gibt]{10}, [und fragten]{11} [ihn]{12} ~9(μή nach ἀντιλέγω verstärkt die Verneinung; nicht eigens wiedergegeben)",
 "LUK.20.28": "[und sagten]{1}: «[Lehrer]{2}, [Mose]{3} [hat]{4} [uns]{5} [geschrieben]{4}: [Wenn]{6} [jemandes]{7} [Bruder]{8} [stirbt]{9}, der [eine Frau]{11} [hat]{10}, und{12} [dieser]{13} [kinderlos]{14} [ist]{15}, [dann soll]{16} [sein]{20} [Bruder]{18,19} [die]{21} [Frau]{22} [nehmen]{17} und{23} [seinem]{28} [Bruder]{26,27} [Nachkommen]{25} [erwecken]{24}.",
 "LUK.20.29": "[Es waren]{4} [nun]{2} [sieben]{1} [Brüder]{3}. Und{5} [der]{6} [erste]{7} [nahm]{8} [eine Frau]{9} [und starb]{10} [kinderlos]{11}.",
 "LUK.20.30": "Und{1} [der]{2} [zweite]{3},",
 "LUK.20.31": "und{1} [der]{2} [dritte]{3} [nahm]{4} [sie]{5}, [ebenso]{6} [auch]{8} [alle]{9} [sieben]{10}: [Sie hinterliessen]{12} [keine]{11} [Kinder]{13} und{14} [starben]{15}. ~7",
 "LUK.20.32": "[Zuletzt]{1} [starb]{5} [auch]{2} [die]{3} [Frau]{4}.",
 "LUK.20.33": "[Die]{1} [Frau]{2} [nun]{3} – [in]{4} [der]{5} [Auferstehung]{6}: [Wem]{7} [von ihnen]{8} [wird sie]{9} [als Frau]{10} [gehören]{9}? [Denn]{12} [die]{11} [sieben]{13} [haben]{14} [sie]{15} [zur Frau]{16} [gehabt]{14}.»",
 "LUK.20.34": "Und{1} [Jesus]{4,5} [sagte]{2} [zu ihnen]{3}: «[Die Menschen]{6,7} [dieser]{10} [Weltzeit]{8,9} [heiraten]{11} und{12} [werden verheiratet]{13};",
 "LUK.20.35": "[die]{1} [aber]{2}, [die für würdig befunden werden]{3}, [jene]{6} [Weltzeit]{4,5} [zu erlangen]{7} und{8} [die Auferstehung]{9-11} [von]{12} [den Toten]{13}, [heiraten]{15} [weder]{14}, [noch]{16} [werden sie verheiratet]{17};",
 "LUK.20.36": "[denn]{2} [sie können]{5} [auch nicht]{1} [mehr]{4} [sterben]{3}; [sie sind]{8} [nämlich]{7} [den Engeln gleich]{6} und{9} [sind]{11} [Söhne]{10} [Gottes]{12}, [weil sie]{16} [Söhne]{15} [der Auferstehung]{13,14} [sind]{16}.",
 "LUK.20.37": "[Dass]{1} [aber]{2} [die Toten]{4,5} [auferweckt werden]{3}, [hat]{8} [auch]{6} [Mose]{7} [beim]{9,10} [Dornbusch]{11} [angezeigt]{8}, [wo]{12} er [den Herrn]{14} ‹[den Gott]{15,16} [Abrahams]{17} und{18} [Gott]{19} [Isaaks]{20} und{21} [Gott]{22} [Jakobs]{23}› [nennt]{13}.",
 "LUK.20.38": "[Er ist]{4} [aber]{2} [nicht]{3} [ein Gott]{1} [von Toten]{5}, [sondern]{6} [von Lebenden]{7}; [denn]{9} [für ihn]{10} [leben]{11} [alle]{8}.»",
 "LUK.20.39": "[Einige]{3} [der Schriftgelehrten]{4,5} [aber]{2} [antworteten]{1} [und sagten]{6}: «[Lehrer]{7}, [du hast]{9} [gut]{8} [gesprochen]{9}.»",
 "LUK.20.40": "[Denn]{2} [sie wagten]{3} [nicht mehr]{1}, [ihn]{5} [etwas]{6} [zu fragen]{4}.",
 "LUK.20.41": "[Er sagte]{1} [aber]{2} [zu ihnen]{3,4}: «[Wie]{5} [sagen sie]{6}, [der Christus]{7,8} [sei]{9} [Davids]{10} [Sohn]{11}?",
 "LUK.20.42": "[Denn]{2} [David]{3} [selbst]{1} [sagt]{4} [im]{5} [Buch]{6} [der Psalmen]{7}: ‹[Der Herr]{9} [sprach]{8} [zu]{10} [meinem]{12} [Herrn]{11}: [Setze dich]{13} [zu]{14} [meiner]{16} [Rechten]{15},",
 "LUK.20.43": "[bis]{1,2} [ich]{3} [deine]{6} [Feinde]{4,5} [zum Schemel]{7} [deiner]{10} [Füsse]{8,9} [mache]{3}.›",
 "LUK.20.44": "[David]{1} [nennt]{5} [ihn]{3} [also]{2} ‹[Herr]{4}›; und{6} [wie]{7} [ist er]{10} dann [sein]{8} [Sohn]{9}?»",
 "LUK.20.45": "[Während]{1} [aber]{2} [das ganze]{3,4} [Volk]{5} [zuhörte]{1}, [sagte er]{6} [zu den]{7} [Jüngern]{8}:",
 "LUK.20.46": "«[Hütet euch]{1} [vor]{2} [den Schriftgelehrten]{3,4}, [die]{5} [gern]{6} [in langen Gewändern]{8,9} [umhergehen]{7} und{10} [die Begrüssungen]{12} [auf]{13} [den Marktplätzen]{14,15} [lieben]{11} und{16} [die Ehrensitze]{17} [in]{18} [den Synagogen]{19,20} und{21} [die Ehrenplätze]{22} [bei]{23} [den Gastmählern]{24,25},",
 "LUK.20.47": "[die]{1} [die Häuser]{3,4} [der Witwen]{5,6} [auffressen]{2} und{7} [zum Schein]{8} [lange]{9} [beten]{10}. [Die]{11} [werden]{12} [ein umso härteres]{13} [Urteil]{14} [empfangen]{12}.»",
 # ------------------------------------------------------------ Kapitel 21
 "LUK.21.1": "[Er blickte]{1} [aber]{2} [auf]{1} [und sah]{3} [die Reichen]{4,12} [ihre]{11} [Gaben]{9,10} [in]{6} [den Opferkasten]{7,8} [einwerfen]{5}.",
 "LUK.21.2": "[Da]{2} [sah er]{1} [eine]{3} [arme]{5} [Witwe]{4} [dort]{7} [zwei]{9} [Lepta]{8} [einwerfen]{6}",
 "LUK.21.3": "und{1} [sagte]{2}: «[Wahrhaftig]{3}, [ich sage]{4} [euch]{5}: [Diese]{11} [arme]{10} [Witwe]{7-9} [hat]{14} [mehr]{12} [eingeworfen]{14} [als alle]{13}. ~6(" + RIGHT + ")",
 "LUK.21.4": "[Denn]{2} [diese]{3} [alle]{1} [haben]{8} [aus]{4} [ihrem]{7} [Überfluss]{5,6} [zu]{9} [den Gaben]{10,11} [eingeworfen]{8}; [sie]{12} [aber]{13} [hat]{23} [aus]{14} [ihrem]{17} [Mangel]{15,16} [den ganzen]{18} [Lebensunterhalt]{19,20}, [den]{21} [sie hatte]{22}, [eingeworfen]{23}.»",
 "LUK.21.5": "Und{1} [als]{3} [einige]{2} [vom]{4,5} [Tempel]{6} [sagten]{3}, [dass]{7} er [mit schönen]{9} [Steinen]{8} und{10} [Weihegaben]{11} [geschmückt sei]{12}, [sagte er]{13}:",
 "LUK.21.6": "«[Das]{1}, [was]{2} [ihr da seht]{3} – [es werden]{4} [Tage]{5} [kommen]{4}, [in]{6} [denen]{7} [kein]{8} [Stein]{10} [auf]{11} [dem anderen]{12} [gelassen wird]{9}, [der]{13} [nicht]{14} [abgebrochen wird]{15}.»",
 "LUK.21.7": "[Sie fragten]{1} [ihn]{3} [aber]{2}: «[Lehrer]{5}, [wann]{6} [wird]{9} [das]{8} [denn]{7} [geschehen]{9}, und{10} [was]{11} ist [das Zeichen]{12,13}, [wenn]{14} [das]{16} [geschehen]{17} [soll]{15}?» ~4(λέγοντες «sagend»; nicht eigens wiedergegeben)",
 "LUK.21.8": "[Er]{1} [aber]{2} [sagte]{3}: «[Seht zu]{4}, [dass ihr]{6} [nicht]{5} [irregeführt werdet]{6}! [Denn]{8} [viele]{7} [werden]{9} [unter]{10} [meinem]{13} [Namen]{11,12} [kommen]{9} [und sagen]{14}: ‹[Ich]{15} [bin es]{16}!›, und{17}: ‹[Die Zeit]{18,19} [ist nahe gekommen]{20}!› [Lauft]{22} [ihnen]{24} [nicht]{21} [nach]{23}!",
 "LUK.21.9": "[Wenn]{1} [ihr]{3} [aber]{2} [von Kriegen]{4} und{5} [Unruhen]{6} [hört]{3}, [lasst euch]{8} [nicht]{7} [erschrecken]{8}! [Denn]{10} [das]{11} [muss]{9} [zuerst]{13} [geschehen]{12}, [aber]{14} [das Ende]{17,18} kommt [nicht]{15} [sofort]{16}.»",
 "LUK.21.10": "[Dann]{1} [sagte er]{2} [zu ihnen]{3}: «[Es wird sich]{4} [Volk]{5} [gegen]{6} [Volk]{7} [erheben]{4} und{8} [Reich]{9} [gegen]{10} [Reich]{11};",
 "LUK.21.11": "[es wird]{10} [grosse]{3} [Erdbeben]{1} [geben]{10} und{4} [an vielen Orten]{5,6} [Hungersnöte]{7} und{8} [Seuchen]{9}; [Schreckliches]{11} und{12,13} [grosse]{17} [Zeichen]{14} [vom]{15} [Himmel]{16} [wird es geben]{18}. ~2(τε «und»; nicht eigens wiedergegeben)",
 "LUK.21.12": "[Vor]{1} [all]{4} [dem]{3} [aber]{2} [werden sie]{5} [ihre]{10} [Hände]{8,9} [an]{6} [euch]{7} [legen]{5} und{11} [euch verfolgen]{12}; [sie werden euch]{13} [an]{14} [die Synagogen]{15,16} und{17} [in die Gefängnisse]{18} [ausliefern]{13}, und [ihr werdet]{19} [vor]{20} [Könige]{21} und{22} [Statthalter]{23} [geführt werden]{19} [wegen]{24} [meines]{27} [Namens]{25,26}.",
 "LUK.21.13": "[Das wird]{1} [für euch]{2} [zum]{3} [Zeugnis]{4} [führen]{1}.",
 "LUK.21.14": "[Nehmt euch]{1} [also]{2} [zu Herzen]{3-6}, euch [nicht]{7} [im Voraus Gedanken zu machen]{8}, [wie ihr euch verteidigen sollt]{9};",
 "LUK.21.15": "[denn]{2} [ich]{1} [werde]{3} [euch]{4} [die rechten Worte]{5} und{6} [Weisheit]{7} [geben]{3}, [denen]{8} [alle]{14} [eure]{17} [Gegner]{15,16} [weder]{9} [widerstehen]{11} [noch]{12} [widersprechen]{13} [können]{10}.",
 "LUK.21.16": "[Ihr werdet]{1} [aber]{2} [sogar]{3} [von]{4} [Eltern]{5} und{6} [Brüdern]{7} und{8} [Verwandten]{9} und{10} [Freunden]{11} [ausgeliefert werden]{1}, und{12} [man wird]{13} [einige]{14} [von euch]{15} [töten]{13},",
 "LUK.21.17": "und{1} [ihr werdet]{2} [von]{4} [allen]{5} [gehasst]{3} [sein]{2} [wegen]{6,7} [meines]{9} [Namens]{8}.",
 "LUK.21.18": "Und{1} [kein]{7,8} [Haar]{2} [von]{3} [eurem]{6} [Kopf]{4,5} [wird verloren gehen]{9}.",
 "LUK.21.19": "[Durch]{1} [eure]{4} [Standhaftigkeit]{2,3} [gewinnt]{5} [euer]{8} [Leben]{6,7}!",
 "LUK.21.20": "[Wenn]{1} [ihr]{3} [aber]{2} [Jerusalem]{7} [von Heeren]{5,6} [umzingelt]{4} [seht]{3}, [dann]{8} [erkennt]{9}, [dass]{10} [seine]{14} [Verwüstung]{12,13} [nahe gekommen ist]{11}.",
 "LUK.21.21": "[Dann]{1} [sollen]{6} [die]{2} [in]{3} [Judäa]{4,5} [in]{7} [die Berge]{8,9} [fliehen]{6}, und{10} [die]{11} [in]{12} [der Stadt]{13,14} [sollen weggehen]{15}, und{16} [die]{17} [auf]{18} [dem Land]{19,20} [sollen]{22} [nicht]{21} [hinein]{23,24}[gehen]{22};",
 "LUK.21.22": "[denn]{1} [das]{4} [sind]{5} [Tage]{2} [der Vergeltung]{3}, [damit]{6} [alles]{8} [erfüllt wird]{7}, [was]{9} [geschrieben ist]{10}.",
 "LUK.21.23": "[Weh]{1} [den]{2} [Schwangeren]{3-5} und{6} [den]{7} [Stillenden]{8} [in]{9} [jenen]{10} [Tagen]{11,12}! [Denn]{14} [es wird]{13} [grosse]{16} [Not]{15} [im]{17,18} [Land]{19} [sein]{13} und{20} [Zorn]{21} [über]{22} [dieses]{24} [Volk]{23},",
 "LUK.21.24": "und{1} [sie werden]{2} [durch die Schärfe]{3} [des Schwertes]{4} [fallen]{2} und{5} [als Gefangene]{6} [zu]{7} [allen]{10} [Völkern]{8,9} [weggeführt werden]{6}, und{11} [Jerusalem]{12} [wird]{13} [von]{15} [den Völkern]{16} [zertreten werden]{14}, [bis]{17,18} [die Zeiten]{20} [der Völker]{21} [erfüllt sind]{19}.",
 "LUK.21.25": "Und{1} [es werden]{2} [Zeichen]{3} [an]{4} [Sonne]{5} und{6} [Mond]{7} und{8} [Sternen]{9} [sein]{2}, und{10} [auf]{11} [der Erde]{12,13} [Angst]{14} [unter den Völkern]{15}, [die ratlos sind]{16,17} [über das Tosen]{18} [des Meeres]{19} und{20} [der Wogen]{21},",
 "LUK.21.26": "[Menschen]{2} [vergehen]{1} [vor]{3} [Furcht]{4} und{5} [in Erwartung]{6} [dessen, was]{7} [über]{9} [die Welt]{10} [kommt]{8}; [denn]{12} [die Mächte]{11,13} [des Himmels]{14,15} [werden erschüttert werden]{16}.",
 "LUK.21.27": "Und{1} [dann]{2} [werden sie]{3} [den Menschensohn]{4-7} [in]{9} [einer Wolke]{10} [kommen]{8} [sehen]{3} [mit]{11} [Macht]{12} und{13} [grosser]{15} [Herrlichkeit]{14}.",
 "LUK.21.28": "[Wenn]{1} [dies]{3} [aber]{2} [zu geschehen]{4} [beginnt]{1}, [richtet euch auf]{5} und{6} [erhebt]{7} [eure]{10} [Köpfe]{8,9}, [denn]{11} [eure]{15} [Erlösung]{13,14} [naht]{12}.»",
 "LUK.21.29": "Und{1} [er erzählte]{2} [ihnen]{4} [ein Gleichnis]{3}: «[Seht euch]{5} [den Feigenbaum]{6,7} und{8} [alle]{9} [Bäume]{10,11} [an]{5}:",
 "LUK.21.30": "[Wenn]{1} sie [schon]{3} [ausschlagen]{2}, [seht ihr es]{4} [und erkennt]{7} [von selbst]{5,6}, [dass]{8} [der Sommer]{11,12} [schon]{9} [nahe]{10} [ist]{13}.",
 "LUK.21.31": "[So]{1} [auch]{2} [ihr]{3}: [Wenn]{4} ihr [das]{6} [geschehen]{7} [seht]{5}, [erkennt]{8}, [dass]{9} [das Reich]{12,13} [Gottes]{14,15} [nahe]{10} [ist]{11}.",
 "LUK.21.32": "[Amen]{1}, [ich sage]{2} [euch]{3}: [Dieses]{10} [Geschlecht]{8,9} [wird]{7} [nicht]{5,6} [vergehen]{7}, [bis]{11,12} [alles]{13} [geschieht]{14}. ~4(" + RIGHT + ")",
 "LUK.21.33": "[Der Himmel]{1,2} und{3} [die Erde]{4,5} [werden vergehen]{6}, [meine]{10} [Worte]{7,9} [aber]{8} [werden]{13} [nicht]{11,12} [vergehen]{13}.",
 "LUK.21.34": "[Gebt]{1} [aber]{2} [acht]{1} [auf euch]{3}, [dass]{4} [eure]{6} [Herzen]{7,8} [nicht]{4} [beschwert werden]{5} [durch]{9} [Rausch]{10} und{11} [Trunkenheit]{12} und{13} [Sorgen]{14} [des Alltags]{15} und{16} [jener]{23} [Tag]{21,22} nicht [plötzlich]{20} [über]{18} [euch]{19} [hereinbricht]{17}",
 "LUK.21.35": "[wie]{1} [eine Falle]{2}. [Denn]{4} [er wird]{3} [über]{5} [alle]{6} [hereinbrechen]{3}, [die]{7} [auf]{9} [der ganzen]{11} [Erde]{10,12,13} [wohnen]{8}.",
 "LUK.21.36": "[Seid]{1} [aber]{2} [allezeit]{3-5} [wach]{1} [und betet]{6}, [damit]{7} [ihr stark genug seid]{8}, [all]{11} [dem]{10} [zu entkommen]{9}, [was]{12} [geschehen]{14} [soll]{13}, und{15} [vor]{17} [dem Menschensohn]{18-21} [zu bestehen]{16}.»",
 "LUK.21.37": "[Er lehrte]{1,8} [aber]{2} [tagsüber]{3,4} [im]{5,6} [Tempel]{7}; [nachts]{9,11} [aber]{10} [ging er hinaus]{12} [und übernachtete]{13} [auf]{14} [dem]{15} [sogenannten]{17,18} [Ölberg]{16,19}.",
 "LUK.21.38": "Und{1} [das ganze]{2,3} [Volk]{4} [kam]{5} [früh am Morgen]{5} [zu]{6} [ihm]{7} [in]{8} [den Tempel]{9,10}, um [ihn]{12} [zu hören]{11}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 18
 "LUK.18.1": "[Er hät]{1} [ine]{4} [aber]{2} [es Gliichnis]{3} [verzellt]{1}, [für z zeige, dass]{5,6} [si]{10} [immer]{8} [söled]{7} [bätte]{9} und{11} [nöd]{12} [de Muet verlüüre]{13}.",
 "LUK.18.2": "[Er hät gseit]{1}: «[I]{5} [ere]{6} [Stadt]{7} [isch]{4} [en]{3} [Richter]{2} [gsii]{4}, [wo]{11} [Gott]{8,9} [nöd]{10} [gfürchtet hät]{11} und{12} [uf kein]{14} [Mänsch]{13} [Rücksicht gnoo hät]{15}.",
 "LUK.18.3": "[I]{4} [dere]{7} [Stadt]{5,6} [isch]{3} [aber]{2} [e Witwe]{1} [gsii]{3}, und{8} [si isch immer wider]{9} [zu]{10} [ihm]{11} [choo]{9} [und hät gseit]{12}: ‹[Verschaff]{13} [mir]{14} [Rächt]{13} [gäge]{15} [mine]{18} [Gägner]{16,17}!›",
 "LUK.18.4": "Und{1} [e Ziit lang]{4,5} [hät er]{3} [nöd]{2} [wele]{3}. [Dänach]{6,7} [aber]{8} [hät er]{9} [sich]{10,11} [gseit]{9}: ‹[Au wänn]{12,13} [ich]{17} [Gott]{14,15} [nöd]{16} [fürchte]{17} [und uf kein]{18} [Mänsch]{19} [Rücksicht nimm]{20},",
 "LUK.18.5": "[wil]{1,3} [mir]{5} [die]{9} [Witwe]{7,8} [halt]{2} [Müe]{6} [macht]{4}, [verschaff ich]{10} [ere]{11} [Rächt]{10}, [demit]{12} [si]{16} [nöd]{13} [ohni Änd]{14,15} [chunnt]{16} und [mich]{18} [fertig macht]{17}.›»",
 "LUK.18.6": "[De Herr]{3,4} [aber]{2} [hät gseit]{1}: «[Losed]{5}, [was]{6} [de]{7} [ungrächt]{9,10} [Richter]{8} [seit]{11}!",
 "LUK.18.7": "[Sött]{6} [aber]{2} [Gott]{1,3} [sine]{11} [Userwählte]{9,10} [nöd]{4,5} [Rächt]{7,8} [verschaffe]{6}, [wo]{12} [Tag]{15} und{16} [Nacht]{17} [zu ihm]{14} [schreied]{13}? Und{18} [laat er]{19} [si]{20,21} [warte]{19}?",
 "LUK.18.8": "[Ich säg]{1} [eu]{2}: [Er wird]{4} [ine]{7} [Rächt]{5,6} [verschaffe]{4}, und zwar [schnell]{8,9}. [Aber]{10} [wird]{17} [de Mänschesohn]{11-14}, [wänn er chunnt]{15}, [ächt]{16} [de Glaube]{18,19} [uf]{20} [de Ärde]{21,22} [finde]{17}?» ~3(" + RIGHT_G + ")",
 "LUK.18.9": "[Er hät]{1} [aber]{2} [au]{3} [es paar]{4,5}, [wo]{6} [vo sich]{8,9} [überzüügt gsii sind]{7}, [dass]{10} [si]{11} [grächt]{12} [sind]{11}, und{13} [di andere]{15,16} [verachtet händ]{14}, [das]{19} [Gliichnis]{17,18} [verzellt]{1}:",
 "LUK.18.10": "«[Zwei]{2} [Mänsche]{1} [sind]{3} [in]{4} [Tämpel]{5,6} [ufe gange]{3} [go bätte]{7}, [de]{8} [eint]{9} [en Pharisäer]{10} und{11} [de]{12} [ander]{13} [en Zöllner]{14}.",
 "LUK.18.11": "[De Pharisäer]{1,2} [hät sich häregstellt]{3} [und hät]{7} [bi sich]{4,5} [eso]{6} [bättet]{7}: ‹[Gott]{8,9}, [ich dank]{10} [dir]{11}, [dass]{12} [ich]{14} [nöd]{13} [bi]{14} [wie]{15} [di andere]{16,17} [Mänsche]{18,19}: [Röiber]{20}, [Ungrächti]{21}, [Ehebrächer]{22}, [oder]{23} [au]{24} [wie]{25} [dä]{26} [Zöllner]{27,28} da.",
 "LUK.18.12": "[Ich faschte]{1} [zweimal]{2} [i de Wuche]{3,4}, [ich gib de Zäänte]{5} [vo allem]{6}, [was]{7} [ich iinimm]{8}.›",
 "LUK.18.13": "[De Zöllner]{1,3} [aber]{2} [isch]{5} [wiit wäg]{4} [gstande]{5} [und hät]{7} [nöd emal]{6,8} [d Auge]{9,10} [zum]{12,13} [Himmel]{14} [wele]{7} [ufhebe]{11}, [sondern]{15} [hät]{16} [a]{17} [sini]{19} [Bruscht]{18} [gschlage]{16} [und gseit]{20}: ‹[Gott]{21,22}, [bis]{23} [mir]{24} [Sünder]{25,26} [gnädig]{23}!›",
 "LUK.18.14": "[Ich säg]{1} [eu]{2}: [Dä]{4} [isch]{3} [grächtfertiget]{5} [hei]{6-9} [gange]{3}, [und nöd]{10} [säbe]{11}. [Dänn]{12} [jede]{13}, [wo]{14} [sich sälber]{16} [erhöcht]{15}, [wird erniedriget]{17}; [wer]{18} [aber]{19} [sich sälber]{21} [erniedriget]{20}, [wird erhöcht]{22}.»",
 "LUK.18.15": "[Mer hät]{1} [aber]{2} [au]{4} [di chliine Chind]{5,6} [zu ihm]{3} [bracht]{1}, [demit]{7} [er]{9} [si]{8} [aalangi]{9}. [Aber]{11} [wo]{10} [d Jünger]{12,13} das [gseh händ]{10}, [händ si]{14} [d Lüüt]{15} [aagfahre]{14}.",
 "LUK.18.16": "[De Jesus]{1,3} [aber]{2} [hät]{4} [si]{5} [zu sich grüeft]{4} [und gseit]{6}: «[Lönd]{7} [d Chind]{8,9} [zu]{11} [mir]{12} [choo]{10} und{13} [hindered]{15} [si]{16} [nöd]{14}; [dänn]{18} [settige]{17,19} [ghört]{20} [s Riich]{21,22} [vo Gott]{23,24}.",
 "LUK.18.17": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Wär]{4,5} [s Riich]{8,9} [vo Gott]{10,11} [nöd]{6} [aanimmt]{7} [wie]{12} [es Chind]{13}, [dä chunnt]{16} [sicher nöd]{14,15} [ine]{17,18}.»",
 "LUK.18.18": "Und{1} [en]{3} [füerende Maa]{5} [hät]{2} [en]{4} [gfröget]{2}: «[Guete]{8} [Lehrer]{7}, [was]{9} [mues ich mache]{10}, demit ich [ewigs]{12} [Läbe]{11} [erbe]{13}?» ~6(λέγων «sägend» leitet d Red ii)",
 "LUK.18.19": "[De Jesus]{4,5} [aber]{2} [hät]{1} [zu ihm]{3} [gseit]{1}: «[Werum]{6} [seisch]{8} du [mir]{7} [guet]{9}? [Niemer]{10} isch [guet]{11} [usser]{12,13} [Gott]{15,16} [elei]{14}.",
 "LUK.18.20": "[D Gebot]{1,2} [kännsch du]{3}: ‹[Du söllsch nöd]{4} [d Ee breche]{5}, [du söllsch nöd]{6} [töte]{7}, [du söllsch nöd]{8} [stäle]{9}, [du söllsch nöd]{10} [falsch uussäge]{11}, [ehr]{12} [din]{15} [Vatter]{13,14} und{16} dini [Mueter]{17,18}.›»",
 "LUK.18.21": "[Er]{1} [aber]{2} [hät gseit]{3}: «[Das]{4} [alles]{5} [han ich ghalte]{6} [vo]{7} [minere]{9} [Jugend]{8} [aa]{7}.»",
 "LUK.18.22": "[Wo]{1} [de Jesus]{3,4} das [ghört hät]{1}, [hät er]{5} [zu ihm]{6} [gseit]{5}: «[Eis]{8} [fäält]{10} [dir]{9} [no]{7}: [Verchauf]{14} [alles]{11}, [was]{12} [du häsch]{13}, und{15} [verteil s]{16} [a d Arme]{17}, und{18} [du wirsch]{19} [en Schatz]{20} [im]{21} [Himmel]{22} [ha]{19}; und{23} [chumm]{24}, [folg]{25} [mir]{26} [nache]{25}!» ~2",
 "LUK.18.23": "[Wo]{3} [er]{1} [das]{4} [aber]{2} [ghört hät]{3}, [isch er]{6} [ganz truurig]{5} [worde]{6}; [er isch]{7} [nämli]{8} [sehr]{10} [riich]{9} [gsii]{7}.",
 "LUK.18.24": "[De Jesus]{4,5} [aber]{2} [hät]{1} [en]{3} [aagluegt]{1} [und gseit]{6}: «[Wie]{7} [schwär]{8} [chömed]{18} [die]{9}, wo [Vermöge]{10,11} [händ]{12}, [is]{13,14} [Riich]{15} [vo Gott]{16,17} [ine]{18}!",
 "LUK.18.25": "[Es isch]{3} [nämli]{2} [liechter]{1}, dass [es Kamel]{4} [dur]{5} [es Nadelööhr]{6,7} [gaat]{8}, [als]{9} dass [en Riiche]{10} [is]{11,12} [Riich]{13} [vo Gott]{14,15} [ine chunnt]{16}.»",
 "LUK.18.26": "[D Zuehörer]{3,4} [aber]{2} [händ gseit]{1}: «[Wär]{6} [cha]{7} [dänn]{5} [grettet wärde]{8}?»",
 "LUK.18.27": "[Er]{1} [aber]{2} [hät gseit]{3}: «[Was]{4} [bi]{6} [Mänsche]{7} [unmöglich]{5} isch, [isch]{12} [bi]{9} [Gott]{10,11} [möglich]{8}.»",
 "LUK.18.28": "[Da]{2} [hät]{1} [de Petrus]{3,4} [gseit]{1}: «[Lueg]{5}, [mir]{6} [händ]{7} [alles, wo üs ghört hät]{8,9}, [verlaa]{7} und [sind]{10} [dir]{11} [nachegfolget]{10}.»",
 "LUK.18.29": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4} [gseit]{3}: «[Amen]{5}, [ich säg]{6} [eu]{7}: [Es git]{10} [niemer]{9}, [wo]{11} [Huus]{13} [oder]{14} [Frau]{15} [oder]{16} [Brüeder]{17} [oder]{18} [Eltere]{19} [oder]{20} [Chind]{21} [wäge]{22} [em Riich]{23,24} [vo Gott]{25,26} [verlaa hät]{12}, ~8(" + RIGHT_G + ")",
 "LUK.18.30": "[wo]{1} [nöd]{2,3} [vilfach]{5} [zrugg überchunnt]{4} [i]{6} [dere]{9} [Ziit]{7,8} und{10} [i]{11} [de chömende]{14,15} [Wältziit]{12,13} [ewigs]{17} [Läbe]{16}.»",
 "LUK.18.31": "[Er hät]{1} [aber]{2} [di Zwölf]{3,4} [zu sich gnoo]{1} [und hät]{5} [zu ine]{6,7} [gseit]{5}: «[Lueged]{8}, [mir gönd]{9} [uf]{10} [Jerusalem]{11} [ufe]{9}, und{12} [alles]{14}, [wo]{15} [dur]{17} [d Prophete]{18,19} [gschribe isch]{16}, [wird]{13} [am Mänschesohn]{20-23} [erfüllt]{13}.",
 "LUK.18.32": "[Er wird]{1} [nämli]{2} [de Heide]{3,4} [usgliferet]{1} und{5} [verspottet]{6} und{7} [misshandlet]{8} und{9} [aagspöit wärde]{10},",
 "LUK.18.33": "und{1} [si wärded]{3} [en]{4} [uspeitsche]{2} und [umbringe]{3}; und{5} [am]{6} [dritte]{8,9} [Tag]{7} [wird er uferstaa]{10}.»",
 "LUK.18.34": "Und{1} [si]{2} [händ]{5} [nüüt]{3} [devo]{4} [verstande]{5}; und{6} [das]{10} [Wort]{8,9} [isch]{7} [vor]{12} [ine]{13} [verborge]{11} [gsii]{7}, und{14} [si händ]{16} [nöd]{15} [begriffe]{16}, [was gseit worde isch]{17,18}.",
 "LUK.18.35": "[Es isch]{1} [aber]{2} [gsii]{1}, [wo]{3,4} [er]{6} [i d Nöchi]{5} [vo]{7} [Jericho]{8} [choo isch]{5}: [En]{10} [Blinde]{9} [isch]{11} [am]{12,13} [Wäg]{14} [gsässe]{11} [und hät bettlet]{15}.",
 "LUK.18.36": "[Won er]{1} [e Mängi]{3} [verbiiziehe]{4} [ghört hät]{1}, [hät er gfröget]{5}, [was]{6} [das]{8} [sig]{7}. ~2",
 "LUK.18.37": "[Mer hät]{1} [em]{3} [aber]{2} [verzellt]{1}, [dass]{4} [de Jesus]{5} [vo Nazaret]{6,7} [verbiichunnt]{8}.",
 "LUK.18.38": "Und{1} [er hät grüeft]{2}: «[Jesus]{4}, [Sohn]{5} [vom David]{6}, [häb Erbarme]{7} [mit mir]{8}!» ~3(λέγων «sägend» leitet d Red ii)",
 "LUK.18.39": "Und{1} [d Lüüt, wo]{2} [voruusgange sind]{3}, [händ]{4} [en]{5} [aagfahre]{4}, [er söll]{6} [still sii]{7}. [Er]{8} [aber]{9} [hät]{12} [no vil]{10} [lüüter]{11} [gschroue]{12}: «[Sohn]{13} [vom David]{14}, [häb Erbarme]{15} [mit mir]{16}!»",
 "LUK.18.40": "[De Jesus]{3,4} [aber]{2} [isch staa blibe]{1} [und hät befole]{5}, [en]{6} [zu]{8} [sich]{9} [z bringe]{7}. [Wo]{10} [er]{12} [dänn]{11} [nöcher choo isch]{10}, [hät er]{13} [en]{14} [gfröget]{13}:",
 "LUK.18.41": "«[Was]{1} [wottsch]{3}, [dass ich]{4} [dir]{2} [mache]{4}?» [Er]{5} [aber]{6} [hät gseit]{7}: «[Herr]{8}, [dass]{9} [ich wider gseh]{10}!»",
 "LUK.18.42": "Und{1} [de Jesus]{2,3} [hät]{4} [zu ihm]{5} [gseit]{4}: «[Du söllsch wider gseh]{6}! [Din]{9} [Glaube]{7,8} [hät]{10} [dich]{11} [grettet]{10}.»",
 "LUK.18.43": "Und{1} [sofort]{2} [hät er wider gseh]{3}, und{4} [er isch]{5} [ihm]{6} [nachegfolget]{5} [und hät]{7} [Gott]{8,9} [d Ehr ggää]{7}. Und{10} [wo]{14} [s ganz]{11,12} [Volk]{13} das [gseh hät]{14}, [hät s]{15,16} [Gott]{17,18} [globt]{15,16}.",
 # ------------------------------------------------------------ Kapitel 19
 "LUK.19.1": "Und{1} [er isch]{2} [uf Jericho]{4,5} [choo]{2} und [isch dur d Stadt zoge]{3}.",
 "LUK.19.2": "Und{1} [lueg]{2}, da isch [en Maa]{3} gsii, wo [Zachäus]{6} [gheisse hät]{4,5}; und{7} [er]{8} [isch]{9} [Oberzöllner]{10} und{11} [riich]{13} [gsii]{9}. ~12(αὐτός «er» widerholt s Subjekt; nöd eigens widergää)",
 "LUK.19.3": "Und{1} [er hät probiert]{2} [z gseh]{3}, [wer]{6} [de Jesus]{4,5} [isch]{7}, und{8} [er hät s]{10} [nöd]{9} [chöne]{10} [wäge]{11} [de Mängi]{12,13}; [dänn]{14} [er isch]{18} [vo Gstalt]{15,16} [chlii]{17} [gsii]{18}.",
 "LUK.19.4": "Und{1} [er isch]{2} [voruus]{3-5} [gsprunge]{2} [und isch]{6} [uf]{7} [en Maulbeerfiigebaum]{8} [ufegchlätteret]{6}, [demit]{9} [er]{10} [en]{11} [gseht]{10}; [dänn]{12} [er hät]{14} [dört]{13} [söle]{14} [verbiichoo]{15}.",
 "LUK.19.5": "Und{1} [wo]{2} [de Jesus]{8,9} [a]{4} [d Stell]{5,6} [choo isch]{3}, [hät er ufegluegt]{7} [und]{10} [zu ihm]{11,12} [gseit]{10}: «[Zachäus]{13}, [chumm]{15} [schnell]{14} [abe]{15}! [Dänn]{17} [hüt]{16} [mues ich]{22,23} [i]{18} [dim]{21} [Huus]{19,20} [bliibe]{24}.»",
 "LUK.19.6": "Und{1} [er isch]{3} [schnell]{2} [abechoo]{3} und{4} [hät]{5} [en]{6} [mit Fröid]{7} [ufgnoo]{5}.",
 "LUK.19.7": "Und{1} [alli]{3}, [wo s gseh händ]{2}, [händ gmotzt]{4} [und gseit]{5}: «[Bi]{7} [eme sündige]{8} [Maa]{9} [isch er iicheert]{10}, [zum dört z Gascht sii]{11}!» ~6(" + RIGHT_G + ")",
 "LUK.19.8": "[De Zachäus]{3} [aber]{2} [isch häregstande]{1} [und hät]{4} [zum]{5,6} [Herr]{7} [gseit]{4}: «[Lueg]{8}, [Herr]{14}, [d Hälfti]{9,10} [vo mim]{11} [Vermöge]{12,13} [gib ich]{17} [de Arme]{15,16}, und{18} [wänn]{19} [ich]{22} [öpperem]{20} [öppis]{21} [abprässt ha]{22}, [gib ich]{23} [s vierfach]{24} [zrugg]{23}.»",
 "LUK.19.9": "[De Jesus]{5,6} [aber]{2} [hät]{1} [zu ihm]{3,4} [gseit]{1}: «[Hüt]{8} [isch]{13} [Rettig]{9} [zu dem]{10,12} [Huus]{11} [choo]{13}, [dänn]{14} [au]{15} [er]{16} [isch]{19} [en Sohn]{17} [vom Abraham]{18}. ~7(" + RIGHT_G + ")",
 "LUK.19.10": "[Dänn]{2} [de Mänschesohn]{3-6} [isch choo]{1}, [zum sueche]{7} und{8} [zum rette]{9}, [was]{10} [verlore isch]{11}.»",
 "LUK.19.11": "[Wo]{1} [si]{3} [das]{4} [aber]{2} [ghört händ]{1}, [hät er]{6} [no]{5} [es Gliichnis]{7} [verzellt]{6}, [wil]{8,9} [er]{13} [nöch]{10} [bi Jerusalem]{12} [gsii isch]{11} und{14} [si]{16} [gmeint händ]{15}, [dass]{17} [s Riich]{20,21} [vo Gott]{22,23} [sofort]{18} [söll]{19} [sichtbar wärde]{24}.",
 "LUK.19.12": "[Er hät]{1} [also]{2} [gseit]{1}: «[En]{4} [Maa]{3} [us vornähmer Familie]{5} [isch]{6} [in]{7} [es wiit entfernts]{9} [Land]{8} [greist]{6}, zum [sich]{11} [d Königswürde]{12} [z hole]{10} und{13} [zrugg z choo]{14}.",
 "LUK.19.13": "[Er hät]{1} [aber]{2} [zää]{3} [vo sine]{5} [Chnächt]{4} [grüeft]{1}, [hät]{6} [ine]{7} [zää]{8} [Mine]{9} [ggää]{6} und{10} [hät]{11} [zu ine]{12,13} [gseit]{11}: ‹[Mached Gschäft demit]{14}, [bis]{15,16} [ich chume]{17}!›",
 "LUK.19.14": "[Sini]{4} [Mitbürger]{1,3} [aber]{2} [händ]{5} [en]{6} [ghasst]{5} und{7} [händ]{8} [e Gsandtschaft]{9} [hinder]{10} [ihm]{11} [nache]{10} [gschickt]{8} [und händ la säge]{12}: ‹[Mir wänd]{14} [nöd]{13}, dass [dä]{15} [über]{17} [üs]{18} [König wird]{16}!›",
 "LUK.19.15": "Und{1} [wo]{3,4} [er]{6} [zruggchoo isch]{5}, nachdem er [d Königswürde]{8,9} [übercho hät]{7}, [dänn]{10} [hät er]{11} [die]{16} [Chnächt]{14,15}, [won er ine]{17} [s Silber]{19,20} [ggää gha hät]{18}, [zu sich]{13} [la rüefe]{12}, [demit er]{21} [erfahrt]{22}, [was]{23} [si erwirtschaftet händ]{24}. ~2(" + EGEN_G + ")",
 "LUK.19.16": "[Da]{2} [isch]{1} [de]{3} [erscht]{4} [choo]{1} [und hät gseit]{5}: ‹[Herr]{6}, [dini]{9} [Mine]{7,8} [hät]{11} [zää]{10} [Mine]{12} [dezue verdient]{11}.›",
 "LUK.19.17": "Und{1} [er hät]{2} [zu ihm]{3} [gseit]{2}: ‹[Guet gmacht]{4}, [du guete]{5} [Chnächt]{6}! [Wil]{7} [du]{11} [im]{8} [Chliinschte]{9} [tröi]{10} [gsii bisch]{11}, [söllsch du]{12} [Macht]{13} [ha]{14} [über]{15} [zää]{16} [Städt]{17}.›",
 "LUK.19.18": "Und{1} [de]{3} [zweit]{4} [isch choo]{2} [und hät gseit]{5}: ‹[Dini]{8} [Mine]{6,7}, [Herr]{9}, [hät]{10} [föif]{11} [Mine]{12} [iibracht]{10}.›",
 "LUK.19.19": "[Zu dem]{4} [hät er]{1} [aber]{2} [ebeso]{3} [gseit]{1}: ‹[Au]{5} [du]{6} [söllsch]{8} [über]{7} [föif]{9} [Städt]{10} [regiere]{8}.›",
 "LUK.19.20": "Und{1} [de]{2} [ander]{3} [isch choo]{4} [und hät gseit]{5}: ‹[Herr]{6}, [lueg]{7}, da isch [dini]{10} [Mine]{8,9}; [die]{11} [han ich]{12} [i]{14} [eme Tüechli]{15} [ufbewahrt]{13}.",
 "LUK.19.21": "[Ich han]{1} [nämli]{2} [Angscht gha]{1} [vor dir]{3}, [wil]{4} [du]{7} [en stränge]{6} [Maa]{5} [bisch]{7}: [Du nimmsch]{8}, [was]{9} du [nöd]{10} [anegleit häsch]{11}, und{12} [ärntisch]{13}, [was]{14} du [nöd]{15} [gsäit häsch]{16}.›",
 "LUK.19.22": "[Er seit]{1} [zu ihm]{2}: ‹[Nach]{3} [dine eigete Wort]{4-6} [richt ich]{7} [dich]{8}, [du böse]{9} [Chnächt]{10}! [Du häsch gwüsst]{11}, [dass]{12} [ich]{13} [en stränge]{15} [Maa]{14} [bi]{16}: [Ich nimm]{17}, [was]{18} ich [nöd]{19} [anegleit ha]{20}, und{21} [ärnte]{22}, [was]{23} ich [nöd]{24} [gsäit ha]{25}?",
 "LUK.19.23": "Und{1} [werum]{2,3} [häsch]{5} [mis]{6} [Silber]{7,8} [nöd]{4} [uf]{9} [d Bank]{10} [bracht]{5}? [Dänn]{11} [hett]{15} [ich]{11} [s]{16} [bi minere Rückchehr]{12} [mit]{13} [Zins]{14} [iizoge]{17}.›",
 "LUK.19.24": "Und{1} [zu de Umstehende]{2,3} [hät er gseit]{4}: ‹[Nämed]{5} [em]{6,7} [d Mine]{8,9} [wäg]{5} und{10} [gänd si]{11} [dem]{12}, [wo]{16} [di zää]{13,14} [Mine]{15} [hät]{16}!› –",
 "LUK.19.25": "– und{1} [si händ]{2} [zu ihm]{3} [gseit]{2}: ‹[Herr]{4}, [er hät]{5} [zää]{6} [Mine]{7}!› –",
 "LUK.19.26": "‹[Ich säg]{1} [eu]{2}: [Jedem]{4,5}, [wo hät]{6}, [wird ggää]{7}; [vo]{8} [dem]{10} [aber]{9}, wo [nüüt]{11} [hät]{12}, [wird]{16} [au]{13} [das, wo]{14} [er hät]{15}, [wäggnoo]{16}. ~3(" + RIGHT_G + ")",
 "LUK.19.27": "[Aber]{1} [mini]{4} [Find]{2,3} [da]{5}, [wo]{6} [nöd]{7} [händ wele]{8}, [dass ich]{9} [über]{11} [si]{12} [König wird]{10}, [bringed]{13} [da ane]{14} und{15} [mached]{16} [si]{17} [vor]{18} [mine Auge]{19} [nider]{16}!›»",
 "LUK.19.28": "Und{1} [nachdem er]{2} [das]{3} [gseit hät]{2}, [isch er]{4} [voruus]{5} [gange]{4} [und isch]{6} [uf]{7} [Jerusalem]{8} [ufe]{6}.",
 "LUK.19.29": "Und{1} [wo]{3} [er i d Nöchi]{4} [vo]{5} [Betfage]{6} und{7} [Betanie]{8} [choo isch]{4}, [am]{9,10} [sogenannte]{12,13} [Ölberg]{11,14}, [hät er]{15} [zwei]{16} [vo de]{17} [Jünger]{18} [losgschickt]{15} ~2(" + EGEN_G + ")",
 "LUK.19.30": "[und gseit]{1}: «[Gönd]{2} [i]{3} [s]{4} [Dorf]{6} [gägenüber]{5}! [Wänn ir]{9} [dete]{7,8} [ine chömed]{9}, [wärded ir]{10} [es Füli]{11} [aabunde]{12} [finde]{10}, [wo]{13,14} [no nie]{16} [öpper]{15,17} [druf gsässe isch]{18}. [Binded]{20} [s]{21} [los]{20} und{19} [bringed s]{22}!",
 "LUK.19.31": "Und{1} [wänn]{2} [eu]{4} [öpper]{3} [fröget]{5}: ‹[Werum]{6,7} [binded ir s los]{8}?›, [dänn säged]{10} [eso]{9}: ‹[De Herr]{12,13} [bruucht]{15,16} [s]{14}.›» ~11(" + RIGHT_G + ")",
 "LUK.19.32": "[Die]{3}, [wo gschickt worde sind]{4}, [sind ane gange]{1} [und händ s gfunde]{5}, [wie]{6} er [s ine]{8} [gseit hät]{7}. ~2",
 "LUK.19.33": "[Wo]{1} [si]{3} [aber]{2} [s Füli]{4,5} [losbunde händ]{1}, [händ]{6} [sini]{9} [Bsitzer]{7,8} [zu ine]{10,11} [gseit]{6}: «[Werum]{12} [binded ir]{13} [s Füli]{14,15} [los]{13}?»",
 "LUK.19.34": "[Si]{1} [aber]{2} [händ gseit]{3}: «[De Herr]{5,6} [bruucht]{8,9} [s]{7}.» ~4(" + RIGHT_G + ")",
 "LUK.19.35": "Und{1} [si händ]{2} [s]{3} [zum]{4,5} [Jesus]{6} [bracht]{2}, und{7} [händ]{8} [iri]{9} [Mäntel]{10,11} [uf]{12} [s Füli]{13,14} [gworfe]{8} [und händ]{15} [de Jesus]{16,17} [druf gsetzt]{15}.",
 "LUK.19.36": "[Wo]{1} [er]{3} [aber]{2} [wiiterzoge isch]{1}, [händ si]{4} [iri]{7} [Mäntel]{5,6} [uf]{8} [em]{9} [Wäg]{10} [usbreitet]{4}.",
 "LUK.19.37": "[Wo]{1} [er]{3} [aber]{2} [scho]{4} [nöch]{1} [bim]{5,6} [Abstiig]{7} [vom Ölberg]{8-11} [gsii isch]{1}, [hät]{12} [di ganz]{13,14} [Schar]{15} [vo de Jünger]{16,17} [aagfange]{12}, [voll Fröid]{18} [Gott]{20,21} [mit luuter]{23} [Stimm]{22} [z lobe]{19} [für]{24} [all]{25} [di mächtige Tate]{28}, [wo]{26} [si gseh händ]{27},",
 "LUK.19.38": "[und händ grüeft]{1}: «[Gsägnet]{2} sig [de König]{3,5}, [wo chunnt]{4} [im]{6} [Name]{7} [vom Herr]{8}! [Im]{9} [Himmel]{10} [Fride]{11} und{12} [Ehr]{13} [i]{14} [de Höchi]{15}!»",
 "LUK.19.39": "Und{1} [es paar]{2} [vo de Pharisäer]{3,4} [us]{5} [de Mängi]{6,7} [händ]{8} [zu ihm]{9,10} [gseit]{8}: «[Lehrer]{11}, [wiis]{12} [dini]{15} [Jünger]{13,14} [zrächt]{12}!»",
 "LUK.19.40": "Und{1} [er hät gantwortet]{2} [und gseit]{3}: «[Ich säg]{4} [eu]{5}: [Wänn]{7} [die]{8} [schwiiged]{9}, [dänn wärded]{12} [d Stei]{10,11} [schreie]{12}.» ~6(" + RIGHT_G + ")",
 "LUK.19.41": "Und{1} [wo]{2} [er nöcher choo isch]{3} und [d Stadt]{5,6} [gseh hät]{4}, [hät er]{7} [über]{8} [si]{9} [briegget]{7}",
 "LUK.19.42": "[und gseit]{1}: «[Wänn]{3} doch [au]{9} [du]{10} [a]{5} [dem]{8} [Tag]{6,7} [erchännt hettsch]{4}, [was]{11} [zum Fride füert]{12,13}! – [Jetzt]{14} [aber]{15} [isch es]{16} [vor]{17} [dine]{19} [Auge]{18} [verborge]{16}. ~2(" + RIGHT_G + ")",
 "LUK.19.43": "[Dänn]{1} [es chömed]{2} [Täg]{3} [über]{4} [dich]{5}, und{6} [dini]{10} [Find]{8,9} [wärded]{7} [en Wall]{11} [um dich]{12} [ufschütte]{7} und{13} [dich]{15} [iischlüüsse]{14} und{16} [dich]{18} [vo allne Siite]{19} [bedränge]{17},",
 "LUK.19.44": "und{1} [si wärded]{2} [dich]{3} und{4} [dini]{7} [Chind]{5,6} [i]{8} [dir]{9} [em Bode gliichmache]{2}, und{10} [si wärded]{12} [i]{16} [dir]{17} [kei]{11} [Stei]{13} [uf]{14} [em andere]{15} [laa]{12}, [wil]{18,19} du [d Ziit]{22,23} [vo dinere]{26} [Heimsuechig]{24,25} [nöd]{20} [erchännt häsch]{21}.»",
 "LUK.19.45": "Und{1} [er isch]{2} [in]{3} [Tämpel]{4,5} [ine gange]{2} [und hät aagfange]{6}, [d Händler]{8,9} [usezjage]{7},",
 "LUK.19.46": "[und hät]{1} [zu ine]{2} [gseit]{1}: «[Es staat gschribe]{3}: ‹[Mis]{8} [Huus]{6,7} [wird]{5} [es Huus]{9} [zum Bätte]{10} [sii]{5}.› [Ir]{11} [aber]{12} [händ]{14} [e Röiberhöli]{15,16} [drus]{13} [gmacht]{14}.» ~4(καί «und» leitet s Zitat ii; nöd eigens widergää)",
 "LUK.19.47": "Und{1} [er hät]{2,3} [jede Tag]{4-6} [im]{7,8} [Tämpel]{9} [glehrt]{2,3}. [D Hoheprieschter]{10,12} [aber]{11} und{13} [d Schriftgleerte]{14,15} [händ probiert]{16}, [en]{17} [umzbringe]{18}, [ebeso]{19} [di Füerende]{20,21} [vom Volk]{22,23},",
 "LUK.19.48": "und{1} [si händ]{3} [nöd]{2} [gfunde]{3}, [was]{4,5} [si sötted mache]{6}; [dänn]{9} [s ganz]{10} [Volk]{7,8} [hät]{11} [a sine Lippe]{12,13:idiom} [ghanget]{11}.",
 # ------------------------------------------------------------ Kapitel 20
 "LUK.20.1": "[Und es isch gsii]{1,2} [a]{3} [eim]{4} [vo dene Täg]{5,6}, [wo]{7} [er]{8} [im]{11,12} [Tämpel]{13} [s Volk]{9,10} [glehrt]{7} und{14} [s Evangelium verchündet hät]{15}: [D Hoheprieschter]{17,18} und{19} [d Schriftgleerte]{20,21} [sind]{16} [mit]{22} [de Ältischte]{23,24} [härechoo]{16}",
 "LUK.20.2": "und{1} [händ]{2} [zu ihm]{4,5} [gseit]{2}: «[Säg]{6} [üs]{7}: [Mit]{8} [was für ere]{9} [Vollmacht]{10} [machsch du]{12} [das]{11}? [Oder]{13} [wer]{14} [isch es]{15}, [wo]{16} [dir]{18} [die]{21} [Vollmacht]{19,20} [ggää hät]{17}?» ~3(λέγοντες «sägend»; nöd eigens widergää)",
 "LUK.20.3": "Er [hät]{3} [aber]{2} [gantwortet]{1} und [zu ine]{4,5} [gseit]{3}: «[Au ich]{8} [frög]{6} [eu]{7} [öppis]{9}, und{10} [säged]{11} [mir]{12}:",
 "LUK.20.4": "[D]{1} [Taufi]{2} [vom Johannes]{3}, [isch si]{6} [vom]{4} [Himmel]{5} [gsii]{6} [oder]{7} [vo]{8} [Mänsche]{9}?»",
 "LUK.20.5": "[Si]{1} [aber]{2} [händ]{3} [mitenand]{4,5} [überleit]{3} [und gseit]{6}: «[Wänn]{8} [mir säged]{9}: ‹[Vom]{10} [Himmel]{11}›, [dänn seit er]{12}: ‹[Werum]{13,14} [händ ir]{16} [em]{17} [nöd]{15} [glaubt]{16}?› ~7(" + RIGHT_G + ")",
 "LUK.20.6": "[Wänn]{1} [mir]{3} [aber]{2} [säged]{3}: ‹[Vo]{4} [Mänsche]{5}›, [dänn wird]{9} [s ganz]{8} [Volk]{6,7} [üs]{10} [steinige]{9}; [es isch]{13} [nämli]{12} [überzüügt]{11}, dass [de Johannes]{14} [en Prophet]{15} [gsii isch]{16}.»",
 "LUK.20.7": "Und{1} [si händ gantwortet]{2}, [si wüssed]{4} [nöd]{3}, [vo wo]{5} si sig.",
 "LUK.20.8": "Und{1} [de Jesus]{2,3} [hät]{4} [zu ine]{5} [gseit]{4}: «Dänn [säg]{8} [au]{6} [ich]{7} [eu]{9} [nöd]{6}, [mit]{10} [was für ere]{11} [Vollmacht]{12} ich [das]{13} [mache]{14}.»",
 "LUK.20.9": "[Er hät]{1} [aber]{2} [aagfange]{1}, [em Volk]{3-5} [das]{9} [Gliichnis]{7,8} [z verzelle]{6}: «[En Mänsch]{10} [hät]{11} [en Wiibärg]{12} [aapflanzt]{11} und{13} [hät]{14} [en]{15} [a Wiibuure]{16} [verpachtet]{14} und{17} [isch]{18} [für lang Ziit]{19,20} [verreist]{18}.",
 "LUK.20.10": "Und{1} [zur richtige Ziit]{2} [hät er]{3} [en Chnächt]{7} [zu]{4} [de Wiibuure]{5,6} [gschickt]{3}, [demit]{8} [si]{14} [ihm]{15} [sin Teil]{9,10} [a de Frücht]{11} [vom Wiibärg]{12,13} [gänd]{14}. [D Wiibuure]{16,18} [aber]{17} [händ]{19} [en]{20} [verprüglet]{21} und [mit lääre Händ]{22} [furtgschickt]{19}.",
 "LUK.20.11": "Und{1} [er hät]{4} [no]{2} [en andere]{3} [Chnächt]{5} [gschickt]{4}. [Si]{6} [aber]{7} [händ]{9} [au dä]{8} [verprüglet]{9} und{10} [händ en beschimpft]{11} und [händ en]{12} [mit lääre Händ]{13} [furtgschickt]{12}.",
 "LUK.20.12": "Und{1} [er hät]{4} [no]{2} [en dritte]{3} [gschickt]{4}. [Si]{5} [aber]{6} [händ]{9} [au]{7} [dä]{8} [verwundet]{9} [und usegworfe]{10}.",
 "LUK.20.13": "[Da]{2} [hät]{1} [de Herr]{3,4} [vom Wiibärg]{5,6} [gseit]{1}: ‹[Was]{7} [söll ich mache]{8}? [Ich schick]{9} [min]{12} [gliebte]{13,14} [Sohn]{10,11}; [villicht]{15} [händ si]{17} [vor ihm]{16} [Respekt]{17}.›",
 "LUK.20.14": "[Wo]{1} [d Wiibuure]{4,5} [en]{3} [aber]{2} [gseh händ]{1}, [händ si]{6} [mitenand]{7,8} [überleit]{6} [und gseit]{9}: ‹[Das]{10} [isch]{11} [de Erb]{12,13}; [chömed, mir bringed]{14} [en]{15} [um]{14}, [demit]{16} [s Erb]{19,20} [üs]{17} [ghört]{18}!›",
 "LUK.20.15": "Und{1} [si händ]{2} [en]{3} [us]{4} [em Wiibärg]{5,6} [usegworfe]{2} [und umbracht]{7}. [Was]{8} [wird]{10} [jetzt]{9} [de Herr]{12,13} [vom Wiibärg]{14,15} [mit ine]{11} [mache]{10}?",
 "LUK.20.16": "[Er wird choo]{1} und{2} [die]{6} [Wiibuure]{4,5} [umbringe]{3} und{7} [de Wiibärg]{9,10} [andere]{11} [gää]{8}.» [D Zuehörer]{12} [aber]{13} [händ gseit]{14}: «[Das dörf nöd]{15} [passiere]{16}!»",
 "LUK.20.17": "[Er]{1} [aber]{2} [hät]{3} [si]{4} [aagluegt]{3} [und gseit]{5}: «[Was]{6} [bedüütet]{8} [dänn]{7} [das]{11} [Schriftwort]{9,10}: ‹[De Stei]{12}, [wo]{13} [d Buulüüt]{15,16} [verworfe händ]{14}, [dä]{17} [isch]{18} [zum]{19} [Eckstei]{20,21} [worde]{18}›?",
 "LUK.20.18": "[Jede]{1}, [wo]{2} [uf]{4} [dä]{5} [Stei]{6,7} [gheit]{3}, [wird zerschmätteret]{8}; [uf wän]{9,10} er [aber]{11} [gheit]{12,13}, [dä]{15} [zermalmt er]{14}.»",
 "LUK.20.19": "Und{1} [d Schriftgleerte]{3,4} und{5} [d Hoheprieschter]{6,7} [händ probiert]{2}, [no]{13} [i dere gliiche]{14} [Stund]{15,16} [d Händ]{11,12} [a]{9} [ihn]{10} [z lege]{8}, [aber]{17} [si händ Angscht gha]{18} [vor em Volk]{19,20}; [si händ]{21} [nämli]{22} [gmerkt]{21}, [dass]{23} er [das]{29} [Gliichnis]{27,28} [gäge]{24} [si]{25} [verzellt hät]{26}.",
 "LUK.20.20": "Und{1} [si händ en beobachtet]{2} [und händ]{3} [Spitzel]{4} [gschickt]{3}, wo [sich]{6} [als Grächti]{7} [usggää händ]{5,8}, [demit si]{9} [en]{11} [bi eme Wort]{12} [chönted packe]{10}, [zum]{13} [en]{15} [de Macht]{16,17} und{18} [de Gwalt]{19,20} [vom Statthalter]{21,22} [uszliefere]{14}.",
 "LUK.20.21": "Und{1} [si händ]{2} [en]{3} [gfröget]{2}: «[Lehrer]{5}, [mir wüssed]{6}, [dass]{7} du [richtig]{8} [redsch]{9} und{10} [lehrsch]{11} und{12} [nöd]{13} [uf s Aaseh vo de Person luegsch]{14,15:idiom}, [sondern]{16} [de Wäg]{19,20} [vo Gott]{21,22} [i]{17} [Wahrheit]{18} [lehrsch]{23}. ~4(λέγοντες «sägend»; nöd eigens widergää)",
 "LUK.20.22": "[Isch es]{1} [üs]{2} [erlaubt]{1}, [em Kaiser]{3} [Stüür]{4} [z zale]{5}, [oder]{6} [nöd]{7}?»",
 "LUK.20.23": "Er [hät]{1} [aber]{2} [iri]{3} [Verschlagenheit]{4,5} [duureschaut]{1} [und hät]{6} [zu ine]{7,8} [gseit]{6}:",
 "LUK.20.24": "«[Zeiged]{1} [mir]{2} [en Denar]{3}! [Wem sis]{4} [Bild]{6} und{7} [Ufschrift]{8} [hät er]{5}?» [Si händ]{9} [aber]{10} [gantwortet]{9} [und gseit]{11}: «[Vom Kaiser]{12}.»",
 "LUK.20.25": "[Er]{1} [aber]{2} [hät]{3} [zu ine]{4,5} [gseit]{3}: «[Dänn]{6} [gänd]{7} [em Kaiser]{10} [zrugg]{7}, [was em Kaiser ghört]{8,9}, und{11} [Gott]{15,16}, [was Gott ghört]{12-14}!»",
 "LUK.20.26": "Und{1} [si händ]{3} en [vor]{7} [em Volk]{8,9} [nöd]{2} [bi sinere Red]{5,6} [chöne]{3} [packe]{4}, und{10} [si händ]{11} [über]{12} [sini]{15} [Antwort]{13,14} [gstuunt]{11} [und gschwige]{16}.",
 "LUK.20.27": "[Es sind]{1} [aber]{2} [es paar]{3} [vo de Sadduzäer]{4,5} [härechoo]{1}, [wo]{6} [bestriited]{7}, dass [es en Uferstehig]{8} [git]{10}, [und händ]{11} [en]{12} [gfröget]{11} ~9(μή nach ἀντιλέγω verstärkt d Verneinig; nöd eigens widergää)",
 "LUK.20.28": "[und gseit]{1}: «[Lehrer]{2}, [de Mose]{3} [hät]{4} [üs]{5} [gschribe]{4}: [Wänn]{6} [öpperem]{7} [sin Brueder]{8} [stirbt]{9}, wo [e Frau]{11} [hät]{10}, und{12} [dä]{13} [ohni Chind]{14} [isch]{15}, [dänn söll]{16} [sin]{20} [Brueder]{18,19} [d]{21} [Frau]{22} [nää]{17} und{23} [sim]{28} [Brueder]{26,27} [Nachkomme]{25} [verschaffe]{24}.",
 "LUK.20.29": "[Es sind]{4} [also]{2} [sibe]{1} [Brüeder]{3} [gsii]{4}. Und{5} [de]{6} [erscht]{7} [hät]{8} [e Frau]{9} [gnoo]{8} [und isch]{10} [ohni Chind]{11} [gstorbe]{10}.",
 "LUK.20.30": "Und{1} [de]{2} [zweit]{3},",
 "LUK.20.31": "und{1} [de]{2} [dritt]{3} [hät]{4} [si]{5} [gnoo]{4}, [gnau gliich]{6} [au]{8} [alli]{9} [sibe]{10}: [Si händ]{12} [kei]{11} [Chind]{13} [hinderlaa]{12} und{14} [sind gstorbe]{15}. ~7",
 "LUK.20.32": "[Zletscht]{1} [isch]{5} [au]{2} [d]{3} [Frau]{4} [gstorbe]{5}.",
 "LUK.20.33": "[D]{1} [Frau]{2} [also]{3} – [i]{4} [de]{5} [Uferstehig]{6}: [Wem]{7} [vo ine]{8} [ghört si]{9} [als Frau]{10}? [Dänn]{12} [di]{11} [sibe]{13} [händ]{14} [si]{15} [zur Frau]{16} [gha]{14}.»",
 "LUK.20.34": "Und{1} [de Jesus]{4,5} [hät]{2} [zu ine]{3} [gseit]{2}: «[D Mänsche]{6,7} [vo dere]{10} [Wältziit]{8,9} [hürated]{11} und{12} [wärded verhüratet]{13};",
 "LUK.20.35": "[die]{1} [aber]{2}, [wo würdig befunde wärded]{3}, [säbi]{6} [Wältziit]{4,5} [z erläbe]{7} und{8} [d Uferstehig]{9-11} [vo]{12} [de Tote]{13}, [hürated]{15} [weder]{14}, [no]{16} [wärded si verhüratet]{17};",
 "LUK.20.36": "[dänn]{2} [si chönd]{5} [au nöd]{1} [meh]{4} [stärbe]{3}; [si sind]{8} [nämli]{7} [wie d Ängel]{6} und{9} [sind]{11} [Söhn]{10} [vo Gott]{12}, [wil si]{16} [Söhn]{15} [vo de Uferstehig]{13,14} [sind]{16}.",
 "LUK.20.37": "[Dass]{1} [aber]{2} [d Tote]{4,5} [uferweckt wärded]{3}, [hät]{8} [au]{6} [de Mose]{7} [bim]{9,10} [Dornbusch]{11} [aazeigt]{8}, [wo]{12} er [de Herr]{14} ‹[de Gott]{15,16} [vom Abraham]{17} und{18} [Gott]{19} [vom Isaak]{20} und{21} [Gott]{22} [vom Jakob]{23}› [nännt]{13}.",
 "LUK.20.38": "[Er isch]{4} [aber]{2} [nöd]{3} [en Gott]{1} [vo Tote]{5}, [sondern]{6} [vo Läbige]{7}; [dänn]{9} [für ihn]{10} [läbed]{11} [alli]{8}.»",
 "LUK.20.39": "[Es paar]{3} [vo de Schriftgleerte]{4,5} [aber]{2} [händ gantwortet]{1} [und gseit]{6}: «[Lehrer]{7}, [du häsch]{9} [guet]{8} [gredt]{9}.»",
 "LUK.20.40": "[Dänn]{2} [si händ sich]{3} [nüme]{1} [traut]{3}, [en]{5} [öppis]{6} [z fröge]{4}.",
 "LUK.20.41": "[Er hät]{1} [aber]{2} [zu ine]{3,4} [gseit]{1}: «[Wie]{5} [säged si]{6}, [de Christus]{7,8} [sig]{9} [de Sohn]{11} [vom David]{10}?",
 "LUK.20.42": "[De David]{3} [sälber]{1} [seit]{4} [nämli]{2} [im]{5} [Buech]{6} [vo de Psalme]{7}: ‹[De Herr]{9} [hät]{8} [zu]{10} [mim]{12} [Herr]{11} [gseit]{8}: [Sitz]{13} [zu]{14} [minere]{16} [Rächte]{15},",
 "LUK.20.43": "[bis]{1,2} [ich]{3} [dini]{6} [Find]{4,5} [zum Schämel]{7} [vo dine]{10} [Füess]{8,9} [mache]{3}.›",
 "LUK.20.44": "[De David]{1} [nännt]{5} [en]{3} [also]{2} ‹[Herr]{4}›; und{6} [wie]{7} [isch er]{10} dänn [sin]{8} [Sohn]{9}?»",
 "LUK.20.45": "[Während]{1} [aber]{2} [s ganz]{3,4} [Volk]{5} [zueglost hät]{1}, [hät er]{6} [zu de]{7} [Jünger]{8} [gseit]{6}:",
 "LUK.20.46": "«[Nämed eu in Acht]{1} [vor]{2} [de Schriftgleerte]{3,4}, [wo]{5} [gärn]{6} [i lange Gwänder]{8,9} [umelaufed]{7} und{10} [d Grüess]{12} [uf]{13} [de Märtplätz]{14,15} [gärn händ]{11} und{16} [d Ehreplätz]{17} [i]{18} [de Synagoge]{19,20} und{21} [di beschte Plätz]{22} [a]{23} [de Fäschtässe]{24,25},",
 "LUK.20.47": "[wo]{1} [d Hüüser]{3,4} [vo de Witwe]{5,6} [uffrässed]{2} und{7} [zum Schii]{8} [lang]{9} [bätted]{10}. [Die]{11} [wärded]{12} [es umso härters]{13} [Urteil]{14} [übercho]{12}.»",
 # ------------------------------------------------------------ Kapitel 21
 "LUK.21.1": "[Er hät]{1} [aber]{2} [ufegluegt]{1} [und hät]{3} [gseh]{3}, wie [d Riiche]{4,12} [iri]{11} [Gabe]{9,10} [i]{6} [de Opferstock]{7,8} [iigworfe händ]{5}.",
 "LUK.21.2": "[Da]{2} [hät er]{1} [e]{3} [armi]{5} [Witwe]{4} [gseh]{1}, wo [dört]{7} [zwei]{9} [Lepta]{8} [iigworfe hät]{6},",
 "LUK.21.3": "und{1} [hät gseit]{2}: «[Wahrhaftig]{3}, [ich säg]{4} [eu]{5}: [Die]{11} [armi]{10} [Witwe]{7-9} [hät]{14} [meh]{12} [iigworfe]{14} [als alli]{13}. ~6(" + RIGHT_G + ")",
 "LUK.21.4": "[Dänn]{2} [die]{3} [alli]{1} [händ]{8} [us]{4} [irem]{7} [Überfluss]{5,6} [zu]{9} [de Gabe]{10,11} [iigworfe]{8}; [si]{12} [aber]{13} [hät]{23} [us]{14} [irem]{17} [Mangel]{15,16} [de ganz]{18} [Läbesunderhalt]{19,20}, [wo]{21} [si gha hät]{22}, [iigworfe]{23}.»",
 "LUK.21.5": "Und{1} [wo]{3} [es paar]{2} [vom]{4,5} [Tämpel]{6} [gseit händ]{3}, [dass]{7} er [mit schöne]{9} [Stei]{8} und{10} [Weihgschänk]{11} [gschmückt sig]{12}, [hät er gseit]{13}:",
 "LUK.21.6": "«[Das]{1}, [was]{2} [ir da gsehnd]{3} – [es chömed]{4} [Täg]{5}, [wo]{6,7} [kei]{8} [Stei]{10} [uf]{11} [em andere]{12} [bliibt]{9}, [wo]{13} [nöd]{14} [abbroche wird]{15}.»",
 "LUK.21.7": "[Si händ]{1} [en]{3} [aber]{2} [gfröget]{1}: «[Lehrer]{5}, [wänn]{6} [passiert]{9} [das]{8} [dänn]{7}, und{10} [was]{11} isch [s Zeiche]{12,13}, [wänn]{14} [das]{16} [söll]{15} [passiere]{17}?» ~4(λέγοντες «sägend»; nöd eigens widergää)",
 "LUK.21.8": "[Er]{1} [aber]{2} [hät gseit]{3}: «[Passed uf]{4}, [dass ir eu]{6} [nöd]{5} [i d Irri füere lönd]{6}! [Dänn]{8} [vili]{7} [wärded]{9} [i]{10} [mim]{13} [Name]{11,12} [choo]{9} [und säge]{14}: ‹[Ich]{15} [bi s]{16}!›, und{17}: ‹[D Ziit]{18,19} [isch nöch]{20}!› [Laufed]{22} [ine]{24} [nöd]{21} [nache]{23}!",
 "LUK.21.9": "[Wänn]{1} [ir]{3} [aber]{2} [vo Chrieg]{4} und{5} [Ufständ]{6} [ghöred]{3}, [lönd eu]{8} [nöd]{7} [verschrecke]{8}! [Dänn]{10} [das]{11} [mues]{9} [zerscht]{13} [passiere]{12}, [aber]{14} [s Änd]{17,18} chunnt [nöd]{15} [grad]{16}.»",
 "LUK.21.10": "[Dänn]{1} [hät er]{2} [zu ine]{3} [gseit]{2}: «[Es wird sich]{4} [Volk]{5} [gäge]{6} [Volk]{7} [erhebe]{4} und{8} [Riich]{9} [gäge]{10} [Riich]{11};",
 "LUK.21.11": "[es wird]{10} [grossi]{3} [Ärdbebe]{1} [gää]{10} und{4} [a vilne Orte]{5,6} [Hungersnöt]{7} und{8} [Süüche]{9}; [Schrecklichs]{11} und{12,13} [grossi]{17} [Zeiche]{14} [vom]{15} [Himmel]{16} [wird s gää]{18}. ~2(τε «und»; nöd eigens widergää)",
 "LUK.21.12": "[Vor]{1} [all]{4} [dem]{3} [aber]{2} [wärded si]{5} [iri]{10} [Händ]{8,9} [a]{6} [eu]{7} [lege]{5} und{11} [eu verfolge]{12}; [si wärded eu]{13} [a]{14} [d Synagoge]{15,16} und{17} [i d Gfängnis]{18} [uslifere]{13}, und [ir wärded]{19} [vor]{20} [König]{21} und{22} [Statthalter]{23} [gfüert]{19} [wäge]{24} [mim]{27} [Name]{25,26}.",
 "LUK.21.13": "[Das wird]{1} [für eu]{2} [zum]{3} [Zügnis]{4} [füere]{1}.",
 "LUK.21.14": "[Nämed eu]{1} [also]{2} [z Härze]{3-6}, eu [nöd]{7} [zum voruus Gedanke z mache]{8}, [wie ir eu verteidiged]{9};",
 "LUK.21.15": "[dänn]{2} [ich]{1} [wirde]{3} [eu]{4} [di richtige Wort]{5} und{6} [Wiisheit]{7} [gää]{3}, [dene]{8} [alli]{14} [eui]{17} [Gägner]{15,16} [weder]{9} [chönd]{10} [standhalte]{11} [no]{12} [widerspräche]{13}.",
 "LUK.21.16": "[Ir wärded]{1} [aber]{2} [sogar]{3} [vo]{4} [Eltere]{5} und{6} [Brüeder]{7} und{8} [Verwandte]{9} und{10} [Fründe]{11} [usgliferet]{1}, und{12} [si wärded]{13} [es paar]{14} [vo eu]{15} [umbringe]{13},",
 "LUK.21.17": "und{1} [ir wärded]{2} [vo]{4} [allne]{5} [ghasst]{3} [sii]{2} [wäge]{6,7} [mim]{9} [Name]{8}.",
 "LUK.21.18": "Und{1} [kei]{7,8} [Haar]{2} [vo]{3} [eurem]{6} [Chopf]{4,5} [gaat verlore]{9}.",
 "LUK.21.19": "[Mit]{1} [eurem]{4} [Durehebe]{2,3} [gwünned]{5} [eues]{8} [Läbe]{6,7}!",
 "LUK.21.20": "[Wänn]{1} [ir]{3} [aber]{2} [Jerusalem]{7} [vo Heer]{5,6} [umzinglet]{4} [gsehnd]{3}, [dänn]{8} [merked]{9}, [dass]{10} [sini]{14} [Verwüeschtig]{12,13} [nöch]{11} [isch]{11}.",
 "LUK.21.21": "[Dänn]{1} [söled]{6} [die]{2} [z]{3} [Judäa]{4,5} [i]{7} [d Bärge]{8,9} [flüchte]{6}, und{10} [die]{11} [i]{12} [de Stadt]{13,14} [söled usegaa]{15}, und{16} [die]{17} [uf]{18} [em Land]{19,20} [söled]{22} [nöd]{21} [ine]{23,24} [gaa]{22};",
 "LUK.21.22": "[dänn]{1} [das]{4} [sind]{5} [Täg]{2} [vom Strafgricht]{3}, [demit]{6} [alles]{8} [erfüllt wird]{7}, [was]{9} [gschribe isch]{10}.",
 "LUK.21.23": "[Weh]{1} [de]{2} [Schwangere]{3-5} und{6} [dene]{7}, [wo stilled]{8}, [i]{9} [dene]{10} [Täg]{11,12}! [Dänn]{14} [es wird]{13} [grossi]{16} [Not]{15} [im]{17,18} [Land]{19} [sii]{13} und{20} [Zorn]{21} [über]{22} [das]{24} [Volk]{23},",
 "LUK.21.24": "und{1} [si wärded]{2} [dur d Schärfi]{3} [vom Schwärt]{4} [falle]{2} und{5} [als Gfangeni]{6} [zu]{7} [allne]{10} [Völker]{8,9} [verschleppt wärde]{6}, und{11} [Jerusalem]{12} [wird]{13} [vo]{15} [de Völker]{16} [zertrampet wärde]{14}, [bis]{17,18} [d Ziite]{20} [vo de Völker]{21} [erfüllt sind]{19}.",
 "LUK.21.25": "Und{1} [es wird]{2} [Zeiche]{3} [a]{4} [de Sunne]{5} und{6} [am Mond]{7} und{8} [a de Stärne]{9} [gää]{2}, und{10} [uf]{11} [de Ärde]{12,13} [Angscht]{14} [under de Völker]{15}, [wo ratlos sind]{16,17} [wäge em Toose]{18} [vom Meer]{19} und{20} [vo de Wälle]{21},",
 "LUK.21.26": "[d Mänsche]{2} [vergönd]{1} [vor]{3} [Forcht]{4} und{5} [im Warte]{6} [uf das, wo]{7} [über]{9} [d Wält]{10} [chunnt]{8}; [dänn]{12} [d Mächt]{11,13} [vom Himmel]{14,15} [wärded erschütteret]{16}.",
 "LUK.21.27": "Und{1} [dänn]{2} [wärded si]{3} [de Mänschesohn]{4-7} [gseh]{3} [choo]{8} [i]{9} [ere Wolche]{10} [mit]{11} [Macht]{12} und{13} [grosser]{15} [Herrlichkeit]{14}.",
 "LUK.21.28": "[Wänn]{1} [das]{3} [aber]{2} [aafangt]{1} [z passiere]{4}, [dänn richted eu uf]{5} und{6} [hebed]{7} [eui]{10} [Chöpf]{8,9} [uf]{7}, [wil]{11} [eui]{15} [Erlösig]{13,14} [nöch chunnt]{12}.»",
 "LUK.21.29": "Und{1} [er hät]{2} [ine]{4} [es Gliichnis]{3} [verzellt]{2}: «[Lueged]{5} [de Fiigebaum]{6,7} und{8} [alli]{9} [Bäum]{10,11} [aa]{5}:",
 "LUK.21.30": "[Wänn]{1} si [scho]{3} [ustriibed]{2}, [gsehnd ir s]{4} [und merked]{7} [vo sälber]{5,6}, [dass]{8} [de Summer]{11,12} [scho]{9} [nöch]{10} [isch]{13}.",
 "LUK.21.31": "[So]{1} [au]{2} [ir]{3}: [Wänn]{4} ir [das]{6} [gsehnd]{5} [passiere]{7}, [merked]{8}, [dass]{9} [s Riich]{12,13} [vo Gott]{14,15} [nöch]{10} [isch]{11}.",
 "LUK.21.32": "[Amen]{1}, [ich säg]{2} [eu]{3}: [Die]{10} [Generation]{8,9} [vergaat]{7} [nöd]{5,6}, [bis]{11,12} [alles]{13} [passiert]{14}. ~4(" + RIGHT_G + ")",
 "LUK.21.33": "[De Himmel]{1,2} und{3} [d Ärde]{4,5} [vergönd]{6}, [mini]{10} [Wort]{7,9} [aber]{8} [vergönd]{13} [nöd]{11,12}.",
 "LUK.21.34": "[Lueged]{1} [aber]{2} [uf eu sälber]{3}, [dass]{4} [eui]{6} [Härz]{7,8} [nöd]{4} [beschwärt wärded]{5} [dur]{9} [Rusch]{10} und{11} [Suff]{12} und{13} [Sorge]{14} [vom Alltag]{15} und{16} [säbe]{23} [Tag]{21,22} nöd [plötzlich]{20} [über]{18} [eu]{19} [chunnt]{17}",
 "LUK.21.35": "[wie]{1} [e Falle]{2}. [Dänn]{4} [er chunnt]{3} [über]{5} [alli]{6}, [wo]{7} [uf]{9} [de ganze]{11} [Ärde]{10,12,13} [wohned]{8}.",
 "LUK.21.36": "[Bliibed]{1} [aber]{2} [jederziit]{3-5} [wach]{1} [und bätted]{6}, [demit]{7} [ir d Chraft händ]{8}, [dem allem]{10,11} [z entchoo]{9}, [wo]{12} [söll]{13} [passiere]{14}, und{15} [vor]{17} [em Mänschesohn]{18-21} [z bestaa]{16}.»",
 "LUK.21.37": "[Er hät]{1,8} [aber]{2} [tagsüber]{3,4} [im]{5,6} [Tämpel]{7} [glehrt]{1,8}; [znacht]{9,11} [aber]{10} [isch er usegange]{12} [und hät]{13} [uf]{14} [em]{15} [sogenannte]{17,18} [Ölberg]{16,19} [übernachtet]{13}.",
 "LUK.21.38": "Und{1} [s ganz]{2,3} [Volk]{4} [isch]{5} [am Morge früe]{5} [zu]{6} [ihm]{7} [in]{8,9} [Tämpel]{10} [choo]{5}, zum [em]{12} [zuelose]{11}.",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ('LUK.20.24', 'Denar', 'literal', 'δηνάριον', None, None, 'Römische Silbermünze mit Bild und Aufschrift des Kaisers, etwa der übliche Tageslohn eines Arbeiters ([[MAT.20.2]]). Damaliger Münzname im Text, Wert in der Erklärung (Entscheid Andi Neck 2026-10-26).'),
 ('LUK.19.23', 'Silber', 'literal', 'τὸ ἀργύριον', None, ['Geld'], 'Wie [[LUK.19.15]]. ἀργύριον einheitlich: Einzahl «Silber», Mehrzahl ἀργύρια «Silberstücke» ([[MAT.26.15]]). Damaliger Münzname im Text, Wert in der Erklärung (Entscheid Andi Neck 2026-10-26).'),
 ('LUK.19.15', 'das Silber', 'literal', 'τὸ ἀργύριον', None, ['das Geld'], 'Gemeint sind die Minen ([[LUK.19.13]]), ein Gewicht Silber von hundert Drachmen, etwa hundert Tageslöhnen. ἀργύριον einheitlich: Einzahl «Silber», Mehrzahl ἀργύρια «Silberstücke» ([[MAT.26.15]]). Damaliger Münzname im Text, Wert in der Erklärung (Entscheid Andi Neck 2026-10-26).'),
 # Kapitel 18
 ("LUK.18.1", "den Mut verlieren", "literal", "ἐγκακεῖν", None, ["nachlassen", "müde werden"], "ἐγκακέω heisst «müde werden, aufgeben». Lukas nennt den Zweck des Gleichnisses, bevor er es erzählt."),
 ("LUK.18.3", "Verschaffe mir Recht", "literal", "Ἐκδίκησόν με", None, ["Hilf mir zu meinem Recht"], "ἐκδικέω ist hier ein Wort aus dem Rechtsleben: jemandem zu seinem Recht verhelfen, nicht «rächen». Dasselbe Wortfeld steht in [[LUK.18.5]], [[LUK.18.7]] und [[LUK.18.8]]."),
 ("LUK.18.5", "zermürbt", "interpretive", "ὑπωπιάζῃ", "unter die Augen schlägt", ["ins Gesicht schlägt", "blossstellt"], "ὑπωπιάζω kommt aus dem Faustkampf: «ein blaues Auge schlagen». Übertragen kann es «zermürben» oder «blamieren» heissen. Ob der Richter ernsthaft Gewalt befürchtet oder übertreibt, bleibt offen."),
 ("LUK.18.5", "ohne Ende", "interpretive", "εἰς τέλος", None, ["schliesslich", "am Ende"], "εἰς τέλος kann «bis zum Ende, ständig» oder «schliesslich» heissen."),
 ("LUK.18.6", "der ungerechte Richter", "adapted", "ὁ κριτὴς τῆς ἀδικίας", "der Richter der Ungerechtigkeit", None, "Semitisch geprägter Genitiv der Eigenschaft; im Deutschen als Adjektiv."),
 ("LUK.18.7", "lässt er sie warten", "interpretive", "μακροθυμεῖ ἐπʼ αὐτοῖς", "ist er langmütig über ihnen", ["hat er Geduld mit ihnen", "zögert er bei ihnen"], "Bezug und Sinn des Satzes sind umstritten. Er kann als zweite Frage gelesen werden («Lässt er sie warten?») oder als Nachsatz («auch wenn er mit ihnen Geduld hat»). μακροθυμέω heisst sonst «geduldig, langmütig sein»."),
 ("LUK.18.8", "der Menschensohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "der Sohn des Menschen", ["der Mensch"], "«Sohn eines Menschen» heisst hebräisch und aramäisch einfach «Mensch». Bei Jesus ist es eine Selbstbezeichnung, oft mit Anklang an [[DAN.7.13]]. Ebenso in [[LUK.18.31]], [[LUK.19.10]], [[LUK.21.27]] und [[LUK.21.36]]."),
 ("LUK.18.8", "den Glauben", "literal", "τὴν πίστιν", None, ["diesen Glauben", "Treue"], "Mit Artikel: gemeint ist wohl der Glaube, der wie die Witwe beharrlich bittet."),
 ("LUK.18.10", "ein Zöllner", "traditional", "τελώνης", None, ["ein Steuereinnehmer"], "Zöllner trieben im Auftrag von Pächtern Zölle und Abgaben ein. Sie galten als habgierig und unrein, weil sie mit der Besatzungsmacht zusammenarbeiteten."),
 ("LUK.18.11", "stellte sich hin und betete bei sich so", "interpretive", "σταθεὶς πρὸς ἑαυτὸν ταῦτα προσηύχετο", None, ["stellte sich für sich hin und betete so", "betete zu sich selbst"], "πρὸς ἑαυτόν kann zu «stellte sich hin» gehören (abseits) oder zu «betete» (still bei sich, oder spitz: «zu sich selbst»). WH und Treg stellen ταῦτα voran, was die Verbindung mit «betete» nahelegt."),
 ("LUK.18.12", "in der Woche", "literal", "τοῦ σαββάτου", "des Sabbats", None, "σάββατον heisst auch «Woche». Das Gesetz schrieb nur am Versöhnungstag ein Fasten vor; zweimal wöchentlich zu fasten war freiwillige Frömmigkeit."),
 ("LUK.18.13", "sei mir Sünder gnädig", "interpretive", "ἱλάσθητί μοι τῷ ἁμαρτωλῷ", "sei versöhnt mit mir, dem Sünder", ["sei mir, dem Sünder, gnädig"], "ἱλάσκομαι gehört zum Wortfeld von Sühne und Versöhnung. Der Artikel («dem Sünder») stellt den Zöllner gegen die «übrigen Menschen» des Pharisäers ([[LUK.18.11]])."),
 ("LUK.18.14", "gerechtfertigt", "literal", "δεδικαιωμένος", None, ["von Gott als gerecht angenommen"], "Perfekt Passiv: Gott ist der Handelnde."),
 ("LUK.18.14", "und nicht jener", "interpretive", "παρʼ ἐκεῖνον", "im Vergleich zu jenem", ["mehr als jener"], "παρά mit Akkusativ vergleicht. Meist wird es ausschliessend verstanden: der eine gerechtfertigt, der andere nicht. Siehe auch die Alternative."),
 ("LUK.18.15", "die kleinen Kinder", "literal", "τὰ βρέφη", None, ["die Säuglinge"], "βρέφος ist ein Säugling oder Kleinkind; in [[LUK.18.16]] und [[LUK.18.17]] steht παιδίον «Kind»."),
 ("LUK.18.15", "wiesen sie die Leute zurecht", "adapted", "ἐπετίμων αὐτοῖς", "fuhren sie sie an", None, "αὐτοῖς meint die Leute, die die Kinder bringen; zur Klarheit ergänzt."),
 ("LUK.18.18", "ein führender Mann", "interpretive", "ἄρχων", None, ["ein Vorsteher", "ein Oberster", "ein Ratsherr"], "ἄρχων bezeichnet jemanden in leitender Stellung, etwa in einer Synagoge oder einem Rat. Welches Amt gemeint ist, sagt Lukas nicht."),
 ("LUK.18.18", "was muss ich tun", "adapted", "τί ποιήσας", "was getan habend", None, "Partizip Aorist; im Deutschen als Hauptsatz."),
 ("LUK.18.19", "ausser Gott allein", "adapted", "εἰ μὴ εἷς ὁ θεός", "ausser einer, Gott", ["ausser dem einen Gott"], "εἷς «einer» kann auf das Bekenntnis zum einen Gott anspielen ([[DEU.6.4]])."),
 ("LUK.18.20", "Du sollst nicht", "traditional", "Μὴ μοιχεύσῃς", "Brich nicht die Ehe", None, "μή mit Konjunktiv Aorist ist ein Verbot. Wiedergegeben in der vertrauten Form der Zehn Gebote (vgl. [[EXO.20.12]]–[[EXO.20.16]]); Lukas nennt sie in eigener Reihenfolge."),
 ("LUK.18.22", "im Himmel", "adapted", "ἐν οὐρανοῖς", "in den Himmeln", None, "Die Mehrzahl entspricht hebräisch šāmayim; im Deutschen Einzahl."),
 ("LUK.18.25", "ein Nadelöhr", "literal", "τρήματος βελόνης", "das Loch einer Nadel", None, "Ein absichtlich unmögliches Bild. Spätere Erklärungen (ein enges Stadttor, ein Tau statt eines Kamels) sind nicht belegt."),
 ("LUK.18.28", "alles, was uns gehörte", "adapted", "τὰ ἴδια", "das Eigene", ["unser Zuhause", "unseren Besitz"], "τὰ ἴδια kann Besitz oder Zuhause meinen (vgl. [[JHN.19.27]]). Zur Lesart «wir haben alles verlassen» siehe die Alternative."),
 ("LUK.18.30", "Weltzeit", "literal", "αἰῶνι", None, ["Welt", "Zeitalter"], "αἰών ist eine Weltzeit; «die kommende Weltzeit» steht der jetzigen Zeit gegenüber. Ebenso [[LUK.20.34]] und [[LUK.20.35]]."),
 ("LUK.18.31", "am Menschensohn vollendet werden", "interpretive", "τῷ υἱῷ τοῦ ἀνθρώπου", None, ["was über den Menschensohn geschrieben ist"], "Der Dativ kann zu «vollendet werden» gehören («am Menschensohn») oder zu «geschrieben» («über den Menschensohn»)."),
 ("LUK.18.32", "den Heiden", "traditional", "τοῖς ἔθνεσιν", None, ["den Völkern", "den Nichtjuden"], "ἔθνη sind im jüdischen Sprachgebrauch die Nichtjuden. Gemeint sind hier die Römer."),
 ("LUK.18.32", "ausgeliefert", "literal", "παραδοθήσεται", None, ["übergeben"], "παραδίδωμι ist wie bei Markus durchgehend «ausliefern» (auch [[LUK.20.20]], [[LUK.21.12]], [[LUK.21.16]])."),
 ("LUK.18.35", "Es geschah aber", "literal", "Ἐγένετο δὲ", None, None, EGEN_DE),
 ("LUK.18.37", "Jesus von Nazaret", "adapted", "Ἰησοῦς ὁ Ναζωραῖος", "Jesus, der Nazoräer", ["Jesus, der Nazarener"], "Ναζωραῖος wird meist als Herkunftsbezeichnung verstanden; die Herleitung des Wortes ist umstritten."),
 ("LUK.18.38", "Sohn Davids", "literal", "υἱὲ Δαυίδ", None, None, "Anrede an den erwarteten König aus Davids Nachkommenschaft (vgl. [[2SA.7.12]]–[[2SA.7.16]]). Siehe auch [[LUK.20.41]]–[[LUK.20.44]]."),
 ("LUK.18.42", "gerettet", "literal", "σέσωκέν", None, ["geheilt"], "σῴζω heisst «retten» und «heilen»; beides schwingt mit."),
 ("LUK.18.43", "pries Gott", "literal", "δοξάζων τὸν θεόν", "Gott verherrlichend", None, None),
 # Kapitel 19
 ("LUK.19.2", "Oberzöllner", "literal", "ἀρχιτελώνης", None, ["Zollvorsteher"], "Das Wort ist sonst nicht belegt. Gemeint ist wohl jemand, der andere Zöllner unter sich hatte; Jericho lag an einer Handelsstrasse."),
 ("LUK.19.3", "er versuchte", "adapted", "ἐζήτει", "er suchte", None, "Imperfekt: ein andauernder, erfolgloser Versuch."),
 ("LUK.19.3", "er war klein von Gestalt", "literal", "τῇ ἡλικίᾳ μικρὸς ἦν", None, None, "ἡλικία kann auch «Lebensalter» heissen; hier ist die Körpergrösse gemeint. Gemeint ist Zachäus."),
 ("LUK.19.4", "einen Maulbeerfeigenbaum", "literal", "συκομορέαν", None, ["eine Sykomore"], "Die Sykomore ist ein Feigenbaum mit kurzem Stamm und weit ausladenden Ästen, leicht zu besteigen."),
 ("LUK.19.7", "um dort Gast zu sein", "adapted", "καταλῦσαι", "um Herberge zu nehmen", ["um zu übernachten"], None),
 ("LUK.19.8", "gebe ich", "interpretive", "δίδωμι", None, ["will ich geben", "gebe ich (schon bisher)"], "Präsens: Es kann einen Entschluss ausdrücken («ab jetzt») oder eine Gewohnheit, mit der Zachäus sich gegen das Murren verteidigt. Meist wird es als Entschluss gelesen. Ebenso «gebe ich … zurück»."),
 ("LUK.19.8", "erpresst habe", "interpretive", "ἐσυκοφάντησα", None, ["betrogen habe", "durch falsche Anzeige abgenommen habe"], "συκοφαντέω heisst «durch falsche Anschuldigung oder Druck etwas abnehmen»."),
 ("LUK.19.8", "vierfach", "literal", "τετραπλοῦν", None, None, "Das Gesetz verlangte für ein gestohlenes Schaf vierfachen Ersatz ([[EXO.22.1]]); sonst genügte meist der Betrag mit einem Fünftel Zuschlag ([[NUM.5.7]])."),
 ("LUK.19.9", "Rettung", "interpretive", "σωτηρία", None, ["Heil"], "σωτηρία ist Rettung, Heil im umfassenden Sinn. Vgl. «retten» in [[LUK.19.10]]."),
 ("LUK.19.11", "erzählte er noch", "adapted", "προσθεὶς εἶπεν", "fügte hinzu und sagte", None, None),
 ("LUK.19.12", "die Königswürde", "interpretive", "βασιλείαν", "ein Königtum", ["die Königsherrschaft"], "Ein Herrscher, der in ein fernes Land reist, um die Königswürde zu erhalten, erinnert an die Fürsten der Herodesfamilie, die sich ihre Herrschaft in Rom bestätigen lassen mussten. Ob Lukas daran denkt, ist eine Deutung."),
 ("LUK.19.13", "Knechte", "traditional", "δούλους", "Sklaven", ["Diener"], None),
 ("LUK.19.13", "Minen", "literal", "μνᾶς", None, None, "Eine Mine war eine Rechnungseinheit von hundert Drachmen, etwa hundert Tageslöhnen."),
 ("LUK.19.13", "bis ich komme", "interpretive", "ἐν ᾧ ἔρχομαι", "während ich komme", None, "ἐν ᾧ heisst wörtlich «während»; gemeint ist die Zeit bis zur Rückkehr. RP liest ἕως «bis»."),
 ("LUK.19.17", "Gut gemacht", "adapted", "Εὖγε", "Wohlan", ["Recht so", "Sehr gut"], None),
 ("LUK.19.20", "einem Tuch", "literal", "σουδαρίῳ", "einem Schweisstuch", None, None),
 ("LUK.19.21", "ein strenger", "literal", "αὐστηρὸς", None, ["ein harter"], None),
 ("LUK.19.22", "Nach deinen eigenen Worten", "adapted", "Ἐκ τοῦ στόματός σου", "Aus deinem Mund", None, None),
 ("LUK.19.23", "auf die Bank", "adapted", "ἐπὶ τράπεζαν", "auf den Tisch", ["zu den Geldwechslern"], "τράπεζα ist der Tisch der Geldwechsler und Geldverleiher."),
 ("LUK.19.27", "macht sie vor meinen Augen nieder", "literal", "κατασφάξατε αὐτοὺς ἔμπροσθέν μου", None, ["tötet sie vor mir"], "Das Gleichnis zeichnet einen antiken König mit harter Strafe für die, die ihn ablehnten. Wie weit das Bild auf Gott zu übertragen ist, wird verschieden beurteilt."),
 ("LUK.19.29", "Ölberg", "literal", "Ἐλαιῶν", "Berg der Ölbäume", None, "Lukas sagt «der Berg, der ‹der Ölbäume› genannt wird»."),
 ("LUK.19.30", "ein Fohlen", "interpretive", "πῶλον", None, ["einen jungen Esel"], "πῶλος ist ein junges Tier; meist ist ein Esel gemeint (vgl. [[ZEC.9.9]]). Lukas nennt die Tierart nicht."),
 ("LUK.19.33", "Besitzer", "adapted", "οἱ κύριοι αὐτοῦ", "seine Herren", None, "Wortspiel: Die «Herren» des Fohlens hören, dass «der Herr» es braucht ([[LUK.19.31]], [[LUK.19.34]])."),
 ("LUK.19.37", "Machttaten", "interpretive", "δυνάμεων", "Kräfte", ["Wunder", "Krafttaten"], "δύναμις ist Kraft und die Tat, in der sie sich zeigt; so auch bei Markus."),
 ("LUK.19.38", "Gesegnet sei der König, der kommt im Namen des Herrn", "literal", "Εὐλογημένος ὁ ἐρχόμενος βασιλεὺς ἐν ὀνόματι κυρίου", None, None, "Nach [[PSA.118.26]], erweitert um «der König». Das «sei» ist ergänzt."),
 ("LUK.19.38", "Ehre", "interpretive", "δόξα", None, ["Herrlichkeit"], "Erinnert an den Lobgesang der Engel in [[LUK.2.14]]."),
 ("LUK.19.42", "was zum Frieden dient", "literal", "τὰ πρὸς εἰρήνην", None, None, "Der Satz bricht ab («wenn doch …»). Ob ein Wortspiel mit dem Namen Jerusalem (šālôm «Friede») beabsichtigt ist, ist eine Vermutung."),
 ("LUK.19.43", "einen Wall", "literal", "χάρακά", None, ["einen Belagerungswall", "eine Palisade"], None),
 ("LUK.19.44", "deiner Heimsuchung", "traditional", "τῆς ἐπισκοπῆς σου", None, ["in der Gott dich besucht hat"], "ἐπισκοπή ist der Besuch Gottes, hier zum Heil (vgl. [[LUK.1.68]], [[LUK.1.78]]), nicht die Strafe. «Heimsuchung» hatte früher diesen Sinn."),
 ("LUK.19.46", "zu einer Räuberhöhle", "literal", "σπήλαιον λῃστῶν", None, None, "Zitate aus [[ISA.56.7]] und [[JER.7.11]]."),
 ("LUK.19.47", "die Führenden des Volkes", "literal", "οἱ πρῶτοι τοῦ λαοῦ", "die Ersten des Volkes", None, None),
 ("LUK.19.48", "hing an seinen Lippen", "adapted", "ἐξεκρέματο αὐτοῦ ἀκούων", "hing an ihm, indem es zuhörte", None, "Deutsche Redewendung für das griechische Bild."),
 # Kapitel 20
 ("LUK.20.1", "das Evangelium verkündigte", "literal", "εὐαγγελιζομένου", None, ["die gute Nachricht verkündete"], None),
 ("LUK.20.2", "Vollmacht", "literal", "ἐξουσίᾳ", None, ["Befugnis", "Recht"], None),
 ("LUK.20.3", "etwas", "adapted", "λόγον", "ein Wort", ["eine Sache"], None),
 ("LUK.20.10", "zur rechten Zeit", "literal", "καιρῷ", "zur Zeit", None, "Gemeint ist die Zeit der Ernte."),
 ("LUK.20.10", "Weinbauern", "literal", "γεωργοὺς", None, ["Pächter"], None),
 ("LUK.20.11", "Und er sandte noch einen anderen Knecht", "adapted", "καὶ προσέθετο ἕτερον πέμψαι δοῦλον", "Und er fügte hinzu, einen anderen Knecht zu senden", None, "Semitisch geprägte Wendung; ebenso [[LUK.20.12]]."),
 ("LUK.20.13", "geliebten", "literal", "ἀγαπητόν", None, None, "Wie die Himmelsstimme bei der Taufe ([[LUK.3.22]])."),
 ("LUK.20.16", "Das darf nicht geschehen", "adapted", "Μὴ γένοιτο", "Es möge nicht geschehen", ["Auf keinen Fall", "Das sei ferne"], None),
 ("LUK.20.17", "Eckstein", "interpretive", "κεφαλὴν γωνίας", "Haupt der Ecke", ["Schlussstein"], "Zitat aus [[PSA.118.22]]. Gemeint ist der tragende Stein an der Ecke oder der Schlussstein."),
 ("LUK.20.18", "zermalmen", "interpretive", "λικμήσει", "worfeln", ["zerstreuen wie Spreu"], "λικμάω heisst «worfeln» (das Korn von der Spreu trennen) und übertragen «zerreiben, zermalmen». Anklang an [[DAN.2.34]]–[[DAN.2.35]] und [[ISA.8.14]]."),
 ("LUK.20.20", "Spitzel", "literal", "ἐγκαθέτους", None, ["Agenten"], None),
 ("LUK.20.20", "Statthalters", "literal", "ἡγεμόνος", None, None, "Gemeint ist der römische Statthalter (Pilatus)."),
 ("LUK.20.21", "auf das Ansehen der Person siehst", "literal", "λαμβάνεις πρόσωπον", "das Gesicht nimmst", ["parteiisch bist"], "Semitische Wendung für Parteilichkeit."),
 ("LUK.20.22", "Steuer", "interpretive", "φόρον", None, ["Tribut"], "Die direkte Abgabe an Rom, die das Land als unterworfenes Gebiet kennzeichnete."),
 ("LUK.20.25", "Dann gebt dem Kaiser zurück", "literal", "Τοίνυν ἀπόδοτε", None, ["Gebt also dem Kaiser"], "ἀποδίδωμι heisst «zurückgeben, abgeben, was man schuldet»."),
 ("LUK.20.27", "Sadduzäer", "literal", "Σαδδουκαίων", None, None, "Eine Gruppe der priesterlichen Oberschicht; sie lehnte die Auferstehung ab (vgl. [[ACT.23.8]])."),
 ("LUK.20.28", "Nachkommen erwecken", "literal", "ἐξαναστήσῃ σπέρμα", None, ["Nachkommen verschaffen"], "Nach dem Gesetz der Schwagerehe ([[DEU.25.5]]–[[DEU.25.6]])."),
 ("LUK.20.30", "Und der zweite,", "literal", "καὶ ὁ δεύτερος", None, None, "Der SBLGNT-Text ist hier sehr knapp; zu ergänzen ist «nahm sie» aus [[LUK.20.31]]. Zum längeren Wortlaut siehe die Alternative."),
 ("LUK.20.34", "Die Menschen dieser Weltzeit", "adapted", "Οἱ υἱοὶ τοῦ αἰῶνος τούτου", "Die Söhne dieser Weltzeit", None, "Semitisch geprägte Wendung für Menschen, die zu dieser Weltzeit gehören."),
 ("LUK.20.36", "den Engeln gleich", "literal", "ἰσάγγελοι", None, None, None),
 ("LUK.20.36", "Söhne", "literal", "υἱοί", None, ["Kinder"], "«Söhne Gottes» und «Söhne der Auferstehung» sind semitisch geprägte Wendungen: Sie gehören zu Gott und zur Auferstehung."),
 ("LUK.20.37", "beim Dornbusch", "adapted", "ἐπὶ τῆς βάτου", "beim Dornbusch (-Abschnitt)", None, "Bibelstellen wurden nach Stichworten angeführt; gemeint ist [[EXO.3.6]]."),
 ("LUK.20.38", "für ihn leben alle", "literal", "αὐτῷ ζῶσιν", None, ["in seinen Augen leben alle"], None),
 ("LUK.20.41", "der Christus", "traditional", "τὸν χριστὸν", None, ["der Messias", "der Gesalbte"], "χριστός übersetzt hebräisch māšîaḥ «Gesalbter»."),
 ("LUK.20.42", "Buch der Psalmen", "literal", "βίβλῳ ψαλμῶν", None, None, "Zitat aus [[PSA.110.1]]."),
 ("LUK.20.46", "in langen Gewändern", "adapted", "ἐν στολαῖς", "in Gewändern", None, "στολή ist ein langes, vornehmes Gewand."),
 ("LUK.20.47", "die Häuser der Witwen auffressen", "literal", "κατεσθίουσιν τὰς οἰκίας τῶν χηρῶν", None, None, "Ein Bild dafür, Schutzlose um ihren Besitz zu bringen. Wie das geschah, ist nicht bekannt."),
 # Kapitel 21
 ("LUK.21.1", "den Opferkasten", "literal", "γαζοφυλάκιον", None, ["die Schatzkammer"], "Im Tempel standen Behälter für Gaben."),
 ("LUK.21.2", "Lepta", "literal", "λεπτὰ", None, None, "Das Lepton war die kleinste Münze."),
 ("LUK.21.3", "Wahrhaftig", "literal", "Ἀληθῶς", None, ["In Wahrheit"], None),
 ("LUK.21.4", "Lebensunterhalt", "literal", "βίον", None, ["alles, was sie zum Leben hatte"], None),
 ("LUK.21.5", "Weihegaben", "literal", "ἀναθήμασιν", None, ["Weihegeschenken"], None),
 ("LUK.21.8", "bin es", "interpretive", "εἰμι", "bin", ["bin der Christus"], "Ἐγώ εἰμι kann heissen «Ich bin es (der Erwartete)». Ob ein Anklang an die Selbstvorstellung Gottes ([[EXO.3.14]]) mitschwingt, ist umstritten."),
 ("LUK.21.9", "Unruhen", "literal", "ἀκαταστασίας", None, ["Aufstände", "Umstürze"], None),
 ("LUK.21.11", "Hungersnöte und Seuchen", "literal", "λιμοὶ καὶ λοιμοὶ", None, None, "Im Griechischen ein Wortspiel (limoi kai loimoi)."),
 ("LUK.21.11", "Schreckliches", "literal", "φόβητρά", None, ["Schreckbilder", "Schrecknisse"], None),
 ("LUK.21.13", "Das wird für euch zum Zeugnis führen", "interpretive", "ἀποβήσεται ὑμῖν εἰς μαρτύριον", None, ["Das wird euch Gelegenheit geben, Zeugnis abzulegen", "Das wird für euch zum Zeugnis (vor Gott) werden"], "Gemeint sein kann die Gelegenheit, vor Königen und Statthaltern Zeugnis abzulegen, oder ein Zeugnis zugunsten der Verfolgten."),
 ("LUK.21.14", "Nehmt euch also zu Herzen", "adapted", "θέτε οὖν ἐν ταῖς καρδίαις ὑμῶν", "Legt also in eure Herzen", None, None),
 ("LUK.21.14", "wie ihr euch verteidigen sollt", "literal", "ἀπολογηθῆναι", "euch zu verteidigen", None, "ἀπολογέομαι ist das Wort für die Verteidigung vor Gericht."),
 ("LUK.21.15", "die rechten Worte", "adapted", "στόμα", "Mund", ["Beredsamkeit"], "«Mund» steht für die Gabe zu reden."),
 ("LUK.21.18", "Und kein Haar von eurem Kopf wird verloren gehen", "literal", "καὶ θρὶξ ἐκ τῆς κεφαλῆς ὑμῶν οὐ μὴ ἀπόληται", None, None, "Steht neben [[LUK.21.16]] («einige von euch wird man töten»). Meist wird es so verstanden, dass die Verfolgten bei Gott letztlich bewahrt sind, nicht dass ihnen nichts geschieht."),
 ("LUK.21.19", "Leben", "interpretive", "ψυχὰς", "Seelen", None, "ψυχή ist das Leben, das ganze Selbst."),
 ("LUK.21.19", "gewinnt", "literal", "κτήσασθε", None, ["bewahrt"], "Aufforderung (Imperativ Aorist). Zur Lesart mit Futur siehe die Alternative."),
 ("LUK.21.20", "Heeren", "literal", "στρατοπέδων", None, ["Heerlagern"], None),
 ("LUK.21.21", "in der Stadt", "interpretive", "ἐν μέσῳ αὐτῆς", "in ihrer Mitte", None, "αὐτῆς «ihrer» bezieht sich wohl auf Jerusalem ([[LUK.21.20]]); grammatisch ist auch Judäa möglich."),
 ("LUK.21.22", "der Vergeltung", "interpretive", "ἐκδικήσεως", None, ["der Strafe", "des Strafgerichts"], "Dasselbe Wortfeld wie das «Recht verschaffen» in [[LUK.18.3]]–[[LUK.18.8]]."),
 ("LUK.21.23", "Land", "interpretive", "γῆς", None, ["Erde"], "γῆ kann das Land (Judäa) oder die ganze Erde meinen; hier wohl das Land, wegen «dieses Volk»."),
 ("LUK.21.24", "durch die Schärfe des Schwertes", "literal", "στόματι μαχαίρης", "durch den Mund des Schwertes", None, "Hebräisch geprägte Wendung."),
 ("LUK.21.24", "die Zeiten der Völker", "interpretive", "καιροὶ ἐθνῶν", None, ["die Zeiten der Heiden"], "Die Bedeutung ist umstritten: die Zeit, in der Völker über Jerusalem herrschen, oder die Zeit, in der die Völker die Botschaft hören."),
 ("LUK.21.25", "der Wogen", "literal", "σάλου", None, ["der Brandung"], None),
 ("LUK.21.26", "vergehen", "interpretive", "ἀποψυχόντων", None, ["werden ohnmächtig", "verlieren den Atem"], None),
 ("LUK.21.26", "die Welt", "literal", "τῇ οἰκουμένῃ", "die bewohnte Erde", None, None),
 ("LUK.21.27", "in einer Wolke", "literal", "ἐν νεφέλῃ", None, None, "Anklang an [[DAN.7.13]]."),
 ("LUK.21.28", "Erlösung", "literal", "ἀπολύτρωσις", None, ["Befreiung"], "Eigentlich der Loskauf eines Gefangenen, dann allgemein Befreiung."),
 ("LUK.21.32", "Dieses Geschlecht", "traditional", "ἡ γενεὰ αὕτη", "diese Generation", ["Diese Generation", "Dieses Volk"], "γενεά meint meist die Menschen einer Zeit. Worauf sich «alles» bezieht und wie weit γενεά zu fassen ist, wird verschieden beantwortet; «Geschlecht» hält die Mehrdeutigkeit offen (wie bei [[MRK.13.30]])."),
 ("LUK.21.34", "Rausch", "literal", "κραιπάλῃ", None, ["Völlerei", "Katerstimmung"], None),
 ("LUK.21.36", "stark genug seid", "literal", "κατισχύσητε", None, ["die Kraft habt"], "Zur Lesart «für würdig gehalten werdet» siehe die Alternative."),
 ("LUK.21.37", "übernachtete", "literal", "ηὐλίζετο", None, ["verbrachte die Nacht im Freien"], None),
]

DEC_GSW = [
 ('LUK.21.2', 'Lepta', 'literal', 'λεπτὰ', None, None, 'S Lepton (Mehrzahl «Lepta») isch di chliinscht Chupfermünz gsii, en halbe Quadrans ([[MRK.12.42]]); zwei Lepta sind en Bruchteil vomene Taglohn. Damalige Münzname im Text, de Wärt i de Erkläärig (Entscheid Andi Neck 2026-10-26).'),
 ('LUK.20.24', 'Denar', 'literal', 'δηνάριον', None, None, 'Römischi Silbermünz mit Bild und Ufschrift vom Kaiser, öppe de üblich Taglohn vomene Arbeiter ([[MAT.20.2]]). Damalige Münzname im Text, de Wärt i de Erkläärig (Entscheid Andi Neck 2026-10-26).'),
 ('LUK.19.23', 'Silber', 'literal', 'τὸ ἀργύριον', None, ['Gäld'], 'Wie [[LUK.19.15]]. ἀργύριον einheitlich: Einzahl «Silber», Mehrzahl ἀργύρια «Silberstück» ([[MAT.26.15]]). Damalige Münzname im Text, de Wärt i de Erkläärig (Entscheid Andi Neck 2026-10-26).'),
 ('LUK.19.15', 's Silber', 'literal', 'τὸ ἀργύριον', None, ['s Gäld'], 'Gmeint sind d Mine ([[LUK.19.13]]), es Gwicht Silber vo hundert Drachme, öppe hundert Taglöhn. ἀργύριον einheitlich: Einzahl «Silber», Mehrzahl ἀργύρια «Silberstück» ([[MAT.26.15]]). Damalige Münzname im Text, de Wärt i de Erkläärig (Entscheid Andi Neck 2026-10-26).'),
 ("LUK.18.3", "Verschaff mir Rächt", "literal", "Ἐκδίκησόν με", None, None, "ἐκδικέω isch es Wort us em Rächt: öpperem zu sim Rächt verhälfe, nöd «räche»."),
 ("LUK.18.5", "fertig macht", "interpretive", "ὑπωπιάζῃ", "under d Auge schlaat", ["is Gsicht schlaat", "blossstellt"], "S Wort chunnt us em Fuschtkampf («es blaus Aug schlaa»); übertreit «fertig mache» oder «blamiere»."),
 ("LUK.18.6", "ungrächt Richter", "adapted", "ὁ κριτὴς τῆς ἀδικίας", "Richter vo de Ungrächtigkeit", None, None),
 ("LUK.18.7", "laat er si warte", "interpretive", "μακροθυμεῖ ἐπʼ αὐτοῖς", "isch er langmüetig mit ine", ["hät er Gedult mit ine"], "Bezug und Sinn vom Satz sind umstritte."),
 ("LUK.18.8", "de Mänschesohn", "traditional", "ὁ υἱὸς τοῦ ἀνθρώπου", "de Sohn vom Mänsch", ["de Mänsch"], "«Sohn vo me Mänsch» heisst hebräisch und aramäisch eifach «Mänsch»; bim Jesus e Bezeichnig für sich sälber, mit Aaklang a [[DAN.7.13]]."),
 ("LUK.18.8", "ächt", "adapted", "ἆρα", "wohl", None, "Fragepartikel; i de Mundart «ächt»."),
 ("LUK.18.11", "bi sich", "interpretive", "πρὸς ἑαυτὸν", None, ["für sich elei", "zu sich sälber"], "πρὸς ἑαυτόν cha zu «hät sich häregstellt» oder zu «hät bättet» ghöre."),
 ("LUK.18.13", "bis mir Sünder gnädig", "interpretive", "ἱλάσθητί μοι τῷ ἁμαρτωλῷ", "bis versöhnt mit mir, em Sünder", None, None),
 ("LUK.18.14", "und nöd säbe", "interpretive", "παρʼ ἐκεῖνον", "im Vergliich zu säbem", ["meh als säbe"], None),
 ("LUK.18.15", "d Lüüt", "adapted", "αὐτοῖς", "si", None, "Gmeint sind d Lüüt, wo d Chind bringed; ergänzt."),
 ("LUK.18.18", "füerende Maa", "interpretive", "ἄρχων", None, ["Vorsteher", "Ratsherr"], "Welles Amt gmeint isch, seit de Lukas nöd."),
 ("LUK.18.19", "usser Gott elei", "adapted", "εἰ μὴ εἷς ὁ θεός", "usser eine, Gott", None, None),
 ("LUK.18.28", "alles, wo üs ghört hät", "adapted", "τὰ ἴδια", "s Eigete", ["üses Dihei"], None),
 ("LUK.18.32", "de Heide", "traditional", "τοῖς ἔθνεσιν", None, ["de Völker"], "ἔθνη sind im jüdische Sprachgebruuch d Nichtjude; da sind d Römer gmeint."),
 ("LUK.18.35", "Es isch aber gsii", "literal", "Ἐγένετο δὲ", None, None, EGEN_GSW),
 ("LUK.18.37", "vo Nazaret", "adapted", "ὁ Ναζωραῖος", "de Nazoräer", None, None),
 ("LUK.18.42", "Du söllsch wider gseh", "adapted", "Ἀνάβλεψον", "Lueg wider", None, "D Mundart hät für «wider gseh» kei natürliche Befehlsform."),
 ("LUK.18.43", "d Ehr ggää", "adapted", "δοξάζων", "verherrlichend", ["prise"], None),
 ("LUK.19.7", "gmotzt", "adapted", "διεγόγγυζον", "gmurret", ["gmuulet"], None),
 ("LUK.19.8", "gib ich", "interpretive", "δίδωμι", None, ["wott ich gää"], "Präsens: e Entschluss («ab jetzt») oder e Gwohnet; meischt als Entschluss gläse."),
 ("LUK.19.9", "Rettig", "interpretive", "σωτηρία", None, ["Heil"], None),
 ("LUK.19.13", "Chnächt", "traditional", "δούλους", "Sklave", ["Diener"], None),
 ("LUK.19.13", "Mine", "literal", "μνᾶς", None, None, "E Mine isch e Rächnigsiiheit vo hundert Drachme gsii, öppe hundert Taglöhn."),
 ("LUK.19.33", "Bsitzer", "adapted", "οἱ κύριοι αὐτοῦ", "Herre", None, "Wortspiel: D «Herre» vom Füli ghöred, dass «de Herr» es bruucht."),
 ("LUK.19.37", "di mächtige Tate", "interpretive", "δυνάμεων", "Chräft", ["Wunder"], None),
 ("LUK.19.44", "Heimsuechig", "traditional", "ἐπισκοπῆς", None, ["Bsuech vo Gott"], "ἐπισκοπή isch de Bsuech vo Gott, da zum Heil, nöd d Straf."),
 ("LUK.19.48", "a sine Lippe", "adapted", "ἐξεκρέματο αὐτοῦ ἀκούων", "a ihm ghanget und zueglost", None, None),
 ("LUK.20.16", "Das dörf nöd passiere", "adapted", "Μὴ γένοιτο", "Es söll nöd gscheh", ["Uf kein Fall"], None),
 ("LUK.20.17", "Eckstei", "interpretive", "κεφαλὴν γωνίας", "Chopf vo de Egge", ["Schlussstei"], "Zitat us [[PSA.118.22]]."),
 ("LUK.20.21", "uf s Aaseh vo de Person luegsch", "literal", "λαμβάνεις πρόσωπον", "s Gsicht nimmsch", None, "Semitischi Wändig für parteiisch sii."),
 ("LUK.20.25", "gänd em Kaiser zrugg", "literal", "ἀπόδοτε", None, None, "ἀποδίδωμι heisst «zruggää, abgää, was mer schuldig isch»."),
 ("LUK.20.34", "D Mänsche vo dere Wältziit", "adapted", "Οἱ υἱοὶ τοῦ αἰῶνος τούτου", "D Söhn vo dere Wältziit", None, None),
 ("LUK.21.8", "bi s", "interpretive", "εἰμι", "bi", ["bi de Christus"], "Ἐγώ εἰμι cha heisse «ich bi s (de Erwartet)»."),
 ("LUK.21.11", "Hungersnöt und Süüche", "literal", "λιμοὶ καὶ λοιμοὶ", None, None, "Im Griechische es Wortspiel (limoi kai loimoi)."),
 ("LUK.21.14", "Nämed eu also z Härze", "adapted", "θέτε οὖν ἐν ταῖς καρδίαις ὑμῶν", "Legged also i eui Härz", None, None),
 ("LUK.21.15", "di richtige Wort", "adapted", "στόμα", "Muul", None, "«Muul» staat für d Gab, z rede."),
 ("LUK.21.19", "Läbe", "interpretive", "ψυχὰς", "Seele", None, None),
 ("LUK.21.19", "Durehebe", "adapted", "ὑπομονῇ", "Uusdur", ["Standhaftigkeit"], None),
 ("LUK.21.21", "i de Stadt", "interpretive", "ἐν μέσῳ αὐτῆς", "i irere Mitti", None, "Gmeint isch wohl Jerusalem ([[LUK.21.20]]); grammatisch chönt au Judäa gmeint sii."),
 ("LUK.21.22", "Strafgricht", "interpretive", "ἐκδικήσεως", "Vergältig", None, None),
 ("LUK.21.24", "d Ziite vo de Völker", "interpretive", "καιροὶ ἐθνῶν", None, ["d Ziite vo de Heide"], "D Bedüütig isch umstritte."),
 ("LUK.21.32", "Die Generation", "interpretive", "ἡ γενεὰ αὕτη", None, ["Das Volk"], "γενεά meint meischt d Mänsche vo ere Ziit; «Gschlächt» seit mer i de Mundart für d Mänsche vo ere Ziit chuum (es meint dört d Abstammig, vgl. [[LUK.2.4]]); drum «Generation» wie bi [[MRK.13.30]]. D hochdüütschi Fassig hät «Geschlecht»."),
 ("LUK.21.36", "d Chraft händ", "literal", "κατισχύσητε", None, None, "Zur Läsart «für würdig aagluegt wärded» lueg d Alternative."),
]

AUTO = "Laut der automatischen Zuordnung"
AUTO_G = "Nach de automatische Zueornig"
# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung,
#  WREAD-CNTR-LUK-0NN-…) bzw. aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-LUK-018-014-01:R2", "LUK.18.14", "und nicht jener", "eher als jener", "und nöd säbe", "ehner als säbe", "gering",
  "Eine andere Vergleichsform; der Sinn bleibt im Wesentlichen gleich.", "En anderi Vergliichsform; de Sinn bliibt im Wäsentliche gliich.",
  {"R1": [("παρʼ ἐκεῖνον", "im Vergleich zu jenem", None)], "R2": [("ἢ γὰρ ἐκεῖνος", "eher als jener", "RP")]},
  {"R1": [("παρʼ ἐκεῖνον", "im Vergliich zu säbem", None)], "R2": [("ἢ γὰρ ἐκεῖνος", "ehner als säbe", "RP")]},
  ["Die ungewöhnliche Wendung παρʼ ἐκεῖνον kann durch eine geläufigere ersetzt worden sein.",
   AUTO + " lesen 01, 03 und 𝔓75 R1, 02 R2; 032 hat ἢ ἐκεῖνος ohne γάρ, 05 μᾶλλον παρʼ ἐκεῖνον τὸν Φαρισαῖον («mehr als jener Pharisäer»)."],
  ["Di ungwöhnlich Wändig παρʼ ἐκεῖνον cha dur e gläufigeri ersetzt worde sii.",
   AUTO_G + " läsed 01, 03 und 𝔓75 R1, 02 R2; 032 hät ἢ ἐκεῖνος ohni γάρ, 05 «meh als säbe Pharisäer»."]),
 ("VAR-SBLGNTAPP-LUK-018-024-01:R2", "LUK.18.24", "Jesus aber sah ihn an und sagte", "Als Jesus aber sah, dass er sehr traurig geworden war, sagte er",
  "De Jesus aber hät en aagluegt und gseit", "Wo de Jesus aber gseh hät, dass er ganz truurig worde isch, hät er gseit", "gering",
  "Mit dem Zusatz nimmt Jesus ausdrücklich die Traurigkeit des Mannes wahr ([[LUK.18.23]]).", "Mit em Zuesatz gseht de Jesus usdrücklich, dass de Maa truurig isch ([[LUK.18.23]]).",
  {"R1": [("Ἰησοῦς", "Jesus", "WH, SBLGNT")], "R2": [("Ἰησοῦς περίλυπον γενόμενον", "Jesus … ihn, der sehr traurig geworden war", "Treg, RP, NA28")]},
  {"R1": [("Ἰησοῦς", "de Jesus", "WH, SBLGNT")], "R2": [("Ἰησοῦς περίλυπον γενόμενον", "de Jesus … en, wo ganz truurig worde isch", "Treg, RP, NA28")]},
  ["Der Zusatz kann aus [[LUK.18.23]] (περίλυπος «sehr traurig») aufgenommen sein, um den Anlass des Wortes zu nennen; er kann auch ursprünglich und wegen der Wiederholung ausgelassen worden sein.",
   AUTO + " lesen 02 und 032 mit dem Zusatz, 05 ebenfalls, aber in anderer Wortstellung. 01 und 03 haben ihn im erfassten Wortlaut nicht; die Zuordnung führt sie unter «andere Form». 𝔓75 ist hier nicht erhalten."],
  ["De Zuesatz cha us [[LUK.18.23]] übernoo sii; er cha au ursprünglich sii und wäge de Widerholig wäggloo worde sii.",
   AUTO_G + " läsed 02 und 032 mit Zuesatz, 05 au, aber i anderer Wortstellig; 01 und 03 händ en im erfasste Wortlut nöd."]),
 ("VAR-SBLGNTAPP-LUK-018-028-02:R2", "LUK.18.28", "haben alles, was uns gehörte, verlassen", "haben alles verlassen",
  "händ alles, wo üs ghört hät, verlaa", "händ alles verlaa", "gering",
  "«Wir haben alles verlassen und sind dir gefolgt» statt «das Unsere verlassend sind wir dir gefolgt».", "«Mir händ alles verlaa und sind dir nachegfolget» statt «s Eigete verlaa».",
  {"R1": [("ἀφέντες τὰ ἴδια", "das Unsere verlassend", None)], "R2": [("ἀφήκαμεν πάντα καὶ", "wir haben alles verlassen und", "RP")]},
  {"R1": [("ἀφέντες τὰ ἴδια", "s Eigete verlaa", None)], "R2": [("ἀφήκαμεν πάντα καὶ", "mir händ alles verlaa und", "RP")]},
  ["R2 entspricht dem Wortlaut bei Markus und Matthäus ([[MRK.10.28]], [[MAT.19.27]]); Abschreiber haben Paralleltexte oft angeglichen. τὰ ἴδια ist eine Wendung, die Lukas auch sonst verwendet ([[ACT.4.32]]).",
   AUTO + " liest 03 R1; 01, 02 und 032 lesen R2; 05 hat τὰ ἴδια ἀφέντες (R1 in anderer Wortstellung); 𝔓75 ist hier nicht erhalten."],
  ["R2 entspricht em Wortlut bim Markus und bim Matthäus ([[MRK.10.28]], [[MAT.19.27]]); Abschriiber händ Paralleltext oft aaglichen.",
   AUTO_G + " lisst 03 R1; 01, 02 und 032 läsed R2; 05 hät R1 i anderer Wortstellig."]),
 ("VAR-SBLGNTAPP-LUK-019-042-02:R2", "LUK.19.42", "was zum Frieden dient", "was zu deinem Frieden dient", "was zum Fride füert", "was zu dim Fride füert", "gering",
  "Mit «deinem» wird die Anrede an die Stadt verstärkt.", "Mit «dim» wird d Aared a d Stadt verstärkt.",
  {"R1": [("εἰρήνην", "Frieden", None)], "R2": [("εἰρήνην σου", "deinem Frieden", "Treg, RP")]},
  {"R1": [("εἰρήνην", "Fride", None)], "R2": [("εἰρήνην σου", "dim Fride", "Treg, RP")]},
  ["Das Fürwort kann verdeutlichend ergänzt worden sein.",
   AUTO + " lesen 01 und 03 ohne «dein», 032 mit σου, 05 mit σοι («für dich»); in 02 ist σου in der Erstschrift unsicher lesbar und in der Korrektur vorhanden; 04 lässt sich hier keiner Lesart zuordnen."],
  ["S Fürwort cha zur Verdüütlichig ergänzt worde sii.",
   AUTO_G + " läsed 01 und 03 ohni «dim», 032 und 02 (Korrektur) mit σου, 05 mit σοι."]),
 ("VAR-SBLGNTAPP-LUK-019-045-01:R2", "LUK.19.45", "die Händler hinauszutreiben", "die Händler darin und die Käufer hinauszutreiben",
  "d Händler usezjage", "d Händler drin und d Chäufer usezjage", "gering",
  "Mit dem Zusatz treibt Jesus auch die Käufer hinaus.", "Mit em Zuesatz jagt de Jesus au d Chäufer use.",
  {"R1": [("πωλοῦντας", "Händler", None)], "R2": [("πωλοῦντας ἐν αὐτῷ καὶ ἀγοράζοντας", "Händler darin und Käufer", "RP")]},
  {"R1": [("πωλοῦντας", "Händler", None)], "R2": [("πωλοῦντας ἐν αὐτῷ καὶ ἀγοράζοντας", "Händler drin und Chäufer", "RP")]},
  ["Der Zusatz entspricht [[MRK.11.15]] und [[MAT.21.12]] und kann von dort übernommen sein.",
   AUTO + " lesen 01 und 03 ohne Zusatz, 02, 032 und 05 mit ihm; 04 hat καὶ τοὺς ἀγοράζοντας ohne ἐν αὐτῷ."],
  ["De Zuesatz entspricht [[MRK.11.15]] und [[MAT.21.12]] und cha vo dört übernoo sii.",
   AUTO_G + " läsed 01 und 03 ohni Zuesatz, 02, 032, 04 und 05 mit."]),
 ("VAR-SBLGNTAPP-LUK-019-046-01:R2", "LUK.19.46", "Mein Haus wird ein Haus des Gebets sein", "Mein Haus ist ein Haus des Gebets",
  "Mis Huus wird es Huus zum Bätte sii", "Mis Huus isch es Huus zum Bätte", "gering",
  "Ohne καὶ ἔσται («und … wird sein»); RP hat stattdessen am Ende des Zitats ἐστίν «ist» (VAR-SBLGNTAPP-LUK-019-046-02).",
  "Ohni καὶ ἔσται («und … wird sii»); RP hät defür am Änd vom Zitat ἐστίν «isch».",
  {"R1": [("Καὶ ἔσται", "Und … wird sein", None)], "R2": [("–", "(fehlt)", "RP, mit ἐστίν «ist»")]},
  {"R1": [("Καὶ ἔσται", "Und … wird sii", None)], "R2": [("–", "(fäält)", "RP, mit ἐστίν «isch»")]},
  ["Die knappe Einleitung καὶ ἔσται ist ungewöhnlich; sie kann geglättet worden sein. Umgekehrt kann sie ergänzt worden sein. Bei Markus und Matthäus heisst es «wird … genannt werden» ([[MRK.11.17]], [[MAT.21.13]]).",
   AUTO + " hat nur 03 καὶ ἔσται; 02, 032, 04 und 05 lesen ὅτι und am Ende ἐστίν («ist»); 01 hat weder καὶ ἔσται noch ἐστίν."],
  ["Di knapp Iileitig καὶ ἔσται isch ungwöhnlich; si cha glättet oder ergänzt worde sii.",
   AUTO_G + " hät nu 03 καὶ ἔσται; 02, 032, 04 und 05 händ ὅτι und am Änd ἐστίν; 01 hät weder s eint no s ander."]),
 ("VAR-SBLGNTAPP-LUK-020-023-01:R2", "LUK.20.23", "und sagte zu ihnen:", "und sagte zu ihnen: «Warum stellt ihr mich auf die Probe?",
  "und hät zu ine gseit:", "und hät zu ine gseit: «Werum stelled ir mi uf d Prob?", "gering",
  "Mit dem Zusatz spricht Jesus die Absicht der Fragenden offen aus.", "Mit em Zuesatz seit de Jesus offe, was d Frager wänd.",
  {"R1": [("αὐτούς", "(ohne Frage)", None)], "R2": [("αὐτούς· Τί με πειράζετε", "Warum stellt ihr mich auf die Probe?", "RP")]},
  {"R1": [("αὐτούς", "(ohni Frag)", None)], "R2": [("αὐτούς· Τί με πειράζετε", "Werum stelled ir mi uf d Prob?", "RP")]},
  ["Die Frage steht in [[MRK.12.15]] und [[MAT.22.18]] und kann von dort übernommen sein.",
   AUTO + " lesen 01 und 03 ohne die Frage, 02, 032, 04 und 05 mit ihr; 04 und 05 haben ausserdem πονηρίαν («Bosheit») statt πανουργίαν («Verschlagenheit»)."],
  ["D Frag staat i [[MRK.12.15]] und [[MAT.22.18]] und cha vo dört übernoo sii.",
   AUTO_G + " läsed 01 und 03 ohni Frag, 02, 032, 04 und 05 mit."]),
 ("VAR-SBLGNTAPP-LUK-020-030-01:R2", "LUK.20.30", "Und der zweite,", "Und der zweite nahm die Frau, und auch er starb kinderlos.",
  "Und de zweit,", "Und de zweit hät d Frau gnoo, und au dä isch ohni Chind gstorbe.", "gering",
  "Der längere Text erzählt den Schritt ausdrücklich.", "De länger Text verzellt de Schritt usdrücklich.",
  {"R1": [("ὁ δεύτερος", "der zweite", None)], "R2": [("ἔλαβεν ὁ δεύτερος τὴν γυναῖκα καὶ οὗτος ἀπέθανεν ἄτεκνος", "der zweite nahm die Frau, und dieser starb kinderlos", "RP")]},
  {"R1": [("ὁ δεύτερος", "de zweit", None)], "R2": [("ἔλαβεν ὁ δεύτερος τὴν γυναῖκα καὶ οὗτος ἀπέθανεν ἄτεκνος", "de zweit hät d Frau gnoo, und dä isch ohni Chind gstorbe", "RP")]},
  ["Der knappe Text kann ergänzt worden sein, damit der Satz vollständig ist; die Ergänzung wiederholt [[LUK.20.29]].",
   AUTO + " lesen 01, 03 und 05 den kurzen Text, 02 und 032 den längeren; 04 ist hier nicht erhalten."],
  ["De knapp Text cha ergänzt worde sii; d Ergänzig widerholt [[LUK.20.29]].",
   AUTO_G + " läsed 01, 03 und 05 de churz Text, 02 und 032 de länger."]),
 ("VAR-SBLGNTAPP-LUK-021-019-01:R2", "LUK.21.19", "gewinnt euer Leben!", "werdet ihr euer Leben gewinnen.", "gwünned eues Läbe!", "wärded ir eues Läbe gwünne.", "mittel",
  "Aufforderung oder Zusage: «gewinnt» (Imperativ) oder «ihr werdet gewinnen» (Futur).", "Ufforderig oder Zuesag: «gwünned!» oder «ir wärded gwünne».",
  {"R1": [("κτήσασθε", "gewinnt", "Imperativ; NA28, RP")], "R2": [("κτήσεσθε", "ihr werdet gewinnen", "Futur; WH, Treg")]},
  {"R1": [("κτήσασθε", "gwünned", "Befehlsform; NA28, RP")], "R2": [("κτήσεσθε", "ir wärded gwünne", "Zuekunft; WH, Treg")]},
  ["Die beiden Formen unterscheiden sich in einem Buchstaben und wurden gleich oder fast gleich ausgesprochen; beim Abschreiben lag eine Verwechslung nahe.",
   AUTO + " lesen 05 κτήσασθε und 01 und 032 κτησασθαι (wegen der gleich klingenden Endung der Aufforderung zugeordnet), 03 κτήσεσθε und 02 κτησεσθαι (Futur); 04 ist hier nicht erhalten."],
  ["Di beide Forme underscheided sich i eim Buechstabe und sind gliich oder fascht gliich uusgsproche worde.",
   AUTO_G + " läsed 01, 032 und 05 d Befehlsform (01 und 032 i ere gliich klingende Schriibig), 02 und 03 d Zuekunft."]),
 ("VAR-SBLGNTAPP-LUK-021-036-02:R2", "LUK.21.36", "damit ihr stark genug seid", "damit ihr für würdig gehalten werdet", "demit ir d Chraft händ", "demit ir für würdig aagluegt wärded", "mittel",
  "Statt um die Kraft zum Entkommen geht es um die Würdigkeit.", "Statt um d Chraft zum Entcho gaat s um d Würdigkeit.",
  {"R1": [("κατισχύσητε", "ihr stark genug seid", None)], "R2": [("καταξιωθῆτε", "ihr für würdig gehalten werdet", "RP")]},
  {"R1": [("κατισχύσητε", "ir d Chraft händ", None)], "R2": [("καταξιωθῆτε", "ir für würdig aagluegt wärded", "RP")]},
  ["καταξιόω steht auch in [[LUK.20.35]]; die Lesart kann davon beeinflusst sein. Umgekehrt kann das seltenere κατισχύω ersetzt worden sein.",
   AUTO + " lesen 01, 03 und 032 κατισχύσητε (in unterschiedlicher Schreibung), 02, 04 und 05 καταξιωθῆτε."],
  ["καταξιόω staat au i [[LUK.20.35]]; d Läsart cha devo beiiflusst sii.",
   AUTO_G + " läsed 01, 03 und 032 κατισχύσητε, 02, 04 und 05 καταξιωθῆτε."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-LUK-018-001-043", "LUK.18.1-LUK.18.43", "section", "Vom Beten, vom Reichtum und der Weg nach Jericho",
  ["TU-LUK-018-001-008", "TU-LUK-018-009-014", "TU-LUK-018-015-017", "TU-LUK-018-018-030", "TU-LUK-018-031-034", "TU-LUK-018-035-043"],
  "Mit zwei Gleichnissen lehrt Jesus beharrlich und demütig beten: Eine Witwe setzt sich gegen einen ungerechten Richter durch, und ein Zöllner, nicht ein selbstgerechter Pharisäer, geht gerechtfertigt nach Hause. Jesus nimmt die Kinder an. Einem reichen Mann rät er, alles zu verkaufen und ihm zu folgen; Reichen falle der Weg ins Reich Gottes schwer, doch bei Gott sei möglich, was bei Menschen unmöglich ist. Er kündigt den Zwölf sein Leiden und seine Auferstehung an, sie verstehen es nicht. Bei Jericho heilt er einen Blinden, der ihn als Sohn Davids anruft.", SEG),
 ("TU-LUK-018-001-008", "LUK.18.1-LUK.18.8", "parable", "Die Witwe und der Richter", None,
  "Eine Witwe bittet einen Richter, der weder Gott fürchtet noch auf Menschen Rücksicht nimmt, immer wieder um ihr Recht. Er gibt nach, damit sie ihn nicht weiter zermürbt. Jesus folgert: Gott wird seinen Auserwählten, die zu ihm schreien, erst recht und schnell Recht verschaffen. Doch wird der Menschensohn bei seinem Kommen Glauben finden?", None),
 ("TU-LUK-018-009-014", "LUK.18.9-LUK.18.14", "parable", "Der Pharisäer und der Zöllner", None,
  "Jesus erzählt das Gleichnis Leuten, die sich für gerecht halten und andere verachten. Ein Pharisäer dankt Gott, dass er nicht ist wie die anderen, und zählt seine Frömmigkeit auf. Ein Zöllner steht abseits und bittet nur: «Gott, sei mir Sünder gnädig!» Dieser geht gerechtfertigt nach Hause, nicht jener; denn wer sich erhöht, wird erniedrigt, und wer sich erniedrigt, wird erhöht.", None),
 ("TU-LUK-018-015-017", "LUK.18.15-LUK.18.17", "narrative_with_saying", "Jesus und die Kinder", None,
  "Man bringt kleine Kinder zu Jesus; die Jünger weisen die Leute zurecht. Jesus ruft die Kinder zu sich: Solchen gehört das Reich Gottes, und wer es nicht annimmt wie ein Kind, kommt nicht hinein.", None),
 ("TU-LUK-018-018-030", "LUK.18.18-LUK.18.30", "dialogue", "Der reiche Mann und der Lohn der Nachfolge", None,
  "Ein führender Mann fragt, was er tun müsse, um ewiges Leben zu erben. Er sagt, er habe die Gebote von Jugend an gehalten; Jesus sagt ihm, er solle alles verkaufen, den Armen geben und ihm folgen. Der Mann wird traurig, denn er ist sehr reich. Jesus sagt, wie schwer Reiche ins Reich Gottes kommen; bei Gott aber ist möglich, was Menschen unmöglich ist. Wer um des Reiches Gottes willen verlassen hat, was ihm gehörte, empfängt jetzt ein Vielfaches und in der kommenden Weltzeit ewiges Leben.", None),
 ("TU-LUK-018-031-034", "LUK.18.31-LUK.18.34", "narrative_with_saying", "Ankündigung von Leiden und Auferstehung", None,
  "Auf dem Weg nach Jerusalem kündigt Jesus den Zwölf an, dass sich am Menschensohn erfüllen wird, was die Propheten geschrieben haben: Er wird den Heiden ausgeliefert, verspottet, misshandelt und getötet werden und am dritten Tag auferstehen. Die Jünger verstehen nichts davon; das Wort bleibt ihnen verborgen.", None),
 ("TU-LUK-018-035-043", "LUK.18.35-LUK.18.43", "narrative", "Der Blinde bei Jericho", None,
  "Ein blinder Bettler am Weg bei Jericho ruft Jesus als Sohn Davids um Erbarmen an und lässt sich nicht zum Schweigen bringen. Jesus fragt, was er für ihn tun soll, und sagt: «Sieh wieder! Dein Glaube hat dich gerettet.» Der Mann sieht wieder, folgt Jesus und preist Gott, und das ganze Volk lobt Gott.", None),
 ("TU-LUK-019-001-048", "LUK.19.1-LUK.19.48", "section", "Zachäus, das Gleichnis von den Minen und der Einzug in Jerusalem",
  ["TU-LUK-019-001-010", "TU-LUK-019-011-027", "TU-LUK-019-028-040", "TU-LUK-019-041-044", "TU-LUK-019-045-048"],
  "In Jericho kehrt Jesus beim Oberzöllner Zachäus ein, der die Hälfte seines Besitzes den Armen geben und Erpresstes vierfach erstatten will; der Menschensohn ist gekommen, das Verlorene zu suchen und zu retten. Im Gleichnis von den Minen fordert ein König, der seine Herrschaft antritt, Rechenschaft von seinen Knechten und straft seine Gegner. Jesus zieht auf einem Fohlen nach Jerusalem, die Jünger rufen ihn als kommenden König aus. Er weint über die Stadt, die nicht erkannt hat, was zum Frieden dient, treibt die Händler aus dem Tempel und lehrt dort täglich, während die Führenden ihn umbringen wollen.", SEG),
 ("TU-LUK-019-001-010", "LUK.19.1-LUK.19.10", "narrative", "Zachäus", None,
  "Zachäus, ein reicher Oberzöllner, steigt auf einen Baum, um Jesus zu sehen. Jesus ruft ihn herunter und kehrt bei ihm ein; alle murren, weil er Gast bei einem Sünder ist. Zachäus sagt, er gebe die Hälfte seines Besitzes den Armen und erstatte Erpresstes vierfach. Jesus sagt: Heute ist diesem Haus Rettung widerfahren, denn der Menschensohn ist gekommen, zu suchen und zu retten, was verloren ist.", None),
 ("TU-LUK-019-011-027", "LUK.19.11-LUK.19.27", "parable", "Das Gleichnis von den anvertrauten Minen", None,
  "Weil man meint, das Reich Gottes erscheine sofort, erzählt Jesus ein Gleichnis: Ein vornehmer Mann reist fort, um die Königswürde zu erlangen, und gibt zehn Knechten je eine Mine, um damit zu wirtschaften; seine Mitbürger wollen ihn nicht als König. Zurückgekehrt belohnt er die Knechte, die gewonnen haben, mit Macht über Städte. Dem Knecht, der die Mine aus Angst verwahrt hat, nimmt er sie weg: Wer hat, dem wird gegeben, wer nicht hat, dem wird auch das genommen. Seine Feinde lässt er töten.", None),
 ("TU-LUK-019-028-040", "LUK.19.28-LUK.19.40", "narrative", "Der Einzug in Jerusalem", None,
  "Bei Betfage und Betanien schickt Jesus zwei Jünger, ein Fohlen zu holen, auf dem noch niemand gesessen hat; es geschieht, wie er gesagt hat: «Der Herr braucht es.» Jesus reitet hinab zur Stadt, die Leute breiten ihre Mäntel aus, und die Schar der Jünger lobt Gott: «Gesegnet sei der König, der kommt im Namen des Herrn!» Pharisäern, die das verbieten wollen, antwortet Jesus: Wenn diese schweigen, werden die Steine schreien.", None),
 ("TU-LUK-019-041-044", "LUK.19.41-LUK.19.44", "narrative_with_saying", "Jesus weint über Jerusalem", None,
  "Beim Anblick der Stadt weint Jesus: Jerusalem hat nicht erkannt, was zum Frieden dient. Er kündigt an, dass Feinde die Stadt belagern und dem Erdboden gleichmachen werden, weil sie die Zeit nicht erkannt hat, in der Gott sie besucht hat.", None),
 ("TU-LUK-019-045-048", "LUK.19.45-LUK.19.48", "narrative", "Im Tempel", None,
  "Jesus treibt die Händler aus dem Tempel: Gottes Haus soll ein Haus des Gebets sein, sie aber haben eine Räuberhöhle daraus gemacht. Er lehrt täglich im Tempel. Hohepriester, Schriftgelehrte und Führende des Volkes wollen ihn umbringen, finden aber keinen Weg, denn das ganze Volk hängt an seinen Lippen.", None),
 ("TU-LUK-020-001-047", "LUK.20.1-LUK.20.47", "section", "Streitgespräche im Tempel",
  ["TU-LUK-020-001-008", "TU-LUK-020-009-019", "TU-LUK-020-020-026", "TU-LUK-020-027-040", "TU-LUK-020-041-044", "TU-LUK-020-045-047"],
  "Im Tempel stellen die Führenden Jesus zur Rede. Auf die Frage nach seiner Vollmacht antwortet er mit einer Gegenfrage nach der Taufe des Johannes. Im Gleichnis von den Weinbauern, die die Knechte und den geliebten Sohn des Besitzers misshandeln und töten, erkennen sie sich selbst. Die Fangfrage nach der Steuer beantwortet er so, dass sie schweigen: Gebt dem Kaiser, was des Kaisers ist, und Gott, was Gottes ist. Den Sadduzäern zeigt er, dass die Toten auferstehen, weil Gott ein Gott der Lebenden ist. Er fragt, wie der Christus Davids Sohn sein kann, wenn David ihn Herr nennt, und warnt vor geltungssüchtigen Schriftgelehrten.", SEG),
 ("TU-LUK-020-001-008", "LUK.20.1-LUK.20.8", "dialogue", "Die Frage nach der Vollmacht", None,
  "Hohepriester, Schriftgelehrte und Älteste fragen Jesus, mit welcher Vollmacht er handelt. Er fragt zurück, ob die Taufe des Johannes vom Himmel oder von Menschen war. Weil ihnen beide Antworten schaden würden, sagen sie, sie wüssten es nicht; da sagt auch Jesus ihnen nicht, mit welcher Vollmacht er handelt.", None),
 ("TU-LUK-020-009-019", "LUK.20.9-LUK.20.19", "parable", "Das Gleichnis von den Weinbauern", None,
  "Ein Mensch verpachtet seinen Weinberg. Die Weinbauern schicken drei Knechte, die den Ertrag holen sollen, geschlagen fort; den geliebten Sohn werfen sie hinaus und töten ihn, um das Erbe zu bekommen. Der Herr wird sie umbringen und den Weinberg anderen geben. Jesus fügt das Schriftwort vom verworfenen Stein an, der zum Eckstein geworden ist. Die Schriftgelehrten und Hohepriester merken, dass er das Gleichnis im Blick auf sie erzählt hat, fürchten aber das Volk.", None),
 ("TU-LUK-020-020-026", "LUK.20.20-LUK.20.26", "dialogue", "Die Steuer für den Kaiser", None,
  "Spitzel fragen Jesus, ob es erlaubt sei, dem Kaiser Steuer zu zahlen, um ihn dem Statthalter ausliefern zu können. Er lässt sich einen Denar zeigen, der Bild und Aufschrift des Kaisers trägt, und sagt: «Gebt dem Kaiser zurück, was des Kaisers ist, und Gott, was Gottes ist!» Sie staunen über seine Antwort und schweigen.", None),
 ("TU-LUK-020-027-040", "LUK.20.27-LUK.20.40", "dialogue", "Die Frage nach der Auferstehung", None,
  "Sadduzäer, die die Auferstehung bestreiten, fragen nach einer Frau, die nacheinander sieben Brüder geheiratet hat: Wem gehört sie in der Auferstehung? Jesus antwortet: Die zur kommenden Weltzeit gehören, heiraten nicht mehr und können nicht mehr sterben; sie sind den Engeln gleich und Söhne Gottes. Dass die Toten auferweckt werden, zeigt schon Mose am Dornbusch, wo er den Herrn den Gott Abrahams, Isaaks und Jakobs nennt; Gott ist ein Gott der Lebenden. Einige Schriftgelehrte loben die Antwort; danach wagt niemand mehr, ihn zu fragen.", None),
 ("TU-LUK-020-041-044", "LUK.20.41-LUK.20.44", "discourse", "Davids Sohn und Herr", None,
  "Jesus fragt, wie man sagen kann, der Christus sei Davids Sohn, wenn David ihn im Psalm ([[PSA.110.1]]) seinen Herrn nennt.", None),
 ("TU-LUK-020-045-047", "LUK.20.45-LUK.20.47", "discourse", "Warnung vor den Schriftgelehrten", None,
  "Vor dem ganzen Volk warnt Jesus seine Jünger vor Schriftgelehrten, die Ansehen und Ehrenplätze suchen, Witwen um ihre Häuser bringen und zum Schein lange beten. Sie werden ein umso härteres Urteil empfangen.", None),
 ("TU-LUK-021-001-038", "LUK.21.1-LUK.21.38", "section", "Die Gabe der Witwe und die Rede über die kommende Zeit",
  ["TU-LUK-021-001-004", "TU-LUK-021-005-019", "TU-LUK-021-020-024", "TU-LUK-021-025-028", "TU-LUK-021-029-033", "TU-LUK-021-034-038"],
  "Eine arme Witwe gibt mit zwei kleinen Münzen mehr als alle Reichen, denn sie gibt alles, was sie zum Leben hat. Als einige den Tempel bewundern, kündigt Jesus an, dass kein Stein auf dem anderen bleiben wird. Er warnt vor Verführern, sagt Kriege, Erdbeben, Hungersnöte und Verfolgungen an und verheisst den Verfolgten Worte und Weisheit; durch Standhaftigkeit gewinnen sie ihr Leben. Jerusalem wird belagert und zertreten werden. Dann werden Zeichen am Himmel geschehen und der Menschensohn wird in einer Wolke kommen; die Seinen sollen aufsehen, denn ihre Erlösung naht. Jesus mahnt zur Wachsamkeit und lehrt täglich im Tempel.", SEG + " Die Rede über die Zukunft ([[LUK.21.5]]–[[LUK.21.36]]) ist hier in fünf Teile gegliedert; die Einteilung ist besonders bei [[LUK.21.20]]–[[LUK.21.28]] umstritten."),
 ("TU-LUK-021-001-004", "LUK.21.1-LUK.21.4", "narrative_with_saying", "Die Gabe der Witwe", None,
  "Jesus sieht Reiche ihre Gaben in den Opferkasten werfen und eine arme Witwe zwei Lepta. Er sagt: Sie hat mehr eingeworfen als alle; die anderen gaben von ihrem Überfluss, sie aus ihrem Mangel ihren ganzen Lebensunterhalt.", None),
 ("TU-LUK-021-005-019", "LUK.21.5-LUK.21.19", "discourse", "Das Ende des Tempels, Verführung und Verfolgung", None,
  "Jesus kündigt an, dass vom prächtigen Tempel kein Stein auf dem anderen bleiben wird. Auf die Frage nach dem Wann und dem Zeichen warnt er vor Verführern, die in seinem Namen auftreten, und vor Angst bei Kriegen: Das Ende kommt nicht sofort. Völker und Reiche werden sich erheben, Erdbeben, Hungersnöte, Seuchen und Zeichen am Himmel kommen. Vorher aber werden die Jünger verfolgt, ausgeliefert und vor Könige gestellt; Jesus selbst wird ihnen die rechten Worte und Weisheit geben. Sie werden gehasst, einige getötet, doch kein Haar geht verloren; durch Standhaftigkeit gewinnen sie ihr Leben.", None),
 ("TU-LUK-021-020-024", "LUK.21.20-LUK.21.24", "discourse", "Die Verwüstung Jerusalems", None,
  "Wenn Heere Jerusalem umzingeln, ist seine Verwüstung nahe: Wer in Judäa ist, soll in die Berge fliehen. Es sind Tage der Vergeltung, grosse Not kommt über das Land und Zorn über das Volk; viele fallen oder werden verschleppt, und Jerusalem wird von den Völkern zertreten, bis die Zeiten der Völker erfüllt sind.", None),
 ("TU-LUK-021-025-028", "LUK.21.25-LUK.21.28", "discourse", "Das Kommen des Menschensohns", None,
  "Zeichen an Sonne, Mond und Sternen und das Tosen des Meeres versetzen die Völker in Angst; die Mächte des Himmels werden erschüttert. Dann sieht man den Menschensohn in einer Wolke mit Macht und grosser Herrlichkeit kommen. Wenn das beginnt, sollen die Jünger sich aufrichten, denn ihre Erlösung naht.", None),
 ("TU-LUK-021-029-033", "LUK.21.29-LUK.21.33", "parable", "Das Gleichnis vom Feigenbaum", None,
  "Wie die ausschlagenden Bäume den Sommer ankündigen, so zeigen diese Ereignisse, dass das Reich Gottes nahe ist. Dieses Geschlecht wird nicht vergehen, bis alles geschieht; Himmel und Erde vergehen, Jesu Worte aber nicht.", None),
 ("TU-LUK-021-034-038", "LUK.21.34-LUK.21.38", "discourse", "Aufruf zur Wachsamkeit", None,
  "Jesus mahnt, die Herzen nicht durch Rausch und Alltagssorgen beschweren zu lassen, damit jener Tag nicht wie eine Falle über sie kommt; sie sollen wach bleiben und beten, um vor dem Menschensohn zu bestehen. Tagsüber lehrt Jesus im Tempel, die Nächte verbringt er am Ölberg, und das ganze Volk kommt früh am Morgen, um ihn zu hören.", None),
]
UNITS_GSW = {
 "TU-LUK-018-001-043": ("Vom Bätte, vom Riichtum und de Wäg uf Jericho", "Mit zwei Gliichnis lehrt de Jesus, wie mer drahebt und demüetig bättet: E Witwe setzt sich gäge en ungrächte Richter dure, und en Zöllner, nöd en sälbschtgrächte Pharisäer, gaat grächtfertiget hei. De Jesus nimmt d Chind aa. Eme riiche Maa rätet er, alles z verchaufe und ihm nachezfolge; Riichi chömed schwär is Riich vo Gott, aber bi Gott isch möglich, was bi Mänsche unmöglich isch. Er seit de Zwölf sis Liide und sini Uferstehig aa, si verstönd s nöd. Bi Jericho heilt er en Blinde, wo en als Sohn vom David aarüeft."),
 "TU-LUK-018-001-008": ("D Witwe und de Richter", "E Witwe bittet en Richter, wo weder Gott fürchtet no uf Mänsche Rücksicht nimmt, immer wider um ires Rächt. Er git naa, demit si en nöd wiiter fertig macht. De Jesus folgeret: Gott wird sine Userwählte, wo zu ihm schreied, erscht rächt und schnell Rächt verschaffe. Aber wird de Mänschesohn, wänn er chunnt, Glaube finde?"),
 "TU-LUK-018-009-014": ("De Pharisäer und de Zöllner", "De Jesus verzellt s Gliichnis Lüüt, wo sich für grächt halted und anderi verachted. En Pharisäer dankt Gott, dass er nöd isch wie di andere, und zellt sini Frömmigkeit uf. En Zöllner staat wiit wäg und bittet nu: «Gott, bis mir Sünder gnädig!» Dä gaat grächtfertiget hei, nöd säbe; dänn wer sich sälber erhöcht, wird erniedriget, und wer sich sälber erniedriget, wird erhöcht."),
 "TU-LUK-018-015-017": ("De Jesus und d Chind", "Mer bringt chliini Chind zum Jesus; d Jünger fahred d Lüüt aa. De Jesus rüeft d Chind zu sich: Settige ghört s Riich vo Gott, und wer s nöd aanimmt wie es Chind, chunnt nöd ine."),
 "TU-LUK-018-018-030": ("De riich Maa und de Lohn vo de Nachfolg", "En füerende Maa fröget, was er mües mache, demit er ewigs Läbe erbt. Er seit, er heig d Gebot vo Jugend aa ghalte; de Jesus seit em, er söll alles verchaufe, de Arme gää und ihm nachefolge. De Maa wird truurig, dänn er isch sehr riich. De Jesus seit, wie schwär Riichi is Riich vo Gott chömed; bi Gott aber isch möglich, was für Mänsche unmöglich isch. Wer wäge em Riich vo Gott verlaa hät, was em ghört hät, überchunnt jetzt vilfach zrugg und i de chömende Wältziit ewigs Läbe."),
 "TU-LUK-018-031-034": ("Aasag vo Liide und Uferstehig", "Uf em Wäg uf Jerusalem seit de Jesus de Zwölf, dass am Mänschesohn erfüllt wird, was d Prophete gschribe händ: Er wird de Heide usgliferet, verspottet, misshandlet und umbracht und am dritte Tag uferstaa. D Jünger verstönd nüüt devo; s Wort bliibt ine verborge."),
 "TU-LUK-018-035-043": ("De Blind bi Jericho", "En blinde Bettler am Wäg bi Jericho rüeft de Jesus als Sohn vom David um Erbarme aa und laat sich nöd zum Schwiige bringe. De Jesus fröget, was er für en söll mache, und seit: «Du söllsch wider gseh! Din Glaube hät dich grettet.» De Maa gseht wider, folgt em Jesus und git Gott d Ehr, und s ganz Volk lobt Gott."),
 "TU-LUK-019-001-048": ("De Zachäus, s Gliichnis vo de Mine und de Iizug in Jerusalem", "Z Jericho chehrt de Jesus bim Oberzöllner Zachäus ii; dä wott d Hälfti vo sim Vermöge de Arme gää und Abprässts vierfach zruggzale. De Mänschesohn isch choo, zum sueche und rette, was verlore isch. Im Gliichnis vo de Mine verlangt en König, wo sini Herrschaft aatrittet, vo sine Chnächt Rächeschaft und straft sini Gägner. De Jesus zieht uf eme Füli uf Jerusalem, d Jünger rüefed en als König uus, wo chunnt. Er briegget über d Stadt, wo nöd erchännt hät, was zum Fride füert, jagt d Händler us em Tämpel und lehrt dört jede Tag, während d Füerende en wänd umbringe."),
 "TU-LUK-019-001-010": ("De Zachäus", "De Zachäus, en riiche Oberzöllner, chlätteret uf en Baum, zum de Jesus gseh. De Jesus rüeft en abe und chehrt bi ihm ii; alli motzed, wil er bi me Sünder z Gascht isch. De Zachäus seit, er gäb d Hälfti vo sim Vermöge de Arme und zali Abprässts vierfach zrugg. De Jesus seit: Hüt isch Rettig zu dem Huus choo, dänn de Mänschesohn isch choo, zum sueche und rette, was verlore isch."),
 "TU-LUK-019-011-027": ("S Gliichnis vo de aavertraute Mine", "Wil mer meint, s Riich vo Gott chömi grad, verzellt de Jesus es Gliichnis: En vornähme Maa reist furt, zum d Königswürde z hole, und git zää Chnächt je e Mine, zum demit z gschäfte; sini Mitbürger wänd en nöd als König. Wo er zrugg isch, belohnt er d Chnächt, wo öppis gwunne händ, mit Macht über Städt. Em Chnächt, wo d Mine us Angscht versteckt hät, nimmt er si wäg: Wer hät, däm wird ggää, wer nüüt hät, däm wird au das gnoo. Sini Find laat er umbringe."),
 "TU-LUK-019-028-040": ("De Iizug in Jerusalem", "Bi Betfage und Betanie schickt de Jesus zwei Jünger, es Füli z hole, wo no nie öpper druf gsässe isch; es gaat, wie er gseit hät: «De Herr bruucht s.» De Jesus riitet abe gäge d Stadt, d Lüüt breited iri Mäntel uus, und d Schar vo de Jünger lobt Gott: «Gsägnet sig de König, wo chunnt im Name vom Herr!» Pharisäer wänd s verbiete; de Jesus antwortet: Wänn die schwiiged, schreied d Stei."),
 "TU-LUK-019-041-044": ("De Jesus briegget über Jerusalem", "Wo de Jesus d Stadt gseht, briegget er: Jerusalem hät nöd erchännt, was zum Fride füert. Er seit aa, dass Find d Stadt belageret und em Bode gliichmached, wil si d Ziit nöd erchännt hät, wo Gott si bsuecht hät."),
 "TU-LUK-019-045-048": ("Im Tämpel", "De Jesus jagt d Händler us em Tämpel: Gottes Huus söll es Huus zum Bätte sii, si aber händ e Röiberhöli drus gmacht. Er lehrt jede Tag im Tämpel. Hoheprieschter, Schriftgleerti und Füerendi vom Volk wänd en umbringe, finded aber kei Wäg, dänn s ganz Volk hanget a sine Lippe."),
 "TU-LUK-020-001-047": ("Striitgspräch im Tämpel", "Im Tämpel stelled d Füerende de Jesus zur Red. Uf d Frag nach sinere Vollmacht antwortet er mit ere Gägefrag nach de Taufi vom Johannes. Im Gliichnis vo de Wiibuure, wo d Chnächt und de gliebt Sohn vom Bsitzer misshandled und umbringed, erchänned si sich sälber. D Fangfrag nach de Stüür beantwortet er eso, dass si schwiiged: Gänd em Kaiser, was em Kaiser ghört, und Gott, was Gott ghört. De Sadduzäer zeigt er, dass d Tote uferstönd, wil Gott en Gott vo de Läbige isch. Er fröget, wie de Christus de Sohn vom David chönn sii, wänn de David en Herr nännt, und warnt vor Schriftgleerte, wo Ehr sueched."),
 "TU-LUK-020-001-008": ("D Frag nach de Vollmacht", "Hoheprieschter, Schriftgleerti und Ältischti fröged de Jesus, mit was für ere Vollmacht er handlet. Er fröget zrugg, öb d Taufi vom Johannes vom Himmel oder vo Mänsche gsii sig. Wil ine beidi Antworte schade würded, säged si, si wüssed s nöd; dänn seit ine au de Jesus nöd, mit was für ere Vollmacht er handlet."),
 "TU-LUK-020-009-019": ("S Gliichnis vo de Wiibuure", "En Mänsch verpachtet sin Wiibärg. D Wiibuure schicked drei Chnächt, wo de Ertrag sötted hole, verprüglet furt; de gliebt Sohn wärfed si use und bringed en um, zum s Erb übercho. De Herr wird si umbringe und de Wiibärg andere gää. De Jesus hänkt s Schriftwort vom verworfene Stei aa, wo zum Eckstei worde isch. D Schriftgleerte und d Hoheprieschter merked, dass er s Gliichnis gäge si verzellt hät, händ aber Angscht vor em Volk."),
 "TU-LUK-020-020-026": ("D Stüür für de Kaiser", "Spitzel fröged de Jesus, öb s erlaubt sig, em Kaiser Stüür z zale, demit si en em Statthalter chönted uslifere. Er laat sich en Denar zeige mit em Bild und de Ufschrift vom Kaiser und seit: «Gänd em Kaiser zrugg, was em Kaiser ghört, und Gott, was Gott ghört!» Si stuuned über sini Antwort und schwiiged."),
 "TU-LUK-020-027-040": ("D Frag nach de Uferstehig", "Sadduzäer, wo d Uferstehig bestriited, fröged nach ere Frau, wo nachenand sibe Brüeder ghürate hät: Wem ghört si i de Uferstehig? De Jesus antwortet: Die, wo zur chömende Wältziit ghöred, hürated nüme und chönd nüme stärbe; si sind wie d Ängel und Söhn vo Gott. Dass d Tote uferweckt wärded, zeigt scho de Mose bim Dornbusch, won er de Herr de Gott vom Abraham, vom Isaak und vom Jakob nännt; Gott isch en Gott vo de Läbige. Es paar Schriftgleerti lobed d Antwort; dänach traut sich niemer meh, en z fröge."),
 "TU-LUK-020-041-044": ("De Sohn und Herr vom David", "De Jesus fröget, wie mer cha säge, de Christus sig de Sohn vom David, wänn de David en im Psalm ([[PSA.110.1]]) sin Herr nännt."),
 "TU-LUK-020-045-047": ("Warnig vor de Schriftgleerte", "Vor em ganze Volk warnt de Jesus sini Jünger vor Schriftgleerte, wo Aaseh und Ehreplätz sueched, Witwe um iri Hüüser bringed und zum Schii lang bätted. Si wärded es umso härters Urteil übercho."),
 "TU-LUK-021-001-038": ("D Gab vo de Witwe und d Red über di chömend Ziit", "E armi Witwe git mit zwei chliine Münze meh als alli Riiche, dänn si git alles, was si zum Läbe hät. Wo es paar de Tämpel bewunderet, seit de Jesus aa, dass kei Stei uf em andere bliibt. Er warnt vor Verfüerer, seit Chrieg, Ärdbebe, Hungersnöt und Verfolgige aa und verspricht de Verfolgte di richtige Wort und Wiisheit; mit Durehebe gwünned si ires Läbe. Jerusalem wird belageret und zertrampet. Dänn gscheend Zeiche am Himmel, und de Mänschesohn chunnt i ere Wolche; di Sine söled ufluege, dänn iri Erlösig chunnt nöch. De Jesus mahnt, wach z bliibe, und lehrt jede Tag im Tämpel."),
 "TU-LUK-021-001-004": ("D Gab vo de Witwe", "De Jesus gseht Riichi iri Gabe i de Opferstock wärfe und e armi Witwe zwei Lepta. Er seit: Si hät meh iigworfe als alli; di andere händ vo irem Überfluss ggää, si us irem Mangel ire ganz Läbesunderhalt."),
 "TU-LUK-021-005-019": ("S Änd vom Tämpel, Verfüerig und Verfolgig", "De Jesus seit aa, dass vom prächtige Tämpel kei Stei uf em andere bliibt. Uf d Frag nach em Wänn und em Zeiche warnt er vor Verfüerer, wo i sim Name uftreted, und vor Angscht bi Chrieg: S Änd chunnt nöd grad. Völker und Riich wärded sich erhebe, Ärdbebe, Hungersnöt, Süüche und Zeiche am Himmel chömed. Vorher aber wärded d Jünger verfolgt, usgliferet und vor König gstellt; de Jesus sälber git ine di richtige Wort und Wiisheit. Si wärded ghasst, es paar umbracht, aber kei Haar gaat verlore; mit Durehebe gwünned si ires Läbe."),
 "TU-LUK-021-020-024": ("D Verwüeschtig vo Jerusalem", "Wänn Heer Jerusalem umzingled, isch sini Verwüeschtig nöch: Wer z Judäa isch, söll i d Bärge flüchte. Es sind Täg vom Strafgricht, grossi Not chunnt übers Land und Zorn über s Volk; vili falled oder wärded verschleppt, und Jerusalem wird vo de Völker zertrampet, bis d Ziite vo de Völker erfüllt sind."),
 "TU-LUK-021-025-028": ("S Choo vom Mänschesohn", "Zeiche a Sunne, Mond und Stärne und s Toose vom Meer mached de Völker Angscht; d Mächt vom Himmel wärded erschütteret. Dänn gseht mer de Mänschesohn i ere Wolche mit Macht und grosser Herrlichkeit choo. Wänn das aafangt, söled sich d Jünger ufrichte, dänn iri Erlösig chunnt nöch."),
 "TU-LUK-021-029-033": ("S Gliichnis vom Fiigebaum", "Wie d Bäum, wo ustriibed, de Summer aazeiged, so zeiged die Ereignis, dass s Riich vo Gott nöch isch. Die Generation vergaat nöd, bis alles passiert; Himmel und Ärde vergönd, d Wort vom Jesus aber nöd."),
 "TU-LUK-021-034-038": ("Ufruef, wach z bliibe", "De Jesus mahnt, d Härz nöd dur Rusch und Alltagssorge z beschwäre, demit säbe Tag nöd wie e Falle über si chunnt; si söled wach bliibe und bätte, zum vor em Mänschesohn z bestaa. Tagsüber lehrt de Jesus im Tämpel, znacht isch er uf em Ölberg, und s ganz Volk chunnt am Morge früe, zum em zuelose."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Gegenlesung am 2026-10-26 durch eine getrennte KI-Instanz (Claude), die die Übersetzung nicht geschrieben hat: Vers für Vers gegen den SBLGNT (Treue, Sprache, Abschnittstitel und Zusammenfassungen), Wortzuordnung stichprobenweise, Handschriftenangaben gegen data/witness-readings und die CNTR-Transkriptionen. Das ist keine fachliche und keine muttersprachliche Prüfung."),
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1, "
  "data/witness-readings/WREAD-CNTR-LUK-018-001-043 bis WREAD-CNTR-LUK-021-001-038) bzw. auf den CNTR-Transkriptionen "
  "(Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften."),
 ("Lukas beginnt Erzählabschnitte oft mit ἐγένετο «es geschah»; am Abschnittsbeginn ist die Formel wiedergegeben "
  "([[LUK.18.35]], [[LUK.20.1]]), innerhalb eines Abschnitts nicht eigens ([[LUK.19.15]], [[LUK.19.29]]). ὅτι vor direkter Rede und λέγων/λέγοντες «sagend» neben einem anderen Verb des "
  "Sagens sind nicht eigens wiedergegeben; die Wortzuordnung vermerkt das."),
 ("παραδίδωμι ist durchgehend mit «ausliefern» wiedergegeben, υἱὸς τοῦ ἀνθρώπου mit «Menschensohn», ἔθνη je nach "
  "Zusammenhang mit «Heiden» ([[LUK.18.32]]) oder «Völker» ([[LUK.21.24]]); siehe decisions."),
 ("In Lukas 18–21 fehlt im SBLGNT kein Vers. Die Übersetzung folgt dem Token-Text des SBLGNT; abweichende Lesarten, die die "
  "Übersetzung verändern, stehen als Alternativen. Lesarten, die nur Wortstellung oder Schreibweise betreffen, sind nicht "
  "eigens aufgeführt."),
 ("Die Übersetzung gleicht nicht an Markus oder Matthäus an; Unterschiede zu den Parallelen (z. B. [[LUK.18.18]] «ein "
  "führender Mann», [[LUK.19.38]] «der König») bleiben stehen."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 ("Gägeläsig am 2026-10-26 dur e getrennti KI-Instanz (Claude), wo d Übersetzig nöd gschribe hät: Vers für Vers gäge de SBLGNT, Wortzueornig stichprobewiis. Das isch kei fachlichi und kei muettersprachlichi Prüefig."),
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("De Lukas faat Abschnitt oft mit ἐγένετο «es isch gsii» aa; am Aafang vo me Abschnitt isch d Formle widergää, "
  "innerhalb nöd eigens. ὅτι vor diräkter Red "
  "und λέγων/λέγοντες «sägend» näbe eme andere Verb vom Säge sind nöd eigens widergää."),
 ("Mundart hät kei Präteritum und kei Genitiv: d Vergangeheit staat im Perfekt, de Genitiv mit «vo» oder «em/de» (z. B. "
  "«s Riich vo Gott», «de Sohn vom David»)."),
]


def run():
    import json
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _lib import localize  # noqa: E402
    n = 0
    pruefe_mundart(list(GSW.values()) + [x for t in UNITS_GSW.values() for x in t] + [str(d) for d in DEC_GSW]
                   + [str(x) for x in NOTES_GSW] + [str(a[4:6] + a[8:9] + a[10:11] + a[12:]) for a in ALTS],
                   pathlib.Path(__file__).name)
    if not (D / "works" / "WORK-LUK.json").exists():
        raise SystemExit("WORK-LUK fehlt")
    for uid, rng, kind, title, parts, summary, seg in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-LUK", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}), "segmentation_note_de": seg,
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        rec = {k: v for k, v in rec.items() if v is not None}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-26; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    variants = {}
    for p in (D / "variants" / "sblgntapp-luk").glob("*.json"):
        v = json.loads(p.read_text(encoding="utf-8"))
        variants[v["id"]] = v
    for c, last in CHAPTERS:
        ts_id, toks = load_tokens(D / "tokens" / f"SBLGNT-LUK-{c:03d}.json")
        refs_c = [f"LUK.{c}.{v}" for v in range(1, last + 1) if f"LUK.{c}.{v}" in toks]
        if len(refs_c) != last:
            raise SystemExit(f"LUK {c}: Verse ohne Tokens")
        follows = sorted(f"{vid}:R1" for vid, v in variants.items() if v["reference"] in refs_c)
        for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
            texts, aligns = {}, []
            for r in refs_c:
                words = {pos: t["word"] for pos, t in toks[r].items()}
                text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
                texts[r], aligns = text, aligns + al
            tid = f"TRANS-LUK-{c:03d}-001-{last:03d}-{code}-WORKING"
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
            rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": f"LUK.{c}.1-LUK.{c}.{last}",
                   "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
            if lang == "gsw":
                rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-LUK-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches, zeitgemässes Deutsch; Zeitformen und Satzarten erhalten, die Erzählformel ἐγένετο nur am Abschnittsbeginn wiedergegeben. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                                                   if lang == "de" else "Möglichi Erkläärige, wie d Underschid entstande sii chönted. Si stönd näbenand; keini isch als richtig entschide.")
            n += write(D / "translations" / f"{tid}.json", rec)
            aid = f"ALIGN-LUK-{c:03d}-001-{last:03d}-{code}-001"
            n += write(D / "alignments" / f"{aid}.json", {
                "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": f"LUK.{c}.1-LUK.{c}.{last}",
                "source_language": "grc", "target_language": rec["language"], "source_basis": "ED-SBLGNT", "source_tokens_set": ts_id,
                "target_translation": tid, "coverage": "complete",
                "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} SBLGNT-Tokens ist genau einer Zuordnung zugewiesen.",
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/lukas_text_18_21.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Lukas 18–21 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
