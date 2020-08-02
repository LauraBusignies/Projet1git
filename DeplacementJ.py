import Variable
import time
import os
import random
import Utilities
import message
import json
import sys

def clear():
    os.system('cls') #pour Windows

def entrerDeplacement():

    entrer = input("Entrez une instruction  : ")
    if entrer != "" :
        Variable.deplacement = entrer

    listeDeplacement= ["z", "q","s","d","i","r","b","l", "c", "a", "f", "tricheur"]
    while Variable.deplacement not in listeDeplacement:
            print("Entrez seulement une lettre")
            entrer = (input("Entrez une instruction : ")).lower()

            if entrer != "" :
                Variable.deplacement = entrer


            
def ZQSD ():
    if Variable.deplacement == "z" :
        prevision = Variable.liste_Map[Variable.var_enregistrer['positionJoueur'][0]-1][Variable.var_enregistrer['positionJoueur'][1]]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.var_enregistrer['positionJoueur'][0] -= 1
                Utilities.vitaliteJoueur()
                clear()
                Variable.var_enregistrer['nombreDeplacement'] += 1


    if Variable.deplacement == "s" :
        prevision = Variable.liste_Map[Variable.var_enregistrer['positionJoueur'][0]+1][Variable.var_enregistrer['positionJoueur'][1]]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.var_enregistrer['positionJoueur'][0] += 1
                Utilities.vitaliteJoueur()
                clear()
                Variable.var_enregistrer['nombreDeplacement'] += 1


    if Variable.deplacement == "d" :
        prevision = Variable.liste_Map[Variable.var_enregistrer['positionJoueur'][0]][Variable.var_enregistrer['positionJoueur'][1]+1]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.var_enregistrer['positionJoueur'][1] += 1
                Utilities.vitaliteJoueur()
                clear()
                Variable.var_enregistrer['nombreDeplacement'] += 1


    if Variable.deplacement == "q" :
        prevision = Variable.liste_Map[Variable.var_enregistrer['positionJoueur'][0]][Variable.var_enregistrer['positionJoueur'][1]-1]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.var_enregistrer['positionJoueur'][1] -= 1
                Utilities.vitaliteJoueur()
                clear()
                Variable.var_enregistrer['nombreDeplacement'] += 1
            
    if Variable.deplacement == "i":
        message.displaySac()
        Variable.var_enregistrer['nombreAction'] += 1

    if Variable.deplacement == "a" :
        Utilities.remplirBouteille()
        Variable.var_enregistrer['nombreAction'] += 1

    if Variable.deplacement == "l" :
        try:
            Variable.var_enregistrer['leave'] = True
            with open("Enregistrement.json", "w", encoding="utf-8") as MyFile:
                json.dump(Variable.var_enregistrer, MyFile, sort_keys = True, indent = 4, ensure_ascii = False)
                print("La partie a été sauvegardée")
                time.sleep(2.0)
                
        except :
            print("La partie n'a pas été sauvegardée")
            time.sleep(2.0)
        Variable.var_enregistrer['nombreAction'] += 1
        sys.exit(0)

    
    if Variable.deplacement == "f" :
        Utilities.sleep()
        Variable.var_enregistrer['nombreAction'] += 1
    

    if Variable.deplacement == "tricheur":
        Variable.tricheur = True