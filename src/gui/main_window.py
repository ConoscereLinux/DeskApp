"""Finestra principale dell'applicazione."""

# Standard Import

# Site-package Import
from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore

# Local Import
from util import resource as r
from pickle import TRUE
from PySide6.QtCore import Slot


class MainBase(QtWidgets.QMainWindow):
    """
    Classe per la finestra principale dell'applicazione.
    
    Viene ereditata la classe QMainWindow, e poi viene caratterizzata in base
    alle peculiarità dell'applicazione.
    """
    
    def __init__(self,
                 app: r.ResourceManager,
                 title: str,
                 width: int = 800,
                 height: int = 600):
        """
        Il costruttore della finestra.
        
        Args:
            app: il riferimento alla raccolta di resource 
            title: il titolo della finestra
            width: la larghezza iniziale della finestra
            height: l'altezza iniziale della finestra
            
        """
        super().__init__()
 
        self.__app = app
        self.__title_text = title
        self.__width = width
        self.__height = height
        
        self.__create_widget()
        
        self.show()

    def __create_widget(self):
        """
        Creazione dei Widget dell'interfaccia grafica.
        """
        self.resize(self.__width, self.__height)
        self.setWindowTitle(self.__title_text)
        # self.setWindowIcon(QtGui.QIcon(self.__app.icon))
        
        # ----------------------------------------------------------------------
        self.__widget = QtWidgets.QFrame(self)
        self.__layout = QtWidgets.QVBoxLayout()
        self.setCentralWidget(self.__widget)

        self.__widget.setLayout(self.__layout)
        
        # ----------------------------------------------------------------------
        self.__tab = QtWidgets.QTabWidget()
        self.__layout.addWidget(self.__tab)
        
        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.__timer__timeout)
        self.__timer.setInterval(1000)
        self.__timer.setSingleShot(True)
        self.__timer.start()
        
        self.__center()

    def __center(self,
                 maximized: bool = False):
        """
        Si occupa di centrare la finestra.
        
        Args:
            maximized: massimizza la finestra
            
        """
        
        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        if(maximized):
            self.showMaximized()
     
    # @Slot
    def __timer__timeout(self):
        """Usato per gestire in maniera simile al Thread la chiamat al Digger."""
        
        self.__app.digger.scan()
        
        self.__timer.setInterval(5000)
        self.__timer.start()
    