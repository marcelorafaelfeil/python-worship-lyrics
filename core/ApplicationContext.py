from . import Lyrics, MessageHandle, WebSocketServer


class ApplicationContext:

    def __init__(self):
        self._lyrics_handle = Lyrics('/Users/marcelorafael/lyrics')
        self.message_handler = None
        self.websocket: WebSocketServer | None = None

    def lyricsHandle(self):
        return self._lyrics_handle

    def setMessageHandler(self, message_handler: MessageHandle):
        self.message_handler = message_handler

    def setWebsocket(self, websocket: WebSocketServer):
        self.websocket = websocket

    def getMessageHandler(self) -> MessageHandle:
        return self.message_handler

    def getWebsocket(self) -> WebSocketServer:
        return self.websocket
