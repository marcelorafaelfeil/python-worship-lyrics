import os

from core.Event import Event
from services.utils.PathUtils import PathUtils


def _add_file(file_name: str, author: str, path: str):
    extension = file_name[-4:]
    name = file_name.replace(extension, '')

    return {
        'file_name': file_name,
        'name': name,
        'author': author,
        'path': path
    }


class Lyrics:
    _event_add_to_selected = 'ON_ADD_TO_SELECTED'
    _event_on_change_lyric = 'ON_CHANGE_LYRIC'
    _event_on_change_verse = 'ON_CHANGE_VERSE'

    def __init__(self, context):
        self.context = context
        self._current_lyric = None
        self.original_lyrics_list = []
        self.lyrics_list = []

    def load_lyrics(self):
        path = self.context.settings.get_directory_path()
        folders = os.listdir(path)
        lyrics_list = []

        for folder in folders:
            if os.path.isdir(path + folder):
                current_path = PathUtils.validatePath(path + folder)
                lyrics_files = os.listdir(current_path)

                for lfile in lyrics_files:
                    if os.path.isfile(current_path + lfile) and lfile.lower().endswith(".txt"):
                        lyrics_list.append(_add_file(lfile, folder, current_path + lfile))

        self.original_lyrics_list = lyrics_list
        self.lyrics_list = lyrics_list

    def refresh(self):
        self.load_lyrics()
        self.context.lyrics_tree.setItems(self.lyrics_list)
        return self.lyrics_list

    def set_lyrics_list(self, lyrics_list):
        self.lyrics_list = lyrics_list

    def get_lyrics_list(self):
        return self.lyrics_list

    def reset_lyrics_list(self):
        self.lyrics_list = self.original_lyrics_list

    def set_selected_lyric(self, lyric):
        self._current_lyric = lyric
        Event.emit(self._event_on_change_lyric, lyric)

    def get_current_lyric(self):
        return self._current_lyric

    def get_current_lyric_content(self):
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

    def on_change_lyric(self, func) -> None:
        Event.on(self._event_on_change_lyric, func)

    def on_change_verse(self, func) -> None:
        Event.on(self._event_on_change_verse, func)

    def add_to_selected_lyrics(self, widget_item) -> None:
        Event.emit(self._event_add_to_selected, widget_item)

    def on_add_to_selected_lyric(self, func) -> None:
        Event.on(self._event_add_to_selected, func)

    def emit_verse_changed(self, lyric) -> None:
        Event.emit(self._event_on_change_verse, lyric)
