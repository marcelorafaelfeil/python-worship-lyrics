from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QTreeWidget, QTreeWidgetItem, QWidget, QAbstractItemView

from core import ApplicationContext
from widgets.form import SearchInput
from services import LyricSearchService


# TODO: It's necessary to fix the height of the widget


class LyricsWidget(QWidget):
    def __init__(self, context: ApplicationContext, list_lyrics):
        super(LyricsWidget, self).__init__()

        self.context = context

        layout = QVBoxLayout()
        layout.addWidget(SearchInput(lambda value, search_by: self.searchLyrics(value, search_by)))

        self.lyrics_tree = QTreeWidget()
        self.lyrics_tree.setColumnCount(2)
        self.lyrics_tree.setIndentation(0)
        self.lyrics_tree.setSortingEnabled(True)
        self.lyrics_tree.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.lyrics_tree.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.lyrics_tree.setDragEnabled(True)
        self.lyrics_tree.setHeaderLabels(["Título", "Autor"])

        items = self.parseToTreeItems(list_lyrics)

        self.lyrics_tree.insertTopLevelItems(0, items)
        self.lyrics_tree.doubleClicked.connect(self.addToSelectedLyrics)

        layout.addWidget(self.lyrics_tree, 1)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def addToSelectedLyrics(self, index):
        widget_item = self.lyrics_tree.itemFromIndex(index)
        item = widget_item.data(0, Qt.ItemDataRole.UserRole)

        self.context.lyricsHandle().addToSelectedLyrics(item)

    def parseToTreeItems(self, list_lyrics):

        items = []

        for lyric in list_lyrics:
            item = QTreeWidgetItem([lyric['name'], lyric['author']])
            item.setData(0, Qt.ItemDataRole.UserRole, lyric)
            items.append(item)

        return items

    def searchLyrics(self, value, search_by):
        handle = self.context.lyricsHandle()
        search_service = LyricSearchService(handle.getLyricsList(), value)
        result = []

        if search_by == 0:
            result = search_service.searchByName()
        elif search_by == 1:
            result = search_service.searchByAuthor()
        elif search_by == 2:
            result = search_service.searchByLyric()

        items = self.parseToTreeItems(result)

        self.lyrics_tree.clear()
        self.lyrics_tree.insertTopLevelItems(0, items)
