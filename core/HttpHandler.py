import asyncio
import threading

from tornado.httpserver import HTTPServer
from tornado.web import Application

from . import HttpRequestConfiguration


class HttpHandler:
    http_port: int = 9092

    def __init__(self):
        self._run()

    def _run(self):
        self.thread = threading.Thread(target=self._runAsyncTask)
        self.thread.daemon = True
        self.thread.start()

    def _runAsyncTask(self):
        asyncio.run(HttpHandler._runHttpServer())

    @staticmethod
    async def _runHttpServer():
        web_app = Application([('/', HttpRequestConfiguration)])

        server = HTTPServer(web_app)
        server.listen(HttpHandler.http_port)
        await asyncio.Event().wait()
