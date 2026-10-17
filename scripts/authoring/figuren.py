#!/usr/bin/env python3
"""Figurenbaukasten: Aussehen der Personen, Rollen und Gruppen des Bildlexikons für alle Bildstile.

Je Lexikon-Eintrag Parameter (Gewand, Mantel, Haar, Bart, Kopfbedeckung, Alter, Attribut), abgeleitet aus den
Pflichtmerkmalen und der Palette des Lexikons (data/illustrations/lexicon/). Aus denselben Parametern entstehen
- im Stil «Symbol» ein Bauteil ``ill-p-<name>`` (Ganzfigur ohne Gesicht, viewBox 0 0 30 64),
- im Stil «Anime» eine Figur für das Brustbild (``CHAR`` in bilder_anime.py).
So sieht eine Figur in beiden Stilen gleich aus (gleiche Farben, gleiche Zeichen). Handgezeichnete Figuren
(ill-p-jesus, ill-p-maria …) bleiben unverändert; hier stehen nur die übrigen.

Attribute (ill-a-*) sind kleine Bauteile, die eine Figur trägt (Schlüssel, Ähren …); sie stehen nicht im Lexikon,
sondern gehören zur Figur. Gegenstände, die selbst handeln oder gezeigt werden, sind Lexikon-Einträge (bildsymbole.py).

KI-Entwurf (Claude) vom 2026-10-17 auf Wunsch von Andi Neck; eigene Zeichnungen (CC0), keine fachliche Prüfung.
"""
INK = "#3B3226"
SKIN = "#C89B72"

# ------------------------------------------------------------------ Attribute (klein, viewBox 0 0 16 16)
ATTR = {
    "schluessel": '<g fill="none" stroke="#C08A2A" stroke-width="1.8" stroke-linecap="round"><circle cx="5" cy="5" r="3.2"/><path d="M7.4 7.4l6.4 6.4M11 11l1.8-1.8M12.6 12.6l1.6-1.6"/></g>',
    "x-kreuz": '<path d="M2 2l12 12M14 2L2 14" stroke="#7A5A34" stroke-width="2.6" stroke-linecap="round"/>',
    "messer": '<path d="M3 13l8-8 2 1-8 8z" fill="#C9C2B4" stroke="#3B3226" stroke-width=".7"/><path d="M11 5l2.6-2.6" stroke="#5B4630" stroke-width="2.2" stroke-linecap="round"/>',
    "saege": '<path d="M1 10h13v3H1z" fill="#C9C2B4" stroke="#3B3226" stroke-width=".7"/><path d="M1 10l1.5-2 1.5 2 1.5-2 1.5 2 1.5-2 1.5 2 1.5-2 1.5 2" fill="none" stroke="#3B3226" stroke-width=".7"/><path d="M14 9h2v5h-2z" fill="#7A5A34"/>',
    "keule": '<path d="M4 14L11 4" stroke="#7A5A34" stroke-width="2" stroke-linecap="round"/><ellipse cx="11.6" cy="3.6" rx="3" ry="2.4" fill="#7A5A34" stroke="#3B3226" stroke-width=".7"/>',
    "winkelmass": '<path d="M3 2v11h11" fill="none" stroke="#8C8070" stroke-width="2.4" stroke-linejoin="round"/>',
    "kreuzstab": '<path d="M8 1v15M4.5 4.5h7" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/>',
    "kasse": '<path d="M2 6h12v8H2z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".8"/><path d="M2 6l2-3h8l2 3" fill="#A07A44" stroke="#3B3226" stroke-width=".8"/><circle cx="8" cy="10" r="1.3" fill="#D9A441"/>',
    "muschel": '<path d="M8 14L2 5q6-5 12 0z" fill="#F2E6CC" stroke="#3B3226" stroke-width=".8"/><path d="M8 14L5 4M8 14V3M8 14l3-10" stroke="#B4A98F" stroke-width=".7"/>',
    "walkerstange": '<path d="M3 15L13 2" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/><path d="M11 2h5v3h-5z" fill="#8A6A3A"/>',
    "buch": '<path d="M2 3h6v11H2zM8 3h6v11H8z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M13 1l2 6" stroke="#3B3226" stroke-width="1"/>',
    "kelch": '<path d="M4 2h8q0 6-4 7-4-1-4-7z" fill="#D9A441" stroke="#9C6F1C" stroke-width=".8"/><path d="M8 9v4M5 14h6" stroke="#9C6F1C" stroke-width="1.4" stroke-linecap="round"/>',
    "stabkreuz": '<path d="M8 1v15M5 4h6" stroke="#8F6BA8" stroke-width="1.6" stroke-linecap="round"/>',
    "feigenblatt": '<path d="M8 15V8M8 8Q2 9 2 4q3 1 4-2 2 2 2 2 0 0 2-2 1 3 4 2 0 5-6 4z" fill="#5E7F3A" stroke="#3B3226" stroke-width=".7"/>',
    "aehren": '<g stroke="#B08A2A" stroke-width="1.1" stroke-linecap="round"><path d="M5 15L7 3M8 15V2M11 15L9 3"/></g><g fill="#E8B84A" stroke="#B08A2A" stroke-width=".5"><ellipse cx="7" cy="4" rx="1.4" ry="2.4"/><ellipse cx="8" cy="3" rx="1.4" ry="2.4"/><ellipse cx="9.2" cy="4" rx="1.4" ry="2.4"/></g>',
    "worfel": '<path d="M3 15L11 5" stroke="#7A5A34" stroke-width="1.6" stroke-linecap="round"/><path d="M9.5 6.5l3-4 3 3-4 3z" fill="#A07A44" stroke="#3B3226" stroke-width=".7"/>',
    "schuh": '<path d="M2 11q0-4 3-4l3 1q2 1 6 1 1 0 1 2v2H2z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".8"/><path d="M5 7v-3" stroke="#5B4630" stroke-width="1"/>',
    "salbgefaess": '<path d="M5 6h6l1 8H4z" fill="#E9D8B4" stroke="#3B3226" stroke-width=".8"/><path d="M6 6V4h4v2" fill="#C9B48E" stroke="#3B3226" stroke-width=".8"/><path d="M5 3h6v1.4H5z" fill="#8E3B5E"/>',
    "flaeschchen": '<path d="M6.5 3h3v3l1.5 2v7h-6V8l1.5-2z" fill="#E9D8B4" stroke="#3B3226" stroke-width=".8"/><path d="M6.5 2h3v1.4h-3z" fill="#6B8E7A"/>',
    "kelle": '<path d="M12 2L6 9" stroke="#7A5A34" stroke-width="1.6" stroke-linecap="round"/><path d="M2 10a4 3 0 0 0 7 0z" fill="#8C8070" stroke="#3B3226" stroke-width=".8"/>',
    "lampe": '<path d="M2 10q6-5 11 0l2-1v2q-7 4-13-1z" fill="#B07A3E" stroke="#3B3226" stroke-width=".8"/><path d="M13 9q2-4 0-7-1 3 0 7z" fill="#F2B53A"/>',
    "netz": '<path d="M2 3h12l-2 11H4z" fill="none" stroke="#8A6A3A" stroke-width="1"/><path d="M2 3l10 11M6 3l8 8M10 3l4 4M14 3L4 14M10 3l-8 8M6 3L2 7" stroke="#8A6A3A" stroke-width=".6"/>',
    "laterne": '<path d="M8 1v2" stroke="#3B3226" stroke-width="1"/><path d="M4 3h8l-1 10H5z" fill="#F2B53A" stroke="#3B3226" stroke-width=".9"/><path d="M4 13h8v2H4z" fill="#5B4630"/>',
    "stab": '<path d="M9 1v15" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/>',
    "hirtenstab": '<path d="M9 16V5q0-4 3-4t3 3" fill="none" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/>',
    "kette": '<g fill="none" stroke="#6A6A6A" stroke-width="1.2"><ellipse cx="3" cy="8" rx="2.4" ry="1.6"/><ellipse cx="7" cy="8" rx="2.4" ry="1.6"/><ellipse cx="11" cy="8" rx="2.4" ry="1.6"/></g><path d="M13.6 8l1.8-2M13.6 8l1.8 2" stroke="#6A6A6A" stroke-width="1"/>',
    "leinentuch": '<path d="M2 3h12v11H2z" fill="#F6EBD9" stroke="#3B3226" stroke-width=".8"/><path d="M2 6h12M2 9h12" stroke="#D8CBB0" stroke-width=".8"/>',
    "beutel": '<path d="M5 5q-3 3-3 6 0 3 6 3t6-3q0-3-3-6z" fill="#7A8A5A" stroke="#3B3226" stroke-width=".8"/><path d="M5 5h6" stroke="#5B4630" stroke-width="1.4"/>',
    "brief": '<path d="M2 3h9l3 3v8H2z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M4 7h7M4 10h8" stroke="#A79A80" stroke-width=".8"/><circle cx="11" cy="11.5" r="1.6" fill="#A33A2E"/>',
    "rolle": '<path d="M3 4h10v8H3z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/><rect x="1.5" y="3" width="2.6" height="10" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><rect x="11.9" y="3" width="2.6" height="10" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><circle cx="8" cy="11" r="1.4" fill="#A33A2E"/>',
    "feder": '<path d="M3 15Q6 6 14 2q-2 7-9 10" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M1 13h5v2H1z" fill="#2E2017"/>',
    "muenzen": '<circle cx="5" cy="10" r="3" fill="#D9A441" stroke="#9C6F1C" stroke-width=".7"/><circle cx="10" cy="9" r="3" fill="#D9A441" stroke="#9C6F1C" stroke-width=".7"/><circle cx="7.5" cy="5.5" r="3" fill="#C9C2B4" stroke="#8C8070" stroke-width=".7"/>',
    "zwei-muenzen": '<circle cx="5.5" cy="9" r="2.6" fill="#B07A3E" stroke="#6A4A2A" stroke-width=".7"/><circle cx="10.5" cy="9" r="2.6" fill="#B07A3E" stroke="#6A4A2A" stroke-width=".7"/>',
    "matte": '<path d="M1 9h14v4H1z" fill="#C9B48E" stroke="#3B3226" stroke-width=".8"/><path d="M3 9v4M6 9v4M9 9v4M12 9v4" stroke="#A79A80" stroke-width=".6"/>',
    "tuer": '<path d="M3 1h10v15H3z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".9"/><circle cx="11" cy="9" r=".9" fill="#D9A441"/>',
    "tuer-offen": '<path d="M3 1h10v15H3z" fill="#3B3226"/><path d="M3 1l5 2v14l-5-1z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".7"/>',
    "garbe": '<g stroke="#B08A2A" stroke-width="1" stroke-linecap="round"><path d="M4 15L7 4M8 15V3M12 15L9 4M6 15l2-11M10 15L8 4"/></g><path d="M5 11h6" stroke="#8A6A3A" stroke-width="1.6"/><g fill="#E8B84A"><ellipse cx="7" cy="4" rx="1.3" ry="2.2"/><ellipse cx="8" cy="3" rx="1.3" ry="2.2"/><ellipse cx="9" cy="4" rx="1.3" ry="2.2"/></g>',
    "tinte": '<path d="M4 8h7v6H4z" fill="#2E2017"/><path d="M9 9L14 1" stroke="#F4F1EA" stroke-width="1.2"/><path d="M9 9L14 1" stroke="#3B3226" stroke-width=".4"/>',
    "myrrhe": '<path d="M4 6h8v8H4z" fill="#C9B48E" stroke="#3B3226" stroke-width=".8"/><path d="M4 6l1-2h6l1 2" fill="#A07A44" stroke="#3B3226" stroke-width=".7"/>',
    "kind": '<circle cx="8" cy="5" r="3" fill="#C89B72" stroke="#3B3226" stroke-width=".7"/><path d="M4 15q0-7 4-7t4 7z" fill="#F2E6CC" stroke="#3B3226" stroke-width=".7"/>',
    "saeugling": '<ellipse cx="8" cy="10" rx="6" ry="4" fill="#F2E6CC" stroke="#3B3226" stroke-width=".8"/><circle cx="4.5" cy="8.5" r="2.4" fill="#C89B72" stroke="#3B3226" stroke-width=".6"/>',
}
ATTR_VB = "0 0 16 16"

# ------------------------------------------------------------------ Figuren
# robe, mantle, hair (Farbe), style (short|curls|long|bald|none), beard (None|short|full|long), beard_color,
# head (None | ("veil", Farbe) | ("turban", Farbe) | ("hood", Farbe) | ("crown",) | ("helmet",) | ("wreath",) | ("band", Farbe)),
# age (adult|young|old|child|baby), sex (m|f), belt, sash, apron, trim, attr (Attribut), wings, bound, chains, kneel
def F(robe, mantle=None, hair="#2E2017", style="short", beard=None, head=None, age="adult", sex="m", attr=None, **kw):
    return dict(robe=robe, mantle=mantle, hair=hair, style=style, beard=beard, head=head, age=age, sex=sex, attr=attr, **kw)


GREY, WHITE, DARK, BROWN, BLACK = "#8A8478", "#D8D2C4", "#2E2017", "#4A3020", "#1E1610"
APOSTLE = "#9C7A4C"
FIGS = {
    # Zwölf und Jünger (Jüngergewand, je eigene Mantelfarbe)
    "FIG-PETRUS": F(APOSTLE, "#C08A2A", GREY, "curls", "short", attr="schluessel"),
    "FIG-ANDREAS": F(APOSTLE, "#6E8B3D", "#5A4A3A", "long", "full", attr="x-kreuz"),
    "FIG-JAKOBUS-ZEBEDAEUS": F(APOSTLE, "#2F6F73", BROWN, "short", "full", attr="muschel"),
    "FIG-JOHANNES-ZEBEDAEUS": F(APOSTLE, "#6A8FB3", "#6A4A2A", "long", None, age="young", attr="kelch"),
    "FIG-PHILIPPUS": F(APOSTLE, "#8F6BA8", DARK, "short", "short", attr="stabkreuz"),
    "FIG-BARTHOLOMAEUS": F(APOSTLE, "#7A4E3A", DARK, "curls", "full", attr="messer"),
    "FIG-NATANAEL": F(APOSTLE, "#5E7F3A", DARK, "curls", "full", attr="feigenblatt"),
    "FIG-MATTHAEUS": F(APOSTLE, "#3F5A7A", BROWN, "short", "full", attr="buch"),
    "FIG-LEVI": F("#4A6B5A", "#4A6B5A", BROWN, "short", "short", attr="muenzen"),
    "FIG-THOMAS": F(APOSTLE, "#A0703A", DARK, "short", "short", attr="winkelmass"),
    "FIG-JAKOBUS-ALPHAEUS": F(APOSTLE, "#6B6B8A", BROWN, "short", "full", attr="walkerstange"),
    "FIG-THADDAEUS": F(APOSTLE, "#8A8F4A", DARK, "long", "full", attr="keule"),
    "FIG-JUDAS-NICHT-ISKARIOT": F(APOSTLE, "#5F8F8A", DARK, "short", "short"),
    "FIG-SIMON-KANANAEUS": F(APOSTLE, "#9A4E4E", "#3A2A1C", "curls", "full", attr="saege"),
    "FIG-JUDAS-ISKARIOT": F(APOSTLE, "#7A8A9A", DARK, "short", "short", attr="kasse"),
    "FIG-LIEBLINGSJUENGER": F(APOSTLE, "#E2CDA8", "#6A4A2A", "long", None, age="young"),
    # Frauen
    "FIG-MARIA-MAGDALA": F("#E2CDA8", "#8E3B5E", "#4A2A1A", "long", sex="f", head=("veil", "#8E3B5E"), attr="salbgefaess"),
    "FIG-MARIA-BETANIEN": F("#6B8E7A", None, "#3A2618", "long", sex="f", attr="flaeschchen"),
    "FIG-MARTA": F("#B4704A", None, "#3A2618", "short", sex="f", head=("veil", "#E9D8B4"), attr="kelle"),
    "FIG-MARIA-KLOPAS": F("#D8CBB0", None, DARK, "short", sex="f", head=("veil", "#7A6A8E")),
    "FIG-MARIA-MUTTER-JAKOBUS": F("#6E7F5A", None, DARK, "short", sex="f", head=("veil", "#D8CBB0"), attr="salbgefaess"),
    "FIG-SALOME": F("#F2E6CC", None, DARK, "short", sex="f", head=("veil", "#B07A3E"), attr="salbgefaess"),
    "FIG-HERODIAS": F("#7A3E6A", None, BLACK, "long", sex="f", trim="#D9A441", head=("veil", "#C9A0BE")),
    "FIG-TOCHTER-HERODIAS": F("#D4537E", None, BLACK, "long", sex="f", age="young"),
    "FIG-EUODIA": F("#A8687A", None, DARK, "short", sex="f", head=("veil", "#F2E6CC")),
    "FIG-SYNTYCHE": F("#6A8AA8", None, BROWN, "short", sex="f", head=("veil", "#F2E6CC")),
    "FIG-AUSERWAEHLTE-HERRIN": F("#6A4A7A", None, DARK, "short", sex="f", head=("veil", "#F2E6CC")),
    # Rut
    "FIG-RUT": F("#7A8B4A", None, BROWN, "short", sex="f", head=("veil", "#E8B84A"), attr="garbe"),
    "FIG-NOOMI": F("#C9BFAA", None, GREY, "short", sex="f", age="old", head=("veil", "#4A4A5A")),
    "FIG-ORPA": F("#8E6A7A", None, DARK, "short", sex="f", head=("veil", "#E2CDA8")),
    "FIG-BOAS": F("#E8B84A", "#2F5F6F", "#5A4A3A", "short", "full", attr="worfel"),
    "FIG-ELIMELECH": F("#C9BFAA", "#6A5A4A", GREY, "short", "full", attr="stab"),
    "FIG-MACHLON": F("#7A6A5A", None, DARK, "short", "short", age="young", sash="#7A8B4A"),
    "FIG-KILJON": F("#7A6A5A", None, DARK, "short", "short", age="young", sash="#8E6A7A"),
    "FIG-LOESER": F("#8A7A6A", "#5B4630", DARK, "short", "full", attr="schuh"),
    "FIG-OBED": F("#F2E6CC", None, DARK, "none", age="baby"),
    # Propheten, Könige
    "FIG-JONA": F("#6FB2E6", "#4A6E8A", DARK, "short", "full"),
    "FIG-OBADJA": F("#E7DCC4", "#6A5A7A", GREY, "short", "long", attr="rolle"),
    "FIG-ELIJA": F("#8A6A3A", "#5B4630", GREY, "long", "long", fur=True),
    "FIG-HERODES-ANTIPAS": F("#6A2E5E", "#6A2E5E", BLACK, "short", "short", head=("crown",), trim="#D9A441"),
    # Johannes der Täufer und Evangelien-Personen
    "FIG-JOHANNES-TAEUFER": F("#8A6A3A", None, "#3A2618", "long", "full", belt="#5B4630", attr="kreuzstab", fur=True),
    "FIG-NIKODEMUS": F("#C9BFAA", "#3B4A6B", GREY, "short", "full", head=("hood", "#3B4A6B"), attr="lampe"),
    "FIG-LAZARUS": F("#E7DCC4", None, BROWN, "short", "short", belt="#8A7A60"),
    "FIG-JAIRUS": F("#E7DCC4", "#4F6B7A", DARK, "short", "full", head=("hood", "#E7DCC4"), tassels=True),
    "FIG-BARTIMAEUS": F("#C9BFAA", "#8A7A60", GREY, "short", "short", attr="stab"),
    "FIG-GERASENER": F("#8A8070", None, DARK, "long", "short", chains=True),
    "FIG-JOSEF-ARIMATAEA": F("#F6EBD9", "#5A5A5A", GREY, "short", "full", attr="leinentuch"),
    "FIG-SIMON-KYRENE": F("#8A7A50", None, DARK, "short", "short", belt="#5B4630"),
    "FIG-BARABBAS": F("#7A6A5A", None, BLACK, "short", "short", bound=True),
    "FIG-MALCHUS": F("#B8A98A", None, DARK, "short", None, sash="#4A5A7A"),
    "FIG-PILATUS": F("#F2E6CC", None, "#5A4A3A", "short", None, trim="#6A2E5E", toga=True),
    "FIG-KAJAFAS": F("#4A5A7A", None, GREY, "short", "full", head=("turban", "#F6EBD9"), breast=True, plate=True),
    "FIG-HANNAS": F("#6A6A7A", "#8A8A8A", WHITE, "short", "long", head=("turban", "#F6EBD9"), attr="stab"),
    "FIG-SATAN": None,  # dunkler Schatten ohne Gestalt: Bauteil in bildsymbole.py
    # Mitarbeitende und Briefpersonen
    "FIG-TIMOTHEUS": F("#5A7A9A", None, BROWN, "short", None, age="young", attr="brief"),
    "FIG-TITUS": F("#5A6A3A", None, DARK, "short", "short", attr="brief"),
    "FIG-EPAPHRODITUS": F("#7A8A5A", "#E2CDA8", BROWN, "short", "short", attr="beutel"),
    "FIG-DER-AELTESTE": F("#6A6A6A", "#E7DCC4", WHITE, "short", "long", age="old", attr="tinte"),
    "FIG-GAIUS": F("#8A6A4A", "#F6EBD9", DARK, "short", "short", attr="tuer-offen"),
    "FIG-DIOTREPHES": F("#6A5A5A", "#C9BFAA", DARK, "short", "short", attr="tuer"),
    "FIG-DEMETRIUS": F("#4A7A6A", "#E7DCC4", BROWN, "short", "short", attr="brief"),
    # Rollen
    "FIG-ROLLE-AELTESTER": F("#C9BFAA", "#6A5A4A", GREY, "short", "long", age="old", attr="stab"),
    "FIG-ROLLE-BOTE": F("#8A6A3A", "#E2CDA8", DARK, "short", "short", attr="brief"),
    "FIG-ROLLE-ENGEL": F("#FFFFFF", None, "#D9A441", "short", None, wings=True),
    "FIG-ROLLE-FISCHER": F("#6A7F8A", None, DARK, "curls", "short", attr="netz"),
    "FIG-ROLLE-HIRTE": F("#8A7A50", "#F6EBD9", DARK, "short", "short", attr="hirtenstab"),
    "FIG-ROLLE-HOHEPRIESTER": F("#4A5A7A", None, GREY, "short", "full", head=("turban", "#F6EBD9"), breast=True),
    "FIG-ROLLE-KAPITAEN": F("#8A6A3A", "#2F4F6F", DARK, "short", "full", head=("band", "#2F4F6F")),
    "FIG-ROLLE-KRANKER": F("#C9BFAA", None, DARK, "short", "short", attr="matte"),
    "FIG-ROLLE-PHARISAEER": F("#5A6A7A", "#4F6D8A", DARK, "short", "full", head=("hood", "#F2E6CC"), tassels=True),
    "FIG-ROLLE-PRIESTER": F("#F6EBD9", None, DARK, "short", "short", head=("turban", "#F6EBD9"), sash="#4A5A7A"),
    "FIG-ROLLE-SCHRIFTGELEHRTER": F("#6A5A4A", "#E7DCC4", DARK, "short", "full", attr="rolle"),
    "FIG-ROLLE-TEMPELWACHE": F("#4A5A6A", None, DARK, "short", "short", belt="#C9BFAA", attr="laterne"),
    "FIG-ROLLE-WITWE": F("#C9BFAA", None, GREY, "short", sex="f", age="old", head=("veil", "#4A4A4A"), attr="zwei-muenzen"),
    # Gruppen
    "FIG-GRUPPE-SEELEUTE": F("#E2CDA8", None, DARK, "curls", "short", sash="#2F4F6F", head=("band", "#2F4F6F")),
    "FIG-GRUPPE-EDOM": F("#C9A27A", "#9A4E3A", DARK, "short", "full"),
    "FIG-GRUPPE-ZWOELF": F(APOSTLE, "#7A5A34", DARK, "curls", "full"),
}
GROUPS = {"FIG-GRUPPE-SEELEUTE", "FIG-GRUPPE-EDOM", "FIG-GRUPPE-ZWOELF"}


def slug(fid):
    return fid.replace("FIG-", "").replace("ROLLE-", "").replace("GRUPPE-", "g-").lower()


# ------------------------------------------------------------------ Stil «Symbol»: Ganzfigur ohne Gesicht
def _hair_sym(p):
    h, st = p["hair"], p["style"]
    if p["age"] == "baby":
        return ""
    if st == "curls":
        return "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="{h}"/>' for x, y in ((10, 10), (12.4, 8), (15, 7.4), (17.6, 8), (20, 10)))
    if st == "long":
        return f'<path d="M8.4 14q-.6-8 6.6-8.4 7.2.4 6.6 8.4l1 7h-2.6l-.6-6q-1-4.6-4.4-5-3.4.4-4.4 5l-.6 6H7.4z" fill="{h}"/>'
    if st == "bald":
        return f'<path d="M8.6 15q-.4-3 1-4.6M21.4 15q.4-3-1-4.6" stroke="{h}" stroke-width="1.8" fill="none"/>'
    if st == "none":
        return ""
    return f'<path d="M8.6 12.5q1-7 6.4-7t6.4 7q-2-3-6.4-3t-6.4 3z" fill="{h}"/>'


def _beard_sym(p):
    b = p.get("beard")
    if not b:
        return ""
    c = p.get("beard_color") or p["hair"]
    d = {"short": "M9.5 16q5.5 6 11 0q-1 4-5.5 4.6-4.5-.6-5.5-4.6z",
         "full": "M9 16q6 9 12 0q-1 6-6 7q-5-1-6-7z",
         "long": "M9 16q6 12 12 0q-1 9-6 10q-5-1-6-10z"}[b]
    return f'<path d="{d}" fill="{c}"/>'


def _head_sym(p):
    hd = p.get("head")
    if not hd:
        return ""
    k = hd[0]
    if k == "veil":
        return f'<path d="M7 26q-1-14 2-17 3-4 6-4t6 4q3 3 2 17l-2-1q1-9-1.4-12-2-2.4-4.6-2.4t-4.6 2.4Q7.9 16 9 25z" fill="{hd[1]}" stroke="{INK}" stroke-width=".7"/>'
    if k == "hood":
        return f'<path d="M7.6 20q-1-12 7.4-13 8.4 1 7.4 13l-2 .4q.6-9-5.4-9.6-6 .6-5.4 9.6z" fill="{hd[1]}" stroke="{INK}" stroke-width=".7"/>'
    if k == "turban":
        return (f'<path d="M8.4 11q0-6 6.6-6.4 6.6.4 6.6 6.4z" fill="{hd[1]}" stroke="{INK}" stroke-width=".7"/>'
                f'<path d="M8.6 9q6.4-2 12.8 0" stroke="#C9BFAA" stroke-width=".8" fill="none"/>')
    if k == "band":
        return f'<path d="M8.6 10.6q6.4-2.4 12.8 0v1.8q-6.4-2.4-12.8 0z" fill="{hd[1]}"/>'
    if k == "crown":
        return '<path d="M8.5 10l1-7 3 4 2.5-5 2.5 5 3-4 1 7z" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".8"/>'
    if k == "helmet":
        return f'<path d="M8 14q0-9 7-9t7 9z" fill="#8C8070" stroke="{INK}" stroke-width="1"/><path d="M9 5q6-5 12 0" fill="none" stroke="#8E1F2F" stroke-width="2.4"/>'
    if k == "wreath":
        return '<path d="M8.6 11q6.4-4 12.8 0" fill="none" stroke="#D9A441" stroke-width="1.8" stroke-dasharray="1.6 .8"/>'
    return ""


def symbol_person(fid):
    p = FIGS[fid]
    sid = "ill-p-" + slug(fid)
    o = []
    if p.get("wings"):
        o.append(f'<path d="M9 28Q-2 18 1 6q5 8 10 14zM21 28q11-10 8-22-5 8-10 14z" fill="#FFFDF6" stroke="#D9A441" stroke-width="1"/>')
    if p["age"] == "baby":
        o.append(f'<ellipse cx="15" cy="50" rx="11" ry="7" fill="{p["robe"]}" stroke="{INK}" stroke-width="1.1"/><circle cx="8.5" cy="46" r="4.4" fill="{SKIN}" stroke="{INK}" stroke-width="1"/>')
        return f'<symbol id="{sid}" viewBox="0 0 30 64">{"".join(o)}</symbol>'
    body = "M5 62L8 26q7-7 14 0l3 36z" if p["sex"] == "m" else "M4 62L8 27q7-7 14 0l4 35z"
    o.append(f'<path d="{body}" fill="{p["robe"]}" stroke="{INK}" stroke-width="1.2"/>')
    if p.get("fur"):
        o.append(f'<path d="M8 27q7-7 14 0l1 8q-8 3-16 0z" fill="#8A6A3A" stroke="{INK}" stroke-width=".7"/><path d="M9 30l1 3M12 29l.5 3M15 29v3M18 29l-.5 3M21 30l-1 3" stroke="#5B4630" stroke-width=".7"/>')
    if p.get("mantle"):
        o.append(f'<path d="M8 26q7-7 14 0l3 36H18L9 28z" fill="{p["mantle"]}" stroke="{INK}" stroke-width="1"/>')
    if p.get("toga"):
        o.append(f'<path d="M8 27q8 2 13 14l2 21h-3l-2-18Q14 32 8 30z" fill="#FFFFFF" stroke="{INK}" stroke-width=".7"/><path d="M20 41l2 21" stroke="{p["trim"]}" stroke-width="1.6"/>')
    elif p.get("trim"):
        o.append(f'<path d="M10.5 24.5L15 30l4.5-5.5" fill="none" stroke="{p["trim"]}" stroke-width="1.4"/>')
    if p.get("sash"):
        o.append(f'<path d="M9 25l13 22" stroke="{p["sash"]}" stroke-width="3.4"/>')
    if p.get("belt"):
        o.append(f'<path d="M7 40h16" stroke="{p["belt"]}" stroke-width="2"/>')
    if p.get("breast"):
        o.append('<path d="M11.5 30h7v7h-7z" fill="#D9A441" stroke="#9C6F1C" stroke-width=".6"/>'
                 + "".join(f'<circle cx="{13 + (i % 3) * 2}" cy="{31.6 + (i // 3) * 1.8}" r=".6" fill="{c}"/>'
                           for i, c in enumerate(["#A33A2E", "#3E6E9E", "#6E8B3D"] * 4)))
    if p.get("tassels"):
        o.append(f'<path d="M7 60v2M10 61v2M20 61v2M23 60v2" stroke="#F2E6CC" stroke-width="1.2"/>')
    if p.get("chains"):
        o.append(f'<g fill="none" stroke="#6A6A6A" stroke-width="1"><ellipse cx="6" cy="44" rx="2" ry="1.3"/><ellipse cx="3.5" cy="46" rx="2" ry="1.3"/><ellipse cx="24" cy="44" rx="2" ry="1.3"/><ellipse cx="26.5" cy="46" rx="2" ry="1.3"/></g>')
    if p.get("bound"):
        o.append(f'<path d="M10 38h10v5H10z" fill="{SKIN}" stroke="{INK}" stroke-width=".7"/><path d="M10 40.5h10" stroke="#8A6A3A" stroke-width="1.6"/>')
    hd = p.get("head")
    if hd and hd[0] == "veil":
        o.append(_head_sym(p))
    r = 6.0 if p["age"] in ("young", "child") else 6.5
    o.append(f'<circle cx="15" cy="14" r="{r}" fill="{SKIN}" stroke="{INK}" stroke-width="1.2"/>')
    if not (hd and hd[0] in ("veil", "hood", "turban", "helmet")):
        o.append(_hair_sym(p))
    o.append(_beard_sym(p))
    if hd and hd[0] != "veil":
        o.append(_head_sym(p))
    if p.get("plate"):
        o.append('<path d="M12 8.6h6v1.6h-6z" fill="#E0B24E"/>')
    if p.get("attr"):
        o.append(f'<svg x="-1" y="34" width="13" height="13" viewBox="{ATTR_VB}">{ATTR[p["attr"]]}</svg>')
    inner = "".join(o)
    if p["age"] == "child":  # Kind: kleiner, auf dem Boden stehend
        inner = f'<g transform="translate(4.5 19.2) scale(.7)">{inner}</g>'
    return f'<symbol id="{sid}" viewBox="0 0 30 64">{inner}</symbol>'


def symbol_group(fid):
    """Gruppe: drei gestaffelte Figuren desselben Aussehens, dahinter zwei blassere (Menge statt Dreiergruppe, Blindtest 2026-10-17)."""
    one = "ill-p-" + slug(fid) + "-1"
    return (symbol_person(fid).replace(f'id="ill-p-{slug(fid)}"', f'id="{one}"')
            + f'<symbol id="ill-p-{slug(fid)}" viewBox="0 0 30 64"><use href="#{one}" x="0" y="11" width="16" height="35" opacity=".5"/>'
              f'<use href="#{one}" x="14" y="11" width="16" height="35" opacity=".5"/><use href="#{one}" x="-4" y="17" width="22" height="47" opacity=".8"/>'
              f'<use href="#{one}" x="12" y="17" width="22" height="47" opacity=".8"/><use href="#{one}" x="3" y="10" width="25" height="54"/></symbol>')


def symbol_attrs():
    return "".join(f'<symbol id="ill-a-{k}" viewBox="{ATTR_VB}">{v}</symbol>' for k, v in ATTR.items())


def symbol_library():
    out = [symbol_attrs()]
    for fid, p in FIGS.items():
        if p is None:
            continue
        out.append(symbol_group(fid) if fid in GROUPS else symbol_person(fid))
    return "".join(out)


def symbol_render():
    return {fid: "ill-p-" + slug(fid) for fid, p in FIGS.items() if p is not None}


# ------------------------------------------------------------------ Stil «Anime»: Brustbild (Parameter für bilder_anime.CHAR)
FRONT = {
    "short": "M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q8-6 0-6.6Q-8-6-10.6-.4z",
    "long": "M-10.6-1Q-10.5-11.6 0-12Q10.5-11.6 10.6-1Q7-6.4 .8-7.6L0-5.4-.8-7.6Q-7-6.4-10.6-1z",
    "bald": "M-10.6 1Q-10.8-6-8.6-8.6Q-6-6.8-6.4-1z M10.6 1Q10.8-6 8.6-8.6Q6-6.8 6.4-1z",
    "veil": "M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z",
}
BACK_LONG = "M-10.6 -2Q-12.5 9-10 17L-5.6 16Q-8.4 7-7.6-1z M10.6 -2Q12.5 9 10 17L5.6 16Q8.4 7 7.6-1z"
BEARD = {"short": "M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z",
         "full": "M-8.4 5Q-8 14 0 15.6Q8 14 8.4 5Q6.6 10.4 0 11Q-6.6 10.4-8.4 5z",
         "long": "M-8.6 4.6Q-9 15 0 19Q9 15 8.6 4.6Q6.6 10.6 0 11.2Q-6.6 10.6-8.6 4.6z"}


def anime_char(fid):
    p = FIGS[fid]
    c = {"hair": p["hair"], "robe": p["robe"]}
    if p.get("mantle"):
        c["mantle"] = p["mantle"]
    hd = p.get("head")
    st = p["style"]
    if hd and hd[0] in ("veil", "hood"):
        c["veil"] = hd[1]
        c["front"] = FRONT["veil"]
    elif st == "curls":
        c["curls"] = True
    elif st in FRONT:
        c["front"] = FRONT[st]
    if st == "long" and not hd:
        c["back"] = BACK_LONG
    if p.get("beard"):
        c["beard"] = BEARD[p["beard"]]
    if hd and hd[0] == "crown":
        c["crown"] = True
    if hd and hd[0] == "helmet":
        c["helmet"] = True
    if hd and hd[0] == "turban":
        c["turban"] = hd[1]
    if hd and hd[0] == "band":
        c["band"] = hd[1]
    if hd and hd[0] == "wreath":
        c["wreath"] = True
    for k in ("belt", "sash", "trim", "wings", "chains", "bound", "fur", "breast", "plate", "toga", "tassels"):
        if p.get(k):
            c[k] = p[k]
    if p["age"] in ("young", "child"):
        c["young"] = True
    if p["age"] == "child":
        c["child"] = True
    if p["age"] == "old":
        c["old"] = True
    if p["age"] == "baby":
        c["baby"] = True
    if p.get("attr"):
        c["attr"] = "an-a-" + p["attr"]
    return c


def anime_chars():
    return {slug(fid): anime_char(fid) for fid, p in FIGS.items() if p is not None}


def anime_attrs():
    return "".join(f'<symbol id="an-a-{k}" viewBox="{ATTR_VB}">{v}</symbol>' for k, v in ATTR.items())


# ------------------------------------------------------------------ Weitere Figuren aus figuren_daten/*.json
# Aufbau: {"FIG-…": {"robe": "#…", "mantle": "#…"|null, "hair": "#…", "style": "short|curls|long|bald|none",
#          "beard": null|"short"|"full"|"long", "head": null|["veil", "#…"]|["turban", "#…"]|["hood", "#…"]|["band", "#…"]|["crown"]|["helmet"]|["wreath"],
#          "age": "adult|young|old|child|baby", "sex": "m|f", "attr": null|"<Attribut aus ATTR>", weitere Schalter: belt, sash, trim, wings, bound, chains, fur, breast, toga, tassels},
#  "_group": ["FIG-…"]  (Einträge, die als Gruppe von drei Figuren gezeichnet werden)}
def _load_extra():
    import json
    import pathlib
    d = pathlib.Path(__file__).resolve().parent / "figuren_daten"
    for f in sorted(d.glob("*.json")) if d.exists() else []:
        data = json.loads(f.read_text(encoding="utf-8"))
        for g in data.pop("_group", []):
            GROUPS.add(g)
        for fid, p in data.items():
            if fid in FIGS:
                raise SystemExit(f"{f.name}: Figur {fid} doppelt")
            if p.get("head"):
                p["head"] = tuple(p["head"])
            if p.get("attr") and p["attr"] not in ATTR:
                raise SystemExit(f"{f.name}: Attribut {p['attr']} unbekannt (vorhanden: {', '.join(sorted(ATTR))})")
            FIGS[fid] = F(**{k: v for k, v in p.items()})


_load_extra()
