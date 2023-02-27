from core import ApplicationContext


class Core:

    def __init__(self):
        self.context = ApplicationContext

    def update(self):
        self.context.lyrics_service.refresh()
        pass

