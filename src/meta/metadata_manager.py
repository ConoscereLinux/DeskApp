"""Modulo per la gestione dei metadati di un file chiamato PHOTO fornito da classe digger_manager.py"""

# Standard Import
import os
from pathlib import Path

# Project Import
from exif import Image  #libreria python per lettura metadati immagini


DB_FILE_NAME = "database.txt"  # creazione file DATABASE (probabilmente verrà tolto?)


class MetadataManager():
    """Classe che estrae i metadati di un file"""

    def __init__(self,
                 db_folder: Path):

        self.__metadati = None
        self.__db_folder = db_folder

    def scan_file(self, photo):

        self.__metadati = {}  # inizializzo dizionario metadati


        f = open(Path(self.__db_folder, DB_FILE_NAME), 'w')  # apri file txt per salvare tutti i dati estratti

        # leggere file PHOTO inserito, per test, dentro a \src\meta poi verrà passato da digger_manager.py
        with open(photo, 'rb') as img_file:
            img = Image(img_file)

        # Make of device which captured image
        print(f'Make: {img.get("make")}')
        f.write(f'Make: {img.get("make")}\n')
        self.__metadati["Make"] = img.get("make")

        # Model of device which captured image
        print(f'Model: {img.get("model")}')
        f.write(f'Model: {img.get("model")}\n')
        self.__metadati["Model"] = img.get("model")

        # Software involved in uploading and digitizing image
        print(f'Software: {img.get("software")}')
        f.write(f'Software: {img.get("software")}\n')
        self.__metadati["Software"] = img.get("software")

        # Name of photographer who took the image
        print(f'Artist: {img.get("artist")}')
        f.write(f'Artist: {img.get("artist")}\n')
        self.__metadati["Artist"] = img.get("artist")

        # Original datetime that image was taken (photographed)
        print(f'DateTime (Original): {img.get("datetime_original")}')
        f.write(f'DateTime (Original): {img.get("datetime_original")}\n')
        self.__metadati["DateTime (Original)"] = img.get("datetime_original")

        # Details of flash function
        print(f'Flash Details: {img.get("flash")}')
        f.write(f'Flash Details: {img.get("flash")}\n')
        self.__metadati["Flash Details"] = img.get("flash")

        # getting the Longitude and latitude data
        print(f' Longitude data: {img.get("gps_longitude")}')
        print(f' latitude data: {img.get("gps_latitude")}')
        f.write(f' Longitude data: {img.get("gps_longitude")}\n')
        f.write(f' latitude data: {img.get("gps_latitude")}\n')
        self.__metadati["Longitude data"] = img.get("gps_longitude")
        self.__metadati["latitude data"] = img.get("gps_latitud")

        # getting the Longitude  and latitude Reference data is also very important when converting the Decimal degrees formen
        print(f' Longitude data reference : {img.get("gps_longitude_ref")}')
        print(f' latitude data reference : {img.get("gps_latitude_ref")}')
        f.write(f' Longitude data reference : {img.get("gps_longitude_ref")}\n')
        f.write(f' latitude data reference : {img.get("gps_latitude_ref")}\n')
        self.__metadati["Longitude data reference"] = img.get("gps_longitude_ref")
        self.__metadati["latitude data reference"] = img.get("gps_latitude_ref")

        # Larghezza
        print(f'Larghezza: {img.get("pixel_x_dimension")}')
        f.write(f'Larghezza: {img.get("pixel_x_dimension")}\n')
        self.__metadati["Larghezza"] = img.get("pixel_x_dimension")

        # altezza
        print(f'Altezza: {img.get("pixel_y_dimension")}')
        f.write(f'Altezza: {img.get("pixel_y_dimension")}\n')
        self.__metadati["Altezza"] = img.get("pixel_y_dimension")

        # risoluzione
        print(f'Risoluzione: {img.get("x_resolution")}')
        f.write(f'Risoluzione: {img.get("x_resolution")}\n')
        self.__metadati["Risoluzione"] = img.get("x_resolution")

        print(f'Dimensione file (in byte): {int(os.stat(photo).st_size)}\n')
        f.write(f'Dimensione file (in byte): {int(os.stat(photo).st_size)}\n')
        self.__metadati["Dimensione file (in byte)"] = int(os.stat(photo).st_size)

        print(list(self.__metadati.items()))   #lasciato un print per fare vedere nel dizionario cosa sarà scritto

        f.close()

        return self.__metadati   # restituisci dizionario con metadati

if(__name__ == "__main__"):

    import sys

    actual_path = Path(sys.path[0])

    db_folder = Path(actual_path.parent.parent,
                     'tests', 'data')

    test = MetadataManager(db_folder)

    test.scan_file('photo.jpg')
    