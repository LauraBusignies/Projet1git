import random
import time
import sys
import os



def clear ():
    os.system('cls')

def rules ():
    print("\nTe revoilà aventurier ! Pour gagner cette enigme tu devras gagner le jeu du FizzBuzz contre des singes !\n")
    time.sleep(1.5)
    print("Les règles du jeu sont :")
    time.sleep(1.5)
    print("On compte à tour de rôle en commençant à 1")
    time.sleep(1.0)
    print(" Si le nombre à annoncer est un multiple de 3, il faut dire Fizz au lieu du nombre.")
    time.sleep(1.0)
    print("     Si c’est un multiple de 5, il faut dire Buzz.")
    time.sleep(1.0)
    print("         Si c’est à la fois un multiple de 3 et 5 il faut dire FizzBuzz.")
    time.sleep(1.0)
    print("             Si on se trompe, on est éliminé de la partie et les joueurs restants recommencent jusqu’à ce qu’il n’en reste qu’un.")
    time.sleep(1.0)


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



def game ():
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
                if chiffre == 1 and nombre % 3 == 0:
                    print("Fizz, ", end = "")
                    
                elif chiffre == 1 and nombre % 5 == 0:
                    print('Buzz, ', end = "")

                elif chiffre == 1 and (nombre % 5 == 0 and nombre % 3 == 0) :
                    print("FizzBuzz", end="")

                else :
                    print(nombre)
                    print(f'{listeJoueur[compteur]} est éliminé'.capitalize())
                    time.sleep(1.0)
                    del listeJoueur[compteur]       
                    
            else :
                print (nombre,espace, end="")
                time.sleep(1.0)
            if compteur + 1 == len(listeJoueur) :
                compteur = 0
            else : 
                compteur += 1
            nombre += 1 
    return listeJoueur


def mainFizzBuzz():

    listeJoueur = []       
    listeJoueur = game ()        

    if "aventurier" not in listeJoueur:
        reponse = input("Tu as perdu, le chef ne veut pas te donner la clé, veux tu rejouer ? ").lower()
        while reponse == "non" and reponse == "oui" :
            reponse = input("Oui ou non ? ").lower()
        while reponse == "oui" :
            clear()
            listeJoueur = game ()
            reponse = input("Tu as perdu, le chef ne veut pas te donner la clé, veux tu rejouer ? ").lower()
            while reponse == "non" and reponse == "oui" :
                reponse = input("Oui ou non ? ").lower()
    else :
        clear()
        print("Bravo tout les singes ont perdu, tu as gagné la clé !")


#                  /88888888888888888888888888\
#                   |88888888888888888888888888/
#                    |~~____~~~~~~~~~"""""""""|
#                   / \_________/"""""""""""""\
#                  /  |              \         \
#                 /   |  88    88     \         \
#                /    |  88    88      \         \
#               /    /                  \        |
#              /     |   ________        \       |
#              \     |   \______/        /       |
#   /"\         \     \____________     /        |
#   | |__________\_        |  |        /        /
# /""""\           \_------'  '-------/       --
# \____/,___________\                 -------/
# ------*            |                    \