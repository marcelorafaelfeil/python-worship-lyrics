from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QFrame

from core import ApplicationContext
from services import LyricSearchService
from widgets.form import SearchInput
from . import TreeLyricsWidget


class LyricsWidget(QFrame):
    def __init__(self, list_lyrics):
        super(LyricsWidget, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(SearchInput(lambda value, search_by: self.searchLyrics(value, search_by)))

        self.lyrics_tree = TreeLyricsWidget(["Título", "Autor"], list_lyrics)
        self.lyrics_tree.onSelectItem(lambda item: self.addToSelectedLyrics(item))

        ApplicationContext.lyrics_tree = self.lyrics_tree

        layout.addWidget(self.lyrics_tree)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
        self.setObjectName('Lyrics')

    def addToSelectedLyrics(self, item):
        ApplicationContext.lyric_handler.add_to_selected_lyrics(item)

    def searchLyrics(self, value, search_by):
        handle = ApplicationContext.lyric_handler
        search_service = LyricSearchService(handle.get_lyrics_list(), value)
        result = []

        if search_by == 0:
            result = search_service.searchByName()
        elif search_by == 1:
            result = search_service.searchByAuthor()
        elif search_by == 2:
            result = search_service.searchByLyric()

        self.lyrics_tree.clear()
        self.lyrics_tree.setItems(result)
