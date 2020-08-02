import random
import Variable

#__________________________________________________________________________________________________________________________
def ObjetAnanas():

        for loop in range(20) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != "γ" :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.var_enregistrer['positionArbreAnanas'].append(emplacementY)
            Variable.var_enregistrer['positionArbreAnanas'].append(emplacementX)

def ObjetMangue():

        for loop in range(20) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != "♣" :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.var_enregistrer['positionArbreMangue'].append(emplacementY)
            Variable.var_enregistrer['positionArbreMangue'].append(emplacementX)

def ObjetBanane():

        for loop in range(20) :
            emplacementX = random.randint (1, 80)
            emplacementY = random.randint (2, 25)
            while Variable.liste_Map[emplacementY][emplacementX] != "↑" :
                emplacementX = random.randint (1, 80)
                emplacementY = random.randint (2, 25)
            Variable.var_enregistrer['positionArbreBanane'].append(emplacementY)
            Variable.var_enregistrer['positionArbreBanane'].append(emplacementX)
#__________________________________________________________________________________________________________________________

def globaleObjet():
    ObjetAnanas()
    ObjetBanane()
    ObjetMangue()
#__________________________________________________________________________________________________________________________

def verificationPositionArbre() :

    Variable.validationPositionFruit = False
    compteur = 0
    for loop in range(len(Variable.var_enregistrer['positionArbreAnanas'])//2):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionArbreAnanas'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionArbreAnanas'][compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.var_enregistrer['positionArbreBanane'])//2):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionArbreBanane'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionArbreBanane'][compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.var_enregistrer['positionArbreMangue'])//2):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionArbreMangue'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionArbreMangue'][compteur+1] :
            Variable.validationPositionFruit = True
        compteur += 2
#__________________________________________________________________________________________________________________________

def verificationPositionObjet() :

    Variable.validationPositionSol = False
    compteur = 0
    for loop in range(len(Variable.var_enregistrer['positionSolAnanas'])//2):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionSolAnanas'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionSolAnanas'][compteur+1] :
            Variable.validationPositionSol = True
            Variable.var_enregistrer['objetRamasser'] = "Ananas"
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.var_enregistrer['positionSolBanane'])//2):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionSolBanane'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionSolBanane'][compteur+1] :
            Variable.validationPositionSol = True
            Variable.var_enregistrer['objetRamasser'] = "Banane"
        compteur += 2

    compteur = 0
    for loop in range(len(Variable.var_enregistrer['positionSolMangue'])//2):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionSolMangue'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionSolMangue'][compteur+1] :
            Variable.var_enregistrer['objetRamasser'] = "Mangue"
            Variable.validationPositionSol = True
        compteur += 2
#__________________________________________________________________________________________________________________________

# Supprimer la position des objet de la liste
#__________________________________________________________________________________________________________________________

def supprimerPositionArbreAnanas():
    compteur = 0
    for i in (Variable.var_enregistrer['positionArbreAnanas']):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionArbreAnanas'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionArbreAnanas'][compteur+1] :
            Variable.var_enregistrer['positionSolAnanas'].append(Variable.var_enregistrer['positionArbreAnanas'][compteur])
            Variable.var_enregistrer['positionSolAnanas'].append(Variable.var_enregistrer['positionArbreAnanas'][compteur+1])
            del Variable.var_enregistrer['positionArbreAnanas'][compteur+1]
            del Variable.var_enregistrer['positionArbreAnanas'][compteur]
            break
        compteur += 2
        
def supprimerPositionArbreBanane():
    compteur = 0
    for i in (Variable.var_enregistrer['positionArbreBanane']):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionArbreBanane'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionArbreBanane'][compteur+1] :
            Variable.var_enregistrer['positionSolBanane'].append(Variable.var_enregistrer['positionArbreBanane'][compteur])
            Variable.var_enregistrer['positionSolBanane'].append(Variable.var_enregistrer['positionArbreBanane'][compteur+1])
            del Variable.var_enregistrer['positionArbreBanane'][compteur+1]
            del Variable.var_enregistrer['positionArbreBanane'][compteur]
            break
        compteur += 2

def supprimerPositionArbreMangue():
    compteur = 0
    for i in (Variable.var_enregistrer['positionArbreMangue']):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionArbreMangue'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionArbreMangue'][compteur+1] :
            Variable.var_enregistrer['positionSolMangue'].append(Variable.var_enregistrer['positionArbreMangue'][compteur])
            Variable.var_enregistrer['positionSolMangue'].append(Variable.var_enregistrer['positionArbreMangue'][compteur+1])
            del Variable.var_enregistrer['positionArbreMangue'][compteur+1]
            del Variable.var_enregistrer['positionArbreMangue'][compteur]
            break
        compteur += 2
#_____________________________________________________________________________________________________________________________

def supprimerObjet():

    compteur = 0
    for i in (Variable.var_enregistrer['positionSolAnanas']):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionSolAnanas'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionSolAnanas'][compteur+1] :
            del Variable.var_enregistrer['positionSolAnanas'][compteur +1]
            del Variable.var_enregistrer['positionSolAnanas'][compteur]
            break
        compteur += 1
        
    compteur = 0
    for i in (Variable.var_enregistrer['positionSolBanane']):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionSolBanane'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionSolBanane'][compteur+1] :
            del Variable.var_enregistrer['positionSolBanane'][compteur +1]
            del Variable.var_enregistrer['positionSolBanane'][compteur]
            break
        compteur += 1

    compteur = 0
    for i in (Variable.var_enregistrer['positionSolMangue']):
        if Variable.var_enregistrer['positionJoueur'][0] == Variable.var_enregistrer['positionSolMangue'][compteur] and Variable.var_enregistrer['positionJoueur'][1] == Variable.var_enregistrer['positionSolMangue'][compteur+1] :
            del Variable.var_enregistrer['positionSolMangue'][compteur +1]
            del Variable.var_enregistrer['positionSolMangue'][compteur]
            break
        compteur += 1


#_____________________________________________________________________________________________________________________________