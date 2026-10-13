"""Bücher des Alten Testaments in MACULA Hebrew (Dateinamen)."""
# Dateipräfixe von MACULA Hebrew (WLC/lowfat/<NN>-<Buch>-<KKK>-lowfat.xml) je Buchcode
FILES = {code: f"{i:02d}-{name}" for i, (code, name) in enumerate([
    ("GEN", "Gen"), ("EXO", "Exo"), ("LEV", "Lev"), ("NUM", "Num"), ("DEU", "Deu"), ("JOS", "Jos"), ("JDG", "Jdg"),
    ("RUT", "Rut"), ("1SA", "1Sa"), ("2SA", "2Sa"), ("1KI", "1Ki"), ("2KI", "2Ki"), ("1CH", "1Ch"), ("2CH", "2Ch"),
    ("EZR", "Ezr"), ("NEH", "Neh"), ("EST", "Est"), ("JOB", "Job"), ("PSA", "Psa"), ("PRO", "Pro"), ("ECC", "Ecc"),
    ("SNG", "Sng"), ("ISA", "Isa"), ("JER", "Jer"), ("LAM", "Lam"), ("EZK", "Ezk"), ("DAN", "Dan"), ("HOS", "HOS"),
    ("JOL", "Jol"), ("AMO", "Amo"), ("OBA", "Oba"), ("JON", "Jon"), ("MIC", "Mic"), ("NAM", "Nam"), ("HAB", "Hab"),
    ("ZEP", "Zep"), ("HAG", "Hag"), ("ZEC", "Zec"), ("MAL", "Mal")], start=1)}
