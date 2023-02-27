class Lyric:
    name: str
    author: str
    lyric: str
    path: str
    file_name: str

    def __init__(self, name, author, lyric, path='', file_name=''):
        self.name = name
        self.author = author
        self.lyric = lyric
        self.path = path
        self.file_name = file_name

