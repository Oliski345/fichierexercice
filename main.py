import os
from datetime import datetime, timedelta
from pathlib import Path
import shutil
import json
import csv

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
# chemin = Path("donnees/fichier.txt")
# # Obtenir le répertoire parent
# parent = chemin.parent
# print(f"Répertoire parent: {parent}")
# # obtenir le nom du fichier
# nom = chemin.name
# print(f"Nom du fichier: {nom}")
# # Obtenir l'extension
# extension = chemin.suffix
# print(f"Extension du fichier: {extension}")
# # Vérifier si le fichier existe
# if chemin.exists():
#     print("Le fichier existe")
# # chemin absolu
# chemin_absolu = chemin.absolute()
# print(f"Chemin absolu: {chemin_absolu}")
# # Joindre des chemins
# nouveau_chemin = Path("dossier") / "sous-dossier" / "fichier.txt"
# print(f"nouveau_chemin: {nouveau_chemin}")
# # répertoire de base
# home = Path.home()
# print(f"répertoire utilisateur: {home}")
#
# Path("SIM/chimie/Structure de données/ math").mkdir(parents=True, exist_ok=True)
# Path("SIM/Structure de données").mkdir(parents=True, exist_ok=True)
# Path("SIM/math").mkdir(parents=True, exist_ok=True)
# Path("e/f/g/h").mkdir(parents=True, exist_ok=True)

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

moncheminnom = "C:\\Olivier Pinard"
chemin_prog = Path(moncheminnom).joinpath("prog2")
chemin_prog.mkdir(parents=True, exist_ok=True)
chemin_prog_intra = chemin_prog.joinpath("projetpoo.txt")
chemin_prog_intra.mkdir(parents=True, exist_ok=True)
chemin_philosophie = Path(moncheminnom).joinpath("philosophie")
chemin_philosophie.mkdir(parents=True, exist_ok=True)
chemin_math = Path(moncheminnom).joinpath("math")
chemin_math.mkdir(parents=True, exist_ok=True)
chemin_math_intra = chemin_math.joinpath("intra.txt")
chemin_math_intra.mkdir(parents=True, exist_ok=True)


# class GestionNoteMathematique:
#     """Cette classe sera utilisée pour gérer un système
#         de notes mathématiques organisées par catégories
#         """
#
#     def __init__(self, dossier_racine=None):
#         """Initialisation de la classe GestionNoteMathematique"""
#         if dossier_racine is None:
#             self.dossier_racine = Path.home() / 'MathNotes'
#         else:
#             mondossier_Math = dossier_racine + "\\MathNotes"  # Variable texte pour indiquer le chemin
#             self.dossier_racine = Path(mondossier_Math)  # Création du chemin
#         self.categories = ["algebre", "analyse", "geometrie", "probabilites", "archives"]
#
#     def creer_structure_dossiers(self):
#         """Ici la structure des dossiers pour
#         les notes de mathématiques doit être créé"""
#         self.dossier_racine.mkdir(exist_ok=True)
#
#         # Création des sous dossiers
#         for categorie in self.categories:
#             dossier_categorie = self.dossier_racine / categorie
#             dossier_categorie.mkdir(exist_ok=True)
#
#         print(f"La structure de dossiers a été créée dans {self.dossier_racine}")
#
#     def creer_note(self, categorie, titre, contenu):
#
#         """Cette méthode va créer une nouvelle note mathématique dans la
#             catégorie spécifiée"""
#         categories_valides = self.categories[:-1]
#         if categorie not in categories_valides:
#             print(
#                 f"Erreur: la catégorie {categorie} est invalide. La liste des catégories disponible est"
#                 f" {categories_valides}")
#             return None
#         date_actuelle = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
#         nom_fichier = f"{date_actuelle}_{titre.replace(' ', '_')}.txt"
#
#         chemin_fichier = self.dossier_racine / categorie / nom_fichier  # Chemin complet du fichier
#
#         contenu_complet = f"Titre:{titre}\nDate:{date_actuelle}\n\n{contenu}"
#
#         chemin_fichier.write_text(contenu_complet, encoding="utf-8")
#         print(f"Note créée:{chemin_fichier}")
#         return chemin_fichier
#
#     def rechercher_note_par_titre(self, titre):
#         """Rechercher la note par titre"""
#         resultats = []
#         titre_lower = titre.lower()
#         categories_valides = self.categories[:-1]
#         for categorie in categories_valides:
#             dossier_categorie = self.dossier_racine / categorie
#             if not dossier_categorie.exists():
#                 continue
#             for fichier in dossier_categorie.iterdir():
#                 # Ici on vérifie si c'est un fichier et si le titre est dans le nom
#                 if fichier.is_file() and titre_lower in fichier.name.lower():
#                     resultats.append(fichier)
#
#         return resultats
#
#     def rechercher_note_par_contenu(self, texte):
#
#         resultats = []
#         texte_lower = texte.lower()
#         categories_valides = self.categories[:-1]
#         for categorie in categories_valides:
#             dossier_categorie = self.dossier_racine / categorie
#             if not dossier_categorie.exists():
#                 continue
#             for fichier in dossier_categorie.iterdir():
#                 # Ici on vérifie si c'est un fichier et si le titre est dans le nom
#                 if fichier.is_file() and fichier.suffix == '.txt':
#                     try:
#                         contenu = fichier.read_text(encoding="utf-8")
#                         if texte_lower in contenu.lower():
#                             resultats.append(fichier)
#                     except Exception as e:
#                         print(f"Erreur lors de la lecture de {fichier}: {e}")
#
#         return resultats
#
#     def archiver_notes_anciennes(self, jours):
#         """
#         Déplace les notes plus anciennes que le nombre de jours spécifié vers le dossier archives.
#
#         """
#         # Calculer la date limite
#         delta = timedelta(days=1)
#         date_limite = datetime.now() - delta
#         dossier_archives = self.dossier_racine / "archives"
#
#         # S'assurer que le dossier archives existe
#         dossier_archives.mkdir(exist_ok=True)
#
#         notes_archivees = 0
#
#         # Parcourir tous les dossiers de catégories (sauf archives)
#         for categorie in self.categories[:-1]:  # Toutes sauf "archives"
#             dossier_categorie = self.dossier_racine / categorie
#
#             # Vérifier si le dossier existe
#             if not dossier_categorie.exists():
#                 continue
#
#             # Parcourir tous les fichiers de la catégorie
#             for fichier in dossier_categorie.iterdir():
#                 # Vérifier si c'est un fichier
#                 if fichier.is_file():
#                     # Obtenir la date de modification du fichier
#                     temps_modification = fichier.stat().st_mtime
#                     date_modification = datetime.fromtimestamp(temps_modification)
#
#                     # Vérifier si le fichier est plus ancien que la date limite
#                     if date_modification < date_limite:
#                         # Chemin de destination dans les archives
#                         chemin_destination = dossier_archives / fichier.name
#
#                         # Déplacer le fichier
#                         fichier.rename(chemin_destination)
#                         notes_archivees += 1
#
#         print(f"{notes_archivees} note(s) archivée(s)")
#         return notes_archivees
#
#     def afficher_resultats(self, resultats):
#         """
#         Affiche les résultats d'une recherche.
#         """
#         if not resultats:
#             print("Aucun résultat trouvé.")
#         else:
#             print(f"{len(resultats)} note(s) trouvée(s):")
#             for i, chemin in enumerate(resultats, 1):
#                 print(f"{i}. {chemin}")
#
#
# monchemin2 = "C:\\2475333"
# G1 = GestionNoteMathematique(monchemin2)
# G1.creer_structure_dossiers()
#
# G1.creer_note("algebre", "Equations du second degré",
#               "Formule: x = (-b ± √(b² - 4ac)) / 2a\n\nExemple: Pour 2x² + 3x - 5 = 0\na=2, b=3, c=-5")
#
# # G1.creer_note("analyse", "Formule de Taylor",
# #                             "f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + ...\n
# #                             \nExemple: ex ≈ 1 + x + x²/2 + x³/6 + ...")
# #
# G1.creer_note("geometrie", "Théorème de Pythagore",
#               "a² + b² = c²\n\nDans un triangle rectangle, le carré de "
#               "l'hypoténuse est égal à la somme des carrés des deux autres côtés.")
#
# # print(" Recherche par titre pour le titre 'equation'")
# # resultats_titre=G1.rechercher_note_par_titre("equation")
# # print(resultats_titre)
#
# print(" Recherche par contenu pour le texte 'triangle'")
# resultats_titre = G1.rechercher_note_par_contenu("triangle")
# print(resultats_titre)

data = {"nom": "Olivier", "Sport": "Hockey", "age": 18}
with open("data_scimoli.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data_scimoli.json", "r") as f:
    data_lue = json.load(f)
    print(data_lue["Sport"])

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nom", "Sport", "Age"])
    writer.writerow(["Olivier", "Hockey", 18])

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
