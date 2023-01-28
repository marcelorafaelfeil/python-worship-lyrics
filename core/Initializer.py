import os
from pathlib import Path
from core import Core, ApplicationContext, WebSocketHandler, Lyrics, HttpHandler, SettingsHandler
from screens.preferences import PreferencesScreen


class Initializer:
    @staticmethod
    def start():
        ApplicationContext.core = Core(ApplicationContext)
        ApplicationContext.settings = SettingsHandler(ApplicationContext)
        ApplicationContext.http = HttpHandler()
        ApplicationContext.lyric_handler = Lyrics(os.path.join(Path.home(), 'lyrics'))
        ApplicationContext.lyric_handler.loadLyrics()
        ApplicationContext.websocket_handler = WebSocketHandler(ApplicationContext)
        ApplicationContext.window_preference = PreferencesScreen()

