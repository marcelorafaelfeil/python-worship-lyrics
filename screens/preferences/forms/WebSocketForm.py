from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from .FormHeader import FormHeader


class WebSocketForm(QWidget):
    def __init__(self):
        super(WebSocketForm, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(FormHeader('WebSocket'))
        layout.addWidget(self._renderForm(), 1)

        self.setLayout(layout)

    def _renderForm(self) -> QWidget:
        return QWidget()
