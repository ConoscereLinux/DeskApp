# Modulo per effettuare parser a riga di comando, formato altamente embrionale e alquanto incompleto

# Standard Import
import sys

# Site-package Import
import os
# import re

# Project Import
# from app import application as a

"""Creo una classe Request dove l'utente indica il criterio di ricerca
in base all'estensione dei file presenti in una cartella"""
class Request:
    def __init__(self, word): 
        self.word = word
        self.sizeWord = len(self.word)

    """definizione di un metodo che visualizza i file presenti nella directory"""
    def view(self):
        # print(os.listdir("Source"))
        os.chdir("Source") # ci si sposta nella cartella 'Source'
        for cartelle, sottocartelle, files in os.walk(os.getcwd()):
            # funzione che ottiene la lista delle cartelle, sottocartelle e files 
            # presenti nel filesystem
            for file in files: #scorrimento della lista dei files per confronto con estensione richiesta
                # print("confronto ",self.extension == file[:-4])
                # if file.endswith(self.word): 
                   # print(file)   
                if self.word in file: 
                    print(file)
#creazione dell'istanza della classe e chiamata del metodo view
req = input("Inserisci l'estensione dei file da ricercare(.ext) ")
objExt = Request(req) #creazione di un istanza della classe Request
objExt.view() # chiamata del metodo di visualizzazione dei file nel filesystem
