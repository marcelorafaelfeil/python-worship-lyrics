from typing import List

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidgetItem, QListWidget

from core import ApplicationContext
from entity.Lyric import Lyric
from entity.LyricLine import LyricLine
from styles import CurrentLyricStyle


class CurrentLyricWidget(QWidget):
    def __init__(self):
        super(CurrentLyricWidget, self).__init__()
        self.setObjectName('currentLyricWidget')

        self.lyrics_service = ApplicationContext.lyrics_service

        self.list = QListWidget()
        self.list.setViewportMargins(0, 0, 0, 0)
        self.list.setWordWrap(True)
        self.list.setStyleSheet(CurrentLyricStyle.list_style)
        self.list.currentItemChanged.connect(self.on_select_verse)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.list)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.lyrics_service.select_lyric.subscribe(self.on_select_lyric)

        self.setLayout(self.layout)

    def on_select_lyric(self, lyric: Lyric):
        list_lines: List[LyricLine] = self.lyrics_service.read_lyric(lyric)

        self.list.clear()

        for line in list_lines:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, line)
            item.setText(line.content)

            self.list.addItem(item)

    def on_select_verse(self, current: QListWidgetItem, previous: QListWidgetItem):
        if previous is not None:
            previous_data = previous.data(Qt.ItemDataRole.UserRole)
            previous_data.selected = False

        if current is not None:
            current_data = current.data(Qt.ItemDataRole.UserRole)
            current_data.selected = True

            self.lyrics_service.project_verse.on_next(current_data)
