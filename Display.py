import Variable
import FonctionPrint
import Utilities
import Nourriture

def map1():
    # J'importe ma map d'un ficher txt
    with open("Map", "r", encoding = "utf-8") as map : 
        displayMap = [line for line in map]
    Variable.liste_Map = displayMap
    if len(Variable.var_enregistrer['positionArbreBanane']) == 0 :
        # Attribution des fruits dans les arbres
        Nourriture.globaleObjet() #  ligne 43
    axeY = 0
    # Pour chaque ligne puis chaque lettre, je print le caractere
    for line in displayMap:
        axeX = 0
        for caractere in line :
            # Vérification si le caractère est sur la position d'un fruit, si oui le caractère change
            caractere = Utilities.objetFruit(axeY, axeX, caractere) # ligne 62

            # Vérification si caractere est sur sur la position de la bouteille ou le couteau
            for k in Variable.var_enregistrer['sac_a_dos']:
                if axeY == Variable.var_enregistrer['sac_a_dos'][k]["positionY"] and axeX == Variable.var_enregistrer['sac_a_dos'][k]["positionX"]:
                    caractere = "×"

            # Attribution dans couleur pour chaque caractère
            if caractere in Variable.color_character :
                caractere = f'{Variable.color_character[caractere]["colorS"]}{Variable.color_character[caractere]["colorE"]}'

            # Vérification si l'enigme est déjà faite, si oui, la couleur change
            if caractere == "\u001b[38;5;226m♪\033[0m" :
                if axeY in Variable.var_enregistrer['positionEnigme'] and axeX in Variable.var_enregistrer['positionEnigme'] :
                    caractere = "\u001b[38;5;240m♪\033[0m"

            # Changement de couleur quand les 3 clés sont débloquées
            if caractere == "\u001b[38;5;226m♫\033[0m" and Variable.var_enregistrer['nbKey'] != 3:
                caractere = "\u001b[38;5;240m♫\033[0m"

            # Faire passer le joueur sous les arbres
            if Variable.var_enregistrer['positionJoueur'][0] == axeY and Variable.var_enregistrer['positionJoueur'][1] == axeX :
                Variable.var_enregistrer['ancienCaractere'] = caractere
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

            # Print les clés a côté de la map
            if axeY == 29 and axeX == 98:
                print("\u001b[38;5;226m♪\033[0m " * Variable.var_enregistrer['nbKey'], end ="")
        axeY += 1
    print()
    # Print les signes vitaux du joueur
    Utilities.displayvitalite() # ligne 41
    print()

    # Rentrer dans une enigme si le joueur et sur la bonne position
    Utilities.enigmeMystereCesarSinge () # ligne 239

    # Print une phrase si le joueur est sous un arbre
    FonctionPrint.arbre() # ligne 47

    # Print secouer les arbres pour faire tomber un fruit, Verifier si le joueur est sous un arbre
    FonctionPrint.bougerArbre() # ligne 54

    # Ramasser les objets et les mettre dans le sac à dos
    FonctionPrint.ramasserFruit() # ligne 77

    # Vérification des conditions de victoire, sauvegarde des scores
    Utilities.finish() # ligne 313
    
    # Aide aux déplacements
    if Variable.tricheur == False :
        # Vérification des signes vitaux, sauvegarde des scores, possibilité de rejouer 
        FonctionPrint.die() # ligne 174

    
