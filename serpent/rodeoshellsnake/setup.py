# -*- coding: utf-8 -*-


from cx_Freeze import setup, Executable

setup(
	# Nom de notre futur programme:
    name = "rodeoshellsnake",
    # Version de notre futur programme:
    version = "1.1",
    # Description de notre futur programme:
    description = "Snake game (Coded with Python3 + pygame).",
    # Notre exécutable QUI EST BIEN NOTRE PROGRAMME PRINCIPAL:
    executables = [Executable("rodeoshellsnake.py", base = "Win32GUI")]
)