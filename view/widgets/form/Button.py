from PyQt6.QtWidgets import QPushButton, QGraphicsOpacityEffect


class Button(QPushButton):
    def __init__(self, text: str = ""):
        super(Button, self).__init__(text)

    def setDisabled(self, disabled: bool) -> None:
        super(QPushButton, self).setDisabled(disabled)

        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7 if disabled else 1)

        self.setGraphicsEffect(opacity_effect)
