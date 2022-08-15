import threading

from core import WebSocketServer
from tornado import ioloop, web


class MessageHandle:
    def __init__(self):
        print()
        self._runThread()

    def _runThread(self):
        web_app = web.Application(
            [("/lyric/", WebSocketServer)],
            websocket_ping_interval=10,
            websocket_ping_timeout=30,
        )

        web_app.listen(4041)
        ioloop.IOLoop.current().start()
        self.thread = threading.Thread(target=ioloop.IOLoop.current().start())
        self.thread.daemon = True
        self.thread.start()


