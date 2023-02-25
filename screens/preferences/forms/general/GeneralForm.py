from PyQt6.QtWidgets import QWidget, QVBoxLayout

from core import ApplicationContext
from screens.preferences.forms import SettingsForm
from screens.preferences.forms.general import DirectoryForm
from widgets import Label


class GeneralForm(SettingsForm):
    _general_key: str = 'general'
    _directory_path_key: str = _general_key + '.directory.path'

    def __init__(self):
        SettingsForm.__init__(self)

        self.general_form: {QWidget} = {}
        self.general_labels: {Label} = {}

        layout = QVBoxLayout()
        layout.addWidget(self._render_directory_form())

        self.setLayout(layout)

    def _render_directory_form(self):
        current_directory_value = None
        current_config = ApplicationContext.settings.getTemporaryConfig()

        if (
                (current_config is not None) and
                ('general' in current_config) and
                ('directory' in current_config['general']) and
                ('path' in current_config['general']['directory'])
        ):
            current_directory_value = current_config['general']['directory']['path']

        return DirectoryForm(current_directory_value, self.save_directory)

    def save_directory(self, directory_path: str):
        self.savePropertyInTemporaryFile(self._directory_path_key, directory_path)
