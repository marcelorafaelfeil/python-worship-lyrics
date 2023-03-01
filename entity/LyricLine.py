class LyricLine:
    _id: int
    selected: bool
    content: str

    def __init__(self, _id, selected, content):
        self._id = _id
        self.selected = selected
        self.content = content

    def get_id(self) -> int:
        return self._id
