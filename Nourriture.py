
import random
import Variable

#__________________________________________________________________________________________________________________________
def ObjetAnanas():

        for loop in range(15) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != "γ" :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.positionAbreAnanas.append(emplacementY)
            Variable.positionAbreAnanas.append(emplacementX)

def ObjetMangue():

        for loop in range(15) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != "♣" :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.positionAbreMangue.append(emplacementY)
            Variable.positionAbreMangue.append(emplacementX)

def ObjetBanane():

        for loop in range(15) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != "↑" :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.positionAbreBanane.append(emplacementY)
            Variable.positionAbreBanane.append(emplacementX)
#__________________________________________________________________________________________________________________________

def globaleObjet():
    ObjetAnanas()
    ObjetBanane()
    ObjetMangue()
#__________________________________________________________________________________________________________________________

def verificationPositionArbre() :

    Variable.validationPositionFruit = False
    compteur = 0
    for loop in range(len(Variable.positionAbreAnanas)//2):
        if Variable.positionJoueur[0] == Variable.positionAbreAnanas[compteur] and Variable.positionJoueur[1] == Variable.positionAbreAnanas[compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.positionAbreBanane)//2):
        if Variable.positionJoueur[0] == Variable.positionAbreBanane[compteur] and Variable.positionJoueur[1] == Variable.positionAbreBanane[compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.positionAbreMangue)//2):
        if Variable.positionJoueur[0] == Variable.positionAbreMangue[compteur] and Variable.positionJoueur[1] == Variable.positionAbreMangue[compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2
#__________________________________________________________________________________________________________________________

def verificationPositionObjet() :

    Variable.validationPositionSol = False
    compteur = 0
    for loop in range(len(Variable.positionSolAnanas)//2):
        if Variable.positionJoueur[0] == Variable.positionSolAnanas[compteur] and Variable.positionJoueur[1] == Variable.positionSolAnanas[compteur+1] :
            Variable.validationPositionSol = True
            Variable.objetRamasser = "Ananas"
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.positionSolBanane)//2):
        if Variable.positionJoueur[0] == Variable.positionSolBanane[compteur] and Variable.positionJoueur[1] == Variable.positionSolBanane[compteur+1] :
            Variable.validationPositionSol = True
            Variable.objetRamasser = "Banane"
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.positionSolMangue)//2):
        if Variable.positionJoueur[0] == Variable.positionSolMangue[compteur] and Variable.positionJoueur[1] == Variable.positionSolMangue[compteur+1] :
            Variable.objetRamasser = "Mangue"
            Variable.validationPositionSol = True
        compteur += 2
#__________________________________________________________________________________________________________________________

# Supprimer la position des objet de la liste
#__________________________________________________________________________________________________________________________

def supprimerPositionArbreAnanas():
    compteur = 0
    for i in (Variable.positionAbreAnanas):
        if Variable.positionJoueur[0] == Variable.positionAbreAnanas[compteur] and Variable.positionJoueur[1] == Variable.positionAbreAnanas[compteur+1] :
            Variable.positionSolAnanas.append(Variable.positionAbreAnanas[compteur])
            Variable.positionSolAnanas.append(Variable.positionAbreAnanas[compteur+1])
            del Variable.positionAbreAnanas[compteur+1]
            del Variable.positionAbreAnanas[compteur]
            break
        compteur += 2
        
def supprimerPositionArbreBanane():
    compteur = 0
    for i in (Variable.positionAbreBanane):
        if Variable.positionJoueur[0] == Variable.positionAbreBanane[compteur] and Variable.positionJoueur[1] == Variable.positionAbreBanane[compteur+1] :
            Variable.positionSolBanane.append(Variable.positionAbreBanane[compteur])
            Variable.positionSolBanane.append(Variable.positionAbreBanane[compteur+1])
            del Variable.positionAbreBanane[compteur+1]
            del Variable.positionAbreBanane[compteur]
            break
        compteur += 2

def supprimerPositionArbreMangue():
    compteur = 0
    for i in (Variable.positionAbreMangue):
        if Variable.positionJoueur[0] == Variable.positionAbreMangue[compteur] and Variable.positionJoueur[1] == Variable.positionAbreMangue[compteur+1] :
            Variable.positionSolMangue.append(Variable.positionAbreMangue[compteur])
            Variable.positionSolMangue.append(Variable.positionAbreMangue[compteur+1])
            del Variable.positionAbreMangue[compteur+1]
            del Variable.positionAbreMangue[compteur]
            break
        compteur += 2
#_____________________________________________________________________________________________________________________________

def supprimerObjet():

    compteur = 0
    for i in (Variable.positionSolAnanas):
        if Variable.positionJoueur[0] == Variable.positionSolAnanas[compteur] and Variable.positionJoueur[1] == Variable.positionSolAnanas[compteur+1] :
            del Variable.positionSolAnanas[compteur +1]
            del Variable.positionSolAnanas[compteur]
            break
        compteur += 1
        
    compteur = 0
    for i in (Variable.positionSolBanane):
        if Variable.positionJoueur[0] == Variable.positionSolBanane[compteur] and Variable.positionJoueur[1] == Variable.positionSolBanane[compteur+1] :
            del Variable.positionSolBanane[compteur +1]
            del Variable.positionSolBanane[compteur]
            break
        compteur += 1

    compteur = 0
    for i in (Variable.positionSolMangue):
        if Variable.positionJoueur[0] == Variable.positionSolMangue[compteur] and Variable.positionJoueur[1] == Variable.positionSolMangue[compteur+1] :
            del Variable.positionSolMangue[compteur +1]
            del Variable.positionSolMangue[compteur]
            break
        compteur += 1


#_____________________________________________________________________________________________________________________________