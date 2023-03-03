from PyQt6.QtWidgets import QRadioButton, QGraphicsOpacityEffect
from view.styles import FormStyle


class RadioButton(QRadioButton):
    def __init__(self, text: str = ''):
        super(RadioButton, self).__init__(text)

        self.setStyleSheet(FormStyle.radiobutton_style)

    def setDisabled(self, disabled: bool) -> None:
        super(RadioButton, self).setDisabled(disabled)

        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7 if disabled else 1)

        self.setGraphicsEffect(opacity_effect)
