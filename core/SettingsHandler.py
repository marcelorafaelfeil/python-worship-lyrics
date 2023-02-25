from reactivex import Subject

from services import SettingsFileService
import os


class SettingsHandler:
    update_settings_file = Subject()
    has_settings_changes = Subject()

    def __init__(self, context):
        self.context = context
        self.update_settings_file.subscribe(self._updateSettingsFile)
        self._settings_file = SettingsFileService()

    def startConfiguration(self):
        self._settings_file.clearTemporarySettings()

    def _updateSettingsFile(self, data):
        self._settings_file.addPropertyInTemporaryFile(data.get('key'), data.get('value'))
        self.has_settings_changes.on_next(self._settings_file.hasDifference())

    def updateTemporarySettingsFile(self, key, value):
        self.update_settings_file.on_next({'key': key, 'value': value})

    def save(self, update_tree=True):
        self._settings_file.persistTemporarySettings()

        if update_tree:
            self.context.core.update()

    def getTemporaryConfig(self):
        return self._settings_file.loadSettingsFile(file_type=1)

    def getDefaultConfig(self):
        return self._settings_file.loadSettingsFile(file_type=0)

    def getConfig(self):
        default_configuration = self.getDefaultConfig()
        config = self._settings_file.loadSettingsFile(file_type=2)

        default_configuration.update(config)

        return default_configuration

    def get_directory_path(self):
        config = self.getConfig()
        path = None

        if (
                ('general' in config) and
                ('directory' in config['general']) and
                ('path' in config['general']['directory'])
        ):
            path = config['general']['directory']['path']
        else:
            default_config = self.getDefaultConfig()
            if (
                ('general' in default_config) and
                ('directory' in default_config['general']) and
                ('path' in default_config['general']['directory'])
            ):
                path = default_config['general']['directory']['path']

        if path is not None and path[-1] != os.path.sep:
            path += os.path.sep

        return path

