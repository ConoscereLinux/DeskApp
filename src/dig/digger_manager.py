"""Modulo che gestisce lo 'scavatore' delle cartelle."""

# Standard Import
import os
import time


# Site-package Import

# Project Import
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm

# Costanti per il debug
CONFIG = {
    "percorso": "/home/pg/"
}
LOG = []

class DiggerManager():
    """Recupera i files nelle cartelle e manda i dati al DB.


    Il percorso della cartella viene passato nelle configurazioni,
    in fase di sviluppo si prenderà una costante.

    Attributi:
        path: percorsi delle risorse dell'applicazione(per ora ignorato)
        option: opzioni definite dall'utente(per ora ignorato)
        config: indicazione del percorso da monitorare
        reperti: dict che conterrà il risultato di scavo
        log: raccoglie errori ed eventi in fase runtime
    """
    def __init__(self,
                 path: pm.PathManager, 
                 option: om.OptionManager,
                 config: cm.ConfigManager = CONFIG,
                 log: lm.LoggerManager = LOG):
        """
        Inizializza la variabile reperti (dictionary) in cui verranno salvati
        i dati recuperati.
        """
        self.__percorso = CONFIG["percorso"]
        self.__reperti = {}
        self.__log = LOG
        self.__path = path
        self.__option = option


    def __scavo(self):
        """ritorna un os.DirEntry per scorrere il contenuto della cartella
        
        Raises:
            FileNotFound: quando il percorso non è trovato nel sistema 
            NotADirectoryError: quando il percorso punta a un file
            Per il momento gli errori vengono buttati dentro una lista, saranno
            poi mandati al logger manager"""
        
        try:
            files = os.scandir(self.__percorso)
        except FileNotFoundError as err:
            self.__log.append(f"{err} il percorso non è presente nel sistema")
        except NotADirectoryError as err:
            self.__log.append(f"{err} Non è una cartella.")
        finally:
            print(self.__log)

        return files


    def __ordina(self):
        """Estrae e fomatta le info trovate con os.stat()

        Sfrutta il metodo scavo per generare l'iteratore, quindi cicla tutti
        gli elementi della cartella e inserisce i dati trovati in reperti
        La struttura in cui vengono inseriti i dati è del tipo:

        reperti = {'nome_file: ' : {'mode: ': 16893,
                                'ctime: ': 'Mon Mar 13 14:18:39 2023', 
                                'atime: ': 'Mon Mar 13 14:18:49 2023', 
                                'UserID': 1000, 'Dimensione': 36864, 
                                'tipo': 'cartella'}}
        """
        for entry in self.__scavo():

            st: os.stat_result = entry.stat()
            name , ext = os.path.splitext(entry.path)

            element = {
                "mode: " : st.st_mode,
                "ctime: " : time.ctime(st.st_ctime),
                "atime: " : time.ctime(st.st_atime),
                "UserID" : st.st_uid,
                "Dimensione" : st.st_size
                }

            #Per assegnare il tipo controllo se è una cartella altrimenti
            #assumo il tipo file leggendo l'estensione 
            if entry.is_dir():
                ext = "Cartella"
            elif entry.is_symlink():
                ext = "Symlink"
            elif entry.is_file():
                print(ext)
            element.update({"tipo" : ext })

            self.__reperti.update({name : element})



    def get_reperti(self) -> dict:
        self.__ordina()
        return (self.__reperti)
    
################### Test ######################################################
if __name__ == "__main__":

    test = DiggerManager(None, None, CONFIG, LOG)
    folder = test.get_reperti()
    
    print(folder)

    for files in folder:
        print(f"{files} -> {folder[files]} \n")
