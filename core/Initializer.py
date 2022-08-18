import os
from pathlib import Path
from . import ApplicationContext, WebSocketHandler, Lyrics, MessageHandle, HttpHandler


class Initializer:
    @staticmethod
    def start():
        ApplicationContext.websocket = WebSocketHandler()
        ApplicationContext.http = HttpHandler()

        ApplicationContext.lyric_handler = Lyrics(os.path.join(Path.home(), 'lyrics'))
        ApplicationContext.lyric_handler.loadLyrics()

        ApplicationContext.message_handler = MessageHandle()
