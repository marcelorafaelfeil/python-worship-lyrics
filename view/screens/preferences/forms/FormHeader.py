from PyQt6.QtWidgets import QFrame, QLabel, QHBoxLayout
from view.styles import PreferencesStyle as styles


class FormHeader(QFrame):
    def __init__(self, text: str):
        super(FormHeader, self).__init__()

        layout = QHBoxLayout()
        layout.addWidget(QLabel(text))
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setObjectName('HeaderForm')
        self.setStyleSheet(styles.header_style)
