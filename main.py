import os
from pathlib import Path
import shutil
# répertoire de travail actuel
repertoire_actuelle = os.getcwd()
print(repertoire_actuelle)

# # Chemin absolu vers un fichier
# chemin_absolu = os.path.join(repertoire_actuelle, 'donnees', "fichier.txt")
# print(chemin_absolu)
#
# # Chemin relatif
# chemin_relatif = os.path.join("donnees", "fichier.txt")
# print(chemin_relatif)
#
# fichier_exist = os.path.exists(r"C:\Users\2475333\PycharmProjects\fichierexercice\main.py")
# print(fichier_exist)

# Créer un objet Path
chemin = Path("donnees/fichier.txt")
# Obtenir le répertoire parent
parent = chemin.parent
print(f"Répertoire parent: {parent}")
# obtenir le nom du fichier
nom = chemin.name
print(f"Nom du fichier: {nom}")
# Obtenir l'extension
extension = chemin.suffix
print(f"Extension du fichier: {extension}")
# Vérifier si le fichier existe
if chemin.exists():
    print("Le fichier existe")
# chemin absolu
chemin_absolu = chemin.absolute()
print(f"Chemin absolu: {chemin_absolu}")
# Joindre des chemins
nouveau_chemin = Path("dossier") / "sous-dossier" / "fichier.txt"
print(f"nouveau_chemin: {nouveau_chemin}")
# répertoire de base
home = Path.home()
print(f"répertoire utilisateur: {home}")

Path("SIM/chimie/Structure de données/ math").mkdir(parents=True, exist_ok=True)
Path("SIM/Structure de données").mkdir(parents=True, exist_ok=True)
Path("SIM/math").mkdir(parents=True, exist_ok=True)
Path("e/f/g/h").mkdir(parents=True, exist_ok=True)

# dossier vide
# os.rmdir("SIM/Structure de données")
# Path("SIM/chimie").rmdir()

# dossier avec contenue
# shutil.rmtree("SIM/math")


# monchemin2 = "C:\\Nouveau dossier"
# chemin_chimie = Path(monchemin2).joinpath("chimie")
# (Path(monchemin2).joinpath("math")).mkdir(parents=True, exist_ok=True)
# chemin_chimie.mkdir(parents=True, exist_ok=True)
# chemin_math = Path(monchemin2).joinpath("math")
# chemin_math_intra1 = chemin_math.joinpath("intra1")
# chemin_math_intra1.mkdir(parents=True, exist_ok=True)
# chemin_math_intra2 = chemin_math.joinpath("intra2")
# chemin_math_intra2.mkdir(parents=True, exist_ok=True)
# shutil.move(chemin_math_intra1, chemin_chimie)
