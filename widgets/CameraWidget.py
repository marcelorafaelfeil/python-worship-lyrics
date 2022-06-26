from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtMultimedia import QMediaDevices, QCamera, QCameraDevice, QMediaCaptureSession, QImageCapture
from PyQt6.QtMultimediaWidgets import QVideoWidget


class CameraWidget(QWidget):
    def __init__(self):
        super(CameraWidget, self).__init__()

        self._startCamera()

    def _startCamera(self):
        self.camera_device = CameraWidget.getAvailableCameras()[1]
        self.camera = QCamera(self.camera_device)

        self.capture_session = QMediaCaptureSession()
        self.viewfinder = QVideoWidget()
        self.viewfinder.setAspectRatioMode(Qt.AspectRatioMode.IgnoreAspectRatio)

        self.capture_session.setCamera(self.camera)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.camera_device.description()))
        layout.addWidget(self.viewfinder)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.capture_session.setVideoOutput(self.viewfinder)

        self.setLayout(layout)
        self.camera.start()
        self.viewfinder.sizeHint()

    @staticmethod
    def getAvailableCameras() -> [QCameraDevice]:
        cameras = QMediaDevices.videoInputs()
        return cameras
