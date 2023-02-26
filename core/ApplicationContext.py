from core import Lyrics, WebSocketHandler, SettingsHandler, Core
from PyQt6.QtWidgets import QWidget, QDialog


class ApplicationContext:
    core: Core
    lyric_handler: Lyrics
    websocket_handler: WebSocketHandler
    main_window: QWidget
    window_preference: QDialog
    window_new_lyric: any
    lyrics_tree: any
    selected_lyrics_tree: any
    settings: SettingsHandler

    @staticmethod
    def getWebsocket() -> WebSocketHandler:
        return ApplicationContext.websocket_handler
