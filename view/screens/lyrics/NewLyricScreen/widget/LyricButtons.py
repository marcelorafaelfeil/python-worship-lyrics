from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from view.widgets.form import Button


class LyricButtons(QWidget):
    def __init__(self, on_uppercase, on_lowercase):
        super().__init__()

        self.on_uppercase = on_uppercase
        self.on_lowercase = on_lowercase

        layout = QVBoxLayout()
        layout.addWidget(self._render_to_uppercase_button())
        layout.addWidget(self._render_to_lowercase_button())
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(15, 72, 0, 0)

        self.setLayout(layout)

    def _render_to_uppercase_button(self):
        button = Button('Converter para maiúsculo')
        button.clicked.connect(self.on_uppercase)
        return button

    def _render_to_lowercase_button(self):
        button = Button('Converter para minúsculo')
        button.clicked.connect(self.on_lowercase)
        return button
