import sys

from PyQt6.QtWidgets import QApplication, QWidget
from styles.theme import DarkTheme

from MainWindow import MainWindow
from core import Initializer
from screens.preferences import PreferencesScreen
from styles.GlobalStyle import global_style


app = QApplication(sys.argv)

app.setStyleSheet(global_style)
app.setDesktopSettingsAware(True)
app.setPalette(DarkTheme())

Initializer.start()

window = PreferencesScreen()
# window = MainWindow()
window.show()

test = app.exec()

