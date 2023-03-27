from general_lib import *

class sessionsHistoryPage():
    def __init__(self,mainSelf):
        self.mainSelf = mainSelf
        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()


    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.dataEntry_widget = self.mainSelf.findChild(QtWidgets.QWidget, "dataEntry_widget")
        self.dataEntry_widget.show()
        self.dataEntry_widget.raise_()

        # ------------ Buttons ------------
        self.dataEntryBack_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "dataEntryBack_btn")

    def GUI_connect_buttons(self):
        self.dataEntryBack_btn.clicked.connect(self.dataEntryBack_btn_clicked)

    # ------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.mainSelf.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.mainSelf.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
        destinationPageObj.raise_()

    def dataEntryBack_btn_clicked(self):
        self.navigate("dataEntry_widget", "homeManagerScreen_widget")