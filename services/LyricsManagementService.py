import os

from core import ApplicationContext
from entity import Lyric

_lyric_extension = '.txt'


class LyricsManagementService:
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

