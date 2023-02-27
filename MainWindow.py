import qtawesome as qta
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow

from actions import PreferencesAction
from actions.Lyrics import RefreshAction
from actions.NewLyricAction import NewLyricAction
from actions.SelectedLyrics import RemoveAction
from core import ApplicationContext, WebSocketServer
from entity.LyricLine import LyricLine
from structure import PresentationScreen
from widgets import LyricsWidget, SelectedListLyricsWidget, CurrentLyricWidget
from widgets.tab import Tab


def _on_change_verse(verse: LyricLine):
    content = verse.content
    WebSocketServer.send(content)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.refresh_menu = None
        self.lyric_menu = None
        self.remove_lyric_menu = None

        ApplicationContext.main_window = self
        self.setWindowTitle('Worship Lyrics')
        self.setMinimumSize(QSize(1024, 600))
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.menu_organizer()

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self._loaded_lyrics_tab())
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self._pre_selected_lyrics_tab())
        self.setDockOptions(QMainWindow.DockOption.AnimatedDocks | QMainWindow.DockOption.GroupedDragging)
        self.setCentralWidget(PresentationScreen())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self._selected_lyric_tab())

        ApplicationContext.lyrics_service.project_verse.subscribe(_on_change_verse)

    def _loaded_lyrics_tab(self) -> Tab:
        lyrics_tab = Tab(self, Qt.WindowType.WindowMinimizeButtonHint)
        lyrics_tab.setTitle('Letras', qta.icon('mdi.text-box-multiple', color='#42E8FF'))
        lyrics_tab.setBody(LyricsWidget(), False)

        return lyrics_tab

    def _pre_selected_lyrics_tab(self) -> Tab:
        pre_selected_lyrics_tab = Tab(self, Qt.WindowType.WindowMinimizeButtonHint)
        pre_selected_lyrics_tab.setTitle('Letras selecionadas', qta.icon('mdi.star', color='#FFE042'))
        pre_selected_lyrics_tab.setBody(SelectedListLyricsWidget(), False)

        return pre_selected_lyrics_tab

    def _selected_lyric_tab(self) -> Tab:
        lyric_bar_tab = Tab(self)
        lyric_bar_tab.setTitle('Letra selecionada', qta.icon('mdi.television-play', color='#30E842'))
        lyric_bar_tab.setBody(CurrentLyricWidget(), False)

        return lyric_bar_tab

    def menu_organizer(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("&Arquivos")
        file_menu.addAction(NewLyricAction(self))
        file_menu.addAction(PreferencesAction(self))

        self.remove_lyric_menu = RemoveAction()
        self.remove_lyric_menu.setEnabled(False)

        self.refresh_menu = RefreshAction()

        self.lyric_menu = menu.addMenu("&Letras")
        self.lyric_menu.addAction(self.refresh_menu)
        self.lyric_menu.addAction(self.remove_lyric_menu)

