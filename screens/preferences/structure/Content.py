from PyQt6.QtWidgets import QSplitter, QWidget

from .OptionsTree import OptionsTree
from screens.preferences.forms.ListForms import default_option


class Content(QSplitter):
    def __init__(self):
        super(Content, self).__init__()

        self._on_option_selected = None
        self._last_widget: QWidget | None = None

        self.options_tree = OptionsTree(self, self._onOptionSelected)
        self.addWidget(self.options_tree)

        self.options_tree.selectDefault()

    def _onOptionSelected(self, item):
        if item is not None:
            if self._last_widget is not None:
                self._last_widget.deleteLater()

            self._last_widget = item()
            self.addWidget(self._last_widget)
