"""Modulo per parsare a riga di comando"""


# Standard Import
import sys

# Site-package Import
import os
import shutil

# Project Import
# from app import application as a

"""Creo una classe Request dove l'utente indica il criterio di ricerca
in base all'estensione dei file presenti in una cartella"""

class Request:
    def __init__(self, ext): 
        self.extension = ext

    """definizione di un metodo che visualizza i file presenti nella directory"""
    def view(self):
        os.getcwd() # ci si posiziona nella directory corrente
        print(os.listdir()) # visualizza i file e cartelle nella directory corrente
        
#creazione dell'istanza della classe e chiamata del metodo view
objExt = Request(req)
objExt.view()





            

      
