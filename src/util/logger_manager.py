"""Modulo per la gestione dei log dell'applicazione."""

# Standard Import

# Site-package Import

# Project Import
from util import config_manager as cm
from util import path_manager as pm


class LoggerManager():
    def __init__(self,
                 path: pm.PathManager,
                 config: cm.ConfigManager):
        """
        Costruttore con già definito un prototipo dei parametri necessari.
        """
        pass
    
    def info(self, text):
        """Funzione temporanea per far funionare il programma."""
        print(text)