#!/usr/bin/env python3
"""Gemeinsame Handbibliothek für Bildzeichen (docs/SYMBOLPROZESS.md, Runde 11, 2026-10-25).

Hände wurden bisher in jedem Zeichen neu gezeichnet und waren oft Fäustlinge, Keile oder Balken (Durchsicht: «Hände fast
durchweg mangelhaft»). Alle Zeichen mit Händen setzen ihre Hände aus diesen Bausteinen zusammen. Jede Funktion gibt
SVG-Inhalt in einem eigenen Koordinatensystem zurück (Box im Docstring); platzieren mit
`f'<g transform="translate(x y) rotate(a) scale(s)">{hand_…()}</g>'`, spiegeln mit scale(-1 1).

Regeln: eine Silhouette mit Kontur nur aussen (Teile zuerst dick in Tinte, darüber hautfarben ohne Strich), Daumen klar
abgesetzt, Finger verschieden lang, Ärmel als Manschette.
"""
INK, SKIN, SLEEVE, GOLD = "#3B3226", "#E2AE80", "#5E7FA8", "#E8B931"


def sil(parts, fill=SKIN, sw=2.2):
    """Teile (Pfade) als eine Silhouette: Kontur nur aussen."""
    ink = "".join(f'<path d="{p}"/>' for p in parts)
    return (f'<g fill="{INK}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round">{ink}</g>'
            f'<g fill="{fill}">{ink}</g>')


def line(d, w=.7):
    return f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def cuff(d, fill=SLEEVE):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>'


def hand_empfangend(sleeve=SLEEVE):
    """Offene Hand, Handfläche nach oben, leicht gewölbt (wie 🫴); Ärmel links, Finger rechts. Box 0 0 32 18."""
    return (sil(["M7 7.4Q12 6.6 16 8.2L19 14.8Q12 15.6 7 14.4Z",
                 "M16 11Q22 11.4 25.6 10.4Q28.6 9.2 29.6 6.8Q30.4 5.6 31 6.6Q31.4 9 29.4 12Q27 15.2 21 15L16 14.8Z",
                 "M12.6 9Q15.4 5.4 18.4 3.8Q20.4 2.9 20.6 4.4Q20.6 5.4 18.8 6.8L16.4 9.8Z"])
            + line("M29.2 9.4Q27.4 12 23.4 12.6", .6) + cuff("M1.5 7H7.6V15H1.5Z", sleeve))


def hand_gebend(sleeve=SLEEVE):
    """Hand von oben, Handrücken oben, Finger nach links unten geöffnet (wie 🫳, lässt etwas fallen); Ärmel rechts.
    Box 0 0 32 18; Fingerspitze bei etwa (4.6, 11.4)."""
    return (sil(["M24 3.2Q18 2.6 13.6 4.6L12.8 10.6Q18.4 11.8 24 10.4Z",
                 "M14 6Q8.6 6.8 6 9.2Q4.4 10.8 5.4 12Q6.6 12.8 8.4 11.6L14.2 10.4Z",
                 "M16.4 9.8Q15.6 12.8 14.2 14.8Q13.4 15.8 12.6 15.2Q12 14.4 12.8 12.8L13.8 9.6Z"])
            + line("M6.4 10.4Q9 8.6 12.4 8.2", .6) + cuff("M30.5 2.8H23.6V11H30.5Z", sleeve))


def muenze(cx, cy, r=2.4):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{GOLD}" stroke="{INK}" stroke-width="1"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * .55:.2f}" fill="none" stroke="#B8891A" stroke-width=".6"/>')


def almosen():
    """Almosen geben: gebende Hand von oben legt eine Münze in eine offene, empfangende Hand. viewBox 0 -2 38 32."""
    return (f'<g transform="translate(24.2 13.2) rotate(-35) scale(.72) translate(-4.6 -11.4)">{hand_gebend()}</g>'
            + muenze(24.6, 20.2) + line("M24.6 14.8v1.3M22.8 15.3l.7 1M26.4 15.3l-.7 1", .55)
            + f'<g transform="translate(0 13)">{hand_empfangend()}</g>')
