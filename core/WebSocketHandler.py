import asyncio
import threading

from tornado import web

from .WebSocketServer import WebSocketServer


class WebSocketHandler:

    websocket_task: str = 'lyric'

    def __init__(self, context):
        settings = context.settings.getConfig()['websocket'] if bool(context.settings.getConfig()) else None

        self.websocket_port = settings['port']
        self.websocket_host = settings['host']
        self._run()

    def get_port(self):
        return self.websocket_port

    def get_host(self):
        return self.websocket_host

    def _run(self):
        self.thread = threading.Thread(target=self._run_async_task)
        self.thread.daemon = True
        self.thread.start()

    def _run_async_task(self):
        asyncio.run(self._run_websocket_server())

    async def _run_websocket_server(self):
        websocket = web.Application(
            [(f"/{WebSocketHandler.websocket_task}", WebSocketServer)],
            websocket_ping_interval=10,
            websocket_ping_timeout=30,
        )

        websocket.listen(self.websocket_port)

        await asyncio.Event().wait()

