from . import Lyrics, MessageHandle, WebSocketServer, WebSocketHandler
from PyQt6.QtWidgets import QWidget, QDialog


class ApplicationContext:
    websocket: WebSocketServer
    lyric_handler: Lyrics
    message_handler: MessageHandle
    main_window: QWidget
    window_preference: QDialog
    lyrics_tree: any
    selected_lyrics_tree: any

    @staticmethod
    def getMessageHandler() -> MessageHandle:
        return ApplicationContext.message_handler

    @staticmethod
    def getWebsocket() -> WebSocketServer:
        return ApplicationContext.websocket
