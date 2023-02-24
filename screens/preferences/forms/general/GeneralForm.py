from PyQt6.QtWidgets import QWidget, QVBoxLayout

from screens.preferences.forms import SettingsForm
from screens.preferences.forms.general import DirectoryForm
from widgets import Label


class GeneralForm(SettingsForm):

    def __init__(self):
        SettingsForm.__init__(self)

        self.general_form: {QWidget} = {}
        self.general_labels: {Label} = {}

        layout = QVBoxLayout()
        layout.addWidget(DirectoryForm())

        self.setLayout(layout)
