from PyQt6.QtWidgets import QWidget, QLabel

from widgets.layout import Row, Column

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
    def __init__(self, text: str):
        super(TabTitle, self).__init__()

        title = QLabel(text)

        width_control = QLabel()
        width_control.setFixedWidth(180)
        width_control.setFixedHeight(0)

        layout = Row()
        layout.addWidget(title, 1)

        column = Column()
        column.addLayout(layout)

        self.setLayout(column)
        self.setStyleSheet(style)

