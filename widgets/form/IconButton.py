from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QGraphicsOpacityEffect, QToolButton


style = """
QToolButton {
    border-radius: 3px;
    padding: 3px;
}
QToolButton:hover {
    background-color: rgba(0, 0, 0, 0.3);
}
"""


class IconButton(QToolButton):
    def __init__(self, icon: QIcon):
        super(IconButton, self).__init__()
        self.setIcon(icon)
        self.setStyleSheet(style)

    def setDisabled(self, disabled: bool) -> None:
        super(QToolButton, self).setDisabled(disabled)

        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7 if disabled else 1)

        self.setGraphicsEffect(opacity_effect)
