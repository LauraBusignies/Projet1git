import Display
import Utilities
import Variable
import DeplacementJ
import time

if __name__ == "__main__":



    while Variable.positionJoueur[0] != 0 :
        Display.map1()
        DeplacementJ.entrerDeplacement()
        DeplacementJ.ZQSD()