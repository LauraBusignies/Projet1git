import Variable
import os
import Display
import random
import time
import enigme
import FonctionPrint
import sys
import json




def clear():
    os.system('cls') #pour Windows
#__________________________________________________________________________________________________________________________

# Clear la console puis affiche la map
def afterClear():
    clear()
    Display.map1()
#__________________________________________________________________________________________________________________________

# Vérification oui ou non pour les input
def YesOrNo(variable):   
        while variable != "non" and variable != "oui" :
            variable = input("Oui ou non ? ").lower()
        return variable

#__________________________________________________________________________________________________________________________

# A chaque déplacement j'actualise les signes vitaux
def vitaliteJoueur() :
    Variable.var_enregistrer["vitalite"]["Energie"]["Stock"] -= Variable.var_enregistrer["vitalite"]["Energie"]["-"]
    Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"] -= Variable.var_enregistrer["vitalite"]["Hydratation"]["-"]
    Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"] -= Variable.var_enregistrer["vitalite"]["Satiete"]["-"]

#________________________________________________________________________________________________________________________________________

# Définir une couleur pour chaque signes vitaux
def displayvitalite():
    graduation("Energie","\u001b[31m•\u001b[0m", ":    ")
    graduation("Hydratation","\u001b[34m•\u001b[0m", ":")
    graduation("Satiete","\u001b[32m•\u001b[0m", ":    ")

#________________________________________________________________________________________________________________________________________

# print les lignes des signes vitaux 
def graduation(string, couleur, espace):
    ligne = ""
    compteur = 0
    for loop in range(Variable.var_enregistrer['vitalite'][string]["Stock"]):
        if compteur % 2 == 0 :
            ligne += "•"
        else : 
            ligne += couleur
        compteur += 1
    print(f'{string} {espace} {ligne}')
    
#__________________________________________________________________________________________________________________________

# Vérification si le joueur 
def objetFruit(axeY, axeX, caractere):
    
    if len(Variable.var_enregistrer['positionSolAnanas']) > 1 :
        compteur = 0
        for loop in range(len(Variable.var_enregistrer['positionSolAnanas'])//2):
            if axeY == Variable.var_enregistrer['positionSolAnanas'][compteur] and axeX == Variable.var_enregistrer['positionSolAnanas'][compteur+1]:
                caractere = "×"
            compteur +=2

    if len(Variable.var_enregistrer['positionSolBanane']) > 1 :
        compteur = 0
        for loop in range(len(Variable.var_enregistrer['positionSolBanane'])//2):
            if axeY == Variable.var_enregistrer['positionSolBanane'][compteur] and axeX == Variable.var_enregistrer['positionSolBanane'][compteur+1] :
                caractere = "×"
            compteur +=2

    if len(Variable.var_enregistrer['positionSolMangue']) > 1 :
        compteur = 0
        for loop in range(len(Variable.var_enregistrer['positionSolMangue'])//2):
            if axeY == Variable.var_enregistrer['positionSolMangue'][compteur] and axeX == Variable.var_enregistrer['positionSolMangue'][compteur+1] :
                caractere = "×"
            compteur +=2
    return caractere

#__________________________________________________________________________________________________________________________

# Vérification un objet au sol peut être ramassé et si c'est la bouteille ou le couteau
def verificationObjetSol() :
    for k in Variable.var_enregistrer['sac_a_dos']:
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['sac_a_dos'][k]["positionY"] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['sac_a_dos'][k]["positionX"] :
            Variable.validationPositionSol = True
            Variable.var_enregistrer['objetRamasser'] = k
#__________________________________________________________________________________________________________________________   

# Capacité du Sac à dos 
def nombreObjet():
    Variable.compteurStock = 0
    for key in Variable.var_enregistrer['sac_a_dos']:
        Variable.compteurStock += Variable.var_enregistrer['sac_a_dos'][key]['nombre']

#__________________________________________________________________________________________________________________________

# Vérification des entrées pour le sac à dos
def checkAction(action, listeAction):
    if action != "":
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

# Supprimer un objet du sac a dos
def deleteObjet ():
    # Retirer l'objet du sac a dos 
    Variable.var_enregistrer['sac_a_dos'][Variable.fruit]['nombre'] += -1
    print(Variable.var_enregistrer['sac_a_dos'][Variable.fruit]['message'])
    time.sleep (1.5)
    listeFruit = ["Mangue", "Banane", "Ananas"]
    # Si l'objet n'est pas dans la liste des fruit, j'ajoute la position dans le dictionnaire pour le couteau ou la bouteille
    if Variable.fruit not in listeFruit :
        Variable.var_enregistrer['sac_a_dos'][Variable.fruit]["positionY"] = Variable.var_enregistrer['positionJoueur'][0]
        Variable.var_enregistrer['sac_a_dos'][Variable.fruit]["positionX"] = Variable.var_enregistrer['positionJoueur'][1]

    # Si l'objet est dans la liste des fruits, j'ajoute sa position a la liste des position de fruit
    elif Variable.fruit == "Ananas" :
        Variable.var_enregistrer['positionSolAnanas'].append(Variable.var_enregistrer['positionJoueur'][0])
        Variable.var_enregistrer['positionSolAnanas'].append(Variable.var_enregistrer['positionJoueur'][1])
    elif Variable.fruit == "Banane" :
        Variable.var_enregistrer['positionSolBanane'].append(Variable.var_enregistrer['positionJoueur'][0])
        Variable.var_enregistrer['positionSolBanane'].append(Variable.var_enregistrer['positionJoueur'][1])
    else : 
        Variable.var_enregistrer['positionSolMangue'].append(Variable.var_enregistrer['positionJoueur'][0])
        Variable.var_enregistrer['positionSolMangue'].append(Variable.var_enregistrer['positionJoueur'][1])

#______________________________________________________________________________________________________________

# Utiliser un objet du sac a dos
def utiliserObjet():
    Satiete = Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"]
    hydratation = Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"]
    bouteille = Variable.var_enregistrer['sac_a_dos']["Bouteille"]["Stockage"]

    # Si l'objet est un fruit, j'agrémente la satieté sauf si la satiété est au max
    if Variable.fruit in Variable.listeFruit :
        fruit = Variable.var_enregistrer['sac_a_dos'][Variable.fruit]["+"]
        addition = (Satiete + fruit)
        if addition < 100 :
            Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"] = addition
            Variable.var_enregistrer['sac_a_dos'][Variable.fruit]["nombre"] -= 1
            print(f'Vous avez récupéré {fruit} de Satiete')

        elif Satiete == 100 :
            print("Vous avez le ventre plein !")
        elif addition > 100 :

            print(f'Vous avez récupéré {Satiete - 100} de Satiete')
            print(f'Vous avez récupéré {fruit} de Satiete')
            Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"] = 100
            Variable.var_enregistrer['sac_a_dos'][Variable.fruit]["nombre"] -= 1
            
    # J'agremente l'hydratation jusqu'au max ou jusqu'a ce que la bouteille soit vide
    elif Variable.fruit == "Bouteille" :
        if bouteille == 0 :
            print("Votre bouteille est vide !")
        elif hydratation == 100 :
            print("Vous n'avez pas soif !")
        else :
            Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"] += bouteille 
            if Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"] > 100 :
                Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"] = 100
            if bouteille < hydratation :
                Variable.var_enregistrer['sac_a_dos']["Bouteille"]["Stockage"] = 0
            else :
                Variable.var_enregistrer['sac_a_dos']["Bouteille"]["Stockage"] = bouteille - (bouteille - hydratation)
            print("Votre bouteille est rempli a", Variable.var_enregistrer['sac_a_dos']["Bouteille"]["Stockage"])
            
    else :
        print("Votre couteau n'a pas d'utilité pour le moment")
    time.sleep(2.5) 




#______________________________________________________________________________________________________________

# Remplir la bouteille d'eau si le signe de la rivière est a proximité
def remplirBouteille() :
    if Variable.var_enregistrer['sac_a_dos']["Bouteille"]["nombre"] == 0 :
        print("Vous n'avez pas votre bouteille dans votre sac")
    elif Variable.liste_Map[Variable.var_enregistrer['positionJoueur'][0]-1][Variable.var_enregistrer['positionJoueur'][1]] == "≈" or Variable.liste_Map[Variable.var_enregistrer['positionJoueur'][0]+1][Variable.var_enregistrer['positionJoueur'][1]] == "≈" :
        Variable.var_enregistrer['sac_a_dos']["Bouteille"]["Stockage"] = 100
        print("Votre bouteille est completement rempli")
    elif Variable.liste_Map[Variable.var_enregistrer['positionJoueur'][0]][Variable.var_enregistrer['positionJoueur'][1]-1] == "≈" or Variable.liste_Map[Variable.var_enregistrer['positionJoueur'][0]][Variable.var_enregistrer['positionJoueur'][1]+1] == "≈" :
        Variable.var_enregistrer['sac_a_dos']["Bouteille"]["Stockage"] = 100
        print("Votre bouteille est completement rempli")
    else:
        print("Vous devez être près de la rivière pour remplir votre bouteille")
    time.sleep(2.5)


#________________________________________________________________________________________________________________________________________

# Faire dormir le joueur pour remonter son energie et faire descendre la satiété et l'hydratation
def sleep():
    try :
        heure = int(input("Combien d'heure veux tu dormir ? : "))
        for loop in range (heure) :
            afterClear()
            print("zzzZZZ")
            time.sleep(1.0)
            Variable.var_enregistrer["vitalite"]["Energie"]["Stock"] += 6
            Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"] -= 2
            Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"] -= 1
            if Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"] <= 0 or Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"] <= 0 :
                FonctionPrint.die() # ligne 170
                break

            if Variable.var_enregistrer["vitalite"]["Energie"]["Stock"] > 100 :
                Variable.var_enregistrer["vitalite"]["Energie"]["Stock"] = 100
                print("Vous avez assez dormis")
                time.sleep(1.5)
                break
    except :
        print("Vous dormirez plus tard ")
        time.sleep(1.5)
#__________________________________________________________________________________________________________________________

# lancer les enigmes dans l'ordre, une fois que l'enigme est faite, la position est prise et ne peut pas etre refaite
def enigmeMystereCesarSinge ():
    if Variable.var_enregistrer['ancienCaractere'] == "\u001b[38;5;226m♪\033[0m" or Variable.var_enregistrer['ancienCaractere'] == "\u001b[38;5;240m♪\033[0m":
        if Variable.var_enregistrer['positionJoueur'][0] in Variable.var_enregistrer['positionEnigme'] and Variable.var_enregistrer['positionJoueur'][1] in Variable.var_enregistrer['positionEnigme'] :
            Variable.var_enregistrer['positionJoueur'][0] += 1
            afterClear()
            print("Vous avez déjà fait cette enigme")
        else  :
            reponse = input("Tu es pret à faire l'enigme ? ")
            reponse = YesOrNo(reponse)
            if reponse == "oui" :
                if Variable.var_enregistrer['verificationMystere'] == False :
                    clear()
                    enigme.mainMystereGame()

                elif Variable.var_enregistrer['verificationCesar'] == False :
                    clear()
                    enigme.mainCesar()
        
                else:
                    clear()
                    enigme.mainFizzBuzz()
                Variable.var_enregistrer['positionJoueur'][0] += 1
                afterClear()
            else : 
                Variable.var_enregistrer['positionJoueur'][0] += 1
                afterClear()
#________________________________________________________________________________________________________________________________________

# Print l'historique des parties
def historique():
    
    clear()
    with open("Historique.json", "r", encoding="utf-8") as MyFile:
        Variable.dicHistorique = json.load(MyFile)

    print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    print("| Nom du Joueur |   Resultat    |   nbAction    | nbDeplacement |    Energie    |    Satiété    |  Hydratation  |          Date          |")
    print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    espace = " "

    for k in Variable.dicHistorique :
        ligne = "|"
        compteur = 0

        try :
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
            
            
    suite = input("Veux tu commencer le jeu ? ").lower()
    if suite == "oui" :
        pass
    else : 
        sys.exit(0)
#________________________________________________________________________________________________________________________________________

# Condition pour finir le jeu
def finish():
    if Variable.var_enregistrer['ancienCaractere'] == "♫" :
        print("Vous devez faire les trois enigme avant d'acceder à cette porte")
    elif Variable.var_enregistrer['ancienCaractere'] == "\u001b[38;5;226m♫\033[0m" :
        if Variable.var_enregistrer['sac_a_dos']['Bouteille']['nombre'] == 0 or Variable.var_enregistrer['sac_a_dos']['Couteau']['nombre'] == 0 :
            print("Vous devez avoir votre bouteille et votre couteau pour prendre cette porte")
        else :
            clear()
            FonctionPrint.victory() # ligne 264
            Variable.var_enregistrer['resultatJeu'] = 'Victoire'
            Variable.var_enregistrer['date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            try :
                with open("Historique.json", "r", encoding="utf-8") as MyFile:
                    Variable.dicHistorique = json.load(MyFile)
            except : 
                pass
            # Sauvegarde des scores du jeu
            Variable.dicHistorique['compteurHistorique'] += 1
            Variable.dicHistorique[f'joueur{Variable.dicHistorique["compteurHistorique"]}'] = [Variable.var_enregistrer['nomAventurier'],
                                Variable.var_enregistrer['resultatJeu'],
                                Variable.var_enregistrer['nombreAction'],
                                Variable.var_enregistrer['nombreDeplacement'],
                                Variable.var_enregistrer['vitalite']['Energie']['Stock'],
                                Variable.var_enregistrer['vitalite']['Satiete']['Stock'],
                                Variable.var_enregistrer['vitalite']['Hydratation']['Stock'],
                                Variable.var_enregistrer['date']]

            # Vérification de la capacité de l'historique                 
            compteur = -1
            for k in Variable.dicHistorique :
                compteur += 1
            if compteur == 11 :
                for k in Variable.dicHistorique :
                    del Variable.dicHistorique[k]
                    break
            with open("Historique.json", "w", encoding="utf-8") as MyFile:
                json.dump(Variable.dicHistorique, MyFile, sort_keys = True, indent = 4, ensure_ascii = False)
            time.sleep(3.0)
            sys.exit (0)


