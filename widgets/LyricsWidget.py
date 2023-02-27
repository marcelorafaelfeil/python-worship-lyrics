from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QFrame

from core import ApplicationContext
from services import LyricSearchService
from services.LyricSearchService import LyricSearchService
from widgets.form import SearchInput
from . import TreeLyricsWidget


class LyricsWidget(QFrame):
    def __init__(self):
        super(LyricsWidget, self).__init__()

        self.lyrics_service = ApplicationContext.lyrics_service
        self.lyrics_tree = TreeLyricsWidget(["Título", "Autor"])

        ApplicationContext.lyrics_tree = self.lyrics_tree

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        search_input = SearchInput()
        search_input.search.subscribe(self.search_lyrics)

        layout.addWidget(search_input)
        layout.addWidget(self.lyrics_tree)

        self.setLayout(layout)
        self.setObjectName('Lyrics')

    def search_lyrics(self, data):
        search_service = LyricSearchService(data['value'])
        result = []

        if data['search_by'] == 0:
            result = search_service.search_by_name()
        elif data['search_by'] == 1:
            result = search_service.search_by_author()
        elif data['search_by'] == 2:
            result = search_service.search_by_lyric()

        self.lyrics_tree.clear()
        self.lyrics_tree.set_items(result)
