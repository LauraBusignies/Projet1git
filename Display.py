import Variable
import message
import Utilities

def map1():
    with open("Map", "r", encoding = "utf-8") as map : 
        displayMap = [line for line in map]
    Variable.liste_Map = displayMap
    if len(Variable.positionObjet) ==0 :
        Utilities.NourritureObjet()
    axeY = 0
    # displayMap = Variable.liste_Map
    for line in displayMap:
        axeX = 0
        for caractere in line :
            compteur = 0
            for loop in range(len(Variable.positionObjet)//2):
                if axeY == Variable.positionObjet[compteur] and axeX == Variable.positionObjet[compteur+1] :
                    caractere = "○"
                compteur += 2
            # if caractere in Variable.color_character :
            #      caractere = f'{Variable.color_character[caractere]["colorS"]}{Variable.color_character[caractere]["image"]}{Variable.color_character[caractere]["colorE"]}'
            if Variable.positionJoueur[0] == axeY and Variable.positionJoueur[1] == axeX:
                Variable.ancienCaractere = caractere
                if caractere == "γ":
                    caractere = "γ"
                elif caractere == "↑":
                    caractere = "↑"
                elif caractere == "♣":
                    caractere = "♣"
                else:
                    caractere = "☺"
            axeX += 1
            print(caractere, end="")
        axeY += 1
    print()
    print(Variable.ancienCaractere)
    message.arbre()
    Utilities.afterClear()
    message.ObjetSol()