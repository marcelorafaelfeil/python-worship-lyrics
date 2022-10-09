from PyQt6.QtWidgets import QSpinBox, QGraphicsOpacityEffect
from styles import FormStyle


class SpinBox(QSpinBox):

    def __init__(self, value: int = None, maximum: int = 9999):
        super(SpinBox, self).__init__()

        self.setMaximum(maximum)
        self.setValue(value)
        self.setStyleSheet(FormStyle.spinbox_style)

    def setDisabled(self, disabled: bool) -> None:
        super(SpinBox, self).setDisabled(disabled)

        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7 if disabled else 1)

        self.setGraphicsEffect(opacity_effect)
