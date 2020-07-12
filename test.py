import Variable
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

action =input("Que veux tu faire ? Sortir du sac -> L / Utiliser un objet de ton sac -> NomObjet / Jetter un objet de ton sac -> D objet")
    







