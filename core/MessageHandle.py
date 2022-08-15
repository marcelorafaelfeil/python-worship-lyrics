import websockets
import asyncio

from threading import Thread
from core import HttpHandle
from http.server import HTTPServer, SimpleHTTPRequestHandler


class MessageHandle:
    def __init__(self):
        self.websocket = None
        self.thread_websocket = Thread(target=self.__websocketRunner, args=(self,))

    async def echo(self, websocket):
        async for message in websocket:
            await websocket.send(message)

    async def __websocketRunner(self):
        async with websockets.serve(self.echo, 'localhost', 4041):
            await asyncio.Future()

    def startWebsocket(self):
        self.thread_websocket.start()

    def startHTTP(self):
        server = HTTPServer(('localhost', 9091), HttpHandle)

