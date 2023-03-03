import qtawesome as qta
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QFrame

from view.widgets.layout import Row, Column

from view.styles import Tab as style


class TabTitle(QFrame):
    def __init__(self, text: str, icon=None, on_minimize=None):
        super(TabTitle, self).__init__()

        self._on_minimize = on_minimize

        title = QLabel(text)

        self.layout = Row()

        if icon is not None:
            icon_widget = qta.IconWidget()
            icon_widget.setIcon(icon)
            self.layout.addWidget(icon_widget)

        self.layout.addWidget(title, 1)

        if self._on_minimize is not None:
            self.layout.addWidget(self._actionToMinimize())

        column = Column()
        column.addLayout(self.layout)

        self.setLayout(column)
        self.setObjectName('TabTitle')
        self.setStyleSheet(style.title_content_style)

    def setOnMinimize(self, _on_minimize):
        self._on_minimize = _on_minimize
        self.layout.addWidget(self._actionToMinimize())

    def _actionToMinimize(self) -> QWidget:
        button = QPushButton()
        button.setIcon(qta.icon('mdi.window-minimize'))
        button.clicked.connect(self._on_minimize)
        button.setStyleSheet(style.title_action_style)

        return button

