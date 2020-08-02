import time
import Variable
# Obtenir l'heure et la date locale
now = time.localtime(time.time())
listeHeure = ['2019-08-01 21:24:33', '2020-08-01 13:24:33', '2020-03-01 21:24:33', '2022-08-01 21:24:33']
now = time.localtime(time.time())
listeHeure.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
dictionnaire = {}
compteur = 1
dictionnaire[f'joueur{compteur}'] = [Variable.var_enregistrer['nomAventurier'],
                                    Variable.var_enregistrer['resultatJeu'],
                                    Variable.var_enregistrer['nombreAction'],
                                    Variable.var_enregistrer['nombreDeplacement'],
                                    Variable.var_enregistrer['vitalite']['Energie']['Stock'],
                                    Variable.var_enregistrer['vitalite']['Satiete']['Stock'],
                                    Variable.var_enregistrer['vitalite']['Hydratation']['Stock'],
                                    Variable.var_enregistrer['date']]

dictionnaire[f'joueur2'] = [Variable.var_enregistrer['nomAventurier'],
                                    Variable.var_enregistrer['resultatJeu'],
                                    Variable.var_enregistrer['nombreAction'],
                                    Variable.var_enregistrer['nombreDeplacement'],
                                    Variable.var_enregistrer['vitalite']['Energie']['Stock'],
                                    Variable.var_enregistrer['vitalite']['Satiete']['Stock'],
                                    Variable.var_enregistrer['vitalite']['Hydratation']['Stock'],
                                    Variable.var_enregistrer['date']]

dictionnaire[f'joueur3'] = [Variable.var_enregistrer['nomAventurier'],
                                    Variable.var_enregistrer['resultatJeu'],
                                    Variable.var_enregistrer['nombreAction'],
                                    Variable.var_enregistrer['nombreDeplacement'],
                                    Variable.var_enregistrer['vitalite']['Energie']['Stock'],
                                    Variable.var_enregistrer['vitalite']['Satiete']['Stock'],
                                    Variable.var_enregistrer['vitalite']['Hydratation']['Stock'],
                                    Variable.var_enregistrer['date']]

for k in dictionnaire :
    print(k)
print(dictionnaire)
listeHeure.sort()
print(listeHeure)