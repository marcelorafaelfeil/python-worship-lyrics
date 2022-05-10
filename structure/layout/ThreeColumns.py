from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLayout, QBoxLayout


class ThreeColumns(QHBoxLayout):
    def __init__(self, first_column: QLayout, second_column: QLayout, third_column: QLayout):
        super(ThreeColumns, self).__init__()

        self.firstColumn = first_column
        self.secondColumn = second_column
        self.thirdColumn = third_column

        self.addLayout(first_column)
        self.addLayout(second_column)
        self.addLayout(third_column)
        self.setAlignment(Qt.AlignmentFlag.AlignTop)


