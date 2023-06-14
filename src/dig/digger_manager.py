"""Modulo che gestisce lo 'scavatore' delle cartelle."""

# Standard Import
import os
from hashlib import md5



# Site-package Import

# Project Import
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm
from meta import metadata_manager as mm
from index import indexer_manager as im

class DiggerManager():
    """Recupera i files nelle cartelle e manda i dati al DB.

    Scansiona periodicamente le cartelle selezionate, quando rileva un nuovo
    file o una modifica, recupera i  nuovi metadata usnado metadata_manager
    e manda al database con index_manager.



    Il percorso della cartella viene passato nelle configurazioni,
    in fase di sviluppo si prenderà una costante."""

    def __init__(self,
                 path: pm.PathManager, 
                 option: om.OptionManager,
                 config: cm.ConfigManager,
                 log: lm.LoggerManager,
                 index: im.IndexerManager,
                 meta: mm.MetadataManager):
        
        """

        Args:
            path: percorsi delle risorse dell'applicazione(per ora ignorato)
            option: opzioni definite dall'utente(per ora ignorato)
            config: indicazione del percorso da monitorare
            log: raccoglie errori ed eventi in fase runtime
            index: collegamento e funzioni per il database
            meta: recupera i metadati dei files passati 
        """

        self.__path = path
        self.__option = option
        self.__config = config
        self.__log = log
        self.__index = index
        self.__meta = meta
        
        self.__dirPath = self.__config["path"]["source_folder"]
        self.__files = {}
    

    def __scan(self) -> None:
        """invoca os.scandir 
        torna l'iteratore"""
        with os.scandir(self.__dirPath) as dir:
            for item in dir:
                print(item) #mandare al log
                self.__files[f'{item.name}'] = item.path

    def __resolveMd5():
        pass

    def __checkIndex():
        """richiama il servizio indexer per controllare se il file è già
        catalogato e aggiornato sul database"""
        pass

    def update():
        """Public method, richiama gli altri metodi in successione."""
        pass




############################### Test ##########################################

def main():
    """TEST"""
    test = DiggerManager(path=None, option=None, config=CONFIG, log=LOG)
    folder = test.get_reperti()
    
    print(folder)

    for files in folder:
        print(f"{files} -> {folder[files]} \n")

if __name__ == "__main__":
    main()

###############################################################################