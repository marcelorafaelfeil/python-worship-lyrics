from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from core import ApplicationContext


class PresentationScreen(QWidget):
    def __init__(self, context: ApplicationContext):
        super(PresentationScreen, self).__init__()
        self.context = context
        self.handle_lyrics = self.context.lyricsHandle()

        self.__verseChangedObserver()

        button = QPushButton("Play")
        button.clicked.connect(self._startServer)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(button)

        self.setLayout(layout)

    def __verseChangedObserver(self):
        self.handle_lyrics.onChangeLyric(self.__changeText)

    def __changeText(self, item):
        print(f'item: {item}')

    def _startServer(self):
        websocket = self.context.getWebsocket()
        websocket.clientConnect()

