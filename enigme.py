import random
import time 
import os
from Nombre_mystere import gardian
import Variable

def key():
    clear()
    print(" ____   ____._______  .____                   ___ .___ .______  ")
    print(" \   \_/   /: .___  \ |    |___      .___    |   |: __|:      \ ")
    print("  \___ ___/ | :   |  ||    |   |     :   | /\|   || : ||       |")
    print("    |   |   |     :  ||    :   |     |   |/  :   ||   ||   |   |")
    print("    |___|    \_. ___/ |        |     |   /       ||   ||___|   |")
    print("               :/     |. _____/      |______/|___||___|    |___|")
    print("               :       :/                    :                  ")
    print("                       :                     :                  ")
    print("                 ______")
    print("                 /      \____________________")
    print("                (   ()   ______________█     | ")
    print("                \______/               |_||_|")
    time.sleep(2.5)
#règles du jeu
def rules_mystery_number():
    print("_____________________________________________________________________________________________________________________\n")
    print("Te voici arrivé à la première enigme, LE NOMBRE MYSTERIEUX.\n")
    print("Tu vas devoir réussir cette enigme 3 fois pour gagner une des clés necessaires pour ouvrir la porte")
    print("Mais un sphinx est confortablement assis sur votre clé !\n")
    print("Pour gagner tu devras trouver le chiffre exact entre 0 et 100, et cela trois fois de suite !\n")
    print("Si tu perds un des trois test, tu devras recommener au début")
    print("Ha oui ! Petite règle suplémentaire tu auras un nombre aléatoire d'essaie par test.\n\n")


#Définir la validation de l'enté
def inpunt_validation():

    #time.sleep(0.5)
    adventurer_number = input("Choisis ton chiffre : ").strip().lower()
    validation = False 
    while not validation:
        if not adventurer_number.isdigit() or int(adventurer_number) >= 100 or int(adventurer_number) <= 0 :
            adventurer_number = input("Choisissez un chiffre entre 0 et 100 : ")
        if adventurer_number.isdigit() and int(adventurer_number) < 100 and int(adventurer_number) > 0 :
            validation = True
            return adventurer_number

# Définir si c'est moins ou plus 
def game(adventurer_number, counter, mystery_number, total_counter, try_number):

    while adventurer_number != mystery_number and counter != try_number :
        adventurer_number = inpunt_validation()
        counter += 1  
        if int(adventurer_number) > mystery_number : 
            print("C'est moins !")
        elif int(adventurer_number) == mystery_number :
            total_counter += counter
            counter = 0
            break
        else :
            print("C'est plus")
    return adventurer_number, counter, total_counter

#Définir la victoire 
def victory_or_defeat(victory, adventurer_number, mystery_number, counter_game, try_number):

    if  int(adventurer_number) == mystery_number :
        print()
        print(f"Bravo tu as gagné le niveau {counter_game} ")
        #time.sleep(2.0)
    else : 
        print()
        print(f"Perdu ! Tu as utilisé tes {try_number} essaies. Tu dois recommencer ! 凸(^_^)凸")
        victory = False
        #time.sleep(1.5)
    return victory

# Clear la console
def clear():
    os.system('cls') #pour Windows

# Assemblement des fonction

# Variables global


def mainMystereGame():
    
    adventurer_number = 0
    counter = 0
    total_counter = 0
    victory = True 
    counter_game = 0
    yes_or_no = 'non'
    rules_mystery_number()
    gardian.sphinx()
    yes_or_no = input("Et tu prêt à commencer ? Oui ou Non : ").lower()    
    while yes_or_no != "oui" :
        yes_or_no=input("Tant que tu ne diras pas oui, on sera coincé ici !").lower()
    while counter_game != 3 :
        for loop in range (3) :
            mystery_number = random.randint(0, 100)
            try_number = random.randint(5,10)
            counter_game += 1

            clear()
            if counter_game == 1 :
                print("Tu vas commencer le 1er NOMBRE MYSTERIEUX ")
                time.sleep(1.0)
                print("Le sphinx choisis combien tu auras d'essai pour ce test")
                time.sleep(1.0)
                gardian.sphinx()
                print("Suspense ...")
                time.sleep(1.0)
                print(f"Tu auras {try_number} essaies !\n")
            else :
                print(f"Tu vas commencer le {counter_game}ème NOMBRE MYSTERIEUX ")
                #time.sleep(1.5)
                print("Le sphinx choisis combien tu auras d'essai pour ce test")
                #time.sleep(1.5)
                gardian.sphinx()
                print("Suspense ...")
                #time.sleep(1.5)
                print(f"Tu auras {try_number} essaies !\n")
            
            adventurer_number, counter, total_counter = game(adventurer_number, counter, mystery_number, total_counter, try_number)
            victory = victory_or_defeat(victory, adventurer_number, mystery_number, counter_game, try_number)
            if victory == False :
                counter_game = 0
                counter = 0
                break 

    Variable.var_enregistrer['verificationMystere'] = True 
    Variable.var_enregistrer['nbKey'] += 1
    Variable.var_enregistrer['positionEnigme'].append(Variable.var_enregistrer['positionJoueur'][0])
    Variable.var_enregistrer['positionEnigme'].append(Variable.var_enregistrer['positionJoueur'][1])

    key()
 

#__________________________________________________________________________________________________________________________________



def verificationAction(action, verification, listeCode):
    if len(action) == 1 and action in listeCode[0] :
        verification = True 
    elif action == "":
        verification = True 
    elif action == action :
        verification = True
    return verification

#__________________________________________________________________________________
 
def entré(action, verification, listeCode, chance):
    print(f'Tu as {5 - chance} essai !')
    action = input("Quelle est votre proposition ? ").upper()
    verification = verificationAction(action, verification, listeCode)
    while verification == False :
        verification = verificationAction(action, verification, listeCode)
        action = input("Votre entré n'est pas valide : ")
    return action 
#__________________________________________________________________________________

def decryptageCredo(nom, chance, credoOfficiel, action , listeCode, nomPrincipal):
    nom = nomPrincipal
    if len(action) == 1 and action in listeCode[0] :
        nom = list(nom)
        credo = list(credoOfficiel.upper())
        compteur = 0
        for loop in range (len(credo)):
            lettre = credo[compteur]
            if lettre not in listeCode[0]:
                compteur += 1
            else :
                indexCode = int(listeCode[1][listeCode[0].index(action)-1])
                indexLettre = int(listeCode[1][listeCode[0].index(lettre)])
                addition = indexCode + indexLettre
                try :
                    credo[compteur] = listeCode[0][addition]

                except IndexError :
                    addition = (indexCode + indexLettre) - 26
                    credo[compteur] = listeCode[0][addition]
                compteur += 1
        print ("".join(credo).capitalize())
    # cryptage du nom pour la solution 
        compteur = 0
        for loop in range (len(nom)):
            lettre = nom[compteur]
            indexCode = int(listeCode[1][listeCode[0].index(action)-1])
            indexLettre = int(listeCode[1][listeCode[0].index(lettre)])
            addition = indexCode + indexLettre
            try :
                nom[compteur] = listeCode[0][addition]

            except IndexError :
                addition = (indexCode + indexLettre) - 26
                nom[compteur] = listeCode[0][addition]
            compteur += 1
        nom = "".join(nom)

    elif action == "" :
        print (credoOfficiel)

    else :
        chance += 1
    return nom, chance
        
def reglement() :
    print ("Règles :\n")
    print("Appuyer sur entré pour avoir le texte sans clé ")
    print("    Appuyer sur une lettre pour modifier le texte avec une clé")
    print("        Entrez un mot pour proposer une proposition de réponse")
    print("            Pour gagner tu devras entrer ton nom crypté avec la clé choisis")
    print("                Tu as seulement 5 chances, réfléchis bien\n")
    print("Voici le crédo sans cryptage ""Tu as peu de chance de reussir, mais bon courage !\n")

def mainCesar():        
    listeCode= [["A","B","C","D","E","F","G","H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
                ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]]

    credoOfficiel = "Tu as peu de chance de reussir, mais bon courage !"
    nomPrincipal = ""
    nom = nomPrincipal
    action =""
    ancienAction = ""
    verification = False
    chance = 0
    réponse = "oui"

    while réponse == "oui" :
        print()
        reglement ()
        nomPrincipal = input("Quel est ton nom ? ").upper()
        clear()
        reglement()
        action = listeCode[0][random.randint(1,25)]
        nom, chance = decryptageCredo(nom, chance, credoOfficiel, action , listeCode,nomPrincipal)
        while action != nom and chance < 5 :
            action = entré(action, verification, listeCode, chance)
            clear()
            reglement()
            if action != nom :
                nom, chance = decryptageCredo(nom, chance, credoOfficiel, action , listeCode, nomPrincipal)

        if chance > 5 :
            réponse = input("Tu as perdu, veux tu recommencer ? ")
        else : 
            print("Tu as décodé le credo !")
            time.sleep(1.0)
            key()
            réponse = "non"
            Variable.var_enregistrer['verificationCesar'] = True
            Variable.var_enregistrer['nbKey'] += 1
            Variable.var_enregistrer['positionEnigme'].append(Variable.var_enregistrer['positionJoueur'][0])
            Variable.var_enregistrer['positionEnigme'].append(Variable.var_enregistrer['positionJoueur'][1])



#_________________________________________________________________________________________________________________________________


def rules ():
    print("\nTe revoilà aventurier ! Pour gagner cette enigme tu devras gagner le jeu du FizzBuzz contre des singes !\n")
    #time.sleep(1.5)
    print("Les règles du jeu sont :")
    #time.sleep(1.5)
    print("On compte à tour de rôle en commençant à 1")
    #time.sleep(1.0)
    print(" Si le nombre à annoncer est un multiple de 3, il faut dire Fizz au lieu du nombre.")
    #time.sleep(1.0)
    print("     Si c’est un multiple de 5, il faut dire Buzz.")
    #time.sleep(1.0)
    print("         Si c’est à la fois un multiple de 3 et 5 il faut dire FizzBuzz.")
    #time.sleep(1.0)
    print("             Si on se trompe, on est éliminé de la partie et les joueurs restants recommencent jusqu’à ce qu’il n’en reste qu’un.")
    


def monkey(listeJoueur):
    l1 = ["   .-'-.      ",
    " _/.-.-.\_    ",
    "( ( o o ) )   ",
    " |/  '  \|    ",
    "  \ .-. /     ",
    "  /`'''`\     ",
    " /       \    "]

    compteur = 0
    for loop in range (7):
        ligne = ""
        for loop in range(len(listeJoueur) -1):
            ligne = (f'{ligne}{l1[compteur]}')
        compteur += 1
        print (ligne)
    



def gameFizzBuzz ():
    rules()
    nbJoueur = { "singe1" : 0, "singe2" : 0, "singe3" : 0, "singe4" : 0, "singe5" : 0, "singe6" : 0, "singe7" : 0, "singe8" : 0, "singe9" : 0, }
    listeJoueur = []
    for k in nbJoueur :
        nbJoueur[k] = random.randint(1, 7)
        listeJoueur.append(k)
    listeJoueur.append("chef")
    listeJoueur.append("aventurier")
    nbJoueur["chef"] = random.randint (5,8)
    nbJoueur["aventurier"] = random.randint(8,9)
    random.shuffle(listeJoueur)
    espace = ", "

    while len(listeJoueur) != 1 and "aventurier" in listeJoueur :
        ancienlen = len(listeJoueur)
        nombre = 1
        compteur = 0
        ligne = ""
        print()
        clear()
        monkey(listeJoueur)
        print()
        while len(listeJoueur) == ancienlen :

            chiffre = random.randint(1, 10 - nbJoueur[listeJoueur[compteur]])
            if nombre % 3 == 0 or nombre % 5 == 0 :
                if chiffre == 1 and (nombre % 5 == 0 and nombre % 3 == 0) :
                    print("FizzBuzz", end="")
                elif chiffre == 1 and nombre % 3 == 0:
                    print("Fizz, ", end = "")
                    
                elif chiffre == 1 and nombre % 5 == 0:
                    print('Buzz, ', end = "")

                else :
                    print(nombre)
                    print(f'{listeJoueur[compteur]} est éliminé'.capitalize())
                    time.sleep(1.5)
                    del listeJoueur[compteur]    
                    
            else :
                print (nombre,espace, end="")
                
            if compteur + 1 == len(listeJoueur) :
                compteur = 0
            else : 
                compteur += 1
            nombre += 1 
    return listeJoueur


def mainFizzBuzz():

    listeJoueur = []       
    listeJoueur = gameFizzBuzz ()        
    reponse = ""

    while "aventurier" not in listeJoueur and reponse != "non" :
        reponse = input("Tu as perdu, le chef ne veut pas te donner la clé, veux tu rejouer ? ").lower()
        while reponse == "non" and reponse == "oui" :
            reponse = input("Oui ou non ? ").lower()
        if reponse == "oui" :
            clear() 
            listeJoueur = gameFizzBuzz ()

    if "aventurier" in listeJoueur :
        clear()
        print("Bravo tout les singes ont perdu !")
        key()
        Variable.var_enregistrer['verificationMonkey'] = True
        Variable.var_enregistrer['nbKey'] += 1
        Variable.var_enregistrer['positionEnigme'].append(Variable.var_enregistrer['positionJoueur'][0])
        Variable.var_enregistrer['positionEnigme'].append(Variable.var_enregistrer['positionJoueur'][1])

