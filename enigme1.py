import random
import time 
import os

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

    time.sleep(0.5)
    adventurer_number = input("Choisis ton chiffre : ").strip().lower()
    validation = False 
    while not validation:
        if not adventurer_number.isdigit() or int(adventurer_number) >= 100 or int(adventurer_number) <= 0 :
            adventurer_number = input("Choisissez un chiffre entre 0 et 100 : ")
        if adventurer_number.isdigit() and int(adventurer_number) < 100 and int(adventurer_number) > 0 :
            validation = True
            return adventurer_number

# Définir si c'est moins ou plus 
def game(adventurer_number, counter, mystery_number, total_counter):

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
def victory_or_defeat(victory):

    if  int(adventurer_number) == mystery_number :
        print()
        print(f"Bravo tu as gagné le niveau {counter_game} ")
        time.sleep(2.0)
    else : 
        print()
        print(f"Perdu ! Tu as utilisé tes {try_number} essaies. Tu dois recommencer ! 凸(^_^)凸")
        victory = False
        time.sleep(2.0)
    return victory

# Clear la console
def clear():
    os.system('cls') #pour Windows

# Assemblement des fonction

# Variables global

adventurer_number = 0
counter = 0
total_counter = 0
victory = True 
counter_game = 0
yes_or_no = 'non'


if __name__ == '__main__' :

    rules_mystery_number()
    yes_or_no = input("Et tu prêt à commencer ? Oui ou Non : ").lower()
    while yes_or_no != "oui" :
        yes_or_no=input("Tant que tu ne diras pas oui, on sera coincé ici !").lower()
    while counter_game != 3 :
        for loop in range (3) :
            mystery_number = random.randint(0, 100)
            try_number = random.randint(1,3)
            counter_game += 1

            clear()
            if counter_game == 1 :
                print("Tu vas commencer le 1er NOMBRE MYSTERIEUX ")
                time.sleep(1.0)
                print("Le sphinx choisis combien tu auras d'essai pour ce test")
                time.sleep(1.0)
                print("Suspense ...")
                time.sleep(1.0)
                print(f"Tu auras {try_number} essaies !\n")
            else :
                print(f"Tu vas commencer le {counter_game+1}ème NOMBRE MYSTERIEUX ")
                time.sleep(1.0)
                print("Le sphinx choisis combien tu auras d'essai pour ce test")
                time.sleep(1.0)
                print("Suspense ...")
                time.sleep(1.0)
                print(f"Tu auras {try_number} essaies !\n")
            
            adventurer_number, counter, total_counter = game(adventurer_number, counter, mystery_number, total_counter)
            victory = victory_or_defeat(victory)
            if victory == False :
                counter_game = 0
                break 
    print()
    print(f"BRAVO ! tu as gagné les trois manches avec {total_counter} essaies ! Tu as bien mérité cette clé 🔑")
