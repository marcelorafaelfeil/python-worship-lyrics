import logging


class Core:

    def __init__(self, context):
        self.context = context

    def update(self):
        self.context.lyric_handler.refresh()
        pass

