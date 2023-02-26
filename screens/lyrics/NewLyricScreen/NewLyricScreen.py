from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLabel, QVBoxLayout, QMessageBox

from core import ApplicationContext
from entity.Lyric import Lyric
from screens.lyrics.NewLyricScreen.widget.Footer import Footer
from screens.lyrics.NewLyricScreen.widget.LyricButtons import LyricButtons
from screens.lyrics.NewLyricScreen.widget.LyricForm import LyricForm
from services.LyricsManagementService import LyricsManagementService


class NewLyricScreen(QDialog):

    def __init__(self):
        super(NewLyricScreen, self).__init__()

        self._form = LyricForm()
        self._footer = self._render_footer()

        structure_layout = QVBoxLayout()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.setSpacing(0)

        layout.addWidget(self._form)
        layout.addWidget(LyricButtons())

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

        LyricsManagementService.create_new_lyric(Lyric(name, author, lyric))
        self._form.reset()
        ApplicationContext.lyric_handler.refresh()

        self.close()

    def _alert(self, text):
        message_box = QMessageBox(self)
        message_box.setWindowTitle('Valor inválido')
        message_box.setText(text)
        return message_box

    def cancel(self):
        self.close()
