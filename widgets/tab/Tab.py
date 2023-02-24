import typing

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QDockWidget, QScrollArea, QMainWindow
from services.utils import DataUtils

from .TabTitle import TabTitle

internal_body_style = """
border: 0px;
"""


class Tab(QDockWidget):
    _default_widget_flags = Qt.WindowType.Widget

    def __init__(self, parent: typing.Optional[QMainWindow] = None, flags: typing.Union[Qt.WindowType, None] = None):
        super(Tab, self).__init__(parent)

        self.parent = parent
        self._flags = flags
        self.body: typing.Union[QWidget, None] = None
        self._last_size: typing[int, None] = None

        self.setObjectName('tab')
        self.setFeatures(self.DockWidgetFeature.DockWidgetMovable)
        self.setUpdatesEnabled(True)

        self.setWindowFlags(Tab._default_widget_flags)

        if flags is not None:
            self.setWindowFlag(flags)

    def setTitle(self, title_text: str, icon) -> None:
        title = TabTitle(title_text, icon)

        if Qt.WindowType.WindowMinimizeButtonHint in self.windowFlags():
            title.setOnMinimize(self._toggleMinimize)
        super().setTitleBarWidget(title)

    def setBody(self, body_widget: QWidget, scroll: bool = True):
        body_widget.setContentsMargins(0, 0, 0, 0)
        body_widget.setStyleSheet(internal_body_style)
        body_widget.setMaximumHeight(DataUtils.max_size)
        body_widget.setObjectName('body')

        if scroll:
            area = QScrollArea()
            area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            area.setWidget(body_widget)
            self.body = area
        else:
            self.body = body_widget

        self.setWidget(self.body)

    def minimize(self):
        self._last_size = self.size().height() * 2

        if self.body is not None:
            self.setMaximumHeight(34)
            self.body.setMaximumHeight(0)

        self.setWindowState(Qt.WindowState.WindowMinimized)

    def maximize(self):
        if self.body is not None:
            self.body.setMaximumHeight(DataUtils.max_size)
            self.setMaximumHeight(DataUtils.max_size)
            self.parent.resizeDocks([self], [self._last_size], Qt.Orientation.Vertical)

        self.setWindowState(Qt.WindowState.WindowMaximized)

    def _toggleMinimize(self):
        if self.windowState() == Qt.WindowState.WindowMinimized:
            self.maximize()
        else:
            self.minimize()

