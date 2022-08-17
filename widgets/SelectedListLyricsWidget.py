from core import ApplicationContext
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QTreeWidget, QAbstractItemView, QTreeWidgetItem


class SelectedListLyricsWidget(QFrame):
    def __init__(self):
        super().__init__()

        self._onSelectLyric()

        layout = QVBoxLayout()

        self.lyrics_tree = QTreeWidget()
        self.lyrics_tree.setColumnCount(2)
        self.lyrics_tree.setIndentation(0)
        self.lyrics_tree.setSortingEnabled(True)
        self.lyrics_tree.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)
        self.lyrics_tree.setHeaderLabels(["Música", "Autor"])
        self.lyrics_tree.doubleClicked.connect(self.selectItem)

        layout.addWidget(self.lyrics_tree, 1)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def selectItem(self, index):
        widget_item = self.lyrics_tree.itemFromIndex(index)
        item = widget_item.data(0, Qt.ItemDataRole.UserRole)
        ApplicationContext.lyric_handler.setSelectedLyric(item)

    def addNewItemToSelected(self, item):
        widget_item = QTreeWidgetItem([item['name'], item['author']])
        widget_item.setData(0, Qt.ItemDataRole.UserRole, item)
        self.lyrics_tree.addTopLevelItem(widget_item)

    def _onSelectLyric(self):
        lyric_handle = ApplicationContext.lyric_handler
        lyric_handle.onAddToSelectedLyric(self.addNewItemToSelected)


