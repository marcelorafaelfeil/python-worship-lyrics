import sys

from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QHBoxLayout, QWidget
from qframelesswindow import TitleBarButton
from qframelesswindow.titlebar import MinimizeButton, CloseButton, MaximizeButton
from qframelesswindow.utils import startSystemMove


class BaseTitleBar(QWidget):

    _end_widgets = None

    def __init__(self, parent, end_widgets=None):
        super().__init__(parent)

        self._window = parent
        self._end_widgets = end_widgets
        self.minBtn = MinimizeButton(parent=self)
        self.closeBtn = CloseButton(parent=self)
        self.maxBtn = MaximizeButton(parent=self)
        self.hBoxLayout = QHBoxLayout(self)
        self._is_double_click_enabled = True

        self.content_layout = QHBoxLayout()
        self.content_layout.setSpacing(0)
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        self.content_widget = QWidget()
        self.content_widget.setLayout(self.content_layout)

        # connect signal to slot
        self.minBtn.clicked.connect(self.window().showMinimized)
        self.maxBtn.clicked.connect(self._toggle_max_state)
        self.closeBtn.clicked.connect(self.window().close)

        self.render_layout()

        self.window().installEventFilter(self)

    def render_title_widget(self):
        self.content_layout.addStretch(1)


    def render_layout(self):
        self.render_title_widget()
        self.content_layout.addWidget(self.minBtn, 0, Qt.AlignmentFlag.AlignRight)
        self.content_layout.addWidget(self.maxBtn, 0, Qt.AlignmentFlag.AlignRight)
        self.content_layout.addWidget(self.closeBtn, 0, Qt.AlignmentFlag.AlignRight)

        self.resize(200, 32)
        self.setFixedHeight(32)

        # add buttons to layout
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

        self.hBoxLayout.addWidget(self.content_widget)

    def eventFilter(self, obj, e):
        if obj is self.window():
            if e.type() == QEvent.Type.WindowStateChange:
                self.maxBtn.setMaxState(self.window().isMaximized())
                return False

        return super().eventFilter(obj, e)

    def mouseDoubleClickEvent(self, event):
        """ Toggles the maximization state of the window """
        if event.button() != Qt.MouseButton.LeftButton or not self._is_double_click_enabled:
            return

        self._toggle_max_state()

    def mouseMoveEvent(self, e):
        if sys.platform != "win32" or not self.can_drag(e.pos()):
            return

        startSystemMove(self.window(), e.globalPosition().toPoint())

    def mousePressEvent(self, e):
        if sys.platform == "win32" or not self.can_drag(e.pos()):
            return

        startSystemMove(self.window(), e.globalPosition().toPoint())

    def _toggle_max_state(self):
        """ Toggles the maximization state of the window and change icon """
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()

    def _is_drag_region(self, pos):
        """ Check whether the position belongs to the area where dragging is allowed """
        width = 0
        for button in self.findChildren(TitleBarButton):
            if button.isVisible():
                width += button.width()

        return 0 < pos.x() < self.width()

    def _has_button_pressed(self):
        """ whether any button is pressed """
        return any(btn.isPressed() for btn in self.findChildren(TitleBarButton))

    def can_drag(self, pos):
        """ whether the position is draggable """
        return self._is_drag_region(pos) and not self._has_button_pressed()

    def set_double_click_enabled(self, isEnabled):
        """ whether to switch window maximization status when double clicked

        Parameters
        ----------
        isEnabled: bool
            whether to enable double click
        """
        self._is_double_click_enabled = isEnabled
