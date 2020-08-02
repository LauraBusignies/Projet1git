import Variable
import random
import Utilities
import Display
import Nourriture
import sys
import json
import time


def arbre ():
    if Variable.ancienCaractere == "\u001b[38;5;64mγ\033[0m" or Variable.ancienCaractere == "\u001b[38;5;76m↑\033[0m" or Variable.ancienCaractere == "\u001b[38;5;46m♣\033[0m": 
        print("Vous êtes cachez sous un arbres")
        print("Bougez le avec ""b"", un fruit tombera peut etre")

#__________________________________________________________________________________________________________________________
    
def bougerArbre():
    Nourriture.verificationPositionArbre()

    if Variable.deplacement == "b":
        if Variable.deplacement == "b" and Variable.validationPositionFruit == True:
            
            if Variable.ancienCaractere == "\u001b[38;5;64mγ\033[0m" :
                print(" Oh ! Un ananas est tomber, appui sur R pour le ramasser")
                Nourriture.supprimerPositionArbreAnanas()
            elif Variable.ancienCaractere == "\u001b[38;5;76m↑\033[0m" :
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
    
    if Variable.deplacement == "r" :
        Nourriture.verificationPositionObjet()
        Utilities.verificationObjetSol()
        if Variable.deplacement == "r" and Variable.validationPositionSol == False :
            print("Il n'y a rien a ramasser")
        else : 
            print(Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]["Ramassage"])
            decision = input("Souhaitez vous mettre cette objet dans votre sac ? ").lower()
            while decision != "oui" and decision != "non" :
                decision = input("Veuillez choisir oui ou non ")
            if decision == "oui" :
                Utilities.nombreObjet()
                if Variable.compteurStock >= 10 :
                    print("Vous ne pouvez pas le prendre, votre sac à dos est pleins")
                else :
                    Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]['nombre'] += 1
                    print("Vous avez",Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]['nombre'],Variable.var_enregistrer['objetRamasser'])
                    Nourriture.supprimerObjet()
                    if Variable.var_enregistrer['objetRamasser'] not in Variable.listeFruit :
                        Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]["positionY"] = None
                        Variable.var_enregistrer['sac_a_dos'][Variable.var_enregistrer['objetRamasser']]["positionX"] = None


#__________________________________________________________________________________________________________________________


def displaySac():

    Utilities.clear()
    Variable.contenuInventaire = []
    def VisuelSac(contenuSac):
        for k in Variable.var_enregistrer['sac_a_dos']:
            if Variable.var_enregistrer['sac_a_dos'][k]['nombre'] > 0 :
                contenuSac.append(f"{Variable.var_enregistrer['sac_a_dos'][k]['nom']} * {Variable.var_enregistrer['sac_a_dos'][k]['nombre']}")
                Variable.contenuInventaire.append(Variable.var_enregistrer['sac_a_dos'][k]['nom'])
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
    print(f'|| Energie :{Variable.var_enregistrer["vitalite"]["Energie"]["Stock"]} || Hydratation :{Variable.var_enregistrer["vitalite"]["Hydratation"]["Stock"]} || Satiete :{Variable.var_enregistrer["vitalite"]["Satiete"]["Stock"]} ||\n')
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
        Utilities.clear()
        displaySac()
    elif Variable.lettre == "u" :
        Utilities.utiliserObjet()
        Utilities.clear()
        displaySac()


def die():
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
        Variable.var_enregistrer['resultatJeu'] = 'Perdu'
        Variable.var_enregistrer['date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        try :
            with open("Historique.json", "r", encoding="utf-8") as MyFile:
                Variable.dicHistorique = json.load(MyFile)
        except : 
            pass
        Variable.dicHistorique['compteurHistorique'] += 1
        Variable.dicHistorique[f'joueur{Variable.dicHistorique["compteurHistorique"]}'] = [Variable.var_enregistrer['nomAventurier'],
                            Variable.var_enregistrer['resultatJeu'],
                            Variable.var_enregistrer['nombreAction'],
                            Variable.var_enregistrer['nombreDeplacement'],
                            Variable.var_enregistrer['vitalite']['Energie']['Stock'],
                            Variable.var_enregistrer['vitalite']['Satiete']['Stock'],
                            Variable.var_enregistrer['vitalite']['Hydratation']['Stock'],
                            Variable.var_enregistrer['date']]
        # listeHistorique =[]
        # for k in 
        with open("Historique.json", "w", encoding="utf-8") as MyFile:
            json.dump(Variable.dicHistorique, MyFile, sort_keys = True, indent = 4, ensure_ascii = False)
        
        réponse = input("Veux tu rejouer ? ").lower()
        while réponse != "oui" and réponse != "non" :
            réponse = input("Oui ou non ? ") 
        if réponse == "non" :
            sys.exit (0)
        else :
            with open("VariableDebut.json", "r", encoding="utf-8") as MyFile:
                Variable.var_enregistrer = json.load(MyFile)
            Utilities.afterClear()
        
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



def start():
    print("  ____  _                                                               _              _           ")
    print(" |  _ \(_)                                          /\                 | |            (_)          ")
    print(" | |_) |_  ___ _ ____   _____ _ __  _   _  ___     /  \__   _____ _ __ | |_ _   _ _ __ _  ___ _ __ ")
    print(" |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| | | |/ _ \   / /\ \ \ / / _ \ '_ \| __| | | | '__| |/ _ \ '__|")
    print(" | |_) | |  __/ | | \ V /  __/ | | | |_| |  __/  / ____ \ V /  __/ | | | |_| |_| | |  | |  __/ |   ")
    print(" |____/|_|\___|_| |_|\_/ \___|_| |_|\__,_|\___| /_/    \_\_/ \___|_| |_|\__|\__,_|_|  |_|\___|_|  ")
    print()
    with open("Enregistrement.json", "r", encoding="utf-8") as MyFile:
        Variable.var_enregistrer = json.load(MyFile)
    if Variable.var_enregistrer['leave'] == True :
        validation = input("Voulez vous charger la dernier partie sauvegardée ? ")
        if validation == "oui" :
            print("Te revoilà ",Variable.var_enregistrer['nomAventurier'])
            time.sleep(1.5)
    else : 
        with open("VariableDebut.json", "r", encoding="utf-8") as MyFile:
            Variable.var_enregistrer = json.load(MyFile)     
        Variable.var_enregistrer['nomAventurier'] = input('Quel est ton nom ? ').capitalize()
    # while Variable.var_enregistrer['nomAventurier'].isalpha == True :
    #     Variable.var_enregistrer['nomAventurier'] = input('Seulement des lettres ').capitalize()