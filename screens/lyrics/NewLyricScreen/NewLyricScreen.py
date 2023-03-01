import typing

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QMessageBox, QPlainTextEdit

from core import ApplicationContext
from entity.Lyric import Lyric
from screens.lyrics.NewLyricScreen.widget.Footer import Footer
from screens.lyrics.NewLyricScreen.widget.LyricButtons import LyricButtons
from screens.lyrics.NewLyricScreen.widget.LyricForm import LyricForm
from services.LyricsFileManagementService import LyricsFileManagementService


class NewLyricScreen(QDialog):

    _selected_lyric: typing.Union[Lyric, None] = None

    def __init__(self):
        super(NewLyricScreen, self).__init__()

        self._form = LyricForm()
        self._footer = self._render_footer()

        structure_layout = QVBoxLayout()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.setSpacing(0)

        layout.addWidget(self._form)
        layout.addWidget(LyricButtons(
            on_uppercase=self.transform_to_uppercase,
            on_lowercase=self.transform_to_lowercase
        ))

        structure_layout.addLayout(layout)
        structure_layout.addWidget(self._footer)

        self.resize(QSize(650, 700))
        self.setLayout(structure_layout)

    def _render_footer(self):
        return Footer(
            on_save=self.save,
            on_cancel=self.cancel
        )

    def save(self):
        name = self._form.get_song_name()
        author = self._form.get_author()
        lyric = self._form.get_lyric()

        if not name or not author or not lyric:
            if not name:
                self._alert('É necessário preencher o nome da música.').show()
            elif not author:
                self._alert('É necessário preencher o nome do autor.').show()
            elif not lyric:
                self._alert('É necessário preencher a letra da música.').show()
            return

        if not self._selected_lyric:
            LyricsFileManagementService.create_new_lyric(Lyric(name, author, lyric))
        else:
            self._selected_lyric.name = name
            self._selected_lyric.author = author
            self._selected_lyric.lyric = lyric
            LyricsFileManagementService.update_lyric(self._selected_lyric)

        self._form.reset()
        self._selected_lyric = None
        ApplicationContext.lyrics_service.refresh()

        self.close()

    def _alert(self, text):
        message_box = QMessageBox(self)
        message_box.setWindowTitle('Valor inválido')
        message_box.setText(text)
        return message_box

    def cancel(self):
        self.close()

    def transform_to_uppercase(self):
        lyric_input: QPlainTextEdit = self._form.get_lyric_input()
        text = lyric_input.toPlainText().upper()
        lyric_input.setPlainText(text)

    def transform_to_lowercase(self):
        lyric_input: QPlainTextEdit = self._form.get_lyric_input()
        text = lyric_input.toPlainText().lower()
        lyric_input.setPlainText(text)

    def update_lyric(self, lyric: Lyric):
        self._form.set_song_name(lyric.name)
        self._form.set_author(lyric.author)
        self._form.set_lyric(lyric.lyric)

        self._selected_lyric = lyric

        self.show()
