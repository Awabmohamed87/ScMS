from general_lib import *


class loginPage():
    def __init__(self, mainSelf):
        self.mainSelf = mainSelf

        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()

    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.loginScreen_widget = self.mainSelf.findChild(QtWidgets.QWidget, "loginScreen_widget")

        # ------------ Buttons ------------
        # ----- Login page -----
        self.loginHome_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "loginHome_btn")
        self.login_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "login_btn")

        self.loginUserName_tbox = self.mainSelf.findChild(QtWidgets.QLineEdit, "loginUserName_tbox")
        self.loginUserName_tbox.textChanged.connect(self.onTextChanged)
        self.loginPassword_tbox = self.mainSelf.findChild(QtWidgets.QLineEdit, "loginPassword_tbox")
        self.loginPassword_tbox.textChanged.connect(self.onTextChanged)


    def onTextChanged(self):
        login_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "login_btn")
        if(login_btn.text() == "Invalid Credentials, Try again"):
            login_btn.setText("Login")

    def GUI_connect_buttons(self):
        self.loginHome_btn.clicked.connect(self.home_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)

    # ------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.mainSelf.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.mainSelf.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
        destinationPageObj.raise_()

    def login_btn_clicked(self):
        self.login_handling()

    def home_btn_clicked(self):
        self.navigate("loginScreen_widget", "welcomeScreen_widget")

    # ------------------- Login Handler -------------------
    def login_handling(self):
        loginUserName_tbox = self.mainSelf.findChild(QtWidgets.QLineEdit, "loginUserName_tbox")
        loginPassword_tbox = self.mainSelf.findChild(QtWidgets.QLineEdit, "loginPassword_tbox")
        if login(loginUserName_tbox.text(), loginPassword_tbox.text()):
            getUser(loginUserName_tbox.text())
            self.navigate("loginScreen_widget", "homeManagerScreen_widget")
            # Reset fields
            login_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "login_btn")
            login_btn.setText("Login")
            loginUserName_tbox.setText("")
            loginPassword_tbox.setText("")

        else:
            login_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "login_btn")
            login_btn.setText("Invalid Credentials, Try again")
