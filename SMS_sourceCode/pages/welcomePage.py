from general_lib import *

class welcomePage():
    def __init__(self,mainSelf):
        self.mainSelf = mainSelf

        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()


    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.welcomeScreen_widget = self.mainSelf.findChild(QtWidgets.QWidget, "welcomeScreen_widget")
        self.welcomeScreen_widget.raise_()

        # ------------ Buttons ------------
        # ----- Welcome Page -----
        self.getStarted_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "getStarted_btn")
        self.welcomeExit_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "welcomeExit_btn")

    def GUI_connect_buttons(self):
        self.getStarted_btn.clicked.connect(self.getStarted_btn_clicked)
        self.welcomeExit_btn.clicked.connect(self.welcomeExit_btn_clicked)

    # ------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.mainSelf.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.mainSelf.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
        destinationPageObj.raise_()
    def getStarted_btn_clicked(self):
        self.navigate("welcomeScreen_widget", "loginScreen_widget")

    def welcomeExit_btn_clicked(self):
        self.mainSelf.close()