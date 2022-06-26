import asyncio
import websockets


class MessageHandle:
    def __init__(self):
        self.websocket = websockets.connect