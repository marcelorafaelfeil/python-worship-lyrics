from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class RightBar(QWidget):
    def __init__(self):
        super(RightBar, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel('RightBar'))
        layout.addWidget(QLabel('RightBar 2'))
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(layout)

