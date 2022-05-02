from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt

from app.Helpers.Names import Names


class ExportLanguagePane(QtWidgets.QGroupBox):
    def __init__(self,str):
        super().__init__(str)
        self.lay = QtWidgets.QVBoxLayout()
        self.setLayout(self.lay)

        self.languages = Names.TestLanguages.languages
        self.languageCheckBoxes = []

        self.scroll = QtWidgets.QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QtWidgets.QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QtWidgets.QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for language in self.languages:
            object = QtWidgets.QCheckBox(language)
            self.languageCheckBoxes.append(object)
            self.vbox.addWidget(self.languageCheckBoxes[-1])
        self.widget.setLayout( self.vbox )

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy( Qt.ScrollBarPolicy.ScrollBarAlwaysOn )
        self.scroll.setHorizontalScrollBarPolicy( Qt.ScrollBarPolicy.ScrollBarAlwaysOff )
        self.scroll.setWidgetResizable( True )
        self.scroll.setWidget( self.widget )
        self.lay.addWidget(self.scroll)
