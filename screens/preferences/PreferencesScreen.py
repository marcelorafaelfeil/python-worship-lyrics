from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QDialogButtonBox

from .structure import Content, Footer


class PreferencesScreen(QDialog):
    def __init__(self):
        super(PreferencesScreen, self).__init__()
        self.setWindowTitle('Preferências')
        self.setWindowFlags(
            Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMaximizeButtonHint)
        self.setMinimumSize(QSize(900, 700))

        self._renderLayout()

    def _renderLayout(self):
        structure = QVBoxLayout()
        content = QHBoxLayout()
        footer = QHBoxLayout()

        content.addWidget(Content())

        footer.setAlignment(Qt.AlignmentFlag.AlignRight)
        footer.addWidget(Footer(self.accept, self.reject, self.apply))

        structure.addLayout(content, 1)
        structure.addLayout(footer)
        structure.setSpacing(0)
        structure.setContentsMargins(0, 0, 0, 0)

        self.setLayout(structure)

    def accept(self) -> None:
        super(PreferencesScreen, self).accept()

        print('Acertou!')

    def reject(self) -> None:
        super(PreferencesScreen, self).reject()
        print('Rejeitou')

    def apply(self) -> None:
        print('Aplicou em preferências')
