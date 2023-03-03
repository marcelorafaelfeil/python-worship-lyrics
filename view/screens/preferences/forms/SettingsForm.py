import logging

from PyQt6.QtWidgets import QWidget
from controller.core import ApplicationContext


class SettingsForm(QWidget):
    _settings_prefix_key: str = 'websocket'
    _current_config = {}

    def __init__(self):
        super().__init__()
        self._current_config = ApplicationContext.settings.getTemporaryConfig()

        if bool(self._current_config) is False:
            self._current_config = ApplicationContext.settings.getDefaultConfig()

    def savePropertyInTemporaryFile(self, key, value):
        try:
            ApplicationContext.settings.updateTemporarySettingsFile(key, value)
        except Exception as err:
            logging.error('Error to save the settings in the temporary file.', err)
