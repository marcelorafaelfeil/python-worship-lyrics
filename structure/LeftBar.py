from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel


class LeftBar(QWidget):
    def __init__(self):
        super(LeftBar, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel('LeftBar'))
        layout.addWidget(QLabel('LeftBar 2'))
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(layout)

