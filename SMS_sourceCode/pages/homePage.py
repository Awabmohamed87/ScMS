from general_lib import *
from pages.newSessionPage import *
from pages.sessionsHistoryPage import *
from pages.newUserPage import *
from pages.uniformConfigurePage import *
from pages.cameraConfigPage import *

class homePage():
    currentUser = {'Name': '...'}
    role = 1
    def __init__(self, mainSelf, user, roleID):
        self.mainSelf = mainSelf
        self.currentUser = user
        self.role = roleID
        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()
        self._setupPage()

    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.homeManagerScreen_widget = self.mainSelf.findChild(QtWidgets.QWidget, "homeManagerScreen_widget")

        # ------------ Buttons ------------
        # ----- Home page -----
        self.startNewSession_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "startNewSession_btn")
        self.startNewSession_btn.setFocusPolicy(Qt.NoFocus)
        self.sessionsHistory_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "sessionsHistory_btn")
        self.sessionsHistory_btn.setFocusPolicy(Qt.NoFocus)
        self.addNewStudent_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "addNewStudent_btn")
        self.addNewStudent_btn.setFocusPolicy(Qt.NoFocus)
        self.cameraConfigure_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "cameraConfigure_btn")
        self.cameraConfigure_btn.setFocusPolicy(Qt.NoFocus)

        self.uniformConfigure_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "uniformConfigure_btn")
        self.uniformConfigure_btn.setFocusPolicy(Qt.NoFocus)

        self.homeLogout_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "homeLogout_btn")
        self.homeLogout_btn.setFocusPolicy(Qt.NoFocus)
        self.currentUserNameLabel = self.mainSelf.findChild(QtWidgets.QLabel, "homeUserName_label")
        self.homeRolelabel = self.mainSelf.findChild(QtWidgets.QLabel, "homeJobRole_label")




    def _setupPage(self):
        self.currentUserNameLabel.setText(self.currentUser['Name'])
        self.homeRolelabel.setText(mapRole(self.role))

    def GUI_connect_buttons(self):
        self.startNewSession_btn.clicked.connect(self.startNewSession_btn_clicked)
        self.sessionsHistory_btn.clicked.connect(self.sessionsHistory_btn_clicked)
        self.addNewStudent_btn.clicked.connect(self.addNewStudent_btn_clicked)
        self.uniformConfigure_btn.clicked.connect(self.uniformConfigure_btn_clicked)
        self.cameraConfigure_btn.clicked.connect(self.cameraConfigure_btn_clicked)
        self.homeLogout_btn.clicked.connect(self.homeLogout_btn_clicked)

    # ------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.mainSelf.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.mainSelf.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
        destinationPageObj.raise_()
        # get logged in user data
        #getUser(email)

    def startNewSession_btn_clicked(self):
        self.mainSelf.newSessionPage = newSessionPage(self.mainSelf)
        self.navigate("homeManagerScreen_widget", "NewSessionScreen_widget")


    def sessionsHistory_btn_clicked(self):
        self.mainSelf.sessionsHistoryPage = sessionsHistoryPage(self.mainSelf)
        # self.navigate("homeManagerScreen_widget", "dataEntry_widget")
    def addNewStudent_btn_clicked(self):
        self.newUserPage = newUserPage(self.mainSelf)
        self.navigate("homeManagerScreen_widget", "newUser_widget")
    def uniformConfigure_btn_clicked(self):
        self.uniformConfigurePage = uniformConfigurePage(self.mainSelf)
        self.navigate("homeManagerScreen_widget", "uniformConfig_widget")
    def cameraConfigure_btn_clicked(self):
        self.cameraConfigPage = cameraConfigPage(self.mainSelf)
        self.navigate("homeManagerScreen_widget", "cameraConfig_widget")
    def homeLogout_btn_clicked(self):
        self.navigate("homeManagerScreen_widget", "welcomeScreen_widget")