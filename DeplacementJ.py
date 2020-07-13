import Variable
import time
import os
import random
import Utilities


def clear():
    os.system('cls') #pour Windows

def entrerDeplacement():

    Variable.nombre = 1
    entrer = input("Entrez une instruction  : ")
    if entrer != "" :
        Variable.deplacement = entrer[0]
    if len(entrer) > 1 :
        Variable.nombre = entrer[1:]
    listeDeplacement= ["z", "q","s","d","o","r","b"]
    while Variable.deplacement not in listeDeplacement :
            print("Veuillez saisir une lettre entre Z, Q , S, D. \n Z pour monter \n S pour descendre \n D pour aller a droite \n Q pour aller a gauche")
            entrer = (input("Entrez une instruction : ")).lower()
            print()

            if entrer != "" :
                Variable.deplacement = entrer[0]
            if len(entrer) > 1 :
                Variable.nombre = entrer[1:]

            
def ZQSD ():
    if Variable.deplacement == "z" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]-1][Variable.positionJoueur[1]]
        if Variable.liste_Map[Variable.positionJoueur[0]-1][Variable.positionJoueur[1]] in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(2.0)
            else :
                Variable.positionJoueur[0] -= 1
                clear()


    if Variable.deplacement == "s" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]+1][Variable.positionJoueur[1]]
        if Variable.liste_Map[Variable.positionJoueur[0]+1][Variable.positionJoueur[1]] in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(2.0)
            else :
                Variable.positionJoueur[0] += 1
                clear()


    if Variable.deplacement == "d" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]+1]
        if Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]+1] in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(2.0)
            else :
                Variable.positionJoueur[1] += 1
                clear()


    if Variable.deplacement == "q" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]-1]
        if Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]-1] in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(2.0)
            else :
                Variable.positionJoueur[1] -= 1
                clear()
    if Variable.deplacement == "o":
        Utilities.displaySac()

