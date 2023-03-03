from typing import Optional, Awaitable

from tornado.web import RequestHandler

from services.utils import PathUtils, NetworkUtils
from controller.core import ApplicationContext


class HttpRequestConfiguration(RequestHandler):
    template_name = 'lyric.html'

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        html_file = open(PathUtils.template(HttpRequestConfiguration.template_name), 'r')
        html = html_file.read()

        host = 'localhost'

        if NetworkUtils.getIPAddress() is not None:
            host = NetworkUtils.getIPAddress()
        html_file.close()

        websocket_handler = ApplicationContext.websocket_handler

        html = html.replace('{{WebSocketHost}}', host)
        html = html.replace('{{WebSocketPort}}', str(websocket_handler.get_port()))

        self.write(html)

