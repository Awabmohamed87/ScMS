import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from faceRecognation_lib.simple_facerec import SimpleFacerec
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

class attentionCamera_Worker(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(1)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                FlippedImage = cv2.flip(frame, 1)
                face_locations, face_names = sfr.detect_known_faces(FlippedImage)
                for face_loc, name in zip(face_locations, face_names):
                    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                    cv2.putText(FlippedImage, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)
                    cv2.rectangle(FlippedImage, (x1, y1), (x2, y2), (0, 200, 0), 4)

                Image = cv2.cvtColor(FlippedImage, cv2.COLOR_BGR2RGB)
                # FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
