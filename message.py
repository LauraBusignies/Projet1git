import Variable
import random
import Utilities
import Display
import Nourriture
import sys


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
            print(Variable.sac_a_dos[Variable.objetRamasser]["Ramassage"])
            decision = input("Souhaitez vous mettre cette objet dans votre sac ? ").lower()
            while decision != "oui" and decision != "non" :
                decision = input("Veuillez choisir oui ou non ")
            if decision == "oui" :
                Utilities.nombreObjet()
                if Variable.compteurStock >= 10 :
                    print("Vous ne pouvez pas le prendre, votre sac à dos est pleins")
                else :
                    Variable.sac_a_dos[Variable.objetRamasser]['nombre'] += 1
                    print(f'Vous avez {Variable.sac_a_dos[Variable.objetRamasser]["nombre"]} {Variable.objetRamasser}' )
                    Nourriture.supprimerObjet()
                    if Variable.objetRamasser not in Variable.listeFruit :
                        Variable.sac_a_dos[Variable.objetRamasser]["positionY"] = None
                        Variable.sac_a_dos[Variable.objetRamasser]["positionX"] = None


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
    print(f'|| Energie :{Variable.Vitalite["Energie"]["Stock"]} || Hydratation :{Variable.Vitalite["Hydratation"]["Stock"]} || Satiete :{Variable.Vitalite["Satiete"]["Stock"]} ||\n')
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
    if Variable.Vitalite["Energie"]["Stock"] < 0 or Variable.Vitalite["Hydratation"]["Stock"] < 0 or Variable.Vitalite["Satiete"]["Stock"] < 0 :
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
        réponse = input("Veux tu rejouer ?").lower()
        while réponse != "oui" and réponse != "non" :
            réponse = input("Oui ou non ? ")
        if réponse == "non" :
            sys.exit (0)
        else :
            Variable.positionJoueur[0] = 25
            Variable.positionJoueur[1] = 75
            Variable.Vitalite["Energie"]["Stock"] = 100
            Variable.Vitalite["Hydratation"]["Stock"] = 100
            Variable.Vitalite["Satiete"]["Stock"] = 100
            Display.map1()
        
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



