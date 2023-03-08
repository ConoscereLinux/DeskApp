"""Modulo per la gestione delle opzioni da riga di comando."""

# Standard Import
import sys
import os

# Site-package Import

# Project Import
import argparse

class OptionManager():
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
# implementazione della funzionalità passaggio parametri con la funzione 'argparse'
parser = argparse.ArgumentParser(description='funzione che permette la ricerca dei file a riga di comando')                    
parser.add_argument("req", type=str, help="inserisci una stringa per cercare il file")
args = parser.parse_args()
# creazione dell'istanza della classe e chiamata del metodo view
# req = input("Inserisci l'estensione dei file da ricercare(.ext) ")
if(__name__ == "__main__"):
    objExt = OptionManager(args.req) #creazione di un istanza della classe Request
    objExt.view() # chiamata del metodo di visualizzazione dei file nel filesystem
