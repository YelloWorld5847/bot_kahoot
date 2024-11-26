import sys
from cx_Freeze import setup, Executable

# Inclure les bibliothèques nécessaires
packages = ["tkinter", "selenium", "requests", "datetime", "time"]  # Ajoute les bibliothèques spécifiques à ton projet

# Déterminer l'application principale à convertir en .exe
script_name = "app_tiktok.py"  # Remplace par le nom de ton script Python

# Options de compilation
build_options = {
    "packages": packages,
    "include_files": ['mots_cles.json'],  # Si tu as des fichiers supplémentaires à inclure (images, fichiers de données, etc.)
    "excludes": [],  # Bibliothèques à exclure si nécessaire
}

# Configuration de l'exécutable
executables = [Executable(script_name, base=None, target_name="bot_tiktokTEST.exe", icon="tiktok_logo_icon_188431.ico")]

# Setup cx_Freeze
setup(
    name="bot_tiktok_app",
    version="1.0",
    description="c'est un bot tiktok",
    options={"build_exe": build_options},
    executables=executables,
)
