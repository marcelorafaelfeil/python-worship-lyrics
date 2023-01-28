from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout

from .structure import Content, Footer
from styles.DialogStyle import dialog_style
from core import ApplicationContext


class PreferencesScreen(QDialog):
    _footer: Footer

    def __init__(self):
        super(PreferencesScreen, self).__init__()

        ApplicationContext.settings.startConfiguration()

        self.setWindowTitle('Preferências')
        self.setWindowFlags(
            Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMaximizeButtonHint)
        self.setMinimumSize(QSize(900, 700))
        self.setStyleSheet(dialog_style)

        self._renderLayout()

        ApplicationContext.settings.has_settings_changes.subscribe(self.enableApplyButton)

    def enableApplyButton(self, enable):
        if enable:
            self._footer.enableApplyButton()
        else:
            self._footer.disableApplyButton()

    def _renderLayout(self):
        structure = QVBoxLayout()
        content = QHBoxLayout()
        footer_layout = QHBoxLayout()
        self._footer = Footer(self.accept, self.reject, self.apply)

        self._footer.disableApplyButton()

        content.addWidget(Content())

        footer_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        footer_layout.addWidget(self._footer)

        structure.addLayout(content, 1)
        structure.addLayout(footer_layout)
        structure.setSpacing(0)
        structure.setContentsMargins(0, 0, 0, 0)

        self.setLayout(structure)

    def accept(self) -> None:
        super(PreferencesScreen, self).accept()
        self.apply()

    def reject(self) -> None:
        super(PreferencesScreen, self).reject()

    def apply(self) -> None:
        ApplicationContext.settings.save()
        self._footer.disableApplyButton()
