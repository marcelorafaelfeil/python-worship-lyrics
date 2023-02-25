from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout

from core import ApplicationContext
from . import TreeSelectedLyricsWidget


class SelectedListLyricsWidget(QFrame):
    def __init__(self):
        super().__init__()

        self._startEvents()

        layout = QVBoxLayout()

        self.lyrics_tree = TreeSelectedLyricsWidget(['Título', 'Autor'])
        self.lyrics_tree.onSelectItem(self.selectItem)
        self.lyrics_tree.setOnFocus(self.controlMenuStatusFocusIn)
        self.lyrics_tree.setOnFocusOut(self.controlMenuStatusFocusOut)

        ApplicationContext.selected_lyrics_tree = self.lyrics_tree

        layout.addWidget(self.lyrics_tree)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def controlMenuStatusFocusIn(self):
        window = ApplicationContext.main_window
        window.remove_lyric_menu.setEnabled(True)

    def controlMenuStatusFocusOut(self):
        window = ApplicationContext.main_window
        window.remove_lyric_menu.setEnabled(False)

    def selectItem(self, item):
        ApplicationContext.lyric_handler.set_selected_lyric(item)

    def addNewItemToSelected(self, item):
        self.lyrics_tree.addItem([item['name'], item['author']], item)

    def _onSelectLyricEvent(self):
        lyric_handle = ApplicationContext.lyric_handler
        lyric_handle.on_add_to_selected_lyric(self.addNewItemToSelected)

    def _startEvents(self):
        self._onSelectLyricEvent()


