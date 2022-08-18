import sys

import PyQt6.QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from styles.theme import DarkTheme

from MainWindow import MainWindow
from core import Initializer

app_style = """
QMainWindow::separator {
    border: 2px solid #111111;
}
QHeaderView::section {
    background-color: #282A37;
    color: #EFEFEF;
}
"""


Initializer.start()

app = QApplication(sys.argv)
app.setStyleSheet(app_style)
app.setDesktopSettingsAware(True)
app.setStyle('macOS')
app.setPalette(DarkTheme())

window = MainWindow()
window.show()

app.exec()

