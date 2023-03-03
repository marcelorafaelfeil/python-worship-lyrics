import os

from controller.core import ApplicationContext
from controller.entity import Lyric

_lyric_extension = '.txt'


class LyricsFileManagementService:
    @staticmethod
    def create_new_lyric(lyric: Lyric):
        if not lyric.name or not lyric.author or not lyric.lyric:
            raise Exception("It's necessary to specify all properties for the lyric")

        settings = ApplicationContext.settings
        directory_path = settings.get_directory_path()
        lyric_path = directory_path + os.path.sep + lyric.author
        file_path = lyric_path + os.path.sep + lyric.name + _lyric_extension

        if not os.path.exists(lyric_path):
            os.mkdir(lyric_path)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(lyric.lyric)

    @staticmethod
    def update_lyric(lyric: Lyric):
        LyricsFileManagementService.remove_lyric(lyric)
        LyricsFileManagementService.create_new_lyric(lyric)

    @staticmethod
    def remove_lyric(lyric: Lyric):
        if os.path.exists(lyric.path):
            os.remove(lyric.path)

            dir_path = os.path.dirname(lyric.path)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

    @staticmethod
    def get_lyric_by_path(path):
        content = ''
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

        return content
