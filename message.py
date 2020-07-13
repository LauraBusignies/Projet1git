import Variable
import random
import Utilities
import Display
import Nourriture

def arbre ():
    if Variable.ancienCaractere == "γ" or Variable.ancienCaractere == "↑" or Variable.ancienCaractere == "♣": 
        print("Vous êtes cachez sous un arbres")
        print("Bougez le avec ""b"", un fruit tombera peut etre")

#__________________________________________________________________________________________________________________________
    
def bougerArbre():
    Nourriture.verificationPositionArbre()

    if Variable.deplacement == "b":
        if Variable.deplacement == "b" and Variable.validationPositionFruit == True:
            
            if Variable.ancienCaractere == "γ" :
                print(" Oh ! Un ananas est tomber, appui sur R pour le ramasser")
                Nourriture.supprimerPositionArbreAnanas()
            elif Variable.ancienCaractere == "↑" :
                print(" Oh ! Une banane est tomber, appui sur R pour la ramasser")
                Nourriture.supprimerPositionArbreBanane()
            else :
                print(" Oh ! Une mangue est tomber, appui sur R pour la ramasser")
                Nourriture.supprimerPositionArbreMangue()
        elif Variable.deplacement == "b" and Variable.ancienCaractere in Variable.listeArbre and Variable.validationPositionFruit == False :
            print("Rien n'est tombé")
        else :
            print("Tu n'as rien a bouger, tu dois etre sous un arbre")        

#__________________________________________________________________________________________________________________________

def ramasserFruit():
    
    fruit = ""
    if Variable.deplacement == "r" :
        Nourriture.verificationPositionObjet()
        if Variable.deplacement == "r" and Variable.validationPositionSolFruit == False :
            print("Il n'y a rien a ramasser")
        else : 
            decision = input("Souhaitez vous mettre cette objet dans votre sac ? ").lower()
            while decision != "oui" and decision != "non" :
                decision = input("Veuillez choisir oui ou non ")
            if decision == "oui" :
                Utilities.nombreObjet()
                if Variable.compteurStock >= 10 :
                    print("Vous ne pouvez pas le prendre, votre sac à dos est pleins")
                else :
                    if Variable.ancienCaractere == "γ":
                        fruit = "Ananas"
                    elif Variable.ancienCaractere == "↑" :
                        fruit = "Banane"
                    else:
                        fruit = "Mangue"
                    Variable.sac_a_dos[fruit]['nombre'] += 1
                    print(Variable.sac_a_dos[fruit]['nombre'])
                    if fruit == "Ananas":
                        Nourriture.supprimerPositionSolAnanas()
                    elif fruit == "Banane":
                        Nourriture.supprimerPositionSolBanane()
                    else :
                        Nourriture.supprimerPositionSolMangue()

# def ObjetSac():
#     if Variable.deplacement == "o" :


def supprimerObjet():
    if Variable.deplacement == "o":
        Utilities.clear()
        Utilities.displaySac()





