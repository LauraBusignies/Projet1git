import Variable
import time
import os
import random
import message

def clear():
    os.system('cls') #pour Windows

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

