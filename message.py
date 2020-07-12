import Variable
import random
import Utilities
import Display

def arbre ():
    if Variable.ancienCaractere == "γ" or Variable.ancienCaractere == "↑" or Variable.ancienCaractere == "♣": 
        print("Vous êtes cachez sous un arbres")

def ObjetSol():
    
    if Variable.ancienCaractere == '○' :
        print("Vous êtes sur un objet, ramassez le pour voir ce que c'est !")
        if Variable.deplacement == "r" :
            object = random.choice(Variable.listeObjet)
            print (Variable.sac_a_dos[object]['Ramassage'])
            decision = input("Souhaitez vous le mettre dans votre sac à dos ? ").lower()
            while decision != "oui" and decision != "non" :
                decision = input("Veuillez choisir oui ou non ")
            if decision == "oui" :
                Utilities.nombreObjet()
                if Variable.compteurS >= 10 :
                    print("Vous ne pouvez pas le prendre, votre sac à dos est pleins")
                else : 
                    Variable.sac_a_dos[object]['nombre'] += 1
                    print(Variable.sac_a_dos[object]['nombre'])
    if Variable.deplacement == "r" and Variable.ancienCaractere != "○" :
        print("Il n'y a rien a ramasser")

# def ObjetSac():
#     if Variable.deplacement == "o" :


