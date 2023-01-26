# from uis import welcome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5 import pyrcc
from uis import res
from cameras import *
from logIn import *

import sys
class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis\GUI.ui",self)

        self.GUI_initialize_properities()
        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()

    def GUI_initialize_properities(self):
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.welcomeScreen_widget = self.findChild(QtWidgets.QWidget, "welcomeScreen_widget")
        self.loginScreen_widget = self.findChild(QtWidgets.QWidget, "loginScreen_widget")
        self.homeManagerScreen_widget= self.findChild(QtWidgets.QWidget, "homeManagerScreen_widget")
        self.mainManagerScreen_widget= self.findChild(QtWidgets.QWidget, "mainManagerScreen_widget")
        self.dataEntry_widget = self.findChild(QtWidgets.QWidget, "dataEntry_widget")
        self.loginScreen_widget.hide()
        self.homeManagerScreen_widget.hide()
        self.mainManagerScreen_widget.hide()
        self.dataEntry_widget.hide()

        # ------------ Cameras ------------
        self.cameraAttendance_Label = self.findChild(QLabel, "cameraAttendance_Label")

        # ------------ Buttons ------------
        # ----- Welcome Page -----
        self.getStarted_btn = self.findChild(QtWidgets.QPushButton, "getStarted_btn")
        # ----- Login page -----
        self.home_btn = self.findChild(QtWidgets.QPushButton, "loginHome_btn")
        self.login_btn = self.findChild(QtWidgets.QPushButton, "login_btn")
        # ----- Home page -----
        self.startNewSession_btn = self.findChild(QtWidgets.QPushButton, "startNewSession_btn")
        self.sessionsHistory_btn = self.findChild(QtWidgets.QPushButton, "sessionsHistory_btn")
        self.homeLogout_btn = self.findChild(QtWidgets.QPushButton, "homeLogout_btn")
        # ----- New Session page -----
        self.endSession_btn = self.findChild(QtWidgets.QPushButton, "endSession_btn")
        self.studentsAttendance_tableWidget = self.findChild(QtWidgets.QTableWidget, "studentsAttendance_tableWidget")


    def GUI_connect_buttons(self):
        self.getStarted_btn.clicked.connect(self.getStarted_btn_clicked)
        self.home_btn.clicked.connect(self.home_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)
        self.startNewSession_btn.clicked.connect(self.startNewSession_btn_clicked)
        self.sessionsHistory_btn.clicked.connect(self.sessionsHistory_btn_clicked)
        self.endSession_btn.clicked.connect(self.endSession_btn_clicked)
        self.homeLogout_btn.clicked.connect(self.homeLogout_btn_clicked)

    #------------ Session ------------
    def AttendanceCamera_UpdateSlot(self, Image):
        self.cameraAttendance_Label.setPixmap(QPixmap.fromImage(Image))

    #------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
    # ----- Welcome Page -----
    def getStarted_btn_clicked(self):
        self.navigate("welcomeScreen_widget", "loginScreen_widget")

    # ----- Login Page -----
    def login_btn_clicked(self):
        login_handling(self)

    def home_btn_clicked(self):
        self.navigate("loginScreen_widget", "welcomeScreen_widget")

    # ----- Home Page -----
    def startNewSession_btn_clicked(self):
        self.navigate("homeManagerScreen_widget", "mainManagerScreen_widget")
        self.attentionCamera_Worker = attentionCamera_Worker()
        self.attentionCamera_Worker.start()
        self.attentionCamera_Worker.ImageUpdate.connect(self.AttendanceCamera_UpdateSlot)

    def sessionsHistory_btn_clicked(self):
        self.navigate("homeManagerScreen_widget", "dataEntry_widget")

    def homeLogout_btn_clicked(self):
        self.navigate("homeManagerScreen_widget", "welcomeScreen_widget")

    # ----- New Session Page -----
    def endSession_btn_clicked(self):
        self.navigate("mainManagerScreen_widget", "homeManagerScreen_widget")

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