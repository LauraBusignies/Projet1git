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
        Utilities.verificationObjetSol()
        if Variable.deplacement == "r" and Variable.validationPositionSol == False :
            print("Il n'y a rien a ramasser")
        else : 
            print(Variable.sac_a_dos[Variable.objetRamasser]["Ramassage"])
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
                    Nourriture.supprimerObjet()


#__________________________________________________________________________________________________________________________


def displaySac():

    Utilities.clear()
    Variable.contenuInventaire = []
    def VisuelSac(contenuSac):
        for k in Variable.sac_a_dos:
            if Variable.sac_a_dos[k]['nombre'] > 0 :
                contenuSac.append(f"{Variable.sac_a_dos[k]['nom']} * {Variable.sac_a_dos[k]['nombre']}")
                Variable.contenuInventaire.append(Variable.sac_a_dos[k]['nom'])
        return contenuSac
    
    contenuSac = []
    contenuSac = VisuelSac(contenuSac)

    print("\n              ▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("             ▓▓           ▓▓")
    print("            ▓▓             ▓▓")
    print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(" ▓▓                                 ▓▓")

    for i in range(0, len(contenuSac)):
        espace = 23 - len(contenuSac[i])
        espace = " " * espace
        print(f" ▓▓          {contenuSac[i]}{espace}▓▓")
    print(" ▓▓                                 ▓▓")
    print(f"  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")

    listeAction =["l", "u", "d"]
    action =input("Que veux tu faire ? Sortir du sac -> L / Utiliser un objet de ton sac -> U + NomObjet / Jetter un objet de ton sac -> D + objet \n").lower()
    Variable.checkActionSac = False
    Utilities.checkAction(action, listeAction)
    while Variable.checkActionSac == False :
        action = input("L"" pour leave le sac, U + Objet pour l'utiliser, D + Objet pour le jetter ")
        Utilities.checkAction(action, listeAction)
    if Variable.lettre == "l" :
        Utilities.clear()
    elif Variable.lettre == "d":
        Utilities.deleteObjet()
        




