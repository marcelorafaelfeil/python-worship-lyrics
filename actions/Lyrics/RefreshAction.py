from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QKeyCombination

from core import ApplicationContext
from services.utils import PathUtils


def _perform_action():
    ApplicationContext.lyrics_service.refresh()


class RefreshAction(QAction):
    def __init__(self):
        super(RefreshAction, self).__init__(ApplicationContext.main_window)
        self.setText('Atualizar')
        self.triggered.connect(_perform_action)

        icon = QIcon(PathUtils.icon('refresh_blue.png'))
        self.setIcon(icon)
        self.setShortcut(QKeySequence(QKeyCombination(Qt.KeyboardModifier.ControlModifier, Qt.Key.Key_R)))
        self.setShortcutVisibleInContextMenu(True)
