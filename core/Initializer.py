import os
from os import path

from core import Core, ApplicationContext, WebSocketHandler, HttpHandler, SettingsHandler
from screens.lyrics.NewLyricScreen import NewLyricScreen
from screens.preferences import PreferencesScreen
from services.LyricsService import LyricsService


class Initializer:
    @staticmethod
    def start():
        ApplicationContext.core = Core()
        ApplicationContext.settings = SettingsHandler(ApplicationContext)

        Initializer.prepare_default_settings()

        ApplicationContext.http = HttpHandler()
        ApplicationContext.lyrics_service = LyricsService(ApplicationContext)
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
