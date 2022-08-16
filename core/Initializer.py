from . import ApplicationContext, WebSocketHandler, Lyrics, MessageHandle, HttpHandler


class Initializer:
    @staticmethod
    def start():
        ApplicationContext.websocket = WebSocketHandler()
        ApplicationContext.http = HttpHandler()

        ApplicationContext.lyric_handler = Lyrics('/Users/marcelorafael/lyrics')
        ApplicationContext.lyric_handler.loadLyrics()

        ApplicationContext.message_handler = MessageHandle()
