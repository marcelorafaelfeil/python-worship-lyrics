from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow

from actions.NewFileAction import NewFileAction
from core import ApplicationContext, WebSocketServer
from structure import PresentationScreen
from widgets import LyricsWidget, SelectedListLyricsWidget, CurrentLyricWidget
from widgets.tab import Tab, TabTitle
from actions.SelectedLyrics import RemoveAction
from actions.Lyrics import RefreshAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.refresh_menu = None
        self.lyric_menu = None
        self.remove_lyric_menu = None

        ApplicationContext.main_window = self
        self.setWindowTitle('Worship Lyrics')
        self.resize(QSize(1024, 600))
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.menuOrganizer()

        lyrics_list = ApplicationContext.lyric_handler.getLyricsList()

        lyrics_tab = Tab(self)
        lyrics_tab.setTitleBarWidget(TabTitle('Letras'))
        lyrics_tab.setBody(LyricsWidget(lyrics_list), False)

        selected_lyrics_tab = Tab(self)
        selected_lyrics_tab.setTitleBarWidget(TabTitle('Letras selecionadas'))
        selected_lyrics_tab.setBody(SelectedListLyricsWidget(), False)

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, lyrics_tab)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, selected_lyrics_tab)
        self.setDockOptions(QMainWindow.DockOption.AnimatedDocks | QMainWindow.DockOption.GroupedDragging)

        self.setCentralWidget(PresentationScreen())

        lyric_bar_tab = Tab(self)
        lyric_bar_tab.setTitleBarWidget(TabTitle('Letra selecionada'))
        lyric_bar_tab.setBody(CurrentLyricWidget(), False)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, lyric_bar_tab)

        ApplicationContext.lyric_handler.onChangeVerse(self._onChangeVerse)

    def menuOrganizer(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("&Arquivos")
        file_menu.addAction(NewFileAction(self))

        self.remove_lyric_menu = RemoveAction()
        self.remove_lyric_menu.setEnabled(False)

        self.refresh_menu = RefreshAction()

        self.lyric_menu = menu.addMenu("&Letras")
        self.lyric_menu.addAction(self.refresh_menu)
        self.lyric_menu.addAction(self.remove_lyric_menu)

    def _onChangeVerse(self, verse):
        content = verse['content']
        WebSocketServer.send(content)

