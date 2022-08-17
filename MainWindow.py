from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow

from actions.NewFileAction import NewFileAction
from core import ApplicationContext, WebSocketServer
from structure import PresentationScreen
from widgets import LyricsWidget, SelectedListLyricsWidget, CurrentLyricWidget
from widgets.tab import Tab, TabTitle

window_style = """
background-color: #282A37;
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(window_style)
        self.setWindowTitle('Worship Lyrics')
        self.resize(QSize(1024, 600))

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

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(NewFileAction(self))

        ApplicationContext.lyric_handler.onChangeVerse(self._onChangeVerse)

    def _onChangeVerse(self, verse):
        content = verse['content']
        WebSocketServer.send(content)

