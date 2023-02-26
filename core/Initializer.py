import os
from os import path

from core import Core, ApplicationContext, WebSocketHandler, Lyrics, HttpHandler, SettingsHandler
from screens.lyrics.NewLyricScreen import NewLyricScreen
from screens.preferences import PreferencesScreen


class Initializer:
    @staticmethod
    def start():
        ApplicationContext.core = Core(ApplicationContext)
        ApplicationContext.settings = SettingsHandler(ApplicationContext)

        Initializer.prepare_default_settings()

        ApplicationContext.http = HttpHandler()
        ApplicationContext.lyric_handler = Lyrics(ApplicationContext)
        ApplicationContext.lyric_handler.load_lyrics()
        ApplicationContext.websocket_handler = WebSocketHandler(ApplicationContext)
        ApplicationContext.window_preference = PreferencesScreen()
        ApplicationContext.window_new_lyric = NewLyricScreen()

    @staticmethod
    def prepare_default_settings():
        settings = ApplicationContext.settings

        if settings.get_directory_path() is None:
            home_path = path.expanduser("~")
            home_path += path.sep + "lyrics"

            if not path.exists(home_path):
                os.mkdir(home_path)

            ApplicationContext.settings.updateTemporarySettingsFile("general.directory.path", home_path)
            ApplicationContext.settings.save(False)
