# from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5 import uic
from PyQt5 import pyrcc
from uis import res
from pages.welcomePage import *
from pages.loginPage import *
from pages.homePage import *
from pages.newSessionPage import *
from pages.sessionChartsPage import *
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis\GUI.ui",self)
        self.GUI_initialize_properities()
        self.GUI_initialize_Pages()

    def GUI_initialize_properities(self):
        self.setWindowIcon(QIcon("uis\materials\systemLogo.png"))
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def GUI_initialize_Pages(self):
        # ------------ Pages ------------
        self.welcomePage = welcomePage(self)
        self.loginPage = loginPage(self)
        self.homePage = homePage(self)
        self.sessionChartsPage = sessionChartsPage(self)

        self.dataEntry_widget = self.findChild(QtWidgets.QWidget, "dataEntry_widget")


    # action #1
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()
    # action #2
    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window =Window()
    window.show()
    sys.exit(app.exec())