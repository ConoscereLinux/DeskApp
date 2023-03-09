"""Modulo per la gestione delle opzioni da riga di comando."""

# Standard Import
import sys
import os

# Site-package Import

# Project Import

class OptionManager():
    def __init__ (self, chiave):
        self.key = chiave
    
    """definizione di un metodo che visualizza i file presenti nella directory"""
    def view(self):
        os.chdir("Source") # ci si sposta nella cartella 'Source'
        # funzione che ottiene la lista delle cartelle, sottocartelle e files 
        # presenti nel filesystem
        for cartelle, sottocartelle, files in os.walk(os.getcwd()):
            for file in files: #scorrimento della lista dei files per confronto con estensione richiesta
                # poiché self.key è una lista e non può essere inserita come confronto 
                # si utilizza la seconda stringa che è la stringa da ricercare
                if self.key[1] in file: 
                    print(file)

# creazione dell'istanza della classe e chiamata del metodo view
if(__name__ == "__main__"):
    objExt = OptionManager(sys.argv) #creazione di un istanza della classe Request
    objExt.view() # chiamata del metodo di visualizzazione dei file nel filesystem
