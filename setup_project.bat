@echo off

REM Créer les dossiers
mkdir descriptions implementations tests visualisations analyses ressources

REM Créer les fichiers
type nul > main.py
type nul > descriptions\description_simple.md
type nul > implementations\implementation1.py
type nul > implementations\implementation2.py
type nul > tests\test_implementation1.py
type nul > tests\test_implementation2.py
type nul > visualisations\visualisation.py
type nul > analyses\analyse_complexite.md
type nul > ressources\.gitkeep

echo Structure du projet créée avec succès!

      