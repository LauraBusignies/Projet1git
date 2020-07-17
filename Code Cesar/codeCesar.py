import random
import os 


def clear():
    os.system('cls') #pour Windows
#_________________________________________________________________________________________________________

def verificationAction(action, verification):
    if len(action) == 1 and action in listeCode[0] :
        verification = True 
    elif action == "":
        verification = True 
    elif action == action :
        verification = True
    return verification

#_________________________________________________________________________________________________________
 
def entré(action, verification):
    action = input("Quelle est votre proposition ? ").upper()
    verification = verificationAction(action, verification)
    while verification == False :
        verification = verificationAction(action, verification)
        action = input("Votre entré n'est pas valide : ")
    return action 
#_________________________________________________________________________________________________________

def decryptageCredo(nom, chance, credoOfficiel, action):
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
        
listeCode= [["A","B","C","D","E","F","G","H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
            ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]]

credoOfficiel = "Tu as peu de chance de reussir, mais bon courage !"
nom = ""
action =""
ancienAction = ""
verification = False
chance = 0
réponse = "oui"

while réponse == "oui" :
    print()
    reglement ()
    nom = input("Quel est ton nom ? ").upper()
    clear()
    reglement()
    action = listeCode[0][random.randint(1,25)]
    nom, chance = decryptageCredo(nom, chance, credoOfficiel, action)
    while action != nom and chance < 5 :
        action = entré(action, verification)
        clear()
        reglement()
        nom, chance = decryptageCredo(nom, chance, credoOfficiel, action)

    if chance > 5 :
        réponse = input("Tu as perdu, veux tu recommencer ? ")
    else : 
        print("Tu as gagné la clé, Bravo !")
        réponse = "non"


