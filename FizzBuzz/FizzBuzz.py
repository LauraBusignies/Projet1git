import random
import time
import sys
import os


def clear ():
    os.system('cls')

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
        while len(listeJoueur) == ancienlen :

            chiffre = random.randint(1, 10 - nbJoueur[listeJoueur[compteur]])
            if nombre % 3 == 0 or nombre % 5 == 0 :
                if chiffre == 1 and nombre % 3 == 0:
                    print("Fizz, ", end = "")
                    
                elif chiffre == 1 and nombre % 5 == 0:
                    print('Buzz, ', end = "")
                    
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
        print("Bravo tu as gagné la clé !")
 