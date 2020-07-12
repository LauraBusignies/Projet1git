import Variable
import os
import Display
import random

def clear():
    os.system('cls') #pour Windows

def afterClear():
    clear()
    Display.map1()

# Definir l
def entrerDeplacement():

    Variable.nombre = 1
    entrer = input("Entrez une instruction  : ")
    if entrer != "" :
        Variable.deplacement = entrer[0]
    if len(entrer) > 1 :
        Variable.nombre = entrer[1:]
    listeDeplacement= ["z", "q","s","d","o","r"]
    while Variable.deplacement not in listeDeplacement :
            print("Veuillez saisir une lettre entre Z, Q , S, D. \n Z pour monter \n S pour descendre \n D pour aller a droite \n Q pour aller a gauche")
            entrer = (input("Entrez une instruction : ")).lower()
            print()

            if entrer != "" :
                Variable.deplacement = entrer[0]
            if len(entrer) > 1 :
                Variable.nombre = entrer[1:]
    
# Capacité du Sac à dos 
def nombreObjet():
    Variable.compteurS = 0
    for key in Variable.sac_a_dos:
        if Variable.sac_a_dos[key]["nombre"] > 0 :
            Variable.compteurS += Variable.sac_a_dos[key]["nombre"]

# Positionner les Objets

def NourritureObjet():

        for loop in range(10) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != " " :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.positionObjet.append(emplacementY)
            Variable.positionObjet.append(emplacementX)
        # Variable.liste_Map = "".join(Variable.liste_Map)