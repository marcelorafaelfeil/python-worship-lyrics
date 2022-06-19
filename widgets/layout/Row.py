from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLayout


class Row(QHBoxLayout):
    def __init__(self):
        super(Row, self).__init__()

        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

