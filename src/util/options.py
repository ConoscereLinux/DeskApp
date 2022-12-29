# Modulo per effettuare parser a riga di comando, formato altamente embrionale e alquanto incompleto

# Standard Import
import sys

# Site-package Import
import os

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
        os.chdir("Source") # ci si sposta nella cartella 'Source'
        for cartelle, sottocartelle, files in os.walk(os.getcwd()): """ funzione che ottiene la lista delle cartelle, sottocartelle e files 
                                                                        presenti nel filesystem""" 
        for file in files: #scorrimento della lista dei files per confronto con estensione richiesta
            if file.endswith(self.extension): """ questa funzione rende vera la condizione solo per la stampa a video 
                                                  dei file con estensione che corrisponde a self.extension""" 
            print(file) #stampa lista file con estensione richiesta
            
        # riga commentata creata per mie esigenze che non deve essere presa in considerazione
        # print(os.listdir()) # visualizza i file e cartelle nella directory corrente
        
#creazione dell'istanza della classe e chiamata del metodo view
req = input("Inserisci l'estensione dei file da ricercare(.ext) ")
objExt = Request(req) #creazione di un istanza della classe Request
objExt.view() # chiamata del metodo di visualizzazione dei file nel filesystem