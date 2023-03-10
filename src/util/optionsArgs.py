# Modulo per effettuare parser a riga di comando, formato altamente embrionale e alquanto incompleto

# Standard Import
import sys

# Site-package Import
import os
import argparse

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
        os.chdir("Source") # ci si sposta nella cartella 'Source'
        for cartelle, sottocartelle, files in os.walk(os.getcwd()):
            # funzione che ottiene la lista delle cartelle, sottocartelle e files 
            # presenti nel filesystem
            for file in files: #scorrimento della lista dei files per confronto con estensione richies 
                if self.word in file: 
                    print(file)
#creazione dell'istanza della classe e chiamata del metodo view
parser = argparse.ArgumentParser(description='funzione che permette la ricerca dei file a riga di comando')                    
parser.add_argument("req", type=str, help="inserisci una stringa per cercare il file")
args = parser.parse_args()
# req = input("Inserisci l'estensione dei file da ricercare(.ext) ")
objExt = Request(args.req) #creazione di un istanza della classe Request
objExt.view() # chiamata del metodo di visualizzazione dei file nel filesystem
