from controller.core import WebSocketHandler, SettingsHandler, Core
from PyQt6.QtWidgets import QWidget, QDialog

from services.LyricsService import LyricsService


class ApplicationContext:
    core: Core
    websocket_handler: WebSocketHandler
    main_window: QWidget
    window_preference: QDialog
    window_new_lyric: any
    lyrics_tree: any
    selected_lyrics_tree: any
    settings: SettingsHandler
    lyrics_service: LyricsService

    @staticmethod
    def getWebsocket() -> WebSocketHandler:
        return ApplicationContext.websocket_handler
