import Variable
import os
import Display
import random
import time
import enigme
import message
import sys




def clear():
    os.system('cls') #pour Windows
#__________________________________________________________________________________________________________________________
def afterClear():
    clear()
    Display.map1()
#__________________________________________________________________________________________________________________________
def YesOrNo(variable):   
        while variable != "non" and variable != "oui" :
            variable = input("Oui ou non ? ").lower()
        return variable
#__________________________________________________________________________________________________________________________ 

def finish():
    if Variable.ancienCaractere == "♫" :
        print("Vous devez faire les trois enigme avant d'acceder à cette porte")
    elif Variable.ancienCaractere == "\u001b[38;5;226m♫\033[0m" :
        if Variable.sac_a_dos['Bouteille']['nombre'] == 0 or Variable.sac_a_dos['Couteau']['nombre'] == 0 :
            print("Vous devez avoir votre bouteille et votre couteau pour prendre cette porte")
        else :
            clear()
            message.victory()
            time.sleep(3.0)
            sys.exit (0)

#__________________________________________________________________________________________________________________________



#__________________________________________________________________________________________________________________________

def enigmeMystereCesarSinge ():
    if Variable.ancienCaractere == "\u001b[38;5;226m♪\033[0m" or Variable.ancienCaractere == "\u001b[38;5;240m♪\033[0m":
        if Variable.positionJoueur[0] in Variable.positionEnigme and Variable.positionJoueur[1] in Variable.positionEnigme :
            print("Vous avez déjà fait cette enigme")
        else  :
            reponse = input("Tu es pret à faire l'enigme ? ")
            reponse = YesOrNo(reponse)
            if reponse == "oui" :
                if Variable.verificationMystere == False :
                    clear()
                    enigme.mainMystereGame()

                elif Variable.verificationCesar == False :
                    clear()
                    enigme.mainCesar()

                else:
                    clear()
                    enigme.mainFizzBuzz()
                Variable.positionJoueur[0] += 1
                afterClear()
                print(Variable.nbKey)
            else : 
                Variable.positionJoueur[0] += 1
                afterClear()

#__________________________________________________________________________________________________________________________   
# Capacité du Sac à dos 
def nombreObjet():
    Variable.compteurStock = 0
    for key in Variable.sac_a_dos:
        if Variable.sac_a_dos[key]["nombre"] > 0 :
            Variable.compteurStock += Variable.sac_a_dos[key]["nombre"]

#__________________________________________________________________________________________________________________________

def checkAction(action, listeAction):
    if len(action) > 1 and action[0] == "d" or action[0] == "u":
            action = list(action)
            Variable.lettre = action[0]
            Variable.fruit = "".join(action[2:]).capitalize()
    else :
            Variable.lettre = action

    Variable.checkActionSac = False
    if len(action) == 1 and Variable.lettre == "l" :
        Variable.checkActionSac = True
    elif (Variable.lettre == "u" and Variable.fruit in Variable.contenuInventaire) or (Variable.lettre == "d" and Variable.fruit in Variable.contenuInventaire) :
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

def VitaliteJoeur() :
    Variable.Vitalite["Energie"]["Stock"] -= Variable.Vitalite["Energie"]["-"]
    Variable.Vitalite["Hydratation"]["Stock"] -= Variable.Vitalite["Hydratation"]["-"]
    Variable.Vitalite["Satiete"]["Stock"] -= Variable.Vitalite["Satiete"]["-"]
    
#__________________________________________________________________________________________________________________________

def caracterePosition(axeY, axeX, caractere):
    if len(Variable.positionAbreAnanas) > 1 :
        compteur = 0
        for loop in range(len(Variable.positionSolAnanas)//2):
            if axeY == Variable.positionSolAnanas[compteur] and axeX == Variable.positionSolAnanas[compteur+1]:
                caractere = "×"
            compteur +=2

    if len(Variable.positionAbreBanane) > 1 :
        compteur = 0
        for loop in range(len(Variable.positionSolBanane)//2):
            if axeY == Variable.positionSolBanane[compteur] and axeX == Variable.positionSolBanane[compteur+1] :
                caractere = "×"
            compteur +=2

    if len(Variable.positionAbreMangue) > 1 :
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

#______________________________________________________________________________________________________________

def remplirBouteille() :
    if Variable.sac_a_dos["Bouteille"]["nombre"] == 0 :
        print("Vous n'avez pas votre bouteille dans votre sac")
    elif Variable.liste_Map[Variable.positionJoueur[0]-1][Variable.positionJoueur[1]] == "≈" or Variable.liste_Map[Variable.positionJoueur[0]+1][Variable.positionJoueur[1]] == "≈" :
        Variable.sac_a_dos["Bouteille"]["Stockage"] = 100
        print("Votre bouteille est completement rempli")
    elif Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]-1] == "≈" or Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]+1] == "≈" :
        Variable.sac_a_dos["Bouteille"]["Stockage"] = 100
        print("Votre bouteille est completement rempli")
    else:
        print("Vous devez être près de la rivière pour remplir votre bouteille")
    time.sleep(2.5)

#______________________________________________________________________________________________________________

def utiliserObjet():
    Satiete = Variable.Vitalite["Satiete"]["Stock"]
    hydratation = Variable.Vitalite["Hydratation"]["Stock"]
    bouteille = Variable.sac_a_dos["Bouteille"]["Stockage"]

    if Variable.fruit in Variable.listeFruit :
        fruit = Variable.sac_a_dos[Variable.fruit]["+"]
        addition = (Satiete + fruit)
        if addition < 100 :
            Variable.Vitalite["Satiete"]["Stock"] = addition
            Variable.sac_a_dos[Variable.fruit]["nombre"] -= 1
            print(f'Vous avez récupéré {fruit} de Satiete')

        elif Satiete == 100 :
            print("Vous avez le ventre plein !")
        elif addition > 100 :

            print(f'Vous avez récupéré {Satiete - 100} de Satiete')
            print(f'Vous avez récupéré {fruit} de Satiete')
            Variable.Vitalite["Satiete"]["Stock"] = 100
            Variable.sac_a_dos[Variable.fruit]["nombre"] -= 1
            
    elif Variable.fruit == "Bouteille" :
        if bouteille == 0 :
            print("Votre bouteille est vide !")
        elif hydratation == 100 :
            print("Vous n'avez pas soif !")
        else :
            Variable.Vitalite["Hydratation"]["Stock"] += bouteille 
            if Variable.Vitalite["Hydratation"]["Stock"] > 100 :
                Variable.Vitalite["Hydratation"]["Stock"] = 100
            if bouteille < hydratation :
                Variable.sac_a_dos["Bouteille"]["Stockage"] = 0
            else :
                Variable.sac_a_dos["Bouteille"]["Stockage"] = bouteille - (bouteille - hydratation)
            print(f'Votre bouteille est rempli a {Variable.sac_a_dos["Bouteille"]["Stockage"]}%')
            
    else :
        print("Votre couteau n'a pas d'utilité pour le moment")
    time.sleep(2.5)

def displayVitalite():
    graduation("Energie","\u001b[31m•\u001b[0m", ":    ")
    graduation("Hydratation","\u001b[34m•\u001b[0m", ":")
    graduation("Satiete","\u001b[32m•\u001b[0m", ":    ")

def graduation(string, couleur, espace):
    ligne = ""
    compteur = 0
    for loop in range(Variable.Vitalite[string]["Stock"]):
        if compteur % 2 == 0 :
            ligne += "•"
        else : 
            ligne += couleur
        compteur += 1
    print(f'{string} {espace} {ligne}')

def sleep():
    try :
        heure = int(input("Combien d'heure veux tu dormir ? : "))
        for loop in range (heure) :
            afterClear()
            print("zzzZZZ")
            time.sleep(1.0)
            Variable.Vitalite["Energie"]["Stock"] += 10

            if Variable.Vitalite["Energie"]["Stock"] > 100 :
                Variable.Vitalite["Energie"]["Stock"] = 100
                print("Vous avez assez dormis")
                time.sleep(1.5)
                break
    except :
        print("Vous dormirez plus tard ")
        time.sleep(1.5)


#def victoire ():

