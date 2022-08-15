import sys
import threading

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

from actions.NewFileAction import NewFileAction
from core import ApplicationContext, MessageHandle, WebSocketServer
from structure import PresentationScreen
from widgets import LyricsWidget, SelectedListLyricsWidget, CurrentLyricWidget
from widgets.tab import Tab, TabTitle

from tornado import ioloop, web

app_style = """
QMainWindow::separator {
    border: 2px solid #111111;
}
"""

window_style = """
background-color: #282A37;
"""

context = ApplicationContext()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._runThread()

        # web_app = web.Application(
        #     [("/lyric/", WebSocketServer)],
        #     websocket_ping_interval=10,
        #     websocket_ping_timeout=30,
        # )
        #
        # web_app.listen(4041)
        # io_loop = ioloop.IOLoop.current()
        # io_loop.start()

        self.setStyleSheet(window_style)
        self.setWindowTitle('Worship Lyrics')
        self.resize(QSize(1024, 600))

        context.lyricsHandle().loadLyrics()
        lyrics_list = context.lyricsHandle().getLyricsList()

        lyrics_tab = Tab(self)
        lyrics_tab.setTitleBarWidget(TabTitle('Letras'))
        lyrics_tab.setBody(LyricsWidget(context, lyrics_list))

        selected_lyrics_tab = Tab(self)
        selected_lyrics_tab.setTitleBarWidget(TabTitle('Letras selecionadas'))
        selected_lyrics_tab.setBody(SelectedListLyricsWidget(context))

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, lyrics_tab)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, selected_lyrics_tab)
        self.setDockOptions(QMainWindow.DockOption.AnimatedDocks | QMainWindow.DockOption.GroupedDragging)

        self.setCentralWidget(PresentationScreen(context))

        lyric_bar_tab = Tab(self)
        lyric_bar_tab.setTitleBarWidget(TabTitle('Letra selecionada'))
        lyric_bar_tab.setBody(CurrentLyricWidget(context), False)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, lyric_bar_tab)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(NewFileAction(self))

        context.lyricsHandle().onChangeVerse(self._onChangeVerse)

    # TODO: É necessário passar isso para uma nova classe e organizar
    def _runThread(self):
        web_app = web.Application(
            [("/lyric/", WebSocketServer)],
            websocket_ping_interval=10,
            websocket_ping_timeout=30,
        )

        web_app.listen(4041)
        self.thread = threading.Thread(target=ioloop.IOLoop.current().start)
        self.thread.daemon = True
        self.thread.start()

    def _onChangeVerse(self, verse):
        content = verse['content']
        WebSocketServer.send(content)


app = QApplication(sys.argv)
app.setStyleSheet(app_style)
app.setDesktopSettingsAware(True)

window = MainWindow()
window.show()

app.exec()

