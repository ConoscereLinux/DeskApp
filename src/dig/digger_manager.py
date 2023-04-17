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
        
        self.__dirPath = self.__config["percorso"]
        self.__files = {}
    
    #Decorators Approach 
    ##non credo sia l'approccio migliore per gestire la funzione scan dentro alla classe
    ##perché devo passare un parametro che ho immagazzinato nelle proprietà della stessa
    '''def digger(self,func_scan):
        def check():
            #controlla e raccoglie gli eventuali errori di scan
            try:
                func_scan()
            except FileNotFoundError as err:
                self.__log.append(err)
                print(err)
            except NotADirectoryError as err:
                self.__log.append(err)
                print(err)
        return check

    @digger
    def scan(self, p: str):
        """usa scandir per vedere i files nelle cartelle
        
        Args:
            p: sarebbe il percorso, si trova invocando 

        La funzione passa dal decoratore digger per gestire la chiamata con try
        e loggare eventuali errori.
        Inoltre la funzione esegue una chiamata ricorsiva se c'è il flag nelle
        option."""
        with os.scandir(p) as entry:
            for e in entry:
                if e.is_dir():
                    print(f"Chiamata a self.already_known per controllare se {e.name} è già nel DB")
                    #controllo dalle option se l'utente ha selezionato "ricorsivo"
                    if self.__option["ricorsivo"]: self.scan(self, e.path)
                else:
                    print(f"Chiamata a self.already_known per controllare se {e.name} è già nel DB")
'''
    def __scan(self) -> os.DirEntry:
        """invoca os.scandir 
        torna l'iteratore"""
        pass
    
    def __dig(self, entry:os.DirEntry):
        """Prende il risultato di scan 
        """
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

    
