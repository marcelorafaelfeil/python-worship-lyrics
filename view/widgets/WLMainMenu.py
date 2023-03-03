from PyQt6.QtWidgets import QMenuBar

from actions import NewLyricAction, PreferencesAction
from actions.Lyrics import RefreshAction
from actions.SelectedLyrics import RemoveAction


class WLMainMenu(QMenuBar):
    
    def __init__(self):
        super().__init__()

        files_menu = self.addMenu("Arquivos")
        files_menu.addAction(NewLyricAction(self))
        files_menu.addAction(PreferencesAction(self))
        # self.addMenu("Editar")

        remove_lyric_menu = RemoveAction()
        remove_lyric_menu.setEnabled(False)

        refresh_menu = RefreshAction()

        lyrics_menu = self.addMenu("Letras")
        lyrics_menu.addAction(refresh_menu)
        lyrics_menu.addAction(remove_lyric_menu)
