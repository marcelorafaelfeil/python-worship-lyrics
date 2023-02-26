from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from screens.preferences.forms import SettingsForm


class HTTPForm(SettingsForm):
    def __init__(self):
        super(SettingsForm, self).__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel('HTTP form!'))

        self.setLayout(layout)
