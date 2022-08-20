from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QKeyCombination

from core import ApplicationContext


class PreferencesAction(QAction):
    def __init__(self, parent):
        super(PreferencesAction, self).__init__(parent)

        self.setText('Preferências')
        self.triggered.connect(self._openPreferencesScreen)

        self.setShortcut(QKeySequence(QKeyCombination(Qt.Modifier.CTRL, Qt.Key.Key_Comma)))

    def _openPreferencesScreen(self):
        ApplicationContext.window_preference.exec()
