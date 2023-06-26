from general_lib import *
from config import *
from PyQt5.QtCore import *
import cv2


class newUserPage():
    def __init__(self, mainSelf):
        self.mainSelf = mainSelf

        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()

    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.newUser_widget = self.mainSelf.findChild(QtWidgets.QWidget, "newUser_widget")
        # ------------ Icons ------------
        self.fingerPrintIcon_Label = self.mainSelf.findChild(QtWidgets.QWidget, "breakAnimation_Label_3")
        # Load the GIF using QMovie
        self.movie = QMovie("uis/materials/icons/wired-lineal-1021-rules.gif", QByteArray(), self.mainSelf)
        # Set the size of the QMovie to be the same as the QLabel
        self.movie.setScaledSize(self.fingerPrintIcon_Label.size())
        self.fingerPrintIcon_Label.setMovie(self.movie)
        self.movie.start()
        # ------------ Buttons ------------
        self.newUser_Back_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "newUser_Back_btn")
        self.newUser_Back_btn.setFocusPolicy(Qt.NoFocus)

    def GUI_connect_buttons(self):
        self.newUser_Back_btn.clicked.connect(self.newUser_Back_btn_clicked)

    # ------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.mainSelf.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.mainSelf.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
        destinationPageObj.raise_()

    def newUser_Back_btn_clicked(self):
        self.navigate("newUser_widget", "homeManagerScreen_widget")