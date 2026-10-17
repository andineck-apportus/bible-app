#!/usr/bin/env python3
"""Autorenwerkzeug: Matthäus 3–4 (Johannes der Täufer, Taufe Jesu, Versuchung, Beginn in Galiläa, erste Jünger) –
Texteinheiten, Arbeitsübersetzungen (Hochdeutsch, Züridüütsch) aus dem SBLGNT, Übersetzungsentscheidungen,
Lesarten-Alternativen und vollständige Wortzuordnung.

Aufruf: python3 scripts/authoring/matthaeus_text_03_04.py

Die Übersetzung steht als Auszeichnung je Vers (siehe scripts/authoring/_lib.py); Text und Wortzuordnung entstehen
daraus und stimmen deshalb überein. Idempotent; bei Änderungen kommt die frühere Fassung ins revision_log.
WORK-MAT besteht bereits und wird hier nur referenziert, nicht geschrieben.

Besonderheiten:
- In Matthäus 3–4 fehlt im SBLGNT kein Vers (per Skript geprüft); alle Verse haben Tokens.
- Die einheitlichen Matthäus-Begriffe (Reich der Himmel, siehe, sogleich, Umkehr, Erfüllungsformel …) sind für alle
  Matthäus-Bereiche abgestimmt; in Kapitel 3–4 neu festgelegte Wiedergaben stehen in translation_notes.
- [[MAT.4.12]], [[MAT.4.23]]: Die automatische Kollation widerspricht teils dem erfassten Wortlaut der Handschriften;
  das ist bei den Alternativen benannt.

KI-Entwurf (Claude) vom 2026-10-18 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt. Die Mundart ist noch
nicht muttersprachlich geprüft. Handschriftenangaben stammen aus der maschinellen Zuordnung (METHOD-AUTO-COLLATION-V1)
bzw. aus deren erfasstem Wortlaut der CNTR-Transkriptionen (Sekundärtranskription), nicht aus eigener Prüfung der
Handschriften. Zahlen zu Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts (data/annotations)
ermittelt.
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
CHAPTERS = ((3, 17), (4, 25))

DE = {
 # ------------------------------------------------------------ Kapitel 3
 "MAT.3.1": "[In]{1} [jenen]{5} [Tagen]{3,4} [aber]{2} [tritt]{6} Johannes{7} [der Täufer]{8,9} [auf]{6} [und verkündigt]{10} [in]{11} [der Wüste]{12,13} [Judäas]{14,15}",
 "MAT.3.2": "und{1} [sagt]{2}: «[Kehrt um]{3}, [denn]{5} [das Reich]{6,7} [der Himmel]{8,9} [ist nahe gekommen]{4}!»",
 "MAT.3.3": "[Denn]{2} [dieser]{1} [ist]{3} [es, von dem]{4} [durch]{6} Jesaja{7}, [den Propheten]{8,9}, [gesagt ist]{5}: «[Stimme]{11} [eines Rufenden]{12} [in]{13} [der Wüste]{14,15}: ‹[Bereitet]{16} [den Weg]{17,18} [des Herrn]{19}, [macht]{21} [seine]{24} [Pfade]{22,23} [gerade]{20}!›» ~10(λέγοντος «sagend» leitet das Zitat ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.3.4": "Johannes{3,4} [selbst]{1} [aber]{2} [hatte]{5} [sein]{8} [Gewand]{6,7} [aus]{9} [Kamelhaar]{10,11} und{12} [einen ledernen]{14} [Gurt]{13} [um]{15} [seine]{18} [Hüften]{16,17}; [seine]{23} [Nahrung]{19,21} [aber]{20} [waren]{22} [Heuschrecken]{24} und{25} [wilder]{27} [Honig]{26}.",
 "MAT.3.5": "[Da]{1} [zog]{2} Jerusalem{5} und{6} [ganz]{7} [Judäa]{8,9} und{10} [die ganze]{11,12} [Umgebung]{13} [des Jordan]{14,15} [zu]{3} [ihm]{4} [hinaus]{2},",
 "MAT.3.6": "und{1} [sie liessen sich]{2} [im]{3,4} [Fluss]{6} Jordan{5} [von]{7} [ihm]{8} [taufen]{2} [und bekannten]{9} [ihre]{12} [Sünden]{10,11}.",
 "MAT.3.7": "[Als er]{1} [aber]{2} [viele]{3} [von den]{4} [Pharisäern]{5} und{6} [Sadduzäern]{7} [zu]{9} [seiner]{12} [Taufe]{10,11} [kommen]{8} [sah]{1}, [sagte er]{13} [zu ihnen]{14}: «[Ihr Schlangenbrut]{15,16}! [Wer]{17} [hat]{18} [euch]{19} [darauf gebracht]{18}, [vor]{21} [dem kommenden]{22,23} [Zorn]{24} [zu fliehen]{20}?",
 "MAT.3.8": "[Bringt]{1} [also]{2} [Frucht]{3}, die [der Umkehr]{5,6} [würdig ist]{4}!",
 "MAT.3.9": "Und{1} [meint]{3} [nicht]{2}, ihr könntet [bei euch selbst]{5,6} [sagen]{4}: ‹[Wir haben]{8} [Abraham]{9,10} [zum Vater]{7}.› [Denn]{12} [ich sage]{11} [euch]{13}: [Gott]{16,17} [kann]{15} [aus]{18} [diesen]{21} [Steinen]{19,20} [dem Abraham]{24,25} [Kinder]{23} [erwecken]{22}. ~14(ὅτι leitet die Rede ein)",
 "MAT.3.10": "[Die Axt]{3,4} [liegt]{10} [aber]{2} [schon]{1} [an]{5} [der Wurzel]{6,7} [der Bäume]{8,9}. [Jeder]{11} [Baum]{13} [also]{12}, der [keine]{14} [gute]{17} [Frucht]{16} [bringt]{15}, [wird umgehauen]{18} und{19} [ins]{20} [Feuer]{21} [geworfen]{22}.",
 "MAT.3.11": "[Ich]{1} [taufe]{4} [euch]{3} [zwar]{2} [mit]{5} [Wasser]{6} [zur]{7} [Umkehr]{8}; [der]{9} [aber]{10} [nach]{11} [mir]{12} [kommt]{13}, [ist]{16} [stärker]{14} [als ich]{15}; [ich bin]{19} [nicht]{18} [wert]{20}, [seine]{17} [Sandalen]{21,22} [zu tragen]{23}. [Er]{24} [wird]{26} [euch]{25} [mit]{27} [heiligem]{29} [Geist]{28} und{30} [Feuer]{31} [taufen]{26}.",
 "MAT.3.12": "[Er]{1} hat [die Worfschaufel]{2,3} [in]{4} [der]{5} [Hand]{6}, und{8} [er wird]{9} [seine]{12} [Tenne]{10,11} [gründlich reinigen]{9} und{13} [seinen]{17} [Weizen]{15,16} [in]{18} [die Scheune]{19,20} [sammeln]{14}; [die Spreu]{21,23} [aber]{22} [wird er]{24} [mit unauslöschlichem]{26} [Feuer]{25} [verbrennen]{24}.» ~7(αὐτοῦ «seiner» ist durch «er hat … in der Hand» ausgedrückt)",
 "MAT.3.13": "[Da]{1} [kommt]{2} Jesus{3,4} [aus]{5} [Galiläa]{6,7} [an]{8} [den Jordan]{9,10} [zu]{11} Johannes{12,13}, [um]{14} sich [von]{16} [ihm]{17} [taufen zu lassen]{15}.",
 "MAT.3.14": "Johannes{1,3} [aber]{2} [wollte]{4} [ihn]{5} [daran hindern]{4} [und sagte]{6}: «[Ich]{7} [habe es nötig]{8,9}, [von]{10} [dir]{11} [getauft zu werden]{12}, und{13} [du]{14} [kommst]{15} [zu]{16} [mir]{17}?»",
 "MAT.3.15": "Jesus{3,4} [aber]{2} [antwortete]{1} und [sagte]{5} [zu]{6} [ihm]{7}: «[Lass es]{8} [jetzt]{9} [zu]{8}! [Denn]{11} [so]{10} [gehört es sich]{12,13} [für uns]{14}, [alle]{16} [Gerechtigkeit]{17} [zu erfüllen]{15}.» [Da]{18} [lässt er]{19} [ihn]{20} [gewähren]{19}.",
 "MAT.3.16": "[Als]{1} Jesus{3,4} [aber]{2} [getauft war]{1}, [stieg er]{6} [sogleich]{5} [aus]{7} [dem Wasser]{8,9} [herauf]{6}; und{10} [siehe]{11}, [die Himmel]{13,14} [öffneten sich]{12}, und{15} [er sah]{16} [den Geist]{17} [Gottes]{18} [wie]{20} [eine Taube]{21} [herabkommen]{19} und [auf]{23} [ihn]{24} [kommen]{22}.",
 "MAT.3.17": "Und{1} [siehe]{2}, [eine Stimme]{3} [aus]{4} [den Himmeln]{5,6} [sagte]{7}: «[Dieser]{8} [ist]{9} [mein]{12} [geliebter]{13,14} [Sohn]{10,11}, [an]{15} [dem]{16} [ich Gefallen gefunden habe]{17}.»",
 # ------------------------------------------------------------ Kapitel 4
 "MAT.4.1": "[Da]{1} [wurde]{4} Jesus{2,3} [vom]{8,9} [Geist]{10} [in]{5} [die Wüste]{6,7} [hinaufgeführt]{4}, um [vom]{12,13} [Teufel]{14} [versucht zu werden]{11}.",
 "MAT.4.2": "Und{1} [nachdem er]{2} [vierzig]{4} [Tage]{3} und{5} [vierzig]{7} [Nächte]{6} [gefastet hatte]{2}, [bekam er]{9} [schliesslich]{8} [Hunger]{9}.",
 "MAT.4.3": "Und{1} [der Versucher]{3,4} [trat heran]{2} und [sagte]{5} [zu ihm]{6}: «[Wenn]{7} du [Gottes]{10,11} [Sohn]{8} [bist]{9}, dann [sag]{12}, [dass]{13} [diese]{16} [Steine]{14,15} [zu Broten]{17} [werden]{18}!»",
 "MAT.4.4": "[Er]{1} [aber]{2} [antwortete]{3} und [sagte]{4}: «[Es steht geschrieben]{5}: ‹[Der Mensch]{11,12} [lebt]{10} [nicht]{6} [vom]{7} [Brot]{8} [allein]{9}, [sondern]{13} [von]{14} [jedem]{15} [Wort]{16}, das [aus]{18} [dem Mund]{19} [Gottes]{20} [kommt]{17}.›»",
 "MAT.4.5": "[Da]{1} [nimmt]{2} [ihn]{3} [der Teufel]{4,5} [mit]{2} [in]{6} [die heilige]{7,8} [Stadt]{9}, und{10} [er stellte]{11} [ihn]{12} [auf]{13} [die Zinne]{14,15} [des Tempels]{16,17}",
 "MAT.4.6": "und{1} [sagt]{2} [zu ihm]{3}: «[Wenn]{4} du [Gottes]{7,8} [Sohn]{5} [bist]{6}, dann [wirf]{9} [dich]{10} [hinab]{11}! [Denn]{13} [es steht geschrieben]{12}: ‹[Seinen]{17} [Engeln]{15,16} [wird er]{18} [deinetwegen]{19,20} [Befehl geben]{18}, und{21} [sie werden]{24} [dich]{25} [auf]{22} [Händen]{23} [tragen]{24}, [damit]{26} du [deinen]{32} [Fuss]{30,31} [nicht]{26} [an]{28} [einen Stein]{29} [stösst]{27}.›» ~14(ὅτι leitet das Zitat ein)",
 "MAT.4.7": "Jesus{3,4} [sagte]{1} [zu ihm]{2}: «[Es steht]{6} [auch]{5} [geschrieben]{6}: ‹[Du sollst]{8} [den Herrn]{9}, [deinen]{12} [Gott]{10,11}, [nicht]{7} [auf die Probe stellen]{8}.›»",
 "MAT.4.8": "[Wieder]{1} [nimmt]{2} [ihn]{3} [der Teufel]{4,5} [mit]{2} [auf]{6} [einen sehr]{9} [hohen]{8} [Berg]{7} und{10} [zeigt]{11} [ihm]{12} [alle]{13} [Reiche]{14,15} [der Welt]{16,17} und{18} [ihre]{21} [Herrlichkeit]{19,20}",
 "MAT.4.9": "und{1} [sagte]{2} [zu ihm]{3}: «[Das]{4} [alles]{6} [werde ich]{7} [dir]{5} [geben]{7}, [wenn]{8} du [niederfällst]{9} und [mich]{11} [anbetest]{10}.»",
 "MAT.4.10": "[Da]{1} [sagt]{2} Jesus{4,5} [zu ihm]{3}: «[Geh weg]{6}, [Satan]{7}! [Denn]{9} [es steht geschrieben]{8}: ‹[Den Herrn]{10}, [deinen]{13} [Gott]{11,12}, [sollst du anbeten]{14} und{15} [ihm]{16} [allein]{17} [dienen]{18}.›»",
 "MAT.4.11": "[Da]{1} [verlässt]{2} [ihn]{3} [der Teufel]{4,5}, und{6} [siehe]{7}, [Engel]{8} [traten heran]{9} und{10} [dienten]{11} [ihm]{12}.",
 "MAT.4.12": "[Als er]{1} [aber]{2} [hörte]{1}, [dass]{3} Johannes{4} [ausgeliefert worden war]{5}, [zog er sich]{6} [nach]{7} [Galiläa]{8,9} [zurück]{6}.",
 "MAT.4.13": "Und{1} [er verliess]{2} [Nazaret]{3,4}, [kam]{5} und [liess sich]{6} [in]{7} [Kafarnaum]{8} [nieder]{6}, [das]{9} [am See]{10} liegt, [im]{11} [Gebiet]{12} [von Sebulon]{13} und{14} [Naftali]{15},",
 "MAT.4.14": "[damit]{1} [erfüllt würde]{2}, [was]{3} [durch]{5} Jesaja{6}, [den Propheten]{7,8}, [gesagt ist]{4}: ~9(λέγοντος «sagend» leitet das Zitat ein; durch den Doppelpunkt wiedergegeben)",
 "MAT.4.15": "«[Land]{1} [Sebulon]{2} und{3} [Land]{4} [Naftali]{5}, [Weg]{6} [am Meer]{7}, [jenseits]{8} [des Jordan]{9,10}, [Galiläa]{11} [der Völker]{12,13}:",
 "MAT.4.16": "[das Volk]{1,2}, [das]{3} [in]{5} [Finsternis]{6} [sass]{4}, [hat]{8} [ein grosses]{9} [Licht]{7} [gesehen]{8}, und{10} [denen]{11}, die [im]{13} [Land]{14} und{15} [Schatten]{16} [des Todes]{17} [sassen]{12}, [ist]{19} [ein Licht]{18} [aufgegangen]{19}.» ~20(αὐτοῖς «ihnen» nimmt «denen» auf; nicht eigens wiedergegeben)",
 "MAT.4.17": "[Von da an]{1,2} [begann]{3} Jesus{4,5} [zu verkündigen]{6} und{7} [zu sagen]{8}: «[Kehrt um]{9}, [denn]{11} [das Reich]{12,13} [der Himmel]{14,15} [ist nahe gekommen]{10}!»",
 "MAT.4.18": "[Als er]{1} [aber]{2} [am]{3,4} [See]{5} [von Galiläa]{6,7} [entlangging]{1}, [sah er]{8} [zwei]{9} [Brüder]{10}, Simon{11}, [der]{12} Petrus{14} [genannt wird]{13}, und{15} Andreas{16}, [seinen]{19} [Bruder]{17,18}, [wie sie]{20} [ein Wurfnetz]{21} [in]{22} [den See]{23,24} [warfen]{20}; [sie waren]{25} [nämlich]{26} Fischer{27}.",
 "MAT.4.19": "Und{1} [er sagt]{2} [zu ihnen]{3}: «[Kommt]{4} [mir]{6} [nach]{5}, und{7} [ich werde]{8} [euch]{9} [zu Menschenfischern]{10,11} [machen]{8}!»",
 "MAT.4.20": "[Sie]{1} [aber]{2} [liessen]{4} [sogleich]{3} [die Netze]{5,6} [liegen]{4} [und folgten]{7} [ihm]{8}.",
 "MAT.4.21": "Und{1} [als er]{2} [von dort]{3} [weiterging]{2}, [sah er]{4} [zwei]{6} [andere]{5} [Brüder]{7}, Jakobus{8}, [den Sohn]{9} [des Zebedäus]{10,11}, und{12} Johannes{13}, [seinen]{16} [Bruder]{14,15}, [im]{17,18} [Boot]{19} [mit]{20} Zebedäus{21}, [ihrem]{24} [Vater]{22,23}, [wie sie]{25} [ihre]{28} [Netze]{26,27} [herrichteten]{25}; und{29} [er rief]{30} [sie]{31}.",
 "MAT.4.22": "[Sie]{1} [aber]{2} [liessen]{4} [sogleich]{3} [das Boot]{5,6} und{7} [ihren]{10} [Vater]{8,9} [zurück]{4} [und folgten]{11} [ihm]{12}.",
 "MAT.4.23": "Und{1} [er zog]{2} [in]{3} [ganz]{4} [Galiläa]{5,6} [umher]{2}, [lehrte]{7} [in]{8} [ihren]{11} [Synagogen]{9,10} und{12} [verkündigte]{13} [das Evangelium]{14,15} [vom Reich]{16,17} und{18} [heilte]{19} [jede]{20} [Krankheit]{21} und{22} [jedes]{23} [Leiden]{24} [im]{25,26} [Volk]{27}.",
 "MAT.4.24": "Und{1} [die Kunde]{3,4} [von ihm]{5} [verbreitete sich]{2} [in]{6} [ganz]{7} [Syrien]{8,9}. Und{10} [man brachte]{11} [ihm]{12} [alle]{13} [Kranken]{14,15,16}, die [von mancherlei]{17} [Krankheiten]{18} und{19} [Qualen]{20} [geplagt waren]{21}: [Besessene]{22} und{23} [Mondsüchtige]{24} und{25} [Gelähmte]{26}; und{27} [er heilte]{28} [sie]{29}.",
 "MAT.4.25": "Und{1} [es folgten]{2} [ihm]{3} [viele]{5} [Menschenmengen]{4} [aus]{6} [Galiläa]{7,8} und{9} [der Dekapolis]{10} und{11} [Jerusalem]{12} und{13} [Judäa]{14} und{15} [von jenseits]{16} [des Jordan]{17,18}.",
}

GSW = {
 # ------------------------------------------------------------ Kapitel 3
 "MAT.3.1": "[I]{1} [dene]{5} [Täg]{3,4} [aber]{2} [tritt]{6} [de Johannes]{7} [de Täufer]{8,9} [uf]{6} [und verchündet]{10} [i]{11} [de Wüeschti]{12,13} [vo Judäa]{14,15}",
 "MAT.3.2": "und{1} [seit]{2}: «[Chehred um]{3}, [dänn]{5} [s Riich]{6,7} [vo de Himel]{8,9} [isch nöch choo]{4}!»",
 "MAT.3.3": "[Dänn]{2} [dä]{1} [isch]{3} [es, vo däm]{4} [dur]{6} [de Jesaja]{7}, [de Prophet]{8,9}, [gseit worden isch]{5}: «[E Stimm]{11} [vo eim, wo rüeft]{12} [i]{13} [de Wüeschti]{14,15}: ‹[Mached]{16} [de Wäg]{17,18} [vom Herr]{19} [parat]{16}, [mached]{21} [sini]{24} [Pfäd]{22,23} [grad]{20}!›» ~10(λέγοντος «sagend» leitet s Zitat ii; dur de Doppelpunkt widergää)",
 "MAT.3.4": "[De Johannes]{3,4} [sälber]{1} [aber]{2} [hät]{5} [sis]{8} [Gwand]{6,7} [us]{9} [Kamelhaar]{10,11} und{12} [en lädrige]{14} [Gurt]{13} [um]{15} [sini]{18} [Hüfte]{16,17} [ghaa]{5}; [sis]{23} [Ässe]{19,21} [aber]{20} [sind]{22} [Heuschrecke]{24} und{25} [wilde]{27} [Hung]{26} [gsii]{22}.",
 "MAT.3.5": "[Dänn]{1} [isch]{2} Jerusalem{5} und{6} [ganz]{7} [Judäa]{8,9} und{10} [di ganz]{11,12} [Gäged]{13} [um de Jordan]{14,15} [zu]{3} [ihm]{4} [usegange]{2},",
 "MAT.3.6": "und{1} [si händ sich]{2} [im]{3,4} [Fluss]{6} Jordan{5} [vo]{7} [ihm]{8} [la taufe]{2} [und händ]{9} [iri]{12} [Sünde]{10,11} [bekännt]{9}.",
 "MAT.3.7": "[Wo er]{1} [aber]{2} [vili]{3} [vo de]{4} [Pharisäer]{5} und{6} [Sadduzäer]{7} [zu]{9} [sinere]{12} [Taufi]{10,11} [hät gseh]{1} [choo]{8}, [hät er]{13} [zu ine]{14} [gseit]{13}: «[Ir Schlangebruet]{15,16}! [Wer]{17} [hät]{18} [eu]{19} [druf bracht]{18}, [vor]{21} [em]{22} [Zorn]{24}, [wo chunnt]{23}, [z flüchte]{20}?",
 "MAT.3.8": "[Bringed]{1} [also]{2} [Frucht]{3}, wo [zur Umkehr]{5,6} [passt]{4}!",
 "MAT.3.9": "Und{1} [meined]{3} [nöd]{2}, ir chönnted [bi eu sälber]{5,6} [säge]{4}: ‹[Mir händ]{8} [de Abraham]{9,10} [zum Vatter]{7}.› [Dänn]{12} [ich säg]{11} [eu]{13}: [Gott]{16,17} [cha]{15} [us]{18} [dene]{21} [Stei]{19,20} [em Abraham]{24,25} [Chind]{23} [erwecke]{22}. ~14(ὅτι leitet d Red ii)",
 "MAT.3.10": "[D Axt]{3,4} [liit]{10} [aber]{2} [scho]{1} [a]{5} [de Wurzle]{6,7} [vo de Bäum]{8,9}. [Jede]{11} [Baum]{13} [also]{12}, wo [kei]{14} [gueti]{17} [Frucht]{16} [bringt]{15}, [wird umghaue]{18} und{19} [is]{20} [Füür]{21} [gworfe]{22}.",
 "MAT.3.11": "[Ich]{1} [tauf]{4} [eu]{3} [zwar]{2} [mit]{5} [Wasser]{6} [zur]{7} [Umkehr]{8}; [dä]{9} [aber]{10}, wo [nach]{11} [mir]{12} [chunnt]{13}, [isch]{16} [stärcher]{14} [als ich]{15}; [ich bi]{19} [nöd]{18} [wärt]{20}, [sini]{17} [Sandale]{21,22} [z träge]{23}. [Er]{24} [wird]{26} [eu]{25} [mit]{27} [heilige]{29} [Geischt]{28} und{30} [Füür]{31} [taufe]{26}.",
 "MAT.3.12": "[Er]{1} hät [d Worfschufle]{2,3} [i]{4} [de]{5} [Hand]{6}, und{8} [er wird]{9} [sis]{12} [Tenn]{10,11} [ganz suuber mache]{9} und{13} [sin]{17} [Weize]{15,16} [i]{18} [d Schüür]{19,20} [sammle]{14}; [d Sprüür]{21,23} [aber]{22} [wird er]{24} [mit Füür]{25}, [wo nie uusgaat]{26}, [verbrenne]{24}.» ~7(αὐτοῦ «sinere» isch dur «er hät … i de Hand» usdruckt)",
 "MAT.3.13": "[Dänn]{1} [chunnt]{2} [de Jesus]{3,4} [vo]{5} [Galiläa]{6,7} [a]{8} [de Jordan]{9,10} [zum]{11} [Johannes]{12,13}, [zum]{14} sich [vo]{16} [ihm]{17} [la taufe]{15}.",
 "MAT.3.14": "[De Johannes]{1,3} [aber]{2} [hät]{4} [en]{5} [welle devo abhalte]{4} [und gseit]{6}: «[Ich]{7} [han s nötig]{8,9}, [vo]{10} [dir]{11} [tauft z wärde]{12}, und{13} [du]{14} [chunnsch]{15} [zu]{16} [mir]{17}?»",
 "MAT.3.15": "[De Jesus]{3,4} [aber]{2} [hät gantwortet]{1} und [zu]{6} [ihm]{7} [gseit]{5}: «[Lass es]{8} [jetzt]{9} [zue]{8}! [Dänn]{11} [so]{10} [ghört es sich]{12,13} [für üs]{14}, [alli]{16} [Grächtigkeit]{17} [z erfülle]{15}.» [Dänn]{18} [laat er]{19} [en]{20} [mache]{19}.",
 "MAT.3.16": "[Wo]{1} [de Jesus]{3,4} [aber]{2} [tauft worde isch]{1}, [isch er]{6} [grad]{5} [us]{7} [em Wasser]{8,9} [ufecho]{6}; und{10} [lueg]{11}, [d Himel]{13,14} [sind ufgange]{12}, und{15} [er hät]{16} [de Geischt]{17} [vo Gott]{18} [wie]{20} [e Tuube]{21} [gseh]{16} [abecho]{19} und [uf]{23} [ihn]{24} [choo]{22}.",
 "MAT.3.17": "Und{1} [lueg]{2}, [e Stimm]{3} [us]{4} [de Himel]{5,6} [hät gseit]{7}: «[Dä]{8} [isch]{9} [min]{12} [liebe]{13,14} [Sohn]{10,11}, [a däm]{15,16} [han ich Gfalle gfunde]{17}.»",
 # ------------------------------------------------------------ Kapitel 4
 "MAT.4.1": "[Dänn]{1} [isch]{4} [de Jesus]{2,3} [vom]{8,9} [Geischt]{10} [i]{5} [d Wüeschti]{6,7} [ufegfüert worde]{4}, für [vom]{12,13} [Tüüfel]{14} [versuecht z wärde]{11}.",
 "MAT.4.2": "Und{1} [nachdem er]{2} [vierzg]{4} [Täg]{3} und{5} [vierzg]{7} [Nächt]{6} [gfaschtet hät]{2}, [hät er]{9} [am Schluss]{8} [Hunger übercho]{9}.",
 "MAT.4.3": "Und{1} [de Versuecher]{3,4} [isch anecho]{2} und [hät]{5} [zu ihm]{6} [gseit]{5}: «[Wänn]{7} du [de Sohn]{8} [vo Gott]{10,11} [bisch]{9}, dänn [säg]{12}, [dass]{13} [die]{16} [Stei]{14,15} [zu Broot]{17} [wärded]{18}!»",
 "MAT.4.4": "[Er]{1} [aber]{2} [hät gantwortet]{3} und [gseit]{4}: «[Es staat gschribe]{5}: ‹[De Mänsch]{11,12} [läbt]{10} [nöd]{6} [vom]{7} [Broot]{8} [ellei]{9}, [sondern]{13} [vo]{14} [jedem]{15} [Wort]{16}, wo [us]{18} [em Mund]{19} [vo Gott]{20} [chunnt]{17}.›»",
 "MAT.4.5": "[Dänn]{1} [nimmt]{2} [en]{3} [de Tüüfel]{4,5} [mit]{2} [i]{6} [di heilig]{7,8} [Stadt]{9}, und{10} [er hät]{11} [en]{12} [uf]{13} [d Zinne]{14,15} [vom Tämpel]{16,17} [gstellt]{11}",
 "MAT.4.6": "und{1} [seit]{2} [zu ihm]{3}: «[Wänn]{4} du [de Sohn]{5} [vo Gott]{7,8} [bisch]{6}, dänn [rüer]{9} [dich]{10} [abe]{11}! [Es staat]{12} [nämli]{13} [gschribe]{12}: ‹[Sine]{17} [Ängel]{15,16} [wird er]{18} [dinetwäge]{19,20} [Befehl gää]{18}, und{21} [si wärded]{24} [dich]{25} [uf]{22} [de Händ]{23} [träge]{24}, [demit]{26} du [din]{32} [Fuess]{30,31} [nöd]{26} [a]{28} [en Stei]{29} [stoosch]{27}.›» ~14(ὅτι leitet s Zitat ii)",
 "MAT.4.7": "[De Jesus]{3,4} [hät]{1} [zu ihm]{2} [gseit]{1}: «[Es staat]{6} [au]{5} [gschribe]{6}: ‹[Du söllsch]{8} [de Herr]{9}, [din]{12} [Gott]{10,11}, [nöd]{7} [uf d Prob stelle]{8}.›»",
 "MAT.4.8": "[Wider]{1} [nimmt]{2} [en]{3} [de Tüüfel]{4,5} [mit]{2} [uf]{6} [en ganz]{9} [hööche]{8} [Bärg]{7} und{10} [zeigt]{11} [ihm]{12} [alli]{13} [Riich]{14,15} [vo de Wält]{16,17} und{18} [iri]{21} [Herrlichkeit]{19,20}",
 "MAT.4.9": "und{1} [hät]{2} [zu ihm]{3} [gseit]{2}: «[Das]{4} [alles]{6} [gib ich]{7} [dir]{5}, [wänn]{8} du [di uf de Bode wirfsch]{9} und [mich]{11} [aabättisch]{10}.»",
 "MAT.4.10": "[Dänn]{1} [seit]{2} [de Jesus]{4,5} [zu ihm]{3}: «[Gang wäg]{6}, [Satan]{7}! [Es staat]{8} [nämli]{9} [gschribe]{8}: ‹[De Herr]{10}, [din]{13} [Gott]{11,12}, [söllsch du aabätte]{14} und{15} [ihm]{16} [ellei]{17} [diene]{18}.›»",
 "MAT.4.11": "[Dänn]{1} [laat]{2} [de Tüüfel]{4,5} [vo ihm]{3} [ab]{2}, und{6} [lueg]{7}, [Ängel]{8} [sind anecho]{9} und{10} [händ]{11} [ihm]{12} [dienet]{11}.",
 "MAT.4.12": "[Wo er]{1} [aber]{2} [ghört hät]{1}, [dass]{3} [de Johannes]{4} [usgliferet worde isch]{5}, [hät er sich]{6} [uf]{7} [Galiläa]{8,9} [zruggzoge]{6}.",
 "MAT.4.13": "Und{1} [er hät]{2} [Nazaret]{3,4} [verlaa]{2}, [isch]{5,6} [uf]{7} [Kafarnaum]{8} [cho wohne]{5,6}, [wo]{9} [am See]{10} liit, [im]{11} [Gebiet]{12} [vo Sebulon]{13} und{14} [Naftali]{15},",
 "MAT.4.14": "[demit]{1} [erfüllt wird]{2}, [was]{3} [dur]{5} [de Jesaja]{6}, [de Prophet]{7,8}, [gseit worden isch]{4}: ~9(λέγοντος «sagend» leitet s Zitat ii; dur de Doppelpunkt widergää)",
 "MAT.4.15": "«[S Land]{1} [Sebulon]{2} und{3} [s Land]{4} [Naftali]{5}, [de Wäg]{6} [am Meer]{7}, [änet]{8} [em Jordan]{9,10}, [Galiläa]{11} [vo de Völker]{12,13}:",
 "MAT.4.16": "[s Volk]{1,2}, [wo]{3} [i]{5} [de Fiischteri]{6} [gsässe isch]{4}, [hät]{8} [es grosses]{9} [Liecht]{7} [gseh]{8}, und{10} [dene]{11}, wo [im]{13} [Land]{14} und{15} [Schatte]{16} [vom Tod]{17} [gsässe sind]{12}, [isch]{19} [es Liecht]{18} [ufgange]{19}.» ~20(αὐτοῖς «ine» nimmt «dene» uf; nöd extra widergää)",
 "MAT.4.17": "[Vo dänn aa]{1,2} [hät]{3} [de Jesus]{4,5} [aagfange]{3} [z verchünde]{6} und{7} [z säge]{8}: «[Chehred um]{9}, [dänn]{11} [s Riich]{12,13} [vo de Himel]{14,15} [isch nöch choo]{10}!»",
 "MAT.4.18": "[Wo er]{1} [aber]{2} [am]{3,4} [See]{5} [vo Galiläa]{6,7} [entlang gange isch]{1}, [hät er]{8} [zwei]{9} [Brüeder]{10} [gseh]{8}, [de Simon]{11}, [wo]{12} mer [Petrus]{14} [seit]{13}, und{15} [de Andreas]{16}, [sin]{19} [Brueder]{17,18}, [wie si]{20} [es Wurfnetz]{21} [in]{22} [de See]{23,24} [gworfe händ]{20}; [si sind]{25} [nämli]{26} Fischer{27} [gsii]{25}.",
 "MAT.4.19": "Und{1} [er seit]{2} [zu ine]{3}: «[Chömed]{4} [mir]{6} [nache]{5}, und{7} [ich mache]{8} [eu]{9} [zu Mänschefischer]{10,11}!»",
 "MAT.4.20": "[Si]{1} [aber]{2} [händ]{4} [grad]{3} [d Netz]{5,6} [la ligge]{4} [und sind]{7} [ihm]{8} [nachegange]{7}.",
 "MAT.4.21": "Und{1} [wo er]{2} [vo dört]{3} [wiitergange isch]{2}, [hät er]{4} [zwei]{6} [anderi]{5} [Brüeder]{7} [gseh]{4}, [de Jakobus]{8}, [de Sohn]{9} [vom Zebedäus]{10,11}, und{12} [de Johannes]{13}, [sin]{16} [Brueder]{14,15}, [im]{17,18} [Boot]{19} [mit]{20} [em Zebedäus]{21}, [irem]{24} [Vatter]{22,23}, [wie si]{25} [iri]{28} [Netz]{26,27} [parat gmacht händ]{25}; und{29} [er hät]{30} [si]{31} [grüeft]{30}.",
 "MAT.4.22": "[Si]{1} [aber]{2} [händ]{4} [grad]{3} [s Boot]{5,6} und{7} [ire]{10} [Vatter]{8,9} [zrugglaa]{4} [und sind]{11} [ihm]{12} [nachegange]{11}.",
 "MAT.4.23": "Und{1} [er isch]{2} [i]{3} [ganz]{4} [Galiläa]{5,6} [umezoge]{2}, [hät]{7} [i]{8} [irne]{11} [Synagoge]{9,10} [glehrt]{7} und{12} [s Evangelium]{14,15} [vom Riich]{16,17} [verchündet]{13} und{18} [jedi]{20} [Chranket]{21} und{22} [jedes]{23} [Liide]{24} [im]{25,26} [Volk]{27} [gheilt]{19}.",
 "MAT.4.24": "Und{1} [de Ruef]{3,4} [vo ihm]{5} [isch]{2} [i]{6} [ganz]{7} [Syrie]{8,9} [usegange]{2}. Und{10} [mer hät]{11} [ihm]{12} [alli]{13} [Chranke]{14,15,16} [bracht]{11}, wo [vo allerlei]{17} [Chrankete]{18} und{19} [Quale]{20} [plaget gsii sind]{21}: [Bsässni]{22} und{23} [Mondsüchtigi]{24} und{25} [Glähmti]{26}; und{27} [er hät]{28} [si]{29} [gheilt]{28}.",
 "MAT.4.25": "Und{1} [vili]{5} [Schaare vo Lüüt]{4} [sind]{2} [ihm]{3} [nachegange]{2} [us]{6} [Galiläa]{7,8} und{9} [de Dekapolis]{10} und{11} [Jerusalem]{12} und{13} [Judäa]{14} und{15} [vo änet]{16} [em Jordan]{17,18}.",
}

# (Stelle, Zieltext, Art, griechisch, wörtlicher, weitere Möglichkeiten, Begründung)
DEC_DE = [
 ("MAT.3.1", "In jenen Tagen", "literal", "Ἐν δὲ ταῖς ἡμέραις ἐκείναις", None, None,
  "Lose Zeitangabe: Zwischen der Rückkehr nach Nazaret ([[MAT.2.23]]) und dem Auftreten des Johannes liegen nach dem Erzählten viele Jahre. Die Wendung verbindet die Erzählung, ohne einen Zeitpunkt zu nennen."),
 ("MAT.3.1", "tritt", "adapted", "παραγίνεται", "kommt herbei", ["erscheint", "kommt"],
  "παραγίνομαι «herbeikommen, sich einfinden»; beim ersten Erscheinen des Johannes «auftreten», in [[MAT.3.13]] «kommt». Grundentscheid für Kapitel 3–4: Das erzählende Präsens des Matthäus bleibt erhalten, auch im Wechsel mit Vergangenheitsformen (vgl. [[MAT.4.5]])."),
 ("MAT.3.1", "Wüste", "literal", "ἐρήμῳ", None, ["Steppe", "Einöde"],
  "ἔρημος ist das unbewohnte, karge Land, nicht unbedingt Sandwüste; gemeint ist das Gebiet am unteren Jordan."),
 ("MAT.3.2", "Kehrt um", "interpretive", "Μετανοεῖτε", "Ändert euren Sinn", ["Tut Busse"],
  "Wie [[MRK.1.15]]: μετανοέω ist wörtlich ein Umdenken; im biblischen Zusammenhang schwingt die prophetische Aufforderung zur Rückkehr zu Gott mit. «Busse» lässt an Strafe oder Wiedergutmachung denken. Einheitlich im ganzen Matthäusevangelium μετανοέω «umkehren», μετάνοια «Umkehr» ([[MAT.3.8]], [[MAT.3.11]]). Johannes ([[MAT.3.2]]) und Jesus ([[MAT.4.17]]) verkündigen bei Matthäus wörtlich dasselbe."),
 ("MAT.3.2", "das Reich der Himmel", "traditional", "ἡ βασιλεία τῶν οὐρανῶν", "die Königsherrschaft der Himmel", ["das Himmelreich", "das Reich Gottes"],
  "Einheitlicher Matthäus-Begriff: Matthäus sagt meist «Reich der Himmel» (nach MACULA-Lemmata 32-mal, «Reich Gottes» nur 4-mal), wohl nach jüdischem Brauch, den Gottesnamen zu umschreiben; gemeint ist dieselbe Sache wie «Reich Gottes» bei Markus ([[MRK.1.15]]). Der Plural «Himmel» bleibt wie im Griechischen stehen. βασιλεία meint zuerst Gottes Herrschaft als Geschehen, nicht ein Gebiet; «Reich» folgt der vertrauten Wiedergabe."),
 ("MAT.3.2", "ist nahe gekommen", "literal", "ἤγγικεν", None, ["ist nahe", "ist da"],
  "Perfekt wie in [[MRK.1.15]]: ein erreichter Zustand. Ob das Reich als schon angebrochen oder als unmittelbar bevorstehend gedacht ist, ist umstritten; «nahe gekommen» lässt beides offen."),
 ("MAT.3.3", "gesagt ist", "literal", "ῥηθεὶς", "der Gesagte", None,
  "Matthäus leitet Schriftworte mit einer festen Formel ein («was durch den Propheten gesagt ist»); sie ist im ganzen Evangelium gleich wiedergegeben (vgl. [[MAT.4.14]]). Hier ohne «damit erfüllt würde»: Johannes ist der, von dem Jesaja spricht ([[ISA.40.3]])."),
 ("MAT.3.3", "des Herrn", "literal", "κυρίου", None, ["JHWHs"],
  "In [[ISA.40.3]] steht im hebräischen Text der Gottesname, in der griechischen Bibel κύριος. Matthäus bezieht den «Weg des Herrn» auf Jesus, dem Johannes vorausgeht. Anders als [[MRK.1.2]] zitiert Matthäus hier nur Jesaja; das Wort aus [[MAL.3.1]] folgt erst in [[MAT.11.10]]."),
 ("MAT.3.4", "aus Kamelhaar", "literal", "ἀπὸ τριχῶν καμήλου", "aus Haaren eines Kamels", None,
  "Ein grobes Gewand und der Ledergurt erinnern an Elija ([[2KI.1.8]]); vgl. [[MAT.11.14]] und [[MAT.17.12]]–[[MAT.17.13]]."),
 ("MAT.3.4", "Heuschrecken", "literal", "ἀκρίδες", None, None,
  "Heuschrecken waren nach [[LEV.11.22]] erlaubte Speise."),
 ("MAT.3.5", "Jerusalem", "literal", "Ἱεροσόλυμα", None, ["die Leute aus Jerusalem"],
  "Die Ortsnamen stehen für ihre Bewohner; das Verb steht im Singular («zog»). Die Übersetzung behält das Bild bei; in [[MAT.3.6]] folgt «sie liessen sich taufen»."),
 ("MAT.3.7", "Pharisäern", "literal", "Φαρισαίων", None, None,
  "Pharisäer und Sadduzäer waren jüdische Gruppen mit unterschiedlichen Lehren (die Sadduzäer bestritten z. B. die Auferstehung, [[MAT.22.23]]); Matthäus nennt sie mehrmals zusammen ([[MAT.16.1]]). Grundsatz: Gruppennamen neutral wiedergeben; der scharfe Ton liegt im Wort des Johannes, nicht in der Bezeichnung."),
 ("MAT.3.7", "Ihr Schlangenbrut", "adapted", "Γεννήματα ἐχιδνῶν", "Brut von Vipern", ["Ihr Natterngezücht", "Ihr Otternbrut"],
  "ἔχιδνα ist eine Giftschlange. Das Scheltwort steht bei Matthäus noch in [[MAT.12.34]] und [[MAT.23.33]] (dort im Mund Jesu) und ist einheitlich «Schlangenbrut» übersetzt. Bei Matthäus richtet Johannes es an Pharisäer und Sadduzäer, bei Lukas an die Menge ([[LUK.3.7]])."),
 ("MAT.3.7", "darauf gebracht", "adapted", "ὑπέδειξεν", "gezeigt", ["gewarnt", "gelehrt"],
  "ὑποδείκνυμι heisst «zeigen, vor Augen führen, anweisen». Viele verstehen die Frage als ironisch."),
 ("MAT.3.7", "dem kommenden Zorn", "literal", "τῆς μελλούσης ὀργῆς", None, ["dem bevorstehenden Gericht"],
  "Gemeint ist Gottes Zorn im Gericht, das nach [[MAT.3.10]]–[[MAT.3.12]] unmittelbar bevorsteht."),
 ("MAT.3.8", "würdig ist", "literal", "ἄξιον", None, ["entspricht"],
  "Frucht ist ein Bild für das Tun, das der Umkehr entsprechen soll. καρπός einheitlich «Frucht» (vgl. [[MAT.3.10]], [[MAT.7.16]]–[[MAT.7.20]])."),
 ("MAT.3.9", "bei euch selbst", "literal", "ἐν ἑαυτοῖς", "in euch selbst", ["untereinander"],
  "Gemeint ist das innere Sprechen: ein Gedanke, auf den man sich verlässt."),
 ("MAT.3.9", "Kinder erwecken", "literal", "ἐγεῖραι τέκνα", None, ["Kinder hervorbringen", "Kinder schaffen"],
  "ἐγείρω «aufrichten, erwecken» steht sonst oft für das Auferwecken. Im Hebräischen und Aramäischen klingen «Söhne» (banim) und «Steine» (abanim) ähnlich; ob dem Wort ein solches Wortspiel zugrunde liegt, lässt sich nicht nachweisen."),
 ("MAT.3.10", "liegt", "literal", "κεῖται", None, ["ist angelegt"],
  "Präsens: Das Gericht steht unmittelbar bevor. Ebenso die Präsensformen «wird umgehauen» und «geworfen»; Jesus braucht den zweiten Satz wörtlich in [[MAT.7.19]]."),
 ("MAT.3.11", "zur Umkehr", "interpretive", "εἰς μετάνοιαν", None, ["auf Umkehr hin", "wegen der Umkehr"],
  "εἰς kann Ziel oder Grund angeben: Die Taufe führt zur Umkehr oder setzt sie voraus. Anders als [[MRK.1.4]] verbindet Matthäus die Taufe des Johannes nicht mit «Vergebung der Sünden»; die Wendung steht bei ihm beim Abendmahl ([[MAT.26.28]])."),
 ("MAT.3.11", "wert", "literal", "ἱκανὸς", "genügend", ["würdig", "gut genug"],
  "Wie [[MRK.1.7]]. Bei Matthäus geht es ums Tragen der Sandalen (βαστάσαι), bei Markus ums Lösen der Riemen; beides war Arbeit von Sklaven."),
 ("MAT.3.11", "mit heiligem Geist und Feuer", "interpretive", "ἐν πνεύματι ἁγίῳ καὶ πυρί", None, ["im heiligen Geist und im Feuer"],
  "Ohne Artikel, im Gegenüber zu «mit Wasser»; ἐν kann «mit» oder «in» heissen. «Feuer» kann Läuterung oder (nach [[MAT.3.10]] und [[MAT.3.12]]) Gericht meinen; der Text entscheidet nicht. πνεῦμα ἅγιον einheitlich «heiliger Geist». Zur Lesart ohne «und Feuer» siehe die Alternative."),
 ("MAT.3.12", "Er", "adapted", "οὗ", "dessen", None,
  "Der Relativsatz («dessen Worfschaufel in seiner Hand ist») ist als eigener Satz wiedergegeben."),
 ("MAT.3.12", "Worfschaufel", "literal", "πτύον", None, ["Wurfschaufel"],
  "Mit der Worfschaufel warf man das gedroschene Getreide in den Wind; die leichte Spreu flog weg, die Körner fielen auf die Tenne. Bild für das Gericht, das scheidet."),
 ("MAT.3.12", "unauslöschlichem", "literal", "ἀσβέστῳ", None, ["nie verlöschendem"], None),
 ("MAT.3.14", "wollte ihn daran hindern", "interpretive", "διεκώλυεν αὐτὸν", "hinderte ihn", ["versuchte, ihn davon abzuhalten"],
  "Imperfekt des Versuchs: Johannes will Jesus abhalten, tut es aber nicht. Das Gespräch [[MAT.3.14]]–[[MAT.3.15]] hat nur Matthäus."),
 ("MAT.3.15", "Lass es jetzt zu", "literal", "Ἄφες ἄρτι", None, ["Lass es für jetzt geschehen"],
  "ἀφίημι heisst «lassen, zulassen»; am Ende des Verses steht dasselbe Verb («lässt ihn gewähren»)."),
 ("MAT.3.15", "alle Gerechtigkeit zu erfüllen", "interpretive", "πληρῶσαι πᾶσαν δικαιοσύνην", None, ["alles zu tun, was Gott will", "alles zu erfüllen, was recht ist"],
  "Grundentscheid für das Matthäusevangelium: δικαιοσύνη einheitlich «Gerechtigkeit» (7-mal, z. B. [[MAT.5.6]], [[MAT.5.20]], [[MAT.6.33]]). Gemeint ist bei Matthäus meist das rechte Tun nach Gottes Willen. Was es heisst, dass Jesus «alle Gerechtigkeit erfüllt», wird verschieden erklärt: Gehorsam gegenüber Gottes Willen, Verbundenheit mit dem umkehrenden Volk, Erfüllung der Schrift (vgl. πληρόω in [[MAT.4.14]], [[MAT.5.17]]). «Uns» kann Jesus und Johannes meinen oder Jesus allein."),
 ("MAT.3.16", "sogleich", "literal", "εὐθὺς", None, ["sofort"],
  "Einheitlicher Matthäus-Begriff: εὐθύς und εὐθέως «sogleich» (Mundart «grad»), ebenso [[MAT.4.20]], [[MAT.4.22]]."),
 ("MAT.3.16", "siehe", "literal", "ἰδοὺ", None, ["und sieh", "plötzlich"],
  "Einheitlicher Matthäus-Begriff: ἰδού «siehe» (Mundart «lueg»). Matthäus führt damit oft etwas Unerwartetes ein (62-mal; hier, [[MAT.3.17]], [[MAT.4.11]])."),
 ("MAT.3.16", "die Himmel öffneten sich", "literal", "ἠνεῴχθησαν οἱ οὐρανοί", None, ["der Himmel öffnete sich"],
  "Plural wie im Griechischen (so auch [[MAT.3.17]]). Ruhiger als das «Aufreissen» bei [[MRK.1.10]]. Zur Lesart «öffneten sich ihm» siehe die Alternative."),
 ("MAT.3.16", "den Geist Gottes", "literal", "πνεῦμα θεοῦ", "Geist Gottes", None,
  "Im SBLGNT ohne Artikel (wie WH); Treg, NA28 und RP lesen τὸ πνεῦμα τοῦ θεοῦ. Im Deutschen ergibt beides «den Geist Gottes», deshalb keine eigene Alternative. Laut der automatischen Zuordnung lesen 032 und 04 mit Artikeln; 01 und 03 sind als «liest anders» geführt, haben im erfassten Wortlaut aber πνεῦμα θεοῦ ohne Artikel (als Kürzel). Ebenso ändert ein καί vor «auf ihn kommen» (Treg, NA28, RP) den deutschen Wortlaut nicht."),
 ("MAT.3.17", "Dieser ist mein geliebter Sohn", "literal", "Οὗτός ἐστιν ὁ υἱός μου ὁ ἀγαπητός", "Dieser ist mein Sohn, der geliebte", ["Das ist mein Sohn, den ich liebe"],
  "Bei Matthäus spricht die Stimme über Jesus («Dieser ist»), bei [[MRK.1.11]] zu ihm («Du bist»); vgl. [[MAT.17.5]]. Anklänge an [[PSA.2.7]] und [[ISA.42.1]]. ἀγαπητός kann auch «einzig» mitmeinen (vgl. [[GEN.22.2]] in der griechischen Bibel)."),
 ("MAT.3.17", "an dem ich Gefallen gefunden habe", "interpretive", "ἐν ᾧ εὐδόκησα", None, ["an dem ich Freude habe", "den ich erwählt habe"],
  "Der Aorist kann zeitlos verstanden werden. Gleich übersetzt wie [[MRK.1.11]]."),
 # Kapitel 4
 ("MAT.4.1", "hinaufgeführt", "literal", "ἀνήχθη", None, ["geführt"],
  "ἀνάγω «hinaufführen»: vom Jordantal hinauf ins Bergland der Wüste. [[MRK.1.12]] sagt «treibt hinaus»."),
 ("MAT.4.1", "Teufel", "literal", "διαβόλου", "Verleumder", ["Widersacher"],
  "διάβολος heisst wörtlich «Verleumder»; einheitlich «Teufel». In [[MAT.4.3]] heisst er «der Versucher», in [[MAT.4.10]] «Satan» (hebräisch «Widersacher»); die Übersetzung behält die drei Bezeichnungen bei."),
 ("MAT.4.1", "versucht zu werden", "literal", "πειρασθῆναι", None, ["auf die Probe gestellt zu werden"],
  "πειράζω heisst prüfen, auf die Probe stellen, auch zur Sünde verleiten. Vorschlag für Matthäus: πειράζω «versuchen», wo der Teufel handelt ([[MAT.4.1]], [[MAT.4.3]]); wo Menschen Jesus prüfen (z. B. [[MAT.16.1]], [[MAT.22.35]]), nach dem Zusammenhang «auf die Probe stellen». Im Vaterunser steht πειρασμός «Versuchung» ([[MAT.6.13]])."),
 ("MAT.4.2", "vierzig", "literal", "τεσσεράκοντα", None, None,
  "Vierzig Tage und Nächte erinnern an Mose auf dem Berg ([[EXO.34.28]]) und an Elija ([[1KI.19.8]]); die Antworten Jesu stammen aus dem Rückblick auf Israels vierzig Jahre in der Wüste ([[DEU.8.2]]–[[DEU.8.3]])."),
 ("MAT.4.3", "der Versucher", "literal", "ὁ πειράζων", "der Versuchende", None,
  "Partizip mit Artikel als Bezeichnung, vom selben Verb wie «versucht» in [[MAT.4.1]]."),
 ("MAT.4.3", "trat heran", "literal", "προσελθὼν", "herangetreten", ["kam zu ihm"],
  "Vorschlag für Matthäus: προσέρχομαι, ein häufiges Wort des Evangeliums (51-mal), einheitlich «herantreten» (Mundart «anechoo»); ebenso [[MAT.4.11]]."),
 ("MAT.4.3", "Wenn du Gottes Sohn bist", "interpretive", "Εἰ υἱὸς εἶ τοῦ θεοῦ", None, ["Da du Gottes Sohn bist", "Wenn du wirklich Gottes Sohn bist"],
  "Die Bedingung knüpft an die Himmelsstimme an ([[MAT.3.17]]). Viele verstehen sie als Voraussetzung, die der Versucher für seine Zwecke nutzen will; andere hören einen Zweifel heraus. «Gottes Sohn» ohne Artikel wie im Griechischen; ebenso [[MAT.4.6]]."),
 ("MAT.4.4", "Es steht geschrieben", "literal", "Γέγραπται", "Es ist geschrieben", None,
  "Perfekt: Das Geschriebene gilt fort. Die drei Antworten Jesu stammen aus [[DEU.8.3]], [[DEU.6.16]] und [[DEU.6.13]]."),
 ("MAT.4.4", "lebt", "adapted", "ζήσεται", "wird leben", None,
  "Das Futur hat hier den Sinn einer allgemein gültigen Aussage ([[DEU.8.3]])."),
 ("MAT.4.4", "aus dem Mund Gottes kommt", "adapted", "ἐκπορευομένῳ διὰ στόματος θεοῦ", "das durch den Mund Gottes ausgeht", None, None),
 ("MAT.4.5", "er stellte", "literal", "ἔστησεν", None, ["er stellt"],
  "Matthäus wechselt vom erzählenden Präsens («nimmt … mit») in die Vergangenheit; die Übersetzung behält den Wechsel bei. RP liest auch hier Präsens (siehe die Alternative)."),
 ("MAT.4.5", "die heilige Stadt", "literal", "τὴν ἁγίαν πόλιν", None, ["Jerusalem"],
  "Bezeichnung für Jerusalem (vgl. [[ISA.52.1]], [[MAT.27.53]])."),
 ("MAT.4.5", "Zinne", "interpretive", "πτερύγιον", "Flügelchen", ["höchster Punkt", "Dachrand"],
  "πτερύγιον heisst wörtlich «kleiner Flügel», dann ein vorspringender Teil eines Gebäudes. Welche Stelle der Tempelanlage gemeint ist, ist unbekannt."),
 ("MAT.4.6", "deinetwegen", "literal", "περὶ σοῦ", "über dich", ["für dich"],
  "Zitat aus [[PSA.91.11]]–[[PSA.91.12]] nach der griechischen Bibel; die Worte «dich zu behüten auf allen deinen Wegen» fehlen im Zitat."),
 ("MAT.4.7", "Es steht", "adapted", "Πάλιν γέγραπται", "Wiederum steht geschrieben", None,
  "πάλιν «wiederum» stellt dem Schriftwort des Teufels ein anderes entgegen; wiedergegeben mit «Es steht auch geschrieben»."),
 ("MAT.4.7", "auf die Probe stellen", "literal", "ἐκπειράσεις", None, ["versuchen", "herausfordern"],
  "Zitat aus [[DEU.6.16]]. ἐκπειράζω ist verstärktes πειράζω; gegenüber Gott heisst es, ihn herauszufordern. Das Futur ist als Verbot wiedergegeben («du sollst nicht»), ebenso in [[MAT.4.10]]."),
 ("MAT.4.8", "alle Reiche der Welt", "literal", "πάσας τὰς βασιλείας τοῦ κόσμου", None, ["alle Königreiche der Welt"],
  "Hier meint βασιλεία irdische Herrschaftsbereiche; es ist dasselbe Wort wie im «Reich der Himmel» ([[MAT.4.17]])."),
 ("MAT.4.9", "anbetest", "interpretive", "προσκυνήσῃς", "dich vor mir niederwirfst", ["mir huldigst"],
  "προσκυνέω bezeichnet die Gebärde des Niederwerfens, mit der man einem Herrscher huldigt oder Gott anbetet (bei Matthäus 13-mal). Vorschlag für Matthäus: «anbeten», wo die Verehrung Gottes oder der Anspruch darauf im Blick ist (hier und [[MAT.4.10]]); wo die Gebärde vor einem Menschen im Vordergrund steht, «sich niederwerfen vor», jeweils mit eigener Entscheidung."),
 ("MAT.4.10", "Geh weg, Satan", "literal", "Ὕπαγε, Σατανᾶ", None, ["Weg mit dir, Satan"],
  "ὑπάγω «weggehen». Zur Lesart «Geh hinter mich» (wie [[MAT.16.23]]) siehe die Alternative. Σατανᾶς bleibt als Name stehen."),
 ("MAT.4.10", "dienen", "literal", "λατρεύσεις", None, ["verehren"],
  "λατρεύω meint den Dienst, der Gott zukommt, besonders im Gottesdienst. Im hebräischen Text von [[DEU.6.13]] steht «fürchten» statt «anbeten», und «allein» fehlt; einzelne Handschriften der griechischen Bibel lesen wie Matthäus."),
 ("MAT.4.11", "dienten", "literal", "διηκόνουν", None, ["versorgten ihn"],
  "Imperfekt: Die Engel dienen ihm über eine Zeit hin; ob mit Nahrung nach dem Fasten, sagt der Text nicht."),
 ("MAT.4.12", "ausgeliefert worden war", "literal", "παρεδόθη", None, ["gefangen genommen worden war"],
  "Wie [[MRK.1.14]]: παραδίδωμι «ausliefern» steht bei Matthäus auch für Jesus ([[MAT.17.22]], [[MAT.26.2]]). Die Verhaftung des Johannes erzählt erst [[MAT.14.3]]."),
 ("MAT.4.12", "zog er sich", "literal", "ἀνεχώρησεν", None, ["ging fort"],
  "Vorschlag für Matthäus: ἀναχωρέω (10-mal) einheitlich «sich zurückziehen»; das Wort steht oft, wenn jemand einer Gefahr ausweicht (vgl. [[MAT.2.14]], [[MAT.12.15]], [[MAT.14.13]])."),
 ("MAT.4.13", "liess sich", "literal", "κατῴκησεν", None, ["wohnte"],
  "κατοικέω «wohnen, sich niederlassen»: Kafarnaum wird Jesu Wohnort (vgl. [[MAT.9.1]] «seine eigene Stadt»). Ναζαρά ist eine seltene Form des Ortsnamens (noch [[LUK.4.16]]); übersetzt wie sonst «Nazaret»."),
 ("MAT.4.13", "am See", "adapted", "παραθαλασσίαν", "am Meer gelegen", None,
  "θάλασσα bezeichnet im Erzähltext den See Gennesaret und ist dort «See» übersetzt ([[MAT.4.18]]; wie [[MRK.1.16]]). Im Zitat [[MAT.4.15]] steht «Meer» wie bei Jesaja."),
 ("MAT.4.14", "damit erfüllt würde", "literal", "ἵνα πληρωθῇ", None, ["so sollte erfüllt werden"],
  "Feste Erfüllungsformel des Matthäus (vgl. [[MAT.1.22]], [[MAT.2.15]], [[MAT.2.23]]), im ganzen Evangelium gleich wiedergegeben. ἵνα kann Zweck oder Folge ausdrücken."),
 ("MAT.4.15", "Weg am Meer", "interpretive", "ὁδὸν θαλάσσης", "Weg des Meeres", ["zum Meer hin"],
  "Das Zitat folgt frei [[ISA.9.1]]–[[ISA.9.2]]. Der Akkusativ ὁδόν ist ungewöhnlich; gemeint ist eine Strasse oder Richtung zum Meer, von Matthäus wohl auf den See Gennesaret bezogen."),
 ("MAT.4.15", "Galiläa der Völker", "interpretive", "Γαλιλαία τῶν ἐθνῶν", None, ["Galiläa der Heiden"],
  "Vorschlag für Matthäus: τὰ ἔθνη «die Völker»; wo der Gegensatz zu Israel betont ist, kann «Heiden» näher liegen, dann mit eigener Entscheidung. Galiläa hatte eine gemischte Bevölkerung."),
 ("MAT.4.16", "im Land und Schatten des Todes", "literal", "ἐν χώρᾳ καὶ σκιᾷ θανάτου", None, ["im Schattenland des Todes"],
  "Zwei Begriffe für eine Sache: das Land, über dem der Schatten des Todes liegt."),
 ("MAT.4.17", "Von da an", "literal", "Ἀπὸ τότε", None, None,
  "Die Wendung markiert einen Einschnitt; sie kehrt in [[MAT.16.21]] wieder. Jesu Verkündigung stimmt wörtlich mit der des Johannes überein ([[MAT.3.2]])."),
 ("MAT.4.18", "See", "adapted", "θάλασσαν", "Meer", None,
  "Wie [[MRK.1.16]]: gemeint ist der See Gennesaret."),
 ("MAT.4.18", "der Petrus genannt wird", "literal", "τὸν λεγόμενον Πέτρον", None, None,
  "Matthäus nennt den Beinamen schon hier; eine Erklärung folgt in [[MAT.16.18]]."),
 ("MAT.4.18", "ein Wurfnetz", "literal", "ἀμφίβληστρον", None, None,
  "Ein rundes Netz, das man vom Ufer oder im flachen Wasser auswirft."),
 ("MAT.4.19", "zu Menschenfischern", "literal", "ἁλιεῖς ἀνθρώπων", "zu Fischern von Menschen", None,
  "Wie [[MRK.1.17]]; Wortspiel mit dem Beruf der Angesprochenen."),
 ("MAT.4.23", "das Evangelium vom Reich", "literal", "τὸ εὐαγγέλιον τῆς βασιλείας", "die gute Botschaft des Reiches", ["die gute Nachricht vom Reich"],
  "Die Wendung steht so nur bei Matthäus ([[MAT.9.35]], [[MAT.24.14]]). εὐαγγέλιον «Evangelium» wie bei Markus. [[MAT.4.23]] und [[MAT.9.35]] sind fast gleich formuliert: Jesus lehrt, verkündigt und heilt."),
 ("MAT.4.23", "ihren Synagogen", "literal", "ταῖς συναγωγαῖς αὐτῶν", None, None,
  "«Ihre» meint die Synagogen der Leute Galiläas; Matthäus sagt oft so (vgl. [[MAT.9.35]], [[MAT.10.17]]). Neutral wiedergegeben."),
 ("MAT.4.24", "Kunde", "literal", "ἀκοὴ", "das Gehörte", ["der Ruf"], None),
 ("MAT.4.24", "Kranken", "adapted", "τοὺς κακῶς ἔχοντας", "die, denen es schlecht geht", None,
  "Wie bei Markus «die Kranken»."),
 ("MAT.4.24", "Besessene", "literal", "δαιμονιζομένους", "von Dämonen Besessene", None,
  "Einheitlicher Matthäus-Begriff: δαιμονίζομαι «besessen sein», δαιμόνιον «Dämon» (Mundart «Bsässne», «Dämon»). Die Aufzählung nennt Besessene neben Kranken, ohne sie scharf zu trennen; zur Lesart mit «und» siehe die Alternative."),
 ("MAT.4.24", "Mondsüchtige", "interpretive", "σεληνιαζομένους", "vom Mond Getroffene", ["Epileptiker", "Fallsüchtige"],
  "Das Wort verbindet Anfälle mit dem Mond, wie es antiker Vorstellung entsprach. Die Beschreibung in [[MAT.17.15]] erinnert an Epilepsie; «Epileptiker» würde aber eine heutige Diagnose in den Text tragen."),
 ("MAT.4.25", "Menschenmengen", "literal", "ὄχλοι", None, ["Volksmengen", "Scharen"],
  "Vorschlag für Matthäus: ὄχλος «Menge», im Plural «Menschenmengen» (Mundart «Mängi», im Plural «Schaare vo Lüüt»), wie bei Markus."),
 ("MAT.4.25", "Dekapolis", "literal", "Δεκαπόλεως", "Zehnstadt", None,
  "Ein Bund griechisch geprägter Städte, die meisten östlich des Jordan."),
]

DEC_GSW = [
 ("MAT.3.1", "tritt", "adapted", "παραγίνεται", "chunnt", ["erschiint"],
  "S erzellend Präsens vom Matthäus bliibt; bim erschte Uftrete vom Johannes «uftrete», i [[MAT.3.13]] «chunnt»."),
 ("MAT.3.1", "Wüeschti", "literal", "ἐρήμῳ", None, ["Einöödi"],
  "ἔρημος isch s unbewohnt, karg Land, nöd unbedingt Sandwüeschti."),
 ("MAT.3.2", "Chehred um", "interpretive", "Μετανοεῖτε", "Dänked um", ["Tüend Buess"],
  "Wie [[MRK.1.15]]: μετανοέω isch es Umdänke; mitgmeint isch d Rückkehr zu Gott. «Buess» tönt nach Straf. Im ganze Matthäus «umchehre», «Umkehr». De Johannes ([[MAT.3.2]]) und de Jesus ([[MAT.4.17]]) säged wörtli s Gliich."),
 ("MAT.3.2", "s Riich vo de Himel", "traditional", "ἡ βασιλεία τῶν οὐρανῶν", "d Chönigsherrschaft vo de Himel", ["s Himelriich", "s Riich vo Gott"],
  "Einheitlich im Matthäus: Er seit meischtens «Riich vo de Himel» (32-mal, «Riich vo Gott» nu 4-mal), wahrschiinli nach jüdischem Bruuch, de Gottesname z umschriibe; gmeint isch s Gliich wie «s Riich vo Gott» bim Markus. βασιλεία meint zersch d Herrschaft vo Gott als Gscheh, nöd es Gebiet."),
 ("MAT.3.2", "isch nöch choo", "literal", "ἤγγικεν", None, ["isch da"],
  "Öb s Riich scho aagfange hät oder grad bevorstaat, isch umstritte; «nöch choo» laat beides offe."),
 ("MAT.3.3", "gseit worden isch", "literal", "ῥηθεὶς", None, None,
  "Feschti Formle vom Matthäus für Schriftwort, im ganze Evangelium gliich widergää (vgl. [[MAT.4.14]]); da ohni «demit erfüllt wird»."),
 ("MAT.3.3", "vom Herr", "literal", "κυρίου", None, ["vo JHWH"],
  "I [[ISA.40.3]] staat im hebräische Text de Gottesname, i de griechische Bible κύριος. De Matthäus bezieht de «Wäg vom Herr» uf de Jesus."),
 ("MAT.3.4", "Hung", "literal", "μέλι", None, ["Honig"], None),
 ("MAT.3.7", "Ir Schlangebruet", "adapted", "Γεννήματα ἐχιδνῶν", "Bruet vo Vipere", ["Ir Natterebruet"],
  "S gliich Schimpfwort staat i [[MAT.12.34]] und [[MAT.23.33]]; überall «Schlangebruet». D Gruppenäme Pharisäer und Sadduzäer sind neutral widergää; de scharf Ton liit im Wort vom Johannes."),
 ("MAT.3.7", "druf bracht", "adapted", "ὑπέδειξεν", "zeigt", ["gwarnt"],
  "ὑποδείκνυμι heisst «zeige, aawiise». Vili verstönd d Frag als ironisch."),
 ("MAT.3.8", "passt", "adapted", "ἄξιον", "wärt", ["entspricht"],
  "Wörtli «wo de Umkehr wärt isch»; Frucht isch es Bild fürs Tue. καρπός überall «Frucht»."),
 ("MAT.3.9", "Chind erwecke", "literal", "ἐγεῖραι τέκνα", None, ["Chind la entstaa"],
  "ἐγείρω «ufrichte, erwecke» staat susch oft fürs Uferwecke vo Tote. Hebräisch und aramäisch tönt «Söhn» (banim) ähnlich wie «Stei» (abanim); öb da es Wortspiil drhinder staat, cha mer nöd nachwiise."),
 ("MAT.3.11", "zur Umkehr", "interpretive", "εἰς μετάνοιαν", None, ["wäge de Umkehr"],
  "εἰς cha s Ziil oder de Grund aagää. Anders als [[MRK.1.4]] redt de Matthäus bim Johannes nöd vo «Vergäbig vo de Sünde»."),
 ("MAT.3.11", "mit heilige Geischt und Füür", "interpretive", "ἐν πνεύματι ἁγίῳ καὶ πυρί", None, ["im heilige Geischt und im Füür"],
  "Ohni Artikel, im Gägesatz zu «mit Wasser». «Füür» cha Lüüterig oder Gricht meine ([[MAT.3.10]], [[MAT.3.12]]). πνεῦμα ἅγιον überall «heilige Geischt»."),
 ("MAT.3.12", "Worfschufle", "literal", "πτύον", None, None,
  "Mit de Worfschufle hät mer s tröschet Choorn i de Wind gworfe; d Sprüür isch wäggfloge, d Chörner sind ufs Tenn gfalle. Es Bild fürs Gricht, wo scheidet."),
 ("MAT.3.14", "hät en welle devo abhalte", "interpretive", "διεκώλυεν αὐτὸν", "hät en abghalte", ["hät probiert, en abzhalte"],
  "Imperfekt vom Versuech: De Johannes wott, aber er machts nöd. S Gspröch [[MAT.3.14]]–[[MAT.3.15]] hät nu de Matthäus."),
 ("MAT.3.15", "alli Grächtigkeit z erfülle", "interpretive", "πληρῶσαι πᾶσαν δικαιοσύνην", None, ["alles z tue, was Gott wott"],
  "Grundentscheid fürs Matthäusevangelium: δικαιοσύνη überall «Grächtigkeit» (7-mal). Gmeint isch meischtens s rächt Tue nach em Wille vo Gott. Was es da heisst, wird verschide erklärt (Ghorsam, Verbundeheit mit em Volk, Erfüllig vo de Schrift). «Üs» cha de Jesus und de Johannes meine oder de Jesus ellei."),
 ("MAT.3.15", "laat er en mache", "adapted", "ἀφίησιν αὐτόν", "laat er en", ["laat er s zue"],
  "S gliich Verb wie «Lass es zue» am Aafang vom Vers."),
 ("MAT.3.16", "grad", "literal", "εὐθὺς", None, ["sofort"],
  "Einheitlich im Matthäus: εὐθύς und εὐθέως «grad» (Hochdüütsch «sogleich»)."),
 ("MAT.3.16", "lueg", "literal", "ἰδοὺ", None, None,
  "Einheitlich im Matthäus: ἰδού «lueg» (Hochdüütsch «siehe»)."),
 ("MAT.3.16", "d Himel sind ufgange", "literal", "ἠνεῴχθησαν οἱ οὐρανοί", None, None,
  "Plural wie im Griechische; rüeiger als s «Ufriisse» bim Markus ([[MRK.1.10]]). Zur Läsart «sind ihm ufgange» lueg d Alternative."),
 ("MAT.3.17", "Dä isch min liebe Sohn", "literal", "Οὗτός ἐστιν ὁ υἱός μου ὁ ἀγαπητός", None, ["Das isch min Sohn, wo n ich gärn ha"],
  "Bim Matthäus redt d Stimm über de Jesus («Dä isch»), bim Markus zu ihm («Du bisch»). Aaklang a [[PSA.2.7]] und [[ISA.42.1]]."),
 ("MAT.4.1", "Tüüfel", "literal", "διαβόλου", "Verleumder", None,
  "διάβολος heisst wörtli «Verleumder»; überall «Tüüfel». I [[MAT.4.3]] heisst er «de Versuecher», i [[MAT.4.10]] «Satan»."),
 ("MAT.4.1", "versuecht z wärde", "literal", "πειρασθῆναι", None, ["uf d Prob gstellt z wärde"],
  "πειράζω heisst prüefe, uf d Prob stelle, au zur Sünd verleite. Vorschlag: «versueche», wo de Tüüfel handlet; wo Mänsche de Jesus prüefed, «uf d Prob stelle»."),
 ("MAT.4.3", "isch anecho", "literal", "προσελθὼν", None, ["isch zue n ihm choo"],
  "Vorschlag fürs Matthäusevangelium: προσέρχομαι (51-mal) überall «anechoo»."),
 ("MAT.4.3", "Wänn du de Sohn vo Gott bisch", "interpretive", "Εἰ υἱὸς εἶ τοῦ θεοῦ", None, ["Wänn du würkli de Sohn vo Gott bisch"],
  "D Bedingig knüpft a d Stimm us em Himel aa ([[MAT.3.17]]). Vili verstönd si als Voruussetzig, wo de Versuecher bruuche wott; anderi ghöred en Zwiifel."),
 ("MAT.4.4", "läbt", "adapted", "ζήσεται", "wird läbe", None,
  "S Futur seit da öppis, wo allgemein gilt ([[DEU.8.3]])."),
 ("MAT.4.5", "er hät en uf d Zinne vom Tämpel gstellt", "literal", "ἔστησεν αὐτὸν ἐπὶ τὸ πτερύγιον τοῦ ἱεροῦ", None, None,
  "De Matthäus wächslet vom erzellende Präsens («nimmt … mit») i d Vergangeheit. πτερύγιον heisst wörtli «chline Flügel»; welli Stell vom Tämpel gmeint isch, weiss mer nöd."),
 ("MAT.4.7", "uf d Prob stelle", "literal", "ἐκπειράσεις", None, ["versueche", "usefordere"],
  "Zitat us [[DEU.6.16]]; ἐκπειράζω heisst gägenüber Gott, ihn usefordere. S Futur isch als Verbot widergää («du söllsch nöd»)."),
 ("MAT.4.9", "aabättisch", "interpretive", "προσκυνήσῃς", "di vor mir uf de Bode wirfsch", ["mir huldigsch"],
  "προσκυνέω isch d Gebärde vom Nidergheie vor eme Herrscher oder vor Gott. Vorschlag: «aabätte», wo d Verehrig vo Gott im Blick isch (da und [[MAT.4.10]]); susch «sich vor öpperem uf de Bode wärfe»."),
 ("MAT.4.10", "Gang wäg, Satan", "literal", "Ὕπαγε, Σατανᾶ", None, ["Verschwind, Satan"],
  "Zur Läsart «Gang hinder mich» (wie [[MAT.16.23]]) lueg d Alternative."),
 ("MAT.4.11", "laat de Tüüfel vo ihm ab", "adapted", "ἀφίησιν αὐτὸν ὁ διάβολος", "verlaat en de Tüüfel", None, None),
 ("MAT.4.12", "hät er sich", "literal", "ἀνεχώρησεν", None, ["isch er furtgange"],
  "Vorschlag: ἀναχωρέω überall «sich zruggzie»; s Wort staat oft, wänn öpper ere Gfaar uswiicht (vgl. [[MAT.2.14]], [[MAT.12.15]])."),
 ("MAT.4.13", "am See", "adapted", "παραθαλασσίαν", "am Meer", None,
  "θάλασσα isch im Erzelltext de See Gennesaret («See»); im Zitat [[MAT.4.15]] staat «Meer» wie bim Jesaja."),
 ("MAT.4.14", "demit erfüllt wird", "literal", "ἵνα πληρωθῇ", None, None,
  "Feschti Erfüllungsformle vom Matthäus, im ganze Evangelium gliich widergää."),
 ("MAT.4.15", "Galiläa vo de Völker", "interpretive", "Γαλιλαία τῶν ἐθνῶν", None, ["Galiläa vo de Heide"],
  "Vorschlag: τὰ ἔθνη «d Völker»; wo de Gägesatz zu Israel im Vordergrund staat, cha «Heide» nöcher ligge. S Zitat folgt frei [[ISA.9.1]]–[[ISA.9.2]]."),
 ("MAT.4.16", "im Land und Schatte vom Tod", "literal", "ἐν χώρᾳ καὶ σκιᾷ θανάτου", None, None,
  "Zwei Wort für ei Sach: s Land, wo de Schatte vom Tod druf liit."),
 ("MAT.4.18", "wo mer Petrus seit", "adapted", "τὸν λεγόμενον Πέτρον", "wo Petrus gnännt wird", None, None),
 ("MAT.4.19", "zu Mänschefischer", "literal", "ἁλιεῖς ἀνθρώπων", None, None,
  "Wie [[MRK.1.17]]; es Wortspiil mit em Bruef vo de Aagredte."),
 ("MAT.4.23", "s Evangelium vom Riich", "literal", "τὸ εὐαγγέλιον τῆς βασιλείας", None, ["di gueti Nachricht vom Riich"],
  "D Wändig staat eso nu bim Matthäus ([[MAT.9.35]], [[MAT.24.14]])."),
 ("MAT.4.24", "Bsässni", "literal", "δαιμονιζομένους", None, None,
  "Einheitlich im Matthäus: δαιμονίζομαι «bsässe sii» (Eizahl «en Bsässne», Mehrzahl «Bsässni»), δαιμόνιον «Dämon»."),
 ("MAT.4.24", "Mondsüchtigi", "interpretive", "σεληνιαζομένους", None, ["Epileptiker"],
  "S Wort verbindet Aafäll mit em Mond, wie mer s i de Antike gmeint hät; «Epileptiker» wär e hüttigi Diagnose."),
 ("MAT.4.25", "Schaare vo Lüüt", "adapted", "ὄχλοι", "Mängene", ["Mängine"],
  "ὄχλος isch wie bim Markus «Mängi»; d Mehrzahl isch mit «Schaare vo Lüüt» widergää."),
]

# (Lesart, Stelle, von de, zu de, von gsw, zu gsw, Wirkung, Hinweis de, Hinweis gsw, Wortlaute de, Wortlaute gsw,
#  Entstehung de, Entstehung gsw). Handschriftenangaben nur aus data/witness-readings (maschinelle Zuordnung) und
#  dem dort erfassten Wortlaut.
ALTS = [
 ("VAR-SBLGNTAPP-MAT-003-002-01:R2", "MAT.3.2", "und sagt", "sagt", "und seit", "seit", "gering",
  "Ohne καί hängt «sagend» unmittelbar an «verkündigt» an; der Sinn bleibt gleich.",
  "Ohni καί hanget «sägend» diräkt am «verchündet»; de Sinn bliibt gliich.",
  {"R1": [("καὶ λέγων", "und sagt", "Treg, NA28, RP")], "R2": [("λέγων", "sagt", "WH")]},
  {"R1": [("καὶ λέγων", "und seit", "Treg, NA28, RP")], "R2": [("λέγων", "seit", "WH")]},
  ["Das καί kann ergänzt worden sein, um die beiden Partizipien zu verbinden; ebenso kann es als entbehrlich weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 04, 05 und 032 mit καί, 01 und 03 ohne."],
  ["S καί cha ergänzt worde sii, zum di zwei Partizip verbinde; oder es isch als überflüssig wäggfalle.",
   "Nach de automatische Zueornig läsed 04, 05 und 032 mit καί, 01 und 03 ohni."]),
 ("VAR-SBLGNTAPP-MAT-003-003-01:R2", "MAT.3.3", "durch Jesaja", "von Jesaja", "dur de Jesaja", "vom Jesaja", "gering",
  "Mit ὑπό («von») ist Jesaja selbst der Sprecher; mit διά («durch») spricht Gott durch den Propheten, wie in den Erfüllungsformeln (z. B. [[MAT.1.22]]).",
  "Mit ὑπό («vo») isch de Jesaja sälber de Sprächer; mit διά («dur») redt Gott dur de Prophet, wie i de Erfüllungsformle.",
  {"R1": [("διὰ", "durch", "WH, Treg, NA28")], "R2": [("ὑπὸ", "von", "RP")]},
  {"R1": [("διὰ", "dur", "WH, Treg, NA28")], "R2": [("ὑπὸ", "vo", "RP")]},
  ["ὑπό kann aus dem Gebrauch beim Passiv («gesagt von») stammen; διά kann an die übrigen Erfüllungsformeln des Matthäus angeglichen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04, 05 und 032 διά."],
  ["ὑπό cha vom Bruuch bim Passiv («gseit vo») cho; διά cha a di andere Erfüllungsformle vom Matthäus aaglicht sii.",
   "Nach de automatische Zueornig läsed 01, 03, 04, 05 und 032 διά."]),
 ("VAR-SBLGNTAPP-MAT-003-006-01:R2", "MAT.3.6", "im Fluss Jordan", "im Jordan", "im Fluss Jordan", "im Jordan", "gering",
  "Das Wort «Fluss» fehlt; der Sinn bleibt gleich.", "S Wort «Fluss» fehlt; de Sinn bliibt gliich.",
  {"R1": [("ποταμῷ", "Fluss", "WH, Treg, NA28")], "R2": [("–", "ohne «Fluss»", "RP")]},
  {"R1": [("ποταμῷ", "Fluss", "WH, Treg, NA28")], "R2": [("–", "ohni «Fluss»", "RP")]},
  ["ποταμῷ kann aus [[MRK.1.5]] ergänzt sein; ebenso kann es als selbstverständlich weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 03 und 04 mit ποταμῷ, 05 und 032 ohne. Bei 01 ist die Erstschrift nicht eindeutig zugeordnet: Nach dem erfassten Wortlaut steht ποταμῷ dort, es fehlt aber ὑπʼ αὐτοῦ («von ihm»); die Korrektur liest wie der SBLGNT."],
  ["ποταμῷ cha us [[MRK.1.5]] ergänzt sii; oder es isch als sälbverständlich wäggfalle.",
   "Nach de automatische Zueornig läsed 03 und 04 mit ποταμῷ, 05 und 032 ohni. Bi 01 isch d Erschtschrift nöd eidüütig zueornet: Nach em erfasste Wortlut staat ποταμῷ, aber ὑπʼ αὐτοῦ («vo ihm») fehlt; d Korrektur list wie de SBLGNT."]),
 ("VAR-SBLGNTAPP-MAT-003-007-01:R2", "MAT.3.7", "zu seiner Taufe", "zur Taufe", "zu sinere Taufi", "zur Taufi", "gering",
  "Ohne «seiner» ist die Taufe nur allgemein genannt; der Sinn bleibt nahezu gleich.",
  "Ohni «sinere» isch d Taufi nu allgemein gnännt; de Sinn bliibt fascht gliich.",
  {"R1": [("αὐτοῦ", "seiner", "Treg, NA28, RP")], "R2": [("–", "ohne «seiner»", "WH")]},
  {"R1": [("αὐτοῦ", "sinere", "Treg, NA28, RP")], "R2": [("–", "ohni «sinere»", "WH")]},
  ["αὐτοῦ kann zur Verdeutlichung ergänzt oder als entbehrlich weggelassen worden sein.",
   "Laut der automatischen Zuordnung lesen 04, 05 und 032 mit αὐτοῦ, 01 und 03 ohne; bei 01 ergänzt eine Korrektur das Wort."],
  ["αὐτοῦ cha zur Verdüütlichung ergänzt oder als überflüssig wägglaa worde sii.",
   "Nach de automatische Zueornig läsed 04, 05 und 032 mit αὐτοῦ, 01 und 03 ohni; bi 01 ergänzt e Korrektur s Wort."]),
 ("VAR-SBLGNTAPP-MAT-003-010-01:R2", "MAT.3.10", "Die Axt liegt aber schon", "Die Axt liegt aber auch schon",
  "D Axt liit aber scho", "D Axt liit aber au scho", "gering",
  "Mit καί («auch») wird die Drohung noch unterstrichen.", "Mit καί («au») wird d Drohig no unterstriche.",
  {"R1": [("δὲ", "aber", "WH, Treg, NA28")], "R2": [("δὲ καὶ", "aber auch", "RP")]},
  {"R1": [("δὲ", "aber", "WH, Treg, NA28")], "R2": [("δὲ καὶ", "aber au", "RP")]},
  ["καί kann aus der Parallele [[LUK.3.9]] eingedrungen sein; ebenso kann es weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 032 ohne καί; 05 ist an dieser Stelle nicht erhalten."],
  ["καί cha us de Parallele [[LUK.3.9]] cho sii; oder es isch wäggfalle.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 032 ohni καί; 05 isch a dere Stell nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-003-011-02:R2", "MAT.3.11", "mit heiligem Geist und Feuer", "mit heiligem Geist",
  "mit heilige Geischt und Füür", "mit heilige Geischt", "mittel",
  "Ohne «und Feuer» fehlt der Hinweis auf Läuterung oder Gericht; der Satz entspricht dann [[MRK.1.8]].",
  "Ohni «und Füür» fehlt de Hiiwiis uf Lüüterig oder Gricht; de Satz entspricht dänn [[MRK.1.8]].",
  {"R1": [("καὶ πυρί", "und Feuer", "WH, Treg, NA28")], "R2": [("–", "ohne «und Feuer»", "RP")]},
  {"R1": [("καὶ πυρί", "und Füür", "WH, Treg, NA28")], "R2": [("–", "ohni «und Füür»", "RP")]},
  ["Die Worte können durch Angleichung an [[MRK.1.8]] weggefallen sein; umgekehrt kann eine Angleichung an [[LUK.3.16]], wo sie ebenfalls stehen, sie ergänzt haben.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 032 mit καὶ πυρί; 05 ist nicht erhalten. Sie führt ED-RP bei der Lesart ohne die Worte (wie der Apparat), KJTR und Stephanus mit ihnen."],
  ["D Wort chönd dur Aagliichig a [[MRK.1.8]] wäggfalle sii; umgekehrt cha e Aagliichig a [[LUK.3.16]], wo s au staat, si ergänzt ha.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 032 mit καὶ πυρί; 05 isch nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-003-012-01:R2", "MAT.3.12", "in die Scheune", "in seine Scheune", "i d Schüür", "i sini Schüür", "gering",
  "Mit αὐτοῦ ist es «seine» Scheune, wie zuvor seine Tenne und sein Weizen.",
  "Mit αὐτοῦ isch es «sini» Schüür, wie vorher sis Tenn und sin Weize.",
  {"R1": [("ἀποθήκην", "Scheune", "WH, NA28, RP")], "R2": [("ἀποθήκην αὐτοῦ", "seine Scheune", "Treg")]},
  {"R1": [("ἀποθήκην", "Schüür", "WH, NA28, RP")], "R2": [("ἀποθήκην αὐτοῦ", "sini Schüür", "Treg")]},
  ["αὐτοῦ kann nach den vorangehenden «seine Tenne», «seinen Weizen» ergänzt oder als überflüssig weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 01 und 04 ohne, 03 und 032 mit αὐτοῦ; 05 ist nicht erhalten."],
  ["αὐτοῦ cha nach «sis Tenn», «sin Weize» ergänzt oder als überflüssig wäggfalle sii.",
   "Nach de automatische Zueornig läsed 01 und 04 ohni, 03 und 032 mit αὐτοῦ; 05 isch nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-003-014-01:R2", "MAT.3.14", "Johannes aber wollte", "Er aber wollte", "De Johannes aber hät", "Er aber hät", "gering",
  "Ohne den Namen ist Johannes nur durch «er» bezeichnet; der Sinn bleibt gleich.",
  "Ohni de Name isch de Johannes nu mit «er» gmeint; de Sinn bliibt gliich.",
  {"R1": [("ὁ δὲ Ἰωάννης", "Johannes aber", "Treg, NA28, RP")], "R2": [("ὁ δὲ", "er aber", "WH")]},
  {"R1": [("ὁ δὲ Ἰωάννης", "de Johannes aber", "Treg, NA28, RP")], "R2": [("ὁ δὲ", "er aber", "WH")]},
  ["Der Name kann zur Verdeutlichung ergänzt worden sein, etwa am Beginn eines Leseabschnitts; ebenso kann er als entbehrlich weggefallen sein.",
   "Laut der automatischen Zuordnung lesen 04 und 032 mit dem Namen, 01 und 03 ohne; bei 01 ergänzt eine Korrektur den Namen. 05 ist nicht erhalten."],
  ["De Name cha zur Verdüütlichung ergänzt worde sii, öppe am Aafang vo me Läseabschnitt; oder er isch wäggfalle.",
   "Nach de automatische Zueornig läsed 04 und 032 mit em Name, 01 und 03 ohni; bi 01 ergänzt e Korrektur de Name. 05 isch nöd erhalte."]),
 ("VAR-SBLGNTAPP-MAT-003-016-03:R2", "MAT.3.16", "die Himmel öffneten sich", "die Himmel öffneten sich ihm",
  "d Himel sind ufgange", "d Himel sind ihm ufgange", "gering",
  "Mit «ihm» öffnen sich die Himmel ausdrücklich für Jesus. Hier folgt der SBLGNT WH gegen Treg, NA28 und RP.",
  "Mit «ihm» gönd d Himel usdrücklich für de Jesus uf. Da folgt de SBLGNT de WH gäge Treg, NA28 und RP.",
  {"R1": [("ἠνεῴχθησαν", "öffneten sich", "WH, NIV")], "R2": [("ἠνεῴχθησαν αὐτῷ", "öffneten sich ihm", "Treg, RP, NA28")]},
  {"R1": [("ἠνεῴχθησαν", "sind ufgange", "WH, NIV")], "R2": [("ἠνεῴχθησαν αὐτῷ", "sind ihm ufgange", "Treg, RP, NA28")]},
  ["αὐτῷ kann ergänzt sein, um zu sagen, wem sich die Himmel öffnen; ebenso kann es weggefallen sein, etwa unter dem Einfluss von [[LUK.3.21]].",
   "Laut der automatischen Zuordnung liest 03 ohne αὐτῷ, 04 und 032 mit; die Erstschrift von 01 ohne, eine Korrektur mit. Für 05 liefert die Zuordnung keinen verwertbaren Befund."],
  ["αὐτῷ cha ergänzt sii, zum säge, für wär sich d Himel uftüend; oder es isch wäggfalle, öppe under em Iifluss vo [[LUK.3.21]].",
   "Nach de automatische Zueornig list 03 ohni αὐτῷ, 04 und 032 mit; d Erschtschrift vo 01 ohni, e Korrektur mit. Für 05 git d Zueornig kein bruuchbare Befund."]),
 ("VAR-SBLGNTAPP-MAT-004-005-01:R2", "MAT.4.5", "er stellte ihn", "er stellt ihn",
  "er hät en uf d Zinne vom Tämpel gstellt", "er stellt en uf d Zinne vom Tämpel", "gering",
  "Mit dem Präsens läuft das erzählende Präsens («nimmt … mit») weiter.",
  "Mit em Präsens lauft s erzellend Präsens («nimmt … mit») wiiter.",
  {"R1": [("ἔστησεν", "stellte", "WH, Treg, NA28")], "R2": [("ἵστησιν", "stellt", "RP")]},
  {"R1": [("ἔστησεν", "hät gstellt", "WH, Treg, NA28")], "R2": [("ἵστησιν", "stellt", "RP")]},
  ["Das Präsens kann an das vorangehende παραλαμβάνει («nimmt») angeglichen sein; umgekehrt kann der Aorist eine Glättung sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 ἔστησεν, 032 ἵστησιν."],
  ["S Präsens cha as vorig παραλαμβάνει («nimmt») aaglicht sii; umgekehrt cha de Aorist e Glättig sii.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 ἔστησεν, 032 ἵστησιν."]),
 ("VAR-SBLGNTAPP-MAT-004-009-01:R2", "MAT.4.9", "und sagte zu ihm", "und sagt zu ihm", "und hät zu ihm gseit", "und seit zu ihm", "gering",
  "Präsens statt Vergangenheit; der Sinn bleibt gleich.", "Präsens statt Vergangeheit; de Sinn bliibt gliich.",
  {"R1": [("εἶπεν", "sagte", "WH, Treg, NA28")], "R2": [("λέγει", "sagt", "RP")]},
  {"R1": [("εἶπεν", "hät gseit", "WH, Treg, NA28")], "R2": [("λέγει", "seit", "RP")]},
  ["λέγει kann an die Präsensformen von [[MAT.4.8]] angeglichen sein; ebenso kann εἶπεν eine Glättung sein.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 05 εἶπεν, 032 λέγει."],
  ["λέγει cha a d Präsensforme vo [[MAT.4.8]] aaglicht sii; oder εἶπεν isch e Glättig.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 05 εἶπεν, 032 λέγει."]),
 ("VAR-SBLGNTAPP-MAT-004-010-01:R2", "MAT.4.10", "Geh weg, Satan", "Geh hinter mich, Satan", "Gang wäg, Satan", "Gang hinder mich, Satan", "gering",
  "Mit ὀπίσω μου («hinter mich») lautet das Wort wie die Zurechtweisung des Petrus in [[MAT.16.23]].",
  "Mit ὀπίσω μου («hinder mich») tönt s Wort wie d Zrächtwiisig vom Petrus i [[MAT.16.23]].",
  {"R1": [("Ὕπαγε", "Geh weg", "WH, Treg, NA28")], "R2": [("Ὕπαγε ὀπίσω μου", "Geh hinter mich", "NIV, RP")]},
  {"R1": [("Ὕπαγε", "Gang wäg", "WH, Treg, NA28")], "R2": [("Ὕπαγε ὀπίσω μου", "Gang hinder mich", "NIV, RP")]},
  ["Die Worte können aus [[MAT.16.23]] bzw. [[MRK.8.33]] eingedrungen sein; ebenso kann man sie weggelassen haben, weil sie dem Satan gegenüber unpassend schienen.",
   "Laut der automatischen Zuordnung lesen 01, 03, 04 und 032 ohne, 05 mit ὀπίσω μου. Sie führt ED-RP mit den Worten (wie der Apparat), KJTR und Stephanus ohne."],
  ["D Wort chönd us [[MAT.16.23]] oder [[MRK.8.33]] cho sii; oder mer hät si wägglaa, wil s gägenüber em Satan unpassend gschine händ.",
   "Nach de automatische Zueornig läsed 01, 03, 04 und 032 ohni, 05 mit ὀπίσω μου."]),
 ("VAR-SBLGNTAPP-MAT-004-012-01:R2", "MAT.4.12", "Als er aber hörte", "Als Jesus aber hörte", "Wo er aber ghört hät", "Wo de Jesus aber ghört hät", "gering",
  "Der Name verdeutlicht, wer handelt; der Sinn bleibt gleich.", "De Name macht klar, wer handlet; de Sinn bliibt gliich.",
  {"R1": [("δὲ", "aber", "WH, Treg, NA28")], "R2": [("δὲ ὁ Ἰησοῦς", "aber Jesus", "RP")]},
  {"R1": [("δὲ", "aber", "WH, Treg, NA28")], "R2": [("δὲ ὁ Ἰησοῦς", "aber de Jesus", "RP")]},
  ["Der Name kann zu Beginn eines neuen Abschnitts (und Leseabschnitts) ergänzt worden sein; ebenso kann er weggefallen sein.",
   "Laut der automatischen Zuordnung lesen alle erfassten Handschriften (01, 03, 04, 05, 032) ohne den Namen. Nach dem erfassten Wortlaut hat 032 aber ὁ Ἰησοῦς; die Zuordnung ist hier also unsicher."],
  ["De Name cha am Aafang vo me neue Abschnitt ergänzt worde sii; oder er isch wäggfalle.",
   "Nach de automatische Zueornig läsed all erfasste Handschrifte (01, 03, 04, 05, 032) ohni de Name. Nach em erfasste Wortlut hät 032 aber ὁ Ἰησοῦς; d Zueornig isch da also unsicher."]),
 ("VAR-SBLGNTAPP-MAT-004-023-01:R2", "MAT.4.23", "Und er zog", "Und Jesus zog", "Und er isch", "Und de Jesus isch", "gering",
  "Der Name verdeutlicht, wer handelt. Die Lesart von RP (ὅλην τὴν Γαλιλαίαν ὁ Ἰησοῦς, «Jesus zog durch ganz Galiläa») ergibt im Deutschen denselben Wortlaut.",
  "De Name macht klar, wer handlet. D Läsart vo RP git im Düütsche de gliich Wortlut.",
  {"R1": [("ἐν ὅλῃ τῇ Γαλιλαίᾳ", "in ganz Galiläa", "WH, NA28")], "R2": [("ὁ Ἰησοῦς ἐν ὅλῃ τῇ Γαλιλαίᾳ", "Jesus … in ganz Galiläa", "Treg")],
   "R3": [("ὅλην τὴν Γαλιλαίαν ὁ Ἰησοῦς", "Jesus … durch ganz Galiläa", "RP")]},
  {"R1": [("ἐν ὅλῃ τῇ Γαλιλαίᾳ", "in ganz Galiläa", "WH, NA28")], "R2": [("ὁ Ἰησοῦς ἐν ὅλῃ τῇ Γαλιλαίᾳ", "de Jesus … in ganz Galiläa", "Treg")],
   "R3": [("ὅλην τὴν Γαλιλαίαν ὁ Ἰησοῦς", "de Jesus … dur ganz Galiläa", "RP")]},
  ["Der Name kann am Beginn des Summariums zur Verdeutlichung ergänzt worden sein, an wechselnden Stellen im Satz; das spricht für viele für eine spätere Ergänzung. Ebenso kann er weggefallen sein.",
   "Laut der automatischen Zuordnung liest 03 wie der SBLGNT, 04 und 05 wie Treg (R2), 032 wie RP (R3). 01 ist beim SBLGNT-Text geführt, hat nach dem erfassten Wortlaut aber ὁ Ἰησοῦς ohne ὅλῃ; die Korrektur von 01 und 05 haben ὅλην τὴν Γαλιλαίαν. Die Zuordnung ist hier unsicher."],
  ["De Name cha am Aafang vom Summarium zur Verdüütlichung ergänzt worde sii, a wächselnde Stelle im Satz; das spricht für vili für e spööteri Ergänzig. Oder er isch wäggfalle.",
   "Nach de automatische Zueornig list 03 wie de SBLGNT, 04 und 05 wie Treg, 032 wie RP. 01 isch bim SBLGNT-Text gfüert, hät nach em erfasste Wortlut aber ὁ Ἰησοῦς ohni ὅλῃ. D Zueornig isch da unsicher."]),
 ("VAR-SBLGNTAPP-MAT-004-024-01:R2", "MAT.4.24", "geplagt waren: Besessene", "geplagt waren, und Besessene",
  "plaget gsii sind: Bsässni", "plaget gsii sind, und Bsässni", "gering",
  "Mit καί sind Besessene, Mondsüchtige und Gelähmte eine weitere Gruppe neben den Kranken; ohne καί zählen sie die Kranken auf. Hier folgt der SBLGNT WH und Treg gegen NA28 und RP.",
  "Mit καί sind Bsässni, Mondsüchtigi und Glähmti e wiiteri Gruppe näbe de Chranke; ohni καί zelled si d Chranke uf.",
  {"R1": [("συνεχομένους", "geplagt waren:", "WH, Treg")], "R2": [("συνεχομένους καὶ", "geplagt waren, und", "NA28, RP")]},
  {"R1": [("συνεχομένους", "plaget gsii sind:", "WH, Treg")], "R2": [("συνεχομένους καὶ", "plaget gsii sind, und", "NA28, RP")]},
  ["καί kann ergänzt sein, um die Aufzählung zu glätten; ebenso kann es weggefallen sein, etwa beim Abschreiben der langen Reihe.",
   "Laut der automatischen Zuordnung lesen 03 und 04 ohne, 01, 05 und 032 mit καί."],
  ["καί cha ergänzt sii, zum d Ufzellig glätte; oder es isch bim Abschriibe vo de lange Reie wäggfalle.",
   "Nach de automatische Zueornig läsed 03 und 04 ohni, 01, 05 und 032 mit καί."]),
]

SEG = "Gliederungsvorschlag; die Abgrenzung der Abschnitte ist eine redaktionelle Entscheidung."
UNITS = [
 # (id, Bereich, Art, Titel, Teile, Zusammenfassung, Gliederungshinweis)
 ("TU-MAT-003-001-017", "MAT.3.1-MAT.3.17", "section", "Johannes der Täufer und die Taufe Jesu",
  ["TU-MAT-003-001-012", "TU-MAT-003-013-017"],
  "Johannes der Täufer tritt in der Wüste Judäas auf und verkündigt: «Kehrt um, denn das Reich der Himmel ist nahe gekommen!»; der Erzähler bezieht das Wort aus [[ISA.40.3]] auf ihn. Die Leute aus Jerusalem, ganz Judäa und der Umgebung des Jordan lassen sich von ihm taufen und bekennen ihre Sünden. Die Pharisäer und Sadduzäer, die zu seiner Taufe kommen, nennt er Schlangenbrut, fordert Frucht, die der Umkehr würdig ist, und sagt, die Axt liege schon an der Wurzel der Bäume; er kündigt einen Stärkeren an, der mit heiligem Geist und Feuer taufen wird. Jesus kommt aus Galiläa, um sich taufen zu lassen. Johannes will ihn hindern, lässt ihn aber gewähren, als Jesus sagt, so gehöre es sich, alle Gerechtigkeit zu erfüllen. Nach der Taufe öffnen sich die Himmel, Jesus sieht den Geist Gottes wie eine Taube auf sich kommen, und eine Stimme sagt: «Dieser ist mein geliebter Sohn.»",
  SEG),
 ("TU-MAT-003-001-012", "MAT.3.1-MAT.3.12", "narrative_with_saying", "Johannes der Täufer", None,
  "In jenen Tagen tritt Johannes der Täufer in der Wüste Judäas auf und verkündigt: «Kehrt um, denn das Reich der Himmel ist nahe gekommen!» Der Erzähler sagt, von ihm spreche Jesaja: die Stimme eines Rufenden in der Wüste ([[ISA.40.3]]). Johannes trägt ein Gewand aus Kamelhaar und einen ledernen Gurt und isst Heuschrecken und wilden Honig. Jerusalem, ganz Judäa und die Umgebung des Jordan ziehen zu ihm hinaus; die Leute lassen sich im Jordan von ihm taufen und bekennen ihre Sünden. Als er viele Pharisäer und Sadduzäer zu seiner Taufe kommen sieht, nennt er sie Schlangenbrut und fordert Frucht, die der Umkehr würdig ist. Sie sollen sich nicht darauf berufen, Abraham zum Vater zu haben, denn Gott könne aus Steinen Abraham Kinder erwecken; schon liege die Axt an der Wurzel der Bäume. Er tauft mit Wasser zur Umkehr; der nach ihm kommt, ist stärker als er, wird mit heiligem Geist und Feuer taufen, seinen Weizen in die Scheune sammeln und die Spreu mit unauslöschlichem Feuer verbrennen.",
  None),
 ("TU-MAT-003-013-017", "MAT.3.13-MAT.3.17", "narrative", "Die Taufe Jesu", None,
  "Jesus kommt aus Galiläa an den Jordan zu Johannes, um sich von ihm taufen zu lassen. Johannes will ihn daran hindern, denn er habe es nötig, von Jesus getauft zu werden. Jesus antwortet: «Lass es jetzt zu! Denn so gehört es sich für uns, alle Gerechtigkeit zu erfüllen.» Da lässt Johannes ihn gewähren. Als Jesus nach der Taufe aus dem Wasser heraufsteigt, öffnen sich die Himmel; er sieht den Geist Gottes wie eine Taube herabkommen und auf sich kommen, und eine Stimme aus den Himmeln sagt: «Dieser ist mein geliebter Sohn, an dem ich Gefallen gefunden habe.»",
  None),
 ("TU-MAT-004-001-025", "MAT.4.1-MAT.4.25", "section", "Versuchung und Beginn in Galiläa",
  ["TU-MAT-004-001-011", "TU-MAT-004-012-017", "TU-MAT-004-018-022", "TU-MAT-004-023-025"],
  "Der Geist führt Jesus in die Wüste, wo er nach vierzig Tagen Fasten vom Teufel versucht wird; dreimal antwortet Jesus mit einem Schriftwort, bis der Teufel ihn verlässt und Engel ihm dienen. Als Jesus hört, dass Johannes ausgeliefert worden ist, zieht er sich nach Galiläa zurück und lässt sich in Kafarnaum nieder; nach dem Erzähler erfüllt sich damit das Wort Jesajas vom Licht für Galiläa der Völker. Von da an verkündigt Jesus: «Kehrt um, denn das Reich der Himmel ist nahe gekommen!» Am See von Galiläa ruft er die Brüder Simon Petrus und Andreas, dann Jakobus, den Sohn des Zebedäus, und seinen Bruder Johannes; die einen lassen sogleich ihre Netze liegen, die anderen das Boot und ihren Vater, und sie folgen ihm. Jesus zieht durch ganz Galiläa, lehrt in den Synagogen, verkündigt das Evangelium vom Reich und heilt Kranke aller Art; die Kunde von ihm verbreitet sich in ganz Syrien, und viele Menschenmengen folgen ihm.",
  SEG),
 ("TU-MAT-004-001-011", "MAT.4.1-MAT.4.11", "dialogue", "Die Versuchung Jesu", None,
  "Der Geist führt Jesus in die Wüste hinauf, damit er vom Teufel versucht werde. Nach vierzig Tagen und Nächten Fasten hat er Hunger. Der Versucher sagt, wenn er Gottes Sohn sei, solle er sagen, dass die Steine zu Broten werden; Jesus antwortet mit [[DEU.8.3]]: Der Mensch lebt nicht vom Brot allein, sondern von jedem Wort aus dem Mund Gottes. Der Teufel stellt ihn auf die Zinne des Tempels in der heiligen Stadt und fordert ihn mit [[PSA.91.11]]–[[PSA.91.12]] auf, sich hinabzuwerfen; Jesus antwortet mit [[DEU.6.16]]: «Du sollst den Herrn, deinen Gott, nicht auf die Probe stellen.» Auf einem sehr hohen Berg zeigt ihm der Teufel alle Reiche der Welt und verspricht sie ihm, wenn er niederfalle und ihn anbete. Jesus sagt: «Geh weg, Satan!» und antwortet mit [[DEU.6.13]]: Den Herrn, deinen Gott, sollst du anbeten und ihm allein dienen. Da verlässt ihn der Teufel, und Engel treten heran und dienen ihm.",
  None),
 ("TU-MAT-004-012-017", "MAT.4.12-MAT.4.17", "narrative", "Jesus zieht nach Galiläa", None,
  "Als Jesus hört, dass Johannes ausgeliefert worden ist, zieht er sich nach Galiläa zurück. Er verlässt Nazaret und lässt sich in Kafarnaum am See nieder, im Gebiet von Sebulon und Naftali. Nach dem Erzähler geschieht das, damit sich erfüllt, was durch Jesaja gesagt ist ([[ISA.9.1]]–[[ISA.9.2]]): Das Volk, das in Finsternis sass, hat ein grosses Licht gesehen. Von da an beginnt Jesus zu verkündigen: «Kehrt um, denn das Reich der Himmel ist nahe gekommen!»",
  None),
 ("TU-MAT-004-018-022", "MAT.4.18-MAT.4.22", "narrative", "Die ersten Jünger", None,
  "Am See von Galiläa sieht Jesus die Brüder Simon, genannt Petrus, und Andreas, Fischer, die ein Wurfnetz auswerfen. Er sagt zu ihnen: «Kommt mir nach, und ich werde euch zu Menschenfischern machen!» Sogleich lassen sie die Netze liegen und folgen ihm. Weiter sieht er Jakobus, den Sohn des Zebedäus, und seinen Bruder Johannes, die mit ihrem Vater im Boot ihre Netze herrichten, und ruft sie; sogleich lassen sie das Boot und ihren Vater zurück und folgen ihm.",
  None),
 ("TU-MAT-004-023-025", "MAT.4.23-MAT.4.25", "narrative", "Jesus lehrt, verkündigt und heilt", None,
  "Jesus zieht durch ganz Galiläa, lehrt in ihren Synagogen, verkündigt das Evangelium vom Reich und heilt jede Krankheit und jedes Leiden im Volk. Die Kunde von ihm verbreitet sich in ganz Syrien; man bringt ihm alle Kranken, die von mancherlei Krankheiten und Qualen geplagt sind: Besessene, Mondsüchtige und Gelähmte; und er heilt sie. Viele Menschenmengen aus Galiläa, der Dekapolis, Jerusalem, Judäa und von jenseits des Jordan folgen ihm.",
  "Kurzer zusammenfassender Bericht (Summarium); er leitet zur Bergpredigt über ([[MAT.5.1]]) und ist deshalb als eigener Abschnitt gefasst."),
]
UNITS_GSW = {
 "TU-MAT-003-001-017": ("De Johannes de Täufer und d Taufi vom Jesus",
  "De Johannes de Täufer tritt i de Wüeschti vo Judäa uf und verchündet: «Chehred um, dänn s Riich vo de Himel isch nöch choo!»; de Erzeller bezieht s Wort us [[ISA.40.3]] uf ihn. D Lüüt us Jerusalem, ganz Judäa und de Gäged um de Jordan lönd sich vo ihm taufe und bekännd iri Sünde. De Pharisäer und Sadduzäer, wo zu sinere Taufi chömed, seit er Schlangebruet, verlangt Frucht, wo zur Umkehr passt, und seit, d Axt liggi scho a de Wurzle vo de Bäum; er chündet en Stärchere aa, wo mit heilige Geischt und Füür wird taufe. De Jesus chunnt vo Galiläa, zum sich la taufe. De Johannes wott en abhalte, laat en aber mache, wo de Jesus seit, eso ghöri es sich, alli Grächtigkeit z erfülle. Nach de Taufi gönd d Himel uf, de Jesus gseht de Geischt vo Gott wie e Tuube uf sich choo, und e Stimm seit: «Dä isch min liebe Sohn.»"),
 "TU-MAT-003-001-012": ("De Johannes de Täufer",
  "I dene Täg tritt de Johannes de Täufer i de Wüeschti vo Judäa uf und verchündet: «Chehred um, dänn s Riich vo de Himel isch nöch choo!» De Erzeller seit, vo ihm redi de Jesaja: d Stimm vo eim, wo i de Wüeschti rüeft ([[ISA.40.3]]). De Johannes hät es Gwand us Kamelhaar und en lädrige Gurt aa und isst Heuschrecke und wilde Hung. Jerusalem, ganz Judäa und d Gäged um de Jordan gönd zu ihm use; d Lüüt lönd sich im Jordan vo ihm taufe und bekännd iri Sünde. Wo er vili Pharisäer und Sadduzäer zu sinere Taufi gseht choo, seit er ine Schlangebruet und verlangt Frucht, wo zur Umkehr passt. Si söled sich nöd druf berüefe, dass de Abraham ire Vatter isch, dänn Gott chönn us Stei em Abraham Chind erwecke; d Axt liggi scho a de Wurzle vo de Bäum. Er tauft mit Wasser zur Umkehr; dä, wo nach ihm chunnt, isch stärcher als er, wird mit heilige Geischt und Füür taufe, sin Weize i d Schüür sammle und d Sprüür mit Füür verbrenne, wo nie uusgaat."),
 "TU-MAT-003-013-017": ("D Taufi vom Jesus",
  "De Jesus chunnt vo Galiläa a de Jordan zum Johannes, zum sich vo ihm la taufe. De Johannes wott en abhalte, dänn er heig s nötig, vom Jesus tauft z wärde. De Jesus antwortet: «Lass es jetzt zue! Dänn so ghört es sich für üs, alli Grächtigkeit z erfülle.» Dänn laat de Johannes en mache. Wo de Jesus nach de Taufi us em Wasser ufechunnt, gönd d Himel uf; er gseht de Geischt vo Gott wie e Tuube abechoo und uf sich choo, und e Stimm us de Himel seit: «Dä isch min liebe Sohn, a däm han ich Gfalle gfunde.»"),
 "TU-MAT-004-001-025": ("D Versuechig und de Aafang z Galiläa",
  "De Geischt füert de Jesus i d Wüeschti, won er nach vierzg Täg Faschte vom Tüüfel versuecht wird; drümal antwortet de Jesus mit eme Schriftwort, bis de Tüüfel vo ihm ablaat und Ängel ihm diened. Wo de Jesus ghört, dass de Johannes usgliferet worde isch, zieht er sich uf Galiläa zrugg und wohnt z Kafarnaum; nach em Erzeller erfüllt sich demit s Wort vom Jesaja vom Liecht für Galiläa vo de Völker. Vo dänn aa verchündet de Jesus: «Chehred um, dänn s Riich vo de Himel isch nöch choo!» Am See vo Galiläa rüeft er d Brüeder Simon Petrus und Andreas, dänn de Jakobus, de Sohn vom Zebedäus, und sin Brueder Johannes; di einte lönd grad iri Netz ligge, di andere s Boot und ire Vatter, und si gönd ihm nache. De Jesus zieht dur ganz Galiläa, lehrt i de Synagoge, verchündet s Evangelium vom Riich und heilt Chranki vo allerlei Art; de Ruef vo ihm gaat dur ganz Syrie, und vili Schaare vo Lüüt gönd ihm nache."),
 "TU-MAT-004-001-011": ("D Versuechig vom Jesus",
  "De Geischt füert de Jesus i d Wüeschti ufe, demit er vom Tüüfel versuecht wird. Nach vierzg Täg und Nächt Faschte hät er Hunger. De Versuecher seit, wänn er de Sohn vo Gott sig, söll er säge, dass d Stei zu Broot wärded; de Jesus antwortet mit [[DEU.8.3]]: De Mänsch läbt nöd vom Broot ellei, sondern vo jedem Wort us em Mund vo Gott. De Tüüfel stellt en uf d Zinne vom Tämpel i de heilige Stadt und forderet en mit [[PSA.91.11]]–[[PSA.91.12]] uf, sich abezrüere; de Jesus antwortet mit [[DEU.6.16]]: «Du söllsch de Herr, din Gott, nöd uf d Prob stelle.» Uf eme ganz hööche Bärg zeigt ihm de Tüüfel alli Riich vo de Wält und verspricht si ihm, wänn er sich uf de Bode wärfi und en aabätti. De Jesus seit: «Gang wäg, Satan!» und antwortet mit [[DEU.6.13]]: De Herr, din Gott, söllsch du aabätte und ihm ellei diene. Dänn laat de Tüüfel vo ihm ab, und Ängel chömed ane und diened ihm."),
 "TU-MAT-004-012-017": ("De Jesus zieht uf Galiläa",
  "Wo de Jesus ghört, dass de Johannes usgliferet worde isch, zieht er sich uf Galiläa zrugg. Er verlaat Nazaret und chunnt uf Kafarnaum am See cho wohne, is Gebiet vo Sebulon und Naftali. Nach em Erzeller passiert das, demit sich erfüllt, was dur de Jesaja gseit worden isch ([[ISA.9.1]]–[[ISA.9.2]]): S Volk, wo i de Fiischteri gsässe isch, hät es grosses Liecht gseh. Vo dänn aa faat de Jesus aa verchünde: «Chehred um, dänn s Riich vo de Himel isch nöch choo!»"),
 "TU-MAT-004-018-022": ("Di erschte Jünger",
  "Am See vo Galiläa gseht de Jesus d Brüeder Simon, wo mer Petrus seit, und Andreas, Fischer, wo es Wurfnetz uswärfed. Er seit zu ine: «Chömed mir nache, und ich mache eu zu Mänschefischer!» Grad lönd si d Netz ligge und gönd ihm nache. Wiiter gseht er de Jakobus, de Sohn vom Zebedäus, und sin Brueder Johannes, wo mit irem Vatter im Boot iri Netz parat mached, und rüeft si; grad lönd si s Boot und ire Vatter zrugg und gönd ihm nache."),
 "TU-MAT-004-023-025": ("De Jesus lehrt, verchündet und heilt",
  "De Jesus zieht dur ganz Galiläa, lehrt i irne Synagoge, verchündet s Evangelium vom Riich und heilt jedi Chranket und jedes Liide im Volk. De Ruef vo ihm gaat dur ganz Syrie; mer bringt ihm alli Chranke, wo vo allerlei Chrankete und Quale plaget sind: Bsässni, Mondsüchtigi und Glähmti; und er heilt si. Vili Schaare vo Lüüt us Galiläa, de Dekapolis, Jerusalem, Judäa und vo änet em Jordan gönd ihm nache."),
}

NOTES_DE = [
 "KI-Entwurf ohne fachliche Prüfung.",
 ("Die Zuordnung von Handschriften zu Lesarten beruht auf maschineller Kollation (METHOD-AUTO-COLLATION-V1) und dem dort "
  "erfassten Wortlaut der CNTR-Transkriptionen (Sekundärtranskription, nicht am Faksimile geprüft), nicht auf eigener Prüfung "
  "der Handschriften. Wo die Zuordnung dem erfassten Wortlaut oder den Sigla des Apparats widerspricht, ist das bei der "
  "Alternative benannt ([[MAT.4.12]], [[MAT.4.23]]); massgeblich für die Ausgaben sind die Sigla des SBLGNT-Apparats. Zahlen zu "
  "Wortvorkommen sind per Skript aus den MACULA-Lemmata des SBLGNT-Texts gezählt."),
 ("Einheitliche Matthäus-Begriffe (für alle Matthäus-Bereiche abgestimmt): ἡ βασιλεία τῶν οὐρανῶν «das Reich der Himmel»; "
  "ἡ βασιλεία τοῦ θεοῦ «das Reich Gottes»; ὁ υἱὸς τοῦ ἀνθρώπου «der Menschensohn»; ἀμὴν λέγω ὑμῖν «Amen, ich sage euch»; "
  "ὁ πατὴρ ὁ ἐν τοῖς οὐρανοῖς «Vater in den Himmeln»; ἰδού «siehe»; εὐθέως/εὐθύς «sogleich»; τότε «da/dann»; Schriftgelehrte, "
  "Pharisäer, Sadduzäer, Hohepriester, Älteste; μετανοέω/μετάνοια «umkehren/Umkehr»; δαιμόνιον «Dämon», δαιμονιζόμενος "
  "«Besessener»; πνεῦμα ἅγιον «heiliger Geist»; Χριστός «Christus»; die Erfüllungsformel «damit erfüllt würde, was … durch den "
  "Propheten gesagt ist». Pharisäer, Sadduzäer und andere Gruppen werden neutral bezeichnet."),
 ("In Kapitel 3–4 neu festgelegt und für die übrigen Kapitel vorgeschlagen (Begründung in decisions): δικαιοσύνη «Gerechtigkeit»; "
  "πειράζω «versuchen» (beim Teufel; wo Menschen prüfen, «auf die Probe stellen»), ἐκπειράζω «auf die Probe stellen»; διάβολος "
  "«Teufel», ὁ πειράζων «der Versucher», Σατανᾶς «Satan»; προσέρχομαι «herantreten»; προσκυνέω «anbeten» (Gott) bzw. «sich "
  "niederwerfen vor» nach Zusammenhang; ἀναχωρέω «sich zurückziehen»; τὰ ἔθνη «die Völker»; ὄχλος «Menge», Plural "
  "«Menschenmengen»; θάλασσα im Erzähltext «See», im Zitat «Meer»; γεννήματα ἐχιδνῶν «Schlangenbrut»; καρπός «Frucht»; "
  "τὸ εὐαγγέλιον τῆς βασιλείας «das Evangelium vom Reich»; γέγραπται «es steht geschrieben»; σεληνιαζόμενος «mondsüchtig»."),
 ("Erzählweise: Das erzählende Präsens des Matthäus ist beibehalten, auch wo es mit Vergangenheitsformen wechselt ([[MAT.4.5]]). "
  "ὅτι und λέγων bzw. λέγοντος vor direkter Rede oder einem Zitat sind nicht eigens übersetzt. Anführungszeichen sind eine "
  "Entscheidung der Übersetzung. Bei Parallelen zu Markus ist dieselbe griechische Wendung möglichst gleich übersetzt "
  "(z. B. [[MAT.3.6]] wie [[MRK.1.5]], [[MAT.4.18]]–[[MAT.4.22]] wie [[MRK.1.16]]–[[MRK.1.20]]); wo Matthäus anders formuliert, "
  "folgt die Übersetzung ihm."),
 ("Text: Die Übersetzung folgt den SBLGNT-Tokens, auch wo der SBLGNT gegen NA28 liest ([[MAT.3.16]] ohne «ihm» und ohne "
  "Artikel bei «Geist Gottes», [[MAT.4.24]] ohne καί). Abweichende Lesarten stehen als Alternativen, soweit sie die Übersetzung "
  "verändern; reine Wortstellungsvarianten und Varianten ohne Wirkung auf den deutschen Wortlaut (z. B. [[MAT.4.16]] σκότει "
  "statt σκοτίᾳ, beides «Finsternis») sind nicht aufgenommen. In Kapitel 3–4 fehlt im SBLGNT kein Vers (per Skript geprüft)."),
 ("Gliederung: Kapitel 3 in zwei Abschnitte (Johannes der Täufer; Taufe Jesu), Kapitel 4 in vier (Versuchung; Rückzug nach "
  "Galiläa und Beginn der Verkündigung; Berufung der ersten Jünger; Summarium [[MAT.4.23]]–[[MAT.4.25]], das zur Bergpredigt "
  "überleitet)."),
 "Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen.",
]
NOTES_GSW = [
 "KI-Entwurf ohni fachlichi Prüefig.",
 "D Mundart isch no nöd vo ere muettersprachliche Person prüeft.",
 ("D Zueornig vo Handschrifte zu Läsarte beruet uf maschineller Kollation (METHOD-AUTO-COLLATION-V1) und em dört erfasste "
  "Wortlut vo de CNTR-Transkriptione, nöd uf eigeter Prüefig vo de Handschrifte."),
 ("Einheitlichi Begriff im Matthäus: «s Riich vo de Himel», «s Riich vo Gott», «de Mänschesohn», «Amen, ich säg eu», «Vatter i "
  "de Himel», ἰδού «lueg», εὐθέως/εὐθύς «grad», τότε «dänn», «Chehred um», «Umkehr», «Dämon», «Bsässne», «heilige Geischt», "
  "«Christus», d Erfüllungsformle «demit erfüllt wird, was … dur de Prophet gseit worden isch»."),
 ("I Kapitel 3–4 neu feschtgleit (Vorschlag für di andere Kapitel): δικαιοσύνη «Grächtigkeit»; πειράζω «versueche» (bim "
  "Tüüfel), ἐκπειράζω «uf d Prob stelle»; διάβολος «Tüüfel», ὁ πειράζων «de Versuecher»; προσέρχομαι «anechoo»; προσκυνέω "
  "«aabätte» (vor Gott); ἀναχωρέω «sich zruggzie»; τὰ ἔθνη «d Völker»; ὄχλοι «Schaare vo Lüüt»; θάλασσα «See» (im Zitat «Meer»); "
  "«Schlangebruet»; «s Evangelium vom Riich»; δαιμονιζόμενοι «Bsässni»; «Mondsüchtigi»."),
 ("Mundart: Näme mit Artikel («de Jesus», «de Johannes»); Perfekt statt Präteritum, nu s erzellend Präsens bliibt; «wo» als "
  "Relativwort; kei Genitiv («s Riich vo de Himel»)."),
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
                            "orthography_de": "Dieth-Schreibung (Schwyzertütschi Dialäktschrift, 2. Aufl. 1986), lautnah: lange Vokale doppelt (Liecht, Riich), ä für offenes e.",
                            "register_de": "Nah am griechischen Wortlaut, aber so, wie man es sagt: Perfekt statt Präteritum, «wo» als Relativpartikel, kein Genitiv, Namen mit Artikel. Jede Abweichung vom Wörtlichen ist in decisions markiert.",
                            "control_translation": f"TRANS-MAT-{c:03d}-001-{last:03d}-DE-WORKING",
                            "review_de": "Mundart noch nicht geprüft. Vorgesehen: Prüfung durch Andi Neck (Muttersprachler), mit Datum einzutragen."})
            rec.update({"method_de": ("Wörtlich orientierte Arbeitsübersetzung aus dem SBLGNT: Satzbau und Wortwahl des Griechischen möglichst sichtbar, verständliches Deutsch; erzählendes Präsens beibehalten; wiederkehrende Begriffe für das ganze Matthäusevangelium einheitlich (siehe translation_notes). Schweizer Rechtschreibung. Eigene Formulierung; nicht aus einer veröffentlichten deutschen Bibel übernommen."
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
                "target_convention_de": "« … » trennt nicht zusammenhängende Teile des Wortlauts. Text und Zuordnung sind aus derselben Auszeichnung erzeugt (scripts/authoring/matthaeus_text_03_04.py).",
                "authorship_de": AUTH if lang == "de" else AUTH_GSW, "knowledge": {"asserted_at": DATE, "supersedes": None},
                "alignments": aligns})
    print(f"PASS: Matthäus 3–4 – Texteinheiten, Übersetzungen de/gsw, Wortzuordnung; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
