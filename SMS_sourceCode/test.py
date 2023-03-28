
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton
from PyQt5.QtCore import QByteArray

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

app = QApplication([])

# Create a push button
push_button = QPushButton("Click me!")

# Create a label to display the GIF
gif_label = QLabel()

# Load the GIF
gif_movie = QMovie("uis/materials/icons/tea-timeAnim.gif")

# Set the movie to the label
gif_label.setMovie(gif_movie)

# Start the animation
gif_movie.start()

# Set the label as the icon of the push button
push_button.setIcon(gif_label)

# Set the size and alignment of the icon
push_button.setIconSize(gif_label.sizeHint())
push_button.setIconAlignment(Qt.AlignCenter)

# Show the push button
push_button.show()

app.exec_()














# import random
# from PyQt5 import QtWidgets, QtGui, QtCore
# # ksize = (10, 10)
# # Image = cv2.blur(Image, ksize, cv2.BORDER_DEFAULT)
#
# import cv2
# import mediapipe as mp
# import time
# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils
#
#
# #For webcam input:
# cap = cv2.VideoCapture(0)
# #For Video input:
# #cap = cv2.VideoCapture("1.mp4")
# prevTime = 0
# with mp_face_detection.FaceDetection(model_selection=1) as face_detection:
#   while True:
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
#       break
#
#     #Convert the BGR image to RGB.
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image.flags.writeable = False
#     results = face_detection.process(image)
#
#     # Draw the face detection annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.detections:
#       for detection in results.detections:
#         mp_drawing.draw_detection(image, detection)
#
#     currTime = time.time()
#     fps = 1 / (currTime - prevTime)
#     prevTime = currTime
#     cv2.putText(image, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 196, 255), 2)
#     cv2.imshow('BlazeFace Face Detection', image)
#     if cv2.waitKey(5) & 0xFF == 27:
#       break
# cap.release()
















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

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtCore import QTimer
#
# class TimerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.counter = 0
#         self.label = QLabel('0:00:00', self)
#         self.label.setFixedWidth(70)
#         self.setCentralWidget(self.label)
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_counter)
#         self.timer.start(1000)
#
#     def update_counter(self):
#         self.counter += 1
#         hours, remainder = divmod(self.counter, 3600)
#         minutes, seconds = divmod(remainder, 60)
#         self.label.setText('{}:{:02d}:{:02d}'.format(hours, minutes, seconds))
#
# app = QApplication(sys.argv)
# window = TimerApp()
# window.show()
# sys.exit(app.exec_())




# import random
# from PyQt5 import QtCore, QtGui, QtWidgets
# def addRow(self):
#     data = [random.randint(0, 100) for i in range(2)]
#     # Get the current number of rows
#     row = self.studentsAttendance_tableWidget.rowCount()
#     # Add a new row
#     self.studentsAttendance_tableWidget.insertRow(row)
#     # Add data to the new row
#     for i, item in enumerate(data):
#         table_item = QtWidgets.QTableWidgetItem(str(item))
#         self.studentsAttendance_tableWidget.setItem(row, i, table_item)
#


# import concurrent.futures
# import time
# def function_1():
#     # some computation
#     time.sleep(10)
#     print('ada')
#     return 'addad'
#
# def function_2():
#     # some computation
#     print('adfhfdhjdgyha')
#     return 'result_2'
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#     future_1 = executor.submit(function_1)
#     future_2 = executor.submit(function_2)
#
#     # result_1 = future_1.result()
#     # result_2 = future_2.result()
#
#     # print(result_1)
#     # print(result_2)