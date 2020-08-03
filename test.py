import time
import Variable
import json

with open("Historique.json", "r", encoding="utf-8") as MyFile:
    Variable.dicHistorique = json.load(MyFile)

print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
print("| Nom du Joueur |   Resultat    |   nbAction    | nbDeplacement |    Energie    |    Satiété    |  Hydratation  |          Date          |")
print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
espace = " "

for k in Variable.dicHistorique :
    ligne = "|"
    compteur = 0
    compteurligne = 0

    try :
        while compteur != len(Variable.dicHistorique) -1 :
            while compteur != 7 :
                    # Mettre les score au centre de la case
                    variable = len(str(Variable.dicHistorique[k][compteur]))
                    espace = (15 - variable)// 2
                    espace1 = " " * espace
                    espace2 = " " * espace
                    if variable % 2 == 0 :
                        espace2 = " " * (espace +1)
                    if Variable.dicHistorique[k][compteur] == "Defaite" :
                        Variable.dicHistorique[k][compteur] = "\u001b[38;5;1mDefaite\033[0m"
                    elif Variable.dicHistorique[k][compteur] == "Victoire" :
                        Variable.dicHistorique[k][compteur] = "\u001b[38;5;82mVictoire\033[0m"
                    # J'agremente la ligne avec toutes les valeurs de chaque clé 
                    ligne = f'{ligne}{espace1}{Variable.dicHistorique[k][compteur]}{espace2}|'
                    compteur += 1
            print (f'{ligne}  {Variable.dicHistorique[k][7]}   |')
            print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    except :
            compteur = 7
        