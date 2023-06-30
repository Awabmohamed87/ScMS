from general_lib import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTableWidgetItem
class sessionsHistoryPage():
    def __init__(self,mainSelf):
        self.mainSelf = mainSelf
        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()
        self.retrieve_SessionsData()

    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.sessionHistory_widget = self.mainSelf.findChild(QtWidgets.QWidget, "sessionHistory_widget")

        # ------------ Tabel ------------
        self.previousSessions_tableWidget = self.mainSelf.findChild(QtWidgets.QTableWidget,"previousSessions_tableWidget")
        self.previousSessions_tableWidget.itemClicked.connect(self.handleItemClick)
        self.previousSessions_tableWidget.setColumnWidth(1, 250)
        self.reportHistoryAttendance_tableWidget = self.mainSelf.findChild(QtWidgets.QTableWidget,"reportHistoryAttendance_tableWidget")
        # ------------ Objects ------------
        self.historySessionTime_label = self.mainSelf.findChild(QtWidgets.QLabel, "historySessionTime_label")
        self.historyAverageAttentionLevel_label = self.mainSelf.findChild(QtWidgets.QLabel, "historyAverageAttentionLevel_label")
        self.historyNumOfStudents_label = self.mainSelf.findChild(QtWidgets.QLabel, "historyNumOfStudents_label")

        # ------------ Buttons ------------
        self.sessionHistory_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "sessionHistory_btn")
        self.sessionHistory_btn.setFocusPolicy(Qt.NoFocus)
    def GUI_connect_buttons(self):
        self.sessionHistory_btn.clicked.connect(self.sessionHistory_btn_clicked)
    def retrieve_SessionsData(self):
        self.sessionHistory=self.mainSelf.dataBase.db.child("Sessions").get()
        self.sessionHistory_Index=[]
        if self.sessionHistory.val() is not None:
            for session in self.sessionHistory.each():
                self.sessionHistory_Index.append(session.key())
                self.previousSessions_tableWidget.setRowCount(0)
                for i in range(len(self.sessionHistory.val())):
                    # Get the current number of rows & Add a new row
                    row = self.previousSessions_tableWidget.rowCount()
                    self.previousSessions_tableWidget.insertRow(row)
                    # Add session_data to the new row
                    session_data = [session.val()['subject'], session.val()['date']]
                    for i, item in enumerate(session_data):
                        table_item = QTableWidgetItem(str(item))
                        # # set Uniform statue text color
                        # if i == 2 and item == True:
                        #     table_item.setForeground(QBrush(QColor(255, 255, 255)))
                        #     table_item.setBackground(QBrush(QColor(33, 140, 116, 160)))
                        # elif i == 2 and item == False:
                        #     table_item.setForeground(QBrush(QColor(255, 255, 255)))
                        #     table_item.setBackground(QBrush(QColor(229, 108, 120, 200)))
                        self.previousSessions_tableWidget.setItem(row, i, table_item)

    def handleItemClick(self, item):
        # Get the row and column of the clicked item
        row = item.row()
        # col = item.column()
        # # Get the text of the clicked item
        # text = item.text()
        # print(self.sessionHistory_Index[row])
        student_Info=self.mainSelf.dataBase.db.child("Sessions").child(self.sessionHistory_Index[row]).get()

        self.historySessionTime_label.setText(student_Info.val()['sessionDuration'])
        self.historyAverageAttentionLevel_label.setText(str(student_Info.val()['avgAttentionLevel'])+"%")
        numStudents=len(student_Info.val()['sessionAttendanceInfo'][0])
        self.historyNumOfStudents_label.setText(str(numStudents))

        # print(student_Info.val()['sessionAttendanceInfo'])
        self.reportHistoryAttendance_tableWidget.setRowCount(0)
        for i in range(numStudents):
            # Get the current number of rows & Add a new row
            row = self.reportHistoryAttendance_tableWidget.rowCount()
            self.reportHistoryAttendance_tableWidget.insertRow(row)

            # Add student_data to the new row
            student_data = [student_Info.val()['sessionAttendanceInfo'][0][i], student_Info.val()['sessionAttendanceInfo'][1][i],
                            student_Info.val()['sessionAttendanceInfo'][2][i]]
            for i, item in enumerate(student_data):
                table_item = QTableWidgetItem(str(item))
                # set Uniform statue text color
                if i == 2 and item == True:
                    table_item.setForeground(QBrush(QColor(255, 255, 255)))
                    table_item.setBackground(QBrush(QColor(33, 140, 116, 160)))
                elif i == 2 and item == False:
                    table_item.setForeground(QBrush(QColor(255, 255, 255)))
                    table_item.setBackground(QBrush(QColor(229, 108, 120, 200)))
                self.reportHistoryAttendance_tableWidget.setItem(row, i, table_item)


    # ------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.mainSelf.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.mainSelf.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
        destinationPageObj.raise_()
    def sessionHistory_btn_clicked(self):
        self.navigate("sessionHistory_widget", "homeManagerScreen_widget")