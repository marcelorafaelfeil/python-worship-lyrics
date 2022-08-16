from typing import Optional, Awaitable, Union

from tornado.websocket import WebSocketHandler


class WebSocketServer(WebSocketHandler):

    clients = set()

    def check_origin(self, origin: str) -> bool:
        return True

    def open(self):
        WebSocketServer.clients.add(self)

    def onClose(self):
        WebSocketServer.clients.remove(self)

    @classmethod
    def send(cls, message: str):
        for client in cls.clients:
            try:
                client.write_message(message)
            except Exception as e:
                print('Não foi possível escrever a mensagem')

    def on_message(self, message: Union[str, bytes]) -> Optional[Awaitable[None]]:
        pass

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass
