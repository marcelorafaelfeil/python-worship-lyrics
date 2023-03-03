import qtawesome
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QKeyCombination

from controller.core import ApplicationContext


class PreferencesAction(QAction):
    def __init__(self, parent):
        super(PreferencesAction, self).__init__(parent)

        self.setText('Preferências')
        self.triggered.connect(self.open_screen)
        self.setIcon(QIcon(qtawesome.icon('mdi6.cog')))

        self.setShortcut(QKeySequence(QKeyCombination(Qt.Modifier.CTRL, Qt.Key.Key_Comma)))

    def open_screen(self):
        ApplicationContext.window_preference.exec()
