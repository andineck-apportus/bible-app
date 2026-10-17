#!/usr/bin/env python3
"""Bauteile für Gegenstände, Orte und Zeichen, die in den Bildern der übersetzten Bücher dazukommen.

Je Lexikon-Eintrag: Bauteil-ID im Stil «Symbol» (ill-*), viewBox, Zeichnung, Platzierung im Feld (siehe
bilder_auto.META) und Grösse. Der Stil «Anime» übernimmt die Bauteile (an-*), damit Gegenstände und Zeichen in
beiden Stilen gleich gelesen werden. Zusätzliche Bauteile anderer Bücher stehen in bildsymbole_daten/*.json
(gleicher Aufbau: {"FIG-…": {"sym": "ill-…", "vb": "0 0 w h", "svg": "…", "place": "floor", "size": [w, h]}}).

KI-Entwurf (Claude) vom 2026-10-17 auf Wunsch von Andi Neck; eigene Zeichnungen (CC0), keine fachliche Prüfung.
"""
import json
import pathlib

INK = "#3B3226"


def S(sym, vb, svg, place, size):
    return {"sym": sym, "vb": vb, "svg": svg, "place": place, "size": list(size)}


WAVES = "".join(f'<path d="M{x} {y}q6-4 12 0t12 0" fill="none" stroke="#A9D2F0" stroke-width="1.6"/>' for x, y in ((10, 30), (60, 26), (120, 34), (150, 50), (30, 52), (90, 46)))
SYMBOLS = {
    # ---- Orte
    "FIG-ORT-SEE": S("ill-see", "0 0 186 70",
                     '<path d="M0 22q30-14 60-4t60-6 66 6V70H0z" fill="#9AAE7E"/><path d="M0 30h186v40H0z" fill="#5DA7DB"/>'
                     + WAVES + '<path d="M0 30h186" stroke="#2E5478" stroke-width="1.2"/>', "band", (186, 70)),
    "FIG-ORT-WUESTE": S("ill-wueste", "0 0 186 70",
                        '<path d="M0 18q40-12 80 0t106-4V70H0z" fill="#E8C98E"/><path d="M0 34q50-10 100 2t86 0V70H0z" fill="#DDB877"/>'
                        '<g fill="#8A9A6A"><path d="M30 30q2-8 4 0zM150 40q2-7 4 0z"/></g>', "band", (186, 70)),
    # ---- Gegenstände
    "FIG-OBJ-BROT": S("ill-brot", "0 0 24 14", f'<path d="M2 11q0-8 10-8t10 8q0 2-10 2T2 11z" fill="#D9A15E" stroke="{INK}" stroke-width="1"/>'
                      '<path d="M7 6l2 4M12 5l1 5M17 6l-1 4" stroke="#A8713A" stroke-width="1"/>', "floor", (16, 10)),
    "FIG-OBJ-FISCH": S("ill-fisch", "0 0 26 12", f'<path d="M2 6q8-6 16 0-8 6-16 0zM18 6l6-4v8z" fill="#8FA3B8" stroke="{INK}" stroke-width=".9"/><circle cx="6" cy="5.4" r=".9" fill="{INK}"/>', "floor", (18, 9)),
    "FIG-OBJ-GROSSER-FISCH": S("ill-grosser-fisch", "0 0 120 64",
                               f'<path d="M6 34Q20 6 64 8q34 2 44 22l10-14v38l-10-14Q98 54 64 58 20 60 6 34z" fill="#5E7F9A" stroke="{INK}" stroke-width="1.6"/>'
                               '<path d="M14 40q30 14 70 8q14-2 24-12" fill="#9CB4C4"/><circle cx="24" cy="26" r="3" fill="#FFFDF6" stroke="#3B3226"/><circle cx="24.6" cy="26.4" r="1.4" fill="#3B3226"/>'
                               '<path d="M8 36q6 2 12 0" fill="none" stroke="#3B3226" stroke-width="1.4"/><path d="M50 12q4 8 0 16M62 10q4 9 0 18" fill="none" stroke="#4A6E8A" stroke-width="1.2"/>', "big", (120, 64)),
    "FIG-OBJ-LAMPE": S("ill-lampe", "0 0 24 16", '<path d="M2 11q8-7 16 0l4-2v3q-11 6-20-1z" fill="#B07A3E" stroke="#3B3226" stroke-width="1"/><path d="M20 9q3-5 0-9-2 4 0 9z" fill="#F2B53A"/>', "hand", (16, 11)),
    "FIG-OBJ-SCHIFF": S("ill-schiff", "0 0 110 80",
                        f'<path d="M6 54h98l-12 18H18z" fill="#7A5A34" stroke="{INK}" stroke-width="1.6"/><path d="M6 54h98" stroke="#5B4630" stroke-width="3"/>'
                        f'<path d="M54 54V6" stroke="{INK}" stroke-width="2.4"/><path d="M56 8q34 16 0 40z" fill="#F4F1EA" stroke="{INK}" stroke-width="1.2"/><path d="M52 10Q26 24 52 44z" fill="#E7DCC4" stroke="{INK}" stroke-width="1.2"/>'
                        f'<path d="M98 54l10-12" stroke="{INK}" stroke-width="1.6"/><g stroke="#5B4630" stroke-width="1.2"><path d="M24 72l-6 6M40 72l-6 6M56 72l-6 6M72 72l-6 6"/></g>', "big", (110, 80)),
    "FIG-OBJ-LOS": S("ill-los", "0 0 26 14", f'<g stroke="{INK}" stroke-width=".9"><ellipse cx="6" cy="8" rx="5" ry="4" fill="#E7DCC4"/><ellipse cx="15" cy="8" rx="5" ry="4" fill="#E7DCC4"/><ellipse cx="21" cy="6" rx="4.4" ry="3.6" fill="#3B3226"/></g>'
                     '<path d="M4 7h4M13 7l4 2" stroke="#3B3226" stroke-width="1"/>', "hand", (18, 10)),
    "FIG-OBJ-RIZINUS": S("ill-rizinus", "0 0 70 80",
                         '<path d="M35 80V24M35 60Q22 54 16 44M35 50q12-6 20-16M35 38Q26 30 22 20M35 34q8-6 12-14" stroke="#6B5A2A" stroke-width="2.2" fill="none"/>'
                         + "".join(f'<g transform="translate({x} {y}) rotate({r}) scale({k})"><path d="M0 0L-9-6-6-13-1-9 0-17 3-9 8-13 11-6 2 0z" fill="#5E9B3D" stroke="#3B3226" stroke-width=".7" stroke-linejoin="round"/><path d="M1 0L-6-9M1 0V-14M1 0l8-9" stroke="#3E6E2A" stroke-width=".5"/></g>'
                                   for x, y, r, k in ((16, 46, -30, 1.3), (55, 36, 25, 1.3), (22, 22, -15, 1.2), (47, 22, 15, 1.2), (35, 14, 0, 1.3), (28, 56, -40, 1.1), (44, 52, 35, 1.1))), "floor", (52, 60)),
    "FIG-OBJ-RIZINUS-VERDORRT": S("ill-rizinus-verdorrt", "0 0 70 80",
                                  '<path d="M34 80V36M34 56Q22 50 16 44M34 48q12-4 18-10" stroke="#7A6A4A" stroke-width="2.4" fill="none"/>'
                                  + "".join(f'<path transform="translate({x} {y}) rotate({r})" d="M0 0q-10 2-10 10 4-2 6 0 2-4 4-2 3 0 4 2 0-5-4-10z" fill="#B49A5A" stroke="#3B3226" stroke-width=".8"/>'
                                            for x, y, r in ((16, 44, 60), (52, 38, -50), (34, 70, 170))), "floor", (52, 60)),
    "FIG-OBJ-WURM": S("ill-wurm", "0 0 24 12", '<path d="M2 9q3-6 6 0t6 0 6 0" fill="none" stroke="#B87A6A" stroke-width="3" stroke-linecap="round"/><circle cx="21" cy="8" r="2" fill="#B87A6A"/><circle cx="21.6" cy="7.4" r=".5" fill="#3B3226"/>', "floor", (16, 8)),
    "FIG-OBJ-RIND": S("ill-rind", "0 0 40 26", f'<g stroke="{INK}" stroke-width="1"><path d="M6 10q0-4 6-4h16q6 0 6 6v4q0 3-3 3H9q-3 0-3-3z" fill="#A0703A"/>'
                      '<path d="M9 19v6M14 19v6M26 19v6M31 19v6" stroke-width="2"/><path d="M33 9q7 0 6 6-1 4-5 3z" fill="#A0703A"/><path d="M34 8l-2-5M38 8l2-5" fill="none" stroke="#E7DCC4" stroke-width="1.6"/></g>', "floor", (40, 26)),
    "FIG-ORT-NINIVE": S("ill-ninive", "0 0 96 70",
                        f'<g stroke="{INK}" stroke-width="1.2"><path d="M32 30h32v-8h-6v-8h-20v8h-6z" fill="#C9A27A"/><path d="M38 14h20v-8H38z" fill="#B48A5E"/>'
                        '<path d="M2 34h92v34H2z" fill="#D8B48A"/><path d="M2 34v-6h8v6h8v-6h8v6h8v-6h8v6h12v-6h8v6h8v-6h8v6h8v-6h8v6" fill="#D8B48A"/>'
                        '<path d="M42 68V52q6-8 12 0v16z" fill="#5B4630"/><path d="M12 44h10v8H12zM74 44h10v8H74z" fill="#5B4630"/></g>'
                        '<path d="M6 60h28M62 60h28" stroke="#B48A5E" stroke-width="1"/>', "back", (96, 70)),
    "FIG-ORT-UFER": S("ill-ufer", "0 0 186 70", '<path d="M0 30h186v40H0z" fill="#5DA7DB"/>' + WAVES
                      + '<path d="M70 70q10-30 50-38t66-2V70z" fill="#E8C98E" stroke="#B49A5A" stroke-width="1.2"/>', "band", (186, 70)),
    "FIG-ORT-MEER-OFFEN": S("ill-meer-offen", "0 0 186 70", '<path d="M0 26q15-8 31 0t31 0 31 0 31 0 31 0 31 0V70H0z" fill="#4C8FC4" stroke="#2E5478" stroke-width="1.2"/>'
                            '<path d="M0 44q15-8 31 0t31 0 31 0 31 0 31 0 31 0V70H0z" fill="#3E7BAE"/>' + WAVES, "band", (186, 70)),
    "FIG-ORT-TIEFE": S("ill-tiefe", "0 0 186 140", '<rect width="186" height="140" fill="#2E5A80"/><rect width="186" height="40" fill="#4C8FC4"/>'
                       '<path d="M0 40q15-6 31 0t31 0 31 0 31 0 31 0 31 0" fill="none" stroke="#A9D2F0" stroke-width="1.6"/>'
                       + "".join(f'<path d="M{x} 140q-6-14 0-28t0-28" fill="none" stroke="#5E8B4A" stroke-width="2.4"/>' for x in (14, 30, 160, 172)), "band", (186, 140)),
    "FIG-ORT-HUETTE": S("ill-huette", "0 0 50 40", f'<g stroke="{INK}" stroke-width="1.1"><path d="M4 40V14M46 40V14" stroke="#7A5A34" stroke-width="2.2"/><path d="M0 16l25-12 25 12z" fill="#9A8A50"/></g>'
                        '<path d="M4 16l6-3M16 10l6-3M30 7l6 3M40 12l6 3" stroke="#6E8B3D" stroke-width="1.4"/>', "back", (54, 43)),
    "FIG-OBJ-ALTAR": S("ill-altar", "0 0 30 34", f'<path d="M5 18h20v16H5z" fill="#C9BFAA" stroke="{INK}" stroke-width="1"/><path d="M5 22h20M5 28h20M15 18v4M10 22v6M20 22v6" stroke="#8C8070" stroke-width=".8"/>'
                       '<path d="M10 18q-2-6 3-8 0 4 2 4 1-6 5-8-1 6 2 8 2 2 0 4z" fill="#E8843A"/><path d="M14 8q-3-4 1-8M19 6q3-3 0-6" fill="none" stroke="#A79A80" stroke-width="1.4"/>', "floor", (22, 25)),
    # ---- Zeichen
    "FIG-ZEICHEN-STURM": S("ill-z-sturm", "0 0 60 36", f'<path d="M8 20q-8 0-6-8 2-6 9-4 2-8 12-7 8 0 10 6 8-3 12 3 8 0 7 7-1 5-8 5H10z" fill="#5A6470" stroke="{INK}" stroke-width="1"/>'
                           '<path d="M28 20l-4 8h5l-3 8 9-11h-5l3-5z" fill="#F2C76E" stroke="#B08A2A" stroke-width=".6"/><path d="M42 24l6 8M48 22l6 8M14 24l-4 8" stroke="#6E8BAA" stroke-width="1.6" stroke-linecap="round"/>', "air", (44, 27)),
    "FIG-ZEICHEN-SCHLAFEN": S("ill-z-schlafen", "0 0 20 16", '<path d="M10 2a6 6 0 1 0 6 9 5 5 0 0 1-6-9z" fill="#F2E6CC" stroke="#8C8070" stroke-width=".8"/><circle cx="16" cy="3" r="1.2" fill="#B4A98F"/><circle cx="18.5" cy="7" r=".9" fill="#B4A98F"/>', "air", (14, 11)),
    "FIG-ZEICHEN-OPFER": S("ill-z-opfer", "0 0 30 34", '<use href="#ill-altar" width="30" height="34"/>', "air", (20, 23)),
    "FIG-ZEICHEN-BUSSE": S("ill-z-busse", "0 0 30 24", f'<path d="M3 4h12l2 18H1z" fill="#6A5E52" stroke="{INK}" stroke-width=".9"/><path d="M4 8h10M3 13h12M2 18h14" stroke="#4E453C" stroke-width=".7"/>'
                           '<g fill="#9A948C"><circle cx="6" cy="2" r=".9"/><circle cx="10" cy="1.4" r=".8"/><circle cx="13" cy="2.4" r=".7"/></g>'
                           f'<path d="M19 14h10q0 6-5 6t-5-6z" fill="#E7DCC4" stroke="{INK}" stroke-width=".9"/><path d="M18 22l12-12" stroke="#A33A2E" stroke-width="1.6" stroke-linecap="round"/>', "air", (26, 21)),
    "FIG-ZEICHEN-WIND": S("ill-z-wind", "0 0 30 20", '<g fill="none" stroke="#8C8070" stroke-width="1.8" stroke-linecap="round"><path d="M2 5h18q5 0 5-3"/><path d="M2 10h24q4 0 4 4"/><path d="M6 15h12q3 0 3 3"/></g>', "air", (24, 16)),
    "FIG-ZEICHEN-HITZE": S("ill-z-hitze", "0 0 30 30", '<g stroke="#D9622A" stroke-width="2" stroke-linecap="round"><path d="M15 1v5M15 24v5M1 15h5M24 15h5M5 5l3.5 3.5M21.5 21.5L25 25M5 25l3.5-3.5M21.5 8.5L25 5"/></g><circle cx="15" cy="15" r="6.5" fill="#F29A3A" stroke="#D9622A" stroke-width="1.4"/>', "air", (24, 24)),
    "FIG-ZEICHEN-ZORN": S("ill-z-zorn", "0 0 24 20", '<path d="M4 14q-4-1-3-5 1-4 5-3 1-5 6-5 5 0 6 4 5-1 5 4 0 5-5 5z" fill="#4A4A52" stroke="#2E2A2A" stroke-width=".8"/><path d="M7 10l3-3 2 3 3-3 2 3" fill="none" stroke="#E8843A" stroke-width="1.2"/>', "air", (18, 15)),
    "FIG-ZEICHEN-ERBARMEN": S("ill-z-erbarmen", "0 0 28 24", '<path d="M14 18C9 14 7 11 7 8.6A3 3 0 0 1 14 7.6a3 3 0 0 1 7 1C21 11 19 14 14 18z" fill="#E07A8A" stroke="#3B3226" stroke-width="1"/>'
                              f'<g fill="#C89B72" stroke="{INK}" stroke-width=".9"><path d="M1 16q3-1 6 2l7 4H6q-4 0-5-4z"/><path d="M27 16q-3-1-6 2l-7 4h8q4 0 5-4z"/></g>', "air", (24, 21)),
    "FIG-ZEICHEN-RETTUNG": S("ill-z-rettung", "0 0 24 26", '<path d="M0 22q3-3 6 0t6 0 6 0 6 0" fill="none" stroke="#4C9BD6" stroke-width="2"/><path d="M12 19V3M6 9l6-6 6 6" fill="none" stroke="#3B3226" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>', "air", (20, 22)),
    "FIG-ZEICHEN-FLIEHEN": S("ill-z-fliehen", "0 0 30 16", '<path d="M10 8h17M22 3l5 5-5 5" fill="none" stroke="#3B3226" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M1 4h6M3 8h5M1 12h6" stroke="#8C8070" stroke-width="1.4" stroke-linecap="round"/>', "air", (24, 13)),
    "FIG-ZEICHEN-HINAB": S("ill-z-hinab", "0 0 16 24", '<path d="M8 2v18M2 14l6 7 6-7" fill="none" stroke="#3B3226" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>', "air", (12, 18)),
    "FIG-ZEICHEN-NICHT-VERSTEHEN": S("ill-z-nicht-verstehen", "0 0 26 20", '<path d="M5 15q-4 0-4-4t5-4q1-5 7-5t7 4q5 0 5 5t-5 4z" fill="#C9C4BA" stroke="#8C8070" stroke-width="1.1"/><path d="M3.5 12q2-1.4 4 0M17 13q2-1.4 4 0" fill="none" stroke="#9E978A" stroke-width="1"/><path d="M11 6.6q0-2.4 2.4-2.4t2.4 2.2-2.4 2.4v1.6M13.4 13v.6" fill="none" stroke="#6A6458" stroke-width="1.7" stroke-linecap="round"/>', "air", (20, 16)),
    "FIG-ZEICHEN-VOLL": S("ill-z-voll", "0 0 22 22", f'<path d="M4 8h14l-2 13H6z" fill="#B07A3E" stroke="{INK}" stroke-width="1"/><path d="M3 8q4-6 8-2 4-6 8 2z" fill="#E8B84A" stroke="{INK}" stroke-width=".8"/><path d="M5 6l-3-2M17 6l3-2M11 3V0" stroke="#D9A441" stroke-width="1.2"/>', "air", (18, 18)),
    "FIG-ZEICHEN-ABLEHNEN": S("ill-z-ablehnen", "0 0 26 24", f'<path d="M7 22Q4 18 4 13V9q0-1.6 1.5-1.6T7 9v3V4.6q0-1.6 1.5-1.6T10 4.6V11V3.2q0-1.6 1.5-1.6T13 3.2V11V4.4q0-1.6 1.5-1.6T16 4.4V13l1.6-2.6q1-1.4 2.2-.6t.2 2.2L17 18q-2 4-6 4z" fill="#C89B72" stroke="{INK}" stroke-width="1" stroke-linejoin="round"/><path d="M20.5 4.5l3-2M21.5 8h3.5M20.5 11.5l3 2" stroke="{INK}" stroke-width="1.2" stroke-linecap="round"/>', "air", (18, 17)),
    "FIG-ZEICHEN-GEBEN": S("ill-z-geben", "0 0 28 20", f'<path d="M2 14q4-4 10-2l8 2q3 1 2 3H10" fill="#C89B72" stroke="{INK}" stroke-width="1"/><circle cx="20" cy="8" r="4" fill="#D9A441" stroke="#9C6F1C"/><path d="M24 8h3M25 4l2-2" stroke="#3B3226" stroke-width="1.2"/>', "air", (22, 16)),
    "FIG-ZEICHEN-HEILEN": S("ill-z-heilen", "0 0 30 24", f'<path d="M1 15h7l3-3q2-1.4 3.4 0l5.6 4.4q1.2 1.4-.4 2.2l-3.6-1.6H8l-2 2H1z" fill="#C89B72" stroke="{INK}" stroke-width="1" stroke-linejoin="round"/>'
                            '<circle cx="24" cy="13" r="5" fill="#BFE3A0" opacity=".85"/><circle cx="24" cy="13" r="2.2" fill="#6EB04E"/>'
                            '<path d="M24 11V5" stroke="#4E8A36" stroke-width="1.4" stroke-linecap="round"/><path d="M24 7q-4-2-5-5 4 0 5 4zM24 6q3-3 5-3-1 4-5 4z" fill="#6EB04E" stroke="#3E7A2E" stroke-width=".6"/>', "air", (22, 18)),
    "FIG-ZEICHEN-SEGNEN": S("ill-z-segnen", "0 0 24 26", '<path d="M12 0v4M4 3l2 3M20 3l-2 3" stroke="#F2C76E" stroke-width="1.6" stroke-linecap="round"/>'
                            f'<path d="M7 25V12q0-2 2-2t2 2V7q0-2 2-2t2 2v2q0-2 2-2t2 2v9q0 7-7 7z" fill="#C89B72" stroke="{INK}" stroke-width="1"/>', "air", (18, 20)),
    "FIG-ZEICHEN-SPRECHEN": S("ill-z-sprechen", "0 0 22 18", '<g fill="none" stroke="#3B3226" stroke-width="1.6" stroke-linecap="round"><path d="M4 5q3 4 0 8"/><path d="M9 2q5 7 0 14"/><path d="M14 0q7 9 0 18"/></g>', "air", (16, 13)),
    "FIG-ZEICHEN-VERKUENDIGEN": S("ill-z-verkuendigen", "0 0 30 20", f'<path d="M2 7h5l10-6v18L7 13H2z" fill="#D9A441" stroke="{INK}" stroke-width="1"/><g fill="none" stroke="#3B3226" stroke-width="1.4" stroke-linecap="round"><path d="M21 6q2 4 0 8"/><path d="M25 3q4 7 0 14"/></g>', "air", (22, 15)),
    "FIG-ZEICHEN-ZEIGEN": S("ill-z-zeigen", "0 0 26 14", f'<path d="M1 5h14l8-1q2 0 2 2t-2 2h-6v3q0 2-2 2H5q-4 0-4-4z" fill="#C89B72" stroke="{INK}" stroke-width="1"/>', "air", (20, 11)),
    "FIG-ZEICHEN-UMSTURZ": S("ill-z-umsturz", "0 0 30 26", f'<g stroke="{INK}" stroke-width="1"><path d="M2 25l3-16 9 2-2 14z" fill="#D8B48A"/><path d="M16 25l4-18 9 3-4 15z" fill="#D8B48A"/></g>'
                             '<path d="M8 12l-1 5 2 3-1 4M22 10l-2 5 2 3" fill="none" stroke="#3B3226" stroke-width="1.1"/><g fill="#B48A5E" stroke="#3B3226" stroke-width=".6"><path d="M12 3h4v3h-4zM24 1h3v3h-3zM5 3h3v3H5z"/></g>', "air", (22, 19)),
    "FIG-ZEICHEN-TOD": S("ill-z-tod", "0 0 34 26", f'<path d="M2 26V14Q2 2 15 2t13 12v12z" fill="#A79A80" stroke="{INK}" stroke-width="1.2"/><path d="M9 26V17q0-6 6-6t6 6v9z" fill="#3B3226"/>'
                         f'<circle cx="17" cy="19.5" r="7.5" fill="#C9BFAA" stroke="{INK}" stroke-width="1.2"/><path d="M13 17q4-2 7 1" fill="none" stroke="#8C8070"/>', "air", (24, 18)),
    "FIG-ZEICHEN-NACHT": S("ill-z-nacht", "0 0 16 16", '<circle cx="8" cy="8" r="7.6" fill="#2E3E5E"/><path d="M9 3a5 5 0 1 0 4 7 4 4 0 0 1-4-7z" fill="#F2E6CC"/>', "air", (12, 12)),
    "_HAFEN-R": S("ill-hafen-r", "0 0 186 70", '<path d="M0 30h186v40H0z" fill="#E8C98E"/><path d="M84 40h102v30H84z" fill="#5DA7DB"/><path d="M84 40h102" stroke="#2E5478" stroke-width="1"/>'
                  '<path d="M96 52q6-3 12 0t12 0M140 60q6-3 12 0t12 0" fill="none" stroke="#A9D2F0" stroke-width="1.4"/><path d="M76 40h12v30H76z" fill="#A07A44" stroke="#3B3226" stroke-width=".8"/>', "band", (186, 70)),
    "_HAFEN-L": S("ill-hafen-l", "0 0 186 70", '<path d="M0 30h186v40H0z" fill="#E8C98E"/><path d="M0 40h102v30H0z" fill="#5DA7DB"/><path d="M0 40h102" stroke="#2E5478" stroke-width="1"/>'
                  '<path d="M20 52q6-3 12 0t12 0M64 60q6-3 12 0t12 0" fill="none" stroke="#A9D2F0" stroke-width="1.4"/><path d="M98 40h12v30H98z" fill="#A07A44" stroke="#3B3226" stroke-width=".8"/>', "band", (186, 70)),
    "_STRAND": S("ill-strand", "0 0 186 34", '<path d="M0 8q40-8 93-4t93 2V34H0z" fill="#E8C98E" stroke="#B49A5A" stroke-width="1"/>', "band", (186, 34)),
    "_MEER-STILL": S("ill-meer-still", "0 0 186 70", '<path d="M0 30q31-3 62 0t62 0 62 0V70H0z" fill="#5DA7DB" stroke="#2E5478" stroke-width="1"/><path d="M0 50h186V70H0z" fill="#4C8FC4"/>'
                     '<path d="M20 42h20M90 46h24M140 40h18" stroke="#A9D2F0" stroke-width="1.4" stroke-linecap="round"/>', "band", (186, 70)),
    "FIG-SATAN": S("ill-satan", "0 0 40 50", '<path d="M20 2q14 4 16 20 4 14-6 26-10-6-10-2-2-4-10 2Q0 36 4 22 6 6 20 2z" fill="#3B3226" opacity=".85"/><path d="M20 8q8 4 10 14M14 10q-6 6-6 14" fill="none" stroke="#6A4A6A" stroke-width="1.6"/>', "back", (34, 42)),
}

EXTRA_DIR = pathlib.Path(__file__).resolve().parent / "bildsymbole_daten"


def all_symbols():
    out = dict(SYMBOLS)
    for f in sorted(EXTRA_DIR.glob("*.json")) if EXTRA_DIR.exists() else []:
        for k, v in json.loads(f.read_text(encoding="utf-8")).items():
            if k in out:
                raise SystemExit(f"{f.name}: Bauteil für {k} doppelt")
            out[k] = v
    return out


def symbol_defs():
    return "".join(f'<symbol id="{v["sym"]}" viewBox="{v["vb"]}">{v["svg"]}</symbol>' for v in all_symbols().values())
