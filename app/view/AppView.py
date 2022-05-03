from PyQt6 import QtWidgets, QtGui
from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel

from app.Helpers.Names import Names
from app.controller.Controller import Controller
from app.view.ExportLanguagePane import ExportLanguagePane
from app.view.InfoPane import InfoPane
from app.view.PatientDataPane import PatientDataPane
from app.view.TestDataPane import TestDataPane


class AppView(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(AppView,self).__init__(parent)
        self.initUI()
        self.resize(800,600)
        self.setWindowTitle(Names.AppViewPane.windowTitle)


    def initUI(self):
        # Setting grid layout
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget( self.central_widget )
        self.lay = QtWidgets.QGridLayout( self.central_widget )

        # Creating panes instances and layouting them
        self.pdPane = PatientDataPane(Names.AppViewPane.patientData)
        self.elPane = ExportLanguagePane(Names.AppViewPane.testLanguages)
        self.tdPane = TestDataPane(Names.AppViewPane.testData)
        self.iPane = InfoPane(Names.AppViewPane.infoPane)

        # Buttons
        self.proceedButton = QtWidgets.QPushButton(Names.AppViewPane.proceedButton, self)
        self.clearButton = QtWidgets.QPushButton(Names.AppViewPane.clearButton)

        # Connections

        # Creating Window Label
        self.titleLabel = QLabel(Names.AppViewPane.title)
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.lay.addWidget(self.titleLabel,0,0,1,5)
        self.lay.addWidget( self.pdPane, 1, 0, 8, 2 )
        self.lay.addWidget( self.elPane, 1, 4, 8, 1 )
        self.lay.addWidget( self.tdPane, 1, 2, 8, 2 )
        self.lay.addWidget( self.iPane, 9, 0, 4, 4 )
        self.lay.addWidget( self.proceedButton, 11, 4,1,1)
        self.lay.addWidget( self.clearButton, 10, 4,1,1)

        #Roam controller
        self.controller = Controller(self.pdPane, self.tdPane,self.elPane,self.iPane)
        self.proceedButton.clicked.connect(self.controller.exportPDF)


