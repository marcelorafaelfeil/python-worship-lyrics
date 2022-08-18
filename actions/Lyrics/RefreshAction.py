from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QKeyCombination

from core import ApplicationContext
from services.utils import PathUtils


class RefreshAction(QAction):
    def __init__(self):
        super(RefreshAction, self).__init__(ApplicationContext.main_window)
        self.setText('Atualizar')
        self.triggered.connect(self._performAction)

        icon = QIcon(PathUtils.icon('refresh_blue.png'))
        self.setIcon(icon)
        self.setShortcut(QKeySequence(QKeyCombination(Qt.KeyboardModifier.ControlModifier, Qt.Key.Key_R)))
        self.setShortcutVisibleInContextMenu(True)

    def _performAction(self):
        print('Atualizou!')
        lyrics_list = ApplicationContext.lyric_handler.refresh()
        ApplicationContext.lyrics_tree.setItems(lyrics_list)
