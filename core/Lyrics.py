import os
from core.PathUtils import PathUtils
from core.Event import Event


class Lyrics:
    _event_on_change_key = 'ON_CHANGE_LYRIC'

    def __init__(self, path: str):
        self.path = PathUtils.validatePath(path)
        self._current_lyric = None

    def loadLyrics(self):
        folders = os.listdir(self.path)
        lyrics_list = []

        for folder in folders:
            if os.path.isdir(self.path + folder):
                current_path = PathUtils.validatePath(self.path + folder)
                lyrics_files = os.listdir(current_path)

                for lfile in lyrics_files:
                    if os.path.isfile(current_path + lfile):
                        lyrics_list.append(self.__addFile(lfile, folder, current_path + lfile))

        return lyrics_list

    def __addFile(self, file_name: str, author: str, path: str):
        extension = file_name[-4:]
        name = file_name.replace(extension, '')

        return {
            'file_name': file_name,
            'name': name,
            'author': author,
            'path': path
        }

    def setSelectedLyric(self, lyric):
        self._current_lyric = lyric
        Event.emit(self._event_on_change_key, lyric)

    def getCurrentLyric(self):
        return self._current_lyric

    def getCurrentLyricContent(self):
        lyric = self._current_lyric
        path = lyric['path']
        content = []

        f = open(path, 'r')
        lines = f.readlines()

        index = 0
        for line in lines:
            content.append({
                '_id': index,
                'selected': False,
                'content': line.strip('\n')
            })
            index += 1

        f.close()

        return content

    def onChangeLyric(self, func) -> None:
        Event.on(self._event_on_change_key, func)
