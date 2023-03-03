import logging
import sys

from PyQt6.QtWidgets import QApplication

from MainWindow import MainWindow
from controller.core import Initializer
from view.styles.GlobalStyle import global_style
from view.styles.theme import DarkTheme

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

