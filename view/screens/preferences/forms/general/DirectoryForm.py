import logging

import qtawesome
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog

from view.screens.preferences.forms import FormHeader
from view.widgets import Label
from view.widgets.form import Input, IconButton


class DirectoryForm(QWidget):
    _fixed_label_width: int = 120

    def __init__(self, default_value: str = None, when_save=None):
        super().__init__()

        self.default_value = default_value
        self.when_save = when_save

        layout = QVBoxLayout()
        layout.addWidget(FormHeader("Diretório"))
        layout.addWidget(self._render_directory_form(), 1)

        self.setLayout(layout)

    def _render_directory_form(self) -> QWidget:
        form_content_widget = QWidget()
        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addLayout(self._render_content_input())

        form_content_widget.setLayout(layout)

        return form_content_widget

    def _render_content_input(self):
        content_input_layout = QHBoxLayout()

        content_input_layout.addWidget(self._render_directory_label())
        content_input_layout.addLayout(self._render_input())

        return content_input_layout

    def _render_directory_label(self) -> Label:
        select_directory_label = Label("Selecione o diretório: ")
        select_directory_label.setFixedWidth(self._fixed_label_width)
        select_directory_label.setContentsMargins(0, 0, 5, 0)

        return select_directory_label

    def _render_input(self):
        layout_input = QHBoxLayout()

        self.directory_path_input = Input(self.default_value)
        layout_input.addWidget(self.directory_path_input)
        layout_input.addWidget(self._render_button_dialog(), 0)

        return layout_input

    def _render_button_dialog(self):
        open_dialog_button = IconButton(qtawesome.icon("mdi.folder-outline", color="#C7A3DD", scale_factor=1.1))
        open_dialog_button.setIconSize(QtCore.QSize(22, 22))
        open_dialog_button.clicked.connect(self._open_directory_dialog)

        return open_dialog_button

    def _open_directory_dialog(self):
        directory_dialog = QFileDialog(self)
        directory_dialog.setFileMode(QFileDialog.FileMode.Directory)
        directory_dialog.setOption(QFileDialog.Option.ShowDirsOnly)

        if directory_dialog.exec():
            selected_directory = directory_dialog.selectedFiles()[0]
            self.directory_path_input.setText(selected_directory)

            if self.when_save is None:
                logging.warning("It's necessary to specify a value for \"when_save\"")
            else:
                self.when_save(selected_directory)
