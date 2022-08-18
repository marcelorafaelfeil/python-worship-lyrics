import sys

from PyQt6.QtWidgets import QApplication
from styles.theme import DarkTheme

from MainWindow import MainWindow
from core import Initializer

app_style = """
QMainWindow::separator {
    border: 2px solid #111111;
}
"""


Initializer.start()

app = QApplication(sys.argv)
app.setStyleSheet(app_style)
app.setDesktopSettingsAware(True)
app.setPalette(DarkTheme())

window = MainWindow()
window.show()

app.exec()

