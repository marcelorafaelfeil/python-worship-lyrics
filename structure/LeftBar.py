from PyQt6.QtWidgets import QHBoxLayout, QLabel


class LeftBar(QHBoxLayout):
    def __init__(self):
        super(LeftBar, self).__init__()

        self.addWidget(QLabel('Teste'))