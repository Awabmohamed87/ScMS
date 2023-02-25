from general_lib import *
from pages.newSessionPage import *

class homePage():
    def __init__(self,mainSelf):
        self.mainSelf = mainSelf

        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()

    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.homeManagerScreen_widget= self.mainSelf.findChild(QtWidgets.QWidget, "homeManagerScreen_widget")

        # ------------ Buttons ------------
        # ----- Home page -----
        self.startNewSession_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "startNewSession_btn")
        self.sessionsHistory_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "sessionsHistory_btn")
        self.homeLogout_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "homeLogout_btn")

    def GUI_connect_buttons(self):
        self.startNewSession_btn.clicked.connect(self.startNewSession_btn_clicked)
        self.sessionsHistory_btn.clicked.connect(self.sessionsHistory_btn_clicked)
        self.homeLogout_btn.clicked.connect(self.homeLogout_btn_clicked)

    # ------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.mainSelf.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.mainSelf.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
        destinationPageObj.raise_()

    def startNewSession_btn_clicked(self):
        self.mainSelf.newSessionPage = newSessionPage(self.mainSelf)
        self.navigate("homeManagerScreen_widget", "NewSessionScreen_widget")


    def sessionsHistory_btn_clicked(self):
        self.navigate("homeManagerScreen_widget", "dataEntry_widget")

    def homeLogout_btn_clicked(self):
        self.navigate("homeManagerScreen_widget", "welcomeScreen_widget")