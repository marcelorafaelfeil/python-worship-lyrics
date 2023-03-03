from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QSplitter, QWidget

from .OptionsTree import OptionsTree


class Content(QSplitter):
    default_options_width = 250
    default_widget_width = 650
    default_margin_error = 7

    def __init__(self):
        super(Content, self).__init__()

        self._on_option_selected = None
        self._widget_initial_width = Content.default_widget_width
        self._last_widget: QWidget | None = None

        self.options_tree = OptionsTree(self, self._onOptionSelected)
        self.addWidget(self.options_tree)
        self.setSizes([Content.default_options_width])
        self.setCollapsible(0, False)

        self.options_tree.selectDefault()
        self.splitterMoved.connect(self._adjustWidgetWidth)

    def _adjustWidgetWidth(self, pos):
        self._widget_initial_width = self.width() - (pos + Content.default_margin_error)

    def _onOptionSelected(self, item):
        if item is not None:
            if self._last_widget is not None:
                self._last_widget.deleteLater()

            self._last_widget = item()
            self._last_widget.resize(QSize(self._widget_initial_width, self._last_widget.height()))
            self.addWidget(self._last_widget)
