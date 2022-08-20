from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class WebSocketForm(QWidget):
    def __init__(self):
        super(WebSocketForm, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel('WebSocket form!'))

        self.setLayout(layout)
