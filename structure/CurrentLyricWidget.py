from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidgetItem, QListWidget

from core import ApplicationContext


class CurrentLyricWidget(QWidget):
    def __init__(self, context: ApplicationContext):
        super(CurrentLyricWidget, self).__init__()
        self.setObjectName('currentLyricWidget')

        self.context = context
        self.context.lyricsHandle().onChangeLyric(self.onSelectLyric)

        self.list = QListWidget()
        self.list.setViewportMargins(0, 0, 0, 0)
        self.list.setWordWrap(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.list)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.layout)

    def onSelectLyric(self, lyric):
        lyrics_handle = self.context.lyricsHandle()
        list_lines = lyrics_handle.getCurrentLyricContent()

        self.list.clear()

        for line in list_lines:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, line)
            item.setText(line['content'])

            self.list.addItem(item)
