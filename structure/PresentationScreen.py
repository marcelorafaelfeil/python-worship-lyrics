from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from core import ApplicationContext


class PresentationScreen(QWidget):
    def __init__(self, context: ApplicationContext):
        super(PresentationScreen, self).__init__()
        self.context = context
        self.handle_lyrics = self.context.handleLyrics()

        self.__verseChangedObserver()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(layout)

    def __verseChangedObserver(self):
        self.handle_lyrics.onChangeLyric(self.__changeText)

    def __changeText(self, item):
        print(f'item: {item}')
