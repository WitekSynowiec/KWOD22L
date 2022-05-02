from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel, QLineEdit, QComboBox, QDateTimeEdit

from app.Helpers.Names import Names


class TestDataPane(QtWidgets.QGroupBox):
    def __init__(self, str):
        super().__init__( str )

        self.lay = QtWidgets.QGridLayout()

        self.setLayout( self.lay )

        # Create widgets
        self.collectedMaterial = QLabel( Names.TestDataPane.collectedMaterial )
        self.doCollection = QLabel( Names.TestDataPane.dateOfCollection )
        self.doAcceptance = QLabel( Names.TestDataPane.dateOfAcceptance )
        self.testName = QLabel( Names.TestDataPane.testName )
        self.result = QLabel( Names.TestDataPane.result )

        self.collectedMaterialComboBox = QComboBox()
        self.doAcceptanceDateTimeEdit = QDateTimeEdit()
        self.doCollectionDateTimeEdit = QDateTimeEdit()
        self.testNameComboBox = QComboBox()
        self.resultComboBox = QComboBox()

        # Adjust widgets
        self.collectedMaterialComboBox.addItems( Names.TestDataPane.collectedMaterialComboBox )
        self.testNameComboBox.addItems( Names.TestDataPane.testNameComboBox )
        self.resultComboBox.addItems( Names.TestDataPane.resultComboBox )

        self.lay.addWidget( self.collectedMaterial, 0, 0 )
        self.lay.addWidget( self.doCollection, 1, 0 )
        self.lay.addWidget( self.doAcceptance, 2, 0 )
        self.lay.addWidget( self.testName, 3, 0 )
        self.lay.addWidget( self.result, 4, 0 )

        self.lay.addWidget( self.collectedMaterialComboBox, 0, 1 )
        self.lay.addWidget( self.doAcceptanceDateTimeEdit, 1, 1 )
        self.lay.addWidget( self.doCollectionDateTimeEdit, 2, 1 )
        self.lay.addWidget( self.testNameComboBox, 3, 1 )
        self.lay.addWidget( self.resultComboBox, 4, 1 )