from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

from screens.preferences.forms import SettingsForm, FormHeader
from widgets import Label


class GeneralForm(SettingsForm):

    def __init__(self):
        SettingsForm.__init__(self)

        self.general_form: {QWidget} = {}
        self.general_labels: {Label} = {}

        layout = QVBoxLayout()
        layout.addWidget(FormHeader('Diretório'))
        layout.addWidget(self._render_directory_form(), 1)

        self.setLayout(layout)

    def _render_directory_form(self):
        form_content_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        test_text = QLabel("Testando som 123...")

        layout.addWidget(test_text)

        form_content_widget.setLayout(layout)

        return form_content_widget
