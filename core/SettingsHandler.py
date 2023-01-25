from reactivex import Subject

from services import SettingsFileService


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

    def save(self):
        self._settings_file.persistTemporarySettings()
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



