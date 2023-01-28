import logging

from PyQt6.QtWidgets import QWidget
from core import ApplicationContext


class SettingsForm(QWidget):
    _settings_prefix_key: str = 'websocket'

    def savePropertyInTemporaryFile(self, key, value):
        try:
            ApplicationContext.settings.updateTemporarySettingsFile(key, value)
        except Exception as err:
            logging.error('Error to save the settings in the temporary file.', err)
