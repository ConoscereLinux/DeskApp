"""Quello che serve per l'indicizazione dei file con relativi metadati."""

# Standard Import

# Site-package Import

# Project Import
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm


class IndexerManager():
    def __init__(self,
                 path: pm.PathManager,
                 option: om.OptionManager,
                 config: cm.ConfigManager,
                 log: lm.LoggerManager):
        """
        Costruttore con già definito un prototipo dei parametri necessari.
        """
        self.__path = path
        self.__option = option
        self.__config = config
        self.__log = log

    def update_index(self,
                     file_path: str,
                     content_hash: str,
                     meta_data: dict,) -> None:
        """
        Si occupa di registrare nel db il file con i suoi metadati.
        
        Args:
            file_path: il percorso del file da indicizzare
            content_hash: l'hash calcolato del contenuto del file
            meta_data: il dizionario di metadati del file
            
        """
        
        self.__log.info(file_path)
    
    def is_already_indexed(self, file_path: str) -> bool:
        """
        Cerca il 'file_path' nel database e restituisce se l'ha trovato.
        """
        
        return False