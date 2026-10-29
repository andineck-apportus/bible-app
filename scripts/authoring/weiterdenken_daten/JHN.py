"""Weiterdenken zu Johannes (Entscheid Andi Neck 2026-10-28, «Vertiefen»): Fragen zum Weiterdenken für jeden Abschnitt,
jedes Kapitel und das Buch, dazu «Wie man es gelesen hat». KI-Entwürfe ohne fachliche Prüfung; Quellen in frei zugänglichen
Ausgaben nachgeschlagen (source_check), Mundart nach scripts/authoring/lukas_einheitlich.py, Zitate nach der Arbeitsübersetzung.

Prüfvermerk (PROC-WEITERDENKEN@1.0, Schritte 3 und 4): Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung,
Claude) gegen die hochdeutsche Arbeitsübersetzung geprüft: alle 250 Fragen und Hintergrundsätze (offen, nicht suggestiv,
nicht moralisierend, kein Glaube vorausgesetzt, keine christologische oder konfessionelle Streitfrage entschieden, Umgang
mit «die Juden» in Kap. 1, 5–10, 16 und 18–19; Zitate per Skript wörtlich verglichen, Stellenmarken), Mundart nach
pruefe_mundart; Quellen aller 15 Einträge «Wie man es gelesen hat» erneut nachgeschlagen (Vermerk im source_check), bei
der Johannes-Passion die Wirkungsfrage nach Judenfeindschaft ergänzt. Grenzen: nicht gegen den griechischen Text geprüft;
Eusebius und Augustinus über andere frei zugängliche Ausgaben als die verlinkten; Mundart-Zitate nur gegen die
Mundart-Arbeitsübersetzung verglichen; keine fachliche und keine muttersprachliche Prüfung durch eine Person."""
DATE = "2026-10-28"
PROCESS = "PROC-WEITERDENKEN@1.0"
TAGS = ["TAG-JOHN"]
AUTHORSHIP_DE = "KI-Entwurf (Claude) vom 2026-10-28 (Weiterdenken Johannes, Entscheid Andi Neck); keine fachliche Prüfung."

REFLECTIONS = [
    # SUM-BOOK-JHN
    {"id": "REFL-JHN-0001", "subject": "SUM-BOOK-JHN", "order": 1,
     "question_de": "Das Buch sagt selbst, wozu es geschrieben ist: Was erwartest du, wenn du es liest?",
     "note_de": "«Diese aber sind aufgeschrieben, damit ihr glaubt … und damit ihr als Glaubende Leben habt in seinem Namen» ([[JHN.20.31]]).",
     "gsw": {"question_de": "S Buech seit sälber, für was s gschribe isch: Was erwartisch du, wänn d s lisisch?", "note_de": "«Die aber sind ufgschribe, demit ir glaubed … und demit ir als Gläubigi Läbe händ in sim Name» ([[JHN.20.31]])."}},
    {"id": "REFL-JHN-0002", "subject": "SUM-BOOK-JHN", "order": 2,
     "question_de": "Viele Menschen in diesem Buch fragen, woher Jesus kommt: Welche Antwort geben sie, und welche das Buch?",
     "gsw": {"question_de": "Vil Lüüt i dem Buech fröged, wohär de Jesus chunnt: Weli Antwort gäbed sie, und weli s Buech?"}},
    {"id": "REFL-JHN-0003", "subject": "SUM-BOOK-JHN", "order": 3,
     "question_de": "Das Buch erzählt von Menschen, die glauben, zweifeln oder weggehen: Bei wem verweilst du am längsten?",
     "gsw": {"question_de": "S Buech verzellt vo Mänsche, wo glaubed, zwiifled oder wäggönd: Bi wem bliibsch du am längschte?"}},
    # SUM-CH-JHN-001
    {"id": "REFL-JHN-0004", "subject": "SUM-CH-JHN-001", "order": 1,
     "question_de": "Was suchst du, wenn du dieses Buch zu lesen beginnst?",
     "note_de": "Die ersten Worte Jesu im Buch sind eine Frage an zwei, die ihm folgen: «Was sucht ihr?» ([[JHN.1.38]]).",
     "gsw": {"question_de": "Was suechsch du, wänn d aafangsch, das Buech läse?", "note_de": "Di erschte Wort vom Jesus im Buech sind e Frag a zwei, wo ihm folged: «Was sueched ir?» ([[JHN.1.38]])."}},
    # TU-JHN-001-001-018
    {"id": "REFL-JHN-0005", "subject": "TU-JHN-001-001-018", "order": 1,
     "question_de": "Warum beginnt dieses Buch nicht mit einer Geburt, sondern «im Anfang»?",
     "note_de": "Die ersten Worte erinnern an den Anfang der Bibel ([[GEN.1.1]]); von Jesus ist erst später mit Namen die Rede ([[JHN.1.17]]).",
     "gsw": {"question_de": "Wieso fangt das Buech nöd mit ere Geburt aa, sondern «im Aafang»?", "note_de": "Di erschte Wort erinnered a de Aafang vo de Bible ([[GEN.1.1]]); vom Jesus isch erscht spöter mit Name d Red ([[JHN.1.17]])."}},
    {"id": "REFL-JHN-0006", "subject": "TU-JHN-001-001-018", "order": 2,
     "question_de": "Das Wort wurde «Fleisch»: Warum wohl dieses Wort und nicht einfach «Mensch»?",
     "gsw": {"question_de": "S Wort isch «Fleisch» worde: Wieso ächt grad das Wort und nöd eifach «Mänsch»?"}},
    {"id": "REFL-JHN-0007", "subject": "TU-JHN-001-001-018", "order": 3,
     "question_de": "«Die Seinen nahmen ihn nicht auf»: Wer sind «die Seinen» – und was ändert sich, je nachdem, wie man es versteht?",
     "note_de": "Manche verstehen darunter Israel, andere die Menschen überhaupt; kurz zuvor heisst es, die Welt habe ihn nicht erkannt ([[JHN.1.10-JHN.1.11]]).",
     "gsw": {"question_de": "«Di Sine händ ihn nöd ufgnoo»: Wer sind «di Sine» – und was änderet sich, je nachdem, wie mer s verstaat?", "note_de": "Di eine verstönd drunder Israel, anderi d Mänsche überhaupt; churz vorher heisst s, d Wält heig en nöd erchännt ([[JHN.1.10-JHN.1.11]])."}},
    # TU-JHN-001-019-028
    {"id": "REFL-JHN-0008", "subject": "TU-JHN-001-019-028", "order": 1,
     "question_de": "Johannes sagt dreimal, wer er nicht ist: Warum ist das wichtig?",
     "note_de": "«Ich bin nicht der Christus» – «Ich bin es nicht» – «Nein» ([[JHN.1.20-JHN.1.21]]).",
     "gsw": {"question_de": "De Johannes seit drüü Mal, wer er nöd isch: Wieso isch das wichtig?", "note_de": "«Ich bi nöd de Christus» – «Ich bi s nöd» – «Nei» ([[JHN.1.20-JHN.1.21]])."}},
    {"id": "REFL-JHN-0009", "subject": "TU-JHN-001-019-028", "order": 2,
     "question_de": "Was würdest du antworten, wenn man dich fragt, wer du bist?",
     "gsw": {"question_de": "Was würdsch du antworte, wänn mer dich fröget, wer du bisch?"}},
    # TU-JHN-001-029-034
    {"id": "REFL-JHN-0010", "subject": "TU-JHN-001-029-034", "order": 1,
     "question_de": "Was mag ein Zuhörer damals bei «Lamm Gottes» gedacht haben?",
     "note_de": "Johannes sagt es zweimal, beim ersten Mal mit dem Zusatz «das die Sünde der Welt wegnimmt» ([[JHN.1.29]], [[JHN.1.36]]).",
     "gsw": {"question_de": "Was hät en Zuehörer dänn ächt bi «Lamm vo Gott» dänkt?", "note_de": "De Johannes seit s zwei Mal, s erscht Mal mit em Zuesatz «wo d Sünd vo de Wält wägnimmt» ([[JHN.1.29]], [[JHN.1.36]])."}},
    {"id": "REFL-JHN-0011", "subject": "TU-JHN-001-029-034", "order": 2,
     "question_de": "Johannes sagt zweimal: «Ich kannte ihn nicht.» Wie kann man jemanden erkennen, den man nicht kennt?",
     "gsw": {"question_de": "De Johannes seit zwei Mal: «Ich han en nöd kännt.» Wie chan mer öpper erchänne, wo mer nöd kännt?"}},
    # TU-JHN-001-035-042
    {"id": "REFL-JHN-0012", "subject": "TU-JHN-001-035-042", "order": 1,
     "question_de": "«Kommt, und ihr werdet sehen!» – warum gibt Jesus keine Antwort, sondern eine Einladung?",
     "note_de": "Die beiden hatten nach seiner Bleibe gefragt ([[JHN.1.38-JHN.1.39]]).",
     "gsw": {"question_de": "«Chömed, und ir wärded s gseh!» – wieso git de Jesus kei Antwort, sondern e Iiladig?", "note_de": "Di beide händ nach sinere Bliibi gfröget ([[JHN.1.38-JHN.1.39]])."}},
    {"id": "REFL-JHN-0013", "subject": "TU-JHN-001-035-042", "order": 2,
     "question_de": "Andreas holt zuerst seinen Bruder: Wem würdest du von etwas Wichtigem zuerst erzählen?",
     "gsw": {"question_de": "De Andreas holt zerscht sin Brueder: Wem würdsch du vo öppis Wichtigem zerscht verzelle?"}},
    # TU-JHN-001-043-051
    {"id": "REFL-JHN-0014", "subject": "TU-JHN-001-043-051", "order": 1,
     "question_de": "Natanaël zweifelt an Nazaret – was bewegt ihn trotzdem zu gehen?",
     "note_de": "«Kann aus Nazaret etwas Gutes kommen?» – «Komm und sieh!» ([[JHN.1.46]])",
     "gsw": {"question_de": "De Natanaël zwiiflet a Nazaret – was bringt en glich derzue, zgaa?", "note_de": "«Cha us Nazaret öppis Guets choo?» – «Chumm und lueg!» ([[JHN.1.46]])"}},
    {"id": "REFL-JHN-0015", "subject": "TU-JHN-001-043-051", "order": 2,
     "question_de": "Wie fühlt es sich an, gesehen zu werden, bevor man selbst etwas gesagt hat?",
     "gsw": {"question_de": "Wie fühlt sich s aa, gseh zwärde, bevor mer sälber öppis gseit hät?"}},
    {"id": "REFL-JHN-0016", "subject": "TU-JHN-001-043-051", "order": 3,
     "question_de": "Jesus kündigt «Grösseres» an: Was erwartest du, wenn du weiterliest?",
     "gsw": {"question_de": "De Jesus chündt «Grössers» aa: Was erwartisch du, wänn d wiiterlisisch?"}},
    # SUM-CH-JHN-002
    {"id": "REFL-JHN-0017", "subject": "SUM-CH-JHN-002", "order": 1,
     "question_de": "Was haben Wein bei einer Hochzeit und ein geräumter Tempel miteinander zu tun?",
     "note_de": "Beide Szenen enden damit, dass die Jünger glauben ([[JHN.2.11]], [[JHN.2.22]]).",
     "gsw": {"question_de": "Was händ Wii a nere Hochziit und en usgrüümte Tämpel mitenand ztue?", "note_de": "Beid Szene hööred dermit uf, dass d Jünger glaubed ([[JHN.2.11]], [[JHN.2.22]])."}},
    # TU-JHN-002-001-012
    {"id": "REFL-JHN-0018", "subject": "TU-JHN-002-001-012", "order": 1,
     "question_de": "Jesus sagt «Meine Stunde ist noch nicht gekommen» – und handelt dann doch: Was hat seine Mutter verstanden?",
     "note_de": "Sie sagt zu den Dienern: «Was er euch auch sagt, das tut!» ([[JHN.2.4-JHN.2.5]])",
     "gsw": {"question_de": "De Jesus seit «Mini Stund isch no nöd choo» – und handlet dänn glich: Was hät sini Mueter verstande?", "note_de": "Si seit zu de Diener: «Was er eu au seit, das mached!» ([[JHN.2.4-JHN.2.5]])"}},
    {"id": "REFL-JHN-0019", "subject": "TU-JHN-002-001-012", "order": 2,
     "question_de": "Die Diener wissen, woher der Wein kommt, der Speisemeister nicht: Was sehen die, die mitarbeiten?",
     "gsw": {"question_de": "D Diener wüssed, wohär de Wii chunnt, de Spiismeischter nöd: Was gsehnd die, wo mitschaffed?"}},
    {"id": "REFL-JHN-0020", "subject": "TU-JHN-002-001-012", "order": 3,
     "question_de": "Warum ist ausgerechnet ein Fest der «Anfang der Zeichen»?",
     "gsw": {"question_de": "Wieso isch grad es Fäscht de «Aafang vo de Zeiche»?"}},
    # TU-JHN-002-013-022
    {"id": "REFL-JHN-0021", "subject": "TU-JHN-002-013-022", "order": 1,
     "question_de": "Die Jünger verstehen das Wort vom Tempel erst nach seiner Auferweckung: Was versteht man oft erst im Rückblick?",
     "note_de": "«Als er nun von den Toten auferweckt worden war, erinnerten sich seine Jünger» ([[JHN.2.22]]).",
     "gsw": {"question_de": "D Jünger verstönd s Wort vom Tämpel erscht nach sinere Uferweckig: Was verstaht mer oft erscht im Ruggblick?", "note_de": "«Wo er dänn vo de Tote uferweckt worde isch, händ sich sini Jünger erinneret» ([[JHN.2.22]])."}},
    {"id": "REFL-JHN-0022", "subject": "TU-JHN-002-013-022", "order": 2,
     "question_de": "Was mögen die Händler und Geldwechsler empfunden haben, deren Arbeit doch dem Tempel diente?",
     "gsw": {"question_de": "Was händ ächt d Händler und Gäldwächsler gfühlt, wo mit irer Arbet doch em Tämpel dient händ?"}},
    # TU-JHN-002-023-025
    {"id": "REFL-JHN-0023", "subject": "TU-JHN-002-023-025", "order": 1,
     "question_de": "Viele glauben, und Jesus vertraut sich ihnen nicht an: Was für ein Glaube ist das?",
     "note_de": "Sie glauben, «da sie seine Zeichen sahen» ([[JHN.2.23-JHN.2.24]]).",
     "gsw": {"question_de": "Vil glaubed, und de Jesus vertrout sich ine nöd aa: Was isch das für en Glaube?", "note_de": "Si glaubed, «wil si sini Zeiche gseh händ» ([[JHN.2.23-JHN.2.24]])."}},
    {"id": "REFL-JHN-0024", "subject": "TU-JHN-002-023-025", "order": 2,
     "question_de": "Wie ist es für dich, dass jemand weiss, «was im Menschen war»?",
     "gsw": {"question_de": "Wie isch es für dich, dass öpper weiss, «was im Mänsch isch»?"}},
    # SUM-CH-JHN-003
    {"id": "REFL-JHN-0025", "subject": "SUM-CH-JHN-003", "order": 1,
     "question_de": "Nikodemus kommt bei Nacht und verschwindet aus dem Gespräch: Was nimmt er wohl mit?",
     "note_de": "Er taucht später wieder auf, im Hohen Rat und beim Begräbnis Jesu ([[JHN.7.50]], [[JHN.19.39]]).",
     "gsw": {"question_de": "De Nikodemus chunnt znacht und verschwindet us em Gspröch: Was nimmt er ächt mit?", "note_de": "Er chunnt spöter wider vor, im Hoche Root und bi de Beärdigung vom Jesus ([[JHN.7.50]], [[JHN.19.39]])."}},
    # TU-JHN-003-001-015
    {"id": "REFL-JHN-0026", "subject": "TU-JHN-003-001-015", "order": 1,
     "question_de": "Warum kommt Nikodemus bei Nacht?",
     "note_de": "Der Text sagt es nicht; er nennt nur die Zeit ([[JHN.3.2]]).",
     "gsw": {"question_de": "Wieso chunnt de Nikodemus znacht?", "note_de": "De Text seit s nöd; er nännt nu d Ziit ([[JHN.3.2]])."}},
    {"id": "REFL-JHN-0027", "subject": "TU-JHN-003-001-015", "order": 2,
     "question_de": "«Von oben geboren» – man kann auch übersetzen: neu geboren. Was hörst du in diesem Wort?",
     "gsw": {"question_de": "«Vo obe gebore» – mer chan au übersetze: nöi gebore. Was ghörsch du i dem Wort?"}},
    {"id": "REFL-JHN-0028", "subject": "TU-JHN-003-001-015", "order": 3,
     "question_de": "Ein Lehrer Israels versteht etwas nicht: Wie geht es dir, wenn du Vertrautes plötzlich nicht mehr verstehst?",
     "gsw": {"question_de": "En Lehrer vo Israel verstaht öppis nöd: Wie gaat s dir, wänn d Vertrauts plötzlich nüme verstaasch?"}},
    # TU-JHN-003-016-021
    {"id": "REFL-JHN-0029", "subject": "TU-JHN-003-016-021", "order": 1,
     "question_de": "Was heisst es, dass Gott «die Welt» liebt – und nicht nur einige?",
     "note_de": "Im selben Abschnitt liebt «die Welt» die Finsternis mehr als das Licht ([[JHN.3.16]], [[JHN.3.19]]).",
     "gsw": {"question_de": "Was heisst s, dass Gott «d Wält» liebt – und nöd nu es paar?", "note_de": "Im gliiche Abschnitt hät «d Wält» d Fiischteri lieber als s Liecht ([[JHN.3.16]], [[JHN.3.19]])."}},
    {"id": "REFL-JHN-0030", "subject": "TU-JHN-003-016-021", "order": 2,
     "question_de": "«Das aber ist das Gericht: Das Licht ist in die Welt gekommen …»: Was heisst «Gericht», wenn es so beschrieben wird?",
     "gsw": {"question_de": "«Das aber isch s Gricht: S Liecht isch i d Wält choo …»: Was heisst «Gricht», wänn s eso beschribe wird?"}},
    # TU-JHN-003-022-030
    {"id": "REFL-JHN-0031", "subject": "TU-JHN-003-022-030", "order": 1,
     "question_de": "Wie gelingt es Johannes, sich zu freuen, während alle zu einem anderen gehen?",
     "note_de": "Er vergleicht sich mit dem Freund des Bräutigams ([[JHN.3.29]]).",
     "gsw": {"question_de": "Wie bringt s de Johannes fertig, sich zfröie, während alli zu me andere gönd?", "note_de": "Er vergliicht sich mit em Fründ vom Brütigam ([[JHN.3.29]])."}},
    {"id": "REFL-JHN-0032", "subject": "TU-JHN-003-022-030", "order": 2,
     "question_de": "«Er muss wachsen, ich aber kleiner werden» – ist das Verzicht oder Erfüllung?",
     "gsw": {"question_de": "«Er mues wachse, ich aber chliiner wärde» – isch das Verzicht oder Erfüllig?"}},
    # TU-JHN-003-031-036
    {"id": "REFL-JHN-0033", "subject": "TU-JHN-003-031-036", "order": 1,
     "question_de": "Wer spricht hier – Johannes, Jesus oder der Erzähler?",
     "note_de": "Der Text setzt keine Anführungszeichen; die Übersetzungen ziehen die Grenze verschieden ([[JHN.3.31]]).",
     "gsw": {"question_de": "Wer redt da – de Johannes, de Jesus oder de Verzeller?", "note_de": "De Text setzt kei Aafüerigszeiche; d Übersetzige ziend d Gränze verschide ([[JHN.3.31]])."}},
    {"id": "REFL-JHN-0034", "subject": "TU-JHN-003-031-036", "order": 2,
     "question_de": "Was unterscheidet ein Zeugnis «von oben» von einem «von der Erde her»?",
     "gsw": {"question_de": "Was unterscheidet es Zügnis «vo obe» vo eim «vo de Ärde här»?"}},
    # SUM-CH-JHN-004
    {"id": "REFL-JHN-0035", "subject": "SUM-CH-JHN-004", "order": 1,
     "question_de": "Eine Fremde, eine ganze Stadt, ein königlicher Beamter: Wer findet in diesem Kapitel zum Glauben, und wie?",
     "note_de": "Am Ende sagen die Samariter: «… dass dieser wirklich der Retter der Welt ist» ([[JHN.4.42]]).",
     "gsw": {"question_de": "E Frömdi, e ganzi Stadt, en königliche Beamte: Wer findet i dem Kapitel zum Glaube, und wie?", "note_de": "Am Schluss säged d Samariter: «… dass dä würkli de Retter vo de Wält isch» ([[JHN.4.42]])."}},
    # TU-JHN-004-001-015
    {"id": "REFL-JHN-0036", "subject": "TU-JHN-004-001-015", "order": 1,
     "question_de": "Jesus bittet zuerst um Wasser: Was ändert es, dass er selbst durstig ist?",
     "note_de": "Er ist müde von der Reise und sitzt an der Quelle ([[JHN.4.6-JHN.4.7]]).",
     "gsw": {"question_de": "De Jesus bittet zerscht um Wasser: Was änderet s, dass er sälber Durscht hät?", "note_de": "Er isch müed vo de Reis und sitzt a de Quelle ([[JHN.4.6-JHN.4.7]])."}},
    {"id": "REFL-JHN-0037", "subject": "TU-JHN-004-001-015", "order": 2,
     "question_de": "Die Frau wundert sich, dass ein Jude eine Samariterin anspricht: Welche Grenzen werden hier überschritten?",
     "gsw": {"question_de": "D Frau wundered sich, dass en Jud e Samariterin aaredt: Weli Gränze wärded da überschritte?"}},
    {"id": "REFL-JHN-0038", "subject": "TU-JHN-004-001-015", "order": 3,
     "question_de": "Wonach hast du Durst, der mit Wasser nicht zu stillen ist?",
     "gsw": {"question_de": "Nach was häsch du Durscht, wo mer mit Wasser nöd cha stille?"}},
    # TU-JHN-004-016-026
    {"id": "REFL-JHN-0039", "subject": "TU-JHN-004-016-026", "order": 1,
     "question_de": "Jesus spricht ihr Leben an, ohne ein Urteil auszusprechen: Wie hört sie das?",
     "note_de": "Sie antwortet: «Herr, ich sehe, dass du ein Prophet bist» ([[JHN.4.19]]).",
     "gsw": {"question_de": "De Jesus redt ires Läbe aa, ohni es Urteil uszspräche: Wie ghört si das?", "note_de": "Si antwortet: «Herr, ich gseh, dass du en Prophet bisch» ([[JHN.4.19]])."}},
    {"id": "REFL-JHN-0040", "subject": "TU-JHN-004-016-026", "order": 2,
     "question_de": "Auf diesem Berg oder in Jerusalem? Warum fragt sie gerade das?",
     "gsw": {"question_de": "Uf dem Bärg oder z Jerusalem? Wieso fröget si grad das?"}},
    {"id": "REFL-JHN-0041", "subject": "TU-JHN-004-016-026", "order": 3,
     "question_de": "Was könnte es heissen, «in Geist und Wahrheit» anzubeten?",
     "gsw": {"question_de": "Was chönt s heisse, «i Geischt und Wahrheit» aazbätte?"}},
    # TU-JHN-004-027-038
    {"id": "REFL-JHN-0042", "subject": "TU-JHN-004-027-038", "order": 1,
     "question_de": "Die Frau lässt ihren Wasserkrug stehen: Was lässt sie damit zurück?",
     "note_de": "Sie war zum Schöpfen gekommen ([[JHN.4.7]], [[JHN.4.28]]).",
     "gsw": {"question_de": "D Frau laat ire Wasserchrueg stah: Was laat si dermit zrugg?", "note_de": "Si isch zum Schöpfe choo ([[JHN.4.7]], [[JHN.4.28]])."}},
    {"id": "REFL-JHN-0043", "subject": "TU-JHN-004-027-038", "order": 2,
     "question_de": "Die Jünger wundern sich und fragen doch nicht: Was fragst du lieber nicht?",
     "gsw": {"question_de": "D Jünger wundered sich und fröged glich nöd: Was frögsch du lieber nöd?"}},
    # TU-JHN-004-039-042
    {"id": "REFL-JHN-0044", "subject": "TU-JHN-004-039-042", "order": 1,
     "question_de": "Zuerst glauben sie wegen der Frau, dann «selbst»: Was ist der Unterschied?",
     "note_de": "«Nicht mehr wegen deines Redens glauben wir; wir haben nämlich selbst gehört» ([[JHN.4.42]]).",
     "gsw": {"question_de": "Zerscht glaubed si wäge de Frau, dänn «sälber»: Was isch de Unterschiid?", "note_de": "«Mir glaubed nüme wäge dim Gred; mir händ nämli sälber ghört» ([[JHN.4.42]])."}},
    {"id": "REFL-JHN-0045", "subject": "TU-JHN-004-039-042", "order": 2,
     "question_de": "Wer hat dir etwas weitergegeben, das du später selbst geprüft hast?",
     "gsw": {"question_de": "Wer hät dir öppis wiitergää, wo d spöter sälber prüeft häsch?"}},
    # TU-JHN-004-043-054
    {"id": "REFL-JHN-0046", "subject": "TU-JHN-004-043-054", "order": 1,
     "question_de": "Der Mann geht los, bevor er weiss, ob es stimmt: Was trägt ihn auf diesem Weg?",
     "note_de": "«Der Mann glaubte dem Wort, das Jesus zu ihm gesagt hatte, und machte sich auf den Weg» ([[JHN.4.50]]).",
     "gsw": {"question_de": "De Maa gaat los, bevor er weiss, öb s stimmt: Was treit en uf dem Wäg?", "note_de": "«De Maa hät em Wort glaubt, wo de Jesus zu ihm gseit hät, und hät sich uf de Wäg gmacht» ([[JHN.4.50]])."}},
    {"id": "REFL-JHN-0047", "subject": "TU-JHN-004-043-054", "order": 2,
     "question_de": "Jesus scheint die Bitte zuerst abzuweisen: Warum bleibt der Vater dran?",
     "gsw": {"question_de": "De Jesus schiint d Bitt zerscht abzwiise: Wieso bliibt de Vatter dra?"}},
    # SUM-CH-JHN-005
    {"id": "REFL-JHN-0048", "subject": "SUM-CH-JHN-005", "order": 1,
     "question_de": "Eine Heilung löst einen Streit aus: Worüber wird hier eigentlich gestritten?",
     "note_de": "Zuerst geht es um die Matte am Sabbat, dann darum, dass Jesus Gott seinen Vater nennt ([[JHN.5.10]], [[JHN.5.18]]).",
     "gsw": {"question_de": "E Heilig löst en Striit us: Über was wird da eigentlich gstritte?", "note_de": "Zerscht gaat s um d Matte am Sabbat, dänn drum, dass de Jesus Gott sin Vatter nännt ([[JHN.5.10]], [[JHN.5.18]])."}},
    # TU-JHN-005-001-009
    {"id": "REFL-JHN-0049", "subject": "TU-JHN-005-001-009", "order": 1,
     "question_de": "Warum fragt Jesus einen, der seit achtunddreissig Jahren krank ist, ob er gesund werden will?",
     "note_de": "Der Mann antwortet nicht mit Ja, sondern damit, dass er keinen Menschen hat ([[JHN.5.6-JHN.5.7]]).",
     "gsw": {"question_de": "Wieso fröget de Jesus eine, wo sit achtedriissg Jahr chrank isch, öb er gsund wärde well?", "note_de": "De Maa antwortet nöd mit Ja, sondern dermit, dass er kein Mänsch hät ([[JHN.5.6-JHN.5.7]])."}},
    {"id": "REFL-JHN-0050", "subject": "TU-JHN-005-001-009", "order": 2,
     "question_de": "«Ich habe keinen Menschen»: Wer fehlt Menschen, die lange warten?",
     "gsw": {"question_de": "«Ich ha kei Mänsch»: Wer fäält Mänsche, wo lang warted?"}},
    # TU-JHN-005-010-018
    {"id": "REFL-JHN-0051", "subject": "TU-JHN-005-010-018", "order": 1,
     "question_de": "Der Geheilte weiss nicht, wer ihn geheilt hat: Was bedeutet ihm Jesus?",
     "note_de": "Später meldet er den Juden, dass es Jesus war ([[JHN.5.13]], [[JHN.5.15]]).",
     "gsw": {"question_de": "De Gheilt weiss nöd, wer en gheilt hät: Was bedüütet ihm de Jesus?", "note_de": "Spöter mäldet er de Jude, dass es de Jesus gsii isch ([[JHN.5.13]], [[JHN.5.15]])."}},
    {"id": "REFL-JHN-0052", "subject": "TU-JHN-005-010-018", "order": 2,
     "question_de": "Wie sieht der Streit um den Sabbat aus der Sicht derer aus, die das Gebot ernst nehmen?",
     "gsw": {"question_de": "Wie gseht de Striit um de Sabbat us de Sicht vo dene us, wo s Gebot ärnscht nämed?"}},
    # TU-JHN-005-019-030
    {"id": "REFL-JHN-0053", "subject": "TU-JHN-005-019-030", "order": 1,
     "question_de": "Der Sohn tut nichts von sich aus: Ist das Abhängigkeit oder Nähe?",
     "note_de": "«Der Sohn kann nichts von sich selbst aus tun, ausser was er den Vater tun sieht» ([[JHN.5.19]]).",
     "gsw": {"question_de": "De Sohn macht nüt vo sich us: Isch das Abhängigkeit oder Nöchi?", "note_de": "«De Sohn cha nüüt vo sich sälber uus mache, usser was er de Vatter mache gseht» ([[JHN.5.19]])."}},
    {"id": "REFL-JHN-0054", "subject": "TU-JHN-005-019-030", "order": 2,
     "question_de": "«Aus dem Tod in das Leben hinübergegangen» – schon jetzt: Was könnte das heissen?",
     "gsw": {"question_de": "«Vom Tod is Läbe übere gange» – scho jetzt: Was chönt das heisse?"}},
    # TU-JHN-005-031-047
    {"id": "REFL-JHN-0055", "subject": "TU-JHN-005-031-047", "order": 1,
     "question_de": "Welche Zeugen würdest du nennen, wenn man dich fragt, warum du etwas glaubst – oder nicht glaubst?",
     "note_de": "Jesus nennt Johannes, seine Werke, den Vater und die Schriften ([[JHN.5.33-JHN.5.39]]).",
     "gsw": {"question_de": "Weli Züge würdsch du nänne, wänn mer dich fröget, wieso d öppis glaubsch – oder nöd glaubsch?", "note_de": "De Jesus nännt de Johannes, sini Wärch, de Vatter und d Schrifte ([[JHN.5.33-JHN.5.39]])."}},
    {"id": "REFL-JHN-0056", "subject": "TU-JHN-005-031-047", "order": 2,
     "question_de": "Man kann die Schriften erforschen und doch nicht kommen: Wie geht beides zusammen?",
     "gsw": {"question_de": "Mer chan d Schrifte erforsche und glich nöd choo: Wie gaat beides zäme?"}},
    # SUM-CH-JHN-006
    {"id": "REFL-JHN-0057", "subject": "SUM-CH-JHN-006", "order": 1,
     "question_de": "Am Anfang wollen alle Brot, am Ende bleiben wenige: Was ist dazwischen geschehen?",
     "note_de": "Viele Jünger ziehen sich zurück; Jesus fragt die Zwölf: «Wollt etwa auch ihr weggehen?» ([[JHN.6.66-JHN.6.67]])",
     "gsw": {"question_de": "Am Aafang wänd alli Broot, am Schluss bliibed wenig: Was isch dezwüsche gscheh?", "note_de": "Vil Jünger ziend sich zrugg; de Jesus fröget di Zwölf: «Wänd öppe au ir gaa?» ([[JHN.6.66-JHN.6.67]])"}},
    # TU-JHN-006-001-015
    {"id": "REFL-JHN-0058", "subject": "TU-JHN-006-001-015", "order": 1,
     "question_de": "Andreas zeigt auf fünf Brote und fragt: «Was ist das für so viele?» Was zählt das Wenige?",
     "note_de": "Ein Junge hat fünf Gerstenbrote und zwei Fische ([[JHN.6.9]]).",
     "gsw": {"question_de": "De Andreas zeigt uf füüf Broot und fröget: «Was isch das für so vili?» Was zellt s Wenige?", "note_de": "En Bueb hät füüf Gärschtebroot und zwei Fisch ([[JHN.6.9]])."}},
    {"id": "REFL-JHN-0059", "subject": "TU-JHN-006-001-015", "order": 2,
     "question_de": "Warum zieht sich Jesus zurück, als man ihn zum König machen will?",
     "gsw": {"question_de": "Wieso zieht sich de Jesus zrugg, wo-n-en d Lüüt zum König mache wänd?"}},
    {"id": "REFL-JHN-0060", "subject": "TU-JHN-006-001-015", "order": 3,
     "question_de": "Die Reste werden gesammelt, «damit nichts verloren geht»: Was sagt das über die Fülle?",
     "gsw": {"question_de": "D Räscht wärded gsammlet, «demit nüüt verlore gaat»: Was seit das über d Füli?"}},
    # TU-JHN-006-016-021
    {"id": "REFL-JHN-0061", "subject": "TU-JHN-006-016-021", "order": 1,
     "question_de": "Die Jünger fürchten sich gerade, als Jesus kommt: Wovor genau?",
     "note_de": "Sie sehen ihn auf dem See gehen und nahe an das Boot kommen ([[JHN.6.19]]).",
     "gsw": {"question_de": "D Jünger fürchted sich grad, wo de Jesus chunnt: Vor was genau?", "note_de": "Si gsehnd en uf em See laufe und nöch as Boot choo ([[JHN.6.19]])."}},
    {"id": "REFL-JHN-0062", "subject": "TU-JHN-006-016-021", "order": 2,
     "question_de": "«Ich bin es» – wie klingt das für Menschen in Dunkelheit und Sturm?",
     "gsw": {"question_de": "«Ich bi s» – wie tönt das für Mänsche im Tunkle und im Sturm?"}},
    # TU-JHN-006-022-034
    {"id": "REFL-JHN-0063", "subject": "TU-JHN-006-022-034", "order": 1,
     "question_de": "Jesus sagt der Menge, warum sie ihn sucht: Warum suchst du, was du suchst?",
     "note_de": "«Ihr sucht mich nicht, weil ihr Zeichen gesehen habt, sondern weil ihr von den Broten gegessen habt» ([[JHN.6.26]]).",
     "gsw": {"question_de": "De Jesus seit de Mängi, wieso si en suecht: Wieso suechsch du, was d suechsch?", "note_de": "«Ir sueched mich nöd, wil ir Zeiche gseh händ, sondern wil ir vo de Broot ggässe händ» ([[JHN.6.26]])."}},
    {"id": "REFL-JHN-0064", "subject": "TU-JHN-006-022-034", "order": 2,
     "question_de": "Was ist eine «Speise, die bleibt»?",
     "gsw": {"question_de": "Was isch es «Ässe, wo bliibt»?"}},
    # TU-JHN-006-035-040
    {"id": "REFL-JHN-0065", "subject": "TU-JHN-006-035-040", "order": 1,
     "question_de": "«Ich bin das Brot des Lebens»: Wofür steht Brot im Alltag der damaligen Hörer?",
     "note_de": "Die Menge hat kurz zuvor vom Manna in der Wüste gesprochen ([[JHN.6.31]], [[JHN.6.35]]).",
     "gsw": {"question_de": "«Ich bi s Broot vom Läbe»: Für was staat Broot im Alltag vo de Zuehörer dänn?", "note_de": "D Mängi hät churz vorher vom Manna i de Wüeschti gredt ([[JHN.6.31]], [[JHN.6.35]])."}},
    {"id": "REFL-JHN-0066", "subject": "TU-JHN-006-035-040", "order": 2,
     "question_de": "«Wer zu mir kommt, den werde ich gewiss nicht hinausstossen»: Wem könnte dieser Satz gelten?",
     "gsw": {"question_de": "«Wer zu mir chunnt, dä rüer ich sicher nöd use»: Wem chönt dä Satz gälte?"}},
    # TU-JHN-006-041-051
    {"id": "REFL-JHN-0067", "subject": "TU-JHN-006-041-051", "order": 1,
     "question_de": "Sie berufen sich darauf, seine Eltern zu kennen: Kann Vertrautheit den Blick verstellen – oder auch schärfen?",
     "note_de": "«Ist das nicht Jesus, der Sohn Josefs, dessen Vater und Mutter wir kennen?» ([[JHN.6.42]])",
     "gsw": {"question_de": "Si beruefed sich druf, dass si sini Eltere känned: Chan Vertrautheit de Blick verstelle – oder au schärfe?", "note_de": "«Isch das nöd de Jesus, de Sohn vom Josef, vo däm mir de Vatter und d Mueter känned?» ([[JHN.6.42]])"}},
    {"id": "REFL-JHN-0068", "subject": "TU-JHN-006-041-051", "order": 2,
     "question_de": "Niemand kann kommen, wenn der Vater ihn nicht «zieht»: Was löst dieses Wort bei dir aus?",
     "gsw": {"question_de": "Niemer chan choo, wänn de Vatter en nöd «zieht»: Was löst das Wort bi dir us?"}},
    # TU-JHN-006-052-059
    {"id": "REFL-JHN-0069", "subject": "TU-JHN-006-052-059", "order": 1,
     "question_de": "Die Zuhörer streiten über das Wort vom Fleisch: Was macht es so anstössig?",
     "note_de": "«Wie kann dieser uns sein Fleisch zu essen geben?» ([[JHN.6.52]])",
     "gsw": {"question_de": "D Zuehörer strited über s Wort vom Fleisch: Was macht s so aastössig?", "note_de": "«Wie cha dä üs sis Fleisch z ässe gää?» ([[JHN.6.52]])"}},
    {"id": "REFL-JHN-0070", "subject": "TU-JHN-006-052-059", "order": 2,
     "question_de": "Christen verschiedener Kirchen lesen diesen Abschnitt verschieden: Was hörst du darin?",
     "gsw": {"question_de": "Chrischte vo verschidene Chilche läsed dä Abschnitt verschide: Was ghörsch du drin?"}},
    # TU-JHN-006-060-071
    {"id": "REFL-JHN-0071", "subject": "TU-JHN-006-060-071", "order": 1,
     "question_de": "«Herr, zu wem sollen wir gehen?» – ist das Gewissheit oder Ratlosigkeit?",
     "note_de": "Petrus antwortet auf die Frage «Wollt etwa auch ihr weggehen?» ([[JHN.6.67-JHN.6.68]]).",
     "gsw": {"question_de": "«Herr, zu wem söled mer gaa?» – isch das Gwüssheit oder Ratlosigkeit?", "note_de": "De Petrus antwortet uf d Frag «Wänd öppe au ir gaa?» ([[JHN.6.67-JHN.6.68]])."}},
    {"id": "REFL-JHN-0072", "subject": "TU-JHN-006-060-071", "order": 2,
     "question_de": "Jesus hält die Gehenden nicht auf: Was sagt das über ihn?",
     "gsw": {"question_de": "De Jesus hebt die, wo gönd, nöd uf: Was seit das über ihn?"}},
    {"id": "REFL-JHN-0073", "subject": "TU-JHN-006-060-071", "order": 3,
     "question_de": "Welches Wort ist dir «hart», sodass du es kaum hören kannst?",
     "gsw": {"question_de": "Weles Wort isch für dich «hert», dass d s chuum chasch ghöre?"}},
    # SUM-CH-JHN-007
    {"id": "REFL-JHN-0074", "subject": "SUM-CH-JHN-007", "order": 1,
     "question_de": "Viele reden über Jesus, nur manche mit ihm: Welche Stimmen hörst du in diesem Kapitel?",
     "note_de": "«Er ist gut» – «Nein, sondern er verführt das Volk» ([[JHN.7.12]]).",
     "gsw": {"question_de": "Vil redet über de Jesus, nu es paar mit ihm: Weli Stimme ghörsch du i dem Kapitel?", "note_de": "«Er isch guet» – «Nei, sondern er verfüert s Volk» ([[JHN.7.12]])."}},
    # TU-JHN-007-001-009
    {"id": "REFL-JHN-0075", "subject": "TU-JHN-007-001-009", "order": 1,
     "question_de": "Seine Brüder glauben nicht an ihn und raten ihm doch, sich zu zeigen: Was wollen sie?",
     "note_de": "«Denn auch seine Brüder glaubten nicht an ihn» ([[JHN.7.5]]).",
     "gsw": {"question_de": "Sini Brüeder glaubed nöd an en und rated ihm glich, sich zzeige: Was wänd si?", "note_de": "«Dänn au sini Brüedere händ nöd a en glaubt» ([[JHN.7.5]])."}},
    {"id": "REFL-JHN-0076", "subject": "TU-JHN-007-001-009", "order": 2,
     "question_de": "«Eure Zeit aber ist immer bereit»: Was unterscheidet die Zeit Jesu von ihrer?",
     "gsw": {"question_de": "«Eui Ziit aber isch immer parat»: Was unterscheidet d Ziit vom Jesus vo irere?"}},
    # TU-JHN-007-010-013
    {"id": "REFL-JHN-0077", "subject": "TU-JHN-007-010-013", "order": 1,
     "question_de": "Niemand redet offen über Jesus, aus Furcht: Wann schweigst du, obwohl du eine Meinung hast?",
     "note_de": "In der Menge wird gemurmelt, doch niemand redet offen über ihn ([[JHN.7.12-JHN.7.13]]).",
     "gsw": {"question_de": "Niemer redt offe über de Jesus, us Angscht: Wänn schwiigsch du, obwohl d e Meinig häsch?", "note_de": "I de Mängi wird gmurmlet, aber niemer redt offe über ihn ([[JHN.7.12-JHN.7.13]])."}},
    {"id": "REFL-JHN-0078", "subject": "TU-JHN-007-010-013", "order": 2,
     "question_de": "Die Menge urteilt «er ist gut» oder «er verführt»: Was bräuchte es für ein eigenes Urteil?",
     "gsw": {"question_de": "D Mängi urteilt «er isch guet» oder «er verfüert»: Was bruuchti s für es eigets Urteil?"}},
    # TU-JHN-007-014-024
    {"id": "REFL-JHN-0079", "subject": "TU-JHN-007-014-024", "order": 1,
     "question_de": "Wie urteilt man «nicht nach dem Augenschein»?",
     "note_de": "So schliesst Jesus seinen Vergleich von Beschneidung und Heilung am Sabbat ([[JHN.7.24]]).",
     "gsw": {"question_de": "Wie urteilt mer «nöd nach em Aaschii»?", "note_de": "So schlüsst de Jesus sin Vergliich vo Beschniidig und Heilig am Sabbat ([[JHN.7.24]])."}},
    {"id": "REFL-JHN-0080", "subject": "TU-JHN-007-014-024", "order": 2,
     "question_de": "«Wenn jemand seinen Willen tun will, wird er … erkennen»: Kommt das Tun vor dem Verstehen?",
     "gsw": {"question_de": "«Wänn öpper sin Wille tue wott, wird er … merke»: Chunnt s Tue vor em Verstaa?"}},
    # TU-JHN-007-025-031
    {"id": "REFL-JHN-0081", "subject": "TU-JHN-007-025-031", "order": 1,
     "question_de": "Die Leute meinen zu wissen, woher Jesus ist: Was übersehen sie damit?",
     "note_de": "«Von diesem wissen wir, woher er ist; wenn aber der Christus kommt, weiss niemand, woher er ist» ([[JHN.7.27]]).",
     "gsw": {"question_de": "D Lüüt meined, si wüssed, wohär de Jesus isch: Was übersehnd si dermit?", "note_de": "«Vo däm wüssed mer, wohär er isch; wänn aber de Christus chunnt, weiss niemer, wohär er isch» ([[JHN.7.27]])."}},
    {"id": "REFL-JHN-0082", "subject": "TU-JHN-007-025-031", "order": 2,
     "question_de": "Niemand legt Hand an ihn, «weil seine Stunde noch nicht gekommen war»: Wer bestimmt hier den Lauf?",
     "gsw": {"question_de": "Niemer leit Hand an en, «wil sini Stund no nöd choo isch»: Wer bestimmt da de Lauf?"}},
    # TU-JHN-007-032-036
    {"id": "REFL-JHN-0083", "subject": "TU-JHN-007-032-036", "order": 1,
     "question_de": "«Ihr werdet mich suchen und nicht finden»: Wie hört sich das für die an, die ihn festnehmen sollen?",
     "note_de": "Die Hohepriester und Pharisäer haben Diener ausgesandt ([[JHN.7.32-JHN.7.34]]).",
     "gsw": {"question_de": "«Ir wärded mich sueche und nöd finde»: Wie tönt das für die, wo-n-en söled feschtnää?", "note_de": "D Hohepriester und d Pharisäer händ Diener usgschickt ([[JHN.7.32-JHN.7.34]])."}},
    {"id": "REFL-JHN-0084", "subject": "TU-JHN-007-032-036", "order": 2,
     "question_de": "Die Zuhörer rätseln, ob er zu den Griechen gehen will: Liegen sie ganz falsch?",
     "gsw": {"question_de": "D Zuehörer rätsled, öb er zu de Grieche wott: Liged si ganz falsch?"}},
    # TU-JHN-007-037-044
    {"id": "REFL-JHN-0085", "subject": "TU-JHN-007-037-044", "order": 1,
     "question_de": "Was bedeutet der Ruf «Wenn jemand Durst hat» am letzten Tag eines Festes?",
     "note_de": "Jesus ruft am letzten, grossen Tag des Laubhüttenfestes ([[JHN.7.2]], [[JHN.7.37]]).",
     "gsw": {"question_de": "Was bedüütet de Ruef «Wänn öpper Durscht hät» am letschte Tag vo me Fäscht?", "note_de": "De Jesus rüeft am letschte, grosse Tag vom Laubhüttefäscht ([[JHN.7.2]], [[JHN.7.37]])."}},
    {"id": "REFL-JHN-0086", "subject": "TU-JHN-007-037-044", "order": 2,
     "question_de": "Die Menge spaltet sich an Jesus: Ist Streit über ihn ein schlechtes Zeichen?",
     "gsw": {"question_de": "D Mängi spaltet sich am Jesus: Isch Striit über ihn es schlächts Zeiche?"}},
    # TU-JHN-007-045-052
    {"id": "REFL-JHN-0087", "subject": "TU-JHN-007-045-052", "order": 1,
     "question_de": "Was hat die Diener so beeindruckt, dass sie ohne Jesus zurückkommen?",
     "note_de": "«Noch nie hat ein Mensch so geredet» ([[JHN.7.46]]).",
     "gsw": {"question_de": "Was hät d Diener so beiidruckt, dass si ohni de Jesus zruggchömed?", "note_de": "«No nie hät en Mänsch eso gredt» ([[JHN.7.46]])."}},
    {"id": "REFL-JHN-0088", "subject": "TU-JHN-007-045-052", "order": 2,
     "question_de": "Nikodemus beruft sich auf das Gesetz, um fair zu bleiben: Was kostet ihn das?",
     "gsw": {"question_de": "De Nikodemus beruefft sich uf s Gsetz, zum fair bliibe: Was choschtet ihn das?"}},
    # TU-JHN-007-053-053
    {"id": "REFL-JHN-0089", "subject": "TU-JHN-007-053-053", "order": 1,
     "question_de": "«Und jeder ging in sein Haus»: Was bedeutet es dir, dass dieser Übergang in den ältesten Handschriften fehlt?",
     "note_de": "Mit diesem Vers beginnt der Abschnitt [[JHN.7.53-JHN.8.11]], den die ältesten Handschriften nicht enthalten.",
     "gsw": {"question_de": "«Und jede isch i sis Huus gange»: Was bedüütet s dir, dass dä Übergang i de eltischte Handschrifte fäält?", "note_de": "Mit dem Vers fangt de Abschnitt [[JHN.7.53-JHN.8.11]] aa, wo i de eltischte Handschrifte nöd drin isch."}},
    {"id": "REFL-JHN-0090", "subject": "TU-JHN-007-053-053", "order": 2,
     "question_de": "Was nehmen die Menschen nach einem langen Streittag mit nach Hause?",
     "gsw": {"question_de": "Was nämed d Mänsche nach eme lange Striittag mit hei?"}},
    # SUM-CH-JHN-008
    {"id": "REFL-JHN-0091", "subject": "SUM-CH-JHN-008", "order": 1,
     "question_de": "Am Anfang des Kapitels ist vom ersten Stein die Rede, am Ende heben sie Steine auf: Was hat sich dazwischen verändert?",
     "note_de": "Zuerst geht es um eine Frau ([[JHN.8.7]]), am Ende um Jesus selbst ([[JHN.8.59]]).",
     "gsw": {"question_de": "Am Aafang vom Kapitel isch vom erschte Stei d Red, am Schluss läsed si Stei uf: Was hät sich dezwüsche veränderet?", "note_de": "Zerscht gaat s um e Frau ([[JHN.8.7]]), am Schluss um de Jesus sälber ([[JHN.8.59]])."}},
    # TU-JHN-008-001-011
    {"id": "REFL-JHN-0092", "subject": "TU-JHN-008-001-011", "order": 1,
     "question_de": "Was schreibt Jesus auf die Erde?",
     "note_de": "Der Text sagt es nicht; er erzählt nur, dass Jesus sich bückt und mit dem Finger schreibt ([[JHN.8.6]], [[JHN.8.8]]).",
     "gsw": {"question_de": "Was schriibt de Jesus uf de Bode?", "note_de": "De Text seit s nöd; er verzellt nu, dass de Jesus sich bückt und mit em Finger schriibt ([[JHN.8.6]], [[JHN.8.8]])."}},
    {"id": "REFL-JHN-0093", "subject": "TU-JHN-008-001-011", "order": 2,
     "question_de": "Wo ist der Mann, mit dem die Frau ergriffen wurde?",
     "gsw": {"question_de": "Wo isch de Maa, mit dem d Frau ertappt worde isch?"}},
    {"id": "REFL-JHN-0094", "subject": "TU-JHN-008-001-011", "order": 3,
     "question_de": "Die Ältesten gehen zuerst: Was könnte sie dazu bewegen?",
     "gsw": {"question_de": "Di Eltischte gönd zerscht: Was chönt si derzue bringe?"}},
    # TU-JHN-008-012-020
    {"id": "REFL-JHN-0095", "subject": "TU-JHN-008-012-020", "order": 1,
     "question_de": "«Licht der Welt» – was zeigt Licht, was man sonst nicht sähe?",
     "note_de": "Jesus sagt es im Tempel, bei der Schatzkammer ([[JHN.8.12]], [[JHN.8.20]]).",
     "gsw": {"question_de": "«Liecht vo de Wält» – was zeigt Liecht, wo mer suscht nöd gsäch?", "note_de": "De Jesus seit s im Tämpel, bi de Schatzkammer ([[JHN.8.12]], [[JHN.8.20]])."}},
    {"id": "REFL-JHN-0096", "subject": "TU-JHN-008-012-020", "order": 2,
     "question_de": "Kann jemand für sich selbst Zeuge sein? Was brauchst du, um einem Menschen zu glauben?",
     "gsw": {"question_de": "Chan öpper für sich sälber Züge sii? Was bruuchsch du, zum eme Mänsch glaube?"}},
    # TU-JHN-008-021-030
    {"id": "REFL-JHN-0097", "subject": "TU-JHN-008-021-030", "order": 1,
     "question_de": "«Ich bin von oben»: Was trennt hier die Gesprächspartner – und was verbindet sie noch?",
     "note_de": "«Ihr seid von unten, ich bin von oben; ihr seid aus dieser Welt, ich bin nicht aus dieser Welt» ([[JHN.8.23]]).",
     "gsw": {"question_de": "«Ich bi vo obe»: Was trännt da d Gsprächspartner – und was verbindet si no?", "note_de": "«Ir sind vo unde, ich bi vo obe; ir sind us dere Wält, ich bi nöd us dere Wält» ([[JHN.8.23]])."}},
    {"id": "REFL-JHN-0098", "subject": "TU-JHN-008-021-030", "order": 2,
     "question_de": "Am Ende glauben viele: Was hat sie im Streit überzeugt?",
     "gsw": {"question_de": "Am Schluss glaubed vil: Was hät si im Striit überzüügt?"}},
    # TU-JHN-008-031-047
    {"id": "REFL-JHN-0099", "subject": "TU-JHN-008-031-047", "order": 1,
     "question_de": "«Die Wahrheit wird euch frei machen»: Frei wovon, frei wozu?",
     "note_de": "Jesus sagt es zu Juden, die ihm geglaubt hatten; sie antworten, sie seien nie Sklaven gewesen ([[JHN.8.31-JHN.8.33]]).",
     "gsw": {"question_de": "«D Wahrheit wird eu frei mache»: Frei vo was, frei für was?", "note_de": "De Jesus seit s zu Jude, wo ihm glaubt händ; si antworted, si seied nie Sklave gsii ([[JHN.8.31-JHN.8.33]])."}},
    {"id": "REFL-JHN-0100", "subject": "TU-JHN-008-031-047", "order": 2,
     "question_de": "Der Streit wird hart bis zum Vorwurf, ihr Vater sei der Teufel: Was ändert es am Lesen, dass hier Juden mit dem Juden Jesus streiten?",
     "note_de": "Das Gespräch beginnt mit Juden, «die ihm geglaubt hatten» ([[JHN.8.31]], [[JHN.8.44]]); Jesus selbst wird im Buch «ein Jude» genannt ([[JHN.4.9]]).",
     "gsw": {"question_de": "De Striit wird hert bis zum Vorwurf, ire Vatter seig de Tüüfel: Was änderet s am Läse, dass da Jude mit em Jud Jesus strited?", "note_de": "S Gspröch fangt mit Jude aa, «wo ihm glaubt händ» ([[JHN.8.31]], [[JHN.8.44]]); de Jesus sälber wird im Buech «en Jud» gnännt ([[JHN.4.9]])."}},
    # TU-JHN-008-048-059
    {"id": "REFL-JHN-0101", "subject": "TU-JHN-008-048-059", "order": 1,
     "question_de": "«Bevor Abraham wurde, bin ich» – warum heben sie gerade bei diesem Satz Steine auf?",
     "note_de": "Vorher hatten sie gefragt: «Bist du etwa grösser als unser Vater Abraham?» ([[JHN.8.53]], [[JHN.8.58-JHN.8.59]])",
     "gsw": {"question_de": "«Bevor de Abraham worde isch, bin ich» – wieso läsed si grad bi dem Satz Stei uf?", "note_de": "Vorher händ si gfröget: «Bisch du öppe grösser als üse Vatter Abraham?» ([[JHN.8.53]], [[JHN.8.58-JHN.8.59]])"}},
    {"id": "REFL-JHN-0102", "subject": "TU-JHN-008-048-059", "order": 2,
     "question_de": "Jesus verbirgt sich und geht hinaus: Warum weicht er hier aus?",
     "gsw": {"question_de": "De Jesus versteckt sich und gaat use: Wieso wiicht er da us?"}},
    # SUM-CH-JHN-009
    {"id": "REFL-JHN-0103", "subject": "SUM-CH-JHN-009", "order": 1,
     "question_de": "Am Anfang sieht einer nichts, am Ende sagen andere «Wir sehen»: Wer sieht in diesem Kapitel wirklich?",
     "note_de": "«Damit die nicht Sehenden sehen und die Sehenden blind werden» ([[JHN.9.39]]).",
     "gsw": {"question_de": "Am Aafang gseht eine nüt, am Schluss säged anderi «Mir gsehnd»: Wer gseht i dem Kapitel würkli?", "note_de": "«Demit die, wo nöd gsehnd, gsehnd und die, wo gsehnd, blind wärded» ([[JHN.9.39]])."}},
    # TU-JHN-009-001-012
    {"id": "REFL-JHN-0104", "subject": "TU-JHN-009-001-012", "order": 1,
     "question_de": "Die Jünger fragen nach Schuld, Jesus antwortet mit einem «damit»: Was verschiebt sich da?",
     "note_de": "«Weder dieser hat gesündigt noch seine Eltern, sondern … damit die Werke Gottes an ihm offenbar werden» ([[JHN.9.3]]).",
     "gsw": {"question_de": "D Jünger fröged nach Schuld, de Jesus antwortet mit eme «demit»: Was verschiebt sich da?", "note_de": "«Weder dä hät gsündiget no sini Eltere, sondern … demit d Wärch vo Gott a ihm offebar wärded» ([[JHN.9.3]])."}},
    {"id": "REFL-JHN-0105", "subject": "TU-JHN-009-001-012", "order": 2,
     "question_de": "Die Nachbarn erkennen den Geheilten kaum wieder: Wie viel von einem Menschen sehen wir in seiner Rolle?",
     "gsw": {"question_de": "D Nachbere erchänned de Gheilte chuum wider: Wie vil vo me Mänsch gsehnd mir i sinere Rolle?"}},
    # TU-JHN-009-013-023
    {"id": "REFL-JHN-0106", "subject": "TU-JHN-009-013-023", "order": 1,
     "question_de": "Die Eltern weichen aus: Wie hättest du an ihrer Stelle geantwortet?",
     "note_de": "Sie fürchten, aus der Synagoge ausgeschlossen zu werden ([[JHN.9.22]]).",
     "gsw": {"question_de": "D Eltere wiiched us: Wie hättsch du a irere Stell gantwortet?", "note_de": "Si fürchted, us de Synagoge usgschlosse zwärde ([[JHN.9.22]])."}},
    {"id": "REFL-JHN-0107", "subject": "TU-JHN-009-013-023", "order": 2,
     "question_de": "Die einen sagen «nicht von Gott», die andern «Wie kann ein sündiger Mensch solche Zeichen tun?»: Welche Gründe haben beide Seiten?",
     "gsw": {"question_de": "Di eine säged «nöd vo Gott», di andere «Wie cha en sündige Mänsch settigi Zeiche tue?»: Weli Gründ händ beidi Siite?"}},
    # TU-JHN-009-024-034
    {"id": "REFL-JHN-0108", "subject": "TU-JHN-009-024-034", "order": 1,
     "question_de": "«Eines weiss ich»: Was ist die Stärke einer Antwort, die nicht mehr behauptet, als sie weiss?",
     "note_de": "«Ob er ein Sünder ist, weiss ich nicht; eines weiss ich: dass ich blind war und jetzt sehe» ([[JHN.9.25]]).",
     "gsw": {"question_de": "«Eis weiss ich»: Was isch d Stärchi vo nere Antwort, wo nöd meh bhauptet, als si weiss?", "note_de": "«Öb er en Sünder isch, weiss ich nöd; eis weiss ich: dass ich blind gsii bi und jetzt gsehne» ([[JHN.9.25]])."}},
    {"id": "REFL-JHN-0109", "subject": "TU-JHN-009-024-034", "order": 2,
     "question_de": "Der Mann wird mutiger, je mehr man ihn bedrängt: Woher kommt dieser Mut?",
     "gsw": {"question_de": "De Maa wird muetiger, je meh dass mer en bedrängt: Wohär chunnt dä Muet?"}},
    # TU-JHN-009-035-041
    {"id": "REFL-JHN-0110", "subject": "TU-JHN-009-035-041", "order": 1,
     "question_de": "Jesus sucht den Hinausgeworfenen auf: Was bedeutet das für ihn?",
     "note_de": "«Jesus hörte, dass sie ihn hinausgeworfen hatten, und als er ihn fand …» ([[JHN.9.35]])",
     "gsw": {"question_de": "De Jesus suecht de Usegworfne uf: Was bedüütet das für ihn?", "note_de": "«De Jesus hät ghört, dass si en usegworfe händ, und won er en gfunde hät …» ([[JHN.9.35]])"}},
    {"id": "REFL-JHN-0111", "subject": "TU-JHN-009-035-041", "order": 2,
     "question_de": "«Sind etwa auch wir blind?» – wie stellt man diese Frage ehrlich?",
     "gsw": {"question_de": "«Sind öppe au mir blind?» – wie stellt mer die Frag ehrlich?"}},
    # SUM-CH-JHN-010
    {"id": "REFL-JHN-0112", "subject": "SUM-CH-JHN-010", "order": 1,
     "question_de": "Wie unterscheiden die Schafe die Stimme des Hirten von einer fremden?",
     "note_de": "Sie folgen ihm, weil sie seine Stimme kennen, einem Fremden aber nicht ([[JHN.10.4-JHN.10.5]]).",
     "gsw": {"question_de": "Wie unterscheided d Schaf d Stimm vom Hirt vo nere frömde?", "note_de": "Si folged ihm, wil si sini Stimm känned, eme Frömde aber nöd ([[JHN.10.4-JHN.10.5]])."}},
    # TU-JHN-010-001-006
    {"id": "REFL-JHN-0113", "subject": "TU-JHN-010-001-006", "order": 1,
     "question_de": "Er ruft die Schafe «mit Namen»: Was ändert es, beim Namen gerufen zu werden?",
     "note_de": "Die Schafe hören auf seine Stimme, und er führt sie hinaus ([[JHN.10.3]]).",
     "gsw": {"question_de": "Er rüeft d Schaf «bim Name»: Was änderet s, bim Name grüeft zwärde?", "note_de": "D Schaf ghöred uf sini Stimm, und er füert si use ([[JHN.10.3]])."}},
    {"id": "REFL-JHN-0114", "subject": "TU-JHN-010-001-006", "order": 2,
     "question_de": "Die Zuhörer verstehen das Bild nicht: Was macht ein Bildwort schwer?",
     "gsw": {"question_de": "D Zuehörer verstönd s Bild nöd: Was macht es Bildwort schwär?"}},
    # TU-JHN-010-007-018
    {"id": "REFL-JHN-0115", "subject": "TU-JHN-010-007-018", "order": 1,
     "question_de": "Was unterscheidet den guten Hirten vom Lohnarbeiter?",
     "note_de": "Der Lohnarbeiter flieht, wenn der Wolf kommt; der gute Hirte gibt sein Leben für die Schafe ([[JHN.10.11-JHN.10.13]]).",
     "gsw": {"question_de": "Was unterscheidet de guet Hirt vom Lohnarbeiter?", "note_de": "De Lohnarbeiter flüüht, wänn de Wolf chunnt; de guet Hirt git sis Läbe für d Schaf ([[JHN.10.11-JHN.10.13]])."}},
    {"id": "REFL-JHN-0116", "subject": "TU-JHN-010-007-018", "order": 2,
     "question_de": "«Andere Schafe, die nicht aus diesem Hof sind»: An wen mögen die ersten Leser gedacht haben?",
     "gsw": {"question_de": "«Anderi Schaf, wo nöd us däm Hof sind»: A wän händ di erschte Läser ächt dänkt?"}},
    {"id": "REFL-JHN-0117", "subject": "TU-JHN-010-007-018", "order": 3,
     "question_de": "Leben und «Überfluss» – was stellst du dir darunter vor?",
     "gsw": {"question_de": "Läbe und «meh als gnueg» – was stellsch du dir drunder vor?"}},
    # TU-JHN-010-019-021
    {"id": "REFL-JHN-0118", "subject": "TU-JHN-010-019-021", "order": 1,
     "question_de": "Dieselben Worte – und die einen sagen «von Sinnen», die andern nicht: Woran messen sie?",
     "note_de": "Die einen sagen, er habe einen Dämon und sei «von Sinnen»; die anderen verweisen auf den geheilten Blinden ([[JHN.10.20-JHN.10.21]]).",
     "gsw": {"question_de": "Di gliiche Wort – und di eine säged «vo Sinne», di andere nöd: A was mässed si?", "note_de": "Di eine säged, er heig en Dämon und seig «vo Sinne»; di andere verwiised uf de gheilt Blind ([[JHN.10.20-JHN.10.21]])."}},
    {"id": "REFL-JHN-0119", "subject": "TU-JHN-010-019-021", "order": 2,
     "question_de": "Wie gehst du mit Menschen um, die dieselbe Person ganz anders sehen als du?",
     "gsw": {"question_de": "Wie gaasch du mit Mänsche um, wo di gliich Person ganz anders gsehnd als du?"}},
    # TU-JHN-010-022-039
    {"id": "REFL-JHN-0120", "subject": "TU-JHN-010-022-039", "order": 1,
     "question_de": "«Sag es uns offen!» – warum genügt eine klare Antwort hier nicht?",
     "note_de": "Jesus verweist auf seine Werke, die von ihm zeugen ([[JHN.10.24-JHN.10.25]]).",
     "gsw": {"question_de": "«Säg s üs offe!» – wieso längt da e klari Antwort nöd?", "note_de": "De Jesus verwiist uf sini Wärch, wo vo ihm zügged ([[JHN.10.24-JHN.10.25]])."}},
    {"id": "REFL-JHN-0121", "subject": "TU-JHN-010-022-039", "order": 2,
     "question_de": "Was bedeutet es, dass niemand die Schafe «aus meiner Hand reissen» wird?",
     "gsw": {"question_de": "Was bedüütet s, dass niemer d Schaf «us minere Hand riisse» wird?"}},
    # TU-JHN-010-040-042
    {"id": "REFL-JHN-0122", "subject": "TU-JHN-010-040-042", "order": 1,
     "question_de": "Johannes hat kein Zeichen getan – und doch glauben die Leute seinem Wort: Was macht ein Zeugnis glaubwürdig?",
     "note_de": "«Johannes hat zwar kein Zeichen getan, aber alles, was Johannes über diesen gesagt hat, war wahr» ([[JHN.10.41]]).",
     "gsw": {"question_de": "De Johannes hät kei Zeiche gmacht – und glich glaubed d Lüüt sim Wort: Was macht es Zügnis glaubwürdig?", "note_de": "«De Johannes hät zwar kei Zeiche gmacht, aber alles, was de Johannes über dä gseit hät, isch wahr gsii» ([[JHN.10.41]])."}},
    {"id": "REFL-JHN-0123", "subject": "TU-JHN-010-040-042", "order": 2,
     "question_de": "Warum geht Jesus gerade an den Ort zurück, wo Johannes zuerst getauft hatte?",
     "gsw": {"question_de": "Wieso gaat de Jesus grad a de Ort zrugg, wo de Johannes zerscht tauft hät?"}},
    # SUM-CH-JHN-011
    {"id": "REFL-JHN-0124", "subject": "SUM-CH-JHN-011", "order": 1,
     "question_de": "Jesus sagt, die Krankheit führe nicht zum Tod – und als er kommt, liegt Lazarus schon vier Tage im Grab: Wie hält das Kapitel diese Spannung aus?",
     "note_de": "Marta und Maria sagen beide: «Herr, wenn du hier gewesen wärst, wäre mein Bruder nicht gestorben» ([[JHN.11.21]], [[JHN.11.32]]).",
     "gsw": {"question_de": "De Jesus seit, d Chranket füeri nöd zum Tod – und won er chunnt, liit de Lazarus scho vier Täg im Grab: Wie haltet s Kapitel die Spannig us?", "note_de": "D Marta und d Maria säged beidi: «Herr, wänn du da gsii wärsch, wär min Brüeder nöd gstorbe» ([[JHN.11.21]], [[JHN.11.32]])."}},
    # TU-JHN-011-001-016
    {"id": "REFL-JHN-0125", "subject": "TU-JHN-011-001-016", "order": 1,
     "question_de": "Jesus liebt die drei Geschwister – und wartet trotzdem zwei Tage: Wie passt das zusammen?",
     "note_de": "Der Text stellt beides direkt nebeneinander ([[JHN.11.5-JHN.11.6]]).",
     "gsw": {"question_de": "De Jesus hät di drüü Gschwüschterti gärn – und wartet glich zwei Täg: Wie passt das zäme?", "note_de": "De Text stellt beides diräkt näbenand ([[JHN.11.5-JHN.11.6]])."}},
    {"id": "REFL-JHN-0126", "subject": "TU-JHN-011-001-016", "order": 2,
     "question_de": "Thomas will mit Jesus sterben: Ist das Mut, Trotz oder Verzweiflung?",
     "gsw": {"question_de": "De Thomas wott mit em Jesus stärbe: Isch das Muet, Trotz oder Verzwiiflig?"}},
    # TU-JHN-011-017-027
    {"id": "REFL-JHN-0127", "subject": "TU-JHN-011-017-027", "order": 1,
     "question_de": "Marta macht Jesus einen Vorwurf und vertraut ihm im selben Atemzug: Darf beides zugleich sein?",
     "note_de": "«Herr, wenn du hier gewesen wärst, wäre mein Bruder nicht gestorben. Und auch jetzt weiss ich …» ([[JHN.11.21-JHN.11.22]])",
     "gsw": {"question_de": "D Marta macht em Jesus en Vorwurf und vertrout ihm im gliiche Atezug: Törf beides glichziitig sii?", "note_de": "«Herr, wänn du da gsii wärsch, wär min Brüeder nöd gstorbe. Und au jetzt weiss ich …» ([[JHN.11.21-JHN.11.22]])"}},
    {"id": "REFL-JHN-0128", "subject": "TU-JHN-011-017-027", "order": 2,
     "question_de": "«Glaubst du das?» – was würdest du Jesus an Martas Stelle antworten?",
     "gsw": {"question_de": "«Glaubsch das?» – was würdsch du em Jesus a de Marta irere Stell antworte?"}},
    # TU-JHN-011-028-037
    {"id": "REFL-JHN-0129", "subject": "TU-JHN-011-028-037", "order": 1,
     "question_de": "Jesus weint, obwohl er Lazarus gleich auferwecken wird: Was sagt dieses Weinen?",
     "note_de": "Er sieht Maria und die Juden weinen und wird im Geist erschüttert ([[JHN.11.33-JHN.11.35]]).",
     "gsw": {"question_de": "De Jesus brüelet, obwohl er de Lazarus grad uferweckt: Was seit das Brüele?", "note_de": "Er gseht d Maria und d Jude brüele und wird im Geischt erschüttered ([[JHN.11.33-JHN.11.35]])."}},
    {"id": "REFL-JHN-0130", "subject": "TU-JHN-011-028-037", "order": 2,
     "question_de": "Die einen sehen seine Liebe, die andern fragen, warum er nicht früher half: Welche Stimme kennst du?",
     "gsw": {"question_de": "Di eine gsehnd sini Liebi, di andere fröged, wieso er nöd früener ghulfe hät: Weli Stimm kännsch du?"}},
    # TU-JHN-011-038-044
    {"id": "REFL-JHN-0131", "subject": "TU-JHN-011-038-044", "order": 1,
     "question_de": "Lazarus kommt heraus, aber gebunden; andere müssen ihn losbinden: Was bleibt den Menschen zu tun?",
     "note_de": "«Bindet ihn los und lasst ihn gehen!» ([[JHN.11.44]])",
     "gsw": {"question_de": "De Lazarus chunnt use, aber bunde; anderi müend en losbinde: Was bliibt de Mänsche ztue?", "note_de": "«Binded en los und lönd en gaa!» ([[JHN.11.44]])"}},
    {"id": "REFL-JHN-0132", "subject": "TU-JHN-011-038-044", "order": 2,
     "question_de": "Marta warnt: «Er riecht schon»: Wo scheint dir etwas zu weit fort, um noch zu hoffen?",
     "gsw": {"question_de": "D Marta warnt: «Er schmöckt scho»: Wo schiint dir öppis z wiit wäg, zum no hoffe?"}},
    # TU-JHN-011-045-053
    {"id": "REFL-JHN-0133", "subject": "TU-JHN-011-045-053", "order": 1,
     "question_de": "Kajafas spricht nüchtern politisch – und der Erzähler hört darin eine Weissagung: Wie liest du diese doppelte Bedeutung?",
     "note_de": "«… dass es besser für euch ist, dass ein Mensch für das Volk stirbt» ([[JHN.11.50-JHN.11.51]]).",
     "gsw": {"question_de": "De Kajafas redt nüechtern politisch – und de Verzeller ghört drin e Wiissagig: Wie lisisch du die doppleti Bedüütig?", "note_de": "«… dass es besser für eu isch, dass ein Mänsch für s Volk stirbt» ([[JHN.11.50-JHN.11.51]])."}},
    {"id": "REFL-JHN-0134", "subject": "TU-JHN-011-045-053", "order": 2,
     "question_de": "Wovor fürchtet sich der Hohe Rat, und wie sieht die Lage aus seiner Sicht aus?",
     "note_de": "«… und die Römer werden kommen und uns sowohl den Ort als auch die Nation wegnehmen» ([[JHN.11.48]]).",
     "gsw": {"question_de": "Vor was fürcht sich de Hoch Root, und wie gseht d Lag us sinere Sicht us?", "note_de": "«… und d Römer wärded choo und wärded üs de Ort und d Nation wägnää» ([[JHN.11.48]])."}},
    # TU-JHN-011-054-057
    {"id": "REFL-JHN-0135", "subject": "TU-JHN-011-054-057", "order": 1,
     "question_de": "«Dass er gewiss nicht zum Fest kommt?» – was erwarten die Leute, die im Tempel nach ihm fragen?",
     "note_de": "Gleichzeitig ist angeordnet, jeden Hinweis zu melden, damit man ihn festnehmen kann ([[JHN.11.56-JHN.11.57]]).",
     "gsw": {"question_de": "«Dass er sicher nöd as Fäscht chunnt?» – was erwarted d Lüüt, wo im Tämpel nach ihm fröged?", "note_de": "Glichziitig isch aagornet, jede Hiiwiis zmälde, demit mer en chan feschtnää ([[JHN.11.56-JHN.11.57]])."}},
    {"id": "REFL-JHN-0136", "subject": "TU-JHN-011-054-057", "order": 2,
     "question_de": "Jesus zieht sich zurück: Wann ist Rückzug klug?",
     "gsw": {"question_de": "De Jesus zieht sich zrugg: Wänn isch Ruggzug gschiid?"}},
    # SUM-CH-JHN-012
    {"id": "REFL-JHN-0137", "subject": "SUM-CH-JHN-012", "order": 1,
     "question_de": "Salbung, Jubel, Weizenkorn: Wie bereitet dieses Kapitel auf die «Stunde» vor?",
     "note_de": "«Gekommen ist die Stunde, dass der Menschensohn verherrlicht wird» ([[JHN.12.23]]).",
     "gsw": {"question_de": "Salbig, Jubel, Weizechorn: Wie bereitet das Kapitel uf d «Stund» vor?", "note_de": "«D Stund isch choo, dass de Mänschesohn verherrlicht wird» ([[JHN.12.23]])."}},
    # TU-JHN-012-001-011
    {"id": "REFL-JHN-0138", "subject": "TU-JHN-012-001-011", "order": 1,
     "question_de": "Maria schenkt etwas sehr Kostbares, Judas rechnet nach: Wie misst man, was eine Geste wert ist?",
     "note_de": "Judas nennt dreihundert Denare ([[JHN.12.5]]).",
     "gsw": {"question_de": "D Maria schänkt öppis sehr Choschtbars, de Judas rächnet nach: Wie misst mer, was e Geschte wärt isch?", "note_de": "De Judas nännt drüühundert Denar ([[JHN.12.5]])."}},
    {"id": "REFL-JHN-0139", "subject": "TU-JHN-012-001-011", "order": 2,
     "question_de": "Das ganze Haus wird vom Duft erfüllt: Was bleibt von einer solchen Tat?",
     "gsw": {"question_de": "S ganz Huus wird vom Duft erfüllt: Was bliibt vo nere söttige Tat?"}},
    # TU-JHN-012-012-019
    {"id": "REFL-JHN-0140", "subject": "TU-JHN-012-012-019", "order": 1,
     "question_de": "Die Menge ruft «König Israels», und Jesus setzt sich auf einen jungen Esel: Was für ein König ist das?",
     "note_de": "Der Erzähler zitiert: «Siehe, dein König kommt, er sitzt auf dem Fohlen eines Esels» ([[JHN.12.15]]).",
     "gsw": {"question_de": "D Mängi rüeft «König vo Israel», und de Jesus setzt sich uf es Eseli: Was isch das für en König?", "note_de": "De Verzeller zitiert: «Lueg, din König chunnt, er sitzt uf em Füli vo me Esel» ([[JHN.12.15]])."}},
    {"id": "REFL-JHN-0141", "subject": "TU-JHN-012-012-019", "order": 2,
     "question_de": "Die Jünger verstehen es erst später: Was hast du erst im Nachhinein verstanden?",
     "gsw": {"question_de": "D Jünger verstönd s erscht spöter: Was häsch du erscht im Nachhinein verstande?"}},
    # TU-JHN-012-020-036
    {"id": "REFL-JHN-0142", "subject": "TU-JHN-012-020-036", "order": 1,
     "question_de": "Griechen möchten Jesus sehen, und er spricht vom Weizenkorn: Ist das eine Antwort auf ihre Bitte?",
     "note_de": "«Herr, wir möchten Jesus sehen» ([[JHN.12.21]], [[JHN.12.24]]).",
     "gsw": {"question_de": "Grieche möchted de Jesus gseh, und er redt vom Weizechorn: Isch das e Antwort uf iri Bitt?", "note_de": "«Herr, mir wetted de Jesus gseh» ([[JHN.12.21]], [[JHN.12.24]])."}},
    {"id": "REFL-JHN-0143", "subject": "TU-JHN-012-020-036", "order": 2,
     "question_de": "Jesus ist erschüttert und betet doch nicht um Rettung: Was hörst du in diesem Gebet?",
     "gsw": {"question_de": "De Jesus isch erschüttered und bättet glich nöd um Rettig: Was ghörsch du i dem Gebätt?"}},
    {"id": "REFL-JHN-0144", "subject": "TU-JHN-012-020-036", "order": 3,
     "question_de": "Dieselbe Stimme vom Himmel – die einen hören Donner, die andern einen Engel: Wovon hängt ab, was man hört?",
     "gsw": {"question_de": "Di gliich Stimm vom Himmel – di eine ghöred en Dunner, di andere en Ängel: Vo was hangt s ab, was mer ghört?"}},
    # TU-JHN-012-037-043
    {"id": "REFL-JHN-0145", "subject": "TU-JHN-012-037-043", "order": 1,
     "question_de": "Viele glauben, sagen es aber nicht: Was kostet ein Bekenntnis?",
     "note_de": "Sie fürchten, aus der Synagoge ausgeschlossen zu werden ([[JHN.12.42]]).",
     "gsw": {"question_de": "Vil glaubed, säged s aber nöd: Was choschtet es Bekenntnis?", "note_de": "Si fürchted, us de Synagoge usgschlosse zwärde ([[JHN.12.42]])."}},
    {"id": "REFL-JHN-0146", "subject": "TU-JHN-012-037-043", "order": 2,
     "question_de": "Wie gehst du mit der Erklärung um, dass Unglaube «erfüllt», was Jesaja sagte?",
     "gsw": {"question_de": "Wie gaasch du mit de Erklärig um, dass de Unglaube erfüllt, was de Jesaja gseit hät?"}},
    # TU-JHN-012-044-050
    {"id": "REFL-JHN-0147", "subject": "TU-JHN-012-044-050", "order": 1,
     "question_de": "«nicht gekommen, um die Welt zu richten, sondern um die Welt zu retten» – und doch gibt es ein Gericht: Wie verträgt sich das?",
     "note_de": "Das Wort selbst richtet am letzten Tag ([[JHN.12.47-JHN.12.48]]).",
     "gsw": {"question_de": "«nöd choo, zum d Wält richte, sondern zum d Wält rette» – und glich gits es Gricht: Wie vertreit sich das?", "note_de": "S Wort sälber richtet am letschte Tag ([[JHN.12.47-JHN.12.48]])."}},
    {"id": "REFL-JHN-0148", "subject": "TU-JHN-012-044-050", "order": 2,
     "question_de": "Wer Jesus sieht, sieht den, der ihn gesandt hat: Was heisst das für das Bild, das du von Gott hast?",
     "gsw": {"question_de": "Wer de Jesus gseht, gseht dä, won en gschickt hät: Was heisst das für s Bild, wo d vo Gott häsch?"}},
    # SUM-CH-JHN-013
    {"id": "REFL-JHN-0149", "subject": "SUM-CH-JHN-013", "order": 1,
     "question_de": "Liebe «bis zur Vollendung» – und doch sitzt einer am Tisch, der ihn ausliefern wird: Was zeigt das über diese Liebe?",
     "note_de": "Beides steht gleich am Anfang des Kapitels ([[JHN.13.1-JHN.13.2]]).",
     "gsw": {"question_de": "Liebi «bis zur Vollendig» – und glich sitzt eine am Tisch, won en usliefere wird: Was zeigt das über die Liebi?", "note_de": "Beides staat grad am Aafang vom Kapitel ([[JHN.13.1-JHN.13.2]])."}},
    # TU-JHN-013-001-011
    {"id": "REFL-JHN-0150", "subject": "TU-JHN-013-001-011", "order": 1,
     "question_de": "Warum wehrt sich Petrus dagegen, dass Jesus ihm die Füsse wäscht?",
     "note_de": "«Nie in Ewigkeit sollst du mir die Füsse waschen!» ([[JHN.13.8]])",
     "gsw": {"question_de": "Wieso wehrt sich de Petrus degäge, dass ihm de Jesus d Füess wäscht?", "note_de": "«Nie im Läbe wäschisch du mir d Füess!» ([[JHN.13.8]])"}},
    {"id": "REFL-JHN-0151", "subject": "TU-JHN-013-001-011", "order": 2,
     "question_de": "Jesus weiss, wer ihn ausliefern wird, und wäscht doch den Jüngern die Füsse: Was bedeutet das für dich?",
     "note_de": "«Er kannte nämlich den, der ihn ausliefert» ([[JHN.13.5]], [[JHN.13.11]]).",
     "gsw": {"question_de": "De Jesus weiss, wer en usliferet, und wäscht glich de Jünger d Füess: Was bedüütet das für dich?", "note_de": "«Er hät nämli dä kännt, wo en usliferet» ([[JHN.13.5]], [[JHN.13.11]])."}},
    {"id": "REFL-JHN-0152", "subject": "TU-JHN-013-001-011", "order": 3,
     "question_de": "Fällt es dir leichter, anderen zu dienen, oder dir dienen zu lassen?",
     "gsw": {"question_de": "Fallt s dir liechter, andere zdiene, oder dir la zdiene?"}},
    # TU-JHN-013-012-020
    {"id": "REFL-JHN-0153", "subject": "TU-JHN-013-012-020", "order": 1,
     "question_de": "«Versteht ihr, was ich euch getan habe?» – was hätten die Jünger antworten können?",
     "note_de": "Jesus stellt die Frage, nachdem er sich wieder zu Tisch gelegt hat ([[JHN.13.12]]).",
     "gsw": {"question_de": "«Verstönd ir, was ich eu gmacht han?» – was hetted d Jünger chöne antworte?", "note_de": "De Jesus stellt d Frag, won er sich wider an Tisch gleit hät ([[JHN.13.12]])."}},
    {"id": "REFL-JHN-0154", "subject": "TU-JHN-013-012-020", "order": 2,
     "question_de": "Selig, «wenn ihr es tut»: Was ist der Unterschied zwischen wissen und tun?",
     "gsw": {"question_de": "Sälig, «wänn ir s mached»: Was isch de Unterschiid zwüsche wüsse und tue?"}},
    # TU-JHN-013-021-030
    {"id": "REFL-JHN-0155", "subject": "TU-JHN-013-021-030", "order": 1,
     "question_de": "Die Jünger blicken einander ratlos an, und auch nach dem Bissen versteht keiner am Tisch, wozu Jesus Judas das sagt: Was sagt das über Judas – und über die anderen?",
     "note_de": "Die Jünger blicken einander ratlos an ([[JHN.13.22]], [[JHN.13.28]]).",
     "gsw": {"question_de": "D Jünger lueged enand ratlos aa, und au nach em Bisse verstaht kein am Tisch, für was de Jesus em Judas das seit: Was seit das über de Judas – und über di andere?", "note_de": "D Jünger lueged enand ratlos aa ([[JHN.13.22]], [[JHN.13.28]])."}},
    {"id": "REFL-JHN-0156", "subject": "TU-JHN-013-021-030", "order": 2,
     "question_de": "«Es war aber Nacht» – was trägt dieser kurze Satz?",
     "gsw": {"question_de": "«Es isch aber Nacht gsii» – was treit dä churz Satz?"}},
    # TU-JHN-013-031-038
    {"id": "REFL-JHN-0157", "subject": "TU-JHN-013-031-038", "order": 1,
     "question_de": "«Ein neues Gebot gebe ich euch»: Was ist neu daran, einander zu lieben?",
     "note_de": "Jesus fügt hinzu: «Wie ich euch geliebt habe» ([[JHN.13.34]]).",
     "gsw": {"question_de": "«Es nöis Gebot gib ich eu»: Was isch nöi dra, enand z liebe?", "note_de": "De Jesus seit derzue: «Wie ich eu gliebt han» ([[JHN.13.34]])."}},
    {"id": "REFL-JHN-0158", "subject": "TU-JHN-013-031-038", "order": 2,
     "question_de": "Petrus verspricht viel und meint es ernst: Wie geht es dir mit Versprechen, die grösser sind als du?",
     "gsw": {"question_de": "De Petrus verspricht vil und meint s ärnscht: Wie gaat s dir mit Verspräche, wo grösser sind als du?"}},
    # SUM-CH-JHN-014
    {"id": "REFL-JHN-0159", "subject": "SUM-CH-JHN-014", "order": 1,
     "question_de": "Jesus kündigt seinen Weggang an und sagt: «Euer Herz sei nicht erschüttert»: Was soll die Jünger trösten?",
     "note_de": "Er sagt den Satz am Anfang und am Ende des Kapitels ([[JHN.14.1]], [[JHN.14.27]]).",
     "gsw": {"question_de": "De Jesus chündt sin Wäggang aa und seit: «Eues Härz söll nöd erschüttert sii»: Was söll d Jünger tröschte?", "note_de": "Er seit dä Satz am Aafang und am Schluss vom Kapitel ([[JHN.14.1]], [[JHN.14.27]])."}},
    # TU-JHN-014-001-014
    {"id": "REFL-JHN-0160", "subject": "TU-JHN-014-001-014", "order": 1,
     "question_de": "Thomas und Philippus stellen ganz einfache Fragen: Welche einfache Frage würdest du stellen?",
     "note_de": "«Herr, wir wissen nicht, wohin du gehst» – «Herr, zeig uns den Vater» ([[JHN.14.5]], [[JHN.14.8]]).",
     "gsw": {"question_de": "De Thomas und de Philippus stelled ganz eifachi Frage: Weli eifachi Frag würdsch du stelle?", "note_de": "«Herr, mir wüssed nöd, wo du hiigaasch» – «Herr, zeig üs de Vatter» ([[JHN.14.5]], [[JHN.14.8]])."}},
    {"id": "REFL-JHN-0161", "subject": "TU-JHN-014-001-014", "order": 2,
     "question_de": "«Viele Wohnungen» im Haus des Vaters: Was löst dieses Bild aus?",
     "gsw": {"question_de": "«Vil Wonige» im Huus vom Vatter: Was löst das Bild us?"}},
    {"id": "REFL-JHN-0162", "subject": "TU-JHN-014-001-014", "order": 3,
     "question_de": "Der Satz «Niemand kommt zum Vater ausser durch mich» wird sehr verschieden verstanden: Wie hörst du ihn?",
     "gsw": {"question_de": "De Satz «Niemer chunnt zum Vatter usser dur mich» wird sehr verschide verstande: Wie ghörsch du ihn?"}},
    # TU-JHN-014-015-026
    {"id": "REFL-JHN-0163", "subject": "TU-JHN-014-015-026", "order": 1,
     "question_de": "«Ich werde euch nicht als Waisen zurücklassen»: Wann fühlt man sich verwaist?",
     "note_de": "Jesus sagt es im Zusammenhang mit dem Beistand, den der Vater geben wird ([[JHN.14.16-JHN.14.18]]).",
     "gsw": {"question_de": "«Ich laa eu nöd als Waise zrugg»: Wänn fühlt mer sich verwaist?", "note_de": "De Jesus seit s im Zämehang mit em Biistand, wo de Vatter wird gää ([[JHN.14.16-JHN.14.18]])."}},
    {"id": "REFL-JHN-0164", "subject": "TU-JHN-014-015-026", "order": 2,
     "question_de": "Lieben und Halten werden hier verbunden: Kann man Liebe an Taten messen?",
     "gsw": {"question_de": "Liebi und Halte wärded da verbunde: Chan mer Liebi a Täte mässe?"}},
    # TU-JHN-014-027-031
    {"id": "REFL-JHN-0165", "subject": "TU-JHN-014-027-031", "order": 1,
     "question_de": "Was unterscheidet den Frieden, den Jesus gibt, von dem, den die Welt gibt?",
     "note_de": "«Nicht wie die Welt gibt, gebe ich euch» ([[JHN.14.27]]).",
     "gsw": {"question_de": "Was unterscheidet de Fride, wo de Jesus git, vo dem, wo d Wält git?", "note_de": "«Nöd wie d Wält git, gib ich eu» ([[JHN.14.27]])."}},
    {"id": "REFL-JHN-0166", "subject": "TU-JHN-014-027-031", "order": 2,
     "question_de": "«Steht auf, lasst uns von hier gehen!» – wohin führt dieser Aufbruch?",
     "gsw": {"question_de": "«Stönd uf, mir gönd vo da furt!» – wohi füert dä Ufbruch?"}},
    # SUM-CH-JHN-015
    {"id": "REFL-JHN-0167", "subject": "SUM-CH-JHN-015", "order": 1,
     "question_de": "Bleiben ist das Leitwort dieses Kapitels: Was heisst es, in einer Beziehung zu bleiben?",
     "note_de": "«Bleibt in mir» – «Bleibt in meiner Liebe!» ([[JHN.15.4]], [[JHN.15.9]])",
     "gsw": {"question_de": "Bliibe isch s Leitwort vo dem Kapitel: Was heisst s, i nere Beziehig zbliibe?", "note_de": "«Bliibed in mir» – «Bliibed i minere Liebi!» ([[JHN.15.4]], [[JHN.15.9]])"}},
    # TU-JHN-015-001-008
    {"id": "REFL-JHN-0168", "subject": "TU-JHN-015-001-008", "order": 1,
     "question_de": "Was erfährt die Rebe vom Weinstock, was sie allein nicht hätte?",
     "note_de": "«Ohne mich könnt ihr nichts tun» ([[JHN.15.5]]).",
     "gsw": {"question_de": "Was überchunnt de Schoss vom Wiistock, won er elei nöd hett?", "note_de": "«Ohni mich chönd ir nüüt mache» ([[JHN.15.5]])."}},
    {"id": "REFL-JHN-0169", "subject": "TU-JHN-015-001-008", "order": 2,
     "question_de": "Der Weingärtner reinigt auch die Reben, die Frucht bringen: Wie klingt das für dich?",
     "gsw": {"question_de": "De Wiibuur macht au d Schoss suuber, wo Frucht bringed: Wie tönt das für dich?"}},
    # TU-JHN-015-009-017
    {"id": "REFL-JHN-0170", "subject": "TU-JHN-015-009-017", "order": 1,
     "question_de": "Was ändert es, nicht mehr Knecht, sondern Freund genannt zu werden?",
     "note_de": "«Ich nenne euch nicht mehr Knechte … euch aber habe ich Freunde genannt» ([[JHN.15.15]]).",
     "gsw": {"question_de": "Was änderet s, nüme Chnächt, sondern Fründ gnännt zwärde?", "note_de": "«Ich säg eu nüme Chnächt … Eu aber han ich Fründe gseit» ([[JHN.15.15]])."}},
    {"id": "REFL-JHN-0171", "subject": "TU-JHN-015-009-017", "order": 2,
     "question_de": "Liebe als Gebot – geht das?",
     "gsw": {"question_de": "Liebi als Gebot – gaat das?"}},
    # TU-JHN-015-018-027
    {"id": "REFL-JHN-0172", "subject": "TU-JHN-015-018-027", "order": 1,
     "question_de": "Die Jünger sollen mit Hass rechnen: Wie hören das Menschen, die tatsächlich verfolgt werden – und wie die, die es nicht werden?",
     "note_de": "«Wenn die Welt euch hasst, so wisst, dass sie mich vor euch gehasst hat» ([[JHN.15.18]]).",
     "gsw": {"question_de": "D Jünger söled mit Hass rächne: Wie ghöred das Mänsche, wo würkli verfolgt wärded – und wie die, wo s nöd wärded?", "note_de": "«Wänn d Wält eu hasst, dänn wüssed, dass si mich vor eu ghasst hät» ([[JHN.15.18]])."}},
    {"id": "REFL-JHN-0173", "subject": "TU-JHN-015-018-027", "order": 2,
     "question_de": "Der Geist legt Zeugnis ab «und auch ihr»: Was ist das Eigene am Zeugnis der Jünger?",
     "gsw": {"question_de": "De Geischt leit Zügnis ab «und au ir»: Was isch s Eigete am Zügnis vo de Jünger?"}},
    # SUM-CH-JHN-016
    {"id": "REFL-JHN-0174", "subject": "SUM-CH-JHN-016", "order": 1,
     "question_de": "Jesus sagt den Jüngern Schweres im Voraus: Hilft es, Schweres vorher zu wissen?",
     "note_de": "«Das habe ich zu euch gesagt, damit ihr nicht zu Fall kommt» ([[JHN.16.1]]).",
     "gsw": {"question_de": "De Jesus seit de Jünger Schwärs im Voruus: Hilft s, Schwärs vorher zwüsse?", "note_de": "«Das han ich eu gseit, demit ir nöd z Fall chömed» ([[JHN.16.1]])."}},
    # TU-JHN-016-001-004
    {"id": "REFL-JHN-0175", "subject": "TU-JHN-016-001-004", "order": 1,
     "question_de": "Wie kann jemand meinen, Gott zu dienen, wenn er andere verfolgt?",
     "note_de": "Jesus sagt es voraus und nennt den Grund: «weil sie weder den Vater noch mich erkannt haben» ([[JHN.16.2-JHN.16.3]]).",
     "gsw": {"question_de": "Wie chan öpper meine, er dieni Gott, wänn er anderi verfolgt?", "note_de": "De Jesus seit s voruus und nännt de Grund: «wil si weder de Vatter no mich erchännt händ» ([[JHN.16.2-JHN.16.3]])."}},
    {"id": "REFL-JHN-0176", "subject": "TU-JHN-016-001-004", "order": 2,
     "question_de": "Jesus kündigt an, man werde die Jünger aus der Synagoge ausschliessen: Wie klingt dieser Satz für die Ausgeschlossenen, und wie aus der Sicht der Synagoge?",
     "note_de": "Manche Forschende sehen darin Erfahrungen der ersten Leser, andere halten das für unsicher ([[JHN.16.2]]).",
     "gsw": {"question_de": "De Jesus chündt aa, mer wärdi d Jünger us de Synagoge usschlüüsse: Wie tönt dä Satz für die, wo usgschlosse wärded, und wie us de Sicht vo de Synagoge?", "note_de": "Es paar Forschendi gsehnd drin Erfahrige vo de erschte Läser, anderi haltet das für unsicher ([[JHN.16.2]])."}},
    # TU-JHN-016-005-015
    {"id": "REFL-JHN-0177", "subject": "TU-JHN-016-005-015", "order": 1,
     "question_de": "«Es ist gut für euch, dass ich weggehe» – wie kann ein Abschied gut sein?",
     "note_de": "Sonst, sagt Jesus, kommt der Beistand nicht ([[JHN.16.7]]).",
     "gsw": {"question_de": "«Es isch guet für eu, dass ich wäggang» – wie chan en Abschiid guet sii?", "note_de": "Suscht, seit de Jesus, chunnt de Biistand nöd ([[JHN.16.7]])."}},
    {"id": "REFL-JHN-0178", "subject": "TU-JHN-016-005-015", "order": 2,
     "question_de": "«Noch vieles habe ich euch zu sagen, aber ihr könnt es jetzt nicht tragen»: Was braucht Zeit, bis man es tragen kann?",
     "gsw": {"question_de": "«No vil han ich eu z säge, aber ir chönd s jetzt nöd träge»: Was bruucht Ziit, bis mer s chan träge?"}},
    # TU-JHN-016-016-024
    {"id": "REFL-JHN-0179", "subject": "TU-JHN-016-016-024", "order": 1,
     "question_de": "Warum wählt Jesus das Bild einer Frau, die gebiert?",
     "note_de": "Ihr Schmerz geht in Freude über, weil ein Mensch zur Welt gekommen ist ([[JHN.16.21]]).",
     "gsw": {"question_de": "Wieso wählt de Jesus s Bild vo nere Frau, wo es Chind überchunnt?", "note_de": "Ire Schmärz gaat i Fröid über, wil en Mänsch uf d Wält choo isch ([[JHN.16.21]])."}},
    {"id": "REFL-JHN-0180", "subject": "TU-JHN-016-016-024", "order": 2,
     "question_de": "«Eure Freude nimmt niemand von euch»: Gibt es so etwas?",
     "gsw": {"question_de": "«Eui Fröid nimmt niemer vo eu wäg»: Git s öppis Söttigs?"}},
    # TU-JHN-016-025-033
    {"id": "REFL-JHN-0181", "subject": "TU-JHN-016-025-033", "order": 1,
     "question_de": "Die Jünger sagen «Darum glauben wir», und Jesus kündigt an, dass sie ihn allein lassen: Wie passt das zusammen?",
     "note_de": "«Siehe, es kommt die Stunde … dass ihr zerstreut werdet … und mich allein lasst» ([[JHN.16.30-JHN.16.32]]).",
     "gsw": {"question_de": "D Jünger säged «Drum glaubed mir», und de Jesus chündt aa, dass si en elei lönd: Wie passt das zäme?", "note_de": "«Lueg, es chunnt d Stund … wo ir verstreut wärded … und mich elei lönd» ([[JHN.16.30-JHN.16.32]])."}},
    {"id": "REFL-JHN-0182", "subject": "TU-JHN-016-025-033", "order": 2,
     "question_de": "«In der Welt habt ihr Bedrängnis; aber seid getrost»: Was macht diesen Trost glaubwürdig – oder nicht?",
     "gsw": {"question_de": "«I de Wält händ ir Not; aber händ Muet»: Was macht dä Troscht glaubwürdig – oder nöd?"}},
    # SUM-CH-JHN-017
    {"id": "REFL-JHN-0183", "subject": "SUM-CH-JHN-017", "order": 1,
     "question_de": "Jesus betet für sich, für die Jünger und für spätere Glaubende: Für wen würdest du – im Gebet oder in Gedanken – so eintreten?",
     "note_de": "Der Kreis weitet sich: «Ich bitte aber nicht nur für diese, sondern auch für die, die durch ihr Wort an mich glauben» ([[JHN.17.20]]).",
     "gsw": {"question_de": "De Jesus bättet für sich, für d Jünger und für spöteri Glaubendi: Für wän würdsch du – im Gebätt oder i Gedanke – eso iiträte?", "note_de": "De Chreis wird wiiter: «Ich bitte aber nöd nu für die, sondern au für die, wo dur ires Wort a mich glaubed» ([[JHN.17.20]])."}},
    # TU-JHN-017-001-005
    {"id": "REFL-JHN-0184", "subject": "TU-JHN-017-001-005", "order": 1,
     "question_de": "«Das aber ist das ewige Leben: dass sie dich … erkennen» – ist ewiges Leben hier eine Zeitdauer oder eine Beziehung?",
     "note_de": "So bestimmt Jesus im Gebet, was ewiges Leben ist ([[JHN.17.3]]).",
     "gsw": {"question_de": "«Das aber isch s ewig Läbe: dass si dich … erchänned» – isch ewigs Läbe da e Ziitduur oder e Beziehig?", "note_de": "So bestimmt de Jesus im Gebätt, was ewigs Läbe isch ([[JHN.17.3]])."}},
    {"id": "REFL-JHN-0185", "subject": "TU-JHN-017-001-005", "order": 2,
     "question_de": "Bei welcher Aufgabe in deinem Leben möchtest du am Ende sagen können, sie sei vollendet?",
     "note_de": "Jesus betet: «… indem ich das Werk vollendet habe, das du mir gegeben hast» ([[JHN.17.4]]).",
     "gsw": {"question_de": "Bi welere Ufgab i dim Läbe möchtisch du am Schluss chöne säge, si seig volländet?", "note_de": "De Jesus bättet: «… indem ich s Wärch volländet han, wo du mir gää häsch» ([[JHN.17.4]])."}},
    # TU-JHN-017-006-019
    {"id": "REFL-JHN-0186", "subject": "TU-JHN-017-006-019", "order": 1,
     "question_de": "Jesus bittet nicht, die Jünger aus der Welt zu nehmen, sondern sie zu bewahren: Warum nicht?",
     "note_de": "«Ich bitte nicht, dass du sie aus der Welt wegnimmst, sondern dass du sie vor dem Bösen bewahrst» ([[JHN.17.15]]).",
     "gsw": {"question_de": "De Jesus bittet nöd, d Jünger us de Wält znää, sondern si zbewahre: Wieso nöd?", "note_de": "«Ich bitte nöd, dass du si us de Wält wägnimmsch, sondern dass du si vor em Böse bhüetisch» ([[JHN.17.15]])."}},
    {"id": "REFL-JHN-0187", "subject": "TU-JHN-017-006-019", "order": 2,
     "question_de": "Wen möchtest du bewahrt wissen – und wovor?",
     "gsw": {"question_de": "Wän möchtisch du bhüetet wüsse – und vor was?"}},
    # TU-JHN-017-020-026
    {"id": "REFL-JHN-0188", "subject": "TU-JHN-017-020-026", "order": 1,
     "question_de": "«Damit alle eins sind» – was hiesse Einheit unter Menschen, die verschieden glauben?",
     "note_de": "Jesus bittet um Einheit, «damit die Welt glaubt» ([[JHN.17.21]]).",
     "gsw": {"question_de": "«Demit alli eis sind» – was hiess Einheit under Mänsche, wo verschide glaubed?", "note_de": "De Jesus bittet um Einheit, «demit d Wält glaubt» ([[JHN.17.21]])."}},
    {"id": "REFL-JHN-0189", "subject": "TU-JHN-017-020-026", "order": 2,
     "question_de": "Jesus bittet auch für die, die später glauben werden: Welcher Satz dieses Gebets spricht dich an, welcher bleibt dir fremd?",
     "gsw": {"question_de": "De Jesus bittet au für die, wo spöter glaubed: Wele Satz vo dem Gebätt redt dich aa, wele bliibt dir frömd?"}},
    # SUM-CH-JHN-018
    {"id": "REFL-JHN-0190", "subject": "SUM-CH-JHN-018", "order": 1,
     "question_de": "Jesus sagt «Ich bin es», Petrus «Ich bin es nicht»: Was zeigt dieser Gegensatz?",
     "note_de": "Beide Sätze fallen in derselben Nacht ([[JHN.18.5]], [[JHN.18.17]], [[JHN.18.25]]).",
     "gsw": {"question_de": "De Jesus seit «Ich bi s», de Petrus «Ich bi s nöd»: Was zeigt dä Gägesatz?", "note_de": "Beid Sätz fallet i de gliiche Nacht ([[JHN.18.5]], [[JHN.18.17]], [[JHN.18.25]])."}},
    # TU-JHN-018-001-011
    {"id": "REFL-JHN-0191", "subject": "TU-JHN-018-001-011", "order": 1,
     "question_de": "Jesus geht den Häschern entgegen und fragt: «Wen sucht ihr?» Wer hat hier die Initiative?",
     "note_de": "Sie kommen mit Laternen, Fackeln und Waffen; er geht hinaus ([[JHN.18.3-JHN.18.4]]).",
     "gsw": {"question_de": "De Jesus gaat de Häscher entgäge und fröget: «Wän sueched ir?» Wer hät da d Initiative?", "note_de": "Si chömed mit Laterne, Fackle und Waffe; er gaat use ([[JHN.18.3-JHN.18.4]])."}},
    {"id": "REFL-JHN-0192", "subject": "TU-JHN-018-001-011", "order": 2,
     "question_de": "Petrus greift zum Schwert, um ihn zu schützen: Was hält Jesus davon ab, sich verteidigen zu lassen?",
     "gsw": {"question_de": "De Petrus griift zum Schwärt, zum en schütze: Was hebt de Jesus devo ab, sich la zverteidige?"}},
    # TU-JHN-018-012-014
    {"id": "REFL-JHN-0193", "subject": "TU-JHN-018-012-014", "order": 1,
     "question_de": "Warum erinnert der Erzähler gerade hier an den Rat des Kajafas?",
     "note_de": "Kajafas hatte geraten, es sei besser, dass ein Mensch für das Volk sterbe ([[JHN.18.14]], [[JHN.11.50]]).",
     "gsw": {"question_de": "Wieso erinneret de Verzeller grad da a de Rat vom Kajafas?", "note_de": "De Kajafas hät groote, es seig besser, dass ein Mänsch für s Volk stärbi ([[JHN.18.14]], [[JHN.11.50]])."}},
    {"id": "REFL-JHN-0194", "subject": "TU-JHN-018-012-014", "order": 2,
     "question_de": "Jesus wird gefesselt: Wie wirkt dieses Bild nach den Worten «Niemand nimmt es mir weg» ([[JHN.10.18]])?",
     "gsw": {"question_de": "De Jesus wird gfesslet: Wie würkt das Bild nach de Wort «Niemer nimmt mir s wäg» ([[JHN.10.18]])?"}},
    # TU-JHN-018-015-018
    {"id": "REFL-JHN-0195", "subject": "TU-JHN-018-015-018", "order": 1,
     "question_de": "Petrus steht beim Feuer der anderen und wärmt sich: Wo stehst du, wenn es kalt wird?",
     "note_de": "Knechte und Diener haben ein Kohlenfeuer gemacht, weil es kalt ist ([[JHN.18.18]]).",
     "gsw": {"question_de": "De Petrus staat bim Füür vo de andere und wärmt sich: Wo staasch du, wänn s chalt wird?", "note_de": "Chnächt und Diener händ es Cholefüür gmacht, wil s chalt isch ([[JHN.18.18]])."}},
    {"id": "REFL-JHN-0196", "subject": "TU-JHN-018-015-018", "order": 2,
     "question_de": "Die Magd fragt nur: «Bist du etwa auch einer der Jünger dieses Menschen?» Warum fällt die Antwort so aus?",
     "gsw": {"question_de": "D Magd frögt nu: «Bisch du öppe au eine vo de Jünger vo däm Mänsch?» Wieso fallt d Antwort eso us?"}},
    # TU-JHN-018-019-024
    {"id": "REFL-JHN-0197", "subject": "TU-JHN-018-019-024", "order": 1,
     "question_de": "«Wenn aber recht, warum schlägst du mich?» – wie widersteht Jesus hier?",
     "note_de": "Ein Diener schlägt ihn ins Gesicht, weil er dem Hohepriester so geantwortet hat ([[JHN.18.22-JHN.18.23]]).",
     "gsw": {"question_de": "«Wänn aber rächt, werum schlaasch mich?» – wie widerstaat de Jesus da?", "note_de": "En Diener schlaat en is Gsicht, wil er em Hohepriester eso gantwortet hät ([[JHN.18.22-JHN.18.23]])."}},
    {"id": "REFL-JHN-0198", "subject": "TU-JHN-018-019-024", "order": 2,
     "question_de": "Jesus verweist auf die, die ihn gehört haben: Wer könnte heute über dein Reden Auskunft geben?",
     "gsw": {"question_de": "De Jesus verwiist uf die, won en ghört händ: Wer chönt hüt über dis Rede Uskunft gää?"}},
    # TU-JHN-018-025-027
    {"id": "REFL-JHN-0199", "subject": "TU-JHN-018-025-027", "order": 1,
     "question_de": "Der Hahn kräht, und der Text schweigt über Petrus: Was mag in ihm vorgehen?",
     "note_de": "Anders als andere Evangelien erzählt Johannes hier nicht, dass Petrus weint ([[JHN.18.27]]).",
     "gsw": {"question_de": "De Güggel chräiht, und de Text schwiigt über de Petrus: Was gaat ächt i ihm vor?", "note_de": "Anders als anderi Evangelie verzellt de Johannes da nöd, dass de Petrus brüelet ([[JHN.18.27]])."}},
    {"id": "REFL-JHN-0200", "subject": "TU-JHN-018-025-027", "order": 2,
     "question_de": "Ein Verwandter des Malchus erkennt ihn: Holt die Vergangenheit Petrus ein?",
     "gsw": {"question_de": "En Verwandte vom Malchus erchännt en: Holt d Vergangeheit de Petrus ii?"}},
    # TU-JHN-018-028-032
    {"id": "REFL-JHN-0201", "subject": "TU-JHN-018-028-032", "order": 1,
     "question_de": "Sie bleiben vor dem Prätorium, um das Passa essen zu können: Warum erzählt der Text dieses Detail gerade hier?",
     "note_de": "Sie gehen nicht ins Prätorium, «um nicht unrein zu werden, sondern das Passa essen zu können» ([[JHN.18.28]]).",
     "gsw": {"question_de": "Si bliibed vor em Prätorium, demit si s Passa chönd ässe: Wieso verzellt de Text das Detail grad da?", "note_de": "Si gönd nöd is Prätorium, «demit si nöd unrein wärded, sondern s Passa chönd ässe» ([[JHN.18.28]])."}},
    {"id": "REFL-JHN-0202", "subject": "TU-JHN-018-028-032", "order": 2,
     "question_de": "Wie sieht die Lage aus der Sicht des Pilatus aus?",
     "note_de": "Zuerst will er den Fall abgeben: «Nehmt ihr ihn und richtet ihn nach eurem Gesetz!» ([[JHN.18.31]])",
     "gsw": {"question_de": "Wie gseht d Lag us de Sicht vom Pilatus us?", "note_de": "Zerscht wott er de Fall abgää: «Nämed ir en und richted en nach euem Gsetz!» ([[JHN.18.31]])"}},
    # TU-JHN-018-033-038
    {"id": "REFL-JHN-0203", "subject": "TU-JHN-018-033-038", "order": 1,
     "question_de": "«Was ist Wahrheit?» – fragt Pilatus spöttisch, müde oder ernsthaft?",
     "note_de": "Er geht nach der Frage hinaus, ohne eine Antwort abzuwarten ([[JHN.18.38]]).",
     "gsw": {"question_de": "«Was isch Wahrheit?» – fröget de Pilatus spöttisch, müed oder ärnschthaft?", "note_de": "Er gaat nach de Frag use, ohni e Antwort abzwarte ([[JHN.18.38]])."}},
    {"id": "REFL-JHN-0204", "subject": "TU-JHN-018-033-038", "order": 2,
     "question_de": "Ein Reich, das «nicht aus dieser Welt» ist: Heisst das, es hat mit dieser Welt nichts zu tun?",
     "gsw": {"question_de": "Es Riich, wo «nöd us dere Wält» isch: Heisst das, es hät mit dere Wält nüt ztue?"}},
    # TU-JHN-018-039-040
    {"id": "REFL-JHN-0205", "subject": "TU-JHN-018-039-040", "order": 1,
     "question_de": "Barabbas statt Jesus: Was sagt diese Wahl über die Stimmung des Augenblicks?",
     "note_de": "«Barabbas aber war ein Räuber» – mit diesem knappen Satz endet das Kapitel ([[JHN.18.40]]).",
     "gsw": {"question_de": "De Barabbas statt de Jesus: Was seit die Wahl über d Stimmig vom Augeblick?", "note_de": "«De Barabbas aber isch en Röiber gsii» – mit dem churze Satz hört s Kapitel uf ([[JHN.18.40]])."}},
    {"id": "REFL-JHN-0206", "subject": "TU-JHN-018-039-040", "order": 2,
     "question_de": "Wie hat Barabbas diesen Tag wohl erlebt?",
     "gsw": {"question_de": "Wie hät de Barabbas dä Tag ächt erläbt?"}},
    # SUM-CH-JHN-019
    {"id": "REFL-JHN-0207", "subject": "SUM-CH-JHN-019", "order": 1,
     "question_de": "Pilatus findet keine Schuld und liefert Jesus doch aus: Was entscheidet am Ende?",
     "note_de": "Er sagt dreimal, er finde keine Schuld an ihm ([[JHN.18.38]], [[JHN.19.4]], [[JHN.19.6]]).",
     "gsw": {"question_de": "De Pilatus findet kei Schuld und lieferet de Jesus glich us: Was entscheidet am Schluss?", "note_de": "Er seit drüü Mal, er findi kei Schuld a ihm ([[JHN.18.38]], [[JHN.19.4]], [[JHN.19.6]])."}},
    {"id": "REFL-JHN-0208", "subject": "SUM-CH-JHN-019", "order": 2,
     "question_de": "Dieses Kapitel wurde oft gegen Juden gewendet: Was steht im Text, und was haben Leser daraus gemacht?",
     "note_de": "Im Text schreien zuerst «die Hohepriester und die Diener» ([[JHN.19.6]]), später heisst es «die Juden» ([[JHN.19.12]]); gekreuzigt wird Jesus von Soldaten ([[JHN.19.23]]).",
     "gsw": {"question_de": "Das Kapitel isch oft gäge Jude gwändet worde: Was staat im Text, und was händ Läser drus gmacht?", "note_de": "Im Text brüeled zerscht «d Hoheprieschter und d Diener» ([[JHN.19.6]]), spöter heisst s «d Jude» ([[JHN.19.12]]); gchrüüziget wird de Jesus vo Soldate ([[JHN.19.23]])."}},
    # TU-JHN-019-001-003
    {"id": "REFL-JHN-0209", "subject": "TU-JHN-019-001-003", "order": 1,
     "question_de": "Die Soldaten spielen König mit Jesus: Was zeigt ihr Spott – über ihn und über sie?",
     "note_de": "Dornenkranz, Purpurmantel und der Gruss «Sei gegrüsst, König der Juden!» ([[JHN.19.2-JHN.19.3]])",
     "gsw": {"question_de": "D Soldate spiled König mit em Jesus: Was zeigt ire Spott – über ihn und über sie?", "note_de": "Dornechranz, Purpurmantel und de Gruess «Sig gegrüesst, König vo de Jude!» ([[JHN.19.2-JHN.19.3]])"}},
    {"id": "REFL-JHN-0210", "subject": "TU-JHN-019-001-003", "order": 2,
     "question_de": "Der Text erzählt die Geisselung in einem einzigen Satz: Warum so knapp?",
     "gsw": {"question_de": "De Text verzellt s Geissle i eim einzige Satz: Wieso so churz?"}},
    # TU-JHN-019-004-007
    {"id": "REFL-JHN-0211", "subject": "TU-JHN-019-004-007", "order": 1,
     "question_de": "«Seht, der Mensch!» – was will Pilatus damit erreichen, und was sagt der Satz darüber hinaus?",
     "note_de": "Jesus kommt heraus mit Dornenkranz und Purpurmantel ([[JHN.19.5]]).",
     "gsw": {"question_de": "«Lueged, de Mänsch!» – was wott de Pilatus dermit erreiche, und was seit de Satz drüber use?", "note_de": "De Jesus chunnt use mit Dornechranz und Purpurmantel ([[JHN.19.5]])."}},
    {"id": "REFL-JHN-0212", "subject": "TU-JHN-019-004-007", "order": 2,
     "question_de": "Wer schreit hier «Kreuzige!», und wer nicht?",
     "gsw": {"question_de": "Wer brüelet da «Chrüüzig!», und wer nöd?"}},
    # TU-JHN-019-008-012
    {"id": "REFL-JHN-0213", "subject": "TU-JHN-019-008-012", "order": 1,
     "question_de": "«Woher bist du?» – warum schweigt Jesus gerade auf diese Frage?",
     "note_de": "Pilatus fürchtet sich noch mehr und fragt; Jesus gibt ihm keine Antwort ([[JHN.19.8-JHN.19.9]]).",
     "gsw": {"question_de": "«Vo wo bisch du?» – wieso schwiigt de Jesus grad uf die Frag?", "note_de": "De Pilatus fürcht sich no meh und fröget; de Jesus git ihm kei Antwort ([[JHN.19.8-JHN.19.9]])."}},
    {"id": "REFL-JHN-0214", "subject": "TU-JHN-019-008-012", "order": 2,
     "question_de": "Vollmacht «von oben»: Was bedeutet das für jemanden, der Macht über andere hat?",
     "gsw": {"question_de": "Vollmacht «vo obe»: Was bedüütet das für öpper, wo Macht über anderi hät?"}},
    # TU-JHN-019-013-016
    {"id": "REFL-JHN-0215", "subject": "TU-JHN-019-013-016", "order": 1,
     "question_de": "«Wir haben keinen König ausser dem Kaiser» – was bedeutet dieser Satz im Mund der Hohepriester?",
     "note_de": "Pilatus hatte gefragt: «Euren König soll ich kreuzigen?» ([[JHN.19.15]])",
     "gsw": {"question_de": "«Mir händ kei König usser em Kaiser» – was bedüütet dä Satz im Muul vo de Hoheprieschter?", "note_de": "De Pilatus hät gfröget: «Eue König söll ich chrüüzige?» ([[JHN.19.15]])"}},
    {"id": "REFL-JHN-0216", "subject": "TU-JHN-019-013-016", "order": 2,
     "question_de": "Der Erzähler nennt Ort und Stunde genau: Warum?",
     "gsw": {"question_de": "De Verzeller nännt Ort und Stund gnau: Wieso?"}},
    # TU-JHN-019-017-022
    {"id": "REFL-JHN-0217", "subject": "TU-JHN-019-017-022", "order": 1,
     "question_de": "Die Tafel steht in drei Sprachen: Wer soll sie lesen?",
     "note_de": "Hebräisch, Lateinisch und Griechisch ([[JHN.19.20]]).",
     "gsw": {"question_de": "D Tafle staat i drüü Sprache: Wer söll si läse?", "note_de": "Hebräisch, Latiinisch und Griechisch ([[JHN.19.20]])."}},
    {"id": "REFL-JHN-0218", "subject": "TU-JHN-019-017-022", "order": 2,
     "question_de": "«Was ich geschrieben habe, habe ich geschrieben» – ist das Trotz, Spott oder ein unfreiwilliges Bekenntnis?",
     "gsw": {"question_de": "«Was ich gschribe han, han ich gschribe» – isch das Trotz, Spott oder es unfreiwilligs Bekenntnis?"}},
    # TU-JHN-019-023-024
    {"id": "REFL-JHN-0219", "subject": "TU-JHN-019-023-024", "order": 1,
     "question_de": "Mitten in der Kreuzigung ein Streit um ein Kleidungsstück: Was zeigt dieses Detail?",
     "note_de": "Das Untergewand ist ohne Naht, von oben an durchgehend gewebt ([[JHN.19.23]]).",
     "gsw": {"question_de": "Mitts i de Chrüüzigung en Striit um es Chleid: Was zeigt das Detail?", "note_de": "S Undergwand isch ohni Naht, vo obe aa am Stück gwobe ([[JHN.19.23]])."}},
    {"id": "REFL-JHN-0220", "subject": "TU-JHN-019-023-024", "order": 2,
     "question_de": "Der Erzähler sieht darin ein Schriftwort erfüllt: Wie liest du solche Hinweise?",
     "gsw": {"question_de": "De Verzeller gseht drin es Schriftwort erfüllt: Wie lisisch du söttigi Hiiwiis?"}},
    # TU-JHN-019-025-027
    {"id": "REFL-JHN-0221", "subject": "TU-JHN-019-025-027", "order": 1,
     "question_de": "Was bedeutet es, dass Jesus im Sterben an seine Mutter und den Jünger denkt?",
     "note_de": "«Frau, siehe, dein Sohn!» – «Siehe, deine Mutter!» ([[JHN.19.26-JHN.19.27]])",
     "gsw": {"question_de": "Was bedüütet s, dass de Jesus im Stärbe a sini Mueter und de Jünger dänkt?", "note_de": "«Frau, lueg, din Sohn!» – «Lueg, dini Mueter!» ([[JHN.19.26-JHN.19.27]])"}},
    {"id": "REFL-JHN-0222", "subject": "TU-JHN-019-025-027", "order": 2,
     "question_de": "Die Frauen stehen beim Kreuz: Was sagt ihr Dableiben?",
     "gsw": {"question_de": "D Fraue stönd bim Chrüz: Was seit ires Dabliibe?"}},
    # TU-JHN-019-028-030
    {"id": "REFL-JHN-0223", "subject": "TU-JHN-019-028-030", "order": 1,
     "question_de": "«Es ist vollbracht» – was ist vollbracht?",
     "note_de": "Kurz zuvor heisst es, Jesus wisse, «dass schon alles vollbracht ist» ([[JHN.19.28]], [[JHN.19.30]]).",
     "gsw": {"question_de": "«Es isch vollbracht» – was isch vollbracht?", "note_de": "Churz vorher heisst s, de Jesus wüssi, «dass scho alles vollbracht isch» ([[JHN.19.28]], [[JHN.19.30]])."}},
    {"id": "REFL-JHN-0224", "subject": "TU-JHN-019-028-030", "order": 2,
     "question_de": "Der, der lebendiges Wasser verheissen hat, sagt «Mich dürstet»: Was hörst du darin?",
     "gsw": {"question_de": "Dä, wo läbigs Wasser verheisse hät, seit «Ich han Durscht»: Was ghörsch du drin?"}},
    # TU-JHN-019-031-037
    {"id": "REFL-JHN-0225", "subject": "TU-JHN-019-031-037", "order": 1,
     "question_de": "Warum betont der Erzähler so sehr, dass jemand das gesehen hat und sein Zeugnis wahr ist?",
     "note_de": "«Der es gesehen hat, hat es bezeugt, und sein Zeugnis ist wahr … damit auch ihr glaubt» ([[JHN.19.35]]).",
     "gsw": {"question_de": "Wieso betont de Verzeller so fescht, dass öpper das gseh hät und sis Zügnis wahr isch?", "note_de": "«Dä, wo s gseh hät, hät s bezüügt, und sis Zügnis isch wahr … demit au ir glaubed» ([[JHN.19.35]])."}},
    {"id": "REFL-JHN-0226", "subject": "TU-JHN-019-031-037", "order": 2,
     "question_de": "Blut und Wasser: Was haben Leser aller Zeiten in diesem Detail gesehen – und was siehst du?",
     "gsw": {"question_de": "Bluet und Wasser: Was händ Läser vo allne Ziite i dem Detail gseh – und was gsehsch du?"}},
    # TU-JHN-019-038-042
    {"id": "REFL-JHN-0227", "subject": "TU-JHN-019-038-042", "order": 1,
     "question_de": "Zwei, die bisher im Verborgenen waren, treten jetzt hervor: Warum gerade jetzt?",
     "note_de": "Josef war ein heimlicher Jünger aus Furcht; Nikodemus war zuerst bei Nacht gekommen ([[JHN.19.38-JHN.19.39]]).",
     "gsw": {"question_de": "Zwee, wo bis jetzt im Verborgne gsii sind, chömed jetzt füre: Wieso grad jetzt?", "note_de": "De Josef isch us Angscht en heimliche Jünger gsii; de Nikodemus isch zerscht znacht choo ([[JHN.19.38-JHN.19.39]])."}},
    {"id": "REFL-JHN-0228", "subject": "TU-JHN-019-038-042", "order": 2,
     "question_de": "Hundert Pfund Myrrhe und Aloe: Was drückt diese Menge aus?",
     "gsw": {"question_de": "Hundert Pfund Myrrhe und Aloe: Was drückt die Mängi us?"}},
    # SUM-CH-JHN-020
    {"id": "REFL-JHN-0229", "subject": "SUM-CH-JHN-020", "order": 1,
     "question_de": "Sehen und glauben: Wie gehen die Menschen in diesem Kapitel damit um, jeder auf seine Weise?",
     "note_de": "Gegen Ende sagt Jesus zu Thomas: «Selig sind, die nicht gesehen und doch geglaubt haben!» ([[JHN.20.29]]).",
     "gsw": {"question_de": "Gseh und glaube: Wie gönd d Mänsche i dem Kapitel dermit um, jede uf sini Art?", "note_de": "Gäge de Schluss seit de Jesus zum Thomas: «Sälig sind die, wo nöd gseh händ und trotzdem glaubt händ!» ([[JHN.20.29]])."}},
    # TU-JHN-020-001-010
    {"id": "REFL-JHN-0230", "subject": "TU-JHN-020-001-010", "order": 1,
     "question_de": "Der andere Jünger «sah und glaubte» – was genau hat er gesehen?",
     "note_de": "Er sieht die Leinenbinden und das Schweisstuch für sich liegen ([[JHN.20.6-JHN.20.8]]).",
     "gsw": {"question_de": "De ander Jünger «hät gseh und hät glaubt» – was gnau hät er gseh?", "note_de": "Er gseht d Liinebinde und s Schweisstuech für sich ligge ([[JHN.20.6-JHN.20.8]])."}},
    {"id": "REFL-JHN-0231", "subject": "TU-JHN-020-001-010", "order": 2,
     "question_de": "Der eine läuft schneller, der andere geht zuerst hinein: Was erzählt dieses Wettlaufen?",
     "gsw": {"question_de": "De eint lauft schneller, de ander gaat zerscht ine: Was verzellt das Wettrenne?"}},
    # TU-JHN-020-011-018
    {"id": "REFL-JHN-0232", "subject": "TU-JHN-020-011-018", "order": 1,
     "question_de": "Warum erkennt Maria Jesus erst, als er ihren Namen sagt?",
     "note_de": "«Mariam!» – «Rabbuni!» ([[JHN.20.16]])",
     "gsw": {"question_de": "Wieso erchännt d Maria de Jesus erscht, won er ire Name seit?", "note_de": "«Mariam!» – «Rabbuni!» ([[JHN.20.16]])"}},
    {"id": "REFL-JHN-0233", "subject": "TU-JHN-020-011-018", "order": 2,
     "question_de": "«Halte mich nicht fest!» – was muss Maria loslassen?",
     "gsw": {"question_de": "«Heb mich nöd fescht!» – was mues d Maria loslaa?"}},
    {"id": "REFL-JHN-0234", "subject": "TU-JHN-020-011-018", "order": 3,
     "question_de": "Eine Frau ist die erste, die sagt «Ich habe den Herrn gesehen»: Was bedeutet das?",
     "gsw": {"question_de": "E Frau isch di erscht, wo seit «Ich han de Herr gseh»: Was bedüütet das?"}},
    # TU-JHN-020-019-023
    {"id": "REFL-JHN-0235", "subject": "TU-JHN-020-019-023", "order": 1,
     "question_de": "Jesus zeigt den Jüngern Hände und Seite: Warum zeigt der Auferstandene seine Wunden?",
     "note_de": "Erst danach heisst es: «Da freuten sich die Jünger» ([[JHN.20.20]]).",
     "gsw": {"question_de": "De Jesus zeigt de Jünger Händ und Siite: Wieso zeigt de Uferstande sini Wunde?", "note_de": "Erscht dänn heisst s: «Da händ sich d Jünger gfröit» ([[JHN.20.20]])."}},
    {"id": "REFL-JHN-0236", "subject": "TU-JHN-020-019-023", "order": 2,
     "question_de": "Hinter verschlossenen Türen «Friede euch!»: Was sind deine verschlossenen Türen?",
     "gsw": {"question_de": "Hinder verschlossne Tüüre «Fride mit eu!»: Was sind dini verschlossne Tüüre?"}},
    # TU-JHN-020-024-029
    {"id": "REFL-JHN-0237", "subject": "TU-JHN-020-024-029", "order": 1,
     "question_de": "Thomas will sehen und berühren: Ist sein Zweifel ein Fehler oder ein Weg?",
     "note_de": "Jesus geht auf seine Bedingung ein: «Reich deinen Finger hierher» ([[JHN.20.25]], [[JHN.20.27]]).",
     "gsw": {"question_de": "De Thomas wott gseh und aalänge: Isch sin Zwiifel en Fehler oder en Wäg?", "note_de": "De Jesus gaat uf sini Bedingig ii: «Streck din Finger da ane» ([[JHN.20.25]], [[JHN.20.27]])."}},
    {"id": "REFL-JHN-0238", "subject": "TU-JHN-020-024-029", "order": 2,
     "question_de": "Der Text sagt nicht, ob Thomas Jesus tatsächlich berührt hat: Was macht diese Lücke mit dir?",
     "gsw": {"question_de": "De Text seit nöd, öb de Thomas de Jesus würkli aaglängt hät: Was macht die Lugge mit dir?"}},
    {"id": "REFL-JHN-0239", "subject": "TU-JHN-020-024-029", "order": 3,
     "question_de": "«Selig sind, die nicht gesehen und doch geglaubt haben» – wem gilt das?",
     "gsw": {"question_de": "«Sälig sind die, wo nöd gseh händ und trotzdem glaubt händ» – wem gilt das?"}},
    # TU-JHN-020-030-031
    {"id": "REFL-JHN-0240", "subject": "TU-JHN-020-030-031", "order": 1,
     "question_de": "Das Buch sagt, es habe ausgewählt: Was fehlt dir vielleicht in dieser Auswahl?",
     "note_de": "«Noch viele andere Zeichen hat Jesus … getan, die nicht in diesem Buch aufgeschrieben sind» ([[JHN.20.30]]).",
     "gsw": {"question_de": "S Buech seit, es heig usgwählt: Was fäält dir villicht i dere Uswahl?", "note_de": "«No vili anderi Zeiche hät de Jesus … vor de Jünger gmacht, wo nöd i däm Buech ufgschribe sind» ([[JHN.20.30]])."}},
    {"id": "REFL-JHN-0241", "subject": "TU-JHN-020-030-031", "order": 2,
     "question_de": "«Damit ihr glaubt»: Darf ein Text so offen sagen, was er bei den Lesenden erreichen will?",
     "gsw": {"question_de": "«Demit ir glaubed»: Törf en Text so offe säge, was er bi de Läsende erreiche wott?"}},
    # SUM-CH-JHN-021
    {"id": "REFL-JHN-0242", "subject": "SUM-CH-JHN-021", "order": 1,
     "question_de": "Warum geht das Buch nach dem ersten Schluss noch einmal weiter?",
     "note_de": "Schon [[JHN.20.30-JHN.20.31]] klingt wie ein Schluss; dann folgt eine weitere Begegnung am See.",
     "gsw": {"question_de": "Wieso gaat s Buech nach em erschte Schluss nomal wiiter?", "note_de": "Scho [[JHN.20.30-JHN.20.31]] tönt wie en Schluss; dänn chunnt nomal e Begägnig am See."}},
    # TU-JHN-021-001-014
    {"id": "REFL-JHN-0243", "subject": "TU-JHN-021-001-014", "order": 1,
     "question_de": "Die Jünger sind wieder beim Fischen: Ist das Rückkehr in den Alltag oder Ratlosigkeit?",
     "note_de": "Petrus sagt: «Ich gehe fischen», und die anderen gehen mit ([[JHN.21.3]]).",
     "gsw": {"question_de": "D Jünger sind wider bim Fische: Isch das Ruggchehr in Alltag oder Ratlosigkeit?", "note_de": "De Petrus seit: «Ich gaa go fische», und di andere gönd mit ([[JHN.21.3]])."}},
    {"id": "REFL-JHN-0244", "subject": "TU-JHN-021-001-014", "order": 2,
     "question_de": "Jesus hat schon ein Feuer gemacht und lädt zum Essen ein: Was sagt dieses Frühstück?",
     "gsw": {"question_de": "De Jesus hät scho es Füür gmacht und laadt zum Ässe ii: Was seit das Zmorge?"}},
    # TU-JHN-021-015-019
    {"id": "REFL-JHN-0245", "subject": "TU-JHN-021-015-019", "order": 1,
     "question_de": "Dreimal «Liebst du mich?» – warum dreimal?",
     "note_de": "Petrus wird beim dritten Mal traurig; vorher hatte er dreimal geleugnet, zu Jesus zu gehören ([[JHN.21.17]], [[JHN.18.17]], [[JHN.18.25-JHN.18.27]]).",
     "gsw": {"question_de": "Drüü Mal fröget de Jesus de Petrus, öb er en gärn heig: Wieso drüü Mal?", "note_de": "De Petrus wird bim dritte Mal truurig; vorher hät er drüü Mal abgstritte, dass er zum Jesus ghört ([[JHN.21.17]], [[JHN.18.17]], [[JHN.18.25-JHN.18.27]])."}},
    {"id": "REFL-JHN-0246", "subject": "TU-JHN-021-015-019", "order": 2,
     "question_de": "Petrus bekommt einen Auftrag, nicht eine Strafe: Was bedeutet das?",
     "gsw": {"question_de": "De Petrus überchunnt en Uftrag, nöd e Straf: Was bedüütet das?"}},
    # TU-JHN-021-020-023
    {"id": "REFL-JHN-0247", "subject": "TU-JHN-021-020-023", "order": 1,
     "question_de": "«Was geht es dich an?» – was sagt diese Antwort über den Blick auf den Weg eines anderen?",
     "note_de": "Petrus fragt: «Herr, was aber wird mit diesem?» ([[JHN.21.21-JHN.21.22]])",
     "gsw": {"question_de": "«Was gaat das dich aa?» – was seit die Antwort über de Blick uf de Wäg vo me andere?", "note_de": "De Petrus fröget: «Herr, was isch aber mit däm?» ([[JHN.21.21-JHN.21.22]])"}},
    {"id": "REFL-JHN-0248", "subject": "TU-JHN-021-020-023", "order": 2,
     "question_de": "Der Erzähler korrigiert ein Gerücht: Wie entstehen falsche Sätze über Worte, die jemand gesagt hat?",
     "gsw": {"question_de": "De Verzeller korrigiert es Grücht: Wie entstönd falschi Sätz über Wort, wo öpper gseit hät?"}},
    # TU-JHN-021-024-025
    {"id": "REFL-JHN-0249", "subject": "TU-JHN-021-024-025", "order": 1,
     "question_de": "«Wir wissen, dass sein Zeugnis wahr ist» – wer ist dieses «wir»?",
     "note_de": "Der Text unterscheidet den Jünger, der geschrieben hat, von einer Gruppe, die für ihn bürgt ([[JHN.21.24]]).",
     "gsw": {"question_de": "«Mer wüssed, dass sis Zügnis wahr isch» – wer isch das «mer»?", "note_de": "De Text unterscheidet de Jünger, wo gschribe hät, vo nere Gruppe, wo für ihn bürgt ([[JHN.21.24]])."}},
    {"id": "REFL-JHN-0250", "subject": "TU-JHN-021-024-025", "order": 2,
     "question_de": "Die Welt könnte die Bücher nicht fassen: Was ist mit allem, was nicht aufgeschrieben ist?",
     "gsw": {"question_de": "D Wält chönt d Büecher nöd fasse: Was isch mit allem, wo nöd ufgschribe isch?"}},
]

RECEPTIONS = [
    {
     "id": "RCPT-JHN-0001",
     "subject": "SUM-BOOK-JHN",
     "tradition": "church_fathers",
     "period_de": "um 180",
     "text_de": "Irenäus von Lyon schreibt, Johannes, der Jünger des Herrn, der an seiner Brust gelegen hatte, habe das Evangelium herausgegeben, als er in Ephesus in der Provinz Asia lebte. Daraus wurde die verbreitete kirchliche Überlieferung zum Verfasser; das Buch selbst nennt keinen Namen ([[JHN.21.24]]).",
     "sources_de": [
      "Irenäus, Gegen die Häresien (Adversus haereses) III,1,1"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Irenäus, Adversus haereses III,1,1",
        "found_at": "https://logoslibrary.org/irenaeus/heresies/301.html (englische Übersetzung, Ante-Nicene Fathers)",
        "finding_de": "Die Stelle sagt, Johannes, der Jünger des Herrn, der an seiner Brust gelegen hatte, habe während seines Aufenthalts in Ephesus in Asia ein Evangelium herausgegeben."
       }
      ]
     },
     "gsw": {
      "period_de": "um 180",
      "text_de": "De Irenäus vo Lyon schriibt, de Johannes, de Jünger vom Herr, wo a sinere Bruscht gläge isch, heig s Evangelium usegää, won er z Ephesus i de Provinz Asia gläbt hät. Drus isch di verbreitet chilchlich Überlieferig zum Verfasser worde; s Buech sälber nännt kein Name ([[JHN.21.24]])."
     }
    },
    {
     "id": "RCPT-JHN-0002",
     "subject": "SUM-BOOK-JHN",
     "tradition": "church_fathers",
     "period_de": "um 200 (überliefert um 325)",
     "text_de": "Nach Klemens von Alexandria, den Eusebius zitiert, sah Johannes, dass das Äussere schon in den anderen Evangelien dargestellt war, und schrieb auf Bitten seiner Freunde und vom Geist bewegt ein «geistliches Evangelium». Die Bezeichnung prägt bis heute, wie man Johannes neben den anderen drei Evangelien liest.",
     "sources_de": [
      "Eusebius, Kirchengeschichte VI,14,7 (nach Klemens von Alexandria, Hypotyposen)"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Eusebius, Kirchengeschichte VI,14,7",
        "found_at": "https://bkv.unifr.ch/works/cpg-3495/compare/kirchengeschichte-bkv-2/159/the-church-history-of-eusebius (englische Übersetzung NPNF und deutsche BKV)",
        "finding_de": "Die Stelle sagt, Johannes habe, da das Äussere in den Evangelien schon dargelegt war, auf Veranlassung seiner Schüler und vom Geist inspiriert ein «geistiges Evangelium» verfasst."
       }
      ]
     },
     "gsw": {
      "period_de": "um 200 (überliferet um 325)",
      "text_de": "Nach em Klemens vo Alexandria, wo de Eusebius zitiert, hät de Johannes gseh, dass s Üsserlich i de andere Evangelie scho dargstellt gsii isch, und hät uf Bitt vo sine Fründ und vom Geischt bewegt es «geischtlichs Evangelium» gschribe. D Bezeichnig prägt bis hüt, wie mer de Johannes näbe de andere drüü Evangelie lisst."
     }
    },
    {
     "id": "RCPT-JHN-0003",
     "subject": "TU-JHN-001-001-018",
     "tradition": "church_fathers",
     "period_de": "um 400",
     "text_de": "Augustinus erzählt in seinen Bekenntnissen, er habe in Büchern der Platoniker sinngemäss gelesen: «Im Anfang war das Wort, und das Wort war bei Gott»; dass aber «das Wort Fleisch wurde und unter uns wohnte», habe er dort nicht gefunden. Für ihn liegt das Unterscheidende im Satz [[JHN.1.14]].",
     "sources_de": [
      "Augustinus, Bekenntnisse (Confessiones) VII,9"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Augustinus, Confessiones VII,9",
        "found_at": "https://logoslibrary.org/augustine/confessions/0709.html (englische Übersetzung Pilkington)",
        "finding_de": "Die Stelle sagt, er habe dort nicht mit denselben Worten, aber dem Sinn nach «Im Anfang war das Wort …» gelesen, nicht aber «das Wort wurde Fleisch und wohnte unter uns»."
       }
      ]
     },
     "gsw": {
      "period_de": "um 400",
      "text_de": "De Augustinus verzellt i sine Bekenntnis, er heig i Büecher vo de Platoniker sinngmäss gläse: «Im Aafang isch s Wort gsii, und s Wort isch bi Gott gsii»; dass aber «s Wort Fleisch worde isch und under üs gwohnt hät», heig er dört nöd gfunde. Für ihn liit s Unterscheidend im Satz [[JHN.1.14]]."
     }
    },
    {
     "id": "RCPT-JHN-0004",
     "subject": "TU-JHN-001-001-018",
     "tradition": "literature",
     "period_de": "1808",
     "text_de": "In Goethes «Faust» (erster Teil, Szene «Studierzimmer») will Faust den Anfang des Johannesevangeliums «in mein geliebtes Deutsch» übertragen. Er verwirft «Wort», dann «Sinn» und «Kraft» und schreibt schliesslich: «Im Anfang war die Tat!» Die Szene hat das deutsche Nachdenken über den Satz «Im Anfang war das Wort» stark geprägt.",
     "sources_de": [
      "Johann Wolfgang von Goethe, Faust. Der Tragödie erster Teil, Szene «Studierzimmer»"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Goethe, Faust I, «Studierzimmer»",
        "found_at": "https://projekt-gutenberg.org/authors/johann-wolfgang-von-goethe/books/faust-eine-tragoedie/chapter/7",
        "finding_de": "Die Szene enthält «In mein geliebtes Deutsch zu übertragen», die Fassungen «Wort», «Sinn», «Kraft» und «Im Anfang war die Tat!»."
       }
      ]
     },
     "gsw": {
      "period_de": "1808",
      "text_de": "Im «Faust» vom Goethe (erschte Teil, Szene «Studierzimmer») wott de Faust de Aafang vom Johannesevangelium «in mein geliebtes Deutsch» übertrage. Er verwirft «Wort», dänn «Sinn» und «Kraft» und schriibt am Schluss: «Im Anfang war die Tat!» D Szene hät s düütsch Nachedänke über de Satz «Im Aafang isch s Wort gsii» starch prägt."
     }
    },
    {
     "id": "RCPT-JHN-0005",
     "subject": "TU-JHN-001-001-018",
     "tradition": "liturgy",
     "period_de": "Mittelalter bis heute",
     "text_de": "In der römisch-katholischen Messe am Weihnachtstag ist der Johannesprolog das Evangelium. In der älteren Form der Messe wurde er ausserdem am Schluss jeder Messe als «Schlussevangelium» gelesen; die nach dem Zweiten Vatikanischen Konzil erneuerte Messe kennt diesen Brauch nicht mehr.",
     "sources_de": [
      "Römisches Lektionar, Weihnachten, Messe am Tag",
      "Schlussevangelium (Last Gospel) der tridentinischen Messe"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Lektionar, Weihnachten, Messe am Tag",
        "found_at": "https://www.catholic-resources.org/Lectionary/1998USL-Christmas.htm",
        "finding_de": "Evangelium der Messe am Tag: [[JHN.1.1-JHN.1.18]] (oder eine kürzere Auswahl daraus)."
       },
       {
        "source": "Schlussevangelium",
        "found_at": "https://en.wikipedia.org/wiki/Last_Gospel",
        "finding_de": "[[JHN.1.1-JHN.1.14]] am Schluss der tridentinischen Messe; zuerst private Andacht des Priesters, dann in die Rubriken aufgenommen; in der Messe Pauls VI. weggelassen."
       }
      ]
     },
     "gsw": {
      "period_de": "Mittelalter bis hüt",
      "text_de": "I de römisch-katholische Mäss am Wienachtstag isch de Johannesprolog s Evangelium. I de ältere Form vo de Mäss isch er ussertem am Schluss vo jedere Mäss als «Schlussevangelium» gläse worde; di nöi Mäss nach em Zweite Vatikanische Konzil kännt dä Bruuch nüme."
     }
    },
    {
     "id": "RCPT-JHN-0006",
     "subject": "TU-JHN-001-029-034",
     "tradition": "liturgy",
     "period_de": "seit dem 7. Jahrhundert",
     "text_de": "Der Ruf «Lamm Gottes, das die Sünde der Welt wegnimmt» ([[JHN.1.29]]) wurde zum «Agnus Dei» der Messe. Nach dem Liber Pontificalis ordnete Papst Sergius I. Ende des 7. Jahrhunderts an, dass Klerus und Volk es beim Brechen des Brotes singen.",
     "sources_de": [
      "Liber Pontificalis, Sergius I. (nach Catholic Encyclopedia, «Agnus Dei (in Liturgy)»)"
     ],
     "confidence": "probable",
     "uncertain_de": "Die Angabe zum Liber Pontificalis ist über ein Nachschlagewerk geprüft, nicht an einer Ausgabe des Liber Pontificalis selbst.",
     "source_check": {
      "date": "2026-10-28",
      "result": "partly",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Catholic Encyclopedia, «Agnus Dei (in Liturgy)»",
        "found_at": "https://www.newadvent.org/cathen/01221a.htm",
        "finding_de": "Der Artikel nennt [[JHN.1.29]] als Quelle und berichtet, nach dem Liber Pontificalis habe Sergius I. 687 angeordnet, dass Klerus und Volk das Agnus Dei bei der Brotbrechung singen; der Liber Pontificalis selbst wurde nicht nachgeschlagen."
       }
      ]
     },
     "gsw": {
      "period_de": "sit em 7. Jahrhundert",
      "text_de": "De Ruef «Lamm vo Gott, wo d Sünd vo de Wält wägnimmt» ([[JHN.1.29]]) isch zum «Agnus Dei» vo de Mäss worde. Nach em Liber Pontificalis hät de Papscht Sergius I. am Änd vom 7. Jahrhundert aagordnet, dass d Geischtliche und s Volk es bim Bräche vom Broot singed."
     }
    },
    {
     "id": "RCPT-JHN-0007",
     "subject": "TU-JHN-004-001-015",
     "tradition": "liturgy",
     "period_de": "bis heute",
     "text_de": "In den orthodoxen Kirchen ist der fünfte Sonntag der Osterzeit der «Sonntag der Samariterin». Die Überlieferung gibt der namenlosen Frau den Namen Photini (die «Erleuchtete») und verehrt sie als Märtyrin, die Christus verkündet hat ([[JHN.4.28-JHN.4.29]]).",
     "sources_de": [
      "Orthodoxe Liturgie, Sonntag der Samariterin (5. Sonntag der Osterzeit)"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Sonntag der Samariterin",
        "found_at": "https://www.pravmir.com/today-the-orthodox-church-celebrates-the-sunday-of-the-samaritan-woman/",
        "finding_de": "Fünfter Sonntag der Osterzeit; die Frau heisst dort «Great-martyr Photeini» und wird als Verkünderin in ihrer Stadt genannt. Die Deutung des Namens als «Erleuchtete» ist eigene Übersetzung des griechischen Namens."
       }
      ]
     },
     "gsw": {
      "period_de": "bis hüt",
      "text_de": "I de orthodoxe Chilche isch de füft Sunntig vo de Oschterziit de «Sunntig vo de Samariterin». D Überlieferig git de Frau ohni Name de Name Photini (di «Erlüüchtet») und verehrt si als Märtyrin, wo Christus verchündet hät ([[JHN.4.28-JHN.4.29]])."
     }
    },
    {
     "id": "RCPT-JHN-0008",
     "subject": "TU-JHN-006-060-071",
     "tradition": "reformation",
     "period_de": "1529",
     "text_de": "Im Abendmahlsstreit der Reformation beruft sich Huldrych Zwingli beim Marburger Religionsgespräch auf das Wort «Das Fleisch nützt nichts» ([[JHN.6.63]]) für ein geistliches Verständnis des Abendmahls; Martin Luther hält am Wortlaut der Einsetzungsworte fest und schreibt nach dem Bericht «Hoc est corpus meum» («Das ist mein Leib») mit Kreide auf den Tisch. Die Frage, wie [[JHN.6.51-JHN.6.58]] mit dem Abendmahl zusammenhängt, wird bis heute verschieden beantwortet.",
     "sources_de": [
      "Philip Schaff, History of the Christian Church, Bd. 7, Abschnitt zum Marburger Gespräch"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Schaff, History of the Christian Church VII (Marburger Gespräch)",
        "found_at": "https://ccel.org/ccel/schaff/hcc7/hcc7.ii.vii.viii.html",
        "finding_de": "Schaff berichtet, die Schweizer hätten sich auf [[JHN.6.63]] gestützt und Zwingli habe den Vers vorgelesen; Luther habe «Hoc est corpus meum» mit Kreide auf den Tisch geschrieben. Geschichtsdarstellung des 19. Jahrhunderts, nicht die Protokolle selbst."
       }
      ]
     },
     "gsw": {
      "period_de": "1529",
      "text_de": "Im Abigmahlsstriit vo de Reformation beruefft sich de Huldrych Zwingli am Marburger Religionsgspröch uf s Wort «S Fleisch nützt nüüt» ([[JHN.6.63]]) für es geischtlichs Verständnis vom Abigmahl; de Martin Luther hebt am Wortlut vo de Iisetzigswort fescht und schriibt nach em Bricht «Hoc est corpus meum» («Das isch min Liib») mit Chriide uf de Tisch. D Frag, wie [[JHN.6.51-JHN.6.58]] mit em Abigmahl zämehangt, wird bis hüt verschide beantwortet."
     }
    },
    {
     "id": "RCPT-JHN-0009",
     "subject": "TU-JHN-008-001-011",
     "tradition": "church_fathers",
     "period_de": "um 420",
     "text_de": "Schon Augustinus wusste, dass die Erzählung von der Frau, die beim Ehebruch ergriffen wurde, nicht in allen Handschriften stand. Er vermutete, einige Kleingläubige hätten sie entfernt, weil sie fürchteten, sie erlaube ihren Frauen die Sünde. Die heutige Textforschung sieht es umgekehrt: Der Abschnitt fehlt in den ältesten Handschriften und gilt als spätere Einfügung ([[JHN.7.53-JHN.8.11]]).",
     "sources_de": [
      "Augustinus, Über ehebrecherische Ehen (De adulterinis coniugiis) II,6–7"
     ],
     "confidence": "probable",
     "uncertain_de": "Augustins Wortlaut ist nur über eine Zitatsammlung geprüft, nicht an einer Ausgabe seines Werks.",
     "source_check": {
      "date": "2026-10-28",
      "result": "partly",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Augustinus, De adulterinis coniugiis II,6–7",
        "found_at": "https://bible-researcher.com/adult.html (Zitatsammlung mit lateinischem Text)",
        "finding_de": "Die Sammlung zitiert die Stelle lateinisch («nonnulli modicae, vel potius inimici verae fidei …»): Einige hätten die Erzählung aus Furcht, sie gebe Frauen Straflosigkeit, aus ihren Handschriften entfernt. Eine Ausgabe des Werks selbst war nicht zugänglich."
       }
      ]
     },
     "gsw": {
      "period_de": "um 420",
      "text_de": "Scho de Augustinus hät gwüsst, dass d Gschicht vo de Frau, wo bim Ehebruch ertappt worde isch, nöd i allne Handschrifte gstande isch. Er hät vermuetet, es paar Chliigläubigi heiged si usegnoo, wil si gfürchtet händ, si erlaubi irne Fraue d Sünd. Di hütig Textforschig gseht s umgekehrt: De Abschnitt fäält i de eltischte Handschrifte und gilt als spöteri Iifüegig ([[JHN.7.53-JHN.8.11]])."
     }
    },
    {
     "id": "RCPT-JHN-0010",
     "subject": "TU-JHN-013-001-011",
     "tradition": "liturgy",
     "period_de": "bis heute",
     "text_de": "Am Gründonnerstag wird in der römisch-katholischen Abendmahlsmesse jedes Jahr [[JHN.13.1-JHN.13.15]] gelesen, und vielerorts wäscht der Priester Menschen die Füsse. Der Brauch heisst nach dem lateinischen Anfang von [[JHN.13.34]] «Mandatum» («Gebot»); daher kommt der englische Name «Maundy Thursday».",
     "sources_de": [
      "Römisches Lektionar, Gründonnerstag, Messe vom Letzten Abendmahl",
      "Fusswaschung («Mandatum»)"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Lektionar, Gründonnerstag",
        "found_at": "https://catholic-resources.org/Lectionary/1998USL-Easter.htm",
        "finding_de": "Evangelium der Abendmahlsmesse in allen drei Lesejahren: [[JHN.13.1-JHN.13.15]]."
       },
       {
        "source": "Mandatum",
        "found_at": "https://www.catholicculture.org/culture/liturgicalyear/blog/index.cfm?id=128",
        "finding_de": "Der Name «Mandatum» kommt vom lateinischen Anfang von [[JHN.13.34]] «Mandatum novum do vobis»; daher «Maundy Thursday»."
       }
      ]
     },
     "gsw": {
      "period_de": "bis hüt",
      "text_de": "Am Hoche Donschtig wird i de römisch-katholische Abigmahlsmäss jedes Jahr [[JHN.13.1-JHN.13.15]] gläse, und a vilne Orte wäscht de Prieschter Mänsche d Füess. De Bruuch heisst nach em latiinische Aafang vo [[JHN.13.34]] «Mandatum» («Gebot»); drum heisst de Tag uf Änglisch «Maundy Thursday»."
     }
    },
    {
     "id": "RCPT-JHN-0011",
     "subject": "SUM-CH-JHN-018",
     "tradition": "music",
     "period_de": "1724",
     "text_de": "Johann Sebastian Bach vertont in der Johannes-Passion den Bericht von [[JHN.18.1-JHN.19.42]] mit Chorälen und Arien. Die erste Aufführung war am Karfreitag, 7. April 1724, in der Nikolaikirche in Leipzig. Weil im vertonten Bibeltext Sätze, die das Evangelium «den Juden» zuschreibt, vom Chor gesungen werden (etwa [[JHN.19.7]], [[JHN.19.12]]), wird gefragt, ob das Werk Judenfeindschaft weitergibt; Michael Marissen kommt 1998 zum Schluss, Feindschaft gegen Juden zu fördern sei weder Thema noch Zweck von Bachs Vertonung.",
     "sources_de": [
      "Johann Sebastian Bach, Johannes-Passion BWV 245",
      "Michael Marissen, Lutheranism, Anti-Judaism, and Bach's St. John Passion (Oxford University Press 1998)"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Bach, Johannes-Passion, Uraufführung",
        "found_at": "https://www.l-iz.de/melder/wortmelder/2016/03/nikolaikirche-bachs-johannespassion-ort-der-urauffuehrung-130323",
        "finding_de": "Uraufführung am Karfreitag, 7. April 1724, in der Leipziger Nikolaikirche."
       },
       {
        "source": "Marissen, Lutheranism, Anti-Judaism, and Bach's St. John Passion (1998)",
        "found_at": "https://works.swarthmore.edu/fac-music/12 (Verlagsangabe und Zusammenfassung, Swarthmore College)",
        "finding_de": "Am 2026-10-29 von einer weiteren Instanz ergänzt und nachgeschlagen: Die Zusammenfassung fragt, ob die Johannes-Passion Feindschaft gegen Juden fördert, und hält fest, dies sei nicht Thema oder Zweck von Bachs Vertonung (Oxford University Press 1998). Das Buch selbst wurde nicht eingesehen."
       }
      ]
     },
     "gsw": {
      "period_de": "1724",
      "text_de": "De Johann Sebastian Bach vertont i de Johannes-Passion de Bricht vo [[JHN.18.1-JHN.19.42]] mit Choräl und Arie. Di erscht Uffüerig isch am Karfriitig, 7. April 1724, i de Nikolaichilche z Leipzig gsii. Wil im vertonte Bibeltext Sätz, wo s Evangelium «de Jude» zueschriibt, vom Chor gsunge wärded (öppe [[JHN.19.7]], [[JHN.19.12]]), wird gfröget, öb s Wärch Judefeindschaft wiitergit; de Michael Marissen chunnt 1998 zum Schluss, Feindschaft gäge Jude z fördere seig weder s Thema no de Zwäck vo de Vertonig vom Bach."
     }
    },
    {
     "id": "RCPT-JHN-0012",
     "subject": "TU-JHN-019-004-007",
     "tradition": "church_teaching",
     "period_de": "1965 bis heute",
     "text_de": "Die Passionserzählung des Johannes, in der oft pauschal «die Juden» handeln, wurde über Jahrhunderte zur Anklage aller Juden verwendet und hat Judenfeindschaft genährt. Das Zweite Vatikanische Konzil hält in der Erklärung «Nostra aetate» fest: Zwar hätten jüdische Obrigkeiten mit ihren Anhängern auf den Tod Christi gedrängt (mit Verweis auf [[JHN.19.6]]); doch dürfe man das Geschehen weder allen damals lebenden noch den heutigen Juden zur Last legen. Neuere Auslegung fragt, wen das Evangelium mit «den Juden» jeweils meint.",
     "sources_de": [
      "Zweites Vatikanisches Konzil, Erklärung «Nostra aetate» 4 (1965)"
     ],
     "confidence": "high",
     "uncertain_de": "Eine kirchliche Erklärung, keine Forschung; die Einordnung unter «Forschung» ist ein Behelf, weil die Liste der Traditionen keine eigene Rubrik dafür hat.",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Nostra aetate 4",
        "found_at": "https://www.christianunity.va/content/unitacristiani/en/commissione-per-i-rapporti-religiosi-con-l-ebraismo/nostra-aetate-n--4/en.html",
        "finding_de": "Der Text sagt, jüdische Obrigkeiten und ihre Anhänger hätten auf den Tod Christi gedrängt; das Leiden dürfe aber weder allen damaligen noch den heutigen Juden zur Last gelegt werden, und die Juden dürften nicht als verworfen oder verflucht dargestellt werden."
       },
       {
        "source": "Nostra aetate 4, Stellenverweis",
        "found_at": "https://www.faculty.umb.edu/lawrence_blum/courses/290h_09/readings/nostra_the_bible.pdf",
        "finding_de": "Der Konzilstext verweist an dieser Stelle in Klammern auf [[JHN.19.6]]."
       }
      ]
     },
     "gsw": {
      "period_de": "1965 bis hüt",
      "text_de": "D Passionsgschicht vom Johannes, i dere oft pauschal «d Jude» handled, isch dur Jahrhundert zur Aaklag vo allne Jude bruucht worde und hät Judefeindschaft gnährt. S Zweit Vatikanisch Konzil haltet i de Erklärig «Nostra aetate» fescht: Zwar heiged jüdischi Obrigkeite mit irne Aahänger uf de Tod vo Christus drängt (mit Verwiis uf [[JHN.19.6]]); aber mer dörf das Gscheh weder allne Jude, wo dänn gläbt händ, no de hütige Jude zur Laascht lege. Neueri Uslegig fröget, wän s Evangelium mit «de Jude» jewiils meint."
     }
    },
    {
     "id": "RCPT-JHN-0013",
     "subject": "TU-JHN-020-011-018",
     "tradition": "art",
     "period_de": "um 1440",
     "text_de": "Fra Angelico malt im Kloster San Marco in Florenz das «Noli me tangere» («Halte mich nicht fest», [[JHN.20.17]]) an die Wand einer Mönchszelle: Maria aus Magdala kniet vor dem Grab im Garten, der Auferstandene wendet sich ihr zu und geht zugleich weg.",
     "sources_de": [
      "Fra Angelico, «Noli me tangere», Fresko, Kloster San Marco, Florenz"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Fra Angelico, Noli me tangere",
        "found_at": "https://scotland.op.org/fra-angelicos-noli-me-tangere-at-san-marco/",
        "finding_de": "Fresko von Fra Angelico, 1440–1441, in einer Zelle von San Marco; Maria kniet links vor dem Felsengrab, Jesus wendet sich ihr zu und scheint sich zu entfernen; Garten."
       }
      ]
     },
     "gsw": {
      "period_de": "um 1440",
      "text_de": "De Fra Angelico malt im Chloschter San Marco z Florenz s «Noli me tangere» («Heb mich nöd fescht», [[JHN.20.17]]) a d Wand vo nere Mönchszälle: D Maria vo Magdala chniet vor em Grab im Garte, de Uferstande wändt sich ere zue und gaat glichziitig wäg."
     }
    },
    {
     "id": "RCPT-JHN-0014",
     "subject": "TU-JHN-020-024-029",
     "tradition": "art",
     "period_de": "um 1601/02",
     "text_de": "Caravaggio malt den «ungläubigen Thomas»: Jesus führt selbst die Hand des Thomas, der seinen Finger in die Seitenwunde legt; zwei weitere Jünger schauen eng daneben zu. Der Text sagt nicht, ob Thomas Jesus berührt hat ([[JHN.20.27-JHN.20.28]]); das Bild hat diese Lesart stark geprägt.",
     "sources_de": [
      "Caravaggio, «Der ungläubige Thomas», Bildergalerie Sanssouci, Potsdam"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Caravaggio, Der ungläubige Thomas",
        "found_at": "https://en.wikipedia.org/wiki/The_Incredulity_of_Saint_Thomas_(Caravaggio)",
        "finding_de": "Um 1601–1602, Bildergalerie Sanssouci; Thomas legt den Finger in die Seitenwunde, Christus führt seine Hand; zwei weitere Apostel dahinter."
       }
      ]
     },
     "gsw": {
      "period_de": "um 1601/02",
      "text_de": "De Caravaggio malt de «unglöibig Thomas»: De Jesus füert sälber d Hand vom Thomas, wo de Finger i d Siitewunde leit; zwei anderi Jünger lueged nöch dernäbe zue. De Text seit nöd, öb de Thomas de Jesus aaglängt hät ([[JHN.20.27-JHN.20.28]]); s Bild hät die Läsart starch prägt."
     }
    },
    {
     "id": "RCPT-JHN-0015",
     "subject": "TU-JHN-021-001-014",
     "tradition": "church_fathers",
     "period_de": "um 420",
     "text_de": "Augustinus deutet die 153 Fische ([[JHN.21.11]]) als Zahl: 153 ist die Summe aller Zahlen von 1 bis 17, und 17 verbindet die zehn Gebote mit den sieben Gaben des Geistes. Gemeint seien nicht nur 153 Menschen, sondern Tausende, die an der Gnade teilhaben.",
     "sources_de": [
      "Augustinus, Vorträge über das Johannesevangelium (Tractatus in Iohannem) 122,8"
     ],
     "confidence": "high",
     "source_check": {
      "date": "2026-10-28",
      "result": "confirmed",
      "method_de": "KI-Prüfung (Claude): Stellen in frei zugänglichen Ausgaben im Web nachgeschlagen; am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung) erneut nachgeschlagen, Ergebnis unverändert; keine fachliche Prüfung.",
      "checked": [
       {
        "source": "Augustinus, Tractatus in Iohannem 122,8",
        "found_at": "https://www.newadvent.org/fathers/1701122.htm (englische Übersetzung NPNF)",
        "finding_de": "Die Stelle erklärt 153 als Summe von 1 bis 17, 17 als zehn Gebote und siebenfältigen Geist, und sagt, gemeint seien Tausende von Heiligen."
       }
      ]
     },
     "gsw": {
      "period_de": "um 420",
      "text_de": "De Augustinus düütet di 153 Fisch ([[JHN.21.11]]) als Zaal: 153 isch d Summe vo allne Zaale vo 1 bis 17, und 17 verbindet di zää Gebot mit de sibe Gabe vom Geischt. Gmeint seied nöd nu 153 Mänsche, sondern Tuusigi, wo a de Gnad teilhäbed."
     }
    },
]

# Jüdische Stimmen, ergänzt nach der Prüfrunde (2026-10-29; noch nicht von einer weiteren Instanz geprüft)
_COMMON = {"process": "PROC-WEITERDENKEN@1.1", "date": "2026-10-29", "check": None, "authorship_de": "KI-Entwurf (Claude) vom 2026-10-29 (Ergänzung jüdischer Stimmen nach der Prüfrunde, Auftrag Andi Neck); Quelle im Web nachgeschlagen; noch nicht von einer weiteren Instanz geprüft; keine fachliche Prüfung."}
RECEPTIONS += [{**_COMMON, **_x} for _x in [
 {
  "id": "RCPT-JHN-0016",
  "subject": "SUM-BOOK-JHN",
  "tradition": "jewish",
  "period_de": "2001",
  "text_de": "Die jüdische Neutestamentlerin Adele Reinhartz beschreibt in «Befriending the Beloved Disciple» ihr Lesen des Johannesevangeliums als Beziehung zum «Jünger, den Jesus liebte», der im Buch für den Erzähler steht: Sie nimmt ihn nacheinander als Mentor (zustimmendes Lesen), als Gegner (widerständiges Lesen), als Kollegen (wohlwollendes Lesen) und als Anderen (engagiertes Lesen, das die Fremdheit des Textes stehen lässt).",
  "sources_de": [
   "Adele Reinhartz, Befriending the Beloved Disciple. A Jewish Reading of the Gospel of John, New York: Continuum 2001"
  ],
  "confidence": "probable",
  "uncertain_de": "Die vier Lesarten sind nach dem Inhaltsverzeichnis wiedergegeben; das Buch selbst wurde nicht eingesehen.",
  "source_check": {
   "date": "2026-10-29",
   "result": "partly",
   "method_de": "KI-Prüfung (Claude): Angaben in frei zugänglichen Bibliothekskatalogen, Besprechungen bzw. im Wiederabdruck des Artikels nachgeschlagen; das Buch selbst nicht eingesehen, soweit nicht anders vermerkt; keine fachliche Prüfung.",
   "checked": [
    {
     "source": "Adele Reinhartz, Befriending the Beloved Disciple (2001)",
     "found_at": "https://4enoch.org/wiki5/index.php/Befriending_the_Beloved_Disciple_(2001_Reinhartz),_book (Titelangaben und Inhaltsverzeichnis); Bibliothekskatalog https://bibliotekils.johannelund.nu/bib/120531",
     "finding_de": "Titel, Untertitel «A Jewish Reading of the Gospel of John», New York: Continuum 2001 bestätigt; Inhaltsverzeichnis mit den Kapiteln Mentor (compliant reading), Opponent (resistant reading), Colleague (sympathetic reading) und Other (engaged reading)."
    }
   ]
  },
  "gsw": {
   "period_de": "2001",
   "text_de": "Di jüdisch Neutestamentlerin Adele Reinhartz beschriibt i «Befriending the Beloved Disciple» ires Läse vom Johannesevangelium als Beziehig zum «Jünger, wo de Jesus gern gha hät», wo im Buech für de Erzäler staat: Si nimmt en nachenand als Mentor (zuestimmends Läse), als Gägner (widerständigs Läse), als Kolleg (wohlwollends Läse) und als Andere (engagierts Läse, wo d Frömdheit vom Text la staa)."
  }
 },
 {
  "id": "RCPT-JHN-0017",
  "subject": "TU-JHN-009-013-023",
  "tradition": "jewish",
  "period_de": "2018",
  "text_de": "Adele Reinhartz bezweifelt in «Cast Out of the Covenant» die verbreitete These, die Angst vor dem Ausschluss aus der Synagoge ([[JHN.9.22]]) spiegle eine tatsächliche Vertreibung der Gemeinde des Johannes (J. Louis Martyn). Sie liest die Rede von «den Juden» als Mittel, eine neue Gemeinschaft zu bilden, vielleicht vor allem aus Nichtjuden, und ruft christliche Leserinnen und Leser auf, den Antijudaismus des Evangeliums abzulehnen und zu bewahren, was sie darin wertvoll finden.",
  "sources_de": [
   "Adele Reinhartz, Cast Out of the Covenant. Jews and Anti-Judaism in the Gospel of John, Lanham: Lexington Books / Fortress Academic 2018"
  ],
  "confidence": "high",
  "source_check": {
   "date": "2026-10-29",
   "result": "confirmed",
   "method_de": "KI-Prüfung (Claude): Angaben in frei zugänglichen Bibliothekskatalogen, Besprechungen bzw. im Wiederabdruck des Artikels nachgeschlagen; das Buch selbst nicht eingesehen, soweit nicht anders vermerkt; keine fachliche Prüfung.",
   "checked": [
    {
     "source": "Adele Reinhartz, Cast Out of the Covenant (2018)",
     "found_at": "https://readingreligion.org/books/cast-out-covenant (Besprechung, Reading Religion, 2019)",
     "finding_de": "Die Besprechung bestätigt: Kritik an J. Louis Martyns Deutung von Joh 9 als Spiegel einer Vertreibung, Gegenvorschlag einer Rhetorik, die eine neue Gemeinschaft (vielleicht aus Nichtjuden) bildet, und Aufruf an christliche Leser, den Antijudaismus abzulehnen; Verlag Lexington Books."
    }
   ]
  },
  "gsw": {
   "period_de": "2018",
   "text_de": "D Adele Reinhartz bezwiiflet i «Cast Out of the Covenant» di verbreitet These, d Angscht vor em Usschluss us de Synagoge ([[JHN.9.22]]) spiegli e würklichi Vertriibig vo de Gmeind vom Johannes (J. Louis Martyn). Si list d Red vo «de Jude» als Mittel, e nöi Gmeinschaft z bilde, villicht vor allem us Nichtjude, und rüeft chrischtlichi Läserinne und Läser uf, de Antijudaismus vom Evangelium abzlehne und z bhalte, was si drin wärtvoll findet."
  }
 }
]]

# Prüfvermerk der Prüfrunde vom 2026-10-29 (getrennte Instanz; docs/WEITERDENKEN.md, Feld check)
CHECK = {"date": "2026-10-29", "by": "weitere Instanz (KI)", "limits_de": "Nicht gegen den Urtext geprüft, sondern gegen die hochdeutsche und die Mundart-Arbeitsübersetzung (Zitate per Skript wörtlich verglichen); Quellen der Rezeption nur in frei zugänglichen Ausgaben nachgeschlagen; keine fachliche und keine muttersprachliche Prüfung durch eine Person.", "process": "PROC-WEITERDENKEN@1.0"}
# in der Prüfung (oder bei der Zitat-Prüfung am selben Tag) berichtigt
CHECK_CORRECTED = ["RCPT-JHN-0001", "RCPT-JHN-0002", "RCPT-JHN-0003", "RCPT-JHN-0004", "RCPT-JHN-0005", "RCPT-JHN-0006", "RCPT-JHN-0007", "RCPT-JHN-0008", "RCPT-JHN-0009", "RCPT-JHN-0010", "RCPT-JHN-0011", "RCPT-JHN-0012", "RCPT-JHN-0013", "RCPT-JHN-0014", "RCPT-JHN-0015", "REFL-JHN-0006", "REFL-JHN-0007", "REFL-JHN-0021", "REFL-JHN-0029", "REFL-JHN-0030", "REFL-JHN-0067", "REFL-JHN-0074", "REFL-JHN-0082", "REFL-JHN-0091", "REFL-JHN-0100", "REFL-JHN-0118", "REFL-JHN-0123", "REFL-JHN-0124", "REFL-JHN-0125", "REFL-JHN-0134", "REFL-JHN-0135", "REFL-JHN-0136", "REFL-JHN-0140", "REFL-JHN-0146", "REFL-JHN-0151", "REFL-JHN-0155", "REFL-JHN-0157", "REFL-JHN-0176", "REFL-JHN-0183", "REFL-JHN-0185", "REFL-JHN-0187", "REFL-JHN-0189", "REFL-JHN-0196", "REFL-JHN-0201", "REFL-JHN-0202", "REFL-JHN-0208", "REFL-JHN-0215", "REFL-JHN-0219", "REFL-JHN-0229", "REFL-JHN-0245", "REFL-JHN-0247", "REFL-JHN-0249"]
