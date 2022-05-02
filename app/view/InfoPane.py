from PyQt6 import QtWidgets

class InfoPane(QtWidgets.QGroupBox):
    def __init__(self,str):
        super().__init__(str)
        self.lay = QtWidgets.QVBoxLayout()
        self.setLayout(self.lay)

        self.infoTextField = QtWidgets.QPlainTextEdit()
        self.lay.addWidget(self.infoTextField)
