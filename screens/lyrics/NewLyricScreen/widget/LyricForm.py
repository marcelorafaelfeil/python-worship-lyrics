from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit

from widgets.form import Input


class LyricForm(QWidget):
    _form = {}

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._render_song_name_input())
        layout.addWidget(self._render_author_input())
        layout.addWidget(self._render_lyric_input())

        self.setLayout(layout)

    def _render_song_name_input(self):
        self._form['song_name'] = Input(placeholder='Nome da música')
        return self._form['song_name']

    def _render_author_input(self):
        self._form['author'] = Input(placeholder='Autor')
        return self._form['author']

    def _render_lyric_input(self):
        self._form['lyric'] = QPlainTextEdit()
        self._form['lyric'].setPlaceholderText('Letra da música')
        return self._form['lyric']

    def set_song_name(self, name: str):
        self._form['song_name'].setText(name)

    def set_author(self, author: str):
        self._form['author'].setText(author)

    def set_lyric(self, lyric: str):
        self._form['lyric'].setPlainText(lyric)

    def get_song_name(self):
        return self._form['song_name'].text()

    def get_author(self):
        return self._form['author'].text()

    def get_lyric(self):
        return self._form['lyric'].toPlainText()

    def get_lyric_input(self) -> QPlainTextEdit:
        return self._form['lyric']

    def reset(self):
        self._form['song_name'].clear()
        self._form['author'].clear()
        self._form['lyric'].clear()
