from PyQt6.QtWidgets import QLabel, QGraphicsOpacityEffect


class Label(QLabel):
    def __init__(self, text: str):
        super(Label, self).__init__(text)

    def setDisabled(self, disabled: bool) -> None:
        super(Label, self).setDisabled(disabled)

        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7 if disabled else 1)

        self.setGraphicsEffect(opacity_effect)
