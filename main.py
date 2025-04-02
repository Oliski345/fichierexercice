import os
from datetime import datetime
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


class GestionNoteMathematique:
    """Cette classe sera utilisée pour gérer un système
        de notes mathématiques organisées par catégories
        """

    def __init__(self, dossier_racine=None):
        """Initialisation de la classe GestionNoteMathematique"""
        if dossier_racine is None:
            self.dossier_racine = Path.home() / 'MathNotes'
        else:
            mondossier_math = dossier_racine + "\\MathNotes"
            self.dossier_racine = Path(mondossier_math)
        self.categories = ["algebre", "analyse", "geometrie", "probabilites", "archives"]

    def creer_structure_dossiers(self):
        """Ici la structure des dossiers pour
        les notes de mathématiques doit être créé"""
        self.dossier_racine.mkdir(exist_ok=True)

        # Création des sous dossiers
        for categorie in self.categories:
            dossier_categorie = self.dossier_racine / categorie
            dossier_categorie.mkdir(exist_ok=True)

        print(f"La structure de dossiers a été créée dans {self.dossier_racine}")

    def creer_note(self, categorie, titre, contenu):
        """Cette méthode va créer une nouvelle mathématique dans la catégorie spécifiée"""
        categorie_valides = self.categories[:-1]
        if categorie not in categorie_valides:
            print(f"Erreur: la catégorie {categorie} est invalide. La liste des catégories disponibles"
                  f" est {categorie_valides}")
            return None
        date_actuelle = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        nom_fichier = f"{date_actuelle}_{titre.replace(' ', '_')}.txt"
        chemin_fichier = self.dossier_racine / categorie / nom_fichier  # chemin complet du fichier

        contenu_complet = f"Titre: {titre}\n Date: {date_actuelle}\n\n{contenu}"
        chemin_fichier.write_text(contenu_complet, encoding="utf-8")
        print(f"Note créée:{chemin_fichier}")
        return chemin_fichier

    def rechercher_note_par_titre(self, titre):
        """Rechercher la note par titre"""
        resultats = []
        titre_lower = titre.lower()
        categorie_valides = self.categories[:-1]
        for categorie in categorie_valides:
            dossier_categorie = self.dossier_racine / categorie
            if not dossier_categorie.exists():
                continue
            for fichier in dossier_categorie.iterdir():
                # Ici, on vérifie si c'est un fichier et si le titre est dans le nom
                if fichier.is_file() and fichier.suffix == ".txt":
                    try:
                        contenu = fichier.read_text(encoding="utf-8")
                        if titre_lower in contenu.lower():
                            resultats.append(fichier)
                    except Exception as e:
                        print(f"Erreur lors de la lecture de {fichier}: {e}")

            return resultats


monchemin2 = "C:\\Users\\2475333"
G1 = GestionNoteMathematique(monchemin2)
G1.creer_structure_dossiers()

G1.creer_note("algebre", "equation du second degré",
              "Formule: x = (-b ± √(b² - 4ac)) / 2a\n\nExemple: Pour 2x² + 3x - 5 = 0\na=2, b=3, c=-5")
G1.creer_note("analyse", "Formule de Taylor",
              "f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + ...\n\nExemple: ex ≈ 1 + x + x²/2 + x³/6 + ...")
G1.creer_note("geometrie", "Théorème de Pythagore",
              "a² + b² = c²\n\nDans un triangle rectangle, "
              "le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés.")
print(" Recherche par titre pour le titre 'equation'")
resultats_titre = G1.rechercher_note_par_titre("equation")
print(resultats_titre)
