import logging
import sys

from PyQt6.QtWidgets import QApplication

from MainWindow import MainWindow
from core import Initializer
from styles.GlobalStyle import global_style
from styles.theme import DarkTheme

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

app = QApplication(sys.argv)

app.setStyleSheet(global_style)
app.setDesktopSettingsAware(True)
app.setPalette(DarkTheme())

Initializer.start()

window = MainWindow()
window.show()

test = app.exec()

