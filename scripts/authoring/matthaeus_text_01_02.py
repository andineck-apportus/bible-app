#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 1–2 (Stammbaum, Geburt, Sterndeuter, Flucht nach Ägypten, Rückkehr nach Nazaret) –
Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen,
Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_01_02.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 1–2 fehlt im SBLGNT kein Vers (per Skript geprüft); alle Verse haben Tokens.
- Stammbaum ([[MAT.1.2]]–[[MAT.1.16]]): Das reihende δέ und der Artikel vor den Namen sind nicht eigens wiedergegeben
  (Artikel mit dem Namen zusammen zugeordnet, δέ als nicht wiedergegeben markiert).
- [[MAT.1.7]]–[[MAT.1.8]]: Der SBLGNT liest Ἀσάφ; der Apparat verzeichnet keine Variante, nach den CNTR-Texten lesen RP
  und KJTR Ἀσά. Das steht in decisions und translation_notes, nicht als Alternative.
- [[MAT.1.18]] und [[MAT.2.17]]: Die automatische Zuordnung der Handschriften widerspricht dort den
  CNTR-Transkriptionen; die Alternativen benennen die Unsicherheit.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1)
bzw. aus den CNTR-Transkriptionen (Sekundärtranskription), nicht aus eigener Prüfung der Handschriften. Zahlen zu
Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts (data/annotations) ermittelt.
"""
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, write  # noqa: E402

DATE = "2026-10-18"
AUTH = "KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; aus dem griechischen Text (SBLGNT) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-MATTHEW"]
CHAPTERS = ((1, 25), (2, 23))

# Im Stammbaum steht ein blosses «~n» für das reihende δέ.
_DE_NOTE = {"de": "δέ reiht die Glieder der Stammfolge aneinander; nicht eigens wiedergegeben",
            "gsw": "δέ reiht d Glider vom Stammbaum anenand; nöd eigens widergää"}


def G(markup, lang="de"):
    return re.sub(r"~(\d+)(?![\d(])", lambda m: f"~{m.group(1)}({_DE_NOTE[lang]})", markup)


def tri_de(a, b, c, d):
    """Vers mit drei Gliedern: a δέ ἐγέννησεν τὸν b, b δέ ἐγέννησεν τὸν c, c δέ ἐγέννησεν τὸν d."""
    return G("[%s]{1} [zeugte]{3} [%s]{4,5}, [%s]{6} [zeugte]{8} [%s]{9,10}, [%s]{11} [zeugte]{13} [%s]{14,15}. ~2 ~7 ~12"
             % (a, b, b, c, c, d))


def tri_gsw(a, b, c, d):
    return G("[De %s]{1} [isch]{3} [de Vatter]{3} [vom %s]{4,5} [worde]{3}, [de %s]{6} [isch]{8} [de Vatter]{8} "
             "[vom %s]{9,10} [worde]{8}, [de %s]{11} [isch]{13} [de Vatter]{13} [vom %s]{14,15} [worde]{13}. ~2 ~7 ~12"
             % (a, b, b, c, c, d), "gsw")


LXN = "λέγοντος «der sagt» leitet das Zitat ein; durch den Doppelpunkt wiedergegeben"
LXN_G = "λέγοντος «wo seit» leitet s Zitat ii; mit em Doppelpunkt widergää"

DE = {
 # ------------------------------------------------------------ Kapitel 1
 "MAT.1.1": "Das [Buch]{1} [vom Ursprung]{2} [Jesu]{3} [Christi]{4}, [des Sohnes]{5} [Davids]{6}, [des Sohnes]{7} [Abrahams]{8}.",
 "MAT.1.2": G("[Abraham]{1} [zeugte]{2} [Isaak]{3,4}, [Isaak]{5} [zeugte]{7} [Jakob]{8,9}, [Jakob]{10} [zeugte]{12} [Juda]{13,14} und{15} [seine]{18} [Brüder]{16,17}. ~6 ~11"),
 "MAT.1.3": G("[Juda]{1} [zeugte]{3} [Perez]{4,5} und{6} [Serach]{7,8} [von]{9} [Tamar]{10,11}, [Perez]{12} [zeugte]{14} [Hezron]{15,16}, [Hezron]{17} [zeugte]{19} [Ram]{20,21}. ~2 ~13 ~18"),
 "MAT.1.4": tri_de("Ram", "Amminadab", "Nachschon", "Salmon"),
 "MAT.1.5": G("[Salmon]{1} [zeugte]{3} [Boas]{4,5} [von]{6} [Rahab]{7,8}, [Boas]{9} [zeugte]{11} [Obed]{12,13} [von]{14} [Rut]{15,16}, [Obed]{17} [zeugte]{19} [Isai]{20,21}. ~2 ~10 ~18"),
 "MAT.1.6": G("[Isai]{1} [zeugte]{3} [den]{4} [König]{6,7} [David]{5}. [David]{8} [zeugte]{10} [Salomo]{11,12} [von]{13} [der]{14} Frau [des Urija]{15,16}. ~2 ~9"),
 "MAT.1.7": tri_de("Salomo", "Rehabeam", "Abija", "Asaf"),
 "MAT.1.8": tri_de("Asaf", "Joschafat", "Joram", "Usija"),
 "MAT.1.9": tri_de("Usija", "Jotam", "Ahas", "Hiskija"),
 "MAT.1.10": tri_de("Hiskija", "Manasse", "Amos", "Joschija"),
 "MAT.1.11": G("[Joschija]{1} [zeugte]{3} [Jechonja]{4,5} und{6} [seine]{9} [Brüder]{7,8} [zur Zeit]{10} [der]{11} [Wegführung]{12} [nach Babylon]{13}. ~2"),
 "MAT.1.12": G("[Nach]{1} [der]{3} [Wegführung]{4} [nach Babylon]{5} [aber]{2} [zeugte]{7} [Jechonja]{6} [Schealtiël]{8,9}, [Schealtiël]{10} [zeugte]{12} [Serubbabel]{13,14}. ~11"),
 "MAT.1.13": tri_de("Serubbabel", "Abihud", "Eljakim", "Azor"),
 "MAT.1.14": tri_de("Azor", "Zadok", "Achim", "Eliud"),
 "MAT.1.15": tri_de("Eliud", "Eleasar", "Mattan", "Jakob"),
 "MAT.1.16": G("[Jakob]{1} [zeugte]{3} [Josef]{4,5}, [den Mann]{6,7} [Marias]{8}, [von]{9} [der]{10} [Jesus]{12} [geboren wurde]{11}, [der]{13} [Christus]{15} [genannt wird]{14}. ~2"),
 "MAT.1.17": "[Alle]{1} [Generationen]{3,4} [nun]{2} [von]{5} [Abraham]{6} [bis]{7} [David]{8} sind [vierzehn]{10} [Generationen]{9}, und{11} [von]{12} [David]{13} [bis]{14} [zur]{15} [Wegführung]{16} [nach Babylon]{17} [vierzehn]{19} [Generationen]{18}, und{20} [von]{21} [der]{22} [Wegführung]{23} [nach Babylon]{24} [bis]{25} [zum]{26} [Christus]{27} [vierzehn]{29} [Generationen]{28}.",
 "MAT.1.18": "[Mit dem Ursprung]{5,6} [Jesu]{1,3} [Christi]{4} [aber]{2} [verhielt es sich]{8} [so]{7}: [Als]{9} [seine]{12} [Mutter]{10,11} [Maria]{13} [mit]{14} [Josef]{15} [verlobt war]{9}, [zeigte sich]{20}, noch [bevor]{16,17} [sie]{19} [zusammenkamen]{18}, dass sie [schwanger war]{21-23:idiom} – [vom]{24} [heiligen]{26} [Geist]{25}.",
 "MAT.1.19": "[Josef]{1} [aber]{2}, [ihr]{5} [Mann]{3,4}, [der]{7} [gerecht]{6} [war]{7} und{8} [sie]{11} [nicht]{9} [blossstellen]{12} [wollte]{10}, [beschloss]{13}, [sich]{15} [heimlich]{14} [von ihr]{16} [zu trennen]{15}.",
 "MAT.1.20": "[Während]{4} [er]{3} [aber]{2} [darüber]{1} [nachdachte]{4}, [siehe]{5}, da [erschien]{10} [ihm]{11} [ein Engel]{6} [des Herrn]{7} [im]{8} [Traum]{9} und [sagte]{12}: «[Josef]{13}, [Sohn]{14} [Davids]{15}, [fürchte dich]{17} [nicht]{16}, [Maria]{19}, [deine]{22} [Frau]{20,21}, [zu dir zu nehmen]{18}; [denn]{24} [was]{23} [in]{25} [ihr]{26} [gezeugt ist]{27}, [ist]{30} [vom]{28} [heiligen]{31} [Geist]{29}.",
 "MAT.1.21": "[Sie wird]{1} [aber]{2} [einen Sohn]{3} [gebären]{1}, und{4} [du sollst]{5} [ihm]{8} [den Namen]{6,7} [Jesus]{9} [geben]{5}; [denn]{11} [er]{10} [wird]{12} [sein]{15} [Volk]{13,14} [von]{16} [ihren]{19} [Sünden]{17,18} [retten]{12}.»",
 "MAT.1.22": f"[Das]{{1}} [alles]{{3}} [aber]{{2}} [ist geschehen]{{4}}, [damit]{{5}} [erfüllt würde]{{6}}, [was]{{7}} [vom]{{9}} [Herrn]{{10}} [durch]{{11}} [den Propheten]{{12,13}} [gesagt ist]{{8}}: ~14({LXN})",
 "MAT.1.23": "«[Siehe]{1}, [die Jungfrau]{2,3} [wird schwanger sein]{4-6:idiom} und{7} [einen Sohn]{9} [gebären]{8}, und{10} [man wird]{11} [ihm]{14} [den Namen]{12,13} [Immanuel]{15} [geben]{11}», [das]{16} [heisst]{17} [übersetzt]{18}: [Gott]{21,22} [mit]{19} [uns]{20}.",
 "MAT.1.24": "[Als]{1} [Josef]{3,4} [aber]{2} [vom]{5,6} [Schlaf]{7} [erwachte]{1}, [tat er]{8}, [wie]{9} [ihm]{11} [der Engel]{12,13} [des Herrn]{14} [befohlen hatte]{10}, und{15} [nahm]{16} [seine]{19} [Frau]{17,18} [zu sich]{16}.",
 "MAT.1.25": "Und{1} [er schlief]{3} [nicht]{2} [mit ihr]{4}, [bis]{5,6} [sie]{7} [einen Sohn]{8} [geboren hatte]{7}; und{9} [er gab]{10} [ihm]{13} [den Namen]{11,12} [Jesus]{14}.",
 # ------------------------------------------------------------ Kapitel 2
 "MAT.2.1": "[Als]{4} [Jesus]{1,3} [aber]{2} [in]{5} [Betlehem]{6} [in Judäa]{7,8} [geboren war]{4}, [in]{9} [den Tagen]{10} [des Königs]{12,13} [Herodes]{11}, [siehe]{14}, da [kamen]{18} [Sterndeuter]{15} [aus]{16} [dem Osten]{17} [nach]{19} [Jerusalem]{20}",
 "MAT.2.2": "und [sagten]{1}: «[Wo]{2} [ist]{3} [der]{4} [neugeborene]{5} [König]{6} [der Juden]{7,8}? [Denn]{10} [wir haben]{9} [seinen]{11} [Stern]{12,13} [bei seinem Aufgang]{14-16} [gesehen]{9} und{17} [sind gekommen]{18}, [um]{19} [ihm]{20} [zu huldigen]{19}.»",
 "MAT.2.3": "[Als]{1} [der König]{3,4} [Herodes]{5} [aber]{2} [das hörte]{1}, [erschrak er]{6}, und{7} [ganz]{8} [Jerusalem]{9} [mit]{10} [ihm]{11}.",
 "MAT.2.4": "Und{1} [er versammelte]{2} [alle]{3} [Hohepriester]{4,5} und{6} [Schriftgelehrten]{7} [des Volkes]{8,9} und [erkundigte sich]{10} [bei]{11} [ihnen]{12}, [wo]{13} [der Christus]{14,15} [geboren werde]{16}.",
 "MAT.2.5": "[Sie]{1} [aber]{2} [sagten]{3} [zu ihm]{4}: «[In]{5} [Betlehem]{6} [in Judäa]{7,8}; [denn]{10} [so]{9} [ist]{11} [durch]{12} [den Propheten]{13,14} [geschrieben]{11}:",
 "MAT.2.6": "‹[Und]{1} [du]{2}, [Betlehem]{3}, [Land]{4} [Juda]{5}, [bist]{8} [keineswegs]{6} [die geringste]{7} [unter]{9} [den Fürsten]{10,11} [Judas]{12}; [denn]{15} [aus]{13} [dir]{14} [wird]{16} [ein Herrscher]{17} [hervorgehen]{16}, [der]{18} [mein]{22} [Volk]{20,21} [Israel]{23,24} [weiden wird]{19}.›»",
 "MAT.2.7": "[Da]{1} [rief]{4} [Herodes]{2} [die Sterndeuter]{5,6} [heimlich]{3} [zu sich]{4} und [erfragte]{7} [von]{8} [ihnen]{9} [genau]{7} [die Zeit]{10,11}, in der [der]{12} [Stern]{14} [erschienen war]{13}.",
 "MAT.2.8": "Und{1} [er schickte]{2} [sie]{3} [nach]{4} [Betlehem]{5} und [sagte]{6}: «[Geht hin]{7} und [forscht]{8} [genau]{9} [nach]{10} [dem Kind]{11,12}; [wenn]{13} [ihr]{15} es [aber]{14} [gefunden habt]{15}, [meldet es]{16} [mir]{17}, [damit]{18} [auch ich]{19} [komme]{20} und [ihm]{22} [huldige]{21}.»",
 "MAT.2.9": "[Als]{3} [sie]{1} [aber]{2} [den König]{4,5} [gehört hatten]{3}, [zogen sie hin]{6}; und{7} [siehe]{8}, [der Stern]{9,10}, [den]{11} [sie]{12} [bei seinem Aufgang]{13-15} [gesehen hatten]{12}, [zog]{16} [vor]{16} [ihnen]{17} [her]{16}, [bis]{18} er [ankam]{19} und [über]{21} dem Ort [stehen blieb]{20}, [wo]{22} [das Kind]{24,25} [war]{23}.",
 "MAT.2.10": "[Als sie]{1} [aber]{2} [den Stern]{3,4} [sahen]{1}, [freuten sie sich]{5} mit [sehr]{8} [grosser]{7} [Freude]{6}.",
 "MAT.2.11": "Und{1} [sie gingen]{2} [in]{3} [das Haus]{4,5} und [sahen]{6} [das Kind]{7,8} [mit]{9} [Maria]{10}, [seiner]{13} [Mutter]{11,12}; und{14} [sie fielen nieder]{15} und [huldigten]{16} [ihm]{17}, und{18} [sie öffneten]{19} [ihre]{22} [Schatztruhen]{20,21} und [brachten]{23} [ihm]{24} [Gaben]{25} [dar]{23}: [Gold]{26} und{27} [Weihrauch]{28} und{29} [Myrrhe]{30}.",
 "MAT.2.12": "Und{1} [weil sie]{2} [im]{3} [Traum]{4} [die Weisung erhalten hatten]{2}, [nicht]{5} [zu]{7} [Herodes]{8} [zurückzukehren]{6}, [zogen sie sich]{12} [auf]{9} [einem anderen]{10} [Weg]{11} [in]{13} [ihr]{16} [Land]{14,15} [zurück]{12}.",
 "MAT.2.13": "[Als]{1} [sie]{3} [sich]{1} [aber]{2} [zurückgezogen hatten]{1}, [siehe]{4}, da [erscheint]{7} [dem Josef]{10,11} [ein Engel]{5} [des Herrn]{6} [im]{8} [Traum]{9} und [sagt]{12}: «[Steh auf]{13}, [nimm]{14} [das Kind]{15,16} und{17} [seine]{20} [Mutter]{18,19} [zu dir]{14} und{21} [flieh]{22} [nach]{23} [Ägypten]{24}, und{25} [bleib]{26} [dort]{27}, [bis]{28,29} [ich]{30} es [dir]{31} [sage]{30}; [denn]{33} [Herodes]{34} [wird]{32} [das Kind]{36,37} [suchen]{35}, [um]{38} [es]{40} [umzubringen]{39}.»",
 "MAT.2.14": "[Er]{1} [aber]{2} [stand auf]{3}, [nahm]{4} [das Kind]{5,6} und{7} [seine]{10} [Mutter]{8,9} [bei Nacht]{11} [zu sich]{4} und{12} [zog sich]{13} [nach]{14} [Ägypten]{15} [zurück]{13}",
 "MAT.2.15": f"und{{1}} [er blieb]{{2}} [dort]{{3}} [bis]{{4}} [zum Tod]{{5,6}} [des Herodes]{{7}}, [damit]{{8}} [erfüllt würde]{{9}}, [was]{{10}} [vom]{{12}} [Herrn]{{13}} [durch]{{14}} [den Propheten]{{15,16}} [gesagt ist]{{11}}: «[Aus]{{18}} [Ägypten]{{19}} [habe ich]{{20}} [meinen]{{23}} [Sohn]{{21,22}} [gerufen]{{20}}.» ~17({LXN})",
 "MAT.2.16": "[Da]{1} [sah]{3} [Herodes]{2}, [dass]{4} [er]{5} [von]{6} [den Sterndeutern]{7,8} [hintergangen worden war]{5}, und [wurde]{9} [sehr]{10} [zornig]{9}; und{11} [er sandte]{12} hin und [liess]{13} [alle]{14} [Knaben]{15,16} [in]{17,18} [Betlehem]{19} und{20} [in]{21} [ihrer]{25} [ganzen]{22} [Umgebung]{23,24} [töten]{13}, [von]{26} [zwei Jahren]{27} [an]{26} und{28} [darunter]{29}, [nach]{30} [der Zeit]{31,32}, [die]{33} [er]{34} [von]{35} [den Sterndeutern]{36,37} [genau erfragt hatte]{34}.",
 "MAT.2.17": f"[Da]{{1}} [wurde erfüllt]{{2}}, [was]{{3}} [durch]{{5}} [Jeremia]{{6}}, [den Propheten]{{7,8}}, [gesagt ist]{{4}}: ~9({LXN})",
 "MAT.2.18": "«[Eine Stimme]{1} [wurde]{4} [in]{2} [Rama]{3} [gehört]{4}, [Weinen]{5} und{6} [viel]{8} [Wehklagen]{7}: [Rahel]{9} [beweinte]{10} [ihre]{13} [Kinder]{11,12} und{14} [wollte]{16} [sich]{17} [nicht]{15} [trösten lassen]{17}, [denn]{18} [sie sind]{20} [nicht mehr]{19}.»",
 "MAT.2.19": "[Als]{1} [Herodes]{3,4} [aber]{2} [gestorben war]{1}, [siehe]{5}, da [erscheint]{8} [dem Josef]{11,12} [in]{13} [Ägypten]{14} [ein Engel]{6} [des Herrn]{7} [im]{9} [Traum]{10}",
 "MAT.2.20": "und [sagt]{1}: «[Steh auf]{2}, [nimm]{3} [das Kind]{4,5} und{6} [seine]{9} [Mutter]{7,8} [zu dir]{3} und{10} [zieh]{11} [in]{12} [das Land]{13} [Israel]{14}; [denn]{16} [gestorben sind]{15} [die, die]{17} [dem Kind]{21,22} [nach dem Leben trachteten]{18-20:idiom}.»",
 "MAT.2.21": "[Er]{1} [aber]{2} [stand auf]{3}, [nahm]{4} [das Kind]{5,6} und{7} [seine]{10} [Mutter]{8,9} [zu sich]{4} und{11} [kam]{12} [in]{13} [das Land]{14} [Israel]{15}.",
 "MAT.2.22": "[Als er]{1} [aber]{2} [hörte]{1}, [dass]{3} [Archelaus]{4} [anstelle]{8} [seines]{11} [Vaters]{9,10} [Herodes]{12} [über Judäa]{6,7} [als König herrschte]{5}, [fürchtete er sich]{13}, [dorthin]{14} [zu gehen]{15}. [Im]{18} [Traum]{19} [aber]{17} [erhielt er eine Weisung]{16} und [zog sich]{20} [in]{21} [die Gegend]{22,23} [von Galiläa]{24,25} [zurück]{20}",
 "MAT.2.23": "und{1} [als er dort ankam]{2}, [liess er sich]{3} [in]{4} [einer Stadt]{5} [nieder]{3}, [die]{6} [Nazaret]{7} [heisst]{6}, [damit]{8} [erfüllt würde]{9}, [was]{10} [durch]{12} [die Propheten]{13,14} [gesagt ist]{11}: [Er]{17} [wird]{17} [Nazoräer]{16} [genannt werden]{17}. ~15(ὅτι leitet das Prophetenwort ein; durch den Doppelpunkt wiedergegeben)",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 1
 "MAT.1.1": "S [Buech]{1} [vom Ursprung]{2} [vo Jesus]{3} [Christus]{4}, [em Sohn]{5} [vom David]{6}, [em Sohn]{7} [vom Abraham]{8}.",
 "MAT.1.2": G("[De Abraham]{1} [isch]{2} [de Vatter]{2} [vom Isaak]{3,4} [worde]{2}, [de Isaak]{5} [isch]{7} [de Vatter]{7} [vom Jakob]{8,9} [worde]{7}, [de Jakob]{10} [isch]{12} [de Vatter]{12} [vom Juda]{13,14} und{15} [vo]{16} [sine]{18} [Brüedere]{17} [worde]{12}. ~6 ~11", "gsw"),
 "MAT.1.3": G("[De Juda]{1} [isch]{3} [vo]{9} [de Tamar]{10,11} [de Vatter]{3} [vom Perez]{4,5} und{6} [vom Serach]{7,8} [worde]{3}, [de Perez]{12} [isch]{14} [de Vatter]{14} [vom Hezron]{15,16} [worde]{14}, [de Hezron]{17} [isch]{19} [de Vatter]{19} [vom Ram]{20,21} [worde]{19}. ~2 ~13 ~18", "gsw"),
 "MAT.1.4": tri_gsw("Ram", "Amminadab", "Nachschon", "Salmon"),
 "MAT.1.5": G("[De Salmon]{1} [isch]{3} [vo]{6} [de Rahab]{7,8} [de Vatter]{3} [vom Boas]{4,5} [worde]{3}, [de Boas]{9} [isch]{11} [vo]{14} [de Rut]{15,16} [de Vatter]{11} [vom Obed]{12,13} [worde]{11}, [de Obed]{17} [isch]{19} [de Vatter]{19} [vom Isai]{20,21} [worde]{19}. ~2 ~10 ~18", "gsw"),
 "MAT.1.6": G("[De Isai]{1} [isch]{3} [de Vatter]{3} [vom]{4} [König]{6,7} [David]{5} [worde]{3}. [De David]{8} [isch]{10} [vo]{13} [de]{14} Frau [vom Urija]{15,16} [de Vatter]{10} [vom Salomo]{11,12} [worde]{10}. ~2 ~9", "gsw"),
 "MAT.1.7": tri_gsw("Salomo", "Rehabeam", "Abija", "Asaf"),
 "MAT.1.8": tri_gsw("Asaf", "Joschafat", "Joram", "Usija"),
 "MAT.1.9": tri_gsw("Usija", "Jotam", "Ahas", "Hiskija"),
 "MAT.1.10": tri_gsw("Hiskija", "Manasse", "Amos", "Joschija"),
 "MAT.1.11": G("[De Joschija]{1} [isch]{3} [de Vatter]{3} [vom Jechonja]{4,5} und{6} [vo]{7} [sine]{9} [Brüedere]{8} [worde]{3}, [zur Ziit]{10} [vo de]{11} [Wägfüerig]{12} [uf Babylon]{13}. ~2", "gsw"),
 "MAT.1.12": G("[Nach]{1} [de]{3} [Wägfüerig]{4} [uf Babylon]{5} [aber]{2} [isch]{7} [de Jechonja]{6} [de Vatter]{7} [vom Schealtiël]{8,9} [worde]{7}, [de Schealtiël]{10} [isch]{12} [de Vatter]{12} [vom Serubbabel]{13,14} [worde]{12}. ~11", "gsw"),
 "MAT.1.13": tri_gsw("Serubbabel", "Abihud", "Eljakim", "Azor"),
 "MAT.1.14": tri_gsw("Azor", "Zadok", "Achim", "Eliud"),
 "MAT.1.15": tri_gsw("Eliud", "Eleasar", "Mattan", "Jakob"),
 "MAT.1.16": G("[De Jakob]{1} [isch]{3} [de Vatter]{3} [vom Josef]{4,5} [worde]{3}, [vom Maa]{6,7} [vo de Maria]{8}; [vo]{9} [ire]{10} [isch]{11} [de Jesus]{12} [gebore worde]{11}, [wo]{13} [Christus]{15} [gnännt wird]{14}. ~2", "gsw"),
 "MAT.1.17": "[Alli]{1} [Generatione]{3,4} [also]{2} [vom]{5} [Abraham]{6} [bis zum]{7} [David]{8} sind [vierzää]{10} [Generatione]{9}, und{11} [vom]{12} [David]{13} [bis]{14} [zur]{15} [Wägfüerig]{16} [uf Babylon]{17} [vierzää]{19} [Generatione]{18}, und{20} [vo]{21} [de]{22} [Wägfüerig]{23} [uf Babylon]{24} [bis]{25} [zum]{26} [Christus]{27} [vierzää]{29} [Generatione]{28}.",
 "MAT.1.18": "[Mit em Ursprung]{5,6} [vo Jesus]{1,3} [Christus]{4} [aber]{2} [isch es]{8} [so]{7} [gsii]{8}: [Wo]{9} [sini]{12} [Mueter]{10,11} [Maria]{13} [mit em]{14} [Josef]{15} [verlobt gsii isch]{9}, [hät sich]{20}, no [bevor]{16,17} [si]{19} [zämechoo sind]{18}, [zeigt]{20}, dass si [schwanger isch]{21-23:idiom} – [vom]{24} [heilige]{26} [Geischt]{25}.",
 "MAT.1.19": "[De Josef]{1} [aber]{2}, [ire]{5} [Maa]{3,4}, [wo]{7} [grächt]{6} [gsii isch]{7} und{8} [si]{11} [nöd]{9} [hät wele]{10} [blossstelle]{12}, [hät beschlosse]{13}, [sich]{15} [heimlich]{14} [vo ire]{16} [z trenne]{15}.",
 "MAT.1.20": "[Wo]{4} [er]{3} [aber]{2} [über das]{1} [nachedänkt hät]{4}, [lueg]{5}, da [isch]{10} [ihm]{11} [en Ängel]{6} [vom Herr]{7} [im]{8} [Traum]{9} [erschiene]{10} und [hät gseit]{12}: «[Josef]{13}, [Sohn]{14} [vom David]{15}, [heb]{17} [kei]{16} [Angscht]{17}, [d Maria]{19}, [dini]{22} [Frau]{20,21}, [zu dir z neh]{18}; [dänn]{24} [was]{23} [in]{25} [ire]{26} [empfange worde isch]{27}, [isch]{30} [vom]{28} [heilige]{31} [Geischt]{29}.",
 "MAT.1.21": "[Si wird]{1} [aber]{2} [en Sohn]{3} [übercho]{1}, und{4} [du söllsch]{5} [ihm]{8} [de Name]{6,7} [Jesus]{9} [gää]{5}; [dänn]{11} [er]{10} [wird]{12} [sis]{15} [Volk]{13,14} [vo]{16} [irne]{19} [Sünde]{17,18} [rette]{12}.»",
 "MAT.1.22": f"[Das]{{1}} [alles]{{3}} [aber]{{2}} [isch gscheh]{{4}}, [damit]{{5}} [erfüllt wird]{{6}}, [was]{{7}} [vom]{{9}} [Herr]{{10}} [dur]{{11}} [de Prophet]{{12,13}} [gseit worden isch]{{8}}: ~14({LXN_G})",
 "MAT.1.23": "«[Lueg]{1}, [d Jungfrau]{2,3} [wird schwanger sii]{4-6:idiom} und{7} [en Sohn]{9} [übercho]{8}, und{10} [mer wird]{11} [ihm]{14} [de Name]{12,13} [Immanuel]{15} [gää]{11}», [das]{16} [heisst]{17} [übersetzt]{18}: [Gott]{21,22} [mit]{19} [üs]{20}.",
 "MAT.1.24": "[Wo]{1} [de Josef]{3,4} [aber]{2} [us em]{5,6} [Schlaf]{7} [verwachet isch]{1}, [hät er gmacht]{8}, [wie]{9} [ihm]{11} [de Ängel]{12,13} [vom Herr]{14} [befohle hät]{10}, und{15} [hät]{16} [sini]{19} [Frau]{17,18} [zu sich gnoo]{16}.",
 "MAT.1.25": "Und{1} [er hät]{3} [nöd]{2} [mit ire]{4} [gschlafe]{3}, [bis]{5,6} [si]{7} [en Sohn]{8} [übercho hät]{7}; und{9} [er hät]{10} [ihm]{13} [de Name]{11,12} [Jesus]{14} [gää]{10}.",
 # ------------------------------------------------------------ Kapitel 2
 "MAT.2.1": "[Wo]{4} [de Jesus]{1,3} [aber]{2} [z]{5} [Betlehem]{6} [in Judäa]{7,8} [gebore worde isch]{4}, [i]{9} [de Täg]{10} [vom König]{12,13} [Herodes]{11}, [lueg]{14}, da [sind]{18} [Stärndüüter]{15} [us]{16} [em Oste]{17} [uf]{19} [Jerusalem]{20} [choo]{18}",
 "MAT.2.2": "und [händ]{1} [gseit]{1}: «[Wo]{2} [isch]{3} [de]{4} [neugebore]{5} [König]{6} [vo de Jude]{7,8}? [Dänn]{10} [mir händ]{9} [sin]{11} [Stärn]{12,13} [bi sim Ufgang]{14-16} [gseh]{9} und{17} [sind choo]{18}, [zum]{19} [ihm]{20} [huldige]{19}.»",
 "MAT.2.3": "[Wo]{1} [de König]{3,4} [Herodes]{5} [aber]{2} [das ghört hät]{1}, [isch er verschrocke]{6}, und{7} [ganz]{8} [Jerusalem]{9} [mit]{10} [ihm]{11}.",
 "MAT.2.4": "Und{1} [er hät]{2} [alli]{3} [Hoheprieschter]{4,5} und{6} [Schriftgelehrti]{7} [vom Volk]{8,9} [versammlet]{2} und [hät]{10} [bi]{11} [ine]{12} [nachgfröget]{10}, [wo]{13} [de Christus]{14,15} [gebore wird]{16}.",
 "MAT.2.5": "[Si]{1} [aber]{2} [händ]{3} [zu ihm]{4} [gseit]{3}: «[Z]{5} [Betlehem]{6} [in Judäa]{7,8}; [dänn]{10} [so]{9} [staat]{11} [dur]{12} [de Prophet]{13,14} [gschribe]{11}:",
 "MAT.2.6": "‹[Und]{1} [du]{2}, [Betlehem]{3}, [Land]{4} [Juda]{5}, [bisch]{8} [überhaupt nöd]{6} [di chliinscht]{7} [under]{9} [de Fürschte]{10,11} [vo Juda]{12}; [dänn]{15} [us]{13} [dir]{14} [wird]{16} [en Herrscher]{17} [usechoo]{16}, [wo]{18} [mis]{22} [Volk]{20,21} [Israel]{23,24} [wird hüete]{19}.›»",
 "MAT.2.7": "[Dänn]{1} [hät]{4} [de Herodes]{2} [d Stärndüüter]{5,6} [heimlich]{3} [zu sich grüeft]{4} und [hät]{7} [vo]{8} [ine]{9} [d Ziit]{10,11} [genau erfröget]{7}, wo [de]{12} [Stärn]{14} [erschiene isch]{13}.",
 "MAT.2.8": "Und{1} [er hät]{2} [si]{3} [uf]{4} [Betlehem]{5} [gschickt]{2} und [gseit]{6}: «[Gönd]{7} und [forsched]{8} [genau]{9} [nach]{10} [em Chind]{11,12}; [wänn]{13} [ir]{15} s [aber]{14} [gfunde händ]{15}, [mälded s]{16} [mir]{17}, [demit]{18} [au ich]{19} [chume]{20} und [ihm]{22} [huldige]{21}.»",
 "MAT.2.9": "[Wo]{3} [si]{1} [aber]{2} [de König]{4,5} [ghört händ]{3}, [sind si gange]{6}; und{7} [lueg]{8}, [de Stärn]{9,10}, [wo]{11} [si]{12} [bi sim Ufgang]{13-15} [gseh händ]{12}, [isch]{16} [ine]{17} [voruus zoge]{16}, [bis]{18} er [aachoo isch]{19} und [über]{21} em Ort, [wo]{22} [s Chind]{24,25} [gsii isch]{23}, [staa bliibe isch]{20}.",
 "MAT.2.10": "[Wo si]{1} [aber]{2} [de Stärn]{3,4} [gseh händ]{1}, [händ si sich]{5} mit ere [ganz]{8} [grosse]{7} [Fröid]{6} [gfröit]{5}.",
 "MAT.2.11": "Und{1} [si sind]{2} [is]{3,4} [Huus]{5} [gange]{2} und [händ]{6} [s Chind]{7,8} [mit]{9} [de Maria]{10}, [sinere]{13} [Mueter]{11,12}, [gseh]{6}; und{14} [si sind uf d Chnü gfalle]{15} und [händ]{16} [ihm]{17} [ghuldiget]{16}, und{18} [si händ]{19} [iri]{22} [Schatztrucke]{20,21} [ufgmacht]{19} und [händ]{23} [ihm]{24} [Gschänk]{25} [brocht]{23}: [Gold]{26} und{27} [Wiirauch]{28} und{29} [Myrrhe]{30}.",
 "MAT.2.12": "Und{1} [wil si]{2} [im]{3} [Traum]{4} [d Wiisig übercho händ]{2}, [nöd]{5} [zum]{7} [Herodes]{8} [zruggzgaa]{6}, [händ si sich]{12} [uf]{9} [eme andere]{10} [Wäg]{11} [i]{13} [ires]{16} [Land]{14,15} [zruggzoge]{12}.",
 "MAT.2.13": "[Wo]{1} [si]{3} [sich]{1} [aber]{2} [zruggzoge händ]{1}, [lueg]{4}, da [erschiint]{7} [em Josef]{10,11} [en Ängel]{5} [vom Herr]{6} [im]{8} [Traum]{9} und [seit]{12}: «[Stand uf]{13}, [nimm]{14} [s Chind]{15,16} und{17} [sini]{20} [Mueter]{18,19} [zu dir]{14} und{21} [flüch]{22} [uf]{23} [Ägypte]{24}, und{25} [bliib]{26} [dört]{27}, [bis]{28,29} [ich]{30} [dir]{31} s [säg]{30}; [dänn]{33} [de Herodes]{34} [wird]{32} [s Chind]{36,37} [sueche]{35}, [für]{38} [s]{40} [umzbringe]{39}.»",
 "MAT.2.14": "[Er]{1} [aber]{2} [isch ufgstande]{3}, [hät]{4} [s Chind]{5,6} und{7} [sini]{10} [Mueter]{8,9} [znacht]{11} [zu sich gnoo]{4} und{12} [hät sich]{13} [uf]{14} [Ägypte]{15} [zruggzoge]{13}",
 "MAT.2.15": f"und{{1}} [er isch]{{2}} [dört]{{3}} [bliibe]{{2}} [bis]{{4}} [zum Tod]{{5,6}} [vom Herodes]{{7}}, [damit]{{8}} [erfüllt wird]{{9}}, [was]{{10}} [vom]{{12}} [Herr]{{13}} [dur]{{14}} [de Prophet]{{15,16}} [gseit worden isch]{{11}}: «[Us]{{18}} [Ägypte]{{19}} [han ich]{{20}} [min]{{23}} [Sohn]{{21,22}} [grüeft]{{20}}.» ~17({LXN_G})",
 "MAT.2.16": "[Dänn]{1} [hät]{3} [de Herodes]{2} [gseh]{3}, [dass]{4} [er]{5} [vo]{6} [de Stärndüüter]{7,8} [für dumm verchauft worde isch]{5}, und [isch]{9} [ganz]{10} [wüetig worde]{9}; und{11} [er hät]{12} Lüüt [gschickt]{12} und [hät]{13} [alli]{14} [Buebe]{15,16} [z]{17,18} [Betlehem]{19} und{20} [i]{21} [de ganze]{22} [Umgäbig]{23,24} [devo]{25}, [vo]{26} [zwei Jahr]{27} [aa]{26} und{28} [drunder]{29}, [la umbringe]{13}, [nach]{30} [de Ziit]{31,32}, [wo]{33} [er]{34} [vo]{35} [de Stärndüüter]{36,37} [genau erfröget hät]{34}.",
 "MAT.2.17": f"[Dänn]{{1}} [isch erfüllt worde]{{2}}, [was]{{3}} [dur]{{5}} [de Jeremia]{{6}}, [de Prophet]{{7,8}}, [gseit worden isch]{{4}}: ~9({LXN_G})",
 "MAT.2.18": "«[E Stimm]{1} [isch]{4} [z]{2} [Rama]{3} [ghört worde]{4}, [Briegge]{5} und{6} [vil]{8} [Jammer]{7}: [D Rahel]{9} [hät]{10} [um]{10} [iri]{13} [Chind]{11,12} [briegget]{10} und{14} [hät]{16} [sich]{17} [nöd]{15} [wele]{16} [la tröschte]{17}, [dänn]{18} [si sind]{20} [nüme]{19}.»",
 "MAT.2.19": "[Wo]{1} [de Herodes]{3,4} [aber]{2} [gstorbe isch]{1}, [lueg]{5}, da [erschiint]{8} [em Josef]{11,12} [in]{13} [Ägypte]{14} [en Ängel]{6} [vom Herr]{7} [im]{9} [Traum]{10}",
 "MAT.2.20": "und [seit]{1}: «[Stand uf]{2}, [nimm]{3} [s Chind]{4,5} und{6} [sini]{9} [Mueter]{7,8} [zu dir]{3} und{10} [gang]{11} [is]{12} [Land]{13} [Israel]{14}; [dänn]{16} [die, wo]{17} [em Chind]{21,22} [as Läbe händ wele]{18-20:idiom}, [sind gstorbe]{15}.»",
 "MAT.2.21": "[Er]{1} [aber]{2} [isch ufgstande]{3}, [hät]{4} [s Chind]{5,6} und{7} [sini]{10} [Mueter]{8,9} [zu sich gnoo]{4} und{11} [isch]{12} [is]{13} [Land]{14} [Israel]{15} [choo]{12}.",
 "MAT.2.22": "[Wo er]{1} [aber]{2} [ghört hät]{1}, [dass]{3} [de Archelaus]{4} [anstell]{8} [vo sim]{11} [Vatter]{9,10} [Herodes]{12} [über Judäa]{6,7} [als König regiert]{5}, [hät er Angscht gha]{13}, [dörthii]{14} [z gaa]{15}. [Im]{18} [Traum]{19} [aber]{17} [hät er e Wiisig übercho]{16} und [hät sich]{20} [i]{21} [d Gäged]{22,23} [vo Galiläa]{24,25} [zruggzoge]{20}",
 "MAT.2.23": "und{1} [wo er dört aachoo isch]{2}, [hät er sich]{3} [i]{4} [ere Stadt]{5} [niderglaa]{3}, [wo]{6} [Nazaret]{7} [heisst]{6}, [damit]{8} [erfüllt wird]{9}, [was]{10} [dur]{12} [d Prophete]{13,14} [gseit worden isch]{11}: [Er]{17} [wird]{17} [Nazoräer]{16} [gnännt wärde]{17}. ~15(ὅτι leitet s Prophetewort ii; mit em Doppelpunkt widergää)",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MAT.1.1", "Buch vom Ursprung", "interpretive", "Βίβλος γενέσεως", "Buch der Entstehung", ["Stammbaum", "Buch der Geschichte", "Buch der Genesis"],
  "βίβλος γενέσεως steht in der Septuaginta in [[GEN.2.4]] und [[GEN.5.1]] («Buch der Entstehung von Himmel und Erde», «der Menschen»); der Anklang an das erste Buch der Bibel ist wahrscheinlich gewollt. Ob die Überschrift nur den Stammbaum ([[MAT.1.2]]–[[MAT.1.17]]), die ganze Vorgeschichte (Kapitel 1–2) oder das ganze Buch meint, ist umstritten. «Ursprung» lässt das offen und wird in [[MAT.1.18]] für dasselbe Wort γένεσις wieder verwendet."),
 ("MAT.1.1", "Christi", "traditional", "χριστοῦ", "des Gesalbten", ["des Messias"],
  "Grundentscheid für das ganze Evangelium: Χριστός «Christus». Das griechische Wort übersetzt das hebräische Wort für «Gesalbter» (Messias, vgl. [[JHN.1.41]]): den von Gott erwarteten König aus Davids Haus. In [[MAT.1.1]] und [[MAT.1.18]] steht es neben «Jesus» fast wie ein Name; mit Artikel ist es Titel («der Christus», [[MAT.1.17]], [[MAT.2.4]]). Nach MACULA-Lemma 16-mal im Evangelium."),
 ("MAT.1.1", "des Sohnes Davids", "literal", "υἱοῦ Δαυὶδ", None, ["des Nachkommen Davids"],
  "υἱός meint hier den Nachkommen. «Sohn Davids» ist bei Matthäus zugleich eine Anrede an Jesus (z. B. [[MAT.9.27]], [[MAT.21.9]]); deshalb bleibt das Wort «Sohn»."),
 ("MAT.1.2", "zeugte", "traditional", "ἐγέννησεν", None, ["wurde der Vater von", "war der Vater von"],
  "ἐγέννησεν steht im Stammbaum 39-mal in derselben Form (per Skript gezählt). «Zeugte» gibt das aktive Verb wörtlich wieder und lässt den Bruch in [[MAT.1.16]] sichtbar (dort Passiv, von Maria aus). Das Wort kann auch einen entfernteren Vorfahren meinen (vgl. [[MAT.1.8]]). Das reihende δέ und der Artikel vor den Namen (τὸν Ἰσαάκ) sind nicht eigens wiedergegeben."),
 ("MAT.1.3", "Hezron", "traditional", "Ἑσρώμ", "Esrom", ["Hesron"],
  "Die Namen des Stammbaums stehen in der aus dem Alten Testament vertrauten Form (Loccumer Richtlinien), nicht in der griechischen Lautung (Esrom, Aram, Naasson, Booz/Boes, Jobed, Jesse, Ozias, Jechonias, Salathiel, Zorobabel). Ausnahmen sind Asaf ([[MAT.1.7]]) und Amos ([[MAT.1.10]]), wo die griechische Form einen anderen Namen ergibt."),
 ("MAT.1.3", "Ram", "traditional", "Ἀράμ", "Aram", None,
  "Nach [[RUT.4.19]] und [[1CH.2.9]] heisst der Sohn Hezrons Ram; die Septuaginta schreibt Αραμ. «Aram» wäre mit dem Volks- und Landesnamen zu verwechseln."),
 ("MAT.1.3", "von Tamar", "literal", "ἐκ τῆς Θαμάρ", "aus der Tamar", ["mit Tamar"],
  "ἐκ nennt die Mutter. Neben den Vätern nennt der Stammbaum vier Frauen: Tamar ([[GEN.38.29]]–[[GEN.38.30]]), Rahab ([[MAT.1.5]]), Rut ([[MAT.1.5]]) und die Frau des Urija ([[MAT.1.6]]); dazu Maria ([[MAT.1.16]]). Warum Matthäus sie nennt, wird verschieden erklärt: weil sie (wohl) keine Israelitinnen waren, weil ihre Verbindungen ungewöhnlich oder anstössig erschienen, oder als Vorbereitung auf die ungewöhnliche Geburt durch Maria. Die Erklärungen schliessen sich nicht aus."),
 ("MAT.1.5", "Boas", "traditional", "Βόες", None, ["Booz"],
  "Der SBLGNT schreibt mit WH und NA28 Βόες; Treg hat Βοός, RP Βοόζ. Ebenso Ἰωβήδ (RP Ὠβήδ) «Obed». Gemeint ist jeweils dieselbe Person; die Übersetzung ändert sich nicht, deshalb stehen diese Varianten nicht als Alternativen. Dass Rahab ([[JOS.2.1]]) die Frau Salmons und Mutter des Boas war, sagt nur Matthäus."),
 ("MAT.1.6", "den König David", "literal", "τὸν Δαυὶδ τὸν βασιλέα", "den David, den König", None,
  "Nur David heisst im Stammbaum «der König»; mit ihm endet der erste Teil der Zählung ([[MAT.1.17]])."),
 ("MAT.1.6", "der Frau des Urija", "adapted", "τῆς τοῦ Οὐρίου", "der des Urija", ["Batseba"],
  "Griechisch nur «der (Frau) des Urija»; «Frau» ist ergänzt. Gemeint ist Batseba ([[2SA.11.3]]), die Matthäus nicht mit Namen nennt."),
 ("MAT.1.7", "Asaf", "literal", "Ἀσάφ", None, ["Asa"],
  "Der König von Juda heisst Asa ([[1KI.15.9]]). Der SBLGNT liest mit 01, 03 und 04 (nach den CNTR-Transkriptionen) Ἀσάφ, den Namen des Psalmdichters Asaf ([[PSA.50.1]]); nach den CNTR-Texten lesen RP und KJTR sowie 032 Ἀσά. Der SBLGNT-Apparat verzeichnet hier keine Variante; deshalb steht der Befund hier und nicht als Alternative. Erklärt wird Ἀσάφ als Schreibweise, die schon in Vorlagen vorkam, als Versehen oder als bewusste Anspielung auf den Psalmdichter. Ebenso [[MAT.1.8]]."),
 ("MAT.1.8", "Joram zeugte Usija", "literal", "Ἰωρὰμ δὲ ἐγέννησεν τὸν Ὀζίαν", None, None,
  "Zwischen Joram und Usija (Asarja) nennt [[1CH.3.11]]–[[1CH.3.12]] drei weitere Könige (Ahasja, Joasch, Amazja). «Zeugte» meint hier also einen Vorfahren; die Auslassung ist eine Folge der schematischen Zählung ([[MAT.1.17]])."),
 ("MAT.1.10", "Amos", "literal", "Ἀμώς", None, ["Amon"],
  "Der König heisst Amon ([[2KI.21.18]], [[1CH.3.14]]); Ἀμώς ist die Form des Prophetennamens Amos. Die Lesart Ἀμών steht als Alternative. Erklärt wird Ἀμώς wie Asaf ([[MAT.1.7]]): als Versehen, als in Vorlagen vorgefundene Form oder als Anspielung auf einen Propheten."),
 ("MAT.1.11", "Jechonja", "traditional", "Ἰεχονίαν", None, ["Jojachin", "Konja"],
  "Jechonja ist König Jojachin ([[2KI.24.8]]; so genannt z. B. [[JER.24.1]]). Nach [[1CH.3.15]]–[[1CH.3.16]] war er ein Enkel Joschijas (Sohn Jojakims); ob Matthäus mit «Jechonja und seine Brüder» Jojakim und seine Brüder mitmeint, wird diskutiert."),
 ("MAT.1.11", "Wegführung", "literal", "μετοικεσίας", "Umsiedlung", ["Verbannung", "Exil", "Deportation"],
  "μετοικεσία heisst «Umsiedlung»; gemeint ist die Deportation nach Babylon (597/587 v. Chr.). Der Genitiv Βαβυλῶνος nennt das Ziel («nach Babylon»). Ebenso [[MAT.1.12]] und [[MAT.1.17]]."),
 ("MAT.1.16", "von der Jesus geboren wurde", "literal", "ἐξ ἧς ἐγεννήθη Ἰησοῦς", None, None,
  "Hier bricht das Muster: Statt «Josef zeugte Jesus» steht ein Passiv, und das Relativpronomen ἧς ist weiblich, bezieht sich also auf Maria. Josef ist nach dem Text Marias Mann, nicht der Erzeuger; [[MAT.1.18]]–[[MAT.1.25]] erklärt das."),
 ("MAT.1.16", "der Christus genannt wird", "literal", "ὁ λεγόμενος χριστός", None, ["der sogenannte Christus"],
  "λέγομαι heisst «genannt werden»; das Wort drückt hier keine Distanz aus. Dieselbe Wendung im Mund des Pilatus [[MAT.27.17]], [[MAT.27.22]]."),
 ("MAT.1.17", "Generationen", "literal", "γενεαὶ", None, ["Geschlechter", "Glieder"],
  "Matthäus gliedert den Stammbaum in dreimal vierzehn Generationen. Die Zählung ist schematisch: Im ersten Teil fehlen keine Glieder, im zweiten sind Könige ausgelassen ([[MAT.1.8]]), und im dritten Teil ergeben sich nur dreizehn Namen, wenn Jechonja nicht doppelt gezählt wird. Als Grund für die Zahl vierzehn wird unter anderem der Zahlenwert des Namens David im Hebräischen (D-W-D = 4+6+4) vermutet; das sagt der Text nicht."),
 ("MAT.1.18", "Ursprung", "interpretive", "γένεσις", None, ["Geburt", "Entstehung", "Herkunft"],
  "Dasselbe Wort wie in [[MAT.1.1]]. Der folgende Bericht erzählt, wie es zur Geburt kam; «Ursprung» hält die Verbindung zur Überschrift. Die Lesart γέννησις «Geburt» steht als Alternative."),
 ("MAT.1.18", "verlobt war", "literal", "μνηστευθείσης", None, ["versprochen war", "anvertraut war"],
  "Die Verlobung war nach jüdischem Recht der Zeit eine rechtlich bindende Eheschliessung, der das Zusammenleben erst folgte. Deshalb heisst Josef schon «ihr Mann» ([[MAT.1.19]]) und Maria «deine Frau» ([[MAT.1.20]]), und eine Trennung wäre eine Scheidung."),
 ("MAT.1.18", "zusammenkamen", "literal", "συνελθεῖν", None, ["zusammenzogen", "miteinander schliefen"],
  "συνέρχομαι kann das Zusammenziehen in ein Haus oder die geschlechtliche Gemeinschaft meinen; die wörtliche Wiedergabe lässt beides offen."),
 ("MAT.1.18", "schwanger war", "adapted", "ἐν γαστρὶ ἔχουσα", "im Leib habend", None,
  "Feste griechische Wendung für «schwanger sein»; ebenso [[MAT.1.23]]."),
 ("MAT.1.18", "vom heiligen Geist", "literal", "ἐκ πνεύματος ἁγίου", "aus heiligem Geist", ["vom Heiligen Geist"],
  "Grundentscheid für das ganze Evangelium: πνεῦμα ἅγιον «heiliger Geist», das Adjektiv klein, weil das Griechische hier ohne Artikel steht und keine Grossschreibung kennt. ἐκ nennt den Ursprung. Ebenso [[MAT.1.20]]."),
 ("MAT.1.19", "der gerecht war", "interpretive", "δίκαιος ὢν", "gerecht seiend", ["weil er gerecht war", "obwohl er gerecht war", "fromm"],
  "Grundentscheid: δίκαιος «gerecht», δικαιοσύνη «Gerechtigkeit» (nach MACULA-Lemma 17- bzw. 7-mal im Evangelium, ein Leitwort, vgl. [[MAT.3.15]], [[MAT.5.6]], [[MAT.5.20]]). Das Partizip lässt offen, ob Josef sich trennen will, weil er gerecht ist (gesetzestreu, vgl. [[DEU.22.20]]–[[DEU.22.24]]), oder ob er gerade als Gerechter Maria schonen will. Die Relativform «der gerecht war» lässt beides stehen."),
 ("MAT.1.19", "blossstellen", "literal", "δειγματίσαι", None, ["öffentlich beschämen", "anprangern"],
  "δειγματίζω heisst «zur Schau stellen»; gemeint ist wohl ein öffentliches Verfahren. Die Lesart παραδειγματίσαι steht als Alternative."),
 ("MAT.1.19", "sich heimlich von ihr zu trennen", "adapted", "λάθρᾳ ἀπολῦσαι αὐτήν", "sie heimlich zu entlassen", ["sich in aller Stille von ihr zu scheiden"],
  "ἀπολύω ist bei Matthäus das Wort für die Entlassung einer Frau aus der Ehe ([[MAT.5.31]]–[[MAT.5.32]], [[MAT.19.3]]). «Heimlich» meint wohl eine Scheidung ohne öffentliche Anklage."),
 ("MAT.1.20", "siehe", "traditional", "ἰδοὺ", None, ["da", "auf einmal", "schau"],
  "Grundentscheid für das ganze Evangelium: ἰδού «siehe» (Mundart «lueg»). Matthäus braucht es nach MACULA-Lemma 62-mal, oft wie hier, um ein neues Geschehen einzuführen. «Siehe» ist altertümlich, macht aber das wiederkehrende Signalwort sichtbar; wo es mitten im Satz steht, ist «da» ergänzt."),
 ("MAT.1.20", "ein Engel des Herrn", "literal", "ἄγγελος κυρίου", None, ["ein Bote des Herrn", "der Engel des Herrn"],
  "ἄγγελος heisst «Bote»; κύριος steht in der Septuaginta für den Gottesnamen. Ohne Artikel: «ein Engel». Ebenso [[MAT.1.24]], [[MAT.2.13]], [[MAT.2.19]]."),
 ("MAT.1.20", "im Traum", "literal", "κατʼ ὄναρ", None, None,
  "κατʼ ὄναρ steht im Neuen Testament nur bei Matthäus (nach MACULA-Lemma 6-mal: [[MAT.1.20]], [[MAT.2.12]], [[MAT.2.13]], [[MAT.2.19]], [[MAT.2.22]], [[MAT.27.19]]). Die Träume führen Josef und die Sterndeuter durch die ganze Vorgeschichte."),
 ("MAT.1.20", "zu dir zu nehmen", "literal", "παραλαβεῖν", None, ["heimzuführen", "zu dir zu holen"],
  "παραλαμβάνω «zu sich nehmen» meint hier die Heimholung der Frau in das Haus des Mannes. Dasselbe Verb in [[MAT.1.24]] und für das Kind und seine Mutter in [[MAT.2.13]]–[[MAT.2.14]], [[MAT.2.20]]–[[MAT.2.21]]."),
 ("MAT.1.20", "gezeugt ist", "literal", "γεννηθὲν", None, ["empfangen ist", "entstanden ist"],
  "Dasselbe Verb γεννάω wie im Stammbaum, hier im Passiv: «das in ihr Gezeugte»."),
 ("MAT.1.21", "du sollst ihm den Namen Jesus geben", "adapted", "καλέσεις τὸ ὄνομα αὐτοῦ Ἰησοῦν", "du wirst seinen Namen Jesus rufen", ["du sollst ihn Jesus nennen"],
  "Das Futur hat hier die Kraft einer Anweisung. Ἰησοῦς ist die griechische Form des hebräischen Namens Jeschua (Jehoschua, Josua), der etwa «JHWH rettet» bedeutet; der Nachsatz «denn er wird sein Volk … retten» spielt darauf an. Die Anspielung ist nur im Hebräischen hörbar. Ebenso [[MAT.1.25]]."),
 ("MAT.1.21", "retten", "literal", "σώσει", None, ["erretten", "erlösen", "heilen"],
  "Grundentscheid: σῴζω «retten» (nach MACULA-Lemma 15-mal im Evangelium). Matthäus braucht das Wort auch für Heilung ([[MAT.9.21]]–[[MAT.9.22]]) und Rettung aus Gefahr ([[MAT.8.25]]); «retten» deckt das ab. «Sein Volk» ist zunächst Israel (vgl. [[MAT.2.6]])."),
 ("MAT.1.22", "damit erfüllt würde, was vom Herrn durch den Propheten gesagt ist", "literal", "ἵνα πληρωθῇ τὸ ῥηθὲν ὑπὸ κυρίου διὰ τοῦ προφήτου", None, ["damit sich erfüllte, was der Herr durch den Propheten gesagt hat"],
  "Grundentscheid für das ganze Evangelium: einheitliche Wiedergabe der Erfüllungsformel (Mundart «damit erfüllt wird, was … dur de Prophet gseit worden isch»). Matthäus leitet so etwa zehn Schriftzitate ein (hier, [[MAT.2.15]], [[MAT.2.17]], [[MAT.2.23]], [[MAT.4.14]] usw.). ὑπό nennt Gott als Sprecher, διά den Propheten als Mittler. Ob ἵνα den Zweck («damit») oder die Folge meint, wird diskutiert; die Übersetzung bleibt bei «damit». Ob [[MAT.1.22]]–[[MAT.1.23]] noch Rede des Engels oder Bemerkung des Erzählers ist, lässt der Text offen; die Übersetzung schliesst die Rede des Engels mit [[MAT.1.21]]."),
 ("MAT.1.23", "die Jungfrau", "interpretive", "ἡ παρθένος", None, ["die junge Frau", "das Mädchen"],
  "Zitat aus [[ISA.7.14]] im Wortlaut der Septuaginta, die παρθένος hat; der hebräische Text hat ʿalmāh «junge Frau (im heiratsfähigen Alter)». Im Zusammenhang bei Matthäus ([[MAT.1.18]], [[MAT.1.25]]) ist eine Jungfrau gemeint; was das Wort bei Jesaja meint, ist umstritten."),
 ("MAT.1.23", "man wird ihm den Namen Immanuel geben", "adapted", "καλέσουσιν τὸ ὄνομα αὐτοῦ Ἐμμανουήλ", "sie werden seinen Namen Immanuel rufen", None,
  "Die verbreiteten Ausgaben der Septuaginta lesen καλέσεις «du wirst nennen», Matthäus hat den Plural «sie werden nennen», hier unpersönlich wiedergegeben. Immanuel ist hebräisch und heisst «mit uns (ist) Gott»; Matthäus übersetzt es selbst."),
 ("MAT.1.23", "Gott mit uns", "literal", "Μεθʼ ἡμῶν ὁ θεός", "Mit uns der Gott", ["Gott ist mit uns"],
  "Die Verheissung «mit uns» rahmt das Evangelium: Am Schluss sagt Jesus «Ich bin mit euch alle Tage» ([[MAT.28.20]])."),
 ("MAT.1.24", "erwachte", "literal", "ἐγερθεὶς", "aufgestanden", ["aufstand"],
  "ἐγείρω heisst «aufstehen, aufwachen»; mit «vom Schlaf» hier «erwachte». In [[MAT.2.13]]–[[MAT.2.14]] und [[MAT.2.20]]–[[MAT.2.21]] «steh auf», «stand auf»."),
 ("MAT.1.25", "er schlief nicht mit ihr", "adapted", "οὐκ ἐγίνωσκεν αὐτὴν", "er erkannte sie nicht", ["er hatte keinen Verkehr mit ihr"],
  "«Erkennen» ist eine biblische Umschreibung für die geschlechtliche Gemeinschaft (vgl. [[GEN.4.1]]); die wörtliche Form wäre heute missverständlich. Das Imperfekt bezeichnet die Dauer. ἕως οὗ «bis» sagt nach dem Wortlaut nichts darüber, was danach war; ob es spätere Gemeinschaft nahelegt (vgl. die Brüder Jesu, [[MAT.13.55]]) oder offen lässt, beurteilen die kirchlichen Traditionen verschieden."),
 ("MAT.2.1", "Sterndeuter", "interpretive", "μάγοι", None, ["Magier", "Weise", "Astrologen"],
  "μάγος bezeichnet ursprünglich Angehörige einer persischen Priesterschaft, dann Kundige der Sterne und Träume, auch Zauberer (so [[ACT.13.6]]). Weil sie einen Stern deuten, steht «Sterndeuter». Ihre Zahl nennt der Text nicht (die Dreizahl wird aus den drei Gaben erschlossen); dass sie Könige waren, ist spätere Deutung, etwa nach [[PSA.72.10]]–[[PSA.72.11]] und [[ISA.60.3]]."),
 ("MAT.2.1", "des Königs Herodes", "literal", "Ἡρῴδου τοῦ βασιλέως", None, None,
  "Gemeint ist Herodes der Grosse, nach verbreiteter Datierung gestorben 4 v. Chr."),
 ("MAT.2.2", "bei seinem Aufgang", "interpretive", "ἐν τῇ ἀνατολῇ", "im Aufgang", ["im Osten", "im Morgenland"],
  "In [[MAT.2.1]] steht der Plural ἀπὸ ἀνατολῶν «aus dem Osten»; hier der Singular mit Artikel, der auch das Aufgehen eines Gestirns bezeichnet. Viele übersetzen «im Osten», doch die Sterndeuter ziehen nach Westen, und in [[MAT.2.9]] geht der Stern vor ihnen her nach Süden. Die Übersetzung wählt «bei seinem Aufgang»; ebenso [[MAT.2.9]]."),
 ("MAT.2.2", "zu huldigen", "interpretive", "προσκυνῆσαι", "sich niederzuwerfen", ["anzubeten", "die Ehre zu erweisen"],
  "Vorschlag als Grundentscheid für das ganze Evangelium: προσκυνέω (nach MACULA-Lemma 13-mal) «huldigen», «anbeten» nur, wo Gott ausdrücklich der Empfänger ist ([[MAT.4.10]]). Das Wort bezeichnet das Niederfallen vor einem König oder vor Gott; bei Matthäus wird Jesus oft so geehrt ([[MAT.2.11]], [[MAT.14.33]], [[MAT.28.9]], [[MAT.28.17]]). «Huldigen» lässt offen, wie weit die Verehrung reicht. Ebenso [[MAT.2.8]], [[MAT.2.11]]."),
 ("MAT.2.2", "König der Juden", "literal", "βασιλεὺς τῶν Ἰουδαίων", None, None,
  "Der Titel kehrt erst in der Passion wieder, im Mund des Pilatus, der Soldaten und in der Kreuzesinschrift ([[MAT.27.11]], [[MAT.27.29]], [[MAT.27.37]]). «Die Juden» steht wörtlich und ohne Wertung; hier sprechen Fremde von Israels König."),
 ("MAT.2.3", "erschrak er", "adapted", "ἐταράχθη", "wurde er erschüttert", ["geriet er in Aufregung", "wurde er bestürzt"], None),
 ("MAT.2.4", "Hohepriester und Schriftgelehrten des Volkes", "literal", "ἀρχιερεῖς καὶ γραμματεῖς τοῦ λαοῦ", None, None,
  "Einheitliche Begriffe für das ganze Evangelium: ἀρχιερεῖς «Hohepriester» (der amtierende Hohepriester und die führenden Priester), γραμματεῖς «Schriftgelehrte» (Kundige der Schrift und des Gesetzes). Beides neutral wiedergegeben."),
 ("MAT.2.6", "unter den Fürsten Judas", "interpretive", "ἐν τοῖς ἡγεμόσιν Ἰούδα", None, ["unter den Fürstenstädten Judas", "unter den Gauen Judas"],
  "Das Zitat verbindet [[MIC.5.2]] mit [[2SA.5.2]] («du sollst mein Volk Israel weiden»). Bei Micha heisst es hebräisch «klein unter den Tausendschaften Judas», in der Septuaginta «unter den Tausendschaften»; Matthäus hat ἡγεμόσιν «Fürsten» und kehrt die Aussage um: «keineswegs die geringste». Ob er eine andere Lesung des hebräischen Wortes voraussetzt oder bewusst deutet, ist offen. Die Fürsten stehen wohl für die Orte, die sie vertreten."),
 ("MAT.2.6", "weiden wird", "literal", "ποιμανεῖ", None, ["hüten wird", "führen wird"],
  "ποιμαίνω «als Hirt weiden»; das Bild des Königs als Hirt stammt aus [[2SA.5.2]]."),
 ("MAT.2.7", "Da", "traditional", "Τότε", "Dann", None,
  "Grundentscheid für das ganze Evangelium: erzählendes τότε (nach MACULA-Lemma 90-mal, typisch für Matthäus) «da» bzw. «dann», in der Mundart «dänn». Ebenso [[MAT.2.16]], [[MAT.2.17]]."),
 ("MAT.2.8", "dem Kind", "literal", "τοῦ παιδίου", None, ["dem Kindlein", "dem kleinen Kind"],
  "παιδίον ist eine Verkleinerungsform, meint aber einfach ein kleines Kind; «Kind» durchgehend in Kapitel 2 (nach MACULA-Lemma 18-mal im Evangelium)."),
 ("MAT.2.10", "mit sehr grosser Freude", "literal", "ἐχάρησαν χαρὰν μεγάλην σφόδρα", "sie freuten sich eine sehr grosse Freude", ["freuten sie sich überaus"],
  "Verb und Nomen vom selben Stamm (χαίρω, χαρά), verstärkt durch «gross» und «sehr»; die Häufung ist beibehalten."),
 ("MAT.2.11", "das Haus", "literal", "τὴν οἰκίαν", None, None,
  "Matthäus spricht von einem Haus; von Stall und Krippe erzählt nur Lukas ([[LUK.2.7]])."),
 ("MAT.2.11", "Schatztruhen", "adapted", "θησαυροὺς", "Schätze", ["Schatzkästchen", "Behälter"],
  "θησαυρός meint den Schatz und den Ort, wo er aufbewahrt wird; beim Öffnen sind die Behälter gemeint."),
 ("MAT.2.12", "die Weisung erhalten hatten", "interpretive", "χρηματισθέντες", None, ["angewiesen worden waren", "gewarnt worden waren"],
  "χρηματίζω im Passiv heisst «eine (göttliche) Weisung erhalten». Ebenso [[MAT.2.22]]."),
 ("MAT.2.12", "zogen sie sich", "literal", "ἀνεχώρησαν", None, ["kehrten sie zurück", "zogen sie weg"],
  "Vorschlag als Grundentscheid für das ganze Evangelium: ἀναχωρέω «sich zurückziehen» (nach MACULA-Lemma 10-mal: viermal in Kapitel 2, dann z. B. [[MAT.4.12]], [[MAT.12.15]], [[MAT.14.13]]). Das Wort bezeichnet bei Matthäus oft das Ausweichen vor Gefahr."),
 ("MAT.2.13", "erscheint", "literal", "φαίνεται", None, ["erschien"],
  "Erzählendes Präsens, beibehalten (ebenso «sagt»); ebenso [[MAT.2.19]]."),
 ("MAT.2.13", "umzubringen", "literal", "ἀπολέσαι", None, ["zu vernichten", "zu töten"], None),
 ("MAT.2.15", "Aus Ägypten habe ich meinen Sohn gerufen", "literal", "Ἐξ Αἰγύπτου ἐκάλεσα τὸν υἱόν μου", None, None,
  "Zitat aus [[HOS.11.1]], wo Gott vom Volk Israel als seinem Sohn spricht. Matthäus folgt dem hebräischen Wortlaut; die Septuaginta hat «seine Kinder»."),
 ("MAT.2.15", "er blieb", "adapted", "ἦν", "er war", None, None),
 ("MAT.2.16", "hintergangen worden war", "adapted", "ἐνεπαίχθη", "verspottet worden war", ["getäuscht worden war", "zum Narren gehalten worden war"],
  "ἐμπαίζω heisst «verspotten, zum Narren halten»; bei Matthäus sonst vom Spott über Jesus in der Passion ([[MAT.20.19]], [[MAT.27.29]], [[MAT.27.31]], [[MAT.27.41]]). Hier aus der Sicht des Herodes: Er sieht sich hintergangen."),
 ("MAT.2.16", "töten", "adapted", "ἀνεῖλεν", "tötete", None,
  "Herodes tötet nicht selbst; ἀποστείλας «er sandte (Leute)» zeigt, dass er töten liess."),
 ("MAT.2.16", "Knaben", "literal", "παῖδας", None, ["Kinder", "Jungen"],
  "Männliche Form; παῖς kann allgemein «Kind» heissen, im Zusammenhang (die Suche nach dem neugeborenen König) sind Knaben gemeint."),
 ("MAT.2.17", "Da wurde erfüllt", "literal", "τότε ἐπληρώθη", None, None,
  "Anders als in [[MAT.1.22]], [[MAT.2.15]] und [[MAT.2.23]] fehlt hier ἵνα «damit» (ebenso [[MAT.27.9]] beim Tod des Judas). Viele sehen darin Absicht: Der Kindermord wird nicht als Zweck Gottes dargestellt."),
 ("MAT.2.18", "beweinte", "adapted", "κλαίουσα", "beweinend", ["weint um"],
  "Das Partizip ist als Hauptverb wiedergegeben. Zitat aus [[JER.31.15]]: Rahel, die Stammmutter, beweint die Weggeführten. Ihr Grab wurde bei Betlehem ([[GEN.35.19]]) und im Gebiet Benjamins ([[1SA.10.2]]) überliefert; Rama liegt nördlich von Jerusalem."),
 ("MAT.2.18", "nicht mehr", "adapted", "οὐκ εἰσίν", "sie sind nicht", None, "Gemeint ist: Sie leben nicht mehr."),
 ("MAT.2.20", "nach dem Leben trachteten", "adapted", "ζητοῦντες τὴν ψυχὴν", "die Seele suchten", ["töten wollten"],
  "Hebräisch geprägte Wendung. Der Plural (obwohl nur Herodes genannt ist) und der Wortlaut erinnern an Gottes Wort an Mose in [[EXO.4.19]] («alle sind gestorben, die dir nach dem Leben trachteten»)."),
 ("MAT.2.22", "als König herrschte", "literal", "βασιλεύει", "herrscht als König", ["regierte"],
  "Präsens der indirekten Rede, im Deutschen als Vergangenheit. Archelaus, ein Sohn des Herodes, herrschte über Judäa (nach Josephus mit dem Titel Ethnarch, nicht König)."),
 ("MAT.2.23", "Er wird Nazoräer genannt werden", "interpretive", "ὅτι Ναζωραῖος κληθήσεται", None, ["dass er Nazoräer genannt werde", "Er wird Nazarener heissen"],
  "Ein Prophetenwort mit diesem Wortlaut gibt es im Alten Testament nicht; Matthäus sagt auch nur allgemein «durch die Propheten». Erklärt wird der Bezug verschieden: über das hebräische nēṣer «Spross» ([[ISA.11.1]]), über nāzîr «Gottgeweihter, Nasiräer» ([[JDG.13.5]], [[JDG.13.7]]) oder über die Geringschätzung Nazarets (vgl. [[JHN.1.46]]). ὅτι kann ein Zitat oder eine indirekte Rede einleiten; die Übersetzung setzt einen Doppelpunkt ohne Anführungszeichen. Ναζωραῖος «Nazoräer» (so auch [[MAT.26.71]]) bleibt als Wort stehen, damit der Bezug zu Nazaret und die möglichen Anklänge sichtbar bleiben."),
]

DEC_GSW = [
 ("MAT.1.1", "Buech vom Ursprung", "interpretive", "Βίβλος γενέσεως", None, ["Stammbaum", "Gschicht"],
  "βίβλος γενέσεως staat i de Septuaginta au i [[GEN.2.4]] und [[GEN.5.1]]. Öb d Überschrift nu de Stammbaum, di ganz Vorgschicht oder s ganz Buech meint, isch offe. γένεσις i [[MAT.1.18]] au «Ursprung»."),
 ("MAT.1.1", "Christus", "traditional", "χριστοῦ", "Gsalbte", ["Messias"],
  "Grundentscheid fürs ganz Evangelium: Χριστός «Christus», s griechisch Wort für «Gsalbte» (Messias). Mit Artikel isch es en Titel: «de Christus» ([[MAT.1.17]], [[MAT.2.4]])."),
 ("MAT.1.2", "de Vatter vom Isaak worde", "adapted", "ἐγέννησεν τὸν Ἰσαάκ", "hät de Isaak zeugt", ["hät de Isaak übercho"],
  "ἐγέννησεν «zeugte» staat im Stammbaum 39-mal. Im Züritüütsch seit mer das nöd eso; drum «isch de Vatter vo … worde». S Verb chunnt so drümal i jedem Glid vor («isch … de Vatter … worde»). S reihend δέ isch nöd eigens widergää."),
 ("MAT.1.3", "vo de Tamar", "literal", "ἐκ τῆς Θαμάρ", None, ["mit de Tamar"],
  "ἐκ nännt d Mueter. De Stammbaum nännt vier Fraue: d Tamar, d Rahab, d Rut und d Frau vom Urija, und dänn d Maria. Werum, wird verschiede erklärt: wil si (wohl) kei Israelitinne gsii sind, wil iri Verbindige ungwöhnlich gsii sind, oder als Vorbereitig uf di ungwöhnlich Geburt dur d Maria."),
 ("MAT.1.3", "Hezron", "traditional", "Ἑσρώμ", "Esrom", None,
  "D Näme stönd i de Form, wo mer vom Alte Teschtament här kännt (Loccumer Richtlinie), mit Artikel. Usnahme: Asaf ([[MAT.1.7]]) und Amos ([[MAT.1.10]])."),
 ("MAT.1.6", "vo de Frau vom Urija", "adapted", "τῆς τοῦ Οὐρίου", "vo dere vom Urija", ["vo de Batseba"],
  "«Frau» isch ergänzt; gmeint isch d Batseba ([[2SA.11.3]])."),
 ("MAT.1.7", "Asaf", "literal", "Ἀσάφ", None, ["Asa"],
  "De König heisst Asa ([[1KI.15.9]]); de SBLGNT list Ἀσάφ, de Name vom Psalmdichter. De SBLGNT-Apparat hät kei Variante; nach de CNTR-Text läsed RP und KJTR Ἀσά."),
 ("MAT.1.10", "Amos", "literal", "Ἀμώς", None, ["Amon"],
  "De König heisst Amon ([[2KI.21.18]]); Ἀμώς isch de Name vom Prophet. D Läsart Ἀμών staat als Alternative."),
 ("MAT.1.11", "Wägfüerig", "literal", "μετοικεσίας", "Umsidlig", ["Verbannig", "Exil"],
  "Gmeint isch d Deportation uf Babylon."),
 ("MAT.1.16", "vo ire isch de Jesus gebore worde", "literal", "ἐξ ἧς ἐγεννήθη Ἰησοῦς", None, None,
  "Da bricht s Muster: Passiv, und s Relativwort ἧς isch wiiblich, meint also d Maria. De Josef isch ire Maa, nöd de Vatter, wo zeugt hät."),
 ("MAT.1.18", "Ursprung", "interpretive", "γένεσις", None, ["Geburt", "Entstehig"],
  "Glich wie i [[MAT.1.1]]. D Läsart γέννησις «Geburt» staat als Alternative."),
 ("MAT.1.18", "verlobt gsii isch", "literal", "μνηστευθείσης", None, None,
  "D Verlobig isch rächtlich scho e Ehe gsii; s Zämeläbe isch erscht spööter choo. Drum heisst de Josef «ire Maa» und d Maria «dini Frau»."),
 ("MAT.1.18", "schwanger isch", "adapted", "ἐν γαστρὶ ἔχουσα", "im Buuch hät", None, "Feschti griechischi Wändig für «schwanger sii»."),
 ("MAT.1.18", "vom heilige Geischt", "literal", "ἐκ πνεύματος ἁγίου", None, None,
  "Grundentscheid: πνεῦμα ἅγιον «heilige Geischt»."),
 ("MAT.1.19", "grächt", "interpretive", "δίκαιος", None, ["fromm"],
  "Grundentscheid: δίκαιος «grächt», δικαιοσύνη «Grächtigkeit». Öb de Josef sich trännt, wil er grächt isch, oder öb er als Grächte d Maria wott schone, laat de Text offe."),
 ("MAT.1.19", "sich heimlich vo ire z trenne", "adapted", "λάθρᾳ ἀπολῦσαι αὐτήν", "si heimlich z entlaa", ["sich vo ire scheide"],
  "ἀπολύω isch bim Matthäus s Wort für d Scheidig ([[MAT.5.31]]–[[MAT.5.32]], [[MAT.19.3]])."),
 ("MAT.1.20", "lueg", "traditional", "ἰδοὺ", "lueg emal", ["da", "uf eimal"],
  "Grundentscheid fürs ganz Evangelium: ἰδού «lueg» (Hochdüütsch «siehe»); bim Matthäus 62-mal."),
 ("MAT.1.20", "empfange worde isch", "adapted", "γεννηθὲν", "zeugt worde isch", None,
  "Glich Verb wie im Stammbaum, im Passiv."),
 ("MAT.1.21", "übercho", "adapted", "τέξεται", "gebäre", ["uf d Wält bringe"],
  "Im Züritüütsch seit mer «es Chind übercho». Ebeso [[MAT.1.23]], [[MAT.1.25]]."),
 ("MAT.1.21", "du söllsch ihm de Name Jesus gää", "adapted", "καλέσεις τὸ ὄνομα αὐτοῦ Ἰησοῦν", "du wirsch sin Name Jesus rüefe", None,
  "S Futur isch en Uftrag. Jesus isch di griechisch Form vom hebräische Name Jeschua, öppe «JHWH rettet»; de Nachsatz spilt druf aa."),
 ("MAT.1.22", "damit erfüllt wird, was vom Herr dur de Prophet gseit worden isch", "literal", "ἵνα πληρωθῇ τὸ ῥηθὲν ὑπὸ κυρίου διὰ τοῦ προφήτου", None, None,
  "Grundentscheid fürs ganz Evangelium: di einheitlich Erfüllungsformle. Öb [[MAT.1.22]]–[[MAT.1.23]] no de Ängel redt oder de Erzäler, laat de Text offe."),
 ("MAT.1.23", "d Jungfrau", "interpretive", "ἡ παρθένος", None, ["di jung Frau"],
  "Zitat us [[ISA.7.14]] nach de Septuaginta (παρθένος); im hebräische Text staat «di jung Frau». Bim Matthäus isch e Jungfrau gmeint."),
 ("MAT.1.25", "er hät nöd mit ire gschlafe", "adapted", "οὐκ ἐγίνωσκεν αὐτὴν", "er hät si nöd erchännt", None,
  "«Erchänne» isch e biblischi Umschriibig für d gschlächtlich Gmeinschaft. «Bis» seit nach em Wortlaut nüüt über spööter; d Kirche beurteiled das verschiede."),
 ("MAT.2.1", "Stärndüüter", "interpretive", "μάγοι", None, ["Magier", "Wiisi"],
  "μάγος meint Kundigi vo de Stärn und Tröim, au Zauberer. Iri Zahl nännt de Text nöd; dass es König gsii sind, isch spööteri Düütig."),
 ("MAT.2.2", "bi sim Ufgang", "interpretive", "ἐν τῇ ἀνατολῇ", "im Ufgang", ["im Oste"],
  "Singular mit Artikel, anders als i [[MAT.2.1]] («us em Oste»); bezeichnet au s Ufgaa vo me Stärn. Ebeso [[MAT.2.9]]."),
 ("MAT.2.2", "huldige", "interpretive", "προσκυνῆσαι", "sich vor ihm uf de Bode wärfe", ["aabätte", "d Ehr erwiise"],
  "Vorschlag fürs ganz Evangelium: προσκυνέω «huldige», «aabätte» nu, wo Gott usdrücklich gmeint isch ([[MAT.4.10]]). Ebeso [[MAT.2.8]], [[MAT.2.11]]."),
 ("MAT.2.6", "under de Fürschte vo Juda", "interpretive", "ἐν τοῖς ἡγεμόσιν Ἰούδα", None, ["under de Gaue vo Juda"],
  "Zitat us [[MIC.5.2]] und [[2SA.5.2]]. Bim Micha heisst s «chlii under de Tuusigschafte vo Juda»; de Matthäus chehrt s um: «überhaupt nöd di chliinscht»."),
 ("MAT.2.7", "Dänn", "traditional", "Τότε", None, ["Da"],
  "Grundentscheid fürs ganz Evangelium: erzählends τότε «dänn» (90-mal)."),
 ("MAT.2.12", "d Wiisig übercho händ", "interpretive", "χρηματισθέντες", None, ["gwarnt worde sind"],
  "χρηματίζω im Passiv: e (göttlichi) Wiisig übercho. Ebeso [[MAT.2.22]]."),
 ("MAT.2.12", "zruggzoge", "literal", "ἀνεχώρησαν", None, ["zrugggange"],
  "Vorschlag fürs ganz Evangelium: ἀναχωρέω «sich zruggzie» (10-mal), oft s Uswiiche vor Gfahr."),
 ("MAT.2.16", "für dumm verchauft worde isch", "adapted", "ἐνεπαίχθη", "verspottet worde isch", ["aagloge worde isch"],
  "ἐμπαίζω «verspotte, zum Narre halte»; us de Sicht vom Herodes. S glich Verb staat i de Passion ([[MAT.27.29]])."),
 ("MAT.2.16", "Buebe", "literal", "παῖδας", None, ["Chind"],
  "Männlichi Form; im Zämehang sind Buebe gmeint."),
 ("MAT.2.18", "um iri Chind briegget", "adapted", "κλαίουσα τὰ τέκνα αὐτῆς", "brieggend um iri Chind", None,
  "S Partizip isch als Verb widergää. Zitat us [[JER.31.15]]."),
 ("MAT.2.20", "as Läbe händ wele", "adapted", "ζητοῦντες τὴν ψυχὴν", "d Seel gsuecht händ", None,
  "Hebräisch prägti Wändig; erinneret a [[EXO.4.19]] (Mose)."),
 ("MAT.2.23", "Er wird Nazoräer gnännt wärde", "interpretive", "ὅτι Ναζωραῖος κληθήσεται", None, ["dass er Nazoräer gnännt wird"],
  "Es Prophetewort mit dem Wortlaut git s im Alte Teschtament nöd. Erklärt wird s über nēṣer «Schoss» ([[ISA.11.1]]), über nāzîr «Nasiräer» ([[JDG.13.5]]) oder über de schlächt Ruef vo Nazaret ([[JHN.1.46]])."),
]

# Alternativen: (Variante:Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw,
#  Lesarten de, Lesarten gsw, Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings
#  (maschinelle Zuordnung) bzw. aus den CNTR-Transkriptionen in data/witness-texts.
ALTS = [
 ("VAR-SBLGNTAPP-MAT-001-006-01:R2", "MAT.1.6", "David zeugte Salomo", "David, der König, zeugte Salomo",
  "De David isch", "De König David isch", "gering",
  "Mit dem Zusatz heisst David auch im zweiten Glied «der König».", "Mit em Zuesatz heisst de David au im zweite Glid «de König».",
  {"R1": [("δέ", "David zeugte", "WH, Treg, NA28")], "R2": [("δὲ ὁ βασιλεύς", "David, der König, zeugte", "RP")]},
  {"R1": [("δέ", "de David", "WH, Treg, NA28")], "R2": [("δὲ ὁ βασιλεύς", "de König David", "RP")]},
  ["Der Zusatz kann den Titel aus dem Satz davor wiederholen; ebenso kann er beim Abschreiben ausgefallen sein, weil «König» unmittelbar vorher schon steht.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne Zusatz, 04 und 032 mit ihm; 05 hat hier eine Lücke."],
  ["De Zuesatz cha de Titel us em Satz devor widerhole; oder er isch bim Abschriibe usgfalle, wil «König» grad vorher scho staat.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni Zuesatz, 04 und 032 mit; 05 hät da e Lucke."]),
 ("VAR-SBLGNTAPP-MAT-001-010-01:R2", "MAT.1.10", "Manasse zeugte Amos, Amos zeugte Joschija", "Manasse zeugte Amon, Amon zeugte Joschija",
  "vom Amos worde, de Amos", "vom Amon worde, de Amon", "gering",
  "Mit Ἀμών steht der Name des Königs von Juda ([[2KI.21.18]]) statt des Prophetennamens Amos.",
  "Mit Ἀμών staat de Name vom König vo Juda ([[2KI.21.18]]) statt em Prophetename Amos.",
  {"R1": [("Ἀμώς, Ἀμώς", "Amos, Amos", "WH, Treg, NA28")], "R2": [("Ἀμών, Ἀμών", "Amon, Amon", "NIV, RP")]},
  {"R1": [("Ἀμώς, Ἀμώς", "Amos, Amos", "WH, Treg, NA28")], "R2": [("Ἀμών, Ἀμών", "Amon, Amon", "NIV, RP")]},
  ["Ἀμών kann eine Angleichung an den Königsnamen in den Königsbüchern und der Chronik sein ([[2KI.21.18]], [[1CH.3.14]]). Ἀμώς kann ein Hör- oder Schreibversehen sein, eine schon in Vorlagen vorgefundene Form oder eine Anspielung auf den Propheten (vgl. Asaf in [[MAT.1.7]]).",
   "Laut der automatischen Zuordnung lesen 01, 03 und 04 Ἀμώς, 032 Ἀμών; 05 hat hier eine Lücke."],
  ["Ἀμών cha e Aagliichig a de Königsname i de Königsbüecher und de Chronik sii. Ἀμώς cha en Hör- oder Schriibfähler sii, e Form, wo scho i Vorlage gstande isch, oder en Aaspilig uf de Prophet.",
   "Nach de automatische Zueornig läsed 01, 03 und 04 Ἀμώς, 032 Ἀμών; 05 hät da e Lucke."]),
 ("VAR-SBLGNTAPP-MAT-001-018-01:R2", "MAT.1.18", "Mit dem Ursprung Jesu Christi", "Mit dem Ursprung des Christus",
  "Mit em Ursprung vo Jesus Christus", "Mit em Ursprung vom Christus", "gering",
  "Ohne «Jesus» steht nur der Titel «der Christus», wie zuletzt in [[MAT.1.17]].",
  "Ohni «Jesus» staat nu de Titel «de Christus», wie zletscht i [[MAT.1.17]].",
  {"R1": [("Ἰησοῦ χριστοῦ", "Jesu Christi", "WH, NA28, RP")], "R2": [("χριστοῦ", "des Christus", "Treg")]},
  {"R1": [("Ἰησοῦ χριστοῦ", "vo Jesus Christus", "WH, NA28, RP")], "R2": [("χριστοῦ", "vom Christus", "Treg")]},
  ["Die kürzere Form schliesst an «bis zum Christus» in [[MAT.1.17]] an; «Jesus» kann aus [[MAT.1.1]] ergänzt sein. Ebenso kann das Wort ausgefallen sein: In den Handschriften stehen beide Namen als Kürzel (ΙΥ ΧΥ) nebeneinander.",
   "Die automatische Zuordnung führt 01, 03, 04 und 032 bei der Auslassung. Das stimmt mit den CNTR-Transkriptionen nicht überein: Danach lesen 01 und 04 Ἰησοῦ χριστοῦ, 03 umgestellt χριστοῦ Ἰησοῦ und 032 nur Ἰησοῦ (ohne «Christus»). Demnach hat keine dieser Handschriften die Lesart von Treg; die automatische Zuordnung ist hier unsicher. 05 hat eine Lücke."],
  ["Di chürzer Form schlüüsst a «bis zum Christus» i [[MAT.1.17]] aa; «Jesus» cha us [[MAT.1.1]] ergänzt sii. Oder s Wort isch usgfalle: I de Handschrifte stönd beidi Näme als Chürzel näbenand.",
   "D automatisch Zueornig füert 01, 03, 04 und 032 bi de Uslassig. Das stimmt mit de CNTR-Transkriptione nöd überii: Nach dene läsed 01 und 04 Ἰησοῦ χριστοῦ, 03 umgstellt χριστοῦ Ἰησοῦ und 032 nu Ἰησοῦ. Kei vo dene Handschrifte hät also d Läsart vom Treg; d Zueornig isch da unsicher. 05 hät e Lucke."]),
 ("VAR-SBLGNTAPP-MAT-001-018-02:R2", "MAT.1.18", "Mit dem Ursprung", "Mit der Geburt", "Mit em Ursprung", "Mit de Geburt", "gering",
  "γέννησις heisst eindeutig «Geburt»; γένεσις («Ursprung») knüpft an [[MAT.1.1]] an.",
  "γέννησις heisst eidüütig «Geburt»; γένεσις («Ursprung») knüpft a [[MAT.1.1]] aa.",
  {"R1": [("γένεσις", "Ursprung", "WH, Treg, NA28")], "R2": [("γέννησις", "Geburt", "RP")]},
  {"R1": [("γένεσις", "Ursprung", "WH, Treg, NA28")], "R2": [("γέννησις", "Geburt", "RP")]},
  ["Die Wörter unterscheiden sich in einem Buchstaben. γέννησις passt zum folgenden Bericht über die Geburt und kann ihn verdeutlichen; γένεσις kann an [[MAT.1.1]] angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01 (auch die Korrektur), 03, 04 und 032 γένεσις; 05 hat hier eine Lücke."],
  ["D Wort underscheided sich i eim Buechstabe. γέννησις passt zum Bricht über d Geburt; γένεσις cha a [[MAT.1.1]] aaglichen sii.",
   "Nach de automatische Zueornig läsed 01 (au d Korrektur), 03, 04 und 032 γένεσις; 05 hät da e Lucke."]),
 ("VAR-SBLGNTAPP-MAT-001-018-03:R2", "MAT.1.18", "Als seine Mutter", "Als nämlich seine Mutter", "Wo sini Mueter", "Wo nämli sini Mueter", "gering",
  "γάρ knüpft den Bericht ausdrücklich als Erklärung an den Einleitungssatz.",
  "γάρ hänkt de Bricht usdrücklich als Erkläärig a de Iileitigssatz.",
  {"R1": [("μνηστευθείσης", "Als … verlobt war", "WH, Treg, NA28")], "R2": [("μνηστευθείσης γάρ", "Als nämlich … verlobt war", "RP")]},
  {"R1": [("μνηστευθείσης", "Wo … verlobt gsii isch", "WH, Treg, NA28")], "R2": [("μνηστευθείσης γάρ", "Wo nämli … verlobt gsii isch", "RP")]},
  ["γάρ kann zur Verdeutlichung des Anschlusses ergänzt worden sein; ebenso kann das kleine Wort beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 (auch die Korrektur), 03 und 04 ohne γάρ, 032 mit ihm; 05 hat hier eine Lücke."],
  ["γάρ cha zur Verdüütlichung ergänzt worde sii; oder s chlii Wort isch bim Abschriibe usgfalle.",
   "Nach de automatische Zueornig läsed 01 (au d Korrektur), 03 und 04 ohni γάρ, 032 mit; 05 hät da e Lucke."]),
 ("VAR-SBLGNTAPP-MAT-001-019-01:R2", "MAT.1.19", "sie nicht blossstellen wollte", "sie nicht öffentlich an den Pranger stellen wollte",
  "si nöd hät wele blossstelle", "si nöd hät wele öffetlich a de Pranger stelle", "gering",
  "παραδειγματίζω betont das öffentliche, abschreckende Vorführen.",
  "παραδειγματίζω betont s öffetlich, abschreckend Vorfüere.",
  {"R1": [("δειγματίσαι", "blossstellen", "WH, Treg, NA28")], "R2": [("παραδειγματίσαι", "öffentlich an den Pranger stellen", "RP")]},
  {"R1": [("δειγματίσαι", "blossstelle", "WH, Treg, NA28")], "R2": [("παραδειγματίσαι", "öffetlich a de Pranger stelle", "RP")]},
  ["Das seltene δειγματίζω kann durch das verwandte παραδειγματίζω ersetzt worden sein oder umgekehrt; die Bedeutungen liegen nahe beieinander.",
   "Laut der automatischen Zuordnung lesen 03 und die Korrektur in 01 δειγματίσαι, die Erstschrift von 01 sowie 04 und 032 παραδειγματίσαι; 05 hat hier eine Lücke."],
  ["S sälte δειγματίζω cha dur s verwandt παραδειγματίζω ersetzt worde sii oder umgekehrt; d Bedüütige liged nöch binenand.",
   "Nach de automatische Zueornig läsed 03 und d Korrektur i 01 δειγματίσαι, d Erschtschrift vo 01, 04 und 032 παραδειγματίσαι; 05 hät da e Lucke."]),
 ("VAR-SBLGNTAPP-MAT-001-025-01:R2", "MAT.1.25", "bis sie einen Sohn geboren hatte", "bis sie ihren erstgeborenen Sohn geboren hatte",
  "bis si en Sohn übercho hät", "bis si iren erschtgeborne Sohn übercho hät", "mittel",
  "Der Zusatz nennt Jesus den Erstgeborenen Marias (vgl. [[LUK.2.7]]).",
  "De Zuesatz nännt de Jesus de Erschtgeborni vo de Maria (vgl. [[LUK.2.7]]).",
  {"R1": [("υἱόν", "einen Sohn", "WH, Treg, NA28")], "R2": [("τὸν υἱὸν αὐτῆς τὸν πρωτότοκον", "ihren erstgeborenen Sohn", "RP")]},
  {"R1": [("υἱόν", "en Sohn", "WH, Treg, NA28")], "R2": [("τὸν υἱὸν αὐτῆς τὸν πρωτότοκον", "iren erschtgeborne Sohn", "RP")]},
  ["Der Zusatz kann aus [[LUK.2.7]] übernommen sein; ebenso wird vermutet, er sei weggelassen worden, weil «erstgeboren» weitere Kinder Marias nahelegen konnte.",
   "Laut der automatischen Zuordnung lesen 01 und 03 nur υἱόν, 04, 05 und 032 den Zusatz."],
  ["De Zuesatz cha us [[LUK.2.7]] übernoo sii; oder er isch wäggloo worde, wil «erschtgebore» wiiteri Chind vo de Maria cha nöchlegge.",
   "Nach de automatische Zueornig läsed 01 und 03 nu υἱόν, 04, 05 und 032 de Zuesatz."]),
 ("VAR-SBLGNTAPP-MAT-002-017-01:R2", "MAT.2.17", "was durch Jeremia, den Propheten, gesagt ist", "was von Jeremia, dem Propheten, gesagt ist",
  "was dur de Jeremia, de Prophet, gseit worden isch", "was vom Jeremia, em Prophet, gseit worden isch", "gering",
  "Mit ὑπό ist Jeremia der Sprecher, nicht der Mittler; sonst nennt die Formel mit ὑπό den Herrn und mit διά den Propheten ([[MAT.1.22]], [[MAT.2.15]]).",
  "Mit ὑπό isch de Jeremia de Sprächer, nöd de Mittler; susch nännt d Formle mit ὑπό de Herr und mit διά de Prophet ([[MAT.1.22]], [[MAT.2.15]]).",
  {"R1": [("διά", "durch", "WH, Treg, NA28")], "R2": [("ὑπό", "von", "RP")]},
  {"R1": [("διά", "dur", "WH, Treg, NA28")], "R2": [("ὑπό", "vo", "RP")]},
  ["Ein Wechsel der kurzen Präpositionen ist beim Abschreiben leicht möglich; διά entspricht der festen Formel des Evangeliums, ὑπό kann aus [[MAT.1.22]] und [[MAT.2.15]] eingedrungen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 032 διά, 05 ὑπό. Nach der CNTR-Transkription hat 05 aber ὑπὸ κυρίου διά («vom Herrn durch»), also beides; die Zuordnung von 05 ist deshalb unsicher."],
  ["En Wächsel vo de churze Präpositione passiert bim Abschriibe liecht; διά entspricht de feschte Formle vom Evangelium.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 032 διά, 05 ὑπό. Nach de CNTR-Transkription hät 05 aber ὑπὸ κυρίου διά («vom Herr dur»), also beides; d Zueornig vo 05 isch drum unsicher."]),
 ("VAR-SBLGNTAPP-MAT-002-018-01:R2", "MAT.2.18", "Weinen und viel Wehklagen", "Totenklage und Weinen und viel Wehklagen",
  "Briegge und vil Jammer", "Totechlag und Briegge und vil Jammer", "gering",
  "Der Zusatz θρῆνος («Totenklage») entspricht dem Wortlaut der Septuaginta in [[JER.31.15]] (dort Kapitel 38).",
  "De Zuesatz θρῆνος («Totechlag») entspricht em Wortlaut vo de Septuaginta i [[JER.31.15]].",
  {"R1": [("ἠκούσθη", "wurde gehört", "WH, Treg, NA28")], "R2": [("ἠκούσθη θρῆνος καί", "wurde gehört, Totenklage und", "RP")]},
  {"R1": [("ἠκούσθη", "isch ghört worde", "WH, Treg, NA28")], "R2": [("ἠκούσθη θρῆνος καί", "isch ghört worde, Totechlag und", "RP")]},
  ["Der Zusatz kann den Wortlaut an die Septuaginta angleichen; ebenso könnte θρῆνος καί beim Abschreiben ausgefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 03 ohne Zusatz, 04, 05 und 032 mit ihm."],
  ["De Zuesatz cha de Wortlaut a d Septuaginta aagliiche; oder θρῆνος καί isch bim Abschriibe usgfalle.",
   "Nach de automatische Zueornig läsed 01 und 03 ohni Zuesatz, 04, 05 und 032 mit."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-001-001-025", "MAT.1.1-MAT.1.25", "section", "Stammbaum und Geburt Jesu",
  ["TU-MAT-001-001-017", "TU-MAT-001-018-025"],
  "Das Evangelium beginnt mit dem Stammbaum Jesu Christi, des Sohnes Davids, des Sohnes Abrahams: von Abraham über König David und die Wegführung nach Babylon bis zu Josef, dem Mann Marias, von der Jesus geboren wurde; der Text zählt dreimal vierzehn Generationen. Maria ist mit Josef verlobt, und noch bevor sie zusammenkommen, zeigt sich, dass sie vom heiligen Geist schwanger ist. Josef will sich heimlich von ihr trennen, doch ein Engel des Herrn sagt ihm im Traum, er solle Maria zu sich nehmen und dem Sohn den Namen Jesus geben, denn er werde sein Volk von ihren Sünden retten. Der Text sieht darin das Wort von [[ISA.7.14]] erfüllt (Immanuel, «Gott mit uns»). Josef tut, wie ihm befohlen, schläft nicht mit Maria, bis sie den Sohn geboren hat, und gibt ihm den Namen Jesus.", SEG),
 ("TU-MAT-001-001-017", "MAT.1.1-MAT.1.17", "genealogy", "Der Stammbaum Jesu Christi", None,
  "Unter der Überschrift «Buch vom Ursprung Jesu Christi, des Sohnes Davids, des Sohnes Abrahams» folgt die Stammfolge: von Abraham über Isaak, Jakob und Juda bis zu König David, von David über Salomo und die Könige Judas bis zu Jechonja zur Zeit der Wegführung nach Babylon und von dort bis zu Josef, dem Mann Marias, von der Jesus geboren wurde, der Christus genannt wird. Neben den Vätern sind Tamar, Rahab, Rut und die Frau des Urija genannt. Am Schluss zählt der Text dreimal vierzehn Generationen: von Abraham bis David, von David bis zur Wegführung nach Babylon und von dort bis zum Christus.", None),
 ("TU-MAT-001-018-025", "MAT.1.18-MAT.1.25", "narrative", "Josef und die Geburt Jesu", None,
  "Maria ist mit Josef verlobt; bevor sie zusammenkommen, zeigt sich, dass sie vom heiligen Geist schwanger ist. Josef, der gerecht ist und sie nicht blossstellen will, beschliesst, sich heimlich von ihr zu trennen. Da erscheint ihm im Traum ein Engel des Herrn: Er solle sich nicht fürchten, Maria zu sich zu nehmen, denn das in ihr Gezeugte sei vom heiligen Geist; sie werde einen Sohn gebären, dem er den Namen Jesus geben solle, denn er werde sein Volk von ihren Sünden retten. Das alles ist nach dem Text geschehen, damit sich das Prophetenwort erfüllt: Die Jungfrau wird einen Sohn gebären, den man Immanuel nennen wird, «Gott mit uns» ([[ISA.7.14]]). Josef erwacht, tut, wie ihm befohlen, und nimmt Maria zu sich; er schläft nicht mit ihr, bis sie einen Sohn geboren hat, und gibt ihm den Namen Jesus.", None),
 ("TU-MAT-002-001-023", "MAT.2.1-MAT.2.23", "section", "Die Sterndeuter, die Flucht nach Ägypten und die Rückkehr",
  ["TU-MAT-002-001-012", "TU-MAT-002-013-015", "TU-MAT-002-016-018", "TU-MAT-002-019-023"],
  "Sterndeuter aus dem Osten kommen nach Jerusalem und fragen nach dem neugeborenen König der Juden. Herodes erfährt von den Hohepriestern und Schriftgelehrten, dass der Christus nach dem Prophetenwort ([[MIC.5.2]]) in Betlehem geboren werden soll, und schickt die Sterndeuter dorthin. Der Stern führt sie zum Kind; sie huldigen ihm, bringen Gold, Weihrauch und Myrrhe und ziehen nach einer Weisung im Traum auf einem anderen Weg heim. Ein Engel des Herrn sagt Josef im Traum, er solle mit dem Kind und seiner Mutter nach Ägypten fliehen; Herodes lässt in Betlehem und Umgebung alle Knaben bis zu zwei Jahren töten. Nach dem Tod des Herodes zieht Josef auf Weisung des Engels in das Land Israel, fürchtet sich aber, nach Judäa zu gehen, wo Archelaus herrscht, und lässt sich nach einer weiteren Weisung in Nazaret in Galiläa nieder. Der Text verbindet die Stationen mit Prophetenworten ([[HOS.11.1]], [[JER.31.15]] und dem Wort, er werde Nazoräer genannt werden).", SEG),
 ("TU-MAT-002-001-012", "MAT.2.1-MAT.2.12", "narrative", "Die Sterndeuter aus dem Osten", None,
  "Nach der Geburt Jesu in Betlehem kommen Sterndeuter aus dem Osten nach Jerusalem und fragen, wo der neugeborene König der Juden sei; sie hätten seinen Stern aufgehen sehen und wollten ihm huldigen. Herodes und ganz Jerusalem erschrecken. Die Hohepriester und Schriftgelehrten nennen Herodes Betlehem und berufen sich auf den Propheten ([[MIC.5.2]]). Herodes erfragt heimlich von den Sterndeutern die Zeit, in der der Stern erschienen war, und schickt sie nach Betlehem: Sie sollen nach dem Kind forschen und es ihm melden, damit auch er komme und ihm huldige. Der Stern geht ihnen voraus und bleibt über dem Ort stehen, wo das Kind ist; sie freuen sich sehr, finden das Kind mit Maria, seiner Mutter, im Haus, fallen nieder, huldigen ihm und bringen Gold, Weihrauch und Myrrhe dar. Nach einer Weisung im Traum kehren sie nicht zu Herodes zurück, sondern ziehen auf einem anderen Weg in ihr Land.", None),
 ("TU-MAT-002-013-015", "MAT.2.13-MAT.2.15", "narrative", "Die Flucht nach Ägypten", None,
  "Ein Engel des Herrn erscheint Josef im Traum und sagt ihm, er solle mit dem Kind und seiner Mutter nach Ägypten fliehen und dort bleiben, denn Herodes werde das Kind suchen, um es umzubringen. Josef zieht sich bei Nacht mit dem Kind und seiner Mutter nach Ägypten zurück und bleibt dort bis zum Tod des Herodes. Der Text sieht darin das Wort aus [[HOS.11.1]] erfüllt: «Aus Ägypten habe ich meinen Sohn gerufen.»", None),
 ("TU-MAT-002-016-018", "MAT.2.16-MAT.2.18", "narrative", "Der Kindermord in Betlehem", None,
  "Als Herodes sieht, dass die Sterndeuter ihn hintergangen haben, wird er sehr zornig und lässt in Betlehem und Umgebung alle Knaben von zwei Jahren an und darunter töten, nach der Zeit, die er von den Sterndeutern erfragt hatte. Der Text sieht darin das Wort Jeremias erfüllt ([[JER.31.15]]): Rahel beweint ihre Kinder und will sich nicht trösten lassen, denn sie sind nicht mehr.", None),
 ("TU-MAT-002-019-023", "MAT.2.19-MAT.2.23", "narrative", "Die Rückkehr nach Nazaret", None,
  "Nach dem Tod des Herodes erscheint Josef in Ägypten ein Engel des Herrn im Traum: Er solle mit dem Kind und seiner Mutter in das Land Israel ziehen, denn die, die dem Kind nach dem Leben trachteten, seien gestorben. Josef tut es. Als er hört, dass Archelaus anstelle seines Vaters Herodes über Judäa herrscht, fürchtet er sich, dorthin zu gehen; nach einer Weisung im Traum zieht er sich nach Galiläa zurück und lässt sich in Nazaret nieder. Der Text verbindet das mit einem Wort der Propheten: Er wird Nazoräer genannt werden.", None),
]
UNITS_GSW = {
 "TU-MAT-001-001-025": ("De Stammbaum und d Geburt vom Jesus", "S Evangelium faat mit em Stammbaum vo Jesus Christus aa, em Sohn vom David, em Sohn vom Abraham: vom Abraham über de König David und d Wägfüerig uf Babylon bis zum Josef, em Maa vo de Maria, vo dere de Jesus gebore worden isch; de Text zellt drümal vierzää Generatione. D Maria isch mit em Josef verlobt, und no bevor si zämechömed, zeigt sich, dass si vom heilige Geischt schwanger isch. De Josef wott sich heimlich vo ire trenne, aber en Ängel vom Herr seit ihm im Traum, er söll d Maria zu sich neh und em Sohn de Name Jesus gää, dänn er wärdi sis Volk vo irne Sünde rette. De Text gseht drin s Wort vo [[ISA.7.14]] erfüllt (Immanuel, «Gott mit üs»). De Josef macht, wie s ihm befohle worden isch, schlaft nöd mit de Maria, bis si de Sohn übercho hät, und git ihm de Name Jesus."),
 "TU-MAT-001-001-017": ("De Stammbaum vo Jesus Christus", "Under de Überschrift «Buech vom Ursprung vo Jesus Christus, em Sohn vom David, em Sohn vom Abraham» chunnt d Stammfolg: vom Abraham über de Isaak, de Jakob und de Juda bis zum König David, vom David über de Salomo und d König vo Juda bis zum Jechonja zur Ziit vo de Wägfüerig uf Babylon und vo dört bis zum Josef, em Maa vo de Maria, vo dere de Jesus gebore worden isch, wo Christus gnännt wird. Näbe de Vätter sind d Tamar, d Rahab, d Rut und d Frau vom Urija gnännt. Am Schluss zellt de Text drümal vierzää Generatione: vom Abraham bis zum David, vom David bis zur Wägfüerig uf Babylon und vo dört bis zum Christus."),
 "TU-MAT-001-018-025": ("De Josef und d Geburt vom Jesus", "D Maria isch mit em Josef verlobt; bevor si zämechömed, zeigt sich, dass si vom heilige Geischt schwanger isch. De Josef, wo grächt isch und si nöd wott blossstelle, beschlüüsst, sich heimlich vo ire z trenne. Da erschiint ihm im Traum en Ängel vom Herr: Er söll kei Angscht ha, d Maria zu sich z neh, dänn was in ire empfange worden isch, sig vom heilige Geischt; si wärdi en Sohn übercho, und er söll ihm de Name Jesus gää, dänn er wärdi sis Volk vo irne Sünde rette. Das alles isch nach em Text gscheh, damit sich s Prophetewort erfüllt: D Jungfrau wird en Sohn übercho, und mer wird ihm de Name Immanuel gää, «Gott mit üs» ([[ISA.7.14]]). De Josef verwachet, macht, wie s ihm befohle worden isch, und nimmt d Maria zu sich; er schlaft nöd mit ire, bis si en Sohn übercho hät, und git ihm de Name Jesus."),
 "TU-MAT-002-001-023": ("D Stärndüüter, d Flucht uf Ägypte und d Heichehr", "Stärndüüter us em Oste chömed uf Jerusalem und fröged nach em neugebore König vo de Jude. De Herodes erfahrt vo de Hoheprieschter und Schriftgelehrte, dass de Christus nach em Prophetewort ([[MIC.5.2]]) z Betlehem söll gebore wärde, und schickt d Stärndüüter dörthii. De Stärn füert si zum Chind; si huldiged ihm, bringed Gold, Wiirauch und Myrrhe und zieched nach ere Wiisig im Traum uf eme andere Wäg hei. En Ängel vom Herr seit em Josef im Traum, er söll mit em Chind und sinere Mueter uf Ägypte flüchte; de Herodes laat z Betlehem und i de Umgäbig alli Buebe bis zwei Jahr umbringe. Nach em Tod vom Herodes zieht de Josef uf d Wiisig vom Ängel is Land Israel, hät aber Angscht, uf Judäa z gaa, wo de Archelaus regiert, und laat sich nach ere wiitere Wiisig z Nazaret in Galiläa nider. De Text verbindet d Station mit Propheteworte ([[HOS.11.1]], [[JER.31.15]] und em Wort, er wärdi Nazoräer gnännt)."),
 "TU-MAT-002-001-012": ("D Stärndüüter us em Oste", "Nach de Geburt vom Jesus z Betlehem chömed Stärndüüter us em Oste uf Jerusalem und fröged, wo de neugebore König vo de Jude sig; si heigid sin Stärn gseh ufgaa und wetted ihm huldige. De Herodes und ganz Jerusalem verschrecked. D Hoheprieschter und d Schriftgelehrte nänned em Herodes Betlehem und berüefed sich uf de Prophet ([[MIC.5.2]]). De Herodes fröget d Stärndüüter heimlich genau, wänn de Stärn erschiene isch, und schickt si uf Betlehem: Si söled nach em Chind forsche und s ihm mälde, demit au er chömi und ihm huldigi. De Stärn gaat ine voruus und bliibt über em Ort staa, wo s Chind isch; si fröied sich riesig, finded s Chind mit de Maria, sinere Mueter, im Huus, gönd uf d Chnü, huldiged ihm und bringed ihm Gold, Wiirauch und Myrrhe. Nach ere Wiisig im Traum gönd si nöd zum Herodes zrugg, sondern zieched uf eme andere Wäg i ires Land."),
 "TU-MAT-002-013-015": ("D Flucht uf Ägypte", "En Ängel vom Herr erschiint em Josef im Traum und seit ihm, er söll mit em Chind und sinere Mueter uf Ägypte flüchte und dört bliibe, dänn de Herodes wärdi s Chind sueche, für s umzbringe. De Josef zieht sich znacht mit em Chind und sinere Mueter uf Ägypte zrugg und bliibt dört bis zum Tod vom Herodes. De Text gseht drin s Wort us [[HOS.11.1]] erfüllt: «Us Ägypte han ich min Sohn grüeft.»"),
 "TU-MAT-002-016-018": ("De Chindermord z Betlehem", "Wo de Herodes gseht, dass en d Stärndüüter für dumm verchauft händ, wird er ganz wüetig und laat z Betlehem und i de Umgäbig alli Buebe vo zwei Jahr aa und drunder umbringe, nach de Ziit, wo er vo de Stärndüüter erfröget hät. De Text gseht drin s Wort vom Jeremia erfüllt ([[JER.31.15]]): D Rahel brieggt um iri Chind und wott sich nöd la tröschte, dänn si sind nüme."),
 "TU-MAT-002-019-023": ("D Heichehr uf Nazaret", "Nach em Tod vom Herodes erschiint em Josef in Ägypte en Ängel vom Herr im Traum: Er söll mit em Chind und sinere Mueter is Land Israel gaa, dänn die, wo em Chind as Läbe händ wele, sigid gstorbe. De Josef macht s. Wo er ghört, dass de Archelaus anstell vo sim Vatter Herodes über Judäa regiert, hät er Angscht, dörthii z gaa; nach ere Wiisig im Traum zieht er sich uf Galiläa zrugg und laat sich z Nazaret nider. De Text verbindet das mit eme Wort vo de Prophete: Er wird Nazoräer gnännt wärde."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) bzw. auf den "
  "CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung der Handschriften. "
  "In [[MAT.1.18]] (Ἰησοῦ) und [[MAT.2.17]] (05) widerspricht die automatische Zuordnung den CNTR-Transkriptionen; die "
  "Alternativen benennen das. Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts gezählt."),
 ("Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen. Die Übersetzung folgt den einheitlichen "
  "Begriffen für das ganze Matthäusevangelium; in Kapitel 1–2 kommen davon vor: Χριστός «Christus», ἰδού «siehe», τότε "
  "«da», ἀρχιερεῖς und γραμματεῖς «Hohepriester», «Schriftgelehrte», πνεῦμα ἅγιον «heiliger Geist», die Erfüllungsformel "
  "«damit erfüllt würde, was … durch den Propheten gesagt ist:» und die Ortsnamen (Betlehem, Jerusalem, Judäa, Galiläa, Nazaret)."),
 ("In diesem Bereich neu festgelegt (Vorschlag für das ganze Evangelium, jeweils mit decision): προσκυνέω «huldigen», "
  "«anbeten» nur mit Gott als Empfänger; ἀναχωρέω «sich zurückziehen»; κατʼ ὄναρ «im Traum»; χρηματίζω (Passiv) «eine "
  "Weisung erhalten»; παιδίον «Kind»; δίκαιος / δικαιοσύνη «gerecht» / «Gerechtigkeit»; σῴζω «retten»; ἄγγελος κυρίου "
  "«ein Engel des Herrn»; παραλαμβάνω «zu sich nehmen»; γεννάω aktiv «zeugen», passiv «geboren werden»; μάγοι "
  "«Sterndeuter»; Ναζωραῖος «Nazoräer»; ἐμπαίζω «verspotten» (in [[MAT.2.16]] aus der Sicht des Herodes «hintergangen»)."),
 ("Namen: in der aus dem Alten Testament vertrauten Form (Loccumer Richtlinien), z. B. Hezron, Ram, Nachschon, Boas, Obed, "
  "Isai, Usija, Hiskija, Joschija, Jechonja, Schealtiël, Serubbabel; Ausnahmen Asaf ([[MAT.1.7]]–[[MAT.1.8]]) und Amos "
  "([[MAT.1.10]]), wo die griechische Form einen anderen Namen ergibt als den des Königs."),
 ("Stammbaum ([[MAT.1.2]]–[[MAT.1.16]]): ἐγέννησεν «zeugte» (39-mal); der Artikel vor den Namen ist mit dem Namen "
  "zugeordnet, das reihende δέ als nicht eigens wiedergegeben markiert. Die Lücken und die schematische Zählung "
  "([[MAT.1.8]], [[MAT.1.11]], [[MAT.1.17]]) sind in decisions als Befund benannt, nicht geglättet."),
 ("Erzählweise: Das erzählende Präsens (φαίνεται «erscheint», λέγει «sagt», [[MAT.2.13]], [[MAT.2.19]]–[[MAT.2.20]]) ist "
  "beibehalten. Anführungszeichen sind eine Entscheidung der Übersetzung. Die Rede des Engels endet mit [[MAT.1.21]]; "
  "[[MAT.1.22]]–[[MAT.1.23]] ist als Bemerkung des Erzählers gesetzt (die andere Möglichkeit in decisions). Das "
  "Prophetenwort in [[MAT.2.23]] steht nach einem Doppelpunkt ohne Anführungszeichen, weil es kein wörtliches Zitat ist."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens. Varianten, die die Übersetzung nicht verändern, stehen nicht als "
  "Alternativen: Schreibweisen von Namen ([[MAT.1.5]] Βόες/Βοός/Βοόζ und Ἰωβήδ/Ὠβήδ, [[MAT.1.20]] Μαρίαν/Μαριάμ), der "
  "Artikel in [[MAT.1.22]] und [[MAT.2.15]], ἐπί in [[MAT.2.22]], Wortstellungen ([[MAT.2.3]], [[MAT.2.8]], [[MAT.2.13]], "
  "[[MAT.2.19]], [[MAT.2.22]]) sowie [[MAT.1.24]] διεγερθείς, [[MAT.2.9]] ἔστη und [[MAT.2.21]] ἦλθεν. In [[MAT.1.7]]–"
  "[[MAT.1.8]] (Ἀσάφ/Ἀσά) verzeichnet der SBLGNT-Apparat keine Variante; der Befund steht in decisions. In Kapitel 1–2 "
  "fehlt im SBLGNT kein Vers."),
 ("Abgrenzung: Kapitel 1–2 bilden die Vorgeschichte (Herkunft, Geburt und Kindheit Jesu). Kapitel 3 setzt mit «In jenen "
  "Tagen» und dem Auftreten Johannes des Täufers neu ein. Die Gliederung in Abschnitte ist ein Vorschlag; die "
  "Erfüllungszitate ([[MAT.2.15]], [[MAT.2.18]], [[MAT.2.23]]) schliessen jeweils einen Abschnitt."),
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) oder uf de "
  "CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte. I [[MAT.1.18]] und [[MAT.2.17]] widerspricht d "
  "automatisch Zueornig de Transkriptione; d Alternative säged das."),
 ("Eigeti Formulierig, direkt us em Griechische (SBLGNT); nöd us ere veröffentlichte Mundart-Bible. Einheitlichi Begriff "
  "fürs ganz Matthäusevangelium: Χριστός «Christus», ἰδού «lueg», τότε «dänn», «Hoheprieschter», «Schriftgelehrti», "
  "«heilige Geischt», d Erfüllungsformle «damit erfüllt wird, was … dur de Prophet gseit worden isch:»."),
 ("Neu feschtgleit (Vorschlag fürs ganz Evangelium): προσκυνέω «huldige» («aabätte» nu für Gott); ἀναχωρέω «sich "
  "zruggzie»; κατʼ ὄναρ «im Traum»; χρηματίζω «e Wiisig übercho»; παιδίον «Chind»; δίκαιος «grächt»; σῴζω «rette»; "
  "τίκτω «(es Chind) übercho»; μάγοι «Stärndüüter»; Ναζωραῖος «Nazoräer»."),
 ("Mundart: Näme mit Artikel («de Josef», «d Maria»); Perfekt statt Präteritum; «wo» als Relativwort; kei Genitiv "
  "(«de Sohn vom David»). Im Stammbaum «isch de Vatter vo … worde» für ἐγέννησεν, wil «zeuge» im Züritüütsch "
  "ungwöhnlich isch."),
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
            raise SystemExit(f"MAT {c}: unerwartete Versanzahl")
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
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; wiederkehrende Wörter des Matthäusevangeliums einheitlich (siehe translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_01_02.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 1–2 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
