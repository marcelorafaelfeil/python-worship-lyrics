from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHeaderView, QTreeWidget, QTreeWidgetItem, QWidget, QAbstractItemView

# TODO: It's necessary to fix the height of the widget


class LyricsWidget(QWidget):
    def __init__(self, list_lyrics):
        super(LyricsWidget, self).__init__()

        layout = QVBoxLayout()

        lyrics_tree = QTreeWidget()
        lyrics_tree.setColumnCount(2)
        lyrics_tree.setIndentation(0)
        lyrics_tree.setSortingEnabled(True)
        lyrics_tree.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        lyrics_tree.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        lyrics_tree.setDragEnabled(True)
        lyrics_tree.setHeaderLabels(["Música", "Autor"])

        items = []

        for lyric in list_lyrics:
            item = QTreeWidgetItem([lyric['file_name'], lyric['author']])
            item.setData(0, Qt.ItemDataRole.UserRole, lyric)
            items.append(item)

        lyrics_tree.insertTopLevelItems(0, items)

        layout.addWidget(lyrics_tree)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

