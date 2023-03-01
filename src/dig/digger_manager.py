"""Modulo che gestiglie lo 'scavatore' delle cartelle."""

# Standard Import

# Site-package Import

# Project Import
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm


class DiggerManager():
    def __init__(self,
                 path: pm.PathManager, 
                 option: om.OptionManager,
                 config: cm.ConfigManager,
                 log: lm.LoggerManager):
        """
        Costruttore con già definito un prototipo dei parametri necessari.
        """
        pass
