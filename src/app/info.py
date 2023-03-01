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


COMPANY_NAME_FOLDER = "ConoscereLinux"
APP_NAME_FOLDER = "DeskApp"
VERSION = "0.0.1"
COMPANY_NAME = camel_case_split(COMPANY_NAME_FOLDER)
APP_DESCRIPTION ="Utility per la gestione e la indicizzazione di file."
COPYRIGHT = "ConoscereLinux. Tutti i diritti sono riservati."
APP_NAME = camel_case_split(APP_NAME_FOLDER)
