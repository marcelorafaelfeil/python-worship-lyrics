from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel

from .structure import Content


class PreferencesScreen(QDialog):
    def __init__(self):
        super(PreferencesScreen, self).__init__()
        self.setWindowTitle('Preferências')
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMaximizeButtonHint)
        self.setMinimumSize(QSize(900, 700))
        self._renderLayout()

    def _renderLayout(self):
        structure = QVBoxLayout()
        content = QHBoxLayout()
        footer = QHBoxLayout()

        content.addWidget(Content())
        footer.addWidget(QLabel('footer'))

        structure.addLayout(content, 1)
        structure.addLayout(footer)
        structure.setSpacing(0)
        structure.setContentsMargins(0, 0, 0, 0)

        self.setLayout(structure)

