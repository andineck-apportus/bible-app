# Rumantsch: Grundlagen für Übersetzungsschichten je Idiom

Zweck: Sammlung der schriftlichen Sprachdefinitionen (Schriftnorm, Grammatik, Wörterbuch), der Rechte und der
Bibel-Vorbilder für die fünf rätoromanischen Schriftidiome und Rumantsch Grischun. Daraus entsteht je Idiom ein Regelwerk
wie [ZUERITUEUETSCH.md](ZUERITUEUETSCH.md); übersetzt wird danach wie immer aus dem Urtext (AGENTS.md: eigene
Übersetzungsschicht je Sprache, `language` nach BCP-47: `rm-sursilv`, `rm-sutsilv`, `rm-surmiran`, `rm-puter`,
`rm-vallader`, `rm-rumgr`). Recherche-Entwurf (KI, Claude) vom 2026-11-21 auf Wunsch von Andi Neck; Angaben mit Quelle,
nicht Belegtes als OFFEN. Bibelausgaben nur als Vergleich, nichts übernehmen (LIZENZEN.md).

**Nächste Schritte:** Idiom wählen; Rechte klären (Lia Rumantscha: Pledari Grond je Idiom; Uniun dals Grischs:
Puter/Vallader; Kanton/PH GR: Mediomatix) und Anfragen in [ANFRAGEN.md](ANFRAGEN.md) protokollieren; Grundlagenwerke
beschaffen; Regelwerk und Prüfwerkzeug wie bei Züritüütsch; Pilot aus dem Urtext; muttersprachliche Prüfung vorsehen.

Stand der Recherche: 21. November 2026. Nur belegte Angaben mit Quelle. Was nicht belegt werden konnte, steht als **OFFEN**. Aus geschützten Werken wurde nichts abgeschrieben, es gibt nur bibliografische Angaben und eigene Beschreibungen.

Hinweis zur Methode: Einige Primärseiten waren während der Recherche nicht abrufbar: pledarigrond.ch, das GitHub-Repo `pledari-grond`, die HLS-Artikel, die Engadiner Post und Grünert 2024 (PDF nicht lesbar). Angaben dazu stammen aus Sekundärquellen und sind entsprechend gekennzeichnet.

---

## 0. Überblick und Querschnitt

### 0.1 Wer pflegt heute welche Norm (Kurzfassung)

| Varietät | Heutige Normpflege bzw. massgebliche Referenz | Belege |
|---|---|---|
| Rumantsch Grischun (RG) | Lia Rumantscha (LR) mit dem Pledari Grond. Die Bundeskanzlei stützt sich für die Rechtschreibung auf den Pledari Grond und für Grammatik und Orthographie auf die Grammatica per l'instrucziun (Uni Fribourg). | [BK-Direktiven 2014](https://www.bk.admin.ch/dam/bk/rm/dokumente/sprachdienste/Directivas_texts_rumantschs_02_11_2016.pdf.download.pdf/directivas_texts_rumantschs.pdf) |
| Sursilvan, Sutsilvan, Surmiran | Online-Wörterbücher im Pledari Grond (© Lia Rumantscha). Die Schulgrammatiken «Mediomatix» erscheinen bei Meds d'instrucziun dal Grischun. | [rumlem/PyPI](https://pypi.org/project/rumlem/), [Kanton GR 2017](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2017/Seiten/2017090501.aspx) |
| Puter, Vallader | Online-Wörterbücher und Grammatiken der Uniun dals Grischs (UdG), dazu die Mediomatix-Schulgrammatiken | [Kanton GR 2022](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2022/Seiten/2022050401.aspx), [Portacultura: Grammatica puter 2013](https://portacultura.gr.ch/api/records/KBG-990005413890206696_108346/export) |

- Das kantonale Recht weist die Normpflege **keiner** Institution ausdrücklich zu. Das Sprachengesetz LLing (BR 492.100) und die Sprachenverordnung OLing (BR 492.110) regeln nur Beiträge an LR, Pro Grigioni Italiano und die Fundaziun Medias Rumantschas, und zwar über Leistungsvereinbarungen ([LLing rm](https://www.gr-lex.gr.ch/frontend/versions/3273/download_pdf_file?locale=rm), [OLing rm](https://www.gr.ch/RM/instituziuns/administraziun/ekud/afk/kfg/sprachenfoerderung/Gesetze%20RM/Sprachenverordnung_rm.pdf)).
- Die Leistungsvereinbarungen 2021–2024 mit LR, FMR und PGI umfassen rund 16,4 Mio. CHF vom Bund und 5,7 Mio. CHF vom Kanton ([Kanton GR 10.9.2021](https://www.gr.ch/RM/medias/communicaziuns/MMStaka/2021/Seiten/2021091001.aspx)).
- Gesetzlicher Status von RG: Kantonale Behörden verwenden RG als Standardform. Romanischsprachige dürfen sich in Idiom oder RG an den Kanton wenden ([LLing Art. 3 Abs. 5](https://www.gr-lex.gr.ch/frontend/versions/3273/download_pdf_file?locale=rm)). Auch Bundestexte werden in RG verfasst oder übersetzt (Art. 6 Abs. 3 des Bundes-Sprachengesetzes, zitiert in den [BK-Direktiven](https://www.bk.admin.ch/dam/bk/rm/dokumente/sprachdienste/Directivas_texts_rumantschs_02_11_2016.pdf.download.pdf/directivas_texts_rumantschs.pdf)).

### 0.2 Standardquelle zur Normierungsgeschichte

Georges Darms, «Bündnerromanisch: Sprachnormierung und Standardsprache», *Lexikon der Romanistischen Linguistik* (LRL), Artikel 230, S. 827–845. Der Text ist als PDF frei abrufbar: [scienzarumantscha-darms.ch](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf). Erscheinungsjahr und Band gehen aus dem Auszug nicht hervor, die Bibliografie reicht bis 1987: **OFFEN**. Ergänzend für Surselva und Engadin im 20. Jh.: Matthias Grünert, «Pressesprache und Standardisierung: Engadin und Surselva im 20. Jahrhundert», *Ladinia* XXVI–XXVII (2002–2003), S. 21–40 ([micura.it PDF](https://www.micura.it/dam/media/ladinia/8499.pdf)).

### 0.3 Idiomübergreifende Sprachtechnologie (mit Lizenzen)

| Ressource | Was | Lizenz/Rechte | Quelle |
|---|---|---|---|
| **Pledari Grond** (LR) | Online-Wörterbuch RG (seit 1980 aufgebaut, Druckausgabe 1993, rund 250'000 Einträge). Seit 2015 auch Surmiran und Sutsilvan, inzwischen auch Sursilvan. Die Wörterbücher von Puter und Vallader liefert die UdG. | RG laut de.wikipedia «freie Inhalte» unter einer CC-Lizenz. 2018 nannte opendata.ch für den Export ausdrücklich **CC BY 4.0** (CSV/XML/JSON). Laut rumlem sind RG, Surmiran, Sursilvan und Sutsilvan «openly licensed» (© LR 1980–2025). Die genaue Lizenz je Idiom auf pledarigrond.ch selbst ist **OFFEN**. | [de.wikipedia](https://de.wikipedia.org/wiki/Pledari_Grond), [opendata.ch 2018](https://opendata.ch/events/mehrsprachigkeit-4-0-plurilinguisme-4-0-plurilinguismo-4-0-plurilinguitad-4-0/), [rumlem](https://pypi.org/project/rumlem/) |
| Pledari-Grond-Software | Code für Backend, API und Frontend (farscrl/pledari-grond, pledarigrond-frontend) | Code Apache-2.0. Für die API ist keine Lizenz angegeben. | [github.com/farscrl](https://github.com/farscrl) |
| **UdG-Wörterbücher Puter/Vallader** (udg.ch) | Online seit 2013. 2022 umfassten sie rund 99'000 Einträge (Puter) und 145'000 (Vallader), dazu Konjugationen von etwa 3'400 bzw. 4'000 Verben. Redaktor war bis 2022 Gion Tscharner. | Laut rumlem: «© Uniun dals Grischs. All rights reserved», für rumlem nur im Rahmen des Lemmatisierers freigegeben. Für eine Nutzung muss man **bei der UdG anfragen**. | [Kanton GR 4.5.2022](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2022/Seiten/2022050401.aspx), [rumlem](https://pypi.org/project/rumlem/) |
| **Rechtschreibprüfung** (Pro Svizra Rumantscha und LR) | Sechs Prüfprogramme (5 Idiome und RG), Projektstart 2022. Surmiran kam zuerst und läuft unter macOS, Firefox, LibreOffice, Thunderbird und InDesign. Ausserdem gibt es Firefox-Add-ons für Sutsilvan und RG. | Firefox-Add-on Sutsilvan: **MIT-Lizenz** (Version 2.2.2, Update Sept. 2026). Die übrigen Idiome sind **OFFEN** (vermutlich gleich, aber nicht geprüft). | [Südostschweiz 15.11.2022](https://www.suedostschweiz.ch/leben-freizeit/ein-neues-romanisches-korrekturprogramm-ist-in-den-startloechern-876445), [AMO Sutsilvan](https://addons.mozilla.org/en-US/firefox/addon/spellchecker-sutsilvan), [AMO RG](https://addons.mozilla.org/eu/firefox/addon/spellchecker-rumgr/) |
| Word-Add-in «Program da correctura rumantsch» | Office-Add-in von farscrl | Lizenz nicht angegeben | [github.com/farscrl](https://github.com/farscrl) |
| Microsoft-Korrekturhilfe RG | Seit Office 2010 | proprietär | [Microsoft News CH](https://news.microsoft.com/de-ch/?p=4541) |
| **ALAS** (UZH und LR) | Maschinelle Übersetzung Deutsch ↔ RG und alle fünf Idiome, kostenlos im Web unter alas.liarumantscha.ch (April/Mai 2026). Trainiert u. a. mit Texten von RTR, Zeitungen, Literatur, Schulbüchern, Gemeinden und Kanton. | Modell laut Medien Open Source, aber ohne Lizenzangabe (**OFFEN**). Auf Hugging Face (ZurichNLP) liegt `romansh-nllb-1.3b-ct2`. | [UZH CL Projektseite](https://www.cl.uzh.ch/en/research-groups/texttechnologies/research/machine-translation/romansh-idioms.html), [Netzwoche 17.5.2026](https://www.netzwoche.ch/news/2026-05-17/neues-ki-programm-uebersetzt-in-fuenf-raetoromanische-idiome), [Südostschweiz 28.4.2026](https://www.suedostschweiz.ch/schweiz-und-welt/ki-programm-uebersetzt-erstmals-alle-raetoromanischen-sprachvarianten-2-1643625) |
| **Mediomatix-Korpus** | Paralleles Korpus aus 291 Schulbuchbänden der Mediomatix-Reihe. Insgesamt 207'892 Segmente und 2,16 Mio. Tokens: Sursilvan 513k, Sutsilvan 514k, Surmiran 146k, Puter 495k, Vallader 495k Tokens | **CC BY-NC-SA** (nicht kommerziell). Die Autoren bemühen sich um eine offenere Lizenz. | [arXiv 2508.16371](https://arxiv.org/html/2508.16371v1) |
| **WMT24++-Romansh** | Benchmark mit professionellen Übersetzungen aus dem Deutschen in alle sechs Varietäten, Stichproben von LR-Linguisten geprüft | **Apache 2.0** | [arXiv 2509.03148](https://arxiv.org/html/2509.03148v1) |
| rumlem | Wörterbuchbasierter Lemmatisierer für alle sechs Varietäten, gestützt auf die Pledari-Grond-Daten | Code MIT. Für die Daten gelten die Rechte oben (UdG-Daten nicht frei). | [GitHub rumlem](https://github.com/ZurichNLP/rumlem) |
| romansh-lid | Erkennt, in welcher Varietät ein Text geschrieben ist | **OFFEN** | [UZH CL](https://www.cl.uzh.ch/en/research-groups/texttechnologies/research/machine-translation/romansh-idioms.html) |
| SMS4science | 1'120 SMS (426 Sursilvan, 336 Vallader, 181 Puter, 110 Surmiran, 59 RG, 9 Sutsilvan), Wort für Wort auf RG normalisiert (Pledari Grond) | **OFFEN** | [Normalisierungsdoku UZH 2013](https://sms.linguistik.uzh.ch/_media/03_processing/normalization_roh.pdf) |
| LLM-Pläne der LR / Apertus | Die LR plant ein eigenes rätoromanisches LLM. Apertus (swiss-ai) deckt die Varietäten mit ab. | **OFFEN** | [Netzwoche 11.3.2025](https://www.netzwoche.ch/news/2025-03-11/lia-rumantscha-plant-raetoromanisches-llm), [UZH CL](https://www.cl.uzh.ch/en/research-groups/texttechnologies/research/machine-translation/romansh-idioms.html) |

### 0.4 Historisch-etymologisches Wörterbuch

**Dicziunari Rumantsch Grischun (DRG)**: 1904 gegründet von Robert von Planta und der Societad Retorumantscha. Die erste Lieferung erschien 1939. Herausgeber ist die Societad Retorumantscha in Chur, das Institut wird heute von Ursin Lutz geleitet. Das DRG erfasst den Wortschatz aller bündnerromanischen Mundarten seit dem 16. Jh. Die ersten 13 Bände sind seit Dezember 2018 online (retrodigitalisiert durch das TCDH Trier), unter [online.drg.ch](http://online.drg.ch/) bzw. [idrg.ch](https://idrg.ch). Quellen: [LR Idiome](https://www.liarumantscha.ch/de/raetoromanisch/idiome), [SAGW](https://www.sagw.ch/en/funding/national-dictionaries/dicziunari-rumantsch-grischun), [TCDH](https://tcdh.uni-trier.de/en/projekt/dicziunari-rumantsch-grischun-drg), [en.wikipedia](https://en.wikipedia.org/wiki/Dicziunari_Rumantsch_Grischun). Lizenz der Online-Fassung und aktueller Buchstabe: **OFFEN**. Für uns dient das DRG als Referenz für Etymologie, Belege und Kirchenwortschatz, nicht als Normquelle.

### 0.5 Schulsituation (alle Idiome)

- Lehrmittelreihe **Mediomatix**: Sie wird von der PH Graubünden im Auftrag des Kantons entwickelt und ist für romanische und zweisprachige Schulen obligatorisch. Die **Schulgrammatiken** für Puter, Sursilvan, Sutsilvan und Vallader erschienen Ende Juli 2017 (CHF 12 für Schulen, CHF 16 für Private, lmv.gr.ch). Für Surmiran gibt es Mediomatix ab 2022/23, Folgebände sind bis 2029 geplant ([Kanton GR 2017](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2017/Seiten/2017090501.aspx), [Kanton GR 2020](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2020/Seiten/2020090801.aspx), [Kanton GR 2022](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2022/Seiten/2022083101.aspx), [Lehrmittelverzeichnis 2025/26](https://www.gr.ch/DE/institutionen/verwaltung/ekud/avs/Volksschule/lehrmittelverzeichnis_25-26_rm.pdf)).
- **Rückkehr zu den Idiomen**: 2011 beschloss der Grosse Rat, die Idiome zu unterstützen, und danach kehrten Surselva und Engadin zurück. Surses beschloss am 24.7.2020 die Rückkehr zu Surmiran ([Südostschweiz 25.7.2020](https://www.suedostschweiz.ch/schweiz-und-welt/klares-votum-gegen-rumantsch-grischun-1050145)). Ab Schuljahr 2021/22 führen **Albula/Alvra, Lantsch/Lenz und Surses** Surmiran wieder ein, aufsteigend ab der 1. Klasse ([Kanton GR 17.9.2020](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2020/Seiten/2020091701.aspx)). 2020 hiess es, RG bleibe dann nur noch in den gemischtsprachigen Gemeinden **Chur, Domat/Ems und Trin** ([Südostschweiz 2020](https://www.suedostschweiz.ch/schweiz-und-welt/klares-votum-gegen-rumantsch-grischun-1050145)). Aktueller Stand 2026 in diesen drei Gemeinden: **OFFEN**.
- Das Lehrmittelverzeichnis 2025/26 führt für **alle sechs** Varietäten eigene Erstlesebücher. Für RG sind unter anderem «Verbs e grammatica» und «Sgurdins» aufgeführt ([Verzeichnis 2025/26](https://www.gr.ch/DE/institutionen/verwaltung/ekud/avs/Volksschule/lehrmittelverzeichnis_25-26_rm.pdf)).

### 0.6 Lebendigkeit (alle Idiome)

- **Sprecherzahlen**: In der Strukturerhebung 2024 nannten **12,3 %** der Bündner Wohnbevölkerung ab 15 Jahren Rätoromanisch als Hauptsprache ([Kanton GR Statistik](https://www.gr.ch/DE/institutionen/verwaltung/dvs/awt/statistik/Bevoelkerung/Seiten/Sprache,_Religion.aspx)). 2022 sprachen in Graubünden rund 15 % zu Hause und 11 % bei der Arbeit (auch) Romanisch ([Kanton GR, SE 2022](https://www.gr.ch/DE/institutionen/verwaltung/dvs/awt/statistik/news/Seiten/Strukturerhebung_2022_Sprache.aspx)). Schweizweit waren es 2021 0,5 % mit Hauptsprache Rätoromanisch, gegenüber 1,1 % im Jahr 1910. Nach EDA sprechen rund 60'000 Personen Romanisch, fast 40 % davon leben ausserhalb Graubündens ([EDA aboutswitzerland](https://www.aboutswitzerland.eda.admin.ch/en/allegra-a-look-at-romansh-switzerlands-fourth-language)). Ältere Absolutzahlen: Für 2014 ergibt die Strukturerhebung rund 37'000 Personen mit Hauptsprache Rätoromanisch (Summe der publizierten Teilwerte, [HTW Chur](https://www.fhgr.ch/fileadmin/fhgr/angewandte_zukunftstechnologien/IMP/projekte/Mediennutzungsverhalten_Raetoromanischsprachige/Projekt-Mediennutzungsverhalten-Strukturerhebungen_Raetoromanen.pdf)). **Zahlen je Idiom erhebt das BFS nicht.** Aktuelle Absolutzahlen 2024 und eine Aufteilung nach Idiom: **OFFEN** (allenfalls über Gemeindezugehörigkeit schätzbar).
- **Medien**:
  - RTR ist der romanische Service public ([EDA](https://www.aboutswitzerland.eda.admin.ch/en/allegra-a-look-at-romansh-switzerlands-fourth-language)).
  - *La Quotidiana* wurde 1997 als einzige romanische Tageszeitung gegründet (Somedia). Sie erscheint in den Idiomen und in RG, oft mehr als die Hälfte auf Sursilvan ([en.wikipedia](https://en.wikipedia.org/wiki/La_Quotidiana)). Seit 2023 wird sie nicht mehr am Kiosk verkauft, nur noch im Abo und digital ([Südostschweiz 23.1.2023](https://www.suedostschweiz.ch/schweiz-und-welt/romanische-zeitung-quotidiana-wird-nicht-mehr-am-kiosk-verkauft-860737)). Aktueller Fortbestand 2026: **OFFEN**.
  - *Engadiner Post / Posta Ladina* (Gammeter Media, 3× wöchentlich) hat 2–3 romanische Seiten, etwa 80 % davon auf Vallader und der Rest auf Puter ([dewiki.de](https://dewiki.de/Lexikon/Engadiner_Post)).

---

## 1. Sursilvan

**1 Schriftnorm**
- Protestantische Tradition seit Steffan Gabriel (1611), katholische seit Calvenzano (1615). 1888/89 folgten die «Normas ortograficas» von Muoth, die 1895 für Schulbücher übernommen wurden. 1924 erschien Cahannes' *Grammatica Romontscha per Surselva e Sutselva* (LR), und **1927 wurde die Orthographie festgelegt**. Dieser Stand gilt als Basis der heutigen Norm ([Darms LRL](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf); [Grünert 2002/03](https://www.micura.it/dam/media/ladinia/8499.pdf): Cahannes, *Entruidament davart nossa ortografia*, 1927).
- **Reform 1957–1970**: Die Vereine Romania und Renania beschlossen 1957 eine Reform (Unterscheidung de/da, o/u in unbetonten Silben). Die *Gasetta Romontscha* setzte sie 1958 um und nahm sie im selben Jahr wieder zurück, de/da übernahm sie erst 1970 ([Grünert](https://www.micura.it/dam/media/ladinia/8499.pdf)). Hintergrund war die «avischinaziun miaivla», die sanfte Annäherung der Idiome (Schorta 1962). Die Romania hob ihre Schreibvorgaben 1966 auf ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).
- Ein heutiges offizielles Orthographie-Regelwerk (Titel, Herausgeber, online) wurde **nicht gefunden: OFFEN**. Faktisch wirken die Mediomatix-Schulgrammatik und das Wörterbuch im Pledari Grond als Norm.

**2 Grammatiken**
- *Sursilvan grammatica da scola: far uorden cul lungatg*, Meds d'instrucziun dal Grischun / PH GR, 2017 ([Portacultura](https://portacultura.gr.ch/api/records/KBG-990006795110206696_34474/export)). Schulgrammatik, vom Kanton als obligatorisch erklärt.
- Arnold Spescha, *Grammatica sursilvana*, 1989 (in einer Bibliografie belegt: [langsci .bib](https://langsci-press.org/catalog/view/308/3110/2386-1)). Verlag und ISBN sind **OFFEN**.
- Theo Candinas, *Romontsch sursilvan. Grammatica per emprender igl idiom sursilvan*, LR, Cuera 1982 (Lerngrammatik, auch als Tondokument, [HelveticArchives](https://www.helveticarchives.admin.ch/detail.aspx?ID=913415)).
- Historisch: Cahannes 1924 (s. o.).

**3 Wörterbücher**
- Ramun Vieli / Alexi Decurtins, *Vocabulari romontsch sursilvan–tudestg*, LR 1962 ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).
- Alexi Decurtins, *Niev vocabulari romontsch sursilvan–tudestg*, 2001 ([UZH Normalisierungsdoku](https://sms.linguistik.uzh.ch/_media/03_processing/normalization_roh.pdf)). Online als «Niev Vocabulari Sursilvan» erwähnt ([Grünke/Gerards 2023](https://www.romanistik.uni-mainz.de/files/2023/10/Gruenke_Gerards-2023.pdf)).
- Online im **Pledari Grond**, laut rumlem «openly licensed», © LR ([rumlem](https://pypi.org/project/rumlem/)).
- LR, *Dicziunari vallader – puter – sursilvan*, [2019] ([Portacultura](https://portacultura.gr.ch/api/records/KBG-990007013780206696_104324/export)).

**4 Technik**: Rechtschreibprüfung im Projekt PSR/LR vorgesehen. Für die Plattformen ist der Stand **OFFEN**. Sursilvan ist in ALAS, Mediomatix (513k Tokens) und WMT24++ enthalten, siehe 0.3.

**5 Bibel/Kirche**
- Luci Gabriel, Neues Testament 1648 ([en.wikipedia](https://en.wikipedia.org/wiki/Bible_translations_into_Romansh)). Die *Bibla da Cuera* (1717–1719) ist laut Wikipedia die erste Vollbibel. Dass sie in Sursilvan geschrieben ist, steht dort nicht ausdrücklich: **OFFEN** (zu prüfen).
- **Bibla romontscha ecumena** (katholisch und reformiert gemeinsam, aus Hebräisch, Aramäisch und Griechisch, Arbeit seit 1968, 5 Bände geplant):
  - NT 1988, Propheten 2004, Psalmen 2010 ([die-bibel.ch](https://www.die-bibel.ch/die-bibel-in-romanischer-sprache/))
  - Band 3, poetische Bücher (Ijob, Psalmen, Sprüche, Kohelet, Hoheslied, Weisheit, Sirach), 2014: Decanat, 680 S., ISBN 978-3-033-04689-4 ([LR-Shop](https://www.liarumantscha.ch/rm/butia/cudeschs/cudeschs-tematics/bibla-romontscha-ecumena-veder-testament--978-3-033-04689-4))
  - **Band 4, Pentateuch**, vorgestellt am **8.12.2022**. Übersetzt von Martin Fontana, Giusep Venzin, Anja Felix-Candrian und Andri Casanova ([Fundaziun Anton Cadonau](https://fundaziun-anton-cadonau.ch/tgei-fagein-nus/))
  - Damit fehlen noch die **Geschichtsbücher des AT (Band 5)**. Ob dieser Band inzwischen erschienen und die Bibel damit **vollständig** ist: **OFFEN** (kein Beleg gefunden; SRF schätzte 2018 noch «etwa zehn Jahre» Arbeit, [SRF 28.4.2018](https://www.srf.ch/kultur/gesellschaft-religion/bibel-uebersetzung-ein-pfarrer-wagt-eine-sprachliche-gratwanderung)).
  - Rechte: Die Bände sind urheberrechtlich geschützt und dürfen nur zum Vergleich genutzt werden. Für mehr müsste man die Herausgeber (Decanat bzw. Kirchen) anfragen.
- Die JW Online Library gibt es auch auf Sursilvan, © Watch Tower ([wol.jw.org](https://wol.jw.org/rm-x-rhs/wol/h/r1105/lp-rhs)). Konfessionell gebunden und nicht als Vorbild geeignet.
- Gesangbuch: Renania, *Canzuns religiusas* ([LR-Shop Religiun](https://www.liarumantscha.ch/de/butia/cudeschs/cudeschs-tematics/religiun-e-cretta)). Offizielle katholische und reformierte Gesangbücher und Katechismen: **OFFEN**.

**6 Lebendigkeit**: Sursilvan ist das Idiom mit den meisten Sprechenden. Mehr als die Hälfte der Artikel in *La Quotidiana* sind oft auf Sursilvan ([en.wikipedia](https://en.wikipedia.org/wiki/La_Quotidiana)). Die Schule ist wieder auf dem Idiom (Surselva ist zurückgekehrt, [Südostschweiz 2020](https://www.suedostschweiz.ch/schweiz-und-welt/klares-votum-gegen-rumantsch-grischun-1050145)).

---

## 2. Sutsilvan

**1 Schriftnorm**
- Bis ins 20. Jh. gab es keine eigene Norm, geschrieben wurde in der (protestantischen) surselvischen Variante. **1944** legte Giuseppe Gangale im Rahmen der Acziun Sutselva Rumantscha die *Reglas digl rumantsch da Sutselva* vor (Cuera), überarbeitet bis 1949 (*Antruvidament*). Eine **Schreibrevision von 1963** zwang zur Umordnung des Wörterbuchs ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf); ebenso [WMT24++-Paper](https://arxiv.org/html/2509.03148v1)).
- Ein heutiges offizielles Regelwerk und die Stelle, die es pflegt: **OFFEN**. Faktisch wirken die Mediomatix-Schulgrammatik und das Pledari Grond Sutsilvan als Norm.

**2 Grammatiken**
- *Sutsilvan gramatica da scola: far urden cugl lungatg*, Meds d'instrucziun dal Grischun / PH GR, 2017 ([Portacultura](https://portacultura.gr.ch/api/records/KBG-990006795130206696_34476/export)).
- Conforti / Cusimano / Tscharner, *An lingia directa 1 – Egn curs da rumàntsch sutsilvan*, LR 1997–98 (Lehrgang, [en.wikipedia](https://en.wikipedia.org/wiki/Sutsilvan_dialects_(Romansh))).
- Eine wissenschaftliche Referenzgrammatik: **OFFEN** (nicht gefunden).

**3 Wörterbücher**
- Curo Mani, *Pledari sutsilvan rumàntsch–tudestg, tudestg–rumàntsch*, LR 1977 ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).
- Wolfgang Eichenhofer (Hg.), *Pledari sutsilvan–tudestg*, Lehrmittelverlag GR 2002 ([en.wikipedia](https://en.wikipedia.org/wiki/Sutsilvan_dialects_(Romansh)); die UZH-Doku nennt 2009, [UZH](https://sms.linguistik.uzh.ch/_media/03_processing/normalization_roh.pdf)). Die Jahresangabe ist widersprüchlich: **OFFEN**.
- Online im Pledari Grond (seit 2015), laut rumlem «openly licensed» ([de.wikipedia](https://de.wikipedia.org/wiki/Pledari_Grond), [rumlem](https://pypi.org/project/rumlem/)).

**4 Technik**: Firefox-Rechtschreibprüfung Sutsilvan (PSR, **MIT-Lizenz**) ([AMO](https://addons.mozilla.org/en-US/firefox/addon/spellchecker-sutsilvan)). Mediomatix-Korpus mit 514k Tokens. In WMT24++ war Sutsilvan bei Einreichung unvollständig (678 von 998 Segmenten) ([arXiv](https://arxiv.org/html/2509.03148v1)).

**5 Bibel/Kirche**: Ein Katechismus für die Schule ist für 1601 belegt ([en.wikipedia](https://en.wikipedia.org/wiki/Sutsilvan_dialects_(Romansh))). Eine Bibel oder ein NT auf Sutsilvan: **OFFEN** (nicht gefunden).

**6 Lebendigkeit**: Gesprochen in Domleschg, Heinzenberg, Schams und Val Ferrera ([en.wikipedia](https://en.wikipedia.org/wiki/Sutsilvan_dialects_(Romansh))). Sprecherzahl: **OFFEN** (im SMS-Korpus nur 9 von 1'120 SMS, [UZH](https://sms.linguistik.uzh.ch/_media/03_processing/normalization_roh.pdf)).

---

## 3. Surmiran

**1 Schriftnorm**
- 1897 beauftragte die Lehrerkonferenz Oberhalbstein G. G. Candreia mit Schreibnormen. 1899 erschien das erste offizielle Schulbuch, 1903 ein Lesebuch mit Regeln. Die Normen selbst wurden nicht publiziert.
- **1939**: Battaglia / Grisch, *Normas ortograficas per igl rumantsch da Surmeir* (Tagblatt Coira, von der LR finanziert).
- **1987**: Faust Signorell, *Normas surmiranas. Grammatica rumantscha digl idiom da Sur- e Sotses*, kantonaler Lehrmittelverlag. Diese Normen nähern sich teilweise anderen Idiomen und RG an ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).
- Ob seit 1987 eine Neuregelung erfolgt ist und wer die Norm heute pflegt (Uniun Rumantsch Grischun Central?): **OFFEN**.

**2 Grammatiken**
- Signorell 1987, *Normas surmiranas* (Norm und Grammatik in einem, s. o.).
- Mediomatix Surmiran, Meds d'instrucziun dal Grischun, 2023, 4 Bände und 2 Beilagen, ISBN 9783038471233 ([Portacultura](https://portacultura.gr.ch/api/records/KBG-997922021006696_35834/export)). Die Schulgrammatik ist Teil der Reihe ([Kanton GR 2022](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2022/Seiten/2022083101.aspx)). Eigenständiger Grammatik-Titel: **OFFEN**.

**3 Wörterbücher**
- Ambros Sonder / Mena Grisch, *Vocabulari da Surmeir*, LR 1970 ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).
- Faust Signorell (Hg.), Surmiran-Wörterbuch 1999 bzw. 2001. Die Quelle nennt beide Jahre ([UZH](https://sms.linguistik.uzh.ch/_media/03_processing/normalization_roh.pdf)). Genauer Titel und Jahr: **OFFEN**.
- Online im Pledari Grond (seit 2015), «openly licensed» ([de.wikipedia](https://de.wikipedia.org/wiki/Pledari_Grond), [rumlem](https://pypi.org/project/rumlem/)).

**4 Technik**: Surmiran war 2022 das **erste** fertige Prüfprogramm (PSR/LR) ([Südostschweiz](https://www.suedostschweiz.ch/leben-freizeit/ein-neues-romanisches-korrekturprogramm-ist-in-den-startloechern-876445)). Im Mediomatix-Korpus ist Surmiran mit nur 146k Tokens vertreten, weil die Lehrmittel noch im Aufbau sind ([arXiv](https://arxiv.org/html/2508.16371v1)).

**5 Bibel/Kirche**: Frühe Texte sind belegt: eine Bellarmin-Übersetzung von 1703 und die Vaz-Handschrift von 1673 ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)). Auch der Kapuziner Alexander Lozza schrieb auf Surmiran ([en.wikipedia](https://en.wikipedia.org/wiki/Surmiran_dialect)). Eine Bibel oder ein NT auf Surmiran: **OFFEN**.

**6 Lebendigkeit**: Gesprochen in Surmeir (Oberhalbstein/Surses und Albulatal). In der Schule wird seit 2021/22 in Surses, Albula/Alvra und Lantsch/Lenz wieder Surmiran statt RG unterrichtet ([Kanton GR 2020](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2020/Seiten/2020091701.aspx)).

---

## 4. Puter (Oberengadin)

**1 Schriftnorm**
- Zaccaria Pallioppi, *Ortografia et ortoepia*, 1857, früh allgemein anerkannt ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)). Die schriftliche Tradition reicht bis 1552 zurück ([arXiv](https://arxiv.org/html/2509.03148v1)).
- **1920**: N. L. Gisep, *Ortografia ladina* (Kompromiss, getragen von UdG und Cussagl ladin).
- **1928**: Bardola, *Pitschna introducziun a la nouva ortografia ladina ufficiala*, von der Regierung sanktioniert und für das ganze Engadin gültig ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf), [Grünert](https://www.micura.it/dam/media/ladinia/8499.pdf)).
- Spätere Änderungen und ein heutiges offizielles Regelwerk: **OFFEN**. Faktisch gelten heute die UdG-Grammatik bzw. das UdG-Wörterbuch und Mediomatix als Norm.

**2 Grammatiken**
- Gian Paul Ganzoni, *Grammatica ladina* (Puter), 1977 ([Grünert](https://www.micura.it/dam/media/ladinia/8499.pdf)). Verlag: vermutlich LR, aber **OFFEN**.
- Gion Tscharner (Hg.), *[Grammatica puter]*, Uniun dals Grischs 2013 ([Portacultura](https://portacultura.gr.ch/api/records/KBG-990005413890206696_108346/export)). Ein PDF «Grammatica puter» mit Verben, Zahlwörtern, Zeichensetzung, Aussprache und Akzenten liegt öffentlich auf einem Uni-Fribourg-Server ([PDF](https://webapps.unifr.ch/guides/de/assets/users/_moritz.sommet/Grammatica_puter.pdf)). Ob es mit der Ausgabe von 2013 identisch ist und welche Rechte gelten: **OFFEN**.
- Mediomatix-Schulgrammatik Puter, 2017 ([Kanton GR](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2017/Seiten/2017090501.aspx)).
- Historisch: Pallioppi, *La conjugaziun del verb* (1868), Velleman, *Grammatica* (1915) ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).

**3 Wörterbücher**
- Gion Tscharner, *Dicziunari puter–tudais-ch*, 2007 ([UZH](https://sms.linguistik.uzh.ch/_media/03_processing/normalization_roh.pdf)).
- **UdG online** (udg.ch, seit 2013): rund 99'000 Einträge und 3'400 konjugierte Verben (2022) ([Kanton GR](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2022/Seiten/2022050401.aspx)). **Alle Rechte bei der UdG** ([rumlem](https://pypi.org/project/rumlem/)).
- Historisch: E. Pallioppi, *Dizionari* (1895), Velleman, *Dicziunari scurznieu* (1929), Bezzola/Tönjachen (Arbeit ab 1924) ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).

**4 Technik**: PSR/LR-Prüfprogramm Puter «online und in Word» (laut Titel einer [rumantsch.ch-Seite](https://www.rumantsch.ch/pro-svizra-rumantscha/nov-program-da-correctura-per-puter-rumantsch-grischun-e-vallader-online-ed-en-word/); der abrufbare Inhalt betraf die Aussprachefunktion, daher ist der Stand **OFFEN**). Puter wird von Klassifikatoren oft als Vallader erkannt: 172 Puter-Segmente wurden als Vallader klassiert ([arXiv](https://arxiv.org/html/2509.03148v1)). Das ist ein Hinweis darauf, dass Normunterschiede im Regelwerk scharf gefasst werden müssen.

**5 Bibel/Kirche**
- Jachiam Bifrun, NT 1560 ([en.wikipedia](https://en.wikipedia.org/wiki/Bible_translations_into_Romansh)). Dass Bifrun auf Oberengadinisch schrieb, ist dort nicht ausdrücklich belegt: **OFFEN**.
- *Il Nouv Testamaint*, 2. Auflage, Samaden 1883, British and Foreign Bible Society, 459 S. ([DDB](https://www.deutsche-digitale-bibliothek.de/item/IM7JFM3TB7XPDNZPLXCSEN65LGOKQ7OO?lang=en)).
- Die Bibel von 1953 (Filli/Gaudenz) wird als **«ladinisch» für Ober- und Unterengadin** bezeichnet ([Valsot ref.](https://valsot-ref.ch/aktuelles/bibla-rumantscha)). Der LR-Shop führt sie jedoch als Vallader, siehe 5. Eine eigene moderne Puter-Bibel: **nicht gefunden (OFFEN)**.

**6 Lebendigkeit**: In der *Posta Ladina* ist etwa 20 % der romanischen Artikel auf Puter ([dewiki.de](https://dewiki.de/Lexikon/Engadiner_Post)). Die Schule ist wieder auf dem Idiom ([Südostschweiz 2020](https://www.suedostschweiz.ch/schweiz-und-welt/klares-votum-gegen-rumantsch-grischun-1050145)).

---

## 5. Vallader (Unterengadin, Val Müstair)

**1 Schriftnorm**
- Frühe Schreibtraditionen: Chiampel 1562, Toutsch 1613, Bibla da Scuol 1679.
- **1920** Gisep und **1928** Bardola (offizielle ladinische Orthographie, wie bei Puter).
- 1957 Kommissionsbeschlüsse zur o-Schreibung im Unterengadin.
- 1964: Jachen Curdin Arquint, *Vierv ladin* (LR). Arquint schlug darin weitere Annäherungen an das gesprochene Vallader vor, die nur teilweise übernommen wurden ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf), [Grünert](https://www.micura.it/dam/media/ladinia/8499.pdf)).
- Ein heutiges offizielles Regelwerk: **OFFEN**. Faktisch gelten die UdG-Grammatik und das UdG-Wörterbuch.

**2 Grammatiken**
- Gian Paul Ganzoni, *Grammatica ladina* (Vallader), 1983 ([Grünert](https://www.micura.it/dam/media/ladinia/8499.pdf); die Forschung zitiert sie weiterhin als Regelquelle, [Grünke/Gerards 2023](https://www.romanistik.uni-mainz.de/files/2023/10/Gruenke_Gerards-2023.pdf)).
- *Grammatica vallader* (UdG/Tscharner?): Ein PDF liegt auf einem Uni-Fribourg-Server ([PDF](https://webapps.unifr.ch/guides/de/assets/users/_moritz.sommet/Grammatica_vallader.pdf)). Herausgeber und Jahr: **OFFEN**.
- Mediomatix-Schulgrammatik Vallader, 2017 ([Kanton GR](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2017/Seiten/2017090501.aspx)).
- Arquint, *Vierv ladin* (1964). Historisch: Andeer, *Rhaetoromanische Elementargrammatik* (1880, Neuauflagen 1906 und 1918) ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).
- Grünke/Gerards stellen fest, dass deskriptive Grammatiken weitgehend fehlen.

**3 Wörterbücher**
- Oscar Peer, *Dicziunari rumantsch ladin–tudais-ch*, LR 1962 ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).
- Gion Tscharner, *Dicziunari vallader–tudaisch*, 2009 ([UZH](https://sms.linguistik.uzh.ch/_media/03_processing/normalization_roh.pdf)).
- **UdG online**: rund 145'000 Einträge und 4'000 konjugierte Verben (2022), **alle Rechte bei der UdG** ([Kanton GR](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2022/Seiten/2022050401.aspx), [rumlem](https://pypi.org/project/rumlem/)).

**4 Technik**: Prüfprogramm (PSR/LR) wie bei Puter: **OFFEN**. Im Mediomatix-Korpus mit 495k Tokens. Mozilla Common Voice enthält Audioaufnahmen auf Vallader und Sursilvan ([Grünke/Gerards](https://www.romanistik.uni-mainz.de/files/2023/10/Gruenke_Gerards-2023.pdf)).

**5 Bibel/Kirche**
- **1679 *La Sacra Bibla*** (Bibla da Scuol): Jacob Dorta und Jachen Anton Vulpi, stark an Diodati (1607) angelehnt, 1674 von der Synode genehmigt ([King's College London](https://kingscollections.org/exhibitions/specialcollections/bible/european-bible/swiss-romansch-bible)).
- **1953 *Bibla – La Soncha Scrittüra, Vegl e Nouv Testamaint*** von Rudolf Filli und Jachen Ulrich Gaudenz, 1'604 S. Sie ist die **einzige moderne Vollbibel im Engadin** (Nachdruck 1980). Ein weiterer Nachdruck erschien 2022 bei Ils Colloquis d'Engiadina, ISBN 978-3-033-08861-0, CHF 31; erhältlich auch über Pro Bibla Rumantscha (gr-ref.ch). Vor dem Nachdruck wurde darüber diskutiert, ob man neu übersetzen, die Sprache anpassen oder auf RG umsteigen soll. Man entschied sich für den Nachdruck ([LR-Shop](https://www.liarumantscha.ch/rm/butia/cudeschs/cudeschs-tematics/bibla--978-3-033-08861-0), [Valsot ref.](https://valsot-ref.ch/aktuelles/bibla-rumantscha)). Eine **ökumenische oder neuere Engadiner Übersetzung wurde nicht gefunden: OFFEN**.
- Reformierte Texte: Jäger/Bezzola, *Cretta refuormada* (Vallader, vergriffen) ([LR-Shop](https://www.liarumantscha.ch/de/butia/cudeschs/cudeschs-tematics/religiun-e-cretta)). Ein Gesangbuch: **OFFEN**.
- Rechte: Die Ausgabe von 1953 ist urheberrechtlich geschützt (Übersetzer bzw. Colloquis). Sie darf nur zum Vergleich genutzt werden, für mehr muss man anfragen.

**6 Lebendigkeit**: In der *Posta Ladina* ist etwa 80 % der romanischen Artikel auf Vallader ([dewiki.de](https://dewiki.de/Lexikon/Engadiner_Post)). Die Schule ist wieder auf dem Idiom.

---

## 6. Rumantsch Grischun (RG)

**1 Schriftnorm**
- **1982**: Heinrich Schmid, *Richtlinien für die Gestaltung einer gesamtbündnerromanischen Schriftsprache Rumantsch Grischun*, LR ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf), [LR Idiome](https://www.liarumantscha.ch/de/raetoromanisch/idiome)). Ob die Richtlinien online verfügbar sind: **OFFEN**.
- **1985**: Darms / Dazzi / Gross, *Pledari rumantsch grischun–tudestg, tudestg–rumantsch grischun e Grammatica elementara dal rumantsch grischun*, LR ([Darms](https://scienzarumantscha-darms.ch/wp-content/uploads/2017/01/Buendnerrom.pdf)).
- Heute ist die Rechtschreibung durch den **Pledari Grond** (LR) geregelt. Für Grammatik und Orthographie (Grossschreibung §314–318, Worttrennung §319–321, Komma §322–326) gilt die *Grammatica per l'instrucziun* ([BK-Direktiven 2014](https://www.bk.admin.ch/dam/bk/rm/dokumente/sprachdienste/Directivas_texts_rumantschs_02_11_2016.pdf.download.pdf/directivas_texts_rumantschs.pdf)). Die Bundeskanzlei hat dazu eigene Direktiven erlassen (Redaktion und Übersetzung) sowie Richtlinien zum inklusiven Sprachgebrauch ([BK](https://www.bk.admin.ch/dam/bk/rm/dokumente/sprachdienste/Directivas%20per%20in%20diever%20inclusiv%20dal%20rumantsch.pdf.download.pdf/Directivas%20per%20in%20diever%20inclusiv%20dal%20rumantsch.pdf)).

**2 Grammatiken**
- Renzo Caduff / Uorschla N. Caprez / Georges Darms, ***Grammatica d'instrucziun dal rumantsch grischun***, Seminari da rumantsch, Uni Fribourg, Ausgabe 2006 (SNF-gefördert). Die BK zitiert eine Ausgabe von 2009. **Frei als PDF** verfügbar, die Nutzung von Teilen ist mit Quellenangabe ausdrücklich erlaubt ([PDF 2006](https://webapps.unifr.ch/guides/de/assets/users/_moritz.sommet/Grammaticadinstrucziundalrumantschgrischun_2006.pdf)). Dazu gibt es Teilbände «Grammatica RG 4 Furmaziun da pleds» (2007) und «5 Sintaxa» (2008) ([PDF 4](https://webapps.unifr.ch/guides/de/assets/users/_moritz.sommet/Grammaticarg_4_FurmaziundaPleds_2007.pdf), [PDF 5](https://webapps.unifr.ch/guides/de/assets/users/_moritz.sommet/Grammaticarg_5_Sintaxa_2008.pdf)).
- Schule: *Verbs e grammatica*, *Sgurdins* ([Verzeichnis 2025/26](https://www.gr.ch/DE/institutionen/verwaltung/ekud/avs/Volksschule/lehrmittelverzeichnis_25-26_rm.pdf)).

**3 Wörterbücher**: Pledari Grond (rund 250'000 Einträge, CC, Export 2018 unter CC BY 4.0), siehe 0.3.

**4 Technik**: Bisher am besten ausgebaut: Firefox-Add-on RG (PSR), Microsoft-Office-Korrektur seit 2010 und eine Wortfrequenzliste im An Crúbadán mit rund 3,8 Mio. Wörtern ([Grünke/Gerards](https://www.romanistik.uni-mainz.de/files/2023/10/Gruenke_Gerards-2023.pdf)).

**5 Bibel/Kirche**: Eine Bibel in RG: **nicht gefunden (OFFEN)**. Die Bibla ecumena wählte bewusst Sursilvan, weil RG von niemandem als Erstsprache gesprochen und in Gottesdienst und Unterricht nicht verwendet wird ([die-bibel.ch](https://www.die-bibel.ch/die-bibel-in-romanischer-sprache/)). Beim Nachdruck der Engadiner Bibel wurde RG verworfen ([Valsot ref.](https://valsot-ref.ch/aktuelles/bibla-rumantscha)). Die Seite *bibla-en-rumantsch.ch* ist eine private «experimentelle» Übersetzung von Rico Loosli («alle Rechte vorbehalten», Varietät und Quelltext nicht angegeben, Links zu jw.org) ([Seite](https://www.bibla-en-rumantsch.ch/)). **Als Referenz ungeeignet.**

**6 Lebendigkeit**: RG ist Amtssprache von Bund und Kanton. In der Schule wird RG nur noch in wenigen gemischtsprachigen Gemeinden verwendet (Stand 2020, siehe 0.5).

---

## 7. Empfehlung: Grundlagen je Idiom (analog «Gallmann + Schreibempfehlung»)

Prinzip: **Wörterbuch** (Schreibung, Wortschatz) + **Grammatik** (Formen, Satzbau) + **Orthographie- und Stilvorgabe**. Die Bibelsprache dient nur als Terminologie-Vergleich.

| Idiom | Normquelle Schreibung/Wortschatz | Grammatik | Orthographie/Stil | Kaufen / anfragen / frei |
|---|---|---|---|---|
| Sursilvan | Pledari Grond Sursilvan (online, «offen», © LR) | Mediomatix *Sursilvan grammatica da scola* (2017), dazu Spescha *Grammatica sursilvana* (1989) für die Tiefe | Kein eigenes Regelwerk gefunden. Mediomatix verwenden, die Regeln von 1927 und 1970 aus Darms und Grünert nachvollziehen | **Kaufen**: Mediomatix (lmv.gr.ch), Spescha (antiquarisch?), Decurtins 2001. **Anfragen**: LR wegen Lizenz und Export der Pledari-Daten |
| Sutsilvan | Pledari Grond Sutsilvan, Eichenhofer *Pledari* | Mediomatix *Sutsilvan gramatica da scola* (2017) | Gangale 1944/49 und Revision 1963 (historisch). Heute de facto Mediomatix | **Kaufen**: Mediomatix, Eichenhofer. **Anfragen**: LR. Frei: Hunspell-Wortliste (MIT) |
| Surmiran | Pledari Grond Surmiran | Signorell *Normas surmiranas* (1987) und Mediomatix Surmiran (2023) | Signorell 1987 | **Kaufen**: Mediomatix, Signorell (antiquarisch?), Vocabulari. **Anfragen**: LR, eventuell Uniun Rumantsch Grischun Central |
| Puter | UdG-Dicziunari (online, Rechte bei UdG) | UdG/Tscharner *Grammatica puter* (2013), Mediomatix Puter, Ganzoni 1977 | Bardola 1928 (historisch). Heute UdG | **Anfragen bei der UdG** (zwingend, wenn Daten maschinell genutzt werden sollen). **Kaufen**: Mediomatix, Tscharner *Dicziunari puter* 2007 |
| Vallader | UdG-Dicziunari (Rechte bei UdG) | Ganzoni 1983, UdG *Grammatica vallader*, Mediomatix Vallader | wie Puter, dazu Arquint *Vierv ladin* 1964 | wie Puter. **Kaufen**: Tscharner 2009 |
| RG | Pledari Grond (CC BY) | *Grammatica d'instrucziun* (Uni FR, **frei**) | BK-Direktiven (**frei**) und Grammatica §314–326 | Weitgehend **frei**. Am besten belegt, aber als Bibelsprache nicht akzeptiert |

Praktische Hinweise:
1. **Mediomatix** ist für Sursilvan, Sutsilvan, Surmiran, Puter und Vallader die einzige einheitliche, aktuelle und kantonal verbindliche Grammatikreihe. Sie eignet sich als gemeinsamer Ausgangspunkt für fünf parallele Regelwerke. Die Schulgrammatiken kosten je CHF 16 (Privatpreis 2017). Für eine maschinelle Nutzung (Korpus) gilt derzeit nur **CC BY-NC-SA**. Für eine kommerzielle App wäre deshalb eine Anfrage beim Kanton bzw. bei Meds d'instrucziun und der PH GR nötig.
2. **Daten**: Für RG, Sursilvan, Sutsilvan und Surmiran ist ein Import der Pledari-Grond-Daten mit Quellenangabe vermutlich zulässig (CC). Die genaue Lizenz je Idiom sollte man bei der LR schriftlich bestätigen lassen. Für **Puter und Vallader** ist ein Import **ohne Vereinbarung mit der UdG nicht zulässig**.
3. **Übersetzung**: ALAS (UZH/LR) ist der aktuelle Stand der Technik für alle sechs Varietäten und eignet sich als Vergleichsmodell oder Prüfinstanz. Die Lizenz ist zu klären.
4. **Bibel-Terminologie**: Für Sursilvan ist die Bibla romontscha ecumena die massgebliche ökumenische Referenz (aus dem Urtext übersetzt). Für Puter und Vallader ist es die Bibla von 1953. Für Surmiran, Sutsilvan und RG gibt es keine Bibel als Vorbild, dort muss die Terminologie aus Sursilvan bzw. Vallader und den Wörterbüchern abgeleitet werden. Alle Bibelausgaben dienen nur zum Vergleich und werden nicht kopiert.

---

## 8. Übersichtstabelle je Idiom

| Idiom | Norm (Entstehung → heute) | Grammatik | Wörterbuch | Bibel | Rechte |
|---|---|---|---|---|---|
| Sursilvan | Muoth 1888/89 → Cahannes 1924/1927 → Reform 1957–1970 → heute de facto Mediomatix + Pledari Grond | Mediomatix 2017; Spescha 1989; Candinas 1982 | Vieli/Decurtins 1962; Decurtins 2001; Pledari Grond online | NT Gabriel 1648; **Bibla romontscha ecumena**: NT 1988, Propheten 2004, poetische Bücher 2014, Pentateuch 2022; Geschichtsbücher OFFEN | Pledari «offen» (© LR); Bibel und Grammatiken geschützt |
| Sutsilvan | Gangale 1944/49 → Revision 1963 → heute Mediomatix + Pledari Grond | Mediomatix 2017; Lehrgang *An lingia directa* 1997/98 | Mani 1977; Eichenhofer 2002 (?); Pledari Grond | Katechismus 1601; Bibel OFFEN | Pledari «offen»; Hunspell MIT |
| Surmiran | Candreia 1897–1903 → Battaglia/Grisch 1939 → Signorell 1987 | Signorell 1987; Mediomatix 2023 | Sonder/Grisch 1970; Signorell 1999/2001; Pledari Grond | Bibel OFFEN | Pledari «offen» |
| Puter | Pallioppi 1857 → Gisep 1920 → Bardola 1928 (offiziell) → heute UdG | Ganzoni 1977; UdG/Tscharner 2013; Mediomatix 2017 | Pallioppi 1895; Tscharner 2007; UdG online (99k) | Bifrun NT 1560; NT Samedan 1883; Bibla 1953 (ladinisch, OFFEN, ob sie für Puter gilt) | UdG: alle Rechte vorbehalten |
| Vallader | Gisep 1920 → Bardola 1928 → Arquint 1964 → heute UdG | Ganzoni 1983; UdG Grammatica vallader; Mediomatix 2017 | Peer 1962; Tscharner 2009; UdG online (145k) | Bibla da Scuol 1679; **Bibla 1953** (Filli/Gaudenz; Nachdruck 2022) | UdG: alle Rechte vorbehalten; Bibel geschützt |
| RG | Schmid 1982 → Pledari/Grammatica elementara 1985 → Pledari Grond | Grammatica d'instrucziun (Uni FR 2006/2009, **frei**) | Pledari Grond (≈250k, CC BY) | keine | weitgehend frei (CC BY, Quellenangabe) |

---

## 9. Offene Punkte

1. **Lizenz des Pledari Grond je Idiom**: Die genaue CC-Version und ob ein aktueller Export bzw. eine API frei ist, liess sich nicht prüfen, weil pledarigrond.ch und das Repo nicht abrufbar waren. Bei der LR schriftlich anfragen.
2. **UdG-Daten Puter/Vallader**: Bedingungen für Lizenz und Kauf direkt bei der Uniun dals Grischs erfragen.
3. **Mediomatix**: Rechte für eine kommerzielle bzw. maschinelle Nutzung beim Kanton (AVS), bei Meds d'instrucziun und der PH GR klären. Ausserdem ist offen, ob es einzelne Grammatikbände für Surmiran gibt.
4. **Heutige offizielle Orthographie-Regelwerke** der fünf Idiome (Titel, Herausgeber, online) wurden nicht gefunden. Klären, ob die LR, die regionalen Vereine (Romania/Renania, Uniun Rumantsch Grischun Central, UdG) oder der Kanton eine verbindliche Fassung führen.
5. **Bibla romontscha ecumena**: Ist Band 5 (Geschichtsbücher) erschienen, ist die Bibel also vollständig? Anfrage bei der Fundaziun Anton Cadonau bzw. beim Decanat.
6. **Engadin**: Gibt es nach 1953 eine neuere, eventuell ökumenische Übersetzung (Teile, NT) in Puter oder Vallader? Gilt die Bibla 1953 sprachlich als Vallader oder als «ladinisch» für beide Idiome? Die Quellen widersprechen sich.
7. **Bibeltexte in Surmiran und Sutsilvan**: Nichts gefunden. Bei den Landeskirchen nachfragen (Perikopen, Lektionare).
8. **Liturgie, Gesangbücher, Katechismen** je Idiom und Konfession: nicht systematisch belegt. Nachfragen beim Bistum Chur und bei der Evangelisch-reformierten Landeskirche Graubünden.
9. **Sprecherzahlen**: Absolutzahlen 2024 (BFS-Tabelle «Hauptsprache GR und CH 2010–2024») und eine Schätzung je Idiom (BFS erhebt keine Idiome).
10. **RG in der Schule 2026**: Ist RG in Chur, Domat/Ems und Trin noch Alphabetisierungssprache?
11. **La Quotidiana**: Erscheint sie 2026 noch? Hinweise auf eine drohende Einstellung gibt es (Swissinfo/Swiss Revue), der Inhalt war nicht abrufbar.
12. **Bibliografische Details**: Verlag und Jahr bei Spescha 1989 und Ganzoni 1977/1983, Titel und Jahr bei Signorell 1999/2001, Eichenhofer 2002 vs. 2009, Band und Jahr des LRL-Artikels von Darms, Herausgeber und Rechte der PDFs «Grammatica puter/vallader» auf dem Server der Uni Fribourg.
13. **Lizenzen der ALAS-Modelle** und von romansh-lid auf Hugging Face/GitHub.
14. **Rechtschreibprüfung**: Stand für Sursilvan, Puter und Vallader (Word/LibreOffice) und ob alle Wortlisten unter MIT stehen wie bei Sutsilvan.
15. **DRG online**: Nutzungsbedingungen und aktueller Stand der Lieferungen.

### Nicht abrufbare Seiten (blockiert oder Fehler)
pledarigrond.ch, raw.githubusercontent.com/ZurichNLP/rumlem, github.com/farscrl/pledari-grond, hls-dhs-dss.ch (Artikel 024592/024594/024573), engadinerpost.ch (2014), grisun.ch, rm.wikipedia.org/wiki/Buna_Nouva, folia.unifr.ch (Grünert 2024, Binärdaten).
