from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from view.styles.theme import DarkTheme
from view.widgets.BaseTitleBar import BaseTitleBar
from view.widgets.WLMainMenu import WLMainMenu


class WLTitleBar(BaseTitleBar):

    def __init__(self, parent, end_widgets=None):
        super().__init__(parent, end_widgets)

        self._window = parent

        default_color = DarkTheme().windowText().color().name()
        self.minBtn.setNormalColor(default_color)
        self.maxBtn.setNormalColor(default_color)
        self.closeBtn.setNormalColor(default_color)

        self.minBtn.setHoverColor(default_color)
        self.maxBtn.setHoverColor(default_color)
        self.closeBtn.setHoverColor(default_color)

    def render_title_widget(self):
        menu = WLMainMenu()

        self.content_layout.addWidget(menu, 0)
        self.content_layout.addWidget(QLabel(self._window.windowTitle()), 1, Qt.AlignmentFlag.AlignCenter)

        if self._end_widgets is not None:
            self.content_layout.addWidget(self._end_widgets(), 0)
