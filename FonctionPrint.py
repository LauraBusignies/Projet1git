import Variable
import random
import Utilities
import Display
import Nourriture
import sys
import json
import time

def welcome():
    print("\u001b[38;5;64m ____  _                                                               _              _           ")
    print("|  _ \(_)                                          /\                 | |            (_)          ")
    print("| |_) |_  ___ _ ____   _____ _ __  _   _  ___     /  \__   _____ _ __ | |_ _   _ _ __ _  ___ _ __ ")
    print("|  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| | | |/ _ \   / /\ \ \ / / _ \ '_ \| __| | | | '__| |/ _ \ '__|")
    print("| |_) | |  __/ | | \ V /  __/ | | | |_| |  __/  / ____ \ V /  __/ | | | |_| |_| | |  | |  __/ |   ")
    print("|____/|_|\___|_| |_|\_/ \___|_| |_|\__,_|\___| /_/    \_\_/ \___|_| |_|\__|\__,_|_|  |_|\___|_|\033[0m  ")
    print()
    
#__________________________________________________________________________________________________________________________

def start():
    welcome()
    validation = input("   1 -> Voir historique \u001b[38;5;64m/\033[0m 2 -> Charger ancienne partie \u001b[38;5;64m/\033[0m 3 -> Commencer nouvelle partie\n").lower()
    print()
    if validation == "1" :
        Utilities.historique() # ligne 268
    Utilities.clear()
    welcome()
    with open("Enregistrement.json", "r", encoding="utf-8") as MyFile:
        Variable.var_enregistrer = json.load(MyFile)
    if validation == "2" :
        if Variable.var_enregistrer['leave'] == True :
            print("Te revoilà ",Variable.var_enregistrer['nomAventurier'])
            time.sleep(1.5)
        else :
            print("La partie n'a pas pu être chargée")
            with open("VariableDebut.json", "r", encoding="utf-8") as MyFile:
                Variable.var_enregistrer = json.load(MyFile)   
            Variable.var_enregistrer['nomAventurier'] = input('Quel est ton nom ? ').capitalize()
    else : 
        with open("VariableDebut.json", "r", encoding="utf-8") as MyFile:
            Variable.var_enregistrer = json.load(MyFile)    
        Variable.var_enregistrer['nomAventurier'] = input('Quel est ton nom ? ').capitalize()

#__________________________________________________________________________________________________________________________     
# Print une phrase si le joueur est sous un arbre
def arbre ():
    if Variable.var_enregistrer['ancienCaractere'] == "\u001b[38;5;64mγ\033[0m" or Variable.var_enregistrer['ancienCaractere'] == "\u001b[38;5;76m↑\033[0m" or Variable.var_enregistrer['ancienCaractere'] == "\u001b[38;5;46m♣\033[0m": 
        print("Vous êtes cachez sous un arbres")
        print("Bougez le avec ""b"", un fruit tombera peut etre")

#__________________________________________________________________________________________________________________________
# Print secouer les arbres pour faire tomber un fruit, Verifier si le joueur est sous un arbre
def bougerArbre():
    # Verifier si l'arbre contient un fruit 
    Nourriture.verificationPositionArbre() # ligne 50

    if Variable.deplacement == "b":
        if Variable.deplacement == "b" and Variable.validationPositionFruit == True:
            
            if Variable.var_enregistrer['ancienCaractere'] == "\u001b[38;5;64mγ\033[0m" :
                print(" Oh ! Un ananas est tomber, appui sur R pour le ramasser")
                Nourriture.supprimerPositionArbreAnanas() # ligne 99
            elif Variable.var_enregistrer['ancienCaractere'] == "\u001b[38;5;76m↑\033[0m" :
                print(" Oh ! Une banane est tomber, appui sur R pour la ramasser")
                Nourriture.supprimerPositionArbreBanane() # ligne 110
            else :
                print(" Oh ! Une mangue est tomber, appui sur R pour la ramasser")
                Nourriture.supprimerPositionArbreMangue() # ligne 121
        elif Variable.deplacement == "b" and Variable.var_enregistrer['ancienCaractere'] in Variable.listeArbre and Variable.validationPositionFruit == False :
            print("Rien n'est tombé")
        else :
            print("Tu n'as rien a bouger, tu dois etre sous un arbre")        

#__________________________________________________________________________________________________________________________
# Ramasser les objets
def ramasserFruit():
    
    if Variable.deplacement == "r" :
        #Verifier la position des objets
        Nourriture.verificationPositionObjet() # ligne 73
        Utilities.verificationObjetSol() # ligne 90
        if Variable.deplacement == "r" and Variable.validationPositionSol == False :
            print("Il n'y a rien a ramasser")
        #Proposer de mettre l'objet dans le sac
        else : 
            print(Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]["Ramassage"])
            decision = input("Souhaitez vous mettre cette objet dans votre sac ? ").lower()
            decision = Utilities.YesOrNo(decision) # ligne 25
            if decision == "oui" :
                # Verifier si le sac à dos est plein
                Utilities.nombreObjet() # ligne 98
                if Variable.compteurStock >= 10 :
                    print("Vous ne pouvez pas le prendre, votre sac à dos est pleins")
                else :
                    # Mettre un objet dans le sac à dos 
                    Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]['nombre'] += 1
                    print("Vous avez",Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]['nombre'],Variable.var_enregistrer['objetRamasser'])
                    Nourriture.supprimerObjet() # ligne 134
                    if Variable.var_enregistrer['objetRamasser'] not in Variable.listeFruit :
                        Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]["positionY"] = None
                        Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]["positionX"] = None


#__________________________________________________________________________________________________________________________

#print le sac a dos
def displaySac():
     
    Utilities.clear()
    Variable.contenuInventaire = []
    # Mettre les item du dictionnaire sac a dos dans une liste pour pouvoir les print
    def VisuelSac(contenuSac):
        for k in Variable.var_enregistrer['sac_a_dos']:
            if Variable.var_enregistrer['sac_a_dos'][k]['nombre'] > 0 :
                # Pour chaque objet dans l'inventaire, j'ajoute à ma liste nom de l'objet avec sa quantité
                contenuSac.append(f"{Variable.var_enregistrer['sac_a_dos'][k]['nom']} * {Variable.var_enregistrer['sac_a_dos'][k]['nombre']}")
                Variable.contenuInventaire.append(Variable.var_enregistrer['sac_a_dos'][k]['nom'])
        return contenuSac
    
    contenuSac = []
    contenuSac = VisuelSac(contenuSac)
    # print le sac a dos 
    action = ""
    while action != "l" :
        print("\n              ▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print("             ▓▓           ▓▓")
        print("            ▓▓             ▓▓")
        print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print(" ▓▓                                 ▓▓")
        # Je print ma liste contenu Sac
        for i in range(0, len(contenuSac)):
            espace = 23 - len(contenuSac[i])
            espace = " " * espace
            print(f" ▓▓          {contenuSac[i]}{espace}▓▓")
        print(" ▓▓                                 ▓▓")
        print(f"  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")

        listeAction =["l", "u", "d"]
        # Print les signes vitaux
        print(f'|| Energie :{Variable.var_enregistrer["vitalite"]["Energie"]["Stock"]} || Hydratation :{Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"]} || Satiete :{Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"]} ||\n')
        action =input("Que veux tu faire ? Sortir du sac -> L / Utiliser un objet de ton sac -> U + NomObjet / Jetter un objet de ton sac -> D + objet \n").lower()
        Variable.checkActionSac = False

        # Je vérifie que l'action est valide
        Utilities.checkAction(action, listeAction) # ligne 106
        while Variable.checkActionSac == False :
            action = input("L"" pour leave le sac, U + Objet pour l'utiliser, D + Objet pour le jetter ")
            Utilities.checkAction(action, listeAction) # ligne 106

        # Si l'action est de delete
        if Variable.lettre == "d":

            # Je retire l'objet de mon dic Sac à dos, si c'est un fruit je l'ajoute a une liste de fruit, sinon je met sa position dans le dic
            Utilities.deleteObjet() # ligne 128

            # Clear et remet la map
            Utilities.clear()

        # SI l'action est d'utiliser
        elif Variable.lettre == "u" :

            # J'ajoute l'objet a mes signaux vitaux en calculant si le personnage en a besoin ou non, puis je calcule l'eau de la bouteille
            Utilities.utiliserObjet() # ligne 148
            Utilities.clear()

#__________________________________________________________________________________________________________________________


def die():
    # Je vérifie si aucun de mes signe vitaux n'est a zéro
    if Variable.var_enregistrer["vitalite"]["Energie"]["Stock"] <= 0 or Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"] <= 0 or Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"] <= 0 :
        Utilities.clear()
        print("    ▄· ▄▌      ▄• ▄▌▄▄▄      ·▄▄▄▄  ▄▄▄ . ▄▄▄· ·▄▄▄▄")  
        print("   ▐█▪██▌▪     █▪██▌▀▄ █·    ██▪ ██ ▀▄.▀·▐█ ▀█ ██▪ ██ ")
        print("   ▐█▌▐█▪ ▄█▀▄ █▌▐█▌▐▀▀▄     ▐█· ▐█▌▐▀▀▪▄▄█▀▀█ ▐█· ▐█▌")
        print("    ▐█▀·.▐█▌.▐▌▐█▄█▌▐█•█▌    ██. ██ ▐█▄▄▌▐█ ▪▐▌██. ██") 
        print("     ▀ •  ▀█▄▀▪ ▀▀▀ .▀  ▀    ▀▀▀▀▀•  ▀▀▀  ▀  ▀ ▀▀▀▀▀•")
        print("                    _,.-------.,_")
        print("                 ,;~'             '~;, ")
        print("               ,;                     ;,")
        print("              ;                         ;")
        print("             ,'                         ',")
        print("            ,;                           ;,")
        print("            ; ;      .           .      ; ;")
        print("            | ;   ______       ______   ; | ")
        print("            |  `/~'     ~' . '~     '~\'   |")
        print("            |  ~  ,-~~~^~, | ,~^~~~-,  ~  |")
        print("             |   |        }:{        |   | ")
        print("             |   l       / | \       !   |")
        print("             .~  (__,.--'.^.  '--.,__)  ~. ")
        print("             |     ---;' / | \ `;---     |  ")
        print("              \__.       \/^\/       .__/  ")
        print("                | \                 / |  ")
        print("                | |T~\___!___!___/~T| |  ")
        print("                | |`IIII_I_I_I_IIII'| |  ")
        print("                |  \,III I I I III,/  |  ")
        print("                 \   `~~~~~~~~~~'    /")
        print("                   \   .       .   /")
        print("                     \.    ^    ./   ")

        print()

        # J'enregistre si le joueur a gagné ou non et la date pour l'historique
        Variable.var_enregistrer['resultatJeu'] = 'Defaite'
        Variable.var_enregistrer['date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        #J 'utilise le try dans la possibilité où l'historique est vide
        # Ma variable dicHistorique prend les données du fichier Historique
        try :
            with open("Historique.json", "r", encoding="utf-8") as MyFile:
                Variable.dicHistorique = json.load(MyFile)
        except : 
            pass

        # J'ajoute les nouveaux score 
        Variable.dicHistorique['compteurHistorique'] += 1
        Variable.dicHistorique[f'joueur{Variable.dicHistorique["compteurHistorique"]}'] = [Variable.var_enregistrer['nomAventurier'],
                            Variable.var_enregistrer['resultatJeu'],
                            Variable.var_enregistrer['nombreAction'],
                            Variable.var_enregistrer['nombreDeplacement'],
                            Variable.var_enregistrer['vitalite']['Energie']['Stock'],
                            Variable.var_enregistrer['vitalite']['Satiete']['Stock'],
                            Variable.var_enregistrer['vitalite']['Hydratation']['Stock'],
                            Variable.var_enregistrer['date']]

        # Je verifie que mon historique n'est pas plus grand que 10 joueur, "compteur = -1" car l'historique contient une variable qui n'est pas un score
        # compteur = -1
        # for k in Variable.dicHistorique :
        #     compteur += 1

        # while compteur >= 11 :
        #     Variable.var_enregistrer['listeHistorique'] = []
        #     # Si mon historique > 10 je supprime le joueur à la date la plus ancienne
        #     for k in Variable.dicHistorique:
        #         if k == 'compteurHistorique' :
        #             pass
        #         else :
        #             Variable.var_enregistrer['listeHistorique'].append(Variable.dicHistorique[k][7])
        #     #J'ajoute les date a une liste, je la tri, et la valeur qui correspond a la date la plus ancienne est supprimée
        #     Variable.var_enregistrer['listeHistorique'].sort()
        #     print(Variable.dicHistorique)
        #     for k in Variable.dicHistorique :
        #         try :
        #             if Variable.dicHistorique[k][7] == Variable.var_enregistrer['listeHistorique'][0] :
        #                 del Variable.dicHistorique[k]
        #                 compteur += -1
        #                 break
        #         except :
        #             pass


        # J'enregistre la nouvel historique dans le fichier json
        with open("Historique.json", "w", encoding="utf-8") as MyFile:
            json.dump(Variable.dicHistorique, MyFile, sort_keys = True, indent = 4, ensure_ascii = False)

        #Je propose au joueur de rejouer
        réponse = input("Veux tu rejouer ? ").lower()
        while réponse != "oui" and réponse != "non" :
            réponse = input("Oui ou non ? ") 
        if réponse == "non" :
            # Si non je sors du programme
            sys.exit (0)
        else :
            # Sinon les variable redevienne celle du debut
            with open("VariableDebut.json", "r", encoding="utf-8") as MyFile:
                Variable.var_enregistrer = json.load(MyFile)
            Utilities.afterClear()
#__________________________________________________________________________________________________________________________
      
def victory ():
    print("  o              o   __o__       o__ __o    ____o__ __o____     o__ __o        o__ __o    \o       o/ ")
    print(" <|>            <|>    |        /v     v\    /   \   /   \     /v     v\      <|     v\    v\     /v  ")
    print(" < >            < >   / \      />                 \o/         />       <\     / \     <\    <\   />   ")
    print("  \o            o/    \o/    o/                    |        o/           \o   \o/     o/      \o/     ")
    print("   v\          /v      |    <|                    < >      <|             |>   |__  _<|        |      ")
    print("    <\        />      < >    \\                     |        \\\           //    |       \      / \     ")
    print("      \o    o/         |       \                   o          \         /     <o>       \o    \o/     ")
    print("       v\  /v          o        o       o         <|           o       o       |         v\    |      ")
    print("        <\/>         __|>_      <\__ __/>         / \          <\__ __/>      / \         <\  / \   ") 




