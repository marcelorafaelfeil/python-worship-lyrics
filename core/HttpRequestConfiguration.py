from typing import Optional, Awaitable

from tornado.web import RequestHandler

from services.utils import PathUtils


class HttpRequestConfiguration(RequestHandler):
    template_name = 'lyric.html'

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        html_file = open(PathUtils.template(HttpRequestConfiguration.template_name), 'r')
        html = html_file.read()
        html_file.close()

        self.write(html)
