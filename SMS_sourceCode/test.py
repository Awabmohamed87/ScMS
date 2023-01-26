# import random
# from PyQt5 import QtWidgets, QtGui, QtCore
#
# class MyTable(QtWidgets.QTableWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Set the number of columns
#         self.setColumnCount(2)
#
#         # Create a timer to add rows every 5 seconds
#         self.timer = QtCore.QTimer()
#         self.timer.setInterval(5000)
#         self.timer.timeout.connect(self.add_row)
#         self.timer.start()
#
#     def add_row(self):
#         # Generate random data
#         data = [random.randint(0, 100) for i in range(2)]
#
#         # Get the current number of rows
#         row = self.rowCount()
#
#         # Add a new row
#         self.insertRow(row)
#
#         # Add data to the new row
#         for i, item in enumerate(data):
#             table_item = QtWidgets.QTableWidgetItem(str(item))
#             self.setItem(row, i, table_item)
#
# app = QtWidgets.QApplication([])
# table = MyTable()
# table.show()
# app.exec_()



import random
from PyQt5 import QtCore, QtGui, QtWidgets
def addRow(self):
    data = [random.randint(0, 100) for i in range(2)]
    # Get the current number of rows
    row = self.studentsAttendance_tableWidget.rowCount()
    # Add a new row
    self.studentsAttendance_tableWidget.insertRow(row)
    # Add data to the new row
    for i, item in enumerate(data):
        table_item = QtWidgets.QTableWidgetItem(str(item))
        self.studentsAttendance_tableWidget.setItem(row, i, table_item)
