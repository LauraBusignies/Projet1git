import Display
import Utilities
import Variable
import DeplacementJ
import time
import FonctionPrint



if __name__ == "__main__":


    FonctionPrint.start()
    while Variable.var_enregistrer['positionJoueur'][0] != 0 :

        Utilities.clear()
        Display.map1()
        DeplacementJ.entrerDeplacement()
        DeplacementJ.ZQSD()
