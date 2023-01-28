import json
import logging
import os
import shutil

import jsonmerge

from services.utils import PathUtils


class SettingsFileService:
    _default_file_name: str = 'default.json'
    _definitive_file_name: str = 'settings.json'
    _temporary_file_name: str = 'settings_temp.wl'

    def resetTemporaryFile(self):
        try:
            if os.path.exists(PathUtils.settings(self._temporary_file_name)):
                os.remove(PathUtils.settings(self._temporary_file_name))

                shutil.copy(
                    PathUtils.settings(self._definitive_file_name), PathUtils.settings(self._temporary_file_name)
                )
        except Exception as err:
            logging.error('It was not possible to delete the temporary file.', err)

    def loadSettingsFile(self, file_type: int):
        if file_type == 0:
            file_name = self._default_file_name
        elif file_type == 1:
            file_name = self._temporary_file_name
        else:
            file_name = self._definitive_file_name

        data = {}

        if os.path.exists(PathUtils.settings(file_name)):
            f = open(PathUtils.settings(file_name), 'r')
            file_content = f.read()

            if file_content != '':
                data = json.loads(file_content)

            f.close()

        return data

    def addPropertyInTemporaryFile(self, key, value):
        logging.debug('Including config: {%s, %s}', key, value)

        divided_key = key.split('.')
        structured_config = {}

        if len(divided_key) > 0:
            for index in range(len(divided_key) - 1, -1, -1):
                if index == len(divided_key) - 1:
                    structured_config[divided_key[index]] = value
                else:
                    structured_config[divided_key[index]] = {
                        divided_key[index + 1]: structured_config.pop(divided_key[index + 1])
                    }

        file_content = self.loadSettingsFile(file_type=1)

        with open(PathUtils.settings(self._temporary_file_name), 'w+') as file:
            final_file = jsonmerge.merge(file_content, structured_config)
            file.write(json.dumps(final_file, indent=4))
            file.close()

    def hasDifference(self):
        saved_file = self.loadSettingsFile(file_type=2)
        temporary_file = self.loadSettingsFile(file_type=1)

        return saved_file != temporary_file

    def clearTemporarySettings(self):
        try:
            if os.path.exists(PathUtils.settings(self._temporary_file_name)):
                os.remove(PathUtils.settings(self._temporary_file_name))

                shutil.copy(
                    PathUtils.settings(self._definitive_file_name), PathUtils.settings(self._temporary_file_name)
                )
        except Exception as err:
            logging.error('It was not possible to delete the temporary file.', err)

    def persistTemporarySettings(self):
        settings_json = self.loadSettingsFile(file_type=2)
        temporary_json = self.loadSettingsFile(file_type=1)

        settings_json.update(temporary_json)

        file = open(PathUtils.settings(self._definitive_file_name), 'w')
        file.write(json.dumps(settings_json, indent=4))
        file.close()
