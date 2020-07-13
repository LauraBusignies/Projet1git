import Variable
import os
import Display
import random

def clear():
    os.system('cls') #pour Windows

def afterClear():
    clear()
    Display.map1()

# Definir l

    
# Capacité du Sac à dos 
def nombreObjet():
    Variable.compteurStock = 0
    for key in Variable.sac_a_dos:
        if Variable.sac_a_dos[key]["nombre"] > 0 :
            Variable.compteurStock += Variable.sac_a_dos[key]["nombre"]

#__________________________________________________________________________________________________________________________

def displaySac():

    clear()
    def VisuelSac(contenuSac):
        for k in Variable.sac_a_dos:
            if Variable.sac_a_dos[k]['nombre'] > 0 :
                contenuSac.append(f"{Variable.sac_a_dos[k]['nom']} * {Variable.sac_a_dos[k]['nombre']}")
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

    action =input("Que veux tu faire ? Sortir du sac -> L / Utiliser un objet de ton sac -> U + NomObjet / Jetter un objet de ton sac -> D + objet").lower()
    verification = False
    while verification == False : 
        if len(action) > 1 and action[0] == "d" :
            action = list(action)
            lettre = action[0]
            fruit = "".join(action[2:]).capitalize()
            
    print(lettre)
    print(fruit)
