from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QTreeWidget, QAbstractItemView, QTreeWidgetItem

from core import ApplicationContext
from . import TreeLyricsWidget


class SelectedListLyricsWidget(QFrame):
    def __init__(self):
        super().__init__()

        self._startEvents()

        layout = QVBoxLayout()

        self.lyrics_tree = TreeLyricsWidget(['Título', 'Autor'])
        self.lyrics_tree.onSelectItem(self.selectItem)

        layout.addWidget(self.lyrics_tree)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def selectItem(self, item):
        ApplicationContext.lyric_handler.setSelectedLyric(item)

    def addNewItemToSelected(self, item):
        self.lyrics_tree.addItem([item['name'], item['author']], item)

    def _onSelectLyricEvent(self):
        lyric_handle = ApplicationContext.lyric_handler
        lyric_handle.onAddToSelectedLyric(self.addNewItemToSelected)

    def _startEvents(self):
        self._onSelectLyricEvent()


