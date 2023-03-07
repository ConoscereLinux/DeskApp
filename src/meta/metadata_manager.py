"""Modulo per la gestione dei metadati dei file."""

# Standard Import
import os
import shutil
import time
from pathlib import Path

# Site-package Import

# Project Import
from exif import Image  #libreria python per lettura metadati immagini


DB_FILE_NAME = "database.txt"


class MetadataManager():
    """Classe che estrae i metadati dei file di una cartella"""

    def __init__(self,
                 source_folder: Path,
                 elaborated_folder: Path,
                 db_folder: Path):
        
        # settaggio variabili
        self.__listOfImage = 0
        self.__listOfScanned = 0
        self.__totalImage = 0
        self.__totalScanned = 0
        self.__x = 0
        self.__y = 0
        self.__counter = 1
        
        self.__source_folder = source_folder
        self.__elaborated_folder = elaborated_folder
        self.__db_folder = db_folder

    def scanfile(self):

        self.metadati = {}  # inizializzo dizionario metadati
        """Esegue la scansione della cartella in cerca dei file"""

        """ scansione cartella file elaborati per verificare presenza file"""
        print("Verifico presenza foto nelle cartelle.")
        print("Scansione in corso", end="")

        self.__listOfScanned = self.__elaborated_folder.glob('**/*.jpg')  # legge tutte le immagini presenti
        self.__totalScanned = (len(list(self.__listOfScanned)))  # conta immagini presenti

        if self.__totalScanned == 0:
            print("Non sono presenti foto nella cartella dei file analizzati")
        elif self.__totalScanned == 1:
            print("E' presente 1 foto nella cartella dei file analizzati")
            self.__counter = self.__totalScanned + 1
        else:
            print("Sono presenti", self.__totalScanned, "foto nella cartella dei file analizzati.")
            self.__counter = self.__totalScanned + 1

        """ legge tutte le immagini presenti nella cartella di file da elavorare"""
        self.__listOfImage = self.__source_folder.glob('**/*.jpg')
        self.__totalImage = (len(list(self.__listOfImage)))  # numero di foto presenti nella cartella

        if self.__totalImage == 0:
            print("Non sono presenti foto nella cartella dei file da analizzare; attendo inserimento file.")

        elif self.__totalImage == 1:
            print("E' presente 1 foto nella cartella dei file da analizzare")
            time.sleep(1)
            print("Ora procedo ad eseguire analisi\n")
            time.sleep(1)
        else:
            print("Sono presenti", self.__totalImage, "foto nella cartella dei file da analizzare.")
            time.sleep(1)
            print("Ora procedo ad eseguire analisi\n")
            time.sleep(1)

        f = open(Path(self.__db_folder, DB_FILE_NAME), 'w')  # apri file txt per salvare tutti i dati estratti

        for name in self.__source_folder.glob('*.jpg'):
            # standardizzazione/rinomina foto, copia la foto nella cartella scannedfolder e cancella foto nella cartella imagefolder
            z = str("image" + str(self.__counter) + ".jpg")
            os.chdir(self.__source_folder)
            os.rename(name, z)
            print("Original name: ", name)
            print("Deskapp name: ", z)
            shutil.copy(self.__source_folder.joinpath(z), self.__elaborated_folder)
            os.remove(self.__source_folder.joinpath(z))

            os.chdir(self.__elaborated_folder)  # cartella dove vengono spostante le immagini lette

            with open(z, 'rb') as img_file:
                img = Image(img_file)

            # elenco EXIF tags contenuti nelle immagini
            # sorted(img.list_all())

            f.write(f'Original name: {name}\n')
            f.write(f'Deskapp name: {z}\n')

            # Make of device which captured image
            print(f'Make: {img.get("make")}')
            f.write(f'Make: {img.get("make")}\n')
            self.metadati["Make"] = img.get("make")

            # Model of device which captured image
            print(f'Model: {img.get("model")}')
            f.write(f'Model: {img.get("model")}\n')
            self.metadati["Model"] = img.get("model")

            # Software involved in uploading and digitizing image
            print(f'Software: {img.get("software")}')
            f.write(f'Software: {img.get("software")}\n')
            self.metadati["Software"] = img.get("software")

            # Name of photographer who took the image
            print(f'Artist: {img.get("artist")}')
            f.write(f'Artist: {img.get("artist")}\n')
            self.metadati["Artist"] = img.get("artist")

            # Original datetime that image was taken (photographed)
            print(f'DateTime (Original): {img.get("datetime_original")}')
            f.write(f'DateTime (Original): {img.get("datetime_original")}\n')
            self.metadati["DateTime (Original)"] = img.get("datetime_original")

            # Details of flash function
            print(f'Flash Details: {img.get("flash")}')
            f.write(f'Flash Details: {img.get("flash")}\n')
            self.metadati["Flash Details"] = img.get("flash")

            # getting the Longitude and latitude data
            print(f' Longitude data: {img.get("gps_longitude")}')
            print(f' latitude data: {img.get("gps_latitude")}')
            f.write(f' Longitude data: {img.get("gps_longitude")}\n')
            f.write(f' latitude data: {img.get("gps_latitude")}\n')
            self.metadati["Longitude data"] = img.get("gps_longitude")
            self.metadati["latitude data"] = img.get("gps_latitud")

            # getting the Longitude  and latitude Reference data is also very important when converting the Decimal degrees formen
            print(f' Longitude data reference : {img.get("gps_longitude_ref")}')
            print(f' latitude data reference : {img.get("gps_latitude_ref")}')
            f.write(f' Longitude data reference : {img.get("gps_longitude_ref")}\n')
            f.write(f' latitude data reference : {img.get("gps_latitude_ref")}\n')
            self.metadati["Longitude data reference"] = img.get("gps_longitude_ref")
            self.metadati["latitude data reference"] = img.get("gps_latitude_ref")

            # Larghezza
            print(f'Larghezza: {img.get("pixel_x_dimension")}')
            f.write(f'Larghezza: {img.get("pixel_x_dimension")}\n')
            self.metadati["Larghezza"] = img.get("pixel_x_dimension")

            # altezza
            print(f'Altezza: {img.get("pixel_y_dimension")}')
            f.write(f'Altezza: {img.get("pixel_y_dimension")}\n')
            self.metadati["Altezza"] = img.get("pixel_y_dimension")

            # risoluzione
            print(f'Risoluzione: {img.get("x_resolution")}')
            f.write(f'Risoluzione: {img.get("x_resolution")}\n')
            self.metadati["Risoluzione"] = img.get("x_resolution")

            print(f'Dimensione file (in byte): {int(os.stat(z).st_size)}\n')
            f.write(f'Dimensione file (in byte): {int(os.stat(z).st_size)}\n')
            self.metadati["Dimensione file (in byte)"] = int(os.stat(z).st_size)
            print(os.stat(z).st_size)

            print(list(self.metadati.items()))

            self.__counter = self.__counter + 1

            os.chdir(self.__source_folder)  # posizionarsi nella cartella dove inserire immagini da leggere

        f.close()
if(__name__ == "__main__"):
    import sys
    
    actual_path = Path(sys.path[0])
    source_folder = Path(actual_path.parent.parent,
                         'tests', 'data', 'source_folder')
    
    elaborated_folder = Path(actual_path.parent.parent,
                         'tests', 'data', 'elaborated_folder')
    
    db_folder = Path(actual_path.parent.parent,
                         'tests', 'data')
    
    test = MetadataManager(source_folder, elaborated_folder, db_folder)

    test.scanfile()
    