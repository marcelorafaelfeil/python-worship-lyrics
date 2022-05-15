from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QSplitter


class ThreeColumns(QSplitter):
    def __init__(self, first_column: QWidget, second_column: QWidget, third_column: QWidget):
        super(ThreeColumns, self).__init__()

        self.firstColumn = first_column
        self.secondColumn = second_column
        self.thirdColumn = third_column

        self.addWidget(first_column)
        self.addWidget(second_column)
        self.addWidget(third_column)

        self.setOrientation(Qt.Orientation.Horizontal)



