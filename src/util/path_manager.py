"""Utility per la gestione dei percorsi base dell'applicazioni."""

# Standard Import
import sys
import os.path

# Site-package Import

# Project Import


class PathManager():
    """Libreria che gestisce in maniera cntralizzata i percorsi."""
    
    CONFIG_FILE_NAME = "DeskApp.ini"
    
    def __init__(self):
        """Costruttore della Class."""
        
        self.__app_folder = sys.path[0]
        
    @property
    def config_path(self):
        return os.path.join(self.__app_folder, self.CONFIG_FILE_NAME)
        
        