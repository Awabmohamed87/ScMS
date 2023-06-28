from general_lib import *
from config import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage,QPixmap
import cv2
import threading

class cameraConfigPage():
    def __init__(self, mainSelf):
        self.mainSelf = mainSelf
        self.GUI_initialize_Objects()
        self.GUI_connect_buttons()
        self.currentSessionPort=self.mainSelf.configuration.sessionCameraPort
        self.currentFaceIDPort=self.mainSelf.configuration.faceIDCameraPort
        self.isThreadActive = True
        self.liveViewCamera = threading.Thread(target=self.liveView_worker)
        self.liveViewCamera.start()

    def GUI_initialize_Objects(self):
        # ------------ Pages ------------
        self.cameraConfig_widget = self.mainSelf.findChild(QtWidgets.QWidget, "cameraConfig_widget")
        # ------------ Objects ------------
        self.sessionCameraConfig_Label = self.mainSelf.findChild(QtWidgets.QLabel, "sessionCameraConfig_Label")
        self.loginCameraConfig_Label = self.mainSelf.findChild(QtWidgets.QLabel, "loginCameraConfig_Label")
        # ------------ Buttons ------------
        self.cameraConfig_Back_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "cameraConfig_Back_btn")
        self.cameraConfig_Back_btn.setFocusPolicy(Qt.NoFocus)

        self.changeSessionCamera_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "changeSessionCamera_btn")
        self.changeSessionCamera_btn.setFocusPolicy(Qt.NoFocus)
        self.changeLoginCamera_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "changeLoginCamera_btn")
        self.changeLoginCamera_btn.setFocusPolicy(Qt.NoFocus)
        self.cameraConfig_save_btn = self.mainSelf.findChild(QtWidgets.QPushButton, "cameraConfig_save_btn")
        self.cameraConfig_save_btn.setFocusPolicy(Qt.NoFocus)
    def GUI_connect_buttons(self):
        self.cameraConfig_Back_btn.clicked.connect(self.cameraConfig_Back_btn_clicked)
        self.changeSessionCamera_btn.clicked.connect(self.changeSessionCamera_btn_clicked)
        self.changeLoginCamera_btn.clicked.connect(self.changeLoginCamera_btn_clicked)
        self.cameraConfig_save_btn.clicked.connect(self.cameraConfig_save_btn_clicked)
    # ------------------- Buttons Clicked -------------------
    def navigate(self, currnetPage, destinationPage):
        currnetPageObj = self.mainSelf.findChild(QtWidgets.QWidget, currnetPage)
        currnetPageObj.hide()
        destinationPageObj = self.mainSelf.findChild(QtWidgets.QWidget, destinationPage)
        destinationPageObj.show()
        destinationPageObj.raise_()

    def cameraConfig_Back_btn_clicked(self):
        self.isThreadActive = False
        self.liveViewCamera.join()
        self.mainSelf.configuration.changeCamerasPorts(sessionPort=self.currentSessionPort, faceIDPort=self.currentFaceIDPort)
        self.navigate("cameraConfig_widget", "homeManagerScreen_widget")
    def changeSessionCamera_btn_clicked(self):
        self.isThreadActive=False
        self.liveViewCamera.join()
        self.mainSelf.configuration.switchCameras(isSession=True)
        self.isThreadActive = True
        self.liveViewCamera = threading.Thread(target=self.liveView_worker)
        self.liveViewCamera.start()

    def changeLoginCamera_btn_clicked(self):
        self.isThreadActive = False
        self.liveViewCamera.join()
        self.mainSelf.configuration.switchCameras(isSession=False)
        self.isThreadActive = True
        self.liveViewCamera = threading.Thread(target=self.liveView_worker)
        self.liveViewCamera.start()
    def cameraConfig_save_btn_clicked(self):
        self.isThreadActive = False
        self.liveViewCamera.join()
        self.navigate("cameraConfig_widget", "homeManagerScreen_widget")
    def liveView_worker(self):
        if self.mainSelf.configuration.sessionCameraPort == self.mainSelf.configuration.faceIDCameraPort:
            self.Capture = cv2.VideoCapture(self.mainSelf.configuration.sessionCameraPort)
            while self.isThreadActive:
                _, Image = self.Capture.read()
                # Image = cv2.resize(Image, (680,383), interpolation = cv2.INTER_AREA)
                Image = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_BGR888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.sessionCameraConfig_Label.setPixmap(QPixmap.fromImage(Pic))
                self.loginCameraConfig_Label.setPixmap(QPixmap.fromImage(Pic))
            self.Capture.release()
        else:
            self.CaptureSession = cv2.VideoCapture(self.mainSelf.configuration.sessionCameraPort)
            self.CaptureFaceID = cv2.VideoCapture(self.mainSelf.configuration.faceIDCameraPort)
            while self.isThreadActive:
                _, Image = self.CaptureSession.read()
                Image = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_BGR888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.sessionCameraConfig_Label.setPixmap(QPixmap.fromImage(Pic))

                _, Image = self.CaptureFaceID.read()
                Image = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_BGR888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.loginCameraConfig_Label.setPixmap(QPixmap.fromImage(Pic))
            self.CaptureSession.release()
            self.CaptureFaceID.release()