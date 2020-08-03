import time
import Variable
import json

with open("Historique.json", "r", encoding="utf-8") as MyFile:
    Variable.dicHistorique = json.load(MyFile)
listeHistorique = []
for k in Variable.dicHistorique:
    listeHistorique.append(Variable.dicHistorique[k][7])

listeHistorique.sort()
print(Variable.dicHistorique)
for k in Variable.dicHistorique :
    if Variable.dicHistorique[k][7] == listeHistorique[0] :
        del Variable.dicHistorique[k]
        break

print(Variable.dicHistorique)
print (listeHistorique)