"""
Modulo della vera e propria applicazione e che contiene la funzione 'main'.

Nella funzione 'main', vengono inzializzati i componenti principali
dell'applicazione e viee lanciata l'interfaccia grafica.
"""

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
    # log = lm.LoggerManager(path, config)
    log = lm.LoggerManager("DeskApp")
    
    # Qualche output alla partenza dell'applicazione
    v = f"{i.APP_NAME} v {i.VERSION}"
    
    log.info("".join(("-" * 74, " START")))
    log.info(f"{i.APP_NAME}")
    log.info(v)
    log.info(f"Running on '{sys.platform}' platform.")
    log.info(f"Processor thread count: {mp.cpu_count()}.")
    log.info("-" * 80)
    
    # Costruisco il gestore delle indicizzazioni
    indexer = im.IndexerManager(path, option, config, log)

    # Costruisco il gestore dei metadati    
    meta = mm.MetadataManager(path, option, config, log)
    
    # Costruisco il gestore delle ricerche dei file
    digger = dm.DiggerManager(path, option, config, log, indexer, meta)
    
    # Costruisco il gestore delle risorse. Questo è un oggetto che contiene i
    # riferimenti a tutti i componenti principali dell'applicazione
    resources = r.ResourceManager(path,
                                  option,
                                  config,
                                  log,
                                  indexer,
                                  digger,
                                  meta)
    
    # QApplication implementa QGuiApplication con alcune funzionalità necessarie
    # per le applicazioni basate su QWidget. Gestisce l'inizializzazione e la
    # finalizzazione specifiche del widget.
    # Ci può essere una ed una sola QApplication, indipendentemente dal numero
    # di finestre.
    app = QtWidgets.QApplication([])
    
    # Creo la finestra principale
    mwindow = mw.MainBase(resources, i.APP_NAME)
    
    # Se la creazione è andata a buon fine
    if(mwindow):
        # Mando in esecuzione il processo principale dell'applicazione
        result = app.exec_()
    
    else:
        # Mi segno che c'è stato un erroe
        result = APP_ERROR
    
    # chiudo il programma, restituendo l'eventuale codice di errore
    sys.exit(result)