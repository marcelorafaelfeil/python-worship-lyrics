import logging

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from core import ApplicationContext


class PresentationScreen(QWidget):
    def __init__(self):
        super(PresentationScreen, self).__init__()
        self.lyrics_service = ApplicationContext.lyrics_service

        self.lyrics_service.project_verse.subscribe(self._changeText)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(layout)

    def _changeText(self, item):
        logging.debug('item: %s', item)


