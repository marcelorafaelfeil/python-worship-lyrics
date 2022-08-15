from . import Lyrics


class ApplicationContext:

    def __init__(self):
        self._lyrics_handle = Lyrics('/Users/marcelorafael/lyrics')

    def lyricsHandle(self):
        return self._lyrics_handle

