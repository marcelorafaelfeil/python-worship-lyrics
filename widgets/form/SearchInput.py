from reactivex import Subject

from styles import SearchInputStyle
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QFrame, QComboBox

from services.utils import PathUtils


class SearchInput(QFrame):
    search = Subject()

    def __init__(self):
        super(SearchInput, self).__init__()

        layout = QHBoxLayout()

        button = QPushButton()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar")
        self.search_input.setContentsMargins(0, 0, 0, 0)
        self.search_input.returnPressed.connect(self.on_search)
        self.search_input.textChanged.connect(self.on_clear_search_input)

        self.search_by = QComboBox()
        self.search_by.addItems(['Título', 'Autor', 'Letra'])
        self.search_by.setContentsMargins(0, 0, 0, 0)
        self.search_by.setMinimumWidth(90)

        icon = QIcon(PathUtils.icon('magnify.png'))
        button.setIcon(icon)
        button.pressed.connect(self.on_search)

        layout.addWidget(self.search_input)
        layout.addWidget(button)
        layout.addWidget(self.search_by)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setObjectName("SearchContent")
        self.setStyleSheet(SearchInputStyle.search_content_style)

    def on_clear_search_input(self):
        value = self.search_input.text()

        if value == '':
            self.on_search()

    def on_search(self):
        value = self.search_input.text()
        search_by = self.search_by.currentIndex()

        self.search.on_next({'value': value, 'search_by': search_by})
