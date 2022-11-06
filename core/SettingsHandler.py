import json

from services.utils import PathUtils


class SettingsHandler:
    _file_name: str = 'settings.json'
    _settings: any = {}

    def __init__(self):
        self._settings = self.loadSettingsFile()

    def loadSettingsFile(self):
        f = open(PathUtils.settings(self._file_name))
        data = json.load(f)
        f.close()

        return data

    def get(self):
        return self._settings

    def hasDifference(self):
        saved_file = self.loadSettingsFile()

        return saved_file == self._settings

