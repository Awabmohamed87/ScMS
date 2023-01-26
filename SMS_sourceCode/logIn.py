from general_lib import *

def login_handling(self):
    loginUserName_tbox = self.findChild(QtWidgets.QLineEdit, "loginUserName_tbox")
    loginPassword_tbox = self.findChild(QtWidgets.QLineEdit, "loginPassword_tbox")
    if login(loginUserName_tbox.text(),loginPassword_tbox.text()) == True:
        self.navigate("loginScreen_widget", "homeManagerScreen_widget")
        # Reset fields
        login_btn = self.findChild(QtWidgets.QPushButton, "login_btn")
        login_btn.setText("Login")
        loginUserName_tbox.setText("")
        loginPassword_tbox.setText("")

    else:
        login_btn = self.findChild(QtWidgets.QPushButton, "login_btn")
        login_btn.setText("Invalid Credentials, Try again")