from PyQt6.QtWidgets import QLineEdit, QGraphicsOpacityEffect
from styles import FormStyle
from typing import Union


class Input(QLineEdit):
    def __init__(self, value: Union[str, None] = None, placeholder: str = ''):
        super(Input, self).__init__()
        self.setPlaceholderText(placeholder)

        if value is not None:
            self.setText(value)

        self.setObjectName('Input')
        self.setStyleSheet(FormStyle.input_style)

    def setDisabled(self, disabled: bool) -> None:
        super(Input, self).setDisabled(disabled)

        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7 if disabled else 1)

        self.setGraphicsEffect(opacity_effect)
