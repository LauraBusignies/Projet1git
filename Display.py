# coding: utf-8
import Variable
import map2

# color_code = {"♣" : "\033[33m"}    
liste_color = list(Variable.color_character)

displayMap = map2.MapInAList

# with open("Map", "r", encoding = "utf-8") as map : 
#     displayMap = [line for line in map]

def addColorToAnEl(element):
    element = Variable.color_character[element]["color"]
    return element

def map(displayMap):
    y = 26
    x = 84
    axeY = 0
    for line in displayMap:
        axeX = 0
        linePrinted = ""
        for caractere in line :
            # if caractere in Variable.color_character:
            #     caractere = addColorToAnEl(caractere)
            if caractere == "♣":
                caractere = "\033[33m♣\033[0m"
            # elif caractere == "■" :
            #     caractere = "\033[32m■\033[0m"

            # caractere = Variable.color_character[caractere]["color"]
            if y == axeY and x == axeX:
                caractere = 0
            linePrinted = f"{linePrinted}{caractere}"
            axeX += 1
        print(linePrinted)
        axeY += 1

map(displayMap)

def entrerDeplacement():

    Variable.nombre = 1
    entrer = input("Entrez une instruction  : ")
    if entrer != "" :
        Variable.deplacement = entrer[0]
    if len(entrer) > 1 :
        Variable.nombre = entrer[1:]
    listeDeplacement= ["z", "q","s","d"]
    while Variable.deplacement not in listeDeplacement :
            print("Veuillez saisir une lettre entre Z, Q , S, D. \n Z pour monter \n S pour descendre \n D pour aller a droite \n Q pour aller a gauche")
            entrer = (input("Entrez une instruction : ")).lower()
            print()
            if entrer != "" :
                Variable.deplacement = entrer[0]
            if len(entrer) > 1 :
                Variable.nombre = entrer[1:]


# def clear():
#     os.system('cls') #pour Windows