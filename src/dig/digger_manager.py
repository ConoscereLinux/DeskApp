"""Modulo che gestisce lo 'scavatore' delle cartelle."""

# Standard Import
import os
import hashlib


# Site-package Import

# Project Import
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm
#aggiungo index e metadata 
from meta import metadata_manager as mm
from index import indexer_manager as im

class DiggerManager():
    """Recupera i files nelle cartelle e manda i dati al DB.

    Scansiona periodicamente le cartelle selezionate, quando rileva un nuovo
    file o una modifica, recupera i  nuovi metadata usnado metadata_manager
    e manda al database con index_manager.



    Il percorso della cartella viene passato nelle configurazioni,
    in fase di sviluppo si prenderà una costante.
    

        TROVARE IL FILE, RECUPERARE PERCORSO COMPLETO E HASH MD5
        MANDARE PERCORSO ASSOLUTO E HASH AL METODO SEARCH DELL'INDEX
        IN BASE AL RITORNO DI SEARCH DECIDE SE INTERPELLARE IL METADATA (SE NON È NEL DB) OPPURE ANDARE OLTRE SE C'È GIÀ
        SE HO DOVUTO RECUPERARE IL METADATA, LO MANDO ALL'INDICE 
    """
    def __init__(self,
                 path: pm.PathManager, 
                 option: om.OptionManager,
                 config: cm.ConfigManager,
                 log: lm.LoggerManager):
        """

        Args:
        path: percorsi delle risorse dell'applicazione(per ora ignorato)
        option: opzioni definite dall'utente(per ora ignorato)
        config: indicazione del percorso da monitorare
        log: raccoglie errori ed eventi in fase runtime
        """

        self.__path = path
        self.__option = option
        self.__config = config
        self.__log = log

        self.__percorso = self.__config["percorso"]
        self.__reperti = {}

    
    def __dig(self):
        """Scansiona le cartelle per trovare nuovi files o le modifiche"""
        pass

    def __dig_dir():
        """Scansiona solo la cartella selezionata nel config"""
        pass

    
    
################### Test ######################################################
if __name__ == "__main__":

    ########################## Costanti per il debug ##########################
    CONFIG = {
        "percorso": "/home/pg/"
        }
    LOG = []

    OPTION = {
        "ricorsivo" : False
        }
    ###########################################################################

    test = DiggerManager(path=None, option=None, config=CONFIG, log=LOG)
    folder = test.get_reperti()
    
    print(folder)

    for files in folder:
        print(f"{files} -> {folder[files]} \n")

    
