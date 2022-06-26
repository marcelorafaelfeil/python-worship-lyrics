from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidgetItem, QListWidget

from core import ApplicationContext


class CurrentLyricWidget(QWidget):
    def __init__(self, context: ApplicationContext):
        super(CurrentLyricWidget, self).__init__()
        self.setObjectName('currentLyricWidget')

        self.context = context
        self.context.handleLyrics().onChangeLyric(self.onSelectLyric)

        self.lyrics_handle = self.context.handleLyrics()

        self.list = QListWidget()
        self.list.setViewportMargins(0, 0, 0, 0)
        self.list.setWordWrap(True)
        self.list.currentItemChanged.connect(self.onVerseChange)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.list)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.layout)

    def onSelectLyric(self, lyric):
        list_lines = self.lyrics_handle.getCurrentLyricContent()

        self.list.clear()

        for line in list_lines:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, line)
            item.setText(line['content'])

            self.list.addItem(item)

    def onVerseChange(self, current: QListWidgetItem, previous: QListWidgetItem):
        if previous is not None:
            previous_data = previous.data(Qt.ItemDataRole.UserRole)
            previous_data['selected'] = False

        current_data = current.data(Qt.ItemDataRole.UserRole)
        current_data['selected'] = True

        self.lyrics_handle.emitVerseChanged(current)
