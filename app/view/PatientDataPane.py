from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel, QLineEdit, QComboBox, QDateEdit

from app import Helpers
from app.Helpers.Names import Names


class PatientDataPane( QtWidgets.QGroupBox ):
    def __init__(self, str):
        super().__init__( str )

        self.lay = QtWidgets.QGridLayout()

        self.setLayout( self.lay )

        #Create widgets
        self.nameLabel = QLabel( Names.PatientDataPane.name)
        self.surnameLabel = QLabel( Names.PatientDataPane.surname)
        self.sexLabel = QLabel( Names.PatientDataPane.sex )
        self.documentLabel = QLabel( Names.PatientDataPane.docId )
        self.dobLabel = QLabel( Names.PatientDataPane.dob)

        self.nameTextField = QLineEdit( )
        self.surnameTextField = QLineEdit( )
        self.sexComboBox = QComboBox()
        self.documentTextField = QLineEdit()
        self.dobDateEdit = QDateEdit()

        self.nameTextField.setPlaceholderText(Names.PatientDataPane.namePlaceholder)
        self.surnameTextField.setPlaceholderText(Names.PatientDataPane.surnamePlaceholder)
        self.documentTextField.setPlaceholderText(Names.PatientDataPane.docIdPlaceholder)

        #Adjust widgets
        self.sexComboBox.addItems(Names.PatientDataPane.sexComboBox)

        self.lay.addWidget( self.nameLabel, 0, 0)
        self.lay.addWidget( self.surnameLabel, 1, 0)
        self.lay.addWidget( self.sexLabel, 2, 0)
        self.lay.addWidget( self.documentLabel, 3, 0)
        self.lay.addWidget( self.dobLabel, 4, 0)

        self.lay.addWidget( self.nameTextField, 0,1)
        self.lay.addWidget( self.surnameTextField, 1,1)
        self.lay.addWidget( self.sexComboBox, 2, 1)
        self.lay.addWidget( self.documentTextField, 3,1 )
        self.lay.addWidget( self.dobDateEdit, 4, 1)
