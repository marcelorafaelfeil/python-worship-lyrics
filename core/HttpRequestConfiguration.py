from typing import Optional, Awaitable

from tornado.web import RequestHandler


class HttpRequestConfiguration(RequestHandler):
    html_path = './template/lyric.html'

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        html_file = open(HttpRequestConfiguration.html_path, 'r')
        html = html_file.read()
        html_file.close()

        self.write(html)
