#!/usr/bin/env python3
"""Autorenwerkzeug: Obadja – Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem hebräischen Text
(Westminster Leningrad Codex), Übersetzungsentscheidungen und vollständige Wortzuordnung je Morphem.

Aufruf: python3 scripts/authoring/obadja_text.py

Auszeichnung wie in scripts/authoring/_lib.py; die Zahlen sind die Morphem-Positionen im Vers (data/tokens/WLC-OBA-001.json).
KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch nicht
muttersprachlich geprüft.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, alignment_entries, load_tokens, localize, write  # noqa: E402

DATE = "2026-10-13"
AUTH = "KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = ("KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; aus dem hebräischen Text (WLC) übersetzt. "
            "Prüfung der Mundart durch eine muttersprachliche Person (vorgesehen: Andi Neck) noch nicht erfolgt.")
TAGS = ["TAG-OBADIAH"]
OBJ = "Objektzeichen אֶת, im Deutschen nicht wiedergegeben"
OBJ_G = "Objektzeiche אֶת, nöd übersetzbar"
Q = "Fragepartikel הֲ; im Deutschen durch die Satzstellung ausgedrückt"
Q_G = "Fragewort הֲ; dur d Satzstellig usdruckt"

DE = {
 "OBA.1.1": "[Die Schauung]{1} [Obadjas]{2}. [So]{3} [spricht]{4} [der Herr]{5,6} [JHWH]{7} [über]{8} [Edom]{9}: [Eine Kunde]{10} [haben wir gehört]{11} [von]{12,13} [JHWH]{14}, und{15} [ein Bote]{16} [ist]{19} [unter]{17} [die Völker]{18} [gesandt]{19}: [Steht auf]{20}, und{21} [lasst uns]{22} [gegen]{23} [Edom]{24} [aufstehen]{22} [zum]{25} [Kampf]{26}!",
 "OBA.1.2": "[Sieh]{1}, [klein]{2} [habe ich]{3} [dich]{4} [gemacht]{3} [unter]{5} [den Völkern]{6}; [verachtet]{7} bist [du]{8} [sehr]{9}.",
 "OBA.1.3": "[Der Übermut]{1} [deines]{3} [Herzens]{2} [hat]{4} [dich]{5} [getäuscht]{4}, [der du wohnst]{6} [in]{7} [den Klüften]{8} [des Felsens]{9}, [hoch]{10} [sein]{12} [Wohnsitz]{11}, [der]{13} [in]{14} [seinem]{16} [Herzen]{15} [spricht]{13}: [Wer]{17} [stürzt]{18} [mich]{19} [zu Boden]{20}?",
 "OBA.1.4": "[Wenn]{1} [du auch hoch baust]{2} [wie]{3} [der Adler]{4} und{5} [wenn]{6} [dein]{11} [Nest]{10} [zwischen]{7} [den Sternen]{8} [gesetzt ist]{9}: [von]{12} [dort]{13} [stürze ich]{14} [dich]{15} [hinab]{14}, [Spruch]{16} [JHWHs]{17}.",
 "OBA.1.5": "[Wenn]{1} [Diebe]{2} [zu]{4} [dir]{5} [kämen]{3}, [wenn]{6} [Räuber]{7} [in der Nacht]{8} – [wie]{9} [bist du vernichtet]{10}! – [würden sie]{13} [nicht]{12} [nur stehlen]{13}, [was sie brauchen]{14,15}? [Wenn]{16} [Winzer]{17} [zu]{19} [dir]{20} [kämen]{18}, [würden sie]{23} [nicht]{22} [eine Nachlese]{24} [übrig lassen]{23}? ~11(" + Q + ") ~21(" + Q + ")",
 "OBA.1.6": "[Wie]{1} [ist]{2} [Esau]{3} [durchsucht]{2}, [aufgespürt]{4} [seine]{6} [verborgenen Schätze]{5}!",
 "OBA.1.7": "[Bis]{1} [an]{2} [die Grenze]{3} [haben sie]{4} [dich]{5} [abgeschoben]{4}, [alle]{6} [Männer]{7} [deines]{9} [Bundes]{8}; [sie haben]{10} [dich]{11} [getäuscht]{10}, [sie haben]{12,13} [dich]{14} [überwältigt]{12,13}, [die Männer]{15} [deines]{17} [Friedens]{16}; [dein]{19} [Brot]{18} [legen sie]{20} [als Falle]{21} [unter]{22} [dich]{23}. [Kein]{24} [Verstand]{25} [ist]{24} [in]{26} [ihm]{27}.",
 "OBA.1.8": "[Werde ich]{10} [nicht]{2} [an]{3} [jenem]{5,6} [Tag]{4} – [Spruch]{7} [JHWHs]{8} – [die Weisen]{11} [aus]{12} [Edom]{13} [vernichten]{10} und{14} [die Einsicht]{15} [vom]{16} [Gebirge]{17} [Esaus]{18}? ~1(" + Q + ") ~9(Verbindungspartikel וְ vor dem Verb; im Deutschen nicht eigens wiedergegeben)",
 "OBA.1.9": "Und{1} [deine]{4} [Helden]{3} [werden erschrecken]{2}, [Teman]{5}, [so dass]{6} [jeder]{8} [vom]{9} [Gebirge]{10} [Esaus]{11} [ausgerottet wird]{7} [durch]{12} [Morden]{13}.",
 "OBA.1.10": "[Wegen]{1} [der Gewalttat]{2} [an deinem]{4} [Bruder]{3} [Jakob]{5} [wird]{6} [dich]{7} [Schande]{8} [bedecken]{6}, und{9} [du wirst ausgerottet]{10} [für]{11} [immer]{12}.",
 "OBA.1.11": "[Am]{1} [Tag]{2}, als [du]{4} [abseits]{5,6} [standest]{3}, [am]{7} [Tag]{8}, als [Fremde]{10} [sein]{12} [Vermögen]{11} [wegführten]{9} und{13} [Ausländer]{14} in [seine]{17} [Tore]{16} [eindrangen]{15} und{18} [über]{19} [Jerusalem]{20} [das Los]{22} [warfen]{21}, warst [auch]{23} [du]{24} [wie]{25} [einer]{26} [von]{27} [ihnen]{28}.",
 "OBA.1.12": "Und{1} [schau]{3} [nicht]{2} [auf]{4} [den Tag]{5} [deines]{7} [Bruders]{6} [herab]{3}, [auf]{8} [den Tag]{9} [seines]{11} [Unglücks]{10}, und{12} [freu dich]{14} [nicht]{13} [über]{15} [die Söhne]{16} [Judas]{17} [am]{18} [Tag]{19} [ihres]{21} [Untergangs]{20}, und{22} [reiss]{24} [deinen]{26} [Mund]{25} [nicht]{23} [auf]{24} [am]{27} [Tag]{28} [der Not]{29}.",
 "OBA.1.13": "[Zieh]{2} [nicht]{1} [ins]{3} [Tor]{4} [meines]{6} [Volkes]{5} [ein]{2} [am]{7} [Tag]{8} [ihres]{10} [Verderbens]{9}; [schau]{12} [nicht]{11} [auch]{13} [du]{14} [auf]{15} [sein]{17} [Unglück]{16} [herab]{12} [am]{18} [Tag]{19} [seines]{21} [Verderbens]{20}; und{22} [greif]{24} [nicht]{23} [nach]{25} [seinem]{27} [Vermögen]{26} [am]{28} [Tag]{29} [seines]{31} [Verderbens]{30}.",
 "OBA.1.14": "Und{1} [stell dich]{3} [nicht]{2} [an]{4} [die]{5} [Wegkreuzung]{6}, [um]{7} [seine]{11} [Flüchtlinge]{10} [niederzumachen]{8}, und{12} [liefere]{14} [seine]{16} [Überlebenden]{15} [nicht]{13} [aus]{14} [am]{17} [Tag]{18} [der Not]{19}. ~9(" + OBJ + ")",
 "OBA.1.15": "Denn{1} [nahe]{2} ist [der Tag]{3} [JHWHs]{4} [über]{5} [alle]{6} [Völker]{7,8}. [Wie]{9,10} [du getan hast]{11}, [wird]{12} [dir]{13,14} [getan werden]{12}; [dein]{16} [Tun]{15} [fällt zurück]{17} [auf]{18} [deinen]{20} [Kopf]{19}.",
 "OBA.1.16": "Denn{1} [wie]{2,3} [ihr getrunken habt]{4} [auf]{5} [meinem]{8} [heiligen]{7} [Berg]{6}, [werden]{9} [alle]{10} [Völker]{11,12} [trinken]{9} [immerfort]{13}; und{14} [sie werden trinken]{15} und{16} [schlürfen]{17} und{18} [werden sein]{19} [wie]{20} [solche, die nie]{21} [gewesen sind]{22}.",
 "OBA.1.17": "[Aber]{1} [auf]{2} [dem Berg]{3} [Zion]{4} [wird]{5} [Rettung]{6} [sein]{5}, und{7} [er wird]{8} [heilig]{9} [sein]{8}; und{10} [das Haus]{12} [Jakob]{13} [wird]{11} [seinen]{16} [Besitz]{15} [in Besitz nehmen]{11}. ~14(" + OBJ + ")",
 "OBA.1.18": "Und{1} [das Haus]{3} [Jakob]{4} [wird]{2} [ein Feuer]{5} [sein]{2} und{6} [das Haus]{7} [Josef]{8} [eine Flamme]{9}, und{10} [das Haus]{11} [Esau]{12} [zu]{13} [Stroh]{14}; und{15} [sie werden]{16} [sie]{17,18} [anzünden]{16} und{19} [verzehren]{20,21}; und{22} [es wird]{24} [kein]{23} [Entronnener]{25} [bleiben]{24} [dem]{26} [Haus]{27} [Esau]{28}, [denn]{29} [JHWH]{30} [hat gesprochen]{31}.",
 "OBA.1.19": "Und{1} [die im]{3} [Negev]{4} [werden]{2} [das Gebirge]{6} [Esau]{7} [in Besitz nehmen]{2}, und{8} [die in]{9} [der Schefela]{10} [die Philister]{12}; und{13} [sie werden]{14} [das Gebiet]{16} [Efraim]{17} und{18} [das Gebiet]{20} [Samaria]{21} [in Besitz nehmen]{14}, und{22} [Benjamin]{23} [Gilead]{25,26}. ~5(" + OBJ + ") ~11(" + OBJ + ") ~15(" + OBJ + ") ~19(" + OBJ + ") ~24(" + OBJ + ")",
 "OBA.1.20": "Und{1} [die Verbannten]{2} [dieses]{5,6} [Heeres]{3,4} [der]{7} [Israeliten]{8,9}, [die]{10} [unter den Kanaanitern]{11} sind [bis]{12} [Sarepta]{13}, und{14} [die Verbannten]{15} [Jerusalems]{16}, [die]{17} [in]{18} [Sefarad]{19} sind, [werden]{20} [die Städte]{22} [des]{23} [Negev]{24} [in Besitz nehmen]{20}. ~21(" + OBJ + ")",
 "OBA.1.21": "Und{1} [Retter]{3} [werden hinaufziehen]{2} [auf]{4} [den Berg]{5} [Zion]{6}, [um]{7} [das Gebirge]{10} [Esau]{11} [zu richten]{8}; und{12} [die]{16} [Königsherrschaft]{17} [wird]{13} [JHWH]{15} [gehören]{14}. ~9(" + OBJ + ")",
}
GSW = {
 "OBA.1.1": "[D Schauig]{1} [vom Obadja]{2}. [So]{3} [seit]{4} [de Herr]{5,6} [JHWH]{7} [über]{8} [Edom]{9}: [E Nachricht]{10} [händ mir ghört]{11} [vo]{12,13} [JHWH]{14}, und{15} [en Bote]{16} [isch]{19} [under]{17} [d Völker]{18} [gschickt worde]{19}: [Stönd uf]{20}, und{21} [mir wänd]{22} [gäge]{23} [Edom]{24} [ufstaa]{22} [zum]{25} [Chrieg]{26}!",
 "OBA.1.2": "[Lueg]{1}, [chlii]{2} [han ich]{3} [dich]{4} [gmacht]{3} [under]{5} [de Völker]{6}; [verachtet]{7} bisch [du]{8} [seer]{9}.",
 "OBA.1.3": "[De Übermuet]{1} [vo dim]{3} [Herz]{2} [hät]{4} [dich]{5} [tüüscht]{4}, [du, wo wohnsch]{6} [i]{7} [de Chlüft]{8} [vom Fels]{9}, [hööch]{10} [sis]{12} [Daheim]{11}, [wo]{13} [i]{14} [sim]{16} [Herz]{15} [seit]{13}: [Wär]{17} [stürzt]{18} [mich]{19} [uf de Bode]{20}?",
 "OBA.1.4": "[Wänn]{1} [du au hööch bausch]{2} [wie]{3} [de Adler]{4} und{5} [wänn]{6} [dis]{11} [Näscht]{10} [zwüsche]{7} [de Stärne]{8} [gsetzt isch]{9}: [vo]{12} [dört]{13} [stürz ich]{14} [dich]{15} [abe]{14}, [Spruch]{16} [vo JHWH]{17}.",
 "OBA.1.5": "[Wänn]{1} [Diebe]{2} [zu]{4} [dir]{5} [chämted]{3}, [wänn]{6} [Röiber]{7} [i de Nacht]{8} – [wie]{9} [bisch du vernichtet]{10}! – [würded si]{13} [nöd]{12} [nu stäle]{13}, [was si bruuched]{14,15}? [Wänn]{16} [Wiibuure]{17} [zu]{19} [dir]{20} [chämted]{18}, [würded si]{23} [nöd]{22} [e Nachläsi]{24} [übrig laa]{23}? ~11(" + Q_G + ") ~21(" + Q_G + ")",
 "OBA.1.6": "[Wie]{1} [isch]{2} [de Esau]{3} [dursuecht]{2}, [uufgspürt]{4} [sini]{6} [versteckte Schätz]{5}!",
 "OBA.1.7": "[Bis]{1} [a]{2} [d Gränze]{3} [händ si]{4} [dich]{5} [abgschobe]{4}, [alli]{6} [Mane]{7} [vo dim]{9} [Bund]{8}; [si händ]{10} [dich]{11} [tüüscht]{10}, [si händ]{12,13} [dich]{14} [überwältiget]{12,13}, [d Mane]{15} [vo dim]{17} [Fride]{16}; [dis]{19} [Broot]{18} [leged si]{20} [als Falle]{21} [under]{22} [dich]{23}. [Kei]{24} [Verstand]{25} [isch]{24} [i]{26} [im]{27}.",
 "OBA.1.8": "[Wird ich]{10} [nöd]{2} [a]{3} [dem]{5,6} [Taag]{4} – [Spruch]{7} [vo JHWH]{8} – [di Wiise]{11} [us]{12} [Edom]{13} [vernichte]{10} und{14} [d Iisicht]{15} [vom]{16} [Gebirg]{17} [vo Esau]{18}? ~1(" + Q_G + ") ~9(Verbindigswort וְ vor em Verb; nöd eigens widergää)",
 "OBA.1.9": "Und{1} [dini]{4} [Helde]{3} [verschrecked]{2}, [Teman]{5}, [so dass]{6} [jede]{8} [vom]{9} [Gebirg]{10} [vo Esau]{11} [usgrottet wird]{7} [dur]{12} [Morde]{13}.",
 "OBA.1.10": "[Wäge]{1} [de Gwalt]{2} [a dim]{4} [Brueder]{3} [Jakob]{5} [wird]{6} [dich]{7} [Schand]{8} [zuedecke]{6}, und{9} [du wirsch usgrottet]{10} [für]{11} [immer]{12}.",
 "OBA.1.11": "[Am]{1} [Taag]{2}, wo [du]{4} [abseits]{5,6} [gstande bisch]{3}, [am]{7} [Taag]{8}, wo [Frömdi]{10} [sis]{12} [Vermöge]{11} [wäggfüert händ]{9} und{13} [Uusländer]{14} i [sini]{17} [Tor]{16} [iidrunge sind]{15} und{18} [über]{19} [Jerusalem]{20} [s Los]{22} [gworfe händ]{21}, bisch [au]{23} [du]{24} [wie]{25} [eine]{26} [vo]{27} [ine]{28} gsii.",
 "OBA.1.12": "Und{1} [lueg]{3} [nöd]{2} [uf]{4} [de Taag]{5} [vo dim]{7} [Brueder]{6} [abe]{3}, [uf]{8} [de Taag]{9} [vo sim]{11} [Unglück]{10}, und{12} [fröi dich]{14} [nöd]{13} [über]{15} [d Söön]{16} [vo Juda]{17} [am]{18} [Taag]{19} [vo irem]{21} [Undergang]{20}, und{22} [riss]{24} [dis]{26} [Muul]{25} [nöd]{23} [uf]{24} [am]{27} [Taag]{28} [vo de Not]{29}.",
 "OBA.1.13": "[Zie]{2} [nöd]{1} [is]{3} [Tor]{4} [vo mim]{6} [Volk]{5} [ii]{2} [am]{7} [Taag]{8} [vo irem]{10} [Verderbe]{9}; [lueg]{12} [nöd]{11} [au]{13} [du]{14} [uf]{15} [sis]{17} [Unglück]{16} [abe]{12} [am]{18} [Taag]{19} [vo sim]{21} [Verderbe]{20}; und{22} [griif]{24} [nöd]{23} [nach]{25} [sim]{27} [Vermöge]{26} [am]{28} [Taag]{29} [vo sim]{31} [Verderbe]{30}.",
 "OBA.1.14": "Und{1} [stell dich]{3} [nöd]{2} [a]{4} [d]{5} [Wägchrüüzig]{6}, [zum]{7} [sini]{11} [Flüchtling]{10} [z töde]{8}, und{12} [liefer]{14} [sini]{16} [Überläbende]{15} [nöd]{13} [us]{14} [am]{17} [Taag]{18} [vo de Not]{19}. ~9(" + OBJ_G + ")",
 "OBA.1.15": "Dänn{1} [nööch]{2} isch [de Taag]{3} [vo JHWH]{4} [über]{5} [alli]{6} [Völker]{7,8}. [Wie]{9,10} [du gmacht häsch]{11}, [wird]{12} [mit dir]{13,14} [gmacht]{12}; [dis]{16} [Tue]{15} [fallt zrugg]{17} [uf]{18} [din]{20} [Chopf]{19}.",
 "OBA.1.16": "Dänn{1} [wie]{2,3} [ir trunke händ]{4} [uf]{5} [mim]{8} [heilige]{7} [Bärg]{6}, [wärded]{9} [alli]{10} [Völker]{11,12} [trinke]{9} [immer wiiter]{13}; und{14} [si wärded trinke]{15} und{16} [schlürfe]{17} und{18} [wärded sii]{19} [wie]{20} [die, wo nie]{21} [gsii sind]{22}.",
 "OBA.1.17": "[Aber]{1} [uf]{2} [em Bärg]{3} [Zion]{4} [wird]{5} [Rettig]{6} [sii]{5}, und{7} [er wird]{8} [heilig]{9} [sii]{8}; und{10} [s Huus]{12} [Jakob]{13} [wird]{11} [sin]{16} [Bsitz]{15} [in Bsitz nää]{11}. ~14(" + OBJ_G + ")",
 "OBA.1.18": "Und{1} [s Huus]{3} [Jakob]{4} [wird]{2} [es Füür]{5} [sii]{2} und{6} [s Huus]{7} [Josef]{8} [e Flamme]{9}, und{10} [s Huus]{11} [Esau]{12} [zu]{13} [Strau]{14}; und{15} [si wärded]{16} [si]{17,18} [aazünde]{16} und{19} [ufzeere]{20,21}; und{22} [es wird]{24} [kein]{23} [Überläbende]{25} [blibe]{24} [em]{26} [Huus]{27} [Esau]{28}, [dänn]{29} [JHWH]{30} [hät gredt]{31}.",
 "OBA.1.19": "Und{1} [die im]{3} [Negev]{4} [wärded]{2} [s Gebirg]{6} [Esau]{7} [in Bsitz nää]{2}, und{8} [die i]{9} [de Schefela]{10} [d Philischter]{12}; und{13} [si wärded]{14} [s Gebiet]{16} [Efraim]{17} und{18} [s Gebiet]{20} [Samaria]{21} [in Bsitz nää]{14}, und{22} [Benjamin]{23} [Gilead]{25,26}. ~5(" + OBJ_G + ") ~11(" + OBJ_G + ") ~15(" + OBJ_G + ") ~19(" + OBJ_G + ") ~24(" + OBJ_G + ")",
 "OBA.1.20": "Und{1} [di Verbannte]{2} [vo däm]{5,6} [Heer]{3,4} [vo de]{7} [Israelite]{8,9}, [wo]{10} [under de Kanaaniter]{11} sind [bis]{12} [Sarepta]{13}, und{14} [di Verbannte]{15} [vo Jerusalem]{16}, [wo]{17} [i]{18} [Sefarad]{19} sind, [wärded]{20} [d Stedt]{22} [vom]{23} [Negev]{24} [in Bsitz nää]{20}. ~21(" + OBJ_G + ")",
 "OBA.1.21": "Und{1} [Retter]{3} [wärded ufezie]{2} [uf]{4} [de Bärg]{5} [Zion]{6}, [zum]{7} [s Gebirg]{10} [Esau]{11} [z richte]{8}; und{12} [d]{16} [Königsherrschaft]{17} [wird]{13} [em JHWH]{15} [ghöre]{14}. ~9(" + OBJ_G + ")",
}

DEC_DE = [
 ("OBA.1.1", "JHWH", "interpretive", "יְהוִה", None, ["der HERR", "der Ewige", "Jahwe"],
  "Der Gottesname wird im Judentum nicht ausgesprochen; gelesen wird «Adonai» (der Herr). Viele deutsche Bibeln schreiben «der HERR». Hier steht der Name in seinen vier Konsonanten, damit sichtbar bleibt, dass im Hebräischen ein Name steht."),
 ("OBA.1.1", "Die Schauung", "literal", "חֲזוֹן", None, ["Die Vision", "Das Gesicht"],
  "חָזוֹן ist das, was ein Prophet «schaut»; als Buchüberschrift auch in [[ISA.1.1]] und [[NAM.1.1]]."),
 ("OBA.1.1", "gegen Edom", "adapted", "עָלֶיהָ", "gegen sie", None, "Wörtlich «gegen sie»: Edom als Land ist im Hebräischen weiblich."),
 ("OBA.1.2", "habe ich", "interpretive", "נְתַתִּיךָ", "ich habe dich gegeben", ["mache ich dich", "werde ich dich machen"],
  "Die Vergangenheitsform kann eine sicher erwartete Zukunft ausdrücken (prophetisches Perfekt); andere lesen sie als Rückblick auf Edoms Geschichte."),
 ("OBA.1.3", "des Felsens", "literal", "סֶלַע", None, ["von Sela"], "Sela («Fels») kann auch ein Ortsname in Edom sein; ein Wortspiel ist möglich."),
 ("OBA.1.4", "Spruch", "literal", "נְאֻם", None, ["spricht"], "נְאֻם יְהוָה ist eine feste Formel am Ende eines Prophetenwortes, traditionell übersetzt mit «spricht der HERR»."),
 ("OBA.1.7", "Brot", "literal", "לַחְמְךָ", None, ["die dein Brot essen"],
  "Der Satz ist schwer verständlich. Oft wird vermutet, dass «die dein Brot essen», also Tischgenossen, gemeint sind; die alten Übersetzungen gehen hier auseinander."),
 ("OBA.1.7", "als Falle", "interpretive", "מָזוֹר", None, ["als Netz", "als Wunde"], "Die Bedeutung von מָזוֹר ist hier unsicher; an anderen Stellen heisst das Wort «Wunde»."),
 ("OBA.1.12", "herab", "interpretive", "תֵּרֶא", "sieh nicht", ["schau nicht schadenfroh zu"], "רָאָה בְּ meint das Zusehen mit Genugtuung am Unglück eines anderen."),
 ("OBA.1.12", "die Söhne", "literal", "בְנֵי", None, ["die Leute"], "Gemeint sind die Bewohner Judas."),
 ("OBA.1.17", "seinen", "interpretive", "מוֹרָשֵׁיהֶם", "ihren Besitz", ["die, die sie enteignet haben"],
  "Wörtlich «ihren Besitz». Mit anderen Vokalen gelesen heisst es «die sie enteignet haben»; so verstehen es die Septuaginta und einige Ausleger. «Seinen» bezieht sich hier auf das Haus Jakob."),
 ("OBA.1.17", "Rettung", "interpretive", "פְלֵיטָה", "Entronnene", ["Entrinnen"], "פְּלֵיטָה meint das Entkommen bzw. die, die entkommen sind; «Rettung» fasst beides zusammen."),
 ("OBA.1.20", "unter den Kanaanitern", "interpretive", "אֲשֶׁר כְּנַעֲנִים", None, ["(werden besitzen,) was den Kanaanitern gehört"], "Der Satz lässt sich auch so lesen, dass die Verbannten das Land der Kanaaniter bis Sarepta in Besitz nehmen."),
 ("OBA.1.20", "dieses Heeres", "interpretive", "הַחֵל הַזֶּה", None, ["dieses Walls", "dieser Festung"],
  "Der Vers ist schwer verständlich; חֵל kann «Heer» oder «Wall» heissen."),
 ("OBA.1.20", "Sefarad", "literal", "סְפָרַד", None, None,
  "Wo Sefarad lag, ist unbekannt; oft wird an Sardes in Kleinasien gedacht. Seit der Spätantike (Targum) wurde der Name auf Spanien bezogen."),
 ("OBA.1.21", "Retter", "interpretive", "מוֹשִׁעִים", None, ["Gerettete"], "Die Septuaginta liest «Gerettete»."),
]
DEC_GSW = [
 ("OBA.1.1", "JHWH", "interpretive", "יְהוִה", None, ["de HERR", "de Ewig", "Jahwe"],
  "De Gottesname wird im Judetum nöd usgsproche; gläse wird «Adonai» (de Herr). Vili düütschi Bible schriibed «der HERR». Da staat de Name i sine vier Konsonante, demit me gseet, dass im Hebräische en Name staat."),
 ("OBA.1.1", "D Schauig", "literal", "חֲזוֹן", None, ["D Vision"], "חָזוֹן isch das, was en Prophet «gseet»; als Buechüberschrift au i [[ISA.1.1]] und [[NAM.1.1]]."),
 ("OBA.1.1", "gäge Edom", "adapted", "עָלֶיהָ", "gäge si", None, "Wörtlich «gäge si»: Edom als Land isch im Hebräische wiiblich."),
 ("OBA.1.2", "han ich", "interpretive", "נְתַתִּיךָ", "ich han dich gää", ["mach ich dich", "wird ich dich mache"],
  "D Vergangeheitsform cha e sicher erwarteti Zuekunft usdrucke (prophetischs Perfekt); anderi läsed si als Ruggblick uf d Gschicht vo Edom."),
 ("OBA.1.3", "vom Fels", "literal", "סֶלַע", None, ["vo Sela"], "Sela («Fels») cha au en Ortsname z Edom sii; es Wortspiil isch möglich."),
 ("OBA.1.4", "Spruch", "literal", "נְאֻם", None, ["seit"], "נְאֻם יְהוָה isch e feschti Formle am Änd vo me Prophetewort, traditionell übersetzt mit «spricht der HERR»."),
 ("OBA.1.7", "Broot", "literal", "לַחְמְךָ", None, ["die, wo dis Broot ässed"],
  "De Satz isch schwär verständlich. Oft vermuetet me, dass «die, wo dis Broot ässed», also Tischgenosse, gmeint sind; di alte Übersetzige gönd da usenand."),
 ("OBA.1.7", "als Falle", "interpretive", "מָזוֹר", None, ["als Netz", "als Wunde"], "D Bedüütig vo מָזוֹר isch da unsicher; a andere Stelle heisst s Wort «Wunde»."),
 ("OBA.1.12", "abe", "interpretive", "תֵּרֶא", "lueg nöd", ["lueg nöd schadefroh zue"], "רָאָה בְּ meint s Zueluege mit Gnuegtuig am Unglück vo me andere."),
 ("OBA.1.12", "d Söön", "literal", "בְנֵי", None, ["d Lüüt"], "Gmeint sind d Bewoner vo Juda."),
 ("OBA.1.17", "sin", "interpretive", "מוֹרָשֵׁיהֶם", "ire Bsitz", ["die, wo si enteignet händ"],
  "Wörtlich «ire Bsitz». Mit andere Vokal gläse heisst s «die, wo si enteignet händ»; so verstönd s d Septuaginta und es paar Usleger."),
 ("OBA.1.17", "Rettig", "interpretive", "פְלֵיטָה", "Entrunneni", ["Entrinne"], "פְּלֵיטָה meint s Entcho oder die, wo entcho sind; «Rettig» fasst beides zäme."),
 ("OBA.1.20", "under de Kanaaniter", "interpretive", "אֲשֶׁר כְּנַעֲנִים", None, ["(wärded in Bsitz nää,) was de Kanaaniter ghört"], "De Satz cha me au so läse, dass d Verbannte s Land vo de Kanaaniter bis Sarepta in Bsitz nämed."),
 ("OBA.1.20", "vo däm", "interpretive", "הַחֵל הַזֶּה", None, ["vo dem Wall", "vo dere Feschtig"],
  "De Vers isch schwär verständlich; חֵל cha «Heer» oder «Wall» heisse."),
 ("OBA.1.20", "Sefarad", "literal", "סְפָרַד", None, None,
  "Wo Sefarad gläge isch, weiss me nöd; oft dänkt me a Sardes z Chliiasie. Sit de Spöötantike (Targum) hät me de Name uf Spanie bezoge."),
 ("OBA.1.21", "Retter", "interpretive", "מוֹשִׁעִים", None, ["Grettete"], "D Septuaginta liest «Grettete»."),
]

UNITS = [
 ("TU-OBA-001-001-021", "OBA.1.1-OBA.1.21", "book", "Das Gesicht Obadjas: gegen Edom",
  ["TU-OBA-001-001-004", "TU-OBA-001-005-009", "TU-OBA-001-010-014", "TU-OBA-001-015-018", "TU-OBA-001-019-021"],
  "Das kürzeste Buch des Alten Testaments kündigt dem Nachbarvolk Edom das Gericht an, weil es sich am Tag der Eroberung Jerusalems gegen seinen «Bruder» Jakob gestellt hat, und schliesst mit der Hoffnung, dass das Königtum JHWH gehören wird."),
 ("TU-OBA-001-001-004", "OBA.1.1-OBA.1.4", "section", "Edoms Hochmut", None,
  "Edom fühlt sich in seinen Felsen unangreifbar. Gott kündigt an, es von dort herabzustürzen."),
 ("TU-OBA-001-005-009", "OBA.1.5-OBA.1.9", "section", "Ausgeplündert und verraten", None,
  "Diebe und Winzer lassen etwas übrig, Edom aber wird gründlich durchsucht. Seine Verbündeten täuschen es, seine Weisheit und seine Krieger versagen."),
 ("TU-OBA-001-010-014", "OBA.1.10-OBA.1.14", "section", "Am Tag der Not deines Bruders", None,
  "Der Grund des Gerichts: Edom hat zugesehen, sich gefreut, geplündert und Flüchtlinge ausgeliefert, als Fremde Jerusalem eroberten."),
 ("TU-OBA-001-015-018", "OBA.1.15-OBA.1.18", "section", "Der Tag JHWHs", None,
  "Der Tag JHWHs kommt über alle Völker; was Edom getan hat, fällt auf es zurück. Auf dem Zion aber gibt es Rettung, und das Haus Jakob wird zum Feuer, das Esau verzehrt."),
 ("TU-OBA-001-019-021", "OBA.1.19-OBA.1.21", "section", "Das Königtum wird JHWH gehören", None,
  "Die Heimkehrenden nehmen das Land in alle Richtungen wieder in Besitz. Vom Zion aus wird Esau gerichtet, und die Königsherrschaft gehört JHWH."),
]
UNITS_GSW = {
 "TU-OBA-001-001-021": ("D Schauig vom Obadja: gäge Edom", "S chürzischt Buech vom Alte Teschtamänt chündet em Nochbervolk Edom s Gricht aa, wil es sich am Taag vo de Eroberig vo Jerusalem gäge sin «Brueder» Jakob gstellt hät, und hört mit de Hoffnig uf, dass d Königsherrschaft em JHWH wird ghöre."),
 "TU-OBA-001-001-004": ("De Hochmuet vo Edom", "Edom füült sich i sine Felse unaagriifbar. Gott chündet aa, es vo dört abezstürze."),
 "TU-OBA-001-005-009": ("Usplünderet und verrate", "Diebe und Wiibuure lönd öppis übrig, Edom aber wird gründlich dursuecht. Sini Verbündete tüüsched s, sini Wiisheit und sini Chrieger versaged."),
 "TU-OBA-001-010-014": ("Am Taag vo de Not vo dim Brueder", "De Grund vom Gricht: Edom hät zuegluegt, sich gfröit, plünderet und Flüchtling usgliferet, wo Frömdi Jerusalem eroberet händ."),
 "TU-OBA-001-015-018": ("De Taag vo JHWH", "De Taag vo JHWH chunnt über alli Völker; was Edom gmacht hät, fallt uf s zrugg. Uf em Zion aber gits Rettig, und s Huus Jakob wird zum Füür, wo de Esau verzeert."),
 "TU-OBA-001-019-021": ("D Königsherrschaft wird em JHWH ghöre", "Die, wo heichömed, nämed s Land i alli Richtige wider in Bsitz. Vom Zion us wird de Esau grichtet, und d Königsherrschaft ghört em JHWH."),
}


def run():
    n = write(D / "works" / "WORK-OBA.json", {"id": "WORK-OBA", "type": "work", "status": "draft", "tags": TAGS,
                                             "name": "Obadja", "original_language": "he"})
    for uid, rng, kind, title, parts, summary in UNITS:
        rec = {"id": uid, "type": "text_unit", "status": "draft", "tags": TAGS, "work": "WORK-OBA", "range": rng, "kind": kind,
               "title": title, **({"parts": parts} if parts else {}),
               **({"segmentation_note_de": "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."} if parts else {}),
               "knowledge": {"asserted_at": DATE, "supersedes": None}, "summary_de": summary, "summary_authorship_de": AUTH}
        n += write(D / "text-units" / f"{uid}.json", rec)
        gt, gs = UNITS_GSW[uid]
        n += localize(uid, rec, {"title": gt, "summary_de": gs}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026",
                      "KI-Entwurf (Claude) vom 2026-10-13; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.", DATE)
    ts_id, toks = load_tokens(D / "tokens" / "WLC-OBA-001.json")
    refs_c = [f"OBA.1.{v}" for v in range(1, 22)]
    for lang, markup, decs, code in (("de", DE, DEC_DE, "DE"), ("gsw", GSW, DEC_GSW, "GSW-ZH")):
        texts, aligns = {}, []
        for r in refs_c:
            words = {pos: t["word"] for pos, t in toks[r].items()}
            text, al = alignment_entries(r, markup[r], words, lambda p, r=r: toks[r][p]["id"])
            texts[r], aligns = text, aligns + al
        tid = f"TRANS-OBA-001-001-021-{code}-WORKING"
        dec = [{"reference": r, "target": tg, "kind": kd, "heb": heb, **({"more_literal": ml} if ml else {}),
                **({"other_options": oo} if oo else {}), "note": nt} for r, tg, kd, heb, ml, oo, nt in decs]
        for d in dec:
            if d["target"] not in texts[d["reference"]]:
                raise SystemExit(f"{tid}: Entscheidung {d['target']!r} nicht im Text {d['reference']}")
        rec = {"id": tid, "type": "translation", "status": "draft", "tags": TAGS, "reference": "OBA.1.1-OBA.1.21",
               "language": "de-CH" if lang == "de" else "gsw-u-sd-chzh", "translation_kind": "literal_original_working"}
        if lang == "gsw":
            rec.update({"language_label_de": "Züridüütsch", "language_name_de": "Zürichdeutsch", "target_context": "CTX-CH-ZH-GSW-2026",
                        "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Broot, Riich), ä für offenes e.",
                        "register_de": "Nah am hebräischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                        "control_translation": "TRANS-OBA-001-001-021-DE-WORKING",
                        "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
        rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem hebräischen Text (Westminster Leningrad Codex): Satzbau und Bilder des Hebräischen möglichst sichtbar, verständliches Deutsch. Der Gottesname steht als JHWH. Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
                                   if lang == "de" else "Direkt aus dem hebräischen Text (WLC) übersetzt, mit Wortzuordnung zu den Morphemen; die hochdeutsche Arbeitsübersetzung dient nur als Kontrolle. Nicht aus einer veröffentlichten Mundart-Bibel übernommen."),
                    "based_on_edition": "ED-WLC", "based_on_tokens": ts_id, "text_by_reference": texts,
                    "translation_notes": (["Textkritische Varianten (Qumran, Septuaginta, mittelalterliche Handschriften) sind für Obadja noch nicht als freie Daten erfasst; schwierige Stellen sind in den Entscheidungen vermerkt."]
                                          if lang == "de" else ["Textkritischi Variante (Qumran, Septuaginta, mittelalterlichi Handschrifte) sind für de Obadja no nöd als freii Date erfasst; schwierigi Stelle sind i de Entscheidige vermerkt."]),
                    "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                    "decisions": dec,
                    "decisions_note_de": "Übersetzungsentscheidungen: wörtlich (literal), sprachlich angepasst (adapted), Deutungsentscheidung (interpretive) oder der vertrauten Wiedergabe folgend (traditional). " + (AUTH if lang == "de" else AUTH_GSW)})
        n += write(D / "translations" / f"{tid}.json", rec)
        aid = f"ALIGN-OBA-001-001-021-{code}-001"
        n += write(D / "alignments" / f"{aid}.json", {
            "id": aid, "type": "alignment", "status": "draft", "tags": TAGS, "reference": "OBA.1.1-OBA.1.21",
            "source_language": "he", "target_language": rec["language"], "source_basis": "ED-WLC", "source_tokens_set": ts_id,
            "target_translation": tid, "coverage": "complete",
            "coverage_de": f"Jedes der {sum(len(toks[r]) for r in refs_c)} Morphem-Tokens ist genau einer Zuordnung zugewiesen.",
            "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/obadja_text.py).",
            "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
            "alignments": aligns})
    print(f"PASS: Obadja – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
