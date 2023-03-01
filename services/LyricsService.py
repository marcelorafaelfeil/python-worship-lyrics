import os
from typing import List

from reactivex import Subject

from entity.Lyric import Lyric
from entity.LyricLine import LyricLine
from services.utils import PathUtils


def _add_file(file_name: str, author: str, path: str) -> Lyric:
    extension = file_name[-4:]
    name = file_name.replace(extension, '')

    return Lyric(name, author, '', path, file_name)


class LyricsService:
    lyrics: Subject = Subject()
    prepare_lyric = Subject()
    select_lyric = Subject()
    project_verse = Subject()

    def __init__(self, context):
        self.context = context
        self._original_lyrics_list: List[Lyric] = []
        self.data: List[Lyric] = []
        self.load_lyrics()

    def load_lyrics(self):
        path = self.context.settings.get_directory_path()
        folders = os.listdir(path)
        lyrics_list: List[Lyric] = []

        for folder in folders:
            if os.path.isdir(path + folder):
                current_path = PathUtils.validatePath(path + folder)
                lyrics_files = os.listdir(current_path)

                for lfile in lyrics_files:
                    if os.path.isfile(current_path + lfile) and lfile.lower().endswith(".txt"):
                        lyrics_list.append(_add_file(lfile, folder, current_path + lfile))

        self._original_lyrics_list = lyrics_list
        self.data = lyrics_list

        self.lyrics.on_next(self.data)

    def refresh(self):
        self.load_lyrics()

    def read_lyric(self, lyric: Lyric):
        path = lyric.path
        content = []

        f = open(path, 'r', encoding='utf-8')
        lines = f.readlines()

        index = 0
        for line in lines:
            content.append(LyricLine(index, False, line.strip('\n')))
            index += 1

        f.close()

        return content
