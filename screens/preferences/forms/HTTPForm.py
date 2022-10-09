from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class HTTPForm(QWidget):
    def __init__(self):
        super(HTTPForm, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel('HTTP form!'))

        self.setLayout(layout)
