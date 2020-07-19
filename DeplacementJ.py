import Variable
import time
import os
import random
import Utilities
import message


def clear():
    os.system('cls') #pour Windows

def entrerDeplacement():

    Variable.nombre = 1
    entrer = input("Entrez une instruction  : ")
    if entrer != "" :
        Variable.deplacement = entrer[0]
    if len(entrer) > 1 :
        Variable.nombre = entrer[1:]
    listeDeplacement= ["z", "q","s","d","o","r","b","e", "c", "a", "f"]
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
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.positionJoueur[0] -= 1
                Utilities.vitalitéJoeur()
                clear()


    if Variable.deplacement == "s" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]+1][Variable.positionJoueur[1]]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.positionJoueur[0] += 1
                Utilities.vitalitéJoeur()
                clear()


    if Variable.deplacement == "d" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]+1]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.positionJoueur[1] += 1
                Utilities.vitalitéJoeur()
                clear()


    if Variable.deplacement == "q" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]-1]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.positionJoueur[1] -= 1
                Utilities.vitalitéJoeur()
                clear()
            
    if Variable.deplacement == "o":
        message.displaySac()

    if Variable.deplacement == "a" :
        Utilities.remplirBouteille()

    if Variable.deplacement == "e" :
        try:
            with open("Enregistrement", "w", encoding="utf-8") as MyFile:
                MyFile.write(f'JoueurY : {Variable.positionJoueur[0]}\n')
                MyFile.write(f'X : {Variable.positionJoueur[1]}\n')
                print("La partie a été sauvegardé")
                time.sleep(2.0)
        except :
            print("La partie n'a pas été sauvegardé")
            time.sleep(2.0)

    if Variable.deplacement == "c" :
        try:
            with open("Enregistrement", "r", encoding="utf-8") as MyFile:
                Line = MyFile.readline()[:-1]
                while Line:
                    Separator = Line.index(":")
                    DataName = Line[:Separator].strip()
                    DataValue = Line[Separator + 1:].strip()
                    if DataName == "JoueurY":
                        Variable.positionJoueur[0] = int(DataValue)
                    elif DataName == "X":
                        Variable.positionJoueur[1] = int(DataValue)
                    Line = MyFile.readline()
            # print(f"Position : {Variable.positionJoueur[0]} x {Variable.positionJoueur[1]}" )
        except: 
            print("On peut pas charger la sauvegarde")
            time.sleep(2.0)
    
    if Variable.deplacement == "f" :
        Utilities.sleep()
        # message.die()
