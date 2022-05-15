import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QSplitter, QHBoxLayout

from structure.LeftBar import LeftBar
from structure.PresentationScreen import PresentationScreen
from structure.RightBar import RightBar
from structure.layout.ThreeColumns import ThreeColumns
from actions.NewFileAction import NewFileAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Worship Lyrics')
        self.resize(QSize(800, 600))

        self.setCentralWidget(ThreeColumns(LeftBar(), PresentationScreen(), RightBar()))

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(NewFileAction(self))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
