from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon

from controller.core import ApplicationContext
from services.utils import PathUtils


class RemoveAction(QAction):
    def __init__(self):
        super(RemoveAction, self).__init__(ApplicationContext.main_window)
        self.setText('Remover')
        self.triggered.connect(self._performAction)

        icon = QIcon(PathUtils.icon('delete_red.png'))
        self.setIcon(icon)
        self.setShortcut(Qt.Key.Key_Backspace)
        self.setShortcutVisibleInContextMenu(True)

    def _performAction(self):
        tree = ApplicationContext.selected_lyrics_tree
        tree.removeSelectedItem()

