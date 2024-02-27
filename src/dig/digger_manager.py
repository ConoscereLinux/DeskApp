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
    """Recupera i file nelle cartelle.

    Apre i file nelle cartelle selezionate,
    interpella metadata_manager per ottenere i metadati del file
    quindi manda hash e metadata al database con index_manager.



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

        if not os.path.isdir(self.__dirPath):
            self.__log.error(f"{self.__dirPath} non è un percorso di una cartella del sistema")

    def scan(self, path=None) -> None:
        """scansiona il percorso passato come parametro o quello nel config"""
        if path is None:
            path = self.__dirPath

        with os.scandir(path) as el:
            for i in el:

                if i.is_file():
                    try:
                        open(i, 'r')
                        self.__log.info(f"File esaminato {i.path}")

                        # calcolo dell'hash
                        h = self.__resolve_checksum(i.path)
                        self.__log.info(f"Hash: {h}")

                        # recupera i metadati
                        m = self.__meta.scan_file(i.path)
                        self.__log.info(f"Metadata: {m}")

                        # aggiorna o inserisce in index
                        self.__index.update_index(i.path, str(h), m)

                    except PermissionError:
                        self.__log.error(f"Permesso negato in lettura per il file {i.path}")


                # chiamata ricorsiva per le cartelle
                elif i.is_dir():
                    self.__log.info(f"Cartella: {i.path}")
                    self.scan(path=i.path)

    def __resolve_checksum(self, path) -> bytes:
        """calcola il checksum del file al percorso indicato
        
        da implementare la possibilità di usare altro algoritmo di hashing

        Return:
            binario che rappresenta il checksum (MD5)
        """
        try:
            with open(path, 'rb') as file:
                file_hash = md5(file.read())
                self.__log.info(f'updated md5 {file_hash.digest()}')
                return file_hash.digest()
        except Exception as err:
            self.__log.error(err)
