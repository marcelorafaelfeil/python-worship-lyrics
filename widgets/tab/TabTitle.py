import qtawesome as qta
from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPixmap, QPicture

from widgets.layout import Row, Column
from services.utils import PathUtils

style = """
TabTitle > QWidget {
    padding: 5px 0 5px 5px;
    background-color: #282A37;
}
"""

minimize_style = """
border: 0px;
border-right: 1px solid #111111;
"""


class TabTitle(QWidget):
    def __init__(self, text: str, icon=None):
        super(TabTitle, self).__init__()

        title = QLabel(text)

        width_control = QLabel()
        width_control.setFixedWidth(180)
        width_control.setFixedHeight(0)

        layout = Row()

        if icon is not None:
            icon_widget = qta.IconWidget()
            icon_widget.setIcon(icon)
            layout.addWidget(icon_widget)

        layout.addWidget(title)

        column = Column()
        column.addLayout(layout)

        self.setLayout(column)
        self.setStyleSheet(style)

