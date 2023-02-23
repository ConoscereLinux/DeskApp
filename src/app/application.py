"""Modulo della vera e propria applicazione."""

# Standard Import

# Site-package Import

# Project Import
from util import config_manager as cm
from util import option_manager as om

def main(argv: list) -> int:
    """La funzione main dell'applicazione, si occupa di caricare i componenti e
     lanciare l'interfaccia grafica.
     
     Args:
        argv (list): la lista dei parametri da riga di comando
         
    Returns:
        (int): il codice d'errore da restituire
    """
    
    option = om.OptionManager()
    
    config = cm.ConfigManager(option)
    
    
    
    # TODO: Sostituire con l'apertura dell'interfaccia grafica
    print("Hallo world!")
    print(argv)
    
    return 0