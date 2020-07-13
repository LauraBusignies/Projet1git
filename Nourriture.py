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
            Variable.positionAnanas.append(emplacementY)
            Variable.positionAnanas.append(emplacementX)

def ObjetMangue():

        for loop in range(15) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != "♣" :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.positionMangue.append(emplacementY)
            Variable.positionMangue.append(emplacementX)

def ObjetBanane():

        for loop in range(15) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != "↑" :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.positionBanane.append(emplacementY)
            Variable.positionBanane.append(emplacementX)
#__________________________________________________________________________________________________________________________

def globaleObjet():
    ObjetAnanas()
    ObjetBanane()
    ObjetMangue()
#__________________________________________________________________________________________________________________________

def verificationPositionArbre() :

    Variable.validationPositionFruit = False
    compteur = 0
    for loop in range(len(Variable.positionAnanas)//2):
        if Variable.positionJoueur[0] == Variable.positionAnanas[compteur] and Variable.positionJoueur[1] == Variable.positionAnanas[compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.positionBanane)//2):
        if Variable.positionJoueur[0] == Variable.positionBanane[compteur] and Variable.positionJoueur[1] == Variable.positionBanane[compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.positionMangue)//2):
        if Variable.positionJoueur[0] == Variable.positionMangue[compteur] and Variable.positionJoueur[1] == Variable.positionMangue[compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2
#__________________________________________________________________________________________________________________________

def verificationPositionObjet() :

    Variable.validationPositionSolFruit = False
    compteur = 0
    for loop in range(len(Variable.positionSolAnanas)//2):
        if Variable.positionJoueur[0] == Variable.positionSolAnanas[compteur] and Variable.positionJoueur[1] == Variable.positionSolAnanas[compteur+1] :
            Variable.validationPositionSolFruit = True
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.positionSolBanane)//2):
        if Variable.positionJoueur[0] == Variable.positionSolBanane[compteur] and Variable.positionJoueur[1] == Variable.positionSolBanane[compteur+1] :
            Variable.validationPositionSolFruit = True
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.positionSolMangue)//2):
        if Variable.positionJoueur[0] == Variable.positionSolMangue[compteur] and Variable.positionJoueur[1] == Variable.positionSolMangue[compteur+1] :
            Variable.validationPositionSolFruit = True
        compteur += 2
#__________________________________________________________________________________________________________________________

# Supprimer la position des objet de la liste
#__________________________________________________________________________________________________________________________

def supprimerPositionArbreAnanas():
    compteur = 0
    for i in (Variable.positionAnanas):
        if Variable.positionJoueur[0] == Variable.positionAnanas[compteur] and Variable.positionJoueur[1] == Variable.positionAnanas[compteur+1] :
            Variable.positionSolAnanas.append(Variable.positionAnanas[compteur])
            Variable.positionSolAnanas.append(Variable.positionAnanas[compteur+1])
            del Variable.positionAnanas[compteur+1]
            del Variable.positionAnanas[compteur]
            break
        compteur += 2
        
def supprimerPositionArbreBanane():
    compteur = 0
    for i in (Variable.positionBanane):
        if Variable.positionJoueur[0] == Variable.positionBanane[compteur] and Variable.positionJoueur[1] == Variable.positionBanane[compteur+1] :
            Variable.positionSolBanane.append(Variable.positionBanane[compteur])
            Variable.positionSolBanane.append(Variable.positionBanane[compteur+1])
            del Variable.positionBanane[compteur+1]
            del Variable.positionBanane[compteur]
            break
        compteur += 2

def supprimerPositionArbreMangue():
    compteur = 0
    for i in (Variable.positionMangue):
        if Variable.positionJoueur[0] == Variable.positionMangue[compteur] and Variable.positionJoueur[1] == Variable.positionMangue[compteur+1] :
            Variable.positionSolMangue.append(Variable.positionMangue[compteur])
            Variable.positionSolMangue.append(Variable.positionMangue[compteur+1])
            del Variable.positionMangue[compteur+1]
            del Variable.positionMangue[compteur]
            break
        compteur += 2
#_____________________________________________________________________________________________________________________________

def supprimerPositionSolAnanas():
    compteur = 0
    for i in (Variable.positionSolAnanas):
        if Variable.positionJoueur[0] == Variable.positionSolAnanas[compteur] and Variable.positionJoueur[1] == Variable.positionSolAnanas[compteur+1] :
            del Variable.positionSolAnanas[compteur +1]
            del Variable.positionSolAnanas[compteur]
            break
        compteur += 1
        
def supprimerPositionSolBanane():
    compteur = 0
    for i in (Variable.positionSolBanane):
        if Variable.positionJoueur[0] == Variable.positionSolBanane[compteur] and Variable.positionJoueur[1] == Variable.positionSolBanane[compteur+1] :
            del Variable.positionSolBanane[compteur +1]
            del Variable.positionSolBanane[compteur]
            break
        compteur += 1

def supprimerPositionSolMangue():
    compteur = 0
    for i in (Variable.positionSolMangue):
        if Variable.positionJoueur[0] == Variable.positionSolMangue[compteur] and Variable.positionJoueur[1] == Variable.positionSolMangue[compteur+1] :
            del Variable.positionSolMangue[compteur +1]
            del Variable.positionSolMangue[compteur]
            break
        compteur += 1


#_____________________________________________________________________________________________________________________________