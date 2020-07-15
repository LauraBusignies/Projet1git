import Variable
import os
import Display
import random
import time

def clear():
    os.system('cls') #pour Windows

def afterClear():
    clear()
    Display.map1()

# Definir l

    
# Capacité du Sac à dos 
def nombreObjet():
    Variable.compteurStock = 0
    for key in Variable.sac_a_dos:
        if Variable.sac_a_dos[key]["nombre"] > 0 :
            Variable.compteurStock += Variable.sac_a_dos[key]["nombre"]

#__________________________________________________________________________________________________________________________

def checkAction(action, listeAction):
    if len(action) > 1 and action[0] == "d" :
            action = list(action)
            Variable.lettre = action[0]
            Variable.fruit = "".join(action[2:]).capitalize()
    else :
            Variable.lettre = action

    Variable.checkActionSac = False
    if len(action) == 1 and Variable.lettre == "l" :
        Variable.checkActionSac = True
    elif Variable.lettre == "u" or Variable.lettre == "d" and Variable.fruit in Variable.contenuInventaire :
        Variable.checkActionSac = True
#__________________________________________________________________________________________________________________________

def deleteObjet ():
    Variable.sac_a_dos[Variable.fruit]['nombre'] += -1
    print(Variable.sac_a_dos[Variable.fruit]['message'])
    time.sleep (1.5)
    listeFruit = ["Mangue", "Banane", "Ananas"]
    if Variable.fruit not in listeFruit :
        Variable.sac_a_dos[Variable.fruit]["positionY"] = Variable.positionJoueur[0]
        Variable.sac_a_dos[Variable.fruit]["positionX"] = Variable.positionJoueur[1]
    elif Variable.fruit == "Ananas" :
        Variable.positionSolAnanas.append(Variable.positionJoueur[0])
        Variable.positionSolAnanas.append(Variable.positionJoueur[1])
    elif Variable.fruit == "Banane" :
        Variable.positionSolBanane.append(Variable.positionJoueur[0])
        Variable.positionSolBanane.append(Variable.positionJoueur[1])
    else : 
        Variable.positionSolMangue.append(Variable.positionJoueur[0])
        Variable.positionSolMangue.append(Variable.positionJoueur[1]) 

#__________________________________________________________________________________________________________________________

def vitalitéJoeur() :
    Variable.vitalité["Fatigue"]["stock"] -= Variable.vitalité["Fatigue"]["-"]
    Variable.vitalité["Hydratation"]["stock"] -= Variable.vitalité["Hydratation"]["-"]
    Variable.vitalité["Satiété"]["stock"] -= Variable.vitalité["Satiété"]["-"]
    
#__________________________________________________________________________________________________________________________

def caracterePosition(axeY, axeX, caractere):
    if len(Variable.positionAnanas) > 1 :
        compteur = 0
        for loop in range(len(Variable.positionSolAnanas)//2):
            if axeY == Variable.positionSolAnanas[compteur] and axeX == Variable.positionSolAnanas[compteur+1] :
                caractere = "×"
            compteur +=2

    if len(Variable.positionBanane) > 1 :
        compteur = 0
        for loop in range(len(Variable.positionSolBanane)//2):
            if axeY == Variable.positionSolBanane[compteur] and axeX == Variable.positionSolBanane[compteur+1] :
                caractere = "×"
            compteur +=2

    if len(Variable.positionMangue) > 1 :
        compteur = 0
        for loop in range(len(Variable.positionSolMangue)//2):
            if axeY == Variable.positionSolMangue[compteur] and axeX == Variable.positionSolMangue[compteur+1] :
                caractere = "×"
            compteur +=2
    return caractere

#__________________________________________________________________________________________________________________________

def verificationObjetSol() :
    for k in Variable.sac_a_dos:
        if Variable.positionJoueur[0] == Variable.sac_a_dos[k]["positionY"] and Variable.positionJoueur[1] == Variable.sac_a_dos[k]["positionX"] :
            Variable.validationPositionSol = True
            Variable.objetRamasser = k