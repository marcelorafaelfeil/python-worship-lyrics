from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout

from core import ApplicationContext
from entity.Lyric import Lyric
from . import TreeSelectedLyricsWidget


class SelectedListLyricsWidget(QFrame):
    def __init__(self):
        super().__init__()

        self.window = ApplicationContext.main_window

        self.lyrics_service = ApplicationContext.lyrics_service
        self.lyrics_service.prepare_lyric.subscribe(self.add_new_item_to_selected)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)

        self.lyrics_tree = TreeSelectedLyricsWidget(['Título', 'Autor'])
        self.lyrics_tree.onSelectItem(self.project_lyric)

        ApplicationContext.selected_lyrics_tree = self.lyrics_tree

        layout.addWidget(self.lyrics_tree)

        self.setLayout(layout)

    def project_lyric(self, item: Lyric):
        self.lyrics_service.select_lyric.on_next(item)

    def add_new_item_to_selected(self, item: Lyric):
        self.lyrics_tree.addItem([item.name, item.author], item)
