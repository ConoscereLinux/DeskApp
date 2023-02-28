"""Una raccolta di costanti con le informazioni dell'applicazione."""

# Standard Import
from re import finditer

# Site-package Import

# Project Import


def camel_case_split(camel_text):
    """
    Divide il testo in ingresso nei punti in cui trova una maiuscola.
    """
    
    matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', camel_text)
    return " ".join([m.group(0) for m in matches])


__company_name_folder__ = "ConoscereLinux"
__app_name_folder__ = "DeskApp"
__version__ = "0.0.1"
__company_name__ = camel_case_split(__company_name_folder__)
__app_description__ ="Utility per la gestione e la indicizzazione di file."
__copyright__ = "ConoscereLinux. Tutti i diritti sono riservati."
__app_name__ = camel_case_split(__app_name_folder__)
