from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QKeyCombination
from PyQt6.QtWidgets import QDialogButtonBox

from core import ApplicationContext


class PreferencesAction(QAction):
    def __init__(self, parent):
        super(PreferencesAction, self).__init__(parent)

        self.setText('Preferências')
        self.triggered.connect(self._openPreferencesScreen)

        self.setShortcut(QKeySequence(QKeyCombination(Qt.Modifier.CTRL, Qt.Key.Key_Comma)))

    def _openPreferencesScreen(self):
        result = ApplicationContext.window_preference.exec()

        print(result)

        if result:
            print('Returnou OK!')
        else:
            print('Será que cancelou?')

