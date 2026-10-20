#!/usr/bin/env python3
"""Autorenwerkzeug: Quellenkatalog – alle bekannten Quellen mit Nutzungsrecht und Verwendung im Projekt.

Aufruf: python3 scripts/authoring/quellen_katalog.py

Schreibt bzw. ergänzt `source`-Datensätze in data/sources/ um das Feld `catalog`:
  area     at | lxx | nt | versions | all                (Bereich)
  layer    manuscripts | editions | language_data | lexica | context | translations | aux   (Schicht)
  rights   free (gemeinfrei, CC0, CC BY) | sa (CC BY-SA) | nc (nicht kommerziell) | ask (auf Anfrage) | prot (geschützt)
  license  Kürzel (PD, CC0, BY, BY-SA, BY-NC, …)
  use      used (im Projekt verwendet) | cited (nur zitiert) | nc_planned (für data-nc vorgesehen) | not_used
  used_in  Dateimuster in data/, die aus der Quelle stammen (Pflicht bei used; der Validator prüft, dass sie passen)
  urls     Adressen, unter denen die Quelle in Datensätzen als Herkunft steht (Validator: jede Herkunft muss im Katalog stehen)
  why_de   wofür verwendet bzw. weshalb (noch) nicht
Bestehende Datensätze werden nur um `catalog` ergänzt (frühere Fassung im revision_log). Aus dem Katalog entstehen die
Quellenkarte (scripts/build_source_map.py -> app/quellenkarte/index.html) und das Blatt «Quellen und Rechte» in der App.
Lizenzangaben nach docs/QUELLEN.md (Recherche 9. und 13. Oktober 2026); KI-Recherche (Claude), keine Rechtsberatung.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _lib import D, write  # noqa: E402

DATE = "2026-10-13"
# Einträge, deren Angaben später geprüft bzw. geändert wurden (Prüfdatum je Eintrag; die übrigen behalten DATE)
CHECKED = {k: "2026-10-14" for k in ("SRC-SDBH", "SRC-STEP-TAHOT", "SRC-BDB", "SRC-STEP-TBESH", "SRC-UBS-DBH", "SRC-STEP-TAGNT",
                                     "SRC-MARBLE", "SRC-GREEK-LEXICA-FREE", "SRC-STEP-TBESG", "SRC-UBS-DGNT")}
AUTH = "Katalogangaben KI-Entwurf (Claude) vom 2026-10-13 nach docs/QUELLEN.md; Lizenzen vor jedem Import erneut prüfen."

# (ID, Titel, Bereich, Schicht, Recht, Kürzel, Verwendung, used_in, urls, Adresse, warum)
C = [
 # --- Altes Testament
 ("SRC-WLC", "Westminster Leningrad Codex (WLC)", "at", "editions", "free", "PD", "used",
  ["data/tokens/WLC-*.json"], ["https://tanach.us"], "https://tanach.us",
  "Grundtext des Alten Testaments (über MACULA Hebrew). Umgerechnet in die Navigationszählung."),
 ("SRC-MACULA-HEBREW", "MACULA Hebrew (mit Cherith-Glossen)", "at", "language_data", "free", "BY", "used",
  ["data/annotations/MACULA-WLC-*.json", "data/counts/WLC-*.json"], ["https://github.com/Clear-Bible/macula-hebrew"],
  "https://github.com/Clear-Bible/macula-hebrew",
  "Morphologie, Syntax, Glossen, Septuaginta-Entsprechungen. Die SDBH-Felder sind ausgeschlossen."),
 ("SRC-OSHB", "OpenScriptures Hebrew Bible (OSHB)", "at", "language_data", "free", "BY", "used",
  ["data/annotations/MACULA-WLC-*.json"], ["https://github.com/openscriptures/morphhb"], "https://github.com/openscriptures/morphhb",
  "Morphologie, über MACULA Hebrew übernommen."),
 ("SRC-SDBH", "SDBH-Wortbedeutungen (in MACULA Hebrew)", "at", "language_data", "ask", "Anfrage", "not_used", [], [], "https://semanticdictionary.org",
  "Die SDBH-Felder in MACULA sind nur «used with permission»; nach Lizenzgrundsatz ausgeschlossen. Die von UBS unter CC BY-SA 4.0 "
  "veröffentlichte Ausgabe (UBS Dictionary of Biblical Hebrew) ist davon getrennt und wird verwendet (SRC-UBS-DBH)."),
 ("SRC-UXLC", "UXLC (Unicode/XML Leningrad Codex)", "at", "editions", "free", "PD", "not_used", [], [], "https://tanach.us",
  "Laufend gepflegte Fassung desselben Codex wie der WLC. MACULA beruht auf dem WLC; ein Wechsel lohnt sich erst, wenn Korrekturen ins Gewicht fallen."),
 ("SRC-STEP-TAHOT", "STEPBible TAHOT", "at", "language_data", "free", "BY", "used", ["data/tagged-alignments/TALIGN-TAHOT-*.json"],
  ["https://github.com/STEPBible/STEPBible-Data"], "https://github.com/STEPBible/STEPBible-Data",
  "Geschriebene Ketiv-Formen, die MACULA nicht enthält (MACULA hat nur das Qere), und disambiguierte Strong-Nummern für den "
  "Wörterbuch-Eintrag; den WLC-Wörtern maschinell zugeordnet."),
 ("SRC-LENINGRAD-PHOTOS", "Codex Leningradensis, Farbfotos", "at", "manuscripts", "free", "PD?", "not_used", [], [],
  "https://archive.org/details/Leningrad_Codex_Color_Images",
  "Für einen Abgleich am Faksimile; Haltung des Fotografen ungeprüft, deshalb noch nicht eingebunden."),
 ("SRC-ALEPPO-MIQRA", "Aleppo-Codex (Miqra al pi ha-Masora)", "at", "manuscripts", "sa", "BY-SA", "not_used", [], [],
  "https://github.com/Sefaria/Sefaria-Export",
  "Älterer Mustercodex, aber ohne den grössten Teil der Tora. Als Vergleich zum WLC vorgesehen, sobald eine Lesarten-Ansicht für das AT steht."),
 ("SRC-QUMRAN-IMAGES", "Qumran-Rollen, Bilder (Leon Levy Library)", "at", "manuscripts", "ask", "Anfrage", "not_used", [], [],
  "https://www.deadseascrolls.org.il/terms", "Bilder nur mit schriftlicher Erlaubnis der Israel Antiquities Authority."),
 ("SRC-ETCBC-DSS", "Texte vom Toten Meer, ETCBC dss (Abegg)", "at", "manuscripts", "nc", "BY-NC", "used",
  ["data-nc/witness-texts/DSS-*.json", "data-nc/witnesses/WIT-DSS-*.json"], ["https://github.com/ETCBC/dss"],
  "https://github.com/ETCBC/dss",
  "Biblische Rollen aus Qumran und der Wüste Juda, in der nicht kommerziellen Schicht (data-nc). Bisher für Rut und Obadja importiert und maschinell mit dem WLC verglichen."),
 ("SRC-GENIZA", "Kairoer Geniza (Cambridge)", "at", "manuscripts", "ask", "Anfrage", "not_used", [], [], "https://cudl.lib.cam.ac.uk/",
  "Bilder nur zur Ansicht."),
 ("SRC-SAMARITAN", "Samaritanischer Pentateuch, Transkription", "at", "manuscripts", "free", "BY", "not_used", [], [],
  "https://zenodo.org/records/10694758", "Erst für die Textkritik der fünf Bücher Mose nötig; davon ist noch nichts ausgearbeitet."),
 ("SRC-BHSA", "BHSA (ETCBC)", "at", "language_data", "nc", "BY-NC", "nc_planned", [], [], "https://github.com/ETCBC/bhsa",
  "Sehr detaillierte Linguistik. MACULA Hebrew deckt den Bedarf frei ab; BHSA nur ergänzend in data-nc."),
 ("SRC-BHS", "Biblia Hebraica Stuttgartensia", "at", "editions", "ask", "Anfrage", "not_used", [], [],
  "https://www.die-bibel.de/biblia-hebraica-stuttgartensia", "Apparat nur mit Lizenz der Deutschen Bibelgesellschaft."),
 ("SRC-BHQ-HUB", "BHQ, Hebrew University Bible, HBCE", "at", "editions", "prot", "©", "not_used", [], [], "https://die-bibel.de/en/biblia-hebraica-quinta-bhq",
  "Geschützt; nur zitieren."),
 ("SRC-BDB", "Brown-Driver-Briggs (OpenScriptures)", "at", "lexica", "free", "BY", "not_used", [], [], "https://github.com/openscriptures/HebrewLexicon",
  "Ausführliches älteres Lexikon (1906). Die Lexikon-Ansicht nutzt zuerst das UBS-Wörterbuch (Bedeutungen nach Bedeutungsfeldern); "
  "BDB wäre eine Ergänzung für Wörter, die dort fehlen."),
 ("SRC-STEP-TBESH", "STEPBible TBESH (Kurzlexikon Hebräisch)", "at", "lexica", "free", "BY", "used", ["data/lexica/LEX-STEP-TBESH-HEB.json"],
  ["https://github.com/STEPBible/STEPBible-Data"], "https://github.com/STEPBible/STEPBible-Data",
  "Kurzglossen je Strong-Nummer als Rückfall, wo das UBS-Wörterbuch keinen Eintrag hat (v. a. Partikeln, Präpositionen). "
  "Die Bedeutungsspalte (Abridged BDB von Online Bible, nur mit Erlaubnis) ist nicht übernommen."),
 ("SRC-UBS-DBH", "UBS Dictionary of Biblical Hebrew", "at", "lexica", "sa", "BY-SA", "used", ["data/lexica/LEX-UBS-DBH-HEB.json"],
  ["https://github.com/ubsicap/ubs-open-license"], "https://github.com/ubsicap/ubs-open-license",
  "Wörterbuch-Eintrag im hebräischen Wortblatt: Bedeutungen mit Kurzdefinition, Glossen und Bedeutungsfeldern (Auszug aus SDBH, "
  "von UBS unter CC BY-SA 4.0 veröffentlicht; rund 90 % der Wörter). Nur Einträge für Wörter der importierten Bücher."),
 ("SRC-HALOT", "HALOT, Gesenius 18. Aufl., DCH", "at", "lexica", "prot", "©", "not_used", [], [], "", "Geschützt; nur zitieren."),
 ("SRC-ANE-TEXTS", "Altorientalische Texte, Inschriften (COS, ANET)", "at", "context", "prot", "©", "cited", [], [], "",
  "Im Hintergrund nur als Fundstelle genannt (z. B. Mescha-Stele)."),
 # --- Septuaginta
 ("SRC-LXX-UNCIALS", "Codex Vaticanus, Sinaiticus, Alexandrinus (Bilder)", "lxx", "manuscripts", "ask", "Anfrage", "not_used", [], [], "",
  "Bilder je Bibliothek, Weiterverwendung auf Anfrage."),
 ("SRC-GOETTINGEN-LXX", "Göttinger Septuaginta", "lxx", "editions", "prot", "©", "not_used", [], [], "", "Geschützt; nur zitieren."),
 ("SRC-RAHLFS-HANHART", "Rahlfs-Hanhart 2006", "lxx", "editions", "ask", "Anfrage", "not_used", [], [], "https://die-bibel.de/en/rights",
  "Daten nur mit Lizenz der Deutschen Bibelgesellschaft."),
 ("SRC-SWETE", "Swete, The Old Testament in Greek (1887–94)", "lxx", "editions", "free", "PD", "not_used", [], [], "",
  "Gemeinfrei, aber kein frei erschlossener Digitaltext gefunden; selbst erschliessen wäre ein grösseres Projekt."),
 ("SRC-CATSS", "CATSS (Rahlfs 1935 mit Morphologie)", "lxx", "language_data", "nc", "Erklärung", "nc_planned", [], [],
  "https://ccat.sas.upenn.edu/gopher/text/religion/biblical/", "Nur nach unterschriebener Nutzungserklärung (Andi Neck als Verantwortlicher); dann in data-nc."),
 ("SRC-LXX-RAHLFS-WONG", "LXX-Rahlfs-1935 (Eliran Wong)", "lxx", "language_data", "nc", "BY-NC-SA", "nc_planned", [], [],
  "https://github.com/eliranwong/LXX-Rahlfs-1935", "CATSS-Daten mit Lemmata; setzt die CATSS-Erklärung voraus. Für data-nc vorgesehen."),
 # --- Neues Testament
 ("SRC-CNTR-TRANSCRIPTIONS", None, "nt", "manuscripts", "sa", "BY-SA", "used",
  ["data/witness-texts/CNTR-*.json", "data/witness-readings/WREAD-CNTR-*.json"],
  ["https://github.com/Center-for-New-Testament-Restoration/transcriptions"], None,
  "Handschriften bis 400 n. Chr. und Ausgabentexte; maschinelle Zuordnung zu den Lesarten."),
 ("SRC-NTVMR", None, "nt", "manuscripts", "free", "BY", "cited", [], ["https://ntvmr.uni-muenster.de/"], None,
  "Katalog und Verweise (Handschriftennummern). Die Daten-API ist noch nicht angebunden; sie würde viel mehr Handschriften erschliessen als CNTR."),
 ("SRC-IGNTP", "IGNTP-Transkriptionen", "nt", "manuscripts", "free", "BY", "not_used", [], [], "https://www.birmingham.ac.uk/news/2017/igntp-releases-open-data",
  "Vor allem Johannes; wird gebraucht, sobald Johannes ausgearbeitet wird."),
 ("SRC-SINAITICUS-PROJECT", "Codex Sinaiticus Project", "nt", "manuscripts", "nc", "BY-NC-SA", "nc_planned", [], [],
  "https://www.codexsinaiticus.org/", "Transkription mit Korrekturschichten; ergänzend zu CNTR in data-nc."),
 ("SRC-CSNTM", "CSNTM, DigiVatLib (Bilder)", "nt", "manuscripts", "ask", "Anfrage", "cited", [], [], "https://www.csntm.org/terms-of-use-copyright/",
  "Als Faksimile-Verweise genannt, Bilder nicht übernommen."),
 ("SRC-PAPYRI-INFO", "papyri.info / DCLP / HGV (Metadaten)", "nt", "manuscripts", "free", "BY?", "used",
  ["data/witnesses/WIT-TM-*.json"], [], "https://papyri.info",
  "Sachangaben zu Amuletten und Papyri, eigene Formulierung."),
 ("SRC-SBLGNT-2010", None, "nt", "editions", "free", "BY", "used", ["data/tokens/SBLGNT-*.json"],
  ["https://github.com/Faithlife/SBLGNT", "https://sblgnt.com/"], None, "Grundtext des Neuen Testaments."),
 ("SRC-SBLGNT-APPARATUS", None, "nt", "editions", "free", "BY", "used", ["data/variants/sblgntapp-*/*.json", "data/assessments/edition-agreement-*/*.json"],
  ["https://github.com/Faithlife/SBLGNT/tree/master/data/sblgntapp"], None,
  "Variantenstellen auf Editionsebene (WH, Tregelles, NA28, RP) und Gesichertheitsbewertung."),
 ("SRC-HISTORIC-EDITIONS", "Robinson-Pierpont, Westcott-Hort, Stephanus, KJTR, Scrivener", "nt", "editions", "free", "PD", "used",
  ["data/witness-texts/CNTR-RP-*.json", "data/witness-texts/CNTR-WH-*.json", "data/witness-texts/CNTR-ST-*.json"], [], "",
  "Als Vergleichstexte über CNTR und den SBLGNT-Apparat."),
 ("SRC-ECM", "Editio Critica Maior (digital)", "nt", "editions", "ask", "nur lesen", "not_used", [], [], "https://ntvmr.uni-muenster.de",
  "Markus und Apostelgeschichte frei lesbar, aber ohne Datenlizenz; nur zitieren."),
 ("SRC-NA28", None, "nt", "editions", "prot", "©", "cited", [], [], None, "Nur zitiert (Fundstelle)."),
 ("SRC-THGNT", "Tyndale House GNT", "nt", "editions", "ask", "Anfrage", "not_used", [], [], "", "«All rights reserved»."),
 ("SRC-MACULA-GREEK", "MACULA Greek", "nt", "language_data", "free", "BY", "used", ["data/annotations/MACULA-SBLGNT-*.json", "data/counts/SBLGNT-*.json"],
  ["https://github.com/Clear-Bible/macula-greek"], "https://github.com/Clear-Bible/macula-greek",
  "Lemma, Morphologie, Syntax, Referenten, Glossen (Berean, Cherith)."),
 ("SRC-MORPHGNT-612", None, "nt", "language_data", "sa", "BY-SA", "used", ["data/annotations/MORPHGNT-*.json"],
  ["https://github.com/morphgnt/sblgnt"], None, "Nur der Pilot Mk 3,22–30; sonst MACULA Greek, weil freier (CC BY)."),
 ("SRC-STEP-TAGNT", "STEPBible TAGNT", "nt", "language_data", "free", "BY", "used", ["data/tagged-alignments/TALIGN-TAGNT-*.json"],
  ["https://github.com/STEPBible/STEPBible-Data"], "https://github.com/STEPBible/STEPBible-Data",
  "Zeigt für jedes Wort, welche gedruckten Ausgaben es haben (NA27/28, Tyndale House, SBL, WH, Tregelles, TR, Byz); den "
  "SBLGNT-Wörtern maschinell zugeordnet. Ausgabenbefund, kein Handschriftenbefund."),
 ("SRC-OPENGNT", "OpenGNT", "nt", "language_data", "sa", "BY-SA", "not_used", [], [], "https://github.com/eliranwong/OpenGNT",
  "Überschneidet sich mit MACULA Greek, das freier lizenziert ist (CC BY)."),
 ("SRC-MARBLE", "MARBLE / Louw-Nida-Bedeutungen (in MACULA Greek)", "nt", "language_data", "ask", "Anfrage", "not_used", [], [], "",
  "Die Felder in MACULA (domain, ln) nur mit Erlaubnis; nach Lizenzgrundsatz ausgeschlossen. Die UBS-Ausgabe unter CC BY-SA 4.0 "
  "wird getrennt davon verwendet (SRC-UBS-DGNT)."),
 ("SRC-GREEK-LEXICA-FREE", "LSJ, Abbott-Smith", "nt", "lexica", "free", "PD/BY", "not_used", [], [], "",
  "Ältere vollständige Lexika (gemeinfrei bzw. frei erschlossen); für ausführliche Einträge vorgesehen. Die Kurzansicht nutzt das "
  "UBS-Wörterbuch und STEPBible TBESG."),
 ("SRC-STEP-TBESG", "STEPBible TBESG (Kurzlexikon Griechisch)", "nt", "lexica", "free", "BY", "used", ["data/lexica/LEX-STEP-TBESG-GRC.json"],
  ["https://github.com/STEPBible/STEPBible-Data"], "https://github.com/STEPBible/STEPBible-Data",
  "Kurzglossen je (disambiguierter) Strong-Nummer als Rückfall, wo das UBS-Wörterbuch kein Lemma hat. Die Definitionsspalte "
  "(Abbott-Smith bzw. Middle Liddell, Herkunft je Eintrag nicht sicher) ist nicht übernommen."),
 ("SRC-UBS-DGNT", "UBS Dictionary of the Greek NT", "nt", "lexica", "sa", "BY-SA", "used", ["data/lexica/LEX-UBS-DGNT-GRC.json"],
  ["https://github.com/ubsicap/ubs-open-license"], "https://translation.bible/open-access-resources/",
  "Wörterbuch-Eintrag im griechischen Wortblatt: Bedeutungen nach Bedeutungsfeldern (überarbeitetes Louw-Nida, von UBS unter "
  "CC BY-SA 4.0 veröffentlicht), Kurzdefinition und Glossen; nur Einträge für Wörter der importierten Bücher."),
 ("SRC-BDAG", "BDAG, Bauer-Aland, Louw-Nida (Vollausgabe)", "nt", "lexica", "prot", "©", "not_used", [], [], "", "Geschützt; nur zitieren."),
 ("SRC-GREEKLAB", "Greeklab Interlinear", "nt", "language_data", "ask", "unklar", "cited", [], ["https://www.greeklab.org/interlinear.php?book=Mark&cap=3&verse=29"], "https://www.greeklab.org",
  "Einmal als Nachschlagehilfe zu Mk 3,29 genannt; keine Daten übernommen."),
 ("SRC-PERSEUS", "Perseus, Scaife Viewer", "nt", "context", "sa", "BY-SA/PD", "not_used", [], [], "https://scaife.perseus.org",
  "Antike Literatur für den Hintergrund; bisher nur als Fundstelle zitiert."),
 ("SRC-PHI-INSCRIPTIONS", "PHI Greek Inscriptions", "nt", "context", "ask", "nur lesen", "not_used", [], [], "https://inscriptions.packhum.org",
  "Durchsuchbar, keine Weiterverwendung."),
 # --- Alte Übersetzungen, Väter
 ("SRC-VULGATA-CLEMENTINA", "Vulgata Clementina", "versions", "editions", "free", "PD", "not_used", [], [], "",
  "Die App zeigt alte Übersetzungen noch nicht; vorgesehen für den Vergleich der Lesarten."),
 ("SRC-STUTTGART-VULGATE", "Stuttgarter Vulgata", "versions", "editions", "ask", "Anfrage", "not_used", [], [], "", "Lizenz der Deutschen Bibelgesellschaft."),
 ("SRC-VETUS-LATINA", "Vetus Latina Database", "versions", "editions", "prot", "Abo", "not_used", [], [], "", "Abo (Brepols)."),
 ("SRC-PESHITTA-LEIDEN", "Leidener Peshitta", "versions", "editions", "prot", "Abo", "not_used", [], [], "", "Abo (Brill)."),
 ("SRC-ETCBC-PESHITTA", "ETCBC Peshitta (AT)", "versions", "language_data", "nc", "BY-NC", "not_used", [], [], "https://github.com/ETCBC/peshitta",
  "Ohne Apparat; erst sinnvoll, wenn alte Übersetzungen in der App gezeigt werden."),
 ("SRC-COPTIC-SCRIPTORIUM", "Coptic Scriptorium", "versions", "language_data", "sa", "BY-SA", "not_used", [], [], "https://copticscriptorium.org",
  "Wie die Vulgata: vorgesehen, sobald alte Übersetzungen gezeigt werden."),
 ("SRC-SEFARIA", "Sefaria (Targumim, Mischna, Talmud)", "versions", "context", "sa", "gemischt", "cited", [], [], "https://github.com/Sefaria/Sefaria-Export",
  "Rabbinische Stellen werden im Hintergrund zitiert; Texte nicht übernommen (Lizenz je Fassung prüfen)."),
 ("SRC-FIRST1KGREEK", "First1KGreek (Kirchenväter u. a.)", "versions", "context", "sa", "BY-SA", "not_used", [], [], "https://opengreekandlatin.github.io/First1KGreek/",
  "Kirchenväter werden bisher nur mit Fundstelle zitiert; für Zitate im Original vorgesehen."),
 ("SRC-TLG-LLT", "TLG, Library of Latin Texts", "versions", "context", "prot", "Abo", "not_used", [], [], "", "Abo; nur zitieren."),
 ("SRC-BIBLINDEX", "Biblindex", "versions", "context", "ask", "nur lesen", "not_used", [], [], "https://www.biblindex.org", "Durchsuchbar; Export ungeprüft."),
 # --- Übergreifend
 ("SRC-LUTHER-1912", "Lutherbibel 1912", "all", "translations", "free", "PD", "used", ["data/translations/TRANS-LUT1912-*.json"],
  ["https://github.com/seven1m/open-bibles"], "https://github.com/seven1m/open-bibles", "Nur Vergleich, nie Lesetext (Entscheid 2026-10-13)."),
 ("SRC-ELBERFELDER-1905", "Elberfelder 1905", "all", "translations", "free", "PD", "used", ["data/translations/TRANS-ELB1905-*.json"],
  ["https://github.com/scrollmapper/bible_databases"], "https://github.com/scrollmapper/bible_databases", "Nur Vergleich."),
 ("SRC-KJV-EBIBLE", "King James Version (eBible.org)", "all", "aux", "free", "PD", "used", ["data/navigation/NAV-PROT66-KJV.json"],
  ["https://ebible.org/Scriptures/eng-kjv_usfm.zip"], "https://ebible.org", "Nur Verszahlen je Kapitel für die Navigation."),
 ("SRC-BEREAN", "Berean Interlinear und Standard Bible", "all", "translations", "free", "PD", "used", ["data/annotations/MACULA-SBLGNT-*.json"], [],
  "https://berean.bible", "Englische Glossen über MACULA Greek."),
 ("SRC-OFFENE-BIBEL", "Offene Bibel", "all", "translations", "sa", "BY-SA?", "not_used", [], [], "https://offene-bibel.de",
  "Lizenz ungeprüft. Wir übersetzen selbst aus dem Urtext; höchstens als weitere Vergleichsübersetzung."),
 ("SRC-MODERN-GERMAN", "Luther 2017, Zürcher, Einheitsübersetzung, Elberfelder neu", "all", "translations", "prot", "©", "not_used", [], [], "",
  "Geschützt; nur zitieren."),
 ("SRC-STEP-TVTMS", "STEPBible TVTMS (Versifikation)", "all", "aux", "free", "BY", "used", ["data/versification/VRS-TVTMS-*.json"],
  ["https://github.com/STEPBible/STEPBible-Data"], "https://github.com/STEPBible/STEPBible-Data", "Umrechnung der Verszählungen."),
 ("SRC-OPENBIBLE-XREF", "OpenBible.info Querverweise", "all", "aux", "free", "BY", "used", ["data/crossrefs/XREF-OPENBIBLE-*.json"],
  ["https://www.openbible.info/labs/cross-references/", "https://github.com/scrollmapper/bible_databases"], "https://www.openbible.info/labs/cross-references/", "344 799 Querverweise (Kopie über scrollmapper/bible_databases)."),
]


def run():
    n = 0
    for (rid, title, area, layer, rights, lic, use, used_in, urls, url, why) in C:
        path = D / "sources" / f"{rid}.json"
        cat = {"area": area, "layer": layer, "rights": rights, "license": lic, "use": use, "why_de": why,
               "checked": CHECKED.get(rid, DATE)}
        if used_in:
            cat["used_in"] = used_in
        if urls:
            cat["urls"] = urls
        if path.exists():
            rec = json.loads(path.read_text(encoding="utf-8"))
            new_title = title if title and rec.get("kind") == "catalog_entry" else rec.get("title")
            if rec.get("catalog") == cat and rec.get("title") == new_title:
                continue
            prev = {"catalog": rec.get("catalog")}
            if rec.get("title") != new_title:
                prev["title"] = rec.get("title")
            rec["revision_log"] = rec.get("revision_log", []) + [{"date": CHECKED.get(rid, DATE), "change_de": "Katalogangaben (Nutzungsrecht, Verwendung) ergänzt bzw. geändert",
                                                                 "previous": prev}]
            rec["catalog"] = cat
            rec["title"] = new_title
            path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            n += 1
        else:
            rec = {"id": rid, "type": "source", "status": "draft", "tags": [], "kind": "catalog_entry", "title": title}
            if url:
                rec["url"] = url
            rec.update({"catalog": cat, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}})
            n += write(path, rec, "Katalogangaben überarbeitet")
    print(f"PASS: Quellenkatalog mit {len(C)} Einträgen; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
