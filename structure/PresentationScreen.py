from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class PresentationScreen(QWidget):
    def __init__(self):
        super(PresentationScreen, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Presentation'))
        layout.addWidget(QLabel('Presentation 2'))
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(layout)

