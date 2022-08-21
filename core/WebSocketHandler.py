import threading

from tornado import web, ioloop

from .WebSocketServer import WebSocketServer


class WebSocketHandler:
    websocket_port: int = 4041
    websocket_task: str = 'lyric'

    def __init__(self):
        self._run()

    def _run(self):
        web_app = web.Application(
            [(f"/{WebSocketHandler.websocket_task}", WebSocketServer)],
            websocket_ping_interval=10,
            websocket_ping_timeout=30,
        )

        web_app.listen(WebSocketHandler.websocket_port)
        self.thread = threading.Thread(target=ioloop.IOLoop.current().start)
        self.thread.daemon = True
        self.thread.start()

