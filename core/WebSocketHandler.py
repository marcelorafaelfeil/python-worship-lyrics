import asyncio
import threading

from tornado import web

from .WebSocketServer import WebSocketServer


class WebSocketHandler:

    websocket_task: str = 'lyric'

    def __init__(self, context):
        self.event = asyncio.Event()

        settings = context.settings.getConfig()['websocket'] if bool(context.settings.getConfig()) else None

        self.websocket_port = settings['port']
        self.websocket_host = settings['host']
        self._run()

    def _run(self):
        self.thread = threading.Thread(target=self._runAsyncTask)
        self.thread.daemon = True
        self.thread.start()

    def _runAsyncTask(self):
        asyncio.run(self._runWebsocketServer())

    async def _runWebsocketServer(self):
        websocket = web.Application(
            [(f"/{WebSocketHandler.websocket_task}", WebSocketServer)],
            websocket_ping_interval=10,
            websocket_ping_timeout=30,
        )

        websocket.listen(self.websocket_port)

        await self.event.wait()

