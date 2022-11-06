import os
from services.utils.PathUtils import PathUtils
from core.Event import Event


class Lyrics:
    _event_add_to_selected = 'ON_ADD_TO_SELECTED'
    _event_on_change_lyric = 'ON_CHANGE_LYRIC'
    _event_on_change_verse = 'ON_CHANGE_VERSE'

    def __init__(self, path: str):
        self.path = PathUtils.validatePath(path)
        self._current_lyric = None
        self.original_lyrics_list = []
        self.lyrics_list = []

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

        self.original_lyrics_list = lyrics_list
        self.lyrics_list = lyrics_list

    def refresh(self):
        self.loadLyrics()
        return self.lyrics_list

    def setLyricsList(self, lyrics_list):
        self.lyrics_list = lyrics_list

    def getLyricsList(self):
        return self.lyrics_list

    def resetLyricsList(self):
        self.lyrics_list = self.original_lyrics_list

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
        Event.emit(self._event_on_change_lyric, lyric)

    def getCurrentLyric(self):
        return self._current_lyric

    def getCurrentLyricContent(self):
        lyric = self._current_lyric
        path = lyric['path']
        content = []

        f = open(path, 'r', encoding='utf-8')
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
        Event.on(self._event_on_change_lyric, func)

    def onChangeVerse(self, func) -> None:
        Event.on(self._event_on_change_verse, func)

    def addToSelectedLyrics(self, widget_item) -> None:
        Event.emit(self._event_add_to_selected, widget_item)

    def onAddToSelectedLyric(self, func) -> None:
        Event.on(self._event_add_to_selected, func)

    def emitVerseChanged(self, lyric) -> None:
        Event.emit(self._event_on_change_verse, lyric)
