import logging

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from core import ApplicationContext


class PresentationScreen(QWidget):
    def __init__(self):
        super(PresentationScreen, self).__init__()
        self.handle_lyrics = ApplicationContext.lyric_handler

        self.__verseChangedObserver()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(layout)

    def __verseChangedObserver(self):
        self.handle_lyrics.on_change_lyric(self.__changeText)

    def __changeText(self, item):
        logging.debug('item: %s', item)


