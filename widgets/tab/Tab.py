import typing

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QDockWidget, QScrollArea

from . import TabTitle

style_dockwidget = """
QDockWidget#tab QWidget {
    background-color: #191A22;
}
"""

internal_body_style = """
background-color: #191A22;
border: 0px;
"""


class Tab(QDockWidget):
    def __init__(self, parent: typing.Optional[QWidget] = None):
        super(Tab, self).__init__(parent)

        self.body: QWidget | None = None

        self.setObjectName('tab')
        self.setStyleSheet(style_dockwidget)
        self.setFeatures(self.DockWidgetFeature.NoDockWidgetFeatures
                         | self.DockWidgetFeature.DockWidgetMovable)

    def setTitleBarWidget(self, title: TabTitle) -> None:
        super().setTitleBarWidget(title)

    def setBody(self, body_widget: QWidget, scroll: bool = True):
        body_widget.setContentsMargins(0, 0, 0, 0)
        body_widget.setStyleSheet(internal_body_style)

        if scroll:
            area = QScrollArea()
            area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            area.setWidget(body_widget)
            self.body = area
        else:
            self.body = body_widget

        self.setWidget(self.body)

    def minimize(self):
        if self.body is not None:
            self.body.hide()

        self.setWindowState(Qt.WindowState.WindowMinimized)

    def maximize(self):
        if self.body is not None:
            self.body.show()

        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.repaint()

