import qtawesome
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QKeyCombination

from controller.core import ApplicationContext


def _open_screen():
    ApplicationContext.window_new_lyric.exec()


class NewLyricAction(QAction):
    def __init__(self, parent):
        super(NewLyricAction, self).__init__(parent)

        self.setText('New Lyric')
        self.triggered.connect(_open_screen)
        self.setIcon(QIcon(qtawesome.icon('mdi.file')))

        self.setShortcut(QKeySequence(QKeyCombination(Qt.Modifier.CTRL, Qt.Key.Key_N)))

