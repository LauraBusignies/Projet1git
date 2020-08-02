import Variable
import message
import Utilities
import Nourriture

def map1():
    with open("Map", "r", encoding = "utf-8") as map : 
        displayMap = [line for line in map]
    Variable.liste_Map = displayMap
    if len(Variable.var_enregistrer['positionArbreBanane']) == 0 :
        Nourriture.globaleObjet()
    axeY = 0
    # displayMap = Variable.liste_Map
    for line in displayMap:
        axeX = 0
        for caractere in line :
            caractere = Utilities.caracterePosition(axeY, axeX, caractere)


            for k in Variable.var_enregistrer['sac_a_dos']:
                if axeY == Variable.var_enregistrer['sac_a_dos'][k]["positionY"] and axeX == Variable.var_enregistrer['sac_a_dos'][k]["positionX"]:
                    caractere = "×"
            if caractere in Variable.color_character :
                caractere = f'{Variable.color_character[caractere]["colorS"]}{Variable.color_character[caractere]["colorE"]}'
            if caractere == "\u001b[38;5;226m♪\033[0m" :
                if axeY in Variable.var_enregistrer['positionEnigme'] and axeX in Variable.var_enregistrer['positionEnigme'] :
                    caractere = "\u001b[38;5;240m♪\033[0m"
            if caractere == "\u001b[38;5;226m♫\033[0m" and Variable.var_enregistrer['nbKey'] != 3:
                caractere = "\u001b[38;5;240m♫\033[0m"

            if Variable.var_enregistrer['positionJoueur'][0] == axeY and Variable.var_enregistrer['positionJoueur'][1] == axeX :
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
    Utilities.displayvitalite()
    print()
    Utilities.enigmeMystereCesarSinge ()
    message.arbre()
    message.bougerArbre()
    message.ramasserFruit()
    Utilities.finish()
    if Variable.tricheur == False :
        message.die()

    
