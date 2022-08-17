from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QTreeWidget, QTreeWidgetItem, QAbstractItemView, QFrame

from core import ApplicationContext
from widgets.form import SearchInput
from services import LyricSearchService
from . import TreeLyricsWidget


class LyricsWidget(QFrame):
    def __init__(self, list_lyrics):
        super(LyricsWidget, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(SearchInput(lambda value, search_by: self.searchLyrics(value, search_by)))

        self.lyrics_tree = TreeLyricsWidget(["Título", "Autor"], list_lyrics)
        self.lyrics_tree.onSelectItem(lambda item: self.addToSelectedLyrics(item))
        self.lyrics_tree.onRefresh(self.refreshLyrics)

        layout.addWidget(self.lyrics_tree, 1)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setObjectName('Lyrics')

    def refreshLyrics(self):
        lyrics_list = ApplicationContext.lyric_handler.refresh()
        self.lyrics_tree.setItems(lyrics_list)


    def addToSelectedLyrics(self, item):
        ApplicationContext.lyric_handler.addToSelectedLyrics(item)

    def searchLyrics(self, value, search_by):
        handle = ApplicationContext.lyric_handler
        search_service = LyricSearchService(handle.getLyricsList(), value)
        result = []

        if search_by == 0:
            result = search_service.searchByName()
        elif search_by == 1:
            result = search_service.searchByAuthor()
        elif search_by == 2:
            result = search_service.searchByLyric()

        self.lyrics_tree.clear()
        self.lyrics_tree.setItems(result)
