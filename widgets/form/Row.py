from PyQt6.QtWidgets import QHBoxLayout


class Row(QHBoxLayout):
    def __init__(self):
        super(Row, self).__init__()

        self.setContentsMargins(0, 15, 0, 0)
        self.setSpacing(0)
