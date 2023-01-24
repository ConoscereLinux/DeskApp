"""Modulo per la gestione delle configurazioni dell'applicazione."""

# Standard Import
import configparser

# Site-package Import

# Project Import
from util import option_manager as om


S_DEFAULT = 'common'
S_PATH = 'path'



class ConfigManager(configparser.ConfigParser):
    """Classe per gestire le configurazioni iniziali dell'applicazione."""
    
    def __init__(self, option: om.OptionManager):
        """
        Il costruttore della classe.
        
        Args:
            option (OptionManager): il gestore delle configurazionida riga di
                comando.
        """
        super().__init__(
            interpolation = configparser.ExtendedInterpolation,
            default_sction = S_DEFAULT)
        
        