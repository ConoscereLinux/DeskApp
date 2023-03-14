"""Modulo per la gestione delle opzioni da riga di comando."""

# Standard Import
import sys
import os

# Site-package Import

# Project Import
from util import path_manager as pm


class OptionManager():
    def __init__(self,
                 argv: lista,
                 path: pm.PathManager):
        self.key = lista
        
        """
        Costruttore con gia definito un prototipo dei parametri necessari.
        """
        
    def view(self):
        os.chdir("Source")
        for cartelle, sottocartelle, files in os.walk(os.getcwd()):
            for file in files:
                if self.key[1] in file:
                    print(file)


if __name__ == "__main__":
    objExt = OptionManager(sys.argv)
    objExt.view()
