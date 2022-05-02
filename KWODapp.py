import sys

from PyQt6 import QtWidgets, QtGui

from app.view import AppView

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    app.setWindowIcon(QtGui.QIcon('icon.png'))

    widget = AppView.AppView()
    widget.show()

    sys.exit(app.exec())
