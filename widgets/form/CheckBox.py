from PyQt6.QtWidgets import QCheckBox
from styles import FormStyle


class CheckBox(QCheckBox):
    def __init__(self, text: str = ''):
        super(CheckBox, self).__init__(text)

        self.setStyleSheet(FormStyle.checkbox_style)
