import Variable
import message
import Utilities
import Nourriture

def map1():
    with open("Map", "r", encoding = "utf-8") as map : 
        displayMap = [line for line in map]
    Variable.liste_Map = displayMap
    if len(Variable.positionAbreBanane) == 0 :
        Nourriture.globaleObjet()
    axeY = 0
    # displayMap = Variable.liste_Map
    for line in displayMap:
        axeX = 0
        for caractere in line :
            caractere = Utilities.caracterePosition(axeY, axeX, caractere)
            for k in Variable.sac_a_dos:
                if axeY == Variable.sac_a_dos[k]["positionY"] and axeX == Variable.sac_a_dos[k]["positionX"]:
                    caractere = "×"
            if caractere in Variable.color_character :
                 caractere = f'{Variable.color_character[caractere]["colorS"]}{Variable.color_character[caractere]["colorE"]}'
            if Variable.positionJoueur[0] == axeY and Variable.positionJoueur[1] == axeX :
                Variable.ancienCaractere = caractere
                if caractere == "\u001b[38;5;64mγ\033[0m" :
                    caractere = "\u001b[38;5;64mγ\033[0m"
                elif caractere == "\u001b[38;5;76m↑\033[0m":
                    caractere = "\u001b[38;5;76m↑\033[0m"
                elif caractere == "\u001b[38;5;46m♣\033[0m":
                    caractere = "\u001b[38;5;46m♣\033[0m"
                else:
                    caractere = "☺"
            axeX += 1
            print(caractere, end="")
        axeY += 1
    print()
    print(f'|| Fatigue :{Variable.vitalité["Fatigue"]["stock"]} || Hydratation :{Variable.vitalité["Hydratation"]["stock"]} || Satiété :{Variable.vitalité["Satiété"]["stock"]} ||')
    print()
    message.arbre()
    message.bougerArbre()
    message.ramasserFruit()

    
