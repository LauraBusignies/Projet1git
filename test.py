import time
import Variable
import json

with open("Historique.json", "r", encoding="utf-8") as MyFile:
    Variable.dicHistorique = json.load(MyFile)

listeHistorique = []
for k in Variable.dicHistorique :
    # listeHistorique.append(Variable.dicHistorique[k]['date'])
    print(k)
print(listeHistorique)