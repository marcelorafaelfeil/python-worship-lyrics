from styles import SearchInputStyle
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QFrame, QComboBox

from services.utils import PathUtils


class SearchInput(QFrame):
    def __init__(self, _callback):
        super(SearchInput, self).__init__()

        self._callback = _callback

        layout = QHBoxLayout()

        button = QPushButton()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar")
        self.search_input.setContentsMargins(0, 0, 0, 0)
        self.search_input.returnPressed.connect(self.onSearch)
        self.search_input.textChanged.connect(self.onClearSearchInput)

        self.search_by = QComboBox()
        self.search_by.addItems(['Título', 'Autor', 'Letra'])
        self.search_by.setContentsMargins(0, 0, 0, 0)
        self.search_by.setMinimumWidth(90)

        icon = QIcon(PathUtils.icon('magnify.png'))
        button.setIcon(icon)
        button.pressed.connect(self.onSearch)

        layout.addWidget(self.search_input)
        layout.addWidget(button)
        layout.addWidget(self.search_by)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setObjectName("SearchContent")
        self.setStyleSheet(SearchInputStyle.search_content_style)

    def onClearSearchInput(self):
        value = self.search_input.text()

        if value == '':
            self.onSearch()

    def onSearch(self):
        value = self.search_input.text()
        search_by = self.search_by.currentIndex()

        self._callback(value, search_by)
