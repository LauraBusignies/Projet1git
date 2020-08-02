import Variable
import time
import os
import random
import Utilities
import message


def clear():
    os.system('cls') #pour Windows

def entrerDeplacement():

    entrer = input("Entrez une instruction  : ")
    if entrer != "" :
        Variable.deplacement = entrer[0]

    listeDeplacement= ["z", "q","s","d","o","r","b","e", "c", "a", "f"]
    while Variable.deplacement not in listeDeplacement or len(entrer) > 1:
            print("Entrez seulement une lettre")
            entrer = (input("Entrez une instruction : ")).lower()

            if entrer != "" :
                Variable.deplacement = entrer[0]


            
def ZQSD ():
    if Variable.deplacement == "z" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]-1][Variable.positionJoueur[1]]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.positionJoueur[0] -= 1
                Utilities.VitaliteJoeur()
                clear()


    if Variable.deplacement == "s" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]+1][Variable.positionJoueur[1]]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.positionJoueur[0] += 1
                Utilities.VitaliteJoeur()
                clear()


    if Variable.deplacement == "d" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]+1]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.positionJoueur[1] += 1
                Utilities.VitaliteJoeur()
                clear()


    if Variable.deplacement == "q" :
        prevision = Variable.liste_Map[Variable.positionJoueur[0]][Variable.positionJoueur[1]-1]
        if prevision in Variable.color_character :
            if Variable.color_character[prevision]["CanWalk"] == False :
                print (Variable.color_character[prevision]["Erreur"])
                time.sleep(1.5)
            else :
                Variable.positionJoueur[1] -= 1
                Utilities.VitaliteJoeur()
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
