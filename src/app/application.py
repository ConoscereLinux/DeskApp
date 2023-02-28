"""Modulo della vera e propria applicazione."""

# Standard Import
import multiprocessing as mp
from pathlib import Path
import sys

# Site-package Import
from PySide6 import QtWidgets, QtGui

# Project Import
from app import info as i
from dig import digger_manager as dm
from gui import main_window as mw
from index import indexer_manager as im
from meta import metadata_manager as mm

from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm

from util import resource as r

# Costante per il ritorno
APP_ERROR = 1

def main(argv: list) -> int:
    """La funzione main dell'applicazione, si occupa di caricare i componenti e
     lanciare l'interfaccia grafica.
     
     Args:
        argv (list): la lista dei parametri da riga di comando
         
    Returns:
        (int): il codice d'errore da restituire
    """
    
    # Costruisco il gestore dei percorsi
    path = pm.PathManager()
    
    # Costruisco il gestore delle opzioni da riga di comando
    option = om.OptionManager(argv, path)
    
    # Costruisco il gestore delle configurazioni
    config = cm.ConfigManager(path, option)
    
    # Costruisco il gestore dei log
    log = lm.LoggerManager(path, config)
    
    # Qualche output alla partenza dell'applicazione
    v = f"{i.__app_name__} v {i.__version__}"
    
    log.info("".join(("-" * 74, " START")))
    log.info(f"{i.__app_name__}")
    log.info(v)
    log.info(f"Running on '{sys.platform}' platform.")
    log.info(f"Processor thread count: {mp.cpu_count()}.")
    log.info("-" * 80)
    
    # Costruisco il gestore delle indicizzazioni
    indexer = im.IndexerManager(path, option, config, log)
    
    # Costruisco il gestore delle ricerche dei file
    digger = dm.DiggerManager(path, option, config, log)
    
    # TEMP --------------------------------------------------------------------
    # IMPLEMENTATO TEMPORANEMENTE DURANTE L'INTEGRAZIONE
    actual_path = Path(sys.path[0])
    source_folder = Path(actual_path.parent.parent,
                         'tests', 'data', 'source_folder')
    
    elaborated_folder = Path(actual_path.parent.parent,
                         'tests', 'data', 'elaborated_folder')
    
    db_folder = Path(actual_path.parent.parent,
                         'tests', 'data')
    
    meta = mm.MetadataManager(source_folder, elaborated_folder, db_folder)
    # -----------------------------------------------------------------END TEMP
    
    # Costruisco il gestore della raccolta dei metadati
    # meta = mm.MetadataManager(path, option, config, log)
    
    # Costruisco il gestore delle risorse
    resources = r.ResourceManager(path,
                                  option,
                                  config,
                                  log,
                                  indexer,
                                  digger,
                                  meta)
    
    app = QtWidgets.QApplication([])
    
    mwindow = mw.MainBase(resources, i.__app_name__)
    
    if(mwindow):
        result = app.exec_()
    
    else:
        result = 1
    
    sys.exit(result)