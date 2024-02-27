"""Modulo per la gestione dei metadati di un file chiamato PHOTO fornito da classe digger_manager.py"""

# Standard Import
import os
from pathlib import Path

# Site-package Import
from exif import Image  #libreria python per lettura metadati immagini

# Project Import
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm



class MetadataManager():
    """Classe che estrae i metadati di un file"""

    def __init__(self,
                 path: pm.PathManager,
                 option: om.OptionManager,
                 config: cm.ConfigManager,
                 log: lm.LoggerManager):
        """
        Costruttore con già definito un prototipo dei parametri necessari.
        """
        self.__path = path
        self.__option = option
        self.__config = config
        self.__log = log

    def scan_file(self, photo):

        self.__metadati = {}  # inizializzo dizionario metadati


        # leggere file PHOTO inserito, per test, dentro a \src\meta poi verrà passato da digger_manager.py
        with open(photo, 'rb') as img_file:
            img = Image(img_file)

            if img.has_exif:
                try:
                    # Larghezza
                    self.__metadati["Larghezza"] = img.get("pixel_x_dimension")
        
                    # altezza
                    self.__metadati["Altezza"] = img.get("pixel_y_dimension")
        
                    # risoluzione
                    self.__metadati["Risoluzione"] = img.get("x_resolution")
        
                    # Make of device which captured image
                    self.__metadati["Make"] = img.get("make")
        
                    # Model of device which captured image
                    self.__metadati["Model"] = img.get("model")
        
                    # Software involved in uploading and digitizing image
                    self.__metadati["Software"] = img.get("software")
        
                    # Name of photographer who took the image
                    self.__metadati["Artist"] = img.get("artist")
        
                    # Original datetime that image was taken (photographed)
                    self.__metadati["DateTime (Original)"] = img.get("datetime_original")
        
                    # Details of flash function
                    self.__metadati["Flash Details"] = img.get("flash")
        
                    # getting the Longitude and latitude data
                    self.__metadati["Longitude data"] = img.get("gps_longitude")
                    self.__metadati["latitude data"] = img.get("gps_latitud")
        
                    # getting the Longitude  and latitude Reference data is also very important when converting the Decimal degrees formen
                    self.__metadati["Longitude data reference"] = img.get("gps_longitude_ref")
                    self.__metadati["latitude data reference"] = img.get("gps_latitude_ref")
        
                    #dimensione
                    self.__metadati["Dimensione file (in byte)"] = int(os.stat(photo).st_size)
        
                    print(list(self.__metadati.items()))   #lasciato un print per fare vedere nel dizionario cosa sarà scritto
                    
                except KeyError:
                    print(f"Errore, probabilmente '{photo}' non è un file immagine valido o non ha metadati.")
                    
            else:
                print(f"Errore, probabilmente '{photo}' non è un file immagine valido o non ha metadati.")
                    
                

        return self.__metadati   # restituisci dizionario con metadati

if(__name__ == "__main__"):
    # TODO: Questo non funziona ora, dovremo trovare un altro modo di fare debug
    import sys

    actual_path = Path(sys.path[0])

    db_folder = Path(actual_path.parent.parent,
                     'tests', 'data')

    test = MetadataManager(db_folder)

    test.scan_file('photo.jpg')
    