class Lyric:
    name: str
    author: str
    lyric: str
    path: str

    def __init__(self, name, author, lyric, path=''):
        self.name = name
        self.author = author
        self.lyric = lyric
        self.path = path

