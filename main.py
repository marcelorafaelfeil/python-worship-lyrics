import sys

from PyQt6.QtWidgets import QApplication, QWidget
from styles.theme import DarkTheme

from MainWindow import MainWindow
from core import Initializer
from styles.GlobalStyle import global_style


Initializer.start()

app = QApplication(sys.argv)
app.setStyleSheet(global_style)
app.setDesktopSettingsAware(True)
app.setPalette(DarkTheme())

window = MainWindow()
window.show()

app.exec()

